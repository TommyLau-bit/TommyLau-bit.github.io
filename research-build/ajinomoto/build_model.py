"""Ajinomoto initiation model, 7 Oct 2026. Live formulas throughout.

House style follows the Vertiv, Schneider and ASML models: navy header rows, blue font for hardcoded inputs, yellow fill on
my own assumptions, green font for cross-sheet links, black for formulas. Yen billion unless stated; per share in yen.
Fiscal years end 31 March (FY2026 = the year to 31 March 2027). Valuation is a sum of the parts on FY2027E.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L
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

Y0 = '"JPY "#,##0'; Y2 = '"JPY "#,##0.00'; B1 = '#,##0.0'; B2 = '#,##0.00'; M2 = '#,##0.00'
PCT1 = '0.0%'; PCT0 = '0%'; XM = '0.0"x"'
SUB = f"Tommy Lau | {NAME} (Tokyo: 2802) | {DATE_LONG} | Yen billion unless stated | Fiscal years end 31 March | Personal research, not investment advice."

wb = openpyxl.Workbook()


def sheet(name, title, widths):
    ws = wb.active if wb.active.title == "Sheet" else wb.create_sheet(name)
    ws.title = name
    ws["A1"] = title; ws["A1"].font = F_TTL
    ws["A2"] = SUB; ws["A2"].font = F_SUB
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[L(i)].width = w
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


def isf(v):
    return isinstance(v, str) and v.startswith("=")


def put(ws, r, c, v, fmt=None, bold=False):
    x = ws.cell(row=r, column=c, value=v if v is not None else "")
    if fmt: x.number_format = fmt
    x.alignment = RIGHT
    if v is not None and not isf(v) and not isinstance(v, str):
        x.font = Font(color="0000FF", bold=bold)
    elif isinstance(v, str) and (v.startswith("=Assumptions") or v.startswith("=History") or v.startswith("=Forecast")
                                 or v.startswith("=SOTP") or v.startswith("=Scenarios")):
        x.font = Font(color="008000", bold=bold)
    elif bold:
        x.font = F_B
    return x


sheet("Cover", f"{NAME.upper()} (TOKYO STOCK EXCHANGE PRIME: 2802)  INITIATION MODEL", [52, 26, 90])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [66, 14, 10, 100])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to another "
            "tab. Black = formula. Yen billion unless stated; per-share figures in yen; shares in millions.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"fms26", "fms27", "fmm26", "fmm27", "foodg27", "foodsg27", "hosg27", "bio27", "oth27", "other27", "shared27", "oopex26",
        "oopex27", "tax", "nci26", "nci27", "sh26", "sh27", "mfood", "mfm"}
rows = [
    ("MARKET (stockanalysis.com, retrieved 7 October 2026)", None, None, None, None),
    ("price", "Share price (Tokyo: 2802)", PRICE, "JPY", "Close, 7 October 2026."),
    ("hiclose", "Highest close of the past year (1 July 2026)", HI_CLOSE, "JPY", "Intraday high JPY 6,340 on 6 July 2026."),
    ("loclose", "Lowest close of the past year (9 January 2026)", LO_CLOSE, "JPY", "Intraday low JPY 3,270 on 8 January 2026."),
    ("pxdec25", "Close, 30 December 2025", PX_DEC25, "JPY", "Split-adjusted."),
    ("pxmar25", "Close, 31 March 2025", PX_MAR25, "JPY", "Split-adjusted (2-for-1 split effective 1 April 2025)."),
    ("shjun", "Shares outstanding excluding treasury, 30 June 2026", SH_JUN, "m", "Q1 FY2026 tanshin: 977,735,616 issued less 23,173,875 treasury."),
    ("shbought", "Shares repurchased 1 July to 30 September 2026", SH_BOUGHT_Q2, "m", "Buyback notices of 2 July and 2 October 2026 (cumulative 11,951,600 to 15,588,400)."),
    ("conseps26", "FY2026 consensus EPS (year to March 2027)", CONS_EPS26, "JPY", "stockanalysis.com (S&P Global), forecast page last updated 7 August 2026."),
    ("consop26", "FY2026 consensus operating income", CONS_OP26, "JPY bn", "Same source."),
    ("constp", "Average analyst price target", CONS_TP, "JPY", "stockanalysis.com, 7 October 2026."),
    ("evsa", "Enterprise value per stockanalysis.com", AJI_EV_SA, "JPY bn", "On 954.56m shares; my EV uses 950.9m."),
    ("BALANCE SHEET, 30 JUNE 2026 (Q1 FY2026 tanshin)", None, None, None, None),
    ("cash", "Cash and cash equivalents", CASH, "JPY bn", ""),
    ("debt", "Borrowings, commercial paper and bonds (excluding leases)", DEBT, "JPY bn", "7.1 + 140.0 + 30.0 + 4.0 + 174.5 + 206.3. Ajinomoto's interest-bearing debt including leases: JPY 623.7bn."),
    ("nci", "Non-controlling interests, book value", NCI, "JPY bn", "Added to EV as stockanalysis.com does for every peer."),
    ("GUIDED (FY2026 revised forecast, 6 August 2026)", None, None, None, None),
    ("foodbp26", "Seasonings and Foods plus Frozen Foods business profit, FY2026", FOOD_BP26, "JPY bn", "145.9 + 12.1."),
    ("foods26", "Seasonings and Foods plus Frozen Foods sales, FY2026", FOOD_SALES26, "JPY bn", "998.6 + 310.6."),
    ("hos26", "Bio-Pharma Services and Ingredients plus Others sales, FY2026", HO_SALES26, "JPY bn", "176.2 + 109.9."),
    ("others26", "Other segment sales, FY2026 (held in FY2027)", SALES["other"][2], "JPY bn", ""),
    ("fmsg26", "Functional Materials sales, FY2026 guide", SALES["fm"][2], "JPY bn", "Raised by JPY 9.0bn on 6 August."),
    ("fmbpg26", "Functional Materials business profit, FY2026 guide", BPROF["fm"][2], "JPY bn", "Raised by JPY 5.0bn on 6 August."),
    ("bio26", "Bio-Pharma Services and Ingredients business profit, FY2026", BIO_BP[0], "JPY bn", "Guide."),
    ("oth26", "Others business profit, FY2026", OTH_BP[0], "JPY bn", "Guide."),
    ("other26", "Other segment business profit, FY2026", OTHER_BP[0], "JPY bn", "Guide."),
    ("shared26", "Shared companywide expenses, FY2026", SHARED[0], "JPY bn", "Guide."),
    ("finnet", "Net financial income and expense", FIN_NET, "JPY bn", "Guide: profit before tax 180.2 less operating profit 184.2."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("fms26", "Functional Materials sales, FY2026E", FM_SALES[0], "JPY bn", "MINE. Q1 33.1; the guide of 120.6 implies only +10% for Q2 to Q4 after +54% in Q1."),
    ("fms27", "Functional Materials sales, FY2027E (base)", FM_SALES[1], "JPY bn", "MINE. +17%: volume within existing sites plus mix and some price."),
    ("fmm26", "Functional Materials business profit margin, FY2026E", FM_MARGIN[0], "%", "MINE. FY2025 54.2%; Q1 FY2026 57.7%."),
    ("fmm27", "Functional Materials business profit margin, FY2027E (base)", FM_MARGIN[1], "%", "MINE."),
    ("foodg27", "Food business profit growth, FY2027E", FOOD_G27, "%", "MINE. Seasonings and Foods plus Frozen Foods."),
    ("foodsg27", "Food sales growth, FY2027E", FOOD_SALES_G27, "%", "MINE."),
    ("hosg27", "Bio-Pharma and Others sales growth, FY2027E", HO_SALES_G27, "%", "MINE."),
    ("bio27", "Bio-Pharma Services and Ingredients business profit, FY2027E", BIO_BP[1], "JPY bn", "MINE."),
    ("oth27", "Others business profit, FY2027E", OTH_BP[1], "JPY bn", "MINE."),
    ("other27", "Other segment business profit, FY2027E", OTHER_BP[1], "JPY bn", "MINE."),
    ("shared27", "Shared companywide expenses, FY2027E", SHARED[1], "JPY bn", "MINE."),
    ("oopex26", "Net other operating expense, FY2026E", OTHER_OPEX[0], "JPY bn", "MINE, from the guide: operating profit 184.2 less business profit 202.0."),
    ("oopex27", "Net other operating expense, FY2027E", OTHER_OPEX[1], "JPY bn", "MINE."),
    ("tax", "Tax rate", TAX, "%", "MINE. FY2026 guide 25.9%; FY2025 26.0%."),
    ("nci26", "Profit to non-controlling interests, FY2026E", NCI_PROFIT[0], "JPY bn", "Guide 10.0."),
    ("nci27", "Profit to non-controlling interests, FY2027E", NCI_PROFIT[1], "JPY bn", "MINE."),
    ("sh26", "Average shares, FY2026E", SH_AVG[0], "m", "MINE. JPY 80bn buyback runs to 30 November 2026."),
    ("sh27", "Average shares, FY2027E", SH_AVG[1], "m", "MINE."),
    ("mfood", "EV / business profit, everything except the film (base)", MULT_FOOD, "x", "MINE. Food peers: Kikkoman 18.9x, Nestle 17.0x, Kraft Heinz 10.9x (median 17.0x)."),
    ("mfm", "EV / business profit, Functional Materials (base)", MULT_FM, "x", "MINE. Electronic materials peers: Resonac 24.5x, Shin-Etsu 14.0x, Entegris 32.6x (median 24.5x)."),
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
    c.number_format = PCT1 if unit == "%" else (XM if unit == "x" else (B2 if unit in ("JPY", "m") else B1))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
r += 1
ws.cell(row=r, column=1, value="Derived").font = Font(bold=True, color=NAVY); r += 1
for key, label, f, fmt in [
    ("shares", "Shares outstanding, about 30 September 2026 (m)", f"={A['shjun']}-{A['shbought']}", B2),
    ("netdebt", "Net debt (debt excluding leases less cash)", f"={A['debt']}-{A['cash']}", B1),
    ("mcap", "Market value", f"={A['price']}*B{r}/1000", B1),
    ("ev", "Enterprise value at the price", f"=B{r + 2}+B{r + 1}+{A['nci']}", B1),
]:
    ws.cell(row=r, column=1, value=label); put(ws, r, 2, f, fmt); A[key] = f"Assumptions!$B${r}"; r += 1

# ===================================================================== HISTORY
ws = sheet("History", "HISTORY: SEGMENTS, FUNCTIONAL MATERIALS AND THE FILM'S SHARE", [58] + [13] * 8)
head(ws, 4, ["JPY billion"] + SEG_COLS)
H = {}
hrows = [("Sales", None)] + [(f"  {n}", SALES[k]) for k, n in [("sf", "Seasonings and Foods"), ("ff", "Frozen Foods"),
         ("bp", "Bio-Pharma Services and Ingredients"), ("fm", "Functional Materials (electronic materials and others)"),
         ("oth", "Others (Healthcare and Others)"), ("other", "Other segment")]]
rr = 5
for lab, vals in hrows:
    ws.cell(row=rr, column=1, value=lab).font = F_B if vals is None else Font()
    if vals:
        for j, v in enumerate(vals): put(ws, rr, 2 + j, v, B1)
        H["s_" + lab.strip()] = rr
    rr += 1
ws.cell(row=rr, column=1, value="Total sales").font = F_B
for j in range(5):
    put(ws, rr, 2 + j, f"=SUM({L(2 + j)}6:{L(2 + j)}11)", B1, bold=True)
H["sales_tot"] = rr; rr += 1
ws.cell(row=rr, column=1, value="Reported total sales (check)")
for j, v in enumerate(SALES_TOT): put(ws, rr, 2 + j, v, B1)
rr += 2
ws.cell(row=rr, column=1, value="Business profit").font = F_B; rr += 1
bstart = rr
for k, n in [("sf", "Seasonings and Foods"), ("ff", "Frozen Foods"), ("bp", "Bio-Pharma Services and Ingredients"),
             ("fm", "Functional Materials"), ("oth", "Others (Healthcare and Others)"), ("other", "Other segment")]:
    ws.cell(row=rr, column=1, value=f"  {n}")
    for j, v in enumerate(BPROF[k]): put(ws, rr, 2 + j, v, B1)
    H["b_" + k] = rr; rr += 1
ws.cell(row=rr, column=1, value="Segment business profit before shared costs").font = F_B
for j in range(5): put(ws, rr, 2 + j, f"=SUM({L(2 + j)}{bstart}:{L(2 + j)}{rr - 1})", B1, bold=True)
H["segbp"] = rr; rr += 1
ws.cell(row=rr, column=1, value="  Shared companywide expenses")
for j, v in enumerate(BPROF["shared"]): put(ws, rr, 2 + j, v, B1)
H["b_shared"] = rr; rr += 1
ws.cell(row=rr, column=1, value="Group business profit").font = F_B
for j in range(5): put(ws, rr, 2 + j, f"={L(2 + j)}{H['segbp']}+{L(2 + j)}{H['b_shared']}", B1, bold=True)
H["bp_tot"] = rr; rr += 1
ws.cell(row=rr, column=1, value="Reported group business profit (check)")
for j, v in enumerate(BP_TOT): put(ws, rr, 2 + j, v, B1)
rr += 2
ws.cell(row=rr, column=1, value="The film's share").font = F_B; rr += 1
for key, lab, f in [
    ("sh_sales", "Functional Materials, share of sales", lambda c: f"={c}{H['s_Functional Materials (electronic materials and others)']}/{c}{H['sales_tot']}"),
    ("sh_segbp", "Functional Materials, share of segment business profit (before shared costs)", lambda c: f"={c}{H['b_fm']}/{c}{H['segbp']}"),
    ("sh_grpbp", "Functional Materials, share of group business profit", lambda c: f"={c}{H['b_fm']}/{c}{H['bp_tot'] + 1}"),
    ("fm_margin", "Functional Materials business profit margin", lambda c: f"={c}{H['b_fm']}/{c}{H['s_Functional Materials (electronic materials and others)']}"),
    ("food_sales", "Seasonings and Foods plus Frozen Foods, share of sales", lambda c: f"=({c}6+{c}7)/{c}{H['sales_tot']}"),
    ("food_bp", "Seasonings and Foods plus Frozen Foods, share of segment business profit", lambda c: f"=({c}{H['b_sf']}+{c}{H['b_ff']})/{c}{H['segbp']}"),
]:
    ws.cell(row=rr, column=1, value=lab)
    for j in range(5): put(ws, rr, 2 + j, f(L(2 + j)), PCT1)
    H[key] = rr; rr += 1
rr += 1
head(ws, rr, ["Functional Materials by year"] + FM_YEARS); rr += 1
ws.cell(row=rr, column=1, value="Sales")
for j, v in enumerate(FM_SALES_H): put(ws, rr, 2 + j, v, B1)
rr += 1
ws.cell(row=rr, column=1, value="Business profit")
for j, v in enumerate(FM_BP_H): put(ws, rr, 2 + j, v, B1)
rr += 1
ws.cell(row=rr, column=1, value="Margin")
for j in range(5): put(ws, rr, 2 + j, f"={L(2 + j)}{rr - 1}/{L(2 + j)}{rr - 2}", PCT1)
H["fmy_margin"] = rr; rr += 2
head(ws, rr, ["Functional Materials by quarter"] + FMQ_L); rr += 1
ws.cell(row=rr, column=1, value="Sales")
for j, v in enumerate(FMQ_SALES): put(ws, rr, 2 + j, v, B1)
rr += 1
ws.cell(row=rr, column=1, value="Business profit")
for j, v in enumerate(FMQ_BP): put(ws, rr, 2 + j, v, B1)
rr += 1
ws.cell(row=rr, column=1, value="Margin")
for j in range(5): put(ws, rr, 2 + j, f"={L(2 + j)}{rr - 1}/{L(2 + j)}{rr - 2}", PCT1)
H["fmq_margin"] = rr; rr += 1
ws.cell(row=rr, column=1, value="Sales growth on the year before")
put(ws, rr, 6, f"=F{rr - 3}/B{rr - 3}-1", PCT1); H["q1_g"] = rr; rr += 1
ws.cell(row=rr, column=1, value="Business profit growth on the year before")
put(ws, rr, 6, f"=F{rr - 3}/B{rr - 3}-1", PCT1); H["q1_bg"] = rr; rr += 1
ws.cell(row=rr, column=1, value="Ajinomoto Fine-Techno FY2025: sales, operating profit")
put(ws, rr, 2, FT_SALES_25, B1); put(ws, rr, 3, FT_OP_25, B1); rr += 2
note(ws, rr, ["Source: Ajinomoto Consolidated Results data sheets (FY2022 to Q1 FY2026) and FY2026 Revised Forecast by Segment, 6 August 2026. FY2024 restated without shared companywide expenses.",
              "Ajinomoto prints Functional Materials sales and business profit in yen each quarter, so the margin is exact, not only the 'over 50%' wording. Functional Materials is a business inside the Healthcare and Others segment; it includes ABF and other products such as adhesives. Business profit bases differ before FY2024 (allocation changes in FY2023 and FY2025).",
              "Ajinomoto Fine-Techno figures: Q1 FY2026 presentation, slide 15."])

# ===================================================================== FORECAST
ws = sheet("Forecast", "FORECAST: SEGMENT BUILD AND GROUP P&L, FY2026E AND FY2027E", [60, 14, 14, 14, 60])
head(ws, 4, ["JPY billion", "FY2026 guide", "FY2026E*", "FY2027E*", "Basis"])
F = {}
frows = [
    ("food_s", "Food sales (Seasonings and Foods plus Frozen Foods)", f"={A['foods26']}", f"={A['foods26']}", f"={A['foods26']}*(1+{A['foodsg27']})", B1, ""),
    ("ho_s", "Bio-Pharma and Others sales", f"={A['hos26']}", f"={A['hos26']}", f"={A['hos26']}*(1+{A['hosg27']})", B1, ""),
    ("oth_s", "Other segment sales", f"={A['others26']}", f"={A['others26']}", f"={A['others26']}", B1, ""),
    ("fm_s", "Functional Materials sales", f"={A['fmsg26']}", f"={A['fms26']}", f"={A['fms27']}", B1, "My estimates differ from the guide here only."),
    ("sales", "Total sales", "=SUM(B5:B8)", "=SUM(C5:C8)", "=SUM(D5:D8)", B1, ""),
    ("food_bp", "Food business profit", f"={A['foodbp26']}", f"={A['foodbp26']}", f"={A['foodbp26']}*(1+{A['foodg27']})", B1, ""),
    ("bio_bp", "Bio-Pharma Services and Ingredients business profit", f"={A['bio26']}", f"={A['bio26']}", f"={A['bio27']}", B1, ""),
    ("oth_bp", "Others business profit", f"={A['oth26']}", f"={A['oth26']}", f"={A['oth27']}", B1, ""),
    ("other_bp", "Other segment business profit", f"={A['other26']}", f"={A['other26']}", f"={A['other27']}", B1, ""),
    ("fm_bp", "Functional Materials business profit", f"={A['fmbpg26']}", f"={A['fms26']}*{A['fmm26']}", f"={A['fms27']}*{A['fmm27']}", B1, ""),
    ("shared", "Shared companywide expenses", f"={A['shared26']}", f"={A['shared26']}", f"={A['shared27']}", B1, ""),
    ("bp", "Group business profit", "=SUM(B10:B15)", "=SUM(C10:C15)", "=SUM(D10:D15)", B1, "Guide: 202.0."),
    ("oopex", "Net other operating expense", f"={A['oopex26']}", f"={A['oopex26']}", f"={A['oopex27']}", B1, ""),
    ("op", "Operating profit", "=B16+B17", "=C16+C17", "=D16+D17", B1, "Guide: 184.2."),
    ("pbt", "Profit before tax", f"=B18+{A['finnet']}", f"=C18+{A['finnet']}", f"=D18+{A['finnet']}", B1, ""),
    ("ni", "Profit attributable to owners of the parent", f"=B19*(1-{A['tax']})-{A['nci26']}", f"=C19*(1-{A['tax']})-{A['nci26']}", f"=D19*(1-{A['tax']})-{A['nci27']}", B1, "Guide: 123.5."),
    ("eps", "EPS, JPY", f"=B20/{A['sh26']}*1000", f"=C20/{A['sh26']}*1000", f"=D20/{A['sh27']}*1000", B2, "Guide: 129.84."),
    ("pe", "P/E at the price", f"={A['price']}/B21", f"={A['price']}/C21", f"={A['price']}/D21", XM, ""),
    ("fm_margin", "Functional Materials margin", "=B14/B8", "=C14/C8", "=D14/D8", PCT1, ""),
    ("fm_g", "Functional Materials sales growth", f"=B8/History!C{H['s_Functional Materials (electronic materials and others)']}-1", f"=C8/History!C{H['s_Functional Materials (electronic materials and others)']}-1", "=D8/C8-1", PCT1, ""),
    ("cons", "Consensus EPS (stockanalysis.com, 7 Aug 2026)", "", f"={A['conseps26']}", "", B2, "FY2027 consensus not verified."),
    ("vs", "Mine against consensus", "", "=C21/C25-1", "", PCT1, ""),
]
for i, (k, lab, b, c, d, fmt, basis) in enumerate(frows):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B if k in ("sales", "bp", "eps") else Font()
    for j, v in enumerate([b, c, d]):
        if v != "": put(ws, rr, 2 + j, v, fmt, bold=k in ("sales", "bp", "eps"))
    ws.cell(row=rr, column=5, value=basis).alignment = WRAP
    F[k] = rr
note(ws, 29, ["*My own estimates. FY2026 guide column applies my tax and other-items assumptions to Ajinomoto's segment guide, so its EPS differs slightly from the company's JPY 129.84.",
              "FY2026 = the year to 31 March 2027; FY2027 = the year to 31 March 2028. Business profit = sales less cost of sales, selling, R&D and G&A, plus share of associates' profit."])

# ===================================================================== SOTP
ws = sheet("SOTP", "SUM OF THE PARTS ON FY2027E, TWELVE MONTHS OUT", [66, 16, 16, 70])
head(ws, 4, ["JPY billion unless stated", "FY2026E", "FY2027E", "Note"])
S = {}
srows = [
    ("costs", "Shared costs and net other operating expense", "=Forecast!C15+Forecast!C17", "=Forecast!D15+Forecast!D17", B1, "Spread by sales."),
    ("fmshare", "Functional Materials share of sales", "=Forecast!C8/Forecast!C9", "=Forecast!D8/Forecast!D9", PCT1, ""),
    ("fmnet", "Functional Materials profit after its share of costs", "=Forecast!C14+B5*B6", "=Forecast!D14+C5*C6", B1, ""),
    ("nonfm", "Everything else after its share of costs", "=Forecast!C10+Forecast!C11+Forecast!C12+Forecast!C13+B5*(1-B6)", "=Forecast!D10+Forecast!D11+Forecast!D12+Forecast!D13+C5*(1-C6)", B1, "Food, Bio-Pharma, Others, Other segment."),
    ("fmnetsh", "Film share of profit after costs", "=B7/(B7+B8)", "=C7/(C7+C8)", PCT1, ""),
]
for i, (k, lab, b, c, fmt, nt) in enumerate(srows):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab); put(ws, rr, 2, b, fmt); put(ws, rr, 3, c, fmt); ws.cell(row=rr, column=4, value=nt)
    S[k] = rr
head(ws, 11, ["Base valuation", "Value", "", "Note"])
vrows = [
    ("evfood", "EV, everything except the film", f"=C8*{A['mfood']}", B1, "Base multiple x FY2027E."),
    ("evfm", "EV, Functional Materials", f"=C7*{A['mfm']}", B1, ""),
    ("ev", "Enterprise value", "=B12+B13", B1, ""),
    ("netdebt", "Less net debt", f"={A['netdebt']}", B1, "30 June 2026, held flat (MINE)."),
    ("nci", "Less non-controlling interests (book)", f"={A['nci']}", B1, ""),
    ("eq", "Equity value", "=B14-B15-B16", B1, ""),
    ("base", "Base value per share, JPY", f"=B17/{A['shares']}*1000", Y0, ""),
    ("up", "Base value against the price", f"=B18/{A['price']}-1", PCT1, ""),
    ("rule", "Rule (long at +15% or more, short at -25% or less)", '=IF(B19>=0.15,"LONG",IF(B19<=-0.25,"SHORT","NO CALL"))', None, ""),
    ("call", "Call", CALL["direction"], None, "Judgement; the rule above gives the band."),
    ("foodps", "Everything else less net debt and minorities, per share", f"=(B12-B15-B16)/{A['shares']}*1000", Y0, ""),
    ("fmps", "Film, per share at the base multiple", f"=B13/{A['shares']}*1000", Y0, ""),
    ("fmsh_base", "Film share of EV at my base", "=B13/B14", PCT1, ""),
    ("revl", "Revisit long: price at or below", "=B18/1.15", Y0, ""),
    ("revs", "Revisit short: price at or above", "=B18/0.75", Y0, ""),
    ("med", "Value on peer medians (no premium), per share", f"=(C8*Peers!H13+C7*Peers!H14-B15-B16)/{A['shares']}*1000", Y0, "Food median and electronic materials median."),
    ("medup", "Peer-median value against the price", f"=B27/{A['price']}-1", PCT1, ""),
]
for i, (k, lab, f, fmt, nt) in enumerate(vrows):
    rr = 12 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B if k in ("base", "eq") else Font()
    c = put(ws, rr, 2, f, fmt, bold=k == "base")
    if k == "call": c.font = F_INB
    if k == "base": c.fill = FILL_KEY
    ws.cell(row=rr, column=4, value=nt)
    S[k] = rr
head(ws, 30, ["What the price implies", "Value", "", "Note"])
irows = [
    ("evmkt", "Enterprise value at the price", f"={A['ev']}", B1, ""),
    ("fmimp", "Implied film EV (EV less everything else at my base)", "=B31-B12", B1, ""),
    ("fmx", "Implied film EV / FY2027E film profit after costs", "=B32/C7", XM, ""),
    ("fmneed", "Film profit after costs the price needs at the base multiple", f"=B32/{A['mfm']}", B1, ""),
    ("fmshmkt", "Film share of EV at the price", "=B32/B31", PCT1, ""),
    ("floor", "Everything else as a share of the price", f"=B22/{A['price']}", PCT1, ""),
    ("ten_mkt", "10% on the implied film value, JPY per share", f"=0.1*B32/{A['shares']}*1000", Y0, ""),
    ("ten_mkt_pc", "... as a share of the price", f"=B37/{A['price']}", PCT1, ""),
    ("ten_base", "10% on my film value, JPY per share", f"=0.1*B13/{A['shares']}*1000", Y0, ""),
    ("turn_fm", "One turn of film multiple, JPY per share", f"=C7/{A['shares']}*1000", Y0, ""),
    ("turn_food", "One turn of the other multiple, JPY per share", f"=C8/{A['shares']}*1000", Y0, ""),
    ("pecons", "P/E on FY2026 consensus", f"={A['price']}/{A['conseps26']}", XM, ""),
    ("evop", "EV / FY2026 consensus operating income (stockanalysis EV)", f"={A['evsa']}/{A['consop26']}", XM, ""),
    ("evbp", "EV / FY2026 guided business profit", f"=B31/History!D{H['bp_tot'] + 1}", XM, "Reported guide total, 202.0."),
    ("since25", "Share price change since 30 December 2025", f"={A['price']}/{A['pxdec25']}-1", PCT1, ""),
    ("offhigh", "Share price against the highest close of the past year", f"={A['price']}/{A['hiclose']}-1", PCT1, ""),
]
for i, (k, lab, f, fmt, nt) in enumerate(irows):
    rr = 31 + i
    ws.cell(row=rr, column=1, value=lab); put(ws, rr, 2, f, fmt); ws.cell(row=rr, column=4, value=nt)
    S[k] = rr
note(ws, 48, ["Costs are spread by sales because Ajinomoto Fine-Techno's own accounts already carry most of the film's overheads: its FY2025 operating profit (53.0) was close to Functional Materials business profit (54.6).",
              "Peer multiples are EV over consensus operating income for the fiscal year ending December 2026 or March 2027; applied to FY2027E, the year the market prices in October 2027."])

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "SCENARIOS: BEAR / BASE / BULL ON FY2027E", [58, 14, 14, 14, 60])
head(ws, 4, ["", "Bear", "Base", "Bull", "Note"])
sc_in = [
    ("Functional Materials sales FY2027E", [SCEN[0][1], f"={A['fms27']}", SCEN[2][1]], B1, "Bear: a pause like FY2023; bull: the reported 30% price rise sticks."),
    ("Functional Materials margin", [SCEN[0][2], f"={A['fmm27']}", SCEN[2][2]], PCT1, ""),
    ("Food business profit growth FY2027E", [SCEN[0][3], f"={A['foodg27']}", SCEN[2][3]], PCT1, ""),
    ("Bio-Pharma business profit FY2027E", [SCEN[0][4], f"={A['bio27']}", SCEN[2][4]], B1, ""),
    ("EV / profit, everything except the film", [SCEN[0][5], f"={A['mfood']}", SCEN[2][5]], XM, ""),
    ("EV / profit, film", [SCEN[0][6], f"={A['mfm']}", SCEN[2][6]], XM, ""),
    ("Probability", [SCEN[0][7], SCEN[1][7], SCEN[2][7]], PCT0, ""),
]
for i, (lab, vals, fmt, nt) in enumerate(sc_in):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab)
    for j, v in enumerate(vals):
        c = put(ws, rr, 2 + j, v, fmt)
        if not isf(v): c.fill = FILL_ASSUME
    ws.cell(row=rr, column=5, value=nt)
calc = [
    ("Total sales FY2027E", lambda c: f"=Forecast!$D$5+Forecast!$D$6+Forecast!$D$7+{c}5", B1),
    ("Costs (shared and other), spread by sales", lambda c: "=Forecast!$D$15+Forecast!$D$17", B1),
    ("Film profit after costs", lambda c: f"={c}5*{c}6+{c}13*{c}5/{c}12", B1),
    ("Everything else after costs", lambda c: f"={A['foodbp26']}*(1+{c}7)+{c}8+{A['oth27']}+{A['other27']}+{c}13*(1-{c}5/{c}12)", B1),
    ("Enterprise value", lambda c: f"={c}15*{c}9+{c}14*{c}10", B1),
    ("Value per share, JPY", lambda c: f"=({c}16-{A['netdebt']}-{A['nci']})/{A['shares']}*1000", Y0),
    ("Change against the price", lambda c: f"={c}17/{A['price']}-1", PCT1),
]
for i, (lab, f, fmt) in enumerate(calc):
    rr = 12 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B if "Value" in lab else Font()
    for j in range(3):
        put(ws, rr, 2 + j, f(L(2 + j)), fmt, bold="Value" in lab)
ws["A20"] = "Probability-weighted value, JPY"; ws["A20"].font = F_B
put(ws, 20, 2, "=SUMPRODUCT(B17:D17,B11:D11)", Y0, bold=True)
ws["A21"] = "Weighted against the price"; put(ws, 21, 2, f"=B20/{A['price']}-1", PCT1)
ws["A22"] = "Sum of probabilities"; put(ws, 22, 2, "=SUM(B11:D11)", PCT0)
ws["A23"] = "Base check: equals SOTP base value"; put(ws, 23, 2, "=C17-SOTP!B18", B2)
note(ws, 25, ["Everything except the film is valued at one multiple; Bio-Pharma Services (CDMO) is small enough that a separate multiple changes little."])

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "SENSITIVITY: FY2027E FILM SALES (56% MARGIN) AGAINST THE FILM MULTIPLE; EVERYTHING ELSE AT BASE", [40, 14, 14, 14])
head(ws, 4, ["Film sales FY2027E \\ film multiple"] + [f"{x:.0f}x" for x in SENS_X])
for i, s in enumerate(SENS_S):
    rr = 5 + i
    put(ws, rr, 1, s, B1)
    for j, x in enumerate(SENS_X):
        col = L(2 + j)
        tot = f"(Forecast!$D$5+Forecast!$D$6+Forecast!$D$7+$A{rr})"
        cost = "(Forecast!$D$15+Forecast!$D$17)"
        fmnet = f"($A{rr}*{A['fmm27']}+{cost}*$A{rr}/{tot})"
        nonfm = f"(Forecast!$D$10+Forecast!$D$11+Forecast!$D$12+Forecast!$D$13+{cost}*(1-$A{rr}/{tot}))"
        put(ws, rr, 2 + j, f"=({nonfm}*{A['mfood']}+{fmnet}*{x}-{A['netdebt']}-{A['nci']})/{A['shares']}*1000", Y0)
ws["A9"] = "Cells above the price"; put(ws, 9, 2, f"=COUNTIF(B5:D7,\">\"&{A['price']})", "0")
ws["A10"] = "Cells 15% or more above the price"; put(ws, 10, 2, f"=COUNTIF(B5:D7,\">=\"&{A['price']}*1.15)", "0")
ws["A11"] = "Cells 25% or more below the price"; put(ws, 11, 2, f"=COUNTIF(B5:D7,\"<=\"&{A['price']}*0.75)", "0")
ws["A12"] = "Centre cell check: equals base"; put(ws, 12, 2, "=C6-SOTP!B18", B2)

# ===================================================================== PEERS
ws = sheet("Peers", "PEERS: EV / FORWARD OPERATING INCOME AND FORWARD P/E", [22, 16, 10, 16, 16, 12, 12, 12, 12, 12, 46])
head(ws, 4, ["Company", "Listing", "Group", "EV (bn, local)", "Fwd op. income (bn)", "Year end", "Price", "EV / op. income", "Fwd EPS", "P/E", "What they make"])
for i, p in enumerate(PEERS + REF_PEERS):
    rr = 5 + i
    n, lst, g, ev, oi, px, eps, ye, what = p
    for j, v in enumerate([n, lst, {"food": "Food", "elec": "Electronic materials", "ref": "Reference"}[g]]):
        ws.cell(row=rr, column=1 + j, value=v)
    put(ws, rr, 4, ev, B1); put(ws, rr, 5, oi, '#,##0.000'); ws.cell(row=rr, column=6, value=ye)
    put(ws, rr, 7, px, B2); put(ws, rr, 8, f"=D{rr}/E{rr}", XM)
    if eps:
        put(ws, rr, 9, eps, B2); put(ws, rr, 10, f"=G{rr}/I{rr}", XM)
    else:
        ws.cell(row=rr, column=10, value="n/m (GAAP loss)")
    ws.cell(row=rr, column=11, value=what)
rr = 5 + len(PEERS + REF_PEERS)
ws.cell(row=rr, column=1, value="Ajinomoto"); ws.cell(row=rr, column=2, value="Tokyo: 2802"); ws.cell(row=rr, column=3, value="Subject")
put(ws, rr, 4, f"={A['evsa']}", B1); put(ws, rr, 5, f"={A['consop26']}", '#,##0.000'); ws.cell(row=rr, column=6, value="Mar 2027")
put(ws, rr, 7, f"={A['price']}", B2); put(ws, rr, 8, f"=D{rr}/E{rr}", XM); put(ws, rr, 9, f"={A['conseps26']}", B2); put(ws, rr, 10, f"=G{rr}/I{rr}", XM)
ws.cell(row=rr, column=11, value="Seasonings, frozen foods, amino acids, CDMO, ABF film")
ws["A13"] = "Food median EV / op. income"; ws["A13"].font = F_B; put(ws, 13, 8, "=MEDIAN(H5:H7)", XM, bold=True)
ws["A14"] = "Electronic materials median"; ws["A14"].font = F_B; put(ws, 14, 8, "=MEDIAN(H8:H10)", XM, bold=True)
note(ws, 16, ["stockanalysis.com (S&P Global consensus), retrieved 7 October 2026. EV = market value + debt - cash + non-controlling interests. Forward operating income = consensus for the fiscal year ending December 2026 or March 2027 (year ends differ by up to three months).",
              "Kraft Heinz, Nestle, Entegris in US$ or CHF; EV and operating income in the same currency, so the multiple needs no conversion. Entegris P/E uses adjusted consensus EPS of US$3.93 (61.1x on reported EPS); Kraft Heinz consensus is on reported (GAAP) figures. The electronic materials median rests on three names, so it equals Resonac.",
              "JSR, once a natural peer, was taken private by Japan Investment Corporation and delisted on 25 June 2024. Sekisui Chemical, a rival film maker, is shown for reference only: films are a small part of a diversified group.",
              "Multiples only; no view on the peers' shares."])

# ===================================================================== PRICE
ws = sheet("Price", "SHARE PRICE: MONTH-END CLOSE, SPLIT-ADJUSTED, JPY", [16, 14])
head(ws, 4, ["Month", "Close"])
for i, (lab, v) in enumerate(zip(PX_LABELS, PX)):
    ws.cell(row=5 + i, column=1, value=lab); put(ws, 5 + i, 2, v, B1)
note(ws, 6 + len(PX), ["stockanalysis.com history for TYO:2802, retrieved 7 October 2026. The last point is the close on 7 October 2026."])

# ===================================================================== SOURCES
ws = sheet("Sources", "SOURCES", [150])
for i, t in enumerate([
    "Ajinomoto Consolidated Financial Results (tanshin) for FY2025, 7 May 2026, and Q1 FY2026, 6 August 2026.",
    "Ajinomoto Consolidated Results data sheets: FY2022 (11 May 2023), FY2023 (9 May 2024), FY2024 (8 May 2025), H1 FY2025 (6 November 2025), 9M FY2025 (5 February 2026), FY2025 (7 May 2026), Q1 FY2026 (6 August 2026).",
    "Ajinomoto FY2026 Revised Forecast by Segment and Notice of Revision to Full-Year Forecast, 6 August 2026.",
    "Ajinomoto FY2025 results presentation with script, 7 May 2026; Q1 FY2026 presentation, 6 August 2026; ASV Report 2026 (integrated report).",
    "Ajinomoto notices on the repurchase of own shares, 2 July and 2 October 2026; Fine-Techno merger policy, 6 August 2026.",
    "Prices, consensus and peer data: stockanalysis.com (S&P Global Market Intelligence), retrieved 7 October 2026.",
    "Palliser Capital value enhancement plan, 31 March 2026 (as reported). Reports of an ABF price rise: DigiTimes, 13 May 2026, citing Taiwanese substrate makers; not confirmed in Ajinomoto's own documents.",
    "All estimates marked MINE, and the valuation, are the author's own.",
]):
    ws.cell(row=4 + i, column=1, value=t).alignment = WRAP

# ===================================================================== COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Draft view" if CALL["draft"] else "Call", "=SOTP!B21", None, "Draft for Tommy Lau's decision; not yet a call." if CALL["draft"] else "Tommy Lau's call."),
    ("Target, JPY", "None (no call)" if CALL["target"] is None else CALL["target"], None, ""),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Reference price, JPY", f"={A['price']}", Y0, "Tokyo close, 7 October 2026."),
    ("Base value, JPY", "=SOTP!B18", Y0, "Sum of the parts on FY2027E: 18x everything else, 28x the film."),
    ("Base value against the price", "=SOTP!B19", PCT1, ""),
    ("Probability-weighted value, JPY", "=Scenarios!B20", Y0, "25 / 50 / 25."),
    ("Value on peer medians, JPY", "=SOTP!B27", Y0, "17.0x food, 24.5x electronic materials."),
    ("Film share of EV: my base / at the price", '=TEXT(SOTP!B24,"0%")&" / "&TEXT(SOTP!B35,"0%")', None, ""),
    ("Film share of sales / business profit, FY2025", f'=TEXT(History!C{H["sh_sales"]},"0.0%")&" / "&TEXT(History!C{H["sh_segbp"]},"0.0%")', None, "Business profit before shared costs, like for like."),
    ("FY2026E / FY2027E EPS, JPY", '=TEXT(Forecast!C21,"0.0")&" / "&TEXT(Forecast!D21,"0.0")', None, "Own estimates."),
    ("Horizon", "12 months, to October 2027", None, ""),
]
for i, (lab, v, fmt, nt) in enumerate(cover):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B
    c = ws.cell(row=rr, column=2, value=v)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    c.font = F_LINK if isf(v) else F_IN
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
ws["A19"] = "Tabs"; ws["A19"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("History", "Segment sales and business profit, the film's share of sales and profit, Functional Materials by year and quarter."),
    ("Forecast", "FY2026E and FY2027E segment build and group P&L, against the guide and consensus."),
    ("SOTP", "Cost allocation, sum of the parts, the band, what the price implies, how much the film moves the whole."),
    ("Scenarios", "Bear / base / bull on FY2027E; probability-weighted value."),
    ("Sensitivity", "Film sales against the film multiple."),
    ("Peers", "Food and electronic materials peers on forward EV / operating income and P/E."),
    ("Price", "Month-end closes, October 2023 to 7 October 2026."),
    ("Sources", "Documents behind every figure."),
]):
    ws.cell(row=20 + i, column=1, value=t).font = F_B
    ws.cell(row=20 + i, column=2, value=d)

order = ["Cover", "Assumptions", "History", "Forecast", "SOTP", "Scenarios", "Sensitivity", "Peers", "Price", "Sources"]
wb._sheets = [wb[n] for n in order]
for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
