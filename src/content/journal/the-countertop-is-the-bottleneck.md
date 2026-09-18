---
title: "The chip isn't slow. Fetching is. Why memory became the bottleneck"
date: 2026-09-18
summary: "When an AI writes its reply, the arithmetic is fast and the waiting for data is slow. So the industry started stacking memory chips into little towers glued right next to the processor. It's a clever fix, it's expensive, and it explains a lot about which parts of the AI supply chain are actually scarce."
category: "Explainer"
cover: "/covers/memory.svg"
tags: ["memory", "HBM", "the-stack"]
---

There is a widespread assumption that AI is limited by how fast a chip can do maths. For the part of the job you actually experience, the answer typing itself out, that is wrong.

When the model writes, one token at a time, its maths cores are often not the constraint. The arithmetic is fast. What is slow is fetching: pulling the model's settings and its working memory of your conversation out of storage and into the cores, over and over, for every word. In the jargon, inference is memory-bandwidth-bound. In plain terms, the cook is quick but the countertop is too far from the pantry.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine a chef who can chop faster than anyone alive, but the pantry is across the car park. It does not matter how fast the knife is. The job is limited by walking.</p>
<p>That is a modern AI chip while it writes an answer. The arithmetic is quick; fetching the data is slow.</p>
<p>So the industry did the obvious thing: it moved the pantry. Stacked memory takes the ingredients, piles them into a tower eight to twelve storeys high, and glues that tower directly beside the chopping board. Millimetres instead of a car park.</p>
</details>

## Move the pantry

For decades, computer memory sat on the motherboard a few centimetres from the processor, connected by wires on the circuit board. Think of it as suburbs across a motorway from the factory. Wide enough for ordinary work. Far too slow for this.

The fix is called high-bandwidth memory, HBM, and it is a genuinely elegant piece of engineering. Instead of laying memory chips flat, you stack them eight to twelve high. You drill thousands of microscopic vertical shafts straight through the silicon so data can travel up and down the tower instead of across a board. Then you glue the whole tower directly beside the processor, on the same package, so the distance is millimetres rather than centimetres.

The result is five to six times the bandwidth of conventional memory. The cost is roughly five to six times the price. Chip makers pay it gladly, because memory is now one of the largest cost components in every AI chip. The countertop moved next to the cook.

## A scarce thing behaves like a scarce thing

Only three companies in the world make HBM at scale, and in the current cycle their output has been sold out well in advance. That changed the psychology of an industry that was, for decades, a brutal boom-and-bust commodity business. Memory is now allocated like a scarce resource and priced like a luxury.

I want to be precise about what I do and do not claim here. I can explain the mechanism, why it works and why it is scarce. I have no view on the memory companies as investments, and I would distrust anyone who confidently offered one, because memory cycles have broken hearts before. The open question is what happens to prices when all three finish expanding capacity at the same time. I don't know.

## The rest of the warehouse

Memory is one layer of a hierarchy, and the rule is simple: the closer to the chip, the faster and pricier. Tiny cache on the chip itself. HBM beside it. Ordinary DRAM on the board. Solid-state drives for data in active use. Spinning hard drives for cold bulk storage at the back.

One thing about that hierarchy surprised people. Everyone expected AI to consume enormous amounts of data for training. Fewer expected it to produce enormous amounts: every conversation, every log, every generated image, retained. AI is a data hoarder in both directions, and the spinning hard drive, declared dead a decade ago, is still the cheapest way per terabyte to keep cold data. It has been quietly resurrected.

## Why this matters for the argument running through this journal

Here is the comparison I actually hold a view on.

Memory and chip packaging are hard, but they are the kind of hard that money solves in quarters. Factories and production lines can be built, and are being built. A transformer, a substation, or a place in a grid connection queue is the kind of hard that money does not solve quickly, because it waits on physical infrastructure, permitting and a supply chain with very few producers.

So the bottlenecks up and down the stack do not resolve together. The ones near the chip clear first. The ones near the wall socket clear last. If you only watch the chip, you will think the constraint has lifted long before it has.

<section class="exposure">
<h3>Who makes the parts</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. On memory in particular I hold no investment view.</p>
<dl>
<dt>Stacked memory beside the chip</dt>
<dd><span class="names">SK Hynix, Samsung and Micron</span> are the only three companies making high-bandwidth memory at scale.</dd>
<dt>Cold bulk storage</dt>
<dd>The spinning hard drive, written off a decade ago, is still the cheapest way to keep data nobody is reading today: <span class="names">Seagate and Western Digital</span>.</dd>
<dt>Hot storage</dt>
<dd>The faster solid-state tier for data in active use: <span class="names">Kioxia and Solidigm</span>.</dd>
<dt>The packaging that makes it work</dt>
<dd>Stacking and joining the tower to the processor is advanced packaging, done by <span class="names">TSMC</span> and its equipment suppliers.</dd>
</dl>
<dl class="against">
<dt>Where I stop</dt>
<dd>I can explain how this works and why it is scarce. I hold no view on the memory companies as investments and I would distrust anyone who offered one confidently. Memory has been a brutal boom-and-bust business for decades, and the open question is what happens to pricing when all three finish expanding capacity at the same time. I do not know.</dd>
</dl>
</section>

---

<p class="sources">This piece explains mechanism: why inference is bound by memory bandwidth, how stacked memory works, and where it sits in the storage hierarchy. I have no view on the memory equities and say so above. Personal research, not investment advice.</p>
