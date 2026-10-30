---
title: "The chip isn't slow. Fetching is. Why memory became the bottleneck"
date: 2026-09-18
summary: "When an AI writes its reply, the arithmetic is fast and the waiting for data is slow. So the industry started stacking memory chips into little towers glued right next to the processor. It's a clever fix, it's expensive, and it explains a lot about which parts of the AI supply chain are actually scarce."
category: "Explainer"
cover: "/covers/memory.svg"
tags: ["memory", "HBM", "the-stack"]
---

There is a widespread assumption that AI is limited by how fast a chip can do maths. For the part you actually experience, the answer typing itself out, that is wrong.

When the model writes, one token at a time, the arithmetic is fast. What is slow is fetching: pulling the model's settings and its memory of your conversation into the cores, again for every word.

In the jargon, inference, the model answering you, is memory-bandwidth-bound.

The cook is quick. The countertop is too far from the pantry.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine a chef who can chop faster than anyone alive, but the pantry is across the car park. However fast the knife, the job is limited by walking.</p>
<p>So the industry moved the pantry. Stacked memory piles the ingredients into a tower eight to twelve storeys high and glues it beside the chopping board. Millimetres instead of a car park.</p>
</details>

## Move the pantry

For decades, computer memory sat on the motherboard a few centimetres from the processor, joined by wires on the circuit board. That was wide enough for ordinary work, and far too slow for this.

The fix is high-bandwidth memory, HBM. Instead of laying memory chips flat, you stack them eight to twelve high. Thousands of microscopic vertical shafts run straight through the silicon, so data travels up and down the tower instead of across a board. Then the whole tower is glued beside the processor on the same package, millimetres away.

The result is five to six times the bandwidth of conventional memory, at roughly five to six times the cost. Chip makers pay it gladly, because memory is now one of the largest costs in every AI chip.

Supply cannot simply catch up. Only three companies in the world make HBM at scale, and each tower must then be joined to its processor by advanced packaging.

## A scarce thing behaves like a scarce thing

In the current cycle, those three companies have sold out their output well in advance. That changed the psychology of an industry that was, for decades, a brutal boom-and-bust commodity business. Memory is now allocated like a scarce resource and priced like a luxury.

The pressure reaches the back of the warehouse too. AI produces enormous amounts of data as well as consuming it. The spinning hard drive, declared dead a decade ago, is still the cheapest way per terabyte to keep it.

## The bottlenecks do not clear together

Memory and chip packaging are hard, but they are the kind of hard that money solves in quarters. Factories and production lines can be built, and are being built.

A transformer, a substation or a place in a grid connection queue is different. It waits on physical infrastructure, permitting and a supply chain with very few producers.

So the bottlenecks near the chip clear first, and the ones near the wall socket clear last. Watch only the chip and you will think the constraint has lifted long before it has.

<section class="exposure">
<h3>Who makes the parts</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. On memory in particular I hold no investment view.</p>
<dl>
<dt>Stacked memory beside the chip</dt>
<dd><span class="names">SK Hynix, Samsung and Micron</span> make high-bandwidth memory at scale.</dd>
<dt>Storage</dt>
<dd><span class="names">Seagate and Western Digital</span> make hard drives for cold data. <span class="names">Kioxia and Solidigm</span> make solid-state drives for data in active use.</dd>
<dt>The packaging that makes it work</dt>
<dd><span class="names">TSMC</span> does the advanced packaging that joins the tower to the processor.</dd>
</dl>
<dl class="against">
<dt>Where I stop</dt>
<dd>Memory has been a boom-and-bust business for decades. I do not know what happens to pricing when all three makers finish expanding at once.</dd>
</dl>
</section>

---

<p class="sources">This piece explains mechanism: why inference is bound by memory bandwidth, how stacked memory works, and where it sits in the storage hierarchy. I have no view on the memory equities. Personal research, not investment advice.</p>
