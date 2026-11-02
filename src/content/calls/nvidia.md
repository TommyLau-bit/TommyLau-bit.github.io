---
title: "Nvidia already sells about twelve gigawatts of AI a year. The price assumes the power stops growing after 2027."
summary: "Nvidia makes the chips, racks and networks inside AI data centres, and its own filings now say that securing land, power and buildings is the next critical phase of the buildout. On Nvidia's own yardstick its revenue this year equips about 12 gigawatts of computers. Consensus needs half as much again next year, which the grid and equipment queues on this site make hard, but the price pays for only one more year of growth."
company: "Nvidia"
ticker: "NVDA"
exchange: "Nasdaq"
claims: ["contracted-energised-running", "memory-not-maths", "powering-the-rack", "the-plug-stays"]
keyPoints:
  - "Nvidia designs the chips, racks and networks inside AI data centres. Data Center revenue was US$89.0 billion in the quarter to 26 July 2026, up 117 per cent, and 92.5 per cent of the total."
  - "Its own filings now treat power as the constraint. Nvidia has guaranteed up to US$108.5 billion of land, power and building costs for customers, mostly for a 4.25 gigawatt campus in Ohio that OpenAI will lease, ready from 2028."
  - "Nvidia's own figures for that campus put about US$41 billion of its revenue on each gigawatt of computers. On that yardstick this year's revenue equips about 12 gigawatts, and the fiscal 2028 consensus needs about 51 per cent more, a pace the queues on this site make hard."
  - "I assume the gigawatts grow 20 per cent and then 15 per cent, so my fiscal 2028 earnings are 23 per cent below consensus. Yet at 16 times, the price needs fiscal 2029 earnings only 4 per cent above my fiscal 2028."
  - "My call is long, with low conviction and a target of US$245. My base value is US$244, 19 per cent above the price, within a range of US$114 to US$394. It is wrong if Data Center revenue falls on the quarter before, if gross margin drops below 70 per cent, or if Nvidia pays out on a guarantee."
files:
  pdf: "/research/2026-11-02_Nvidia_Initiation.pdf"
  xlsx: "/research/2026-11-02_Nvidia_Model.xlsx"
  thumb: "/research/2026-11-02_Nvidia_Initiation-p1.png"
  pages: 6
date: 2026-11-02T18:08:54+08:00
draft: false
call:
  direction: "LONG"
  price: 204.64
  priceDate: 2026-10-30
  currency: "US$"
  target: 245
  horizon: "12 months, to October 2027"
  conviction: "Low"
  wrongIf: "Data Center revenue falls from one quarter to the next in any quarter Nvidia reports before October 2027, which would show chips running ahead of the power to use them; or its non-GAAP gross margin falls below 70 per cent in any of those quarters; or Nvidia makes a payment under any of its land, power and shell guarantees."
charts:
  - id: datacenter
    title: "Data Center revenue by fiscal quarter, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 1
    labels: ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26", "Q1 FY27", "Q2 FY27"]
    series:
      - name: "Data Center"
        values: [22.6, 26.3, 30.8, 35.6, 39.1, 41.1, 51.2, 62.3, 75.2, 89.0]
    refs:
      - value: 108.0
        label: "Q3 FY27 guide, total revenue"
    note: "Data Center revenue has more than tripled in two years. The third quarter guide is for all of Nvidia's revenue, of which Data Center has lately been about 92 per cent."
    source: "Nvidia CFO commentaries, Q3 FY25 to Q2 FY27, with their comparative columns; outlook from the Q2 FY27 commentary of 26 August 2026."
  - id: gigawatts
    title: "Data Center revenue translated into gigawatts of IT load a year"
    kind: bar
    unit: " GW"
    decimals: 1
    labels: ["FY26 actual", "FY27 mine", "FY28 mine", "FY28 consensus", "FY29 mine"]
    series:
      - name: "Gigawatts of IT load"
        values: [6.0, 11.7, 14.0, 17.6, 16.1]
    note: "My arithmetic on Nvidia's own yardstick: about US$150 to 200 billion of revenue for 4.25 gigawatts at PORTS, set to fiscal 2029 and deflated by my assumed rises for earlier years. A yardstick, not a count."
    source: "Nvidia Q2 FY27 CFO commentary and Form 8-K of 17 August 2026; consensus revenue from stockanalysis.com, retrieved 2 November 2026; the rest my estimates."
  - id: price
    title: "Nvidia share price, month-end close, US$"
    kind: line
    prefix: "US$"
    decimals: 2
    labels: ["Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "30 Oct 26"]
    series:
      - name: "Close"
        values: [61.53, 79.11, 90.36, 86.40, 109.63, 123.54, 117.02, 119.37, 121.44, 132.76, 138.25, 134.29, 120.07, 124.92, 108.38, 108.92, 135.13, 157.99, 177.87, 174.18, 186.58, 202.49, 177.00, 186.50, 191.13, 177.19, 174.40, 199.57, 211.14, 200.09, 200.75, 220.78, 228.38, 204.64]
    note: "The shares closed at a high of US$239.24 on 6 October 2026 and fell 14.5 per cent by 30 October."
    source: "Nasdaq.com historical data, month-end closes, retrieved 2 November 2026. The last point is the close on 30 October 2026."
---

Nvidia's shares closed at US$204.64 on 30 October 2026, 14.5 per cent below their high of 6 October. At that price Nvidia is worth about US$4.93 trillion, 22 times this year's expected earnings.

The usual argument is about demand: whether the buyers of AI chips will keep spending. This note asks a narrower question, the one this site exists to ask. Can the buildings and the power be switched on fast enough to plug the chips in?

Nvidia now answers that question in its own filings. In August it said securing land, power and buildings "has become the next critical phase in the AI infrastructure buildout", and it began guaranteeing them for its customers. My answer is that power paces Nvidia's growth but does not end it, and the price assumes it ends.

## The thesis

Go back to the housing estate in my piece on how AI capacity arrives. Houses are sold off plan, built, connected to the mains, handed over and lived in. Nvidia sells the furniture. For three years every house came with a removal van booked, so the furniture maker's sales grew as fast as it could make sofas.

Now the houses are the slow part. The four claims this note rests on all point to the same place. Nvidia has bought its inputs years ahead, it sets the designs its suppliers build to, and what it cannot buy is a switched-on hall.

**The chips now wait on the plug.** Nvidia's annual report for the year to 25 January 2026 lists whether customers can find enough data centre capacity "or energy" among the things that move its demand. By August it had gone further. In its 10-Q it says it now helps "select customers" secure the land, power, buildings and data centre capacity they need to grow.

The largest is in Ohio. On 17 August Nvidia guaranteed leases for about 4.25 gigawatts of IT load at SB Energy's PORTS campus, which OpenAI will rent and fill only with Nvidia systems. The guarantees are capped at US$105 billion and take effect as halls become ready, from 2028. With US$3.5 billion of smaller guarantees for AI clouds, Nvidia now stands behind up to US$108.5 billion of its customers' buildings.

That is the stage my piece called the last one a builder controls: energised power. The chip maker has started paying to hurry it.

**Nvidia's revenue, in gigawatts.** Nvidia gave the yardstick itself. Each generation of its systems at PORTS "could represent approximately 1.5 million NVIDIA GPUs, or approximately $150 billion to $200 billion in NVIDIA revenue". Over 4.25 gigawatts that is about US$35 billion to US$47 billion of Nvidia revenue per gigawatt of computers. It is about 9 to 14 times the US$3.25 million to US$3.75 million a megawatt that Vertiv puts on its own power and cooling gear, as the rack piece records.

The PORTS halls are ready from 2028, so I set the US$41 billion midpoint to fiscal 2029. Revenue per gigawatt rises with each generation, so I deflate it by my own assumptions for earlier years: US$37 billion in fiscal 2028 and US$33 billion in fiscal 2027. On my estimate of US$379 billion of Data Center revenue this fiscal year, that is about 11.7 gigawatts of IT load in one year. Even on the undeflated PORTS range it is 8 to 11 gigawatts.

Set that against what the site has measured. Texas has been asked for 474 gigawatts of connections and had cleared 6.6 gigawatts to the last step by August. GE Vernova, the largest maker of gas turbines, ships about 20 gigawatts a year in all, and its heavy turbines are largely sold out to 2030. Nebius expects 5 gigawatts contracted at the end of 2026 against at most 1 gigawatt connected. The grid makers each hold one to four years of orders.

**What consensus needs.** The fiscal 2028 consensus is US$692 billion of revenue. Less my US$33 billion for edge devices, that is about US$659 billion of Data Center revenue. Even with revenue per gigawatt up 15 per cent, it needs about 51 per cent more gigawatts equipped than this year: roughly 17.6 against 11.7.

I assume 20 per cent in fiscal 2028 and 15 per cent in fiscal 2029. That is faster than the equipment makers are adding factories, because energised halls stand partly idle. Malaysia's data centres drew 1.26 of the 5.65 gigawatts they had booked in June, and buyers keep adding power of their own. It is far slower than consensus. My estimate is my judgement, not a figure anyone publishes, and it is the number the call turns on.

**The other three claims say Nvidia holds the rest of the chain.** On memory, Nvidia's commitments to suppliers rose from US$119 billion to US$279 billion in one quarter, "primarily related to the procurement of memory", with US$87 billion due in fiscal 2028. Its NVHBM design, announced on 26 August, puts Nvidia's own controller in the base of each memory stack, "available from multiple memory providers". Nvidia draws the part and chooses the maker.

On power inside the rack, Nvidia sets the 800 volt design and dates its power rack to the second half of 2026 and its row power centre to 2027, with the building step undated. Rack first means new racks can go into halls whose power rooms already exist, which helps refits more than new halls. On the network, Nvidia's own Vera Rubin blueprints still specify pluggable switches. Its networking was US$14.8 billion of US$75.2 billion of Data Center revenue in the quarter to April, the last quarter it split the two.

Each of the four claims holds on Nvidia's filings and releases.

## What the market prices in, and where I differ

At US$204.64 Nvidia is worth about US$4.93 trillion on 24.1 billion shares, with US$23.2 billion more cash and debt securities than debt. It trades at 22 times my fiscal 2027 earnings of US$9.32 a share, which match the US$9.31 consensus. On the fiscal 2028 consensus of US$15.91 it trades at 12.9 times. The stockanalysis.com forward multiple is 16.9 times.

A multiple of 12.9 times the next year's consensus is low for a company still doubling its main business. The market is telling you it does not believe the consensus will last. It does not say why, and I think the physical layer is the honest reason.

**Where I differ from consensus.** Consensus needs the gigawatts equipped with Nvidia systems to rise about half in one year. On the queues this site documents, I do not believe that. My fiscal 2028 revenue is US$556 billion, 20 per cent below consensus, and my earnings are US$12.25 a share, 23 per cent below.

**Where I differ from the price.** By October 2027 the market will be pricing the year to January 2029. At 16 times, about today's forward multiple rounded down, US$204.64 needs fiscal 2029 earnings of US$12.79. If the gigawatts and the revenue per gigawatt both stopped rising after fiscal 2028, my model gives US$12.24. So the price assumes roughly that growth stops after next year.

The physical layer says growth slows, not that it stops. Equipment makers are adding plants, Nvidia is paying to bring 4.25 gigawatts of halls forward, and each new generation earns more per gigawatt. My base is below consensus on pace and above the price on duration.

**The obvious objection** is that the price is low for a different reason: that chips are already shipping ahead of the power to run them. There are signs that fit. Accounts receivable reached US$63.1 billion in July, 60 days of sales against 45 a quarter earlier, because of "extended payment terms on large, multi-quarter agreements". The 10-Q says such terms run from 90 days up to a year, to help customers with large data centre builds. If chips are reaching halls that are not yet energised, a pause follows. That is my bear case, and it is why the first test of the call is a quarter of falling Data Center revenue.

## Valuation, with the working

I value Nvidia on earnings per share. It holds more cash than debt, and its profit converts largely into cash. From fiscal 2027 Nvidia's non-GAAP earnings include pay in shares, so they no longer leave out that cost. The target looks twelve months out, so I value fiscal 2029, the year to January 2029.

Revenue in my model is gigawatts equipped times revenue per gigawatt, plus edge devices. Fiscal 2027 is two reported quarters, the US$108 billion third quarter guide at 74 per cent gross margin and US$9.0 billion of costs, and my US$122 billion fourth quarter. The estimates after that are mine.

| US$ billion unless stated | FY25 | FY26 | FY27 mine | FY28 mine | FY29 mine |
|---|---|---|---|---|---|
| Data Center revenue | 115.2 | 193.7 | 379.3 | 523.4 | 662.1 |
| Total revenue | 130.5 | 215.9 | 407.8 | 556.4 | 699.1 |
| Gigawatts of IT load equipped | | 6.0 | 11.7 | 14.0 | 16.1 |
| Non-GAAP operating margin | | | 65.9% | 63.0% | 62.0% |
| EPS, US$ (GAAP to FY26) | 2.94 | 4.90 | 9.32 | 12.25 | 15.26 |
| Consensus EPS, US$ | | | 9.31 | 15.91 | |
| P/E at US$204.64 | | 41.8x | 22.0x | 16.7x | 13.4x |

The margin falls in my model because memory, which Nvidia is buying in bulk, is rising in price, and the third quarter guide already steps down a point to 74 per cent. Non-GAAP earnings per share for fiscal 2025 and 2026, before stock-based pay was included, were US$2.99 and US$4.77.

**The multiple.** I use 16 times fiscal 2029 earnings, about today's 16.9 times forward multiple. Broadcom trades at 18.7 times, TSMC at 19.1, Marvell at 34.8 and AMD at 45.2; Micron's 5.0 reflects peak memory earnings. The five-peer median is 19.1 times. Nvidia at 16 does not need a premium.

**Three cases, twelve months out.**

| Case | What happens | GW FY28, FY29 | FY29 EPS | Multiple | Value | Change |
|---|---|---|---|---|---|---|
| Bear | Chips outrun the power; growth stalls | +5%, flat | US$10.34 | 11x | US$114 | down 44% |
| Base | Power paces growth | +20%, +15% | US$15.26 | 16x | US$244 | up 19% |
| Bull | Consensus pace arrives | +50%, +30% | US$21.89 | 18x | US$394 | up 93% |

Revenue per gigawatt rises 10 and 5 per cent in the bear case and 15 and 10 per cent in the other two. The bull case gives fiscal 2028 earnings of US$15.35, close to the consensus. Weighted 25, 50 and 25 per cent, the three give about US$249, 22 per cent above the price.

**How sensitive it is.** Each row is fiscal 2028 growth in gigawatts, with fiscal 2029 held at 15 per cent; each column is a multiple.

| FY28 GW growth | 12x | 16x | 20x |
|---|---|---|---|
| +10% | US$169 | US$225 | US$281 |
| +20% | US$183 | US$244 | US$305 |
| +35% | US$205 | US$273 | US$341 |

Seven of the nine cells sit above the price and five by more than 15 per cent. The two below it both need the multiple to fall to 12 times, with growth of 20 per cent or less. At 12 times even 35 per cent growth only matches the price.

<div class="charts-slot"></div>

## Risks, and what would change my view

**Chips outrun the power.** If buyers have taken systems they cannot yet switch on, orders pause until halls catch up. Longer payment terms and higher receivables fit that story, though they prove nothing yet. This is the bear case, a 44 per cent fall.

**The guarantees.** Nvidia stands behind up to US$108.5 billion of buildings, 4.7 times its net cash. For the Ohio guarantees OpenAI has agreed to reimburse Nvidia for any payment, so the exposure is to OpenAI's ability to pay. Nvidia also has US$36 billion of AI cloud agreements and US$20 billion of leases it expects to hand to others.

**Concentration and custom chips.** One direct customer took 16 per cent of revenue in the July quarter. Every large buyer designs its own chips too; my Broadcom note found custom accelerators were 73 per cent of Broadcom's AI revenue.

**Memory and margin.** Commitments of US$279 billion, mostly memory, lock in costs as prices rise. A gross margin below 70 per cent would mean Nvidia cannot pass them on, which is a test of the call.

**China.** Nvidia's guides assume no Data Center compute revenue from China. Any licence would be upside I do not count.

**What would change my view the other way.** Faster power: a quarter in which a grid operator or equipment maker shows the queues shortening, or Nvidia reporting the first PORTS halls early, would move the base towards the bull case.

The third quarter results are due on 17 November 2026, against a guide of US$108.0 billion. After that come the fourth quarter results and annual report, expected around late February 2027, GTC in March 2027 and the first PORTS halls from 2028.

## Conclusion

The pieces this note rests on argue that power, not chips, sets the pace of AI. Nvidia's own filings now agree: it lists energy among its demand risks, and it has begun guaranteeing its customers' land, power and buildings. On its own PORTS yardstick, its revenue already equips about 12 gigawatts of computers a year, and consensus needs half as much again next year.

I do not believe the consensus pace, and my fiscal 2028 earnings are 23 per cent below it. But the price goes further and assumes growth ends after next year. My call is LONG, with low conviction and a twelve-month target of US$245, about 16 times my fiscal 2029 estimate and 20 per cent above the price. Low, because the gigawatt growth is my judgement, the bear case is a 44 per cent fall and results land within weeks. The call is wrong if Data Center revenue falls on the quarter before, if gross margin drops below 70 per cent, or if Nvidia pays on a guarantee.

<p class="sources">Sources: Nvidia CFO commentaries for the third quarter of fiscal 2025 to the second quarter of fiscal 2027, with their comparative columns, for revenue, Data Center and sub-market revenue, non-GAAP margins and earnings, commitments, guarantees, balance sheet and the third quarter outlook. Nvidia Form 10-K for the year to 25 January 2026, filed 25 February 2026, for memory suppliers and demand risk factors. Nvidia Form 10-Q for the quarter to 26 July 2026, filed 26 August 2026, for the balance sheet, shares outstanding, payment terms, customer concentration, Vera Rubin production shipments and the SB Energy guarantees. Nvidia Form 8-K of 17 August 2026 on the PORTS campus. Nvidia release of 28 October 2026 on the results date. Nvidia blogs of 11 August 2026 (800 VDC) and 26 August 2026 (NVHBM), and the DGX SuperPOD Vera Rubin reference architectures of 15 September 2026, as cited in the journal pieces. Consensus, average target and forward multiples from stockanalysis.com and share prices from Nasdaq.com, all retrieved 2 November 2026. Gigawatt translations and all estimates for fiscal 2027 to 2029 are the author's own. Personal research, not investment advice.</p>
