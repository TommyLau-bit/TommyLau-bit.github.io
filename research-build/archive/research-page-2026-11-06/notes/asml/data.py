"""ASML Holding N.V. (Euronext Amsterdam: ASML; Nasdaq: ASML) initiation, draft of 7 Oct 2026. Single source of figures
for charts, note and model.

Sources: ASML Annual Report 2025 on Form 20-F (filed 25 Feb 2026): net system sales by technology and end use, total net
sales by region, customer concentration, cost of system and service sales, free cash flow, 2030 opportunity table from the
November 2024 Investor Day, export control wording, financial calendar. ASML Q4 2025 results (Form 6-K, 28 Jan 2026):
backlog, bookings, 2025 figures, buyback programme. ASML Q2 2026 results (Form 6-K, 15 Jul 2026): release (Ex. 99.1),
presentation (Ex. 99.2) and US GAAP statements (Ex. 99.3). ASML's own transcript of its Q2 2026 prepared remarks
(asml.com, 15 Jul 2026); the Q&A as transcribed by Webull.
Prices: Euronext Amsterdam historical data (live.euronext.com, ISIN NL0010273215), retrieved 7 Oct 2026; Euronext returns two
years. (Yahoo Finance chart API refused requests with "Too Many Requests" on 7 Oct 2026.) Nasdaq ADR and peer closes:
stockanalysis.com history pages, retrieved 7 Oct 2026. ECB euro reference rates, 6 Oct 2026.
Consensus: stockanalysis.com (S&P Global) for 2026 EPS in euros; Zacks for the ADR's 2026 and 2027 EPS in US dollars,
converted at the ECB rate; peers from Zacks (US listings) and stockanalysis.com (Tokyo Electron). All retrieved 7 Oct 2026.
Everything marked MINE is my own estimate. Calendar year = fiscal year. EUR million unless stated; per-share in EUR.
"""
import statistics

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-07"
DATE_LONG = "7 October 2026"
COMPANY = "ASML"
NAME = "ASML Holding"
SLUG = "asml"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/asml"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",        # e.g. "INITIATE AT NO CALL" / "INITIATE AT LONG" once Tommy decides
    direction="NO CALL",
    target=None,                    # EUR per share; None for NO CALL
    conviction="Medium",
    draft=False,
)

# ---- Market data (Euronext Amsterdam historical data, retrieved 7 Oct 2026) ----
PRICE = 1636.40         # Euronext Amsterdam close, 6 Oct 2026
PRICE_DATE = "6 October 2026"
HI_CLOSE = 1721.40      # highest close of the past year, 30 Jun 2026
HI52 = 1741.00          # intraday high of the past year, also 30 Jun 2026
LO_CLOSE = 813.90       # lowest close of the past year, 10 Oct 2025
LO52 = 812.60           # intraday low of the past year, 8 Oct 2025
PRICE_DEC25 = 921.40    # close, 31 Dec 2025
PRICE_DEC24 = 678.70    # close, 31 Dec 2024
PX_RESULTS = (1555.80, 1549.40)  # closes 14 and 15 Jul 2026 (Q2 results before the open on 15 Jul)
PX_JUL_END = 1434.20    # close, 31 Jul 2026
PX_LABELS = ['Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25',
             'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26', '6 Oct 26']
PX = [621.2, 658.4, 678.7, 722.7, 678.6, 606.0, 582.5, 653.9, 677.6, 613.1, 636.6, 828.1,
      918.1, 903.4, 921.4, 1215.6, 1233.4, 1119.2, 1222.4, 1384.8, 1721.4, 1434.2, 1451.8, 1596.8, 1636.4]
# Month-end closes from Euronext; Oct 24 is the close on 31 Oct 2024, the last point the 6 Oct 2026 close.
ADR_PRICE = 1834.10     # Nasdaq ADR close, 6 Oct 2026 (stockanalysis.com)
EURUSD = 1.1269         # ECB reference rate, 6 Oct 2026
EURJPY = 178.15         # ECB reference rate, 6 Oct 2026
SHARES_OUT = 384.1      # m shares outstanding (stockanalysis.com, 7 Oct 2026)

# ---- Consensus (retrieved 7 Oct 2026) ----
CONS_EPS_26_SA = 38.35  # stockanalysis.com (S&P Global), EUR, 2026 EPS average (31 EPS estimates; 40 analysts on revenue), updated 6 Oct 2026
CONS_REV_26_SA = 42884.0  # EUR m, same; below ASML's own EUR 43bn to 45bn guide, so partly stale
CONS_EPS_USD = (43.86, 58.27)   # Zacks, ADR EPS in US$, 2026 and 2027 (7 estimates each)
CONS_EPS_26 = CONS_EPS_USD[0] / EURUSD   # converted at the ECB rate of 6 Oct 2026
CONS_EPS_27 = CONS_EPS_USD[1] / EURUSD
CONS_TP_USD = 2107.0    # average analyst target for the ADR, 42 analysts (stockanalysis.com, 6 Oct 2026)
# Peers: company, listing, close 6 Oct 2026, consensus EPS for the fiscal year ending in 2027, currency, year end, source, what
PEERS = [
    ("Applied Materials", "Nasdaq: AMAT", 530.27, 18.30, "US$", "Oct 2027", "Zacks", "Deposition, etch, ion implant, inspection"),
    ("Lam Research", "Nasdaq: LRCX", 333.89, 9.32, "US$", "Jun 2027", "Zacks", "Etch and deposition"),
    ("KLA", "Nasdaq: KLAC", 197.46, 5.44, "US$", "Jun 2027", "Zacks", "Inspection and metrology"),
    ("Tokyo Electron", "Tokyo: 8035", 12805.0, 344.66, "JPY", "Mar 2027", "stockanalysis.com", "Coater/developers, etch, deposition, cleaning"),
]

# ---- Annual reported (20-F 2025; Q4 2025 release), EUR m ----
YEARS_H = ["2023", "2024", "2025"]
REV_H = [27558.5, 28262.9, 32667.3]
SYS_H = [21938.6, 21768.7, 24474.3]
IBM_H = [5619.9, 6494.2, 8193.0]
NXE_H = [9124.0, 7856.4, 10445.8]      # low NA EUV system sales
NXE_U = [53, 42, 44]
EXE_H = [0.0, 465.0, 1156.9]           # High NA
EXE_U = [0, 2, 4]
ARFI_H = [9017.4, 9667.0, 10311.4]
ARFI_U = [125, 129, 131]
EUV_H = [n + e for n, e in zip(NXE_H, EXE_H)]
NONEUV_H = [s - e for s, e in zip(SYS_H, EUV_H)]
GP_H = [14136.1, 14492.0, 17258.0]
COST_SYS_H = [None, 10406.9, 11384.0]
COST_SVC_H = [None, 13770.9 - 10406.9, 15409.3 - 11384.0]
RD_H = [None, 4303.7, 4698.8]
SGA_H = [None, 1165.7, 1257.8]
EBIT_H = [None, 9022.6, 11301.4]
NI_H = [7839.0, 7571.6, 9609.4]
EPS_H = [19.91, 19.25, 24.73]          # basic; 2025 diluted 24.71
EPS_DIL_25 = 24.71
EPS_DIL_H = [19.89, 19.24, 24.71]   # diluted
SH_DIL_H = [394.1, 393.6, 388.9]
FCF_H = [None, 11166.2 - 2067.2 - 15.9, 12658.5 - 1573.6 - 57.6]
DPS_H = [6.10, 6.40, 7.50]
CHINA_H = [7251.8, 10195.1, 9519.7]    # total net sales to customers in China
TAIWAN_25, KOREA_25 = 8337.9, 8159.6
TOP4_25 = (20.0, 0.612)                # four customers above 10% each: EUR bn, share of total net sales
BACKLOG_25 = 38797.0
BOOK_25 = 28035.0
EUV_UNITS_SOLD = [("2020", 31), ("2021", 42), ("2022", 40), ("2023", 53), ("2024", 44), ("2025", 48)]
EUV_UNITS_H126 = 32                    # 16 in Q1 and 16 in Q2 2026, including High NA
CAP = dict(c26=65, c27=85, c28=110, arfi26=130)

# ---- Quarters (Q2 2026 statements and presentation) ----
QL = ["Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26 guide"]
Q_SYS = [5596.1, 5553.8, 7584.0, 6279.4, 6564.8, None]
Q_IBM = [2095.6, 1962.2, 2134.1, 2487.5, 2761.7, 2900.0]
Q_REV = [7691.7, 7516.0, 9718.1, 8766.9, 9326.5, 11500.0]   # Q3 guide midpoint of EUR 11.0bn to 12.0bn
Q_GM = [0.537, 0.516, 0.522, 0.530, 0.540, 0.56]
Q_EUV_SHARE = {"Q1 26": 0.66, "Q2 26": 0.57}   # EUV share of net system sales (slides)
Q_EUV_Q226 = 3800.0                    # EUR m, Q2 2026 EUV system sales including one High NA (call)
Q_CHINA_SYS = {"Q1 26": 0.19, "Q2 26": 0.14}  # China share of net system sales (slides)
H1 = dict(rev=18093.4, sys=12844.2, ibm=5249.2, gp=9680.4, rd=2461.5, sga=605.0, ebit=6613.9, ni=5674.3, eps=14.74,
          int=70.9, eqm=145.7, ocf=-482.5, capex=701.8, intang=106.6, cash=7582.0, ltdebt=1984.4, equity=21825.4,
          ibm_h125=4096.7, sh_dil=385.3)
NET_CASH = H1["cash"] - H1["ltdebt"]   # cash and short-term investments less long-term debt, 28 Jun 2026
G26 = dict(rev_lo=43000.0, rev_hi=45000.0, gm_lo=0.54, gm_hi=0.56, tax=0.17, q3_lo=11000.0, q3_hi=12000.0, q3_ibm=2900.0,
           q3_rd=1200.0, q3_sga=400.0, euv_g=0.45, noneuv_g=0.25, ibm_g=0.30, china=0.20)
INVESTOR_DAY_2030 = dict(low=(22, 11, 11, 44), moderate=(26, 14, 12, 52), high=(32, 15, 13, 60), gm=(0.56, 0.60))
Q3_DATE = "14 October 2026"           # ASML financial calendar (20-F 2025, p. 339)
CMD_DATE = "10 June 2027"

# ---- MY assumptions: 2026 from ASML's growth guides ----
EUV_G26 = 0.47          # MINE: "over 45%"
NONEUV_G26 = 0.25       # guide "around 25%"
IBM_G26 = 0.32          # MINE: "over 30%"; H1 +28.1%, Q3 guide +48%
HNA_U = [3, 5, 8]       # MINE: High NA units recognised 2026, 2027, 2028
HNA_ASP = 300.0         # MINE: EUR m per High NA system; 2025 was 1,156.9 / 4 = 289
LNA_U = [65, 85, 100]   # 2026 = stated capacity and expected shipments; 2027 = planned capacity; 2028 MINE
ASP_G = [0.05, 0.03]    # MINE: low NA price and mix, 2027 and 2028 (CFO: 2027 EUV mix "more positive")
NONEUV_G = [0.08, 0.05] # MINE: 2027, 2028
IBM_G = [0.10, 0.10]    # MINE: 2027, 2028
GM = [0.550, 0.565, 0.575]   # MINE: 2026 guide 54% to 56%; Investor Day 2030 range 56% to 60%
RD = [H1["rd"] + 1200.0 + 1250.0, 5400.0, 5900.0]   # MINE beyond the Q3 guide
SGA = [H1["sga"] + 400.0 + 420.0, 1550.0, 1650.0]
INT = [150.0, 100.0, 100.0]  # MINE: interest and other
EQM = [250.0, 250.0, 250.0]  # MINE: profit from equity method investments (H1 2026: 145.7)
TAX = 0.17
SH = [384.5, 382.0, 379.5]   # MINE: diluted shares, m; EUR 12bn buyback over 2026 to 2028, net of employee plans
MULT = 28               # MINE: P/E on 2028E, one year forward in October 2027

EUV26 = EUV_H[2] * (1 + EUV_G26)
LNA_ASP26 = (EUV26 - HNA_U[0] * HNA_ASP) / LNA_U[0]


def model(lna28=LNA_U[2], asp28=ASP_G[1], hna28=HNA_U[2], noneuv28=NONEUV_G[1], ibm28=IBM_G[1], gm28=GM[2]):
    """Returns per-year dicts for 2026, 2027, 2028."""
    out = []
    asp = [LNA_ASP26, LNA_ASP26 * (1 + ASP_G[0])]
    asp.append(asp[1] * (1 + asp28))
    lna = [LNA_U[0], LNA_U[1], lna28]
    hna = [HNA_U[0], HNA_U[1], hna28]
    noneuv = [NONEUV_H[2] * (1 + NONEUV_G26)]
    noneuv.append(noneuv[0] * (1 + NONEUV_G[0])); noneuv.append(noneuv[1] * (1 + noneuv28))
    ibm = [IBM_H[2] * (1 + IBM_G26)]
    ibm.append(ibm[0] * (1 + IBM_G[0])); ibm.append(ibm[1] * (1 + ibm28))
    gm = [GM[0], GM[1], gm28]
    for i in range(3):
        lna_s = lna[i] * asp[i]; hna_s = hna[i] * HNA_ASP
        if i == 0:
            lna_s = EUV26 - hna_s
        sysv = lna_s + hna_s + noneuv[i]
        rev = sysv + ibm[i]
        gp = rev * gm[i]
        ebit = gp - RD[i] - SGA[i]
        pbt = ebit + INT[i]
        ni = pbt * (1 - TAX) + EQM[i]
        out.append(dict(lna_u=lna[i], asp=asp[i], lna=lna_s, hna=hna_s, euv=lna_s + hna_s, noneuv=noneuv[i], sys=sysv,
                        ibm=ibm[i], rev=rev, gm=gm[i], gp=gp, ebit=ebit, ni=ni, eps=ni / SH[i]))
    return out


M = model()
Y26, Y27, Y28 = M
EPS26, EPS27, EPS28 = (y["eps"] for y in M)
BASE_VALUE = EPS28 * MULT

#        name, low NA units 28, ASP step 28, High NA units 28, non-EUV growth 28, IBM growth 28, GM 28, multiple, prob
SCEN = [
    ("Bear", 85, 0.00, 4, -0.10, 0.03, 0.550, 22, 0.25),
    ("Base", LNA_U[2], ASP_G[1], HNA_U[2], NONEUV_G[1], IBM_G[1], GM[2], MULT, 0.50),
    ("Bull", 110, 0.05, 10, 0.10, 0.12, 0.590, 32, 0.25),
]


def scen_value(s):
    y = model(*s[1:7])[2]
    return dict(eps=y["eps"], rev=y["rev"], value=y["eps"] * s[7], y=y)


SV = [scen_value(s) for s in SCEN]
VALS = [v["value"] for v in SV]
WEIGHTED = sum(v * s[8] for v, s in zip(VALS, SCEN))
assert abs(VALS[1] - BASE_VALUE) < 1e-6

# Sensitivity: 2028 low NA units against the multiple
SENS_U = [85, 100, 110]
SENS_X = [24, 28, 32]
VGRID = [[model(lna28=u)[2]["eps"] * x for x in SENS_X] for u in SENS_U]
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75

# What the price needs: 2028 EPS at the base multiple, and the low NA units that give it (other base assumptions)
NEED_EPS = PRICE / MULT
lo, hi = 50.0, 150.0
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if model(lna28=mid)[2]["eps"] < NEED_EPS else (lo, mid)
NEED_UNITS = round((lo + hi) / 2, 2)

# ---- DCF cross-check (MINE), valued at the end of 2027, to compare with the twelve-month base ----
COE = 0.085             # MINE: cost of equity
FCF_CONV = 0.95         # MINE: free cash flow / net income (2024: 120%; 2025: 115%, helped by down payments)
FCF_CONV_HIST = 1.15    # 2025 actual conversion, shown as the alternative
DCF_G = [0.10, 0.08, 0.06, 0.05]   # MINE: net income growth 2029 to 2032
TG = 0.03               # MINE: terminal growth from 2033
NET_CASH_PS = NET_CASH / SHARES_OUT   # held flat: buybacks and dividends absorb free cash flow (MINE)


def dcf(ni28=Y28["ni"], g=DCF_G, coe=COE, tg=TG, conv=FCF_CONV):
    ni = [ni28]
    for x in g:
        ni.append(ni[-1] * (1 + x))
    fcf = [n * conv for n in ni]
    pv = sum(f / (1 + coe) ** (i + 1) for i, f in enumerate(fcf))
    tv = fcf[-1] * (1 + tg) / (coe - tg) / (1 + coe) ** len(fcf)
    return (pv + tv) / SH[2] + NET_CASH_PS, pv, tv


DCF_VALUE, DCF_PV, DCF_TV = dcf()
lo, hi = 0.0, 0.5
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if dcf(g=[mid] * 4)[0] < PRICE else (lo, mid)
DCF_NEED_G = round((lo + hi) / 2, 4)   # flat growth 2029 to 2032 the price needs, at 8.5% and 3%
DCF_VALUE_HIST = dcf(conv=FCF_CONV_HIST)[0]
lo, hi = -0.2, 0.5
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if dcf(g=[mid] * 4, conv=FCF_CONV_HIST)[0] < PRICE else (lo, mid)
DCF_NEED_G_HIST = round((lo + hi) / 2, 4)
FCF_CONV_ACT = [f / n for f, n in zip(FCF_H[1:], NI_H[1:])]

# ---- Value, multiples ----
MCAP = PRICE * SHARES_OUT / 1000            # EUR bn
EV = MCAP - NET_CASH / 1000
EV_EBIT27 = EV * 1000 / Y27["ebit"]
EV_EBIT28_BASE = (BASE_VALUE * SHARES_OUT / 1000 - NET_CASH / 1000) * 1000 / Y28["ebit"]
PE_C26, PE_C27 = PRICE / CONS_EPS_26, PRICE / CONS_EPS_27
PE_C26_SA = PRICE / CONS_EPS_26_SA
PE_ADR27 = ADR_PRICE / CONS_EPS_USD[1]
PE26, PE27, PE28 = PRICE / EPS26, PRICE / EPS27, PRICE / EPS28
PEER_PE = [(p[0], p[2] / p[3]) for p in PEERS]
PEER_MED = statistics.median([x[1] for x in PEER_PE])
SINCE_DEC25 = PRICE / PRICE_DEC25 - 1
OFF_HIGH = PRICE / HI_CLOSE - 1
UP_YEAR = PRICE / LO_CLOSE - 1
CHINA_SH = [c / r for c, r in zip(CHINA_H, REV_H)]
SYS_GM_H = [None] + [(s - c) / s for s, c in zip(SYS_H[1:], COST_SYS_H[1:])]
IBM_GM_H = [None] + [(i - c) / i for i, c in zip(IBM_H[1:], COST_SVC_H[1:])]
BACKLOG_MONTHS = BACKLOG_25 / SYS_H[2] * 12
FWD_PE_DEC24 = PRICE_DEC24 / EPS_DIL_H[2]   # close end 2024 over 2025 actual diluted EPS
FWD_PE_DEC25 = PRICE_DEC25 / EPS26      # close end 2025 over my 2026E
IBM_G_H126 = H1["ibm"] / H1["ibm_h125"] - 1
EUV_Q126 = Q_EUV_SHARE["Q1 26"] * Q_SYS[3]
NXE_ASP_H = [n / u for n, u in zip(NXE_H, NXE_U)]
EXE_ASP_25 = EXE_H[2] / EXE_U[2]

if __name__ == "__main__":
    for yr, y in zip(["2026", "2027", "2028"], M):
        print(yr, f"lna {y['lna_u']} asp {y['asp']:.1f} lna {y['lna']:,.0f} hna {y['hna']:,.0f} euv {y['euv']:,.0f} noneuv {y['noneuv']:,.0f} "
                  f"ibm {y['ibm']:,.0f} rev {y['rev']:,.0f} gm {y['gm']:.1%} ebit {y['ebit']:,.0f} ni {y['ni']:,.0f} eps {y['eps']:.2f}")
    print(f"cons26 {CONS_EPS_26:.2f} (SA {CONS_EPS_26_SA}) mine {EPS26/CONS_EPS_26-1:+.1%}; cons27 {CONS_EPS_27:.2f} mine {EPS27/CONS_EPS_27-1:+.1%}")
    for s, v in zip(SCEN, SV):
        print(s[0], f"eps {v['eps']:.2f} rev {v['rev']:,.0f} value {v['value']:.0f} ({v['value']/PRICE-1:+.1%})")
    print(f"weighted {WEIGHTED:.0f} ({WEIGHTED/PRICE-1:+.1%}); base {BASE_VALUE:.0f} ({BASE_VALUE/PRICE-1:+.1%}); revisit {REVISIT_LONG:.0f} / {REVISIT_SHORT:.0f}")
    print("grid", [[round(v) for v in r] for r in VGRID])
    print(f"dcf hist {DCF_VALUE_HIST:.0f} need g hist {DCF_NEED_G_HIST:.2%} conv act {FCF_CONV_ACT}"); print(f"need eps {NEED_EPS:.2f} units {NEED_UNITS}; dcf {DCF_VALUE:.0f} pv {DCF_PV:,.0f} tv {DCF_TV:,.0f}; dcf need g {DCF_NEED_G:.2%}")
    print(f"mcap {MCAP:.1f} ev {EV:.1f} ev/ebit27 {EV_EBIT27:.1f} base ev/ebit28 {EV_EBIT28_BASE:.1f}; net cash {NET_CASH:,.0f} ps {NET_CASH_PS:.1f}")
    print(f"PE cons26 {PE_C26:.1f} SA {PE_C26_SA:.1f} cons27 {PE_C27:.1f} adr27 {PE_ADR27:.1f}; mine {PE26:.1f} {PE27:.1f} {PE28:.1f}")
    print("peers", [(n, round(x, 1)) for n, x in PEER_PE], "median", round(PEER_MED, 1))
    print(f"china {[round(c*100,1) for c in CHINA_SH]}; sys gm {SYS_GM_H}; ibm gm {IBM_GM_H}; backlog months {BACKLOG_MONTHS:.1f}")
    print(f"fwd pe dec24 {FWD_PE_DEC24:.1f} dec25 {FWD_PE_DEC25:.1f}; since dec25 {SINCE_DEC25:+.1%} off high {OFF_HIGH:+.1%} up yr {UP_YEAR:+.1%}")
    print(f"ibm h1 growth {IBM_G_H126:.1%}; euv q1 {EUV_Q126:.0f}; nxe asp {[round(a,1) for a in NXE_ASP_H]} exe {EXE_ASP_25:.1f}; lna asp26 {LNA_ASP26:.1f}; euv26 {EUV26:,.0f}")
    print(f"adr implied eur {ADR_PRICE/EURUSD:.1f}; target eur {CONS_TP_USD/EURUSD:.0f}")
