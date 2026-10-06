---
title: "Oklo sells electricity it has not yet made. At US$36, the shares price a bigger fleet than all the customers it has announced."
summary: "Oklo designs small fast reactors that it plans to own, selling the power under long contracts. It has no binding power contract yet, has not disclosed what its first plant costs, and funds the build by selling shares. At US$35.97 the market prices about 17 GW running by 2040 at my base costs, more than the 13.2 GW its customers have signed up to in principle."
company: "Oklo"
ticker: "OKLO"
exchange: "NYSE"
claims: ["oklo-sells-the-electricity"]
correction: "I wrote that Oklo's cash and securities rose about US$1.9 billion in the first half of 2026. They rose about US$1.6 billion; US$1.9 billion is what it raised, and the gap of about US$258 million is what Oklo spent running the business and building, mainly US$65.5 million of operating cash and US$126.9 million of capital spending."
keyPoints:
  - "Oklo designs Aurora, a 75 MW sodium-cooled fast reactor, and plans to own each plant and sell the power. Its first, in Idaho, is targeted for 2028, and nothing is under a binding power purchase agreement yet."
  - "The build is paid for by shareholders. Oklo raised US$1.85 billion net in the first half of 2026 and about US$320 million more by 10 September, at an average price that fell from US$97 to about US$44, and opened another US$1 billion programme on 11 September."
  - "At US$35.97 the shares are worth about 2.2 times my estimate of Oklo's cash. On my base plant economics, the price needs about 17 GW running by 2040, more than the 12 GW Switch and 1.2 GW Meta agreements combined."
  - "My call is short, with low conviction and a twelve-month target of US$28, my probability-weighted value. My base case is worth about US$13.50, 62 per cent below the price, but it rests on a plant cost and a power price Oklo does not disclose, and the bull case doubles the price."
  - "Where I was wrong: my September piece said cash rose about US$1.9 billion in the first half. It rose about US$1.6 billion; US$1.9 billion is what Oklo raised."
files:
  pdf: "/research/2026-10-06_Oklo_Initiation.pdf"
  xlsx: "/research/2026-10-06_Oklo_Model.xlsx"
  thumb: "/research/2026-10-06_Oklo_Initiation-p1.png"
  pages: 5
date: 2026-10-07T01:10:29+08:00
draft: false
call:
  direction: "SHORT"
  price: 35.97
  priceDate: 2026-10-05
  currency: "US$"
  target: 28
  horizon: "12 months, to October 2027"
  conviction: "Low"
  wrongIf: "By October 2027, Oklo signs a binding power purchase agreement for 500 MW or more; or it discloses an Aurora-INL cost at or below US$6,000 a kilowatt and the NRC accepts a licence application for a commercial site; or the shares close above US$60, on the path to my bull case."
charts:
  - id: cash
    title: "Cash and marketable securities at quarter end, US$ billion"
    kind: bar
    prefix: "US$"
    unit: "bn"
    decimals: 2
    labels: ["Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Cash and securities"
        values: [0.29, 0.29, 0.28, 0.26, 0.68, 1.18, 1.41, 2.54, 3.01]
    note: "The pile grew because Oklo sold shares, not because it earned money. Shares outstanding rose from 122.1 million in June 2024 to at least 192.3 million by 10 September 2026."
    source: "Oklo Forms 10-Q and 10-K, June 2024 to 30 June 2026, via SEC XBRL. Cash and equivalents plus current and non-current marketable debt securities."
  - id: spend
    title: "Operating cash use plus capital spending by quarter, US$ million"
    kind: bar
    prefix: "US$"
    unit: "m"
    labels: ["Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26"]
    series:
      - name: "Operating cash use"
        values: [10, 8, 13, 12, 18, 18, 33, 18, 48]
      - name: "Capital spending"
        values: [0, 0, 0, 0, 1, 5, 27, 33, 94]
    refs:
      - value: 146
        label: "2026 guide midpoint, per quarter"
    note: "Spending reached US$142 million in the second quarter. Oklo's 2026 guide of US$520 to 650 million implies more in the second half."
    source: "Oklo Forms 10-Q and 10-K via SEC XBRL, quarterly flows derived from year-to-date figures; guide from the business update of 7 August 2026."
  - id: pipeline
    title: "Announced customer capacity against what the price needs, GW"
    kind: bar
    unit: "GW"
    decimals: 1
    labels: ["Binding PPAs", "Meta (prepayment)", "Switch (master)", "My base by 2040", "Price needs by 2040"]
    series:
      - name: "GW"
        values: [0, 1.2, 12.0, 3.7, 16.8]
    note: "My reading of the filings is that no megawatt is under a binding power purchase agreement. The last two bars are my estimates: the fleet in my base case, and the fleet the share price needs at my base costs."
    source: "Oklo Form 10-Q for the quarter to 30 June 2026 and Form 10-K for 2025; Oklo and Meta announcement, 9 January 2026; author's model."
  - id: price
    title: "Oklo share price, month-end close, US$"
    kind: line
    prefix: "US$"
    decimals: 2
    labels: ["May 24", "Jun 24", "Jul 24", "Aug 24", "Sep 24", "Oct 24", "Nov 24", "Dec 24", "Jan 25", "Feb 25", "Mar 25", "Apr 25", "May 25", "Jun 25", "Jul 25", "Aug 25", "Sep 25", "Oct 25", "Nov 25", "Dec 25", "Jan 26", "Feb 26", "Mar 26", "Apr 26", "May 26", "Jun 26", "Jul 26", "Aug 26", "Sep 26", "5 Oct 26"]
    series:
      - name: "Close"
        values: [10.07, 8.47, 9.10, 5.97, 8.09, 22.46, 23.54, 21.23, 41.61, 33.39, 21.63, 23.74, 52.72, 55.99, 76.59, 73.64, 111.63, 132.77, 91.38, 71.76, 79.62, 62.95, 49.59, 72.50, 66.88, 52.33, 38.83, 40.57, 37.02, 35.97]
    note: "The shares peaked at US$193.84 during trading on 15 October 2025 and closed highest at US$174.14 the day before. They have since fallen 79 per cent from that close, as Oklo sold shares at ever lower prices."
    source: "Yahoo Finance monthly closes, retrieved 6 October 2026. Listed as OKLO from May 2024. The last point is the close on 5 October 2026."
---

Oklo's shares closed at US$35.97 on 5 October 2026. That is 79 per cent below their highest close, US$174.14 on 14 October 2025, and just above the year's lowest close, US$35.62 on 16 September.

In September I argued that Oklo is a seller of electricity, not reactors, and that the model stands or falls on building its first plant. The year since the peak has tested the second half of that more than the first. Oklo has kept to its model. What it has not yet shown is what a plant costs, what a customer will pay for its power, or a single binding contract.

So the question for the shares is simple to state. How many reactors does the price assume Oklo builds, and at what margin? My answer is more than all the customers it has announced.

## The thesis

Go back to the coffee supplier from the September piece. It installs the machine, keeps owning it and charges for every cup, for years. Now picture that supplier before it has installed a single machine. It has signed letters with offices that like the idea. It has not agreed a price per cup. It does not yet know what its own machine costs to build. And it pays its bills by selling slices of the company.

That is Oklo today. Its reactor, Aurora, is a 75 MW sodium-cooled fast reactor descended from EBR-II. Oklo plans to own each plant and sell the power under power purchase agreements, or PPAs. Its 10-Q for the quarter to 30 June 2026 says the primary business model is to sell the energy, as opposed to selling the design.

The model has held. The 10-Q also says that Oklo intends to offer customers "flexibility in business model" as its technology matures, and that it is raising capital "at the corporate and asset levels". Neither is a sale of reactors, so the first half of the claim stands. Both are worth watching.

The building has moved, on two tracks. Oklo broke ground on Aurora-INL at Idaho National Laboratory on 22 September 2025, under the Department of Energy rather than the Nuclear Regulatory Commission. The department approved its nuclear safety design agreement early in 2026 and its preliminary documented safety analysis on 11 June: two of the five steps on that path. Oklo targets commercial operation in 2028. At groundbreaking it spoke of late 2027 or early 2028.

Its second reactor shows that the team can build. Groves, a small isotope test reactor in Texas, went from greenfield to first criticality on 5 August 2026, under the same Department of Energy programme. It makes no electricity, but it is a real reactor built on private land with private money.

What the filings do not show is the money that would make each Aurora worth building. Oklo has not disclosed what Aurora-INL will cost. In August its finance chief said the total was still being narrowed with Kiewit, the lead constructor. Nor has it disclosed a power price. The only customer cash on its 30 June balance sheet is a US$25 million payment from 2024 for a right of first refusal.

The contracts are where the September claim set its sharpest test: whether the letters of intent stay letters. On my reading, they still do. The 10-K says Oklo has entered into non-binding agreements such as master power agreements and letters of intent, that many of them are non-binding, and that it is negotiating binding PPAs with customers who signed non-binding agreements. Its 10-Q calls the 12 GW Switch agreement one of the largest corporate PPAs in history, but no filing calls it binding, and I count none of it as a binding PPA. Equinix, Diamondback Energy and Prometheus Hyperscale have signed non-binding letters of intent. Meta signed a prepayment agreement on 5 January 2026 for a 1.2 GW campus in Pike County, Ohio, with the first phase as early as 2030 and the full 1.2 GW by 2034. In the piece I called that a binding prepayment. The 10-Q says the agreement provides a mechanism for Meta to prepay for power, which Oklo will use to secure fuel. It discloses no amount, the 30 June balance sheet shows no customer prepayment beyond the 2024 payment, and the agreement is not a PPA.

Fuel is the other gate. The first core is covered by a five tonne Department of Energy award of high-assay low-enriched uranium, or HALEU, recovered from old EBR-II fuel. Beyond that, Oklo has a letter of intent with Centrus Energy for up to five Auroras from 2029, and was selected in May for talks on surplus government plutonium. None is a firm supply contract.

**Where I was wrong in September.** In the piece I wrote that cash and marketable securities "stood at $3.0 billion at 30 June, about $1.9 billion more than at the start of the year, raised mainly by issuing new shares." The US$3.0 billion was right. The rise was not. The balance sheet shows US$1,412.5 million at 31 December 2025 and US$3,006.3 million at 30 June 2026, a rise of about US$1.6 billion.

The US$1.9 billion is what Oklo raised. Its share sales brought in US$1,880 million gross and US$1,852 million net in the half. The gap of about US$258 million is what went out: US$65.5 million of operating cash, US$126.9 million of capital spending, US$25.7 million on two acquisitions, US$16.5 million of other investments and US$16.9 million moved into restricted cash. Those add to about US$251.5 million; most of the remaining US$7 million is unrealised losses and accretion on the securities.

What showed me the slip was rebuilding the cash bridge from the balance sheet and the cash flow statement, which I had not done for the piece. The view did not change. If anything the mistake sits on the claim's side: the money raised and the money kept are already drifting apart, because Oklo is spending to run the business and to build, US$126.9 million of it on plant. The piece and the claim stay exactly as published, so the record shows the mistake.

## What the market prices in, and where I differ

At US$35.97 Oklo is worth about US$6.9 billion on at least 192.3 million shares. That count adds the 7.26 million shares Oklo sold between 1 July and 10 September to the 185.1 million it had at 30 June. My estimate of cash and securities at 30 September is about US$3.1 billion, so the market values the business beyond its cash at about US$3.8 billion, or 2.2 times cash in all.

The fall has two parts. The first is the whole group. Over the same twelve months NuScale fell 86 per cent from its highest close and NANO Nuclear 73 per cent, against Oklo's 79. The second is Oklo's own funding. It sold shares at an average of US$96.95 in the first quarter, US$63.51 in the second and about US$44 between July and 10 September. On 11 September it opened another US$1 billion programme, and the shares fell 9.2 per cent that day, from US$39.88 to US$36.22. Shares outstanding are up 58 per cent since June 2024.

Analysts are more positive than the price. The 25 tracked by stockanalysis.com have an average target of US$75.78, more than twice the price, and 18 per cent of the shares are sold short.

**What the price needs.** I value Oklo as a fleet of plants, which is the only way to value a company with no revenue from its main product. On my base economics, each 75 MW Aurora earns about US$590,000 a megawatt in its first year and is worth about US$1.35 million a megawatt more than it costs once it runs. To justify US$35.97, Oklo needs about 1.9 GW of new units a year from 2033 to 2040, or about 17 GW running by 2040. My base case has 3.7 GW.

That 17 GW is more than the 12 GW Switch agreement and the 1.2 GW Meta campus combined, and none of it is yet under a PPA. Put the other way, at my base fleet the price needs each plant to cost about US$3,200 a kilowatt, against my base of US$7,500.

**Where I differ.** Not on the claim, which is holding, but on what is already in the price. The market prices Oklo as though the hard part is behind it. The hard part, a cost per kilowatt and a power price that leave a margin, has not been disclosed. The only recent Western small reactor costing I can check is Ontario's: C$20.9 billion for four 300 MW BWRX-300 units at Darlington, about C$17,400 a kilowatt. Oklo's design is simpler and smaller, but my base already assumes well under half of that.

## Valuation, with the working

Oklo has no earnings, so a multiple of them means nothing. I value it plant by plant, in three steps, twelve months out, to October 2027. The estimates are mine; Oklo gives no cost, price or fleet guidance.

**One plant.** A 75 MW Aurora runs at 90 per cent of capacity, sells power at US$110 a megawatt hour and costs US$35 a megawatt hour to run, fuel and decommissioning included. Both rise 2 per cent a year for 40 years. Discounted at 8 per cent, the margin is worth about US$8.85 million a megawatt. At my base cost of US$7,500 a kilowatt, that leaves US$1.35 million a megawatt. The break-even cost at that price is about US$8,850 a kilowatt.

**The fleet.** Aurora-INL first runs in mid-2028, with US$400 million still to spend after September 2027. Meta's 1.2 GW follows from 2030 to 2034, then 300 MW a year to 2040. I discount each plant's value at 10 per cent from its first year back to October 2027, and multiply by a 60 per cent chance that Aurora-INL reaches commercial operation on that timetable. If it does not, I assume the fleet does not follow.

**The company.** To the risked fleet I add my cash at September 2027, about US$2.38 billion, and subtract the present value of corporate, fuel, recycling and isotope spending, about US$1.24 billion. I divide by 201.8 million fully diluted shares, including 5.7 million options and 3.7 million share units. I model no tax and no tax credits.

| | 2024 | 2025 | H1 2026 | 2026 guide | 2026 mine | 2027 mine |
|---|---|---|---|---|---|---|
| Revenue, US$ million | 0 | 0 | 1.2 | | 2.7 (consensus) | |
| Net loss, US$ million | 73.6 | 105.7 | 81.6 | | | |
| Operating cash use, US$ million | 38.4 | 82.2 | 65.5 | 120 to 150 | 140 | 170 |
| Capital spending, US$ million | 0.4 | 33.2 | 126.9 | 400 to 500 | 450 | 550 |
| Cash and securities at the end, US$ million | 275 | 1,413 | 3,006 | | 2,924 | 2,204 |
| Shares outstanding at the end, million | 137.7 | 160.5 | 185.1 | | | |

The 2026 and 2027 cash figures add the US$315 million net raised from July to September and exclude any sales under the new programme. The guide is from the update of 7 August, when Oklo raised it from US$80 to 100 million and US$350 to 450 million.

**Three cases, twelve months out.**

| Case | What happens | Price, cost | Value | Change |
|---|---|---|---|---|
| Bear | Aurora-INL slips past 2029 and the numbers do not close; no fleet, spending winds down | US$95, US$10,000/kW | US$9.87 | down 73% |
| Base | 60% chance Aurora-INL runs in 2028; Meta's 1.2 GW by 2034, then 300 MW a year | US$110, US$7,500/kW | US$13.51 | down 62% |
| Bull | 80% chance; cheap plants; Switch and others contract 900 MW a year from 2033 | US$125, US$6,000/kW | US$76.81 | up 114% |

Weighted 25, 50 and 25 per cent, the three cases give about US$28.43, 21 per cent below the price. The bear case is close to cash: Oklo would still hold about US$11.81 a share in September 2027, which limits how far the value falls in my three cases, though grid cells where new units do not pay go lower, to about US$6. The bull case reaches 8.5 GW by 2040, and even that needs 7.2 GW beyond Meta, 60 per cent of the Switch agreement, turned into contracts.

**How sensitive it is.** Each row is a cost per kilowatt and each column a power price, at the base probability and build rate.

| Cost per kW | US$95/MWh | US$110/MWh | US$125/MWh |
|---|---|---|---|
| US$6,000 | US$11.72 | US$21.38 | US$31.04 |
| US$7,500 | US$6.04 | US$13.51 | US$23.17 |
| US$10,000 | US$6.04 | US$6.41 | US$10.05 |

None of the nine cells reaches the price. The highest, cheap plants and dear power together, gives US$31.04. Where new units do not pay, only Aurora-INL is built, so two cells share the same low value. What closes the gap to the price is scale, not margin.

**Peers.** On enterprise value per gigawatt of announced customer capacity, Oklo is the cheapest of the listed group. It is about US$0.29 billion a gigawatt on 13.2 GW, against US$0.37 billion for NuScale on its non-binding 6 GW with TVA and ENTRA1, and US$0.85 billion for X-energy on Amazon's up to 5 GW. NANO Nuclear, at about US$0.25 billion, has no gigawatt-scale agreement. The whole group is priced on announced capacity, and on that measure Oklo is not the dear one.

<div class="charts-slot"></div>

## Risks, and what would change my view

**The first plant slips or costs more.** The claim's own test. Aurora-INL has already moved from late 2027 or early 2028 to 2028, and Oklo raised its 2026 spending guide in August, citing first-of-a-kind costs at the plant. A further slip, or a cost well above my base, takes the base case towards the bear.

**Dilution below value.** Oklo funds the build with shares, and each programme has sold lower than the last. My base fleet needs about US$27 billion of plant spending by 2040. Even with most of it borrowed against contracted plants, shareholders will be asked for billions more. If they are asked at prices below what the plants are worth, existing holders lose value even if the plants succeed.

**The contracts stay paper.** The September claim breaks if the letters of intent stay letters. Twenty-two months after the Switch agreement, on my reading of the filings, no megawatt is under a binding PPA. Every year without one, buyers fill the need with gas, existing nuclear or fuel cells.

**Fuel.** Beyond the first core, HALEU supply rests on a Centrus letter of intent from 2029 and talks on government plutonium. A firm contract would lower this risk.

**The risks to the short.** These are why conviction is low. The two decisive inputs are undisclosed, so the base case is my assumption stack. A first binding PPA at a good price, a plutonium allocation or a low disclosed cost could each move the shares sharply up, and 18 per cent of them are already sold short. Oklo is also cheaper per announced gigawatt than its listed peers.

**What would change my view.** Towards a higher conviction short: Oklo disclosing an Aurora-INL cost that implies more than about US$10,000 a kilowatt, or another share sale below my weighted value. Out of the short: a binding PPA of 500 MW or more, a disclosed cost at or below about US$6,000 a kilowatt with the NRC accepting a licence application for a commercial site, or a close above US$60. Below about US$14, my base value, the short would have done its work and I would close it.

The third quarter results have no date yet. Last year Oklo announced the date on 29 October and reported on 11 November. The Centrus definitive agreement, the plutonium allocation and the remaining Department of Energy steps for Aurora-INL are the other dates to watch.

## Conclusion

The September piece argued that Oklo sells electricity, not reactors, and that the model stands or falls on building its first plant. Both halves hold. Oklo has kept to its model, broken ground in Idaho and taken Groves critical in eleven months. But no customer has yet signed a binding contract, no plant cost has been disclosed, and shareholders are paying for the build. I was wrong about one figure: cash rose about US$1.6 billion in the first half, not US$1.9 billion.

At US$35.97 the market prices about 17 GW running by 2040 at my base costs, more than all the customers Oklo has announced. My call is short, with low conviction and a twelve-month target of US$28, my probability-weighted value and 22 per cent below the price. The base value is about US$13.51 and the range runs from US$9.87 to US$76.81. The short is wrong if Oklo signs a binding PPA of 500 MW or more, discloses a plant cost at or below US$6,000 a kilowatt with an NRC application accepted, or the shares close above US$60.

<p class="sources">Sources: Oklo Form 10-Q for the quarter to 30 June 2026, filed 7 August 2026, for the balance sheet, statements of operations and cash flows, at-the-market share sales, acquisitions, the right of first refusal payment, customer agreements, the Meta prepayment agreement, the Centrus letter of intent, Department of Energy and Nuclear Regulatory Commission status and Groves. Oklo Form 10-Q/A for the quarter to 31 March 2026, filed 17 June 2026, which amends only a certification. Oklo Form 10-K for 2025, filed 17 March 2026, for non-binding agreements and 2025 figures. Oklo Form 8-K and prospectus supplement of 11 September 2026 for the end of the May 2026 programme, the new US$1 billion programme and options and share units outstanding. SEC XBRL company facts for quarterly history. Oklo second quarter 2026 business update and call, 7 August 2026, for guidance, the Aurora-INL target and the finance chief's remarks. Oklo and Meta announcement, 9 January 2026. Oklo groundbreaking announcement, 22 September 2025, and its third quarter 2025 results date notice, 29 October 2025. Ontario Power Generation's Darlington approval, 8 May 2025. Peer shares and net cash, consensus, analyst targets and short interest from stockanalysis.com, retrieved 6 October 2026. Share prices are Yahoo Finance closes, retrieved 6 October 2026. The valuation and estimates for 2026 to 2040 are the author's own. Personal research, not investment advice.</p>
