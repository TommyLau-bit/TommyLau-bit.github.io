"""Recalculate the Micron model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures printed in the note and src/content/calls/micron.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP


def rnd(x, dp):  # Excel-style half-up rounding, as the cells display
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))

from data import *

TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/87f9daa0-8062-414d-a40b-cb592166359f/scratchpad/mu_recalc")
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

F, V, S, G, Qt, Pe, N = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Peers", "Normal"])
# Figures as published in the note and the md
checks = [
    ("FY26 revenue (sum of quarters)", Qt["B32"].value, 133.188, 3), ("Q4 FY26 rev growth on a year", Qt["B33"].value, 3.79, 2),
    ("BU margin gap, points", Qt["B34"].value, 7, 0), ("Q1 FY27 implied other", Qt["G14"].value, 0.94, 2),
    ("Q1 FY27 EPS", Qt["G17"].value, 38.15, 2),
    ("FY25 net margin", F["B15"].value, 0.253, 3), ("FY26 net margin", F["C15"].value, 0.651, 3),
    ("FY26 conventional DRAM", F["C8"].value, 91, 0),
    ("FY27 revenue", F["D5"].value, 266.3, 1), ("FY27 GM", F["D10"].value, 0.875, 3), ("FY27 net margin", F["D15"].value, 0.723, 3),
    ("FY27 EPS", F["D16"].value, 167.44, 2), ("FY27 vs consensus", F["D18"].value, -0.049, 3), ("FY27 conv DRAM", F["D8"].value, 178, 0),
    ("FY28 revenue", F["E5"].value, 292.9, 1), ("FY28 EPS", F["E16"].value, 179.96, 2), ("FY28 vs consensus", F["E18"].value, -0.128, 3),
    ("FY28 net margin", F["E15"].value, 0.707, 3), ("FY28 conv DRAM", F["E8"].value, 191, 0),
    ("P/E FY25", F["B20"].value, 126, 0), ("P/E FY26", F["C20"].value, 13.8, 1), ("P/E FY27 mine", F["D20"].value, 6.2, 1),
    ("P/E FY28 mine", F["E20"].value, 5.8, 1), ("P/E cons FY27", F["D21"].value, 5.9, 1), ("P/E cons FY28", F["E21"].value, 5.1, 1),
    ("FY27 FCF", F["D23"].value, 145.6, 1), ("Net cash per share Oct 27", F["D26"].value, 174, 0),
    ("Ten-year net margin", N["D17"].value, 0.188, 3), ("FY18 net margin", N["D18"].value, 0.465, 3),
    ("Normal revenue", N["B24"].value, 152, 0), ("Normal EPS", N["B27"].value, 39.63, 2),
    ("Excess per share", V["B6"].value, 186, 0), ("Normal value per share", V["B7"].value, 476, 0),
    ("Base value", V["B8"].value, 835, 0), ("Base vs price", V["B10"].value, -0.20, 2), ("Weighted", V["B11"].value, 879, 0),
    ("Rule on value", V["B12"].value, "NO CALL", None), ("Draft view", V["B13"].value, "NO CALL", None),
    ("Market value", V["B15"].value, 1181, 0), ("P/E normal", V["B22"].value, 26.4, 1),
    ("Need normal EPS", V["B24"].value, 59.31, 2), ("Need margin", V["B25"].value, 0.449, 3),
    ("Need vs FY26", V["B27"].value, 0.79, 2), ("Need vs FY28", V["B28"].value, 0.33, 2),
    ("Revisit long price", V["B29"].value, 726, 0), ("Revisit short price", V["B30"].value, 1114, 0),
    ("Revisit long EPS", V["B31"].value, 74, 0), ("Revisit short EPS", V["B32"].value, 35, 0),
    ("FY22 P/E at high", V["B33"].value, 12.6, 1), ("FY22 to FY23 fall", V["B34"].value, -0.50, 2),
    ("Bear FY28 EPS", S["K5"].value, 104.92, 2), ("Bear normal EPS", S["J5"].value, 18.25, 2), ("Bear value", S["O5"].value, 436, 0), ("Bear chg", S["P5"].value, -0.58, 2),
    ("Base value (scenario)", S["O6"].value, 835, 0), ("Base chg", S["P6"].value, -0.20, 2),
    ("Bull FY28 EPS", S["K7"].value, 206.12, 2), ("Bull normal EPS", S["J7"].value, 67.24, 2), ("Bull value", S["O7"].value, 1409, 0), ("Bull chg", S["P7"].value, 0.35, 2),
    ("Weighted (scenario)", S["O12"].value, 879, 0), ("Weighted vs price", S["P12"].value, -0.16, 2),
    ("Grid cells above price", G["B9"].value, 1, 0), ("Grid cells 25% below", G["B10"].value, 4, 0),
    ("SK Hynix P/E", Pe["G6"].value, 3.7, 1), ("Samsung P/E", Pe["G7"].value, 3.8, 1), ("SanDisk P/E", Pe["G8"].value, 7.8, 1),
    ("Kioxia P/E", Pe["G9"].value, 5.2, 1), ("Peer median", Pe["G11"].value, 4.5, 1),
]
grid = [[664, 723, 781], [756, 835, 915], [848, 948, 1049]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (isinstance(got, (int, float)) and rnd(got, dp) == rnd(want, dp))
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
