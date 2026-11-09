"""Entergy Corporation (NYSE: ETR) initiation, drafted 2 Nov 2026. Single source of figures for charts, note and model.

Fiscal year = calendar year. US$ million unless stated. Adjusted EPS as Entergy defines it (non-GAAP).
Sources (SEC EDGAR, Entergy CIK 65984):
- Q4 2025 earnings release, Form 8-K Ex. 99.1, 12 Feb 2026: 2025 adjusted EPS $3.91 (2024 $3.65), Q4 2025 $0.51 (Q4 2024
  $0.66); 2026 guide $4.25-4.45 initiated.
- Q1 2026 earnings release, Form 8-K Ex. 99.1, 29 Apr 2026: Q1 2026 adjusted EPS $0.86 (Q1 2025 $0.82).
- Q2 2026 earnings release, Form 8-K Ex. 99.1, 29 Jul 2026: Q2 adjusted EPS $1.03 (Q2 2025 $1.05), H1 $1.90; guide
  affirmed; weather-adjusted retail sales +5.7% (Q2), industrial +9.9% (Q2), +12.3% (H1); return on CWIP +$0.07 (Q2),
  +$0.12 (H1); cash $3,854m, total debt $34,749m at 30 Jun 2026; FFO to adjusted debt 15.8%.
- Form 10-Q for the quarter to 30 Jun 2026, filed 31 Jul 2026: capital plan 2026-2030 by year (total $66,530m), which
  "reflects" the March 2026 Meta (Evest) application; second Meta ESA (March 2026), seven CCCTs, 5,278 MW, ~$12.9bn,
  500 kV West Fork Creek to St. Landry line ~$1.4bn, in service 2030 and 2031, LPSC consideration at its December 2026
  meeting, hearing October 2026; minimum monthly bills, contributions in aid of construction, early termination
  obligations, Meta Platforms guaranty; subpoena dispute (June-July 2026); ~$7bn of equity through 2030, ~$4.1bn
  settled or contracted at 30 Jun 2026; 466,631,498 shares at 30 Jun 2026; power island exclusivity agreement, minimum
  27 PIE sets (amended Q2 2026), 10 fulfilled; customer advances on the balance sheet.
- 2025 Form 10-K, filed 19 Feb 2026: first Meta application (Oct 2024), three CCCTs 2,262 MW, Franklin Farms 1 and 2
  ~$2,387m (2028), Waterford 5 similar to each Franklin Farms unit (2029), 500 kV line ~$546m, LPSC order Aug 2025,
  termination payments; intervenors' January 2026 motion on the customer's financing; PIE agreement (one slot a quarter).
- Form 8-K, 2 Sep 2026: 11,145,984 shares delivered under the 2025 forwards (~$913m); 19,247,788 shares under the May
  2026 forwards still outstanding.
- Entergy 2026 Investor Day presentation, 9 Jun 2026 (investors.entergy.com, q4cdn PDF): adjusted EPS guide and outlooks
  2026-2030; $67bn 2026-2030 capital plan; projected rate base $46bn (2025E) to $97bn (2030E); $7bn equity plan; 6%
  dividend growth assumption; ~9% retail and ~16% industrial sales CAGR to 2030; hyperscale contract features
  (15 to 20 year terms, minimum bills, early termination fee, CIAC); 10 CCCTs secured for growth; 7-12 GW data centre
  pipeline beyond the base case; E-LA authorised ROE 9.3-10.1%, equity ratio 50.91%.
Prices: Yahoo Finance history pages (ETR, split-adjusted closes, not dividend-adjusted), read 2 Nov 2026 (the chart API
returned "Too Many Requests"); daily closes cross-checked against stockanalysis.com. Consensus, targets and peer
multiples: stockanalysis.com (S&P Global data), retrieved 2 Nov 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "Entergy"
SLUG = "entergy"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/entergy"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call (Tommy Lau). Rebuild = edit this dict only. ----
CALL = dict(
    banner="NO CALL",                 # Tommy Lau's call, 2 Nov 2026 (draft view adopted on his instruction)
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Yahoo Finance ETR, read 2 Nov 2026) ----
PRICE = 110.11              # NYSE close, Friday 30 Oct 2026
PRICE_DATE = "30 October 2026"
HI_CLOSE = 117.91           # highest close, 30 Apr 2026
HI_INTRA = 118.45           # intraday high, 1 May 2026
PX_DEC25 = 92.43            # close 31 Dec 2025
PX_OFFER_PRE, PX_OFFER_DAY = 117.36, 112.96   # closes 5 and 6 May 2026 (US$2.175bn offering priced 5 May)
PX_Q2_PRE, PX_Q2_DAY = 112.32, 107.79         # closes 28 and 29 Jul 2026 (Q2 results 29 Jul)
PX_SEP_LO = 98.10           # close 28 Sep 2026, lowest close of September
DIV_Q = 0.68                # quarterly dividend declared 2 Nov 2026, up 6% from US$0.64 (Q3 2026 release)
DIV_Q_OLD = 0.64

# ---- Shares and balance sheet ----
SHARES_OUT = 466.631498 + 11.145984   # m: 30 Jun 2026 (10-Q cover) + 2 Sep 2026 forward settlement (8-K) = 477.78m
FWD_UNSETTLED = 19.247788            # m, May 2026 forwards, not yet settled (8-K, 2 Sep 2026)
CASH = 4205.0               # 30 Sep 2026 (Q3 2026 release, Appendix D)
DEBT = 34936.0              # total debt, 30 Sep 2026 (Q3 2026 release, Appendix D; includes US$4.0bn junior subordinated debentures)
FFO_DEBT = 0.168            # FFO to adjusted debt, 12 months to 30 Sep 2026
EQUITY_PLAN, EQUITY_DONE = 7000.0, 4100.0     # US$m through 2030; settled or contracted at 30 Jun 2026 (10-Q)

# ---- Earnings, as reported (adjusted EPS, US$) ----
ADJ_EPS = {"2024A": 3.65, "2025A": 3.91}
Q_LABELS = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
Q_EPS = [0.82, 1.05, 1.53, 0.51, 0.86, 1.03, 1.98]   # Q3 2025 and Q3 2026 from the Q3 2026 release, 2 Nov 2026
H1_26 = 1.90                 # as reported (Q2 release; quarters sum to 1.89 on rounding)
GUIDE = {  # 2026 guide narrowed 2 Nov 2026 from 4.25-4.45; outlooks 2027-2030 from Investor Day 9 Jun 2026, affirmed 2 Nov 2026
    "2026": (4.35, 4.45), "2027": (4.90, 5.20), "2028": (5.55, 5.85), "2029": (6.25, 6.55), "2030": (7.05, 7.35),
}
MID = {y: (lo + hi) / 2 for y, (lo, hi) in GUIDE.items()}

# ---- Capital plan, rate base, data centre projects ----
CAPEX = {"2026": 13165, "2027": 16845, "2028": 15380, "2029": 11820, "2030": 9320}   # 10-Q Q2 2026, US$m
CAPEX_TOTAL = sum(CAPEX.values())
RATE_BASE = {"2025E": 46, "2026E": 58, "2027E": 73, "2028E": 80, "2029E": 89, "2030E": 97}   # Investor Day, US$bn
META1_MW, META2_MW = 2262, 5278
FF_COST = 2387.0            # Franklin Farms 1 and 2, US$m (10-K)
W5_COST = FF_COST / 2       # MINE: Waterford 5 "similar to the cost of each" Franklin Farms unit (10-K)
META1_LINE = 546.0
META2_PLANTS, META2_LINE = 12900.0, 1400.0
META1_TOTAL = FF_COST + W5_COST + META1_LINE
META2_TOTAL = META2_PLANTS + META2_LINE
META_SHARE = (META1_TOTAL + META2_TOTAL) / CAPEX_TOTAL
ELA_ROE = (0.093 + 0.101) / 2   # E-LA authorised ROE band midpoint (Investor Day appendix)
ELA_EQ = 0.5091                 # E-LA equity ratio (Investor Day appendix)
META2_NI = META2_TOTAL * ELA_EQ * ELA_ROE           # MINE: upper bound, US$m a year once all in rate base
META2_EPS = META2_NI / (SHARES_OUT + FWD_UNSETTLED)
PIE_MIN, PIE_DONE = 27, 10
CUST_ADV_JUN26 = 1470.056 + 170.298 + 2086.359     # current + non-current + for construction, 30 Jun 2026 (10-Q)
CUST_ADV_DEC25 = 632.850 + 35.000 + 1615.455

# ---- MY estimates and the valuation ----
E26 = MID["2026"]           # MINE: narrowed guide midpoint
YTD_26 = 3.89               # adjusted EPS, nine months to 30 Sep 2026 (Q3 2026 release)
Q3_WEATHER = 0.24           # estimated weather effect in Q3 2026 EPS (Q3 2026 release)
E27 = MID["2027"]           # MINE: outlook midpoint
E28 = MID["2028"]           # MINE: outlook midpoint
BASE_PE = 21.5              # MINE: about today's multiple of the 2027 consensus, held a year forward

CONS_EPS26, CONS_EPS27 = 4.41, 5.10     # stockanalysis.com (S&P Global), retrieved 2 Nov 2026
CONS_N26 = 17
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 119.71, 24, 91.0, 131.0
FWD_PE_SA = 22.54          # stockanalysis.com forward P/E, re-read 2 Nov 2026 after the Q3 release (was 23.21 earlier that day)

PEERS = [  # company, ticker, forward P/E, EV/EBITDA, what they run, group
    ("Entergy", "NYSE: ETR", 22.54, 15.06, "Regulated utilities in Louisiana, Arkansas, Mississippi and Texas; gas, nuclear and solar", "self"),
    ("NextEra Energy", "NYSE: NEE", 20.27, 21.19, "Florida Power & Light and a large renewables developer", "peer"),
    ("Southern Company", "NYSE: SO", 20.14, 12.76, "Regulated utilities in Georgia, Alabama and Mississippi; Vogtle nuclear", "peer"),
    ("American Electric Power", "Nasdaq: AEP", 19.14, 13.26, "Regulated utilities in 11 states; largest US transmission network", "peer"),
    ("Duke Energy", "NYSE: DUK", 18.77, 11.49, "Regulated utilities in the Carolinas, Florida and the Midwest", "peer"),
    ("Xcel Energy", "Nasdaq: XEL", 18.16, 14.44, "Regulated utilities in eight Midwest and Western states", "peer"),
]

# ---- Scenarios: name, 2028 EPS, multiple, probability ----
SCEN = [
    ("Bear", 5.45, 18.0, 0.25),
    ("Base", E28, BASE_PE, 0.50),
    ("Bull", 5.95, 24.0, 0.25),
]
SC = [dict(name=s[0], e28=s[1], mult=s[2], value=s[1] * s[2], prob=s[3]) for s in SCEN]
WEIGHTED = sum(x["value"] * x["prob"] for x in SC)
BASE_VALUE = BASE_PE * E28
SENS_EPS = [5.45, E28, 5.95]
SENS_PE = [19.0, BASE_PE, 24.0]

# ---- Derived market figures ----
MCAP = PRICE * SHARES_OUT / 1000
NET_DEBT = DEBT - CASH
EV = MCAP + NET_DEBT / 1000
PE_G26 = PRICE / MID["2026"]
PE_G27 = PRICE / MID["2027"]
PE_C27 = PRICE / CONS_EPS27
PE_E28 = PRICE / E28
UP_BASE = BASE_VALUE / PRICE - 1
LONG_BELOW = BASE_VALUE / 1.15
SHORT_ABOVE = BASE_VALUE / 0.75
EPS28_FOR_LONG = PRICE * 1.15 / BASE_PE
PE_FOR_LONG = PRICE * 1.15 / E28
OFF_HIGH = PRICE / HI_CLOSE - 1
YTD = PRICE / PX_DEC25 - 1
OFFER_MOVE = PX_OFFER_DAY / PX_OFFER_PRE - 1
Q2_MOVE = PX_Q2_DAY / PX_Q2_PRE - 1
OCT_MOVE = PRICE / 99.26 - 1     # from the 30 Sep 2026 close
DIV_YIELD = DIV_Q * 4 / PRICE
EPS_CAGR = (MID["2030"] / ADJ_EPS["2025A"]) ** (1 / 5) - 1
RB_CAGR = (RATE_BASE["2030E"] / RATE_BASE["2025E"]) ** (1 / 5) - 1
PEER_MED = sorted(p[2] for p in PEERS if p[5] == "peer")[len([p for p in PEERS if p[5] == "peer"]) // 2]

# ---- Price, month-end close (Yahoo Finance ETR, split-adjusted, read 2 Nov 2026) ----
PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24",
             "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
             "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26",
             "30 Oct 26"]
PX = [49.88, 50.78, 52.84, 53.33, 56.24, 53.50, 57.99, 60.35, 65.81, 77.39, 78.08, 75.82, 81.08, 87.31, 85.49, 83.17,
      83.28, 83.12, 90.43, 88.09, 93.19, 96.09, 97.52, 92.43, 95.89, 107.11, 112.36, 117.91, 109.05, 114.86, 107.62,
      106.31, 99.26, 110.11]

REVISIT_IF = ("A price below US$106.57, where my base value would sit 15 per cent above it, or a 2028 adjusted "
              "earnings outlook raised to a midpoint of US$5.90 or more once the second Meta agreement is approved.")
WRONG_IF = ("The shares close above US$135 or below US$90 in October 2027, or 2026 adjusted earnings per share land below "
            "the US$4.35 bottom of Entergy's narrowed guide, or the Louisiana commission rejects the second Meta agreement.")

if __name__ == "__main__":
    print(f"Q3 25 {Q_EPS[2]} H1 26 {H1_26:.2f} mids {MID}")
    print(f"shares {SHARES_OUT:.2f} mcap {MCAP:.2f} netdebt {NET_DEBT:.0f} EV {EV:.1f}")
    print(f"PE g26 {PE_G26:.1f} g27 {PE_G27:.1f} c27 {PE_C27:.1f} e28 {PE_E28:.1f}; eps cagr {EPS_CAGR:.1%} rb cagr {RB_CAGR:.1%}")
    print(f"base value {BASE_VALUE:.2f} {UP_BASE:+.1%}; long below {LONG_BELOW:.2f} short above {SHORT_ABOVE:.2f}; eps for long {EPS28_FOR_LONG:.2f} pe for long {PE_FOR_LONG:.2f}")
    for x in SC:
        print(x["name"], x["e28"], x["mult"], round(x["value"], 2), f"{x['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED / PRICE - 1:+.1%}")
    grid = [[e * m for m in SENS_PE] for e in SENS_EPS]
    print("grid", [[round(v, 2) for v in r] for r in grid])
    print("above", sum(v > PRICE for r in grid for v in r), "15%", sum(v >= PRICE * 1.15 for r in grid for v in r),
          "-25%", sum(v <= PRICE * 0.75 for r in grid for v in r))
    print(f"off high {OFF_HIGH:.1%} ytd {YTD:.1%} offer {OFFER_MOVE:+.1%} q2 {Q2_MOVE:+.1%} oct {OCT_MOVE:+.1%} div {DIV_YIELD:.2%}")
    print(f"capex total {CAPEX_TOTAL} meta1 {META1_TOTAL:.0f} meta2 {META2_TOTAL:.0f} share {META_SHARE:.1%}; meta2 NI {META2_NI:.0f} eps {META2_EPS:.2f} vs 2030 mid {MID['2030']}")
    print(f"cust adv {CUST_ADV_DEC25:.0f} -> {CUST_ADV_JUN26:.0f}; peer median {PEER_MED}; premium {FWD_PE_SA - PEER_MED:.2f}")
    print(f"MW per $: meta2 per kW {META2_PLANTS*1000/META2_MW:.0f}; ff per kW {(FF_COST+W5_COST)*1000/META1_MW:.0f}")
