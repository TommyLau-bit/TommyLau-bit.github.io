"""Recalculate the Bloom Energy model with LibreOffice headless and check outputs against the note."""
import subprocess, sys, os, openpyxl
from data import *

TMP = os.environ.get("RECALC_DIR", "/tmp/be_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX],
               check=True, capture_output=True)
wb = openpyxl.load_workbook(os.path.join(TMP, os.path.basename(XLSX)), data_only=True)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]

F, V, S, G, Qt, Di, Ca, Pe = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Dilution", "Capacity", "Peers"])
# Figures as published in src/content/calls/bloom-energy.md and the PDF
checks = [
    ("Q3E EPS", Qt["L15"].value, 0.72, 2), ("Q4E EPS", Qt["M15"].value, 0.84, 2),
    ("TTM EPS", Qt["B20"].value, 1.82, 2), ("Product GM H1 26", Qt["B21"].value, 0.356, 3),
    ("Rev H1 26 vs H1 24", Qt["B22"].value, 3.2, 1), ("Rev growth Q2", Qt["B23"].value, 1.66, 2),
    ("Product GM Q2 26", Qt["K8"].value, 0.365, 3), ("Product GM Q4 24", Qt["E8"].value, 0.462, 3),
    ("Service GM Q2 26", Qt["K11"].value, 0.187, 3),
    ("Product GM 2024", F["B9"].value, 0.368, 3), ("Product GM 2025", F["C9"].value, 0.352, 3),
    ("2026E revenue", F["D5"].value, 4.07, 2), ("2026E GM", F["D11"].value, 0.339, 3), ("2026E op inc", F["D13"].value, 0.87, 2),
    ("2026E EPS", F["D19"].value, 2.78, 2),
    ("2027E revenue", F["E5"].value, 6.30, 2), ("2027E op inc", F["E13"].value, 1.59, 2), ("2027E EPS", F["E19"].value, 4.43, 2),
    ("2028E revenue", F["F5"].value, 8.70, 2), ("2028E op inc", F["F13"].value, 2.34, 2), ("2028E EPS", F["F19"].value, 6.03, 2),
    ("2027E op margin", F["E14"].value, 0.252, 3), ("2028E op margin", F["F14"].value, 0.269, 3),
    ("P/E 2025", F["C21"].value, 377, 0), ("P/E 2026E", F["D21"].value, 103, 0), ("P/E 2027E", F["E21"].value, 65, 0), ("P/E 2028E", F["F21"].value, 48, 0),
    ("FD shares 26", F["D18"].value * 1000, 325, 0), ("FD shares 27", F["E18"].value * 1000, 330, 0), ("FD shares 28", F["F18"].value * 1000, 334, 0),
    ("GW 2026E", F["D24"].value, 1.2, 1), ("GW 2027E", F["E24"].value, 1.9, 1), ("GW 2028E", F["F24"].value, 2.6, 1),
    ("Base value", V["B7"].value, 241, 0), ("Base vs price", V["B9"].value, -0.16, 2),
    ("Rule on value", V["B11"].value, "SHORT", None), ("Draft view", V["B12"].value, "NO CALL", None),
    ("Market value", V["B13"].value, 84, 0), ("Net cash", V["B14"].value, 0.14, 2), ("EV", V["B15"].value, 84, 0),
    ("Rise since Dec 25", V["B16"].value, 2.30, 2), ("Below high close", V["B17"].value, 0.17, 2),
    ("P/E guide mid", V["B21"].value, 106, 0), ("P/E cons 2028", V["B22"].value, 41, 0),
    ("Needed EPS 2028", V["B25"].value, 7.17, 2), ("Needed revenue 2028", V["B27"].value, 10.0, 1),
    ("Needed GW 2028", V["B29"].value, 3.0, 1), ("Revisit long", V["B30"].value, 210, 0), ("Revisit short", V["B31"].value, 322, 0),
    ("USD per MW", Ca["B6"].value, 2.94, 2), ("Revenue a 2 GW plant supports", Ca["B12"].value, 6.73, 2),
    ("2030 notes shares m", Di["B8"].value * 1000, 12.8, 1), ("2029 notes shares m", Di["B11"].value * 1000, 1.3, 1),
    ("Fully diluted m", Di["B13"].value * 1000, 325, 0), ("Conversion trigger", Di["B16"].value, 253.46, 2),
    ("SBC vs op income", Di["B19"].value, 0.235, 3),
    ("Bear EPS", S["L5"].value, 3.33, 2), ("Bear value", S["N5"].value, 83, 0), ("Bear chg", S["O5"].value, -0.71, 2),
    ("Bear 2028 revenue", S["I5"].value, 5.9, 1),
    ("Bull EPS", S["L7"].value, 7.89, 2), ("Bull value", S["N7"].value, 394, 0), ("Bull chg", S["O7"].value, 0.38, 2),
    ("Bull GW", S["P7"].value, 3.1, 1), ("Base (scenario tab)", S["N6"].value, 241, 0),
    ("Weighted", S["N12"].value, 240, 0), ("Weighted vs price", S["O12"].value, -0.16, 2),
    ("Grid cells above price", G["B9"].value, 3, 0),
    ("Peer median", Pe["C13"].value, 29.4, 1),
]
grid = [[135, 180, 225], [181, 241, 301], [225, 300, 375]]
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
