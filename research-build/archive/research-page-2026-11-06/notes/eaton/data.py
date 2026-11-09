"""Eaton Corporation plc (NYSE: ETN) initiation, drafted 26 Oct 2026. Single source of figures for charts, note and model.

Fiscal year = calendar year. US$ million unless stated.
Sources (SEC EDGAR, Eaton CIK 1551182):
- Q2 2026 earnings release, Form 8-K Ex. 99, 31 Jul 2026 (etn06302026exhibit99.htm): segment sales and operating profit,
  income statement, adjusted EPS bridge, balance sheet at 30 Jun 2026, 2026 and Q3 2026 guidance, Mobility/Dana note.
- Form 10-Q for the quarter to 30 Jun 2026, filed 31 Jul 2026: Electrical Americas backlog $15,175m, book-to-bill 1.3,
  margin bridge (470 bps commodity inflation, +260 bps sales), total backlog ~$24.1bn (71% within 12 months),
  388.4m shares outstanding at 30 Jun 2026, no share repurchases in H1 2026.
- Form 10-Qs for Q1 2025 (EA backlog $10,050m), Q3 2025, Q1 2026; Form 10-K 2025 (EA backlog Dec 2024 and Dec 2025).
- Quarterly earnings releases (Form 8-K Ex. 99) from Q2 2024 to Q1 2026: segment sales and operating profit by quarter.
- Form 8-K of 11 Jun 2026, Ex. 99.1: Mobility combined with Dana in a Reverse Morris Trust, Mobility valued at about
  $5.1bn, ~$1.1bn cash to Eaton, Eaton shareholders own at least 50.1% of the combined company, close Q1 2027.
- Form 8-K of 16 Oct 2026: recast 2025 segment information (Mobility = Vehicle + eMobility). No new results.
- Eaton press release (Business Wire, via Yahoo Finance and MarketScreener): Q3 2026 results on 3 Nov 2026, before the
  NYSE opens. Q3 2026 was not out on 26 Oct 2026.
- Q2 2026 earnings call, 31 Jul 2026, third-party transcript (Motley Fool via The Globe and Mail).
Prices: Yahoo Finance chart API (ETN), read through a browser fetch on 26 Oct 2026 because curl returned
"Too Many Requests". Consensus, targets and peer multiples: stockanalysis.com (S&P Global data), retrieved 26 Oct 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-26"
COMPANY = "Eaton"
SLUG = "eaton"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/eaton"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call (Tommy Lau, 26 Oct 2026). Rebuild = edit this dict only. ----
CALL = dict(
    banner="LONG",
    direction="LONG",
    target=430.0,
    conviction="Low",
    draft=False,
)

# ---- Market data (Yahoo Finance ETN, retrieved 26 Oct 2026) ----
PRICE = 366.11              # NYSE close, Friday 23 Oct 2026
PRICE_DATE = "23 October 2026"
HI_CLOSE = 459.96           # highest close, 12 Aug 2026
HI_INTRA = 478.00           # intraday high, also 12 Aug 2026
PX_DEC25 = 318.51           # close 31 Dec 2025
PX_OCT13 = 428.31           # close 13 Oct 2026, before the October fall
PX_Q1_PRE, PX_Q1_DAY = 422.44, 410.86   # closes 4 and 5 May 2026 (Q1 results 5 May, before the open)
PX_Q2_PRE, PX_Q2_DAY = 386.89, 415.20   # closes 30 and 31 Jul 2026 (Q2 results 31 Jul, before the open)
PX_OCT21, PX_OCT22 = 393.94, 368.99     # closes 21 and 22 Oct 2026

# ---- Shares and balance sheet, 30 Jun 2026 (Q2 release and 10-Q) ----
SHARES_OUT = 388.4          # m, outstanding at 30 Jun 2026
SHARES_DIL = 389.5          # m, diluted, Q2 2026
CASH = 483.0 + 212.0        # cash + short-term investments
DEBT = 2091.0 + 11.0 + 18509.0
NCI = 45.0

# ---- Group, annual ----
GROUP_SALES = {"2024A": 24878.0, "2025A": 27448.0}
SEG_MARGIN = {"2024A": 0.240, "2025A": 0.245}     # segment margins as Eaton reports them (2025: 24.5%)
ADJ_EPS = {"2024A": 10.80, "2025A": 12.07}
GUIDE26 = dict(eps_lo=13.40, eps_hi=13.60, gaap_lo=10.36, gaap_hi=10.56, org_lo=0.11, org_hi=0.13, m_lo=0.241, m_hi=0.245)
GUIDE26_FEB = dict(eps_lo=13.00, eps_hi=13.50)    # first 2026 guide (Q4 2025 release)
GUIDE_Q3 = dict(eps_lo=3.46, eps_hi=3.56, org_lo=0.135, org_hi=0.155, m_lo=0.246, m_hi=0.250)
Q3_25_EPS = 3.07
H1_26_EPS = 5.96

# ---- Segments: sales and operating profit by quarter (Eaton releases), US$m ----
Q = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
EA_S = [2690, 2877, 2963, 2905, 3010, 3350, 3410, 3506, 3600, 3951]
EA_P = [785, 859, 892, 918, 904, 987, 1034, 1046, 922, 1088]
EA_M = [round(p / s * 100, 1) for p, s in zip(EA_P, EA_S)]
# Electrical Americas backlog (10-K / 10-Q), US$m
BL_LABELS = ["Dec 24", "Mar 25", "Jun 25", "Sep 25", "Dec 25", "Mar 26", "Jun 26"]
EA_BL = [10141, 10050, 11377, 12009, 13246, 14459, 15175]
EA_TTM = [sum(EA_S[i - 3:i + 1]) for i in range(3, 10)]      # Q4 24 .. Q2 26
EA_RATIO = [b / t for b, t in zip(EA_BL, EA_TTM)]
EA_MONTHS = [r * 12 for r in EA_RATIO]
EA_BTB = 1.3                # EA book-to-bill, twelve months, Q2 2026 (10-Q)
EA_ORDERS = 0.41            # EA twelve-month rolling orders, organic, Q2 2026
EA_SALES_GROWTH_TTM = EA_TTM[-1] / EA_TTM[2] - 1
EA_BL_GROWTH = EA_BL[-1] / EA_BL[2] - 1
TOTAL_BL = 24.1             # US$bn, group firm backlog, 30 Jun 2026 (71% for delivery within 12 months)

# H1 2026 actual by segment (Q2 release)
H1 = dict(EA=(7551, 2010), EG=(4463, 873), AE=(2362, 582), MO=(1607, 198))
SEG25 = dict(EA=(13276, 3972), EG=(6815, 1323), AE=(4249, 1013), MO=(3109, 405))   # FY2025, Mobility = Vehicle + eMobility
H1_CORP, H1_INT, H1_PENS = 392.0, 307.0, 6.0    # H1 2026: other expense net 655 less acquisition charges 263; interest; pension

# ---- MY estimates: second half of 2026, by segment (sales, margin) ----
H2 = dict(EA=(3990 + 4100, 0.305), EG=(2450 + 2450, 0.21), AE=(1230 + 1255, 0.25), MO=(780 + 760, 0.13))
CORP26, INT26, PENS = 790.0, 710.0, 10.0
TAX = 0.19
NCI_INC = 5.0

# ---- MY assumptions, 2027 and 2028, continuing operations (Mobility out from 1 Jan 2027, pro forma) ----
EA_G27, EA_G28 = 0.16, 0.13
EA_M27, EA_M28 = 0.300, 0.305
EG_G27, EG_G28 = 0.10, 0.10
BOYD_STUB = 350.0           # extra Boyd Thermal sales in Q1 2027 against the stub period after 12 Mar 2026 (MINE)
EG_M27, EG_M28 = 0.21, 0.215
AE_G27, AE_G28 = 0.09, 0.08
AE_M27, AE_M28 = 0.25, 0.25
CORP27, CORP28 = 760.0, 790.0
INT27, INT28 = 680.0, 580.0
MOB_EQUITY = 4.0            # US$bn: Mobility valued at ~$5.1bn less ~$1.1bn cash = shares to Eaton holders (my inference)
SHARES_RETIRED = 10.0       # m, MINE: split-off exchange offer retires about US$4.0bn of Eaton shares at a ~7% discount
SHARES_27 = SHARES_DIL - SHARES_RETIRED
BASE_PE = 23.0

CONS_EPS26, CONS_EPS27 = 13.60, 16.30     # stockanalysis.com (S&P Global), updated 20 Oct 2026
CONS_REV26, CONS_REV27 = 32.90, 36.94
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 485.47, 28, 333.0, 534.0
FWD_PE_SA = 24.17
EV_EBIT_SA = 29.85
HIST_FWD_PE = {"2021": 23.90, "2022": 19.46, "2023": 24.54, "2024": 28.24, "2025": 23.84}   # stockanalysis.com
HIST_FWD_PE_AVG = sum(HIST_FWD_PE.values()) / 5

PEERS = [  # company, ticker, forward P/E, trailing EV/EBIT, what they make, group
    ("Eaton", "NYSE: ETN", 24.17, 29.85, "Switchgear, UPS, busway, power enclosures, liquid cooling; aerospace", "self"),
    ("Vertiv", "NYSE: VRT", 24.53, 32.75, "Data centre power, thermal and liquid cooling", "peer"),
    ("ABB", "SWX: ABBN", 22.45, 22.90, "Electrification and automation equipment", "peer"),
    ("nVent", "NYSE: NVT", 21.11, 26.51, "Enclosures, electrical connections, liquid cooling", "peer"),
    ("Hubbell", "NYSE: HUBB", 20.53, 22.52, "Utility and electrical components", "peer"),
    ("Siemens", "ETR: SIE", 20.36, 22.99, "Smart infrastructure, automation, rail, software", "peer"),
    ("Legrand", "EPA: LR", 19.19, 20.13, "Electrical and digital building infrastructure, data centre white space", "peer"),
    ("Schneider Electric", "EPA: SU", 19.13, 19.48, "Electrical distribution, automation, data centre power and cooling", "peer"),
]

# ---- Projection ----
def seg26():
    out = {}
    for k in ("EA", "EG", "AE", "MO"):
        s = H1[k][0] + H2[k][0]
        p = H1[k][1] + H2[k][0] * H2[k][1]
        out[k] = (s, p)
    return out


S26 = seg26()
SALES26 = sum(v[0] for v in S26.values())
OP26 = sum(v[1] for v in S26.values())
SEGM26 = OP26 / SALES26
EPS26 = ((OP26 - CORP26 - INT26 + PENS) * (1 - TAX) - NCI_INC) / SHARES_DIL
EA_M26 = S26["EA"][1] / S26["EA"][0]
EA_G26 = S26["EA"][0] / SEG25["EA"][0] - 1


def project(ea_g27=EA_G27, ea_g28=EA_G28, ea_m27=EA_M27, ea_m28=EA_M28, dg=0.0, dm=0.0):
    """Continuing operations (EA, EG, AE), 2027 and 2028. dg / dm shift EG and AE growth / margin."""
    ea27 = S26["EA"][0] * (1 + ea_g27); ea28 = ea27 * (1 + ea_g28)
    eg27 = S26["EG"][0] * (1 + EG_G27 + dg) + BOYD_STUB; eg28 = eg27 * (1 + EG_G28 + dg)
    ae27 = S26["AE"][0] * (1 + AE_G27 + dg); ae28 = ae27 * (1 + AE_G28 + dg)
    p27 = dict(EA=ea27 * ea_m27, EG=eg27 * (EG_M27 + dm), AE=ae27 * (AE_M27 + dm))
    p28 = dict(EA=ea28 * ea_m28, EG=eg28 * (EG_M28 + dm), AE=ae28 * (AE_M28 + dm))
    s27 = dict(EA=ea27, EG=eg27, AE=ae27); s28 = dict(EA=ea28, EG=eg28, AE=ae28)
    op27, op28 = sum(p27.values()), sum(p28.values())
    e27 = ((op27 - CORP27 - INT27 + PENS) * (1 - TAX) - NCI_INC) / SHARES_27
    e28 = ((op28 - CORP28 - INT28 + PENS) * (1 - TAX) - NCI_INC) / SHARES_27
    return dict(s27=s27, s28=s28, p27=p27, p28=p28, op27=op27, op28=op28, e27=e27, e28=e28,
                sales27=sum(s27.values()), sales28=sum(s28.values()))


B = project()
E27, E28 = B["e27"], B["e28"]
BASE_VALUE = BASE_PE * E28
SCEN = [  # name, ea_g27, ea_g28, ea_m27, ea_m28, other growth delta, other margin delta, multiple, prob
    ("Bear", 0.08, 0.04, 0.285, 0.275, -0.03, -0.01, 18, 0.25),
    ("Base", EA_G27, EA_G28, EA_M27, EA_M28, 0.0, 0.0, BASE_PE, 0.50),
    ("Bull", 0.19, 0.16, 0.305, 0.315, 0.02, 0.005, 26, 0.25),
]
SC = []
for s in SCEN:
    pr = project(s[1], s[2], s[3], s[4], s[5], s[6])
    SC.append(dict(name=s[0], e28=pr["e28"], value=pr["e28"] * s[7], mult=s[7], prob=s[8], pr=pr))
WEIGHTED = sum(x["value"] * x["prob"] for x in SC)
SENS_EPS = [17.00, None, 20.50]
SENS_PE = [20, 23, 26]
SENS_EPS[1] = E28

# ---- Derived market figures ----
MCAP = PRICE * SHARES_OUT / 1000
NET_DEBT = DEBT - CASH
EV = MCAP + NET_DEBT / 1000 + NCI / 1000
PE_G26 = PRICE / ((GUIDE26["eps_lo"] + GUIDE26["eps_hi"]) / 2)
PE_C27 = PRICE / CONS_EPS27
PE_E27 = PRICE / E27
PE_E28 = PRICE / E28
PE_PEAK_G26 = HI_CLOSE / ((GUIDE26["eps_lo"] + GUIDE26["eps_hi"]) / 2)
OFF_HIGH = PRICE / HI_CLOSE - 1
YTD = PRICE / PX_DEC25 - 1
OCT_FALL = PRICE / PX_OCT13 - 1
Q1_MOVE = PX_Q1_DAY / PX_Q1_PRE - 1
Q2_MOVE = PX_Q2_DAY / PX_Q2_PRE - 1
OCT22_MOVE = PX_OCT22 / PX_OCT21 - 1
PE_FOR_LONG = PRICE * 1.15 / E28
IMPLIED_PE_E28 = PRICE / E28
UP_BASE = BASE_VALUE / PRICE - 1
LONG_BELOW = BASE_VALUE / 1.15

# ---- Price, month-end close (Yahoo Finance ETN, retrieved 26 Oct 2026) ----
PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24",
             "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
             "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26",
             "23 Oct 26"]
PX = [246.08, 289.00, 312.68, 318.26, 332.85, 313.55, 304.79, 306.93, 331.44, 331.58, 375.42, 331.87, 326.44, 293.32,
      271.83, 294.37, 320.20, 356.99, 384.72, 349.14, 374.25, 381.56, 345.89, 318.51, 351.42, 375.92, 357.67, 433.01,
      400.60, 426.12, 415.20, 401.88, 429.71, 366.11]

WRONG_IF = ("Electrical Americas operating margin is below 29 per cent in the fourth quarter of 2026, after Eaton said price "
            "and cost would be back in balance in the second half; or 2026 adjusted earnings per share land below the "
            "US$13.40 bottom of Eaton's guide; or Electrical Americas backlog over its previous four quarters of sales "
            "falls for two consecutive quarters before mid 2027.")

if __name__ == "__main__":
    print("EA ratio", [round(r, 3) for r in EA_RATIO], "months", [round(m, 1) for m in EA_MONTHS])
    print("EA TTM", EA_TTM, f"ttm growth {EA_SALES_GROWTH_TTM:.1%} bl growth {EA_BL_GROWTH:.1%}")
    print("2026 segs", {k: (round(v[0]), round(v[1]), f"{v[1] / v[0]:.1%}") for k, v in S26.items()})
    print(f"2026 sales {SALES26:.0f} OP {OP26:.0f} margin {SEGM26:.2%} EPS {EPS26:.2f}; EA margin {EA_M26:.1%} growth {EA_G26:.1%}")
    print("2027", {k: round(v) for k, v in B["s27"].items()}, {k: round(v) for k, v in B["p27"].items()}, round(B["op27"]), f"EPS {E27:.2f}")
    print("2028", {k: round(v) for k, v in B["s28"].items()}, {k: round(v) for k, v in B["p28"].items()}, round(B["op28"]), f"EPS {E28:.2f}")
    print(f"sales27 {B['sales27']:.0f} sales28 {B['sales28']:.0f}; margin27 {B['op27'] / B['sales27']:.1%} margin28 {B['op28'] / B['sales28']:.1%}")
    print(f"base {BASE_VALUE:.2f} {UP_BASE:+.1%}; long below {LONG_BELOW:.0f}; PE for long {PE_FOR_LONG:.1f}")
    for x in SC:
        print(x["name"], round(x["e28"], 2), x["mult"], round(x["value"], 1), f"{x['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}")
    print("grid", [[round(e * m) for m in SENS_PE] for e in SENS_EPS])
    print(f"mcap {MCAP:.1f} netdebt {NET_DEBT:.0f} EV {EV:.1f}; PE g26 {PE_G26:.1f} c27 {PE_C27:.1f} e27 {PE_E27:.1f} e28 {PE_E28:.1f} peak {PE_PEAK_G26:.1f}")
    print(f"off high {OFF_HIGH:.1%} ytd {YTD:.1%} oct {OCT_FALL:.1%} q1 {Q1_MOVE:+.1%} q2 {Q2_MOVE:+.1%} oct22 {OCT22_MOVE:+.1%} hist fwd {HIST_FWD_PE_AVG:.1f}")
    import statistics
    ps = [p for p in PEERS if p[5] == "peer"]
    print("peer median fwd", statistics.median(p[2] for p in ps), "EV/EBIT", statistics.median(p[3] for p in ps))
