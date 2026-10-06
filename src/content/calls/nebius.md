---
title: "Nebius is paid only for power that is switched on. At US$233, the shares already assume it switches on fast."
summary: "Nebius builds AI computing centres and rents them out to companies such as Microsoft and Meta. It earns money only once the power is on and the chips are running, and the new contracts pay far more per unit of power than the old ones. The shares already price in most of that, so the call turns on how fast the power comes on, which the next two sets of results will show."
company: "Nebius"
ticker: "NBIS"
exchange: "Nasdaq"
claims: ["nebius-paid-for-what-is-switched-on"]
correction: "I defined connected power as power feeding running chips and said customers pay for it. That is Nebius's active power, which comes on months after connection, so the test is active megawatts."
keyPoints:
  - "Nebius builds AI computing centres and rents them out. It is paid only once the chips are running, months after the power is connected."
  - "New contracts pay US$20 to 25 million a megawatt a year, about twice the 2026 fleet. At the old price a megawatt barely earns its cost; at the new one it returns 16 to 25 per cent before tax."
  - "The gap between that price and a US$7 to 9 billion run-rate guide closes once you see that most new capacity bills in 2027, not 2026."
  - "At about 12.7 times 2027 EBITDA the market already pays for fast switch-on at the new price. My base case is worth about the share price, and the bear case is a 66 per cent fall."
  - "Where I was wrong: my September piece said customers pay for connected power. They pay for active power, so that is the number to watch."
files:
  pdf: "/research/2026-10-06_Nebius_Initiation.pdf"
  xlsx: "/research/2026-10-06_Nebius_Model.xlsx"
  thumb: "/research/2026-10-06_Nebius_Initiation-p1.png"
  pages: 7
date: 2026-10-06T19:29:59+08:00
draft: false
call:
  direction: "NO CALL"
  price: 232.57
  priceDate: 2026-10-05
  currency: "US$"
  target: null
  horizon: "12 months, to October 2027"
  conviction: "Medium"
  revisitIf: "A price below about US$185, or fourth quarter results in early 2027 showing at least 800 megawatts connected, year-end annualised revenue inside the US$7 to 9 billion range and new deals still at US$20 million a megawatt or more."
  wrongIf: "Connected power at the end of 2026 comes in below the 800 megawatt bottom of Nebius's own range, or year-end annualised revenue lands below US$7 billion, or prepayments appear in fewer than half of new deals."
charts:
  - id: arr
    title: "Annualised revenue run-rate at quarter end, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 2
    labels: ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "ARR"
        values: [0.25, 0.43, 0.55, 1.25, 1.92, 3.00]
    refs:
      - value: 7
        label: "Year-end 2026 guide, low end"
    note: "To reach even the bottom of its year-end range, Nebius has to more than double its run-rate in the second half of 2026."
    source: "Nebius quarterly shareholder letters, Q2 2025 to Q2 2026. Before 2026 the figure covers the core AI infrastructure business. Year-end guide from the Q2 2026 letter, 12 August 2026."
  - id: build
    title: "Revenue against capital spending by quarter, US$ million"
    kind: bar
    prefix: "US$"
    unit: "m"
    labels: ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Revenue"
        values: [50.9, 105.1, 146.1, 227.7, 399.0, 582.3]
      - name: "Capital spending"
        values: [544, 510.6, 955.5, 2100, 2500, 5700]
    note: "In the second quarter of 2026 Nebius spent about ten dollars building for every dollar it earned. The money arrives as capacity goes live, months after it is paid for."
    source: "Nebius quarterly shareholder letters and results, Q2 2025 to Q2 2026. Q1 2025 capital spending is derived from the first half less the second quarter. Q4 2025, Q1 2026 and Q2 2026 capital spending are approximate, as reported."
  - id: margin
    title: "AI cloud adjusted EBITDA margin, per cent"
    kind: bar
    unit: "%"
    decimals: 1
    labels: ["Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "AI cloud adjusted EBITDA margin"
        values: [19, 24, 45, 49.7]
    note: "Running capacity earns well once it is running. Half of each dollar of AI cloud revenue is left before interest, tax and the wearing out of equipment."
    source: "Nebius quarterly shareholder letters, Q3 2025 to Q2 2026."
  - id: acv
    title: "Annual contract value per megawatt, US$ million, approximate"
    kind: bar
    prefix: "US$"
    unit: "m"
    decimals: 1
    labels: ["2026 fleet base", "Q2 2026 large deals", "Q3 2026 short-term deals"]
    series:
      - name: "Annual contract value per MW"
        values: [12, 22.5, 40]
    note: "New contracts pay roughly twice what the existing fleet earns. The Q2 bar is the midpoint of the US$20 to 25 million range; the Q3 figure is a floor, as Nebius gave it as above US$40 million."
    source: "Nebius Q2 2026 shareholder letter, 12 August 2026, 'ACV per MW is stepping up'. Revenue recognition basis, excluding prepayments. All figures approximate, as the company states."
  - id: price
    title: "Nebius share price, month-end close, US$"
    kind: line
    prefix: "US$"
    decimals: 2
    labels: ["Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
    series:
      - name: "Close"
        values: [21.99, 27.70, 32.66, 32.49, 21.11, 22.73, 36.75, 55.33, 54.43, 68.32, 112.27, 130.82, 94.87, 83.71, 85.19, 91.19, 103.76, 138.23, 231.09, 276.17, 190.41, 206.32, 235.88, 232.57]
    note: "The shares rose more than tenfold in two years. They fell 17 per cent on 1 July 2026, the day Bloomberg reported that Meta plans to sell its own spare computing capacity."
    source: "Yahoo Finance monthly closes, retrieved 6 October 2026. The last point is the close on 5 October 2026."
---

Nebius closed at US$232.57 on 5 October 2026, more than ten times its price when trading resumed in October 2024. In that time it went from a leftover of Yandex with one data centre in Finland to a supplier of AI capacity to Microsoft and Meta.

In September I argued that Nebius is paid for megawatts that are switched on, not megawatts it has signed. This pitch asks a narrower question. If that is how Nebius gets paid, what is a share worth, and does the price already know?

My answer is that the mechanism is right and the price knows it. At US$233 the shares assume that Nebius switches on most of its contracted power quickly, at the new, higher contract prices.

The call turns on speed, and the next two sets of results will show it.

## The thesis

Go back to the industrial kitchen from the September piece. Nebius has booked the gas supply for five kitchens and expects to light about one this year. Its customers pay only for meals from lit ovens.

Lighting the ovens is not the moment the money starts, and the September piece said so. After the power is connected, Nebius still has to build the network, assemble the clusters, install its software and bring the customer on. Nebius described that sequence on its August results call, and said the stretch after connection takes several months.

That matters, because it changes what the number I watch actually measures. Nebius defines connected power as power wired into fully built and equipped data centres. Active power is power consumed by installed, running equipment and available to earn revenue. Connected comes first, and active follows months later.

**Where I was wrong in September.** In the piece I defined connected power as power wired up and feeding running chips, and wrote that customers pay for it. That was wrong. What I described is Nebius's active power. Connected power is the building, finished and equipped. Active power is the chips running and billing, and it trails connection by several months.

What changed my view was a gap in my own numbers, set out below. Nebius's contract value per megawatt and its run-rate guide do not fit together unless much of its connected power is not yet billing, and its own definitions confirm that. The edge the claim describes is still speed, but the right test is active power, not connected. Nebius does not report active megawatts each quarter, so I read them through annualised revenue divided by the fleet price per megawatt. Hitting 800 megawatts connected by the end of 2026 is necessary. It is not yet revenue. The piece and the claim stay exactly as published, so the record shows the mistake.

This also resolves a gap that has sat open in my notes since September. Nebius says its large second quarter deals carry annual contract value of US$20 to 25 million per megawatt. Multiply that by 800 megawatts and you get US$16 to 20 billion a year. Yet Nebius guides to annualised revenue of only US$7 to 9 billion at the end of 2026.

Three things in Nebius's own words close the gap. First, its annualised revenue is December's revenue multiplied by twelve, so it captures only what is billing that month. Second, the US$20 to 25 million applies to the new deals, against an approximate base of US$12 million for the 2026 fleet. Third, Nebius says most of those new deals were signed against capacity arriving in late 2026 and will mainly earn in 2027.

At US$12 million per megawatt, US$7 to 9 billion of annualised revenue means about 580 to 750 megawatts billing in December. That sits below 800 megawatts connected, which is exactly what a lag of several months looks like. At the end of 2025, US$1.25 billion of annualised revenue sat on about 170 megawatts active, roughly US$7.4 million each, from older and cheaper contracts. The 2026 base of about US$12 million reflects newer contracts replacing them.

So the business has two engines. Speed decides how many megawatts bill. Price per megawatt is roughly doubling as new contracts replace the old fleet. Both have to keep working for the shares to rise from here.

## What the market prices in, and where I differ

On my count, Nebius's equity is worth about US$86 billion at US$232.57, if every convertible note that is currently worth converting turns into shares. Convertible notes are a form of borrowing that can turn into shares. That count uses about 370 million shares, including options, restricted stock and Nvidia's pre-funded warrants.

After the August note issue, I estimate cash of about US$14.5 billion before third quarter spending, against about US$6.5 billion of notes and loans that would stay as debt. That gives an enterprise value, the price of the whole business net of cash, of about US$78 billion.

Against that, the consensus compiled by Yahoo Finance on 6 October expects revenue of US$3.34 billion in 2026 and US$12.3 billion in 2027. At a 50 per cent margin, 2027 earnings before interest, tax, depreciation and amortisation, EBITDA, would be about US$6.15 billion. The enterprise value is about 12.7 times that, and 6.3 times 2027 revenue.

CoreWeave, the closest listed rival, trades at about 3.6 times its 2027 revenue on the same source. Oracle trades at about 4.3 times its next year's revenue. So the market already gives Nebius a premium, and it rests on one belief: that Nebius turns contracted power into earning power faster and at better prices than anyone else.

That is my September claim. The difference is that I think the price now pays for it in advance. Consensus revenue of US$12.3 billion for 2027 already assumes the year-end run-rate roughly doubles again through 2027. It assumes Meta's second contract comes online on time in early 2027, and that new deals keep pricing at US$20 million a megawatt or more.

Where I differ from the market is on what could break. The bull story treats five gigawatts as a pipeline. I treat it as a promise to spend. At my estimate of about US$30 million of capital per megawatt, five gigawatts is roughly US$150 billion of building, against an if-converted equity value of US$86 billion. Customers prepay part of it, but the rest needs debt and new shares. And if Meta builds a business selling its own spare capacity, as Bloomberg reported on 1 July, the price per megawatt is the first thing to give.

## Valuation, with the working

**What a megawatt earns.** These are my estimates, built on Nebius's figures. I take the cost of a megawatt at about US$30 million, from capital spending of US$20 to 25 billion in 2026 against roughly 600 to 800 megawatts of new connected power, some of which is spending for 2027. I assume 80 per cent of that is chips and network, worn out over five years, and the rest is building, worn out over twenty. Margin before those costs is 50 per cent, close to the 49.7 per cent the AI cloud business reported.

| Contract value per MW | EBITDA per MW | Profit per MW after wear | Pre-tax return on US$30m |
|---|---|---|---|
| US$12m, the 2026 fleet | US$6.0m | US$0.9m | 3% |
| US$20m, new deals, low | US$10.0m | US$4.9m | 16% |
| US$25m, new deals, high | US$12.5m | US$7.4m | 25% |

This table is the whole case in three lines. At the old price, a megawatt barely earns back its cost before the chips age out. At the new price, it earns a good return, and prepayments that fund half the building raise the return on Nebius's own money further. The shares are a bet that the new price lasts through the whole build.

**Three cases, twelve months out.** By October 2027 the market will be pricing 2028. I value 2028 EBITDA at a multiple, then subtract the net debt I expect by the end of 2027, after another year of heavy building. I assume some new shares are sold along the way.

| Case | What happens | 2028 revenue | Margin | Multiple | Net debt | Shares | Value | Change |
|---|---|---|---|---|---|---|---|---|
| Bear | Connection slips, new prices fall towards the old | US$16bn | 40% | 8x | US$20bn | 400m | US$78 | down 66% |
| Base | About 800 MW connected on time, prices hold | US$21bn | 45% | 11x | US$15bn | 388m | US$229 | down 1% |
| Bull | More than 1 GW a year from 2027, prices keep rising | US$27bn | 50% | 13x | US$10bn | 385m | US$430 | up 85% |

The base multiple of 11 times sits between CoreWeave and where Nebius trades today. Weighted 25, 50 and 25 per cent, the three cases give about US$242, 4 per cent above the price.

**How sensitive it is.** Each row is 2028 EBITDA in US$ billion, and each column a multiple, with net debt of US$15 billion and 388 million shares.

| 2028 EBITDA | 9x | 11x | 13x |
|---|---|---|---|
| US$7.5bn | US$135 | US$174 | US$213 |
| US$9.5bn | US$182 | US$231 | US$280 |
| US$11.5bn | US$228 | US$287 | US$347 |

The range is wide and centred close to today's price. That is what a stock looks like when the market agrees with the thesis.

<div class="charts-slot"></div>

## Risks, and what would change my view

**Connection slips.** Nebius guides to 800 megawatts to 1 gigawatt connected by the end of 2026. Missing the bottom of that range would mean its edge is not speed, which breaks both the claim and the call.

**The price per megawatt falls.** The return table shows how much rests on new deals pricing at US$20 million or more. Meta selling spare capacity, or hyperscalers catching up on their own building, would push that down. The rise of 17 to 21 per cent in on-demand GPU prices reported from 1 October points the other way for now, though I have not confirmed it on a Nebius page.

**Funding.** Nebius has raised about US$5.75 billion of convertible notes in August, sold about US$2.8 billion of shares in May and June, and taken US$2 billion from Nvidia in March. Second half capital spending implied by the guide is US$12 to 17 billion. More new shares are likely, and at a lower price they would cost holders more.

**Customer concentration.** Three unnamed customers made up 59 per cent of second quarter revenue, at 24, 21 and 14 per cent. A pause by one of them changes the year.

**Ageing chips.** A switched-on hall of older chips earns less each year. Nebius must keep replacing them, which is why I depreciate chips over five years rather than longer.

**What would move me to a long.** Two things, either of which is enough. A price below about US$185, where the base case offers about a quarter of upside. Or fourth quarter results, early in 2027, showing at least 800 megawatts connected, year-end run-rate inside the US$7 to 9 billion range and new deals still at US$20 million a megawatt or more. That would move weight from the base case to the bull case.

**What would move me to a short.** Connection behind the pace in the third quarter results, expected around 10 or 11 November though Nebius has not confirmed the date, together with falling prepayments. About a fifth of the free-floating shares were already sold short in mid September, so a short would join a crowded trade.

## Conclusion

The September claim holds up. Nebius earns money only from capacity that is running, its new contracts pay roughly twice the old ones, and customers prepay to hold their place. The gap between US$20 to 25 million per megawatt and a US$7 to 9 billion run-rate is explained by the lag between connecting power and billing for it.

But the market has read the same letter. At about 12.7 times 2027 EBITDA, the price assumes fast connection and lasting new-deal pricing. My call is no call at US$232.57, held with medium conviction: the base case is worth about the price, and the bear case is a 66 per cent fall. I would go long below about US$185, or at today's price once the fourth quarter results show the power switching on as promised. The evidence that would change that is dated, and it arrives with the next two sets of results.

<p class="sources">Sources: Nebius quarterly shareholder letters and results on Form 6-K, Q2 2025 to Q2 2026, for revenue, annualised run-rate, margins, capital spending, power and customer concentration. Nebius Q2 2026 shareholder letter, 12 August 2026, for the annualised revenue guide, contract value per megawatt and prepayments. Nebius Q1 2026 shareholder letter, 13 May 2026, for the definitions of connected and active power and the 800 megawatt to 1 gigawatt connected power guide. Nebius Q2 2026 earnings call, 12 August 2026, for the capital spending guide, the connected power guide as reaffirmed, and the deployment sequence. Nebius interim financial statements to 30 June 2026 for shares, cash, notes and warrants. Nebius releases of 19 and 24 August 2026 on the convertible notes, and of 10 July 2026 on the secured loan. Nebius Form 6-K on the Microsoft agreement, 8 September 2025, and announcement of the second Meta agreement, 16 March 2026. Bloomberg News on Meta's cloud plans, 1 July 2026. Consensus revenue, peer multiples, short interest and share prices from Yahoo Finance, retrieved 6 October 2026. On-demand GPU price changes as reported by Spheron and Coin Republic, September 2026. Unit economics, net debt, share count and 2028 estimates are the author's own. Personal research, not investment advice.</p>
