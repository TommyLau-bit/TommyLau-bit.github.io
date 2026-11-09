"""Oklo (NYSE: OKLO) initiation, draft of 6 Oct 2026. Single source of figures for charts, note and model.

Sources: Oklo Form 10-Q for the quarter to 30 June 2026 (filed 7 Aug 2026), Form 10-Q/A for Q1 2026 (17 Jun 2026,
certification only), Form 10-K for 2025 (17 Mar 2026), Form 8-K of 11 Sep 2026 (new US$1bn ATM; May 2026 ATM ended
after 17,971,448 shares for about US$1bn gross), 424B5 of 11 Sep 2026 (options and RSUs outstanding at 30 Jun 2026).
SEC XBRL company facts for quarterly history. Second quarter 2026 business update and call, 7 Aug 2026 (2026 guidance,
Aurora-INL in 2028, CFO on the Meta payment and Kiewit cost). Oklo and Meta announcement, 9 Jan 2026 (phase one as early
as 2030, 1.2 GW by 2034). Oklo groundbreaking release, 22 Sep 2025. OPG and Ontario Darlington BWRX-300 approval,
8 May 2025. Yahoo Finance chart API (prices), stockanalysis.com (peers, consensus, target, short interest), all
retrieved 6 October 2026. Everything marked MINE is my own estimate.
All money in US$ million unless stated.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-06"
DATE_LONG = "6 October 2026"
COMPANY = "Oklo"
NAME = "Oklo"
SLUG = "oklo"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/oklo"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view; Tommy decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT SHORT",          # e.g. "INITIATE AT SHORT" once Tommy decides
    direction="SHORT",
    target=28,                      # US$ per share: the probability-weighted value, rounded
    conviction="Low",
    draft=False,
)

# ---- Market data (Yahoo Finance chart API, retrieved 6 Oct 2026) ----
PRICE = 35.97            # NYSE close, 5 Oct 2026
PRICE_DATE = "5 October 2026"
PRICE_PIECE = 37.11      # close on 29 Sep 2026, the journal piece's date
HI52 = 193.84            # 52-week high, intraday 15 Oct 2025
HI_CLOSE = 174.14        # highest close, 14 Oct 2025
LO52 = 34.38             # 52-week low, intraday 14 Sep 2026
LO_CLOSE = 35.62         # lowest close, 16 Sep 2026
PX_META = (97.60, 105.31)    # closes 8 and 9 Jan 2026 (Meta agreement announced 9 Jan)
PX_Q2 = (42.19, 48.42)       # closes 6 and 7 Aug 2026 (Q2 update after the close on 7 Aug? see note)
PX_ATM = (39.88, 36.22)      # closes 10 and 11 Sep 2026 (new US$1bn ATM filed 11 Sep)
PRICE_DEC25 = 71.76          # month-end close, 31 Dec 2025
PEER_FALL = dict(OKLO=(174.14, 35.97), SMR=(53.43, 7.68), NNE=(56.63, 15.51))  # highest close in 52 weeks, 5 Oct close

# ---- Balance sheet and shares (10-Q for Q2 2026; 8-K and 424B5 of 11 Sep 2026) ----
CASH_EQ = 1644.704; MKT_CUR = 820.454; MKT_NONCUR = 541.131
CASH_JUN = CASH_EQ + MKT_CUR + MKT_NONCUR     # 3,006.3, cash and marketable debt securities, 30 Jun 2026
RESTRICTED = 16.9
CASH_DEC25 = 788.445 + 439.526 + 184.568      # 1,412.5 at 31 Dec 2025
ROFR = 25.0              # right-of-first-refusal payment from a prospective customer, March 2024, held as a liability
SH_JUN = 185.090155      # m shares outstanding, 30 Jun 2026
ATM_MAY_SH = 17.971448   # m shares sold under the May 2026 ATM to its end on 10 Sep 2026 (8-K)
ATM_MAY_GROSS = 1000.0   # about US$1bn gross (8-K)
ATM_Q2_SH = 10.712054; ATM_Q2_GROSS = 680.371   # of which sold by 30 Jun 2026 (10-Q)
ATM_Q3_SH = ATM_MAY_SH - ATM_Q2_SH               # 7.26m sold 1 Jul to 10 Sep 2026
ATM_Q3_GROSS = ATM_MAY_GROSS - ATM_Q2_GROSS      # about US$320m
ATM_FEE = 0.015
ATM_Q3_NET = ATM_Q3_GROSS * (1 - ATM_FEE)
SH_SEP = SH_JUN + ATM_Q3_SH                      # at least 192.35m by 10 Sep 2026
OPTIONS = 5.738353; OPT_STRIKE = 2.07; RSUS = 3.677081   # m, 30 Jun 2026 (424B5)
FD = SH_SEP + OPTIONS + RSUS
ATM_H1 = [("2025 ATM, Q1 2026", 12.376352, 1199.868, 96.95), ("May 2026 ATM, Q2 2026", 10.712054, 680.371, 63.51)]
RAISED_25 = 1263.6       # net proceeds from share sales in 2025 (10-K)
RAISED_H1_26 = 1851.9    # net, H1 2026 (10-Q)

# ---- History (10-K 2025, 10-Q Q2 2026, XBRL) ----
YEARS_H = ["2024", "2025"]
OPLOSS_H = [-52.8, -139.3]; NETLOSS_H = [-73.6, -105.7]
OCF_H = [-38.4, -82.2]; CAPEX_H = [0.4, 33.2]
CASHSEC_H = [275.3, CASH_DEC25]; SH_H = [137.7, 160.5]
H1 = dict(rev=1.21, oploss=-124.2, netloss=-81.6, ocf=-65.5, capex=126.9, sbc=29.9, interest=44.5)
GUIDE_26 = dict(ocf=(120, 150), capex=(400, 500))           # 7 Aug 2026, raised from 80-100 and 350-450
GUIDE_26_PRIOR = dict(ocf=(80, 100), capex=(350, 450))
Q = ["Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_CASHSEC = [294.6, 288.5, 275.3, 260.7, 683.0, 1183.6, 1412.5, 2536.9, 3006.3]
Q_SHARES = [122.1, 122.1, 137.7, 139.2, 147.6, 156.2, 160.5, 173.9, 185.1]
Q_CAPEX = [0.08, 0.11, 0.07, 0.33, 0.88, 5.05, 26.95, 32.81, 94.09]
Q_OCF = [-9.75, -7.88, -13.47, -12.24, -18.47, -18.03, -33.43, -17.87, -47.59]
Q_NETLOSS = [-27.3, -10.0, -12.3, -9.8, -24.7, -29.7, -41.4, -33.1, -48.5]

# ---- Consensus and peers (stockanalysis.com, retrieved 6 Oct 2026) ----
CONS_EPS_26 = -0.95; CONS_REV_26 = 2.74
CONS_TP = 75.78; CONS_TP_MED = 74.50; CONS_TP_RANGE = (14, 130); CONS_N = 25
SHORT_PCT = 18.1
# Announced customer capacity, GW: (label, GW, status per Oklo filings)
PIPE = [("Binding power purchase agreements", 0.0, "None disclosed; Oklo is negotiating them (10-Q)"),
        ("Meta, Pike County, Ohio", 1.2, "Prepayment agreement, 5 Jan 2026; no PPA; amount not disclosed"),
        ("Switch, master power agreement", 12.0, "Dec 2024; master agreements are non-binding (10-K risk factors)")]
PIPE_GW = sum(p[1] for p in PIPE)
# Peers: name, ticker, close 5 Oct, shares m, net cash US$m, announced GW, what they make, model
PEERS = [
    ("Oklo", "NYSE: OKLO", PRICE, None, None, PIPE_GW, "Aurora sodium-cooled fast reactors it intends to own; sells power"),
    ("X-energy", "Nasdaq: XE", 14.41, 406.37, 1610, 5.0, "Xe-100 gas-cooled reactors and TRISO fuel; Amazon up to 5 GW by 2039"),
    ("NuScale", "NYSE: SMR", 7.68, 429.72, 1070, 6.0, "77 MWe light-water modules (NRC approved May 2025); TVA and ENTRA1 up to 6 GW, non-binding"),
    ("NANO Nuclear", "Nasdaq: NNE", 15.51, 53.70, 579, None, "KRONOS microreactor and others; no gigawatt-scale agreement"),
]
DARLINGTON = (20.9, 1.2, 7.7, 0.3)   # C$bn, GW for four BWRX-300 units; C$bn and GW for the first (OPG, 8 May 2025)

# ---- MY assumptions: cash (US$m) ----
OCF26, CAPEX26 = 140, 450      # inside the 2026 guide
OCF27, CAPEX27 = 170, 550
H2_SPEND = (OCF26 + H1["ocf"]) + (CAPEX26 - H1["capex"])      # 397.6 in H2 2026
CASH_END26 = CASH_JUN + ATM_Q3_NET - H2_SPEND
CASH_SEP27 = CASH_END26 - 0.75 * (OCF27 + CAPEX27)
Q3_SPEND = H2_SPEND / 2
NETCASH_NOW = CASH_JUN + ATM_Q3_NET - Q3_SPEND                  # my estimate at 30 Sep 2026

# ---- MY assumptions: the plant (per 75 MWe Aurora) ----
UNIT_MW = 75
CF = 0.90                      # capacity factor
OPEX_MWH = 35                  # US$/MWh, operations, fuel, insurance, decommissioning fund
ESC = 0.02                     # price and cost escalation a year
LIFE = 40                      # years
R_PLANT = 0.08                 # discount rate for an operating, contracted plant
R_DEV = 0.10                   # discount rate from first power back to October 2027
INL_REM = 400                  # US$m Aurora-INL capex still to spend after Sep 2027
INL_COD = 2028.5
CORP = [250] * 4 + [150] * 5   # US$m a year of corporate, fuel, recycling and isotope spending from Oct 2027
CORP_BEAR = [150] * 3          # wind-down if the first plant fails
META = {2030: 150, 2031: 225, 2032: 225, 2033: 300, 2034: 300}   # MW coming online; 1.2 GW by 2034 per Meta release
PIPE_YEARS = list(range(2033, 2041))                              # further units, MW a year
#         name,   price, capex/kW, P(first plant), MW a year after Meta, weight
SCEN = [
    ("Bear", 95, 10000, 0.0, 0, 0.25),
    ("Base", 110, 7500, 0.60, 300, 0.50),
    ("Bull", 125, 6000, 0.80, 900, 0.25),
]
SENS_PRICE = [95, 110, 125]
SENS_CAPEX = [6000, 7500, 10000]


def pvf(r=R_PLANT, g=ESC, n=LIFE):
    return (1 - ((1 + g) / (1 + r)) ** n) / (r - g)


def margin_mw(price):            # US$m a year per MW in the first year
    return 8760 * CF * (price - OPEX_MWH) / 1e6


def npv_mw(price, capex):        # US$m per MW at first power
    return margin_mw(price) * pvf() - capex / 1000


def disc(year):                  # from mid-year of first power back to Oct 2027
    return 1 / (1 + R_DEV) ** (year + 0.5 - 2027.75)


D_INL = 1 / (1 + R_DEV) ** (INL_COD - 2027.75)
S_META = sum(mw * disc(y) for y, mw in META.items())
S_RATE = sum(disc(y) for y in PIPE_YEARS)


def inl_npv(price):
    return margin_mw(price) * UNIT_MW * pvf() - INL_REM


def pv_costs(costs):
    return sum(c / (1 + R_DEV) ** (i + 0.5) for i, c in enumerate(costs))


PV_CORP = pv_costs(CORP)
PV_CORP_BEAR = pv_costs(CORP_BEAR)


def fleet(price, capex, p, rate):
    return p * (inl_npv(price) * D_INL + max(0, npv_mw(price, capex)) * (S_META + rate * S_RATE))


def value(price, capex, p, rate):
    if p == 0:
        return (CASH_SEP27 - PV_CORP_BEAR) / FD
    return (fleet(price, capex, p, rate) + CASH_SEP27 - PV_CORP) / FD


def gw_2040(rate):
    return (UNIT_MW + sum(META.values()) + rate * len(PIPE_YEARS)) / 1000


VALS = [value(*s[1:5]) for s in SCEN]
WEIGHTED = sum(v * s[5] for v, s in zip(VALS, SCEN))
B = SCEN[1]
BASE_VALUE = VALS[1]
BASE_FLEET = fleet(*B[1:5])
GRID = [[value(pr, cx, B[3], B[4]) for pr in SENS_PRICE] for cx in SENS_CAPEX]
# What the price needs, holding the other base inputs
NEED_FLEET = PRICE * FD - CASH_SEP27 + PV_CORP
NEED_RATE = ((NEED_FLEET / B[3] - inl_npv(B[1]) * D_INL) / npv_mw(B[1], B[2]) - S_META) / S_RATE
NEED_GW = gw_2040(NEED_RATE)
NEED_NPV_MW = (NEED_FLEET / B[3] - inl_npv(B[1]) * D_INL) / (S_META + B[4] * S_RATE)
NEED_CAPEX = (margin_mw(B[1]) * pvf() - NEED_NPV_MW) * 1000
CASH_VALUE = CASH_SEP27 / FD                      # cash per share at Sep 2027, before any further spending
LCOE_BASE = (B[2] / 1000 / pvf(R_PLANT, 0, LIFE)) / (8760 * CF / 1e6) + OPEX_MWH   # flat-price break-even, US$/MWh
BREAKEVEN_CAPEX = margin_mw(B[1]) * pvf() * 1000                                  # US$/kW at the base price
REVISIT_LONG = BASE_VALUE                  # price at which the base case is no longer below the price
REVISIT_SHORT = WEIGHTED / 0.60            # price at which even the weighted value is 40% below it
MCAP = PRICE * SH_SEP
EV = MCAP - NETCASH_NOW


def peer_ev(p):
    if p[0] == "Oklo":
        return EV
    return p[2] * p[3] - p[4]


PEER_EV = [peer_ev(p) for p in PEERS]
PEER_EV_GW = [(ev / p[5] / 1000 if p[5] else None) for ev, p in zip(PEER_EV, PEERS)]
DARL_KW = DARLINGTON[0] / DARLINGTON[1] * 1000    # C$ per kW, four units
DARL1_KW = DARLINGTON[2] / DARLINGTON[3] * 1000   # C$ per kW, first unit with shared costs
ATM_Q3_AVG = ATM_Q3_GROSS / ATM_Q3_SH
CASH_RISE_H1 = CASH_JUN - CASH_DEC25
H1_OUT = RAISED_H1_26 - CASH_RISE_H1
SH_RISE_2Y = SH_SEP / Q_SHARES[0] - 1
SH_RISE_25 = SH_SEP / SH_H[0] - 1

# ---- Share price, month-end close (Yahoo Finance, retrieved 6 Oct 2026). Listed as OKLO from 10 May 2024. ----
PX_LABELS = ["May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25",
             "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25",
             "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
PX = [10.07, 8.47, 9.10, 5.97, 8.09, 22.46, 23.54, 21.23, 41.61, 33.39, 21.63, 23.74, 52.72, 55.99, 76.59, 73.64,
      111.63, 132.77, 91.38, 71.76, 79.62, 62.95, 49.59, 72.50, 66.88, 52.33, 38.83, 40.57, 37.02, 35.97]

if __name__ == "__main__":
    print(f"cash Jun {CASH_JUN:.1f} Dec25 {CASH_DEC25:.1f} rise {CASH_RISE_H1:.1f} raised {RAISED_H1_26} out {H1_OUT:.1f}")
    print(f"ATM Q3 {ATM_Q3_SH:.3f}m gross {ATM_Q3_GROSS:.1f} avg {ATM_Q3_AVG:.2f} net {ATM_Q3_NET:.1f}; SH_SEP {SH_SEP:.2f} FD {FD:.2f}")
    print(f"H2 spend {H2_SPEND:.1f} cash end26 {CASH_END26:.1f} sep27 {CASH_SEP27:.1f} now {NETCASH_NOW:.1f}; mcap {MCAP:.0f} EV {EV:.0f}")
    print(f"pvf {pvf():.3f} margin/MW {margin_mw(110):.4f} npv/MW base {npv_mw(110, 7500):.3f} inl {inl_npv(110):.1f} D_INL {D_INL:.3f} S_META {S_META:.1f} S_RATE {S_RATE:.3f}")
    print(f"PV corp {PV_CORP:.1f} bear {PV_CORP_BEAR:.1f}; base fleet {BASE_FLEET:.0f}")
    for s, v in zip(SCEN, VALS):
        print(s[0], round(v, 2), f"{v / PRICE - 1:+.1%}", "GW2040", round(gw_2040(s[4]), 2), "npv/MW", round(npv_mw(s[1], s[2]), 2))
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.1f} short {REVISIT_SHORT:.1f}")
    print("grid", [[round(x, 2) for x in r] for r in GRID])
    print(f"need fleet {NEED_FLEET:.0f} rate {NEED_RATE:.0f} MW/yr GW2040 {NEED_GW:.1f}; need npv/MW {NEED_NPV_MW:.2f} capex {NEED_CAPEX:.0f}/kW")
    print(f"cash/share Sep27 {CASH_VALUE:.2f}; LCOE base {LCOE_BASE:.0f}; breakeven capex {BREAKEVEN_CAPEX:.0f}")
    print("peers EV", [round(x) for x in PEER_EV], "EV/GW", PEER_EV_GW)
    print(f"Darlington C$/kW fleet {DARL_KW:.0f} first {DARL1_KW:.0f}; share rise 2y {SH_RISE_2Y:.1%} since 2024 end {SH_RISE_25:.1%}")
    print("fall from high close", {k: f"{v[1] / v[0] - 1:.0%}" for k, v in PEER_FALL.items()})
