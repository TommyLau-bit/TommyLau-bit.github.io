"""Recalculate the Texas Instruments model with LibreOffice headless and check outputs against the note."""
import subprocess, sys, os, openpyxl
from data import *

TMP = os.environ.get("RECALC_DIR", "/tmp/txn_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX],
               check=True, capture_output=True)
wb = openpyxl.load_workbook(os.path.join(TMP, os.path.basename(XLSX)), data_only=True)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]

F, V, S, G, Qt, DC = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "DataCentre"])
# Figures as published in src/content/calls/texas-instruments.md and the PDF
checks = [
    ("DC Q1 25 US$m", DC["B8"].value * 1000, 290, 0), ("DC Q2 25 US$m", DC["B9"].value * 1000, 331, 0),
    ("DC Q3 25 US$m", DC["B6"].value * 1000, 429, 0),
    ("DC Q1 26 US$m", DC["B10"].value * 1000, 552, 0), ("DC Q2 26 US$m", DC["B11"].value * 1000, 662, 0),
    ("DC share Q2 26", DC["B12"].value, 0.12, 2), ("DC share of growth", DC["B13"].value, 0.33, 2),
    ("DC 2026E", DC["B15"].value, 2.77, 2), ("DC 2026E growth", DC["B16"].value, 0.85, 2),
    ("TTM FCF", Qt["B20"].value, 6.534, 3), ("Q3 EPS mine", Qt["L11"].value, 2.40, 2), ("Q4 EPS mine", Qt["M11"].value, 2.28, 2),
    ("GM Q2 26", Qt["K8"].value, 0.614, 3), ("OM Q2 26", Qt["K10"].value, 0.423, 3),
    ("2026E revenue", F["E7"].value, 22.04, 2), ("2026E growth", F["E8"].value, 0.25, 2),
    ("2026E op margin", F["E12"].value, 0.419, 3), ("2026E EPS", F["E15"].value, 8.50, 2),
    ("2027E revenue", F["F7"].value, 24.73, 2), ("2027E op margin", F["F12"].value, 0.447, 3), ("2027E EPS", F["F15"].value, 10.15, 2),
    ("2028E revenue", F["G7"].value, 26.35, 2), ("2028E op margin", F["G12"].value, 0.462, 3), ("2028E EPS", F["G15"].value, 11.20, 2),
    ("DC share 2028E", F["G9"].value, 0.20, 2), ("GM 2022", F["B10"].value, 0.688, 3), ("FCF 2025", F["D22"].value, 2.938, 3),
    ("P/E 2026E", F["E17"].value, 34.7, 1), ("P/E 2027E", F["F17"].value, 29.1, 1), ("P/E 2028E", F["G17"].value, 26.3, 1),
    ("P/E cons 2027", V["B22"].value, 27.7, 1), ("EPS27 vs cons", V["B24"].value, -0.05, 2),
    ("Base value", V["B7"].value, 280, 0), ("Base vs price", V["B9"].value, -0.05, 2),
    ("Draft view", V["B11"].value, "NO CALL", None),
    ("Market value", V["B13"].value, 271, 0), ("Net debt", V["B14"].value, 7.05, 2), ("EV", V["B15"].value, 278, 0),
    ("Dividend yield", V["B16"].value, 0.0206, 4), ("Rise since Sep 25", V["B17"].value, 0.61, 2), ("Below high", V["B18"].value, 0.12, 2),
    ("Needed EPS 2028", V["B26"].value, 11.80, 2), ("Needed revenue 2028", V["B28"].value, 27.2, 1),
    ("Needed vs 2022", V["B29"].value, 0.36, 2), ("FCF 2026 framework", V["B31"].value, 9.5, 1),
    ("FCF per share", V["B32"].value, 10.35, 2), ("FCF yield", V["B33"].value, 0.035, 3),
    ("Revisit price", V["B34"].value, 244, 0),
    ("Bear EPS", S["I5"].value, 7.66, 2), ("Bear value", S["K5"].value, 168.5, 1), ("Bear chg", S["L5"].value, -0.43, 2),
    ("Bull EPS", S["I7"].value, 13.14, 2), ("Bull value", S["K7"].value, 368, 0), ("Bull chg", S["L7"].value, 0.25, 2),
    ("Base (scenario tab)", S["K6"].value, 280, 0),
    ("Weighted", S["K12"].value, 274, 0), ("Weighted vs price", S["L12"].value, -0.07, 2),
    ("DC swing", S["I21"].value, 1.58, 2), ("Rest swing", S["I22"].value, 3.90, 2), ("Ratio", S["I23"].value, 2.5, 1),
    ("Grid cells above price", G["B9"].value, 3, 0),
]
grid = [[200, 238, 276], [235, 280, 325], [262, 312, 362]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and round(got, dp) == round(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:30s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("RESULT:", "PASS" if not bad and not errs else f"{bad} mismatches")
sys.exit(1 if bad or errs else 0)
