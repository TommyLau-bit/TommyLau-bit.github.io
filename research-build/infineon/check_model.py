"""Recalculate the Infineon model with LibreOffice headless, cache the values in the published file, and check outputs
against the figures in data.py (which the note and src/content/calls/infineon.md print)."""
import subprocess, sys, os, shutil, openpyxl
from decimal import Decimal, ROUND_HALF_UP
from data import *


def rnd(x, dp):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


TMP = os.environ.get("RECALC_DIR", "/private/tmp/claude-501/-Users-tommylau-Desktop-journal/a038aede-c286-4285-8e30-e20d06604dcf/scratchpad/ifx_recalc")
os.makedirs(TMP, exist_ok=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", TMP, XLSX], check=True, capture_output=True)
RECALC = os.path.join(TMP, os.path.basename(XLSX))
wb = openpyxl.load_workbook(RECALC, data_only=True)
wbf = openpyxl.load_workbook(XLSX)
errs = [f"{ws.title}!{c.coordinate}={c.value}" for ws in wb.worksheets for row in ws.iter_rows() for c in row
        if isinstance(c.value, str) and c.value.startswith(("#", "Err:"))]
blank = [f"{ws.title}!{c.coordinate}" for ws in wbf.worksheets for row in ws.iter_rows() for c in row
         if isinstance(c.value, str) and c.value.startswith("=") and wb[ws.title][c.coordinate].value is None]


def find(ws, text, col=2):
    for row in ws.iter_rows(min_col=1, max_col=1):
        if isinstance(row[0].value, str) and row[0].value.strip() == text:
            return ws.cell(row=row[0].row, column=col).value
    raise KeyError(text)


Mo, S, G, V, P, C, Q = (wb[n] for n in ["Model", "Scenarios", "Sensitivity", "Valuation", "Peers", "Cover", "Quarters"])
import statistics
checks = [
    ("FY26E revenue", find(Mo, "Group revenue", 4), GROUP_REV26, 0),
    ("FY26E SR", find(Mo, "Segment Result", 4), GROUP_SR26, 0),
    ("FY26E margin", find(Mo, "Segment Result Margin", 4), GROUP_SR26 / GROUP_REV26, 3),
    ("FY26E EPS", find(Mo, "Adjusted EPS, diluted (€)", 4), EPS26, 2),
    ("FY27E revenue", find(Mo, "Group revenue", 5), B["rev"], 0),
    ("FY27E SR", find(Mo, "Segment Result", 5), B["sr"], 0),
    ("FY27E margin", find(Mo, "Segment Result Margin", 5), B["margin"], 3),
    ("FY27E EPS", find(Mo, "Adjusted EPS, diluted (€)", 5), B["eps"], 2),
    ("FY26E ATV", find(Mo, "Automotive revenue", 4), REV26["ATV"], 0),
    ("FY26E rest", find(Mo, "Everything else", 4), REST26, 0),
    ("AI share 26", find(Mo, "AI share of revenue", 4), AI_SHARE26, 3),
    ("DC share 26", find(Mo, "All data centre power (AI plus ~0.5bn classic), share", 4), DC_SHARE26, 3),
    ("AI share 27", find(Mo, "AI share of revenue", 5), AI_SHARE27, 3),
    ("AI share growth", find(Mo, "AI share of FY26E revenue growth"), AI_SHARE_GROWTH26, 3),
    ("AI share SR27", find(Mo, "AI share of FY27E Segment Result"), AI_SHARE_SR27, 3),
    ("GW", find(Mo, "FY26E AI revenue as GW of racks at full average content"), GW_FY26, 1),
    ("EPS per AI bn", find(Mo, "EPS from each €1bn of AI revenue (€)"), EPS_PER_AI_BN, 3),
    ("Value per AI bn", find(Mo, "Value per share from each €1bn of AI revenue (€)"), VAL_PER_AI_BN, 2),
    ("EPS per ATV pt", find(Mo, "EPS from one point of Automotive margin (€)"), EPS_PER_ATV_PT, 3),
    ("FY25 EPS check", find(Mo, "FY25 adjusted EPS from the same bridge (check, €)"), EPS25_CHECK, 2),
    ("PSS Q4E margin", Q["G14"].value, Q4_PSS_SR / Q4_PSS_REV, 3),
    ("ATV share", Q.cell(row=[r for r in range(1, 40) if Q.cell(row=r, column=1).value == "Automotive share of FY26E revenue"][0], column=2).value, ATV_SHARE26, 3),
    ("Base value", find(V, "Base value (€)"), BASE_VALUE, 2),
    ("Base vs price", find(V, "Base value against the price"), BASE_VALUE / PRICE - 1, 3),
    ("Band", find(V, "Band (LONG at +15% or more; SHORT at -25% or less; else NO CALL)"), "NO CALL", None),
    ("Weighted", find(V, "Weighted value, 25/50/25 (€)"), WEIGHTED, 2),
    ("Market value", find(V, "Market value (€bn)"), MCAP, 2),
    ("Net debt Sep", find(V, "Net debt, 30 September 2026, my estimate (€m)"), NET_DEBT_SEP26, 0),
    ("EV", find(V, "Enterprise value (€bn)"), EV, 2),
    ("EV/SR27", find(V, "EV / FY27E Segment Result (x)"), EV_SR27, 1),
    ("PE c26", find(V, "P/E on FY26 consensus (x)"), PE_C26, 1),
    ("PE c27", find(V, "P/E on FY27 consensus (x)"), PE_C27, 1),
    ("PE m27", find(V, "P/E on my FY27E (x)"), PE_M27, 1),
    ("PE peak", find(V, "Highest close on FY27 consensus (x)"), PE_PEAK_C27, 1),
    ("Off high", find(V, "Price against the highest close"), OFF_HIGH, 3),
    ("YTD", find(V, "Price against 30 December 2025"), RISE_DEC25, 3),
    ("Implied AI", find(V, "FY27 AI revenue implied by the price at the base P/E (€m)"), IMPLIED_AI, 0),
    ("AI for long", find(V, "Like-for-like FY27 AI revenue that lifts the base to +15% (€m)"), AI_FOR_LONG, 0),
    ("Revisit long", find(V, "Price below which the base is 15% above (€)"), REVISIT_LONG, 2),
    ("Revisit short", find(V, "Price above which the base is 25% below (€)"), REVISIT_SHORT, 2),
    ("Cons value", find(V, "Consensus FY27 EPS at the base P/E (€)"), CONS_VALUE, 2),
    ("Bear value", S["M5"].value, SC[0]["value"], 2), ("Base value scen", S["M6"].value, SC[1]["value"], 2),
    ("Bull value", S["M7"].value, SC[2]["value"], 2), ("Bear EPS", S["L5"].value, SC[0]["eps"], 2),
    ("Bull EPS", S["L7"].value, SC[2]["eps"], 2), ("Bear margin", S["J5"].value, SC[0]["margin"], 3),
    ("Bull margin", S["J7"].value, SC[2]["margin"], 3), ("Bear rev", S["H5"].value, SC[0]["rev"], 0),
    ("Bull rev", S["H7"].value, SC[2]["rev"], 0),
    ("Base check", S["E12"].value, 0, 6),
    ("Grid above", G["B9"].value, sum(x > PRICE for r in SENS for x in r), 0),
    ("Grid 15%", G["B10"].value, sum(x >= PRICE * 1.15 for r in SENS for x in r), 0),
    ("Peer median", P.cell(row=4 + len(PEERS) + 2, column=3).value, statistics.median(p[2] for p in PEERS[1:]), 2),
    ("Cover band", C["B5"].value, "NO CALL", None),
]
for i in range(3):
    for j in range(3):
        checks.append((f"Grid r{i+1}c{j+1}", G.cell(row=5 + i, column=2 + j).value, SENS[i][j], 2))
bad = 0
for name, got, want, dp in checks:
    ok = (got == want) if dp is None else (got is not None and not isinstance(got, str) and rnd(got, dp) == rnd(want, dp))
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} {name:18s} model={got!r:>24}  data={want}")
print("formula errors:", errs or "none")
print("formula cells without cached values:", blank or "none")
ok = not bad and not errs and not blank
if ok:
    shutil.copyfile(RECALC, XLSX)
    print("cached values copied back to", XLSX)
print("RESULT:", "PASS" if ok else f"{bad} mismatches")
sys.exit(0 if ok else 1)
