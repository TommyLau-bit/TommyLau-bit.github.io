"""Nvidia initiation model, 2 Nov 2026. Live formulas throughout.

House style follows the Vertiv and Broadcom models: navy header rows, blue font for hardcoded inputs, yellow fill on
my own assumptions, green font for links to the Assumptions tab, black for formulas.
Non-GAAP basis from FY27 (includes stock-based pay); FY25 and FY26 history shown on GAAP EPS.
Fiscal years end on the last Sunday of January (FY2027 = year to about 31 Jan 2027).
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
F_B = Font(bold=True)
F_NOTE = Font(color=MUTED, size=9, italic=True)
FILL_HDR = PatternFill("solid", fgColor=NAVY)
FILL_ASSUME = PatternFill("solid", fgColor="FFFF00")
FILL_KEY = PatternFill("solid", fgColor="D9E2F3")
WRAP = Alignment(wrap_text=True, vertical="top")
RIGHT = Alignment(horizontal="right")

USD2 = '"US$"#,##0.00'; USD0 = '"US$"#,##0'; BN1 = '#,##0.0'; BN2 = '#,##0.00'; BN3 = '#,##0.000'
PCT1 = '0.0%'; PCT0 = '0%'; MULT = '0.0"x"'; MULT0 = '0"x"'
SUB = (f"Tommy Lau | Nvidia Corporation (Nasdaq: NVDA) | {DATE_LONG} | Non-GAAP from FY27; FY27 ends about 31 Jan 2027 | "
       "Personal research, not investment advice.")

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


def put(ws, r, c, v, fmt=None, bold=False):
    x = ws.cell(row=r, column=c, value=v if v is not None else "")
    if fmt: x.number_format = fmt
    x.alignment = RIGHT
    if v is not None and not isinstance(v, str):
        x.font = Font(color="0000FF", bold=bold)
    elif isinstance(v, str) and v.startswith("=Assumptions"):
        x.font = Font(color="008000", bold=bold)
    elif bold:
        x.font = F_B
    return x


def label(ws, r, text, bold=False):
    ws.cell(row=r, column=1, value=text).font = F_B if bold else Font()


sheet("Cover", "NVIDIA CORPORATION (NASDAQ: NVDA)  INITIATION MODEL", [34, 26, 96])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [62, 14, 10, 96])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "this tab. Black = formula. US$ billion unless stated; per-share figures in US$; shares in billions.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"edge3", "edge4", "revq4", "omq4", "oiq", "tax", "sh27", "gw28", "gw29", "usd28", "usd29", "edge28", "edge29",
        "om28", "om29", "oiyr", "sh28", "sh29", "mbase"}
rows = [
    ("MARKET (retrieved 2 November 2026)", None, None, None, None),
    ("price", "Share price (Nasdaq: NVDA)", PRICE, "US$", "Nasdaq close, 30 October 2026. Nasdaq.com historical data (Yahoo Finance answered 'Too Many Requests')."),
    ("hi52", "52-week high (intraday, 6 October 2026)", HI52, "US$", "Nasdaq.com."),
    ("hiclose", "Highest close (6 October 2026)", HI_CLOSE, "US$", "Nasdaq.com."),
    ("lo52", "52-week low (intraday, 30 March 2026)", LO52, "US$", "Nasdaq.com."),
    ("loclose", "Lowest close in 52 weeks (30 March 2026)", LO_CLOSE, "US$", "Nasdaq.com."),
    ("pxdec25", "Close, 31 December 2025", PRICE_DEC25, "US$", "Nasdaq.com."),
    ("shares", "Shares outstanding, 21 August 2026", SHARES_OUT, "bn", "Form 10-Q cover: 24.1 billion."),
    ("cash", "Cash, equivalents and marketable debt securities, 26 Jul 2026", CASH, "US$bn", "10-Q balance sheet: 22.443 + 34.143."),
    ("debt", "Short and long-term debt, 26 Jul 2026", DEBT, "US$bn", "10-Q balance sheet: 1.000 + 32.366. Marketable equity securities of US$42.8bn are not counted."),
    ("cons27", "FY27 consensus EPS", CONS_EPS_27, "US$", "stockanalysis.com (S&P Global, updated 26 Oct 2026), 54 analysts; range 9.01 to 10.10."),
    ("consrev27", "FY27 consensus revenue", CONS_REV_27, "US$bn", "Same; range 403.2 to 426.9."),
    ("cons28", "FY28 consensus EPS", CONS_EPS_28, "US$", "Same page, shown as 'EPS Next Year'. FY28 detail is behind a paywall."),
    ("consrev28", "FY28 consensus revenue", CONS_REV_28, "US$bn", "Same page, shown as 'Revenue Next Year'."),
    ("constp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com, 62 analysts; median 315, range 180 to 515."),
    ("fwdpe", "Forward P/E shown by stockanalysis.com", FWD_PE_SA, "x", "stockanalysis.com, at the 30 October 2026 close."),
    ("REPORTED AND GUIDED (CFO commentaries, 10-Q, 8-K)", None, None, None, None),
    ("g3rev", "Q3 FY27 revenue guide", G3["rev"], "US$bn", "Q2 FY27 CFO commentary, 26 Aug 2026: US$108.0bn, plus or minus 2%."),
    ("g3gm", "Q3 FY27 gross margin guide", G3["gm"], "%", "Same: 74.0%, plus or minus 50 basis points."),
    ("g3opex", "Q3 FY27 non-GAAP operating expenses guide", G3["opex"], "US$bn", "Same: approximately US$9.0bn."),
    ("portsgw", "PORTS campus, IT load under the guarantees", PORTS_GW, "GW", "Form 8-K, 17 Aug 2026: approximately 4.25 GW of IT load; option on about 3.8 GW more."),
    ("portslo", "Nvidia revenue per generation at PORTS, low", PORTS_REV[0], "US$bn", "Q2 FY27 CFO commentary: about 1.5 million GPUs, or about US$150bn to US$200bn."),
    ("portshi", "Nvidia revenue per generation at PORTS, high", PORTS_REV[1], "US$bn", "Same."),
    ("vertivlo", "Vertiv opportunity per MW, low", VERTIV_PER_GW[0], "US$m", "Vertiv 2026 Investor Conference, 19 May 2026 (management estimate), as in the journal."),
    ("vertivhi", "Vertiv opportunity per MW, high", VERTIV_PER_GW[1], "US$m", "Same."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("edge3", "Edge Computing revenue, Q3 FY27", EDGE_Q3, "US$bn", "MINE. Q2 was US$7.198bn."),
    ("edge4", "Edge Computing revenue, Q4 FY27", EDGE_Q4, "US$bn", "MINE."),
    ("revq4", "Revenue, Q4 FY27", REV_Q4, "US$bn", "MINE. 13% above the Q3 guide; consensus implies about US$126bn."),
    ("omq4", "Non-GAAP operating margin, Q4 FY27", OM_Q4, "%", "MINE. Q3 guide implies 65.7%; Q2 was 66.5%."),
    ("oiq", "Non-GAAP other income a quarter, Q3 and Q4 FY27", OI_Q, "US$bn", "MINE. Q2 was US$0.300bn, Q1 US$0.457bn."),
    ("tax", "Non-GAAP tax rate", TAX, "%", "MINE, within the 16% to 18% guide for FY27; held for FY28 and FY29."),
    ("sh27", "Diluted shares, Q3 and Q4 FY27", SH27_Q3Q4, "bn", "MINE. Q2 was 24.285bn."),
    ("gw28", "Growth in GW of IT load equipped with Nvidia systems, FY28 (base)", G_GW[0], "%", "MINE. The pace of the physical layer: equipment makers' plans, energised but idle halls, on-site power."),
    ("gw29", "Growth in GW equipped, FY29 (base)", G_GW[1], "%", "MINE."),
    ("usd28", "Rise in Nvidia revenue per GW, FY28 (base)", G_USD[0], "%", "MINE. Vera Rubin began production shipments in Q3 FY27 (10-Q)."),
    ("usd29", "Rise in Nvidia revenue per GW, FY29 (base)", G_USD[1], "%", "MINE."),
    ("edge28", "Edge Computing revenue, FY28", EDGE28, "US$bn", "MINE."),
    ("edge29", "Edge Computing revenue, FY29", EDGE29, "US$bn", "MINE."),
    ("om28", "Non-GAAP operating margin, FY28 (base)", OM28, "%", "MINE. Supply commitments rose to US$279bn, mainly memory; memory costs press the margin."),
    ("om29", "Non-GAAP operating margin, FY29 (base)", OM29, "%", "MINE."),
    ("oiyr", "Non-GAAP other income a year, FY28 and FY29", OI_YR, "US$bn", "MINE."),
    ("sh28", "Diluted shares, FY28", SH28, "bn", "MINE. Buybacks net of dilution."),
    ("sh29", "Diluted shares, FY29", SH29, "bn", "MINE."),
    ("mbase", "Multiple on FY29 EPS (base)", M_BASE, "x", "MINE. Today's forward P/E is 16.9x (stockanalysis.com), rounded down."),
]
r = 6
for key, lab, val, unit, src in rows:
    if lab is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY); r += 1; continue
    ws.cell(row=r, column=1, value=lab)
    c = ws.cell(row=r, column=2, value=val)
    mine = key in MINE
    c.font = F_INB if mine else F_IN
    if mine: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else ("#,##0.000" if unit == "bn" else ("#,##0.00" if unit in ("US$", "GW", "US$m") else BN3)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1

# ===================================================================== QUARTERLY
QH = ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26", "Q1 FY27", "Q2 FY27", "Q3 FY27E", "Q4 FY27E"]
ws = sheet("Quarterly", "QUARTERLY HISTORY, Q1 FY25 TO Q2 FY27, THE Q3 FY27 GUIDE AND MY Q4", [50] + [11] * 12)
head(ws, 4, ["US$ billion unless stated"] + QH)
C = [get_column_letter(2 + j) for j in range(12)]   # B..M
label(ws, 5, "Revenue", True)
for j, v in enumerate(Q_REV):
    put(ws, 5, 2 + j, v, BN3)
put(ws, 5, 12, "=" + A["g3rev"], BN3); put(ws, 5, 13, "=" + A["revq4"], BN3)
label(ws, 6, "Data Center")
for j, v in enumerate(Q_DC):
    put(ws, 6, 2 + j, v, BN3)
put(ws, 6, 12, f"=L5-L7", BN3); put(ws, 6, 13, f"=M5-M7", BN3)
label(ws, 7, "Everything else (Edge Computing from FY27)")
for j in range(10):
    put(ws, 7, 2 + j, f"={C[j]}5-{C[j]}6", BN3)
put(ws, 7, 12, "=" + A["edge3"], BN3); put(ws, 7, 13, "=" + A["edge4"], BN3)
label(ws, 8, "Data Center share of revenue")
for j in range(12):
    put(ws, 8, 2 + j, f"={C[j]}6/{C[j]}5", PCT1)
label(ws, 9, "Data Center growth on a year earlier")
for j in range(4, 12):
    put(ws, 9, 2 + j, f"={C[j]}6/{C[j - 4]}6-1", PCT1)
label(ws, 10, "Non-GAAP operating income (FY27 basis)", True)
put(ws, 10, 10, NG_Q27["q1"]["op"], BN3); put(ws, 10, 11, NG_Q27["q2"]["op"], BN3)
put(ws, 10, 12, f"=L5*{A['g3gm']}-{A['g3opex']}", BN3); put(ws, 10, 13, f"=M5*{A['omq4']}", BN3)
label(ws, 11, "Non-GAAP operating margin")
for j in range(8, 12):
    put(ws, 11, 2 + j, f"={C[j]}10/{C[j]}5", PCT1)
label(ws, 12, "Non-GAAP net income")
put(ws, 12, 10, NG_Q27["q1"]["ni"], BN3); put(ws, 12, 11, NG_Q27["q2"]["ni"], BN3)
put(ws, 12, 12, f"=(L10+{A['oiq']})*(1-{A['tax']})", BN3); put(ws, 12, 13, f"=(M10+{A['oiq']})*(1-{A['tax']})", BN3)
label(ws, 13, "Diluted shares, bn")
put(ws, 13, 10, 24.391, BN3); put(ws, 13, 11, SH_Q2, BN3)
put(ws, 13, 12, "=" + A["sh27"], BN3); put(ws, 13, 13, "=" + A["sh27"], BN3)
label(ws, 14, "Non-GAAP diluted EPS, US$ (reported; Q3 and Q4 mine)", True)
put(ws, 14, 10, NG_Q27["q1"]["eps"], USD2); put(ws, 14, 11, NG_Q27["q2"]["eps"], USD2)
put(ws, 14, 12, "=L12/L13", USD2); put(ws, 14, 13, "=M12/M13", USD2)
ws["A16"] = "Checks"; ws["A16"].font = Font(bold=True, color=NAVY)
for rr, lab, f, fmt in [(17, "Data Center share of revenue, Q2 FY27", "=K8", PCT1),
                        (18, "Data Center growth, Q2 FY27 on Q2 FY26", "=K9", PCT1),
                        (19, "Q3 FY27E non-GAAP operating margin implied by the guide", "=L11", PCT1),
                        (20, "Q3 FY27E EPS", "=L14", USD2), (21, "Q4 FY27E EPS", "=M14", USD2)]:
    ws.cell(row=rr, column=1, value=lab); c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
note(ws, 23, ["Source: Nvidia CFO commentaries, Q3 FY25 to Q2 FY27, with comparative columns. Q1 FY27 diluted shares 24.391bn (Q2 commentary).",
              "Q1 and Q2 FY27 non-GAAP include stock-based pay (Nvidia's basis from Q1 FY27). Q3 FY27E uses the guide of 26 August 2026; Q4 FY27E is mine.",
              "Data Center sub-markets, Q2 FY27: Hyperscale US$48.710bn, AI Clouds, Industrial and Enterprise US$40.313bn (Q1 recast: 43.050 and 32.196)."])

# ===================================================================== GIGAWATTS
ws = sheet("Gigawatts", "DATA CENTER REVENUE TRANSLATED INTO GIGAWATTS OF IT LOAD A YEAR", [60, 14, 14, 14, 14, 14])
ws["A3"] = "The yardstick is Nvidia's own: about US$150bn to US$200bn of revenue for about 4.25 GW of IT load at PORTS, ready from 2028 (FY29)."
ws["A3"].font = F_NOTE
label(ws, 5, "Nvidia revenue per GW of IT load, low (US$bn)"); put(ws, 5, 2, f"={A['portslo']}/{A['portsgw']}", BN2)
label(ws, 6, "Nvidia revenue per GW of IT load, high (US$bn)"); put(ws, 6, 2, f"={A['portshi']}/{A['portsgw']}", BN2)
label(ws, 7, "Midpoint, set to FY29 (US$bn per GW)", True); put(ws, 7, 2, "=(B5+B6)/2", BN2, True)
label(ws, 8, "FY28 revenue per GW (midpoint deflated by my FY29 rise)"); put(ws, 8, 2, f"=B7/(1+{A['usd29']})", BN2)
label(ws, 9, "FY27 revenue per GW (and FY26), deflated by my FY28 rise"); put(ws, 9, 2, f"=B8/(1+{A['usd28']})", BN2)
label(ws, 10, "Low end of the PORTS range against its midpoint"); put(ws, 10, 2, "=B5/B7", BN3)
label(ws, 11, "High end against its midpoint"); put(ws, 11, 2, "=B6/B7", BN3)
label(ws, 12, "Nvidia revenue per GW against Vertiv's opportunity per GW, low"); put(ws, 12, 2, f"=B5/({A['vertivhi']})", MULT)
label(ws, 13, "Same, high"); put(ws, 13, 2, f"=B6/({A['vertivlo']})", MULT)
head(ws, 15, ["Year", "Data Center revenue", "US$bn per GW", "GW, central", "GW, low", "GW, high"])
gwrows = [("FY26 actual", f"={DC_H[1]}", "=B9"), ("FY27E mine", "=Financials!D5", "=B9"), ("FY28E mine", "=Financials!E5", "=B8"),
          ("FY28 consensus (revenue less my Edge)", f"={A['consrev28']}-{A['edge28']}", "=B8"), ("FY29E mine", "=Financials!F5", "=B7")]
for i, (lab, dcf, usdf) in enumerate(gwrows):
    rr = 16 + i
    label(ws, rr, lab)
    put(ws, rr, 2, dcf, BN1); put(ws, rr, 3, usdf, BN2)
    put(ws, rr, 4, f"=B{rr}/C{rr}", BN1, True); put(ws, rr, 5, f"=B{rr}/(C{rr}*$B$11)", BN1); put(ws, rr, 6, f"=B{rr}/(C{rr}*$B$10)", BN1)
label(ws, 22, "GW growth consensus FY28 needs, at my FY28 rise in revenue per GW", True); put(ws, 22, 2, "=D19/D17-1", PCT1, True)
label(ws, 23, "GW growth in my FY28 base"); put(ws, 23, 2, "=D18/D17-1", PCT1)
label(ws, 24, "FY27 GW at the undeflated PORTS range, low"); put(ws, 24, 2, "=B17/B6", BN1)
label(ws, 25, "FY27 GW at the undeflated PORTS range, high"); put(ws, 25, 2, "=B17/B5", BN1)
note(ws, 27, ["The PORTS figure is Nvidia's own (CFO commentary, 26 Aug 2026; Form 8-K, 17 Aug 2026). Setting it to FY29 and deflating it for earlier years is my method.",
              "IT load is the power drawn by the computers, before cooling and other losses; the grid connection is larger.",
              "Revenue is booked when systems ship, not when they are switched on, and some systems will refit halls already powered; the GW are a yardstick, not a count."])

# ===================================================================== FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (US$ billion unless stated)", [52, 12, 12, 12, 12, 12])
head(ws, 4, ["", "FY25A", "FY26A", "FY27E*", "FY28E*", "FY29E*"])
fin = [
    (5, "Data Center", [DC_H[0], DC_H[1], "=SUM(Quarterly!J6:M6)", "=D5*(1+Scenarios!B6)*(1+Scenarios!D6)", "=E5*(1+Scenarios!C6)*(1+Scenarios!E6)"], BN1, False),
    (6, "Edge Computing and other", [REV_H[0] - DC_H[0], REV_H[1] - DC_H[1], "=SUM(Quarterly!J7:M7)", "=" + A["edge28"], "=" + A["edge29"]], BN1, False),
    (7, "Revenue", ["=B5+B6", "=C5+C6", "=SUM(Quarterly!J5:M5)", "=E5+E6", "=F5+F6"], BN1, True),
    (8, "Revenue growth", [f"=B7/{FY24_REV}-1", "=C7/B7-1", "=D7/C7-1", "=E7/D7-1", "=F7/E7-1"], PCT1, False),
    (9, "Non-GAAP operating income", [None, None, "=SUM(Quarterly!J10:M10)", f"=E7*Scenarios!F6", f"=F7*Scenarios!G6"], BN1, True),
    (10, "Non-GAAP operating margin", [None, None, "=D9/D7", "=E9/E7", "=F9/F7"], PCT1, False),
    (11, "Other income, net", [None, None, None, "=" + A["oiyr"], "=" + A["oiyr"]], BN2, False),
    (12, "Tax rate", [None, None, None, "=" + A["tax"], "=" + A["tax"]], PCT1, False),
    (13, "Non-GAAP net income", [None, None, "=SUM(Quarterly!J12:M12)", "=(E9+E11)*(1-E12)", "=(F9+F11)*(1-F12)"], BN1, True),
    (14, "Diluted shares, bn", [None, None, None, "=" + A["sh28"], "=" + A["sh29"]], BN3, False),
    (15, "Diluted EPS, US$ (FY25 and FY26 GAAP; then non-GAAP)", [GAAP_EPS_H[0], GAAP_EPS_H[1], "=SUM(Quarterly!J14:M14)", "=E13/E14", "=F13/F14"], USD2, True),
    (16, "EPS growth", [None, "=C15/B15-1", "=D15/C15-1", "=E15/D15-1", "=F15/E15-1"], PCT1, False),
    (17, "P/E at reference price", [None, f"={A['price']}/C15", f"={A['price']}/D15", f"={A['price']}/E15", f"={A['price']}/F15"], MULT, False),
    (18, "Consensus EPS, US$", [None, None, "=" + A["cons27"], "=" + A["cons28"], None], USD2, False),
    (19, "Mine against consensus", [None, None, "=D15/D18-1", "=E15/E18-1", None], PCT1, False),
    (20, "P/E on consensus", [None, None, f"={A['price']}/D18", f"={A['price']}/E18", None], MULT, False),
    (21, "Consensus revenue", [None, None, "=" + A["consrev27"], "=" + A["consrev28"], None], BN1, False),
    (22, "My revenue against consensus", [None, None, "=D7/D21-1", "=E7/E21-1", None], PCT1, False),
]
for rr, lab, vals, fmt, bold in fin:
    label(ws, rr, lab, bold)
    for j, v in enumerate(vals):
        put(ws, rr, 2 + j, v, fmt)
note(ws, 24, [
    "*FY27E sums two reported quarters, the Q3 guide and my Q4 (Quarterly tab). FY28E and FY29E are the base case (Scenarios row 6).",
    f"FY25 and FY26 as reported. Their non-GAAP EPS excluding stock-based pay was US${NG_EPS_OLD_H[0]:.2f} and US${NG_EPS_OLD_H[1]:.2f}; from FY27 Nvidia's non-GAAP includes it.",
    "Consensus from stockanalysis.com (S&P Global data, last updated 26 October 2026); FY28 is the page's 'next year' figure.",
])

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (MULTIPLE OF FY29E EPS)", [12] + [12] * 16)
head(ws, 4, ["Case", "GW FY28", "GW FY29", "US$/GW FY28", "US$/GW FY29", "Op. margin FY28", "Op. margin FY29", "Multiple",
             "Weight", "DC FY28", "DC FY29", "Revenue FY28", "Revenue FY29", "EPS FY28", "EPS FY29", "Value, US$", "vs price"])
for i, s in enumerate(SCEN):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    if s[0] == "Base":
        ins = ["=" + A["gw28"], "=" + A["gw29"], "=" + A["usd28"], "=" + A["usd29"], "=" + A["om28"], "=" + A["om29"], "=" + A["mbase"], s[8]]
    else:
        ins = list(s[1:9])
    fmts = [PCT0, PCT0, PCT0, PCT0, PCT1, PCT1, MULT0, PCT0]
    for j, (v, f) in enumerate(zip(ins, fmts)):
        c = put(ws, rr, 2 + j, v, f)
        if not isinstance(v, str): c.fill = FILL_ASSUME
    put(ws, rr, 10, f"=Financials!$D$5*(1+B{rr})*(1+D{rr})", BN1)
    put(ws, rr, 11, f"=J{rr}*(1+C{rr})*(1+E{rr})", BN1)
    put(ws, rr, 12, f"=J{rr}+{A['edge28']}", BN1)
    put(ws, rr, 13, f"=K{rr}+{A['edge29']}", BN1)
    put(ws, rr, 14, f"=(L{rr}*F{rr}+{A['oiyr']})*(1-{A['tax']})/{A['sh28']}", USD2)
    put(ws, rr, 15, f"=(M{rr}*G{rr}+{A['oiyr']})*(1-{A['tax']})/{A['sh29']}", USD2)
    put(ws, rr, 16, f"=O{rr}*H{rr}", USD0, True)
    put(ws, rr, 17, f"=P{rr}/{A['price']}-1", PCT1)
ws.cell(row=8, column=1, value="Weighted").font = F_B
put(ws, 8, 16, "=SUMPRODUCT(I5:I7,P5:P7)", USD0, True); put(ws, 8, 17, f"=P8/{A['price']}-1", PCT1)
put(ws, 8, 9, "=SUM(I5:I7)", PCT0)
note(ws, 10, ["Bear: power barely grows for Nvidia systems (GW +5%, then flat) and the market pays 11x. Base: GW +20% then +15%, about the pace of the equipment queues.",
              "Bull: consensus-like growth (GW +50% then +30%) and 18x. Yellow cells are my assumptions; the base row links to the Assumptions tab."])

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "SENSITIVITY: FY28 GW GROWTH AGAINST THE MULTIPLE (FY29 GW GROWTH HELD AT THE BASE)", [30, 14, 14, 14])
head(ws, 4, ["FY28 GW growth"] + [f"{m}x" for m in SENS_M])
for j, m in enumerate(SENS_M):
    put(ws, 3, 2 + j, m, MULT0)
for i, g in enumerate(SENS_GW):
    rr = 5 + i
    c = put(ws, rr, 1, g, PCT0); c.alignment = Alignment(horizontal="left")
    for j in range(3):
        col = get_column_letter(2 + j)
        f = (f"={col}$3*((Financials!$D$5*(1+$A{rr})*(1+{A['usd28']})*(1+{A['gw29']})*(1+{A['usd29']})+{A['edge29']})"
             f"*{A['om29']}+{A['oiyr']})*(1-{A['tax']})/{A['sh29']}")
        put(ws, rr, 2 + j, f, USD0)
label(ws, 9, "Cells above the price"); put(ws, 9, 2, f"=COUNTIF(B5:D7,\">\"&{A['price']})", "0")
label(ws, 10, "Cells more than 15% above"); put(ws, 10, 2, f"=COUNTIF(B5:D7,\">\"&{A['price']}*1.15)", "0")
note(ws, 12, ["Row 3 holds the multiples. Every cell uses the base margins, Edge revenue and revenue-per-GW rises."])

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION SUMMARY AND THE CALL", [64, 16, 70])
vals = [
    (4, "Share price", "=" + A["price"], USD2),
    (5, "Market value, US$bn", f"={A['price']}*{A['shares']}", BN1),
    (6, "Net cash, US$bn (cash and debt securities less debt)", f"={A['cash']}-{A['debt']}", BN1),
    (7, "Enterprise value, US$bn", "=B5-B6", BN1),
    (8, "FY29E EPS, base", "=Financials!F15", USD2),
    (9, "Multiple, base", "=" + A["mbase"], MULT0),
    (10, "Base value per share", "=Scenarios!P6", USD2),
    (11, "Base against price", "=B10/B4-1", PCT1),
    (12, "Probability-weighted value", "=Scenarios!P8", USD2),
    (13, "Rule on the base value (long at +15%, short at -25%)", '=IF(B11>=0.15,"LONG",IF(B11<=-0.25,"SHORT","NO CALL"))', None),
    (14, "Call (Tommy Lau, 2 November 2026)", CALL["direction"], None),
    (15, "Target (base rounded to the nearest US$5)", "=MROUND(B10,5)", USD0),
    (16, "FY29 EPS the price needs at the base multiple", "=B4/B9", USD2),
    (17, "FY29 EPS if GW and revenue per GW stop growing in FY29", f"=((Scenarios!J6+{A['edge29']})*{A['om29']}+{A['oiyr']})*(1-{A['tax']})/{A['sh29']}", USD2),
    (18, "P/E on my FY27E / FY28E / FY29E", "=Financials!D17", MULT),
    (19, "", "=Financials!E17", MULT),
    (20, "", "=Financials!F17", MULT),
    (21, "P/E on consensus FY27 / FY28", "=Financials!D20", MULT),
    (22, "", "=Financials!E20", MULT),
    (23, "Below the highest close", f"=B4/{A['hiclose']}-1", PCT1),
    (24, "Change since 31 December 2025", f"=B4/{A['pxdec25']}-1", PCT1),
    (25, "Guarantees, maximum gross exposure, US$bn", GUAR_TOTAL, BN1),
    (26, "Guarantees against net cash", "=B25/B6", MULT),
]
for rr, lab, f, fmt in vals:
    ws.cell(row=rr, column=1, value=lab)
    c = put(ws, rr, 2, f, fmt, rr in (10, 13, 14))
    if rr in (10, 13, 14, 15): c.fill = FILL_KEY
note(ws, 28, [f"Call: {CALL['direction']}, {CALL['conviction']} conviction, target US${CALL['target']:.0f}.",
              f"Wrong if: {WRONG_IF}"])

# ===================================================================== PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com forward P/E, at the 30 October 2026 close)", [26, 16, 14, 70])
head(ws, 4, ["Company", "Ticker", "Forward P/E", "What they make"])
put(ws, 5, 1, "Nvidia").alignment = Alignment(horizontal="left")
ws.cell(row=5, column=2, value="Nasdaq: NVDA"); put(ws, 5, 3, FWD_PE_SA, MULT)
ws.cell(row=5, column=4, value="GPUs, rack-scale systems, NVLink, InfiniBand and Ethernet networking")
for i, (c_, t, p, w) in enumerate(PEERS):
    rr = 6 + i
    ws.cell(row=rr, column=1, value=c_); ws.cell(row=rr, column=2, value=t); put(ws, rr, 3, p, MULT); ws.cell(row=rr, column=4, value=w)
label(ws, 12, "Median of the five peers"); put(ws, 12, 3, "=MEDIAN(C6:C10)", MULT)
note(ws, 14, ["Multiples only; no view on the peers' shares. Micron's multiple reflects peak memory earnings."])

# ===================================================================== COVER
ws = wb["Cover"]
cover = [
    ("Company", "Nvidia Corporation (Nasdaq: NVDA)"),
    ("Note date", DATE_LONG),
    ("Price", f"US${PRICE:.2f}, Nasdaq close {PRICE_DATE}"),
    ("Call", f"{CALL['direction']}, {CALL['conviction']} conviction, target US${CALL['target']:.0f}"),
    ("Base value", "=Valuation!B10"),
    ("Tabs", "Assumptions, Quarterly, Gigawatts, Financials, Scenarios, Sensitivity, Valuation, Peers"),
    ("Colour code", "Blue = input; yellow fill = my assumption; green = link to Assumptions; black = formula"),
    ("Journal", "https://thephysicallayer.fyi/journal/memory-not-maths/ and the pieces on the rack, the network and capacity stages"),
    ("Research", "https://thephysicallayer.fyi/research/"),
    ("Disclaimer", "I hold no position in Nvidia. Personal research, not investment advice."),
]
for i, (k, v) in enumerate(cover):
    ws.cell(row=4 + i, column=1, value=k).font = F_B
    c = ws.cell(row=4 + i, column=2, value=v)
    if k == "Base value": c.number_format = USD2

wb.save(XLSX)
print("saved", XLSX)
