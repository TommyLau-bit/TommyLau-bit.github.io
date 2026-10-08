---
title: "TSMC's chief says the AI bottleneck is its factories, not the power grid"
date: 2026-10-02T12:49:47+08:00
summary: "Almost every advanced AI chip, whoever designs it, is made by one company, TSMC, mostly in Taiwan. Its chief executive says those factories, not electricity, are what limits AI today, and the company's own numbers show why: a new chip factory takes years to build and more years to fill. That is a fair point, and it changes how long I think the chip side of the shortage lasts."
category: "Analysis"
cover: "/covers/tsmc-says-it-is-the-bottleneck.svg"
tags: ["the-stack", "data-centres", "supply-chain"]
draft: false
---

This journal has argued for months that the thing holding back AI is not the chip. It is the wire, the substation and the queue to connect to the grid.

In January 2026 the company that makes almost every AI chip disagreed in public. Asked on TSMC's earnings call whether power was the limit, chief executive C.C. Wei said not yet. The bottleneck, he said, was TSMC's own wafer supply.

That deserves a fair hearing rather than a reflex. TSMC is the one place where Nvidia, Google, Amazon, AMD and Broadcom all queue for the same factories.

And TSMC's own timetable shows a factory that runs on a clock much closer to a substation's than to a chip's.

On today's horizon, TSMC is right: its factories are the bottleneck.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine every famous restaurant in a city designs its own dishes, but all of them send the cooking to one shared kitchen. The kitchen is extraordinary, and nobody else can match its standards.</p>
<p>When demand surges, the restaurants cannot simply hire another kitchen. A new one takes years to build, and more years before the new cooks match the old ones dish for dish.</p>
<p>So the queue at the shared kitchen sets how fast every restaurant can grow, however good its menu is. That kitchen is TSMC.</p>
</details>

## Three words you need

**Foundry.** A company that makes chips other companies design. Nvidia, Apple, AMD and the cloud giants design. TSMC, the Taiwan Semiconductor Manufacturing Company, makes them.

**Fab.** Short for fabrication plant, the factory where chips are made on thin silicon discs called wafers. TSMC's largest sites are clusters of fabs built side by side.

**CoWoS.** TSMC's name for the advanced packaging that joins an AI processor to its stacked memory on one base. Every leading AI chip needs it, and it is a separate factory step.

## Why one company makes everyone's chips

Most chip companies stopped building their own factories long ago. Each new generation of manufacturing cost more, until only a company making chips for everyone could afford it.

TSMC's model was simple: give us your design, and we will make the best chips. The result is that rivals share a supplier. Nvidia's chips, the custom chips Broadcom designs for Google and OpenAI, and AMD's chips all come out of the same fabs.

The fabs cluster for a physical reason. Starting up a new fab depends on copying settings, people and suppliers from one already working. So TSMC's sites sit close together in Taiwan, in Hsinchu, Taichung, Tainan and Kaohsiung.

Building away from the cluster costs more, and TSMC says so. It has begun making chips in Arizona, and it warns that its overseas fabs cut its margin, and by more as they grow.

## The clock on a chip factory

The usual assumption, which I shared, is that chip shortages clear in quarters, because money can buy another production line. TSMC's own timetable says otherwise.

On the January call, Wei said a new fab takes two to three years to build. In April he added that ramping it to full output takes one to two years more. Money spent today mostly buys output for 2028 and 2029.

TSMC plans to spend at least $60 billion on new capacity this year, far more than last year. Yet Wei said that money adds almost nothing to output this year and only a little next year.

Packaging is tighter still. In July Wei said TSMC's packaging capacity was so tight it was limiting its customers' growth. An AI chip that cannot be joined to its memory cannot ship, however many processors are waiting.

## What TSMC's own results show

If AI is the pull and the factories are the limit, AI work should be taking over TSMC's business while it spends heavily and still cannot catch up.

That is what its results show. The part of TSMC that makes chips for AI and other heavy computing now brings in about two thirds of its sales, up from three fifths a year earlier.

Its gross margin, the share of each sale left after the cost of making it, has risen sharply over the same year. Margin rising while factories run full is what a scarce supplier looks like in money.

## What would prove me wrong

My claim is narrow. Today, TSMC's factories bind before the grid does. Over the longer run, I still expect the grid to be the slower clock, because a grid connection still takes years.

I am wrong about today if TSMC's tightness eases while data centres with chips on order still sit waiting for power. That would show power was binding all along, and the chip queue was simply more visible.

I am wrong about the longer run if TSMC still calls its capacity tight in 2028, once the new spending has landed, while waits for grid connections shorten. Then the chip side would be the slower clock after all.

Wei himself hinted at the link. On the same January call, he said that when it came to electricity, the first worry was Taiwan's own supply. A fab is also a building waiting on power.

So I watch whether TSMC keeps calling packaging tight, and whether Arizona's second fab reaches volume in the second half of 2027. I watch AI and heavy computing as a share of its sales. And I watch how TSMC describes Taiwan's electricity.

<section class="exposure">
<h3>Who is exposed if the factory, for now, is the bottleneck</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are TSMC's own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">TSMC</span> manufactures chips for other companies, including most leading AI accelerators, and makes the CoWoS packaging that joins them to their memory.</dd>
<dt>The designers in the queue</dt>
<dd><span class="names">Nvidia</span> and <span class="names">AMD</span> design AI accelerators. <span class="names">Broadcom</span> and <span class="names">Marvell</span> design custom AI chips with the cloud giants. All of them have them made at TSMC.</dd>
<dt>The other foundries</dt>
<dd><span class="names">Samsung Foundry</span> and <span class="names">Intel Foundry</span> make advanced chips for outside customers.</dd>
<dt>The packaging and test houses</dt>
<dd><span class="names">ASE</span> and <span class="names">Amkor</span> package and test chips, including some advanced packaging work for AI processors.</dd>
<dt>The memory beside the chip</dt>
<dd><span class="names">SK Hynix</span>, <span class="names">Samsung</span> and <span class="names">Micron</span> make the stacked memory that CoWoS joins to each processor.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>AI chip designers without a firm place in TSMC's queue, and data centre builders with power ready and no chips to fill it. And this journal's own argument, for as long as the factory binds first.</dd>
</dl>
</section>

---

<p class="sources">Sources: TSMC second quarter 2026 management report and earnings release, 16 July 2026, for platform mix and margin. TSMC earnings calls of 15 January, 16 April and 16 July 2026 for comments on wafer supply, power, fab build and ramp times, capital spending, packaging capacity, Taiwan's electricity and overseas margin dilution. TSMC 2025 annual report for 2025 results and Arizona production. Figures are as reported on the dates cited. Where a quote comes from a call, it is TSMC's management speaking. I hold no view here on the politics around Taiwan, which sits outside this site's layer. Personal research, not investment advice.</p>
