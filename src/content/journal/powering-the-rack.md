---
title: "Powering the rack: 800 volts reaches the AI rack before it reaches the building"
date: 2026-08-07
summary: "An AI rack now draws so much power that the copper and power supplies wired for it would crowd out the computers, so the industry is moving it from 54 volts to 800. The building around it cannot change as fast, so on Nvidia's own dates the new voltage arrives first as a cabinet beside the rack, fed from the old power room. That order means more power gear in every megawatt until halls run on 800 volts from the grid in."
category: "Analysis"
cover: "/covers/powering-the-rack.svg"
tags: ["power", "data-centres", "800VDC"]
draft: false
---

Nvidia has done something unusual for a company with a product to sell. It has written down why its own design cannot go on. A rack of its AI chips, wired the way racks are wired today, would need up to 200 kilograms of copper bar to carry one megawatt.

Its power supplies would fill up to 64 of the rack's slots. That leaves, in Nvidia's words, no room for the computers the rack exists to hold.

The fix is a higher voltage, and the industry is moving the rack from 54 volts to 800. But the building around the rack cannot change at the same pace. So 800 volts reaches the rack before it reaches the building, and that order decides what gets bought while the building waits.

The physics is simple. For the same power, a lower voltage needs more current, and more current needs thicker copper and wastes more as heat. A megawatt at today's rack voltage is about 18,500 amps. At 800 volts it is about 1,250, a fifteenth as much.

The building is the slow part. Its power room is designed years ahead and runs for decades. Transformers step the grid's high voltage down, a large battery system called a UPS rides through dips, and cables carry alternating current out to the racks. Rebuilding all of that for racks that change with each chip generation is slow and costly.

So the change starts beside the computers. The first product is a power rack: a cabinet of converters that stands next to the computer racks, takes alternating current from the old power room and feeds them 800 volts. Nvidia dates it to the second half of 2026, and a unit serving a whole row of racks to 2027. The step that turns a whole building over to 800 volts it describes, but does not date.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A house was wired for a kettle and a few lamps. Add a heat pump, an oven and a car charger, and the fuse box, the cables and the sockets all have to grow.</p>
<p>A thicker supply cable is the lasting fix, but the walls are already plastered. So the new supply runs along the outside first, beside the old one, and the full rewire comes later.</p>
</details>

Rack first means more gear, not less. The old power room stays, and the power racks are added to it. Vertiv, which sells power and cooling equipment for data centres, estimates it can now sell about US$3.25 million to 3.75 million of gear into each megawatt, up by a tenth or more on its earlier range.

The chips nearest the processor are selling faster too, before 800 volts has arrived. For anyone building or supplying an AI hall, the new voltage is coming as an extra cabinet beside the rack, not as a new building.

<hr class="layer">
<p class="layer-label">For investors</p>

<a id="the-rack-runs-out-of-copper"></a>

## The rack has outgrown the wiring it was born with

Rack power has risen tenfold within one wiring design, and the next step is tenfold again. Google says the 48 volt rack architecture it pushed through the industry scaled from 10 kW racks to 100 kW. Vertiv's reference design for Nvidia's GB200 NVL72 runs up to 132 kW per rack.

The next racks go far past that. Nvidia's Kyber rack is to house 576 Rubin Ultra GPUs by 2027, at around a megawatt. Google expects machine learning to need more than 500 kW per rack before 2030.

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

Nvidia made the case against its own wiring in May 2025. Above 200 kW, it wrote, racks start "to hit physical limits". A 1 MW rack at 54 volts would need up to 200 kg of copper busbar, and up to 200,000 kg across a gigawatt site. Its power shelves "would consume up to 64 U of rack space for Kyber at MW scale", leaving no room for compute.

Google reached the same answer by its own road. It calls for ±400 VDC, 800 volts pole to pole, to take racks "from 100 kilowatts up to 1 megawatt". That is why the claim below counts ±400 VDC as 800 volts.

## Only a higher voltage shrinks the copper

Current, not power, sets the size of the copper, so the only lasting fix is to raise the voltage. Power is voltage times current. Hold the power at a megawatt and the current falls fifteenfold between 54 volts and 800.

<figure class="chart">
<p class="chart-title">At 800 volts, a megawatt needs a fifteenth of the current</p>
<p class="chart-sub">Current needed to deliver one megawatt, in amps</p>
<svg viewBox="0 0 560 130" role="img" aria-label="Bar chart. Delivering one megawatt at 54 volts takes about 18,500 amps. At 800 volts it takes about 1,250 amps, about a fifteenth as much.">
<g class="c-axis"><text x="100" y="43" text-anchor="end">54 V today</text><text x="100" y="99" text-anchor="end">800 V</text></g>
<rect class="c-bar c-mute" x="110" y="24" width="270.0" height="30" rx="2"/>
<text class="c-lab c-s2t" x="390" y="44">about 18,500 amps</text>
<rect class="c-bar" x="110" y="80" width="18.2" height="30" rx="2"/>
<text class="c-lab c-s2t" x="138.2" y="100">about 1,250 amps</text>
<line class="c-base" x1="110" y1="14" x2="110" y2="120"/>
</svg>
<figcaption>Physics: current equals power divided by voltage, so 1,000,000 W over 54 V is 18,519 A and over 800 V is 1,250 A. Real systems add losses and safety margins.</figcaption>
</figure>

Nvidia puts the gain in its own terms. Moving the row from 415 volts AC to 800 volts DC carries 85% more power through the same conductor size and cuts copper by 45%, its May 2025 post says. Its October 2025 post gives 157% more power through the same wire gauge. The two measures differ, so I quote both.

Fewer conversions also waste less. Nvidia says today's AC path, end to end, "can be less than 90%" efficient, and claims up to 5% better efficiency for 800 VDC against 54 volt systems.

Less copper per unit of power does not mean less copper, though. Power per rack is rising faster than the saving, so the 800 volt move changes the copper's specification, not its direction.

## The building cannot move as fast as the rack

The rack can change every product cycle; the building cannot, so the conversion moves outward in phases. Today alternating current runs all the way to the rack, and a power shelf inside it makes 54 volts. In the first phase the power room stays as it is, and a power rack beside the computers makes 800 volts. Only in the last does the building itself turn grid power straight into 800 volts.

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

Each phase also decides which chip material does the switching. The phased framing and this split are SemiAnalysis's, from the free part of its "Inside the 800VDC Revolution, Part 1" (26 May 2026); the makers' own releases place them.

Silicon carbide, SiC, belongs at the top, where voltages run to kilovolts. Infineon and SolarEdge are developing a 2 to 5 MW solid-state transformer block on Infineon's SiC switches, converting medium voltage straight to 800 to 1,500 volts DC.

Gallium nitride, GaN, belongs at or below the bus, and takes 800 volts by stacking parts rated at 650. Navitas's board shown at GTC in March 2026 steps 800 volts to 6 on sixteen of them. Texas Instruments' own 800 to 6 volt converter uses GaN at 97.6% peak efficiency. That silicon still holds the last step, below one volt, is my reading, not a figure I have sourced.

So a rack-first transition pulls GaN and tray-level converters forward, and leaves SiC for solid-state transformers until buildings follow.

## Nvidia dates the rack and the row, but not the building

The strongest evidence is Nvidia's own calendar, and it puts the rack first. In May 2025 it said 800 VDC targets "1 MW IT racks and beyond, starting in 2027", in step with Kyber. In October 2025 it said the move "will occur in phases".

Then, on 11 August 2026, it gave the phases dates. The 800 VDC power rack arrives "in the second half of 2026". A row power centre of up to 2 MW per row is expected in 2027. The DC power block that converts medium voltage for a whole hall is described, but carries no date.

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

The rest of the record points the same way. The solid-state transformer specification Nvidia cites had reached only version 0.3 by July 2026. More than 80 manufacturers are building to the 800 VDC specification, and Nvidia, Google and Microsoft published a joint white paper in March 2026. The ecosystem is real; the building-wide step is simply last in line.

This is not what I first expected. My research note of 17 September, which is not on this site, led with the building design, grid power converted straight to 800 volts at the perimeter. It treated a power rack beside each compute rack as the downside case, a sign the move would stall and stay partial. Nvidia has since made that cabinet its first product, so it is phase one, not the failure mode. I changed my view of the order, not of the direction.

<a id="every-megawatt-got-harder"></a>

## Rack first puts more gear in every megawatt

A rack-first transition adds equipment before it removes any, because the AC room stays and the power racks join it. The end state removes AC power shelves and much UPS conversion, and adds rectifiers, DC busway, power racks and storage on the DC line. In between, a hall carries parts of both.

Vertiv is the one maker to put a figure on what a megawatt holds. Its management estimated in May 2026 that it could sell about US$3.25 million to 3.75 million of power and cooling gear into each megawatt of IT power, up about 10 to 15% on its earlier range. That is an estimate of opportunity, not reported revenue.

Its results show demand, not yet the cause. In the third quarter of 2026 Vertiv's sales grew 55.0% organically and its adjusted operating margin widened 2.9 points to 25.2%, with organic orders more than doubling. A margin widening on that much volume fits operating leverage as well as richer gear, so it cannot separate the two. Vertiv says its own 800 VDC range, from central rectifiers to rack converters, is scheduled for the second half of 2026.

<a id="ti-feeds-the-chip"></a>

## The last centimetre is growing before 800 volts arrives

At the other end of the chain, the chips beside the processor are already selling faster, and density, not voltage, is doing it so far. Texas Instruments makes the power stages, converters and electronic fuses on the board, and at GTC in March 2026 it showed a full 800 volt set, from a 30 kW supply to the stage below one volt.

Its data centre business was 9% of revenue in 2025, about US$1.5bn. It doubled in the second quarter of 2026 and grew about 95% in the third, to about 13% of revenue, in management's words on the call. But racks shipping in volume today run at 48 and 54 volts, and TI said in July that 800 volts will be phased in.

TI names both drivers: "When there is more power density, there is more opportunity for TI," and "When there is higher voltages, more opportunity for TI." So far the first one is paying. The second arrives with the power racks.

## What could bring the building forward

The case against is real. Nvidia said in May 2025 that full-scale production would coincide with Kyber in 2027. Foxconn's 40 MW Kaohsiung-1 site is being built for 800 VDC. CoreWeave, Lambda, Nebius, Oracle Cloud Infrastructure and Together AI are "designing for" 800 volt data centres. Vertiv's range includes central rectifiers, and Infineon's SiC transformer block is in development. A hall fed from the building could open before 2028.

Each of these is a design, not a running hall. Nvidia's own calendar dates the rack and the row and leaves the building open, and the transformer specification is still at version 0.3. Foxconn's site is the one to watch: if it opens on a central rectifier, the building did not wait for the rack, and the claim below breaks.

Until then, the rack's new voltage arrives the way the house's new supply does. It runs along the outside first, in a cabinet beside the rack, fed from a power room built for the old one. The full rewire, from the grid in, comes later, and every year it waits is a year a megawatt carries both.

## Claims on record

The test this piece stands behind, quoted word for word from the claims page:

<a id="powering-the-rack"></a>

**Powering the rack** (30 October 2026)

Claim: "800 volts reaches the AI rack before it reaches the building: until 2028, 800 VDC enters data halls through power racks and row power centres fed from AC power rooms, and no data hall of 10 MW or more goes into service fed by a facility-level rectifier or solid-state transformer. 800 VDC here includes ±400 VDC, 800 V pole to pole."

Breaks if: "Before 1 January 2028, Nvidia, a data centre operator or its equipment supplier states that a data hall of 10 MW or more is in service with 800 VDC distributed from a facility-level rectifier or solid-state transformer, rather than from power racks or row power centres fed by AC. 800 VDC includes ±400 VDC, 800 V pole to pole."

<details class="claims-earlier">
<summary>Two earlier claims on the rack's power, quoted word for word</summary>

**Vertiv is paid per megawatt, and AI has made every megawatt harder to build** (25 September 2026)

Claim: "What Vertiv sells per megawatt is rising, because AI makes every megawatt harder to power and cool."

Breaks if: "Vertiv's growth only ever tracks the megawatts being built, or its margin shrinks while orders stay strong, or the biggest buyers take cooling in-house."

Where later evidence bears on it: I was wrong. The piece said service revenue grew faster than product sales. Those were reported figures, swollen by acquisitions. Organically, services and spares grew 18.1% in the third quarter of 2026 against 63.6% for products, so that evidence fell away, as the Vertiv note said on 6 October. The margin limb has not broken: 25.2%, up 2.9 points, with orders more than doubling. But that margin fits operating leverage as well as richer content. The claim now rests on Vertiv's own per-MW estimate, up about 10 to 15%. The in-house limb is partly met, and was from the start: Google's own blog (30 April 2025) says it has liquid-cooled its TPUs since 2018 "at GigaWatt scale". So at least one of the biggest buyers already designs its own cooling, which the September piece did not weigh.

**The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones** (2 October 2026)

Claim: "The move to 800 volt racks turns Texas Instruments' small, cheap power chips into a growing data centre business."

Breaks if: "Racks stay at 54 volts for years, or rivals hold the demanding high end, or TI's new 300mm lines run part-empty as industrial and car demand weakens."

Where later evidence bears on it: the growing data centre business is here, about 13% of revenue in the third quarter of 2026. But it grew before 800 V racks ship in volume, so the cause the claim names is not yet shown. TI names power density and higher voltages together, so the growth so far cannot be pinned on 800 V. Nvidia dates its own 800 V power rack to the second half of 2026, so the first limb cannot be tested before 2027. Industrial grew more than 40%, so the part-empty limb is not near.

</details>

## What would prove me wrong

The test is a named hall. If Foxconn's Kaohsiung-1, or any hall of 10 MW or more, goes into service before 2028 fed by a central rectifier or solid-state transformer, the building did not wait for the rack.

That would matter beyond timing. A building-first switch would pull SiC demand for solid-state transformers forward and shrink the UPS sooner. A rack-first switch adds power racks while the AC room stays, which is more gear per megawatt, not less.

## Research notes

[Vertiv](/research/vertiv/) and [Texas Instruments](/research/texas-instruments/), each resting on its live claim above. Both notes already record where the September and October pieces were wrong.

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

Correction to the August piece: it put today's flagship racks "near 200 kilowatts". That was loose. Vertiv's GB200 NVL72 design is up to 132 kW per rack; 200 kW is where Nvidia says 54 V starts to fail.

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

<p class="sources">Sources: Nvidia Technical Blog and Nvidia blog posts of 20 May 2025, 13 October 2025 and 11 August 2026; Google Cloud blog on 1 MW racks and liquid cooling (30 April 2025); Vertiv releases of 15 October 2024 and 19 May 2025, its 2026 Investor Conference presentation (19 May 2026), and its third quarter 2026 results on Form 8-K (28 October 2026); Texas Instruments' Form 10-K for 2025, its release of 16 March 2026, its third quarter 2026 results (21 October 2026) and its earnings calls of 27 January, 22 July and 21 October 2026; Infineon releases of May and 5 November 2025; Navitas releases of October 2025 and March 2026. The phased framing of the 800 VDC transition and the SiC and GaN split are SemiAnalysis's, from the free part of "Inside the 800VDC Revolution, Part 1" (26 May 2026). Personal research, not investment advice.</p>
