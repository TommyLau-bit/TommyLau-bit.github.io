"""Recalculate the Entergy model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures printed in the note and src/content/calls/entergy.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/etr_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

E, V, S, G, R, Pe, C = (wb[n] for n in ["Earnings", "Valuation", "Scenarios", "Sensitivity", "RateBase", "Peers", "Cover"])
checks = [
    # Earnings, as printed in the key financials table
    ("Mid 2026", E["D7"].value, 4.40, 2), ("Mid 2027", E["E7"].value, 5.05, 2), ("Mid 2028", E["F7"].value, 5.70, 2),
    ("Mid 2029", E["G7"].value, 6.40, 2), ("Mid 2030", E["H7"].value, 7.20, 2),
    ("Growth 2025", E["C8"].value, 0.071, 3), ("Growth 2026", E["D8"].value, 0.125, 3), ("Growth 2027", E["E8"].value, 0.148, 3),
    ("Growth 2028", E["F8"].value, 0.129, 3), ("Growth 2029", E["G8"].value, 0.123, 3), ("Growth 2030", E["H8"].value, 0.125, 3),
    ("PE 2026 mid", E["D12"].value, 25.0, 1), ("PE 2027 mid", E["E12"].value, 21.8, 1), ("PE 2028 mid", E["F12"].value, 19.3, 1),
    ("Mine vs cons 26", E["D11"].value, -0.002, 3), ("Mine vs cons 27", E["E11"].value, -0.010, 3),
    ("EPS CAGR", E["B14"].value, 0.130, 3), ("Q4 2026 implied", E["B15"].value, 0.51, 2), ("Q4 2025", E["B16"].value, 0.51, 2),
    ("PE cons 27", E["B17"].value, 21.6, 1),
    # Valuation
    ("Base value", V["B7"].value, 122.55, 2), ("Base vs price", V["B9"].value, 0.113, 3), ("Band", V["B10"].value, "NO CALL", None),
    ("Shares", V["B14"].value, 477.78, 2), ("Market value", V["B15"].value, 52.6, 1), ("Net debt", V["B16"].value, 30731, 0),
    ("EV", V["B17"].value, 83.3, 1), ("PE guide 26", V["B18"].value, 25.0, 1), ("PE cons 27", V["B19"].value, 21.6, 1),
    ("PE 2028E", V["B21"].value, 19.3, 1), ("PE for long", V["B22"].value, 22.2, 1), ("EPS for long", V["B23"].value, 5.89, 2),
    ("Long below", V["B24"].value, 106.57, 2), ("Short above", V["B25"].value, 163.40, 2),
    ("Off high", V["B26"].value, -0.066, 3), ("YTD", V["B27"].value, 0.191, 3), ("Target vs price", V["B28"].value, 0.087, 3),
    ("Div yield", V["B29"].value, 0.0247, 4), ("With dividends", V["B30"].value, 0.138, 3),
    # Scenarios
    ("Bear value", S["D5"].value, 98.10, 2), ("Bear chg", S["E5"].value, -0.109, 3),
    ("Base value scen", S["D6"].value, 122.55, 2), ("Bull value", S["D7"].value, 142.80, 2), ("Bull chg", S["E7"].value, 0.297, 3),
    ("Weighted", S["D11"].value, 121.50, 2), ("Weighted chg", S["E11"].value, 0.103, 3), ("Base check", S["D12"].value, 0, 6),
    ("Grid above", G["B9"].value, 7, 0), ("Grid 15%", G["B10"].value, 4, 0), ("Grid -25%", G["B11"].value, 0, 0),
    # Rate base and Meta
    ("Capex total", R["B5"].value, 66530, 0), ("RB CAGR", R["B6"].value, 0.161, 3), ("Meta1", R["B8"].value, 4127, 0),
    ("Meta2", R["B9"].value, 14300, 0), ("Meta share", R["B10"].value, 0.277, 3), ("Meta1 per kW", R["B11"].value, 1583, 0),
    ("Meta2 per kW", R["B12"].value, 2444, 0), ("Meta2 NI", R["B13"].value, 706, 0), ("Meta2 EPS", R["B14"].value, 1.42, 2),
    ("Adv increase", R["B15"].value, 1443, 0), ("Equity left", R["B16"].value, 2900, 0),
    ("Peer median fwd", Pe["C12"].value, 19.1, 1), ("Premium", Pe["C13"].value, 3.4, 1),
    ("Cover band", C["B5"].value, "NO CALL", None),
]
grid = [[104, 117, 131], [108, 123, 137], [113, 128, 143]]
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
