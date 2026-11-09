"""Recalculate the Broadcom model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures printed in the note and src/content/calls/broadcom.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP


def rnd(x, dp):  # Excel-style half-up rounding, as the cells display
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))

from data import *

TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/87f9daa0-8062-414d-a40b-cb592166359f/scratchpad/avgo_recalc")
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

F, V, S, G, Qt, Pe = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Peers"])
# Figures as published in the note and the md
checks = [
    ("AI growth Q3 FY26", Qt["B22"].value, 2.21, 2), ("AI share Q3 FY26", Qt["B23"].value, 0.56, 2),
    ("Custom Q3 FY26", Qt["B24"].value, 12.2, 1), ("Networking Q3 FY26", Qt["B25"].value, 4.5, 1),
    ("GM change, points", Qt["B26"].value, -3.4, 1), ("Semi op margin Q3", Qt["B27"].value, 0.613, 3),
    ("SW op margin Q3", Qt["B28"].value, 0.837, 3), ("Q4 EPS", Qt["I19"].value, 3.81, 2),
    ("Q3 FY25 GM", Qt["D14"].value, 0.784, 3), ("Q3 FY26 GM", Qt["H14"].value, 0.750, 3), ("Q3 FY26 OM", Qt["H16"].value, 0.679, 3),
    ("FY24 GM", F["B11"].value, 0.765, 3), ("FY25 GM", F["C11"].value, 0.786, 3), ("FY26 GM", F["D11"].value, 0.751, 3),
    ("FY24 OM", F["B15"].value, 0.596, 3), ("FY25 OM", F["C15"].value, 0.657, 3),
    ("FY26 revenue", F["D9"].value, 105.9, 1), ("FY26 AI", F["D5"].value, 57.6, 1), ("FY26 non-AI", F["D6"].value, 16.8, 1),
    ("FY26 software", F["D8"].value, 31.4, 1), ("FY26 op income", F["D14"].value, 70.8, 1), ("FY26 OM", F["D15"].value, 0.669, 3),
    ("FY26 EPS", F["D20"].value, 11.62, 2),
    ("FY27 revenue", F["E9"].value, 166.0, 1), ("FY27 op income", F["E14"].value, 106.6, 1), ("FY27 OM", F["E15"].value, 0.642, 3),
    ("FY27 EPS", F["E20"].value, 17.76, 2), ("FY27 vs consensus", F["E24"].value, -0.08, 2), ("FY27 rev vs cons", F["E26"].value, -0.05, 2),
    ("FY28 revenue", F["F9"].value, 243.5, 1), ("FY28 op income", F["F14"].value, 149.4, 1), ("FY28 OM", F["F15"].value, 0.614, 3),
    ("FY28 EPS", F["F20"].value, 25.15, 2),
    ("P/E FY25", F["C22"].value, 53, 0), ("P/E FY26", F["D22"].value, 31, 0), ("P/E FY27", F["E22"].value, 20, 0),
    ("P/E FY28", F["F22"].value, 14, 0), ("P/E cons FY27", F["E25"].value, 19, 0),
    ("Net debt", V["B6"].value, 35.4, 1), ("Chip value/share", V["B7"].value, 410, 0), ("Software value/share", V["B8"].value, 83, 0),
    ("Net debt/share", V["B9"].value, 7, 0),
    ("Base value", V["B10"].value, 486, 0), ("Base vs price", V["B12"].value, 0.34, 2), ("Weighted", V["B13"].value, 461, 0),
    ("Rule on value", V["B14"].value, "LONG", None), ("Draft view", V["B15"].value, "LONG", None), ("Target", V["B16"].value, 485, 0),
    ("Market value", V["B17"].value, 1731, 0), ("EV", V["B18"].value, 1766, 0),
    ("Since piece", V["B19"].value, 0.055, 3), ("Off high close", V["B20"].value, -0.25, 2),
    ("P/E at $30", V["B27"].value, 12, 0),
    ("Need AI FY28", V["B30"].value, 127, 0), ("Need growth", V["B31"].value, 0.11, 2),
    ("Cut vs mgmt", V["B32"].value, 0.17, 2), ("FY28 vs FY27 AI", V["B33"].value, 0.65, 2), ("No-call price", V["B34"].value, 423, 0),
    ("Bear EPS", S["I5"].value, 16.39, 2), ("Bear value", S["L5"].value, 226, 0), ("Bear chg", S["M5"].value, -0.38, 2),
    ("Base (scenario)", S["L6"].value, 486, 0), ("Base EPS (scenario)", S["I6"].value, 25.15, 2),
    ("Bull EPS", S["I7"].value, 29.94, 2), ("Bull value", S["L7"].value, 647, 0), ("Bull chg", S["M7"].value, 0.79, 2),
    ("Weighted (scenario)", S["L12"].value, 461, 0), ("Weighted vs price", S["M12"].value, 0.27, 2),
    ("Grid cells above price", G["B9"].value, 8, 0), ("Grid cells 15% above", G["B10"].value, 6, 0),
    ("Chip peer median", Pe["C12"].value, 20.7, 1), ("Software peer median", Pe["C19"].value, 17.4, 1),
]
grid = [[341, 407, 474], [404, 486, 568], [467, 565, 663]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:30s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)   # publish the recalculated file so previews show values
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
