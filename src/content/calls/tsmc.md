---
title: "TSMC is the bottleneck today. At US$486, the ADR already pays for it still being one in 2028."
summary: "TSMC makes almost every advanced AI chip, and its factories, not the power grid, limit AI supply today. Its own numbers show it: it ships more wafers, earns more on each, and keeps two thirds of every sale as gross profit. The shares have risen three quarters in a year and now price that scarcity lasting into 2028, when the new fabs land, which is the horizon on which I expect the grid, not TSMC, to bind."
company: "TSMC"
ticker: "TSM"
exchange: "NYSE"
claims: ["tsmc-says-it-is-the-bottleneck"]
correction: "I attached Wei's remark that new spending adds almost nothing to 2026 output to the raised US$60 to 64 billion budget; he said it in January, of the original US$52 to 56 billion."
keyPoints:
  - "TSMC makes almost every advanced AI chip, and on today's horizon its factories, not the grid, are what limits AI supply. Its own numbers agree: wafers shipped rose 17 per cent in the second quarter and revenue per wafer rose 17 per cent too."
  - "Scarcity shows up as margin. Gross margin reached 67.7 per cent in the second quarter, almost twelve points above the 56 per cent TSMC itself calls achievable through the cycle."
  - "July and August revenue already put the third quarter on course to beat the top of TSMC's own guide, so the near horizon of the claim is holding."
  - "At US$485.80 the ADR trades at 24 times my 2027 estimate. At 20 times, the price needs a 2028 operating margin of about 58 per cent, the scarcity margin, just as US$60 billion a year of new capacity starts to land."
  - "My call is no call: the base case is worth about the price, and the downside if the grid becomes the slower clock early is larger than the upside."
files:
  pdf: "/research/2026-10-06_TSMC_Initiation.pdf"
  xlsx: "/research/2026-10-06_TSMC_Model.xlsx"
  thumb: "/research/2026-10-06_TSMC_Initiation-p1.png"
  pages: 5
date: 2026-10-06T21:47:37+08:00
draft: false
call:
  direction: "NO CALL"
  price: 485.80
  priceDate: 2026-10-05
  currency: "US$"
  target: null
  horizon: "12 months, to October 2027"
  conviction: "Medium"
  revisitIf: "A price below about US$400 a share, or TSMC raising its through-the-cycle gross margin floor above 56 per cent."
  wrongIf: "Full year 2027 revenue grows 30 per cent or more in US dollars with an operating margin of 58 per cent or more, or TSMC raises its through-the-cycle gross margin floor above 56 per cent, or the ADR trades above US$560 by October 2027 without either."
charts:
  - id: revenue
    title: "Revenue by quarter, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 2
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Revenue"
        values: [18.87, 20.82, 23.50, 26.88, 25.53, 30.07, 33.10, 33.73, 35.90, 40.20]
    refs:
      - value: 45.2
        label: "Q3 2026 guide, midpoint"
    note: "Revenue more than doubled in two years. The third quarter guide of US$44.6 to 45.8 billion would add another 12 per cent on the second quarter."
    source: "TSMC quarterly results releases on Form 6-K, 18 April 2024 to 16 July 2026."
  - id: margin
    title: "Gross margin by quarter, per cent"
    kind: bar
    unit: "%"
    decimals: 1
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Gross margin"
        values: [53.1, 53.2, 57.8, 59.0, 58.8, 58.6, 59.5, 62.3, 66.2, 67.7]
    refs:
      - value: 56
        label: "TSMC's through-the-cycle floor"
    note: "Margin rose fourteen points in two years while the factories ran full. TSMC calls 56 per cent and higher achievable through the cycle; the gap is the price of scarcity."
    source: "TSMC quarterly results releases, 18 April 2024 to 16 July 2026; long-term margin from the fourth quarter 2025 presentation, 15 January 2026."
  - id: hpc
    title: "High-performance computing as a share of revenue, per cent"
    kind: bar
    unit: "%"
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "HPC share"
        values: [46, 52, 51, 53, 59, 60, 57, 55, 61, 66]
    note: "The platform that holds AI accelerators went from under half of revenue to two thirds. It dipped in the second half of 2025, when phone chips had their seasonal peak."
    source: "TSMC quarterly presentations, revenue by platform, 18 April 2024 to 16 July 2026."
  - id: monthly
    title: "Monthly revenue, NT$ billion"
    kind: bar
    prefix: "NT$"
    unit: "bn"
    decimals: 1
    labels: ["Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26"]
    series:
      - name: "Revenue"
        values: [293.29, 260.01, 285.96, 349.57, 320.52, 263.71, 323.17, 335.77, 330.98, 367.47, 343.61, 335.00, 401.26, 317.66, 415.19, 410.73, 416.98, 442.68, 467.58, 514.81]
    refs:
      - value: 482.1
        label: "Monthly pace of the Q3 guide midpoint"
    note: "July and August together came to NT$982.4 billion. September needs only NT$445 to 483 billion to land inside the guide; August alone was NT$514.8 billion."
    source: "TSMC monthly revenue reports on Form 6-K, 10 February 2025 to 10 September 2026. Guide pace is US$45.2 billion at TSMC's assumed NT$32 per US$, divided by three."
  - id: price
    title: "TSMC ADR price, month-end close, US$"
    kind: line
    prefix: "US$"
    decimals: 2
    labels: ["Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
    series:
      - name: "Close"
        values: [97.31, 104.00, 112.96, 128.67, 136.05, 137.34, 151.04, 173.81, 165.80, 171.70, 173.67, 190.54, 184.66, 197.49, 209.32, 180.53, 166.00, 166.69, 193.32, 226.49, 241.62, 230.87, 279.29, 300.43, 291.51, 303.89, 330.56, 374.58, 337.95, 396.06, 418.45, 477.57, 404.25, 415.32, 456.19, 485.80]
    note: "The ADR has risen 74 per cent since the end of September 2025 and closed on 5 October 2026 within 0.4 per cent of its 52-week high."
    source: "Yahoo Finance monthly closes for NYSE: TSM, not adjusted for dividends, retrieved 6 October 2026. The last point is the close on 5 October 2026."
---

TSMC's American depositary shares closed at US$485.80 on 5 October 2026. Each one stands for five ordinary shares listed in Taipei. The ADR has risen 74 per cent in a year and sits within two dollars of its 52-week high.

On 2 October I argued that, on today's horizon, TSMC's factories bind before the grid does. I also said that over the longer run I still expect the grid to be the slower clock. The claim has two horizons, and a twelve-month call has to say which one it rests on.

The near horizon is holding, and TSMC's own numbers say so plainly. The difficulty is that the price says so too.

My call is no call. The evidence for the near horizon is already in the price, and the longer horizon is the one the market will be pricing by October 2027.

## The thesis

Go back to the shared kitchen from the October piece. Every famous restaurant in the city designs its own dishes, and all of them send the cooking to one kitchen. When demand surges, the queue at that kitchen sets how fast every restaurant grows.

A kitchen with a queue does two things. It cooks more meals, and it charges more for each one. TSMC is doing both.

**More wafers.** TSMC shipped 4.34 million wafers, counted in twelve-inch equivalents, in the second quarter of 2026. That was 17 per cent more than a year earlier. The fabs were already full a year ago, so the extra came from squeezing more out of existing lines and starting new ones.

**More per wafer.** Revenue in Taiwan dollars rose 36 per cent in the same quarter, so revenue per wafer rose about 17 per cent as well. Part of that is mix, as more wafers move to the newest processes. Part is price. Either way, each wafer is earning more because customers are queuing for the scarce ones.

**More of each sale kept.** Gross margin, the share of each sale left after the cost of making it, reached 67.7 per cent in the second quarter. Two years earlier it was 53.1 per cent. TSMC's own long-term target is 56 per cent and higher through the cycle, so today's margin sits almost twelve points above the floor its management calls normal.

**Where the pull comes from.** High-performance computing, the platform that holds AI accelerators, was 66 per cent of revenue in the second quarter, against 46 per cent at the start of 2024. TSMC said AI accelerators alone were in the high teens as a share of 2025 revenue. It expects that business to grow at a mid to high 50s per cent rate a year from 2024 to 2029.

**The packaging pinch.** In July chief executive C.C. Wei said TSMC's packaging capacity is so tight that it is limiting customers' growth. That is the near horizon of the claim in the company's own words. A stacked-memory AI chip that cannot be joined to its memory cannot ship, however many processors wait.

**The newest evidence.** TSMC publishes revenue every month, and the third quarter is already two thirds reported. July and August came to NT$982.4 billion. At TSMC's assumed rate of NT$32 to the dollar, the guide of US$44.6 to 45.8 billion needs only NT$445 to 483 billion in September. August alone was NT$514.8 billion. Unless September falls sharply, the quarter lands at or above the top of the guide.

**Where I was wrong in October.** In the piece I wrote that TSMC raised its 2026 capital budget to US$60 to 64 billion, and that Wei said that money adds almost nothing to output this year. The timing was wrong. Wei made that remark on 15 January, about the original budget of US$52 to 56 billion. The raise came on 16 July.

What changed my view was rereading the January and July transcripts side by side for this note. The point itself stands, and if anything the larger budget makes it stronger: spending decided in 2026 buys supply for 2028 and 2029. The piece and the claim stay exactly as published, so the record shows the slip.

## What the market prices in, and where I differ

At US$485.80 the ADR values TSMC at about US$2.52 trillion. TSMC holds roughly US$84 billion more in cash and marketable securities than in long-term debt, so the net cash barely moves the answer.

That is 28.9 times my 2026 earnings estimate of US$16.81 per ADR, and 24.0 times my 2027 estimate of US$20.25. On MarketBeat's 2027 consensus of US$21.33, retrieved on 6 October, it is 22.8 times. Stockanalysis.com shows a forward multiple of 20.7 times and an average analyst target of US$552.

The ADR also costs more than the shares underneath it. The Taipei shares closed at NT$2,585 on 6 October. Five of them, at NT$31.75 to the dollar, are worth US$407. The ADR therefore trades at a premium of about 19 per cent to its own underlying shares.

**What the price needs.** By October 2027 the market will be pricing 2028 earnings. At 20 times, close to TSMC's forward multiple today, US$485.80 needs 2028 earnings of US$24.29 per ADR. On my 2028 revenue of US$251 billion, that needs an operating margin of about 58 per cent. Operating margin is the share of sales left after running costs, before interest and tax. TSMC's was 57.7 per cent on my 2026 estimate.

So the market is paying for today's scarcity margin to last into 2028. That is the year the October piece named as the test of the longer horizon. It is when the US$60 to 64 billion of 2026 spending, and whatever TSMC spends in 2027, starts producing wafers.

**Where I differ.** I agree with the market on the near horizon. Where I differ is on what happens when the new capacity lands. Three physical things push margin down in 2028, whatever demand does.

The first is depreciation. A fab is paid for up front and charged against profit over several years once it runs. Capital spending rose from NT$956 billion in 2024 to NT$1,272 billion in 2025, and the first half of 2026 alone was NT$847 billion. That charge arrives with the output.

The second is distance from the cluster. TSMC guides that overseas fabs cut gross margin by two to three points at first, widening to three to four. Arizona's second fab is due to reach volume in the second half of 2027.

The third is the newest process. TSMC expects its 2 nanometre ramp to cut gross margin by about three to four points in the second half of 2026.

TSMC has offset all of this so far with price. It can keep doing so only while customers are still queuing. That is where the longer horizon of my claim comes in. If the grid is the slower clock, the capacity arriving in 2028 meets customers whose data centres are waiting for power. The queue at the kitchen shortens just as the kitchen gets bigger.

TSMC's own plan points the same way. It guides to revenue growth approaching 25 per cent a year from 2024 to 2029, from US$90.1 billion. That implies about US$275 billion in 2029. With 2026 already near US$172 billion, the plan leaves about 17 per cent a year for 2027 to 2029. My base case follows that plan, not a bust.

## Valuation, with the working

I value TSMC on earnings per ADR, because it earns most of its revenue in US dollars, carries net cash and pays out a steady, rising dividend. The target horizon is twelve months, to October 2027, so the year I value is 2028.

The estimates below are mine except where marked. I build earnings from revenue and operating margin. Non-operating income adds 2.5 per cent of revenue, its level in the first quarter of 2026. Tax and minorities take 17 per cent of pre-tax profit, close to the first half of 2026. Each ADR is five of TSMC's 25.93 billion shares.

One adjustment matters. Non-operating items jumped to NT$95.8 billion in the second quarter, from NT$28.8 billion in the first, the quarter TSMC sold part of its stake in Vanguard International. I treat that jump as non-recurring and leave it out of my estimates. It added roughly US$0.34 to second quarter earnings per ADR, on my working.

| | 2024 | 2025 | 2026 mine | 2027 mine | 2028 mine |
|---|---|---|---|---|---|
| Revenue, US$ billion | 90.08 | 122.42 | 171.50 | 212.66 | 250.94 |
| Growth | | 36% | 40% | 24% | 18% |
| Gross margin | 56.1% | 59.9% | | | |
| Operating margin | 45.7% | 50.8% | 57.7% | 57.0% | 55.5% |
| EPS per ADR, US$ | 7.04 | 10.65 | 16.81 | 20.25 | 23.29 |
| Price to earnings at US$485.80 | 69.0x | 45.6x | 28.9x | 24.0x | 20.9x |

The 2024 and 2025 figures are TSMC's, with earnings per ADR summed from its quarterly releases. My 2026 uses the reported first half, then US$46.4 billion in the third quarter on the monthly run-rate and US$49.0 billion in the fourth. That gives growth of 40 per cent, in line with TSMC's guide of slightly above 40. I model operating margin, not gross margin, for the years ahead. My 2027 earnings sit 5 per cent below the MarketBeat consensus.

**The multiple.** I use 20 times 2028 earnings for the base case. That is TSMC's own forward multiple today, and below the 22 to 24 times of the smaller foundries GlobalFoundries and UMC. It assumes no rerating either way.

**Three cases, twelve months out.**

| Case | What happens | 2028 EPS | Multiple | Value | Change |
|---|---|---|---|---|---|
| Bear | The grid binds first: growth of 15% then 5%, operating margin falls to 50% in 2028 | US$17.40 | 16x | US$278 | down 43% |
| Base | TSMC's own plan: growth of 24% then 18%, margin eases to 55.5% | US$23.29 | 20x | US$466 | down 4% |
| Bull | The factory stays the bottleneck: growth of 30% then 25%, margin holds at 59% | US$27.43 | 24x | US$658 | up 36% |

Weighted 25, 50 and 25 per cent, the three cases give about US$467, 4 per cent below the price. The downside in the bear case is larger than the upside in the bull case.

**How sensitive it is.** Each row is a 2028 estimate and each column a multiple.

| 2028 EPS | 16x | 20x | 24x |
|---|---|---|---|
| US$20.00 | US$320 | US$400 | US$480 |
| US$23.29 | US$373 | US$466 | US$559 |
| US$26.00 | US$416 | US$520 | US$624 |

Only three of the nine cells sit above today's price. To make money from here, TSMC needs both the bull case's earnings and a multiple at least as high as today's.

**Peers.** Forward multiples from stockanalysis.com on 6 October: GlobalFoundries 22.4 times, UMC 24.0, ASE Technology 31.4, Intel 68.8 and Samsung Electronics 4.5, the last two distorted by recovery and memory cycles. Nvidia, TSMC's largest AI customer, trades at 19.8 times. TSMC at 20.7 times is not expensive against them. It is fully priced against its own margin cycle.

<div class="charts-slot"></div>

## Risks, and what would change my view

**The factory stays the bottleneck for longer.** This is the bull case and the main risk to a no call. If AI demand keeps outrunning the new fabs into 2028, and the grid keeps up, the scarcity margin survives. TSMC raising its through-the-cycle margin floor above 56 per cent would be the clearest sign.

**The grid binds first, and sooner.** This is the bear case. It would show as TSMC's tightness easing while data centres with chips on order still wait for power, which is the near horizon of my claim breaking. Watch for TSMC describing packaging as balanced, or high-performance computing slipping as a share of revenue.

**The exchange rate.** TSMC reports in Taiwan dollars, sells mostly in US dollars and guides margin at a set rate, NT$32 for the third quarter. A stronger Taiwan dollar lowers margin and earnings per ADR. The ADR premium of about 19 per cent to the Taipei shares can also narrow, which would hurt the ADR even if the business does well.

**Taiwan's electricity.** In January Wei said his first worry on power was Taiwan's own supply. A fab is a building waiting on power too, and the Taiwan cluster is where almost all advanced capacity sits.

**Rival foundries.** Intel Foundry and Samsung Foundry both want TSMC's AI customers. I found no sign of a large AI accelerator moving away from TSMC, but packaging is where a second source is easiest.

**What would change my view.** A price below about US$400 would put my base case about 16 per cent above the price and make this a call. So would third quarter results on 15 October showing gross margin at or above the 67 per cent top of the guide despite the 2 nanometre ramp. In the other direction, TSMC calling packaging supply balanced before 2028 would bring the bear case forward.

The third quarter results and call are on Thursday 15 October 2026, at 2pm Taiwan time, as TSMC has announced. September revenue usually follows around the tenth of the month; TSMC has not confirmed the date.

## Conclusion

The October piece argued that, today, TSMC's factories bind before the grid does. A quarter of TSMC's own numbers says that is right: more wafers, more per wafer, and a margin almost twelve points above its own long-term floor. The third quarter is on course to beat the top of the guide.

The shares know this. At US$485.80 the ADR is 24 times my 2027 earnings and needs the scarcity margin to survive into 2028, the year new capacity lands and the longer horizon of my claim begins to be tested. My call is no call, with medium conviction. My base case, close to TSMC's own five-year plan, is worth about the price, and the downside if the grid becomes the slower clock early is larger than the upside. I would revisit below about US$400, or if TSMC raises its through-the-cycle margin floor.

<p class="sources">Sources: TSMC quarterly results releases and presentations furnished on Form 6-K, 18 April 2024 to 16 July 2026, for revenue, margins, earnings per share and per ADR, technology and platform mix, wafer shipments, non-operating items, cash, debt, share count, capital expenditures and the third quarter 2026 guide. TSMC fourth quarter 2025 presentation, 15 January 2026, for 2024 and 2025 annual figures and its 2024 to 2029 targets. TSMC monthly revenue reports on Form 6-K, 10 February 2025 to 10 September 2026. TSMC earnings call transcripts of 15 January and 16 July 2026, for comments on wafer supply, power, Taiwan's electricity, fab build times, capital spending, packaging capacity, overseas and 2 nanometre margin dilution, Arizona and dividends. TSMC Form 6-K of 15 May 2026 on the Vanguard International share sale. TSMC investor relations, for the 15 October 2026 results date. Consensus from MarketBeat and stockanalysis.com, and peer multiples from stockanalysis.com, all retrieved 6 October 2026. ADR, Taipei share and exchange rate prices from Yahoo Finance, retrieved 6 October 2026. Estimates for 2026 to 2028 are the author's own. Personal research, not investment advice.</p>
