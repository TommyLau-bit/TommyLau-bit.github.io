"""Samsung Electronics (KRX: 005930) initiation, draft of 2 Nov 2026. Single source of figures for charts, note and model.

Sources: Samsung Electronics earnings call decks ("conference_eng.pdf", Samsung IR) for 1Q, 2Q and 3Q 2026 and for 4Q of
2018 to 2025 (segment sales and operating profit, income statement, balance sheet, cash flow, shareholder return update);
3Q 2026 earnings call of 29 Oct 2026 (transcript, Investing.com) for bits, prices, HBM4, the 2027 HBM sell-out, long-term
contracts, the FX effect, capex and the foundry base die; LSE RNS filings of the GDRs (Investegate): 3Q 2026 dividend
(29 Oct 2026, KRW 30,003.0bn), FY2026 capex plan (29 Oct 2026, KRW 84.4tn), share repurchase results (12 Oct 2026),
cancellation decision (31 Mar 2026), 2026 half-year business report (31 Aug 2026: issued shares at 30 Jun 2026);
Samsung newsroom, 12 Feb 2026 (HBM4 shipments, 4nm base die, custom HBM samples in 2027, HBM sales to more than triple in
2026). Micron FQ4 2025 prepared remarks of 23 Sep 2025 ("We are partnering with TSMC for manufacturing the HBM4E base
logic die for both standard and customized products"). IDC HBM shares as quoted in SK hynix's prospectus (424B4, 10 Jul 2026). Annual revenue, operating income and net
income 2021 to 2025: stockanalysis.com (S&P Global), matching the decks.
Prices: KRX closes via Naver Finance to August 2026 and stockanalysis.com from September 2026 (Naver's daily list mixes in
Nextrade after-hours trades from September 2026). USD/KRW: Hana Bank notice rate via Naver, 2 Nov 2026.
Consensus: stockanalysis.com (S&P Global), retrieved 2 Nov 2026. Everything marked MINE is my own estimate.

Units: KRW trillion (tn) unless stated; shares in millions; per-share figures in KRW. Calendar year = fiscal year.
Method: a sum of the parts at about October 2027. Memory is valued with the same cycle method and normal cases as my
Micron and SK Hynix notes (net cash, plus earnings above normal still to come, plus 12 times normal earnings). The other
businesses are valued on normal operating profit after tax. One value per economic share: common and preferred shares
carry the same dividend (KRW 4,601 each for 3Q 2026) and near-identical EPS.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
DATE_LONG = "2 November 2026"
COMPANY = "SamsungElectronics"
NAME = "Samsung Electronics"
SLUG = "samsung-electronics"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/samsung-electronics"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="LONG",
    direction="LONG",
    target=270000,                 # KRW per common share; None for NO CALL
    conviction="Low",
    draft=False,
)

# ---- Market data ----
PRICE = 229000.0        # common, KRX regular-session close 2 Nov 2026 (stockanalysis.com; Naver's 229,500 includes Nextrade)
PRICE_P = 177000.0      # preferred (005935), same basis
PRICE_DATE = "2 November 2026"
HI_CLOSE = (362500.0, "18 June 2026")     # highest close of the past year (Naver, regular session before Sep 2026)
HI52 = (374500.0, "19 June 2026")         # intraday high
LO_CLOSE = (94800.0, "21 November 2025")
LO52 = (94500.0, "21 November 2025")
FX = 1341.70            # KRW per US$, Hana Bank notice rate, 2 Nov 2026
PX_LABELS = ['Sep 23', 'Dec 23', 'Mar 24', 'Jun 24', 'Sep 24', 'Dec 24', 'Mar 25', 'Jun 25', 'Sep 25', 'Oct 25', 'Nov 25',
             'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26', 'Oct 26', '2 Nov 26']
PX = [68400, 78500, 82400, 81500, 61500, 53200, 57800, 59800, 83900, 107500, 100500,
      119900, 160500, 216500, 167200, 220500, 317000, 334000, 262500, 260000, 268500, 225000, 229000]
PX_P = [54500, 62300, 68000, 63600, 50900, 44200, 47200, 49500, 66400, 84400, 75000,
        89200, 117400, 143800, 114000, 158300, 202500, 212000, 191000, 186500, 195200, 174100, 177000]
PREF_GAP = 1 - PRICE_P / PRICE
PREF_GAP_HIST = [("Sep 2023", 1 - 54500 / 68400), ("Dec 2024", 1 - 44200 / 53200)]

# ---- Shares ----
DIV_TOTAL = 30.003      # KRW tn, 3Q 2026 dividend (RNS, 29 Oct 2026), KRW 4,601 per common and preferred share
DPS_Q3 = 4601
SH_P = 802.371203       # m preferred issued and outstanding, no preferred in treasury (half-year report, 30 Jun 2026; RNS 12 Oct 2026: "Other shares 0")
SH_C_ISSUED = 5846.278608   # m common issued after the 2 Apr 2026 cancellation (half-year report, 30 Jun 2026)
SH_C_REC = DIV_TOTAL * 1e12 / DPS_Q3 / 1e6 - SH_P          # 5,718.6m common entitled at 30 Sep (check against the dividend total)
TREAS_C = 136.727099    # m common treasury shares after the buyback to 6 Oct 2026, 2.34% of common (RNS, 12 Oct 2026)
SH_C = SH_C_ISSUED - TREAS_C                               # 5,709.6m common outstanding after 6 Oct
SH = SH_C + SH_P                                           # economic shares
BUY_OCT = 2.5           # KRW tn: KRW 15tn programme (24 Aug to 6 Oct) less KRW 12.5tn paid in 3Q (DERIVED)
MCAP = (PRICE * SH_C + PRICE_P * SH_P) / 1e6               # KRW tn at market, both classes
MCAP_C_ONLY = PRICE * SH / 1e6                              # if the preferred traded at the common price

# ---- Balance sheet, 30 Sep 2026 (3Q deck, KRW tn) ----
CASH = 214.8
DEBT = 17.2
NET_CASH = 197.6
INVEST = 97.2           # "Investments" line
EQUITY = 614.1
RETURN_26 = (90.0, 110.0)   # estimated 2026 shareholder returns; KRW 35tn planned or done; 55 to 75 to come
CAPEX_26 = 84.4; CAPEX_9M = 56.9; CAPEX_DS_26 = 76.8

# ---- Consensus and peers (stockanalysis.com, S&P Global; retrieved 2 Nov 2026) ----
CONS_EPS_26 = 46173.60
CONS_EPS_27 = 75630.0      # shown as 75.63K
CONS_REV_26 = 722.30
CONS_REV_27 = 1008.63
CONS_TP = 480103.0         # average target, 35 analysts; median 450,000
PEERS = [  # company, listing, price, consensus EPS for the year ending in 2027, year, price date
    ("SK Hynix", "KRX: 000660", 1472000.0, 527160.0, "CY2027", "2 Nov close"),
    ("Micron", "Nasdaq: MU", 884.74, 176.50, "FY to Aug 2027", "30 Oct close"),
]

# ---- Annual history (decks; stockanalysis.com for consolidated 2021 to 2025) ----
YRS = ["2021", "2022", "2023", "2024", "2025"]
REV = [279.6, 302.2, 258.9, 300.9, 333.6]
OP = [51.6, 43.4, 6.6, 32.7, 43.6]
NI = [39.2, 54.7, 14.5, 33.6, 44.3]          # attributable to owners
EPS_H = [5777, 8057, 2131, 4950, 6603]
# Semiconductor (DS) sales and operating profit, 2017 to 2025: 4Q decks of 2018, 2019, 2021, 2022, 2024 and 2025
DS_YRS = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
DS_REV = [74.26, 86.29, 64.94, 72.86, 95.39, 98.46, 66.59, 111.1, 130.1]
DS_OP = [35.20, 44.57, 14.02, 18.81, 29.19, 23.82, -14.88, 15.1, 24.9]
DS_CYC_M = sum(DS_OP) / sum(DS_REV)
MEM_REV_H = {"2023": 44.1, "2024": 84.5, "2025": 104.1}
SEG25 = dict(mx=(129.5, 12.9), vdda=(57.3, -0.2), sdc=(29.8, 4.1), harman=(15.8, 1.5), ds=(130.1, 24.9))
SEG_OP_HIST = dict(mx=[13.0, 10.6, 12.9], vdda=[1.2, 1.7, -0.2], sdc=[5.6, 3.7, 4.1], harman=[1.2, 1.3, 1.5])  # 2023-2025

# ---- Quarterly, KRW tn (decks) ----
QL = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
Q_REV = [79.1, 74.6, 86.1, 93.8, 133.9, 171.5, 195.3]
Q_OP = [6.7, 4.7, 12.2, 20.1, 57.2, 89.5, 107.4]
Q_DS_REV = [25.1, 27.9, 33.1, 44.0, 81.7, 127.5, 147.1]
Q_DS_OP = [1.1, 0.4, 7.0, 16.4, 53.7, 89.2, 106.5]
Q_MEM = [19.1, 21.2, 26.7, 37.1, 74.8, 120.8, 140.7]
Q_MX_REV = [37.0, 29.2, 34.1, 29.3, 38.1, 33.2, 37.7]
Q_MX_OP = [4.3, 3.1, 3.6, 1.9, 2.8, -0.7, -0.6]
Q_DX_OP = [4.7, 3.3, 3.5, 1.3, 3.0, -0.8, -0.8]
Q_NI_ATTR_26 = [47.1, 71.3, 75.2]
Q_EPS_26 = [7123, 10849, 11462]
Q3_FIN = -9.5           # finance income/expenses, 3Q 2026
Q3_FX_OP = 10.0         # FX cut operating profit by about KRW 10tn on the quarter (call)
NI_ALL_9M = 47.2 + 71.6 + 75.1     # net profit incl. minorities; attributable 193.6, so minorities are negligible
# 3Q call: DRAM bits up low to mid single digits, ASP up about 20%; NAND bits up mid single digits, ASP up high teens.
# 4Q guide: DRAM bits up mid to high teens, NAND mid teens; no price guide. HBM4 sales up more than threefold on the
# quarter, 60% of HBM sales; 2027 HBM supply sold out at an agreed target price; HBM share in line with DRAM share in 3Q;
# HBM4E mass production in 1H 2027; contracts with 10 major accounts, multi-year mix target 60 to 70% of capacity.

# ---- HBM: how much of the business (all MINE) ----
# Industry HBM revenue in US$bn on Micron's path (about 35 in 2025, growing about 40% a year), as in my Micron and SK Hynix
# notes. Samsung's 2025 share is IDC's 19.3% (as quoted in SK hynix's prospectus of 10 Jul 2026; IDC: SK hynix 63.2%,
# Micron 17.4% in 2025; 56.4, 20.5 and 23.1% in 1Q 2026). 2026: Samsung said HBM sales would "more than triple"; I use 3.2x.
# 2027: share in line with DRAM share, which I put at 35% (MINE; not disclosed).
HBM_YEARS = ["2025", "2026E", "2027E"]
HBM_TAM = [35.0, 49.0, 69.0]
IDC_SAM_25 = 0.193
HBM_SAM_USD = [35.0 * IDC_SAM_25, None, 69.0 * 0.35]
HBM_SAM_USD[1] = HBM_SAM_USD[0] * 3.2
HBM_FX = [1420.0, 1460.0, FX]
HBM_REV = [u * f / 1000 for u, f in zip(HBM_SAM_USD, HBM_FX)]
HBM_SHARE_26 = HBM_SAM_USD[1] / HBM_TAM[1]      # implied share of a US$49bn market

# ---- MY forecasts by segment, KRW tn ----
TAX = 0.24              # MINE: 3Q 2026 23.8%, 2Q 24.2%
# Q4 2026
Q4 = dict(mem=170.0, nonmem=7.5, ds_opm=0.74, dx=47.0, dx_op=-1.0, sdc=9.0, sdc_op=1.2, har=4.6, har_op=0.4, elim=-18.0)
Q4["ds"] = Q4["mem"] + Q4["nonmem"]
Q4["rev"] = Q4["ds"] + Q4["dx"] + Q4["sdc"] + Q4["har"] + Q4["elim"]
Q4["op"] = Q4["ds"] * Q4["ds_opm"] + Q4["dx_op"] + Q4["sdc_op"] + Q4["har_op"]
Q4["ni"] = Q4["op"] * (1 - TAX)
REV26 = sum(Q_REV[4:]) + Q4["rev"]
OP26 = sum(Q_OP[4:]) + Q4["op"]
NI26 = sum(Q_NI_ATTR_26) + Q4["ni"]
EPS26 = sum(Q_EPS_26) + Q4["ni"] / SH * 1e6
MEM26 = sum(Q_MEM[4:]) + Q4["mem"]
DS_OP26 = sum(Q_DS_OP[4:]) + Q4["ds"] * Q4["ds_opm"]

# 2027 and 2028: memory drives it; the rest MINE
MEM27 = 760.0; MEM_OPM27 = 0.76
G28 = -0.10; MEM_OPM28 = 0.68
OTH27 = dict(nonmem=(32.0, 1.0), dx=(196.0, 2.0), sdc=(33.0, 3.5), har=(18.0, 1.7), elim=(-72.0, 0.0))
OTH28 = dict(nonmem=(36.0, 2.0), dx=(200.0, 6.0), sdc=(34.0, 4.0), har=(19.0, 1.8), elim=(-70.0, 0.0))
DA_Q4 = 12.5; DA27 = 52.0          # MINE (3Q 2026 depreciation 11.9)
CAPEX_Q4 = CAPEX_26 - CAPEX_9M; CAPEX27 = 110.0   # MINE: industry capex to "rise significantly" in 2027
WC_Q4 = 8.0; WC27 = 25.0


def year(m27=MEM27, mo27=MEM_OPM27, g28=G28, mo28=MEM_OPM28):
    mop27 = m27 * mo27
    rev27 = m27 + sum(v[0] for v in OTH27.values())
    op27 = mop27 + sum(v[1] for v in OTH27.values())
    ni27 = op27 * (1 - TAX)
    m28 = m27 * (1 + g28)
    mop28 = m28 * mo28
    rev28 = m28 + sum(v[0] for v in OTH28.values())
    op28 = mop28 + sum(v[1] for v in OTH28.values())
    ni28 = op28 * (1 - TAX)
    fcf_q4 = Q4["ni"] + DA_Q4 - CAPEX_Q4 - WC_Q4
    fcf27 = ni27 + DA27 - CAPEX27 - WC27
    nc = NET_CASH - DIV_TOTAL - BUY_OCT + fcf_q4 + 0.75 * fcf27   # net cash at 30 Sep 2027, before distributions
    return dict(m27=m27, mni27=mop27 * (1 - TAX), rev27=rev27, op27=op27, ni27=ni27, eps27=ni27 / SH * 1e6,
                m28=m28, mni28=mop28 * (1 - TAX), rev28=rev28, op28=op28, ni28=ni28, eps28=ni28 / SH * 1e6,
                fcf_q4=fcf_q4, fcf27=fcf27, nc=nc)


BASE_Y = year()
REV27, OP27, NI27, EPS27 = BASE_Y["rev27"], BASE_Y["op27"], BASE_Y["ni27"], BASE_Y["eps27"]
REV28, OP28, NI28, EPS28 = BASE_Y["rev28"], BASE_Y["op28"], BASE_Y["ni28"], BASE_Y["eps28"]
FCF_Q4, FCF27, NC_SEP27 = BASE_Y["fcf_q4"], BASE_Y["fcf27"], BASE_Y["nc"]
NC_PS = NC_SEP27 / SH * 1e6
NC_NOW = NET_CASH - DIV_TOTAL - BUY_OCT

# ---- Normal memory earnings: the same method and normal cases as my Micron and SK Hynix notes ----
BASE_MEM = Q_MEM[2] + Q_MEM[3] + Q_MEM[4] + Q_MEM[5]   # four quarters to June 2026, as in my SK Hynix note
BITS = 1.20; N_YEARS = 4
PF = 0.55; NM = 0.30; MULT = 12; RATE = 0.10
W_UP = (0.25, 1.0, 0.5)   # Q4 2027 share of 2027's excess; 2028's excess; half again in 2029
GROWTH_F = BITS ** N_YEARS


def normal_mem(pf=PF):
    return BASE_MEM * GROWTH_F * pf


# ---- The rest of the group, normal after-tax operating profit times a multiple (all MINE) ----
# name, normal operating profit (KRW tn), multiple on after-tax profit, basis
OTHERS = [
    ("Foundry and System LSI", None, None, "1.5x my 2026 revenue of about 27.5; no profit disclosed"),
    ("MX and Networks (phones)", 12.0, 10, "2023 to 2025 average 12.2"),
    ("VD and DA (TVs, appliances)", 0.9, 8, "2023 to 2025 average 0.9"),
    ("Samsung Display", 4.5, 8, "2023 to 2025 average 4.5"),
    ("Harman", 1.5, 12, "2025 1.5"),
]
FOUNDRY_REV26 = 6.9 + 6.7 + 6.4 + Q4["nonmem"]      # DS less memory, 1Q to 3Q 2026 plus my 4Q (net of internal sales)
FOUNDRY_X = 1.5
OTH_VAL = [FOUNDRY_REV26 * FOUNDRY_X] + [o * (1 - TAX) * m for _, o, m, _ in OTHERS[1:]]
INV_HAIRCUT = 0.25
INV_VAL = INVEST * (1 - INV_HAIRCUT)
REST = sum(OTH_VAL) + INV_VAL
DISC = 0.20            # MINE: conglomerate and governance discount on the whole sum


def sotp(nm_ni, mult=MULT, y=None, w=W_UP, disc=DISC, cash=True):
    """Value per economic share (KRW) and its parts (KRW tn) for a normal memory after-tax profit nm_ni (KRW tn)."""
    y = BASE_Y if y is None else y
    exc = w[0] * (y["mni27"] - nm_ni) + w[1] * (y["mni28"] - nm_ni) / (1 + RATE) + w[2] * (y["mni28"] - nm_ni) / (1 + RATE) ** 2
    term = nm_ni * mult
    nc = y["nc"] if cash else 0.0
    gross = nc + exc + term + REST
    net = gross * (1 - disc)
    return dict(nc=nc, exc=exc, term=term, rest=REST, gross=gross, net=net, value=net / SH * 1e6, gross_ps=gross / SH * 1e6)


N_BASE = normal_mem() * NM          # normal memory after-tax profit, KRW tn
BASE = sotp(N_BASE)
BASE_VALUE = BASE["value"]
#        name, price factor, net margin, multiple, 2027 memory rev, 2027 memory OPM, 2028 change, 2028 OPM, weights, prob
SCEN = [
    ("Bear", 0.40, 0.19, 10, 645.0, 0.70, -0.35, 0.45, (0.25, 1.0, 0.0), 0.25),
    ("Base", PF, NM, MULT, MEM27, MEM_OPM27, G28, MEM_OPM28, W_UP, 0.50),
    ("Bull", 0.70, 0.40, 14, 840.0, 0.80, 0.05, 0.78, (0.25, 1.0, 1.0), 0.25),
]


def scen(s):
    y = year(s[4], s[5], s[6], s[7])
    n = normal_mem(s[1]) * s[2]
    v = sotp(n, s[3], y, s[8])
    return dict(n=n, nrev=normal_mem(s[1]), eps27=y["eps27"], eps28=y["eps28"], ni27=y["ni27"], **v)


SV = [scen(s) for s in SCEN]
VALS = [v["value"] for v in SV]
WEIGHTED = sum(v * s[9] for v, s in zip(VALS, SCEN))
UP_BASE = BASE_VALUE / PRICE - 1
RULE = "LONG" if UP_BASE >= 0.15 else ("SHORT" if UP_BASE <= -0.25 else "NO CALL")

# Sensitivity: normal memory net margin (rows) against the multiple (columns), discount fixed
SENS_NM = [0.22, NM, 0.38]
SENS_X = [10, MULT, 14]
VGRID = [[sotp(normal_mem() * m, x)["value"] for x in SENS_X] for m in SENS_NM]
DISC_ROW = [sotp(N_BASE, disc=d)["value"] for d in (0.0, 0.10, 0.20, 0.30)]

# What the market value implies for normal memory profit (linear, solved exactly), market value of both classes
_k = W_UP[0] + W_UP[1] / (1 + RATE) + W_UP[2] / (1 + RATE) ** 2
_c = W_UP[0] * BASE_Y["mni27"] + (W_UP[1] / (1 + RATE) + W_UP[2] / (1 + RATE) ** 2) * BASE_Y["mni28"]


def need(disc=DISC, cash=True):
    gross = MCAP / (1 - disc)
    n = (gross - (NC_SEP27 if cash else 0) - REST - _c) / (MULT - _k)
    return n, n / normal_mem()


NEED_0 = need(0.0)               # no discount, cash kept
NEED_D = need()                  # my discount, cash kept
NEED_D0 = need(cash=False)       # my discount, cash spent
NOCASH = sotp(N_BASE, cash=False)["value"]
REVISIT_HI = BASE_VALUE / 1.15
VALUE_P = BASE_VALUE             # same economic value per preferred share

# ---- Multiples ----
PE25 = PRICE / EPS_H[-1]
PE26, PE27, PE28 = PRICE / EPS26, PRICE / EPS27, PRICE / EPS28
PEC26, PEC27 = PRICE / CONS_EPS_26, PRICE / CONS_EPS_27
PEER_PE = [(p[0], p[2] / p[3]) for p in PEERS]
OFF_HIGH = PRICE / HI_CLOSE[0] - 1
PB = MCAP / EQUITY
MEM_SHARE_OP26 = DS_OP26 / OP26
TP_VS = CALL["target"] / PRICE - 1 if CALL["target"] else None

if __name__ == "__main__":
    print(f"shares C {SH_C:.1f} (rec {SH_C_REC:.1f}, issued {SH_C_ISSUED:.1f}) P {SH_P:.1f} tot {SH:.1f}; mcap {MCAP:.1f} = US${MCAP / FX * 1000:.0f}bn; pref gap {PREF_GAP:.1%} hist {PREF_GAP_HIST}")
    print(f"Q4 {Q4}")
    print(f"2026 rev {REV26:.1f} (cons {CONS_REV_26}) OP {OP26:.1f} NI {NI26:.1f} EPS {EPS26:,.0f} ({EPS26 / CONS_EPS_26 - 1:+.1%}); mem26 {MEM26:.1f}; DS OP share {MEM_SHARE_OP26:.1%}")
    print(f"2027 rev {REV27:.1f} ({REV27 / CONS_REV_27 - 1:+.1%}) OP {OP27:.1f} NI {NI27:.1f} EPS {EPS27:,.0f} ({EPS27 / CONS_EPS_27 - 1:+.1%}); mni27 {BASE_Y['mni27']:.1f}")
    print(f"2028 rev {REV28:.1f} OP {OP28:.1f} NI {NI28:.1f} EPS {EPS28:,.0f}; mni28 {BASE_Y['mni28']:.1f}")
    print(f"FCF Q4 {FCF_Q4:.1f} 27 {FCF27:.1f}; NC now {NC_NOW:.1f}; Sep27 {NC_SEP27:.1f} = {NC_PS:,.0f}/sh")
    print(f"HBM usd {[round(x, 1) for x in HBM_SAM_USD]} krw {[round(x, 1) for x in HBM_REV]}; share26 {HBM_SHARE_26:.0%}; of mem 25 {HBM_REV[0] / MEM_REV_H['2025']:.1%} 26 {HBM_REV[1] / MEM26:.1%} 27 {HBM_REV[2] / MEM27:.1%}")
    print(f"base mem {BASE_MEM:.1f} normal mem {normal_mem():.1f} N {N_BASE:.1f}; others {[round(x, 1) for x in OTH_VAL]} inv {INV_VAL:.1f} rest {REST:.1f}")
    print({k: round(v, 1) for k, v in BASE.items()})
    for s, v in zip(SCEN, SV):
        print(s[0], {k: round(x, 1) for k, x in v.items()}, f"{v['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:,.0f} ({WEIGHTED / PRICE - 1:+.1%}); base {BASE_VALUE:,.0f} ({UP_BASE:+.1%}) rule {RULE}; gross/sh {BASE['gross_ps']:,.0f}")
    print("grid", [[round(v / 1000, 1) for v in r] for r in VGRID], sum(v > PRICE for r in VGRID for v in r))
    print("disc row 0/10/20/30", [round(v) for v in DISC_ROW])
    print(f"need nodisc {NEED_0[0]:.1f} {NEED_0[1]:.1%}; disc {NEED_D[0]:.1f} {NEED_D[1]:.1%}; disc no cash {NEED_D0[0]:.1f} {NEED_D0[1]:.1%}; nocash value {NOCASH:,.0f} ({NOCASH / PRICE - 1:+.1%})")
    print(f"revisit hi {REVISIT_HI:,.0f}; PE25 {PE25:.1f} PE26 {PE26:.1f} PE27 {PE27:.1f} PE28 {PE28:.1f} cons26 {PEC26:.1f} cons27 {PEC27:.2f}; PB {PB:.2f}")
    print("peers", [(n, round(x, 2)) for n, x in PEER_PE], f"DS cyc margin {DS_CYC_M:.1%}; off high {OFF_HIGH:+.1%}")
    print(f"pref value upside {VALUE_P / PRICE_P - 1:+.1%}")
