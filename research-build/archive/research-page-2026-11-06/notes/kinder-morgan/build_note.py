# -*- coding: utf-8 -*-
"""Kinder Morgan, Inc. (NYSE: KMI) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/kinder-morgan.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Kinder Morgan, Inc. (NYSE: KMI)"
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


def bn(x, d=2):
    return f"{x / 1000:,.{d}f}"


bear, base, bull = (x["value"] for x in SC)
tgt = CALL["target"]
tp_txt = usd(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({UP_BASE * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
direction = CALL["direction"].lower() if CALL["direction"] == "NO CALL" else CALL["direction"]
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

A('<h1 class="doctitle">Kinder Morgan, Inc.</h1>')
A('<p class="docsubtitle"><b>NYSE: KMI | Natural gas pipelines and storage, products pipelines, terminals | Houston, Texas</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{usd(PRICE)} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{usd(PRICE)}, NYSE close {PRICE_DATE}; highest close since Dec 2023 {usd(HI_CLOSE)} ({HI_CLOSE_DATE})"),
    ("Market value", f"US${MCAP:.1f}bn on {SHARES:,.1f}m shares (22 Oct 2026)"),
    ("Net debt, 30 Sep 2026", f"US${NET_DEBT / 1000:.1f}bn, {LEV_SEP26} times trailing EBITDA; enterprise value about US${EV:.1f}bn"),
    ("2026 outlook (21 Oct 2026)", "Adjusted EBITDA more than 6% above the US$8.6bn budget; Adjusted EPS more than 13% above US$1.36"),
    ("EV / Adjusted EBITDA", f"{EV_LTM:.1f}x trailing; {EV_26:.1f}x my 2026E; {EV_28:.1f}x my 2028E"),
    ("Dividend", f"US$1.19 declared for 2026; yield {DIV_YIELD * 100:.1f}%, against {DIV_YIELD_DEC23 * 100:.1f}% at end 2023"),
    ("Project backlog", f"US$14.4bn at 30 Sep 2026; more than 75% for power plants and local gas utilities"),
    ("Consensus (stockanalysis.com)", f"Average target {usd(CONS_TP)} ({CONS_N} analysts); EPS US$1.57 for 2026, US$1.55 for 2027"),
    ("Next event", "2027 budget and Q4 2026 results; dates not announced (8 Dec 2025 and 21 Jan 2026 last cycle)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Kinder Morgan has booked the gas for AI power. At US$33.87, the price has already counted it.</p>')
A(para("Kinder Morgan runs America's largest network of gas pipelines. My journal piece on building your own power argued that an AI "
       "campus building its own gas power swaps the grid's queue for the makers', and that the gas pipe lands on the same clock as the "
       "turbine. Kinder Morgan's release of 21 October agrees: Permian Link, for an A-rated hyperscaler's new power plants, was "
       "announced as sanctioned that day and opens in the third quarter of 2030."))
A(para(f"The demand is contracted, but it lands late, and the market re-priced the shares for it in 2024. At {usd(PRICE)} Kinder Morgan "
       f"trades at {EV_LTM:.1f} times trailing EBITDA, against {HIST_EV[0]:.1f} times at the end of 2023. At that old multiple the price "
       "would need the whole backlog's EBITDA already earned."))
A(para(f"<b>{my_call}: {direction}, {conv} conviction.</b> {BASE_MULT} times my 2028 EBITDA of US${E28 / 1000:.2f}bn gives "
       f"{usd(BASE_VALUE)}, {chg(BASE_VALUE)}, inside a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} ({chg(bull)}). "
       "A long needs 15% or more."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (calendar years; Adjusted EBITDA and EPS as Kinder Morgan defines them)"))
g = lambda a, b: f"{(a / b - 1) * 100:.0f}"
A(datatable(
    ["US$ million unless stated", "2023A", "2024A", "2025A", "2026E*", "2027E*", "2028E*"],
    [
        ["Adjusted EBITDA", f"{EBITDA_H[0]:,.0f}", f"{EBITDA_H[1]:,.0f}", f"{EBITDA_H[2]:,.0f}", f"{EBITDA26:,.0f}", f"{E27:,.0f}", f"{E28:,.0f}"],
        ["Growth (%)", "", g(EBITDA_H[1], EBITDA_H[0]), g(EBITDA_H[2], EBITDA_H[1]), g(EBITDA26, EBITDA_H[2]), g(E27, EBITDA26), g(E28, E27)],
        ["of which new backlog projects (mine)", "", "", "", "", f"{BL27:,.0f}", f"{BL28:,.0f}"],
        ["Net debt, year end", f"{NETDEBT_H[0]:,.0f}", f"{NETDEBT_H[1]:,.0f}", f"{NETDEBT_H[2]:,.0f}", f"{ND26:,.0f}", f"{ND27:,.0f}", ""],
        ["Net debt / EBITDA (x)", "4.2", "4.0", "3.8", f"{LEV26_OUT:.1f}", f"{LEV27:.1f}", ""],
        ["Adjusted EPS (US$)", "1.07", "1.15", "1.30", f"{EPS26_FLOOR:.2f}+ (guide)", f"{CONS_EPS27:.2f} (cons.)", ""],
        ["Dividend declared (US$)", "1.13", "1.15", "1.17", "1.19", f"{DPS27:.2f}", ""],
        [f"EV / EBITDA at {usd(PRICE)} (x)", f"{HIST_EV[0]:.1f}&dagger;", f"{HIST_EV[1]:.1f}&dagger;", f"{HIST_EV[2]:.1f}&dagger;", f"{EV_26:.1f}", f"{EV_27:.1f}", f"{EV_28:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E EBITDA is my reading of Kinder Morgan's 'more than 6% favorable' to its US$8.6bn budget; 2026 EPS is Kinder Morgan's floor of "
          "more than 13% above US$1.36; 2027 EPS is the stockanalysis.com consensus of 28 October 2026. Net debt at end 2026 uses Kinder Morgan's "
          "own 3.6x expectation. All other estimates are mine. &dagger;At each year-end price, not today's. Leverage for 2023 to 2025 is net debt "
          "over that year's Adjusted EBITDA, my arithmetic; Kinder Morgan reports 3.8x for 2025. Sources: Kinder Morgan results releases, January 2024 to October 2026."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: EBITDA that grows late, and a value close to the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: Adjusted EBITDA, US$bn; 2023A to 2025A per Kinder Morgan, 2026E to 2029E mine, with new backlog projects in red. Right: value "
          "per share from the base case, the weighted cases, the sensitivity grid, the bear to bull range and a dividend cross-check, against the price (grey)."))
A('</div>')

A(section("The thesis: the water main is laid only after the neighbours sign"))
A(para("Think of the street from the piece, where every house is sinking its own well. Someone still has to lay the main that feeds the pump. "
       "The firm that owns the mains does not dig on hope. It waits until the neighbours sign twenty-year standing orders, paid whether or "
       "not they draw the water, and only then breaks ground."))
A(para("Kinder Morgan is that firm. It owns or operates about 78,000 miles of pipeline, more than 65,000 of them for gas, and over 700 "
       "billion cubic feet of working gas storage. Most of its income is a reservation fee: a shipper books space on a pipe and pays "
       "for it whether gas flows or not. That is take-or-pay, and it makes AI power demand unusually easy to see, because a pipe enters "
       "the backlog only once the shippers have signed."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_backlog.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_land.png"></div></div>')
A(caption("Left: project backlog at quarter end, US$bn. Sources: results releases, January 2024 to October 2026. Right: Kinder Morgan's share of "
          f"capital in sixteen named projects with a cost and date (US${NAMED_TOTAL / 1000:.1f}bn of the US$14.4bn backlog), by first in-service "
          "year; a two-phase project sits in its first year. Sources: 2025 Form 10-K project table and 2026 releases; grouping is my arithmetic."))
A('</div>')
A(para(f"The backlog was US$3.0bn at the end of 2023 and US$14.4bn at the end of September 2026, US$13.2bn of it natural gas. Kinder Morgan "
       "says more than 75% of it supports power generation and local gas utilities, up from nearly 60% in March. The quarter added the "
       "two pipes the piece named. Permian Link, about 2.8 Bcf/d over 434 miles, \"will serve new power generation for an A-rated "
       "hyperscaler\" from the third quarter of 2030. The Southeast Connector, up to 2.6 Bcf/d over about 470 miles, opens in phases "
       "from the fourth quarter of 2030. Both were announced as sanctioned on 21 October on long-term take-or-pay agreements; on the call, per "
       "the transcript published by Earnings Whispers, management said both run at least 20 years."))
A(para("<b>The claim holds.</b> The piece said pipe \"sanctioned in October 2026 lands in 2030, level with heavy turbines sold out to "
       "2030\". The release gives exactly those dates, and every Kinder Morgan figure in the piece matches it: the US$14.4bn backlog, the "
       "share above 75%, Permian Link's capacity, customer and date, and the Southeast Connector's phases. "
       "Take-or-pay adds one point: if the hyperscaler's turbines come late, the pipe is still paid for. The turbine queue is "
       "the buyer's timing risk, not the pipe owner's."))
A(para(f"<b>What it is worth, and when.</b> Kinder Morgan says the US$13.7bn of the backlog that is mainly take-or-pay should cost about 5.7 times "
       f"the EBITDA it earns in its first full year: about US${BACKLOG_EBITDA / 1000:.1f}bn a year once complete, by my arithmetic, a quarter "
       f"on top of 2026. But it opens late. Of the named projects, US${LAND[2027] / 1000:.1f}bn opens in 2027, mostly Trident to the Port "
       f"Arthur export corridor; US${LAND[2028] / 1000:.1f}bn in 2028; and US${LAND[2030] / 1000:.1f}bn, {LAND[2030] / 14400 * 100:.0f}% of "
       f"the backlog, in 2030. The two pipes built for power are US${AI_PIPES / 1000:.1f}bn of that: about US${AI_PIPES_EBITDA / 1000:.1f}bn "
       f"of EBITDA, {AI_PIPES_EBITDA / EBITDA26 * 100:.0f}% of 2026, little of it before 2031."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {usd(PRICE)} Kinder Morgan is worth US${MCAP:.1f}bn. With US${NET_DEBT / 1000:.1f}bn of net debt and US${NCI / 1000:.1f}bn of "
       f"minority interests, the enterprise value is about US${EV:.1f}bn: {EV_LTM:.1f} times trailing Adjusted EBITDA and {EV_28:.1f} times my "
       f"2028 estimate. The same arithmetic gave {HIST_EV[0]:.1f} times at the end of 2023, {HIST_EV[1]:.1f} at the end of 2024 and "
       f"{HIST_EV[2]:.1f} at the end of 2025. The re-rating happened in 2024; since then the shares have roughly followed earnings, up "
       f"{YTD * 100:.0f}% this year as EBITDA beat its budget. The dividend yield fell from {DIV_YIELD_DEC23 * 100:.1f}% to {DIV_YIELD * 100:.1f}%."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["Jan 2024", "Backlog US$3.0bn; 9.6x EBITDA at end 2023", f"{usd(PX_JAN24)}"],
        ["Late 2024", "Gas for AI power becomes a theme; backlog US$8.1bn", "11.8x at year end"],
        ["22 Apr 2026", "Q1: cold winter; EBITDA up 18%", ""],
        ["22 Oct 2026", "Q3 after the close on 21 Oct: backlog US$14.4bn", f"{Q3_MOVE * 100:+.1f}%"],
        ["Since Jan 2024", "Price doubled", f"up {SINCE_JAN24 * 100:.0f}%"],
    ],
), [21, 57, 22]))
A('</div></div>')
A(caption("Left: Kinder Morgan month-end close, January 2024 to 30 October 2026, against my base value (red). Nasdaq historical quotes, not "
          "adjusted for dividends, retrieved 2 November 2026. Right: multiples are my arithmetic at each year-end price."))
A('</div>')
A(para(f"<strong class='lead'>At the old multiple, the price holds the whole backlog.</strong> At {HIST_EV[0]:.1f} times, today's "
       f"enterprise value needs about US${IMPLIED_EBITDA_AT_23 / 1000:.1f}bn of EBITDA: my underlying 2026 of about US${UNDERLYING26 / 1000:.1f}bn "
       f"plus all US${BACKLOG_EBITDA / 1000:.1f}bn the backlog earns when complete. The market bought the demand in 2024, years before most "
       "of it opens."))
A(para("<strong class='lead'>I differ on timing, not on demand.</strong> 2026 is flattered: Kinder Morgan expects to beat its US$8.6bn "
       "budget by more than 6%, and on the call, per the transcript published by Earnings Whispers, put about US$225m of the beat down to "
       "items that may not recur and about US$175m to commodity prices. The consensus sees a flat 2027, US$1.57 of EPS this year and US$1.55 next. And the "
       "projects that open before 2028 serve mostly export and industry, not AI power."))
A(para("<strong class='lead'>None of this makes it expensive.</strong> Contracted revenue under take-or-pay and minimum volume deals "
       "was US$37bn at 30 September, US$31bn of it from 2028 on (10-Q). Leverage is 3.5 times, at the low end of Kinder Morgan's target "
       "range, and Moody's raised it to Baa1 in March. The demand the market bought has simply to be built first."))

A(section("Valuation, with the working"))
A(para("I value Kinder Morgan on enterprise value to Adjusted EBITDA, twelve months out: by October 2027 the market will price 2028. From "
       f"my 2026E of US${EBITDA26 / 1000:.2f}bn I remove the US$225m that may not recur, grow the existing business {BASE_G * 100:.0f}% a year "
       f"(escalators, high use, 2026 projects for a full year) and add backlog EBITDA of US${BL27:.0f}m in 2027 and US${BL28:.0f}m in 2028. "
       f"Net debt reaches about US${ND27 / 1000:.1f}bn at end 2027, as about US${CAPEX27 / 1000:.1f}bn of capital spending and "
       f"US${DPS27 * SHARES / 1000:.1f}bn of dividends exceed about US${CFO27 / 1000:.2f}bn of operating cash flow. All are my estimates."))
A(para(f"<strong class='lead'>The multiple.</strong> I use {BASE_MULT} times 2028 EBITDA, the middle of Kinder Morgan's own range since "
       f"the re-rating ({HIST_EV[2]:.1f} to {EV_LTM:.1f} times). {BASE_MULT} x US${E28 / 1000:.2f}bn = US${BASE_MULT * E28 / 1000:.1f}bn, less "
       f"US${ND27 / 1000:.1f}bn of net debt and US${NCI / 1000:.1f}bn of minority interests, over {SHARES:,.1f}m shares: {usd(BASE_VALUE)}, "
       f"{UP_BASE * 100:.0f}% above the price. Gas pipeline peers trade higher and set the bull case."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EBITDA", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "No underlying growth; projects slip a year; rates take the multiple back towards 2023", f"US${SC[0]['e28'] / 1000:.2f}bn", f"{SC[0]['mult']:.1f}x", usd(bear), chg(bear), "25%"],
        ["Base", "Underlying growth 1%; backlog opens on Kinder Morgan's dates", f"US${SC[1]['e28'] / 1000:.2f}bn", f"{SC[1]['mult']:.1f}x", usd(base), chg(base), "50%"],
        ["Bull", "Growth 1.5%; more sanctioned and earlier; multiple closes part of the gap to Williams", f"US${SC[2]['e28'] / 1000:.2f}bn", f"{SC[2]['mult']:.1f}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 41, 12, 9, 11, 10, 8]))
A(caption(f"Backlog EBITDA in 2028: bear US${SC[0]['bl']:.0f}m, base US${SC[1]['bl']:.0f}m, bull US${SC[2]['bl']:.0f}m. Net debt and minority "
          "interests are the same in every case. Contracted cash flows make the bear case mostly a multiple story, not an earnings one."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 EBITDA against the multiple"))
A('<div class="chartsrow"><div class="col left">')
grid = [[value(e, mm) for mm in SENS_M] for e in SENS_E]
A(datatable(
    ["2028 EBITDA"] + [f"{mm:.1f}x" for mm in SENS_M],
    [[f"US${e / 1000:.2f}bn"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_E, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
A(para(f"{W[n_above]} of the nine cells sit above the price, and only {W[n_15].lower()} sit 15% or more above it. A long needs about "
       f"{EV_MULT_FOR_LONG:.1f} times my base EBITDA, a multiple Kinder Morgan has not held at any year end since at least 2023. A short "
       f"needs a price above about {usd(SHORT_ABOVE)}. The dividend agrees: US${DPS27:.2f} at today's {DIV_YIELD * 100:.1f}% yield is "
       f"{usd(DIV_CHECK)}."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "EV/EBITDA", "Dividend yield", "What they run"],
    [[c, t, f"{e:.1f}x", f"{y * 100:.1f}%", w] for c, t, e, y, w, grp in PEERS],
    num_cols={2, 3},
), [20, 13, 11, 12, 44]))
A(caption("Trailing EV/EBITDA and dividend yield from stockanalysis.com, retrieved 2 November 2026 (closes of 30 October). Its EBITDA is not "
          f"Kinder Morgan's Adjusted EBITDA, so Kinder Morgan shows 14.1x here against {EV_LTM:.1f}x on its own measure; compare the peers on "
          "this basis only. Peer median 16.1x. Multiples set the range only; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Early Dec 2026 (not announced)", "2027 budget (8 Dec last year)", "Adjusted EBITDA against my US$9.31bn and the US$9.7bn revisit level"],
        ["Late Jan 2027 (not announced)", "Q4 2026 results (21 Jan last year)", "2026 EBITDA against US$9.1bn; backlog additions and in-service"],
        ["Q1 2027", "Trident first phase in service", "On time; the largest 2027 project, US$1.8bn"],
        ["2027 to 2028", "Permits for Permian Link and the Southeast Connector", "FERC filings and any challenge to the dates"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Rates.</strong> Kinder Morgan is bought partly for its dividend. If long rates rise, the multiple falls whatever the backlog does. "
       f"The bear case is mostly this, {chg(bear)}."))
A(para("<strong>Permits and building.</strong> Every date is \"subject to the timely receipt of all required permits and approvals\". The two "
       "power pipes are about 900 miles of new line. Kinder Morgan bears overruns, and the 5.7 times build multiple holds only on budget."))
A(para("<strong>One customer, one place.</strong> Permian Link serves one hyperscaler's new plants in the Texas Panhandle. Take-or-pay protects "
       "against a late plant, not a cancelled contract."))
A(para("<strong>Commodities and one-offs.</strong> The CO2 and products businesses carry oil and product price risk; about US$225m of 2026 "
       "may not recur; a US$138m legal and environmental accrual, kept out of Adjusted EBITDA, hit products in the third quarter."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Towards a long:</strong> {REVISIT_IF} <strong>Towards a short:</strong> a price above about {usd(SHORT_ABOVE)} on unchanged estimates."))
A(para(f"<strong>{my_call} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para("The piece argued that own gas power trades the grid's queue for the makers', and that the pipe lands with the turbine. Kinder Morgan's "
       "filings agree. The demand is contracted and the backlog is the largest in the company's "
       "history. But the market re-priced Kinder Morgan for it in 2024, and at the old multiple today's price holds all of the backlog before "
       f"most of it opens. {my_call}: {direction}, {conv} conviction; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Adjusted EBITDA, US$m", f"{EBITDA26:,.0f}", f"{E27:,.0f}", f"{E28:,.0f}", "More than 6% above the US$8.6bn budget in 2026"],
        ["Potentially non-recurring, US$m", f"{NONREC26:.0f}", "removed", "removed", "Q3 call transcript (Earnings Whispers)"],
        ["Underlying growth", "", f"{BASE_G * 100:.0f}%", f"{BASE_G * 100:.0f}%", "Escalators, use, 2026 projects for a full year"],
        ["Backlog project EBITDA, US$m", "", f"{BL27:.0f}", f"{BL28:.0f}", "Named opening dates; 5.7x build multiple"],
        ["Net debt, year end, US$m", f"{ND26:,.0f}", f"{ND27:,.0f}", "", "3.6x in 2026 (Kinder Morgan); cash flow after"],
        ["Dividend, US$", "1.19", f"{DPS27:.2f}", "", "About 2% a year, as since 2024"],
        ["Shares, m", f"{SHARES:,.1f}", f"{SHARES:,.1f}", f"{SHARES:,.1f}", "No buybacks assumed"],
    ],
), [27, 13, 12, 12, 36]))
A(caption(f"All my estimates unless marked. Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Kinder Morgan quarterly results releases (Form 8-K, Exhibit 99.1), 17 January 2024 to 21 October 2026, for Adjusted '
  'EBITDA, Adjusted EPS, dividends, backlog, Project EBITDA multiples, net debt, minority interests, cash flow and the 2026 budget and '
  'outlook; the release of 21 October 2026 for Permian Link, the Southeast Connector, Creekside and Bear Creek. Form 10-Q for the quarter '
  'to 30 September 2026 (filed 23 October 2026) for shares, 2026 growth spending and remaining performance obligations. 2025 Form 10-K '
  '(filed 13 February 2026) for the major projects table. Third quarter 2026 earnings call, 21 October 2026, transcript published by '
  'Earnings Whispers. Kinder Morgan\'s 2026 financial expectations, 8 December 2025. Share prices from Nasdaq historical quotes; consensus, '
  'targets and peer multiples from stockanalysis.com (S&amp;P Global data); all retrieved 2 November 2026. Estimates for 2026 to 2029 are '
  'the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests the gas pipe section of my journal piece, '
  '<a href="https://thephysicallayer.fyi/journal/building-your-own-power/">thephysicallayer.fyi/journal/building-your-own-power</a>, '
  'and its claim on record; all notes and their track record are at '
  '<a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Kinder Morgan. Personal research, not investment advice.</p>')
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
