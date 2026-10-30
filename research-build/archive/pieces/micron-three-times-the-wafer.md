---
title: "Micron sells AI memory before the year starts, and each bit takes three times the wafer"
date: 2026-10-07T17:49:04+08:00
summary: "Micron, one of three makers of the stacked memory beside AI chips, sells most of each year's supply before that year starts, and by its own account each unit uses about three times the silicon of ordinary memory. So as AI memory grows, it takes silicon from the memory in phones, laptops and servers, and keeps that short too."
category: "Analysis"
cover: "/covers/micron-three-times-the-wafer.svg"
tags: ["memory", "HBM", "supply-chain"]
draft: false
---

Here is a claim I am willing to be wrong about in public. The memory shortage inside AI chips and the one in your next laptop are the same shortage.

The link is Micron, the memory maker based in Boise, Idaho. It is one of three companies making HBM, high-bandwidth memory, the stacked memory beside the leading AI processors.

Micron says HBM uses about three times the silicon wafer of ordinary memory to store the same data.

Micron sells most of each year's HBM before the year starts, and every wafer that goes into HBM is a wafer ordinary memory goes without.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a home baker with one oven. A tiered wedding cake takes three trays of oven time for the weight of one tray of bread, and couples book their cake a year ahead.</p>
<p>So every year the cake orders grow, there is less oven left for bread. A second oven would fix it, but building one takes years.</p>
</details>

## Why HBM eats wafers

HBM is DRAM, the working memory in every phone, laptop and server, made in the same factories. A memory maker's output is limited by how many wafers, the thin silicon discs chips are made on, its cleanrooms can process.

An HBM stack is a pile of DRAM chips wired together by tiny vertical connections, sitting on a logic chip that talks to the processor. Micron gives three reasons it is so hungry. Each HBM chip is roughly twice the size of a DDR5 chip, the standard server memory, holding the same data. Each stack needs that extra logic chip. And the stacking lowers yields, the share of finished stacks that work.

Micron calls the result "the three to one trade ratio with DDR5", restated in December 2025. It says the ratio "only increases with future generations".

The cure is more cleanroom, and cleanrooms are slow. Micron's first new fab in Idaho, ID1, is due to start output in mid 2027. Among the delays it lists building times, permits and "the need for enhanced energy infrastructure".

## Sold before it is made

For three years running, Micron has had most of each year's HBM committed before that year started. This autumn it said it had agreements for "the vast majority" of next year's.

The reason is qualification, the testing a customer runs before trusting a part. HBM is approved separately for each AI processor, so a buyer cannot easily switch late.

The squeeze shows in ordinary memory. Micron's DRAM prices rose sharply last quarter while the amount it shipped rose only a little, which it put down to "tight DRAM industry conditions".

## What would prove me wrong

My claim has two halves. The first, sold before the year starts, fails if, by its results around December 2027, Micron has not said most of its calendar 2028 HBM is agreed, or if it reports unsold HBM and blames customer demand.

The second, the squeeze, fails if, before the end of 2028, Micron stops expecting DRAM to be short while HBM still outgrows it. It also fails if Micron puts any current HBM generation below about three times the wafer of DDR5.

<section class="exposure">
<h3>Who is exposed if HBM keeps taking wafers from ordinary memory</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The figures are Micron's own disclosures, used as evidence for the mechanism.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Micron</span> makes DRAM, including HBM, and NAND flash for solid-state drives.</dd>
<dt>The other HBM makers</dt>
<dd><span class="names">SK Hynix</span> and <span class="names">Samsung</span> make DRAM, HBM and NAND flash.</dd>
<dt>The chips and the package</dt>
<dd><span class="names">Nvidia</span> designs AI accelerators carrying HBM. <span class="names">TSMC</span> joins processor and memory in its CoWoS packaging.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Makers of phones, laptops and servers buying ordinary DRAM, and Micron itself if HBM demand slows and wafers flow back.</dd>
</dl>
</section>

---

<p class="sources">Sources: Micron earnings calls and prepared remarks from December 2023 to 30 September 2026, and its fourth quarter fiscal 2026 results, 30 September 2026. Personal research, not investment advice.</p>
