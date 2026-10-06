---
title: "Corning's AI fibre is sold out. At US$159, the shares already pay for it to stay that way."
summary: "Corning makes the glass fibre that carries data between AI chips, and its data centre sales are growing faster than it can build factories. That is why it set up a US$2 billion share sale in September: being sold out costs money before it earns any. At about 37 times next year's earnings, the price already assumes the new factories fill on time and at today's margins."
company: "Corning"
ticker: "GLW"
exchange: "NYSE"
claims: ["corning-lays-the-glass"]
correction: "I wrote that Nvidia paid US$500 million to secure Corning's glass. It paid that for Corning equity, and Corning gave it a second warrant, valued at US$296 million, that comes off future revenue."
keyPoints:
  - "Corning makes the glass fibre that carries data between AI chips. Its optical sales rose 32 per cent in the second quarter, the data centre part 65 per cent, and the segment's margin reached a record 21 per cent."
  - "The US$2 billion share sale set up in September answers a real question. Corning is sold out, so growth needs factories first: capital spending rises to about US$2 billion this year, and customer deposits pay for only part of it."
  - "Optical is now the stock. Swinging optical from my bear case to my bull case moves 2028 earnings four times as much as doing the same to the rest of Corning."
  - "At US$159.37 the shares trade at 49 times my 2026 earnings and 29 times my 2028. At 27 times, the price needs optical sales of about US$16 billion in 2028, 2.6 times 2025."
  - "My call is no call: the base case is worth about US$146, 8 per cent below the price, and the range runs from US$86 to US$220."
files:
  pdf: "/research/2026-10-06_Corning_Initiation.pdf"
  xlsx: "/research/2026-10-06_Corning_Model.xlsx"
  thumb: "/research/2026-10-06_Corning_Initiation-p1.png"
  pages: 5
date: 2026-10-06T21:47:37+08:00
draft: false
call:
  direction: "NO CALL"
  price: 159.37
  priceDate: 2026-10-05
  currency: "US$"
  target: null
  horizon: "12 months, to October 2027"
  conviction: "Medium"
  revisitIf: "A price below about US$127, or fourth quarter results in January 2027 showing optical sales of US$2.4 billion or more in the quarter with a segment net margin of 23 per cent or more, and the share sale programme largely unused."
  wrongIf: "Optical Communications sales reach US$11.5 billion or more in 2027 with a segment net margin of 24 per cent or more, or the shares close above US$200 or below US$110 by October 2027."
charts:
  - id: optical
    title: "Optical Communications sales by quarter, US$ million"
    kind: bar
    prefix: "US$"
    unit: "m"
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Optical Communications"
        values: [930, 1113, 1246, 1368, 1355, 1566, 1652, 1701, 1846, 2072]
    note: "Optical sales more than doubled in two years. Growth has eased from 46 per cent to 32 per cent a year as the base has grown."
    source: "Corning quarterly earnings releases, 30 April 2024 to 28 July 2026."
  - id: margin
    title: "Optical Communications segment net income as a share of its sales, per cent"
    kind: bar
    unit: "%"
    decimals: 1
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Segment net margin"
        values: [10.8, 12.8, 14.0, 14.2, 14.8, 15.8, 17.9, 17.9, 21.0, 21.1]
    note: "The claim breaks if this margin falls while sales rise. So far it has risen in every quarter since early 2024."
    source: "Corning quarterly earnings releases, 30 April 2024 to 28 July 2026. Segment net income divided by segment sales."
  - id: mix
    title: "Core sales, optical and the rest of Corning, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 2
    labels: ["2023", "2024", "2025", "2026E", "2027E", "2028E"]
    series:
      - name: "Optical Communications"
        values: [4.01, 4.66, 6.27, 8.50, 11.47, 14.34]
      - name: "Rest of Corning"
        values: [9.57, 9.81, 10.13, 10.62, 11.57, 12.50]
    note: "Optical was 38 per cent of sales in 2025. On my estimates it passes half in 2028."
    source: "Corning fourth quarter releases and Form 10-K for 2025; 2026E to 2028E are the author's own."
  - id: cash
    title: "Capital spending against adjusted free cash flow, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 2
    labels: ["2023", "2024", "2025", "H1 2026"]
    series:
      - name: "Capital spending"
        values: [1.39, 0.97, 1.28, 0.75]
      - name: "Adjusted free cash flow"
        values: [0.88, 1.25, 1.72, 1.61]
    note: "First half 2026 free cash flow includes US$0.71 billion of net customer deposits and government incentives. Capital spending is guided to about US$2 billion for 2026, so the second half spends about US$1.25 billion."
    source: "Corning fourth quarter 2024 and 2025 releases, second quarter 2026 release and Form 10-Q."
  - id: price
    title: "GLW share price, month-end close, US$"
    kind: line
    prefix: "US$"
    decimals: 2
    labels: ["Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
    series:
      - name: "Close"
        values: [28.49, 30.45, 32.49, 32.24, 32.96, 33.38, 37.26, 38.85, 40.01, 41.85, 45.15, 47.59, 48.67, 47.52, 52.08, 50.15, 45.78, 44.38, 49.59, 52.59, 63.24, 67.03, 82.03, 89.08, 84.20, 87.56, 103.25, 150.38, 135.97, 164.24, 181.16, 255.43, 138.25, 148.73, 153.76, 159.37]
    note: "The shares rose fivefold in eighteen months, then fell 46 per cent in July alone. They are still up about 91 per cent on a year ago."
    source: "Yahoo Finance monthly closes for NYSE: GLW, not adjusted for dividends, retrieved 6 October 2026. The last point is the close on 5 October 2026."
---

Corning closed at US$159.37 on 5 October 2026. The shares are up about 91 per cent on a year ago. They are also 41 per cent below the intraday high of US$271.78 reached on 30 June.

On 1 October I argued that glass fibre is the part of the AI network that outlives every chip generation, and that Corning is paid each time a campus grows. The claim is holding. Corning's optical business grew 32 per cent in the second quarter, and it earned more on each sale than ever before.

The piece left one question unanswered. Why does a business that is sold out need a US$2 billion share sale?

I tested both. The answer to the share sale is in Corning's own cash flow, and it is not a warning about demand. The shares are a different matter. They already price most of what Corning plans to build. My call is no call.

All income figures here are Corning's core measures, which strip out currency hedges and one-off items. Corning guides on that basis. GAAP figures are marked where used.

## The thesis

Go back to the pipes in the walls from the October piece. The plumber is fully booked. Every builder in town wants him, and three of the biggest have paid him in advance to keep a van free for their jobs.

That plumber still has to buy more vans and hire more hands before he can take more work. The deposits help, but they do not cover the lot. Corning is that plumber, and the question for the shares is what the extra vans cost and who pays for them.

**The mechanism is showing up.** Optical Communications sales were US$2.07 billion in the second quarter of 2026. Enterprise Networks, the data centre side, grew 65 per cent to about US$1.27 billion, as Corning said on its call. That is 61 per cent of the segment.

The older carrier side, fibre for telecom networks, was about flat at US$0.80 billion on my working. So all of the segment's growth came from data centres. That is exactly what the claim's first watch item asked for.

**The margin is the test.** The claim breaks if the segment's margin falls while its sales rise. It has not. Segment net income was 21.1 per cent of sales in the second quarter, against 15.8 per cent a year earlier and 10.8 per cent in early 2024.

**Customers are paying ahead.** Meta agreed in January to buy up to US$6 billion of fibre and cable through 2030. In April Corning said two more hyperscale customers had signed deals of similar size and length. Amazon signed in June. In September Verizon signed for fibre from 2027 to 2032.

Contract liabilities, which include customer deposits, rose from US$2.3 billion at the end of 2025 to US$2.7 billion in June. Corning says long-term contracts will become the lion's share of optical.

**The third watch item is moving the wrong way.** In 2025 two end customers bought 28 per cent of optical sales. Since then, at least five large buyers have signed long-term deals. Fewer, larger buyers on long contracts means steadier volume, but it also means buyers who set terms.

**Where I was wrong in October.** In the piece I wrote that Nvidia paid US$500 million as part of a partnership for Corning to build more fibre. That is not what the money bought. The 8-K of 6 May and the second quarter 10-Q show that Nvidia paid US$500 million for a pre-funded warrant, in effect three million Corning shares.

Corning also gave Nvidia a second warrant, over 15 million shares at US$180, for no separate payment. The 10-Q values it at US$296 million and treats it as a payment to a customer. That amount comes off Corning's revenue as it delivers under the deal.

The same 10-Q books a US$1.0 billion customer deposit, running to the end of 2029, against that warrant. The 10-Q ties the deposit to the customer that received the warrant, and the 8-K shows that customer is Nvidia. The deposit, not the US$500 million, is what secures supply.

What changed my view was reading the 10-Q note for this initiation. It matters for the claim. Buyers are paying ahead, but the biggest one is also being paid, about 30 cents of warrant for each dollar of deposit. Scarcity is being shared, not kept. The piece and the claim stay exactly as published.

## What the market prices in, and where I differ

At US$159.37 Corning is worth about US$137 billion on 861 million shares. Net debt was US$5.9 billion at the end of June, so the enterprise value is about US$143 billion. The dividend of US$0.28 a quarter yields 0.7 per cent.

The price is 49.0 times my 2026 core earnings estimate of US$3.25, close to the US$3.28 consensus on Nasdaq.com. It is 36.5 times my 2027 estimate of US$4.37 and 29.4 times my 2028 estimate of US$5.41. On trailing GAAP earnings it is 73.5 times, as stockanalysis.com shows.

For scale, at the end of 2024 the shares cost 18.9 times the core earnings Corning went on to report for 2025. The market has re-rated Corning from a glass company to an AI supplier.

**Why a sold-out business sells shares.** On 11 September Corning set up an at-the-market programme with Goldman Sachs to sell up to US$2 billion of new shares over time. The prospectus gives general corporate purposes, including capital spending, debt repayment and buybacks. The shares fell 13.7 per cent on the next trading day.

Corning has not said why it needs the money. Its own figures answer the question well enough. Being sold out means the limit is factory space, and factories are paid for before they earn anything.

Capital spending was US$1.28 billion in 2025. Corning expects about US$2.0 billion in 2026, which puts the second half at about US$1.25 billion against US$0.75 billion in the first. That pays for three new plants under the Nvidia deal and the Meta and Amazon expansions in North Carolina.

Adjusted free cash flow was US$1.61 billion in the first half, but US$0.71 billion of that was net customer deposits and government incentives. Without them, free cash flow was about US$0.90 billion. Dividends took US$0.50 billion, and US$0.67 billion of debt falls due within a year.

None of this is distress. Corning has US$2.5 billion of cash and an undrawn US$1.5 billion credit line. Its debt is 39 per cent of capital, against a 60 per cent covenant ceiling. At today's price the full US$2 billion would be about 12.5 million shares, 1.5 per cent dilution.

So my answer is this. The programme is cheap insurance for a capital spending step-up that customer money only partly covers, raised while the shares trade at 49 times earnings. It is a sign that demand is real, and that meeting it is expensive. The 2027 spending plan, not yet given, is the number to watch.

**What the price needs.** By October 2027 the market will price 2028. At 27 times, the multiple I use below, US$159.37 needs 2028 core earnings of US$5.90 a share. That is above the US$5.64 consensus.

Holding the rest of Corning at my base case, that needs optical sales of about US$16.1 billion in 2028 at a 24 per cent margin. That is 2.6 times 2025, and 38 per cent a year from my 2026 estimate.

**Where I differ.** I do not differ on the mechanism. I differ on how much of the next two years the price already holds. I hold one part of Corning at my base case and swing the other from my bear case to my bull case.

Swinging optical moves my 2028 earnings by US$2.06 a share. Swinging the rest of Corning, display, phone glass, car filters and solar, moves them by US$0.52. Optical is now four times the bigger driver, and on my estimates it passes half of sales in 2028.

So this is now an optical stock, priced as one. At 43 times forward earnings on stockanalysis.com, it trades above the fibre and cable makers at about 23 times and Amphenol at 29 times. Yet more than half of today's sales are still display, phone, car and solar glass.

## Valuation, with the working

I value Corning on core earnings per share, twelve months out, so the year I value is 2028. I build sales in two parts: Optical Communications and the rest. Each part earns a segment net margin, and a corporate line of about US$0.16 billion a quarter comes off the total.

For the second half of 2026 I use optical sales of US$2.22 billion and US$2.36 billion, and the rest at US$2.73 billion and US$2.72 billion. That gives a third quarter at the US$4.95 billion middle of Corning's guide, and core earnings of US$0.87, inside its US$0.85 to US$0.89 range.

The share count starts at 875 million diluted. I assume half of the US$2 billion programme is sold by the 2027 average and all of it by 2028.

| | 2023 | 2025 | 2026 mine | 2027 mine | 2028 mine |
|---|---|---|---|---|---|
| Core sales, US$ billion | 13.58 | 16.41 | 19.11 | 23.04 | 26.84 |
| Of which optical | 4.01 | 6.27 | 8.50 | 11.47 | 14.34 |
| Optical segment net margin | 11.9% | 16.7% | 21.4% | 23.0% | 24.0% |
| Core earnings per share, US$ | 1.70 | 2.52 | 3.25 | 4.37 | 5.41 |
| Consensus, US$ | | | 3.28 | 4.29 | 5.64 |
| Price to earnings at US$159.37 | 93.7x | 63.2x | 49.0x | 36.5x | 29.4x |

The 2023 and 2025 figures are Corning's own. My 2028 sales of US$26.8 billion fall a little short of Corning's plan for a US$30 billion annual run-rate by the end of 2028.

**The multiple.** I use 27 times 2028 earnings for the base case. Prysmian, Fujikura and Sumitomo Electric, the fibre and cable makers, have a median of 23.5 times forward earnings. Amphenol is at 29.4 times. Corning earns a premium for its fibre know-how and customer contracts, but late-2027 earnings will still be half glass, phones and cars.

**Three cases, twelve months out.**

| Case | What happens | 2028 EPS | Multiple | Value | Change |
|---|---|---|---|---|---|
| Bear | Fibre loosens: optical grows 22% then 12%, margin 21% then 20%; rest grows 6% then 5% | US$3.89 | 22x | US$86 | down 46% |
| Base | Optical grows 35% then 25%, margin 23% then 24%; rest grows 9% then 8% | US$5.41 | 27x | US$146 | down 8% |
| Bull | Optical grows 45% then 32%, margin 24% then 25.5%; rest grows 12% then 10% | US$6.47 | 34x | US$220 | up 38% |

Weighted 25, 50 and 25 per cent, the cases give about US$149, 6 per cent below the price. The bear case is not a collapse in demand. Optical still grows by more than a third over two years. Prices and margins slip as new fibre capacity, Corning's and China's, catches up.

**How sensitive it is.** Each row is a 2028 estimate and each column a multiple.

| 2028 EPS | 22x | 27x | 32x |
|---|---|---|---|
| US$4.60 | US$101 | US$124 | US$147 |
| US$5.41 | US$119 | US$146 | US$173 |
| US$6.20 | US$136 | US$167 | US$198 |

Three of the nine cells sit above today's price. Each needs earnings above my base, a multiple above 27 times, or both.

**Peers.** Forward multiples from stockanalysis.com on 6 October: Sumitomo Electric 21.4 times, Prysmian 23.5, Fujikura 28.9 and Amphenol 29.4. The active optics makers trade higher: Coherent 35.4, Ciena 37.5 and Lumentum 50.1. Corning at 43.0 times is priced with the makers of the plugs, not the makers of the pipes.

<div class="charts-slot"></div>

## Risks, and what would change my view

**The upturn runs longer.** This is the bull case and the main risk to a no call. Corning says it could sell more if it could make more. If the new plants come on early and the margin keeps rising towards 25 per cent, 2028 earnings beat my base and the multiple holds.

**Fibre loosens.** This is the bear case, and the claim's own falsifier. Corning is expanding hard, and so are Fujikura, Prysmian and Chinese producers. A segment margin falling while sales rise would be the first sign, and the shares would fall faster than earnings.

**Buyers take a bigger share.** Long contracts steady volume but concentrate it. The Nvidia warrant shows the largest buyers can take part of the scarcity rent. Corning's 2026 annual report will show the new customer concentration figures.

**More shares.** The at-the-market programme is about 1.5 per cent dilution at today's price. Samsung Display holds 58 million Corning shares under a lock-up that expires in 2027, and can offer another 22 million to Corning in tranches through 2027. The Nvidia warrant adds 15 million shares above US$180.

**The rest of Corning.** Display, phone glass and solar are more than half of sales. Corning said on its July call that higher memory prices were a headwind for its glass. The solar ramp had a costly shutdown in the second quarter. The rest of Corning moves my value less than optical, but it is not nothing.

**What would change my view.** A price below about US$127 would put my base case 15 per cent above it and make this a call. So would fourth quarter results showing optical at US$2.4 billion or more in the quarter, at a margin of 23 per cent or more, with the share sale largely unused. A falling optical margin before mid-2027 would bring the bear case forward.

Corning reports third quarter results on Tuesday 27 October 2026, with a call at 8:30am Eastern time, as listed on its investor relations events page. The 10-Q that follows will show whether any shares were sold under the programme.

## Conclusion

The October piece argued that glass fibre is the part of the AI network that outlives every chip, and that Corning is paid each time a campus grows. Corning's own numbers back it: optical up 32 per cent, data centre up 65 per cent, and a record segment margin of 21 per cent. The share sale does not undercut the claim. It shows that being sold out costs money before it makes any.

The shares are the harder part. At US$159.37 they trade at 49 times my 2026 earnings and price optical sales of about US$16 billion in 2028. My call is no call, with medium conviction. My base case is worth about US$146, with a range from US$86 to US$220. I would revisit below about US$127, or on a fourth quarter showing optical at US$2.4 billion with a 23 per cent margin.

<p class="sources">Sources: Corning quarterly earnings releases furnished on Form 8-K, 30 April 2024 to 28 July 2026, for core sales, core earnings per share, segment sales and net income, margins, cash flow, capital spending and the third quarter 2026 guide. Corning Form 10-K for 2025, filed 12 February 2026, for segment sales, enterprise and carrier network sales, customer concentration and the Samsung Display share agreement. Corning Form 10-Q for the second quarter of 2026, filed 29 July 2026, for the customer deposit, the warrant accounting, contract liabilities, liquidity, the credit facility and the 2026 capital spending outlook. Corning 8-K and press release of 6 May 2026 on the Nvidia partnership and warrants. Corning 8-K and prospectus supplement of 11 September 2026 on the at-the-market programme. Corning second quarter 2026 earnings call of 28 July 2026 for Enterprise Networks sales and capacity commentary. Meta, Amazon and Verizon agreement announcements of 27 January, 8 June and 8 September 2026. Corning investor relations events page for the results date. Consensus earnings from Nasdaq.com (Zacks), and multiples and the average analyst target from stockanalysis.com, retrieved 6 October 2026. Share prices from Yahoo Finance, retrieved 6 October 2026. Estimates for 2026 to 2028 are the author's own. Personal research, not investment advice.</p>
