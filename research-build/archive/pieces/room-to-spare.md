---
title: "Jane Street's AI data hall has room to spare, and no power to fill it"
date: 2026-09-25T13:59:00+08:00
summary: "Jane Street is a trading firm, not a tech giant, yet it now runs its own AI training centre in Texas with 4,032 chips cooled by liquid. The most revealing thing on its tour is the empty floor. The building has space left over, because the electricity the utility agreed to supply runs out long before the room does."
category: "Explainer"
cover: "/covers/room-to-spare.svg"
tags: ["power", "cooling", "data-centres"]
draft: false
---

Twenty years ago, Jane Street's first computing cluster was six Dell boxes at the end of a row of desks. A cleaner once unplugged a trading system while vacuuming.

In May 2026 the trading firm published a tour of its new AI training site in Texas. It holds 4,032 Nvidia GPUs, the chips that do AI maths, and most of their heat leaves through liquid.

The most revealing thing in the tour is not the chips. It is the empty floor.

Jane Street has more room than it can use. What it cannot get more of is power.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A caravan pitch comes with an electric hook-up rated for a fixed amount of current. Switch on the kettle and the heater together and the trip switch clicks.</p>
<p>A bigger pitch does not help. You could have room for three caravans and still run only one kettle, because the limit is the cable from the post, not the grass. Jane Street's data hall is that pitch, with a lot of spare grass.</p>
</details>

## Why the floor went quiet

Jane Street planned the building at what its engineers call an intermediate point. It knew it had to grow, but not what shape the coming computers would take.

The answer turned out to be dense. Each GB300 NVL72 cabinet, Nvidia's current flagship rack, draws about 140 kilowatts at peak. A traditional air-cooled cabinet draws 10 to 40 kW.

The site runs on a fixed allocation of power from the utility. So when each cabinet started drawing several times as much, the same megawatts filled only a fraction of the room. The engineers joke that the rest left space for a podcast studio.

Air cannot carry that much heat. About 85 to 90 per cent of each server's heat now leaves through cold plates, metal blocks with liquid channels sitting directly on the GPUs.

Cooling turned out to be the flexible part, because oversized pipes let water be moved wherever it is needed. Power is not flexible. It reaches the racks through busway, metal power rails overhead, and every rail and breaker has a hard current limit. Load one too heavily and the breaker trips.

## Running close to the edge

Jane Street's own write-up says the new racks use a small fraction of the space originally allotted for chips. The part of the site holding computers keeps shrinking, and the part supporting them keeps growing.

So the firm built more power distribution than its supply can fill, and runs as close to the limit as it safely can. Its technology co-head Yaron Minsky explains why: the opportunity cost of an idle GPU tends to dominate the hardware cost. Its own software reads the breakers and can shut down machines before one trips.

## The one fixed number

Jane Street is not a hyperscaler, the industry's term for the giant cloud companies. It met the same wall they did.

The chips arrived. The floor was there. The cooling could be retrofitted. The fixed number was the power the utility had agreed to supply, and every engineering choice in the tour bends around it.

That is [the grid queue](/journal/the-queue-not-the-chip/), seen from inside one building. The wait for a new connection sets the size of the site, and nothing inside the walls can change it.

<section class="exposure">
<h3>Who is exposed if power, not floor space, sets the limit</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The tour does not name Jane Street's suppliers, and none below is claimed to be one.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Jane Street</span> is a trading firm that builds and runs its own AI training clusters.</dd>
<dt>The rack</dt>
<dd><span class="names">Nvidia</span> designs the GB300 NVL72 rack. <span class="names">LITEON</span> makes power shelves for it.</dd>
<dt>Cooling and power inside the hall</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span>, <span class="names">nVent</span> and <span class="names">CoolIT</span> make liquid cooling. <span class="names">Eaton</span> and <span class="names">ABB</span> make busway and switchgear.</dd>
<dt>Chillers</dt>
<dd><span class="names">Trane</span>, <span class="names">Carrier</span> and <span class="names">Johnson Controls</span> make rooftop chillers.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone who values data centre space by the square metre rather than the megawatt, and older halls with floor to spare but no spare power.</dd>
</dl>
</section>

---

<p class="sources">Sources: Jane Street's video tour of its latest AI data centre with Dwarkesh Patel, 15 May 2026, with Yaron Minsky and Dan Pontecorvo, and Jane Street's own write-up of the site. Personal research, not investment advice.</p>
