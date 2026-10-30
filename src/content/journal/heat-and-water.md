---
title: "Heat and water decide where AI goes: liquid to the chip, a choice on the roof"
date: 2026-10-30T14:20:52+08:00
summary: "Almost every watt an AI chip draws comes back out as heat, and a rack of them now gives off more than air can carry. So the heat goes into liquid at the chip. That liquid runs warm enough to be cooled without evaporating water, for little extra power, which turns water from a limit on how much AI gets built into a choice about where and how each hall is cooled."
category: "Analysis"
cover: "/covers/heat-and-water.svg"
tags: ["cooling", "data-centres", "liquid", "water"]
draft: false
---

A chip does not use up electricity the way a kettle uses up water. Almost every watt that goes in comes back out as heat.

Jane Street's engineers say one cabinet of Nvidia's current flagship chips draws about 140 kilowatts at peak. That is roughly ninety space heaters in a box the size of a fridge.

Air cannot carry that away, so the heat now leaves through liquid. And once it is in liquid, the building has a choice: evaporate water to get rid of it, or spend a little more electricity and use none.

Heat decides how AI is cooled. Water decides where, not how much.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Ninety hairdryers in a shut wardrobe: no fan clears that, so you run cold water through pipes pressed against each one.</p>
<p>The pipes come out warm. Wrap them in a wet flannel on the balcony, which costs no electricity but dries the flannel, or put a fan on a radiator, which uses no water and a little more power.</p>
</details>

## How it works

A data hall has two cooling jobs. The first is inside: getting heat off the chip. The second is outside: getting that heat out of the building.

For twenty years air did the inside job. Fans pushed cold air through servers drawing a few kilowatts each. AI racks draw several times as much, and air simply carries too little heat per litre. Water carries thousands of times more.

So the mainstream answer is direct-to-chip cooling. A metal plate with liquid channels sits on each chip, and a pump unit drives coolant round the rack. Google has run this on its own AI chips since 2018.

The outside job decides the water. Heat leaves through a cooling tower, which evaporates water and is cheap in electricity, or through a dry cooler, a large radiator with fans, which evaporates nothing.

Here liquid cooling changes the trade. Chips tolerate warm coolant, and a dry cooler only needs the outside air to be cooler than the water inside. Warm water makes that true for most of the year in many climates.

Supply cannot simply catch up where water is short. An aquifer in drought cannot be enlarged, and local water rights are already spoken for. So a campus in a dry basin gives up water and pays in electricity, or goes somewhere wetter.

## The number that matters

Lawrence Berkeley National Laboratory, a US government lab, simulated every common cooling design for its December 2024 report on American data centres.

For a large liquid-cooled hall using a cooling tower, it found about 2 litres of water evaporated per kilowatt-hour of computing. With a dry cooler, almost none, and its energy efficiency barely moved.

That is the whole argument in one comparison. With liquid at the chip, going without water costs very little power, so water stops being a limit on how much gets built.

The lab also found that the power stations feeding American data centres consumed about twelve times the water the data centres did on site. Most of a data centre's water follows its electricity, not its roof.

<hr class="layer">
<p class="layer-label">For investors</p>

## The mechanism in depth

Heat leaves an AI hall in a chain of four steps. Only the last one decides the water, and only the first is new.

| Step | What carries the heat | What decides it | Evidence, dated |
|---|---|---|---|
| Chip to rack | Cold plates on each chip, or air for older racks | Rack density | Google's rack power design scaled from 10 to 100 kW and it expects more than 500 kW per rack before 2030 (30 April 2025) |
| Rack to room | A coolant distribution unit (CDU) and a facility water loop | The coolant temperature the chips accept | LBNL models AI liquid cooling at ASHRAE class W45, warm facility water (December 2024) |
| Room to plant | Chillers, which refrigerate, or none when outside air is cool enough | Climate and coolant temperature | LBNL: liquid's warmer water means fewer chiller hours (December 2024) |
| Plant to outside | Cooling tower (evaporates water) or dry cooler (does not) | Water risk at the site | Google air-cools sites where its framework finds the water source at high risk: Waltham Cross, Mesa and Canelones (2025 report) |

PUE, power usage effectiveness, is total power entering the building divided by power reaching the computers. WUE, water usage effectiveness, is litres of water per kilowatt-hour of IT energy; The Green Grid defined it in 2011. LBNL's 2024 report simulated both for each cooling design, across 965 US weather stations. These are its median results as I read them from its Figure 4.4, rounded.

| Cooling method (LBNL's name) | Hall size | PUE, about | Site WUE, litres per kWh, about |
|---|---|---|---|
| Direct expansion, room air conditioners | Small | 2.0 | 0 |
| Water-cooled chiller with cooling tower | Midsize | 1.5 | 2.9 |
| Air-cooled chiller | Midsize | 1.8 | 0 |
| Waterside economiser with cooling tower, air to the servers | Large | 1.1 | 2.2 |
| Airside economiser with adiabatic cooling, air-cooled chiller | Large | 1.2 | near 0 |
| Liquid cooling, waterside economiser with cooling tower | Large | 1.1 | 2.0 |
| Liquid cooling, dry cooler with adiabatic assist | Large | 1.1 | 0.15 |
| Liquid cooling, dry cooler | Large | 1.1 | 0 |

The pattern is the mechanism. In an air-cooled midsize hall, dropping the cooling tower for an air-cooled chiller costs about 0.3 of PUE. In a liquid-cooled hall, dropping it for a dry cooler costs almost nothing, while water falls from about 2 litres per kWh to zero.

LBNL adds two cautions. Its PUEs assume systems run as designed, which "is rarely the case". And hyperscalers report 0.1 to 0.3 litres per kWh for systems like its near-zero airside design, so real water use is higher than simulated.

What the operators report is the other half. Each names its measure differently, so the column says exactly what each source measures. Google and AWS report calendar years; Microsoft's year is most likely its fiscal year to June.

| Who | PUE | Water per kWh | What is measured | Year |
|---|---|---|---|---|
| Uptime Institute survey, all respondents | 1.54 | not given | Average of respondents' sites, as cited by Google | 2025 |
| LBNL, all US data centres | 1.4 | just over 0.36 L | Modelled, water consumed on site | 2023 |
| LBNL, hyperscale | 1.22 | 0.32 L | Modelled aggregate | 2023 |
| LBNL, AI specialised | 1.14 | 0.61 L | Modelled aggregate, mixed liquid and air | 2023 |
| Google, fleet | 1.09 | not given as WUE | Owned and operated campuses | 2025 |
| Amazon Web Services, global | 1.14 | 0.12 L | Water withdrawn per kWh of IT load | 2025 |
| Microsoft | not used here | 0.27 L | Water withdrawn per kWh, average WUE | 2025, likely its fiscal year to June |

One line in it cuts against easy optimism. LBNL's AI specialised halls had the best PUE and nearly twice the hyperscale water per kWh. It projects the national average WUE rising after 2023 to between 0.45 and 0.48 litres, partly from "the increased water consumption of liquid-cooled systems". Liquid at the chip makes going waterless cheap. It does not make it happen; the choice on the roof does.

<a id="cooling-is-half-the-job"></a>
## Why heat forced liquid to the chip

Google's engineers set the pace in public. Their rack power design scaled from 10 to 100 kilowatts, and they expect machine learning to need more than 500 kW per rack before 2030 (30 April 2025). Google first liquid-cooled its TPU v3 chips in 2018. It says it has since deployed liquid cooling "at GigaWatt scale across more than 2000 TPU Pods", with its pump units available about 99.999% of the time since 2020.

No primary source I found gives an industry-wide liquid cooling share. The closest is LBNL's model, which, as I read its Figure 4.2, puts roughly two thirds of AI specialised space on liquid in 2023. That is an estimate built from Dell'Oro sales data and expert input, not a census.

The industrial companies have bought in. Schneider Electric agreed to take control of Motivair, a liquid cooling specialist, on 17 October 2024. Eaton completed its purchase of Boyd Thermal on 12 March 2026. Both buy the same thing: the cold plates, pump units and pipework every liquid-cooled rack needs, whoever makes the chip.

PUE also tells the efficiency story. LBNL's simulations put small air-cooled rooms near 2.0 and large liquid-cooled halls near 1.1. Google's fleet ran at 1.09 in 2025, against the 1.54 average of Uptime's survey respondents. Singapore now [rations new capacity](/journal/the-queue-not-the-chip/#two-governments-one-confession) partly on a PUE of 1.25 or better.

The August piece said air fails "somewhere between 30 and 50 kilowatts per rack". I found no primary source for that band, so this page no longer uses it. What the sources do show is enough: air-cooled racks of 10 to 40 kW at Jane Street, against 140 kW for the rack replacing them.

<a id="room-to-spare"></a>
## Inside one hall: Jane Street's retrofit

Jane Street, a trading firm, showed its newest Texas AI site to the podcaster Dwarkesh Patel in a video tour published on 15 May 2026. Its write-up names the guides as Ron Minsky, who co-leads its technology group, and Dan Pontecorvo, who runs physical engineering. The site holds "4,032 GPUs across 56 racks, retrofitted for liquid cooling". Patel, quoted in the write-up, was struck by "the whole grid interconnect wattage of the datacenter taken up by racks that fit in a small fraction of the space originally allotted for chips".

On the tour, each GB300 NVL72 rack draws about 140 kilowatts at peak, against 10 to 40 kW for a traditional air-cooled cabinet. About 85 to 90% of each server's heat leaves through cold plates; air takes the rest.

Two of the tour's points matter here. Cooling proved the flexible part: oversized pipes let water be moved wherever it was needed. Power did not: every busway and breaker has a hard current limit, and the site runs on a fixed allocation from its utility.

So an existing hall could be retrofitted for liquid, and the cooling stopped being the limit. The fixed number was power. That second point belongs to how campuses arrive, and the stage-by-stage story is told in [power first, chips last](/journal/contracted-energised-running/#power-first-chips-last).

<a id="water-is-a-siting-problem"></a>
## Water: a choice made site by site

Engineers separate withdrawal, water taken in and mostly returned, from consumption, water lost for good, mostly as vapour. LBNL estimates American data centres consumed 66 billion litres on site in 2023. The power stations feeding them consumed "nearly 800 billion liters", about twelve times as much.

Google states the trade in its own words: water is "a highly efficient means of cooling that requires less energy than air-cooling technologies". Its rule since December 2023 is that where a source is high risk, "we will pursue alternative sources or cooling solutions". The big operators now make the choice in public.

| Site or fleet | What the operator did | Source, dated |
|---|---|---|
| Waltham Cross, Mesa, Canelones | Google's framework found the water sources at high risk of depletion and scarcity, so it chose air cooling at all three | Google 2025 Environmental Report, pp.40 to 41 |
| Mesa, Arizona | 9.7 million gallons consumed in 2025 | Google 2026 Environmental Report, per-site table |
| The Dalles, Oregon | Local water found not at high risk, so water cooling; 469 million gallons consumed in 2025, overhead of 6 to 10% in the fourth quarter | Google 2026 Environmental Report |
| Google, fleet | Share of freshwater withdrawal from sources at high risk: 15% in 2023, 14% in 2024, 13% in 2025 | Google Environmental Reports, 2024 to 2026 |
| Santiago, Chile | Google filed in February 2022 to replace water cooling towers with air-cooled chillers, ending its draw from three wells; a court still partly annulled the permit on 26 February 2024 | Chile's Second Environmental Court ruling |
| Microsoft, new designs | Since August 2024 all new designs evaporate no water for cooling, at "a nominal increase" in annual energy use; pilots in Phoenix and Mount Pleasant | Microsoft, 9 December 2024 |
| Microsoft, owned fleet | About 90% of its 2025 owned fleet uses "low- to zero-water cooling" | Microsoft, 24 June 2026 |

The rule has a visible edge. Henderson, Nevada, in a dry desert basin, consumed 239.4 million gallons in 2025, on Google's own table. Google does not publish how it rates that source, so I cannot say whether it breaks the rule. It shows that "dry region" and "high risk" in Google's framework are not the same thing.

None of this means data centre water is falling. Google's water consumption rose 34% in 2025, to 10.9 billion gallons, 41 billion litres, across data centres and offices. The claim is narrower: water steers how and where halls are cooled, and so far has not stopped a powered campus outright.

Johor is the Southeast Asian case. Its water margin is set by treatment plants, covered in [the plug, not the chip](/journal/the-queue-not-the-chip/#johor-waits-on-the-treatment-plant), and not repeated here.

## Claims on record

None of the merged pieces put a claim on record. Cooling-is-half-the-job (21 August 2026) and room-to-spare (25 September 2026) were Explainers, and the water draft never went live. So the claim below is this page's first.

<a id="heat-and-water"></a>

**New: Heat and water decide where AI goes** (30 October 2026)

Claim: "In AI data centres heat sets the cooling method and water sets where and how the heat leaves the building, not how many halls get built: every Google campus that Google itself names as at high water risk (Mesa, Waltham Cross and Canelones) will consume under 50 million gallons of water in each of 2026 and 2027, and no hyperscaler will report a new evaporatively cooled campus drawing on a water source it rates at high risk."

Breaks if: "Google reports consumption of 50 million gallons or more in 2026 or 2027 at Mesa, Waltham Cross or Canelones; or Google, Microsoft, Amazon or Meta reports opening a data centre cooled by evaporating water from a source it rates at high risk of depletion or scarcity; or a large AI campus with its power already secured is cancelled outright over water rather than redesigned to cool without it."

## What would prove me wrong

The first test is Google's own high-risk sites. Mesa consumed 9.7 million gallons in 2025, against 469 million at The Dalles, which is water cooled. If any of the three it named reaches 50 million gallons a year, Google is evaporating water where it said it would not.

The second is any hyperscaler disclosing a new evaporatively cooled campus on a source it rates high risk. That would mean water is being spent where it is scarcest, not traded away.

The third is a cancellation. A powered AI campus abandoned over water, rather than redesigned to cool without it, would mean water decides how many, not only where.

## Research notes

No initiation note rests on these claims yet. Liquid cooling equipment is part of the notes on [Vertiv](/research/vertiv/), [Schneider Electric](/research/schneider-electric/) and [Eaton](/research/eaton/), which rest on their own claims.

<section class="exposure">
<h3>Who is exposed if heat sets the cooling and water sets where it goes</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>Liquid to the chip</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span>, <span class="names">Eaton</span>, <span class="names">nVent</span> and <span class="names">CoolIT</span> make cold plates, pumps and loops.</dd>
<dt>Heat out of the building</dt>
<dd><span class="names">Trane</span>, <span class="names">Carrier</span>, <span class="names">Johnson Controls</span>, <span class="names">Modine</span> and <span class="names">Munters</span> make chillers and coolers. <span class="names">Ecolab</span> treats cooling water.</dd>
<dt>The halls that choose</dt>
<dd><span class="names">Microsoft</span>, <span class="names">Google</span>, <span class="names">Meta</span>, <span class="names">Amazon</span> and <span class="names">Jane Street</span> run data centres, filled with chips <span class="names">Nvidia</span> and <span class="names">AMD</span> design.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Campuses planned around cheap evaporative cooling in dry basins, and air-cooled halls that cannot take liquid without a refit.</dd>
</dl>
</section>

---

<p class="sources">Sources: Lawrence Berkeley National Laboratory, its report on United States data centre energy use (December 2024), Tables 4.2 and 4.3 and Figures 4.2, 4.4, 4.5 and 4.7; The Green Grid, WUE white paper (March 2011); Google's 2025 and 2026 Environmental Reports and its post on liquid cooling at the OCP EMEA Summit (30 April 2025); Amazon Web Services' sustainability page (2025 figures); Microsoft's posts of 9 December 2024 and 24 June 2026; Google's post on watershed health (15 December 2023); Chile's Second Environmental Court, ruling of 26 February 2024; Schneider Electric (17 October 2024) and Eaton (12 March 2026) releases; Jane Street's video tour with Dwarkesh Patel (15 May 2026) and its write-up of the site, with Ron Minsky and Dan Pontecorvo. Personal research, not investment advice.</p>
