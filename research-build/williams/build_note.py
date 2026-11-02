# -*- coding: utf-8 -*-
"""The Williams Companies (NYSE: WMB) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/williams.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "The Williams Companies, Inc. (NYSE: WMB)"
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


def usd(x, d=2):
    return f"US${x:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def m(x):
    return f"{x:,.0f}"


def bn(x, d=1):
    return f"US${x / 1000:,.{d}f}bn"


bear, base, bull = (x["value"] for x in SC)
tgt = CALL["target"]
tp_txt = usd(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({UP_BASE * 100:+.1f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
dirw = CALL["direction"].lower()
pi_share28 = PI28 / EB28
turn_pipes = (GRID[2][0] - GRID[0][0]) / 3
turn_power = (GRID[0][2] - GRID[0][0]) / 4
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
n_above = sum(v > PRICE for r in GRID for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in GRID for v in r)

A('<h1 class="doctitle">The Williams Companies, Inc.</h1>')
A('<p class="docsubtitle"><b>NYSE: WMB | Gas pipelines (Transco), gathering and storage; off-grid gas power for data centres | Tulsa, Oklahoma</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{usd(PRICE)} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{usd(PRICE)}, NYSE close {PRICE_DATE}; record close {usd(HI_CLOSE)} on 19 May 2026, intraday high US$80.08 on 20 May"),
    ("Market value", f"US${MCAP:.1f}bn on {SHARES:,.0f}m shares (30 Jul 2026 plus Momentum shares)"),
    ("Enterprise value", f"About US${EV_NOW:.0f}bn with net debt of about {bn(ND_SEP)} (30 Sep, my estimate) and outside owners"),
    ("2026 guide (3 Aug 2026)", "Adjusted EBITDA US$8.3 to 8.5bn; AFFO US$5.15 a share; dividend US$2.10"),
    ("Multiples", f"EV {EV_EB26:.1f}x 2026 guide and {EV_EB27:.1f}x my 2027E EBITDA; yield {YIELD * 100:.1f}%"),
    ("Power Innovation", f"Five projects, {MW_TOTAL:,} MW installed, about US$9.0bn before capitalised interest; 10 to 12.5-year contracts"),
    ("Consensus (stockanalysis.com)", f"Average target {usd(CONS_TP)} ({CONS_N} analysts); 2027 EPS US${CONS_EPS27:.2f}"),
    ("Next event", "Q3 2026 results, early November; not on EDGAR by 2 November, date not confirmed by Williams in what I read"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Williams owns the gas main and now builds the power plant beside the data centre. At US$74, the price pays for the pipes in full and the power plants only in part.</p>')
A(para("Williams moves about a third of America's gas through Transco and its other pipes. Since late July it has also run its own gas "
       "power plant for Meta in Ohio, off the grid, the first of five such projects. My October piece argued that building your own "
       "power swaps the grid's queue for the machine makers' queues. Williams got ahead by buying its machines first."))
A(para(f"The power plants earn well, about 5 times build multiples on contracts of 10 to 12.5 years. But on my estimates they make "
       f"about {pi_share28 * 100:.0f}% of 2028 Adjusted EBITDA, and the price already pays today's full multiple for the pipes."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction.</b> A sum of the parts gives {usd(BASE_VALUE)}, {UP_BASE * 100:.1f}% "
       f"above the price, inside a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} ({chg(bull)}). That is inside my no call band."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (calendar years; Adjusted EBITDA and AFFO as Williams defines them)"))
A(datatable(
    ["US$ million unless stated", "2024A", "2025A", "2026G*", "2027E", "2028E"],
    [
        ["Pipes, gathering, marketing, other", "7,080", "7,750", m(CORE26), m(CORE27), m(CORE28)],
        ["Momentum (from 3 Sep 2026)", "", "", m(MOM26), m(MOM27), m(MOM28)],
        ["Power Innovation", "", "", m(PI26), m(PI27), m(PI28)],
        ["Adjusted EBITDA", "7,080", "7,750", m(EB26), m(EB27), m(EB28)],
        ["Growth (%)", "", f"{(7750 / 7080 - 1) * 100:.1f}", f"{(EB26 / 7750 - 1) * 100:.1f}", f"{(EB27 / EB26 - 1) * 100:.1f}", f"{(EB28 / EB27 - 1) * 100:.1f}"],
        ["AFFO per share (US$)", "4.40", "4.78", "5.15", f"{AFFO27 / SHARES:.2f}", f"{AFFO28 / SHARES:.2f}"],
        ["Dividend per share (US$)", "1.90", "2.00", "2.10", f"{DPS27:.2f}", f"{DPS28:.2f}"],
        ["Net debt / Adjusted EBITDA (x)", "", "", f"{ND26 / (EB26 + MOM27 * 8 / 12):.2f}", f"{ND27 / EB27:.2f}", ""],
        [f"EV / Adjusted EBITDA at {usd(PRICE)} (x)", "", "", f"{EV_EB26:.1f}", f"{EV_EB27:.1f}", ""],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*2026G is Williams' guide midpoint of 3 August 2026; its split into the three sources is mine. 2027E and 2028E are my estimates. "
          "2024A and 2025A from Williams' releases; AFFO per share for those years is my arithmetic on AFFO and weighted diluted shares. "
          "Net debt is mine, rolled from 30 June 2026; Williams' own leverage measure counts the Blackstone capital as equity and guides about 3.75x for 2026."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: the power build, and where it sits in the company"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_power.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_ebitda.png"></div></div>')
A(caption("Left: Power Innovation installed MW in service at the end of each half year, from Williams' in-service windows (Form 10-Q, 30 June 2026); "
          "Aquila's split is mine. Right: Adjusted EBITDA by source, US$bn; 2024A and 2025A per Williams, 2026 its guide midpoint split by me, "
          "2027E and 2028E mine."))
A('</div>')

A(section("The thesis: the owner of the gas main digs the well"))
A(para("Go back to the street in the piece whose water main is too small. Every house wants its own well, and the drilling firms are "
       "booked for years. Now the company that owns the water main offers to dig your well, install the pump and run it for ten years at a "
       "fixed fee. It already has the water and the trench, and it booked the pump makers' diaries before the neighbours did."))
A(para("That is Williams. It builds a gas power plant on or beside a customer's site, lays the gas line to it and runs it, under a "
       "primarily fixed-price contract. It calls this Power Innovation, and has signed five projects:"))
A(cols(datatable(
    ["Project", "State", "Installed MW", "Contract", "Williams' in-service window"],
    [[p[0], p[4], f"{p[1]:,}", f"{p[2]:g} years", p[5]] for p in PROJ] + [["Total", "", f"{MW_TOTAL:,}", f"{CONTRACT_YRS:.1f} years, MW-weighted", "About US$9.0bn before capitalised interest"]],
    num_cols={2}, total_row_idx=5,
), [22, 9, 13, 20, 36]))
A(caption("Source: Williams Form 10-Q for the quarter to 30 June 2026. Customers are not named in Williams' filings; Ohio's siting board names "
          "Sidecat, a Meta affiliate, for Socrates North. The 10-K calls the first projects' customer 'a large, investment-grade company'."))
A(para("Williams' filings since May 2026 give Socrates 556 MW of expected capacity. The 2025 10-K described 400 MW committed to the "
       "customer, two plants of 200 MW, the figure on Williams' project page. My reading is that the gap is spare capacity, which an "
       "off-grid plant needs because no grid stands behind it."))
A(para("<b>The claim holds, and Williams shows the mechanism.</b> Williams moved fast because it joined the makers' queues early and paid. "
       "At the end of June its leverage measure left out US$777m of cash spent on long-lead power equipment, also outside its capex guide, "
       "because customers reimburse it if an order is cancelled. On the Q2 call, per a third-party transcript, its operating chief said Williams had \"locked up the turbines\" for its "
       "backlog, and that equipment timing is \"really going to be setting some of the pace\". Ohio approved Socrates North on 18 September "
       "2025; Socrates South entered service in late July 2026, \"within budget and on time\", and North is due later in Q4."))
A(para(f"<b>The returns are high because speed is scarce.</b> Blackstone's US$4.4bn for 49% of the growth capex implies about US$9.0bn before "
       f"capitalised interest (8-K, 13 July 2026). \"Like our other power innovation projects\", Williams expects to build Neo at \"an attractive 5x build multiple\" (CEO, Q1 call), cost over yearly EBITDA. At about 5 times, "
       f"the five projects earn about {bn(PI_RUN)} a year at full output, my estimate: about US${EB_PER_MW:.2f}m per installed MW, or "
       f"US${EB_PER_MWDAY:,.0f} per MW-day. PJM's 2027/28 capacity auction cleared at its cap of US$333.44 per MW-day. The comparison is rough, "
       f"since a capacity price pays only for availability, but the data centre pays about {EB_PER_MWDAY / PJM_CAP:.1f} times it for a plant that comes years sooner."))
A(para(f"Over the contract alone, with nothing after it, a 5 times build multiple earns about {IRR_5X * 100:.0f}% a year before tax and "
       f"maintenance, my arithmetic on the {CONTRACT_YRS:.1f}-year average term. Blackstone, Apollo and KKR fund 49% at a 6.35% target "
       "return; distributions above it cut their balance, and Williams can buy them out at that balance from July 2033."))
A(para("<b>The pipe's clock still runs.</b> Transco's Southeast Supply Enhancement, 1,597,000 dekatherms a day, received its FERC "
       "certificate in January 2026. Williams' 10-Q now says \"as early as the third quarter of 2027\", against the 1 November 2027 target "
       "in the original application the piece cites."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {usd(PRICE)} Williams is worth US${MCAP:.1f}bn on {SHARES:,.0f}m shares, including 26.9m issued for Momentum Midstream on "
       f"3 September. With net debt of about {bn(ND_SEP)} at the end of September, my estimate, and outside owners' stakes, the enterprise "
       f"value is about US${EV_NOW:.0f}bn: {EV_EB26:.1f} times the 2026 guide midpoint and {EV_EB27:.1f} times my 2027 EBITDA. The shares trade at "
       f"{PRICE / G26['eps']:.1f} times the 2026 adjusted EPS guide of US$2.35 and yield {YIELD * 100:.1f}%. On stockanalysis.com's own EBITDA, "
       "Williams is at 17.3 times trailing against a 12.8 times median for six pipeline peers, and was 10.9 times at the end of 2023."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["10 Feb 2026", "Q4 results and Analyst Day", f"up {(PX_FEB10 / PX_FEB9 - 1) * 100:.1f}%"],
        ["19 May 2026", f"Record close {usd(HI_CLOSE)}", "Peak"],
        ["13 Jul 2026", "Blackstone joint venture, US$5.34bn", f"down {abs(PX_JUL13 / PX_JUL10 - 1) * 100:.1f}%"],
        ["4 Aug 2026", "Q2 results; Socrates phase one; Momentum", f"up {(PX_AUG4 / PX_AUG3 - 1) * 100:.1f}%"],
    ],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: Williams month-end close, January 2024 to the 30 October 2026 close, against my base value (red). Nasdaq.com, retrieved "
          "2 November 2026. Right: move from the previous close to the close on the day the news reached the market."))
A('</div>')
A(para(f"<strong class='lead'>The power business is too small to carry the premium alone.</strong> On my estimates Power Innovation makes "
       f"US${PI27 / 1000:.2f}bn of EBITDA in 2027 and US${PI28 / 1000:.2f}bn in 2028, about {pi_share28 * 100:.0f}% of that year's total. "
       f"Counting only signed projects, I grow EBITDA {CAGR30 * 100:.1f}% a year to 2030, below Williams' target of more than 11%; the gap "
       "is the 6 GW backlog Williams talks about but has not signed."))
A(para(f"<strong class='lead'>The price pays for the pipes in full, and the power plants only in part.</strong> If I value the pipes, "
       f"gathering and Momentum at {CORE_MULT} times my 2028 EBITDA, the price implies about {IMPL_PI_MULT:.1f} times run-rate EBITDA for "
       f"the five power projects. A {CONTRACT_YRS:.1f}-year level stream is worth {CONTRACT_PV:.1f} times at 8%, so the market pays less than "
       "the contracts are worth and nothing for renewals or the backlog. That is the part I think it undervalues."))
A(para(f"<strong class='lead'>But the pipes' multiple decides the value.</strong> Each turn on the pipes moves my value about "
       f"{usd(turn_pipes)} a share; each turn on power about {usd(turn_power)}. Williams' year-end EV was about 13.4 times its Adjusted "
       f"EBITDA in both 2024 and 2025, my arithmetic, so {CORE_MULT} times only holds today's rating."))
A(para(f"<strong class='lead'>The dividend needs fast growth.</strong> The US$2.10 dividend is about 41% of guided AFFO per share. At an 8% "
       f"cost of equity and 3% growth after ten years, the price needs it to grow about {DIV_G_NEEDED * 100:.1f}% a year for ten years, "
       "twice its recent rise, though close to my AFFO per share growth to 2028."))

A(section("Valuation, with the working"))
A(para(f"I value Williams twelve months out, at October 2027, as a sum of two parts on Adjusted EBITDA; by then the market prices 2028. "
       f"I split the 2026 guide midpoint of US$8.4bn into Momentum (four months, US${MOM26:.0f}m), Socrates (US${PI26:.0f}m) and the core, "
       f"and grow the core {CORE_G27 * 100:.0f}% in 2027 and {CORE_G28 * 100:.0f}% in 2028. Momentum adds US${MOM27:.0f}m in 2027, from "
       "Williams' 8.5 times multiple on US$5.5bn, and US$700m in 2028. All are my estimates."))
A(cols(datatable(
    ["Part", "Basis", "US$ million"],
    [
        ["Pipes, gathering, Momentum", f"{CORE_MULT} x 2028E EBITDA of {m(CORE28 + MOM28)}", m((CORE28 + MOM28) * CORE_MULT)],
        ["Power Innovation", f"{PI_MULT:.0f} x run-rate EBITDA of {m(PI_RUN)}, less {m(PI_REMAIN)} still to spend", m(PI_RUN * PI_MULT - PI_REMAIN)],
        ["Enterprise value, October 2027", "", m(BASE["ev"])],
        ["Less net debt, end 2027", "My roll from 30 June 2026; about 3.7x 2027E EBITDA", f"({m(ND27)})"],
        ["Less existing outside owners", f"{NCI_PE:.0f} x their income of about US${NCI_INC_RUN:.0f}m (book US$2.2bn)", f"({m(NCI_VALUE)})"],
        ["Less Blackstone's investment", "Debt-like: 6.35% target return", f"({m(BX_TOTAL)})"],
        ["Equity value", f"{SHARES:,.0f}m shares", m(BASE["eq"])],
        ["Base value per share", "", usd(BASE_VALUE)],
    ],
    num_cols={2}, total_row_idx=7,
), [30, 52, 18]))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "Pipes 2028E", "Pipes x", "Power x", "Value", "Change", "Weight"],
    [
        ["Bear", "Gas growth slows; AI power deals stall; core 2% a year", bn(SC[0]["ebp"], 2), f"{SC[0]['cm']}x", f"{SC[0]['pm']:.0f}x", usd(bear), chg(bear), "25%"],
        ["Base", "Core 4% then 5%; five projects on time", bn(SC[1]["ebp"], 2), f"{SC[1]['cm']}x", f"{SC[1]['pm']:.0f}x", usd(base), chg(base), "50%"],
        ["Bull", "More Transco expansions; the backlog converts", bn(SC[2]["ebp"], 2), f"{SC[2]['cm']:.0f}x", f"{SC[2]['pm']:.0f}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", usd(WEIGHTED), chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [9, 35, 11, 8, 8, 11, 10, 8]))
A(caption("Pipes 2028E includes Momentum. All cases keep the same net debt, outside owners and Blackstone balance; a weaker case would "
          "also carry more debt, so the bear case is if anything generous."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: the pipes' multiple against the power multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Pipes \\ Power"] + [f"{p:.0f}x" for p in SENS_PM],
    [[f"{c}x"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (c, row) in enumerate(zip(SENS_CM, GRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{W[n_above]} of the nine cells sit above the price, and only the {W[n_15].lower()} in the 15 times row sit 15% or more above it. "
       f"The pipes' multiple moves the value about five times as much per turn as the power multiple. A long needs the base 15% or more "
       f"above the price, a short 25% or more below. At {UP_BASE * 100:.1f}% above, {my_call.lower()} is no call."))
A('</div></div>')
A('</div>')
A(para(f"<strong class='lead'>Dividend cross-check.</strong> If the dividend grows 7% a year for ten years and 3% after, at an 8% cost of "
       f"equity, it is worth {usd(DDM_VALUE)}, {abs(DDM_VALUE / PRICE - 1) * 100:.0f}% below the price; at that growth the price implies "
       f"a cost of equity of {IMPL_KE * 100:.1f}%. A dividend model undercounts a company paying out two fifths of its cash, so I use it "
       "only to show how much growth the price needs."))
A('<div class="keeptogether">')
A(section("Valuation cross-check and peer landscape"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_valuation.png"></div><div class="col">')
A(cols(datatable(
    ["Company", "EV/EBITDA", "Fwd P/E", "Yield"],
    [[c, f"{e:.1f}x", f"{p:.1f}x", f"{y * 100:.1f}%"] for c, t, e, p, y, w, g in PEERS],
    num_cols={1, 2, 3},
), [40, 20, 20, 20]))
A('</div></div>')
A(caption("Left: value per share by method against the price (grey). Right: trailing EV/EBITDA, forward P/E and dividend yield from "
          "stockanalysis.com, retrieved 2 November 2026, on its own EBITDA measure (Williams: US$7.03bn trailing against its Adjusted "
          "EBITDA of US$8.13bn); peer median 12.8x. Multiples set the range only; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Early November 2026 (date not confirmed)", "Q3 2026 results", "Socrates South's first full quarter; EBITDA against the US$8.3 to 8.5bn guide; new power contracts"],
        ["Q4 2026", "Socrates North in service", "On time and on budget, like South"],
        ["February 2027 (date not announced)", "Q4 2026 results and 2027 guide", "2027 Adjusted EBITDA against my US$9.6bn; US$10.3bn or more would move me towards a long"],
        ["Early 2027", "Rest of the Blackstone capital", "About US$1.6bn more after July's US$3.75bn"],
        ["2H 2027", "Apollo, Aquila; Southeast Supply Enhancement", "Two plants and 1,597,000 Dth a day of new Transco capacity"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para(f"<strong>One customer per plant, and the end of the contract.</strong> Each plant sits on one customer's site with no grid behind "
       f"it. After 10 to 12.5 years the customer can extend but need not. If the plants have no value after the contract, my power value "
       f"falls by about US${PI_RUN * (PI_MULT - CONTRACT_PV) / 1000:.1f}bn, under a dollar a share."))
A(para("<strong>Delays and debt.</strong> Four more plants, 2,032 MW, are due from 2H 2027 to 2H 2028, all assuming permits on time, "
       "and equipment timing still sets the pace. Net debt rose from US$29.3bn at the end of 2025 to US$30.6bn at the end of June, "
       "before Momentum's US$3.5bn of cash and debt; Williams calls 2026 and 2027 its tight years."))
A(para(f"<strong>The pipes' multiple.</strong> The largest risk to the value: at 12 times rather than {CORE_MULT} times, my value falls to {usd(GRID[0][1])}. "
       f"The build multiple matters far less: at 6 times rather than 5, my value falls by about US${BASE_VALUE - value(pi_run=CAPEX_PI_EX / 6)['ps']:.2f}, to {usd(value(pi_run=CAPEX_PI_EX / 6)['ps'])}."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price below about {usd(LONG_BELOW)}, where my base value would sit 15% above it; or a 2027 guide "
       "of US$10.3bn or more of Adjusted EBITDA, which would lift my pipes estimate by about US$720m. New power contracts help less than "
       f"they sound: each further GW at a 5 times build multiple adds about US$1.70 a share at my 8 times. <strong>Into a short:</strong> a "
       f"price above about {usd(SHORT_ABOVE)}."))
A(para(f"<strong>{my_call} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para(f"The October piece argued that building your own gas power swaps the grid's queue for the makers' queues. Williams agrees in its "
       "own words: it bought the machines first, and equipment timing sets its pace. Its first plant for Meta entered service in late July, "
       "and four more are due by the end of 2028. The power business earns well, but it is about "
       f"a ninth of Williams' EBITDA by 2028, and the price already pays today's full multiple for the pipes. {my_call}: "
       f"{CALL['direction']}, {conv} conviction; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026", "2027E", "2028E", "Basis"],
    [
        ["Core EBITDA growth", f"{(CORE26 / 7750 - 1) * 100:.1f}%*", f"{CORE_G27 * 100:.0f}%", f"{CORE_G28 * 100:.0f}%", "Transco expansions; SESE from 2H 2027"],
        ["Momentum EBITDA, US$m", f"{MOM26:.0f}", f"{MOM27:.0f}", f"{MOM28:.0f}", "8.5x on US$5.5bn; Shelby Trough 2Q 2028"],
        ["Power EBITDA, US$m", f"{PI26:,.0f}", f"{PI27:,.0f}", f"{PI28:,.0f}", f"US${EB_PER_MW:.3f}m per installed MW-year"],
        ["Interest, US$m", "1,535 (guide)", f"{INT27:,.0f}", f"{INT28:,.0f}", "Debt rises with capex"],
        ["Growth capex, US$m", "7,600 (guide)", f"{GCX27:,.0f}", "", "2027 'a high watermark' (Q2 call)"],
        ["Dividend per share, US$", "2.10", f"{DPS27:.3f}", f"{DPS28:.3f}", "+5% a year, the recent pace"],
    ],
), [26, 15, 11, 11, 37]))
A(caption(f"*Implied by my split of the guide. All my estimates. Full workings, with live formulas, in {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Williams Q2 2026 earnings release (Form 8-K, Ex. 99.1) and Form 10-Q, 3 August 2026, for '
  'results, guidance, the power projects, the Blackstone joint venture, Momentum and the Southeast Supply Enhancement. Williams 2025 Form 10-K (24 February 2026) and first quarter 2026 Form 10-Q for Socrates\' capacity. '
  'Williams earnings releases of 3 November 2025, 10 February 2026 and 4 May 2026. Williams Form 8-K of 13 July 2026, Exhibits 99.1 and '
  '99.2. Williams prospectus supplement of 3 September 2026 for the Momentum shares. Williams first and second quarter 2026 earnings '
  'calls, 5 May and 4 August 2026, from third-party transcripts (AllMind). Ohio Power Siting Board, case 25-188-EL-BGN, 18 September '
  '2025. PJM 2027/2028 Base Residual Auction report, December 2025. Share prices from Nasdaq.com; consensus, targets and peer multiples '
  'from stockanalysis.com (S&amp;P Global data); all retrieved 2 November 2026. Estimates for 2027 and 2028, the 2026 split and the '
  'valuation are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 22 September 2026, updated on 30 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/building-your-own-power/">thephysicallayer.fyi/journal/building-your-own-power</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Williams. Personal research, not investment advice.</p>')
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
