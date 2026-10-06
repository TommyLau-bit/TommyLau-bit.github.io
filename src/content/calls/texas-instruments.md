---
title: "Texas Instruments' data centre business is real. At US$295, the shares already pay for a full analog upturn as well."
summary: "Texas Instruments makes the cheap power chips that feed every AI processor, and its data centre sales doubled in a year. But data centre is still about an eighth of revenue. Most of the recent growth, and most of what could go wrong, is the ordinary analog cycle in factories and cars. At 35 times this year's earnings, the shares already price a long upturn on top of the AI story."
company: "Texas Instruments"
ticker: "TXN"
exchange: "Nasdaq"
claims: ["ti-feeds-the-chip"]
correction: "I called TI's 61 per cent gross margin what full factories look like. TI's factories are not full: loadings are still rising, and the margin sits seven points below 2022, mostly because depreciation has more than doubled."
keyPoints:
  - "Texas Instruments makes the small power chips that step electricity down to an AI processor. Its data centre sales doubled in a year, and on my working they reached about 12 per cent of revenue in the second quarter, up from 9 per cent for 2025."
  - "Data centre supplied about a third of TI's growth in that quarter. The rest came from the analog upturn in factories and cars, and that cycle moves my 2028 earnings two and a half times as much as data centre does."
  - "TI's six-year factory build is nearly done. Capital spending falls to US$2 to 3 billion in 2026 and free cash flow is recovering, but depreciation has more than doubled since 2022, so the margin now swings harder with the cycle."
  - "At US$294.90 the shares trade at 35 times my 2026 earnings and 29 times my 2027. At 25 times, the price needs 2028 revenue about 36 per cent above the 2022 peak."
  - "My call is no call: the base case is worth about US$280, and a turn in the analog cycle would cost more than continued strength would add."
files:
  pdf: "/research/2026-10-06_TexasInstruments_Initiation.pdf"
  xlsx: "/research/2026-10-06_TexasInstruments_Model.xlsx"
  thumb: "/research/2026-10-06_TexasInstruments_Initiation-p1.png"
  pages: 5
date: 2026-10-06T21:47:37+08:00
draft: false
call:
  direction: "NO CALL"
  price: 294.90
  priceDate: 2026-10-05
  currency: "US$"
  target: null
  horizon: "12 months, to October 2027"
  conviction: "Medium"
  revisitIf: "A price below about US$244, or data centre reaching 15 per cent of TI's revenue while industrial sales are still growing."
  wrongIf: "Full year 2027 revenue reaches US$26 billion or more with data centre above 15 per cent of it, or gross margin reaches 65 per cent or more in any quarter to June 2027, or the shares trade above US$340 by October 2027 without either."
charts:
  - id: datacentre
    title: "Data centre revenue by quarter, my estimate, US$ million"
    kind: bar
    prefix: "US$"
    unit: "m"
    labels: ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Data centre"
        values: [290, 331, 429, 450, 552, 662]
    note: "TI gives growth rates, not quarterly sizes. These figures are my derivation from them: about 12 per cent of revenue in the second quarter of 2026, against 9 per cent for 2025."
    source: "My estimates from TI earnings calls of 27 January, 22 April and 22 July 2026 (US$1.5 billion in 2025, about US$450 million in the fourth quarter, about 90 per cent growth in the first quarter of 2026, doubling and about 20 per cent sequential growth in the second)."
  - id: margin
    title: "Gross margin by quarter, per cent"
    kind: bar
    unit: "%"
    decimals: 1
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Gross margin"
        values: [57.2, 57.8, 59.6, 57.7, 56.8, 57.9, 57.4, 55.9, 58.0, 61.4]
    refs:
      - value: 68.8
        label: "2022 gross margin"
    note: "The margin has started to rise as loadings increase, but it is still seven points below 2022, when depreciation was less than half today's."
    source: "TI quarterly earnings releases, 23 April 2024 to 22 July 2026; 2022 from SEC XBRL company facts."
  - id: capex
    title: "Capital spending and depreciation, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 2
    labels: ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026 guide"]
    series:
      - name: "Capital spending"
        values: [0.85, 0.65, 2.46, 2.80, 5.07, 4.82, 4.55, 2.50]
      - name: "Depreciation"
        values: [0.71, 0.73, 0.76, 0.93, 1.18, 1.51, 1.92, 2.30]
    note: "About US$22 billion of factory spending from 2021 to 2026. Spending is falling back; the depreciation it created is not."
    source: "SEC XBRL company facts from TI Forms 10-K, 2019 to 2025; 2026 guide midpoints from the 2025 Form 10-K and the 27 January 2026 call."
  - id: revenue
    title: "Revenue, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 2
    labels: ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026E", "2027E", "2028E"]
    series:
      - name: "Revenue"
        values: [14.38, 14.46, 18.34, 20.03, 17.52, 15.64, 17.68, 22.04, 24.73, 26.35]
    note: "The last upturn peaked at US$20.0 billion in 2022 and fell 22 per cent over two years. 2026 to 2028 are my estimates."
    source: "SEC XBRL company facts from TI Forms 10-K; 2026E to 2028E are the author's own."
  - id: price
    title: "TXN share price, month-end close, US$"
    kind: line
    prefix: "US$"
    decimals: 2
    labels: ["Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
    series:
      - name: "Close"
        values: [152.71, 170.46, 160.12, 167.33, 174.21, 176.42, 195.01, 194.53, 203.81, 214.34, 206.57, 203.16, 201.03, 187.51, 184.61, 195.99, 179.70, 160.05, 182.85, 207.62, 181.06, 202.48, 183.73, 161.46, 168.27, 173.49, 215.55, 212.11, 194.14, 281.08, 305.68, 298.07, 275.74, 260.91, 280.09, 294.90]
    note: "The shares have risen 61 per cent since the end of September 2025, most of it after first quarter results in April."
    source: "Yahoo Finance monthly closes for Nasdaq: TXN, not adjusted for dividends, retrieved 6 October 2026. The last point is the close on 5 October 2026."
---

Texas Instruments closed at US$294.90 on 5 October 2026. The shares have risen 61 per cent in a year, much of it after first quarter results in April. They sit 12 per cent below their 52-week high.

On 2 October I argued that the move to 800 volt racks turns TI's small, cheap power chips into a growing data centre business. The claim is holding. Data centre revenue doubled in a year, and it is now the fastest-growing market TI reports.

The harder question is whether that business is big enough to matter to the shares. An earlier paper-portfolio read, written by Claude on 5 October and used here only as an input, said no. It called TI mostly an analog-cycle bet, with AI rack power too small a share of revenue to carry a thesis.

I tested that properly. It is half right. Data centre now matters to TI's growth. But the analog cycle still drives most of TI's earnings, and the share price already assumes that cycle runs a long way further. My call is no call.

## The thesis

Go back to the water main from the October piece. Water arrives at the street at a pressure that would blast a glass out of your hand. A row of cheap valves under the sink steps it down to the gentle, steady trickle the tap needs.

The AI processor is that tap, and TI makes many of the valves. They are power stages, converters, electronic fuses and hot-swap controllers. Each sells for cents or a few dollars. None works without the others.

**How big data centre has become.** TI first broke data centre out as its own market in its 2025 annual report. It was 9 per cent of revenue that year, about US$1.5 billion, up 64 per cent. TI said it left 2025 at about US$450 million a quarter.

Since then TI has given growth rates but no dollar figures. Data centre grew about 90 per cent in the first quarter of 2026. In the second quarter it doubled on a year earlier and grew about 20 per cent on the first quarter.

Those rates are enough to work out the size, within a margin. On my working, data centre was about US$660 million in the second quarter of 2026. That is about 12 per cent of TI's revenue of US$5.46 billion.

**What it adds to growth.** TI's revenue rose by about US$1.0 billion on a year earlier in that quarter. Data centre supplied about a third of the rise. Industrial, up about 30 per cent, supplied more. Automotive grew in the mid-teens and personal electronics was flat.

So data centre is no longer a rounding error in TI's growth. On my estimates it reaches about a fifth of revenue by 2028. That is more than the earlier read allowed for.

**Which racks it comes from.** The doubling so far comes from today's racks at 48 and 54 volts. In July TI said the 800 volt design will be phased in, and that more conversion stages mean more of its parts per rack. The claim's 800 volt mechanism is still ahead of TI's numbers, not behind them.

**The factory build.** TI spent about US$22 billion on capital projects from 2021 to 2026, counting the 2026 guide midpoint. The largest site is Sherman, Texas, where the first fab began production on 17 December 2025. TI says a chip made on a 300mm wafer costs about 40 per cent less than one made on 200mm.

Capital spending fell from US$4.55 billion in 2025 to an expected US$2 to 3 billion in 2026. CHIPS Act grants and tax credits return part of the rest. Free cash flow, in TI's definition, rose from US$1.5 billion in 2024 to US$6.5 billion in the twelve months to June 2026.

**Where I was wrong in October.** In the piece I called TI's 61 per cent gross margin what owning cheap, full factories looks like in money. TI's factories are not full. On the July call TI said loadings rose through the second quarter and were still rising into the third. It also said it has empty clean room space ready to equip. The piece also said the factories now had to be filled, so it contradicted itself.

The margin also sits well below its last peak. Gross margin was 68.8 per cent in 2022, on revenue of US$20.0 billion, about what TI earned in the year to June 2026. Most of the difference is depreciation, the annual charge for factories already built. It rose from US$0.93 billion in 2022 to US$1.92 billion in 2025, and TI expects US$2.2 to 2.4 billion in 2026.

What changed my view was putting the July call next to TI's depreciation line for this note. The point matters for the call. Partly filled factories mean the margin can still rise as they fill. But a larger fixed cost base also means earnings fall faster if the cycle turns. The piece and the claim stay exactly as published.

## What the market prices in, and where I differ

At US$294.90 TI is worth about US$271 billion on its 920 million diluted shares. Net debt was about US$7 billion at the end of June. That is before the US$7.5 billion purchase of Silicon Labs, which TI expects to close in the first half of 2027.

The price is 34.7 times my 2026 earnings estimate of US$8.50 a share. That estimate matches the stockanalysis.com consensus of US$8.49. It is 29.1 times my 2027 estimate of US$10.15, and 27.7 times the consensus of US$10.64.

The dividend, raised in September to US$1.52 a quarter, yields 2.1 per cent. On TI's own framework, my 2026 revenue of about US$22 billion implies free cash flow of about US$9.5 billion. That is about US$10.35 a share, a yield of 3.5 per cent, including CHIPS Act cash.

**What the price needs.** By October 2027 the market will price 2028. At 25 times, the multiple I use below, US$294.90 needs 2028 earnings of US$11.80 a share. On my margin bridge that needs 2028 revenue of about US$27.2 billion.

That is 36 per cent above TI's last peak of US$20.0 billion in 2022. It would also be the fourth straight year of growth. In the last cycle revenue grew two years running, then fell 22 per cent over the next two.

**Where I differ.** I agree data centre is a real, fast-growing business. Where I differ is on how much of the price it can carry. To test that, I hold one driver at my base case and swing the other from my bear case to my bull case.

Swinging data centre from 25 per cent growth to 60 per cent in 2027, and from 15 to 40 per cent in 2028, moves my 2028 earnings by US$1.58 a share. Swinging the rest of TI from an 8 per cent fall to 12 per cent growth in 2027 moves them by US$3.90. The cycle in factories, cars and phones is two and a half times the bigger driver.

So the earlier read was right about the stock. The AI exposure has grown faster than it assumed, but it does not decide the value. What decides it is whether industrial and automotive demand keeps rising into 2027 and 2028.

There is a second point. Industrial grew about 30 per cent on a year earlier in the second quarter. Part of that is customers restocking after two years of running inventories down, which tends to flatter one or two quarters. TI's own inventory fell from 222 days at the end of 2025 to 196 days in June, which shows demand catching up with its stock.

## Valuation, with the working

I value TI on earnings per share, twelve months out, so the year I value is 2028. TI itself targets free cash flow per share, so I cross-check against its free cash flow yield. Silicon Labs is left out until it closes.

I build revenue in two parts: data centre and the rest of TI. Operating profit rises by 75 per cent of each extra dollar of revenue, before depreciation, the middle of the 70 to 85 per cent TI gives. I then subtract extra depreciation of US$0.2 billion in 2027 and US$0.1 billion in 2028.

Other income less interest costs about US$0.3 billion a year, close to the second quarter's rate. Tax is 13 per cent, as TI guides, and the share count stays at 920 million. For the third quarter I use revenue of US$5.95 billion, which gives earnings at the US$2.40 midpoint of TI's guide.

| | 2022 | 2025 | 2026 mine | 2027 mine | 2028 mine |
|---|---|---|---|---|---|
| Revenue, US$ billion | 20.03 | 17.68 | 22.04 | 24.73 | 26.35 |
| Of which data centre | | 1.5 | 2.77 | 4.02 | 5.23 |
| Growth | | 13% | 25% | 12% | 7% |
| Operating margin | 50.6% | 34.1% | 41.9% | 44.7% | 46.2% |
| Earnings per share, US$ | 9.41 | 5.45 | 8.50 | 10.15 | 11.20 |
| Price to earnings at US$294.90 | 31.3x | 54.1x | 34.7x | 29.1x | 26.3x |

The 2022 and 2025 figures are TI's own. Data centre in 2025 is the figure TI gave on its January call. My 2027 earnings sit 5 per cent below the consensus.

**The multiple.** I use 25 times 2028 earnings for the base case. The six analog and power peers below trade at a median of 23.3 times forward earnings. TI earns a premium for its own factories, its free cash flow and 23 years of dividend increases. But 2028 would be late in an upturn, and the market rarely pays a top multiple for peak earnings.

**Three cases, twelve months out.**

| Case | What happens | 2028 EPS | Multiple | Value | Change |
|---|---|---|---|---|---|
| Bear | The upturn turns: rest of TI falls 8% then 2%; data centre grows 25% then 15% | US$7.66 | 22x | US$168 | down 43% |
| Base | The upturn matures: rest grows 7.5% then 2%; data centre 45% then 30% | US$11.20 | 25x | US$280 | down 5% |
| Bull | The upturn runs: rest grows 12% then 6%; data centre 60% then 40% | US$13.14 | 28x | US$368 | up 25% |

Weighted 25, 50 and 25 per cent, the three cases give about US$274, 7 per cent below the price. The bear case is still mild by TI's own history: revenue stays above 2025 and data centre keeps growing. It is a fall in earnings because the margin falls with volume across a larger cost base.

**How sensitive it is.** Each row is a 2028 estimate and each column a multiple.

| 2028 EPS | 21x | 25x | 29x |
|---|---|---|---|
| US$9.50 | US$200 | US$238 | US$276 |
| US$11.20 | US$235 | US$280 | US$325 |
| US$12.50 | US$262 | US$312 | US$362 |

Only three of the nine cells sit above today's price. To make money from here, TI needs earnings above my base and a multiple close to today's.

**Peers.** Forward multiples from stockanalysis.com on 6 October: Analog Devices 26.3 times, Infineon 24.5, onsemi 22.1, Microchip 20.7 and NXP 14.5. Monolithic Power, a power specialist with large AI server sales, trades at 46.1 times. TI at 30.5 times sits between the ordinary analog makers and the AI power specialist. That is the market already paying for part of the data centre story.

<div class="charts-slot"></div>

## Risks, and what would change my view

**The upturn runs longer.** This is the bull case and the main risk to a no call. Analog makers spent 2023 and 2024 running stock down, and restocking could last into 2027. With empty clean room space and falling capital spending, each extra dollar of revenue carries a high margin. TI also said on the July call that it had started raising prices, which builds through the second half. A gross margin of 65 per cent or more would be the clearest sign.

**The upturn turns.** This is the bear case. TI warns every quarter that demand can differ from forecasts. Industrial and automotive are two thirds of revenue, and the 30 per cent industrial growth will not repeat for long. The new fixed cost base makes the fall in earnings steeper than the fall in revenue.

**The data centre share is my estimate.** TI gives growth rates, not dollar sizes, each quarter. If the 2025 figure of US$1.5 billion or the quarterly rates are rounded differently, my 12 per cent could be a point or so out either way. The conclusion holds across that range.

**800 volt timing and rivals.** TI itself says the 800 volt design will be phased in. Infineon, Monolithic Power and Analog Devices compete for the same sockets, and the processor makers choose. Cheaper factories help most on simpler parts.

**Silicon Labs.** The purchase adds about US$0.8 billion of revenue and up to US$5 billion of new borrowing. TI expects it to add to earnings in the first full year, excluding deal costs. Integration and interest costs are not in my numbers.

**What would change my view.** A price below about US$244 would put my base case 15 per cent above it and make this a call. So would third quarter results showing data centre at 15 per cent or more of revenue while industrial still grows. In the other direction, a fall in industrial orders before mid-2027 would bring the bear case forward.

TI reports third quarter results on Wednesday 21 October 2026, with a call at 3:30pm Central time, as TI announced on 1 October.

## Conclusion

The October piece argued that the move to 800 volt racks turns TI's cheap power chips into a growing data centre business. TI's own numbers say the business is real and growing fast: doubled in a year, about 12 per cent of revenue on my working, a third of recent growth. That growth comes from today's racks, before 800 volts arrives.

The earlier read was still right about the shares. The analog cycle moves TI's earnings two and a half times as much as data centre does, and at US$294.90 the price already assumes a fourth straight year of growth. My call is no call, with medium conviction. My base case is worth about US$280, and the bear case loses more than the bull case gains. I would revisit below about US$244, or if data centre reaches 15 per cent of revenue while industrial still grows.

<p class="sources">Sources: Texas Instruments quarterly earnings releases furnished on Form 8-K, 23 April 2024 to 22 July 2026, for revenue, margins, earnings per share, depreciation, capital spending, cash flow, CHIPS Act proceeds, debt, cash and the third quarter 2026 guide. Texas Instruments Form 10-K for 2025, filed 6 February 2026, for revenue by market, the 300mm cost advantage and 2026 capital spending. Texas Instruments Form 10-Q for the second quarter of 2026 for Silicon Labs and its financing. SEC XBRL company facts for annual figures from 2019 to 2025. Texas Instruments earnings calls of 27 January, 22 April and 22 July 2026 for data centre size and growth, end-market growth, depreciation, loadings, fall-through, inventory days and the free cash flow framework. Texas Instruments announcements of 4 February 2026 on Silicon Labs, 17 September 2026 on the dividend and 1 October 2026 on the results date. Consensus and peer multiples from stockanalysis.com, retrieved 6 October 2026. Share prices from Yahoo Finance, retrieved 6 October 2026. The data centre quarterly sizes and all estimates for 2026 to 2028 are the author's own. Personal research, not investment advice.</p>
