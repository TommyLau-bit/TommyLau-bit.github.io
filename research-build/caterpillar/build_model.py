"""Caterpillar Inc. (NYSE: CAT) initiation model. Segment build to 2028E, adjusted EPS bridge, sum of the parts.
Live formulas throughout. House style: navy header rows, blue font for hardcoded inputs, yellow fill on my own
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
USD2 = '"US$"#,##0.00'; USD0 = '"US$"#,##0'; M0 = '#,##0'; M1 = '#,##0.0'; PCT1 = '0.0%'; PCT0 = '0%'; MULTF = '0.0"x"'; MULT0 = '0"x"'
SUB = f"Tommy Lau | Caterpillar Inc. (NYSE: CAT) | {DATE} | Personal research, not investment advice."

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


ws = sheet("Cover", "CATERPILLAR INC. (NYSE: CAT)  INITIATION MODEL", [42, 26, 100])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [64, 14, 10, 110])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). "
            "Green = link to another tab. Black = formula. US$ million unless stated. Year end 31 December.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}; MINE = set()
Q3R = "Q3 2026 earnings release, Form 8-K Ex. 99.1, 29 October 2026"
REC = "Form 8-K of 26 March 2026, Ex. 99.1 (segments recast for Rail)"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "US$", "NYSE close, 30 October 2026. stockanalysis.com, retrieved 2 November 2026."),
    ("hiclose", "Highest close, 30 June 2026", HI_CLOSE, "US$", "stockanalysis.com. Intraday high US$1,073.46 the same day."),
    ("pxdec", "Close, 31 December 2025", PX_DEC25, "US$", "stockanalysis.com."),
    ("shares_out", "Shares outstanding", SHARES_OUT, "m", "Form 10-Q cover, outstanding at 30 June 2026 (459,674,889). Q3 2026 weighted basic 459.1m, diluted 460.9m (" + Q3R + ")."),
    ("mpe_cash", "MP&E cash, 30 September 2026", MPE_CASH, "US$m", Q3R + ", supplemental consolidating data."),
    ("mpe_debt", "MP&E debt, 30 September 2026", MPE_DEBT, "US$m", Q3R + ": long-term debt due within one year 36 + after one year 10,614 (consolidated presentation)."),
    ("GUIDANCE AND CONSENSUS", None, None, None, None),
    ("eps24", "2024 adjusted EPS", ADJ_EPS["2024A"], "US$", "Q4 2025 earnings release, 29 January 2026."),
    ("eps25", "2025 adjusted EPS", ADJ_EPS["2025A"], "US$", "Q4 2025 earnings release."),
    ("cons26", "2026 consensus adjusted EPS", CONS_EPS26, "US$", "stockanalysis.com (S&P Global), updated 30 October 2026. Cross-check only."),
    ("cons27", "2027 consensus adjusted EPS", CONS_EPS27, "US$", "stockanalysis.com, as above. Cross-check only."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com: 29 analysts, low US$575, high US$1,150. Cross-check only."),
    ("ACTUALS: 9 MONTHS 2026 (Q1 TO Q3 RELEASES)", None, None, None, None),
    ("eps9m", "Adjusted EPS, Q1 to Q3 2026 (5.54 + 8.17 + 7.20)", sum(Q_ADJ_EPS_26), "US$", "Q1, Q2 and Q3 2026 earnings releases. Includes about US$0.86 of tariff refunds (my arithmetic)."),
    ("op9m", "Adjusted operating profit, Q1 to Q3 2026", sum(Q_ADJ_OP_26), "US$m", "3,126 + 4,497 + 4,255. Includes 520 of IEEPA tariff recoveries."),
]
for k in ("PG", "OG", "IN"):
    rows += [(f"a24_{k}", f"{APP_NAMES[k]} external sales, 2024", APP[k]["2024A"], "US$m", REC + "."),
             (f"a25_{k}", f"{APP_NAMES[k]} external sales, 2025", APP[k]["2025A"], "US$m", REC + "."),
             (f"a9m_{k}", f"{APP_NAMES[k]} external sales, Q1 to Q3 2026", APP[k]["9M26"], "US$m", "Q1 to Q3 2026 releases" + (" (Industrial derived as external sales less the other two)." if k == "IN" else "."))]
for k in ("PE", "CI", "RI", "FP"):
    lab = "revenues" if k == "FP" else "sales"
    rows += [(f"s24_{k}", f"{SEG_NAMES[k]} {lab}, 2024", SEG[k]["2024A"][0], "US$m", REC + "."),
             (f"p24_{k}", f"{SEG_NAMES[k]} profit, 2024", SEG[k]["2024A"][1], "US$m", REC + "."),
             (f"s25_{k}", f"{SEG_NAMES[k]} {lab}, 2025", SEG[k]["2025A"][0], "US$m", REC + "."),
             (f"p25_{k}", f"{SEG_NAMES[k]} profit, 2025", SEG[k]["2025A"][1], "US$m", REC + "."),
             (f"s9m_{k}", f"{SEG_NAMES[k]} {lab}, Q1 to Q3 2026", SEG[k]["9M26"][0], "US$m", "Q1 to Q3 2026 releases."),
             (f"p9m_{k}", f"{SEG_NAMES[k]} profit, Q1 to Q3 2026", SEG[k]["9M26"][1], "US$m", "Q1 to Q3 2026 releases.")]
rows += [("MY ESTIMATES: FOURTH QUARTER 2026", None, None, None, None),
         ("q4_PG", "Power Generation sales, Q4 2026", Q4["PG"], "US$m", "MY ESTIMATE. Q4 2025 3,238, up 25%."),
         ("q4_OG", "Oil and Gas sales, Q4 2026", Q4["OG"], "US$m", "MY ESTIMATE. Q4 2025 2,398, up 6%."),
         ("q4_IN", "Industrial sales, Q4 2026", Q4["IN"], "US$m", "MY ESTIMATE. Q4 2025 1,482, up 3%."),
         ("q4_inter", "Power & Energy inter-segment sales, Q4 2026", Q4["PE_INTER"], "US$m", "MY ESTIMATE. Q3 2026 1,496."),
         ("q4_pem", "Power & Energy margin, Q4 2026", Q4["PE_M"], "%", "MY ESTIMATE. CFO on the Q3 call (third-party transcript): Q4 margin similar to Q3's 24.4%."),
         ("q4_cis", "Construction Industries sales, Q4 2026", Q4["CI_S"], "US$m", "MY ESTIMATE. Q4 2025 6,926; volume down modestly, price up."),
         ("q4_cim", "Construction Industries margin, Q4 2026", Q4["CI_M"], "%", "MY ESTIMATE. Q4 2025 14.9%; tariff costs about 200 lower."),
         ("q4_ris", "Resource Industries sales, Q4 2026", Q4["RI_S"], "US$m", "MY ESTIMATE. Q4 2025 4,374, up 15% (strong growth guided)."),
         ("q4_rim", "Resource Industries margin, Q4 2026", Q4["RI_M"], "%", "MY ESTIMATE. Q4 2025 9.6%; Q3 2026 13.5%."),
         ("q4_fp", "Financial Products profit, Q4 2026", Q4["FP_P"], "US$m", "MY ESTIMATE. Q3 2026 264."),
         ("q4_br", "Corporate items and eliminations, Q4 2026", Q4["BRIDGE"], "US$m", "MY ESTIMATE. Adjusted operating profit less segment profit; Q3 2026 about -733 before 128 of tariff refunds."),
         ("q4_below", "Below operating profit (other income less interest), Q4 2026", Q4["BELOW"], "US$m", "MY ESTIMATE."),
         ("tax", "Tax rate on adjusted pre-tax profit", Q4["TAX"], "%", "MY ESTIMATE. Caterpillar guides 23.0% excluding discrete items."),
         ("q4_eq", "Equity in affiliates, Q4 2026", Q4["EQ"], "US$m", "MY ESTIMATE. 131 in nine months."),
         ("q4_sh", "Diluted shares, Q4 2026", Q4["SH"], "m", "MY ESTIMATE. Q3 460.9m; buybacks."),
         ("MY ASSUMPTIONS: 2027 AND 2028", None, None, None, None)]
for key, lab, src in [("PG27", "Power Generation growth, 2027", "Capacity paced; orders into 2029 and 2030."), ("PG28", "Power Generation growth, 2028", "Takes 2028 to about 2.4x 2024."),
                      ("OG27", "Oil and Gas growth, 2027", ""), ("OG28", "Oil and Gas growth, 2028", ""), ("IN27", "Industrial growth, 2027", ""), ("IN28", "Industrial growth, 2028", ""),
                      ("PEM27", "Power & Energy margin, 2027", "Q3 2026 24.4%."), ("PEM28", "Power & Energy margin, 2028", ""),
                      ("CI27", "Construction Industries growth, 2027", "After a 21% year with a dealer stock build."), ("CI28", "Construction Industries growth, 2028", ""),
                      ("CIM27", "Construction Industries margin, 2027", ""), ("CIM28", "Construction Industries margin, 2028", ""),
                      ("RI27", "Resource Industries growth, 2027", ""), ("RI28", "Resource Industries growth, 2028", ""),
                      ("RIM27", "Resource Industries margin, 2027", "2024 17.0%, 2025 13.5% (tariffs)."), ("RIM28", "Resource Industries margin, 2028", ""),
                      ("FP27", "Financial Products profit, 2027", ""), ("FP28", "Financial Products profit, 2028", ""),
                      ("BR27", "Corporate items and eliminations, 2027", "No tariff refunds; 2025 was -2,453."), ("BR28", "Corporate items and eliminations, 2028", ""),
                      ("BELOW", "Below operating profit, 2027 and 2028", "2024 +147, 2025 +97."), ("EQ", "Equity in affiliates, 2027 and 2028", ""),
                      ("SH27", "Diluted shares, 2027", "About US$6bn a year of buybacks."), ("SH28", "Diluted shares, 2028", "")]:
    unit = "%" if key[:2] in ("PG", "OG", "IN", "PE", "CI", "RI") else ("m" if key.startswith("SH") else "US$m")
    rows.append((key.lower(), lab, G[key], unit, "MY ASSUMPTION. " + src))
rows += [("pg_pe", "Multiple on 2028E Power Generation earnings", PG_PE, "x", "MY ASSUMPTION. Power peers (GE Vernova, Siemens Energy, Wärtsilä) median 21.8x forward; GE Vernova 37.2x."),
         ("rest_pe", "Multiple on 2028E earnings of the rest of Caterpillar", REST_PE, "x", "MY ASSUMPTION. Caterpillar's 2021 to 2024 average forward P/E 16.3x; machinery and truck peers median 15.2x.")]
for r_ in rows:
    if r_[1] is not None and (r_[4] or "").startswith("MY"):
        MINE.add(r_[0])
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY); r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else (M1 if unit == "m" else (USD2 if unit == "US$" else M0)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
a = lambda k: A[k]

# =====================================================================  SEGMENTS
ws = sheet("Segments", "SEGMENTS: SALES AND PROFIT, 2024A TO 2028E (US$ MILLION)", [50, 13, 13, 13, 13, 13])
head(ws, 4, ["US$ million", "2024A", "2025A", "2026E*", "2027E*", "2028E*"])
labels = {5: "Power Generation external sales", 6: "  growth", 7: "Oil and Gas external sales", 8: "Industrial external sales",
          9: "Power & Energy external sales", 10: "Power & Energy total sales (incl. inter-segment)", 11: "  total / external",
          12: "Power & Energy margin", 13: "Power & Energy profit", 14: "  of which Power Generation (my allocation)",
          16: "Construction Industries sales", 17: "  growth", 18: "  margin", 19: "  profit",
          21: "Resource Industries sales", 22: "  growth", 23: "  margin", 24: "  profit",
          26: "Financial Products profit", 28: "Total segment profit", 29: "Power Generation share of segment profit"}
for rr, t in labels.items():
    ws.cell(row=rr, column=1, value=t).font = F_B if not t.startswith("  ") else Font()
for col, y in (("B", "24"), ("C", "25")):
    for rr, k in ((5, "PG"), (7, "OG"), (8, "IN")):
        put(ws, f"{col}{rr}", f"={a(f'a{y}_{k}')}", M0)
    put(ws, f"{col}10", f"={a(f's{y}_PE')}", M0); put(ws, f"{col}13", f"={a(f'p{y}_PE')}", M0)
    put(ws, f"{col}16", f"={a(f's{y}_CI')}", M0); put(ws, f"{col}19", f"={a(f'p{y}_CI')}", M0)
    put(ws, f"{col}21", f"={a(f's{y}_RI')}", M0); put(ws, f"{col}24", f"={a(f'p{y}_RI')}", M0)
    put(ws, f"{col}26", f"={a(f'p{y}_FP')}", M0)
# 2026E
put(ws, "D5", f"={a('a9m_PG')}+{a('q4_PG')}", M0); put(ws, "D7", f"={a('a9m_OG')}+{a('q4_OG')}", M0); put(ws, "D8", f"={a('a9m_IN')}+{a('q4_IN')}", M0)
put(ws, "D10", f"={a('s9m_PE')}+{a('q4_PG')}+{a('q4_OG')}+{a('q4_IN')}+{a('q4_inter')}", M0)
put(ws, "D13", f"={a('p9m_PE')}+({a('q4_PG')}+{a('q4_OG')}+{a('q4_IN')}+{a('q4_inter')})*{a('q4_pem')}", M0)
put(ws, "D16", f"={a('s9m_CI')}+{a('q4_cis')}", M0); put(ws, "D19", f"={a('p9m_CI')}+{a('q4_cis')}*{a('q4_cim')}", M0)
put(ws, "D21", f"={a('s9m_RI')}+{a('q4_ris')}", M0); put(ws, "D24", f"={a('p9m_RI')}+{a('q4_ris')}*{a('q4_rim')}", M0)
put(ws, "D26", f"={a('p9m_FP')}+{a('q4_fp')}", M0)
for col, prev, y in (("E", "D", "27"), ("F", "E", "28")):
    put(ws, f"{col}5", f"={prev}5*(1+{a('pg' + y)})", M0)
    put(ws, f"{col}7", f"={prev}7*(1+{a('og' + y)})", M0); put(ws, f"{col}8", f"={prev}8*(1+{a('in' + y)})", M0)
    put(ws, f"{col}10", f"={col}9*$D$11", M0)
    put(ws, f"{col}12", f"={a('pem' + y)}", PCT1); put(ws, f"{col}13", f"={col}10*{col}12", M0)
    put(ws, f"{col}16", f"={prev}16*(1+{a('ci' + y)})", M0); put(ws, f"{col}18", f"={a('cim' + y)}", PCT1); put(ws, f"{col}19", f"={col}16*{col}18", M0)
    put(ws, f"{col}21", f"={prev}21*(1+{a('ri' + y)})", M0); put(ws, f"{col}23", f"={a('rim' + y)}", PCT1); put(ws, f"{col}24", f"={col}21*{col}23", M0)
    put(ws, f"{col}26", f"={a('fp' + y)}", M0)
for col in "BCDEF":
    put(ws, f"{col}9", f"={col}5+{col}7+{col}8", M0)
    put(ws, f"{col}11", f"={col}10/{col}9", '0.0000')
    if col in "BCD":
        put(ws, f"{col}12", f"={col}13/{col}10", PCT1); put(ws, f"{col}18", f"={col}19/{col}16", PCT1); put(ws, f"{col}23", f"={col}24/{col}21", PCT1)
    put(ws, f"{col}14", f"={col}13*{col}5/{col}9", M0)
    put(ws, f"{col}28", f"={col}13+{col}19+{col}24+{col}26", M0)
    put(ws, f"{col}29", f"={col}14/{col}28", PCT1)
for col, prev in (("C", "B"), ("D", "C"), ("E", "D"), ("F", "E")):
    put(ws, f"{col}6", f"={col}5/{prev}5-1", PCT1); put(ws, f"{col}17", f"={col}16/{prev}16-1", PCT1); put(ws, f"{col}22", f"={col}21/{prev}21-1", PCT1)
note(ws, 31, ["*2026E = Q1 to Q3 2026 actual + my Q4; 2027E and 2028E are my estimates. 2024A and 2025A as recast for Rail (Form 8-K, 26 March 2026).",
              "Power Generation profit is my allocation: Caterpillar does not report it. I give it the Power & Energy margin and its share of that segment's external sales.",
              "2027E and 2028E Power & Energy total sales keep the 2026E ratio of total to external sales (inter-segment sales)."])

# =====================================================================  EPS
ws = sheet("EPS", "ADJUSTED EPS BRIDGE (US$ MILLION UNLESS STATED)", [56, 13, 13, 13, 13, 13])
head(ws, 4, ["", "2024A", "2025A", "2026E*", "2027E*", "2028E*"])
lab = ["Total segment profit", "Corporate items and eliminations", "Adjusted operating profit", "Below operating profit", "Adjusted pre-tax profit",
       "Tax", "Equity in affiliates", "Adjusted profit", "Diluted shares, m", "ADJUSTED EPS, US$", "Growth", "Consensus, US$", "Mine against consensus",
       "Power Generation EPS, US$ (my allocation)", "Rest of Caterpillar EPS, US$"]
for i, t in enumerate(lab):
    ws.cell(row=5 + i, column=1, value=t).font = F_B if i in (2, 9) else Font()
put(ws, "B7", 13431, M0, F_IN); put(ws, "C7", 11595, M0, F_IN)
for col in "BC":
    put(ws, f"{col}5", f"=Segments!{col}28", M0, F_LINK); put(ws, f"{col}6", f"={col}7-{col}5", M0)
put(ws, "B14", f"={a('eps24')}", USD2); put(ws, "C14", f"={a('eps25')}", USD2)
# 2026E: nine months actual EPS plus my Q4 EPS
put(ws, "D5", "=Segments!D28", M0, F_LINK)
put(ws, "D7", f"={a('op9m')}+(({a('q4_PG')}+{a('q4_OG')}+{a('q4_IN')}+{a('q4_inter')})*{a('q4_pem')}+{a('q4_cis')}*{a('q4_cim')}+{a('q4_ris')}*{a('q4_rim')}+{a('q4_fp')}+{a('q4_br')})", M0)
put(ws, "D6", "=D7-D5", M0)
ws["D8"] = "n.a."; ws["D9"] = "n.a."; ws["D12"] = "n.a."; ws["D13"] = "n.a."
for c_ in ("D8", "D9", "D12", "D13"): ws[c_].alignment = RIGHT
put(ws, "D10", f"=(D7-{a('op9m')}+{a('q4_below')})*(1-{a('tax')})", M0)
ws["A20"] = "2026E: Q4 adjusted EPS (my estimate)"; ws["A20"].font = F_B
put(ws, "D20", f"=(D10+{a('q4_eq')})/{a('q4_sh')}", USD2)
put(ws, "D14", f"={a('eps9m')}+D20", USD2, F_B, FILL_KEY)
ws["A21"] = "2026E row 10 shows Q4 after-tax profit only; 2026E EPS = nine months actual US$20.91 + Q4."; ws["A21"].font = F_NOTE
for col, y in (("E", "27"), ("F", "28")):
    put(ws, f"{col}5", f"=Segments!{col}28", M0, F_LINK)
    put(ws, f"{col}6", f"={a('br' + y)}", M0)
    put(ws, f"{col}7", f"={col}5+{col}6", M0)
    put(ws, f"{col}8", f"={a('below')}", M0)
    put(ws, f"{col}9", f"={col}7+{col}8", M0)
    put(ws, f"{col}10", f"=-{col}9*{a('tax')}", M0)
    put(ws, f"{col}11", f"={a('eq')}", M0)
    put(ws, f"{col}12", f"={col}9+{col}10+{col}11", M0)
    put(ws, f"{col}13", f"={a('sh' + y)}", M1)
    put(ws, f"{col}14", f"={col}12/{col}13", USD2, F_B, FILL_KEY)
for col, prev in (("C", "B"), ("D", "C"), ("E", "D"), ("F", "E")):
    put(ws, f"{col}15", f"={col}14/{prev}14-1", PCT1)
put(ws, "D16", f"={a('cons26')}", USD2); put(ws, "E16", f"={a('cons27')}", USD2)
put(ws, "D17", "=D14/D16-1", PCT1); put(ws, "E17", "=E14/E16-1", PCT1)
for col in "DEF":
    put(ws, f"{col}18", f"={col}14*Segments!{col}29", USD2); put(ws, f"{col}19", f"={col}14-{col}18", USD2)
note(ws, 23, ["*My estimates. Adjusted EPS excludes restructuring and pension mark-to-market, as Caterpillar defines it. 2024A and 2025A as reported.",
              "Corporate items and eliminations = adjusted operating profit less the four segments' profit. 2026E includes US$520m of IEEPA tariff refunds.",
              "Power Generation EPS allocates EPS in proportion to segment profit (corporate costs, interest and tax spread pro rata)."])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: SUM OF THE PARTS ON 2028E ADJUSTED EPS, TWELVE MONTHS OUT", [64, 16, 70])
head(ws, 4, ["Item", "Value", "Working / note"])
vrows = [
    (5, "2028E Power Generation EPS, US$", "=EPS!F18", USD2, "My allocation."),
    (6, "Multiple", f"={a('pg_pe')}", MULTF, ""),
    (7, "Power Generation value, US$", "=B5*B6", USD2, ""),
    (8, "2028E rest of Caterpillar EPS, US$", "=EPS!F19", USD2, ""),
    (9, "Multiple", f"={a('rest_pe')}", MULTF, ""),
    (10, "Rest of Caterpillar value, US$", "=B8*B9", USD2, ""),
    (11, "BASE VALUE PER SHARE, US$", "=B7+B10", USD2, ""),
    (12, "Reference price, US$", f"={a('price')}", USD2, "NYSE close, 30 October 2026."),
    (13, "Base value against price", "=B11/B12-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (14, "VIEW ON THE BAND", '=IF(B13>=0.15,"LONG",IF(B13<=-0.25,"SHORT","NO CALL"))', None, "The band's view; Tommy Lau's call is NO CALL."),
    (15, "Power Generation share of base value", "=B7/B11", PCT1, ""),
    (16, "Blended P/E on 2028E", "=B11/EPS!F14", MULTF, ""),
    (18, "Multiple the price pays for Power Generation (rest at its multiple)", "=(B12-B10)/B5", MULTF, "What is left of the price after the rest."),
    (19, "Same, at the record close of 30 June 2026", f"=({a('hiclose')}-B10)/B5", MULTF, ""),
    (20, "Power Generation share of the price", "=(B12-B10)/B12", PCT1, ""),
    (21, "Same, at the record close", f"=({a('hiclose')}-B10)/{a('hiclose')}", PCT1, ""),
    (23, "Market value, US$bn", f"={a('shares_out')}*B12/1000", '#,##0.0', ""),
    (24, "MP&E net debt, US$m, 30 September 2026", f"={a('mpe_debt')}-{a('mpe_cash')}", M0, "Excludes Cat Financial, whose debt funds its loans."),
    (25, "P/E on 2026 consensus", f"=B12/{a('cons26')}", MULTF, ""),
    (26, "P/E on 2027 consensus", f"=B12/{a('cons27')}", MULTF, ""),
    (27, "P/E on 2026E (mine)", "=B12/EPS!D14", MULTF, ""),
    (28, "P/E on 2027E (mine)", "=B12/EPS!E14", MULTF, ""),
    (29, "P/E on 2028E (mine)", "=B12/EPS!F14", MULTF, ""),
    (30, "P/E on 2027 consensus at the record close", f"={a('hiclose')}/{a('cons27')}", MULTF, ""),
    (31, "Price below which the base value is 15% or more above it, US$", "=B11/1.15", USD2, ""),
    (32, "Price above which the base value is 25% or more below it, US$", "=B11/0.75", USD2, ""),
    (33, "Price against the record close", f"=B12/{a('hiclose')}-1", PCT1, ""),
    (34, "Price change in 2026 to date", f"=B12/{a('pxdec')}-1", PCT1, ""),
    (35, "Average analyst target against price", f"={a('constp')}/B12-1", PCT1, "Cross-check only."),
]
for rr, lab_, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab_)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    if rr in (11, 14):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    elif isinstance(f, str) and (f.startswith("=Assumptions") or f.startswith("=EPS")): c.font = F_LINK
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (VALUE ON 2028E)", [10] + [10] * 14 + [11, 11, 11, 11, 11, 11])
hdr = ["Case", "PG g27", "PG g28", "OG g27", "OG g28", "P&E m27", "P&E m28", "CI g27", "CI g28", "CI m27", "CI m28",
       "RI g27", "RI g28", "RI m27", "RI m28", "PG x", "Rest x", "2028E EPS", "PG EPS", "Value, US$", "vs price"]
head(ws, 4, hdr)
keys = ["pg27", "pg28", "og27", "og28", "pem27", "pem28", "ci27", "ci28", "cim27", "cim28", "ri27", "ri28", "rim27", "rim28"]
r = 5
for name, ov, mpg, mrest, p in SCEN:
    ws.cell(row=r, column=1, value=name).font = F_B
    for j, k in enumerate(keys):
        col = 2 + j
        if name == "Base" or k not in ov:
            c = ws.cell(row=r, column=col, value="=" + a(k)); c.font = F_LINK
        else:
            c = ws.cell(row=r, column=col, value=ov[k]); c.font = F_INB; c.fill = FILL_ASSUME
        c.number_format = PCT1
    for j, (v, kk) in enumerate([(mpg, "pg_pe"), (mrest, "rest_pe")]):
        c = ws.cell(row=r, column=16 + j, value=("=" + a(kk)) if name == "Base" else v)
        c.font = F_LINK if name == "Base" else F_INB
        if name != "Base": c.fill = FILL_ASSUME
        c.number_format = MULT0
    pg28 = f"Segments!$D$5*(1+B{r})*(1+C{r})"
    og28 = f"Segments!$D$7*(1+D{r})*(1+E{r})"
    in28 = f"Segments!$D$8*(1+{a('in27')})*(1+{a('in28')})"
    ext = f"({pg28}+{og28}+{in28})"
    pep = f"{ext}*Segments!$D$11*G{r}"
    cip = f"Segments!$D$16*(1+H{r})*(1+I{r})*K{r}"
    rip = f"Segments!$D$21*(1+L{r})*(1+M{r})*O{r}"
    seg = f"({pep}+{cip}+{rip}+{a('fp28')})"
    ws.cell(row=r, column=18, value=f"=(({seg}+{a('br28')}+{a('below')})*(1-{a('tax')})+{a('eq')})/{a('sh28')}").number_format = USD2
    ws.cell(row=r, column=19, value=f"=R{r}*({pep}*{pg28}/{ext})/{seg}").number_format = USD2
    ws.cell(row=r, column=20, value=f"=S{r}*P{r}+(R{r}-S{r})*Q{r}").number_format = USD2
    ws.cell(row=r, column=21, value=f"=T{r}/{a('price')}-1").number_format = PCT1
    r += 1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[4]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, US$"; ws["A11"].font = F_B
ws["E11"] = "=B9*T5+C9*T6+D9*T7"; ws["E11"].number_format = USD2; ws["E11"].font = F_B; ws["E11"].fill = FILL_KEY
ws["F11"] = f"=E11/{a('price')}-1"; ws["F11"].number_format = PCT1
ws["A12"] = "Check: base case equals the Valuation tab"; ws["E12"] = "=T6-Valuation!B11"; ws["E12"].number_format = '0.000'
note(ws, 14, ["PG = Power Generation, OG = Oil and Gas, P&E = Power & Energy, CI = Construction Industries, RI = Resource Industries; g = growth, m = margin.",
              "Bear: data centre orders pause and the building cycle turns; 18x power, 14x the rest. Bull: capacity arrives early and the cycle holds; 30x and 18x.",
              "Industrial growth, Financial Products, corporate costs, tax and shares are the base case in every case."])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: POWER GENERATION MULTIPLE AGAINST THE REST'S MULTIPLE (US$)", [34, 14, 14, 14])
head(ws, 4, ["Power x \\ rest x", "", "", ""])
for j, (mm, link) in enumerate(zip(SENS_REST, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + a("rest_pe")) if link else mm)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (mm, link) in enumerate(zip(SENS_PG, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=("=" + a("pg_pe")) if link else mm)
    c.number_format = MULT0; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=f"=$A{rr}*EPS!$F$18+{col}$4*EPS!$F$19").number_format = USD0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["B9"] = f'=COUNTIF(B5:D7,">"&{a("price")})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["B10"] = f'=COUNTIF(B5:D7,">="&{a("price")}*1.15)'; ws["C10"] = "of 9"
ws["A11"] = "Cells 25% or more below the price"; ws["B11"] = f'=COUNTIF(B5:D7,"<="&{a("price")}*0.75)'; ws["C11"] = "of 9"
for c_ in ("A9", "A10", "A11"): ws[c_].font = F_B
note(ws, 13, ["Both multiples apply to my 2028E EPS split (EPS tab). The middle cell is the base value."])

# =====================================================================  BACKLOG
ws = sheet("Backlog", "THE QUEUE: FIRM BACKLOG AND POWER GENERATION SALES", [58] + [10] * 11)
head(ws, 4, ["US$ billion"] + BL_LABELS)
ws["A5"] = "Firm backlog"; ws["A6"] = "Not expected within twelve months"; ws["A7"] = "Share not expected within twelve months"
for j in range(len(BL)):
    col = get_column_letter(2 + j)
    put(ws, f"{col}5", BL[j], '0.0', F_IN)
    if BL_LATE[j] is not None:
        put(ws, f"{col}6", BL_LATE[j], '0.0', F_IN); put(ws, f"{col}7", f"={col}6/{col}5", PCT1)
put(ws, "I6", f"=I5*(1-{BL_Q3_WITHIN12})", '0.0'); put(ws, "I7", "=I6/I5", PCT1)
ws["A9"] = "Sales and revenues over the previous four quarters, Dec 2024, US$m"; put(ws, "B9", TTM_SALES_DEC24, M0, F_IN)
ws["A10"] = "Sales and revenues over the previous four quarters, Sep 2026, US$m (Q4 2025 + 9M 2026)"; put(ws, "B10", TTM_SALES_SEP26, M0, F_IN)
ws["A11"] = "Backlog in years of trailing sales, Dec 2024"; put(ws, "B11", "=B5*1000/B9", '0.00')
ws["A12"] = "Backlog in years of trailing sales, Sep 2026"; put(ws, "B12", "=I5*1000/B10", '0.00')
ws["A13"] = "Backlog growth, Sep 2025 to Sep 2026"; put(ws, "B13", "=I5/E5-1", PCT1)
ws["A14"] = "Customer advances, Dec 2025 and Sep 2026, US$m"; put(ws, "B14", CUST_ADV["Dec 25"], M0, F_IN); put(ws, "C14", CUST_ADV["Sep 26"], M0, F_IN)
ws["A15"] = "Customer advances growth"; put(ws, "B15", "=C14/B14-1", PCT1)
head(ws, 17, ["Power Generation sales, US$m"] + PG_Q_LABELS)
ws["A18"] = "Quarterly external sales"; ws["A19"] = "Growth on the same quarter a year earlier"
for j, v in enumerate(PG_Q):
    col = get_column_letter(2 + j)
    put(ws, f"{col}18", v, M0, F_IN)
    if j >= 4:
        put(ws, f"{col}19", f"={col}18/{get_column_letter(2 + j - 4)}18-1", PCT1)
note(ws, 21, ["Sources: Form 10-K 2024 and 2025; Form 10-Qs March 2025 to June 2026; Q3 2026 slides (US$78.1bn). The Sep 2026 split uses the CFO's 58% within",
              "twelve months from the Q3 call (third-party transcript); the Q3 10-Q was not out on 2 November 2026. Power Generation from Form 8-K of 26 March 2026 and 2026 releases.",
              "Wells Fargo virtual HQ visit, 10 September 2026 (transcript posted by Caterpillar): orders into 2029, a first turbine order into 2030; 'pretty full for 2027'."])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, RETRIEVED 2 NOVEMBER 2026)", [20, 15, 13, 18, 70])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "EV/EBIT (trailing)", "What they make"])
for i, (co, tk, pe_, eve, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, v in enumerate([pe_, eve]):
        c = ws.cell(row=rr, column=3 + j, value=v); c.number_format = MULTF; c.font = F_IN
    ws.cell(row=rr, column=5, value=what).alignment = WRAP
ws["A16"] = "Power peers median (GE Vernova, Siemens Energy, Wärtsilä)"; ws["C16"] = "=MEDIAN(C6:C8)"
ws["A17"] = "Machinery and truck peers median (Cummins to Deere)"; ws["C17"] = "=MEDIAN(C9:C13)"
ws["A18"] = "Caterpillar forward P/E, 2021 to 2024 average"; ws["C18"] = f"=AVERAGE({','.join(str(v) for v in list(HIST_FWD_PE.values())[:4])})"
for c_ in ("A16", "A17", "A18"): ws[c_].font = F_B
for c_ in ("C16", "C17", "C18"): ws[c_].number_format = MULTF
note(ws, 20, ["Multiples only, to set the range. No view on the peers' shares is expressed. Caterpillar's history (stockanalysis.com): 17.95x, 15.83x,",
              "14.51x, 17.06x, 27.73x for 2021 to 2025."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 150])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Caterpillar Q3 2026 earnings release, Form 8-K Ex. 99.1, 29 October 2026: segment sales and profit, Power & Energy sales by application, adjusted EPS reconciliation, balance sheet, customer advances, MP&E data.",
    "Caterpillar Q3 2026 analyst slides, 29 October 2026 (investors.caterpillar.com): backlog US$78.1bn, 2026 outlook, margin target range, retail statistics, results calendar (Q4 2026 on 2 February 2027).",
    "Caterpillar Q1 and Q2 2026 earnings releases, Form 8-K Ex. 99.1, 30 April and 4 August 2026; Form 10-Q for the quarter to 30 June 2026 (outlook, backlog, tariff refunds).",
    "Caterpillar Form 8-K of 26 March 2026, Ex. 99.1: 2024 and 2025 quarterly segment data recast for the Rail move; Power & Energy sales by application.",
    "Caterpillar Q4 2025 earnings release (29 January 2026) and analyst slides: 2024 and 2025 adjusted operating profit and EPS; 2030 targets incl. Power Generation sales more than 2x 2024.",
    "Caterpillar Form 10-K for 2024 and 2025; Form 10-Qs March 2025 to June 2026: firm backlog and the part not expected within twelve months.",
    "Caterpillar virtual HQ visit with Wells Fargo, 10 September 2026, transcript posted on Caterpillar's IR site: capacity target from two to three times, orders into 2029 and 2030, framework agreements, 'free supply'.",
    "Caterpillar Q3 2026 earnings call, 29 October 2026, third-party transcript (The Singju Post): 'as far out as 2029', 58% of backlog within twelve months, Q4 guidance by segment.",
    "stockanalysis.com (S&P Global Market Intelligence data), retrieved 2 November 2026: daily and month-end prices, consensus, targets, forward P/E and EV/EBIT.",
    "The Physical Layer, 'Building your own power', 22 September 2026, claim of 30 October 2026: https://thephysicallayer.fyi/journal/building-your-own-power/",
    "Estimates for Q4 2026, 2027 and 2028 are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Tommy Lau's call (the band's view)", "=Valuation!B14", None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Base value per share, US$", "=Valuation!B11", USD2, "Sum of the parts on 2028E adjusted EPS."),
    ("Reference price, US$", "=" + a("price"), USD2, "NYSE close, 30 October 2026."),
    ("Base value against price", "=Valuation!B13", PCT1, ""),
    ("Probability-weighted value, US$", "=Scenarios!E11", USD2, "25 / 50 / 25 bear / base / bull."),
    ("2028E adjusted EPS, US$", "=EPS!F14", USD2, "My estimate."),
    ("Multiple the price pays for Power Generation", "=Valuation!B18", MULTF, "With the rest at its base multiple."),
    ("Horizon", "12 months, to October 2027", None, ""),
    ("Wrong if", "See note", None, WRONG_IF),
    ("Revisit if", "See note", None, REVISIT_IF),
]
for i, (lab_, v, fmt, nt) in enumerate(cover):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab_).font = F_B
    c = ws.cell(row=rr, column=2, value=v)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    c.font = F_LINK if isinstance(v, str) and v.startswith("=") else F_IN
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
ws.row_dimensions[14].height = 58; ws.row_dimensions[15].height = 44
ws["A18"] = "Tabs"; ws["A18"].font = Font(bold=True, color=NAVY)
for i, (t, d_) in enumerate([("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
                             ("Segments", "Sales and profit by segment and Power & Energy application, 2024A to 2028E."),
                             ("EPS", "Bridge from segment profit to adjusted EPS; the Power Generation split."),
                             ("Valuation", "Sum of the parts, the band, what the price pays for power."),
                             ("Scenarios", "Bear / base / bull and the probability-weighted value."),
                             ("Sensitivity", "Power multiple against the rest's multiple."),
                             ("Backlog", "The queue: backlog, the part due later, Power Generation by quarter."),
                             ("Peers", "Forward P/E and EV/EBIT used to set the multiples."), ("Sources", "Every source used.")]):
    ws.cell(row=19 + i, column=1, value=t); ws.cell(row=19 + i, column=2, value=d_)
ws["A29"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."; ws["A29"].font = F_NOTE
ws["A30"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."; ws["A30"].font = F_NOTE
for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
