---
title: "Heat and water decide where AI goes: liquid to the chip, a choice on the roof"
date: 2026-08-21
summary: "AI data centres are blamed for drinking towns dry, yet a US government lab finds a liquid-cooled AI hall can stop evaporating water for almost no extra power. Heat has pushed cooling onto liquid at the chip, and that liquid runs warm enough to be cooled by fans alone. So water decides where and how each hall is cooled, not how many get built."
category: "Analysis"
cover: "/covers/heat-and-water.svg"
tags: ["cooling", "data-centres", "liquid", "water"]
updated: 2026-11-06
updateNote: "Now follows one watt of heat from the chip to the roof and asks what going dry costs on the hottest afternoon, with evidence to 6 November 2026."
draft: false
---


AI data centres are blamed for drinking towns dry. Yet a US government laboratory has found that a modern liquid-cooled AI hall can stop evaporating water altogether, and barely change how much electricity it uses.

Heat decides how AI is cooled: with liquid, pressed against the chip. Water decides where and how that heat leaves the building, not how many halls get built. Liquid makes going without water cheap. It does not make it happen.

"Cooling" is really three jobs. At the chip, heat must be pulled off a hot surface, and for AI only liquid can now do it. Across the building, pumps and pipes carry that heat to the roof. Out of the building, it is released to the air. The first job is settled, and only the third can spend water.

<details class="analogy">
<summary>The analogy</summary>
<p>Think of cooling down after a run. Sweat cools you by evaporating and works even on a hot day, but you must drink to replace it: that is the cooling tower. A fan on dry skin costs a little electricity and no water, but helps only while the air is cooler than you: that is the dry cooler.</p>
<p>On a sweltering afternoon the air is as warm as your skin, and the fan barely helps. Now picture skin at 45 degrees. The fan would win almost every day, and sweat would be for the worst afternoons. Liquid at the chip gives the building that hot skin.</p>
</details>

The argument runs in five steps. First, almost every watt that goes into a chip comes back out as heat. One Blackwell-generation Nvidia rack sheds about 140 kilowatts, roughly ninety hairdryers in a box the size of a fridge, and air cannot carry that away. Second, the heat therefore moves to liquid at the chip, through a cold plate, a metal block with coolant inside. Third, chips tolerate warm coolant, so the building's water can run warm: Nvidia's newest rack takes it at up to 45 degrees. Fourth, water that warm can be cooled by outside air alone for most hours, so a cooling tower, which evaporates water, can give way to a dry cooler, a large radiator with fans. Fifth, water stops being a wall and becomes a choice about each roof.

Inside the hall, one watt takes that route through sealed loops: from the cold plate into the rack's coolant, across a pump unit to the building's water, up to the roof, and out.

<figure class="chart">
<p class="chart-title">Only the last step can spend water, and it is a choice</p>
<p class="chart-sub">One watt of heat, from an AI chip to the outside air</p>
<svg viewBox="0 0 560 196" role="img" aria-label="Diagram of five steps in order. One, chip: a cold plate on each chip takes the heat; a Blackwell-generation rack sheds about 140 kilowatts. Two, rack loop: sealed coolant, which Nvidia's Rubin rack takes in at up to 45 degrees Celsius and returns at about 55. Three, pump unit: pumps and a heat exchanger hand the heat to the building's water. Four, building: a warm water loop carries it to the roof, with a chiller on hot days. Five, roof: a cooling tower evaporates about 2 litres per kilowatt-hour in a large liquid-cooled hall, a dry cooler none. This is the choke point: only the roof touches outside air.">
<rect class="c-box" x="5.0" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="13.0" y="66">1. Chip</text>
<text class="c-note" x="13.0" y="88">Cold plate on</text>
<text class="c-note" x="13.0" y="106">each chip</text>
<text class="c-note" x="13.0" y="124">About 140 kW</text>
<text class="c-note" x="13.0" y="142">a rack</text>
<line class="c-arrow" x1="106.4" y1="97" x2="111.4" y2="97"/><polygon class="c-arrow-head" points="116.4,97 110.4,93 110.4,101"/>
<rect class="c-box" x="117.4" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="125.4" y="66">2. Rack loop</text>
<text class="c-note" x="125.4" y="88">Sealed</text>
<text class="c-note" x="125.4" y="106">coolant: up to</text>
<text class="c-note" x="125.4" y="124">45°C in, about</text>
<text class="c-note" x="125.4" y="142">55°C out</text>
<line class="c-arrow" x1="218.8" y1="97" x2="223.8" y2="97"/><polygon class="c-arrow-head" points="228.8,97 222.8,93 222.8,101"/>
<rect class="c-box" x="229.8" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="237.8" y="66">3. Pump unit</text>
<text class="c-note" x="237.8" y="88">Pumps and a</text>
<text class="c-note" x="237.8" y="106">heat exchanger</text>
<text class="c-note" x="237.8" y="124">hand heat to</text>
<text class="c-note" x="237.8" y="142">the building</text>
<line class="c-arrow" x1="331.2" y1="97" x2="336.2" y2="97"/><polygon class="c-arrow-head" points="341.2,97 335.2,93 335.2,101"/>
<rect class="c-box" x="342.2" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="350.2" y="66">4. Building</text>
<text class="c-note" x="350.2" y="88">Warm water</text>
<text class="c-note" x="350.2" y="106">loop to the</text>
<text class="c-note" x="350.2" y="124">roof; chiller</text>
<text class="c-note" x="350.2" y="142">on hot days</text>
<line class="c-arrow" x1="443.6" y1="97" x2="448.6" y2="97"/><polygon class="c-arrow-head" points="453.6,97 447.6,93 447.6,101"/>
<rect class="c-zone" x="450.6" y="14" width="108.4" height="144" rx="4"/>
<text class="c-zone-t" x="504.8" y="30" text-anchor="middle">THE CHOKE POINT</text>
<rect class="c-box" x="454.6" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="462.6" y="66">5. Roof</text>
<text class="c-note" x="462.6" y="88">Tower: about</text>
<text class="c-note" x="462.6" y="106">2 L per kWh</text>
<text class="c-note" x="462.6" y="124">Dry cooler:</text>
<text class="c-note" x="462.6" y="142">no water</text>
<text class="c-lab c-s2t" x="555.0" y="180" text-anchor="end">Only the roof touches outside air, so only it spends water</text>
</svg>
<figcaption>Jane Street's site tour (15 May 2026); Nvidia (21 June 2026); Lawrence Berkeley National Laboratory (December 2024), simulated medians. My framing of the chain.</figcaption>
</figure>

The fifth step binds because it alone touches the outside air; the four before it lose almost no water. A tower keeps one edge. Evaporation can cool water below the temperature of the air, and a dry cooler never can. Warm coolant leaves that edge mattering only on the hottest days.

Lawrence Berkeley National Laboratory simulated a large liquid-cooled hall both ways. With a tower it evaporated about 2 litres of water per kilowatt-hour of computing. With a dry cooler it used almost none, and the hall's energy efficiency barely moved.

So heat has settled the inside of the hall. Water decides only the roof, and there it is traded for a little electricity, not for whether the hall gets built.

<hr class="layer">
<p class="layer-label">For investors</p>

## Water is a roof decision for AI halls, not a wall

<a id="heat-and-water"></a>

Going dry costs a liquid AI hall almost nothing in power. Lawrence Berkeley National Laboratory, a US government lab, simulated every common cooling design across 965 American weather stations. A large liquid hall with a cooling tower, which evaporates water to shed heat, uses about 2 litres per kWh; with a dry cooler, a radiator with fans, water falls to zero, and its PUE, total power entering the building over power reaching the computers, stays near 1.1. In a midsize air-cooled hall, dropping the tower costs about 0.3 of PUE.

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

That gap matters to a fund in three ways. If the fix is cheap, the real risk in the headline that AI drinks towns dry is consent and siting, not the number of halls. The equipment mix moves: liquid loops at the chip are now needed in every AI rack, while on the roof orders shift between towers, dry coolers and chillers. And a site with power but little water is more usable than it looks.

## Six physical limits keep going dry from being free everywhere

**The air-temperature floor.** A dry cooler can bring water only to a few degrees above the air. A tower can go below it, towards the temperature a thermometer in a wet cloth reads.

**The worst afternoon.** Plant is sized for the hottest hours, not the average, and those are the hours a dry cooler is weakest.

**Small gaps need big radiators.** The heat a coil moves scales with its area and the temperature gap across it, so the closer the air is to the water, the more coil, fan, roof and land each megawatt needs.

**Fans cost power on peak.** A dry roof spends a little more electricity, most of it on hot afternoons, when the grid is tightest.

**The chip sets the ceiling.** Only chips that accept warm coolant unlock the dry roof, and part of every server still runs on air. At the AI hall of Jane Street, a trading firm, cold plates take 85 to 90% of each server's heat and fans the rest.

<a id="room-to-spare"></a>

**Old halls are locked in.** A hall built for cold air and towers needs pipes, pump units and new roof plant. Jane Street's newest Texas site, shown in a video tour on 15 May 2026, holds "4,032 GPUs across 56 racks, retrofitted for liquid cooling": a refit, not a switch. The site runs on a fixed allocation from its utility, as told in [power first, chips last](/journal/contracted-energised-running/#power-first-chips-last).

## The headlines count the roof, and most of the water is at the power station

Water headlines count the roof because the roof is local and visible. The lab estimates American data centres consumed 66 billion litres on site in 2023, while the power stations feeding them consumed "nearly 800 billion liters", about twelve to one. Both count water lost for good, mostly as vapour, not water taken in and returned.

Most of a data centre's water therefore follows its electricity, and PUE is also a water number. A dry roof that wastes power spends the water again, at a plant somewhere else and in someone else's report.

## Four terms carry the argument

**PUE.** Power usage effectiveness: total power into the building divided by power reaching the computers. At 1.1 the overhead for cooling and losses is a tenth, like a bill over the price of the food, where the gap is service. It is an annual average and says nothing about the worst hour.

**WUE, consumed and withdrawn.** Water usage effectiveness, litres per kWh of computing. Consumed water evaporates and is gone, like a drink; withdrawn water is taken and mostly returned, like a borrowed glass poured back. The lab counts consumed water. Amazon Web Services, Amazon's cloud arm, and Microsoft report withdrawn water, so Amazon's 0.12 litres and the lab's 2.0 do not measure the same thing.

**Tower, dry cooler and chiller.** Sweat, fan and fridge. The tower evaporates water and is cheap in power; the dry cooler uses fans and no water; the chiller refrigerates the loop, costs the most power and is kept for hot hours. Between them sits adiabatic assist, a dry cooler that sprays a little water on hot days, at about 0.15 litres in the lab's model.

**CDU and W45.** The coolant distribution unit is pumps plus a heat exchanger between the rack's sealed loop and the building's water, the pass between kitchen and dining room. W45 is the class set by ASHRAE, the American cooling engineers' body, for facility water up to about 45 degrees, and the lab models AI liquid cooling at it.

## Counted whole, a dry liquid hall uses about half the water

A hall's whole water bill is its roof figure plus its PUE times the lab's national average of 4.52 litres consumed at the power station per kWh bought, since each kWh of computing buys PUE kWh from the grid. The sum is mine, built only from the lab's numbers.

<figure class="chart">
<p class="chart-title">Counted whole, a large dry liquid hall uses about half the water of a midsize air hall with a tower</p>
<p class="chart-sub">Water consumed per kWh of computing, in litres: at the power station for the electricity bought, plus on the roof</p>
<svg viewBox="0 0 560 212" role="img" aria-label="Stacked bar chart, my arithmetic from Lawrence Berkeley National Laboratory's figures. Midsize air-cooled hall with a cooling tower: about 6.8 litres at the power station plus 2.9 on the roof, about 9.7 in all. Air-cooled chiller with no water on site: about 8.1, all at the power station. Large liquid-cooled hall with a cooling tower: about 5.0 at the power station plus 2.0 on the roof, about 7.0. Liquid-cooled hall with a dry cooler: about 5.0, all at the power station.">
<g class="c-axis">
<text x="180" y="52" text-anchor="end">Air, cooling tower</text>
<text x="180" y="98" text-anchor="end">Air, chiller, no water</text>
<text x="180" y="144" text-anchor="end">Liquid, cooling tower</text>
<text x="180" y="190" text-anchor="end">Liquid, dry cooler</text>
</g>
<rect class="c-bar c-mute" x="190" y="34" width="183.1" height="26" rx="2"/>
<rect class="c-bar c-alt" x="373.1" y="34" width="78.3" height="26" rx="2"/>
<text class="c-lab c-s1t" x="459.4" y="52">about 9.7 L</text>
<rect class="c-bar c-mute" x="190" y="80" width="219.7" height="26" rx="2"/>
<text class="c-lab c-s1t" x="417.7" y="98">about 8.1 L</text>
<rect class="c-bar c-mute" x="190" y="126" width="134.2" height="26" rx="2"/>
<rect class="c-bar c-alt" x="324.2" y="126" width="54.0" height="26" rx="2"/>
<text class="c-lab c-s1t" x="386.2" y="144">about 7.0 L</text>
<rect class="c-bar c-mute" x="190" y="172" width="134.2" height="26" rx="2"/>
<text class="c-lab c-s1t" x="332.2" y="190">about 5.0 L</text>
<text class="c-note" x="281.5" y="26" text-anchor="middle">at the power station</text><text class="c-note" x="412.2" y="26" text-anchor="middle">on the roof</text>
<line class="c-base" x1="190" y1="30" x2="190" y2="202"/>
</svg>
<figcaption>My arithmetic from Lawrence Berkeley National Laboratory, December 2024. Roof water and PUE are its simulated medians as I read them from Figure 4.4, rounded (air: midsize hall; liquid: large hall); the power station share is PUE times its national average of 4.52 litres per kWh a data centre buys. A hall on a different power mix would differ.</figcaption>
</figure>

At the lab's medians, a midsize air hall with a tower uses about 9.7 litres per kWh in all, and a large liquid hall with a dry cooler about 5.0. In the air hall, dropping the tower saves about 2.9 litres on the roof, but its PUE rises about 0.3, which spends about 1.4 litres again at the power station. In the liquid hall the roof saving of about 2 litres is kept whole, because PUE does not move. Under a fixed grid allowance the dry liquid hall also runs over 60% more computing from the same plug, at a PUE of about 1.1 against 1.8.

The sum carries four traps. It compares a midsize air hall with a large liquid one, and the medians are my rounded readings of the lab's chart. The 4.52 is a national grid average: on wind and solar it falls towards zero and the roof matters more, while on thermal plant with wet towers it is higher. And the lab warns that its PUEs assume systems run as designed, which "is rarely the case", while hyperscalers, the largest cloud operators, report 0.1 to 0.3 litres per kWh for one design it simulates near zero. The direction of the trade survives all four.

## The value sits in the liquid loop, the roof mix and the dry site with power

If water sets the roof and not the count, three positions in the chain gain.

**The liquid loop.** Cold plates, pump units and pipework go into every AI rack, whatever the chip and whatever the roof, and power gear makers have bought in. Schneider Electric, the French power equipment maker, agreed to take control of Motivair, a liquid cooling maker, on 17 October 2024, and Eaton, the power management group, completed its purchase of Boyd Thermal, another, on 12 March 2026.

**The roof mix.** On the roof the mix shifts from towers and chiller hours towards dry coolers and adiabatic assist. Chillers shrink as a share of each megawatt but stay, because plant is sized on the worst hour, not the average. Treating cooling water is a tower business, so fewer towers mean less of it per megawatt.

<a id="water-is-a-siting-problem"></a>

**The dry site with power.** If a liquid hall can go dry cheaply, a site with a grid allocation and scarce water is usable after all, and operators already act on it. Google, the search and cloud company, found the water sources at Waltham Cross, Mesa and Canelones, its campuses in England, Arizona and Uruguay, at high risk in its 2025 report, and chose air cooling at all three. Microsoft, another of the largest cloud operators, has gone further: since August 2024 all its new designs evaporate no water for cooling, at "a nominal increase" in annual energy use.

## What would prove me wrong

Three things would break the claim, and each tests what operators and towns do, not physics.

The first is Google's own sites: any of Mesa, Waltham Cross or Canelones reaching 50 million gallons in 2026 or 2027. Mesa consumed 9.7 million in 2025, about one fiftieth of The Dalles, Google's water-cooled Oregon campus, so crossing the line would point to evaporative cooling, not humidification of the air.

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

The second is a wet campus on scarce water: Google, Microsoft, Amazon or Meta opening a campus that evaporates water from a source it rates high risk, which would mean the dry roof is not chosen even where it should be. The third is a powered AI campus cancelled outright over water rather than redesigned, which would mean water decides how many halls, not only where.

Two things would move me first: Mesa climbing towards the line in Google's yearly per-site table, or Waltham Cross or Canelones, which have no row yet, entering near it; and a water utility refusing service to a campus whose grid power is already secured.

<a id="cooling-is-half-the-job"></a>

The claim stands on two legs. The first, that heat forces liquid to the chip, is physics, and no test attacks it. Google's engineers say their rack power design scaled from 10 to 100 kilowatts, and they expect machine learning to need more than 500 kW per rack before 2030 (30 April 2025). An air-cooled cabinet draws 10 to 40 kW, against about 140 kW for the GB300 NVL72, a Blackwell-generation rack from Nvidia, the leading AI chip designer. The second leg, that water sets the roof, is economics and consent. The first two tests attack operators' choices and the third attacks "not how many". Any of the three breaks the dated claim, but only the third would overturn the idea.

If the objection is that water will cap AI building, my answer is that water stops projects through consent, not physics. The engineering fix exists and is cheap in a liquid hall, so where a project dies, the first question is whether its power was secured. In Santiago, Chile, Google filed in 2022 to replace water cooling towers with air-cooled chillers, though a court still partly annulled the permit in 2024: a redesign, not an abandoned site.

Rising water totals would not move me either. The lab projects the national average rising from just over 0.36 litres per kWh to between 0.45 and 0.48, partly from "the increased water consumption of liquid-cooled systems". Google's water consumption rose 34% in 2025, and Henderson, its Nevada campus in a dry desert basin, consumed 239.4 million gallons, with no published rating of its source. More evaporation where water is plentiful is the trade working, and Google's share of freshwater withdrawal from high-risk sources has edged down from 15% in 2023 to 13% in 2025.

## Nvidia's warmer coolant shrinks the chiller without removing it

Nvidia has written the third step of the chain into its own specification. Vera Rubin, its next rack, takes coolant at up to 45°C and returns it at about 55°C (21 June 2026), and on 26 August 2026 Nvidia said it was ramping into full production with racks running at partners. Nvidia says dry coolers can then reject the heat for much of the year, with chillers, which refrigerate the loop, needed "maybe 1% of the year" in some climates.

I concede that chiller hours per megawatt fall, and that in mild climates some new halls may run without a chiller at all. But 1% of a year is about 88 hours, and they are the hottest ones, so the plant for them still has to exist. Nvidia's own engineers write that heat rejection is still "sized for worst-case scenarios" (24 August 2026). Heat waves, hot climates and the heat still carried by air keep mechanical cooling in the design, and the vendor's figures are claims, not measurements. Chillers shrink as a share of each megawatt while the megawatts keep rising.

<a id="towns-say-no"></a>
## Towns are saying no to water, even for halls that use almost none

This development partly cuts against me. In Ypsilanti, Michigan, the utility authority serving the city and township voted on 22 April 2026 to halt, for at least 12 months, any commitment of water or sewer service to data centres while it studies supply and wastewater capacity. Pinal County, Arizona, voted 4-1 on 26 August 2026 to refuse rezoning for Vermaland's campus near Eloy despite a closed-loop cooling pledge, and supervisors cited water, public opposition and no identified end user, local press reported. Heatmap, a climate news site, counted at least 20 proposed projects cancelled after local pushback in the first quarter of 2026, reasons not broken down.

I concede that water is now a permit-stage risk, and that a closed-loop promise no longer buys consent, a cost the engineering chain leaves out. But the claim's test is a campus with power already secured, cancelled over water. Pinal's developer still planned its own gas plant and had no end user, and Ypsilanti is a pause, not a cancellation. So far water kills weak projects and moves strong ones, and I count consent as a cost of a site, not a cap on the industry.

<a id="the-worst-afternoon"></a>
## Going dry may be paid for in peak megawatts, not annual kilowatt-hours

My working hypothesis is that a dry roof is paid for on the hottest afternoon, since a grid connection and a water main are both built for the peak, not the annual average. Researchers at the University of California, Riverside estimate that evaporative cooling's water demand on the peak day can run six to ten times its average, and that utilities must size plants, pumps and pipes for it (12 March 2026). Nvidia's engineers add that power budgeted for cooling in the worst hour is free for computing much of the year (24 August 2026).

The inference is mine. A grid allocation caps a building's maximum draw, so the computing it allows is set by the worst hour's PUE, not the year's. A dry roof's PUE worsens most in those hours, while a tower holds it down and spends its most water just as the town's mains peak. Under a fixed plug, like Jane Street's, a little water for the hottest 88 hours may buy back peak megawatts. The Riverside authors already propose switching to water cooling when the grid is stressed and to dry when the water system is; the link to a fixed plug is mine.

The test is design-day PUE against annual PUE for dry-cooled liquid halls, in permit files and utility filings. If 45°C coolant keeps the worst hour within a few points of the year's average, the effect is small and the idea dies. It also dies if operators book plugs with so much headroom that the worst hour never binds.

## The chip sets the temperature, the roof makes the choice, and the town and grid pay at the peak

The chip maker sets how warm the coolant may be, and each degree adds hours in which outside air alone takes the heat. The roof trades water for power or power for water. The town and the grid pay, with most of the water spent at the power station and both mains and connection sized for the same hot afternoon.

The scales meet where it is always warm. Singapore and Johor, the Malaysian data centre hub beside it, have no cold season, so fewer hours are free, and humid air blunts a tower's edge too; warm coolant matters most there. Johor's water margin is set by its treatment plants, covered in [the plug, not the chip](/journal/the-queue-not-the-chip/#johor-waits-on-the-treatment-plant).

<details class="claims-record">
<summary>The claims on record, word for word</summary>

The test this piece stands behind, quoted word for word:

**Heat and water decide where AI goes** (30 October 2026)

Claim: "In AI data centres heat sets the cooling method and water sets where and how the heat leaves the building, not how many halls get built: every Google campus that Google itself names as at high water risk (Mesa, Waltham Cross and Canelones) will consume under 50 million gallons of water in each of 2026 and 2027, and no hyperscaler will report a new evaporatively cooled campus drawing on a water source it rates at high risk."

Breaks if: "Google reports consumption of 50 million gallons or more in 2026 or 2027 at Mesa, Waltham Cross or Canelones; or Google, Microsoft, Amazon or Meta reports opening a data centre cooled by evaporating water from a source it rates at high risk of depletion or scarcity; or a large AI campus with its power already secured is cancelled outright over water rather than redesigned to cool without it."

Earlier pieces on this subject made no claim. "Electricity doesn't get used up making AI. It turns into heat. Cooling is half the job." (21 August 2026) and "Jane Street's AI data hall has room to spare, and no power to fill it" (25 September 2026) were Explainers, so the claim above is this page's first.

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

Heat leaves an AI hall in a chain of four steps:

| Step | What carries the heat | What decides it | Evidence, dated |
|---|---|---|---|
| Chip to rack | Cold plates on each chip, or air for older racks | Rack density | Google's rack power design scaled from 10 to 100 kW and it expects more than 500 kW per rack before 2030 (30 April 2025) |
| Rack to room | A coolant distribution unit (CDU) and a facility water loop | The coolant temperature the chips accept | LBNL models AI liquid cooling at ASHRAE class W45, warm facility water (December 2024) |
| Room to plant | Chillers, which refrigerate, or none when outside air is cool enough | Climate and coolant temperature | LBNL: liquid's warmer water means fewer chiller hours (December 2024); Nvidia's Rubin rack takes coolant at up to 45°C and returns about 55°C, with chillers "maybe 1% of the year" in some climates (21 June 2026), and heat rejection is "sized for worst-case scenarios" (24 August 2026) |
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

The water counted from the power station to the roof, in the stacked bar chart, is my arithmetic. The lab puts water consumed at the power station at a "national average of 4.52 L/kWh of indirect water consumption" for each kWh a US data centre used in 2023, from the regional grid mix where data centres sit (December 2024, section 5, beside its Figure 5.10; about 800 billion litres over 176 TWh). Each kWh of computing buys PUE kWh, so the whole figure is site WUE plus PUE times 4.52: air with tower 1.5 × 4.52 = 6.8, plus 2.9, about 9.7 litres; air-cooled chiller 1.8 × 4.52 = 8.1; liquid with tower 1.1 × 4.52 = 5.0, plus 2.0, about 7.0; liquid with dry cooler about 5.0. Dropping the tower in the air hall adds 0.3 × 4.52, about 1.4 litres, at the power station. On a fixed supply, computing scales with 1 divided by PUE, and 1.8 divided by 1.1 is about 1.64. The air and liquid rows compare a midsize hall with a large one, as the lab simulated them, and the method ignores power purchase agreements and on-site generation, which the lab also leaves out.

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
| Ypsilanti, Michigan | The Ypsilanti Community Utilities Authority, set up by the city and township, adopted Resolution 26-08 at its meeting of 22 April 2026: an immediate moratorium on the delivery, commitment, reservation, extension or approval of water and sewer services to data centres and AI computing facilities, at the township's request (Resolution 2026-08, 15 April 2026, asking for not less than 12 months pending supply, wastewater, rate and capital studies) | YCUA Resolution 26-08; Ypsilanti Township Resolution 2026-08 |
| Pinal County, Arizona | Board of Supervisors voted 4-1 on 26 August 2026 against rezoning for Vermaland's La Osa campus near Eloy, cut from 59 buildings and two gas plants to 11 and one, despite a closed-loop cooling pledge; supervisors cited water, opposition and no end user | Press reports: KTAR (26 August 2026), AZFamily (7 September 2026); county minutes not read |

The 140 kW rack is the GB300 NVL72, a Blackwell-generation design; Nvidia said on 26 August 2026 that Vera Rubin, its next, was ramping into full production with racks running at partners. Peak water: University of California, Riverside, news release of 12 March 2026 on the preprint "Small bottle, big pipe" (arXiv 2603.02705), which puts peak-day evaporative demand at six to ten times average, over 30 times for some planned sites; these are the authors' estimates.

Jane Street: this page cites the video tour (15 May 2026) and Jane Street's write-up of the site, which names the guides as Ron Minsky, who co-leads its technology group, and Dan Pontecorvo, who runs physical engineering; not the longer conversation the three released on 21 May.

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

<p class="sources">Sources: Lawrence Berkeley National Laboratory, its report on United States data centre energy use (December 2024), Tables 4.2 and 4.3 and Figures 4.2, 4.4, 4.5 and 4.7; The Green Grid, WUE white paper (March 2011); Google's 2025 and 2026 Environmental Reports and its post on liquid cooling at the OCP EMEA Summit (30 April 2025); Amazon Web Services' sustainability page (2025 figures); Microsoft's posts of 9 December 2024 and 24 June 2026; Google's post on watershed health (15 December 2023); Chile's Second Environmental Court, ruling of 26 February 2024; Schneider Electric (17 October 2024) and Eaton (12 March 2026) releases; Nvidia's posts of 21 June and 24 August 2026 and results release of 26 August 2026; University of California, Riverside (12 March 2026); YCUA Resolution 26-08 (22 April 2026) and Ypsilanti Township Resolution 2026-08 (15 April 2026); KTAR and AZFamily on Pinal County (26 August and 7 September 2026); Jane Street's video tour with Dwarkesh Patel (15 May 2026) and its write-up of the site, with Ron Minsky and Dan Pontecorvo. Heatmap's count of cancelled projects (6 May 2026). Personal research, not investment advice.</p>
