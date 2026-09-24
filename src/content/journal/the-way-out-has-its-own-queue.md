---
title: "The best argument against my own thesis, and why I still think it is wrong"
date: 2026-09-22T18:56:00+08:00
summary: "I have argued that the queue to connect to the electricity grid is what limits AI. The strongest objection is that operators can skip the queue entirely by building their own power station on site. That objection is real, and worth taking seriously. But the escape route has a waiting list of its own, and the order books are already full to 2030."
category: "Analysis"
cover: "/covers/the-way-out-has-its-own-queue.svg"
tags: ["grid", "power", "data-centres"]
draft: false
---

I have written twice now that the thing holding back AI is not the chip. It is the wait to plug into the electricity grid.

Every argument deserves its strongest opponent, and this one has an obvious one.

If the queue is the problem, do not join the queue. Build your own power station next to the building, burn gas, and connect to nothing.

This is called going behind the meter, meaning you generate on your own side of the utility's meter and never ask permission to draw from the public network. It is happening, it is real, and if it works at scale then most of what I have written is a two year story rather than a structural one.

So here is my honest attempt to argue against myself.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine a restaurant that cannot get a big enough water connection from the council. There is a long wait for the new pipe, and without it the kitchen cannot open.</p>
<p>The obvious answer is to stop waiting and drill your own well. No council, no queue, water on your own land.</p>
<p>Then you ring the drilling company. They are fully booked for four years, because every other restaurant on the street had the same clever idea at the same time. The well is a real solution. It is just not a fast one, and it was never the bit that was quick.</p>
</details>

## The objection, put at its strongest

On-site generation genuinely removes the part of the delay I have spent the most time on. No interconnection study, no place in a queue, no waiting for a utility to decide whose project goes first.

It is also not fringe. Gas turbine makers are reporting demand of a kind they have not seen in decades, and a meaningful share of it is data centre driven. If you can buy a machine that makes your own electricity, the grid becomes a backup rather than a dependency.

Anyone holding my view should be uncomfortable with that. I am.

## Why I still think it relocates the problem rather than removing it

Then you look at who makes the machines, and how full their order books are.

GE Vernova has **116 gigawatts under contract**. That splits into 53 gigawatts of firm backlog and 63 gigawatts under slot reservation agreements, which are effectively places held in a queue to be manufactured. Its capacity is described as mostly sold out through 2030.

Siemens Energy reports **95 gigawatts**, comprising 69 gigawatts of firm backlog and 26 gigawatts under reservation.

Read those numbers again, because they are the answer to the objection. The escape route from the connection queue is itself a queue, and it is already years deep.

The manufacturers are responding, which is the right thing to do and also the slowest possible thing to do. GE Vernova is lifting annual gas turbine output from 20 gigawatts to 24 in 2028 and 30 by 2030. That is a large expansion. It is also a four year plan to increase supply by half, which tells you exactly how quickly this kind of capacity can be added.

## The part people forget entirely

A gas turbine on your site does not connect itself to your building with an extension lead.

It still needs transformers to step the voltage to something the site can use. It still needs switchgear, the heavy equipment that makes and breaks connections safely. It still needs protection systems and a substation-grade electrical yard.

Those are the same components, from the same constrained supply chain, that make the grid connection slow in the first place. You have removed the utility from the process. You have not removed the equipment.

**You have swapped a queue you cannot control for a queue you can, which is worth something, but it is not the same as no queue.**

There is a second cost that rarely appears in the argument. On-site gas means you now operate a power station. That is fuel supply, emissions permitting, maintenance crews and the local politics of putting a combustion plant next to a community. Those are all solvable and none of them is instant.

## What this changes about my view

It sharpens it rather than softening it.

My claim has never been that electricity is scarce. Generation capacity is broadly sufficient in the markets I have looked at closely. My claim is that the **delivery** of electricity is the constraint, and behind the meter does not contradict that. It confirms it, because it is a very expensive way of saying the normal route is too slow.

If anything, the size of the turbine backlog is the clearest evidence I have found for the original thesis. Nobody reserves a manufacturing slot years out for a power station they do not need. That backlog is a measurement of how badly the ordinary connection route is failing people.

## What would prove me wrong

This piece is the falsifier, so it deserves a specific one rather than a vague one.

I am wrong if turbine lead times fall materially while the backlog is still being worked through, because that would mean the bottleneck was capacity discipline rather than physical capability, and it could unwind quickly. I am also wrong if a significant number of large sites energise on site generation faster than comparable sites achieve a grid connection. That is the direct head to head test, and it is measurable.

And I am wrong about the whole stack if the equipment underneath both routes, the transformers and the switchgear, stops being the constraint. That is the single dependency my argument rests on. If it clears, everything I have written becomes a story about one difficult decade rather than a structural feature.

So I watch three things: gas turbine lead times and whether the announced expansions land on schedule, the ratio of behind-the-meter to grid-connected capacity actually energised rather than announced, and transformer and high voltage cable lead times, which sit underneath both.

<section class="exposure">
<h3>Who is exposed if the escape route is slower than it looks</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The order book figures below are the companies' own disclosures as reported, and I draw no conclusion from them about value.</p>
<dl>
<dt>The turbine makers</dt>
<dd><span class="names">GE Vernova</span>, <span class="names">Siemens Energy</span>, <span class="names">Mitsubishi Power</span> and <span class="names">Ansaldo Energia</span> build the heavy-duty gas turbines that on-site generation depends on.</dd>
<dt>The electrical plant either route still needs</dt>
<dd><span class="names">Hitachi Energy</span>, <span class="names">Schneider Electric</span> and <span class="names">Eaton</span> make the transformers, switchgear and protection equipment required whether the power comes from the grid or from next door.</dd>
<dt>The people who build the yard</dt>
<dd><span class="names">EGP Energy</span> and <span class="names">Surbana Jurong</span> do electrical transmission, distribution and industrial engineering work of the kind an on-site plant needs.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Operators whose published timelines assume on-site generation is a fast alternative rather than a differently-shaped wait. Anyone treating a reserved manufacturing slot as though it were a delivered machine.</dd>
</dl>
</section>

---

<p class="sources">Sources: gas turbine order book and manufacturing capacity figures for GE Vernova and Siemens Energy as reported by POWER Magazine on 1 September 2026, drawing on the companies' own disclosures, including GE Vernova's 116 gigawatts under contract and planned output increase to 30 gigawatts a year by 2030, and Siemens Energy's 95 gigawatts. The description of the electrical equipment an on-site plant requires is mechanism rather than forecast. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
