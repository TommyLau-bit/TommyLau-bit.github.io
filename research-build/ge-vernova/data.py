"""GE Vernova (NYSE: GEV) initiation, 9 Oct 2026. Single source of figures for charts, note and model.

Sources (EDGAR CIK 1996810):
- Quarterly results releases, Exhibit 99 to Form 8-K: 1Q25 (23 Apr 2025), 2Q25 (23 Jul 2025), 3Q25 (22 Oct 2025),
  4Q25 (28 Jan 2026, with full year 2025, the 2026 guide and the outlook by 2028), 1Q26 (22 Apr 2026), 2Q26 (22 Jul 2026).
- Form 10-Q for the quarter to 30 Jun 2026 (filed 22 Jul 2026): balance sheet, borrowings (Note 14), contract liabilities
  by segment (Note 9), RPO, share count, cash flow explanation, Prolec GE (Note 8).
- Form 10-Q for the quarters to 31 Mar 2026 and 30 Sep 2025, Form 10-K for 2025 (filed 29 Jan 2026): Power contract
  liabilities at earlier dates.
- Second quarter 2026 earnings call transcript, 22 Jul 2026 (gevernova.com): output plan, sold-out comments, pricing,
  commissioning times, data centre share, Q3 2026 segment outlook.
- 3rd quarter 2026 earnings webcast page, gevernova.com/investors/events: 28 Oct 2026, 7:30 am EDT.
Prices: Nasdaq.com historical data (Yahoo Finance chart API refused requests with "Too Many Requests" on 9 Oct 2026),
retrieved 9 Oct 2026. Consensus and peer multiples: stockanalysis.com (S&P Global data, updated 1 Oct 2026) and MarketBeat,
retrieved 9 Oct 2026. Everything marked MINE is my own estimate. Fiscal year = calendar year. US$ billion unless stated.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-09"
COMPANY = "GEVernova"
SLUG = "ge-vernova"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/ge-vernova"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call (Tommy Lau, 9 Oct 2026). Rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",     # Tommy Lau's call, 9 Oct 2026
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Nasdaq.com historical data, retrieved 9 Oct 2026) ----
PRICE = 999.35              # NYSE close, 8 Oct 2026
PRICE_DATE = "8 October 2026"
HI_INTRA = 1195.94          # all-time and 52-week intraday high, 6 Jul 2026
HI_CLOSE = 1174.86          # highest close, 30 Jun 2026
LO_INTRA = 530.16           # 52-week intraday low, 21 Nov 2025
LO_CLOSE = 547.96           # 52-week lowest close, 4 Nov 2025
PX_DEC25 = 653.57           # close, 31 Dec 2025
PX_Q1_PRE, PX_Q1_DAY = 991.30, 1127.56     # closes 21 and 22 Apr 2026 (1Q26 results day)
PX_Q2_PRE, PX_Q2_DAY = 1078.81, 985.03     # closes 21 and 22 Jul 2026 (2Q26 results day)

# ---- Shares and balance sheet, 30 Jun 2026 (10-Q) ----
SHARES_OUT = 266.333581     # m, outstanding 30 Jun 2026 (10-Q cover)
DILUTIVE = 3.0              # m, dilutive effect of common stock equivalents, Q2 2026 (Note 18)
SHARES = SHARES_OUT + DILUTIVE
CASH = 13.120               # cash, cash equivalents and restricted cash
DEBT = 2.849                # total borrowings incl. current maturities and finance leases (Note 14)
CL_TOTAL = 39.944           # contract liabilities and current deferred income, all segments
RPO = 176.284               # remaining performance obligation
RPO_EQ = 87.821
BUYBACK_LEFT = 3.0          # US$bn left of the US$10bn authorisation (2Q26 call)

# ---- Power contract liabilities and current deferred income (US$bn; 10-K 2025 and 10-Qs) ----
CL_LABELS = ["Dec 24", "Sep 25", "Dec 25", "Mar 26", "Jun 26"]
CL_POWER = [9.674, 12.627, 16.527, 20.396, 27.679]

# ---- Gas turbine queue (results releases), GW ----
Q = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
GW_BACKLOG = [29, 29, 33, 40, 44, 53]
GW_SRA = [21, 25, 29, 43, 56, 63]
GW_TOTAL = [50, 55, 62, 83, 100, 116]    # as stated by GE Vernova (Q2 25: 29 + 25 rounds to 55)
GW_SIGNED = [14, 9, 12, 24, 21, 20]      # Q1 25: 7 GW orders + 7 GW SRAs; Q3 25 "just over 12"
GW_SHIPPED = [None, 5, 4, 3, 4, 3]       # Q1 25 not stated in the release
GW_YE26 = 125                            # "at least 125 GW" by year end 2026 (2Q26 release)
OUTPUT_PLAN = {"2026": 20, "2028": 24, "2030": 30}   # GW a year (2Q26 release and call)
CLAIM_YEARS = 4                          # the claim's test: queue at four or more years of planned output

# ---- Quarterly results (US$bn) ----
Q_REV = [8.032, 9.111, 9.969, 10.956, 9.339, 11.104]
Q_EBITDA = [0.457, 0.770, 0.811, 1.158, 0.896, 1.250]      # adjusted EBITDA
Q_POWER_REV = [4.423, 4.758, 4.838, 5.749, 4.971, 5.477]
Q_POWER_M = [11.5, 16.4, 13.3, 16.9, 16.3, 18.8]           # Power segment EBITDA margin, as first reported
Q_POWER_ORD = [6.247, 7.088, 7.807, 11.693, 10.008, 16.729]

# ---- Annual reported ----
YEARS_H = ["2024A", "2025A"]
REV_H = [34.935, 38.068]
EBITDA_H = [2.035, 3.196]
FCF_H = [1.701, 3.710]
POWER_REV_25 = 19.767
POWER_ORD_25 = 32.835

# ---- Guidance (2Q26 release, 22 Jul 2026) and outlook by 2028 (4Q25 release, 28 Jan 2026) ----
G26 = dict(rev_lo=45.5, rev_hi=46.5, m_lo=0.12, m_hi=0.14, fcf_lo=11.5, fcf_hi=12.5)
G26_JAN = dict(rev_lo=44.0, rev_hi=45.0)
OUT28 = dict(rev=56.0, m=0.20, fcf_cum=24.0, power_m=0.22, elec_m=0.22)

# ---- Consensus and peers (retrieved 9 Oct 2026) ----
CONS_EPS_26 = 15.06         # stockanalysis.com, S&P Global, 37 analysts, updated 1 Oct 2026
CONS_EPS_27 = 25.18
CONS_REV_26 = 46.31
CONS_TP = 1230.0            # average target, 37 analysts (low 940, high 1,450)
MB_EPS_27 = 23.90           # MarketBeat
FWD_PE_SA = 47.79           # stockanalysis.com forward P/E for GEV at the 8 Oct close
PEERS = [  # company, ticker, forward P/E, EV/EBITDA (trailing), what they make
    ("GE Vernova", "NYSE: GEV", 47.79, 65.49, "Heavy-duty and aeroderivative gas turbines, grid equipment, wind turbines, services"),
    ("Mitsubishi Heavy", "TYO: 7011", 29.91, 16.21, "Heavy-duty gas turbines among a wide industrial and defence business"),
    ("Eaton", "NYSE: ETN", 28.13, 27.94, "Switchgear, power distribution and data centre electrical equipment"),
    ("Siemens Energy", "ETR: ENR", 23.98, 22.12, "Heavy-duty gas turbines, grid technology, wind turbines"),
    ("Hitachi", "TYO: 6501", 23.96, 13.64, "Transformers and grid systems through Hitachi Energy, with IT and rail"),
    ("Schneider Electric", "EPA: SU", 22.97, 18.38, "Electrical distribution, automation, data centre power and cooling"),
]

# ---- MY assumptions ----
G27, G28 = 0.11, 0.11       # revenue growth
M27, M28 = 0.165, 0.20      # adjusted EBITDA margin
BASE_MULT = 24              # EV / 2028 adjusted EBITDA, twelve months out
SCEN = [  # name, g27, g28, m28, multiple, prob
    ("Bear", 0.06, 0.06, 0.17, 16, 0.25),
    ("Base", G27, G28, M28, BASE_MULT, 0.50),
    ("Bull", 0.15, 0.15, 0.22, 30, 0.25),
]
SENS_EBITDA = [9.5, None, 13.0]     # middle row = model 2028E
SENS_MULT = [20, 24, 28]

# ---- Derived ----
REV26 = (G26["rev_lo"] + G26["rev_hi"]) / 2
M26 = (G26["m_lo"] + G26["m_hi"]) / 2
EBITDA26 = REV26 * M26
FCF26 = (G26["fcf_lo"] + G26["fcf_hi"]) / 2
NETCASH = CASH - DEBT
MCAP = PRICE * SHARES_OUT / 1000
MCAP_D = PRICE * SHARES / 1000
EV = MCAP_D - NETCASH


def project(g27, g28, m28, m27=M27):
    r27 = REV26 * (1 + g27)
    r28 = r27 * (1 + g28)
    return dict(r27=r27, r28=r28, e27=r27 * m27, e28=r28 * m28)


def value(ebitda, mult):
    return (ebitda * mult + NETCASH) / SHARES * 1000


B = project(G27, G28, M28)
REV27, REV28, EBITDA27, EBITDA28 = B["r27"], B["r28"], B["e27"], B["e28"]
SENS_EBITDA[1] = EBITDA28
VALS = [value(project(s[1], s[2], s[3])["e28"], s[4]) for s in SCEN]
EB28 = [project(s[1], s[2], s[3])["e28"] for s in SCEN]
RV28 = [project(s[1], s[2], s[3])["r28"] for s in SCEN]
WEIGHTED = sum(v * s[5] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75
OUT28_EBITDA = OUT28["rev"] * OUT28["m"]
NEED_EBITDA28 = (MCAP_D - NETCASH) / BASE_MULT
EV_EB26 = EV / EBITDA26
EV_EB27 = EV / EBITDA27
EV_EB28 = EV / EBITDA28
EV_OUT28 = EV / OUT28_EBITDA
PE_C26, PE_C27 = PRICE / CONS_EPS_26, PRICE / CONS_EPS_27
FCF_YIELD26 = FCF26 / MCAP_D
GW_YEARS = [g / OUTPUT_PLAN["2026"] for g in GW_TOTAL]
NEED_GW = {y: CLAIM_YEARS * v for y, v in OUTPUT_PLAN.items()}
CL_RISE_H1 = CL_POWER[-1] / CL_POWER[2] - 1
CL_MULT_18M = CL_POWER[-1] / CL_POWER[0]
CL_VS_POWER_REV = CL_POWER[-1] / POWER_REV_25
FCF_TO_EBITDA26 = FCF26 / EBITDA26
CUM_FCF_25_26 = FCF_H[1] + FCF26
RISE_DEC25 = PRICE / PX_DEC25 - 1
OFF_HIGH = PRICE / HI_CLOSE - 1
RISE_LO = PRICE / LO_CLOSE - 1
Q1_MOVE = PX_Q1_DAY / PX_Q1_PRE - 1
Q2_MOVE = PX_Q2_DAY / PX_Q2_PRE - 1

# ---- Price, month-end close (Nasdaq.com historical data, retrieved 9 Oct 2026) ----
PX_LABELS = ["Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25",
             "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26",
             "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "8 Oct 26"]
PX = [153.71, 175.90, 171.51, 178.24, 201.00, 254.98, 301.66, 334.12, 328.93, 372.88, 335.18, 305.28, 370.82, 472.98,
      529.15, 660.29, 612.97, 614.90, 585.14, 599.77, 653.57, 726.37, 873.60, 872.90, 1083.46, 968.32, 1174.86, 990.29,
      898.53, 950.49, 999.35]

# ---- The call's tests (Tommy Lau, 9 Oct 2026) ----
REVISIT_IF = ("A price below about US$910, where my base value would sit 15 per cent above it, or GE Vernova raising its 2028 "
              "outlook above US$60 billion of revenue at a 20 per cent adjusted EBITDA margin.")
WRONG_IF = ("The shares close above US$1,250 or below US$750 in October 2027, or full year 2026 adjusted EBITDA margin lands "
            "outside GE Vernova's own 12 to 14 per cent guide, or gigawatts under contract fall below 80 at any quarter end "
            "before 2028, four years of the 20 gigawatt output.")

if __name__ == "__main__":
    print(f"shares {SHARES:.1f} mcap {MCAP:.1f} mcapD {MCAP_D:.1f} netcash {NETCASH:.3f} EV {EV:.1f}")
    print(f"2026 rev {REV26} m {M26:.1%} ebitda {EBITDA26:.3f} fcf {FCF26}")
    print(f"2027 rev {REV27:.2f} ebitda {EBITDA27:.2f}; 2028 rev {REV28:.2f} ebitda {EBITDA28:.2f}; outlook ebitda {OUT28_EBITDA:.2f}")
    for s, v, e, r in zip(SCEN, VALS, EB28, RV28):
        print(s[0], round(r, 2), round(e, 2), round(v, 1), f"{v / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.0f} short {REVISIT_SHORT:.0f}")
    print("grid", [[round(value(e, m)) for m in SENS_MULT] for e in SENS_EBITDA],
          sum(value(e, m) > PRICE for e in SENS_EBITDA for m in SENS_MULT))
    print(f"EV/EBITDA 26 {EV_EB26:.1f} 27 {EV_EB27:.1f} 28 {EV_EB28:.1f} out28 {EV_OUT28:.1f}; need ebitda28 {NEED_EBITDA28:.2f}")
    print(f"PE cons 26 {PE_C26:.1f} 27 {PE_C27:.1f}; FCF yield 26 {FCF_YIELD26:.1%}; FCF/EBITDA {FCF_TO_EBITDA26:.2f}; cum {CUM_FCF_25_26:.2f}")
    print("GW years", [round(x, 2) for x in GW_YEARS], NEED_GW)
    print(f"CL rise H1 {CL_RISE_H1:.1%} x18m {CL_MULT_18M:.2f} vs power rev {CL_VS_POWER_REV:.2f}")
    print(f"rise dec {RISE_DEC25:.1%} off high {OFF_HIGH:.1%} rise lo {RISE_LO:.1%} q1 {Q1_MOVE:+.1%} q2 {Q2_MOVE:+.1%}")
    import statistics; print("peer median PE", statistics.median([p[2] for p in PEERS[1:]]), "EV/EBITDA", statistics.median([p[3] for p in PEERS[1:]]))
