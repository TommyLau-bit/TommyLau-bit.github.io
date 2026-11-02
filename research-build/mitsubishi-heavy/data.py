"""Mitsubishi Heavy Industries (TSE: 7011) initiation, 2 Nov 2026. Single source of figures for charts, note and model.

Fiscal year ends 31 March: FY2025 = year to March 2026; FY2026 = year to March 2027; FY2027 = year to March 2028.
Sources (mhi.com/finance/library):
- Q1 FY2026 Financial Results presentation and Consolidated Financial Results (4 Aug 2026): segment orders, revenue and
  business profit; main businesses (GTCC, Nuclear, Defense & Space); FY2026 forecast as revised; balance sheet; shares;
  large frame gas turbine units and backlog (p21); order backlog by segment (p22); FX assumptions (p16).
- Q&A Summary, Q1 FY2026 Financial Results Briefing, dated 6 Aug 2026 (CFO Hiroshi Nishio).
- FY2025 Financial Results presentation and Consolidated Financial Results (12 May 2026), with Q&A Summary of 12 May 2026:
  FY2025 actuals, GTCC and Defense & Space history (p6, p8), FY2024 restated (excl. Mitsubishi Logisnext), balance sheet.
- 2024 Medium-Term Business Plan Progress briefing, presentation and Q&A summary (27 May 2026): gas turbine capacity
  (units shipped up 30%+ by FY2028 versus current capacity, then a further 50%+, about twice FY2024), demand outlook.
- 1H FY2025 (7 Nov 2025) and Q1-3 FY2025 (4 Feb 2026) presentations and Q&A summaries: unit backlog history, demand views.
- IR events, mhi.com/finance: 1H FY2026 results release on 6 Nov 2026, 13:30 JST (scheduled).
Prices: stockanalysis.com (TYO:7011 daily and monthly history, split-adjusted), retrieved 2 Nov 2026. Yahoo Finance chart API
answered "Too Many Requests" and was not retried. Consensus and peer multiples: stockanalysis.com, retrieved 2 Nov 2026.
Everything marked MINE is my own estimate. Yen billion unless stated.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "MitsubishiHeavy"
SLUG = "mitsubishi-heavy"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/mitsubishi-heavy"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call (Tommy Lau, 2 Nov 2026: publish with the draft view as the call). ----
CALL = dict(
    banner="NO CALL",
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (stockanalysis.com TYO:7011, retrieved 2 Nov 2026) ----
PRICE = 3363.0              # TSE close, 2 Nov 2026; the lowest close since 18 Jul 2025 (¥3,211)
PRICE_DATE = "2 November 2026"
HI_CLOSE = 5195.0           # record close, 2 Mar 2026
HI_INTRA = 5208.0           # record intraday high, 2 Mar 2026
PX_DEC25 = 3840.0           # close, 30 Dec 2025
PX_Q1_PRE, PX_Q1_DAY = 3799.0, 4091.0      # closes 3 and 4 Aug 2026 (Q1 results released 4 Aug, during trading)
PX_FY_PRE, PX_FY_DAY = 4384.0, 4300.0      # closes 11 and 12 May 2026 (FY2025 results, 12 May)
PX_MTBP_PRE, PX_MTBP_DAY = 3944.0, 3898.0  # closes 26 and 27 May 2026 (2024 MTBP progress briefing, 27 May)
PX_H1_PRE, PX_H1_DAY = 4618.0, 4449.0      # closes 6 and 7 Nov 2025 (1H FY2025 results, 7 Nov 2025)

# ---- Shares and balance sheet, 30 Jun 2026 (Q1 FY2026 Consolidated Financial Results and presentation p8) ----
SHARES_ISSUED = 3373.647810  # m, including treasury shares
TREASURY = 12.985995         # m
SHARES = SHARES_ISSUED - TREASURY
CASH = 1684.084
DEBT = 519.8                 # interest-bearing debt, presentation p8
EQUITY_METHOD = 325.143      # investments accounted for using the equity method, book
OTHER_FA = 531.248           # non-current other financial assets, book
NCI = 68.339                 # non-controlling interests
PENSION = 57.983             # retirement benefit liabilities
CL_JUN26 = 2483.2            # contract liabilities, 30 Jun 2026
CL_MAR26 = 2161.8            # 31 Mar 2026
CL_MAR25 = 1434.5            # 31 Mar 2025, after the Logisnext reclassification (FY2025 presentation p12)
ADV_COST_SHARE = 0.80        # MINE: share of the advance build-up still to be spent on delivery (1 less a ~20% margin)
BACKLOG_JUN26 = 14103.0
BACKLOG_SEG = {"Energy": 7814.6, "PI": 2286.1, "IS": 103.2, "ADS": 3898.3}

# ---- Group (continuing operations, excluding Mitsubishi Logisnext) ----
GROUP = {  # orders, revenue, business profit, net income (owners of parent)
    "FY2024": (6405.1, 4361.1, 354.9, 245.4),
    "FY2025": (7653.6, 4974.1, 432.2, 332.1),
    "FY2026G": (7000.0, 5400.0, 540.0, 380.0),
}
EPS25, EPS26G = 98.86, 113.09
DPS26 = 29.0
FCF25, FCF26G, FCF26G_MAY = 893.4, 600.0, 300.0
Q1_FCF = 391.5
FX_USD = 150.0               # MHI's FY2026 assumption

# ---- Segments: FY2025 actual (restated for April 2026 changes) and FY2026 forecast (revised 4 Aug 2026) ----
SEGS = ["Energy", "PI", "IS", "ADS", "Corp"]
SEG_NAMES = {"Energy": "Energy Systems", "PI": "Plants & Infrastructure Systems", "IS": "Industrial Solutions",
             "ADS": "Aircraft, Defense & Space", "Corp": "Others, Corporate & Eliminations"}
ORD25 = {"Energy": 3936.7, "PI": 1158.0, "IS": 704.7, "ADS": 1929.4, "Corp": -75.3}
REV25 = {"Energy": 2062.6, "PI": 880.8, "IS": 699.9, "ADS": 1393.8, "Corp": -63.1}
BP25 = {"Energy": 267.2, "PI": 84.1, "IS": -2.0, "ADS": 151.5, "Corp": -68.5}
ORD26 = {"Energy": 3550.0, "PI": 1000.0, "IS": 750.0, "ADS": 1750.0, "Corp": -50.0}
REV26 = {"Energy": 2200.0, "PI": 950.0, "IS": 750.0, "ADS": 1500.0, "Corp": 0.0}
BP26 = {"Energy": 340.0, "PI": 90.0, "IS": 30.0, "ADS": 170.0, "Corp": -90.0}
Q1_BP = {"Energy": (56.4, 101.3), "PI": (18.5, 21.7), "IS": (4.0, 9.9), "ADS": (28.8, 32.4), "Corp": (-11.1, -5.8)}
Q1_ONE_OFF = 25.0            # about ¥25bn one-time items in Q1, mostly Energy Systems (Q&A, 6 Aug 2026)
ES_BUFFER = 20.0             # general risk buffer in the FY2026 Energy Systems forecast (Q&A, 12 May 2026)

# ---- Main businesses ----
GT_YEARS = ["FY22", "FY23", "FY24", "FY25", "FY26G"]
GT_ORD = [834.6, 1259.3, 1474.4, 2652.6, 2400.0]     # GTCC order intake (FY2025 presentation p6; FY26 revised 4 Aug)
GT_REV = [736.8, 735.6, 790.7, 992.2, 1100.0]        # GTCC revenue
GT_Q1_ORD, GT_Q1_REV = (602.5, 930.0), (196.8, 274.9)  # Q1 FY25, Q1 FY26
GT_BACKLOG_FY25 = 5000.0     # "order backlog surpassing ¥5 tr" (FY2025 presentation p6)
GT_AS_RATIO = (0.55, 0.45)   # GTCC after-sales share of revenue, Q1 FY25 and Q1 FY26
NUC_REV = (361.1, 400.0); NUC_ORD = (540.6, 450.0)
DS_ORD = {"FY2024": 1876.8, "FY2025": 1682.6, "FY2026G": 1500.0}
DS_REV = {"FY2024": 827.6, "FY2025": 1144.5, "FY2026G": 1250.0}
CA_REV26 = 250.0

# Large frame gas turbines (>100 MW): units on order at period end, and orders (presentations, Nov 2025 to Aug 2026)
UNIT_LABELS = ["Sep 24", "Dec 24", "Mar 25", "Jun 25", "Sep 25", "Dec 25", "Mar 26", "Jun 26"]
UNIT_BL = [36, 40, 48, 53, 67, 75, 74, 80]
UNIT_ORD = {"FY2024": (25, 11), "FY2025": (35, 16), "Q1 FY2026": (10, 4)}    # units, GW
UNIT_BL_GW = {"Mar 25": 21, "Mar 26": 33, "Jun 26": 35}
MKT_GW_2025 = 96.1           # world gas turbine orders for power, CY2025 (McCoy Power Reports, via MHI)
MKT_GW_AVG = 70              # MHI's view: about 70 GW a year on average over the next five years (27 May 2026)

# ---- Consensus and peers (stockanalysis.com, retrieved 2 Nov 2026) ----
CONS_EPS_26 = 134.68         # FY ending Mar 2027, average (S&P Global data)
CONS_TP = 5469.0             # 17 analysts; low 3,000, high 6,400
CONS_N = 17
PEERS = [  # company, ticker, forward P/E, trailing EV/EBIT, what they make, group
    ("Mitsubishi Heavy", "TSE: 7011", 27.74, 20.74, "Gas turbines, nuclear, defence, space, aero engines, plants", "self"),
    ("GE Vernova", "NYSE: GEV", 37.17, 58.92, "Gas turbines, grid equipment, wind turbines", "gas"),
    ("Siemens Energy", "ETR: ENR", 21.81, 26.41, "Gas turbines, grid technology, wind turbines", "gas"),
    ("Rheinmetall", "ETR: RHM", 23.02, 26.15, "Ammunition, vehicles, air defence", "def"),
    ("BAE Systems", "LON: BA", 23.04, 20.39, "Combat aircraft, ships, submarines, electronics", "def"),
    ("Thales", "EPA: HO", 20.29, 19.11, "Defence electronics, aerospace, cyber", "def"),
    ("Leonardo", "BIT: LDO", 19.54, 16.96, "Helicopters, defence electronics, aerostructures", "def"),
    ("Kawasaki Heavy", "TSE: 7012", 14.21, 16.49, "Defence aircraft and submarines, aero engines, gas engines, motorcycles", "jp"),
    ("IHI", "TSE: 7013", 15.49, 14.17, "Aero engines, defence engines, plants", "jp"),
    ("Hitachi", "TSE: 6501", 21.15, 16.15, "Grid equipment, IT services, rail", "jp"),
]

# ---- MY assumptions: FY2026 GTCC split and FY2027 (year to March 2028) ----
GT_M26 = 0.20                # MINE: GTCC business profit margin in the FY2026 forecast (MHI does not disclose it)
GT_BP26 = GT_REV[4] * GT_M26
EREST_REV26 = REV26["Energy"] - GT_REV[4]
EREST_BP26 = BP26["Energy"] - GT_BP26
GT_G27, GT_M27 = 0.18, 0.22  # GTCC revenue growth and margin, FY2027
ER_G27, ER_M27 = 0.06, 0.115  # Energy rest (nuclear, steam, aero engines, compressors)
ADS_G27, ADS_M27 = 0.10, 0.12
PI_BP27, IS_BP27, CORP27 = 100.0, 35.0, -90.0
NI_RATIO = GROUP["FY2026G"][3] / GROUP["FY2026G"][2]   # net income per yen of business profit, MHI's FY2026 forecast
MULT = {"GT": 20, "ER": 14, "PI": 10, "IS": 10, "ADS": 18, "Corp": 12}
SCEN = [  # name, GTCC growth, GTCC margin, GTCC multiple, other multiples delta, prob
    ("Bear", 0.08, 0.19, 14, -3, 0.25),
    ("Base", GT_G27, GT_M27, MULT["GT"], 0, 0.50),
    ("Bull", 0.25, 0.24, 25, 2, 0.25),
]
SENS_GT = [240.0, None, 330.0]   # middle row = model FY2027E GTCC business profit
SENS_MULT = [16, 20, 24]


def gt27(g, m):
    r = GT_REV[4] * (1 + g)
    return dict(rev=r, bp=r * m)


GT_REV27 = GT_REV[4] * (1 + GT_G27)
GT_BP27 = GT_REV27 * GT_M27
ER_REV27 = EREST_REV26 * (1 + ER_G27)
ER_BP27 = ER_REV27 * ER_M27
ADS_REV27 = REV26["ADS"] * (1 + ADS_G27)
ADS_BP27 = ADS_REV27 * ADS_M27
E27 = {"GT": GT_BP27, "ER": ER_BP27, "PI": PI_BP27, "IS": IS_BP27, "ADS": ADS_BP27, "Corp": CORP27}
BP27 = sum(E27.values())
NI27 = BP27 * NI_RATIO
EPS27 = NI27 / SHARES * 1000
REST_KEYS = ["ER", "PI", "IS", "ADS", "Corp"]

# ---- Bridge ----
NETCASH = CASH - DEBT
ADV_BUILD = CL_JUN26 - CL_MAR25
ADV_DEDUCT = ADV_BUILD * ADV_COST_SHARE
ADJ_FULL = NETCASH + EQUITY_METHOD + OTHER_FA - NCI - PENSION
ADJ = ADJ_FULL - ADV_DEDUCT


def rest_ev(delta=0):
    return sum(E27[k] * (MULT[k] + delta) for k in REST_KEYS)


def value(gt_bp, gt_mult, delta=0, adj=None):
    return (gt_bp * gt_mult + rest_ev(delta) + (ADJ if adj is None else adj)) / SHARES * 1000


SOTP = {k: E27[k] * MULT[k] for k in E27}
SOTP_EV = sum(SOTP.values())
EQUITY = SOTP_EV + ADJ
BASE_VALUE = value(GT_BP27, MULT["GT"])
BASE_FULLCASH = value(GT_BP27, MULT["GT"], adj=ADJ_FULL)
MCAP = PRICE * SHARES / 1000
EV_ADJ = MCAP - ADJ
EV_SIMPLE = MCAP - NETCASH
GROSS_POS = sum(v for v in SOTP.values() if v > 0)
GT_SHARE_SOTP = SOTP["GT"] / EQUITY
ADS_SHARE_SOTP = SOTP["ADS"] / EQUITY
GT_SHARE_REV26 = GT_REV[4] / GROUP["FY2026G"][1]
DS_SHARE_REV26 = DS_REV["FY2026G"] / GROUP["FY2026G"][1]
GT_SHARE_BP26 = GT_BP26 / GROUP["FY2026G"][2]
ADS_SHARE_BP26 = BP26["ADS"] / GROUP["FY2026G"][2]
# What the price implies: for GTCC with the rest at my base; for ADS with GTCC at my base
GT_IMPLIED_EV = EV_ADJ - rest_ev(0)
GT_IMPLIED_MULT = GT_IMPLIED_EV / GT_BP27
ADS_IMPLIED_EV = EV_ADJ - SOTP_EV + SOTP["ADS"]
ADS_IMPLIED_MULT = ADS_IMPLIED_EV / ADS_BP27
GT_MULT_FOR_LONG = (PRICE * 1.15 * SHARES / 1000 - ADJ - rest_ev(0)) / GT_BP27

VALS, GTE = [], []
for s in SCEN:
    e = gt27(s[1], s[2])["bp"]
    GTE.append(e)
    VALS.append(value(e, s[3], s[4]))
WEIGHTED = sum(v * s[5] for v, s in zip(VALS, SCEN))
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75
SENS_GT[1] = GT_BP27
EV_BP26 = EV_ADJ / GROUP["FY2026G"][2]
EV_BP27 = EV_ADJ / BP27
PE_G26 = PRICE / EPS26G
PE_C26 = PRICE / CONS_EPS_26
PE_27 = PRICE / EPS27
OFF_HIGH = PRICE / HI_CLOSE - 1
YTD = PRICE / PX_DEC25 - 1
Q1_MOVE = PX_Q1_DAY / PX_Q1_PRE - 1
FY_MOVE = PX_FY_DAY / PX_FY_PRE - 1
MTBP_MOVE = PX_MTBP_DAY / PX_MTBP_PRE - 1
H1_MOVE = PX_H1_DAY / PX_H1_PRE - 1
GT_BTB25 = GT_ORD[3] / GT_REV[3]
GT_BTB_Q1 = GT_Q1_ORD[1] / GT_Q1_REV[1]
GT_BL_YEARS = GT_BACKLOG_FY25 / GT_REV[3]
ES_M_Q1 = Q1_BP["Energy"][1] / 536.3
ES_M26 = BP26["Energy"] / REV26["Energy"]
UNIT_BL_GROWTH = UNIT_BL[-1] / UNIT_BL[2] - 1

# ---- Price, month-end close (stockanalysis.com TYO:7011, split-adjusted, retrieved 2 Nov 2026) ----
PX_LABELS = ["Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24",
             "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25",
             "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26",
             "Aug 26", "Sep 26", "Oct 26", "2 Nov 26"]
PX = [826.8, 824.1, 994.2, 1182.5, 1448.5, 1417.5, 1368, 1723, 1830, 1942.5, 2117.5, 2193, 2197.5, 2223, 2296, 1987, 2526,
      2796.5, 3352, 3610, 3630, 3753, 3879, 4653, 3947, 3840, 4519, 5014, 4223, 4615, 3806, 3666, 3764, 3889, 3839, 3413,
      3363]

# ---- The call's tests ----
REVISIT_IF = ("A price below about ¥3,200, where my base value would sit 15 per cent above it, or a 2027 medium-term plan "
              "that dates the doubling of gas turbine output against fiscal 2024 to fiscal 2030 or earlier.")
WRONG_IF = ("The shares close above ¥4,200 or below ¥2,500 in October 2027, or MHI books fewer than 25 large frame gas "
            "turbines in fiscal 2026 against 35 a year earlier, or Energy Systems' fiscal 2026 business profit margin lands "
            "below 14 per cent against the 15.5 per cent forecast.")

if __name__ == "__main__":
    print(f"shares {SHARES:.3f}m mcap {MCAP:.1f} netcash {NETCASH:.1f} advbuild {ADV_BUILD:.1f} deduct {ADV_DEDUCT:.1f}")
    print(f"adj {ADJ:.1f} adj_full {ADJ_FULL:.1f} EVadj {EV_ADJ:.1f} EVsimple {EV_SIMPLE:.1f}")
    print(f"GT26 bp {GT_BP26:.1f}; Erest26 rev {EREST_REV26:.1f} bp {EREST_BP26:.1f} ({EREST_BP26 / EREST_REV26:.1%})")
    print("E27", {k: round(v, 1) for k, v in E27.items()}, "BP27", round(BP27, 1), "NI27", round(NI27, 1), "EPS27", round(EPS27, 2))
    print("SOTP", {k: round(v, 1) for k, v in SOTP.items()}, "EV", round(SOTP_EV, 1), "eq", round(EQUITY, 1))
    print(f"base {BASE_VALUE:.1f} {BASE_VALUE / PRICE - 1:+.1%}; full cash {BASE_FULLCASH:.1f} {BASE_FULLCASH / PRICE - 1:+.1%}")
    for s, v, e in zip(SCEN, VALS, GTE):
        print(s[0], round(e, 1), round(v, 0), f"{v / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.0f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.0f} short {REVISIT_SHORT:.0f}")
    grid = [[round(value(e, m)) for m in SENS_MULT] for e in SENS_GT]
    print("grid", grid, sum(v > PRICE for r in grid for v in r), sum(v >= PRICE * 1.15 for r in grid for v in r))
    print(f"shares: GT rev26 {GT_SHARE_REV26:.1%} DS rev26 {DS_SHARE_REV26:.1%} GT bp26 {GT_SHARE_BP26:.1%} ADS bp26 {ADS_SHARE_BP26:.1%}"
          f" GT sotp {GT_SHARE_SOTP:.1%} ADS sotp {ADS_SHARE_SOTP:.1%}")
    print(f"implied GT {GT_IMPLIED_EV:.0f} = {GT_IMPLIED_MULT:.1f}x; implied ADS {ADS_IMPLIED_EV:.0f} = {ADS_IMPLIED_MULT:.1f}x; GT for long {GT_MULT_FOR_LONG:.1f}")
    print(f"EV/BP 26 {EV_BP26:.1f} 27 {EV_BP27:.1f}; PE guide {PE_G26:.1f} cons {PE_C26:.1f} mine27 {PE_27:.1f}")
    print(f"off high {OFF_HIGH:.1%} ytd {YTD:.1%} Q1 {Q1_MOVE:+.1%} FY {FY_MOVE:+.1%} MTBP {MTBP_MOVE:+.1%} H1 {H1_MOVE:+.1%}")
    print(f"GT btb25 {GT_BTB25:.2f} q1 {GT_BTB_Q1:.2f} bl yrs {GT_BL_YEARS:.1f}; ES m q1 {ES_M_Q1:.1%} m26 {ES_M26:.1%}; unit bl growth {UNIT_BL_GROWTH:.1%}")
    import statistics
    for g in ["gas", "def", "jp"]:
        ps = [p for p in PEERS if p[5] == g]
        print(g, "median fwdPE", statistics.median(p[2] for p in ps), "EV/EBIT", statistics.median(p[3] for p in ps))
