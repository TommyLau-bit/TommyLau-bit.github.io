"""SpaceX (Nasdaq: SPCX) initiation model: sum of the parts and what the price leaves for orbit. Live formulas.

House style follows the Vertiv and Hitachi models: navy header rows, navy bold titles, blue font for hardcoded inputs,
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
M0 = '#,##0'
M1 = '#,##0.0'
PCT1 = '0.0%'
MULTF = '0.0"x"'
SUB = "Tommy Lau | SpaceX (Nasdaq: SPCX) | 2 November 2026 | Personal research, not investment advice."

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


def put(ws, ref, v, fmt=None, font=None):
    ws[ref] = v
    if fmt: ws[ref].number_format = fmt
    if font: ws[ref].font = font
    elif isinstance(v, str) and v.startswith("=Assumptions"): ws[ref].font = F_LINK
    if not (isinstance(v, str) and not v.startswith("=")): ws[ref].alignment = RIGHT


# =====================================================================  COVER (filled last)
ws = sheet("Cover", "SPACEX (SPACE EXPLORATION TECHNOLOGIES CORP., NASDAQ: SPCX)  INITIATION MODEL", [44, 24, 90])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [58, 14, 10, 100])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "another tab. Black = formula. US$ million unless stated.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = set()
ER = "Results release, 8-K Exhibit 99.1, 20 October 2026"
Q3 = "Form 10-Q, quarter to 30 September 2026, filed 22 October 2026"
rows = [
    ("MARKET AND BALANCE SHEET", None, None, None, None),
    ("price", "Reference share price", PRICE, "US$", "Nasdaq close, 30 October 2026. Yahoo Finance SPCX history page, read 2 November 2026."),
    ("ipo", "IPO price", IPO_PRICE, "US$", "Final prospectus (424B4), 12 June 2026."),
    ("hiclose", "Highest close, 16 June 2026", HI_CLOSE, "US$", "Yahoo Finance; intraday high US$225.64 the same day."),
    ("sha", "Class A shares outstanding, 15 October 2026", SHARES_A, "m", Q3 + ", cover: 8,246,541,218."),
    ("shb", "Class B shares outstanding, 15 October 2026", SHARES_B, "m", Q3 + ", cover: 5,334,522,491."),
    ("cash", "Cash and cash equivalents, 30 September 2026", CASH, "US$m", ER + ", balance sheet."),
    ("secs", "Marketable securities, 30 September 2026", SECS, "US$m", ER + "."),
    ("debtc", "Debt and finance leases, current", DEBT_CUR, "US$m", ER + "."),
    ("debtl", "Debt and finance leases, non-current", DEBT_LT, "US$m", ER + "."),
    ("CONSENSUS (YAHOO FINANCE, READ 2 NOVEMBER 2026)", None, None, None, None),
    ("crev26", "Revenue consensus, 2026", CONS_REV_26, "US$m", "35 analysts."),
    ("crev27", "Revenue consensus, 2027", CONS_REV_27, "US$m", "37 analysts; range US$71.75bn to US$290.06bn."),
    ("ceps27", "EPS consensus, 2027", CONS_EPS_27, "US$", "33 analysts; range US$0.34 to US$13.49."),
    ("ctp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com, 39 analysts, 2 November 2026; low US$70, high US$800. Cross-check only."),
    ("MY ASSUMPTIONS: FOURTH QUARTER 2026", None, None, None, None),
]
for k in SEGS:
    rows.append((f"q4r_{k}", f"{SEG_NAMES[k]} revenue, Q4 2026E", Q4_26[k][0], "US$m", "MY ASSUMPTION. Consensus total Q4 revenue US$22.92bn (Yahoo)."))
    rows.append((f"q4e_{k}", f"{SEG_NAMES[k]} Segment Adjusted EBITDA, Q4 2026E", Q4_26[k][1], "US$m", "MY ASSUMPTION."))
rows.append(("MY ASSUMPTIONS: 2027", None, None, None, None))
for k in SEGS:
    rows.append((f"r27_{k}", f"{SEG_NAMES[k]} revenue, 2027E", R27[k], "US$m",
                 {"Space": "MY ASSUMPTION. Falcon pipeline plus early Starship customer work.",
                  "Connectivity": "MY ASSUMPTION. About 40% growth on 2026E; Q3 2026 grew 69% year on year.",
                  "SI": "MY ASSUMPTION. Q1 2027 guide for the whole company US$33bn to 37bn; consensus implies about US$148bn for SI."}[k]))
    rows.append((f"m27_{k}", f"{SEG_NAMES[k]} Segment Adjusted EBITDA margin, 2027E", M27[k], "%",
                 {"Space": "MY ASSUMPTION. Not used in the base value (Space is valued on revenue).",
                  "Connectivity": "MY ASSUMPTION. Q3 2026: 66.7%.",
                  "SI": "MY ASSUMPTION. Q2 2026 44.7%, Q3 2026 65.5% (CFO expects Q4 company gross margin nearer Q2, citing Q3 one-time benefits and customer mix)."}[k]))
    rows.append((f"x_{k}", f"Multiple, {SEG_NAMES[k]}", MULT[k], "x",
                 {"Space": "MY ASSUMPTION. EV / 2027E revenue. Rocket Lab 39.7x trailing EV/sales.",
                  "Connectivity": "MY ASSUMPTION. EV / 2027E Segment Adjusted EBITDA. T-Mobile US 7.9x trailing.",
                  "SI": "MY ASSUMPTION. EV / 2027E Segment Adjusted EBITDA. CoreWeave 20.1x, Oracle 15.3x trailing."}[k]))
    MINE |= {f"q4r_{k}", f"q4e_{k}", f"r27_{k}", f"m27_{k}", f"x_{k}"}
rows += [
    ("opt", "Value of options not in the three segments (Starship beyond launch, orbital compute, spectrum, Terafab)", OPTIONS, "US$m", "MY ASSUMPTION. Base case."),
    ("gw27", "SI nameplate compute, end 2027", GW_END27, "GW", "Elon Musk, Q3 call, 20 October 2026: surprised by less than 13 GW. Used only to express the gap in gigawatts."),
    ("ORBITAL COMPUTE, AS SPACEX STATES IT", None, None, None, None),
    ("tgt", "Target, compute power per metric ton launched", TARGET_KW_T, "kW/t", "424B4, 12 June 2026."),
    ("ai1kwt", "AI1 vehicle efficiency", AI1_KW_T, "kW/ton", "SpaceX Starmind page, spacex.com/spacexsi/starmind, read 2 November 2026: \"75 kW / ton\"; the page does not say compute or solar, or which ton. Treated here as compute per metric ton."),
    ("ai1avg", "AI1 compute payload, average", AI1_KW_AVG, "kW", "Starmind page: up to 250 kW peak, 175 kW average."),
    ("ai1rad", "AI1 deployable liquid radiator", AI1_RAD_M2, "m2", "Starmind page."),
    ("ai1sol", "AI1 solar array", AI1_SOLAR_KW, "kW", "Starmind page, at 250 W/m2."),
    ("solwm2", "Solar power density", SOLAR_WM2, "W/m2", "Starmind page."),
    ("iss", "Space station radiator areal density", ISS_KG_M2, "kg/m2", "NASA, IEEE Aerospace 2022 (as cited in the journal piece)."),
    ("mass25", "SpaceX mass to orbit, 2025", MASS_25, "t", "424B4, segment data."),
    ("thr", "Claim's launch price test", THRESHOLD_KG, "US$/kg", "Journal piece claim, Google's threshold."),
]
MINE.add("opt")
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY)
        r += 1; continue
    ws.cell(row=r, column=1, value=label).alignment = WRAP
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULTF if unit == "x" else ("#,##0.000" if unit == "m" else (USD2 if unit == "US$" else M1)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  SEGMENTS
ws = sheet("Segments", "SEGMENTS: REVENUE AND SEGMENT ADJUSTED EBITDA (US$ MILLION)", [42, 12, 12, 12, 12, 12, 12, 12])
head(ws, 4, ["", "2024", "2025", "9M 2026", "Q4 2026E*", "2026E*", "2027E*", "Growth 27E"])
r = 5
SR = {}
for k in SEGS:
    ws.cell(row=r, column=1, value=f"{SEG_NAMES[k]} revenue").font = F_B
    for j, v in enumerate([REV_24[k], REV_25[k], REV_9M26[k]]):
        c = ws.cell(row=r, column=2 + j, value=v); c.font = F_IN; c.number_format = M0
    put(ws, f"E{r}", L(f"q4r_{k}"), M0); put(ws, f"F{r}", f"=D{r}+E{r}", M0)
    put(ws, f"G{r}", L(f"r27_{k}"), M0); put(ws, f"H{r}", f"=G{r}/F{r}-1", PCT1)
    ws.cell(row=r + 1, column=1, value=f"{SEG_NAMES[k]} Segment Adjusted EBITDA")
    for j, v in enumerate([EBITDA_24[k], EBITDA_25[k], EBITDA_9M26[k]]):
        c = ws.cell(row=r + 1, column=2 + j, value=v); c.font = F_IN; c.number_format = M0
    put(ws, f"E{r+1}", L(f"q4e_{k}"), M0); put(ws, f"F{r+1}", f"=D{r+1}+E{r+1}", M0)
    put(ws, f"G{r+1}", f"=G{r}*{A[f'm27_{k}']}", M0)
    ws.cell(row=r + 2, column=1, value="  margin")
    for col in "BCDEFG":
        put(ws, f"{col}{r+2}", f"={col}{r+1}/{col}{r}", PCT1)
    SR[k] = r
    r += 4
# totals at row 17
ws["A17"] = "Total revenue"; ws["A17"].font = F_B
ws["A18"] = "Total of Segment Adjusted EBITDA"
for col in "BCDEFG":
    put(ws, f"{col}17", "=" + "+".join(f"{col}{SR[k]}" for k in SEGS), M0)
    put(ws, f"{col}18", "=" + "+".join(f"{col}{SR[k]+1}" for k in SEGS), M0)
ws["A19"] = "Reported total revenue (check = 0)"
put(ws, "B19", f"=B17-{REV_TOT_24}", M0); put(ws, "C19", f"=C17-{REV_TOT_25}", M0); put(ws, "D19", "=D17-27083", M0)
ws["A20"] = "2026E revenue against consensus"; put(ws, "F20", f"=F17/{A['crev26']}-1", PCT1)
ws["A21"] = "2027E revenue against consensus"; put(ws, "G21", f"=G17/{A['crev27']}-1", PCT1)
ws["A23"] = "Quarters (8-K results releases)"; ws["A23"].font = Font(bold=True, color=NAVY)
head(ws, 24, ["US$ million"] + QL)
rr = 25
for k in SEGS:
    ws.cell(row=rr, column=1, value=f"{SEG_NAMES[k]} revenue")
    ws.cell(row=rr + 1, column=1, value=f"{SEG_NAMES[k]} Segment Adjusted EBITDA")
    for j in range(4):
        c = ws.cell(row=rr, column=2 + j, value=QREV[k][j]); c.font = F_IN; c.number_format = M0
        c = ws.cell(row=rr + 1, column=2 + j, value=QEBITDA[k][j]); c.font = F_IN; c.number_format = M0
    rr += 2
ws.cell(row=rr, column=1, value="SI margin, Q2 and Q3 2026")
put(ws, f"D{rr}", "=D30/D29", PCT1); put(ws, f"E{rr}", "=E30/E29", PCT1)
ws.cell(row=rr + 1, column=1, value="Connectivity margin, Q3 2026"); put(ws, f"E{rr+1}", "=E28/E27", PCT1)
note(ws, rr + 3, [
    "*Q4 2026E, 2026E and 2027E are my own estimates. 2024 and 2025 from the 424B4 (2024 segment revenue derived from 2025 less the reported 2025 increase).",
    "9M 2026 from the 20 October 2026 release. Segment Adjusted EBITDA is SpaceX's non-GAAP measure. SI was reported as the AI segment until Q3 2026.",
    "Q1 2026 from the 424B4; Q2 2026 from the 4 August 2026 release; Q3 2025 and Q3 2026 from the 20 October 2026 release.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "SUM OF THE PARTS AND WHAT THE PRICE LEAVES", [60, 16, 12, 16, 12, 14])
head(ws, 4, ["Part", "2027E basis, US$m", "Multiple", "Value, US$m", "Share", "Per share, US$"])
parts = [("Connectivity (Starlink), 2027E Segment Adjusted EBITDA", "Connectivity", f"=Segments!G{SR['Connectivity']+1}"),
         ("Super Intelligence, 2027E Segment Adjusted EBITDA", "SI", f"=Segments!G{SR['SI']+1}"),
         ("Space (launch), 2027E revenue", "Space", f"=Segments!G{SR['Space']}")]
for i, (lab, k, basis) in enumerate(parts):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab)
    put(ws, f"B{rr}", basis, M0, F_LINK); put(ws, f"C{rr}", L(f"x_{k}"), MULTF)
    put(ws, f"D{rr}", f"=B{rr}*C{rr}", M0); put(ws, f"E{rr}", f"=D{rr}/$D$13", PCT1); put(ws, f"F{rr}", f"=D{rr}/$D$14", USD2)
ws["A8"] = "Three businesses, enterprise value"; ws["A8"].font = F_B
put(ws, "D8", "=SUM(D5:D7)", M0); put(ws, "F8", "=D8/$D$14", USD2)
ws["A9"] = "Net cash: cash + marketable securities - debt and finance leases, 30 September 2026"
put(ws, "D9", f"={A['cash']}+{A['secs']}-{A['debtc']}-{A['debtl']}", M0); put(ws, "E9", "=D9/$D$13", PCT1); put(ws, "F9", "=D9/$D$14", USD2)
ws["A10"] = "Options not in the three segments, including orbital compute (MY ASSUMPTION)"
put(ws, "D10", L("opt"), M0); put(ws, "E10", "=D10/$D$13", PCT1); put(ws, "F10", "=D10/$D$14", USD2)
ws["A13"] = "Equity value, base"; ws["A13"].font = F_B; put(ws, "D13", "=D8+D9+D10", M0)
ws["A14"] = "Shares outstanding, Class A + Class B, 15 October 2026 (m)"; put(ws, "D14", f"={A['sha']}+{A['shb']}", '#,##0.0')
ws["A15"] = "Base value per share"; ws["A15"].font = F_B; put(ws, "D15", "=D13/D14", USD2); ws["D15"].fill = FILL_KEY
ws["A16"] = "Three businesses plus net cash only, per share"; put(ws, "D16", "=(D8+D9)/D14", USD2)
ws["A17"] = "Base value against the price"; put(ws, "D17", f"=D15/{A['price']}-1", PCT1)
ws["A18"] = "Band (LONG if +15% or more, SHORT if -25% or less)"
put(ws, "D18", '=IF(D17>=0.15,"LONG",IF(D17<=-0.25,"SHORT","NO CALL"))')
ws["A20"] = "WHAT THE PRICE LEAVES"; ws["A20"].font = Font(bold=True, color=NAVY)
ws["A21"] = "Market value at the price, US$m"; put(ws, "D21", f"={A['price']}*D14", M0)
ws["A22"] = "Enterprise value at the price (market value less net cash), US$m"; put(ws, "D22", "=D21-D9", M0)
ws["A23"] = "Left above the three businesses, US$m"; ws["A23"].font = F_B; put(ws, "D23", "=D22-D8", M0); ws["D23"].fill = FILL_KEY
ws["A24"] = "  as a share of enterprise value"; put(ws, "D24", "=D23/D22", PCT1)
ws["A25"] = "  per share, US$"; put(ws, "D25", "=D23/D14", USD2)
ws["A26"] = "Left after the options I credit, US$m"; put(ws, "D26", "=D23-D10", M0)
ws["A27"] = "  per share, US$"; put(ws, "D27", "=D26/D14", USD2)
ws["A28"] = "SI value per gigawatt of end-2027 nameplate compute, US$m"; put(ws, "D28", f"=D6/{A['gw27']}", M0)
ws["A29"] = "Gap expressed as orbital gigawatts valued like SI (no discount for time)"; put(ws, "D29", "=D23/D28", '0.00')
ws["A30"] = "  AI1 satellites at 175 kW average"; put(ws, "D30", f"=D29*1000000/{A['ai1avg']}", M0)
ws["A31"] = "  tonnes in orbit at AI1's 75 kW per ton (read as compute per metric ton)"; put(ws, "D31", f"=D29*1000000/{A['ai1kwt']}", M0)
ws["A32"] = "  tonnes in orbit at the 100 kW per ton target"; put(ws, "D32", f"=D29*1000000/{A['tgt']}", M0)
ws["A33"] = "  multiple of SpaceX's 2025 mass to orbit (AI1 basis)"; put(ws, "D33", f"=D31/{A['mass25']}", MULTF)
ws["A35"] = "MARKET MULTIPLES AT THE PRICE"; ws["A35"].font = Font(bold=True, color=NAVY)
ws["A36"] = "P/E on 2027 consensus EPS"; put(ws, "D36", f"={A['price']}/{A['ceps27']}", MULTF)
ws["A37"] = "EV / 2027 consensus revenue"; put(ws, "D37", f"=D22/{A['crev27']}", MULTF)
ws["A38"] = "EV / my 2027E total Segment Adjusted EBITDA"; put(ws, "D38", "=D22/Segments!G18", MULTF)
ws["A39"] = "Price against the IPO price"; put(ws, "D39", f"={A['price']}/{A['ipo']}-1", PCT1)
ws["A40"] = "Price against the highest close"; put(ws, "D40", f"={A['price']}/{A['hiclose']}-1", PCT1)
ws["A41"] = "Revisit towards a short above (base 25% below)"; put(ws, "D41", "=D15/0.75", USD2)
ws["A42"] = "Revisit towards a long below (base 15% above)"; put(ws, "D42", "=D15/1.15", USD2)
note(ws, 44, ["Fourth quarter 2026 capital spending (guided US$35bn to 40bn) and the US$40bn Apollo GPU lease (8-K, 26 October 2026) are not deducted:",
              "both buy the capacity my 2027 estimates assume. Share count excludes options and unvested awards (for example those assumed in the Cursor merger)."])

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "SCENARIOS, TWELVE MONTHS OUT (MY ASSUMPTIONS)", [26, 14, 14, 14, 14, 14, 14, 14])
head(ws, 4, ["", "Bear", "Base", "Bull"])
lines = []
rr = 5
for k in SEGS:
    lines.append((f"{SEG_NAMES[k]} revenue 2027E", [s[1][k] for s in SCEN], M0, f"r_{k}"))
    lines.append((f"{SEG_NAMES[k]} margin", [s[2][k] for s in SCEN], PCT1, f"m_{k}"))
    lines.append((f"{SEG_NAMES[k]} multiple", [s[3][k] for s in SCEN], MULTF, f"x_{k}"))
lines.append(("Options, US$m", [s[4] for s in SCEN], M0, "opt"))
lines.append(("Probability", [s[5] for s in SCEN], PCT1, "p"))
RW = {}
for lab, vals, fmt, key in lines:
    ws.cell(row=rr, column=1, value=lab)
    for j, v in enumerate(vals):
        col = "BCD"[j]
        if j == 1:
            base_link = {"opt": L("opt"), "p": None}.get(key)
            if key.startswith("r_"): base_link = L(f"r27_{key[2:]}")
            if key.startswith("m_"): base_link = L(f"m27_{key[2:]}")
            if key.startswith("x_"): base_link = L(key)
            if base_link: put(ws, f"{col}{rr}", base_link, fmt); continue
        c = ws.cell(row=rr, column=2 + j, value=v); c.font = F_IN; c.number_format = fmt; c.fill = FILL_ASSUME
    RW[key] = rr; rr += 1
rr += 1
ws.cell(row=rr, column=1, value="Enterprise value of the three businesses, US$m").font = F_B
for col in "BCD":
    f = (f"={col}{RW['r_Space']}*{col}{RW['x_Space']}"
         f"+{col}{RW['r_Connectivity']}*{col}{RW['m_Connectivity']}*{col}{RW['x_Connectivity']}"
         f"+{col}{RW['r_SI']}*{col}{RW['m_SI']}*{col}{RW['x_SI']}")
    put(ws, f"{col}{rr}", f, M0)
EVR = rr; rr += 1
ws.cell(row=rr, column=1, value="Value per share, US$").font = F_B
for col in "BCD":
    put(ws, f"{col}{rr}", f"=({col}{EVR}+{col}{RW['opt']}+Valuation!$D$9)/Valuation!$D$14", USD2)
VR = rr; rr += 1
ws.cell(row=rr, column=1, value="Change against the price")
for col in "BCD":
    put(ws, f"{col}{rr}", f"={col}{VR}/{A['price']}-1", PCT1)
CR = rr; rr += 2
ws.cell(row=rr, column=1, value="Probability-weighted value, US$").font = F_B
put(ws, f"B{rr}", f"=SUMPRODUCT(B{VR}:D{VR},B{RW['p']}:D{RW['p']})", USD2); WR = rr
put(ws, f"C{rr}", f"=B{rr}/{A['price']}-1", PCT1)
ws.cell(row=rr + 1, column=1, value="Base check against Valuation tab (= 0)"); put(ws, f"B{rr+1}", f"=C{VR}-Valuation!D15", '0.000000')
note(ws, rr + 3, ["Space is valued on revenue in every case; its margin row is shown for completeness. Bear: rented-compute prices fall and",
                  "the ramp slips; no value for options. Bull: SI beats the consensus path and US$300bn is paid for options, orbital compute among them."])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "SENSITIVITY: SI 2027E EBITDA AGAINST ITS MULTIPLE (VALUE PER SHARE, US$)", [30, 14, 14, 14])
head(ws, 4, ["SI EBITDA, US$m"] + [f"{m:.0f}x" for m in SENS_MULT])
for j, m in enumerate(SENS_MULT):
    c = ws.cell(row=3, column=2 + j, value=m); c.font = F_IN; c.number_format = MULTF
for i, e in enumerate(SENS_SI):
    rr = 5 + i
    if i == 1:
        put(ws, f"A{rr}", "=Valuation!B6", M0, F_LINK)
    else:
        c = ws.cell(row=rr, column=1, value=e); c.font = F_IN; c.number_format = M0
    for j in range(3):
        col = "BCD"[j]
        put(ws, f"{col}{rr}", f"=(Valuation!$D$5+Valuation!$D$7+$A{rr}*{col}$3+Valuation!$D$9+Valuation!$D$10)/Valuation!$D$14", USD2)
ws["A9"] = "Cells above the price"; ws["A9"].font = F_B; put(ws, "B9", f'=COUNTIF(B5:D7,">"&{A["price"]})', '0'); ws["C9"] = "of 9"
ws["A10"] = "Cells 25% or more below the price"; ws["A10"].font = F_B; put(ws, "B10", f'=COUNTIF(B5:D7,"<="&{A["price"]}*0.75)', '0'); ws["C10"] = "of 9"
ws["A11"] = "Cells 15% or more above the price"; ws["A11"].font = F_B; put(ws, "B11", f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)', '0'); ws["C11"] = "of 9"
note(ws, 13, ["Row 3 holds the multiples. Everything else at base: Starlink, Space, net cash and options. The middle row links to my SI 2027E EBITDA."])

# =====================================================================  ORBIT
ws = sheet("Orbit", "ORBITAL COMPUTE AND LAUNCH PRICE: THE CLAIM'S TWO TESTS", [64, 14, 14, 14, 14, 14, 14])
ws["A4"] = "AI1, SpaceX's first AI satellite (Starmind page, read 2 November 2026)"; ws["A4"].font = Font(bold=True, color=NAVY)
ws["A5"] = "Vehicle efficiency against the 100 kW per ton target"; put(ws, "B5", f"={A['ai1kwt']}/{A['tgt']}", PCT1)
ws["A6"] = "Shortfall against the target"; put(ws, "B6", "=1-B5", PCT1)
ws["A7"] = "Kilograms launched per kW of compute"; put(ws, "B7", f"=1000/{A['ai1kwt']}", M1)
ws["A8"] = "Implied mass on average compute, tonnes (my arithmetic)"; put(ws, "B8", f"={A['ai1avg']}/{A['ai1kwt']}", '0.00')
ws["A9"] = "Heat per m2 of radiator if all average compute leaves through it, W/m2"; put(ws, "B9", f"={A['ai1avg']}*1000/{A['ai1rad']}", M0)
ws["A10"] = "Radiator mass at the space station's areal density, tonnes"; put(ws, "B10", f"={A['ai1rad']}*{A['iss']}/1000", '0.00')
ws["A11"] = "Solar array area at 250 W/m2, m2"; put(ws, "B11", f"={A['ai1sol']}*1000/{A['solwm2']}", M0)
ws["A13"] = "Launch services revenue per kg of customer payload (8-K releases, my arithmetic)"; ws["A13"].font = Font(bold=True, color=NAVY)
head(ws, 14, ["US$ million / tonnes"] + KG_LABELS)
ws["A15"] = "Launch services revenue, US$m"; ws["A16"] = "Customer payload, t"; ws["A17"] = "US$ per kg"
for j in range(6):
    col = get_column_letter(2 + j)
    c = ws[f"{col}15"]; c.value = LS_REV[j]; c.font = F_IN; c.number_format = M0
    c = ws[f"{col}16"]; c.value = CUST_T[j]; c.font = F_IN; c.number_format = M0
    put(ws, f"{col}17", f"={col}15*1000000/({col}16*1000)", M0)
ws["A19"] = "First nine months of 2026, US$ per kg"; ws["A19"].font = F_B
ws["C19"] = LS_9M26; ws["C19"].font = F_IN; ws["D19"] = CUST_9M26; ws["D19"].font = F_IN
put(ws, "B19", "=C19*1000000/(D19*1000)", M0)
ws["A20"] = "  multiple of the claim's US$200 per kg"; put(ws, "B20", f"=B19/{A['thr']}", MULTF)
ws["A21"] = "Mass for 100 GW a year (424B4: about one million metric tons) / 2025 mass to orbit"; put(ws, "B21", f"=1000000/{A['mass25']}", M0)
note(ws, 23, ["Q1 2025 and Q1 2026 are the half year less the second quarter. Revenue per kg is a mix of missions and orbits, not a list price;",
              "Starship has flown only internal payloads to date. 9M 2026: US$2,108m for 251 t (20 October 2026 release)."])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, 2 NOVEMBER 2026, TRAILING, AT THE 30 OCTOBER CLOSE)", [20, 10, 14, 14, 14, 56])
head(ws, 4, ["Company", "Ticker", "EV, US$bn", "EV/EBITDA", "EV/sales", "What they do"])
for i, (co, tk, ev, eve, evs, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, v in enumerate([ev, eve, evs]):
        c = ws.cell(row=rr, column=3 + j, value=v if v is not None else "n/m"); c.font = F_IN
        c.number_format = '#,##0.00' if j == 0 else MULTF; c.alignment = RIGHT
    ws.cell(row=rr, column=6, value=what).alignment = WRAP
note(ws, 13, ["n/m: EBITDA negative or not meaningful. Multiples only set the ranges for my segment multiples; no view on the peers' shares is expressed."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 140])
head(ws, 4, ["No.", "Source and what it supports"])
src = [
    "SpaceX final prospectus, Form 424B4, 12 June 2026 (SEC EDGAR, CIK 1181412): IPO terms, 2023 to 2025 and Q1 2026 results and segment data, lock-up schedule, voting control, orbital compute disclosure.",
    "SpaceX results releases, Form 8-K Exhibit 99.1, 4 August 2026 (Q2) and 20 October 2026 (Q3): segment revenue, Segment Adjusted EBITDA, capex, launches, payload mass, launch services revenue, subscribers, nameplate compute, balance sheet.",
    "SpaceX Form 10-Q, quarter to 30 September 2026, filed 22 October 2026: shares outstanding at 15 October 2026, backlog, customer concentration, Tesla special committee.",
    "SpaceX Forms 8-K: 23 and 26 June 2026 (US$25bn senior notes), 14 August 2026 (Cursor merger), 26 October 2026 (Apollo GPU finance lease, about US$40bn).",
    "SpaceX Q3 2026 webcast, 20 October 2026, SpaceX edited transcript at ir.spacex.com: Q1 2027 revenue guide, Q4 capex, compute targets, Starmind timing.",
    "SpaceX Starmind page, spacex.com/spacexsi/starmind, read 2 November 2026: AI1 specifications.",
    "Yahoo Finance SPCX history and analysis pages, read 2 November 2026: prices and consensus. stockanalysis.com, 2 November 2026: average target and peer multiples.",
    "Journal piece: Data centres in orbit: the plug is free and the heat is the bill, thephysicallayer.fyi/journal/data-centres-in-space/, 2 November 2026.",
]
for i, s in enumerate(src):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
cover = [
    ("Call", CALL["direction"] + ", " + CALL["conviction"].lower() + " conviction (Tommy Lau, 2 November 2026)"),
    ("Price", "=" + A["price"]),
    ("Base value per share", "=Valuation!D15"),
    ("Base against the price", "=Valuation!D17"),
    ("Band", "=Valuation!D18"),
    ("Probability-weighted value", f"=Scenarios!B{WR}"),
    ("Left above the three businesses, US$m", "=Valuation!D23"),
    ("  share of enterprise value", "=Valuation!D24"),
    ("AI1 kW per ton against the 100 target", "=Orbit!B5"),
    ("Launch revenue per kg, 9M 2026, US$", "=Orbit!B19"),
]
for i, (lab, v) in enumerate(cover):
    ws.cell(row=4 + i, column=1, value=lab).font = F_B
    c = ws.cell(row=4 + i, column=2, value=v); c.alignment = RIGHT
fm = {5: USD2, 6: USD2, 7: PCT1, 9: USD2, 10: M0, 11: PCT1, 12: PCT1, 13: M0}
for rr, f in fm.items():
    ws.cell(row=rr, column=2).number_format = f
ws["B8"].value = "=Valuation!D18"
note(ws, 16, ["Tabs: Assumptions (inputs; yellow = mine), Segments, Valuation (sum of the parts and the gap), Scenarios, Sensitivity,",
              "Orbit (the claim's two tests in SpaceX's own figures), Peers, Sources. All figures US$ million unless stated."])
wb.save(XLSX)
print("model written", XLSX)
