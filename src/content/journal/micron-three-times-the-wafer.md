---
title: "Micron sells AI memory before the year starts, and each bit takes three times the wafer"
date: 2026-10-07T17:49:04+08:00
summary: "Micron, one of three companies that make the stacked memory beside AI chips, commits most of each year's supply of it before that year starts. By Micron's own account, each unit of it uses about three times the silicon of ordinary computer memory. So while AI memory grows faster than the rest, it takes silicon away from the ordinary memory in phones, laptops and servers, and keeps that short too."
category: "Analysis"
cover: "/covers/micron-three-times-the-wafer.svg"
tags: ["memory", "HBM", "supply-chain"]
draft: false
updated: 2026-10-08T16:00:00+08:00
updateNote: "Shortened and made plainer on 8 October 2026. The claim and the test of it are unchanged."
---

Here is a claim I am willing to be wrong about in public. The memory shortage inside AI chips and the one in your next laptop are the same shortage.

The link is Micron, the memory maker based in Boise, Idaho. It is one of three companies making HBM, high-bandwidth memory, the stacked memory beside the leading AI processors. SK Hynix and Samsung are the other two.

In [the piece on the memory wall](/journal/the-countertop-is-the-bottleneck/), I explained why AI chips need memory beside them. In [the map of who makes Nvidia's flagship AI chip](/journal/nobody-makes-a-b200-alone/), I noted Micron had agreed its 2026 supply before the year began. This piece asks what that memory takes away.

The answer is silicon wafers. Micron says HBM uses about three times the wafer of ordinary memory to store the same amount of data.

Micron sells most of each year's HBM before the year starts, and every wafer that goes into HBM is a wafer ordinary memory goes without.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a home baker with one oven. She bakes everyday loaves, and she also bakes tiered wedding cakes.</p>
<p>A wedding cake takes three trays of oven time for the same weight as one tray of bread, because it is built in layers and some layers come out cracked. Couples also book their cake a year ahead, at a price agreed on the day.</p>
<p>So every year the cake orders grow, there is less oven left for bread, and the bread queue lengthens. A second oven would fix it, but building one takes years.</p>
<p>Micron is that baker. The cake is HBM, the bread is ordinary memory, and the oven is its factories.</p>
</details>

## Three words you need

**DRAM.** Dynamic random access memory, the working memory in every phone, laptop and server. HBM is DRAM too, made from the same kind of memory chip in the same factories.

**Wafer.** The thin silicon disc on which hundreds of memory chips are made together. A memory maker's output is limited by how many wafers its cleanrooms, the dust-free halls where chips are made, can process.

**Trade ratio.** Micron's term for how many wafers of ordinary DRAM it gives up to make the same amount of HBM. It is measured in bits, the smallest unit of stored data.

## Why HBM eats wafers

An HBM stack is a pile of DRAM chips, wired together through their own silicon by tiny vertical connections. The pile sits on a logic chip that talks to the processor.

Micron gives three reasons the stack is so hungry. First, an HBM memory chip is roughly twice the size of a DDR5 chip, the standard server memory, holding the same data.

Second, each stack needs that extra logic chip at its base. Third, the stacking is complex enough to lower yields, the share of finished stacks that actually work.

Put together, Micron calls it "the three to one trade ratio with DDR5". It says the ratio "only increases with future generations". So three is a floor, not a ceiling.

## Sold before it is made

For three years running, Micron has had most of each year's HBM committed before that year started. This autumn it said it had agreements for "the vast majority" of its HBM for next year.

The reason is qualification, the testing a customer runs before trusting a supplier's part. HBM is tested and approved separately for each AI processor it sits beside.

So a buyer cannot easily switch memory late. My inference is that the order is effectively placed when the processor is designed.

The price is fixed early too. Asked when HBM prices would move closer to ordinary memory, Sanjay Mehrotra, Micron's chief executive, said "for 2026, our prices for HBM were negotiated with our customers last year."

## Where the squeeze shows up

If HBM takes wafers from ordinary DRAM, ordinary DRAM should be the tighter market. Micron's latest figures fit that.

Its DRAM prices rose sharply over the past quarter while the amount it shipped rose only a little. Micron put the price rise down to "tight DRAM industry conditions".

Here is the surprise. Micron's own wording implies that HBM, priced a year earlier, has lately been the less profitable kind. It says next year's HBM prices are rising enough to narrow the gap in gross margin, the share of each sale left after the cost of making it.

My reading is that ordinary memory, sold nearer today's price, felt the shortage first. HBM is still far dearer per bit, but it catches up only as each new year's contracts are signed.

SK Hynix describes the same pull. It says demand for AI memory and ordinary memory is "expanding in tandem", in a market where demand outruns what makers can supply.

## Why the squeeze lasts

The lasting cure is more cleanroom, and cleanrooms are slow. Micron's first new fab in Idaho, called ID1, is due to start output in mid 2027, with more sites to follow.

Among the things slowing new fabs, Micron lists building times, permits and "the need for enhanced energy infrastructure". Memory waits on the same grid as everything else in this journal.

Micron expects HBM across the industry to keep growing faster than ordinary memory, and a rising trade ratio to keep squeezing everything else. That ordinary memory stays short for years is my stronger reading, not Micron's wording.

An analyst asked the obvious question: if one large customer used less HBM, would its wafers returning to ordinary memory add much supply? Mehrotra did not answer that part directly. He said HBM demand would outpace the industry for the next two years. That is Micron's forecast, not proof, and it marks where my claim is weakest.

## What would prove me wrong

My claim has two halves, and Micron's own results and calls test both through calendar 2028.

The first half, sold before the year starts, fails if, by its fiscal first quarter 2028 results around December 2027, Micron has not said most of its calendar 2028 HBM is agreed. It also fails if Micron reports unsold HBM, or cuts HBM output, and itself blames customer demand.

The second half, the squeeze, fails if Micron stops expecting DRAM to be short across the industry in 2027 or 2028, while still expecting HBM to outgrow ordinary DRAM. It also fails if Micron puts any current HBM generation below about three times the wafer of DDR5 for each bit.

A shortage made longer by late cleanrooms supports the claim rather than breaking it. And if chip designers cut the HBM on each chip, the squeeze would ease for a reason my claim allows. I will say so if it happens.

So I watch next year's HBM agreements each autumn, Micron's view of the DRAM market, and whether ID1 starts on time.

<section class="exposure">
<h3>Who is exposed if HBM keeps taking wafers from ordinary memory</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Where this piece draws on Micron's own disclosures, they are used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Micron</span> makes DRAM, including HBM, and NAND flash, the memory inside solid-state drives.</dd>
<dt>The other HBM makers</dt>
<dd><span class="names">SK Hynix</span> makes DRAM, HBM and NAND flash. <span class="names">Samsung</span> makes DRAM, HBM and NAND flash, alongside logic chips and phones.</dd>
<dt>The chips HBM sits beside</dt>
<dd><span class="names">Nvidia</span> designs AI accelerators that carry stacks of HBM from all three makers.</dd>
<dt>The packager</dt>
<dd><span class="names">TSMC</span> joins AI processors and their HBM on one base in its CoWoS packaging.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Makers of phones, laptops and servers buying ordinary DRAM while HBM takes the wafers. AI chip designers wanting to change memory late. And Micron's own case, if HBM demand slows and wafers flow back to ordinary memory.</dd>
</dl>
</section>

---

<p class="sources">Sources: Micron earnings call prepared remarks of 20 December 2023, 17 December 2025, 24 June 2026 and 30 September 2026, and its calls of 20 March 2024 and 30 September 2026. Micron fourth quarter and fiscal 2026 results, 30 September 2026, filed on Form 8-K. SK Hynix second quarter 2026 results, 29 July 2026. Figures are as reported on the dates cited, with call quotes as transcribed or reported. Personal research, not investment advice.</p>
