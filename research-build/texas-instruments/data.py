"""Texas Instruments (Nasdaq: TXN) initiation, draft of 6 Oct 2026. Single source of figures for charts, note and model.

Sources: TI quarterly earnings releases (Exhibit 99 to Form 8-K, EDGAR CIK 97476), Form 10-K for 2025 (6 Feb 2026),
Form 10-Q for Q2 2026 (24 Jul 2026), SEC XBRL company facts (annual history), TI earnings calls of 27 Jan and
22 Jul 2026, TI 8-Ks of 4 Feb 2026 (Silicon Labs) and 17 Sep 2026 (dividend), Yahoo Finance chart API (prices),
stockanalysis.com and MarketBeat (consensus, peers), all retrieved 6 October 2026. Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-10-06"
DATE_LONG = "6 October 2026"
COMPANY = "TexasInstruments"
NAME = "Texas Instruments"
SLUG = "texas-instruments"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/texas-instruments"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Claude's draft view; Tommy decides. Final rebuild = edit this dict only. ----
CALL = dict(
    banner="INITIATE AT NO CALL",      # e.g. "INITIATE AT LONG" once Tommy decides
    direction="NO CALL",
    target=None,                  # US$ per share; None for NO CALL
    conviction="Medium",
    draft=False,
)

# ---- Market data (Yahoo Finance chart API, retrieved 6 Oct 2026) ----
PRICE = 294.90          # Nasdaq close, 5 Oct 2026
PRICE_DATE = "5 October 2026"
PRICE_2OCT = 293.80     # close on 2 Oct 2026, the journal piece's date
HI52 = 334.03           # 52-week high (Yahoo meta)
LO52 = 152.73           # 52-week low
PRICE_SEP25 = 183.73    # month-end close, 30 Sep 2025
DPS_NEW = 1.52          # quarterly dividend from Nov 2026 (8-K 17 Sep 2026)
DILUTED = 0.920         # bn diluted shares, Q2 2026 release
CASH = 7.001            # US$bn cash 3.660 + short-term investments 3.341, 30 Jun 2026
DEBT = 14.052           # US$bn long-term debt 12.903 + current portion 1.149, 30 Jun 2026

# ---- Consensus and peers (retrieved 6 Oct 2026) ----
CONS_REV_26 = 21.91     # stockanalysis.com, US$bn
CONS_EPS_26 = 8.49      # stockanalysis.com
CONS_EPS_27 = 10.64     # stockanalysis.com
CONS_FCF_26 = 8.25      # stockanalysis.com, US$bn
FWD_PE_SA = 30.47       # stockanalysis.com forward P/E for TXN
CONS_TP = 324.71        # stockanalysis.com average target, 36 analysts
PEERS = [  # company, ticker, forward P/E, what they make
    ("Texas Instruments", "Nasdaq: TXN", 30.47, "Analog and embedded chips, mostly made in its own 300mm fabs"),
    ("Analog Devices", "Nasdaq: ADI", 26.33, "Analog, mixed-signal and power management chips"),
    ("Infineon", "XETRA: IFX", 24.46, "Power semiconductors, including server power stages"),
    ("onsemi", "Nasdaq: ON", 22.11, "Power and sensing chips, silicon carbide"),
    ("Microchip", "Nasdaq: MCHP", 20.67, "Microcontrollers, analog and power chips"),
    ("NXP", "Nasdaq: NXPI", 14.47, "Automotive and industrial processors and analog"),
    ("Monolithic Power", "Nasdaq: MPWR", 46.08, "Power modules and converters, large AI server exposure"),
]

# ---- Annual reported (SEC XBRL company facts from Forms 10-K), US$bn ----
YEARS_H = ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]
REV_H = [14.383, 14.461, 18.344, 20.028, 17.519, 15.641, 17.682]
GP_H = [9.164, 9.269, 12.376, 13.771, 11.019, 9.094, 10.083]
OP_H = [5.723, 5.894, 8.960, 10.140, 7.331, 5.465, 6.023]
EPS_H = [5.24, 5.97, 8.26, 9.41, 7.07, 5.20, 5.45]
CFO_H = [6.649, 6.139, 8.756, 8.720, 6.420, 6.318, 7.153]
CAPEX_H = [0.847, 0.649, 2.462, 2.797, 5.071, 4.820, 4.550]
CHIPS_H = [0, 0, 0, 0, 0, 0, 0.335]
DEP_H = [0.708, 0.733, 0.755, 0.925, 1.175, 1.508, 1.918]
DPS_H = [3.21, 3.72, 4.21, 4.69, 5.02, 5.26, 5.50]

# 2025 end markets (2025 Form 10-K shares; dollar sizes and growth from the 27 Jan 2026 call)
MARKETS_25 = [  # market, share of revenue, US$bn, growth 2025
    ("Industrial", 0.33, 5.8, 0.12), ("Automotive", 0.33, 5.8, 0.06), ("Personal electronics", 0.21, 3.7, 0.07),
    ("Data centre", 0.09, 1.5, 0.64), ("Communications equipment", 0.03, 0.5, 0.20),
]

# ---- Quarterly (earnings releases), US$m unless stated ----
Q = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
Q_REV = [3661, 3822, 4151, 4007, 4069, 4448, 4742, 4423, 4825, 5463]
Q_GP = [2095, 2211, 2474, 2314, 2313, 2575, 2723, 2472, 2799, 3352]
Q_OP = [1286, 1248, 1554, 1377, 1324, 1563, 1663, 1473, 1808, 2310]
Q_EPS = [1.20, 1.22, 1.47, 1.30, 1.28, 1.41, 1.48, 1.27, 1.68, 2.14]
Q_DEP = [346, 363, 383, 416, 424, 460, 497, 537, 541, 547]
Q_CAPEX = [1248, 1064, 1316, 1192, 1123, 1305, 1197, 925, 676, 514]
Q_CFO = [1017, 1571, 1732, 1998, 849, 1860, 2190, 2254, 1520, 2703]
Q_CHIPS = [0, 0, 0, 0, 260, 0, 75, 0, 555, 549]
Q_ANALOG = [2836, 2928, 3223, 3174, 3210, 3452, 3729, 3615, 3924, 4365]
TTM_FCF = 6.534; TTM_CHIPS = 1.179; TTM_CFO = 8.667; TTM_CAPEX = 3.312
INV_DAYS_Q2 = 196; INV_DAYS_Q4 = 222
OI_Q2 = 69; INT_Q2 = 141
G3_REV = (5.65, 6.15); G3_EPS = (2.23, 2.57); G3_TAX = 0.13
CAPEX_GUIDE_26 = (2.0, 3.0); DEP_GUIDE_26 = (2.2, 2.4)
FCF_FRAME = [(20, 8, 9), (22, 9, 10)]   # revenue US$bn -> FCF US$bn range, TI capital management framework (Q2 26 call)
FALL_TI = (0.70, 0.85)                   # TI's fall-through range excluding depreciation (Q2 26 call)

# ---- Data centre: TI's stated growth rates, and my derivation of dollar size ----
DC_25 = 1.5             # US$bn, 2025 (27 Jan 2026 call)
DC_Q4_25 = 0.45         # "about US$450m a quarter" exiting 2025 (call)
DC_Q4_QQ = 0.05         # Q4 25 sequential, "mid-single digits" (call)
DC_Q1_YY = 0.90         # Q1 26 y/y, "about 90%" (Q1 26 call, as reported)
DC_Q2_YY = 1.00         # Q2 26 y/y, "doubled" (Q2 26 call)
DC_Q2_QQ = 0.20         # Q2 26 sequential, "around 20%" (Q2 26 call)
# Solve: q3 = q4/1.05; q1 + q2 = 1.5 - q3 - q4; Q2 26 = 2 * q2 = 1.2 * Q1 26 = 1.2 * 1.9 * q1 -> q2 = 1.14 q1
_q4 = DC_Q4_25; _q3 = _q4 / (1 + DC_Q4_QQ)
_k = (1 + DC_Q2_QQ) * (1 + DC_Q1_YY) / (1 + DC_Q2_YY)
_q1 = (DC_25 - _q3 - _q4) / (1 + _k); _q2 = _k * _q1
DCQ = [_q1, _q2, _q3, _q4, _q1 * (1 + DC_Q1_YY), _q2 * (1 + DC_Q2_YY)]   # Q1 25 .. Q2 26, US$bn, MINE
DCQ_LABELS = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
DCQ_SHARE = [d / (r / 1000) for d, r in zip(DCQ, Q_REV[4:])]
DC_Q2_26 = DCQ[5]
DC_SHARE_Q2 = DCQ_SHARE[5]
DC_GROWTH_SHARE = (DCQ[5] - DCQ[1]) / ((Q_REV[9] - Q_REV[5]) / 1000)   # share of y/y revenue growth in Q2 26

# ---- Share price, month-end close (Yahoo Finance, retrieved 6 Oct 2026) ----
PX_LABELS = ["Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24",
             "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25",
             "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26",
             "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
PX = [152.71, 170.46, 160.12, 167.33, 174.21, 176.42, 195.01, 194.53, 203.81, 214.34, 206.57, 203.16, 201.03,
      187.51, 184.61, 195.99, 179.70, 160.05, 182.85, 207.62, 181.06, 202.48, 183.73, 161.46, 168.27, 173.49,
      215.55, 212.11, 194.14, 281.08, 305.68, 298.07, 275.74, 260.91, 280.09, 294.90]

# ---- MY assumptions ----
NONOP_Q = -0.08         # US$bn a quarter: other income less interest (Q2 26: +0.069 - 0.141)
TAX = 0.13              # TI guides about 13% for Q3 2026; 13 to 14% for 2026
Q3E_REV, Q3E_OM = 5.95, 0.44     # guide 5.65 to 6.15; OM gives EPS at the 2.40 midpoint
Q4E_REV, Q4E_OM = 5.80, 0.43     # seasonally softer fourth quarter
FALL = 0.75             # incremental operating profit per incremental revenue, before depreciation (TI: 70 to 85%)
DDEP27, DDEP28 = 0.20, 0.10      # extra depreciation, US$bn (TI: rises in 2027 at a slower rate)
DC_G27, DC_G28 = 0.45, 0.30      # data centre growth
RE_G27, RE_G28 = 0.075, 0.02     # rest of TI growth (industrial, auto, personal electronics, comms, other)
DC_26E = DCQ[4] + DCQ[5] + 0.76 + 0.80   # MINE: H2 26 data centre US$0.76bn and 0.80bn
BASE_PE = 25
SCEN = [  # name, dc27, dc28, rest27, rest28, multiple, prob
    ("Bear", 0.25, 0.15, -0.08, -0.02, 22, 0.25),
    ("Base", DC_G27, DC_G28, RE_G27, RE_G28, BASE_PE, 0.50),
    ("Bull", 0.60, 0.40, 0.12, 0.06, 28, 0.25),
]
SENS_EPS = [9.50, None, 12.50]   # middle row = model 2028E
SENS_PE = [21, 25, 29]


def eps(op_q_or_year, quarters=1):
    """EPS from operating profit (US$bn) over n quarters."""
    return (op_q_or_year + NONOP_Q * quarters) * (1 - TAX) / DILUTED


Q3E_EPS = eps(Q3E_REV * Q3E_OM)
Q4E_EPS = eps(Q4E_REV * Q4E_OM)
REV26 = (Q_REV[8] + Q_REV[9]) / 1000 + Q3E_REV + Q4E_REV
OP26 = (Q_OP[8] + Q_OP[9]) / 1000 + Q3E_REV * Q3E_OM + Q4E_REV * Q4E_OM
OM26 = OP26 / REV26
EPS26 = Q_EPS[8] + Q_EPS[9] + Q3E_EPS + Q4E_EPS
REST26 = REV26 - DC_26E


def project(dc27, dc28, re27, re28):
    d27 = DC_26E * (1 + dc27); r27 = REST26 * (1 + re27); rev27 = d27 + r27
    d28 = d27 * (1 + dc28); r28 = r27 * (1 + re28); rev28 = d28 + r28
    op27 = OP26 + FALL * (rev27 - REV26) - DDEP27
    op28 = op27 + FALL * (rev28 - rev27) - DDEP28
    return dict(dc27=d27, dc28=d28, rev27=rev27, rev28=rev28, op27=op27, op28=op28,
                eps27=eps(op27, 4), eps28=eps(op28, 4))


P = project(DC_G27, DC_G28, RE_G27, RE_G28)
R27, R28, EPS27, EPS28 = P["rev27"], P["rev28"], P["eps27"], P["eps28"]
OM27, OM28 = P["op27"] / R27, P["op28"] / R28
VALS = [s[5] * project(*s[1:5])["eps28"] for s in SCEN]
WEIGHTED = sum(v * s[6] for v, s in zip(VALS, SCEN))
BASE_VALUE = VALS[1]
SENS_EPS[1] = round(EPS28, 2)

MCAP = PRICE * DILUTED                     # US$bn, on diluted shares
NETDEBT = DEBT - CASH
EV = MCAP + NETDEBT
FCF25 = CFO_H[-1] - CAPEX_H[-1] + CHIPS_H[-1]
DIV_YIELD = DPS_NEW * 4 / PRICE
GM22 = GP_H[3] / REV_H[3]; OM22 = OP_H[3] / REV_H[3]
GM_Q2 = Q_GP[9] / Q_REV[9]; OM_Q2 = Q_OP[9] / Q_REV[9]
CAPEX_CYCLE = sum(CAPEX_H[2:]) + sum(CAPEX_GUIDE_26) / 2   # 2021 to 2026E at guide midpoint
NEED_EPS28 = PRICE / BASE_PE
REVISIT = BASE_VALUE / 1.15
NEED_OP28 = NEED_EPS28 * DILUTED / (1 - TAX) - 4 * NONOP_Q
NEED_REV28 = R27 + (NEED_OP28 - P["op27"] + DDEP28) / FALL   # on my 2027E and margin bridge
DC_SHARE_28 = P["dc28"] / R28
FCF26_MID = 9.5 + (REV26 - 22) * 0.5        # TI framework interpolated at my 2026E revenue, US$bn
FCF26_PS = FCF26_MID / DILUTED
# How much each driver moves 2028E EPS: data centre bear to bull with the rest at base, and the reverse
DC_SWING = project(SCEN[2][1], SCEN[2][2], RE_G27, RE_G28)["eps28"] - project(SCEN[0][1], SCEN[0][2], RE_G27, RE_G28)["eps28"]
RE_SWING = project(DC_G27, DC_G28, SCEN[2][3], SCEN[2][4])["eps28"] - project(DC_G27, DC_G28, SCEN[0][3], SCEN[0][4])["eps28"]

if __name__ == "__main__":
    print("DC quarterly", [round(x, 3) for x in DCQ], "shares", [f"{s:.1%}" for s in DCQ_SHARE])
    print(f"DC Q2 26 {DC_Q2_26:.3f} share {DC_SHARE_Q2:.1%} of y/y growth {DC_GROWTH_SHARE:.1%}; DC 26E {DC_26E:.2f}")
    print(f"Q3E EPS {Q3E_EPS:.2f} Q4E {Q4E_EPS:.2f}; 2026E rev {REV26:.2f} OP {OP26:.2f} OM {OM26:.3f} EPS {EPS26:.2f}")
    print(f"2027E rev {R27:.2f} OM {OM27:.3f} EPS {EPS27:.2f}; 2028E rev {R28:.2f} OM {OM28:.3f} EPS {EPS28:.2f}; DC share 28 {DC_SHARE_28:.1%}")
    print("PE 26/27/28", round(PRICE / EPS26, 1), round(PRICE / EPS27, 1), round(PRICE / EPS28, 1), "cons26/27", round(PRICE / CONS_EPS_26, 1), round(PRICE / CONS_EPS_27, 1))
    for s, v in zip(SCEN, VALS):
        p = project(*s[1:5]); print(s[0], round(p["rev28"], 2), round(p["eps28"], 2), round(v, 1), f"{v / PRICE - 1:+.1%}")
    print("weighted", round(WEIGHTED, 1), f"{WEIGHTED / PRICE - 1:+.1%}", "revisit", round(REVISIT))
    print("grid", [[round(e * m) for m in SENS_PE] for e in SENS_EPS])
    print(f"mcap {MCAP:.1f} netdebt {NETDEBT:.2f} EV {EV:.1f} FCF25 {FCF25:.3f} yield {DIV_YIELD:.2%} GM22 {GM22:.3f} OM22 {OM22:.3f} GMQ2 {GM_Q2:.3f} OMQ2 {OM_Q2:.3f}")
    print(f"capex cycle {CAPEX_CYCLE:.2f}; FCF26 {FCF26_MID:.2f} per share {FCF26_PS:.2f} yield {FCF26_PS / PRICE:.2%}; EPS27 vs cons {EPS27 / CONS_EPS_27 - 1:+.1%}")
    print(f"need EPS28 {NEED_EPS28:.2f} OP {NEED_OP28:.2f} rev28 {NEED_REV28:.2f} vs 2022 peak {NEED_REV28 / REV_H[3] - 1:+.1%}")
    print(f"DC swing {DC_SWING:.2f} rest swing {RE_SWING:.2f}")
    print("rise since Sep 25", PRICE / PRICE_SEP25 - 1, "below high", 1 - PRICE / HI52)
    print("QGM", [round(g / r * 100, 1) for g, r in zip(Q_GP, Q_REV)])
