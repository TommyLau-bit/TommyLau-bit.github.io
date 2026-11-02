"""Recalculate the SK hynix model with LibreOffice headless, cache the values in the published file, and check outputs
against data.py and the figures printed in the note and src/content/calls/sk-hynix.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/skh_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

F, V, S, G, Q, Pe, N, H = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Peers", "Normal", "HBM"])
# (name, model value, published figure, decimals). Published figures are as printed in the md and PDF.
checks = [
    ("Q1-Q3 2026 revenue", Q["B12"].value, 236.51, 2), ("2024 revenue sum", Q["B13"].value, 66.193, 3),
    ("2025 revenue sum", Q["B14"].value, 97.147, 2), ("Normal base revenue", Q["B15"].value, 189.17, 2),
    ("Q3 26 yoy growth", Q["B16"].value, 3.28, 2), ("Q3 26 op margin", Q["L7"].value, 0.80, 2), ("Q3 25 op margin", Q["H7"].value, 0.47, 2),
    ("HBM 2025", H["B8"].value, 28.8, 1), ("HBM 2026", H["C8"].value, 39.3, 1), ("HBM 2027", H["D8"].value, 46.3, 1),
    ("HBM share 2025", H["B10"].value, 0.30, 2), ("HBM share 2026", H["C10"].value, 0.11, 2), ("HBM share 2027", H["D10"].value, 0.09, 2),
    ("HBM share of 2026 OP", H["C13"].value, 0.08, 2),
    ("2026 revenue", F["D5"].value, 364.5, 1), ("2026 OP", F["D8"].value, 283.9, 1), ("2026 OPM", F["D9"].value, 0.779, 3),
    ("2026 net margin", F["D11"].value, 0.696, 3), ("2026 EPS", F["D12"].value, 359567, 0), ("2026 vs cons", F["D14"].value, 0.002, 3),
    ("2027 revenue vs cons", F["E7"].value, -0.063, 3), ("2027 OP", F["E8"].value, 410.4, 1), ("2027 net margin", F["E11"].value, 0.593, 3),
    ("2027 EPS", F["E12"].value, 453948, 0), ("2027 vs cons", F["E14"].value, -0.139, 3),
    ("2028 revenue", F["F5"].value, 486.0, 1), ("2028 OP", F["F8"].value, 330.5, 1), ("2028 net margin", F["F11"].value, 0.530, 3),
    ("2028 EPS", F["F12"].value, 365548, 0),
    ("2025 net margin", F["C11"].value, 0.442, 3), ("2025 OPM", F["C9"].value, 0.486, 3), ("2024 OPM", F["B9"].value, 0.355, 3),
    ("P/E 2025", F["C15"].value, 24.4, 1), ("P/E 2026", F["D15"].value, 4.1, 1), ("P/E 2027", F["E15"].value, 3.2, 1),
    ("P/E 2028", F["F15"].value, 4.0, 1), ("P/E cons 2027", F["E16"].value, 2.8, 1),
    ("FCF Q4 26", F["D18"].value, 65, 0), ("FCF 27", F["E18"].value, 257, 0), ("Net cash Sep 27", F["E19"].value, 338, 0),
    ("Net cash/sh Sep 27", F["E20"].value, 479300, -2), ("Net cash/sh now", F["D21"].value, 127159, 0),
    ("Ten-year net margin", N["D16"].value, 0.235, 3), ("2018 net margin", N["D17"].value, 0.384, 3),
    ("Normal revenue", N["B23"].value, 215.7, 1), ("Normal EPS", N["B26"].value, 91784, 0),
    ("Excess/sh", V["B6"].value, 452500, -2), ("Normal value/sh", V["B7"].value, 1101400, -2),
    ("Base value", V["B8"].value, 2033000, -3), ("Base vs price", V["B10"].value, 0.38, 2), ("Weighted", V["B11"].value, 2139000, -3),
    ("Rule", V["B12"].value, "LONG", None), ("Draft view", V["B13"].value, "LONG", None), ("Target", V["B14"].value, 2000000, 0),
    ("Market value KRW tn", V["B15"].value, 1038, 0), ("Market value US$bn", V["B16"].value, 774, 0),
    ("Need EPS cash kept", V["B20"].value, 38000, -2), ("Need margin cash kept", V["B21"].value, 0.124, 3),
    ("Need EPS cash spent", V["B22"].value, 83900, -2), ("Need margin cash spent", V["B23"].value, 0.274, 3),
    ("Base without cash", V["B24"].value, 1554000, -3), ("without cash vs price", V["B25"].value, 0.06, 2),
    ("Base half cash", V["B26"].value, 1790000, -4), ("half cash vs price", V["B27"].value, 0.22, 2),
    ("Revisit price", V["B28"].value, 1768000, -3), ("P/E normal", V["B32"].value, 16.0, 1),
    ("Off high", V["B33"].value, -0.50, 2), ("ADS premium", V["B34"].value, 0.41, 2),
    ("Bear 2027 EPS", S["M5"].value, 356200, -2), ("Bear normal EPS", S["L5"].value, 42300, -2), ("Bear value", S["R5"].value, 1004000, -3), ("Bear chg", S["S5"].value, -0.32, 2),
    ("Base 2027 EPS", S["M6"].value, 453900, -2), ("Base normal EPS", S["L6"].value, 91800, -2), ("Base chg", S["S6"].value, 0.38, 2),
    ("Bull 2027 EPS", S["M7"].value, 530900, -2), ("Bull normal EPS", S["L7"].value, 155800, -2), ("Bull value", S["R7"].value, 3484000, -3), ("Bull chg", S["S7"].value, 1.37, 2),
    ("Bear normal revenue", S["L5"].value * SH / 1e6 / 0.19, 157, 0), ("Weighted vs price", S["S12"].value, 0.45, 2),
    ("Grid above price", G["B9"].value, 9, 0), ("Grid lowest vs price", G["B10"].value, 0.12, 2),
    ("Samsung P/E", Pe["G6"].value, 3.0, 1), ("Micron P/E", Pe["G7"].value, 5.0, 1), ("SK P/E", Pe["G5"].value, 2.8, 1),
]
grid = [[1643000, 1778000, 1913000], [1850000, 2033000, 2217000], [2056000, 2288000, 2521000]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], -3))
# and every model output against data.py
checks += [("data: base", V["B8"].value, BASE_VALUE, 0), ("data: weighted", V["B11"].value, WEIGHTED, 0),
           ("data: need", V["B20"].value, NEED_N, 0), ("data: need0", V["B22"].value, NEED_N_NOCASH, 0),
           ("data: bear", S["R5"].value, VALS[0], 0), ("data: bull", S["R7"].value, VALS[2], 0), ("data: NC/sh", F["E20"].value, NC_PS, 0)]

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (isinstance(got, (int, float)) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:28s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
