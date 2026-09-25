---
title: "Jane Street's AI data hall has room to spare, and no power to fill it"
date: 2026-09-25T12:51:00+08:00
summary: "Jane Street is a trading firm, not a tech giant, yet it now runs its own AI training centre in Texas with 4,032 chips cooled by liquid. The most revealing thing on its tour is the empty floor. The building has space left over, because the electricity the utility agreed to supply runs out long before the room does."
category: "Explainer"
cover: "/covers/room-to-spare.svg"
tags: ["power", "cooling", "data-centres"]
draft: false
---

Twenty years ago, Jane Street's first computing cluster was six Dell boxes stacked at the end of a row of desks. Once, a cleaner unplugged one of its trading systems while vacuuming.

In May 2026 the firm published a tour of its new AI training site in Texas. It holds 4,032 Nvidia GPUs, the chips that do AI maths, in 56 racks, and nearly all the heat leaves through liquid.

Jane Street is a trading firm, not a cloud company. It trains its own models, some of them large language models and some built around trading data. So it has had to learn the same physics as the tech giants, in a building that was never designed for it.

The most revealing thing in the tour is not the chips. It is the empty floor.

Jane Street has more room than it can use. What it cannot get more of is power.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A caravan pitch comes with an electric hook-up rated for a fixed amount of current. Switch on the kettle and the heater together and the trip switch clicks, and everything goes dark.</p>
<p>A bigger pitch does not help. You could have room for three caravans and still only run one kettle at a time, because the limit is the cable from the post, not the grass around it.</p>
<p>So the clever camper buys small, powerful appliances, packs them close to the post and watches the meter. Jane Street's data hall is that pitch, with a lot of spare grass.</p>
</details>

## Why the floor went quiet

The building was planned at what Jane Street's engineers call an intermediate point. The firm knew it had to grow a lot, but not what shape the coming computers would take.

The answer turned out to be dense. Each of its GB300 NVL72 cabinets, Nvidia's current rack of 72 GPUs, draws about 140 kilowatts at peak. A traditional air-cooled cabinet draws 10 to 40 kW.

The site runs on a fixed allocation of power from the utility. It is on the grid, not generating its own. So when each cabinet started drawing three to fourteen times as much, the same megawatts filled a fraction of the room.

The rest of the hall sits empty. The engineers joke that it left space for a podcast studio.

Their own summary is the whole story. The part of the site holding computers keeps shrinking, and the part supporting them keeps growing. Transformers, chillers and pipework now take the room the servers gave up.

## Putting water where water was forbidden

Data centres spent decades keeping water away from servers. Jane Street now pipes it onto the chips on purpose, in a hall built for air.

About 85 to 90 per cent of each server's heat leaves through cold plates, metal blocks with liquid channels sitting directly on the GPUs. Each server slides into the rack and clicks onto its coolant supply, coolant return and power in one movement. Around 15 per cent of the cabinets are still air-cooled.

Chillers on the roof send down water at about 18°C. Valves with ultrasonic flow meters give each cabinet exactly the flow its heat needs, so the racks at the end of a row are not starved.

That water never touches the chips. A heat exchanger, which passes heat between two loops without mixing them, hands it to a sealed technical loop. That loop is filtered to 25 microns, about a third of the width of a hair, so nothing clogs the cold plates. It carries 25 per cent propylene glycol, an antifreeze, because bacteria growing inside it could block the plates.

Leaks are handled in layers. Sensing ropes under the raised floor detect drips, valves isolate a section, and large buffer tanks store cold water. Those tanks keep the GPUs cool for the minutes the chillers need to restart after a power cut.

## Why power is harder to move than water

The engineers draw a sharp distinction here. Cooling is flexible: the same water feeds the air units and the liquid racks, and oversized pipes let it be moved wherever it is needed.

Power is not. It reaches the racks through busway, metal power rails overhead, fed from breaker panels. Every rail and every breaker has a hard current limit. Load one too heavily and the breaker trips.

So Jane Street deliberately built more distribution than its power supply can fill. That lets it move load between rows, growing GPUs in one place and ordinary processors in another, without new wiring. The ceiling stays fixed. Only the layout under it can change.

The risk is oversubscription, promising the racks more than the supply could deliver if all of them peaked at once. An operator plans on being 10 per cent over and finds the real figure is 15 or 20. A tripped breaker in the middle of a training run sends the job back to its last saved checkpoint.

## Running close to the edge on purpose

Why take that risk at all? Because an idle GPU is the most expensive thing in the building.

Jane Street's technology co-head Yaron Minsky puts it plainly: the opportunity cost tends to dominate the hardware cost, even though the hardware is not cheap. New compute takes a long time to arrive. Inside the firm, teams end up bidding against each other for the same machines.

So the firm runs as close to its power limit as it safely can. Its own monitoring software reads the breakers, understands which racks sit on which rails, and can shut down individual machines before a breaker trips.

Nvidia is attacking the same problem inside the rack. The GB300's power shelves carry banks of capacitors that store energy when demand dips and release it during spikes. Nvidia says this cuts the rack's peak draw from the grid by up to 30 per cent. It is the same smoothing, one layer down.

## What one trading firm tells us about everyone

Jane Street matters here because it is not a hyperscaler, the industry's term for the giant cloud companies. It is a firm that decided it needed its own AI factory, and it met the same wall they did.

The chips arrived. The floor was there. The cooling could be retrofitted. The fixed number was the power the utility had agreed to supply, and every engineering choice in the tour bends around it.

That is the argument I have made about the grid queue, seen from inside one building. The wait for a new connection sets the size of the site, and nothing inside the walls can change it.

There is a limit to what I can say. The tour does not give the site's megawatts, who owns the building or who supplied the equipment, so I do not claim any of those.

<section class="exposure">
<h3>Who is exposed if power, not floor space, sets the limit</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The tour does not name Jane Street's suppliers, and none of the companies below is claimed to be one.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Jane Street</span> is a trading firm that builds and runs its own AI training clusters.</dd>
<dt>The rack</dt>
<dd><span class="names">Nvidia</span> designs the GB300 NVL72 rack. <span class="names">LITEON</span> builds power shelves with built-in energy storage for it.</dd>
<dt>Liquid cooling</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span>, <span class="names">nVent</span> and <span class="names">CoolIT</span> make coolant distribution units, cold plates and liquid loops.</dd>
<dt>Power distribution</dt>
<dd><span class="names">Eaton</span>, <span class="names">Schneider Electric</span>, <span class="names">ABB</span> and <span class="names">Vertiv</span> make busway, breaker panels, switchgear and uninterruptible power supplies.</dd>
<dt>Chillers</dt>
<dd><span class="names">Trane</span>, <span class="names">Carrier</span> and <span class="names">Johnson Controls</span> make the rooftop chillers and air handlers that reject heat from the building.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone who sells or values data centre space by the square metre rather than by the megawatt. And older halls with plenty of floor but no spare power, whose space is now the least scarce thing they own.</dd>
</dl>
</section>

---

<p class="sources">Sources: Jane Street's video tour of its latest AI data centre with the podcaster Dwarkesh Patel, published on Jane Street's YouTube channel on 15 May 2026, for the site's GPU count, rack power, cooling design, power distribution and the engineers' descriptions of how they run it. Nvidia developer blog on GB300 NVL72 power smoothing, 2025, for the capacitor energy storage and the reduction in peak grid draw. Figures are as stated by the companies on the dates cited. Personal research, not investment advice.</p>
