"""Kinder Morgan, Inc. (NYSE: KMI) initiation model. Adjusted EBITDA build to 2029E, net debt, EV/EBITDA valuation.
Live formulas throughout. House style follows the Vertiv and Eaton models: navy header rows, blue font for hardcoded
inputs, yellow fill on my own assumptions, green font for cross-sheet links, black for formulas.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from data import *

NAVY = "1F3864"; MUTED = "595959"
F_TTL = Font(bold=True, color=NAVY, size=12)
F_SUB = Font(color=MUTED, size=9)
F_HDR = Font(bold=True, color="FFFFFF", size=10)
F_IN = Font(color="0000FF")
F_INB = Font(color="0000FF", bold=True)
F_LINK = Font(color="008000")
F_B = Font(bold=True)
F_NOTE = Font(color=MUTED, size=9, italic=True)
FILL_HDR = PatternFill("solid", fgColor=NAVY)
FILL_ASSUME = PatternFill("solid", fgColor="FFFF00")
FILL_KEY = PatternFill("solid", fgColor="D9E2F3")
WRAP = Alignment(wrap_text=True, vertical="top")
RIGHT = Alignment(horizontal="right")

USD2 = '"US$"#,##0.00'
M0 = '#,##0'
M1 = '#,##0.0'
PCT1 = '0.0%'
PCT0 = '0%'
MULTF = '0.0"x"'
SUB = f"Tommy Lau | Kinder Morgan, Inc. (NYSE: KMI) | {DATE} | Personal research, not investment advice."

wb = openpyxl.Workbook()


def sheet(name, title, widths):
    ws = wb.active if wb.active.title == "Sheet" else wb.create_sheet(name)
    ws.title = name
    ws["A1"] = title; ws["A1"].font = F_TTL
    ws["A2"] = SUB; ws["A2"].font = F_SUB
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.sheet_view.showGridLines = False
    return ws


def head(ws, row, cells, start=1):
    for i, c in enumerate(cells, start):
        x = ws.cell(row=row, column=i, value=c)
        x.font = F_HDR; x.fill = FILL_HDR
        x.alignment = Alignment(horizontal="left" if i == start else "right", vertical="center", wrap_text=True)


def note(ws, row, texts):
    for i, t in enumerate(texts):
        ws.cell(row=row + i, column=1, value=t).font = F_NOTE


def put(ws, ref, v, fmt=None, font=None, fill=None):
    c = ws[ref]; c.value = v
    if fmt: c.number_format = fmt
    if font: c.font = font
    elif isinstance(v, str) and v.startswith(("=Assumptions", "=EBITDA", "=Valuation")): c.font = F_LINK
    if fill: c.fill = fill
    c.alignment = RIGHT
    return c


# =====================================================================  COVER (filled last)
ws = sheet("Cover", "KINDER MORGAN, INC. (NYSE: KMI)  INITIATION MODEL", [42, 24, 100])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [62, 14, 10, 110])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. US$ million unless stated. Year end 31 December.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = set()
Q3R = "Q3 2026 results release, Form 8-K Ex. 99.1, 21 October 2026"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "US$", "NYSE close, 30 October 2026. Nasdaq historical quotes, retrieved 2 November 2026."),
    ("hiclose", "Highest close since December 2023, 23 October 2026", HI_CLOSE, "US$", "Nasdaq. Intraday high US$34.805 on 19 May 2026."),
    ("pxdec25", "Close, 31 December 2025", PX_DEC25, "US$", "Nasdaq."),
    ("pxjan24", "Close, 31 January 2024", PX_JAN24, "US$", "Nasdaq."),
    ("shares", "Class P shares outstanding, 22 October 2026", SHARES, "m", "Form 10-Q cover, quarter to 30 September 2026: 2,227,715,229."),
    ("netdebt", "Net Debt, 30 September 2026", NET_DEBT, "US$m", Q3R + ", Table 5 (debt less cash, fair value adjustments and FX on euro bonds)."),
    ("nci", "Noncontrolling interests, 30 September 2026", NCI, "US$m", Q3R + ", Table 5."),
    ("ltm", "Adjusted EBITDA, twelve months to 30 September 2026", LTM_EBITDA, "US$m", Q3R + ", Table 5."),
    ("HISTORY (KINDER MORGAN RELEASES)", None, None, None, None),
    ("e23", "Adjusted EBITDA, 2023", EBITDA_H[0], "US$m", "Q4 2023 release, 17 January 2024."),
    ("e24", "Adjusted EBITDA, 2024", EBITDA_H[1], "US$m", "Q4 2024 release, 22 January 2025."),
    ("e25", "Adjusted EBITDA, 2025", EBITDA_H[2], "US$m", "Q4 2025 release, 21 January 2026."),
    ("nd23", "Net Debt, 31 December 2023", NETDEBT_H[0], "US$m", "Q4 2024 release."),
    ("nd24", "Net Debt, 31 December 2024", NETDEBT_H[1], "US$m", "Q4 2025 release."),
    ("nd25", "Net Debt, 31 December 2025", NETDEBT_H[2], "US$m", "Q4 2025 release."),
    ("nci23", "Noncontrolling interests, 31 December 2023", NCI_H[0], "US$m", "Q4 2023 release."),
    ("nci24", "Noncontrolling interests, 31 December 2024", NCI_H[1], "US$m", "Q4 2024 release."),
    ("nci25", "Noncontrolling interests, 31 December 2025", NCI_H[2], "US$m", "Q4 2025 release."),
    ("sh23", "Weighted average shares, Q4 2023", SHARES_H[0], "m", "Q4 2023 release."),
    ("sh24", "Weighted average shares, Q4 2024", SHARES_H[1], "m", "Q4 2024 release."),
    ("sh25", "Weighted average shares, Q4 2025", SHARES_H[2], "m", "Q4 2025 release."),
    ("px23", "Close, 29 December 2023", PX_DEC23, "US$", "Nasdaq."),
    ("px24", "Close, 31 December 2024", PX_DEC24, "US$", "Nasdaq."),
    ("dps23", "Dividend declared, 2023", DPS_H[0], "US$", "Q4 2023 release."),
    ("BUDGET, OUTLOOK AND BACKLOG", None, None, None, None),
    ("budget", "2026 budgeted Adjusted EBITDA", BUDGET26_EBITDA, "US$m", Q3R + "."),
    ("beat", "Expected beat on the 2026 EBITDA budget (at least)", OUT26_EBITDA_PCT, "%", Q3R + ": 'more than 6% favorable to budget'."),
    ("eps_b", "2026 budgeted Adjusted EPS", BUDGET26_EPS, "US$", Q3R + ". Expected more than 13% favourable."),
    ("dps26", "2026 dividend declared", DPS26, "US$", Q3R + ": US$1.19 annualised."),
    ("lev26", "Expected year-end 2026 Net Debt / Adjusted EBITDA", LEV26_OUT, "x", Q3R + "."),
    ("nonrec", "2026 items that may not recur", NONREC26, "US$m", "Q3 2026 call, 21 October 2026, CFO: 'approximately $225 million'; transcript published by Earnings Whispers (third-party)."),
    ("bl_top", "Take-or-pay backlog used for the Project EBITDA multiple", BACKLOG_TOP * 1000, "US$m", Q3R + ": 'The larger $13.7 billion portion of the backlog'."),
    ("bl_mult", "First-full-year Project EBITDA multiple", BACKLOG_MULT, "x", Q3R + ": 'approximately 5.7 times'."),
    ("bl_all", "Total project backlog, 30 September 2026", 14400.0, "US$m", Q3R + "."),
    ("cons26", "2026 consensus Adjusted EPS", CONS_EPS26, "US$", "stockanalysis.com (S&P Global), updated 28 October 2026. Cross-check only."),
    ("cons27", "2027 consensus Adjusted EPS", CONS_EPS27, "US$", "stockanalysis.com, as above."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com: 24 analysts, low US$32, high US$43. Cross-check only."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("e26", "Adjusted EBITDA, 2026E", EBITDA26, "US$m", "MY ESTIMATE. Just above the US$9,116m that a 6% beat on budget implies; nine months US$6,918m."),
    ("g", "Underlying growth of the existing business, a year", BASE_G, "%", "MY ASSUMPTION. Tariff escalators, high use of the system, 2026 projects running a full year."),
    ("bl27", "Project EBITDA from the backlog, 2027", BL27, "US$m", "MY ASSUMPTION. Trident first phase from Q1 2027; Creekside, Pelican, terminals. See Backlog tab."),
    ("bl28", "Project EBITDA from the backlog, 2028", BL28, "US$m", "MY ASSUMPTION. Adds Mississippi Crossing from Q2 2028 and late-2028 openings."),
    ("bl29", "Project EBITDA from the backlog, 2029", BL29, "US$m", "MY ASSUMPTION. SSE4 and FGT phases; Bear Creek."),
    ("cfo27", "Operating cash flow, 2027", CFO27, "US$m", "MY ESTIMATE. 2025 US$5,917m; nine months 2026 US$5,041m."),
    ("capex27", "Capital spending and JV contributions, 2027", CAPEX27, "US$m", "MY ESTIMATE. 2026 growth spending US$4.2bn (10-Q) plus sustaining."),
    ("dps27", "Dividend, 2027", DPS27, "US$", "MY ASSUMPTION. About 2% growth, as each year since 2024."),
    ("mult", "Base multiple, EV / 2028E Adjusted EBITDA", BASE_MULT, "x", "MY ASSUMPTION. Kinder Morgan's own range since the 2024 re-rating, 11.2x to 11.9x."),
]
MINE |= {"e26", "g", "bl27", "bl28", "bl29", "cfo27", "capex27", "dps27", "mult"}
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY)
        r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULTF if unit == "x" else (M1 if unit == "m" else (USD2 if unit == "US$" else M0)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  EBITDA AND NET DEBT
ws = sheet("EBITDA", "ADJUSTED EBITDA AND NET DEBT, 2023A TO 2029E (US$ MILLION)", [52, 13, 13, 13, 13, 13, 13, 13])
head(ws, 4, ["US$ million", "2023A", "2024A", "2025A", "2026E*", "2027E*", "2028E*", "2029E*"])
labs = {5: "Existing business (underlying)", 6: "Items that may not recur", 7: "Project EBITDA from the backlog",
        8: "ADJUSTED EBITDA", 9: "Growth", 11: "Net debt, year end", 12: "Net debt / Adjusted EBITDA",
        13: "Operating cash flow", 14: "Capital spending and JV contributions", 15: "Dividends", 16: "Shares, m"}
for rr, t in labs.items():
    ws.cell(row=rr, column=1, value=t).font = F_B if t.isupper() or rr in (11,) else Font()
for col, k in zip("BCD", ["e23", "e24", "e25"]):
    put(ws, f"{col}8", L(k), M0)
put(ws, "E5", f"={A['e26']}-{A['nonrec']}", M0); put(ws, "E6", L("nonrec"), M0); put(ws, "E7", 0, M0, F_IN)
put(ws, "E8", "=SUM(E5:E7)", M0)
for col, prev, bl in [("F", "E", "bl27"), ("G", "F", "bl28"), ("H", "G", "bl29")]:
    put(ws, f"{col}5", f"={prev}5*(1+{A['g']})", M0); put(ws, f"{col}6", 0, M0, F_IN)
    put(ws, f"{col}7", L(bl), M0); put(ws, f"{col}8", f"=SUM({col}5:{col}7)", M0)
for col, prev in [("C", "B"), ("D", "C"), ("E", "D"), ("F", "E"), ("G", "F"), ("H", "G")]:
    put(ws, f"{col}9", f"={col}8/{prev}8-1", PCT1)
for c in "BCDEFGH":
    ws[f"{c}8"].font = F_B; ws[f"{c}8"].fill = FILL_KEY
for col, k in zip("BCD", ["nd23", "nd24", "nd25"]):
    put(ws, f"{col}11", L(k), M0)
put(ws, "E11", f"={A['lev26']}*E8", M0)
put(ws, "F13", L("cfo27"), M0); put(ws, "F14", L("capex27"), M0); put(ws, "F15", f"={A['dps27']}*{A['shares']}", M0)
put(ws, "F16", L("shares"), M1)
put(ws, "F11", "=E11+F14+F15-F13", M0)
for col in "BCDEF":
    put(ws, f"{col}12", f"={col}11/{col}8", '0.00"x"')
note(ws, 18, [
    "*My estimates. 2026E is my reading of Kinder Morgan's 'more than 6% favorable' to its US$8.6bn budget; the US$225m that may not recur",
    "(Q3 call transcript, Earnings Whispers) is removed from 2027 on. Year-end 2026 net debt uses Kinder Morgan's own 3.6x expectation (21 October 2026).",
    "2023A to 2025A as reported. Backlog EBITDA follows the in-service dates on the Backlog tab and the 5.7x first-full-year build multiple.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: EV / 2028E ADJUSTED EBITDA, TWELVE MONTHS OUT", [64, 16, 70])
head(ws, 4, ["Item", "Value", "Working / note"])
vrows = [
    (5, "2028E Adjusted EBITDA, US$m", "=EBITDA!G8", M0, "My estimate."),
    (6, "Base multiple", L("mult"), MULTF, "Kinder Morgan's own range since the 2024 re-rating."),
    (7, "Enterprise value at the base multiple, US$m", "=B5*B6", M0, ""),
    (8, "Less net debt, end 2027E, US$m", "=EBITDA!F11", M0, "My estimate."),
    (9, "Less noncontrolling interests, US$m", L("nci"), M0, "30 September 2026, held flat."),
    (10, "Shares, m", L("shares"), M1, "22 October 2026; no buybacks assumed."),
    (11, "BASE VALUE PER SHARE, US$", "=(B7-B8-B9)/B10", USD2, ""),
    (12, "Reference price, US$", L("price"), USD2, "NYSE close, 30 October 2026."),
    (13, "Base value against price", "=B11/B12-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (14, "VIEW ON THE BAND", '=IF(B13>=0.15,"LONG",IF(B13<=-0.25,"SHORT","NO CALL"))', None, "Tommy Lau's call, 2 November 2026: NO CALL, medium conviction."),
    (16, "Market value, US$bn", f"={A['shares']}*B12/1000", '#,##0.00', ""),
    (17, "Enterprise value, US$bn", f"=B16+({A['netdebt']}+{A['nci']})/1000", '#,##0.00', "Net debt and NCI at 30 September 2026."),
    (18, "EV / trailing Adjusted EBITDA", f"=B17*1000/{A['ltm']}", MULTF, ""),
    (19, "EV / 2026E", "=B17*1000/EBITDA!E8", MULTF, ""),
    (20, "EV / 2027E", "=B17*1000/EBITDA!F8", MULTF, ""),
    (21, "EV / 2028E: what the price pays", "=B17*1000/EBITDA!G8", MULTF, ""),
    (22, "EV / EBITDA at end 2023", f"=({A['px23']}*{A['sh23']}+{A['nd23']}+{A['nci23']})/{A['e23']}", '0.00"x"', "Year-end price, Q4 weighted shares, year-end net debt and NCI."),
    (23, "EV / EBITDA at end 2024", f"=({A['px24']}*{A['sh24']}+{A['nd24']}+{A['nci24']})/{A['e24']}", '0.00"x"', ""),
    (24, "EV / EBITDA at end 2025", f"=({A['pxdec25']}*{A['sh25']}+{A['nd25']}+{A['nci25']})/{A['e25']}", '0.00"x"', ""),
    (25, "Backlog EBITDA when complete, US$m", f"={A['bl_top']}/{A['bl_mult']}", M0, "Take-or-pay portion over the build multiple. My arithmetic."),
    (26, "EBITDA today's EV needs at the end-2023 multiple, US$m", "=B17*1000/B22", M0, ""),
    (27, "Share of the backlog's EBITDA that implies, beyond underlying 2026", "=(B26-EBITDA!E5)/B25", PCT0, ""),
    (28, "Dividend yield, 2026", f"={A['dps26']}/B12", PCT1, ""),
    (29, "Dividend yield at end 2023", f"={A['dps23']}/{A['px23']}", PCT1, ""),
    (30, "2027 dividend at today's yield, US$", f"={A['dps27']}/B28", USD2, "Cross-check."),
    (31, "Multiple of 2028E needed for a value 15% above the price", "=(B12*1.15*B10+B8+B9)/B5", MULTF, ""),
    (32, "Price below which the base value is 15% or more above it, US$", "=B11/1.15", USD2, ""),
    (33, "Price above which the base value is 25% or more below it, US$", "=B11/0.75", USD2, ""),
    (34, "Price change since January 2024", f"=B12/{A['pxjan24']}-1", PCT1, ""),
    (35, "Price change in 2026 to date", f"=B12/{A['pxdec25']}-1", PCT1, ""),
    (36, "Average analyst target against price", f"={A['constp']}/B12-1", PCT1, "Cross-check only."),
]
for rr, lab, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    if rr in (11, 14):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    elif isinstance(f, str) and f.startswith(("=Assumptions", "=EBITDA")): c.font = F_LINK
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (VALUE = MULTIPLE x 2028E EBITDA, LESS NET DEBT AND NCI)", [10, 14, 16, 12, 16, 14, 12])
head(ws, 4, ["Case", "Underlying growth", "Backlog EBITDA 2028", "Multiple", "2028E EBITDA", "Value, US$", "vs price"])
r = 5
for s in SC:
    ws.cell(row=r, column=1, value=s["name"]).font = F_B
    if s["name"] == "Base":
        for j, k in enumerate(["g", "bl28", "mult"]):
            c = ws.cell(row=r, column=2 + j, value="=" + A[k]); c.font = F_LINK
    else:
        for j, v in enumerate([s["g"], s["bl"], s["mult"]]):
            c = ws.cell(row=r, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME
    ws.cell(row=r, column=2).number_format = PCT1; ws.cell(row=r, column=3).number_format = M0
    ws.cell(row=r, column=4).number_format = MULTF
    ws.cell(row=r, column=5, value=f"=EBITDA!$E$5*(1+B{r})^2+C{r}").number_format = M0
    ws.cell(row=r, column=6, value=f"=(D{r}*E{r}-Valuation!$B$8-Valuation!$B$9)/Valuation!$B$10").number_format = USD2
    ws.cell(row=r, column=7, value=f"=F{r}/{A['price']}-1").number_format = PCT1
    r += 1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SC):
    ws.cell(row=8, column=2 + j, value=s["name"]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s["prob"]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, US$"; ws["A11"].font = F_B
ws["E11"] = "=B9*F5+C9*F6+D9*F7"; ws["E11"].number_format = USD2; ws["E11"].font = F_B; ws["E11"].fill = FILL_KEY
ws["F11"] = f"=E11/{A['price']}-1"; ws["F11"].number_format = PCT1
ws["A12"] = "Check: base case equals the Valuation tab"; ws["E12"] = "=F6-Valuation!B11"; ws["E12"].number_format = '0.000'
note(ws, 14, [
    "All cases start from my underlying 2026 EBITDA (2026E less the items that may not recur) and use the same end-2027 net debt and NCI.",
    "Bear: no underlying growth; projects slip about a year; rates or sentiment take the multiple back towards the 9.6x of end 2023; 10x.",
    "Bull: growth of 1.5%; more projects sanctioned and opened early; the multiple closes part of the gap to Williams and TC Energy; 13x.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: 2028E ADJUSTED EBITDA AGAINST THE MULTIPLE (US$)", [30, 14, 14, 14])
head(ws, 4, ["2028E EBITDA \\ EV/EBITDA", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_M, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["mult"]) if link else m)
    c.number_format = MULTF; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, ref in enumerate(["=Scenarios!E5", "=EBITDA!G8", "=Scenarios!E7"]):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=ref); c.number_format = M0; c.font = F_LINK
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=f"=($A{rr}*{col}$4-Valuation!$B$8-Valuation!$B$9)/Valuation!$B$10").number_format = USD2
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["Rows link to the bear, base and bull 2028E EBITDA; the middle column to the base multiple."])

# =====================================================================  BACKLOG
ws = sheet("Backlog", "THE BACKLOG: BY QUARTER, AND WHEN THE NAMED PROJECTS OPEN", [46, 16, 14, 60])
head(ws, 4, ["Quarter end", "Backlog, US$bn", "", ""])
for i, (lab, v) in enumerate(zip(BL_LABELS, BACKLOG)):
    ws.cell(row=5 + i, column=1, value=lab)
    c = ws.cell(row=5 + i, column=2, value=v); c.font = F_IN; c.number_format = M1
r0 = 5 + len(BL_LABELS) + 1
head(ws, r0, ["Named project", "KMI-share capital, US$m", "First in service", "What it serves"])
for i, (nm, cap, yr, what) in enumerate(PROJECTS):
    rr = r0 + 1 + i
    ws.cell(row=rr, column=1, value=nm)
    c = ws.cell(row=rr, column=2, value=cap); c.font = F_IN; c.number_format = M0
    c = ws.cell(row=rr, column=3, value=yr); c.font = F_IN
    ws.cell(row=rr, column=4, value=what)
pe = r0 + len(PROJECTS)
rs = pe + 2
head(ws, rs, ["First in-service year", "KMI-share capital, US$m", "Share of backlog", ""])
for i, y in enumerate(LAND_YEARS):
    rr = rs + 1 + i
    ws.cell(row=rr, column=1, value=y)
    ws.cell(row=rr, column=2, value=f"=SUMIF($C${r0 + 1}:$C${pe},A{rr},$B${r0 + 1}:$B${pe})").number_format = M0
    ws.cell(row=rr, column=3, value=f"=B{rr}/{A['bl_all']}").number_format = PCT0
rt = rs + 1 + len(LAND_YEARS)
ws.cell(row=rt, column=1, value="Named total").font = F_B
ws.cell(row=rt, column=2, value=f"=SUM(B{rs + 1}:B{rt - 1})").number_format = M0
ws.cell(row=rt + 1, column=1, value="Permian Link and Southeast Connector, KMI share").font = F_B
ws.cell(row=rt + 1, column=2, value=f"=B{r0 + 15}+B{r0 + 16}").number_format = M0
ws.cell(row=rt + 2, column=1, value="Their EBITDA at the 5.7x build multiple").font = F_B
ws.cell(row=rt + 2, column=2, value=f"=B{rt + 1}/{A['bl_mult']}").number_format = M0
ws.cell(row=rt + 3, column=1, value="As a share of 2026E EBITDA").font = F_B
ws.cell(row=rt + 3, column=2, value=f"=B{rt + 2}/{A['e26']}").number_format = PCT0
BK = dict(total=rt, ai=rt + 1, ai_e=rt + 2, ai_s=rt + 3, y2030=rs + 5, y2028=rs + 3, y2027=rs + 2)
note(ws, rt + 5, [
    "Backlog: quarterly results releases, Form 8-K Ex. 99.1; December 2023 from the release of 17 April 2024 ('up from $3 billion at year-end 2023').",
    "Projects: 2025 Form 10-K major projects table (KMI-share capital and dates) and the 2026 releases for Creekside, Amarillo, Bear Creek, Permian Link,",
    "the Southeast Connector and the Houston terminal projects. A two-phase project sits in its first year. Grouping is my arithmetic.",
    "Remaining performance obligations, 30 September 2026 (10-Q): US$1bn rest of 2026, US$5bn 2027, US$31bn 2028 and after; US$5bn / 5bn / 26bn at December 2025.",
])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, RETRIEVED 2 NOVEMBER 2026)", [22, 14, 13, 14, 70])
head(ws, 4, ["Company", "Ticker", "EV/EBITDA (trailing)", "Dividend yield", "What they run"])
for i, (co, tk, e, y, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    c = ws.cell(row=rr, column=3, value=e); c.number_format = MULTF; c.font = F_IN
    c = ws.cell(row=rr, column=4, value=y); c.number_format = PCT1; c.font = F_IN
    ws.cell(row=rr, column=5, value=what).alignment = WRAP
last = 4 + len(PEERS)
ws[f"A{last + 2}"] = "Peer median (excluding Kinder Morgan)"; ws[f"A{last + 2}"].font = F_B
ws[f"C{last + 2}"] = f"=MEDIAN(C6:C{last})"; ws[f"C{last + 2}"].number_format = MULTF
ws[f"D{last + 2}"] = f"=MEDIAN(D6:D{last})"; ws[f"D{last + 2}"].number_format = PCT1
note(ws, last + 4, ["stockanalysis.com's EBITDA is not Kinder Morgan's Adjusted EBITDA (14.1x here against 11.9x on its own measure), so compare",
                    "the peers on this basis only. Multiples set the range only; no view on the peers' shares is expressed."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 150])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Kinder Morgan Q3 2026 results release, Form 8-K Ex. 99.1, 21 October 2026: results, LTM Adjusted EBITDA, Net Debt, backlog and its multiple, Permian Link, Southeast Connector, Creekside, Bear Creek, 2026 outlook.",
    "Kinder Morgan Form 10-Q, quarter to 30 September 2026, filed 23 October 2026: shares outstanding, 2026 growth spending of US$4.2bn, remaining performance obligations.",
    "Kinder Morgan 2025 Form 10-K, filed 13 February 2026: major projects table with KMI-share capital and in-service dates; remaining performance obligations at December 2025.",
    "Kinder Morgan quarterly results releases, Form 8-K Ex. 99.1, 17 January 2024 to 22 July 2026: Adjusted EBITDA, Adjusted EPS, backlog, net debt, NCI, cash flow, dividends, 2026 budget, Moody's upgrade, Monument, SSE4, MSX, Trident, Amarillo.",
    "Kinder Morgan Q3 2026 earnings call, 21 October 2026, transcript published by Earnings Whispers (Kinder Morgan posts only the webcast): ~US$225m that may not recur, ~US$175m commodity benefit, at least 20-year terms. Third-party transcript.",
    "Kinder Morgan, 'Kinder Morgan Announces 2026 Financial Expectations', 8 December 2025 (Business Wire): timing of the budget announcement.",
    "Nasdaq historical quotes, KMI, retrieved 2 November 2026: daily closes, highs and month-end closes (not adjusted for dividends); cross-checked against stockanalysis.com.",
    "stockanalysis.com (S&P Global Market Intelligence data), retrieved 2 November 2026: consensus EPS (updated 28 October), average target, peer EV/EBITDA and dividend yields.",
    "The Physical Layer, 'Building your own power: GE Vernova's queue, not the grid's, sets the date': https://thephysicallayer.fyi/journal/building-your-own-power/",
    "Estimates for 2026 to 2029 EBITDA, net debt, cash flow and the 2027 dividend are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Call (2 November 2026)", "=Valuation!B14", None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between. Tommy Lau's call: NO CALL."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Base value per share, US$", "=Valuation!B11", USD2, "11.5x 2028E Adjusted EBITDA, less end-2027 net debt and NCI."),
    ("Reference price, US$", "=" + A["price"], USD2, "NYSE close, 30 October 2026."),
    ("Base value against price", "=Valuation!B13", PCT1, ""),
    ("Probability-weighted value, US$", "=Scenarios!E11", USD2, "25 / 50 / 25 bear / base / bull."),
    ("2028E Adjusted EBITDA, US$m", "=EBITDA!G8", M0, "My estimate."),
    ("Horizon", "12 months, to October 2027", None, ""),
    ("Revisit if", "See note", None, REVISIT_IF),
    ("Wrong if", "See note", None, WRONG_IF),
]
for i, (lab, v, fmt, nt) in enumerate(cover):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B
    c = ws.cell(row=rr, column=2, value=v)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    c.font = F_LINK if isinstance(v, str) and v.startswith("=") else F_IN
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
ws.row_dimensions[13].height = 44; ws.row_dimensions[14].height = 58
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("EBITDA", "Adjusted EBITDA 2023A to 2029E: underlying business, one-offs and backlog; net debt."),
    ("Valuation", "Base value, the band, multiples at the price and in history, revisit levels."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "2028E EBITDA against the multiple."),
    ("Backlog", "Backlog by quarter and the named projects by first in-service year."),
    ("Peers", "Trailing EV/EBITDA and dividend yields."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t)
    ws.cell(row=18 + i, column=2, value=d)
ws["A28"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A28"].font = F_NOTE
ws["A29"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."
ws["A29"].font = F_NOTE

for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX, BK)
