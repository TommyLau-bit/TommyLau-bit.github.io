"""GE Vernova (NYSE: GEV) initiation model. Live formulas throughout.

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
USD0 = '"US$"#,##0'
BN2 = '#,##0.00'
BN3 = '#,##0.000'
PCT1 = '0.0%'
PCT0 = '0%'
MULT = '0.0"x"'
MULT0 = '0"x"'
SUB = "Tommy Lau | GE Vernova (NYSE: GEV) | 9 October 2026 | Personal research, not investment advice."

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
ws = sheet("Cover", "GE VERNOVA INC. (NYSE: GEV)  INITIATION MODEL", [36, 24, 80])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [46, 14, 10, 96])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. US$ billion unless stated.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"g27", "g28", "m27", "m28", "mult"}
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "US$", "NYSE close, 8 October 2026. Nasdaq.com historical data, retrieved 9 October 2026."),
    ("hiclose", "Highest close, 30 June 2026", HI_CLOSE, "US$", "Nasdaq.com historical data. Intraday high US$1,195.94 on 6 July 2026."),
    ("shout", "Shares outstanding, 30 June 2026", SHARES_OUT, "m", "Form 10-Q for the quarter to 30 June 2026, cover page: 266,333,581."),
    ("dil", "Dilutive effect of common stock equivalents", DILUTIVE, "m", "Form 10-Q, Note 18, three months to 30 June 2026."),
    ("cash", "Cash, cash equivalents and restricted cash, 30 Jun 2026", CASH, "US$bn", "Form 10-Q, statement of financial position."),
    ("debt", "Total borrowings incl. current maturities and finance leases", DEBT, "US$bn", "Form 10-Q, Note 14 (US$2,849m)."),
    ("cltot", "Contract liabilities and current deferred income, all segments", CL_TOTAL, "US$bn", "Form 10-Q, Note 9."),
    ("cons26", "2026 consensus EPS", CONS_EPS_26, "US$", "stockanalysis.com (S&P Global, 37 analysts, updated 1 Oct 2026). Basis not stated by the source. Cross-check only."),
    ("cons27", "2027 consensus EPS", CONS_EPS_27, "US$", "stockanalysis.com, same source. MarketBeat shows US$23.90. Cross-check only."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com, 37 analysts, range US$940 to 1,450. Cross-check only."),
    ("REPORTED", None, None, None, None),
    ("r24", "2024 revenue", REV_H[0], "US$bn", "4Q25 results release (Form 8-K, Exhibit 99), 28 January 2026."),
    ("r25", "2025 revenue", REV_H[1], "US$bn", "4Q25 results release."),
    ("e24", "2024 adjusted EBITDA", EBITDA_H[0], "US$bn", "4Q25 results release, non-GAAP reconciliation."),
    ("e25", "2025 adjusted EBITDA", EBITDA_H[1], "US$bn", "4Q25 results release."),
    ("f24", "2024 free cash flow", FCF_H[0], "US$bn", "4Q25 results release."),
    ("f25", "2025 free cash flow", FCF_H[1], "US$bn", "4Q25 results release."),
    ("prev25", "2025 Power revenue", POWER_REV_25, "US$bn", "4Q25 results release, Power segment table."),
    ("2026 GUIDE (2Q26 release, 22 July 2026) AND OUTLOOK BY 2028 (4Q25 release, 28 January 2026)", None, None, None, None),
    ("gr_lo", "2026 revenue guide, low", G26["rev_lo"], "US$bn", "Raised from US$44.5 to 45.5bn (April) and US$44 to 45bn (January)."),
    ("gr_hi", "2026 revenue guide, high", G26["rev_hi"], "US$bn", "2Q26 results release."),
    ("gm_lo", "2026 adjusted EBITDA margin guide, low", G26["m_lo"], "%", "2Q26 results release; unchanged since April."),
    ("gm_hi", "2026 adjusted EBITDA margin guide, high", G26["m_hi"], "%", "2Q26 results release."),
    ("gf_lo", "2026 free cash flow guide, low", G26["fcf_lo"], "US$bn", "Raised from US$6.5 to 7.5bn on down payments and higher EBITDA."),
    ("gf_hi", "2026 free cash flow guide, high", G26["fcf_hi"], "US$bn", "2Q26 results release."),
    ("o28r", "Revenue outlook by 2028", OUT28["rev"], "US$bn", "4Q25 results release: US$56bn, up from US$52bn, including Prolec GE. Not updated since."),
    ("o28m", "Adjusted EBITDA margin outlook by 2028", OUT28["m"], "%", "4Q25 results release: 20%. Power and Electrification segment margins 22% each."),
    ("o28f", "Cumulative free cash flow, 2025 to 2028, outlook", OUT28["fcf_cum"], "US$bn", "4Q25 results release: at least US$24bn."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("g27", "2027 revenue growth", G27, "%", "MY ASSUMPTION. About the pace that carries the 2026 guide midpoint to the US$56bn 2028 outlook, plus a little for the 2026 raise."),
    ("g28", "2028 revenue growth", G28, "%", "MY ASSUMPTION. Gas volume rises with the 24 GW output step; price and services do the rest."),
    ("m27", "2027 adjusted EBITDA margin", M27, "%", "MY ASSUMPTION. Halfway between the 2026 guide midpoint and the 2028 outlook."),
    ("m28", "2028 adjusted EBITDA margin", M28, "%", "MY ASSUMPTION. GE Vernova's own 2028 outlook, 20%."),
    ("mult", "EV / 2028E adjusted EBITDA, base", BASE_MULT, "x", "MY ASSUMPTION. Between Siemens Energy (22.1x) and Eaton (27.9x) trailing EV/EBITDA; see Peers."),
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
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else ("#,##0.000" if unit in ("m",) else (USD2 if unit == "US$" else BN3)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1

# =====================================================================  FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (US$ billion unless stated)", [44, 13, 13, 13, 13, 13, 13])
head(ws, 4, ["", "2024A", "2025A", "2026 guide", "2027E*", "2028E*", "2028 outlook"])
L = lambda k: "=" + A[k]
lines = [
    ("Revenue", [L("r24"), L("r25"), f"=AVERAGE({A['gr_lo']},{A['gr_hi']})", "=D5*(1+" + A["g27"] + ")", "=E5*(1+" + A["g28"] + ")", L("o28r")], BN2),   # 5
    ("Revenue growth", [None, "=C5/B5-1", "=D5/C5-1", "=E5/D5-1", "=F5/E5-1", None], PCT1),                                                             # 6
    ("Adjusted EBITDA margin", ["=B8/B5", "=C8/C5", f"=AVERAGE({A['gm_lo']},{A['gm_hi']})", L("m27"), L("m28"), L("o28m")], PCT1),                       # 7
    ("Adjusted EBITDA", [L("e24"), L("e25"), "=D5*D7", "=E5*E7", "=F5*F7", "=G5*G7"], BN2),                                                              # 8
    ("Adjusted EBITDA growth", [None, "=C8/B8-1", "=D8/C8-1", "=E8/D8-1", "=F8/E8-1", None], PCT1),                                                     # 9
    ("Free cash flow", [L("f24"), L("f25"), f"=AVERAGE({A['gf_lo']},{A['gf_hi']})", None, None, None], BN2),                                             # 10
    ("Free cash flow / adjusted EBITDA", ["=B10/B8", "=C10/C8", "=D10/D8", None, None, None], "0.00\"x\""),                                               # 11
    ("EV / adjusted EBITDA at reference price", [None, None, "=Valuation!$B$16/D8", "=Valuation!$B$16/E8", "=Valuation!$B$16/F8", "=Valuation!$B$16/G8"], MULT),  # 12
]
r = 5
for label, vals, fmt in lines:
    ws.cell(row=r, column=1, value=label).font = F_B if label in ("Revenue", "Adjusted EBITDA") else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=r, column=2 + j, value=v if v is not None else "")
        c.number_format = fmt; c.alignment = RIGHT
        if isinstance(v, str) and v.startswith("=Assumptions"):
            c.font = F_LINK
    r += 1
note(ws, 15, [
    "*2027E and 2028E are my own estimates, not GE Vernova's. 2026 is the midpoint of GE Vernova's own guide of 22 July 2026.",
    "2028 outlook: revenue of US$56bn and a 20% adjusted EBITDA margin, set on 28 January 2026 with the Prolec GE acquisition; adjusted EBITDA is derived.",
    "Free cash flow in 2026 is about twice adjusted EBITDA because customers' down payments on orders and slot reservations arrive years before delivery.",
    "No free cash flow forecast for 2027 or 2028: down payments unwind as turbines ship, and GE Vernova gives only a cumulative figure.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: EV / 2028E ADJUSTED EBITDA, TWELVE MONTHS OUT", [56, 16, 72])
head(ws, 4, ["Line", "Value", "Working / note"])
val = [
    ("eb28", "2028E adjusted EBITDA, US$bn", "=Financials!F8", BN2, "Financials tab. By October 2027 the market will be pricing 2028."),               # 5
    ("mult", "Multiple, x", "=" + A["mult"], MULT0, "Assumptions tab."),                                                                                # 6
    ("ev28", "Enterprise value at the base multiple, US$bn", "=B5*B6", BN2, "EBITDA x multiple."),                                                       # 7
    ("nc", "Add net cash, 30 June 2026, US$bn", "=" + A["cash"] + "-" + A["debt"], BN3, "Cash less borrowings. Much of the cash is customer down payments."),  # 8
    ("sh", "Diluted shares, m", "=" + A["shout"] + "+" + A["dil"], "#,##0.0", "Outstanding plus dilutive equivalents. No buybacks assumed."),           # 9
    ("base", "BASE VALUE PER SHARE, US$", "=(B7+B8)/B9*1000", USD2, "Equity value / diluted shares."),                                                 # 10
    ("px", "Reference price, US$", "=" + A["price"], USD2, "NYSE close, 8 October 2026."),                                                               # 11
    ("up", "Base value against price", "=B10/B11-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),           # 12
    ("rule", "VIEW ON THE BAND", '=IF(B12>=0.15,"LONG",IF(B12<=-0.25,"SHORT","NO CALL"))', None, "Tommy Lau's call, 9 October 2026: NO CALL, Medium conviction."),                 # 13
    (None, "", None, None, ""),                                                                                                                          # 14
    ("mcap", "Market value on diluted shares, US$bn", "=B9*B11/1000", BN2, "Price x diluted shares."),                                                   # 15
    ("ev", "Enterprise value, US$bn", "=B15-B8", BN2, "Market value less net cash."),                                                                    # 16
    ("need", "2028 adjusted EBITDA the price needs at the base multiple, US$bn", "=B16/B6", BN2, "Compare with the 2028 outlook (Financials G8) and my 2028E (B5)."),  # 17
    ("needo", "That figure against the 2028 outlook", "=B17/Financials!G8", PCT1, ""),                                                                   # 18
    ("evo", "EV / 2028 outlook EBITDA", "=B16/Financials!G8", MULT, ""),                                                                                 # 19
    ("pec26", "P/E on 2026 consensus EPS", "=B11/" + A["cons26"], MULT, "Cross-check only; consensus basis not stated by the source."),                  # 20
    ("pec27", "P/E on 2027 consensus EPS", "=B11/" + A["cons27"], MULT, "Cross-check only."),                                                            # 21
    ("fcfy", "2026 free cash flow yield at guide midpoint", "=Financials!D10/B15", PCT1, "Flattered by down payments; see Financials note."),            # 22
    ("revl", "Price at which the base value is 15% above it, US$", "=B10/1.15", USD0, "Revisit level for a LONG."),                                      # 23
    ("revs", "Price at which the base value is 25% below it, US$", "=B10/0.75", USD0, "Revisit level for a SHORT."),                                     # 24
    ("offhi", "Price against highest close", "=B11/" + A["hiclose"] + "-1", PCT1, "Highest close US$1,174.86, 30 June 2026."),                           # 25
    ("cltp", "Contract liabilities, all segments, against cash", "=" + A["cltot"] + "/" + A["cash"], "0.00\"x\"", "Customer money held exceeds cash on hand."),  # 26
]
V = {}
r = 5
for key, label, f, fmt, nt in val:
    ws.cell(row=r, column=1, value=label)
    if f is not None:
        c = ws.cell(row=r, column=2, value=f)
        if fmt: c.number_format = fmt
        if key in ("base", "rule"):
            ws.cell(row=r, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
        if isinstance(f, str) and f.startswith("=Assumptions"):
            c.font = F_LINK
    ws.cell(row=r, column=3, value=nt).alignment = WRAP
    if key: V[key] = f"Valuation!$B${r}"
    r += 1

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT", [12, 12, 12, 12, 13, 13, 13, 11, 14, 12])
head(ws, 4, ["Case", "2027 growth", "2028 growth", "2028 margin", "2027 revenue", "2028 revenue", "2028 EBITDA", "Multiple", "Value, US$", "vs price"])
r = 5
for name, g1, g2, m, mult, p in SCEN:
    ws.cell(row=r, column=1, value=name).font = F_B
    if name == "Base":
        for j, k in enumerate(["g27", "g28", "m28"]):
            c = ws.cell(row=r, column=2 + j, value="=" + A[k]); c.font = F_LINK; c.number_format = PCT1
        c = ws.cell(row=r, column=8, value="=" + A["mult"]); c.font = F_LINK
    else:
        for j, v in enumerate([g1, g2, m]):
            c = ws.cell(row=r, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT1
        c = ws.cell(row=r, column=8, value=mult); c.font = F_INB; c.fill = FILL_ASSUME
    ws.cell(row=r, column=8).number_format = MULT0
    ws.cell(row=r, column=5, value=f"=Financials!$D$5*(1+B{r})").number_format = BN2
    ws.cell(row=r, column=6, value=f"=E{r}*(1+C{r})").number_format = BN2
    ws.cell(row=r, column=7, value=f"=F{r}*D{r}").number_format = BN2
    ws.cell(row=r, column=9, value=f"=(G{r}*H{r}+Valuation!$B$8)/Valuation!$B$9*1000").number_format = USD2
    ws.cell(row=r, column=10, value=f"=I{r}/{A['price']}-1").number_format = PCT0
    r += 1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[5]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, US$"; ws["A11"].font = F_B
ws["E11"] = "=B9*I5+C9*I6+D9*I7"; ws["E11"].number_format = USD2; ws["E11"].font = F_B; ws["E11"].fill = FILL_KEY
ws["F11"] = f"=E11/{A['price']}-1"; ws["F11"].number_format = PCT1
note(ws, 13, [
    "All cases start from the 2026 guide midpoint (US$46.0bn), keep my 16.5% adjusted EBITDA margin for 2027 (Assumptions, linked through Financials E7),",
    "and add net cash of 30 June 2026 over the same diluted shares. Only 2027 and 2028 growth and the 2028 margin differ by case.",
    "Bear: gas orders peak, conversions slow and the market pays 16x, about Mitsubishi Heavy's trailing EV/EBITDA. Bull: price in backlog and services lift",
    "margin above the 2028 outlook and the market pays 30x for a queue sold into the 2030s.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: 2028E ADJUSTED EBITDA AGAINST EV MULTIPLE (US$)", [26, 14, 14, 14])
head(ws, 4, ["2028 EBITDA (US$bn) \\ multiple", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_MULT, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["mult"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (e, link) in enumerate(zip(SENS_EBITDA, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value="=Financials!F8" if link else e)
    c.number_format = BN2; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=f"=($A{rr}*{col}$4+Valuation!$B$8)/Valuation!$B$9*1000").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
note(ws, 12, ["Middle row links to the model's 2028E EBITDA and the middle column to the base multiple, so the grid moves with the assumptions."])

# =====================================================================  QUEUE
ws = sheet("Queue", "GAS TURBINE QUEUE AND DEPOSITS", [52] + [11] * 6)
head(ws, 4, ["Gigawatts unless stated"] + Q)
cols = [get_column_letter(2 + j) for j in range(6)]


def qrow(r, label, vals, fmt, inp=True, bold=False):
    ws.cell(row=r, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        c = ws.cell(row=r, column=2 + j, value=v if v is not None else "n.d.")
        c.number_format = fmt; c.alignment = RIGHT
        if inp and not (isinstance(v, str) and v.startswith("=")): c.font = F_IN


qrow(5, "Firm orders in gas equipment backlog", GW_BACKLOG, "0")
qrow(6, "Slot reservation agreements", GW_SRA, "0")
qrow(7, "Gigawatts under contract, as stated", GW_TOTAL, "0", bold=True)
qrow(8, "Signed in the quarter (orders and reservations)", GW_SIGNED, "0")
qrow(9, "Shipped in the quarter", GW_SHIPPED, "0")
qrow(10, "Years of output at 20 GW a year (derived)", [f"={c}7/20" for c in cols], "0.0", inp=False)
qrow(11, "Reservations share of the total (derived)", [f"={c}6/{c}7" for c in cols], PCT0, inp=False)
qrow(12, "Power revenue, US$bn", Q_POWER_REV, BN2)
qrow(13, "Power segment EBITDA margin (as first reported)", [m / 100 for m in Q_POWER_M], PCT1)
qrow(14, "Power orders, US$bn", Q_POWER_ORD, BN2)
qrow(15, "Revenue, GE Vernova, US$bn", Q_REV, BN2)
qrow(16, "Adjusted EBITDA, GE Vernova, US$bn", Q_EBITDA, BN3)
qrow(17, "Adjusted EBITDA margin (derived)", [f"={c}16/{c}15" for c in cols], PCT1, inp=False)
ws["A19"] = "Signed in the first half of 2026"; ws["B19"] = "=F8+G8"
ws["A20"] = "Shipped in the first half of 2026"; ws["B20"] = "=F9+G9"
ws["A21"] = "Growth in the queue, first half of 2026"; ws["B21"] = "=G7/E7-1"; ws["B21"].number_format = PCT1
ws["A23"] = "The claim's floor: gigawatts under contract needed for four years of planned output"; ws["A23"].font = Font(bold=True, color=NAVY)
head(ws, 24, ["Year", "Planned output, GW", "Floor, GW"])
for i, (y, v) in enumerate(OUTPUT_PLAN.items()):
    rr = 25 + i
    ws.cell(row=rr, column=1, value=f"From {y}")
    c = ws.cell(row=rr, column=2, value=v); c.font = F_IN
    ws.cell(row=rr, column=3, value=f"=B{rr}*4")
ws["A29"] = "Power contract liabilities and current deferred income, US$bn"; ws["A29"].font = Font(bold=True, color=NAVY)
head(ws, 30, ["Date"] + CL_LABELS)
ws["A31"] = "Power"
for j, v in enumerate(CL_POWER):
    c = ws.cell(row=31, column=2 + j, value=v); c.font = F_IN; c.number_format = BN3
ws["A32"] = "Rise in the first half of 2026"; ws["B32"] = "=F31/D31-1"; ws["B32"].number_format = PCT1
ws["A33"] = "Multiple of December 2024"; ws["B33"] = "=F31/B31"; ws["B33"].number_format = '0.00"x"'
ws["A34"] = "Against 2025 Power revenue"; ws["B34"] = "=F31/" + A["prev25"]; ws["B34"].number_format = '0.00"x"'
note(ws, 36, [
    "Sources: GE Vernova quarterly results releases, 23 April 2025 to 22 July 2026; Forms 10-Q to 30 September 2025, 31 March 2026 and 30 June 2026, Note 9;",
    "Form 10-K for 2025. December 2024 and September 2025 contract liabilities are on the segment basis before the 1 January 2026 realignment; the",
    "December 2025 Power figure (US$16,527m) is the same on both bases. 2026 Power margins are on the realigned basis. Q2 25 total: 29 + 25 = 54, stated as 55.",
])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, RETRIEVED 9 OCTOBER 2026)", [22, 14, 14, 16, 80])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "EV/EBITDA (trailing)", "What they make"])
for i, (co, tk, pe, eve, what) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if co == "GE Vernova" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, v in enumerate([pe, eve]):
        c = ws.cell(row=rr, column=3 + j, value=v); c.number_format = MULT; c.font = F_IN
    ws.cell(row=rr, column=5, value=what).alignment = WRAP
ws["A12"] = "Peer median (excluding GE Vernova)"; ws["A12"].font = F_B
ws["C12"] = "=MEDIAN(C6:C10)"; ws["D12"] = "=MEDIAN(D6:D10)"
for c in ("C12", "D12"): ws[c].number_format = MULT
ws["A13"] = "GE Vernova on 2028 outlook EBITDA"; ws["D13"] = "=Valuation!B19"; ws["D13"].number_format = MULT
note(ws, 15, ["Multiples only, to set the range of EV multiples. No view on the peers' shares is expressed."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 130])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "GE Vernova quarterly results releases on Form 8-K, Exhibit 99: 23 April 2025, 23 July 2025, 22 October 2025, 28 January 2026, 22 April 2026, 22 July 2026. Revenue, adjusted EBITDA, free cash flow, Power segment, gigawatts signed, converted, shipped and under contract, 2026 guide and the outlook by 2028.",
    "GE Vernova Form 10-Q for the quarter to 30 June 2026, filed 22 July 2026: shares outstanding, cash, borrowings (Note 14), contract liabilities by segment (Note 9), RPO, cash flow explanation, Prolec GE (Note 8).",
    "GE Vernova Forms 10-Q for the quarters to 31 March 2026 and 30 September 2025, and Form 10-K for 2025 (filed 29 January 2026): Power contract liabilities at earlier dates.",
    "GE Vernova second quarter 2026 earnings call, 22 July 2026, transcript on gevernova.com: output plan (20, 24 and 30 GW), funding by down payments, sold-out comments, pricing, commissioning times, data centre share, third quarter segment outlook.",
    "GE Vernova Form 8-K of 25 August 2026: Kenneth Parks to retire; Claire McDonough becomes CFO on 1 January 2027.",
    "GE Vernova investor events page: third quarter 2026 earnings webcast on 28 October 2026, 7:30 am EDT.",
    "Nasdaq.com historical data, retrieved 9 October 2026: daily and month-end closes, highs and lows.",
    "stockanalysis.com (S&P Global consensus, updated 1 October 2026) and MarketBeat, retrieved 9 October 2026: consensus EPS, average target, peer multiples.",
    "The Physical Layer, 'GE Vernova's customers are paying years in advance for a place in its queue', 9 October 2026: https://thephysicallayer.fyi/journal/ge-vernova-sells-the-wait/",
    "Estimates for 2027 and 2028 are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Call (Tommy Lau, 9 October 2026)", "=" + V["rule"], None, "Applied on the band to the base value: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    ("Base value per share, US$", "=" + V["base"], USD2, f"{BASE_MULT}x 2028E adjusted EBITDA plus net cash, over diluted shares."),
    ("Reference price, US$", "=" + A["price"], USD2, "NYSE close, 8 October 2026."),
    ("Base value against price", "=" + V["up"], PCT1, ""),
    ("Probability-weighted value, US$", "=Scenarios!E11", USD2, "25 / 50 / 25 bear / base / bull."),
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
ws.row_dimensions[12].height = 32; ws.row_dimensions[13].height = 44
ws["A16"] = "Tabs"; ws["A16"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Financials", "2024A to 2028E: revenue, adjusted EBITDA, free cash flow, EV multiples; 2028 outlook alongside."),
    ("Valuation", "Base value, the band, what the price needs, cross-checks."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "2028E adjusted EBITDA against EV multiple."),
    ("Queue", "Gigawatts under contract, signed and shipped; years of output; the claim's floor; Power deposits; quarterly results."),
    ("Peers", "Forward P/E and EV/EBITDA used to set the multiple range."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=17 + i, column=1, value=t)
    ws.cell(row=17 + i, column=2, value=d)
ws["A26"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A26"].font = F_NOTE
ws["A27"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."
ws["A27"].font = F_NOTE

for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
