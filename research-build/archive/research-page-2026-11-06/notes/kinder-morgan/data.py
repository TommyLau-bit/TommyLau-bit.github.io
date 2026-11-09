"""Kinder Morgan, Inc. (NYSE: KMI) initiation, drafted 2 Nov 2026. Single source of figures for charts, note and model.

Fiscal year = calendar year. US$ million unless stated. Adjusted EBITDA, Adjusted EPS, Net Debt and Project EBITDA are
KMI's non-GAAP measures as KMI defines them.
Sources (SEC EDGAR, KMI CIK 1506307):
- Q3 2026 results, Form 8-K Ex. 99.1, 21 Oct 2026 (kmi2026q38-kex991.htm): Q3 and nine-month results, LTM Adjusted
  EBITDA 9,189, Net Debt 32,229, 3.5x, backlog US$14.4bn (US$13.2bn natural gas; >75% power generation and LDC demand;
  US$13.7bn take-or-pay portion at ~5.7x first-full-year Project EBITDA), Permian Link, Southeast Connector, Creekside,
  Bear Creek, 2026 outlook (>6% above the US$8.6bn EBITDA budget, >13% above the US$1.36 EPS budget, 3.6x year end).
- Form 10-Q for the quarter to 30 Sep 2026, filed 23 Oct 2026: 2,227,715,229 shares at 22 Oct 2026; US$4.2bn of 2026
  expansion, acquisitions and JV contributions; remaining performance obligations US$1bn / 5bn / 31bn.
- Form 10-K 2025, filed 13 Feb 2026: major projects table with KMI-share capital and in-service dates; RPO at Dec 2025.
- Quarterly results releases, Form 8-K Ex. 99.1, 17 Jan 2024 to 22 Jul 2026: quarterly Adjusted EBITDA, Adjusted EPS,
  backlog, net debt, NCI, cash flow, dividends.
- Q3 2026 earnings call, 21 Oct 2026, transcript published by Earnings Whispers (KMI posts only the webcast): CFO,
  "approximately $225 million" of items that may not recur in 2026; "an additional $175 million versus our budget" from
  commodity prices; "at least 20-year take-or-pay contracts" on the two large projects; Rich Kinder, "$2.5 billion of
  additional EBITDA" on the backlog. Third-party transcript; labelled as such in the note.
Prices: Nasdaq historical quotes API (daily close, high, low), retrieved 2 Nov 2026; cross-checked against
stockanalysis.com. Yahoo returned "Too Many Requests". Consensus, targets and peer multiples: stockanalysis.com (S&P
Global data), retrieved 2 Nov 2026. Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "KinderMorgan"
SLUG = "kinder-morgan"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/kinder-morgan"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Published 2 Nov 2026 on Tommy's instruction to follow the view on the band. ----
CALL = dict(
    banner="NO CALL",
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Nasdaq historical quotes, retrieved 2 Nov 2026) ----
PRICE = 33.87               # NYSE close, Friday 30 Oct 2026
PRICE_DATE = "30 October 2026"
HI_CLOSE = 34.43            # highest close in the series since Dec 2023, 23 Oct 2026
HI_CLOSE_DATE = "23 October 2026"
HI_INTRA = 34.805           # highest intraday, 19 May 2026
HI_INTRA_DATE = "19 May 2026"
LO_52W = 25.84              # lowest close of the past year, 4 Nov 2025
PX_DEC23, PX_DEC24, PX_DEC25 = 17.64, 27.40, 27.49
PX_JAN24 = 16.92            # close 31 Jan 2024
PX_OCT21, PX_OCT22 = 33.97, 33.72   # Q3 results came after the close on 21 Oct

# ---- Shares and balance sheet ----
SHARES = 2227.7             # m, outstanding at 22 Oct 2026 (10-Q cover)
NET_DEBT = 32229.0          # KMI Net Debt, 30 Sep 2026 (Q3 release, Table 5)
NCI = 1232.0                # noncontrolling interests, 30 Sep 2026
LTM_EBITDA = 9189.0         # Adjusted EBITDA, twelve months to 30 Sep 2026
LEV_SEP26 = 3.5

# ---- Annual history (KMI releases) ----
YEARS = ["2023A", "2024A", "2025A"]
EBITDA_H = [7561.0, 7938.0, 8391.0]
EPS_H = [1.07, 1.15, 1.30]
DPS_H = [1.13, 1.15, 1.17]
NETDEBT_H = [31837.0, 31725.0, 31716.0]
NCI_H = [1424.0, 1336.0, 1287.0]
SHARES_H = [2221.0, 2222.0, 2225.0]      # Q4 weighted average shares, m
PX_H = [PX_DEC23, PX_DEC24, PX_DEC25]
CFO_25, CAPEX_25 = 5917.0, 3026.0

# ---- 2026 budget and outlook ----
BUDGET26_EBITDA = 8600.0
BUDGET26_EPS = 1.36
DPS26 = 1.19
OUT26_EBITDA_PCT = 0.06     # "more than 6% favorable" (Q3 release)
OUT26_EPS_PCT = 0.13
LEV26_OUT = 3.6
NONREC26 = 225.0            # potentially non-recurring items in 2026 (Q3 call transcript, Earnings Whispers)
COMMOD26 = 175.0            # favourable commodity prices against budget (Q3 call transcript, Earnings Whispers)
EBITDA_9M26 = 6918.0
GROWTH_CAPEX26 = 4200.0     # 10-Q: expansion, acquisitions and JV contributions, 2026

# ---- Quarterly series ----
Q = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
Q_EBITDA = [2137, 1858, 1880, 2063, 2157, 1972, 1991, 2271, 2539, 2199, 2180]
BL_LABELS = ["Dec 23", "Mar 24", "Jun 24", "Sep 24", "Dec 24", "Mar 25", "Jun 25", "Sep 25", "Dec 25", "Mar 26", "Jun 26", "Sep 26"]
BACKLOG = [3.0, 3.3, 5.2, 5.1, 8.1, 8.8, 9.3, 9.3, 10.0, 10.1, 9.6, 14.4]   # US$bn, project backlog at quarter end
BACKLOG_TOP = 13.7          # US$bn, take-or-pay portion used for the Project EBITDA multiple, Sep 2026
BACKLOG_MULT = 5.7          # first-full-year Project EBITDA multiple, Sep 2026
BACKLOG_GAS = 13.2
RPO = (1.0, 5.0, 31.0)      # US$bn: rest of 2026, 2027, 2028 and after (10-Q, 30 Sep 2026)
RPO_DEC25 = (5.0, 5.0, 26.0)

# ---- Named projects with KMI-share capital and first in-service year (10-K 2025 table, 2026 releases) ----
# (name, KMI-share US$m, first in-service year, what it serves)
PROJECTS = [
    ("KinderHawk Plantation North", 516, 2026, "Haynesville gathering and treating"),
    ("Creekside Lateral, phase 1", 85, 2026, "Central Texas power, industry, data centres"),
    ("Trident Intrastate", 1799, 2027, "LNG and industry, Port Arthur; second phase Q4 2028"),
    ("Creekside Lateral, phases 2 and 3", 150, 2027, "Data centre and industrial customers"),
    ("Pelican", 135, 2027, "TGP capacity, south-east Louisiana"),
    ("Houston Ship Channel products and export terminal", 169, 2027, "Refined products"),
    ("Mississippi Crossing", 1703, 2028, "South-east markets via TGP"),
    ("South System Expansion 4", 1830, 2028, "South-east power and gas utilities; second phase Q4 2029"),
    ("FGT Phase IX and South Florida", 700, 2028, "Florida; South Florida lateral Q1 2030"),
    ("North Extension", 170, 2028, "NGPL Midwest"),
    ("Texas Access", 112, 2028, "LNG customer, south Louisiana"),
    ("Amarillo Expansion", 75, 2028, "Texas Panhandle, including data centres"),
    ("Bear Creek Storage", 120, 2029, "Storage for TGP"),
    ("Elba Express Bridge", 430, 2030, "South Carolina"),
    ("Permian Link", 1600, 2030, "New power generation for an A-rated hyperscaler"),
    ("Southeast Connector", 3100, 2030, "South-east; phases from Q4 2030"),
]
LAND_YEARS = [2026, 2027, 2028, 2029, 2030]
LAND = {y: sum(p[1] for p in PROJECTS if p[2] == y) for y in LAND_YEARS}
NAMED_TOTAL = sum(LAND.values())
AI_PIPES = 1600 + 3100      # Permian Link and Southeast Connector, KMI share

# ---- MY estimates ----
EBITDA26 = 9150.0           # MINE: KMI says more than 6% above the US$8.6bn budget (US$9,116m)
EPS26_FLOOR = BUDGET26_EPS * (1 + OUT26_EPS_PCT)
UNDERLYING26 = EBITDA26 - NONREC26
BASE_G = 0.01               # MINE: underlying growth a year (escalators, high utilisation, 2026 projects for a full year)
BL27, BL28, BL29 = 300.0, 650.0, 1050.0   # MINE: Project EBITDA from the backlog in each year
BACKLOG_EBITDA = BACKLOG_TOP / BACKLOG_MULT * 1000   # full run-rate, US$m (derived)
DPS27 = 1.21                # MINE: 2% growth, the pattern since 2024
CFO27 = 6850.0              # MINE
CAPEX27 = 5000.0            # MINE: sustaining plus expansion and JV contributions
BASE_MULT = 11.5            # MINE: KMI's own range since the 2024 re-rating, 11.2x to 11.9x
CONS_EPS26, CONS_EPS27 = 1.57, 1.55      # stockanalysis.com, updated 28 Oct 2026
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 37.55, 24, 32.0, 43.0


def ebitda(year, g=BASE_G, bl=None, nonrec_back=0.0):
    """Adjusted EBITDA, MINE. year in (2027, 2028, 2029)."""
    bl = bl if bl is not None else {2027: BL27, 2028: BL28, 2029: BL29}[year]
    n = year - 2026
    return (UNDERLYING26 + nonrec_back) * (1 + g) ** n + bl


E27, E28, E29 = ebitda(2027), ebitda(2028), ebitda(2029)
ND26 = LEV26_OUT * EBITDA26                   # KMI's own 3.6x year-end expectation
ND27 = ND26 + CAPEX27 + DPS27 * SHARES - CFO27
LEV27 = ND27 / E27


def value(e28, mult):
    return (mult * e28 - ND27 - NCI) / SHARES


BASE_VALUE = value(E28, BASE_MULT)
SCEN = [  # name, underlying growth, backlog EBITDA in 2028, multiple, prob, what happens
    ("Bear", 0.0, 350.0, 10.0, 0.25),
    ("Base", BASE_G, BL28, BASE_MULT, 0.50),
    ("Bull", 0.015, 950.0, 13.0, 0.25),
]
SC = []
for nm, g, bl, mult, p in SCEN:
    e = ebitda(2028, g=g, bl=bl)
    SC.append(dict(name=nm, g=g, bl=bl, e28=e, mult=mult, prob=p, value=value(e, mult)))
WEIGHTED = sum(x["value"] * x["prob"] for x in SC)
SENS_E = [SC[0]["e28"], E28, SC[2]["e28"]]
SENS_M = [10.5, BASE_MULT, 12.5]

# ---- Derived market figures ----
MCAP = PRICE * SHARES / 1000
EV = MCAP + (NET_DEBT + NCI) / 1000
EV_LTM = EV * 1000 / LTM_EBITDA
EV_26 = EV * 1000 / EBITDA26
EV_27 = EV * 1000 / E27
EV_28 = EV * 1000 / E28
HIST_EV = [(p * s / 1000 + (nd + n) / 1000) * 1000 / e for p, s, nd, n, e in zip(PX_H, SHARES_H, NETDEBT_H, NCI_H, EBITDA_H)]
DIV_YIELD = DPS26 / PRICE
DIV_YIELD_DEC23 = 1.13 / PX_DEC23
FCF25 = CFO_25 - CAPEX_25
FCF_YIELD25 = FCF25 / (MCAP * 1000)
# What the price pays for: the EBITDA the current EV implies at the end-2023 multiple
IMPLIED_EBITDA_AT_23 = EV * 1000 / HIST_EV[0]
IMPLIED_BL_SHARE = (IMPLIED_EBITDA_AT_23 - UNDERLYING26) / BACKLOG_EBITDA
UP_BASE = BASE_VALUE / PRICE - 1
LONG_BELOW = BASE_VALUE / 1.15
SHORT_ABOVE = BASE_VALUE / 0.75
SINCE_JAN24 = PRICE / PX_JAN24 - 1
YTD = PRICE / PX_DEC25 - 1
Q3_MOVE = PX_OCT22 / PX_OCT21 - 1
EV_MULT_FOR_LONG = (PRICE * 1.15 * SHARES + ND27 + NCI) / E28
DIV_CHECK = DPS27 / DIV_YIELD                 # 2027 dividend at today's yield
PL_EBITDA = 1600 / BACKLOG_MULT * 1000 / 1000  # US$m per US$bn: Permian Link at 5.7x (derived)
AI_PIPES_EBITDA = AI_PIPES / BACKLOG_MULT      # US$m

# ---- Price, month-end close (Nasdaq historical quotes, unadjusted) ----
PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24",
             "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
             "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26",
             "30 Oct 26"]
PX = [16.92, 17.39, 18.34, 18.28, 19.49, 19.87, 21.13, 21.57, 22.09, 24.51, 28.27, 27.40, 27.48, 27.10, 28.53, 26.30, 28.04,
      29.40, 28.06, 26.98, 28.31, 26.19, 27.32, 27.49, 30.49, 33.27, 33.53, 32.87, 31.08, 31.97, 32.18, 32.24, 30.15, 33.87]

# ---- Peers (stockanalysis.com, retrieved 2 Nov 2026; closes of 30 Oct 2026) ----
PEERS = [  # company, ticker, trailing EV/EBITDA, dividend yield, what they run, group
    ("Kinder Morgan", "NYSE: KMI", 14.05, 0.0351, "Gas pipelines and storage, products pipelines, terminals, CO2", "self"),
    ("Williams", "NYSE: WMB", 17.28, 0.0282, "Transco and other gas pipelines; Socrates power plants", "peer"),
    ("TC Energy", "NYSE: TRP", 17.13, 0.0386, "Gas pipelines in Canada, the US and Mexico; power", "peer"),
    ("DT Midstream", "NYSE: DTM", 16.85, 0.0283, "Gas pipelines, storage and gathering", "peer"),
    ("Enbridge", "NYSE: ENB", 16.07, 0.0563, "Liquids and gas pipelines, gas utilities", "peer"),
    ("ONEOK", "NYSE: OKE", 11.62, 0.0441, "NGL, gas and refined products pipelines", "peer"),
    ("Enterprise Products", "NYSE: EPD", 10.89, 0.0587, "NGL, crude, gas and petrochemical pipelines", "peer"),
    ("Energy Transfer", "NYSE: ET", 8.23, 0.0650, "Gas, NGL and crude pipelines; export terminals", "peer"),
]

REVISIT_IF = ("A price below about US$30, where my base value would sit 15 per cent above it, or a 2027 budget with Adjusted "
              "EBITDA of US$9.7bn or more, which would put my 2028 estimate near the bull case.")
WRONG_IF = ("The shares close above US$43.50 or below US$25.90 at the end of October 2027, outside my bull and bear values; "
            "or 2026 Adjusted EBITDA lands below US$9.1bn, short of the 6 per cent beat on budget Kinder Morgan expects; or Permian Link "
            "or the Southeast Connector is cancelled or its first in-service date moves beyond 2031.")

if __name__ == "__main__":
    print("land by year", LAND, "named", NAMED_TOTAL, "AI pipes", AI_PIPES, f"share 2030 {LAND[2030] / 14400:.1%}")
    print(f"backlog EBITDA {BACKLOG_EBITDA:.0f}; AI pipes EBITDA {AI_PIPES_EBITDA:.0f}; underlying26 {UNDERLYING26:.0f}; EPS floor {EPS26_FLOOR:.3f}")
    print(f"E27 {E27:.0f} ({E27 / EBITDA26 - 1:+.1%}) E28 {E28:.0f} ({E28 / E27 - 1:+.1%}) E29 {E29:.0f}")
    print(f"ND26 {ND26:.0f} ND27 {ND27:.0f} lev27 {LEV27:.2f}")
    print(f"mcap {MCAP:.2f} EV {EV:.2f} EV/LTM {EV_LTM:.2f} EV/26 {EV_26:.2f} EV/27 {EV_27:.2f} EV/28 {EV_28:.2f}")
    print("hist EV/EBITDA", [round(h, 2) for h in HIST_EV])
    print(f"div yield {DIV_YIELD:.2%} dec23 {DIV_YIELD_DEC23:.2%} FCF25 {FCF25:.0f} yield {FCF_YIELD25:.2%}")
    print(f"implied EBITDA at 2023 multiple {IMPLIED_EBITDA_AT_23:.0f}; share of backlog {IMPLIED_BL_SHARE:.0%}")
    print(f"base {BASE_VALUE:.2f} {UP_BASE:+.1%}; long below {LONG_BELOW:.2f}; short above {SHORT_ABOVE:.2f}; mult for long {EV_MULT_FOR_LONG:.2f}")
    for x in SC:
        print(x["name"], round(x["e28"]), x["mult"], round(x["value"], 2), f"{x['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED / PRICE - 1:+.1%}")
    print("grid", [[round(value(e, m), 2) for m in SENS_M] for e in SENS_E])
    print(f"since jan24 {SINCE_JAN24:.1%} ytd {YTD:.1%} q3 move {Q3_MOVE:+.1%} div check {DIV_CHECK:.2f} cons tp {CONS_TP / PRICE - 1:+.1%}")
    import statistics
    print("peer median", statistics.median(p[2] for p in PEERS if p[5] == "peer"))
