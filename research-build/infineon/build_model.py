"""Infineon Technologies AG (Xetra: IFX) initiation model. Live formulas throughout.
House style follows the Vertiv and Eaton models: navy header rows, blue font for hardcoded inputs, yellow fill on my own
assumptions, green font for links to the Assumptions tab, black for formulas.
Tabs: Cover, Assumptions, Quarters, Model, Scenarios, Sensitivity, Valuation, Peers, Price.
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
EUR2 = '"€"#,##0.00'
EUR0 = '"€"#,##0'
M0 = '#,##0'
M1 = '#,##0.0'
PCT1 = '0.0%'
MULTF = '0.0"x"'
MULT0 = '0"x"'
SUB = f"Tommy Lau | Infineon Technologies AG (Xetra: IFX) | {DATE} | Personal research, not investment advice."

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


def put(ws, ref, v, fmt=None, font=None, fill=None):
    c = ws[ref]; c.value = v
    if fmt: c.number_format = fmt
    if font: c.font = font
    elif isinstance(v, str) and v.startswith("=Assumptions"): c.font = F_LINK
    elif not (isinstance(v, str) and v.startswith("=")) and isinstance(v, (int, float)): c.font = F_IN
    if fill: c.fill = fill
    c.alignment = RIGHT
    return c


def label(ws, ref, text, bold=False):
    c = ws[ref]; c.value = text
    if bold: c.font = F_B


# ===================================================================== COVER (filled last)
cover = sheet("Cover", "INFINEON TECHNOLOGIES AG (XETRA: IFX)  INITIATION MODEL", [44, 24, 100])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [64, 14, 10, 110])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "another tab. Black = formula. Euro million unless stated. Fiscal year ends 30 September.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = set()
AR = "Annual Report 2025"
Q3 = "Q3 FY26 analyst call intro statement and results release, 5 August 2026"
rows = [
    ("MARKET", None, None, None, None),
    ("price", "Reference share price", PRICE, "€", "Xetra close, 30 October 2026. Yahoo Finance IFX.DE history page, read 2 November 2026; matches stockanalysis.com."),
    ("hiclose", "Highest close, 2 and 3 June 2026", HI_CLOSE, "€", "Yahoo Finance. Intraday high €88.83 on 22 June 2026."),
    ("pxdec", "Close, 30 December 2025", PX_DEC25, "€", "Yahoo Finance."),
    ("shares", "Shares outstanding", SHARES, "m", AR + ": 1,305.9m issued, 4.2m own shares after the buyback completed 14 November 2025. stockanalysis.com shows 1.30bn."),
    ("nd_jun", "Net debt, 30 June 2026", NET_DEBT_JUN26, "€m", Q3 + ": gross cash 1,656, financial debt 6,841."),
    ("fcf9m", "Free cash flow, Q1 to Q3 FY26", FCF_9M, "€m", "Intro statements: minus 199, minus 63, plus 599."),
    ("fcf26", "Free cash flow guide, FY26", FCF_GUIDE26, "€m", Q3 + ". Includes the ~€570m paid for the ams OSRAM sensor portfolio on 1 July 2026."),
    ("GROUP HISTORY", None, None, None, None),
    ("rev24", "Revenue, FY24", FY["FY24"][0], "€m", AR + "."),
    ("sr24", "Segment Result, FY24", FY["FY24"][1], "€m", AR + "."),
    ("eps24", "Adjusted EPS, diluted, FY24", FY["FY24"][2], "€", AR + "."),
    ("rev25", "Revenue, FY25", FY["FY25"][0], "€m", AR + "."),
    ("sr25", "Segment Result, FY25", FY["FY25"][1], "€m", AR + "."),
    ("eps25", "Adjusted EPS, diluted, FY25", FY["FY25"][2], "€", AR + "."),
    ("AI DATA CENTRE POWER (INFINEON'S OWN FIGURES)", None, None, None, None),
    ("ai25", "AI data centre power revenue, FY25", AI_FY25, "€m", AR + ": \"over €700 million\", nearly tripled."),
    ("ai26g", "AI data centre power revenue guide, FY26", AI_FY26_GUIDE, "€m", Q3 + ": \"more than 1.6 billion Euros\", up from 1.5bn."),
    ("ai27old", "AI data centre power revenue indication, FY27", AI_FY27_OLD, "€m", Q3 + ": \"2.5 billion Euros plus\", to be revised upwards, \"material\", on 10 November 2026."),
    ("classic", "Non-AI (classic) data centre power revenue, a year", CLASSIC_DC, "€m", Q3 + ": \"around 500 million Euros annually\"."),
    ("content", "Semiconductor content, average, US$ per kW", CONTENT_AVG, "US$", "Q2 FY26 intro statement, 6 May 2026: range US$100 to 250 per kW, average about US$175."),
    ("fx", "US$ per euro", USD_EUR, "", "Infineon's planning rate in the Q4 FY26 outlook."),
    ("GUIDANCE, 5 AUGUST 2026", None, None, None, None),
    ("q4rev", "Q4 FY26 revenue guide", Q4_REV_GUIDE, "€m", Q3 + ": around €4.7bn."),
    ("q4m", "Q4 FY26 Segment Result Margin guide", Q4_M_GUIDE, "%", Q3 + ": around 23%."),
    ("CONSENSUS (STOCKANALYSIS.COM, S&P GLOBAL; UPDATED 21 OCTOBER 2026, READ 2 NOVEMBER 2026)", None, None, None, None),
    ("cons26", "Consensus adjusted EPS, FY26", CONS_EPS26, "€", "Cross-check only."),
    ("cons27", "Consensus adjusted EPS, FY27", CONS_EPS27, "€", "Cross-check only."),
    ("consrev27", "Consensus revenue, FY27", CONS_REV27, "€m", "Cross-check only."),
    ("constp", "Average analyst target", CONS_TP, "€", "24 analysts; low €50, high €124. Cross-check only."),
    ("MY ESTIMATES: Q4 FY26 BY SEGMENT (INFINEON GAVE THE GROUP FIGURE AND THE DIRECTION FOR EACH SEGMENT)", None, None, None, None),
    ("q4atv", "Automotive revenue, Q4 FY26", Q4["ATV"][0], "€m", "MY ESTIMATE. Guide: moderate sequential growth from 1,932."),
    ("q4atvm", "Automotive margin, Q4 FY26", Q4["ATV"][1], "%", "MY ESTIMATE. Q3 18.4%, Q1 22.1%."),
    ("q4gip", "Green Industrial Power revenue, Q4 FY26", Q4["GIP"][0], "€m", "MY ESTIMATE. Guide: significant growth from 447."),
    ("q4gipm", "Green Industrial Power margin, Q4 FY26", Q4["GIP"][1], "%", "MY ESTIMATE. Q3 9.8% called temporary; Q4 FY25 16.3%."),
    ("q4css", "Connected Secure Systems revenue, Q4 FY26", Q4["CSS"][0], "€m", "MY ESTIMATE. Guide: significant growth from 350."),
    ("q4cssm", "Connected Secure Systems margin, Q4 FY26", Q4["CSS"][1], "%", "MY ESTIMATE."),
    ("MY ASSUMPTIONS: FY27 (BASE CASE) AND THE EARNINGS BRIDGE", None, None, None, None),
    ("ai26", "AI data centre power revenue, FY26", AI26, "€m", "MY ESTIMATE. Guide is \"more than 1.6bn\"."),
    ("ai_m", "AI power Segment Result margin", AI_M, "%", "MY ASSUMPTION. Not disclosed. Infineon calls the business margin-accretive; PSS reached 24.9% in Q3 FY26 with AI its main driver."),
    ("g_atv", "Automotive revenue growth, FY27", SCEN[1][1], "%", "MY ASSUMPTION. Inventory replenishment and design wins against a flat car market."),
    ("m_atv", "Automotive margin, FY27", SCEN[1][2], "%", "MY ASSUMPTION. FY26E 19.8%; Q4 FY25 22.4% before the high-voltage refocus."),
    ("ai27", "AI data centre power revenue, FY27, like for like", SCEN[1][3], "€m", "MY ASSUMPTION. Above the 2.5bn+ indication, which Infineon says it will raise materially."),
    ("g_rest", "Everything else: revenue growth, FY27", SCEN[1][5], "%", "MY ASSUMPTION. Industrial, power infrastructure, consumer, IoT; upcycle plus a full year of the ams OSRAM sensors (~€230m a year)."),
    ("m_rest", "Everything else: margin, FY27", SCEN[1][6], "%", "MY ASSUMPTION. Implied 14.9% in FY26E; idle costs falling from ~€650m."),
    ("fin26", "Net financial cost in adjusted earnings, FY26", FIN["FY26"], "€m", "MY ESTIMATE. Financial result minus 56, 68, 63 in Q1 to Q3."),
    ("fin27", "Net financial cost in adjusted earnings, FY27", FIN["FY27"], "€m", "MY ASSUMPTION. Debt repaid in FY26."),
    ("tax", "Tax rate on adjusted pre-tax profit", TAX, "%", "MY ASSUMPTION. Effective rates 24%, 23%, 21% in Q1 to Q3 FY26. With fin 250 it gives €1.38 for FY25 against €1.39 reported."),
    ("pe", "Base multiple, P/E on FY27E adjusted EPS", BASE_PE, "x", "MY ASSUMPTION. Peer median forward P/E 19.2x; power specialists 26 to 28x."),
]
MINE |= {"q4atv", "q4atvm", "q4gip", "q4gipm", "q4css", "q4cssm", "ai26", "ai_m", "g_atv", "m_atv", "ai27", "g_rest", "m_rest",
         "fin26", "fin27", "tax", "pe"}
r = 6
for key, lab, val, unit, src in rows:
    if lab is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY)
        r += 1; continue
    ws.cell(row=r, column=1, value=lab)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else (EUR2 if unit == "€" else (M1 if unit == "m" else ('0.00' if unit == "" else M0))))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# ===================================================================== QUARTERS
ws = sheet("Quarters", "SEGMENTS BY QUARTER, Q3 FY25 TO Q4 FY26E (EURO MILLION)", [40, 12, 12, 12, 12, 12, 13, 13])
ws["A3"] = ("Source: Infineon company presentation, August 2026 (restated for the Power Drivers & Signal ICs transfer from GIP to PSS). "
            "Q4 FY26E is mine, with PSS as the plug to the 23% group guide.")
ws["A3"].font = F_NOTE
head(ws, 5, ["€ million"] + Q_LABELS + ["Q4 FY26E", "FY26E"])
QR = {}
r = 6
for k, nm in [("ATV", "Automotive"), ("GIP", "Green Industrial Power"), ("PSS", "Power & Sensor Systems"), ("CSS", "Connected Secure Systems")]:
    QR[k] = r
    label(ws, f"A{r}", f"{nm}: revenue", True); label(ws, f"A{r+1}", "  Segment Result"); label(ws, f"A{r+2}", "  margin")
    for i in range(5):
        col = get_column_letter(2 + i)
        put(ws, f"{col}{r}", Q_REV[k][i], M0); put(ws, f"{col}{r+1}", Q_SR[k][i], M0)
        put(ws, f"{col}{r+2}", f"={col}{r+1}/{col}{r}", PCT1)
    r += 3
# group rows
GR = r
label(ws, f"A{GR}", "Group revenue (sum of segments)", True); label(ws, f"A{GR+1}", "Group Segment Result", True); label(ws, f"A{GR+2}", "  margin")
label(ws, f"A{GR+3}", "Reported group revenue (check)"); label(ws, f"A{GR+4}", "Reported group Segment Result (check)")
for i in range(6):
    col = get_column_letter(2 + i)
    put(ws, f"{col}{GR}", "=" + "+".join(f"{col}{QR[k]}" for k in QR), M0)
    put(ws, f"{col}{GR+1}", "=" + "+".join(f"{col}{QR[k]+1}" for k in QR), M0)
    put(ws, f"{col}{GR+2}", f"={col}{GR+1}/{col}{GR}", PCT1)
for i in range(5):
    col = get_column_letter(2 + i)
    put(ws, f"{col}{GR+3}", Q_GROUP_REV[i], M0); put(ws, f"{col}{GR+4}", Q_GROUP_SR[i], M0)
# Q4 FY26E column G
put(ws, f"G{QR['ATV']}", L("q4atv"), M0); put(ws, f"G{QR['ATV']+1}", f"=G{QR['ATV']}*{A['q4atvm']}", M0)
put(ws, f"G{QR['GIP']}", L("q4gip"), M0); put(ws, f"G{QR['GIP']+1}", f"=G{QR['GIP']}*{A['q4gipm']}", M0)
put(ws, f"G{QR['CSS']}", L("q4css"), M0); put(ws, f"G{QR['CSS']+1}", f"=G{QR['CSS']}*{A['q4cssm']}", M0)
put(ws, f"G{QR['PSS']}", f"={A['q4rev']}-G{QR['ATV']}-G{QR['GIP']}-G{QR['CSS']}", M0)
put(ws, f"G{QR['PSS']+1}", f"={A['q4rev']}*{A['q4m']}-G{QR['ATV']+1}-G{QR['GIP']+1}-G{QR['CSS']+1}", M0)
for k in QR:
    put(ws, f"G{QR[k]+2}", f"=G{QR[k]+1}/G{QR[k]}", PCT1)
    put(ws, f"H{QR[k]}", f"=SUM(D{QR[k]}:G{QR[k]})", M0); put(ws, f"H{QR[k]+1}", f"=SUM(D{QR[k]+1}:G{QR[k]+1})", M0)
    put(ws, f"H{QR[k]+2}", f"=H{QR[k]+1}/H{QR[k]}", PCT1)
put(ws, f"H{GR}", f"=SUM(D{GR}:G{GR})", M0); put(ws, f"H{GR+1}", f"=SUM(D{GR+1}:G{GR+1})", M0); put(ws, f"H{GR+2}", f"=H{GR+1}/H{GR}", PCT1)
r = GR + 6
label(ws, f"A{r}", "PSS revenue growth, Q3 FY26 on Q3 FY25"); put(ws, f"B{r}", f"=F{QR['PSS']}/B{QR['PSS']}-1", PCT1); PSS_YOY = f"Quarters!B{r}"
label(ws, f"A{r+1}", "Automotive share of FY26E revenue"); put(ws, f"B{r+1}", f"=H{QR['ATV']}/H{GR}", PCT1); ATV_SH = f"Quarters!B{r+1}"
QH = dict(rev=f"Quarters!$H${GR}", sr=f"Quarters!$H${GR+1}", atv=f"Quarters!$H${QR['ATV']}", atvsr=f"Quarters!$H${QR['ATV']+1}")

# ===================================================================== MODEL
ws = sheet("Model", "GROUP MODEL: FY24A TO FY27E, BASE CASE (EURO MILLION)", [52, 13, 13, 13, 13, 70])
head(ws, 4, ["€ million unless stated", "FY24A", "FY25A", "FY26E", "FY27E", "Note"])
M = {}
lines = [
    ("atv", "Automotive revenue", None, None, f"={QH['atv']}", f"=D{{atv}}*(1+{A['g_atv']})", "FY26E: Q1 to Q3 actual plus my Q4."),
    ("ai", "AI data centre power revenue", None, L("ai25"), L("ai26"), L("ai27"), "Infineon's own figures to FY25; mine after."),
    ("rest", "Everything else", None, None, f"=D{{rev}}-D{{atv}}-D{{ai}}", f"=D{{rest}}*(1+{A['g_rest']})", "Industrial, power infrastructure, non-AI PSS, CSS."),
    ("rev", "Group revenue", L("rev24"), L("rev25"), f"={QH['rev']}", "=E{atv}+E{ai}+E{rest}", "FY26 guide: around 16.3bn."),
    ("g", "  growth", None, "=C{rev}/B{rev}-1", "=D{rev}/C{rev}-1", "=E{rev}/D{rev}-1", ""),
    ("aish", "  AI share of revenue", None, "=C{ai}/C{rev}", "=D{ai}/D{rev}", "=E{ai}/E{rev}", ""),
    ("dcsh", "  All data centre power (AI plus ~0.5bn classic), share", None, f"=(C{{ai}}+{A['classic']})/C{{rev}}", f"=(D{{ai}}+{A['classic']})/D{{rev}}", f"=(E{{ai}}+{A['classic']})/E{{rev}}", ""),
    ("sratv", "Segment Result: Automotive", None, None, f"={QH['atvsr']}", f"=E{{atv}}*{A['m_atv']}", ""),
    ("srai", "Segment Result: AI power", None, None, f"=D{{ai}}*{A['ai_m']}", f"=E{{ai}}*{A['ai_m']}", "My margin assumption."),
    ("srrest", "Segment Result: everything else", None, None, f"=D{{sr}}-D{{sratv}}-D{{srai}}", f"=E{{rest}}*{A['m_rest']}", "FY26E is the remainder."),
    ("sr", "Segment Result", L("sr24"), L("sr25"), f"={QH['sr']}", "=E{sratv}+E{srai}+E{srrest}", "FY26 guide: around 20%."),
    ("m", "  Segment Result Margin", "=B{sr}/B{rev}", "=C{sr}/C{rev}", "=D{sr}/D{rev}", "=E{sr}/E{rev}", ""),
    ("fin", "Less net financial cost", None, None, L("fin26"), L("fin27"), "My estimate."),
    ("pbt", "Adjusted pre-tax profit", None, None, "=D{sr}-D{fin}", "=E{sr}-E{fin}", ""),
    ("ni", "Adjusted net income", None, None, f"=D{{pbt}}*(1-{A['tax']})", f"=E{{pbt}}*(1-{A['tax']})", ""),
    ("eps", "Adjusted EPS, diluted (€)", L("eps24"), L("eps25"), f"=D{{ni}}/{A['shares']}", f"=E{{ni}}/{A['shares']}", "FY24A and FY25A reported."),
    ("epsg", "  growth", None, "=C{eps}/B{eps}-1", "=D{eps}/C{eps}-1", "=E{eps}/D{eps}-1", ""),
    ("cons", "Consensus adjusted EPS (€)", None, None, L("cons26"), L("cons27"), "stockanalysis.com."),
    ("vs", "  mine against consensus", None, None, "=D{eps}/D{cons}-1", "=E{eps}/E{cons}-1", ""),
    ("pe", "P/E at the reference price (x)", None, None, f"={A['price']}/D{{eps}}", f"={A['price']}/E{{eps}}", ""),
]
r = 5
for key, *_ in lines:
    M[key] = r; r += 1
for key, lab, b, c, d, e, nt in lines:
    rr = M[key]
    label(ws, f"A{rr}", lab, bold=key in ("rev", "sr", "eps"))
    fmt = PCT1 if key in ("g", "aish", "dcsh", "m", "epsg", "vs") else (EUR2 if key in ("eps", "cons") else (MULTF if key == "pe" else M0))
    for col, v in zip("BCDE", (b, c, d, e)):
        if v is not None:
            put(ws, f"{col}{rr}", v.format(**M) if isinstance(v, str) else v, fmt)
    ws[f"F{rr}"] = nt; ws[f"F{rr}"].font = F_NOTE
for col in "BCDE":
    ws[f"{col}{M['eps']}"].fill = FILL_KEY
r = M["pe"] + 2
label(ws, f"A{r}", "AI share of FY26E revenue growth"); put(ws, f"B{r}", f"=(D{M['ai']}-C{M['ai']})/(D{M['rev']}-C{M['rev']})", PCT1); AI_GROWTH_SH = f"Model!B{r}"
label(ws, f"A{r+1}", "AI share of FY27E Segment Result"); put(ws, f"B{r+1}", f"=E{M['srai']}/E{M['sr']}", PCT1); AI_SR_SH = f"Model!B{r+1}"
label(ws, f"A{r+2}", "FY26E AI revenue as GW of racks at full average content"); put(ws, f"B{r+2}", f"=D{M['ai']}*{A['fx']}/{A['content']}", M1); GW = f"Model!B{r+2}"
label(ws, f"A{r+3}", "EPS from each €1bn of AI revenue (€)"); put(ws, f"B{r+3}", f"=1000*{A['ai_m']}*(1-{A['tax']})/{A['shares']}", EUR2); EPS_AI = f"Model!B{r+3}"
label(ws, f"A{r+4}", "Value per share from each €1bn of AI revenue (€)"); put(ws, f"B{r+4}", f"=B{r+3}*{A['pe']}", EUR2); VAL_AI = f"Model!B{r+4}"
label(ws, f"A{r+5}", "EPS from one point of Automotive margin (€)"); put(ws, f"B{r+5}", f"=E{M['atv']}*0.01*(1-{A['tax']})/{A['shares']}", EUR2); EPS_ATV = f"Model!B{r+5}"
label(ws, f"A{r+6}", "FY25 adjusted EPS from the same bridge (check, €)"); put(ws, f"B{r+6}", f"=({A['sr25']}-{A['fin26']})*(1-{A['tax']})/{A['shares']}", EUR2)
ws[f"C{r+2}"] = "My arithmetic: revenue in US$ divided by Infineon's average content of US$175 per kW."; ws[f"C{r+2}"].font = F_NOTE

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "SCENARIOS: FY27E, TWELVE MONTHS OUT", [12, 11, 11, 12, 11, 11, 11, 13, 13, 11, 9, 13, 11, 10])
ws["A3"] = "Inputs in blue (the base row links to Assumptions). All my assumptions. Value = P/E x FY27E adjusted EPS."
ws["A3"].font = F_NOTE
head(ws, 4, ["Case", "ATV growth", "ATV margin", "AI revenue", "AI margin", "Rest growth", "Rest margin", "Revenue", "Segment Result",
             "Margin", "P/E", "EPS (€)", "Value (€)", "Change"])
SCR = {}
for i, s in enumerate(SCEN):
    rr = 5 + i; SCR[s[0]] = rr
    ws[f"A{rr}"] = s[0]; ws[f"A{rr}"].font = F_B
    keys = ["g_atv", "m_atv", "ai27", "ai_m", "g_rest", "m_rest", "pe"]
    vals = [s[1], s[2], s[3], s[4], s[5], s[6], s[7]]
    for col, k, v in zip("BCDEFGK", keys, vals):
        fmt = PCT1 if k in ("g_atv", "m_atv", "ai_m", "g_rest", "m_rest") else (M0 if k == "ai27" else MULT0)
        if s[0] == "Base":
            put(ws, f"{col}{rr}", L(k), fmt)
        else:
            put(ws, f"{col}{rr}", v, fmt, font=F_INB, fill=FILL_ASSUME)
    atv = f"{QH['atv']}*(1+B{rr})"
    rest = f"(Model!$D${M['rest']})*(1+F{rr})"
    put(ws, f"H{rr}", f"={atv}+D{rr}+{rest}", M0)
    put(ws, f"I{rr}", f"={atv}*C{rr}+D{rr}*E{rr}+{rest}*G{rr}", M0)
    put(ws, f"J{rr}", f"=I{rr}/H{rr}", PCT1)
    put(ws, f"L{rr}", f"=(I{rr}-{A['fin27']})*(1-{A['tax']})/{A['shares']}", EUR2)
    put(ws, f"M{rr}", f"=K{rr}*L{rr}", EUR2)
    put(ws, f"N{rr}", f"=M{rr}/{A['price']}-1", PCT1)
ws["A9"] = "Probabilities"; ws["A9"].font = F_B
for i, (s, p) in enumerate(zip(SCEN, [0.25, 0.5, 0.25])):
    ws.cell(row=9, column=2 + i, value=s[0])
    put(ws, f"{get_column_letter(2 + i)}10", p, PCT1, font=F_INB, fill=FILL_ASSUME)
label(ws, "A11", "Weighted value (€)", True); put(ws, "E11", "=B10*M5+C10*M6+D10*M7", EUR2); put(ws, "F11", f"=E11/{A['price']}-1", PCT1)
label(ws, "A12", "Base row against Model (check, should be 0)"); put(ws, "E12", f"=L6-Model!E{M['eps']}", '0.000000')

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "SENSITIVITY: VALUE PER SHARE, FY27E AI REVENUE AGAINST THE P/E", [34, 13, 13, 13])
ws["A3"] = "All else as the base case. Rows: FY27 AI data centre power revenue, like for like. Columns: P/E on FY27E adjusted EPS."
ws["A3"].font = F_NOTE
head(ws, 4, ["AI revenue (€m) \\ P/E"] + [f"{p}x" for p in SENS_PE])
for j, p in enumerate(SENS_PE):
    put(ws, f"{get_column_letter(2 + j)}4", p, MULT0, font=Font(bold=True, color="FFFFFF"), fill=FILL_HDR)
for i, a in enumerate(SENS_AI):
    rr = 5 + i
    put(ws, f"A{rr}", a, M0, font=F_INB)
    for j in range(3):
        col = get_column_letter(2 + j)
        sr = f"(Model!$E${M['sratv']}+Model!$E${M['srrest']}+$A{rr}*{A['ai_m']})"
        put(ws, f"{col}{rr}", f"={col}$4*({sr}-{A['fin27']})*(1-{A['tax']})/{A['shares']}", EUR2)
label(ws, "A9", "Cells above the price"); put(ws, "B9", f"=COUNTIF(B5:D7,\">\"&{A['price']})", M0)
label(ws, "A10", "Cells 15% or more above the price"); put(ws, "B10", f"=COUNTIF(B5:D7,\">=\"&{A['price']}*1.15)", M0)

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION: P/E ON FY27E ADJUSTED EPS", [60, 16, 80])
head(ws, 4, ["Item", "Value", "Note"])
V = [
    ("FY27E adjusted EPS, base (€)", f"=Model!E{M['eps']}", EUR2, ""),
    ("P/E, base (x)", L("pe"), MULT0, "My assumption."),
    ("Base value (€)", "=B5*B6", EUR2, ""),
    ("Reference price (€)", L("price"), EUR2, "Xetra close, 30 October 2026."),
    ("Base value against the price", "=B7/B8-1", PCT1, ""),
    ("Band (LONG at +15% or more; SHORT at -25% or less; else NO CALL)", '=IF(B9>=0.15,"LONG",IF(B9<=-0.25,"SHORT","NO CALL"))', None, ""),
    ("Weighted value, 25/50/25 (€)", "=Scenarios!E11", EUR2, ""),
    ("Market value (€bn)", f"={A['price']}*{A['shares']}/1000", '0.00', ""),
    ("Net debt, 30 September 2026, my estimate (€m)", f"={A['nd_jun']}-({A['fcf26']}-{A['fcf9m']})", M0, "June net debt less the Q4 free cash flow implied by the FY26 guide."),
    ("Enterprise value (€bn)", "=B12+B13/1000", '0.00', ""),
    ("EV / FY27E Segment Result (x)", f"=B14*1000/Model!E{M['sr']}", MULTF, ""),
    ("P/E on FY26 consensus (x)", f"={A['price']}/{A['cons26']}", MULTF, ""),
    ("P/E on FY27 consensus (x)", f"={A['price']}/{A['cons27']}", MULTF, ""),
    ("P/E on my FY27E (x)", f"={A['price']}/Model!E{M['eps']}", MULTF, ""),
    ("Highest close on FY27 consensus (x)", f"={A['hiclose']}/{A['cons27']}", MULTF, ""),
    ("Price against the highest close", f"={A['price']}/{A['hiclose']}-1", PCT1, ""),
    ("Price against 30 December 2025", f"={A['price']}/{A['pxdec']}-1", PCT1, ""),
    ("FY27 AI revenue implied by the price at the base P/E (€m)", f"=(({A['price']}/{A['pe']})*{A['shares']}/(1-{A['tax']})+{A['fin27']}-Model!E{M['sratv']}-Model!E{M['srrest']})/{A['ai_m']}", M0, "Other blocks as base."),
    ("Like-for-like FY27 AI revenue that lifts the base to +15% (€m)", f"={A['ai27']}+({A['price']}*1.15-B7)/{VAL_AI}*1000", M0, ""),
    ("Price below which the base is 15% above (€)", "=B7/1.15", EUR2, ""),
    ("Price above which the base is 25% below (€)", "=B7/0.75", EUR2, ""),
    ("Consensus FY27 EPS at the base P/E (€)", f"={A['cons27']}*{A['pe']}", EUR2, ""),
    ("Average analyst target against the price", f"={A['constp']}/{A['price']}-1", PCT1, ""),
]
for i, (lab, f, fmt, nt) in enumerate(V):
    rr = 5 + i
    ws[f"A{rr}"] = lab
    put(ws, f"B{rr}", f, fmt)
    ws[f"C{rr}"] = nt; ws[f"C{rr}"].font = F_NOTE
ws["B7"].fill = FILL_KEY

# ===================================================================== PEERS
ws = sheet("Peers", "PEERS: FORWARD P/E AND TRAILING EV/EBIT", [22, 14, 13, 13, 70])
ws["A3"] = "stockanalysis.com (S&P Global data), read 2 November 2026. Used only to set the range; no view on the peers' shares."
ws["A3"].font = F_NOTE
head(ws, 4, ["Company", "Ticker", "Forward P/E", "EV/EBIT", "What they make"])
for i, p in enumerate(PEERS):
    rr = 5 + i
    ws[f"A{rr}"] = p[0]; ws[f"B{rr}"] = p[1]
    put(ws, f"C{rr}", p[2], MULTF); put(ws, f"D{rr}", p[3], MULTF); ws[f"E{rr}"] = p[4]
last = 4 + len(PEERS)
label(ws, f"A{last + 2}", "Median excluding Infineon", True)
put(ws, f"C{last + 2}", f"=MEDIAN(C6:C{last})", MULTF); put(ws, f"D{last + 2}", f"=MEDIAN(D6:D{last})", MULTF)
PEER_MED = f"Peers!C{last + 2}"

# ===================================================================== PRICE
ws = sheet("Price", "SHARE PRICE, MONTH-END CLOSE (€)", [16, 12])
ws["A3"] = "Yahoo Finance IFX.DE, not adjusted for dividends, read 2 November 2026. Last point is the close on 30 October 2026."
ws["A3"].font = F_NOTE
head(ws, 4, ["Month", "Close"])
for i, (l, p) in enumerate(zip(PX_LABELS, PX)):
    ws[f"A{5 + i}"] = l; put(ws, f"B{5 + i}", p, EUR2)

# ===================================================================== COVER
ws = cover
ws["A3"] = (("Draft initiation model. The direction is a draft view; the final call is Tommy Lau's. " if CALL["draft"] else
             "Initiation model. The call is Tommy Lau's. ") + f"Read with the note {DATE}_{COMPANY}_Initiation.pdf.")
ws["A3"].font = F_NOTE
head(ws, 4, ["Item", "Value", "Note"])
cv = [
    ("Band from the base value", "=Valuation!B10", None, "LONG at 15% or more above the price; SHORT at 25% or more below."),
    ("Draft view" if CALL["draft"] else "Call", CALL["banner"], None, "Driven by CALL in data.py." if CALL["draft"] else "Tommy Lau's call."),
    ("Reference price (€)", L("price"), EUR2, "Xetra close, 30 October 2026."),
    ("Base value (€)", "=Valuation!B7", EUR2, "21x FY27E adjusted EPS."),
    ("Base against the price", "=Valuation!B9", PCT1, ""),
    ("Bear / base / bull value (€)", '=TEXT(Scenarios!M5,"0.0")&" / "&TEXT(Scenarios!M6,"0.0")&" / "&TEXT(Scenarios!M7,"0.0")', None, ""),
    ("Weighted value (€)", "=Scenarios!E11", EUR2, ""),
    ("FY27E adjusted EPS, mine against consensus (€)", f'=TEXT(Model!E{M["eps"]},"0.00")&" against "&TEXT({A["cons27"]},"0.00")', None, ""),
    ("AI share of FY26E revenue", f"=Model!D{M['aish']}", PCT1, "Infineon's AI figure is purely AI; ~0.5bn of classic data centre power is extra."),
    ("Automotive share of FY26E revenue", "=" + ATV_SH, PCT1, ""),
    ("AI share of FY26E revenue growth", "=" + AI_GROWTH_SH, PCT1, ""),
    ("AI share of FY27E Segment Result", "=" + AI_SR_SH, PCT1, ""),
    ("Next results", "10 November 2026", None, "2026 Fiscal Fourth Quarter Results; FY27 outlook in the new three-division setup (Infineon investor page)."),
]
for i, (lab, f, fmt, nt) in enumerate(cv):
    rr = 5 + i
    ws[f"A{rr}"] = lab
    c = put(ws, f"B{rr}", f, fmt)
    ws[f"C{rr}"] = nt; ws[f"C{rr}"].font = F_NOTE
ws["B6"].font = Font(bold=True, color="C00000")

wb.save(XLSX)
print("saved", XLSX)
