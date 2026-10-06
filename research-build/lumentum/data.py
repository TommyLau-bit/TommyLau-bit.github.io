"""Lumentum (Nasdaq: LITE) initiation, draft of 6 Oct 2026. Single source of figures for charts, note and model.

Sources: Lumentum quarterly results releases (Exhibit 99.1 to Form 8-K, EDGAR CIK 1633978): Q4 FY24 (14 Aug 2024),
Q1 FY25 (7 Nov 2024) to Q4 FY26 (11 Aug 2026). Q4 FY26 earnings presentation (11 Aug 2026) for 200G EML share,
Q1 FY27 diluted share and tax guide. Form 10-K for FY2026 (filed 17 Aug 2026) for shares outstanding, convertible
notes, capped call, customer concentration, capex, Greensboro, Sagamihara. Form 8-K of 2 Mar 2026 (Nvidia preferred
stock). Coherent Form 8-K Exhibit 99.1 of 2 Mar 2026 (Nvidia's US$2bn in Coherent). Q4 FY26 earnings call
(11 Aug 2026) for supply, Japan fabs, Greensboro timing, repricing. Lumentum IR event list (Q1 FY27 call 5 Nov 2026).
Prices: Nasdaq.com historical data (Yahoo Finance chart API refused requests on 6 Oct 2026). Consensus:
stockanalysis.com (FY27, 23 analysts) and Nasdaq.com / Zacks (FY27, FY28). Peer forward P/E: stockanalysis.com.
All retrieved 6 October 2026. Everything marked MINE is my own estimate.

Fiscal years end late June / early July: FY2026 = year to 27 June 2026; FY2027 = year to June 2027; FY2028 = year to
June 2028. Income figures are Lumentum's NON-GAAP measures unless marked GAAP. Lumentum guides on non-GAAP.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-06"
DATE_LONG = "6 October 2026"
COMPANY = "Lumentum"
NAME = "Lumentum"
SLUG = "lumentum"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/lumentum"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",       # e.g. "INITIATE AT NO CALL" once Tommy decides
    direction="NO CALL",
    target=None,                    # US$ per share; None for NO CALL
    conviction="Medium",
    draft=False,
)

# ---- Market data (Nasdaq.com historical data, retrieved 6 Oct 2026) ----
PRICE = 1091.67         # Nasdaq close, 5 Oct 2026
PRICE_DATE = "5 October 2026"
PRICE_PIECE = 1085.42   # close on 2 Oct 2026, the last close before the journal piece (5 Oct 2026, 14:01 SGT)
HI52 = 1124.40          # 52-week high, intraday 5 Oct 2026
HI_CLOSE = 1091.67      # highest close, 5 Oct 2026
LO52 = 147.81           # 52-week low, intraday 10 Oct 2025
LO_CLOSE = 149.61       # lowest close, 10 Oct 2025
PRICE_DEC25 = 368.59    # close, 31 Dec 2025
PX_NVDA = (700.91, 783.25, 694.43)   # closes 27 Feb, 2 Mar, 3 Mar 2026 (Nvidia deal announced 2 Mar, before the open)
PX_Q4 = (820.59, 932.47)             # closes 11 Aug 2026 (results after the close) and 12 Aug 2026

# ---- Shares and balance sheet (Form 10-K for FY2026; Q4 FY26 release) ----
COMMON_OUT = 0.0897     # bn, 14 Aug 2026 (10-K cover)
PREF = 0.002876415      # bn, Series A convertible preferred held by Nvidia, converts one for one
PREF_PX = 695.31        # US$ per preferred share paid by Nvidia, 2 Mar 2026
PREF_USD = 2.0          # US$bn
CASH = 2.7384           # US$bn, cash and short-term investments, 27 Jun 2026
NOTES = [               # name, principal US$bn at 27 Jun 2026, conversion price US$
    ("2032 notes, 0.375%", 1.2650, 187.77),
    ("2029 notes, 1.50%", 0.0549, 69.54),
    ("2028 notes, 0.50%", 0.1796, 131.03),
    ("2026 notes, 0.50%", 0.0548, 99.29),
]
CAP_PRICE = 268.24      # 2032 capped call cap, US$
JAPAN_LOANS = 0.0928    # US$bn, SMBC and Mizuho term loans
EARLY_CONV = 0.7578     # US$bn principal of early conversion requests received by 14 Aug 2026 (cash for principal)
AWARDS = 0.0031         # bn, staff awards in Q4 FY26 non-GAAP diluted count (treasury method)
SH_GUIDE = 0.102        # bn, Q1 FY27 non-GAAP diluted share guide
TAX_GUIDE = 0.165       # non-GAAP tax rate guide
SBC_26 = 0.1913         # US$bn, stock-based pay and related payroll tax excluded from non-GAAP, FY2026
CAPEX_26 = 0.4513       # US$bn, FY2026
OCF_26 = 0.7514         # US$bn, FY2026
CUST_A, CUST_B = 0.266, 0.150   # shares of FY2026 revenue (10-K)
LOSS_EXTING = 7.7566    # US$bn, non-cash loss on debt extinguishment, Q4 FY26 (GAAP)
GAAP_EPS_Q4 = -84.65

# ---- Consensus and peers (retrieved 6 Oct 2026) ----
CONS_EPS_27 = 21.74     # stockanalysis.com, 23 analysts
CONS_REV_27 = 6.33      # stockanalysis.com
CONS_EPS_27_Z = 19.78   # Nasdaq.com (Zacks), 8 estimates
CONS_EPS_28 = 32.96     # Nasdaq.com (Zacks), 6 estimates (range 23.24 to 36.80)
CONS_Q1 = 3.82          # Nasdaq.com (Zacks), Sep 2026 quarter, 6 estimates (below the company's own guide)
CONS_TP = 1157          # stockanalysis.com average target, 26 analysts (median 1,168; range 820 to 1,400)
FWD_PE_SA = 51.01       # stockanalysis.com forward P/E for LITE
PEERS = [  # company, ticker, forward P/E, what they make
    ("Lumentum", "Nasdaq: LITE", 51.01, "Indium phosphide lasers (EML, CW), transceivers, optical circuit switches, industrial lasers"),
    ("Applied Optoelectronics", "Nasdaq: AAOI", 55.25, "Lasers and transceivers for data centres and cable networks"),
    ("Ciena", "NYSE: CIEN", 40.80, "Optical networking systems and coherent modules"),
    ("Coherent", "NYSE: COHR", 35.46, "Indium phosphide and other lasers, transceivers, materials"),
    ("Fabrinet", "NYSE: FN", 26.38, "Contract assembly of optical modules"),
    ("Broadcom", "Nasdaq: AVGO", 20.92, "Networking chips, custom AI chips, EML and VCSEL lasers"),
]

# ---- Annual reported, non-GAAP unless marked (FY24 as recast in the Q4 FY25 release), US$bn ----
YEARS_H = ["FY24", "FY25", "FY26"]
REV_H = [1.3592, 1.6450, 3.0140]
GM_GAAP_H = [0.185, 0.280, 0.417]
GM_H = [0.302, 0.347, 0.460]
OM_H = [-0.006, 0.097, 0.298]
OPINC_H = [-0.0082, 0.1601, 0.8970]
EPS_H = [0.44, 2.06, 8.67]
SH_H = [None, 0.0712, 0.0902]
FY23_REV = 1.7670

# ---- Quarterly (results releases), US$m ----
Q = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26"]   # fiscal quarters; Q4 26 = to 27 Jun 2026
Q_REV = [336.9, 402.2, 425.2, 480.7, 533.8, 665.5, 808.4, 1006.3]
Q_COMP = [231.4, 263.7, 300.8, 320.4, 379.2, 443.7, 533.3, 649.4]
Q_SYS = [105.5, 138.5, 124.4, 160.3, 154.6, 221.8, 275.1, 356.9]
Q_GM_GAAP = [23.1, 24.8, 28.8, 33.3, 34.0, 36.1, 44.2, 47.4]
Q_GM = [32.8, 32.3, 35.2, 37.8, 39.4, 42.5, 47.9, 50.4]
Q_OM = [3.0, 7.9, 10.8, 15.0, 18.7, 25.2, 32.2, 36.6]
Q_EPS = [0.18, 0.42, 0.57, 0.88, 1.10, 1.67, 2.37, 3.23]
Q_SH = [69.1, 71.6, 72.2, 72.0, 78.3, 86.1, 95.2, 101.1]
Q4_OPINC, Q4_OTHER, Q4_NI = 0.3688, 0.0220, 0.3263
GUIDE_Q1 = dict(rev=(1.225, 1.275), om=(0.395, 0.405), eps=(4.05, 4.35))
EML_200G_SHARE = 0.25   # more than 25% of EML revenue, Q4 FY26
GREENSBORO_USD = 0.038  # US$bn paid, 17 Mar 2026

# ---- Share price, month-end close (Nasdaq.com historical data, retrieved 6 Oct 2026) ----
PX_LABELS = ['Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24', 'Sep 24', 'Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25', 'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26', '5 Oct 26']
PX = [45.18, 39.21, 42.8, 52.42, 54.94, 48.47, 47.35, 43.76, 43.5, 50.92, 51.78, 57.61, 63.38, 63.87, 86.97, 83.95, 85.06, 70.33, 62.34, 59.04, 72.28, 95.06, 110.08, 132.81, 162.71, 201.56, 325.16, 368.59, 391.84, 700.91, 702.76, 902.32, 854.96, 858.06, 713.94, 914.76, 971.26, 1091.67]

# ---- MY assumptions (FY2027 by quarter; FY2028 by case) ----
Q27_REV = [1.26, 1.44, 1.62, 1.80]          # US$bn, Q1 within the 1.225 to 1.275 guide
Q27_OM = [0.400, 0.410, 0.415, 0.420]       # non-GAAP operating margin; Q1 guide 39.5 to 40.5%
OTHER_Q = 0.015         # US$bn a quarter of non-GAAP other income (Q4 FY26: 0.022; cash falls with note conversions)
OTHER_Y = 0.060         # US$bn a year, FY2028
TAX = TAX_GUIDE
SH27 = SH_GUIDE         # FY2027 diluted shares: the company's Q1 guide
SH_DIL = 0.01           # net new shares a year from awards and notes, MINE
SH28 = SH27 * (1 + SH_DIL)
BASE_PE = 35
#        name,  g28,  om28, multiple, prob
SCEN = [
    ("Bear", 0.10, 0.330, 22, 0.25),
    ("Base", 0.35, 0.415, BASE_PE, 0.50),
    ("Bull", 0.55, 0.450, 42, 0.25),
]
SENS_EPS = [22.00, None, 35.00]   # middle row = model FY2028E
SENS_PE = [28, 35, 42]

# ---- FY2027E ----
Q27_OPINC = [r * m for r, m in zip(Q27_REV, Q27_OM)]
Q27_NI = [(o + OTHER_Q) * (1 - TAX) for o in Q27_OPINC]
Q27_EPS = [n / SH27 for n in Q27_NI]
REV27 = sum(Q27_REV)
OPINC27 = sum(Q27_OPINC)
OM27 = OPINC27 / REV27
NI27 = sum(Q27_NI)
EPS27 = sum(Q27_EPS)


def project(g28, om28):
    r28 = REV27 * (1 + g28)
    o28 = r28 * om28
    n28 = (o28 + OTHER_Y) * (1 - TAX)
    return dict(r28=r28, o28=o28, n28=n28, eps28=n28 / SH28)


B = SCEN[1]
P = project(B[1], B[2])
REV28, EPS28 = P["r28"], P["eps28"]
VALS = [s[3] * project(s[1], s[2])["eps28"] for s in SCEN]
WEIGHTED = sum(v * s[4] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
SENS_EPS[1] = EPS28
REVISIT_LONG = BASE_VALUE / 1.15      # price at which my base case is 15% above
REVISIT_SHORT = BASE_VALUE / 0.75     # price at which my base case is 25% below

# ---- Shares, value, debt ----
BASIC_PLUS_PREF = COMMON_OUT + PREF
NOTE_SH = [p / c * (1 - c / PRICE) for _, p, c in NOTES]          # net shares at PRICE, principal paid in cash
CAPCALL_SH = NOTES[0][1] / NOTES[0][2] * (1 - NOTES[0][2] / CAP_PRICE)   # shares the capped call offsets
FD_NOW = BASIC_PLUS_PREF + sum(NOTE_SH) - CAPCALL_SH + AWARDS
NOTES_PRINC = sum(p for _, p, _ in NOTES)
DEBT = NOTES_PRINC + JAPAN_LOANS
NETCASH = CASH - DEBT
MCAP = PRICE * COMMON_OUT
MCAP_FD = PRICE * BASIC_PLUS_PREF
EV = MCAP_FD - NETCASH
NVDA_STAKE = PREF * PRICE                 # US$bn
NVDA_GAIN = PRICE / PREF_PX - 1
PE27, PE28 = PRICE / EPS27, PRICE / EPS28
PEC27, PEC28 = PRICE / CONS_EPS_27, PRICE / CONS_EPS_28
TTM_EPS = sum(Q_EPS[-4:])
PE_TTM = PRICE / TTM_EPS
PE_RUNRATE = PRICE / (4 * sum(GUIDE_Q1["eps"]) / 2)
RISE_YEAR = PRICE / LO_CLOSE - 1
RISE_DEC25 = PRICE / PRICE_DEC25 - 1
# What the price needs: FY2028 EPS at the base multiple, and the revenue that needs at the base margin
NEED_EPS28 = PRICE / BASE_PE
NEED_OPINC28 = NEED_EPS28 * SH28 / (1 - TAX) - OTHER_Y
NEED_REV28 = NEED_OPINC28 / B[2]
NEED_G28 = NEED_REV28 / REV27 - 1
NEED_X26 = NEED_REV28 / REV_H[2]
# What consensus FY2028 needs at the base margin
CONS28_REV = (CONS_EPS_28 * SH28 / (1 - TAX) - OTHER_Y) / B[2]
# Margin and growth facts
GM_GAAP_UP = Q_GM_GAAP[-1] - Q_GM_GAAP[3]
REV_Q4_GROWTH = Q_REV[-1] / Q_REV[3] - 1
COMP_Q4_GROWTH = Q_COMP[-1] / Q_COMP[3] - 1
SYS_Q4_GROWTH = Q_SYS[-1] / Q_SYS[3] - 1
FY24_DROP = REV_H[0] / FY23_REV - 1
FCF_26 = OCF_26 - CAPEX_26

if __name__ == "__main__":
    print("Q27 EPS", [round(x, 2) for x in Q27_EPS], f"FY27 rev {REV27:.2f} OM {OM27:.1%} NI {NI27:.3f} EPS {EPS27:.2f} (cons {CONS_EPS_27}, Zacks {CONS_EPS_27_Z})")
    print(f"FY28 rev {REV28:.2f} EPS {EPS28:.2f} (cons {CONS_EPS_28}); SH27 {SH27*1000:.1f} SH28 {SH28*1000:.1f}; FD now {FD_NOW*1000:.1f}")
    print("note shares m", [round(x * 1000, 2) for x in NOTE_SH], "capcall", round(CAPCALL_SH * 1000, 2))
    for s, v in zip(SCEN, VALS):
        p = project(s[1], s[2]); print(s[0], round(p["r28"], 2), round(p["eps28"], 2), round(v, 1), f"{v / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.0f} short {REVISIT_SHORT:.0f}")
    print("grid", [[round(e * m) for m in SENS_PE] for e in SENS_EPS])
    print(f"PE mine 27 {PE27:.1f} 28 {PE28:.1f}; cons {PEC27:.1f} {PEC28:.1f}; ttm {PE_TTM:.1f} ({TTM_EPS:.2f}); Q1 run-rate {PE_RUNRATE:.1f}")
    print(f"need EPS28 {NEED_EPS28:.2f} rev {NEED_REV28:.2f} g28 {NEED_G28:.1%} x FY26 {NEED_X26:.2f}; consensus rev at base margin {CONS28_REV:.2f}")
    print(f"mcap {MCAP:.1f} mcap incl pref {MCAP_FD:.1f} netcash {NETCASH:.3f} EV {EV:.1f}; Nvidia stake {NVDA_STAKE:.2f} gain {NVDA_GAIN:.1%}")
    print(f"rise yr {RISE_YEAR:.1%} since Dec {RISE_DEC25:.1%}; GM up {GM_GAAP_UP:.1f}; growth Q4 {REV_Q4_GROWTH:.1%} comp {COMP_Q4_GROWTH:.1%} sys {SYS_Q4_GROWTH:.1%}; FY24 {FY24_DROP:.1%}; FCF {FCF_26:.3f}")
