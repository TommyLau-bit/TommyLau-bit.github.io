"""The Williams Companies (NYSE: WMB) initiation model. Power Innovation build, Adjusted EBITDA to 2028E, cash and net
debt roll, sum-of-the-parts EV/EBITDA valuation, scenarios, sensitivity, dividend cross-check, peers.
Live formulas throughout. Blue = hardcoded input, yellow fill = my own assumption, green = link, black = formula.
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
USD2 = '"US$"#,##0.00'; M0 = '#,##0'; M1 = '#,##0.0'; M3 = '0.000'; PCT1 = '0.0%'; PCT0 = '0%'; MULTF = '0.0"x"'
SUB = f"Tommy Lau | The Williams Companies, Inc. (NYSE: WMB) | {DATE} | Personal research, not investment advice."

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
    elif isinstance(v, str) and v.startswith("=") and "!" in v: c.font = F_LINK
    if fill: c.fill = fill
    c.alignment = RIGHT
    return c


# =====================================================================  COVER (filled last)
ws = sheet("Cover", "THE WILLIAMS COMPANIES, INC. (NYSE: WMB)  INITIATION MODEL", [44, 26, 100])

# =====================================================================  ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [64, 14, 10, 110])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to another "
            "tab. Black = formula. US$ million unless stated. Year end 31 December.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}; MINE = set()
Q2R = "Q2 2026 earnings release, Form 8-K Ex. 99.1, 3 August 2026"
Q2Q = "Form 10-Q, quarter to 30 June 2026, filed 3 August 2026"
rows = [
    ("MARKET AND BALANCE SHEET", None, None, None, None),
    ("price", "Reference share price", PRICE, "US$", "NYSE close, 30 October 2026. Nasdaq.com historical data, retrieved 2 November 2026; matches stockanalysis.com."),
    ("hiclose", "Highest close, 19 May 2026", HI_CLOSE, "US$", "Nasdaq.com historical data. Intraday high US$80.075 on 20 May 2026."),
    ("pxdec", "Close, 31 December 2025", PX_DEC25, "US$", "Nasdaq.com historical data."),
    ("sh_jul", "Shares outstanding, 30 July 2026", SHARES_JUL, "m", Q2Q + ", cover page: 1,223,167,472."),
    ("sh_mom", "Shares issued to the Momentum sellers", SHARES_MOM, "m", "Prospectus supplement (424B2), 3 September 2026: 26,874,496 shares issued as partial consideration."),
    ("cash", "Cash, 30 June 2026", CASH_JUN, "US$m", Q2R + ", balance sheet."),
    ("debt", "Debt, 30 June 2026", DEBT_JUN, "US$m", Q2R + ": commercial paper 475 + long-term debt due within one year 2,197 + long-term debt 28,121."),
    ("nci_book", "Noncontrolling interests, book, 30 June 2026", NCI_BOOK, "US$m", Q2R + ". Before the Blackstone joint venture."),
    ("nci_inc", "Income to existing noncontrolling interests, run rate", NCI_INC_RUN, "US$m", "MY ESTIMATE. First half 2026: 96 (Q2 release), before the joint venture."),
    ("nci_pe", "Multiple on that income to value existing NCI", NCI_PE, "x", "MY ASSUMPTION. Book value (2,178) understates it."),
    ("bx_total", "Blackstone committed capital for 49% of five projects", BX_TOTAL, "US$m", "Form 8-K, 13 July 2026, Ex. 99.1: US$4.4bn = 49% of expected growth capex plus ~US$0.9bn. Target return 6.35%; excess distributions cut its balance; Williams' buyout right years 7 to 14 at that balance."),
    ("bx_jul", "Blackstone capital received, July 2026", BX_JUL, "US$m", Q2Q + ", Note 11: about US$3.75bn; the rest through early 2027."),
    ("bx_q4", "Blackstone capital received, Q4 2026", BX_Q4, "US$m", "MY ESTIMATE."),
    ("mom_cash", "Momentum: cash and debt consideration", 3500.0, "US$m", Q2R + ": up to US$5.5bn, about US$3.5bn cash and debt and about US$2bn of Williams shares. Closed 3 September 2026."),
    ("GUIDANCE AND HISTORY (WILLIAMS RELEASES)", None, None, None, None),
    ("eb24", "Adjusted EBITDA, 2024", EBITDA["2024A"], "US$m", "Q4 2025 earnings release, 10 February 2026."),
    ("eb25", "Adjusted EBITDA, 2025", EBITDA["2025A"], "US$m", "Q4 2025 earnings release; Q2 2026 release reconciliation."),
    ("g26", "Adjusted EBITDA guide, 2026 midpoint", G26["mid"], "US$m", Q2R + ": US$8.3bn to US$8.5bn, including Momentum from closing."),
    ("g26lo", "Adjusted EBITDA guide, 2026 low", G26["lo"], "US$m", Q2R + "."),
    ("affo26", "AFFO guide, 2026 midpoint", G26["affo"], "US$m", Q2R + ", guidance reconciliation: US$5.15 a share; coverage 2.47x."),
    ("affo_h1", "AFFO, first half 2026", H1_26["affo"], "US$m", Q2R + "."),
    ("div26", "Common dividends paid, 2026 guide", G26["div_paid"], "US$m", Q2R + ", guidance reconciliation."),
    ("div_h1", "Common dividends paid, first half 2026", H1_26["div"], "US$m", Q2R + "."),
    ("gcx26", "Growth capex guide, 2026 midpoint", (G26["gcx_lo"] + G26["gcx_hi"]) / 2, "US$m", Q2R + ": US$7.3bn to US$7.9bn, excluding reimbursable long-lead power equipment."),
    ("cx_h1", "Capital investments, first half 2026", 3284.0, "US$m", Q2R + ", excluding US$170m of reimbursable long-lead power equipment."),
    ("mcx26", "Maintenance capex guide, 2026 midpoint", G26["mcx"], "US$m", "Form 8-K, 13 July 2026: US$850m to US$950m."),
    ("dps26", "Dividend per share, 2026 annualised", DPS["2026G"], "US$", "Q4 2025 earnings release: raised 5% to US$2.10."),
    ("lt_target", "Williams' Adjusted EBITDA growth target, 2025 to 2030", LT_TARGET, "%", "Q2 2026 call (third-party transcript): '11-plus percent compound annual growth through 2030'."),
    ("cons_tp", "Average analyst target", CONS_TP, "US$", "stockanalysis.com (S&P Global), 25 analysts, low US$69, high US$103, retrieved 2 November 2026. Cross-check only."),
    ("POWER INNOVATION", None, None, None, None),
    ("capex_pi", "Five projects' capital, including capitalised interest", CAPEX_PI, "US$m", "US$9.6bn on Williams' Q2 slides as cited by an analyst on the 4 Aug 2026 call (third-party transcript), the CFO attributing most of the gap to capitalised interest; growth capex ex capitalised interest about US$8.98bn (US$4.4bn / 49%, 8-K 13 Jul 2026). Not used in the valuation."),
    ("pi_run", "Five projects' run-rate Adjusted EBITDA, 2029", PI_RUN, "US$m", "MY ESTIMATE. About 5x the ~US$9.0bn growth capex: Williams expects Neo at 'an attractive 5x build multiple' (Q1 2026 call). The Blackstone buyout illustration (2.3x, 1.6x, 0.8x, 0.0x in years 8 to 11) fits roughly US$1.7bn a year of project cash, my arithmetic."),
    ("pi_remain", "Power capital still to spend after 2027", PI_REMAIN, "US$m", "MY ESTIMATE. Socrates the Younger and Neo enter service in 2H 2028."),
    ("pjm", "PJM capacity price, 2027/28, RTO", PJM_CAP, "US$/MW-day", "PJM 2027/2028 Base Residual Auction report, December 2025: cleared at the cap."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("mom27", "Momentum Adjusted EBITDA, 2027", MOM27, "US$m", "Derived: US$5.5bn / 8.5x projected 2027 EBITDA (Q2 release)."),
    ("mom_m26", "Momentum months in 2026", 4, "months", "Closed 3 September 2026."),
    ("mom28", "Momentum Adjusted EBITDA, 2028", MOM28, "US$m", "MY ESTIMATE. Shelby Trough Connector due 2Q 2028."),
    ("core_g27", "Pipes, gathering and other: growth, 2027", CORE_G27, "%", "MY ASSUMPTION. 2025: +9.5% for the whole company; 2026 core about +4.8% on my split."),
    ("core_g28", "Pipes, gathering and other: growth, 2028", CORE_G28, "%", "MY ASSUMPTION. Southeast Supply Enhancement (1,597 Mdth/d) due as early as 3Q 2027."),
    ("int27", "Interest expense, 2027", INT27, "US$m", "MY ESTIMATE. 2026 guide 1,535."),
    ("int28", "Interest expense, 2028", INT28, "US$m", "MY ESTIMATE."),
    ("nci_d", "Distributions to existing NCI, 2027 and 2028", 335.0, "US$m", "MY ESTIMATE. 2026 guide 328."),
    ("bx_share", "Blackstone share of power cash", 0.49, "%", "Form 8-K, 13 July 2026: distributions align with 51% / 49%."),
    ("other27", "Other AFFO items, 2027", OTHER27, "US$m", "MY ESTIMATE. About 160 in the 2026 guide."),
    ("other28", "Other AFFO items, 2028", OTHER28, "US$m", "MY ESTIMATE."),
    ("dps27", "Dividend per share, 2027", DPS27, "US$", "MY ASSUMPTION. +5%, the 2025 and 2026 pace."),
    ("dps28", "Dividend per share, 2028", DPS28, "US$", "MY ASSUMPTION."),
    ("gcx27", "Growth capex, 2027", GCX27, "US$m", "MY ESTIMATE. Management called 2027 'a bit of a high watermark' for capital (Q2 call)."),
    ("mcx27", "Maintenance capex, 2027", MCX27, "US$m", "MY ESTIMATE."),
    ("core_mult", "Pipes and gathering: EV / 2028E Adjusted EBITDA", CORE_MULT, "x", "MY ASSUMPTION. Williams' year-end EV over its own Adjusted EBITDA was about 13.4x in both 2024 and 2025 (my arithmetic on stockanalysis.com EV)."),
    ("pi_mult", "Power Innovation: EV / run-rate EBITDA", PI_MULT, "x", "MY ASSUMPTION. An 11.6-year level stream at 8% is worth 7.4x; a little more for extensions."),
    ("ke", "Cost of equity, dividend cross-check", KE, "%", "MY ASSUMPTION."),
    ("dg1", "Dividend growth, years 1 to 10", DG1, "%", "MY ASSUMPTION. Between the recent 5% and my ~10% AFFO per share growth to 2028."),
    ("dg2", "Dividend growth after year 10", DG2, "%", "MY ASSUMPTION."),
]
MINE = {"nci_inc", "nci_pe", "bx_q4", "pi_run", "pi_remain", "mom28", "core_g27", "core_g28", "int27", "int28", "nci_d",
        "other27", "other28", "dps27", "dps28", "gcx27", "mcx27", "core_mult", "pi_mult", "ke", "dg1", "dg2"}
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY); r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    c.font = F_INB if key in MINE else F_IN
    if key in MINE: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULTF if unit == "x" else (M1 if unit in ("m",) else (USD2 if unit in ("US$", "US$/MW-day") else M0)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1
L = lambda k: "=" + A[k]

# =====================================================================  POWER
ws = sheet("Power", "POWER INNOVATION: FIVE PROJECTS IN THE BLACKSTONE JOINT VENTURE", [24, 11, 11, 12, 12, 12, 12, 12, 12, 30])
head(ws, 4, ["Project", "Installed MW", "Contract, years", "In service 2026", "In service 2027", "In service 2028",
             "EBITDA 2026", "EBITDA 2027", "EBITDA 2028", "Williams' in-service window"])
for i, p in enumerate(PROJ):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=p[0]).font = F_B
    put(ws, f"B{rr}", p[1], M0, F_IN); put(ws, f"C{rr}", p[2], M1, F_IN)
    for j in range(3):
        put(ws, f"{'DEF'[j]}{rr}", p[3][j], PCT0, F_INB, FILL_ASSUME)
    for j in range(3):
        put(ws, f"{'GHI'[j]}{rr}", f"=$B{rr}*$B$13*{'DEF'[j]}{rr}", M0)
    ws.cell(row=rr, column=10, value=p[5])
ws["A10"] = "Total"; ws["A10"].font = F_B
put(ws, "B10", "=SUM(B5:B9)", M0, F_B)
for col in "GHI":
    put(ws, f"{col}10", f"=SUM({col}5:{col}9)", M0, F_B, FILL_KEY)
ws["A12"] = "Run-rate EBITDA, five projects (US$m)"; put(ws, "B12", L("pi_run"), M0)
ws["A13"] = "EBITDA per installed MW-year (US$m)"; put(ws, "B13", "=B12/B10", M3)
ws["A14"] = "EBITDA per installed MW-day (US$)"; put(ws, "B14", "=B13*1000000/365", M0)
ws["A15"] = "PJM capacity price, 2027/28 (US$/MW-day)"; put(ws, "B15", L("pjm"), USD2)
ws["A16"] = "Ratio (rough comparison)"; put(ws, "B16", "=B14/B15", MULTF)
ws["A17"] = "MW-weighted contract term (years)"; put(ws, "B17", "=SUMPRODUCT(B5:B9,C5:C9)/B10", '0.00')
ws["A18"] = "Build multiple on growth capex ex interest"; put(ws, "B18", f"=4400/0.49/B12", MULTF)
ws["A19"] = "Build multiple incl. capitalised interest"; put(ws, "B19", f"={A['capex_pi']}/B12", MULTF)
ws["A20"] = "Unlevered IRR at 5x over the term, no residual"; put(ws, "B20", "=RATE(B17,1,-5)", PCT1)
ws["A21"] = "PV of the term at 8%, x run-rate EBITDA"; put(ws, "B21", "=PV(0.08,B17,-1)", MULTF)
note(ws, 23, [
    "Sources: Form 10-Q for the quarter to 30 June 2026 (MW, terms, windows; Socrates South in service late July 2026, North Q4 2026);",
    "Form 10-K 2025: Socrates 'a combined 400 megawatts of onsite power generation capacity to the customer'; Form 10-Q Q1 2026 onwards: 556 MW expected.",
    "In-service shares of each year are my estimates inside Williams' windows. EBITDA by project is my estimate at one rate per installed MW.",
    "The PJM ratio is rough: a capacity price pays a grid plant for being available only, and that plant also earns energy revenue.",
])

# =====================================================================  EBITDA
ws = sheet("EBITDA", "ADJUSTED EBITDA BY SOURCE, 2024A TO 2028E (US$ MILLION)", [50, 13, 13, 13, 13, 13])
head(ws, 4, ["US$ million", "2024A", "2025A", "2026G*", "2027E", "2028E"])
labels = ["Pipes, gathering, marketing, other", "  growth", "Momentum (from 3 September 2026)", "Power Innovation",
          "ADJUSTED EBITDA", "  growth", "Williams' 11% a year path from 2025"]
for i, lab in enumerate(labels):
    ws.cell(row=5 + i, column=1, value=lab).font = F_B if lab.isupper() else Font()
put(ws, "B5", L("eb24"), M0); put(ws, "C5", L("eb25"), M0)
put(ws, "D7", f"={A['mom27']}*{A['mom_m26']}/12", M0)
put(ws, "D8", "=Power!G10", M0)
put(ws, "D5", f"={A['g26']}-D7-D8", M0)
put(ws, "E5", f"=D5*(1+{A['core_g27']})", M0); put(ws, "F5", f"=E5*(1+{A['core_g28']})", M0)
put(ws, "E7", L("mom27"), M0); put(ws, "F7", L("mom28"), M0)
put(ws, "E8", "=Power!H10", M0); put(ws, "F8", "=Power!I10", M0)
for col in "BC":
    put(ws, f"{col}7", 0, M0, F_IN); put(ws, f"{col}8", 0, M0, F_IN)
for col in "BCDEF":
    put(ws, f"{col}9", f"={col}5+{col}7+{col}8", M0, F_B, FILL_KEY)
for col, prev in [("C", "B"), ("D", "C"), ("E", "D"), ("F", "E")]:
    put(ws, f"{col}10", f"={col}9/{prev}9-1", PCT1)
for col, prev in [("D", "C"), ("E", "D"), ("F", "E")]:
    put(ws, f"{col}6", f"={col}5/{prev}5-1", PCT1)
for k, col in enumerate("DEF", 1):
    put(ws, f"{col}11", f"=$C$9*(1+{A['lt_target']})^{k}", M0)
ws["A13"] = "2030E, signed projects only (my estimate)"; put(ws, "B13", f"=F5*1.05^2+760+{A['pi_run']}", M0)
ws["A14"] = "2025 to 2030E growth a year"; put(ws, "B14", "=(B13/C9)^(1/5)-1", PCT1)
ws["A15"] = "Williams' 11% path, 2030"; put(ws, "B15", f"=C9*(1+{A['lt_target']})^5", M0)
note(ws, 17, [
    "*2026 is Williams' guide midpoint (3 August 2026); its split into the three sources is mine. 2027E and 2028E are my estimates.",
    "2024A and 2025A as reported; Power Innovation and Momentum contributed nothing before 2026. 2030E assumes 5% a year for the pipes after 2028 and Momentum at 760.",
])

# =====================================================================  CASH
ws = sheet("Cash", "AFFO, DIVIDENDS AND NET DEBT (US$ MILLION)", [56, 13, 13, 13, 13])
head(ws, 4, ["US$ million", "2H 2026", "2026G", "2027E", "2028E"])
lab = ["Adjusted EBITDA", "Interest expense", "Distributions to noncontrolling interests, incl. Blackstone", "Other",
       "AFFO", "Diluted shares, m", "AFFO per share, US$", "Dividend per share, US$", "Dividends paid",
       "Coverage (AFFO / dividends)", "Growth and maintenance capex", "Momentum cash and debt", "Blackstone capital received",
       "Net debt at period end", "Net debt / Adjusted EBITDA"]
for i, t in enumerate(lab):
    ws.cell(row=5 + i, column=1, value=t).font = F_B if t in ("AFFO", "Net debt at period end") else Font()
put(ws, "C5", "=EBITDA!D9", M0); put(ws, "D5", "=EBITDA!E9", M0); put(ws, "E5", "=EBITDA!F9", M0)
put(ws, "D6", "=-" + A["int27"], M0); put(ws, "E6", "=-" + A["int28"], M0)
put(ws, "D7", f"=-({A['nci_d']}+{A['bx_share']}*EBITDA!E8)", M0); put(ws, "E7", f"=-({A['nci_d']}+{A['bx_share']}*EBITDA!F8)", M0)
put(ws, "D8", "=-" + A["other27"], M0); put(ws, "E8", "=-" + A["other28"], M0)
put(ws, "C9", L("affo26"), M0); put(ws, "B9", f"={A['affo26']}-{A['affo_h1']}", M0)
put(ws, "D9", "=SUM(D5:D8)", M0); put(ws, "E9", "=SUM(E5:E8)", M0)
for col in "CDE":
    put(ws, f"{col}10", f"={A['sh_jul']}+{A['sh_mom']}", M1)
put(ws, "C10", 1237, M1, F_IN)
for col in "CDE":
    put(ws, f"{col}11", f"={col}9/{col}10", USD2)
put(ws, "C12", L("dps26"), USD2); put(ws, "D12", L("dps27"), USD2); put(ws, "E12", L("dps28"), USD2)
put(ws, "B13", f"={A['div26']}-{A['div_h1']}", M0); put(ws, "C13", L("div26"), M0)
put(ws, "D13", "=D12*D10", M0); put(ws, "E13", "=E12*E10", M0)
for col in "CDE":
    put(ws, f"{col}14", f"={col}9/{col}13", '0.00"x"')
put(ws, "B15", f"={A['gcx26']}-{A['cx_h1']}+{A['mcx26']}/2", M0); put(ws, "D15", f"={A['gcx27']}+{A['mcx27']}", M0)
put(ws, "B16", L("mom_cash"), M0)
put(ws, "B17", f"={A['bx_jul']}+{A['bx_q4']}", M0); put(ws, "D17", f"={A['bx_total']}-B17", M0)
put(ws, "B18", f"={A['debt']}-{A['cash']}+B15+B16-B17-B9+B13", M0, F_B, FILL_KEY)
put(ws, "D18", "=B18+D15-D17-D9+D13", M0, F_B, FILL_KEY)
put(ws, "B19", f"=B18/(EBITDA!D9+{A['mom27']}*8/12)", '0.00"x"'); put(ws, "D19", "=D18/EBITDA!E9", '0.00"x"')
note(ws, 21, [
    "Column B rolls net debt from 30 June 2026 (Q2 release) to 31 December 2026: second-half capex at the guide midpoint, Momentum, Blackstone capital,",
    "and the second half of Williams' 2026 AFFO and dividend guides. The 2026 ratio adds eight months of Momentum, as Williams does. 2027 and 2028 are mine.",
    "Williams' own leverage metric treats the Blackstone capital as equity and excludes reimbursable long-lead equipment; it guided about 3.75x for 2026.",
])

# =====================================================================  VALUATION
ws = sheet("Valuation", "VALUATION: SUM OF THE PARTS, TWELVE MONTHS OUT", [66, 16, 70])
head(ws, 4, ["Item", "Value", "Working / note"])
vrows = [
    (5, "Pipes, gathering and Momentum: 2028E Adjusted EBITDA", "=EBITDA!F5+EBITDA!F7", M0, "My estimate."),
    (6, "Multiple", L("core_mult"), MULTF, "Williams' year-end EV over Adjusted EBITDA: about 13.4x in 2024 and 2025."),
    (7, "Value of pipes and gathering", "=B5*B6", M0, ""),
    (8, "Power Innovation: run-rate EBITDA", "=Power!B12", M0, "Five projects at full output, 2029."),
    (9, "Multiple", L("pi_mult"), MULTF, "Contracts of 10 to 12.5 years; PV of the term at 8% is 7.4x."),
    (10, "Less power capital still to spend after 2027", "=-" + A["pi_remain"], M0, ""),
    (11, "Value of Power Innovation", "=B8*B9+B10", M0, ""),
    (12, "Enterprise value, October 2027", "=B7+B11", M0, ""),
    (13, "Less net debt, end 2027", "=-Cash!D18", M0, "My roll in the Cash tab."),
    (14, "Less existing noncontrolling interests", f"=-{A['nci_inc']}*{A['nci_pe']}", M0, "20x income; book 2,178."),
    (15, "Less Blackstone's investment balance", "=-" + A["bx_total"], M0, "Treated as debt-like: 6.35% target return, cut by excess distributions."),
    (16, "Equity value", "=SUM(B12:B15)", M0, ""),
    (17, "Shares, m", f"={A['sh_jul']}+{A['sh_mom']}", M1, "30 July 2026 plus the Momentum shares."),
    (18, "BASE VALUE PER SHARE, US$", "=B16/B17", USD2, ""),
    (19, "Reference price, US$", L("price"), USD2, "NYSE close, 30 October 2026."),
    (20, "Base value against price", "=B18/B19-1", PCT1, "Band: LONG at +15% or more, SHORT at -25% or worse, NO CALL between."),
    (21, "VIEW ON THE BAND", '=IF(B20>=0.15,"LONG",IF(B20<=-0.25,"SHORT","NO CALL"))', None, ("Draft view. Tommy Lau decides the call." if CALL["draft"] else "Tommy Lau's call, 2 November 2026: NO CALL, Medium conviction.")),
    (23, "Market value, US$bn", "=B17*B19/1000", '#,##0.0', ""),
    (24, "Net debt, 30 September 2026 (my estimate), US$m", f"={A['debt']}-{A['cash']}-{A['bx_jul']}+{A['mom_cash']}+2400+640+80-1550", M0, "30 June plus Q3: capex ~2,400, dividends ~640, NCI ~80, AFFO ~1,550 (mine), Blackstone and Momentum."),
    (25, "Enterprise value now, US$bn", f"=B23+(B24-B14+{A['bx_jul']})/1000", '#,##0.0', "Includes NCI and the Blackstone capital received so far."),
    (26, "EV / 2026 Adjusted EBITDA guide", "=B25*1000/EBITDA!D9", MULTF, ""),
    (27, "EV / 2027E Adjusted EBITDA", "=B25*1000/EBITDA!E9", MULTF, ""),
    (28, "Power multiple the price implies at 13.5x pipes", "=(B19*B17-B13-B14-B15-B10-B7)/B8", MULTF, "What the market pays for the five projects, on my other inputs."),
    (29, "Price below which the base value is 15% or more above it", "=B18/1.15", USD2, ""),
    (30, "Price above which the base value is 25% or more below it", "=B18/0.75", USD2, ""),
    (31, "Price against the highest close", f"=B19/{A['hiclose']}-1", PCT1, ""),
    (32, "Price change in 2026 to date", f"=B19/{A['pxdec']}-1", PCT1, ""),
    (33, "Dividend yield at the price", f"={A['dps26']}/B19", PCT1, ""),
    (34, "Average analyst target against price", f"={A['cons_tp']}/B19-1", PCT1, "Cross-check only."),
]
for rr, lab_, f, fmt, nt in vrows:
    ws.cell(row=rr, column=1, value=lab_)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    if rr in (18, 21):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    elif isinstance(f, str) and "!" in f: c.font = F_LINK
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP

# =====================================================================  SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT", [10, 12, 12, 13, 12, 12, 14, 14, 12, 11])
head(ws, 4, ["Case", "Pipes growth 27", "Pipes growth 28", "Momentum 2028", "Pipes multiple", "Power multiple",
             "Pipes + Momentum 2028E", "EV", "Value, US$", "vs price"])
for i, s in enumerate(SCEN):
    rr = 5 + i
    name = s[0]
    ws.cell(row=rr, column=1, value=name).font = F_B
    if name == "Base":
        for j, k in enumerate(["core_g27", "core_g28", "mom28", "core_mult", "pi_mult"]):
            c = ws.cell(row=rr, column=2 + j, value="=" + A[k]); c.font = F_LINK
    else:
        for j, v in enumerate([s[1], s[2], s[3], s[4], s[5]]):
            c = ws.cell(row=rr, column=2 + j, value=v); c.font = F_INB; c.fill = FILL_ASSUME
    for j, fm in enumerate([PCT1, PCT1, M0, MULTF, MULTF]):
        ws.cell(row=rr, column=2 + j).number_format = fm
    ws.cell(row=rr, column=7, value=f"=EBITDA!$D$5*(1+B{rr})*(1+C{rr})+D{rr}").number_format = M0
    ws.cell(row=rr, column=8, value=f"=G{rr}*E{rr}+Power!$B$12*F{rr}+Valuation!$B$10").number_format = M0
    ws.cell(row=rr, column=9, value=f"=(H{rr}+Valuation!$B$13+Valuation!$B$14+Valuation!$B$15)/Valuation!$B$17").number_format = USD2
    ws.cell(row=rr, column=10, value=f"=I{rr}/{A['price']}-1").number_format = PCT1
ws["A9"] = "Probability"; ws["A9"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=8, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=9, column=2 + j, value=s[7]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E9"] = "=SUM(B9:D9)"; ws["E9"].number_format = PCT0; ws["F9"] = "must be 100%"; ws["F9"].font = F_NOTE
ws["A11"] = "Probability-weighted value, US$"; ws["A11"].font = F_B
ws["E11"] = "=B9*I5+C9*I6+D9*I7"; ws["E11"].number_format = USD2; ws["E11"].font = F_B; ws["E11"].fill = FILL_KEY
ws["F11"] = f"=E11/{A['price']}-1"; ws["F11"].number_format = PCT1
ws["A12"] = "Check: base case equals the Valuation tab"; ws["E12"] = "=I6-Valuation!B18"; ws["E12"].number_format = '0.000'
note(ws, 14, [
    "All cases use the same net debt, NCI and Blackstone balance; a weaker case would also carry more debt, so the bear case is if anything generous.",
    "Bear: gas demand growth slows and AI power deals stall; pipes grow 2% a year, multiple back to 11.5x; power valued at 6x, below its contracts at 8%.",
    "Bull: more Transco expansions and the 6 GW power backlog converts; pipes 5% then 6%, 15x; power at 11x for extensions and new projects.",
])

# =====================================================================  SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: PIPES MULTIPLE AGAINST POWER MULTIPLE (US$)", [34, 14, 14, 14])
head(ws, 4, ["Pipes multiple \\ Power multiple", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_PM, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["pi_mult"]) if link else m)
    c.number_format = MULTF; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (cm, link) in enumerate(zip(SENS_CM, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=("=" + A["core_mult"]) if link else cm)
    c.number_format = MULTF; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=(f"=(Valuation!$B$5*$A{rr}+Valuation!$B$8*{col}$4+Valuation!$B$10"
                                              f"+Valuation!$B$13+Valuation!$B$14+Valuation!$B$15)/Valuation!$B$17")).number_format = USD2
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
ws["A11"] = "Value per turn of the pipes multiple, US$"; ws["B11"] = "=(B7-B5)/3"; ws["B11"].number_format = USD2
ws["A12"] = "Value per turn of the power multiple, US$"; ws["B12"] = "=(D5-B5)/4"; ws["B12"].number_format = USD2

# =====================================================================  DIVIDEND
ws = sheet("Dividend", "DIVIDEND CROSS-CHECK: TWO-STAGE DIVIDEND DISCOUNT MODEL", [40, 13, 13, 13])
head(ws, 4, ["Year", "Dividend, US$", "Discount factor", "Present value, US$"])
for t in range(1, 11):
    rr = 4 + t
    ws.cell(row=rr, column=1, value=2026 + t)
    prev = L("dps26") if t == 1 else f"=B{rr - 1}"
    ws.cell(row=rr, column=2, value=(f"={A['dps26']}" if t == 1 else f"=B{rr - 1}") + f"*(1+{A['dg1']})").number_format = USD2
    ws.cell(row=rr, column=3, value=f"=1/(1+{A['ke']})^{t}").number_format = '0.0000'
    ws.cell(row=rr, column=4, value=f"=B{rr}*C{rr}").number_format = USD2
ws["A16"] = "Terminal value at year 10, US$"; ws["B16"] = f"=B14*(1+{A['dg2']})/({A['ke']}-{A['dg2']})"; ws["B16"].number_format = USD2
ws["D16"] = "=B16*C14"; ws["D16"].number_format = USD2
ws["A17"] = "VALUE PER SHARE, US$"; ws["A17"].font = F_B
ws["D17"] = "=SUM(D5:D14)+D16"; ws["D17"].number_format = USD2; ws["D17"].font = F_B; ws["D17"].fill = FILL_KEY
ws["A18"] = "Against the price"; ws["D18"] = f"=D17/{A['price']}-1"; ws["D18"].number_format = PCT1
ws["A20"] = "Dividend growth for ten years the price needs at 8% and 3% after"; put(ws, "D20", DIV_G_NEEDED, PCT1, F_IN)
ws["A21"] = "Cost of equity the price implies at 7% growth"; put(ws, "D21", IMPL_KE, PCT1, F_IN)
note(ws, 23, ["Rows 20 and 21 are solved in data.py (goal seek) and entered as values. AFFO per share: US$5.15 guided for 2026, and the",
              "dividend takes about 41% of it, so a dividend model undercounts the cash. I use it to show what growth the price needs."])

# =====================================================================  PEERS
ws = sheet("Peers", "PEER MULTIPLES (stockanalysis.com, RETRIEVED 2 NOVEMBER 2026)", [22, 13, 16, 12, 12, 60])
head(ws, 4, ["Company", "Ticker", "EV/EBITDA (trailing)", "Forward P/E", "Dividend yield", "What they do"])
for i, (co, tk, ev, pe, dy, what, grp) in enumerate(PEERS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=co).font = F_B if grp == "self" else Font()
    ws.cell(row=rr, column=2, value=tk)
    for j, (v, fm) in enumerate([(ev, MULTF), (pe, MULTF), (dy, PCT1)]):
        c = ws.cell(row=rr, column=3 + j, value=v); c.number_format = fm; c.font = F_IN
    ws.cell(row=rr, column=6, value=what).alignment = WRAP
last = 4 + len(PEERS)
ws[f"A{last + 2}"] = "Peer median (excluding Williams)"; ws[f"A{last + 2}"].font = F_B
for col in "CDE":
    ws[f"{col}{last + 2}"] = f"=MEDIAN({col}6:{col}{last})"
    ws[f"{col}{last + 2}"].number_format = PCT1 if col == "E" else MULTF
note(ws, last + 4, ["stockanalysis.com computes EBITDA its own way (Williams: US$7.03bn trailing against Williams' Adjusted EBITDA of US$8.13bn),",
                    "so these multiples compare peers with each other, not with my valuation. No view on the peers' shares is expressed.",
                    "Williams on the same basis, year end: 12.6x (2021), 13.0x (2022), 10.9x (2023), 16.9x (2024), 15.3x (2025)."])

# =====================================================================  SOURCES
ws = sheet("Sources", "SOURCES", [6, 150])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Williams Q2 2026 earnings release, Form 8-K Ex. 99.1, 3 August 2026: Adjusted EBITDA by segment and quarter, balance sheet, AFFO, dividends, 2026 guidance and reconciliation, Momentum terms, Socrates phase one complete within budget and on time.",
    "Williams Form 10-Q, quarter to 30 June 2026: Power Innovation projects (MW, contract terms, in-service windows), Blackstone joint venture note, Southeast Supply Enhancement, shares outstanding.",
    "Williams Form 10-K 2025 (24 February 2026) and Form 10-Q, quarter to 31 March 2026: Socrates 400 MW committed to the customer; 556 MW expected capacity.",
    "Williams earnings releases of 3 November 2025, 10 February 2026 and 4 May 2026 (Form 8-K Ex. 99.1): Socrates at US$2bn; over US$7bn of power capital; Neo US$2.3bn, 682 MW; 2025 results; dividend.",
    "Williams Form 8-K, 13 July 2026, Ex. 99.1 and 99.2: Blackstone, Apollo and KKR joint venture, US$5.34bn for 49%, 6.35% target return, buyout illustration.",
    "Williams prospectus supplement (424B2), 3 September 2026: 26,874,496 shares issued to the Momentum sellers.",
    "Williams Q1 and Q2 2026 earnings calls (5 May and 4 August 2026), third-party transcripts (AllMind): 5x build multiple on Neo, 'like our other power innovation projects' (CEO); US$9.6bn on the Q2 slides; 11%+ growth target; turbines locked up; 200 MW in under 18 months since commercialisation.",
    "Ohio Power Siting Board, case 25-188-EL-BGN, 18 September 2025: Socrates North, 200 MW, not connected to the grid, for Sidecat, a Meta affiliate.",
    "PJM, 2027/2028 Base Residual Auction report, December 2025: RTO capacity price US$333.44/MW-day.",
    "Nasdaq.com historical prices for WMB, retrieved 2 November 2026; stockanalysis.com (S&P Global data) for consensus, targets and multiples, retrieved 2 November 2026.",
    "The Physical Layer, 'Building your own power: GE Vernova's queue, not the grid's, sets the date': https://thephysicallayer.fyi/journal/building-your-own-power/",
    "Estimates for 2026 splits, 2027, 2028 and beyond are the author's own. Personal research, not investment advice.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# =====================================================================  COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    (("Draft view on the band" if CALL["draft"] else "Call (Tommy Lau, 2 November 2026)"), "=Valuation!B21", None, "LONG at +15% or more, SHORT at -25% or worse, NO CALL between. Tommy Lau decides the call."),
    (("Draft conviction" if CALL["draft"] else "Conviction"), CALL["conviction"], None, "Judgement, not formula."),
    ("Base value per share, US$", "=Valuation!B18", USD2, "Sum of the parts: pipes at 13.5x 2028E, power at 8x run-rate, less debt, NCI and Blackstone."),
    ("Reference price, US$", "=" + A["price"], USD2, "NYSE close, 30 October 2026."),
    ("Base value against price", "=Valuation!B20", PCT1, ""),
    ("Probability-weighted value, US$", "=Scenarios!E11", USD2, "25 / 50 / 25 bear / base / bull."),
    ("Dividend model value, US$", "=Dividend!D17", USD2, "7% growth for ten years, 8% cost of equity."),
    ("2028E Adjusted EBITDA, US$m", "=EBITDA!F9", M0, "My estimate."),
    ("Horizon", "12 months, to October 2027", None, ""),
    ("Wrong if", "See note", None, WRONG_IF),
]
for i, (lab_, v, fmt, nt) in enumerate(cover):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab_).font = F_B
    c = ws.cell(row=rr, column=2, value=v)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    c.font = F_LINK if isinstance(v, str) and v.startswith("=") else F_IN
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
ws.row_dimensions[14].height = 58
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Power", "The five Power Innovation projects: MW, terms, timing, EBITDA, returns."),
    ("EBITDA", "Adjusted EBITDA by source, 2024A to 2028E, against Williams' 11% path."),
    ("Cash", "AFFO, dividends, capex and the net debt roll to end 2027."),
    ("Valuation", "Sum of the parts, the band, multiples at the price, revisit levels."),
    ("Scenarios", "Bear / base / bull and the probability-weighted value."),
    ("Sensitivity", "Pipes multiple against power multiple."),
    ("Dividend", "Two-stage dividend discount cross-check."),
    ("Peers", "Trailing EV/EBITDA, forward P/E and yields of pipeline peers."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t)
    ws.cell(row=18 + i, column=2, value=d)
ws["A29"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A29"].font = F_NOTE
ws["A30"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."
ws["A30"].font = F_NOTE

for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
