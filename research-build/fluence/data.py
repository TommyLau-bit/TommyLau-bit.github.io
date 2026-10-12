"""Fluence Energy (Nasdaq: FLNC) initiation, 12 Oct 2026. Single source of figures for charts, note and model.

Sources (EDGAR CIK 1868941):
- Quarterly results releases, Exhibit 99.1 to Form 8-K: 1Q FY25 (10 Feb 2025), 2Q FY25 (7 May 2025), 3Q FY25 (11 Aug 2025),
  4Q and full FY25 (24 Nov 2025, with the first FY26 guide), 1Q FY26 (4 Feb 2026), 2Q FY26 (6 May 2026),
  3Q FY26 (5 Aug 2026, first FY26 cut).
- Form 8-K of 16 Sep 2026, Exhibit 99.1: revised FY26 guide (revenue about US$2.4bn, adjusted EBITDA loss about US$200m).
- Form 10-Q for the quarter to 30 Jun 2026 (filed 5 Aug 2026): balance sheet, shares (cover, 31 Jul 2026), convertible notes
  (Note 12), backlog (RPO), key operating metrics, revenue by region, liquidated damages, credit agreement covenants.
- Form 8-K of 15 May 2026 (AES redemption) and 10-Q Note 1 (secondary offering); Form 8-K of 9 Oct 2026 (officer separation).
- Third fiscal quarter 2026 earnings call, 6 Aug 2026 (transcript published by The Motley Fool, 12 Aug 2026): Houston
  capacity, generators, full production timing, FY27 backlog scheduled, data centre pipeline.
- 16 Sep 2026 call: transcript not accessible; unit rates and shares of the cut from trade press (Latitude Media, 21 Sep 2026;
  mgrid.org, 18 Sep 2026) and the Quartr event summary. Labelled as reported, not verified against the replay.
Prices: Nasdaq.com historical data (Yahoo Finance chart API refused requests with "Too Many Requests" on 12 Oct 2026),
retrieved 12 Oct 2026. Consensus and peer multiples: stockanalysis.com (S&P Global data), retrieved 12 Oct 2026. The forecast page
showed 'last updated 23 Sep 2026' on my retrieval; the fact-check saw it dated 7 Oct 2026. Re-checked 12 Oct 2026: FY26 revenue
US$2.40bn, FY27 US$3.25bn, FY27 EPS -0.27, FY26 FCF -431.93m, 23 analysts, average target US$10, median 8.50, range 3 to 23,
all unchanged. Published text cites the retrieval date only.
Class action: Hatweek v. Fluence Energy, No. 1:26-cv-08475 (S.D.N.Y.), filed 28 Sep 2026; class period 24 Nov 2025 to 16 Sep 2026;
lead plaintiff deadline 27 Nov 2026 (Kaplan Fox case page; Kessler Topaz on Business Wire, 1 Oct 2026). Everything marked MINE is my own estimate. Fiscal year ends 30 September. US$ million unless stated.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-12"
COMPANY = "Fluence"
SLUG = "fluence"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/fluence"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Tommy Lau's call, 12 Oct 2026: NO CALL, medium conviction. ----
CALL = dict(
    banner="NO CALL",
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Nasdaq.com historical data, retrieved 12 Oct 2026) ----
PRICE = 7.43                # Nasdaq close, 9 Oct 2026
PRICE_DATE = "9 October 2026"
HI_CLOSE = 32.23            # highest close, 3 Feb 2026
HI_INTRA = 33.51            # intraday high, 30 Jan 2026
LO_CLOSE = 7.27             # lowest close in 52 weeks, 22 Sep 2026
LO_INTRA = 7.01             # intraday low in 52 weeks, 17 Sep 2026
PX_DEC25 = 19.78            # close, 31 Dec 2025
# results-day moves, close to close (release after the close, reaction the next session)
MOVES = [  # date of reaction, what, close before, close on the day
    ("25 Nov 2025", "FY25 results; FY26 guide of US$3.2 to 3.6bn", 15.80, 16.77),
    ("5 Feb 2026", "1Q FY26 results; gross margin 4.9%", 28.99, 18.95),
    ("7 May 2026", "2Q FY26 results; two hyperscaler supply agreements", 13.56, 18.97),
    ("6 Aug 2026", "3Q FY26 results; first cut, to US$2.9 to 3.1bn", 14.23, 13.21),
    ("17 Sep 2026", "Second cut, to about US$2.4bn; Houston named", 9.05, 7.66),
]

# ---- Shares and balance sheet ----
SH_A = 143.163588           # m Class A, 31 Jul 2026 (10-Q cover)
SH_B1 = 41.432781           # m Class B-1 (AES Grid Stability), exchangeable one for one
SHARES = SH_A + SH_B1       # economic shares
CASH_JUN = 364.958          # cash, cash equivalents and restricted cash, 30 Jun 2026 (339.328 + 25.630)
CONVERT = 400.0             # 2.25% convertible senior notes due June 2030, principal; conversion price about US$21.35
CONV_PRICE = 21.35
LIQ_JUN = 863.0             # total liquidity, 30 Jun 2026 (3Q FY26 release)
BACKLOG_FY27 = 2200.0       # backlog scheduled for FY27 revenue, 3Q FY26 call (6 Aug 2026), before the September cut
Q4_BURN = 130.0             # MINE: cash used in the September 2026 quarter, not yet reported (see note)
FCF_9M = -299.026           # free cash flow, nine months to 30 Jun 2026 (company definition)
FCF_CONS_FY26 = -431.93     # stockanalysis.com (S&P Global) FY26 free cash flow forecast; cross-check for Q4_BURN
SHORT_PCT = 15.10           # short interest, % of shares outstanding (stockanalysis.com)
SELLABLE = 94.666665        # m Class A shares selling stockholders may still sell under the May 2026 shelf

# ---- Quarterly results (US$m) ----
Q = ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26"]
QL = ["Dec 24", "Mar 25", "Jun 25", "Sep 25", "Dec 25", "Mar 26", "Jun 26"]
Q_REV = [186.788, 431.618, 602.533, 1041.891, 475.234, 464.891, 649.848]
Q_GP = [21.201, 42.582, 89.099, 142.903, 23.049, 46.630, 33.241]
Q_AGM = [12.5, 10.4, 15.4, 14.3, 5.6, 11.1, 5.9]          # adjusted gross margin, %, as reported
Q_EBITDA = [-49.676, -30.411, 27.355, 72.187, -52.058, -9.442, -29.296]
BACKLOG = [5.1, 4.9, 4.9, 5.3, 5.5, 5.6, 6.4]              # US$bn at quarter end, as reported
REV_9M = 1589.973
AGP_9M = 116.772
EBITDA_9M = -90.796
AMERICAS_9M = 890.926       # revenue by customer location, nine months to 30 Jun 2026 (10-Q)
GW_ORD_9M, GW_ORD_9M_PY = 4.2, 1.9                          # storage GW contracted, nine months (10-Q)
PIPE_GWH, PIPE_GWH_PY = 163.7, 122.0                        # storage pipeline, 30 Jun 2026 vs 30 Sep 2025
DC_GWH = 16.0                                               # data centre pipeline, 3Q FY26 call

# ---- Annual reported (fiscal years to 30 September) ----
YEARS_H = ["FY24A", "FY25A"]
REV_H = [2698.562, 2262.830]
AGP_H = [347.856, 309.538]
EBITDA_H = [78.106, 19.455]
FCF_H = [71.570, -160.422]

# ---- Guidance ----
G26_NOV = dict(rev_lo=3200, rev_hi=3600, e_lo=40, e_hi=60)      # 24 Nov 2025
G26_AUG = dict(rev_lo=2900, rev_hi=3100, e_lo=-30, e_hi=10)     # 5 Aug 2026
G26 = dict(rev=2400, ebitda=-200)                               # 16 Sep 2026

# ---- Consensus (stockanalysis.com, S&P Global, retrieved and re-checked 12 Oct 2026) ----
CONS_REV_26 = 2400.0
CONS_REV_27 = 3250.0
CONS_EPS_27 = -0.27
CONS_TP = 10.0              # average target, 23 analysts; median 8.50, low 3, high 23
CONS_TP_MED, CONS_TP_LO, CONS_TP_HI, CONS_N = 8.50, 3.0, 23.0, 23

# ---- Peers (stockanalysis.com statistics pages, retrieved 12 Oct 2026; trailing EV/sales and EV/EBITDA) ----
PEERS = [  # company, ticker, EV/sales, EV/EBITDA, what they make
    ("Fluence", "Nasdaq: FLNC", 0.55, None, "Grid battery systems, services and control software (integrator)"),
    ("Sungrow", "SZSE: 300274", 1.84, 10.04, "Inverters and grid battery systems"),
    ("Nextracker", "Nasdaq: NXT", 3.28, 15.88, "Solar trackers"),
    ("Shoals", "Nasdaq: SHLS", 2.87, 16.79, "Electrical balance of system for solar and storage"),
    ("Array Technologies", "Nasdaq: ARRY", 0.85, 8.48, "Solar trackers"),
    ("Eos Energy", "Nasdaq: EOSE", 5.85, None, "Zinc-based long-duration batteries"),
]

# ---- MY assumptions ----
REV26 = G26["rev"]
G27, G28 = 0.25, 0.20       # revenue growth
AGM27, AGM28 = 0.105, 0.13  # adjusted gross margin
OPX27, OPX28 = 295.0, 320.0 # net operating costs: adjusted gross profit less adjusted EBITDA
BASE_MULT = 0.45            # EV / FY28 revenue, twelve months out
SCEN = [  # name, g27, g28, adjusted gross margin FY28, EV/sales multiple, prob
    ("Bear", 0.10, 0.10, 0.12, 0.25, 0.25),
    ("Base", G27, G28, AGM28, BASE_MULT, 0.50),
    ("Bull", 0.35, 0.30, 0.145, 0.70, 0.25),
]
CASE = "Hatweek v. Fluence Energy, No. 1:26-cv-08475 (S.D.N.Y.)"
CASE_FILED = "28 September 2026"
LEAD_PLAINTIFF = "27 November 2026"
SENS_REV = [3000.0, None, 4200.0]   # middle row = model FY28E
SENS_MULT = [0.35, 0.45, 0.55]

# ---- Derived ----
import statistics as _st
PEERS_EB = [p for p in PEERS[1:] if p[3] is not None]   # peers with positive EBITDA (excludes Eos Energy)
PEER_MED_S = _st.median([p[2] for p in PEERS_EB])
PEER_MED_EB = _st.median([p[3] for p in PEERS_EB])
OPX_H = [a - e for a, e in zip(AGP_H, EBITDA_H)]
OPX_9M = AGP_9M - EBITDA_9M
NETDEBT_JUN = CONVERT - CASH_JUN
NETDEBT = NETDEBT_JUN + Q4_BURN
MCAP = PRICE * SHARES
EV = MCAP + NETDEBT
REV27 = REV26 * (1 + G27)
REV28 = REV27 * (1 + G28)
EBITDA27 = REV27 * AGM27 - OPX27
EBITDA28 = REV28 * AGM28 - OPX28
SENS_REV[1] = REV28


def project(g27, g28):
    r27 = REV26 * (1 + g27)
    return r27, r27 * (1 + g28)


def value(rev28, mult):
    return (rev28 * mult - NETDEBT) / SHARES


RV28 = [project(s[1], s[2])[1] for s in SCEN]
EB28 = [r * s[3] - OPX28 for r, s in zip(RV28, SCEN)]
VALS = [value(r, s[4]) for r, s in zip(RV28, SCEN)]
EVEB = [r * s[4] / e for r, s, e in zip(RV28, SCEN, EB28)]
WEIGHTED = sum(v * s[5] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75
NEED_REV28 = EV / BASE_MULT
EV_S26 = EV / REV26
EV_S27C = EV / CONS_REV_27
EV_S28 = EV / REV28
EV_EB28 = EV / EBITDA28
BASE_EVEB = REV28 * BASE_MULT / EBITDA28
OFF_HIGH = PRICE / HI_CLOSE - 1
FROM_DEC25 = PRICE / PX_DEC25 - 1
GUIDE_CUT = 1 - G26["rev"] / ((G26_NOV["rev_lo"] + G26_NOV["rev_hi"]) / 2)
Q_GM = [g / r for g, r in zip(Q_GP, Q_REV)]
AMERICAS_SHARE = AMERICAS_9M / REV_9M
Q4_REV_IMPLIED = G26["rev"] - REV_9M
Q4_EBITDA_IMPLIED = G26["ebitda"] - EBITDA_9M
FCF_CONS_Q4 = FCF_CONS_FY26 - FCF_9M

# ---- Price, month-end close (Nasdaq.com historical data, retrieved 12 Oct 2026) ----
PX_LABELS = ["Sep 23", "Oct 23", "Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24",
             "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25",
             "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26",
             "Jun 26", "Jul 26", "Aug 26", "Sep 26", "9 Oct 26"]
PX = [22.99, 17.32, 25.08, 23.85, 19.87, 15.29, 17.34, 17.84, 25.13, 17.34, 16.38, 18.37, 22.71, 21.75, 18.81, 15.88, 13.01,
      5.72, 4.85, 4.09, 4.70, 6.71, 8.12, 7.40, 10.80, 21.00, 19.64, 19.78, 30.77, 15.54, 13.76, 12.18, 18.88, 19.88, 13.93,
      10.81, 7.68, 7.43]

# ---- The draft view's tests ----
REVISIT_IF = ("A price below about US$6.85, where my base value would sit 15 per cent above it, or Fluence's first quarterly "
              "American production figures, due with its fiscal 2026 results, showing Houston at or near its planned 11 units a "
              "day alongside a fiscal 2027 plan of at least US$3.0 billion of revenue.")
WRONG_IF = ("The shares close above US$11.00 or below US$4.50 in October 2027, or the fiscal 2027 plan Fluence publishes "
            "with its fiscal 2026 results puts revenue below US$2.6 billion or above US$3.5 billion.")

if __name__ == "__main__":
    print(f"shares {SHARES:.3f} mcap {MCAP:.1f} netdebt jun {NETDEBT_JUN:.2f} sep(est) {NETDEBT:.2f} EV {EV:.1f}")
    print(f"FY27 rev {REV27:.0f} ebitda {EBITDA27:.1f} ({EBITDA27/REV27:.1%}); FY28 rev {REV28:.0f} ebitda {EBITDA28:.1f} ({EBITDA28/REV28:.1%})")
    for s, v, e, r, x in zip(SCEN, VALS, EB28, RV28, EVEB):
        print(s[0], round(r), round(e, 1), f"{e/r:.1%}", round(v, 2), f"{v / PRICE - 1:+.1%}", f"EV/EBITDA {x:.1f}")
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.2f} short {REVISIT_SHORT:.2f}")
    grid = [[round(value(r, m), 2) for m in SENS_MULT] for r in SENS_REV]
    print("grid", grid, "above", sum(v > PRICE for row in grid for v in row), "15%+", sum(v >= PRICE * 1.15 for row in grid for v in row))
    print(f"EV/S 26 {EV_S26:.2f} 27cons {EV_S27C:.2f} 28 {EV_S28:.2f}; EV/EBITDA28 {EV_EB28:.1f}; base EV/EBITDA {BASE_EVEB:.1f}; need rev28 {NEED_REV28:.0f}")
    print(f"opx hist {[round(x,1) for x in OPX_H]} 9M {OPX_9M:.1f} ann {OPX_9M/0.75:.1f}; Q4 rev {Q4_REV_IMPLIED:.0f} ebitda {Q4_EBITDA_IMPLIED:.0f}; cons Q4 FCF {FCF_CONS_Q4:.0f}")
    print(f"off high {OFF_HIGH:.1%} from dec {FROM_DEC25:.1%} guide cut {GUIDE_CUT:.1%} americas {AMERICAS_SHARE:.1%}")
    print("moves", [(m[0], f"{m[3]/m[2]-1:+.1%}") for m in MOVES])
    print("Q GM", [f"{x:.1%}" for x in Q_GM])
    import statistics; print("peer median EV/S", statistics.median([p[2] for p in PEERS[1:]]), "EV/EBITDA", statistics.median([p[3] for p in PEERS[1:] if p[3]]))
