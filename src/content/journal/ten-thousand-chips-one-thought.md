---
title: "Ten thousand chips, one thought: why the network costs almost as much as the chips"
date: 2026-09-18
summary: "A frontier AI model is too big to fit on any single chip, so it's sliced across thousands of them, and they have to swap notes for every single word. If the wiring between them is even slightly slow, the most expensive chips ever built sit idle. That's why a huge slice of every AI dollar goes on cables and light."
category: "Explainer"
cover: "/covers/network.svg"
tags: ["networking", "optics", "the-stack"]
---

Here is the problem in one sentence. A frontier model has more than a trillion internal settings, and no single chip has anywhere near enough memory to hold them. So the model is cut into pieces and spread across thousands of chips.

That would be fine if each piece could work alone. It can't. To produce one token, the pieces have to exchange their partial results with each other, constantly, and then do it again for the next token. Ten thousand chips, one thought.

Imagine a kitchen with ten thousand cooks preparing a single dish, where every cook needs ingredients from other cooks every second. If passing ingredients is slow, the most expensive cooks in history stand around waiting. At this scale, a network that is 10 per cent slower can leave billions of dollars of silicon doing nothing.

That is why the network is not an afterthought. It is a large fraction of what a data centre spends per chip, and the spending is rational.

## Two words you need

**Bandwidth** is how much data moves per second: the width of the conveyor belt.

**Latency** is the delay of a single handoff: how long one ingredient takes to cross the kitchen.

Most computing cares about one or the other. AI needs both, everywhere, at the same time, because thousands of chips are waiting on each other for every word.

## Two networks, not one

The wiring inside an AI data centre is really two different systems.

**Scale-up: inside the cabinet.** Within a single rack, dozens of chips are linked by a proprietary, extremely fast web that makes them behave as one machine. This is the tightest, fastest, most expensive connection in the building, and it is measured in centimetres.

**Scale-out: cabinet to cabinet.** Connecting racks to each other across a hall is a different job with a different technology, and it is where a real contest has played out. One approach is a premium, single-vendor technology with the best performance and the highest price. The other is Ethernet, the open standard that runs the ordinary internet, adapted for AI. By early 2026 roughly two thirds of new AI cluster networking was Ethernet. Open standards, given time, usually win. They just did.

## Where copper dies and light takes over

Copper wire carries a signal well for a few metres and then the signal degrades. Between racks, everything is converted to light and sent down glass fibre.

At each end of every fibre link sits a thumb-sized device called an optical transceiver, which translates between electricity and light. A large cluster uses hundreds of thousands of them. And because the speed requirement rises with every chip generation, they get replaced at each upgrade cycle. They are consumables. Razor blades for data centres.

The frontier here is to move the light conversion directly onto the switch chip itself, an approach called co-packaged optics, which cuts power and distance. Watch for it, because it changes what gets bought and how often.

## The uncomfortable footnote

Most of the time, the world's most expensive chips are not waiting for data from across the room. They are waiting for data two centimetres away, in their own memory. That is the next piece.

## How I'd say this in a room

The skeleton I use for any "justify the spending" question runs claim, constraint, consequence, reframe.

Claim: the network costs what it costs because the alternative is worse. Constraint: a trillion-parameter model versus a few hundred gigabytes of memory per chip, so it is sliced across thousands. Consequence: a network 10 per cent slow leaves the most expensive silicon ever made idle, and idle GPUs are the costliest waste in the building. Reframe: so forty to sixty cents of network for every dollar of chips is not extravagance. It is insurance on the other dollar.

---

<p class="sources">This piece explains mechanism: why models are split across chips, the two kinds of network, and why optics replace copper. Figures are structural. I name technologies rather than vendors on purpose. Personal research, not investment advice.</p>
