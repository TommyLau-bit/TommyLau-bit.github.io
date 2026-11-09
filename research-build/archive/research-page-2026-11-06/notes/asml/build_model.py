"""ASML initiation model, 7 Oct 2026. Live formulas throughout.

House style follows the Vertiv, Broadcom and Schneider models: navy header rows, blue font for hardcoded inputs, yellow fill
on my own assumptions, green font for cross-sheet links, black for formulas. EUR million unless stated; per-share in EUR.
Revenue is built by segment: low NA EUV (units x price), High NA EUV, DUV and metrology systems, Installed Base Management.
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

EUR2 = '"EUR "#,##0.00'; EUR0 = '"EUR "#,##0'; M0 = '#,##0'; M1 = '#,##0.0'; N2 = '#,##0.00'
PCT1 = '0.0%'; PCT0 = '0%'; XMULT = '0.0"x"'; MULT0 = '0"x"'
SUB = f"Tommy Lau | ASML Holding N.V. (Euronext Amsterdam: ASML; Nasdaq: ASML) | {DATE_LONG} | EUR million unless stated | Personal research, not investment advice."

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


sheet("Cover", "ASML HOLDING N.V. (EURONEXT AMSTERDAM: ASML)  INITIATION MODEL", [44, 26, 90])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [64, 14, 10, 100])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "another tab. Black = formula. EUR million unless stated; per-share figures in EUR; shares in millions.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"euvg26", "ibmg26", "hna26", "hna27", "hna28", "hnaasp", "lna28", "aspg27", "aspg28", "noneuvg27", "noneuvg28",
        "ibmg27", "ibmg28", "gm26", "gm27", "gm28", "rd26", "rd27", "rd28", "sga26", "sga27", "sga28", "int26", "int27", "int28",
        "eqm26", "eqm27", "eqm28", "sh26", "sh27", "sh28", "mult", "coe", "fcfconv", "g29", "g30", "g31", "g32", "tg"}
rows = [
    ("MARKET (retrieved 7 October 2026)", None, None, None, None),
    ("price", "Share price (Euronext Amsterdam: ASML)", PRICE, "EUR", "Euronext Amsterdam close, 6 October 2026."),
    ("adr", "ADR price (Nasdaq: ASML)", ADR_PRICE, "US$", "Nasdaq close, 6 October 2026 (stockanalysis.com)."),
    ("eurusd", "EUR/USD", EURUSD, "rate", "ECB euro reference rate, 6 October 2026."),
    ("eurjpy", "EUR/JPY", EURJPY, "rate", "ECB euro reference rate, 6 October 2026."),
    ("hiclose", "Highest close of the past year (30 June 2026)", HI_CLOSE, "EUR", "Euronext; intraday high EUR 1,741.00 the same day."),
    ("loclose", "Lowest close of the past year (10 October 2025)", LO_CLOSE, "EUR", "Euronext; intraday low EUR 812.60 on 8 October 2025."),
    ("pxdec24", "Close, 31 December 2024", PRICE_DEC24, "EUR", "Euronext."),
    ("pxdec25", "Close, 31 December 2025", PRICE_DEC25, "EUR", "Euronext."),
    ("shout", "Shares outstanding", SHARES_OUT, "m", "stockanalysis.com, 7 October 2026."),
    ("cons26sa", "2026 consensus EPS (EUR)", CONS_EPS_26_SA, "EUR", "stockanalysis.com (S&P Global), average of 31 EPS estimates, updated 6 October 2026."),
    ("consusd26", "2026 consensus EPS for the ADR (US$)", CONS_EPS_USD[0], "US$", "Zacks, 7 estimates, retrieved 7 October 2026."),
    ("consusd27", "2027 consensus EPS for the ADR (US$)", CONS_EPS_USD[1], "US$", "Zacks, 7 estimates, retrieved 7 October 2026."),
    ("tpusd", "Average analyst target for the ADR (US$)", CONS_TP_USD, "US$", "stockanalysis.com, 42 analysts, 6 October 2026."),
    ("REPORTED (20-F 2025; Q2 2026 6-K)", None, None, None, None),
    ("cash", "Cash, cash equivalents and short-term investments, 28 June 2026", H1["cash"], "EUR m", "Q2 2026 balance sheet."),
    ("ltdebt", "Long-term debt, 28 June 2026", H1["ltdebt"], "EUR m", "Q2 2026 balance sheet."),
    ("backlog", "Backlog, 31 December 2025", BACKLOG_25, "EUR m", "Q4 2025 release; ASML stopped reporting bookings after Q4 2025."),
    ("top4", "Four customers above 10% each, share of 2025 total net sales", TOP4_25[1], "%", "20-F 2025: EUR 20.0bn, 61.2%. Customers not named."),
    ("hnaasp25", "High NA (EXE) sales per system, 2025", EXE_ASP_25, "EUR m", "20-F 2025: EUR 1,156.9m for 4 systems."),
    ("GUIDED (Q2 2026 release and call, 15 July 2026)", None, None, None, None),
    ("revlo", "2026 total net sales guide, low", G26["rev_lo"], "EUR m", "EUR 43bn to 45bn."),
    ("revhi", "2026 total net sales guide, high", G26["rev_hi"], "EUR m", ""),
    ("noneuvg26", "2026 non-EUV system sales growth", NONEUV_G26, "%", "Call: around 25%."),
    ("lna26", "Low NA EUV systems shipped, 2026", LNA_U[0], "units", "Call: around 65, equal to 2026 capacity."),
    ("lna27", "Low NA EUV systems, 2027 (planned capacity)", LNA_U[1], "units", "Release: add 30% to around 65; call: 2027 close to fully covered with orders."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("euvg26", "2026 EUV system sales growth", EUV_G26, "%", "MINE. Call: over 45%."),
    ("ibmg26", "2026 Installed Base Management growth", IBM_G26, "%", "MINE. Call: over 30%; H1 +28.1%; Q3 guide EUR 2.9bn (+48%)."),
    ("hna26", "High NA systems recognised, 2026", HNA_U[0], "units", "MINE. One in Q2 2026; two in Q4 2025."),
    ("hna27", "High NA systems recognised, 2027", HNA_U[1], "units", "MINE."),
    ("hna28", "High NA systems recognised, 2028 (base)", HNA_U[2], "units", "MINE."),
    ("hnaasp", "High NA sales per system", HNA_ASP, "EUR m", "MINE. 2025: EUR 289m."),
    ("lna28", "Low NA EUV systems, 2028 (base)", LNA_U[2], "units", "MINE. ASML is investigating 110 (another +30%); 'significant number' of 2028 orders."),
    ("aspg27", "Low NA sales per system, change 2027", ASP_G[0], "%", "MINE. CFO: 2027 EUV mix 'more positive' than 2026."),
    ("aspg28", "Low NA sales per system, change 2028 (base)", ASP_G[1], "%", "MINE."),
    ("noneuvg27", "Non-EUV system sales growth, 2027", NONEUV_G[0], "%", "MINE. Immersion capacity +30% for 2027; China falling."),
    ("noneuvg28", "Non-EUV system sales growth, 2028 (base)", NONEUV_G[1], "%", "MINE."),
    ("ibmg27", "Installed Base Management growth, 2027", IBM_G[0], "%", "MINE."),
    ("ibmg28", "Installed Base Management growth, 2028 (base)", IBM_G[1], "%", "MINE."),
    ("gm26", "Gross margin, 2026", GM[0], "%", "MINE. Guide 54% to 56%."),
    ("gm27", "Gross margin, 2027", GM[1], "%", "MINE. Investor Day 2030 range 56% to 60%."),
    ("gm28", "Gross margin, 2028 (base)", GM[2], "%", "MINE."),
    ("rd26", "R&D, 2026", RD[0], "EUR m", "MINE. H1 2,461.5; Q3 guide around 1,200."),
    ("rd27", "R&D, 2027", RD[1], "EUR m", "MINE."),
    ("rd28", "R&D, 2028", RD[2], "EUR m", "MINE."),
    ("sga26", "SG&A, 2026", SGA[0], "EUR m", "MINE. H1 605.0; Q3 guide around 400."),
    ("sga27", "SG&A, 2027", SGA[1], "EUR m", "MINE."),
    ("sga28", "SG&A, 2028", SGA[2], "EUR m", "MINE."),
    ("int26", "Interest and other, 2026", INT[0], "EUR m", "MINE. H1 70.9."),
    ("int27", "Interest and other, 2027", INT[1], "EUR m", "MINE."),
    ("int28", "Interest and other, 2028", INT[2], "EUR m", "MINE."),
    ("eqm26", "Profit from equity method investments, 2026", EQM[0], "EUR m", "MINE. H1 145.7 (mainly Carl Zeiss SMT Holding, 24.9%)."),
    ("eqm27", "Profit from equity method investments, 2027", EQM[1], "EUR m", "MINE."),
    ("eqm28", "Profit from equity method investments, 2028", EQM[2], "EUR m", "MINE."),
    ("tax", "Effective tax rate", TAX, "%", "Guided around 17% for 2026; MINE for 2027 and 2028."),
    ("sh26", "Diluted shares, 2026", SH[0], "m", "MINE. H1 2026: 385.3m."),
    ("sh27", "Diluted shares, 2027", SH[1], "m", "MINE. EUR 12bn buyback over 2026 to 2028."),
    ("sh28", "Diluted shares, 2028", SH[2], "m", "MINE."),
    ("mult", "P/E on 2028E EPS, base", MULT, "x", "MINE. Today 32.2x my 2027E; peers' median 36.1x on the year ending in 2027."),
    ("coe", "Cost of equity (DCF cross-check)", COE, "%", "MINE."),
    ("fcfconv", "Free cash flow / net income", FCF_CONV, "%", "MINE. 2024: 120%; 2025: 115%. Below history, as down payments unwind (H1 2026 free cash flow was negative)."),
    ("fcfconvh", "Free cash flow / net income, 2025 actual (alternative case)", FCF_CONV_HIST, "%", "20-F 2025: free cash flow EUR 11.0bn on net income EUR 9.6bn (115%)."),
    ("g29", "Net income growth, 2029", DCF_G[0], "%", "MINE."),
    ("g30", "Net income growth, 2030", DCF_G[1], "%", "MINE."),
    ("g31", "Net income growth, 2031", DCF_G[2], "%", "MINE."),
    ("g32", "Net income growth, 2032", DCF_G[3], "%", "MINE."),
    ("tg", "Terminal growth from 2033", TG, "%", "MINE."),
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
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else (N2 if unit in ("EUR", "US$") else ('0.0000' if unit == "rate" else M1)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1

# ===================================================================== QUARTERLY
ws = sheet("Quarterly", "QUARTERS: SYSTEMS, INSTALLED BASE MANAGEMENT AND MARGIN, Q2 2025 TO Q3 2026 GUIDE", [56] + [12] * 6)
head(ws, 4, ["EUR million unless stated"] + QL)
for j in range(6):
    put(ws, 5, 2 + j, Q_SYS[j] if Q_SYS[j] is not None else f"={get_column_letter(2 + j)}7-{get_column_letter(2 + j)}6", M0)
    put(ws, 6, 2 + j, Q_IBM[j], M0)
    put(ws, 7, 2 + j, Q_REV[j] if j == 5 else f"={get_column_letter(2 + j)}5+{get_column_letter(2 + j)}6", M0)
    put(ws, 8, 2 + j, Q_GM[j], PCT1)
    put(ws, 9, 2 + j, f"={get_column_letter(2 + j)}6/{get_column_letter(2 + j)}7", PCT1)
for rr, lab in [(5, "Net system sales"), (6, "Installed Base Management"), (7, "Total net sales"), (8, "Gross margin"), (9, "IBM share of total net sales")]:
    ws.cell(row=rr, column=1, value=lab)
ws["A11"] = "Checks"; ws["A11"].font = Font(bold=True, color=NAVY)
qchk = [
    (12, "IBM growth, H1 2026 on H1 2025", f"=(E6+F6)/{H1['ibm_h125']}-1", PCT1),
    (13, "EUV system sales, Q1 2026 (66% of system sales)", f"={Q_EUV_SHARE['Q1 26']}*E5", M0),
    (14, "EUV system sales, Q2 2026 (call)", Q_EUV_Q226, M0),
    (15, "IBM growth, Q3 2026 guide on Q3 2025", "=G6/C6-1", PCT1),
    (16, "H1 2026 total net sales", "=E7+F7", M0),
]
for rr, lab, f, fmt in qchk:
    ws.cell(row=rr, column=1, value=lab); put(ws, rr, 2, f, fmt)
note(ws, 18, ["Source: ASML Q2 2026 US GAAP statements and presentation (Form 6-K, 15 July 2026). Q3 2026 guide: total net sales EUR 11.0bn to 12.0bn (midpoint used), IBM around EUR 2.9bn, gross margin 55% to 57%.",
              "Q1 2026 and Q2 2026 EUV shares of system sales (66% and 57%) and China shares (19% and 14% of system sales) from the presentation."])

# ===================================================================== SEGMENTS
ws = sheet("Segments", "REVENUE BY SEGMENT: LOW NA EUV, HIGH NA EUV, DUV AND METROLOGY, INSTALLED BASE MANAGEMENT", [52, 12, 12, 12, 12, 12, 12])
head(ws, 4, ["EUR million unless stated", "2023A", "2024A", "2025A", "2026E*", "2027E*", "2028E*"])
seg = [
    (5, "Low NA EUV systems recognised / shipped, units", NXE_U + ["=" + A["lna26"], "=" + A["lna27"], "=" + A["lna28"]], M0),
    (6, "Low NA sales per system, EUR m", ["=B7/B5", "=C7/C5", "=D7/D5", "=E7/E5", f"=E6*(1+{A['aspg27']})", f"=F6*(1+{A['aspg28']})"], M1),
    (7, "Low NA EUV system sales", NXE_H + ["=E10-E9", "=F5*F6", "=G5*G6"], M0),
    (8, "High NA EUV systems, units", EXE_U + ["=" + A["hna26"], "=" + A["hna27"], "=" + A["hna28"]], M0),
    (9, "High NA EUV system sales", EXE_H + [f"=E8*{A['hnaasp']}", f"=F8*{A['hnaasp']}", f"=G8*{A['hnaasp']}"], M0),
    (10, "EUV system sales", ["=B7+B9", "=C7+C9", "=D7+D9", f"=D10*(1+{A['euvg26']})", "=F7+F9", "=G7+G9"], M0),
    (11, "EUV growth", [None, "=C10/B10-1", "=D10/C10-1", "=E10/D10-1", "=F10/E10-1", "=G10/F10-1"], PCT1),
    (12, "DUV and metrology system sales (non-EUV)", NONEUV_H + [f"=D12*(1+{A['noneuvg26']})", f"=E12*(1+{A['noneuvg27']})", f"=F12*(1+{A['noneuvg28']})"], M0),
    (13, "Net system sales", ["=B10+B12", "=C10+C12", "=D10+D12", "=E10+E12", "=F10+F12", "=G10+G12"], M0),
    (14, "Installed Base Management", IBM_H + [f"=D14*(1+{A['ibmg26']})", f"=E14*(1+{A['ibmg27']})", f"=F14*(1+{A['ibmg28']})"], M0),
    (15, "Total net sales", ["=B13+B14", "=C13+C14", "=D13+D14", "=E13+E14", "=F13+F14", "=G13+G14"], M0),
    (16, "IBM share of total net sales", ["=B14/B15", "=C14/C15", "=D14/D15", "=E14/E15", "=F14/F15", "=G14/G15"], PCT1),
    (17, "EUV share of net system sales", ["=B10/B13", "=C10/C13", "=D10/D13", "=E10/E13", "=F10/F13", "=G10/G13"], PCT1),
    (18, "Total net sales to China", CHINA_H + [None, None, None], M0),
    (19, "China share of total net sales", ["=B18/B15", "=C18/C15", "=D18/D15", G26["china"], None, None], PCT1),
    (20, "Gross margin, systems", [None, (SYS_H[1] - COST_SYS_H[1]) / SYS_H[1], (SYS_H[2] - COST_SYS_H[2]) / SYS_H[2], None, None, None], PCT1),
    (21, "Gross margin, Installed Base Management", [None, IBM_GM_H[1], IBM_GM_H[2], None, None, None], PCT1),
]
for rr, label, vals, fmt in seg:
    ws.cell(row=rr, column=1, value=label).font = F_B if rr in (10, 13, 15) else Font()
    for j, v in enumerate(vals):
        put(ws, rr, 2 + j, v, fmt)
ws["D20"] = f"=({SYS_H[2]}-{COST_SYS_H[2]})/{SYS_H[2]}"; ws["C20"] = f"=({SYS_H[1]}-{COST_SYS_H[1]})/{SYS_H[1]}"
ws["D21"] = f"=({IBM_H[2]}-{COST_SVC_H[2]})/{IBM_H[2]}"; ws["C21"] = f"=({IBM_H[1]}-{COST_SVC_H[1]})/{IBM_H[1]}"
for c in ("C20", "D20", "C21", "D21"):
    ws[c].number_format = PCT1; ws[c].alignment = RIGHT
note(ws, 23, [
    "*2026E to 2028E are my estimates. History from the 20-F 2025 (net system sales per technology, total net sales by region, cost of system and of service sales).",
    "2026E EUV sales follow the CFO's 'over 45%' growth; the low NA figure is EUV less my High NA. 2026 China share is ASML's 'around 20%' of total net sales.",
    "Units are systems recognised in sales for 2023 to 2025 and shipments (equal to capacity) for 2026 and 2027; recognition can lag shipment.",
])

# ===================================================================== FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (EUR million unless stated, US GAAP)", [52, 12, 12, 12, 12, 12, 12])
head(ws, 4, ["", "2024A", "2025A", "H1 2026A", "2026E*", "2027E*", "2028E*"])
fin = [
    (5, "Total net sales", [REV_H[1], REV_H[2], H1["rev"], "=Segments!E15", "=Segments!F15", "=Segments!G15"], M0, True),
    (6, "Growth", [None, "=C5/B5-1", f"=D5/{H1['ibm_h125'] + 11336.5}-1", "=E5/C5-1", "=F5/E5-1", "=G5/F5-1"], PCT1, False),
    (7, "Gross margin", ["=B8/B5", "=C8/C5", "=D8/D5", "=" + A["gm26"], "=" + A["gm27"], "=" + A["gm28"]], PCT1, False),
    (8, "Gross profit", [GP_H[1], GP_H[2], H1["gp"], "=E5*E7", "=F5*F7", "=G5*G7"], M0, True),
    (9, "R&D", [-RD_H[1], -RD_H[2], -H1["rd"], "=-" + A["rd26"], "=-" + A["rd27"], "=-" + A["rd28"]], M0, False),
    (10, "SG&A", [-SGA_H[1], -SGA_H[2], -H1["sga"], "=-" + A["sga26"], "=-" + A["sga27"], "=-" + A["sga28"]], M0, False),
    (11, "Income from operations", ["=B8+B9+B10", "=C8+C9+C10", "=D8+D9+D10", "=E8+E9+E10", "=F8+F9+F10", "=G8+G9+G10"], M0, True),
    (12, "Operating margin", ["=B11/B5", "=C11/C5", "=D11/D5", "=E11/E5", "=F11/F5", "=G11/G5"], PCT1, False),
    (13, "Interest and other", [19.8, 104.7, H1["int"], "=" + A["int26"], "=" + A["int27"], "=" + A["int28"]], M0, False),
    (14, "Income tax", [-1680.6, -2013.4, -1156.2, f"=-(E11+E13)*{A['tax']}", f"=-(F11+F13)*{A['tax']}", f"=-(G11+G13)*{A['tax']}"], M0, False),
    (15, "Profit from equity method investments", [209.8, 216.7, H1["eqm"], "=" + A["eqm26"], "=" + A["eqm27"], "=" + A["eqm28"]], M0, False),
    (16, "Net income", ["=B11+B13+B14+B15", "=C11+C13+C14+C15", "=D11+D13+D14+D15", "=E11+E13+E14+E15", "=F11+F13+F14+F15", "=G11+G13+G14+G15"], M0, True),
    (17, "Diluted shares, m", [SH_DIL_H[1], SH_DIL_H[2], H1["sh_dil"], "=" + A["sh26"], "=" + A["sh27"], "=" + A["sh28"]], M1, False),
    (18, "Diluted EPS, EUR", [EPS_DIL_H[1], EPS_DIL_H[2], 14.73, "=E16/E17", "=F16/F17", "=G16/G17"], N2, True),
    (19, "EPS growth", [None, "=C18/B18-1", None, "=E18/C18-1", "=F18/E18-1", "=G18/F18-1"], PCT1, False),
    (20, "P/E at reference price", ["=" + A["price"] + "/B18", "=" + A["price"] + "/C18", None, "=" + A["price"] + "/E18", "=" + A["price"] + "/F18", "=" + A["price"] + "/G18"], XMULT, False),
    (21, "Consensus EPS, EUR (Zacks ADR, converted)", [None, None, None, f"={A['consusd26']}/{A['eurusd']}", f"={A['consusd27']}/{A['eurusd']}", None], N2, False),
    (22, "Mine against consensus", [None, None, None, "=E18/E21-1", "=F18/F21-1", None], PCT1, False),
    (23, "P/E on consensus", [None, None, None, "=" + A["price"] + "/E21", "=" + A["price"] + "/F21", None], XMULT, False),
    (24, "Free cash flow (operating cash flow less capex and intangibles)", [FCF_H[1], FCF_H[2], H1["ocf"] - H1["capex"] - H1["intang"], None, None, None], M0, False),
]
for rr, label, vals, fmt, bold in fin:
    ws.cell(row=rr, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        put(ws, rr, 2 + j, v, fmt)
note(ws, 26, [
    "*2026E to 2028E are my estimates. 2024, 2025 and H1 2026 as reported (20-F 2025; Q2 2026 statements). H1 2025 total net sales EUR 15,433.2m.",
    "Consensus: Zacks ADR EPS in US$ converted at the ECB rate of 6 October 2026; stockanalysis.com (S&P Global) has EUR 38.35 for 2026. 2028 consensus not verified.",
    "H1 2026 free cash flow was negative as customer down payments received in Q4 2025 (operating cash flow EUR 11.4bn that quarter) were worked through.",
])

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (P/E ON 2028E EPS)", [20] + [12] * 18)
hd = ["Case", "Low NA units 28", "Price step 28", "High NA units 28", "Non-EUV growth 28", "IBM growth 28", "Gross margin 28", "P/E",
      "Low NA sales 28", "High NA sales 28", "Non-EUV sales 28", "IBM 28", "Total net sales 28", "Gross profit 28", "Op. income 28",
      "Net income 28", "EPS 28", "Value, EUR", "vs price"]
head(ws, 4, hd)
SROWS = SCEN + [("Price-implied", NEED_UNITS, ASP_G[1], HNA_U[2], NONEUV_G[1], IBM_G[1], GM[2], MULT, None)]
for i, s in enumerate(SROWS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    if s[0] == "Base":
        for col, key, fmt in [(2, "lna28", M0), (3, "aspg28", PCT1), (4, "hna28", M0), (5, "noneuvg28", PCT1), (6, "ibmg28", PCT1), (7, "gm28", PCT1), (8, "mult", MULT0)]:
            c = ws.cell(row=rr, column=col, value="=" + A[key]); c.font = F_LINK; c.number_format = fmt
    else:
        for col, v, fmt in [(2, s[1], '0.00'), (3, s[2], PCT1), (4, s[3], M0), (5, s[4], PCT1), (6, s[5], PCT1), (7, s[6], PCT1), (8, s[7], MULT0)]:
            c = ws.cell(row=rr, column=col, value=v); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = fmt
    f = {
        9: f"=B{rr}*Segments!$F$6*(1+C{rr})", 10: f"=D{rr}*{A['hnaasp']}", 11: f"=Segments!$F$12*(1+E{rr})", 12: f"=Segments!$F$14*(1+F{rr})",
        13: f"=I{rr}+J{rr}+K{rr}+L{rr}", 14: f"=M{rr}*G{rr}", 15: f"=N{rr}-{A['rd28']}-{A['sga28']}",
        16: f"=(O{rr}+{A['int28']})*(1-{A['tax']})+{A['eqm28']}", 17: f"=P{rr}/{A['sh28']}", 18: f"=Q{rr}*H{rr}", 19: f"=R{rr}/{A['price']}-1",
    }
    fm = {9: M0, 10: M0, 11: M0, 12: M0, 13: M0, 14: M0, 15: M0, 16: M0, 17: N2, 18: EUR2, 19: PCT1}
    for col, ff in f.items():
        ws.cell(row=rr, column=col, value=ff).number_format = fm[col]
ws["A11"] = "Probability"; ws["A11"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=10, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=11, column=2 + j, value=s[8]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E11"] = "=SUM(B11:D11)"; ws["E11"].number_format = PCT0; ws["F11"] = "must be 100%"; ws["F11"].font = F_NOTE
ws["A13"] = "Probability-weighted value, EUR"; ws["A13"].font = F_B
ws["R13"] = "=B11*R5+C11*R6+D11*R7"; ws["R13"].number_format = EUR2; ws["R13"].font = F_B; ws["R13"].fill = FILL_KEY
ws["S13"] = f"=R13/{A['price']}-1"; ws["S13"].number_format = PCT1
note(ws, 15, ["Value = 2028E diluted EPS x P/E, the year the market prices in October 2027. 2026 and 2027 are the same in all cases: 2027 low NA output is close to fully covered with orders.",
              "Bear: no low NA step in 2028 (85), price flat, 4 High NA, non-EUV -10% (China, DUV digestion), IBM +3%, gross margin 55%, 22x. Bull: 110 units, +5% price, 10 High NA, non-EUV +10%, IBM +12%, 59%, 32x.",
              "Price-implied: the 2028 low NA units, with every other base assumption, that give today's price at the base multiple (row 8 value equals the price)."])

# ===================================================================== DCF
ws = sheet("DCF", "DCF CROSS-CHECK, VALUED AT THE END OF 2027 (MY ASSUMPTIONS)", [44, 13, 13, 13, 13, 13])
head(ws, 4, ["", "2028E", "2029E", "2030E", "2031E", "2032E"])
ws["A5"] = "Net income growth"
for j, k in enumerate(["g29", "g30", "g31", "g32"]):
    c = ws.cell(row=5, column=3 + j, value="=" + A[k]); c.font = F_LINK; c.number_format = PCT1
ws["A6"] = "Net income"; ws["B6"] = "=Financials!G16"; ws["B6"].font = F_LINK
for j in range(4):
    col = get_column_letter(3 + j); prev = get_column_letter(2 + j)
    ws[f"{col}6"] = f"={prev}6*(1+{col}5)"
ws["A7"] = "Free cash flow"; ws["A8"] = "Discount factor"; ws["A9"] = "Present value"
for j in range(5):
    col = get_column_letter(2 + j)
    ws[f"{col}7"] = f"={col}6*{A['fcfconv']}"; ws[f"{col}8"] = f"=1/(1+{A['coe']})^{j + 1}"; ws[f"{col}9"] = f"={col}7*{col}8"
    for rr, fmt in [(6, M0), (7, M0), (8, '0.000'), (9, M0)]:
        ws[f"{col}{rr}"].number_format = fmt; ws[f"{col}{rr}"].alignment = RIGHT
dl = [
    (11, "Sum of present values, 2028 to 2032", "=SUM(B9:F9)", M0),
    (12, "Terminal value at end 2032", f"=F7*(1+{A['tg']})/({A['coe']}-{A['tg']})", M0),
    (13, "Present value of terminal value", "=B12*F8", M0),
    (14, "Equity value of operations", "=B11+B13", M0),
    (15, "Per share (2028 diluted shares), EUR", f"=B14/{A['sh28']}", EUR2),
    (16, "Net cash per share, held flat, EUR", f"=({A['cash']}-{A['ltdebt']})/{A['shout']}", EUR2),
    (17, "DCF value per share, EUR", "=B15+B16", EUR2),
    (18, "Against the price", f"=B17/{A['price']}-1", PCT1),
    (19, "Implied P/E on 2028E", "=B17/Financials!G18", XMULT),
    (21, "Reverse DCF: flat growth 2029 to 2032 that gives the price", DCF_NEED_G, PCT1),
    (22, "Value at that growth, EUR", f"=((B6*{A['fcfconv']}/(1+{A['coe']}))+B6*(1+B21)*{A['fcfconv']}/(1+{A['coe']})^2+B6*(1+B21)^2*{A['fcfconv']}/(1+{A['coe']})^3"
          f"+B6*(1+B21)^3*{A['fcfconv']}/(1+{A['coe']})^4+B6*(1+B21)^4*{A['fcfconv']}/(1+{A['coe']})^5"
          f"+B6*(1+B21)^4*{A['fcfconv']}*(1+{A['tg']})/({A['coe']}-{A['tg']})/(1+{A['coe']})^5)/{A['sh28']}+B16", EUR2),
]
conv_h = A["fcfconvh"]; conv = A["fcfconv"]
dl += [
    (24, "DCF value per share at 2025 conversion (115%), EUR", f"=B14*{conv_h}/{conv}/{A['sh28']}+B16", EUR2),
    (25, "Against the price", f"=B24/{A['price']}-1", PCT1),
    (26, "Reverse DCF at 115% conversion: flat growth 2029 to 2032 that gives the price", DCF_NEED_G_HIST, PCT1),
    (27, "Value at that growth, EUR", f"=((B6*{conv_h}/(1+{A['coe']}))+B6*(1+B26)*{conv_h}/(1+{A['coe']})^2+B6*(1+B26)^2*{conv_h}/(1+{A['coe']})^3"
          f"+B6*(1+B26)^3*{conv_h}/(1+{A['coe']})^4+B6*(1+B26)^4*{conv_h}/(1+{A['coe']})^5"
          f"+B6*(1+B26)^4*{conv_h}*(1+{A['tg']})/({A['coe']}-{A['tg']})/(1+{A['coe']})^5)/{A['sh28']}+B16", EUR2),
]
for rr, lab, f, fmt in dl:
    ws.cell(row=rr, column=1, value=lab); c = put(ws, rr, 2, f, fmt)
ws["B17"].fill = FILL_KEY; ws["B17"].font = F_B
note(ws, 29, ["A cross-check, not the method. The terminal value at 8.5% and 3% implies about 18 times free cash flow from 2033.",
              "The base uses 95% free cash flow conversion, below the 120% of 2024 and 115% of 2025; rows 24 to 27 show the same DCF at 115%.",
              "Rows 22 and 27 should equal the reference price (within rounding of the growth rate)."])

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION: P/E ON 2028E, TWELVE MONTHS OUT", [72, 16, 70])
head(ws, 4, ["Line", "Value", "Working / note"])
val = [
    ("base", "Base value, EUR", "=Scenarios!R6", EUR2, "28x 2028E diluted EPS."),
    ("wtd", "Probability-weighted value, EUR", "=Scenarios!R13", EUR2, "25 / 50 / 25."),
    ("px", "Reference price, EUR", "=" + A["price"], EUR2, "Euronext Amsterdam close, 6 October 2026."),
    ("upb", "Base value against the price", "=B5/B7-1", PCT1, ""),
    ("rule", "Rule on value alone (long at 15% above, short at 25% below)", '=IF(B8>=0.15,"LONG",IF(B8<=-0.25,"SHORT","NO CALL"))', None, "Mechanical, on the base value."),
    ("call", "DRAFT VIEW" if CALL["draft"] else "CALL", CALL["direction"], None, "Draft for Tommy Lau's decision." if CALL["draft"] else "Tommy Lau's call."),
    ("tgt", "Target, EUR", CALL["target"] if CALL["target"] else "none", EUR2, "No target for no call."),
    ("rlong", "Price at or below which the base is 15% above (points long)", "=B5/1.15", EUR2, ""),
    ("rshort", "Price at or above which the base is 25% below (points short)", "=B5/0.75", EUR2, ""),
    ("needeps", "2028E EPS the price needs at the base multiple, EUR", f"={A['price']}/{A['mult']}", N2, ""),
    ("needu", "2028 low NA units that give it (other base assumptions)", "=Scenarios!B8", '0.0', "Scenarios row 8."),
    ("mcap", "Market value, EUR bn", f"={A['price']}*{A['shout']}/1000", M1, ""),
    ("netcash", "Cash and short-term investments less long-term debt, EUR bn", f"=({A['cash']}-{A['ltdebt']})/1000", M1, "28 June 2026."),
    ("ev", "Enterprise value, EUR bn", "=B16-B17", M1, ""),
    ("evebit27", "EV / 2027E income from operations", "=B18*1000/Financials!F11", XMULT, ""),
    ("evebit28b", "EV at the base value / 2028E income from operations", f"=(B5*{A['shout']}/1000-B17)*1000/Financials!G11", XMULT, ""),
    ("pec26", "P/E on 2026 consensus (Zacks, converted)", "=Financials!E23", XMULT, ""),
    ("pec26sa", "P/E on 2026 consensus (stockanalysis.com)", f"={A['price']}/{A['cons26sa']}", XMULT, ""),
    ("pec27", "P/E on 2027 consensus (Zacks, converted)", "=Financials!F23", XMULT, ""),
    ("peadr27", "ADR P/E on 2027 consensus (US$)", f"={A['adr']}/{A['consusd27']}", XMULT, "Same basis as the peer table."),
    ("pe27", "P/E on my 2027E", "=Financials!F20", XMULT, ""),
    ("pe28", "P/E on my 2028E", "=Financials!G20", XMULT, ""),
    ("dcf", "DCF cross-check, EUR", "=DCF!B17", EUR2, "8.5% cost of equity, 3% terminal growth, 95% cash conversion; DCF!B24 at 115%."),
    ("peermed", "Peer median P/E, fiscal year ending in 2027", "=Peers!G10", XMULT, ""),
    ("fwd24", "Close at end 2024 over 2025 diluted EPS", f"={A['pxdec24']}/Financials!C18", XMULT, "History: one year forward, on actual EPS."),
    ("fwd25", "Close at end 2025 over my 2026E EPS", f"={A['pxdec25']}/Financials!E18", XMULT, ""),
    ("offhi", "Against the highest close (30 June 2026)", f"={A['price']}/{A['hiclose']}-1", PCT1, ""),
    ("uplo", "Against the lowest close (10 October 2025)", f"={A['price']}/{A['loclose']}-1", PCT1, ""),
    ("sincedec", "Change since 31 December 2025", f"={A['price']}/{A['pxdec25']}-1", PCT1, ""),
    ("blm", "End-2025 backlog in months of 2025 system sales", f"={A['backlog']}/Segments!D13*12", '0.0', ""),
    ("tpeur", "Average analyst target, converted to EUR", f"={A['tpusd']}/{A['eurusd']}", EUR2, ""),
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
assert V["base"] == "Valuation!$B$5" and V["px"] == "Valuation!$B$7" and V["upb"] == "Valuation!$B$8" and V["mcap"] == "Valuation!$B$16" and V["netcash"] == "Valuation!$B$17" and V["ev"] == "Valuation!$B$18"

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: 2028 LOW NA EUV UNITS AGAINST THE P/E (EUR)", [34, 14, 14, 14])
head(ws, 4, ["2028 low NA units \\ P/E", "", "", ""])
for j, (x, link) in enumerate(zip(SENS_X, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["mult"]) if link else x)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, u in enumerate(SENS_U):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=("=" + A["lna28"]) if i == 1 else u)
    c.number_format = M0; c.font = F_LINK if i == 1 else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=(
            f"=((($A{rr}*Segments!$F$6*(1+{A['aspg28']})+Scenarios!$J$6+Scenarios!$K$6+Scenarios!$L$6)*{A['gm28']}"
            f"-{A['rd28']}-{A['sga28']}+{A['int28']})*(1-{A['tax']})+{A['eqm28']})/{A['sh28']}*{col}$4")).number_format = EUR0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
ws["A11"] = "Cells 25% or more below the price"; ws["A11"].font = F_B
ws["B11"] = f'=COUNTIF(B5:D7,"<="&{A["price"]}*0.75)'; ws["C11"] = "of 9"
note(ws, 13, ["Middle row is my base 2028 low NA units; everything else as in the base case. 85 is ASML's planned 2027 capacity; 110 the 2028 step it is investigating."])

# ===================================================================== PEERS
ws = sheet("Peers", "PEER MULTIPLES: P/E ON CONSENSUS EPS FOR THE FISCAL YEAR ENDING IN 2027 (closes of 6 OCTOBER 2026)", [22, 18, 12, 12, 12, 12, 12, 20, 60])
head(ws, 4, ["Company", "Listing", "Price", "EPS FY27", "Currency", "Year end", "P/E", "EPS source", "What they make"])
ws.cell(row=5, column=1, value="ASML (ADR)").font = F_B; ws.cell(row=5, column=2, value="Nasdaq: ASML")
put(ws, 5, 3, "=" + A["adr"], N2); put(ws, 5, 4, "=" + A["consusd27"], N2); ws.cell(row=5, column=5, value="US$"); ws.cell(row=5, column=6, value="Dec 2027")
put(ws, 5, 7, "=C5/D5", XMULT); ws.cell(row=5, column=8, value="Zacks"); ws.cell(row=5, column=9, value="Lithography systems, metrology, installed base service and upgrades")
for i, (co, tk, px, eps, cur, ye, srcn, what) in enumerate(PEERS):
    rr = 6 + i
    ws.cell(row=rr, column=1, value=co); ws.cell(row=rr, column=2, value=tk)
    put(ws, rr, 3, px, N2); put(ws, rr, 4, eps, N2); ws.cell(row=rr, column=5, value=cur); ws.cell(row=rr, column=6, value=ye)
    put(ws, rr, 7, f"=C{rr}/D{rr}", XMULT); ws.cell(row=rr, column=8, value=srcn); ws.cell(row=rr, column=9, value=what).alignment = WRAP
ws["A10"] = "Median, four peers"; ws["A10"].font = F_B; ws["G10"] = "=MEDIAN(G6:G9)"; ws["G10"].number_format = XMULT
note(ws, 12, ["Year ends differ: ASML December, Applied Materials October, Lam Research and KLA June, Tokyo Electron March. The peers' fiscal 2027 ends 2 to 9 months before ASML's, so on a calendar basis their multiples would be lower than shown.",
              "Prices are 6 October 2026 closes in local currency (stockanalysis.com history pages). Zacks consensus retrieved 7 October 2026; Tokyo Electron from stockanalysis.com (S&P Global).",
              "Multiples only, to set the base multiple; no view on the peers' shares is expressed."])

# ===================================================================== SOURCES
ws = sheet("Sources", "SOURCES", [6, 130])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "ASML Annual Report 2025 on Form 20-F, filed 25 February 2026: income statement 2023 to 2025, net system sales per technology and end use, total net sales by region (China 29.1% in 2025, 36.1% in 2024), customer concentration (four customers, 61.2%), cost of system and service sales, free cash flow, export control risk wording, 2024 Investor Day 2030 opportunity table, financial calendar (Q3 2026 results on 14 October 2026), cost of sales with related parties.",
    "ASML Q4 and full-year 2025 results, Form 6-K, 28 January 2026: backlog EUR 38.8bn, 2025 net bookings, 2026 initial guide, EUR 12bn buyback to 2028; presentation slide 9 (system sales by technology and region).",
    "ASML Q2 2026 results, Form 6-K, 15 July 2026: release (Ex. 99.1), presentation (Ex. 99.2: technology, end-use and region splits, units, outlook, dividends) and US GAAP statements (Ex. 99.3: quarterly income statements, balance sheet, cash flows).",
    "ASML transcript of the Q2 2026 investor call prepared remarks, asml.com, 15 July 2026: 2026 segment growth guides, 65 low NA shipments, 2027 close to fully covered, 30% capacity steps, China around 20%, Capital Markets Day 10 June 2027.",
    "ASML Q2 2026 investor call Q&A as transcribed by Webull: 2027 EUV mix, order lead times, the 110 scenario for 2028.",
    "Euronext Amsterdam historical prices (live.euronext.com, ISIN NL0010273215), retrieved 7 October 2026. (Yahoo Finance chart API refused requests on 7 October 2026.) ECB euro reference rates, 6 October 2026.",
    "Zacks detailed earnings estimates for ASML (ADR), AMAT, LRCX and KLAC; stockanalysis.com (S&P Global) for ASML 2026 EUR consensus, analyst target, shares outstanding, closes and Tokyo Electron consensus; all retrieved 7 October 2026.",
    "Bloomberg report of 18 June 2026 on US questions over a possible EUV-related export to China, as carried by NL Times (19 June 2026), and ASML's statement; MATCH Act introduced in the US Congress in April 2026 (press reports). Not independently verified.",
    "The Physical Layer, 'ASML's EUV machines are booked a year or two ahead, like a grid connection', 7 October 2026: https://thephysicallayer.fyi/journal/asml-booked-ahead/",
    "Estimates for 2026 to 2028, the scenarios, the DCF and the valuation are the author's own. Personal research, not investment advice. I hold no position in ASML.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# ===================================================================== COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Draft view" if CALL["draft"] else "Call", "=" + V["call"], None, "Draft for Tommy Lau's decision; not yet a call." if CALL["draft"] else "Tommy Lau's call."),
    ("Target, EUR", "=" + V["tgt"], EUR2, "None for no call."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Reference price, EUR", "=" + A["price"], EUR2, "Euronext Amsterdam close, 6 October 2026."),
    ("Base value, EUR", "=" + V["base"], EUR2, "28x 2028E diluted EPS."),
    ("Base value against the price", "=" + V["upb"], PCT1, ""),
    ("Probability-weighted value, EUR", "=" + V["wtd"], EUR2, "25 / 50 / 25 bear / base / bull."),
    ("DCF cross-check, EUR (95% / 115% cash conversion)", '=TEXT(DCF!B17,"#,##0")&" / "&TEXT(DCF!B24,"#,##0")', None, "8.5% cost of equity, 3% terminal growth."),
    ("2026E / 2027E / 2028E EPS, EUR", '=TEXT(Financials!E18,"0.00")&" / "&TEXT(Financials!F18,"0.00")&" / "&TEXT(Financials!G18,"0.00")', None, "Own estimates, diluted, US GAAP."),
    ("Horizon", "12 months, to October 2027", None, ""),
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
    ("Quarterly", "Systems, Installed Base Management and gross margin, Q2 2025 to the Q3 2026 guide."),
    ("Segments", "Revenue build: low NA EUV units and price, High NA, DUV and metrology, Installed Base Management; China; segment margins."),
    ("Financials", "2024A to 2028E: income statement, EPS, P/E, consensus, free cash flow."),
    ("Scenarios", "Bear / base / bull on 2028E and the price-implied case; probability-weighted value."),
    ("DCF", "Cross-check at the end of 2027 and the reverse DCF."),
    ("Valuation", "Base value, the band, revisit levels, multiples, enterprise value."),
    ("Sensitivity", "2028 low NA units against the P/E."),
    ("Peers", "P/E on consensus for the fiscal year ending in 2027."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t); ws.cell(row=18 + i, column=2, value=d)
ws["A30"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A30"].font = F_NOTE
ws["A31"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."; ws["A31"].font = F_NOTE

order = ["Cover", "Assumptions", "Quarterly", "Segments", "Financials", "Scenarios", "DCF", "Valuation", "Sensitivity", "Peers", "Sources"]
wb._sheets = [wb[n] for n in order]
for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
