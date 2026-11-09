"""Nebius (Nasdaq: NBIS) initiation, 6 Oct 2026. Single source of inputs for charts, model and note.

Every figure here comes from src/content/calls/nebius.md (the published pitch) or from the
capital-structure detail supplied with the brief (Nebius filings: 30 Jun 2026 interim statements,
Aug 2026 releases). The Python calculations mirror the Excel formulas and are used to verify them.
"""

PRICE = 232.57            # Nasdaq close, 5 Oct 2026
RELOOK = 185.0            # re-look level from the pitch

# ---------- quarterly history (pitch frontmatter) ----------
Q_LABELS = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
ARR = [0.25, 0.43, 0.55, 1.25, 1.92, 3.00]                  # US$bn, quarter end
REVENUE = [50.9, 105.1, 146.1, 227.7, 399.0, 582.3]          # US$m
CAPEX = [544, 510.6, 955.5, 2100, 2500, 5700]                # US$m, Q4 25 to Q2 26 approx
AI_MARGIN = [None, None, 19, 24, 45, 49.7]                   # AI cloud adj. EBITDA margin, %

PRICE_LABELS = ["Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25",
                "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26",
                "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
PRICE_SERIES = [21.99, 27.70, 32.66, 32.49, 21.11, 22.73, 36.75, 55.33, 54.43, 68.32, 112.27, 130.82, 94.87,
                83.71, 85.19, 91.19, 103.76, 138.23, 231.09, 276.17, 190.41, 206.32, 235.88, 232.57]

ACV_LABELS = ["2026 fleet base", "Q2 2026 large deals", "Q3 2026 short-term deals"]
ACV = [12, 22.5, 40]

# ---------- guidance and consensus ----------
ARR_GUIDE = (7.0, 9.0)        # US$bn, year-end 2026
CONNECTED_GUIDE = (800, 1000) # MW, end 2026
CAPEX_GUIDE = (20.0, 25.0)    # US$bn, 2026
CONS_REV_26 = 3.34            # US$bn, Yahoo 6 Oct 2026
CONS_REV_27 = 12.30
ACV_NEW = (20.0, 25.0)        # US$m per MW, Q2 2026 large deals
ACV_BASE = 12.0               # US$m per MW, 2026 fleet
ARR_YE25 = 1.25               # US$bn
ACTIVE_YE25 = 170             # MW, approx
PIPELINE_GW = 5.0

# ---------- capital structure (30 Jun 2026 interim + Aug 2026 releases) ----------
SH_A = 238_400_165
SH_B = 33_455_053
SH_BASIC = SH_A + SH_B                        # 271,855,218
NVDA_WARRANTS = 21_065_936
AUG_EXCHANGE_SH = 15.8e6                      # ~ shares issued ~24 Aug for US$800m of 2029/2031 notes
OPTIONS = 6_740_600
OPT_WAEP = 88.65
RSUS = 6_234_091
CASH = 8042.1                                 # US$m, 30 Jun 2026
RESTRICTED = 1056.0
DEF_REV_CUR = 979.4
DEF_REV_NC = 4995.8
RPO = 37.49                                   # US$bn
SECURED = 775.0                               # US$m, SOFR+2.50% to Oct 2030
ATM_SH = 12_729_493
ATM_AVG = 223.60
ATM_NET = 2.81                                # US$bn
CASH_PF = 14500.0                             # US$m, author's pro forma estimate (pitch)

# name, principal US$m, coupon, conversion price, maturity label, issued
CONVERTS = [
    ("2029 notes", 100.0, 0.0200, 51.45, "Jun 2029", "Remaining after Aug 2026 exchange"),
    ("2031 notes", 100.0, 0.0300, 51.45, "Jun 2031", "Remaining after Aug 2026 exchange"),
    ("2030 notes", 1581.25, 0.0100, 138.75, "Sep 2030", ""),
    ("2032 notes", 1581.25, 0.0275, 138.75, "Sep 2032", ""),
    ("2031 notes (Mar)", 2587.5, 0.0125, 183.22, "Mar 2031", ""),
    ("2033 notes", 1750.0, 0.02625, 180.31, "Mar 2033", ""),
    ("2030 notes (Aug 2026)", 3450.0, 0.0050, 313.46, "Feb 2030", "Issued Aug 2026"),
    ("2034 notes (Aug 2026)", 2300.0, 0.0450, 324.65, "Feb 2034", "Issued Aug 2026"),
]

CONCENTRATION = (24, 21, 14)                  # % of Q2 2026 revenue, three customers
SHORT_SH = 46.78e6
SHORT_PCT = 19.8

PEERS = [  # name, ticker, multiple, basis
    ("Nebius", "Nasdaq: NBIS", 6.3, "EV / 2027 revenue (author's EV)"),
    ("CoreWeave", "Nasdaq: CRWV", 3.6, "EV / 2027 revenue"),
    ("Oracle", "NYSE: ORCL", 4.3, "Next financial year revenue"),
    ("IREN", "Nasdaq: IREN", 2.4, "Next financial year revenue"),
]

# ---------- unit economics ----------
CAPEX_PER_MW = 30.0
CHIP_SHARE = 0.80
CHIP_LIFE = 5
BLDG_LIFE = 20
EBITDA_MARGIN = 0.50
ACV_CASES = [("US$12m, the 2026 fleet", 12.0), ("US$20m, new deals, low", 20.0), ("US$25m, new deals, high", 25.0)]

# ---------- scenarios (2028, valued Oct 2027) ----------
SCEN = [  # name, what happens, rev bn, margin, multiple, net debt bn, shares m, weight
    ("Bear", "Connection slips, new prices fall towards the old", 16.0, 0.40, 8.0, 20.0, 400.0, 0.25),
    ("Base", "About 800 MW connected on time, prices hold", 21.0, 0.45, 11.0, 15.0, 388.0, 0.50),
    ("Bull", "More than 1 GW a year from 2027, prices keep rising", 27.0, 0.50, 13.0, 10.0, 385.0, 0.25),
]
SENS_EBITDA = [7.5, 9.5, 11.5]
SENS_MULT = [9.0, 11.0, 13.0]
SENS_ND = 15.0
SENS_SH = 388.0


# ================= calculations (mirror the Excel model) =================
def unit_econ():
    dep = CAPEX_PER_MW * CHIP_SHARE / CHIP_LIFE + CAPEX_PER_MW * (1 - CHIP_SHARE) / BLDG_LIFE
    out = []
    for lbl, acv in ACV_CASES:
        e = acv * EBITDA_MARGIN
        out.append((lbl, acv, e, e - dep, (e - dep) / CAPEX_PER_MW))
    return dep, out


def share_bridge():
    tsm_opts = OPTIONS * (1 - OPT_WAEP / PRICE)
    conv_rows = []
    itm_sh = 0.0
    debt_stays = 0.0
    for name, p, c, cp, mat, note in CONVERTS:
        sh = p / cp  # m shares
        itm = cp < PRICE
        conv_rows.append((name, p, c, cp, mat, itm, sh))
        if itm:
            itm_sh += sh
        else:
            debt_stays += p
    basic = SH_BASIC / 1e6
    total = basic + NVDA_WARRANTS / 1e6 + AUG_EXCHANGE_SH / 1e6 + tsm_opts / 1e6 + RSUS / 1e6 + itm_sh
    debt_stays += SECURED
    equity = total * PRICE  # US$m
    ev = equity - CASH_PF + debt_stays
    return dict(tsm_opts=tsm_opts / 1e6, conv_rows=conv_rows, itm_sh=itm_sh, total=total,
                debt_stays=debt_stays, equity=equity, ev=ev)


def multiples():
    b = share_bridge()
    ebitda27 = CONS_REV_27 * EBITDA_MARGIN
    ebitda27_r = round(ebitda27 + 1e-9, 1)
    return dict(ebitda27=ebitda27, ebitda27_r=ebitda27_r,
                ev_ebitda=b["ev"] / 1000 / ebitda27, ev_ebitda_r=b["ev"] / 1000 / ebitda27_r,
                ev_rev=b["ev"] / 1000 / CONS_REV_27)


def scenarios():
    out = []
    for n, w, rev, m, x, nd, sh, wt in SCEN:
        e = rev * m
        v = (e * x - nd) / sh * 1000
        out.append((n, w, rev, m, x, nd, sh, wt, e, v, v / PRICE - 1))
    wv = sum(r[7] * r[9] for r in out)
    return out, wv, wv / PRICE - 1


def sensitivity():
    return [[(e * x - SENS_ND) / SENS_SH * 1000 for x in SENS_MULT] for e in SENS_EBITDA]


if __name__ == "__main__":
    print("basic shares", SH_BASIC)
    dep, ue = unit_econ(); print("dep/MW", dep, ue)
    b = share_bridge(); print({k: v for k, v in b.items() if k != "conv_rows"})
    for r in b["conv_rows"]: print(r)
    print(multiples())
    s, wv, wc = scenarios()
    for r in s: print(r)
    print("weighted", wv, wc)
    print(sensitivity())
    print("ARR recon MW", ARR_GUIDE[0] * 1000 / ACV_BASE, ARR_GUIDE[1] * 1000 / ACV_BASE, ARR_YE25 * 1000 / ACTIVE_YE25)
    print("base vs relook", s[1][9] / RELOOK - 1)
