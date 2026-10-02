---
title: "The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones"
date: 2026-10-02T12:49:47+08:00
summary: "An AI processor needs electricity at less than one volt, but power reaches the cabinet at hundreds of volts. Texas Instruments makes many of the small, cheap chips that step it down and keep it safe on the way. It is spending tens of billions of dollars on its own American factories to make those chips more cheaply than anyone who rents factory space."
category: "Analysis"
cover: "/covers/ti-feeds-the-chip.svg"
tags: ["power", "data-centres", "800VDC"]
---

Here is a fact about AI processors that rarely makes the news. The chip that costs tens of thousands of dollars cannot run on the electricity delivered to it. Something has to change that electricity first, millimetres away.

Power arrives at an AI cabinet at 54 volts today, and at 800 volts in the designs coming next. The processor's core runs at less than one volt. Bridging that gap, safely and with almost nothing lost as heat, falls to a crowd of small chips around it.

Texas Instruments, the company most people still know for calculators, makes many of them. Some sell for cents. And TI is spending more than $60 billion on American factories to make them more cheaply than its rivals can.

The most expensive chip in an AI rack runs on Texas Instruments' cheapest ones.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of the water coming into your house from the street main. It arrives at a pressure that would blast a glass out of your hand, so a small valve near the meter steps it down before it reaches any tap.</p>
<p>Now imagine a tap that wants a gentle trickle, but a huge volume of it, all at once, and with the pressure never wobbling. You cannot do that with one valve by the front door. You need a row of small valves right under the sink.</p>
<p>The AI processor is that tap. The valves under the sink are cheap, and nobody photographs them. But without them the most expensive thing in the house does not work.</p>
</details>

## Three words you need

**Analog chip.** A chip that handles real-world quantities such as voltage, current and temperature, rather than doing calculations. Most of TI's revenue comes from analog chips, and many of them manage power.

**Power stage.** A small chip that switches on and off very fast to step a voltage down. Several work together around one processor, each carrying a share of the current.

**300mm wafer.** A wafer is the thin silicon disc chips are made on, before it is cut up. A 300 millimetre wafer has about 2.25 times the area of the older 200mm size, so each pass through the factory yields more than twice as many chips.

## Why the last centimetre is the hard part

An AI processor's core runs at below one volt but draws enormous power. Low voltage and high power together mean very high current, and high current is what turns copper hot and wastes energy.

So the power has to be carried at high voltage for as long as possible and stepped down at the very last moment, as close to the processor as the board allows. As I wrote in an earlier piece, that logic is why the industry is moving the whole rack to 800 volts.

TI says a one megawatt rack fed at 48 volts would need almost 450 pounds of copper. In March 2026, at Nvidia's developer conference, it showed a complete set of parts for the 800 volt design. Power steps down in only two stages: from 800 volts to 6 volts, then from 6 volts to below one volt.

TI says its first-stage converter reaches 97.6 per cent peak efficiency. That number matters more than it looks. In a one megawatt rack, every percentage point lost in conversion is ten kilowatts of extra heat, which the cooling system then has to remove as well.

Around those converters sit protection chips. An eFuse, an electronic fuse, cuts the power in microseconds if something shorts, and a hot-swap controller lets an engineer pull a live tray without crashing the rack. In 2025 TI released a 48 volt eFuse for exactly that job.

## The factory bet

The second half of the story is where those chips are made. Most chip companies now design their products and rent factory space to make them. TI went the other way and decided to own almost every step.

On 18 June 2025, TI announced plans to invest more than $60 billion across seven American chip factories in Texas and Utah. The largest site is Sherman, Texas, with room for four connected factories. The first, SM1, began production on 17 December 2025.

TI says SM1 will ultimately produce tens of millions of chips a day. Every wafer it runs is 300mm. In its 2025 annual report, TI says an unpackaged chip made on a 300mm wafer costs about 40 per cent less than one made on a 200mm wafer.

That is a big edge for a product that sells for cents and competes on price. TI's stated goal is to make more than 95 per cent of its wafers in its own factories by 2030, with over 80 per cent of them on 300mm.

## What TI's own numbers show

If AI is pulling on these chips, the data centre should be growing much faster than the rest of TI.

**Mix.** In TI's 2025 annual report, data centres were 9 per cent of revenue. Industrial and automotive were 33 per cent each. So this is a small slice of a large analog business, not an AI company.

**Growth.** In the second quarter of 2026, reported on 22 July 2026, total revenue rose 23 per cent to $5.46 billion. On the earnings call, TI said data centre revenue had doubled on a year earlier. That is the fastest-growing market TI reports.

**Margin.** Gross margin, the share of each sale left after the cost of making it, was 61 per cent in the quarter. For a company whose main product sells for very little, that is what owning cheap, full factories looks like in money.

**Spending.** Capital spending fell from $4.55 billion in 2025 to an expected $2 billion to $3 billion in 2026. TI says its six-year cycle of heavy factory building is nearly over. The factories are built. Now they have to fill.

## What would prove me wrong

I am wrong if the 800 volt design is adopted slowly. TI itself said on the July call that the new architecture will be phased in. If racks stay at 54 volts for years, TI is one of many suppliers of a mature product rather than an early mover in a new one.

I am also wrong if rivals hold the high end. Infineon, Monolithic Power, Analog Devices and others make the same kinds of power chips, and the processor makers choose. Cheaper factories help most on simple parts. The newest, most demanding parts are won on design.

And the factory bet can backfire. TI built ahead of demand. If industrial and car demand weakens while data centre stays small, those new 300mm lines run part-empty, and a cost advantage becomes a cost burden.

So I watch three things. Whether data centre keeps growing as a share of TI's revenue. Whether named operators commit to 800 volt racks. And whether gross margin holds as the new Sherman capacity comes online.

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

<p class="sources">Sources: Texas Instruments second quarter 2026 results, released 22 July 2026, and earnings call of the same date, for revenue, gross margin, data centre growth and 800 volt timing. Texas Instruments annual report and Form 10-K for 2025 for revenue by end market, 300mm cost and the 2030 manufacturing goal. Texas Instruments announcements of 18 June 2025 on the $60 billion investment, 17 December 2025 on Sherman production, 17 March 2025 on its 48 volt eFuse, 23 May 2025 on copper in a one megawatt rack, and 16 March 2026 on its 800 volt power design. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
