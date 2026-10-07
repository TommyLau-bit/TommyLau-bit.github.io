"""Micron Technology, Inc. (Nasdaq: MU) initiation, draft of 7 Oct 2026. Single source of figures for charts, note and model.

Sources: Micron fiscal Q4 2026 results release (Exhibit 99.1 to Form 8-K, 30 Sep 2026) and prepared remarks (30 Sep 2026);
fiscal Q3 2026 prepared remarks (24 Jun 2026); earnings call transcripts for fiscal Q1 2026 (17 Dec 2025) and fiscal Q2 2026
(transcripts.platformaeronaut.com) and fiscal Q4 2026 (30 Sep 2026, stockanalysis.com / Quartr). Fiscal Q4 2025 figures from
the comparatives in the Q4 2026 release and remarks, and the Q4 2025 call (23 Sep 2025). Annual revenue and GAAP net income
FY2016 to FY2021 from Micron's 10-K XBRL data on SEC EDGAR (companyconcept API); FY2022 to FY2026 from stockanalysis.com
(S&P Global), matching the 10-Ks and the Q4 2026 release.
Prices: Nasdaq.com historical data (Yahoo Finance chart API refused requests with "Too Many Requests" on 7 Oct 2026).
Consensus, average target, shares outstanding and peer figures: stockanalysis.com (S&P Global), retrieved 7 Oct 2026.
Everything marked MINE is my own estimate.

Fiscal years end on the Thursday closest to 31 August: FY2025 = year to 28 Aug 2025; FY2026 = year to 3 Sep 2026 (53 weeks);
FY2027 = year to about 2 Sep 2027; FY2028 = year to about 31 Aug 2028. Calendar years (CY) are used for Micron's HBM and
industry supply statements. Income figures are Micron's NON-GAAP measures unless marked GAAP. Micron guides on non-GAAP.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-07"
DATE_LONG = "7 October 2026"
COMPANY = "Micron"
NAME = "Micron Technology"
SLUG = "micron"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/micron"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",        # e.g. "INITIATE AT NO CALL" / "INITIATE AT SHORT" once Tommy decides
    direction="NO CALL",
    target=None,                    # US$ per share; None for NO CALL
    conviction="Low",
    draft=False,
)

# ---- Market data (Nasdaq.com historical data, retrieved 7 Oct 2026) ----
PRICE = 1045.56         # Nasdaq close, 6 Oct 2026
PRICE_DATE = "6 October 2026"
HI_CLOSE = 1213.56      # highest close of the past year, 25 Jun 2026
HI52 = 1255.00          # intraday high of the past year, 25 Jun 2026
LO_CLOSE = 181.60       # lowest close of the past year, 10 Oct 2025
LO52 = 179.61           # intraday low of the past year, 10 Oct 2025
PRICE_DEC25 = 285.41    # close, 31 Dec 2025
PX_RESULTS = (1065.11, 1097.39)  # closes 30 Sep 2026 (results after the close) and 1 Oct 2026
PX_LABELS = ['Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24',
             'Sep 24', 'Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25',
             'Sep 25', 'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26',
             'Sep 26', '6 Oct 26']
PX = [68.03, 66.87, 76.12, 85.34, 85.75, 90.61, 117.89, 112.96, 125.0, 131.53, 109.82, 96.24,
      103.71, 99.65, 97.95, 84.16, 91.24, 93.63, 86.89, 76.95, 94.46, 123.25, 109.14, 119.01,
      167.32, 223.77, 236.48, 285.41, 414.88, 412.37, 337.84, 517.16, 971.0, 1154.29, 823.03, 958.73,
      1065.11, 1045.56]
# The last cycle, for scale (Nasdaq.com): highest close of fiscal 2022 US$97.36 (14 Jan 2022); lowest close US$48.88
# (26 Sep 2022), weeks into fiscal 2023, when GAAP EPS swung to a loss of US$5.34.
FY22_HI = (97.36, "14 January 2022")
FY23_LO = (48.88, "26 September 2022")

SHARES_OUT = 1.13       # bn shares outstanding (stockanalysis.com, 7 Oct 2026)
SH_Q4 = 1.149           # bn, non-GAAP diluted shares, fiscal Q4 2026 (release)

# ---- Balance sheet, 3 Sep 2026 (Q4 FY26 release and prepared remarks), US$bn ----
CASH_INV = 73.453       # cash, marketable investments: 38.364 + 5.070 + 30.019
DEBT = 5.179            # 0.491 current + 4.688 long-term
NET_CASH = CASH_INV - DEBT
DEPOSITS = 12.7         # SCA customer cash deposits on the balance sheet; returned to customers over time
NET_CASH_ADJ = NET_CASH - DEPOSITS
RPO = 150.0             # remaining performance obligations, about US$150bn (Q4 FY26 remarks)
SCA_N = 26              # strategic customer agreements signed
SCA_SHARE = 0.35        # "over 35% of our revenue through 2030"; three quarters has a defined pricing framework,
                        # "a majority of which have pricing bands with floor and ceiling prices": floors on roughly 13 to 26% of revenue
FLOOR_SHARE = (SCA_SHARE * 0.75 * 0.5, SCA_SHARE * 0.75)
SCA_COMMIT = 32.0       # US$bn financial commitments from customers, mostly cash deposits
COMMIT_27 = 0.75        # "more than 75% of our output is already committed for 2027" (call, 30 Sep 2026)
DEP_Q4 = 12.3           # customer cash deposits received in fiscal Q4 2026
DA_26 = 9.50            # depreciation and amortisation, FY2026 (stockanalysis.com cash flow)

# ---- Consensus and peers (stockanalysis.com, S&P Global data; retrieved 7 Oct 2026) ----
CONS_EPS_27 = 176.15    # FY27 non-GAAP EPS, 39 analysts, range 161.00 to 214.70; updated 6 Oct 2026
CONS_EPS_28 = 206.33    # FY28
CONS_REV_27 = 275.01
CONS_REV_28 = 314.64
CONS_TP = 1535.57       # average target, 49 analysts; range 361 to 2,200
CONS_TP_RANGE = (361.0, 2200.0)
PEERS = [  # company, listing, price, currency, consensus EPS (year ending in 2027), year, what they make, note
    ("SK Hynix", "KRX: 000660", 1723000.0, "KRW", 470190.0, "CY2027", "DRAM, HBM, NAND", "7 Oct close"),
    ("Samsung Electronics", "KRX: 005930", 268500.0, "KRW", 71030.0, "CY2027", "DRAM, HBM, NAND, logic, phones", "7 Oct close"),
    ("SanDisk", "Nasdaq: SNDK", 1660.46, "US$", 213.90, "FY to Jun 2027", "NAND flash and SSDs", "6 Oct close"),
]
KIOXIA = ("Kioxia", "TSE: 285A", 29.43, 5.63, "FY to Mar 2027", "NAND flash and SSDs")  # market value and consensus net income, JPY trillion
PEERS_THIS = {"SK Hynix": 353756.88, "Samsung Electronics": 47890.93, "SanDisk": 263.49}  # CY2026 / CY2026 / FY to Jun 2028

# ---- Annual history ----
# GAAP revenue and GAAP net income, US$bn, FY2016 to FY2026 (10-K XBRL; stockanalysis.com for FY2022 to FY2026)
YRS10 = ["FY16", "FY17", "FY18", "FY19", "FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]
REV10 = [12.399, 20.322, 30.391, 23.406, 21.435, 27.705, 30.758, 15.540, 25.111, 37.378, 133.188]
NI10 = [-0.276, 5.089, 14.135, 6.313, 2.687, 5.861, 8.687, -5.833, 0.778, 8.539, 84.969]
GAAP_EPS = {"FY22": 7.75, "FY23": -5.34, "FY24": 0.70, "FY25": 7.59, "FY26": 74.33}
CYC_REV = sum(REV10[:10]); CYC_NI = sum(NI10[:10])
CYC_NM = CYC_NI / CYC_REV                 # ten-year GAAP net margin, FY2016 to FY2025
PEAK18_NM = NI10[2] / REV10[2]           # FY2018, the last cycle's peak year
NM26_GAAP = NI10[10] / REV10[10]

# Non-GAAP annual, US$bn (Q4 FY26 release)
FY25 = dict(rev=37.378, ni=9.470, eps=8.29, gm=0.409)  # non-GAAP gross margin 40.9% (Q4 FY26 release comparatives)
FY26 = dict(rev=133.188, ni=86.758, eps=75.52, gm=0.811, op=6.4 + 16.5 + 33.7 + 44.6, opex=1.3 + 1.4 + 1.5 + 2.6,
            dram=10.8 + 18.8 + 31.3 + 39.8, nand=2.7 + 5.0 + 9.9 + 14.1, ocf=89.675, capex=27.367, fcf=62.308)
BU26 = dict(CMBU=43.085, CDBU=37.592, MCBU=36.601, AEBU=15.886)

# ---- Quarterly, non-GAAP (prepared remarks and calls), US$bn ----
QL = ["Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26"]
QS = ["Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26"]
Q_REV = [11.315, 13.643, 23.860, 41.456, 54.229]   # Q2 FY26 = FY26 less the other three quarters
Q_DRAM = [8.98, 10.8, 18.8, 31.3, 39.8]              # Q4 FY25: US$39.8bn is up 343% (8.98)
Q_NAND = [2.25, 2.7, 5.0, 9.9, 14.1]                 # Q4 FY25: US$14.1bn is up 526% (2.25)
Q_GM = [0.457, 0.568, 0.750, 0.849, 0.870]
Q_OP = [None, 6.4, 16.5, 33.7, 44.6]
Q_OM = [None, 0.47, 0.69, 0.812, 0.823]
Q_EPS = [3.03, 4.78, 12.20, 25.11, 33.42]
Q_OPEX = [None, 1.3, 1.4, 1.5, 2.6]
# Business unit gross margins by quarter, fiscal 2026 (prepared remarks and calls)
BU_GM = {"CMBU (cloud, includes HBM)": [0.66, 0.74, 0.83, 0.83], "CDBU (core data centre)": [0.51, 0.74, 0.87, 0.90],
         "MCBU (mobile and PC)": [0.54, 0.79, 0.87, 0.90], "AEBU (auto and embedded)": [0.45, 0.68, 0.79, 0.84]}
BU_REV = {"CMBU": [5.3, 7.7, 13.8, 16.283], "CDBU": [2.4, 5.7, 11.5, 18.002], "MCBU": [4.3, 7.7, 11.5, 13.114], "AEBU": [1.7, 2.7, 4.6, 6.824]}
# Q4 FY26 price and bit moves (sequential): DRAM bits up mid single digits, prices up high teens; NAND bits about +10%, prices about +30%.
HBM_Q4FY25 = 2.0        # "nearly $2 billion" HBM revenue in fiscal Q4 2025 (call, 23 Sep 2025)
HBM_TAM = (35.0, 100.0)  # industry HBM revenue, CY2025 about US$35bn to about US$100bn in CY2028 (17 Dec 2025)
DC_SSD_Q4 = 10.0        # data centre SSD revenue "nearly $10 billion" in fiscal Q4 2026, over two thirds of NAND

# ---- Guidance (Q4 FY26 release and remarks, 30 Sep 2026) ----
G1 = dict(rev=61.5, rev_pm=1.5, gm=0.8625, opex=2.06, eps=38.15, eps_pm=1.00, sh=1.15, tax=0.155)
OPEX_FY27_UP = 2.5      # "operating expenses to increase by approximately $2.5 billion in fiscal 2027"
CAPEX_H1 = 25.0         # first-half fiscal 2027 capex about US$25bn; second half higher
INDUSTRY = dict(dram26="mid-20s %", dram2728="low-20s %", nand26="low-20s %", nand2728="mid-20s %")
RESULTS_DATE = "17 December 2026"   # third-party calendars (Wall Street Horizon, MarketScreener); not yet confirmed by Micron
RETURN_DATE = "9 December 2026"     # capital return to step up from this date (second anniversary of the CHIPS agreements)

# ---- MY FY2027 quarters (Q1 = the guide) ----
Q27_REV = [G1["rev"], 65.2, 68.4, 71.2]        # MINE after Q1: "sequential revenue growth each quarter", slower price rises
Q27_GM = [G1["gm"], 0.875, 0.880, 0.880]        # MINE after Q1: Q1 is "the floor for gross margins in fiscal 2027"
Q27_OPEX = [G1["opex"], 2.40, 2.42, 2.42]       # MINE: sums to FY26's 6.8 plus the guided 2.5
TAX = G1["tax"]
SH = G1["sh"]           # MINE: share count held at 1.15bn; buybacks from December treated as cash kept (value-neutral at fair value)
OTHER_Q1 = G1["eps"] * SH / (1 - TAX) - (G1["rev"] * G1["gm"] - G1["opex"])   # interest and other implied by the Q1 guide
Q27_OTHER = [OTHER_Q1, 1.0, 1.1, 1.2]          # MINE after Q1: interest income on a growing cash pile


def q27():
    ni = [(r * g - o + x) * (1 - TAX) for r, g, o, x in zip(Q27_REV, Q27_GM, Q27_OPEX, Q27_OTHER)]
    return ni, [n / SH for n in ni]


Q27_NI, Q27_EPS = q27()
REV27 = sum(Q27_REV); NI27 = sum(Q27_NI); EPS27 = sum(Q27_EPS)
GM27 = sum(r * g for r, g in zip(Q27_REV, Q27_GM)) / REV27
OPEX27 = sum(Q27_OPEX)
OP27 = REV27 * GM27 - OPEX27

# Split of revenue by line, MINE (Micron reports DRAM including HBM, and NAND; it stopped giving HBM revenue in FY26)
HBM26 = 10.0            # MINE: about Micron's DRAM share of an industry HBM market of about US$49bn in CY2026 (40% a year from US$35bn)
SPLIT27 = dict(hbm=16.0, nand=72.0)             # MINE: HBM about 23% of a CY2027 market near US$69bn
SPLIT28 = dict(hbm=22.0, nand=80.0)             # MINE: HBM about 22% of Micron's US$100bn CY2028 market forecast

# ---- MY FY2028 and the cash at October 2027 ----
G28 = 0.10              # MINE: revenue growth in FY28 (consensus +14%)
GM28 = 0.86             # MINE
OPEX28 = 11.0           # MINE
OTHER28 = 4.0           # MINE: interest income
DA27 = 13.0             # MINE: depreciation, FY27 (FY26 US$9.5bn)
CAPEX27 = 55.0          # MINE: H1 about US$25bn guided, H2 higher
WC27 = 5.0              # MINE: working capital build
DIV27 = 0.60 * SH       # dividend of US$0.15 a quarter
FCF27 = NI27 + DA27 - CAPEX27 - WC27
NC_OCT27 = NET_CASH_ADJ + FCF27 - DIV27        # net cash after deposits, end of FY27 (about 2 Sep 2027)
NC_PS = NC_OCT27 / SH


def eps28(g=G28, gm=GM28):
    rev = REV27 * (1 + g)
    ni = (rev * gm - OPEX28 + OTHER28) * (1 - TAX)
    return rev, ni / SH


REV28, EPS28 = eps28()

# ---- Normal (mid-cycle) earnings, MINE ----
BITS = 1.20             # MINE: bit growth a year, about Micron's low-20s industry outlook for CY2027 and CY2028
N_YEARS = 4             # FY2026 to a mid-cycle year around FY2030
PF = 0.55               # MINE: mid-cycle revenue per bit against FY2026's average
NM = 0.30               # MINE: mid-cycle net margin, against 18.8% over FY2016 to FY2025 and 46.5% at the FY2018 peak
MULT = 12               # MINE: P/E on normal earnings
RATE = 0.10             # MINE: discount rate on above-normal earnings
W_UP = (1.0, 0.5, 0.0)  # MINE: share of FY28's excess earned in FY28, FY29, FY30 (base)
GROWTH_F = BITS ** N_YEARS


def normal_rev(pf=PF):
    return FY26["rev"] * GROWTH_F * pf


def normal_eps(pf=PF, nm=NM):
    return normal_rev(pf) * nm / SH


def value(n, mult=MULT, e28=None, w=W_UP):
    e28 = EPS28 if e28 is None else e28
    exc = sum(wi * (e28 - n) / (1 + RATE) ** (i + 1) for i, wi in enumerate(w))
    return dict(nc=NC_PS, exc=exc, term=n * mult, value=NC_PS + exc + n * mult)


N_BASE = normal_eps()
#        name,  price factor, net margin, multiple, FY28 growth, FY28 GM, upcycle weights, prob
SCEN = [
    ("Bear", 0.40, 0.19, 10, -0.25, 0.75, (1.0, 0.0, 0.0), 0.25),
    ("Base", PF, NM, MULT, G28, GM28, W_UP, 0.50),
    ("Bull", 0.70, 0.40, 14, 0.22, 0.885, (1.0, 1.0, 0.5), 0.25),
]


def scen(s):
    n = normal_eps(s[1], s[2]); r28, e28 = eps28(s[4], s[5])
    v = value(n, s[3], e28, s[6])
    return dict(n=n, nrev=normal_rev(s[1]), rev28=r28, eps28=e28, **v)


SV = [scen(s) for s in SCEN]
VALS = [v["value"] for v in SV]
WEIGHTED = sum(v * s[7] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
UP_BASE = BASE_VALUE / PRICE - 1
RULE = "LONG" if UP_BASE >= 0.15 else ("SHORT" if UP_BASE <= -0.25 else "NO CALL")

# Sensitivity: normal net margin (rows) against the normal multiple (columns), base revenue and FY28
SENS_NM = [0.22, NM, 0.38]
SENS_X = [10, MULT, 14]
VGRID = [[value(normal_eps(PF, m), x)["value"] for x in SENS_X] for m in SENS_NM]

# What the price implies: normal EPS at the base multiple, FY28 and up-cycle (linear in n, solved exactly)
_k = sum(wi / (1 + RATE) ** (i + 1) for i, wi in enumerate(W_UP))
NEED_N = (PRICE - NC_PS - _k * EPS28) / (MULT - _k)
NEED_NM = NEED_N * SH / normal_rev()          # as a net margin on my base normal revenue
NEED_REV30 = NEED_N * SH / NM                 # as revenue at my base margin
REVISIT_LONG = BASE_VALUE / 1.15              # price at or below which the base is 15% above (points long)
REVISIT_SHORT = BASE_VALUE / 0.75             # price at or above which the base is 25% below (points short)
REVISIT_N_LONG = (PRICE * 1.15 - NC_PS - _k * EPS28) / (MULT - _k)
REVISIT_N_SHORT = (PRICE * 0.75 - NC_PS - _k * EPS28) / (MULT - _k)

# ---- Value and multiples ----
MCAP = PRICE * SHARES_OUT
EV = MCAP - NET_CASH_ADJ
PE26 = PRICE / FY26["eps"]
PE27, PE28 = PRICE / EPS27, PRICE / EPS28
PEC27, PEC28 = PRICE / CONS_EPS_27, PRICE / CONS_EPS_28
PE_NORMAL = PRICE / N_BASE
PEER_PE = [(p[0], p[2] / p[4]) for p in PEERS] + [(KIOXIA[0], KIOXIA[2] / KIOXIA[3])]
import statistics
PEER_MED = statistics.median([x[1] for x in PEER_PE])
FY22_PE_HI = FY22_HI[0] / GAAP_EPS["FY22"]
FY23_FALL = FY23_LO[0] / FY22_HI[0] - 1
SINCE_DEC25 = PRICE / PRICE_DEC25 - 1
OFF_HIGH = PRICE / HI_CLOSE - 1
RISE_LO = PRICE / LO_CLOSE - 1
NEED_VS_26 = NEED_N / FY26["eps"]
NEED_VS_28 = NEED_N / EPS28
CONV27 = REV27 - SPLIT27["hbm"] - SPLIT27["nand"]
CONV28 = REV28 - SPLIT28["hbm"] - SPLIT28["nand"]
CONV26 = FY26["dram"] - HBM26

if __name__ == "__main__":
    print(f"other Q1 {OTHER_Q1:.3f}; Q27 EPS {[round(e, 2) for e in Q27_EPS]}")
    print(f"FY27 rev {REV27:.1f} GM {GM27:.2%} opex {OPEX27:.2f} op {OP27:.1f} NI {NI27:.1f} EPS {EPS27:.2f} (cons {CONS_EPS_27}, {EPS27/CONS_EPS_27-1:+.1%}); rev vs cons {REV27/CONS_REV_27-1:+.1%}")
    print(f"FY28 rev {REV28:.1f} EPS {EPS28:.2f} (cons {CONS_EPS_28}, {EPS28/CONS_EPS_28-1:+.1%})")
    print(f"FCF27 {FCF27:.1f}; NC Oct27 {NC_OCT27:.1f} = {NC_PS:.1f}/sh; net cash adj now {NET_CASH_ADJ:.1f}")
    print(f"normal rev {normal_rev():.1f} EPS {N_BASE:.2f}; growth f {GROWTH_F:.4f}")
    for s, v in zip(SCEN, SV):
        print(s[0], {k: round(x, 2) for k, x in v.items()}, f"{v['value']/PRICE-1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} ({WEIGHTED/PRICE-1:+.1%}); base {BASE_VALUE:.1f} ({UP_BASE:+.1%}) rule {RULE}")
    print("grid", [[round(v) for v in r] for r in VGRID], sum(v > PRICE for r in VGRID for v in r))
    print(f"need N {NEED_N:.2f} nm {NEED_NM:.1%} rev@30% {NEED_REV30:.0f}; vs26 {NEED_VS_26:.0%} vs28 {NEED_VS_28:.0%}")
    print(f"revisit price <= {REVISIT_LONG:.0f} >= {REVISIT_SHORT:.0f}; N >= {REVISIT_N_LONG:.2f} <= {REVISIT_N_SHORT:.2f}")
    print(f"mcap {MCAP:.0f} EV {EV:.0f}; PE26 {PE26:.1f} PE27 {PE27:.1f} PE28 {PE28:.1f} cons {PEC27:.1f} {PEC28:.1f} normal {PE_NORMAL:.1f}")
    print("peers", [(n, round(x, 2)) for n, x in PEER_PE], "median", round(PEER_MED, 2))
    print(f"cycle nm {CYC_NM:.1%} peak18 {PEAK18_NM:.1%} nm26 {NM26_GAAP:.1%}; FY22 PE hi {FY22_PE_HI:.1f} fall {FY23_FALL:.0%}")
    print(f"since dec {SINCE_DEC25:+.0%} off high {OFF_HIGH:+.1%} rise lo {RISE_LO:+.0%}; FY26 op {FY26['op']:.1f} opm {FY26['op']/FY26['rev']:.1%} dram {FY26['dram']:.1f} nand {FY26['nand']:.1f}")
    print(f"conv dram 26 {CONV26:.1f} 27 {CONV27:.1f} 28 {CONV28:.1f}; Q sum rev {sum(Q_REV[1:]):.3f}")
