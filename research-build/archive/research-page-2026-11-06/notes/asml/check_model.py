"""Recalculate the ASML model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures printed in the note and src/content/calls/asml.md (both are generated from data.py)."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):  # Excel-style half-up rounding, as the cells display
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/87f9daa0-8062-414d-a40b-cb592166359f/scratchpad/asml_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

F, V, S, G, Sg, Pe, Dc, Q = (wb[n] for n in ["Financials", "Valuation", "Scenarios", "Sensitivity", "Segments", "Peers", "DCF", "Quarterly"])
checks = [
    # headline figures printed in the note (hardcoded as published)
    ("Base value", V["B5"].value, 1697, 0), ("Base vs price", V["B8"].value, 0.04, 2), ("Weighted", V["B6"].value, 1653, 0),
    ("Bear value", S["R5"].value, 1013, 0), ("Bull value", S["R7"].value, 2208, 0),
    ("Bear chg", S["S5"].value, -0.38, 2), ("Bull chg", S["S7"].value, 0.35, 2),
    ("FY26 EPS", F["E18"].value, 39.49, 2), ("FY27 EPS", F["F18"].value, 50.78, 2), ("FY28 EPS", F["G18"].value, 60.59, 2),
    ("FY26 revenue", F["E5"].value, 43960, 0), ("FY27 revenue", F["F5"].value, 52956, 0), ("FY28 revenue", F["G5"].value, 60612, 0),
    ("DCF value", Dc["B17"].value, 1226, 0), ("DCF value 115%", Dc["B24"].value, 1481, 0), ("Reverse DCF 115% = price", Dc["B27"].value, PRICE, 0), ("Revisit long", V["B12"].value, 1475, 0), ("Revisit short", V["B13"].value, 2262, 0),
    ("Need units", V["B15"].value, 93.65, 2), ("Need EPS", V["B14"].value, 58.44, 2), ("Reverse DCF value = price", Dc["B22"].value, PRICE, 0),
    ("Price-implied value = price", S["R8"].value, PRICE, 0),
    ("Peer median", Pe["G10"].value, 36.1, 1), ("ADR P/E 27", Pe["G5"].value, 31.5, 1),
    # everything else against data.py
    ("Low NA ASP 2026", Sg["E6"].value, LNA_ASP26, 1), ("Low NA ASP 2027", Sg["F6"].value, Y27["asp"], 1),
    ("EUV 2026", Sg["E10"].value, Y26["euv"], 0), ("EUV 2027", Sg["F10"].value, Y27["euv"], 0), ("EUV 2028", Sg["G10"].value, Y28["euv"], 0),
    ("Non-EUV 2028", Sg["G12"].value, Y28["noneuv"], 0), ("IBM 2028", Sg["G14"].value, Y28["ibm"], 0),
    ("China 2025", Sg["D19"].value, CHINA_SH[2], 3), ("China 2024", Sg["C19"].value, CHINA_SH[1], 3),
    ("Sys GM 2025", Sg["D20"].value, SYS_GM_H[2], 3), ("IBM GM 2025", Sg["D21"].value, IBM_GM_H[2], 3),
    ("IBM H1 growth", Q["B12"].value, IBM_G_H126, 3), ("EUV Q1 26", Q["B13"].value, EUV_Q126, 0),
    ("FY26 cons P/E", V["B21"].value, PE_C26, 1), ("FY27 cons P/E", V["B23"].value, PE_C27, 1), ("FY26 SA P/E", V["B22"].value, PE_C26_SA, 1),
    ("PE27 mine", V["B25"].value, PE27, 1), ("PE28 mine", V["B26"].value, PE28, 1),
    ("Mine vs cons 26", F["E22"].value, EPS26 / CONS_EPS_26 - 1, 3), ("Mine vs cons 27", F["F22"].value, EPS27 / CONS_EPS_27 - 1, 3),
    ("Mcap", V["B16"].value, MCAP, 1), ("EV", V["B18"].value, EV, 1), ("EV/EBIT 27", V["B19"].value, EV_EBIT27, 1),
    ("EV/EBIT 28 base", V["B20"].value, EV_EBIT28_BASE, 1), ("Fwd PE dec24", V["B29"].value, FWD_PE_DEC24, 1),
    ("Fwd PE dec25", V["B30"].value, FWD_PE_DEC25, 1), ("Off high", V["B31"].value, OFF_HIGH, 3), ("Up from low", V["B32"].value, UP_YEAR, 3),
    ("Since Dec 25", V["B33"].value, SINCE_DEC25, 3), ("Backlog months", V["B34"].value, BACKLOG_MONTHS, 1), ("Target EUR", V["B35"].value, CONS_TP_USD / EURUSD, 0),
    ("Rule", V["B9"].value, "NO CALL", None), ("Draft view", V["B10"].value, CALL["direction"], None),
    ("Grid above price", G["B9"].value, sum(v > PRICE for r in VGRID for v in r), 0),
    ("Grid 15% above", G["B10"].value, sum(v >= PRICE * 1.15 for r in VGRID for v in r), 0),
    ("Grid 25% below", G["B11"].value, sum(v <= PRICE * 0.75 for r in VGRID for v in r), 0),
    ("Weights", S["E11"].value, 1.0, 2),
]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, VGRID[i][j], 0))
for k, (n, pe) in enumerate(PEER_PE):
    checks.append((f"P/E {n}", Pe.cell(row=6 + k, column=7).value, pe, 1))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (isinstance(got, (int, float)) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:30s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)   # publish the recalculated file so previews show values
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
