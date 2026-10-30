---
title: "The queue, not the chip, is what's holding AI back"
date: 2026-07-27
summary: "Everyone watches the chip supply. Almost nobody watches the queue to plug a data centre into the grid. But a chip order arrives in months, and a substation takes years. The scarce thing is a finished connection to the wires, and it isn't priced like it's scarce."
category: "Analysis"
cover: "/covers/queue.svg"
tags: ["power", "grid", "johor", "singapore"]
---

Here is a claim I am willing to be wrong about in public: the thing holding back the AI buildout is not the chip.

Over the last year, the gating item for a new data centre has moved from "is there enough electricity" to "can I connect to it". Power exists. Wires, substations, transformers and a place in the connection queue do not, or not on time.

Johor and Singapore show it most clearly, and the evidence sits in public documents you can check.

The scarce thing is not the chip. It is the wire.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine you have bought every brick, tile and window for a new house, and hired the builders. Then the council tells you the connection to the water main will take four years.</p>
<p>The bricks were never the problem. But everyone watches brick prices, because bricks are what you can see and count.</p>
</details>

## Why the wire sets the clock

A data centre needs more than electricity being generated somewhere. It needs a substation, the yard where high-voltage power is stepped down, and a transformer feeding it, plus a slot in the utility's connection queue.

**Johor** is the cleanest example. Data centre load there more than doubled in a single year to about 3.8 gigawatts of maximum demand, around one and a half times the state's own electricity use. Generation is sufficient system-wide. What decides whether a project goes ahead is access to the wires.

**Singapore** tells the same story from the other side. It now awards capacity only to sites with a power-efficiency score of 1.25 or better. It is rationing connection by efficiency because it cannot ration it by supply.

Supply cannot simply catch up. A chip order clears in months, but a substation, its transformer and its queue slot clear in years, and transformers are short globally. So announced megawatts have become a poor guide to deliverable ones.

## What the utility's own behaviour says

The strongest evidence is what Tenaga Nasional, Malaysia's grid utility, chose to build. Its Green Lane Pathway cut new connection timelines from 36 months to 12, delivering 33 projects by March 2026.

You do not build a programme to compress connection time unless connection time, not generation, was the thing stopping projects.

Chip supply is tracked weekly by a crowd of analysts. Connection queues are tracked by very few. That is where I think the common picture goes wrong.

## What would prove me wrong

The honest counter-argument is Tenaga's own success. If connection waits keep shrinking the way the Green Lane cut them, from 36 months to 12, a place near the front of the queue stops mattering.

I would also be wrong if transformer and cable lead times normalise faster than utilities commit capital. That would turn a bottleneck into a glut.

<section class="exposure">
<h3>Who is exposed if the connection is the bottleneck</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The equipment that clears the queue</dt>
<dd>Transformers and switchgear: <span class="names">Hitachi Energy, Siemens Energy, GE Vernova, Schneider Electric, Eaton, ABB</span>. Cable: <span class="names">Prysmian, Nexans, NKT</span>.</dd>
<dt>Operators holding energised capacity</dt>
<dd><span class="names">Equinix, Digital Realty, AirTrunk, Princeton Digital Group, STT GDC, Keppel Data Centres, Vantage</span> run data centre campuses.</dd>
<dt>Storage and the utilities</dt>
<dd>Batteries: <span class="names">Fluence, Tesla Energy, Sungrow, CATL, BYD</span>. Grid and generation: <span class="names">Tenaga Nasional</span>, <span class="names">SP Group</span> and <span class="names">YTL Power</span>.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Developers whose pipeline is announced but unenergised, paid only once a site switches on, on a date they do not control.</dd>
</dl>
</section>

---

<p class="sources">Sources: Energy Market Authority, EDB and JTC, Tenaga Nasional disclosures, Wood Mackenzie, EIA and ERCOT, from my market notes on the Singapore-Johor power corridor (29 July 2026) and battery storage (7 August 2026). Personal research, not investment advice.</p>
