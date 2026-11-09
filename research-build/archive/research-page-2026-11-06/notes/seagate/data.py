"""Seagate Technology Holdings plc (Nasdaq: STX) initiation, draft of 2 Nov 2026. Single source of figures for charts, note and model.

Sources: Seagate fiscal Q1 2027 results release (Exhibit 99.1 to Form 8-K, 27 Oct 2026) and Supplemental Financial Information
(27 Oct 2026); fiscal Q4 2026 and fiscal 2026 results release (Exhibit 99.1 to Form 8-K, 28 Jul 2026); supplementals of 28 Oct 2025
(Q1 FY26, which restates FY25 quarters for the VIA nearline definition), 27 Jan 2026 (Q2 FY26) and 28 Apr 2026 (Q3 FY26); Form 10-K for
the year to 3 Jul 2026 (filed 4 Aug 2026). Annual GAAP revenue, cost of revenue and net income FY2016 to FY2026 from Seagate's 10-K XBRL
data on SEC EDGAR (companyfacts API). Earnings call of 27 Oct 2026: Seagate's corrected transcript (FactSet CallStreet), posted at
investors.seagate.com, used only for management's spoken remarks. Form 10-Q for the quarter to 2 Oct 2026 (filed 29 Oct 2026) for
inventory. Western Digital fiscal Q1 2027 release (Exhibit 99.1 to Form 8-K, 22 Oct 2026). Toshiba Electronic Devices & Storage
news release, 2 Oct 2026: the doubling target is for Toshiba Information Equipment (Philippines), Toshiba's Philippine drive plant,
not for all of Toshiba. Micron fiscal Q4 2026 prepared remarks, 30 Sep 2026 (NAND prices up approximately 30% sequentially).
Prices: stockanalysis.com daily history (Nasdaq closes), retrieved 2 Nov 2026 (Yahoo Finance chart API returned "Too Many Requests").
Consensus and peer figures: stockanalysis.com (S&P Global data), retrieved 2 Nov 2026.
Everything marked MINE is my own estimate.

Fiscal years end on the Friday closest to 30 June: FY2026 = year to 3 Jul 2026 (53 weeks); FY2027 = year to 2 Jul 2027;
FY2028 = year to about 30 Jun 2028. Seagate's supply statements are in calendar years (CY). Income figures are Seagate's
NON-GAAP measures unless marked GAAP. Revenue per nearline terabyte is my derived ratio: Data Center revenue over nearline exabytes
shipped, both from the supplementals (US$ million per exabyte = US$ per terabyte).
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
DATE_LONG = "2 November 2026"
COMPANY = "Seagate"
NAME = "Seagate Technology"
SLUG = "seagate"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/seagate"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="NO CALL",              # Tommy's call, 2 Nov 2026
    direction="NO CALL",
    target=None,                    # US$ per share; None for NO CALL
    conviction="Low",
    draft=False,
)

# ---- Market data (stockanalysis.com daily history, Nasdaq closes, retrieved 2 Nov 2026) ----
PRICE = 644.58          # close, 30 Oct 2026 (Friday; latest close at drafting)
PRICE_DATE = "30 October 2026"
HI_CLOSE = 1094.04      # highest close of the past year, 22 Jun 2026
HI52 = 1145.00          # intraday high of the past year, 18 Jun 2026 (a different day from the highest close)
LO_CLOSE = 237.49       # lowest close of the past year, 21 Nov 2025
LO52 = 228.61           # intraday low of the past year, 21 Nov 2025
PRICE_DEC25 = 275.39    # close, 31 Dec 2025
PX_TOSHIBA = (945.57, 848.99)   # closes 1 Oct 2026 and 2 Oct 2026, the day of Toshiba's release (down 10.2%)
PX_RESULTS = (667.85, 697.97)   # closes 27 Oct 2026 (results after the close) and 28 Oct 2026
PX_SEP26 = 922.34       # close, 30 Sep 2026
PX_LABELS = ['Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24', 'Sep 24',
             'Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25',
             'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26',
             '30 Oct 26']
PX = [68.25, 79.10, 85.37, 85.68, 93.05, 93.05, 85.91, 93.24, 103.27, 102.17, 99.55, 109.53,
      100.37, 101.33, 86.31, 96.36, 101.91, 84.95, 91.03, 117.94, 144.33, 157.01, 167.40, 236.06,
      255.88, 276.69, 275.39, 407.69, 407.84, 391.76, 673.64, 879.80, 965.00, 856.13, 828.38, 922.34,
      644.58]

SHARES_OUT = 0.230      # bn ordinary shares issued and outstanding at 2 Oct 2026 (Q1 FY27 release)

# ---- Balance sheet, 2 Oct 2026 (Q1 FY27 release and supplemental), US$bn ----
CASH = 1.258
DEBT_PRINCIPAL = 2.383  # principal outstanding; net debt 1.125 in the supplemental
NET_DEBT = 1.125        # principal less cash (supplemental). US$750m more retired in October from cash: net debt unchanged
DEBT_OCT = 1.6          # principal after the October retirement (release)
BUYBACK_LEFT = 4.4      # US$bn left on the authorisation (call, 27 Oct 2026)
INV = (1.571, 1.700)    # inventories, net, 3 Jul 2026 and 2 Oct 2026 (10-Q, filed 29 Oct 2026)

# ---- Consensus and peers (stockanalysis.com, S&P Global data; retrieved 2 Nov 2026) ----
CONS_EPS_27 = 39.98     # FY27 non-GAAP EPS, 21 analysts, range 32.75 to 45.94; updated 29 Oct 2026
CONS_EPS_28 = 65.34     # FY28
CONS_REV_27 = 20.32
CONS_REV_28 = 28.41
CONS_RANGE_27 = (32.75, 45.94)
PEERS = [  # company, listing, price 30 Oct 2026, consensus EPS (year ending in 2027), year, what they make
    ("Western Digital", "Nasdaq: WDC", 366.11, 24.72, "FY to Jun 2027", "Hard drives (nearline and other)"),
    ("Sandisk", "Nasdaq: SNDK", 1150.89, 226.85, "FY to Jun 2027", "NAND flash and SSDs"),
    ("Micron", "Nasdaq: MU", 884.74, 176.50, "FY to Aug 2027", "DRAM, HBM, NAND flash"),
]
WDC_Q1 = dict(rev=4.381, gm=0.581, om=0.491, eps=4.64, g_rev=5.1, g_gm=0.605, g_eps=5.80)   # WDC Q1 FY27 release, 22 Oct 2026

# ---- Annual history: GAAP (10-K XBRL via SEC EDGAR), US$bn ----
YRS = ["FY16", "FY17", "FY18", "FY19", "FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]
REV_H = [11.160, 10.771, 11.184, 10.390, 10.509, 10.681, 11.661, 7.384, 6.551, 9.097, 12.195]
COR_H = [8.545, 7.597, 7.820, 7.458, 7.667, 7.764, 8.192, 6.033, 5.015, 5.897, 6.637]
NI_H = [0.248, 0.772, 1.182, 2.012, 1.004, 1.314, 1.649, -0.529, 0.335, 1.469, 3.184]
GM_H = [(r - c) / r for r, c in zip(REV_H, COR_H)]
CYC_REV = sum(REV_H[:10]); CYC_NI = sum(NI_H[:10]); CYC_COR = sum(COR_H[:10])
CYC_NM = CYC_NI / CYC_REV                 # ten-year GAAP net margin, FY2016 to FY2025
CYC_GM = 1 - CYC_COR / CYC_REV            # ten-year GAAP gross margin
FY23_REV_FALL = REV_H[7] / REV_H[6] - 1   # FY23 revenue against FY22

# Non-GAAP annual (Q4 FY26 release, 28 Jul 2026), US$bn
FY25 = dict(rev=9.097, ni=1.733, eps=8.10, gm=0.358, om=0.234)
FY26 = dict(rev=12.195, ni=3.538, eps=15.58, gm=0.461, om=0.365, fcf=3.105, capex=0.569, nl_eb=695, eb=789)   # nearline EB from the FY26 10-K (quarterly supplementals sum to 694 on rounding)

# ---- Quarterly, non-GAAP (supplementals), US$bn; exabytes (EB) ----
QL = ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26", "Q1 FY27"]
QS = ["Sep 24", "Dec 24", "Mar 25", "Jun 25", "Sep 25", "Dec 25", "Mar 26", "Jun 26", "Sep 26"]
Q_REV = [2.168, 2.325, 2.160, 2.444, 2.629, 2.825, 3.112, 3.629, 4.233]
Q_DC = [1.582, 1.736, 1.615, 1.863, 2.114, 2.224, 2.500, 2.933, 3.449]   # Data Center revenue
Q_EDGE = [r - d for r, d in zip(Q_REV, Q_DC)]                              # Edge IoT (total less Data Center)
Q_NL = [114, 126, 120, 137, 159, 165, 175, 195, 198]                      # nearline EB (VIA included from the Q1 FY26 supplemental)
Q_EB = [138, 151, 144, 162, 182, 190, 199, 218, 220]                      # total HDD EB
Q_GM = [0.333, 0.355, 0.362, 0.379, 0.401, 0.422, 0.470, 0.527, 0.578]
Q_OM = [0.204, 0.231, 0.235, 0.262, 0.290, 0.319, 0.375, 0.446, 0.507]
Q_EPS = [1.58, 2.03, 1.90, 2.59, 2.61, 3.11, 4.10, 5.71, 7.68]
Q_FCF = [0.027, 0.150, 0.216, 0.425, 0.427, 0.607, 0.953, 1.118, 1.479]
Q_PTB = [d * 1000 / n for d, n in zip(Q_DC, Q_NL)]                       # US$ per nearline TB (derived)
PTB_2Y = sum(Q_DC[:8]) * 1000 / sum(Q_NL[:8])                             # FY25 and FY26 average, US$ per TB
PTB_26 = sum(Q_DC[4:8]) * 1000 / sum(Q_NL[4:8])
PTB_UP = Q_PTB[8] / Q_PTB[4] - 1                                          # Q1 FY27 against Q1 FY26
NL_UP = Q_NL[8] / Q_NL[4] - 1
Q1_NM = 1.781 / 4.233                                                     # Q1 FY27 non-GAAP net margin

# ---- Guidance and outlook (Q1 FY27 release and supplemental, 27 Oct 2026; call) ----
G2 = dict(rev=4.8, rev_pm=0.1, eps=9.20, eps_pm=0.20, opex=0.300, tax=0.16, sh=0.233)
EB_CAGR_MGMT = "mid-20s %"   # nearline exabyte supply growth targeted (call); "25% is a really good number"
CAPEX_RANGE = (0.04, 0.06)   # FY27 capex 4% to 6% of revenue (call)
RESULTS_DATE = "late January 2027"   # Q2 FY27; not yet announced (Q2 FY26 was reported on 27 Jan 2026)

# ---- MY FY2027 quarters (Q1 actual, Q2 = the guide midpoint) ----
TAX = G2["tax"]
SH = G2["sh"]           # MINE: diluted shares held at the Q2 guide; buybacks treated as cash kept (value-neutral at fair value)
Q27_REV = [4.233, G2["rev"], 5.15, 5.45]       # MINE after Q2: price per TB keeps rising on CY27 contracts, more slowly
Q27_OM = [0.507, None, 0.570, 0.580]           # MINE after Q2; Q2 "towards mid 50% range"
OTHER = -0.010          # MINE: net interest and other a quarter, after the debt paydown
Q27_EPS_FIX = [7.68, G2["eps"]]


def q27():
    eps = list(Q27_EPS_FIX)
    for r, m in zip(Q27_REV[2:], Q27_OM[2:]):
        eps.append((r * m + OTHER) * (1 - TAX) / SH)
    ni = [1.781, G2["eps"] * SH] + [e * SH for e in eps[2:]]
    return ni, eps


Q27_NI, Q27_EPS = q27()
REV27 = sum(Q27_REV); NI27 = sum(Q27_NI); EPS27 = sum(Q27_EPS)
Q2_OM_IMPLIED = (G2["eps"] * SH / (1 - TAX) - OTHER) / G2["rev"]

# ---- MY FY2028 and the cash at October 2027 ----
EB28 = 0.25             # MINE: nearline exabyte growth, management's mid-20s
PTB28 = 0.05            # MINE: price per TB, H1 on CY27 contracts, H2 on CY28 terms not yet set
G28 = (1 + EB28) * (1 + PTB28) - 1
OM28 = 0.58             # MINE
CAPEX_PCT = 0.05        # MINE: middle of the guided 4% to 6%
DA_YR = 0.32            # MINE: depreciation, a year (FY26 US$0.276bn)
WC = 0.40               # MINE: working capital build over the year
DPS = 0.76 * 4


def eps28(g=G28, om=OM28):
    rev = REV27 * (1 + g)
    return rev, (rev * om + 4 * OTHER) * (1 - TAX) / SH


REV28, EPS28 = eps28()
NI28 = EPS28 * SH
# Free cash flow from Q2 FY27 to Q1 FY28 (the twelve months to about October 2027)
NI_12M = sum(Q27_NI[1:]) + NI28 / 4
REV_12M = sum(Q27_REV[1:]) + REV28 / 4
FCF_12M = NI_12M + DA_YR - CAPEX_PCT * REV_12M - WC
NC_OCT27 = -NET_DEBT + FCF_12M - DPS * SH       # net cash, about October 2027
NC_PS = NC_OCT27 / SH

# ---- Normal (mid-cycle) earnings, MINE ----
EB_G = 1.25             # MINE: nearline exabytes a year, management's mid-20s supply growth
N_YEARS = 4             # FY2026 to a mid-cycle year around FY2030
PF = 1.00               # MINE: normal price per TB against the FY25 and FY26 average
EDGE_N = 2.5            # MINE: Edge IoT revenue in a normal year (FY26 US$2.43bn)
NM = 0.30               # MINE: normal net margin (FY26 non-GAAP 29.0%; FY25 19.1%; FY16 to FY25 GAAP 9.5%)
MULT = 14               # MINE: P/E on normal earnings
RATE = 0.10             # MINE: discount rate on above-normal earnings
W_UP = (1.0, 0.5, 0.0)  # MINE: share of FY28's excess earned in FY28, FY29, FY30 (base)
NL_N = FY26["nl_eb"] * EB_G ** N_YEARS


def normal_rev(pf=PF):
    return NL_N * PTB_2Y * pf / 1000 + EDGE_N


def normal_eps(pf=PF, nm=NM):
    return normal_rev(pf) * nm / SH


def value(n, mult=MULT, e28=None, w=W_UP):
    e28 = EPS28 if e28 is None else e28
    exc = sum(wi * (e28 - n) / (1 + RATE) ** (i + 1) for i, wi in enumerate(w))
    return dict(nc=NC_PS, exc=exc, term=n * mult, value=NC_PS + exc + n * mult)


N_BASE = normal_eps()
#        name, price factor, net margin, multiple, FY28 EB growth, FY28 price per TB, FY28 op margin, weights, prob
SCEN = [
    ("Bear", 0.80, 0.18, 12, 0.20, -0.10, 0.50, (1.0, 0.0, 0.0), 0.25),
    ("Base", PF, NM, MULT, EB28, PTB28, OM28, W_UP, 0.50),
    ("Bull", 1.25, 0.38, 16, 0.25, 0.15, 0.62, (1.0, 1.0, 0.5), 0.25),
]


def scen(s):
    n = normal_eps(s[1], s[2])
    r28, e28 = eps28((1 + s[4]) * (1 + s[5]) - 1, s[6])
    v = value(n, s[3], e28, s[7])
    return dict(n=n, nrev=normal_rev(s[1]), ptb=PTB_2Y * s[1], rev28=r28, eps28=e28, **v)


SV = [scen(s) for s in SCEN]
VALS = [v["value"] for v in SV]
WEIGHTED = sum(v * s[8] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
UP_BASE = BASE_VALUE / PRICE - 1
RULE = "LONG" if UP_BASE >= 0.15 else ("SHORT" if UP_BASE <= -0.25 else "NO CALL")

# Sensitivity: normal net margin (rows) against the normal multiple (columns), base revenue and FY28
SENS_NM = [0.22, NM, 0.38]
SENS_X = [12, MULT, 16]
VGRID = [[value(normal_eps(PF, m), x)["value"] for x in SENS_X] for m in SENS_NM]

# What the price implies: normal EPS at the base multiple, FY28 and up-cycle (linear in n, solved exactly)
_k = sum(wi / (1 + RATE) ** (i + 1) for i, wi in enumerate(W_UP))
NEED_N = (PRICE - NC_PS - _k * EPS28) / (MULT - _k)
NEED_NM = NEED_N * SH / normal_rev()                        # as a net margin on my base normal revenue
NEED_REV = NEED_N * SH / NM                                 # as normal revenue at my base margin
NEED_PTB = (NEED_REV - EDGE_N) * 1000 / NL_N                # as a normal price per TB at my base margin
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75

# ---- Value and multiples ----
MCAP = PRICE * SHARES_OUT
EV = MCAP + NET_DEBT
PE26 = PRICE / FY26["eps"]
PE27, PE28 = PRICE / EPS27, PRICE / EPS28
PEC27, PEC28 = PRICE / CONS_EPS_27, PRICE / CONS_EPS_28
PE_NORMAL = PRICE / N_BASE
PE_RUN = PRICE / (G2["eps"] * 4)
PEER_PE = [(p[0], p[2] / p[3]) for p in PEERS]
OFF_HIGH = PRICE / HI_CLOSE - 1
SINCE_DEC25 = PRICE / PRICE_DEC25 - 1
OCT_FALL = PRICE / PX_SEP26 - 1
TOSHIBA_DAY = PX_TOSHIBA[1] / PX_TOSHIBA[0] - 1
NEED_VS_26 = NEED_N / FY26["eps"]
NEED_VS_28 = NEED_N / EPS28
Q2_PTB_IMPLIED = None   # Seagate gives no Q2 split; not used

if __name__ == "__main__":
    print("PTB by quarter", [round(x, 2) for x in Q_PTB], f"2y avg {PTB_2Y:.2f} FY26 {PTB_26:.2f} up {PTB_UP:+.1%} NL up {NL_UP:+.1%}")
    print("edge", [round(x, 3) for x in Q_EDGE], f"FY26 edge {sum(Q_EDGE[4:8]):.3f}")
    print(f"Q27 EPS {[round(e, 2) for e in Q27_EPS]} Q2 OM implied {Q2_OM_IMPLIED:.1%}")
    print(f"FY27 rev {REV27:.2f} (cons {CONS_REV_27}, {REV27/CONS_REV_27-1:+.1%}) EPS {EPS27:.2f} (cons {CONS_EPS_27}, {EPS27/CONS_EPS_27-1:+.1%}) NM {NI27/REV27:.1%}")
    print(f"FY28 growth {G28:.2%} rev {REV28:.2f} (cons {CONS_REV_28}, {REV28/CONS_REV_28-1:+.1%}) EPS {EPS28:.2f} (cons {CONS_EPS_28}, {EPS28/CONS_EPS_28-1:+.1%})")
    print(f"FCF 12m {FCF_12M:.2f}; NC Oct27 {NC_OCT27:.2f} = {NC_PS:.2f}/sh")
    print(f"normal NL {NL_N:.0f} EB, rev {normal_rev():.2f}, EPS {N_BASE:.2f}")
    for s, v in zip(SCEN, SV):
        print(s[0], {k: round(x, 2) for k, x in v.items()}, f"{v['value']/PRICE-1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} ({WEIGHTED/PRICE-1:+.1%}); base {BASE_VALUE:.1f} ({UP_BASE:+.1%}) rule {RULE}")
    print("grid", [[round(v) for v in r] for r in VGRID], "above", sum(v > PRICE for r in VGRID for v in r), "25% below", sum(v <= PRICE * 0.75 for r in VGRID for v in r))
    print(f"need N {NEED_N:.2f} nm {NEED_NM:.1%} rev@30% {NEED_REV:.1f} ptb {NEED_PTB:.2f}; vs26 {NEED_VS_26:.0%} vs28 {NEED_VS_28:.0%}")
    print(f"revisit <= {REVISIT_LONG:.0f} >= {REVISIT_SHORT:.0f}")
    print(f"mcap {MCAP:.1f} EV {EV:.1f}; PE26 {PE26:.1f} PE27 {PE27:.1f} PE28 {PE28:.1f} cons {PEC27:.1f} {PEC28:.1f} normal {PE_NORMAL:.1f} run {PE_RUN:.1f}")
    print("peers", [(n, round(x, 1)) for n, x in PEER_PE])
    print(f"cycle nm {CYC_NM:.1%} gm {CYC_GM:.1%}; GM by year {[round(g*100,1) for g in GM_H]}; FY23 fall {FY23_REV_FALL:.0%}")
    print(f"off high {OFF_HIGH:+.1%} since dec {SINCE_DEC25:+.0%} oct {OCT_FALL:+.1%} toshiba day {TOSHIBA_DAY:+.1%} Q1 NM {Q1_NM:.1%}")
