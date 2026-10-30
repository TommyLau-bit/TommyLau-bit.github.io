---
title: "Memory, not maths, sets the pace of AI, so the biggest buyer now designs it"
date: 2026-10-31T00:02:15+08:00
summary: "When an AI model writes an answer, the chip spends much of its time waiting for numbers to arrive from the memory stacked beside it, so memory sets how fast AI answers and how many people one chip can serve. Since 2020 the maths in Nvidia's top chip has grown about twelve times faster than the memory feeding it. The chip makers now compete on memory, and Nvidia has designed memory that puts its own controller into the base of each stack, which Micron says the next generation of GPUs will adopt, turning a standard part into one built to a buyer's design."
category: "Analysis"
cover: "/covers/memory-not-maths.svg"
tags: ["memory", "the-stack", "supply-chain"]
draft: false
---

Nvidia's newest AI chip, Rubin, can do 35 thousand trillion sums a second. Yet when it writes an answer, one word at a time, much of that power sits idle.

Nvidia's own engineers call that step "a memory-bound operation". The chip finishes its sums quickly, then waits for the model's numbers to arrive from memory.

So memory, not maths, sets how fast an AI answers and how many people one chip can serve. That has made memory the part chip makers compete on, and it is changing what memory is. For decades a memory chip was a standard part, the same for every buyer. From the next generation, the biggest buyer designs the bottom of the memory stack itself.

The memory in question is HBM, high-bandwidth memory: towers of memory chips stacked beside the processor. To write each word, the chip must read the whole model out of those towers again. A faster chip that cannot be fed faster simply waits longer.

The gap shows in the makers' own spec sheets. Since 2020, the peak maths in Nvidia's top chip has grown about 112 times. The speed of the memory feeding it has grown about nine times.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A chef gets faster at chopping every year, but the ingredients still come through one hatch from the pantry. Past a point, a faster chef just stands at the hatch, and the kitchen serves only as many plates as the hatch allows.</p>
<p>So kitchens widen the hatch and build bigger pantries. The busiest kitchen has now gone further: it designs its own hatch, made to fit its kitchen and no other.</p>
</details>

The chip makers' answer has been to pile on memory. Nvidia's H100 of 2022 carried 80 gigabytes; Rubin carries 288, and AMD plans 432 for its next chip. This year's memory generation, HBM4, doubled the number of connections between each tower and the chip.

Doubling them needed a smarter chip at the foot of each tower, called the base die, and it is increasingly made the way processors are made. Samsung's chip foundry credits its improving results to selling these base dies. In August Nvidia went further. It announced a memory design that moves its own controller, the circuit that runs the memory, into that base die. Micron says it is working with Nvidia on the first one.

That matters beyond engineering. A custom part is designed to one buyer's plan, generation after generation. If demand for that design falls, it cannot simply be sold as standard memory. Memory has long been a commodity that swings from glut to shortage. Memory built to one customer's design behaves more like a chip made to order.

My test is whether that becomes real at scale soon. By the end of 2027, at least two of the three makers, SK Hynix, Samsung and Micron, should say they are shipping custom memory in volume.

<hr class="layer">
<p class="layer-label">For investors</p>

## The chip waits on memory, not maths

An AI model answers in two steps. It reads the question in one pass, which keeps the maths busy. Then it writes the answer one word at a time, and for each word it must read every weight of the model from memory again.

Nvidia's engineers describe the second step plainly. It is "a memory-bound operation", and model execution is "frequently memory-bandwidth bound", "in particular, bandwidth-bound in the weights". Even after every software trick, it is "still very likely to be memory bound".

A rough sum shows why. A model of 70 billion weights stored at eight bits fills about 70 gigabytes. At 8 terabytes a second, one full read takes about nine milliseconds, so a single conversation tops out near 110 words a second, however fast the maths. That is my arithmetic, and it ignores overlap and caching.

Serving many users at once shares each read, but every conversation keeps its own working memory, the KV cache. Nvidia's own example puts it at about 2 gigabytes for one 4,096-token conversation on a small 7 billion weight model, and it grows with every user and every word. So bandwidth sets the speed of each answer, and capacity sets how many conversations fit on one chip.

The running measure in this piece is maths per byte: how many operations a chip can do for each byte its memory delivers. The higher it climbs, the longer the chip waits.

## For six years the maths outran the memory

On Nvidia's own spec sheets, maths per byte rose from about 150 on the A100 of 2020 to about 1,900 on Blackwell Ultra in 2025, more than twelvefold.

<figure class="chart">
<p class="chart-title">Since 2020 the maths has grown about twelve times faster than the memory feeding it</p>
<p class="chart-sub">Peak maths and memory bandwidth per Nvidia chip, as multiples of the A100 of 2020</p>
<svg viewBox="0 0 560 340" role="img" aria-label="Line chart, both lines indexed to the A100 of 2020 as 1. Peak maths per chip, in the smallest number format each supports, rose to 6.4 times with the H100 in 2022, 32 times with Blackwell in 2024, 48 times with Blackwell Ultra in 2025 and 112 times with Rubin in 2026. Memory bandwidth per chip rose to 1.6, 3.9, 3.9 and 9.4 times over the same chips.">
<g class="c-grid"><line x1="50" y1="290.0" x2="500" y2="290.0"/><line x1="50" y1="225.0" x2="500" y2="225.0"/><line x1="50" y1="160.0" x2="500" y2="160.0"/><line x1="50" y1="95.0" x2="500" y2="95.0"/><line x1="50" y1="30.0" x2="500" y2="30.0"/></g>
<g class="c-axis"><text x="42" y="294.0" text-anchor="end">0</text><text x="42" y="229.0" text-anchor="end">30</text><text x="42" y="164.0" text-anchor="end">60</text><text x="42" y="99.0" text-anchor="end">90</text><text x="42" y="34.0" text-anchor="end">120</text><text x="50.0" y="310" text-anchor="middle">A100</text><text x="50.0" y="326" text-anchor="middle">2020</text><text x="200.0" y="310" text-anchor="middle">H100</text><text x="200.0" y="326" text-anchor="middle">2022</text><text x="350.0" y="310" text-anchor="middle">Blackwell</text><text x="350.0" y="326" text-anchor="middle">2024</text><text x="425.0" y="310" text-anchor="middle">Ultra</text><text x="425.0" y="326" text-anchor="middle">2025</text><text x="500.0" y="310" text-anchor="middle">Rubin</text><text x="500.0" y="326" text-anchor="middle">2026</text></g>
<polyline class="c-line c-s2" points="50.0,287.8 200.0,276.1 350.0,220.6 425.0,185.8 500.0,46.9"/>
<polyline class="c-line c-s3" points="50.0,287.8 200.0,286.4 350.0,281.5 425.0,281.5 500.0,269.6"/>
<circle class="c-dot c-s2" cx="50.0" cy="287.8" r="3.5"/><circle class="c-dot c-s2" cx="200.0" cy="276.1" r="3.5"/><circle class="c-dot c-s2" cx="350.0" cy="220.6" r="3.5"/><circle class="c-dot c-s2" cx="425.0" cy="185.8" r="3.5"/><circle class="c-dot c-s2" cx="500.0" cy="46.9" r="3.5"/>
<circle class="c-dot c-s3" cx="50.0" cy="287.8" r="3.5"/><circle class="c-dot c-s3" cx="200.0" cy="286.4" r="3.5"/><circle class="c-dot c-s3" cx="350.0" cy="281.5" r="3.5"/><circle class="c-dot c-s3" cx="425.0" cy="281.5" r="3.5"/><circle class="c-dot c-s3" cx="500.0" cy="269.6" r="3.5"/>
<text class="c-lab c-s2t" x="492.0" y="36.9" text-anchor="end">Peak maths, 112 times</text>
<text class="c-lab c-s3t" x="492.0" y="257.6" text-anchor="end">Memory bandwidth, 9.4 times</text>
</svg>
<figcaption>Nvidia spec pages and technical blog, read 30 October 2026. Peak maths is dense, in the smallest number format each chip supports: 16-bit for the A100 (312 TFLOPS), 8-bit for the H100 (about 2 PFLOPS), 4-bit for Blackwell (10), Blackwell Ultra (15) and Rubin (35, Nvidia's dense training figure). Bandwidth 2.0, 3.35, 8, 8 and 19.2 TB/s. Halving the number format also halves the bytes per weight, so in numbers moved the gap is narrower than shown.</figcaption>
</figure>

The caveat is real but does not reverse the direction. Held at 16-bit, peak maths rose about seven to eight times from the A100 to Blackwell Ultra while bandwidth rose about four. Smaller number formats have been the industry's main release valve, and with the maths already at four bits, few halvings are left.

The memory makers say the same in their own words. SK Hynix's head of memory systems research told the Open Compute summit in October that processor-centric designs "face a bottleneck known as the 'memory wall'".

## Rubin held the line, on HBM4

Rubin is the first Nvidia generation in this run where maths per byte did not rise: about 1,820, against 1,875 for Blackwell Ultra. Its bandwidth jumped 2.4 times, to 19.2 terabytes a second, on HBM4.

That came from the standard. JEDEC's HBM4 standard of April 2025 doubles each stack's interface to 2,048 bits and its channels to 32, for up to 2 terabytes a second per stack. SK Hynix says its HBM4 runs above 10 gigabits a second per pin, against the standard's top speed of 8. So a maker already runs memory past its own rulebook.

Capacity has climbed alongside. A bigger model, or more conversations, needs more gigabytes on the chip.

<figure class="chart">
<p class="chart-title">Memory per chip has grown 3.6 times since the H100</p>
<p class="chart-sub">High-bandwidth memory on each AI chip, in gigabytes, by maker and year of launch</p>
<svg viewBox="0 0 560 290" role="img" aria-label="Bar chart of memory per chip in gigabytes. Nvidia: H100 80, H200 141, Blackwell 192, Blackwell Ultra 288, Rubin 288. AMD: MI300X 192, MI355X 288, MI400 432, an engineering projection.">
<g class="c-axis"><text x="192" y="29" text-anchor="end">Nvidia H100, 2022</text><text x="192" y="61" text-anchor="end">Nvidia H200, 2024</text><text x="192" y="93" text-anchor="end">Nvidia Blackwell, 2024</text><text x="192" y="125" text-anchor="end">Nvidia Blackwell Ultra, 2025</text><text x="192" y="157" text-anchor="end">Nvidia Rubin, 2026</text><text x="192" y="199" text-anchor="end">AMD MI300X, 2023</text><text x="192" y="231" text-anchor="end">AMD MI355X, 2025</text><text x="192" y="263" text-anchor="end">AMD MI400, 2026 (projected)</text></g>
<rect class="c-bar" x="200" y="14" width="53.3" height="22" rx="2"/><rect class="c-bar" x="200" y="46" width="94.0" height="22" rx="2"/><rect class="c-bar" x="200" y="78" width="128.0" height="22" rx="2"/><rect class="c-bar" x="200" y="110" width="192.0" height="22" rx="2"/><rect class="c-bar" x="200" y="142" width="192.0" height="22" rx="2"/><rect class="c-bar c-alt" x="200" y="184" width="128.0" height="22" rx="2"/><rect class="c-bar c-alt" x="200" y="216" width="192.0" height="22" rx="2"/><rect class="c-bar c-alt" x="200" y="248" width="288.0" height="22" rx="2"/>
<text class="c-lab c-s2t" x="261.3" y="30">80 GB</text><text class="c-lab c-s2t" x="302.0" y="62">141 GB</text><text class="c-lab c-s2t" x="336.0" y="94">192 GB</text><text class="c-lab c-s2t" x="400.0" y="126">288 GB</text><text class="c-lab c-s2t" x="400.0" y="158">288 GB</text><text class="c-lab c-s3t" x="336.0" y="200">192 GB</text><text class="c-lab c-s3t" x="400.0" y="232">288 GB</text><text class="c-lab c-s3t" x="496.0" y="264">432 GB</text>
<line class="c-base" x1="200" y1="8" x2="200" y2="276"/>
</svg>
<figcaption>Nvidia spec pages and its Blackwell Ultra technical blog (22 August 2025); AMD's MI300X page and Advancing AI deck (12 June 2025). The MI400 figure is AMD's engineering projection. Nvidia's DGX B200 system works out at 180 GB a chip; the 192 GB is its Blackwell chip specification.</figcaption>
</figure>

AMD sells on it directly: its own slide says "Highest memory bandwidth & capacity drives performance". Micron told investors in September that every AI platform's "value proposition is enhanced by the performance and capacity of memory". For the buyer, memory per chip has become a headline specification, beside the maths.

## The bottom of the stack became a logic chip

Wider memory needs a cleverer base die, the chip at the foot of each stack that talks to the processor. From HBM4 it moves towards logic processes, the kind used for processors in chip foundries.

The three makers have taken three routes. SK Hynix said in April 2024 that, for HBM4, it planned to "adopt TSMC's advanced logic process for HBM4's base die", so it could "produce customized HBM". Samsung makes its base die in its own foundry: its foundry business credited improving earnings to "HBM base-die demand" in July and to "HBM base-die sales growth" in October, on a 4 nanometre process. Micron, as [the chip supply chain piece](/journal/the-chip-supply-chain/) notes, makes its HBM4 base die in-house.

So at Samsung, and at SK Hynix if its 2024 plan held, a stack of memory now passes through a logic factory before it is finished. Samsung's foundry results already move with HBM.

## The buyer now designs the memory

The strongest evidence is a buyer's own design. On 26 August 2026 Nvidia announced NVHBM. Standard HBM, it said, places "the memory controller on the XPU die", using processor space that could do maths. NVHBM instead "integrates NVIDIA's custom memory controller into the HBM base die".

<figure class="chart">
<p class="chart-title">With NVHBM, Nvidia's design moves into the memory stack</p>
<p class="chart-sub">Where the memory controller sits, standard HBM against Nvidia's custom design; the shaded part is what moves</p>
<svg viewBox="0 0 560 270" role="img" aria-label="Diagram of two designs. Standard HBM: the processor die holds the maths and the memory controller, linked to a stack of DRAM dies on a base die that connects them. NVHBM, from HBM4E: the processor die holds only the maths, with up to 25 per cent more room, and the base die at the foot of the memory stack carries Nvidia's memory controller.">
<text class="c-lab c-s1t" x="8" y="18">Standard HBM: the memory controller sits on the processor</text>
<rect class="c-box" x="8" y="30" width="230" height="84" rx="4"/>
<rect class="c-zone" x="14" y="78" width="218" height="28" rx="3"/>
<text class="c-box-t" x="20" y="50">Processor die</text>
<text class="c-note" x="20" y="70">the maths</text>
<text class="c-note" x="20" y="94">memory controller</text>
<line class="c-arrow" x1="244" y1="72" x2="296" y2="72"/><polygon class="c-arrow-head" points="302,72 295,68 295,76"/>
<line class="c-arrow" x1="252" y1="72" x2="248" y2="72"/><polygon class="c-arrow-head" points="242,72 249,68 249,76"/>
<rect class="c-box" x="308" y="30" width="240" height="8" rx="2"/>
<rect class="c-box" x="308" y="41" width="240" height="8" rx="2"/>
<rect class="c-box" x="308" y="52" width="240" height="8" rx="2"/>
<rect class="c-box" x="308" y="63" width="240" height="8" rx="2"/>
<rect class="c-box" x="308" y="76" width="240" height="38" rx="4"/>
<text class="c-box-t" x="318" y="92">Base die</text>
<text class="c-note" x="318" y="107">connects the DRAM dies above</text>
<text class="c-lab c-s1t" x="8" y="150">NVHBM, from HBM4E: Nvidia&#8217;s controller moves into the stack</text>
<rect class="c-box" x="8" y="162" width="230" height="84" rx="4"/>
<text class="c-box-t" x="20" y="182">Processor die</text>
<text class="c-note" x="20" y="202">the maths, with up to 25%</text>
<text class="c-note" x="20" y="226">more room on the die</text>
<line class="c-arrow" x1="244" y1="204" x2="296" y2="204"/><polygon class="c-arrow-head" points="302,204 295,200 295,208"/>
<line class="c-arrow" x1="252" y1="204" x2="248" y2="204"/><polygon class="c-arrow-head" points="242,204 249,200 249,208"/>
<rect class="c-box" x="308" y="162" width="240" height="8" rx="2"/>
<rect class="c-box" x="308" y="173" width="240" height="8" rx="2"/>
<rect class="c-box" x="308" y="184" width="240" height="8" rx="2"/>
<rect class="c-box" x="308" y="195" width="240" height="8" rx="2"/>
<rect class="c-box" x="308" y="208" width="240" height="38" rx="4"/>
<rect class="c-zone" x="312" y="211" width="232" height="32" rx="3"/>
<text class="c-box-t" x="318" y="224">Base die</text>
<text class="c-note" x="318" y="239">carries Nvidia&#8217;s memory controller</text>
<text class="c-note" x="308" y="262">DRAM dies stacked on the base die</text>
</svg>
<figcaption>Nvidia blog, 26 August 2026. Nvidia's own figures against standard HBM4E: up to 30% more memory bandwidth, 15% lower HBM power, up to 25% more room on the processor die. Not to scale.</figcaption>
</figure>

Nvidia claims up to 30% more bandwidth and 15% lower memory power than standard HBM4E, and says NVHBM will be "available from multiple memory providers". Micron named itself a month later: it is working with Nvidia on "the industry's first custom-HBM4E implementation, NVHBM, to be adopted on next generation of GPUs". Its annual report adds that HBM4E "customization options" bring "even deeper R&D engagement with customers", and that HBM4E ramps in volume in calendar 2027. Samsung shipped its first HBM4E samples in the second quarter of 2026.

A custom base die changes the trade. The stack is designed to one buyer's plan for each generation. Nvidia offers that plan to the chipmakers that link to its systems, but it stays Nvidia's design, and if demand for it falls, the stacks cannot simply be sold as standard HBM. That is how a foundry works, and it is not how memory has worked.

## Two of the three makers are Korean

Nvidia names its memory suppliers in its annual report: SK Hynix, Micron and Samsung. Two are Korean, and SK Hynix's new HBM capacity before 2028 is in Korea.

SK Hynix will run its M15X fab in Cheongju at full capacity by the end of 2026 to make more HBM4. A dedicated HBM packaging plant in the same city, P&T7, gets its test line by October 2027 and packaging by February 2028. Its American HBM packaging plant, in Indiana, starts mass production in the second half of 2028. Micron's HBM packaging plant in Singapore starts output in early 2027.

SK Hynix expects demand to outrun supply "through 2030", citing "the long lead time required to build new production facilities". A custom stack adds a logic foundry to that chain, so every stack now depends on a memory fab, a logic fab and a packaging line being ready together.

## What could loosen the memory limit

The case against is real. First, smaller numbers: each halving of the number format halves the bytes per weight, and software keeps finding savings. Second, overflow: Micron says SSDs are now used "for KV cache offload", and SK Hynix is showing high bandwidth flash as a cheaper tier. Both ease capacity more than bandwidth, since the weights still have to be read for every word.

The custom half is weaker still. NVHBM has one named chip partner, Amazon's Annapurna Labs, "starting with Trainium4", and no date. The HBM4 standard stays backward compatible with HBM3 controllers, and Nvidia measures NVHBM against "standard HBM4E", which remains on sale. Custom memory could stay one buyer's niche through 2027. That is exactly what the test below checks.

None of this lets the maths stop waiting. The chef is still faster than the hatch. What has changed is who designs the hatch: the biggest kitchen now draws its own, and the memory makers build it to order.

## Claims on record

The test this piece stands behind, dated when it was written:

<a id="memory-not-maths"></a>

**From HBM4E, the memory beside AI chips is built to the buyer's design** (31 October 2026)

Claim: "From HBM4E, high-bandwidth memory becomes a part built to the buyer's design: by 31 December 2027, at least two of SK Hynix, Samsung and Micron will have said, in their own results releases, filings or newsroom, that they are in volume production of, or shipping in volume, HBM whose base die carries a customer's own design, such as Nvidia's NVHBM."

Breaks if: "By 31 December 2027, fewer than two of SK Hynix, Samsung and Micron have said, in their own results releases, filings or newsroom, that they are in volume production of, or shipping in volume, HBM whose base die carries a customer's own design, such as Nvidia's NVHBM; a maker's own base die sold as 'custom HBM' does not count unless the maker says it carries the customer's design. Samples, development, qualification, design wins and plans do not count, and nor do press or research-firm reports."

## What would prove me wrong

The test fails if, by the end of 2027, fewer than two of the three makers say in their own words that they ship custom HBM in volume. That is a genuine risk. Micron's HBM4E ramps only in 2027, NVHBM has no published date, and Samsung and SK Hynix have said nothing dated about custom volume in releases I could open.

A pass would not prove the memory limit on its own; it would show that buyers now treat memory as a part worth designing. The wider argument weakens if the generations after Rubin and MI400 stop raising memory per chip, since that would say memory no longer sets what a chip can serve.

## Research notes

[Micron](/research/micron/) has an initiation note, resting on its own claim about HBM wafers. How far ahead each year's HBM is sold is in [the chip supply chain](/journal/the-chip-supply-chain/).

<details class="evidence">
<summary>The figures behind the charts</summary>

| Chip | Launch | Memory | Bandwidth | Peak dense maths, smallest format | Maths per byte | Source |
|---|---|---|---|---|---|---|
| Nvidia A100 80GB | 2020 | 80 GB HBM2e | 2.039 TB/s | 312 TFLOPS, 16-bit (624 with sparsity) | about 153 | Nvidia A100 page |
| Nvidia H100 | 2022 | 80 GB | 3.35 TB/s | about 2 PFLOPS, 8-bit (3,958 TFLOPS with sparsity) | about 600 | Nvidia H100 page; Blackwell Ultra blog |
| Nvidia H200 | 2024 | 141 GB HBM3e | 4.8 TB/s | as H100 | about 410 | Nvidia H200 page |
| Nvidia Blackwell | 2024 | 192 GB HBM3E | 8 TB/s | 10 PFLOPS, 4-bit | 1,250 | Blackwell Ultra blog, 22 August 2025 |
| Nvidia Blackwell Ultra | 2025 | 288 GB HBM3E | 8 TB/s | 15 PFLOPS, 4-bit | 1,875 | same |
| Nvidia Rubin | 2026 | 288 GB HBM4 | 19.2 TB/s | 35 PFLOPS, 4-bit, training (50 inference, with sparsity) | about 1,820 | Vera Rubin NVL72 page |
| AMD MI300X | 2023 | 192 GB HBM3 | 5.3 TB/s | | | AMD MI300X page |
| AMD MI355X | 2025 | 288 GB HBM3E | 8 TB/s | 10 PFLOPS, MXFP4 | | AMD deck, 12 June 2025 |
| AMD MI400 | 2026, projected | 432 GB HBM4 | 19.6 TB/s | 40 PFLOPS, FP4 | | same, engineering projection |

Maths per byte is peak dense operations divided by bytes a second, my arithmetic. Nvidia publishes sparse figures by default and states that dense is half. The A100 is shown at 16-bit because 8-bit integer maths was not its usual format for models; at 8-bit its maths per byte would be about 306. Rubin at 16-bit (4 PFLOPS dense) gives about 210 against about 280 to 310 for Blackwell Ultra (Nvidia's HGX and rack pages imply 2.25 to 2.5 PFLOPS dense), so at fixed format Rubin narrowed the gap, which fits the story of HBM4 catching up a step. The V100 of 2017 is left off because Nvidia no longer publishes its specification page.

Not used: market shares and any report that SK Hynix's shipping HBM4 base die is made by TSMC, which rest on press and research firms; SK Hynix's own words are its plan of April 2024. Micron's HBM4E base die partner is likewise press only.

</details>

<section class="exposure">
<h3>Who is exposed if memory becomes a part built to the buyer's design</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>The memory makers</dt>
<dd><span class="names">SK Hynix</span>, <span class="names">Samsung</span> and <span class="names">Micron</span> make HBM, the stacked memory beside AI chips.</dd>
<dt>The base die</dt>
<dd><span class="names">TSMC</span> and Samsung's foundry make logic base dies for HBM4.</dd>
<dt>The buyers who design it</dt>
<dd><span class="names">Nvidia</span> and <span class="names">AMD</span> design AI chips; <span class="names">Amazon</span>'s Annapurna Labs is the first named NVHBM partner.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Chip designers without the volume to commission their own stack, and memory makers whose standard HBM loses ground to custom parts they do not make.</dd>
<dt>Where I stop</dt>
<dd>I have no view on the memory equities.</dd>
</dl>
</section>

---

<p class="sources">Sources: Nvidia spec pages for the A100, H100, H200, DGX B200, HGX and Vera Rubin NVL72 (read 30 October 2026), its technical blogs of 17 November 2023 and 22 August 2025, its NVHBM blog (26 August 2026) and Form 10-K (25 February 2026); AMD's MI300X page, its release of 2 June 2024 and Advancing AI deck (12 June 2025); JEDEC's HBM4 release (16 April 2025); SK Hynix releases of 3, 19 and 24 April 2024, 12 September 2025, 22 April, 16 October and 28 October 2026; Samsung results of 30 April, 30 July and 29 October 2026; Micron's prepared remarks (30 September 2026) and Form 10-K (9 October 2026). Maths per byte and the read-time sum are my arithmetic. Personal research, not investment advice.</p>
