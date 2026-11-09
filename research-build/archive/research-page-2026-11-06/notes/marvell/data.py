"""Marvell Technology (Nasdaq: MRVL) initiation of 8 Oct 2026, rebuilt on the Investor Day of 6 Oct 2026. Single source of figures for charts, note and model.

Sources: Marvell quarterly results releases (Exhibit 99.1 to Form 8-K, EDGAR CIK 1835632): Q3 FY25 (3 Dec 2024),
Q4 FY25 (5 Mar 2025), Q1 FY26 (29 May 2025), Q2 FY26 (28 Aug 2025), Q3 FY26 (2 Dec 2025), Q4 FY26 (5 Mar 2026),
Q1 FY27 (27 May 2026), Q2 FY27 (27 Aug 2026), with their comparative columns. Form 10-K for FY2026 (filed 11 Mar 2026)
and FY2025 (filed 12 Mar 2025) for ten-largest-customer shares and capacity reservation commitments. Form 10-Q for the
quarter to 1 Aug 2026 (filed 28 Aug 2026) for shares outstanding, Celestial AI, contingent consideration, prepayments,
customers. Form 8-K of 31 Mar 2026 (Nvidia preferred), 15 Apr 2026 (2036 notes), 19 Aug 2026 (Google warrant).
Earnings calls: Q4 FY26 (5 Mar 2026), Q1 FY27 (27 May 2026), Q2 FY27 (27 Aug 2026), transcripts on stockanalysis.com.
Investor Day, New York, 6 Oct 2026: presentation deck on investor.marvell.com (slides 28, 33, 36 to 40, 122, 133, 140, 142),
and the transcript of the remarks on stockanalysis.com. No 8-K or press release on it had been filed by 8 Oct 2026.
Prices: Nasdaq.com historical data (Yahoo Finance chart API refused requests with "Too Many Requests" on 6 Oct 2026).
Consensus, average target and forward P/E: stockanalysis.com (S&P Global data, last updated 2 Oct 2026), retrieved
6 October 2026. Everything marked MINE is my own estimate.

Fiscal years end on the Saturday nearest 31 January: FY2026 = year to 31 Jan 2026; FY2027 = year to about 30 Jan 2027;
FY2028 = year to about 29 Jan 2028; FY2029 = year to about Jan 2029. Income figures are Marvell's NON-GAAP measures unless
marked GAAP. Marvell guides on non-GAAP.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-08"
DATE_LONG = "8 October 2026"
COMPANY = "Marvell"
NAME = "Marvell"
SLUG = "marvell"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/marvell"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT LONG",     # Tommy Lau's call, 8 Oct 2026
    direction="LONG",
    target=355.0,                   # US$ per share
    conviction="Medium",
    draft=False,
)

# ---- Market data (Nasdaq.com historical data to 5 Oct; stockanalysis.com for 6 and 7 Oct, retrieved 8 Oct 2026) ----
PRICE = 284.68          # Nasdaq close, 7 Oct 2026
PRICE_DATE = "7 October 2026"
PX_5OCT = 271.25        # close, 5 Oct 2026, the day before the Investor Day
PX_6OCT = 287.01        # close, 6 Oct 2026, Investor Day
PRICE_PIECE = 261.94    # close on 25 Sep 2026 (261.935), the last close before the journal piece (28 Sep 2026, 13:25 SGT)
HI52 = 329.88           # 52-week high, intraday, 18 Jun 2026
HI_CLOSE = 316.43       # highest close, 4 Jun 2026
LO52 = 70.69            # 52-week low, intraday, 5 Feb 2026 (70.685)
LO_CLOSE = 73.73        # lowest close, 4 Feb 2026
LO_JUL = 183.30         # close, 30 Jul 2026, the low after the June high
PRICE_DEC25 = 84.98     # close, 31 Dec 2025

# ---- Shares and balance sheet (Q2 FY27 release and 10-Q) ----
COMMON_OUT = 0.8769     # bn, 21 Aug 2026 (10-Q cover: 876.9 million)
PREF_ASCONV = 0.021778  # bn, Nvidia Series A preferred, as converted (8-K of 31 Mar 2026: up to 21,778,000 shares at about US$91.84)
PREF_USD = 2.0          # US$bn paid by Nvidia, 31 Mar 2026
PREF_CONV = 91.8355     # US$ conversion price
CASH = 3.9328           # US$bn, cash and equivalents, 1 Aug 2026
DEBT = 4.9629           # US$bn, long-term debt, 1 Aug 2026 (no short-term debt)
WARRANT_SH = 0.058970907    # bn, Google warrant, 8-K of 19 Aug 2026
WARRANT_PX = 206.58         # US$ exercise price
WARRANT_TRANCHE_USD = 0.5   # US$bn of Custom Products revenue per vesting tranche; 240 tranches = US$120bn
WARRANT_TRANCHES = 240
CELESTIAL_USD = 3.5337      # US$bn total purchase consideration (10-Q)
CELESTIAL_MAX_SH = 0.0224   # bn, maximum contingent shares; plus about US$233m cash
CONTINGENT_LIAB = 0.7495    # US$bn, contingent consideration liability, 1 Aug 2026
PREPAY_AUG = 0.4870         # US$bn, prepayments on supply capacity reservation agreements, 1 Aug 2026
PREPAY_JAN = 0.2788         # US$bn, same line, 31 Jan 2026
PREPAY_PLAN = 1.0           # US$bn, planned in FY27 (Q1 and Q2 FY27 calls)
SBC_Q2 = 0.3262             # US$bn, stock-based pay, Q2 FY27 (excluded from non-GAAP)
SBC_Q2_PY = 0.1536          # US$bn, Q2 FY26
SBC_26 = 0.5908             # US$bn, FY26
GAAP_EPS_H1 = 0.38          # US$, six months to 1 Aug 2026
NG_EPS_H1 = 1.75
TOP10 = (0.81, 0.82)        # ten largest customers, share of revenue, FY25 and FY26 (10-Ks)
DIST_A_Q2 = (0.34, 0.44)    # Distributor A share of revenue, Q2 FY26 and Q2 FY27 (10-Q)
CUST_A_Q2 = 0.16            # direct Customer A, Q2 FY27 (and Q2 FY26)

# ---- Consensus and peers (stockanalysis.com, S&P Global data updated 2 Oct 2026; retrieved 6 Oct 2026) ----
CONS_EPS_27 = 4.22      # FY27 non-GAAP EPS, 40 analysts, stockanalysis.com updated 7 Oct 2026
CONS_REV_27 = 12.07
CONS_EPS_28 = 6.75      # FY28, S&P Global data updated 2 Oct 2026, before the Investor Day
CONS_REV_28 = 18.18
CONS_TP = 335.83        # average target, 46 analysts (range 210 to 450), stockanalysis.com updated 7 Oct 2026
FWD_PE_SA = 50.43       # stockanalysis.com forward P/E for MRVL at the 7 Oct 2026 close
PEERS = [  # company, ticker, forward P/E, what they make
    ("Marvell", "Nasdaq: MRVL", 50.43, "Optical DSPs, TIAs and drivers, DCI modules, Ethernet switch chips, custom AI chips"),
    ("Astera Labs", "Nasdaq: ALAB", 69.94, "Retimers, PCIe and scale-up switches, smart cable modules"),
    ("Lumentum", "Nasdaq: LITE", 51.47, "Indium phosphide lasers, transceivers, optical circuit switches"),
    ("Coherent", "NYSE: COHR", 35.99, "Lasers, optical transceivers, materials"),
    ("Credo", "Nasdaq: CRDO", 30.78, "Active electrical cables, SerDes and optical DSPs"),
    ("Broadcom", "Nasdaq: AVGO", 20.92, "Switch chips, optical DSPs, custom AI chips"),
    ("Nvidia", "Nasdaq: NVDA", 19.75, "GPUs, NVLink, InfiniBand and Ethernet networking"),
]

# ---- Annual reported, non-GAAP unless marked, US$bn ----
YEARS_H = ["FY24", "FY25", "FY26"]
REV_H = [5.5077, 5.7673, 8.1946]
DC_H = [2.2167, 4.1642, 6.1003]
GM_H = [0.612, 0.610, 0.595]
OM_H = [0.290, 0.289, 0.353]
EPS_H = [1.51, 1.57, 2.84]
NI_H = [1.3101, 1.3773, 2.4656]
FY23_REV = 5.9196       # stockanalysis.com (FY2023 revenue 5.92bn); used only for FY24 growth

# ---- Quarterly (results releases), US$m; fiscal quarters ----
Q = ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26", "Q1 FY27", "Q2 FY27"]
QS = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26", "Q1 27", "Q2 27"]
Q_REV = [1160.9, 1272.9, 1516.1, 1817.4, 1895.3, 2006.1, 2074.5, 2218.7, 2417.8, 2739.3]
Q_DC = [816.4, 880.9, 1101.1, 1365.8, 1440.6, 1490.5, 1517.9, 1651.3, 1832.7, 2171.5]
Q_GM = [62.4, 61.9, 60.5, 60.1, 59.8, 59.4, 59.7, 59.0, 58.9, 58.9]
Q_OM = [23.3, 26.1, 29.7, 33.7, 34.2, 34.8, 36.3, 35.7, 35.0, 36.6]
Q_EPS = [0.24, 0.30, 0.43, 0.60, 0.62, 0.67, 0.76, 0.80, 0.80, 0.94]
Q27_ACT = dict(rev=(2.4178, 2.7393), opinc=(0.8469, 1.0032), ni=(0.7180, 0.8659), sh=(0.8933, 0.9212), eps=(0.80, 0.94),
               opex=(0.5769, 0.6108), gm=(0.589, 0.589))
GUIDE_Q3 = dict(rev=3.15, rev_band=0.05, gm=(0.575, 0.585), opex=0.655, other=-0.036, tax=0.11, sh=0.921, eps=(1.05, 1.15))
FY27_OUTLOOK = 12.0     # US$bn, "roughly $12 billion" (Q2 FY27 call)
FY28_PRIOR = 18.0       # US$bn, "approximately $18 billion" (Q2 FY27 call, 27 Aug 2026)
FY28_OUTLOOK = 20.0     # US$bn, FY28 updated revenue outlook, 67% growth (Investor Day deck, slide 33)
DC28_ID = 18.0          # US$bn, data centre about US$18bn in FY28, "pulled in one year early" (slide 36)
CUSTOM29_ID = 12.0      # US$bn, FY29 custom target US$12bn+, more than 3x FY28, was US$10bn (slide 28)
FY31_LO, FY31_HI, FY31_MID = 70.0, 90.0, 80.0   # US$bn revenue, FY31 (slide 39)
FY31_DC = (67.5, 87.5)  # US$bn data centre revenue, FY31 (slide 38)
FY31_SPLIT = dict(interconnect=37.5, custom=30.0, switch_storage=10.0, comms=2.5)   # US$bn at the FY31 midpoint (slide 40)
LT_GM = (0.56, 0.59)    # FY31 target model (slide 142)
LT_OM = (0.44, 0.46)
LT_TAX = 0.15
LT_FCF = 0.36           # free cash flow above 36% of revenue
LT_EPS = 30.0           # FY31 implied non-GAAP EPS above US$30
TAM_2030 = 400.0        # US$bn, CY30 Marvell TAM forecast (slide 41)
FY27_OPEX = 2.55        # US$bn non-GAAP opex guide (Q2 FY27 call)
FY28_TAX = 0.13         # non-GAAP tax rate guide for FY28 (Q2 FY27 call)
CUSTOM_26 = 1.5         # US$bn custom revenue FY26 (Q4 FY26 call)
SWITCH_26 = 0.3         # US$bn data centre switching FY26, "exceeding $300 million" (Q4 FY26 call)

# ---- Price, month-end close (Nasdaq.com historical data, retrieved 6 Oct 2026) ----
PX_LABELS = ['Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24', 'Sep 24', 'Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25', 'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26', '7 Oct 26']
PX = [54.13, 47.22, 55.73, 60.31, 67.7, 71.66, 70.88, 65.91, 68.81, 69.9, 66.98, 76.24, 72.12, 80.11, 92.69, 110.45, 112.86, 91.82, 61.57, 58.37, 60.19, 77.4, 80.37, 62.87, 84.07, 93.74, 89.4, 84.98, 78.92, 81.69, 99.05, 165.15, 205.0, 297.89, 187.56, 211.66, 264.21, 284.68]

# ---- MY assumptions ----
# FY27 second half: Q3 at the guide midpoints; Q4 is what the "roughly $12 billion" outlook leaves.
Q3_REV = GUIDE_Q3["rev"]
Q4_REV = round(FY27_OUTLOOK - sum(Q27_ACT["rev"]) - Q3_REV, 3)    # 3.693
H2_GM = 0.580           # non-GAAP gross margin, Q3 and Q4 (guide 57.5 to 58.5%; "same range" in FY28)
Q3_OPEX = GUIDE_Q3["opex"]
Q4_OPEX = round(FY27_OPEX - sum(Q27_ACT["opex"]) - Q3_OPEX, 4)    # 0.7073
OTHER_Q = GUIDE_Q3["other"]     # US$bn a quarter, non-GAAP interest and other
TAX27 = GUIDE_Q3["tax"]
SH_Q3, SH_Q4 = 0.921, 0.925
# FY28: the company outlook, mine for the margin build
REV28_IN = FY28_OUTLOOK
GM28 = 0.580
OPEX_G_RATIO = 0.5      # opex grows at half the rate of revenue (Q2 FY27 call)
OTHER28 = -0.14         # US$bn
TAX28 = FY28_TAX
SH28 = 0.930            # bn, MINE: Q3 guide 921m plus awards, warrant vesting and Celestial shares, net of buybacks
# FY29: valued twelve months out
OTHER29 = -0.12
TAX29 = 0.15            # the Investor Day long-term rate
SH29 = 0.940
BASE_PE = 33
#        name,  g29,  om29, multiple, prob
SCEN = [
    ("Bear", 0.00, 0.390, 22, 0.25),
    ("Base", 0.40, 0.430, BASE_PE, 0.50),
    ("Bull", 0.60, 0.450, 40, 0.25),
]
SENS_EPS = [8.50, None, 13.00]   # middle row = model FY29E
SENS_PE = [26, 33, 40]
# Data centre split, MINE except where disclosed (US$bn)
DC_SPLIT = {   # year: (custom, switching, interconnect and the rest)
    "FY26": (CUSTOM_26, SWITCH_26, None),
    "FY27E": (2.0, 0.65, None),
    "FY28E": (3.9, 1.5, None),
}
COMMS_27 = 2.25         # communications and other, FY27E (about 10% growth: Q2 FY27 call)
COMMS_28 = FY28_OUTLOOK - DC28_ID   # FY28E: total less the Investor Day data centre figure

# ---- FY2027E ----
Q3_OPINC = Q3_REV * H2_GM - Q3_OPEX
Q4_OPINC = Q4_REV * H2_GM - Q4_OPEX
Q3_NI = (Q3_OPINC + OTHER_Q) * (1 - TAX27)
Q4_NI = (Q4_OPINC + OTHER_Q) * (1 - TAX27)
Q3_EPS, Q4_EPS = Q3_NI / SH_Q3, Q4_NI / SH_Q4
REV27 = sum(Q27_ACT["rev"]) + Q3_REV + Q4_REV
OPINC27 = sum(Q27_ACT["opinc"]) + Q3_OPINC + Q4_OPINC
OM27 = OPINC27 / REV27
NI27 = sum(Q27_ACT["ni"]) + Q3_NI + Q4_NI
EPS27 = sum(Q27_ACT["eps"]) + Q3_EPS + Q4_EPS
OPEX27 = sum(Q27_ACT["opex"]) + Q3_OPEX + Q4_OPEX

# ---- FY2028E ----
G28 = REV28_IN / REV27 - 1
OPEX28 = OPEX27 * (1 + OPEX_G_RATIO * G28)
OPINC28 = REV28_IN * GM28 - OPEX28
OM28 = OPINC28 / REV28_IN
NI28 = (OPINC28 + OTHER28) * (1 - TAX28)
EPS28 = NI28 / SH28


def project(g29, om29):
    r29 = REV28_IN * (1 + g29)
    o29 = r29 * om29
    n29 = (o29 + OTHER29) * (1 - TAX29)
    return dict(r29=r29, o29=o29, n29=n29, eps29=n29 / SH29)


B = SCEN[1]
P = project(B[1], B[2])
REV29, EPS29 = P["r29"], P["eps29"]
VALS = [s[3] * project(s[1], s[2])["eps29"] for s in SCEN]
WEIGHTED = sum(v * s[4] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
SENS_EPS[1] = EPS29
REVISIT_LONG = BASE_VALUE / 1.15      # price at which my base case is 15% above
REVISIT_SHORT = BASE_VALUE / 0.75     # price at which my base case is 25% below
EPS_FOR_LONG = PRICE * 1.15 / BASE_PE
EPS_FOR_SHORT = PRICE * 0.75 / BASE_PE

# ---- Value, debt, multiples ----
SH_ASCONV = COMMON_OUT + PREF_ASCONV
MCAP = PRICE * COMMON_OUT
MCAP_FD = PRICE * SH_ASCONV
NETDEBT = DEBT - CASH
EV = MCAP_FD + NETDEBT
NVDA_STAKE = PREF_ASCONV * PRICE
NVDA_GAIN = PRICE / PREF_CONV - 1
WARRANT_NET = WARRANT_SH * (1 - WARRANT_PX / PRICE)      # treasury method if fully vested
WARRANT_REV = WARRANT_TRANCHE_USD * WARRANT_TRANCHES       # US$bn
PE27, PE28, PE29 = PRICE / EPS27, PRICE / EPS28, PRICE / EPS29
PEC27, PEC28 = PRICE / CONS_EPS_27, PRICE / CONS_EPS_28
PE26 = PRICE / EPS_H[2]
TTM_EPS = sum(Q_EPS[-4:])
RISE_LO = PRICE / LO_CLOSE - 1
RISE_DEC25 = PRICE / PRICE_DEC25 - 1
SINCE_PIECE = PRICE / PRICE_PIECE - 1
OFF_HIGH = PRICE / HI_CLOSE - 1
# What the price needs: FY29 EPS at the base multiple, and the revenue that needs at the base margin
NEED_EPS29 = PRICE / BASE_PE
NEED_OPINC29 = NEED_EPS29 * SH29 / (1 - TAX29) - OTHER29
NEED_REV29 = NEED_OPINC29 / B[2]
NEED_G29 = NEED_REV29 / REV28_IN - 1
# Data centre: FY27E and FY28E from the outlook
DC27 = REV27 - COMMS_27
DC28 = REV28_IN - COMMS_28
DC_G27, DC_G28 = DC27 / DC_H[2] - 1, DC28 / DC27 - 1
REST = {"FY26": DC_H[2] - CUSTOM_26 - SWITCH_26, "FY27E": DC27 - sum(DC_SPLIT["FY27E"][:2]), "FY28E": DC28 - sum(DC_SPLIT["FY28E"][:2])}
DCV = {"FY26": DC_H[2], "FY27E": DC27, "FY28E": DC28}
CUS = {k: v[0] for k, v in DC_SPLIT.items()}
SWI = {k: v[1] for k, v in DC_SPLIT.items()}
REST_G27 = REST["FY27E"] / REST["FY26"] - 1
REST_G28 = REST["FY28E"] / REST["FY27E"] - 1
CUS_SHARE_G27 = (CUS["FY27E"] - CUS["FY26"]) / (DC27 - DC_H[2])
CUS_SHARE_G28 = (CUS["FY28E"] - CUS["FY27E"]) / (DC28 - DC27)
REST_SHARE_G27 = (REST["FY27E"] - REST["FY26"]) / (DC27 - DC_H[2])
REST_SHARE_G28 = (REST["FY28E"] - REST["FY27E"]) / (DC28 - DC27)
DC_SHARE_Q2 = Q_DC[-1] / Q_REV[-1]
DC_SHARE_Q4FY26 = Q_DC[7] / Q_REV[7]
DC_G_Q2 = Q_DC[-1] / Q_DC[-5] - 1
SBC_PCT_Q2 = SBC_Q2 / Q27_ACT["rev"][1]

if __name__ == "__main__":
    print(f"Q3E opinc {Q3_OPINC:.3f} ({Q3_OPINC/Q3_REV:.1%}) EPS {Q3_EPS:.3f}; Q4E rev {Q4_REV:.3f} opex {Q4_OPEX:.4f} opinc {Q4_OPINC:.3f} ({Q4_OPINC/Q4_REV:.1%}) EPS {Q4_EPS:.3f}")
    print(f"FY27 rev {REV27:.3f} opinc {OPINC27:.3f} OM {OM27:.1%} NI {NI27:.3f} EPS {EPS27:.2f} (cons {CONS_EPS_27})")
    print(f"FY28 rev {REV28_IN} g {G28:.1%} opex {OPEX28:.3f} opinc {OPINC28:.3f} OM {OM28:.1%} NI {NI28:.3f} EPS {EPS28:.2f} (cons {CONS_EPS_28})")
    for s, v in zip(SCEN, VALS):
        p = project(s[1], s[2]); print(s[0], round(p["r29"], 2), round(p["eps29"], 2), round(v, 1), f"{v / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.0f} short {REVISIT_SHORT:.0f}; eps long {EPS_FOR_LONG:.2f} short {EPS_FOR_SHORT:.2f}")
    print("grid", [[round(e * m) for m in SENS_PE] for e in SENS_EPS], sum(e * m > PRICE for e in SENS_EPS for m in SENS_PE))
    print(f"PE 26 {PE26:.1f} 27 {PE27:.1f} 28 {PE28:.1f} 29 {PE29:.1f}; cons {PEC27:.1f} {PEC28:.1f}; ttm {PRICE/TTM_EPS:.1f}")
    print(f"need EPS29 {NEED_EPS29:.2f} rev {NEED_REV29:.2f} g {NEED_G29:.1%}")
    print(f"mcap {MCAP:.1f} fd {MCAP_FD:.1f} netdebt {NETDEBT:.3f} EV {EV:.1f}; nvda {NVDA_STAKE:.2f} gain {NVDA_GAIN:.1%}; warrant net {WARRANT_NET*1000:.1f}m rev {WARRANT_REV}")
    print(f"rise lo {RISE_LO:.1%} dec {RISE_DEC25:.1%} piece {SINCE_PIECE:.1%} offhigh {OFF_HIGH:.1%}")
    print(f"DC27 {DC27:.2f} g {DC_G27:.1%} DC28 {DC28:.2f} g {DC_G28:.1%}; rest {REST} g27 {REST_G27:.1%} g28 {REST_G28:.1%}")
    print(f"custom share of DC growth 27 {CUS_SHARE_G27:.1%} 28 {CUS_SHARE_G28:.1%}; rest share 27 {REST_SHARE_G27:.1%} 28 {REST_SHARE_G28:.1%}")
    print(f"DC share Q2 {DC_SHARE_Q2:.1%} Q4FY26 {DC_SHARE_Q4FY26:.1%} DC growth Q2 {DC_G_Q2:.1%}; SBC {SBC_PCT_Q2:.1%}")
    import statistics; print("peer median", statistics.median([p[2] for p in PEERS[1:]]))

# ---- The call's tests (Tommy Lau, 8 Oct 2026) ----
WRONG_IF = ("The shares close below US$230 by October 2027, or Marvell's fiscal 2028 revenue, the year to January 2028, "
            "comes in below US$18 billion.")
FY28_RAISE = FY28_OUTLOOK / FY28_PRIOR - 1
CUS28_MAX = CUSTOM29_ID / 3            # "more than 3x" FY28 implies FY28 custom below about US$4bn
FY29_PATH_ADD = CUSTOM29_ID - DC_SPLIT["FY28E"][0]   # what the custom target alone adds in FY29, on my FY28 custom
FY31_INT_SHARE = FY31_SPLIT["interconnect"] / FY31_MID
FY31_CUS_SHARE = FY31_SPLIT["custom"] / FY31_MID
ID_MOVE = PX_6OCT / PX_5OCT - 1
