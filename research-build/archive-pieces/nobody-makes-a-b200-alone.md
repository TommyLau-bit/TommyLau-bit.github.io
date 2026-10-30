---
title: "Nobody makes an Nvidia B200 alone, and the weak links are measured in years"
date: 2026-10-07T16:36:29+08:00
summary: "Nvidia's B200, one of the chips behind today's AI boom, is designed in California but built by dozens of companies in at least five countries. Some of those suppliers could be swapped out in months. Others would take years, because a replacement needs new factories or years of testing before anyone trusts it."
category: "Explainer"
cover: "/covers/nobody-makes-a-b200-alone.svg"
tags: ["the-stack", "supply-chain", "data-centres"]
draft: false
---

Pick up an Nvidia B200 and ask a simple question: who made it? The honest answer is nobody, not alone.

Nvidia designed it, but runs no chip factories. TSMC made its two slabs of logic, mostly in Taiwan, using machines only ASML in the Netherlands can build. Its memory comes from three makers, two of them South Korean.

The chip holds 208 billion transistors, according to Nvidia. So the useful question is not who makes each part.

The B200's real dependency is how long each part would take to replace.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a wedding cake. One baker designs it, but the flour, the eggs and the sugar flowers come from different shops. If the eggs run out, you buy eggs elsewhere tomorrow.</p>
<p>If the only shop that makes the sugar flowers closes, you wait while someone else learns, then test their flowers before trusting them. The suppliers that matter are the ones that would take longest to learn.</p>
</details>

## From blueprint to wafer

The finished design becomes masks, plates carrying the circuit pattern for one layer, made on blank plates from Japanese suppliers such as AGC and Hoya. Wafers, the thin silicon discs chips are made on, come largely from Shin-Etsu and SUMCO.

Lithography prints the pattern with light. The finest layers use extreme ultraviolet light, EUV, which ASML describes as unique to itself, bounced off mirrors made by ZEISS in Germany.

TSMC makes the dies, the single chips cut from a wafer, on a custom four nanometre process. Each die is as large as the factory's printing field allows, which is why there are two.

## Memory, the package and the rack

Beside the logic sit eight stacks of HBM, memory chips piled vertically. Nvidia names SK Hynix, Micron and Samsung as suppliers, and each maker's stacks must pass qualification, months of testing, for each chip.

TSMC's CoWoS packaging joins dies and memory on a slab of fine wiring, mounted on a substrate from makers such as Ibiden. Inside it is insulating film from Ajinomoto, whose new film plant will not operate until 2032.

In Nvidia's flagship rack, 72 Blackwell processors join through Nvidia's switch chips. Lasers, glass fibre, power chips and cold plates surround them, and Foxconn, Quanta and Wistron assemble the whole thing.

## The clock on each part

My own rough sort, by how long each supplier would take to replace, gives four groups.

**Swappable fastest.** Rack assembly, connectors and much of the power hardware, which several firms can do in months rather than years.

**A handful, each slow to qualify.** HBM, substrates, test equipment and photoresist, the light-sensitive coating lithography prints into. Each new part must be proven on each new chip.

**Short of capacity.** TSMC's fabs and packaging lines. Its chief has said a new fab takes two to three years to build and one to two more to fill.

**No second source at all.** EUV machines and their mirrors, with Ajinomoto's film close by. Replacing either is not a purchasing decision.

Nvidia's annual report shows the cost: lead times beyond twelve months, paid with deposits and long-term capacity commitments. The slowest links each have their own piece: [ASML](/journal/asml-booked-ahead/), [Ajinomoto](/journal/ajinomoto-grows-with-the-package/) and [Micron](/journal/micron-three-times-the-wafer/).

<section class="exposure">
<h3>Who operates at each stage of a B200</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Nvidia</span> designs the chip, licensing from <span class="names">Arm</span>.</dd>
<dt>Factory and tools</dt>
<dd><span class="names">TSMC</span> makes the dies. <span class="names">ASML</span>, <span class="names">ZEISS</span>, <span class="names">Trumpf</span>, <span class="names">Applied Materials, Lam Research, Tokyo Electron</span> and <span class="names">KLA</span> make tools.</dd>
<dt>Materials and memory</dt>
<dd><span class="names">Shin-Etsu</span>, <span class="names">SUMCO</span>, <span class="names">JSR</span>, <span class="names">Tokyo Ohka Kogyo</span>, <span class="names">AGC</span>, <span class="names">Hoya</span> and <span class="names">Ajinomoto</span> make materials. <span class="names">SK Hynix, Micron</span>, <span class="names">Samsung</span>, <span class="names">Ibiden</span>, <span class="names">Unimicron</span>, <span class="names">Advantest</span> and <span class="names">Teradyne</span> make memory, substrates and testers.</dd>
<dt>The rack</dt>
<dd><span class="names">Broadcom</span>, <span class="names">Marvell</span>, <span class="names">Coherent</span>, <span class="names">Lumentum</span>, <span class="names">Corning</span>, <span class="names">Texas Instruments, Infineon</span>, <span class="names">Monolithic Power</span> and <span class="names">Vertiv</span> make network, power and cooling parts. <span class="names">Foxconn, Quanta</span> and <span class="names">Wistron</span> assemble.</dd>
</dl>
<dl class="against">
<dt>Where I stop</dt>
<dd>One product's whole chain, so no loser. I hold no investment view on any.</dd>
</dl>
</section>

---

<p class="sources">Sources: Nvidia's Blackwell pages and its Form 10-K of 25 February 2026, TSMC earnings calls of 2026, ASML and ZEISS EUV pages, and Ajinomoto's release of 7 May 2026. Personal research, not investment advice.</p>
