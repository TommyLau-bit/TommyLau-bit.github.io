---
title: "TSMC's chief says the AI bottleneck is its factories, not the power grid"
date: 2026-10-02T12:49:47+08:00
summary: "Almost every advanced AI chip, whoever designs it, is made by one company, TSMC, and its chief executive says those factories, not electricity, limit AI today. Its own numbers show why, since a new chip factory takes years to build and more years to fill, and that changes how long I think the chip side of the shortage lasts."
category: "Analysis"
cover: "/covers/tsmc-says-it-is-the-bottleneck.svg"
tags: ["the-stack", "data-centres", "supply-chain"]
draft: false
---

This journal has argued for months that the thing holding back AI is not the chip. It is the wire and the [queue to connect to the grid](/journal/the-queue-not-the-chip/).

In January 2026 the company that makes almost every AI chip disagreed in public. Asked whether power was the limit, TSMC's chief executive C.C. Wei said not yet. The bottleneck was TSMC's own wafer supply.

That deserves a fair hearing. TSMC is where Nvidia, Google, Amazon, AMD and Broadcom all queue for the same factories.

On today's horizon, TSMC is right: its factories are the bottleneck.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine every famous restaurant in a city designs its own dishes, but all of them send the cooking to one shared kitchen that nobody else can match.</p>
<p>When demand surges, they cannot simply hire another kitchen. A new one takes years to build, and more years before its cooks match the old ones. So the queue at that kitchen sets how fast every restaurant grows.</p>
</details>

## Why one company makes everyone's chips

TSMC is a foundry, a company that makes chips other companies design. Each new generation of manufacturing cost more, until only a company making chips for everyone could afford it. So rivals now share a supplier.

Its fabs, the factories where chips are made on thin silicon discs called wafers, cluster in Taiwan for a physical reason. Starting a new fab depends on copying settings, people and suppliers from one already working.

That is why supply cannot simply catch up. On the January call, Wei said a new fab takes two to three years to build. In April he added that ramping it to full output takes one to two years more. Money spent today mostly buys output for 2028 and 2029.

Packaging is tighter still. CoWoS, TSMC's name for the step that joins an AI processor to its stacked memory, is a separate factory step every leading AI chip needs.

## What TSMC itself says

In July Wei said TSMC's packaging capacity was so tight it was limiting its customers' growth. An AI chip that cannot be joined to its memory cannot ship.

TSMC's results point the same way. The part of its business making chips for AI and other heavy computing now brings in about two thirds of its sales, up from three fifths a year earlier.

A chip factory runs on a clock much closer to a substation's than to a chip's.

## What would prove me wrong

My claim is narrow. Today TSMC's factories bind before the grid does, but over the longer run I still expect the grid to be the slower clock.

I am wrong about today if TSMC's tightness eases while data centres with chips on order still wait for power. I am wrong about the longer run if TSMC still calls capacity tight in 2028 while grid connection waits shorten.

<section class="exposure">
<h3>Who is exposed if the factory, for now, is the bottleneck</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures are TSMC's own disclosures, used as evidence for the mechanism.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">TSMC</span> makes chips for other companies, including most AI accelerators, and the CoWoS packaging.</dd>
<dt>The designers in the queue</dt>
<dd><span class="names">Nvidia</span> and <span class="names">AMD</span> design AI accelerators. <span class="names">Broadcom</span> and <span class="names">Marvell</span> design custom AI chips.</dd>
<dt>Other foundries and packagers</dt>
<dd><span class="names">Samsung Foundry</span> and <span class="names">Intel Foundry</span> make advanced chips. <span class="names">ASE</span> and <span class="names">Amkor</span> package and test them.</dd>
<dt>The memory beside the chip</dt>
<dd><span class="names">SK Hynix</span>, <span class="names">Samsung</span> and <span class="names">Micron</span> make stacked memory.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>AI chip designers without a firm place in TSMC's queue, and data centre builders with power ready and no chips to fill it.</dd>
</dl>
</section>

---

<p class="sources">Sources: TSMC second quarter 2026 management report, 16 July 2026, and its earnings calls of 15 January, 16 April and 16 July 2026, where quotes are TSMC's management speaking. Personal research, not investment advice.</p>
