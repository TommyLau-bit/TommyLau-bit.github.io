"""Vertiv (NYSE: VRT) initiation, 6 Oct 2026. Single source of figures for charts, note and model.

Every figure here is taken from src/content/calls/vertiv.md (the published pitch), or from
the sources it cites, or is simple arithmetic on those figures (marked DERIVED).
"""

OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/vertiv"
PDF = f"{OUT_DIR}/2026-10-06_Vertiv_Initiation.pdf"
XLSX = f"{OUT_DIR}/2026-10-06_Vertiv_Model.xlsx"
PNG = f"{OUT_DIR}/2026-10-06_Vertiv_Initiation-p1.png"

# ---- Call ----
PRICE = 253.62          # NYSE close 5 Oct 2026
TARGET = 300.0
PEAK = 379.94           # intraday, 14 May 2026

# ---- Balance sheet, 10-Q to 30 Jun 2026 (US$m) ----
SHARES_DIL = 392.7      # m, diluted
CASH = 2810.6
ST_INV = 300.0
DEBT = 2939.8

# ---- Annual ----
SALES = {"2024A": 8.01, "2025A": 10.23}
MARGIN = {"2024A": 0.194, "2025A": 0.204}
EPS = {"2024A": 2.85, "2025A": 4.19}
GUIDE = dict(sales_lo=13.8, sales_hi=14.2, m_lo=0.233, m_hi=0.243,
             eps_lo=6.65, eps_hi=6.75, op_mid=3.325)   # US$bn, from release of 29 Jul 2026
G_EPS_MID = 6.70
G_SALES_MID = 14.0
G_M_MID = 0.238

# ---- My assumptions (base) ----
G27, G28 = 0.21, 0.20
M27, M28 = 0.25, 0.26
BASE_PE = 28
SCEN = [  # name, g27, g28, m28, multiple, prob
    ("Bear", 0.11, 0.11, 0.235, 22, 0.25),
    ("Base", G27, G28, M28, BASE_PE, 0.50),
    ("Bull", 0.23, 0.23, 0.27, 34, 0.25),
]
SENS_EPS = [9.50, 10.65, 11.50]
SENS_PE = [24, 28, 32]

CONSENSUS_27 = 8.93     # MarketBeat, 6 Oct 2026
FWD_PE_SA = 32.1        # stockanalysis.com, 6 Oct 2026

RATIO = G_EPS_MID / (GUIDE["op_mid"])  # US$ EPS per US$bn adj OP


def project(g27, g28, m28, m27=M27):
    s27 = G_SALES_MID * (1 + g27)
    s28 = s27 * (1 + g28)
    return s27, s28, s27 * m27 * RATIO, s28 * m28 * RATIO


S27, S28, E27, E28 = project(G27, G28, M28)

# ---- Quarterly ----
Q = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_SALES = [1.64, 1.95, 2.07, 2.35, 2.04, 2.64, 2.68, 2.88, 2.65, 3.27]
Q_MARGIN = [15.2, 19.6, 20.1, 21.5, 16.5, 18.5, 22.3, 23.2, 20.8, 22.6]
Q_PROD = [7.7, 15.3, 19.9, 31.5, 31.1, 38.5, 33.6, 20.4, 24.9, 19.7]
Q_SERV = [9.4, 8.5, 16.9, 12.1, 7.4, 18.6, 10.1, 14.9, 13.7, 10.1]

PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24",
             "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25",
             "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26",
             "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
PX = [56.33, 67.62, 81.67, 93.00, 98.07, 86.57, 78.70, 83.03, 99.49, 109.29, 127.60, 113.61, 117.02, 95.17,
      72.20, 85.38, 107.93, 128.41, 145.60, 127.55, 150.86, 192.86, 179.73, 162.01, 186.18, 254.89, 250.58,
      328.49, 315.71, 334.82, 241.57, 258.72, 241.31, 253.62]

PEERS = [  # company, ticker, forward P/E text, what they make (exposure)
    ("Vertiv", "NYSE: VRT", "32.1x", "Power, thermal and liquid cooling equipment and service for data centres; pure play"),
    ("Eaton", "NYSE: ETN", "~28.5 to 29x", "Electrical equipment; data centre exposure is one division among several"),
    ("nVent", "NYSE: NVT", "~28.5 to 29x", "Enclosures, electrical connections and liquid cooling"),
    ("Trane Technologies", "NYSE: TT", "~28.5 to 29x", "HVAC and chillers; data centre cooling within a wider building business"),
    ("Schneider Electric", "EPA: SU", "24x", "Electrical distribution, automation, cooling via Motivair"),
]
