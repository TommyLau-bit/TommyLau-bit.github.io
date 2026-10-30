---
title: "The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones"
date: 2026-10-02T12:49:47+08:00
summary: "An AI processor needs power at less than one volt, but it reaches the cabinet at hundreds of volts, and Texas Instruments makes many of the small, cheap chips that step it down safely. It is spending tens of billions of dollars on its own American factories to make them more cheaply than rivals who rent factory space."
category: "Analysis"
cover: "/covers/ti-feeds-the-chip.svg"
tags: ["power", "data-centres", "800VDC"]
draft: false
---

Here is a fact about AI processors that rarely makes the news. The chip that costs tens of thousands of dollars cannot run on the electricity delivered to it.

Inside an AI cabinet, power runs at 54 volts today, and at 800 volts in the designs coming next. The processor's core runs at less than one volt.

Bridging that gap falls to a crowd of small chips around the processor. Texas Instruments, still best known for calculators, makes many of them.

The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Water arrives from the street main at a pressure that would blast a glass out of your hand, so a valve near the meter steps it down. Now imagine a tap that wants a gentle trickle, but a huge volume of it, with the pressure never wobbling.</p>
<p>One valve by the front door cannot do that. You need a row of small, cheap valves right under the sink.</p>
</details>

## Why the last centimetre is the hard part

An AI processor runs at very low voltage but draws enormous power. That means a very large current, and large currents heat copper and waste energy.

So power travels at high voltage for as long as possible, then steps down at the last moment, as close to the processor as the board allows. The job falls to analog chips, which handle real quantities such as voltage and current rather than doing sums. Power stages, small chips that switch very fast, share the load around each processor.

Protection chips sit beside them. An eFuse, an electronic fuse, cuts power in an instant if something shorts.

Most chip companies rent factory space. TI went the other way and is building its own American factories, all on 300 millimetre wafers, the silicon discs chips are cut from. A 300mm wafer has about 2.25 times the area of the older 200mm size, so each pass yields more than twice the chips. TI says that makes a chip about 40 per cent cheaper, before packaging. That is a big edge for a product that sells for cents and competes on price.

## What TI's own results show

If AI is pulling on these chips, data centres should be growing much faster than the rest of TI.

They are, from a small base. Data centres were under a tenth of TI's sales in 2025, but TI said in July 2026 that its data centre sales had doubled in a year. That makes it the fastest-growing market TI reports.

This is a small slice of a large analog business, not an AI company. The factories are built. Now they have to fill.

## What would prove me wrong

I am wrong if racks stay at 54 volts for years. I am also wrong if rivals such as Infineon and Monolithic Power hold the demanding high end, where parts are won on design rather than cost.

And the factory bet can backfire. If industrial and car demand weakens while data centres stay small, TI's new 300mm lines run part-empty.

<section class="exposure">
<h3>Who is exposed if power at the chip runs through cheap analog parts</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures are Texas Instruments' own disclosures, used as evidence for the mechanism.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Texas Instruments</span> makes analog and embedded chips, including power stages and eFuses for AI servers.</dd>
<dt>The power chip rivals</dt>
<dd><span class="names">Infineon</span>, <span class="names">Monolithic Power</span>, <span class="names">Analog Devices</span>, <span class="names">Renesas</span> and <span class="names">onsemi</span> make server power chips. <span class="names">Navitas</span> and <span class="names">Innoscience</span> make gallium nitride ones.</dd>
<dt>The systems and the architect</dt>
<dd><span class="names">Delta</span>, <span class="names">Vertiv</span> and <span class="names">Eaton</span> make rack power systems. <span class="names">Nvidia</span> makes the processors and sets the 800 volt design.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Rack designs built on many conversion steps and heavy low-voltage copper, and chip makers renting older factory space for analog parts.</dd>
</dl>
</section>

---

<p class="sources">Sources: Texas Instruments second quarter 2026 results and earnings call, 22 July 2026, its 2025 annual report and Form 10-K, and its announcements of 18 June 2025 and 16 March 2026. Personal research, not investment advice.</p>
