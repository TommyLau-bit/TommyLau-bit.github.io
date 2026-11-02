"""Wärtsilä Oyj Abp (Nasdaq Helsinki: WRT1V) initiation, drafted 2 Nov 2026. Single source of figures for charts, note and model.

Calendar year. EUR million unless stated. Continuing operations: Energy Storage is a discontinued operation since June 2026
(50/50 joint venture Valo with RCT Solutions from 1 October 2026), and Portfolio Business was fully divested by 1 June 2026.
Sources (wartsila.com investors; full reports are the PDFs attached to each stock exchange release):
- Interim Report January-September 2026, 27 Oct 2026: segment tables (Marine, Energy, Portfolio Business), Energy MW
  ordered, order books, order book for 2026 deliveries, balance sheet, shares, risks, outlook, CEO statement.
- Result presentation Q3 2026, 27 Oct 2026: Energy equipment orders by region (p32), Capital Markets Day date.
- Inside information, 27 Oct 2026: new mid-term financial targets and new guidance practice from 2027.
- Half-year Financial Report January-June 2026, 21 Jul 2026: "1.2 GW of firm data centre-related orders across two
  projects"; STH expansion to about 2.2 times the 2025 output by Q1 2029; Energy Q2 figures.
- Interim Report January-March 2026, 28 Apr 2026: 429 MW data centre order (24 x 50SG); 35% STH expansion by Q1 2028.
- Financial Statements Bulletin January-December 2025, 4 Feb 2026: 2025 and 2024 segment figures; "first two projects in
  the US, which together included delivering 789 MWs"; Energy MW 2025 and 2024.
- Stock exchange release, 5 Oct 2026: 2027 financial calendar (FY2026 bulletin 5 February 2027).
Prices: Nasdaq Nordic official price history (api.nasdaq.com, orderbook TX50138), retrieved 2 Nov 2026. The Yahoo chart
API returned "Too Many Requests" and was not retried. Cross-checked against stockanalysis.com daily history.
Consensus and peer multiples: stockanalysis.com (S&P Global data), retrieved 2 Nov 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "Wartsila"
SLUG = "wartsila"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/wartsila"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Published 2 Nov 2026 on Tommy's instruction to follow the band view. ----
CALL = dict(
    banner="LONG",
    direction="LONG",
    target=30.0,
    conviction="Low",
    draft=False,
)

# ---- Market data (Nasdaq Nordic, WRT1V, retrieved 2 Nov 2026) ----
PRICE = 25.64               # Nasdaq Helsinki close, 30 Oct 2026 (last full session before drafting)
PRICE_DATE = "30 October 2026"
HI_CLOSE = 39.63            # record close in the data, 23 Apr 2026
HI_INTRA = 40.75            # intraday high, 23 Apr 2026
LO_CLOSE_52 = 25.62         # lowest close in 52 weeks, 18 Nov 2025
LO_INTRA_52 = 25.27         # lowest intraday in 52 weeks, 30 Oct 2026
PX_DEC25 = 30.40            # close, 30 Dec 2025 (last trading day of 2025)
PX_OCT23 = 11.24            # month-end close, October 2023
EVENTS = [  # date, what, close before, close on the day (reports come out before the market opens)
    ("4 Feb 2026", "FY2025 results", 35.21, 33.00),
    ("28 Apr 2026", "Q1 results; record Energy orders", 38.21, 35.91),
    ("21 Jul 2026", "Q2 results; record group orders", 30.56, 29.99),
    ("27 Oct 2026", "Q3 results and new mid-term targets", 28.76, 26.36),
]

# ---- Shares (millions) and balance sheet, 30 Sep 2026 (Q3 interim report) ----
SHARES = 589.801254         # shares outstanding, 30 Sep 2026 (treasury 1,922,136 excluded)
CASH = 2469                 # cash, continuing operations (a further 246 sat in assets held for sale and went with Valo)
DEBT = 188 + 256 + 41 + 63  # lease liabilities and other interest-bearing debt, non-current and current
NCI_BOOK = 8
NET_CASH = CASH - DEBT      # continuing operations; Wärtsilä's own figure, -2,165 net debt, includes the 246 held for sale
VALO = 0                    # MY ASSUMPTION: 50% of the loss-making Valo joint venture valued at nil
ADVANCES = 2014             # advances received, 30 Sep 2026 (1,347 at end of 2025)
NIBD_REPORTED = -2165
BRIDGE = (NET_CASH + VALO - NCI_BOOK) / 1000   # EUR bn

# ---- Segments: history ----
SEGS = ["MA", "EN"]
SEG_NAMES = {"MA": "Marine", "EN": "Energy"}
REV24 = {"MA": 3053, "EN": 1897}
P24 = {"MA": 360, "EN": 269}
REV25 = {"MA": 3494, "EN": 2048}
P25 = {"MA": 443, "EN": 315}
ORD25 = {"MA": 3926, "EN": 2940}
REV9M = {"MA": 2615, "EN": 1624}
P9M = {"MA": 341, "EN": 259}
ORD9M = {"MA": 3124, "EN": 4055}
BOOK_SEP26 = {"MA": 4304, "EN": 5571}
BOOK_SEP25 = {"MA": 3660, "EN": 2977}
BOOK_2026DEL = {"MA": 949, "EN": 692}       # order book for 2026 deliveries at 30 Sep 2026
EN_EQ_ORD9M, EN_EQ_REV9M = 2998, 770        # Energy equipment orders and sales, 9M 2026
EN_EQ_ORD9M_25, EN_EQ_AMERICAS9M = 1258, 2619
PB_REV9M, PB_P9M = 259, 23                  # Portfolio Business, 9M 2026 (nothing after 1 June 2026)
GROUP_REV25, GROUP_P25 = 6219, 805          # continuing operations, restated
GROUP_REV9M, GROUP_P9M = 4497, 623
GROUP_ORD9M, GROUP_BOOK = 7302, 9876
EPS9M_CONT = 0.78

# Energy by quarter (orders, net sales, comparable operating result, MW ordered, order book)
EN_Q_LABELS = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
EN_Q_ORD = [625, 913, 644, 758, 973, 1661, 1421]
EN_Q_REV = [415, 529, 382, 723, 465, 580, 579]
EN_Q_P = [63, 76, 61, 115, 68, 90, 101]
EN_Q_MW = [475, 760, 569, 520, 1070, 1934, 1147]
EN_Q_BOOK = [2454, 2729, 2977, 3009, 3584, 4715, 5571]
EN_MW_24, EN_MW_25 = 1376, 2324
EN_MW_9M26 = 4150
# Data centre MW named in Wärtsilä's reports
DC_MW_25 = 789                               # "first two projects in the US", 2025 (not split by quarter)
DC_MW_Q = {"Q1 26": 429, "Q2 26": 1200, "Q3 26": 282}   # 24 x 50SG; "1.2 GW ... across two projects"; 15 x 50SG
DC_MW_9M26 = sum(DC_MW_Q.values())

# Mid-term targets (inside information, 27 Oct 2026), organic growth and operating margin
TGT = {"MA": ("mid-single-digit", 0.14), "EN": ("high-teens", 0.18), "Group": ("low-double-digit", 0.16)}

# ---- MY estimates: Q4 2026 and 2026 ----
Q4_REV = {"MA": 960, "EN": 760}
Q4_M = {"MA": 0.130, "EN": 0.170}
REV26 = {k: REV9M[k] + Q4_REV[k] for k in SEGS}
P26 = {k: P9M[k] + Q4_REV[k] * Q4_M[k] for k in SEGS}
M26 = {k: P26[k] / REV26[k] for k in SEGS}
GROUP_REV26 = sum(REV26.values()) + PB_REV9M
GROUP_P26 = sum(P26.values()) + PB_P9M

# ---- MY estimates: 2027 (current accounting; IFRS 18 from 2027 moves joint venture results out of operating result) ----
G27 = {"MA": 0.05, "EN": 0.22}
M27 = {"MA": 0.130, "EN": 0.175}
MULT = {"MA": 14, "EN": 18}
FIN27, TAX27, NCI27 = -5, 0.24, 4

# ---- Consensus and peers (stockanalysis.com, S&P Global data, retrieved 2 Nov 2026) ----
CONS_EPS26, CONS_EPS27 = 1.11, 1.31
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 32.18, 17, 19.50, 40.00
PEERS = [  # company, ticker, forward P/E, trailing EV/EBIT, what they make, group
    ("Wärtsilä", "HEL: WRT1V", 19.91, 15.52, "Marine engines and service, engine power plants and service", "self"),
    ("Caterpillar", "NYSE: CAT", 20.77, 21.80, "Gas engines and turbines (Solar), construction and mining machines", "engine"),
    ("Cummins", "NYSE: CMI", 15.22, 18.71, "Engines and generator sets, power systems", "engine"),
    ("Rolls-Royce", "LSE: RR", 26.23, 20.65, "Aero engines; mtu engines and generator sets", "engine"),
    ("Siemens Energy", "Xetra: ENR", 21.81, 26.41, "Gas turbines and service, grid equipment, wind turbines", "power"),
    ("GE Vernova", "NYSE: GEV", 37.17, 58.92, "Gas turbines, grid equipment, wind turbines", "power"),
    ("Alfa Laval", "STO: ALFA", 22.75, 20.14, "Heat exchangers, separators, marine equipment", "marine"),
]

# ---- Scenarios: name, Marine (g, m, x), Energy (g, m, x), prob ----
SCEN = [
    ("Bear", (0.00, 0.120, 11), (0.08, 0.155, 12), 0.25),
    ("Base", (G27["MA"], M27["MA"], MULT["MA"]), (G27["EN"], M27["EN"], MULT["EN"]), 0.50),
    ("Bull", (0.07, 0.135, 16), (0.30, 0.185, 22), 0.25),
]
SENS_MA_X = [11, 14, 17]     # rows: Marine multiple
SENS_EN_X = [13, 18, 23]     # columns: Energy multiple

# ---- Derived ----
REV27 = {k: REV26[k] * (1 + G27[k]) for k in SEGS}
P27 = {k: REV27[k] * M27[k] for k in SEGS}
GROUP_REV27 = sum(REV27.values())
GROUP_P27 = sum(P27.values())
NI27 = (GROUP_P27 + FIN27) * (1 - TAX27) - NCI27
EPS27 = NI27 / SHARES
MCAP = PRICE * SHARES / 1000                     # EUR bn
EV = MCAP - BRIDGE


def values(ma=None, en=None):
    ma = ma or SCEN[1][1]; en = en or SCEN[1][2]
    p_ma = REV26["MA"] * (1 + ma[0]) * ma[1] / 1000
    p_en = REV26["EN"] * (1 + en[0]) * en[1] / 1000
    return dict(MA=p_ma * ma[2], EN=p_en * en[2]), dict(MA=p_ma, EN=p_en)


def per_share(vals):
    return (sum(vals.values()) + BRIDGE) / SHARES * 1000


SOTP, PROF = values()
SOTP_EV = sum(SOTP.values())
EQUITY = SOTP_EV + BRIDGE
BASE_VALUE = per_share(SOTP)
VALS, PEN = [], []
for s in SCEN:
    v, p = values(s[1], s[2])
    VALS.append(per_share(v)); PEN.append(p["EN"])
WEIGHTED = sum(v * s[3] for v, s in zip(VALS, SCEN))
REVISIT_LONG = BASE_VALUE / 1.15
EN_IMPLIED_X = (EV - SOTP["MA"]) / PROF["EN"]
MA_IMPLIED_X = (EV - SOTP["EN"]) / PROF["MA"]
EN_SHARE_EQ = SOTP["EN"] / EQUITY
MA_SHARE_EQ = SOTP["MA"] / EQUITY
EV_P26 = EV / (GROUP_P26 / 1000)
EV_P27 = EV / (GROUP_P27 / 1000)
PE_C26 = PRICE / CONS_EPS26
PE_C27 = PRICE / CONS_EPS27
PE_M27 = PRICE / EPS27
OFF_HIGH = PRICE / HI_CLOSE - 1
CHG_DEC25 = PRICE / PX_DEC25 - 1
EN_BTB_9M = ORD9M["EN"] / REV9M["EN"]
EN_EQ_BTB_9M = EN_EQ_ORD9M / EN_EQ_REV9M
EN_BOOK_X25 = BOOK_SEP26["EN"] / REV25["EN"]
EN_BOOK_LATER = BOOK_SEP26["EN"] - BOOK_2026DEL["EN"]
EN_BOOK_GROWTH = BOOK_SEP26["EN"] / BOOK_SEP25["EN"] - 1
DC_SHARE_25 = DC_MW_25 / EN_MW_25
DC_SHARE_9M26 = DC_MW_9M26 / EN_MW_9M26
DC_SHARE_Q = {k: v / m for (k, v), m in zip(DC_MW_Q.items(), EN_Q_MW[4:])}
MW_GROWTH_9M = EN_MW_9M26 / (EN_Q_MW[0] + EN_Q_MW[1] + EN_Q_MW[2]) - 1
EN_SHARE_P25 = P25["EN"] / GROUP_P25
MA_SHARE_P25 = P25["MA"] / GROUP_P25
EN_GROWTH26 = REV26["EN"] / REV25["EN"] - 1


def grid_value(ma_x, en_x):
    return (PROF["MA"] * ma_x + PROF["EN"] * en_x + BRIDGE) / SHARES * 1000


SENS = [[grid_value(a, b) for b in SENS_EN_X] for a in SENS_MA_X]

# ---- Price, month-end close (Nasdaq Nordic, WRT1V, retrieved 2 Nov 2026) ----
PX_LABELS = ["Oct 23", "Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24",
             "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25",
             "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26",
             "Jul 26", "Aug 26", "Sep 26", "30 Oct 26"]
PX = [11.24, 12.66, 13.125, 13.70, 14.295, 14.09, 17.36, 19.205, 18.00, 19.055, 20.02, 20.10, 17.51, 17.205, 17.11, 18.255,
      18.275, 16.395, 16.26, 17.63, 20.04, 24.24, 25.04, 25.45, 28.37, 27.91, 30.40, 34.20, 36.90, 31.71, 35.75, 34.90,
      33.38, 29.34, 27.89, 28.12, 25.64]

# ---- The call's tests ----
WRONG_IF = ("Energy's order intake over the four quarters to September 2027 falls below its net sales over the same "
            "quarters, or Energy's operating margin for 2027, as Wärtsilä reports it, lands below 16 per cent, or the "
            "shares close below €20 at any month end before October 2027.")

if __name__ == "__main__":
    print(f"net cash {NET_CASH} bridge {BRIDGE:.3f} mcap {MCAP:.2f} EV {EV:.2f}")
    for k in SEGS:
        print(f"{k}: rev26 {REV26[k]:.0f} p26 {P26[k]:.0f} m26 {M26[k]:.1%} | rev27 {REV27[k]:.0f} p27 {P27[k]:.0f}")
    print(f"group rev26 {GROUP_REV26:.0f} p26 {GROUP_P26:.0f} ({GROUP_P26 / GROUP_REV26:.1%}); rev27 {GROUP_REV27:.0f} p27 {GROUP_P27:.0f} ({GROUP_P27 / GROUP_REV27:.1%})")
    print(f"NI27 {NI27:.0f} EPS27 {EPS27:.3f} vs cons {CONS_EPS27}")
    print("SOTP", {k: round(v, 2) for k, v in SOTP.items()}, "EV", round(SOTP_EV, 2), "equity", round(EQUITY, 2))
    print(f"base {BASE_VALUE:.2f} {BASE_VALUE / PRICE - 1:+.1%}")
    for s, v, p in zip(SCEN, VALS, PEN):
        print(s[0], round(v, 2), f"{v / PRICE - 1:+.1%}", "EN profit", round(p, 3))
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED / PRICE - 1:+.1%}; revisit (no call above) {REVISIT_LONG:.2f}")
    print("grid", [[round(x, 2) for x in r] for r in SENS], sum(x > PRICE for r in SENS for x in r), sum(x >= PRICE * 1.15 for r in SENS for x in r))
    print(f"EN implied {EN_IMPLIED_X:.1f}x MA implied {MA_IMPLIED_X:.1f}x; EN share {EN_SHARE_EQ:.1%} MA share {MA_SHARE_EQ:.1%}")
    print(f"EV/P26 {EV_P26:.1f} EV/P27 {EV_P27:.1f}; PE cons26 {PE_C26:.1f} cons27 {PE_C27:.1f} mine27 {PE_M27:.1f}")
    print(f"off high {OFF_HIGH:.1%} vs dec25 {CHG_DEC25:+.1%}; EN btb 9M {EN_BTB_9M:.2f} eq btb {EN_EQ_BTB_9M:.2f}; book x25 {EN_BOOK_X25:.2f}; later {EN_BOOK_LATER}; book growth {EN_BOOK_GROWTH:.1%}")
    print(f"DC share 25 {DC_SHARE_25:.1%} 9M26 {DC_SHARE_9M26:.1%} q {DC_SHARE_Q}; MW growth 9M {MW_GROWTH_9M:.1%}; EN share P25 {EN_SHARE_P25:.1%}; EN growth26 {EN_GROWTH26:.1%}")
    for d, w, a, b in EVENTS:
        print(d, f"{b / a - 1:+.1%}")
    import statistics
    eng = [p for p in PEERS if p[5] == "engine"]
    print("engine median PE", statistics.median(p[2] for p in eng), "EV/EBIT", statistics.median(p[3] for p in eng))
    allp = [p for p in PEERS if p[5] != "self" and p[0] != "GE Vernova"]
    print("peers ex GEV median EV/EBIT", statistics.median(p[3] for p in allp))
