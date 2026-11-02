---
title: "SK Hynix is sold as an HBM company. Nine tenths of its revenue is ordinary memory, and the price already assumes the worst."
summary: "SK Hynix leads the world in HBM, the memory stacked beside AI chips, and my October piece argued that HBM is becoming a part built to the buyer's design. On my estimates HBM is now only about a tenth of SK Hynix's revenue, because ordinary memory prices have risen far faster. At KRW 1,472,000 the shares trade at 2.8 times 2027 consensus earnings, and the price holds up only if the cash the shortage throws off is spent and earns nothing."
company: "SK Hynix"
ticker: "000660"
exchange: "KRX"
claims: ["memory-not-maths"]
keyPoints:
  - "SK Hynix makes DRAM, including HBM, the memory stacked beside AI chips, and NAND flash. Revenue in the third quarter of 2026 was KRW 104.6 trillion, 4.3 times a year earlier, at an 80 per cent operating margin."
  - "HBM made SK Hynix's name, but on my estimates it is now only about 11 per cent of 2026 revenue, against about 30 per cent in 2025. HBM prices are set a year ahead, while ordinary DRAM prices have soared. The earnings rest on the memory cycle, not on custom HBM."
  - "Custom HBM, the claim in my piece, decides how durable that tenth is. SK Hynix says custom HBM is growing in importance and it runs joint projects with major customers, but it has given no date for volume, so the claim is still open."
  - "At KRW 1,472,000 the shares trade at 2.8 times 2027 consensus earnings. On my method the price needs normal earnings worth a 12.4 per cent net margin if the cash is kept, about half SK Hynix's ten-year 23.5 per cent. Only if the cash is spent and earns nothing does the price look fair."
  - "My call is LONG, with medium conviction and a target of KRW 2,000,000. My base value is KRW 2,033,000, 38 per cent above the price, within a range of KRW 1,004,000 to KRW 3,484,000. The view is wrong if revenue and DRAM prices both fall on the quarter before by October 2027, or if SK Hynix returns less than half of its free cash flow."
files:
  pdf: "/research/2026-11-02_SKHynix_Initiation.pdf"
  xlsx: "/research/2026-11-02_SKHynix_Model.xlsx"
  thumb: "/research/2026-11-02_SKHynix_Initiation-p1.png"
  pages: 5
date: 2026-11-02T17:52:21+08:00
draft: false
call:
  direction: "LONG"
  price: 1472000
  priceDate: 2026-11-02
  currency: "KRW "
  target: 2000000
  horizon: "12 months, to October 2027"
  conviction: "Medium"
  wrongIf: "By October 2027, SK Hynix reports a quarter in which total revenue and DRAM average selling price both fall on the quarter before, which points to my bear case; or it returns less than half of its free cash flow to shareholders for 2026 or 2027, which turns the cash I count into the capital spending the price already assumes."
charts:
  - id: quarters
    title: "Revenue by quarter, KRW trillion"
    kind: bar
    prefix: "KRW "
    unit: "tn"
    decimals: 1
    labels: ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
    series:
      - name: "Revenue"
        values: [12.4, 16.4, 17.6, 19.8, 17.6, 22.2, 24.4, 32.8, 52.6, 79.3, 104.6]
    note: "Revenue rose more than fourfold in four quarters, mostly on price. The operating margin went from 47 per cent in the third quarter of 2025 to 80 per cent."
    source: "SK hynix preliminary results releases, 23 January 2025 to 28 October 2026; Form 6-K of 28 October 2026."
  - id: hbm
    title: "HBM against everything else, KRW trillion (my estimates for HBM)"
    kind: bar
    prefix: "KRW "
    unit: "tn"
    decimals: 1
    labels: ["2025", "2026E", "2027E"]
    series:
      - name: "HBM, my estimate"
        values: [28.8, 39.3, 46.3]
      - name: "Conventional DRAM, NAND and other"
        values: [68.3, 325.2, 493.7]
    note: "HBM grows every year, but ordinary memory grows far faster, so HBM falls from about 30 per cent of revenue in 2025 to about 11 per cent in 2026."
    source: "SK hynix does not disclose HBM revenue. My estimate: an industry HBM market of about US$35 billion in 2025 growing about 40 per cent a year (Micron, 17 December 2025), SK Hynix's share at 58, 55 and 50 per cent (IDC put it at 56.4 per cent in the first quarter of 2026, in SK Hynix's prospectus of 10 July 2026), at my average exchange rates. 2025 revenue reported; 2026 and 2027 totals are my estimates."
  - id: cycle
    title: "SK Hynix's net margin by year, per cent"
    kind: bar
    unit: "%"
    decimals: 0
    labels: ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
    series:
      - name: "Net margin"
        values: [17, 35, 38, 7, 15, 22, 5, -28, 30, 44]
    refs:
      - value: 23.5
        label: "2016 to 2025, all ten years"
      - value: 12.4
        label: "Normal margin the price needs, on my method"
    note: "Over the ten years to 2025 SK Hynix earned a 23.5 per cent net margin in all. The price needs a normal year at about half that."
    source: "SK hynix annual results releases for 2016 to 2020; stockanalysis.com (S&P Global) for 2021 to 2025, matching the prospectus of 10 July 2026. The reference lines are the author's."
  - id: price
    title: "SK Hynix share price, month-end close, KRW thousand"
    kind: line
    prefix: "KRW "
    unit: "k"
    decimals: 0
    labels: ["Sep 23", "Oct 23", "Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "Oct 26", "2 Nov 26"]
    series:
      - name: "Close"
        values: [115, 116, 134, 142, 135, 156, 183, 174, 189, 237, 195, 174, 175, 186, 160, 174, 199, 190, 191, 178, 205, 292, 274, 269, 348, 559, 530, 651, 909, 1061, 807, 1286, 2333, 2650, 1718, 1674, 1776, 1418, 1472]
    note: "The shares rose from KRW 519,000 on 25 November 2025 to a highest close of KRW 2,919,000 on 22 June 2026, and have since roughly halved."
    source: "KRX regular-session closes via Yahoo Finance, checked against stockanalysis.com, retrieved 2 November 2026. The last point is the close on 2 November 2026."
---

SK Hynix's shares closed at KRW 1,472,000 on 2 November 2026. In June they closed at KRW 2,919,000. In between, SK Hynix reported the first quarter in its history with revenue above KRW 100 trillion.

My piece of 31 October argued that memory, not maths, sets the pace of AI, and that from HBM4E the biggest buyer designs the bottom of the memory stack. SK Hynix is the largest maker of that memory, HBM, the towers stacked beside AI chips.

So the obvious reading is that SK Hynix is an HBM company, and custom HBM decides its future. The numbers say something different. HBM is now a small slice of the money, and the question for the shares is the ordinary memory cycle.

## The thesis

Go back to the kitchen from the piece. The chef is the AI chip and the hatch is the memory feeding it. SK Hynix stocks the pantry, and it built the best hatch in the business.

This year the pantry's ordinary goods, the flour and the oil, have become the scarce part. Their price has soared, while the hatch was sold a year ahead at last year's price. So the supplier now earns most of its money on flour.

**The pantry is full and the prices are high.** Revenue in the third quarter of 2026 was KRW 104.6 trillion, up 328 per cent on a year earlier. Operating profit was KRW 83.3 trillion, an 80 per cent margin, against 47 per cent a year before.

DRAM bits shipped rose about 10 per cent on the quarter, and DRAM prices rose by a high twenties percentage. NAND prices rose by a mid twenties percentage. For the fourth quarter SK Hynix guides DRAM bits up by a mid twenties percentage.

DRAM revenue in the first quarter of 2026 was KRW 40.7 trillion, 2.9 times a year earlier. Gartner, quoted in SK Hynix's prospectus, forecast conventional DRAM prices to roughly triple year on year by the second quarter.

**HBM is now a small slice.** SK Hynix does not report HBM revenue. Its last figure I could find is for the fourth quarter of 2024, when HBM was more than 40 per cent of DRAM revenue. It said HBM revenue more than doubled in 2025.

My estimate puts HBM at about KRW 28.8 trillion in 2025, 30 per cent of revenue. In 2026 it is about KRW 39 trillion of my KRW 364.5 trillion, or 11 per cent. In 2027 it is about 9 per cent.

I build it from the same industry path as my Micron note: about US$35 billion of HBM in 2025, growing about 40 per cent a year. I give SK Hynix 58, 55 and 50 per cent of it. IDC put its share at 56.4 per cent in the first quarter of 2026, as quoted in SK Hynix's US prospectus.

Two primary figures point the same way. The largest customer took 23.9 per cent of 2025 revenue; in the first quarter of 2026 the two largest took 14.8 and 12.4 per cent. Sales booked in China rose from 19.7 to 24.3 per cent of revenue.

So how much of the earnings rest on HBM? About a tenth of revenue, and less of profit. Micron said on 30 September that its 2027 HBM prices narrow "the gross margin gap with conventional DRAM", which means HBM earns the lower margin today. On my 60 per cent HBM margin, HBM is about 8 per cent of 2026 operating profit.

**Custom HBM decides how durable that slice is.** On 28 October SK Hynix's head of HBM sales said "we are seeing growing importance of custom HBM", optimised for each customer's systems. SK Hynix runs joint projects with major customers. HBM4E samples shipped in the second quarter.

SK Hynix's prospectus of 10 July 2026 defines custom HBM as integrating "certain functions of GPUs and ASICs into the HBM base die", and lists custom base die integration among its HBM4E work. None of that gives a date for volume, so the piece's claim, that two of the three makers ship custom HBM in volume by the end of 2027, is still open.

Is custom a moat or a capex trap? Both, for different halves of the business. A base die drawn by the buyer ties each stack to one customer's chip. That makes qualification slower to win and harder to lose, which protects the leader's tenth.

But the buyer owns the design, and Nvidia says NVHBM will be "available from multiple memory providers". The edge in pricing moves to the buyer, as the piece argued. For the other nine tenths, the risk is the old one: too many fabs.

**The cupboards are being doubled.** The prospectus says SK Hynix is "targeting to double our wafer production capacity within the next five years". It expects to invest about KRW 600 trillion in the Yongin complex, with a fourth fab's first cleanroom by 2033.

On 28 October SK Hynix said 2027 capital spending will "increase significantly" on 2026. It has long-term agreements with 14 customers covering more than half of its 2027 and 2028 capacity, generally for five years, with prices within an agreed range and safeguards such as deposits.

That is the capex trap in plain sight. The shortage throws off cash faster than ever, and the plan to spend it is larger than ever. What the shares are worth depends on which wins.

## What the market prices in, and where I differ

At KRW 1,472,000 SK Hynix is worth about KRW 1,038 trillion on 705.2 million shares, or about US$774 billion at KRW 1,341 to the dollar. That count is the 730.5 million shares issued less 25.3 million held in treasury; it matches the third quarter dividend of KRW 14.10 trillion at KRW 20,000 a share.

Net cash was KRW 98.7 trillion on 30 September. After the KRW 9.0 trillion of share purchases made in October, it is about KRW 127,000 a share, 9 per cent of the price.

The shares trade at 4.1 times my 2026 earnings and 2.8 times the 2027 consensus of KRW 527,160. They are 50 per cent below the June high. Samsung Electronics trades at 3.0 times its 2027 consensus and Micron at 5.0 times its fiscal 2027.

**The low multiple is not the point.** As in my Micron note, peak memory earnings are not a stream to capitalise. SK Hynix lost KRW 9.1 trillion in 2023, a year after record revenue. Over 2016 to 2025 it earned a 23.5 per cent net margin in all, with 38.4 per cent at the 2018 peak.

**So I value the cycle, not the year.** Value at October 2027 is the net cash then, plus the earnings above normal still to come, plus 12 times normal earnings. I use the method and the three normal-year cases of my Micron note, so the two notes can be read side by side.

**What the price needs.** By September 2027 I expect net cash of about KRW 338 trillion, or KRW 479,000 a share, before dividends and cancellations. On that, KRW 1,472,000 needs normal earnings of only about KRW 38,000 a share. That is a 12.4 per cent net margin on my normal revenue, about half of SK Hynix's ten-year margin.

**Where I differ.** The market does not believe the cash will reach holders. If the cash is spent and earns nothing, the price needs normal earnings of about KRW 83,900, a 27.4 per cent margin. That is close to my base of 30 per cent. So the price is roughly my base view with the cash thrown away.

I think that is too harsh. SK Hynix plans about KRW 100 trillion of shareholder returns for 2026, at least KRW 30 trillion in dividends and at least KRW 60 trillion in cancelled shares. It says it intends to return at least half of its free cash flow. On 5 November it cancels 23.7 million shares bought for KRW 40.0 trillion.

Even if only half the cash comes back, my base is about KRW 1,790,000, 22 per cent above the price. The variant view is not that HBM is a moat. It is that the cash is real and SK Hynix says at least half of it will come back.

One sign of the gap: on 30 October the Nasdaq-listed ADSs closed at US$149.21 for a tenth of a share. That is about 41 per cent above the Seoul close at the day's exchange rate. The prospectus warns that shares withdrawn from ADSs may not be deposited again, so the gap does not close freely.

## Valuation, with the working

All forecasts below are mine. Figures are in KRW trillion unless per share. I value operations: reported net profit swings with finance items, KRW 22.9 trillion of investment valuation losses and KRW 11.6 trillion of foreign exchange losses in the third quarter alone.

**2026.** The fourth quarter brings KRW 128 trillion of revenue at an 80 per cent operating margin; consensus implies about KRW 127 trillion. With reported profit for the first nine months, EPS is about KRW 359,600, in line with consensus.

**2027.** Revenue is KRW 540 trillion, 6.3 per cent below consensus, at a 76 per cent operating margin and a 22 per cent tax rate. EPS is KRW 453,900, 13.9 per cent below consensus. Bits grow by a mid twenties percentage, but I let prices ease and the stronger won take some of it.

**2028.** Revenue falls 10 per cent at a 68 per cent margin, as M15X and Yongin add supply: EPS KRW 365,500.

**Cash.** Fourth quarter free cash flow is about KRW 65 trillion and 2027's about KRW 257 trillion, after KRW 75 trillion of capital spending. I deduct the October purchases and the KRW 10 trillion of new purchases set aside for staff pay.

| | 2025 | 2026E | 2027E | 2028E | Normal year |
|---|---|---|---|---|---|
| Revenue | 97.1 | 364.5 | 540.0 | 486.0 | 215.7 |
| HBM, my estimate | 28.8 | 39.3 | 46.3 | | |
| HBM share of revenue | 30% | 11% | 9% | | |
| Operating margin | 48.6% | 77.9% | 76.0% | 68.0% | |
| Net margin | 44.2% | 69.6% | 59.3% | 53.0% | 30.0% |
| EPS, KRW | 60,378 | 359,567 | 453,948 | 365,548 | 91,784 |
| Consensus EPS, KRW | | 358,672 | 527,160 | | |
| P/E at KRW 1,472,000 | 24.4x | 4.1x | 3.2x | 4.0x | 16.0x |

**The base value.** Net cash at September 2027 adds KRW 479,300 a share. Earnings above normal, a quarter of 2027's excess, all of 2028's and half of it again in 2029, discounted at 10 per cent, add KRW 452,500. Twelve times normal EPS of KRW 91,800 adds KRW 1,101,400. Together they make KRW 2,033,000.

Normal revenue takes the four quarters to June 2026, the period nearest Micron's fiscal 2026, grows bits 20 per cent a year for four years, and settles revenue per bit at 55 per cent. That gives KRW 215.7 trillion, at a 30 per cent net margin.

**Three cases, twelve months out.**

| Case | What happens | 2027 EPS | Normal EPS | P/E on normal | Value | Change |
|---|---|---|---|---|---|---|
| Bear | Prices turn in 2027; 2028 revenue falls 35%; normal margin 19% | KRW 356,200 | KRW 42,300 | 10x | KRW 1,004,000 | down 32% |
| Base | Tight through 2028, half the excess in 2029; normal margin 30% | KRW 453,900 | KRW 91,800 | 12x | KRW 2,033,000 | up 38% |
| Bull | 2027 above consensus; shortage lasts to 2029; normal margin 40% | KRW 530,900 | KRW 155,800 | 14x | KRW 3,484,000 | up 137% |

Weighted 25, 50 and 25 per cent, the cases give about KRW 2,139,000, 45 per cent above the price. Unlike in my Micron note, the bear case also cuts 2027, because SK Hynix's year runs to December and its agreements set ranges, not fixed prices.

**The band.** I go long when my base value is at least 15 per cent above the price. At 38 per cent above, SK Hynix clears it. A target of KRW 2,000,000 rounds the base down.

**How sensitive it is.** Each row is the normal net margin and each column the multiple on normal earnings.

| Normal net margin | 10x | 12x | 14x |
|---|---|---|---|
| 22% | KRW 1,643,000 | KRW 1,778,000 | KRW 1,913,000 |
| 30% | KRW 1,850,000 | KRW 2,033,000 | KRW 2,217,000 |
| 38% | KRW 2,056,000 | KRW 2,288,000 | KRW 2,521,000 |

All nine cells sit above the price; the lowest is 12 per cent above. The grid holds the cash fixed. Take the cash away and the base falls to about KRW 1,554,000, 6 per cent above the price, which is why the cash is the call.

<div class="charts-slot"></div>

## Risks, and what would change my view

**The cycle turns early.** About nine tenths of revenue rides on ordinary DRAM and NAND prices that have soared in a year. Micron says server makers already use a "modestly lower rate of content growth" while supply is tight. If prices fall in 2027 my bear case applies, a 32 per cent fall.

**The capex trap.** SK Hynix aims to double wafer capacity in five years and to spend about KRW 600 trillion at Yongin. Samsung, Micron and Chinese makers have the same price signal. If spending runs ahead of the promised returns, the cash I count disappears, and the price is about fair.

**Custom HBM moves the edge to the buyer.** If Nvidia's NVHBM spreads, the buyer draws the base die and chooses among makers. My numbers already let SK Hynix's HBM share fall to half by 2027 as Samsung's HBM4 ramps. That would cost the most durable tenth of the business, not the bulk of it.

**The won.** Sales are in dollars. The won moved from KRW 1,538 to the dollar on 2 July to KRW 1,341 now. A stronger won cuts revenue in won and produced the third quarter's foreign exchange loss.

**Leakage.** About KRW 10 trillion of the new KRW 20 trillion buyback goes to staff pay, on top of profit sharing of 10 per cent of operating profit. I count it as a cost.

**What would change my view.** Back to no call: a price above about KRW 1,768,000, where my base would sit less than 15 per cent above it, with my numbers unchanged. Towards the bull case: SK Hynix confirming volume custom HBM shipments and long-term agreements covering more than half of 2029 capacity.

The view is wrong if, by October 2027, SK Hynix reports a quarter in which revenue and DRAM average selling price both fall on the quarter before. It is also wrong if it returns less than half of its free cash flow for 2026 or 2027.

SK Hynix cancels 23.7 million shares on 5 November 2026, and the third quarter dividend has a record date of 30 November. Fourth quarter results are expected in late January 2027, as in January 2026; SK Hynix has not confirmed the date. The first Yongin cleanroom opens in early 2027.

## Conclusion

My piece of 31 October argued that from HBM4E the biggest buyer designs the bottom of the memory stack. SK Hynix's own words since support the direction: custom HBM is growing in importance and joint projects are under way. The claim stays open until a maker reports volume.

The shares are a different question. HBM is about a tenth of SK Hynix's revenue now; the rest is an ordinary memory boom. At 2.8 times consensus 2027 earnings, the price already assumes that boom ends badly and the cash it throws off is spent for nothing. My base value is KRW 2,033,000, 38 per cent above the price, within a range of KRW 1,004,000 to KRW 3,484,000. My call is LONG, with medium conviction and a twelve-month target of KRW 2,000,000. Medium, not high, because nine tenths of the earnings ride on memory prices that can turn within a year, and the margin of safety is the cash, which SK Hynix must return rather than spend.

<p class="sources">Sources: SK hynix preliminary results releases of 23 January 2025 (as reprinted), 28 January 2026, 23 April 2026, 29 July 2026 and 28 October 2026, for quarterly revenue, operating profit, net profit, net cash, HBM statements, long-term agreements and the shareholder return plan. Form 6-K of 28 October 2026 for third quarter results; Forms 6-K of 26 and 28 October 2026 for the treasury share purchases and cancellation, the third quarter dividend and the new buyback. SK hynix third quarter 2026 earnings call, 28 October 2026, for bits, prices, the fourth quarter guide, custom HBM, non-operating items and capital spending. SK hynix prospectus (Form 424B4), 10 July 2026, for 2023 to 2025 and first quarter 2026 income statements, revenue by product, customer concentration, regional sales, share count, the ADS terms, the Yongin plan and the definition of custom HBM, with IDC market shares and Gartner forecasts as quoted there. SK hynix annual results releases for 2016 to 2020; stockanalysis.com (S&P Global) for 2021 to 2025 annual figures, consensus and the average target, retrieved 2 November 2026. Micron earnings call of 17 December 2025 and prepared remarks of 30 September 2026. Nvidia NVHBM blog, 26 August 2026. Share prices are KRX regular-session closes via Yahoo Finance, checked against stockanalysis.com, retrieved 2 November 2026; ADS prices from Nasdaq.com; KRW/USD is the Hana Bank notice rate of 2 November 2026 via Naver Finance. Estimates for the fourth quarter of 2026 to 2028, HBM revenue, normal earnings and the valuation are the author's own. Personal research, not investment advice.</p>
