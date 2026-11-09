"""Recalculate the Siemens Energy model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/siemens-energy.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/67e35963-b3b4-4df6-afdf-283132896f08/scratchpad/se_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

Sg, G, V, S, Se, Pe, C = (wb[n] for n in ["Segments", "Grid", "Valuation", "Scenarios", "Sensitivity", "Peers", "Cover"])
# Figures as printed in the note and the md
checks = [
    ("Grid rev FY26E", Sg["H6"].value / 1000, 13.8, 1), ("Grid margin FY26E", Sg["J6"].value, 0.188, 3),
    ("Gas rev FY26E", Sg["H5"].value / 1000, 13.9, 1), ("Gas margin FY26E", Sg["J5"].value, 0.162, 3),
    ("Group rev FY26E", Sg["H10"].value / 1000, 43.4, 1), ("Group PBSI FY26E", Sg["I10"].value / 1000, 5.31, 2),
    ("Grid rev FY27E", Sg["K6"].value / 1000, 16.3, 1), ("Gas rev FY27E", Sg["K5"].value / 1000, 16.3, 1),
    ("Group rev FY27E", Sg["K10"].value / 1000, 49.0, 1), ("Group PBSI FY27E", Sg["L10"].value / 1000, 6.94, 2),
    ("EPS FY27E", Sg["B23"].value, 5.92, 2),
    ("Grid 9M BTB", G["B11"].value, 1.88, 2), ("Grid 9M orders", G["B9"].value / 1000, 18.3, 1),
    ("Grid BTB FY24", G["D17"].value, 2.25, 2), ("Grid BTB FY25", G["D18"].value, 1.90, 2),
    ("Grid profit FY27E", V["B5"].value, 3.27, 2), ("Gas profit FY27E", V["B6"].value, 2.93, 2),
    ("TI profit FY27E", V["B7"].value, 0.82, 2), ("SG profit FY27E", V["B8"].value, 0.21, 2),
    ("SOTP Grid", V["D5"].value, 71.9, 1), ("SOTP Gas", V["D6"].value, 52.8, 1), ("SOTP TI", V["D7"].value, 11.5, 1),
    ("SOTP SG", V["D8"].value, 0.6, 1), ("SOTP corp", V["D9"].value, -4.5, 1),
    ("Bridge", V["D18"].value, 3.8, 1), ("Equity", V["D19"].value, 136.1, 1), ("Shares", V["D20"].value, 836.4, 1),
    ("Base value", V["D21"].value, 163, 0), ("Base vs price", V["D23"].value, 0.27, 2), ("Band", V["D24"].value, "LONG", None),
    ("Mcap", V["D26"].value, 107.5, 1), ("EV adj", V["D27"].value, 103.7, 1),
    ("EV/PBSI 26", V["D28"].value, 19.5, 1), ("EV/PBSI 27", V["D29"].value, 15.0, 1), ("PE cons 27", V["D30"].value, 20.6, 1),
    ("Implied Grid EV", V["D32"].value, 43, 0), ("Implied Grid x", V["D33"].value, 13.3, 1), ("Implied Gas x", V["D34"].value, 8.3, 1),
    ("No call above", V["D35"].value, 141.5, 1), ("Grid share", V["D37"].value, 0.53, 2), ("Gas share", V["D38"].value, 0.39, 2),
    ("Off record", V["D39"].value, -0.31, 2),
    ("Bear value", S["M5"].value, 98, 0), ("Bear chg", S["N5"].value, -0.23, 2), ("Bear Grid profit", S["L5"].value, 2.87, 2),
    ("Base scen", S["M6"].value, 163, 0), ("Bull value", S["M7"].value, 218, 0), ("Bull chg", S["N7"].value, 0.69, 2),
    ("Bull Grid profit", S["L7"].value, 3.55, 2), ("Weighted", S["E11"].value, 160, 0), ("Weighted chg, rounded value", round(S["E11"].value) / PRICE - 1, 0.24, 2),
    ("Grid above", Se["B9"].value, 8, 0), ("Grid 15%", Se["B10"].value, 6, 0),
    ("Peer grid median EV/EBIT", Pe["D16"].value, 20.8, 1), ("Peer grid median ex Hitachi", Pe["D17"].value, 22.4, 1),
    ("Peer grid median fwd PE", Pe["C16"].value, 22.2, 1), ("Cover", C["B5"].value, "LONG", None),
]
grid = [[122, 145, 169], [139, 163, 186], [157, 180, 204]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", Se.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and rnd(got, dp) == rnd(want, dp))
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
