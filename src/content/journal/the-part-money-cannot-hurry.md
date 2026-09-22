---
title: "The one part of the grid that money cannot hurry"
date: 2026-09-24
summary: "Malaysia cut the wait to connect a data centre to the grid from three years to one, which is a real achievement and also a warning. Paperwork can be sped up, but the large steel machine that actually delivers the power cannot. Those two things sit in the same queue and run on completely different clocks."
category: "Analysis"
cover: "/covers/the-part-money-cannot-hurry.svg"
tags: ["grid", "power", "data-centres"]
draft: false
---

Malaysia's grid operator did something unusual last year. It took the time needed to connect a new project to the grid and cut it from thirty six months to twelve.

That is a genuine piece of administration, and it worked. Thirty three projects went through the scheme by March 2026.

It is also the most useful experiment anyone has run on the AI buildout, because of what it could not do.

It could not make a transformer any faster.

A connection queue looks like one line. It is really two, and only one of them answers to a government.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think about getting a new kitchen fitted. Some of the wait is admin: the council signing off the work, the installer finding a slot, the paperwork moving between desks. Push hard enough, pay for the faster service, and that part of the wait shrinks.</p>
<p>The rest of the wait is the worktop itself. It is cut to measure from a slab of stone, in a workshop, by people with a full order book. No amount of chasing makes the stone arrive sooner, because nobody has one sitting on a shelf in your exact size.</p>
<p>A grid connection is the same shape. Half the delay is desks. The other half is a machine the size of a small house, built to order, and the two halves do not speed up together.</p>
</details>

## Two clocks inside one queue

When a data centre developer says it is waiting for a grid connection, it is waiting for two different things at once.

The first is permission and position. Studies, approvals, a place in the order in which projects get connected, and agreement on who pays for what. All of that is process. It is done by people, on schedules that a government can rewrite.

The second is plant. A substation is not paperwork. It is a physical site holding switchgear, which is the heavy equipment that makes and breaks high voltage connections safely, along with protection equipment, cable and, at its centre, a large power transformer. That last item is the one that decides everything.

A transformer steps voltage down from the level the grid uses for long distance transport to the level a site can actually consume. Without one, the wires arriving at the fence are useless.

## Why the first clock can be compressed

Malaysia's scheme is the clean proof. Tenaga Nasional, the national utility, created what it called a Green Lane Pathway and cut connection timelines from thirty six months to twelve. It has also committed around RM43bn, about 10.8 billion US dollars, to modernising the grid specifically for data centre demand.

You do not build a programme to compress connection time unless connection time, rather than generation, was the thing stopping projects.

That is worth sitting with. The common assumption is that the constraint on data centres is electricity supply. In Johor it is not. Data centre load there more than doubled between 2024 and 2025 to roughly 3.8 gigawatts of maximum demand, which Wood Mackenzie notes is about one and a half times the state's own current electricity demand. Generation capacity remains sufficient across the system. Access to the wires is what decides whether a project proceeds.

So the first clock moved, and it moved a long way. Twenty four months came out of it.

## Why the second clock cannot

A large power transformer is not a product you order from a catalogue. It is designed for the site it will serve, wound from a great deal of copper, and built around a core of a specialist material called grain oriented electrical steel, which is made by a small number of mills worldwide and is not easily substituted.

Then it is tested, because a unit that fails in service takes the site with it. Then it is moved, and at this size moving it is a civil engineering job of its own involving road surveys and sometimes bridges.

None of those steps is inefficiency. Each is there because the alternative is a fire.

This is the difference that matters. The first clock is a policy variable, and a policy variable can be compressed by decision. The second is a manufacturing variable, and a manufacturing variable can only be compressed by building more factories, which itself takes years.

**Policy compression has a floor, and the floor is made of steel and copper.**

## What this means for a date on a slide

Announced capacity and energised capacity are not the same number, and the gap between them is where I think the mispricing sits.

An announcement is a decision. An energisation is a delivery. Between the two sits a queue whose faster half has already been optimised in the markets that care most, and whose slower half has not moved at all.

Singapore shows the same constraint from the other direction. Peak demand is projected to grow 3.7 to 5.7 per cent a year to between 10.1 and 11.8 gigawatts by 2030. The response has included a roughly twenty hectare low carbon data centre park on Jurong Island sized to 700 megawatts, and a capacity call requiring a power usage effectiveness of 1.25 or better, a measure of how much total electricity a site uses for every unit that reaches the computers.

Singapore is rationing connection by efficiency because it cannot ration it by supply. That is a regulator telling you which clock is binding.

Inside the Johor-Singapore Special Economic Zone, installed capacity stood at 3,885 megavolt amperes in December 2025, a rating called MVA that measures what the equipment can carry, against demand near 1,272 megawatts. The state's own published utilisation figure is 72.76 per cent.

Those two numbers divide to about 33 per cent, not 73, so the published rate cannot be measured against total installed capacity. My reading is that it is measured against capacity actually energised, while the 3,885 headline includes substations approved but not yet commissioned. I take that discrepancy apart properly in a later piece, because it is this whole argument happening inside an official statistic. Either way the headroom is comfortable today and narrowing quickly at the growth rate of the last two years.

## What would prove me wrong

The honest falsifier is that the first clock keeps winning.

If connection timelines keep compressing the way the Green Lane did, the premium on queue position decays fast and this becomes a two year dislocation rather than a structural one. I would also be wrong if transformer and high voltage cable lead times normalise faster than utility capital spending is committed, which would turn a bottleneck into a glut.

There is a second escape route I take seriously. Operators can build their own generation on site and skip the queue entirely. My position is that this relocates the constraint rather than removing it, because on site generation still needs transformers and switchgear and has its own waiting list. But that is the part of my own argument most likely to be wrong, and I would rather name it than have it pointed out to me.

So I watch four things: transformer and high voltage cable lead times, the Green Lane project count beyond thirty three, Johor-Singapore Special Economic Zone utilisation past 72.76 per cent, and who wins the Singapore capacity award, because the winner under a 1.25 ceiling tells you what the regulator now believes is buildable.

<section class="exposure">
<h3>Who is exposed if the transformer clock is the binding one</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The makers of the plant</dt>
<dd><span class="names">Hitachi Energy</span>, <span class="names">Siemens Energy</span> and <span class="names">GE Vernova</span> build large power transformers and the high voltage equipment around them.</dd>
<dt>The equipment around the transformer</dt>
<dd><span class="names">Schneider Electric</span> and <span class="names">Eaton</span> make switchgear, protection and distribution equipment for the site side of the connection.</dd>
<dt>The people who build the substation</dt>
<dd><span class="names">EGP Energy</span> is a Singapore electrical transmission and distribution contractor. <span class="names">Surbana Jurong</span> does energy and industrial engineering across the region.</dd>
<dt>The utility that sets the first clock</dt>
<dd><span class="names">Tenaga Nasional</span> operates the Malaysian grid and runs the connection scheme described above. <span class="names">SP Group</span> operates Singapore's.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Operators quoting announced megawatts rather than energised ones, since the distinction is rarely made cleanly in disclosure. Anyone whose delivery schedule assumes the policy half of the queue keeps compressing at the rate it did once.</dd>
</dl>
</section>

---

<p class="sources">Sources: Tenaga Nasional disclosures on the Green Lane Pathway and its grid investment programme, Wood Mackenzie on Johor data centre load, Malaysia's Johor-Singapore Special Economic Zone capacity and utilisation figures as at December 2025, and Singapore's Energy Market Authority, EDB and JTC on demand projections and the Jurong Island capacity call. Figures are as reported on the dates cited. The description of transformer manufacture is mechanism rather than a forecast, and I give no lead time figure because I have not verified one. Personal research, not investment advice.</p>
