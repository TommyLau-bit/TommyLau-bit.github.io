---
title: "ASML's machines are booked to 2027, so its earnings are unusually visible. At €1,636, the price already pays for them."
summary: "ASML is the only maker of the EUV machines that print the finest layers of AI chips. It ships about 65 of its standard model this year, its full capacity, and says 2027's planned 85 are close to fully ordered. That makes its next two years of earnings unusually visible, but at €1,636.40 the shares already price about 94 machines in 2028 at 28 times earnings, so my base value of €1,697 sits only 4 per cent above the price."
company: "ASML"
ticker: "ASML"
exchange: "Euronext Amsterdam"
claims: ["asml-booked-ahead"]
keyPoints:
  - "ASML is the only maker of EUV lithography machines. It expects to ship about 65 low NA EUV machines in 2026, all of its capacity, and plans about 85 for 2027, which it says is close to fully covered with orders. It guides 2026 total net sales of €43 billion to €45 billion, up about a third."
  - "The evidence since the piece supports the claim. Output steps up about 30 per cent a year inside existing cleanrooms. Installed Base Management, lifted by NXE:3800E field upgrades, grew 28 per cent in the first half of 2026 and beat guidance by almost €300 million in the second quarter."
  - "At €1,636.40 the shares trade at 31.6 times 2027 consensus earnings. At 28 times 2028 earnings, my base multiple, the price needs about 94 low NA machines in 2028 with my other assumptions: more than the 85 planned for 2027 and fewer than the 110 ASML is investigating."
  - "My call is no call, with medium conviction. Twenty-eight times my 2028 EPS of €60.59 gives €1,697, 4 per cent above the price, within a range of €1,013 to €2,208. On earnings the shares look roughly fairly priced; a DCF cross-check falls below the price only if cash conversion runs below its recent history."
files:
  pdf: "/research/2026-10-07_ASML_Initiation.pdf"
  xlsx: "/research/2026-10-07_ASML_Model.xlsx"
  thumb: "/research/2026-10-07_ASML_Initiation-p1.png"
  pages: 5
date: 2026-10-07T20:26:26+08:00
draft: false
call:
  direction: "NO CALL"
  price: 1636.40
  priceDate: 2026-10-06
  currency: "€"
  target: null
  horizon: "12 months, to October 2027"
  conviction: "Medium"
  revisitIf: "A price at or below about €1,475, which points long, or at or above about €2,262, which points short, with my numbers unchanged; or results that move my 2028 EPS to about €67.21 or more, which points long, or to about €43.83 or less, which points short."
  wrongIf: "By October 2027, ASML says 2027 low NA EUV shipments will fall more than 10 per cent short of about 85 because customers pushed out or cancelled orders, which points to my bear case; or it confirms 2028 low NA capacity of 110 or more and says 2028 is close to fully covered with orders, which points to my bull case."
charts:
  - id: units
    title: "EUV systems: recognised in sales, then low NA capacity"
    kind: bar
    decimals: 0
    labels: ["2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028"]
    series:
      - name: "EUV systems recognised in sales (incl. High NA)"
        values: [31, 42, 40, 53, 44, 48, null, null, null]
      - name: "Low NA capacity: 2026 actual, 2027 plan, 2028 under study"
        values: [null, null, null, null, null, null, 65, 85, 110]
    refs:
      - value: 100
        label: "My base for 2028"
    note: "Recognised units include a few High NA machines; capacity is low NA only. ASML recognised 32 EUV systems in the first half of 2026."
    source: "ASML annual reports for 2021, 2023 and 2025 (Form 20-F); ASML Q2 2026 release and investor call, 15 July 2026. The 2028 base is the author's."
  - id: mix
    title: "Total net sales by segment, € billion"
    kind: bar
    prefix: "€"
    unit: "bn"
    decimals: 1
    labels: ["2023", "2024", "2025", "2026E", "2027E", "2028E"]
    series:
      - name: "Net system sales (EUV, DUV, metrology)"
        values: [21.9, 21.8, 24.5, 33.1, 41.1, 47.5]
      - name: "Installed Base Management"
        values: [5.6, 6.5, 8.2, 10.8, 11.9, 13.1]
    refs:
      - value: 44
        label: "2030 low scenario, Investor Day 2024"
      - value: 60
        label: "2030 high scenario, Investor Day 2024"
    note: "On my numbers ASML reaches the top of its 2030 revenue range in 2028. 2026E to 2028E are the author's estimates."
    source: "ASML Annual Report 2025 (Form 20-F) for 2023 to 2025 and the 2030 scenarios; estimates are the author's."
  - id: quarters
    title: "Installed Base Management by quarter, € billion"
    kind: bar
    prefix: "€"
    unit: "bn"
    decimals: 2
    labels: ["Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26 guide"]
    series:
      - name: "Installed Base Management"
        values: [2.10, 1.96, 2.13, 2.49, 2.76, 2.90]
    note: "Second quarter 2026 came in almost €300 million above guidance, mainly on upgrades, and lifted gross margin to 54.0 per cent."
    source: "ASML Q2 2026 US GAAP statements and investor call, 15 July 2026."
  - id: china
    title: "China, share of total net sales, per cent"
    kind: bar
    unit: "%"
    decimals: 1
    labels: ["2023", "2024", "2025", "2026 guide"]
    series:
      - name: "China"
        values: [26.3, 36.1, 29.1, 20.0]
    note: "ASML expects China to make up around 20 per cent of 2026 total net sales."
    source: "ASML Annual Report 2025 (Form 20-F), total net sales by region; Q2 2026 investor call, 15 July 2026."
  - id: price
    title: "ASML share price, Euronext Amsterdam, month-end close, €"
    kind: line
    prefix: "€"
    decimals: 0
    labels: ["Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "6 Oct 26"]
    series:
      - name: "Close"
        values: [621.2, 658.4, 678.7, 722.7, 678.6, 606.0, 582.5, 653.9, 677.6, 613.1, 636.6, 828.1, 918.1, 903.4, 921.4, 1215.6, 1233.4, 1119.2, 1222.4, 1384.8, 1721.4, 1434.2, 1451.8, 1596.8, 1636.4]
    refs:
      - value: 1697
        label: "My base value"
    note: "The shares doubled from a lowest close of €813.90 on 10 October 2025 to a highest close of €1,721.40 on 30 June 2026."
    source: "Euronext Amsterdam historical prices, retrieved 7 October 2026. Month-end closes; the last point is the close on 6 October 2026."
---

ASML's shares closed at €1,636.40 in Amsterdam on 6 October 2026, and its Nasdaq ADR at US$1,834.10. A year earlier the shares were near their low of the past year, a close of €813.90 on 10 October 2025. They have doubled since.

My piece of 7 October argued that ASML's EUV machines are sold out and booked a year or two ahead. Their number grows only as fast as ZEISS optics and ASML's cleanrooms allow, about 30 per cent a year.

The filings and the July call support that claim. The question for the shares is what that visibility is worth, and how much of it the price already holds.

## The thesis

Go back to the workshop in the piece. One workshop in the whole country makes the special oven every bakery needs. Next year's ovens are already promised, and it can add only a few each year, as fast as its glassmaker can make oven doors.

For an owner of the workshop, that changes the question. Demand is not the unknown for the next two years. The unknowns are how many ovens, at what price, and how much the workshop earns servicing ovens it already sold.

**The count is set.** ASML expects to ship about 65 low NA EUV machines in 2026, equal to its capacity. It plans about 85 for 2027, a 30 per cent step, and says it is "close to being fully covered with orders" for that year.

For 2028 it has "already received a significant number" of low NA orders and is investigating another 30 per cent, about 110. In the Q&A, as transcribed, the finance chief said ASML did not yet hold orders for all of them: "we're not waiting, we're preempting." Each step comes from its existing footprint.

ASML is not claiming a shortage. On the same call Christophe Fouquet, the chief executive, said "the capacity is there to meet the demand but the demand is still fluctuating." That is the main counterpoint to "booked": ASML sizes its output to the orders it holds, and orders can move.

**The price per machine is rising.** Low NA EUV sales per system rose from €187 million in 2024 to €237 million in 2025, by my arithmetic, as the faster NXE:3800E took over. On the July call, as transcribed, ASML said next year's EUV mix will be "more positive" than this year's. Four High NA machines brought €1,156.9 million in 2025, about €289 million each.

**The installed base pays twice.** Installed Base Management, service and upgrades on machines already in the field, grew 26.2 per cent in 2025, to €8.2 billion. It rose 28.1 per cent in the first half of 2026.

In the second quarter it came in almost €300 million above guidance, "driven primarily by additional upgrade business". Gross margin beat too, on "very high margin components" within it. ASML guides €2.9 billion for the third quarter, 48 per cent above a year earlier.

My piece noted that NXE:3800E field upgrades shifted "a substantial portion of EUV system revenue" into this line. An upgrade raises the wafers an installed machine prints each hour. So part of this growth is extra EUV capacity sold without a new machine, the one way round the queue. In 2025 systems earned a 53.5 per cent gross margin and the installed base 50.9 per cent, by my arithmetic from the cost lines.

**The supplier behind it is paid more each year.** ASML bought €4.4 billion from Carl Zeiss SMT in 2025, against €3.3 billion in 2023. It owns 24.9 per cent of the ZEISS holding company. Its profit from equity method investments, which include that stake, was €145.7 million in the first half of 2026.

**Not everything is EUV.** DUV and metrology systems brought €12.9 billion in 2025. ASML expects non-EUV system sales to grow about 25 per cent in 2026, and plans 30 per cent more immersion capacity for 2027.

China is the soft spot. It took 36.1 per cent of total net sales in 2024 and 29.1 per cent in 2025. ASML expects around 20 per cent in 2026, and China was 14 per cent of second quarter system sales.

**Customers are few.** Four customers each took more than 10 per cent of 2025 sales, together €20.0 billion, or 61.2 per cent. ASML does not name them. By region, Taiwan and South Korea each took about a quarter.

I checked the piece's figures against the 20-F, the releases and ASML's own transcript. They stand.

## What the market prices in, and where I differ

At €1,636.40 ASML is worth about €628.5 billion on 384.1 million shares. Cash and short-term investments less long-term debt were €5.6 billion on 28 June, so the enterprise value is about €622.9 billion.

The shares trade at 42.0 times 2026 consensus earnings of €38.92 and 31.6 times 2027 consensus of €51.71. Both are Zacks figures for the ADR, in US dollars, converted at the ECB rate of 6 October. stockanalysis.com has €38.35 for 2026, but its revenue consensus sits below ASML's own guide, so it is partly stale.

**Against its peers ASML looks cheaper, not dearer.** On the ADR, ASML trades at 31.5 times consensus for the year ending December 2027. Applied Materials, Lam Research, KLA and Tokyo Electron trade at a median of 36.1 times their fiscal years ending in 2027. Those years end two to nine months earlier, so on calendar 2027 their multiples would be lower and the gap narrower.

The obvious objection is that the only maker of EUV machines should trade at a premium. My answer is that its growth is booked, and it is also capped. The piece's growth half says output steps up about 30 per cent a year, and ASML guides it that way. The market prices a known path, not an open-ended one.

**What the price needs.** In October 2027 the market will price 2028 earnings. At my base 28 times, €1,636.40 needs 2028 EPS of €58.44. With my other base assumptions, that is about 94 low NA machines in 2028: more than the 85 planned for 2027, fewer than the 110 under study.

**Where I differ, and where I do not.** On the next two years I barely differ. My 2027 EPS of €50.78 is 1.8 per cent below consensus. I take 100 machines in 2028, a little above what the price needs.

The difference comes after 2028. On my numbers ASML reaches €60.6 billion of revenue in 2028. That is the top of the 2030 range it gave at its November 2024 Investor Day, €44 billion to €60 billion, two years early.

A discounted cash flow check at an 8.5 per cent cost of equity gives €1,226 a share if free cash flow is 95 per cent of net income, and €1,481 at the 115 per cent of 2025. At 115 per cent, the price needs net income to grow about 10 per cent a year from 2029 to 2032; at 95 per cent, about 16 per cent. ASML will update its long-term view at a Capital Markets Day on 10 June 2027.

## Valuation, with the working

I value ASML on earnings: 28 times my 2028 EPS, the year the market will price in October 2027. I build revenue by segment, because the drivers differ. Low NA is units times price, High NA is a handful of machines, DUV follows the wider cycle and China, and the installed base compounds. All forecasts below are mine.

**2026.** EUV system sales grow 47 per cent, against "over 45 per cent" guided, to €17.1 billion. Non-EUV grows 25 per cent to €16.1 billion, and the installed base 32 per cent to €10.8 billion. Total net sales are €44.0 billion, the middle of the guide. At a 55 per cent gross margin, EPS is €39.49, 1.5 per cent above consensus.

**2027.** Eighty-five low NA machines at €261 million each, 5 per cent more than 2026, make €22.2 billion. Five High NA machines at €300 million add €1.5 billion. Non-EUV grows 8 per cent and the installed base 10 per cent. Revenue is €53.0 billion, gross margin 56.5 per cent, and EPS €50.78.

**2028.** One hundred low NA machines at €269 million, eight High NA, non-EUV up 5 per cent and the installed base up 10 per cent give €60.6 billion. At a 57.5 per cent gross margin, inside the 56 to 60 per cent range for 2030, EPS is €60.59.

| € million unless stated | 2024 | 2025 | H1 2026 | 2026E | 2027E | 2028E |
|---|---|---|---|---|---|---|
| Low NA EUV units | 42 | 44 | | 65 | 85 | 100 |
| EUV system sales | 8,321 | 11,603 | | 17,056 | 23,683 | 29,281 |
| DUV and metrology systems | 13,447 | 12,872 | | 16,090 | 17,377 | 18,245 |
| Installed Base Management | 6,494 | 8,193 | 5,249 | 10,815 | 11,896 | 13,086 |
| Total net sales | 28,263 | 32,667 | 18,093 | 43,960 | 52,956 | 60,612 |
| Gross margin | 51.3% | 52.8% | 53.5% | 55.0% | 56.5% | 57.5% |
| Income from operations | 9,023 | 11,301 | 6,614 | 17,842 | 22,970 | 27,302 |
| Diluted EPS, € | 19.24 | 24.71 | 14.73 | 39.49 | 50.78 | 60.59 |
| Consensus EPS, € | | | | 38.92 | 51.71 | |
| P/E at €1,636.40 | 85.1x | 66.2x | | 41.4x | 32.2x | 27.0x |

Units for 2024 and 2025 are low NA systems recognised in sales; for 2026 and 2027 they are shipments, equal to capacity.

**The multiple.** I use 28 times. At the end of 2024 the shares traded at 27.5 times the EPS ASML then earned in 2025. Today they trade at 32.2 times my 2027. One year on, EPS growth slows from 29 per cent in 2027 to 19 per cent in 2028 on my numbers, so I take less than today.

**The base value.** Twenty-eight times €60.59 is €1,697, 4 per cent above the price. On that value, enterprise value is 23.7 times 2028 income from operations. Today it is 27.1 times my 2027.

**Three cases, twelve months out.** 2026 and 2027 are the same in all three, because 2027 output is close to fully covered. The cases differ in 2028.

| Case | What happens in 2028 | Low NA units | Gross margin | P/E | EPS 2028 | Value | Change |
|---|---|---|---|---|---|---|---|
| Bear | Memory and China digest; no capacity step; DUV down 10% | 85 | 55.0% | 22x | €46.04 | €1,013 | down 38% |
| Base | One more step, short of the 110 under study | 100 | 57.5% | 28x | €60.59 | €1,697 | up 4% |
| Bull | 110 machines, richer mix, High NA ramps | 110 | 59.0% | 32x | €68.99 | €2,208 | up 35% |

Weighted 25, 50 and 25 per cent, the cases give €1,653, 1 per cent above the price.

**The band.** I go long when my base value is at least 15 per cent above the price, and short when it is at least 25 per cent below. At 4 per cent above, ASML sits in between, so my call is no call.

**How sensitive it is.** Each row is 2028 low NA units and each column the multiple, with everything else as in the base.

| 2028 low NA units | 24x | 28x | 32x |
|---|---|---|---|
| 85 | €1,332 | €1,555 | €1,777 |
| 100 | €1,454 | €1,697 | €1,939 |
| 110 | €1,535 | €1,791 | €2,047 |

Five of the nine cells sit above the price, but only two clear it by 15 per cent, both at 32 times with 100 or 110 machines. None sits 25 per cent below. The multiple moves the value more than the count, which is what a booked order book should look like.

**The DCF cross-check.** I take net income growth of 10, 8, 6 and 5 per cent from 2029 to 2032, then 3 per cent a year, at an 8.5 per cent cost of equity. With free cash flow at 95 per cent of net income, my assumption as customer down payments unwind, that is €1,226 a share at the end of 2027, 25 per cent below the price. ASML converted 120 per cent in 2024 and 115 per cent in 2025; at 115 per cent the DCF gives €1,481, 9 per cent below. The DCF is a cross-check, not my method. It sits below the price mainly because my cash conversion is below history, so I read the shares as roughly fairly priced on earnings, not as a short.

<div class="charts-slot"></div>

## Risks, and what would change my view

**Against the no call, on the upside.** The Capital Markets Day on 10 June 2027 will replace 2030 targets that my base already reaches in 2028. If ASML confirms 110 low NA machines for 2028 and its customers' megafab plans hold, my bull case of €2,208 is in reach. High NA is a second lever: Intel now uses it on some layers of its 18A process.

**China and export controls.** ASML expects China to fall to around 20 per cent of sales this year. Its 20-F says changes in export controls "may have a material impact" on sales volume, mix and timing. The MATCH Act, introduced in the US Congress on 2 April 2026, would ban DUV immersion sales to China and require licences to service tools in covered Chinese fabs, which matters for Installed Base Management as well as systems. TrendForce reported on 17 April 2026 that a revised, more targeted version dropped some curbs but kept the DUV ban and the service licences, now reviewable rather than automatically denied.

In June, Bloomberg reported that US officials had raised concerns with ASML that an EUV system may have reached China. ASML told Reuters it has "never shipped an EUV machine to China, nor any component, module or equipment specially designed for use in one." No evidence has been made public, and I have not verified either side.

**Few customers, one cycle.** Four customers took 61.2 per cent of 2025 sales. ASML expects memory-related system sales to grow over 75 per cent this year, on DRAM fabs built for AI. If DRAM prices turn, the 2028 step is the first thing to go, which is my bear case.

**Fewer machines per layer.** ASML says High NA saves fab space by "requiring fewer systems overall". Faster low NA machines and upgrades do the same. Each one is good for revenue per machine but caps the count.

**ZEISS.** A shortfall caused by ZEISS would support my piece's claim, but it would cut ASML's earnings in the year it happened.

**What would change my view.** Into a long: a price at or below about €1,475 with my numbers unchanged, or results that lift my 2028 EPS to about €67.21 or more. Into a short: a price at or above about €2,262, or 2028 EPS at or below about €43.83.

The view is wrong if, by October 2027, ASML says 2027 low NA shipments will fall more than 10 per cent short of about 85 because customers pushed out or cancelled orders, which points to my bear case. It is also wrong if ASML confirms 2028 low NA capacity of 110 or more and says 2028 is close to fully covered, which points to my bull case.

ASML reports third quarter results on 14 October 2026, a date in its own financial calendar. I will watch its words on 2027 and 2028 coverage, China, and the fourth quarter implied by the €43 billion to €45 billion guide. Fourth quarter results usually follow in late January; the 2027 date is not yet confirmed.

## Conclusion

My piece of 7 October argued that ASML's EUV machines are sold out and booked a year or two ahead, and grow about 30 per cent a year. The July results and call support both halves. That makes ASML's next two years of earnings unusually visible, and my 2027 is within 2 per cent of consensus.

The shares already pay for that. At €1,636.40 the price needs about 94 low NA machines in 2028 at 28 times earnings, between the 85 planned and the 110 under study. My base value is €1,697, 4 per cent above the price, within a range of €1,013 to €2,208, and a DCF check sits lower only on below-history cash conversion. My call is no call, with medium conviction.

<p class="sources">Sources: ASML Annual Report 2025 on Form 20-F, filed 25 February 2026, for income statements from 2023 to 2025, net system sales by technology, total net sales by region, customer concentration, cost of system and service sales, purchases from Carl Zeiss SMT, free cash flow, export control risks, the 2030 scenarios from the November 2024 Investor Day and the financial calendar. ASML fourth quarter 2025 results, Form 6-K, 28 January 2026, for backlog and the buyback programme. ASML second quarter 2026 results, Form 6-K, 15 July 2026, for the release, presentation and US GAAP statements. ASML's own transcript of its 15 July 2026 investor call for the 2026 guides, capacity, order coverage and China; the call's questions and answers as transcribed by Webull. Share prices are Euronext Amsterdam closes, retrieved 7 October 2026; ADR and peer closes from stockanalysis.com; exchange rates from the ECB, 6 October 2026. Consensus from Zacks and stockanalysis.com (S&P Global), retrieved 7 October 2026. Bloomberg's report of 18 June 2026 as carried by NL Times, and ASML's statement to Reuters of 19 June 2026. TrendForce, 17 April 2026, on the MATCH Act. Estimates for 2026 to 2028, the scenarios, the DCF and the valuation are the author's own. Personal research, not investment advice.</p>
