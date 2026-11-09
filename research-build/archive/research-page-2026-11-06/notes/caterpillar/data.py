"""Caterpillar Inc. (NYSE: CAT) initiation, drafted 2 Nov 2026. Single source of figures for charts, note and model.

Fiscal year = calendar year. US$ million unless stated.
Sources (SEC EDGAR, Caterpillar CIK 18230):
- Q3 2026 earnings release, Form 8-K Ex. 99.1, 29 Oct 2026 (ex991toformcat3q2026earnin.htm): segment sales and profit,
  Power & Energy sales by application, income statement, adjusted EPS reconciliation, balance sheet at 30 Sep 2026
  (customer advances 5,329 v 3,314 at Dec 2025), MP&E supplemental data, nine-month cash flow.
- Q3 2026 analyst slide deck, 29 Oct 2026 (Caterpillar IR, s25.q4cdn.com ... 3Q-2026-Analyst-Slide-Deck_Final.pdf): backlog
  US$78.1bn (+6.0bn q/q, +38.2bn y/y), FY2026 outlook (sales and revenues mid-to-high teens growth; adjusted operating margin
  near the bottom of the target range excluding IEEPA recoveries), margin target range (15-19% at $60bn, 18-22% at $72bn,
  21-25% at $100bn), MP&E capex about $3.3bn, Power Generation retail +75%, results dates (4Q 2026 on 2 Feb 2027).
- Q1 and Q2 2026 earnings releases (Form 8-K Ex. 99.1, 30 Apr and 4 Aug 2026): segment data, adjusted EPS, IEEPA recovery 392.
- Form 8-K of 26 Mar 2026, Ex. 99.1: 2024 and 2025 quarterly segment data recast for the Rail move to Resource Industries,
  Power & Energy external sales by application (Power Generation 7,756 in 2024, 10,275 in 2025).
- Q4 2025 earnings release (8-K, 29 Jan 2026): 2024 and 2025 adjusted operating profit (13,431; 11,595) and adjusted EPS.
- Form 10-K 2025 and Form 10-Qs Q1 2025 to Q2 2026: firm backlog and the part not expected within twelve months.
- Q4 2025 analyst slide deck (Caterpillar IR): 2030 targets, Power Generation sales >2.0x 2024 by 2030 (1.3x in 2025).
- Caterpillar virtual HQ visit with Wells Fargo, 10 Sep 2026, transcript posted on Caterpillar's IR site (Q&A Reporting):
  capacity target moved from two to three times; orders into 2029 and a first turbine order into 2030; framework agreements.
- Q3 2026 earnings call, 29 Oct 2026, third-party transcript (The Singju Post): "as far out as 2029 ... into 2030"; 58% of
  backlog within twelve months; Q4 P&E margin similar to Q3.
Prices: stockanalysis.com history (S&P Global data), retrieved 2 Nov 2026; key closes confirmed on the Yahoo chart API, 2 Nov 2026.
Consensus, targets, peer multiples: stockanalysis.com, retrieved 2 Nov 2026 (forecast page updated 30 Oct 2026).
Everything marked MINE is my own estimate.
"""

# ---- Dates and paths (change DATE at publish; the file names follow it) ----
DATE = "2026-11-02"
COMPANY = "Caterpillar"
SLUG = "caterpillar"
OUT_DIR = "/Users/tommylau/Desktop/journal/public/research"
BUILD_DIR = "/Users/tommylau/Desktop/journal/research-build/caterpillar"
PDF = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation.pdf"
XLSX = f"{OUT_DIR}/{DATE}_{COMPANY}_Model.xlsx"
PNG = f"{OUT_DIR}/{DATE}_{COMPANY}_Initiation-p1.png"

# ---- The call. Rebuild = edit this dict only. ----
CALL = dict(
    banner="NO CALL",                 # Tommy Lau's call, 2 Nov 2026 (draft view adopted on his instruction)
    direction="NO CALL",
    target=None,
    conviction="Medium",
    draft=False,
)

# ---- Market data (stockanalysis.com, retrieved 2 Nov 2026; closes cross-checked on the Yahoo chart API, 2 Nov 2026) ----
PRICE = 622.75              # NYSE close, Friday 30 Oct 2026
PRICE_DATE = "30 October 2026"
PRICE_ISO = "2026-10-30"
HI_CLOSE = 1064.90          # highest close, 30 Jun 2026
HI_INTRA = 1073.46          # intraday high, also 30 Jun 2026
PX_DEC25 = 572.87           # close 31 Dec 2025
PX_OCT6 = 863.44            # close 6 Oct 2026, the October high
PX_Q3_PRE, PX_Q3_DAY = 713.38, 647.39   # closes 28 and 29 Oct 2026 (Q3 results 29 Oct, before the open)
PX_Q2_PRE, PX_Q2_DAY = 830.03, 876.54   # closes 3 and 4 Aug 2026
PX_Q1_PRE, PX_Q1_DAY = 810.05, 890.11   # closes 29 and 30 Apr 2026
PX_JUL31 = 814.81

# ---- Shares and balance sheet, 30 Sep 2026 (Q3 release, supplemental MP&E data) ----
SHARES_OUT = 459.67         # m, Form 10-Q cover, outstanding at 30 Jun 2026 (459,674,889; Q3 10-Q not yet filed); Q3 2026 basic weighted 459.1, diluted 460.9
SHARES_Q3_DIL = 460.9
MPE_CASH = 7102.0
MPE_DEBT = 36.0 + 10614.0   # MP&E long-term debt due within one year + after one year (consolidated presentation)
SECURITIES = 1600.0         # "additional $1.6B in slightly longer-dated liquid marketable securities" (Q3 slides)
CUST_ADV = {"Dec 24": None, "Dec 25": 3314.0, "Sep 26": 5329.0}

# ---- Group, annual ----
SALES = {"2024A": 64809.0, "2025A": 67589.0}
ADJ_OP = {"2024A": 13431.0, "2025A": 11595.0}
ADJ_EPS = {"2024A": 21.90, "2025A": 19.06}
Q_ADJ_EPS_26 = [5.54, 8.17, 7.20]
Q_ADJ_OP_26 = [3126.0, 4497.0, 4255.0]
Q_ADJ_PBT_26 = [3252.0, 4760.0, 4261.0]
Q_ADJ_TAX_26 = [679.0, 1070.0, 977.0]
Q_ADJ_PROFIT_26 = [2581.0, 3780.0, 3319.0]
SALES_9M26 = 58640.0
IEEPA_26 = 392.0 + 128.0    # tariff recoveries recorded in Q2 and Q3 2026, in operating profit

# ---- Segments (recast, 8-K 26 Mar 2026; 2026 from quarterly releases). Total sales incl. inter-segment. ----
SEG = {  # (sales, profit)
    "PE": {"2024A": (25506, 5598), "2025A": (28624, 6256), "9M26": (7031 + 8238 + 8784, 1450 + 2027 + 2143)},
    "CI": {"2024A": (25455, 6165), "2025A": (25060, 4675), "9M26": (7161 + 8346 + 7983, 1535 + 1947 + 1831)},
    "RI": {"2024A": (15745, 2676), "2025A": (15920, 2151), "9M26": (3797 + 4648 + 4615, 378 + 693 + 622)},
    "FP": {"2024A": (4053, 932), "2025A": (4220, 966), "9M26": (1096 + 1145 + 1177, 245 + 328 + 264)},
}
SEG_NAMES = {"PE": "Power & Energy", "CI": "Construction Industries", "RI": "Resource Industries", "FP": "Financial Products"}
# Power & Energy external sales by application
APP = {
    "PG": {"2024A": 7756, "2025A": 10275, "9M26": 2817 + 3098 + 3421},
    "OG": {"2024A": 6980, "2025A": 7502, "9M26": 1423 + 2044 + 2236},
    "IN": {"2024A": 6120, "2025A": 5970, "9M26": (5713 - 2817 - 1423) + (6795 - 3098 - 2044) + 1631},
}
APP_NAMES = {"PG": "Power Generation", "OG": "Oil and Gas", "IN": "Industrial"}
PG_Q_LABELS = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
PG_Q = [1618, 1885, 2011, 2242, 1996, 2407, 2634, 3238, 2817, 3098, 3421]
PE_Q_MARGIN = [None] * 4 + [1288 / 5783, 1554 / 7037, 1633 / 7463, 1781 / 8341, 1450 / 7031, 2027 / 8238, 2143 / 8784]

# ---- Backlog (firm), US$bn, and the part not expected within twelve months (10-K, 10-Qs; Q3 2026 slides and call) ----
BL_LABELS = ["Dec 24", "Mar 25", "Jun 25", "Sep 25", "Dec 25", "Mar 26", "Jun 26", "Sep 26"]
BL = [30.0, 35.0, 37.5, 39.8, 51.2, 62.7, 72.1, 78.1]
BL_LATE = [8.0, 9.2, 10.3, 12.5, 19.3, 24.8, 29.2, None]   # Sep 26 not yet in a 10-Q
BL_Q3_WITHIN12 = 0.58       # CFO on the Q3 call (third-party transcript); the 10-Q figure is not out
TTM_SALES_SEP26 = 19133.0 + SALES_9M26          # Q4 2025 + 9M 2026
TTM_SALES_DEC24 = SALES["2024A"]

# ---- MY estimates: Q4 2026 ----
Q4 = dict(PG=4050, OG=2540, IN=1525, PE_INTER=1500, PE_M=0.244,
          CI_S=6930, CI_M=0.170, RI_S=5030, RI_M=0.120, FP_P=275,
          BRIDGE=-720, BELOW=60, TAX=0.23, EQ=35, SH=458.0)

# ---- MY assumptions, 2027 and 2028 ----
G = dict(PG27=0.22, PG28=0.15, OG27=0.06, OG28=0.05, IN27=0.03, IN28=0.03,
         PEM27=0.250, PEM28=0.255,
         CI27=0.02, CI28=0.00, CIM27=0.215, CIM28=0.210,
         RI27=0.06, RI28=0.04, RIM27=0.145, RIM28=0.150,
         FP27=1150, FP28=1190, BR27=-2800, BR28=-2900, BELOW=100, TAX=0.23, EQ=130, SH27=452.0, SH28=443.0)

# ---- Valuation (sum of the parts on 2028E EPS) ----
PG_PE = 25.0                # MY ASSUMPTION: multiple on Power Generation earnings
REST_PE = 16.0              # MY ASSUMPTION: multiple on the rest of Caterpillar
CONS_EPS26, CONS_EPS27 = 27.50, 32.17      # stockanalysis.com (S&P Global), updated 30 Oct 2026
CONS_REV26, CONS_REV27 = 79.55, 88.19
CONS_TP, CONS_N, CONS_TP_LO, CONS_TP_HI = 859.53, 29, 575.0, 1150.0
FWD_PE_SA = 20.77
HIST_FWD_PE = {"2021": 17.95, "2022": 15.83, "2023": 14.51, "2024": 17.06, "2025": 27.73}   # stockanalysis.com
HIST_FWD_PE_AVG_2124 = sum(list(HIST_FWD_PE.values())[:4]) / 4

PEERS = [  # company, ticker, forward P/E, trailing EV/EBIT, what they make, group
    ("Caterpillar", "NYSE: CAT", 20.77, 21.80, "Construction and mining machines, engines, gas turbines, locomotives", "self"),
    ("GE Vernova", "NYSE: GEV", 37.17, 58.92, "Heavy and aeroderivative gas turbines, grid equipment, wind", "power"),
    ("Siemens Energy", "ETR: ENR", 21.81, 26.41, "Gas turbines, grid technology, wind", "power"),
    ("Wärtsilä", "HEL: WRT1V", 19.91, 15.52, "Gas engines and power plants, marine engines", "power"),
    ("Cummins", "NYSE: CMI", 15.22, 18.71, "Diesel and gas engines, generator sets, power systems", "cycle"),
    ("Paccar", "NASDAQ: PCAR", 15.62, 18.39, "Heavy trucks and engines", "cycle"),
    ("Komatsu", "TYO: 6301", 13.14, 11.66, "Construction and mining machines", "cycle"),
    ("Volvo", "STO: VOLV.B", 12.21, 17.06, "Trucks, construction equipment, Volvo Penta engines", "cycle"),
    ("Deere", "NYSE: DE", 32.05, 37.01, "Farm and construction machines", "cycle"),
]


# ---- Projection ----
def build(pg27=G["PG27"], pg28=G["PG28"], og27=G["OG27"], og28=G["OG28"], pem27=G["PEM27"], pem28=G["PEM28"],
          ci27=G["CI27"], ci28=G["CI28"], cim27=G["CIM27"], cim28=G["CIM28"],
          ri27=G["RI27"], ri28=G["RI28"], rim27=G["RIM27"], rim28=G["RIM28"]):
    y = {}
    # 2026E = 9M actual + my Q4
    app26 = {"PG": APP["PG"]["9M26"] + Q4["PG"], "OG": APP["OG"]["9M26"] + Q4["OG"], "IN": APP["IN"]["9M26"] + Q4["IN"]}
    ext26 = sum(app26.values())
    pe_s26 = SEG["PE"]["9M26"][0] + Q4["PG"] + Q4["OG"] + Q4["IN"] + Q4["PE_INTER"]
    pe_p26 = SEG["PE"]["9M26"][1] + (Q4["PG"] + Q4["OG"] + Q4["IN"] + Q4["PE_INTER"]) * Q4["PE_M"]
    inter_ratio = pe_s26 / ext26
    ci_s26 = SEG["CI"]["9M26"][0] + Q4["CI_S"]; ci_p26 = SEG["CI"]["9M26"][1] + Q4["CI_S"] * Q4["CI_M"]
    ri_s26 = SEG["RI"]["9M26"][0] + Q4["RI_S"]; ri_p26 = SEG["RI"]["9M26"][1] + Q4["RI_S"] * Q4["RI_M"]
    fp_p26 = SEG["FP"]["9M26"][1] + Q4["FP_P"]
    seg26 = pe_p26 + ci_p26 + ri_p26 + fp_p26
    q4_seg = (Q4["PG"] + Q4["OG"] + Q4["IN"] + Q4["PE_INTER"]) * Q4["PE_M"] + Q4["CI_S"] * Q4["CI_M"] + Q4["RI_S"] * Q4["RI_M"] + Q4["FP_P"]
    q4_op = q4_seg + Q4["BRIDGE"]
    q4_eps = ((q4_op + Q4["BELOW"]) * (1 - Q4["TAX"]) + Q4["EQ"]) / Q4["SH"]
    op26 = sum(Q_ADJ_OP_26) + q4_op
    eps26 = sum(Q_ADJ_EPS_26) + q4_eps
    y["2026E"] = dict(app=app26, ext=ext26, pe_s=pe_s26, pe_p=pe_p26, ci_s=ci_s26, ci_p=ci_p26, ri_s=ri_s26, ri_p=ri_p26,
                      fp_p=fp_p26, seg=seg26, op=op26, eps=eps26, bridge=op26 - seg26, q4_eps=q4_eps)
    prev = y["2026E"]
    for yr, pg, og, inn, pem, ci, cim, ri, rim, fp, br, sh in [
            ("2027E", pg27, og27, G["IN27"], pem27, ci27, cim27, ri27, rim27, G["FP27"], G["BR27"], G["SH27"]),
            ("2028E", pg28, og28, G["IN28"], pem28, ci28, cim28, ri28, rim28, G["FP28"], G["BR28"], G["SH28"])]:
        app = {"PG": prev["app"]["PG"] * (1 + pg), "OG": prev["app"]["OG"] * (1 + og), "IN": prev["app"]["IN"] * (1 + inn)}
        ext = sum(app.values())
        pe_s = ext * inter_ratio; pe_p = pe_s * pem
        ci_s = prev["ci_s"] * (1 + ci); ci_p = ci_s * cim
        ri_s = prev["ri_s"] * (1 + ri); ri_p = ri_s * rim
        seg = pe_p + ci_p + ri_p + fp
        op = seg + br
        prof = (op + G["BELOW"]) * (1 - G["TAX"]) + G["EQ"]
        eps = prof / sh
        y[yr] = dict(app=app, ext=ext, pe_s=pe_s, pe_p=pe_p, ci_s=ci_s, ci_p=ci_p, ri_s=ri_s, ri_p=ri_p, fp_p=fp,
                     seg=seg, op=op, eps=eps, bridge=br)
        prev = y[yr]
    for yr in y:
        d = y[yr]
        d["pg_p"] = d["pe_p"] * d["app"]["PG"] / d["ext"]          # MINE: Power Generation at the segment's margin
        d["pg_share"] = d["pg_p"] / d["seg"]
        d["pg_eps"] = d["eps"] * d["pg_share"]
        d["rest_eps"] = d["eps"] - d["pg_eps"]
    y["inter_ratio"] = inter_ratio
    return y


Y = build()
Y26, Y27, Y28 = Y["2026E"], Y["2027E"], Y["2028E"]
E26, E27, E28 = Y26["eps"], Y27["eps"], Y28["eps"]
PG_EPS, REST_EPS = Y28["pg_eps"], Y28["rest_eps"]
PG_VAL, REST_VAL = PG_EPS * PG_PE, REST_EPS * REST_PE
BASE_VALUE = PG_VAL + REST_VAL
UP_BASE = BASE_VALUE / PRICE - 1
IMPLIED_PG_PE = (PRICE - REST_VAL) / PG_EPS                 # what the price pays for Power Generation
IMPLIED_PG_PE_PEAK = (HI_CLOSE - REST_VAL) / PG_EPS
PG_SHARE_PRICE = (PRICE - REST_VAL) / PRICE
PG_SHARE_PEAK = (HI_CLOSE - REST_VAL) / HI_CLOSE
PG_SHARE_BASE = PG_VAL / BASE_VALUE
BLENDED_PE = BASE_VALUE / E28

SCEN = [  # name, overrides, pg multiple, rest multiple, prob
    ("Bear", dict(pg27=0.10, pg28=0.03, pem27=0.235, pem28=0.230, ci27=-0.06, ci28=-0.04, cim27=0.195, cim28=0.185,
                  ri27=0.00, ri28=-0.02, rim27=0.135, rim28=0.130), 18.0, 14.0, 0.25),
    ("Base", dict(), PG_PE, REST_PE, 0.50),
    ("Bull", dict(pg27=0.28, pg28=0.22, pem27=0.260, pem28=0.270, ci27=0.05, ci28=0.03, cim27=0.225, cim28=0.225,
                  ri27=0.08, ri28=0.07, rim27=0.155, rim28=0.160), 30.0, 18.0, 0.25),
]
SC = []
for name, ov, mpg, mrest, p in SCEN:
    yy = build(**ov)[ "2028E"]
    v = yy["pg_eps"] * mpg + yy["rest_eps"] * mrest
    SC.append(dict(name=name, e28=yy["eps"], pg_eps=yy["pg_eps"], rest_eps=yy["rest_eps"], mpg=mpg, mrest=mrest,
                   value=v, prob=p, y=yy))
WEIGHTED = sum(x["value"] * x["prob"] for x in SC)
SENS_PG = [18, PG_PE, 32]
SENS_REST = [13, REST_PE, 19]

# ---- Derived market figures ----
MCAP = PRICE * SHARES_OUT / 1000
NET_DEBT_MPE = MPE_DEBT - MPE_CASH
EV_MPE = MCAP + NET_DEBT_MPE / 1000
PE_E26 = PRICE / E26
PE_C26 = PRICE / CONS_EPS26
PE_C27 = PRICE / CONS_EPS27
PE_E27 = PRICE / E27
PE_E28 = PRICE / E28
PE_PEAK_C27 = HI_CLOSE / CONS_EPS27
OFF_HIGH = PRICE / HI_CLOSE - 1
YTD = PRICE / PX_DEC25 - 1
OCT_FALL = PRICE / PX_OCT6 - 1
JUL_FALL = PX_JUL31 / HI_CLOSE - 1
Q1_MOVE = PX_Q1_DAY / PX_Q1_PRE - 1
Q2_MOVE = PX_Q2_DAY / PX_Q2_PRE - 1
Q3_MOVE = PX_Q3_DAY / PX_Q3_PRE - 1
LONG_BELOW = BASE_VALUE / 1.15
SHORT_ABOVE = BASE_VALUE / 0.75
PG_X_2024_26 = Y26["app"]["PG"] / APP["PG"]["2024A"]
PG_X_2024_28 = Y28["app"]["PG"] / APP["PG"]["2024A"]
BL_YEARS_SEP26 = BL[-1] * 1000 / TTM_SALES_SEP26
BL_YEARS_DEC24 = BL[0] * 1000 / TTM_SALES_DEC24
BL_LATE_SEP26 = BL[-1] * (1 - BL_Q3_WITHIN12)

# ---- Price, month-end close (stockanalysis.com, retrieved 2 Nov 2026) ----
PX_LABELS = ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24",
             "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25",
             "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26",
             "30 Oct 26"]
PX = [300.31, 333.96, 366.43, 334.57, 338.52, 333.10, 346.20, 356.10, 391.12, 376.20, 406.11, 362.76, 371.44, 343.95,
      329.80, 309.27, 348.03, 388.21, 438.02, 419.04, 477.15, 577.26, 575.76, 572.87, 657.36, 742.83, 708.46, 890.11,
      875.87, 1064.90, 814.81, 797.47, 810.79, 622.75]

WRONG_IF = ("The shares close above US$778 or below US$467 at the end of October 2027, more than 25 per cent from the price; "
            "or Power Generation sales for 2026 come in below US$12.8 billion, under 25 per cent growth; or the firm order "
            "backlog falls in two consecutive quarters before the end of 2027.")
REVISIT_IF = ("A price below about US$520, where my base value would sit 15 per cent above it, or fourth quarter results on "
              "2 February 2027 showing Power Generation sales up 25 per cent or more for a second year with the backlog "
              "still rising, which would lift my 2027 and 2028 estimates.")

if __name__ == "__main__":
    for yr in ("2026E", "2027E", "2028E"):
        d = Y[yr]
        print(yr, {k: round(v) for k, v in d["app"].items()}, "ext", round(d["ext"]), "PE", round(d["pe_s"]), round(d["pe_p"]),
              f"{d['pe_p'] / d['pe_s']:.1%}", "CI", round(d["ci_s"]), round(d["ci_p"]), f"{d['ci_p'] / d['ci_s']:.1%}",
              "RI", round(d["ri_s"]), round(d["ri_p"]), f"{d['ri_p'] / d['ri_s']:.1%}", "FP", round(d["fp_p"]),
              "seg", round(d["seg"]), "bridge", round(d["bridge"]), "op", round(d["op"]), f"EPS {d['eps']:.2f}",
              f"PG share {d['pg_share']:.1%} PG EPS {d['pg_eps']:.2f} rest {d['rest_eps']:.2f}")
    print(f"Q4 EPS {Y26['q4_eps']:.2f}; inter ratio {Y['inter_ratio']:.4f}")
    print(f"base {BASE_VALUE:.2f} ({UP_BASE:+.1%}); PG val {PG_VAL:.1f} rest {REST_VAL:.1f}; implied PG PE {IMPLIED_PG_PE:.1f} peak {IMPLIED_PG_PE_PEAK:.1f}")
    print(f"PG share of price {PG_SHARE_PRICE:.1%}, peak {PG_SHARE_PEAK:.1%}, base {PG_SHARE_BASE:.1%}; blended {BLENDED_PE:.1f}")
    for x in SC:
        print(x["name"], f"EPS {x['e28']:.2f} PG {x['pg_eps']:.2f} rest {x['rest_eps']:.2f} value {x['value']:.1f} {x['value'] / PRICE - 1:+.1%}")
    print(f"weighted {WEIGHTED:.1f} {WEIGHTED / PRICE - 1:+.1%}")
    print("grid", [[round(PG_EPS * a + REST_EPS * b) for b in SENS_REST] for a in SENS_PG])
    print(f"mcap {MCAP:.1f} netdebt {NET_DEBT_MPE:.0f} EV {EV_MPE:.1f}; PE e26 {PE_E26:.1f} c26 {PE_C26:.1f} c27 {PE_C27:.1f} e27 {PE_E27:.1f} e28 {PE_E28:.1f} peak c27 {PE_PEAK_C27:.1f}")
    print(f"off high {OFF_HIGH:.1%} ytd {YTD:.1%} oct {OCT_FALL:.1%} jul {JUL_FALL:.1%} q1 {Q1_MOVE:+.1%} q2 {Q2_MOVE:+.1%} q3 {Q3_MOVE:+.1%}")
    print(f"PG x2024 2026E {PG_X_2024_26:.2f} 2028E {PG_X_2024_28:.2f}; BL years sep26 {BL_YEARS_SEP26:.2f} dec24 {BL_YEARS_DEC24:.2f}; late sep26 {BL_LATE_SEP26:.1f}")
    print(f"long below {LONG_BELOW:.0f} short above {SHORT_ABOVE:.0f}; hist fwd 21-24 {HIST_FWD_PE_AVG_2124:.2f}")
    import statistics
    print("power median", statistics.median(p[2] for p in PEERS if p[5] == "power"), "cycle median", statistics.median(p[2] for p in PEERS if p[5] == "cycle"))
    print("2026 op margin", Y26["op"] / (SALES_9M26 + 20000), "ex IEEPA", (Y26["op"] - IEEPA_26) / (SALES_9M26 + 20000))
