# -*- coding: utf-8 -*-
"""TSMC (NYSE: TSM; TWSE: 2330) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/tsmc.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "TSMC (NYSE: TSM)"
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

A('<h1 class="doctitle">Taiwan Semiconductor Manufacturing Co (TSMC)</h1>')
A('<p class="docsubtitle"><b>NYSE: TSM (ADR, 1 ADR = 5 shares) | TWSE: 2330 | Foundry and advanced packaging for AI chips | Taiwan</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:.2f} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price, ADR", f"US${PRICE:.2f}, NYSE close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:.2f}"),
    ("Last price, Taipei", f"NT${TW_PRICE:,.0f}, TWSE close 6 Oct 2026 (2330.TW)"),
    ("ADR premium to Taipei", f"{ADR_PREMIUM * 100:.0f}% at NT${FX:.2f} per US$ (5 shares per ADR)"),
    ("Market value", f"US${MCAP_ADR / 1000:.2f}tn at the ADR price, US${MCAP_TW / 1000:.2f}tn at Taipei's; {SHARES * 1000:,.0f}m shares, 30 Jun 2026"),
    ("Net cash, 30 Jun 2026", f"About US${NETCASH:.0f}bn (cash and securities NT${CASH_NT:,.0f}bn less long-term debt NT${LTDEBT_NT:,.0f}bn)"),
    ("P/E on my estimates", f"{PRICE / EPS26:.1f}x 2026E, {PRICE / EPS27:.1f}x 2027E, {PRICE / EPS28:.1f}x 2028E"),
    ("Consensus", f"2027 EPS US${CONS_27_ADR:.2f} per ADR (MarketBeat); forward P/E {FWD_PE_SA:.1f}x, target US${CONS_TP:.0f} (stockanalysis.com)"),
    ("Q3 2026 guide (16 Jul)", "Revenue US$44.6 to 45.8bn; gross margin 65 to 67%; operating margin 56 to 58%, at NT$32"),
    ("Next results", "Q3 2026: Thursday 15 Oct 2026, 2pm Taiwan time"),
]))
A('</div><div class="maincol">')
A('<p class="lede">TSMC is the bottleneck today. At US$486, the ADR already pays for it still being one in 2028.</p>')
A(para("TSMC makes almost every advanced AI chip. Its ADR closed at US$485.80 on 5 October 2026, up 74% in a year and within "
       "two dollars of its 52-week high. On 2 October I argued that, on today's horizon, TSMC's factories bind before the grid "
       "does, and that over the longer run the grid is still the slower clock."))
A(para("The near horizon is holding. TSMC shipped 17% more wafers in the second quarter and earned about 17% more on each, at a "
       "67.7% gross margin, almost twelve points above its own through-the-cycle floor. July and August revenue put the third quarter on "
       "course to beat the top of the guide. The price knows it: at 20 times, it needs a 2028 operating margin of about 58%, "
       "the scarcity margin, just as the new fabs land."))
A(para(f"<b>My call: {CALL['direction']}, {CALL['conviction'].lower()} conviction.</b> My base case, close to TSMC's own "
       f"five-year plan, is worth {usd(BASE_VALUE)}, {chg(BASE_VALUE)}. The bear case, in which the grid becomes the slower clock, "
       f"is {usd(bear)} ({chg(bear)}), against a bull case of {usd(bull)} ({chg(bull)}). I would revisit below about US$400."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials"))
A(datatable(
    ["US$ billion unless stated", "2024A", "2025A", "2026E*", "2027E*", "2028E*"],
    [
        ["Revenue", "90.08", "122.42", f"{REV26:.2f}", f"{R27:.2f}", f"{R28:.2f}"],
        ["Revenue growth (%)", "n.a.", "36", f"{(REV26 / 122.42 - 1) * 100:.0f}", f"{G27 * 100:.0f}", f"{G28 * 100:.0f}"],
        ["Gross margin (%)", "56.1", "59.9", "n.m.", "n.m.", "n.m."],
        ["Operating margin (%)", "45.7", "50.8", f"{OM26 * 100:.1f}", f"{OM27 * 100:.1f}", f"{OM28 * 100:.1f}"],
        ["EPS per ordinary share (NT$)", "45.25", "66.25", "", "", ""],
        ["EPS per ADR (US$)", "7.04", "10.65", f"{EPS26:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}"],
        [f"P/E at US${PRICE:.2f} (x)", f"{PRICE / 7.04:.1f}", f"{PRICE / 10.65:.1f}", f"{PRICE / EPS26:.1f}", f"{PRICE / EPS27:.1f}", f"{PRICE / EPS28:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*2026E to 2028E are my own estimates. 2026E uses the reported first half (US$7.80 per ADR) plus my third and fourth "
          f"quarters (revenue US${Q3E_REV} and {Q4E_REV}bn; operating margin {Q3E_OM * 100:.0f}% and {Q4E_OM * 100:.0f}%). EPS = revenue x "
          f"(operating margin + {NONOP * 100:.1f}% non-operating) x (1 - {TAX * 100:.0f}% tax and minorities) x 5 / 25.932bn shares. "
          "I model operating, not gross, margin ahead (n.m.). 2024A and 2025A from TSMC's 4Q25 presentation; per-ADR EPS summed from "
          f"quarterly releases. My 2027E sits {abs(EPS27 / CONS_27_ADR - 1) * 100:.0f}% below the MarketBeat consensus of US${CONS_27_ADR}."))

A('<div class="keeptogether">')
A(section("Two charts: the margin path I expect, and a valuation that brackets the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and operating margin, 2024A to 2028E; 2024A and 2025A per TSMC, the rest my estimates. Right: value per ADR "
          "from the base case, the probability-weighted cases, the sensitivity grid and the bear to bull range, against the US$485.80 "
          "price (red) and the stockanalysis.com average analyst target, retrieved 6 October 2026."))
A('</div>')

A(section("The thesis: a kitchen with a queue cooks more and charges more"))
A(para("Go back to the shared kitchen from the October piece. Every famous restaurant designs its own dishes, and all of them send "
       "the cooking to one kitchen. When demand surges, the queue at that kitchen sets how fast every restaurant grows. A kitchen "
       "with a queue does two things: it cooks more meals, and it charges more for each one. TSMC is doing both."))
A(para("<strong>More wafers.</strong> TSMC shipped 4.34 million twelve-inch-equivalent wafers in the second quarter of 2026, 17% "
       "more than a year earlier, from fabs that were already full. <strong>More per wafer.</strong> Revenue in Taiwan dollars rose "
       "36%, so revenue per wafer rose about 17% too, part mix towards the newest processes and part price. <strong>More of each "
       "sale kept.</strong> Gross margin reached 67.7%, against 53.1% two years earlier and TSMC's own target of 56% and higher "
       "through the cycle."))
A(para("<strong>Where the pull comes from.</strong> High-performance computing, which holds AI accelerators, was 66% of revenue in "
       "the second quarter, against 46% at the start of 2024. AI accelerators alone were in the high teens as a share of 2025 "
       "revenue, and TSMC expects them to grow at a mid to high 50s per cent rate a year from 2024 to 2029. <strong>The packaging "
       "pinch.</strong> In July C.C. Wei said TSMC's packaging capacity is so tight that it is limiting customers' growth. That is "
       "the near horizon of the claim in the company's own words."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_qgm.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_hpc.png"></div></div>')
A(caption("Left: gross margin by quarter, Q1 2024 to Q2 2026, against TSMC's through-the-cycle floor of 56% (dashed). Right: "
          "high-performance computing as a share of revenue. Source: TSMC quarterly results releases and presentations, "
          "18 April 2024 to 16 July 2026; long-term margin from the 4Q25 presentation, 15 January 2026."))
A('</div>')
A(para("<strong>The newest evidence.</strong> TSMC publishes revenue monthly, and the third quarter is two thirds reported. July and "
       "August came to NT$982.4bn. At TSMC's assumed NT$32 per US$, the US$44.6 to 45.8bn guide needs only NT$445 to 483bn in "
       "September; August alone was NT$514.8bn. Unless September falls sharply, the quarter lands at or above the top of the guide."))

A(section("Where I was wrong in October"))
A(para("In the piece I wrote that TSMC raised its 2026 capital budget to US$60 to 64bn, and that Wei said that money adds almost "
       "nothing to output this year. The timing was wrong. Wei made that remark on 15 January, about the original budget of US$52 "
       "to 56bn; the raise came on 16 July. Rereading the two transcripts side by side for this note showed the slip. The point "
       "stands, and the larger budget makes it stronger: spending decided in 2026 buys supply for 2028 and 2029. The piece and the "
       "claim stay exactly as published, so the record shows the slip."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US$485.80 the ADR values TSMC at about US${MCAP_ADR / 1000:.2f}tn, with roughly US${NETCASH:.0f}bn of net cash. That is "
       f"{PRICE / EPS26:.1f} times my 2026 estimate of US${EPS26:.2f} per ADR and {PRICE / EPS27:.1f} times my 2027 estimate of "
       f"US${EPS27:.2f}; on MarketBeat's 2027 consensus of US${CONS_27_ADR} it is {PRICE / CONS_27_ADR:.1f} times. The ADR also "
       f"trades at about {ADR_PREMIUM * 100:.0f}% above five Taipei shares, which closed at NT${TW_PRICE:,.0f} on 6 October."))
A(para(f"<strong class='lead'>What the price needs.</strong> By October 2027 the market will price 2028. At 20 times, close to "
       f"TSMC's forward multiple today, US$485.80 needs 2028 earnings of US${NEED_EPS28:.2f} per ADR. On my 2028 revenue of "
       f"US${R28:.0f}bn, that needs an operating margin of about {NEED_OM28 * 100:.0f}%, against my {OM26 * 100:.1f}% for 2026. The "
       "market is paying for today's scarcity margin to last into 2028, the year the October piece named as the test of the "
       "longer horizon, when the US$60 to 64bn of 2026 spending starts producing wafers."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_monthly.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: monthly revenue, January 2025 to August 2026, against the monthly pace of the Q3 guide midpoint at NT$32 per US$ "
          "(TSMC monthly revenue reports on Form 6-K). Right: TSM ADR month-end close, November 2023 to the 5 October 2026 close, "
          "not adjusted for dividends (Yahoo Finance, retrieved 6 October 2026), against my base value."))
A('</div>')
A(para("<strong class='lead'>Where I differ.</strong> I agree on the near horizon. I differ on what happens when the new capacity "
       "lands, because three physical things push margin down in 2028 whatever demand does. <strong>Depreciation:</strong> capital "
       "spending rose from NT$956bn in 2024 to NT$1,272bn in 2025, and the first half of 2026 alone was NT$847bn; that charge "
       "arrives with the output. <strong>Distance from the cluster:</strong> TSMC guides that overseas fabs cut gross margin by two "
       "to three points at first, widening to three to four, and Arizona's second fab is due in volume in the second half of 2027. "
       "<strong>The newest process:</strong> TSMC expects the 2 nanometre ramp to cut gross margin by about three to four points in "
       "the second half of 2026."))
A(para("TSMC has offset all of this with price, which works only while customers queue. That is where the longer horizon comes in. "
       "If the grid is the slower clock, the capacity arriving in 2028 meets customers whose data centres are waiting for power: the "
       "queue shortens just as the kitchen gets bigger. TSMC's own plan points the same way. Revenue growth approaching 25% a year "
       "from 2024 to 2029 implies about US$275bn in 2029; with 2026 near US$172bn, that leaves about 17% a year for 2027 to 2029. "
       "My base case follows that plan, not a bust."))

A(section("Valuation, with the working"))
A(para("I value TSMC on earnings per ADR, because it sells mostly in US dollars, carries net cash and pays a steady, rising "
       "dividend (NT$24 a share in 2026). The horizon is twelve months, to October 2027, so the year I value is 2028. Non-operating "
       "items jumped to NT$95.8bn in the second quarter from NT$28.8bn in the first, the quarter TSMC sold part of its stake in "
       "Vanguard International. I treat the jump as non-recurring: on my working it added about US$0.34 to second quarter EPS per "
       "ADR. Ahead, non-operating income is 2.5% of revenue, its first quarter level."))
A(para(f"<strong class='lead'>The multiple.</strong> I use 20 times 2028 earnings for the base case. That is TSMC's own forward "
       f"multiple today ({FWD_PE_SA:.1f}x), below the 22 to 24 times of GlobalFoundries and UMC, and it assumes no rerating either "
       f"way. 20 x US${EPS28:.2f} = {usd(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "The grid binds first: growth 15% then 5%; operating margin 55% in 2027, 50% in 2028",
         usd(project(*SCEN[0][1:5])[3], 2), "16x", usd(bear), chg(bear), "25%"],
        ["Base", "TSMC's own plan: growth 24% then 18%; margin 57% then 55.5%", usd(EPS28, 2), "20x", usd(base), chg(base), "50%"],
        ["Bull", "The factory stays the bottleneck: growth 30% then 25%; margin holds at 59%",
         usd(project(*SCEN[2][1:5])[3], 2), "24x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [10, 40, 11, 9, 11, 11, 8]))
A(caption("All cases start from my 2026E revenue of US$171.5bn and use the same earnings bridge. Values are per ADR, unrounded in "
          "the model. The downside in the bear case is larger than the upside in the bull case."))
A('</div>')
grid = [[e * m for m in SENS_PE] for e in SENS_EPS]
above = sum(v > PRICE for r in grid for v in r)
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["2028 EPS per ADR"] + [f"{m}x" for m in SENS_PE],
    [[usd(e, 2)] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (e, r) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"Only {above} of the nine cells sit above today's price. To make money from here, TSMC needs both bull-case earnings and a "
       "multiple at least as high as today's. Every figure is live in the accompanying model, so a change to growth, margin or the "
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
A(caption("Forward P/E from stockanalysis.com, retrieved 6 October 2026. Intel's and Samsung's multiples are distorted by recovery "
          "and memory cycles. Nvidia is TSMC's largest AI customer, shown for context. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Around 10 Oct 2026 (date not confirmed)", "September 2026 revenue", "Whether Q3 lands above the US$45.8bn top of the guide"],
        ["15 Oct 2026, 2pm Taiwan time", "Q3 2026 results and call", "Gross margin against 65 to 67% with the 2nm ramp; Q4 guide; whether packaging is still called tight; any 2027 capex signal"],
        ["January 2027", "Q4 2026 results", "2027 capital budget and revenue outlook; any change to the 56% through-the-cycle margin floor"],
        ["Second half of 2027", "Arizona second fab in volume", "Overseas margin dilution moving from 2 to 3 points towards 3 to 4"],
        ["Monthly", "Revenue reports", "High-performance computing share and the run-rate against each guide"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The factory stays the bottleneck for longer.</strong> The bull case and the main risk to a no call. If AI demand "
       "outruns the new fabs into 2028 and the grid keeps up, the scarcity margin survives. A raised margin floor would be the "
       "clearest sign."))
A(para("<strong>The grid binds first, and sooner.</strong> The bear case: TSMC's tightness eases while data centres with chips on "
       "order still wait for power, which is the near horizon of my claim breaking. Watch for packaging called balanced, or "
       "high-performance computing slipping as a share of revenue."))
A(para("<strong>The exchange rate and the ADR premium.</strong> TSMC reports in Taiwan dollars, sells mostly in US dollars and "
       "guides margin at a set rate. A stronger Taiwan dollar lowers margin and earnings per ADR, and the ADR's 19% premium to the "
       "Taipei shares can narrow even if the business does well."))
A(para("<strong>Taiwan's electricity.</strong> In January Wei said his first worry on power was Taiwan's own supply. A fab is a "
       "building waiting on power too. <strong>Rival foundries.</strong> Intel Foundry and Samsung Foundry want TSMC's AI customers. "
       "I found no sign of a large AI accelerator moving away, but packaging is where a second source is easiest."))

A('<div class="keeptogether">')
A(section("What would change our mind"))
A(para("<strong>Into a call:</strong> a price below about US$400, which would put my base case about 16% above it; or third quarter "
       "results showing gross margin at or above the 67% top of the guide despite the 2 nanometre ramp; or TSMC raising its "
       "through-the-cycle margin floor above 56%."))
A(para("<strong>The call is wrong if</strong> full year 2027 revenue grows 30% or more in US dollars with an operating margin of 58% "
       "or more, or TSMC raises its through-the-cycle gross margin floor above 56%, or the ADR trades above US$560 by October 2027 "
       "without either."))
A('</div>')

A(section("Conclusion"))
A(para("The October piece argued that, today, TSMC's factories bind before the grid does. A quarter of TSMC's own numbers says that "
       "is right: more wafers, more per wafer, and a margin almost twelve points above its own floor. The shares know it. At US$485.80 the "
       "ADR needs the scarcity margin to survive into 2028, when new capacity lands and the longer horizon of my claim begins to be "
       f"tested. My call: {CALL['direction']}, {CALL['conviction']} conviction. Revisit below about US$400."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Revenue growth, US$", "40%", "24%", "18%", "2026 on TSMC's guide and monthly revenue; then TSMC's 2024 to 2029 plan"],
        ["Operating margin", f"{OM26 * 100:.1f}%", "57.0%", "55.5%", "H2 2026 guide 56 to 58%; then depreciation, overseas and 2nm dilution"],
        ["Non-operating income, % of revenue", "2.5%", "2.5%", "2.5%", "Q1 2026 level; Q2 2026 jump excluded"],
        ["Tax and minorities, % of pre-tax", "17%", "17%", "17%", "2025: 15.9%; first half 2026: 17.5%"],
        ["Target multiple", "", "", "20x", "TSMC's forward P/E today"],
    ],
), [27, 9, 9, 9, 46]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">TSMC quarterly results releases and presentations furnished on Form 6-K, 18 April 2024 to 16 July 2026, for '
  'revenue, margins, EPS per share and per ADR, technology and platform mix, wafer shipments, non-operating items, cash, debt, share '
  'count, capital expenditures and the Q3 2026 guide. TSMC 4Q25 presentation, 15 January 2026, for 2024 and 2025 annual figures and '
  'its 2024 to 2029 targets. TSMC monthly revenue reports on Form 6-K, 10 February 2025 to 10 September 2026. TSMC earnings call '
  'transcripts of 15 January and 16 July 2026. TSMC Form 6-K of 15 May 2026 on the Vanguard International share sale. TSMC investor '
  'relations for the 15 October 2026 results date. Consensus from MarketBeat and stockanalysis.com, and peer multiples from '
  'stockanalysis.com, retrieved 6 October 2026. ADR, Taipei share and exchange rate prices from Yahoo Finance, retrieved 6 October '
  '2026. Estimates for 2026 to 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 2 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/tsmc-says-it-is-the-bottleneck/">thephysicallayer.fyi/journal/tsmc-says-it-is-the-bottleneck</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in TSMC. Personal research, not investment advice.</p>')
A('<p class="signoff">Tommy Lau | The Physical Layer | thephysicallayer.fyi</p>')
A('</div>')

html = page_shell("\n".join(P), FOOT, DLONG).replace("</style>", EXTRA_CSS + "</style>")
hp = f"{D}/tsmc_note.html"
open(hp, "w", encoding="utf-8").write(html)
render_pdf(hp, PDF)

import pypdfium2 as pdfium
doc = pdfium.PdfDocument(PDF)
print("pages", len(doc))
doc[0].render(scale=2).to_pil().save(PNG)
print("thumb", PNG)
