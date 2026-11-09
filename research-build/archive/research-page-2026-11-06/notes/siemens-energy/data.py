"""Siemens Energy AG (Xetra: ENR) initiation, drafted 28 Oct 2026. Single source of figures for charts, note and model.

Fiscal year ends 30 September: FY2026 = year to Sep 2026 (results due 11 Nov 2026); FY2027 = year to Sep 2027.
Euro million unless stated (segment tables), euro billion where marked.
Sources (siemens-energy.com investor relations):
- Earnings Release Q3 FY2026, 5 Aug 2026: segment orders, revenue, profit before special items (SI), Q3 and 9M;
  balance sheet at 30 Jun 2026; adjusted net cash; FY2026 outlook; external revenue split.
- Earnings Releases Q1 FY2026 (11 Feb 2026) and Q2 FY2026 (12 May 2026): quarterly Grid figures and the
  prior-year quarters; Q2 raised the FY2026 outlook.
- Shareholder Letter Q4 FY2025, 14 Nov 2025: FY2025 segment results, FY2028 group targets, buyback and capital allocation.
- Shareholder Letter Q4 FY2024, 13 Nov 2024: FY2024 Grid orders and revenue; Grid backlog EUR33bn.
- Capital Market Day, 20 Nov 2025: CEO, CFO, Grid Technologies, Gas Services, Siemens Gamesa and Transformation of
  Industry presentations (FY2028 targets; Grid FY22 to FY25 history; the transformer market chart).
- Half-year Financial Report 2026, 12 May 2026: treasury shares (Note 4), issued shares.
- Share buyback page (siemens-energy.com/sharebuyback), read 28 Oct 2026: shares bought by tranche and month.
- Q4 FY2026 Pre-Close Call transcript, 30 Sep 2026; IR financial calendar (Q4 FY2026 results 11 Nov 2026).
Prices: Yahoo Finance ENR.DE chart API (read in a browser; curl was refused with "Too Many Requests"), 28 Oct 2026.
Consensus and peer multiples: stockanalysis.com (S&P Global data), retrieved 28 Oct 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-28"
COMPANY = "SiemensEnergy"
SLUG = "siemens-energy"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/siemens-energy"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call (Tommy Lau, 28 Oct 2026). Rebuild = edit this dict only. ----
CALL = dict(
    banner="LONG",
    direction="LONG",
    target=160.0,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Yahoo Finance ENR.DE, retrieved 28 Oct 2026) ----
PRICE = 128.58              # Xetra close, 27 Oct 2026
PRICE_DATE = "27 October 2026"
HI_CLOSE = 187.62           # record close, 24 Apr 2026
HI_INTRA = 191.66           # record intraday high, 24 Apr 2026
LO_CLOSE_52 = 100.80        # lowest close in 52 weeks, 21 Nov 2025
LO_CLOSE_26 = 118.68        # lowest close of 2026, 23 Oct 2026
PX_DEC25 = 120.40           # close, 30 Dec 2025 (last trading day of 2025)
EVENTS = [  # date, what, close before, close on the day (releases come out before the market opens)
    ("14 Nov 2025", "FY2025 results; FY2028 targets raised", 101.05, 110.50),
    ("11 Feb 2026", "Q1 FY2026 results", 150.60, 163.25),
    ("12 May 2026", "Q2 FY2026 results; FY2026 outlook raised", 178.50, 169.48),
    ("5 Aug 2026", "Q3 FY2026 results", 150.86, 150.86),
    ("22 Oct 2026", "Barclays study on AI equipment pricing power, reported", 133.64, 122.20),
]

# ---- Shares (millions) ----
ISSUED = 861.104914          # issued shares, 31 Mar 2026 and per voting rights notices to Sep 2026
TREAS_SEP25 = 5.761          # treasury shares, 30 Sep 2025 (Half-year Financial Report, Note 4)
EMP_H1 = 4.644               # treasury shares issued to employee plans, H1 FY2026 (Note 4); H2 not yet disclosed
BB_T1 = 12.618469            # first tranche, Mar to May 2026, EUR2.0bn at EUR158.50
BB_T2 = 6.467098             # second tranche, Jun to Aug 2026, EUR1.0bn at EUR154.63
BB_T3 = 4.513232             # third tranche from 24 Sep 2026, to 27 Oct read on 28 Oct 2026, EUR623m at EUR138.04
BB_CASH_AFTER_JUN = 0.4598 + 0.1806 + 0.1170 + 0.5060   # EUR bn bought July to October (buyback page), after the 30 Jun balance sheet
TREAS_NOW = TREAS_SEP25 + BB_T1 + BB_T2 + BB_T3 - EMP_H1
SHARES = ISSUED - TREAS_NOW  # MY derivation; cancellation of treasury shares does not change shares outstanding

# ---- Balance sheet, 30 Jun 2026 (EUR bn, Q3 FY2026 release) ----
CASH = 11.088
DEBT = 0.407 + 2.552
PENSION = 0.410
ADJ_NET_CASH = 7.719         # Siemens Energy's own "adjusted net cash" = cash less debt less pensions
EQUITY_METHOD = 1.853        # investments accounted for using the equity method, at book
NCI_BOOK = 0.473
NCI_NI = 0.30                # non-controlling interests' share of net income, FY2026 guidance (~EUR0.3bn)
NCI_MULT = 15                # MY ASSUMPTION: minorities valued at 15x their earnings, not at book
CONTRACT_LIAB = 28.071       # customer advances and other contract liabilities

# ---- Segments: history (EUR m) ----
SEGS = ["GS", "GT", "TI", "SG"]
SEG_NAMES = {"GS": "Gas Services", "GT": "Grid Technologies", "TI": "Transformation of Industry", "SG": "Siemens Gamesa"}
REV25 = {"GS": 12198, "GT": 11305, "TI": 5723, "SG": 10375}
M25 = {"GS": 0.130, "GT": 0.158, "TI": 0.113, "SG": -0.131}
REV9M = {"GS": 10331, "GT": 9744, "TI": 4251, "SG": 7624}
P9M = {"GS": 1715, "GT": 1784, "TI": 543, "SG": -15}
REV_Q4_25 = {"GS": 3094, "GT": 3145, "TI": 1614, "SG": 2744}
GROUP_REV25, GROUP_PBSI25 = 39100, 2355        # FY2025 revenue EUR39.1bn, profit before SI EUR2,355m
GROUP_REV9M, GROUP_PBSI9M = 31416, 3946
RECON9M = -82
NI9M, NI_NCI9M = 2769, 243

# FY2026 outlook (raised May 2026, confirmed Aug and 30 Sep 2026); comparable revenue growth, margin before SI
GUIDE26 = {"Group": ("14 to 16%", "10 to 12%"), "GS": ("16 to 18%", "14 to 16%"), "GT": ("25 to 27%", "18 to 20%"),
           "TI": ("5 to 7%", "11 to 13%"), "SG": ("3 to 5%", "break-even")}
GUIDE26_NI, GUIDE26_FCF = 4.0, 8.0
# FY2028 targets (Capital Market Day, 20 Nov 2025): revenue CAGR FY25 to FY28, margin before SI
TGT28 = {"Group": ("low teens", "14 to 16%"), "GS": ("mid-teens", "18 to 20%"), "GT": ("high teens", "18 to 20%"),
         "TI": ("mid to high single digit", "12 to 14%"), "SG": ("mid single digit", "3 to 5%")}

# Grid Technologies history
GT_YEARS = ["FY22", "FY23", "FY24", "FY25"]
GT_REV_HIST = [6.3, 7.2, 9.28, 11.305]           # EUR bn (CMD Grid deck p12; FY24 and FY25 from the shareholder letters)
GT_M_HIST = [0.036, 0.076, 0.105, 0.158]
GT_ORD = {"FY24": 20901, "FY25": 21423}
GT_Q_LABELS = ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26"]
GT_Q_ORD = [5117, 5209, 4218, 6880, 5964, 6996, 5367]
GT_Q_REV = [2480, 2861, 2819, 3145, 3054, 3067, 3624]
GT_BL_LABELS = ["Sep 24", "Sep 25", "Dec 25", "Mar 26", "Jun 26"]
GT_BL = [33, 42, 45, 49, 51]                     # EUR bn, rounded as reported
GT_Q3_M = 0.199
GT_9M_ORD = sum(GT_Q_ORD[4:])
GT_9M_BTB = GT_9M_ORD / REV9M["GT"]
GROUP_BL_JUN26 = 162

# ---- MY estimates: Q4 FY2026 (results due 11 Nov 2026) ----
Q4_REV = {"GS": 3600, "GT": 4100, "TI": 1700, "SG": 2700}
Q4_M = {"GS": 0.150, "GT": 0.200, "TI": 0.130, "SG": 0.000}
RECON26 = -300               # FY2026 reconciliation line, about minus EUR0.3bn (Q3 presentation)
ELIM_REV26 = -700            # revenue eliminations, about the 9M pace (MINE)
REV26 = {k: REV9M[k] + Q4_REV[k] for k in SEGS}
P26 = {k: P9M[k] + Q4_REV[k] * Q4_M[k] for k in SEGS}
M26 = {k: P26[k] / REV26[k] for k in SEGS}
GROUP_REV26 = sum(REV26.values()) + ELIM_REV26
GROUP_PBSI26 = sum(P26.values()) + RECON26

# ---- MY estimates: FY2027 (year to September 2027) ----
G27 = {"GS": 0.17, "GT": 0.18, "TI": 0.06, "SG": 0.04}
M27 = {"GS": 0.18, "GT": 0.20, "TI": 0.13, "SG": 0.02}
RECON27 = -300
ELIM_REV27 = -700
SG_BURN = 1.5                # EUR bn, MY estimate of Siemens Gamesa cash still to burn before it turns cash positive (FY2027 to FY2028)
MULT = {"GS": 18, "GT": 22, "TI": 14, "SG": 10, "Corp": 15}

# Net income bridge for an EPS cross-check (MINE)
SI27 = -200; PPA27 = -200; FIN27 = 200; TAX27 = 0.22; NCI27 = 300

# ---- Consensus and peers (stockanalysis.com, S&P Global data, retrieved 28 Oct 2026) ----
CONS_EPS26, CONS_EPS27 = 4.52, 6.25
CONS_REV26, CONS_REV27 = 44.20, 50.70
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 192.55, 28, 100.0, 260.0
FWD_PE_SA = 22.09
PEERS = [  # company, ticker, forward P/E, trailing EV/EBIT, what they make, group
    ("Siemens Energy", "Xetra: ENR", 22.09, 26.78, "Gas turbines and service, grid equipment, wind turbines, industrial compressors", "self"),
    ("ABB", "SWX: ABBN", 22.15, 24.13, "Electrification and automation equipment", "grid"),
    ("Schneider Electric", "EPA: SU", 20.02, 20.33, "Electrical distribution, automation, data centre power", "grid"),
    ("Eaton", "NYSE: ETN", 25.36, 31.14, "Switchgear and power distribution, data centre electrical", "grid"),
    ("Prysmian", "BIT: PRY", 19.44, 20.76, "High voltage and power cable", "grid"),
    ("Hitachi", "TSE: 6501", 24.04, 18.57, "Grid equipment (Hitachi Energy), IT services, rail, industrial products", "grid"),
    ("GE Vernova", "NYSE: GEV", 42.61, 84.18, "Gas turbines, grid equipment, wind turbines", "gas"),
    ("Mitsubishi Heavy", "TSE: 7011", 28.67, 21.48, "Gas turbines, defence, aerospace, industrial machinery", "gas"),
    ("Baker Hughes", "NASDAQ: BKR", 20.93, 20.91, "Compressors, turbomachinery, oilfield services", "gas"),
    ("Vestas", "CPH: VWS", 17.31, 15.46, "Wind turbines and service", "wind"),
]

# ---- Scenarios: name, GT (g, m, x), GS (g, m, x), TI x, SG (m, x, burn), prob ----
SCEN = [
    ("Bear", (0.12, 0.185, 16), (0.10, 0.16, 13), 10, (0.00, 10, 3.0), 0.25),
    ("Base", (G27["GT"], M27["GT"], MULT["GT"]), (G27["GS"], M27["GS"], MULT["GS"]), MULT["TI"], (M27["SG"], MULT["SG"], SG_BURN), 0.50),
    ("Bull", (0.22, 0.21, 27), (0.20, 0.19, 22), 16, (0.04, 12, 1.0), 0.25),
]
SENS_GS_X = [13, 18, 23]     # rows: Gas Services multiple
SENS_GT_X = [16, 22, 28]     # columns: Grid Technologies multiple

# ---- Derived ----
REV27 = {k: REV26[k] * (1 + G27[k]) for k in SEGS}
P27 = {k: REV27[k] * M27[k] for k in SEGS}
GROUP_REV27 = sum(REV27.values()) + ELIM_REV27
GROUP_PBSI27 = sum(P27.values()) + RECON27
NI27 = (GROUP_PBSI27 + SI27 + PPA27 + FIN27) * (1 - TAX27) - NCI27
EPS27 = NI27 / SHARES
MCAP = PRICE * SHARES / 1000                       # EUR bn
NET_CASH_NOW = ADJ_NET_CASH - BB_CASH_AFTER_JUN     # 30 Jun adjusted net cash less buybacks paid since
NCI_VALUE = NCI_NI * NCI_MULT
BRIDGE = NET_CASH_NOW + EQUITY_METHOD - NCI_VALUE   # EUR bn
EV_ADJ = MCAP - BRIDGE


def seg_values(gt=None, gs=None, ti_x=None, sg=None):
    """EUR bn value of each part on FY2027E profit before SI."""
    gt = gt or SCEN[1][1]; gs = gs or SCEN[1][2]; ti_x = ti_x or SCEN[1][3]; sg = sg or SCEN[1][4]
    p_gt = REV26["GT"] * (1 + gt[0]) * gt[1] / 1000
    p_gs = REV26["GS"] * (1 + gs[0]) * gs[1] / 1000
    p_ti = P27["TI"] / 1000
    p_sg = REV27["SG"] * sg[0] / 1000
    return dict(GT=p_gt * gt[2], GS=p_gs * gs[2], TI=p_ti * ti_x, SG=p_sg * sg[1] - sg[2], Corp=RECON27 / 1000 * MULT["Corp"]), \
        dict(GT=p_gt, GS=p_gs, TI=p_ti, SG=p_sg)


def per_share(vals):
    return (sum(vals.values()) + BRIDGE) / SHARES * 1000


SOTP, PROF = seg_values()
SOTP_EV = sum(SOTP.values())
EQUITY = SOTP_EV + BRIDGE
BASE_VALUE = per_share(SOTP)
VALS, PGT = [], []
for s in SCEN:
    v, p = seg_values(s[1], s[2], s[3], s[4])
    VALS.append(per_share(v)); PGT.append(p["GT"])
WEIGHTED = sum(v * s[5] for v, s in zip(VALS, SCEN))
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75
REST_EV = SOTP_EV - SOTP["GT"]
GT_IMPLIED_EV = EV_ADJ - REST_EV
GT_IMPLIED_X = GT_IMPLIED_EV / PROF["GT"]
GS_IMPLIED_X = (EV_ADJ - (SOTP_EV - SOTP["GS"])) / PROF["GS"]
GT_SHARE_EQ = SOTP["GT"] / EQUITY
GS_SHARE_EQ = SOTP["GS"] / EQUITY
EV_PBSI26 = EV_ADJ / (GROUP_PBSI26 / 1000)
EV_PBSI27 = EV_ADJ / (GROUP_PBSI27 / 1000)
PE_C26 = PRICE / CONS_EPS26
PE_C27 = PRICE / CONS_EPS27
PE_M27 = PRICE / EPS27
OFF_HIGH = PRICE / HI_CLOSE - 1
RISE_DEC25 = PRICE / PX_DEC25 - 1
GT_GROWTH26 = REV26["GT"] / REV25["GT"] - 1
GT_BTB_FY24 = GT_ORD["FY24"] / (GT_REV_HIST[2] * 1000)
GT_BTB_FY25 = GT_ORD["FY25"] / REV25["GT"]
GT_TTM_JUN26 = sum(GT_Q_REV[3:])
GT_BL_RATIO_JUN26 = GT_BL[-1] * 1000 / GT_TTM_JUN26
GT_BL_GROWTH = GT_BL[-1] / GT_BL[0] - 1


def grid_value(gs_x, gt_x):
    v = dict(SOTP); v["GS"] = PROF["GS"] * gs_x; v["GT"] = PROF["GT"] * gt_x
    return per_share(v)


SENS = [[grid_value(a, b) for b in SENS_GT_X] for a in SENS_GS_X]

# ---- Price, month-end close (Yahoo Finance ENR.DE, retrieved 28 Oct 2026) ----
PX_LABELS = ["Oct 23", "Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24",
             "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25",
             "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26",
             "Jul 26", "Aug 26", "Sep 26", "27 Oct 26"]
PX = [8.37, 10.88, 12.00, 13.97, 14.20, 17.00, 19.30, 24.82, 24.31, 26.91, 26.05, 33.07, 37.53, 51.02, 50.38, 57.84, 54.94,
      53.84, 67.54, 85.50, 98.06, 102.00, 90.72, 99.42, 107.30, 115.30, 120.40, 144.55, 166.45, 142.25, 180.58, 163.24,
      165.80, 147.44, 142.18, 142.60, 128.58]

# ---- The draft call's tests ----
WRONG_IF = ("Grid Technologies' profit margin before special items for fiscal 2027 lands below 18 per cent, or its orders "
            "fall below its revenue in fiscal 2027, or Siemens Gamesa's free cash flow pre tax for fiscal 2027 is worse than "
            "minus €2 billion, or the shares close below €105 at any month end before October 2027.")

if __name__ == "__main__":
    print(f"treasury {TREAS_NOW:.3f}m shares {SHARES:.3f}m mcap {MCAP:.2f}bn netcash now {NET_CASH_NOW:.3f} bridge {BRIDGE:.3f} EVadj {EV_ADJ:.2f}")
    for k in SEGS:
        print(f"{k}: rev26 {REV26[k]:.0f} p26 {P26[k]:.0f} m26 {M26[k]:.1%} | rev27 {REV27[k]:.0f} p27 {P27[k]:.0f}")
    print(f"group rev26 {GROUP_REV26:.0f} pbsi26 {GROUP_PBSI26:.0f} ({GROUP_PBSI26 / GROUP_REV26:.1%}); rev27 {GROUP_REV27:.0f} pbsi27 {GROUP_PBSI27:.0f} ({GROUP_PBSI27 / GROUP_REV27:.1%})")
    print(f"NI27 {NI27:.0f} EPS27 {EPS27:.2f} vs cons {CONS_EPS27}")
    print("SOTP", {k: round(v, 2) for k, v in SOTP.items()}, "EV", round(SOTP_EV, 2), "equity", round(EQUITY, 2))
    print(f"base {BASE_VALUE:.2f} {BASE_VALUE / PRICE - 1:+.1%}")
    for s, v in zip(SCEN, VALS):
        print(s[0], round(v, 1), f"{v / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.1f} short {REVISIT_SHORT:.1f}")
    print("grid", [[round(x, 1) for x in r] for r in SENS], sum(x > PRICE for r in SENS for x in r), sum(x >= PRICE * 1.15 for r in SENS for x in r))
    print(f"GT implied EV {GT_IMPLIED_EV:.1f} = {GT_IMPLIED_X:.1f}x; GS implied {GS_IMPLIED_X:.1f}x; GT share {GT_SHARE_EQ:.1%} GS share {GS_SHARE_EQ:.1%}")
    print(f"EV/PBSI 26 {EV_PBSI26:.1f} 27 {EV_PBSI27:.1f}; PE cons26 {PE_C26:.1f} cons27 {PE_C27:.1f} mine27 {PE_M27:.1f}")
    print(f"off high {OFF_HIGH:.1%} vs dec25 {RISE_DEC25:+.1%}; GT growth26 {GT_GROWTH26:.1%}; btb24 {GT_BTB_FY24:.2f} btb25 {GT_BTB_FY25:.2f} 9M {GT_9M_BTB:.2f}")
    print(f"GT ttm {GT_TTM_JUN26} BL ratio {GT_BL_RATIO_JUN26:.2f}; BL growth {GT_BL_GROWTH:.1%}")
    for d, w, a, b in EVENTS:
        print(d, f"{b / a - 1:+.1%}")
    import statistics
    for g in ["grid", "gas"]:
        ps = [p for p in PEERS if p[5] == g]
        print(g, "median fwd PE", statistics.median(p[2] for p in ps), "EV/EBIT", statistics.median(p[3] for p in ps))
