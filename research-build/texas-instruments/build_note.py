# -*- coding: utf-8 -*-
"""Texas Instruments (Nasdaq: TXN) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/texas-instruments.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Texas Instruments (Nasdaq: TXN)"
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

P = []
A = P.append


def cols(html, widths):
    cg = "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in widths) + "</colgroup>"
    i = html.index(">") + 1
    return html[:i].replace('class="datatable', 'style="table-layout:fixed" class="compact datatable') + cg + html[i:]


def usd(x, d=0):
    return f"US${x:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
pb = project(*SCEN[0][1:5]); pu = project(*SCEN[2][1:5]); PB = project(*SCEN[1][1:5])

A('<h1 class="doctitle">Texas Instruments Incorporated</h1>')
A('<p class="docsubtitle"><b>Nasdaq: TXN | Analog and embedded chips, including power chips for AI servers | Dallas, Texas</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:.2f} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:.2f}, Nasdaq close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:.2f}"),
    ("Market value", f"About US${MCAP:.0f}bn on {DILUTED * 1000:.0f}m diluted shares; net debt US${NETDEBT:.1f}bn at 30 Jun 2026"),
    ("P/E on my estimates", f"{PRICE / EPS26:.1f}x 2026E, {PRICE / EPS27:.1f}x 2027E, {PRICE / EPS28:.1f}x 2028E"),
    ("Consensus", f"EPS US${CONS_EPS_26:.2f} 2026, US${CONS_EPS_27:.2f} 2027; forward P/E {FWD_PE_SA:.1f}x; target US${CONS_TP:.0f} (stockanalysis.com)"),
    ("Dividend", f"US${DPS_NEW:.2f} a quarter from November, yield {DIV_YIELD * 100:.1f}%"),
    ("Free cash flow", f"US${TTM_FCF:.1f}bn in the 12 months to June 2026, incl. US${TTM_CHIPS:.1f}bn CHIPS Act cash"),
    ("Data centre", f"9% of 2025 revenue; about {DC_SHARE_Q2 * 100:.0f}% in Q2 2026 on my working"),
    ("Q3 2026 guide (22 Jul)", "Revenue US$5.65 to 6.15bn; EPS US$2.23 to 2.57; tax about 13%"),
    ("Next results", "Q3 2026: Wednesday 21 Oct 2026, 3:30pm Central time"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Texas Instruments\' data centre business is real. At US$295, the shares already pay for a full analog upturn as well.</p>')
A(para("TI makes many of the small power chips that step electricity down to an AI processor. On 2 October I argued that the "
       "move to 800 volt racks turns them into a growing data centre business. The claim is holding: data centre revenue doubled "
       f"in a year, and on my working it reached about {DC_SHARE_Q2 * 100:.0f}% of revenue in the second quarter, a third of TI's growth."))
A(para("The obvious objection is that the stock is mostly an analog-cycle bet. That is right. Swinging the rest of TI from my bear to "
       f"my bull case moves 2028 earnings by {usd(RE_SWING, 2)} a share; doing the same to data centre moves them by {usd(DC_SWING, 2)}. "
       f"At US${PRICE:.2f} the shares are {PRICE / EPS26:.0f} times my 2026 earnings and need 2028 revenue about "
       f"{(NEED_REV28 / REV_H[3] - 1) * 100:.0f}% above the 2022 peak."))
A(para(f"<b>My call: {CALL['direction']}, {CALL['conviction'].lower()} conviction.</b> My base case is worth {usd(BASE_VALUE)}, "
       f"{chg(BASE_VALUE)}. A turn in the cycle is {usd(bear)} ({chg(bear)}), against a bull case of {usd(bull)} ({chg(bull)}). "
       f"I would revisit below about US${REVISIT:.0f}."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials"))
A(datatable(
    ["US$ billion unless stated", "2022A", "2024A", "2025A", "2026E*", "2027E*", "2028E*"],
    [
        ["Revenue", f"{REV_H[3]:.2f}", f"{REV_H[5]:.2f}", f"{REV_H[6]:.2f}", f"{REV26:.2f}", f"{R27:.2f}", f"{R28:.2f}"],
        ["Of which data centre", "n.d.", "n.d.", f"{DC_25:.1f}", f"{DC_26E:.2f}", f"{PB['dc27']:.2f}", f"{PB['dc28']:.2f}"],
        ["Revenue growth (%)", "9", "(11)", f"{(REV_H[6] / REV_H[5] - 1) * 100:.0f}", f"{(REV26 / REV_H[6] - 1) * 100:.0f}", f"{(R27 / REV26 - 1) * 100:.0f}", f"{(R28 / R27 - 1) * 100:.0f}"],
        ["Gross margin (%)", f"{GM22 * 100:.1f}", f"{GP_H[5] / REV_H[5] * 100:.1f}", f"{GP_H[6] / REV_H[6] * 100:.1f}", "not forecast", "not forecast", "not forecast"],
        ["Operating margin (%)", f"{OM22 * 100:.1f}", f"{OP_H[5] / REV_H[5] * 100:.1f}", f"{OP_H[6] / REV_H[6] * 100:.1f}", f"{OM26 * 100:.1f}", f"{OM27 * 100:.1f}", f"{OM28 * 100:.1f}"],
        ["Diluted EPS (US$)", f"{EPS_H[3]:.2f}", f"{EPS_H[5]:.2f}", f"{EPS_H[6]:.2f}", f"{EPS26:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}"],
        [f"P/E at US${PRICE:.2f} (x)", f"{PRICE / EPS_H[3]:.1f}", f"{PRICE / EPS_H[5]:.1f}", f"{PRICE / EPS_H[6]:.1f}", f"{PRICE / EPS26:.1f}", f"{PRICE / EPS27:.1f}", f"{PRICE / EPS28:.1f}"],
        ["Depreciation", f"{DEP_H[3]:.2f}", f"{DEP_H[5]:.2f}", f"{DEP_H[6]:.2f}", "2.30", f"{2.30 + DDEP27:.2f}", f"{2.30 + DDEP27 + DDEP28:.2f}"],
        ["Capital spending", f"{CAPEX_H[3]:.2f}", f"{CAPEX_H[5]:.2f}", f"{CAPEX_H[6]:.2f}", "2 to 3", "", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E to 2028E are my own estimates; n.d. = not disclosed. 2026E uses the reported first half plus my third quarter "
          f"(revenue US${Q3E_REV}bn, EPS US${Q3E_EPS:.2f}, the guide midpoint) and fourth (US${Q4E_REV}bn, US${Q4E_EPS:.2f}). Ahead, operating "
          f"profit rises by {FALL * 100:.0f}% of extra revenue before depreciation, less extra depreciation; EPS = (operating profit less "
          f"about US$0.3bn net interest) x (1 - {TAX * 100:.0f}% tax) / 920m shares. 2026 depreciation and capital spending are TI's guides. "
          "History from TI's Forms 10-K (SEC XBRL). Silicon Labs is excluded."))

A('<div class="keeptogether">')
A(section("Two charts: an upturn I expect to mature, and a valuation that sits around the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and operating margin, 2019A to 2028E; 2019A to 2025A per TI, the rest my estimates. Right: value per share "
          "from the base case, the probability-weighted cases, the sensitivity grid and the bear to bull range, against the "
          f"US${PRICE:.2f} price (red) and the stockanalysis.com average analyst target, retrieved 6 October 2026."))
A('</div>')

A(section("The thesis: the valves under the sink"))
A(para("Go back to the water main from the October piece. Water arrives at a pressure that would blast a glass out of your hand, "
       "and a row of cheap valves under the sink steps it down to the steady trickle the tap needs. The AI processor is the tap. "
       "TI makes many of the valves: power stages, converters, electronic fuses and hot-swap controllers, each selling for cents "
       "or a few dollars."))
A(para("<strong>How big data centre has become.</strong> TI first reported data centre as its own market for 2025: 9% of revenue, "
       "about US$1.5bn, up 64%, leaving the year at about US$450m a quarter. Since then TI gives only growth rates: about 90% in the "
       "first quarter of 2026, and in the second a doubling on a year earlier and about 20% on the first quarter. Those rates are "
       f"enough to size it. On my working, data centre was about US${DC_Q2_26 * 1000:.0f}m in the second quarter, "
       f"{DC_SHARE_Q2 * 100:.0f}% of revenue, and supplied {DC_GROWTH_SHARE * 100:.0f}% of TI's US$1.0bn rise on a year earlier."))
A(para("<strong>Which racks it comes from.</strong> That doubling comes from today's racks at 48 and 54 volts. In July TI said the "
       "800 volt design will be phased in, with more conversion stages and more of its parts per rack. The claim's 800 volt "
       "mechanism is still ahead of TI's numbers, not behind them."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_dc.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_qgm.png"></div></div>')
A(caption("Left: data centre revenue and share of TI revenue by quarter, my derivation from the growth rates TI gave on its calls of "
          "27 January, 22 April and 22 July 2026 (TI does not disclose quarterly sizes). Right: gross margin by quarter, Q1 2024 to "
          "Q2 2026, against 2022 (dashed). Source: TI quarterly earnings releases; SEC XBRL company facts."))
A('</div>')
A(para(f"<strong>The factory build.</strong> TI spent about US${CAPEX_CYCLE:.0f}bn on capital projects from 2021 to 2026, counting "
       "the 2026 guide midpoint. The first Sherman fab began production on 17 December 2025, and TI says a chip made on 300mm costs "
       "about 40% less than on 200mm. Capital spending falls to US$2 to 3bn in 2026, and CHIPS Act grants and tax credits return "
       f"part of it. Free cash flow rose from US${(CFO_H[5] - CAPEX_H[5]):.1f}bn in 2024 to US${TTM_FCF:.1f}bn in the twelve months to June 2026."))

A(section("Where I was wrong in October"))
A(para("In the piece I called TI's 61% gross margin what owning cheap, full factories looks like in money. TI's factories are not "
       "full, and the piece itself said they still had to be filled. On the July call TI said loadings rose through the second quarter and were still rising into the third, and that it "
       f"has empty clean room space ready to equip. The margin is also {GM22 * 100 - GM_Q2 * 100:.0f} points below 2022's "
       f"{GM22 * 100:.1f}%, on revenue of about what TI earned in the year to June 2026, mostly because depreciation rose from US${DEP_H[3]:.2f}bn in 2022 to US${DEP_H[6]:.2f}bn "
       "in 2025, with US$2.2 to 2.4bn guided for 2026. Putting the July call next to the depreciation line showed the slip. It "
       "matters: partly filled factories leave room for the margin to rise, but the larger fixed cost base makes earnings fall faster "
       "if the cycle turns. The piece and the claim stay exactly as published."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:.2f} TI is worth about US${MCAP:.0f}bn, with net debt of about US${NETDEBT:.0f}bn before the US$7.5bn "
       f"Silicon Labs purchase, due to close in the first half of 2027. That is {PRICE / EPS26:.1f} times my 2026 estimate of "
       f"US${EPS26:.2f}, in line with the US${CONS_EPS_26:.2f} consensus, and {PRICE / EPS27:.1f} times my 2027 estimate of "
       f"US${EPS27:.2f} ({PRICE / CONS_EPS_27:.1f} times the US${CONS_EPS_27:.2f} consensus). On TI's own framework, my 2026 revenue "
       f"implies free cash flow of about US${FCF26_MID:.1f}bn, US${FCF26_PS:.2f} a share: a {FCF26_PS / PRICE * 100:.1f}% yield, "
       "including CHIPS Act cash."))
A(para(f"<strong class='lead'>What the price needs.</strong> By October 2027 the market will price 2028. At {BASE_PE} times, "
       f"US${PRICE:.2f} needs 2028 earnings of US${NEED_EPS28:.2f}, which on my margin bridge needs revenue of about "
       f"US${NEED_REV28:.1f}bn: {(NEED_REV28 / REV_H[3] - 1) * 100:.0f}% above the 2022 peak of US${REV_H[3]:.1f}bn, and a fourth "
       "straight year of growth. In the last cycle revenue grew two years running, then fell 22% over the next two."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_capex.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: capital spending, depreciation and free cash flow (TI's definition, including CHIPS Act proceeds), 2019 to 2025, "
          "with 2026 guide midpoints (SEC XBRL company facts; TI 2025 Form 10-K and 27 January 2026 call). Right: TXN month-end "
          "close, November 2023 to the 5 October 2026 close, not adjusted for dividends (Yahoo Finance, retrieved 6 October 2026), "
          "against my base value."))
A('</div>')
A(para("<strong class='lead'>Where I differ.</strong> I agree data centre is real and fast-growing. I differ on how much of the price "
       "it can carry. Holding one driver at my base and swinging the other from bear to bull: data centre (25% to 60% growth in "
       f"2027, 15% to 40% in 2028) moves 2028 earnings by {usd(DC_SWING, 2)} a share; the rest of TI (an 8% fall to 12% growth in "
       f"2027) moves them by {usd(RE_SWING, 2)}. The cycle in factories, cars and phones is {RE_SWING / DC_SWING:.1f} times the "
       "bigger driver. So the objection is right about the stock, even though the AI exposure has grown faster than it assumes."))
A(para("Industrial grew about 30% on a year earlier in the second quarter. Part of that is customers restocking after two years of "
       f"running inventories down, which flatters a quarter or two. TI's own inventory fell from {INV_DAYS_Q4} days at the end of "
       f"2025 to {INV_DAYS_Q2} days in June: demand is catching up with its stock."))

A(section("Valuation, with the working"))
A(para("I value TI on earnings per share twelve months out, so on 2028, and cross-check against free cash flow yield, the measure "
       "TI itself targets. Revenue is built in two parts, data centre and the rest. Operating profit rises by 75% of each extra "
       "dollar before depreciation, the middle of TI's 70 to 85%, less extra depreciation of US$0.2bn in 2027 and US$0.1bn in 2028. "
       "The same fall-through applies in a downturn."))
A(para(f"<strong class='lead'>The multiple.</strong> I use {BASE_PE} times 2028 earnings. The six analog and power peers trade at "
       "a median of 23.3 times forward earnings; TI earns a premium for its own factories, its cash flow and 23 years of dividend "
       f"increases, but 2028 would be late in an upturn. {BASE_PE} x US${EPS28:.2f} = {usd(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "The upturn turns: rest of TI falls 8% then 2%; data centre grows 25% then 15%", usd(pb["eps28"], 2),
         f"{SCEN[0][5]}x", usd(bear), chg(bear), "25%"],
        ["Base", "The upturn matures: rest grows 7.5% then 2%; data centre 45% then 30%", usd(EPS28, 2), f"{BASE_PE}x",
         usd(base), chg(base), "50%"],
        ["Bull", "The upturn runs: rest grows 12% then 6%; data centre 60% then 40%", usd(pu["eps28"], 2),
         f"{SCEN[2][5]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [10, 40, 11, 9, 11, 11, 8]))
A(caption(f"All cases start from my 2026E (data centre US${DC_26E:.2f}bn, rest US${REST26:.2f}bn) and use the same margin "
          f"bridge. Even the bear case keeps 2028 revenue (US${pb['rev28']:.1f}bn) above 2025; earnings fall because the margin "
          "falls with volume across a larger cost base. The bear case loses more than the bull case gains."))
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
A(para(f"Only {above} of the nine cells sit above today's price. To make money from here, TI needs earnings above my base and a "
       "multiple close to today's. Every figure is live in the accompanying model, so a change to growth, fall-through or the "
       "multiple moves the value."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [[c, t, f"{p:.1f}x", w] for c, t, p, w in PEERS],
    num_cols={2},
), [22, 14, 12, 52]))
A(caption("Forward P/E from stockanalysis.com, retrieved 6 October 2026 (Infineon from an intraday price that day). TI at 30.5 "
          "times sits between the ordinary analog makers and Monolithic Power, the power specialist with large AI server sales. "
          "Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["21 Oct 2026, 3:30pm Central", "Q3 2026 results and call", "Revenue against US$5.65 to 6.15bn; gross margin as loadings rise; data centre growth; industrial momentum; Q4 guide"],
        ["October 2026", "Board declares the raised dividend", "US$1.52 a quarter, payable 10 November"],
        ["January 2027", "Q4 2026 results", "2027 capital spending and depreciation; any sign the industrial restock is ending"],
        ["First half of 2027", "Silicon Labs expected to close", "Financing, interest cost and deal charges"],
        ["2027 and after", "800 volt racks phase in", "Named operators adopting 800 volts; TI design wins in the first conversion stage"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The upturn runs longer.</strong> The bull case and the main risk to a no call. Restocking could last into 2027, "
       "and with empty clean room space and falling capital spending each extra dollar carries a high margin. TI also said on the "
       "July call that it had started raising prices, which builds through the second half. A gross margin of "
       "65% or more would be the clearest sign."))
A(para("<strong>The upturn turns.</strong> The bear case. Industrial and automotive are two thirds of revenue, and 30% industrial "
       "growth will not repeat for long. The new fixed cost base makes earnings fall faster than revenue."))
A(para("<strong>The data centre share is my estimate.</strong> TI gives rates, not sizes; different rounding could move my 12% by a "
       "point or so. The conclusion holds across that range. <strong>800 volt timing and rivals.</strong> TI says the design will "
       "be phased in; Infineon, Monolithic Power and Analog Devices compete for the same sockets. <strong>Silicon Labs.</strong> "
       "About US$0.8bn of revenue and up to US$5bn of new borrowing, neither in my numbers."))

A('<div class="keeptogether">')
A(section("What would change our mind"))
A(para(f"<strong>Into a call:</strong> a price below about US${REVISIT:.0f}, which would put my base case 15% above it; or third "
       "quarter results showing data centre at 15% or more of revenue while industrial still grows; or a gross margin of 65% or more."))
A(para("<strong>The call is wrong if</strong> full year 2027 revenue reaches US$26bn or more with data centre above 15% of it, or "
       "gross margin reaches 65% or more in any quarter to June 2027, or the shares trade above US$340 by October 2027 without either."))
A('</div>')

A(section("Conclusion"))
A(para("The October piece argued that the move to 800 volt racks turns TI's cheap power chips into a growing data centre business. "
       f"TI's own numbers say the business is real: doubled in a year, about {DC_SHARE_Q2 * 100:.0f}% of revenue on my working, a "
       "third of recent growth, and all of it before 800 volts arrives. The objection is still right about the shares: the "
       f"analog cycle moves earnings {RE_SWING / DC_SWING:.1f} times as much as data centre does, and the price already assumes a "
       f"fourth straight year of growth. My call: {CALL['direction']}, {CALL['conviction'].lower()} conviction. Revisit below about "
       f"US${REVISIT:.0f}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Data centre growth", f"{(DC_26E / DC_25 - 1) * 100:.0f}%", f"{DC_G27 * 100:.0f}%", f"{DC_G28 * 100:.0f}%", "H1 2026 derived from TI's rates; H2 US$0.76 and 0.80bn mine"],
        ["Rest of TI growth", f"{(REST26 / (REV_H[6] - DC_25) - 1) * 100:.0f}%", f"{RE_G27 * 100:.1f}%", f"{RE_G28 * 100:.0f}%", "Third and fourth years of the analog upturn"],
        ["Fall-through before depreciation", "", f"{FALL * 100:.0f}%", f"{FALL * 100:.0f}%", "TI: 70 to 85% (22 July 2026 call)"],
        ["Extra depreciation, US$bn", "", f"{DDEP27:.1f}", f"{DDEP28:.1f}", "TI: 2.2 to 2.4bn in 2026, rising more slowly in 2027"],
        ["Tax rate", "13%", "13%", "13%", "TI guide for Q3 2026; 13 to 14% for 2026"],
        ["Target multiple", "", "", f"{BASE_PE}x", "Peer median 23.3x; TI 30.5x today"],
    ],
), [27, 9, 9, 9, 46]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Texas Instruments quarterly earnings releases furnished on Form 8-K, 23 April 2024 to 22 July 2026, for '
  'revenue, margins, EPS, depreciation, capital spending, cash flow, CHIPS Act proceeds, debt, cash and the Q3 2026 guide. TI Form '
  '10-K for 2025 (6 February 2026) for revenue by market, the 300mm cost advantage and 2026 capital spending. TI Form 10-Q for Q2 '
  '2026 for Silicon Labs and its financing. SEC XBRL company facts for annual figures, 2019 to 2025. TI earnings calls of 27 January, '
  '22 April and 22 July 2026 for data centre size and growth, end-market growth, depreciation, loadings, fall-through, inventory '
  'days and the free cash flow framework. TI announcements of 4 February 2026 (Silicon Labs), 17 September 2026 (dividend) and '
  '1 October 2026 (results date). Consensus and peer multiples from stockanalysis.com, retrieved 6 October 2026. Share prices from '
  'Yahoo Finance, retrieved 6 October 2026. Data centre quarterly sizes and estimates for 2026 to 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 2 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/ti-feeds-the-chip/">thephysicallayer.fyi/journal/ti-feeds-the-chip</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Texas Instruments. Personal research, not investment advice.</p>')
A('<p class="signoff">Tommy Lau | The Physical Layer | thephysicallayer.fyi</p>')
A('</div>')

html = page_shell("\n".join(P), FOOT, DLONG).replace("</style>", EXTRA_CSS + "</style>")
hp = f"{D}/{SLUG}_note.html"
open(hp, "w", encoding="utf-8").write(html)
render_pdf(hp, PDF)

import pypdfium2 as pdfium
doc = pdfium.PdfDocument(PDF)
print("pages", len(doc))
doc[0].render(scale=2).to_pil().save(PNG)
print("thumb", PNG)
