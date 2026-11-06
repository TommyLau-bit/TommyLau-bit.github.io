---
title: "Powering the rack: 800 volts reaches the AI rack before it reaches the building"
date: 2026-08-07
summary: "An AI rack now draws so much power that the copper and power supplies wired for it would crowd out the computers, so the industry is moving it from 54 volts to 800. The building around it cannot change as fast, so on Nvidia's own dates the new voltage arrives first as a cabinet beside the rack, fed from the old power room. That order means more power gear in every megawatt until halls run on 800 volts from the grid in."
category: "Analysis"
cover: "/covers/powering-the-rack.svg"
tags: ["power", "data-centres", "800VDC"]
updated: 2026-11-06
updateNote: "Now traces one megawatt from the grid to the chip and shows why the power room changes last, with evidence to 6 November 2026."
draft: false
---

Nvidia has done something unusual for a chipmaker. It has written down why its own design cannot go on. Wired as racks are today, a rack of its AI chips would need up to 200 kilograms of copper bar to carry one megawatt.

Its power supplies would fill up to 64 of the rack's slots, leaving, in Nvidia's words, no room for the computers.

The fix is to move the rack from 54 volts to 800. The building around it cannot change as fast.

So 800 volts reaches the rack before it reaches the building, and that order decides what gets bought while the building waits.

"800 volts" is three products, not one. A power rack is a cabinet of converters beside the computers, fed from the building's old power room. A row power centre serves a whole row. A building block turns the grid's supply into the new voltage at the building's edge, and the old power room shrinks. They differ in where the grid's alternating current becomes the direct current chips use, and this piece is about their order.

The chain behind that order has five steps. First, racks are climbing towards a megawatt, and Nvidia says today's racks start to hit physical limits at a fifth of that. Second, current is power divided by voltage, so a megawatt at 54 volts is about 18,500 amps, and that current is what needs the copper and the power supplies. Third, at 800 volts the current falls to a fifteenth, and since copper is sized by current, only a higher voltage shrinks it. Fourth, the rack changes with each chip generation, while the power room is designed years ahead, so the new voltage starts beside the rack, fed from the old room. Fifth, each megawatt therefore carries both for a while: the old room and the new cabinet, so more gear, not less.

<details class="analogy">
<summary>The analogy</summary>
<p>A busy restaurant's new ovens draw far more power than its kitchen was wired for. Closing to rewire is out, so the electrician wheels a power cabinet beside each oven, fed from the old fuse board: that is the power rack. One bigger cabinet for a whole line of ovens is the row power centre.</p>
<p>The lasting fix is a new mains supply into the building, the building block, and it waits for the next full refit. Until then the restaurant pays for both: the old fuse board stays, and every oven gets its cabinet too.</p>
</details>

Trace one megawatt from the street to the chip and the order explains itself. It passes five conversions, and only one is slow to change.

<figure class="chart">
<p class="chart-title">The power room changes last, because it is bought years ahead and kept for decades</p>
<p class="chart-sub">One megawatt traced from the grid to the chip, with the current it needs at each step</p>
<svg viewBox="0 0 560 196" role="img" aria-label="Diagram of five conversions in order, carrying one megawatt. One, grid: 35 kilovolts AC, about 16 amps per phase. Two, the AC power room: transformer and UPS, 415 volts AC, about 1,390 amps per phase. This is the choke point: it is booked years ahead and the specification for its 800 volt replacement was at version 0.3 in July 2026. Three, the rack: 54 volts DC is about 18,500 amps, 800 volts DC is 1,250 amps; it changes with each chip generation. Four, the tray: stepped to 12 volts, about 83,000 amps; new 800 volt designs use GaN switches for this step. Five, the chip: below 1 volt; at an assumed 0.8 volts, about 1.25 million amps.">
<rect class="c-box" x="5.0" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="13.0" y="66">1. Grid</text>
<text class="c-note" x="13.0" y="88">35 kV AC</text>
<text class="c-note" x="13.0" y="106">about 16 A</text>
<text class="c-note" x="13.0" y="124">per phase</text>
<line class="c-arrow" x1="106.4" y1="97" x2="111.4" y2="97"/><polygon class="c-arrow-head" points="116.4,97 110.4,93 110.4,101"/>
<rect class="c-zone" x="113.4" y="14" width="108.4" height="144" rx="4"/>
<text class="c-zone-t" x="167.6" y="30" text-anchor="middle">THE CHOKE POINT</text>
<rect class="c-box" x="117.4" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="125.4" y="66">2. AC room</text>
<text class="c-note" x="125.4" y="88">Transformer</text>
<text class="c-note" x="125.4" y="106">and UPS</text>
<text class="c-note" x="125.4" y="124">415 V AC</text>
<text class="c-note" x="125.4" y="142">about 1,390 A</text>
<line class="c-arrow" x1="218.8" y1="97" x2="223.8" y2="97"/><polygon class="c-arrow-head" points="228.8,97 222.8,93 222.8,101"/>
<rect class="c-box" x="229.8" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="237.8" y="66">3. Rack</text>
<text class="c-note" x="237.8" y="88">54 V: 18,500 A</text>
<text class="c-note" x="237.8" y="106">800 V: 1,250 A</text>
<text class="c-note" x="237.8" y="124">Changes each</text>
<text class="c-note" x="237.8" y="142">chip cycle</text>
<line class="c-arrow" x1="331.2" y1="97" x2="336.2" y2="97"/><polygon class="c-arrow-head" points="341.2,97 335.2,93 335.2,101"/>
<rect class="c-box" x="342.2" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="350.2" y="66">4. Tray</text>
<text class="c-note" x="350.2" y="88">Steps to 12 V</text>
<text class="c-note" x="350.2" y="106">about 83,000 A</text>
<text class="c-note" x="350.2" y="124">GaN in new</text>
<text class="c-note" x="350.2" y="142">800 V designs</text>
<line class="c-arrow" x1="443.6" y1="97" x2="448.6" y2="97"/><polygon class="c-arrow-head" points="453.6,97 447.6,93 447.6,101"/>
<rect class="c-box" x="454.6" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="462.6" y="66">5. Chip</text>
<text class="c-note" x="462.6" y="88">Below 1 V</text>
<text class="c-note" x="462.6" y="106">about 1.25m A</text>
<text class="c-note" x="462.6" y="124">at 0.8 V,</text>
<text class="c-note" x="462.6" y="142">my estimate</text>
<text class="c-lab c-s2t" x="117.4" y="180" text-anchor="start">Booked years ahead; 800 V spec at version 0.3</text>
</svg>
<figcaption>Voltages from Nvidia's Technical Blog (13 October 2025); specification version from Nvidia's blog (11 August 2026). Currents are my arithmetic at one megawatt, ignoring losses; three-phase AC per phase; the chip voltage of 0.8 V is my assumption. My framing of the chain.</figcaption>
</figure>

The second step binds. The rack and tray are products, redesigned with each chip generation. The power room is designed years ahead and runs for decades, its makers hold years of orders, and the standard for its replacement is unfinished.

So the change starts beside the computers, and Nvidia's own dates follow that order: the power rack in the second half of 2026, a unit for a whole row in 2027, and the building step described but not dated.

<hr class="layer">
<p class="layer-label">For investors</p>

## 800 volts reaches the rack years before the building, so each megawatt carries both for now

<a id="powering-the-rack"></a>

The order decides what gets bought first, and rack power forces it. Google, which designs its own AI chips and data centres, scaled its 48 volt architecture from 10 kW racks to 100 kW. Vertiv, a maker of data centre power and cooling gear, has a reference design for Nvidia's GB200 NVL72, the AI chip leader's current rack, that runs up to 132 kW. Nvidia's next rack, Kyber, is to house 576 Rubin Ultra GPUs by 2027, at around a megawatt.

<figure class="chart">
<p class="chart-title">The rack is heading far past what its wiring can carry</p>
<p class="chart-sub">Power per rack, in kilowatts, against the point where Nvidia says 54 volt racks start to fail</p>
<svg viewBox="0 0 560 244" role="img" aria-label="Bar chart of power per rack. Google's 48 volt design scaled from 10 kilowatt racks to 100 kilowatts. Vertiv's GB200 NVL72 design runs up to 132 kilowatts. Google expects more than 500 kilowatts per rack before 2030, and Nvidia's 800 VDC design targets 1 megawatt racks from 2027. Nvidia says 54 volt racks start to hit physical limits above 200 kilowatts, so the last two sit past that limit.">
<rect class="c-zone" x="256" y="10" width="284" height="224"/>
<text class="c-zone-t" x="266" y="29">Past the 54 V limit, 200 kW</text>
<g class="c-axis">
<text x="188" y="56.5" text-anchor="end">48 V design, first racks</text>
<text x="188" y="96.5" text-anchor="end">48 V design, largest</text>
<text x="188" y="136.5" text-anchor="end">GB200 NVL72 design, 2024</text>
<text x="188" y="176.5" text-anchor="end">Google, before 2030</text>
<text x="188" y="216.5" text-anchor="end">Nvidia Kyber, from 2027</text>
</g>
<rect class="c-bar c-mute" x="196" y="40" width="3.0" height="24" rx="2"/>
<text class="c-note" x="207" y="57">10 kW</text>
<rect class="c-bar c-mute" x="196" y="80" width="30.0" height="24" rx="2"/>
<text class="c-note" x="234" y="97">100 kW</text>
<rect class="c-bar" x="196" y="120" width="39.6" height="24" rx="2"/>
<text class="c-lab c-s2t" x="243.6" y="137">up to 132 kW</text>
<rect class="c-bar c-alt" x="196" y="160" width="150.0" height="24" rx="2"/>
<text class="c-lab c-s3t" x="354" y="177">more than 500 kW</text>
<rect class="c-bar c-alt" x="196" y="200" width="300.0" height="24" rx="2"/>
<text class="c-lab c-s3t" x="504" y="217">1 MW</text>
<line class="c-base" x1="196" y1="10" x2="196" y2="234"/>
</svg>
<figcaption>Google Cloud blog, 30 April 2025 (10 to 100 kW; more than 500 kW before 2030); Vertiv, 15 October 2024 (132 kW); Nvidia Technical Blog, 20 May 2025 (200 kW limit; 1 MW racks starting in 2027). The 500 kW is a floor, so its bar is the least it could be.</figcaption>
</figure>

<a id="the-rack-runs-out-of-copper"></a>

That megawatt is what breaks today's wiring, and Nvidia made the case itself in May 2025. Above 200 kW, it wrote, racks start "to hit physical limits". A 1 MW rack at 54 volts would need up to 200 kg of copper busbar, and up to 200,000 kg across a gigawatt site. Its power shelves, the rack's converters, "would consume up to 64 U of rack space for Kyber at MW scale", leaving no room for compute. So the rack moves now: Nvidia dates an 800 VDC power rack to the second half of 2026 and a row power centre to 2027, and gives the building no date. Until then the AC room stays and the cabinets join it.

## Six things hold the building back, and none of them changes with a chip generation

The rack changes every year; the power room is bought years ahead and kept for decades. So the change moves outward in phases.

<figure class="chart">
<p class="chart-title">The new voltage starts beside the rack and reaches the building last</p>
<p class="chart-sub">Where power is converted, from the grid to the chip, in each phase; the shaded box is what changes</p>
<svg viewBox="0 0 560 270" role="img" aria-label="Diagram of three power chains. Today: grid at 13.8 to 35 kilovolts AC, an AC power room at 415 volts AC, a power shelf in the rack at 54 volts DC, then the tray and board down to below 1 volt. First phase, with Nvidia's power rack in 2026 and row unit in 2027: the same grid and AC room, then a power rack beside the computer rack making 800 volts DC, then the tray down to below 1 volt. Last phase, not dated: the grid feeds a rectifier or solid-state transformer that makes 800 volts DC for the whole building, carried on DC busway to the rack and then down to below 1 volt.">
<text class="c-lab c-s1t" x="8" y="22">Today: alternating current all the way to the rack</text>
<rect class="c-box" x="8" y="32" width="126" height="44" rx="4"/><text class="c-box-t" x="18" y="50">Grid</text><text class="c-note" x="18" y="67">13.8 to 35 kV AC</text>
<line class="c-arrow" x1="135" y1="54" x2="139" y2="54"/><polygon class="c-arrow-head" points="144,54 138,50 138,58"/>
<rect class="c-box" x="146" y="32" width="126" height="44" rx="4"/><text class="c-box-t" x="156" y="50">AC power room</text><text class="c-note" x="156" y="67">415 V AC</text>
<line class="c-arrow" x1="273" y1="54" x2="277" y2="54"/><polygon class="c-arrow-head" points="282,54 276,50 276,58"/>
<rect class="c-box" x="284" y="32" width="126" height="44" rx="4"/><text class="c-box-t" x="294" y="50">Power shelf</text><text class="c-note" x="294" y="67">54 V DC</text>
<line class="c-arrow" x1="411" y1="54" x2="415" y2="54"/><polygon class="c-arrow-head" points="420,54 414,50 414,58"/>
<rect class="c-box" x="422" y="32" width="126" height="44" rx="4"/><text class="c-box-t" x="432" y="50">Tray to chip</text><text class="c-note" x="432" y="67">down to below 1 V</text>
<text class="c-lab c-s1t" x="8" y="112">First: 800 V at the rack (power rack 2026, row unit 2027)</text>
<rect class="c-zone" x="279" y="117" width="136" height="54" rx="4"/>
<rect class="c-box" x="8" y="122" width="126" height="44" rx="4"/><text class="c-box-t" x="18" y="140">Grid</text><text class="c-note" x="18" y="157">13.8 to 35 kV AC</text>
<line class="c-arrow" x1="135" y1="144" x2="139" y2="144"/><polygon class="c-arrow-head" points="144,144 138,140 138,148"/>
<rect class="c-box" x="146" y="122" width="126" height="44" rx="4"/><text class="c-box-t" x="156" y="140">Same AC room</text><text class="c-note" x="156" y="157">415 V AC</text>
<line class="c-arrow" x1="273" y1="144" x2="277" y2="144"/><polygon class="c-arrow-head" points="282,144 276,140 276,148"/>
<rect class="c-box" x="284" y="122" width="126" height="44" rx="4"/><text class="c-box-t" x="294" y="140">Power rack</text><text class="c-note" x="294" y="157">800 V DC</text>
<line class="c-arrow" x1="411" y1="144" x2="415" y2="144"/><polygon class="c-arrow-head" points="420,144 414,140 414,148"/>
<rect class="c-box" x="422" y="122" width="126" height="44" rx="4"/><text class="c-box-t" x="432" y="140">Tray to chip</text><text class="c-note" x="432" y="157">down to below 1 V</text>
<text class="c-lab c-s1t" x="8" y="202">Last: 800 V from the building (not dated)</text>
<rect class="c-zone" x="141" y="207" width="136" height="54" rx="4"/>
<rect class="c-box" x="8" y="212" width="126" height="44" rx="4"/><text class="c-box-t" x="18" y="230">Grid</text><text class="c-note" x="18" y="247">13.8 to 35 kV AC</text>
<line class="c-arrow" x1="135" y1="234" x2="139" y2="234"/><polygon class="c-arrow-head" points="144,234 138,230 138,238"/>
<rect class="c-box" x="146" y="212" width="126" height="44" rx="4"/><text class="c-box-t" x="156" y="230">Rectifier or SST</text><text class="c-note" x="156" y="247">800 V DC</text>
<line class="c-arrow" x1="273" y1="234" x2="277" y2="234"/><polygon class="c-arrow-head" points="282,234 276,230 276,238"/>
<rect class="c-box" x="284" y="212" width="126" height="44" rx="4"/><text class="c-box-t" x="294" y="230">DC busway</text><text class="c-note" x="294" y="247">800 V DC</text>
<line class="c-arrow" x1="411" y1="234" x2="415" y2="234"/><polygon class="c-arrow-head" points="420,234 414,230 414,238"/>
<rect class="c-box" x="422" y="212" width="126" height="44" rx="4"/><text class="c-box-t" x="432" y="230">Tray to chip</text><text class="c-note" x="432" y="247">down to below 1 V</text>
</svg>
<figcaption>Voltages and steps from Nvidia's Technical Blog (20 May and 13 October 2025) and its blog of 11 August 2026. SST is a solid-state transformer. At 54 V the tray steps down to 12 V; at 800 V one converter steps to 12 V, or to 6 V in Texas Instruments' design (16 March 2026), before the last step to below 1 V.</figcaption>
</figure>

**Booked years ahead.** The power room's transformer and switchgear makers hold years of orders, as [the equipment queue](/journal/the-equipment-queue/) shows. My inference from those order books, not any maker's statement: a hall opening in 2028 has probably already booked gear for an AC power room.

**Built to last decades.** No owner rips out a working power room for one rack generation.

**No finished specification.** The solid-state transformer specification Nvidia cites, for the electronic replacement of the room's transformer, had reached only version 0.3 by July 2026.

**The off switch.** Direct current never passes through zero, so the breakers built for alternating current cannot simply be reused. An 800 volt building needs new protection, much of it solid-state.

**New rules for inspectors.** Local code officials and inspectors are often unfamiliar with 800 volt halls, a sponsored trade article of 26 October 2026 says, so approvals and safety work take time.

**The backup moves.** Today's UPS, the battery system that rides through dips, is redesigned rather than swapped: in Nvidia's end state, capacitors sit beside the racks and batteries at the grid connection.

## The end state removes gear; the road to it adds gear first

<a id="every-megawatt-got-harder"></a>

Read from its end state, 800 VDC looks simpler: grid power turned straight into 800 volts at the building's edge, fewer conversions, a smaller UPS, less copper. Read that way it is a silicon carbide story that removes gear. The order delivers the opposite first. The AC room stays and a power rack joins it, so gear per megawatt rises before it falls. The power supplies move into a cabinet on the floor, and the floor is there: the refitted Texas site of Jane Street, the trading firm, in [heat and water](/journal/heat-and-water/#room-to-spare), fills its whole grid allowance with racks that take a small fraction of the floor once set aside for chips.

Vertiv is the one maker to put a figure on what a megawatt holds. Its management estimated in May 2026 that it could sell about US$3.25 million to 3.75 million of power and cooling gear into each megawatt of IT power, up about 10 to 15% on its earlier range. That is an estimate of opportunity, not reported revenue. In the third quarter of 2026 Vertiv's sales grew 55.0% organically and its adjusted operating margin widened 2.9 points to 25.2%, with organic orders more than doubling, which fits operating leverage as well as richer gear.

The road is long. On Vertiv's third-quarter call of 28 October 2026, per a transcript, chief executive Giordano Albertazzi called 2027 the customer validation phase for its 800 volt range, with first revenue that year, and put deployment in 2028. He described the road as 800 volts to the rack first, fed by medium or low voltage AC, before an end-to-end 800 volt system. Nvidia's statements give the same order.

<figure class="chart">
<p class="chart-title">Nvidia dates the rack and the row, but not the building</p>
<p class="chart-sub">Nvidia's own 800 VDC statements, from the date it said them to the date it gave</p>
<svg viewBox="0 0 560 210" role="img" aria-label="Timeline of Nvidia's statements. On 20 May 2025 Nvidia said 1 megawatt racks start in 2027 with Kyber. On 11 August 2026 it dated its power rack to the second half of 2026 and its row power centre to 2027, and described a building-level DC power block without a date.">
<g class="c-grid"><line x1="200" y1="20" x2="200" y2="180"/><line x1="285" y1="20" x2="285" y2="180"/><line x1="370" y1="20" x2="370" y2="180"/><line x1="455" y1="20" x2="455" y2="180"/><line x1="540" y1="20" x2="540" y2="180"/></g>
<g class="c-axis">
<text x="200" y="200" text-anchor="middle">2025</text><text x="285" y="200" text-anchor="middle">2026</text><text x="370" y="200" text-anchor="middle">2027</text><text x="455" y="200" text-anchor="middle">2028</text><text x="540" y="200" text-anchor="middle">2029</text>
<text x="188" y="48" text-anchor="end">Kyber, 1 MW racks</text>
<text x="188" y="88" text-anchor="end">Power rack</text>
<text x="188" y="128" text-anchor="end">Row power centre</text>
<text x="188" y="168" text-anchor="end">Building DC block</text>
</g>
<line class="c-today" x1="355.3" y1="14" x2="355.3" y2="180"/><text class="c-today-t" x="355.3" y="12" text-anchor="middle">today</text>
<g class="c-span"><line x1="232.4" y1="44" x2="412.5" y2="44"/><line x1="336.7" y1="84" x2="348.8" y2="84"/><line x1="336.7" y1="124" x2="412.5" y2="124"/></g>
<g class="c-start"><circle cx="232.4" cy="44" r="4"/><circle cx="336.7" cy="84" r="4"/><circle cx="336.7" cy="124" r="4"/><circle cx="336.7" cy="164" r="4"/></g>
<g class="c-end"><circle cx="412.5" cy="44" r="4.5"/><circle cx="348.8" cy="84" r="4.5"/><circle cx="412.5" cy="124" r="4.5"/></g>
<g class="c-endt"><text x="420.5" y="48">2027</text><text x="364" y="88">second half 2026</text><text x="420.5" y="128">2027</text></g>
<text class="c-note" x="364" y="168">described, not dated</text>
</svg>
<figcaption>Hollow dot: when Nvidia said it. Solid dot: the date it gave, with a year or half year placed at its middle. Sources: Nvidia Technical Blog, 20 May 2025; Nvidia blog, 11 August 2026. Press reports contest the timing; only Nvidia's own words are shown.</figcaption>
</figure>

## Four terms and three materials carry the argument

**Volts, amps and watts.** Watts are volts times amps: voltage is the push, current the flow of charge, power their product. At a higher voltage the same power needs less current.

**Resistive loss.** Heat in a conductor is the current squared times its resistance, so doubling the current quadruples the heat, like friction in a pipe rising with the flow.

**AC, DC and ±400 volts.** Alternating current reverses 50 or 60 times a second, which lets a copper and steel transformer step it; direct current flows one way, which is what chips use. Google called for ±400 VDC, 400 volts each side of earth, to take racks "from 100 kilowatts up to 1 megawatt". That is 800 volts pole to pole, so the claim below counts it as 800 volts.

**Switching loss.** A converter chops current on and off up to millions of times a second, and in each transition the switch briefly carries voltage and current at once. That overlap is heat, so a faster switch wastes less per flick.

The material of the switch sets how much voltage it can block, how hot it can run and how fast it can flick. The reason is the bandgap, the energy an electron needs to break loose and conduct. Silicon carbide's and gallium nitride's are about three times silicon's, so they hold about ten times the electric field before breaking down. A switch blocking 800 volts can then be about a tenth as thick, so it loses less when on and switches faster, which lets the transformers and inductors around it shrink. Silicon carbide also moves heat about three times better than silicon; gallium nitride switches fastest but moves heat slightly worse.

So silicon carbide, SiC, belongs at the top, where voltages run to kilovolts and heat is the enemy. Infineon, a German power chip maker, and SolarEdge, a solar inverter maker, are developing a 2 to 5 MW solid-state transformer block on Infineon's SiC switches. Gallium nitride, GaN, belongs at or below the 800 volt bus, and takes 800 volts by stacking parts rated at 650. Texas Instruments, a maker of the small power chips beside the processor, has an 800 to 6 volt converter that uses GaN at 97.6% peak efficiency. On my reading, silicon stays at the last low-voltage step, where it is cheapest. The phased framing and this split come from SemiAnalysis, a chip and AI research firm, in the free part of its "Inside the 800VDC Revolution, Part 1" (26 May 2026); the makers' own releases place them.

## 18,500 amps is the number that moves the rack

The number is plain arithmetic. Amps are watts divided by volts, so a megawatt at 54 volts is 1,000,000 divided by 54, about 18,500 amps, and at 800 volts it is 1,250. The ratio is about 14.8, before losses.

It means copper because heat goes with current squared. Keep the same bar and cut the current 14.8 times, and its heat falls about 219 times. In practice the gain is taken as thinner copper, because a bar is sized to carry its current without overheating.

The trap is the comparison. Against 54 volts DC inside the rack the gain is fifteenfold; against the building's 415 volts AC it is smaller. Moving a row from 415 volts AC to 800 volts DC carries 85% more power through the same conductor size and cuts copper by 45%, Nvidia's May 2025 post says. And less copper per unit of power is not less copper: power per rack is rising faster than the saving.

Traced down the chain, the arithmetic shows why every design converts to low voltage as late and as close to the chip as it can. At one megawatt the current is about 16 amps per phase on a 35 kV feed and about 1,390 amps per phase at 415 volts. It is about 83,000 amps at 12 volts, and at an assumed 0.8 volts at the cores about 1.25 million, spread over thousands of power stages, each millimetres from the silicon.

## Value sits first with the cabinet builders and the fast switches, and later with silicon carbide

<a id="ti-feeds-the-chip"></a>

Rack first pays the cabinet builders now: makers of power racks, converters and building power systems sell a cabinet for every new row while the AC room keeps selling too.

The fast switches are pulled forward with them: GaN makers, and the chips beside the processor. Texas Instruments' data centre business was 9% of revenue in 2025, about US$1.5bn. It doubled in the second quarter of 2026 and grew about 95% in the third, to about 13% of revenue, in management's words on the call. But racks shipping in volume today run at 48 and 54 volts, and TI names power density and higher voltage together as drivers, so the growth so far is density, not 800 volts.

The old power room is the quiet one. Transformer, switchgear and UPS makers keep selling AC rooms to every hall built while the building waits. SiC makers wait longest, for the transformer volume that comes only when buildings follow. Makers of 54 volt power shelves and in-rack copper bar lose their place inside the rack.

## What would prove me wrong

The test is a named hall. If, before 2028, Nvidia, an operator or its supplier says a hall of 10 MW or more is in service on 800 volts made by a central rectifier or solid-state transformer, the building did not wait for the rack. Foxconn's 40 MW Kaohsiung-1, the Taiwanese electronics maker's AI data centre, is one to watch.

Two events would move me before the test. Nvidia giving its DC power block a date before 2028, or the solid-state transformer specification reaching a finished version, would show the building catching up. And if power racks ship but Vertiv cuts its per-megawatt estimate, or halls drop the AC room as racks arrive, more gear first is wrong even if the order holds.

The claim stands on two legs. The rack must move: that is physics, current against copper, and no falsifier attacks it; only a rack that stops growing would. The building waits: that rests on equipment, standards and protection, which money and a greenfield owner can speed. The named hall and the dated building step attack that leg; the Vertiv test attacks its consequence.

Plans would not move me. Nvidia said in May 2025 that full-scale production would coincide with Kyber in 2027. Kaohsiung-1 is being built for 800 VDC, and five cloud providers selling AI computing, among them CoreWeave and Oracle Cloud Infrastructure, are "designing for" 800 volt data centres. Each is a design, not a running hall.

Nor would the view that 800 VDC is a silicon carbide story today. On Nvidia's and Vertiv's own dates the first products are power racks fed by AC rooms, so GaN and tray converters move first, and SiC transformers wait for buildings.

## GaN's supply changes hands just as the rack pulls it forward

Rack first pulls GaN forward, and its supply base is reshuffling at the same moment. Navitas, a GaN chip maker, said in a filing of 1 July 2025 that the leading foundry will end GaN production in July 2027, and that moving its 650 volt parts to Powerchip, a Taiwanese foundry, would take about 12 to 24 months. Infineon is to invest about €1.1 billion by 2034 in GaN on 300 mm wafers at Villach in Austria, with volume production from the end of 2027 and €319 million of EU state aid approved, electrive, an electric vehicle trade site, reported on 28 October 2026. Innoscience, a Chinese GaN maker, said its shipments of chips for AI and data centres rose 183% in the first half of 2026.

I concede this is not a shortage call: GaN is a small share of a rack's cost, and silicon or SiC can make the 800 volt step less efficiently. But timing matters. A design-in is for a part from a named fab, so a fab change means requalifying, and Navitas's own 12 to 24 months land inside the rack-first window of 2026 to 2028.

## Envision runs a building-fed 800 volt system, but no size is stated

On 2 November 2026 Envision, a Chinese wind turbine, battery and energy software group, said in its own release that an 800 VDC system on solid-state transformers, converting 10 kV straight to an 800 volt bus, is "now powering live computing workloads" at its Ulanqab campus in Inner Mongolia. That is an operator, a building-level converter and live load: the falsifier's shape.

I concede the building step is closer than undated sounds, and if Envision states 10 MW or more before 2028, the claim breaks. It gives no size for the 800 volt system, and the 3 GW it cites is the plan for the whole campus. It shows who can skip the queue: one owner building its own system, with storage and renewable supply, on a new campus opened in August 2026. The typical hall, fed through an AC room ordered years ahead, still goes rack first, and Vertiv, which sells into those halls, gives the same order.

<a id="the-off-switch"></a>
## The off switch, not the converter, may set the building's pace

A view I am testing is that protection, not conversion, decides when buildings switch over. Alternating current passes through zero 100 or 120 times a second, and a mechanical breaker uses that moment to put out its arc. Direct current never does. "Without a natural current zero, mechanical interruption faces challenges with arcing," Infineon said on 9 September 2026, announcing a solid-state breaker with SolarEdge, built on its SiC switches and designed to cut a fault within a few microseconds.

The inference is mine. Beside the rack, each power rack's converters limit how much current a fault can draw. On a building-wide 800 volt bus fed by megawatt transformers, batteries and capacitors, a fault can draw on all of them at once. If that is right, rack first is also the safer order, the building step waits on a new class of breaker as much as on the converter, and SiC enters data halls early, inside breakers, before solid-state transformers bring volume.

The test is whether building-fed systems publish their breaker ratings, and whether rules for solid-state breakers settle. What would kill the idea is a hall of 10 MW or more on a building bus, signed off quickly with ordinary DC fuses and breakers.

## At chip, rack and building, the slowest part sets the pace

At the scale of the chip, the material follows the voltage: silicon at the last step, GaN at and below the 800 volt bus, SiC in kilovolts at the grid side, and rack first moves the GaN layer first.

At the scale of the rack, current sets the copper, and a megawatt at 54 volts leaves no choice, so the rack moves now, in a cabinet beside it.

At the scale of the building, rooms booked years ahead, an unfinished specification and a new class of breaker set the pace, unless one owner builds the end state from scratch.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

The test this piece stands behind, quoted word for word:

**Powering the rack** (30 October 2026)

Claim: "800 volts reaches the AI rack before it reaches the building: until 2028, 800 VDC enters data halls through power racks and row power centres fed from AC power rooms, and no data hall of 10 MW or more goes into service fed by a facility-level rectifier or solid-state transformer. 800 VDC here includes ±400 VDC, 800 V pole to pole."

Breaks if: "Before 1 January 2028, Nvidia, a data centre operator or its equipment supplier states that a data hall of 10 MW or more is in service with 800 VDC distributed from a facility-level rectifier or solid-state transformer, rather than from power racks or row power centres fed by AC. 800 VDC includes ±400 VDC, 800 V pole to pole."

Earlier claims on the rack's power:

**Vertiv is paid per megawatt, and AI has made every megawatt harder to build** (25 September 2026)

Claim: "What Vertiv sells per megawatt is rising, because AI makes every megawatt harder to power and cool."

Breaks if: "Vertiv's growth only ever tracks the megawatts being built, or its margin shrinks while orders stay strong, or the biggest buyers take cooling in-house."

Where later evidence bears on it: service revenue no longer supports it. Its reported growth was swollen by acquisitions; organically, services and spares grew 18.1% in the third quarter of 2026 against 63.6% for products. The margin limb has not broken: 25.2%, up 2.9 points, with orders more than doubling. But that margin fits operating leverage as well as richer content. The claim now rests on Vertiv's own per-MW estimate, up about 10 to 15%. The in-house limb is partly met, and was from the start: Google's own blog (30 April 2025) says it has liquid-cooled its TPUs since 2018 "at GigaWatt scale". So at least one of the biggest buyers already designs its own cooling.

**The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones** (2 October 2026)

Claim: "The move to 800 volt racks turns Texas Instruments' small, cheap power chips into a growing data centre business."

Breaks if: "Racks stay at 54 volts for years, or rivals hold the demanding high end, or TI's new 300mm lines run part-empty as industrial and car demand weakens."

Where later evidence bears on it: the growing data centre business is here, about 13% of revenue in the third quarter of 2026. But it grew before 800 V racks ship in volume, so the cause the claim names is not yet shown. TI names power density and higher voltages together, so the growth so far cannot be pinned on 800 V. Nvidia dates its own 800 V power rack to the second half of 2026, so the first limb cannot be tested before 2027. Industrial grew more than 40%, so the part-empty limb is not near.

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

Every watt an AI chip uses passes through the same chain of conversions, each made by a different set of firms:

| Step | Today, AC to the rack | 800 VDC end state | Switching material | Who makes it |
|---|---|---|---|---|
| Grid to building | Medium voltage, for example 13.8 kV or 35 kV AC, stepped down by a transformer to 415 or 480 VAC | Medium voltage AC converted straight to 800 VDC at the edge of the building, by a rectifier or a solid-state transformer | SiC in solid-state transformers | Hitachi Energy, GE Vernova, ABB, Siemens, Schneider Electric, Eaton, Vertiv |
| Backup | UPS converts AC to DC and back again | Capacitors beside the racks; batteries at the grid connection | Not stated | Vertiv, Schneider Electric, Eaton |
| Room to rack | 415 or 480 VAC on busway | 800 VDC on two-conductor busway | None, it is copper | Vertiv, Schneider Electric, Eaton |
| Rack to tray | Power shelves turn 415 VAC into 54 VDC on a copper busbar | 800 VDC enters the tray directly | Varies by design | Delta, LiteOn, Flex, Megmeet |
| Tray to board | 54 V to 12 V | One converter steps 800 V to 12 V at about 64 to 1, or 800 V to 6 V | GaN, low-voltage on today's 54 V step; high-voltage at 800 V | Navitas, Innoscience, Infineon, TI |
| Board to chip | 12 V to below 1 V | 12 V or 6 V to below 1 V | Power stages, many per processor | TI, Monolithic Power, Infineon, Renesas, Analog Devices |

The voltages and steps are Nvidia's (20 May and 13 October 2025). The 800 V to 6 V step is Texas Instruments' design (16 March 2026). On materials: Infineon and SolarEdge's SST block converts 13.8 to 34.5 kV to 800 to 1,500 V DC (5 November 2025); Navitas sells SiC from 650 V to 6,500 V; its GTC board (March 2026) uses 16 of its 650 V GaN switches in a stacked full bridge with 25 V silicon switches on the output side; its 100 V GaN is "optimised for the lower-voltage DC-DC stages on GPU power boards" (October 2025). Infineon sells all three materials and expects the share of power semiconductors in an 800 VDC design to be similar to or higher than in today's AC one (May 2025).

The same megawatt traced in current, my arithmetic at 1 MW, ignoring losses (three-phase AC per phase at unity power factor; current equals power divided by voltage):

| Point in the chain | Voltage | Current |
|---|---|---|
| Grid feed | 35 kV AC | about 16.5 A |
| Power room output | 415 V AC | about 1,391 A |
| Rack today | 54 V DC | 18,519 A |
| Rack at 800 V | 800 V DC | 1,250 A |
| Tray output | 12 V DC | 83,333 A |
| GPU cores | about 0.8 V, my assumption; core voltages run below 1 V and vary by chip and load | about 1,250,000 A |

Material values, room temperature: bandgap 1.12 eV for silicon, 3.26 for 4H-SiC, 3.4 for GaN; critical breakdown field about 0.3, 2.8 and 3.3 MV/cm; thermal conductivity 1.5, 4.9 and 1.3 W/cm.K (halbleiter.org, read 6 November 2026). A layer blocking a given voltage scales inversely with the field, hence about a tenth as thick.

Since the claim, and against it: Envision's release (PR Newswire, 2 November 2026) gives 10 kV medium voltage to an 800 V DC bus, battery storage for second-scale support and minute-scale backup, campus operations from August 2026, a planned 3 GW campus and no size for the 800 V system. Vertiv's chief executive on the third-quarter call (28 October 2026, per a published transcript): "revenue generating during 2027, and 2027 being the validation phase, customer validation", with deployment "in '28". Infineon's release (9 September 2026): the SolarEdge solid-state breaker sits between the solid-state transformer and the compute rack. Navitas Form 8-K (1 July 2025): the leading foundry "will end GaN production in July 2027"; 650 V parts move to Powerchip "over the next approximately 12-24 months".

Nvidia's own dated statements on timing:

| Date | Nvidia's statement | Source |
|---|---|---|
| 20 May 2025 | 800 VDC targets "1 MW IT racks and beyond, starting in 2027"; full-scale production "will coincide with NVIDIA Kyber rack-scale systems in 2027" | Nvidia Technical Blog |
| 13 October 2025 | Kyber will house "576 NVIDIA Rubin Ultra GPUs by 2027"; the move "will occur in phases" | Nvidia blog and Technical Blog |
| March 2026 | Nvidia, Google and Microsoft publish a joint 800 VDC white paper through the Open Compute Project | Nvidia blog, 11 August 2026 |
| 11 August 2026 | The 800 VDC power rack arrives "in the second half of 2026"; a row power centre of up to 2 MW per row is expected in 2027; the DC power block for direct medium-voltage conversion is described but not dated | Nvidia blog |

The August post dates the power gear, not Kyber. In October 2025 Nvidia named Foxconn's 40 MW Kaohsiung-1 as being built for 800 VDC.

Rack power, for the first chart:

| Measure | Figure | Source |
|---|---|---|
| Google's 48 V rack architecture | Scaled from 10 kW to 100 kW IT racks | Google Cloud blog, 30 April 2025 |
| Vertiv's GB200 NVL72 reference design | Up to 132 kW per rack, 7 MW in all | Vertiv, 15 October 2024 |
| Where 54 V racks hit physical limits | Above 200 kW | Nvidia Technical Blog, 20 May 2025 |
| Google's expectation | More than 500 kW per rack before 2030 | Google Cloud blog, 30 April 2025 |
| Nvidia's 800 VDC target | 1 MW racks, starting in 2027 | Nvidia Technical Blog, 20 May 2025 |

Content per megawatt and the two companies:

| Measure | Figure | Source |
|---|---|---|
| Vertiv's data centre opportunity per MW of IT power | About US$3.25 million to 3.75 million, up about 10 to 15% on its prior range | Vertiv 2026 Investor Conference, 19 May 2026, management estimate |
| Vertiv, Q3 2026 | Net sales US$4.31bn, 55.0% organic growth; products 63.6% and services and spares 18.1% organic; adjusted operating margin 25.2%, up 2.9 points; organic orders up more than 100%; full-year guide US$14.45bn to 14.85bn at 23.5% to 24.5% | Vertiv Form 8-K, 28 October 2026 |
| TI data centre share of revenue, 2025 | 9%, about US$1.5bn | TI Form 10-K for 2025; call of 27 January 2026 |
| TI data centre growth | Doubled in Q2 2026; about 95% in Q3 2026, about 13% of revenue | TI calls, 22 July and 21 October 2026, per transcript |
| TI, Q3 2026 | Revenue US$6.06bn, up 28%; industrial up more than 40%, its first new peak in four years | TI release and call, 21 October 2026 |

Vertiv does not state its prior per-MW range on its slide. I found no per-MW figure in Eaton's or Schneider Electric's own filings that I could open. Adjusted operating margin is the share of each sale left after running costs, with one-off items stripped out; organic growth strips out acquisitions and currency.

</details>

<section class="exposure">
<h3>Who is exposed if 800 volts reaches the rack before the building</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>Building power systems</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span>, <span class="names">Eaton</span>, <span class="names">ABB</span> and <span class="names">Siemens</span> make UPS, switchgear, busway and rectifiers.</dd>
<dt>Rack power</dt>
<dd><span class="names">Delta</span>, <span class="names">LiteOn</span>, <span class="names">Flex</span> and <span class="names">Megmeet</span> make power shelves and converters.</dd>
<dt>High-voltage switches</dt>
<dd><span class="names">Infineon</span>, <span class="names">onsemi</span>, <span class="names">STMicroelectronics</span> and <span class="names">ROHM</span> make SiC chips; <span class="names">Navitas</span> and <span class="names">Innoscience</span> make GaN ones.</dd>
<dt>At the chip</dt>
<dd><span class="names">Texas Instruments</span>, <span class="names">Monolithic Power</span>, <span class="names">Analog Devices</span> and <span class="names">Renesas</span> make power stages and eFuses. <span class="names">Nvidia</span> sets the 800 VDC design.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Makers of 54 volt power shelves and in-rack copper busbar, and halls with no room for power racks.</dd>
</dl>
</section>

---

<p class="sources">Sources: Nvidia Technical Blog and Nvidia blog posts of 20 May 2025, 13 October 2025 and 11 August 2026; Google Cloud blog (30 April 2025); Vertiv releases of 15 October 2024 and 19 May 2025, its 2026 Investor Conference presentation (19 May 2026), its third quarter 2026 Form 8-K and call transcript (28 October 2026); Texas Instruments' Form 10-K for 2025, its release of 16 March 2026, its third quarter 2026 results and its calls of 27 January, 22 July and 21 October 2026; Infineon releases of May 2025, 5 November 2025 and 9 September 2026; Navitas releases of October 2025 and March 2026 and its Form 8-K (1 July 2025); Envision's release (2 November 2026); Innoscience's interim results (28 August 2026); electrive (28 October 2026); a sponsored trade article (26 October 2026); halbleiter.org material values. The phased framing and the SiC and GaN split are SemiAnalysis's, from the free part of "Inside the 800VDC Revolution, Part 1" (26 May 2026). Personal research, not investment advice.</p>
