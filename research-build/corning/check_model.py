"""Recalculate the Corning model with LibreOffice headless and check outputs against the note."""
import subprocess, sys, os, openpyxl
from data import *

TMP = os.environ.get("RECALC_DIR", "/tmp/glw_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX],
               check=True, capture_output=True)
wb = openpyxl.load_workbook(os.path.join(TMP, os.path.basename(XLSX)), data_only=True)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]

F, V, S, G, Qt, Fu, Pe = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Funding", "Peers"])
# Figures as published in src/content/calls/corning.md and the PDF
checks = [
    ("Q3E EPS", Qt["L12"].value, 0.87, 2), ("Q4E EPS", Qt["M12"].value, 0.91, 2),
    ("Q4 run-rate", Qt["B18"].value, 20.3, 1), ("TTM core EPS", Qt["B15"].value, 2.87, 2),
    ("Enterprise share Q2", Qt["B19"].value, 0.61, 2), ("Carrier Q2 26", Qt["B20"].value, 0.80, 2), ("Carrier Q2 25", Qt["B21"].value, 0.80, 2),
    ("Opt margin Q2 26", Qt["K11"].value, 0.211, 3), ("Opt margin Q2 25", Qt["G11"].value, 0.158, 3), ("Opt margin Q1 24", Qt["B11"].value, 0.108, 3),
    ("Opt growth Q2 26", Qt["K8"].value, 0.32, 2),
    ("2026E sales", F["E7"].value, 19.11, 2), ("2026E optical", F["E5"].value, 8.50, 2), ("2026E opt margin", F["E11"].value, 0.214, 3),
    ("2026E EPS", F["E17"].value, 3.25, 2),
    ("2027E sales", F["F7"].value, 23.04, 2), ("2027E optical", F["F5"].value, 11.47, 2), ("2027E EPS", F["F17"].value, 4.37, 2),
    ("2028E sales", F["G7"].value, 26.84, 2), ("2028E optical", F["G5"].value, 14.34, 2), ("2028E EPS", F["G17"].value, 5.41, 2),
    ("2028E opt share", F["G9"].value, 0.53, 2), ("2025 opt share", F["D9"].value, 0.38, 2),
    ("2023 opt margin", F["B11"].value, 0.119, 3), ("2025 opt margin", F["D11"].value, 0.167, 3),
    ("P/E 2023", F["B19"].value, 93.7, 1), ("P/E 2025", F["D19"].value, 63.2, 1),
    ("P/E 2026E", F["E19"].value, 49.0, 1), ("P/E 2027E", F["F19"].value, 36.5, 1), ("P/E 2028E", F["G19"].value, 29.4, 1),
    ("Base value", V["B7"].value, 146, 0), ("Base vs price", V["B9"].value, -0.08, 2),
    ("Draft view", V["B11"].value, "NO CALL", None),
    ("Market value", V["B13"].value, 137, 0), ("Net debt", V["B14"].value, 5.9, 1), ("EV", V["B15"].value, 143, 0),
    ("Dividend yield", V["B16"].value, 0.007, 3), ("Rise since Sep 25", V["B17"].value, 0.94, 2), ("Below high", V["B18"].value, 0.41, 2),
    ("P/E hindsight end-2024", V["B25"].value, 18.9, 1),
    ("Needed EPS 2028", V["B27"].value, 5.90, 2), ("Needed optical 2028", V["B29"].value, 16.1, 1),
    ("Needed vs 2025", V["B30"].value, 2.6, 1), ("Needed growth", V["B31"].value, 0.38, 2),
    ("Revisit price", V["B32"].value, 127, 0),
    ("Capex H2 2026", Fu["B9"].value, 1.25, 2), ("FCF H1 ex deposits", Fu["B12"].value, 0.90, 2),
    ("ATM shares m", Fu["B18"].value * 1000, 12.5, 1), ("ATM dilution", Fu["B19"].value, 0.015, 3),
    ("ATM day drop", Fu["B20"].value, -0.137, 3), ("Warrant per deposit dollar", Fu["B24"].value, 0.30, 2),
    ("Bear EPS", S["M5"].value, 3.89, 2), ("Bear value", S["O5"].value, 86, 0), ("Bear chg", S["P5"].value, -0.46, 2),
    ("Bull EPS", S["M7"].value, 6.47, 2), ("Bull value", S["O7"].value, 220, 0), ("Bull chg", S["P7"].value, 0.38, 2),
    ("Base (scenario tab)", S["O6"].value, 146, 0),
    ("Weighted", S["O12"].value, 149.5, 1), ("Weighted vs price", S["P12"].value, -0.06, 2),
    ("Optical swing", S["M21"].value, 2.06, 2), ("Rest swing", S["M22"].value, 0.52, 2), ("Ratio", S["M23"].value, 4.0, 0),
    ("Grid cells above price", G["B9"].value, 3, 0),
    ("Fibre peer median", Pe["C14"].value, 23.5, 1),
]
grid = [[101, 124, 147], [119, 146, 173], [136, 167, 198]]
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
