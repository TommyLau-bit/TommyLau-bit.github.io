"""Recalculate the Caterpillar model with LibreOffice headless, cache the values in the published file, and check
outputs against data.py, which drives the note and src/content/calls/caterpillar.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/cat_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]
Sg, E, V, S, G_, B_, Pe, C = (wb[n] for n in ["Segments", "EPS", "Valuation", "Scenarios", "Sensitivity", "Backlog", "Peers", "Cover"])
checks = [
    ("PG 2026E", Sg["D5"].value, Y26["app"]["PG"], 0), ("PG 2027E", Sg["E5"].value, Y27["app"]["PG"], 0), ("PG 2028E", Sg["F5"].value, Y28["app"]["PG"], 0),
    ("PE sales 2026E", Sg["D10"].value, Y26["pe_s"], 0), ("PE sales 2028E", Sg["F10"].value, Y28["pe_s"], 0),
    ("PE margin 2026E", Sg["D12"].value, Y26["pe_p"] / Y26["pe_s"], 3), ("PE margin 2025A", Sg["C12"].value, 0.219, 3),
    ("CI sales 2026E", Sg["D16"].value, Y26["ci_s"], 0), ("CI margin 2026E", Sg["D18"].value, 0.213, 3),
    ("RI sales 2026E", Sg["D21"].value, Y26["ri_s"], 0), ("RI margin 2026E", Sg["D23"].value, 0.127, 3),
    ("Seg profit 2026E", Sg["D28"].value, Y26["seg"], 0), ("Seg profit 2028E", Sg["F28"].value, Y28["seg"], 0),
    ("PG share 2026E", Sg["D29"].value, Y26["pg_share"], 3), ("PG share 2028E", Sg["F29"].value, Y28["pg_share"], 3),
    ("PE share of seg 2025", Sg["C13"].value / Sg["C28"].value, 0.445, 3),
    ("EPS 2026E", E["D14"].value, E26, 2), ("EPS 2027E", E["E14"].value, E27, 2), ("EPS 2028E", E["F14"].value, E28, 2),
    ("EPS 2026E printed", E["D14"].value, 27.28, 2), ("EPS 2027E printed", E["E14"].value, 29.95, 2), ("EPS 2028E printed", E["F14"].value, 32.53, 2),
    ("2027 vs cons", E["E17"].value, E27 / CONS_EPS27 - 1, 3), ("PG EPS", E["F18"].value, PG_EPS, 2), ("Rest EPS", E["F19"].value, REST_EPS, 2),
    ("Base value", V["B11"].value, BASE_VALUE, 2), ("Base printed", V["B11"].value, 599.70, 2), ("Base vs price", V["B13"].value, UP_BASE, 3),
    ("Band", V["B14"].value, "NO CALL", None), ("PG share of value", V["B15"].value, PG_SHARE_BASE, 3), ("Blended PE", V["B16"].value, BLENDED_PE, 1),
    ("Implied PG PE", V["B18"].value, IMPLIED_PG_PE, 1), ("Implied PG PE peak", V["B19"].value, IMPLIED_PG_PE_PEAK, 1),
    ("PG share price", V["B20"].value, PG_SHARE_PRICE, 3), ("PG share peak", V["B21"].value, PG_SHARE_PEAK, 3),
    ("Mcap", V["B23"].value, MCAP, 1), ("Net debt", V["B24"].value, NET_DEBT_MPE, 0), ("PE c26", V["B25"].value, PE_C26, 1),
    ("PE c27", V["B26"].value, PE_C27, 1), ("PE e26", V["B27"].value, PE_E26, 1), ("PE e27", V["B28"].value, PE_E27, 1),
    ("PE e28", V["B29"].value, PE_E28, 1), ("PE peak c27", V["B30"].value, PE_PEAK_C27, 1), ("Long below", V["B31"].value, LONG_BELOW, 0),
    ("Short above", V["B32"].value, SHORT_ABOVE, 0), ("Off high", V["B33"].value, OFF_HIGH, 3), ("YTD", V["B34"].value, YTD, 3),
    ("Bear EPS", S["R5"].value, SC[0]["e28"], 2), ("Bear value", S["T5"].value, SC[0]["value"], 1), ("Base scen", S["T6"].value, SC[1]["value"], 1),
    ("Bull EPS", S["R7"].value, SC[2]["e28"], 2), ("Bull value", S["T7"].value, SC[2]["value"], 1), ("Weighted", S["E11"].value, WEIGHTED, 1),
    ("Base check", S["E12"].value, 0, 6),
    ("Grid above", G_["B9"].value, 3, 0), ("Grid 15", G_["B10"].value, 1, 0), ("Grid 25 below", G_["B11"].value, 1, 0),
    ("BL years Dec24", B_["B11"].value, 0.46, 2), ("BL years Sep26", B_["B12"].value, 1.00, 2), ("BL growth", B_["B13"].value, 0.962, 3),
    ("Adv growth", B_["B15"].value, 0.608, 3), ("PG Q3 growth", B_["L19"].value, 0.299, 3),
    ("Power median", Pe["C16"].value, 21.81, 2), ("Cycle median", Pe["C17"].value, 15.22, 2), ("Hist avg", Pe["C18"].value, 16.34, 2),
    ("Cover view", C["B5"].value, "NO CALL", None),
]
grid = [[PG_EPS * a + REST_EPS * b for b in SENS_REST] for a in SENS_PG]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G_.cell(row=5 + i, column=2 + j).value, grid[i][j], 1))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and not isinstance(got, str) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:22s} model={got!r:>24}  want={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
