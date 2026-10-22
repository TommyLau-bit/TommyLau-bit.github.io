"""Recalculate the Hitachi model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/hitachi.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/b9b0dbaf-088e-4507-84d5-644e8abd4f9c/scratchpad/hit_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

H, Sg, V, S, G, Qu, Pe, C = (wb[n] for n in ["HitachiEnergy", "Segments", "Valuation", "Scenarios", "Sensitivity", "Queue", "Peers", "Cover"])
checks = [
    ("HE growth FY25", H["C6"].value, 0.26, 2), ("HE growth FY26", H["D6"].value, 0.19, 2),
    ("HE rev FY27E", H["E5"].value, 26.5, 1), ("HE EBITA FY27E US$", H["E8"].value, 4.11, 2),
    ("HE EBITA FY26 yen", H["D10"].value, 560, 0), ("HE EBITA FY27E yen", H["E10"].value, 657, 0),
    ("HE rev FY26 yen", H["D11"].value, 3784, 0),
    ("HE share rev", H["B14"].value, 0.32, 2), ("HE share EBITA", H["B15"].value, 0.37, 2),
    ("Group EBITA FY26 check", Sg["E14"].value, 0, 6), ("Group rev FY26 check", Sg["C14"].value, 0, 6),
    ("Energy rest FY26", Sg["E6"].value, 16, 0), ("DSS FY27E", Sg["G7"].value, 538, 0), ("CI FY27E", Sg["G8"].value, 404, 0),
    ("Mobility FY27E", Sg["G9"].value, 150, 0), ("Group FY27E", Sg["G12"].value, 1680, 0),
    ("SOTP HE", V["D5"].value, 13138, 0), ("SOTP DSS", V["D7"].value, 8077, 0), ("SOTP CI", V["D8"].value, 6064, 0),
    ("SOTP Mob", V["D9"].value, 1496, 0), ("SOTP corp", V["D11"].value, -1500, 0),
    ("Bridge", V["D18"].value, 1154, 0), ("Equity", V["D19"].value, 28757, 0), ("Shares", V["D20"].value, 4471.0, 1),
    ("Base value", V["D21"].value, 6432, 0), ("Base vs price", V["D23"].value, 0.10, 2), ("Band", V["D24"].value, "NO CALL", None),
    ("HE share equity", V["E5"].value, 0.46, 2), ("DSS share", V["E7"].value, 0.28, 2), ("CI share", V["E8"].value, 0.21, 2),
    ("Mcap", V["D26"].value, 26111, 0), ("EV adj", V["D27"].value, 24957, 0),
    ("EV/EBITA 26", V["D28"].value, 16.4, 1), ("EV/EBITA 27", V["D29"].value, 14.9, 1),
    ("PE guide", V["D30"].value, 29.0, 1), ("PE cons", V["D31"].value, 27.0, 1),
    ("Implied HE", V["D32"].value, 10.5, None), ("Implied HE mult", V["D33"].value, 16.0, 1), ("Implied HE US$", V["D34"].value, 66, 0),
    ("HE mult for long", V["D35"].value, 22, 0), ("Revisit long", V["D36"].value, 5593, 0), ("Revisit short", V["D37"].value, 8576, 0),
    ("HE share mkt", V["D41"].value, 0.40, 2), ("Off intraday high", V["D42"].value, -0.033, 3),
    ("Bear HE EBITA", S["G5"].value, 605, 0), ("Bear value", S["I5"].value, 4929, 0), ("Bear chg", S["J5"].value, -0.16, 2),
    ("Base scen", S["I6"].value, 6432, 0), ("Bull HE EBITA", S["G7"].value, 718, 0), ("Bull value", S["I7"].value, 7966, 0),
    ("Bull chg", S["J7"].value, 0.36, 2), ("Weighted", S["E11"].value, 6440, -1), ("Weighted chg", S["F11"].value, 0.10, 2),
    ("Grid above", G["B9"].value, 8, 0), ("Grid 15%", G["B10"].value, 2, 0),
    ("Ratio Mar25", Qu["B7"].value, 2.78, 2), ("Ratio Mar26", Qu["F7"].value, 2.92, 2), ("Ratio Jun26", Qu["G7"].value, 3.06, 2),
    ("TTM Jun26", Qu["G6"].value, 20.8, 1), ("Backlog growth", Qu["B8"].value, 0.46, 2), ("FY30 ratio", Qu["B11"].value, 2.78, 2),
    ("BTB FY25", Qu["D16"].value, 1.66, 2), ("BTB Q1 PG", Qu["D17"].value, 2.16, 2),
    ("Grid median EV/EBIT", Pe["D16"].value, 24.5, 1), ("Cover", C["B5"].value, "NO CALL", None),
]
grid = [[5641, 6177, 6714], [5844, 6432, 7020], [6070, 6714, 7358]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))
bad = 0
for name, got, want, dp in checks:
    if name == "Implied HE":
        ok = got is not None and round(got / 1000, 1) == want
    else:
        ok = (got == want) if dp is None else (got is not None and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:24s} model={got!r:>24}  note={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
