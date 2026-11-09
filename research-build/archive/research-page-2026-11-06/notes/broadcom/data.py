"""Broadcom Inc. (Nasdaq: AVGO) initiation, draft of 6 Oct 2026. Single source of figures for charts, note and model.

Sources: Broadcom quarterly results releases (Exhibit 99.1 to Form 8-K, EDGAR CIK 1730168): Q4 FY24 (12 Dec 2024),
Q1 FY25 (6 Mar 2025), Q2 FY25 (5 Jun 2025), Q3 FY25 (4 Sep 2025), Q4 FY25 (11 Dec 2025), Q1 FY26 (4 Mar 2026),
Q2 FY26 (3 Jun 2026), Q3 FY26 (2 Sep 2026), with their comparative columns. Form 10-Q for the quarter to 2 Aug 2026
(filed 10 Sep 2026): shares outstanding, remaining performance obligations, purchase commitments, the Backstop and
convertible notes, customer concentration, segment operating income. Form 8-K of 6 Apr 2026 (Google long-term TPU
agreement; Anthropic access to TPU-based compute through Broadcom). Earnings calls of 4 Sep 2025, 11 Dec 2025,
4 Mar 2026, 3 Jun 2026 and 2 Sep 2026 (transcripts: fool.com for 2 Sep 2026; transcripts.platformaeronaut.com for
the others). Prices: Nasdaq.com historical data (Yahoo Finance chart API refused requests with "Too Many Requests"
on 6 Oct 2026). Consensus, average target and forward P/E: stockanalysis.com (S&P Global data, last updated
2 Oct 2026), retrieved 6 Oct 2026. Everything marked MINE is my own estimate.

Fiscal years end on the Sunday closest to 31 October: FY2025 = year to 2 Nov 2025; FY2026 = year to 1 Nov 2026;
FY2027 = year to about 31 Oct 2027; FY2028 = year to about 29 Oct 2028. Income figures are Broadcom's NON-GAAP
measures unless marked GAAP. Broadcom guides on non-GAAP.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-06"
DATE_LONG = "6 October 2026"
COMPANY = "Broadcom"
NAME = "Broadcom"
SLUG = "broadcom"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/broadcom"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT LONG",           # e.g. "INITIATE AT LONG" once Tommy decides
    direction="LONG",
    target=485.0,                   # US$ per share; None for NO CALL. Base value rounded to the nearest US$5.
    conviction="Medium",
    draft=False,
)
WRONG_IF = ("The shares close below US$270 by October 2027, or Broadcom cuts its fiscal 2027 AI revenue outlook "
            "below US$100 billion, or it makes a payment under its Backstop for a customer's AI rack leases.")
WRONG_PX = 270

# ---- Market data (Nasdaq.com historical data, retrieved 6 Oct 2026) ----
PRICE = 362.51          # Nasdaq close, 5 Oct 2026
PRICE_DATE = "5 October 2026"
PRICE_PIECE = 343.64    # close on 1 Oct 2026, the last close before the journal piece (2 Oct 2026, 12:05 SGT)
HI52 = 495.00           # 52-week high, intraday, 3 Jun 2026
HI_CLOSE = 481.57       # highest close, 2 Jun 2026
LO52 = 289.96           # 52-week low, intraday, 30 Mar 2026
LO_CLOSE = 293.41       # lowest close, 30 Mar 2026
PRICE_DEC25 = 346.10    # close, 31 Dec 2025
PX_RESULTS = (367.24, 357.16)   # closes on 2 Sep 2026 (results after the close) and 3 Sep 2026

# ---- Price, month-end close (Nasdaq.com historical data, retrieved 6 Oct 2026); last point is the 5 Oct 2026 close ----
PX_LABELS = ['Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24', 'Sep 24', 'Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25', 'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26', '5 Oct 26']
PX = [83.06, 84.14, 92.57, 111.62, 118.0, 130.05, 132.54, 130.03, 132.85, 160.55, 160.68, 162.82, 172.5, 169.77, 162.08, 231.84, 221.27, 199.43, 167.43, 192.47, 242.07, 275.65, 293.7, 297.39, 329.91, 369.63, 402.96, 346.1, 331.3, 319.55, 309.51, 417.43, 446.77, 377.75, 389.28, 370.34, 351.19, 362.51]

# ---- Shares and balance sheet (Q3 FY26 release and 10-Q) ----
COMMON_OUT = 4.774      # bn, 2 Aug 2026 (10-Q balance sheet: 4,774 million issued and outstanding)
CASH = 23.975           # US$bn, 2 Aug 2026
DEBT_ST = 2.252         # US$bn, short-term debt, 2 Aug 2026
DEBT_LT = 57.167        # US$bn, long-term debt, 2 Aug 2026
DEBT = DEBT_ST + DEBT_LT
BACKSTOP_MAX = 29.0     # US$bn, maximum potential liability under the Backstop, undiscounted (10-Q)
XPV_TRANCHE = 35.0      # US$bn, first AI XPV tranche, June 2026 (10-Q)
CONV_NOTES = 42.0       # US$bn, convertible notes the customer may issue to Broadcom (10-Q); none issued
RPO = 179.2             # US$bn, remaining performance obligations, 2 Aug 2026 (10-Q); about 25% in 12 months
PURCH = (52.674, 72.952, 126.821)   # US$bn, unconditional purchase commitments FY27, FY28, total (10-Q)
TOP5 = (0.40, 0.55)     # top five end customers, share of revenue, Q3 FY25 and Q3 FY26 (10-Q)
DIST_Q3 = (0.32, 0.50)  # one distributor, share of revenue, Q3 FY25 and Q3 FY26 (10-Q)
SBC_Q3 = 2.019          # US$bn, stock-based pay, Q3 FY26 (excluded from non-GAAP)
GAAP_EPS_9M = 6.09      # US$, three quarters to 2 Aug 2026
NG_NI_9M = 38.631       # US$bn, non-GAAP net income, three quarters to 2 Aug 2026
NG_SH_9M = 4.945        # bn
SEG_Q3 = dict(semi_rev=20.839, semi_op=12.770, sw_rev=8.752, sw_op=7.325)   # 10-Q segment table, Q3 FY26

# ---- Consensus and peers (stockanalysis.com, S&P Global data updated 2 Oct 2026; retrieved 6 Oct 2026) ----
CONS_EPS_26 = 11.66     # FY26 non-GAAP EPS (40 analysts; range 11.35 to 12.38)
CONS_REV_26 = 105.97
CONS_EPS_27 = 19.39     # FY27
CONS_REV_27 = 173.93
CONS_TP = 531.85        # average target, 50 analysts (range 215.88 to 715)
CONS_TP_RANGE = (215.88, 715.0)
FWD_PE_SA = 20.92       # stockanalysis.com forward P/E for AVGO, 6 Oct 2026
SEMI_PEERS = [  # company, ticker, forward P/E, what they make
    ("Advanced Micro Devices", "Nasdaq: AMD", 56.89, "GPUs and CPUs for data centres"),
    ("Marvell", "Nasdaq: MRVL", 53.37, "Custom AI chips, optical DSPs, switch chips"),
    ("TSMC", "NYSE: TSM", 20.73, "Foundry: makes Broadcom's custom chips and switch chips"),
    ("Nvidia", "Nasdaq: NVDA", 19.75, "GPUs, NVLink, InfiniBand and Ethernet networking"),
    ("Qualcomm", "Nasdaq: QCOM", 19.51, "Mobile and connectivity chips; data centre CPUs"),
]
SW_PEERS = [
    ("ServiceNow", "NYSE: NOW", 30.03, "Enterprise workflow software"),
    ("Microsoft", "Nasdaq: MSFT", 26.57, "Cloud, operating systems and enterprise software"),
    ("IBM", "NYSE: IBM", 17.35, "Mainframes, Red Hat and infrastructure software"),
    ("Oracle", "NYSE: ORCL", 16.72, "Databases, enterprise software and cloud"),
    ("Adobe", "Nasdaq: ADBE", 8.89, "Creative and document software"),
]
OTHER_PEERS = [("Arista Networks", "NYSE: ANET", 44.54, "Ethernet switches, many built on Broadcom chips")]

# ---- Annual reported, non-GAAP unless marked, US$bn ----
YEARS_H = ["FY24", "FY25"]
REV_H = [51.574, 63.887]
SEMI_H = [30.096, 36.858]
SW_H = [21.478, 27.029]
AI_H = [12.2, 20.2]         # FY24 release; FY25 = sum of the four quarters (4.1 + 4.4 + 5.2 + 6.5)
GMH = [39.459, 50.245]      # non-GAAP gross margin, US$bn
OPH = [30.736, 41.997]      # non-GAAP operating income, US$bn
NIH = [23.733, 33.728]
SHH = [4.877, 4.943]
EPS_H = [4.87, 6.82]        # NI / diluted shares (4.866 and 6.823)
FY23_REV = 35.819

# ---- Quarterly (results releases), US$bn; fiscal quarters ----
Q = ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26"]
QS = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
Q_REV = [14.916, 15.004, 15.952, 18.015, 19.311, 22.187, 29.591]
Q_SEMI = [8.212, 8.408, 9.166, 11.072, 12.515, 15.009, 20.839]
Q_SW = [6.704, 6.596, 6.786, 6.943, 6.796, 7.178, 8.752]
Q_AI = [4.1, 4.4, 5.2, 6.5, 8.4, 10.8, 16.7]     # releases; Q4 FY25 from the 11 Dec 2025 call
Q_GMD = [11.796, 11.911, 12.499, 14.039, 14.868, 17.109, 22.191]   # non-GAAP gross margin, US$bn
Q_OPD = [9.828, 9.793, 10.455, 11.921, 12.826, 14.928, 20.095]     # non-GAAP operating income, US$bn
Q_NI = [7.823, 7.787, 8.404, 9.714, 10.185, 12.074, 16.372]
Q_SH = [4.895, 4.937, 4.972, 4.969, 4.957, 4.940, 4.937]
Q_EPS = [1.60, 1.58, 1.69, 1.95, 2.05, 2.44, 3.32]
Q_GM = [round(g / r * 100, 1) for g, r in zip(Q_GMD, Q_REV)]
Q_OM = [round(o / r * 100, 1) for o, r in zip(Q_OPD, Q_REV)]
# Networking share of AI revenue, where Broadcom disclosed it on its calls
NET_SHARE = {"Q3 25": 0.35, "Q1 26": 1 / 3, "Q2 26": 0.40, "Q3 26": 0.27}
# Q3 FY25 call: XPUs 65% of AI revenue. Q1 FY26 call: networking one third. Q2 FY26 call: "almost 40%".
# Q3 FY26 call: XPU shipments 73% of AI revenue; networking up over 2.5x, XPUs up over 3.5x on a year earlier.

# ---- Guidance (Q3 FY26 release and call, 2 Sep 2026) ----
G4 = dict(rev=34.8, ai=21.7, semi=26.1, sw=8.7, nonai_call=4.3, om=0.66, gm=0.73, tax=0.16, sh=4.94, capex=1.4)
AI_FY26_CALL = 58.0     # "about $58 billion" for fiscal 2026
AI_FY27_OUT = 115.0     # "secured the supply to again double AI revenue to approximately $115 billion"
AI_FY28_OUT = 230.0     # "line of sight ... to again double to $230 billion"
EPS28_CALL = 30.0       # "very much on target to exceed $30 in earnings per share in fiscal 2028"
RESULTS_DATE = "9 December 2026"   # Q4 FY26, planned per the 2 Sep 2026 call (Ji Yoo)

# ---- FY2026E: three reported quarters plus the Q4 guide ----
Q4_OP = G4["rev"] * G4["om"]
Q4_INT = -0.68          # MINE: non-GAAP interest expense after debt repayment
Q4_OTHER = 0.10         # MINE: other income
Q4_NI = (Q4_OP + Q4_INT + Q4_OTHER) * (1 - G4["tax"])
Q4_EPS = Q4_NI / G4["sh"]
REV26 = sum(Q_REV[4:]) + G4["rev"]
NONAI26 = sum(s - a for s, a in zip(Q_SEMI[4:], Q_AI[4:])) + G4["nonai_call"]   # Q4: guided "approximately $4.3 billion"
SW26 = sum(Q_SW[4:]) + G4["sw"]
AI26 = sum(Q_AI[4:]) + G4["ai"]
SEMI26 = AI26 + NONAI26   # segment guides sum to US$34.7bn against the US$34.8bn consolidated guide (rounding)
OP26 = sum(Q_OPD[4:]) + Q4_OP
OM26 = OP26 / REV26
NI26 = sum(Q_NI[4:]) + Q4_NI
EPS26 = sum(Q_EPS[4:]) + Q4_EPS
GM26 = (sum(Q_GMD[4:]) + G4["rev"] * G4["gm"]) / REV26

# ---- MY assumptions, FY27 and FY28 ----
AI27 = AI_FY27_OUT       # management's outlook, taken as given
NONAI27 = 17.5           # MINE: non-AI semiconductors, about 4% growth
SW27 = 33.5              # MINE: infrastructure software, about 7% growth
SM27 = 0.60              # MINE: semiconductor segment operating margin (61.3% in Q3 FY26; about 60% implied in Q4)
SWM = 0.81               # MINE: software segment operating margin (83.7% in Q3 FY26; 80.5% over three quarters)
INT27 = -2.2             # MINE: non-GAAP interest and other, net
TAX = 0.16               # guided for FY26 (global minimum tax); MINE for FY27 and FY28
SH = 4.94                # bn, Q4 FY26 guide; MINE: buybacks offset dilution in FY27 and FY28
AI28 = 190.0             # MINE: base case, 17% below management's US$230bn
NONAI28 = 18.0           # MINE
SW28 = 35.5              # MINE: about 6% growth
SM28 = 0.58              # MINE: XPU racks with more memory dilute the semiconductor margin
INT28 = -1.5             # MINE
NETDEBT = DEBT - CASH    # US$bn at 2 Aug 2026; MINE: held flat to October 2027 (free cash after dividends goes to buybacks)
M_SEMI = 20              # MINE: about the median forward P/E of five chip peers (20.7x), rounded down
M_SW = 17                # MINE: about the median forward P/E of five software peers (17.4x)

SEMI27 = AI27 + NONAI27
REV27 = SEMI27 + SW27
OP27 = SEMI27 * SM27 + SW27 * SWM
OM27 = OP27 / REV27
NI27 = (OP27 + INT27) * (1 - TAX)
EPS27 = NI27 / SH


def project(ai28, sm28, m_semi, m_sw):
    semi = ai28 + NONAI28
    semi_op = semi * sm28
    sw_op = SW28 * SWM
    op = semi_op + sw_op
    ni = (op + INT28) * (1 - TAX)
    v_semi = semi_op * (1 - TAX) * m_semi
    v_sw = sw_op * (1 - TAX) * m_sw
    value = (v_semi + v_sw - NETDEBT) / SH
    return dict(semi=semi, rev=semi + SW28, semi_op=semi_op, sw_op=sw_op, op=op, om=op / (semi + SW28), ni=ni,
                eps=ni / SH, v_semi=v_semi / SH, v_sw=v_sw / SH, nd=NETDEBT / SH, value=value)


#        name,  AI FY28, semi op margin, semi multiple, software multiple, prob
SCEN = [
    ("Bear", 115.0, 0.52, 14, 14, 0.25),
    ("Base", AI28, SM28, M_SEMI, M_SW, 0.50),
    ("Bull", AI_FY28_OUT, 0.60, 22, 20, 0.25),
]
P = project(AI28, SM28, M_SEMI, M_SW)
REV28, EPS28, OP28, OM28 = P["rev"], P["eps"], P["op"], P["om"]
VALS = [project(s[1], s[2], s[3], s[4])["value"] for s in SCEN]
WEIGHTED = sum(v * s[5] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
SENS_AI = [150.0, AI28, 230.0]
SENS_M = [16, M_SEMI, 24]
VGRID = [[project(a, SM28, m, M_SW)["value"] for m in SENS_M] for a in SENS_AI]
REVISIT_NOCALL = BASE_VALUE / 1.15   # price above which the base is less than 15% above (the long lapses to no call)

# ---- Value, debt, multiples ----
MCAP = PRICE * COMMON_OUT
EV = MCAP + NETDEBT
PE25 = PRICE / EPS_H[1]
PE26, PE27, PE28 = PRICE / EPS26, PRICE / EPS27, PRICE / EPS28
PEC26, PEC27 = PRICE / CONS_EPS_26, PRICE / CONS_EPS_27
PE28_CALL = PRICE / EPS28_CALL
SINCE_PIECE = PRICE / PRICE_PIECE - 1
OFF_HIGH = PRICE / HI_CLOSE - 1
RISE_LO = PRICE / LO_CLOSE - 1
RISE_DEC25 = PRICE / PRICE_DEC25 - 1
# What the price needs: FY28 AI revenue at the base multiples and margins
NEED_SEMI_NOPAT = (PRICE * SH + NETDEBT - P["v_sw"] * SH) / M_SEMI
NEED_SEMI_REV = NEED_SEMI_NOPAT / (1 - TAX) / SM28
NEED_AI28 = NEED_SEMI_REV - NONAI28
NEED_AI_G = NEED_AI28 / AI27 - 1
# Claim test figures
NET_Q3 = Q_AI[-1] * NET_SHARE["Q3 26"]
XPU_Q3 = Q_AI[-1] - NET_Q3
AI_SHARE_Q3 = Q_AI[-1] / Q_REV[-1]
AI_G_Q3 = Q_AI[-1] / Q_AI[2] - 1
SEMI_GM_Q3 = (Q_GMD[-1] - 0.94 * Q_SW[-1]) / Q_SEMI[-1]   # software gross margin 94% (CFO, 2 Sep 2026)
SEMI_OM_Q3 = SEG_Q3["semi_op"] / SEG_Q3["semi_rev"]
SW_OM_Q3 = SEG_Q3["sw_op"] / SEG_Q3["sw_rev"]
SW_SHARE_VALUE = P["v_sw"] / BASE_VALUE

if __name__ == "__main__":
    print(f"Q4E op {Q4_OP:.3f} NI {Q4_NI:.3f} EPS {Q4_EPS:.3f}")
    print(f"FY26 rev {REV26:.3f} semi {SEMI26:.3f} sw {SW26:.3f} AI {AI26:.1f} nonAI {NONAI26:.2f} op {OP26:.3f} OM {OM26:.1%} GM {GM26:.1%} NI {NI26:.2f} EPS {EPS26:.2f} (cons {CONS_EPS_26})")
    print(f"FY27 rev {REV27:.2f} op {OP27:.2f} OM {OM27:.1%} NI {NI27:.2f} EPS {EPS27:.2f} (cons {CONS_EPS_27}, {EPS27/CONS_EPS_27-1:+.1%}); rev vs cons {REV27/CONS_REV_27-1:+.1%}")
    print(f"FY28 rev {REV28:.2f} op {OP28:.2f} OM {OM28:.1%} EPS {EPS28:.2f}; v_semi {P['v_semi']:.1f} v_sw {P['v_sw']:.1f} nd {P['nd']:.2f}")
    for s, v in zip(SCEN, VALS):
        p = project(s[1], s[2], s[3], s[4]); print(s[0], round(p["rev"], 1), round(p["eps"], 2), round(v, 1), f"{v / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}; base {BASE_VALUE:.1f} {BASE_VALUE/PRICE-1:+.1%}; nocall above {REVISIT_NOCALL:.0f}")
    print("grid", [[round(v) for v in r] for r in VGRID], sum(v > PRICE for r in VGRID for v in r), sum(v > PRICE * 1.15 for r in VGRID for v in r))
    print(f"PE 25 {PE25:.1f} 26 {PE26:.1f} 27 {PE27:.1f} 28 {PE28:.1f}; cons {PEC26:.1f} {PEC27:.1f}; at $30 {PE28_CALL:.1f}")
    print(f"need AI28 {NEED_AI28:.1f} growth {NEED_AI_G:.1%}; semi rev {NEED_SEMI_REV:.1f}")
    print(f"mcap {MCAP:.1f} netdebt {NETDEBT:.2f} EV {EV:.1f}; piece {SINCE_PIECE:+.1%} offhigh {OFF_HIGH:+.1%} lo {RISE_LO:+.1%} dec {RISE_DEC25:+.1%}")
    print(f"net Q3 {NET_Q3:.2f} xpu {XPU_Q3:.2f}; AI share {AI_SHARE_Q3:.1%} AI g {AI_G_Q3:.1%}; semi GM {SEMI_GM_Q3:.1%} semi OM {SEMI_OM_Q3:.1%} sw OM {SW_OM_Q3:.1%}; sw share of value {SW_SHARE_VALUE:.1%}")
    print("GM", Q_GM, "OM", Q_OM)
    import statistics; print("semi med", statistics.median([p[2] for p in SEMI_PEERS]), "sw med", statistics.median([p[2] for p in SW_PEERS]))
