---
title: "The rack runs out of copper before it runs out of chips"
date: 2026-08-07
summary: "AI computers are getting so power-hungry that the copper bars carrying electricity inside each cabinet would soon weigh more than the computers. So the industry is about to change how power enters the building. That change, not the chips, is what decides who gets to build."
category: "Explainer"
cover: "/covers/copper-rack.svg"
tags: ["power", "data-centres", "800VDC"]
draft: false
---


Every few months a new AI chip is announced and the headlines follow it.

What almost nobody writes about is the metal cabinet the chip lives in, and how electricity gets to it.

The cabinets are now drawing so much power that the copper inside them is becoming the limit. So the industry is about to change how power enters the building.

That question is about to become the whole story.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine watering a garden through a hundred drinking straws instead of one hosepipe. You move the same water, but you need an absurd number of straws, and they weigh a fortune.</p>
<p>Electricity behaves the same way. At low voltage you need enormous amounts of copper. The AI cabinet has got big enough that the straws no longer fit, so the industry is switching to a hosepipe.</p>
</details>

## A cabinet drawing the power of a small town

An AI rack is a cabinet about two metres tall, packed with computer trays. Today's flagship racks, holding NVIDIA's latest chips, sit near 200 kilowatts. The next generation, called Kyber and due in 2027, is designed to draw up to **one megawatt**, as much as several hundred homes.

Inside the rack, power reaches the trays through thick copper bars called busbars, at 54 volts. Pushing a megawatt at that voltage needs enormous current, and enormous current needs enormous conductors.

The fix is to raise the voltage. Higher voltage means less current for the same power, so thinner wires, less copper and less heat. The industry is moving to **800 volts direct current**, carried from the edge of the building straight to the cabinet.

It can happen now because electric car charging already built the parts. The electronics that switch high-voltage direct current safely and cheaply were made at scale for cars first.

## NVIDIA published the numbers itself

NVIDIA, which has every reason to make this sound easy, put the problem in writing.

Its own figure is **up to 200 kilograms of copper busbar in a single rack** at today's 54 volts. And the power shelves, the units that convert incoming power for the trays, would need more space than the rack has. In its words, that would leave no room for compute.

The power delivery system starts eating the thing it exists to power.

## Why power, not silicon, now sets the pace

Every new chip generation pushes more of the problem out of silicon and into power delivery. This is the [grid connection problem](/journal/the-queue-not-the-chip/) one floor down.

The two problems run on different clocks. A chip shortage clears in quarters, because you can build another factory line. Power hardware clears in years, because it waits on transformers, switchgear and the grid.

A published standard is also not a deployment. The operators who must rebuild their electrical rooms have said little publicly, and 2027 is a date in an industry where dates slip.

<section class="exposure">
<h3>Who is exposed in the power delivery shift</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>Rack and facility power systems</dt>
<dd><span class="names">Eaton, Schneider Electric and Vertiv</span> make rack and building power systems.</dd>
<dt>Power components</dt>
<dd><span class="names">Delta, LiteOn, Megmeet, Flex Power and Lead Wealth</span> build the conversion hardware.</dd>
<dt>The switching silicon</dt>
<dd><span class="names">Infineon, Texas Instruments, onsemi, ROHM, STMicroelectronics, Renesas, Analog Devices and Monolithic Power</span> make high-voltage power chips, and <span class="names">Navitas and Innoscience</span> make gallium nitride ones.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Makers of the in-rack power shelves and low-voltage busbar the new design is built to delete.</dd>
</dl>
</section>

---

<p class="sources">Sources: NVIDIA Technical Blog, "NVIDIA 800 VDC Architecture Will Power the Next Generation of AI Factories", 20 May 2025, and the Open Compute Project. All figures as published by NVIDIA. Personal research, not investment advice.</p>
