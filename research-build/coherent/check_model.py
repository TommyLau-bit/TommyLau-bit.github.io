"""Recalculate the Coherent model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/coherent.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/cohr_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

Qt, An, V, S, G, Ca, Pe, C = (wb[n] for n in ["Quarters", "Annual", "Valuation", "Scenarios", "Sensitivity", "Cash", "Peers", "Cover"])
checks = [
    ("Q1 FY27E EPS", Qt["J14"].value, 1.99, 2), ("Q1 guide mid EPS", Qt["J17"].value, 1.95, 2),
    ("Q4 FY26 D&C share", Qt["I8"].value, 0.79, 2), ("Q1 FY25 D&C share", Qt["B8"].value, 0.64, 2),
    ("D&C growth FY26", Qt["B19"].value, 0.405, 3),
    ("FY27 revenue", An["E5"].value, 10420, 0), ("FY28 revenue", An["F5"].value, 13025, 0),
    ("FY27 growth", An["E6"].value, 0.464, 3), ("FY26 growth", An["D6"].value, 0.225, 3),
    ("FY27 GM", An["E7"].value, 0.413, 3), ("FY27 op margin", An["E9"].value, 0.243, 3), ("FY28 op margin", An["F9"].value, 0.255, 3),
    ("FY27 EPS", An["E15"].value, 9.56, 2), ("FY28 EPS", An["F15"].value, 12.53, 2),
    ("FY27 EPS growth", An["E16"].value, 0.704, 3), ("FY28 EPS growth", An["F16"].value, 0.310, 3),
    ("FY27 vs cons", An["E18"].value, 0.017, 3), ("FY28 vs cons", An["F18"].value, -0.099, 3),
    ("FY28 rev vs cons", An["F20"].value, -0.113, 3), ("DC share FY26", An["D22"].value, 0.741, 3),
    ("DC seg margin FY25", An["C23"].value, 0.241, 3), ("DC seg margin FY26", An["D23"].value, 0.252, 3),
    ("Base value", V["B7"].value, 275.60, 2), ("Base vs price", V["B9"].value, 0.310, 3), ("Band", V["B10"].value, "LONG", None),
    ("Target vs price", V["B12"].value, 0.308, 3),
    ("Market value", V["B14"].value, 41.19, 2), ("Net debt", V["B15"].value, 1235, 0), ("EV", V["B16"].value, 42.76, 2),
    ("PE FY26", V["B17"].value, 37.5, 1), ("PE cons 27", V["B18"].value, 22.4, 1), ("PE cons 28", V["B19"].value, 15.1, 1),
    ("PE 27E", V["B20"].value, 22.0, 1), ("PE 28E", V["B21"].value, 16.8, 1),
    ("EPS needed", V["B22"].value, 9.56, 2), ("Needed vs FY27E", V["B23"].value, 0.0, 2),
    ("Long below", V["B24"].value, 240, 0), ("Short above", V["B25"].value, 367, 0),
    ("Off high", V["B26"].value, -0.507, 3), ("YTD", V["B27"].value, 0.140, 3), ("vs Nvidia", V["B28"].value, -0.181, 3),
    ("Cons TP vs price", V["B29"].value, 0.859, 3),
    ("Bear EPS", S["H5"].value, 7.48, 2), ("Bear value", S["I5"].value, 105, 0), ("Bear chg", S["J5"].value, -0.502, 3),
    ("Base value scen", S["I6"].value, 276, 0), ("Bull EPS", S["H7"].value, 15.23, 2), ("Bull value", S["I7"].value, 426, 0),
    ("Bull chg", S["J7"].value, 1.027, 3), ("Weighted", S["E11"].value, 271, 0), ("Weighted chg", S["F11"].value, 0.287, 3),
    ("Base check", S["E12"].value, 0, 6),
    ("Grid above", G["B9"].value, 7, 0), ("Grid 15%", G["B10"].value, 6, 0),
    ("FCF FY26", Ca["D7"].value, -1023, 0), ("Inventory growth", Ca["D10"].value, 0.795, 3),
    ("Peer median", Pe["C13"].value, 30.4, 1), ("Hist fwd PE", Pe["C14"].value, 24.3, 1),
    ("Cover band", C["B5"].value, "LONG", None),
]
grid = [[171, 209, 247], [225, 276, 326], [270, 330, 390]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and not isinstance(got, str) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:24s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
