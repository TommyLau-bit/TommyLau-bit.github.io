# -*- coding: utf-8 -*-
"""Corning (NYSE: GLW) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/corning.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Corning (NYSE: GLW)"
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


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
pb = project(*SCEN[0][1:9]); pu = project(*SCEN[2][1:9])

A('<h1 class="doctitle">Corning Incorporated</h1>')
A('<p class="docsubtitle"><b>NYSE: GLW | Optical fibre, cable and connectivity, plus display, phone, car and solar materials | Corning, New York</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:.2f} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:.2f}, NYSE close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:.2f}"),
    ("Market value", f"About US${MCAP:.0f}bn on {SHARES_OUT * 1000:.0f}m shares; net debt US${NETDEBT:.1f}bn at 30 Jun 2026"),
    ("Core P/E, my estimates", f"{PE26:.1f}x 2026E, {PE27:.1f}x 2027E, {PE28:.1f}x 2028E"),
    ("Consensus", f"Core EPS US${CONS_EPS_26:.2f} 2026, US${CONS_EPS_27:.2f} 2027, US${CONS_EPS_28:.2f} 2028 (Nasdaq.com, Zacks); target US${CONS_TP:.0f} (stockanalysis.com)"),
    ("Dividend", f"US${DPS_Q:.2f} a quarter, yield {DIV_YIELD * 100:.1f}%"),
    ("Optical Communications", f"{OPT_SHARE_25 * 100:.0f}% of 2025 sales; Q2 2026 sales US${Q_OPT[-1] / 1000:.2f}bn, up {OPT_YY[-1] * 100:.0f}%"),
    ("Share sale", f"Up to US${ATM:.0f}bn at the market, filed 11 Sep 2026; about {ATM_DILUTION * 100:.1f}% of shares at today's price"),
    ("Q3 2026 guide (28 Jul)", "Core sales US$4.9 to 5.0bn; core EPS US$0.85 to 0.89"),
    ("Next results", "Q3 2026: Tuesday 27 Oct 2026, 8:30am Eastern"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Corning\'s AI fibre is sold out. At US${PRICE:.0f}, the shares already pay for it to stay that way.</p>')
A(para("Corning makes the glass fibre that carries data between AI chips. On 1 October I argued that this fibre outlives every "
       "chip generation and that Corning is paid each time a campus grows. The claim is holding: optical sales rose "
       f"{OPT_YY[-1] * 100:.0f}% in the second quarter, data centre sales 65%, and the segment's net margin reached a record "
       f"{OPT_NM[-1] * 100:.1f}%."))
A(para(f"The US${ATM:.0f}bn share sale set up in September is not a warning about demand. Being sold out means paying for "
       f"factories first: capital spending rises to about US${CAPEX_GUIDE_26:.0f}bn this year, and customer deposits cover only part. "
       f"The shares are the harder part. At US${PRICE:.2f} they trade at {PE26:.0f} times my 2026 core earnings and need optical "
       f"sales of about US${NEED_OPT28:.0f}bn in 2028, {NEED_OPT28 / OPT_H[-1]:.1f} times 2025."))
A(para(f"<b>My call: {CALL['direction']}, {CALL['conviction'].lower()} conviction.</b> My base case is worth {usd(BASE_VALUE)}, "
       f"{chg(BASE_VALUE)}. The bear case is {usd(bear)} ({chg(bear)}) and the bull case {usd(bull)} ({chg(bull)}). "
       f"I would revisit below about US${REVISIT:.0f}."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (core basis)"))
A(datatable(
    ["US$ billion unless stated", "2023A", "2024A", "2025A", "2026E*", "2027E*", "2028E*"],
    [
        ["Core sales", f"{SALES_H[0]:.2f}", f"{SALES_H[1]:.2f}", f"{SALES_H[2]:.2f}", f"{SALES26:.2f}", f"{S27:.2f}", f"{S28:.2f}"],
        ["Of which Optical Communications", f"{OPT_H[0]:.2f}", f"{OPT_H[1]:.2f}", f"{OPT_H[2]:.2f}", f"{OPT26:.2f}", f"{P['opt27']:.2f}", f"{P['opt28']:.2f}"],
        ["Optical growth (%)", "", f"{(OPT_H[1] / OPT_H[0] - 1) * 100:.0f}", f"{(OPT_H[2] / OPT_H[1] - 1) * 100:.0f}", f"{(OPT26 / OPT_H[2] - 1) * 100:.0f}", f"{B[1] * 100:.0f}", f"{B[2] * 100:.0f}"],
        ["Optical segment net margin (%)", f"{OPT_NI_H[0] / OPT_H[0] * 100:.1f}", f"{OPT_NI_H[1] / OPT_H[1] * 100:.1f}", f"{OPT_NI_H[2] / OPT_H[2] * 100:.1f}", f"{OPT_NI26 / OPT26 * 100:.1f}", f"{B[3] * 100:.1f}", f"{B[4] * 100:.1f}"],
        ["Core net income", f"{CORE_NI_H[0]:.2f}", f"{CORE_NI_H[1]:.2f}", f"{CORE_NI_H[2]:.2f}", f"{NI26:.2f}", f"{P['ni27']:.2f}", f"{P['ni28']:.2f}"],
        ["Core EPS (US$)", f"{EPS_H[0]:.2f}", f"{EPS_H[1]:.2f}", f"{EPS_H[2]:.2f}", f"{EPS26:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}"],
        ["Consensus core EPS (US$)", "", "", "", f"{CONS_EPS_26:.2f}", f"{CONS_EPS_27:.2f}", f"{CONS_EPS_28:.2f}"],
        [f"P/E at US${PRICE:.2f} (x)", f"{PRICE / EPS_H[0]:.1f}", f"{PRICE / EPS_H[1]:.1f}", f"{PRICE / EPS_H[2]:.1f}", f"{PE26:.1f}", f"{PE27:.1f}", f"{PE28:.1f}"],
        ["Capital spending", f"{CAPEX_H[0]:.2f}", f"{CAPEX_H[1]:.2f}", f"{CAPEX_H[2]:.2f}", f"about {CAPEX_GUIDE_26:.1f}", "", ""],
        ["Adjusted free cash flow", f"{FCF_H[0]:.2f}", f"{FCF_H[1]:.2f}", f"{FCF_H[2]:.2f}", "", "", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E to 2028E are my own estimates. All income figures are Corning's core (non-GAAP) measures, which exclude currency "
          "hedge effects and one-off items; Corning guides on this basis. Q2 2026 GAAP EPS was US$0.64 against core US$0.78. 2026E "
          f"uses the reported first half plus my third quarter (core EPS US${Q3E_EPS:.2f}, inside the US$0.85 to 0.89 guide) and fourth "
          f"(US${Q4E_EPS:.2f}). Shares include the US$2bn programme, half sold by the 2027 average. History from Corning releases and Form 10-K."))

A('<div class="keeptogether">')
A(section("Two charts: optical becomes half the company, and a valuation that sits below the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: core sales split into Optical Communications and the rest, with core EPS, 2023A to 2028E; 2023A to 2025A per "
          "Corning, the rest my estimates. Right: value per share from the base case, the probability-weighted cases, the "
          f"sensitivity grid and the bear to bull range, against the US${PRICE:.2f} price (red) and the stockanalysis.com average "
          "analyst target, retrieved 6 October 2026."))
A('</div>')

A(section("The thesis: the plumber who is fully booked"))
A(para("Go back to the pipes in the walls from the October piece. The plumber is fully booked, and three of the biggest builders "
       "in town have paid him in advance to keep a van free. He still has to buy more vans and hire more hands before he can take "
       "more work. The deposits help, but they do not cover the lot. Corning is that plumber."))
A(para(f"<strong>The mechanism is showing up.</strong> Optical sales were US${Q_OPT[-1] / 1000:.2f}bn in the second quarter. "
       f"Enterprise Networks, the data centre side, grew 65% to about US${ENT_Q2_26:.2f}bn, {ENT_SHARE_Q2 * 100:.0f}% of the segment. "
       f"The carrier side was about flat at US${CAR_Q2_26:.2f}bn on my working, so all of the growth came from data centres. "
       f"<strong>The margin is the test.</strong> The claim breaks if the segment margin falls while sales rise. It has risen every "
       f"quarter since early 2024, from {OPT_NM[0] * 100:.1f}% to {OPT_NM[-1] * 100:.1f}%."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_optical.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_margin.png"></div></div>')
A(caption("Left: Optical Communications sales by quarter and growth on a year earlier. Right: segment net income as a share of "
          "segment sales, the claim's falsifier, against my 2028 base case (dashed). Source: Corning quarterly earnings releases, "
          "30 April 2024 to 28 July 2026."))
A('</div>')
A(para("<strong>Customers are paying ahead, and becoming fewer and larger.</strong> Meta agreed in January to buy up to US$6bn of "
       "fibre and cable through 2030; two more hyperscalers signed similar deals by April; Amazon signed in June and Verizon in "
       f"September. Contract liabilities rose from US${CONTRACT_LIAB[0]:.1f}bn to US${CONTRACT_LIAB[1]:.1f}bn in the first half. In "
       f"2025 two end customers bought {TOP2_OPT_25 * 100:.0f}% of optical sales. Long contracts steady volume, but the claim's third "
       "watch item, buyer concentration, is moving the wrong way."))

A(section("Where I was wrong in October"))
A(para(f"In the piece I wrote that Nvidia paid US$500m as part of a partnership for Corning to build more fibre. That is not what "
       "the money bought. The 8-K of 6 May and the Q2 10-Q show Nvidia paid US$500m for a pre-funded warrant, in effect three million Corning "
       f"shares. Corning also gave Nvidia a second warrant, over 15 million shares at US${NV_WARRANT_K:.0f}, for no separate payment. "
       f"The 10-Q values it at US${NV_WARRANT_FV * 1000:.0f}m and treats it as a payment to a customer, which comes off revenue as "
       f"Corning delivers. The same note books a US${DEPOSIT_Q2:.1f}bn customer deposit, to the end of 2029, against that warrant; the "
       "10-Q ties it to the warrant's holder, which the 8-K shows is Nvidia. The deposit, not the US$500m, secures supply. "
       f"Reading the 10-Q note for this initiation changed my view: buyers pay ahead, but the largest is also paid, about "
       f"{NV_WARRANT_PCT * 100:.0f} cents of warrant per dollar of deposit. Scarcity is being shared, not kept. The piece and the "
       "claim stay exactly as published."))

A(section("Why a sold-out business set up a US$2bn share sale"))
A(para(f"On 11 September Corning set up an at-the-market programme with Goldman Sachs for up to US${ATM:.0f}bn of new shares, for "
       f"general corporate purposes. The shares fell {abs(ATM_DROP) * 100:.1f}% on the next trading day. Corning has not said why. Its "
       f"own figures answer it. Capital spending was US${CAPEX_H[-1]:.2f}bn in 2025 and is guided to about US${CAPEX_GUIDE_26:.1f}bn "
       f"in 2026, so the second half spends about US${CAPEX_H2:.2f}bn against US${H1_26_CAPEX:.2f}bn in the first: three new "
       "plants under the Nvidia deal and the Meta and Amazon expansions in North Carolina."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_cash.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: capital spending, adjusted free cash flow (Corning's definition; hatched: net customer deposits and government "
          "incentives) and dividends, 2023 to the first half of 2026 (Corning releases and 10-Q). Right: GLW month-end close, "
          "November 2023 to the 5 October 2026 close, not adjusted for dividends (Yahoo Finance, retrieved 6 October 2026), against "
          "my base value."))
A('</div>')
A(para(f"Adjusted free cash flow was US${H1_26_FCF:.2f}bn in the first half, but US${H1_26_DEP_INFLOW:.2f}bn of it was net "
       f"customer deposits and incentives. Without them it was about US${FCF_H1_EX:.2f}bn, against US${H1_26_DIV:.3f}bn of dividends "
       f"and US${DEBT_DUE_1Y:.2f}bn of debt due within a year. None of this is distress: Corning has US${CASH:.1f}bn of cash, an "
       f"undrawn US$1.5bn credit line, and debt at {LEVERAGE_COV[0] * 100:.0f}% of capital against a {LEVERAGE_COV[1] * 100:.0f}% "
       f"covenant. The full programme is about {ATM_SHARES * 1000:.1f}m shares, {ATM_DILUTION * 100:.1f}% dilution at today's price."))
A(para("<strong>My answer:</strong> the programme is cheap insurance for a spending step-up that customer money only partly "
       f"covers, raised while the shares trade at {PE26:.0f} times earnings. It shows demand is real and that meeting it is "
       "expensive. The 2027 spending plan, not yet given, is the number to watch."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:.2f} Corning is worth about US${MCAP:.0f}bn, {PE26:.1f} times my 2026 core estimate of US${EPS26:.2f} "
       f"(consensus US${CONS_EPS_26:.2f}), {PE27:.1f} times 2027 and {PE28:.1f} times 2028. At the end of 2024 the shares cost "
       f"{PE_HIST:.1f} times the core earnings Corning went on to report for 2025. The market has re-rated a glass company into an "
       "AI supplier."))
A(para(f"<strong class='lead'>What the price needs.</strong> By October 2027 the market will price 2028. At {BASE_PE} times, "
       f"US${PRICE:.2f} needs 2028 core earnings of US${NEED_EPS28:.2f}, above the US${CONS_EPS_28:.2f} consensus. With the rest of "
       f"Corning at my base case, that needs optical sales of about US${NEED_OPT28:.1f}bn at a {B[4] * 100:.0f}% margin: "
       f"{NEED_OPT28 / OPT_H[-1]:.1f} times 2025, and {NEED_OPT_CAGR * 100:.0f}% a year from my 2026 estimate."))
A(para("<strong class='lead'>Where I differ.</strong> Not on the mechanism, but on how much of the next two years the price "
       "already holds. Holding one part at my base and swinging the other from bear to bull, optical moves 2028 earnings by "
       f"{usd(OPT_SWING, 2)} a share and the rest of Corning by {usd(REST_SWING, 2)}. Optical is {OPT_SWING / REST_SWING:.0f} times the "
       f"bigger driver, and passes half of sales in 2028 on my estimates. At {FWD_PE_SA:.0f} times forward earnings Corning trades "
       f"above the fibre and cable makers at {FIBRE_MEDIAN:.1f} times and Amphenol at 29.4 times, though more than half of today's "
       "sales are still display, phone, car and solar glass."))

A(section("Valuation, with the working"))
A(para("I value Corning on core earnings per share twelve months out, so on 2028. Sales are built in two parts, optical and the "
       "rest, each earning a segment net margin, less a corporate line of about US$0.16bn a quarter. I use "
       f"{BASE_PE} times: above the fibre makers' {FIBRE_MEDIAN:.1f} times for Corning's fibre know-how and contracts, below Amphenol's "
       f"29.4 because late-2027 earnings will still be half glass, phones and cars. {BASE_PE} x US${EPS28:.2f} = {usd(BASE_VALUE)}. "
       f"My 2028 sales of US${S28:.1f}bn fall a little short of Corning's plan for a US$30bn run-rate by the end of 2028."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "Fibre loosens: optical grows 22% then 12%, margin 21% then 20%; rest grows 6% then 5%", usd(pb["eps28"], 2),
         f"{SCEN[0][9]}x", usd(bear), chg(bear), "25%"],
        ["Base", "Optical grows 35% then 25%, margin 23% then 24%; rest grows 9% then 8%", usd(EPS28, 2), f"{BASE_PE}x",
         usd(base), chg(base), "50%"],
        ["Bull", "New plants fill early: optical grows 45% then 32%, margin 24% then 25.5%; rest 12% then 10%", usd(pu["eps28"], 2),
         f"{SCEN[2][9]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [10, 40, 11, 9, 11, 11, 8]))
A(caption(f"All cases start from my 2026E (optical US${OPT26:.2f}bn, rest US${REST26:.2f}bn). The bear case is not a collapse in "
          f"demand: optical still grows by more than a third over two years, to US${pb['opt28']:.1f}bn. Prices and margins slip as new "
          "fibre capacity, Corning's and China's, catches up, and the multiple falls towards the fibre makers'."))
A('</div>')
grid = [[e * m for m in SENS_PE] for e in SENS_EPS]
above = sum(v > PRICE for r in grid for v in r)
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 core EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["2028 EPS"] + [f"{m}x" for m in SENS_PE],
    [[usd(e, 2)] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (e, r) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"Only {above} of the nine cells sit above today's price. Each needs earnings above my base, a multiple above "
       f"{BASE_PE} times, or both. Every figure is live in the accompanying model, so a change to growth, margin, dilution or the multiple "
       "moves the value."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [[c, t, f"{p:.1f}x", w] for c, t, p, w in PEERS],
    num_cols={2},
), [22, 14, 12, 52]))
A(caption("Forward P/E from stockanalysis.com, retrieved 6 October 2026; Prysmian, Fujikura and Sumitomo Electric on their local "
          f"listings. Corning at {FWD_PE_SA:.1f} times is priced with the makers of the plugs (Coherent, Ciena, Lumentum), not the "
          "makers of the pipes. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["27 Oct 2026, 8:30am Eastern", "Q3 2026 results and call", "Optical sales and segment margin; Enterprise growth; Q4 guide; first word on 2027 capital spending"],
        ["Early Nov 2026", "Q3 2026 Form 10-Q", "Any shares sold under the US$2bn programme; contract liabilities and deposits"],
        ["Late Jan 2027", "Q4 2026 results", "The US$20bn run-rate; 2027 capital spending; optical at US$2.4bn a quarter"],
        ["Feb 2027", "Form 10-K for 2026", "Customer concentration in optical, against 28% for two customers in 2025"],
        ["2027", "Samsung Display lock-up ends", "58m shares free to sell; 22m more can be offered to Corning in tranches"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The upturn runs longer.</strong> The bull case and the main risk to a no call. Corning says it could sell more if "
       "it could make more. If the new plants come on early and the margin rises towards 25%, 2028 earnings beat my base and the "
       "multiple holds. <strong>Fibre loosens.</strong> The bear case and the claim's own falsifier. Corning, Fujikura, Prysmian and "
       "Chinese producers are all expanding; a margin falling while sales rise would be the first sign."))
A(para("<strong>Buyers take a bigger share.</strong> The Nvidia warrant shows the largest buyers can take part of the scarcity "
       f"rent. <strong>More shares.</strong> The programme is about {ATM_DILUTION * 100:.1f}% dilution; Samsung Display's "
       f"{SDC_LOCKED * 1000:.0f}m locked shares free up in 2027; the Nvidia warrant adds 15m shares above US$180. "
       "<strong>The rest of Corning.</strong> Display, phone glass and solar are more than half of sales. Corning cited higher "
       "memory prices as a headwind for glass in July, and the solar ramp had a costly shutdown in the second quarter."))

A('<div class="keeptogether">')
A(section("What would change our mind"))
A(para(f"<strong>Into a call:</strong> a price below about US${REVISIT:.0f}, which would put my base case 15% above it; or fourth "
       "quarter results showing optical sales of US$2.4bn or more in the quarter at a segment margin of 23% or more, with the share "
       "sale largely unused. A falling optical margin before mid-2027 would bring the bear case forward."))
A(para("<strong>The call is wrong if</strong> Optical Communications sales reach US$11.5bn or more in 2027 with a segment net "
       "margin of 24% or more, or the shares close above US$200 or below US$110 by October 2027."))
A('</div>')

A(section("Conclusion"))
A(para("The October piece argued that glass fibre is the part of the AI network that outlives every chip, and that Corning is "
       f"paid each time a campus grows. Corning's own numbers back it: optical up {OPT_YY[-1] * 100:.0f}%, data centre up 65%, and a "
       f"record {OPT_NM[-1] * 100:.0f}% segment margin. The share sale does not undercut the claim; it shows that being sold out "
       f"costs money before it makes any. The shares are the harder part: at US${PRICE:.2f} they price optical sales of about "
       f"US${NEED_OPT28:.0f}bn in 2028. My call: {CALL['direction']}, {CALL['conviction'].lower()} conviction, base value "
       f"{usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}. Revisit below about US${REVISIT:.0f}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Optical growth", f"{(OPT26 / OPT_H[-1] - 1) * 100:.0f}%", f"{B[1] * 100:.0f}%", f"{B[2] * 100:.0f}%", f"H2 2026 US${Q3E_OPT} and {Q4E_OPT}bn, mine"],
        ["Optical segment net margin", f"{OPT_NI26 / OPT26 * 100:.1f}%", f"{B[3] * 100:.1f}%", f"{B[4] * 100:.1f}%", "Q2 2026: 21.1%; scale and contracts"],
        ["Rest of Corning growth", f"{(REST26 / (SALES_H[-1] - OPT_H[-1]) - 1) * 100:.0f}%", f"{B[5] * 100:.0f}%", f"{B[6] * 100:.0f}%", "Solar ramp; display and auto flat to low growth"],
        ["Rest segment net margin", f"{REST_M_26 * 100:.1f}% (H2)", f"{B[7] * 100:.1f}%", f"{B[8] * 100:.1f}%", f"H1 2026: {REST_M_H1 * 100:.1f}%; Solar improving from Q3"],
        ["Corporate line, US$bn", f"({-(CORP_H1 + 2 * CORP_Q):.2f})", f"({-CORP27:.2f})", f"({-CORP28:.2f})", "Core net income less segment net income"],
        ["Diluted shares, m", f"{DILUTED * 1000:.0f}", f"{SH27 * 1000:.0f}", f"{SH28 * 1000:.0f}", "Q2 2026 diluted plus the US$2bn programme"],
        ["Target multiple", "", "", f"{BASE_PE}x", f"Fibre makers {FIBRE_MEDIAN:.1f}x; Amphenol 29.4x; GLW {FWD_PE_SA:.1f}x"],
    ],
), [27, 11, 9, 9, 44]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Corning quarterly earnings releases furnished on Form 8-K, 30 April 2024 to 28 July 2026, for core '
  'sales, core EPS, segment sales and net income, margins, cash flow, capital spending and the Q3 2026 guide. Corning Form 10-K for '
  '2025 (12 February 2026) for segment and product-line sales, customer concentration and the Samsung Display share agreement. '
  'Corning Form 10-Q for Q2 2026 (29 July 2026) for the customer deposit, warrant accounting, contract liabilities, liquidity and the '
  '2026 capital spending outlook. Corning 8-K and press release of 6 May 2026 (Nvidia partnership and warrants). Corning 8-K and '
  'prospectus supplement of 11 September 2026 (at-the-market programme). Corning Q2 2026 earnings call, 28 July 2026. Meta, Amazon '
  'and Verizon announcements of 27 January, 8 June and 8 September 2026. Corning investor relations events page (results date). '
  'Consensus EPS from Nasdaq.com (Zacks); multiples and average target from stockanalysis.com; share prices from Yahoo Finance; all '
  'retrieved 6 October 2026. Estimates for 2026 to 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 1 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/corning-lays-the-glass/">thephysicallayer.fyi/journal/corning-lays-the-glass</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Corning. Personal research, not investment advice.</p>')
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
