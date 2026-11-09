"""The Williams Companies, Inc. (NYSE: WMB) initiation, drafted 2 Nov 2026. Single source of figures for charts, note and model.

Fiscal year = calendar year. US$ million unless stated.
Sources (SEC EDGAR, Williams CIK 107263):
- Q2 2026 earnings release, Form 8-K Ex. 99.1, 3 Aug 2026 (wmb_20260630xer.htm): Adjusted EBITDA by segment and quarter,
  balance sheet at 30 Jun 2026, AFFO and dividends, 2026 guidance (Adjusted EBITDA US$8.3-8.5bn, growth capex US$7.3-7.9bn),
  2026 guidance reconciliation (AFFO US$6,375m, interest US$1,535m, NCI and preferred US$220m), Momentum terms (up to
  US$5.5bn, ~8.5x projected 2027 EBITDA), $777m reimbursable long-lead Power Innovation equipment, Socrates phase one done.
- Form 10-Q for the quarter to 30 Jun 2026, filed 3 Aug 2026: Socrates 556 MW expected (North and South), South in service
  late July 2026, North Q4 2026, 10-year primarily fixed-price PPA; Apollo 490 MW / 12.5 yr / 2H27; Aquila 520 MW / 12.5 yr /
  2H27-1H28; Socrates the Younger 340 MW / 10 yr / 2H28; Neo 682 MW / 12.5 yr / 2H28; JV note (US$5.34bn for 49%, ~US$3.75bn
  received July 2026, rest through early 2027, buyout right years 7 to 14); SESE as early as 3Q 2027, 1,597 Mdth/d;
  1,223,167,472 shares outstanding at 30 Jul 2026.
- Form 10-K 2025 (filed 24 Feb 2026): Socrates "a combined 400 megawatts of onsite power generation capacity to the
  customer"; projects 1.9 GW, up to 12.5-year primarily fixed-price agreements with a large, investment-grade company.
- Form 10-Q Q1 2026 (4 May 2026): Socrates "together have an expected 556 MW of capacity".
- Q1 2026 release (4 May 2026): Neo, US$2.3bn, 682 MW installed. Q4 2025 release (10 Feb 2026): over US$7bn of power
  innovation capital in execution; 2025 Adjusted EBITDA 7,750; 2026 dividend US$2.10. Q3 2025 release: Socrates scope
  raised by ~US$400m to US$2bn.
- Form 8-K 13 Jul 2026, Ex. 99.1 and 99.2 (Blackstone JV): US$4.4bn = 49% of expected growth capex, ~US$0.9bn more;
  6.35% target return; buyout multiples 2.3x / 1.6x / 0.8x / 0.0x in years 8 to 11; 2.6 GW announced; 6+ GW backlog.
- 424B2 prospectus supplement, 3 Sep 2026: 26,874,496 shares issued to the Momentum sellers.
- Calls (third-party transcripts, AllMind): Q1 2026 (5 May, CEO): Neo, "like our other power innovation projects", at "an attractive
  5x build multiple"; Q2 2026 (4 Aug): US$9.6bn on Williams' slides per an analyst, CFO: capitalised interest the biggest part of the gap;
  CEO: 200 MW "in under 18 months since commercialization"; "locked up the turbines"; 11%+ EBITDA CAGR 2025-2030 target; year-end
  leverage ~3.9x; 2027 a high watermark for capital.
- PJM 2027/2028 Base Residual Auction report (Dec 2025): RTO clearing price US$333.44/MW-day.
Prices: Nasdaq.com historical data API (WMB, NYSE-listed), retrieved 2 Nov 2026, cross-checked against stockanalysis.com
(S&P Global data). Consensus EPS, targets and multiples: stockanalysis.com, retrieved 2 Nov 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "Williams"
SLUG = "williams"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/williams"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Tommy Lau, 2 Nov 2026: NO CALL, Medium. Rebuild = edit this dict only. ----
CALL = dict(
    banner="NO CALL",
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Nasdaq.com historical, retrieved 2 Nov 2026) ----
PRICE = 74.35               # NYSE close, Friday 30 Oct 2026
PRICE_DATE = "30 October 2026"
HI_CLOSE = 79.40            # highest close, 19 May 2026
HI_INTRA = 80.075           # intraday high, 20 May 2026
PX_DEC25 = 60.11            # close 31 Dec 2025
PX_JUL10, PX_JUL13 = 75.02, 74.46       # JV announced 13 Jul 2026 (before the open)
PX_AUG3, PX_AUG4 = 70.43, 71.51         # Q2 results 3 Aug after the close
PX_FEB9, PX_FEB10 = 67.85, 68.84        # Q4 results and Analyst Day 10 Feb 2026 (before the open)
PX_MAY4, PX_MAY5 = 75.41, 76.12         # Q1 results 4 May after the close

# ---- Shares and balance sheet ----
SHARES_JUL = 1223.167       # m, 30 Jul 2026 (10-Q cover)
SHARES_MOM = 26.874         # m, issued to the Momentum sellers (424B2, 3 Sep 2026)
SHARES = SHARES_JUL + SHARES_MOM
CASH_JUN = 203.0
DEBT_JUN = 475.0 + 2197.0 + 28121.0     # commercial paper + current LTD + LTD, 30 Jun 2026
NETDEBT_JUN = DEBT_JUN - CASH_JUN
NCI_BOOK = 2178.0           # noncontrolling interests (book), 30 Jun 2026
NCI_INC_RUN = 190.0         # MINE: pre-JV run-rate of income to NCI (H1 2026: 96)
NCI_PE = 20.0               # MINE: value existing NCI at 20x that income
NCI_VALUE = NCI_INC_RUN * NCI_PE
BX_TOTAL = 5340.0           # Blackstone committed capital
BX_JUL = 3750.0             # received July 2026
BX_REST = BX_TOTAL - BX_JUL # through early 2027

# ---- History and guidance (company releases) ----
EBITDA = {"2024A": 7080.0, "2025A": 7750.0}
AFFO = {"2024A": 5378.0, "2025A": 5858.0}
DPS = {"2024A": 1.90, "2025A": 2.00, "2026G": 2.10}
ADJ_EPS = {"2024A": 1.92, "2025A": 2.10}
G26 = dict(lo=8300.0, hi=8500.0, mid=8400.0, affo=6375.0, int=1535.0, nci=220.0, eps=2.35, div_paid=2585.0,
           gcx_lo=7300.0, gcx_hi=7900.0, mcx=900.0)
H1_26 = dict(ebitda=4175.0, affo=3220.0, div=1284.0, capex=3193.0)
Q_LBL = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_EBITDA = [1989, 1808, 1920, 2033, 2254, 1921]
Q_TPG = [862, 903, 947, 998, 1010, 959]      # Transmission, Power & Gulf Adjusted EBITDA
TTM_EBITDA = sum(Q_EBITDA[-4:])
LEV_Q2 = 3.67
CONS_EPS26, CONS_EPS27 = 2.42, 2.62         # stockanalysis.com, updated 22 Oct 2026
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 85.38, 25, 69.0, 103.0
LT_TARGET = 0.11            # Williams: 11%+ Adjusted EBITDA CAGR 2025-2030 (Q2 call)

# ---- Power Innovation: the five projects in the Blackstone JV (10-Q, 30 Jun 2026) ----
# name, installed MW, contract years, (2026, 2027, 2028) share of the year in service (MINE, from Williams' windows)
PROJ = [
    ("Socrates", 556, 10.0, (0.17, 1.0, 1.0), "Ohio", "South late Jul 2026; North Q4 2026", "Meta (Sidecat), per Ohio Power Siting Board"),
    ("Apollo", 490, 12.5, (0.0, 0.25, 1.0), "Ohio", "2H 2027", "Not named"),
    ("Aquila", 520, 12.5, (0.0, 0.15, 0.85), "Utah", "2H 2027 to 1H 2028", "Not named"),
    ("Socrates the Younger", 340, 10.0, (0.0, 0.0, 0.2), "Ohio", "2H 2028", "Not named"),
    ("Neo", 682, 12.5, (0.0, 0.0, 0.2), "Ohio", "2H 2028", "Not named; 'a high-quality hyperscaler'"),
]
MW_TOTAL = sum(p[1] for p in PROJ)
CAPEX_PI = 9600.0           # US$m incl. capitalised interest (Q2 call); ~9.0bn growth capex ex interest (US$4.4bn = 49%)
CAPEX_PI_EX = 4400.0 / 0.49
BUILD_MULT = 5.0            # Williams on Neo (Q1 call)
PI_RUN = 1800.0             # MINE: five-project run-rate EBITDA, 2029
EB_PER_MW = PI_RUN / MW_TOTAL               # US$m per installed MW-year
EB_PER_MWDAY = EB_PER_MW * 1e6 / 365        # US$ per MW-day
PJM_CAP = 333.44            # US$/MW-day, PJM 2027/28 BRA
CONTRACT_YRS = sum(p[1] * p[2] for p in PROJ) / MW_TOTAL
PI_REMAIN = 1500.0          # MINE: power capex still to spend after 2027


def pi_ebitda(i, shift=0.0):
    """Power EBITDA in year index i (0=2026, 1=2027, 2=2028)."""
    return sum(p[1] * EB_PER_MW * p[3][i] for p in PROJ)


PI26, PI27, PI28 = pi_ebitda(0), pi_ebitda(1), pi_ebitda(2)

# ---- Momentum (acquired 3 Sep 2026) ----
MOM27 = 5500.0 / 8.5        # Williams: ~8.5x projected 2027 EBITDA
MOM26 = MOM27 * 4 / 12      # MINE: four months
MOM28 = 700.0               # MINE: Shelby Trough from 2Q 2028

# ---- MY core (pipes, gathering, marketing, other; ex Momentum, ex Power Innovation) ----
CORE26 = G26["mid"] - MOM26 - PI26
CORE_G27, CORE_G28 = 0.04, 0.05
CORE27 = CORE26 * (1 + CORE_G27)
CORE28 = CORE27 * (1 + CORE_G28)
EB26 = G26["mid"]
EB27 = CORE27 + MOM27 + PI27
EB28 = CORE28 + MOM28 + PI28
EB30 = CORE28 * 1.05 ** 2 + 760.0 + PI_RUN  # MINE, 2030, signed projects only
CAGR30 = (EB30 / EBITDA["2025A"]) ** 0.2 - 1

# ---- AFFO, dividends, net debt roll (MINE unless guided) ----
INT27, INT28 = 1700.0, 1800.0
NCI_DIST26 = 328.0
NCI_DIST27 = 335.0 + 0.49 * PI27
NCI_DIST28 = 335.0 + 0.49 * PI28
OTHER27, OTHER28 = 200.0, 220.0
AFFO26 = G26["affo"]
AFFO27 = EB27 - INT27 - NCI_DIST27 - OTHER27
AFFO28 = EB28 - INT28 - NCI_DIST28 - OTHER28
DPS27, DPS28 = 2.205, 2.315                 # MINE: +5% a year, the 2025 and 2026 pace
GCX27, MCX27 = 7500.0, 950.0
H2_GCX = (G26["gcx_lo"] + G26["gcx_hi"]) / 2 - 3284.0   # 2026 growth capex mid less H1 capital investments
H2_MCX = G26["mcx"] / 2
BX_Q4 = 800.0                               # MINE: Blackstone contributions in Q4 2026
ND26 = NETDEBT_JUN - BX_JUL - BX_Q4 + 3500.0 + H2_GCX + H2_MCX - (AFFO26 - H1_26["affo"]) + (G26["div_paid"] - H1_26["div"])
ND27 = ND26 - (BX_REST - BX_Q4) + GCX27 + MCX27 - AFFO27 + DPS27 * SHARES
ND_SEP = NETDEBT_JUN - BX_JUL + 3500.0 + 2400.0 + 640.0 + 80.0 - 1550.0   # MINE, 30 Sep 2026

# ---- Valuation (12 months out, on 2028E; sum of the parts) ----
CORE_MULT = 13.5            # MINE: pipes and gathering, EV / 2028E EBITDA
PI_MULT = 8.0               # MINE: power, EV / run-rate EBITDA


def value(core28=None, mom28=MOM28, core_mult=CORE_MULT, pi_mult=PI_MULT, pi_run=PI_RUN):
    c = CORE28 if core28 is None else core28
    ev = (c + mom28) * core_mult + pi_run * pi_mult - PI_REMAIN
    eq = ev - ND27 - NCI_VALUE - BX_TOTAL
    return dict(ev=ev, eq=eq, ps=eq / SHARES)


BASE = value()
BASE_VALUE = BASE["ps"]
SCEN = [  # name, core g27, core g28, momentum 28, core mult, power mult, power run, prob
    ("Bear", 0.02, 0.02, 650.0, 11.5, 6.0, PI_RUN, 0.25),
    ("Base", CORE_G27, CORE_G28, MOM28, CORE_MULT, PI_MULT, PI_RUN, 0.50),
    ("Bull", 0.05, 0.06, 720.0, 15.0, 11.0, PI_RUN, 0.25),
]
SC = []
for s in SCEN:
    c28 = CORE26 * (1 + s[1]) * (1 + s[2])
    v = value(c28, s[3], s[4], s[5], s[6])
    SC.append(dict(name=s[0], core28=c28, ebp=c28 + s[3], cm=s[4], pm=s[5], value=v["ps"], prob=s[7]))
WEIGHTED = sum(x["value"] * x["prob"] for x in SC)
SENS_CM = [12.0, CORE_MULT, 15.0]
SENS_PM = [6.0, PI_MULT, 10.0]
GRID = [[value(core_mult=c, pi_mult=p)["ps"] for p in SENS_PM] for c in SENS_CM]

# ---- What the price implies ----
MCAP = PRICE * SHARES / 1000
EV_NOW = MCAP + (ND_SEP + NCI_VALUE + BX_JUL) / 1000      # US$bn, NCI incl. Blackstone funded so far
EV_EB26 = EV_NOW * 1000 / EB26
EV_EB27 = EV_NOW * 1000 / EB27
EQ_PX = PRICE * SHARES
IMPL_PI_MULT = (EQ_PX + ND27 + NCI_VALUE + BX_TOTAL + PI_REMAIN - (CORE28 + MOM28) * CORE_MULT) / PI_RUN
CONTRACT_PV = (1 - 1.08 ** -CONTRACT_YRS) / 0.08          # PV of 1 a year over the MW-weighted term at 8%
# unlevered IRR on 5x build multiple over the MW-weighted term, no residual
def irr(mult, n):
    lo, hi = 0.0, 1.0
    for _ in range(100):
        m = (lo + hi) / 2
        if (1 - (1 + m) ** -n) / m > mult: lo = m
        else: hi = m
    return m
IRR_5X = irr(BUILD_MULT, CONTRACT_YRS)

# ---- Dividend cross-check (two-stage DDM) ----
KE = 0.08                   # MINE: cost of equity
DG1, DG2, DN = 0.07, 0.03, 10   # MINE: +7% a year for ten years, then 3%
def ddm(ke=KE, g1=DG1, g2=DG2, n=DN):
    d = DPS["2026G"]; pv = 0.0
    for t in range(1, n + 1):
        d *= 1 + g1; pv += d / (1 + ke) ** t
    tv = d * (1 + g2) / (ke - g2)
    return pv + tv / (1 + ke) ** n
DDM_VALUE = ddm()
def solve(f, lo, hi, target=PRICE):
    for _ in range(100):
        m = (lo + hi) / 2
        if f(m) < target: lo = m
        else: hi = m
    return m
DIV_G_NEEDED = solve(lambda g: ddm(g1=g), 0.0, 0.5)        # growth the price needs at 8% and 3% after
IMPL_KE = solve(lambda k: -ddm(ke=k), 0.04, 0.2, -PRICE)  # cost of equity the price implies at my growth
AFFO_PS26 = G26["affo"] / 1237.0                            # Williams' guide, US$5.15 on 1,237m diluted shares
YIELD = DPS["2026G"] / PRICE

UP_BASE = BASE_VALUE / PRICE - 1
LONG_BELOW = BASE_VALUE / 1.15
SHORT_ABOVE = BASE_VALUE / 0.75
OFF_HIGH = PRICE / HI_CLOSE - 1
YTD = PRICE / PX_DEC25 - 1

PEERS = [  # company, ticker, EV/EBITDA trailing, forward P/E, dividend yield, what they do, group (stockanalysis.com, 2 Nov 2026)
    ("Williams", "NYSE: WMB", 17.28, 29.95, 0.0282, "Transco and other gas pipes, gathering, storage; off-grid gas power", "self"),
    ("Kinder Morgan", "NYSE: KMI", 14.05, 21.80, 0.0351, "Gas pipelines and storage, products and CO2", "peer"),
    ("DT Midstream", "NYSE: DTM", 16.85, 25.14, 0.0283, "Gas pipelines and gathering", "peer"),
    ("Targa Resources", "NYSE: TRGP", 15.82, 27.30, 0.0159, "Gas gathering and processing, NGL logistics", "peer"),
    ("ONEOK", "NYSE: OKE", 11.62, 16.39, 0.0441, "NGL, gas gathering, processing and pipelines", "peer"),
    ("Enterprise Products", "NYSE: EPD", 10.89, 12.37, 0.0587, "NGL, gas, crude and petrochemical pipelines", "peer"),
    ("Energy Transfer", "NYSE: ET", 8.23, 12.63, 0.0650, "Gas, NGL and crude pipelines", "peer"),
]
WMB_EV_EB_HIST = {"2021": 12.62, "2022": 12.96, "2023": 10.88, "2024": 16.94, "2025": 15.30}   # stockanalysis.com basis

# ---- Price, month-end close (Nasdaq.com historical, retrieved 2 Nov 2026) ----
PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24",
             "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
             "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26",
             "30 Oct 26"]
PX = [34.66, 35.94, 38.97, 38.36, 41.51, 42.50, 42.94, 45.77, 45.65, 52.37, 58.52, 54.12, 55.43, 58.18, 59.76, 58.57,
      60.51, 62.81, 59.95, 57.88, 63.35, 57.87, 60.93, 60.11, 67.26, 74.72, 72.78, 76.31, 71.39, 74.34, 71.54, 75.05,
      67.97, 74.35]

WRONG_IF = ("The shares close above US$93 or below US$56 in October 2027, a quarter above or below the price; or 2026 "
            "Adjusted EBITDA lands below the US$8.3 billion bottom of Williams' guide; or Socrates North is not in service "
            "by 31 March 2027.")
REVISIT_IF = None  # filled below once the base value is known

if __name__ == "__main__":
    print(f"shares {SHARES:.1f} mcap {MCAP:.1f} ND_jun {NETDEBT_JUN:.0f} ND_sep {ND_SEP:.0f} ND26 {ND26:.0f} ND27 {ND27:.0f}")
    print(f"EV now {EV_NOW:.1f}  EV/EB26 {EV_EB26:.1f} EV/EB27 {EV_EB27:.1f} ttm {TTM_EBITDA}")
    print(f"MW {MW_TOTAL} EB/MW {EB_PER_MW:.3f} per MW-day {EB_PER_MWDAY:.0f} vs PJM {PJM_CAP} x{EB_PER_MWDAY / PJM_CAP:.1f} term {CONTRACT_YRS:.2f}")
    print(f"PI 26 {PI26:.0f} 27 {PI27:.0f} 28 {PI28:.0f}; capex ex {CAPEX_PI_EX:.0f} build mult ex {CAPEX_PI_EX / PI_RUN:.2f} incl {CAPEX_PI / PI_RUN:.2f}")
    print(f"MOM 26 {MOM26:.0f} 27 {MOM27:.0f}; core 26 {CORE26:.0f} 27 {CORE27:.0f} 28 {CORE28:.0f}")
    print(f"EB 26 {EB26:.0f} 27 {EB27:.0f} 28 {EB28:.0f} 30 {EB30:.0f} cagr {CAGR30:.1%}  target 2028 {7750 * 1.11 ** 3:.0f} 2030 {7750 * 1.11 ** 5:.0f}")
    print(f"AFFO 27 {AFFO27:.0f} 28 {AFFO28:.0f} per sh {AFFO27 / SHARES:.2f} {AFFO28 / SHARES:.2f}; cover {AFFO27 / (DPS27 * SHARES):.2f} {AFFO28 / (DPS28 * SHARES):.2f}")
    print(f"lev 26 {ND26 / (EB26 + MOM27 * 8 / 12):.2f} lev27 {ND27 / EB27:.2f}")
    print(f"base EV {BASE['ev']:.0f} eq {BASE['eq']:.0f} ps {BASE_VALUE:.2f} {UP_BASE:+.1%}; long below {LONG_BELOW:.2f} short above {SHORT_ABOVE:.2f}")
    for x in SC: print(x["name"], round(x["core28"]), round(x["ebp"]), x["cm"], x["pm"], round(x["value"], 2), f"{x['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED / PRICE - 1:+.1%}")
    print("grid", [[round(v, 1) for v in r] for r in GRID])
    print(f"implied power mult {IMPL_PI_MULT:.2f}; contract PV {CONTRACT_PV:.2f}; IRR 5x {IRR_5X:.1%}")
    print(f"DDM {DDM_VALUE:.2f} implied ke {IMPL_KE:.2%} g needed {DIV_G_NEEDED:.2%} yield {YIELD:.2%} affo/sh26 {AFFO_PS26:.2f}")
    print(f"off high {OFF_HIGH:.1%} ytd {YTD:.1%} jul13 {PX_JUL13 / PX_JUL10 - 1:+.1%} aug4 {PX_AUG4 / PX_AUG3 - 1:+.1%} feb10 {PX_FEB10 / PX_FEB9 - 1:+.1%} may5 {PX_MAY5 / PX_MAY4 - 1:+.1%}")
    import statistics
    ps = [p for p in PEERS if p[6] == "peer"]
    print("peer median EV/EBITDA", statistics.median(p[2] for p in ps), "fwd PE", statistics.median(p[3] for p in ps))
    print("PE on cons 26/27", PRICE / CONS_EPS26, PRICE / CONS_EPS27, "guide eps", PRICE / G26["eps"])
