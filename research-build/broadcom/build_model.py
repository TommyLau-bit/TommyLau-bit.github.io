"""Broadcom initiation model, 6 Oct 2026. Live formulas throughout.

House style follows the Vertiv and Marvell models: navy header rows, blue font for hardcoded inputs, yellow fill on
my own assumptions, green font for cross-sheet links, black for formulas.
Non-GAAP basis unless marked GAAP. Fiscal years end on the Sunday closest to 31 October (FY2026 = year to 1 November 2026; FY2027 = about 31 October 2027).
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

USD2 = '"US$"#,##0.00'; USD0 = '"US$"#,##0'; BN2 = '#,##0.00'; BN3 = '#,##0.000'; BN1 = '#,##0.0'
PCT1 = '0.0%'; PCT0 = '0%'; MULT = '0.0"x"'; MULT0 = '0"x"'
SUB = f"Tommy Lau | Broadcom Inc. (Nasdaq: AVGO) | {DATE_LONG} | Non-GAAP basis; FY26 ends 1 Nov 2026, FY27 about 31 Oct 2027 | Personal research, not investment advice."

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


def is_formula(v):
    return isinstance(v, str) and v.startswith("=")


def put(ws, r, c, v, fmt=None, bold=False):
    x = ws.cell(row=r, column=c, value=v if v is not None else "")
    if fmt: x.number_format = fmt
    x.alignment = RIGHT
    if v is not None and not is_formula(v) and not isinstance(v, str):
        x.font = Font(color="0000FF", bold=bold)
    elif isinstance(v, str) and v.startswith("=Assumptions"):
        x.font = Font(color="008000", bold=bold)
    elif bold:
        x.font = F_B
    return x


sheet("Cover", "BROADCOM INC. (NASDAQ: AVGO)  INITIATION MODEL", [38, 26, 90])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [62, 14, 10, 92])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "another tab. Black = formula. US$ billion unless stated; per-share figures in US$; shares in billions.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"q4int", "q4other", "nonai27", "sw27", "sm27", "swm", "int27", "tax", "sh", "ai28", "nonai28", "sw28", "sm28",
        "int28", "msemi", "msw"}
rows = [
    ("MARKET (retrieved 6 October 2026)", None, None, None, None),
    ("price", "Share price (Nasdaq: AVGO)", PRICE, "US$", "Nasdaq close, 5 October 2026. Nasdaq.com historical data (Yahoo Finance refused requests on 6 Oct)."),
    ("hi52", "52-week high (intraday, 3 June 2026)", HI52, "US$", "Nasdaq.com."),
    ("hiclose", "Highest close (2 June 2026)", HI_CLOSE, "US$", "Nasdaq.com."),
    ("lo52", "52-week low (intraday, 30 March 2026)", LO52, "US$", "Nasdaq.com."),
    ("loclose", "Lowest close (30 March 2026)", LO_CLOSE, "US$", "Nasdaq.com."),
    ("pxdec25", "Close, 31 Dec 2025", PRICE_DEC25, "US$", "Nasdaq.com."),
    ("pxpiece", "Close, 1 Oct 2026 (last close before the journal piece)", PRICE_PIECE, "US$", "Nasdaq.com. The piece went live at 12:05 SGT on 2 October."),
    ("common", "Common shares outstanding, 2 Aug 2026", COMMON_OUT, "bn", "10-Q balance sheet: 4,774 million issued and outstanding."),
    ("cash", "Cash and cash equivalents, 2 Aug 2026", CASH, "US$bn", "Q3 FY26 release balance sheet."),
    ("debtst", "Short-term debt, 2 Aug 2026", DEBT_ST, "US$bn", "Same."),
    ("debtlt", "Long-term debt, 2 Aug 2026", DEBT_LT, "US$bn", "Same."),
    ("cons26", "FY26 consensus EPS", CONS_EPS_26, "US$", "stockanalysis.com (S&P Global, updated 2 Oct 2026), 40 analysts; range 11.35 to 12.38."),
    ("cons27", "FY27 consensus EPS", CONS_EPS_27, "US$", "stockanalysis.com (S&P Global). FY28 consensus not verified."),
    ("consrev27", "FY27 consensus revenue", CONS_REV_27, "US$bn", "stockanalysis.com (S&P Global)."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com, 50 analysts; range 215.88 to 715."),
    ("fwdpe", "Forward P/E shown by stockanalysis.com", FWD_PE_SA, "x", "stockanalysis.com, 6 October 2026."),
    ("REPORTED AND GUIDED (Broadcom releases, 10-Q, calls)", None, None, None, None),
    ("g4rev", "Q4 FY26 revenue guide", G4["rev"], "US$bn", "Release of 2 September 2026: approximately US$34.8bn."),
    ("g4ai", "Q4 FY26 AI semiconductor revenue guide", G4["ai"], "US$bn", "Same: US$21.7bn."),
    ("g4semi", "Q4 FY26 semiconductor revenue guide", G4["semi"], "US$bn", "Call of 2 September 2026: approximately US$26.1bn."),
    ("g4nonai", "Q4 FY26 non-AI semiconductor revenue guide", G4["nonai_call"], "US$bn", "Call of 2 September 2026: approximately US$4.3bn."),
    ("g4sw", "Q4 FY26 infrastructure software guide", G4["sw"], "US$bn", "Same: approximately US$8.7bn."),
    ("g4om", "Q4 FY26 non-GAAP operating margin guide", G4["om"], "%", "Release: approximately 66% of revenue."),
    ("g4gm", "Q4 FY26 gross margin guide", G4["gm"], "%", "Call: approximately 73%."),
    ("g4tax", "Non-GAAP tax rate, Q4 and FY26", G4["tax"], "%", "Call: approximately 16% (global minimum tax)."),
    ("g4sh", "Q4 FY26 non-GAAP diluted shares", G4["sh"], "bn", "Call: approximately 4.94 billion."),
    ("ai27", "FY27 AI revenue outlook", AI_FY27_OUT, "US$bn", "Call: secured the supply to double AI revenue to approximately US$115bn."),
    ("ai28out", "FY28 AI revenue outlook", AI_FY28_OUT, "US$bn", "Call: line of sight to US$230bn; supply secured for it too."),
    ("eps28call", "FY28 EPS management expects to exceed", EPS28_CALL, "US$", "Call: on target to exceed US$30 in FY28."),
    ("semiop", "Semiconductor segment operating income, Q3 FY26", SEG_Q3["semi_op"], "US$bn", "10-Q segment table."),
    ("swop", "Infrastructure software operating income, Q3 FY26", SEG_Q3["sw_op"], "US$bn", "Same."),
    ("backstop", "Maximum potential liability under the Backstop", BACKSTOP_MAX, "US$bn", "10-Q: approximately US$29bn, undiscounted, upon deployment of all racks."),
    ("notes", "Convertible notes the customer may issue to Broadcom", CONV_NOTES, "US$bn", "10-Q: up to US$42bn; none issued at 2 Aug 2026."),
    ("purch28", "Unconditional purchase commitments falling in FY28", PURCH[1], "US$bn", "10-Q: US$72.952bn (FY27 US$52.674bn; total US$126.821bn)."),
    ("netq3", "Networking share of AI revenue, Q3 FY26", NET_SHARE["Q3 26"], "%", "Call: XPU shipments 73% of AI revenue."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("q4int", "Non-GAAP interest expense, Q4 FY26", Q4_INT, "US$bn", "MINE. Q3 was US$0.703bn before US$1.5bn of notes repaid."),
    ("q4other", "Other income, Q4 FY26", Q4_OTHER, "US$bn", "MINE. Q3 was US$0.098bn."),
    ("nonai27", "Non-AI semiconductor revenue, FY27", NONAI27, "US$bn", "MINE. About 4% growth."),
    ("sw27", "Infrastructure software revenue, FY27", SW27, "US$bn", "MINE. About 7% growth; Q4 FY26 guided to stabilise at US$8.7bn."),
    ("sm27", "Semiconductor segment operating margin, FY27", SM27, "%", "MINE. 61.3% in Q3 FY26; about 60% implied by the Q4 guide."),
    ("swm", "Software segment operating margin, FY27 and FY28", SWM, "%", "MINE. 83.7% in Q3 FY26; 80.5% over three quarters."),
    ("int27", "Non-GAAP interest and other, net, FY27", INT27, "US$bn", "MINE."),
    ("tax", "Non-GAAP tax rate, FY27 and FY28", TAX, "%", "MINE: the FY26 guide held."),
    ("sh", "Diluted shares, FY27 and FY28", SH, "bn", "MINE: the Q4 guide held; buybacks offset dilution."),
    ("ai28", "AI revenue, FY28 (base)", AI28, "US$bn", "MINE. 17% below management's US$230bn: my judgement on customer credit and deployment risk."),
    ("nonai28", "Non-AI semiconductor revenue, FY28", NONAI28, "US$bn", "MINE."),
    ("sw28", "Infrastructure software revenue, FY28", SW28, "US$bn", "MINE. About 6% growth."),
    ("sm28", "Semiconductor segment operating margin, FY28 (base)", SM28, "%", "MINE. Memory-heavy racks dilute the margin."),
    ("int28", "Non-GAAP interest and other, net, FY28", INT28, "US$bn", "MINE."),
    ("msemi", "Multiple on chip after-tax operating profit (base)", M_SEMI, "x", "MINE. Median forward P/E of five chip peers 20.7x (Peers tab), rounded down."),
    ("msw", "Multiple on software after-tax operating profit (base)", M_SW, "x", "MINE. Median forward P/E of five software peers 17.4x (Peers tab)."),
]
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY); r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    mine = key in MINE
    c.font = F_INB if mine else F_IN
    if mine: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else ("#,##0.000" if unit == "bn" else ("#,##0.00" if unit == "US$" else BN3)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1

# ===================================================================== QUARTERLY
ws = sheet("Quarterly", "QUARTERLY HISTORY, Q1 FY25 TO Q3 FY26, AND THE Q4 FY26 GUIDE", [52] + [11] * 8)
QH = Q + ["Q4 FY26E"]
head(ws, 4, ["US$ billion unless stated"] + QH)
C = [get_column_letter(2 + j) for j in range(8)]   # B..I


def qrow(row, label, vals, fmt, bold=False):
    ws.cell(row=row, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        put(ws, row, 2 + j, v, fmt)


qrow(5, "Revenue", Q_REV + ["=" + A["g4rev"]], BN3, True)
qrow(6, "Semiconductor solutions (Q4: AI plus non-AI guides)", Q_SEMI + ["=I7+I8"], BN3)
qrow(7, "  of which AI semiconductors", Q_AI + ["=" + A["g4ai"]], BN1)
qrow(8, "  of which non-AI semiconductors (derived; Q4 guided)", [f"={c}6-{c}7" for c in C[:7]] + ["=" + A["g4nonai"]], BN3)
qrow(9, "Infrastructure software", Q_SW + ["=" + A["g4sw"]], BN3)
qrow(10, "AI share of revenue", [f"={c}7/{c}5" for c in C], PCT1)
qrow(11, "AI growth on a year earlier", [None] * 4 + [f"={C[j]}7/{C[j - 4]}7-1" for j in range(4, 8)], PCT1)
qrow(12, "Networking share of AI revenue (where disclosed on calls)", [None, None, NET_SHARE["Q3 25"], None, NET_SHARE["Q1 26"], NET_SHARE["Q2 26"], NET_SHARE["Q3 26"], None], PCT1)
qrow(13, "Gross margin, non-GAAP, US$bn", Q_GMD + [f"=I5*{A['g4gm']}"], BN3)
qrow(14, "Gross margin, non-GAAP", [f"={c}13/{c}5" for c in C], PCT1)
qrow(15, "Operating income, non-GAAP", Q_OPD + [f"=I5*{A['g4om']}"], BN3, True)
qrow(16, "Operating margin, non-GAAP", [f"={c}15/{c}5" for c in C], PCT1)
qrow(17, "Net profit, non-GAAP", Q_NI + [f"=(I15+{A['q4int']}+{A['q4other']})*(1-{A['g4tax']})"], BN3)
qrow(18, "Diluted shares, non-GAAP, bn", Q_SH + ["=" + A["g4sh"]], "#,##0.000")
qrow(19, "Diluted EPS, US$ (reported; Q4 mine)", Q_EPS + ["=I17/I18"], USD2, True)
ws["A21"] = "Checks"; ws["A21"].font = Font(bold=True, color=NAVY)
chk = [
    (22, "AI growth, Q3 FY26 on Q3 FY25", "=H11", PCT1),
    (23, "AI share of revenue, Q3 FY26", "=H10", PCT1),
    (24, "Custom accelerator revenue, Q3 FY26 (73% of AI)", "=H7*(1-H12)", BN2),
    (25, "AI networking revenue, Q3 FY26 (27% of AI)", "=H7*H12", BN2),
    (26, "Gross margin change, Q3 FY25 to Q3 FY26, points", "=(H14-D14)*100", BN1),
    (27, "Semiconductor segment operating margin, Q3 FY26", f"={A['semiop']}/H6", PCT1),
    (28, "Software segment operating margin, Q3 FY26", f"={A['swop']}/H9", PCT1),
]
for rr, lab, f, fmt in chk:
    ws.cell(row=rr, column=1, value=lab); c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
note(ws, 30, ["Source: Broadcom results releases (Exhibit 99.1 to Form 8-K), 6 March 2025 to 2 September 2026, with comparatives; AI revenue for Q4 FY25 and the networking shares from the earnings calls.",
              "Q4 FY26E uses the guide of 2 September 2026; interest, other income and so Q4 EPS are my estimates.",
              "The Q4 segment guides (AI US$21.7bn, non-AI about US$4.3bn, software about US$8.7bn) sum to US$34.7bn against the US$34.8bn consolidated guide; revenue uses the consolidated figure."])

# ===================================================================== FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (US$ billion unless stated, non-GAAP basis)", [52, 12, 12, 12, 12, 12])
head(ws, 4, ["", "FY24A", "FY25A", "FY26E*", "FY27E*", "FY28E*"])
fin = [
    (5, "AI semiconductors", [AI_H[0], AI_H[1], "=SUM(Quarterly!F7:I7)", "=" + A["ai27"], "=Scenarios!B6"], BN1, False),
    (6, "Non-AI semiconductors", [SEMI_H[0] - AI_H[0], SEMI_H[1] - AI_H[1], "=SUM(Quarterly!F8:I8)", "=" + A["nonai27"], "=" + A["nonai28"]], BN2, False),
    (7, "Semiconductor solutions", ["=B5+B6", "=C5+C6", "=D5+D6", "=E5+E6", "=F5+F6"], BN2, False),
    (8, "Infrastructure software", [SW_H[0], SW_H[1], "=SUM(Quarterly!F9:I9)", "=" + A["sw27"], "=" + A["sw28"]], BN2, False),
    (9, "Revenue", ["=B7+B8", "=C7+C8", "=SUM(Quarterly!F5:I5)", "=E7+E8", "=F7+F8"], BN2, True),
    (10, "Revenue growth", [f"=B9/{FY23_REV}-1", "=C9/B9-1", "=D9/C9-1", "=E9/D9-1", "=F9/E9-1"], PCT1, False),
    (11, "Gross margin, non-GAAP", [GMH[0] / REV_H[0], GMH[1] / REV_H[1], "=SUM(Quarterly!F13:I13)/D9", None, None], PCT1, False),
    (12, "Semiconductor operating income", [None, None, None, f"=E7*{A['sm27']}", "=F7*Scenarios!C6"], BN3, False),
    (13, "Software operating income", [None, None, None, f"=E8*{A['swm']}", f"=F8*{A['swm']}"], BN3, False),
    (14, "Operating income", [OPH[0], OPH[1], "=SUM(Quarterly!F15:I15)", "=E12+E13", "=F12+F13"], BN3, True),
    (15, "Operating margin", ["=B14/B9", "=C14/C9", "=D14/D9", "=E14/E9", "=F14/F9"], PCT1, False),
    (16, "Interest and other, net", [None, None, None, "=" + A["int27"], "=" + A["int28"]], BN3, False),
    (17, "Tax rate", [None, None, "=" + A["g4tax"], "=" + A["tax"], "=" + A["tax"]], PCT1, False),
    (18, "Net profit", [NIH[0], NIH[1], "=SUM(Quarterly!F17:I17)", "=(E14+E16)*(1-E17)", "=(F14+F16)*(1-F17)"], BN3, True),
    (19, "Diluted shares, bn", [SHH[0], SHH[1], None, "=" + A["sh"], "=" + A["sh"]], "#,##0.000", False),
    (20, "Diluted EPS, US$", [EPS_H[0], EPS_H[1], "=SUM(Quarterly!F19:I19)", "=E18/E19", "=F18/F19"], USD2, True),
    (21, "EPS growth", [None, "=C20/B20-1", "=D20/C20-1", "=E20/D20-1", "=F20/E20-1"], PCT1, False),
    (22, "P/E at reference price", [None, f"={A['price']}/C20", f"={A['price']}/D20", f"={A['price']}/E20", f"={A['price']}/F20"], MULT, False),
    (23, "Consensus EPS, US$", [None, None, "=" + A["cons26"], "=" + A["cons27"], None], USD2, False),
    (24, "Mine against consensus", [None, None, "=D20/D23-1", "=E20/E23-1", None], PCT1, False),
    (25, "P/E on consensus", [None, None, f"={A['price']}/D23", f"={A['price']}/E23", None], MULT, False),
    (26, "My revenue against consensus revenue", [None, None, None, f"=E9/{A['consrev27']}-1", None], PCT1, False),
]
for rr, label, vals, fmt, bold in fin:
    ws.cell(row=rr, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        put(ws, rr, 2 + j, v, fmt)
note(ws, 28, [
    "*FY26E sums three reported quarters and the Q4 guide (Quarterly tab). FY27E takes management's US$115bn AI outlook; the rest of FY27E and all of FY28E are my estimates. FY28E is the base case (Scenarios row 6).",
    "FY24A and FY25A as reported; FY25 AI revenue is the sum of the four quarters. FY24 and FY25 EPS are non-GAAP net profit over non-GAAP diluted shares.",
    "Consensus from stockanalysis.com (S&P Global data, last updated 2 October 2026). FY28 consensus not verified.",
    f"Note check: FY26E EPS {EPS26:.2f}; FY27E revenue {REV27:.2f}, EPS {EPS27:.2f}; FY28E revenue {REV28:.2f}, EPS {EPS28:.2f}.",
])

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (SUM OF THE PARTS ON FY28E)", [16] + [13] * 12)
head(ws, 4, ["Case", "FY28 AI rev.", "Chip op. margin", "Chip multiple", "Software multiple", "Chip revenue", "Chip op. income",
             "Software op. income", "FY28 EPS", "Chip value / share", "Software value / share", "Value, US$", "vs price"])
for i, s in enumerate(SCEN):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    if s[0] == "Base":
        for col, key, fmt in [(2, "ai28", BN1), (3, "sm28", PCT1), (4, "msemi", MULT0), (5, "msw", MULT0)]:
            c = ws.cell(row=rr, column=col, value="=" + A[key]); c.font = F_LINK; c.number_format = fmt
    else:
        for col, v, fmt in [(2, s[1], BN1), (3, s[2], PCT1), (4, s[3], MULT0), (5, s[4], MULT0)]:
            c = ws.cell(row=rr, column=col, value=v); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = fmt
    ws.cell(row=rr, column=6, value=f"=B{rr}+{A['nonai28']}").number_format = BN1
    ws.cell(row=rr, column=7, value=f"=F{rr}*C{rr}").number_format = BN2
    ws.cell(row=rr, column=8, value=f"={A['sw28']}*{A['swm']}").number_format = BN2
    ws.cell(row=rr, column=9, value=f"=(G{rr}+H{rr}+{A['int28']})*(1-{A['tax']})/{A['sh']}").number_format = USD2
    ws.cell(row=rr, column=10, value=f"=G{rr}*(1-{A['tax']})*D{rr}/{A['sh']}").number_format = USD2
    ws.cell(row=rr, column=11, value=f"=H{rr}*(1-{A['tax']})*E{rr}/{A['sh']}").number_format = USD2
    ws.cell(row=rr, column=12, value=f"=J{rr}+K{rr}-Valuation!$B$6/{A['sh']}").number_format = USD2
    ws.cell(row=rr, column=13, value=f"=L{rr}/{A['price']}-1").number_format = PCT0
ws["A10"] = "Probability"; ws["A10"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=9, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=10, column=2 + j, value=s[5]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E10"] = "=SUM(B10:D10)"; ws["E10"].number_format = PCT0; ws["F10"] = "must be 100%"; ws["F10"].font = F_NOTE
ws["A12"] = "Probability-weighted value, US$"; ws["A12"].font = F_B
ws["L12"] = "=B10*L5+C10*L6+D10*L7"; ws["L12"].number_format = USD2; ws["L12"].font = F_B; ws["L12"].fill = FILL_KEY
ws["M12"] = f"=L12/{A['price']}-1"; ws["M12"].number_format = PCT1
note(ws, 14, ["Value = chip after-tax operating profit x chip multiple + software after-tax operating profit x software multiple - net debt, over FY28 diluted shares.",
              "Software (US$35.5bn at 81%) and non-AI chips (US$18bn) are the same in all three cases. Net debt is held at its 2 August 2026 level (Valuation tab).",
              "Bear: lab financing stalls and AI revenue does not grow after FY27. Bull: management's US$230bn arrives in full. The base row (6) drives the Financials tab."])

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION: SUM OF THE PARTS ON FY28E, TWELVE MONTHS OUT", [70, 16, 70])
head(ws, 4, ["Line", "Value", "Working / note"])
val = [
    ("debt", "Total debt, US$bn", f"={A['debtst']}+{A['debtlt']}", BN3, "2 August 2026."),
    ("nd", "Net debt, US$bn", f"=B5-{A['cash']}", BN3, "Held flat to October 2027 (my assumption: cash after dividends goes to buybacks)."),
    ("vsemi", "Chip value per share, US$", "=Scenarios!J6", USD2, "Base case."),
    ("vsw", "Software value per share, US$", "=Scenarios!K6", USD2, "Base case."),
    ("ndps", "Net debt per share, US$", f"=B6/{A['sh']}", USD2, ""),
    ("base", "Base-case value per share, US$", "=B7+B8-B9", USD2, "Sum of the parts."),
    ("px", "Reference price, US$", "=" + A["price"], USD2, "Nasdaq close, 5 October 2026."),
    ("upb", "Base value against the price", "=B10/B11-1", PCT1, ""),
    ("wtd", "Probability-weighted value, US$", "=Scenarios!L12", USD2, "Scenarios tab."),
    ("rule", "Rule on value alone (long at 15% above, short at 25% below)", '=IF(B12>=0.15,"LONG",IF(B12<=-0.25,"SHORT","NO CALL"))', None, "Mechanical only; wider on the short side because a short's losses are open-ended."),
    ("call", "DRAFT VIEW" if CALL["draft"] else "CALL", CALL["direction"], None, "Tommy Lau's call, published 7 Oct 2026."),
    ("tgt", "Target, US$", CALL["target"], USD2, "Base value rounded to the nearest US$5."),
    ("mcap", "Market value, US$bn", f"={A['price']}*{A['common']}", BN1, "On 4,774m shares."),
    ("ev", "Enterprise value, US$bn", "=B17+B6", BN1, ""),
    ("piece", "Change since the last close before the journal piece (1 Oct 2026)", f"={A['price']}/{A['pxpiece']}-1", PCT1, ""),
    ("offhi", "Against the highest close (2 Jun 2026)", f"={A['price']}/{A['hiclose']}-1", PCT1, ""),
    ("rise", "Change since 31 Dec 2025", f"={A['price']}/{A['pxdec25']}-1", PCT1, ""),
    ("pe25", "P/E on FY25 EPS", "=Financials!C22", MULT, ""),
    ("pe26", "P/E on my FY26E", "=Financials!D22", MULT, ""),
    ("pe27", "P/E on my FY27E", "=Financials!E22", MULT, ""),
    ("pe28", "P/E on my FY28E", "=Financials!F22", MULT, ""),
    ("pec27", "P/E on FY27 consensus", "=Financials!E25", MULT, "stockanalysis.com."),
    ("pe30", "P/E on management's 'more than US$30' FY28 EPS", f"={A['price']}/{A['eps28call']}", MULT, ""),
    ("needsemi", "Chip after-tax operating profit the price needs, US$bn", f"=({A['price']}*{A['sh']}+B6-Scenarios!K6*{A['sh']})/{A['msemi']}", BN2, "At the base multiples, software at its base value."),
    ("needrev", "Chip revenue that needs at the base margin, US$bn", f"=B28/(1-{A['tax']})/{A['sm28']}", BN1, ""),
    ("needai", "FY28 AI revenue the price needs, US$bn", f"=B29-{A['nonai28']}", BN1, "What the market prices in."),
    ("needg", "That as growth on FY27's US$115bn", f"=B30/{A['ai27']}-1", PCT1, ""),
    ("cut", "My FY28 AI revenue below management's", f"=1-{A['ai28']}/{A['ai28out']}", PCT1, ""),
    ("g28", "My FY28 AI revenue against FY27", f"={A['ai28']}/{A['ai27']}-1", PCT1, ""),
    ("nocall", "Price above which the base is less than 15% above (long lapses to no call)", "=B10/1.15", USD2, ""),
    ("bstop", "Backstop as a share of market value", f"={A['backstop']}/B17", PCT1, ""),
    ("swshare", "Software share of the base value", "=B8/B10", PCT1, ""),
]
V = {}
for i, (key, label, f, fmt, nt) in enumerate(val):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=label)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    if not is_formula(f): c.font = F_IN
    if key in ("base", "call"):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    if key == "call": c.font = F_INB
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
    V[key] = f"Valuation!$B${rr}"
assert V["needsemi"] == "Valuation!$B$28" and V["base"] == "Valuation!$B$10" and V["mcap"] == "Valuation!$B$17"

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: FY28 AI REVENUE AGAINST THE CHIP MULTIPLE (US$)", [28, 14, 14, 14])
head(ws, 4, ["FY28 AI revenue \\ chip multiple", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_M, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["msemi"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (a, link) in enumerate(zip(SENS_AI, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=("=" + A["ai28"]) if link else a)
    c.number_format = BN1; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j,
                value=f"=(($A{rr}+{A['nonai28']})*{A['sm28']}*(1-{A['tax']})*{col}$4+Scenarios!$K$6*{A['sh']}-Valuation!$B$6)/{A['sh']}").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells more than 15% above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">"&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["Middle row links to my base FY28 AI revenue and the middle column to the base chip multiple. Software at 17x, chip margin 58% and net debt held throughout."])

# ===================================================================== PEERS
ws = sheet("Peers", "PEER MULTIPLES (FORWARD P/E, stockanalysis.com, 6 OCTOBER 2026)", [28, 16, 14, 80])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "What they make"])
ws.cell(row=5, column=1, value="Broadcom").font = F_B; ws.cell(row=5, column=2, value="Nasdaq: AVGO")
c = ws.cell(row=5, column=3, value="=" + A["fwdpe"]); c.font = F_LINK; c.number_format = MULT
ws.cell(row=5, column=4, value="Custom AI chips, switch chips, optical parts, infrastructure software")
ws.cell(row=6, column=1, value="Chip peers").font = Font(bold=True, color=NAVY)
for i, (co, tk, pe, what) in enumerate(SEMI_PEERS):
    rr = 7 + i
    ws.cell(row=rr, column=1, value=co); ws.cell(row=rr, column=2, value=tk)
    c = ws.cell(row=rr, column=3, value=pe); c.number_format = MULT; c.font = F_IN
    ws.cell(row=rr, column=4, value=what).alignment = WRAP
ws["A12"] = "Median, chip peers"; ws["A12"].font = F_B; ws["C12"] = "=MEDIAN(C7:C11)"; ws["C12"].number_format = MULT
ws.cell(row=13, column=1, value="Software peers").font = Font(bold=True, color=NAVY)
for i, (co, tk, pe, what) in enumerate(SW_PEERS):
    rr = 14 + i
    ws.cell(row=rr, column=1, value=co); ws.cell(row=rr, column=2, value=tk)
    c = ws.cell(row=rr, column=3, value=pe); c.number_format = MULT; c.font = F_IN
    ws.cell(row=rr, column=4, value=what).alignment = WRAP
ws["A19"] = "Median, software peers"; ws["A19"].font = F_B; ws["C19"] = "=MEDIAN(C14:C18)"; ws["C19"].number_format = MULT
co, tk, pe, what = OTHER_PEERS[0]
ws["A21"] = co + " (reference)"; ws["B21"] = tk; ws["C21"] = pe; ws["C21"].number_format = MULT; ws["C21"].font = F_IN; ws["D21"] = what
note(ws, 23, ["Forward P/E as shown on stockanalysis.com during US trading on 6 October 2026. Multiples only, to set the base multiples.",
              "No view on the peers' shares is expressed."])

# ===================================================================== SOURCES
ws = sheet("Sources", "SOURCES", [6, 130])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Broadcom results releases (Exhibit 99.1 to Form 8-K), 12 December 2024 to 2 September 2026, with comparatives: revenue, segment revenue, AI revenue, non-GAAP gross margin, operating income, net income, diluted shares, EPS, stock-based pay, balance sheet, Q4 FY26 guide.",
    "Broadcom Form 10-Q for the quarter to 2 August 2026 (filed 10 September 2026): 4,774m shares outstanding; remaining performance obligations US$179.2bn; purchase commitments US$126.8bn (US$52.7bn FY27, US$73.0bn FY28); AI XPV platform; Backstop up to about US$29bn; convertible notes up to US$42bn; top five end customers about 55% of Q3 revenue (about 40% a year earlier); one distributor 50%; segment operating income.",
    "Broadcom Form 8-K of 6 April 2026: long-term agreement with Google for future TPU generations and supply assurance for networking through up to 2031; Anthropic to access about 3.5 gigawatts of next generation TPU-based compute through Broadcom from 2027, dependent on Anthropic's continued commercial success.",
    "Broadcom earnings calls: Q3 FY25 (4 September 2025; XPUs 65% of AI revenue), Q4 FY25 (11 December 2025; AI revenue US$6.5bn; Ironwood TPU racks for Anthropic), Q1 FY26 (4 March 2026; networking one third of AI revenue; sixth customer), Q2 FY26 (3 June 2026; networking almost 40%, about 30% expected), Q3 FY26 (2 September 2026; XPUs 73%; six customers; TPU 8i ahead of MediaTek's 8t; US$115bn and US$230bn outlooks; EPS above US$30 in FY28; gross margin; XPV tranche; substrates and lasers; results on 9 December 2026). Transcripts: fool.com (2 September 2026) and transcripts.platformaeronaut.com (others).",
    "Nasdaq.com historical prices, retrieved 6 October 2026: daily and month-end closes, 52-week range. (Yahoo Finance chart API refused requests on 6 October 2026.)",
    "stockanalysis.com, retrieved 6 October 2026: FY26 and FY27 consensus EPS and revenue (S&P Global, updated 2 October 2026), average target, forward P/E for Broadcom and peers.",
    "The Physical Layer, 'Broadcom is paid whether the cloud giants stay with Nvidia or leave', 2 October 2026: https://thephysicallayer.fyi/journal/broadcom-wins-either-way/",
    "Estimates for FY26 Q4 below operating income, FY27 and FY28, and the sum of the parts are the author's own. Personal research, not investment advice. I hold no position in Broadcom.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# ===================================================================== COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Draft view" if CALL["draft"] else "Call", "=" + V["call"], None, "Draft for Tommy Lau's decision; not yet a call." if CALL["draft"] else "Tommy Lau's call."),
    ("Target, US$" if CALL["draft"] else "Target, US$", "=" + V["tgt"], USD2, "Base value rounded to the nearest US$5."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Reference price, US$", "=" + A["price"], USD2, "Nasdaq close, 5 October 2026."),
    ("Base value, US$", "=" + V["base"], USD2, "Sum of the parts on FY28E: chips at 20x and software at 17x after-tax operating profit, less net debt."),
    ("Base value against the price", "=" + V["upb"], PCT1, ""),
    ("Probability-weighted value, US$", "=" + V["wtd"], USD2, "25 / 50 / 25 bear / base / bull."),
    ("FY26E / FY27E / FY28E EPS, US$", '=TEXT(Financials!D20,"0.00")&" / "&TEXT(Financials!E20,"0.00")&" / "&TEXT(Financials!F20,"0.00")', None, "Own estimates, non-GAAP, diluted."),
    ("Horizon", "12 months, to October 2027", None, ""),
    ("Wrong if", "See note", None, WRONG_IF),
]
for i, (lab, v, fmt, nt) in enumerate(cover):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B
    c = ws.cell(row=rr, column=2, value=v)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    c.font = F_LINK if is_formula(v) else F_IN
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Quarterly", "Q1 FY25 to Q3 FY26 reported, the Q4 FY26 guide, and the AI, networking and margin tests."),
    ("Financials", "FY24A to FY28E by part: AI, non-AI chips, software; margins, EPS, P/E, consensus."),
    ("Scenarios", "Bear / base / bull sum of the parts and the probability-weighted value."),
    ("Valuation", "Base value, net debt, market value, multiples, what the price needs."),
    ("Sensitivity", "FY28 AI revenue against the chip multiple."),
    ("Peers", "Forward multiples used to set the chip and software multiples."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t); ws.cell(row=18 + i, column=2, value=d)
ws["A28"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A28"].font = F_NOTE
ws["A29"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."; ws["A29"].font = F_NOTE

order = ["Cover", "Assumptions", "Quarterly", "Financials", "Scenarios", "Valuation", "Sensitivity", "Peers", "Sources"]
wb._sheets = [wb[n] for n in order]
for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
