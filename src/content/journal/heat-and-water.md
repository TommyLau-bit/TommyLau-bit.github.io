---
title: "Heat and water decide where AI goes: liquid to the chip, a choice on the roof"
date: 2026-08-21
summary: "AI data centres are blamed for drinking towns dry, yet a US government lab finds a liquid-cooled AI hall can stop evaporating water for almost no extra power. Heat has pushed cooling onto liquid at the chip, and that liquid runs warm enough to be cooled by fans alone. So water decides where and how each hall is cooled, not how many get built."
category: "Analysis"
cover: "/covers/heat-and-water.svg"
tags: ["cooling", "data-centres", "liquid", "water"]
draft: false
---

AI data centres are blamed for drinking towns dry. Yet a US government laboratory has found that a modern liquid-cooled AI hall can stop evaporating water altogether, and barely change how much electricity it uses.

The reason starts with heat. A chip does not use up electricity the way a car uses up petrol: almost every watt that goes in comes back out as heat. An AI rack now gives off so much that air can no longer carry it away, so the heat leaves through liquid instead.

That shift settles the argument. Heat decides how AI is cooled: with liquid, pressed against the chip. Water decides where and how that heat leaves the building, not how many halls get built.

Start with the heat. Jane Street's engineers say one cabinet of Nvidia's current flagship chips draws about 140 kilowatts at peak, roughly ninety hairdryers in a box the size of a fridge. An older air-cooled cabinet draws a fraction of that. Water carries thousands of times more heat per litre than air, so the industry now runs liquid through a metal plate on each chip. Google has cooled its own AI chips this way since 2018.

Then the heat has to leave the building, and that is where the water is decided. A cooling tower evaporates water, which is cheap in electricity. A dry cooler, a large radiator with fans, evaporates nothing but uses a little more power. It works whenever the outside air is cooler than the water inside it.

This is where liquid cooling changes the trade. Chips tolerate warm coolant, so the water leaving the hall is warm too, and for most of the year in many climates the outside air is cooler. Lawrence Berkeley National Laboratory simulated a large liquid-cooled hall both ways. With a cooling tower, it evaporated about 2 litres of water per kilowatt-hour of computing. With a dry cooler, almost none, and the hall's energy efficiency barely moved.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Ninety hairdryers in a shut wardrobe: no fan clears that, so you run cold water through pipes pressed against each one.</p>
<p>The pipes come out warm. Wrap them in a wet flannel on the balcony, which costs no electricity but dries the flannel, or put a fan on a radiator, which uses no water and a little more power.</p>
</details>

The same lab found that the power stations feeding American data centres consumed about twelve times the water the data centres did on site. Most of a data centre's water follows its electricity, not its roof.

The big operators now make the choice in public. Google air-cools its campuses where it judges the local water at high risk, and Microsoft says its new designs evaporate no water for cooling. Water has become a decision about each site, with its price in electricity, rather than a wall that stops AI being built.

<hr class="layer">
<p class="layer-label">For investors</p>

<a id="cooling-is-half-the-job"></a>

## A rack of AI chips now gives off more heat than air can carry

Rack power has outrun air, so the heat now leaves through liquid at the chip. Google's engineers say their rack power design scaled from 10 to 100 kilowatts, and they expect machine learning to need more than 500 kW per rack before 2030 (30 April 2025). On Jane Street's tour, a traditional air-cooled cabinet draws 10 to 40 kW, against about 140 kW for the GB300 NVL72 rack replacing it.

Google got there first. It liquid-cooled its TPU v3 chips in 2018 and says it has since deployed liquid cooling "at GigaWatt scale across more than 2000 TPU Pods", with its pump units available about 99.999% of the time since 2020.

No primary source I found gives an industry-wide liquid cooling share. The closest is the lab's model, which, as I read its Figure 4.2, puts roughly two thirds of AI specialised space on liquid in 2023, an estimate built from Dell'Oro sales data and expert input. The industrial companies have bought in anyway: Schneider Electric agreed to take control of Motivair on 17 October 2024, and Eaton completed its purchase of Boyd Thermal on 12 March 2026. Both bought the cold plates, pump units and pipework every liquid-cooled rack needs, whoever makes the chip.

## Liquid takes the heat off the chip, and the roof decides the water

Heat leaves an AI hall in a chain of steps, and only the first is new while only the last decides the water. A cold plate takes heat off each chip. A pump unit, a CDU, drives coolant round the rack and hands the heat to the building's water loop. The loop carries it to the roof.

<figure class="chart">
<p class="chart-title">Only the last step decides the water</p>
<p class="chart-sub">The path heat takes out of a liquid-cooled AI hall</p>
<svg viewBox="0 0 560 200" role="img" aria-label="Diagram. Heat passes from the chip, through a cold plate, to a pump unit that drives coolant round the rack, to the building's warm water loop. The loop then goes either to a cooling tower, which evaporates water, or to a dry cooler, which uses fans and no water. The liquid at the chip is the new part; the choice on the roof decides the water.">
<rect class="c-box" x="8" y="70" width="124" height="44" rx="4"/><text class="c-box-t" x="18" y="88">Chip</text><text class="c-note" x="18" y="105">cold plate on it</text>
<line class="c-arrow" x1="133" y1="92" x2="139" y2="92"/><polygon class="c-arrow-head" points="144,92 138,88 138,96"/>
<rect class="c-box" x="146" y="70" width="124" height="44" rx="4"/><text class="c-box-t" x="156" y="88">Pump unit</text><text class="c-note" x="156" y="105">drives coolant</text>
<line class="c-arrow" x1="271" y1="92" x2="277" y2="92"/><polygon class="c-arrow-head" points="282,92 276,88 276,96"/>
<rect class="c-box" x="284" y="70" width="124" height="44" rx="4"/><text class="c-box-t" x="294" y="88">Water loop</text><text class="c-note" x="294" y="105">runs warm</text>
<line class="c-arrow" x1="409" y1="92" x2="424.1" y2="47.7"/><polygon class="c-arrow-head" points="426,42 427.9,49 420.3,46.4"/>
<line class="c-arrow" x1="409" y1="92" x2="424.1" y2="136.3"/><polygon class="c-arrow-head" points="426,142 420.3,137.6 427.9,135"/>
<rect class="c-box" x="428" y="20" width="124" height="44" rx="4"/><text class="c-box-t" x="438" y="38">Cooling tower</text><text class="c-note" x="438" y="55">evaporates water</text>
<rect class="c-box" x="428" y="120" width="124" height="44" rx="4"/><text class="c-box-t" x="438" y="138">Dry cooler</text><text class="c-note" x="438" y="155">fans, no water</text>
<text class="c-lab c-s3t" x="8" y="146">New: liquid at the chip</text>
<text class="c-lab c-s2t" x="552" y="190" text-anchor="end">The choice on the roof decides the water</text>
</svg>
<figcaption>After the lab's report on United States data centre energy use (December 2024), Table 4.2, and Google's liquid cooling post (30 April 2025). Chillers, which refrigerate the loop on hot days, sit between the loop and the roof in many halls; warm liquid needs them for fewer hours.</figcaption>
</figure>

The warmth is the point. The lab models AI liquid cooling at ASHRAE class W45, warm facility water, and a dry cooler only needs the outside air to be cooler than that water. The warmer the loop, the more hours a year a hall can reject heat without evaporating anything.

Two measures keep score. PUE, power usage effectiveness, is total power entering the building divided by power reaching the computers. WUE, water usage effectiveness, is litres of water per kilowatt-hour of IT energy; The Green Grid defined it in 2011.

<a id="room-to-spare"></a>

## An existing hall can be refitted, so cooling is not the wall

Liquid cooling has proved the flexible part of an AI hall, which is why heat changes how halls are built, not whether. Jane Street showed its newest Texas AI site to the podcaster Dwarkesh Patel in a video tour published on 15 May 2026. The site holds "4,032 GPUs across 56 racks, retrofitted for liquid cooling".

On the tour, about 85 to 90% of each server's heat leaves through cold plates; air takes the rest. Oversized pipes let water be moved wherever it was needed. Patel, quoted in Jane Street's write-up, was struck by "the whole grid interconnect wattage of the datacenter taken up by racks that fit in a small fraction of the space originally allotted for chips".

Power was the fixed number. Every busway and breaker has a hard current limit, and the site runs on a fixed allocation from its utility. That half of the story is told in [power first, chips last](/journal/contracted-energised-running/#power-first-chips-last).

## Most of a data centre's water is spent at the power station

Before weighing the roof, it helps to see how small its share is. Engineers separate withdrawal, water taken in and mostly returned, from consumption, water lost for good, mostly as vapour. The lab estimates American data centres consumed 66 billion litres on site in 2023. The power stations feeding them consumed "nearly 800 billion liters".

<figure class="chart">
<p class="chart-title">Most of a data centre's water is used at the power station</p>
<p class="chart-sub">Water consumed for American data centres in 2023, in billions of litres</p>
<svg viewBox="0 0 560 130" role="img" aria-label="Bar chart. American data centres consumed 66 billion litres of water on site in 2023. The power stations generating their electricity consumed nearly 800 billion litres, about twelve times as much.">
<g class="c-axis"><text x="180" y="43" text-anchor="end">On site, cooling</text><text x="180" y="99" text-anchor="end">At the power stations</text></g>
<rect class="c-bar" x="190" y="24" width="16.5" height="30" rx="2"/>
<text class="c-lab c-s2t" x="216.5" y="44">66 billion litres</text>
<rect class="c-bar c-mute" x="190" y="80" width="200.0" height="30" rx="2"/>
<text class="c-lab c-s2t" x="400" y="100">nearly 800 billion</text>
<line class="c-base" x1="190" y1="14" x2="190" y2="120"/>
</svg>
<figcaption>Lawrence Berkeley National Laboratory, report on United States data centre energy use, December 2024. Both are modelled estimates of water consumed, not withdrawn. The power station figure is drawn at 800, its stated ceiling.</figcaption>
</figure>

That ratio, about twelve to one, frames everything on the roof. A hall that cuts its own evaporation to zero still carries most of its water footprint in the electricity it buys. For a town worried about its aquifer, the cooling choice still matters most, because that water is drawn locally.

## In a liquid-cooled hall, giving up water costs almost no power

The strongest evidence is the lab's simulation of every common cooling design across 965 American weather stations. It shows that liquid at the chip changes the price of going dry. In a midsize air-cooled hall, dropping the cooling tower costs real electricity. In a liquid-cooled hall, it costs almost none.

<figure class="chart">
<p class="chart-title">Liquid makes going without water almost free in power</p>
<p class="chart-sub">Simulated medians: PUE (power used per unit of computing) against water evaporated on site, litres per kWh</p>
<svg viewBox="0 0 560 300" role="img" aria-label="Scatter chart from Lawrence Berkeley National Laboratory's simulations. A midsize air-cooled hall with a water-cooled chiller and cooling tower has a PUE of about 1.5 and evaporates about 2.9 litres per kilowatt-hour; switching to an air-cooled chiller cuts water to zero but raises PUE to about 1.8. A large liquid-cooled hall with a cooling tower has a PUE of about 1.1 and evaporates about 2.0 litres per kilowatt-hour; switching to a dry cooler cuts water to zero with PUE still about 1.1.">
<g class="c-grid"><line x1="80" y1="250" x2="530" y2="250"/><line x1="80" y1="210" x2="530" y2="210"/><line x1="80" y1="170" x2="530" y2="170"/><line x1="80" y1="130" x2="530" y2="130"/><line x1="80" y1="90" x2="530" y2="90"/><line x1="80" y1="50" x2="530" y2="50"/></g>
<g class="c-axis">
<text x="70" y="254" text-anchor="end">1.0</text><text x="70" y="214" text-anchor="end">1.2</text><text x="70" y="174" text-anchor="end">1.4</text><text x="70" y="134" text-anchor="end">1.6</text><text x="70" y="94" text-anchor="end">1.8</text><text x="70" y="54" text-anchor="end">2.0</text>
<text x="80" y="270" text-anchor="middle">0</text><text x="230" y="270" text-anchor="middle">1</text><text x="380" y="270" text-anchor="middle">2</text><text x="530" y="270" text-anchor="middle">3</text>
</g>
<text class="c-note" x="80" y="36">PUE, lower is better</text>
<text class="c-note" x="530" y="292" text-anchor="end">Water evaporated on site, litres per kWh</text>
<line class="c-arrow" x1="507.1" y1="148.9" x2="94.9" y2="92"/><polygon class="c-arrow-head" points="87.9,91.1 95.4,88.1 94.3,96"/>
<line class="c-arrow" x1="372" y1="230" x2="95" y2="230"/><polygon class="c-arrow-head" points="88,230 95,226 95,234"/>
<circle class="c-dot c-s1" cx="515" cy="150" r="5"/><circle class="c-dot c-s1" cx="80" cy="90" r="5"/>
<circle class="c-dot c-s2" cx="380" cy="230" r="5"/><circle class="c-dot c-s2" cx="80" cy="230" r="5"/>
<text class="c-lab c-s1t" x="96" y="72">Air-cooled hall: PUE 1.5 rises to 1.8</text>
<text class="c-note" x="530" y="172" text-anchor="end">with a cooling tower</text>
<text class="c-lab c-s2t" x="96" y="216">Liquid-cooled hall: PUE about 1.1 either way</text>
<text class="c-note" x="380" y="246" text-anchor="middle">with a tower</text>
</svg>
<figcaption>Lawrence Berkeley National Laboratory, December 2024, Figure 4.4: medians as I read them from its chart, rounded. Air: midsize hall, water-cooled chiller with tower against air-cooled chiller. Liquid: large hall, waterside economiser with tower against dry cooler. Arrows show the tower being dropped.</figcaption>
</figure>

The pattern is the mechanism. In the air-cooled midsize hall, swapping the tower for an air-cooled chiller costs about 0.3 of PUE, because the chiller must then work against the outside air. In the liquid-cooled hall, swapping it for a dry cooler leaves PUE near 1.1, while water falls from about 2 litres per kWh to zero. A dry cooler with a little evaporation on hot days, the lab's adiabatic assist, lands at about 0.15. Large air-cooled halls that cool with outside air also get close, at about 1.2 with little water in the model, so the sharpest penalty is in midsize halls.

The lab adds two cautions. Its PUEs assume systems run as designed, which "is rarely the case". And hyperscalers report 0.1 to 0.3 litres per kWh for one design it simulates near zero, large air-cooled halls using outside air with occasional evaporation, so real water use can run higher than its model. The direction of the trade survives both.

<a id="water-is-a-siting-problem"></a>

## The operators now make the choice site by site

Once going dry is cheap, the operators choose it where water is scarce, and they say so. Google calls water "a highly efficient means of cooling that requires less energy than air-cooling technologies". Its rule since December 2023 is that where a source is high risk, "we will pursue alternative sources or cooling solutions".

It has applied the rule by name. Its 2025 report says its framework found the water sources at Waltham Cross, Mesa and Canelones at high risk of depletion and scarcity, so it chose air cooling at all three. Its own per-site table then shows what that choice is worth.

<figure class="chart">
<p class="chart-title">Where Google judged the water scarce, it used almost none</p>
<p class="chart-sub">Water consumed in 2025 at three Google campuses, millions of gallons</p>
<svg viewBox="0 0 560 196" role="img" aria-label="Bar chart. In 2025 Google's Mesa, Arizona campus, where it rated the water source high risk and chose air cooling, consumed 9.7 million gallons. Henderson, Nevada, whose rating Google does not publish, consumed 239.4 million gallons. The Dalles, Oregon, where the water was not high risk and the campus is water cooled, consumed 469 million gallons. The claim's line is 50 million gallons.">
<line class="c-today" x1="230.9" y1="28" x2="230.9" y2="182"/><text class="c-today-t" x="234" y="22">the claim's line, 50</text>
<g class="c-axis"><text x="190" y="52" text-anchor="end">Mesa, Arizona</text><text x="190" y="104" text-anchor="end">Henderson, Nevada</text><text x="190" y="156" text-anchor="end">The Dalles, Oregon</text></g>
<text class="c-note" x="190" y="67" text-anchor="end">high risk, air-cooled</text>
<text class="c-note" x="190" y="119" text-anchor="end">rating not published</text>
<text class="c-note" x="190" y="171" text-anchor="end">not high risk, water-cooled</text>
<rect class="c-bar" x="200" y="40" width="6.0" height="28" rx="2"/><text class="c-lab c-s1t" x="240" y="59">9.7</text>
<rect class="c-bar c-mute" x="200" y="92" width="148.0" height="28" rx="2"/><text class="c-lab c-s1t" x="358" y="111">239.4</text>
<rect class="c-bar c-alt" x="200" y="144" width="290.0" height="28" rx="2"/><text class="c-lab c-s1t" x="500" y="163">469</text>
<line class="c-base" x1="200" y1="32" x2="200" y2="182"/>
</svg>
<figcaption>Google 2026 Environmental Report, per-site table, 2025 consumption; risk ratings from its 2025 report, pp.40 to 41, and its watershed post of 15 December 2023. Waltham Cross and Canelones have no row yet.</figcaption>
</figure>

Mesa used about one fiftieth of the water The Dalles did. That gap is the choice on the roof, made by the operator in its own report, and it is why the claim below sets its line at 50 million gallons: crossing it would point to evaporative cooling, not humidification.

Microsoft has gone further by design. Since August 2024 all its new designs evaporate no water for cooling, at "a nominal increase" in annual energy use, and it says about 90% of its 2025 owned fleet uses "low- to zero-water cooling". Google's share of freshwater withdrawal from high-risk sources has edged down from 15% in 2023 to 13% in 2025. In Santiago, Google filed in 2022 to replace water cooling towers with air-cooled chillers, though a court still partly annulled the permit in 2024.

## What could make water a limit on how many

The case against is real, and it starts with the lab's own numbers. Its AI specialised halls in 2023 had the best PUE, 1.14, and nearly twice the hyperscale water per kWh, 0.61 litres against 0.32. It projects the national average rising from just over 0.36 litres to between 0.45 and 0.48, partly from "the increased water consumption of liquid-cooled systems".

The totals are rising too. Google's water consumption rose 34% in 2025, to 10.9 billion gallons, across data centres and offices. Henderson, in a dry desert basin, consumed 239.4 million gallons, and Google does not publish how it rates that source, so "dry region" and "high risk" in its framework are not the same thing.

That is a limit I concede. Liquid at the chip makes going without water cheap; it does not make it happen, and many halls still evaporate where water is plentiful. But I have found no powered campus stopped outright by it. Where water is short, the operators so far redesign the roof rather than abandon the site. Johor's water margin, set by treatment plants, is covered in [the plug, not the chip](/journal/the-queue-not-the-chip/#johor-waits-on-the-treatment-plant).

So the ninety hairdryers stay in the wardrobe, and the pipes still come out warm. Whether they meet a wet flannel or a fan is now a choice each site makes, paid for in a little electricity. Heat chose the liquid; water only chooses the roof.

## Claims on record

None of the merged pieces put a claim on record. "Electricity doesn't get used up making AI. It turns into heat. Cooling is half the job." (21 August 2026) and "Jane Street's AI data hall has room to spare, and no power to fill it" (25 September 2026) were Explainers. So the claim below is this page's first, quoted word for word from the claims page:

<a id="heat-and-water"></a>

**Heat and water decide where AI goes** (30 October 2026)

Claim: "In AI data centres heat sets the cooling method and water sets where and how the heat leaves the building, not how many halls get built: every Google campus that Google itself names as at high water risk (Mesa, Waltham Cross and Canelones) will consume under 50 million gallons of water in each of 2026 and 2027, and no hyperscaler will report a new evaporatively cooled campus drawing on a water source it rates at high risk."

Breaks if: "Google reports consumption of 50 million gallons or more in 2026 or 2027 at Mesa, Waltham Cross or Canelones; or Google, Microsoft, Amazon or Meta reports opening a data centre cooled by evaporating water from a source it rates at high risk of depletion or scarcity; or a large AI campus with its power already secured is cancelled outright over water rather than redesigned to cool without it."

## What would prove me wrong

The first test is Google's own high-risk sites. Mesa consumed 9.7 million gallons in 2025, against 469 million at The Dalles. If any of the three it named reaches 50 million gallons a year, Google is evaporating water where it said it would not.

The second is any hyperscaler disclosing a new evaporatively cooled campus on a source it rates high risk. That would mean water is being spent where it is scarcest, not traded away.

The third is a cancellation. A powered AI campus abandoned over water, rather than redesigned to cool without it, would mean water decides how many, not only where.

## Research notes

No initiation note rests on this claim yet. Liquid cooling equipment is part of the notes on [Vertiv](/research/vertiv/), [Schneider Electric](/research/schneider-electric/) and [Eaton](/research/eaton/), which rest on their own claims.

<details class="evidence">
<summary>The figures behind the charts</summary>

Heat leaves an AI hall in a chain of four steps:

| Step | What carries the heat | What decides it | Evidence, dated |
|---|---|---|---|
| Chip to rack | Cold plates on each chip, or air for older racks | Rack density | Google's rack power design scaled from 10 to 100 kW and it expects more than 500 kW per rack before 2030 (30 April 2025) |
| Rack to room | A coolant distribution unit (CDU) and a facility water loop | The coolant temperature the chips accept | LBNL models AI liquid cooling at ASHRAE class W45, warm facility water (December 2024) |
| Room to plant | Chillers, which refrigerate, or none when outside air is cool enough | Climate and coolant temperature | LBNL: liquid's warmer water means fewer chiller hours (December 2024) |
| Plant to outside | Cooling tower (evaporates water) or dry cooler (does not) | Water risk at the site | Google air-cools sites where its framework finds the water source at high risk: Waltham Cross, Mesa and Canelones (2025 report) |

LBNL's simulated medians by cooling design, across 965 US weather stations, as I read them from its Figure 4.4, rounded:

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

What the operators report. Each names its measure differently, so the column says exactly what each source measures. Google and AWS report calendar years; Microsoft's year is most likely its fiscal year to June.

| Who | PUE | Water per kWh | What is measured | Year |
|---|---|---|---|---|
| Uptime Institute survey, all respondents | 1.54 | not given | Average of respondents' sites, as cited by Google | 2025 |
| LBNL, all US data centres | 1.4 | just over 0.36 L | Modelled, water consumed on site | 2023 |
| LBNL, hyperscale | 1.22 | 0.32 L | Modelled aggregate | 2023 |
| LBNL, AI specialised | 1.14 | 0.61 L | Modelled aggregate, mixed liquid and air | 2023 |
| Google, fleet | 1.09 | not given as WUE | Owned and operated campuses | 2025 |
| Amazon Web Services, global | 1.14 | 0.12 L | Water withdrawn per kWh of IT load | 2025 |
| Microsoft | not used here | 0.27 L | Water withdrawn per kWh, average WUE | 2025, likely its fiscal year to June |

Singapore now [rations new capacity](/journal/the-queue-not-the-chip/#two-governments-one-confession) partly on a PUE of 1.25 or better.

The siting record:

| Site or fleet | What the operator did | Source, dated |
|---|---|---|
| Waltham Cross, Mesa, Canelones | Google's framework found the water sources at high risk of depletion and scarcity, so it chose air cooling at all three | Google 2025 Environmental Report, pp.40 to 41 |
| Mesa, Arizona | 9.7 million gallons consumed in 2025 | Google 2026 Environmental Report, per-site table |
| Henderson, Nevada | 239.4 million gallons consumed in 2025; Google does not publish its rating of the source | Google 2026 Environmental Report, per-site table |
| The Dalles, Oregon | Local water found not at high risk, so water cooling; 469 million gallons consumed in 2025 | Google 2026 Environmental Report |
| Google, fleet | Share of freshwater withdrawal from sources at high risk: 15% in 2023, 14% in 2024, 13% in 2025; water consumption up 34% in 2025 to 10.9 billion gallons, 41 billion litres, data centres and offices | Google Environmental Reports, 2024 to 2026 |
| Santiago, Chile | Google filed in February 2022 to replace water cooling towers with air-cooled chillers, ending its draw from three wells; a court still partly annulled the permit on 26 February 2024 | Chile's Second Environmental Court ruling |
| Microsoft, new designs | Since August 2024 all new designs evaporate no water for cooling, at "a nominal increase" in annual energy use; pilots in Phoenix and Mount Pleasant | Microsoft, 9 December 2024 |
| Microsoft, owned fleet | About 90% of its 2025 owned fleet uses "low- to zero-water cooling" | Microsoft, 24 June 2026 |

Jane Street: this page cites the video tour (15 May 2026) and Jane Street's write-up of the site, which names the guides as Ron Minsky, who co-leads its technology group, and Dan Pontecorvo, who runs physical engineering; not the longer conversation the three released on 21 May.

Correction to the August piece: it said air fails "somewhere between 30 and 50 kilowatts per rack". I found no primary source for that band, so this page no longer uses it. What the sources show is enough: air-cooled racks of 10 to 40 kW at Jane Street, against 140 kW for the rack replacing them.

</details>

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
