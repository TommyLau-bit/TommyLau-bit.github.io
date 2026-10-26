# -*- coding: utf-8 -*-
"""Eaton Corporation plc (NYSE: ETN) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/eaton.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Eaton Corporation plc (NYSE: ETN)"
DLONG = datetime.date.fromisoformat(DATE).strftime("%-d %B %Y")

EXTRA_CSS = """
a { color: #1F3864; text-decoration: none; }
.chartsrow { break-inside: avoid; margin-top: 2px; }
.keeptogether { break-inside: avoid; }
table.datatable.compact td { padding: 2.6px 7px; font-size: 8.5pt; }
table.datatable.compact th { padding: 4px 7px; font-size: 8.5pt; }
p.lede { font-size: 10.4pt; font-weight: 700; color: #1F3864; margin: 0 0 6px 0; line-height: 1.28; }
.fullwidth > p.body { clear: both; }
p.draftnote { font-size: 8.2pt; color: #C00000; font-weight: 700; margin: -6px 0 8px 0; }
"""

P_ = []
A = P_.append


def cols(html, widths):
    cg = "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in widths) + "</colgroup>"
    i = html.index(">") + 1
    return html[:i].replace('class="datatable', 'style="table-layout:fixed" class="compact datatable') + cg + html[i:]


def usd(x, d=0):
    return f"US${x:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def m(x):
    return f"{x:,.0f}"


bear, base, bull = (x["value"] for x in SC)
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
tgt_word = "draft target" if CALL["draft"] else "target"
g_mid = (GUIDE26["eps_lo"] + GUIDE26["eps_hi"]) / 2

A('<h1 class="doctitle">Eaton Corporation plc</h1>')
A('<p class="docsubtitle"><b>NYSE: ETN | Switchgear, UPS, power distribution and liquid cooling for data centres; aerospace | Dublin, Ireland</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{usd(PRICE, 2)} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{usd(PRICE, 2)}, NYSE close {PRICE_DATE}; record close {usd(HI_CLOSE, 2)} and intraday high {usd(HI_INTRA, 2)} on 12 Aug 2026"),
    ("Market value", f"US${MCAP:.1f}bn on {SHARES_OUT}m shares (30 Jun 2026)"),
    ("Net debt, 30 Jun 2026", f"US${NET_DEBT / 1000:.1f}bn after Boyd Thermal; enterprise value about US${EV:.0f}bn"),
    ("2026 guide (31 Jul 2026)", f"Adjusted EPS US$13.40 to 13.60; organic growth 11 to 13%; segment margin 24.1 to 24.5%"),
    ("P/E", f"{PE_G26:.1f}x 2026 guide midpoint; {PE_C27:.1f}x 2027 consensus (US${CONS_EPS27:.2f}); {PE_E28:.1f}x my 2028E"),
    ("Electrical Americas queue", f"Backlog US$15.2bn at 30 Jun 2026: {EA_MONTHS[-1]:.1f} months of trailing sales, from {EA_MONTHS[2]:.1f} a year earlier"),
    ("Consensus (stockanalysis.com)", f"Average target {usd(CONS_TP)} ({CONS_N} analysts); forward P/E {FWD_PE_SA:.1f}x"),
    ("Next event", "Q3 2026 results, 3 November 2026, before the NYSE opens (announced by Eaton)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Eaton has a year of orders waiting. At US$366, the shares price in the margin it lost this year, not the margin it gets back.</p>')
A(para("Eaton's Electrical Americas business makes switchgear, UPS systems, busway and prefabricated electrical rooms, the equipment "
       "inside a data centre's fence. My piece of 26 October argued that its queue keeps lengthening even as it ships more. At the end "
       f"of June its backlog equalled {EA_MONTHS[-1]:.1f} months of sales, up from {EA_MONTHS[2]:.1f} a year earlier."))
A(para("The claim holds. The queue also cut this year's margin, because orders priced months earlier met higher metal costs, and Eaton "
       f"expects that gap to close in the second half. The shares fell {abs(OCT_FALL) * 100:.1f}% from 13 to 23 October with no new "
       f"results, and now trade at {PE_E28:.1f} times my 2028 earnings for Eaton without Mobility."))
A(para(f"<b>{my_call}: {CALL['direction']}, {tgt_word} {usd(tgt)}, {conv} conviction.</b> Twenty-three times my 2028 EPS of "
       f"US${E28:.2f} gives {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, inside a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} "
       f"({chg(bull)}). Conviction is low because the base clears my 15% bar by only three points."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (calendar years; adjusted EPS as Eaton defines it)"))
A(datatable(
    ["US$ million unless stated", "2024A", "2025A", "2026E*", "2027E*", "2028E*"],
    [
        ["Electrical Americas sales", "11,436", m(SEG25["EA"][0]), m(S26["EA"][0]), m(B["s27"]["EA"]), m(B["s28"]["EA"])],
        ["Growth (%)", "", f"{(SEG25['EA'][0] / 11436 - 1) * 100:.0f}", f"{EA_G26 * 100:.0f}", f"{EA_G27 * 100:.0f}", f"{EA_G28 * 100:.0f}"],
        ["Electrical Americas margin (%)", "30.2", "29.9", f"{EA_M26 * 100:.1f}", f"{EA_M27 * 100:.1f}", f"{EA_M28 * 100:.1f}"],
        ["Group sales&dagger;", "24,878", "27,448", m(SALES26), m(B["sales27"]), m(B["sales28"])],
        ["Segment margin (%)", "24.0", "24.5", f"{SEGM26 * 100:.1f}", f"{B['op27'] / B['sales27'] * 100:.1f}", f"{B['op28'] / B['sales28'] * 100:.1f}"],
        ["Adjusted EPS (US$)", "10.80", "12.07", f"{EPS26:.2f}", f"{E27:.2f}", f"{E28:.2f}"],
        ["Guide midpoint / consensus EPS (US$)", "", "", f"{g_mid:.2f}", f"{CONS_EPS27:.2f}", ""],
        [f"P/E at {usd(PRICE, 2)} (x)", "", "", f"{PE_G26:.1f}", f"{PE_E27:.1f}", f"{PE_E28:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*2026E is Eaton's first half results plus my second half; 2027E and 2028E are my estimates for continuing operations. "
          "&dagger;2027E and 2028E exclude Mobility (US$3.1bn of sales in 2025), which Eaton plans to combine with Dana in Q1 2027. "
          "2024A and 2025A from Eaton's releases. 2026 P/E on the guide midpoint. Consensus from stockanalysis.com, updated 20 October 2026; the 2027 consensus appears to include Mobility, so it is not directly comparable with my 2027E."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: the margin that has to come back, and a value above the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: Electrical Americas sales and operating margin; 2024A and 2025A per Eaton, 2026E to 2028E mine. Right: value per share from "
          f"the base case, the weighted cases, the sensitivity grid and the bear to bull range, against the {tgt_word} (red) and the price (grey)."))
A('</div>')

A(section("The thesis: a year-long queue, priced before the metal went up"))
A(para("Think of the bakery from the piece before a holiday. The queue runs out of the door, and the owner has taken orders weeks ahead at "
       "prices written on the order slips. Then the price of flour jumps. Every cake already promised is baked at the old price on new "
       "flour, so the owner earns less on each one until the old orders clear and the new slips carry the new price."))
A(para(f"Eaton's Electrical Americas business is that bakery. Its backlog was US$15.2bn at the end of June 2026, against US$14.5bn of sales "
       f"over the previous four quarters: {EA_RATIO[-1]:.2f} years, or {EA_MONTHS[-1]:.1f} months. The ratio was {EA_MONTHS[1]:.1f} months "
       f"in March 2025 and {EA_MONTHS[2]:.1f} in June 2025, and has risen in each quarter since. Over the year to June, trailing sales grew "
       f"{EA_SALES_GROWTH_TTM * 100:.0f}% and the backlog {EA_BL_GROWTH * 100:.0f}%. Twelve-month orders were up 41% organically, and book "
       "to bill was 1.3. The ratio is my arithmetic and a proxy, not a lead time: some of the rise is price, which Eaton does not split out."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_queue.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_qmargin.png"></div></div>')
A(caption("Left: Electrical Americas backlog at quarter end, US$bn; white figures are months of sales on order (derived). Sources: Form 10-K 2025 "
          "and Form 10-Qs. Right: Electrical Americas operating margin by quarter, Q1 2024 to Q2 2026; red bars are the two quarters of 2026. "
          "Sources: Eaton quarterly earnings releases, 1 August 2024 to 31 July 2026."))
A('</div>')
A(para("<b>The queue had a cost.</b> Electrical Americas earned 29.9% in 2025, and between 29.2% and 31.6% in every quarter of 2024 and 2025. "
       "In the first quarter of 2026 the margin fell to 25.6%; the 10-Q puts 480 basis points of that down to commodity inflation and 100 "
       "to the cost of growth projects. In the second quarter it recovered to 27.5%, still 2 points below a year earlier, after a 470 basis "
       "point commodity hit. On the call of 31 July, according to a third-party transcript, management said most of the fall was a temporary gap between price and cost and, after "
       "price rises in the second quarter and early third, expected it to be roughly neutral in the second half."))
A(para("My reading is the bakery's: orders priced months earlier were still shipping on more expensive metal. If so, the margin returns as "
       "the old orders clear, and the longer queue then carries the new prices. Electrical Americas earned 59% of Eaton's segment profit "
       "in 2025. Each point of its 2028 margin is worth about US$0.44 a share on my estimates, about US$10 at my multiple."))
A(para("Eaton is also changing shape. It bought Boyd Thermal, a liquid cooling maker, for US$9.55bn in March 2026 and Ultra PCS, aerospace "
       "electronics, for US$1.53bn in January. It plans to combine Mobility, its truck and car parts business, with Dana in Q1 2027, "
       "receiving about US$1.1bn in cash while its shareholders own at least 50.1% of the combined company."))
A(para("<b>Nothing in Eaton's filings shows the piece was wrong.</b> The ratio has risen five quarters running, orders run ahead of "
       "sales, and the plants the piece named are still due in 2027. One caveat strengthens it: the June 2025 backlog included Fibrebond, "
       "bought on 1 April 2025, while that date's trailing sales held only one quarter of it, so the rise since is if anything understated. "
       f"On my Q3 sales estimate of about US$4.0bn, the September backlog needs to exceed about US$15.8bn for the ratio to keep rising."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {usd(PRICE, 2)} Eaton is worth US${MCAP:.1f}bn. Net debt was US${NET_DEBT / 1000:.1f}bn at the end of June, so the enterprise "
       f"value is about US${EV:.0f}bn. The shares trade at {PE_G26:.1f} times the 2026 guide midpoint and {PE_C27:.1f} times the 2027 "
       f"consensus of US${CONS_EPS27:.2f}, which appears to include Mobility; at the August high they traded at {PE_PEAK_G26:.1f} times the guide. Eaton's forward P/E is "
       f"{FWD_PE_SA:.1f} times against a 20.5 times median for seven electrical peers, and averaged {HIST_FWD_PE_AVG:.1f} times from 2021 to "
       f"2025 (stockanalysis.com). The average target of {CONS_N} analysts is {usd(CONS_TP)}."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["5 May 2026", "Q1 results; EA margin 25.6%; 2026 guide raised", f"down {abs(Q1_MOVE) * 100:.1f}%"],
        ["31 Jul 2026", "Q2 results; EA margin 27.5%; guide raised to US$13.40 to 13.60", f"up {Q2_MOVE * 100:.1f}%"],
        ["12 Aug 2026", f"Record close {usd(HI_CLOSE, 2)}", "Peak"],
        ["14 to 23 Oct", "AI infrastructure sell-off; no Eaton results", f"down {abs(OCT_FALL) * 100:.1f}%"],
    ],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: Eaton month-end close, January 2024 to the 23 October 2026 close, against my base value (red). Yahoo Finance, retrieved 26 October "
          "2026. Right: moves from the previous close to the close on the results day (results come before the open), and from 13 to 23 October."))
A('</div>')
A(para("I read the October fall as the market pricing two worries: that AI data centre spending is near a peak, and that this year's lower "
       "margin is the new normal. I differ on both."))
A(para(f"<strong class='lead'>The queue answers most of the first worry for 2027.</strong> With {EA_MONTHS[-1]:.1f} months of sales on order, "
       "and capacity setting the pace of shipments, a slowdown in orders would shorten the queue before it cut sales. My base case grows "
       f"Electrical Americas {EA_G27 * 100:.0f}% in 2027, close to Q2's 18% organic, and {EA_G28 * 100:.0f}% in 2028, when new plants add capacity."))
A(para("<strong class='lead'>The margin is the real variable, and it should come back.</strong> I take Electrical Americas to 30.5% in the "
       "second half of 2026, 30.0% in 2027 and 30.5% in 2028: the level of 2024 and 2025, not above it. That matches Eaton's own guide of a "
       "24.6 to 25.0% segment margin in Q3 and 24.1 to 24.5% for 2026, against 22.9% in the first half."))
A(para(f"<strong class='lead'>The price pays {PE_E28:.1f} times my 2028 earnings.</strong> Without Mobility, I estimate US${E27:.2f} a share in "
       f"2027 and US${E28:.2f} in 2028; the 2027 consensus appears to include Mobility, so the two are not directly comparable. Year for "
       f"year, the price is {PE_E27:.1f} times my 2027 estimate against a 20.5 times peer median forward P/E, a premium of about two turns, "
       "for a business with a year of orders waiting and earnings growing about 18% a year."))

A(section("Valuation, with the working"))
A(para("I value Eaton on adjusted EPS, twelve months out: by October 2027 the market will price 2028 as the year ahead. I build each segment's "
       f"sales and margin and bridge to EPS. For 2026, first half actuals plus my second half, corporate costs of US$790m, net interest of "
       f"US$710m and a 19% tax rate give US${EPS26:.2f}, against Eaton's guide midpoint of US$13.50. For 2027 and 2028 I remove Mobility, cut "
       f"interest to US$680m and US$580m as debt is repaid, and retire {SHARES_RETIRED:.0f}m shares in the Mobility exchange offer. All are my estimates."))
A(para(f"<strong class='lead'>The multiple.</strong> I use {BASE_PE:.0f} times 2028 earnings: one turn below Eaton's own {HIST_FWD_PE_AVG:.1f} "
       "times average forward P/E of 2021 to 2025, because AI sentiment has cooled, and above the 20.5 times peer median because Eaton's "
       f"earnings grow about 18% a year on my estimates. {BASE_PE:.0f} x US${E28:.2f} = {usd(BASE_VALUE, 2)}, rounded down to a "
       f"{tgt_word} of {usd(tgt)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "AI orders pause in 2027; EA growth 8% then 4%, margin slips to 27.5%", f"US${SC[0]['e28']:.2f}", f"{SC[0]['mult']}x", usd(bear), chg(bear), "25%"],
        ["Base", "EA growth 16% then 13%, margin back to 30 to 30.5%", f"US${SC[1]['e28']:.2f}", f"{SC[1]['mult']:.0f}x", usd(base), chg(base), "50%"],
        ["Bull", "Capacity early; EA growth 19% then 16%, margin 31.5%", f"US${SC[2]['e28']:.2f}", f"{SC[2]['mult']}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 41, 11, 9, 11, 11, 8]))
A(caption("All cases start from my 2026E segment sales and use the same bridge. Electrical Global and Aerospace growth moves 3 points down or 2 "
          "up and their margins 1 point down or half a point up. The bear case is close to a quarter below the price."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
grid = [[e * mm for mm in SENS_PE] for e in SENS_EPS]
A(datatable(
    ["2028 EPS"] + [f"{mm}x" for mm in SENS_PE],
    [[f"US${e:.2f}"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
A(para(f"{W[n_above]} of the nine cells sit above the price, but only {W[n_15].lower()} sit 15% or more above it. At 22 times my 2028 EPS the base value "
       f"would be 13% above the price, inside the no call band. A long needs the base 15% or more above the price, a short 25% or more "
       f"below. At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, {my_call.lower()} is long, with low conviction."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBIT", "What they make"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w, g in PEERS],
    num_cols={2, 3},
), [18, 13, 11, 10, 48]))
A(caption("Forward P/E and trailing EV/EBIT from stockanalysis.com, retrieved 26 October 2026. Peer median excluding Eaton: 20.5x forward P/E, "
          "22.9x EV/EBIT. GE Vernova is left out: its trailing EV/EBIT of 76x reflects earnings still recovering. Multiples are used only to "
          "set the range; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["3 November 2026 (announced)", "Q3 2026 results, before the NYSE opens", "EA margin against 30.3% a year earlier; September backlog against about US$15.8bn; adjusted EPS against US$3.46 to 3.56"],
        ["Early 2027 (date not announced)", "Q4 2026 results and 2027 guide", "EA margin above 29% in Q4; 2026 EPS against the US$13.40 bottom of the guide"],
        ["Q1 2027", "Mobility combined with Dana", "Exchange offer terms; shares retired; use of the ~US$1.1bn cash"],
        ["2027", "South Carolina transformer and Nebraska switchgear plants start", "On time; whether Eaton says its extended lead times are shrinking"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>AI spending turns.</strong> On the Q2 call, per a third-party transcript, management said data centre sales in Electrical Americas were up about 65%. "
       "A cut by the largest cloud companies would show first in orders, then in the queue. That is the bear case, a 26% fall."))
A(para("<strong>The margin does not come back.</strong> If metal costs keep rising faster than Eaton can reprice, the gap could last into "
       "2027. Each point of 2028 EA margin is worth about US$10 a share at my multiple."))
A(para("<strong>The new capacity is slow.</strong> Eaton is spending more than US$1bn on about two dozen capacity projects in the Americas. "
       "New lines run on overtime and new operators at first. A third plant, for enclosures, is announced in Arkansas."))
A(para(f"<strong>Debt and deals.</strong> Net debt rose from US$9.1bn at the end of 2025 to US${NET_DEBT / 1000:.1f}bn, mostly for Boyd "
       "Thermal, and Eaton bought back no shares in the first half. The Dana transaction needs Dana's shareholders and regulators. If it "
       "becomes a pro rata spin-off, no shares are retired and my 2028 EPS falls about 2.6%."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into no call:</strong> a weak EA margin in Q3 or Q4, or the queue falling for two quarters. On unchanged estimates, the base "
       f"value sits 15% above any price below about {usd(LONG_BELOW)}, and 25% below any price above about {usd(BASE_VALUE / 0.75)}."))
A(para(f"<strong>{'My draft view' if CALL['draft'] else 'My call'} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para(f"The October piece argued that Eaton's queue in the Americas keeps lengthening even as it ships more. Its filings agree: "
       f"{EA_MONTHS[-1]:.1f} months of sales on order in June, up from {EA_MONTHS[2]:.1f}, with orders 1.3 times sales. Nothing I found "
       "says the piece was wrong. The queue cut this year's margin, because orders priced months ago met higher metal costs; Eaton expects "
       f"that gap to close in the second half. At {usd(PRICE, 2)} the market pays {PE_E27:.1f} times my 2027 and {PE_E28:.1f} times my 2028 earnings. {my_call}: "
       f"{CALL['direction']}, {tgt_word} {usd(tgt)}, {conv} conviction; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["EA sales growth", f"{EA_G26 * 100:.0f}%", f"{EA_G27 * 100:.0f}%", f"{EA_G28 * 100:.0f}%", "Near Q2's 18% organic; capacity sets the pace"],
        ["EA operating margin", f"{EA_M26 * 100:.1f}% (H2 30.5%)", f"{EA_M27 * 100:.1f}%", f"{EA_M28 * 100:.1f}%", "Back to the 2024 and 2025 level"],
        ["Electrical Global margin", f"{S26['EG'][1] / S26['EG'][0] * 100:.1f}%", f"{EG_M27 * 100:.1f}%", f"{EG_M28 * 100:.1f}%", "Boyd Thermal in for a full year"],
        ["Aerospace margin", f"{S26['AE'][1] / S26['AE'][0] * 100:.1f}%", f"{AE_M27 * 100:.1f}%", f"{AE_M28 * 100:.1f}%", "First half 2026: 24.6%"],
        ["Interest, US$m", f"{INT26:.0f}", f"{INT27:.0f}", f"{INT28:.0f}", "Debt repaid from Dana cash and free cash flow"],
        ["Tax rate", "19%", "19%", "19%", "Reproduces the 2026 guide midpoint"],
        ["Diluted shares, m", f"{SHARES_DIL}", f"{SHARES_27}", f"{SHARES_27}", "Less 10m in the exchange offer; no buybacks"],
    ],
), [26, 18, 11, 11, 34]))
A(caption(f"All my estimates. Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Eaton second quarter 2026 earnings release (Form 8-K, Exhibit 99) and Form 10-Q, 31 July 2026, for segment sales '
  'and profit, the adjusted EPS bridge, the balance sheet, guidance, backlog, book to bill and the margin bridge. Eaton Form 10-Qs for the '
  'quarters to 31 March 2025, 30 September 2025 and 31 March 2026, and the 2025 Form 10-K, for backlog and margin. Eaton quarterly earnings '
  'releases from 1 August 2024 to 5 May 2026 for segment results by quarter. Eaton Form 8-K of 11 June 2026 on the Mobility and Dana '
  'transaction, and of 16 October 2026 recasting 2025 segments. Eaton\'s announcement of its 3 November 2026 results date. Eaton second '
  'quarter 2026 earnings call, 31 July 2026, from a third-party transcript (Motley Fool). Plant announcements of 12 February 2025, 8 April '
  '2026 and 2 September 2026, confirmed through trade press. Share prices from Yahoo Finance; consensus, targets and peer multiples from '
  'stockanalysis.com (S&amp;P Global data); all retrieved 26 October 2026. Estimates for the second half of 2026, 2027 and 2028 are the '
  'author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 26 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/eaton-order-book-outruns-it/">thephysicallayer.fyi/journal/eaton-order-book-outruns-it</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Eaton. Personal research, not investment advice.</p>')
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
