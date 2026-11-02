---
title: "Samsung Electronics is a memory company with a phone maker attached, and its price assumes the memory cash never leaves the group."
summary: "Samsung Electronics makes memory, phones, TVs, displays and chips for others, but its chip division, almost all of it memory, earned 98 per cent of operating profit in the first nine months of 2026. HBM, the memory stacked beside AI chips, is only about 6 per cent of its memory sales on my estimates. At KRW 229,000 the common shares trade at 3.0 times 2027 consensus earnings, and on my sum of the parts the price holds up only if the cash the shortage throws off stays inside the group."
company: "Samsung Electronics"
ticker: "005930"
exchange: "KRX"
claims: ["memory-not-maths"]
keyPoints:
  - "Samsung Electronics is now a memory company with a phone maker attached. In the third quarter of 2026 memory sales were KRW 140.7 trillion of KRW 195.3 trillion, and the chip division earned KRW 106.5 trillion of the KRW 107.4 trillion operating profit."
  - "HBM is a small slice. On my estimates it is about 6 per cent of 2026 memory sales, even though Samsung says its 2027 HBM is sold out and it ships HBM4 for Nvidia's Vera Rubin."
  - "Samsung is the only HBM maker that builds the base die, the logic chip under each stack, in its own foundry. That is an edge while the maker designs the die; if the buyer designs it, as Nvidia's NVHBM does, the edge narrows. Samsung expects custom HBM samples only in 2027."
  - "At KRW 229,000 the common shares trade at 3.0 times 2027 consensus. On my sum of the parts, after a 20 per cent conglomerate discount, the price needs memory to earn a normal net margin of only 15 per cent if the cash is counted, half my base of 30 per cent."
  - "My call is long, with low conviction, and a target of KRW 270,000. My base value is KRW 278,700, 22 per cent above the price, within a range of KRW 156,200 to KRW 450,200. The preferred shares, at a 22.7 per cent discount, carry the same dividend."
files:
  pdf: "/research/2026-11-02_SamsungElectronics_Initiation.pdf"
  xlsx: "/research/2026-11-02_SamsungElectronics_Model.xlsx"
  thumb: "/research/2026-11-02_SamsungElectronics_Initiation-p1.png"
  pages: 6
date: 2026-11-02T18:20:21+08:00
draft: false
call:
  direction: "LONG"
  price: 229000
  priceDate: 2026-11-02
  currency: "KRW "
  target: 270000
  horizon: "12 months, to October 2027"
  conviction: "Low"
  wrongIf: "By October 2027, Samsung reports a quarter in which memory sales fall on the quarter before while DRAM prices also fall, which points to my bear case; or the 2026 shareholder return it finalises in late January 2027 comes in below KRW 90 trillion, the bottom of its own range, which says the cash I count stays inside the group."
charts:
  - id: profit
    title: "Operating profit by quarter: chips against everything else, KRW trillion"
    kind: bar
    prefix: "KRW "
    unit: "tn"
    decimals: 1
    labels: ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
    series:
      - name: "Device Solutions (memory, foundry, System LSI)"
        values: [1.1, 0.4, 7.0, 16.4, 53.7, 89.2, 106.5]
      - name: "Phones, TVs, appliances, display and Harman"
        values: [5.6, 4.3, 5.2, 3.7, 3.5, 0.3, 0.9]
    note: "The chip division went from a sixth of operating profit in the first quarter of 2025 to 99 per cent in the third quarter of 2026. Memory was KRW 140.7 trillion of the division's KRW 147.1 trillion of sales."
    source: "Samsung Electronics earnings call decks, 1Q 2026 to 3Q 2026 and 4Q 2025, segment appendix. The second series is total operating profit less Device Solutions."
  - id: squeeze
    title: "Phones pay for the memory: MX and Networks operating profit, KRW trillion"
    kind: bar
    prefix: "KRW "
    unit: "tn"
    decimals: 1
    labels: ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26"]
    series:
      - name: "MX and Networks operating profit"
        values: [4.3, 3.1, 3.6, 1.9, 2.8, -0.7, -0.6]
    note: "Phone sales rose on the year in the third quarter, but the division lost money for the second quarter running, which Samsung put down to cost pressures. Samsung expects high raw material prices to persist into 2027."
    source: "Samsung Electronics earnings call decks, 4Q 2025 to 3Q 2026; 3Q 2026 earnings call, 29 October 2026."
  - id: parts
    title: "Sum of the parts at October 2027, KRW thousand per share (my estimates)"
    kind: bar
    prefix: "KRW "
    unit: "k"
    decimals: 0
    labels: ["Net cash, Sep 2027", "Memory above normal", "Memory, 12x normal", "Phones, TVs, display, Harman", "Foundry and LSI", "Investments", "Less 20% discount"]
    series:
      - name: "Value per economic share"
        values: [79, 67, 164, 21, 6, 11, -70]
    refs:
      - value: 229
        label: "Common share price, 2 November 2026"
    note: "The parts add to KRW 348,400 a share before the discount and KRW 278,700 after it. Memory, at normal and above, is two thirds of the gross value."
    source: "Author's estimates from the model; balance sheet and segment history from Samsung Electronics earnings call decks."
  - id: price
    title: "Share prices, common and preferred, month-end close, KRW thousand"
    kind: line
    prefix: "KRW "
    unit: "k"
    decimals: 0
    labels: ["Sep 23", "Dec 23", "Mar 24", "Jun 24", "Sep 24", "Dec 24", "Mar 25", "Jun 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "Oct 26", "2 Nov 26"]
    series:
      - name: "Common (005930)"
        values: [68.4, 78.5, 82.4, 81.5, 61.5, 53.2, 57.8, 59.8, 83.9, 107.5, 100.5, 119.9, 160.5, 216.5, 167.2, 220.5, 317.0, 334.0, 262.5, 260.0, 268.5, 225.0, 229.0]
      - name: "Preferred (005935)"
        values: [54.5, 62.3, 68.0, 63.6, 50.9, 44.2, 47.2, 49.5, 66.4, 84.4, 75.0, 89.2, 117.4, 143.8, 114.0, 158.3, 202.5, 212.0, 191.0, 186.5, 195.2, 174.1, 177.0]
    note: "The common shares rose from KRW 94,800 on 21 November 2025 to a highest close of KRW 362,500 on 18 June 2026. The preferred discount widened from 16.9 per cent at the end of 2024 to 22.7 per cent."
    source: "KRX closes via Naver Finance to August 2026 and stockanalysis.com from September 2026, retrieved 2 November 2026."
---

Samsung Electronics' common shares closed at KRW 229,000 on 2 November 2026. In June they closed at KRW 362,500. In between, Samsung reported the first quarter in its history with operating profit above KRW 100 trillion.

My piece of 31 October argued that memory, not maths, sets the pace of AI. From HBM4E, it said, the biggest buyer designs the bottom of the memory stack. Samsung is one of the three makers of that memory, HBM, and the only one with its own logic foundry.

So the obvious reading is that Samsung is an AI conglomerate, and HBM decides its future. The numbers say something narrower. Samsung is now a memory company with a phone maker attached, and HBM is a small slice of the memory.

## The thesis

Go back to the kitchen from the piece. The chef is the AI chip and the hatch is the memory feeding it. Samsung stocks the pantry, builds hatches, and also runs a restaurant chain that buys its own flour.

This year flour became the scarce part. The pantry earns a fortune, the restaurants pay more for every loaf, and the hatch, sold a year ahead, is a small line in the books.

**The pantry is the company.** Third quarter revenue was KRW 195.3 trillion, up 127 per cent on a year earlier. Operating profit was KRW 107.4 trillion, a 55 per cent margin. Memory sales were KRW 140.7 trillion, and the chip division, Device Solutions, earned KRW 106.5 trillion.

In the first nine months of 2026 the chip division earned 98 per cent of the group's operating profit. In the first nine months of 2025 it earned 36 per cent.

The driver is price. In the third quarter DRAM bits rose by a low to mid single digit percentage on the quarter, and DRAM prices by about 20 per cent. NAND prices rose by a high teens percentage. For the fourth quarter Samsung guides DRAM bits up by a mid to high teens percentage.

**The restaurants pay for the flour.** Phones and networks, the MX division, lost KRW 0.6 trillion in the third quarter on KRW 37.7 trillion of sales, its second loss in a row. Samsung blamed cost pressures and expects high raw material prices to persist into 2027. TVs and appliances lost KRW 0.2 trillion.

So Samsung is paid twice for the shortage and charged once. The charge is small: against a year earlier, the consumer businesses lost about KRW 4 trillion of quarterly profit, while the chip division gained about KRW 100 trillion.

**HBM is a small slice.** Samsung does not report HBM revenue. It said in February that HBM sales would more than triple in 2026. In the third quarter HBM4 sales rose more than threefold on the quarter, to 60 per cent of HBM sales.

Samsung also says its 2027 HBM supply is already sold out, at prices agreed with customers. It began volume sales of HBM4 for Nvidia's Vera Rubin platform in the first quarter, so Samsung is now qualified at Nvidia.

My estimate puts Samsung's HBM at about KRW 9.6 trillion in 2025 and KRW 32 trillion in 2026. That is about 6 per cent of my KRW 506 trillion of 2026 memory sales, and about 4 per cent in 2027.

Here my notes do not fully agree, and I say so. IDC, as quoted in SK Hynix's US prospectus, put Samsung's HBM share at 19.3 per cent in 2025 and 20.5 per cent in the first quarter of 2026. It put SK Hynix at 63.2 and 56.4 per cent, and Micron at 17.4 and 23.1 per cent.

I start from IDC's 2025 share. If Samsung's HBM sales more than triple, as it said, it takes about 44 per cent of a US$49 billion market in 2026, the path in my Micron note. My SK Hynix note gives SK Hynix 55 per cent of that 2026 market, and my Micron note implies about a fifth for Micron.

Those 2026 shares sum to more than the whole. Samsung also says its HBM share in the third quarter of 2026 was in line with its DRAM share. Either the 2026 market is larger than US$49 billion, or SK Hynix's share falls faster than my SK Hynix note assumes. No maker discloses HBM revenue, so I cannot settle it. On any of these, HBM is a small part of Samsung's money.

**The base die is Samsung's real difference.** HBM4's base die, the logic chip under each stack, is made the way processors are made. Samsung builds its own on a 4 nanometre process in its own foundry. Its foundry credited improving results to base die demand in the second quarter and base die sales growth in the third.

SK Hynix said in April 2024 that it would use TSMC's logic process for HBM4's base die. Micron makes its HBM4 base die in house, but said on 23 September 2025 that it is partnering with TSMC to make its HBM4E base die. So from HBM4E, Samsung is the only one of the three that keeps the whole stack under one roof.

**Micron says so in its own words.** In Micron's prepared remarks for its call of 23 September 2025, Sanjay Mehrotra said: "We are partnering with TSMC for manufacturing the HBM4E base logic die". That covers standard and custom products alike. It supports the piece's point that the base die moves to logic foundries, and it sharpens Samsung's difference.

**Custom HBM cuts both ways for Samsung.** While the maker designs the base die, one roof is an edge: memory, logic and packaging in one company. When the buyer designs it, as Nvidia's NVHBM does, the buyer also has a say in where it is made. Nvidia's chips are made at TSMC. That is my reading, not anything Samsung or Nvidia has said.

Samsung said in February that "custom HBM samples will start reaching customers in 2027". It plans mass production of HBM4E in the first half of 2027. So Samsung is unlikely to say it ships custom HBM in volume by the end of 2027. The piece's claim needs two of three makers, so it now rests mainly on SK Hynix and Micron.

## What the market prices in, and where I differ

At KRW 229,000 the common shares and KRW 177,000 the preferred value Samsung at about KRW 1,450 trillion, or US$1,080 billion at KRW 1,341.70 to the dollar. I count about 5,710 million common and 802 million preferred shares, from the half-year report and the October buyback report.

The common shares trade at 5.1 times my 2026 earnings and 3.0 times the 2027 consensus of KRW 75,630. SK Hynix trades at 2.8 times its 2027 consensus and Micron at 5.0 times its fiscal 2027. The common shares are 37 per cent below their June high.

Net cash was KRW 197.6 trillion on 30 September. After the KRW 30.0 trillion third quarter dividend, already declared, and about KRW 2.5 trillion of October buybacks, it is about KRW 165 trillion.

**The low multiple is not the point.** As in my Micron and SK Hynix notes, peak memory earnings are not a stream to capitalise. Samsung's chip division lost KRW 14.9 trillion in 2023. From 2017 to 2025 it earned a 23.8 per cent operating margin in all.

**So I value the cycle, and the conglomerate around it.** For memory I use the same method and normal cases as my other two memory notes. Value at October 2027 is the net cash then, plus memory earnings above normal still to come, plus 12 times normal memory earnings. To that I add the other businesses at modest multiples, and take 20 per cent off the whole.

**What the price needs.** By September 2027 I expect net cash of about KRW 514 trillion, or KRW 79,000 a share, before distributions. With no discount, the market value needs normal memory earnings of only KRW 10 trillion after tax. That is a 3.5 per cent net margin on my normal memory sales.

With my 20 per cent discount, the price needs a 15.2 per cent margin, half my base of 30 per cent. If the cash also stays inside the group and earns nothing, the price needs 31.9 per cent, close to my base. So the price is roughly my base with a discount and the cash thrown away.

**Where I differ.** The discount is earned, but the market charges it twice. Samsung's 2026 plan returns a third to two fifths of my 2026 free cash flow, while SK Hynix has committed to at least half. The Lee family controls Samsung through Samsung C&T and Samsung Life Insurance with a small direct stake. That justifies a discount, which I take.

But Samsung now plans KRW 90 to 110 trillion of shareholder returns for 2026, with KRW 55 to 75 trillion still to come. It includes "a substantial share repurchase and cancellation program". The final amount is set at a board meeting in late January 2027.

**The preferred shares are the cleaner way in.** Each preferred share received the same KRW 4,601 third quarter dividend and earned near the same EPS, but trades 22.7 per cent below the common. The gap was 16.9 per cent at the end of 2024. Samsung says it will consider "adjusting the proportion of preferred shares" in its buybacks. The note covers the common, but the same value per share applies to both, and the preferred lacks only the vote.

## Valuation, with the working

All forecasts below are mine. Figures are in KRW trillion unless per share. I value operations, because reported profit swings with finance items: a KRW 9.5 trillion finance loss in the third quarter, and about KRW 10 trillion of operating profit lost to the stronger won.

**2026.** The fourth quarter brings KRW 170 trillion of memory sales and a 74 per cent margin in the chip division, with phones still at a small loss. Revenue is KRW 720.8 trillion, against KRW 722.3 trillion in consensus. EPS is KRW 44,834, 2.9 per cent below consensus.

**2027.** Memory sales are KRW 760 trillion at a 76 per cent operating margin, and group revenue KRW 967 trillion, 4.1 per cent below consensus. EPS is KRW 68,368, 9.6 per cent below consensus. **2028.** Memory sales fall 10 per cent at a 68 per cent margin, and EPS is KRW 55,894.

**Cash.** Fourth quarter free cash flow is about KRW 77 trillion and 2027's about KRW 362 trillion, after KRW 110 trillion of capital spending. Samsung plans KRW 84.4 trillion for 2026, KRW 76.8 trillion of it for chips.

| | 2025 | 2026E | 2027E | 2028E | Normal year |
|---|---|---|---|---|---|
| Revenue | 333.6 | 720.8 | 967.0 | 903.0 | |
| Memory sales | 104.1 | 506.3 | 760.0 | 684.0 | 295.8 |
| HBM, my estimate | 9.6 | 31.6 | 32.4 | | |
| Operating profit | 43.6 | 386.1 | 585.8 | 478.9 | |
| Memory net margin | | | 57.8% | 51.7% | 30.0% |
| EPS, KRW | 6,603 | 44,834 | 68,368 | 55,894 | |
| Consensus EPS, KRW | | 46,174 | 75,630 | | |
| P/E at KRW 229,000 | 34.7x | 5.1x | 3.3x | 4.1x | |

**Normal memory.** I take memory sales for the four quarters to June 2026, KRW 259.4 trillion, grow bits 20 per cent a year for four years, and settle revenue per bit at 55 per cent. That gives KRW 295.8 trillion, at a 30 per cent net margin: KRW 88.8 trillion.

**The rest.** Phones, at 10 times after-tax profit on a normal operating profit of KRW 12 trillion, the 2023 to 2025 average, give KRW 91 trillion. Display, TVs and appliances, and Harman add KRW 47 trillion. Foundry and System LSI, which report no profit, I put at 1.5 times sales, KRW 41 trillion. Investments of KRW 97.2 trillion count at three quarters.

**The base value.** Net cash adds KRW 514 trillion, memory above normal KRW 438 trillion, and 12 times normal memory earnings KRW 1,065 trillion. The rest adds KRW 252 trillion. The gross is KRW 2,269 trillion, or KRW 348,400 a share. Less 20 per cent, it is KRW 278,700.

**Three cases, twelve months out.**

| Case | What happens | 2027 EPS | Normal memory profit | P/E on normal | Value | Change |
|---|---|---|---|---|---|---|
| Bear | Prices turn in 2027; 2028 memory sales fall 35%; normal margin 19% | KRW 53,700 | 40.9 | 10x | KRW 156,200 | down 32% |
| Base | Tight through 2028, half the excess in 2029; normal margin 30% | KRW 68,400 | 88.8 | 12x | KRW 278,700 | up 22% |
| Bull | 2027 near consensus; shortage lasts to 2029; normal margin 40% | KRW 79,400 | 150.6 | 14x | KRW 450,200 | up 97% |

Weighted 25, 50 and 25 per cent, the cases give about KRW 290,900, 27 per cent above the price. The discount and the other businesses are the same in all three cases.

**The band.** I go long when my base value is at least 15 per cent above the price. At 22 per cent above, Samsung clears it, but not by much. A target of KRW 270,000 rounds the base down.

**How sensitive it is.** Each row is the normal memory net margin and each column the multiple on normal earnings, with the discount at 20 per cent.

| Normal net margin | 10x | 12x | 14x |
|---|---|---|---|
| 22% | KRW 232,400 | KRW 248,400 | KRW 264,400 |
| 30% | KRW 256,900 | KRW 278,700 | KRW 300,500 |
| 38% | KRW 281,400 | KRW 309,000 | KRW 336,600 |

All nine cells sit above the price, but the lowest only by 1.5 per cent. The discount matters as much: at 10 per cent the base is KRW 313,500, and at 30 per cent KRW 243,900. Take the cash away and the base falls to KRW 215,500, 6 per cent below the price.

<div class="charts-slot"></div>

## Risks, and what would change my view

**The cycle turns early.** The chip division, almost all of it memory, earns 98 per cent of the profit, and memory prices have soared in a year. Every maker has the same price signal: SK Hynix plans to double its wafer capacity in five years, and Micron's new fabs start in 2027. If prices fall in 2027, my bear case applies, a 32 per cent fall.

**The cash stays in the group.** Samsung had planned or completed about KRW 35 trillion of 2026 returns by October, against nine months of free cash flow near KRW 186 trillion. If the January plan disappoints or the cash goes into large acquisitions, my base falls below the price.

**Custom HBM goes to the buyer's foundry.** If NVHBM's base die is made at TSMC, Samsung's one roof matters less, and its foundry loses the base die sales that lifted it this year. HBM is a small slice, so this costs the story more than the value.

**The won.** Sales are largely in dollars. A stronger won cost about KRW 10 trillion of third quarter operating profit against the second, and every further step up cuts dollar sales in won.

**Phones.** A longer squeeze on MX would cut the KRW 91 trillion I give phones. It is a small part of the value.

**What would change my view.** Back to no call: a price above about KRW 242,500, where my base would sit less than 15 per cent above it, with my numbers unchanged. Towards the bull case: a January return plan at the top of the range, weighted towards cancelled shares.

The view is wrong if, by October 2027, Samsung reports a quarter in which memory sales and DRAM prices both fall on the quarter before. It is also wrong if the 2026 shareholder return, finalised in late January 2027, comes in below KRW 90 trillion, the bottom of its own range.

Samsung pays the third quarter dividend on 27 November 2026. Fourth quarter results are expected in late January 2027, with preliminary figures in early January, as in past years; Samsung has not confirmed the dates. The board sets the 2026 return in late January. HBM4E mass production is planned for the first half of 2027, and the first Taylor fab is starting up.

## Conclusion

My piece of 31 October argued that from HBM4E the biggest buyer designs the bottom of the memory stack. Samsung is the maker best placed to build such a stack under one roof, and the one least likely to ship it in volume by the end of 2027. The claim now rests mainly on SK Hynix and Micron.

The shares are a different question. HBM is about 6 per cent of Samsung's memory sales; the rest is an ordinary memory boom inside a conglomerate. At 3.0 times consensus 2027 earnings, the price assumes the boom ends badly and the cash stays in the group. My base value is KRW 278,700, 22 per cent above the price, within a range of KRW 156,200 to KRW 450,200. My call is long, with low conviction, and a target of KRW 270,000.

<p class="sources">Sources: Samsung Electronics earnings call decks for 1Q, 2Q and 3Q 2026 and for 4Q 2018, 2019, 2021, 2022, 2024 and 2025 (Samsung IR), for segment sales and operating profit, memory sales, the income statement, balance sheet, cash flow, the foundry base die and the shareholder return update. Samsung 3Q 2026 earnings call, 29 October 2026 (transcript via Investing.com), for bits, prices, HBM4, the 2027 HBM sell-out, long-term contracts, HBM4E timing, the 4 nanometre base die, the exchange rate effect, capital spending and the phone outlook. Samsung filings to the London Stock Exchange of 31 March, 12 October and 29 October 2026 for the share cancellation, the buyback and treasury shares, the third quarter dividend and the 2026 capital spending plan. Samsung 2026 half-year business report (filed 31 August 2026) for the shares issued. SK Hynix prospectus (Form 424B4), 10 July 2026, for IDC's HBM market shares. Samsung newsroom, 12 February 2026, for HBM4 shipments, the base die, custom HBM samples and HBM sales in 2026. Micron prepared remarks of 23 September 2025 for its HBM4E base die; SK Hynix release of 19 April 2024; Nvidia NVHBM blog, 26 August 2026. stockanalysis.com (S&P Global) for annual figures from 2021 to 2025, consensus, the average target and peer multiples, retrieved 2 November 2026. KRX closes via Naver Finance and stockanalysis.com, and the Hana Bank KRW/USD notice rate via Naver, retrieved 2 November 2026. Estimates from the fourth quarter of 2026, HBM revenue, normal earnings, the other businesses, the discount and the valuation are the author's own. Personal research, not investment advice.</p>
