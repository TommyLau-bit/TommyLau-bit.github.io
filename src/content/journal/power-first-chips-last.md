---
title: "Jane Street now commits to the power first and picks the chips last"
date: 2026-09-25T13:59:00+08:00
summary: "You might expect an AI buildout to start with the chips. At Jane Street it now starts with the building, the power and the cooling, because those take more than a year to arrive and the chips do not. The firm even kept backup generators to the core of a site, rather than the whole building, to switch its chips on six months sooner."
category: "Analysis"
cover: "/covers/power-first-chips-last.svg"
tags: ["power", "grid", "data-centres"]
draft: false
---

Here is a claim I am willing to be wrong about: the order in which a company commits its money tells you what is scarce.

Most people picture an AI buildout starting with the chips. You buy the GPUs, then find somewhere to put them. Jane Street's head of physical engineering, Dan Pontecorvo, describes the opposite order.

Speaking on a podcast recorded at the firm's Texas site, he said the infrastructure can take more than a year to arrive. So the building, the power and the cooling are settled before the chip order is placed. The firm will even commit to a site early and delay the chip decision, holding slightly more power than it needs.

Chips used to be the thing everyone queued for. At Jane Street they are now the last decision, because they are the quickest thing to buy.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Planning a wedding, you book the venue first, often more than a year ahead. You do it before you know the guest list, the menu or the band, because good venues go years out and a caterer can be found in weeks.</p>
<p>You might book a room slightly too big, because the alternative is having no room at all. And if plans change, a venue date can be passed to another couple. A cake baked to your order cannot.</p>
<p>That is Jane Street's order of commitment. The building and power are the venue, booked early and resellable. The chips are the cake, ordered last.</p>
</details>

## Why the order flipped

Pontecorvo names the slow parts plainly: generators, transformers, and some of the equipment used for liquid cooling. He adds that the list changes every few weeks, which is itself a sign of how tight supply is.

Those items decide when a building can open. A chip order placed today arrives far sooner than a large transformer, the grey box that steps grid voltage down to a usable level.

There is a second reason to commit to the building early but the chips late. Different chips need different buildings. In Pontecorvo's example, Google's TPUs, its own AI chips, run on cooler water and are about half as dense as Nvidia's GB300 NVL72 rack. A hall designed tightly around one of them may not suit the other.

So the firm designs for several possible futures, then chooses the chip once the building is nearly ready. Pontecorvo also makes the point from the other side. Chip designers have to sell something that can be powered and cooled, because a one-megawatt rack is useless in a building that cannot feed it.

## The generator it chose not to buy

The sharpest example in the conversation is about backup power. Traditionally a data centre backs up everything with diesel generators, so the whole site can ride through a grid failure.

But generators are among the longest-lead items a builder can order. So Jane Street's team asked whether every rack really needed one. They now back up only the core of the system that needs that resilience, not the whole site. The result, in Pontecorvo's words, was GPUs switched on six months faster.

He is candid that it may not be the best engineering decision. It is the best business decision. My reading of the logic is that a training job can restart from its last saved checkpoint, so an outage costs hours of work. Six months of waiting for a generator costs six months.

This is the same trade I described in Bloom Energy's case. Paying for a less perfect answer that arrives sooner beats waiting for the ideal one.

The firm also changes how it buys. It warehouses components that fit any of its sites so they are ready when a project starts. The largest items cannot sit on a shelf, so it increasingly uses modular infrastructure, power and cooling built off-site and shipped close to plug-and-play.

## Why power pushes compute apart

Jane Street runs tens of thousands of GPUs today and expects to reach hundreds of thousands. Its technology co-head, Yaron Minsky, says it cannot put them all in one place, because no single building can get enough power.

For years the firm ran one big research data centre and one big storage cluster. That shortcut is gone. Compute now sits across many sites, and moving the vast amounts of data between them becomes a problem of its own.

Renting is part of the same answer. In April 2026 CoreWeave, which builds and operates GPU data centres, announced that Jane Street had committed about $6 billion to its cloud, with compute across multiple facilities. I read that as buying capacity that already has a building and a grid connection behind it.

Even the firm's smallest sites feel it. In the colocation halls beside the exchanges, where trading machines sit metres from the market, power and cooling limits are set by the host. Sometimes that means one GPU per rack, spread out, instead of a dense liquid-cooled cabinet.

## What would prove me wrong

My claim is that the order of commitment reveals the constraint, and right now the constraint is power and the equipment that delivers it. That can be tested.

I am wrong if chips become the longest wait again. If GPU allocation tightens while transformer and generator lead times fall back to months, builders should return to ordering chips first and fitting buildings around them.

I am also wrong if dropping full generator backup proves to be a false saving. If outages at sites like this cost far more than the months saved, operators will quietly put the generators back.

So I watch three things. Published lead times for transformers and generators. Whether Jane Street and others keep describing the building as the first decision. And whether partial backup spreads, or disappears after the first serious failure.

<section class="exposure">
<h3>Who is exposed if power is committed first and chips last</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Apart from CoreWeave, none of the companies below is named by Jane Street as a supplier.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Jane Street</span> is a trading firm that builds and runs its own AI training sites and rents further capacity.</dd>
<dt>The long-lead equipment</dt>
<dd><span class="names">Caterpillar</span>, <span class="names">Cummins</span> and <span class="names">Rolls-Royce</span> make backup generators. <span class="names">Hitachi Energy</span>, <span class="names">Siemens Energy</span> and <span class="names">GE Vernova</span> make large power transformers.</dd>
<dt>Modular power and cooling</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span> and <span class="names">Eaton</span> make prefabricated power and cooling modules built off-site and shipped ready to connect.</dd>
<dt>Capacity with a building behind it</dt>
<dd><span class="names">CoreWeave</span> builds and operates GPU data centres and rents their capacity to customers, Jane Street among them.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Projects that order chips before securing power, and buildings designed so tightly around one chip generation that the next cannot move in. And the old habit of backing up every rack with a generator, wherever waiting for that generator delays the whole site.</dd>
</dl>
</section>

---

<p class="sources">Sources: Jane Street's podcast conversation with Dwarkesh Patel, recorded at its Texas site with Yaron Minsky and Dan Pontecorvo, published on Jane Street's YouTube channel on 21 May 2026, for the order of commitment, the generator decision, the long-lead equipment, the multi-site shift and the GPU counts. CoreWeave's announcement of Jane Street's cloud agreement, 15 April 2026. Figures are as stated by the companies on the dates cited. Personal research, not investment advice.</p>
