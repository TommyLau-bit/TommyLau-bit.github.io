"""Entergy Corporation (NYSE: ETR) initiation model. Adjusted EPS on Entergy's own guide and outlooks to 2030, P/E
valuation on 2028E, scenarios, sensitivity, rate base and data centre arithmetic. Live formulas throughout. House style
follows the Vertiv, Eaton and Constellation models: navy header rows, blue font for hardcoded inputs, yellow fill on my
own assumptions, green font for cross-sheet links, black for formulas.
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
M2 = '#,##0.00'
PCT1 = '0.0%'
PCT0 = '0%'
MULTF = '0.0"x"'
MULT0 = '0"x"'
SUB = f"Tommy Lau | Entergy Corporation (NYSE: ETR) | {DATE} | Personal research, not investment advice."

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
ws = sheet("Cover", "ENTERGY CORPORATION (NYSE: ETR)  INITIATION MODEL", [42, 24, 100])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [66, 14, 10, 110])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. US$ unless stated. Year end 31 December.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
Q2R = "Q2 2026 earnings release, Form 8-K Ex. 99.1, 29 July 2026"
Q2Q = "Form 10-Q for the quarter to 30 June 2026, filed 31 July 2026"
INV = "Entergy 2026 Investor Day presentation, 9 June 2026; outlooks affirmed in the Q3 2026 release, 2 November 2026"
K25 = "2025 Form 10-K, filed 19 February 2026"
Q3R = "Q3 2026 earnings release, Form 8-K Ex. 99.1, 2 November 2026"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "US$", "NYSE close, 30 October 2026. Yahoo Finance history, read 2 November 2026; matches stockanalysis.com."),
    ("hiclose", "Highest close, 30 April 2026", HI_CLOSE, "US$", "Yahoo Finance. Intraday high US$118.45 on 1 May 2026."),
    ("pxdec", "Close, 31 December 2025", PX_DEC25, "US$", "Yahoo Finance (split-adjusted; 2-for-1 split 13 December 2024)."),
    ("shares_jun", "Common shares outstanding, 30 June 2026", 466.631498, "m", Q2Q + ", cover page: 466,631,498."),
    ("shares_sep", "Shares delivered under the 2025 forwards, 2 September 2026", 11.145984, "m", "Form 8-K, 2 September 2026: 11,145,984 shares for about US$913m."),
    ("fwd", "Shares under the May 2026 forwards, not yet settled", FWD_UNSETTLED, "m", "Form 8-K, 2 September 2026: 19,247,788 shares."),
    ("cash", "Cash and cash equivalents, 30 September 2026", CASH, "US$m", Q3R + ", Appendix D."),
    ("debt", "Total debt, 30 September 2026", DEBT, "US$m", Q3R + ", Appendix D (includes US$4,000m junior subordinated debentures)."),
    ("divq", "Quarterly dividend, declared 2 November 2026", DIV_Q, "US$", Q3R + ": 68 cents, up 6% from 64 cents."),
    ("eq_plan", "Equity to be issued, 2026 to 2030", EQUITY_PLAN, "US$m", Q2Q + ": about US$7bn through 2030."),
    ("eq_done", "Of which settled or contracted, 30 June 2026", EQUITY_DONE, "US$m", Q2Q + ": about US$4.1bn."),
    ("EARNINGS, GUIDANCE AND CONSENSUS", None, None, None, None),
    ("eps24", "2024 adjusted EPS", ADJ_EPS["2024A"], "US$", "Q4 2025 earnings release, 12 February 2026."),
    ("eps25", "2025 adjusted EPS", ADJ_EPS["2025A"], "US$", "Q4 2025 earnings release, 12 February 2026. As-reported EPS was the same."),
    ("ytd", "Adjusted EPS, nine months to 30 September 2026", YTD_26, "US$", Q3R + ": Q1 US$0.86, Q2 US$1.03, Q3 US$1.98 (Q3 2025 US$1.53)."),
]
for y in ["2026", "2027", "2028", "2029", "2030"]:
    lab = "guide" if y == "2026" else "outlook"
    if y == "2026":
        rows.append((f"g{y}lo", "2026 adjusted EPS guide, low (narrowed from US$4.25)", GUIDE[y][0], "US$", Q3R + "."))
        rows.append((f"g{y}hi", "2026 adjusted EPS guide, high", GUIDE[y][1], "US$", Q3R + "."))
        continue
    rows.append((f"g{y}lo", f"{y} adjusted EPS {lab}, low", GUIDE[y][0], "US$", INV + "."))
    rows.append((f"g{y}hi", f"{y} adjusted EPS {lab}, high", GUIDE[y][1], "US$", INV + "."))
rows += [
    ("cons26", "2026 consensus adjusted EPS", CONS_EPS26, "US$", "stockanalysis.com (S&P Global), 17 analysts, retrieved 2 November 2026. Cross-check only."),
    ("cons27", "2027 consensus adjusted EPS", CONS_EPS27, "US$", "stockanalysis.com, as above. Cross-check only."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com: 24 analysts, low US$91, high US$131. Cross-check only."),
    ("CAPITAL PLAN, RATE BASE AND DATA CENTRES", None, None, None, None),
]
for y in ["2026", "2027", "2028", "2029", "2030"]:
    rows.append((f"cap{y}", f"Planned construction and capital investment, {y}", CAPEX[y], "US$m", Q2Q + ". Excludes capital funded by customer advances."))
for y, v in RATE_BASE.items():
    rows.append((f"rb{y[:4]}", f"Projected rate base, {y}", v, "US$bn", INV + " (internal estimate, includes CWIP)."))
rows += [
    ("ff", "Franklin Farms Units 1 and 2 (first Meta agreement), cost", FF_COST, "US$m", K25 + ": about US$2,387m combined; in service 2028."),
    ("w5_ratio", "Waterford 5 cost as a share of the two Franklin Farms units", 0.5, "%", "MY ASSUMPTION from the 10-K wording: 'similar to the cost of each' Franklin Farms unit; in service 2029."),
    ("line1", "500 kV line for the first Meta agreement", META1_LINE, "US$m", K25 + "."),
    ("p2", "Seven CCCTs for the second Meta agreement, 5,278 MW", META2_PLANTS, "US$m", Q2Q + ": about US$12.9bn; in service 2030 and 2031; LPSC vote set for its December 2026 meeting."),
    ("line2", "West Fork Creek to St. Landry 500 kV line", META2_LINE, "US$m", Q2Q + ": about US$1.4bn."),
    ("mw1", "First Meta agreement, CCCT capacity", META1_MW, "MW", K25 + "."),
    ("mw2", "Second Meta agreement, CCCT capacity", META2_MW, "MW", Q2Q + "."),
    ("roe", "Entergy Louisiana authorised ROE, midpoint of 9.3% to 10.1%", ELA_ROE, "%", INV + ", appendix. Generation rider earns from the month after in service at the ROE midpoint."),
    ("eqr", "Entergy Louisiana equity ratio", ELA_EQ, "%", INV + ", appendix."),
    ("adv25", "Customer advances, all three lines, 31 December 2025", CUST_ADV_DEC25, "US$m", Q2Q + ", balance sheet: current 632.9 + non-current 35.0 + for construction 1,615.5."),
    ("adv26", "Customer advances, all three lines, 30 June 2026", CUST_ADV_JUN26, "US$m", Q2Q + ", balance sheet: current 1,470.1 + non-current 170.3 + for construction 2,086.4."),
    ("MY ESTIMATES", None, None, None, None),
    ("e26", "2026E adjusted EPS", E26, "US$", "MY ESTIMATE: midpoint of the narrowed guide; implies Q4 2026 of US$0.51, level with Q4 2025."),
    ("e27", "2027E adjusted EPS", E27, "US$", "MY ESTIMATE: outlook midpoint."),
    ("e28", "2028E adjusted EPS", E28, "US$", "MY ESTIMATE: outlook midpoint. Entergy reported 2025 in the top half of its range."),
    ("pe_base", "Base multiple, P/E on 2028E adjusted EPS", BASE_PE, "x", "MY ASSUMPTION. Today's 21.6x on the 2027 consensus, held a year forward; peers' forward median 19.1x (stockanalysis.com)."),
]
MINE = {"w5_ratio", "e26", "e27", "e28", "pe_base"}
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY)
        r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULTF if unit == "x" else (M2 if unit == "m" else (USD2 if unit == "US$" else M0)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  EARNINGS
ws = sheet("Earnings", "ADJUSTED EPS: REPORTED, ENTERGY'S GUIDE AND OUTLOOKS, AND MY ESTIMATES (US$ PER SHARE)", [52, 12, 12, 12, 12, 12, 12, 12])
head(ws, 4, ["US$ per share", "2024A", "2025A", "2026", "2027", "2028", "2029", "2030"])
labs = ["Entergy guide / outlook, low", "Entergy guide / outlook, high", "Midpoint", "Growth at the midpoint",
        "MY ESTIMATE (adjusted EPS)", "Consensus (stockanalysis.com)", "Mine against consensus", "P/E at the reference price"]
for i, lab in enumerate(labs):
    ws.cell(row=5 + i, column=1, value=lab).font = F_B if i in (2, 4) else Font()
put(ws, "B7", L("eps24"), USD2); put(ws, "C7", L("eps25"), USD2)
put(ws, "B9", L("eps24"), USD2); put(ws, "C9", L("eps25"), USD2)
for col, y in zip("DEFGH", ["2026", "2027", "2028", "2029", "2030"]):
    put(ws, f"{col}5", L(f"g{y}lo"), USD2); put(ws, f"{col}6", L(f"g{y}hi"), USD2)
    put(ws, f"{col}7", f"=({col}5+{col}6)/2", USD2, F_B)
    put(ws, f"{col}12", f"={A['price']}/{col}7", MULTF)
for col, prev in zip("CDEFGH", "BCDEFG"):
    put(ws, f"{col}8", f"={col}7/{prev}7-1", PCT1)
put(ws, "D9", L("e26"), USD2, F_B, FILL_KEY); put(ws, "E9", L("e27"), USD2, F_B, FILL_KEY); put(ws, "F9", L("e28"), USD2, F_B, FILL_KEY)
put(ws, "D10", L("cons26"), USD2); put(ws, "E10", L("cons27"), USD2)
put(ws, "D11", "=D9/D10-1", PCT1); put(ws, "E11", "=E9/E10-1", PCT1)
ws["A14"] = "Adjusted EPS growth a year, 2025 to 2030 midpoint"; put(ws, "B14", f"=(H7/{A['eps25']})^(1/5)-1", PCT1)
ws["A15"] = "Q4 2026 implied by the guide midpoint (2026 midpoint less nine months)"; put(ws, "B15", f"=D7-{A['ytd']}", USD2)
ws["A16"] = "Q4 2025, for comparison (2025 less Q1 US$0.82, Q2 US$1.05, Q3 US$1.53)"; put(ws, "B16", f"={A['eps25']}-0.82-1.05-1.53", USD2)
ws["A17"] = "P/E on the 2027 consensus"; put(ws, "B17", f"={A['price']}/E10", MULTF)
note(ws, 19, [
    "2026 is Entergy's guide, narrowed on 2 November 2026; 2027 to 2030 are its outlooks from the Investor Day of 9 June 2026, affirmed on 2 November 2026.",
    "My estimates sit at the midpoints: Entergy reported 2025 at US$3.91, in the top half of its range. Q3 2026 (US$1.98) included about US$0.24 of favourable weather.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: P/E ON 2028E ADJUSTED EPS, TWELVE MONTHS OUT", [66, 16, 70])
head(ws, 4, ["Item", "Value", "Working / note"])
vrows = [
    (5, "2028E adjusted EPS, US$", "=Earnings!F9", USD2, "My estimate: outlook midpoint."),
    (6, "Base multiple", L("pe_base"), MULTF, "Today's multiple of the 2027 consensus, held a year forward."),
    (7, "BASE VALUE PER SHARE, US$", "=B5*B6", USD2, ""),
    (8, "Reference price, US$", L("price"), USD2, "NYSE close, 30 October 2026."),
    (9, "Base value against price", "=B7/B8-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (10, "VIEW ON THE BAND", '=IF(B9>=0.15,"LONG",IF(B9<=-0.25,"SHORT","NO CALL"))', None, "The band; the call is Tommy Lau's."),
    (11, "Target, US$", CALL["target"] or "None (no call)", USD2, "None for a no call."),
    (12, "Target against price", "=IF(ISNUMBER(B11),B11/B8-1,\"n.a.\")", PCT1, ""),
    (14, "Shares outstanding, m (30 June 2026 plus 2 September settlement)", f"={A['shares_jun']}+{A['shares_sep']}", M2, ""),
    (15, "Market value, US$bn", "=B14*B8/1000", '#,##0.0', ""),
    (16, "Net debt, US$m, 30 September 2026", f"={A['debt']}-{A['cash']}", M0, ""),
    (17, "Enterprise value, US$bn", "=B15+B16/1000", '#,##0.0', "Before preferred, pensions and decommissioning."),
    (18, "P/E on 2026 narrowed guide midpoint", "=B8/Earnings!D7", MULTF, ""),
    (19, "P/E on 2027 consensus", "=B8/" + A["cons27"], MULTF, "stockanalysis.com."),
    (20, "P/E on 2027 outlook midpoint", "=B8/Earnings!E7", MULTF, ""),
    (21, "P/E on 2028E (mine): what the price pays", "=B8/Earnings!F9", MULTF, ""),
    (22, "Multiple of 2028E needed for a value 15% above the price", "=B8*1.15/B5", MULTF, ""),
    (23, "2028E EPS needed at the base multiple for a long, US$", "=B8*1.15/B6", USD2, ""),
    (24, "Price below which the base value is 15% or more above it, US$", "=B7/1.15", USD2, "Revisit level for a long."),
    (25, "Price above which the base value is 25% or more below it, US$", "=B7/0.75", USD2, "Revisit level for a short."),
    (26, "Price against the highest close", f"=B8/{A['hiclose']}-1", PCT1, ""),
    (27, "Price change in 2026 to date", f"=B8/{A['pxdec']}-1", PCT1, ""),
    (28, "Average analyst target against price", f"={A['constp']}/B8-1", PCT1, "Cross-check only."),
    (29, "Dividend yield at the price", f"={A['divq']}*4/B8", '0.00%', ""),
    (30, "Base value plus four dividends, against price", f"=(B7+4*{A['divq']})/B8-1", PCT1, "Total return view; the band uses the base value alone."),
]
for rr, lab, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    if rr in (7, 10):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    elif isinstance(f, str) and (f.startswith("=Assumptions") or f.startswith("=Earnings")): c.font = F_LINK
    elif rr == 11: c.font = F_INB; c.fill = FILL_ASSUME
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (VALUE = MULTIPLE x 2028E EPS)", [10, 16, 12, 14, 12])
head(ws, 4, ["Case", "2028E EPS", "Multiple", "Value, US$", "vs price"])
for i, s in enumerate(SCEN):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    if s[0] == "Base":
        for col, ref in [(2, "=Earnings!F9"), (3, "=" + A["pe_base"])]:
            c = ws.cell(row=rr, column=col, value=ref); c.font = F_LINK
    else:
        for col, v in [(2, s[1]), (3, s[2])]:
            c = ws.cell(row=rr, column=col, value=v); c.font = F_INB; c.fill = FILL_ASSUME
    ws.cell(row=rr, column=2).number_format = USD2; ws.cell(row=rr, column=3).number_format = MULTF
    ws.cell(row=rr, column=4, value=f"=B{rr}*C{rr}").number_format = USD2
    ws.cell(row=rr, column=5, value=f"=D{rr}/{A['price']}-1").number_format = PCT1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[3]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0
ws["A10"] = "must be 100%"; ws["A10"].font = F_NOTE
ws["A11"] = "Probability-weighted value, US$"; ws["A11"].font = F_B
ws["D11"] = "=B9*D5+C9*D6+D9*D7"; ws["D11"].number_format = USD2; ws["D11"].font = F_B; ws["D11"].fill = FILL_KEY
ws["E11"] = f"=D11/{A['price']}-1"; ws["E11"].number_format = PCT1
ws["A12"] = "Check: base case equals the Valuation tab"; ws["D12"] = "=D6-Valuation!B7"; ws["D12"].number_format = '0.000'
note(ws, 14, [
    "Bear: the Louisiana commission rejects or heavily conditions the second Meta agreement, or a large customer slips; 2028 EPS US$5.45, below the bottom of the outlook; 18x, near the large-utility median, as the growth premium goes.",
    "Base: the outlook midpoint for 2028, US$5.70; 21.5x, today's multiple of next year's consensus, held a year forward.",
    "Bull: the second agreement is approved, more of the 7 to 12 GW data centre pipeline signs and the outlook is raised; 2028 EPS US$5.95, above the top of the range; 24x.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: 2028E EPS AGAINST THE P/E (US$)", [30, 14, 14, 14])
head(ws, 4, ["2028E EPS \\ P/E", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_PE, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["pe_base"]) if link else m)
    c.number_format = MULTF; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (e, link) in enumerate(zip(SENS_EPS, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value="=Earnings!F9" if link else e)
    c.number_format = USD2; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=f"=$A{rr}*{col}$4").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
ws["A11"] = "Cells 25% or more below the price"; ws["A11"].font = F_B
ws["B11"] = f'=COUNTIF(B5:D7,"<="&{A["price"]}*0.75)'; ws["C11"] = "of 9"
note(ws, 13, ["The middle row links to the model's 2028E EPS and the middle column to the base multiple."])

# =====================================================================  RATE BASE AND DATA CENTRES
ws = sheet("RateBase", "RATE BASE, CAPITAL PLAN AND THE META PLANTS: THE CLAIM'S ARITHMETIC", [74, 16, 70])
head(ws, 4, ["Item", "Value", "Note"])
crows = [
    (5, "Capital plan 2026 to 2030, US$m", "=" + "+".join(A[f"cap{y}"] for y in ["2026", "2027", "2028", "2029", "2030"]), M0, "10-Q, Q2 2026. Entergy rounds to US$67bn."),
    (6, "Rate base growth a year, 2025E to 2030E", f"=({A['rb2030']}/{A['rb2025']})^(1/5)-1", PCT1, "Entergy's projection."),
    (7, "Adjusted EPS growth a year, 2025 to 2030 midpoint", "=Earnings!B14", PCT1, "Below rate base growth: new shares, parent interest and lag."),
    (8, "First Meta agreement: plants and line, US$m", f"={A['ff']}*(1+{A['w5_ratio']})+{A['line1']}", M0, "Waterford 5 at half of the two Franklin Farms units (my reading of the 10-K)."),
    (9, "Second Meta agreement: plants and line, US$m", f"={A['p2']}+{A['line2']}", M0, "Pending; LPSC vote set for December 2026."),
    (10, "Both Meta agreements against the five-year plan", "=(B8+B9)/B5", PCT1, "Gross project cost; a rough guide, not a bound: some spend falls after 2030 and customers fund part directly, while the second application also includes batteries and other lines not costed in the 10-Q."),
    (11, "First agreement: cost per kW of CCCT, US$", f"={A['ff']}*(1+{A['w5_ratio']})*1000/{A['mw1']}", M0, "Plants only."),
    (12, "Second agreement: cost per kW of CCCT, US$", f"={A['p2']}*1000/{A['mw2']}", M0, "Plants only."),
    (13, "Second agreement: net income a year at the allowed return, US$m", f"=B9*{A['eqr']}*{A['roe']}", M0, "MY ARITHMETIC, upper bound for these plants and the main line once all in rate base (2031 on): cost x equity ratio x ROE midpoint."),
    (14, "Per share, on shares outstanding plus unsettled forwards, US$", f"=B13/(Valuation!B14+{A['fwd']})", USD2, "Against the 2030 outlook midpoint of US$7.20."),
    (15, "Customer advances, increase in H1 2026, US$m", f"={A['adv26']}-{A['adv25']}", M0, "Cash paid ahead by large customers; the return on CWIP it funds added US$0.21 a share to the year-on-year rise in EPS over the nine months to September 2026 (Q3 2026 release, Appendix B)."),
    (16, "Equity still to raise, 2026 to 2030, US$m", f"={A['eq_plan']}-{A['eq_done']}", M0, "From 30 June 2026."),
]
for rr, lab, f, fmt, nt in crows:
    ws.cell(row=rr, column=1, value=lab)
    c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt; c.alignment = RIGHT
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
note(ws, 18, [
    "Hyperion timeline: first application October 2024; LPSC order accepting a settlement August 2025; Franklin Farms 1 and 2 in service 2028, Waterford 5 in 2029.",
    "Second agreement (Evest LLC, a Meta subsidiary): signed and filed March 2026; LPSC set consideration for its December 2026 meeting; settlement with LPSC staff reached (Q3 2026 release); terms not yet filed with the SEC.",
    "Contract protections (10-Q): minimum monthly bills, contributions in aid of construction, early termination obligations based on unrecovered costs, Meta Platforms guaranty.",
    "Turbine slots (10-Q): exclusivity agreement for power island equipment, one manufacturing slot a quarter; minimum raised to 27 sets in Q2 2026, 10 fulfilled at 30 June 2026.",
])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, UPDATED 2 NOVEMBER 2026)", [26, 14, 13, 14, 70])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "EV/EBITDA", "What they run"])
for i, (co, tk, pe, eve, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, v in enumerate([pe, eve]):
        c = ws.cell(row=rr, column=3 + j, value=v); c.number_format = MULTF; c.font = F_IN
    ws.cell(row=rr, column=5, value=what).alignment = WRAP
last = 4 + len(PEERS)
ws[f"A{last + 2}"] = "Peer median (excluding Entergy)"; ws[f"A{last + 2}"].font = F_B
ws[f"C{last + 2}"] = f"=MEDIAN(C6:C{last})"; ws[f"C{last + 2}"].number_format = MULTF
ws[f"A{last + 3}"] = "Entergy premium over the peer median, turns"; ws[f"A{last + 3}"].font = F_B
ws[f"C{last + 3}"] = f"=C5-C{last + 2}"; ws[f"C{last + 3}"].number_format = MULTF
note(ws, last + 5, ["Multiples only, to set the range. No view on the peers' shares is expressed."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 150])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Entergy second quarter 2026 earnings release, Form 8-K Ex. 99.1, 29 July 2026: Q2 and H1 adjusted EPS, guide affirmed, sales by class, return on CWIP, cash, debt, credit metrics.",
    "Entergy Form 10-Q, quarter to 30 June 2026, filed 31 July 2026: capital plan by year, second Meta agreement and LPSC schedule, contract protections, subpoena dispute, equity plan, power island agreement, customer advances, shares outstanding.",
    "Entergy 2025 Form 10-K, filed 19 February 2026: first Meta application and order, costs, in-service dates, termination payments, intervenors' January 2026 motion, power island agreement terms.",
    "Entergy third quarter 2026 earnings release, Form 8-K Ex. 99.1, 2 November 2026: Q3 adjusted EPS, narrowed 2026 guide, outlooks affirmed, Evest settlement with LPSC staff, dividend increase, cash, debt, FFO to adjusted debt.",
    "Entergy fourth quarter 2025 release, 12 February 2026, and first quarter 2026 release, 29 April 2026: annual and quarterly adjusted EPS, 2026 guide.",
    "Entergy 2026 Investor Day presentation, 9 June 2026: guide and outlooks to 2030, US$67bn capital plan, projected rate base, equity plan, sales outlook, hyperscale contract features, 10 CCCTs secured, pipeline, regulatory appendix.",
    "Entergy Form 8-K filings of 23 June and 2 September 2026: forward sale settlements.",
    "Yahoo Finance ETR history pages, read 2 November 2026; stockanalysis.com (S&P Global data) for consensus, targets and peer multiples, retrieved 2 November 2026.",
    "The Physical Layer, 'Building your own power: GE Vernova's queue, not the grid's, sets the date', https://thephysicallayer.fyi/journal/building-your-own-power/",
    "Estimates for 2026 to 2028 are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Call (Tommy Lau)", CALL["direction"], None, "On the band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between (Valuation!B10)."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Base value per share, US$", "=Valuation!B7", USD2, "Base multiple x 2028E adjusted EPS."),
    ("Reference price, US$", "=" + A["price"], USD2, "NYSE close, 30 October 2026."),
    ("Base value against price", "=Valuation!B9", PCT1, ""),
    ("Probability-weighted value, US$", "=Scenarios!D11", USD2, "25 / 50 / 25 bear / base / bull."),
    ("2028E adjusted EPS, US$", "=Earnings!F9", USD2, "My estimate: outlook midpoint."),
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
ws.row_dimensions[13].height = 44; ws.row_dimensions[14].height = 58
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Earnings", "Adjusted EPS, 2024A to 2030, against Entergy's guide, outlooks and the consensus."),
    ("Valuation", "Base value, the band, multiples at the price, revisit levels."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "2028E EPS against the multiple."),
    ("RateBase", "Rate base, capital plan and the arithmetic of the Meta plants."),
    ("Peers", "Forward P/E and EV/EBITDA used to set the multiple."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t)
    ws.cell(row=18 + i, column=2, value=d)
ws["A27"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A27"].font = F_NOTE
ws["A28"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."
ws["A28"].font = F_NOTE

for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
