"""Ajinomoto Co., Inc. (Tokyo Stock Exchange Prime: 2802) initiation, draft of 7 Oct 2026. Single source of figures for
charts, note and model.

Fiscal years end 31 March. Ajinomoto's own labels are used throughout: FY2025 = the year to 31 March 2026, FY2026 = the
year to 31 March 2027, FY2027 = the year to 31 March 2028.

Sources (all Ajinomoto, ajinomoto.co.jp investor relations):
  Consolidated Financial Results (tanshin) for FY2025, 7 May 2026, and for Q1 FY2026, 6 Aug 2026: group P&L, balance
  sheet, shares, forecasts. "Consolidated Results" data sheets for FY2022 (11 May 2023), FY2023 (9 May 2024), FY2024
  (8 May 2025), H1 FY2025 (6 Nov 2025), 9M FY2025 (5 Feb 2026), FY2025 (7 May 2026) and Q1 FY2026 (6 Aug 2026): segment
  and business sales and business profit, including Functional Materials. "FY2026 Revised Forecast by Segment", 6 Aug 2026.
  Notice of Revision to Full-Year Forecast, 6 Aug 2026. FY2025 results presentation with script, 7 May 2026 (slides 25 to
  27, 38 and 39: ABF volume by application, Functional Materials margin wording, package sizes, Kani City, capital
  allocation, buybacks). Q1 FY2026 presentation, 6 Aug 2026 (slides 14 and 15: Functional Materials, Fine-Techno accounts
  and merger). ASV Report 2026 (ten-year summary, P/E at fiscal year ends). Buyback progress notices of 2 Jul and
  2 Oct 2026.
Prices: stockanalysis.com history for TYO:2802 (split-adjusted for the 2-for-1 split of 1 Apr 2025), retrieved 7 Oct 2026.
  (Yahoo Finance chart API refused requests with "Too Many Requests" on 7 Oct 2026.)
Consensus and peers: stockanalysis.com (S&P Global Market Intelligence) statistics and forecast pages, retrieved 7 Oct 2026.
Everything marked MINE is my own estimate. Yen billion unless stated; per-share in yen.
"""
import statistics

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-07"
DATE_LONG = "7 October 2026"
COMPANY = "Ajinomoto"
NAME = "Ajinomoto Co., Inc."
SLUG = "ajinomoto"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/ajinomoto"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",        # e.g. "INITIATE AT NO CALL" once Tommy decides
    direction="NO CALL",
    target=None,                    # yen per share; None for NO CALL
    conviction="Low",
    draft=False,
)

# ---- Market data (stockanalysis.com, retrieved 7 Oct 2026; Tokyo had closed for the day) ----
PRICE = 5346.0          # close, 7 Oct 2026
PRICE_DATE = "7 October 2026"
PRICE_DATE_ISO = "2026-10-07"
HI_CLOSE = 6175.0       # highest close of the past year, 1 Jul 2026
HI52 = 6340.0           # intraday high of the past year, 6 Jul 2026
LO_CLOSE = 3300.0       # lowest close of the past year, 9 Jan 2026
LO52 = 3270.0           # intraday low of the past year, 8 Jan 2026
PX_LIMIT = (4323.0, 3623.0)   # closes 6 and 7 Nov 2025, the day after H1 FY2025 results (limit down, ASV Report)
PX_PRE_RESULTS = 4958.0       # close 7 May 2026 (FY2025 results after the close)
PX_DEC25 = 3317.0       # close 30 Dec 2025
PX_MAR25 = 2958.5       # close 31 Mar 2025 (split-adjusted)
PX_LABELS = ['Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24', 'Sep 24',
             'Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25',
             'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26', '7 Oct 26']
PX = [2740, 2763, 2720, 3043.5, 2751.5, 2830, 2937.5, 2802.5, 2820.5, 3115.5, 2798.5, 2773,
      2952, 3141, 3226, 3122.5, 3002.5, 2958.5, 2916, 3612, 3909, 4005, 4009, 4246,
      4373, 3623, 3317, 3520, 4968, 4397, 5090, 5152, 5873, 4965, 5402, 5111, 5346]
# Month-end closes, split-adjusted; the last point is the 7 Oct 2026 close.

# Shares: 977,735,616 issued less 23,173,875 treasury at 30 Jun 2026 (Q1 tanshin) = 954.56m; less 3,636,800 bought
# from 1 Jul to 30 Sep 2026 (cumulative 15,588,400 at 30 Sep less 11,951,600 at 30 Jun, buyback notices). MY arithmetic.
SH_JUN = (977735616 - 23173875) / 1e6
SH_BOUGHT_Q2 = (15588400 - 11951600) / 1e6
SHARES = SH_JUN - SH_BOUGHT_Q2          # m, about 30 Sep 2026

# ---- Balance sheet, 30 Jun 2026 (Q1 FY2026 tanshin), yen billion ----
CASH = 196.979
DEBT = 7.069 + 140.000 + 29.991 + 4.048 + 174.531 + 206.280   # borrowings, commercial paper, bonds (excl. leases)
DEBT_INCL_LEASES = 623.7                 # "interest bearing debt" as Ajinomoto states it
NET_DEBT = DEBT - CASH                   # stockanalysis.com definition, used for peers too
NCI = 73.845                             # non-controlling interests, book value
EQUITY_PARENT = 774.552

# ---- Consensus (stockanalysis.com, S&P Global; forecast page last updated 7 Aug 2026) ----
CONS_EPS26 = 146.08     # FY2026 (to Mar 2027) EPS average
CONS_OP26 = 206.59      # FY2026 operating income average
CONS_REV26 = 1740.88
CONS_TP = 6321.0        # average analyst price target
GUIDE_EPS26 = 129.84    # Ajinomoto's revised forecast, 6 Aug 2026

# ---- History by business, yen billion (Consolidated Results data sheets) ----
# Functional Materials (electronic materials and others), a business inside the Healthcare and Others segment.
# Business profit bases differ: FY2021-22 on the FY2022 allocation, FY2023 on the FY2023 basis, FY2024-25 restated without
# shared companywide expenses (FY2025 basis).
FM_YEARS = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
FM_SALES_H = [60.5, 70.1, 60.8, 76.5, 100.7]
FM_BP_H = [28.9, 36.9, 27.6, 40.2, 54.6]
FMQ_L = ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26"]
FMQ_SALES = [21.5, 23.4, 28.9, 26.9, 33.1]
FMQ_BP = [10.8, 12.8, 16.5, 14.4, 19.1]
FT_SALES_25, FT_OP_25 = 98.383, 53.012   # Ajinomoto Fine-Techno, the subsidiary that makes ABF, FY2025

# Group by segment, FY2024 (restated, FY2025 basis), FY2025 actual, FY2026 revised forecast (6 Aug 2026), Q1 FY2025, Q1 FY2026
SEG_COLS = ["FY2024", "FY2025", "FY2026 guide", "Q1 FY25", "Q1 FY26"]
SALES = dict(
    sf=[896.0, 936.9, 998.6, 213.3, 238.7],      # Seasonings and Foods
    ff=[289.3, 290.3, 310.6, 68.7, 72.5],        # Frozen Foods
    bp=[147.6, 148.0, 176.2, 34.2, 37.9],        # Bio-Pharma Services and Ingredients
    fm=[76.5, 100.7, 120.6, 21.5, 33.1],         # Functional Materials
    oth=[104.1, 92.6, 109.9, 23.2, 25.9],        # Others (in Healthcare and Others)
    other=[16.7, 14.9, 15.8, 2.8, 3.7],          # Other segment
)
BPROF = dict(
    sf=[134.1, 143.0, 145.9, 36.3, 41.0],
    ff=[13.0, 8.4, 12.1, 2.8, 2.1],
    bp=[0.8, 9.5, 17.0, 2.8, 4.2],
    fm=[40.2, 54.6, 65.5, 10.8, 19.1],
    oth=[4.5, 2.0, 2.4, 1.6, 1.7],
    other=[6.3, 6.0, 5.1, 1.9, 1.6],
    shared=[-39.8, -42.5, -46.2, -9.2, -9.9],
)
SALES_TOT = [1530.5, 1583.7, 1732.0, 364.0, 412.1]
BP_TOT = [159.3, 181.1, 202.0, 47.2, 60.1]
OP_H = [113.968, 199.412]        # FY2024, FY2025 operating profit (FY2025 includes a 41.2bn gain on sale of fixed assets)
OP_G26 = 184.2                   # FY2026 revised forecast operating profit
PBT_G26 = 180.2
NI_H = [70.272, 134.675]         # profit attributable, FY2024, FY2025
EPS_H = [69.77, 138.36]          # basic EPS (split-adjusted)
NI_G26 = 123.5
NCI_PROFIT_G26 = 10.0
TAX_G26 = 0.259
DPS = [40.0, 48.0, 50.0]         # FY2024 split-adjusted, FY2025, FY2026 plan
ABF_SERVERS = [("FY2017", 40), ("FY2022", 60), ("FY2023", 65), ("FY2024", 70), ("FY2025", 70), ("FY2030 outlook", 80)]  # 75-85 shown at mid
PE_HIST = [("FY2016", 23.7), ("FY2017", 18.0), ("FY2018", 33.0), ("FY2019", 58.5), ("FY2020", 20.9), ("FY2021", 24.9),
           ("FY2022", 26.2), ("FY2023", 33.8), ("FY2024", 42.4), ("FY2025", 31.8)]  # P/E at fiscal year end, ASV Report 2026
CAPEX_G26, OCF_G26 = 129.5, 230.0
BUYBACK = dict(total=80.0, shares_max=30.0, done_sh=15.5884, done_yen=68.563, end="30 November 2026")

# ---- Peers (stockanalysis.com, retrieved 7 Oct 2026). EV = market value + debt - cash + non-controlling interests.
# Forward operating income = consensus for the fiscal year ending Dec 2026 or Mar 2027. Currency in local units, billions.
# name, listing, group, EV, fwd operating income, price, fwd EPS, year end, what they make
PEERS = [
    ("Kikkoman", "Tokyo: 2801", "food", 1590.439, 84.183, 1742.0, 71.38, "Mar 2027", "Soy sauce, seasonings, Del Monte foods in Asia"),
    ("Nestle", "SIX: NESN", "food", 250.288, 14.756, 75.15, 3.804, "Dec 2026", "Coffee, pet food, nutrition, confectionery"),
    ("Kraft Heinz", "Nasdaq: KHC", "food", 42.444, 3.911, 22.03, None, "Dec 2026", "Sauces, cheese, packaged meals"),
    ("Resonac", "Tokyo: 4004", "elec", 4075.462, 166.660, 18075.0, 581.06, "Dec 2026", "Semiconductor materials, incl. packaging films and laminates"),
    ("Shin-Etsu Chemical", "Tokyo: 4063", "elec", 10383.784, 742.976, 6234.0, 301.57, "Mar 2027", "Silicon wafers, photoresists, PVC, silicones"),
    ("Entegris", "Nasdaq: ENTG", "elec", 28.707, 0.8817, 166.89, 3.93, "Dec 2026", "Filters, process chemicals and materials for chipmaking"),
]
REF_PEERS = [  # shown, not in the medians
    ("Sekisui Chemical", "Tokyo: 4204", "ref", 1142.689, 113.38, 2535.0, 195.28, "Mar 2027", "Diversified; makes rival build-up films"),
]
AJI_EV_SA = 5541.872     # stockanalysis.com EV for Ajinomoto, 7 Oct 2026
PEER_EVEBIT = {p[0]: p[3] / p[4] for p in PEERS + REF_PEERS}
PEER_PE = {p[0]: (p[5] / p[6] if p[6] else None) for p in PEERS + REF_PEERS}
FOOD_MED = statistics.median([PEER_EVEBIT[p[0]] for p in PEERS if p[2] == "food"])
ELEC_MED = statistics.median([PEER_EVEBIT[p[0]] for p in PEERS if p[2] == "elec"])

# ---- MY estimates, yen billion ----
# FY2026E (to Mar 2027): company guide except Functional Materials. FY2027E (to Mar 2028): mine throughout.
FM_SALES = [130.0, 152.0]       # MINE. Q1 33.1; guide 120.6 implies 2Q-4Q +10% on a year earlier, after Q1 +54%.
FM_MARGIN = [0.56, 0.56]        # MINE. FY2025 54.2%; Q1 FY2026 57.7%; guide 54.3%.
FOOD_G27 = 0.04                 # MINE. Seasonings and Foods plus Frozen Foods business profit growth, FY2027
FOOD_SALES_G27 = 0.04
HO_SALES_G27 = 0.06             # Bio-Pharma and Others sales growth, FY2027
BIO_BP = [17.0, 20.0]           # MINE: FY2026 = guide
OTH_BP = [2.4, 2.5]
OTHER_BP = [5.1, 5.0]
SHARED = [-46.2, -48.0]         # FY2026 = guide
OTHER_OPEX = [-17.8, -18.0]     # MINE: net other operating expense; FY2026 guide OP 184.2 less BP 202.0
FIN_NET = -4.0                  # guide PBT 180.2 less OP 184.2
TAX = 0.26
NCI_PROFIT = [10.0, 10.5]
SH_AVG = [952.0, 948.0]         # MINE: average shares, m

FOOD_BP26 = BPROF["sf"][2] + BPROF["ff"][2]
FOOD_SALES26 = SALES["sf"][2] + SALES["ff"][2]
HO_SALES26 = SALES["bp"][2] + SALES["oth"][2]

# ---- Valuation (MINE): sum of the parts on FY2027E, twelve months out ----
MULT_FOOD = 18.0                # MINE. Food peers 17.0x median (Nestle), Kikkoman 18.9x
MULT_FM = 28.0                  # MINE. Electronic materials median 24.5x, a premium for margin, share and growth


def year(i, fm_sales=None, fm_margin=None, food_g=FOOD_G27, bio=None):
    """Segment build for FY2026E (i=0) or FY2027E (i=1). Returns a dict, yen billion."""
    fs = FM_SALES[i] if fm_sales is None else fm_sales
    fmm = FM_MARGIN[i] if fm_margin is None else fm_margin
    bio = BIO_BP[i] if bio is None else bio
    if i == 0:
        food_bp, food_s, ho_s = FOOD_BP26, FOOD_SALES26, HO_SALES26
        other_s = SALES["other"][2]
    else:
        food_bp = FOOD_BP26 * (1 + food_g)
        food_s = FOOD_SALES26 * (1 + FOOD_SALES_G27)
        ho_s = HO_SALES26 * (1 + HO_SALES_G27)
        other_s = SALES["other"][2]
    fm_bp = fs * fmm
    sales = food_s + ho_s + fs + other_s
    nonfm_gross = food_bp + bio + OTH_BP[i] + OTHER_BP[i]
    costs = SHARED[i] + OTHER_OPEX[i]                       # negative
    fm_share = fs / sales
    fm_net = fm_bp + costs * fm_share
    nonfm_net = nonfm_gross + costs * (1 - fm_share)
    bp = nonfm_gross + fm_bp + SHARED[i]
    op = bp + OTHER_OPEX[i]
    pbt = op + FIN_NET
    ni = pbt * (1 - TAX) - NCI_PROFIT[i]
    return dict(fm_sales=fs, fm_margin=fmm, fm_bp=fm_bp, food_bp=food_bp, food_sales=food_s, ho_sales=ho_s, bio=bio,
                sales=sales, nonfm_gross=nonfm_gross, costs=costs, fm_share=fm_share, fm_net=fm_net, nonfm_net=nonfm_net,
                bp=bp, op=op, pbt=pbt, ni=ni, eps=ni / SH_AVG[i] * 1000)


Y26, Y27 = year(0), year(1)


def sotp(y, m_food=MULT_FOOD, m_fm=MULT_FM):
    ev_food = y["nonfm_net"] * m_food
    ev_fm = y["fm_net"] * m_fm
    eq = ev_food + ev_fm - NET_DEBT - NCI
    return dict(ev_food=ev_food, ev_fm=ev_fm, ev=ev_food + ev_fm, equity=eq, ps=eq / SHARES * 1000,
                food_ps=(ev_food - NET_DEBT - NCI) / SHARES * 1000, fm_ps=ev_fm / SHARES * 1000)


BASE = sotp(Y27)
BASE_VALUE = BASE["ps"]
MED = sotp(Y27, FOOD_MED, ELEC_MED)       # on peer medians, no premium
MED_VALUE = MED["ps"]

#        name, FM sales FY27, FM margin, food BP growth, bio BP, food multiple, FM multiple, prob
SCEN = [
    ("Bear", 135.0, 0.50, 0.00, 17.0, 16.0, 20.0, 0.25),
    ("Base", FM_SALES[1], FM_MARGIN[1], FOOD_G27, BIO_BP[1], MULT_FOOD, MULT_FM, 0.50),
    ("Bull", 175.0, 0.60, 0.06, 22.0, 20.0, 36.0, 0.25),
]


def scen(s):
    y = year(1, fm_sales=s[1], fm_margin=s[2], food_g=s[3], bio=s[4])
    v = sotp(y, s[5], s[6])
    return dict(y=y, v=v, value=v["ps"])


SV = [scen(s) for s in SCEN]
VALS = [x["value"] for x in SV]
WEIGHTED = sum(v * s[7] for v, s in zip(VALS, SCEN))
assert abs(VALS[1] - BASE_VALUE) < 1e-6

# Sensitivity: FY2027E Functional Materials sales (56% margin) against the film multiple; food at base
SENS_S = [135.0, 152.0, 175.0]
SENS_X = [20.0, 28.0, 36.0]
VGRID = [[sotp(year(1, fm_sales=s), MULT_FOOD, x)["ps"] for x in SENS_X] for s in SENS_S]
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75

# ---- What the price implies ----
MCAP = PRICE * SHARES / 1000                     # yen billion
EV_MKT = MCAP + NET_DEBT + NCI
FM_IMPLIED_EV = EV_MKT - BASE["ev_food"]         # food and the rest at my base
FM_IMPLIED_X = FM_IMPLIED_EV / Y27["fm_net"]     # film EV / FY2027E film profit after allocated costs
FM_IMPLIED_NET_AT_BASE_X = FM_IMPLIED_EV / MULT_FM
FM_SHARE_EV_MKT = FM_IMPLIED_EV / EV_MKT
FM_SHARE_EV_BASE = BASE["ev_fm"] / BASE["ev"]
FOOD_FLOOR_PS = BASE["food_ps"]
FOOD_FLOOR_SHARE = FOOD_FLOOR_PS / PRICE
# FY2027E film sales at 56% that the price needs at 28x
lo, hi = 50.0, 400.0
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if sotp(year(1, fm_sales=mid))["ps"] < PRICE else (lo, mid)
NEED_FM_SALES = (lo + hi) / 2
NEED_FM_BP = NEED_FM_SALES * FM_MARGIN[1]
# FY2027E film sales that move the base value to the band edges (other inputs unchanged)
def _solve(target):
    lo, hi = 20.0, 500.0
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if sotp(year(1, fm_sales=mid))["ps"] < target else (lo, mid)
    return (lo + hi) / 2
FM_SALES_LONG = _solve(PRICE * 1.15)
FM_SALES_SHORT = _solve(PRICE * 0.75)
FM_BP_LONG = FM_SALES_LONG * FM_MARGIN[1]
FM_BP_SHORT = FM_SALES_SHORT * FM_MARGIN[1]

# Leverage: how much the film moves the whole company
FM_10PCT_MKT_PS = 0.10 * FM_IMPLIED_EV / SHARES * 1000
FM_10PCT_BASE_PS = 0.10 * BASE["ev_fm"] / SHARES * 1000
FM_TURN_PS = Y27["fm_net"] / SHARES * 1000        # one turn of film multiple, yen per share
FOOD_TURN_PS = Y27["nonfm_net"] / SHARES * 1000

# Shares of sales and profit (Ajinomoto's own figures)
FM_SALES_SHARE = [SALES["fm"][k] / SALES_TOT[k] for k in range(5)]
SEG_BP_TOTAL = [sum(BPROF[x][k] for x in ["sf", "ff", "bp", "fm", "oth", "other"]) for k in range(5)]
FM_BP_SHARE_SEG = [BPROF["fm"][k] / SEG_BP_TOTAL[k] for k in range(5)]     # before shared costs
FM_BP_SHARE_GRP = [BPROF["fm"][k] / BP_TOT[k] for k in range(5)]           # of group business profit
FOOD_SALES_SHARE = [(SALES["sf"][k] + SALES["ff"][k]) / SALES_TOT[k] for k in range(5)]
FOOD_BP_SHARE_SEG = [(BPROF["sf"][k] + BPROF["ff"][k]) / SEG_BP_TOTAL[k] for k in range(5)]
FM_MARGIN_H = [b / s for b, s in zip(FM_BP_H, FM_SALES_H)]
FMQ_MARGIN = [b / s for b, s in zip(FMQ_BP, FMQ_SALES)]
# FY2025 film profit after a sales-based share of shared costs, as a share of group business profit (MINE)
FM_BP_ALLOC_25 = BPROF["fm"][1] + BPROF["shared"][1] * FM_SALES_SHARE[1]
FM_BP_SHARE_ALLOC_25 = FM_BP_ALLOC_25 / BP_TOT[1]
PE_HIST_RANGE = (min(p for y, p in PE_HIST[:6]), max(p for y, p in PE_HIST[:6]))   # FY2016 to FY2021
FM_NET27_SHARE = Y27["fm_net"] / (Y27["fm_net"] + Y27["nonfm_net"])

# Multiples at the price
PE_CONS26 = PRICE / CONS_EPS26
PE_GUIDE26 = PRICE / GUIDE_EPS26
PE26, PE27 = PRICE / Y26["eps"], PRICE / Y27["eps"]
EV_BP26_GUIDE = EV_MKT / BP_TOT[2]
EV_OP_CONS = AJI_EV_SA / CONS_OP26
SINCE_DEC25 = PRICE / PX_DEC25 - 1
SINCE_MAR25 = PRICE / PX_MAR25 - 1
OFF_HIGH = PRICE / HI_CLOSE - 1
PE_PRE = statistics.median([p for y, p in PE_HIST if y in ("FY2016", "FY2017", "FY2020", "FY2021")])

if __name__ == "__main__":
    print(f"shares {SHARES:.2f}m mcap {MCAP:,.1f} netdebt {NET_DEBT:.1f} ev {EV_MKT:,.1f} (SA {AJI_EV_SA:,.1f})")
    for n, y in (("FY26E", Y26), ("FY27E", Y27)):
        print(n, {k: round(v, 2) if isinstance(v, float) else v for k, v in y.items()})
    print(f"peers evebit {{{', '.join(f'{k}: {v:.1f}' for k, v in PEER_EVEBIT.items())}}} food med {FOOD_MED:.1f} elec med {ELEC_MED:.1f}")
    print("peers pe", {k: (round(v, 1) if v else None) for k, v in PEER_PE.items()})
    print(f"base {BASE_VALUE:.0f} ({BASE_VALUE/PRICE-1:+.1%}) food_ps {BASE['food_ps']:.0f} fm_ps {BASE['fm_ps']:.0f} ev food {BASE['ev_food']:.0f} fm {BASE['ev_fm']:.0f}")
    print(f"median-based {MED_VALUE:.0f} ({MED_VALUE/PRICE-1:+.1%})")
    for s, v in zip(SCEN, SV):
        print(s[0], f"fm_net {v['y']['fm_net']:.1f} nonfm {v['y']['nonfm_net']:.1f} value {v['value']:.0f} ({v['value']/PRICE-1:+.1%})")
    print(f"weighted {WEIGHTED:.0f} ({WEIGHTED/PRICE-1:+.1%}); revisit {REVISIT_LONG:.0f} / {REVISIT_SHORT:.0f}")
    print("grid", [[round(v) for v in r] for r in VGRID])
    print(f"implied fm EV {FM_IMPLIED_EV:,.0f} = {FM_IMPLIED_X:.1f}x FY27E fm_net {Y27['fm_net']:.1f}; at 28x needs fm_net {FM_IMPLIED_NET_AT_BASE_X:.1f}")
    print(f"need fm sales {NEED_FM_SALES:.1f} bp {NEED_FM_BP:.1f}; band fm sales long {FM_SALES_LONG:.1f} ({FM_BP_LONG:.1f}) short {FM_SALES_SHORT:.1f} ({FM_BP_SHORT:.1f})")
    print(f"fm share of EV: mkt {FM_SHARE_EV_MKT:.1%} base {FM_SHARE_EV_BASE:.1%}; food floor {FOOD_FLOOR_PS:.0f} = {FOOD_FLOOR_SHARE:.1%} of price")
    print(f"10% film: mkt {FM_10PCT_MKT_PS:.0f}/sh ({FM_10PCT_MKT_PS/PRICE:.1%}) base {FM_10PCT_BASE_PS:.0f} ({FM_10PCT_BASE_PS/PRICE:.1%}); turn fm {FM_TURN_PS:.0f} food {FOOD_TURN_PS:.0f}")
    print("fm sales share", [f"{x:.1%}" for x in FM_SALES_SHARE], "bp share seg", [f"{x:.1%}" for x in FM_BP_SHARE_SEG], "grp", [f"{x:.1%}" for x in FM_BP_SHARE_GRP])
    print("food sales share", [f"{x:.1%}" for x in FOOD_SALES_SHARE], "food bp share seg", [f"{x:.1%}" for x in FOOD_BP_SHARE_SEG])
    print(f"fm27 share of net profit {FM_NET27_SHARE:.1%}; fm margins {[round(m*100,1) for m in FM_MARGIN_H]} q {[round(m*100,1) for m in FMQ_MARGIN]}")
    print(f"PE cons26 {PE_CONS26:.1f} guide26 {PE_GUIDE26:.1f} mine {PE26:.1f} {PE27:.1f}; ev/bp26 guide {EV_BP26_GUIDE:.1f} ev/op cons {EV_OP_CONS:.1f}; eps {Y26['eps']:.1f} {Y27['eps']:.1f}")
    print(f"since dec25 {SINCE_DEC25:+.1%} since mar25 {SINCE_MAR25:+.1%} off high {OFF_HIGH:+.1%}; pe pre {PE_PRE}")
