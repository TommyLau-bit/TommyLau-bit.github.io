"""Recalculate the Nvidia model with LibreOffice headless, cache the values in the published file, and check its
outputs against data.py, the single source the note and src/content/calls/nvidia.md print from."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/nvda_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

Q, F, G, S, Se, V, Pe = (wb[n] for n in ["Quarterly", "Financials", "Gigawatts", "Scenarios", "Sensitivity", "Valuation", "Peers"])
pb, pbear, pbull = (project(*s[1:8]) for s in (SCEN[1], SCEN[0], SCEN[2]))
checks = [
    # Quarterly
    ("DC share Q2 FY27", Q["B17"].value, DC_SHARE_Q2, 3), ("DC growth Q2 FY27", Q["B18"].value, DC_G_Q2, 3),
    ("Q3E OM", Q["B19"].value, OP_Q3 / G3["rev"], 3), ("Q3E EPS", Q["B20"].value, EPS_Q3, 2), ("Q4E EPS", Q["B21"].value, EPS_Q4, 2),
    # Financials
    ("FY27 revenue", F["D7"].value, REV27, 1), ("FY27 DC", F["D5"].value, DC27, 1), ("FY27 OM", F["D10"].value, OM27, 3),
    ("FY27 EPS", F["D15"].value, EPS27, 2), ("FY27 vs cons", F["D19"].value, EPS27_VS_CONS, 3),
    ("FY28 revenue", F["E7"].value, pb["rev28"], 1), ("FY28 DC", F["E5"].value, pb["dc28"], 1), ("FY28 EPS", F["E15"].value, pb["eps28"], 2),
    ("FY28 vs cons", F["E19"].value, EPS28_VS_CONS, 3), ("FY28 rev vs cons", F["E22"].value, REV28_VS_CONS, 3),
    ("FY29 revenue", F["F7"].value, pb["rev29"], 1), ("FY29 DC", F["F5"].value, pb["dc29"], 1), ("FY29 EPS", F["F15"].value, pb["eps29"], 2),
    ("P/E FY27", F["D17"].value, PE27, 1), ("P/E FY28", F["E17"].value, PE28, 1), ("P/E FY29", F["F17"].value, PE29, 1),
    ("P/E cons FY27", F["D20"].value, PEC27, 1), ("P/E cons FY28", F["E20"].value, PEC28, 1),
    # Gigawatts
    ("US$/GW low", G["B5"].value, USD_PER_GW[0], 1), ("US$/GW high", G["B6"].value, USD_PER_GW[1], 1),
    ("US$/GW FY29", G["B7"].value, USD_GW_29, 1), ("US$/GW FY28", G["B8"].value, USD_GW_28, 1), ("US$/GW FY27", G["B9"].value, USD_GW_27, 1),
    ("Nvidia/Vertiv low", G["B12"].value, NV_TO_VERTIV[0], 1), ("Nvidia/Vertiv high", G["B13"].value, NV_TO_VERTIV[1], 1),
    ("GW FY26", G["D16"].value, GW_FY26, 1), ("GW FY27", G["D17"].value, GW27, 1), ("GW FY28", G["D18"].value, pb["gw28"], 1),
    ("GW FY28 cons", G["D19"].value, GW28_CONS, 1), ("GW FY29", G["D20"].value, pb["gw29"], 1),
    ("GW FY27 low", G["E17"].value, GW_RANGE(DC27, USD_GW_27)[0], 1), ("GW FY27 high", G["F17"].value, GW_RANGE(DC27, USD_GW_27)[1], 1),
    ("Cons GW growth", G["B22"].value, CONS_GW_G, 3), ("FY27 GW undeflated low", G["B24"].value, DC27 / USD_PER_GW[1], 1),
    ("FY27 GW undeflated high", G["B25"].value, DC27 / USD_PER_GW[0], 1),
    # Scenarios
    ("Bear value", S["P5"].value, VALS[0], 0), ("Base value", S["P6"].value, VALS[1], 0), ("Bull value", S["P7"].value, VALS[2], 0),
    ("Bear EPS29", S["O5"].value, pbear["eps29"], 2), ("Bull EPS29", S["O7"].value, pbull["eps29"], 2), ("Bull EPS28", S["N7"].value, pbull["eps28"], 2),
    ("Bear chg", S["Q5"].value, VALS[0] / PRICE - 1, 2), ("Bull chg", S["Q7"].value, VALS[2] / PRICE - 1, 2),
    ("Weighted", S["P8"].value, WEIGHTED, 0), ("Weights sum", S["I8"].value, 1.0, 2),
    # Sensitivity
    ("Cells above", Se["B9"].value, sum(v > PRICE for r in VGRID for v in r), 0),
    ("Cells 15% above", Se["B10"].value, sum(v > PRICE * 1.15 for r in VGRID for v in r), 0),
    # Valuation
    ("Market value", V["B5"].value, MCAP, 0), ("Net cash", V["B6"].value, NETCASH, 1), ("EV", V["B7"].value, EV, 0),
    ("Base vs price", V["B11"].value, BASE_VALUE / PRICE - 1, 3), ("Rule", V["B13"].value, "LONG", None),
    ("Call", V["B14"].value, CALL["direction"], None), ("Target", V["B15"].value, CALL["target"], 0),
    ("Need EPS29", V["B16"].value, NEED_EPS29, 2), ("EPS29 flat", V["B17"].value, eps29_flat(0.0), 2),
    ("Off high", V["B23"].value, OFF_HIGH, 3), ("Since Dec 25", V["B24"].value, RISE_DEC25, 3),
    ("Peer median", Pe["C12"].value, 19.05, 2),
]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", Se.cell(row=5 + i, column=2 + j).value, VGRID[i][j], 0))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:26s} model={got!r:>24}  data={want!r}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
