"""Recalculate the Ajinomoto model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures printed in the note and src/content/calls/ajinomoto.md (both are generated from data.py)."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):  # Excel-style half-up rounding, as the cells display
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/87f9daa0-8062-414d-a40b-cb592166359f/scratchpad/ajinomoto_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

Hs, Fc, Sp, Sc, G, Pe = (wb[n] for n in ["History", "Forecast", "SOTP", "Scenarios", "Sensitivity", "Peers"])
checks = [
    # headline figures printed in the note (hardcoded as published)
    ("Base value", Sp["B18"].value, 4369, 0), ("Base vs price", Sp["B19"].value, -0.18, 2),
    ("Weighted", Sc["B20"].value, 4450, 0), ("Bear", Sc["B17"].value, 2898, 0), ("Bull", Sc["D17"].value, 6164, 0),
    ("Bear chg", Sc["B18"].value, -0.46, 2), ("Bull chg", Sc["D18"].value, 0.15, 2),
    ("Median value", Sp["B27"].value, 3929, 0), ("Median chg", Sp["B28"].value, -0.27, 2),
    ("Revisit long", Sp["B25"].value, 3799, 0), ("Revisit short", Sp["B26"].value, 5825, 0),
    ("Film implied x", Sp["B33"].value, 39.7, 1), ("Film share EV mkt", Sp["B35"].value, 0.57, 2), ("Film share EV base", Sp["B24"].value, 0.49, 2),
    ("Food floor ps", Sp["B22"].value, 2024, 0), ("Film ps", Sp["B23"].value, 2345, 0),
    ("10% film mkt ps", Sp["B37"].value, 332, 0), ("10% film mkt pc", Sp["B38"].value, 0.062, 3),
    ("FY26E EPS", Fc["C21"].value, 135.1, 1), ("FY27E EPS", Fc["D21"].value, 150.5, 1),
    ("FY27E film net", Sp["C7"].value, 79.6, 1), ("FY27E other net", Sp["C8"].value, 131.3, 1),
    ("Food median", Pe["H13"].value, 17.0, 1), ("Elec median", Pe["H14"].value, 24.5, 1),
    ("Rule", Sp["B20"].value, "NO CALL", None), ("Draft view", Sp["B21"].value, CALL["direction"], None),
    # everything else against data.py
    ("FY26E sales", Fc["C9"].value, Y26["sales"], 1), ("FY27E sales", Fc["D9"].value, Y27["sales"], 1),
    ("FY26E BP", Fc["C16"].value, Y26["bp"], 1), ("FY27E BP", Fc["D16"].value, Y27["bp"], 1),
    ("FY26E NI", Fc["C20"].value, Y26["ni"], 1), ("FY27E NI", Fc["D20"].value, Y27["ni"], 1),
    ("FY26 guide BP (sum of rounded parts)", Fc["B16"].value, 201.8, 1),
    ("EV food", Sp["B12"].value, BASE["ev_food"], 1), ("EV film", Sp["B13"].value, BASE["ev_fm"], 1),
    ("EV mkt", Sp["B31"].value, EV_MKT, 1), ("Film EV implied", Sp["B32"].value, FM_IMPLIED_EV, 1),
    ("Film need at 28x", Sp["B34"].value, FM_IMPLIED_NET_AT_BASE_X, 1), ("Floor share", Sp["B36"].value, FOOD_FLOOR_SHARE, 3),
    ("10% film base", Sp["B39"].value, FM_10PCT_BASE_PS, 0), ("Turn film", Sp["B40"].value, FM_TURN_PS, 0), ("Turn food", Sp["B41"].value, FOOD_TURN_PS, 0),
    ("PE cons", Sp["B42"].value, PE_CONS26, 1), ("EV/OP cons", Sp["B43"].value, EV_OP_CONS, 1), ("EV/BP guide", Sp["B44"].value, EV_BP26_GUIDE, 1),
    ("Since Dec 25", Sp["B45"].value, SINCE_DEC25, 3), ("Off high", Sp["B46"].value, OFF_HIGH, 3),
    ("FY27E film share of net", Sp["C9"].value, FM_NET27_SHARE, 3),
    ("Grid above price", G["B9"].value, sum(v > PRICE for r in VGRID for v in r), 0),
    ("Grid 15% above", G["B10"].value, sum(v >= PRICE * 1.15 for r in VGRID for v in r), 0),
    ("Grid 25% below", G["B11"].value, sum(v <= PRICE * 0.75 for r in VGRID for v in r), 0),
    ("Grid centre = base", G["B12"].value, 0.0, 2), ("Scen base = SOTP", Sc["B23"].value, 0.0, 2), ("Weights", Sc["B22"].value, 1.0, 2),
]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, VGRID[i][j], 0))
for k, s in enumerate(SV):
    checks.append((f"Scenario {SCEN[k][0]}", Sc.cell(row=17, column=2 + k).value, s["value"], 0))
for k, p in enumerate(PEERS + REF_PEERS):
    checks.append((f"EV/OI {p[0]}", Pe.cell(row=5 + k, column=8).value, PEER_EVEBIT[p[0]], 1))
# shares of sales and profit, FY2025 and FY2026 guide
hrow = {Hs.cell(row=r, column=1).value: r for r in range(1, Hs.max_row + 1)}
for lab, arr in [("Functional Materials, share of sales", FM_SALES_SHARE),
                 ("Functional Materials, share of segment business profit (before shared costs)", FM_BP_SHARE_SEG),
                 ("Functional Materials, share of group business profit", FM_BP_SHARE_GRP)]:
    for j in range(5):
        checks.append((f"{lab[:40]} {SEG_COLS[j]}", Hs.cell(row=hrow[lab], column=2 + j).value, arr[j], 3))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (isinstance(got, (int, float)) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:46s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)   # publish the recalculated file so previews show values
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
