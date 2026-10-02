---
title: "TSMC's chief says the AI bottleneck is its factories, not the power grid"
date: 2026-10-02T12:49:47+08:00
summary: "Almost every advanced AI chip, whoever designs it, is made by one company, TSMC, mostly in Taiwan. Its chief executive says those factories, not electricity, are what limits AI today, and the company's own numbers show why: a new chip factory takes years to build and more years to fill. That is a fair point, and it changes how long I think the chip side of the shortage lasts."
category: "Analysis"
cover: "/covers/tsmc-says-it-is-the-bottleneck.svg"
tags: ["the-stack", "data-centres", "supply-chain"]
---

This journal has argued for months that the thing holding back AI is not the chip. It is the wire, the substation and the queue to connect to the grid.

In January 2026, the company that makes almost every AI chip disagreed in public. Asked on TSMC's earnings call whether power was the limit, chief executive C.C. Wei said not yet. The bottleneck, Wei said, was TSMC's own wafer supply.

That deserves a fair hearing rather than a reflex. TSMC is the one place where Nvidia, Google, Amazon, AMD and Broadcom all queue for the same factories. And its own numbers show a factory that runs on a clock much closer to a substation's than to a chip's.

On today's horizon, TSMC is right: its factories are the bottleneck.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Imagine every famous restaurant in a city designs its own dishes, but all of them send the cooking to one shared kitchen. The kitchen is extraordinary, and nobody else can match its standards.</p>
<p>When demand surges, the restaurants cannot simply hire another kitchen. A new one takes years to build, and more years before the new cooks match the old ones dish for dish.</p>
<p>So the queue at the shared kitchen sets how fast every restaurant can grow, however good its menu is. That kitchen is TSMC.</p>
</details>

## Three words you need

**Foundry.** A company that manufactures chips other companies design. Nvidia, Apple, AMD and the cloud giants design. TSMC, the Taiwan Semiconductor Manufacturing Company, makes them.

**Fab.** Short for fabrication plant, the factory where chips are made on silicon wafers. TSMC's largest sites, which it calls gigafabs, are clusters of fabs built side by side.

**CoWoS.** TSMC's name for the advanced packaging that joins an AI processor to its stacked memory on one base. Every leading AI accelerator needs it, and it is a separate factory step from making the chip itself.

## Why one company makes everyone's chips

Most chip companies stopped building their own factories long ago. The cost of each new generation of manufacturing rose until only a company making chips for everyone could afford it. TSMC's model was simple: give us your design, and we will make the best chips.

The result is that rivals share a supplier. Nvidia's GPUs, the custom chips Broadcom designs for Google and OpenAI, and AMD's accelerators all come out of the same fabs. In the second quarter of 2026, 77 per cent of TSMC's wafer revenue came from its most advanced processes.

The fabs are clustered for a physical reason. Starting up a new fab, which the industry calls bringing it up, depends on copying settings, people and suppliers from one already working. So the sites sit next to each other, in Hsinchu, Taichung, Tainan and Kaohsiung.

## The clock on a chip factory

The usual assumption, which I shared, is that chip shortages clear in quarters, because money can buy another production line. TSMC's own timeline says otherwise.

On its January call, Wei said a new fab takes two to three years to build. In April Wei added that ramping it to full output takes one to two years more. In July Wei put the whole cycle, from developing the process to high-volume production, at more than five years.

The spending shows the same lag. TSMC raised its 2026 capital spending guidance to $60 billion to $64 billion, up from $40.9 billion in 2025. Wei said that money adds almost nothing to output in 2026 and only a little in 2027. It buys supply for 2028 and 2029.

Packaging is tighter still. In July, Wei said TSMC's packaging capacity was so tight it was limiting customers' growth. A stacked-memory AI chip that cannot be joined to its memory cannot ship, however many processors are waiting.

## What TSMC's own numbers show

If AI is the pull and the factories are the limit, AI work should be taking over the mix while TSMC spends heavily and still cannot catch up.

**Mix.** High-performance computing, the platform that includes AI accelerators, was 66 per cent of revenue in the second quarter of 2026, reported on 16 July. A year earlier it was 60 per cent. AI accelerators alone were in the high teens as a share of 2025 revenue, according to TSMC.

**Growth.** Second quarter revenue was $40.2 billion, up 33.7 per cent in dollars. TSMC now expects 2026 growth slightly above 40 per cent. Those are TSMC's forecasts, not mine.

**Margin.** Gross margin, the share of each sale left after the cost of making it, was 67.7 per cent, up 9.1 points on a year earlier. Margin rising while factories run full is what a scarce supplier looks like in money.

**The cost of leaving the cluster.** TSMC began volume production in Arizona at the end of 2024 and has committed $165 billion in America. It guides that overseas fabs cut gross margin by two to three points at first, widening to three to four. Building away from the cluster costs more, which is why clusters form.

## What would prove me wrong

My claim is narrow. Today, TSMC's factories bind before the grid does. I am not conceding the longer argument, because a grid connection and the substation behind it still take years, and the queue in front of them keeps growing.

I am wrong about today if TSMC's tightness eases while data centres with chips on order still sit waiting for power. That would show power was binding all along, and the chip queue was simply more visible.

I am wrong about the longer argument if TSMC still describes capacity as tight in 2028, once the new spending has landed, while grid connection waits shorten. Then the chip side would be the slower clock after all.

Wei himself hinted at the link between the two. On the same January call, Wei said that when it came to electricity, the first worry was Taiwan's own supply. A fab is also a building waiting on power.

So I watch four things. Whether TSMC keeps calling packaging capacity tight. Whether Arizona's second fab reaches volume in the second half of 2027 as planned. Whether high-performance computing keeps rising as a share of revenue. And how TSMC describes Taiwan's electricity supply.

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

<p class="sources">Sources: TSMC second quarter 2026 management report and earnings release, 16 July 2026, for revenue, margin, platform and technology mix. TSMC earnings calls of 15 January, 16 April and 16 July 2026 for comments on wafer supply, power, fab build and ramp times, capital spending, packaging capacity, Taiwan's electricity and overseas margin dilution. TSMC 2025 annual report for 2025 results and Arizona production. TSMC announcement of its expanded United States investment, 4 March 2025. Figures are as reported on the dates cited. Where a quote comes from a call, it is TSMC's management speaking. I hold no view here on the politics around Taiwan, which sits outside this site's layer. Personal research, not investment advice.</p>
