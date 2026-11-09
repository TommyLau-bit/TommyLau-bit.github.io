"""Recalculate the Williams model with LibreOffice headless, cache the values in the published file, and check outputs
against data.py, which drives every figure printed in the note and in src/content/calls/williams.md."""
import subprocess, sys, os, shutil, openpyxl
from data import *

TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/wmb_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

P, E, Ca, V, S, G, Dv, Pe, C = (wb[n] for n in ["Power", "EBITDA", "Cash", "Valuation", "Scenarios", "Sensitivity", "Dividend", "Peers", "Cover"])
checks = [
    ("MW total", P["B10"].value, MW_TOTAL, 0), ("EB per MW", P["B13"].value, EB_PER_MW, 3),
    ("per MW-day", P["B14"].value, EB_PER_MWDAY, 0), ("x PJM", P["B16"].value, EB_PER_MWDAY / PJM_CAP, 1),
    ("term", P["B17"].value, CONTRACT_YRS, 2), ("IRR 5x", P["B20"].value, IRR_5X, 3), ("PV term", P["B21"].value, CONTRACT_PV, 2),
    ("build ex", P["B18"].value, CAPEX_PI_EX / PI_RUN, 2), ("build incl", P["B19"].value, CAPEX_PI / PI_RUN, 2),
    ("PI 26", P["G10"].value, PI26, 0), ("PI 27", P["H10"].value, PI27, 0), ("PI 28", P["I10"].value, PI28, 0),
    ("core 26", E["D5"].value, CORE26, 0), ("core 27", E["E5"].value, CORE27, 0), ("core 28", E["F5"].value, CORE28, 0),
    ("mom 26", E["D7"].value, MOM26, 0), ("EB 26", E["D9"].value, EB26, 0), ("EB 27", E["E9"].value, EB27, 0),
    ("EB 28", E["F9"].value, EB28, 0), ("EB 30", E["B13"].value, EB30, 0), ("CAGR 30", E["B14"].value, CAGR30, 3),
    ("AFFO 27", Ca["D9"].value, AFFO27, 0), ("AFFO 28", Ca["E9"].value, AFFO28, 0),
    ("AFFO/sh 27", Ca["D11"].value, AFFO27 / SHARES, 2), ("AFFO/sh 28", Ca["E11"].value, AFFO28 / SHARES, 2),
    ("cover 27", Ca["D14"].value, AFFO27 / (DPS27 * SHARES), 2), ("ND 26", Ca["B18"].value, ND26, 0), ("ND 27", Ca["D18"].value, ND27, 0),
    ("lev 26", Ca["B19"].value, ND26 / (EB26 + MOM27 * 8 / 12), 2), ("lev 27", Ca["D19"].value, ND27 / EB27, 2),
    ("EV", V["B12"].value, BASE["ev"], 0), ("equity", V["B16"].value, BASE["eq"], 0), ("base", V["B18"].value, BASE_VALUE, 2),
    ("base vs px", V["B20"].value, UP_BASE, 3), ("band", V["B21"].value, "NO CALL", None),
    ("mcap", V["B23"].value, MCAP, 1), ("ND sep", V["B24"].value, ND_SEP, 0), ("EV now", V["B25"].value, EV_NOW, 1),
    ("EV/EB26", V["B26"].value, EV_EB26, 1), ("EV/EB27", V["B27"].value, EV_EB27, 1), ("impl power", V["B28"].value, IMPL_PI_MULT, 2),
    ("long below", V["B29"].value, LONG_BELOW, 2), ("short above", V["B30"].value, SHORT_ABOVE, 2),
    ("off high", V["B31"].value, OFF_HIGH, 3), ("ytd", V["B32"].value, YTD, 3), ("yield", V["B33"].value, YIELD, 3),
    ("cons tp", V["B34"].value, CONS_TP / PRICE - 1, 3),
    ("bear", S["I5"].value, SC[0]["value"], 2), ("base sc", S["I6"].value, SC[1]["value"], 2), ("bull", S["I7"].value, SC[2]["value"], 2),
    ("weighted", S["E11"].value, WEIGHTED, 2), ("base check", S["E12"].value, 0, 6),
    ("DDM", Dv["D17"].value, DDM_VALUE, 2), ("cover band", C["B5"].value, "NO CALL", None),
    ("peer median", Pe["C13"].value, 12.835, 3),
]
for i in range(3):
    for j in range(3):
        checks.append((f"grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, GRID[i][j], 2))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and not isinstance(got, str) and abs(got - want) < 0.5 * 10 ** -dp + 1e-9)
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:14s} model={got!r:>24}  data={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
