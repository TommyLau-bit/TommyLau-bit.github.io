"""Hitachi, Ltd. (TSE: 6501) initiation model: sum of the parts. Live formulas throughout.

House style follows the Vertiv model: navy header rows, navy bold titles, blue font for hardcoded inputs,
yellow fill on my own assumptions, green font for cross-sheet links, black for formulas.
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
JPY0 = '"¥"#,##0'
JPY2 = '"¥"#,##0.00'
BN2 = '#,##0.00'
BN3 = '#,##0.000'
PCT1 = '0.0%'
PCT0 = '0%'
MULTF = '0.0"x"'
MULT0 = '0"x"'
SUB = "Tommy Lau | Hitachi, Ltd. (TSE: 6501) | 22 October 2026 | Personal research, not investment advice."

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
ws = sheet("Cover", "HITACHI, LTD. (TSE: 6501)  INITIATION MODEL", [40, 24, 90])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [52, 14, 10, 100])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. Yen billion unless stated. Fiscal year ends 31 March.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"he_g27", "he_m27", "fx27", "g_dss", "g_ci", "g_mob", "g_oth", "eo27", "corp27",
        "x_he", "x_eo", "x_dss", "x_ci", "x_mob", "x_oth", "x_corp"}
Q1 = "Q1 FY2026 results outline and supplement, 29 July 2026"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "¥", "TSE close, 21 October 2026 (a record close). Yahoo Finance 6501.T, retrieved 22 October 2026."),
    ("hiintra", "All-time intraday high, 10 February 2026", HI_INTRA, "¥", "Yahoo Finance 6501.T."),
    ("issued", "Issued shares including treasury stock, 30 June 2026", SHARES_ISSUED, "m", Q1 + ": 4,535,560,985."),
    ("treas", "Treasury stock, 30 June 2026", TREASURY, "m", Q1 + ": 64,552,492."),
    ("cash", "Cash and cash equivalents, 30 June 2026", CASH, "¥bn", Q1 + ", statement of financial position."),
    ("debt", "Interest-bearing debt, 30 June 2026", DEBT, "¥bn", "Short-term debt 61.1 + current portion of long-term debt 432.9 + long-term debt 562.9."),
    ("eqm", "Investments accounted for using the equity method", EQUITY_METHOD, "¥bn", "Book value, 30 June 2026. Taken at book."),
    ("sec", "Non-current investments in securities and other financial assets", SECURITIES, "¥bn", "Book value, 30 June 2026. Taken at book."),
    ("nci", "Non-controlling interests", NCI, "¥bn", "Book value, 30 June 2026. Deducted at book."),
    ("pens", "Retirement and severance benefits liability", PENSION, "¥bn", "30 June 2026. Deducted."),
    ("eps26", "FY2026 EPS forecast (Hitachi)", EPS26, "¥", "Raised on 29 July 2026 from ¥188.78."),
    ("cons26", "FY2026 consensus EPS (year to March 2027)", CONS_EPS_26, "¥", "stockanalysis.com (S&P Global data), retrieved and reconfirmed 22 October 2026. Cross-check only."),
    ("constp", "Average analyst target", CONS_TP, "¥", "stockanalysis.com, 14 analysts, updated 17 September 2026; range ¥5,500 to ¥7,500. Cross-check only."),
    ("GROUP, FY2025 ACTUAL (RESTATED) AND FY2026 FORECAST (RAISED 29 JULY 2026)", None, None, None, None),
    ("grev25", "Group revenue, FY2025", GROUP_REV25, "¥bn", "FY2025 results outline, 27 April 2026."),
    ("geb25", "Group adjusted EBITA, FY2025", GROUP_EBITA25, "¥bn", "FY2025 results outline."),
    ("grev26", "Group revenue, FY2026 forecast", GROUP_REV26, "¥bn", Q1 + ". Raised from ¥11,100bn."),
    ("geb26", "Group adjusted EBITA, FY2026 forecast", GROUP_EBITA26, "¥bn", Q1 + ". Raised from ¥1,420bn."),
]
for k in SEGS:
    rows.append((f"r25_{k}", f"{SEG_NAMES[k]} revenue, FY2025 (restated)", REV25[k], "¥bn", "Q1 FY2026 supplement (FY2025 revised for the April 2026 segment changes)."))
    rows.append((f"e25_{k}", f"{SEG_NAMES[k]} adjusted EBITA, FY2025 (restated)", EBITA25[k], "¥bn", "Q1 FY2026 supplement."))
    rows.append((f"r26_{k}", f"{SEG_NAMES[k]} revenue, FY2026 forecast", REV26[k], "¥bn", Q1 + ", p29."))
    rows.append((f"e26_{k}", f"{SEG_NAMES[k]} adjusted EBITA, FY2026 forecast", EBITA26[k], "¥bn", Q1 + ", p29."))
rows += [
    ("fx26", "Assumed yen per US dollar, Q2 to Q4 FY2026", FX_USD26, "¥", Q1 + ", p19."),
    ("HITACHI ENERGY (US$ BILLION, AS HITACHI REPORTS)", None, None, None, None),
    ("he_r24", "Revenue, FY2024", HE_REV[0], "US$bn", "FY2024 results outline, 28 April 2025."),
    ("he_r25", "Revenue, FY2025", HE_REV[1], "US$bn", "FY2025 results outline, p25."),
    ("he_r26", "Revenue, FY2026 forecast", HE_REV[2], "US$bn", Q1 + ", p23. Raised from US$23.2bn in April."),
    ("he_m24", "Adjusted EBITA margin, FY2024", HE_MARGIN[0], "%", "FY2024 results outline."),
    ("he_m25", "Adjusted EBITA margin, FY2025", HE_MARGIN[1], "%", "FY2025 results outline, p25."),
    ("he_m26", "Adjusted EBITA margin, FY2026 forecast", HE_MARGIN[2], "%", Q1 + ", p23. Raised from 14.3%."),
    ("he_e24", "Adjusted EBITA, FY2024", HE_EBITA[0], "US$bn", "FY2024 results outline."),
    ("he_e25", "Adjusted EBITA, FY2025", HE_EBITA[1], "US$bn", "FY2025 results outline, p25."),
    ("he_e26", "Adjusted EBITA, FY2026 forecast", HE_EBITA[2], "US$bn", Q1 + ", p23."),
    ("he_t27r", "FY2027 revenue target", HE_TGT27["rev"], "US$bn", "Investor Day, Energy Business Strategy, 10 June 2026, p3: about US$26bn."),
    ("he_t27m", "FY2027 adjusted EBITA margin target", HE_TGT27["m"], "%", "Investor Day: 15%+."),
    ("he_t30r", "FY2030 revenue ambition", HE_TGT30["rev"], "US$bn", "Investor Day, p10, stated at Hitachi's 2026 budget exchange rate."),
    ("he_q1r25", "Revenue, Q1 FY2025", HE_Q1_REV25, "US$bn", "Derived: Q1 FY2026 US$5.40bn less the US$0.99bn year-on-year increase."),
    ("he_q1r26", "Revenue, Q1 FY2026", HE_Q1_REV26, "US$bn", Q1 + ", p23."),
    ("MY ASSUMPTIONS, FY2027 (YEAR TO MARCH 2028)", None, None, None, None),
    ("he_g27", "Hitachi Energy revenue growth in US$", HE_G27, "%", "MY ASSUMPTION. Close to the plan's pace to FY2030 (about 12% a year) and to the FY2027 target of about US$26bn."),
    ("he_m27", "Hitachi Energy adjusted EBITA margin", HE_M27, "%", "MY ASSUMPTION. Above the 15%+ target, below the FY2030 range of 16 to 20%."),
    ("fx27", "Yen per US dollar, FY2027", FX27, "¥", "MY ASSUMPTION. Held at Hitachi's own FY2026 assumption."),
    ("g_dss", "Digital Systems & Services adjusted EBITA growth", G27["DSS"], "%", "MY ASSUMPTION. Hitachi expects DSS revenue to grow 6% in FY2026 excluding FX, reorganisation and one-offs (Q1 FY2026 outline, p7)."),
    ("g_ci", "Connective Industries adjusted EBITA growth", G27["CI"], "%", "MY ASSUMPTION."),
    ("g_mob", "Mobility adjusted EBITA growth", G27["Mobility"], "%", "MY ASSUMPTION. Rail Control margin gains."),
    ("g_oth", "Others adjusted EBITA growth", G27["Others"], "%", "MY ASSUMPTION."),
    ("eo27", "Energy segment excluding Hitachi Energy, adjusted EBITA", EOTHER27, "¥bn", "MY ASSUMPTION. FY2026: ¥576bn segment less ¥560bn Hitachi Energy = ¥16bn (mainly Nuclear Energy)."),
    ("corp27", "Corporate items and eliminations, adjusted EBITA", CORP27, "¥bn", "MY ASSUMPTION. FY2026 forecast minus ¥96bn; strategic investment rising."),
    ("x_he", "Multiple, Hitachi Energy, EV / FY2027E adjusted EBITA", MULT["HE"], "x", "MY ASSUMPTION. Grid peers' median trailing EV/EBIT 24.5x (Peers tab), less a year of growth."),
    ("x_eo", "Multiple, Energy rest (nuclear)", MULT["Eother"], "x", "MY ASSUMPTION."),
    ("x_dss", "Multiple, Digital Systems & Services", MULT["DSS"], "x", "MY ASSUMPTION. Fujitsu 17.4x, NEC 19.1x trailing EV/EBIT."),
    ("x_ci", "Multiple, Connective Industries", MULT["CI"], "x", "MY ASSUMPTION. Mitsubishi Electric 19.1x trailing EV/EBIT."),
    ("x_mob", "Multiple, Mobility", MULT["Mobility"], "x", "MY ASSUMPTION. Alstom 10.3x trailing EV/EBIT."),
    ("x_oth", "Multiple, Others", MULT["Others"], "x", "MY ASSUMPTION."),
    ("x_corp", "Multiple, corporate costs (capitalised)", MULT["Corporate"], "x", "MY ASSUMPTION. About the blended multiple of the other businesses."),
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
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else ("#,##0.000" if unit == "m" else (JPY2 if unit == "¥" else BN2)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  HITACHI ENERGY
ws = sheet("HitachiEnergy", "HITACHI ENERGY: REVENUE, MARGIN AND ADJUSTED EBITA", [50, 13, 13, 14, 13, 13])
head(ws, 4, ["US$ billion unless stated", "FY2024A", "FY2025A", "FY2026 forecast", "FY2027E*", "FY2030 plan"])
he = [
    ("Revenue, US$bn", [L("he_r24"), L("he_r25"), L("he_r26"), "=D5*(1+" + A["he_g27"] + ")", L("he_t30r")], BN2),          # 5
    ("Revenue growth", [None, "=C5/B5-1", "=D5/C5-1", "=E5/D5-1", None], PCT1),                                                  # 6
    ("Adjusted EBITA margin", [L("he_m24"), L("he_m25"), L("he_m26"), L("he_m27"), None], PCT1),                                # 7
    ("Adjusted EBITA, US$bn", [L("he_e24"), L("he_e25"), L("he_e26"), "=E5*E7", None], BN3),                                     # 8
    ("Yen per US$", [None, None, L("fx26"), L("fx27"), None], "0"),                                                              # 9
    ("Adjusted EBITA, ¥bn", [None, None, "=D8*D9", "=E8*E9", None], BN2),                                                        # 10
    ("Revenue, ¥bn", [None, None, "=D5*D9", "=E5*E9", None], BN2),                                                               # 11
]
r = 5
for label, vals, fmt in he:
    ws.cell(row=r, column=1, value=label).font = F_B if label.startswith(("Revenue, US", "Adjusted EBITA, ¥")) else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=r, column=2 + j, value=v if v is not None else "")
        c.number_format = fmt; c.alignment = RIGHT
        if isinstance(v, str) and v.startswith("=Assumptions"): c.font = F_LINK
    r += 1
ws["A13"] = "Share of Hitachi, FY2026 forecast"; ws["A13"].font = Font(bold=True, color=NAVY)
ws["A14"] = "Hitachi Energy revenue / group revenue"; ws["B14"] = "=D11/" + A["grev26"]
ws["A15"] = "Hitachi Energy adjusted EBITA / group adjusted EBITA"; ws["B15"] = "=D10/" + A["geb26"]
ws["A16"] = "Hitachi Energy adjusted EBITA / sum of segments excluding corporate"
ws["B16"] = "=D10/(" + "+".join(A[f"e26_{k}"] for k in ["DSS", "Energy", "Mobility", "CI", "Others"]) + ")"
for c in ("B14", "B15", "B16"): ws[c].number_format = PCT1
ws["A18"] = "Hitachi's forecasts for Hitachi Energy, FY2025, as the year went on"; ws["A18"].font = Font(bold=True, color=NAVY)
head(ws, 19, ["Date", "Revenue, US$bn", "Margin"])
for i, (d, rv, m) in enumerate(HE_GUIDE_HIST):
    ws.cell(row=20 + i, column=1, value=d)
    c = ws.cell(row=20 + i, column=2, value=rv); c.font = F_IN; c.number_format = BN2
    c = ws.cell(row=20 + i, column=3, value=m); c.font = F_IN; c.number_format = PCT1
note(ws, 25, [
    "*FY2027E is my own estimate, not Hitachi's. FY2024 to FY2026 are Hitachi's reported figures and forecast for Hitachi Energy in US dollars.",
    "Hitachi's FY2027 target is about US$26bn of revenue at a 15%+ margin; its FY2030 ambition US$36bn at 16 to 20% (Investor Day, 10 June 2026).",
    "The yen conversion uses Hitachi's assumed ¥160 to the dollar. Power Grids BU (incl. Hitachi Energy) forecast: revenue ¥3,783.5bn, adjusted EBITA ¥550.5bn.",
])

# =====================================================================  SEGMENTS
ws = sheet("Segments", "SEGMENTS: ADJUSTED EBITA, FY2025A TO FY2027E (¥ BILLION)", [46, 13, 13, 13, 13, 12, 13])
head(ws, 4, ["Part", "FY2025A revenue", "FY2026F revenue", "FY2025A EBITA", "FY2026F EBITA", "Growth*", "FY2027E EBITA*"])
seg_rows = [
    ("Hitachi Energy", None, "=HitachiEnergy!D11", None, "=HitachiEnergy!D10", "=HitachiEnergy!E5/HitachiEnergy!D5-1", "=HitachiEnergy!E10"),
    ("Energy, rest (mainly Nuclear Energy)", None, "=" + A["r26_Energy"] + "-C5", None, "=" + A["e26_Energy"] + "-E5", None, L("eo27")),
    ("Digital Systems & Services", L("r25_DSS"), L("r26_DSS"), L("e25_DSS"), L("e26_DSS"), L("g_dss"), "=E7*(1+F7)"),
    ("Connective Industries", L("r25_CI"), L("r26_CI"), L("e25_CI"), L("e26_CI"), L("g_ci"), "=E8*(1+F8)"),
    ("Mobility", L("r25_Mobility"), L("r26_Mobility"), L("e25_Mobility"), L("e26_Mobility"), L("g_mob"), "=E9*(1+F9)"),
    ("Others", L("r25_Others"), L("r26_Others"), L("e25_Others"), L("e26_Others"), L("g_oth"), "=E10*(1+F10)"),
    ("Corporate items and eliminations", L("r25_Corporate"), L("r26_Corporate"), L("e25_Corporate"), L("e26_Corporate"), None, L("corp27")),
    ("Group total", "=SUM(B5:B11)+" + A["r25_Energy"], "=SUM(C5:C11)", "=SUM(D5:D11)+" + A["e25_Energy"], "=SUM(E5:E11)", "=G12/E12-1", "=SUM(G5:G11)"),
]
for i, (lab, *vals) in enumerate(seg_rows):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B if lab == "Group total" else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v if v is not None else "")
        c.number_format = PCT1 if j == 4 else BN2; c.alignment = RIGHT
        if isinstance(v, str) and v.startswith("=Assumptions"): c.font = F_LINK
ws["A14"] = "Check: group total against Hitachi's FY2026 forecast"; ws["E14"] = "=E12-" + A["geb26"]; ws["C14"] = "=C12-" + A["grev26"]
ws["A15"] = "Energy segment as reported (FY2025A, FY2026F)"; ws["B15"] = L("r25_Energy"); ws["C15"] = L("r26_Energy")
ws["D15"] = L("e25_Energy"); ws["E15"] = L("e26_Energy")
for c in ("C14", "E14", "B15", "C15", "D15", "E15"): ws[c].number_format = BN2
note(ws, 17, [
    "*Growth rates and FY2027E are my own estimates. FY2025A is restated for the April 2026 segment changes (Q1 FY2026 supplement).",
    "FY2025A revenue and EBITA for Hitachi Energy alone in yen are not split here; the group FY2025A total adds back the Energy segment as reported.",
])

# =====================================================================  VALUATION (SUM OF THE PARTS)
ws = sheet("Valuation", "VALUATION: SUM OF THE PARTS ON FY2027E ADJUSTED EBITA", [58, 14, 10, 16, 12, 60])
head(ws, 4, ["Part", "FY2027E EBITA", "Multiple", "Value, ¥bn", "Share", "Working / note"])
parts = [("Hitachi Energy", 5, "x_he"), ("Energy, rest (mainly nuclear)", 6, "x_eo"), ("Digital Systems & Services", 7, "x_dss"),
         ("Connective Industries", 8, "x_ci"), ("Mobility", 9, "x_mob"), ("Others", 10, "x_oth"), ("Corporate costs", 11, "x_corp")]
for i, (lab, srow, mk) in enumerate(parts):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f"=Segments!G{srow}"); c.font = F_LINK; c.number_format = BN2
    c = ws.cell(row=rr, column=3, value="=" + A[mk]); c.font = F_LINK; c.number_format = MULT0
    ws.cell(row=rr, column=4, value=f"=B{rr}*C{rr}").number_format = BN2
    ws.cell(row=rr, column=5, value=f"=D{rr}/$D$19").number_format = PCT0
V = {}
vrows = [
    (12, "Enterprise value of the parts", "=SUM(D5:D11)", BN2, ""),
    (13, "Net cash: cash less interest-bearing debt, 30 June 2026", "=" + A["cash"] + "-" + A["debt"], BN2, ""),
    (14, "Add equity-method investments at book", L("eqm"), BN2, ""),
    (15, "Add other long-term investments at book", L("sec"), BN2, ""),
    (16, "Less non-controlling interests at book", "=-" + A["nci"], BN2, ""),
    (17, "Less retirement and severance benefits liability", "=-" + A["pens"], BN2, ""),
    (18, "Bridge from enterprise value to equity value", "=SUM(D13:D17)", BN2, ""),
    (19, "Equity value, ¥bn", "=D12+D18", BN2, ""),
    (20, "Shares outstanding, m (issued less treasury, 30 June 2026)", "=" + A["issued"] + "-" + A["treas"], "#,##0.0", "No further buybacks assumed."),
    (21, "BASE VALUE PER SHARE, ¥", "=D19/D20*1000", JPY0, ""),
    (22, "Reference price, ¥", L("price"), JPY0, "TSE close, 21 October 2026."),
    (23, "Base value against price", "=D21/D22-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (24, "VIEW ON THE BAND", '=IF(D23>=0.15,"LONG",IF(D23<=-0.25,"SHORT","NO CALL"))', None, "Tommy Lau's call, 22 October 2026: NO CALL, Medium conviction."),
    (26, "Market value, ¥bn", "=D20*D22/1000", BN2, ""),
    (27, "Adjusted enterprise value at the price, ¥bn", "=D26-D18", BN2, "Market value less the bridge items."),
    (28, "EV / FY2026 forecast group adjusted EBITA", "=D27/Segments!E12", MULTF, ""),
    (29, "EV / FY2027E group adjusted EBITA", "=D27/Segments!G12", MULTF, ""),
    (30, "P/E on Hitachi's FY2026 EPS forecast", "=D22/" + A["eps26"], MULTF, ""),
    (31, "P/E on FY2026 consensus EPS", "=D22/" + A["cons26"], MULTF, "Cross-check only."),
    (32, "Value the price leaves for Hitachi Energy, ¥bn", "=D27-SUM(D6:D11)", BN2, "Rest of Hitachi at my base multiples."),
    (33, "That value / Hitachi Energy FY2027E EBITA", "=D32/B5", MULTF, ""),
    (34, "That value in US$bn at the FY2027 rate", "=D32/" + A["fx27"], BN2, ""),
    (35, "Hitachi Energy multiple needed for base value 15% above price", "=(D22*1.15*D20/1000-D18-SUM(D6:D11))/B5", MULTF, ""),
    (36, "Price at which the base value is 15% above it, ¥", "=D21/1.15", JPY0, "Revisit level for a LONG."),
    (37, "Price at which the base value is 25% below it, ¥", "=D21/0.75", JPY0, "Revisit level for a SHORT."),
    (38, "Hitachi Energy share of FY2026 forecast revenue", "=HitachiEnergy!B14", PCT1, ""),
    (39, "Hitachi Energy share of FY2026 forecast adjusted EBITA", "=HitachiEnergy!B15", PCT1, ""),
    (40, "Hitachi Energy share of my sum of the parts equity value", "=D5/D19", PCT1, ""),
    (41, "Hitachi Energy share of market value, as implied", "=D32/D26", PCT1, ""),
    (42, "Price against the all-time intraday high", "=D22/" + A["hiintra"] + "-1", PCT1, "¥6,039 on 10 February 2026."),
]
for rr, lab, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=4, value=f)
    if fmt: c.number_format = fmt
    if rr in (21, 24):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    if isinstance(f, str) and f.startswith("=Assumptions"): c.font = F_LINK
    ws.cell(row=rr, column=6, value=nt).alignment = WRAP
ws["E18"] = "=D18/$D$19"; ws["E18"].number_format = PCT0
ws["A12"].font = F_B; ws["A19"].font = F_B

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT", [12, 12, 12, 12, 13, 14, 14, 15, 13, 11])
head(ws, 4, ["Case", "HE growth", "HE margin", "HE multiple", "Other multiples +/-", "HE revenue US$bn", "HE EBITA ¥bn",
             "Rest of Hitachi EV ¥bn", "Value, ¥", "vs price"])
r = 5
for name, g, m, mult, dlt, p in SCEN:
    ws.cell(row=r, column=1, value=name).font = F_B
    if name == "Base":
        for j, k in enumerate(["he_g27", "he_m27", "x_he"]):
            c = ws.cell(row=r, column=2 + j, value="=" + A[k]); c.font = F_LINK
        c = ws.cell(row=r, column=5, value=0); c.font = F_INB; c.fill = FILL_ASSUME
    else:
        for j, v in enumerate([g, m, mult, dlt]):
            c = ws.cell(row=r, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME
    for col in (2, 3): ws.cell(row=r, column=col).number_format = PCT1
    ws.cell(row=r, column=4).number_format = MULT0; ws.cell(row=r, column=5).number_format = '+0;-0;0'
    ws.cell(row=r, column=6, value=f"=HitachiEnergy!$D$5*(1+B{r})").number_format = BN2
    ws.cell(row=r, column=7, value=f"=F{r}*C{r}*{A['fx27']}").number_format = BN2
    ws.cell(row=r, column=8, value=f"=SUMPRODUCT(Valuation!$B$6:$B$11,Valuation!$C$6:$C$11+E{r})").number_format = BN2
    ws.cell(row=r, column=9, value=f"=(G{r}*D{r}+H{r}+Valuation!$D$18)/Valuation!$D$20*1000").number_format = JPY0
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
    "Hitachi Energy (HE) cases start from Hitachi's FY2026 forecast of US$23.65bn and convert at ¥160. The rest of Hitachi keeps my FY2027E EBITA;",
    "only its multiples move, two turns lower in the bear case and two higher in the bull case (corporate costs included). Same bridge and shares in every case.",
    "Bear: orders slow, margin flat at the FY2026 forecast, grid names de-rate to 14x. Bull: margin 16.5%, the bottom of the FY2030 range reached early, 25x.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: HITACHI ENERGY FY2027E EBITA AGAINST ITS MULTIPLE (¥)", [30, 14, 14, 14])
head(ws, 4, ["HE EBITA (¥bn) \\ multiple", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_MULT, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["x_he"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (e, link) in enumerate(zip(SENS_HE, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value="=HitachiEnergy!E10" if link else e)
    c.number_format = BN2; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j,
                value=f"=($A{rr}*{col}$4+SUM(Valuation!$D$6:$D$11)+Valuation!$D$18)/Valuation!$D$20*1000").number_format = JPY0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["Rest of Hitachi at my base. The middle row links to the model's Hitachi Energy FY2027E EBITA and the middle column to the base multiple."])

# =====================================================================  QUEUE
ws = sheet("Queue", "HITACHI ENERGY ORDER BACKLOG AND THE CLAIM'S TEST", [56] + [11] * 6)
head(ws, 4, ["US$ billion unless stated"] + HE_BL_LABELS)
for j, v in enumerate(HE_BL):
    c = ws.cell(row=5, column=2 + j, value=v); c.font = F_IN; c.number_format = BN2
ws["A5"] = "Order backlog at quarter end"; ws["A5"].font = F_B
ws["A6"] = "Revenue over the previous four quarters (where derivable)"
ws["B6"] = "=" + A["he_r24"]; ws["F6"] = "=" + A["he_r25"]; ws["G6"] = f"={A['he_r25']}-{A['he_q1r25']}+{A['he_q1r26']}"
ws["A7"] = "Backlog / revenue over the previous four quarters"
for col in ("B", "F", "G"):
    ws[f"{col}6"].number_format = BN2
    ws[f"{col}7"] = f"={col}5/{col}6"; ws[f"{col}7"].number_format = '0.00"x"'
ws["A8"] = "Growth in backlog, March 2025 to June 2026"; ws["B8"] = "=G5/B5-1"; ws["B8"].number_format = PCT1
ws["A10"] = "The claim's floor"; ws["B10"] = CLAIM_FLOOR; ws["B10"].font = F_IN; ws["B10"].number_format = '0.0"x"'
ws["A11"] = "FY2030 plan: backlog about US$100bn / revenue US$36bn"; ws["B11"] = f"={HE_TGT30['backlog']}/{A['he_t30r']}"; ws["B11"].number_format = '0.00"x"'
ws["A13"] = "Orders against revenue"; ws["A13"].font = Font(bold=True, color=NAVY)
head(ws, 14, ["Year", "Orders, US$bn", "Revenue, US$bn", "Orders / revenue"])
for i, (y, rk) in enumerate([("FY2024", "he_r24"), ("FY2025", "he_r25")]):
    rr = 15 + i
    ws.cell(row=rr, column=1, value=y)
    c = ws.cell(row=rr, column=2, value=HE_ORDERS[y]); c.font = F_IN; c.number_format = BN2
    c = ws.cell(row=rr, column=3, value="=" + A[rk]); c.font = F_LINK; c.number_format = BN2
    ws.cell(row=rr, column=4, value=f"=B{rr}/C{rr}").number_format = '0.00"x"'
ws["A17"] = "Power Grids BU, Q1 FY2026, ¥bn: orders / revenue"
ws["B17"] = Q1_PG_ORDERS; ws["C17"] = Q1_PG_REV; ws["D17"] = "=B17/C17"
ws["B17"].font = F_IN; ws["C17"].font = F_IN; ws["D17"].number_format = '0.00"x"'
note(ws, 19, [
    "Sources: Hitachi results presentations of 28 April 2025 (US$43.6bn), 31 July 2025 (US$47.6bn), 30 October 2025 (US$49.7bn), 29 January 2026 (US$56.7bn),",
    "27 April 2026 (US$57.9bn; orders US$32.8bn FY2025, US$27.9bn FY2024) and 29 July 2026 (US$63.6bn; Power Grids orders ¥1,871.6bn). FY2024 revenue as first reported, US$15.7bn.",
    "Quarterly Hitachi Energy revenue for FY2024 is not used, so the ratio is shown only at March 2025, March 2026 and June 2026.",
])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, RETRIEVED 22 OCTOBER 2026)", [22, 14, 13, 18, 70])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "EV/EBIT (trailing)", "What they make"])
for i, (co, tk, pe, eve, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, v in enumerate([pe, eve]):
        c = ws.cell(row=rr, column=3 + j, value=v); c.number_format = MULTF; c.font = F_IN
    ws.cell(row=rr, column=5, value=what).alignment = WRAP
ws["A16"] = "Grid equipment median (rows 6 to 10)"; ws["A16"].font = F_B
ws["C16"] = "=MEDIAN(C6:C10)"; ws["D16"] = "=MEDIAN(D6:D10)"
ws["A17"] = "IT services median (rows 11 to 12)"; ws["A17"].font = F_B
ws["C17"] = "=MEDIAN(C11:C12)"; ws["D17"] = "=MEDIAN(D11:D12)"
for c in ("C16", "D16", "C17", "D17"): ws[c].number_format = MULTF
note(ws, 19, ["Multiples only, to set the range of segment multiples. No view on the peers' shares is expressed. GE Vernova is left out: its",
              "trailing EV/EBIT of 87x reflects earnings still recovering and would distort the median."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 140])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Hitachi, Outline of Consolidated Financial Results for the First Quarter Ended June 30, 2026, 29 July 2026 (2026_1Qpre.pdf): segment results, raised FY2026 forecast, Hitachi Energy in US$ (p23), orders and backlog (p17), FX assumptions, buybacks.",
    "Hitachi, Consolidated Financial Results for Q1 FY2026 and Supplemental Material (2026_1Q.pdf, 2026_1Qsup.xlsx), 29 July 2026: balance sheet, issued shares and treasury stock, restated FY2025 segments.",
    "Hitachi, Outline of Consolidated Financial Results for FY2025, 27 April 2026: FY2025 results, the April FY2026 forecast, Hitachi Energy FY2025 and its orders and backlog.",
    "Hitachi results presentations of 28 April 2025, 31 July 2025 (page 11: Hitachi Energy backlog US$47.6bn at 30 June 2025), 30 October 2025 and 29 January 2026: earlier Hitachi Energy backlog and FY2025 forecasts.",
    "Hitachi Investor Day 2026, Energy Business Strategy (Andreas Schierenbeck) and Q&A summary, 10 June 2026: backlog ratio 2.5 to 3x, US$100bn 2030 backlog, >US$9bn investment, FY2027 and FY2030 targets, DSS pricing pressure.",
    "Hitachi investor relations library, hitachi.com/en/ir/library/fr/: Q2 FY2026 results on 28 October 2026, webcast 17:00 to 18:00 JST.",
    "Yahoo Finance, 6501.T, retrieved 22 October 2026: daily and month-end closes, highs and lows (split-adjusted).",
    "stockanalysis.com, retrieved 22 October 2026: Hitachi consensus EPS and average target (updated 17 September 2026), peer forward P/E and trailing EV/EBIT.",
    "The Physical Layer, 'Hitachi Energy is spending more than $9 billion on factories, and still plans a three-year queue', 22 October 2026: https://thephysicallayer.fyi/journal/hitachi-energy-plans-the-queue/",
    "Estimates for FY2027 are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Call (Tommy Lau, 22 October 2026)", "=Valuation!D24", None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    ("Base value per share, ¥", "=Valuation!D21", JPY0, "Sum of the parts on FY2027E adjusted EBITA, plus the bridge, over shares outstanding."),
    ("Reference price, ¥", "=" + A["price"], JPY0, "TSE close, 21 October 2026."),
    ("Base value against price", "=Valuation!D23", PCT1, ""),
    ("Probability-weighted value, ¥", "=Scenarios!E11", JPY0, "25 / 50 / 25 bear / base / bull."),
    ("Hitachi Energy share of my equity value", "=Valuation!D40", PCT1, ""),
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
    ("HitachiEnergy", "Revenue, margin and adjusted EBITA in US$, FY2024A to FY2027E; share of Hitachi; forecast history."),
    ("Segments", "Adjusted EBITA by part, FY2025A, FY2026 forecast, FY2027E."),
    ("Valuation", "Sum of the parts, the bridge, base value, the band, what the price implies for Hitachi Energy."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "Hitachi Energy FY2027E EBITA against its multiple."),
    ("Queue", "Order backlog, backlog to revenue, orders against revenue: the claim's tests."),
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
