"""Recalculate the Wärtsilä model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/wartsila.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/wrt_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

Sg, E, V, S, Se, Pe, C = (wb[n] for n in ["Segments", "Energy", "Valuation", "Scenarios", "Sensitivity", "Peers", "Cover"])
# Figures as printed in the note and the md
checks = [
    ("Energy sales 2026E", Sg["J5"].value, 2384, 0), ("Energy margin 2026E", Sg["L5"].value, 0.163, 3),
    ("Marine sales 2026E", Sg["J6"].value, 3575, 0), ("Marine margin 2026E", Sg["L6"].value, 0.130, 3),
    ("Group sales 2026E", Sg["J8"].value, 6218, 0), ("Group result 2026E", Sg["K8"].value, 877, 0),
    ("Energy sales 2027E", Sg["M5"].value, 2908, 0), ("Marine sales 2027E", Sg["M6"].value, 3754, 0),
    ("Group sales 2027E", Sg["M8"].value, 6662, 0), ("Group result 2027E", Sg["N8"].value, 997, 0),
    ("Energy growth 2026E", Sg["J10"].value, 0.16, 2), ("EPS 2027E", Sg["B20"].value, 1.27, 2),
    ("Energy 9M orders/sales", E["B17"].value, 2.50, 2), ("MW 9M 2026", E["B18"].value, 4150, 0),
    ("MW growth 9M", E["B20"].value, 1.30, 2), ("DC MW 9M", E["B21"].value, 1911, 0), ("DC share 9M", E["B22"].value, 0.46, 2),
    ("DC share 2025", E["B25"].value, 0.34, 2), ("DC share Q2", E["G13"].value, 0.62, 2), ("DC share Q3", E["H13"].value, 0.25, 2),
    ("DC share Q1", E["F13"].value, 0.40, 2),
    ("Eq orders/sales", E["B28"].value, 3.9, 1), ("Book later", E["B31"].value, 4.9e3, -2), ("Book x 2025 sales", E["B32"].value, 2.7, 1),
    ("Book growth", E["B33"].value, 0.87, 2),
    ("Energy result 2027E", V["B5"].value * 1000, 509, 0), ("Marine result 2027E", V["B6"].value * 1000, 488, 0),
    ("SOTP Energy", V["D5"].value, 9.16, 2), ("SOTP Marine", V["D6"].value, 6.83, 2),
    ("Net cash", V["D9"].value, 1.92, 2), ("Bridge", V["D13"].value, 1.91, 2), ("Equity", V["D14"].value, 17.91, 2),
    ("Shares", V["D15"].value, 589.8, 1), ("Base value", V["D16"].value, 30.36, 2), ("Base vs price", V["D18"].value, 0.18, 2),
    ("Band", V["D19"].value, "LONG", None), ("Mcap", V["D21"].value, 15.1, 1), ("EV", V["D22"].value, 13.2, 1),
    ("EV/2026E", V["D23"].value, 15.1, 1), ("EV/2027E", V["D24"].value, 13.2, 1), ("PE cons 27", V["D25"].value, 19.6, 1),
    ("Implied Energy x", V["D27"].value, 12.5, 1), ("Implied Marine x", V["D28"].value, 8.3, 1),
    ("No call above", V["D29"].value, 26.40, 2), ("Energy share", V["D30"].value, 0.51, 2), ("Marine share", V["D31"].value, 0.38, 2),
    ("Off record", V["D32"].value, -0.35, 2), ("Marine share of 2025 result", V["D33"].value, 0.55, 2),
    ("Bear value", S["I5"].value, 19.36, 2), ("Bear chg", S["J5"].value, -0.24, 2), ("Bear Energy result", S["H5"].value * 1000, 399, 0),
    ("Base scen", S["I6"].value, 30.36, 2), ("Bull value", S["I7"].value, 38.64, 2), ("Bull chg", S["J7"].value, 0.51, 2),
    ("Bull Energy result", S["H7"].value * 1000, 573, 0), ("Weighted", S["E11"].value, 29.68, 2),
    ("Target vs price", CALL["target"] / PRICE - 1, 0.17, 2),
    ("Grid above", Se["B9"].value, 8, 0), ("Grid 15%", Se["B10"].value, 5, 0),
    ("Peer engine median EV/EBIT", Pe["D13"].value, 20.7, 1), ("Peer engine median fwd PE", Pe["C13"].value, 20.8, 1),
    ("Cover", C["B5"].value, "LONG", None),
]
grid = [[23.56, 27.88, 32.19], [26.05, 30.36, 34.68], [28.53, 32.84, 37.16]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", Se.cell(row=5 + i, column=2 + j).value, grid[i][j], 2))
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
