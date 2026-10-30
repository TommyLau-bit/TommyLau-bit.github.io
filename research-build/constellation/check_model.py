"""Recalculate the Constellation model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/constellation.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/57a32070-c387-42a3-a0cc-4422a81a840c/scratchpad/ceg_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

E, V, S, G, Cr, Pe, C = (wb[n] for n in ["Earnings", "Valuation", "Scenarios", "Sensitivity", "Crane", "Peers", "Cover"])
checks = [
    # Earnings, as printed in the key financials table
    ("EPS 2026E", E["D7"].value, 12.10, 2), ("EPS 2027E", E["E7"].value, 12.24, 2), ("EPS 2028E", E["F7"].value, 14.52, 2),
    ("Base 2028", E["F5"].value, 9.44, 2), ("Enhanced 2026", E["D6"].value, 0.446, 3), ("Enhanced 2027", E["E6"].value, 0.375, 3),
    ("Enhanced 2028", E["F6"].value, 0.35, 3), ("Growth 2025", E["C8"].value, 0.083, 3), ("Growth 2026", E["D8"].value, 0.289, 3),
    ("Growth 2027", E["E8"].value, 0.012, 3), ("Growth 2028", E["F8"].value, 0.187, 3),
    ("Cons vs mine 27", E["B14"].value, 0.088, 3), ("Base CAGR", E["B15"].value, 0.202, 3),
    # Valuation
    ("Base value", V["B7"].value, 290.48, 2), ("Base vs price", V["B9"].value, 0.098, 3), ("Band", V["B10"].value, "NO CALL", None),
    ("Market value", V["B14"].value, 93.7, 1), ("Net debt", V["B15"].value, 24003, 0), ("EV", V["B16"].value, 118.1, 1),
    ("PE guide 26", V["B17"].value, 22.0, 1), ("PE cons 27", V["B19"].value, 19.9, 1), ("PE 2027E", V["B20"].value, 21.6, 1),
    ("PE 2028E", V["B21"].value, 18.2, 1), ("EPS for long", V["B23"].value, 15.21, 2),
    ("Long below", V["B24"].value, 253, 0), ("Short above", V["B25"].value, 387, 0),
    ("Off high", V["B26"].value, -0.345, 3), ("YTD", V["B27"].value, -0.251, 3), ("Div yield", V["B29"].value, 0.0064, 4),
    # 2027 guide that makes a long: about US$13.50 or less needed
    ("Guide for long", E["B16"].value, 12.82, 2), ("Value at 13.00, scaled", E["B18"].value, 308.5, 1), ("Value at 13.00, path", E["B19"].value, 299.4, 1),
    # Scenarios
    ("Bear EPS", S["E5"].value, 12.29, 2), ("Bear value", S["F5"].value, 184, 0), ("Bear chg", S["G5"].value, -0.303, 3),
    ("Base value scen", S["F6"].value, 290, 0), ("Bull EPS", S["E7"].value, 16.57, 2), ("Bull value", S["F7"].value, 381, 0),
    ("Bull chg", S["G7"].value, 0.440, 3), ("Weighted", S["E11"].value, 287, 0), ("Weighted chg", S["F11"].value, 0.083, 3),
    ("Base check", S["E12"].value, 0, 6), ("Bull add-on", S["E13"].value, 0.54, 2),
    ("Grid above", G["B9"].value, 6, 0), ("Grid 15%", G["B10"].value, 3, 0), ("Grid -25%", G["B11"].value, 0, 0),
    # Crane
    ("Crane TWh", Cr["B5"].value, 6.80, 2), ("Crane share", Cr["B6"].value, 0.038, 3), ("EPS per $10", Cr["B7"].value, 0.14, 2),
    ("Crane per kW", Cr["B8"].value, 1916, 0), ("Replacement mult", Cr["B9"].value, 2.44, 2), ("Google per kW", Cr["B10"].value, 4831, 0),
    ("Capacity revenue", Cr["B12"].value, 2239, 0),
    ("Peer median fwd", Pe["C10"].value, 12.0, 1),
    ("Cover band", C["B5"].value, "NO CALL", None),
]
grid = [[213, 250, 288], [247, 290, 334], [281, 330, 380]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))
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
