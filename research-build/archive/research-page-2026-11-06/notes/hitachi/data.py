"""Hitachi, Ltd. (TSE: 6501) initiation, 22 Oct 2026. Single source of figures for charts, note and model.

Fiscal year ends 31 March: FY2025 = year to March 2026; FY2026 = year to March 2027; FY2027 = year to March 2028.
Sources (hitachi.com investor relations):
- Outline of Consolidated Financial Results for the First Quarter Ended June 30, 2026 (29 Jul 2026, 2026_1Qpre.pdf):
  segment revenue and adjusted EBITA, Q1 actual and the raised FY2026 forecast; Hitachi Energy in US$ (p23); orders and
  backlog (p17); balance sheet summary (p15); FX assumptions (p5, p19); share buybacks (p13, p19).
- Consolidated Financial Results for Q1 FY2026 (29 Jul 2026, 2026_1Q.pdf): balance sheet line items, 30 Jun 2026.
- Supplemental Material for Q1 FY2026 (29 Jul 2026, 2026_1Qsup.xlsx): segment tables by quarter, FY2025 restated,
  issued shares and treasury stock at 30 Jun 2026.
- Outline of Consolidated Financial Results for FY2025 (27 Apr 2026, 2025_Anpre.pdf): FY2025 actual, the April FY2026
  forecast, Hitachi Energy FY2025 actual and April FY2026 forecast in US$ (p25), Hitachi Energy orders and backlog (p8, p16).
- Outlines for Q2 FY2025 (30 Oct 2025), Q3 FY2025 (29 Jan 2026), Q1 FY2025 (31 Jul 2025) and FY2024 (28 Apr 2025):
  Hitachi Energy backlog and guidance history.
- Hitachi Investor Day 2026, Energy Business Strategy (Andreas Schierenbeck), 10 Jun 2026, and the Q&A summary.
- IR library page, hitachi.com/en/ir/library/fr/: Q2 FY2026 results on 28 Oct 2026, webcast 17:00 to 18:00 JST.
Prices: Yahoo Finance 6501.T (chart API and history pages), retrieved 22 Oct 2026; the API endpoint answered curl with
"Too Many Requests", so the same data was read through the history page and the chart endpoint in a browser fetch.
Consensus and peer multiples: stockanalysis.com, retrieved 22 Oct 2026. Everything marked MINE is my own estimate.
Yen billion unless stated.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-22"
COMPANY = "Hitachi"
SLUG = "hitachi"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/hitachi"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call (Tommy Lau, 22 Oct 2026). Rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",     # Tommy Lau's call, 22 Oct 2026
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Yahoo Finance 6501.T, retrieved 22 Oct 2026) ----
PRICE = 5840.0              # TSE close, 21 Oct 2026 (a record close)
PRICE_DATE = "21 October 2026"
HI_INTRA = 6039.0           # all-time intraday high, 10 Feb 2026
HI_CLOSE = 5840.0           # highest close, 21 Oct 2026
LO_CLOSE_26 = 4464.0        # lowest close of 2026, 31 Mar 2026
LO_CLOSE_52 = 4429.0        # 52-week lowest close, 23 Oct 2025
PX_DEC25 = 4902.0           # close, 30 Dec 2025
PX_FY_PRE, PX_FY_DAY = 5356.0, 5047.0      # closes 27 and 28 Apr 2026 (FY2025 results, 27 Apr)
PX_ID_PRE, PX_ID_DAY = 4784.0, 4655.0      # closes 10 and 11 Jun 2026 (Investor Day, 10 Jun)
PX_Q1_PRE, PX_Q1_DAY = 4957.0, 5255.0      # closes 29 and 30 Jul 2026 (Q1 results, 29 Jul)

# ---- Shares and balance sheet, 30 Jun 2026 (Q1 FY2026 results and supplement) ----
SHARES_ISSUED = 4535.560985  # m, including treasury stock
TREASURY = 64.552492         # m
SHARES = SHARES_ISSUED - TREASURY
CASH = 1504.496
DEBT = 1056.927              # short-term debt 61.089 + current portion of long-term debt 432.901 + long-term debt 562.937
EQUITY_METHOD = 615.565      # investments accounted for using the equity method, book value
SECURITIES = 513.273         # non-current investments in securities and other financial assets, book value
NCI = 189.101                # non-controlling interests, book value
PENSION = 233.475            # retirement and severance benefits liability
CONTRACT_LIAB = 3213.623     # contract liabilities, current
BUYBACK_FY26 = 550.0         # FY2026 buyback plan; 147.9 done in Q1
BUYBACK_Q1 = 147.9

# ---- Group: FY2025 actual (restated, supplement) and FY2026 forecast (raised 29 Jul 2026) ----
SEGS = ["DSS", "Energy", "Mobility", "CI", "Others", "Corporate"]
SEG_NAMES = {"DSS": "Digital Systems & Services", "Energy": "Energy", "Mobility": "Mobility",
             "CI": "Connective Industries", "Others": "Others", "Corporate": "Corporate items and eliminations"}
REV25 = {"DSS": 3068.3, "Energy": 3219.9, "Mobility": 1321.5, "CI": 3086.0, "Others": 531.0, "Corporate": -640.1}
EBITA25 = {"DSS": 477.1, "Energy": 416.0, "Mobility": 108.1, "CI": 340.3, "Others": 22.9, "Corporate": -53.1}
REV26 = {"DSS": 3220.0, "Energy": 4060.0, "Mobility": 1450.0, "CI": 3250.0, "Others": 500.0, "Corporate": -780.0}
EBITA26 = {"DSS": 508.0, "Energy": 576.0, "Mobility": 136.0, "CI": 385.0, "Others": 11.0, "Corporate": -96.0}
GROUP_REV25, GROUP_EBITA25 = 10586.7, 1311.4
GROUP_REV26, GROUP_EBITA26 = 11700.0, 1520.0
GROUP_REV26_APR, GROUP_EBITA26_APR = 11100.0, 1420.0
NI25, NI26 = 802.3, 900.0
EPS25, EPS26 = 176.76, 201.14
PG_REV25, PG_EBITA25 = 3005.6, 396.5         # Power Grids BU (incl. Hitachi Energy), FY2025
PG_REV26, PG_EBITA26 = 3783.5, 550.5         # Power Grids BU, FY2026 forecast
Q1_PG_ORDERS, Q1_PG_REV = 1871.6, 867.8     # Power Grids orders and revenue, Q1 FY2026
FX_USD26 = 160.0                             # Hitachi's assumed rate, Q2 to Q4 FY2026
FX_USD25 = 151.0                             # FY2025 actual average

# ---- Hitachi Energy, US$ billion ----
HE_YEARS = ["FY2024", "FY2025", "FY2026G"]
HE_REV = [15.7, 19.8, 23.65]
HE_EBITA = [1.74, 2.64, 3.50]
HE_MARGIN = [0.111, 0.134, 0.148]   # as Hitachi reports them
HE_REV26_APR, HE_EBITA26_APR = 23.2, 3.32   # April 2026 forecast
HE_GUIDE_HIST = [  # date, forecast for FY2025 revenue, adjusted EBITA margin
    ("28 Apr 2025", 18.0, 0.119), ("30 Oct 2025", 19.0, 0.132), ("29 Jan 2026", 19.7, 0.133), ("27 Apr 2026, actual", 19.8, 0.134)]
HE_TGT27 = dict(rev=26.0, m=0.15)            # Investor Day: FY2027 about $26bn, margin 15%+
HE_TGT30 = dict(rev=36.0, m_lo=0.16, m_hi=0.20, backlog=100.0)
HE_ORDERS = {"FY2024": 27.9, "FY2025": 32.8}
HE_Q1_REV26, HE_Q1_REV25 = 5.40, 4.41
HE_BL_LABELS = ["Mar 25", "Jun 25", "Sep 25", "Dec 25", "Mar 26", "Jun 26"]
HE_BL = [43.6, 47.6, 49.7, 56.7, 57.9, 63.6]
HE_TTM_JUN26 = HE_REV[1] - HE_Q1_REV25 + HE_Q1_REV26
RATIO_MAR25 = HE_BL[0] / HE_REV[0]
RATIO_MAR26 = HE_BL[4] / HE_REV[1]
RATIO_JUN26 = HE_BL[5] / HE_TTM_JUN26
RATIO_FY30 = HE_TGT30["backlog"] / HE_TGT30["rev"]
CLAIM_FLOOR = 2.5

# ---- Consensus and peers (stockanalysis.com, retrieved 22 Oct 2026) ----
CONS_EPS_26 = 216.65        # FY ending Mar 2027, average
CONS_TP = 6600.0            # 14 analysts, updated 17 Sep 2026; low 5,500, high 7,500
CONS_N = 14
FWD_PE_SA = 25.00
PEERS = [  # company, ticker, forward P/E, trailing EV/EBIT, what they make, group
    ("Hitachi", "TSE: 6501", 25.00, 19.33, "Grid equipment (Hitachi Energy), IT services, rail, industrial products", "self"),
    ("Siemens Energy", "ETR: ENR", 22.99, 27.91, "Grid technology, gas turbines, wind turbines", "grid"),
    ("ABB", "SWX: ABBN", 23.89, 24.46, "Electrification and automation equipment", "grid"),
    ("Schneider Electric", "EPA: SU", 20.55, 20.80, "Electrical distribution, automation, data centre power", "grid"),
    ("Eaton", "NYSE: ETN", 26.00, 31.83, "Switchgear and power distribution, data centre electrical", "grid"),
    ("Prysmian", "BIT: PRY", 19.84, 21.11, "High voltage and power cable", "grid"),
    ("Fujitsu", "TSE: 6702", 23.73, 17.37, "IT services and systems in Japan and abroad", "it"),
    ("NEC", "TSE: 6701", 23.50, 19.13, "IT services, network and public systems", "it"),
    ("Mitsubishi Electric", "TSE: 6503", 18.28, 19.09, "Factory automation, building systems, power equipment", "ind"),
    ("Alstom", "EPA: ALO", 9.50, 10.33, "Rolling stock and rail signalling", "rail"),
]

# ---- MY assumptions: FY2027 (year to March 2028) ----
HE_G27 = 0.12          # Hitachi Energy revenue growth in US$
HE_M27 = 0.155         # Hitachi Energy adjusted EBITA margin
FX27 = 160.0           # yen per US$, held at Hitachi's FY2026 assumption
EOTHER26 = EBITA26["Energy"] - HE_EBITA[2] * FX_USD26   # Energy segment less Hitachi Energy (Nuclear and items)
G27 = {"Eother": None, "DSS": 0.06, "CI": 0.05, "Mobility": 0.10, "Others": 0.0}
EOTHER27 = 20.0
CORP27 = -100.0
MULT = {"HE": 20, "Eother": 12, "DSS": 15, "CI": 15, "Mobility": 10, "Others": 8, "Corporate": 15}
SCEN = [  # name, HE growth, HE margin, HE multiple, other multiples delta, prob
    ("Bear", 0.08, 0.148, 14, -2, 0.25),
    ("Base", HE_G27, HE_M27, MULT["HE"], 0, 0.50),
    ("Bull", 0.15, 0.165, 25, 2, 0.25),
]
SENS_HE = [600.0, None, 720.0]   # middle row = model FY2027E Hitachi Energy EBITA, yen bn
SENS_MULT = [16, 20, 24]

# ---- Derived ----
MCAP = PRICE * SHARES / 1000
NETCASH = CASH - DEBT
ADJ = NETCASH + EQUITY_METHOD + SECURITIES - NCI - PENSION   # bridge from enterprise value to equity value
EV_ADJ = MCAP - ADJ
EV_SIMPLE = MCAP - NETCASH
HE_REV26_YEN = HE_REV[2] * FX_USD26
HE_EBITA26_YEN = HE_EBITA[2] * FX_USD26


def he27(g, m, fx=FX27):
    r = HE_REV[2] * (1 + g)
    return dict(rev=r, ebita_usd=r * m, ebita=r * m * fx)


B = he27(HE_G27, HE_M27)
HE_REV27, HE_EBITA27_USD, HE_EBITA27 = B["rev"], B["ebita_usd"], B["ebita"]
E27 = {
    "HE": HE_EBITA27,
    "Eother": EOTHER27,
    "DSS": EBITA26["DSS"] * (1 + G27["DSS"]),
    "CI": EBITA26["CI"] * (1 + G27["CI"]),
    "Mobility": EBITA26["Mobility"] * (1 + G27["Mobility"]),
    "Others": EBITA26["Others"] * (1 + G27["Others"]),
    "Corporate": CORP27,
}
GROUP_EBITA27 = sum(E27.values())
REST_KEYS = ["Eother", "DSS", "CI", "Mobility", "Others", "Corporate"]


def rest_ev(delta=0):
    return sum(E27[k] * (MULT[k] + delta) for k in REST_KEYS)


def value(he_ebita, he_mult, delta=0):
    return (he_ebita * he_mult + rest_ev(delta) + ADJ) / SHARES * 1000


SOTP = {k: E27[k] * MULT[k] for k in E27}
SOTP_EV = sum(SOTP.values())
BASE_VALUE = value(HE_EBITA27, MULT["HE"])
GROSS_POS = sum(v for v in SOTP.values() if v > 0)
HE_SHARE_SOTP_GROSS = SOTP["HE"] / GROSS_POS
HE_SHARE_SOTP_EQ = SOTP["HE"] / (SOTP_EV + ADJ)
HE_SHARE_REV26 = HE_REV26_YEN / GROUP_REV26
HE_SHARE_EBITA26 = HE_EBITA26_YEN / GROUP_EBITA26
SEG_POS26 = sum(EBITA26[k] for k in ["DSS", "Energy", "Mobility", "CI", "Others"])
HE_SHARE_EBITA26_SEG = HE_EBITA26_YEN / SEG_POS26
# What the price implies for Hitachi Energy, with the rest at my base multiples
HE_IMPLIED_EV = EV_ADJ - rest_ev(0)
HE_IMPLIED_MULT = HE_IMPLIED_EV / HE_EBITA27
HE_IMPLIED_USD = HE_IMPLIED_EV / FX27
HE_SHARE_MKT = HE_IMPLIED_EV / MCAP
HE_MULT_FOR_LONG = (PRICE * 1.15 * SHARES / 1000 - ADJ - rest_ev(0)) / HE_EBITA27

VALS, HEE = [], []
for s in SCEN:
    e = he27(s[1], s[2])["ebita"]
    HEE.append(e)
    VALS.append(value(e, s[3], s[4]))
WEIGHTED = sum(v * s[5] for v, s in zip(VALS, SCEN))
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75
SENS_HE[1] = HE_EBITA27
EV_EBITA26 = EV_ADJ / GROUP_EBITA26
EV_EBITA27 = EV_ADJ / GROUP_EBITA27
PE_G26 = PRICE / EPS26
PE_C26 = PRICE / CONS_EPS_26
RISE_DEC25 = PRICE / PX_DEC25 - 1
OFF_HIGH_INTRA = PRICE / HI_INTRA - 1
FY_MOVE = PX_FY_DAY / PX_FY_PRE - 1
ID_MOVE = PX_ID_DAY / PX_ID_PRE - 1
Q1_MOVE = PX_Q1_DAY / PX_Q1_PRE - 1
HE_GROWTH_25 = HE_REV[1] / HE_REV[0] - 1
HE_GROWTH_26 = HE_REV[2] / HE_REV[1] - 1
BTB25 = HE_ORDERS["FY2025"] / HE_REV[1]
BTB24 = HE_ORDERS["FY2024"] / HE_REV[0]
Q1_PG_BTB = Q1_PG_ORDERS / Q1_PG_REV

# ---- Price, month-end close (Yahoo Finance 6501.T, split-adjusted, retrieved 22 Oct 2026) ----
PX_LABELS = ["Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25",
             "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26",
             "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "21 Oct 26"]
PX = [2924, 3229, 3601, 3288, 3572, 3781, 3924, 3751, 3937, 3946, 3750, 3458, 3518, 4046, 4205, 4697, 4049, 3930, 5318,
      4968, 4902, 5361, 5226, 4464, 4882, 5166, 4471, 5267, 5438, 5489, 5840]

# ---- The call's tests (Tommy Lau, 22 Oct 2026) ----
REVISIT_IF = ("A price below about ¥5,600, where my base value would sit 15 per cent above it, or Hitachi raising its "
              "fiscal 2027 target for Hitachi Energy above US$28 billion of revenue at a 16 per cent adjusted EBITA margin.")
WRONG_IF = ("The shares close above ¥7,300 or below ¥4,400 in October 2027, or Hitachi Energy's fiscal 2026 adjusted "
            "EBITA margin lands below 14 per cent against the 14.8 per cent forecast, or its backlog falls below 2.5 times "
            "its revenue over the previous four quarters at two quarter ends in a row before October 2027.")

if __name__ == "__main__":
    print(f"shares {SHARES:.3f}m mcap {MCAP:.1f} netcash {NETCASH:.1f} adj {ADJ:.1f} EVadj {EV_ADJ:.1f} EVsimple {EV_SIMPLE:.1f}")
    print(f"HE26 yen rev {HE_REV26_YEN:.1f} ebita {HE_EBITA26_YEN:.1f}; Eother26 {EOTHER26:.1f}")
    print(f"HE27 rev ${HE_REV27:.2f}bn ebita ${HE_EBITA27_USD:.3f}bn = {HE_EBITA27:.1f}")
    print("E27", {k: round(v, 1) for k, v in E27.items()}, "group", round(GROUP_EBITA27, 1))
    print("SOTP", {k: round(v, 1) for k, v in SOTP.items()}, "EV", round(SOTP_EV, 1), "eq", round(SOTP_EV + ADJ, 1))
    print(f"base {BASE_VALUE:.1f} {BASE_VALUE / PRICE - 1:+.1%}")
    for s, v, e in zip(SCEN, VALS, HEE):
        print(s[0], round(e, 1), round(v, 0), f"{v / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.0f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.0f} short {REVISIT_SHORT:.0f}")
    print("grid", [[round(value(e, m)) for m in SENS_MULT] for e in SENS_HE],
          sum(value(e, m) > PRICE for e in SENS_HE for m in SENS_MULT),
          sum(value(e, m) >= PRICE * 1.15 for e in SENS_HE for m in SENS_MULT))
    print(f"HE share: rev26 {HE_SHARE_REV26:.1%} ebita26 {HE_SHARE_EBITA26:.1%} (segments {HE_SHARE_EBITA26_SEG:.1%}) "
          f"sotp gross {HE_SHARE_SOTP_GROSS:.1%} sotp eq {HE_SHARE_SOTP_EQ:.1%} mkt {HE_SHARE_MKT:.1%}")
    print(f"implied HE EV {HE_IMPLIED_EV:.0f} = {HE_IMPLIED_MULT:.1f}x = ${HE_IMPLIED_USD:.1f}bn; HE mult for long {HE_MULT_FOR_LONG:.1f}")
    print(f"EV/EBITA 26 {EV_EBITA26:.1f} 27 {EV_EBITA27:.1f}; PE guide {PE_G26:.1f} cons {PE_C26:.1f}")
    print(f"ratios mar25 {RATIO_MAR25:.2f} mar26 {RATIO_MAR26:.2f} jun26 {RATIO_JUN26:.2f} fy30 {RATIO_FY30:.2f}; ttm {HE_TTM_JUN26:.2f}")
    print(f"btb24 {BTB24:.2f} btb25 {BTB25:.2f} q1 PG {Q1_PG_BTB:.2f}; growth 25 {HE_GROWTH_25:.1%} 26 {HE_GROWTH_26:.1%}")
    print(f"rise dec {RISE_DEC25:.1%} off intra high {OFF_HIGH_INTRA:.1%} FY {FY_MOVE:+.1%} ID {ID_MOVE:+.1%} Q1 {Q1_MOVE:+.1%}")
    import statistics
    for g in ["grid", "it"]:
        ps = [p for p in PEERS if p[5] == g]
        print(g, "median fwdPE", statistics.median(p[2] for p in ps), "EV/EBIT", statistics.median(p[3] for p in ps))
