---
title: "Google lets the grid slow its AI chips when power runs short"
date: 2026-10-29T17:54:38+08:00
summary: "Google says it has deals with five American power companies that let them ask it to use less electricity at the busiest hours. It does that by holding back or slowing some of its AI computing, not by building anything new. I think that makes the AI chip the quickest spare power a crowded grid can add, and I expect a power company to connect a large data centre on that promise by the end of 2027."
category: "Analysis"
cover: "/covers/google-lets-the-grid-slow-its-chips.svg"
tags: ["grid", "power", "data-centres"]
draft: true
---

In August 2025, Google announced two utility deals of a new kind. Indiana Michigan Power and the Tennessee Valley Authority could ask it to use less power at peak, and Google would answer by reducing or shifting its AI work.

By March this year, Google said such deals covered one gigawatt across five utilities.

No new machine is bought for the job. The computers that make the demand are the ones asked to give it back.

The quickest spare power a stressed grid can add is now Google's own AI chips, slowed on request.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture a house whose fuse trips if the oven, kettle and heater all run at teatime. You could rewire the street, which takes years, or buy a generator for the garage.</p>
<p>Or you press delay start on the washing machine and dishwasher. The clothes still get washed, at midnight instead. The quickest fix on the street is the machine that agreed to wait.</p>
</details>

## How slowing a chip frees up the grid

Machine learning, the work of training and running AI models, is mostly chips doing arithmetic. Google says only that it will reduce or shift that work at peak; its contract terms are confidential. Published tests show how it can be done. Software caps how much power each chip may draw, so it runs slower, and holds back work with no deadline today until the peak passes.

That moves energy in time rather than saving it. The delayed work still gets done later, when the wires have room.

A utility wants this because its lines and substations are sized for the hottest hour of the year. A site that promises to shrink in that hour needs less new wire. New lines take years to permit and build, and the [transformers behind them wait years too](/journal/siemens-energy-measures-the-shortage/). A promise kept in software is capacity that can arrive this year.

It is not a [battery bought as connection equipment](/journal/what-the-battery-is-really-for/), and it is not the grid [pulling the plug](/journal/ercot-rations-the-plug/). The chip itself is the resource, and Google chooses which work slows.

The promise is checked. Indiana's regulator approved a contract under which Google earns credits for taking part, with compliance standards and penalties for missed cuts.

## What the tests and the regulators show

Google keeps the size of each cut confidential, so the clearest public test ran elsewhere. At an Oracle data centre in Phoenix, Emerald AI's software cut the power of 256 Nvidia chips by 25 per cent for three hours at peak, with no battery, while agreed performance held. The study appeared in Nature Energy.

Regulators are making room. In June 2026, federal regulators told the six regional grid operators they oversee to justify or reform their rules for large loads. For PJM, the largest, they said its rules appeared to lack a service for sites willing to limit their draw.

In September, Google, Nvidia and Emerald AI formed an alliance asking for faster connections in return for flexibility that can be checked.

## What would prove me wrong

I am wrong if, by 31 December 2027, no US utility or grid operator has publicly approved a data centre connection of 100 megawatts or more, at a Google site or anyone's, whose peak cut is stated to come from slowing or deferring computing, with no battery or generator counted towards it.

A utility's backup right to trip the site if the software fails is allowed. A cut delivered by the utility opening the switch is not. Then the grid trusts the plug, not the chip.

<section class="exposure">
<h3>Who is exposed if the grid counts the AI chip as spare power</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Google</span> runs data centres and designs its own AI chips.</dd>
<dt>The slowing</dt>
<dd><span class="names">Emerald AI</span> makes software that fits AI work to grid requests. <span class="names">Nvidia</span> makes AI chips and data centre systems.</dd>
<dt>The buyers of the cut</dt>
<dd><span class="names">Indiana Michigan Power</span>, <span class="names">Tennessee Valley Authority</span>, <span class="names">Entergy Arkansas</span>, <span class="names">Minnesota Power</span> and <span class="names">DTE Energy</span> are Google's demand response utilities.</dd>
<dt>The trial hosts</dt>
<dd><span class="names">Oracle</span> and <span class="names">Nebius</span> run data centres. <span class="names">National Grid</span> owns high-voltage networks in England, Wales and the US.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Batteries and generators sold as connection equipment, if software does the job, and AI customers whose work slows at peak.</dd>
</dl>
</section>

---

<p class="sources">Sources: Google's announcements of 4 August 2025 and 19 March 2026, the Indiana regulator's order in Cause 46276 of April 2026, the Phoenix study in Nature Energy, FERC's orders of 18 June 2026 and Nvidia's announcement of 16 September 2026, with the lead from a YouTube video by Leo Cui. Personal research, not investment advice.</p>
