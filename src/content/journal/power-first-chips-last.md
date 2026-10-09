---
title: "Jane Street now commits to the power first and picks the chips last"
date: 2026-09-25T14:00:00+08:00
summary: "You might expect an AI buildout to start with the chips, but at Jane Street it now starts with the building, the power and the cooling, because those take more than a year to arrive. The firm even kept backup generators to the core of a site, rather than the whole building, to switch its chips on six months sooner."
category: "Analysis"
cover: "/covers/power-first-chips-last.svg"
tags: ["power", "grid", "data-centres"]
draft: false
---

Here is a claim I am willing to be wrong about: the order in which a company commits its money tells you what is scarce.

Most people picture an AI buildout starting with the chips. Jane Street's head of physical engineering, Dan Pontecorvo, describes the opposite order.

Speaking on a podcast recorded at the firm's Texas site, he said the infrastructure can take more than a year to arrive. So the building, the power and the cooling are settled before the chip order is placed.

At Jane Street, chips are now the last decision, because they are the quickest thing to buy.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Planning a wedding, you book the venue first, often more than a year ahead, before you know the guest list or the menu. Good venues go years out, and a caterer can be found in weeks.</p>
<p>You might book a room slightly too big, because the alternative is no room at all. The building and power are Jane Street's venue. The chips are the cake, ordered last.</p>
</details>

## Why the order flipped

Pontecorvo names the slow parts plainly: generators, transformers and some liquid cooling equipment. A chip order placed today arrives far sooner than a large transformer, the grey box that steps grid voltage down to a usable level.

Different chips also need different buildings. In his example, Google's TPUs, its own AI chips, run on cooler water and are about half as dense as Nvidia's GB300 NVL72 rack. So Jane Street commits to a site early, holds slightly more power than it needs, designs for several possible chips and chooses once the building is nearly ready.

The slow parts stay slow because the list of them changes every few weeks, a sign of how tight supply is. The firm warehouses components that fit any site, and uses modular power and cooling, built off-site and shipped close to plug-and-play.

## The generator it chose not to buy

The sharpest evidence is about backup power. A data centre traditionally backs up everything with diesel generators, so the whole site rides through a grid failure.

But generators are among the longest-lead items a builder can order. Jane Street now backs up only the core of the system that needs it. The result, in Pontecorvo's words, was GPUs switched on six months faster.

He is candid that it may not be the best engineering decision. It is the best business decision. A training job can restart from its last saved point, so an outage costs hours, while waiting for a generator costs months.

## What would prove me wrong

I am wrong if chips become the longest wait again. If GPU supply tightens while transformer and generator lead times fall back to months, builders should return to ordering chips first.

I am also wrong if dropping full generator backup proves to be a false saving. If outages cost far more than the months saved, operators will quietly put the generators back.

<section class="exposure">
<h3>Who is exposed if power is committed first and chips last</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Apart from CoreWeave, none of the companies below is named by Jane Street as a supplier.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Jane Street</span> is a trading firm that builds and runs its own AI training sites.</dd>
<dt>The long-lead equipment</dt>
<dd><span class="names">Caterpillar</span>, <span class="names">Cummins</span> and <span class="names">Rolls-Royce</span> make generators. <span class="names">Hitachi Energy</span>, <span class="names">Siemens Energy</span> and <span class="names">GE Vernova</span> make transformers.</dd>
<dt>Modular power and capacity</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span> and <span class="names">Eaton</span> make prefabricated power and cooling modules. <span class="names">CoreWeave</span> rents GPU capacity, Jane Street among its customers.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Projects that order chips before securing power, and the habit of backing up every rack with a generator.</dd>
</dl>
</section>

---

<p class="sources">Sources: Jane Street's podcast conversation with Dwarkesh Patel, with Yaron Minsky and Dan Pontecorvo, published 21 May 2026, and CoreWeave's announcement of Jane Street's cloud agreement, 15 April 2026. Personal research, not investment advice.</p>
