"""Coherent Corp. (NYSE: COHR) initiation model. Quarterly build for fiscal 2027, annual to fiscal 2028E, non-GAAP EPS
bridge, P/E valuation. Live formulas throughout. Navy header rows, blue font for hardcoded inputs, yellow fill on my own
assumptions, green font for cross-sheet links, black for formulas.
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
USD0 = '"US$"#,##0'
M0 = '#,##0'
M1 = '#,##0.0'
PCT1 = '0.0%'
PCT0 = '0%'
MULTF = '0.0"x"'
MULT0 = '0"x"'
SUB = f"Tommy Lau | Coherent Corp. (NYSE: COHR) | {DATE} | " + ("DRAFT | " if CALL["draft"] else "") + "Personal research, not investment advice."

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
    elif isinstance(v, str) and v.startswith("=Assumptions"): c.font = F_LINK
    if fill: c.fill = fill
    c.alignment = RIGHT
    return c


# =====================================================================  COVER (filled last)
ws = sheet("Cover", "COHERENT CORP. (NYSE: COHR)  INITIATION MODEL" + ("  (DRAFT)" if CALL["draft"] else ""), [44, 26, 100])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [62, 14, 10, 110])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. US$ million unless stated. Fiscal year ends 30 June.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = set()
Q4R = "Q4 FY26 results release, Form 8-K Ex. 99.1, 12 August 2026"
K10 = "Form 10-K for the year to 30 June 2026, filed 14 August 2026"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "US$", "NYSE close, 30 October 2026. Nasdaq.com COHR history, retrieved 2 November 2026."),
    ("hiclose", "Highest close, 2 June 2026", HI_CLOSE, "US$", "Nasdaq.com. Intraday high US$440.00 on 3 June 2026."),
    ("pxdec", "Close, 31 December 2025", PX_DEC25, "US$", "Nasdaq.com."),
    ("nvpx", "Price Nvidia paid per share, 2 March 2026", NV_PRICE, "US$", "Form 8-K of 2 March 2026, Item 3.02: 7,788,161 shares for US$2bn."),
    ("shares_out", "Common shares outstanding, 10 August 2026", SHARES_OUT, "m", K10 + ", cover page: 195,832,246."),
    ("cash", "Cash and short-term investments, 30 June 2026", CASH, "US$m", Q4R + ": cash 1,162.0 + short-term investments 825.0. Restricted cash of 606.4 left out."),
    ("debt", "Debt, 30 June 2026", DEBT, "US$m", Q4R + ": current portion 7.9 + long-term debt 3,214.3."),
    ("nci", "Noncontrolling interests, 30 June 2026", NCI, "US$m", Q4R + "."),
    ("HISTORY (RELEASES; NON-GAAP AS RECAST)", None, None, None, None),
    ("rev24", "Revenue, FY24", REV["FY24"], "US$m", "Q4 FY25 results release, 13 August 2025."),
    ("rev25", "Revenue, FY25", REV["FY25"], "US$m", Q4R + "."),
    ("rev26", "Revenue, FY26", REV["FY26"], "US$m", Q4R + "."),
    ("dc25", "Datacenter & Communications revenue, FY25 (recast)", DC["FY25"], "US$m", Q4R + ", Table 5."),
    ("dc26", "Datacenter & Communications revenue, FY26", DC["FY26"], "US$m", Q4R + ", Table 5."),
    ("dcp25", "Datacenter & Communications segment profit, FY25", SEGP["DC"][0], "US$m", K10 + ", MD&A."),
    ("dcp26", "Datacenter & Communications segment profit, FY26", SEGP["DC"][1], "US$m", K10 + ", MD&A."),
    ("eps24", "Non-GAAP diluted EPS, FY24", NG_EPS["FY24"], "US$", "Derived: FY25 US$3.53 'improved $2.32' (Q4 FY25 release)."),
    ("eps25", "Non-GAAP diluted EPS, FY25", NG_EPS["FY25"], "US$", Q4R + "."),
    ("eps26", "Non-GAAP diluted EPS, FY26", NG_EPS["FY26"], "US$", Q4R + "."),
    ("gm25", "Non-GAAP gross margin, FY25", NG_GM["FY25"], "%", Q4R + "."),
    ("gm26", "Non-GAAP gross margin, FY26", NG_GM["FY26"], "%", Q4R + "."),
    ("opm25", "Non-GAAP operating margin, FY25", NG_OPM["FY25"], "%", Q4R + "."),
    ("opm26", "Non-GAAP operating margin, FY26", NG_OPM["FY26"], "%", Q4R + "."),
    ("GUIDANCE AND CONSENSUS", None, None, None, None),
    ("g_rev_lo", "Q1 FY27 revenue guide, low", G_REV[0], "US$m", Q4R + ", Business Outlook."),
    ("g_rev_hi", "Q1 FY27 revenue guide, high", G_REV[1], "US$m", Q4R + "."),
    ("g_eps_lo", "Q1 FY27 non-GAAP EPS guide, low", G_EPS[0], "US$", Q4R + "."),
    ("g_eps_hi", "Q1 FY27 non-GAAP EPS guide, high", G_EPS[1], "US$", Q4R + "."),
    ("cons27", "FY27 consensus non-GAAP EPS", CONS_EPS27, "US$", "stockanalysis.com (S&P Global), updated 30 October 2026. Cross-check only."),
    ("cons28", "FY28 consensus non-GAAP EPS", CONS_EPS28, "US$", "stockanalysis.com, as above. Cross-check only."),
    ("consrev27", "FY27 consensus revenue", CONS_REV27, "US$m", "stockanalysis.com, as above."),
    ("consrev28", "FY28 consensus revenue", CONS_REV28, "US$m", "stockanalysis.com, as above."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com: 26 analysts, low US$230, high US$500. Cross-check only."),
    ("MY ESTIMATES: FISCAL 2027 BY QUARTER", None, None, None, None),
]
for i, (r_, g_, o_) in enumerate(zip(F27_REV, F27_GM, F27_OPEX)):
    q = f"Q{i + 1} FY27"
    why = {0: "Guide 2,200 to 2,400; data centre growth above 80% year on year expected (call, 12 Aug 2026).",
           1: "First co-packaged optics revenue expected in the December quarter.",
           2: "Coherent targets internal InP output doubled by the end of 2026.",
           3: "Coherent expects a quarter above US$3bn by the end of FY27 (call); I assume it slips just short."}[i]
    rows += [(f"r{i}", f"{q} revenue", r_, "US$m", "MY ESTIMATE. " + why),
             (f"g{i}", f"{q} non-GAAP gross margin", g_, "%", "MY ESTIMATE. Guide Q1 39.5 to 41.5%; Coherent targets above 42%." if i == 0 else "MY ESTIMATE. Rising half a point a quarter towards the 42% target."),
             (f"o{i}", f"{q} non-GAAP operating expenses", o_, "US$m", "MY ESTIMATE. Q1 guide 400 to 420." if i == 0 else "MY ESTIMATE.")]
    MINE |= {f"r{i}", f"g{i}", f"o{i}"}
rows += [
    ("int27", "Non-GAAP interest and other expense, FY27", INT27, "US$m", "MY ESTIMATE. FY26 118.1; the Q1 guide implies about 30 a quarter."),
    ("tax", "Non-GAAP tax rate", TAX_NG, "%", "Coherent's normalised non-GAAP rate for FY26; Q1 FY27 guide 18 to 20%."),
    ("sh27", "Diluted shares, FY27 average", SH27, "m", "MY ESTIMATE. Q4 FY26 diluted 202.2m."),
    ("MY ASSUMPTIONS: FISCAL 2028 (BASE)", None, None, None, None),
    ("g28", "Revenue growth, FY28", G28, "%", "MY ASSUMPTION. Consensus implies 41% (14.69bn on 10.42bn); InP output to more than double again by end of calendar 2027."),
    ("gm28", "Non-GAAP gross margin, FY28", GM28, "%", "MY ASSUMPTION. Coherent's target is above 42%."),
    ("opex28", "Non-GAAP operating expenses, % of revenue, FY28", OPEX28, "%", "MY ASSUMPTION. FY26 19.0%; Q1 FY27 guide about 17.8% at the midpoints."),
    ("int28", "Non-GAAP interest and other expense, FY28", INT28, "US$m", "MY ASSUMPTION."),
    ("sh28", "Diluted shares, FY28 average", SH28, "m", "MY ASSUMPTION."),
    ("pe_base", "Base multiple, P/E on FY28E non-GAAP EPS", BASE_PE, "x", "MY ASSUMPTION. Coherent's own forward P/E averaged 24.3x at the ends of FY23 to FY25 (stockanalysis.com); peer median 30.4x; lower margins and the transceiver's CPO risk justify a discount."),
]
MINE |= {"int27", "sh27", "g28", "gm28", "opex28", "int28", "sh28", "pe_base"}
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY)
        r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else (M1 if unit == "m" else (USD2 if unit == "US$" else M0)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  QUARTERS
ws = sheet("Quarters", "QUARTERS: FY25 AND FY26 ACTUAL, FY27 MY ESTIMATES (US$ MILLION)", [40] + [11] * 12)
qh = Q + ["Q1 FY27E", "Q2 FY27E", "Q3 FY27E", "Q4 FY27E"]
head(ws, 4, ["US$ million"] + qh)
labs = ["Revenue", "  Datacenter & Communications", "  Industrial", "  D&C share of revenue", "Non-GAAP gross margin",
        "Non-GAAP gross profit", "Non-GAAP operating expenses", "Non-GAAP operating income", "Non-GAAP operating margin",
        "Non-GAAP diluted EPS, US$", "GAAP gross margin"]
for i, l in enumerate(labs):
    ws.cell(row=5 + i, column=1, value=l).font = F_B if i in (0, 7, 9) else Font()
for j in range(8):
    col = get_column_letter(2 + j)
    put(ws, f"{col}5", Q_REV[j], M1, F_IN); put(ws, f"{col}6", Q_DC[j], M1, F_IN)
    put(ws, f"{col}7", f"={col}5-{col}6", M1); put(ws, f"{col}8", f"={col}6/{col}5", PCT1)
    put(ws, f"{col}9", Q_NGGM[j] / 100, PCT1, F_IN); put(ws, f"{col}10", f"={col}5*{col}9", M1)
    put(ws, f"{col}13", Q_NGOPM[j] / 100, PCT1, F_IN); put(ws, f"{col}12", f"={col}5*{col}13", M1)
    put(ws, f"{col}11", f"={col}10-{col}12", M1)
    put(ws, f"{col}14", Q_EPS[j], USD2, F_IN); put(ws, f"{col}15", Q_GAAPGM[j] / 100, PCT1, F_IN)
for j in range(4):
    col = get_column_letter(10 + j)
    put(ws, f"{col}5", L(f"r{j}"), M1); put(ws, f"{col}9", L(f"g{j}"), PCT1)
    put(ws, f"{col}10", f"={col}5*{col}9", M1); put(ws, f"{col}11", L(f"o{j}"), M1)
    put(ws, f"{col}12", f"={col}10-{col}11", M1); put(ws, f"{col}13", f"={col}12/{col}5", PCT1)
put(ws, "J14", f"=(J12-{A['int27']}/4)*(1-{A['tax']})/203.5", USD2)
ws["A17"] = "Q1 FY27 EPS guide midpoint, US$"; put(ws, "J17", f"=({A['g_eps_lo']}+{A['g_eps_hi']})/2", USD2)
ws["A18"] = "Q1 FY27 revenue guide midpoint"; put(ws, "J18", f"=({A['g_rev_lo']}+{A['g_rev_hi']})/2", M1)
ws["A19"] = "FY26 revenue growth, D&C"; put(ws, "B19", f"={A['dc26']}/{A['dc25']}-1", PCT1)
note(ws, 21, [
    "Sources: Coherent quarterly results releases, Form 8-K Ex. 99.1, 6 November 2024 to 12 August 2026. FY25 non-GAAP margins and EPS as recast in the FY26 releases.",
    "Operating expenses and gross profit for actual quarters are derived from the reported margins. Q1 FY27E EPS uses 203.5m diluted shares (my estimate).",
    "FY27 quarters are my estimates. Coherent does not split datacenter from communications revenue in its releases.",
])

# =====================================================================  ANNUAL
ws = sheet("Annual", "ANNUAL: FY24A TO FY28E, NON-GAAP EPS BRIDGE (US$ MILLION UNLESS STATED)", [50, 13, 13, 13, 13, 13])
head(ws, 4, ["", "FY24A", "FY25A", "FY26A", "FY27E*", "FY28E*"])
labs = ["Revenue", "Growth", "Non-GAAP gross margin", "Non-GAAP operating income", "Non-GAAP operating margin",
        "Interest and other expense", "Pre-tax", "Tax", "Non-GAAP net income", "Diluted shares, m", "NON-GAAP EPS, US$",
        "Growth", "Consensus EPS, US$", "Mine against consensus", "Consensus revenue", "Mine against consensus"]
for i, l in enumerate(labs):
    ws.cell(row=5 + i, column=1, value=l).font = F_B if i in (0, 10) else Font()
put(ws, "B5", L("rev24"), M0); put(ws, "C5", L("rev25"), M0); put(ws, "D5", L("rev26"), M0)
put(ws, "E5", "=SUM(Quarters!J5:M5)", M0, F_LINK); put(ws, "F5", f"=E5*(1+{A['g28']})", M0)
for col, prev in [("C", "B"), ("D", "C"), ("E", "D"), ("F", "E")]:
    put(ws, f"{col}6", f"={col}5/{prev}5-1", PCT1)
put(ws, "C7", L("gm25"), PCT1); put(ws, "D7", L("gm26"), PCT1)
put(ws, "E7", "=SUM(Quarters!J10:M10)/E5", PCT1, F_LINK); put(ws, "F7", L("gm28"), PCT1)
put(ws, "C9", L("opm25"), PCT1); put(ws, "D9", L("opm26"), PCT1)
put(ws, "C8", "=C5*C9", M0); put(ws, "D8", "=D5*D9", M0)
put(ws, "E8", "=SUM(Quarters!J12:M12)", M0, F_LINK); put(ws, "E9", "=E8/E5", PCT1)
put(ws, "F9", f"={A['gm28']}-{A['opex28']}", PCT1); put(ws, "F8", "=F5*F9", M0)
for col, intk, shk in [("E", "int27", "sh27"), ("F", "int28", "sh28")]:
    put(ws, f"{col}10", "=-" + A[intk], M0, F_LINK)
    put(ws, f"{col}11", f"={col}8+{col}10", M0)
    put(ws, f"{col}12", f"=-{col}11*{A['tax']}", M0, F_LINK)
    put(ws, f"{col}13", f"={col}11+{col}12", M0)
    put(ws, f"{col}14", L(shk), M1)
    put(ws, f"{col}15", f"={col}13/{col}14", USD2, F_B, FILL_KEY)
put(ws, "B15", L("eps24"), USD2); put(ws, "C15", L("eps25"), USD2); put(ws, "D15", L("eps26"), USD2)
for col, prev in [("C", "B"), ("D", "C"), ("E", "D"), ("F", "E")]:
    put(ws, f"{col}16", f"={col}15/{prev}15-1", PCT1)
put(ws, "E17", L("cons27"), USD2); put(ws, "F17", L("cons28"), USD2)
put(ws, "E18", "=E15/E17-1", PCT1); put(ws, "F18", "=F15/F17-1", PCT1)
put(ws, "E19", L("consrev27"), M0); put(ws, "F19", L("consrev28"), M0)
put(ws, "E20", "=E5/E19-1", PCT1); put(ws, "F20", "=F5/F19-1", PCT1)
ws["A22"] = "Datacenter & Communications share of revenue, FY26"; put(ws, "D22", f"={A['dc26']}/{A['rev26']}", PCT1)
ws["A23"] = "D&C segment profit margin, FY25 / FY26"; put(ws, "C23", f"={A['dcp25']}/{A['dc25']}", PCT1); put(ws, "D23", f"={A['dcp26']}/{A['dc26']}", PCT1)
note(ws, 25, [
    "*My estimates. FY27E sums the Quarters tab. FY24A to FY26A as reported; FY24 and FY25 non-GAAP as recast by Coherent.",
    "Non-GAAP excludes share-based pay (US$193.8m in FY26), amortisation of acquired intangibles, restructuring and other items, as Coherent defines it.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: P/E ON FY28E NON-GAAP EPS, TWELVE MONTHS OUT", [64, 16, 70])
head(ws, 4, ["Item", "Value", "Working / note"])
vrows = [
    (5, "FY28E non-GAAP EPS, US$", "=Annual!F15", USD2, "My estimate. By October 2027 the market prices the year to June 2028."),
    (6, "Base multiple", L("pe_base"), MULTF, "Below Coherent's 24.3x FY23 to FY25 average and the 30.4x peer median."),
    (7, "BASE VALUE PER SHARE, US$", "=B5*B6", USD2, ""),
    (8, "Reference price, US$", L("price"), USD2, "NYSE close, 30 October 2026."),
    (9, "Base value against price", "=B7/B8-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (10, "VIEW ON THE BAND", '=IF(B9>=0.15,"LONG",IF(B9<=-0.25,"SHORT","NO CALL"))', None, "Draft view only; Tommy Lau decides the call." if CALL["draft"] else "The band's answer; the call is Tommy Lau's."),
    (11, ("Draft target" if CALL["draft"] else "Target") + ", US$ (base value rounded down)", CALL["target"] or "", USD2, "Judgement."),
    (12, "Target against price", "=IF(B11=\"\",\"\",B11/B8-1)", PCT1, ""),
    (14, "Market value, US$bn", f"={A['shares_out']}*B8/1000", '#,##0.00', "Shares outstanding at 10 August 2026."),
    (15, "Net debt, US$m, 30 June 2026", f"={A['debt']}-{A['cash']}", M0, "Restricted cash excluded."),
    (16, "Enterprise value, US$bn", f"=B14+(B15+{A['nci']})/1000", '#,##0.00', ""),
    (17, "P/E on FY26 non-GAAP EPS", f"=B8/{A['eps26']}", MULTF, ""),
    (18, "P/E on FY27 consensus", f"=B8/{A['cons27']}", MULTF, "stockanalysis.com."),
    (19, "P/E on FY28 consensus", f"=B8/{A['cons28']}", MULTF, "stockanalysis.com."),
    (20, "P/E on FY27E (mine)", "=B8/Annual!E15", MULTF, ""),
    (21, "P/E on FY28E (mine)", "=B8/Annual!F15", MULTF, ""),
    (22, "FY28 EPS the price needs at the base multiple, US$", "=B8/B6", USD2, "What the price assumes."),
    (23, "That EPS against my FY27E", "=B22/Annual!E15-1", PCT1, ""),
    (24, "Price below which the base value is 15% or more above it, US$", "=B7/1.15", USD2, ""),
    (25, "Price above which the base value is 25% or more below it, US$", "=B7/0.75", USD2, ""),
    (26, "Price against the highest close", f"=B8/{A['hiclose']}-1", PCT1, "Close of US$426.89, 2 June 2026."),
    (27, "Price change in 2026 to date", f"=B8/{A['pxdec']}-1", PCT1, ""),
    (28, "Price against Nvidia's purchase price", f"=B8/{A['nvpx']}-1", PCT1, ""),
    (29, "Average analyst target against price", f"={A['constp']}/B8-1", PCT1, "Cross-check only."),
]
for rr, lab, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    if rr in (7, 10):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    elif isinstance(f, str) and (f.startswith("=Assumptions") or f.startswith("=Annual")): c.font = F_LINK
    elif rr == 11: c.font = F_INB; c.fill = FILL_ASSUME
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (VALUE = MULTIPLE x FY28E NON-GAAP EPS)", [10, 13, 13, 13, 11, 14, 14, 13, 13, 11])
head(ws, 4, ["Case", "FY28 growth", "Gross margin", "Opex / revenue", "Multiple", "FY28 revenue", "Operating income",
             "FY28E EPS", "Value, US$", "vs price"])
r = 5
for s in SCEN:
    name, g, gm, ox, mult, p = s
    ws.cell(row=r, column=1, value=name).font = F_B
    if name == "Base":
        for j, k in enumerate(["g28", "gm28", "opex28", "pe_base"]):
            c = ws.cell(row=r, column=2 + j, value="=" + A[k]); c.font = F_LINK
    else:
        for j, v in enumerate([g, gm, ox, mult]):
            c = ws.cell(row=r, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME
    for col in range(2, 5): ws.cell(row=r, column=col).number_format = PCT1
    ws.cell(row=r, column=5).number_format = MULT0
    ws.cell(row=r, column=6, value=f"=Annual!$E$5*(1+B{r})").number_format = M0
    ws.cell(row=r, column=7, value=f"=F{r}*(C{r}-D{r})").number_format = M0
    ws.cell(row=r, column=8, value=f"=(G{r}-{A['int28']})*(1-{A['tax']})/{A['sh28']}").number_format = USD2
    ws.cell(row=r, column=9, value=f"=H{r}*E{r}").number_format = USD2
    ws.cell(row=r, column=10, value=f"=I{r}/{A['price']}-1").number_format = PCT1
    r += 1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[5]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, US$"; ws["A11"].font = F_B
ws["E11"] = "=B9*I5+C9*I6+D9*I7"; ws["E11"].number_format = USD2; ws["E11"].font = F_B; ws["E11"].fill = FILL_KEY
ws["F11"] = f"=E11/{A['price']}-1"; ws["F11"].number_format = PCT1
ws["A12"] = "Check: base case equals the Valuation tab"; ws["E12"] = "=I6-Valuation!B7"; ws["E12"].number_format = '0.000'
note(ws, 14, [
    "All cases start from my FY27E revenue of the Quarters tab and use the same interest, tax and share count.",
    "Bear: new InP capacity across the industry meets a customer inventory pause, as in FY24 when revenue fell 9%; flat revenue, gross margin 37.5%, opex 18%; 14x.",
    "Bull: the plug stays and 1.6T and 3.2T both ramp on time; growth 40%, close to consensus; gross margin 43.5%, opex 16%; 28x, still below the peer median.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: FY28E NON-GAAP EPS AGAINST THE P/E (US$)", [30, 14, 14, 14])
head(ws, 4, ["FY28E EPS \\ P/E", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_PE, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["pe_base"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (e, link) in enumerate(zip(SENS_EPS, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value="=Annual!F15" if link else e)
    c.number_format = USD2; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=f"=$A{rr}*{col}$4").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["The middle row links to the model's FY28E EPS and the middle column to the base multiple."])

# =====================================================================  CASH
ws = sheet("Cash", "CASH, INVENTORY AND COMMITMENTS: THE BET ON VOLUME", [56, 13, 13, 13])
head(ws, 4, ["US$ million", "FY24", "FY25", "FY26"])
ws["A5"] = "Operating cash flow"; ws["A6"] = "Capital spending"; ws["A7"] = "Free cash flow"
ws["A8"] = "Inventory, 30 June"; ws["A9"] = "Accounts payable, 30 June"; ws["A10"] = "Inventory growth"
for j, y in enumerate(["FY24", "FY25", "FY26"]):
    col = get_column_letter(2 + j)
    put(ws, f"{col}5", OCF[y], M1, F_IN); put(ws, f"{col}6", CAPEX[y], M1, F_IN); put(ws, f"{col}7", f"={col}5-{col}6", M1)
for y, col in [("FY25", "C"), ("FY26", "D")]:
    put(ws, f"{col}8", INVENTORY[y], M1, F_IN); put(ws, f"{col}9", PAYABLES[y], M1, F_IN)
put(ws, "D10", "=D8/C8-1", PCT1)
ws["A12"] = "Purchase commitments due in FY27, US$bn"; put(ws, "B12", PURCH_27, '0.0', F_IN)
ws["A13"] = "Purchase commitments due after FY27, US$bn"; put(ws, "B13", PURCH_LATER, '0.0', F_IN)
note(ws, 15, ["Sources: Q4 FY26 release and Form 10-K (cash flow statement, balance sheet, Note 13); FY24 from the FY26 10-K cash flow statement."])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, 30 OCTOBER 2026 CLOSE)", [26, 16, 13, 76])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "What they make"])
for i, (co, tk, pe, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    c = ws.cell(row=rr, column=3, value=pe); c.number_format = MULTF; c.font = F_IN
    ws.cell(row=rr, column=4, value=what).alignment = WRAP
last = 4 + len(PEERS)
ws[f"A{last + 2}"] = "Peer median (excluding Coherent)"; ws[f"A{last + 2}"].font = F_B
ws[f"C{last + 2}"] = f"=MEDIAN(C6:C{last})"
ws[f"A{last + 3}"] = "Coherent forward P/E, FY23 to FY25 year ends, average"; ws[f"A{last + 3}"].font = F_B
ws[f"C{last + 3}"] = f"=AVERAGE({','.join(str(v) for v in HIST_FWD_PE.values())})"
for c in (f"C{last + 2}", f"C{last + 3}"): ws[c].number_format = MULTF
note(ws, last + 5, ["Multiples only, to set the range of multiples. No view on the peers' shares is expressed. Coherent's history:",
                    "25.1x, 26.5x, 21.3x at the ends of FY23 to FY25, and 53.0x at the end of FY26 (stockanalysis.com)."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 150])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Coherent Q4 FY26 results release, Form 8-K Ex. 99.1, 12 August 2026: income statement, non-GAAP reconciliation, balance sheet, cash flow, segment revenue, Q1 FY27 outlook.",
    "Coherent Q4 FY26 investor presentation, Form 8-K Ex. 99.2, 12 August 2026: quarterly segment revenue; InP output doubling by end of 2026 and more than doubling again by 2027; 6-inch InP lines making EMLs, CW lasers and photodiodes at higher yields than 3-inch; CPO/NPO revenue from the second half of 2026; 1.6T, 3.2T and 6.4T transceivers.",
    "Coherent Form 10-K for the year to 30 June 2026, filed 14 August 2026: shares outstanding, segment profit, customer concentration, purchase commitments, Sherman expansion, Nvidia agreement and share issue, BIS inquiry.",
    "Coherent quarterly results releases, Form 8-K Ex. 99.1, 6 November 2024, 5 February 2025, 7 May 2025, 13 August 2025, 5 November 2025, 4 February 2026 and 6 May 2026.",
    "Coherent Form 8-K of 2 March 2026 (Item 3.02 and Ex. 99.1): Nvidia's US$2bn investment at US$256.80 a share; multi-billion-dollar purchase commitment; five additional product families related to co-packaged optics.",
    "Coherent Form 8-K of 31 August 2026: special performance share awards with price hurdles of US$454.43 to US$757.77.",
    "Coherent release of 14 October 2026 (GlobeNewswire): Q1 FY27 results on 4 November 2026 after the NYSE close.",
    "Coherent Q4 FY26 call (12 August 2026), third-party transcript published by stockanalysis.com: InP lasers up about 80%, data centre growth above 80% expected in Q1 FY27, 1.6T ramp pulled in, gross margin target above 42%, US$3bn quarter by end FY27, LTA terms.",
    "Nasdaq.com COHR historical prices, retrieved 2 November 2026; Yahoo Finance chart API used as a cross-check.",
    "stockanalysis.com (S&P Global Market Intelligence data), updated 30 October 2026: consensus revenue and EPS, average target, forward P/E for Coherent and peers.",
    "The Physical Layer, 'How ten thousand chips talk: the glass stays, and the plug survives its replacement': https://thephysicallayer.fyi/journal/ten-thousand-chips-one-thought/",
    "Estimates for FY27 and FY28 are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    (("Draft view (Tommy Lau decides the call)" if CALL["draft"] else "Call (Tommy Lau)"), "=Valuation!B10" if CALL["draft"] else CALL["direction"], None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (("Draft conviction" if CALL["draft"] else "Conviction"), CALL["conviction"], None, "Judgement, not formula."),
    (("Draft target, US$" if CALL["draft"] else "Target, US$"), "=Valuation!B11", USD2, "Base value rounded down."),
    ("Base value per share, US$", "=Valuation!B7", USD2, "Base multiple x FY28E non-GAAP EPS."),
    ("Reference price, US$", "=" + A["price"], USD2, "NYSE close, 30 October 2026."),
    ("Base value against price", "=Valuation!B9", PCT1, ""),
    ("Probability-weighted value, US$", "=Scenarios!E11", USD2, "25 / 50 / 25 bear / base / bull."),
    ("FY28E non-GAAP EPS, US$", "=Annual!F15", USD2, "My estimate."),
    ("Horizon", "12 months, to October 2027", None, ""),
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
ws.row_dimensions[14].height = 58
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Quarters", "FY25 and FY26 by quarter; my FY27 by quarter."),
    ("Annual", "FY24A to FY28E and the bridge to non-GAAP EPS; against consensus."),
    ("Valuation", "Base value, the band, multiples at the price, what the price needs."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "FY28E EPS against the multiple."),
    ("Cash", "Operating cash flow, capital spending, inventory and purchase commitments."),
    ("Peers", "Forward P/E used to set the multiple."),
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
