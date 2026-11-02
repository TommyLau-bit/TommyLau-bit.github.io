"""Recalculate the Samsung Electronics model with LibreOffice headless, cache the values in the published file, and check
outputs against data.py and the figures printed in the note and src/content/calls/samsung-electronics.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    q = Decimal(1).scaleb(-dp)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))


TMP = "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/sam_recalc"
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)

errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith("#")]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

I, F, V, S, G, Q, Pe, H, Hs = (wb[n] for n in ["Inputs", "Financials", "Valuation", "Scenarios", "Sensitivity", "Quarterly", "Peers", "HBM", "History"])
inp = {I.cell(row=r, column=1).value: I.cell(row=r, column=2).value for r in range(5, I.max_row + 1)}
# (name, model value, published figure, decimals). Published figures are as printed in the md and PDF.
checks = [
    ("Preferred shares m", inp["Preferred shares, m"], 802, 0), ("Common shares m", inp["Common outstanding, m"], 5710, 0),
    ("Market value", inp["Market value, both classes, KRW tn"], 1450, 0), ("Market value US$", inp["Market value, US$bn"], 1080, 0),
    ("Pref gap", inp["Preferred discount to common"], 0.227, 3),
    ("Chips share 9M", Q["B16"].value, 0.98, 2), ("Q3 26 op margin", Q["H14"].value, 0.55, 2), ("Q1 25 chips share", Q["B13"].value, 0.16, 2),
    ("2026 memory", F["C5"].value, 506.3, 1), ("2026 revenue", F["C6"].value, 720.8, 1), ("2026 OP", F["C10"].value, 386.1, 1),
    ("2026 chip OP", F["C8"].value, 380.8, 1), ("2026 EPS", F["C13"].value, 44834, 0), ("2026 vs cons", F["C15"].value, -0.029, 3),
    ("2027 revenue", F["D6"].value, 967.0, 1), ("2027 vs cons rev", F["D7"].value, -0.041, 3), ("2027 OP", F["D10"].value, 585.8, 1),
    ("2027 EPS", F["D13"].value, 68368, 0), ("2027 vs cons", F["D15"].value, -0.096, 3), ("2027 memory net margin", F["D19"].value, 0.578, 3),
    ("2028 revenue", F["E6"].value, 903.0, 1), ("2028 memory", F["E5"].value, 684.0, 1), ("2028 OP", F["E10"].value, 478.9, 1),
    ("2028 EPS", F["E13"].value, 55894, 0), ("2028 memory net margin", F["E19"].value, 0.517, 3),
    ("P/E 2025", F["B16"].value, 34.7, 1), ("P/E 2026", F["C16"].value, 5.1, 1), ("P/E 2027", F["D16"].value, 3.3, 1),
    ("P/E 2028", F["E16"].value, 4.1, 1), ("P/E cons 2027", F["D17"].value, 3.0, 1),
    ("FCF Q4", F["C21"].value, 77, 0), ("FCF 27", F["D21"].value, 362, 0), ("Net cash now", F["C22"].value, 165, 0),
    ("Net cash Sep 27", F["D23"].value, 514, 0), ("Net cash/sh", F["D24"].value, 79000, -3),
    ("HBM 2025", H["B12"].value, 9.6, 1), ("HBM 2026", H["C12"].value, 31.6, 1), ("HBM 2027", H["D12"].value, 32.4, 1),
    ("HBM share 26", H["C14"].value, 0.06, 2), ("HBM share 27", H["D14"].value, 0.04, 2), ("HBM industry share 26", H["C15"].value, 0.44, 2),
    ("Normal memory", V["B5"].value, 295.8, 1), ("Normal memory profit", V["B6"].value, 88.8, 1),
    ("Excess", V["B8"].value, 438, 0), ("Normal value", V["B9"].value, 1065, 0), ("Phones", V["B11"].value, 91, 0),
    ("Foundry", V["B10"].value, 41, 0), ("Other three", V["B12"].value + V["B13"].value + V["B14"].value, 47, 0), ("Investments", V["B15"].value, 73, 0),
    ("Gross", V["B16"].value, 2269, 0), ("Gross/sh", V["C16"].value, 348400, -2), ("Discount/sh", V["C17"].value, -69700, -2),
    ("Base value", V["C18"].value, 278700, -2), ("Base vs price", V["C19"].value, 0.22, 2), ("Base vs pref", V["C20"].value, 0.57, 2),
    ("Rule", V["C21"].value, "LONG", None), ("Draft", V["C22"].value, "LONG", None), ("Target", V["C23"].value, 270000, 0),
    ("Revisit", V["C24"].value, 242300, -2), ("No cash", V["C25"].value, 215500, -2), ("No cash vs price", V["C26"].value, -0.06, 2),
    ("Need no disc", V["C29"].value, 0.035, 3), ("Need disc", V["C30"].value, 0.152, 3), ("Need disc no cash", V["C31"].value, 0.319, 3),
    ("Need no disc tn", V["B29"].value, 10, 0),
    ("Disc 0", V["C34"].value, 348400, -2), ("Disc 10", V["C35"].value, 313500, -2), ("Disc 30", V["C37"].value, 243900, -2),
    ("Bear 2027 EPS", S["B21"].value, 53700, -2), ("Bear normal", S["B25"].value, 40.9, 1), ("Bear value", S["B29"].value, 156200, -2), ("Bear chg", S["B30"].value, -0.32, 2),
    ("Base 2027 EPS", S["C21"].value, 68400, -2), ("Base normal", S["C25"].value, 88.8, 1), ("Base value scen", S["C29"].value, 278700, -2),
    ("Bull 2027 EPS", S["D21"].value, 79400, -2), ("Bull normal", S["D25"].value, 150.6, 1), ("Bull value", S["D29"].value, 450200, -2), ("Bull chg", S["D30"].value, 0.97, 2),
    ("Bear normal rev", S["B24"].value, 215, 0), ("Bull normal rev", S["D24"].value, 377, 0),
    ("Weighted", S["B32"].value, 290900, -2), ("Weighted vs price", S["B33"].value, 0.27, 2),
    ("Grid above", G["B9"].value, 9, 0), ("Grid lowest vs price", G["B10"].value, 0.015, 3),
    ("Samsung P/E", Pe["F5"].value, 3.0, 1), ("SK P/E", Pe["F6"].value, 2.8, 1), ("Micron P/E", Pe["F7"].value, 5.0, 1),
    ("DS 2017-25 margin", Hs["D14"].value, 0.238, 3),
]
grid = [[232400, 248400, 264400], [256900, 278700, 300500], [281400, 309000, 336600]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], -2))
checks += [("data: base", V["C18"].value, BASE_VALUE, 0), ("data: weighted", S["B32"].value, WEIGHTED, 0),
           ("data: bear", S["B29"].value, VALS[0], 0), ("data: bull", S["D29"].value, VALS[2], 0),
           ("data: need disc", V["B30"].value, NEED_D[0], 2), ("data: NC", F["D23"].value, NC_SEP27, 2),
           ("data: EPS27", F["D13"].value, EPS27, 0), ("data: EPS26", F["C13"].value, EPS26, 0), ("data: nocash", V["C25"].value, NOCASH, 0)]
for i in range(3):
    for j in range(3):
        checks.append((f"data grid {i}{j}", G.cell(row=5 + i, column=2 + j).value, VGRID[i][j], 0))

bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (isinstance(got, (int, float)) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:26s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
