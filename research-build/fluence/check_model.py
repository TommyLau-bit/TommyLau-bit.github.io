"""Recalculate the Fluence model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/fluence.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):  # Excel-style half-up rounding, as the cells display
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/cd10b0e0-d2a1-4252-8640-5eea98c6183e/scratchpad/flnc_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

F, V, S, G, Qu, Pe, C = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarters", "Peers", "Cover"])
# Figures as printed in the note and the md
checks = [
    ("FY25 growth", F["C6"].value, -0.16, 2), ("FY26 growth", F["D6"].value, 0.06, 2),
    ("FY24 adj GM", F["B7"].value, 0.129, 3), ("FY25 adj GM", F["C7"].value, 0.137, 3),
    ("FY24 opex", F["B9"].value, 270, 0), ("FY25 opex", F["C9"].value, 290, 0),
    ("FY24 EBITDA margin", F["B11"].value, 0.029, 3), ("FY25 EBITDA margin", F["C11"].value, 0.009, 3),
    ("FY26 EBITDA margin", F["D11"].value, -0.083, 3),
    ("FY27E revenue", F["E5"].value, 3000, 0), ("FY27E EBITDA", F["E10"].value, 20, 0), ("FY27E margin", F["E11"].value, 0.007, 3),
    ("FY28E revenue", F["F5"].value, 3600, 0), ("FY28E EBITDA", F["F10"].value, 148, 0), ("FY28E margin", F["F11"].value, 0.041, 3),
    ("EV/rev FY26", F["D13"].value, 0.64, 2), ("EV/rev FY27E", F["E13"].value, 0.51, 2), ("EV/rev FY28E", F["F13"].value, 0.43, 2),
    ("Net debt Sep est", V["B8"].value, 165, 0), ("Shares", V["B9"].value, 184.6, 1),
    ("Base value", V["B10"].value, 7.88, 2), ("Base vs price", V["B12"].value, 0.06, 2),
    ("Band", V["B13"].value, "NO CALL", None), ("Market value", V["B15"].value, 1370, -1), ("EV", V["B16"].value, 1540, -1),
    ("EV/S consensus FY27", V["B20"].value, 0.47, 2), ("Base EV/EBITDA", V["B23"].value, 11, 0),
    ("Revisit long", V["B24"].value, 6.85, 2), ("Revisit short", V["B25"].value, 10.51, 2),
    ("Off high close", V["B26"].value, -0.77, 2), ("Net debt June", V["B27"].value, 35, 0), ("Cons Q4 FCF", V["B28"].value, -133, 0),
    ("Bear FY28 revenue", S["G5"].value, 2904, 0), ("Bear EBITDA", S["H5"].value, 28, 0), ("Bear value", S["J5"].value, 3.04, 2), ("Bear chg", S["K5"].value, -0.59, 2),
    ("Base value (scenario)", S["J6"].value, 7.88, 2), ("Base EBITDA", S["H6"].value, 148, 0),
    ("Bull FY28 revenue", S["G7"].value, 4212, 0), ("Bull EBITDA", S["H7"].value, 291, 0), ("Bull EV/EBITDA", S["I7"].value, 10, 0),
    ("Bull value", S["J7"].value, 15.08, 2), ("Bull chg", S["K7"].value, 1.03, 2),
    ("Weighted", S["E11"].value, 8.47, 2), ("Weighted vs price", S["F11"].value, 0.14, 2),
    ("Grid cells above price", G["B9"].value, 5, 0), ("Grid cells 15% above", G["B10"].value, 3, 0),
    ("Nine-month opex", Qu["B16"].value, 208, 0), ("Americas share", Qu["B18"].value, 0.56, 2),
    ("Implied Q4 revenue", Qu["B21"].value, 810, 0), ("Implied Q4 EBITDA", Qu["B22"].value, -109, 0),
    ("GW contracted change", Qu["D26"].value, 1.21, 2), ("Pipeline change", Qu["D27"].value, 0.34, 2),
    ("Q3 FY26 gross margin", Qu["H7"].value, 0.051, 3), ("Q3 FY25 gross margin", Qu["D7"].value, 0.148, 3),
    ("Peer median EV/sales", Pe["C12"].value, 2.36, 2), ("Peer median EV/EBITDA", Pe["D12"].value, 13.0, 1),
    ("Cover view", C["B5"].value, "NO CALL", None),
]
grid = [[4.79, 6.42, 8.04], [5.93, 7.88, 9.83], [7.07, 9.34, 11.62]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 2))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (isinstance(got, (int, float)) and rnd(got, dp) == rnd(want, dp))
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
