"""Nvidia (Nasdaq: NVDA) initiation, draft of 2 Nov 2026. Single source of figures for charts, note and model.

Sources: Nvidia CFO Commentary for Q3 FY25, Q4 FY25, Q3 FY26, Q4 FY26, Q1 FY27 and Q2 FY27 (investor.nvidia.com,
s201.q4cdn.com), with their comparative columns. Form 10-K for the year to 25 Jan 2026 (filed 25 Feb 2026): memory
suppliers, demand risk factors. Form 10-Q for the quarter to 26 Jul 2026 (filed 26 Aug 2026): balance sheet, shares
outstanding (24.1bn at 21 Aug 2026), payment terms, customer concentration, Vera Rubin production shipments, the
SB Energy guarantees. Form 8-K of 17 Aug 2026 (PORTS campus: about 4.25 GW of IT load, guarantees capped at US$105bn,
ready-for-service expected beginning in 2028). Nvidia release of 28 Oct 2026 (Q3 FY27 call on 17 Nov 2026; quarter
ended 25 Oct 2026). Nvidia and OpenAI release of 22 Sep 2025 (at least 10 GW; first GW in 2H 2026 on Vera Rubin).
Nvidia GTC 2026 blog (16 to 19 Mar 2026): "at least $1 trillion in revenue from 2025 through 2027".
Prices: Nasdaq.com historical data, retrieved 2 Nov 2026 (Yahoo Finance chart API answered "Too Many Requests").
Consensus, average target and forward P/E: stockanalysis.com (S&P Global data, last updated 26 Oct 2026), retrieved
2 Nov 2026. Everything marked MINE is my own estimate.

Fiscal years end on the last Sunday of January: FY2026 = year to 25 Jan 2026; FY2027 = year to about 31 Jan 2027;
FY2028 = about Feb 2027 to Jan 2028; FY2029 = about Feb 2028 to Jan 2029. From Q1 FY27 Nvidia's non-GAAP measures
include stock-based pay; FY25 and FY26 non-GAAP figures exclude it, so history is shown on GAAP EPS as well.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
DATE_LONG = "2 November 2026"
COMPANY = "Nvidia"
SLUG = "nvidia"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/nvidia"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Draft view for Tommy; he decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="LONG",
    direction="LONG",
    target=245.0,                   # US$ per share; None for NO CALL. Base value rounded to the nearest US$5.
    conviction="Low",
    draft=False,
)
WRONG_IF = ("Data Center revenue falls from one quarter to the next in any quarter Nvidia reports before October 2027, "
            "or its non-GAAP gross margin falls below 70% in any of those quarters, or Nvidia makes a payment under any of "
            "its land, power and shell guarantees.")

# ---- Market data (Nasdaq.com historical data, retrieved 2 Nov 2026) ----
PRICE = 204.64          # Nasdaq close, 30 Oct 2026
PRICE_DATE = "30 October 2026"
HI52 = 243.37           # 52-week high, intraday, 6 Oct 2026
HI_CLOSE = 239.24       # highest close, 6 Oct 2026 (also the 52-week closing high)
LO52 = 164.27           # 52-week low, intraday, 30 Mar 2026
LO_CLOSE = 165.17       # lowest close in 52 weeks, 30 Mar 2026
PRICE_DEC25 = 186.50    # close, 31 Dec 2025
PX_RESULTS = (209.66, 227.98)   # closes on 26 Aug 2026 (Q2 results after the close) and 27 Aug 2026

PX_LABELS = ['Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24', 'Sep 24', 'Oct 24', 'Nov 24',
             'Dec 24', 'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25', 'Jul 25', 'Aug 25', 'Sep 25', 'Oct 25',
             'Nov 25', 'Dec 25', 'Jan 26', 'Feb 26', 'Mar 26', 'Apr 26', 'May 26', 'Jun 26', 'Jul 26', 'Aug 26', 'Sep 26',
             '30 Oct 26']
PX = [61.53, 79.11, 90.36, 86.40, 109.63, 123.54, 117.02, 119.37, 121.44, 132.76, 138.25, 134.29, 120.07, 124.92, 108.38,
      108.92, 135.13, 157.99, 177.87, 174.18, 186.58, 202.49, 177.00, 186.50, 191.13, 177.19, 174.40, 199.57, 211.14,
      200.09, 200.75, 220.78, 228.38, 204.64]

# ---- Shares and balance sheet (10-Q to 26 Jul 2026), US$bn ----
SHARES_OUT = 24.1       # bn, 21 Aug 2026 (10-Q cover)
SH_Q2 = 24.285          # bn, diluted weighted average, Q2 FY27
CASH = 22.443 + 34.143  # cash and marketable debt securities
EQUITY_SEC = 42.783     # marketable equity securities (excluded from net cash)
DEBT = 1.000 + 32.366   # short-term and long-term debt
NETCASH = CASH - DEBT
AR_Q2, DSO_Q2, DSO_Q1 = 63.059, 60, 45
INV_Q2, INV_Q1 = 31.575, 25.8
TOP_CUST_Q2 = 0.16      # one direct customer, share of Q2 FY27 revenue (10-Q)
# Commitments (CFO commentaries)
SUPPLY_COMMIT = [("Q3 FY26", None), ("Q4 FY26", 95.2), ("Q1 FY27", 119.0), ("Q2 FY27", 279.0)]
SUPPLY_BY_YEAR = dict(rem27=92, fy28=87, fy29=88)       # supply and capacity commitments falling due, US$bn
AI_CLOUD_COMMIT = 36.0  # AI cloud agreements, US$bn (Q2 FY27 commentary)
LEASE_3P = 20.0         # data centre leases not commenced, for third parties
GUAR_LPS = 3.5          # land, power and shell guarantees for AI clouds, maximum gross exposure
GUAR_SBE = 105.0        # SB Energy (PORTS campus) guarantees, cap
GUAR_TOTAL = GUAR_LPS + GUAR_SBE
PORTS_GW = 4.25         # GW of IT load (8-K, 17 Aug 2026)
PORTS_OPTION_GW = 3.8
PORTS_GPUS = 1.5        # million GPUs per generation (Q2 FY27 commentary)
PORTS_REV = (150.0, 200.0)   # US$bn of Nvidia revenue per generation at the site

# ---- Consensus and peers (stockanalysis.com, S&P Global data updated 26 Oct 2026; retrieved 2 Nov 2026) ----
CONS_EPS_27 = 9.31      # FY27 (54 analysts; range 9.01 to 10.10)
CONS_REV_27 = 411.7     # US$bn (range 403.2 to 426.9)
CONS_EPS_28 = 15.91     # shown as "EPS Next Year" (FY28)
CONS_REV_28 = 692.21    # shown as "Revenue Next Year" (FY28)
CONS_TP = 328.95        # average target, 62 analysts (median 315; range 180 to 515)
FWD_PE_SA = 16.92       # stockanalysis.com forward P/E for NVDA, 30 Oct 2026 close
PEERS = [  # company, ticker, forward P/E, what they make
    ("Broadcom", "Nasdaq: AVGO", 18.74, "Custom AI chips and Ethernet switch chips"),
    ("TSMC", "NYSE: TSM", 19.05, "Foundry and CoWoS packaging for Nvidia's chips"),
    ("AMD", "Nasdaq: AMD", 45.16, "GPUs and CPUs for data centres"),
    ("Marvell", "Nasdaq: MRVL", 34.76, "Custom AI chips and optical DSPs"),
    ("Micron", "Nasdaq: MU", 5.01, "DRAM and HBM, one of Nvidia's three memory suppliers"),
]

# ---- Annual reported, US$bn ----
YEARS_H = ["FY25", "FY26"]
REV_H = [130.497, 215.938]
DC_H = [115.186, 193.737]
GAAP_EPS_H = [2.94, 4.90]
NG_EPS_OLD_H = [2.99, 4.77]        # non-GAAP excluding stock-based pay (old basis)
GM_NG_H = [0.755, 0.713]
FY24_REV = 60.922
NET_FY26, COMPUTE_FY26 = 31.376, 162.361

# ---- Quarterly (CFO commentaries), US$bn; fiscal quarters ----
QS = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26", "Q1 27", "Q2 27"]
Q_REV = [26.044, 30.040, 35.082, 39.331, 44.062, 46.743, 57.006, 68.127, 81.615, 96.221]
Q_DC = [22.563, 26.272, 30.771, 35.580, 39.112, 41.096, 51.215, 62.314, 75.246, 89.023]
Q_HYPER = {"Q1 27": 43.050, "Q2 27": 48.710}       # recast in the Q2 FY27 commentary
Q_ACIE = {"Q1 27": 32.196, "Q2 27": 40.313}
Q_EDGE_27 = [6.369, 7.198]
NG_Q27 = dict(q1=dict(op=53.783, ni=45.548, eps=1.87, gm=0.750), q2=dict(op=63.956, ni=53.954, eps=2.22, gm=0.750))
NET_Q1_27, COMPUTE_Q1_27 = 14.8, 60.4   # last quarter with the split, "under the previous sub-markets"

# ---- Guidance (Q2 FY27 CFO commentary, 26 Aug 2026) ----
G3 = dict(rev=108.0, gm=0.74, opex=9.0, tax_lo=0.16, tax_hi=0.18)
RESULTS_DATE = "17 November 2026"        # Q3 FY27, per Nvidia's release of 28 Oct 2026

# ---- MY assumptions ----
EDGE_Q3, EDGE_Q4 = 7.5, 7.5      # MINE: Edge Computing, Q3 and Q4 FY27
REV_Q4 = 122.0                   # MINE: Q4 FY27 revenue (+13% on the Q3 guide)
OM_Q4 = 0.655                    # MINE: Q4 FY27 non-GAAP operating margin
OI_Q = 0.4                       # MINE: non-GAAP other income per quarter, US$bn
TAX = 0.165                      # MINE: non-GAAP tax rate (guide 16% to 18% for FY27)
SH27_Q3Q4 = 24.2                 # MINE: diluted shares, Q3 and Q4 FY27
USD_PER_GW = (PORTS_REV[0] / PORTS_GW, PORTS_REV[1] / PORTS_GW)   # US$bn of Nvidia revenue per GW of IT load
USD_PER_GW_MID = sum(USD_PER_GW) / 2      # the PORTS yardstick; its first halls are ready from 2028, so I set it to FY29
# Base: powered GW for new Nvidia systems grows 20% then 15%; revenue per GW rises 15% then 10% (MINE)
G_GW = (0.20, 0.15)
G_USD = (0.15, 0.10)
USD_GW_29 = USD_PER_GW_MID                          # FY29 (calendar 2028), PORTS yardstick
USD_GW_28 = USD_GW_29 / (1 + G_USD[1])              # MINE: deflated by my assumed rise
USD_GW_27 = USD_GW_28 / (1 + G_USD[0])              # MINE; FY26 is translated at the same figure
USD_GW = {"FY26": USD_GW_27, "FY27": USD_GW_27, "FY28": USD_GW_28, "FY29": USD_GW_29}
RANGE_LO, RANGE_HI = USD_PER_GW[0] / USD_PER_GW_MID, USD_PER_GW[1] / USD_PER_GW_MID   # the PORTS range around its midpoint
EDGE28, EDGE29 = 33.0, 37.0      # MINE
OM28, OM29 = 0.63, 0.62          # MINE: memory costs press the margin
OI_YR = 1.5                      # MINE: non-GAAP other income a year
SH28, SH29 = 24.0, 23.8          # MINE: buybacks net of dilution
M_BASE = 16                      # MINE: about today's 16.9x forward multiple, rounded down

# ---- FY27E: two reported quarters, the Q3 guide, my Q4 ----
OP_Q3 = G3["rev"] * G3["gm"] - G3["opex"]
NI_Q3 = (OP_Q3 + OI_Q) * (1 - TAX)
EPS_Q3 = NI_Q3 / SH27_Q3Q4
OP_Q4 = REV_Q4 * OM_Q4
NI_Q4 = (OP_Q4 + OI_Q) * (1 - TAX)
EPS_Q4 = NI_Q4 / SH27_Q3Q4
REV27 = Q_REV[-2] + Q_REV[-1] + G3["rev"] + REV_Q4
EDGE27 = sum(Q_EDGE_27) + EDGE_Q3 + EDGE_Q4
DC27 = REV27 - EDGE27
OP27 = NG_Q27["q1"]["op"] + NG_Q27["q2"]["op"] + OP_Q3 + OP_Q4
OM27 = OP27 / REV27
NI27 = NG_Q27["q1"]["ni"] + NG_Q27["q2"]["ni"] + NI_Q3 + NI_Q4
EPS27 = NG_Q27["q1"]["eps"] + NG_Q27["q2"]["eps"] + EPS_Q3 + EPS_Q4
GW27 = DC27 / USD_GW_27


def project(g_gw28, g_gw29, g_usd28, g_usd29, om28, om29, mult):
    dc28 = DC27 * (1 + g_gw28) * (1 + g_usd28)
    dc29 = dc28 * (1 + g_gw29) * (1 + g_usd29)
    rev28, rev29 = dc28 + EDGE28, dc29 + EDGE29
    ni28 = (rev28 * om28 + OI_YR) * (1 - TAX)
    ni29 = (rev29 * om29 + OI_YR) * (1 - TAX)
    eps28, eps29 = ni28 / SH28, ni29 / SH29
    gw28 = GW27 * (1 + g_gw28); gw29 = gw28 * (1 + g_gw29)
    return dict(dc28=dc28, dc29=dc29, rev28=rev28, rev29=rev29, ni28=ni28, ni29=ni29, eps28=eps28, eps29=eps29,
                gw28=gw28, gw29=gw29, value=eps29 * mult)


#        name,  GW FY28, GW FY29, US$/GW FY28, US$/GW FY29, OM28, OM29, multiple, prob
SCEN = [
    ("Bear", 0.05, 0.00, 0.10, 0.05, 0.60, 0.59, 11, 0.25),
    ("Base", G_GW[0], G_GW[1], G_USD[0], G_USD[1], OM28, OM29, M_BASE, 0.50),
    ("Bull", 0.50, 0.30, 0.15, 0.10, 0.64, 0.64, 18, 0.25),
]
P = project(*SCEN[1][1:8])
VALS = [project(*s[1:8])["value"] for s in SCEN]
WEIGHTED = sum(v * s[8] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
SENS_GW = [0.10, G_GW[0], 0.35]          # FY28 GW growth; FY29 GW growth held at the base 15%
SENS_M = [12, M_BASE, 20]
VGRID = [[project(g, G_GW[1], G_USD[0], G_USD[1], OM28, OM29, m)["value"] for m in SENS_M] for g in SENS_GW]

# ---- What consensus and the price need ----
DC28_CONS = CONS_REV_28 - EDGE28
CONS_GW_G = DC28_CONS / DC27 / (1 + G_USD[0]) - 1      # GW growth consensus FY28 needs, at my US$/GW rise
GW28_CONS = GW27 * (1 + CONS_GW_G)
NEED_EPS29 = PRICE / M_BASE                          # FY29 EPS the price needs at the base multiple


def eps29_flat(g_gw29):
    return project(G_GW[0], g_gw29, G_USD[0], 0.0, OM28, OM29, M_BASE)["eps29"]


# ---- Value and multiples ----
MCAP = PRICE * SHARES_OUT
EV = MCAP - NETCASH
PE27, PE28, PE29 = PRICE / EPS27, PRICE / P["eps28"], PRICE / P["eps29"]
PEC27, PEC28 = PRICE / CONS_EPS_27, PRICE / CONS_EPS_28
OFF_HIGH = PRICE / HI_CLOSE - 1
RISE_DEC25 = PRICE / PRICE_DEC25 - 1
DC_SHARE_Q2 = Q_DC[-1] / Q_REV[-1]
DC_G_Q2 = Q_DC[-1] / Q_DC[-5] - 1
GW_FY26 = DC_H[1] / USD_GW_27
GW_RANGE = lambda dc, usd: (dc / (usd * RANGE_HI), dc / (usd * RANGE_LO))
VERTIV_PER_GW = (3.25, 3.75)     # US$bn per GW, Vertiv management estimate, 19 May 2026 (powering-the-rack)
NV_TO_VERTIV = (USD_PER_GW[0] / VERTIV_PER_GW[1], USD_PER_GW[1] / VERTIV_PER_GW[0])
EPS28_VS_CONS = P["eps28"] / CONS_EPS_28 - 1
REV28_VS_CONS = P["rev28"] / CONS_REV_28 - 1
EPS27_VS_CONS = EPS27 / CONS_EPS_27 - 1

if __name__ == "__main__":
    print(f"USGW 27 {USD_GW_27:.1f} 28 {USD_GW_28:.1f} 29 {USD_GW_29:.1f}"); print(f"US$/GW {USD_PER_GW[0]:.1f}-{USD_PER_GW[1]:.1f} mid {USD_PER_GW_MID:.1f}; Nvidia/Vertiv {NV_TO_VERTIV[0]:.1f}-{NV_TO_VERTIV[1]:.1f}x")
    print(f"Q3E op {OP_Q3:.2f} eps {EPS_Q3:.3f}; Q4E op {OP_Q4:.2f} eps {EPS_Q4:.3f}")
    print(f"FY27 rev {REV27:.1f} DC {DC27:.1f} edge {EDGE27:.1f} OM {OM27:.3f} NI {NI27:.1f} EPS {EPS27:.2f} (cons {CONS_EPS_27}, {EPS27_VS_CONS:+.1%}); GW {GW27:.1f} range {GW_RANGE(DC27, USD_GW_27)}")
    print(f"FY26 GW {GW_FY26:.1f} range {GW_RANGE(DC_H[1], USD_GW_27)}")
    print(f"FY28 base rev {P['rev28']:.1f} DC {P['dc28']:.1f} EPS {P['eps28']:.2f} (cons {CONS_EPS_28} {EPS28_VS_CONS:+.1%}; rev {REV28_VS_CONS:+.1%}) GW {P['gw28']:.1f}")
    print(f"FY29 base rev {P['rev29']:.1f} DC {P['dc29']:.1f} EPS {P['eps29']:.2f} GW {P['gw29']:.1f}")
    print(f"consensus FY28 DC {DC28_CONS:.1f} GW growth needed {CONS_GW_G:.1%} -> {GW28_CONS:.1f} GW")
    for s, v in zip(SCEN, VALS):
        p = project(*s[1:8]); print(s[0], round(p['rev28'], 1), round(p['rev29'], 1), round(p['eps28'], 2), round(p['eps29'], 2), round(v, 1), f"{v / PRICE - 1:+.1%}", round(p['gw29'], 1))
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}; base {BASE_VALUE:.1f} {BASE_VALUE / PRICE - 1:+.1%}")
    print("grid", [[round(v) for v in r] for r in VGRID], sum(v > PRICE for r in VGRID for v in r), sum(v > PRICE * 1.15 for r in VGRID for v in r))
    print(f"PE 27 {PE27:.1f} 28 {PE28:.1f} 29 {PE29:.1f}; cons {PEC27:.1f} {PEC28:.1f}")
    print(f"need EPS29 {NEED_EPS29:.2f}; eps29 if FY29 GW flat {eps29_flat(0):.2f}")
    print(f"mcap {MCAP:.0f} netcash {NETCASH:.1f} EV {EV:.0f}; offhigh {OFF_HIGH:+.1%}; dec25 {RISE_DEC25:+.1%}; DC share {DC_SHARE_Q2:.1%} DC g {DC_G_Q2:.1%}")
