---
title: "Hong Kong has the plug, and the chip needs a licence"
date: 2026-10-30
summary: "Hong Kong's main utility is obliged to meet demand for electricity at the lowest reasonable cost, and last year had about a quarter more capacity than its highest demand. It is building substations for data centres faster than ever, and its one AI megasite, Sandy Ridge, drew a single bid. The hard part is the chip: under American rules Hong Kong is treated as China, so the hall's address decides the licence."
category: "Analysis"
cover: "/covers/hong-kong-has-the-plug.svg"
tags: ["grid", "power", "hong-kong", "export-controls"]
draft: true
---

Hong Kong's main utility, CLP Power, is bound by its agreement with the government to meet demand for electricity at the lowest reasonable cost. Last year it had about a quarter more capacity than its highest demand.

Its one AI megasite, Sandy Ridge, was offered to the whole industry. It drew a single bid. The winner, a mainland group, plans to let racks abroad, not run its own chips.

The chips are the hard part. Washington has treated Hong Kong as China since 2020, so the address of the hall sets the licence.

In Hong Kong the plug is being built. The chip waits on a licence.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A landlord must by law wire every flat that gets let. His fuse box carries a quarter more than the building's busiest hour. Lighting the flats is easy.</p>
<p>Filling them is not. The best fridges come from one maker abroad, whose government approves them one by one. It judges the street address and the tenant's family. Counting sockets says nothing about what is inside.</p>
</details>

## How it works

A data centre needs a connection to the grid and something to run on it. In Johor and Singapore the connection is the scarce part. In Hong Kong it is not.

Hong Kong's two power companies work under a Scheme of Control with the government. It obliges them to supply enough electricity to meet demand at the lowest reasonable cost. In return they earn a regulated return on what they build. Building for new demand is the job, not a favour.

So CLP builds substations, the yards where high voltage power is stepped down, as data centres ask for them. It has finished more for data centres since 2024 than in the six years before.

The chips are different. Under American export rules, Hong Kong has counted as China since December 2020. Advanced AI chips need an American licence there, and the best ones are presumed refused.

Since January, a defined class of chip up to Nvidia's H200, shipped straight from America to a user in Hong Kong, is judged case by case if the exporter meets the rule's conditions. The same chip for a Chinese company's hall in Johor is still presumed refused.

So in Hong Kong the licence follows the hall's address as well as the tenant's owner. Neither CLP nor Hong Kong's government decides it.

## The number that matters

CLP plans 18 substations for data centres in its plan to 2028. By June it had finished eight.

In the first nine months of 2026, CLP's sales to data centres grew by 12.8%. On my arithmetic that is an average draw of about 280 megawatts. Its system has about a quarter more capacity than its highest demand.

The government puts Hong Kong's total computing power at 5,000 petaflops, a measure of calculations per second. Sandy Ridge promises 36 times that. Neither figure says how precisely the sums are done, so treat them as scale only.

The power is there and growing. The step up in AI computing depends on chips Hong Kong does not decide.

<hr class="layer">
<p class="layer-label">For investors</p>

## The mechanism in depth

A new AI hall passes three gates: the plot, the plug and the chip. Hong Kong's government controls the first, its regulated utility is obliged to open the second, and Washington holds the third.

| Gate | Singapore | Johor | Hong Kong | Evidence for Hong Kong, dated |
|---|---|---|---|---|
| The plug | Rationed: capacity allocated through calls for applications | Connected fast, then filled slowly | The utility must meet demand under the Scheme of Control | CLP offering circular (1 April 2026); EEB reply to LegCo (1 April 2026) |
| The plot | Scarce land | Not shown as the constraint | Government tender; Sandy Ridge drew one bid | ITIB release (2 March 2026) |
| The US licence for advanced chips | Follows the tenant's headquarters, as BIS enforces it (31 May 2026) | Follows the tenant's headquarters, as BIS enforces it (31 May 2026) | Follows the hall's address and the tenant's headquarters | 85 FR 83765 (23 December 2020); 15 CFR 742.6, as revised 15 January 2026 |

The power-gated and chip-gated split is SemiAnalysis's. Its free work puts America in the first box and China in the second. I found nothing from it on Hong Kong. My addition is narrow. Legally Hong Kong sits in the chip-gated box, but on a grid obliged to build, so the plug is not what binds.

What follows is the evidence for each gate, then the one thing no primary source shows: what will run in the halls.

## CLP: a utility obliged to build

CLP Power supplies Kowloon, the New Territories and most outlying islands, about 6.4 million people. Its offering circular of 1 April 2026 states the deal plainly. Under the Scheme of Control, CLP and its generating partner CAPCO "are obliged to meet electricity demand at the lowest reasonable cost". In return they may earn "a reasonable return on their investments". The current agreement runs from 1 October 2018 to 31 December 2033.

The government told the Legislative Council the same on 1 April 2026: the power companies must supply electricity "to meet the demand, including the demand from the I&T sector", innovation and technology.

| Measure | Figure | Source |
|---|---|---|
| Capacity available to Hong Kong customers | 9,258 MW: CAPCO's plants, 70% of Daya Bay nuclear station's output, 600 MW of Guangzhou pumped storage | CLP Power offering circular, 1 April 2026; CLP Ten-year Summary |
| Local maximum demand, 2025 | 7,455 MW (7,532 MW without demand response) | CLP Ten-year Summary, 2025 |
| Local reserve margin, 2025 | About 24% more capacity than peak demand; about 19% of capacity was idle at the peak | Offering circular; my arithmetic from the Ten-year Summary |
| Demand met in 2025 | All of it; 36,989 GWh supplied to the system, down 1.13% | same |
| Data centre substations | Three in the 2018 to 2023 plan; eight finished in the 2024 to 2028 plan by June 2026, the latest two adding 260 MVA; one more due in the second half of 2026 | CLP interim results, 6 August 2026 |
| Planned by 2028 | 18 in all: six energised in 2024 and 2025, and "additional 12 data centres substations" | CLP results presentation, 26 February 2026 |

The plug is growing faster than the rest of CLP's sales, but from a small base.

| Period | CLP sales to data centres, change on a year earlier | Share of CLP sales | CLP total sales | Source |
|---|---|---|---|---|
| First half 2025 | +6.7% | not given | 16,453 GWh | Interim results, 4 August 2025 |
| Nine months 2025 | +6.7% | not given | 27,456 GWh | Quarterly statement, 20 October 2025 |
| Full year 2025 | +7.5% | not given | 35,760 GWh | Annual results, 26 February 2026 |
| First quarter 2026 | +11.1% | not given | 7,319 GWh | Quarterly statement, 18 May 2026 |
| First half 2026 | +11.8% | 7.1% | 17,038 GWh | Interim results, 6 August 2026 |
| Nine months 2026 | +12.8% | 6.6% | 28,131 GWh | Quarterly statement, 12 October 2026 |

My arithmetic, not CLP's: 6.6% of 28,131 GWh is about 1,860 GWh over the 6,552 hours of the nine months. That is an average draw of about 283 MW, or 281 to 286 MW allowing for rounding. Against a 2025 local peak of 7,455 MW, data centres are a small load on a system with headroom.

Two limits to that reading. The reserve margin is CLP's whole system, not the Northern Metropolis grid where Sandy Ridge sits. No filing I read gives a megawatt figure for Sandy Ridge. CLP says only that its power infrastructure there is "progressing at pace", with operations planned "in phases from mid-2027" (12 October 2026). Hong Kong Electric, the island's other utility, does not mention data centres in its 2025 annual or 2026 interim results.

**No record I read shows a Hong Kong data centre waiting for the grid.**

## Sandy Ridge: one site, one bid

On 2 March 2026 the Innovation, Technology and Industry Bureau awarded the Sandy Ridge Data Facility Cluster, a site of over 110,000 square metres in North District, on a 50-year land grant. "One tender was received in this exercise."

| Term | Figure | Source |
|---|---|---|
| Premium | HK$581 million | ITIB release, 2 March 2026 |
| Floor area | 250,000 sq m, about 88% high-tier data centre | same |
| Investment | HK$23.8 billion cumulative, to the third year of operation | same |
| Computing power | 180,000 petaflops by 2032, "36 times the current computing power in Hong Kong" | same; 2026 Policy Address, 16 September 2026 |
| Who decides how it is used | "the operator according to its business plan and market demand" | LegCo reply, 22 April 2026 |

The opening date depends on who is asked. The tender says within 42 months of award. The government told LegCo on 22 April 2026 to expect operations in 2029. CLP says phases from mid-2027. The tenant's own report says delivery within 2028.

The government's measure of today's base is from 16 January 2026: total computing power of 5,000 petaflops, 3,000 of them at Cyberport's AI Supercomputing Centre. Neither the base nor the target states its numerical precision, so the 36 times is a ratio of like with like, not a count of chips.

**One bid for the only AI megasite on offer says the plot was not contested.**

## Range: the tenant lets racks, not chips

The award names the ultimate holding company as Range Intelligent Computing Technology Group Company Limited. That is the foreign name the Shenzhen-listed company 300442 gives itself, in its interim report of 28 August 2026. The report defines the Hong Kong park as its Sandy Ridge intelligent computing centre project, held through two Hong Kong subsidiaries.

Its filings say four things that matter here.

| What the filing says | Source |
|---|---|
| Strategy: AI computing services at home, the "IDC rack business" abroad, Hong Kong included | Interim report, 28 August 2026 |
| Hong Kong and Batam, Indonesia, together plan about 600 MW in the short to medium term; no Hong Kong-only figure | Annual report, 10 April 2026; interim report |
| The Hong Kong park is expected to be delivered within 2028; construction in progress there was RMB 17.1 million at 30 June 2026 | Interim report |
| Its top three customers, unnamed, were 93.7% of 2025 revenue | Annual report, 10 April 2026 |

Letting racks means Range sells space, power and cooling, and its customers bring the chips. Its filings name no Hong Kong customer and say nothing about which chips will run there. At home, it describes liquid cooling adapted to domestic Chinese chips; that is about its mainland parks.

**The operator who won the plot has said it will sell the plug, and left the chip to its tenants.**

## The chip: a licence that follows the address

Since 23 December 2020 the US Bureau of Industry and Security has treated Hong Kong "the same as China" under its export rules (85 FR 83765). Hong Kong keeps a separate customs and export control system, but gets no easier American treatment.

The rule of 15 January 2026 changed the review policy for one class of chip, "the Nvidia H200 and its equivalents, as well as less advanced chips", defined by performance and memory bandwidth limits. Hong Kong is not named; it is inside China.

| Chip | Route | US review policy | Source |
|---|---|---|---|
| H200 class or below | Exported from the US to an end user located in China, Hong Kong included | Case by case, if the exporter certifies its conditions | 15 CFR 742.6(b)(10)(iii)(A)(1), 15 January 2026 |
| H200 class or below | Re-exported from abroad, or transferred within China | Presumption of denial | same |
| H200 class or below | To a company headquartered in China but located outside it, such as a hall in Johor | Presumption of denial | same |
| Above those limits | To or within China, Hong Kong included, for any tenant | Presumption of denial | same |

The conditions are heavy. The exporter must certify that US supply is sufficient, and that exports to China and Macau stay within 50% of what was shipped for use in the US. The consignee must screen remote users, and every shipment is tested by an independent laboratory in the US first.

Read together, the rules invert Johor's picture for this one class. An exporter shipping H200-class chips to a Chinese-headquartered tenant's Hong Kong hall gets case-by-case review. The same shipment to that tenant's hall in Johor faces a presumption of denial. For anything better, Hong Kong is presumed refused for every tenant, Chinese or not. That is my reading of the rule text, and it is the mechanism this piece adds.

What has actually shipped is far smaller than what the rule allows. Nvidia said on 26 August 2026 that shipments of its Hopper data centre products to China were less than 1% of its data centre revenue in the quarter to 26 July 2026, and that its outlook assumes no data centre compute revenue from China.

No primary source says what Sandy Ridge, or any Hong Kong hall, will run. It could be Nvidia chips under licence, mainland chips needing none, or nothing yet. The claim below does not depend on it.

## Claims on record

This piece absorbs no earlier piece, so it carries no older claims. Its one claim is new.

**New: Hong Kong has the plug, and the chip needs a licence** (30 October 2026)

Claim: "Hong Kong's grid is building to its data centres, not holding them back: CLP will have completed the 18 data centre substations in its 2024 to 2028 Development Plan by 31 December 2028, and Sandy Ridge's first phase will be energised by 31 December 2027."

Breaks if: "CLP's interim or annual results show fewer than 18 data centre substations completed in its 2024 to 2028 Development Plan by 31 December 2028, or Sandy Ridge's first phase is not energised by 31 December 2027."

## What would prove me wrong

The substation test is marked every six months, in CLP's interim and annual results. It is not safe. CLP finished eight in the two and a half years to June 2026 and targets one more by the end of 2026. That leaves about nine for 2027 and 2028, roughly four or five a year against about three a year so far. The 18 is also CLP's own target of "up to" that many, so demand that never arrives would miss it too.

The Sandy Ridge test is the date. CLP says phases from mid-2027, the tenant says delivery within 2028, and the government told LegCo 2029. If the first phase is not energised by the end of 2027, the claim breaks, whether the delay sits in the grid or the building.

CLP's reserve margin is context, not a test. The Ten-year Summary in each annual report gives capacity and local peak demand. A margin below 15% would tell me the plug was tightening even if the substations arrive.

The export licence is mechanism, not forecast, so it is not in the falsifier. Slow filling would not break the claim either: Range's own date is 2028, so halls may fill slowly because they are not built, not because chips are short.

## Research notes

No initiation note rests on this claim. The contrast with [Johor and Singapore](/journal/the-queue-not-the-chip/), where the connection is the scarce thing, is the subject of that deep piece.

<section class="exposure">
<h3>Who is exposed if Hong Kong has the plug and the chip needs a licence</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>The utilities</dt>
<dd><span class="names">CLP Power</span> and <span class="names">Hong Kong Electric</span> generate and deliver Hong Kong's electricity under the Scheme of Control.</dd>
<dt>The site operator</dt>
<dd><span class="names">Range Intelligent Computing</span> builds and runs data centres.</dd>
<dt>What could fill the halls</dt>
<dd><span class="names">Nvidia</span> and <span class="names">AMD</span> make the AI chips named in the US rule.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone reading Hong Kong's spare power as AI computing to come, and halls whose tenants rest on a licence decided in Washington.</dd>
</dl>
</section>

---

<p class="sources">Sources: CLP Power Hong Kong's offering circular (1 April 2026) and CLP's Ten-year Summary of Scheme of Control statistics (2025); CLP Holdings' interim and annual results and quarterly statements (4 August 2025, 20 October 2025, 26 February 2026, 18 May 2026, 6 August 2026, 12 October 2026) and results presentation (26 February 2026); Hong Kong Electric's results (17 March and 11 August 2026); the Innovation, Technology and Industry Bureau (2 March 2026), the Secretary for Innovation, Technology and Industry (16 January 2026), Legislative Council replies (1 and 22 April 2026) and the 2026 Policy Address (16 September 2026); Range Intelligent Computing Technology Group's annual, interim and third quarter reports (10 April, 28 August and 23 October 2026); the US Bureau of Industry and Security's rules of 23 December 2020 and 15 January 2026 and 15 CFR 742.6; Nvidia's CFO commentary and results release (26 August 2026). The power-gated and chip-gated framing is SemiAnalysis's, from its free articles of 13 March 2024 and 30 December 2025. Personal research, not investment advice.</p>
