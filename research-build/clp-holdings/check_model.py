"""Recalculate the CLP Holdings model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/clp-holdings.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/clp_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

S_, E, V, Sc, G, Pe, C = (wb[n] for n in ["SoC", "Earnings", "Valuation", "Scenarios", "Sensitivity", "Peers", "Cover"])
checks = [
    # SoC, as printed in the key financials table and thesis
    ("ANFA 2024 bn", S_["C6"].value / 1000, 140.9, 1), ("ANFA 2025 bn", S_["D6"].value / 1000, 145.3, 1),
    ("ANFA 2026E bn", S_["E6"].value / 1000, 149.8, 1), ("ANFA 2027E bn", S_["F6"].value / 1000, 154.1, 1),
    ("ANFA 2028E bn", S_["G6"].value / 1000, 158.2, 1), ("Net return 2025", S_["D10"].value, 0.0711, 4),
    ("CLP share", S_["D11"].value, 0.906, 3), ("HK other", S_["D13"].value, 195, 0),
    ("HK 2026E", S_["E14"].value, 10030, 0), ("HK 2027E", S_["F14"].value, 10313, 0), ("HK 2028E", S_["G14"].value, 10584, 0),
    ("HK growth 2025", S_["D15"].value, 0.073, 3), ("ANFA CAGR", S_["B17"].value, 0.029, 3),
    ("Per bn EPS", S_["B19"].value, 0.026, 3), ("Per bn value", S_["B20"].value, 0.47, 2),
    ("ANFA for long", S_["B21"].value, 22, 0), ("Share of plan", S_["B22"].value, 0.42, 2),
    ("DC illus bn", S_["B23"].value, 9.6, 1), ("DC illus EPS", S_["B24"].value, 0.25, 2), ("DC illus share", S_["B25"].value, 0.05, 2),
    # Earnings
    ("Check 2024", E["B19"].value, 0, 0), ("Check 2025", E["C19"].value, 0, 0),
    ("OPE 2026E", E["D12"].value, 11460, 0), ("OPE 2027E", E["E12"].value, 11793, 0), ("OPE 2028E", E["F12"].value, 12064, 0),
    ("EPS 2024A", E["B14"].value, 4.33, 2), ("EPS 2025A", E["C14"].value, 4.23, 2), ("EPS 2026E", E["D14"].value, 4.54, 2),
    ("EPS 2027E", E["E14"].value, 4.67, 2), ("EPS 2028E", E["F14"].value, 4.77, 2), ("Cons gap 27", E["B22"].value, 0.06, 2),
    ("HK share 2025", E["C17"].value, 0.82, 2),
    # Valuation
    ("Base value", V["B9"].value, 79.10, 2), ("Base vs price", V["B11"].value, 0.017, 3), ("Band", V["B12"].value, "NO CALL", None),
    ("Group multiple", V["B14"].value, 16.6, 1), ("Market value", V["B16"].value, 196.4, 1), ("Net debt", V["B17"].value, 62242, 0),
    ("PE ttm", V["B19"].value, 17.6, 1), ("PE 2027E", V["B21"].value, 16.7, 1), ("PE cons 27", V["B22"].value, 15.7, 1),
    ("PE 2028E", V["B23"].value, 16.3, 1), ("Implied HK mult", V["B24"].value, 17.7, 1),
    ("Long below", V["B25"].value, 68.78, 2), ("Short above", V["B26"].value, 105.47, 2),
    ("Yield", V["B27"].value, 0.0412, 4), ("YTD", V["B28"].value, 0.120, 3), ("Off high", V["B29"].value, -0.026, 3),
    ("HK part per share", V["D5"].value / SHARES, 75.40, 2), ("Ovs part per share", V["D6"].value / SHARES, 9.46, 2),
    ("Costs part per share", V["D7"].value / SHARES, -5.76, 2),
    # Scenarios
    ("Bear EPS", Sc["I5"].value, 4.41, 2), ("Bear value", Sc["J5"].value, 61.62, 2), ("Bear chg", Sc["K5"].value, -0.21, 2),
    ("Base value scen", Sc["J6"].value, 79.10, 2), ("Bull EPS", Sc["I7"].value, 5.05, 2), ("Bull value", Sc["J7"].value, 92.39, 2),
    ("Bull chg", Sc["K7"].value, 0.19, 2), ("Weighted", Sc["J11"].value, 78.05, 2), ("Base check", Sc["J12"].value, 0, 6),
    ("Grid above", G["B9"].value, 7, 0), ("Grid 15%", G["B10"].value, 3, 0), ("Grid -25%", G["B11"].value, 0, 0),
    ("Peer median fwd", Pe["C11"].value, 18.8, 1), ("Alt base", V["B31"].value, BASE_ALT, 2), ("Alt chg", V["B32"].value, 0.066, 3), ("Peer median yield", Pe["E11"].value, 0.046, 3),
    ("Cover band", C["B5"].value, "NO CALL", None),
]
grid = [[70.72, 79.10, 87.48], [74.88, 83.78, 92.68], [81.12, 90.80, 100.48]]
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
