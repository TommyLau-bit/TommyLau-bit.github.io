---
title: "The market has sold Vertiv as a volume story. Its margin says each megawatt is worth more."
summary: "Vertiv makes the power and cooling equipment inside AI data centres. Its shares have fallen by a third since May on fears that growth is peaking and supply is congested. Its own numbers show each sale earning more, not less, which is what a rising amount of equipment per megawatt looks like."
company: "Vertiv"
ticker: "VRT"
exchange: "NYSE"
claims: ["every-megawatt-got-harder"]
correction: "I cited service growing faster than products as evidence. Without acquisitions it grew more slowly, so the claim rests on margin alone."
date: 2026-10-06T19:29:59+08:00
draft: false
call:
  direction: "LONG"
  price: 253.62
  priceDate: 2026-10-05
  currency: "US$"
  target: 300
  horizon: "12 months, to October 2027"
  conviction: "Medium"
  wrongIf: "Adjusted operating margin falls year on year in any quarter to mid 2027 while sales are still growing, or full year 2026 adjusted earnings per share land below the US$6.65 bottom of Vertiv's own guide, or the 2026 annual report shows backlog below the US$15.0 billion of a year earlier."
charts:
  - id: sales
    title: "Net sales by quarter, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 2
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Net sales"
        values: [1.64, 1.95, 2.07, 2.35, 2.04, 2.64, 2.68, 2.88, 2.65, 3.27]
    note: "Sales doubled in two years. The first quarter is always the softest, so compare each quarter with the same one a year earlier."
    source: "Vertiv quarterly results releases, Exhibit 99.1, 24 April 2024 to 29 July 2026."
  - id: margin
    title: "Adjusted operating margin by quarter, per cent"
    kind: bar
    unit: "%"
    decimals: 1
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Adjusted operating margin"
        values: [15.2, 19.6, 20.1, 21.5, 16.5, 18.5, 22.3, 23.2, 20.8, 22.6]
    refs:
      - value: 23.8
        label: "2026 guide, midpoint"
    note: "Every quarter since the third quarter of 2025 has beaten the same quarter a year earlier, by 1.7 to 4.3 points, while sales kept rising. The call rests on that pattern holding."
    source: "Vertiv quarterly results releases, 24 April 2024 to 29 July 2026; full year 2026 guide from the release of 29 July 2026."
  - id: mix
    title: "Organic growth, products against service and spares, per cent"
    kind: bar
    unit: "%"
    decimals: 1
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Products"
        values: [7.7, 15.3, 19.9, 31.5, 31.1, 38.5, 33.6, 20.4, 24.9, 19.7]
      - name: "Service and spares"
        values: [9.4, 8.5, 16.9, 12.1, 7.4, 18.6, 10.1, 14.9, 13.7, 10.1]
    note: "Stripped of acquisitions and currency, service has grown more slowly than products in nine of these ten quarters. This is where my September piece was wrong, as the thesis explains."
    source: "Vertiv quarterly results releases, organic growth reconciliation tables, 24 April 2024 to 29 July 2026."
  - id: price
    title: "Vertiv share price, month-end close, US$"
    kind: line
    prefix: "US$"
    decimals: 2
    labels: ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
    series:
      - name: "Close"
        values: [56.33, 67.62, 81.67, 93.00, 98.07, 86.57, 78.70, 83.03, 99.49, 109.29, 127.60, 113.61, 117.02, 95.17, 72.20, 85.38, 107.93, 128.41, 145.60, 127.55, 150.86, 192.86, 179.73, 162.01, 186.18, 254.89, 250.58, 328.49, 315.71, 334.82, 241.57, 258.72, 241.31, 253.62]
    note: "The shares peaked at US$379.94 during trading on 14 May 2026 and fell 17 per cent on the day of the second quarter results, when sales missed forecasts but profit beat them."
    source: "Yahoo Finance monthly closes, not adjusted for dividends, retrieved 6 October 2026. The last point is the close on 5 October 2026."
---

Vertiv's shares closed at US$253.62 on 5 October 2026. That is a third below their peak in May, during a year when Vertiv twice raised its own guidance and widened its margin by four points.

The market's worry is easy to state. AI data centre spending may be near its peak, Vertiv's sales missed forecasts in July, and Vertiv stopped publishing its order backlog. The fear is that a supplier riding a building boom is about to find out where the boom ends.

My answer comes from the claim I made in September. Vertiv is paid per megawatt, and AI has made every megawatt harder to build. If that is right, the thing to watch is not how many megawatts get built. It is how much Vertiv earns on each one.

That number is still rising, and the shares no longer pay for it.

## The thesis

Think of the electrician from the September piece. For years every new house needed the same fuse box. Now each house wants a heat pump, an induction hob and a car charger, so the job inside every house has grown. The electrician gains twice: more houses, and a bigger job in each.

Vertiv is that electrician inside an AI data centre. An AI cabinet draws more than 130 kilowatts, against 5 to 12 kW for an ordinary server rack. Air cannot carry that heat away, so the heat leaves through liquid, which needs coolant distribution units, pipework and heat exchangers on every row. The power side is moving to 800 volts of direct current, which needs new conversion equipment. Each megawatt of AI capacity holds more of what Vertiv makes, and more complicated versions of it.

The money should show this in one place above all: margin. Adjusted operating margin is the share of each sale left after running costs, with one-off items stripped out. If Vertiv were only selling more of the same boxes into a boom, margin would drift with volume and then fall as rivals added capacity. If each megawatt holds richer equipment, margin should keep rising while sales grow.

It has. Every quarter since the third quarter of 2025 has beaten the same quarter a year earlier. The second quarter of 2026 reached 22.6 per cent, up 4.1 points, on sales of US$3.27 billion. Vertiv now guides to 23.3 to 24.3 per cent for the full year, and to 24 to 25 per cent for the third quarter. At its investor conference in May it set a target of about 27 per cent or more by 2030.

**Where I was wrong in September.** In the piece I wrote that service revenue grew 33 per cent against 22 per cent for products, and called service outgrowing hardware evidence for the claim. That was wrong. Those were reported figures, swollen by acquisitions. Stripped of acquisitions and currency, service grew about 10 per cent and products about 20 per cent, and service has grown more slowly than products in nine of the last ten quarters.

What changed my view was working through the organic split in Vertiv's own reconciliation tables for this pitch, which I had not done for the piece. The claim itself, that what Vertiv sells per megawatt is rising, survives on margin, which is the stronger test anyway. This call rests on margin and not on service. The piece and the claim stay exactly as published, so the record shows the mistake.

## What the market prices in, and where I differ

At US$253.62 Vertiv is valued at about US$99.6 billion on its diluted shares. It holds roughly US$170 million more cash than debt. That is 37.9 times the midpoint of its own 2026 earnings guide, and 28.4 times the 2027 consensus of US$8.93 a share, as compiled by MarketBeat on 6 October.

That multiple has fallen fast. At the May peak the shares traded at about 59 times the 2026 earnings guide of the time, US$6.30 to 6.40 a share. Today the gap to the large electrical groups is small. Eaton, nVent and Trane each trade at about 28.5 to 29 times forward earnings, and Schneider Electric at 24, according to stockanalysis.com on 6 October.

So the market now prices Vertiv close to a diversified industrial whose data centre exposure is one division among many. The three things that moved the price explain why.

**The July sales miss.** Second quarter sales came in about 3 per cent below consensus, while earnings per share beat it. Vertiv blamed timing and supply congestion. The shares fell 17 per cent that day.

**The September fall.** On 8 September the chief executive spoke of congestion in the supply chain for complex products. The next day the shares fell 9.6 per cent, in a broad sell-off of AI infrastructure names. A week earlier Vertiv had agreed to buy UtilityInnovation Group, a microgrid controls business, for about US$1.45 billion in cash, with little financial detail.

**The missing backlog.** On 11 February Vertiv said it would stop reporting orders and backlog each quarter, because large orders arrive in lumps. It will still report backlog once a year, in its annual report.

Where I differ is in what the first two mean. A supplier that cannot ship fast enough, while its margin rises, is short of capacity, not short of demand. Congestion in making complex products is the claim seen from the factory floor. The products are harder to build because each megawatt needs harder equipment. Vertiv's response has been to raise its full year sales guide twice, from US$13.25 to 13.75 billion in February to US$13.8 to 14.2 billion in July.

The missing backlog is a real loss of evidence, and I said so in September. But it moves the test, rather than removing it. The last figure was US$15.0 billion at the end of 2025, up 109 per cent, with fourth quarter orders up about 252 per cent. The 2026 annual report, due in February 2027, gives the next one.

## Valuation, with the working

I value Vertiv on earnings per share, because its profit converts almost fully into cash and it carries little debt. The target looks twelve months out, to October 2027. By then the market will be pricing 2028 earnings, so that is the year I value.

The estimates below are mine, not Vertiv's, except where marked as its guide. I tie earnings to adjusted operating profit using the ratio implied by Vertiv's own 2026 guide, about US$6.70 of earnings per share for every US$3.325 billion of operating profit. That carries its current tax rate, interest cost and share count forward unchanged.

| | 2024 | 2025 | 2026 guide | 2027 mine | 2028 mine |
|---|---|---|---|---|---|
| Net sales, US$ billion | 8.01 | 10.23 | 13.8 to 14.2 | 16.94 | 20.33 |
| Growth | | 28% | 37% | 21% | 20% |
| Adjusted operating margin | 19.4% | 20.4% | 23.8% | 25.0% | 26.0% |
| Adjusted EPS, US$ | 2.85 | 4.19 | 6.65 to 6.75 | 8.53 | 10.65 |
| Price to earnings at US$253.62 | | | 37.9x | 29.7x | 23.8x |

The 2024 and 2025 figures are the sums of the four quarterly releases. Growth in 2027 and 2028 sits at Vertiv's own long-run target of 20 to 22 per cent organic growth a year. Margin climbs about one point a year towards its 2030 target of 27 per cent. My 2027 earnings sit about 4 per cent below the consensus, so this is not a call that depends on beating the street.

**The multiple.** I use 28 times 2028 earnings for the base case. That is in line with Eaton, nVent and Trane on forward earnings today, and far below where Vertiv itself traded in May. A business growing at twice their pace with a rising margin should not need a discount to them.

**Three cases, twelve months out.**

| Case | What happens | 2028 EPS | Multiple | Value | Change |
|---|---|---|---|---|---|
| Bear | Growth slows to 10 to 12 per cent, margin stalls at 23.5 per cent | US$8.17 | 22x | US$180 | down 29% |
| Base | Growth at the long-run target, margin up a point a year | US$10.65 | 28x | US$298 | up 18% |
| Bull | Growth of 22 to 24 per cent, margin reaches 27 per cent early | US$11.52 | 34x | US$392 | up 54% |

Weighted 25, 50 and 25 per cent, the three cases give about US$293, 15 per cent above the price.

**How sensitive it is.** Each row is a 2028 estimate and each column a multiple.

| 2028 EPS | 24x | 28x | 32x |
|---|---|---|---|
| US$9.50 | US$228 | US$266 | US$304 |
| US$10.65 | US$256 | US$298 | US$341 |
| US$11.50 | US$276 | US$322 | US$368 |

Most of the range sits above today's price. The call loses money mainly if earnings fall short and the multiple compresses together, which is the bear case.

<div class="charts-slot"></div>

## Risks, and what would change my view

**The cycle turns.** If the largest cloud companies cut data centre spending, Vertiv's volume falls whatever happens to content per megawatt. The bear case is this, and it is a 29 per cent fall.

**The margin stalls.** The call rests on margin rising while sales grow. A year-on-year fall in any quarter while sales still grow would mean liquid cooling is turning into a commodity. That is the first line of what proves the call wrong.

**Buyers build their own.** The biggest cloud operators design much of their own hardware, and cooling could follow. I found no report of one doing so at scale yet, but it is the risk the September piece named and it stays on the list.

**Rivals with deeper pockets.** Schneider Electric bought Motivair and Eaton bought Boyd Thermal for liquid cooling. On 5 October Schneider agreed to buy PTC, a software company, for about US$22.6 billion. That money goes to software, not cooling factories, which slightly helps Vertiv for now.

**Acquisitions.** Vertiv has agreed five deals this year, the largest being UtilityInnovation Group. It costs about US$1.45 billion in cash, plus up to US$1.15 billion more if profit targets are met, at about 13 times its expected 2027 earnings before interest, tax and depreciation. Buying growth at that price only works if the integration is clean.

**Weak spots in the evidence.** Europe, the Middle East and Africa fell 2.4 per cent organically in the second quarter. Vertiv discloses no single customer's share of sales, and the backlog figure is now annual.

**What would change my view the other way.** A margin above the 24 to 25 per cent guide in the third quarter, together with a 2026 backlog well above US$15.0 billion, would move the bull case closer to the base case.

The third quarter results are due in late October. Vertiv has not yet announced the date.

## Conclusion

The September piece argued that each AI megawatt holds more of what Vertiv makes. A year of margins says that is happening. The market has spent five months treating Vertiv as a volume story near its peak, and has cut the multiple of this year's earnings from about 59 times to about 38.

The price now pays for the volume but not for the richer content. My call is LONG, with medium conviction and a twelve-month target of US$300, which is 28 times my 2028 estimate and 18 per cent above the price. Medium, not high, because the bear case is a 29 per cent fall and the third quarter results land within weeks. The call is wrong if margin falls while sales grow, if 2026 earnings land below Vertiv's own guide, or if the 2026 backlog comes in below US$15.0 billion.

<p class="sources">Sources: Vertiv quarterly results releases on Form 8-K, Exhibit 99.1, from 24 April 2024 to 29 July 2026, for sales, organic growth by products and services, adjusted operating profit and margin, adjusted earnings per share, orders and backlog. Vertiv Form 10-Q for the quarter to 30 June 2026, filed 29 July 2026, for cash, debt, share count and regional sales. Vertiv 2025 Form 10-K, filed 13 February 2026. Vertiv 2026 Investor Conference presentation, 19 May 2026, for 2030 targets. Vertiv Form 8-K of 2 September 2026 on UtilityInnovation Group. Vertiv fourth quarter 2025 earnings call, 11 February 2026, on ending quarterly backlog disclosure. Consensus earnings from MarketBeat and peer multiples from stockanalysis.com, both retrieved 6 October 2026. Share prices are Yahoo Finance closes, retrieved 6 October 2026. Estimates for 2027 and 2028 are the author's own. Personal research, not investment advice.</p>
