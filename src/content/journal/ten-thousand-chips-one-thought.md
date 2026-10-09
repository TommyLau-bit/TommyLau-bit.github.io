---
title: "Ten thousand chips, one thought: why the network costs about half as much as the chips"
date: 2026-09-04
summary: "A frontier AI model is too big to fit on any single chip, so it's sliced across thousands of them, and they have to swap notes for every single word. If the wiring between them is even slightly slow, the most expensive chips ever built sit idle, so a huge slice of every AI dollar goes on cables and light."
category: "Explainer"
cover: "/covers/network.svg"
tags: ["networking", "optics", "the-stack"]
---

A frontier model has more than a trillion internal settings, and no single chip has anywhere near enough memory to hold them. So the model is cut into pieces and spread across thousands of chips.

That would be fine if each piece could work alone. It can't. To produce one token, a word or part of a word, the pieces must swap partial results, then do it again for the next token.

At this scale, a network that is 10 per cent slower can leave billions of dollars of silicon doing nothing.

The network is not an afterthought. It is a large share of what a data centre spends per chip, and the spending is rational.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture ten thousand people writing one essay together, a word at a time. Before anyone adds a word, they have to read what everyone else just wrote.</p>
<p>If passing notes around the room is slow, ten thousand of the world's most expensive writers sit still, waiting. The writing was never the bottleneck. The note-passing was.</p>
</details>

## Two networks, not one

Two words matter here. Bandwidth is how much data moves per second, the width of the conveyor belt. Latency is the delay of a single handoff. AI needs both at once, because thousands of chips wait on each other for every word.

The wiring inside an AI data centre is really two different systems.

**Scale-up: inside the cabinet.** Within one rack, dozens of chips are linked by a proprietary, extremely fast web that makes them behave as one machine. It is the tightest, most expensive connection in the building, measured in centimetres.

**Scale-out: cabinet to cabinet.** Connecting racks across a hall is a different job. One approach is a premium, single-vendor technology. The other is Ethernet, the open standard that runs the ordinary internet, adapted for AI. By early 2026 roughly two thirds of new AI cluster networking was Ethernet.

Copper carries a signal well for a few metres, then the signal degrades. So between racks, everything is converted to light and sent down glass fibre.

## Where copper dies and light takes over

At each end of every fibre link sits a thumb-sized device called an optical transceiver, which translates between electricity and light. A large cluster uses hundreds of thousands of them.

Because the speed requirement rises with every chip generation, they are replaced at each upgrade. They are consumables, razor blades for data centres.

The frontier is co-packaged optics, which moves the light conversion onto the switch chip itself to cut power and distance. It changes what gets bought, and how often.

## Why the network costs what it costs

The constraint is plain. A model with a trillion settings, against a few hundred gigabytes of memory per chip, has to be sliced across thousands of chips.

A network 10 per cent slow then leaves the most expensive silicon ever made idle, and idle chips are the costliest waste in the building. So forty to sixty cents of network for every dollar of chips is not extravagance. It is insurance on the other dollar.

Even then, the chips mostly wait on data two centimetres away, in their own memory. That is [the next piece](/journal/the-countertop-is-the-bottleneck/).

<section class="exposure">
<h3>Who is exposed in the network layer</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>Switch and network silicon</dt>
<dd><span class="names">Broadcom</span> and <span class="names">Marvell</span> make networking chips and custom accelerators. <span class="names">Astera Labs</span> makes retimer chips that clean up fading signals.</dd>
<dt>The boxes</dt>
<dd><span class="names">Arista</span> and <span class="names">Cisco</span> make switches. <span class="names">Nvidia</span> makes NVLink and InfiniBand.</dd>
<dt>The optics</dt>
<dd><span class="names">Coherent, Lumentum, Innolight</span> make transceivers, assembled by <span class="names">Fabrinet</span>. <span class="names">Corning</span> makes the fibre, <span class="names">Amphenol</span> the connectors.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Single-vendor, proprietary scale-out networking, if open Ethernet keeps spreading through AI clusters.</dd>
</dl>
</section>

---

<p class="sources">This piece explains mechanism: why models are split across chips, the two kinds of network, and why optics replace copper. Figures are structural. Personal research, not investment advice.</p>
