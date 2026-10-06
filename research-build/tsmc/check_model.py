"""Recalculate the TSMC model with LibreOffice headless and check outputs against the note."""
import subprocess, sys, os, openpyxl
from data import *

TMP = os.environ.get("RECALC_DIR", "/tmp/tsmc_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX],
               check=True, capture_output=True)
wb = openpyxl.load_workbook(os.path.join(TMP, os.path.basename(XLSX)), data_only=True)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]

F, V, S, G, Qt, M, Cv = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Monthly", "Cover"])
# Figures as published in src/content/calls/tsmc.md and the PDF
checks = [
    ("2026E revenue", F["D5"].value, 171.50, 2), ("2026E growth", F["D6"].value, 0.40, 2),
    ("2026E op margin", F["D8"].value, 0.577, 3), ("2026E EPS", F["D12"].value, 16.81, 2),
    ("2027E revenue", F["E5"].value, 212.66, 2), ("2027E EPS", F["E12"].value, 20.25, 2),
    ("2028E revenue", F["F5"].value, 250.94, 2), ("2028E EPS", F["F12"].value, 23.29, 2),
    ("2025 growth", F["C6"].value, 0.36, 2),
    ("P/E 2024", F["B14"].value, 69.0, 1), ("P/E 2025", F["C14"].value, 45.6, 1),
    ("P/E 2026E", F["D14"].value, 28.9, 1), ("P/E 2027E", F["E14"].value, 24.0, 1), ("P/E 2028E", F["F14"].value, 20.9, 1),
    ("P/E cons 2027", V["B22"].value, 22.8, 1), ("EPS27 vs cons", V["B24"].value, -0.05, 2),
    ("Base value", V["B7"].value, 466, 0), ("Base vs price", V["B9"].value, -0.04, 2),
    ("Draft view", V["B11"].value, "NO CALL", None),
    ("Market value US$bn (2.52tn)", V["B13"].value / 1000, 2.52, 2), ("Taipei value US$tn", V["B14"].value / 1000, 2.11, 2),
    ("Net cash US$bn", V["B15"].value, 84, 0), ("ADR premium", V["B16"].value, 0.19, 2),
    ("Rise since Sep 25", V["B17"].value, 0.74, 2),
    ("Needed EPS 2028", V["B26"].value, 24.29, 2), ("Needed OM 2028", V["B27"].value, 0.58, 2),
    ("2029 plan revenue", V["B29"].value, 275, 0), ("Plan growth 27 to 29", V["B30"].value, 0.17, 2),
    ("Revisit price", V["B31"].value, 400, 0),
    ("Bear EPS", S["H5"].value, 17.40, 2), ("Bear value", S["J5"].value, 278, 0), ("Bear chg", S["K5"].value, -0.43, 2),
    ("Bull EPS", S["H7"].value, 27.43, 2), ("Bull value", S["J7"].value, 658, 0), ("Bull chg", S["K7"].value, 0.36, 2),
    ("Base (scenario tab)", S["J6"].value, 466, 0),
    ("Weighted", S["F11"].value, 467, 0), ("Weighted vs price", S["G11"].value, -0.04, 2),
    ("Grid cells above price", G["B9"].value, 3, 0),
    ("Wafers y/y", Qt["B20"].value, 0.17, 2), ("Rev per wafer y/y", Qt["B21"].value, 0.17, 2),
    ("Q2 excess non-op per ADR", Qt["B23"].value, 0.34, 2), ("1H26 capex NT$bn", Qt["D24"].value, 847, 0),
    ("Jul+Aug NT$bn", M["B27"].value, 982.4, 1), ("Sep needed low", M["B30"].value, 445, 0), ("Sep needed high", M["B31"].value, 483, 0),
    ("Guide monthly pace", M["B32"].value, 482.1, 1),
    ("GM above floor Q2 26", Qt["K14"].value, 11.7, 1),
]
grid = [[320, 400, 480], [373, 466, 559], [416, 520, 624]]
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
