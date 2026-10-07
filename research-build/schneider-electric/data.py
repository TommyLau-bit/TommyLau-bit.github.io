"""Schneider Electric SE (Euronext Paris: SU) initiation, draft of 7 Oct 2026. Single source of figures for charts, note and model.

Sources: Schneider Electric financial releases as filed with the AMF (echanges.dila.gouv.fr): Full Year 2024 Results
(20 Feb 2025, FCECO077559), Half Year 2025 Results (31 Jul 2025, FCECO079331), Third Quarter 2025 Revenues (30 Oct 2025,
FCECO080070), Full Year 2025 Results (26 Feb 2026) and its presentation, Q1 2026 Revenues (30 Apr 2026), Half Year 2026
Results (30 Jul 2026, FCECO082813). Capital Markets Day release and transcript (11 Dec 2025). "Schneider Electric to acquire
PTC" release (5 Oct 2026, FCECO083330; also PTC Form 8-K Ex. 99.1) and the transaction presentation of 5 Oct 2026.
Prices: Euronext Paris historical data (live.euronext.com, ISIN FR0000121972), retrieved 7 Oct 2026; Euronext returns the
last two years only. (Yahoo Finance chart API refused requests with "Too Many Requests" on 7 Oct 2026.) Consensus, targets
and peer EPS: stockanalysis.com (S&P Global Market Intelligence data), retrieved 7 Oct 2026. Everything marked MINE is my
own estimate. Calendar year = fiscal year. EUR million unless stated; per-share figures in EUR.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-07"
DATE_LONG = "7 October 2026"
COMPANY = "SchneiderElectric"
NAME = "Schneider Electric"
SLUG = "schneider-electric"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/schneider-electric"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",        # e.g. "INITIATE AT LONG" / "NO CALL" once Tommy decides
    direction="NO CALL",
    target=None,                    # EUR per share; None for NO CALL
    conviction="Medium",
    draft=False,
)

# ---- Market data (Euronext Paris historical data, retrieved 7 Oct 2026) ----
PRICE = 260.50          # close, 6 Oct 2026
PRICE_DATE = "6 October 2026"
PRICE_PRE_DEAL = 303.00 # close, 2 Oct 2026, the last close before the PTC announcement (5 Oct 2026)
PRICE_5OCT = 272.80     # close, 5 Oct 2026
LEGRAND = (144.55, 148.40)   # Legrand closes 2 Oct and 6 Oct 2026 (Euronext), a control for the sector move
HI_CLOSE = 311.00       # highest close of the past year, 12 Aug 2026
HI52 = 312.30           # intraday high of the past year, 13 Aug 2026
LO_CLOSE = 222.30       # lowest close of the past year, 21 Nov 2025
LO52 = 220.40           # intraday low of the past year, 21 Nov 2025
PRICE_DEC25 = 234.90    # close, 31 Dec 2025
PX_RESULTS = (256.80, 284.60)  # closes 29 Jul and 30 Jul 2026 (H1 results on 30 Jul, before the open)
PX_LABELS = ['Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25',
             'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26', '6 Oct 26']
PX = [237.2, 243.5, 240.9, 245.35, 233.95, 210.75, 204.2, 221.35, 225.8, 228.25, 210.05, 237.6,
      246.1, 231.0, 234.9, 242.3, 276.7, 229.1, 268.6, 269.95, 285.4, 289.6, 294.6, 292.0, 260.5]
# Oct 24 is the close on 31 Oct 2024; the last point is the 6 Oct 2026 close. Month-end closes from Euronext.

SHARES_OUT = 563.54     # m shares outstanding (stockanalysis.com, 7 Oct 2026)
SH_H126 = 2696 / 4.79   # m, adjusted net income / adjusted EPS, H1 2026 (implied diluted average)

# ---- Consensus and peers (stockanalysis.com, S&P Global data; retrieved 7 Oct 2026, prices are 6 Oct 2026 closes) ----
CONS_EPS_26 = 10.41     # adjusted EPS 2026, updated 25 Sep 2026 (before the PTC announcement)
CONS_EPS_27 = 12.38
CONS_REV_26 = 44900.0
CONS_TP = 327.49        # average target, 21 analysts, range 262 to 370, updated 25 Sep 2026
CONS_N = 21
PEERS = [  # company, listing, price, 2026 consensus EPS, currency, what they make, note
    ("Eaton", "NYSE: ETN", 445.09, 13.57, "US$", "Switchgear, UPS, power distribution, prefabricated electrical rooms", ""),
    ("Vertiv", "NYSE: VRT", 253.14, 6.74, "US$", "UPS, switchgear, prefabricated modules, liquid cooling", ""),
    ("ABB", "SIX: ABBN", 82.58, 3.19, "CHF", "Electrification, motion and automation", ""),
    ("Siemens", "Xetra: SIE", 278.55, 11.45, "EUR", "Automation, smart infrastructure, rail", "fiscal year to Sep 2026"),
    ("Legrand", "Euronext Paris: LR", 148.40, 6.01, "EUR", "Low voltage electrical products, data centre white space", ""),
]

# ---- Annual reported (Schneider releases), EUR m ----
YEARS_H = ["2024", "2025"]
REV_H = [38153.0, 40152.0]
REV_23 = 35902.0
ORG_H = [0.084, 0.089]
EBITA_H = [7083.0, 7520.0]
GM_H = [0.426, 0.421]
ADJ_NI_H = [4664.0, 4829.0]
EPS_H = [8.32, 8.59]
DPS_H = [3.90, 4.20]
FCF_H = [4216.0, 4635.0]
NETDEBT_H = [8147.0, 13721.0]
CAPEX_H = [1364.0, 1496.0]
AMORT_H = [406.0, 457.0]
FIN_H = [409.0, 519.0]
ADJ_TAX_H = [1451.0, 1541.0]
MINOR_H = [153.0, 174.0]
BACKLOG = (21.4, 25.4)  # EUR bn, end 2024 and end 2025 (FY25 presentation); >1 year 4.8 and 8.0
DCN_ORDERS = 0.30       # Data Center & Networks share of FY2025 orders (FY25 presentation)

# ---- Half years ----
H = dict(rev_h125=19336.0, rev_h126=21226.0, ebita_h125=3510.0, ebita_h126=4093.0, gm_h125=0.424, gm_h126=0.425,
         eps_h125=3.97, eps_h126=4.79, fcf_h126=1631.0, capex_h125=717.0, capex_h126=669.0, mix=-148.0,
         amort_h126=206.0, fin_h126=286.0, minor_h126=40.0, nd_h126=15360.0, org_h126=0.140)

# ---- Quarterly business model (releases): revenue, shares of the quarter (or of the year where only that is given),
#      organic growth. Q4 2025 shares are not disclosed; the Q4 release gives FY2025 shares. ----
QL = ["Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_REV = [10011.0, 9721.0, 11095.0, 9767.0, 11459.0]
Q_ORG = [0.083, 0.090, 0.107, 0.112, 0.165]
Q_SHARE = {"Products": [0.48, 0.48, None, 0.48, 0.47], "Systems": [0.33, 0.34, None, 0.33, 0.35],
           "Software & Services": [0.19, 0.18, None, 0.19, 0.18]}
Q_GROW = {"Products": [0.02, 0.03, 0.04, 0.09, 0.13], "Systems": [0.17, 0.19, 0.19, 0.16, 0.28],
          "Software & Services": [0.11, 0.08, 0.10, 0.09, 0.06]}
SYS_SHARE_FY = {"2024": 0.31, "2025": 0.34}
# Q2 2026 contribution to organic growth (my arithmetic on rounded shares of the Q2 2025 base)
Q2_BASE = Q_REV[0]
CONTRIB = {k: Q2_BASE * Q_SHARE[k][0] * Q_GROW[k][4] for k in Q_SHARE}
SYS_CONTRIB_SHARE = CONTRIB["Systems"] / sum(CONTRIB.values())
# H1 2026 Systems share: Q1 33% of 9,767 plus Q2 35% of 11,459 (rounded shares)
SYS_H126 = (Q_REV[3] * 0.33 + Q_REV[4] * 0.35) / (Q_REV[3] + Q_REV[4])

# ---- Guidance (H1 2026 release, 30 Jul 2026) and CMD targets (11 Dec 2025) ----
G26 = dict(org_lo=0.10, org_hi=0.13, m_lo=0.194, m_hi=0.197, ebita_lo=0.14, ebita_hi=0.19, fx=-450.0, tax=0.24)
CMD = dict(org_lo=0.07, org_hi=0.10, margin_bps=250, conversion=1.0, buyback=(2.5, 3.5), ss_share=0.25)
Q3_DATE = "16 October 2026"    # brought forward from 29 October (PTC release, 5 Oct 2026)

# ---- PTC (release and presentation of 5 Oct 2026; EUR/USD 1.1255 as of 2 Oct 2026) ----
PTC = dict(px_usd=205.0, eq_usd=22.6, ev_usd=23.7, eq_eur=20.1, ev_eur=21.1, rev25=2400.0, margin25=0.40,
           mult27=21.0, mult27_syn=13.0, cost_syn=250.0, rev_syn=800.0, one_off=250.0, cash=22000.0,
           equity=(5000.0, 6000.0), debt=(16000.0, 17000.0), premium=0.423, close="Q3 2027", ss_pf=0.24)
PTC_EBITA27 = PTC["ev_eur"] * 1000 / PTC["mult27"]          # implied 2027E adjusted EBITA, EUR m (about 1,005)
PTC_NETDEBT = (PTC["ev_eur"] - PTC["eq_eur"]) * 1000       # EUR m (about 1,000)
COGNITE = 3.1 / 1.1255 * 1000                               # EUR m, all-cash, agreed 30 Jun 2026
AIDASH = 0.35 * 0.9 / 1.1255 * 1000                         # EUR m, c.90% of a US$350m enterprise value
SHELLY = 1200.0     # EUR m, all-cash offer for Shelly Group, 24 Sep 2026 (AMF FCECO083243); closing expected by Q1 2027

# ---- MY assumptions: standalone Schneider ----
ORG26 = 0.12            # MINE: upper half of the 10 to 13% guide; H1 was +14.0%
M26 = 0.196             # MINE: inside the guided 19.4 to 19.7%
AMORT = [420.0, 400.0, 380.0]   # MINE: purchase accounting amortisation, 2026 to 2028 (H1 2026: 206)
FIN = [600.0, 650.0, 650.0]     # MINE: net financial expense (H1 2026: 286); Cognite debt from 2027
TAX = 0.24              # guided 23 to 25% for 2026; MINE for 2027 and 2028
MINOR = [90.0, 100.0, 110.0]    # MINE: associates and non-controlling interests (H1 2026: 40)
SH = [562.5, 560.5, 558.3]      # MINE: diluted shares, m; standalone buybacks of about EUR 0.6bn a year
ORG27, ORG28 = 0.09, 0.08       # MINE: inside the CMD's 7 to 10%
DM27, DM28 = 0.006, 0.005       # MINE: margin steps, about the CMD's 250bps over five years
MULT = 22               # MINE: P/E on 2028E, one year forward in October 2027

# ---- MY assumptions: PTC from closing (Q3 2027); first full year 2028 ----
PTC_G28 = 0.10          # PTC revenue and ARR guided by broker consensus at about 10% a year
SYN28 = 80.0            # MINE: about a third of the EUR 250m cost synergies in the first full year
RATE = 0.035            # MINE: blended cost of the EUR 16 to 17bn of new debt
NEW_DEBT = 16500.0      # midpoint
ABO = 5500.0            # midpoint of the equity raise
ABO_PX = 250.0          # MINE: placement price, about 4% below the 6 Oct close
NEW_SH = ABO / ABO_PX   # m new shares
BUYBACK_SAVED = 1200.0  # MINE: standalone buybacks paused in 2027 and 2028 (EUR 0.6bn a year)
PPA = 600.0             # MINE: annual amortisation of PTC purchase accounting intangibles; not disclosed
SH_PTC28 = SH[0] - 0.6 + NEW_SH   # no buybacks in 2027 and 2028


def standalone(org27=ORG27, org28=ORG28, dm27=DM27, dm28=DM28):
    rev26 = REV_H[1] * (1 + ORG26) + G26["fx"]
    e26 = rev26 * M26
    rev27 = rev26 * (1 + org27); m27 = M26 + dm27; e27 = rev27 * m27
    rev28 = rev27 * (1 + org28); m28 = m27 + dm28; e28 = rev28 * m28
    ni = [(e - a - f) * (1 - TAX) - mi for e, a, f, mi in zip([e26, e27, e28], AMORT, FIN, MINOR)]
    eps = [n / s for n, s in zip(ni, SH)]
    return dict(rev=[rev26, rev27, rev28], m=[M26, m27, m28], ebita=[e26, e27, e28], ni=ni, eps=eps)


def with_ptc(st, syn=SYN28, ppa=PPA):
    ptc_ebita = PTC_EBITA27 * (1 + PTC_G28) + syn
    interest = NEW_DEBT * RATE - BUYBACK_SAVED * RATE   # the ~EUR 22bn cash consideration exceeds the EUR 21.1bn EV, so it covers PTC's debt
    add_pre = (ptc_ebita - interest) * (1 - TAX)
    ppa_at = ppa * (1 - TAX)
    ni = st["ni"][2] + add_pre - ppa_at
    eps = ni / SH_PTC28
    own_ppa_at = AMORT[2] * (1 - TAX)
    eps_pre = (ni + ppa_at + own_ppa_at) / SH_PTC28
    st_pre = (st["ni"][2] + own_ppa_at) / SH[2]
    return dict(ptc_ebita=ptc_ebita, interest=interest, add_pre=add_pre, ni=ni, eps=eps, eps_pre=eps_pre, st_pre=st_pre,
                rev=st["rev"][2] + PTC["rev25"] * (1 + PTC_G28) ** 3)


ST = standalone()
PT = with_ptc(ST)
REV26, REV27, REV28 = ST["rev"]
EBITA26, EBITA27, EBITA28 = ST["ebita"]
EPS26, EPS27, EPS28 = ST["eps"]
EPS28_PTC = PT["eps"]
ACCR_REPORTED = EPS28_PTC / EPS28 - 1          # on Schneider's adjusted EPS (after purchase accounting)
ACCR_PRE_PPA = PT["eps_pre"] / PT["st_pre"] - 1   # before purchase accounting, management's measure

#        name, org27, org28, dm27, dm28, PTC synergies 2028, PTC PPA, multiple, prob
SCEN = [
    ("Bear", 0.04, 0.03, 0.000, 0.000, 0.0, PPA, 18, 0.25),
    ("Base", ORG27, ORG28, DM27, DM28, SYN28, PPA, MULT, 0.50),
    ("Bull", 0.11, 0.10, 0.008, 0.008, 160.0, PPA, 25, 0.25),
]


def scen_value(s):
    st = standalone(s[1], s[2], s[3], s[4]); pt = with_ptc(st, s[5], s[6])
    return dict(eps_st=st["eps"][2], eps=pt["eps"], value=pt["eps"] * s[7], value_st=st["eps"][2] * s[7],
                rev=pt["rev"], m28=st["m"][2])


SV = [scen_value(s) for s in SCEN]
VALS = [v["value"] for v in SV]
WEIGHTED = sum(v * s[8] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
BASE_STANDALONE = SV[1]["value_st"]
# Sensitivity: 2028 adjusted EBITA margin (standalone) against the multiple, PTC included
SENS_M28 = [ST["m"][2] - 0.01, ST["m"][2], ST["m"][2] + 0.01]
SENS_X = [18, MULT, 26]


def grid_value(m28, x):
    st = standalone(ORG27, ORG28, DM27, m28 - M26 - DM27)
    return with_ptc(st)["eps"] * x


VGRID = [[grid_value(m, x) for x in SENS_X] for m in SENS_M28]
REVISIT_LONG = BASE_VALUE / 1.15     # price at or below which the base is 15% above (points long)
REVISIT_SHORT = BASE_VALUE / 0.75    # price at or above which the base is 25% below (points short)
REVISIT_EPS_LONG = PRICE * 1.15 / MULT    # 2028E EPS with PTC at which the base is 15% above the price
REVISIT_EPS_SHORT = PRICE * 0.75 / MULT   # and 25% below
WRONG_ORG = (SCEN_ORG_LO := 0.04, SCEN_ORG_HI := 0.11)   # organic growth, four quarters to Sep 2027: bear and bull 2027 cases

# What the price needs: 2028 EPS at the base multiple, and the organic growth that gives it (bisection, margins as base)
NEED_EPS = PRICE / MULT


def _eps_at(g):
    return with_ptc(standalone(g, g))["eps"]


lo, hi = -0.05, 0.15
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if _eps_at(mid) < NEED_EPS else (lo, mid)
NEED_ORG = round((lo + hi) / 2, 4)

# ---- Value, debt, multiples ----
MCAP = PRICE * SHARES_OUT / 1000            # EUR bn
MCAP_PRE = PRICE_PRE_DEAL * SHARES_OUT / 1000
MCAP_LOST = MCAP_PRE - MCAP
DROP = PRICE / PRICE_PRE_DEAL - 1
LEGRAND_CHG = LEGRAND[1] / LEGRAND[0] - 1
PE_C26, PE_C27 = PRICE / CONS_EPS_26, PRICE / CONS_EPS_27
PE_C27_PRE = PRICE_PRE_DEAL / CONS_EPS_27
PE26, PE27, PE28, PE28_PTC = PRICE / EPS26, PRICE / EPS27, PRICE / EPS28, PRICE / EPS28_PTC
PEER_PE = [(p[0], p[2] / p[3]) for p in PEERS]
import statistics
PEER_MED = statistics.median([x[1] for x in PEER_PE])
DEAL_COST_PS = BASE_STANDALONE - BASE_VALUE     # EUR a share, the deal's cost on my numbers at the base multiple
# Net debt path to closing, MINE (EUR m)
ND_END26 = H["nd_h126"] + COGNITE + AIDASH - 3400.0          # H2 2026 free cash flow about EUR 3.4bn (MINE)
ND_CLOSE_PRE = ND_END26 + SHELLY - 3300.0 + 2600.0            # 2027 to Q3: Shelly, FCF 3.3bn, dividend 2.6bn (MINE)
ND_CLOSE = ND_CLOSE_PRE + PTC["cash"] - ABO   # the cash consideration already covers PTC's net debt
LEV_25 = NETDEBT_H[1] / EBITA_H[1]
LEV_CLOSE = ND_CLOSE / (EBITA27 + PTC_EBITA27)
SINCE_DEC25 = PRICE / PRICE_DEC25 - 1
OFF_HIGH = PRICE / HI_CLOSE - 1

if __name__ == "__main__":
    print(f"2026 rev {REV26:,.0f} ebita {EBITA26:,.0f} eps {EPS26:.2f} (cons {CONS_EPS_26}, {EPS26/CONS_EPS_26-1:+.1%}); cons rev {CONS_REV_26}")
    print(f"2027 rev {REV27:,.0f} ebita {EBITA27:,.0f} m {ST['m'][1]:.1%} eps {EPS27:.2f} (cons {CONS_EPS_27}, {EPS27/CONS_EPS_27-1:+.1%})")
    print(f"2028 rev {REV28:,.0f} ebita {EBITA28:,.0f} m {ST['m'][2]:.1%} eps {EPS28:.2f}; with PTC {EPS28_PTC:.2f} ({ACCR_REPORTED:+.1%}); pre-PPA {PT['eps_pre']:.2f} vs {PT['st_pre']:.2f} ({ACCR_PRE_PPA:+.1%})")
    print(f"PTC ebita27 {PTC_EBITA27:.0f} ebita28 {PT['ptc_ebita']:.0f} interest {PT['interest']:.0f} add {PT['add_pre']:.0f}; new sh {NEW_SH:.1f} sh28 {SH_PTC28:.1f}; PTC nd {PTC_NETDEBT:.0f}")
    for s, v in zip(SCEN, SV):
        print(s[0], f"eps {v['eps']:.2f} st {v['eps_st']:.2f} value {v['value']:.1f} ({v['value']/PRICE-1:+.1%}) standalone {v['value_st']:.1f} m28 {v['m28']:.1%}")
    print(f"weighted {WEIGHTED:.1f} ({WEIGHTED/PRICE-1:+.1%}); base {BASE_VALUE:.1f} ({BASE_VALUE/PRICE-1:+.1%}); standalone {BASE_STANDALONE:.1f} ({BASE_STANDALONE/PRICE-1:+.1%}); deal cost/sh {DEAL_COST_PS:.1f}")
    print(f"revisit long <= {REVISIT_LONG:.1f}, short >= {REVISIT_SHORT:.1f}")
    print("grid", [[round(v) for v in r] for r in VGRID], [f"{m:.1%}" for m in SENS_M28])
    print(f"need eps {NEED_EPS:.2f} need org {NEED_ORG:.2%}")
    print(f"mcap {MCAP:.1f} pre {MCAP_PRE:.1f} lost {MCAP_LOST:.1f}; drop {DROP:+.1%}; legrand {LEGRAND_CHG:+.1%}")
    print(f"PE cons26 {PE_C26:.1f} cons27 {PE_C27:.1f} pre-deal27 {PE_C27_PRE:.1f}; mine 26 {PE26:.1f} 27 {PE27:.1f} 28 {PE28:.1f} 28ptc {PE28_PTC:.1f}")
    print("peers", [(n, round(x, 1)) for n, x in PEER_PE], "median", round(PEER_MED, 1))
    print(f"lev rise {LEV_CLOSE/LEV_25-1:+.1%}; revisit eps {REVISIT_EPS_LONG:.2f} {REVISIT_EPS_SHORT:.2f}"); print(f"nd end26 {ND_END26:.0f} pre-close {ND_CLOSE_PRE:.0f} close {ND_CLOSE:.0f}; lev25 {LEV_25:.2f} lev close {LEV_CLOSE:.2f}")
    print(f"Q2 contrib {CONTRIB} sys share {SYS_CONTRIB_SHARE:.1%}; H1 26 sys share {SYS_H126:.2%}; cognite {COGNITE:.0f} aidash {AIDASH:.0f}")
    print(f"since dec25 {SINCE_DEC25:+.1%} off high {OFF_HIGH:+.1%}; H1 shares {SH_H126:.1f}")
