# -*- coding: utf-8 -*-
"""GE Vernova (NYSE: GEV) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/ge-vernova.md.
"""
import datetime
from decimal import Decimal, ROUND_HALF_UP
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "GE Vernova (NYSE: GEV)"
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
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"US${q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()

A('<h1 class="doctitle">GE Vernova Inc.</h1>')
A('<p class="docsubtitle"><b>NYSE: GEV | Gas turbines, grid equipment and wind turbines | Cambridge, Massachusetts</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:,.2f} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:,.2f}, NYSE close {PRICE_DATE}; highest close US${HI_CLOSE:,.2f} (30 Jun 2026); intraday high US${HI_INTRA:,.2f} (6 Jul 2026); 52-week low close US${LO_CLOSE:.2f} (4 Nov 2025)"),
    ("Market value", f"About US${MCAP_D:.0f}bn on {SHARES:.1f}m diluted shares ({SHARES_OUT:.1f}m outstanding, 30 Jun 2026)"),
    ("Net cash, 30 Jun 2026", f"US${NETCASH:.1f}bn: cash US${CASH:.1f}bn, borrowings US${DEBT:.1f}bn; customer contract liabilities US${CL_TOTAL:.1f}bn"),
    ("Enterprise value", f"About US${EV:.0f}bn; {EV_EB26:.1f}x 2026 guide adjusted EBITDA, {EV_OUT28:.1f}x the 2028 outlook"),
    ("2026 guide (22 Jul 2026)", "Revenue US$45.5 to 46.5bn; adjusted EBITDA margin 12 to 14%; free cash flow US$11.5 to 12.5bn"),
    ("Gas turbines under contract", f"116 GW at 30 Jun 2026 (53 firm, 63 reserved); at least {GW_YE26} GW expected by year end"),
    ("Consensus (stockanalysis.com)", f"EPS US${CONS_EPS_26:.2f} 2026, US${CONS_EPS_27:.2f} 2027; average target {usd(CONS_TP)} (37 analysts)"),
    ("Next event", "Third quarter 2026 results, 28 October 2026 (confirmed by GE Vernova)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">GE Vernova\'s queue is real and its customers are paying for it. At US$999, the shares already pay for the 2028 plan.</p>')
A(para("GE Vernova builds the large gas turbines that power stations, and now AI campuses, run on, plus grid equipment and wind "
       "turbines. My piece of 9 October argued that the long wait for its turbines is a choice its customers pay for: deposits hold "
       "factory slots for 2030 and 2031, and the money stretches the factories it already has rather than building new ones."))
A(para(f"The filings support the claim. At the end of June GE Vernova had 116 gigawatts under contract, almost six years of its "
       f"20 gigawatt annual output, and US${CL_POWER[-1]:.1f}bn of customer deposits sat in its Power segment, up "
       f"{CL_RISE_H1 * 100:.0f}% in six months. But the same choice caps gas turbine volume to 2028, and the higher prices signed "
       f"this year mostly ship from 2029. At US${PRICE:,.2f} the shares trade at {EV_OUT28:.0f} times the adjusted EBITDA GE Vernova "
       f"expects by 2028; at {BASE_MULT} times, the price needs {NEED_EBITDA28 / OUT28_EBITDA * 100:.0f}% of that outlook."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction.</b> My base case is worth {usd(BASE_VALUE)}, "
       f"{chg(BASE_VALUE)}, inside a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} ({chg(bull)}). I would revisit below "
       f"about US$910, or if GE Vernova lifts its 2028 outlook above US$60bn at a 20% margin."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div class="keeptogether">')
A(section("Key financials (calendar years; adjusted EBITDA is GE Vernova's non-GAAP measure)"))
A(datatable(
    ["US$ billion unless stated", "2024A", "2025A", "2026 guide", "2027E*", "2028E*", "2028 outlook"],
    [
        ["Revenue", f"{REV_H[0]:.1f}", f"{REV_H[1]:.1f}", "45.5 to 46.5", f"{REV27:.1f}", f"{REV28:.1f}", "about 56"],
        ["Revenue growth (%)", "", f"{(REV_H[1] / REV_H[0] - 1) * 100:.0f}", f"{(REV26 / REV_H[1] - 1) * 100:.0f}", f"{G27 * 100:.0f}", f"{G28 * 100:.0f}", ""],
        ["Adjusted EBITDA margin (%)", f"{EBITDA_H[0] / REV_H[0] * 100:.1f}", f"{EBITDA_H[1] / REV_H[1] * 100:.1f}", "12 to 14", f"{M27 * 100:.1f}", f"{M28 * 100:.1f}", "20"],
        ["Adjusted EBITDA", f"{EBITDA_H[0]:.1f}", f"{EBITDA_H[1]:.1f}", f"{EBITDA26:.1f}&dagger;", f"{EBITDA27:.1f}", f"{EBITDA28:.1f}", f"{OUT28_EBITDA:.1f}&dagger;"],
        ["Free cash flow", f"{FCF_H[0]:.1f}", f"{FCF_H[1]:.1f}", "11.5 to 12.5", "", "", "24+ cumulative, 2025 to 2028"],
        ["EV / adjusted EBITDA at US$999.35 (x)", "", "", f"{EV_EB26:.1f}", f"{EV_EB27:.1f}", f"{EV_EB28:.1f}", f"{EV_OUT28:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2027E and 2028E are my own estimates, not GE Vernova's. 2024A and 2025A from the fourth quarter 2025 results release of "
          "28 January 2026. 2026 is the guide of 22 July 2026; growth and EBITDA use its midpoints. The 2028 outlook was set on 28 January "
          "2026 with the Prolec GE acquisition. &dagger;Derived: revenue x margin. No free cash flow forecast for 2027 and 2028: down "
          "payments unwind as turbines ship."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: earnings rising to the 2028 outlook, and a valuation that sits around the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and adjusted EBITDA margin, 2024A to 2028E. 2026G is the guide midpoint; 2027E and 2028E are my estimates. "
          "Right: value per share from the base case, the probability-weighted cases, the sensitivity grid and the bear to bull range, "
          f"against the US${PRICE:,.2f} price (red) and the average analyst target."))
A('</div>')

A(section("The thesis: a workshop sold out for years, with its volume already set"))
A(para("Think of the sofa workshop from the piece. Everyone wants one of its sofas, so it asks for a deposit to hold a delivery week. It "
       "spends the deposits on a second sewing machine and longer shifts, not a second workshop. Its order book stays full for years, "
       "and it can raise its prices on every new booking. That is a fine business. But its output next year is set by the sewing "
       "machines already on the floor, and a buyer gets what those machines can make at the prices already agreed."))
A(para("GE Vernova is that workshop, at the scale of power stations. At the end of June 2026 it had 116 gigawatts of gas turbines under "
       "contract: 53 gigawatts of firm orders and 63 of slot reservation agreements, which are paid holds on future production. It "
       "ships about 20 gigawatts a year from the third quarter of 2026, so the queue is almost six years of output. In the first half "
       "it signed 41 gigawatts and shipped seven."))
A(para(f"The deposits show up where the piece said they would. In Power, the segment that holds Gas Power alongside Nuclear and Hydro "
       f"Power, contract liabilities and current deferred income reached US${CL_POWER[-1]:.1f}bn at the end of June, up "
       f"{CL_RISE_H1 * 100:.0f}% in six months and {CL_MULT_18M:.1f} times the US${CL_POWER[0]:.1f}bn of December 2024. The quarterly "
       "filing ties the rise in cash from operations to higher down payments on orders and slot reservation agreements at Power. "
       f"Customer money held in Power now exceeds the US${POWER_REV_25:.1f}bn of revenue Power booked in all of 2025."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_queue.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_deposits.png"></div></div>')
A(caption("Left: gigawatts under contract at quarter end, firm orders and slot reservations; white figures are years of output at 20 GW a "
          "year (derived). Q2 25 is 29 + 25, stated by GE Vernova as 55. Right: Power contract liabilities and current deferred income, "
          "US$bn. December 2024 and September 2025 are on the segment basis before the January 2026 realignment; the December 2025 "
          "figure is the same on both bases. Sources: results releases, 23 April 2025 to 22 July 2026; Form 10-K for 2025; Forms 10-Q, "
          "Note 9."))
A('</div>')
A(para("The capacity plan matches the claim too. On the July call the chief executive set out 20 gigawatts a year now, 24 in 2028 and "
       "30 in 2030, from lean methods and new machinery inside the existing factory footprint, all funded by customer down payments. "
       f"He expects at least {GW_YE26} gigawatts under contract by the end of 2026, mostly sold out through 2030 and more than half of "
       "2031 sold."))
A(para("<b>The claim holds on every test it set.</b> The queue sits at 5.8 years against a floor of four. There is no new heavy-duty "
       "factory. Deposits are rising and so is price: first half equipment orders were priced more than 20% above those of the fourth "
       "quarter of 2025. Nothing in the filings shows the piece was wrong."))
A(para(f"The claim's floor does rise. Four years of output is {NEED_GW['2026']} gigawatts today, {NEED_GW['2028']} from 2028 and "
       f"{NEED_GW['2030']} from 2030. To stay above it in 2030, GE Vernova must keep signing contracts for 2033 and beyond while "
       "shipping 30 gigawatts a year. On the July call it said it needs more time before it can say when 2032 will be contracted."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:,.2f} GE Vernova is worth about US${MCAP_D:.0f}bn on its diluted shares. Net cash is about US${NETCASH:.1f}bn, "
       f"so the enterprise value is about US${EV:.0f}bn. That is {EV_EB26:.0f} times the midpoint of its 2026 adjusted EBITDA guide, "
       f"about US${EBITDA26:.1f}bn. On stockanalysis.com's forward earnings measure the shares trade at {FWD_PE_SA:.1f} times, "
       "against a peer median of 24.0 times on the same measure."))
A(para(f"The fairer yardstick is the outlook by 2028: revenue of about US$56bn at a 20% margin, or about US${OUT28_EBITDA:.1f}bn of "
       f"adjusted EBITDA. The shares trade at {EV_OUT28:.0f} times that. At my base multiple of {BASE_MULT} times, the price needs "
       f"2028 adjusted EBITDA of about US${NEED_EBITDA28:.1f}bn, {NEED_EBITDA28 / OUT28_EBITDA * 100:.0f}% of the company's own "
       f"outlook. The market already assumes GE Vernova delivers its 2028 plan. The average target of 37 analysts is "
       f"{usd(CONS_TP)}, {(CONS_TP / PRICE - 1) * 100:.0f}% above the price. I differ on three points."))
A(para("<strong class='lead'>The claim caps the volume.</strong> If GE Vernova keeps expanding inside its own walls, gas turbine "
       "shipments are set: about 20 gigawatts in 2027 and 24 in 2028, with the castings and forgings for the 2028 step arriving in 2027. "
       "There is no route to shipping much more before 2029, which is exactly what keeps the queue long. Growth to 2028 comes from "
       "price, services, the grid business and the wind recovery, not from more turbines."))
A(para("<strong class='lead'>The new prices land late.</strong> Orders signed this year at higher prices mostly ship in 2029 to 2031, "
       "and the chief executive said a heavy-duty unit can then take another 18 months at site to commission. The 2028 outlook was set before most of those prices "
       "were agreed, so some upside is real, but most of it shows up beyond the year the market will price by October 2027."))
A(para(f"<strong class='lead'>The cash flow is flattered by deposits.</strong> The 2026 free cash flow guide of US$11.5 to 12.5bn is "
       f"about {FCF_TO_EBITDA26:.0f} times adjusted EBITDA, because customers pay years before delivery. GE Vernova expects the second "
       f"half to be well below the first as reservations convert. All its contract liabilities, US${CL_TOTAL:.1f}bn, are three times its "
       f"cash. I value it on EBITDA, not on a {FCF_YIELD26 * 100:.1f}% free cash flow yield that will not repeat."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["28 Jan 2026", "Q4 2025 results; outlook by 2028 raised to about US$56bn revenue with Prolec GE", "up 2.7%"],
        ["22 Apr 2026", "Q1 results; gigawatts under contract reach 100; 2026 guide raised", f"up {Q1_MOVE * 100:.1f}%"],
        ["30 Jun 2026", f"Highest close, US${HI_CLOSE:,.2f}", "Peak"],
        ["22 Jul 2026", "Q2 results; 2026 revenue and free cash flow guide raised", f"down {abs(Q2_MOVE) * 100:.1f}%"],
        ["8 Oct 2026", f"Close of US${PRICE:,.2f}, {abs(OFF_HIGH) * 100:.0f}% below the highest close", ""],
    ],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: GE Vernova month-end close, April 2024 to the 8 October 2026 close, against my base value (red). Nasdaq.com historical "
          "data, retrieved 9 October 2026. Right: moves on results days, close to close, from the same data."))
A('</div>')

A(section("Valuation, with the working"))
A(para("I value GE Vernova on enterprise value to adjusted EBITDA. Its reported earnings per share swing with one-off gains, such as the "
       "US$4.0bn gain on Prolec GE this year, and the company guides on adjusted EBITDA. The horizon is twelve months, to October 2027, "
       "when the market will price 2028. Growth of 11% a year carries the 2026 guide midpoint just above the 2028 outlook, which was "
       "set before GE Vernova raised its 2026 revenue guide by US$1.5bn. The 2028 margin is the company's own 20%; 2027 sits halfway."))
A(para(f"<b>The multiple: {BASE_MULT} times.</b> I use {BASE_MULT} times 2028 adjusted EBITDA for the base case, between Siemens "
       "Energy at 22.1 times trailing EBITDA and Eaton at 27.9 times (stockanalysis.com, 9 October). A queue sold into the 2030s deserves "
       "no discount to Siemens Energy, but by October 2027 the 2028 figure will be only a year away. I add the net cash of June 2026 "
       f"and divide by {SHARES:.1f}m diluted shares, with no buybacks assumed. {BASE_MULT} x US${EBITDA28:.2f}bn + US${NETCASH:.2f}bn = "
       f"{usd(BASE_VALUE)} a share."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 revenue", "2028 EBITDA", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "Gas orders peak, reservations convert slowly; growth 6% a year, margin 16.5% in 2027, 17% in 2028", f"US${RV28[0]:.1f}bn", f"US${EB28[0]:.1f}bn", f"{SCEN[0][4]}x", usd(bear), chg(bear), "25%"],
        ["Base", "Revenue and margin at the 2028 outlook", f"US${RV28[1]:.1f}bn", f"US${EB28[1]:.1f}bn", f"{SCEN[1][4]}x", usd(base), chg(base), "50%"],
        ["Bull", "Price and services lift margin to 22%; growth 15% a year", f"US${RV28[2]:.1f}bn", f"US${EB28[2]:.1f}bn", f"{SCEN[2][4]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [9, 33, 11, 11, 8, 11, 9, 8]))
A(caption("All cases start from the 2026 guide midpoint of US$46.0bn, keep my 16.5% margin for 2027, and add the same net cash over the same diluted shares. The bear "
          "multiple is about where Mitsubishi Heavy trades on trailing EBITDA; the bull multiple is what a market convinced the queue "
          "runs into the 2030s might pay."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 adjusted EBITDA against the multiple"))
A('<div class="chartsrow"><div class="col left">')
grid = [[value(e, m) for m in SENS_MULT] for e in SENS_EBITDA]
A(datatable(
    ["2028 EBITDA"] + [f"{m}x" for m in SENS_MULT],
    [[f"US${e:.1f}bn"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_EBITDA, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
A(para(f"{n_above} of the nine cells sit above the price, but only {n_15} sit 15% or more above it, and each of those needs a higher "
       "multiple or EBITDA above the outlook. Under my rule, a long needs the base value 15% or more above the price and a "
       f"short needs it 25% or more below. At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, my call is no call."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBITDA", "What they make"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w in PEERS],
    num_cols={2, 3},
), [17, 12, 11, 11, 49]))
A(caption("Forward P/E and trailing EV/EBITDA from stockanalysis.com, retrieved 9 October 2026; peer median 24.0x forward P/E and 18.4x "
          "EV/EBITDA. Multiples are used only to set the range for GE Vernova; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Power: the segment that holds the queue"))
A('<div class="chartsrow"><div class="col left">')
A(f'<img class="chart" src="file://{D}/chart_power.png">')
A('</div><div class="col">')
A(para("Power revenue grew 14% in the second quarter, led by aeroderivative volume and price, and its segment EBITDA margin "
       "reached 18.8%, against the 22% GE Vernova targets by 2028. On the July call the chief financial officer said he expects "
       "third quarter Power revenue to grow 17 to 19% at a margin of about 17 to 18%, the seasonally lowest quarter for services. Power orders were US$16.7bn in the quarter, three "
       "times revenue."))
A('</div></div>')
A(caption("Power revenue and segment EBITDA margin by quarter, as first reported; 2026 is on the segment basis realigned on 1 January "
          "2026. Source: GE Vernova quarterly results releases and the second quarter 2026 earnings call."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["28 October 2026 (confirmed)", "Third quarter 2026 results", "Gigawatts under contract on the way to at least 125; reservations converting to orders; Power margin against 17 to 18%"],
        ["Early 2027 (date not announced)", "Fourth quarter results and the 2027 guide", "Any update to the outlook by 2028; 2026 adjusted EBITDA margin against the 12 to 14% guide"],
        ["2027", "Castings and forgings arrive", "On time for the 24 GW output step in 2028"],
        ["Each quarter", "Results and Form 10-Q", "Power contract liabilities; whether 2032 slots start to sell; any new heavy-duty factory"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Peak orders.</strong> On the July call an analyst asked whether 2026 is the peak year for gas turbine orders. GE Vernova "
       "expects gigawatts under contract to keep growing through 2027. If they stop growing while it ships 20 gigawatts a year, the "
       "queue shrinks and the multiple falls with it. That is most of the bear case."))
A(para("<strong>Reservations are not orders.</strong> More than half the queue is slot reservations, which become orders only when a "
       "project has a schedule, a gas pipeline and a builder. I could not verify from GE Vernova's own filings how much of each deposit "
       "is refundable. A wave of lapsed reservations would test the claim directly."))
A(para("<strong>The output steps.</strong> The 24 gigawatt step in 2028 waits on castings and forgings from outside suppliers, due in "
       "2027. A slip delays revenue the 2028 outlook needs."))
A(para("<strong>A new factory.</strong> The claim is wrong if GE Vernova announces a new heavy-duty turbine factory. For the shares that "
       "would be mixed: more volume later, but a shorter queue and weaker pricing."))
A(para("<strong>Wind.</strong> GE Vernova expects Wind to lose about US$400m of segment EBITDA in 2026. Offshore project costs rose in "
       "the second quarter and onshore orders in the United States stay soft, so the recovery my growth rates assume may come later."))
A(para("<strong>Competition.</strong> Siemens Energy, Mitsubishi Heavy and Ansaldo Energia also build heavy-duty turbines. On the July "
       "call the chief executive said that, on his view of heavy-duty capacity across the industry, supply looks very balanced with "
       "demand for the next six years, but that he finds it harder to judge how much smaller machines will add."))
A(para("<strong>A new chief financial officer.</strong> On 25 August GE Vernova said (Form 8-K) that Kenneth Parks will retire and "
       "Claire McDonough, now finance chief of Rivian, becomes chief financial officer on 1 January 2027, ahead of the results that "
       "carry the 2027 guide."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price below about US${round(REVISIT_LONG, -1):,.0f}, where my base value would sit 15% above "
       "it on unchanged estimates, or GE Vernova raising its 2028 outlook above US$60bn of revenue at a 20% margin. "
       f"<strong>Towards a short:</strong> a price above about US${round(REVISIT_SHORT, -2):,.0f}, where my base value would sit 25% below it."))
A(para(f"<strong>The view is wrong if</strong> {WRONG_IF[0].lower() + WRONG_IF[1:]}"))
A('</div>')

A(section("Conclusion"))
A(para("The October piece argued that GE Vernova's customers are paying for a place in a queue that will stay years long. Its filings "
       f"say so: 116 gigawatts under contract, almost six years of output, and US${CL_POWER[-1]:.1f}bn of deposits in Power. Nothing I "
       "found says the piece was wrong. One simplification: the piece called Power \"its gas turbine segment\" and read the deposits "
       "as gas turbine deposits, while Power also holds Nuclear and Hydro Power; the filing ties the rise to gas orders and slot "
       "reservations, so the claim stands. But the same choice that keeps the queue long sets the volume to 2028, and the higher prices "
       f"signed this year mostly arrive after it. At US${PRICE:,.2f} the shares already pay for GE Vernova reaching its own 2028 "
       f"outlook. {my_call}: {CALL['direction']}, {conv} conviction; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026", "2027E", "2028E", "Basis"],
    [
        ["Revenue growth", f"{(REV26 / REV_H[1] - 1) * 100:.0f}% (guide midpoint)", f"{G27 * 100:.0f}%", f"{G28 * 100:.0f}%", "Carries the 2026 guide just above the US$56bn 2028 outlook"],
        ["Adjusted EBITDA margin", f"{M26 * 100:.0f}% (guide midpoint)", f"{M27 * 100:.1f}%", f"{M28 * 100:.0f}%", "2028 at GE Vernova's own outlook; 2027 halfway"],
        ["Net cash, US$bn", f"{NETCASH:.2f}", "", "", "30 June 2026, held flat"],
        ["Diluted shares, m", f"{SHARES:.1f}", "", "", "30 June 2026 outstanding plus dilutive equivalents; no buybacks"],
        ["Multiple, EV / 2028 adjusted EBITDA", "", "", f"{BASE_MULT}x", "Between Siemens Energy (22.1x) and Eaton (27.9x), trailing"],
    ],
), [27, 18, 9, 9, 37]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">GE Vernova quarterly results releases on Form 8-K, Exhibit 99, of 23 April 2025, 23 July 2025, 22 October '
  '2025, 28 January 2026, 22 April 2026 and 22 July 2026, for revenue, adjusted EBITDA, free cash flow, Power results, gigawatts signed, '
  'shipped and under contract, the 2026 guide and the outlook by 2028. GE Vernova Form 10-Q for the quarter to 30 June 2026, filed '
  '22 July 2026, for shares, cash, borrowings (Note 14), contract liabilities by segment (Note 9), the cash flow explanation and the '
  'Prolec GE gain. GE Vernova Forms 10-Q to 30 September 2025 and 31 March 2026 and Form 10-K for 2025, filed 29 January 2026, for '
  'earlier contract liabilities. GE Vernova second quarter 2026 earnings call, 22 July 2026, transcript on gevernova.com, for the '
  'output plan, funding, pricing, commissioning times, sold-out comments and the third quarter outlook. GE Vernova Form 8-K of 25 August '
  '2026 on the chief financial officer. GE Vernova investor events page '
  'for the 28 October 2026 results date. Share prices from Nasdaq.com historical data; consensus, average target and peer multiples '
  'from stockanalysis.com (S&amp;P Global data, updated 1 October 2026) and MarketBeat; all retrieved 9 October 2026. Estimates for 2027 '
  'and 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 9 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/ge-vernova-sells-the-wait/">thephysicallayer.fyi/journal/ge-vernova-sells-the-wait</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in GE Vernova. Personal research, not investment advice.</p>')
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
