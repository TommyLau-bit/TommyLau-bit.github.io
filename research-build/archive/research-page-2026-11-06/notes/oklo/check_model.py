"""Recalculate the Oklo model with LibreOffice headless, cache the values, and check outputs against the note."""
import subprocess, sys, os, shutil, openpyxl
from data import *

TMP = os.environ.get("RECALC_DIR", os.path.join(__import__("tempfile").gettempdir(), "oklo_recalc"))
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
out = os.path.join(TMP, os.path.basename(XLSX))
shutil.copyfile(out, XLSX)            # keep cached values so previews are not blank
wb = openpyxl.load_workbook(XLSX, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

C, S, G, V, Pe = (wb[n] for n in ["Cash", "Scenarios", "Sensitivity", "Valuation", "Peers"])
# Figures as published in src/content/calls/oklo.md and the PDF
checks = [
    ("Shares sold Jul-Sep m", C["B5"].value, 7.26, 2), ("Gross Jul-Sep US$m", C["B6"].value, 320, 0),
    ("Avg price Jul-Sep", C["B7"].value, 44.03, 2), ("Shares by 10 Sep m", C["B9"].value, 192.3, 1),
    ("FD shares m", C["B10"].value, 201.8, 1), ("Cash rise H1", C["B12"].value, 1594, 0),
    ("Spent H1", C["B14"].value, 258, 0), ("H2 spending", C["B17"].value, 398, 0),
    ("Cash 30 Sep 26", C["B19"].value, 3122, 0), ("Cash end 26", C["B20"].value, 2924, 0),
    ("Cash Sep 27", C["B22"].value, 2384, 0), ("Cash per share Sep 27", C["B23"].value, 11.81, 2),
    ("Market value", C["B24"].value, 6919, 0), ("EV", C["B25"].value, 3796, 0), ("Mcap / cash", C["B26"].value, 2.2, 1),
    ("Share rise since Jun 24", C["B27"].value, 0.58, 2),
    ("Bear value", S["I5"].value, 9.87, 2), ("Bear chg", S["J5"].value, -0.73, 2),
    ("Base value", S["I6"].value, 13.51, 2), ("Base chg", S["J6"].value, -0.62, 2), ("Base NPV/MW", S["G6"].value, 1.35, 2),
    ("Base fleet", S["H6"].value, 1580, 0), ("Base GW 2040", S["K6"].value, 3.7, 1),
    ("Bull value", S["I7"].value, 76.81, 2), ("Bull chg", S["J7"].value, 1.14, 2), ("Bull NPV/MW", S["G7"].value, 4.62, 2),
    ("Bull GW 2040", S["K7"].value, 8.5, 1), ("Bear NPV/MW", S["G5"].value, -2.92, 2),
    ("Weighted", S["I9"].value, 28.43, 2), ("Target ~ weighted", round(S["I9"].value), CALL["target"], 0), ("Weighted chg", S["J9"].value, -0.21, 2),
    ("Grid cells above price", G["B9"].value, 0, 0), ("Grid high", G["B10"].value, 31.04, 2), ("Grid low", G["B11"].value, 6.04, 2),
    ("Rule", V["B9"].value, "SHORT", None), ("Draft view", V["B10"].value, "SHORT", None),
    ("Margin per MW", V["B11"].value, 0.59, 2), ("Break-even capex", V["B13"].value, 8853, 0),
    ("Flat price to repay", V["B14"].value, 115, 0), ("Fleet needed", V["B15"].value, 6112, 0),
    ("MW a year needed", V["B17"].value, 1945, 0), ("GW needed by 2040", V["B18"].value, 16.8, 1),
    ("Capex needed", V["B19"].value, 3220, 0), ("Below high close", V["B22"].value, 0.79, 2),
    ("Cover level", V["B23"].value, 13.5, 1), ("Short wrong above", V["B24"].value, 60, 0),
    ("Consensus target vs price", V["B25"].value, 1.11, 2),
    ("Darlington fleet C$/kW", V["B26"].value, 17417, 0), ("Darlington first C$/kW", V["B27"].value, 25667, 0),
    ("Oklo EV/GW", Pe["H5"].value, 0.29, 2), ("XE EV/GW", Pe["H6"].value, 0.85, 2), ("SMR EV/GW", Pe["H7"].value, 0.37, 2),
    ("NNE EV", Pe["F8"].value, 254, 0),
]
grid = [[11.72, 21.38, 31.04], [6.04, 13.51, 23.17], [6.04, 6.41, 10.05]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 2))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and round(got, dp) == round(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:28s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("uncached formula cells:", blank or "none")
print("RESULT:", "PASS" if not bad and not errs and not blank else f"{bad} mismatches")
sys.exit(1 if bad or errs or blank else 0)
