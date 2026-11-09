"""Recalculate the SpaceX model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures printed in the note (src/content/calls/spacex.md and the PDF)."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/spx_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

Sg, V, S, G, O, C = (wb[n] for n in ["Segments", "Valuation", "Scenarios", "Sensitivity", "Orbit", "Cover"])
# find scenario rows by label
srow = {S.cell(row=r, column=1).value: r for r in range(1, 60)}
VR = srow["Value per share, US$"]; CR = VR + 1; WR = srow["Probability-weighted value, US$"]
checks = [  # name, model value, figure in the note, decimals
    ("Check 2024 total", Sg["B19"].value, 0, 6), ("Check 2025 total", Sg["C19"].value, 0, 6), ("Check 9M26", Sg["D19"].value, 0, 6),
    ("2026E revenue bn", Sg["F17"].value / 1000, 49.3, 1), ("2027E revenue bn", Sg["G17"].value / 1000, 167.0, 1),
    ("Space 2026E bn", Sg["F5"].value / 1000, 4.7, 1), ("Conn 2026E bn", Sg["F9"].value / 1000, 18.6, 1),
    ("SI 2026E bn", Sg["F13"].value / 1000, 25.9, 1), ("Conn EBITDA 26E", Sg["F10"].value / 1000, 12.1, 1),
    ("SI EBITDA 26E", Sg["F14"].value / 1000, 12.2, 1), ("Conn EBITDA 27E", Sg["G10"].value / 1000, 17.7, 1),
    ("SI EBITDA 27E", Sg["G14"].value / 1000, 64.8, 1), ("2027E vs cons", Sg["G21"].value, -0.07, 2),
    ("SI margin Q2", Sg["D31"].value, 0.45, 2), ("SI margin Q3", Sg["E31"].value, 0.66, 2), ("Conn margin Q3", Sg["E32"].value, 0.67, 2),
    ("SOTP Conn bn", V["D5"].value / 1000, 442, 0), ("SOTP SI bn", V["D6"].value / 1000, 842, 0), ("SOTP Space bn", V["D7"].value / 1000, 90, 0),
    ("Conn per share", V["F5"].value, 32.5, 1), ("SI per share", V["F6"].value, 62.0, 1), ("Space per share", V["F7"].value, 6.6, 1),
    ("Net cash bn", V["D9"].value / 1000, 51.0, 1), ("Net cash ps", V["F9"].value, 3.8, 1), ("Options ps", V["F10"].value, 7.4, 1),
    ("Three businesses tn", V["D8"].value / 1e6, 1.37, 2), ("Equity bn", V["D13"].value / 1000, 1525, 0),
    ("Shares m", V["D14"].value, 13581, 0), ("Base value", V["D15"].value, 112.3, 1), ("Base vs price", V["D17"].value, -0.17, 2),
    ("Band", V["D18"].value, "NO CALL", None), ("Mcap tn", V["D21"].value / 1e6, 1.83, 2), ("EV tn", V["D22"].value / 1e6, 1.78, 2),
    ("Gap bn", V["D23"].value / 1000, 404, 0), ("Gap share", V["D24"].value, 0.23, 2), ("Gap after options bn", V["D26"].value / 1000, 304, 0),
    ("Gap after options ps", V["D27"].value, 22, 0), ("SI per GW bn", V["D28"].value / 1000, 65, 0), ("Gap GW", V["D29"].value, 6.2, 1),
    ("Sats", V["D30"].value, 36000, -3), ("Tonnes AI1", V["D31"].value, 83000, -3), ("x 2025 mass", V["D33"].value, 38, 0),
    ("PE 27 cons", V["D36"].value, 33.4, 1), ("EV/rev 27 cons", V["D37"].value, 9.9, 1),
    ("Revisit short", V["D41"].value, 150, 0), ("Revisit long", V["D42"].value, 98, 0),
    ("Bear", S.cell(row=VR, column=2).value, 45, 0), ("Bull", S.cell(row=VR, column=4).value, 203, 0),
    ("Base scen", S.cell(row=VR, column=3).value, 112, 0), ("Bear chg", S.cell(row=CR, column=2).value, -0.66, 2),
    ("Bull chg", S.cell(row=CR, column=4).value, 0.50, 2), ("Weighted", S.cell(row=WR, column=2).value, 118, 0),
    ("Weighted chg", S.cell(row=WR, column=3).value, -0.12, 2), ("Base link check", S.cell(row=WR + 1, column=2).value, 0, 6),
    ("Grid above", G["B9"].value, 1, 0), ("Grid short", G["B10"].value, 3, 0), ("Grid long", G["B11"].value, 0, 0),
    ("AI1 vs target", O["B5"].value, 0.75, 2), ("AI1 shortfall", O["B6"].value, 0.25, 2), ("AI1 mass t", O["B8"].value, 2.3, 1),
    ("Radiator flux", O["B9"].value, 1094, 0), ("ISS radiator t", O["B10"].value, 2.2, 1), ("Solar m2", O["B11"].value, 840, 0),
    ("Per kg 9M26", O["B19"].value, 8400, -2), ("Per kg x200", O["B20"].value, 42, 0),
    ("Cover band", C["B8"].value, "NO CALL", None),
]
grid = [[89, 100, 112], [98, 112, 127], [108, 125, 142]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))
kg = [7547, 5568, 9009, 7333, 7448, 9496]
for j in range(6):
    checks.append((f"Per kg {KG_LABELS[j]}", O.cell(row=17, column=2 + j).value, kg[j], 0))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:22s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
