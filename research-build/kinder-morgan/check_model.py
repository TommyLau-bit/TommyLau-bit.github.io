"""Recalculate the Kinder Morgan model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/kinder-morgan.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/kmi_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

E, V, S, G, B, P, C = (wb[n] for n in ["EBITDA", "Valuation", "Scenarios", "Sensitivity", "Backlog", "Peers", "Cover"])
checks = [
    # EBITDA table as printed (US$bn to 2dp in the md, US$m in the PDF)
    ("EBITDA 2026E", E["E8"].value, 9150, 0), ("EBITDA 2027E", E["F8"].value, 9314, 0), ("EBITDA 2028E", E["G8"].value, 9754, 0),
    ("EBITDA 2029E", E["H8"].value, 10245, 0), ("Underlying 2026", E["E5"].value, 8925, 0),
    ("Growth 2024", E["C9"].value, 0.05, 2), ("Growth 2025", E["D9"].value, 0.06, 2), ("Growth 2026", E["E9"].value, 0.09, 2),
    ("Growth 2027", E["F9"].value, 0.02, 2), ("Growth 2028", E["G9"].value, 0.05, 2),
    ("Net debt 2026E", E["E11"].value, 32940, 0), ("Net debt 2027E", E["F11"].value, 33786, 0),
    ("Lev 2023", E["B12"].value, 4.2, 1), ("Lev 2024", E["C12"].value, 4.0, 1), ("Lev 2025", E["D12"].value, 3.8, 1),
    ("Lev 2027", E["F12"].value, 3.6, 1), ("Dividends 2027", E["F15"].value, 2700, -2),
    # Valuation
    ("Base value", V["B11"].value, 34.64, 2), ("Base vs price", V["B13"].value, 0.02, 2), ("Band", V["B14"].value, "NO CALL", None),
    ("EV at base", V["B7"].value, 112200, -2),
    ("Market value", V["B16"].value, 75.5, 1), ("EV", V["B17"].value, 108.9, 1), ("EV/LTM", V["B18"].value, 11.9, 1),
    ("EV/26E", V["B19"].value, 11.9, 1), ("EV/27E", V["B20"].value, 11.7, 1), ("EV/28E", V["B21"].value, 11.2, 1),
    ("EV/EBITDA 2023", V["B22"].value, 9.6, 1), ("EV/EBITDA 2024", V["B23"].value, 11.8, 1), ("EV/EBITDA 2025", V["B24"].value, 11.2, 1),
    ("Backlog EBITDA", V["B25"].value, 2400, -2), ("Implied EBITDA at 2023x", V["B26"].value, 11400, -2),
    ("Implied backlog share", V["B27"].value, 1.02, 2),
    ("Yield 2026", V["B28"].value, 0.035, 3), ("Yield 2023", V["B29"].value, 0.064, 3), ("Div check", V["B30"].value, 34.44, 2),
    ("Mult for long", V["B31"].value, 12.5, 1), ("Long below", V["B32"].value, 30.1, 1), ("Short above", V["B33"].value, 46.18, 2),
    ("Since Jan 24", V["B34"].value, 1.00, 2), ("YTD", V["B35"].value, 0.23, 2), ("Cons TP vs price", V["B36"].value, 0.109, 3),
    # Scenarios
    ("Bear EBITDA", S["E5"].value, 9280, -1), ("Bear value", S["F5"].value, 25.92, 2), ("Bear chg", S["G5"].value, -0.23, 2),
    ("Base value scen", S["F6"].value, 34.64, 2), ("Bull EBITDA", S["E7"].value, 10140, -1), ("Bull value", S["F7"].value, 43.48, 2),
    ("Bull chg", S["G7"].value, 0.28, 2), ("Weighted", S["E11"].value, 34.67, 2), ("Weighted chg", S["F11"].value, 0.02, 2),
    ("Base check", S["E12"].value, 0, 6),
    ("Grid above", G["B9"].value, 5, 0), ("Grid 15%", G["B10"].value, 2, 0),
    # Backlog
    ("Land 2027", B[f"B{38}"].value, 2253, 0), ("Land 2028", B["B39"].value, 4590, 0), ("Land 2030", B["B41"].value, 5130, 0),
    ("Land 2030 share", B["C41"].value, 0.36, 2), ("Named total", B["B42"].value, 12694, 0), ("AI pipes", B["B43"].value, 4700, 0),
    ("AI pipes EBITDA", B["B44"].value, 800, -2), ("AI share of 2026", B["B45"].value, 0.09, 2),
    ("Peer median", P["C14"].value, 16.1, 1),
    ("Cover band", C["B5"].value, "NO CALL", None),
]
grid = [[28.00, 32.16, 36.32], [30.26, 34.64, 39.01], [32.10, 36.65, 41.20]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 2))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and not isinstance(got, str) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:24s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
