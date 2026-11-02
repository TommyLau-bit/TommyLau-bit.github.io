# -*- coding: utf-8 -*-
"""Seagate Technology Holdings plc (Nasdaq: STX) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/seagate.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Seagate Technology Holdings plc (Nasdaq: STX)"
DLONG = datetime.date.fromisoformat(DATE).strftime("%-d %B %Y")

EXTRA_CSS = """
a { color: #1F3864; text-decoration: none; }
.chartsrow { break-inside: avoid; margin-top: 2px; }
.keeptogether { break-inside: avoid; }
table.datatable.compact td { padding: 2.6px 7px; font-size: 8.5pt; }
table.datatable.compact th { padding: 4px 7px; font-size: 8.5pt; }
p.lede { font-size: 10.4pt; font-weight: 700; color: #1F3864; margin: 0 0 6px 0; line-height: 1.28; }
p.draftnote { font-size: 8.2pt; color: #C00000; font-weight: 700; margin: -6px 0 8px 0; }
"""

P_ = []
A = P_.append


def cols(html, widths):
    cg = "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in widths) + "</colgroup>"
    i = html.index(">") + 1
    return html[:i].replace('class="datatable', 'style="table-layout:fixed" class="compact datatable') + cg + html[i:]


def usd(x, d=0):
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"US${q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


bear, base, bull = VALS
sb, sm, su = SV
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = ("My draft view" if CALL["draft"] else "My call")
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
above = sum(v > PRICE for r in VGRID for v in r)
below25 = sum(v <= PRICE * 0.75 for r in VGRID for v in r)
OM27 = (sum(Q27_REV[i] * m for i, m in enumerate([Q_OM[8], Q2_OM_IMPLIED, Q27_OM[2], Q27_OM[3]]))) / REV27

A('<h1 class="doctitle">Seagate Technology Holdings plc</h1>')
A('<p class="docsubtitle"><b>Nasdaq: STX | Hard drives for data centres and the edge | Incorporated in Ireland; principal executive office in Singapore</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:,.2f} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:,.2f}, Nasdaq close {PRICE_DATE}; 52-week range US${LO52:,.2f} to {HI52:,.2f} (intraday)"),
    ("Market value", f"About US${MCAP:,.0f}bn on {SHARES_OUT * 1000:.0f}m shares; net debt US${NET_DEBT * 1000:,.0f}m"),
    ("Non-GAAP P/E", f"{PE26:.1f}x FY26; {PEC27:.1f}x FY27 and {PEC28:.1f}x FY28 consensus; {PE27:.1f}x and {PE28:.1f}x my estimates"),
    ("Consensus (stockanalysis.com)", f"EPS US${CONS_EPS_27:.2f} FY27, US${CONS_EPS_28:.2f} FY28"),
    ("Q2 FY27 guide (27 Oct)", f"Revenue US${G2['rev']:.1f}bn; EPS US${G2['eps']:.2f}; operating margin towards the mid 50s %"),
    ("Supply", "Vast majority of data centre nearline supply allocated through 2028; prices set through 2027"),
    ("Fiscal year", "Ends on the Friday nearest 30 June: FY26 to 3 Jul 2026; FY27 to 2 Jul 2027"),
    ("Next results", f"Q2 FY27, expected {RESULTS_DATE}; date not yet announced"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Seagate\'s drives are allocated through 2028, but at US${PRICE:,.0f} the price needs today\'s record price per terabyte to become the normal.</p>')
A(para("Seagate makes the high-capacity hard drives that cloud and AI data centres use to keep their data. It grows by packing more "
       "terabytes into each drive, not by making more drives, and it says the vast majority of its data centre supply is allocated "
       f"through 2028. In the quarter to 2 October it earned a {pc(Q_GM[8])} gross margin, a record, on revenue up "
       f"{(Q_REV[8] / Q_REV[4] - 1) * 100:.0f}%."))
A(para(f"The shares are {abs(OFF_HIGH) * 100:.0f}% below their June high, and trade at {PEC28:.1f} times consensus fiscal 2028 "
       "earnings. That looks cheap, but hard drives are cyclical. On my method the price needs normal earnings of "
       f"{usd(NEED_N, 2)} a share after the shortage. At my margin that means a normal price of {usd(NEED_PTB, 2)} per terabyte, "
       f"above the {usd(Q_PTB[8], 2)} of the last quarter, the highest yet."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction.</b> My base case is worth "
       f"{usd(BASE_VALUE)}, {chg(BASE_VALUE)}, inside my band. The bear case is {usd(bear)} ({chg(bear)}) and the bull case "
       f"{usd(bull)} ({chg(bull)}). The view leans short, but prices are set and rising through 2027."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (non-GAAP unless marked; FY26 ended 3 July 2026, FY27 ends 2 July 2027)"))
A(datatable(
    ["US$ billion unless stated", "FY25A", "FY26A", "Q1 FY27A", "Q2 FY27 guide", "FY27E*", "FY28E*", "Normal year*"],
    [
        ["Revenue", f"{FY25['rev']:.2f}", f"{FY26['rev']:.2f}", f"{Q_REV[8]:.2f}", f"{G2['rev']:.1f}", f"{REV27:.2f}", f"{REV28:.2f}", f"{normal_rev():.2f}"],
        ["Revenue growth (%)", f"{(FY25['rev'] / REV_H[8] - 1) * 100:.0f}", f"{(FY26['rev'] / FY25['rev'] - 1) * 100:.0f}",
         f"{(Q_REV[8] / Q_REV[4] - 1) * 100:.0f}", "", f"{(REV27 / FY26['rev'] - 1) * 100:.0f}", f"{G28 * 100:.0f}", ""],
        ["Nearline exabytes", "497", f"{FY26['nl_eb']}", f"{Q_NL[8]}", "", "", "", f"{NL_N:,.0f}"],
        ["Price per nearline TB (US$)", f"{sum(Q_DC[:4]) * 1000 / sum(Q_NL[:4]):.2f}", f"{PTB_26:.2f}", f"{Q_PTB[8]:.2f}", "", "", "", f"{PTB_2Y * PF:.2f}"],
        ["Operating margin (%)", pc(FY25["om"]), pc(FY26["om"]), pc(Q_OM[8]), "mid 50s", pc(OM27), pc(OM28), ""],
        ["Net margin (%)", pc(FY25["ni"] / FY25["rev"]), pc(FY26["ni"] / FY26["rev"]), pc(Q1_NM), "", pc(NI27 / REV27), pc(NI28 / REV28), pc(NM)],
        ["EPS, diluted (US$)", f"{FY25['eps']:.2f}", f"{FY26['eps']:.2f}", f"{Q_EPS[8]:.2f}", f"{G2['eps']:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}", f"{N_BASE:.2f}"],
        ["Consensus EPS (US$)", "", "", "", "", f"{CONS_EPS_27:.2f}", f"{CONS_EPS_28:.2f}", ""],
        [f"P/E at US${PRICE:,.2f} (x)", f"{PRICE / FY25['eps']:.0f}", f"{PE26:.1f}", "", "", f"{PE27:.1f}", f"{PE28:.1f}", f"{PE_NORMAL:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6, 7},
))
A(caption("*FY27E is Q1 actual, the Q2 guide and my Q3 and Q4; FY28E and the normal year are my own estimates. Price per nearline "
          "terabyte is my derived ratio: Data Center revenue over nearline exabytes, from Seagate's supplementals. FY25 growth is on "
          "GAAP FY24 revenue. Consensus from stockanalysis.com (S&P Global data, updated 29 October 2026). History from Seagate's "
          "releases of 28 July and 27 October 2026 and its supplementals."))

A('<div class="keeptogether">')
A(section("Two charts: a cycle at its highest, and a value below the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_cycle.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and net margin by fiscal year; GAAP to FY26 (Seagate 10-K data via SEC EDGAR), my non-GAAP estimates for "
          "FY27 and FY28. Right: value per share from the base case, the probability-weighted cases, the sensitivity grid and the bear "
          f"to bull range, against the US${PRICE:,.2f} price (red) and the highest close of the past year."))
A('</div>')

A(section("The thesis: the removals firm that will not buy more vans"))
A(para("Think of a removals firm with a fixed fleet. As bookings grow, it does not buy more vans; it packs each one tighter, and "
       "customers book their move a year or more ahead. For two years that meant more boxes at the same price per box. Now the "
       "firm is also charging more per box. The question for an investor is whether that lasts once a rival buys more vans."))
A(para(f"<strong>More terabytes, not more drives.</strong> Seagate shipped {Q_NL[8]} exabytes of nearline drives in the quarter to "
       f"2 October, up about 24% on a year, and {FY26['nl_eb']} in fiscal 2026 against 497 the year before. In the December "
       "2025 quarter it shipped 26% more exabytes than a year earlier \"on similar number of units\". On 27 October it said it meets exabyte growth "
       "\"by increasing capacity per drive rather than increasing drive unit production\", and on the call it put capital spending at "
       "4 to 6% of revenue, enough for exabyte supply growth in the mid 20s %. Its HAMR drives, which heat each bit with a laser so it "
       "can be smaller, carry that density."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_ptb.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_quarters.png"></div></div>')
A(caption("Left: Data Center revenue per nearline terabyte (my derived ratio; the red bar is the latest quarter) and nearline "
          "exabytes shipped, by quarter ending. Right: revenue by end market, with non-GAAP gross margin in white, and the Q2 FY27 "
          "guide. Source: Seagate supplementals, 28 October 2025 to 27 October 2026; FY25 quarters on the definition that includes "
          "VIA customers."))
A('</div>')
A(para(f"<strong>The horizon lengthened.</strong> Seagate said its nearline supply was allocated through 2026 in January, largely "
       "through 2027 in April, and on 27 October that the \"vast majority\" of data centre nearline supply is allocated through 2028, "
       "with some cloud agreements to 2030. My piece put Seagate on the watch list for exactly this: a few qualified makers, booked "
       "years ahead, but growing without a new building. The supplementals and filings support every figure the piece used."))
A(para(f"<strong>Now the price moves too.</strong> From late 2024 to early 2026, Data Center revenue per nearline terabyte held "
       f"between {usd(min(Q_PTB[:7]), 2)} and {usd(max(Q_PTB[:7]), 2)}. In the last two quarters it rose to {usd(Q_PTB[7], 2)} and "
       f"then {usd(Q_PTB[8], 2)}, up {PTB_UP * 100:.0f}% on a year. Seagate said pricing rose faster than before, mainly by "
       "repricing contracts, and that it now passes higher component costs through. That is what pushed the gross margin from "
       f"{pc(Q_GM[4])} to {pc(Q_GM[8])} in a year, and why it guides US${G2['rev']:.1f}bn and EPS of US${G2['eps']:.2f} for the "
       "December quarter."))
A(para("<strong>The piece left one question unanswered.</strong> Allocated is not priced. Seagate's build-to-order contracts set "
       "configuration and price for nearline shipments through calendar 2027 only. It expects to start finalising 2028 prices over "
       "the next few quarters. The horizon in my chart is a horizon of volume; the price on its last year is still open, and that "
       "is the year the share price now depends on."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:,.2f} Seagate is worth about US${MCAP:,.0f}bn. The shares trade at {PEC27:.1f} times fiscal 2027 consensus "
       f"of US${CONS_EPS_27:.2f}, {PEC28:.1f} times fiscal 2028 consensus of US${CONS_EPS_28:.2f}, and {PE_RUN:.1f} times the "
       f"December quarter guide annualised. They closed at a high of US${HI_CLOSE:,.2f} on 22 June 2026 and fell "
       f"{abs(OCT_FALL) * 100:.0f}% in October alone. They fell {abs(TOSHIBA_DAY) * 100:.1f}% on 2 October, the day Toshiba said "
       "its Philippine drive plant had begun making nearline drives on an expanded line and aims to nearly double that plant's annual "
       "capacity, measured in storage, by fiscal 2027 against fiscal 2025."))
A(para(f"<strong class='lead'>Hard drives are priced as steadier than flash.</strong> Seagate and Western Digital trade at "
       f"{PEC27:.1f} and {PEER_PE[0][1]:.1f} times 2027 consensus; the flash makers Sandisk and Micron at {PEER_PE[1][1]:.1f} and "
       f"{PEER_PE[2][1]:.1f} times. The market already believes three makers, long contracts and no new factories make this cycle "
       "milder than memory's. I agree it is milder. The question is how much milder."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_eps.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: non-GAAP EPS, reported for FY25 and FY26, my estimates for FY27 and FY28, my base normal year, and the normal year "
          "the price needs on my method. Right: STX month-end close, October 2023 to the 30 October 2026 close (stockanalysis.com, "
          "retrieved 2 November 2026), against my base value."))
A('</div>')
A(para(f"<strong class='lead'>What the price needs.</strong> I value the cycle, not the year: net cash at October 2027, plus the "
       f"earnings above normal still to come, plus {MULT} times normal earnings. On my base fiscal 2028, US${PRICE:,.2f} needs normal "
       f"EPS of {usd(NEED_N, 2)}, {NEED_VS_26:.1f} times fiscal 2026 and {NEED_VS_28 * 100:.0f}% of my fiscal 2028. On my normal "
       f"revenue that is a {pc(NEED_NM)} net margin, against {pc(FY26['ni'] / FY26['rev'])} in fiscal 2026 and a ten-year GAAP "
       f"average of {pc(CYC_NM)}. Put another way, at my {pc(NM, 0)} margin it needs a normal price of {usd(NEED_PTB, 2)} per "
       "terabyte at the scale of 2030."))
A(para(f"<strong class='lead'>Where I differ.</strong> My normal year lets nearline exabytes grow {(EB_G - 1) * 100:.0f}% a year "
       f"for four years, to {NL_N:,.0f} exabytes, at the {usd(PTB_2Y, 2)} per terabyte Seagate averaged over fiscal 2025 and 2026. "
       f"That average was not a glut price: by January 2026, with the price still near it, Seagate had already allocated its output a year ahead. I give it a "
       f"{pc(NM, 0)} net margin, slightly above fiscal 2026, because each HAMR generation cuts the cost of a terabyte. The market "
       "assumes the 2026 price rise survives Toshiba's added Philippine capacity and the next round of contracts. It may: no maker is building "
       "a drive factory. That is why I do not go short."))

A(section("Valuation, with the working"))
A(para(f"Fiscal 2027 is the first quarter, the guide, then US${Q27_REV[2]:.2f}bn and US${Q27_REV[3]:.2f}bn at operating margins of "
       f"{pc(Q27_OM[2], 0)} and {pc(Q27_OM[3], 0)}, with 16% tax on 233m shares: EPS {usd(EPS27, 2)}, "
       f"{abs(EPS27 / CONS_EPS_27 - 1) * 100:.1f}% below consensus. Fiscal 2028 lets exabytes grow {EB28 * 100:.0f}% and the price "
       f"per terabyte {PTB28 * 100:.0f}%, at a {pc(OM28, 0)} operating margin: EPS {usd(EPS28, 2)}, "
       f"{abs(EPS28 / CONS_EPS_28 - 1) * 100:.1f}% below consensus, because 2028 prices are not yet set. Free cash flow of about "
       f"US${FCF_12M:.1f}bn over the next twelve months turns net debt of US${NET_DEBT * 1000:,.0f}m into net cash of about "
       f"{usd(NC_PS, 2)} a share by October 2027. The fiscal 2028 excess over normal, and half of it again in 2029, discounted at "
       f"10%, adds {usd(sm['exc'], 2)}; {MULT} times normal EPS of {usd(N_BASE, 2)} adds {usd(sm['term'], 2)}. Total: "
       f"{usd(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "FY28 EPS", "Normal EPS", "Normal P/E", "Value", "Change", "Weight"],
    [
        ["Bear", "2028 contracts reprice 10% lower as Toshiba's capacity ships; normal price per TB 20% below the two-year average",
         usd(sb["eps28"], 2), usd(sb["n"], 2), f"{SCEN[0][3]}x", usd(bear), chg(bear), "25%"],
        ["Base", "Prices firm through FY28, half the excess in FY29; normal at the FY25 and FY26 price per TB", usd(sm["eps28"], 2),
         usd(sm["n"], 2), f"{SCEN[1][3]}x", usd(base), chg(base), "50%"],
        ["Bull", "2028 prices rise again; the last quarter's US$17.4 per TB becomes the normal", usd(su["eps28"], 2), usd(su["n"], 2),
         f"{SCEN[2][3]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [9, 37, 10, 10, 8, 9, 10, 7]))
A(caption(f"Normal revenue: bear US${sb['nrev']:.1f}bn at an {pc(SCEN[0][2], 0)} margin; base US${sm['nrev']:.1f}bn at "
          f"{pc(SCEN[1][2], 0)}; bull US${su['nrev']:.1f}bn at {pc(SCEN[2][2], 0)}. Fiscal 2027 and the cash at October 2027 are "
          "the same in all three on purpose: 2027 prices are set in contracts, so a price turn shows from fiscal 2028. The bear is not "
          f"fanciful: revenue fell {abs(FY23_REV_FALL) * 100:.0f}% in fiscal 2023, and the shares are already "
          f"{abs(OFF_HIGH) * 100:.0f}% off their June high. The band: long when my base value is at least 15% above the price, short "
          "when it is at least 25% below, no call in between."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: normal net margin against the multiple on normal earnings"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Normal net margin"] + [f"{m}x" for m in SENS_X],
    [[pc(m, 0)] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (m, r) in enumerate(zip(SENS_NM, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{NUMW[above].capitalize()} of the nine cells sits above the price: it needs both a {pc(SENS_NM[2], 0)} normal margin "
       f"and {SENS_X[2]} times. The cell with {pc(SENS_NM[2], 0)} and {SENS_X[1]} times sits just below it, at "
       f"{usd(VGRID[2][1])}. {NUMW[below25].capitalize()} cells sit 25% or more below the price: every cell at "
       f"{pc(SENS_NM[0], 0)}, and {pc(SENS_NM[1], 0)} at {SENS_X[0]} times. Normal revenue, fiscal 2028 and the cash are as in the "
       "base. Every figure is live in the accompanying model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Listing", "P/E on consensus", "Year", "What they make"],
    [["Seagate", "Nasdaq: STX", f"{PEC27:.1f}x", "FY to Jul 2027", "Hard drives (nearline and other)"]]
    + [[c, t, f"{px / e:.1f}x", y, w] for c, t, px, e, y, w in PEERS],
    num_cols={2},
), [20, 16, 14, 16, 34]))
A(caption("Price over consensus EPS for the year ending in 2027, from stockanalysis.com (S&P Global), retrieved 2 November 2026; "
          f"Nasdaq closes of 30 October 2026. Western Digital earned a {pc(WDC_Q1['gm'])} non-GAAP gross margin in the quarter to 2 "
          f"October and guides {pc(WDC_Q1['g_gm'])} for the next (release, 22 October 2026). Toshiba, the third hard drive maker, has "
          "been privately held since December 2023. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        [f"{RESULTS_DATE} (not yet announced)", "Q2 FY27 results", f"Revenue against US${G2['rev']:.1f}bn; price per terabyte; any 2028 prices set"],
        ["Next few quarters", "Calendar 2028 build-to-order terms", "Whether 2028 prices are set above 2027's"],
        ["March 2027 quarter", "Buybacks step up (call)", "US$4.4bn left on the authorisation"],
        ["Toshiba FY2027 (April 2027 to March 2028)", "Toshiba's Philippine plant capacity nearly doubled on fiscal 2025", "Shipments, and any price cutting to fill it"],
        ["Late calendar 2027", "Mozaic 5 qualification shipments", "Cost per terabyte, and how far supply can stretch"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>On the upside, durability.</strong> Seagate says it is talking to customers well past 2028, and some cloud agreements "
       "already run to 2030. If 2028 prices are set above 2027's and the 2029 book fills in the same way, the normal year moves towards "
       f"my bull case, {chg(bull)}. Flash, the obvious substitute, is short and dear too: Micron said on 30 September that its NAND "
       "prices rose by about 30% in a single quarter. <strong>On the downside, supply.</strong> Toshiba is adding capacity now, and "
       "every maker sees the same price signal. Seagate's revenue fell 37% in fiscal 2023, the last downturn."))
A(para("<strong>Execution and costs.</strong> HAMR needs longer manufacturing cycle times and more tooling, and Seagate said scrap and "
       "yield losses during transitions weigh on costs. External component costs are much higher than a year ago. Inventory rose to "
       f"US${INV[1]:.2f}bn from US${INV[0]:.2f}bn in the quarter as it prepared manufacturing for Mozaic 4 qualifications. <strong>Double ordering.</strong> Buyers in a boom book early "
       "and sometimes twice, and allocation does not prove use."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price at or below about {usd(REVISIT_LONG)} with my numbers unchanged. "
       f"<strong>Into a short:</strong> a price at or above about {usd(REVISIT_SHORT)}."))
A(para("<strong>The view is wrong if</strong>, by October 2027, Seagate's supplementals show Data Center revenue per nearline exabyte "
       "below the same quarter a year earlier, or Seagate says calendar 2028 nearline prices are lower than calendar 2027's, which points "
       "to my bear case; or Seagate says the vast majority of its calendar 2029 nearline supply is allocated and that calendar 2028 prices "
       "are set above calendar 2027's, which lifts normal earnings towards my bull case."))
A('</div>')

A(section("Conclusion"))
A(para("My piece put Seagate on the watch list: few makers, booked years ahead, but growing without a new building. Its results "
       f"support that, and add something the piece did not have: the price per terabyte is up {PTB_UP * 100:.0f}% in a year. The "
       f"shares are a different question. At {PEC28:.1f} times consensus fiscal 2028 they look cheap, but the price needs that rise "
       f"to become the normal at the scale of 2030. Base value {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, range {usd(bear)} to "
       f"{usd(bull)}. {my_call}: {CALL['direction']}, leaning short, {CALL['conviction'].lower()} conviction."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY27E", "FY28E", "Normal", "Basis"],
    [
        ["Revenue, US$bn", f"{REV27:.2f}", f"{REV28:.2f}", f"{normal_rev():.2f}", f"Q1, Q2 guide, then 5.15 and 5.45; FY28 EB +25%, price +5%; normal {NL_N:,.0f} EB at US${PTB_2Y:.2f} plus Edge IoT 2.5"],
        ["Operating margin", pc(OM27), pc(OM28), "", "Q2 implied by the EPS guide; 'gross margin to keep expanding'"],
        ["Net margin", pc(NI27 / REV27), pc(NI28 / REV28), pc(NM, 0), "Normal: FY26 29.0%; FY16-25 GAAP 9.5%"],
        ["Tax rate", pc(TAX, 0), pc(TAX, 0), "", "Guided about 16%"],
        ["Diluted shares, m", f"{SH * 1000:.0f}", f"{SH * 1000:.0f}", f"{SH * 1000:.0f}", "Q2 guide held; buybacks treated as cash kept"],
        ["Capex, share of revenue", pc(CAPEX_PCT, 0), pc(CAPEX_PCT, 0), "", "Guided 4% to 6% for FY27"],
        ["Multiple, discount rate", "", "", f"{MULT}x, 10%", "Mine"],
    ],
), [24, 9, 9, 10, 48]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Seagate fiscal Q1 2027 results release, Exhibit 99.1 to Form 8-K, 27 October 2026, and its Supplemental '
  'Financial Information of the same date, for revenue, margins, net income, EPS, cash flow, debt, shares, exabytes, Data Center '
  'revenue, supply allocation and the Q2 FY27 guide. Seagate supplementals of 28 October 2025, 27 January 2026 and 28 April 2026. '
  'Seagate fiscal Q4 and fiscal 2026 results release, Exhibit 99.1 to Form 8-K, 28 July 2026, and Form 10-K for the year to 3 July 2026. '
  'Seagate earnings call of 27 October 2026, Seagate\'s corrected transcript (FactSet CallStreet) at investors.seagate.com, for '
  'build-to-order terms, exabyte growth, capital spending, pricing, costs and buybacks. Form 10-Q for the quarter to 2 October 2026 '
  'for inventory. Seagate 10-K data via SEC EDGAR for fiscal 2016 to 2026. Western Digital fiscal Q1 2027 '
  'release, Exhibit 99.1 to Form 8-K, 22 October 2026. Toshiba Electronic Devices &amp; Storage news release on Toshiba Information '
  'Equipment (Philippines), 2 October 2026. Micron '
  'prepared remarks, 30 September 2026. Share prices from stockanalysis.com daily history, retrieved 2 November 2026; consensus and '
  'peer figures from stockanalysis.com, retrieved 2 November 2026. Estimates for fiscal 2027 and 2028, normal earnings and the '
  'valuation are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests the Seagate part of my journal piece, the claim of 30 October 2026 and its watch list, '
  '<a href="https://thephysicallayer.fyi/journal/the-chip-supply-chain/">thephysicallayer.fyi/journal/the-chip-supply-chain</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Seagate. Personal research, not investment advice.</p>')
A('<p class="signoff">Tommy Lau | The Physical Layer | thephysicallayer.fyi</p>')
A('</div>')

html = page_shell("\n".join(P_), FOOT, DLONG).replace("</style>", EXTRA_CSS + "</style>")
hp = f"{D}/{SLUG}_note.html"
open(hp, "w", encoding="utf-8").write(html)
render_pdf(hp, PDF)

import pypdfium2 as pdfium
doc = pdfium.PdfDocument(PDF)
print("pages", len(doc))
doc[0].render(scale=2).to_pil().save(PNG)
print("thumb", PNG)
