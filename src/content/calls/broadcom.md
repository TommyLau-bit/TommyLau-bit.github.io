---
title: "Broadcom is still paid either way, but the tailor now earns most of the toll. At US$363, the price assumes AI revenue barely grows after fiscal 2027."
summary: "Broadcom designs the custom AI chips the largest buyers use to rely less on Nvidia, and sells the Ethernet switch chips their clusters run on. Custom chips made 73 per cent of its US$16.7 billion of AI revenue in the quarter to August. At US$362.51 the shares price fiscal 2028 AI revenue of about US$127 billion, against management's US$230 billion and my own US$190 billion."
company: "Broadcom"
ticker: "AVGO"
exchange: "Nasdaq"
claims: ["broadcom-wins-either-way"]
correction: "I wrote that Google, Meta, Anthropic and OpenAI design their own AI chips with Broadcom for their own data centres; Anthropic does not design its own chip with Broadcom but accesses Google's TPU design through it, and the 10-Q and the September call show its first deployment, of more than one gigawatt, is leased from a financial partner rather than owned."
keyPoints:
  - "Broadcom makes the custom AI chips that Google, Meta and OpenAI use to rely less on Nvidia, and the Ethernet switch chips that clusters of any maker's chips run on. AI revenue was US$16.7 billion in the quarter to 2 August 2026, up 221 per cent on a year earlier."
  - "The claim is holding, but its weight has shifted. Custom chips were 73 per cent of AI revenue in that quarter, and networking's share fell from almost 40 per cent to 27 per cent in three months. In June Broadcom put the likely level at about 30 per cent; in September it said networking would grow just as fast as custom chips."
  - "Management expects AI revenue of about US$115 billion in fiscal 2027 and US$230 billion in fiscal 2028. At US$362.51 the shares price about US$127 billion for fiscal 2028, on my sum of the parts with chips at 20 times and software at 17 times."
  - "My call is long, with medium conviction. I take US$190 billion for fiscal 2028, 17 per cent below management, which gives US$486 a share, 34 per cent above the price, within a range of US$226 to US$647."
  - "Where I was wrong: my piece said Anthropic designs its own chips with Broadcom. Broadcom's 8-K shows Anthropic accesses Google's TPU design through Broadcom. The 10-Q and the September call show its first deployment, of more than one gigawatt, is leased from a financial partner, with Broadcom backstopping up to about US$29 billion."
files:
  pdf: "/research/2026-10-06_Broadcom_Initiation.pdf"
  xlsx: "/research/2026-10-06_Broadcom_Model.xlsx"
  thumb: "/research/2026-10-06_Broadcom_Initiation-p1.png"
  pages: 6
date: 2026-10-07T01:10:29+08:00
draft: false
call:
  direction: "LONG"
  price: 362.51
  priceDate: 2026-10-05
  currency: "US$"
  target: 485
  horizon: "12 months, to October 2027"
  conviction: "Medium"
  wrongIf: "The shares close below US$270 by October 2027, or Broadcom cuts its fiscal 2027 AI revenue outlook below US$100 billion, or it makes a payment under its Backstop for a customer's AI rack leases."
charts:
  - id: ai
    title: "AI semiconductor revenue by quarter, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 1
    labels: ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26 guide"]
    series:
      - name: "AI semiconductors"
        values: [4.1, 4.4, 5.2, 6.5, 8.4, 10.8, 16.7, 21.7]
    note: "AI revenue more than tripled in a year. Networking was 35 per cent of it in Q3 FY25, almost 40 per cent in Q2 FY26 and 27 per cent in Q3 FY26; custom chips were the rest."
    source: "Broadcom results releases, Exhibit 99.1 to Form 8-K, 6 March 2025 to 2 September 2026; Q4 FY25 and the networking shares from the earnings calls of 4 September 2025, 11 December 2025, 4 March, 3 June and 2 September 2026."
  - id: mix
    title: "Revenue by quarter: AI semiconductors and the rest, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 1
    labels: ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26 guide"]
    series:
      - name: "AI semiconductors"
        values: [4.1, 4.4, 5.2, 6.5, 8.4, 10.8, 16.7, 21.7]
      - name: "Non-AI semiconductors and infrastructure software"
        values: [10.8, 10.6, 10.8, 11.5, 10.9, 11.4, 12.9, 13.1]
    note: "AI was 56 per cent of revenue in the quarter to 2 August 2026 and is guided to 62 per cent this quarter. Infrastructure software, mostly VMware, is most of the rest."
    source: "Broadcom results releases, 6 March 2025 to 2 September 2026; Q4 FY26 guide from the release and call of 2 September 2026."
  - id: margin
    title: "Non-GAAP gross and operating margin by quarter, per cent"
    kind: bar
    unit: "%"
    decimals: 1
    labels: ["Q1 FY25", "Q2 FY25", "Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26"]
    series:
      - name: "Gross margin"
        values: [79.1, 79.4, 78.4, 77.9, 77.0, 77.1, 75.0]
      - name: "Operating margin"
        values: [65.9, 65.3, 65.5, 66.2, 66.4, 67.3, 67.9]
    refs:
      - value: 73.0
        label: "Q4 FY26 gross margin guide"
    note: "Gross margin is falling as memory-heavy custom chips grow, and Broadcom guides it to about 73 per cent this quarter. Operating margin has held because costs grow far more slowly than revenue."
    source: "Broadcom results releases, 6 March 2025 to 2 September 2026; Q4 FY26 guide from the call of 2 September 2026."
  - id: price
    title: "Broadcom share price, month-end close, US$"
    kind: line
    prefix: "US$"
    decimals: 2
    labels: ["Sep 23", "Oct 23", "Nov 23", "Dec 23", "Jan 24", "Feb 24", "Mar 24", "Apr 24", "May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
    series:
      - name: "Close"
        values: [83.06, 84.14, 92.57, 111.62, 118.0, 130.05, 132.54, 130.03, 132.85, 160.55, 160.68, 162.82, 172.5, 169.77, 162.08, 231.84, 221.27, 199.43, 167.43, 192.47, 242.07, 275.65, 293.7, 297.39, 329.91, 369.63, 402.96, 346.1, 331.3, 319.55, 309.51, 417.43, 446.77, 377.75, 389.28, 370.34, 351.19, 362.51]
    note: "The shares closed at US$362.51 on 5 October 2026, 25 per cent below their highest close of US$481.57 on 2 June, even though Broadcom has raised its AI outlook since."
    source: "Nasdaq.com historical prices, retrieved 6 October 2026. The last point is the close on 5 October 2026."
---

Broadcom's shares closed at US$362.51 on 5 October 2026. On 2 June they closed at US$481.57, the highest of the past year. Since then Broadcom has beaten its own AI forecast, raised it, and told investors to expect US$230 billion of AI revenue in fiscal 2028.

My piece of 2 October argued something narrower. Broadcom is paid whether the cloud giants stay with Nvidia or leave. If they stay, their chips talk across Broadcom's switches. If they leave, Broadcom very often designs the chip they leave with.

The results support that claim. The question for the shares is different. The price assumes Broadcom's AI revenue barely grows after next year, and the risk behind the growth has moved from customer power to customer credit.

## The thesis

Go back to the tailor from the October piece. A shirt off the rail fits most people well enough. Ten thousand shirts for exactly the same body are worth having made. Very few workshops can cut cloth at that standard, and one of them also makes the zip sewn into almost every shirt on the rail.

**Both halves of the workshop are growing.** In the quarter to 2 August 2026, Broadcom's AI revenue was US$16.7 billion, up 221 per cent on a year earlier. On the call of 2 September, Hock Tan, the chief executive, said custom accelerator shipments were 73 per cent of it. That is about US$12.2 billion of custom chips and US$4.5 billion of networking. Custom chips grew more than three and a half times in the year, and AI networking more than two and a half times.

**The zip still goes on every rail.** Charlie Kawwas, who runs the chip business, said Tomahawk 6 is deployed at pretty much every AI customer building custom chips with Broadcom. He added that even those not using its custom chips are using Tomahawk 6. In June Hock Tan said Broadcom sells networking into clusters that use no Broadcom custom chips. That is the half of the toll paid by buyers who stay with Nvidia.

**But the tailor now earns most of it.** Networking's share of AI revenue was 35 per cent in the quarter to 3 August 2025, a third in the quarter to 1 February 2026 and almost 40 per cent in the quarter to 3 May. In the quarter to 2 August it fell to 27 per cent. Tan said in June that 40 per cent was probably the peak and about 30 per cent the more likely level. Broadcom does not say how much of its networking goes into Nvidia clusters.

So my piece's first test, networking's share, has moved against the stay half. The claim survives because Tan expects networking to grow as fast as custom chips over the next few years. But the money increasingly comes from buyers who leave.

**The supply behind it is physical, and Broadcom has bought it.** The 10-Q for the quarter to 2 August shows US$126.8 billion of unconditional purchase commitments, mostly inventory. Of that, US$52.7 billion falls in fiscal 2027 and US$73.0 billion in fiscal 2028. Broadcom will open its own substrate plant in Singapore from fiscal 2027. Kawwas said its indium phosphide laser factories are more than tripling capacity. Firm contracted revenue across both segments, its remaining performance obligations, reached US$179.2 billion.

**The other tests.** The custom customer count is still six, unchanged since March. On Google, Tan said Broadcom is now shipping TPU version 8i ahead of MediaTek's version 8t, which was started earlier. In April Google signed a long-term agreement for Broadcom to develop and supply future TPU generations. A separate supply assurance agreement covers networking and other components for Google's next AI racks through up to 2031. Gross margin keeps falling, as my piece feared: from 78.4 per cent a year earlier to 75.0 per cent, and about 73 per cent guided this quarter.

The reason is memory, not price. Amie Thuener, the finance chief, said custom chips carry rising memory content that dilutes the margin. Operating margin rose to 67.9 per cent and is guided at 66 per cent. The toll per dollar of operating profit has not thinned. The toll per dollar of sales has.

**Where I was wrong in October.** My piece's exposure map said: "Google, Meta, Anthropic and OpenAI design their own AI chips with Broadcom for their own data centres." That is wrong for Anthropic on the chip, and too loose on the data centres. Broadcom's 8-K of 6 April 2026 says Anthropic will "access through Broadcom" next generation "TPU-based AI compute capacity". The TPU is Google's chip.

On the December 2025 call Tan described Anthropic's first orders as TPU Ironwood racks. On the September call he said Broadcom delivered Ironwood TPUs in volume "to both Anthropic and Google". The 10-Q adds that, for a customer it does not name, a financial partner bought racks for more than one gigawatt of compute and leases them to that customer. Broadcom backstops those lease payments, up to about US$29 billion. Thuener said on the September call that this first US$35 billion tranche is for Anthropic's one gigawatt deployment. So the racks are leased, not owned. The filings do not say where they are hosted, so "their own data centres" claimed more than I knew.

What showed me the slip was reading the April 8-K against my own exposure map. It matters more than a label. Tan expects Anthropic to become Broadcom's largest custom chip customer in 2027. So the two largest buyers run one chip family, the TPU, which is the family Google has split with MediaTek. The claim still holds, because Broadcom is paid on those TPUs. The piece and the claim stay exactly as published.

## What the market prices in, and where I differ

At US$362.51 Broadcom is worth about US$1,731 billion on its 4,774 million shares. It has US$35.4 billion more debt than cash. The shares trade at 31 times my fiscal 2026 non-GAAP earnings of US$11.62 and 20 times my fiscal 2027 estimate. On the stockanalysis.com consensus they trade at 19 times fiscal 2027. The average analyst target is US$531.85.

**What the price needs.** By October 2027 the market will be pricing fiscal 2028, the year to about 29 October 2028. I value the chip business at 20 times after-tax operating profit and software at 17 times, then subtract net debt. On those multiples and my margins, US$362.51 needs fiscal 2028 AI revenue of about US$127 billion. That is only 11 per cent above the US$115 billion Broadcom expects in fiscal 2027.

**Where I differ.** Management says it has line of sight to US$230 billion in fiscal 2028, and that it has secured the supply for both years. Tan said Broadcom is on target to exceed US$30 of earnings a share. He also said timely deployment is "always very much in our mind" when Broadcom sets its outlook, and that customers' land, power and shell are already reflected in it.

I still take less, and the haircut is my own judgement. First, credit: most of the growth to fiscal 2028 comes from two labs that must raise money to pay, which I return to below. Second, in my view doubling deployed capacity in a single year leaves little room for a late building or grid connection, however carefully it was planned.

But the price assumes far less than a cautious reading. I take US$190 billion, 17 per cent below management's figure and 65 per cent above fiscal 2027. The purchase commitments are the physical evidence: Broadcom has already contracted US$73.0 billion of supply for fiscal 2028.

**What I worry about is credit, not power.** My piece said the risk sits with a handful of very powerful customers. The bigger risk now is that two of them must borrow to buy. Tan expects Anthropic to be the largest custom customer in 2027 and OpenAI the second largest in 2028. Broadcom built the AI XPV platform with financial partners to fund more than 20 gigawatts for them by the end of 2028.

The first tranche carries the US$29 billion backstop, and the customer may issue Broadcom up to US$42 billion of convertible notes. The 8-K of 6 April says Anthropic's use of the capacity "is dependent on Anthropic's continued commercial success". Broadcom says future tranches will be tailored and it has announced none. That is the reason for medium conviction rather than high.

## Valuation, with the working

I value Broadcom as two businesses. Semiconductors, AI and non-AI, are valued at a chip multiple. Infrastructure software, mostly VMware, is valued at a software multiple. Software sits outside the layer this site covers, so it gets its own price. Both use non-GAAP after-tax operating profit for fiscal 2028, the year the market will price in October 2027.

Non-GAAP figures leave out stock-based pay, US$2.0 billion in the August quarter, and acquisition amortisation. Over the first three quarters of fiscal 2026, GAAP earnings were US$6.09 a share against US$7.81 non-GAAP.

**Fiscal 2026.** Three quarters are reported. The fourth is the guide: US$34.8 billion of revenue, of which US$21.7 billion is AI and about US$4.3 billion non-AI chips, and a 66 per cent operating margin. With the guided 16 per cent tax rate and 4.94 billion shares, that gives US$3.81 a share for the quarter and US$11.62 for the year. The consensus is US$11.66.

**Fiscal 2027.** I take management's US$115 billion of AI revenue, US$17.5 billion of non-AI chips and US$33.5 billion of software. The chip segment earns a 60 per cent operating margin, against 61.3 per cent in the August quarter. Software earns 81 per cent, against 83.7 per cent. That gives US$17.76 a share, 8 per cent below the consensus of US$19.39, which assumes about 5 per cent more revenue.

**Fiscal 2028.** AI revenue is US$190 billion, non-AI chips US$18 billion and software US$35.5 billion. The chip margin falls to 58 per cent as memory-heavy racks grow. Earnings are US$25.15 a share. The estimates below are mine, except the history and guide.

| | FY24 | FY25 | Q4 FY26 guide | FY26 mine | FY27 mine | FY28 mine |
|---|---|---|---|---|---|---|
| Revenue, US$ billion | 51.6 | 63.9 | 34.8 | 105.9 | 166.0 | 243.5 |
| AI semiconductors, US$ billion | 12.2 | 20.2 | 21.7 | 57.6 | 115.0 | 190.0 |
| Infrastructure software, US$ billion | 21.5 | 27.0 | 8.7 | 31.4 | 33.5 | 35.5 |
| Non-GAAP gross margin | 76.5% | 78.6% | 73% | 75.1% | | |
| Non-GAAP operating margin | 59.6% | 65.7% | 66% | 66.9% | 64.2% | 61.4% |
| Non-GAAP EPS, US$ | 4.87 | 6.82 | | 11.62 | 17.76 | 25.15 |
| Consensus EPS, US$ | | | | 11.66 | 19.39 | |
| Price to earnings at US$362.51 | | 53x | | 31x | 20x | 14x |

The consensus comes from stockanalysis.com, using S&P Global data last updated on 2 October. I could not verify a fiscal 2028 consensus. Fiscal years end on the Sunday closest to 31 October: fiscal 2026 ends on 1 November 2026 and fiscal 2027 on about 31 October 2027.

**The multiples.** For chips I use 20 times, just below the 20.7 times median forward multiple of five chip peers on stockanalysis.com on 6 October: AMD at 56.9 times, Marvell 53.4, TSMC 20.7, Nvidia 19.8 and Qualcomm 19.5. For software I use 17 times, about the median of five: ServiceNow at 30.0, Microsoft 26.6, IBM 17.4, Oracle 16.7 and Adobe 8.9.

**The base case.** Chips are worth about US$410 a share and software about US$83, less US$7 of net debt. I hold net debt and the share count flat, on the assumption that cash left after dividends goes to buybacks that offset dilution. That gives US$486, 34 per cent above the price.

**Three cases, twelve months out.** Software and non-AI chips are the same in all three.

| Case | What happens | FY28 AI revenue | Chip margin | Multiples | Value | Change |
|---|---|---|---|---|---|---|
| Bear | Lab financing stalls: no AI growth after fiscal 2027 | US$115bn | 52% | 14x and 14x | US$226 | down 38% |
| Base | Deployment slips behind management's plan | US$190bn | 58% | 20x and 17x | US$486 | up 34% |
| Bull | Management's plan arrives in full | US$230bn | 60% | 22x and 20x | US$647 | up 79% |

Weighted 25, 50 and 25 per cent, the three cases give about US$461, 27 per cent above the price. The bear case is not fanciful. The shares fell 28 per cent between the end of December 2024 and the end of March 2025, and closed at US$293.41 as recently as 30 March 2026.

**The band.** I go long when my base value is at least 15 per cent above the price, and short when it is at least 25 per cent below. At US$486, 34 per cent above, Broadcom clears the long threshold. The target is US$485.

**How sensitive it is.** Each row is fiscal 2028 AI revenue and each column the chip multiple, with software at 17 times.

| FY28 AI revenue | 16x | 20x | 24x |
|---|---|---|---|
| US$150bn | US$341 | US$407 | US$474 |
| US$190bn | US$404 | US$486 | US$568 |
| US$230bn | US$467 | US$565 | US$663 |

Eight of the nine cells sit above the price, and six by more than 15 per cent. The only cell below it needs both fiscal 2028 AI revenue of US$150 billion and a chip multiple of 16 times.

<div class="charts-slot"></div>

## Risks, and what would change my view

**The labs cannot pay.** Anthropic and OpenAI are set to be the two largest custom chip buyers, and both depend on raising capital. Broadcom backstops up to US$29 billion of one lab's rack leases, and may hold up to US$42 billion of its notes. If later tranches carry similar terms, Broadcom's exposure grows with its revenue. This is the bear case, and it is a 38 per cent fall.

**Concentration.** Broadcom's top five end customers took about 55 per cent of revenue in the August quarter, against about 40 per cent a year earlier. One distributor took 50 per cent. Two of the four largest custom buyers run the TPU, the family Google has split with MediaTek.

**The exit door swings both ways.** Every custom buyer has its own chip team. Google started MediaTek's version 8t before Broadcom's 8i, and could move more work. The long-term agreement of April covers future TPU generations, but it does not say Broadcom supplies all of them.

**Margin dilution.** Gross margin has fallen 3.4 points in a year and is guided down again. If racks with more memory and bought-in parts grow faster than operating leverage, operating margin falls too. My base already takes the chip margin from 61 to 58 per cent.

**Nvidia's networking.** Nvidia sells its own Ethernet and scale-up links. If they win inside Nvidia's clusters, Broadcom's stay half shrinks further than the 27 per cent share already shows.

**What would change my view.** Out of the long: a price above about US$423 with my numbers unchanged, which leaves the base less than 15 per cent above it. Or evidence that cuts fiscal 2028 AI revenue towards US$150 billion and the chip multiple towards 16 times together. Into more conviction: a second financing tranche without a Broadcom backstop, or a third custom customer reaching volume.

The fourth quarter results, for the quarter to 1 November, are planned for 9 December 2026, as Broadcom said on its September call. That release should also give the guide for the first quarter of fiscal 2027.

## Conclusion

My piece of 2 October argued that Broadcom is paid whether the cloud giants stay with Nvidia or leave. The year of results behind it supports that claim. Custom chips and AI networking both grew more than two and a half times, and Tomahawk 6 sits in clusters that use no Broadcom custom chips. But the custom half now earns almost three quarters of the AI money. I was wrong about one thing: Anthropic does not design its own chip with Broadcom; it uses Google's TPU.

The price does not believe the next step. At US$362.51 it assumes fiscal 2028 AI revenue of about US$127 billion, against management's US$230 billion and my US$190 billion. My call is long, with medium conviction and a target of US$485. The range runs from US$226 to US$647. The view is wrong if the shares close below US$270 by October 2027.

<p class="sources">Sources: Broadcom quarterly results releases on Form 8-K, Exhibit 99.1, from 12 December 2024 to 2 September 2026, with their comparative columns, for revenue, segment revenue, AI semiconductor revenue, non-GAAP margins, earnings per share, stock-based pay, cash, debt and the fourth quarter guide. Broadcom Form 10-Q for the quarter to 2 August 2026, filed 10 September 2026, for shares outstanding, remaining performance obligations, purchase commitments, the AI XPV platform, the Backstop, the convertible notes, customer concentration and segment operating income. Broadcom Form 8-K of 6 April 2026 on the Google long-term agreement and Anthropic's access to TPU-based compute. Broadcom earnings calls of 4 September 2025, 11 December 2025, 4 March, 3 June and 2 September 2026, for the custom chip and networking shares, customer count, TPU and MediaTek, gross margin, the fiscal 2027 and 2028 outlook, the AI XPV platform, substrates and lasers, and the results date. Share prices are Nasdaq.com closes, retrieved 6 October 2026. Consensus earnings, average target and peer multiples from stockanalysis.com, retrieved 6 October 2026. Estimates for fiscal 2026 to 2028 and the sum of the parts are the author's own. Personal research, not investment advice.</p>
