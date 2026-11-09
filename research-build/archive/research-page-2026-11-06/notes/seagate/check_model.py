"""Recalculate the Seagate model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures in data.py, which the note and src/content/calls/seagate.md print."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/stx_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

F, V, S, G, Qt, Pe, N = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Peers", "Normal"])
sb, sm, su = SV
checks = [
    ("FY26 revenue (sum of quarters)", Qt["B22"].value, FY26["rev"], 3), ("FY26 nearline EB, sum of quarters", Qt["B23"].value, 694, 0),
    ("Price per TB, 2-year avg", Qt["B24"].value, PTB_2Y, 2), ("Price per TB, FY26", Qt["B25"].value, PTB_26, 2),
    ("Price per TB Q1 FY27", Qt["J10"].value, Q_PTB[8], 2), ("Price per TB Q1 FY26", Qt["F10"].value, Q_PTB[4], 2),
    ("Price per TB up a year", Qt["J11"].value, PTB_UP, 3), ("NL EB up a year", Qt["B26"].value, NL_UP, 3),
    ("Q2 implied op margin", Qt["K13"].value, Q2_OM_IMPLIED, 3), ("Q3 EPS", Qt["L18"].value, Q27_EPS[2], 2), ("Q4 EPS", Qt["M18"].value, Q27_EPS[3], 2),
    ("Q1 FY27 net margin", Qt["B29"].value, Q1_NM, 3),
    ("FY27 revenue", F["D5"].value, REV27, 2), ("FY27 EPS", F["D10"].value, EPS27, 2), ("FY27 vs consensus", F["D12"].value, EPS27 / CONS_EPS_27 - 1, 3),
    ("FY27 net margin", F["D9"].value, NI27 / REV27, 3),
    ("FY28 revenue", F["E5"].value, REV28, 2), ("FY28 growth", F["E6"].value, G28, 4), ("FY28 EPS", F["E10"].value, EPS28, 2),
    ("FY28 vs consensus", F["E12"].value, EPS28 / CONS_EPS_28 - 1, 3), ("FY28 rev vs consensus", F["E13"].value, REV28 / CONS_REV_28 - 1, 3),
    ("FY28 net margin", F["E9"].value, NI28 / REV28, 3),
    ("P/E FY26", F["C14"].value, PE26, 1), ("P/E FY27 mine", F["D14"].value, PE27, 1), ("P/E FY28 mine", F["E14"].value, PE28, 1),
    ("P/E cons FY27", F["D15"].value, PEC27, 1), ("P/E cons FY28", F["E15"].value, PEC28, 1),
    ("FCF 12m", F["D19"].value, FCF_12M, 2), ("Net cash Oct 27", F["D20"].value, NC_OCT27, 2), ("Net cash per share", F["D21"].value, NC_PS, 2),
    ("Ten-year net margin", N["F17"].value, CYC_NM, 3), ("Ten-year gross margin", N["D17"].value, CYC_GM, 3), ("FY23 fall", N["B18"].value, FY23_REV_FALL, 2),
    ("Normal NL EB", N["B23"].value, NL_N, 0), ("Normal revenue", N["B28"].value, normal_rev(), 2), ("Normal EPS", N["B31"].value, N_BASE, 2),
    ("Excess per share", V["B6"].value, sm["exc"], 2), ("Normal value per share", V["B7"].value, sm["term"], 2),
    ("Base value", V["B8"].value, BASE_VALUE, 2), ("Base vs price", V["B10"].value, UP_BASE, 3), ("Weighted", V["B11"].value, WEIGHTED, 2),
    ("Rule on value", V["B12"].value, RULE, None), ("Draft view", V["B13"].value, CALL["direction"], None),
    ("Market value", V["B15"].value, MCAP, 1), ("EV", V["B16"].value, EV, 1), ("P/E normal", V["B22"].value, PE_NORMAL, 1),
    ("Need normal EPS", V["B24"].value, NEED_N, 2), ("Need margin", V["B25"].value, NEED_NM, 3), ("Need revenue", V["B26"].value, NEED_REV, 1),
    ("Need price per TB", V["B27"].value, NEED_PTB, 2), ("Need vs FY26", V["B28"].value, NEED_VS_26, 2), ("Need vs FY28", V["B29"].value, NEED_VS_28, 2),
    ("Revisit long price", V["B30"].value, REVISIT_LONG, 0), ("Revisit short price", V["B31"].value, REVISIT_SHORT, 0),
    ("Off high", V["B32"].value, OFF_HIGH, 3), ("Since Dec 25", V["B33"].value, SINCE_DEC25, 2), ("October fall", V["B34"].value, OCT_FALL, 3),
    ("Toshiba day", V["B35"].value, TOSHIBA_DAY, 3), ("P/E run rate", V["B36"].value, PE_RUN, 1),
    ("Bear FY28 EPS", S["L5"].value, sb["eps28"], 2), ("Bear normal EPS", S["K5"].value, sb["n"], 2), ("Bear value", S["P5"].value, VALS[0], 2),
    ("Base value (scenario)", S["P6"].value, VALS[1], 2),
    ("Bull FY28 EPS", S["L7"].value, su["eps28"], 2), ("Bull normal EPS", S["K7"].value, su["n"], 2), ("Bull value", S["P7"].value, VALS[2], 2),
    ("Weighted (scenario)", S["P12"].value, WEIGHTED, 2),
    ("Grid cells above price", G["B9"].value, sum(v > PRICE for r in VGRID for v in r), 0),
    ("Grid cells 25% below", G["B10"].value, sum(v <= PRICE * 0.75 for r in VGRID for v in r), 0),
    ("WDC P/E", Pe["F6"].value, PEER_PE[0][1], 1), ("SNDK P/E", Pe["F7"].value, PEER_PE[1][1], 1), ("MU P/E", Pe["F8"].value, PEER_PE[2][1], 1),
    ("STX P/E", Pe["F5"].value, PEC27, 1),
]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, VGRID[i][j], 0))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (isinstance(got, (int, float)) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:28s} model={got!r:>24}  data={want!r}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
