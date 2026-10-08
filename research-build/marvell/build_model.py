"""Marvell initiation model, 8 Oct 2026, rebuilt on the Investor Day of 6 Oct 2026. Live formulas throughout.

House style follows the Vertiv and Lumentum models: navy header rows, blue font for hardcoded inputs, yellow fill on
my own assumptions, green font for cross-sheet links, black for formulas.
Non-GAAP basis unless marked GAAP. Fiscal years end around 31 January (FY2027 = year to about 30 January 2027).
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

USD2 = '"US$"#,##0.00'; USD0 = '"US$"#,##0'; BN2 = '#,##0.00'; BN3 = '#,##0.000'; BN4 = '#,##0.0000'; BN1 = '#,##0.0'
PCT1 = '0.0%'; PCT0 = '0%'; MULT = '0.0"x"'; MULT0 = '0"x"'
SUB = f"Tommy Lau | Marvell Technology (Nasdaq: MRVL) | {DATE_LONG} | Non-GAAP basis; fiscal years to about 31 January | Personal research, not investment advice."

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


sheet("Cover", "MARVELL TECHNOLOGY (NASDAQ: MRVL)  INITIATION MODEL", [38, 26, 80])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [60, 14, 10, 92])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "another tab. Black = formula. US$ billion unless stated; per-share figures in US$; shares in billions.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"q4rev", "h2gm", "sh3", "sh4", "gm28", "opexratio", "other28", "sh28", "other29", "tax29", "sh29", "pe",
        "cus27", "swi27", "cus28", "swi28", "comms27", "comms28"}
rows = [
    ("MARKET (retrieved 6 to 8 October 2026)", None, None, None, None),
    ("price", "Share price (Nasdaq: MRVL)", PRICE, "US$", "Nasdaq close, 7 October 2026 (stockanalysis.com, 4:00pm EDT)."),
    ("hi52", "52-week high (intraday, 18 June 2026)", HI52, "US$", "Nasdaq.com."),
    ("hiclose", "Highest close (4 June 2026)", HI_CLOSE, "US$", "Nasdaq.com."),
    ("lo52", "52-week low (intraday, 5 February 2026)", LO52, "US$", "Nasdaq.com (70.685)."),
    ("loclose", "Lowest close (4 February 2026)", LO_CLOSE, "US$", "Nasdaq.com."),
    ("pxdec25", "Close, 31 Dec 2025", PRICE_DEC25, "US$", "Nasdaq.com."),
    ("pxpiece", "Close, 25 Sep 2026 (last close before the journal piece)", PRICE_PIECE, "US$", "Nasdaq.com (261.935)."),
    ("common", "Common shares outstanding, 21 Aug 2026", COMMON_OUT, "bn", "10-Q cover: 876.9 million."),
    ("pref", "Nvidia Series A preferred, as converted", PREF_ASCONV, "bn", "8-K of 31 March 2026: up to 21,778,000 common shares."),
    ("prefconv", "Preferred conversion price", PREF_CONV, "US$", "8-K of 31 March 2026: about US$91.8355; US$2.0bn paid."),
    ("cash", "Cash and cash equivalents, 1 Aug 2026", CASH, "US$bn", "Q2 FY27 release balance sheet."),
    ("debt", "Long-term debt, 1 Aug 2026", DEBT, "US$bn", "Q2 FY27 release; no short-term debt."),
    ("wsh", "Google warrant, shares", WARRANT_SH, "bn", "8-K of 19 Aug 2026: 58,970,907 shares."),
    ("wpx", "Google warrant exercise price", WARRANT_PX, "US$", "Same."),
    ("wtr", "Custom revenue per vesting tranche", WARRANT_TRANCHE_USD, "US$bn", "Same: one tranche per US$500m; 240 tranches."),
    ("wn", "Number of revenue tranches", WARRANT_TRANCHES, "no.", "Same."),
    ("cons27", "FY27 consensus EPS", CONS_EPS_27, "US$", "stockanalysis.com, updated 7 Oct 2026, 40 analysts."),
    ("cons28", "FY28 consensus EPS", CONS_EPS_28, "US$", "stockanalysis.com (S&P Global, updated 2 Oct 2026, before the Investor Day)."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com, updated 7 Oct 2026, 46 analysts; range 210 to 450."),
    ("fwdpe", "Forward P/E shown by stockanalysis.com", FWD_PE_SA, "x", "stockanalysis.com, at the 7 October 2026 close."),
    ("REPORTED AND GUIDED (Marvell releases, 10-Q, calls)", None, None, None, None),
    ("q3rev", "Q3 FY27 revenue guide, midpoint", GUIDE_Q3["rev"], "US$bn", "Release of 27 August 2026: US$3.150bn +/- 5%."),
    ("q3gmlo", "Q3 FY27 non-GAAP gross margin guide, low", GUIDE_Q3["gm"][0], "%", "Same."),
    ("q3gmhi", "Q3 FY27 non-GAAP gross margin guide, high", GUIDE_Q3["gm"][1], "%", "Same."),
    ("q3opex", "Q3 FY27 non-GAAP operating expenses guide", GUIDE_Q3["opex"], "US$bn", "Same: about US$655m."),
    ("other", "Non-GAAP interest and other, per quarter", GUIDE_Q3["other"], "US$bn", "Q2 FY27 call: about US$36m expense in Q3."),
    ("tax27", "Non-GAAP tax rate, FY27", GUIDE_Q3["tax"], "%", "Release and call of 27 August 2026: 11%."),
    ("q3epslo", "Q3 FY27 non-GAAP EPS guide, low", GUIDE_Q3["eps"][0], "US$", "Same."),
    ("q3epshi", "Q3 FY27 non-GAAP EPS guide, high", GUIDE_Q3["eps"][1], "US$", "Same."),
    ("fy27", "FY27 revenue outlook", FY27_OUTLOOK, "US$bn", "Q2 FY27 call: roughly US$12 billion."),
    ("fy27opex", "FY27 non-GAAP operating expenses outlook", FY27_OPEX, "US$bn", "Q2 FY27 call: about US$2.55bn."),
    ("fy28", "FY28 revenue outlook", FY28_OUTLOOK, "US$bn", "Investor Day deck, 6 October 2026 (slide 33): about US$20bn, 67% growth; was US$18bn on the Q2 FY27 call."),
    ("tax28", "Non-GAAP tax rate, FY28", FY28_TAX, "%", "Q2 FY27 call: approximately 13%."),
    ("cus26", "Custom revenue, FY26", CUSTOM_26, "US$bn", "Q4 FY26 call (5 March 2026): US$1.5 billion."),
    ("swi26", "Data centre switching revenue, FY26", SWITCH_26, "US$bn", "Q4 FY26 call: exceeding US$300 million."),
    ("sbcq2", "Stock-based pay, Q2 FY27", SBC_Q2, "US$bn", "Q2 FY27 release reconciliation."),
    ("sbcq2py", "Stock-based pay, Q2 FY26", SBC_Q2_PY, "US$bn", "Same."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("q4rev", "Revenue, Q4 FY27", Q4_REV, "US$bn", "MINE. What the US$12bn outlook leaves after Q1, Q2 and the Q3 midpoint."),
    ("h2gm", "Non-GAAP gross margin, Q3 and Q4 FY27", H2_GM, "%", "MINE. Guide 57.5 to 58.5% for Q3, same range in Q4."),
    ("sh3", "Diluted shares, Q3 FY27", SH_Q3, "bn", "MINE: the company's guide of 921m."),
    ("sh4", "Diluted shares, Q4 FY27", SH_Q4, "bn", "MINE."),
    ("gm28", "Non-GAAP gross margin, FY28", GM28, "%", "MINE. CFO: same range as the second half of FY27."),
    ("opexratio", "FY28 opex growth as a share of revenue growth", OPEX_G_RATIO, "%", "MINE. CFO: roughly half the rate."),
    ("other28", "Non-GAAP interest and other, FY28", OTHER28, "US$bn", "MINE."),
    ("sh28", "Diluted shares, FY28", SH28, "bn", "MINE. Awards, warrant and Celestial shares, net of buybacks."),
    ("other29", "Non-GAAP interest and other, FY29", OTHER29, "US$bn", "MINE."),
    ("tax29", "Non-GAAP tax rate, FY29", TAX29, "%", "MINE. The Investor Day FY31 model rate (slide 142)."),
    ("sh29", "Diluted shares, FY29", SH29, "bn", "MINE."),
    ("pe", "Target multiple on FY29E EPS (base)", BASE_PE, "x", "MINE. Median forward P/E of six peers (Peers tab), rounded."),
    ("comms27", "Communications and other revenue, FY27", COMMS_27, "US$bn", "MINE. About 10% growth (Q2 FY27 call)."),
    ("comms28", "Communications and other revenue, FY28", COMMS_28, "US$bn", "MINE. FY28 outlook of US$20bn less data centre of about US$18bn (Investor Day, slides 33 and 36)."),
    ("cus27", "Custom revenue, FY27", DC_SPLIT["FY27E"][0], "US$bn", "MINE. Guided more than 20% growth in March; H2 acceleration since."),
    ("swi27", "Data centre switching revenue, FY27", DC_SPLIT["FY27E"][1], "US$bn", "MINE. Guided above US$600m; more than double."),
    ("cus28", "Custom revenue, FY28", DC_SPLIT["FY28E"][0], "US$bn", "MINE. Below US$4bn: the FY29 target of US$12bn+ is more than 3x FY28 (slide 28)."),
    ("swi28", "Data centre switching revenue, FY28", DC_SPLIT["FY28E"][1], "US$bn", "MINE. Scale-out switching above US$1bn in FY28 (slide 122), plus scale-up."),
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
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else (BN4 if unit == "bn" else ("#,##0.00" if unit == "US$" else ("0" if unit == "no." else BN3))))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1

# ===================================================================== QUARTERLY
ws = sheet("Quarterly", "QUARTERLY HISTORY, Q1 FY25 TO Q2 FY27, AND MY SECOND HALF OF FY27", [50] + [10] * 12)
QH = Q + ["Q3 FY27E", "Q4 FY27E"]
head(ws, 4, ["US$ billion unless stated"] + QH)
C = [get_column_letter(2 + j) for j in range(12)]


def qrow(row, label, vals, fmt, bold=False):
    ws.cell(row=row, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=row, column=2 + j, value=v if v is not None else "")
        c.number_format = fmt; c.alignment = RIGHT
        if v is not None and not is_formula(v):
            c.font = F_IN
        elif isinstance(v, str) and v.startswith("=Assumptions"):
            c.font = F_LINK


bn = lambda xs: [x / 1000 for x in xs]
pct = lambda xs: [x / 100 for x in xs]
E2 = [None] * 2
qrow(5, "Revenue", bn(Q_REV) + ["=" + A["q3rev"], "=" + A["q4rev"]], BN3, True)
qrow(6, "Data centre revenue", bn(Q_DC) + E2, BN3)
qrow(7, "Data centre share of revenue", [f"={c}6/{c}5" for c in C[:10]] + E2, PCT1)
qrow(8, "Data centre growth on a year earlier", [None] * 4 + [f"={C[j]}6/{C[j - 4]}6-1" for j in range(4, 10)] + E2, PCT1)
qrow(9, "Gross margin, non-GAAP", pct(Q_GM) + ["=" + A["h2gm"], "=" + A["h2gm"]], PCT1, True)
qrow(10, "Operating expenses, non-GAAP", [None] * 8 + [Q27_ACT["opex"][0], Q27_ACT["opex"][1], "=" + A["q3opex"],
     f"={A['fy27opex']}-J10-K10-L10"], BN4)
qrow(11, "Operating income, non-GAAP", [f"={c}5*{c}12" for c in C[:8]] + [Q27_ACT["opinc"][0], Q27_ACT["opinc"][1], "=L5*L9-L10", "=M5*M9-M10"], BN4, True)
qrow(12, "Operating margin, non-GAAP", pct(Q_OM[:8]) + ["=J11/J5", "=K11/K5", "=L11/L5", "=M11/M5"], PCT1)
qrow(13, "Net profit, non-GAAP", [None] * 8 + [Q27_ACT["ni"][0], Q27_ACT["ni"][1], f"=(L11+{A['other']})*(1-{A['tax27']})",
     f"=(M11+{A['other']})*(1-{A['tax27']})"], BN4)
qrow(14, "Diluted shares, bn", [None] * 8 + [Q27_ACT["sh"][0], Q27_ACT["sh"][1], "=" + A["sh3"], "=" + A["sh4"]], BN4)
qrow(15, "Diluted EPS, US$ (reported; second half of FY27 mine)", Q_EPS + ["=L13/L14", "=M13/M14"], USD2, True)
ws["A17"] = "Checks"; ws["A17"].font = Font(bold=True, color=NAVY)
chk = [
    (18, "Trailing four quarters EPS to Q2 FY27", "=SUM(H15:K15)", USD2),
    (19, "Data centre growth, Q2 FY27 on Q2 FY26", "=K8", PCT1),
    (20, "Data centre share, Q2 FY27", "=K7", PCT1),
    (21, "Data centre share, Q4 FY26", "=I7", PCT1),
    (22, "Q3 FY27E EPS against the guide (low / high)", "=L15", USD2),
    (23, "Q4 FY27E operating margin", "=M12", PCT1),
    (24, "Non-GAAP gross margin, Q1 FY25 to Q2 FY27, change in points", "=(K9-B9)*100", BN1),
]
for rr, lab, f, fmt in chk:
    ws.cell(row=rr, column=1, value=lab); c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
ws["C22"] = "=" + A["q3epslo"]; ws["D22"] = "=" + A["q3epshi"]
for c_ in ("C22", "D22"): ws[c_].number_format = USD2
note(ws, 26, ["Source: Marvell results releases (Exhibit 99.1 to Form 8-K), 3 December 2024 to 27 August 2026, with comparatives.",
              "Operating income to Q4 FY26 is revenue x reported non-GAAP operating margin; Q1 and Q2 FY27 are as reported (US$846.9m and US$1,003.2m).",
              "Q3 FY27E uses the guide's midpoints; Q4 FY27E is what the US$12bn outlook and the US$2.55bn opex outlook leave. Both are my estimates."])

# ===================================================================== FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (US$ billion unless stated, non-GAAP basis)", [52, 12, 12, 12, 12, 12, 12])
head(ws, 4, ["", "FY24A", "FY25A", "FY26A", "FY27E*", "FY28E*", "FY29E*"])
fin = [
    ("Revenue", [REV_H[0], REV_H[1], REV_H[2], "=SUM(Quarterly!H5:K5)+Quarterly!L5+Quarterly!M5-Quarterly!H5-Quarterly!I5", "=" + A["fy28"], "=F5*(1+Scenarios!B6)"], BN2, True),
    ("Revenue growth", [None, "=C5/B5-1", "=D5/C5-1", "=E5/D5-1", "=F5/E5-1", "=G5/F5-1"], PCT1, False),
    ("Data centre revenue", [DC_H[0], DC_H[1], DC_H[2], "=DataCentre!C5", "=DataCentre!D5", None], BN2, False),
    ("Gross margin, non-GAAP", [GM_H[0], GM_H[1], GM_H[2], f"=(SUMPRODUCT(Quarterly!J5:M5,Quarterly!J9:M9))/E5", "=" + A["gm28"], None], PCT1, False),
    ("Operating expenses, non-GAAP", [None, None, None, "=SUM(Quarterly!J10:M10)", f"=E9*(1+{A['opexratio']}*F6)", None], BN3, False),
    ("Operating income", [REV_H[0] * OM_H[0], REV_H[1] * OM_H[1], REV_H[2] * OM_H[2], "=SUM(Quarterly!J11:M11)", "=F5*F8-F9", "=G5*Scenarios!C6"], BN3, True),
    ("Operating margin", ["=B10/B5", "=C10/C5", "=D10/D5", "=E10/E5", "=F10/F5", "=G10/G5"], PCT1, False),
    ("Interest and other", [None, None, None, None, "=" + A["other28"], "=" + A["other29"]], BN3, False),
    ("Tax rate", [None, None, None, "=" + A["tax27"], "=" + A["tax28"], "=" + A["tax29"]], PCT1, False),
    ("Net profit", [NI_H[0], NI_H[1], NI_H[2], "=SUM(Quarterly!J13:M13)", "=(F10+F12)*(1-F13)", "=(G10+G12)*(1-G13)"], BN3, True),
    ("Diluted shares, bn", [None, None, None, "=E14/E16", "=" + A["sh28"], "=" + A["sh29"]], BN4, False),
    ("Diluted EPS, US$", [EPS_H[0], EPS_H[1], EPS_H[2], "=SUM(Quarterly!J15:M15)", "=F14/F15", "=G14/G15"], USD2, True),
    ("EPS growth", [None, "=C16/B16-1", "=D16/C16-1", "=E16/D16-1", "=F16/E16-1", "=G16/F16-1"], PCT1, False),
    ("P/E at reference price", [None, None, f"={A['price']}/D16", f"={A['price']}/E16", f"={A['price']}/F16", f"={A['price']}/G16"], MULT, False),
    ("Consensus EPS, US$", [None, None, None, "=" + A["cons27"], "=" + A["cons28"], None], USD2, False),
    ("Mine against consensus", [None, None, None, "=E16/E19-1", "=F16/F19-1", None], PCT1, False),
    ("P/E on consensus", [None, None, None, f"={A['price']}/E19", f"={A['price']}/F19", None], MULT, False),
]
for i, (label, vals, fmt, bold) in enumerate(fin):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v if v is not None else "")
        c.number_format = fmt; c.alignment = RIGHT
        if v is not None and not isinstance(v, str): c.font = F_IN
        elif isinstance(v, str) and v.startswith("=Assumptions"): c.font = F_LINK
# FY27 revenue: simpler, the sum of four quarters
ws["E5"] = "=SUM(Quarterly!J5:M5)"
note(ws, 24, [
    "*FY27E, FY28E and FY29E are my own estimates. FY27E sums the Quarterly tab. FY28E takes management's US$20bn Investor Day outlook. FY29E is the base case on the Scenarios tab (row 6).",
    "FY24A to FY26A as reported. FY24 to FY26 operating income is revenue x reported non-GAAP operating margin. FY27E diluted shares is implied (net profit / EPS).",
    "Consensus from stockanalysis.com: FY27 updated 7 October 2026; FY28 S&P Global data of 2 October 2026, before the Investor Day.",
    f"Note check: FY27E revenue {REV27:.2f}, EPS {EPS27:.2f}; FY28E EPS {EPS28:.2f}; FY29E revenue {REV29:.2f}, EPS {EPS29:.2f}.",
])

# ===================================================================== DATA CENTRE SPLIT
ws = sheet("DataCentre", "DATA CENTRE BY BUSINESS: WHAT IS DISCLOSED, AND MY SPLIT", [52, 12, 12, 12, 70])
head(ws, 4, ["US$ billion", "FY26", "FY27E*", "FY28E*", "Basis"])
dc = [
    (5, "Data centre revenue", [DC_H[2], f"=Financials!E5-{A['comms27']}", f"=Financials!F5-{A['comms28']}"], BN2, "FY26 reported. FY27E and FY28E: total less my communications and other."),
    (6, "Custom (XPU and XPU attach)", ["=" + A["cus26"], "=" + A["cus27"], "=" + A["cus28"]], BN2, "FY26 disclosed on the Q4 FY26 call; later years mine."),
    (7, "Data centre switching", ["=" + A["swi26"], "=" + A["swi27"], "=" + A["swi28"]], BN2, "FY26 disclosed as above US$300m; later years mine."),
    (8, "Interconnect, storage and other (derived)", ["=B5-B6-B7", "=C5-C6-C7", "=D5-D6-D7"], BN2, "Remainder. Interconnect is the largest part (Q1 FY27 call)."),
    (9, "Data centre growth", [None, "=C5/B5-1", "=D5/C5-1"], PCT1, "Management: about 60% in FY27 (27 Aug); about US$18bn in FY28 (Investor Day). FY27E here is total less my communications estimate."),
    (10, "Growth of the remainder", [None, "=C8/B8-1", "=D8/C8-1"], PCT1, "Management: interconnect more than 70% in FY27."),
    (11, "Custom share of data centre growth", [None, "=(C6-B6)/(C5-B5)", "=(D6-C6)/(D5-C5)"], PCT1, "The claim's test: how much growth comes from custom."),
    (12, "Remainder share of data centre growth", [None, "=(C8-B8)/(C5-B5)", "=(D8-C8)/(D5-C5)"], PCT1, ""),
    (13, "Custom share of data centre revenue", ["=B6/B5", "=C6/C5", "=D6/D5"], PCT1, ""),
]
for rr, label, vals, fmt, basis in dc:
    ws.cell(row=rr, column=1, value=label).font = F_B if rr in (5, 11) else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v if v is not None else "")
        c.number_format = fmt; c.alignment = RIGHT
        if v is not None and not isinstance(v, str): c.font = F_IN
        elif isinstance(v, str) and v.startswith("=Assumptions"): c.font = F_LINK
    ws.cell(row=rr, column=5, value=basis).alignment = WRAP
note(ws, 15, ["*Marvell does not report interconnect revenue in dollars. The split is my own, built on the disclosed FY26 custom and switching figures and the growth rates management gave."])

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (VALUED ON FY29E)", [30] + [12] * 9)
head(ws, 4, ["Case", "Growth FY29", "Op. margin FY29", "FY29 revenue", "FY29 op. income", "FY29 net profit", "FY29 EPS",
             "Multiple", "Value, US$", "vs price"])
R28 = "Financials!$F$5"
for i, s in enumerate(SCEN):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    for j, v in enumerate(s[1:3]):
        c = ws.cell(row=rr, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT1
    ws.cell(row=rr, column=4, value=f"={R28}*(1+B{rr})").number_format = BN2
    ws.cell(row=rr, column=5, value=f"=D{rr}*C{rr}").number_format = BN3
    ws.cell(row=rr, column=6, value=f"=(E{rr}+{A['other29']})*(1-{A['tax29']})").number_format = BN3
    ws.cell(row=rr, column=7, value=f"=F{rr}/{A['sh29']}").number_format = USD2
    if s[0] == "Base":
        c = ws.cell(row=rr, column=8, value="=" + A["pe"]); c.font = F_LINK
    else:
        c = ws.cell(row=rr, column=8, value=s[3]); c.font = F_INB; c.fill = FILL_ASSUME
    c.number_format = MULT0
    ws.cell(row=rr, column=9, value=f"=G{rr}*H{rr}").number_format = USD2
    ws.cell(row=rr, column=10, value=f"=I{rr}/{A['price']}-1").number_format = PCT0
ws["A10"] = "Probability"; ws["A10"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=9, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=10, column=2 + j, value=s[4]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E10"] = "=SUM(B10:D10)"; ws["E10"].number_format = PCT0; ws["F10"] = "must be 100%"; ws["F10"].font = F_NOTE
ws["A12"] = "Probability-weighted value, US$"; ws["A12"].font = F_B
ws["I12"] = "=B10*I5+C10*I6+D10*I7"; ws["I12"].number_format = USD2; ws["I12"].font = F_B; ws["I12"].fill = FILL_KEY
ws["J12"] = f"=I12/{A['price']}-1"; ws["J12"].number_format = PCT1
note(ws, 14, ["All cases start from FY28E revenue (management's US$20bn Investor Day outlook, Financials tab) and use FY29 diluted shares.",
              "Bear: AI spending pauses and FY29 does not grow. Bull: custom (including the Google programmes) and scale-up optics arrive early.",
              "The base row (6) drives the Financials tab for FY29E."])

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION: 33x FY29E EPS, TWELVE MONTHS OUT", [66, 16, 70])
head(ws, 4, ["Line", "Value", "Working / note"])
val = [
    ("eps29", "FY29E diluted EPS, US$", "=Financials!G16", USD2, "By October 2027 the market will be pricing FY29 (year to about January 2029)."),
    ("mult", "Base multiple, x", "=" + A["pe"], MULT0, "Assumptions tab."),
    ("base", "Base-case value per share, US$", "=B5*B6", USD2, "EPS x multiple."),
    ("px", "Reference price, US$", "=" + A["price"], USD2, "Nasdaq close, 7 October 2026."),
    ("upb", "Base value against the price", "=B7/B8-1", PCT1, ""),
    ("wtd", "Probability-weighted value, US$", "=Scenarios!I12", USD2, "Scenarios tab."),
    ("rule", "Rule on value alone (long at 15% above, short at 25% below)", '=IF(B9>=0.15,"LONG",IF(B9<=-0.25,"SHORT","NO CALL"))', None, "Mechanical only; wider on the short side because a short's losses are open-ended."),
    ("call", "DRAFT VIEW" if CALL["draft"] else "CALL", CALL["direction"], None, "Draft for Tommy Lau's decision." if CALL["draft"] else "Tommy Lau's call, 8 October 2026; target US$355, medium conviction."),
    ("mcap", "Market value on common shares, US$bn", f"={A['price']}*{A['common']}", BN1, ""),
    ("mcapfd", "Market value with the preferred as converted, US$bn", f"={A['price']}*({A['common']}+{A['pref']})", BN1, ""),
    ("nd", "Net debt, US$bn", f"={A['debt']}-{A['cash']}", BN3, "1 August 2026."),
    ("ev", "Enterprise value, US$bn", "=B14+B15", BN1, ""),
    ("riselo", "Change since the lowest close (4 Feb 2026)", f"={A['price']}/{A['loclose']}-1", PCT0, ""),
    ("rise", "Change since 31 Dec 2025", f"={A['price']}/{A['pxdec25']}-1", PCT0, ""),
    ("piece", "Change since the last close before the journal piece (25 Sep 2026)", f"={A['price']}/{A['pxpiece']}-1", PCT1, ""),
    ("offhi", "Against the highest close (4 Jun 2026)", f"={A['price']}/{A['hiclose']}-1", PCT1, ""),
    ("pe26", "P/E on FY26 EPS", "=Financials!D18", MULT, ""),
    ("pe27", "P/E on my FY27E", "=Financials!E18", MULT, ""),
    ("pe28", "P/E on my FY28E", "=Financials!F18", MULT, ""),
    ("pe29", "P/E on my FY29E", "=Financials!G18", MULT, ""),
    ("pec27", "P/E on FY27 consensus", "=Financials!E21", MULT, "stockanalysis.com."),
    ("pec28", "P/E on FY28 consensus", "=Financials!F21", MULT, "stockanalysis.com."),
    ("need", "FY29 EPS the price needs at the base multiple, US$", f"={A['price']}/{A['pe']}", USD2, "What the market prices in."),
    ("needoi", "FY29 operating income that needs, US$bn", f"=B27*{A['sh29']}/(1-{A['tax29']})-{A['other29']}", BN3, ""),
    ("needrev", "FY29 revenue that needs at the base margin, US$bn", "=B28/Scenarios!C6", BN2, "Against my base FY29E."),
    ("needg", "That as growth on FY28E (US$20bn)", "=B29/Financials!F5-1", PCT1, ""),
    ("revl", "Price that puts the base case 15% above (revisit as long)", "=B7/1.15", USD2, ""),
    ("revs", "Price that puts the base case 25% below (revisit as short)", "=B7/0.75", USD2, ""),
    ("epsl", "FY29 EPS that would put the base 15% above today's price", f"={A['price']}*1.15/{A['pe']}", USD2, ""),
    ("epss", "FY29 EPS that would put the base 25% below today's price", f"={A['price']}*0.75/{A['pe']}", USD2, ""),
    ("nvda", "Nvidia preferred at the price, US$bn", f"={A['pref']}*{A['price']}", BN2, ""),
    ("nvdag", "Nvidia preferred against the US$2.0bn paid", f"={A['price']}/{A['prefconv']}-1", PCT0, ""),
    ("wnet", "Google warrant, net shares if fully vested at the price (treasury method), bn", f"={A['wsh']}*(1-{A['wpx']}/{A['price']})", BN4, ""),
    ("wrev", "Google custom revenue that vests the whole warrant, US$bn", f"={A['wtr']}*{A['wn']}", BN1, "240 tranches of US$500m, Q3 FY27 to the end of FY2033."),
    ("sbc", "Stock-based pay, Q2 FY27, against revenue", f"={A['sbcq2']}/Quarterly!K5", PCT1, ""),
    ("sbcg", "Stock-based pay, Q2 FY27 against Q2 FY26", f"={A['sbcq2']}/{A['sbcq2py']}", '0.00"x"', ""),
]
V = {}
for i, (key, label, f, fmt, nt) in enumerate(val):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=label)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    if key in ("base", "call"):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    if key == "call": c.font = F_INB
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
    V[key] = f"Valuation!$B${rr}"

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: FY29E EPS AGAINST MULTIPLE (US$)", [24, 14, 14, 14])
head(ws, 4, ["FY29 EPS \\ multiple", "", "", ""])
for j, (pe, link) in enumerate(zip(SENS_PE, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["pe"]) if link else pe)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (e, link) in enumerate(zip(SENS_EPS, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value="=Financials!G16" if link else e)
    c.number_format = USD2; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=f"=$A{rr}*{col}$4").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells more than 15% above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">"&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["Middle row links to the model's FY29E EPS and the middle column to the base multiple."])

# ===================================================================== PEERS
ws = sheet("Peers", "PEER MULTIPLES (FORWARD P/E, stockanalysis.com, 6 OCTOBER 2026)", [26, 16, 14, 80])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "What they make"])
for i, (co, tk, pe, what) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if co == NAME else Font()
    ws.cell(row=rr, column=2, value=tk)
    c = ws.cell(row=rr, column=3, value=("=" + A["fwdpe"]) if co == NAME else pe)
    c.number_format = MULT; c.font = F_LINK if co == NAME else F_IN
    ws.cell(row=rr, column=4, value=what).alignment = WRAP
ws["A13"] = "Median, six peers (excluding Marvell)"; ws["C13"] = "=MEDIAN(C6:C11)"; ws["C13"].number_format = MULT
note(ws, 15, ["Forward P/E as shown on stockanalysis.com during US trading on 6 October 2026 (Marvell at the 7 October close). Multiples only, to set the base multiple.",
              "No view on the peers' shares is expressed."])

# ===================================================================== SOURCES
ws = sheet("Sources", "SOURCES", [6, 130])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Marvell results releases (Exhibit 99.1 to Form 8-K), 3 December 2024 to 27 August 2026, with comparatives: revenue, data centre revenue, non-GAAP gross and operating margin, EPS, diluted shares, stock-based pay, balance sheet, Q3 FY27 guide.",
    "Marvell Form 10-Q for the quarter to 1 August 2026 (filed 28 August 2026): shares outstanding (876.9m, 21 August 2026), Celestial AI consideration and contingent consideration (up to 22.4m shares and about US$233m cash), prepayments on supply capacity reservation agreements (US$487.0m against US$278.8m), capacity reservation arrangements, customer and distributor shares.",
    "Marvell Form 10-K for fiscal 2026 (filed 11 March 2026) and fiscal 2025 (filed 12 March 2025): ten largest customers 82% and 81% of revenue; purchase commitments with foundries and test and assembly partners.",
    "Marvell Form 8-K of 31 March 2026: US$2.0bn Series A convertible preferred to Nvidia, convertible into up to 21,778,000 shares at about US$91.84. Form 8-K of 19 August 2026: Google warrant, 58,970,907 shares at US$206.58.",
    "Marvell earnings calls: Q4 FY26 (5 March 2026; custom US$1.5bn, switching above US$300m, Celestial run rates), Q1 FY27 (27 May 2026; interconnect above 70% growth, US$1bn prepayments), Q2 FY27 (27 August 2026; US$12bn and US$18bn outlooks, opex, tax, pluggable modules, Investor Day). Transcripts from stockanalysis.com.",
    "Marvell Investor Day presentation, 6 October 2026 (investor.marvell.com): FY28 outlook about US$20bn (slide 33), data centre about US$18bn in FY28 (slide 36), FY29 custom US$12bn+ (slide 28), FY31 revenue US$70bn to 90bn and its split (slides 38 to 40), FY31 target model: gross margin 56 to 59%, operating margin 44 to 46%, tax 15%, FCF above 36%, EPS above US$30 (slide 142). Not filed on Form 8-K by 8 October 2026.",
    "Nasdaq.com historical prices, retrieved 6 October 2026: daily and month-end closes to 5 October, 52-week range. Closes for 6 and 7 October from stockanalysis.com, retrieved 8 October 2026.",
    "stockanalysis.com: FY27 consensus EPS and average target (updated 7 October 2026), FY28 consensus EPS (S&P Global, updated 2 October 2026, before the Investor Day), forward P/E for the peers (6 October) and Marvell (7 October close).",
    "The Physical Layer, 'Marvell is paid every time AI chips talk to each other, whoever made the chips', 28 September 2026: https://thephysicallayer.fyi/journal/marvell-collects-the-toll/",
    "Estimates for FY27 to FY29 and the data centre split are the author's own. Personal research, not investment advice. I hold no position in Marvell.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# ===================================================================== COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Draft view" if CALL["draft"] else "Call", "=" + V["call"], None, "Draft for Tommy Lau's decision; not yet a call." if CALL["draft"] else "Tommy Lau's call."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Reference price, US$", "=" + A["price"], USD2, "Nasdaq close, 7 October 2026."),
    ("Base value, US$", "=" + V["base"], USD2, "33x FY29E EPS."),
    ("Base value against the price", "=" + V["upb"], PCT1, ""),
    ("Probability-weighted value, US$", "=" + V["wtd"], USD2, "25 / 50 / 25 bear / base / bull."),
    ("FY27E / FY28E / FY29E EPS, US$", '=TEXT(Financials!E16,"0.00")&" / "&TEXT(Financials!F16,"0.00")&" / "&TEXT(Financials!G16,"0.00")', None, "Own estimates, non-GAAP, diluted."),
    ("Horizon", "12 months, to October 2027", None, ""),
    ("Wrong if", "See note", None, WRONG_IF),
    ("What would change my view", "See note", None, "Into no call: a price above about US$310 on unchanged estimates, or FY29 earnings below about US$9.92 a share, such as a custom target cut back towards US$10bn."),
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
    ("Quarterly", "Q1 FY25 to Q2 FY27 reported; my Q3 and Q4 FY27."),
    ("Financials", "FY24A to FY29E: revenue, margins, operating income, net profit, EPS, P/E, consensus."),
    ("DataCentre", "Custom, switching and the remainder (interconnect, storage and other): the claim's test."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Valuation", "Base value, market value, multiples, what the price needs, dilution."),
    ("Sensitivity", "FY29E EPS against multiple."),
    ("Peers", "Forward multiples used to set the base multiple."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t); ws.cell(row=18 + i, column=2, value=d)
ws["A28"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A28"].font = F_NOTE
ws["A29"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."; ws["A29"].font = F_NOTE

order = ["Cover", "Assumptions", "Quarterly", "Financials", "DataCentre", "Scenarios", "Valuation", "Sensitivity", "Peers", "Sources"]
wb._sheets = [wb[n] for n in order]
for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
