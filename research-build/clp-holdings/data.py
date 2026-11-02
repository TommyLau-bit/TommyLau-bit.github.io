"""CLP Holdings Limited (HKEX: 0002) initiation, drafted 2 Nov 2026. Single source of figures for charts, note and model.

Year end 31 December. HK$ million unless stated.
Sources (HKEXnews, CLP Holdings stock code 00002, and CLP Power Hong Kong):
- Annual results announcement 2025, 26 Feb 2026 (2026022600152): operating earnings by segment, Hong Kong energy
  business 9,312 and related 232, Chinese Mainland 1,598, Australia 85, India 221, Taiwan Region and Southeast Asia 179,
  other Hong Kong (76), unallocated finance income 44, unallocated expenses (910); operating earnings before fair value
  movements 10,685 (2024: 10,949); total earnings 10,468; dividends HK$3.20 (2024: HK$3.15); data centre sales +7.5%;
  three 132 kV data centre substations in 2025, six since 2024, three in the 2018 to 2023 plan; segment capital
  additions Hong Kong 10,639 (2024: 11,378); 2,526,450,570 shares in issue.
- 2025 results presentation, 26 Feb 2026 (2026022600162): SoC capex HK$10.6bn (generation 2.6, T&D and services 8.0);
  2024 to 2028 Development Plan HK$52.9bn, 72% transmission and distribution; six data centres energised in 2024 to
  2025 and an additional 12 data centre substations planned by 2028.
- Interim results 2026, 6 Aug 2026 (2026080600235): operating earnings before fair value movements 5,733 (H1 2025:
  5,227); Hong Kong energy business 4,736 and related 94; data centre sales +11.8%, 7.1% of sales; two substations of
  260 MVA, eight in the plan period, one more targeted in H2; borrowings 14,628 + 52,015; cash 4,401.
- Quarterly statement January to September 2026, 12 Oct 2026 (2026101200581): data centre sales +12.8%, 6.6% of
  28,131 GWh; Sandy Ridge operations targeted in phases from mid-2027; third interim dividend HK$0.63; Average Net
  Tariff in October 4.8% above January.
- CLP Power Hong Kong US$4.5bn MTN offering circular, 1 Apr 2026 (2026040100797): permitted return 8% of average net
  fixed assets; SoC statements 2023 to 2025 (permitted return 10,858 / 11,271 / 11,621; net return after CESF 9,580 /
  9,651 / 10,321; CLP Power's share 8,612 / 8,716 / 9,349; SoC depreciation 5,380 / 5,683 / 5,832); CAPCO 70% owned;
  SoC to 31 Dec 2033; interim review every five years; development plan review when a major expansion is proposed;
  about HK$38bn of T&D in the plan.
- CLP 2023 annual results, 26 Feb 2024 (2024022600164): "up to 18 large-scale data centres by 2028".
- LegCo Panel on Environmental Affairs paper CB(1)1046/2023(02), 28 Nov 2023: CLP Development Plan slides, basic
  tariff path. Government release of 28 Nov 2023: HK Electric's plan HK$22.0bn.
Prices: Yahoo Finance 0002.HK monthly history page and stockanalysis.com daily history, read 2 Nov 2026 (the Yahoo
chart API returned "Too Many Requests"). Consensus and peer multiples: stockanalysis.com (S&P Global data), read
2 Nov 2026; price targets last updated 17 Sep 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "CLPHoldings"
SLUG = "clp-holdings"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/clp-holdings"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call (Tommy Lau, 2 Nov 2026). Rebuild = edit this dict only. ----
CALL = dict(
    banner="NO CALL",
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data ----
PRICE = 77.75               # HKEX close, Monday 2 Nov 2026 (stockanalysis.com daily history; Yahoo quote page agrees)
PRICE_DATE = "2 November 2026"
HI_CLOSE = 79.80            # highest close of the past year, 21 Aug 2026 (intraday high also 79.80, 21 and 24 Aug)
LO_INTRA_52W = 66.25        # 52-week intraday low, November 2025
PX_DEC25 = 69.40            # close 31 Dec 2025
SHARES = 2526.45057         # m, shares in issue (unchanged through 12 Oct 2026)
CASH = 4401.0               # 30 Jun 2026
DEBT = 14628.0 + 52015.0    # bank loans and other borrowings, current + non-current, 30 Jun 2026
PERPS = 3872.0              # perpetual capital securities, 31 Dec 2025
DPS25 = 3.20
DPS26_DECL = 0.63 * 3       # first three interims of 2026

# ---- Reported earnings (operating earnings before fair value movements) ----
OPE = {"2024A": 10949.0, "2025A": 10685.0}
H1_OPE = {"2025": 5227.0, "2026": 5733.0}
HK_OPE = {"2024A": 8694.0 + 201.0, "2025A": 9312.0 + 232.0}     # Hong Kong energy business and related
H1_HK = {"2025": 4469.0 + 99.0, "2026": 4736.0 + 94.0}
SEG25 = [  # 2025 operating earnings before fair value movements, HK$m
    ("Hong Kong energy and related", 9312.0 + 232.0),
    ("Chinese Mainland", 1598.0),
    ("India", 221.0),
    ("Taiwan Region and SE Asia", 179.0),
    ("Australia", 85.0),
]
OTHER25 = -76.0 + 44.0 - 910.0   # other Hong Kong, unallocated finance income, unallocated Group expenses

# ---- Scheme of Control (offering circular, 1 Apr 2026) ----
PERMIT_RATE = 0.08
PERMITTED = {"2023": 10858.0, "2024": 11271.0, "2025": 11621.0}
NET_AFTER_CESF = {"2023": 9580.0, "2024": 9651.0, "2025": 10321.0}
CLP_SHARE_NR = {"2023": 8612.0, "2024": 8716.0, "2025": 9349.0}
SOC_DEP = {"2024": 5683.0, "2025": 5832.0}
ANFA = {y: v / PERMIT_RATE for y, v in PERMITTED.items()}       # implied average net fixed assets (derived)
R_NET25 = NET_AFTER_CESF["2025"] / ANFA["2025"]                 # net return after CESF over ANFA, 2025 (derived)
SHARE_NR = CLP_SHARE_NR["2025"] / NET_AFTER_CESF["2025"]        # CLP's share (CLP Power 100%, CAPCO 70%), derived
HK_OTHER = HK_OPE["2025A"] - CLP_SHARE_NR["2025"]              # rest of Hong Kong energy and related earnings, 2025

PLAN_CAPEX = 52900.0        # 2024 to 2028 Development Plan, approved Nov 2023
SOC_CAPEX = {"2024": 8010.0 + 2807.0 + 20.0, "2025": 10571.0}    # SoC capex, CLP Power + CAPCO + 70% of HKLTL (offering circular)
PLAN_LEFT = PLAN_CAPEX - SOC_CAPEX["2024"] - SOC_CAPEX["2025"]
CAPEX_E = PLAN_LEFT / 3      # MINE: the rest of the plan spread evenly over 2026 to 2028
DEP_GROWTH = 0.03            # MINE: SoC depreciation growth a year
DC_SALES_SHARE = 0.066       # data centres' share of CLP Power sales, nine months 2026
DC_SUBS_DONE, DC_SUBS_PLAN = 8, 18

# ---- MY estimates ----
R_NET_E = 0.0725            # MINE: net return after CESF on ANFA, 2026 to 2028 (2025: 7.11%; H1 2026 Hong Kong +5.7%)
YEARS = ["2026", "2027", "2028"]
DEP_E, ANFA_E = {}, {}
_prev_a, _prev_d = ANFA["2025"], SOC_DEP["2025"]
for y in YEARS:
    _prev_d = _prev_d * (1 + DEP_GROWTH)
    DEP_E[y] = _prev_d
    _prev_a = _prev_a + CAPEX_E - _prev_d
    ANFA_E[y] = _prev_a
HK_E = {y: ANFA_E[y] * R_NET_E * SHARE_NR + HK_OTHER for y in YEARS}
NONHK_E = {  # MINE: Mainland, Australia, India, Taiwan Region and SE Asia
    "2026": dict(cn=1650.0, au=220.0, ind=200.0, tw=200.0),
    "2027": dict(cn=1700.0, au=250.0, ind=220.0, tw=200.0),
    "2028": dict(cn=1750.0, au=200.0, ind=240.0, tw=200.0),
}
CORP_E = {  # MINE: other Hong Kong + unallocated finance income + unallocated Group expenses
    "2026": -40.0 + 20.0 - 820.0,
    "2027": -40.0 + 0.0 - 850.0,
    "2028": -40.0 + 0.0 - 870.0,
}
OVS_E = {y: sum(NONHK_E[y].values()) for y in YEARS}
OPE_E = {y: HK_E[y] + OVS_E[y] + CORP_E[y] for y in YEARS}
EPS_E = {y: OPE_E[y] / SHARES for y in YEARS}
EPS_A = {k: v / SHARES for k, v in OPE.items()}
HK_SHARE_E = {y: HK_E[y] / (HK_E[y] + OVS_E[y]) for y in YEARS}
HK_SHARE25 = HK_OPE["2025A"] / sum(v for _, v in SEG25)

# ---- Valuation: sum of the parts on 2028E, twelve months out ----
M_HK, M_OVS, M_CORP = 18.0, 10.0, 16.0     # MINE
M_OVS_ALT = 14.0                            # MINE: the alternative shown in the note
def sotp(hk, ovs, corp, mhk, movs, mcorp):
    return (hk * mhk + ovs * movs + corp * mcorp) / SHARES
BASE_VALUE = sotp(HK_E["2028"], OVS_E["2028"], CORP_E["2028"], M_HK, M_OVS, M_CORP)
BASE_ALT = sotp(HK_E["2028"], OVS_E["2028"], CORP_E["2028"], M_HK, M_OVS_ALT, M_CORP)
OVS_DROP25 = (1851.0 + 591.0 + 329.0 + 260.0) and (1598.0 + 85.0 + 221.0 + 179.0) / (1851.0 + 591.0 + 329.0 + 260.0) - 1
PER_BN = 1000 * R_NET_E * SHARE_NR          # HK$m of CLP earnings a year per HK$1bn of ANFA
PER_BN_EPS = PER_BN / SHARES
PER_BN_VALUE = PER_BN * M_HK / SHARES        # HK$ a share of value per HK$1bn of ANFA
ANFA_FOR_LONG = (PRICE * 1.15 - BASE_VALUE) / PER_BN_VALUE   # extra HK$bn of 2028 ANFA for a long
IMPLIED_HK_MULT = (PRICE * SHARES - OVS_E["2028"] * M_OVS - CORP_E["2028"] * M_CORP) / HK_E["2028"]
DC_ANFA_ILLUS = ANFA["2025"] * DC_SALES_SHARE / 1000         # HK$bn, illustration only
DC_EPS_ILLUS = DC_ANFA_ILLUS * PER_BN_EPS

# ---- Scenarios: name, extra 2028 ANFA (HK$bn), net return, overseas earnings, HK mult, overseas mult, corp mult, prob ----
SCEN = [
    ("Bear", 0.0, 0.0695, 1900.0, 15.0, 8.0, 13.0, 0.25),
    ("Base", 0.0, R_NET_E, OVS_E["2028"], M_HK, M_OVS, M_CORP, 0.50),
    ("Bull", 5.0, 0.0735, 2600.0, 20.0, 11.0, 18.0, 0.25),
]
SC = []
for s in SCEN:
    hk = (ANFA_E["2028"] + s[1] * 1000) * s[2] * SHARE_NR + HK_OTHER
    v = sotp(hk, s[3], CORP_E["2028"], s[4], s[5], s[6])
    SC.append(dict(name=s[0], extra=s[1], r=s[2], ovs=s[3], mhk=s[4], movs=s[5], mcorp=s[6], prob=s[7], hk=hk,
                   eps=(hk + s[3] + CORP_E["2028"]) / SHARES, value=v))
WEIGHTED = sum(x["value"] * x["prob"] for x in SC)
SENS_ANFA = [0.0, 10.0, 25.0]      # extra HK$bn of 2028 ANFA above my path
SENS_MULT = [16.0, 18.0, 20.0]     # Hong Kong multiple
def sens(extra, m):
    hk = HK_E["2028"] + extra * PER_BN
    return sotp(hk, OVS_E["2028"], CORP_E["2028"], m, M_OVS, M_CORP)
GRID = [[sens(a, m) for m in SENS_MULT] for a in SENS_ANFA]

# ---- Consensus and peers (stockanalysis.com, 2 Nov 2026) ----
CONS_EPS26, CONS_EPS27 = 4.82, 4.95
CONS_EPS25_SA = 4.32         # its 2025 figure; matches operating earnings after fair value movements (10,909 / 2,526)
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 79.60, 9, 69.50, 89.43
FWD_PE_SA, YIELD_SA = 17.18, 0.0412
PEERS = [  # company, ticker, forward P/E, trailing P/E, dividend yield, what they run, group
    ("CLP Holdings", "0002", 17.18, 18.12, 0.0412, "Kowloon and New Territories grid and generation (SoC); Mainland nuclear and renewables; EnergyAustralia; Apraava", "self"),
    ("HK Electric Investments", "2638", 16.27, 17.30, 0.0519, "Hong Kong Island and Lamma grid and generation (SoC), plan HK$22.0bn", "peer"),
    ("Power Assets", "0006", 7.75, 7.58, 0.0443, "33.37% of HK Electric Investments; overseas regulated networks", "distorted"),
    ("Towngas", "0003", 21.35, 21.31, 0.0484, "Hong Kong gas distribution; Mainland city gas", "peer"),
    ("CK Infrastructure", "1038", 10.61, 6.97, 0.0375, "Regulated networks in the UK, Australia and elsewhere", "distorted"),
]

CKI_PX, CKI_CONS27 = 69.65, 3.29    # stockanalysis.com, 2 Nov 2026
CKI_PE27 = CKI_PX / CKI_CONS27

# ---- Derived market figures ----
MCAP = PRICE * SHARES / 1000                 # HK$bn
NET_DEBT = DEBT - CASH
EV = MCAP + (NET_DEBT + PERPS) / 1000
TTM_OPE = (OPE["2025A"] - H1_OPE["2025"]) + H1_OPE["2026"]
PE_TTM = PRICE / (TTM_OPE / SHARES)
PE_E26, PE_E27, PE_E28 = (PRICE / EPS_E[y] for y in YEARS)
PE_C26, PE_C27 = PRICE / CONS_EPS26, PRICE / CONS_EPS27
YIELD25 = DPS25 / PRICE
YTD = PRICE / PX_DEC25 - 1
OFF_HIGH = PRICE / HI_CLOSE - 1
UP_BASE = BASE_VALUE / PRICE - 1
LONG_BELOW = BASE_VALUE / 1.15
SHORT_ABOVE = BASE_VALUE / 0.75
CONS_GAP27 = CONS_EPS27 / EPS_E["2027"] - 1
ANFA_CAGR = (ANFA_E["2028"] / ANFA["2025"]) ** (1 / 3) - 1

# ---- Price, month-end close (Yahoo Finance 0002.HK history page, read 2 Nov 2026) ----
PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24",
             "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
             "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26",
             "Oct 26", "2 Nov 26"]
PX = [62.15, 65.25, 62.35, 61.70, 61.85, 63.10, 67.05, 69.90, 68.85, 66.05, 65.30, 65.40, 64.65, 64.45, 63.40, 66.30,
      66.55, 66.10, 68.15, 65.85, 64.45, 66.30, 68.00, 69.40, 73.95, 74.20, 73.50, 75.10, 76.50, 73.20, 78.10, 78.70,
      76.70, 77.40, 77.75]

REVISIT_IF = ("A price below about HK$68.80, where my base value would sit 15 per cent above it, or Government approval "
              "of additions to the Development Plan worth about HK$22 billion of regulated assets by 2028, the amount "
              "my sensitivity says a long needs at today's multiple.")
WRONG_IF = ("The shares close above HK$90 or below HK$62 in October 2027, or Hong Kong energy and related operating "
            "earnings for 2026 come in below HK$9.8 billion, which would mean the regulated engine is growing more "
            "slowly than its asset base.")

if __name__ == "__main__":
    print("ANFA", {k: round(v) for k, v in ANFA.items()}, "r25", round(R_NET25, 5), "share", round(SHARE_NR, 4), "other", HK_OTHER)
    print("plan left", PLAN_LEFT, "capex/yr", round(CAPEX_E, 1), "dep", {k: round(v) for k, v in DEP_E.items()})
    print("ANFA_E", {k: round(v) for k, v in ANFA_E.items()}, "cagr", round(ANFA_CAGR, 4))
    print("HK_E", {k: round(v) for k, v in HK_E.items()}, "growth26", round(HK_E["2026"] / HK_OPE["2025A"] - 1, 4))
    print("OVS", OVS_E, "CORP", CORP_E)
    print("OPE_E", {k: round(v) for k, v in OPE_E.items()}, "EPS", {k: round(v, 3) for k, v in EPS_E.items()}, "EPS_A", {k: round(v, 3) for k, v in EPS_A.items()})
    print("H2 26 implied", round(OPE_E["2026"] - H1_OPE["2026"]), "vs H2 25", OPE["2025A"] - H1_OPE["2025"])
    print("HK share", {k: round(v, 3) for k, v in HK_SHARE_E.items()}, "2025", round(HK_SHARE25, 3))
    print(f"base {BASE_VALUE:.2f} up {UP_BASE:+.2%} long below {LONG_BELOW:.2f} short above {SHORT_ABOVE:.2f}")
    print(f"per bn {PER_BN:.2f}m eps {PER_BN_EPS:.4f} value {PER_BN_VALUE:.3f}; anfa for long {ANFA_FOR_LONG:.1f}bn; implied HK mult {IMPLIED_HK_MULT:.2f}")
    print(f"dc illus anfa {DC_ANFA_ILLUS:.1f}bn eps {DC_EPS_ILLUS:.3f} share of eps28 {DC_EPS_ILLUS / EPS_E['2028']:.1%}")
    for x in SC:
        print(x["name"], round(x["hk"]), round(x["eps"], 3), round(x["value"], 2), f"{x['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED / PRICE - 1:+.1%}")
    print("grid", [[round(v, 2) for v in r] for r in GRID])
    print("above", sum(v > PRICE for r in GRID for v in r), "15%", sum(v >= PRICE * 1.15 for r in GRID for v in r),
          "-25%", sum(v <= PRICE * 0.75 for r in GRID for v in r))
    print(f"mcap {MCAP:.1f} netdebt {NET_DEBT:.0f} EV {EV:.1f} ttm {TTM_OPE:.0f} pe ttm {PE_TTM:.1f} pe26 {PE_E26:.1f} pe27 {PE_E27:.1f} pe28 {PE_E28:.1f} c26 {PE_C26:.1f} c27 {PE_C27:.1f}")
    print(f"yield {YIELD25:.2%} ytd {YTD:.1%} off high {OFF_HIGH:.1%} cons gap27 {CONS_GAP27:+.1%}")
    import statistics
    print("peer median fwd (undistorted)", statistics.median(p[2] for p in PEERS if p[6] == "peer"), "yield all peers", statistics.median(p[4] for p in PEERS if p[6] != "self"))
    print(f"base alt {BASE_ALT:.2f} {BASE_ALT / PRICE - 1:+.1%} cki pe27 {CKI_PE27:.1f} ovs drop {OVS_DROP25:.1%}")
