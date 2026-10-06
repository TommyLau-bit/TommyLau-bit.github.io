"""Bloom Energy (NYSE: BE) initiation, draft of 6 Oct 2026. Single source of figures for charts, note and model.

Sources: Bloom quarterly results releases (Exhibit 99.1 to Form 8-K, EDGAR CIK 1664703, also on Bloom's IR CDN):
Q2 2024 (with Q1 2024), Q2 2025 (with Q1 2025), Q3 2025 (with Q3 2024), Q4 2025 (with Q4 2024 and full years),
Q2 2026 (with Q1 2026). Form 10-K for 2025 (backlog definitions, service contract terms, 2 GW plan, grid context).
Form 10-Q for Q2 2026 (convertible notes, Oracle warrant, EPS dilution, Brookfield JVs, customers, short report).
Bloom newsroom (Oracle 13 Apr 2026, Brookfield 30 Jun 2026, Power Connect 19 Aug 2026, Q3 2025 date notice
9 Oct 2025). AEP option exercise reported 8 Jan 2026. Yahoo Finance chart API (prices), stockanalysis.com
(multiples, target), Nasdaq.com / Zacks (consensus EPS), all retrieved 6 October 2026.
Everything marked MINE is my own estimate.

Income figures are Bloom's NON-GAAP measures unless marked GAAP. Bloom guides on non-GAAP.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-06"
DATE_LONG = "6 October 2026"
COMPANY = "BloomEnergy"
NAME = "Bloom Energy"
SLUG = "bloom-energy"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/bloom-energy"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Claude's draft view; Tommy decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",      # e.g. "INITIATE AT SHORT" once Tommy decides
    direction="NO CALL",
    target=None,                  # US$ per share; None for NO CALL
    conviction="Medium",
    draft=False,
)

# ---- Market data (Yahoo Finance chart API, retrieved 6 Oct 2026) ----
PRICE = 286.65          # NYSE close, 5 Oct 2026
PRICE_DATE = "5 October 2026"
PRICE_PIECE = 266.65    # close on 24 Sep 2026, the journal piece's date
HI52 = 351.28           # 52-week high, intraday 25 Jun 2026
HI_CLOSE = 345.85       # highest close, 22 Jun 2026
LO52 = 75.70            # 52-week low, intraday 17 Dec 2025
PRICE_DEC25 = 86.89     # month-end close, 31 Dec 2025
PX_ORCL = (176.67, 219.03)   # closes 13 and 14 Apr 2026 (Oracle expansion announced 13 Apr)
PX_SHORT = (269.57, 254.29)  # closes 7 and 8 Jul 2026 (short report, 8 Jul)
PX_Q2 = (166.84, 207.12)     # closes 28 Jul 2026 (results after the close) and 30 Jul 2026
SHARES_OUT = 0.294527   # bn, 22 Jul 2026 (10-Q cover)
CASH = 2.667            # US$bn, cash and equivalents, 30 Jun 2026 (excl. restricted 0.022)
DEBT = 2.530            # US$bn, debt principal, 30 Jun 2026 (0% 2030 notes 2.500, Green 2029 0.027, 2028 0.001, Korea loan 0.003)
FIN_OBLIG = 0.206       # US$bn, financing obligations (old sale-leasebacks), excluded from net cash
# Dilution (10-Q for Q2 2026)
CONV_2030 = 2.500; CONV_2030_PX = 194.97; CONV_2030_RATE = 5.1290   # US$bn, conversion price, shares per US$1,000
CONV_2030_SH = CONV_2030 * CONV_2030_RATE / 1000                     # bn shares, 12.82m
CONV_2030_MAX = 0.019554                                             # bn shares with full make-whole
CONV_2029 = 0.026971; CONV_2029_RATE = 47.9795
CONV_2029_SH = CONV_2029 * CONV_2029_RATE / 1000                     # bn shares, 1.29m
OPTIONS_Q2 = 0.016022   # bn, stock options and awards in Q2 2026 diluted count (treasury method)
DIL_Q2 = 0.323331; BASIC_Q2 = 0.287288
SBC_Q2 = 0.0564         # US$bn, stock-based compensation excluded from non-GAAP operating income, Q2 2026
ORCL_WARRANT = (3.531073, 113.28, 0.2516, 0.0723, 2.154231)  # m shares, strike, FV US$bn, inducement US$bn, m shares issued
CONV_TRIGGER_DAYS = 17  # of the last 30 Q3 trading days closing above 130% of US$194.97 (my count of Yahoo closes; 20 needed)
FULLY_DILUTED = SHARES_OUT + CONV_2030_SH + CONV_2029_SH + OPTIONS_Q2

# ---- Consensus and peers (retrieved 6 Oct 2026) ----
CONS_EPS_26 = 2.71      # stockanalysis.com, 25 analysts
CONS_EPS_27 = 4.33      # Nasdaq.com (Zacks), 6 estimates
CONS_EPS_28 = 7.00      # Nasdaq.com (Zacks), 2 estimates
CONS_Q3 = 0.57          # Nasdaq.com (Zacks), 4 estimates
CONS_REV_26 = 4.12      # stockanalysis.com
CONS_TP = 282.82        # stockanalysis.com average target, 29 analysts (median 303, range 97 to 390)
FWD_PE_SA = 83.47       # stockanalysis.com forward P/E for BE
PEERS = [  # company, ticker, forward P/E, what they make
    ("Bloom Energy", "NYSE: BE", 83.47, "Solid oxide fuel cell systems for on-site power, and their maintenance"),
    ("GE Vernova", "NYSE: GEV", 47.34, "Gas turbines, grid equipment and wind turbines"),
    ("Vertiv", "NYSE: VRT", 31.93, "Power and cooling equipment for data centres"),
    ("Caterpillar", "NYSE: CAT", 29.42, "Gas and diesel engine generators, plus construction and mining machines"),
    ("Siemens Energy", "Xetra: ENR", 24.48, "Gas turbines, grid equipment and wind turbines"),
    ("Cummins", "NYSE: CMI", 15.94, "Engines and generator sets"),
    ("FuelCell Energy", "Nasdaq: FCEL", None, "Carbonate and solid oxide fuel cells; loss-making, no forward P/E"),
]

# ---- Annual reported (Q4 2025 release), US$bn ----
YEARS_H = ["2024", "2025"]
REV_H = [1.4739, 2.0240]
PROD_H = [1.0852, 1.5313]; PROD_COST_H = [0.6858, 0.9928]
SERV_H = [0.2135, 0.2283]; SERV_COST_H = [0.2150, 0.2054]
GM_GAAP_H = [0.275, 0.290]; GM_H = [0.287, 0.303]   # non-GAAP
OPINC_H = [0.1076, 0.2210]; EPS_H = [0.28, 0.76]
RELATED_H = [0.3386, 0.8920]    # related-party revenue (2025: mainly Brookfield joint ventures)
OCF_25 = 0.1139

# ---- Quarterly (results releases), US$m ----
Q = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_REV = [235.3, 335.8, 330.4, 572.4, 326.0, 401.2, 519.0, 777.7, 751.1, 1065.4]
Q_PROD = [153.4, 226.3, 233.8, 471.7, 211.9, 296.6, 384.3, 638.5, 653.3, 935.4]
Q_PROD_COST = [115.8, 161.3, 155.1, 253.6, 139.6, 198.7, 249.8, 404.7, 429.2, 594.0]
Q_SERV = [56.5, 52.5, 50.8, 53.8, 53.5, 54.4, 58.6, 61.7, 61.9, 69.0]
Q_SERV_COST = [56.5, 52.4, 51.4, 54.7, 52.9, 49.4, 51.8, 51.3, 53.7, 56.1]
Q_GM_GAAP = [16.2, 20.4, 23.8, 38.3, 27.2, 26.7, 29.2, 30.8, 30.0, 33.4]
Q_GM = [17.5, 21.8, 25.2, 39.3, 28.7, 28.2, 30.4, 31.9, 31.5, 34.3]     # non-GAAP, %
Q_EPS = [-0.17, -0.06, -0.01, 0.43, 0.03, 0.10, 0.15, 0.45, 0.44, 0.78]  # non-GAAP diluted
Q_RELATED = [122.2, 86.8, 126.6, 3.0, 2.8, 27.1, 288.0, 574.2, 373.3, 2.8]
H1_26_REV = 1.8164; H1_26_GP = 0.6017; H1_26_OPEX = 0.2323; H1_26_OPINC = 0.3694
H1_26_NI = 0.3863; H1_26_EPS = 1.22
Q2_TOP2 = (0.44, 0.21)   # two customers' share of Q2 2026 revenue (10-Q)
GUIDE_26 = dict(rev=(3.9, 4.2), gm=0.34, opinc=(0.80, 0.90), eps=(2.55, 2.85))
GUIDE_26_FEB = dict(rev=(3.1, 3.3), eps=(1.33, 1.48))
BACKLOG_25 = (20.0, 6.0)   # US$bn total and product, end 2025; service by subtraction
CAPACITY_GW = (1.0, 2.0, 5.0)   # Fremont annual capacity: 2025, end-2026 plan, site room
AEP_DEAL = (2.65, 0.9)     # US$bn, GW: AEP's exercise of most of its 900 MW option, Jan 2026
ORCL_GW = (2.8, 1.2)       # up to, contracted (13 Apr 2026)
BROOKFIELD_BN = (5, 25)    # framework, Oct 2025 and 30 Jun 2026
TTM_EPS = sum(Q_EPS[-4:])

# ---- Share price, month-end close (Yahoo Finance, retrieved 6 Oct 2026) ----
PX_LABELS = ["Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24",
             "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25",
             "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26",
             "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
PX = [14.44, 14.80, 11.32, 8.77, 11.24, 11.13, 16.32, 12.24, 13.54, 11.91, 10.56, 9.60, 27.45, 22.21, 23.58,
      24.02, 19.66, 18.32, 18.47, 23.92, 37.39, 52.94, 84.57, 132.16, 109.24, 86.89, 151.37, 155.67, 135.49, 283.36,
      285.00, 302.70, 205.81, 206.30, 276.98, 286.65]

# ---- MY assumptions ----
Q3E_REV, Q4E_REV = 1.05, 1.20          # US$bn (H2 2.25 against the 2.08 to 2.38 the guide implies)
Q3E_GM, Q4E_GM = 0.345, 0.345          # non-GAAP gross margin (guide ~34% for the year; H1 33.1%)
Q3E_OPEX, Q4E_OPEX = 0.135, 0.145      # non-GAAP operating expenses, US$bn (Q2: 0.126)
OTHER_Q = 0.008                        # US$bn a quarter: adjusted net profit less non-GAAP operating income (Q1, Q2: about 0.008)
OTHER_Y = 0.035                        # US$bn a year, 2027 and 2028
TAX26, TAX27, TAX28 = 0.01, 0.10, 0.15 # non-GAAP tax rate; large losses carried forward keep it low for now
SBC_DIL = 0.015                        # net new shares a year from staff awards
SH26 = FULLY_DILUTED
SH27 = SH26 * (1 + SBC_DIL)
SH28 = SH27 * (1 + SBC_DIL)
PROD_SHARE = 0.875                     # product share of revenue (H1 2026: 87.5%)
USD_PER_MW = AEP_DEAL[0] / AEP_DEAL[1] # US$m per MW, AEP's order; my unit for converting revenue to megawatts
BASE_PE = 40
#        name,  g27,  g28,  gm27,  gm28,  opex27, opex28, multiple, prob
SCEN = [
    ("Bear", 0.30, 0.12, 0.330, 0.320, 0.58, 0.62, 25, 0.25),
    ("Base", 0.55, 0.38, 0.350, 0.355, 0.62, 0.75, BASE_PE, 0.50),
    ("Bull", 0.70, 0.50, 0.365, 0.375, 0.66, 0.82, 50, 0.25),
]
SENS_EPS = [4.50, None, 7.50]   # middle row = model 2028E
SENS_PE = [30, 40, 50]

# ---- 2026E ----
Q3E_OPINC = Q3E_REV * Q3E_GM - Q3E_OPEX
Q4E_OPINC = Q4E_REV * Q4E_GM - Q4E_OPEX
Q3E_NI = (Q3E_OPINC + OTHER_Q) * (1 - TAX26)
Q4E_NI = (Q4E_OPINC + OTHER_Q) * (1 - TAX26)
Q3E_EPS = Q3E_NI / SH26; Q4E_EPS = Q4E_NI / SH26
REV26 = H1_26_REV + Q3E_REV + Q4E_REV
GP26 = H1_26_GP + Q3E_REV * Q3E_GM + Q4E_REV * Q4E_GM
GM26 = GP26 / REV26
OPEX26 = H1_26_OPEX + Q3E_OPEX + Q4E_OPEX
OPINC26 = H1_26_OPINC + Q3E_OPINC + Q4E_OPINC
NI26 = H1_26_NI + Q3E_NI + Q4E_NI
EPS26 = H1_26_EPS + Q3E_EPS + Q4E_EPS


def project(g27, g28, gm27, gm28, ox27, ox28):
    r27 = REV26 * (1 + g27); r28 = r27 * (1 + g28)
    o27 = r27 * gm27 - ox27; o28 = r28 * gm28 - ox28
    n27 = (o27 + OTHER_Y) * (1 - TAX27); n28 = (o28 + OTHER_Y) * (1 - TAX28)
    return dict(r27=r27, r28=r28, o27=o27, o28=o28, n27=n27, n28=n28, eps27=n27 / SH27, eps28=n28 / SH28,
                om27=o27 / r27, om28=o28 / r28, gw28=r28 * PROD_SHARE / USD_PER_MW)


B = SCEN[1]
P = project(*B[1:7])
REV27, REV28, EPS27, EPS28 = P["r27"], P["r28"], P["eps27"], P["eps28"]
VALS = [s[7] * project(*s[1:7])["eps28"] for s in SCEN]
WEIGHTED = sum(v * s[8] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
SENS_EPS[1] = EPS28
REVISIT_LONG = BASE_VALUE / 1.15      # price at which my base case is 15% above
REVISIT_SHORT = BASE_VALUE / 0.75     # price at which my base case is 25% below

MCAP = PRICE * SHARES_OUT
NETCASH = CASH - DEBT
EV = MCAP - NETCASH
PE26, PE27, PE28 = PRICE / EPS26, PRICE / EPS27, PRICE / EPS28
PEC26, PEC27, PEC28 = PRICE / CONS_EPS_26, PRICE / CONS_EPS_27, PRICE / CONS_EPS_28
PE_GUIDE = PRICE / (sum(GUIDE_26["eps"]) / 2)
PE_TTM = PRICE / TTM_EPS
# The evidence: product margin against total margin
Q_PROD_GM = [(r - c) / r for r, c in zip(Q_PROD, Q_PROD_COST)]
Q_SERV_GM = [(r - c) / r for r, c in zip(Q_SERV, Q_SERV_COST)]
PROD_GM_H = [(r - c) / r for r, c in zip(PROD_H, PROD_COST_H)]
SERV_GM_H = [(r - c) / r for r, c in zip(SERV_H, SERV_COST_H)]
H1_26_PROD_GM = (Q_PROD[8] + Q_PROD[9] - Q_PROD_COST[8] - Q_PROD_COST[9]) / (Q_PROD[8] + Q_PROD[9])
REV_GROWTH_2Y = (Q_REV[-1] + Q_REV[-2]) / (Q_REV[0] + Q_REV[1]) - 1   # H1 2026 on H1 2024
RELATED_SHARE_25 = RELATED_H[1] / REV_H[1]
# What the price needs: 2028 EPS at the base multiple, and the revenue and megawatts that needs at base margins
NEED_EPS28 = PRICE / BASE_PE
NEED_OPINC28 = NEED_EPS28 * SH28 / (1 - TAX28) - OTHER_Y
NEED_REV28 = (NEED_OPINC28 + B[6]) / B[4]
NEED_GW28 = NEED_REV28 * PROD_SHARE / USD_PER_MW
BASE_GW28 = P["gw28"]
CAP_REV = CAPACITY_GW[1] * USD_PER_MW / PROD_SHARE   # revenue a 2 GW factory supports at AEP's price, US$bn
GW26 = REV26 * PROD_SHARE / USD_PER_MW
SERV_BACKLOG = BACKLOG_25[0] - BACKLOG_25[1]
CONV_DILUTION = (CONV_2030_SH + CONV_2029_SH) / SHARES_OUT

if __name__ == "__main__":
    print(f"2026E rev {REV26:.3f} GM {GM26:.3%} opinc {OPINC26:.3f} NI {NI26:.3f} EPS {EPS26:.2f} (Q3 {Q3E_EPS:.2f} Q4 {Q4E_EPS:.2f}) cons {CONS_EPS_26}")
    print(f"2027E rev {REV27:.2f} opm {P['om27']:.1%} EPS {EPS27:.2f} (cons {CONS_EPS_27}); 2028E rev {REV28:.2f} opm {P['om28']:.1%} EPS {EPS28:.2f} (cons {CONS_EPS_28})")
    print(f"shares out {SHARES_OUT*1000:.1f}m FD {SH26*1000:.1f}m 27 {SH27*1000:.1f} 28 {SH28*1000:.1f}; conv {CONV_2030_SH*1000:.2f}m + {CONV_2029_SH*1000:.2f}m = {CONV_DILUTION:.1%}")
    print(f"PE mine {PE26:.1f} {PE27:.1f} {PE28:.1f}; cons {PEC26:.1f} {PEC27:.1f} {PEC28:.1f}; guide {PE_GUIDE:.1f}; ttm {PE_TTM:.1f} ({TTM_EPS:.2f})")
    for s, v in zip(SCEN, VALS):
        p = project(*s[1:7]); print(s[0], round(p["r28"], 2), f"{p['om28']:.1%}", round(p["eps28"], 2), round(v, 1), f"{v / PRICE - 1:+.1%}", f"{p['gw28']:.2f}GW")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.0f} short {REVISIT_SHORT:.0f}")
    print("grid", [[round(e * m) for m in SENS_PE] for e in SENS_EPS])
    print(f"need EPS28 {NEED_EPS28:.2f} rev {NEED_REV28:.2f} GW {NEED_GW28:.2f}; base GW {BASE_GW28:.2f}; 2026 GW {GW26:.2f}; cap rev {CAP_REV:.2f}; $/MW {USD_PER_MW:.2f}")
    print(f"mcap {MCAP:.1f} netcash {NETCASH:.3f} EV {EV:.1f}; below high close {1 - PRICE / HI_CLOSE:.1%}; since Dec25 {PRICE / PRICE_DEC25 - 1:+.0%}")
    print("prod GM", [f"{x:.1%}" for x in Q_PROD_GM]); print("serv GM", [f"{x:.1%}" for x in Q_SERV_GM])
    print(f"prod GM yrs {[f'{x:.1%}' for x in PROD_GM_H]} H1 26 {H1_26_PROD_GM:.1%}; serv yrs {[f'{x:.1%}' for x in SERV_GM_H]}; rev growth 2y {REV_GROWTH_2Y:.0%}; related 25 {RELATED_SHARE_25:.0%}")
