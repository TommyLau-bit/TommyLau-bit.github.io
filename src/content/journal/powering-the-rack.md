---
title: "Powering the rack: from 54 volts to 800, and the gear each megawatt now needs"
date: 2026-10-30T14:20:52+08:00
summary: "An AI rack now draws so much power that the copper and power supplies inside it would crowd out the computers. So the industry is moving the rack from 54 volts to 800. Vertiv sells the power equipment in the building and Texas Instruments makes the small chips beside the processor, and both sell more into each megawatt as rack power climbs. The new voltage reaches the rack years before it reaches the whole building."
category: "Analysis"
cover: "/covers/powering-the-rack.svg"
tags: ["power", "data-centres", "800VDC"]
draft: false
---

Nvidia says a one megawatt rack, wired the way AI racks are wired today, would need up to 200 kilograms of copper bar. Its power supplies would take up to 64 of the rack's slots, which Nvidia says leaves no room for computing.

So the industry is moving the rack from 54 volts to 800.

Vertiv sells the power equipment in the building. Texas Instruments makes small chips beside the processor. Both sell more into each rack as its power climbs.

The rack has outgrown its wiring, and 800 volts reaches the rack years before it reaches the building.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A house was wired for a kettle and a few lamps. Add a heat pump, an oven and a car charger, and the fuse box, the cables and the sockets all have to grow.</p>
<p>A thicker supply cable is the lasting fix, but the walls are already plastered. So the new supply runs along the outside first, beside the old one, and the full rewire comes years later.</p>
</details>

## How it works

Power reaches an AI chip in steps. The grid delivers it at high voltage. A transformer steps it down, a large battery system called a UPS, an uninterruptible power supply, guards against dips, and power supplies in the rack turn it into low-voltage direct current. Small chips beside the processor take it below one volt.

The trouble is current. For the same power, lower voltage means more current, and more current needs thicker copper and wastes more as heat. A megawatt at today's rack voltage is about 18,500 amps. At 800 volts it is about 1,250.

So the fix is to carry power at high voltage as far as possible and step it down only at the end.

Supply cannot simply switch over. A building's power room is designed years ahead and runs for decades. So the change comes in phases: first a cabinet of power converters beside the computers, then a converter for each row, and only later the whole building.

Two newer chip materials do the switching. Silicon carbide, SiC, handles the highest voltages near the grid. Gallium nitride, GaN, switches faster at lower voltages, closer to the processor.

## The number that matters

Vertiv estimates that each megawatt of computing power in a data centre now holds about US$3.25 million to 3.75 million of the kind of equipment it sells. That was its own management estimate in May 2026, up about 10 to 15% on its earlier range.

To the grid, a megawatt is a megawatt. Inside the building, each one now carries more gear, because the rack draws so much more.

The new voltage moves where that gear sits. Nvidia's own power rack is due in the second half of 2026, and its row-level unit is expected in 2027.

<hr class="layer">
<p class="layer-label">For investors</p>

## The mechanism in depth

Every watt an AI chip uses passes through the same chain of conversions. Each step loses a little energy and needs its own equipment, and each is made by a different set of firms.

| Step | Today, AC to the rack | 800 VDC end state | Switching material | Who makes it |
|---|---|---|---|---|
| Grid to building | Medium voltage, for example 13.8 kV or 35 kV AC, stepped down by a transformer to 415 or 480 VAC | Medium voltage AC converted straight to 800 VDC at the edge of the building, by a rectifier or a solid-state transformer | SiC in solid-state transformers | Hitachi Energy, GE Vernova, ABB, Siemens, Schneider Electric, Eaton, Vertiv |
| Backup | UPS converts AC to DC and back again | Capacitors beside the racks; batteries at the grid connection | Not stated | Vertiv, Schneider Electric, Eaton |
| Room to rack | 415 or 480 VAC on busway | 800 VDC on two-conductor busway | None, it is copper | Vertiv, Schneider Electric, Eaton |
| Rack to tray | Power shelves turn 415 VAC into 54 VDC on a copper busbar | 800 VDC enters the tray directly | Varies by design | Delta, LiteOn, Flex, Megmeet |
| Tray to board | 54 V to 12 V | One converter steps 800 V to 12 V at 64 to 1, or 800 V to 6 V | GaN, low-voltage on today's 54 V step; high-voltage at 800 V | Navitas, Innoscience, Infineon, TI |
| Board to chip | 12 V to below 1 V | 12 V or 6 V to below 1 V | Power stages, many per processor | TI, Monolithic Power, Infineon, Renesas, Analog Devices |

The voltages and steps are Nvidia's (20 May and 13 October 2025). The 800 V to 6 V step is Texas Instruments' design (16 March 2026). Nvidia's October 2025 post says end-to-end efficiency on today's AC path "can be less than 90%". Its May 2025 post claims up to 5% better efficiency for 800 VDC against today's 54 V systems.

The phased framing and the SiC and GaN split are SemiAnalysis's, from the free part of "Inside the 800VDC Revolution, Part 1" (26 May 2026). Where they sit, on the makers' own statements:

- **SiC belongs at the top of the chain.** Infineon and SolarEdge are developing a 2 to 5 MW solid-state transformer block on Infineon's SiC switches, converting 13.8 to 34.5 kV straight to 800 to 1,500 V DC (5 November 2025). Navitas sells SiC from 650 V to 6,500 V.
- **GaN belongs at or below the bus.** Navitas's high-voltage GaN parts are rated at 650 V, below the 800 V bus, so they take 800 V by stacking. Its GTC board (March 2026) steps 800 V to 6 V on 16 of its 650 V GaN switches in a stacked full bridge, with 25 V silicon switches on the output side. TI's own 800 V to 6 V converter uses integrated GaN power stages at 97.6% peak efficiency (16 March 2026). Navitas's 100 V GaN is "optimised for the lower-voltage DC-DC stages on GPU power boards" (October 2025).
- **The last step is power stages.** TI's release names no material for its 6 V to below 1 V stage. That silicon still holds it is my reading, not a figure I have sourced.

So the honest split is SiC on the grid side, where voltages run into kilovolts, and GaN at or below the 800 V bus, stacked to take the bus and switching fast near the chip, with silicon on the low-voltage side. Infineon sells all three materials and expects the share of power semiconductors in an 800 VDC design to be similar to or higher than in today's AC one (May 2025).

## 800 VDC timing: what Nvidia itself has said

Timing is contested in press reports, which I leave aside. Nvidia's own dated statements are these.

| Date | Nvidia's statement | Source |
|---|---|---|
| 20 May 2025 | 800 VDC targets "1 MW IT racks and beyond, starting in 2027"; full-scale production "will coincide with NVIDIA Kyber rack-scale systems in 2027" | Nvidia Technical Blog |
| 13 October 2025 | Kyber will house "576 NVIDIA Rubin Ultra GPUs by 2027"; the move "will occur in phases" | Nvidia blog and Technical Blog |
| March 2026 | Nvidia, Google and Microsoft publish a joint 800 VDC white paper through the Open Compute Project | Nvidia blog, 11 August 2026 |
| 11 August 2026 | The 800 VDC power rack arrives "in the second half of 2026"; a row power centre of up to 2 MW per row is expected in 2027; the DC power block for direct medium-voltage conversion is described but not dated | Nvidia blog |

The August post dates the power gear, not Kyber, and it says more than 80 manufacturers are building to the specification. The building-wide step, a facility rectifier or solid-state transformer feeding a whole hall, is the one Nvidia's own posts do not date. The solid-state transformer specification Nvidia cites reached only version 0.3, in July 2026.

That ordering is my reading of the evidence: the rack converts first, from an AC room, and the building follows.

It reverses my September note. That note led with the building design, 13.8 kV converted straight to 800 VDC at the perimeter, and treated a rack of power supplies beside each compute rack as the downside case. Nvidia has since made that power rack its first product, so the sidecar is the first phase, not the failure mode. The note also counted about thirty vendors; Nvidia now counts more than 80.

## Content per megawatt

A megawatt of AI capacity holds more power and cooling gear than a megawatt of ordinary servers. Vertiv is the one maker in this cluster to put a dollar figure on it in its own materials.

| Measure | Figure | Source |
|---|---|---|
| Vertiv's data centre opportunity per MW of IT power | About US$3.25 million to 3.75 million | Vertiv 2026 Investor Conference, 19 May 2026, management estimate |
| Change against Vertiv's prior range | Up about 10 to 15% | Same |
| Vertiv's GB200 NVL72 reference design | Up to 132 kW per rack, 7 MW in all | Vertiv, 15 October 2024 |

The per-MW figure is an estimate of what Vertiv could sell into a megawatt, across power and cooling, not a reported revenue figure. Vertiv does not state its prior range on that slide. I found no per-MW figure in Eaton's or Schneider Electric's own filings that I could open, so they are not in the table.

The 800 V move does not obviously shrink this content. It removes AC power shelves and much UPS conversion, and adds rectifiers, DC busway, power racks and storage on the DC line.

<a id="the-rack-runs-out-of-copper"></a>
## The copper limit: what Nvidia put in writing

Nvidia made the case against its own current design. In its May 2025 post, racks start "to hit physical limits" above 200 kW. A 1 MW rack at 54 V would need up to 200 kg of copper busbar, and up to 200,000 kg across a 1 GW site. Power shelves "would consume up to 64 U of rack space for Kyber at MW scale", leaving no room for compute, in Nvidia's framing.

Moving the row from 415 VAC to 800 VDC carries 85% more power through the same conductor size and cuts copper by 45%, the same post says. Nvidia's October 2025 post puts it as 157% more power through the same wire gauge. The two measures differ, so I quote both.

My August piece put today's flagship racks "near 200 kilowatts". That was loose. Vertiv's GB200 NVL72 design is up to 132 kW per rack; 200 kW is where Nvidia says 54 V starts to fail.

Less copper per unit of power does not mean less copper. Power per rack is rising faster than the saving, so the 800 V move changes the copper's specification, not its direction.

Who is building for it is still mostly vendors. In October 2025 Nvidia named Foxconn's 40 MW Kaohsiung-1 site as being built for 800 VDC, and CoreWeave, Lambda, Nebius, Oracle Cloud Infrastructure and Together AI as "designing for" 800 V data centres. Designing is not running.

<a id="every-megawatt-got-harder"></a>
## Vertiv: more gear in every megawatt

Vertiv makes UPS systems, switchgear, busway, rack power and liquid cooling, and services them. It is in Nvidia's power systems group for 800 VDC, unveiled an 800 VDC reference architecture in October 2025, and says its 800 VDC portfolio, from central rectifiers to rack converters, is scheduled for the second half of 2026 (19 May 2025).

Its third quarter of 2026, released on 28 October 2026, tests the claim.

| Quarter | Net sales | Products, organic growth | Services and spares, organic growth | Adjusted operating margin |
|---|---|---|---|---|
| Q3 2026 | US$4.31bn, 55.0% organic growth | 63.6% | 18.1% | 25.2%, up 2.9 points |

Adjusted operating margin is the share of each sale left after running costs, with one-off items stripped out. Organic growth strips out acquisitions and currency. Vertiv said organic orders grew more than 100% in the third quarter, and raised its full-year guide to US$14.45 to 14.85 billion of sales at a 23.5 to 24.5% adjusted margin.

The margin keeps widening. But a margin widening on 55% organic growth fits operating leverage on volume as well as richer gear per megawatt, so it cannot by itself separate the two. Vertiv's own per-MW estimate points the claim's way, and it is an estimate.

**The margin shows a business stretched by demand. On its own, it cannot show that each megawatt holds more.**

<a id="ti-feeds-the-chip"></a>
## Texas Instruments: the last centimetre

TI works at the bottom of the chain, from the tray's input down to the processor. It makes power stages, converters, electronic fuses and hot-swap controllers, which let a live tray be pulled without crashing the rack. At GTC on 16 March 2026 it showed a full 800 V set: a 30 kW AC to 800 V supply, an 800 V hot-swap controller, the GaN 800 V to 6 V converter and a 6 V to below 1 V stage.

| Measure | Figure | Source |
|---|---|---|
| Data centre share of revenue, 2025 | 9%, about US$1.5bn | TI Form 10-K for 2025; call of 27 January 2026 |
| Data centre growth, Q2 2026 | Doubled on a year earlier | TI call, 22 July 2026 |
| Data centre growth, Q3 2026 | About 95% on a year earlier, about 13% of revenue | TI management on the call, 21 October 2026, per transcript |
| Total revenue, Q3 2026 | US$6.06bn, up 28% | TI release, 21 October 2026 |
| Industrial growth, Q3 2026 | More than 40%, its first new peak in four years | TI call, 21 October 2026, per transcript |

The data centre business is real and growing fastest. But racks shipping in volume today run at 48 and 54 V, and TI said in July that the 800 V design will be phased in. So the doubling came before the 800 V move. On the October call TI named both drivers: "When there is more power density, there is more opportunity for TI," and "When there is higher voltages, more opportunity for TI."

**TI is selling more into each rack already; 800 volts is still ahead of its numbers.**

## Claims on record

Each claim is quoted word for word from the claims page, with the date its piece went live.

**Vertiv is paid per megawatt, and AI has made every megawatt harder to build** (25 September 2026)

Claim: "What Vertiv sells per megawatt is rising, because AI makes every megawatt harder to power and cool."

Breaks if: "Vertiv's growth only ever tracks the megawatts being built, or its margin shrinks while orders stay strong, or the biggest buyers take cooling in-house."

Where I was wrong: the piece said service revenue grew faster than product sales. Those were reported figures, swollen by acquisitions. Organically, services and spares grew 18.1% in the third quarter of 2026 against 63.6% for products, so that evidence fell away, as the Vertiv note said on 6 October. The margin limb has not broken: 25.2%, up 2.9 points, with orders more than doubling. But that margin fits operating leverage as well as richer content. The claim now rests on Vertiv's own per-MW estimate, up about 10 to 15%. The in-house limb is partly met, and was from the start: Google's own blog (30 April 2025) says it has liquid-cooled its TPUs since 2018 "at GigaWatt scale". So at least one of the biggest buyers already designs its own cooling, which the September piece did not weigh.

**The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones** (2 October 2026)

Claim: "The move to 800 volt racks turns Texas Instruments' small, cheap power chips into a growing data centre business."

Breaks if: "Racks stay at 54 volts for years, or rivals hold the demanding high end, or TI's new 300mm lines run part-empty as industrial and car demand weakens."

Where later evidence cuts against it: the growing data centre business is here, about 13% of revenue in the third quarter of 2026. But it grew before 800 V racks ship in volume, so the cause the claim names is not yet shown. TI names power density and higher voltages together, so the growth so far cannot be pinned on 800 V. Nvidia dates its own 800 V power rack to the second half of 2026, so the first limb cannot be tested before 2027. Industrial grew more than 40%, so the part-empty limb is not near.

<a id="powering-the-rack"></a>

**New: Powering the rack** (30 October 2026)

Claim: "800 volts reaches the AI rack before it reaches the building: until 2028, 800 VDC enters data halls through power racks and row power centres fed from AC power rooms, and no data hall of 10 MW or more goes into service fed by a facility-level rectifier or solid-state transformer. 800 VDC here includes ±400 VDC, 800 V pole to pole."

Breaks if: "Before 1 January 2028, Nvidia, a data centre operator or its equipment supplier states that a data hall of 10 MW or more is in service with 800 VDC distributed from a facility-level rectifier or solid-state transformer, rather than from power racks or row power centres fed by AC. 800 VDC includes ±400 VDC, 800 V pole to pole."

## What would prove me wrong

The test is a named hall. Nvidia's own posts date the power rack and the row power centre but not the facility block, and the solid-state transformer specification is at version 0.3. If Foxconn's Kaohsiung-1, or any hall of 10 MW or more, goes into service before 2028 on a central rectifier or solid-state transformer, the building did not wait for the rack.

This matters beyond timing. A building-first switch would pull SiC demand for solid-state transformers forward and shrink the UPS sooner. A rack-first switch adds power racks while the AC room stays, which is more gear per megawatt, not less.

## Research notes

[Vertiv](/research/vertiv/) and [Texas Instruments](/research/texas-instruments/), each resting on its live claim above. Both notes already record where the September and October pieces were wrong.

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

<p class="sources">Sources: Nvidia Technical Blog and Nvidia blog posts of 20 May 2025, 13 October 2025 and 11 August 2026; Vertiv releases of 15 October 2024 and 19 May 2025, its 2026 Investor Conference presentation (19 May 2026), and its third quarter 2026 results on Form 8-K (28 October 2026); Texas Instruments' Form 10-K for 2025, its release of 16 March 2026, its third quarter 2026 results (21 October 2026) and its earnings calls of 27 January, 22 July and 21 October 2026; Infineon releases of May and 5 November 2025; Navitas releases of October 2025 and March 2026; Google's blog of 30 April 2025. The phased framing of the 800 VDC transition and the SiC and GaN split are SemiAnalysis's, from the free part of "Inside the 800VDC Revolution, Part 1" (26 May 2026). Personal research, not investment advice.</p>
