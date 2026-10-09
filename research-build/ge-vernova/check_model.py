"""Recalculate the GE Vernova model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/ge-vernova.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):  # Excel-style half-up rounding, as the cells display
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/5eb25e34-4358-449f-9a62-dbe67b3de501/scratchpad/gev_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

F, V, S, G, Qu, Pe, C = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Queue", "Peers", "Cover"])
# Figures as printed in the note and the md
checks = [
    ("2025 growth", F["C6"].value, 0.09, 2), ("2026 growth", F["D6"].value, 0.21, 2),
    ("2024 margin", F["B7"].value, 0.058, 3), ("2025 margin", F["C7"].value, 0.084, 3),
    ("2026 EBITDA", F["D8"].value, 5.98, 2), ("2027E revenue", F["E5"].value, 51.06, 2), ("2027E EBITDA", F["E8"].value, 8.42, 2),
    ("2028E revenue", F["F5"].value, 56.68, 2), ("2028E EBITDA", F["F8"].value, 11.34, 2), ("2028 outlook EBITDA", F["G8"].value, 11.20, 2),
    ("FCF/EBITDA 2026", F["D11"].value, 2.0, 1),
    ("EV/EBITDA 2026", F["D12"].value, 43.3, 1), ("EV/EBITDA 2027E", F["E12"].value, 30.7, 1),
    ("EV/EBITDA 2028E", F["F12"].value, 22.8, 1), ("EV/EBITDA outlook", F["G12"].value, 23.1, 1),
    ("Net cash", V["B8"].value, 10.27, 2), ("Diluted shares", V["B9"].value, 269.3, 1),
    ("Base value", V["B10"].value, 1048, 0), ("Base vs price", V["B12"].value, 0.049, 3),
    ("Band", V["B13"].value, "NO CALL", None), ("Market value", V["B15"].value, 269.2, 1), ("EV", V["B16"].value, 258.9, 1),
    ("Needed 2028 EBITDA", V["B17"].value, 10.79, 2), ("Needed vs outlook", V["B18"].value, 0.96, 2),
    ("P/E cons 2026", V["B20"].value, 66.4, 1), ("P/E cons 2027", V["B21"].value, 39.7, 1),
    ("FCF yield 2026", V["B22"].value, 0.045, 3), ("Revisit long", V["B23"].value, 911, 0), ("Revisit short", V["B24"].value, 1398, 0),
    ("Off high close", V["B25"].value, -0.149, 3), ("Contract liabilities / cash", V["B26"].value, 3.0, 1),
    ("Bear 2028 EBITDA", S["G5"].value, 8.79, 2), ("Bear value", S["I5"].value, 560, 0), ("Bear chg", S["J5"].value, -0.44, 2),
    ("Base value (scenario)", S["I6"].value, 1048, 0),
    ("Bull 2028 EBITDA", S["G7"].value, 13.38, 2), ("Bull value", S["I7"].value, 1529, 0), ("Bull chg", S["J7"].value, 0.53, 2),
    ("Weighted", S["E11"].value, 1046, 0), ("Weighted vs price", S["F11"].value, 0.047, 3),
    ("Grid cells above price", G["B9"].value, 6, 0), ("Grid cells 15% above", G["B10"].value, 3, 0),
    ("Years Q2 26", Qu["G10"].value, 5.8, 1), ("Years Q4 25", Qu["E10"].value, 4.15, 2),
    ("Signed H1 26", Qu["B19"].value, 41, 0), ("Shipped H1 26", Qu["B20"].value, 7, 0), ("Queue growth H1", Qu["B21"].value, 0.40, 2),
    ("Floor 2028", Qu["C26"].value, 96, 0), ("Floor 2030", Qu["C27"].value, 120, 0),
    ("Power CL rise H1", Qu["B32"].value, 0.67, 2), ("Power CL x Dec 24", Qu["B33"].value, 2.9, 1), ("Power CL vs revenue", Qu["B34"].value, 1.4, 1),
    ("Peer median P/E", Pe["C12"].value, 24.0, 1), ("Peer median EV/EBITDA", Pe["D12"].value, 18.4, 1),
    ("Cover view", C["B5"].value, "NO CALL", None),
]
grid = [[744, 885, 1026], [880, 1048, 1217], [1003, 1197, 1390]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:28s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
