"""Eaton Corporation plc (NYSE: ETN) initiation model. Segment build to 2028E, adjusted EPS bridge, P/E valuation.
Live formulas throughout. House style follows the Vertiv and Hitachi models: navy header rows, blue font for hardcoded
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
USD0 = '"US$"#,##0'
M0 = '#,##0'
M1 = '#,##0.0'
PCT1 = '0.0%'
PCT0 = '0%'
MULTF = '0.0"x"'
MULT0 = '0"x"'
SUB = f"Tommy Lau | Eaton Corporation plc (NYSE: ETN) | {DATE} | Personal research, not investment advice."

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
ws = sheet("Cover", "EATON CORPORATION PLC (NYSE: ETN)  INITIATION MODEL", [42, 24, 100])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [60, 14, 10, 110])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. US$ million unless stated. Year end 31 December.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = set()
Q2R = "Q2 2026 earnings release, Form 8-K Ex. 99, 31 July 2026"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "US$", "NYSE close, 23 October 2026. Yahoo Finance ETN, retrieved 26 October 2026."),
    ("hiclose", "Highest close, 12 August 2026", HI_CLOSE, "US$", "Yahoo Finance. Intraday high US$478.00 the same day."),
    ("pxdec", "Close, 31 December 2025", PX_DEC25, "US$", "Yahoo Finance."),
    ("shares_out", "Ordinary shares outstanding, 30 June 2026", SHARES_OUT, "m", "Form 10-Q, quarter to 30 June 2026."),
    ("shares_dil", "Diluted weighted shares, Q2 2026", SHARES_DIL, "m", Q2R + "."),
    ("cash", "Cash and short-term investments, 30 June 2026", CASH, "US$m", Q2R + ": cash 483 + short-term investments 212."),
    ("debt", "Debt, 30 June 2026", DEBT, "US$m", Q2R + ": short-term debt 2,091 + current portion 11 + long-term debt 18,509."),
    ("nci", "Noncontrolling interests, 30 June 2026", NCI, "US$m", Q2R + "."),
    ("GUIDANCE AND CONSENSUS", None, None, None, None),
    ("g_lo", "2026 adjusted EPS guide, low", GUIDE26["eps_lo"], "US$", Q2R + ". Raised from US$13.05 to 13.50 in May."),
    ("g_hi", "2026 adjusted EPS guide, high", GUIDE26["eps_hi"], "US$", Q2R + "."),
    ("eps24", "2024 adjusted EPS", ADJ_EPS["2024A"], "US$", "Q4 2025 earnings release."),
    ("eps25", "2025 adjusted EPS", ADJ_EPS["2025A"], "US$", Q2R + ", reconciliation."),
    ("cons26", "2026 consensus adjusted EPS", CONS_EPS26, "US$", "stockanalysis.com (S&P Global), updated 20 October 2026, retrieved 26 October 2026. Cross-check only."),
    ("cons27", "2027 consensus adjusted EPS", CONS_EPS27, "US$", "stockanalysis.com, as above. May include Mobility for part of the year. Cross-check only."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com: 28 analysts, low US$333, high US$534. Cross-check only."),
    ("SEGMENTS, ACTUAL (EATON RELEASES)", None, None, None, None),
]
for k, nm in [("EA", "Electrical Americas"), ("EG", "Electrical Global"), ("AE", "Aerospace"), ("MO", "Mobility (Vehicle + eMobility)")]:
    s24 = {"EA": (11436, 3455), "EG": (6248, 1149), "AE": (3744, 859), "MO": (2790 + 662, 502 - 7)}[k]
    rows += [
        (f"s24_{k}", f"{nm} sales, 2024", s24[0], "US$m", "Q4 2024 earnings release, 31 January 2025."),
        (f"p24_{k}", f"{nm} operating profit, 2024", s24[1], "US$m", "Q4 2024 earnings release."),
        (f"s25_{k}", f"{nm} sales, 2025", SEG25[k][0], "US$m", "Q4 2025 earnings release and 2025 Form 10-K."),
        (f"p25_{k}", f"{nm} operating profit, 2025", SEG25[k][1], "US$m", "Q4 2025 earnings release."),
        (f"h1s_{k}", f"{nm} sales, first half 2026", H1[k][0], "US$m", Q2R + "."),
        (f"h1p_{k}", f"{nm} operating profit, first half 2026", H1[k][1], "US$m", Q2R + "."),
    ]
rows += [
    ("h1corp", "Corporate other expense excluding acquisition charges, first half 2026", H1_CORP, "US$m", "Derived: other expense net 655 less acquisition and divestiture charges 263 (Q2 release, Note 4)."),
    ("h1int", "Interest expense net, first half 2026", H1_INT, "US$m", Q2R + "."),
    ("MY ESTIMATES: SECOND HALF OF 2026", None, None, None, None),
]
for k, nm, why in [("EA", "Electrical Americas", "Q3 3,990 and Q4 4,100: about 17% growth on the same quarters of 2025, near Q2's 18% organic."),
                   ("EG", "Electrical Global", "2,450 a quarter: about 16% organic plus Boyd Thermal at Q2's level."),
                   ("AE", "Aerospace", "Q3 1,230 and Q4 1,255: 7% organic plus Ultra PCS."),
                   ("MO", "Mobility", "780 and 760: flat to slightly down.")]:
    rows += [(f"h2s_{k}", f"{nm} sales, second half 2026", H2[k][0], "US$m", "MY ESTIMATE. " + why),
             (f"h2m_{k}", f"{nm} operating margin, second half 2026", H2[k][1], "%", "MY ESTIMATE." + (
                 " Back to its 2025 level as Eaton guides price and cost to roughly neutral in the second half; Q3 2025 was 30.3%." if k == "EA" else ""))]
    MINE |= {f"h2s_{k}", f"h2m_{k}"}
rows += [
    ("corp26", "Corporate other expense excluding charges, 2026", CORP26, "US$m", "MY ESTIMATE. First half 392."),
    ("int26", "Interest expense net, 2026", INT26, "US$m", "MY ESTIMATE. First half 307; about 200 a quarter after the Boyd Thermal debt."),
    ("pens", "Pension and other postretirement income", PENS, "US$m", "MY ESTIMATE."),
    ("tax", "Tax rate on adjusted pre-tax profit", TAX, "%", "MY ESTIMATE. About 18% in 2025 and 22% in the first half of 2026 by my arithmetic; 19% reproduces the 2026 guide midpoint."),
    ("nci_inc", "Net income to noncontrolling interests", NCI_INC, "US$m", "MY ESTIMATE."),
    ("MY ASSUMPTIONS: 2027 AND 2028, CONTINUING OPERATIONS (MOBILITY OUT, PRO FORMA FROM 1 JANUARY 2027)", None, None, None, None),
    ("ea_g27", "Electrical Americas sales growth, 2027", EA_G27, "%", "MY ASSUMPTION. Near the 2026 pace; 12.6 months of sales already on order at June 2026."),
    ("ea_g28", "Electrical Americas sales growth, 2028", EA_G28, "%", "MY ASSUMPTION. New plants add capacity from 2027."),
    ("ea_m27", "Electrical Americas operating margin, 2027", EA_M27, "%", "MY ASSUMPTION. 2025 level was 29.9%."),
    ("ea_m28", "Electrical Americas operating margin, 2028", EA_M28, "%", "MY ASSUMPTION."),
    ("eg_g27", "Electrical Global organic growth, 2027", EG_G27, "%", "MY ASSUMPTION."),
    ("boyd", "Boyd Thermal sales against the 2026 stub period", BOYD_STUB, "US$m", "MY ESTIMATE. Boyd closed 12 March 2026; it added 25% to Q2 Electrical Global sales (about 440 a quarter)."),
    ("eg_g28", "Electrical Global growth, 2028", EG_G28, "%", "MY ASSUMPTION."),
    ("eg_m27", "Electrical Global operating margin, 2027", EG_M27, "%", "MY ASSUMPTION. Q2 2026 19.8%."),
    ("eg_m28", "Electrical Global operating margin, 2028", EG_M28, "%", "MY ASSUMPTION."),
    ("ae_g27", "Aerospace growth, 2027", AE_G27, "%", "MY ASSUMPTION."),
    ("ae_g28", "Aerospace growth, 2028", AE_G28, "%", "MY ASSUMPTION."),
    ("ae_m27", "Aerospace operating margin, 2027", AE_M27, "%", "MY ASSUMPTION. First half 2026 24.6%."),
    ("ae_m28", "Aerospace operating margin, 2028", AE_M28, "%", "MY ASSUMPTION."),
    ("corp27", "Corporate other expense, 2027", CORP27, "US$m", "MY ASSUMPTION."),
    ("corp28", "Corporate other expense, 2028", CORP28, "US$m", "MY ASSUMPTION."),
    ("int27", "Interest expense net, 2027", INT27, "US$m", "MY ASSUMPTION. Debt repaid from the ~US$1.1bn Dana cash and free cash flow after dividends."),
    ("int28", "Interest expense net, 2028", INT28, "US$m", "MY ASSUMPTION."),
    ("retired", "Eaton shares retired in the Mobility exchange offer", SHARES_RETIRED, "m", "MY ASSUMPTION. Mobility valued at ~US$5.1bn less ~US$1.1bn cash leaves ~US$4.0bn of combined-company shares for Eaton holders; a split-off at a ~7% discount retires about 10m Eaton shares. Zero if it becomes a pro rata spin-off. No other buybacks."),
    ("pe_base", "Base multiple, P/E on 2028E adjusted EPS", BASE_PE, "x", "MY ASSUMPTION. Eaton's own forward P/E averaged 24.0x for 2021 to 2025 (stockanalysis.com); one turn lower; peer median 20.5x."),
]
MINE |= {"corp26", "int26", "pens", "tax", "nci_inc", "ea_g27", "ea_g28", "ea_m27", "ea_m28", "eg_g27", "boyd", "eg_g28",
         "eg_m27", "eg_m28", "ae_g27", "ae_g28", "ae_m27", "ae_m28", "corp27", "corp28", "int27", "int28", "retired", "pe_base"}
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

# =====================================================================  SEGMENTS
ws = sheet("Segments", "SEGMENTS: SALES AND OPERATING PROFIT, 2024A TO 2028E (US$ MILLION)", [46, 13, 13, 13, 13, 13])
head(ws, 4, ["US$ million", "2024A", "2025A", "2026E*", "2027E*", "2028E*"])
SR = {}
r = 5
for k, nm, g27, g28, m27, m28, extra in [("EA", "Electrical Americas", "ea_g27", "ea_g28", "ea_m27", "ea_m28", ""),
                                         ("EG", "Electrical Global", "eg_g27", "eg_g28", "eg_m27", "eg_m28", "+" + A["boyd"]),
                                         ("AE", "Aerospace", "ae_g27", "ae_g28", "ae_m27", "ae_m28", ""),
                                         ("MO", "Mobility (to be combined with Dana, Q1 2027)", None, None, None, None, "")]:
    rs, rg, rm, rp = r, r + 1, r + 2, r + 3
    SR[k] = dict(s=rs, m=rm, p=rp)
    ws.cell(row=rs, column=1, value=f"{nm}: sales").font = F_B
    ws.cell(row=rg, column=1, value="  growth")
    ws.cell(row=rm, column=1, value="  operating margin")
    ws.cell(row=rp, column=1, value="  operating profit")
    put(ws, f"B{rs}", L(f"s24_{k}"), M0); put(ws, f"C{rs}", L(f"s25_{k}"), M0)
    put(ws, f"D{rs}", f"={A[f'h1s_{k}']}+{A[f'h2s_{k}']}", M0)
    put(ws, f"B{rp}", L(f"p24_{k}"), M0); put(ws, f"C{rp}", L(f"p25_{k}"), M0)
    put(ws, f"D{rp}", f"={A[f'h1p_{k}']}+{A[f'h2s_{k}']}*{A[f'h2m_{k}']}", M0)
    for col in "BCD":
        put(ws, f"{col}{rm}", f"={col}{rp}/{col}{rs}", PCT1)
    if g27:
        put(ws, f"E{rs}", f"=D{rs}*(1+{A[g27]}){extra}", M0); put(ws, f"F{rs}", f"=E{rs}*(1+{A[g28]})", M0)
        put(ws, f"E{rm}", L(m27), PCT1); put(ws, f"F{rm}", L(m28), PCT1)
        put(ws, f"E{rp}", f"=E{rs}*E{rm}", M0); put(ws, f"F{rp}", f"=F{rs}*F{rm}", M0)
    else:
        for col in "EF":
            put(ws, f"{col}{rs}", 0, M0); put(ws, f"{col}{rp}", 0, M0)
    for col, prev in [("C", "B"), ("D", "C"), ("E", "D"), ("F", "E")]:
        put(ws, f"{col}{rg}", f'=IF({prev}{rs}=0,"n.a.",{col}{rs}/{prev}{rs}-1)', PCT1)
    r += 5
TS, TP, TM = r, r + 1, r + 2   # 25, 26, 27
ws.cell(row=TS, column=1, value="Total sales").font = F_B
ws.cell(row=TP, column=1, value="Total segment operating profit").font = F_B
ws.cell(row=TM, column=1, value="Segment margin").font = F_B
for col in "BCDEF":
    put(ws, f"{col}{TS}", "=" + "+".join(f"{col}{SR[k]['s']}" for k in SR), M0)
    put(ws, f"{col}{TP}", "=" + "+".join(f"{col}{SR[k]['p']}" for k in SR), M0)
    put(ws, f"{col}{TM}", f"={col}{TP}/{col}{TS}", PCT1)
note(ws, TM + 2, [
    "*2026E combines Eaton's first-half results with my second-half estimates; 2027E and 2028E are my estimates for continuing operations,",
    "Electrical Americas, Electrical Global and Aerospace, with Mobility treated as gone from 1 January 2027 (the Dana transaction is expected to close in Q1 2027).",
    "Eaton guides 2026 segment margins to 24.1 to 24.5% and organic growth to 11 to 13% (31 July 2026). 2024A and 2025A as reported; Mobility recast as Vehicle plus eMobility.",
])

# =====================================================================  EPS BRIDGE
ws = sheet("EPS", "ADJUSTED EPS BRIDGE (US$ MILLION UNLESS STATED)", [52, 13, 13, 13, 13, 13])
head(ws, 4, ["", "2024A", "2025A", "2026E*", "2027E*", "2028E*"])
labels = ["Segment operating profit", "Corporate other expense, excluding charges", "Interest expense, net",
          "Pension and other postretirement income", "Adjusted pre-tax profit", "Tax", "Noncontrolling interests",
          "Adjusted earnings", "Diluted shares, m", "ADJUSTED EPS, US$", "Growth", "Eaton guide / consensus, US$", "Mine against it"]
for i, lab in enumerate(labels):
    ws.cell(row=5 + i, column=1, value=lab).font = F_B if lab.isupper() or i in (0, 4, 7) else Font()
for col, corp, intr in [("D", "corp26", "int26"), ("E", "corp27", "int27"), ("F", "corp28", "int28")]:
    put(ws, f"{col}5", f"=Segments!{col}{TP}", M0, F_LINK)
    put(ws, f"{col}6", "=-" + A[corp], M0, F_LINK)
    put(ws, f"{col}7", "=-" + A[intr], M0, F_LINK)
    put(ws, f"{col}8", L("pens"), M0)
    put(ws, f"{col}9", f"=SUM({col}5:{col}8)", M0)
    put(ws, f"{col}10", f"=-{col}9*{A['tax']}", M0, F_LINK)
    put(ws, f"{col}11", "=-" + A["nci_inc"], M0, F_LINK)
    put(ws, f"{col}12", f"=SUM({col}9:{col}11)", M0)
    put(ws, f"{col}13", L("shares_dil") if col == "D" else f"={A['shares_dil']}-{A['retired']}", M1)
    put(ws, f"{col}14", f"={col}12/{col}13", USD2, F_B, FILL_KEY)
put(ws, "B14", L("eps24"), USD2); put(ws, "C14", L("eps25"), USD2)
for col, prev in [("C", "B"), ("D", "C"), ("E", "D"), ("F", "E")]:
    put(ws, f"{col}15", f"={col}14/{prev}14-1", PCT1)
put(ws, "D16", f"=({A['g_lo']}+{A['g_hi']})/2", USD2); put(ws, "E16", L("cons27"), USD2)
put(ws, "D17", "=D14/D16-1", PCT1); put(ws, "E17", "=E14/E16-1", PCT1)
note(ws, 19, [
    "*My estimates. 2026E uses Eaton's first-half results plus my second half; the bridge with a 19% tax rate reproduces the midpoint of Eaton's 2026 guide.",
    "Adjusted EPS excludes intangible amortisation, acquisition and divestiture charges and restructuring, as Eaton defines it. 2024A and 2025A are as reported.",
    "2027E and 2028E exclude Mobility and use diluted shares less the shares retired in the exchange offer. Consensus 2027 (stockanalysis.com) may still include some Mobility.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: P/E ON 2028E ADJUSTED EPS, TWELVE MONTHS OUT", [62, 16, 70])
head(ws, 4, ["Item", "Value", "Working / note"])
vrows = [
    (5, "2028E adjusted EPS, US$", "=EPS!F14", USD2, "Continuing operations, my estimate."),
    (6, "Base multiple", L("pe_base"), MULTF, "Eaton's 2021 to 2025 average forward P/E of 24.0x, less one turn."),
    (7, "BASE VALUE PER SHARE, US$", "=B5*B6", USD2, ""),
    (8, "Reference price, US$", L("price"), USD2, "NYSE close, 23 October 2026."),
    (9, "Base value against price", "=B7/B8-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (10, "VIEW ON THE BAND", '=IF(B9>=0.15,"LONG",IF(B9<=-0.25,"SHORT","NO CALL"))', None, "Tommy Lau's call, 26 October 2026: LONG, target US$430, Low conviction."),
    (11, "Target, US$ (base value rounded down)", CALL["target"] or "", USD2, "Judgement: rounded down from the base value."),
    (12, "Target against price", "=IF(B11=\"\",\"\",B11/B8-1)", PCT1, ""),
    (14, "Market value, US$bn", f"={A['shares_out']}*B8/1000", '#,##0.0', "Shares outstanding at 30 June 2026."),
    (15, "Net debt, US$m, 30 June 2026", f"={A['debt']}-{A['cash']}", M0, ""),
    (16, "Enterprise value, US$bn", f"=B14+(B15+{A['nci']})/1000", '#,##0.0', "Before leases and pensions."),
    (17, "P/E on 2026 guide midpoint", f"=B8/EPS!D16", MULTF, ""),
    (18, "P/E on 2026E (mine)", "=B8/EPS!D14", MULTF, ""),
    (19, "P/E on 2027 consensus", "=B8/" + A["cons27"], MULTF, "stockanalysis.com."),
    (20, "P/E on 2027E (mine)", "=B8/EPS!E14", MULTF, ""),
    (21, "P/E on 2028E (mine): what the price pays", "=B8/EPS!F14", MULTF, ""),
    (22, "P/E on 2026 guide midpoint at the August high", f"={A['hiclose']}/EPS!D16", MULTF, "Close of US$459.96, 12 August 2026."),
    (23, "Multiple of 2028E needed for a value 15% above the price", "=B8*1.15/B5", MULTF, ""),
    (24, "Price below which the base value is 15% or more above it, US$", "=B7/1.15", USD2, ""),
    (25, "Price above which the base value is 25% or more below it, US$", "=B7/0.75", USD2, ""),
    (26, "Price against the highest close", f"=B8/{A['hiclose']}-1", PCT1, ""),
    (27, "Price change in 2026 to date", f"=B8/{A['pxdec']}-1", PCT1, ""),
    (28, "Average analyst target against price", f"={A['constp']}/B8-1", PCT1, "Cross-check only."),
]
for rr, lab, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    if rr in (7, 10):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    elif isinstance(f, str) and (f.startswith("=Assumptions") or f.startswith("=EPS")): c.font = F_LINK
    elif rr == 11: c.font = F_INB; c.fill = FILL_ASSUME
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (VALUE = MULTIPLE x 2028E ADJUSTED EPS)", [10, 11, 11, 11, 11, 12, 12, 10, 12, 12, 12, 12, 12, 11])
head(ws, 4, ["Case", "EA growth 27", "EA growth 28", "EA margin 27", "EA margin 28", "Other growth +/-", "Other margin +/-",
             "Multiple", "EA sales 28", "Other sales 28", "Segment OP 28", "2028E EPS", "Value, US$", "vs price"])
r = 5
for s in SCEN:
    name, g27, g28, m27, m28, dg, dm, mult, p = s
    ws.cell(row=r, column=1, value=name).font = F_B
    if name == "Base":
        for j, k in enumerate(["ea_g27", "ea_g28", "ea_m27", "ea_m28"]):
            c = ws.cell(row=r, column=2 + j, value="=" + A[k]); c.font = F_LINK
        for j, v in enumerate([0, 0]):
            c = ws.cell(row=r, column=6 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME
        c = ws.cell(row=r, column=8, value="=" + A["pe_base"]); c.font = F_LINK
    else:
        for j, v in enumerate([g27, g28, m27, m28, dg, dm, mult]):
            c = ws.cell(row=r, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME
    for col in range(2, 8): ws.cell(row=r, column=col).number_format = PCT1
    ws.cell(row=r, column=8).number_format = MULT0
    ea = SR["EA"]["s"]; eg = SR["EG"]["s"]; ae = SR["AE"]["s"]
    ws.cell(row=r, column=9, value=f"=Segments!$D${ea}*(1+B{r})*(1+C{r})").number_format = M0
    egf = f"(Segments!$D${eg}*(1+{A['eg_g27']}+F{r})+{A['boyd']})*(1+{A['eg_g28']}+F{r})"
    aef = f"Segments!$D${ae}*(1+{A['ae_g27']}+F{r})*(1+{A['ae_g28']}+F{r})"
    ws.cell(row=r, column=10, value=f"={egf}+{aef}").number_format = M0
    ws.cell(row=r, column=11, value=f"=I{r}*E{r}+{egf}*({A['eg_m28']}+G{r})+{aef}*({A['ae_m28']}+G{r})").number_format = M0
    ws.cell(row=r, column=12, value=f"=((K{r}-{A['corp28']}-{A['int28']}+{A['pens']})*(1-{A['tax']})-{A['nci_inc']})/({A['shares_dil']}-{A['retired']})").number_format = USD2
    ws.cell(row=r, column=13, value=f"=L{r}*H{r}").number_format = USD2
    ws.cell(row=r, column=14, value=f"=M{r}/{A['price']}-1").number_format = PCT1
    r += 1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[8]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, US$"; ws["A11"].font = F_B
ws["E11"] = "=B9*M5+C9*M6+D9*M7"; ws["E11"].number_format = USD2; ws["E11"].font = F_B; ws["E11"].fill = FILL_KEY
ws["F11"] = f"=E11/{A['price']}-1"; ws["F11"].number_format = PCT1
ws["A12"] = "Check: base case equals the Valuation tab"; ws["E12"] = "=M6-Valuation!B7"; ws["E12"].number_format = '0.000'
note(ws, 14, [
    "All cases start from my 2026E segment sales and use the same EPS bridge (corporate costs, interest, tax, shares). 'Other' = Electrical Global and Aerospace.",
    "Bear: AI data centre orders pause in 2027; EA growth 8% then 4%, margin slips to 27.5% as the queue shortens and price competition returns; 18x.",
    "Bull: capacity arrives early and orders hold; EA growth 19% then 16%, margin 31.5%; 26x, near Eaton's own forward multiple today and below its August peak.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: 2028E ADJUSTED EPS AGAINST THE P/E (US$)", [30, 14, 14, 14])
head(ws, 4, ["2028E EPS \\ P/E", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_PE, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["pe_base"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (e, link) in enumerate(zip(SENS_EPS, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value="=EPS!F14" if link else e)
    c.number_format = USD2; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=f"=$A{rr}*{col}$4").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["The middle row links to the model's 2028E EPS and the middle column to the base multiple."])

# =====================================================================  QUEUE
ws = sheet("Queue", "ELECTRICAL AMERICAS: BACKLOG, SALES AND THE CLAIM'S TEST", [52] + [10] * 10)
head(ws, 4, ["US$ million"] + Q)
ws["A5"] = "Sales"; ws["A6"] = "Operating profit"; ws["A7"] = "Operating margin"; ws["A8"] = "Sales over the previous four quarters"
ws["A9"] = "Backlog at quarter end"; ws["A10"] = "Backlog / previous four quarters' sales (years)"; ws["A11"] = "Months of sales on order"
for j in range(10):
    col = get_column_letter(2 + j)
    put(ws, f"{col}5", EA_S[j], M0, F_IN); put(ws, f"{col}6", EA_P[j], M0, F_IN)
    put(ws, f"{col}7", f"={col}6/{col}5", PCT1)
    if j >= 3:
        c0 = get_column_letter(2 + j - 3)
        put(ws, f"{col}8", f"=SUM({c0}5:{col}5)", M0)
        put(ws, f"{col}9", EA_BL[j - 3], M0, F_IN)
        put(ws, f"{col}10", f"={col}9/{col}8", '0.000')
        put(ws, f"{col}11", f"={col}10*12", '0.0')
ws["A13"] = "Trailing sales growth, June 2025 to June 2026"; put(ws, "B13", "=K8/G8-1", PCT1)
ws["A14"] = "Backlog growth, June 2025 to June 2026"; put(ws, "B14", "=K9/G9-1", PCT1)
ws["A15"] = "The claim's floor before end 2027 (June 2025 level)"; put(ws, "B15", "=G10", '0.000')
ws["A16"] = "My Q3 2026 sales estimate"; put(ws, "B16", 3990, M0, F_INB, FILL_ASSUME)
ws["A17"] = "September 2026 backlog needed for the ratio not to fall"; put(ws, "B17", "=K10*(SUM(I5:K5)+B16)", M0)
note(ws, 19, [
    "Sources: Eaton quarterly earnings releases (Form 8-K Ex. 99), Q2 2024 to Q2 2026, for sales and operating profit; Form 10-K 2025 for backlog at Dec 2024 and",
    "Dec 2025; Form 10-Qs for Mar 2025 (10,050), Jun 2025 and Jun 2026 (11,377 and 15,175), Sep 2025 (12,009) and Mar 2026 (14,459). The ratio is my arithmetic;",
    "Eaton does not publish it. Fibrebond (acquired 1 April 2025) is in the June 2025 backlog but in only one quarter of that date's trailing sales.",
    "Q1 and Q2 2026 margins: 480 and 470 bps hits from commodity inflation (10-Qs); Eaton expects price and cost roughly neutral in the second half (Q2 call).",
])
ws.column_dimensions["A"].width = 56

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, RETRIEVED 26 OCTOBER 2026)", [22, 14, 13, 18, 70])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "EV/EBIT (trailing)", "What they make"])
for i, (co, tk, pe, eve, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, v in enumerate([pe, eve]):
        c = ws.cell(row=rr, column=3 + j, value=v); c.number_format = MULTF; c.font = F_IN
    ws.cell(row=rr, column=5, value=what).alignment = WRAP
last = 4 + len(PEERS)
ws[f"A{last + 2}"] = "Peer median (excluding Eaton)"; ws[f"A{last + 2}"].font = F_B
ws[f"C{last + 2}"] = f"=MEDIAN(C6:C{last})"; ws[f"D{last + 2}"] = f"=MEDIAN(D6:D{last})"
ws[f"A{last + 3}"] = "Eaton forward P/E, 2021 to 2025 average"; ws[f"A{last + 3}"].font = F_B
ws[f"C{last + 3}"] = f"=AVERAGE({','.join(str(v) for v in HIST_FWD_PE.values())})"
for c in (f"C{last + 2}", f"D{last + 2}", f"C{last + 3}"): ws[c].number_format = MULTF
note(ws, last + 5, ["Multiples only, to set the range of multiples. No view on the peers' shares is expressed. GE Vernova is left out: its trailing",
                    "EV/EBIT of 76x reflects earnings still recovering. Eaton's history: 23.9x, 19.5x, 24.5x, 28.2x, 23.8x for 2021 to 2025 (stockanalysis.com)."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 150])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Eaton second quarter 2026 earnings release, Form 8-K Ex. 99, 31 July 2026: segment sales and profit, income statement, adjusted EPS bridge, balance sheet, 2026 and Q3 guidance, Boyd Thermal, Ultra PCS, Mobility separation.",
    "Eaton Form 10-Q, quarter to 30 June 2026, filed 31 July 2026: Electrical Americas backlog, book-to-bill and margin bridge; total backlog ~US$24.1bn; shares outstanding; no repurchases in 2026.",
    "Eaton Form 10-Qs for the quarters to 31 March 2025, 30 September 2025 and 31 March 2026, and the 2025 Form 10-K (filed 26 February 2026): Electrical Americas backlog and margin bridges.",
    "Eaton quarterly earnings releases, Form 8-K Ex. 99, 1 August 2024 to 5 May 2026: segment sales and operating profit by quarter; 2024 and 2025 adjusted EPS; earlier 2026 guidance.",
    "Eaton Form 8-K of 11 June 2026 and Ex. 99.1: Mobility to combine with Dana Incorporated in a Reverse Morris Trust; Mobility valued at about US$5.1bn; ~US$1.1bn cash; close expected Q1 2027.",
    "Eaton Form 8-K of 16 October 2026: 2025 financial statements recast for the Mobility segment. Form 8-K of 5 October 2026: change of principal accounting officer.",
    "Eaton press release, 'Eaton to announce third quarter 2026 earnings on November 3, 2026' (Business Wire, via Yahoo Finance and MarketScreener).",
    "Eaton second quarter 2026 earnings call, 31 July 2026, third-party transcript (Motley Fool via The Globe and Mail): price and cost back to roughly neutral in the second half; capacity the priority.",
    "Yahoo Finance, ETN chart data, retrieved 26 October 2026: month-end and daily closes, highs.",
    "stockanalysis.com (S&P Global Market Intelligence data), retrieved 26 October 2026: consensus EPS and revenue (updated 20 October), average target, Eaton and peer forward P/E and EV/EBIT.",
    "The Physical Layer, 'Eaton is shipping more electrical gear than ever, and its order book is growing faster still', 26 October 2026: https://thephysicallayer.fyi/journal/eaton-order-book-outruns-it/",
    "Estimates for the second half of 2026, 2027 and 2028 are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Call (Tommy Lau, 26 October 2026)", "=Valuation!B10", None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Target, US$", "=Valuation!B11", USD2, "Base value rounded down."),
    ("Base value per share, US$", "=Valuation!B7", USD2, "Base multiple x 2028E adjusted EPS, continuing operations."),
    ("Reference price, US$", "=" + A["price"], USD2, "NYSE close, 23 October 2026."),
    ("Base value against price", "=Valuation!B9", PCT1, ""),
    ("Probability-weighted value, US$", "=Scenarios!E11", USD2, "25 / 50 / 25 bear / base / bull."),
    ("2028E adjusted EPS, US$", "=EPS!F14", USD2, "My estimate."),
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
    ("Segments", "Sales, margin and operating profit by segment, 2024A to 2028E."),
    ("EPS", "Bridge from segment profit to adjusted EPS; against the guide and consensus."),
    ("Valuation", "Base value, the band, multiples at the price, revisit levels."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "2028E EPS against the multiple."),
    ("Queue", "Electrical Americas backlog over trailing sales: the claim's test."),
    ("Peers", "Forward P/E and trailing EV/EBIT used to set the multiple."),
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
