"""Seagate initiation model, 2 Nov 2026. Live formulas throughout.

House style follows the Vertiv and Micron models: navy header rows, blue font for hardcoded inputs, yellow fill on
my own assumptions, green font for cross-sheet links, black for formulas.
Non-GAAP basis unless marked GAAP. Fiscal years end on the Friday closest to 30 June (FY2026 = year to 3 July 2026;
FY2027 = year to 2 July 2027). Supply statements are in calendar years.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from data import *
import data as _d

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

USD2 = '"US$"#,##0.00'; USD0 = '"US$"#,##0'; BN2 = '#,##0.00'; BN3 = '#,##0.000'; BN1 = '#,##0.0'; N0 = '#,##0'
PCT1 = '0.0%'; PCT0 = '0%'; PCT2 = '0.00%'; MULTF = '0.0"x"'; MULT0 = '0"x"'
SUB = (f"Tommy Lau | Seagate Technology Holdings plc (Nasdaq: STX) | {DATE_LONG} | Non-GAAP basis; FY26 ended 3 Jul 2026, "
       "FY27 ends 2 Jul 2027 | Personal research, not investment advice.")

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


sheet("Cover", "SEAGATE TECHNOLOGY HOLDINGS PLC (NASDAQ: STX)  INITIATION MODEL", [38, 26, 90])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [64, 14, 10, 92])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "another tab. Black = formula. US$ billion unless stated; per-share figures in US$; shares in billions; exabytes (EB).")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"sh", "q3rev", "q4rev", "q3om", "q4om", "other", "eb28", "ptb28", "om28", "capex", "da", "wc",
        "ebg", "nyears", "pf", "edgen", "nm", "mult", "rate", "w28", "w29", "w30"}
rows = [
    ("MARKET (retrieved 2 November 2026)", None, None, None, None),
    ("price", "Share price (Nasdaq: STX)", PRICE, "US$", "Nasdaq close, 30 October 2026 (stockanalysis.com daily history; Yahoo Finance refused requests on 2 Nov)."),
    ("hiclose", "Highest close of the past year (22 June 2026)", HI_CLOSE, "US$", "stockanalysis.com. Intraday high US$1,145.00 on 18 June 2026."),
    ("loclose", "Lowest close of the past year (21 November 2025)", LO_CLOSE, "US$", "stockanalysis.com. Intraday low US$228.61, same day."),
    ("pxdec25", "Close, 31 Dec 2025", PRICE_DEC25, "US$", "stockanalysis.com."),
    ("pxsep26", "Close, 30 Sep 2026", PX_SEP26, "US$", "stockanalysis.com."),
    ("pxt0", "Close, 1 Oct 2026", PX_TOSHIBA[0], "US$", "stockanalysis.com."),
    ("pxt1", "Close, 2 Oct 2026 (Toshiba's release)", PX_TOSHIBA[1], "US$", "stockanalysis.com."),
    ("sharesout", "Shares outstanding, 2 Oct 2026", SHARES_OUT, "bn", "Q1 FY27 release: 230 million."),
    ("netdebt", "Net debt, 2 Oct 2026 (principal less cash)", NET_DEBT, "US$bn", "Q1 FY27 supplemental: US$1,125m. US$750m of notes retired in October from cash."),
    ("cons27", "FY27 consensus EPS", CONS_EPS_27, "US$", "stockanalysis.com (S&P Global, updated 29 Oct 2026), 21 analysts; range 32.75 to 45.94."),
    ("cons28", "FY28 consensus EPS", CONS_EPS_28, "US$", "stockanalysis.com (S&P Global)."),
    ("consrev27", "FY27 consensus revenue", CONS_REV_27, "US$bn", "stockanalysis.com (S&P Global)."),
    ("consrev28", "FY28 consensus revenue", CONS_REV_28, "US$bn", "stockanalysis.com (S&P Global)."),
    ("REPORTED AND GUIDED (Seagate releases and supplementals)", None, None, None, None),
    ("fy25rev", "FY25 revenue", FY25["rev"], "US$bn", "Q4 FY26 release comparatives."),
    ("fy25ni", "FY25 non-GAAP net income", FY25["ni"], "US$bn", "Same."),
    ("fy25eps", "FY25 non-GAAP EPS", FY25["eps"], "US$", "Same."),
    ("fy25om", "FY25 non-GAAP operating margin", FY25["om"], "%", "Same: 23.4%."),
    ("fy26rev", "FY26 revenue", FY26["rev"], "US$bn", "Q4 FY26 release."),
    ("fy26ni", "FY26 non-GAAP net income", FY26["ni"], "US$bn", "Same."),
    ("fy26eps", "FY26 non-GAAP EPS", FY26["eps"], "US$", "Same."),
    ("fy26om", "FY26 non-GAAP operating margin", FY26["om"], "%", "Same: 36.5%."),
    ("fy26nl", "FY26 nearline exabytes shipped", FY26["nl_eb"], "EB", "FY26 10-K (the four supplementals, 159, 165, 175 and 195, sum to 694 on rounding)."),
    ("g2rev", "Q2 FY27 revenue guide", G2["rev"], "US$bn", "Release, 27 Oct 2026: US$4.8bn plus or minus US$0.1bn."),
    ("g2eps", "Q2 FY27 non-GAAP EPS guide", G2["eps"], "US$", "US$9.20 plus or minus US$0.20; operating margin 'towards mid 50% range'."),
    ("tax", "Tax rate, non-GAAP", TAX, "%", "Q2 guide: about 16% of income before taxes; held (mine)."),
    ("dps", "Dividend per share, a year", DPS, "US$", "US$0.76 a quarter, declared 27 Oct 2026."),
    ("MY ASSUMPTIONS: FISCAL 2027 QUARTERS 3 AND 4 AND FISCAL 2028", None, None, None, None),
    ("sh", "Diluted shares, FY27 Q2 onward and FY28", SH, "bn", "MINE: the Q2 guide of about 233 million held; buybacks treated as cash kept."),
    ("q3rev", "Q3 FY27 revenue", Q27_REV[2], "US$bn", "MINE: price per TB keeps rising on calendar 2027 contracts, more slowly."),
    ("q4rev", "Q4 FY27 revenue", Q27_REV[3], "US$bn", "MINE."),
    ("q3om", "Q3 FY27 operating margin", Q27_OM[2], "%", "MINE: 'gross margin to keep expanding through fiscal 2027' (call)."),
    ("q4om", "Q4 FY27 operating margin", Q27_OM[3], "%", "MINE."),
    ("other", "Net interest and other, a quarter", OTHER, "US$bn", "MINE: after the debt paydown (Q1 FY27 interest expense US$41m)."),
    ("eb28", "FY28 nearline exabyte growth (base)", EB28, "%", "MINE: management targets mid-20s % supply growth (call)."),
    ("ptb28", "FY28 change in price per TB (base)", PTB28, "%", "MINE: first half on calendar 2027 contracts, second half on calendar 2028 terms not yet set."),
    ("om28", "FY28 operating margin (base)", OM28, "%", "MINE."),
    ("capex", "Capital spending, share of revenue", CAPEX_PCT, "%", "MINE: middle of the guided 4% to 6% for FY27."),
    ("da", "Depreciation and amortisation, a year", DA_YR, "US$bn", "MINE. FY26 US$0.276bn (release)."),
    ("wc", "Working capital build over the twelve months", WC, "US$bn", "MINE. Inventories rose to US$1.70bn at 2 Oct 2026 from US$1.57bn at 3 Jul 2026 (10-Q) as Seagate prepared for Mozaic 4 qualifications (call)."),
    ("MY ASSUMPTIONS: NORMAL EARNINGS AND VALUE (base)", None, None, None, None),
    ("ebg", "Nearline exabyte growth a year to a mid-cycle year", EB_G, "x", "MINE: management's mid-20s % supply growth ('25% is a really good number')."),
    ("nyears", "Years from FY26 to the mid-cycle year", N_YEARS, "yrs", "MINE. Around FY2030."),
    ("pf", "Normal price per TB against the FY25 and FY26 average", PF, "%", "MINE. The average is US$13.91 per TB (Quarterly tab)."),
    ("edgen", "Edge IoT revenue in a normal year", EDGE_N, "US$bn", "MINE. FY26 US$2.42bn."),
    ("nm", "Normal net margin", NM, "%", "MINE. FY26 non-GAAP 29.0%; FY25 19.1%; FY16 to FY25 GAAP 9.5% (Normal tab)."),
    ("mult", "P/E on normal earnings", _d.MULT, "x", "MINE."),
    ("rate", "Discount rate on above-normal earnings", RATE, "%", "MINE."),
    ("w28", "Share of FY28 excess earned in FY28", W_UP[0], "%", "MINE: base keeps prices firm through FY28."),
    ("w29", "Share of FY28 excess earned again in FY29", W_UP[1], "%", "MINE: half."),
    ("w30", "Share of FY28 excess earned again in FY30", W_UP[2], "%", "MINE: none."),
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
    c.number_format = (PCT2 if unit == "%" else (MULT0 if key == "mult" else ("0.00" if unit == "x" else
                       ("#,##0.000" if unit == "bn" else ("#,##0.00" if unit == "US$" else (N0 if unit in ("EB", "yrs") else BN3))))))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1

# ===================================================================== QUARTERLY
ws = sheet("Quarterly", "QUARTERLY HISTORY, Q1 FY25 TO Q1 FY27, AND FISCAL 2027 (Q2 GUIDE, Q3 AND Q4 MINE)", [52] + [10] * 12)
QH = QL + ["Q2 FY27 guide", "Q3 FY27E", "Q4 FY27E"]
head(ws, 4, ["US$ billion unless stated"] + QH)
C = [get_column_letter(2 + j) for j in range(12)]   # B..M ; J = Q1 FY27, K..M = rest of FY27


def qrow(row, label, vals, fmt, bold=False):
    ws.cell(row=row, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        put(ws, row, 2 + j, v, fmt)


qrow(5, "Revenue", Q_REV + ["=" + A["g2rev"], "=" + A["q3rev"], "=" + A["q4rev"]], BN3, True)
qrow(6, "  Data Center", Q_DC + [None] * 3, BN3)
qrow(7, "  Edge IoT (revenue less Data Center)", [f"={c}5-{c}6" for c in C[:9]] + [None] * 3, BN3)
qrow(8, "Nearline exabytes shipped", Q_NL + [None] * 3, N0)
qrow(9, "Total HDD exabytes shipped", Q_EB + [None] * 3, N0)
qrow(10, "Data Center revenue per nearline TB, US$ (derived)", [f"={c}6*1000/{c}8" for c in C[:9]] + [None] * 3, BN2, True)
qrow(11, "  change on a year", [None] * 4 + [f"={C[j]}10/{C[j - 4]}10-1" for j in range(4, 9)] + [None] * 3, PCT1)
qrow(12, "Gross margin, non-GAAP", Q_GM + [None] * 3, PCT1)
qrow(13, "Operating margin, non-GAAP (Q2: implied by the EPS guide)",
     Q_OM + [f"=(K17*K18/(1-{A['tax']})-{A['other']})/K5", "=" + A["q3om"], "=" + A["q4om"]], PCT1)
qrow(14, "Operating income, non-GAAP", [None] * 8 + [2.147, "=K5*K13", "=L5*L13", "=M5*M13"], BN3)
qrow(15, "Net interest and other", [None] * 9 + ["=" + A["other"]] * 3, BN3)
qrow(16, "Net income, non-GAAP", [None] * 4 + [0.583, 0.702, 0.934, 1.319, 1.781, "=K18*K17"] +
     [f"=({c}14+{c}15)*(1-{A['tax']})" for c in C[10:]], BN3, True)
qrow(17, "Diluted shares, bn", [None] * 4 + [0.223, 0.226, 0.228, 0.231, 0.232] + ["=" + A["sh"]] * 3, BN3)
qrow(18, "Diluted EPS, US$ (reported; Q2 guide; Q3 and Q4 mine)", Q_EPS + ["=" + A["g2eps"]] + [f"={c}16/{c}17" for c in C[10:]], USD2, True)
qrow(19, "Free cash flow", Q_FCF + [None] * 3, BN3)
ws["A21"] = "Checks"; ws["A21"].font = Font(bold=True, color=NAVY)
chk = [
    (22, "FY26 revenue, sum of quarters", "=SUM(F5:I5)", BN3),
    (23, "FY26 nearline EB, sum of quarters", "=SUM(F8:I8)", N0),
    (24, "Price per nearline TB, FY25 and FY26 average, US$", "=SUM(B6:I6)*1000/SUM(B8:I8)", BN2),
    (25, "Price per nearline TB, FY26 average, US$", "=SUM(F6:I6)*1000/SUM(F8:I8)", BN2),
    (26, "Nearline EB, Q1 FY27 on Q1 FY26", "=J8/F8-1", PCT1),
    (27, "FY27 revenue, sum of quarters", "=SUM(J5:M5)", BN2),
    (28, "FY27 EPS, sum of quarters", "=SUM(J18:M18)", USD2),
    (29, "Q1 FY27 net margin", "=J16/J5", PCT1),
]
for rr, lab, f, fmt in chk:
    ws.cell(row=rr, column=1, value=lab); c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
note(ws, 31, ["Source: Seagate Supplemental Financial Information, 28 Oct 2025 (Q1 FY26, with FY25 quarters on the VIA-inclusive nearline definition), 27 Jan, 28 Apr and 27 Oct 2026; Q4 FY26 and Q1 FY27 releases.",
              "Price per nearline TB is my derived ratio: Data Center revenue (which also includes systems) over nearline exabytes. US$ million per EB equals US$ per TB.",
              "Q2 FY27 is the guide midpoint; its operating margin is what makes the guided EPS. Q3 and Q4 FY27 are my estimates."])

# ===================================================================== FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (US$ billion unless stated, non-GAAP basis)", [60, 12, 12, 12, 12])
head(ws, 4, ["", "FY25A", "FY26A", "FY27E*", "FY28E*"])
fin = [
    (5, "Revenue", ["=" + A["fy25rev"], "=" + A["fy26rev"], "=SUM(Quarterly!J5:M5)", f"=D5*(1+E6)"], BN2, True),
    (6, "Revenue growth (FY28: nearline EB growth and price per TB, mine)", [None, "=C5/B5-1", "=D5/C5-1", f"=(1+{A['eb28']})*(1+{A['ptb28']})-1"], PCT1, False),
    (7, "Operating margin", ["=" + A["fy25om"], "=" + A["fy26om"], "=(SUM(Quarterly!J14:M14))/D5", "=" + A["om28"]], PCT1, False),
    (8, "Net income", ["=" + A["fy25ni"], "=" + A["fy26ni"], "=SUM(Quarterly!J16:M16)", f"=(E5*E7+4*{A['other']})*(1-{A['tax']})"], BN2, True),
    (9, "Net margin", ["=B8/B5", "=C8/C5", "=D8/D5", "=E8/E5"], PCT1, False),
    (10, "Diluted EPS, US$", ["=" + A["fy25eps"], "=" + A["fy26eps"], "=SUM(Quarterly!J18:M18)", f"=E8/{A['sh']}"], USD2, True),
    (11, "Consensus EPS, US$", [None, None, "=" + A["cons27"], "=" + A["cons28"]], USD2, False),
    (12, "Mine against consensus", [None, None, "=D10/D11-1", "=E10/E11-1"], PCT1, False),
    (13, "Revenue against consensus", [None, None, f"=D5/{A['consrev27']}-1", f"=E5/{A['consrev28']}-1"], PCT1, False),
    (14, "P/E at reference price", [f"={A['price']}/B10", f"={A['price']}/C10", f"={A['price']}/D10", f"={A['price']}/E10"], MULTF, False),
    (15, "P/E on consensus", [None, None, f"={A['price']}/D11", f"={A['price']}/E11"], MULTF, False),
    (17, "Net income, Q2 FY27 to Q1 FY28 (three FY27 quarters plus a quarter of FY28)", [None, None, "=SUM(Quarterly!K16:M16)+E8/4", None], BN2, False),
    (18, "Revenue over the same twelve months", [None, None, "=SUM(Quarterly!K5:M5)+E5/4", None], BN2, False),
    (19, "Free cash flow over the twelve months (net income + D&A - capex - working capital)", [None, FY26["fcf"], f"=D17+{A['da']}-{A['capex']}*D18-{A['wc']}", None], BN2, False),
    (20, "Net cash, about October 2027 (less dividends; buybacks treated as cash kept)", [None, None, f"=-{A['netdebt']}+D19-{A['dps']}*{A['sh']}", None], BN2, True),
    (21, "  per share, US$", [None, None, f"=D20/{A['sh']}", None], USD2, True),
]
for rr, label, vals, fmt, bold in fin:
    ws.cell(row=rr, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        put(ws, rr, 2 + j, v, fmt)
note(ws, 23, [
    "*FY27E sums Q1 actual, the Q2 guide and my Q3 and Q4 (Quarterly tab). FY28E is my base case. FY26 free cash flow is Seagate's figure.",
    "Consensus from stockanalysis.com (S&P Global data, updated 29 October 2026).",
    f"Note check: FY27E revenue {REV27:.2f}, EPS {EPS27:.2f}; FY28E revenue {REV28:.2f}, EPS {EPS28:.2f}; net cash per share at October 2027 {NC_PS:.2f}.",
])

# ===================================================================== NORMAL
ws = sheet("Normal", "THE CYCLE AND NORMAL (MID-CYCLE) EARNINGS", [44, 12, 12, 12, 12, 12])
head(ws, 4, ["Fiscal year (GAAP)", "Revenue, US$bn", "Cost of revenue", "Gross margin", "Net income", "Net margin"])
for i, (y, rv, co, ni) in enumerate(zip(YRS, REV_H, COR_H, NI_H)):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=y)
    put(ws, rr, 2, rv, BN3); put(ws, rr, 3, co, BN3); put(ws, rr, 4, f"=1-C{rr}/B{rr}", PCT1)
    put(ws, rr, 5, ni, BN3); put(ws, rr, 6, f"=E{rr}/B{rr}", PCT1)
ws["A17"] = "FY16 to FY25, all ten years"; ws["A17"].font = F_B
ws["B17"] = "=SUM(B5:B14)"; ws["C17"] = "=SUM(C5:C14)"; ws["D17"] = "=1-C17/B17"; ws["E17"] = "=SUM(E5:E14)"; ws["F17"] = "=E17/B17"
for c, f in (("B17", BN2), ("C17", BN2), ("D17", PCT1), ("E17", BN2), ("F17", PCT1)): ws[c].number_format = f
ws["A18"] = "FY23 revenue against FY22"; ws["B18"] = "=B12/B11-1"; ws["B18"].number_format = PCT0
head(ws, 20, ["Normal year (base)", "Value", "", "", "", ""])
nrows = [
    (21, "FY26 nearline EB", "=" + A["fy26nl"], N0),
    (22, "Growth factor", f"={A['ebg']}^{A['nyears']}", "0.000"),
    (23, "Normal nearline EB", "=B21*B22", N0),
    (24, "FY25 and FY26 average price per TB, US$", "=Quarterly!B24", BN2),
    (25, "Normal price per TB against that average", "=" + A["pf"], PCT0),
    (26, "Normal Data Center revenue, US$bn", "=B23*B24*B25/1000", BN2),
    (27, "Edge IoT, US$bn", "=" + A["edgen"], BN2),
    (28, "Normal revenue, US$bn", "=B26+B27", BN2),
    (29, "Normal net margin", "=" + A["nm"], PCT0),
    (30, "Normal net income, US$bn", "=B28*B29", BN2),
    (31, "Normal EPS, US$", f"=B30/{A['sh']}", USD2),
]
for rr, lab, f, fmt in nrows:
    ws.cell(row=rr, column=1, value=lab); c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
ws["A31"].font = F_B; ws["B31"].fill = FILL_KEY
note(ws, 33, ["Revenue, cost of revenue and GAAP net income: Seagate 10-K XBRL data on SEC EDGAR (companyfacts API).",
              "The normal year is mine: nearline EB grow 25% a year for four years from FY26, and the price per TB settles at the FY25 and FY26 average."])

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (VALUE AT OCTOBER 2027)", [12] + [11] * 16)
head(ws, 4, ["Case", "Price per TB vs avg", "Normal margin", "Normal P/E", "FY28 EB growth", "FY28 price per TB", "FY28 op margin",
             "w FY28", "w FY29", "w FY30", "Normal EPS", "FY28 EPS", "Net cash / sh", "Excess / sh", "Normal value / sh", "Value, US$", "vs price"])
for i, s in enumerate(SCEN):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    if s[0] == "Base":
        for col, key, fmt in [(2, "pf", PCT0), (3, "nm", PCT0), (4, "mult", MULT0), (5, "eb28", PCT0), (6, "ptb28", PCT0), (7, "om28", PCT0),
                              (8, "w28", PCT0), (9, "w29", PCT0), (10, "w30", PCT0)]:
            c = ws.cell(row=rr, column=col, value="=" + A[key]); c.font = F_LINK; c.number_format = fmt
    else:
        vals = [s[1], s[2], s[3], s[4], s[5], s[6], s[7][0], s[7][1], s[7][2]]
        fmts = [PCT0, PCT0, MULT0, PCT0, PCT0, PCT0, PCT0, PCT0, PCT0]
        for col, (v, fmt) in enumerate(zip(vals, fmts), 2):
            c = ws.cell(row=rr, column=col, value=v); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = fmt
    ws.cell(row=rr, column=11, value=f"=(Normal!$B$23*Normal!$B$24*B{rr}/1000+Normal!$B$27)*C{rr}/{A['sh']}").number_format = USD2
    ws.cell(row=rr, column=12, value=f"=(Financials!$D$5*(1+E{rr})*(1+F{rr})*G{rr}+4*{A['other']})*(1-{A['tax']})/{A['sh']}").number_format = USD2
    ws.cell(row=rr, column=13, value="=Financials!$D$21").number_format = USD2
    ws.cell(row=rr, column=14, value=f"=(L{rr}-K{rr})*(H{rr}/(1+{A['rate']})+I{rr}/(1+{A['rate']})^2+J{rr}/(1+{A['rate']})^3)").number_format = USD2
    ws.cell(row=rr, column=15, value=f"=K{rr}*D{rr}").number_format = USD2
    ws.cell(row=rr, column=16, value=f"=M{rr}+N{rr}+O{rr}").number_format = USD2
    ws.cell(row=rr, column=17, value=f"=P{rr}/{A['price']}-1").number_format = PCT0
ws["A10"] = "Probability"; ws["A10"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=9, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=10, column=2 + j, value=s[8]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E10"] = "=SUM(B10:D10)"; ws["E10"].number_format = PCT0; ws["F10"] = "must be 100%"; ws["F10"].font = F_NOTE
ws["A12"] = "Probability-weighted value, US$"; ws["A12"].font = F_B
ws["P12"] = "=B10*P5+C10*P6+D10*P7"; ws["P12"].number_format = USD2; ws["P12"].font = F_B; ws["P12"].fill = FILL_KEY
ws["Q12"] = f"=P12/{A['price']}-1"; ws["Q12"].number_format = PCT1
note(ws, 14, ["Value at October 2027 = net cash per share + above-normal earnings to FY30, discounted + normal EPS x normal P/E.",
              "Excess = (FY28 EPS - normal EPS) x (w FY28 / 1.1 + w FY29 / 1.1^2 + w FY30 / 1.1^3). FY27 and the cash at October 2027 are the same in all three cases.",
              "Bear: calendar 2028 contracts reprice 10% lower as Toshiba's added Philippine capacity ships; normal price per TB 20% below the FY25 and FY26 average at an 18% margin.",
              "Bull: the September 2026 quarter's US$17.4 per TB becomes the normal; contracts reach 2030; 38% normal margin."])

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION: NET CASH + ABOVE-NORMAL EARNINGS + NORMAL EARNINGS, AT OCTOBER 2027", [72, 16, 70])
head(ws, 4, ["Line", "Value", "Working / note"])
val = [
    ("nc", "Net cash per share, October 2027, US$", "=Financials!D21", USD2, "Financials tab."),
    ("exc", "Above-normal earnings, discounted, per share, US$", "=Scenarios!N6", USD2, "Base case."),
    ("term", "Normal EPS x normal P/E, US$", "=Scenarios!O6", USD2, "Base case."),
    ("base", "Base-case value per share, US$", "=B5+B6+B7", USD2, ""),
    ("px", "Reference price, US$", "=" + A["price"], USD2, "Nasdaq close, 30 October 2026."),
    ("upb", "Base value against the price", "=B8/B9-1", PCT1, ""),
    ("wtd", "Probability-weighted value, US$", "=Scenarios!P12", USD2, "Scenarios tab."),
    ("rule", "Rule on value alone (long at 15% above, short at 25% below)", '=IF(B10>=0.15,"LONG",IF(B10<=-0.25,"SHORT","NO CALL"))', None, "Mechanical only; wider on the short side because a short's losses are open-ended."),
    ("call", "DRAFT VIEW" if CALL["draft"] else "CALL", CALL["direction"], None, "Draft for Tommy Lau's decision." if CALL["draft"] else "Tommy Lau's call."),
    ("tgt", "Target, US$", CALL["target"] if CALL["target"] else "None (no call)", USD2, ""),
    ("mcap", "Market value, US$bn", f"={A['price']}*{A['sharesout']}", BN1, "On 230 million shares outstanding."),
    ("ev", "Enterprise value, US$bn", f"=B15+{A['netdebt']}", BN1, ""),
    ("pe26", "P/E on FY26 EPS", "=Financials!C14", MULTF, ""),
    ("pe27", "P/E on my FY27E", "=Financials!D14", MULTF, ""),
    ("pe28", "P/E on my FY28E", "=Financials!E14", MULTF, ""),
    ("pec27", "P/E on FY27 consensus", "=Financials!D15", MULTF, "stockanalysis.com."),
    ("pec28", "P/E on FY28 consensus", "=Financials!E15", MULTF, ""),
    ("pen", "P/E on my normal EPS", f"={A['price']}/Normal!B31", MULTF, ""),
    ("k", "Discount factor on the FY28 excess (base weights)", f"={A['w28']}/(1+{A['rate']})+{A['w29']}/(1+{A['rate']})^2+{A['w30']}/(1+{A['rate']})^3", "0.0000", ""),
    ("need", "Normal EPS the price needs, US$", f"=({A['price']}-B5-B23*Scenarios!L6)/({A['mult']}-B23)", USD2, "At my base FY28, cash and multiple. What the market prices in."),
    ("needm", "That as a net margin on my normal revenue", f"=B24*{A['sh']}/Normal!B28", PCT1, "FY26 non-GAAP 29.0%; Q1 FY27 42.1%."),
    ("needrev", "Or as normal revenue at my 30% margin, US$bn", f"=B24*{A['sh']}/{A['nm']}", BN1, ""),
    ("needptb", "Which is a normal price per TB of, US$", f"=(B26-{A['edgen']})*1000/Normal!B23", BN2, "Against US$17.42 in the September 2026 quarter, the highest yet."),
    ("need26", "Needed normal EPS against FY26 EPS", f"=B24/{A['fy26eps']}", PCT0, ""),
    ("need28", "Needed normal EPS against my FY28 EPS", "=B24/Financials!E10", PCT0, ""),
    ("rlong", "Price at or below which the base is 15% above (points long)", "=B8/1.15", USD2, ""),
    ("rshort", "Price at or above which the base is 25% below (points short)", "=B8/0.75", USD2, ""),
    ("offhi", "Against the highest close (22 Jun 2026)", f"={A['price']}/{A['hiclose']}-1", PCT1, ""),
    ("rise", "Change since 31 Dec 2025", f"={A['price']}/{A['pxdec25']}-1", PCT0, ""),
    ("oct", "Change since 30 Sep 2026", f"={A['price']}/{A['pxsep26']}-1", PCT1, ""),
    ("tday", "Move on 2 Oct 2026, the day of Toshiba's release", f"={A['pxt1']}/{A['pxt0']}-1", PCT1, ""),
    ("perun", "P/E on the Q2 FY27 EPS guide, annualised", f"={A['price']}/({A['g2eps']}*4)", MULTF, ""),
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
assert V["base"] == "Valuation!$B$8" and V["k"] == "Valuation!$B$23" and V["need"] == "Valuation!$B$24" and V["mcap"] == "Valuation!$B$15"
assert V["needrev"] == "Valuation!$B$26"

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: NORMAL NET MARGIN AGAINST THE MULTIPLE ON NORMAL EARNINGS (US$)", [30, 14, 14, 14])
head(ws, 4, ["Normal net margin \\ normal P/E", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_X, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["mult"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (m, link) in enumerate(zip(SENS_NM, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=("=" + A["nm"]) if link else m)
    c.number_format = PCT0; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j,
                value=f"=Valuation!$B$5+Valuation!$B$23*(Scenarios!$L$6-Normal!$B$28*$A{rr}/{A['sh']})+Normal!$B$28*$A{rr}/{A['sh']}*{col}$4").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 25% or more below the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,"<="&{A["price"]}*0.75)'; ws["C10"] = "of 9"
note(ws, 12, ["Middle row links to my base normal margin and the middle column to the base multiple. Normal revenue, FY28 EPS and net cash as in the base."])

# ===================================================================== PEERS
ws = sheet("Peers", "PEER MULTIPLES ON CONSENSUS FOR THE YEAR ENDING IN 2027 (stockanalysis.com, 2 NOVEMBER 2026)", [22, 16, 12, 14, 16, 12, 38])
head(ws, 4, ["Company", "Listing", "Price, US$", "Consensus EPS", "Year", "P/E", "What they make"])
ws.cell(row=5, column=1, value="Seagate").font = F_B; ws.cell(row=5, column=2, value="Nasdaq: STX")
c = ws.cell(row=5, column=3, value="=" + A["price"]); c.font = F_LINK; c.number_format = BN2
c = ws.cell(row=5, column=4, value="=" + A["cons27"]); c.font = F_LINK; c.number_format = BN2
ws.cell(row=5, column=5, value="FY to Jul 2027"); ws["F5"] = "=C5/D5"; ws["F5"].number_format = MULTF
ws.cell(row=5, column=7, value="Hard drives (nearline and other)")
for i, (co, tk, px, eps, yr, what) in enumerate(PEERS):
    rr = 6 + i
    ws.cell(row=rr, column=1, value=co); ws.cell(row=rr, column=2, value=tk)
    put(ws, rr, 3, px, BN2); put(ws, rr, 4, eps, BN2)
    ws.cell(row=rr, column=5, value=yr); ws.cell(row=rr, column=6, value=f"=C{rr}/D{rr}").number_format = MULTF
    ws.cell(row=rr, column=7, value=what)
ws["A10"] = "Flash makers, average"; ws["A10"].font = F_B; ws["F10"] = "=AVERAGE(F7:F8)"; ws["F10"].number_format = MULTF
ws["A11"] = "Hard drive makers, average"; ws["A11"].font = F_B; ws["F11"] = "=AVERAGE(F5:F6)"; ws["F11"].number_format = MULTF
note(ws, 13, ["Prices: Nasdaq closes of 30 October 2026. Consensus from stockanalysis.com (S&P Global), retrieved 2 November 2026.",
              "Toshiba, the third hard drive maker, has been privately held since December 2023 and has no listed multiple.",
              "Fiscal year-ends differ by up to two months. Multiples only; no view on the peers' shares is expressed."])

# ===================================================================== SOURCES
ws = sheet("Sources", "SOURCES", [6, 130])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Seagate fiscal Q1 2027 results release, Exhibit 99.1 to Form 8-K, 27 October 2026: revenue, GAAP and non-GAAP margins, net income, EPS, cash flow, cash, debt, shares, the Q2 FY27 guide, dividend, the October debt retirement.",
    "Seagate Supplemental Financial Information, Q1 FY27, 27 October 2026: quarterly trends Q1 FY26 to Q1 FY27, Data Center and Edge IoT revenue, exabytes shipped, net debt; 'vast majority of Data Center nearline supply allocated through CY28, with some cloud supply agreements extending through CY30'; exabyte growth 'by increasing capacity per drive rather than increasing drive unit production'; Mozaic 4 and 5.",
    "Seagate supplementals of 28 October 2025 (Q1 FY26; FY25 quarters on the VIA-inclusive nearline definition), 27 January 2026 (allocated through CY26; 26% more exabytes on similar units) and 28 April 2026 (largely allocated through CY27; build-to-order contracts through FY27).",
    "Seagate fiscal Q4 and fiscal 2026 results release, Exhibit 99.1 to Form 8-K, 28 July 2026: FY25 and FY26 non-GAAP revenue, margins, net income, EPS, free cash flow, capex. Form 10-K for the year to 3 July 2026, filed 4 August 2026.",
    "Seagate earnings call, 27 October 2026, Seagate's corrected transcript (FactSet CallStreet) at investors.seagate.com: build-to-order pricing set through CY27 and CY28 terms to be finalised over the next few quarters; mid-20s % exabyte supply growth; capex 4% to 6% of revenue; pricing and costs; buybacks.",
    "SEC EDGAR XBRL companyfacts data for Seagate (CIK 1137789): GAAP revenue, cost of revenue and net income, FY2016 to FY2026.",
    "Western Digital fiscal Q1 2027 results release, Exhibit 99.1 to Form 8-K, 22 October 2026. Toshiba Electronic Devices & Storage news release, 2 October 2026 (Toshiba Information Equipment (Philippines), its Philippine drive plant, began nearline production at Laguna Technopark and aims to nearly double that plant's annual capacity by FY2027 against FY2025 on a storage capacity basis). Seagate Form 10-Q for the quarter to 2 October 2026, filed 29 October 2026 (inventories). Micron fiscal Q4 2026 prepared remarks, 30 September 2026.",
    "stockanalysis.com, retrieved 2 November 2026: daily price history (Nasdaq closes), consensus EPS and revenue (S&P Global), peer prices and consensus. (Yahoo Finance chart API refused requests on 2 November 2026.)",
    "The Physical Layer, 'The chip supply chain's slow parts are sold years before they are made', claims dated 30 October 2026: https://thephysicallayer.fyi/journal/the-chip-supply-chain/",
    "Estimates for Q3 FY27 to FY28, normal earnings and the valuation are the author's own. Personal research, not investment advice. I hold no position in Seagate.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# ===================================================================== COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Draft view" if CALL["draft"] else "Call", "=" + V["call"], None, "Draft for Tommy Lau's decision; not yet a call." if CALL["draft"] else "Tommy Lau's call."),
    ("Target, US$", "=" + V["tgt"], USD2, "No target for a no call."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Reference price, US$", "=" + A["price"], USD2, "Nasdaq close, 30 October 2026."),
    ("Base value, US$", "=" + V["base"], USD2, f"Net cash + above-normal earnings to FY30 + {MULT}x normal EPS, at October 2027."),
    ("Base value against the price", "=" + V["upb"], PCT1, ""),
    ("Probability-weighted value, US$", "=" + V["wtd"], USD2, "25 / 50 / 25 bear / base / bull."),
    ("Normal EPS the price needs, US$", "=" + V["need"], USD2, f"Against my base of US${N_BASE:.2f}."),
    ("FY27E / FY28E EPS, US$", '=TEXT(Financials!D10,"0.00")&" / "&TEXT(Financials!E10,"0.00")', None, "Own estimates, non-GAAP, diluted."),
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
    ("Quarterly", "Q1 FY25 to Q1 FY27 reported, the Q2 FY27 guide and my Q3 and Q4; exabytes and price per terabyte."),
    ("Financials", "FY25A to FY28E: revenue, margins, EPS, consensus, P/E, cash at October 2027."),
    ("Normal", "Eleven years of the cycle (GAAP) and my normal (mid-cycle) year."),
    ("Scenarios", "Bear / base / bull value at October 2027 and the probability-weighted value."),
    ("Valuation", "Base value, multiples, what the price needs, revisit levels."),
    ("Sensitivity", "Normal net margin against the multiple on normal earnings."),
    ("Peers", "Hard drive and flash makers on consensus for the year ending in 2027."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t); ws.cell(row=18 + i, column=2, value=d)
ws["A29"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A29"].font = F_NOTE
ws["A30"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."; ws["A30"].font = F_NOTE

order = ["Cover", "Assumptions", "Quarterly", "Financials", "Normal", "Scenarios", "Valuation", "Sensitivity", "Peers", "Sources"]
wb._sheets = [wb[n] for n in order]
for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
