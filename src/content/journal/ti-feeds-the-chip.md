---
title: "The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones"
date: 2026-10-02T12:49:47+08:00
summary: "An AI processor needs electricity at less than one volt, but power reaches the cabinet at hundreds of volts. Texas Instruments makes many of the small, cheap chips that step it down and keep it safe on the way. It is spending tens of billions of dollars on its own American factories to make those chips more cheaply than anyone who rents factory space."
category: "Analysis"
cover: "/covers/ti-feeds-the-chip.svg"
tags: ["power", "data-centres", "800VDC"]
draft: false
---

Here is a fact about AI processors that rarely makes the news. The chip that costs tens of thousands of dollars cannot run on the electricity delivered to it.

Inside an AI cabinet, power runs at 54 volts today, and at 800 volts in the designs coming next. The processor's core runs at less than one volt.

Bridging that gap, safely and with almost nothing lost as heat, falls to a crowd of small chips around the processor. Texas Instruments, the company most people still know for calculators, makes many of them. Some sell for cents.

The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of the water coming into your house from the street main. It arrives at a pressure that would blast a glass out of your hand, so a small valve near the meter steps it down before it reaches any tap.</p>
<p>Now imagine a tap that wants a gentle trickle, but a huge volume of it, all at once, and with the pressure never wobbling. You cannot do that with one valve by the front door. You need a row of small valves right under the sink.</p>
<p>The AI processor is that tap. The valves under the sink are cheap, and nobody photographs them. But without them the most expensive thing in the house does not work.</p>
</details>

## Three words you need

**Analog chip.** A chip that handles real-world quantities such as voltage, current and temperature, rather than doing sums. Most of TI's sales come from analog chips, and many of them manage power.

**Power stage.** A small chip that switches on and off very fast to step a voltage down. Several work together around one processor, each carrying a share of the load.

**300mm wafer.** A wafer is the thin silicon disc that chips are made on before it is cut up. A 300 millimetre wafer has about 2.25 times the area of the older 200mm size, so each pass through the factory yields more than twice as many chips.

## Why the last centimetre is the hard part

An AI processor runs at very low voltage but draws enormous power. Low voltage and high power together mean a very large current, and large currents heat copper and waste energy.

So power has to travel at high voltage for as long as possible, then step down at the last moment, as close to the processor as the board allows. That logic is why the industry is moving the whole rack to the higher voltage.

TI says a one megawatt rack fed at today's low voltage would need hundreds of pounds of copper. Earlier this year, at Nvidia's developer conference, it showed a complete set of parts for the new design, stepping power down in only two stages.

Every step loses a little energy as heat, and the cooling system then has to remove that heat too. So a converter that wastes even a sliver less pays twice, in electricity and in cooling.

Around those converters sit protection chips. An eFuse, an electronic fuse, cuts the power in an instant if something shorts. A hot-swap controller lets an engineer pull out a live tray without crashing the whole rack.

## The factory bet

The second half of the story is where those chips are made. Most chip companies now design their products and rent factory space from someone else. TI went the other way and decided to own almost every step.

In June 2025 TI announced plans to invest more than $60 billion in seven American chip factories in Texas and Utah. The largest site is Sherman, Texas, where the first factory began production at the end of that year.

Every wafer Sherman runs is 300mm. TI says a chip made on the larger wafer costs about 40 per cent less than one made on the older size, before it is packaged.

That is a big edge for a product that sells for cents and competes on price. TI wants nearly all its wafers made in its own factories by the end of the decade, most of them on the larger size.

## What TI's own results show

If AI is pulling on these chips, data centres should be growing much faster than the rest of TI.

They are, from a small base. Data centres were under a tenth of TI's sales in 2025, far behind its industrial and car customers. But TI said in July 2026 that its data centre sales had doubled in a year. That makes it the fastest-growing market TI reports.

So this is a small slice of a large analog business, not an AI company. What makes it interesting is the timing. TI says its long cycle of heavy factory building is nearly over. The factories are built. Now they have to fill.

TI's gross margin, the share of each sale left after the cost of making it, is the place to watch that happen. Full factories make cheap chips profitable. Empty ones do the opposite.

## What would prove me wrong

I am wrong if racks stay at 54 volts for years. TI itself says the new design will be phased in. If it is adopted slowly, TI is one of many suppliers of a mature product rather than an early mover in a new one.

I am also wrong if rivals hold the demanding high end. Infineon, Monolithic Power, Analog Devices and others make the same kinds of chips, and the processor makers choose. Cheap factories help most on simple parts. The newest parts are won on design.

And the factory bet can backfire. TI built ahead of demand. If industrial and car demand weakens while data centres stay small, the new 300mm lines run part-empty, and a cost advantage becomes a cost burden.

So I watch whether data centres keep growing as a share of TI's sales. I watch whether named operators commit to 800 volt racks. And I watch whether gross margin holds as the new Sherman capacity comes online.

<section class="exposure">
<h3>Who is exposed if power at the chip runs through cheap analog parts</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are Texas Instruments' own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Texas Instruments</span> makes analog and embedded chips, including power stages, bus converters, eFuses and hot-swap controllers for AI servers, mostly in its own 300mm factories.</dd>
<dt>The power chip rivals</dt>
<dd><span class="names">Infineon</span>, <span class="names">Monolithic Power</span>, <span class="names">Analog Devices</span>, <span class="names">Renesas</span> and <span class="names">onsemi</span> make power management chips and power stages for servers.</dd>
<dt>The gallium nitride specialists</dt>
<dd><span class="names">Navitas</span> and <span class="names">Innoscience</span> make gallium nitride switching chips used in high-voltage power conversion.</dd>
<dt>The power systems builders</dt>
<dd><span class="names">Delta</span>, <span class="names">Vertiv</span> and <span class="names">Eaton</span> make the power supplies and rack power systems these chips go into.</dd>
<dt>The architect</dt>
<dd><span class="names">Nvidia</span> makes the AI processors and sets the 800 volt rack design its suppliers build to.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Power designs built around many conversion steps and heavy low-voltage copper inside the rack. And chip makers that rent older factory space for analog parts, wherever TI's 300mm cost holds.</dd>
</dl>
</section>

---

<p class="sources">Sources: Texas Instruments second quarter 2026 results and earnings call, 22 July 2026, for data centre growth, gross margin, capital spending and 800 volt timing. Texas Instruments annual report and Form 10-K for 2025 for revenue by end market, 300mm cost and the 2030 manufacturing goal. Texas Instruments announcements of 18 June 2025 on the $60 billion investment, 17 December 2025 on Sherman production, 23 May 2025 on copper in a one megawatt rack, and 16 March 2026 on its 800 volt power design. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
