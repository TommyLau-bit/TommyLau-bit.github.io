---
title: "Micron sells AI memory before the year starts, and each bit takes three times the wafer"
date: 2026-10-07T17:49:04+08:00
summary: "Micron, one of three companies that make the stacked memory beside AI chips, commits most of each year's supply of it before that year starts. By Micron's own account, each unit of it uses about three times the silicon of ordinary computer memory. So while AI memory grows faster than the rest, it takes silicon away from the ordinary memory in phones, laptops and servers, and keeps that short too."
category: "Analysis"
cover: "/covers/micron-three-times-the-wafer.svg"
tags: ["memory", "HBM", "supply-chain"]
draft: false
---

Here is a claim I am willing to be wrong about in public. The memory shortage inside AI chips and the one in your next laptop are the same shortage.

The link is Micron, the memory maker based in Boise, Idaho. It is one of three companies making HBM, high-bandwidth memory, the stacked memory beside the leading AI processors. SK Hynix and Samsung are the other two.

In [the piece on the memory wall](/journal/the-countertop-is-the-bottleneck/), I explained why AI chips need memory beside them. In [the map of who makes an Nvidia B200](/journal/nobody-makes-a-b200-alone/), I noted Micron had agreed its 2026 supply in advance. This piece asks what that memory takes away.

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

**Wafer.** The thin silicon disc, 300 millimetres across, on which hundreds of memory chips are made together. A memory maker's output is limited by how many wafers its cleanrooms, the dust-free halls where chips are made, can process.

**Trade ratio.** Micron's term for how many wafers of ordinary DRAM it gives up to make the same number of HBM bits. A bit is the smallest unit of stored data.

## Why HBM eats wafers

An HBM stack is a pile of DRAM chips, wired through their own silicon by vertical connections called through-silicon vias. Micron's HBM4 stacks twelve memory chips on a logic chip that talks to the processor, holding 36 gigabytes.

Micron gave three reasons for its appetite in December 2023. Across the industry, it said, an HBM3E memory chip was roughly twice the size of a DDR5 chip, the standard server memory, holding the same data.

Each stack also needs that extra logic chip at its base. And the stacking is complex enough to lower yields, the share of finished stacks that actually work.

That December, Micron put HBM at more than twice the wafer supply of DDR5 per bit. In March 2024 it called the industry-wide figure "approximately three times", and said the ratio for HBM4 would be "even higher".

In December 2025 Micron restated "the three to one trade ratio with DDR5", and said it "only increases with future generations". So three is a floor, not a ceiling.

## Sold before it is made

For 2025, 2026 and 2027, Micron had most of each year's HBM committed before the year started. In March 2024 it said its 2024 HBM was sold out and the "overwhelming majority" of its 2025 supply already allocated.

In December 2025 it said it had agreed price and volume for its whole calendar 2026 supply. On 30 September 2026 it said it had completed agreements for "the vast majority" of its calendar 2027 HBM bits.

The reason is qualification, the testing a customer runs before trusting a supplier's part. HBM is qualified for each accelerator it sits beside, which Micron calls "platform qualifications". In December 2023 it said it was in the final stages of qualifying its HBM3E for Nvidia's H200. In March 2024 it said the H200 would use it.

So a buyer cannot easily switch memory late. My inference is that the order is effectively placed when the accelerator is designed.

The price is fixed early too. Asked by an analyst from Cantor Fitzgerald when HBM prices would move closer to conventional DRAM's, Micron's chief executive, Sanjay Mehrotra, said "for 2026, our prices for HBM were negotiated with our customers last year."

## Where the squeeze shows up

If HBM takes wafers from ordinary DRAM, ordinary DRAM should be the tighter market. Micron's figures for fiscal 2026, its year to 3 September 2026, fit that.

In the fourth quarter, Micron's DRAM revenue, which includes HBM, was $39.8 billion, up 27 per cent on the quarter before. Bits shipped rose by a mid single digit percentage, while prices rose by a high teens percentage. Micron put the price rise down to "tight DRAM industry conditions".

Here is the surprise. Micron's own wording implies that HBM, priced a year earlier, has been the less profitable kind. It says its 2027 HBM prices carry significant increases, "narrowing the gross margin gap with conventional DRAM". Gross margin is the share of each sale left after the cost of making it.

My reading is that ordinary memory, sold nearer today's price, felt the shortage first. HBM catches up only as each new year's contracts are signed.

That sits alongside my memory wall piece, which called HBM priced like a luxury. Per bit it still costs far more. But by Micron's account its margin lagged ordinary DRAM in 2026, because its prices were fixed a year early.

SK Hynix describes the same pull. In its results release of 29 July 2026 it said demand for AI memory and conventional memory is "expanding in tandem", in a market where customer demand "exceeds supply capabilities".

## Why the squeeze lasts

The lasting cure is more cleanroom, and cleanrooms are slow. Micron's first new Idaho fab, ID1, is due to start wafer output in mid 2027, ID2 in late 2028, and its first New York fab in 2030.

Even then, Micron says, new output becomes meaningful only "a few quarters after initial output." SK Hynix's Yongin Phase 1 cleanroom opens in early 2027.

In June 2026 Micron listed what slows new fabs, from construction lead times and permitting to "the need for enhanced energy infrastructure". Memory waits on the same grid as everything else in this journal.

Asked whether new capacity or customers' cutbacks could ease the market by 2028, Mehrotra said HBM's next generations, "with the trade ratio that exists", create headwinds for supply growth. Micron expects industry HBM bits to grow faster than conventional DRAM through 2028. In June it said that growth, and a trade ratio rising with each generation, "further pressures non-HBM supply". That ordinary memory stays short through 2028 is my stronger reading, not Micron's wording.

An analyst from TD Cowen offered the obvious counter: if one large customer used less HBM, would its wafers returning to ordinary DRAM add much supply?

Mehrotra did not answer the wafer part directly. He said HBM demand would outpace the industry in 2027 and 2028. That is Micron's forecast, not proof, and it marks where my claim is weakest.


## What would prove me wrong

My claim has two halves, and Micron's own results and calls test both through calendar 2028.

The first half, sold before the year starts, fails if, by its fiscal first quarter 2028 results around December 2027, Micron has not said most of its calendar 2028 HBM supply is agreed. It usually says so between September and December. It also fails if Micron reports unsold HBM, or cuts HBM output, and itself blames customer demand.

The second half, the squeeze, fails if Micron stops expecting the DRAM industry to be supply-constrained in 2027 or 2028, while still expecting HBM bits to outgrow conventional DRAM. It also fails if Micron puts any current HBM generation below about three times the wafer of DDR5 per bit.

A shortage prolonged by late cleanrooms supports the claim rather than breaking it. Two things could blur the test. Micron's multi-year take-or-pay agreements, where customers pay for committed volumes whether or not they take them, now cover ordinary memory too.

And if chip designers cut HBM per chip, the squeeze would ease for a reason my claim allows. I will say so if it happens.

So I watch next year's HBM agreements each autumn, Micron's DRAM outlook, any new HBM4 trade ratio, and whether ID1 starts in mid 2027.

<section class="exposure">
<h3>Who is exposed if HBM keeps taking wafers from ordinary memory</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are Micron's own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
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

<p class="sources">Sources: Micron earnings call prepared remarks of 20 December 2023, 17 December 2025, 24 June 2026 and 30 September 2026, and its calls of 20 March 2024 and 30 September 2026. Micron fourth quarter and fiscal 2026 results, 30 September 2026, filed on Form 8-K. Micron HBM4 product page. SK Hynix second quarter 2026 results, 29 July 2026. Figures are as reported on the dates cited, with call quotes as transcribed or reported. Personal research, not investment advice.</p>
