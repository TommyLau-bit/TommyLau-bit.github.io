"""TSMC (NYSE: TSM ADR; TWSE: 2330) initiation, draft of 6 Oct 2026. Single source of figures for charts, note and model.

Sources: TSMC quarterly results releases and presentations furnished on Form 6-K (EDGAR CIK 1046179),
TSMC monthly revenue reports on Form 6-K, TSMC earnings call transcripts (15 Jan, 16 Apr, 16 Jul 2026),
Yahoo Finance chart API (prices, TWD rate), stockanalysis.com and MarketBeat (consensus, peers),
all retrieved 6 October 2026. Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-06"
DATE_LONG = "6 October 2026"
COMPANY = "TSMC"
SLUG = "tsmc"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/tsmc"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Claude's draft view; Tommy decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",      # e.g. "INITIATE AT LONG" once Tommy decides
    direction="NO CALL",
    target=None,                  # US$ per ADR; None for NO CALL
    conviction="Medium",
    draft=False,
)

# ---- Market data ----
PRICE = 485.80          # TSM ADR, NYSE close 5 Oct 2026 (Yahoo Finance)
PRICE_DATE = "5 October 2026"
HI52 = 487.47           # 52-week intraday high, Yahoo meta, 6 Oct 2026
LO52 = 266.82           # 52-week intraday low
PRICE_SEP25 = 279.29    # month-end close, 30 Sep 2025
TW_PRICE = 2585.0       # 2330.TW close, 6 Oct 2026 (Yahoo Finance)
FX = 31.746             # NT$ per US$, Yahoo TWD=X, 6 Oct 2026
ADR_RATIO = 5           # ordinary shares per ADR
SHARES = 25.932         # bn ordinary shares outstanding, 30 Jun 2026 (2Q26 presentation)
CASH_NT = 3518.01       # NT$bn cash and marketable securities, 30 Jun 2026
LTDEBT_NT = 864.27      # NT$bn long-term interest-bearing debts, 30 Jun 2026
DPS_2026_NT = 24.0      # NT$ cash dividend per share received in 2026 (Q2 call)

# ---- Consensus and peers (retrieved 6 Oct 2026) ----
CONS_26_ADR = 16.56     # MarketBeat, 2026 EPS per ADR, US$
CONS_27_ADR = 21.33     # MarketBeat, 2027 EPS per ADR, US$
CONS_26_NT = 107.89     # stockanalysis.com, 2026 EPS per share, NT$
FWD_PE_SA = 20.73       # stockanalysis.com forward P/E for TSM
CONS_TP = 552.26        # stockanalysis.com average ADR target, 21 analysts
PEERS = [  # company, ticker, forward P/E, what they make
    ("TSMC", "NYSE: TSM", 20.73, "Foundry: makes chips others design; CoWoS advanced packaging"),
    ("GlobalFoundries", "Nasdaq: GFS", 22.42, "Foundry, mature and specialty processes"),
    ("United Microelectronics", "NYSE: UMC", 23.97, "Foundry, mature processes; makes interposers"),
    ("Intel", "Nasdaq: INTC", 68.82, "Designs and makes its own chips; Intel Foundry for outside customers"),
    ("ASE Technology", "NYSE: ASX", 31.41, "Chip packaging and test, including advanced packaging"),
    ("Samsung Electronics", "KRX: 005930", 4.46, "Memory, including stacked HBM; Samsung Foundry"),
    ("Nvidia (customer)", "Nasdaq: NVDA", 19.75, "Designs AI accelerators; has them made at TSMC"),
]

# ---- Annual reported (TSMC 4Q25 presentation, 15 Jan 2026) ----
REV_USD = {"2024A": 90.08, "2025A": 122.42}       # US$bn
REV_NT = {"2024A": 2894.31, "2025A": 3809.05}     # NT$bn
GM = {"2024A": 0.561, "2025A": 0.599}
OM = {"2024A": 0.457, "2025A": 0.508}
EPS_NT = {"2024A": 45.25, "2025A": 66.25}
EPS_ADR = {"2024A": 7.04, "2025A": 10.65}         # sum of quarterly US$ per ADR from releases
CAPEX_NT = {"2024A": 956.01, "2025A": 1272.41}
CAPEX_USD_2025 = 40.9                              # as cited in the journal piece
CAPEX_GUIDE_26 = (60.0, 64.0)                      # raised 16 Jul 2026 from 52 to 56

# ---- Quarterly (results releases) ----
Q = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_REV_USD = [18.87, 20.82, 23.50, 26.88, 25.53, 30.07, 33.10, 33.73, 35.90, 40.20]
Q_REV_NT = [592.64, 673.51, 759.69, 868.46, 839.25, 933.79, 989.92, 1046.09, 1134.10, 1270.38]
Q_GM = [53.1, 53.2, 57.8, 59.0, 58.8, 58.6, 59.5, 62.3, 66.2, 67.7]
Q_OM = [42.0, 42.5, 47.5, 49.0, 48.5, 49.6, 50.6, 54.0, 58.1, 60.3]
Q_EPS_NT = [8.70, 9.56, 12.54, 14.45, 13.94, 15.36, 17.44, 19.50, 22.08, 27.25]
Q_EPS_ADR = [1.38, 1.48, 1.94, 2.24, 2.12, 2.47, 2.92, 3.14, 3.49, 4.31]
Q_HPC = [46, 52, 51, 53, 59, 60, 57, 55, 61, 66]     # % of revenue, platform slides
Q_ADV = [65, 67, 69, 74, 73, 74, 74, 77, 74, 77]     # 7nm and below, % of wafer revenue
# Q1 26 and Q2 26 extras (presentations)
NONOP_Q1_26 = 28.83; NONOP_Q2_26 = 95.83            # NT$bn non-operating items
WAFERS = {"Q2 25": 3718, "Q1 26": 4174, "Q2 26": 4336}   # thousand 12-inch equivalent wafers
CAPEX_Q_NT = {"Q1 26": 350.76, "Q2 26": 496.00}
# Q3 2026 guide (16 Jul 2026)
G3_REV = (44.6, 45.8); G3_GM = (0.65, 0.67); G3_OM = (0.56, 0.58); G3_FX = 32.0

# ---- Monthly revenue, NT$bn (monthly revenue reports on Form 6-K) ----
M_LABELS = ["Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
            "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26"]
M_REV = [293.29, 260.01, 285.96, 349.57, 320.52, 263.71, 323.17, 335.77, 330.98, 367.47,
         343.61, 335.00, 401.26, 317.66, 415.19, 410.73, 416.98, 442.68, 467.58, 514.81]

# ---- Share price, month-end close (Yahoo Finance, retrieved 6 Oct 2026) ----
PX_LABELS = ["Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24",
             "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25",
             "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26",
             "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
PX = [97.31, 104.00, 112.96, 128.67, 136.05, 137.34, 151.04, 173.81, 165.80, 171.70, 173.67, 190.54, 184.66,
      197.49, 209.32, 180.53, 166.00, 166.69, 193.32, 226.49, 241.62, 230.87, 279.29, 300.43, 291.51, 303.89,
      330.56, 374.58, 337.95, 396.06, 418.45, 477.57, 404.25, 415.32, 456.19, 485.80]

# ---- MY assumptions ----
NONOP = 0.025           # non-operating income as share of revenue (Q1 26: 2.5%)
TAX = 0.17              # tax and minorities as share of pre-tax profit (2025: 15.9%; 1H26: 17.5%)
Q3E_REV, Q3E_OM = 46.4, 0.57     # above the guide top, on July and August monthly revenue
Q4E_REV, Q4E_OM = 49.0, 0.56
G27, G28 = 0.24, 0.18
OM27, OM28 = 0.57, 0.555
BASE_PE = 20
SCEN = [  # name, g27, g28, om27, om28, multiple, prob
    ("Bear", 0.15, 0.05, 0.55, 0.50, 16, 0.25),
    ("Base", G27, G28, OM27, OM28, BASE_PE, 0.50),
    ("Bull", 0.30, 0.25, 0.59, 0.59, 24, 0.25),
]
SENS_EPS = [20.00, None, 26.00]   # middle row = model 2028E
SENS_PE = [16, 20, 24]

K = ADR_RATIO / SHARES  # ADRs per US$bn of net income -> US$ per ADR


def adr_eps(rev, om):
    """US$ EPS per ADR from US$bn revenue and operating margin."""
    return rev * (om + NONOP) * (1 - TAX) * K


H1_EPS = Q_EPS_ADR[8] + Q_EPS_ADR[9]
Q3E_EPS = adr_eps(Q3E_REV, Q3E_OM)
Q4E_EPS = adr_eps(Q4E_REV, Q4E_OM)
REV26 = Q_REV_USD[8] + Q_REV_USD[9] + Q3E_REV + Q4E_REV
OP26 = Q_REV_USD[8] * Q_OM[8] / 100 + Q_REV_USD[9] * Q_OM[9] / 100 + Q3E_REV * Q3E_OM + Q4E_REV * Q4E_OM
OM26 = OP26 / REV26
EPS26 = H1_EPS + Q3E_EPS + Q4E_EPS


def project(g27, g28, om27, om28):
    r27 = REV26 * (1 + g27)
    r28 = r27 * (1 + g28)
    return r27, r28, adr_eps(r27, om27), adr_eps(r28, om28)


R27, R28, EPS27, EPS28 = project(G27, G28, OM27, OM28)
VALS = [mult * project(g1, g2, o1, o2)[3] for _, g1, g2, o1, o2, mult, _ in SCEN]
WEIGHTED = sum(v * s[6] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
SENS_EPS[1] = round(EPS28, 2)

# Market cap and ADR premium (derived)
MCAP_ADR = SHARES * PRICE / ADR_RATIO            # US$bn at the ADR price
MCAP_TW = SHARES * TW_PRICE / FX                 # US$bn at the Taiwan price
NETCASH = (CASH_NT - LTDEBT_NT) / FX             # US$bn, approximate
ADR_PREMIUM = (PRICE / ADR_RATIO * FX) / TW_PRICE - 1

# What the price needs at the base multiple
NEED_EPS28 = PRICE / BASE_PE
NEED_OM28 = NEED_EPS28 / (R28 * (1 - TAX) * K) - NONOP
NEED_REV28 = NEED_EPS28 / ((OM28 + NONOP) * (1 - TAX) * K)

if __name__ == "__main__":
    print(f"2026E rev {REV26:.2f} OM {OM26:.4f} EPS {EPS26:.2f} (H1 {H1_EPS:.2f}, Q3E {Q3E_EPS:.2f}, Q4E {Q4E_EPS:.2f})")
    print(f"2027E rev {R27:.2f} EPS {EPS27:.2f}; 2028E rev {R28:.2f} EPS {EPS28:.2f}")
    print("PE 26/27/28", PRICE / EPS26, PRICE / EPS27, PRICE / EPS28, "cons27", PRICE / CONS_27_ADR)
    for s, v in zip(SCEN, VALS):
        print(s[0], round(project(*s[1:5])[3], 2), round(v, 1), f"{v / PRICE - 1:+.1%}")
    print("weighted", round(WEIGHTED, 1), f"{WEIGHTED / PRICE - 1:+.1%}")
    print("grid", [[round(e * m) for m in SENS_PE] for e in SENS_EPS])
    print(f"mcap ADR {MCAP_ADR:.0f} TW {MCAP_TW:.0f} netcash {NETCASH:.1f} premium {ADR_PREMIUM:.1%}")
    print(f"need EPS28 {NEED_EPS28:.2f} OM28 {NEED_OM28:.3f} rev28 {NEED_REV28:.1f}")
    print("EPS27 vs cons", EPS27 / CONS_27_ADR - 1, "2024-29 25% CAGR 2029:", 90.08 * 1.25 ** 5)
    jul_aug = M_REV[-2] + M_REV[-1]
    print("Q3 NT$ guide", G3_REV[0] * G3_FX, G3_REV[1] * G3_FX, "Sep needed", G3_REV[0] * G3_FX - jul_aug, G3_REV[1] * G3_FX - jul_aug)
    print("rev/wafer y/y", (1270.38 / 4336) / (933.79 / 3718) - 1, "wafers y/y", 4336 / 3718 - 1)
