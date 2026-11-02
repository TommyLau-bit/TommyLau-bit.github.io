"""Mitsubishi Heavy Industries (TSE: 7011) initiation model: sum of the parts. Live formulas throughout.

House style follows the Vertiv and Hitachi models: navy header rows, navy bold titles, blue font for hardcoded inputs,
yellow fill on my own assumptions, green font for cross-sheet links, black for formulas.
"""
import datetime
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

JPY0 = '"¥"#,##0'
JPY2 = '"¥"#,##0.00'
BN1 = '#,##0.0'
PCT1 = '0.0%'
PCT0 = '0%'
MULTF = '0.0"x"'
MULT0 = '0"x"'
DLONG = datetime.date.fromisoformat(DATE).strftime("%-d %B %Y")
SUB = f"Tommy Lau | Mitsubishi Heavy Industries (TSE: 7011) | {DLONG} | Personal research, not investment advice."
VIEWLBL = "Draft view (Tommy decides)" if CALL["draft"] else "Call (Tommy Lau)"

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


# =====================================================================  COVER (filled last)
ws = sheet("Cover", "MITSUBISHI HEAVY INDUSTRIES (TSE: 7011)  INITIATION MODEL", [40, 24, 90])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [58, 14, 10, 100])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. Yen billion unless stated. Fiscal year ends 31 March.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"gt_m26", "gt_g27", "gt_m27", "er_g27", "er_m27", "ads_g27", "ads_m27", "pi27", "is27", "corp27", "adv_share",
        "x_gt", "x_er", "x_pi", "x_is", "x_ads", "x_corp"}
Q1 = "Q1 FY2026 Financial Results presentation and Consolidated Financial Results, 4 August 2026"
FY = "FY2025 Financial Results presentation, 12 May 2026"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "¥", f"TSE close, {PRICE_DATE}. stockanalysis.com TYO:7011, retrieved 2 November 2026."),
    ("hiclose", "Record close, 2 March 2026", HI_CLOSE, "¥", "stockanalysis.com daily history (intraday high ¥5,208 the same day)."),
    ("issued", "Issued shares including treasury shares, 30 June 2026", SHARES_ISSUED, "m", Q1 + ": 3,373,647,810."),
    ("treas", "Treasury shares, 30 June 2026", TREASURY, "m", Q1 + ": 12,985,995."),
    ("cash", "Cash and cash equivalents, 30 June 2026", CASH, "¥bn", Q1 + ", statement of financial position."),
    ("debt", "Interest-bearing debt, 30 June 2026", DEBT, "¥bn", Q1 + ", presentation p8."),
    ("eqm", "Investments accounted for using the equity method", EQUITY_METHOD, "¥bn", "Book value, 30 June 2026."),
    ("ofa", "Other financial assets, non-current", OTHER_FA, "¥bn", "Book value, 30 June 2026 (includes strategic shareholdings)."),
    ("nci", "Non-controlling interests", NCI, "¥bn", "30 June 2026. Deducted at book."),
    ("pens", "Retirement benefit liabilities", PENSION, "¥bn", "30 June 2026. Deducted."),
    ("cl26", "Contract liabilities, 30 June 2026", CL_JUN26, "¥bn", Q1 + ", presentation p8."),
    ("cl25", "Contract liabilities, 31 March 2025 (after the Logisnext reclassification)", CL_MAR25, "¥bn", FY + ", p12."),
    ("eps25", "FY2025 basic EPS", EPS25, "¥", "FY2025 Consolidated Financial Results, 12 May 2026."),
    ("eps26", "FY2026 EPS forecast (MHI)", EPS26G, "¥", Q1 + ". Unchanged from May."),
    ("cons26", "FY2026 consensus EPS (year to March 2027)", CONS_EPS_26, "¥", "stockanalysis.com (S&P Global data), retrieved 2 November 2026. Cross-check only."),
    ("constp", "Average analyst target", CONS_TP, "¥", "stockanalysis.com, 17 analysts, range ¥3,000 to ¥6,400. Cross-check only."),
    ("GROUP AND SEGMENTS (CONTINUING OPERATIONS, EXCLUDING MITSUBISHI LOGISNEXT)", None, None, None, None),
    ("grev26", "Group revenue, FY2026 forecast", GROUP["FY2026G"][1], "¥bn", Q1 + ", p16."),
    ("gbp26", "Group business profit, FY2026 forecast", GROUP["FY2026G"][2], "¥bn", Q1 + ", p16."),
    ("gni26", "Profit attributable to owners of the parent, FY2026 forecast", GROUP["FY2026G"][3], "¥bn", Q1 + ", p16."),
]
for k in SEGS:
    rows.append((f"r25_{k}", f"{SEG_NAMES[k]} revenue, FY2025 (restated)", REV25[k], "¥bn", Q1 + ", p17 (FY2025 restated for the April 2026 changes)."))
    rows.append((f"b25_{k}", f"{SEG_NAMES[k]} business profit, FY2025 (restated)", BP25[k], "¥bn", Q1 + ", p17."))
    rows.append((f"r26_{k}", f"{SEG_NAMES[k]} revenue, FY2026 forecast", REV26[k], "¥bn", Q1 + ", p17."))
    rows.append((f"b26_{k}", f"{SEG_NAMES[k]} business profit, FY2026 forecast", BP26[k], "¥bn", Q1 + ", p17."))
rows += [
    ("GTCC AND DEFENSE & SPACE", None, None, None, None),
    ("gt_r24", "GTCC revenue, FY2024", GT_REV[2], "¥bn", FY + ", p6."),
    ("gt_r25", "GTCC revenue, FY2025", GT_REV[3], "¥bn", FY + ", p6."),
    ("gt_r26", "GTCC revenue, FY2026 forecast", GT_REV[4], "¥bn", Q1 + ", p18."),
    ("gt_o24", "GTCC order intake, FY2024", GT_ORD[2], "¥bn", FY + ", p6."),
    ("gt_o25", "GTCC order intake, FY2025", GT_ORD[3], "¥bn", FY + ", p6."),
    ("gt_o26", "GTCC order intake, FY2026 forecast", GT_ORD[4], "¥bn", Q1 + ", p18. Raised from ¥2,300bn."),
    ("gt_bl25", "GTCC order backlog, March 2026 (lower bound)", GT_BACKLOG_FY25, "¥bn", FY + ", p6: \"order backlog surpassing ¥5 tr\"."),
    ("gt_q1o", "GTCC order intake, Q1 FY2026", GT_Q1_ORD[1], "¥bn", Q1 + ", p11."),
    ("gt_q1r", "GTCC revenue, Q1 FY2026", GT_Q1_REV[1], "¥bn", Q1 + ", p11."),
    ("ds_r26", "Defense & Space revenue, FY2026 forecast", DS_REV["FY2026G"], "¥bn", Q1 + ", p19."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("gt_m26", "GTCC business profit margin, FY2026", GT_M26, "%", "MY ASSUMPTION. MHI does not disclose GTCC profit; an analyst put it near 20% (Q&A, 6 August 2026)."),
    ("gt_g27", "GTCC revenue growth, FY2027", GT_G27, "%", "MY ASSUMPTION. Order book over ¥5tn; 30%+ more units by FY2028 (27 May 2026)."),
    ("gt_m27", "GTCC business profit margin, FY2027", GT_M27, "%", "MY ASSUMPTION. Higher-margin orders reaching revenue."),
    ("er_g27", "Energy Systems rest, revenue growth, FY2027", ER_G27, "%", "MY ASSUMPTION. Nuclear, steam power, aero engines, compressors."),
    ("er_m27", "Energy Systems rest, business profit margin, FY2027", ER_M27, "%", "MY ASSUMPTION. FY2026 derived 10.9%."),
    ("ads_g27", "Aircraft, Defense & Space revenue growth, FY2027", ADS_G27, "%", "MY ASSUMPTION. Revenue rising towards about ¥1.5tn of yearly defence orders."),
    ("ads_m27", "Aircraft, Defense & Space margin, FY2027", ADS_M27, "%", "MY ASSUMPTION. FY2026 forecast 11.3%."),
    ("pi27", "Plants & Infrastructure Systems business profit, FY2027", PI_BP27, "¥bn", "MY ASSUMPTION. FY2026 forecast ¥90bn."),
    ("is27", "Industrial Solutions business profit, FY2027", IS_BP27, "¥bn", "MY ASSUMPTION. FY2026 forecast ¥30bn."),
    ("corp27", "Others, Corporate & Eliminations, FY2027", CORP27, "¥bn", "MY ASSUMPTION. Flat on the FY2026 forecast."),
    ("adv_share", "Share of the prepayment build-up still to be spent on delivery", ADV_COST_SHARE, "%", "MY ASSUMPTION. One less a margin of about 20%."),
    ("x_gt", "Multiple, GTCC, EV / FY2027E business profit", MULT["GT"], "x", "MY ASSUMPTION. Between 18x used for Siemens Energy Gas Services and Siemens Energy's 26.4x trailing EV/EBIT."),
    ("x_er", "Multiple, Energy Systems rest", MULT["ER"], "x", "MY ASSUMPTION. Kawasaki Heavy 16.5x, IHI 14.2x trailing EV/EBIT."),
    ("x_pi", "Multiple, Plants & Infrastructure Systems", MULT["PI"], "x", "MY ASSUMPTION."),
    ("x_is", "Multiple, Industrial Solutions", MULT["IS"], "x", "MY ASSUMPTION."),
    ("x_ads", "Multiple, Aircraft, Defense & Space", MULT["ADS"], "x", "MY ASSUMPTION. European defence median 19.8x trailing EV/EBIT (Peers tab)."),
    ("x_corp", "Multiple, corporate costs (capitalised)", MULT["Corp"], "x", "MY ASSUMPTION. Near the blend of the parts."),
]
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY)
        r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else ("#,##0.000" if unit == "m" else (JPY2 if unit == "¥" else BN1)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  SEGMENTS
ws = sheet("Segments", "SEGMENTS: BUSINESS PROFIT, FY2025A TO FY2027E (¥ BILLION)", [44, 13, 13, 13, 13, 12, 12, 13, 13])
head(ws, 4, ["Part", "FY2025A revenue", "FY2026F revenue", "FY2025A profit", "FY2026F profit", "Growth*", "Margin*",
             "FY2027E revenue*", "FY2027E profit*"])
seg_rows = [  # label, r25, r26, b25, b26, growth, margin, r27, b27
    ("GTCC (my split of Energy Systems)", L("gt_r25"), L("gt_r26"), None, f"=C5*{A['gt_m26']}", L("gt_g27"), L("gt_m27"), "=C5*(1+F5)", "=H5*G5"),
    ("Energy Systems, rest", f"={A['r25_Energy']}-B5", f"={A['r26_Energy']}-C5", None, f"={A['b26_Energy']}-E5", L("er_g27"), L("er_m27"), "=C6*(1+F6)", "=H6*G6"),
    ("Plants & Infrastructure Systems", L("r25_PI"), L("r26_PI"), L("b25_PI"), L("b26_PI"), None, None, None, L("pi27")),
    ("Industrial Solutions", L("r25_IS"), L("r26_IS"), L("b25_IS"), L("b26_IS"), None, None, None, L("is27")),
    ("Aircraft, Defense & Space", L("r25_ADS"), L("r26_ADS"), L("b25_ADS"), L("b26_ADS"), L("ads_g27"), L("ads_m27"), "=C9*(1+F9)", "=H9*G9"),
    ("Others, Corporate & Eliminations", L("r25_Corp"), L("r26_Corp"), L("b25_Corp"), L("b26_Corp"), None, None, None, L("corp27")),
    ("Group total", "=SUM(B5:B10)", "=SUM(C5:C10)", f"=SUM(D7:D10)+{A['b25_Energy']}", "=SUM(E5:E10)", None, None, None, "=SUM(I5:I10)"),
]
for i, (lab, *vals) in enumerate(seg_rows):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B if lab == "Group total" else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v if v is not None else "")
        c.number_format = PCT1 if j in (4, 5) else BN1; c.alignment = RIGHT
        if isinstance(v, str) and v.startswith("=Assumptions"): c.font = F_LINK
ws["A13"] = "Check: FY2026 profit total against MHI's forecast"; ws["E13"] = "=E11-" + A["gbp26"]
ws["A14"] = "Check: FY2026 revenue total against MHI's forecast"; ws["C14"] = "=C11-" + A["grev26"]
ws["A15"] = "Net income per yen of business profit (MHI FY2026 forecast)"; ws["B15"] = f"={A['gni26']}/{A['gbp26']}"
ws["A16"] = "FY2027E net income, ¥bn"; ws["B16"] = "=I11*B15"
ws["A17"] = "FY2027E EPS, ¥"; ws["B17"] = "=B16/Valuation!D20*1000"
ws["A18"] = "P/E on FY2027E EPS at the reference price"; ws["B18"] = f"={A['price']}/B17"
ws["A19"] = "Energy Systems FY2026 forecast margin"; ws["B19"] = f"={A['b26_Energy']}/{A['r26_Energy']}"
ws["A20"] = "GTCC share of FY2026 forecast revenue"; ws["B20"] = f"=C5/{A['grev26']}"
ws["A21"] = "Defense & Space share of FY2026 forecast revenue"; ws["B21"] = f"={A['ds_r26']}/{A['grev26']}"
ws["A22"] = "GTCC share of FY2026 forecast business profit (my split)"; ws["B22"] = f"=E5/{A['gbp26']}"
ws["A23"] = "Aircraft, Defense & Space share of FY2026 forecast business profit"; ws["B23"] = f"=E9/{A['gbp26']}"
for c, f in [("E13", BN1), ("C14", BN1), ("B15", "0.000"), ("B16", BN1), ("B17", JPY2), ("B18", MULTF), ("B19", PCT1),
             ("B20", PCT1), ("B21", PCT1), ("B22", PCT1), ("B23", PCT1)]:
    ws[c].number_format = f
note(ws, 25, [
    "*Growth, margins and FY2027E are my own estimates. FY2025A and FY2026F are MHI's, restated for the April 2026 organisational changes.",
    "MHI does not disclose GTCC business profit. The GTCC split of Energy Systems profit is my estimate in every year; FY2025A is not split.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: SUM OF THE PARTS ON FY2027E BUSINESS PROFIT", [64, 14, 10, 16, 12, 60])
head(ws, 4, ["Part", "FY2027E profit", "Multiple", "Value, ¥bn", "Share", "Working / note"])
parts = [("GTCC", 5, "x_gt"), ("Energy Systems, rest", 6, "x_er"), ("Plants & Infrastructure Systems", 7, "x_pi"),
         ("Industrial Solutions", 8, "x_is"), ("Aircraft, Defense & Space", 9, "x_ads"), ("Corporate costs", 10, "x_corp")]
for i, (lab, srow, mk) in enumerate(parts):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f"=Segments!I{srow}"); c.font = F_LINK; c.number_format = BN1
    c = ws.cell(row=rr, column=3, value="=" + A[mk]); c.font = F_LINK; c.number_format = MULT0
    ws.cell(row=rr, column=4, value=f"=B{rr}*C{rr}").number_format = BN1
    ws.cell(row=rr, column=5, value=f"=D{rr}/$D$19").number_format = PCT0
vrows = [
    (11, "Enterprise value of the parts", "=SUM(D5:D10)", BN1, ""),
    (12, "Net cash: cash less interest-bearing debt, 30 June 2026", "=" + A["cash"] + "-" + A["debt"], BN1, "MHI reports net interest-bearing debt of minus ¥1,164.2bn."),
    (13, "Add equity-method investments and other financial assets at book", f"={A['eqm']}+{A['ofa']}", BN1, ""),
    (14, "Less non-controlling interests and retirement benefit liabilities", f"=-{A['nci']}-{A['pens']}", BN1, ""),
    (15, "Rise in contract liabilities since March 2025", f"={A['cl26']}-{A['cl25']}", BN1, "Customers' prepayments, mainly GTCC."),
    (16, "Less cost still to be spent on that rise", f"=-D15*{A['adv_share']}", BN1, "My treatment: the margin is already in my profit estimates."),
    (17, "Bridge from enterprise value to equity value", "=D12+D13+D14+D16", BN1, ""),
    (18, "Bridge if all net cash is counted as surplus", "=D12+D13+D14", BN1, "Cross-check."),
    (19, "Equity value, ¥bn", "=D11+D17", BN1, ""),
    (20, "Shares outstanding, m (issued less treasury, 30 June 2026)", "=" + A["issued"] + "-" + A["treas"], "#,##0.0", "No buybacks assumed."),
    (21, "BASE VALUE PER SHARE, ¥", "=D19/D20*1000", JPY0, ""),
    (22, "Reference price, ¥", L("price"), JPY0, f"TSE close, {PRICE_DATE}."),
    (23, "Base value against price", "=D21/D22-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (24, "VIEW ON THE BAND", '=IF(D23>=0.15,"LONG",IF(D23<=-0.25,"SHORT","NO CALL"))', None, f"{VIEWLBL}: {CALL['direction']}, {CALL['conviction']} conviction."),
    (25, "Base value counting all net cash as surplus, ¥", "=(D11+D18)/D20*1000", JPY0, ""),
    (26, "That value against price", "=D25/D22-1", PCT1, ""),
    (28, "Market value, ¥bn", "=D20*D22/1000", BN1, ""),
    (29, "Adjusted enterprise value at the price, ¥bn", "=D28-D17", BN1, "Market value less the bridge."),
    (30, "EV / FY2026 forecast business profit", "=D29/" + A["gbp26"], MULTF, ""),
    (31, "EV / FY2027E business profit", "=D29/Segments!I11", MULTF, ""),
    (32, "P/E on MHI's FY2026 EPS forecast", "=D22/" + A["eps26"], MULTF, ""),
    (33, "P/E on FY2026 consensus EPS", "=D22/" + A["cons26"], MULTF, "Cross-check only."),
    (34, "Value the price leaves for GTCC, ¥bn", "=D29-SUM(D6:D10)", BN1, "Rest of MHI at my base multiples."),
    (35, "That value / GTCC FY2027E profit", "=D34/B5", MULTF, ""),
    (36, "Value the price leaves for Aircraft, Defense & Space, ¥bn", "=D29-D11+D9", BN1, "GTCC and the rest at my base multiples."),
    (37, "That value / Aircraft, Defense & Space FY2027E profit", "=D36/B9", MULTF, ""),
    (38, "GTCC multiple needed for base value 15% above price", "=(D22*1.15*D20/1000-D17-SUM(D6:D10))/B5", MULTF, ""),
    (39, "Price at which the base value is 15% above it, ¥", "=D21/1.15", JPY0, "Revisit level for a LONG."),
    (40, "Price at which the base value is 25% below it, ¥", "=D21/0.75", JPY0, "Revisit level for a SHORT."),
    (41, "GTCC share of my equity value", "=D5/D19", PCT1, ""),
    (42, "Aircraft, Defense & Space share of my equity value", "=D9/D19", PCT1, ""),
    (43, "Price against the record close", "=D22/" + A["hiclose"] + "-1", PCT1, "¥5,195 on 2 March 2026."),
]
for rr, lab, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=4, value=f)
    if fmt: c.number_format = fmt
    if rr in (21, 24):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    if isinstance(f, str) and f.startswith("=Assumptions"): c.font = F_LINK
    ws.cell(row=rr, column=6, value=nt).alignment = WRAP
ws["E17"] = "=D17/$D$19"; ws["E17"].number_format = PCT0
ws["A11"].font = F_B; ws["A19"].font = F_B

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT", [12, 12, 12, 12, 13, 14, 14, 15, 13, 11])
head(ws, 4, ["Case", "GTCC growth", "GTCC margin", "GTCC multiple", "Other multiples +/-", "GTCC revenue ¥bn", "GTCC profit ¥bn",
             "Rest of MHI EV ¥bn", "Value, ¥", "vs price"])
r = 5
for name, g, m, mult, dlt, p in SCEN:
    ws.cell(row=r, column=1, value=name).font = F_B
    if name == "Base":
        for j, k in enumerate(["gt_g27", "gt_m27", "x_gt"]):
            c = ws.cell(row=r, column=2 + j, value="=" + A[k]); c.font = F_LINK
        c = ws.cell(row=r, column=5, value=0); c.font = F_INB; c.fill = FILL_ASSUME
    else:
        for j, v in enumerate([g, m, mult, dlt]):
            c = ws.cell(row=r, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME
    for col in (2, 3): ws.cell(row=r, column=col).number_format = PCT1
    ws.cell(row=r, column=4).number_format = MULT0; ws.cell(row=r, column=5).number_format = '+0;-0;0'
    ws.cell(row=r, column=6, value=f"=Segments!$C$5*(1+B{r})").number_format = BN1
    ws.cell(row=r, column=7, value=f"=F{r}*C{r}").number_format = BN1
    ws.cell(row=r, column=8, value=f"=SUMPRODUCT(Valuation!$B$6:$B$10,Valuation!$C$6:$C$10+E{r})").number_format = BN1
    ws.cell(row=r, column=9, value=f"=(G{r}*D{r}+H{r}+Valuation!$D$17)/Valuation!$D$20*1000").number_format = JPY0
    ws.cell(row=r, column=10, value=f"=I{r}/{A['price']}-1").number_format = PCT0
    r += 1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[5]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, ¥"; ws["A11"].font = F_B
ws["E11"] = "=B9*I5+C9*I6+D9*I7"; ws["E11"].number_format = JPY0; ws["E11"].font = F_B; ws["E11"].fill = FILL_KEY
ws["F11"] = f"=E11/{A['price']}-1"; ws["F11"].number_format = PCT1
note(ws, 13, [
    "GTCC cases start from MHI's FY2026 GTCC revenue forecast of ¥1,100bn. The rest of MHI keeps my FY2027E profit; only its multiples move,",
    "three turns lower in the bear case and two higher in the bull case (corporate costs included). Same bridge and shares in every case.",
    "Bear: world orders fall towards MHI's earlier 50 to 60 GW view, defence de-rates. Bull: the capacity step lands early and margins keep rising.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: GTCC FY2027E PROFIT AGAINST ITS MULTIPLE (¥)", [30, 14, 14, 14])
head(ws, 4, ["GTCC profit (¥bn) \\ multiple", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_MULT, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["x_gt"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (e, link) in enumerate(zip(SENS_GT, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value="=Segments!I5" if link else e)
    c.number_format = BN1; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j,
                value=f"=($A{rr}*{col}$4+SUM(Valuation!$D$6:$D$10)+Valuation!$D$17)/Valuation!$D$20*1000").number_format = JPY0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["Rest of MHI at my base. The middle row links to the model's GTCC FY2027E profit and the middle column to the base multiple."])

# =====================================================================  QUEUE
ws = sheet("Queue", "THE GAS TURBINE QUEUE: ORDERS, BACKLOG, UNITS, PREPAYMENTS", [58] + [11] * 8)
head(ws, 4, ["Large frame gas turbines (>100 MW) on order, units"] + UNIT_LABELS)
for j, v in enumerate(UNIT_BL):
    c = ws.cell(row=5, column=2 + j, value=v); c.font = F_IN
ws["A5"] = "Units on order at period end"; ws["A5"].font = F_B
ws["A6"] = "Growth, March 2025 to June 2026"; ws["B6"] = "=I5/D5-1"; ws["B6"].number_format = PCT1
ws["A8"] = "GTCC, ¥bn"; ws["A8"].font = Font(bold=True, color=NAVY)
head(ws, 9, ["", "FY2024", "FY2025", "FY2026F", "Q1 FY2026"])
qrows = [("Order intake", [L("gt_o24"), L("gt_o25"), L("gt_o26"), L("gt_q1o")]),
         ("Revenue", [L("gt_r24"), L("gt_r25"), L("gt_r26"), L("gt_q1r")]),
         ("Orders / revenue", ["=B10/B11", "=C10/C11", "=D10/D11", "=E10/E11"])]
for i, (lab, vals) in enumerate(qrows):
    rr = 10 + i
    ws.cell(row=rr, column=1, value=lab)
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v); c.number_format = '0.00"x"' if i == 2 else BN1
        if v.startswith("=Assumptions"): c.font = F_LINK
ws["A14"] = "GTCC backlog (over ¥5tn, March 2026) / FY2025 GTCC revenue, years"; ws["B14"] = f"={A['gt_bl25']}/{A['gt_r25']}"
ws["B14"].number_format = '0.0'
ws["A15"] = "Contract liabilities, March 2025 to June 2026, ¥bn"; ws["B15"] = L("cl25"); ws["C15"] = L("cl26"); ws["D15"] = "=C15-B15"
for c in ("B15", "C15", "D15"): ws[c].number_format = BN1
ws["A16"] = "World gas turbine orders for power, 2025 (GW) / MHI five-year average view (GW)"
ws["B16"] = MKT_GW_2025; ws["C16"] = MKT_GW_AVG; ws["B16"].font = F_IN; ws["C16"].font = F_IN
note(ws, 18, [
    "Sources: MHI presentations of 7 November 2025, 4 February 2026, 12 May 2026 and 4 August 2026 (large frame units and gigawatts:",
    "21 GW March 2025, 33 GW March 2026, 35 GW June 2026); FY2025 presentation p6 (GTCC history, backlog over ¥5tn, 96.1 GW courtesy McCoy Power Reports);",
    "2024 MTBP progress Q&A, 27 May 2026 (about 70 GW a year on average over the next five years).",
])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, RETRIEVED 2 NOVEMBER 2026)", [22, 14, 13, 18, 70])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "EV/EBIT (trailing)", "What they make"])
for i, (co, tk, pe, eve, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, v in enumerate([pe, eve]):
        c = ws.cell(row=rr, column=3 + j, value=v); c.number_format = MULTF; c.font = F_IN
    ws.cell(row=rr, column=5, value=what).alignment = WRAP
ws["A16"] = "European defence median (rows 8 to 11)"; ws["A16"].font = F_B
ws["C16"] = "=MEDIAN(C8:C11)"; ws["D16"] = "=MEDIAN(D8:D11)"
ws["A17"] = "Japanese peers median (rows 12 to 14)"; ws["A17"].font = F_B
ws["C17"] = "=MEDIAN(C12:C14)"; ws["D17"] = "=MEDIAN(D12:D14)"
for c in ("C16", "D16", "C17", "D17"): ws[c].number_format = MULTF
note(ws, 19, ["Multiples only, to set the range of segment multiples. No view on the peers' shares is expressed. GE Vernova's trailing",
              "EV/EBIT reflects earnings still recovering and is not used to set a multiple."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 140])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "MHI, Q1 FY2026 Financial Results presentation and Consolidated Financial Results, 4 August 2026: segments, main businesses, revised FY2026 forecast, balance sheet, shares, backlog, large frame units, FX.",
    "MHI, Q&A Summary, Q1 FY2026 Financial Results Briefing, dated 6 August 2026 (CFO Hiroshi Nishio): delivery timing, pricing, advances, capacity, one-off items, defence orders.",
    "MHI, FY2025 Financial Results presentation, Consolidated Financial Results and Q&A Summary, 12 May 2026: FY2025 results, GTCC and Defense & Space history, backlog over ¥5tn, advances, share, risk buffer.",
    "MHI, 2024 Medium-Term Business Plan Progress presentation and Q&A Summary, 27 May 2026: capacity (30%+ by FY2028, then about twice FY2024), demand outlook (96 GW in 2025, about 70 GW a year).",
    "MHI, 1H FY2025 (7 November 2025) and Q1-3 FY2025 (4 February 2026) presentations and Q&A summaries: unit backlog history, demand views.",
    "MHI investor relations page, mhi.com/finance: 1H FY2026 results scheduled for 6 November 2026, 13:30 JST.",
    "stockanalysis.com, TYO:7011 daily and monthly history (split-adjusted), retrieved 2 November 2026. Yahoo Finance chart API returned Too Many Requests and was not retried.",
    "stockanalysis.com, retrieved 2 November 2026: consensus EPS and average target (S&P Global data), peer forward P/E and trailing EV/EBIT.",
    "The Physical Layer, 'Building your own power', 22 September 2026: https://thephysicallayer.fyi/journal/building-your-own-power/",
    "Estimates for FY2027 and the GTCC profit split are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    (VIEWLBL, "=Valuation!D24", None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    ("Base value per share, ¥", "=Valuation!D21", JPY0, "Sum of the parts on FY2027E business profit, plus the bridge, over shares outstanding."),
    ("Reference price, ¥", "=" + A["price"], JPY0, f"TSE close, {PRICE_DATE}."),
    ("Base value against price", "=Valuation!D23", PCT1, ""),
    ("Probability-weighted value, ¥", "=Scenarios!E11", JPY0, "25 / 50 / 25 bear / base / bull."),
    ("GTCC share of my equity value", "=Valuation!D41", PCT1, ""),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
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
ws.row_dimensions[13].height = 32; ws.row_dimensions[14].height = 44
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Segments", "Business profit by part, FY2025A, FY2026 forecast, FY2027E; GTCC split; shares of revenue and profit."),
    ("Valuation", "Sum of the parts, the bridge with the prepayment adjustment, base value, the band, what the price implies."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "GTCC FY2027E profit against its multiple."),
    ("Queue", "Large frame units on order, GTCC orders against revenue, contract liabilities: the claim's tests."),
    ("Peers", "Forward P/E and trailing EV/EBIT used to set the multiples."),
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
print("model written", XLSX)
