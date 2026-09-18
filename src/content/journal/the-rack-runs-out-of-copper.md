---
title: "The rack runs out of copper before it runs out of chips"
date: 2026-08-07
summary: "AI computers are getting so power-hungry that the copper bars carrying electricity inside each cabinet would soon weigh more than the computers. So the industry is about to change how power enters the building. That change, not the chips, is what decides who gets to build."
shortLabel: "800 VDC"
category: "Explainer"
cover: "/covers/copper-rack.svg"
tags: ["power", "data-centres", "800VDC"]
draft: false
---

Every few months a new AI chip is announced and the headlines follow it. What almost nobody writes about is the boring metal box the chip lives in, and the even more boring question of how electricity gets to it.

That question is about to become the whole story.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine watering a garden through a hundred drinking straws instead of one hosepipe. You can move the same water, but you need an absurd number of straws, and they weigh a fortune in plastic.</p>
<p>Electricity behaves the same way. At low voltage you need enormous amounts of copper to carry the current. Raise the voltage and you need far less metal to move the same power, which is exactly why the pylons outside your window run at very high voltage rather than at household voltage.</p>
<p>The AI rack has finally got big enough that the straws no longer fit in the box. So the industry is switching to a hosepipe. And the parts to do it were already built and made cheap by the electric car charging industry, which had the same problem first.</p>
</details>

## A cabinet the size of a fridge, drawing the power of a small town

An AI "rack" is a cabinet about two metres tall, packed with computer trays. A few years ago a full rack drew maybe 10 to 20 kilowatts, roughly what a dozen homes use at once. Today's flagship racks, the kind holding NVIDIA's latest chips, sit near 200 kilowatts. The next generation, called Kyber and due in 2027, is designed to hold 576 chips and draw up to **one megawatt**. That is a single cabinet using as much electricity as several hundred homes.

Inside the rack, power gets to the trays through thick copper bars called busbars. The industry has used the same low-voltage system for years: 54 volts, carried on copper. At 20 kilowatts that works fine. At one megawatt the physics turns against you.

## Two numbers that end the argument

NVIDIA, which has every reason to make this sound easy, published the numbers itself.

**First, the copper.** Pushing a megawatt through a 54-volt system needs enormous current, and enormous current needs enormous conductors. NVIDIA's own figure is **up to 200 kilograms of copper busbar in a single rack**. Across a large campus, the rack busbars alone would come to around 200,000 kilograms of copper.

**Second, the space.** The equipment that converts incoming power for the trays lives in "power shelves" inside the rack. Today's racks carry up to eight of them. To feed a one-megawatt rack the old way, NVIDIA says you would need power shelves taking up **64 units of rack space**, which is more rack than the rack has. In their words, that would leave no room for compute.

That is the entire argument in one line: **the power delivery system starts eating the thing it exists to power.**

## The fix is borrowed from electric cars

The answer is to raise the voltage. Higher voltage means less current for the same power, which means thinner wires, less copper, and less heat. The industry is moving from 54 volts inside the rack to **800 volts direct current**, carried right from the edge of the building to the cabinet.

NVIDIA's published design takes power off the grid at 13,800 volts, converts it once to 800 volts DC at the building's edge, and delivers it straight to the rack. Compared to today's system, the same conductor carries **85% more power**, backbone copper falls by about **45%**, and the whole chain gets **up to 5% more efficient** because there are far fewer conversion steps and far fewer fans and power supplies left to fail. NVIDIA puts the total cost of ownership saving at up to 30%.

Why now, and not ten years ago? Because the electronics needed to switch high-voltage DC safely and cheaply were built out, at scale, by electric vehicle charging. The data centre is inheriting an EV supply chain.

## Why this matters more than the chip roadmap

I have argued elsewhere that the real bottleneck on AI is not the chip but the grid connection: the substation, the transformer, the queue to plug in. This is the same story one floor down. Every new chip generation pushes more of the problem out of silicon and into power delivery and heat removal.

And the two problems have very different clocks. A chip shortage clears in quarters, because you can build another factory line. Power hardware clears in years, because it waits on transformers, switchgear and the grid. Treating them as one cycle is the mistake.

## Who benefits, if I'm right

NVIDIA published the list of companies it is building this with. That list is a map of where the money goes. At the top, the big power-systems firms: Eaton, Schneider Electric, Vertiv. In the middle, the component makers: Delta, LiteOn, Megmeet. Underneath, the chip companies that make the high-voltage switching parts: Infineon, Texas Instruments, onsemi, ROHM, STMicroelectronics, plus two specialists in a newer material called gallium nitride, Navitas and Innoscience.

Two quieter points matter more than they look. NVIDIA says it has not yet decided between traditional transformers and a newer solid-state design at the building's edge, which is a genuine fork in the road. And battery storage is written into the design itself, to absorb the sudden power spikes that AI workloads produce. That makes batteries part of the rack, not just a grid-side product.

One thing runs against the headline. Less copper *per unit of power* does not mean less copper. Power is growing faster than the saving. It changes what kind of copper products are needed, not how much.

## What would prove me wrong

A published standard is not a deployment. NVIDIA and roughly thirty vendors have coordinated this through the Open Compute Project, but the people who have to rebuild their electrical rooms are the data centre operators, and they have said very little publicly. NVIDIA itself names the alternative: a whole separate rack of power supplies next to each compute rack. If the industry does that instead, this becomes a slow component refresh rather than a change in architecture.

I would also be wrong if rack power plateaus below 200 kilowatts because it turns out to be cheaper to run many smaller AI deployments than a few enormous ones. And 2027 is a date in an industry where dates slip.

So I am watching four things: public 800-volt commitments from named operators rather than vendors, whether solid-state transformers win the building edge, new factory capacity for gallium nitride and silicon carbide aimed at data centres rather than cars, and whether this year's racks in the field actually land above 200 kilowatts.

<section class="exposure">
<h3>Who is exposed in the power delivery shift</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>Rack and facility power systems</dt>
<dd>From NVIDIA's own published partner list, which is revealed preference rather than marketing: <span class="names">Eaton, Schneider Electric and Vertiv</span>.</dd>
<dt>Power components</dt>
<dd><span class="names">Delta, LiteOn, Megmeet, Flex Power and Lead Wealth</span> build the conversion hardware inside the chain.</dd>
<dt>The switching silicon</dt>
<dd>Moving to high-voltage direct current is a wide-bandgap semiconductor story: <span class="names">Infineon, Texas Instruments, onsemi, ROHM, STMicroelectronics, Renesas, Analog Devices and Monolithic Power</span>, plus the gallium nitride specialists <span class="names">Navitas and Innoscience</span>.</dd>
<dt>Storage, again</dt>
<dd>Energy storage is written into the architecture itself, sized for the sudden power spikes AI workloads produce rather than for arbitrage. That makes batteries rack-adjacent infrastructure, not only a grid-side trade.</dd>
<dt>The copper nuance</dt>
<dd>Less copper per unit of power does not mean less copper. Power is growing faster than the saving. It changes the specification and the mix, not the direction.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Suppliers whose product is the thing being removed: the in-rack power shelves and the low-voltage busbar the new architecture is designed to delete.</dd>
</dl>
</section>

---

<p class="sources">Sources: NVIDIA Technical Blog, "NVIDIA 800 VDC Architecture Will Power the Next Generation of AI Factories", 20 May 2025; NVIDIA 800 VDC architecture pages; Open Compute Project. All figures as published by NVIDIA. This is a plain-language version of a technical note I published on 17 September 2026. Personal research, not investment advice.</p>
