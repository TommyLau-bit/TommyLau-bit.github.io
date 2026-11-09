"""TSMC initiation model, 6 Oct 2026. Live formulas throughout.

House style follows the Vertiv model: navy header rows, blue font for hardcoded inputs, yellow fill on my
own assumptions, green font for cross-sheet links, black for formulas.
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

USD2 = '"US$"#,##0.00'; USD0 = '"US$"#,##0'; BN2 = '#,##0.00'; BN1 = '#,##0.0'
PCT1 = '0.0%'; PCT0 = '0%'; MULT = '0.0"x"'; MULT0 = '0"x"'
SUB = f"Tommy Lau | TSMC (NYSE: TSM; TWSE: 2330) | {DATE_LONG} | Personal research, not investment advice."

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


sheet("Cover", "TSMC (NYSE: TSM ADR; TWSE: 2330)  INITIATION MODEL", [36, 24, 80])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [46, 14, 10, 92])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "another tab. Black = formula. US$ billion unless stated; per-ADR figures in US$.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"nonop", "tax", "q3rev", "q3om", "q4rev", "q4om", "g27", "g28", "om27", "om28", "pe"}
rows = [
    ("MARKET (retrieved 6 October 2026)", None, None, None, None),
    ("price", "ADR price (NYSE: TSM)", PRICE, "US$", "NYSE close, 5 October 2026. Yahoo Finance."),
    ("hi52", "ADR 52-week high (intraday)", HI52, "US$", "Yahoo Finance."),
    ("px25", "ADR month-end close, 30 Sep 2025", PRICE_SEP25, "US$", "Yahoo Finance."),
    ("twpx", "Taipei share price (2330.TW)", TW_PRICE, "NT$", "TWSE close, 6 October 2026. Yahoo Finance."),
    ("fx", "NT$ per US$", FX, "NT$", "Yahoo Finance TWD=X, 6 October 2026."),
    ("ratio", "Ordinary shares per ADR", ADR_RATIO, "x", "TSMC ADR ratio."),
    ("shares", "Ordinary shares outstanding", SHARES, "bn", "2Q26 presentation: 25,932mn units at 30 June 2026."),
    ("cash", "Cash and marketable securities, 30 Jun 2026", CASH_NT, "NT$bn", "2Q26 presentation, balance sheet."),
    ("ltd", "Long-term interest-bearing debts, 30 Jun 2026", LTDEBT_NT, "NT$bn", "2Q26 presentation. Current portion not separately shown, so net cash is approximate."),
    ("cons26", "2026 consensus EPS per ADR", CONS_26_ADR, "US$", "MarketBeat, retrieved 6 October 2026. Cross-check only."),
    ("cons27", "2027 consensus EPS per ADR", CONS_27_ADR, "US$", "MarketBeat, retrieved 6 October 2026. Cross-check only."),
    ("fwdpe", "Forward P/E shown by stockanalysis.com", FWD_PE_SA, "x", "stockanalysis.com, 6 October 2026."),
    ("constp", "Average analyst ADR target", CONS_TP, "US$", "stockanalysis.com, 21 analysts, 6 October 2026."),
    ("REPORTED (TSMC 4Q25 presentation, 15 Jan 2026; quarterly releases)", None, None, None, None),
    ("r24", "2024 revenue", REV_USD["2024A"], "US$bn", "TSMC 4Q25 presentation, 2025 financial highlights."),
    ("r25", "2025 revenue", REV_USD["2025A"], "US$bn", "Same."),
    ("gm24", "2024 gross margin", GM["2024A"], "%", "Same."),
    ("gm25", "2025 gross margin", GM["2025A"], "%", "Same."),
    ("om24", "2024 operating margin", OM["2024A"], "%", "Same."),
    ("om25", "2025 operating margin", OM["2025A"], "%", "Same."),
    ("e24", "2024 EPS per ADR", EPS_ADR["2024A"], "US$", "Sum of the four quarterly releases (US$ per ADR unit)."),
    ("e25", "2025 EPS per ADR", EPS_ADR["2025A"], "US$", "Same."),
    ("en24", "2024 EPS per share", EPS_NT["2024A"], "NT$", "TSMC 4Q25 presentation."),
    ("en25", "2025 EPS per share", EPS_NT["2025A"], "NT$", "Same."),
    ("ltgm", "Long-term gross margin floor, through the cycle", 0.56, "%", "TSMC 4Q25 presentation: 56% and higher through the cycle."),
    ("ltcagr", "Revenue CAGR 2024 to 2029, approaching", 0.25, "%", "TSMC 4Q25 presentation, US dollar terms."),
    ("g3lo", "Q3 2026 revenue guide, low", G3_REV[0], "US$bn", "Release of 16 July 2026."),
    ("g3hi", "Q3 2026 revenue guide, high", G3_REV[1], "US$bn", "Same."),
    ("g3fx", "Q3 2026 guide exchange rate", G3_FX, "NT$", "Same."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("nonop", "Non-operating income, % of revenue", NONOP, "%", "MINE. Q1 2026 level (NT$28.83bn on NT$1,134.10bn). Q2 2026 jump to NT$95.83bn treated as non-recurring."),
    ("tax", "Tax and minorities, % of pre-tax profit", TAX, "%", "MINE. 2025: 15.9%; first half 2026: 17.5%."),
    ("q3rev", "Q3 2026 revenue", Q3E_REV, "US$bn", "MINE. July and August monthly revenue already NT$982.4bn; above the guide top."),
    ("q3om", "Q3 2026 operating margin", Q3E_OM, "%", "MINE. Middle of the 56 to 58% guide."),
    ("q4rev", "Q4 2026 revenue", Q4E_REV, "US$bn", "MINE. Gives 2026 growth of 40%, in line with 'slightly above 40%'."),
    ("q4om", "Q4 2026 operating margin", Q4E_OM, "%", "MINE. 2nm ramp dilution of 3 to 4 points on gross margin in the second half."),
    ("g27", "2027 revenue growth", G27, "%", "MINE. Inside TSMC's 2024 to 2029 plan."),
    ("g28", "2028 revenue growth", G28, "%", "MINE. Same; leaves about 10% for 2029 to reach ~US$275bn."),
    ("om27", "2027 operating margin", OM27, "%", "MINE. H2 2026 guide level held."),
    ("om28", "2028 operating margin", OM28, "%", "MINE. Depreciation of 2026 to 2027 capex, overseas dilution widening, 2nm."),
    ("pe", "Target multiple on 2028E EPS (base)", BASE_PE, "x", "MINE. TSMC's own forward P/E today, 20.7x (Peers tab)."),
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
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else ("#,##0.00" if unit != "bn" else "#,##0.000"))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
KADR = f"({A['ratio']}/{A['shares']})"   # ADRs per bn shares -> per-ADR factor

# ===================================================================== QUARTERLY
ws = sheet("Quarterly", "QUARTERLY HISTORY, Q1 2024 TO Q2 2026, AND MY Q3 / Q4 2026", [44] + [10] * 12)
QH = Q + ["Q3 26E", "Q4 26E"]
head(ws, 4, ["US$ billion unless stated"] + QH)
C = [get_column_letter(2 + j) for j in range(12)]


def qrow(row, label, vals, fmt, bold=False):
    ws.cell(row=row, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=row, column=2 + j, value=v if v is not None else "")
        c.number_format = fmt; c.alignment = RIGHT
        if not (isinstance(v, str) and v.startswith("=")) and v is not None:
            c.font = F_IN
        elif isinstance(v, str) and "Assumptions" in v:
            c.font = F_LINK


qrow(5, "Revenue, US$bn", Q_REV_USD + ["=" + A["q3rev"], "=" + A["q4rev"]], BN2, True)
qrow(6, "Revenue, NT$bn", Q_REV_NT + [None, None], BN2)
qrow(7, "Revenue growth y/y, US$ (derived)", [None] * 4 + [f"={C[j]}5/{C[j-4]}5-1" for j in range(4, 12)], PCT1)
qrow(8, "Gross margin", [v / 100 for v in Q_GM] + [None, None], PCT1, True)
qrow(9, "Operating margin", [v / 100 for v in Q_OM] + ["=" + A["q3om"], "=" + A["q4om"]], PCT1)
qrow(10, "EPS per share, NT$", Q_EPS_NT + [None, None], BN2)
qrow(11, "EPS per ADR, US$ (reported; Q3 / Q4 26 mine)", Q_EPS_ADR + [
    f"=K5*(K9+{A['nonop']})*(1-{A['tax']})*{KADR}".replace("K", C[10]),
    f"=L5*(L9+{A['nonop']})*(1-{A['tax']})*{KADR}".replace("L", C[11])], USD2, True)
qrow(12, "HPC share of revenue", [v / 100 for v in Q_HPC] + [None, None], PCT0)
qrow(13, "7nm and below, share of wafer revenue", [v / 100 for v in Q_ADV] + [None, None], PCT0)
qrow(14, "Gross margin above the 56% floor, points (derived)", [f"=({c}8-{A['ltgm']})*100" for c in C[:10]] + [None, None], '+0.0;-0.0')
r = 16
ws.cell(row=r, column=1, value="Wafers and the second quarter").font = Font(bold=True, color=NAVY); r += 1
head(ws, r, ["Item", "Q2 25", "Q1 26", "Q2 26", "Note"]); r += 1
ws.cell(row=r, column=1, value="Wafer shipments, thousand 12-inch equivalent")
for j, k in enumerate(["Q2 25", "Q1 26", "Q2 26"]):
    c = ws.cell(row=r, column=2 + j, value=WAFERS[k]); c.font = F_IN; c.number_format = "#,##0"
ws.cell(row=r, column=5, value="2Q26 presentation.").font = F_NOTE; WR = r; r += 1
ws.cell(row=r, column=1, value="Revenue per wafer, NT$ thousand (derived)")
for j, col in enumerate(["G", "J", "K"]):
    c = ws.cell(row=r, column=2 + j, value=f"={col}6/{get_column_letter(2 + j)}{WR}*1000"); c.number_format = "#,##0"
RPW = r; r += 1
ws.cell(row=r, column=1, value="Wafers y/y, Q2 26 (derived)"); ws.cell(row=r, column=2, value=f"=D{WR}/B{WR}-1").number_format = PCT1; WY = r; r += 1
ws.cell(row=r, column=1, value="Revenue per wafer y/y, Q2 26 (derived)"); ws.cell(row=r, column=2, value=f"=D{RPW}/B{RPW}-1").number_format = PCT1; RY = r; r += 1
ws.cell(row=r, column=1, value="Non-operating items, NT$bn, Q1 26 / Q2 26")
ws.cell(row=r, column=2, value=NONOP_Q1_26).font = F_IN; ws.cell(row=r, column=3, value=NONOP_Q2_26).font = F_IN; NO = r; r += 1
ws.cell(row=r, column=1, value="Q2 26 excess non-operating, after tax, per ADR, US$ (derived)")
c = ws.cell(row=r, column=2, value=f"=(C{NO}-B{NO})*(1-{A['tax']})/{A['shares']}*{A['ratio']}/31.60"); c.number_format = USD2
ws.cell(row=r, column=5, value="At the Q2 26 average rate of NT$31.60 (2Q26 presentation).").font = F_NOTE; EX = r; r += 1
ws.cell(row=r, column=1, value="Capital expenditures, NT$bn, Q1 26 / Q2 26")
ws.cell(row=r, column=2, value=CAPEX_Q_NT["Q1 26"]).font = F_IN; ws.cell(row=r, column=3, value=CAPEX_Q_NT["Q2 26"]).font = F_IN
ws.cell(row=r, column=4, value=f"=B{r}+C{r}").number_format = BN2; ws.cell(row=r, column=5, value="First half total in column D.").font = F_NOTE
CX = r; r += 1
ws.cell(row=r, column=1, value="Capital expenditures, NT$bn, 2024 / 2025")
ws.cell(row=r, column=2, value=CAPEX_NT["2024A"]).font = F_IN; ws.cell(row=r, column=3, value=CAPEX_NT["2025A"]).font = F_IN; r += 2
note(ws, r, ["Source: TSMC quarterly results releases and presentations on Form 6-K, 18 April 2024 to 16 July 2026. HPC share from the revenue-by-platform slides.",
             "Q3 26E and Q4 26E are my estimates; EPS per ADR = revenue x (operating margin + non-operating %) x (1 - tax) x 5 / shares."])

# ===================================================================== MONTHLY
ws = sheet("Monthly", "MONTHLY REVENUE, NT$ BILLION, AND THE Q3 2026 TRACK", [30, 14, 60])
head(ws, 4, ["Month", "Revenue, NT$bn", "Note"])
for i, (lab, v) in enumerate(zip(M_LABELS, M_REV)):
    ws.cell(row=5 + i, column=1, value=lab)
    c = ws.cell(row=5 + i, column=2, value=v); c.font = F_IN; c.number_format = BN2
last = 5 + len(M_REV) - 1
r = last + 2
ws.cell(row=r, column=1, value="Q3 2026 track").font = Font(bold=True, color=NAVY); r += 1
r0 = r
items = [
    ("Jul + Aug 2026", f"=B{last-1}+B{last}", BN2, "Two thirds of the quarter, reported."),
    ("Q3 guide low, NT$bn at guide rate", f"={A['g3lo']}*{A['g3fx']}", BN2, ""),
    ("Q3 guide high, NT$bn at guide rate", f"={A['g3hi']}*{A['g3fx']}", BN2, ""),
    ("September needed for the low end", f"=B{r0+1}-B{r0}", BN2, ""),
    ("September needed for the high end", f"=B{r0+2}-B{r0}", BN2, "August alone was NT$514.81bn."),
    ("Monthly pace of the guide midpoint", f"=({A['g3lo']}+{A['g3hi']})/2*{A['g3fx']}/3", BN2, "Reference line on the chart."),
    ("August 2026 y/y", f"=B{last}/B{last-12}-1", PCT1, "August 2025 in row above."),
]
MT = {}
for lab, f, fmt, nt in items:
    ws.cell(row=r, column=1, value=lab)
    c = ws.cell(row=r, column=2, value=f); c.number_format = fmt
    ws.cell(row=r, column=3, value=nt).font = F_NOTE
    MT[lab] = f"Monthly!$B${r}"; r += 1
note(ws, r + 1, ["Source: TSMC monthly revenue reports on Form 6-K, 10 February 2025 to 10 September 2026. September 2026 is due around 10 October (not confirmed)."])

# ===================================================================== FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (US$ billion unless stated)", [48, 13, 13, 13, 13, 13])
head(ws, 4, ["", "2024A", "2025A", "2026E*", "2027E*", "2028E*"])
L = lambda k: "=" + A[k]
fin = [
    ("Revenue", [L("r24"), L("r25"), "=SUM(Quarterly!J5:M5)", f"=D5*(1+{A['g27']})", f"=E5*(1+{A['g28']})"], BN2, True),
    ("Revenue growth", [None, "=C5/B5-1", "=D5/C5-1", "=E5/D5-1", "=F5/E5-1"], PCT1, False),
    ("Gross margin (reported; not modelled ahead)", [L("gm24"), L("gm25"), None, None, None], PCT1, False),
    ("Operating margin", [L("om24"), L("om25"), "=SUMPRODUCT(Quarterly!J5:M5,Quarterly!J9:M9)/D5", L("om27"), L("om28")], PCT1, False),
    ("Operating profit", ["=B5*B8", "=C5*C8", "=D5*D8", "=E5*E8", "=F5*F8"], BN2, True),
    ("Non-operating income", [None, None, f"=D5*{A['nonop']}", f"=E5*{A['nonop']}", f"=F5*{A['nonop']}"], BN2, False),
    ("Net income after tax and minorities", [None, None, f"=(D9+D10)*(1-{A['tax']})", f"=(E9+E10)*(1-{A['tax']})", f"=(F9+F10)*(1-{A['tax']})"], BN2, False),
    ("EPS per ADR, US$", [L("e24"), L("e25"), "=SUM(Quarterly!J11:M11)", f"=E11*{KADR}", f"=F11*{KADR}"], USD2, True),
    ("EPS growth", [None, "=C12/B12-1", "=D12/C12-1", "=E12/D12-1", "=F12/E12-1"], PCT1, False),
    ("P/E at reference price", ["=" + A["price"] + "/B12", "=" + A["price"] + "/C12", "=" + A["price"] + "/D12", "=" + A["price"] + "/E12", "=" + A["price"] + "/F12"], MULT, False),
]
for i, (label, vals, fmt, bold) in enumerate(fin):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v if v is not None else "")
        c.number_format = fmt; c.alignment = RIGHT
        if isinstance(v, str) and v.startswith("=Assumptions"): c.font = F_LINK
note(ws, 17, [
    "*2026E to 2028E are my own estimates. 2026E = reported Q1 and Q2 plus my Q3 and Q4 (Quarterly tab); 2026E EPS uses reported first-half EPS per ADR (US$7.80).",
    "2024A and 2025A operating profit are derived as revenue x margin. Net income for 2026E (row 11) is illustrative; EPS uses the quarterly build.",
    "EPS bridge 2027E and 2028E: (operating profit + non-operating income) x (1 - tax and minorities) x 5 / 25.932bn shares.",
    f"Note check: 2026E revenue {REV26:.2f}, EPS {EPS26:.2f}; 2027E {R27:.2f}, {EPS27:.2f}; 2028E {R28:.2f}, {EPS28:.2f}.",
])

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION: 20x 2028E EPS PER ADR, TWELVE MONTHS OUT", [56, 16, 70])
head(ws, 4, ["Line", "Value", "Working / note"])
val = [
    ("eps28", "2028E EPS per ADR, US$", "=Financials!F12", USD2, "The market will be pricing 2028 by October 2027."),
    ("mult", "Base multiple, x", "=" + A["pe"], MULT0, "Assumptions tab."),
    ("base", "Base-case value per ADR, US$", "=B5*B6", USD2, "EPS x multiple."),
    ("px", "Reference price, US$", "=" + A["price"], USD2, "NYSE close, 5 October 2026."),
    ("upb", "Base value against the price", "=B7/B8-1", PCT1, "Within +/- 10%: no call on value alone."),
    ("wtd", "Probability-weighted value, US$", "=Scenarios!F11", USD2, "Scenarios tab."),
    ("call", "CALL", '=IF(B9>0.15,"LONG",IF(B9<-0.15,"SHORT","NO CALL"))', None, "Rule of thumb: 15% either side of the price. Conviction is judgement. Tommy Lau's call, 6 Oct 2026."),
    (None, "", None, None, ""),
    ("mcap", "Market value at the ADR price, US$bn", f"={A['shares']}*{A['price']}/{A['ratio']}", BN1, "Shares / 5 x ADR price."),
    ("mcaptw", "Market value at the Taipei price, US$bn", f"={A['shares']}*{A['twpx']}/{A['fx']}", BN1, ""),
    ("nc", "Net cash, US$bn (approximate)", f"=({A['cash']}-{A['ltd']})/{A['fx']}", BN1, "Cash and securities less long-term debt, 30 June 2026."),
    ("prem", "ADR premium to five Taipei shares", f"={A['price']}/{A['ratio']}*{A['fx']}/{A['twpx']}-1", PCT1, ""),
    ("rise", "ADR change since 30 Sep 2025", f"={A['price']}/{A['px25']}-1", PCT1, ""),
    ("hi", "Price below the 52-week high", f"=1-{A['price']}/{A['hi52']}", '0.00%', ""),
    (None, "", None, None, ""),
    ("pe26", "P/E on my 2026E", "=Financials!D14", MULT, ""),
    ("pe27", "P/E on my 2027E", "=Financials!E14", MULT, ""),
    ("pec27", "P/E on the 2027 consensus", f"={A['price']}/{A['cons27']}", MULT, "MarketBeat US$21.33."),
    ("pe28", "P/E on my 2028E", "=Financials!F14", MULT, ""),
    ("vc", "My 2027E EPS against consensus", f"=Financials!E12/{A['cons27']}-1", PCT1, ""),
    (None, "", None, None, ""),
    ("need", "2028 EPS the price needs at the base multiple, US$", f"={A['price']}/{A['pe']}", USD2, "What the market prices in."),
    ("needom", "2028 operating margin that needs, on my 2028E revenue", f"=B26/(Financials!F5*(1-{A['tax']})*{KADR})-{A['nonop']}", PCT1, "Against my 55.5%."),
    ("needrev", "2028 revenue that needs, at my 2028E margin, US$bn", f"=B26/(({A['om28']}+{A['nonop']})*(1-{A['tax']})*{KADR})", BN1, "Against my US$250.9bn."),
    ("plan29", "2029 revenue on TSMC's 25% CAGR from 2024, US$bn", f"={A['r24']}*(1+{A['ltcagr']})^5", BN1, "TSMC 4Q25 presentation."),
    ("plan2729", "Annual growth that leaves for 2027 to 2029", "=(B29/Financials!D5)^(1/3)-1", PCT1, "My base sits inside this."),
    ("revisit", "Price that puts the base case 16% above", "=B7/1.165", USD2, "The 'revisit below about US$400' line."),
]
V = {}
for i, (key, label, f, fmt, nt) in enumerate(val):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=label)
    if f is not None:
        c = ws.cell(row=rr, column=2, value=f)
        if fmt: c.number_format = fmt
        if key in ("base", "call"):
            ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
    if key: V[key] = f"Valuation!$B${rr}"

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT", [12] + [12] * 11)
head(ws, 4, ["Case", "2027 growth", "2028 growth", "2027 margin", "2028 margin", "2027 revenue", "2028 revenue",
             "2028 EPS", "Multiple", "Value, US$", "vs price"])
for i, (name, g1, g2, o1, o2, mult, p) in enumerate(SCEN):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=name).font = F_B
    if name == "Base":
        for j, k in enumerate(["g27", "g28", "om27", "om28"]):
            c = ws.cell(row=rr, column=2 + j, value="=" + A[k]); c.font = F_LINK; c.number_format = PCT1
        c = ws.cell(row=rr, column=9, value="=" + A["pe"]); c.font = F_LINK
    else:
        for j, v in enumerate([g1, g2, o1, o2]):
            c = ws.cell(row=rr, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT1
        c = ws.cell(row=rr, column=9, value=mult); c.font = F_INB; c.fill = FILL_ASSUME
    ws.cell(row=rr, column=9).number_format = MULT0
    ws.cell(row=rr, column=6, value=f"=Financials!$D$5*(1+B{rr})").number_format = BN2
    ws.cell(row=rr, column=7, value=f"=F{rr}*(1+C{rr})").number_format = BN2
    ws.cell(row=rr, column=8, value=f"=G{rr}*(E{rr}+{A['nonop']})*(1-{A['tax']})*{KADR}").number_format = USD2
    ws.cell(row=rr, column=10, value=f"=H{rr}*I{rr}").number_format = USD2
    ws.cell(row=rr, column=11, value=f"=J{rr}/{A['price']}-1").number_format = PCT0
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[6]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, US$"; ws["A11"].font = F_B
ws["F11"] = "=B9*J5+C9*J6+D9*J7"; ws["F11"].number_format = USD2; ws["F11"].font = F_B; ws["F11"].fill = FILL_KEY
ws["G11"] = f"=F11/{A['price']}-1"; ws["G11"].number_format = PCT1
note(ws, 14, ["All cases start from my 2026E revenue and use the same earnings bridge. The 2027 margin affects only 2027 earnings; the value uses 2028.",
              "Bear: the grid binds first and TSMC's tightness eases as 2028 capacity lands. Bull: the factory stays the bottleneck and the scarcity margin holds."])

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER ADR: 2028E EPS AGAINST MULTIPLE (US$)", [24, 14, 14, 14])
head(ws, 4, ["2028 EPS \\ multiple", "", "", ""])
for j, (pe, link) in enumerate(zip(SENS_PE, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["pe"]) if link else pe)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (eps, link) in enumerate(zip(SENS_EPS, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value="=Financials!F12" if link else eps)
    c.number_format = USD2; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=f"=$A{rr}*{col}$4").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
note(ws, 11, ["Middle row links to the model's 2028E EPS and the middle column to the base multiple."])

# ===================================================================== PEERS
ws = sheet("Peers", "PEER MULTIPLES (FORWARD P/E, stockanalysis.com, 6 OCTOBER 2026)", [28, 14, 14, 80])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "What they make"])
for i, (co, tk, pe, what) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if co == "TSMC" else Font()
    ws.cell(row=rr, column=2, value=tk)
    c = ws.cell(row=rr, column=3, value=("=" + A["fwdpe"]) if co == "TSMC" else pe)
    c.number_format = MULT; c.font = F_LINK if co == "TSMC" else F_IN
    ws.cell(row=rr, column=4, value=what).alignment = WRAP
ws["A13"] = "Median of the foundries and ASE (GFS, UMC, ASX)"; ws["C13"] = "=MEDIAN(C6,C7,C9)"; ws["C13"].number_format = MULT
note(ws, 15, ["Intel and Samsung multiples are distorted by recovery and memory cycles. Nvidia is a customer, shown for context.",
              "Multiples only, to set the base multiple. No view on the peers' shares is expressed."])

# ===================================================================== SOURCES
ws = sheet("Sources", "SOURCES", [6, 130])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "TSMC quarterly results releases (Exhibit 99.1) and presentations furnished on Form 6-K, 18 April 2024 to 16 July 2026: revenue, margins, EPS, mix, wafers, balance sheet, cash flow, Q3 2026 guide.",
    "TSMC 4Q25 presentation, 15 January 2026: 2024 and 2025 annual figures; 2024 to 2029 revenue CAGR approaching 25%; long-term gross margin of 56% and higher through the cycle.",
    "TSMC monthly revenue reports on Form 6-K, 10 February 2025 to 10 September 2026.",
    "TSMC earnings call transcripts, 15 January 2026 and 16 July 2026: wafer supply, power, Taiwan electricity, fab build time, capex timing and the US$60 to 64bn budget, packaging, overseas and 2nm dilution, Arizona, dividends.",
    "TSMC Form 6-K, 15 May 2026: sale of up to 8.1% of Vanguard International Semiconductor.",
    "TSMC investor relations, quarterly results page: Q3 2026 conference on 15 October 2026, 14:00 Taiwan time.",
    "Yahoo Finance chart API, retrieved 6 October 2026: TSM month-end closes and 5 October close, 52-week range, 2330.TW close, TWD=X.",
    "MarketBeat, retrieved 6 October 2026: 2026 and 2027 consensus EPS per ADR. stockanalysis.com, retrieved 6 October 2026: forward P/E, analyst target, peer multiples.",
    "The Physical Layer, 'TSMC's chief says the AI bottleneck is its factories, not the power grid', 2 October 2026: https://thephysicallayer.fyi/journal/tsmc-says-it-is-the-bottleneck/",
    "Estimates for 2026 to 2028 are the author's own. Personal research, not investment advice. I hold no position in TSMC.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# ===================================================================== COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Call", "=" + V["call"], None, "Tommy Lau's call, published 6 Oct 2026."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Reference price, US$ per ADR", "=" + A["price"], USD2, "NYSE close, 5 October 2026. 1 ADR = 5 ordinary shares."),
    ("Base value, US$ per ADR", "=" + V["base"], USD2, "20x 2028E EPS."),
    ("Base value against the price", "=" + V["upb"], PCT1, ""),
    ("Probability-weighted value, US$", "=" + V["wtd"], USD2, "25 / 50 / 25 bear / base / bull."),
    ("2026E / 2027E / 2028E EPS per ADR, US$", '=TEXT(Financials!D12,"0.00")&" / "&TEXT(Financials!E12,"0.00")&" / "&TEXT(Financials!F12,"0.00")', None, "Own estimates."),
    ("Horizon", "12 months, to October 2027", None, ""),
    ("Wrong if", "See note", None, "Full year 2027 revenue grows 30% or more in US dollars with an operating margin of 58% or more; or TSMC raises its through-the-cycle gross margin floor above 56%; or the ADR trades above US$560 by October 2027 without either."),
    ("Revisit if", "See note", None, "A price below about US$400, or Q3 gross margin at or above the 67% top of the guide despite the 2nm ramp, or a raised margin floor."),
]
for i, (lab, v, fmt, nt) in enumerate(cover):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B
    c = ws.cell(row=rr, column=2, value=v)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    c.font = F_LINK if isinstance(v, str) and v.startswith("=") else F_IN
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Quarterly", "Q1 2024 to Q2 2026 reported, my Q3 and Q4 2026; wafers, revenue per wafer, non-operating items, capex."),
    ("Monthly", "Monthly revenue January 2025 to August 2026 and the Q3 2026 track against the guide."),
    ("Financials", "2024A to 2028E: revenue, margin, the EPS bridge per ADR, P/E."),
    ("Valuation", "Base value, market value, ADR premium, multiples, what the price needs."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "2028E EPS against multiple."),
    ("Peers", "Forward multiples used to set the base multiple."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t); ws.cell(row=18 + i, column=2, value=d)
ws["A28"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A28"].font = F_NOTE
ws["A29"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."; ws["A29"].font = F_NOTE

for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
