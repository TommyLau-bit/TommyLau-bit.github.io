"""Recalculate the Schneider Electric model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures in data.py, which drive the note and src/content/calls/schneider-electric.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(float(x))).quantize(q, rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/87f9daa0-8062-414d-a40b-cb592166359f/scratchpad/su/recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

F, P, S, V, G, Q, Pe = (wb[n] for n in ["Financials", "PTC", "Scenarios", "Valuation", "Sensitivity", "Quarterly", "Peers"])
checks = [
    ("2024 adj NI", F["B13"].value, ADJ_NI_H[0], 0), ("2025 adj NI", F["C13"].value, ADJ_NI_H[1], 0),
    ("2026 revenue", F["D5"].value, REV26, 0), ("2027 revenue", F["E5"].value, REV27, 0), ("2028 revenue", F["F5"].value, REV28, 0),
    ("2028 revenue with PTC", F["G5"].value, PT["rev"], 0),
    ("2026 EBITA", F["D8"].value, EBITA26, 0), ("2027 EBITA", F["E8"].value, EBITA27, 0), ("2028 EBITA", F["F8"].value, EBITA28, 0),
    ("2027 margin", F["E7"].value, ST["m"][1], 4), ("2028 margin", F["F7"].value, ST["m"][2], 4),
    ("2026 EPS", F["D15"].value, EPS26, 2), ("2027 EPS", F["E15"].value, EPS27, 2), ("2028 EPS", F["F15"].value, EPS28, 2),
    ("2028 EPS with PTC", F["G15"].value, EPS28_PTC, 2),
    ("2026 vs cons", F["D19"].value, EPS26 / CONS_EPS_26 - 1, 3), ("2027 vs cons", F["E19"].value, EPS27 / CONS_EPS_27 - 1, 3),
    ("P/E 2026 mine", F["D17"].value, PE26, 1), ("P/E 2027 mine", F["E17"].value, PE27, 1), ("P/E 2028 PTC", F["G17"].value, PE28_PTC, 1),
    ("PTC EBITA 27", P["B5"].value, PTC_EBITA27, 0), ("PTC EBITA 28 syn", P["B10"].value, PT["ptc_ebita"], 0),
    ("New shares", P["B11"].value, NEW_SH, 1), ("Interest", P["B13"].value, PT["interest"], 0), ("Shares 28 PTC", P["B16"].value, SH_PTC28, 1),
    ("Accretion reported", P["B17"].value, ACCR_REPORTED, 3), ("Accretion pre-PPA", P["B20"].value, ACCR_PRE_PPA, 3),
    ("ND end 26", P["B21"].value, ND_END26, 0), ("ND close", P["B23"].value, ND_CLOSE, 0),
    ("Lev 25", P["B24"].value, LEV_25, 2), ("ND pre-close", P["B22"].value, ND_CLOSE_PRE, 0), ("Lev close", P["B25"].value, LEV_CLOSE, 2),
    ("Bear value", S["Q5"].value, VALS[0], 1), ("Base value", S["Q6"].value, VALS[1], 1), ("Bull value", S["Q7"].value, VALS[2], 1),
    ("Bear EPS", S["P5"].value, SV[0]["eps"], 2), ("Bull EPS", S["P7"].value, SV[2]["eps"], 2),
    ("Price-implied value", S["Q8"].value, PRICE, 1), ("Weighted", S["Q13"].value, WEIGHTED, 1),
    ("Standalone value", V["B6"].value, BASE_STANDALONE, 1), ("Deal cost", V["B7"].value, DEAL_COST_PS, 1),
    ("Base vs price", V["B9"].value, BASE_VALUE / PRICE - 1, 3), ("Rule", V["B12"].value, "NO CALL", None),
    ("Draft view", V["B13"].value, CALL["direction"], None),
    ("Revisit long", V["B15"].value, REVISIT_LONG, 1), ("Revisit short", V["B16"].value, REVISIT_SHORT, 1),
    ("Mcap", V["B17"].value, MCAP, 1), ("Lost", V["B19"].value, MCAP_LOST, 1), ("Drop", V["B20"].value, DROP, 3),
    ("Legrand", V["B21"].value, LEGRAND_CHG, 3), ("PE c26", V["B22"].value, PE_C26, 1), ("PE c27", V["B23"].value, PE_C27, 1),
    ("PE c27 pre", V["B24"].value, PE_C27_PRE, 1), ("Need EPS", V["B26"].value, NEED_EPS, 2), ("Need org", V["B27"].value, NEED_ORG, 3),
    ("Peer median", V["B28"].value, PEER_MED, 1), ("Peer value", V["B29"].value, EPS26 * PEER_MED, 1),
    ("Sys share Q2 growth", Q["B18"].value, SYS_CONTRIB_SHARE, 3), ("Sys share H1 26", Q["B19"].value, SYS_H126, 4),
    ("Grid above price", G["B9"].value, sum(v > PRICE for r in VGRID for v in r), 0),
    ("Grid 15% above", G["B10"].value, sum(v >= PRICE * 1.15 for r in VGRID for v in r), 0),
    ("Grid 25% below", G["B11"].value, sum(v <= PRICE * 0.75 for r in VGRID for v in r), 0),
]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, VGRID[i][j], 1))
for i, (n, pe) in enumerate(PEER_PE):
    checks.append((f"Peer {n}", Pe.cell(row=6 + i, column=5).value, pe, 1))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:24s} model={got!r:>24}  data={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
