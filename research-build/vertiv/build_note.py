# -*- coding: utf-8 -*-
"""Vertiv (NYSE: VRT) initiation note, 6 Oct 2026. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
All analysis and figures are from src/content/calls/vertiv.md; derived arithmetic is marked.
"""
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Vertiv (NYSE: VRT)"
DATE = "6 October 2026"
mv = SHARES_DIL * PRICE / 1000
nc = CASH + ST_INV - DEBT
ev = mv - nc / 1000

EXTRA_CSS = """
a { color: #1F3864; text-decoration: none; }
.chartsrow { break-inside: avoid; margin-top: 2px; }
.keeptogether { break-inside: avoid; }
table.datatable.compact td { padding: 2.6px 7px; font-size: 8.5pt; }
table.datatable.compact th { padding: 4px 7px; font-size: 8.5pt; }
p.lede { font-size: 10.4pt; font-weight: 700; color: #1F3864; margin: 0 0 6px 0; line-height: 1.28; }
.pb { break-before: page; }
"""

P = []
A = P.append


def cols(html, widths):
    """Fix column widths on a datatable (percentages)."""
    cg = "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in widths) + "</colgroup>"
    i = html.index(">") + 1
    return html[:i].replace('class="datatable', 'style="table-layout:fixed" class="compact datatable') + cg + html[i:]


def r2(x):
    return f"{x + 1e-9:.2f}"

A('<h1 class="doctitle">Vertiv Holdings Co</h1>')
A('<p class="docsubtitle"><b>NYSE: VRT | Power, thermal and liquid cooling infrastructure for AI data centres | United States</b></p>')
A('<p class="docmeta">Tommy Lau | 6 October 2026 | Initiation of coverage | Independent research</p>')
A(rating_banner("INITIATE AT LONG", "US$300.00", "US$253.62 (NYSE close, 5 Oct 2026)", "+18%"))

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", "US$253.62, NYSE close 5 Oct 2026"),
    ("Peak", "US$379.94 intraday, 14 May 2026; price now 33% below"),
    ("Diluted shares", "392.7m, Q2 2026 weighted average (10-Q)"),
    ("Market value", f"US${mv:.1f}bn"),
    ("Net cash, 30 Jun 2026", f"US${nc:.1f}m (cash US$2,810.6m + short-term investments US$300.0m less debt US$2,939.8m)"),
    ("Enterprise value", f"US${ev:.1f}bn"),
    ("P/E, 2026 guide midpoint", "37.9x (US$6.70)"),
    ("P/E, 2027 consensus", "28.4x (US$8.93, MarketBeat)"),
    ("Forward P/E, stockanalysis.com", "32.1x"),
    ("2026 guide (29 Jul 2026)", "Sales US$13.8 to 14.2bn; adj. operating margin 23.3 to 24.3%; adj. EPS US$6.65 to 6.75"),
    ("Conviction and horizon", "Medium; 12 months, to October 2027"),
    ("Year end", "31 December"),
]))
A('</div><div class="maincol">')
A('<p class="lede">The market has sold Vertiv as a volume story. Its margin says each megawatt is worth more.</p>')
A(para("Vertiv makes the power and cooling equipment inside AI data centres. Its shares closed at US$253.62 on 5 October 2026, "
       "a third below their May peak, in a year when Vertiv twice raised its own guidance and widened its margin by four points. "
       "The market fears AI data centre spending is near its peak, that supply is congested and that the backlog has gone quiet."))
A(para("My answer comes from the claim I made in September: Vertiv is paid per megawatt, and AI has made every megawatt harder to build. "
       "The number to watch is not how many megawatts get built but how much Vertiv earns on each one. That number is still rising, "
       "and the shares no longer pay for it."))
A(para("<b>We initiate at LONG with a twelve-month target of US$300</b>, 28 times my 2028 earnings estimate of US$10.65 and 18% above "
       "the price. Conviction is Medium, not High, because the bear case is a 29% fall and the third quarter results land within weeks."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials"))
A(datatable(
    ["US$ billion unless stated", "2024A", "2025A", "2026 guide", "2027E*", "2028E*"],
    [
        ["Net sales", "8.01", "10.23", "13.8 to 14.2", f"{S27:.2f}", f"{S28:.2f}"],
        ["Net sales growth (%)", "n.a.", "28", "37", "21", "20"],
        ["Adjusted operating margin (%)", "19.4", "20.4", "23.8", "25.0", "26.0"],
        ["Adjusted operating profit", "1.55&dagger;", "2.09&dagger;", "3.33", r2(S27*M27), r2(S28*M28)],
        ["Adjusted EPS (US$)", "2.85", "4.20", "6.65 to 6.75", f"{E27:.2f}", f"{E28:.2f}"],
        ["Adjusted EPS growth (%)&dagger;", "n.a.", "47", "60", "27", "25"],
        ["P/E at US$253.62 (x)", "", "", "37.9", "29.7", "23.8"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*2027E and 2028E are my own estimates, not Vertiv's. 2024A and 2025A sales and margins are the sums of the four quarterly results releases; EPS is as reported for the full year. "
          "2026 is Vertiv's guide of 29 July 2026; growth, margin, operating profit and P/E use the midpoints. &dagger;Derived: operating "
          "profit as sales x margin; EPS growth from the figures shown. My 2027E EPS sits about 4.5% below the US$8.93 consensus."))

A('<div class="keeptogether">')
A(section("Two charts: a margin still rising, and a valuation that sits above the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: net sales and adjusted operating margin, 2024A to 2028E. 2024A and 2025A per Vertiv's results releases; 2026 is the guide "
          "midpoint; 2027E and 2028E are my estimates. Right: value per share from the base case, the probability-weighted cases, the "
          "sensitivity grid and the bear to bull range, against the US$300 target (red) and the US$253.62 price (grey)."))
A('</div>')

A(section("The thesis: each megawatt holds more of what Vertiv makes"))
A(para("Think of the electrician from the September piece. For years every new house needed the same fuse box. Now each house wants a "
       "heat pump, an induction hob and a car charger, so the job inside every house has grown. The electrician gains twice: more houses, "
       "and a bigger job in each."))
A(para("Vertiv is that electrician inside an AI data centre. An AI cabinet draws more than 130 kilowatts, against 5 to 12 kW for an "
       "ordinary server rack. Air cannot carry that heat away, so the heat leaves through liquid, which needs coolant distribution units, "
       "pipework and heat exchangers on every row. The power side is moving to 800 volts of direct current, which needs new conversion "
       "equipment. Each megawatt of AI capacity holds more of what Vertiv makes, and more complicated versions of it."))
A(para("The money should show this in one place above all: margin. Adjusted operating margin is the share of each sale left after running "
       "costs, with one-off items stripped out. If Vertiv were only selling more of the same boxes into a boom, margin would drift with "
       "volume and then fall as rivals added capacity. If each megawatt holds richer equipment, margin should keep rising while sales grow."))
A(para("It has. Every quarter since the third quarter of 2025 has beaten the same quarter a year earlier, by 1.7 to 4.3 points, while "
       "sales kept rising. The second quarter of 2026 reached 22.6%, up 4.1 points, on sales of US$3.27 billion. Vertiv now guides to "
       "23.3 to 24.3% for the full year, and to 24 to 25% for the third quarter. At its investor conference in May it set a target of "
       "about 27% or more by 2030."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_qmargin.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_mix.png"></div></div>')
A(caption("Left: adjusted operating margin by quarter, Q1 2024 to Q2 2026; dark bars are the four quarters that beat the same quarter a "
          "year earlier. The first quarter is always the softest. Right: organic growth, products against service and spares; stripped of "
          "acquisitions and currency, service grew more slowly than products in nine of these ten quarters. Source: Vertiv quarterly "
          "results releases, 24 April 2024 to 29 July 2026, including the organic growth reconciliation tables."))
A('</div>')

A(section("Where I was wrong in September"))
A(para("In the piece I wrote that service revenue grew 33% against 22% for products, and called service outgrowing hardware evidence for "
       "the claim. That was wrong. Those were reported figures, swollen by acquisitions. Stripped of acquisitions and currency, service "
       "grew about 10% and products about 20%, and service has grown more slowly than products in nine of the last ten quarters."))
A(para("What changed my view was working through the organic split in Vertiv's own reconciliation tables for this pitch, which I had not "
       "done for the piece. The claim itself, that what Vertiv sells per megawatt is rising, survives on margin, which is the stronger "
       "test anyway. This call rests on margin and not on service. The piece and the claim stay exactly as published, so the record "
       "shows the mistake."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US$253.62 Vertiv is valued at about US${mv:.1f} billion on its diluted shares, and holds roughly US$170 million more cash "
       "than debt. That is 37.9 times the midpoint of its own 2026 earnings guide, and 28.4 times the 2027 consensus of US$8.93 a share "
       "(MarketBeat, 6 October). That multiple has fallen fast. At the May peak the shares traded at about 60 times the 2026 guide of the "
       "time, US$6.30 to 6.40 a share. Today the gap to the large electrical groups is small: Eaton, nVent and Trane each trade at about "
       "28.5 to 29 times forward earnings, and Schneider Electric at 24 (stockanalysis.com, 6 October). The market now prices Vertiv close "
       "to a diversified industrial whose data centre exposure is one division among many. Three things moved the price."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["11 Feb 2026", "Vertiv stops reporting orders and backlog each quarter; backlog now annual only", "n.a."],
        ["14 May 2026", "Intraday peak of US$379.94; about 60x the 2026 guide of the time", "Peak"],
        ["29 Jul 2026", "Q2 sales about 3% below consensus, EPS beats; timing and supply congestion blamed", "down 17% that day"],
        ["1 Sep 2026", "Agrees to buy UtilityInnovation Group for about US$1.45bn in cash, little financial detail", "n.a."],
        ["9 Sep 2026", "Day after the CEO cites congestion in the supply chain for complex products; sector sell-off", "down 9.6%"],
    ],
), [22, 56, 22]))
A('</div></div>')
A(caption("Left: Vertiv month-end close, January 2024 to the 5 October 2026 close, not adjusted for dividends (Yahoo Finance, retrieved "
          "6 October 2026). Right: the events behind the fall from the May peak, from Vertiv filings and the earnings call of 11 February 2026."))
A('</div>')
A(para("<strong class='lead'>Where I differ is in what the July miss and the September fall mean.</strong> A supplier that cannot ship fast enough, while its "
       "margin rises, is short of capacity, not short of demand. Congestion in making complex products is the claim seen from the factory "
       "floor: the products are harder to build because each megawatt needs harder equipment. Vertiv's response has been to raise its full "
       "year sales guide twice, from US$13.25 to 13.75 billion in February to US$13.8 to 14.2 billion in July."))
A(para("<strong class='lead'>The missing backlog is a real loss of evidence</strong>, and I said so in September. But it moves the test "
       "rather than removing it. The last figure was US$15.0 billion at the end of 2025, up 109%, with fourth quarter organic orders up "
       "about 252% and a book-to-bill of about 2.9. The 2026 annual report, due in February 2027, gives the next one."))

A(section("Valuation, with the working"))
A(para("I value Vertiv on earnings per share, because its profit converts almost fully into cash and it carries little debt. The target "
       "looks twelve months out, to October 2027. By then the market will be pricing 2028 earnings, so that is the year I value."))
A(para("The estimates are mine, not Vertiv's, except where marked as its guide. I tie earnings to adjusted operating profit using the ratio "
       "implied by Vertiv's own 2026 guide, about US$6.70 of earnings per share for every US$3.325 billion of operating profit. That "
       "carries its current tax rate, interest cost and share count forward unchanged. Growth in 2027 and 2028 sits at Vertiv's own "
       "long-run target of 20 to 22% organic growth a year. Margin climbs about one point a year towards its 2030 target of 27%. My 2027 "
       "earnings sit about 4.5% below the consensus, so this is not a call that depends on beating the street."))
A(para("<strong class='lead'>The multiple.</strong> I use 28 times 2028 earnings for the base case. That is in line with Eaton, nVent and "
       "Trane on forward earnings today, and far below where Vertiv itself traded in May. A business growing at twice their pace with a "
       "rising margin should not need a discount to them. 28 x US$10.65 = US$298, rounded to a US$300 target."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "Growth slows to 10 to 12%, margin stalls at 23.5%", "US$8.17", "22x", "US$180", "down 29%", "25%"],
        ["Base", "Growth at the long-run target, margin up a point a year", "US$10.65", "28x", "US$298", "up 18%", "50%"],
        ["Bull", "Growth of 22 to 24%, margin reaches 27% early", "US$11.52", "34x", "US$392", "up 54%", "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "about US$292", "up 15%", ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [10, 36, 11, 9, 13, 12, 9]))
A(caption("All cases start from the 2026 guide midpoint of US$14.0bn and use the same earnings bridge. The bear and bull EPS use the midpoints "
          "of the stated growth ranges (11% and 23% a year). The weighted value uses the unrounded case values of "
          "US$179.70, US$298.20 and US$391.80."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["2028 EPS", "24x", "28x", "32x"],
    [
        ["US$9.50", "US$228", "US$266", "US$304"],
        ["US$10.65", "US$256", "<b>US$298</b>", "US$341"],
        ["US$11.50", "US$276", "US$322", "US$368"],
    ],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para("Most of the range sits above today's price: eight of the nine cells. The call loses money mainly if earnings fall short and the "
       "multiple compresses together, which is the bear case. Every figure here is live in the accompanying model, so a change to growth, "
       "margin or the multiple moves the target."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [[c, t, p, w] for c, t, p, w in PEERS],
    num_cols={2},
), [19, 12, 14, 55]))
A(caption("Forward P/E from stockanalysis.com, retrieved 6 October 2026. Vertiv is also 37.9x the midpoint of its own 2026 earnings guide. "
          "Peer multiples are used only to set the base multiple. Schneider Electric bought Motivair and Eaton bought Boyd Thermal for liquid "
          "cooling; on 5 October Schneider agreed to buy PTC, a software company, for about US$22.6bn."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Late October 2026 (date not yet announced)", "Third quarter 2026 results",
         "Adjusted operating margin against the 24 to 25% Q3 guide, and against the same quarter of 2025; any change to the full year guide"],
        ["Second half of 2026", "800 VDC power line", "Whether Vertiv's 800 VDC equipment, designed alongside Nvidia since May 2025, ships on Nvidia's timetable ahead of its 2027 rack generation"],
        ["February 2027", "2026 Form 10-K and full year results", "Year-end backlog against US$15.0bn a year earlier; full year 2026 adjusted EPS against the US$6.65 bottom of the guide"],
        ["Through mid 2027", "Each quarterly release", "Margin year on year while sales grow; integration of UtilityInnovation Group"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the thesis"))
A(para("<strong>The cycle turns.</strong> If the largest cloud companies cut data centre spending, Vertiv's volume falls whatever happens "
       "to content per megawatt. The bear case is this, and it is a 29% fall."))
A(para("<strong>The margin stalls.</strong> The call rests on margin rising while sales grow. A year-on-year fall in any quarter while sales "
       "still grow would mean liquid cooling is turning into a commodity. That is the first line of what proves the call wrong."))
A(para("<strong>Buyers build their own.</strong> The biggest cloud operators design much of their own hardware, and cooling could follow. "
       "I found no report of one doing so at scale yet, but it is the risk the September piece named and it stays on the list."))
A(para("<strong>Rivals with deeper pockets.</strong> Schneider Electric bought Motivair and Eaton bought Boyd Thermal for liquid cooling. "
       "Schneider's agreed US$22.6 billion purchase of PTC sends money to software, not cooling factories, which slightly helps Vertiv for now."))
A(para("<strong>Acquisitions.</strong> Vertiv has agreed five deals this year, the largest being UtilityInnovation Group. It costs about "
       "US$1.45 billion in cash, plus up to US$1.15 billion more if profit targets are met, at about 13 times its expected 2027 earnings "
       "before interest, tax, depreciation and amortisation. Buying growth at that price only works if the integration is clean."))
A(para("<strong>Weak spots in the evidence.</strong> Europe, the Middle East and Africa fell 2.4% organically in the second quarter. Vertiv "
       "discloses no single customer's share of sales, and the backlog figure is now annual."))

A('<div class="keeptogether">')
A(section("What would change our mind"))
A(para("<strong>The call is wrong if</strong> adjusted operating margin falls year on year in any quarter to mid 2027 while sales are still "
       "growing, or full year 2026 adjusted earnings per share land below the US$6.65 bottom of Vertiv's own guide, or the 2026 annual "
       "report shows backlog below the US$15.0 billion of a year earlier."))
A(para("<strong>The other way:</strong> a margin above the 24 to 25% guide in the third quarter, together with a 2026 backlog well above "
       "US$15.0 billion, would move the base case towards the bull case."))
A('</div>')

A(section("Conclusion"))
A(para("The September piece argued that each AI megawatt holds more of what Vertiv makes. A year of margins says that is happening. The "
       "market has spent five months treating Vertiv as a volume story near its peak, and has cut the multiple of this year's earnings "
       "from about 60 times to about 38. The price now pays for the volume but not for the richer content. LONG, Medium conviction, "
       "twelve-month target US$300."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026", "2027E", "2028E", "Basis"],
    [
        ["Net sales growth", "37% (guide midpoint)", "21%", "20%", "Vertiv long-run target, 20 to 22% organic a year"],
        ["Adjusted operating margin", "23.8% (guide midpoint)", "25.0%", "26.0%", "About a point a year towards the 2030 target of about 27%"],
        ["EPS per US$bn of adjusted operating profit", "US$2.015", "US$2.015", "US$2.015", "US$6.70 / US$3.325bn, 2026 guide midpoints"],
        ["Target multiple", "", "", "28x", "In line with Eaton, nVent and Trane forward"],
    ],
), [27, 17, 10, 10, 36]))
A(caption("Full workings, with live formulas, in the accompanying model, 2026-10-06_Vertiv_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Vertiv quarterly results releases on Form 8-K, Exhibit 99.1, from 24 April 2024 to 29 July 2026, for sales, organic '
  'growth by products and services, adjusted operating profit and margin, adjusted earnings per share, orders and backlog. Vertiv Form 10-Q '
  'for the quarter to 30 June 2026, filed 29 July 2026, for cash, debt, share count and regional sales. Vertiv 2025 Form 10-K, filed '
  '13 February 2026. Vertiv 2026 Investor Conference presentation, 19 May 2026, for 2030 targets. Vertiv Form 8-K of 2 September 2026 on '
  'UtilityInnovation Group. Vertiv fourth quarter 2025 earnings call, 11 February 2026, on ending quarterly backlog disclosure. Vertiv '
  'announcements on the Nvidia 800 VDC architecture, May and October 2025. Consensus earnings from MarketBeat and peer multiples from '
  'stockanalysis.com, both retrieved 6 October 2026. Share prices are Yahoo Finance closes, retrieved 6 October 2026. Estimates for 2027 '
  'and 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. It '
  're-presents, at initiation depth, the call published on The Physical Layer on 6 October 2026, and changes none of its figures or '
  'arguments. The call tests a claim from my journal piece of 25 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/every-megawatt-got-harder/">thephysicallayer.fyi/journal/every-megawatt-got-harder</a>; '
  'all calls and their scorecard are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. Figures '
  'taken from company filings are labelled as such; derived figures are marked; the forecasts, target and call are my own estimates and my '
  'own view. I hold no position in Vertiv. Personal research, not investment advice.</p>')
A('<p class="signoff">Tommy Lau | The Physical Layer | thephysicallayer.fyi</p>')
A('</div>')

html = page_shell("\n".join(P), FOOT, DATE).replace("</style>", EXTRA_CSS + "</style>")
hp = f"{D}/vertiv_note.html"
open(hp, "w", encoding="utf-8").write(html)
render_pdf(hp, PDF)
