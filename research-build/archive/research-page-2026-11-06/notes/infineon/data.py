"""Infineon Technologies AG (Xetra: IFX) initiation, drafted 2 Nov 2026. Single source of figures for charts, note and model.

Fiscal year ends 30 September: FY2026 = year to Sep 2026 (results due 10 Nov 2026); FY2027 = year to Sep 2027.
Euro million unless stated.
Sources (infineon.com investor relations):
- Annual Report 2025 (fiscal year to 30 Sep 2025): segment revenue and Segment Result, adjusted EPS, shares, gross and net cash,
  the AI data centre passage (over EUR700m in FY2025; 800 V collaboration with NVIDIA; EUR8 to 12bn SAM by end of decade).
- Analyst call intro statements (CEO and CFO prepared remarks, published by Infineon): Q1 FY26 (4 Feb 2026), Q2 FY26 (6 May 2026),
  Q3 FY26 (5 Aug 2026). AI revenue targets, content per kW, backlog, capacity reservation agreements, outlook, net debt.
- Q3 FY26 results release (EQS, 5 Aug 2026): group P&L, free cash flow, net cash, FY2026 outlook.
- Company presentation, August 2026 (fy2026-q3-web-en.pdf): segment revenue and Segment Result by quarter, Q3 FY25 to Q3 FY26,
  restated for the Power Drivers & Signal ICs transfer from GIP to PSS.
- Infineon investor page (read 2 Nov 2026): 2026 Fiscal Fourth Quarter Results on 10 November 2026.
- Infineon release via Business Wire, 20 May 2025 (800 V HVDC with NVIDIA); Infineon and SolarEdge release, 5 Nov 2025 (SST).
Prices: Yahoo Finance IFX.DE history pages (the chart API answered "Too Many Requests"), checked against stockanalysis.com daily
history, read 2 Nov 2026. Consensus and peer multiples: stockanalysis.com (S&P Global data), read 2 Nov 2026.
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "Infineon"
SLUG = "infineon"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/infineon"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Tommy Lau's call, published 2 Nov 2026 (the draft view, per his standing instruction of 2 Nov 2026). ----
CALL = dict(
    banner="NO CALL",
    direction="NO CALL",
    target=None,
    conviction="Low",
    draft=False,
)

# ---- Market data (Yahoo Finance IFX.DE history pages; stockanalysis.com; read 2 Nov 2026) ----
PRICE = 50.56               # Xetra close, 30 Oct 2026
PRICE_DATE = "30 October 2026"
HI_CLOSE = 88.00            # highest close, 2 and 3 June 2026
HI_INTRA = 88.83            # intraday high, 22 June 2026
LO_CLOSE_26 = 37.32         # lowest close of 2026, 30 March 2026
PX_DEC25 = 37.73            # close, 30 Dec 2025 (December month-end)
EVENTS = [  # date, what, close before, close on the day (releases come out before Xetra opens)
    ("4 Feb 2026", "Q1 FY26; AI target of about EUR2.5bn for FY27", 41.08, 40.31),
    ("6 May 2026", "Q2 FY26; FY26 raised to 16bn+; US$175 per kW", 60.50, 59.23),
    ("5 Aug 2026", "Q3 FY26; AI above EUR1.6bn; FY27 to be raised", 63.72, 60.08),
]

# ---- Shares and balance sheet ----
SHARES = 1302.0             # m, outstanding: 1,305.9m issued less 4.2m own shares after the Nov 2025 buyback (Annual Report 2025); about flat since (stockanalysis 1.30bn)
NET_DEBT_JUN26 = 5185       # EUR m, net cash of minus 5,185 at 30 Jun 2026 (Q3 release)
GROSS_CASH_JUN26, DEBT_JUN26 = 1656, 6841
FCF_9M = -199 - 63 + 599    # EUR m, Q1 to Q3 FY26 free cash flow (intro statements)
FCF_GUIDE26 = 900           # EUR m, FY26 free cash flow guide incl. the ~EUR570m ams OSRAM sensor purchase (5 Aug 2026)
FCF_Q4 = FCF_GUIDE26 - FCF_9M
NET_DEBT_SEP26 = NET_DEBT_JUN26 - FCF_Q4   # MINE: June net debt less implied Q4 free cash flow (no dividend in Q4)

# ---- History (group) ----
FY = {"FY24": (14955, 3105, 1.87), "FY25": (14662, 2560, 1.39)}   # revenue, Segment Result, adjusted diluted EPS (Annual Report 2025)
SEG_FY25 = {"ATV": 7402, "GIP": 1631, "PSS": 4208, "CSS": 1418}     # Annual Report 2025, before the GIP to PSS restatement
Q_LABELS = ["Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26"]
Q_REV = {"ATV": [1870, 1921, 1821, 1830, 1932], "GIP": [409, 442, 349, 403, 447],
         "PSS": [1075, 1210, 1171, 1260, 1442], "CSS": [349, 369, 321, 319, 350]}
Q_SR = {"ATV": [371, 430, 403, 331, 356], "GIP": [62, 72, 31, 47, 44],
        "PSS": [197, 176, 204, 257, 359], "CSS": [39, 45, 23, 18, 34]}
Q_GROUP_REV = [3704, 3943, 3662, 3812, 4172]
Q_GROUP_SR = [668, 717, 655, 653, 797]
BACKLOG = [("Dec 2025", 21), ("Mar 2026", 25), ("Jun 2026", 30)]   # EUR bn, "around" / "close to" (intro statements)

# ---- AI data centre power revenue (Infineon's own figures) ----
AI_FY25 = 700               # "over EUR700 million" (Annual Report 2025)
AI_FY26_GUIDE = 1600        # "more than 1.6 billion Euros" (5 Aug 2026)
AI_FY27_OLD = 2500          # "2.5 billion Euros plus", to be revised "material[ly]" upwards on 10 Nov 2026
CLASSIC_DC = 500            # "around 500 million Euros annually" of non-AI data centre power
CONTENT_LO, CONTENT_AVG, CONTENT_HI = 100, 175, 250   # US$ per kW (6 May 2026)
USD_EUR = 1.15              # Infineon's planning rate

# ---- Guidance (5 Aug 2026) ----
Q4_REV_GUIDE, Q4_M_GUIDE = 4700, 0.23
FY26_REV_GUIDE, FY26_M_GUIDE = 16300, 0.20

# ---- MINE: Q4 FY26 split (Infineon gave the group figure and the direction by segment) ----
Q4 = {"ATV": (2000, 0.205), "GIP": (510, 0.15), "CSS": (410, 0.13)}
Q4_PSS_REV = Q4_REV_GUIDE - sum(v[0] for v in Q4.values())
Q4_GROUP_SR = Q4_REV_GUIDE * Q4_M_GUIDE
Q4_PSS_SR = Q4_GROUP_SR - sum(r * m for r, m in Q4.values())   # PSS is the plug to the 23% group guide

REV26 = {k: sum(Q_REV[k][2:]) + (Q4[k][0] if k in Q4 else Q4_PSS_REV) for k in Q_REV}
SR26 = {k: sum(Q_SR[k][2:]) + (Q4[k][0] * Q4[k][1] if k in Q4 else Q4_PSS_SR) for k in Q_SR}
GROUP_REV26 = sum(REV26.values())
GROUP_SR26 = sum(SR26.values())

# ---- MINE: FY2027 built in three blocks: Automotive, AI data centre power, everything else ----
AI26 = 1650                 # MINE: "more than 1.6bn"
AI_M = 0.38                 # MINE: AI power Segment Result margin (not disclosed; Infineon calls it margin-accretive)
REST26 = GROUP_REV26 - REV26["ATV"] - AI26
REST_SR26 = GROUP_SR26 - SR26["ATV"] - AI26 * AI_M
FIN = {"FY25": 250, "FY26": 250, "FY27": 220}   # MINE: net financial cost in the adjusted earnings bridge
TAX = 0.225                 # MINE: Q1 to Q3 FY26 effective rates were 24%, 23% and 21%


def adj_eps(sr, fin):
    return (sr - fin) * (1 - TAX) / SHARES


EPS25_CHECK = adj_eps(FY["FY25"][1], FIN["FY25"])   # reproduces FY25 actual of 1.39 to within 0.02
EPS26 = adj_eps(GROUP_SR26, FIN["FY26"])

# scenario: (atv growth, atv margin, AI revenue, AI margin, rest growth, rest margin, P/E, probability)
SCEN = [
    ("Bear", 0.02, 0.185, 2600, 0.33, 0.05, 0.15, 16, 0.25),
    ("Base", 0.07, 0.215, 3300, 0.38, 0.15, 0.20, 21, 0.50),
    ("Bull", 0.10, 0.225, 4200, 0.40, 0.20, 0.22, 25, 0.25),
]


def build27(g_atv, m_atv, ai, m_ai, g_rest, m_rest):
    atv = REV26["ATV"] * (1 + g_atv); rest = REST26 * (1 + g_rest)
    rev = atv + ai + rest
    sr = atv * m_atv + ai * m_ai + rest * m_rest
    return dict(atv=atv, ai=ai, rest=rest, rev=rev, sr_atv=atv * m_atv, sr_ai=ai * m_ai, sr_rest=rest * m_rest, sr=sr,
                margin=sr / rev, eps=adj_eps(sr, FIN["FY27"]))


SC = []
for name, ga, ma, ai, mai, gr, mr, pe, p in SCEN:
    b = build27(ga, ma, ai, mai, gr, mr)
    b.update(name=name, pe=pe, prob=p, value=b["eps"] * pe)
    SC.append(b)
B = SC[1]
BASE_PE = SCEN[1][7]
BASE_VALUE = B["value"]
WEIGHTED = sum(s["value"] * s["prob"] for s in SC)
REVISIT_LONG = BASE_VALUE / 1.15
REVISIT_SHORT = BASE_VALUE / 0.75

# ---- Consensus and peers (stockanalysis.com, S&P Global data; forecast page updated 21 Oct 2026, read 2 Nov 2026) ----
CONS_REV26, CONS_REV27 = 16350, 20000
CONS_EPS26, CONS_EPS27 = 1.75, 2.87
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 86.92, 24, 50.0, 124.0
FWD_PE_SA = 19.14
PEERS = [  # company, ticker, forward P/E, trailing EV/EBIT, what they make
    ("Infineon", "Xetra: IFX", 19.14, 27.75, "Power semiconductors (Si, SiC, GaN), microcontrollers, sensors, security chips"),
    ("STMicroelectronics", "NYSE: STM", 18.88, 39.37, "Power and analog chips, microcontrollers, sensors"),
    ("onsemi", "Nasdaq: ON", 18.38, 20.00, "Power semiconductors incl. SiC, image sensors"),
    ("NXP", "Nasdaq: NXPI", 14.81, 15.52, "Automotive processors and microcontrollers, secure connectivity"),
    ("Microchip", "Nasdaq: MCHP", 19.52, 56.69, "Microcontrollers, analog, SiC"),
    ("Renesas", "TSE: 6723", 12.42, 14.44, "Automotive and industrial microcontrollers, power management"),
    ("Texas Instruments", "Nasdaq: TXN", 26.35, 32.85, "Analog and power management chips"),
    ("Analog Devices", "Nasdaq: ADI", 26.01, 42.20, "Analog, mixed-signal and power chips"),
    ("Monolithic Power", "Nasdaq: MPWR", 28.47, 52.67, "Power modules and controllers, incl. AI server power"),
]

# ---- Derived ----
MCAP = PRICE * SHARES / 1000                   # EUR bn
EV = MCAP + NET_DEBT_SEP26 / 1000
PE_C26 = PRICE / CONS_EPS26
PE_C27 = PRICE / CONS_EPS27
PE_M26 = PRICE / EPS26
PE_M27 = PRICE / B["eps"]
EV_SR27 = EV * 1000 / B["sr"]
PE_PEAK_C27 = HI_CLOSE / CONS_EPS27
OFF_HIGH = PRICE / HI_CLOSE - 1
RISE_DEC25 = PRICE / PX_DEC25 - 1
RISE_LOW = HI_CLOSE / LO_CLOSE_26 - 1
ATV_SHARE26 = REV26["ATV"] / GROUP_REV26
AI_SHARE26 = AI26 / GROUP_REV26
DC_SHARE26 = (AI26 + CLASSIC_DC) / GROUP_REV26
AI_SHARE27 = B["ai"] / B["rev"]
AI_SHARE_GROWTH26 = (AI26 - AI_FY25) / (GROUP_REV26 - FY["FY25"][0])   # share of FY26 revenue growth from AI
AI_SHARE_SR27 = B["sr_ai"] / B["sr"]
GW_FY26 = AI26 * USD_EUR / CONTENT_AVG   # GW of AI racks at full average content (MY arithmetic)
EPS_PER_AI_BN = 1000 * AI_M * (1 - TAX) / SHARES
VAL_PER_AI_BN = EPS_PER_AI_BN * BASE_PE
EPS_PER_ATV_PT = B["atv"] * 0.01 * (1 - TAX) / SHARES
# what the price implies for FY27 AI revenue at the base multiple, other blocks as base
IMPLIED_SR = (PRICE / BASE_PE) * SHARES / (1 - TAX) + FIN["FY27"]
IMPLIED_AI = (IMPLIED_SR - B["sr_atv"] - B["sr_rest"]) / AI_M
# like-for-like AI guide that would lift the base value to 15% above the price
AI_FOR_LONG = B["ai"] + (PRICE * 1.15 - BASE_VALUE) / VAL_PER_AI_BN * 1000
CONS_VALUE = CONS_EPS27 * BASE_PE

SENS_AI = [2600, 3300, 4000]
SENS_PE = [17, 21, 25]


def grid_value(ai, pe):
    b = build27(*SCEN[1][1:3], ai, SCEN[1][4], *SCEN[1][5:7])
    return b["eps"] * pe


SENS = [[grid_value(a, p) for p in SENS_PE] for a in SENS_AI]

# ---- AI revenue series for the chart (FY24 derived from "a factor of ten within just three years" to ~2.5bn) ----
AI_SERIES = [("FY25", AI_FY25, "A"), ("FY26", AI26, "E"), ("FY27 old", AI_FY27_OLD, "G"), ("FY27 mine", B["ai"], "E")]

# ---- Price, month-end close (Yahoo Finance IFX.DE, read 2 Nov 2026) ----
PX_LABELS = ["Oct 23", "Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24",
             "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25",
             "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26",
             "Jul 26", "Aug 26", "Sep 26", "30 Oct 26"]
PX = [27.48, 35.55, 37.80, 33.74, 33.10, 31.51, 32.72, 36.83, 34.31, 32.05, 33.00, 31.46, 29.02, 30.82, 31.40, 32.06, 35.51,
      30.40, 28.89, 34.28, 36.12, 34.63, 34.96, 33.20, 34.32, 36.33, 37.73, 41.61, 45.83, 38.00, 57.13, 81.11, 81.67, 61.67,
      56.29, 59.50, 50.56]

# ---- The call's tests ----
WRONG_IF = ("Fiscal 2027 AI data centre power revenue, on the definition used to 2026, comes in above €4.0 billion with a Segment "
            "Result Margin of 25 per cent or more for the group, about my bull case; or AI revenue below €2.5 billion with a group "
            "margin under 20 per cent, worse than my bear case.")
REVISIT_IF = (f"Like-for-like fiscal 2027 AI revenue guided on 10 November at €{AI_FOR_LONG / 1000:.1f} billion or more (about "
              f"€{(AI_FOR_LONG + CLASSIC_DC) / 1000:.1f} billion if the new definition folds in the €0.5 billion of classic data centre "
              f"power), or the shares closing below about €{REVISIT_LONG:.0f}, would make it long; a close above about "
              f"€{REVISIT_SHORT:.0f} on unchanged estimates would make it short.")

if __name__ == "__main__":
    print(f"mcap {MCAP:.2f}bn netdebt Sep26 {NET_DEBT_SEP26:.0f} (Q4 FCF {FCF_Q4}) EV {EV:.2f}")
    print("FY26 by seg", {k: (round(REV26[k]), round(SR26[k]), f"{SR26[k] / REV26[k]:.1%}") for k in REV26})
    print(f"Q4 PSS rev {Q4_PSS_REV} SR {Q4_PSS_SR:.0f} m {Q4_PSS_SR / Q4_PSS_REV:.1%}")
    print(f"group FY26 rev {GROUP_REV26} SR {GROUP_SR26:.0f} {GROUP_SR26 / GROUP_REV26:.1%} EPS26 {EPS26:.3f} EPS25check {EPS25_CHECK:.3f}")
    print(f"REST26 {REST26:.0f} REST_SR26 {REST_SR26:.0f} {REST_SR26 / REST26:.1%}")
    for s in SC:
        print(s["name"], f"rev {s['rev']:.0f} sr {s['sr']:.0f} m {s['margin']:.1%} eps {s['eps']:.3f} x{s['pe']} value {s['value']:.2f} {s['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.2f} {WEIGHTED / PRICE - 1:+.1%}; revisit long {REVISIT_LONG:.2f} short {REVISIT_SHORT:.2f}")
    print("grid", [[round(x, 1) for x in r] for r in SENS], sum(x > PRICE for r in SENS for x in r), sum(x >= PRICE * 1.15 for r in SENS for x in r))
    print(f"PE c26 {PE_C26:.1f} c27 {PE_C27:.1f} m26 {PE_M26:.1f} m27 {PE_M27:.1f} EV/SR27 {EV_SR27:.1f} peakPE {PE_PEAK_C27:.1f}")
    print(f"off high {OFF_HIGH:.1%} ytd {RISE_DEC25:+.1%} low-to-high {RISE_LOW:+.1%}")
    print(f"ATV share {ATV_SHARE26:.1%} AI share26 {AI_SHARE26:.1%} DC {DC_SHARE26:.1%} AI share27 {AI_SHARE27:.1%} AI share of growth26 {AI_SHARE_GROWTH26:.1%} AI SR share27 {AI_SHARE_SR27:.1%}")
    print(f"GW {GW_FY26:.1f}; EPS per AI bn {EPS_PER_AI_BN:.3f} value {VAL_PER_AI_BN:.2f}; per ATV pt {EPS_PER_ATV_PT:.3f}")
    print(f"implied AI {IMPLIED_AI:.0f}; AI for long {AI_FOR_LONG:.0f}; cons value {CONS_VALUE:.2f}")
    for d, w, a, b in EVENTS:
        print(d, f"{b / a - 1:+.1%}")
    import statistics
    print("peer median fwd", statistics.median(p[2] for p in PEERS[1:]), "EV/EBIT", statistics.median(p[3] for p in PEERS[1:]))
    print(REVISIT_IF)
