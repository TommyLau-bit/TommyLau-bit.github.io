"""SK hynix Inc. (KRX: 000660) initiation, draft of 2 Nov 2026. Single source of figures for charts, note and model.

Sources: SK hynix preliminary results releases (newsroom) of 23 Jan 2025 (FY24, as reprinted), 28 Jan 2026 (FY25), 23 Apr 2026
(Q1 26), 29 Jul 2026 (Q2 26) and 28 Oct 2026 (Q3 26); Form 6-K "Preliminary Results of Operations" of 28 Oct 2026; Q3 2026
earnings call, 28 Oct 2026 (transcripts: stockanalysis.com and The Motley Fool); Form F-1 prospectus (424B4) of 10 Jul 2026 for
2023 to 2025 and Q1 2026 income statements, revenue by product, customer concentration, share count, the Yongin plan and the
definition of custom HBM; Forms 6-K of 26 Oct 2026 (treasury share acquisition report; amended cancellation decision) and
28 Oct 2026 (cash dividend; FY26 shareholder return plan; new treasury share acquisition). Annual revenue and net income 2016 to
2020 from SK hynix's annual results releases; 2021 to 2025 from stockanalysis.com (S&P Global), matching the prospectus.
Prices: KRX regular session closes via Yahoo Finance, checked against stockanalysis.com and Naver's previous-close field
(Naver's daily list mixes in Nextrade after-hours prices from September 2026). SKHY ADS closes from Nasdaq.com. USD/KRW: Hana Bank notice rate via Naver Finance, 18:21 KST 2 Nov 2026.
Consensus: stockanalysis.com (S&P Global), retrieved 2 Nov 2026. Everything marked MINE is my own estimate.

Units: KRW trillion (tn) unless stated; shares in millions; per-share figures in KRW. Calendar year = fiscal year.
Income: I value on operating profit after a normal tax rate. Reported net profit swings with large finance items (Kioxia stake
gains, investment valuation losses, foreign exchange), so 2027 and later forecasts exclude non-operating items.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
DATE_LONG = "2 November 2026"
COMPANY = "SKHynix"
NAME = "SK hynix"
SLUG = "sk-hynix"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/sk-hynix"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="LONG",
    direction="LONG",
    target=2000000,                  # KRW per share; None for NO CALL
    conviction="Medium",
    draft=False,
)

# ---- Market data ----
PRICE = 1472000.0       # KRX regular-session close, 2 Nov 2026 (Yahoo Finance and stockanalysis.com; Naver's 1,479,000 includes Nextrade after-hours trades)
PRICE_DATE = "2 November 2026"
HI_CLOSE = (2919000.0, "22 June 2026")    # highest close of the past year
HI52 = (2987000.0, "25 June 2026")        # intraday high, regular session
LO_CLOSE = (519000.0, "25 November 2025")
LO52 = (501000.0, "26 November 2025")
PRICE_DEC25 = 651000.0  # close, 30 Dec 2025 (last session of 2025)
PX_OCT30 = 1418000.0    # KRX close, 30 Oct 2026 (Yahoo Finance, stockanalysis.com; Naver's previous-close field agrees)
FX = 1341.00            # KRW per US$, Hana Bank notice rate, 18:21 KST 2 Nov 2026
FX_PREV = FX - 5.20     # previous notice (change of +5.20 reported with the 2 Nov rate), used for 30 Oct
ADS_OCT30 = 149.21      # SKHY close, Nasdaq, 30 Oct 2026; one ADS = one tenth of a common share (prospectus)
ADS_PREMIUM = ADS_OCT30 * 10 / (PX_OCT30 / FX_PREV) - 1
PX_LABELS = ['Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24',
             'Sep 24', 'Oct 24', 'Nov 24', 'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25',
             'Sep 25', 'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26',
             'Sep 26', 'Oct 26', '2 Nov 26']
PX = [114700, 116300, 133900, 141500, 134700, 156200, 183000, 174200, 189200, 236500, 194600, 173700,
      174600, 186300, 159900, 173900, 199200, 190200, 190700, 177500, 204500, 292000, 273500, 269000,
      347500, 559000, 530000, 651000, 909000, 1061000, 807000, 1286000, 2333000, 2650000, 1718000, 1674000,
      1776000, 1418000, 1472000]

# ---- Shares (Forms 6-K, 26 and 28 Oct 2026; prospectus, 10 Jul 2026) ----
SH = 14_103_466_480_000 / 20_000 / 1e6           # 705.17m: Q3 dividend total / KRW 20,000 per share = shares entitled
SH_PRE_IPO = 711.0755   # m, outstanding at the prospectus date
IPO_SH = 17.79          # m, new shares sold as ADSs, July 2026 (US$26.5bn gross)
CANCEL = 23.693272      # m, bought 20 Aug to 21 Oct 2026 for KRW 40.004tn, cancellation set for 5 Nov 2026
TREASURY = 25.319041    # m, treasury shares held at 26 Oct 2026 (3.47%)
BUY_OCT = 9.031         # KRW tn of that buyback executed in October 2026, after the 30 Sep balance sheet (6-K, 26 Oct)
BUY_Q4 = 20.0           # KRW tn new buyback, 29 Oct 2026 to 28 Jan 2027: about 10 to cancel, about 10 for staff compensation
STAFF_BUY = 10.0        # KRW tn of that for executive and employee compensation (a cost to holders, MINE treatment)
DPS_Q3 = 20000          # KRW: 10,000 regular + 10,000 special (Kioxia gains); record date 30 Nov 2026
RETURN_26 = 100.0       # about KRW 100tn FY26 shareholder return: >=30 dividends, >=60 buyback and cancellation
MCAP = PRICE * SH / 1e6  # KRW tn

# ---- Balance sheet, 30 Sep 2026 (Q3 release) ----
CASH = 114.5
DEBT = 15.8
NET_CASH = 98.7
NET_CASH_Q2 = 69.4

# ---- Consensus and peers (stockanalysis.com, S&P Global; retrieved 2 Nov 2026) ----
CONS_EPS_26 = 358671.68   # 37 analysts; range 268,436 to 426,371
CONS_EPS_27 = 527160.0    # shown as 527.16K
CONS_REV_26 = 363.55
CONS_REV_27 = 576.17
CONS_TP = 3157409.0       # average target, 41 analysts; range 1,575,000 to 4,700,000
CONS_TP_RANGE = (1575000.0, 4700000.0)
PEERS = [  # company, listing, price, currency, consensus EPS (year ending in 2027), year, what they make, price date
    ("Samsung Electronics", "KRX: 005930", 229000.0, "KRW", 75630.0, "CY2027", "DRAM, HBM, NAND, logic, phones", "2 Nov close"),
    ("Micron", "Nasdaq: MU", 884.74, "US$", 176.50, "FY to Aug 2027", "DRAM, HBM, NAND", "30 Oct close"),
]

# ---- Annual history: revenue and net income, KRW tn ----
YRS10 = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
REV10 = [17.198, 30.109, 40.445, 26.991, 31.900, 42.998, 44.622, 32.766, 66.193, 97.147]
NI10 = [2.960, 10.642, 15.540, 2.009, 4.759, 9.602, 2.230, -9.112, 19.789, 42.919]
CYC_NM = sum(NI10) / sum(REV10)
PEAK18_NM = NI10[2] / REV10[2]
OP24, OP25 = 23.467, 47.206
DRAM = {"2023": 20.769, "2024": 44.732, "2025": 74.904, "Q1 25": 14.037, "Q1 26": 40.659}
NAND = {"2023": 9.653, "2024": 19.274, "2025": 20.690, "Q1 25": 3.229, "Q1 26": 11.574}
DA25 = 12.664 + 0.831    # depreciation 12.664 + amortisation 0.831 (prospectus notes)
CAPEX = {"2023": 8.325, "2024": 15.946, "2025": 27.519, "Q1 26": 7.657}
EPS25 = 60377.79         # stockanalysis.com
TOP_CUST = dict(y2025=0.239, q1_26=(0.148, 0.124))   # largest customer 23.9% of 2025; two largest 14.8% and 12.4% of Q1 2026
US_SHARE = dict(y2025=0.688, q1_26=0.647); CN_SHARE = dict(y2025=0.197, q1_26=0.243)

# ---- Quarterly history, KRW tn (releases; Q3 2026 also Form 6-K) ----
QL = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
Q_REV = [12.4296, 16.4233, 17.5731, 19.7670, 17.6391, 22.2320, 24.4489, 32.8267, 52.5763, 79.3187, 104.6155]
Q_OP = [2.8860, 5.4685, 7.0300, 8.0828, 7.4405, 9.2129, 11.3834, 19.1696, 37.6103, 60.5426, 83.3338]
Q_NI = [None, None, None, None, 8.1082, 6.9962, 12.5975, 15.2460, 40.3459, 93.9226, 39.7756]
Q3_PRETAX = 50.7085
Q3_NONOP = 32.6; Q3_FX_LOSS = 11.6; Q3_INV_LOSS = 22.9
Q3_DA = 4.3; Q3_EBITDA = 87.7
YTD26_NI_CTRL = 173.684804   # profit attributable to controlling interests, Q1 to Q3 2026 (6-K)
YTD26_REV = 236.510516; YTD26_OP = 181.486709
# Q3 2026 call: DRAM bits about +10% on Q2, ASP up high 20s %; NAND bits down slightly, ASP up mid 20s %.
# Q4 2026 guide: DRAM bits up mid 20s %, NAND bits up mid single digits. 2027 demand growth: DRAM mid 20s %, NAND high teens %.
# LTAs with 14 customers cover more than 50% of 2027 and 2028 capacity, generally five years, prices within agreed ranges,
# safeguards such as deposits. HBM4 to pass HBM3E in shipments and revenue in Q4 2026. HBM4E samples shipped in Q2 2026.
LTA_N = 14

# ---- HBM: how much of the business it is (all MINE except where marked) ----
# Industry HBM revenue, US$bn: the same path as my Micron note, so the two notes agree: about 35 in 2025 growing about 40% a
# year (Micron, 17 Dec 2025: about 35 in 2025 to about 100 in 2028), so about 49 in 2026 and 69 in 2027. Gartner, in SK hynix's
# prospectus, has 33 in 2025 and 86 in 2027; on 86, 2027 HBM would be about 10.7% of my revenue rather than 8.6%. SK hynix share: IDC 56.4% in Q1 2026 (prospectus);
# my shares assume Samsung's HBM4 ramp takes some of it. Average USD/KRW MINE (about 1,420 in 2025; March 2026 1,523.5 and
# 2 July 2026 1,538.05 in the prospectus; 1,341 now).
HBM_YEARS = ["2025", "2026E", "2027E"]
HBM_TAM = [35.0, 49.0, 69.0]   # Micron's path, as in my Micron note; Gartner's 2027 forecast (86) is higher
HBM_SHARE = [0.58, 0.55, 0.50]
HBM_FX = [1420.0, 1460.0, FX]
GARTNER_27 = 86.0
HBM_OPM26 = 0.60        # MINE: HBM operating margin in 2026, below the company's because HBM prices were set a year ahead


def hbm_rev():
    return [t * s * f / 1000 for t, s, f in zip(HBM_TAM, HBM_SHARE, HBM_FX)]


HBM_REV = hbm_rev()      # KRW tn

# ---- MY forecasts ----
TAX = 0.22              # MINE: effective rate 21.8% in Q1 2026 (prospectus), about 21.6% in Q3 2026 (pre-tax 50.7, net 39.8)
Q4_REV = 128.0          # MINE: consensus implies about 127 (363.55 less 236.51 reported)
Q4_OPM = 0.80           # MINE: Q3 80%
REV26 = YTD26_REV + Q4_REV
OP26 = YTD26_OP + Q4_REV * Q4_OPM
NI26 = YTD26_NI_CTRL + Q4_REV * Q4_OPM * (1 - TAX)   # reported to Q3 (with finance items) plus my Q4 on operations only
EPS26 = NI26 / SH * 1e6
R27 = 540.0             # MINE: 2027 revenue (consensus 576.17)
OPM27 = 0.76            # MINE
G28 = -0.10             # MINE: 2028 revenue change
OPM28 = 0.68            # MINE
DA_Q4 = 4.6; DA27 = 22.0          # MINE (Q3 2026 D&A 4.3; 2025 13.5)
CAPEX_Q4 = 14.0; CAPEX27 = 75.0   # MINE: 2027 "to increase significantly compared to 2026"; the 30%-of-sales cap allows far more
WC_Q4 = 5.0; WC27 = 10.0          # MINE
HBM_REV26_SHARE = HBM_REV[1] / REV26
HBM_REV27_SHARE = HBM_REV[2] / R27
HBM_OP26_SHARE = HBM_REV[1] * HBM_OPM26 / OP26


def year(r27=R27, om27=OPM27, g28=G28, om28=OPM28):
    ni27 = r27 * om27 * (1 - TAX)
    r28 = r27 * (1 + g28)
    ni28 = r28 * om28 * (1 - TAX)
    fcf_q4 = Q4_REV * Q4_OPM * (1 - TAX) + DA_Q4 - CAPEX_Q4 - WC_Q4
    fcf27 = ni27 + DA27 - CAPEX27 - WC27
    nc = NET_CASH - BUY_OCT - STAFF_BUY + fcf_q4 + 0.75 * fcf27   # net cash at 30 Sep 2027, before dividends and cancellations
    return dict(ni27=ni27, eps27=ni27 / SH * 1e6, r28=r28, ni28=ni28, eps28=ni28 / SH * 1e6,
                fcf_q4=fcf_q4, fcf27=fcf27, nc=nc, ncps=nc / SH * 1e6)


BASE_Y = year()
NI27, EPS27, REV28, EPS28 = BASE_Y["ni27"], BASE_Y["eps27"], BASE_Y["r28"], BASE_Y["eps28"]
FCF_Q4, FCF27, NC_SEP27, NC_PS = BASE_Y["fcf_q4"], BASE_Y["fcf27"], BASE_Y["nc"], BASE_Y["ncps"]

# ---- Normal (mid-cycle) earnings: the same method and the same three normal cases as my Micron note ----
BASE_REV = Q_REV[6] + Q_REV[7] + Q_REV[8] + Q_REV[9]   # four quarters to June 2026, the period nearest Micron's FY26
BITS = 1.20; N_YEARS = 4
PF = 0.55; NM = 0.30; MULT = 12; RATE = 0.10
W_UP = (0.25, 1.0, 0.5)  # MINE: Q4 2027 share of the 2027 excess (undiscounted); 2028 excess; half again in 2029
GROWTH_F = BITS ** N_YEARS


def normal_rev(pf=PF):
    return BASE_REV * GROWTH_F * pf


def normal_eps(pf=PF, nm=NM):
    return normal_rev(pf) * nm / SH * 1e6


def value(n, mult=MULT, y=None, w=W_UP):
    y = BASE_Y if y is None else y
    exc = w[0] * (y["eps27"] - n) + w[1] * (y["eps28"] - n) / (1 + RATE) + w[2] * (y["eps28"] - n) / (1 + RATE) ** 2
    return dict(nc=y["ncps"], exc=exc, term=n * mult, value=y["ncps"] + exc + n * mult)


N_BASE = normal_eps()
#        name, price factor, net margin, multiple, 2027 rev, 2027 OPM, 2028 change, 2028 OPM, weights, prob
SCEN = [
    ("Bear", 0.40, 0.19, 10, 460.0, 0.70, -0.35, 0.45, (0.25, 1.0, 0.0), 0.25),
    ("Base", PF, NM, MULT, R27, OPM27, G28, OPM28, W_UP, 0.50),
    ("Bull", 0.70, 0.40, 14, 600.0, 0.80, 0.05, 0.78, (0.25, 1.0, 1.0), 0.25),
]


def scen(s):
    y = year(s[4], s[5], s[6], s[7])
    n = normal_eps(s[1], s[2])
    v = value(n, s[3], y, s[8])
    return dict(n=n, nrev=normal_rev(s[1]), eps27=y["eps27"], eps28=y["eps28"], **v)


SV = [scen(s) for s in SCEN]
VALS = [v["value"] for v in SV]
WEIGHTED = sum(v * s[9] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
UP_BASE = BASE_VALUE / PRICE - 1
RULE = "LONG" if UP_BASE >= 0.15 else ("SHORT" if UP_BASE <= -0.25 else "NO CALL")

# Sensitivity: normal net margin (rows) against the multiple (columns)
SENS_NM = [0.22, NM, 0.38]
SENS_X = [10, MULT, 14]
VGRID = [[value(normal_eps(PF, m), x)["value"] for x in SENS_X] for m in SENS_NM]

# What the price implies (linear in n, solved exactly)
_k = W_UP[0] + W_UP[1] / (1 + RATE) + W_UP[2] / (1 + RATE) ** 2
_c = W_UP[0] * EPS27 + (W_UP[1] / (1 + RATE) + W_UP[2] / (1 + RATE) ** 2) * EPS28
NEED_N = (PRICE - NC_PS - _c) / (MULT - _k)
NEED_NM = NEED_N * SH / 1e6 / normal_rev()
NEED_N_NOCASH = (PRICE - _c) / (MULT - _k)          # if the cash is spent and earns nothing
NEED_NM_NOCASH = NEED_N_NOCASH * SH / 1e6 / normal_rev()
REVISIT_HI = BASE_VALUE / 1.15     # above this price the base is less than 15% above: back to no call
WRONG_PX = None

# ---- Value and multiples ----
EV = MCAP - NET_CASH
PE25 = PRICE / EPS25
PE26, PE27, PE28 = PRICE / EPS26, PRICE / EPS27, PRICE / EPS28
PEC26, PEC27 = PRICE / CONS_EPS_26, PRICE / CONS_EPS_27
PE_NORMAL = PRICE / N_BASE
PEER_PE = [(p[0], p[2] / p[4]) for p in PEERS]
OFF_HIGH = PRICE / HI_CLOSE[0] - 1
SINCE_DEC25 = PRICE / PRICE_DEC25 - 1
NC_NOW_PS = (NET_CASH - BUY_OCT) / SH * 1e6
TP_VS = CALL["target"] / PRICE - 1 if CALL["target"] else None

if __name__ == "__main__":
    print(f"SH {SH:.3f}m  mcap {MCAP:.1f}tn = US${MCAP / FX * 1000:.0f}bn; EV {EV:.1f}; ADS premium {ADS_PREMIUM:+.1%}")
    print(f"HBM rev {[round(x, 1) for x in HBM_REV]}; share of 2025 rev {HBM_REV[0] / REV10[-1]:.1%} of DRAM {HBM_REV[0] / DRAM['2025']:.1%};"
          f" 2026 {HBM_REV26_SHARE:.1%}; 2027 {HBM_REV27_SHARE:.1%}; HBM OP share 26 {HBM_OP26_SHARE:.1%}")
    print(f"2026 rev {REV26:.1f} (cons {CONS_REV_26}) OP {OP26:.1f} NI {NI26:.1f} EPS {EPS26:,.0f} (cons {CONS_EPS_26:,.0f}, {EPS26 / CONS_EPS_26 - 1:+.1%})")
    print(f"2027 rev {R27} (cons {CONS_REV_27}, {R27 / CONS_REV_27 - 1:+.1%}) NI {NI27:.1f} EPS {EPS27:,.0f} ({EPS27 / CONS_EPS_27 - 1:+.1%}); 2028 rev {REV28:.1f} EPS {EPS28:,.0f}")
    print(f"FCF Q4 {FCF_Q4:.1f} 27 {FCF27:.1f}; NC Sep27 {NC_SEP27:.1f} = {NC_PS:,.0f}/sh; now {NC_NOW_PS:,.0f}/sh")
    print(f"base rev {BASE_REV:.2f}; normal rev {normal_rev():.1f} EPS {N_BASE:,.0f}")
    for s, v in zip(SCEN, SV):
        print(s[0], {k: round(x) if abs(x) > 100 else round(x, 2) for k, x in v.items()}, f"{v['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:,.0f} ({WEIGHTED / PRICE - 1:+.1%}); base {BASE_VALUE:,.0f} ({UP_BASE:+.1%}) rule {RULE}")
    print("grid", [[round(v / 1000) for v in r] for r in VGRID], sum(v > PRICE for r in VGRID for v in r))
    print(f"need N {NEED_N:,.0f} nm {NEED_NM:.1%}; no-cash N {NEED_N_NOCASH:,.0f} nm {NEED_NM_NOCASH:.1%}; revisit hi {REVISIT_HI:,.0f}")
    print(f"PE25 {PE25:.1f} PE26 {PE26:.1f} PE27 {PE27:.1f} PE28 {PE28:.1f} cons26 {PEC26:.1f} cons27 {PEC27:.2f} normal {PE_NORMAL:.1f}")
    print("peers", [(n, round(x, 2)) for n, x in PEER_PE])
    print(f"cycle nm {CYC_NM:.1%} peak18 {PEAK18_NM:.1%}; off high {OFF_HIGH:+.1%}; since dec {SINCE_DEC25:+.0%}")
