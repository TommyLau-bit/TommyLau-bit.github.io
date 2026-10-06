"""Corning (NYSE: GLW) initiation, draft of 6 Oct 2026. Single source of figures for charts, note and model.

Sources: Corning quarterly earnings releases (Exhibit 99 to Form 8-K, EDGAR CIK 24741), Form 10-K for 2025
(12 Feb 2026), Form 10-Q for Q2 2026 (29 Jul 2026), 8-K of 6 May 2026 (NVIDIA warrants) and its press release,
8-K and prospectus supplement of 11 Sep 2026 (US$2bn at-the-market programme), Corning IR events feed (Q3 date),
Yahoo Finance chart API (prices), stockanalysis.com (multiples, target), Nasdaq.com / Zacks (consensus EPS),
all retrieved 6 October 2026. Everything marked MINE is my own estimate.

All income figures are Corning's CORE (non-GAAP) measures unless marked GAAP. Corning guides on core.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-06"
DATE_LONG = "6 October 2026"
COMPANY = "Corning"
NAME = "Corning"
SLUG = "corning"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/corning"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Claude's draft view; Tommy decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",      # e.g. "INITIATE AT LONG" once Tommy decides
    direction="NO CALL",
    target=None,                  # US$ per share; None for NO CALL
    conviction="Medium",
    draft=False,
)

# ---- Market data (Yahoo Finance chart API, retrieved 6 Oct 2026) ----
PRICE = 159.37          # NYSE close, 5 Oct 2026
PRICE_DATE = "5 October 2026"
PRICE_1OCT = 160.42     # close on 1 Oct 2026, the journal piece's date
HI52 = 271.78           # 52-week high, intraday 30 Jun 2026 (Yahoo daily data)
HI_CLOSE = 255.69       # highest close, 29 Jun 2026
LO52 = 77.39            # 52-week low
PRICE_SEP25 = 82.03     # month-end close, 30 Sep 2025
PRICE_DEC24 = 47.52     # month-end close, 31 Dec 2024
ATM_PRE = 166.40        # close on 11 Sep 2026, the day the ATM was filed (stockanalysis.com daily history)
ATM_POST = 143.60       # close on 14 Sep 2026
DPS_Q = 0.28            # quarterly dividend
SHARES_OUT = 0.861388   # bn, shares outstanding 24 Jul 2026 (prospectus supplement)
DILUTED = 0.875         # bn, Q2 2026 weighted diluted shares, incl. the 3m pre-funded NVIDIA warrant
CASH = 2.504            # US$bn, 30 Jun 2026
DEBT = 8.424            # US$bn, 30 Jun 2026: long-term 7.756 + current 0.668
DEBT_DUE_1Y = 0.668     # US$bn current portion and short-term borrowings
EQUITY = 13.127         # total equity, 30 Jun 2026
LEVERAGE_COV = (0.39, 0.60)   # debt to capital, actual and covenant maximum (10-Q)

# ---- Capital raising and customer money ----
ATM = 2.0               # US$bn at-the-market programme, Goldman Sachs, 11 Sep 2026; 1% commission
ATM_SHARES = ATM / PRICE        # bn shares if fully sold at today's price
NV_PF_CASH = 0.500      # US$bn NVIDIA paid for a pre-funded warrant over 3m shares (6 May 2026)
NV_WARRANT_N = 0.015    # bn shares, traditional warrant at US$180, issued for no separate consideration
NV_WARRANT_K = 180.0
NV_WARRANT_FV = 0.296   # US$bn grant-date fair value, booked as consideration payable to a customer
DEPOSIT_Q2 = 1.0        # US$bn customer deposit, long-term supply agreement to 31 Dec 2029 (10-Q Note 2)
CONTRACT_LIAB = (2.3, 2.7)    # US$bn, 31 Dec 2025 and 30 Jun 2026
CAPEX_GUIDE_26 = 2.0    # US$bn, "approximately" (10-Q)
SDC_LOCKED = 0.058      # bn Corning shares held by Samsung Display under a lock-up expiring in 2027
SDC_TRANCHE = 0.022     # bn shares SDC can offer to Corning in tranches, 2024 to 2027
BUYBACK_LEFT = 3.0      # US$bn remaining on the 2019 authorisation

# ---- Consensus and peers (retrieved 6 Oct 2026) ----
CONS_EPS_26 = 3.28      # Nasdaq.com (Zacks), 8 estimates; same on stockanalysis.com
CONS_EPS_27 = 4.29      # Nasdaq.com (Zacks), 8 estimates
CONS_EPS_28 = 5.64      # Nasdaq.com (Zacks), 4 estimates
CONS_Q3 = 0.88          # Nasdaq.com (Zacks), 4 estimates
FWD_PE_SA = 43.03       # stockanalysis.com forward P/E for GLW
TRAIL_PE_SA = 73.52     # stockanalysis.com trailing P/E (GAAP)
CONS_TP = 189.94        # stockanalysis.com average target, 17 analysts
PEERS = [  # company, ticker, forward P/E, what they make
    ("Corning", "NYSE: GLW", 43.03, "Optical fibre, cable and connectivity, plus display, phone, car and solar materials"),
    ("Prysmian", "Milan: PRY", 23.48, "Power and telecom cable, including optical fibre and cable"),
    ("Fujikura", "Tokyo: 5803", 28.92, "Optical fibre, high-count cable and connectors"),
    ("Sumitomo Electric", "Tokyo: 5802", 21.43, "Wire, cable and optical fibre, plus car wiring"),
    ("Amphenol", "NYSE: APH", 29.43, "Connectors and cable assemblies, including for AI racks"),
    ("Ciena", "NYSE: CIEN", 37.51, "Optical networking systems"),
    ("Coherent", "NYSE: COHR", 35.42, "Optical transceivers, lasers and materials"),
    ("Lumentum", "Nasdaq: LITE", 50.12, "Lasers and optical transceivers"),
]

# ---- Annual reported, core basis (Q4 releases), US$bn ----
YEARS_H = ["2023", "2024", "2025"]
SALES_H = [13.580, 14.469, 16.408]       # core sales
OPT_H = [4.012, 4.657, 6.274]            # Optical Communications segment sales
OPT_NI_H = [0.478, 0.612, 1.048]         # Optical Communications segment net income
ENT_H = [1.326, 1.979, 3.195]            # Enterprise network sales (10-K product lines)
CAR_H = [2.686, 2.678, 3.079]            # Carrier network sales
CORE_NI_H = [1.463, 1.699, 2.199]
EPS_H = [1.70, 1.96, 2.52]               # core EPS
OPM_H = [0.165, 0.175, 0.193]            # core operating margin
CAPEX_H = [1.390, 0.965, 1.282]
FCF_H = [0.880, 1.253, 1.717]            # adjusted free cash flow (Corning definition)
DIV_H = [0.989, 0.986, 0.999]
DEP_FLOW_H = [-0.042, -0.006, 0.268]  # cash flow line 'customer deposits and government incentives'
SEG_NI_25 = 2.721                        # segment net income incl. Hemlock and emerging, 2025 (10-K)
TOP2_OPT_25 = 0.28                       # two end customers, share of Optical Communications sales, 2025

# ---- Quarterly (earnings releases), US$m unless stated; core basis ----
Q = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_SALES = [3258, 3604, 3733, 3874, 3679, 4045, 4272, 4412, 4345, 4738]
Q_EPS = [0.38, 0.47, 0.54, 0.57, 0.54, 0.60, 0.67, 0.72, 0.70, 0.78]
Q_OPT = [930, 1113, 1246, 1368, 1355, 1566, 1652, 1701, 1846, 2072]
Q_OPT_NI = [100, 143, 175, 194, 201, 247, 295, 305, 387, 438]
ENT_Q2_26 = 1.27        # US$bn, Enterprise Networks Q2 2026, up 65% (Q2 call)
ENT_Q2_26_G = 0.65
ENT_GROWTH = [("Q1 25", 1.06), ("Q3 25", 0.58), ("Q2 26", 0.65)]   # as stated in releases
H1_26_SALES = 9.083; H1_26_OPT = 3.918; H1_26_OPT_NI = 0.825
H1_26_SEGNI = 1.610     # reportable segments plus Life Sciences and Emerging Growth
H1_26_CORE_NI = 1.292; H1_26_EPS = 1.47
Q2_26_SEGNI = 0.846; Q2_26_CORE_NI = 0.680
Q2_26_GM = 0.396; Q2_26_OM = 0.209
Q2_GAAP_EPS = 0.64; Q2_GAAP_SALES = 4.505
H1_26_CAPEX = 0.754; H1_26_FCF = 1.611; H1_26_DEP_INFLOW = 0.709; H1_26_DIV = 0.495
Q3_GUIDE_SALES = (4.9, 5.0); Q3_GUIDE_EPS = (0.85, 0.89)
SPRINGBOARD = [("End 2026", 20), ("End 2028", 30), ("End 2030", 40)]   # annualised sales run-rate, US$bn
TTM_EPS = sum(Q_EPS[-4:])    # core, Q3 25 to Q2 26

# ---- Share price, month-end close (Yahoo Finance, retrieved 6 Oct 2026) ----
PX_LABELS = ["Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24",
             "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25",
             "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26",
             "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
PX = [28.49, 30.45, 32.49, 32.24, 32.96, 33.38, 37.26, 38.85, 40.01, 41.85, 45.15, 47.59, 48.67, 47.52, 52.08,
      50.15, 45.78, 44.38, 49.59, 52.59, 63.24, 67.03, 82.03, 89.08, 84.20, 87.56, 103.25, 150.38, 135.97, 164.24,
      181.16, 255.43, 138.25, 148.73, 153.76, 159.37]

# ---- MY assumptions ----
# Second half of 2026: optical and the rest, built to land inside Corning's Q3 guide
Q3E_OPT, Q4E_OPT = 2.22, 2.36          # optical sales, US$bn
Q3E_REST, Q4E_REST = 2.73, 2.72        # rest of Corning, US$bn (Q3 total 4.95 = guide midpoint)
Q3E_OPT_M, Q4E_OPT_M = 0.215, 0.22     # optical segment net margin (Q2 2026: 21.1%)
REST_M_26 = 0.162                      # rest of Corning segment net margin, H2 2026 (H1: 15.2%)
CORP_Q = -0.16                         # US$bn a quarter, core net income less segment net income (Q2: -0.166)
CORP27, CORP28 = -0.70, -0.76          # US$bn a year
ATM_SOLD27, ATM_SOLD28 = 0.5, 1.0      # share of the US$2bn programme sold by each year's average
BASE_PE = 27
#        name,  opt27, opt28, optm27, optm28, rest27, rest28, restm27, restm28, multiple, prob
SCEN = [
    ("Bear", 0.22, 0.12, 0.21, 0.20, 0.06, 0.05, 0.160, 0.160, 22, 0.25),
    ("Base", 0.35, 0.25, 0.23, 0.24, 0.09, 0.08, 0.165, 0.170, BASE_PE, 0.50),
    ("Bull", 0.45, 0.32, 0.24, 0.255, 0.12, 0.10, 0.170, 0.180, 34, 0.25),
]
SENS_EPS = [4.60, None, 6.20]   # middle row = model 2028E
SENS_PE = [22, 27, 32]

# ---- 2026E ----
OPT26 = H1_26_OPT + Q3E_OPT + Q4E_OPT
REST26 = (H1_26_SALES - H1_26_OPT) + Q3E_REST + Q4E_REST
SALES26 = OPT26 + REST26
Q3E_NI = Q3E_OPT * Q3E_OPT_M + Q3E_REST * REST_M_26 + CORP_Q
Q4E_NI = Q4E_OPT * Q4E_OPT_M + Q4E_REST * REST_M_26 + CORP_Q
Q3E_EPS = Q3E_NI / DILUTED
Q4E_EPS = Q4E_NI / DILUTED
OPT_NI26 = H1_26_OPT_NI + Q3E_OPT * Q3E_OPT_M + Q4E_OPT * Q4E_OPT_M
NI26 = H1_26_CORE_NI + Q3E_NI + Q4E_NI
EPS26 = H1_26_EPS + Q3E_EPS + Q4E_EPS
SH27 = DILUTED + ATM_SHARES * ATM_SOLD27
SH28 = DILUTED + ATM_SHARES * ATM_SOLD28
Q4_RUNRATE = (Q4E_OPT + Q4E_REST) * 4


def project(o27, o28, om27, om28, r27, r28, rm27, rm28):
    opt27 = OPT26 * (1 + o27); opt28 = opt27 * (1 + o28)
    rest27 = REST26 * (1 + r27); rest28 = rest27 * (1 + r28)
    ni27 = opt27 * om27 + rest27 * rm27 + CORP27
    ni28 = opt28 * om28 + rest28 * rm28 + CORP28
    return dict(opt27=opt27, opt28=opt28, rest27=rest27, rest28=rest28, s27=opt27 + rest27, s28=opt28 + rest28,
                oni27=opt27 * om27, oni28=opt28 * om28, ni27=ni27, ni28=ni28, eps27=ni27 / SH27, eps28=ni28 / SH28)


B = SCEN[1]
P = project(*B[1:9])
S27, S28, EPS27, EPS28 = P["s27"], P["s28"], P["eps27"], P["eps28"]
VALS = [s[9] * project(*s[1:9])["eps28"] for s in SCEN]
WEIGHTED = sum(v * s[10] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
SENS_EPS[1] = round(EPS28, 2)
REVISIT = BASE_VALUE / 1.15

MCAP = PRICE * SHARES_OUT
NETDEBT = DEBT - CASH
EV = MCAP + NETDEBT
DIV_YIELD = DPS_Q * 4 / PRICE
OPT_SHARE_25 = OPT_H[-1] / SALES_H[-1]
OPT_SHARE_26 = OPT26 / SALES26
OPT_SHARE_28 = P["opt28"] / S28
OPT_NM = [n / s for n, s in zip(Q_OPT_NI, Q_OPT)]
OPT_YY = [None] * 4 + [Q_OPT[i] / Q_OPT[i - 4] - 1 for i in range(4, len(Q_OPT))]
ENT_SHARE_Q2 = ENT_Q2_26 / (Q_OPT[-1] / 1000)
CAR_Q2_26 = Q_OPT[-1] / 1000 - ENT_Q2_26
ENT_Q2_25 = ENT_Q2_26 / (1 + ENT_Q2_26_G)
CAR_Q2_25 = Q_OPT[5] / 1000 - ENT_Q2_25
REST_M_H1 = (H1_26_SEGNI - H1_26_OPT_NI) / (H1_26_SALES - H1_26_OPT)
CORP_H1 = H1_26_CORE_NI - H1_26_SEGNI
# What the price needs: 2028 EPS at the base multiple, and the optical sales that needs with the rest at base
NEED_EPS28 = PRICE / BASE_PE
NEED_OPT_NI28 = NEED_EPS28 * SH28 - P["rest28"] * B[8] - CORP28
NEED_OPT28 = NEED_OPT_NI28 / B[4]
NEED_OPT_CAGR = (NEED_OPT28 / OPT26) ** 0.5 - 1
# Cash: the share sale question
FCF_H1_EX = H1_26_FCF - H1_26_DEP_INFLOW
CAPEX_H2 = CAPEX_GUIDE_26 - H1_26_CAPEX
ATM_DILUTION = ATM_SHARES / SHARES_OUT
ATM_DROP = ATM_POST / ATM_PRE - 1
NV_WARRANT_PCT = NV_WARRANT_FV / DEPOSIT_Q2
# Where it trades
PE26, PE27, PE28 = PRICE / EPS26, PRICE / EPS27, PRICE / EPS28
PEC26, PEC27, PEC28 = PRICE / CONS_EPS_26, PRICE / CONS_EPS_27, PRICE / CONS_EPS_28
PE_TTM_CORE = PRICE / TTM_EPS
PE_HIST = PRICE_DEC24 / EPS_H[2]        # what the market paid at end 2024 for 2025 core EPS, in hindsight
FIBRE_MEDIAN = sorted([p[2] for p in PEERS[1:4]])[1]
# Which driver matters: optical bear to bull with the rest at base, and the reverse
OPT_SWING = project(*SCEN[2][1:5], *B[5:9])["eps28"] - project(*SCEN[0][1:5], *B[5:9])["eps28"]
REST_SWING = project(*B[1:5], *SCEN[2][5:9])["eps28"] - project(*B[1:5], *SCEN[0][5:9])["eps28"]

if __name__ == "__main__":
    print(f"2026E opt {OPT26:.3f} rest {REST26:.3f} sales {SALES26:.3f} Q4 run-rate {Q4_RUNRATE:.1f}; opt share {OPT_SHARE_26:.1%}")
    print(f"Q3E NI {Q3E_NI:.3f} EPS {Q3E_EPS:.3f}; Q4E EPS {Q4E_EPS:.3f}; 2026E EPS {EPS26:.2f} NI {NI26:.3f} optNI {OPT_NI26:.3f}")
    print(f"2027E sales {S27:.2f} opt {P['opt27']:.2f} EPS {EPS27:.2f} (cons {CONS_EPS_27}); 2028E sales {S28:.2f} opt {P['opt28']:.2f} EPS {EPS28:.2f} (cons {CONS_EPS_28}) opt share {OPT_SHARE_28:.1%}")
    print(f"shares 27 {SH27:.4f} 28 {SH28:.4f}; ATM shares {ATM_SHARES * 1000:.1f}m = {ATM_DILUTION:.2%}")
    print(f"PE mine 26/27/28 {PE26:.1f} {PE27:.1f} {PE28:.1f}; cons {PEC26:.1f} {PEC27:.1f} {PEC28:.1f}; TTM core {PE_TTM_CORE:.1f} (TTM EPS {TTM_EPS:.2f}); hist {PE_HIST:.1f}")
    for s, v in zip(SCEN, VALS):
        p = project(*s[1:9]); print(s[0], round(p["s28"], 2), round(p["opt28"], 2), round(p["eps28"], 2), round(v, 1), f"{v / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}; revisit {REVISIT:.0f}")
    print("grid", [[round(e * m) for m in SENS_PE] for e in SENS_EPS])
    print(f"need EPS28 {NEED_EPS28:.2f}; opt NI {NEED_OPT_NI28:.2f}; opt sales {NEED_OPT28:.2f} ({NEED_OPT28 / OPT_H[-1]:.2f}x 2025), CAGR 26-28 {NEED_OPT_CAGR:.1%}")
    print(f"mcap {MCAP:.1f} netdebt {NETDEBT:.2f} EV {EV:.1f} yield {DIV_YIELD:.2%}; below high {1 - PRICE / HI52:.1%}; since Sep25 {PRICE / PRICE_SEP25 - 1:+.1%}")
    print(f"opt NM", [f"{x:.1%}" for x in OPT_NM]); print("opt yy", [f"{x:.0%}" if x else None for x in OPT_YY])
    print(f"ent share Q2 {ENT_SHARE_Q2:.1%}; carrier Q2 26 {CAR_Q2_26:.3f} vs Q2 25 {CAR_Q2_25:.3f}; ent Q2 25 {ENT_Q2_25:.3f}")
    print(f"rest margin H1 {REST_M_H1:.1%}; corp H1 {CORP_H1:.3f}; FCF H1 ex dep {FCF_H1_EX:.3f}; capex H2 {CAPEX_H2:.3f}; ATM drop {ATM_DROP:.1%}")
    print(f"swing opt {OPT_SWING:.2f} rest {REST_SWING:.2f}; fibre median {FIBRE_MEDIAN}; opt share 25 {OPT_SHARE_25:.1%}")
