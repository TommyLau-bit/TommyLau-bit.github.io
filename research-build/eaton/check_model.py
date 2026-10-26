"""Recalculate the Eaton model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/eaton.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/e9b3b7d1-27b5-4c6a-9bad-010660d3ef59/scratchpad/etn_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

Sg, E, V, S, G, Qu, Pe, C = (wb[n] for n in ["Segments", "EPS", "Valuation", "Scenarios", "Sensitivity", "Queue", "Peers", "Cover"])
checks = [
    # Segments, as printed in the note's key financials table
    ("EA sales 2026E", Sg["D5"].value, 15641, 0), ("EA margin 2026E", Sg["D7"].value, 0.286, 3),
    ("EA growth 2026E", Sg["D6"].value, 0.178, 3), ("EA growth 2025A", Sg["C6"].value, 0.161, 3),
    ("EA margin 2024A", Sg["B7"].value, 0.302, 3), ("EA margin 2025A", Sg["C7"].value, 0.299, 3),
    ("EA sales 2027E", Sg["E5"].value, 18144, 0), ("EA sales 2028E", Sg["F5"].value, 20502, 0),
    ("EA OP 2027E", Sg["E8"].value, 5443, 0), ("EA OP 2028E", Sg["F8"].value, 6253, 0),
    ("Total sales 2026E", Sg["D25"].value, 32998, 0), ("Segment margin 2026E", Sg["D27"].value, 0.242, 3),
    ("Total sales 2027E", Sg["E25"].value, 34076, 0), ("Total sales 2028E", Sg["F25"].value, 37922, 0),
    ("Segment OP 2027E", Sg["E26"].value, 9000, 0), ("Segment OP 2028E", Sg["F26"].value, 10198, 0),
    ("Segment margin 2028E", Sg["F27"].value, 0.269, 3),
    # EPS
    ("EPS 2026E", E["D14"].value, 13.49, 2), ("EPS 2027E", E["E14"].value, 16.14, 2), ("EPS 2028E", E["F14"].value, 18.85, 2),
    ("EPS growth 2027E", E["E15"].value, 0.197, 3), ("EPS growth 2028E", E["F15"].value, 0.168, 3),
    ("2027E vs consensus", E["E17"].value, -0.010, 3), ("Shares 2027E", E["E13"].value, 379.5, 1),
    # Valuation
    ("Base value", V["B7"].value, 433.57, 2), ("Base vs price", V["B9"].value, 0.184, 3), ("Band", V["B10"].value, "LONG", None),
    ("Target vs price", V["B12"].value, 0.175, 3),
    ("Market value", V["B14"].value, 142.2, 1), ("Net debt", V["B15"].value, 19916, 0), ("EV", V["B16"].value, 162.2, 1),
    ("PE guide 26", V["B17"].value, 27.1, 1), ("PE cons 27", V["B19"].value, 22.5, 1), ("PE 2027E", V["B20"].value, 22.7, 1),
    ("PE 2028E", V["B21"].value, 19.4, 1), ("PE peak", V["B22"].value, 34.1, 1), ("PE for long", V["B23"].value, 22.3, 1),
    ("Long below", V["B24"].value, 377, 0), ("Short above", V["B25"].value, 578, 0),
    ("Off high", V["B26"].value, -0.204, 3), ("YTD", V["B27"].value, 0.149, 3), ("Cons TP vs price", V["B28"].value, 0.326, 3),
    # Scenarios
    ("Bear EPS", S["L5"].value, 15.01, 2), ("Bear value", S["M5"].value, 270, 0), ("Bear chg", S["N5"].value, -0.262, 3),
    ("Base value scen", S["M6"].value, 434, 0), ("Bull EPS", S["L7"].value, 20.52, 2), ("Bull value", S["M7"].value, 534, 0),
    ("Bull chg", S["N7"].value, 0.457, 3), ("Weighted", S["E11"].value, 418, 0), ("Weighted chg", S["F11"].value, 0.141, 3),
    ("Base check", S["E12"].value, 0, 6),
    ("Grid above", G["B9"].value, 8, 0), ("Grid 15%", G["B10"].value, 5, 0),
    # Queue
    ("Ratio Jun26", Qu["K10"].value, 1.049, 3), ("Ratio Jun25", Qu["G10"].value, 0.930, 3), ("Ratio Mar26", Qu["J10"].value, 1.043, 3),
    ("Ratio Mar25", Qu["F10"].value, 0.855, 3), ("Months Jun26", Qu["K11"].value, 12.6, 1), ("Months Jun25", Qu["G11"].value, 11.2, 1),
    ("TTM growth", Qu["B13"].value, 0.183, 3), ("Backlog growth", Qu["B14"].value, 0.334, 3), ("Sep needed", Qu["B17"].value, 15783, 0),
    ("EA margin Q2 26", Qu["K7"].value, 0.275, 3), ("EA margin Q1 26", Qu["J7"].value, 0.256, 3),
    ("Peer median fwd", Pe["C14"].value, 20.5, 1), ("Peer median EV/EBIT", Pe["D14"].value, 22.9, 1), ("Hist fwd PE", Pe["C15"].value, 24.0, 1),
    ("Cover band", C["B5"].value, "LONG", None),
]
grid = [[340, 391, 442], [377, 434, 490], [410, 472, 533]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and not isinstance(got, str) and rnd(got, dp) == rnd(want, dp))
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
