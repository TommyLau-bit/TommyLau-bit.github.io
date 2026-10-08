"""Recalculate the Marvell model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures printed in the note and src/content/calls/marvell.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP


def rnd(x, dp):  # Excel-style half-up rounding, as the cells display
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))

from data import *

TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/5a1d5bb1-c55c-4427-9f09-a6f027895cd6/scratchpad/mrvl_recalc")
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

F, V, S, G, Qt, Dc, Pe = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "DataCentre", "Peers"])
# Figures as published in the note and the md
checks = [
    ("Q3 FY27E EPS", Qt["L15"].value, 1.10, 2), ("Q4 FY27E revenue", Qt["M5"].value, 3.69, 2),
    ("Q4 FY27E op margin", Qt["M12"].value, 0.388, 3), ("Q4 FY27E EPS", Qt["M15"].value, 1.35, 2),
    ("DC growth Q2 FY27", Qt["B19"].value, 0.46, 2), ("DC share Q2 FY27", Qt["B20"].value, 0.79, 2),
    ("DC share Q4 FY26", Qt["B21"].value, 0.74, 2), ("NG GM change, points", Qt["B24"].value, -3.5, 1),
    ("FY25 growth", F["C6"].value, 0.05, 2), ("FY26 growth", F["D6"].value, 0.42, 2),
    ("FY27E revenue", F["E5"].value, 12.00, 2), ("FY27E growth", F["E6"].value, 0.46, 2),
    ("FY27E gross margin", F["E8"].value, 0.584, 3), ("FY27E op margin", F["E11"].value, 0.371, 3), ("FY27E EPS", F["E16"].value, 4.18, 2),
    ("FY28E revenue", F["F5"].value, 20.00, 2), ("FY28E growth", F["F6"].value, 0.67, 2),
    ("FY28E op margin", F["F11"].value, 0.410, 3), ("FY28E EPS", F["F16"].value, 7.54, 2),
    ("FY29E revenue", F["G5"].value, 28.00, 2), ("FY29E op margin", F["G11"].value, 0.43, 2), ("FY29E EPS", F["G16"].value, 10.78, 2),
    ("P/E FY26", F["D18"].value, 100, 0), ("P/E FY27E", F["E18"].value, 68, 0), ("P/E FY28E", F["F18"].value, 38, 0),
    ("P/E FY29E", F["G18"].value, 26, 0), ("P/E cons FY27", F["E21"].value, 67, 0), ("P/E cons FY28", F["F21"].value, 42, 0),
    ("DC FY27E", Dc["C5"].value, 9.75, 2), ("DC FY28E", Dc["D5"].value, 18.00, 2),
    ("DC growth FY27E", Dc["C9"].value, 0.60, 2), ("DC growth FY28E", Dc["D9"].value, 0.85, 2),
    ("Remainder FY26", Dc["B8"].value, 4.3, 1), ("Remainder FY27E", Dc["C8"].value, 7.1, 1), ("Remainder FY28E", Dc["D8"].value, 12.6, 1),
    ("Custom share of growth FY27", Dc["C11"].value, 0.14, 2), ("Custom share of growth FY28", Dc["D11"].value, 0.23, 2),
    ("Remainder share of growth FY27", Dc["C12"].value, 0.77, 2),
    ("Base value", V["B7"].value, 356, 0), ("Base vs price", V["B9"].value, 0.25, 2),
    ("Rule on value", V["B11"].value, "LONG", None), ("Call", V["B12"].value, "LONG", None),
    ("Market value", V["B13"].value, 250, 0), ("Market value with pref", V["B14"].value, 256, 0),
    ("Net debt", V["B15"].value, 1.0, 1), ("EV", V["B16"].value, 257, 0),
    ("Since low close", V["B17"].value, 2.86, 2), ("Since Dec 25", V["B18"].value, 2.35, 2),
    ("Since piece", V["B19"].value, 0.087, 3), ("Off high close", V["B20"].value, -0.10, 2),
    ("Needed EPS FY29", V["B27"].value, 8.63, 2), ("Needed revenue FY29", V["B29"].value, 22.5, 1),
    ("Needed growth", V["B30"].value, 0.12, 2),
    ("Revisit long", V["B31"].value, 310, -1), ("Revisit short", V["B32"].value, 470, -1),
    ("EPS for long", V["B33"].value, 9.92, 2), ("EPS for short", V["B34"].value, 6.5, 1),
    ("Nvidia stake", V["B35"].value, 6.2, 1), ("Warrant net shares m", V["B37"].value * 1000, 16, 0),
    ("Warrant revenue", V["B38"].value, 120, 0), ("SBC share Q2", V["B39"].value, 0.119, 3), ("SBC x", V["B40"].value, 2.1, 1),
    ("Bear EPS", S["G5"].value, 6.94, 2), ("Bear value", S["I5"].value, 153, 0), ("Bear chg", S["J5"].value, -0.46, 2),
    ("Base EPS (scenario)", S["G6"].value, 10.78, 2), ("Base (scenario)", S["I6"].value, 356, 0),
    ("Bull EPS", S["G7"].value, 12.91, 2), ("Bull value", S["I7"].value, 517, 0), ("Bull chg", S["J7"].value, 0.81, 2),
    ("Weighted", S["I12"].value, 345, 0), ("Weighted vs price", S["J12"].value, 0.21, 2),
    ("Grid cells above price", G["B9"].value, 6, 0), ("Grid cells 15% above", G["B10"].value, 6, 0),
    ("Peer median", Pe["C13"].value, 33.4, 1),
]
grid = [[221, 281, 340], [280, 356, 431], [338, 429, 520]]
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
