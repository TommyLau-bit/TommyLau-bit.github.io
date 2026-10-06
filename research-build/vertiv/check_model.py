"""Recalculate the model with LibreOffice headless and check outputs against the published pitch."""
import subprocess, sys, os, openpyxl
from data import XLSX

TMP = os.environ.get("RECALC_DIR", "/tmp/vertiv_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX],
               check=True, capture_output=True)
wb = openpyxl.load_workbook(os.path.join(TMP, os.path.basename(XLSX)), data_only=True)

errs = []
for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and c.value.startswith("#"):
                errs.append(f"{ws.title}!{c.coordinate}={c.value}")

F, V, S, G = wb["Financials"], wb["Valuation"], wb["Scenarios"], wb["Sensitivity"]
checks = [
    ("2027E sales", F["E5"].value, 16.94, 2), ("2027E EPS", F["E10"].value, 8.53, 2),
    ("2028E sales", F["F5"].value, 20.33, 2), ("2028E EPS", F["F10"].value, 10.65, 2),
    ("2026 growth", F["D6"].value, 0.37, 2), ("2025 growth", F["C6"].value, 0.28, 2),
    ("P/E 2026 guide", V["B18"].value, 37.9, 1), ("P/E 2027E", V["B20"].value, 29.7, 1),
    ("P/E 2028E", V["B21"].value, 23.8, 1), ("P/E consensus 2027", V["B19"].value, 28.4, 1),
    ("Base value", V["B7"].value, 298, 0), ("Target", V["B8"].value, 300, 0),
    ("Upside", V["B10"].value, 0.18, 2), ("Market value US$bn", V["B14"].value, 99.6, 1),
    ("Net cash US$m", V["B15"].value, 170.8, 1), ("Peak P/E", V["B23"].value, 59.8, 1),
    ("Bear EPS", S["H5"].value, 8.17, 2), ("Bear value", S["J5"].value, 180, 0), ("Bear chg", S["K5"].value, -0.29, 2),
    ("Bull EPS", S["H7"].value, 11.52, 2), ("Bull value", S["J7"].value, 392, 0), ("Bull chg", S["K7"].value, 0.54, 2),
    ("Weighted (unrounded base)", S["E11"].value, 292, 0),
    ("Weighted vs price", S["F11"].value, 0.15, 2),
]
grid = [[228, 266, 304], [256, 298, 341], [276, 322, 368]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))
Q = wb["Quarterly"]
checks += [("Margin beats since Q3 25", Q["B17"].value, 4, 0), ("Service slower quarters", Q["B18"].value, 9, 0)]

bad = 0
for name, got, want, dp in checks:
    ok = got is not None and round(got, dp) == round(want, dp)
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:28s} model={got!r:>22}  pitch={want}")
print("formula errors:", errs or "none")
print("RESULT:", "PASS" if not bad and not errs else f"{bad} mismatches")
sys.exit(1 if bad or errs else 0)
