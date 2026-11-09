"""Recalculate the Lumentum model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures printed in the note and src/content/calls/lumentum.md."""
import subprocess, sys, os, shutil, openpyxl
from data import *

TMP = os.environ.get("RECALC_DIR", "/tmp/lite_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX],
               check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

F, V, S, G, Qt, Sh, Pe = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Shares", "Peers"])
# Figures as published in the note and the md
checks = [
    ("Q1 FY27E EPS", Qt["J15"].value, 4.25, 2), ("Q2 FY27E EPS", Qt["K15"].value, 4.96, 2),
    ("Q3 FY27E EPS", Qt["L15"].value, 5.63, 2), ("Q4 FY27E EPS", Qt["M15"].value, 6.31, 2),
    ("TTM EPS", Qt["B18"].value, 8.37, 2), ("Rev growth Q4 FY26", Qt["B19"].value, 1.09, 2),
    ("Components growth", Qt["B20"].value, 1.03, 2), ("Systems growth", Qt["B21"].value, 1.23, 2),
    ("GAAP GM rise, points", Qt["B22"].value, 14.1, 1),
    ("FY24 growth", F["B6"].value, -0.23, 2), ("FY25 growth", F["C6"].value, 0.21, 2), ("FY26 growth", F["D6"].value, 0.83, 2),
    ("FY27E revenue", F["E5"].value, 6.12, 2), ("FY27E growth", F["E6"].value, 1.03, 2),
    ("FY27E op income", F["E9"].value, 2.52, 2), ("FY27E op margin", F["E10"].value, 0.412, 3), ("FY27E EPS", F["E15"].value, 21.14, 2),
    ("FY28E revenue", F["F5"].value, 8.26, 2), ("FY28E op income", F["F9"].value, 3.43, 2), ("FY28E EPS", F["F15"].value, 28.28, 2),
    ("FY28 shares m", F["F14"].value * 1000, 103.0, 1),
    ("P/E FY26", F["D17"].value, 126, 0), ("P/E FY27E", F["E17"].value, 52, 0), ("P/E FY28E", F["F17"].value, 39, 0),
    ("Mine vs cons FY27", F["E19"].value, -0.03, 2), ("Mine vs cons FY28", F["F19"].value, -0.14, 2),
    ("P/E cons FY27", F["E20"].value, 50, 0), ("P/E cons FY28", F["F20"].value, 33, 0),
    ("Base value", V["B7"].value, 990, 0), ("Base vs price", V["B9"].value, -0.09, 2),
    ("Rule on value", V["B11"].value, "NO CALL", None), ("Draft view", V["B12"].value, "NO CALL", None),
    ("Market value", V["B13"].value, 98, 0), ("Market value with pref", V["B14"].value, 101, 0),
    ("Net cash", V["B15"].value, 1.09, 2), ("EV", V["B16"].value, 100, 0),
    ("Since low close", V["B17"].value, 6.30, 2), ("Since Dec 25", V["B18"].value, 1.96, 2),
    ("P/E TTM", V["B23"].value, 130, 0), ("P/E Q1 run-rate", V["B24"].value, 65, 0),
    ("Needed EPS FY28", V["B26"].value, 31.19, 2), ("Needed revenue FY28", V["B28"].value, 9.1, 1),
    ("Needed growth", V["B29"].value, 0.49, 2), ("Needed x FY26", V["B30"].value, 3.0, 1),
    ("Consensus revenue FY28", V["B31"].value, 9.7, 1),
    ("Revisit long", V["B32"].value, 860, -1), ("Revisit short", V["B33"].value, 1320, -1),
    ("Notes principal", Sh["B9"].value, 1.55, 2), ("Notes net shares m", (Sh["D9"].value - Sh["B12"].value) * 1000, 6.0, 1),
    ("Awards m", Sh["B15"].value * 1000, 3.1, 1), ("My diluted count m", Sh["B16"].value * 1000, 101.7, 1),
    ("Net cash (Shares)", Sh["B20"].value, 1.09, 2), ("Nvidia stake", Sh["B22"].value, 3.1, 1), ("Nvidia gain", Sh["B23"].value, 0.57, 2),
    ("Preferred share", Sh["B24"].value, 0.03, 2),
    ("Bear EPS", S["G5"].value, 18.49, 2), ("Bear value", S["I5"].value, 407, 0), ("Bear chg", S["J5"].value, -0.63, 2),
    ("Bear revenue", S["D5"].value, 6.73, 2),
    ("Base EPS (scenario)", S["G6"].value, 28.28, 2), ("Base (scenario)", S["I6"].value, 990, 0),
    ("Bull EPS", S["G7"].value, 35.09, 2), ("Bull value", S["I7"].value, 1474, 0), ("Bull chg", S["J7"].value, 0.35, 2),
    ("Bull revenue", S["D7"].value, 9.5, 1),
    ("Weighted", S["I12"].value, 965, 0), ("Weighted vs price", S["J12"].value, -0.12, 2),
    ("Grid cells above price", G["B9"].value, 3, 0),
    ("Peer median", Pe["C12"].value, 35.5, 1),
]
grid = [[616, 770, 924], [792, 990, 1188], [980, 1225, 1470]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and round(got, dp) == round(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:28s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)   # publish the recalculated file so previews show values
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
