"""Coherent Corp. (NYSE: COHR) initiation, drafted 2 Nov 2026. Single source of figures for charts, note and model.

Fiscal year ends 30 June (fiscal 2026 = year to 30 Jun 2026). US$ million unless stated.
Sources (SEC EDGAR, Coherent CIK 820318):
- Q4 FY26 results release, Form 8-K Ex. 99.1, 12 Aug 2026 (d128030dex991.htm): income statement, non-GAAP reconciliation,
  balance sheet at 30 Jun 2026, cash flow FY26, segment revenue, Q1 FY27 outlook.
- Q4 FY26 investor presentation, Form 8-K Ex. 99.2, 12 Aug 2026 (slides 5, 6, 8): quarterly segment revenue; "On track to
  double internal InP output by year-end and more than double again by 2027"; "6-inch platform producing EMLs, CW lasers,
  and photodiodes, with higher yields than 3-inch lines"; CPO/NPO new revenue H2 2026; transceivers 1.6T, 3.2T, 6.4T;
  US$50bn+ SAM existing and US$20bn+ incremental SAM (calendar 2030 estimates).
- Form 10-K for the year to 30 Jun 2026, filed 14 Aug 2026: 195,832,246 shares at 10 Aug 2026; segment profit (D&C 1,330 /
  904; Industrial 423 / 407); two customers each more than 10% of revenue; purchase commitments US$3.4bn in FY27 and
  US$8.4bn thereafter; Sherman InP expansion; Nvidia agreement and 7,788,161 shares at US$256.80 (Note 14, six-month lock-up).
- Quarterly results releases, Form 8-K Ex. 99.1, 6 Nov 2024 to 6 May 2026: revenue, segment revenue, margins, EPS, guidance.
  FY25 quarterly non-GAAP figures as recast in the FY26 releases (methodology refined in Q2 FY25).
- Form 8-K of 2 Mar 2026 (Item 3.02 and Ex. 99.1): Nvidia US$2bn private placement; multi-billion-dollar purchase commitment;
  access to five additional Coherent product families related to co-packaged optics.
- Form 8-K of 31 Aug 2026: special PSU awards with price hurdles US$454.43 to US$757.77.
- Coherent release of 14 Oct 2026 (via GlobeNewswire, Finviz, Earnings Whispers): Q1 FY27 results on Wednesday 4 Nov 2026
  after the NYSE close, webcast 4:30 p.m. ET. Not out on 2 Nov 2026.
- Q4 FY26 call, 12 Aug 2026, third-party transcript on stockanalysis.com (transcripts/661756-q4-2026); Coherent posts no
  transcript of its own that I could retrieve.
Prices: Nasdaq.com historical API (COHR), retrieved 2 Nov 2026; every close used cross-checked against the Yahoo Finance
chart API (fact-check, 2 Nov 2026). Consensus, targets and peer multiples: stockanalysis.com (S&P Global), updated 30 Oct 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "Coherent"
SLUG = "coherent"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/coherent"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Rebuild = edit this dict only. ----
CALL = dict(
    banner="LONG",              # Tommy Lau's call, 2 Nov 2026 (draft view published as his call)
    direction="LONG",
    target=275.0,
    conviction="Low",
    draft=False,
)

# ---- Market data (Nasdaq.com COHR history, retrieved 2 Nov 2026) ----
PRICE = 210.32              # NYSE close, Friday 30 Oct 2026
PRICE_DATE = "30 October 2026"
HI_CLOSE = 426.89           # highest close, 2 Jun 2026
HI_CLOSE_DATE = "2 June 2026"
HI_INTRA = 440.00           # intraday high, 3 Jun 2026
HI_INTRA_DATE = "3 June 2026"
PX_DEC25 = 184.57           # close 31 Dec 2025
PX_OCT6 = 338.36            # close 6 Oct 2026, the October high
PX_YAGO = 132.71            # close 30 Oct 2025
PX_OCT21, PX_OCT22 = 237.53, 207.82     # Nvidia release on SPIL capacity came on 21 Oct 2026
PX_OCT29 = 237.22
PX_AUG11, PX_AUG12, PX_AUG13 = 328.57, 355.64, 327.23   # Q4 results 12 Aug after the close
PX_MAR2_PRE, PX_MAR2 = 258.93, 298.91   # 27 Feb and 2 Mar 2026 (Nvidia investment, 2 Mar)
NV_PRICE = 256.80           # Nvidia's purchase price per share, 2 Mar 2026 (8-K Item 3.02)
NV_SHARES = 7.788161        # m

# ---- Shares and balance sheet, 30 Jun 2026 (Q4 release, 10-K) ----
SHARES_OUT = 195.832246     # m, 10 Aug 2026 (10-K cover)
SHARES_DIL_Q4 = 202.2       # m, diluted, Q4 FY26
CASH = 1162.0 + 825.0       # cash + short-term investments (restricted cash 606.4 left out)
DEBT = 7.9 + 3214.3
NCI = 334.7
INVENTORY = {"FY25": 1437.6, "FY26": 2581.0}
PAYABLES = {"FY25": 847.0, "FY26": 1905.4}
OCF = {"FY24": 545.7, "FY25": 633.6, "FY26": 79.5}
CAPEX = {"FY24": 346.8, "FY25": 440.8, "FY26": 1102.9}
PURCH_27, PURCH_LATER = 3.4, 8.4    # US$bn, purchase commitments (10-K Note 13)

# ---- Annual history (releases; FY25 and FY24 non-GAAP as recast) ----
REV = {"FY24": 4707.7, "FY25": 5810.1, "FY26": 7118.2}
DC = {"FY25": 3755.2, "FY26": 5274.6}
IND = {"FY25": 2054.9, "FY26": 1843.6}
SEGP = {"DC": (904.0, 1330.0), "IND": (407.0, 423.0)}     # FY25, FY26 segment profit (10-K)
NG_GM = {"FY25": 0.379, "FY26": 0.394}
GAAP_GM = {"FY25": 0.352, "FY26": 0.375}
NG_OPM = {"FY25": 0.178, "FY26": 0.205}
NG_EPS = {"FY24": 1.21, "FY25": 3.53, "FY26": 5.61}       # FY24 derived: FY25 3.53 "improved $2.32"
NG_OPEX26 = 1350.0
NG_INT26 = 118.1
TAX_NG = 0.19

# ---- Quarters, fiscal 2025 and 2026 (releases) ----
Q = ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26"]
QS = ["Sep 24", "Dec 24", "Mar 25", "Jun 25", "Sep 25", "Dec 25", "Mar 26", "Jun 26"]
Q_REV = [1348.1, 1434.7, 1497.9, 1529.4, 1581.4, 1685.6, 1805.6, 2045.5]
Q_DC = [863.6, 904.6, 968.7, 1018.3, 1090.0, 1208.0, 1361.6, 1615.0]
Q_IND = [round(a - b, 1) for a, b in zip(Q_REV, Q_DC)]
Q_NGGM = [36.7, 38.2, 38.5, 38.1, 38.7, 39.0, 39.6, 40.2]
Q_GAAPGM = [34.1, 35.5, 35.2, 35.7, 36.6, 36.9, 37.7, 38.5]
Q_NGOPM = [16.1, 18.5, 18.6, 18.0, 19.5, 19.9, 20.3, 21.8]
Q_EPS = [0.67, 0.95, 0.91, 1.00, 1.16, 1.29, 1.41, 1.74]

# ---- Guidance, Q1 FY27 (12 Aug 2026) ----
G_REV = (2200.0, 2400.0)
G_GM = (0.395, 0.415)
G_OPEX = (400.0, 420.0)
G_EPS = (1.85, 2.05)

# ---- MY estimates: fiscal 2027 by quarter ----
F27_REV = [2320.0, 2500.0, 2700.0, 2900.0]
F27_GM = [0.405, 0.410, 0.415, 0.420]
F27_OPEX = [410.0, 430.0, 455.0, 480.0]
INT27 = 120.0
SH27 = 204.0
# ---- MY estimates: fiscal 2028 (base) ----
G28 = 0.25
GM28 = 0.420
OPEX28 = 0.165
INT28 = 120.0
SH28 = 207.0
BASE_PE = 22.0

CONS_REV27, CONS_REV28 = 10630.0, 14690.0     # stockanalysis.com (S&P Global), updated 30 Oct 2026
CONS_EPS27, CONS_EPS28 = 9.40, 13.91
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 391.0, 26, 230.0, 500.0
FWD_PE_SA = 22.38
HIST_FWD_PE = {"FY23": 25.14, "FY24": 26.53, "FY25": 21.26}   # stockanalysis.com forward P/E at each year end
HIST_FWD_PE_AVG = sum(HIST_FWD_PE.values()) / 3
FWD_PE_PEAK = 53.01                                            # at 30 Jun 2026

PEERS = [  # company, ticker, forward P/E, what they make, group
    ("Coherent", "NYSE: COHR", 22.38, "Datacentre transceivers, InP and GaAs lasers, OCS; industrial lasers and materials", "self"),
    ("Lumentum", "Nasdaq: LITE", 38.53, "InP lasers (EMLs, CW), transceivers, optical circuit switches", "peer"),
    ("Marvell", "Nasdaq: MRVL", 34.76, "Optical DSPs, custom chips, switch silicon", "peer"),
    ("Ciena", "NYSE: CIEN", 30.81, "Long-haul and data centre interconnect optics", "peer"),
    ("Applied Optoelectronics", "Nasdaq: AAOI", 30.00, "Datacentre transceivers and lasers", "peer"),
    ("Broadcom", "Nasdaq: AVGO", 18.74, "Switch chips, optical DSPs, lasers, custom AI chips", "peer"),
    ("Fabrinet", "NYSE: FN", 17.95, "Contract assembly of optical modules", "peer"),
]


# ---- Projection ----
def fy27():
    gp = [r * g for r, g in zip(F27_REV, F27_GM)]
    oi = [g - o for g, o in zip(gp, F27_OPEX)]
    rev = sum(F27_REV); op = sum(oi)
    eps = (op - INT27) * (1 - TAX_NG) / SH27
    q1eps = (oi[0] - INT27 / 4) * (1 - TAX_NG) / 203.5
    return dict(rev=rev, gp=sum(gp), op=op, opm=op / rev, gm=sum(gp) / rev, eps=eps, q1eps=q1eps, oi=oi)


F27 = fy27()
E27 = F27["eps"]


def fy28(g=G28, gm=GM28, opex=OPEX28):
    rev = F27["rev"] * (1 + g)
    op = rev * (gm - opex)
    eps = (op - INT28) * (1 - TAX_NG) / SH28
    return dict(rev=rev, op=op, opm=gm - opex, eps=eps)


B = fy28()
E28 = B["eps"]
BASE_VALUE = BASE_PE * E28
SCEN = [  # name, growth 28, gross margin 28, opex % 28, multiple, prob
    ("Bear", 0.00, 0.375, 0.180, 14, 0.25),
    ("Base", G28, GM28, OPEX28, BASE_PE, 0.50),
    ("Bull", 0.40, 0.435, 0.160, 28, 0.25),
]
SC = []
for s in SCEN:
    pr = fy28(s[1], s[2], s[3])
    SC.append(dict(name=s[0], e28=pr["eps"], value=pr["eps"] * s[4], mult=s[4], prob=s[5], pr=pr))
WEIGHTED = sum(x["value"] * x["prob"] for x in SC)
SENS_EPS = [9.50, None, 15.00]
SENS_PE = [18, 22, 26]
SENS_EPS[1] = E28

# ---- Derived market figures ----
MCAP = PRICE * SHARES_OUT / 1000
NET_DEBT = DEBT - CASH
EV = MCAP + NET_DEBT / 1000 + NCI / 1000
PE_26 = PRICE / NG_EPS["FY26"]
PE_C27 = PRICE / CONS_EPS27
PE_C28 = PRICE / CONS_EPS28
PE_E27 = PRICE / E27
PE_E28 = PRICE / E28
EPS_IMPLIED = PRICE / BASE_PE          # FY28 EPS the price needs at the base multiple
OFF_HIGH = PRICE / HI_CLOSE - 1
YTD = PRICE / PX_DEC25 - 1
OCT_FALL = PRICE / PX_OCT6 - 1
YOY = PRICE / PX_YAGO - 1
VS_NV = PRICE / NV_PRICE - 1
OCT22_MOVE = PX_OCT22 / PX_OCT21 - 1
OCT30_MOVE = PRICE / PX_OCT29 - 1
UP_BASE = BASE_VALUE / PRICE - 1
LONG_BELOW = BASE_VALUE / 1.15
SHORT_ABOVE = BASE_VALUE / 0.75
FCF26 = OCF["FY26"] - CAPEX["FY26"]
DC_SHARE26 = DC["FY26"] / REV["FY26"]
DC_GROWTH26 = DC["FY26"] / DC["FY25"] - 1

# ---- Price, month-end close (Nasdaq.com COHR, retrieved 2 Nov 2026) ----
PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24",
             "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
             "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26",
             "30 Oct 26"]
PX = [47.54, 59.48, 60.62, 54.63, 57.06, 72.46, 69.68, 77.95, 88.91, 92.44, 100.16, 94.73, 90.49, 75.19, 64.94, 64.32,
      75.63, 89.21, 107.60, 90.47, 107.72, 131.96, 164.26, 184.57, 212.18, 258.93, 238.21, 319.71, 361.47, 394.47, 262.89,
      277.83, 287.81, 210.32]

WRONG_IF = ("Coherent's non-GAAP gross margin falls below 39 per cent in any quarter to June 2027, which would say it is "
            "buying volume with price; or fiscal 2027 revenue lands below US$9.5 billion; or, before October 2027, an Nvidia "
            "DGX SuperPOD reference architecture makes a co-packaged switch the default for the compute fabric, which "
            "would break the claim the call rests on.")

if __name__ == "__main__":
    print(f"FY27 rev {F27['rev']:.0f} gm {F27['gm']:.2%} op {F27['op']:.0f} opm {F27['opm']:.2%} EPS {E27:.2f} q1eps {F27['q1eps']:.2f}")
    print(f"FY28 rev {B['rev']:.0f} opm {B['opm']:.2%} EPS {E28:.2f}; vs cons {E27 / CONS_EPS27 - 1:+.1%} {E28 / CONS_EPS28 - 1:+.1%}")
    print(f"base {BASE_VALUE:.2f} {UP_BASE:+.1%}; implied EPS {EPS_IMPLIED:.2f}; long below {LONG_BELOW:.0f} short above {SHORT_ABOVE:.0f}")
    for x in SC:
        print(x["name"], round(x["pr"]["rev"]), round(x["e28"], 2), x["mult"], round(x["value"], 1), f"{x['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}")
    grid = [[e * m for m in SENS_PE] for e in SENS_EPS]
    print("grid", [[round(v) for v in r] for r in grid], "above", sum(v > PRICE for r in grid for v in r),
          "15%", sum(v >= PRICE * 1.15 for r in grid for v in r))
    print(f"mcap {MCAP:.2f} netdebt {NET_DEBT:.0f} EV {EV:.2f}; PE26 {PE_26:.1f} c27 {PE_C27:.1f} c28 {PE_C28:.1f} e27 {PE_E27:.1f} e28 {PE_E28:.1f}")
    print(f"off high {OFF_HIGH:.1%} ytd {YTD:.1%} oct {OCT_FALL:.1%} yoy {YOY:.1%} vsNV {VS_NV:.1%} oct22 {OCT22_MOVE:.1%} oct30 {OCT30_MOVE:.1%}")
    print(f"fcf26 {FCF26:.0f} dc share {DC_SHARE26:.1%} dc growth {DC_GROWTH26:.1%} hist fwd {HIST_FWD_PE_AVG:.1f}")
    import statistics
    print("peer median", statistics.median(p[2] for p in PEERS if p[4] == "peer"))
    print("Q_IND", Q_IND, "inv growth", INVENTORY['FY26'] / INVENTORY['FY25'] - 1)
