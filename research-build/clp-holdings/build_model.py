"""CLP Holdings Limited (HKEX: 0002) initiation model. Scheme of Control asset base and Hong Kong earnings to 2028E,
Group earnings, sum-of-the-parts valuation, scenarios, sensitivity, peers. Live formulas throughout. House style follows the
Vertiv and Constellation models: navy header rows, blue font for hardcoded inputs, yellow fill on my own assumptions, green
font for cross-sheet links, black for formulas.
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

HKD2 = '"HK$"#,##0.00'
HKD0 = '"HK$"#,##0'
M0 = '#,##0'
M1 = '#,##0.0'
M3 = '0.000'
PCT1 = '0.0%'
PCT2 = '0.00%'
PCT0 = '0%'
MULTF = '0.0"x"'
MULT0 = '0"x"'
SUB = f"Tommy Lau | CLP Holdings Limited (HKEX: 0002) | {DATE} | Personal research, not investment advice."

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
    elif isinstance(v, str) and v.startswith(("=Assumptions", "=SoC", "=Earnings")): c.font = F_LINK
    if fill: c.fill = fill
    c.alignment = RIGHT
    return c


# =====================================================================  COVER (filled last)
ws = sheet("Cover", "CLP HOLDINGS LIMITED (HKEX: 0002)  INITIATION MODEL", [42, 24, 100])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [66, 14, 10, 110])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. HK$ million unless stated. Year end 31 December.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
AR = "CLP Holdings annual results announcement 2025, 26 February 2026"
IR = "CLP Holdings interim results 2026, 6 August 2026"
OC = "CLP Power Hong Kong offering circular, US$4.5bn MTN programme, 1 April 2026, SoC statements"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "HK$", "HKEX close, 2 November 2026. stockanalysis.com daily history; Yahoo Finance quote page, both read 2 November 2026."),
    ("hiclose", "Highest close of the past year, 21 August 2026", HI_CLOSE, "HK$", "stockanalysis.com daily history. Intraday high HK$79.80 on 21 and 24 August."),
    ("pxdec", "Close, 31 December 2025", PX_DEC25, "HK$", "Yahoo Finance monthly history."),
    ("shares", "Shares in issue", SHARES, "m", "2,526,450,570; quarterly statement of 12 October 2026."),
    ("cash", "Cash and cash equivalents, 30 June 2026", CASH, "HK$m", IR + "."),
    ("debt", "Bank loans and other borrowings, 30 June 2026", DEBT, "HK$m", IR + ": current 14,628 + non-current 52,015."),
    ("perps", "Perpetual capital securities, 31 December 2025", PERPS, "HK$m", AR + "."),
    ("dps25", "Dividends per share, 2025", DPS25, "HK$", AR + "."),
    ("REPORTED EARNINGS (OPERATING EARNINGS BEFORE FAIR VALUE MOVEMENTS)", None, None, None, None),
    ("ope24", "Group, 2024", OPE["2024A"], "HK$m", AR + "."),
    ("ope25", "Group, 2025", OPE["2025A"], "HK$m", AR + "."),
    ("ope_h125", "Group, first half 2025", H1_OPE["2025"], "HK$m", IR + "."),
    ("ope_h126", "Group, first half 2026", H1_OPE["2026"], "HK$m", IR + "."),
    ("hk24", "Hong Kong energy business and related, 2024", HK_OPE["2024A"], "HK$m", AR + ": 8,694 + 201."),
    ("hk25", "Hong Kong energy business and related, 2025", HK_OPE["2025A"], "HK$m", AR + ": 9,312 + 232."),
    ("hk_h126", "Hong Kong energy business and related, first half 2026", H1_HK["2026"], "HK$m", IR + ": 4,736 + 94; +5.7%."),
    ("ovs25", "Mainland, Australia, India, Taiwan Region and SE Asia, 2025", 1598.0 + 85.0 + 221.0 + 179.0, "HK$m", AR + ": 1,598 + 85 + 221 + 179."),
    ("corp25", "Other Hong Kong, unallocated finance income and Group expenses, 2025", OTHER25, "HK$m", AR + ": -76 + 44 - 910."),
    ("SCHEME OF CONTROL", None, None, None, None),
    ("prate", "Permitted return on average net fixed assets", PERMIT_RATE, "%", OC + ". SoC to 31 December 2033."),
    ("pr23", "SoC permitted return, 2023", PERMITTED["2023"], "HK$m", OC + "."),
    ("pr24", "SoC permitted return, 2024", PERMITTED["2024"], "HK$m", OC + "."),
    ("pr25", "SoC permitted return, 2025", PERMITTED["2025"], "HK$m", OC + "."),
    ("nr24", "Net return after CESF contribution, 2024", NET_AFTER_CESF["2024"], "HK$m", OC + "."),
    ("nr25", "Net return after CESF contribution, 2025", NET_AFTER_CESF["2025"], "HK$m", OC + "."),
    ("clp25", "CLP Power's share of net return after CESF (CLP Power 100%, CAPCO 70%), 2025", CLP_SHARE_NR["2025"], "HK$m", OC + ": 7,081 + 2,268."),
    ("dep25", "SoC depreciation, 2025", SOC_DEP["2025"], "HK$m", OC + "."),
    ("plan", "2024 to 2028 Development Plan capital spending", PLAN_CAPEX, "HK$m", "Approved November 2023; CLP presentation of 26 February 2026 and offering circular. 72% transmission and distribution."),
    ("cap24", "SoC capital expenditure, 2024", SOC_CAPEX["2024"], "HK$m", OC.replace(", SoC statements", "") + ": CLP Power 8,010 + CAPCO and other Hong Kong subsidiaries 2,807 + CAPCO's 70% of HKLTL 20."),
    ("cap25", "SoC capital expenditure, 2025", SOC_CAPEX["2025"], "HK$m", OC.replace(", SoC statements", "") + ": 7,971 + 2,501 + 99."),
    ("dcshare", "Data centres' share of CLP Power sales, nine months 2026", DC_SALES_SHARE, "%", "Quarterly statement, 12 October 2026: +12.8%."),
    ("CONSENSUS (CROSS-CHECK ONLY)", None, None, None, None),
    ("cons26", "2026 consensus EPS", CONS_EPS26, "HK$", "stockanalysis.com (S&P Global), read 2 November 2026, last updated 17 September 2026. Its 2025 figure (4.32) matches operating earnings after fair value movements."),
    ("cons27", "2027 consensus EPS", CONS_EPS27, "HK$", "stockanalysis.com, as above."),
    ("constp", "Average analyst target", CONS_TP, "HK$", "stockanalysis.com: 9 analysts, low 69.50, high 89.43; targets updated 17 September 2026."),
    ("MY ESTIMATES", None, None, None, None),
    ("depg", "SoC depreciation growth a year", DEP_GROWTH, "%", "MY ASSUMPTION."),
    ("rnet", "Net return after interest and CESF on average net fixed assets, 2026 to 2028", R_NET_E, "%", "MY ASSUMPTION. 2025: 7.11% (derived); 2024: 6.85%. Lower interest costs in 2026."),
    ("cn26", "Chinese Mainland, 2026", NONHK_E["2026"]["cn"], "HK$m", "MY ESTIMATE. 2025: 1,598; H1 2026: 899."),
    ("cn27", "Chinese Mainland, 2027", NONHK_E["2027"]["cn"], "HK$m", "MY ESTIMATE."),
    ("cn28", "Chinese Mainland, 2028", NONHK_E["2028"]["cn"], "HK$m", "MY ESTIMATE."),
    ("au26", "Australia, 2026", NONHK_E["2026"]["au"], "HK$m", "MY ESTIMATE. 2025: 85; H1 2026: 223; H2 weaker on wholesale prices (Q3 statement)."),
    ("au27", "Australia, 2027", NONHK_E["2027"]["au"], "HK$m", "MY ESTIMATE."),
    ("au28", "Australia, 2028", NONHK_E["2028"]["au"], "HK$m", "MY ESTIMATE. Yallourn retires in 2028."),
    ("in26", "India, 2026", NONHK_E["2026"]["ind"], "HK$m", "MY ESTIMATE. 2025: 221; H1 2026: 105; Jhajjar sold."),
    ("in27", "India, 2027", NONHK_E["2027"]["ind"], "HK$m", "MY ESTIMATE."),
    ("in28", "India, 2028", NONHK_E["2028"]["ind"], "HK$m", "MY ESTIMATE."),
    ("tw26", "Taiwan Region and SE Asia, 2026", NONHK_E["2026"]["tw"], "HK$m", "MY ESTIMATE. 2025: 179; H1 2026: 71."),
    ("tw27", "Taiwan Region and SE Asia, 2027", NONHK_E["2027"]["tw"], "HK$m", "MY ESTIMATE."),
    ("tw28", "Taiwan Region and SE Asia, 2028", NONHK_E["2028"]["tw"], "HK$m", "MY ESTIMATE."),
    ("co26", "Group costs and other, 2026", CORP_E["2026"], "HK$m", "MY ESTIMATE. 2025: -942; H1 2026: -395."),
    ("co27", "Group costs and other, 2027", CORP_E["2027"], "HK$m", "MY ESTIMATE."),
    ("co28", "Group costs and other, 2028", CORP_E["2028"], "HK$m", "MY ESTIMATE."),
    ("mhk", "Multiple, Hong Kong earnings", M_HK, "x", "MY ASSUMPTION. HK Electric Investments 16.3x forward (stockanalysis.com)."),
    ("movs", "Multiple, overseas earnings", M_OVS, "x", "MY ASSUMPTION. No clean listed peer (Power Assets and CKI multiples carry UK Power Networks sale gains). Overseas earnings fell 31% in 2025. At 14x the base value is shown on the Valuation tab."),
    ("mcorp", "Multiple, Group costs and other", M_CORP, "x", "MY ASSUMPTION. Close to the Group multiple."),
]
MINE = {"depg", "rnet", "mhk", "movs", "mcorp"} | {f"{a}{y}" for a in ["cn", "au", "in", "tw", "co"] for y in ["26", "27", "28"]}
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY)
        r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = (PCT2 if key == "rnet" else PCT1) if unit == "%" else (MULT0 if unit == "x" else (HKD2 if unit == "HK$" else (M1 if unit == "m" else M0)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  SOC
ws = sheet("SoC", "SCHEME OF CONTROL: ASSET BASE AND HONG KONG EARNINGS (HK$ MILLION)", [62, 14, 14, 14, 14, 14, 14])
head(ws, 4, ["HK$ million", "2023", "2024", "2025", "2026E", "2027E", "2028E"])
labs = ["Permitted return (reported)", "Implied average net fixed assets", "Capital spending (HK segment additions; 2026E+ rest of plan)",
        "SoC depreciation", "Net return after CESF (reported) / rate (mine)", "Net return after CESF as % of assets",
        "CLP share of net return", "CLP's share of net return, HK$m", "Other Hong Kong energy and related earnings",
        "HONG KONG ENERGY AND RELATED EARNINGS", "Growth"]
for i, lab in enumerate(labs):
    ws.cell(row=5 + i, column=1, value=lab).font = F_B if i in (1, 9) else Font()
put(ws, "B5", L("pr23"), M0); put(ws, "C5", L("pr24"), M0); put(ws, "D5", L("pr25"), M0)
for col in "BCD":
    put(ws, f"{col}6", f"={col}5/{A['prate']}", M0)
put(ws, "C7", L("cap24"), M0); put(ws, "D7", L("cap25"), M0)
for col in "EFG":
    put(ws, f"{col}7", f"=({A['plan']}-{A['cap24']}-{A['cap25']})/3", M0)
put(ws, "D8", L("dep25"), M0)
for col, prev in [("E", "D"), ("F", "E"), ("G", "F")]:
    put(ws, f"{col}8", f"={prev}8*(1+{A['depg']})", M0)
    put(ws, f"{col}6", f"={prev}6+{col}7-{col}8", M0, F_B, FILL_KEY)
put(ws, "C9", L("nr24"), M0); put(ws, "D9", L("nr25"), M0)
put(ws, "C10", "=C9/C6", PCT2); put(ws, "D10", "=D9/D6", PCT2)
for col in "EFG":
    put(ws, f"{col}10", L("rnet"), PCT2)
put(ws, "D11", f"={A['clp25']}/{A['nr25']}", PCT1)
for col in "EFG":
    put(ws, f"{col}11", "=$D$11", PCT1)
put(ws, "D12", L("clp25"), M0)
for col in "EFG":
    put(ws, f"{col}12", f"={col}6*{col}10*{col}11", M0)
put(ws, "D13", f"={A['hk25']}-D12", M0)
for col in "EFG":
    put(ws, f"{col}13", "=$D$13", M0)
put(ws, "C14", L("hk24"), M0); put(ws, "D14", L("hk25"), M0)
for col in "EFG":
    put(ws, f"{col}14", f"={col}12+{col}13", M0, F_B, FILL_KEY)
for col, prev in [("D", "C"), ("E", "D"), ("F", "E"), ("G", "F")]:
    put(ws, f"{col}15", f"={col}14/{prev}14-1", PCT1)
ws["A17"] = "Average net fixed assets, growth a year 2025 to 2028E"; put(ws, "B17", "=(G6/D6)^(1/3)-1", PCT1)
ws["A18"] = "CLP earnings a year per HK$1bn of extra average net fixed assets, HK$m"; put(ws, "B18", "=1000*G10*G11", '#,##0.00')
ws["A19"] = "Per share, HK$"; put(ws, "B19", f"=B18/{A['shares']}", M3)
ws["A20"] = "Value per share per HK$1bn, at the Hong Kong multiple, HK$"; put(ws, "B20", f"=B19*{A['mhk']}", M3)
ws["A21"] = "Extra 2028 assets needed for a base value 15% above the price, HK$bn"; put(ws, "B21", f"=({A['price']}*1.15-Valuation!B9)/B20", M1)
ws["A22"] = "As a share of the whole Development Plan"; put(ws, "B22", f"=B21*1000/{A['plan']}", PCT0)
ws["A23"] = "Illustration: assets in proportion to data centres' share of sales, HK$bn"; put(ws, "B23", f"=D6*{A['dcshare']}/1000", M1)
ws["A24"] = "Illustration: earnings per share on those assets, HK$"; put(ws, "B24", "=B23*B19", M3)
ws["A25"] = "Illustration: share of my 2028E EPS"; put(ws, "B25", "=B24/Earnings!F14", PCT1)
note(ws, 27, [
    "Permitted return = 8% of average net fixed assets (SoC). Net return = permitted return less interest on borrowed capital (up to 7%; 1,488 in 2025), interest on the increase in customers' deposits (11) and the TSF charge (85), plus performance incentives (526); CESF = 65% of energy efficiency incentives (242).",
    "Sales above the permitted return go to the Tariff Stabilisation Fund; a shortfall is drawn from it only up to its balance (SCA clause 5(2)). Volume does not move profit directly.",
    "2026E to 2028E: average net fixed assets roll forward by capital spending less depreciation, a simplification (2025 backtest: 145.7bn against 145.3bn implied).",
    "CLP does not disclose the capital cost of its data centre substations; rows 23 to 25 are an illustration only.",
])

# =====================================================================  EARNINGS
ws = sheet("Earnings", "GROUP OPERATING EARNINGS BEFORE FAIR VALUE MOVEMENTS (HK$ MILLION)", [56, 13, 13, 13, 13, 13])
head(ws, 4, ["HK$ million", "2024A", "2025A", "2026E", "2027E", "2028E"])
labs = ["Hong Kong energy and related", "Chinese Mainland", "Australia", "India", "Taiwan Region and SE Asia",
        "Overseas subtotal", "Group costs and other", "OPERATING EARNINGS BEFORE FAIR VALUE MOVEMENTS", "Growth", "EPS, HK$",
        "Consensus EPS, HK$", "Mine against consensus", "Hong Kong share of segment earnings"]
for i, lab in enumerate(labs):
    ws.cell(row=5 + i, column=1, value=lab).font = F_B if i in (7, 9) else Font()
put(ws, "B5", L("hk24"), M0); put(ws, "C5", L("hk25"), M0)
for col, sc in zip("DEF", "EFG"):
    put(ws, f"{col}5", f"=SoC!{sc}14", M0)
for row, k in [(6, "cn"), (7, "au"), (8, "in"), (9, "tw")]:
    for col, y in zip("DEF", ["26", "27", "28"]):
        put(ws, f"{col}{row}", L(f"{k}{y}"), M0)
put(ws, "B6", 1851.0, M0, F_IN); put(ws, "B7", 591.0, M0, F_IN); put(ws, "B8", 329.0, M0, F_IN); put(ws, "B9", 260.0, M0, F_IN)
put(ws, "C6", 1598.0, M0, F_IN); put(ws, "C7", 85.0, M0, F_IN); put(ws, "C8", 221.0, M0, F_IN); put(ws, "C9", 179.0, M0, F_IN)
for col in "BCDEF":
    put(ws, f"{col}10", f"=SUM({col}6:{col}9)", M0)
put(ws, "B11", -58.0 + 45.0 - 964.0, M0, F_IN); put(ws, "C11", L("corp25"), M0)
for col, y in zip("DEF", ["26", "27", "28"]):
    put(ws, f"{col}11", L(f"co{y}"), M0)
for col in "BCDEF":
    put(ws, f"{col}12", f"={col}5+{col}10+{col}11", M0, F_B, FILL_KEY)
for col, prev in [("C", "B"), ("D", "C"), ("E", "D"), ("F", "E")]:
    put(ws, f"{col}13", f"={col}12/{prev}12-1", PCT1)
for col in "BCDEF":
    put(ws, f"{col}14", f"={col}12/{A['shares']}", HKD2, F_B)
put(ws, "D15", L("cons26"), HKD2); put(ws, "E15", L("cons27"), HKD2)
put(ws, "D16", "=D14/D15-1", PCT1); put(ws, "E16", "=E14/E15-1", PCT1)
for col in "BCDEF":
    put(ws, f"{col}17", f"={col}5/({col}5+{col}10)", PCT1)
ws["A19"] = "Check: 2024 and 2025 sum to reported operating earnings"; put(ws, "B19", f"=B12-{A['ope24']}", M0); put(ws, "C19", f"=C12-{A['ope25']}", M0)
ws["A20"] = "Implied second half 2026, HK$m"; put(ws, "D20", f"=D12-{A['ope_h126']}", M0)
ws["A21"] = "Second half 2025, HK$m"; put(ws, "D21", f"={A['ope25']}-{A['ope_h125']}", M0)
ws["A22"] = "Consensus 2027 against my 2027E"; put(ws, "B22", "=E15/E14-1", PCT1)
note(ws, 24, ["2024A and 2025A segment figures from the 2025 annual results announcement. 2026E to 2028E are my estimates; Hong Kong links to the SoC tab."])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: SUM OF THE PARTS ON 2028E, TWELVE MONTHS OUT", [64, 16, 16, 16, 60])
head(ws, 4, ["Part", "2028E earnings", "Multiple", "Value, HK$m", "Note"])
parts = [(5, "Hong Kong energy and related", "=Earnings!F5", "mhk"), (6, "Overseas", "=Earnings!F10", "movs"), (7, "Group costs and other", "=Earnings!F11", "mcorp")]
for rr, lab, f, mk in parts:
    ws.cell(row=rr, column=1, value=lab)
    put(ws, f"B{rr}", f, M0); put(ws, f"C{rr}", L(mk), MULT0); put(ws, f"D{rr}", f"=B{rr}*C{rr}", M0)
ws["A8"] = "EQUITY VALUE, HK$m"; ws["A8"].font = F_B; put(ws, "D8", "=SUM(D5:D7)", M0, F_B, FILL_KEY)
vrows = [
    (9, "BASE VALUE PER SHARE, HK$", f"=D8/{A['shares']}", HKD2, ""),
    (10, "Reference price, HK$", L("price"), HKD2, "HKEX close, 2 November 2026."),
    (11, "Base value against price", "=B9/B10-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (12, "VIEW ON THE BAND", '=IF(B11>=0.15,"LONG",IF(B11<=-0.25,"SHORT","NO CALL"))', None, "Tommy Lau's call, 2 November 2026: NO CALL, Medium conviction."),
    (13, "Target, HK$", CALL["target"] or "None (no call)", HKD2, "None for a no call."),
    (14, "Implied multiple of 2028E Group EPS", "=B9/Earnings!F14", MULTF, ""),
    (16, "Market value, HK$bn", f"={A['shares']}*B10/1000", M1, ""),
    (17, "Net debt, HK$m, 30 June 2026", f"={A['debt']}-{A['cash']}", M0, "Excludes perpetual securities."),
    (18, "Enterprise value incl. perpetuals, HK$bn", f"=B16+(B17+{A['perps']})/1000", M1, ""),
    (19, "P/E on trailing operating earnings (H2 2025 + H1 2026)", f"=B10/(({A['ope25']}-{A['ope_h125']}+{A['ope_h126']})/{A['shares']})", MULTF, ""),
    (20, "P/E on 2026E", "=B10/Earnings!D14", MULTF, ""),
    (21, "P/E on 2027E", "=B10/Earnings!E14", MULTF, ""),
    (22, "P/E on 2027 consensus", f"=B10/{A['cons27']}", MULTF, ""),
    (23, "P/E on 2028E", "=B10/Earnings!F14", MULTF, ""),
    (24, "Hong Kong multiple implied by the price (other parts at my multiples)", "=(B10*" + A['shares'] + "-D6-D7)/B5", MULTF, ""),
    (25, "Price below which the base value is 15% or more above it, HK$", "=B9/1.15", HKD2, "Revisit level for a long."),
    (26, "Price above which the base value is 25% or more below it, HK$", "=B9/0.75", HKD2, "Revisit level for a short."),
    (27, "Dividend yield on 2025 dividends", f"={A['dps25']}/B10", PCT2, ""),
    (28, "Price change in 2026 to date", f"=B10/{A['pxdec']}-1", PCT1, ""),
    (29, "Price against the highest close of the past year", f"=B10/{A['hiclose']}-1", PCT1, ""),
    (30, "Average analyst target against price", f"={A['constp']}/B10-1", PCT1, "Cross-check only."),
    (31, "Base value with overseas at 14x (alternative), HK$", f"=(D5+B6*14+D7)/{A['shares']}", HKD2, "Still NO CALL on the band."),
    (32, "Alternative against price", "=B31/B10-1", PCT1, ""),
]
for rr, lab, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    if rr in (9, 12):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    elif isinstance(f, str) and f.startswith(("=Assumptions", "=Earnings")): c.font = F_LINK
    elif rr == 13: c.font = F_INB; c.fill = FILL_ASSUME
    ws.cell(row=rr, column=5, value=nt).alignment = WRAP

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (SUM OF THE PARTS ON 2028E)", [10, 14, 12, 14, 11, 11, 11, 14, 12, 14, 12])
head(ws, 4, ["Case", "Extra assets, HK$bn", "Net return", "Overseas, HK$m", "HK mult", "Overseas mult", "Costs mult",
             "HK earnings", "2028 EPS", "Value, HK$", "vs price"])
for i, s in enumerate(SCEN):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    if s[0] == "Base":
        vals = [0.0, "=" + A["rnet"], "=Earnings!F10", "=" + A["mhk"], "=" + A["movs"], "=" + A["mcorp"]]
    else:
        vals = list(s[1:7])
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v)
        if isinstance(v, str): c.font = F_LINK
        else: c.font = F_INB; c.fill = FILL_ASSUME
        c.number_format = [M1, PCT2, M0, MULT0, MULT0, MULT0][j]
    ws.cell(row=rr, column=8, value=f"=(SoC!$G$6+B{rr}*1000)*C{rr}*SoC!$G$11+SoC!$G$13").number_format = M0
    ws.cell(row=rr, column=9, value=f"=(H{rr}+D{rr}+Earnings!$F$11)/{A['shares']}").number_format = HKD2
    ws.cell(row=rr, column=10, value=f"=(H{rr}*E{rr}+D{rr}*F{rr}+Earnings!$F$11*G{rr})/{A['shares']}").number_format = HKD2
    ws.cell(row=rr, column=11, value=f"=J{rr}/{A['price']}-1").number_format = PCT1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[7]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, HK$"; ws["A11"].font = F_B
ws["J11"] = "=B9*J5+C9*J6+D9*J7"; ws["J11"].number_format = HKD2; ws["J11"].font = F_B; ws["J11"].fill = FILL_KEY
ws["K11"] = f"=J11/{A['price']}-1"; ws["K11"].number_format = PCT1
ws["A12"] = "Check: base case equals the Valuation tab"; ws["J12"] = "=J6-Valuation!B9"; ws["J12"].number_format = '0.000'
note(ws, 14, [
    "Bear: higher rates cut the net return to 6.95%; EnergyAustralia and Mainland tariffs weaker, overseas HK$1.9bn; 15x, 8x, 13x.",
    "Base: the approved Development Plan; my estimates.",
    "Bull: HK$5bn of assets added to the plan for the Northern Metropolis and Sandy Ridge; net return 7.35%; overseas HK$2.6bn; 20x, 11x, 18x.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: EXTRA 2028 REGULATED ASSETS AGAINST THE HONG KONG MULTIPLE (HK$)", [30, 14, 14, 14])
head(ws, 4, ["Extra assets, HK$bn \\ HK multiple", "", "", ""])
for j, (mm, link) in enumerate(zip(SENS_MULT, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["mhk"]) if link else mm)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, a in enumerate(SENS_ANFA):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=a); c.number_format = M1; c.font = F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j,
                value=f"=((Earnings!$F$5+$A{rr}*SoC!$B$18)*{col}$4+Valuation!$D$6+Valuation!$D$7)/{A['shares']}").number_format = HKD2
ws["C5"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
ws["A11"] = "Cells 25% or more below the price"; ws["A11"].font = F_B
ws["B11"] = f'=COUNTIF(B5:D7,"<="&{A["price"]}*0.75)'; ws["C11"] = "of 9"
note(ws, 13, ["The middle column links to the base Hong Kong multiple. Overseas and Group costs at my base multiples in every cell."])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, 2 NOVEMBER 2026)", [26, 10, 13, 13, 11, 80])
head(ws, 4, ["Company", "HKEX", "Forward P/E", "Trailing P/E", "Yield", "What they run"])
for i, (co, tk, pe, tpe, y, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, v in enumerate([pe, tpe]):
        c = ws.cell(row=rr, column=3 + j, value=v); c.number_format = MULTF; c.font = F_IN
    c = ws.cell(row=rr, column=5, value=y); c.number_format = PCT2; c.font = F_IN
    ws.cell(row=rr, column=6, value=what).alignment = WRAP
last = 4 + len(PEERS)
ws[f"A{last + 2}"] = "Peer median: forward P/E excludes Power Assets and CKI (distorted); yield all four"; ws[f"A{last + 2}"].font = F_B
ws[f"C{last + 2}"] = "=MEDIAN(C6,C8)"; ws[f"C{last + 2}"].number_format = MULTF
ws[f"E{last + 2}"] = f"=MEDIAN(E6:E{last})"; ws[f"E{last + 2}"].number_format = PCT2
note(ws, last + 4, ["Multiples only, to set the range. No view on the peers' shares is expressed. Power Assets' H1 2026 profit of HK$14.7bn included a gain of about HK$11.3bn on the UK Power Networks sale (completed May 2026); CKI's multiples carry the same sale, about 21x the 2027 consensus of HK$3.29."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 150])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "CLP Holdings annual results announcement 2025, 26 February 2026 (HKEX 2026022600152): segment operating earnings, dividends, segment capital additions, data centre sales and substations, shares in issue.",
    "CLP Holdings 2025 results presentation, 26 February 2026 (HKEX 2026022600162): SoC capex HK$10.6bn, Development Plan HK$52.9bn (72% T&D), six data centres energised and 12 more substations planned by 2028.",
    "CLP Holdings interim results 2026, 6 August 2026 (HKEX 2026080600235): half-year segment earnings, borrowings and cash, data centre sales, two substations of 260 MVA, eight in the plan period.",
    "CLP Holdings quarterly statement January to September 2026, 12 October 2026 (HKEX 2026101200581): data centre sales +12.8%, 6.6% of 28,131 GWh; Sandy Ridge from mid-2027; tariff +4.8%; third interim dividend.",
    "CLP Power Hong Kong offering circular, US$4.5bn MTN programme, 1 April 2026 (HKEX 2026040100797): Scheme of Control terms, SoC statements 2023 to 2025, CAPCO 70%, SoC to 2033, interim reviews, about HK$38bn of T&D.",
    "CLP Holdings 2023 annual results, 26 February 2024 (HKEX 2024022600164): 'up to 18 large-scale data centres by 2028'.",
    "LegCo Panel on Environmental Affairs, CLP paper on the 2024 to 2028 Development Plan, 28 November 2023; Government release of 28 November 2023 (HK Electric plan HK$22.0bn).",
    "Yahoo Finance 0002.HK monthly history page and stockanalysis.com daily history, read 2 November 2026; stockanalysis.com (S&P Global data) for consensus, targets and peer multiples, read 2 November 2026.",
    "The Physical Layer, 'Hong Kong has the plug: its grid builds to demand, and the chip needs a licence', 2 November 2026: https://thephysicallayer.fyi/journal/hong-kong-has-the-plug/",
    "Estimates for 2026 to 2028 are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Call (Tommy Lau, 2 November 2026)", "=Valuation!B12", None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Base value per share, HK$", "=Valuation!B9", HKD2, "Sum of the parts on 2028E."),
    ("Reference price, HK$", "=" + A["price"], HKD2, "HKEX close, 2 November 2026."),
    ("Base value against price", "=Valuation!B11", PCT1, ""),
    ("Probability-weighted value, HK$", "=Scenarios!J11", HKD2, "25 / 50 / 25 bear / base / bull."),
    ("2028E EPS, HK$", "=Earnings!F14", HKD2, "Operating earnings before fair value movements; my estimate."),
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
ws.row_dimensions[13].height = 44; ws.row_dimensions[14].height = 44
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("SoC", "Scheme of Control asset base, net return and Hong Kong earnings, 2023 to 2028E; what HK$1bn of assets is worth."),
    ("Earnings", "Group operating earnings by segment, 2024A to 2028E."),
    ("Valuation", "Sum of the parts, the band, multiples at the price, revisit levels."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "Extra regulated assets against the Hong Kong multiple."),
    ("Peers", "Forward P/E, trailing P/E and yield."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t)
    ws.cell(row=18 + i, column=2, value=d)
ws["A27"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A27"].font = F_NOTE
ws["A28"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."
ws["A28"].font = F_NOTE

for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
