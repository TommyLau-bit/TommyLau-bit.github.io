# -*- coding: utf-8 -*-
"""Bloom Energy (NYSE: BE) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/bloom-energy.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Bloom Energy (NYSE: BE)"
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
    return f"US${x:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
pb = project(*SCEN[0][1:7]); pu = project(*SCEN[2][1:7])
G27 = REV27 * PROD_SHARE / USD_PER_MW

A('<h1 class="doctitle">Bloom Energy Corporation</h1>')
A('<p class="docsubtitle"><b>NYSE: BE | Solid oxide fuel cell systems for on-site power, and their maintenance | San Jose, California</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:.2f} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:.2f}, NYSE close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:.2f}"),
    ("Market value", f"About US${MCAP:.0f}bn on {SHARES_OUT * 1000:.1f}m shares; net cash US${NETCASH:.2f}bn at 30 Jun 2026"),
    ("Fully diluted shares", f"{SH26 * 1000:.0f}m with the US$2.5bn 0% notes (convert at US${CONV_2030_PX:.2f}) and staff awards"),
    ("Non-GAAP P/E, my estimates", f"{PE26:.0f}x 2026E, {PE27:.0f}x 2027E, {PE28:.0f}x 2028E"),
    ("Consensus", f"EPS US${CONS_EPS_26:.2f} 2026 (stockanalysis.com), US${CONS_EPS_27:.2f} 2027, US${CONS_EPS_28:.2f} 2028 (Nasdaq.com, Zacks); target US${CONS_TP:.0f}"),
    ("2026 guide (28 Jul)", "Revenue US$3.9 to 4.2bn; non-GAAP gross margin about 34%; non-GAAP EPS US$2.55 to 2.85"),
    ("Backlog, end 2025", f"About US${BACKLOG_25[0]:.0f}bn, of which product about US${BACKLOG_25[1]:.0f}bn"),
    ("Factory", "Fremont, about 1 GW a year, doubling to 2 GW by end 2026; room for about 5 GW"),
    ("Next results", "Q3 2026: date not yet announced; last year 28 Oct"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Bloom\'s customers pay for time. Bloom is paid for it in volume, not in price, and at US${PRICE:.0f} the shares already need the volume.</p>')
A(para("Bloom Energy makes fuel cells that turn natural gas into electricity beside a building. On 24 September I argued that "
       "its buyers pay for an earlier switch-on date, not for cheap power. The claim is holding: revenue rose "
       f"{(Q_REV[-1] / Q_REV[5] - 1) * 100:.0f}% in the second quarter, Oracle plans up to {ORCL_GW[0]} GW and AEP has taken most of "
       "its 900 MW option."))
A(para(f"But I misread where the premium shows. Product gross margin, where a price for speed would appear, was "
       f"{pc(PROD_GM_H[0])} in 2024, {pc(PROD_GM_H[1])} in 2025 and {pc(H1_26_PROD_GM)} in the first half of 2026. "
       f"Bloom earns the time premium as volume, and volume is set by a factory. At US${PRICE:.2f} the price needs about "
       f"{NEED_GW28:.1f} GW shipped in 2028, half as much again as the plant's planned 2 GW."))
A(para(f"<b>My call: {CALL['direction']}, {CALL['conviction'].lower()} conviction, leaning short.</b> My base case is worth "
       f"{usd(BASE_VALUE)}, {chg(BASE_VALUE)}. The bear case is {usd(bear)} ({chg(bear)}) and the bull case {usd(bull)} "
       f"({chg(bull)}). I would revisit above about US${REVISIT_SHORT:.0f} or below about US${REVISIT_LONG:.0f}."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (non-GAAP basis)"))
A(datatable(
    ["US$ billion unless stated", "2024A", "2025A", "2026 guide", "2026E*", "2027E*", "2028E*"],
    [
        ["Revenue", f"{REV_H[0]:.2f}", f"{REV_H[1]:.2f}", "3.9 to 4.2", f"{REV26:.2f}", f"{REV27:.2f}", f"{REV28:.2f}"],
        ["Revenue growth (%)", "", f"{(REV_H[1] / REV_H[0] - 1) * 100:.0f}", "100 (mid)", f"{(REV26 / REV_H[1] - 1) * 100:.0f}", f"{B[1] * 100:.0f}", f"{B[2] * 100:.0f}"],
        ["Product gross margin, GAAP (%)", pc(PROD_GM_H[0]), pc(PROD_GM_H[1]), "", f"{pc(H1_26_PROD_GM)} (H1)", "", ""],
        ["Gross margin (%)", pc(GM_H[0]), pc(GM_H[1]), "about 34", pc(GM26), pc(B[3]), pc(B[4])],
        ["Operating income", f"{OPINC_H[0]:.2f}", f"{OPINC_H[1]:.2f}", "0.80 to 0.90", f"{OPINC26:.2f}", f"{P['o27']:.2f}", f"{P['o28']:.2f}"],
        ["Operating margin (%)", pc(OPINC_H[0] / REV_H[0]), pc(OPINC_H[1] / REV_H[1]), "", pc(OPINC26 / REV26), pc(P['om27']), pc(P['om28'])],
        ["EPS, diluted (US$)", f"{EPS_H[0]:.2f}", f"{EPS_H[1]:.2f}", "2.55 to 2.85", f"{EPS26:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}"],
        ["Consensus EPS (US$)", "", "", "", f"{CONS_EPS_26:.2f}", f"{CONS_EPS_27:.2f}", f"{CONS_EPS_28:.2f}"],
        [f"P/E at US${PRICE:.2f} (x)", "", f"{PRICE / EPS_H[1]:.0f}", f"{PE_GUIDE:.0f}", f"{PE26:.0f}", f"{PE27:.0f}", f"{PE28:.0f}"],
        ["Fully diluted shares (m)", "", "", "", f"{SH26 * 1000:.0f}", f"{SH27 * 1000:.0f}", f"{SH28 * 1000:.0f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E to 2028E are my own estimates. Income lines are Bloom's non-GAAP measures, which exclude stock-based pay "
          f"(US${SBC_Q2 * 1000:.0f}m in Q2 2026 alone) and other items; Bloom guides on this basis. Q2 2026 GAAP EPS was US$0.62 against "
          f"US$0.78. 2026E is the reported first half plus my third quarter (EPS US${Q3E_EPS:.2f}, consensus US${CONS_Q3:.2f}) and fourth "
          f"(US${Q4E_EPS:.2f}). Tax is my assumption: 1% in 2026, 10% in 2027, 15% in 2028 as losses carried forward run down. "
          "History from Bloom's results releases."))

A('<div class="keeptogether">')
A(section("Two charts: earnings that grow fast, and a value below the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and non-GAAP diluted EPS, 2024A to 2028E; 2024A and 2025A per Bloom, the rest my estimates. Right: value "
          "per share from the base case, the probability-weighted cases, the sensitivity grid and the bear to bull range, against the "
          f"US${PRICE:.2f} price (red) and the stockanalysis.com average analyst target, retrieved 6 October 2026."))
A('</div>')

A(section("The thesis: the hotspot shop with one van"))
A(para("Go back to the mobile hotspot from the September piece. You pay more per gigabyte because the cable engineer is months "
       "away. Now picture the shop that sells the hotspots. Its queue is round the block, yet it charges the same as last year. "
       "It sells more boxes, not dearer ones. And it can only sell as many as its one van can deliver."))
A(para(f"<strong>Bloom is that shop.</strong> Its fuel cells arrive on a lorry and switch on in months, while a grid connection can "
       f"take years. Revenue in the first half of 2026 was {REV_GROWTH_2Y + 1:.1f} times the first half of 2024. Oracle signed on "
       f"13 April to procure up to {ORCL_GW[0]} GW, with {ORCL_GW[1]} GW contracted. AEP exercised most of its 900 MW option in "
       f"January, an order of about US${AEP_DEAL[0]:.2f}bn. Brookfield, which finances many of the projects, lifted its framework "
       f"from US${BROOKFIELD_BN[0]}bn to US${BROOKFIELD_BN[1]}bn on 30 June. Customers are paying for speed."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_margin.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_quarterly.png"></div></div>')
A(caption("Left: GAAP gross margin on products, on services and in total, by quarter. Product margin has sat at 33 to 37% since "
          "early 2025 while revenue tripled; the total rose mainly because products grew to 88% of revenue. Right: revenue by "
          "quarter, with sales to related parties hatched (mainly joint ventures with Brookfield from Q3 2025) and the non-GAAP "
          "gross margin. Source: Bloom results releases, 2024 to 28 July 2026; product and service margins are derived."))
A('</div>')

A(section("Where I was wrong in September"))
A(para(f"In the piece I wrote that gross margin rising from 26.7% to 33.4% while volume more than doubled was \"the time premium, "
       f"expressed in money\". That was wrong. The rise came mainly from mix: products, which earn far more than "
       "installation and service, went from 74% to 88% of revenue between the two quarters. Product margin also recovered, from "
       "33.0% to 36.5%, after a weak 2025, and service added a little. But over a full year the product margin, where a "
       f"premium for speed would show, was {pc(PROD_GM_H[0])} in 2024, {pc(PROD_GM_H[1])} in 2025 and {pc(H1_26_PROD_GM)} in the "
       f"first half of 2026. Splitting the margin by line in Bloom's income statement, which I had not done for the piece, "
       "changed my view."))
A(para("Two smaller points. I wrote that the service backlog of about US$14bn was contracts for up to twenty years and the part "
       "least exposed to the grid catching up. The 10-K says those contracts run 5 to 20 years, but customers can end them for "
       f"convenience each year. And I wrote that Oracle had committed to up to {ORCL_GW[0]} GW. It intends to procure up to "
       f"{ORCL_GW[0]} GW, of which {ORCL_GW[1]} GW is contracted. The claim, that customers pay for an earlier switch-on, survives. "
       "Its margin test is weaker than I thought, because margin never tracked scarcity. The piece and the claim stay as published."))

A(section("The factory is the ceiling"))
A(para(f"If the premium is paid in volume, the question is how much Bloom can make. Its Fremont plant makes about 1 GW a year and "
       f"is doubling to 2 GW by the end of 2026, with room for about 5 GW. AEP's order works out at about US${USD_PER_MW:.2f}m a "
       f"megawatt if it covers the full 900 MW. At that price, and with products {PROD_SHARE * 100:.1f}% of revenue as in the first half, my 2026 estimate is "
       f"about {GW26:.1f} GW, 2027 about {G27:.1f} GW and my 2028 base about {BASE_GW28:.1f} GW. These are my conversions, not "
       "Bloom figures; Bloom does not report megawatts shipped."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_capacity.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption(f"Left: revenue converted to gigawatts a year at AEP's US${USD_PER_MW:.2f}m a megawatt, with products at "
          f"{PROD_SHARE * 100:.1f}% of revenue (my derivation), against the 2 GW the factory is planned to make by the end of 2026. "
          "Right: BE month-end close, November 2023 to the 5 October 2026 close, not adjusted for dividends (Yahoo Finance, "
          "retrieved 6 October 2026), against my base value."))
A('</div>')
A(para("So 2028 needs Fremont to grow again beyond 2 GW, which is possible but not yet announced. Management said in July that "
       "manufacturing capacity and supply are not current constraints. On 8 July a short seller, Hunterbrook, alleged that Bloom "
       "relies on Chinese scandium for its cells; Bloom rejected the report and says supply covers its demand and backlog. The "
       f"shares fell from US${PX_SHORT[0]:.2f} to US${PX_SHORT[1]:.2f} that day."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:.2f} Bloom is worth about US${MCAP:.0f}bn. That is {PE_GUIDE:.0f} times the midpoint of its own 2026 "
       f"earnings guide, {PE27:.0f} times my 2027 estimate and {PE28:.0f} times my 2028. The shares are up "
       f"{(PRICE / PRICE_DEC25 - 1) * 100:.0f}% since the end of 2025. Each big step came on news of volume: from "
       f"US${PX_ORCL[0]:.2f} to US${PX_ORCL[1]:.2f} on the Oracle expansion, and from US${PX_Q2[0]:.2f} to US${PX_Q2[1]:.2f} "
       "in the two days after the second quarter results."))
A(para(f"<strong class='lead'>What the price needs.</strong> By October 2027 the market will price 2028. At {BASE_PE} times, "
       f"US${PRICE:.2f} needs 2028 earnings of US${NEED_EPS28:.2f} a share, close to the US${CONS_EPS_28:.2f} consensus of two "
       f"analysts. At my base margins that needs revenue of about US${NEED_REV28:.1f}bn, about {NEED_GW28:.1f} GW of product "
       f"at AEP's price, against my base of US${REV28:.1f}bn and {BASE_GW28:.1f} GW."))
A(para("<strong class='lead'>Where I differ.</strong> Not on demand, which is real, but on what Bloom keeps from it. The market "
       "prices Bloom as though the scarcity of grid power shows up in Bloom's price as well as its volume. Two years of product "
       "margins say it does not. Bloom's earnings therefore grow at the pace of its factory and its financing partners, and both "
       "are visible and finite. The grid is also slowly getting faster: in January FERC approved a Southwest Power Pool route that "
       "studies large new loads and their generation within 90 days."))

A(section("Valuation, with the working"))
A(para(f"I value Bloom on non-GAAP earnings per share twelve months out, so on 2028. Revenue grows from my 2026E of "
       f"US${REV26:.2f}bn; gross margin less operating costs gives operating income; I add about US${OTHER_Y * 1000:.0f}m a year of "
       "interest income and tax it at my rates. Shares are fully diluted: the 294.5m outstanding, 12.8m from the US$2.5bn 0% notes "
       "due 2030, 1.3m from the remaining 2029 notes, 16.0m of staff awards, then 1.5% a year more. I use "
       f"{BASE_PE} times: below GE Vernova's 47 times, above Vertiv's 32, for faster growth but fewer, larger customers. "
       f"{BASE_PE} x US${EPS28:.2f} = {usd(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "Grid and turbines catch up: growth 30% then 12%, gross margin 33% then 32%", usd(pb["eps28"], 2),
         f"{SCEN[0][7]}x", usd(bear), chg(bear), "25%"],
        ["Base", "Growth 55% then 38%, gross margin 35% then 35.5%; Fremont expands past 2 GW", usd(EPS28, 2), f"{BASE_PE}x",
         usd(base), chg(base), "50%"],
        ["Bull", "Oracle's 2.8 GW and Brookfield's US$25bn fill: growth 70% then 50%, margin 36.5% then 37.5%",
         usd(pu["eps28"], 2), f"{SCEN[2][7]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [10, 40, 11, 9, 11, 11, 8]))
A(caption(f"All cases start from my 2026E. The bear case is not a collapse: revenue still grows by almost half over two years, to "
          f"US${pb['r28']:.1f}bn. It is what happens when the gap Bloom lives in narrows and the multiple falls to a power equipment "
          f"maker's. The bull case needs about {pu['gw28']:.1f} GW a year in 2028."))
A('</div>')
grid = [[e * m for m in SENS_PE] for e in SENS_EPS]
above = sum(v > PRICE for r in grid for v in r)
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["2028 EPS"] + [f"{m}x" for m in SENS_PE],
    [[usd(e, 2)] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (e, r) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"Only {above} of the nine cells sit above today's price. Each needs 2028 earnings at or above my base and a multiple of "
       "40 times or more. Every figure is live in the accompanying model, so a change to growth, margin, tax, dilution or the "
       "multiple moves the value."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [[c, t, (f"{p:.1f}x" if p else "n/m"), w] for c, t, p, w in PEERS],
    num_cols={2},
), [20, 15, 12, 53]))
A(caption("Forward P/E from stockanalysis.com, retrieved 6 October 2026; Siemens Energy on its Frankfurt listing. Bloom's 83.5 times "
          "sits between my 2026 and 2027 multiples. Multiples only; no view on the peers' shares."))
A('</div>')

A(section("Dilution, counted properly"))
A(para(f"The US$2.5bn 0% notes due November 2030 convert at US${CONV_2030_PX:.2f}, into {CONV_2030_SH * 1000:.1f}m shares, "
       f"or up to {CONV_2030_MAX * 1000:.1f}m after a takeover. Bloom may settle in cash, shares or both. Holders can convert early "
       f"only after a quarter in which the shares closed above US${CONV_2030_PX * 1.3:.2f} on 20 of the last 30 trading days. On my "
       f"count of Yahoo closes, the third quarter managed {CONV_TRIGGER_DAYS}, so early conversion looks unlikely this quarter. "
       f"Oracle's warrant over {ORCL_WARRANT[0]:.2f}m shares at US${ORCL_WARRANT[1]:.2f} was exercised in May for "
       f"{ORCL_WARRANT[4]:.2f}m shares; its US$324m value comes off revenue as Oracle's systems are delivered. Stock-based pay ran at "
       f"US${SBC_Q2 * 1000:.0f}m in the second quarter, almost a quarter of non-GAAP operating income."))

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Late Oct or early Nov 2026 (not yet announced)", "Q3 2026 results", "Product gross margin against 36.5%; any further guide raise; consensus EPS US$0.57"],
        ["Late 2026", "Fremont reaches 2 GW a year", "On time, and any plan beyond 2 GW, which my base case needs"],
        ["Feb 2027", "Q4 results and 2027 guide", "Growth guided for 2027 against my 55%; year-end backlog against about US$20bn"],
        ["Feb 2027", "Form 10-K for 2026", "Customer concentration; service contract terms; megawatts if disclosed"],
        ["Through 2027", "Oracle's further 1.6 GW", "Whether 'up to 2.8 GW' becomes contracted"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The volume keeps surprising.</strong> The bull case, and the main risk to a no call that leans short. Bloom raised "
       f"its 2026 revenue guide from US${GUIDE_26_FEB['rev'][0]} to {GUIDE_26_FEB['rev'][1]}bn in February to US$3.9 to 4.2bn in July. "
       "Another step like that, with Fremont expanding fast, puts 2028 near the bull case. <strong>The gap closes.</strong> The "
       "bear case and the claim's own falsifier: faster interconnection or more turbine capacity shrinks the window Bloom sells into."))
A(para(f"<strong>Few, large buyers.</strong> One customer took about 73% of second quarter revenue, and two took "
       f"{Q2_TOP2[0] * 100:.0f}% and {Q2_TOP2[1] * 100:.0f}% of the first half (amended 10-Q), and in 2025 {RELATED_SHARE_25 * 100:.0f}% of revenue went to related parties, mainly Brookfield joint "
       "ventures in which Bloom holds stakes. <strong>Gas and supply.</strong> The boxes need gas and scandium; a supply or permit "
       "shock would slow deployments. <strong>Quality of earnings.</strong> Non-GAAP figures exclude stock-based pay; a short report "
       "and a securities lawsuit are outstanding."))

A('<div class="keeptogether">')
A(section("What would change our mind"))
A(para(f"<strong>Into a short:</strong> a price above about US${REVISIT_SHORT:.0f}, which would put my base case 25% below it, or "
       "a 2027 guide in February of less than 40% growth. <strong>Into a long:</strong> a price below about "
       f"US${REVISIT_LONG:.0f}, or product gross margin of 38% or more in two quarters running, which would show Bloom pricing the "
       "time it sells."))
A(para("<strong>The call is wrong if</strong> Bloom's 2027 revenue reaches US$7bn or more with non-GAAP gross margin of 36% or "
       "more, or the shares close above US$360 or below US$200 by October 2027."))
A('</div>')

A(section("Conclusion"))
A(para("The September piece argued that Bloom sells time, not electricity. The buyers prove it: Oracle, AEP and Brookfield are "
       "committing billions for speed. What I got wrong was how Bloom is paid for it. Product margin has been flat at about 35% "
       "while revenue tripled, so the premium arrives as volume, and volume is set by a factory. At US$"
       f"{PRICE:.2f} the price needs about {NEED_GW28:.1f} GW in 2028. My call: {CALL['direction']}, "
       f"{CALL['conviction'].lower()} conviction, leaning short; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}. "
       f"Revisit above about US${REVISIT_SHORT:.0f} or below about US${REVISIT_LONG:.0f}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Revenue growth", f"{(REV26 / REV_H[1] - 1) * 100:.0f}%", f"{B[1] * 100:.0f}%", f"{B[2] * 100:.0f}%", f"H2 2026 US${Q3E_REV} and {Q4E_REV}bn, mine; guide US$3.9 to 4.2bn"],
        ["Gross margin (non-GAAP)", pc(GM26), pc(B[3]), pc(B[4]), "Guide about 34% for 2026; product margin flat"],
        ["Operating costs, US$bn", f"{OPEX26:.2f}", f"{B[5]:.2f}", f"{B[6]:.2f}", "Q2 2026 run-rate US$0.50bn a year; R&D and sales rising"],
        ["Tax rate (non-GAAP)", f"{TAX26 * 100:.0f}%", f"{TAX27 * 100:.0f}%", f"{TAX28 * 100:.0f}%", "Losses carried forward; H1 2026 rate 0.7%"],
        ["Fully diluted shares, m", f"{SH26 * 1000:.0f}", f"{SH27 * 1000:.0f}", f"{SH28 * 1000:.0f}", "Outstanding plus notes and awards; 1.5% a year more"],
        ["Megawatt price, US$m", f"{USD_PER_MW:.2f}", "", "", "AEP: about US$2.65bn for most of 900 MW; my conversion"],
        ["Target multiple", "", "", f"{BASE_PE}x", "GE Vernova 47.3x; Vertiv 31.9x; Caterpillar 29.4x"],
    ],
), [27, 11, 9, 9, 44]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Bloom Energy quarterly results releases furnished on Form 8-K, Q2 2024 to Q2 2026 (28 July 2026), with '
  'their comparative quarters, for revenue and cost by line, GAAP and non-GAAP margins, operating income, EPS, related-party '
  'revenue, guidance and backlog. Bloom Form 10-K for 2025 for backlog definitions, service contract terms, the 2 GW plan and grid '
  'context. Bloom Form 10-Q/A for Q2 2026 (29 July 2026) for the convertible notes, the Oracle warrant, the diluted share count, Brookfield joint '
  'ventures, customer concentration and the short report. Bloom announcements of 13 April 2026 (Oracle), 30 June 2026 '
  '(Brookfield) and 19 August 2026 (Power Connect); AEP option exercise as reported on 8 January 2026. Consensus EPS from '
  'stockanalysis.com and Nasdaq.com (Zacks); multiples and average target from stockanalysis.com; share prices from Yahoo Finance; '
  'all retrieved 6 October 2026. Estimates for 2026 to 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 24 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/the-product-is-time/">thephysicallayer.fyi/journal/the-product-is-time</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Bloom Energy. Personal research, not investment advice.</p>')
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
