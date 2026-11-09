"""Wärtsilä Oyj Abp (Nasdaq Helsinki: WRT1V) initiation model: sum of the parts. Live formulas throughout.

House style follows the Vertiv and Siemens Energy models: navy header rows, navy bold titles, blue font for hardcoded inputs,
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

EUR0 = '"€"#,##0'
EUR2 = '"€"#,##0.00'
N0 = '#,##0'
BN2 = '#,##0.00'
PCT1 = '0.0%'
PCT0 = '0%'
MULTF = '0.0"x"'
MULT0 = '0"x"'
DLONG = datetime.date.fromisoformat(DATE).strftime("%-d %B %Y")
SUB = f"Tommy Lau | Wärtsilä Oyj Abp (Nasdaq Helsinki: WRT1V) | {DLONG} | Personal research, not investment advice."
Q3 = "Interim Report January-September 2026, 27 October 2026"

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
ws = sheet("Cover", "WÄRTSILÄ OYJ ABP (NASDAQ HELSINKI: WRT1V)  INITIATION MODEL", [40, 24, 90])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [58, 14, 10, 100])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. Euro million unless stated. Calendar year; continuing operations.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = set()
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "€", "Nasdaq Helsinki close, 30 October 2026. Nasdaq Nordic price history, retrieved 2 November 2026."),
    ("hiclose", "Record close, 23 April 2026", HI_CLOSE, "€", "Nasdaq Nordic; intraday high €40.75 the same day."),
    ("cons27", "2027 consensus EPS", CONS_EPS27, "€", "stockanalysis.com (S&P Global data), retrieved 2 November 2026. Cross-check only."),
    ("constp", "Average analyst target", CONS_TP, "€", "stockanalysis.com, 17 analysts; range €19.50 to €40.00. Cross-check only."),
    ("SHARES AND BALANCE SHEET, 30 SEPTEMBER 2026", None, None, None, None),
    ("shares", "Shares outstanding", SHARES, "m", Q3 + ": 589,801,254; treasury shares 1,922,136 excluded."),
    ("cash", "Cash and cash equivalents, continuing operations", CASH, "€m", Q3 + ". A further €246m sat in assets held for sale and went to the Valo joint venture."),
    ("debt", "Lease liabilities and other interest-bearing debt", DEBT, "€m", Q3 + ": non-current 188 + 256, current 41 + 63."),
    ("nci", "Non-controlling interests, book", NCI_BOOK, "€m", Q3 + ". Taken at book; they earn about €4m a year."),
    ("valo", "50% of Valo (energy storage joint venture)", VALO, "€m", "MY ASSUMPTION. Loss-making in 2026; Wärtsilä expects positive results towards the end of 2027."),
    ("adv", "Advances received", ADVANCES, "€m", Q3 + ". Shown for the risk, not used in the value."),
]
for k in SEGS:
    nm = SEG_NAMES[k]
    rows += [
        (nm.upper(), None, None, None, None),
        (f"r24_{k}", f"{nm} net sales, 2024", REV24[k], "€m", "Financial Statements Bulletin 2025, 4 February 2026."),
        (f"p24_{k}", f"{nm} comparable operating result, 2024", P24[k], "€m", "Financial Statements Bulletin 2025."),
        (f"r25_{k}", f"{nm} net sales, 2025", REV25[k], "€m", Q3 + " (restated)."),
        (f"p25_{k}", f"{nm} comparable operating result, 2025", P25[k], "€m", Q3 + "."),
        (f"r9_{k}", f"{nm} net sales, 9M 2026", REV9M[k], "€m", Q3 + "."),
        (f"p9_{k}", f"{nm} comparable operating result, 9M 2026", P9M[k], "€m", Q3 + "."),
        (f"q4r_{k}", f"{nm} net sales, Q4 2026", Q4_REV[k], "€m", "MY ASSUMPTION. Order book for 2026 deliveries at 30 September: €" + str(BOOK_2026DEL[k]) + "m."),
        (f"q4m_{k}", f"{nm} margin, Q4 2026", Q4_M[k], "%", "MY ASSUMPTION."),
        (f"g27_{k}", f"{nm} net sales growth, 2027", G27[k], "%", "MY ASSUMPTION. Mid-term target: " + TGT[k][0] + " organic growth."),
        (f"m27_{k}", f"{nm} margin, 2027", M27[k], "%", f"MY ASSUMPTION. Mid-term target: {TGT[k][1] * 100:.0f}% operating result."),
    ]
    MINE |= {f"q4r_{k}", f"q4m_{k}", f"g27_{k}", f"m27_{k}"}
rows += [
    ("GROUP", None, None, None, None),
    ("rev25", "Group net sales, 2025 (continuing, restated)", GROUP_REV25, "€m", Q3 + "."),
    ("p25", "Group comparable operating result, 2025", GROUP_P25, "€m", Q3 + "."),
    ("pbr9", "Portfolio Business net sales, 9M 2026 (none after 1 June)", PB_REV9M, "€m", Q3 + "."),
    ("pbp9", "Portfolio Business comparable operating result, 9M 2026", PB_P9M, "€m", Q3 + "."),
    ("fin27", "Financial income and expenses, 2027", FIN27, "€m", "MY ASSUMPTION, for the EPS cross-check only."),
    ("tax27", "Tax rate, 2027", TAX27, "%", "MY ASSUMPTION. 9M 2026: 148 / 611 = 24.2%."),
    ("nci27", "Non-controlling interests' result, 2027", NCI27, "€m", "MY ASSUMPTION. 2025: €4m."),
    ("MULTIPLES (EV / 2027E COMPARABLE OPERATING RESULT)", None, None, None, None),
    ("x_EN", "Energy", MULT["EN"], "x", "MY ASSUMPTION. Engine peers' median trailing EV/EBIT 20.7x (Peers tab); Siemens Energy 26.4x."),
    ("x_MA", "Marine", MULT["MA"], "x", "MY ASSUMPTION. Alfa Laval 20.1x; lower for the cycle in new marine equipment."),
]
MINE |= {"valo", "fin27", "tax27", "nci27", "x_EN", "x_MA"}
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY)
        r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else ("#,##0.000" if unit == "m" else (EUR2 if unit == "€" else N0)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  SEGMENTS
ws = sheet("Segments", "SEGMENTS: NET SALES AND COMPARABLE OPERATING RESULT, 2024A TO 2027E (€ MILLION)", [34] + [12] * 13)
head(ws, 4, ["Segment", "2024 sales", "2024 result", "2025 sales", "2025 result", "9M sales", "9M result", "Q4E sales*",
             "Q4E result*", "2026E sales*", "2026E result*", "2026E margin*", "2027E sales*", "2027E result*"])
for i, k in enumerate(["EN", "MA"]):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=SEG_NAMES[k])
    vals = [L(f"r24_{k}"), L(f"p24_{k}"), L(f"r25_{k}"), L(f"p25_{k}"), L(f"r9_{k}"), L(f"p9_{k}"), L(f"q4r_{k}"),
            f"=H{rr}*{A[f'q4m_{k}']}", f"=F{rr}+H{rr}", f"=G{rr}+I{rr}", f"=K{rr}/J{rr}",
            f"=J{rr}*(1+{A[f'g27_{k}']})", f"=M{rr}*{A[f'm27_{k}']}"]
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v)
        c.number_format = PCT1 if j == 10 else N0; c.alignment = RIGHT
        if v.startswith("=Assumptions"): c.font = F_LINK
ws["A7"] = "Portfolio Business (divested by 1 June 2026)"
ws["F7"] = L("pbr9"); ws["G7"] = L("pbp9"); ws["J7"] = "=F7"; ws["K7"] = "=G7"
for c in ("F7", "G7"): ws[c].font = F_LINK
for c in ("F7", "G7", "J7", "K7"): ws[c].number_format = N0
ws["A8"] = "Wärtsilä, continuing operations"; ws["A8"].font = F_B
ws["D8"] = L("rev25"); ws["E8"] = L("p25"); ws["D8"].font = F_LINK; ws["E8"].font = F_LINK
for col in "JKMN":
    ws[f"{col}8"] = f"=SUM({col}5:{col}7)"; ws[f"{col}8"].font = F_B
for col in "DEJKMN": ws[f"{col}8"].number_format = N0
ws["L8"] = "=K8/J8"; ws["L8"].number_format = PCT1
ws["A9"] = "Group margin, 2027E"; ws["N9"] = "=N8/M8"; ws["N9"].number_format = PCT1
ws["A10"] = "Energy growth, 2026E"; ws["J10"] = "=J5/D5-1"; ws["J10"].number_format = PCT1
ws["A12"] = "EPS cross-check, 2027E (€m)"; ws["A12"].font = Font(bold=True, color=NAVY)
eps = [("Comparable operating result", "=N8", N0), ("Financial income and expenses", L("fin27"), N0),
       ("Result before tax", "=B13+B14", N0), ("Tax", f"=-B15*{A['tax27']}", N0), ("Non-controlling interests", f"=-{A['nci27']}", N0),
       ("Net result to shareholders", "=SUM(B15:B17)", N0), ("Shares outstanding, m", "=" + A["shares"], "#,##0.0"),
       ("EPS 2027E, €", "=B18/B19", EUR2), ("2027 consensus EPS, €", L("cons27"), EUR2), ("Mine against consensus", "=B20/B21-1", PCT1)]
for i, (lab, f, fmt) in enumerate(eps):
    rr = 13 + i
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
ws["A20"].font = F_B; ws["B20"].font = F_B
note(ws, 25, [
    "*Q4 2026, 2026E and 2027E are my own estimates, not Wärtsilä's. Energy Storage is a discontinued operation and is excluded throughout.",
    "IFRS 18 applies from 2027 and moves joint venture results out of the operating result; my 2027E is on today's accounting.",
])

# =====================================================================  ENERGY: THE QUEUE AND DATA CENTRES
ws = sheet("Energy", "ENERGY: ORDERS, NET SALES, ORDER BOOK, MW AND DATA CENTRE ORDERS", [52] + [11] * 7)
head(ws, 4, ["€ million unless stated"] + EN_Q_LABELS)
labs = [("Orders", EN_Q_ORD, N0), ("Net sales", EN_Q_REV, N0), ("Comparable operating result", EN_Q_P, N0),
        ("MW ordered", EN_Q_MW, N0), ("Order book, end of quarter", EN_Q_BOOK, N0)]
for i, (lab, vals, fmt) in enumerate(labs):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab)
    for j, v in enumerate(vals):
        c = ws.cell(row=rr, column=2 + j, value=v); c.font = F_IN; c.number_format = fmt
ws["A10"] = "Orders / net sales"; ws["A11"] = "Margin"
for j in range(7):
    col = get_column_letter(2 + j)
    ws[f"{col}10"] = f"={col}5/{col}6"; ws[f"{col}10"].number_format = '0.00"x"'
    ws[f"{col}11"] = f"={col}7/{col}6"; ws[f"{col}11"].number_format = PCT1
ws["A12"] = "Named data centre MW"
for j, v in enumerate(DC_MW_Q.values()):
    c = ws.cell(row=12, column=6 + j, value=v); c.font = F_IN; c.number_format = N0
ws["A13"] = "Named data centre share of MW"
for j in range(3):
    col = get_column_letter(6 + j)
    ws[f"{col}13"] = f"={col}12/{col}8"; ws[f"{col}13"].number_format = PCT0
rows_e = [
    (15, "Orders, 9M 2026", "=SUM(F5:H5)", N0), (16, "Net sales, 9M 2026", "=SUM(F6:H6)", N0),
    (17, "Orders / net sales, 9M 2026", "=B15/B16", '0.00"x"'),
    (18, "MW ordered, 9M 2026 (as reported; quarters sum to 4,151 on rounding)", EN_MW_9M26, N0), (19, "MW ordered, 9M 2025", "=SUM(B8:D8)", N0),
    (20, "MW growth, 9M", "=B18/B19-1", PCT1),
    (21, "Named data centre MW, 9M 2026", "=SUM(F12:H12)", N0), (22, "Named data centre share, 9M 2026", "=B21/B18", PCT1),
    (23, "MW ordered, 2025", EN_MW_25, N0), (24, "Named data centre MW, 2025 (\"first two projects in the US\")", DC_MW_25, N0),
    (25, "Named data centre share, 2025", "=B24/B23", PCT1),
    (26, "Equipment orders, 9M 2026", EN_EQ_ORD9M, N0), (27, "Equipment net sales, 9M 2026", EN_EQ_REV9M, N0),
    (28, "Equipment orders / equipment sales, 9M 2026", "=B26/B27", '0.00"x"'),
    (29, "Equipment orders from the Americas, 9M 2026", EN_EQ_AMERICAS9M, N0),
    (30, "Order book for 2026 deliveries, 30 September 2026", BOOK_2026DEL["EN"], N0),
    (31, "Order book for 2027 and later", "=H9-B30", N0),
    (32, "Order book / 2025 net sales", "=H9/" + A["r25_EN"], '0.00"x"'),
    (33, "Order book growth, September 2025 to September 2026", "=H9/D9-1", PCT1),
]
for rr, lab, f, fmt in rows_e:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
    if not (isinstance(f, str) and f.startswith("=")): c.font = F_IN
note(ws, 35, [
    "Sources: Wärtsilä interim reports Q1 to Q3 2026 and the 2025 Financial Statements Bulletin (quarterly figures and prior-year quarters).",
    "Named data centre MW: Q1 2026 24 x 50SG engines, 429 MW; Q2 2026 \"1.2 GW of firm data centre-related orders across two projects\"; Q3 2026 15 x 50SG, 282 MW.",
    "The named total is approximate, since 1.2 GW is Wärtsilä's rounded figure, and likely a floor: smaller data centre orders may not be named. The shares are my arithmetic. Equipment orders by region: Q3 2026 result presentation.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: SUM OF THE PARTS ON 2027E COMPARABLE OPERATING RESULT", [60, 14, 10, 16, 12, 60])
head(ws, 4, ["Part", "2027E result, €bn", "Multiple", "Value, €bn", "Share", "Working / note"])
for i, (lab, f, mk) in enumerate([("Energy", "=Segments!N5/1000", "x_EN"), ("Marine", "=Segments!N6/1000", "x_MA")]):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f); c.font = F_LINK; c.number_format = "0.000"
    c = ws.cell(row=rr, column=3, value="=" + A[mk]); c.font = F_LINK; c.number_format = MULT0
    ws.cell(row=rr, column=4, value=f"=B{rr}*C{rr}").number_format = BN2
    ws.cell(row=rr, column=5, value=f"=D{rr}/$D$14").number_format = PCT0
vrows = [
    (8, "Enterprise value of the parts", "=SUM(D5:D6)", BN2, ""),
    (9, "Net cash of continuing operations, 30 September 2026", f"=({A['cash']}-{A['debt']})/1000", BN2, "Cash less lease liabilities and other interest-bearing debt. Wärtsilä's own net debt of minus €2,165m includes €246m held for sale."),
    (10, "Add 50% of Valo", f"={A['valo']}/1000", BN2, "My assumption: nil."),
    (11, "Less non-controlling interests at book", f"=-{A['nci']}/1000", BN2, ""),
    (13, "Bridge from enterprise value to equity value", "=SUM(D9:D11)", BN2, ""),
    (14, "Equity value, €bn", "=D8+D13", BN2, ""),
    (15, "Shares outstanding, m", "=" + A["shares"], "#,##0.0", "30 September 2026."),
    (16, "BASE VALUE PER SHARE, €", "=D14/D15*1000", EUR2, ""),
    (17, "Reference price, €", L("price"), EUR2, "Nasdaq Helsinki close, 30 October 2026."),
    (18, "Base value against price", "=D16/D17-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (19, "VIEW ON THE BAND", '=IF(D18>=0.15,"LONG",IF(D18<=-0.25,"SHORT","NO CALL"))', None, "The call follows the band."),
    (21, "Market value, €bn", "=D15*D17/1000", BN2, ""),
    (22, "Enterprise value at the price, €bn", "=D21-D13", BN2, "Market value less the bridge items."),
    (23, "EV / 2026E comparable operating result", "=D22/(Segments!K8/1000)", MULTF, ""),
    (24, "EV / 2027E comparable operating result", "=D22/(Segments!N8/1000)", MULTF, ""),
    (25, "P/E on 2027 consensus EPS", "=D17/" + A["cons27"], MULTF, "Cross-check only."),
    (26, "P/E on my 2027E EPS", "=D17/Segments!B20", MULTF, ""),
    (27, "Energy multiple the price implies, with Marine at base", "=(D22-D6)/B5", MULTF, ""),
    (28, "Marine multiple the price implies, with Energy at base", "=(D22-D5)/B6", MULTF, ""),
    (29, "Price at which the base value is 15% above it, €", "=D16/1.15", EUR2, "Above this, the band gives NO CALL."),
    (30, "Energy share of my equity value", "=D5/D14", PCT1, ""),
    (31, "Marine share of my equity value", "=D6/D14", PCT1, ""),
    (32, "Price against the record close", "=D17/" + A["hiclose"] + "-1", PCT1, "€39.63 on 23 April 2026."),
    (33, "Marine share of 2025 comparable operating result", f"={A['p25_MA']}/{A['p25']}", PCT1, ""),
]
for rr, lab, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=4, value=f)
    if fmt: c.number_format = fmt
    if rr in (16, 19):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    if isinstance(f, str) and f.startswith("=Assumptions"): c.font = F_LINK
    ws.cell(row=rr, column=6, value=nt).alignment = WRAP
ws["E13"] = "=D13/$D$14"; ws["E13"].number_format = PCT0
ws["A8"].font = F_B; ws["A14"].font = F_B

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT", [12, 12, 12, 10, 12, 12, 10, 14, 13, 11])
head(ws, 4, ["Case", "Marine growth", "Marine margin", "Marine x", "Energy growth", "Energy margin", "Energy x",
             "Energy result €bn", "Value, €", "vs price"])
r = 5
for name, ma, en, p in SCEN:
    ws.cell(row=r, column=1, value=name).font = F_B
    if name == "Base":
        for j, k in enumerate(["g27_MA", "m27_MA", "x_MA", "g27_EN", "m27_EN", "x_EN"]):
            c = ws.cell(row=r, column=2 + j, value="=" + A[k]); c.font = F_LINK
    else:
        for j, v in enumerate([ma[0], ma[1], ma[2], en[0], en[1], en[2]]):
            c = ws.cell(row=r, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME
    for col in (2, 3, 5, 6): ws.cell(row=r, column=col).number_format = PCT1
    for col in (4, 7): ws.cell(row=r, column=col).number_format = MULT0
    ws.cell(row=r, column=8, value=f"=Segments!$J$5*(1+E{r})*F{r}/1000").number_format = "0.000"
    ev = f"Segments!$J$6*(1+B{r})*C{r}/1000*D{r}+H{r}*G{r}"
    ws.cell(row=r, column=9, value=f"=({ev}+Valuation!$D$13)/Valuation!$D$15*1000").number_format = EUR2
    ws.cell(row=r, column=10, value=f"=I{r}/{A['price']}-1").number_format = PCT1
    r += 1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[3]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, €"; ws["A11"].font = F_B
ws["E11"] = "=B9*I5+C9*I6+D9*I7"; ws["E11"].number_format = EUR2; ws["E11"].font = F_B; ws["E11"].fill = FILL_KEY
ws["F11"] = f"=E11/{A['price']}-1"; ws["F11"].number_format = PCT1
note(ws, 13, ["Both businesses grow from my 2026 estimates. Net cash, minorities and shares are the same in every case."])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: MARINE MULTIPLE AGAINST THE ENERGY MULTIPLE (€)", [30, 14, 14, 14])
head(ws, 4, ["Marine x (rows) \\ Energy x (columns)", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_EN_X, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["x_EN"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (g, link) in enumerate(zip(SENS_MA_X, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=("=" + A["x_MA"]) if link else g)
    c.number_format = MULT0; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j,
                value=f"=(Valuation!$B$5*{col}$4+Valuation!$B$6*$A{rr}+Valuation!$D$13)/Valuation!$D$15*1000").number_format = EUR2
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["My 2027E results throughout; net cash at base. The middle row and column link to the base multiples."])

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
ws["A13"] = "Engine maker median (rows 6 to 8)"; ws["A13"].font = F_B
ws["C13"] = "=MEDIAN(C6:C8)"; ws["D13"] = "=MEDIAN(D6:D8)"
for c in ("C13", "D13"): ws[c].number_format = MULTF
note(ws, 15, ["Multiples only, to set the range of segment multiples. No view on the peers' shares is expressed. GE Vernova's trailing",
              "EV/EBIT of 58.9x reflects earnings still recovering and is not used for any multiple."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 140])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Wärtsilä, Interim Report January-September 2026, 27 October 2026: segment tables, Energy MW ordered, order books and 2026 deliveries, balance sheet, shares, risks, outlook, lead and delivery time quotes.",
    "Wärtsilä, Result presentation Q3 2026, 27 October 2026: Energy equipment orders by region (Americas €2,619m of €2,998m); Capital Markets Day on 3 November 2026.",
    "Wärtsilä, Inside information, 27 October 2026: new mid-term financial targets; new guidance practice from 2027; IFRS 18 restatement in March 2027.",
    "Wärtsilä, Half-year Financial Report January-June 2026, 21 July 2026: 1.2 GW of firm data centre-related orders across two projects; Energy equipment order book gross margin up more than 500 basis points since the start of 2025; Vaasa expansion to about 2.2 times 2025 output by Q1 2029.",
    "Wärtsilä, Interim Report January-March 2026, 28 April 2026: 429 MW data centre order (24 x 50SG); 35% expansion of production capacity by Q1 2028; Energy Q1 figures.",
    "Wärtsilä, Financial Statements Bulletin January-December 2025, 4 February 2026: 2024 and 2025 segment figures and quarters; 789 MW of data centre projects in 2025; Energy MW 2024 and 2025.",
    "Wärtsilä, stock exchange release of 5 October 2026: 2027 financial calendar (FY2026 bulletin 5 February 2027; Q1 2027 on 27 April 2027).",
    "Nasdaq Nordic price history, WRT1V (orderbook TX50138), retrieved 2 November 2026: daily closes, highs and lows; month-end closes.",
    "stockanalysis.com (S&P Global data), retrieved 2 November 2026: consensus EPS and average target; peer forward P/E and trailing EV/EBIT.",
    "The Physical Layer, 'Building your own power: GE Vernova's queue, not the grid's, sets the date', 22 September 2026: https://thephysicallayer.fyi/journal/building-your-own-power/",
    "Estimates for 2026 and 2027 are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("View on the band (the call)", "=Valuation!D19", None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    ("Base value per share, €", "=Valuation!D16", EUR2, "Sum of the parts on 2027E comparable operating result, plus net cash, over shares outstanding."),
    ("Reference price, €", "=" + A["price"], EUR2, "Nasdaq Helsinki close, 30 October 2026."),
    ("Base value against price", "=Valuation!D18", PCT1, ""),
    ("Probability-weighted value, €", "=Scenarios!E11", EUR2, "25 / 50 / 25 bear / base / bull."),
    ("Energy share of my equity value", "=Valuation!D30", PCT1, ""),
    ("Target, €", CALL["target"], EUR2, "Probability-weighted value, rounded."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
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
ws.row_dimensions[14].height = 44
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Segments", "Net sales and comparable operating result: 2024A, 2025A, 9M 2026A, Q4 2026E, 2026E, 2027E; EPS cross-check."),
    ("Energy", "Energy orders, sales, order book and MW by quarter; named data centre orders; the queue."),
    ("Valuation", "Sum of the parts, the bridge, base value, the band, what the price implies for Energy and Marine."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "Marine multiple against the Energy multiple."),
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
