"""Constellation Energy Corporation (Nasdaq: CEG) initiation, drafted 30 Oct 2026. Single source of figures for charts,
note and model.

Fiscal year = calendar year. US$ million unless stated.
Sources (SEC EDGAR, Constellation CIK 1868275):
- Q2 2026 earnings release, Form 8-K Ex. 99.1, 6 Aug 2026 (ceg-20260806991.htm): Q2 adjusted EPS $2.55, guide raised to
  $11.50-12.50, FERC CIR waiver, NRC fuel licence amendment, Brazos Valley sale ($860m), 920 MW of new PPAs, balance sheet
  at 30 Jun 2026, nuclear output and capacity factor.
- Form 10-Q for the quarter to 30 Jun 2026, filed 6 Aug 2026: Note 3 (Crane CIRs: PJM Phase I study, contingent upgrades
  with in-service dates as late as Dec 2030; Eddystone 3 and 4 planned retirement 31 May 2025, energy-only under DOE
  orders; FERC granted the waiver in June 2026); Note 2 (Calpine: closed 7 Jan 2026, ~$21.8bn purchase price, 50m shares
  plus ~$4.5bn cash; ~23 GW after divestitures; PJM assets to LS Power, ~4.4 GW, $5.0bn); Note 13 (DOE $1.0bn loan
  guarantee for Crane, no borrowings); 354,307,379 shares outstanding at 31 Jul 2026; ~7.1m shares bought back in H1
  for ~$2.0bn, 1m more in July for ~$250m.
- Q1 2026 earnings release, Form 8-K Ex. 99.1, 11 May 2026: Q1 adjusted EPS $2.74; guide $11.00-12.00 affirmed.
- Q4 2025 earnings release, Form 8-K Ex. 99.1, 24 Feb 2026: 2025 adjusted EPS $9.39 (2024 $8.67), Q4 2025 $2.30.
- 2026 Business and Earnings Outlook, Form 8-K Ex. 99.1, 31 Mar 2026: Base EPS $6.65-6.75 (2026), $7.60-7.70 (2027),
  $11.40-11.90 (2029); Enhanced earnings ~40% of 2026, 35-40% of 2027, 30-35% of 2029; base EPS growth 20%+ 2026-29;
  1 GW nuclear PPA at $20-50/MWh premium = $0.40-1.00 of 2029 EPS; 147m MWh of nuclear output available to contract;
  Calpine gas assets ~$65bn at replacement cost, over 2x the $26.6bn enterprise value paid (company estimate).
- Form 8-K, 14 Jul 2026: PJM 2028/2029 capacity auction, 15,700 MW nuclear and 3,175 MW other cleared at $325/MW-day.
- Form 8-K/A, 20 Apr 2026: Calpine acquisition completed 7 Jan 2026. Form 8-K, 2 Jun 2026: 2m shares bought from the
  secondary offering for ~$558m.
- Constellation request for limited waiver, FERC docket ER26-2028-000, 31 Mar 2026 (accession 20260331-5562), with the
  Habtemichael affidavit: hundreds of miles of new 765 kV and 500 kV lines as contingent facilities; soonest full
  deliverability 31 Dec 2030 on the Phase I report; Eddystone 3 and 4 380 MW each; Crane physically able to generate in
  the second half of 2027 with NRC approvals expected in early 2027; maximum facility output 859 MW.
- FERC order of 1 Jun 2026 (accession 20260601-3068), as quoted by Utility Dive and the American Nuclear Society.
- Constellation and Google release, 6 Oct 2026: 890 MW of uprates at 11 units, 20-year PPA, first uprate by 2028,
  >$4.3bn investment; separate 15-year supply agreement for 2,700 MW (price not disclosed).
- Q3 2026 results: listed for 9 Nov 2026 on Constellation's investor events page (event page not readable; MarketBeat
  calls the date estimated). Treated as not confirmed.
Prices: Yahoo Finance history pages (CEG), read on 30 Oct 2026 (the chart API returned "Too Many Requests"); daily closes
for October 2026 cross-checked against stockanalysis.com. Consensus, targets and peer multiples: stockanalysis.com
(S&P Global data), retrieved 30 Oct 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-30"
COMPANY = "Constellation"
SLUG = "constellation"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/constellation"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call (Tommy Lau, 30 Oct 2026). Rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",     # Tommy Lau's call, 30 Oct 2026
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Yahoo Finance CEG, read 30 Oct 2026) ----
PRICE = 264.58              # Nasdaq close, Thursday 29 Oct 2026
PRICE_DATE = "29 October 2026"
HI_CLOSE = 403.95           # highest close, 15 Oct 2025
HI_INTRA = 412.70           # intraday high, also 15 Oct 2025
PX_DEC25 = 353.27           # close 31 Dec 2025
PX_OCT13, PX_OCT23 = 295.79, 253.45     # closes 13 and 23 Oct 2026
PX_GOOG_PRE, PX_GOOG_DAY = 267.62, 300.40   # closes 5 and 6 Oct 2026 (Google agreement, 6 Oct)
PX_Q1_PRE, PX_Q1_DAY = 303.63, 299.69   # closes 8 and 11 May 2026 (Q1 results 11 May)
PX_Q2_PRE, PX_Q2_DAY = 265.12, 261.10   # closes 5 and 6 Aug 2026 (Q2 results 6 Aug)
PX_JAN26 = 280.68          # close 30 Jan 2026 (month end); January fall -20.5%

# ---- Shares and balance sheet, 30 Jun 2026 (Q2 release and 10-Q) ----
SHARES_OUT = 354.31         # m, outstanding at 31 Jul 2026 (10-Q cover)
SHARES_DIL_Q2 = 360.0       # m, diluted, Q2 2026
CASH = 697.0
DEBT = 5226.0 + 363.0 + 19111.0     # short-term borrowings + LTD due within a year + LTD
NCI = 345.0
SALE_PROCEEDS = 5000.0 + 860.0      # PJM assets to LS Power + Brazos Valley, before closing adjustments and tax
DIV_Q = 0.4265

# ---- Earnings, as reported (adjusted operating EPS, US$) ----
ADJ_EPS = {"2024A": 8.67, "2025A": 9.39}
Q_LABELS = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_EPS = [2.14, 1.91, round(9.39 - 2.14 - 1.91 - 2.30, 2), 2.30, 2.74, 2.55]   # Q3 25 derived from the full year
H1_26 = 2.74 + 2.55
GUIDE26 = dict(lo=11.50, hi=12.50)          # raised 6 Aug 2026
GUIDE26_MAR = dict(lo=11.00, hi=12.00)      # initiated 31 Mar 2026 on 361m diluted shares

# ---- Constellation's own earnings framework (31 Mar 2026), midpoints ----
BASE = {"2026": 6.70, "2027": 7.65, "2029": 11.65}
ENH_SHARE_CO = {"2026": 0.40, "2027": (0.35, 0.40), "2029": (0.30, 0.35)}
PPA_SENS = (0.40, 1.00)     # 2029 EPS per 1 GW nuclear PPA at a $20-50/MWh premium to the PTC floor
AVAIL_TWH = 147             # m MWh of nuclear output available to contract
NUC_TWH_26 = 179            # m MWh expected nuclear output, 2026

# ---- Crane (piece and filings) ----
CRANE_MW = 835
CRANE_CAPEX = 1600.0        # US$m, Q3 2024 release
CIR_MW = 760                # Eddystone 3 and 4, 380 MW each
DOE_LOAN = 1000.0
CRANE_CF = 0.93             # MINE: capacity factor, near the fleet's 93-95%
CRANE_TWH = CRANE_MW * 8760 * CRANE_CF / 1e6
CRANE_PER_KW = CRANE_CAPEX * 1e6 / (CRANE_MW * 1e3)
MARG_TAX = 0.255            # marginal statutory rate, Q2 release
EPS_PER_10 = CRANE_TWH * 1e6 * 10 * (1 - MARG_TAX) / (SHARES_OUT * 1e6)   # EPS per $10/MWh of Crane margin
REPL_BN, CALPINE_EV = 65.0, 26.6   # replacement cost of the Calpine gas assets, and the enterprise value paid (31 Mar 2026 outlook)
REPL_MULT = REPL_BN / CALPINE_EV
GOOG_UPRATE_MW, GOOG_CAPEX = 890, 4300.0
GOOG_PER_KW = GOOG_CAPEX * 1e6 / (GOOG_UPRATE_MW * 1e3)
CAP_MW_NUC, CAP_MW_ALL, CAP_PRICE = 15700, 18875, 325.0     # PJM 2028/29
CAP_REV = CAP_MW_ALL * CAP_PRICE * 365 / 1e6                # US$m a year (derived)

# ---- MY estimates ----
Q3E, Q4E = 3.90, 2.91       # MINE: second half 2026
EPS26 = H1_26 + Q3E + Q4E
BASE28 = (BASE["2027"] * BASE["2029"]) ** 0.5   # MINE: geometric path between Constellation's 2027 and 2029 midpoints
ENH27, ENH28 = 0.375, 0.35  # MINE: midpoints of Constellation's own ranges for 2027 and between 2027 and 2029
E27 = BASE["2027"] / (1 - ENH27)
E28 = BASE28 / (1 - ENH28)
BASE_PE = 20.0

CONS_EPS26, CONS_EPS27 = 12.16, 13.32      # stockanalysis.com (S&P Global), checked 28 Oct 2026
CONS_REV26, CONS_REV27 = 35.78, 37.02
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 339.11, 25, 238.0, 399.0
FWD_PE_SA = 21.31
EV_EBITDA_SA = 14.81
Q3_CONS = 3.84              # MarketBeat, retrieved 30 Oct 2026

PEERS = [  # company, ticker, forward P/E, EV/EBITDA, what they run, group
    ("Constellation", "Nasdaq: CEG", 21.31, 14.81, "Largest US nuclear fleet (~22 GW), Calpine gas and geothermal, retail supply", "self"),
    ("Vistra", "NYSE: VST", 14.39, 10.14, "Nuclear (Comanche Peak and others), gas fleet in ERCOT and PJM, retail", "peer"),
    ("Talen Energy", "Nasdaq: TLN", 11.97, 44.76, "Susquehanna nuclear plant and gas plants in PJM", "peer"),
    ("NRG Energy", "NYSE: NRG", 9.57, 13.47, "Gas fleet in ERCOT and PJM, retail electricity and home services", "peer"),
]

# ---- Scenarios: name, 2028 base EPS, enhanced share, multiple, probability ----
SCEN = [
    ("Bear", 8.60, 0.30, 15, 0.25),
    ("Base", BASE28, ENH28, BASE_PE, 0.50),
    ("Bull", 9.94, 0.40, 23, 0.25),
]
SC = []
for s in SCEN:
    e = s[1] / (1 - s[2])
    SC.append(dict(name=s[0], base=s[1], enh=s[2], e28=e, mult=s[3], value=e * s[3], prob=s[4]))
WEIGHTED = sum(x["value"] * x["prob"] for x in SC)
BASE_VALUE = BASE_PE * E28
SENS_EPS = [12.50, E28, 16.50]
SENS_PE = [17, 20, 23]

# ---- Derived market figures ----
MCAP = PRICE * SHARES_OUT / 1000
NET_DEBT = DEBT - CASH
EV = MCAP + (NET_DEBT + NCI) / 1000
PE_G26 = PRICE / ((GUIDE26["lo"] + GUIDE26["hi"]) / 2)
PE_C27 = PRICE / CONS_EPS27
PE_E27 = PRICE / E27
PE_E28 = PRICE / E28
TTM_EPS = Q_EPS[2] + Q_EPS[3] + H1_26
PE_TTM = PRICE / TTM_EPS
OFF_HIGH = PRICE / HI_CLOSE - 1
YTD = PRICE / PX_DEC25 - 1
OCT_FALL = PX_OCT23 / PX_OCT13 - 1
GOOG_MOVE = PX_GOOG_DAY / PX_GOOG_PRE - 1
Q1_MOVE = PX_Q1_DAY / PX_Q1_PRE - 1
Q2_MOVE = PX_Q2_DAY / PX_Q2_PRE - 1
UP_BASE = BASE_VALUE / PRICE - 1
LONG_BELOW = BASE_VALUE / 1.15
SHORT_ABOVE = BASE_VALUE / 0.75
EPS28_FOR_LONG = PRICE * 1.15 / BASE_PE
CONS_GAP27 = CONS_EPS27 / E27 - 1
DIV_YIELD = DIV_Q * 4 / PRICE

# ---- Price, month-end close (Yahoo Finance CEG, read 30 Oct 2026) ----
PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24",
             "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
             "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26",
             "29 Oct 26"]
PX = [122.00, 168.45, 184.85, 185.94, 217.25, 200.27, 189.80, 196.70, 260.02, 262.96, 256.56, 223.71, 299.98, 250.54,
      201.63, 223.44, 306.15, 322.76, 347.84, 307.98, 329.07, 377.00, 364.36, 353.27, 280.68, 329.88, 279.25, 313.00,
      287.75, 248.37, 262.75, 274.77, 254.02, 264.58]

REVISIT_IF = ("A price below about US$253, where my base value would sit 15 per cent above it, or a 2027 "
              "adjusted operating earnings guide with a midpoint of US$13.00 or more, which would lift my 2028 estimate enough for a long.")
WRONG_IF = ("The shares close above US$330 or below US$200 in October 2027, or 2026 adjusted operating earnings land below "
            "the US$11.50 bottom of Constellation's raised guide, or Crane has not delivered power to the grid by the end of "
            "2027, the target Constellation still holds.")

if __name__ == "__main__":
    print(f"Q eps {Q_EPS} H1 {H1_26:.2f} EPS26 {EPS26:.2f} TTM {TTM_EPS:.2f} PE ttm {PE_TTM:.1f}")
    print(f"BASE28 {BASE28:.4f} E27 {E27:.4f} E28 {E28:.4f} base value {BASE_VALUE:.2f} {UP_BASE:+.2%}")
    print(f"long below {LONG_BELOW:.1f} short above {SHORT_ABOVE:.1f} eps28 for long {EPS28_FOR_LONG:.2f} cons gap27 {CONS_GAP27:+.1%}")
    for x in SC:
        print(x["name"], round(x["e28"], 2), x["mult"], round(x["value"], 1), f"{x['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}")
    grid = [[e * m for m in SENS_PE] for e in SENS_EPS]
    print("grid", [[round(v, 1) for v in r] for r in grid])
    print("above", sum(v > PRICE for r in grid for v in r), "15%", sum(v >= PRICE * 1.15 for r in grid for v in r),
          "-25%", sum(v <= PRICE * 0.75 for r in grid for v in r))
    print(f"mcap {MCAP:.2f} netdebt {NET_DEBT:.0f} EV {EV:.1f}; PE g26 {PE_G26:.1f} c27 {PE_C27:.1f} e27 {PE_E27:.1f} e28 {PE_E28:.1f}")
    print(f"off high {OFF_HIGH:.1%} ytd {YTD:.1%} oct {OCT_FALL:.1%} goog {GOOG_MOVE:+.1%} q1 {Q1_MOVE:+.1%} q2 {Q2_MOVE:+.1%} div {DIV_YIELD:.2%}")
    print(f"repl mult {REPL_MULT:.2f}"); print(f"crane TWh {CRANE_TWH:.2f} share {CRANE_TWH / NUC_TWH_26:.1%} per kW {CRANE_PER_KW:.0f} eps per $10 {EPS_PER_10:.3f}; goog per kW {GOOG_PER_KW:.0f}; cap rev {CAP_REV:.0f}")
    print(f"enh 26 {(EPS26 - BASE['2026']) / EPS26:.1%}; 2029 total implied {BASE['2029'] / 0.675:.2f}; base cagr {(BASE['2029'] / BASE['2026']) ** (1 / 3) - 1:.1%}")
    import statistics
    print("peer median fwd", statistics.median(p[2] for p in PEERS if p[5] == "peer"))
    print("end24 trailing", 223.71 / 8.67, "end25", 353.27 / 9.39)
