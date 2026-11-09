"""SpaceX (Space Exploration Technologies Corp., Nasdaq: SPCX) initiation, 2 Nov 2026. Single source of figures.

Sources (SEC EDGAR, CIK 1181412, unless stated):
- Final prospectus, Form 424B4, 12 Jun 2026: IPO price US$135.00, 555,555,555 Class A shares; 2023 to 2025 and Q1 2026
  results and segment data; lock-up schedule (pp. 272 to 273); orbital AI compute disclosure (100 kW per metric ton,
  "as early as 2028", mass "continue to be refined"); TAM; controlled company (Musk about 82.4% of votes).
- Form 8-K, Exhibit 99.1, 4 Aug 2026 (Q2 2026 results) and 20 Oct 2026 (Q3 2026 results): segment revenue, income from
  operations, Segment Adjusted EBITDA, capex, launches, mass to orbit, launch services revenue, Starlink subscribers and
  ARPU, nameplate compute, Cursor deal, consolidated statements.
- Form 10-Q for the quarter to 30 Sep 2026, filed 22 Oct 2026: shares outstanding at 15 Oct 2026, backlog US$62,959m,
  customer concentration (Customer B 34.5% of Q3 revenue, SI segment), Tesla special committee, key metrics. No mention of
  orbital compute.
- Form 8-K, 14 Aug 2026 (Cursor merger closed, US$60.0bn implied equity value); 8-K, 23 and 26 Jun 2026 (US$25bn senior
  notes); 8-K, 26 Oct 2026 (Apollo GPU finance lease commitment, about US$40bn of principal).
- Q3 2026 webcast, 20 Oct 2026 (SpaceX edited transcript, ir.spacex.com, SpaceX-Third-Quarter-2026-Webcast-Transcript.pdf):
  Q1 2027 revenue guide US$33bn to 37bn; Q4 capex US$35bn to 40bn; Gwynne Shotwell: "We'll attempt an on-orbit refueling
  early next year, and we'll begin flying Mobile V2 and Starmind satellites in 2027." No Q4 results date given.
- SpaceX Starmind page, spacex.com/spacexsi/starmind, read 2 Nov 2026: AI1 compute payload up to 250 kW peak / 175 kW
  average, vehicle efficiency "75 kW / ton" (page does not say compute or solar, or which ton), deployable liquid radiator 160 m2, solar array 210 kW at 250 W/m2, Gigasat
  factory, "thousands of AI satellites starting as soon as late 2027".
Prices: Yahoo Finance SPCX history pages (daily and weekly), read 2 Nov 2026 through a page fetch because the chart API
answered "Too Many Requests"; cross-checked against stockanalysis.com daily history. Consensus: Yahoo Finance analysis page,
read 2 Nov 2026. Peer multiples: stockanalysis.com statistics pages, 2 Nov 2026 (prices at the 30 Oct close).
Everything marked MINE is my own estimate. US$ million unless stated.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "SpaceX"
SLUG = "spacex"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/spacex"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view; Tommy decides. Rebuild = edit this dict only. ----
CALL = dict(
    banner="NO CALL",
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (Yahoo Finance SPCX, read 2 Nov 2026) ----
PRICE = 134.72                # Nasdaq close, 30 Oct 2026 (latest close)
PRICE_DATE = "30 October 2026"
IPO_PRICE = 135.00            # 424B4, 12 Jun 2026
DAY1_CLOSE = 160.95           # first close, 12 Jun 2026
HI_CLOSE, HI_CLOSE_DATE = 211.39, "16 June 2026"
HI_INTRA, HI_INTRA_DATE = 225.64, "16 June 2026"
LO_CLOSE, LO_CLOSE_DATE = 108.27, "5 August 2026"
LO_INTRA, LO_INTRA_DATE = 104.83, "3 August 2026"
PX_Q3_PRE, PX_Q3_DAY = 147.79, 159.31     # closes 20 Oct (results after the close) and 21 Oct 2026
PX_LABELS = ["12 Jun", "18 Jun", "26 Jun", "2 Jul", "10 Jul", "17 Jul", "24 Jul", "31 Jul", "7 Aug", "14 Aug", "21 Aug",
             "28 Aug", "4 Sep", "11 Sep", "18 Sep", "25 Sep", "2 Oct", "9 Oct", "16 Oct", "23 Oct", "30 Oct"]
PX = [160.95, 185.00, 153.23, 162.00, 145.30, 123.99, 115.07, 108.37, 133.11, 140.00, 136.97,
      141.50, 147.95, 151.21, 152.71, 148.68, 158.96, 162.57, 146.03, 147.49, 134.72]   # last close of each week

# ---- Shares and balance sheet ----
SHARES_A = 8246.541218        # m, Class A, 15 Oct 2026 (10-Q cover)
SHARES_B = 5334.522491        # m, Class B, 15 Oct 2026
SHARES = SHARES_A + SHARES_B
CASH = 51294.0                # cash and equivalents, 30 Sep 2026
SECS = 38561.0                # marketable securities, 30 Sep 2026
DEBT_CUR = 2698.0             # debt and finance leases, current
DEBT_LT = 36146.0             # debt and finance leases, non-current
BACKLOG = 62959.0             # 30 Sep 2026, 67% within one year
CUST_B_Q3 = 0.345             # Customer B share of Q3 2026 revenue (SI segment)
CUST_A_Q3 = 0.166
NAMEPLATE_GW = {"Q3 25": 0.6, "Q2 26": 1.4, "Q3 26": 1.7}
NAMEPLATE_END26 = (2.5, 3.0)  # Johnsen, Q3 call
GW_END27 = 13.0               # Musk, Q3 call: "surprised if we brought on less than 13 gigawatts ... by the end of next year"
Q4_CAPEX = (35000.0, 40000.0)
Q1_27_REV = (33000.0, 37000.0)
APOLLO_LEASE = 40000.0

# ---- Segments: annual (424B4) ----
SEGS = ["Space", "Connectivity", "SI"]
SEG_NAMES = {"Space": "Space (launch)", "Connectivity": "Connectivity (Starlink)", "SI": "Super Intelligence (SI)"}
REV_24 = {"Space": 3796.0, "Connectivity": 7599.0, "SI": 2620.0}     # derived from 2025 and the 2025 increases (424B4 MD&A)
REV_25 = {"Space": 4086.0, "Connectivity": 11387.0, "SI": 3201.0}
EBITDA_24 = {"Space": 1154.0, "Connectivity": 3849.0, "SI": 347.0}
EBITDA_25 = {"Space": 653.0, "Connectivity": 7168.0, "SI": -1237.0}
CAPEX_25 = {"Space": 3832.0, "Connectivity": 4178.0, "SI": 12727.0}
REV_TOT_24, REV_TOT_25 = 14015.0, 18674.0
MASS_25 = 2213.0              # t to orbit, 2025
LAUNCHES_25 = 170

# ---- Segments: quarters (8-K Exhibit 99.1, 4 Aug and 20 Oct 2026; 424B4 for Q1 2026) ----
QL = ["Q3 25", "Q1 26", "Q2 26", "Q3 26"]
QREV = {"Space": [1666.0, 619.0, 962.0, 1767.0], "Connectivity": [3097.0, 3257.0, 4291.0, 5248.0],
        "SI": [813.0, 818.0, 2561.0, 7560.0]}
QEBITDA = {"Space": [674.0, -351.0, -205.0, 357.0], "Connectivity": [1923.0, 2087.0, 2597.0, 3499.0],
           "SI": [-428.0, -609.0, 1146.0, 4953.0]}
REV_9M26 = {"Space": 3348.0, "Connectivity": 12796.0, "SI": 10939.0}
EBITDA_9M26 = {"Space": -199.0, "Connectivity": 8183.0, "SI": 5490.0}
CAPEX_9M26 = {"Space": 3832.0, "Connectivity": 4242.0, "SI": 39995.0}
Q3_REV, Q3_NI, Q3_ADJ_EBITDA = 14575.0, 4404.0, 8809.0
SUBS_Q3, ARPU_Q3 = 13.6, 69
SUBS_Q3_25, ARPU_Q3_25 = 7.2, 83

# ---- Launch revenue per kilogram of customer payload (my arithmetic from the releases) ----
KG_LABELS = ["Q1 25", "Q2 25", "Q3 25", "Q1 26", "Q2 26", "Q3 26"]
LS_REV = [566.0, 490.0, 1000.0, 330.0, 648.0, 1130.0]      # launch services revenue; Q1 25 = H1 1,056 less Q2 490
CUST_T = [75.0, 88.0, 111.0, 45.0, 87.0, 119.0]            # customer payload, t; Q1 25 = H1 163 less Q2 88
LS_9M26, CUST_9M26 = 2108.0, 251.0
THRESHOLD_KG = 200.0          # Google's threshold, the claim's test
GOOGLE_KG = 3600.0

# ---- Orbital compute: what SpaceX has said ----
TARGET_KW_T = 100.0           # 424B4
AI1_KW_T = 75.0               # Starmind page, read 2 Nov 2026
AI1_KW_AVG, AI1_KW_PEAK = 175.0, 250.0
AI1_RAD_M2 = 160.0
AI1_SOLAR_KW, SOLAR_WM2 = 210.0, 250.0
ISS_KG_M2 = 14.0

# ---- Consensus (Yahoo Finance analysis page, read 2 Nov 2026) ----
CONS_REV_Q4 = 22920.0         # 25 analysts
CONS_REV_26 = 48930.0         # 35 analysts
CONS_REV_27 = 180370.0        # 37 analysts, range 71.75bn to 290.06bn
CONS_EPS_27 = 4.03            # 33 analysts, range 0.34 to 13.49
CONS_TP = 257.11              # stockanalysis.com, 39 analysts, low 70, high 800

# ---- Peers (stockanalysis.com, 2 Nov 2026; trailing multiples at the 30 Oct close) ----
PEERS = [  # company, ticker, EV US$bn, EV/EBITDA, EV/sales, what they do, group
    ("SpaceX", "SPCX", 1780.0, None, 55.52, "Launch, Starlink, AI compute and models", "self"),
    ("Oracle", "ORCL", 528.19, 15.34, 7.36, "Cloud and AI data centre capacity, software", "ai"),
    ("CoreWeave", "CRWV", 76.29, 20.14, 10.05, "Rents GPU computing capacity", "ai"),
    ("Nebius", "NBIS", 44.40, None, 32.77, "Rents GPU computing capacity", "ai"),
    ("T-Mobile US", "TMUS", 279.08, 7.89, 2.97, "Mobile and broadband network", "conn"),
    ("AST SpaceMobile", "ASTS", 16.65, None, 144.40, "Satellite to phone broadband (pre-revenue scale)", "conn"),
    ("Rocket Lab", "RKLB", 30.50, None, 39.65, "Small launch and spacecraft", "space"),
]

# ---- MY assumptions ----
Q4_26 = {"Space": (1400.0, 150.0), "Connectivity": (5800.0, 3900.0), "SI": (15000.0, 6750.0)}   # rev, EBITDA
R27 = {"Space": 6000.0, "Connectivity": 26000.0, "SI": 135000.0}     # 2027E revenue
M27 = {"Space": 0.10, "Connectivity": 0.68, "SI": 0.48}             # 2027E Segment Adjusted EBITDA margin
BASIS = {"Space": "rev", "Connectivity": "ebitda", "SI": "ebitda"}
MULT = {"Space": 15.0, "Connectivity": 25.0, "SI": 13.0}
OPTIONS = 100000.0            # MINE: everything not in the three segments today (Starship beyond launch, orbital compute,
                              # Starlink Mobile spectrum, Terafab), base case
SCEN = [  # name, revenue dict, margin dict, multiple dict, options, prob
    ("Bear", {"Space": 5000.0, "Connectivity": 24000.0, "SI": 90000.0}, {"Space": 0.0, "Connectivity": 0.65, "SI": 0.40},
     {"Space": 8.0, "Connectivity": 15.0, "SI": 8.0}, 0.0, 0.25),
    ("Base", R27, M27, MULT, OPTIONS, 0.50),
    ("Bull", {"Space": 7000.0, "Connectivity": 28000.0, "SI": 175000.0}, {"Space": 0.15, "Connectivity": 0.70, "SI": 0.55},
     {"Space": 25.0, "Connectivity": 35.0, "SI": 16.0}, 300000.0, 0.25),
]
SENS_SI = [52000.0, None, 78000.0]     # SI 2027E EBITDA; middle = base
SENS_MULT = [10.0, 13.0, 16.0]

# ---- Derived ----
NETCASH = CASH + SECS - DEBT_CUR - DEBT_LT
MCAP = PRICE * SHARES
EV_MKT = MCAP - NETCASH
FY26 = {k: (REV_9M26[k] + Q4_26[k][0], EBITDA_9M26[k] + Q4_26[k][1]) for k in SEGS}
REV_26E = sum(v[0] for v in FY26.values())
EBITDA_26E = sum(v[1] for v in FY26.values())
E27 = {k: R27[k] * M27[k] for k in SEGS}
REV_27E = sum(R27.values())
EBITDA_27E = sum(E27.values())


def seg_ev(rev, mar, mult):
    out = {}
    for k in SEGS:
        base = rev[k] if BASIS[k] == "rev" else rev[k] * mar[k]
        out[k] = base * mult[k]
    return out


def value(rev, mar, mult, options):
    return (sum(seg_ev(rev, mar, mult).values()) + options + NETCASH) / SHARES


SOTP = seg_ev(R27, M27, MULT)
TERR_EV = sum(SOTP.values())
BASE_EQ = TERR_EV + OPTIONS + NETCASH
BASE_VALUE = BASE_EQ / SHARES
TERR_VALUE = (TERR_EV + NETCASH) / SHARES
VALS = [value(s[1], s[2], s[3], s[4]) for s in SCEN]
WEIGHTED = sum(v * s[5] for v, s in zip(VALS, SCEN))
REVISIT_SHORT = BASE_VALUE / 0.75
REVISIT_LONG = BASE_VALUE / 1.15
SENS_SI[1] = E27["SI"]


def grid_value(si_ebitda, si_mult):
    other = SOTP["Space"] + SOTP["Connectivity"]
    return (other + si_ebitda * si_mult + OPTIONS + NETCASH) / SHARES


# What the price leaves above the three businesses
RESIDUAL = EV_MKT - TERR_EV
RESIDUAL_SHARE = RESIDUAL / EV_MKT
RESIDUAL_PS = RESIDUAL / SHARES
GAP_AFTER_OPTIONS = RESIDUAL - OPTIONS
SI_EV_PER_GW = SOTP["SI"] / GW_END27
RESIDUAL_GW = RESIDUAL / SI_EV_PER_GW
RESIDUAL_SATS = RESIDUAL_GW * 1e6 / AI1_KW_AVG
RESIDUAL_T_AI1 = RESIDUAL_GW * 1e6 / AI1_KW_T
RESIDUAL_T_TGT = RESIDUAL_GW * 1e6 / TARGET_KW_T
RESIDUAL_X_MASS25 = RESIDUAL_T_AI1 / MASS_25

# Market multiples
EV_REV27C = EV_MKT / CONS_REV_27
PE_27C = PRICE / CONS_EPS_27
EV_EBITDA27M = EV_MKT / EBITDA_27E
VS_IPO = PRICE / IPO_PRICE - 1
OFF_HI = PRICE / HI_CLOSE - 1
Q3_MOVE = PX_Q3_DAY / PX_Q3_PRE - 1

# Physical arithmetic on AI1
AI1_MASS_T = AI1_KW_AVG / AI1_KW_T
AI1_KG_PER_KW = 1000 / AI1_KW_T
AI1_RAD_FLUX = AI1_KW_AVG * 1000 / AI1_RAD_M2
AI1_RAD_ISS_T = AI1_RAD_M2 * ISS_KG_M2 / 1000
AI1_SOLAR_M2 = AI1_SOLAR_KW * 1000 / SOLAR_WM2
AI1_GAP = 1 - AI1_KW_T / TARGET_KW_T
KG_PRICE = [r / t for r, t in zip(LS_REV, CUST_T)]
KG_9M26 = LS_9M26 / CUST_9M26 * 1000 / 1000   # US$m per t = US$ per kg x 1,000 / 1,000
KG_9M26_USD = LS_9M26 * 1e6 / (CUST_9M26 * 1000)
KG_PRICE_USD = [r * 1e6 / (t * 1000) for r, t in zip(LS_REV, CUST_T)]
KG_X_THRESHOLD = KG_9M26_USD / THRESHOLD_KG
MASS_100GW_T = 1_000_000.0
MASS_X = MASS_100GW_T / MASS_25

# ---- The call's tests ----
REVISIT_IF = ("A price above about US$150, where my base value would sit 25 per cent below it, or below about US$98, where it "
              "would sit 15 per cent above it; or SpaceX disclosing an AI compute satellite weighed in service at 100 kilowatts "
              "or more per tonne launched, which would break my piece's claim.")
WRONG_IF = ("The shares close above US$175 or below US$90 on 29 October 2027, or SpaceX's reported 2027 revenue lands below "
            "US$130 billion or above US$260 billion, either of which would put my base value outside the no-call band at today's price.")

if __name__ == "__main__":
    print(f"shares {SHARES:,.3f}m mcap {MCAP/1000:,.1f}bn netcash {NETCASH:,.0f} EV {EV_MKT/1000:,.1f}bn")
    print("FY26E", {k: (round(a), round(b)) for k, (a, b) in FY26.items()}, round(REV_26E), round(EBITDA_26E))
    print("E27", {k: round(v) for k, v in E27.items()}, "rev27", REV_27E, "ebitda27", round(EBITDA_27E))
    print("SOTP", {k: round(v) for k, v in SOTP.items()}, "terr", round(TERR_EV), "eq", round(BASE_EQ))
    print(f"base {BASE_VALUE:.2f} {BASE_VALUE/PRICE-1:+.1%}; terrestrial only {TERR_VALUE:.2f} {TERR_VALUE/PRICE-1:+.1%}")
    for s, v in zip(SCEN, VALS):
        print(s[0], round(v, 2), f"{v/PRICE-1:+.1%}")
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED/PRICE-1:+.1%}; revisit short {REVISIT_SHORT:.1f} long {REVISIT_LONG:.1f}")
    g = [[grid_value(e, m) for m in SENS_MULT] for e in SENS_SI]
    print("grid", [[round(v, 1) for v in r] for r in g], "above price", sum(v > PRICE for r in g for v in r),
          "<= -25%", sum(v <= PRICE * 0.75 for r in g for v in r), ">= +15%", sum(v >= PRICE * 1.15 for r in g for v in r))
    print(f"residual {RESIDUAL/1000:.1f}bn {RESIDUAL_SHARE:.1%} ${RESIDUAL_PS:.2f}/sh; gap after options {GAP_AFTER_OPTIONS/1000:.1f}bn")
    print(f"SI EV/GW {SI_EV_PER_GW/1000:.1f}bn; residual GW {RESIDUAL_GW:.2f}; sats {RESIDUAL_SATS:,.0f}; t AI1 {RESIDUAL_T_AI1:,.0f} "
          f"t tgt {RESIDUAL_T_TGT:,.0f}; x2025 mass {RESIDUAL_X_MASS25:.1f}")
    print(f"EV/rev27 cons {EV_REV27C:.1f} PE27 cons {PE_27C:.1f} EV/EBITDA27 mine {EV_EBITDA27M:.1f}")
    print(f"vs IPO {VS_IPO:+.1%} off high close {OFF_HI:+.1%} Q3 move {Q3_MOVE:+.1%}")
    print(f"AI1 mass {AI1_MASS_T:.2f}t {AI1_KG_PER_KW:.1f}kg/kW flux {AI1_RAD_FLUX:.0f} W/m2 ISS radiator {AI1_RAD_ISS_T:.2f}t "
          f"solar {AI1_SOLAR_M2:.0f} m2 gap {AI1_GAP:.0%}")
    print("kg price", [round(x) for x in KG_PRICE_USD], round(KG_9M26_USD), f"x{KG_X_THRESHOLD:.0f}", "mass x", round(MASS_X))
    print(f"Q3 SI margin {QEBITDA['SI'][3]/QREV['SI'][3]:.1%}; Q2 {QEBITDA['SI'][2]/QREV['SI'][2]:.1%}; conn Q3 {QEBITDA['Connectivity'][3]/QREV['Connectivity'][3]:.1%}")
