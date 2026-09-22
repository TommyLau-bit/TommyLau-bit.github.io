---
title: "The queue, not the chip, is what's holding AI back"
date: 2026-07-27
summary: "Everyone watches the chip supply. Almost nobody watches the queue to plug a data centre into the grid. But a chip order arrives in months, and a substation takes years. The scarce thing is a finished connection to the wires, and it isn't priced like it's scarce."
category: "Analysis"
cover: "/covers/queue.svg"
tags: ["power", "grid", "johor", "singapore"]
---

Here is a claim I am willing to be wrong about in public: the thing holding back the AI buildout is not the chip. It is the wire.

Over the last year, the gating item for a new data centre has quietly moved from "is there enough electricity generated" to "can I physically connect to it." Power exists. Wires, substations, transformers and a place in the connection queue do not, or not on the timeline anyone wants.

I care about this because it is the one part of AI where physics sets the clock and the evidence sits in public documents rather than rumours from a supply chain. You can check it.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine you have bought every brick, tile and window for a new house, and hired the builders. Then the council tells you the connection to the water main will take four years.</p>
<p>The bricks were never the problem. But everyone is watching brick prices, because bricks are what you can see and count.</p>
<p>That is the AI buildout right now. The chips arrive in months. The connection to the electricity grid, the substation and the transformer that feeds it, takes years. And almost nobody is watching that queue.</p>
</details>

## Two places that show it clearly

**Johor** is the cleanest example. Data centre load there more than doubled between 2024 and 2025 and reached roughly 3.8 gigawatts of maximum demand, which is around one and a half times the entire state's own current electricity use. Generation capacity is sufficient system-wide. What now decides whether a project goes ahead is access to transmission and distribution: the wires. Inside the Johor-Singapore Special Economic Zone, installed capacity of 3,885 MVA sat against demand near 1,272 MW in December 2025. The published utilisation figure is 72.76 per cent, which is worth pausing on, because those two numbers divide to about 33 per cent. The likely explanation is that the published rate is measured against energised capacity while the headline includes substations not yet commissioned. Comfortable today on either reading. At the growth rate of the last two years, not for long.

The utility's own behaviour is the strongest evidence. Tenaga Nasional has committed RM43 billion, about US$10.8 billion, to modernise the grid specifically for data centre demand, and its Green Lane Pathway cut new connection timelines from 36 months to 12, delivering 33 projects under that scheme by March 2026. You do not build a programme to compress connection time unless connection time, not generation, was the thing stopping projects.

**Singapore** tells the same story from the other side. Peak demand is projected to grow by 3.7 to 5.7 per cent a year to somewhere between 10.1 and 11.8 gigawatts by 2030. The response has included a roughly 20-hectare low-carbon data centre park on Jurong Island sized to 700 MW, and a capacity award that requires a power-efficiency score of 1.25 or better. Singapore is rationing connection by efficiency because it cannot ration it by supply.

## Why the market still treats it as a chip problem

A GPU order clears in months. A substation, its transformer and its queue slot clear in years, and the transformer is itself in short supply globally.

That mismatch means "announced megawatts" has become a poor guide to "deliverable megawatts." The gap shows up late and unglamorously, as commissioning dates that slip and revenue that arrives a quarter or two after it was promised.

And there is an asymmetry of attention. Chip supply is tracked weekly by a large community of analysts. Connection queues are tracked by very few people with money at risk. That is where I think the mispricing sits, and it is why a reading of the power and grid layer is worth something alongside a reading of the silicon, not instead of it.

## Where the value goes if I'm right

Three places.

First, the equipment that clears the queue: high-voltage transformers, cable, switchgear and the contractors who build substations. Their order books already stretch past the spending cycle that funds them.

Second, operators who hold energised or queue-secured capacity, which ought to be worth more than peers quoting announced capacity, a distinction that company disclosures rarely make cleanly.

Third, batteries, which are quietly becoming a connection product rather than only a trading product. US utility-scale battery additions are expected at 24 GW in 2026 against 15 GW in 2025, with Texas alone around 12.9 GW, more than half the national total, sited against data centre load that the Texas grid operator projects near 35 GW of peak demand by 2035. A battery that lets a campus switch on ahead of its wires is worth more than the money it makes buying cheap and selling dear.

## What would prove me wrong

The honest counter-argument is Tenaga's own success. If connection timelines keep compressing the way the Green Lane did, from 36 months to 12, then the premium on queue position fades fast and this becomes a two-year dislocation rather than a structural one. I would also be wrong if transformer and high-voltage cable lead times normalise faster than utilities commit capital, which would turn a bottleneck into a glut.

So I watch four things: transformer and cable lead times, the Green Lane project count beyond 33, utilisation in the Johor-Singapore zone past 73 per cent, and who wins the Singapore capacity award, because who gets 200 MW under a strict efficiency ceiling tells you what the regulator now believes is buildable.

<section class="exposure">
<h3>Who is exposed if the connection is the bottleneck</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The equipment that clears the queue</dt>
<dd>High-voltage transformers, switchgear and grid connection kit: <span class="names">Hitachi Energy, Siemens Energy, GE Vernova, Schneider Electric, Eaton, ABB</span>. Cable: <span class="names">Prysmian, Nexans, NKT</span>. These order books already stretch past the spending cycle that funds them.</dd>
<dt>Operators holding energised capacity</dt>
<dd>Campuses already connected are worth more than campuses that are merely announced: <span class="names">Equinix, Digital Realty, AirTrunk, Princeton Digital Group, STT GDC, Keppel Data Centres, Vantage</span>. Company disclosure rarely separates the two cleanly, which is where the mispricing hides.</dd>
<dt>Storage as a connection product</dt>
<dd>A battery that lets a campus switch on ahead of its wires is worth more than its trading spread: <span class="names">Fluence, Tesla Energy, Sungrow, CATL, BYD</span>.</dd>
<dt>The utilities doing the connecting</dt>
<dd>In this region specifically, <span class="names">Tenaga Nasional</span> in Malaysia, <span class="names">SP Group</span> in Singapore, and <span class="names">YTL Power</span> as a generator and developer.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Developers whose pipeline is announced but unenergised, and anyone whose revenue recognition depends on a commissioning date they do not control. The damage shows up late and quietly, as dates that slip by a quarter at a time.</dd>
</dl>
</section>

---

<p class="sources">Sources: Energy Market Authority, EDB and JTC, Tenaga Nasional disclosures, Wood Mackenzie, EIA and ERCOT, drawn from my own market notes on the Singapore-Johor power corridor (29 July 2026) and grid-scale battery storage (7 August 2026). Figures as reported on the dates cited. This is the plain-language version of a technical note I published on 15 August 2026. Personal research, not investment advice.</p>
