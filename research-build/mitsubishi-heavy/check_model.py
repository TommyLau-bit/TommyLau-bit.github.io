"""Recalculate the MHI model with LibreOffice headless, cache the values in the published file, and check
outputs against the figures printed in the note and src/content/calls/mitsubishi-heavy.md."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/mhi_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]

Sg, V, S, G, Qu, Pe, C = (wb[n] for n in ["Segments", "Valuation", "Scenarios", "Sensitivity", "Queue", "Peers", "Cover"])
# Figures as printed in the note and the md
checks = [
    ("FY26 profit check", Sg["E13"].value, 0, 6), ("FY26 revenue check", Sg["C14"].value, 0, 6),
    ("GTCC FY26 profit", Sg["E5"].value, 220, 0), ("Erest FY26 profit", Sg["E6"].value, 120, 0),
    ("GTCC FY27 rev", Sg["H5"].value, 1298, 0), ("GTCC FY27 profit", Sg["I5"].value, 286, 0),
    ("Erest FY27", Sg["I6"].value, 134, 0), ("ADS FY27", Sg["I9"].value, 198, 0), ("BP27", Sg["I11"].value, 663, 0),
    ("NI27", Sg["B16"].value, 466, 0), ("EPS27", Sg["B17"].value, 138.76, 2), ("PE27", Sg["B18"].value, 24.2, 1),
    ("ES margin 26", Sg["B19"].value, 0.155, 3), ("GT share rev", Sg["B20"].value, 0.20, 2), ("DS share rev", Sg["B21"].value, 0.23, 2),
    ("GT share BP", Sg["B22"].value, 0.41, 2), ("ADS share BP", Sg["B23"].value, 0.31, 2),
    ("SOTP GT", V["D5"].value, 5711, 0), ("SOTP ER", V["D6"].value, 1877, 0), ("SOTP ADS", V["D9"].value, 3564, 0),
    ("SOTP corp", V["D10"].value, -1080, 0), ("Net cash", V["D12"].value, 1164, 0), ("Adv build", V["D15"].value, 1049, 0),
    ("Adv deduct", V["D16"].value, -839, 0), ("Bridge", V["D17"].value, 1055, 0), ("Equity", V["D19"].value, 12478, 0),
    ("Shares", V["D20"].value, 3360.7, 1), ("Base value", V["D21"].value, 3713, 0), ("Base vs price", V["D23"].value, 0.10, 2),
    ("Band", V["D24"].value, "NO CALL", None), ("Full cash value", V["D25"].value, 3963, 0), ("Full cash chg", V["D26"].value, 0.18, 2),
    ("Mcap", V["D28"].value, 11302, 0), ("EV/BP 26", V["D30"].value, 19.0, 1), ("EV/BP 27", V["D31"].value, 15.5, 1),
    ("PE guide", V["D32"].value, 29.7, 1), ("PE cons", V["D33"].value, 25.0, 1),
    ("GT implied", V["D34"].value, 4.5, None), ("GT implied mult", V["D35"].value, 15.9, 1),
    ("ADS implied mult", V["D37"].value, 12.1, 1), ("GT mult for long", V["D38"].value, 21.8, 1),
    ("Revisit long", V["D39"].value, 3229, 0), ("Revisit short", V["D40"].value, 4951, 0),
    ("GT share eq", V["D41"].value, 0.46, 2), ("ADS share eq", V["D42"].value, 0.29, 2), ("Off record", V["D43"].value, -0.35, 2),
    ("Bear GT", S["G5"].value, 226, 0), ("Bear value", S["I5"].value, 2617, 0), ("Bear chg", S["J5"].value, -0.22, 2),
    ("Base scen", S["I6"].value, 3713, 0), ("Bull GT", S["G7"].value, 330, 0), ("Bull value", S["I7"].value, 4693, 0),
    ("Bull chg", S["J7"].value, 0.40, 2), ("Weighted", S["E11"].value, 3684, 0), ("Weighted chg", S["F11"].value, 0.10, 2),
    ("Grid above", G["B9"].value, 8, 0), ("Grid 15%", G["B10"].value, 3, 0),
    ("Units growth", Qu["B6"].value, 0.667, 3), ("BTB FY25", Qu["C12"].value, 2.67, 2), ("BTB Q1", Qu["E12"].value, 3.38, 2),
    ("Backlog years", Qu["B14"].value, 5.0, 1), ("CL rise", Qu["D15"].value, 1049, 0),
    ("Defence median EV/EBIT", Pe["D16"].value, 19.8, 1), ("Cover", C["B5"].value, "NO CALL", None),
]
grid = [[3156, 3442, 3727], [3373, 3713, 4053], [3585, 3977, 4370]]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, grid[i][j], 0))
bad = 0
for name, got, want, dp in checks:
    if name == "GT implied":
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
