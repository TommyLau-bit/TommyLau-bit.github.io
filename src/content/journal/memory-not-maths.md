---
title: "Memory, not maths, sets the pace of AI, so the biggest buyer now designs it"
date: 2026-10-31T00:02:15+08:00
summary: "When an AI model writes an answer, the chip spends much of its time waiting for numbers to arrive from the memory stacked beside it, so memory sets how fast AI answers and how many people one chip can serve. Since 2020 the maths in Nvidia's top chip has grown about twelve times faster than the memory feeding it. The chip makers now compete on memory, and Nvidia has designed memory that puts its own controller into the base of each stack, which Micron says the next generation of GPUs will adopt, turning a standard part into one built to a buyer's design."
category: "Analysis"
cover: "/covers/memory-not-maths.svg"
tags: ["memory", "the-stack", "supply-chain"]
updated: 2026-11-06
updateNote: "Now traces one word of an answer to the memory step that holds it up, with evidence to 6 November 2026."
draft: false
---

Nvidia's newest AI chip, Rubin, can do 35 thousand trillion sums a second. Yet when it writes an answer, one word at a time, much of that power sits idle.

Nvidia's own engineers call that step "a memory-bound operation": the chip finishes its sums, then waits for numbers to arrive from memory.

So memory, not maths, sets the pace of AI. And from the next generation, the biggest buyer designs the bottom of the memory stack itself.

"Memory" hides three limits. Capacity is how much sits beside the chip, which sets how many conversations one chip can hold. Bandwidth is how many bytes reach the chip each second, which sets how fast each answer is written. Latency is how long the first byte takes, which matters little to a chip streaming huge blocks. This piece is about bandwidth, with capacity second.

<details class="analogy">
<summary>The analogy</summary>
<p>A chef chops faster every year, but every ingredient still comes through one hatch from the pantry. The chef is the chip's maths. The width of the hatch is bandwidth: past a point, a faster chef just waits. The size of the pantry is capacity: how many tables the kitchen can serve at once.</p>
<p>So kitchens widen the hatch, and a wider hatch needs a proper frame: that frame is the base die. The busiest kitchen now draws the frame itself and lets any builder make it. A frame cut to its wall fits no other kitchen.</p>
</details>

Trace one word from question to screen and the wait has a single cause.

First, the chip reads the question in one pass, reusing each of the model's weights many times. Second, to write a word, it streams every weight out of the memory towers beside it, called HBM, high-bandwidth memory. Third, it reads that conversation's own notes, the KV cache, which grow with every word. Fourth, it does the sums, about two for each weight. Fifth, it adds the word and starts again.

<figure class="chart">
<p class="chart-title">Every word waits on one step: reading the whole model from memory</p>
<p class="chart-sub">One word of an answer, from question to screen, on a 70 GB model and 8 TB/s of memory</p>
<svg viewBox="0 0 560 196" role="img" aria-label="Diagram of five steps in order. One, prompt: the chip reads the question once, reusing each weight many times. Two, weights: to write each word it reads the whole model from memory again; a 70 GB model at 8 TB/s takes about 9 milliseconds. This is the choke point. Three, KV cache: it reads the conversation's own notes, which grow with every word. Four, sums: about two operations per weight, a sliver of the 9 milliseconds. Five, write: the word joins the notes and the loop starts again, so one conversation tops out near 110 words a second.">
<rect class="c-box" x="5.0" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="13.0" y="66">1. Prompt</text>
<text class="c-note" x="13.0" y="88">Read once per</text>
<text class="c-note" x="13.0" y="106">question;</text>
<text class="c-note" x="13.0" y="124">weights reused</text>
<text class="c-note" x="13.0" y="142">many times</text>
<line class="c-arrow" x1="106.4" y1="97" x2="111.4" y2="97"/><polygon class="c-arrow-head" points="116.4,97 110.4,93 110.4,101"/>
<rect class="c-zone" x="113.4" y="14" width="108.4" height="144" rx="4"/>
<text class="c-zone-t" x="167.6" y="30" text-anchor="middle">THE CHOKE POINT</text>
<rect class="c-box" x="117.4" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="125.4" y="66">2. Weights</text>
<text class="c-note" x="125.4" y="88">Whole model</text>
<text class="c-note" x="125.4" y="106">read again</text>
<text class="c-note" x="125.4" y="124">70 GB: about</text>
<text class="c-note" x="125.4" y="142">9 ms a word</text>
<line class="c-arrow" x1="218.8" y1="97" x2="223.8" y2="97"/><polygon class="c-arrow-head" points="228.8,97 222.8,93 222.8,101"/>
<rect class="c-box" x="229.8" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="237.8" y="66">3. KV cache</text>
<text class="c-note" x="237.8" y="88">Each chat's</text>
<text class="c-note" x="237.8" y="106">own notes,</text>
<text class="c-note" x="237.8" y="124">growing with</text>
<text class="c-note" x="237.8" y="142">every word</text>
<line class="c-arrow" x1="331.2" y1="97" x2="336.2" y2="97"/><polygon class="c-arrow-head" points="341.2,97 335.2,93 335.2,101"/>
<rect class="c-box" x="342.2" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="350.2" y="66">4. Sums</text>
<text class="c-note" x="350.2" y="88">About two per</text>
<text class="c-note" x="350.2" y="106">weight: a</text>
<text class="c-note" x="350.2" y="124">sliver of</text>
<text class="c-note" x="350.2" y="142">the 9 ms</text>
<line class="c-arrow" x1="443.6" y1="97" x2="448.6" y2="97"/><polygon class="c-arrow-head" points="453.6,97 447.6,93 447.6,101"/>
<rect class="c-box" x="454.6" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="462.6" y="66">5. Write</text>
<text class="c-note" x="462.6" y="88">Add the word,</text>
<text class="c-note" x="462.6" y="106">loop again:</text>
<text class="c-note" x="462.6" y="124">near 110</text>
<text class="c-note" x="462.6" y="142">words a second</text>
<text class="c-lab c-s2t" x="117.4" y="180" text-anchor="start">Every word reads the whole model again</text>
</svg>
<figcaption>Nvidia technical blog (17 November 2023) for the memory-bound step and the KV cache. Timings are my arithmetic: a 70 billion weight model at eight bits, 8 TB/s of HBM, ignoring caching and overlap. My framing of the chain.</figcaption>
</figure>

The second step binds. A model of 70 billion weights fills about 70 gigabytes, and at 8 terabytes a second one full read takes about nine milliseconds, by my arithmetic. The sums fill a sliver of that, so one conversation tops out near 110 words a second, however fast the maths. And the gap has widened: since 2020 the peak maths in Nvidia's top chip has grown about 112 times, the memory feeding it about nine.

Widening the pipe changed what memory is. This year's HBM4 doubled the wires between each tower and the chip, which needed a smarter chip at the foot of each tower, the base die, made like a processor. In August Nvidia announced NVHBM, which moves its own memory controller, the circuit that runs the memory, into that base die. Micron, one of the three memory makers, says it is working with Nvidia on the first.

That matters beyond engineering. Memory has long been a standard part that swings from glut to shortage. A part built to one buyer's design cannot be sold elsewhere if that buyer's demand falls, so it behaves like a chip made to order.

My test: by the end of 2027, at least two of the three makers, SK Hynix, Samsung and Micron, should say they are shipping custom memory in volume.


<hr class="layer">
<p class="layer-label">For investors</p>

## The chip waits on memory, so the biggest buyer now designs the memory

<a id="memory-not-maths"></a>

Since 2020 the maths in the top chip of Nvidia, the biggest buyer of AI memory, has outrun the memory feeding it. On Nvidia's own spec sheets, maths per byte, the operations a chip can do for each byte its memory delivers, rose from about 150 on the A100 of 2020 to about 1,900 on Blackwell Ultra, its flagship of 2025, more than twelvefold. The higher it climbs, the longer the chip waits. So memory is now the part that sells the chip. And from HBM4E, the next generation of stacked memory, Nvidia's own controller moves into the base of the memory stack.

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

The chart flatters the gap a little, since newer chips count maths in smaller numbers, but the caveat does not reverse the direction. Held at 16-bit, peak maths rose about seven to eight times from the A100 to Blackwell Ultra while bandwidth rose about four.

## Every word the model writes rereads the whole model

The chip waits because of how a model answers. It reads the question in one pass, then writes one word at a time, reading every weight from memory for each word. Nvidia's engineers call that step "a memory-bound operation", and even after every software trick, "still very likely to be memory bound".

A rough sum shows how hard that caps the speed. A model of 70 billion weights stored at eight bits fills about 70 gigabytes. At 8 terabytes a second, one full read takes about nine milliseconds, so a single conversation tops out near 110 words a second, however fast the maths. That is my arithmetic, and it ignores overlap and caching.

Memory sets a second limit through capacity. Every conversation keeps its own working memory, the KV cache. Nvidia's own example puts it at about 2 gigabytes for one 4,096-token conversation on a small 7 billion weight model. So bandwidth sets the speed of each answer, and capacity sets how many conversations fit on one chip. The memory makers agree. At SK Hynix, the Korean memory maker, the head of memory systems research told the Open Compute summit in October that processor-centric designs "face a bottleneck known as the 'memory wall'".

## HBM4 held the line, and memory became the headline specification

The industry's answer was wider memory. Rubin, Nvidia's 2026 chip, is the first generation in this run where maths per byte did not rise: about 1,820, against 1,875 for Blackwell Ultra. Its bandwidth jumped 2.4 times, to 19.2 terabytes a second, on HBM4; that is the figure on Nvidia's product spec page, and I use it over the "up to 22" in one of its platform blogs. JEDEC, the body that sets memory standards, published HBM4 in April 2025: it doubles each stack's interface to 2,048 bits, for up to 2 terabytes a second per stack.

Memory per chip has become a headline specification too. Nvidia's went from 80 gigabytes on the H100 of 2022 to 288 on Rubin, 3.6 times, and AMD, Nvidia's nearest GPU rival, projects 432 for its MI400. AMD sells on it directly: its own slide says "Highest memory bandwidth & capacity drives performance".

## The base die became a logic chip, and each maker found its own route to make it

Wider memory changed the chip at the bottom of the stack. From HBM4 the base die, the chip at the foot of each stack that talks to the processor, moves towards the logic processes used for processors, but the three makers took different routes. SK Hynix said in April 2024 that it planned to use the leading foundry's advanced logic process for HBM4's base die, to "produce customized HBM". Samsung, which also makes chips for others, has its own foundry, which credited its results to "HBM base-die demand" in July 2026 and "HBM base-die sales growth" in October. Micron, the American maker, makes its HBM4 base die in-house, its annual report says, as [the chip supply chain piece](/journal/the-chip-supply-chain/) notes, and named the leading foundry for its HBM4E base die in September 2025, "for both standard and customized products".

## Nvidia now draws the base die, and any maker may build it

Once the base die became a logic chip, the buyer could design it. On 26 August 2026 Nvidia announced NVHBM, its own memory design. Standard HBM places "the memory controller on the XPU die", the processor, using space that could do maths. NVHBM "integrates NVIDIA's custom memory controller into the HBM base die".

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

The gains are large on Nvidia's own figures: it claims up to 30% more bandwidth and 15% lower memory power than standard HBM4E. And a maker has signed up. Micron named itself a month later, working with Nvidia on "the industry's first custom-HBM4E implementation, NVHBM, to be adopted on next generation of GPUs". Its HBM4E ramps in volume in calendar 2027. Press reports in October 2026, carried by TrendForce, a research firm, said Nvidia had also asked all three makers to put NVHBM base dies on the leading foundry's 3 nanometre process, and that Samsung agreed; no company has confirmed it, so I do not rely on it.

That changes the trade. Custom HBM is not new: SK Hynix spoke of "customized HBM" in 2024. What is new is who draws the base die. NVHBM is Nvidia's design, "available from multiple memory providers", so Nvidia can move it between makers. The maker gets no such freedom: if demand for that design falls, the stack, as I read it, cannot be sold as standard HBM. That is how a foundry works, and it is not how memory has worked.

## The makers build plants years ahead for a design set one generation at a time

That design risk lands on plants the makers commit to years ahead. SK Hynix's new HBM capacity before 2028 is in Korea, where its M15X memory fab in Cheongju runs at full capacity by the end of 2026. P&T7, its HBM packaging plant in the same city, packages by February 2028, and its American HBM packaging and test plant, in Indiana, opens its cleanroom by October 2028 and starts mass production in the second half of 2029, it said on 28 August 2026. Micron's Singapore HBM packaging plant starts output in early 2027. Nvidia has launched a new flagship every year since 2024.

<figure class="chart">
<p class="chart-title">The new memory plants come on stream one to three chip launches after Rubin</p>
<p class="chart-sub">Nvidia's flagship and the HBM generation by year, against the memory makers' new plants by stated date</p>
<svg viewBox="0 0 560 292" role="img" aria-label="Timeline from 2026 to 2031. Nvidia's flagship: Rubin in 2026 and Rubin Ultra in 2027, with a new flagship each year after that if the pace holds. HBM generation: HBM4 in 2026 and HBM4E in volume in 2027. SK Hynix's M15X fab at full capacity by the end of 2026. Micron's Singapore packaging plant from early 2027. SK Hynix's P&amp;T7 packaging plant with a test line in October 2027 and packaging by February 2028. SK Hynix's Indiana plant with its cleanroom open by October 2028 and mass production in the second half of 2029. SK Hynix expects demand to outrun supply through 2030.">
<g class="c-axis"><text x="150" y="45" text-anchor="end">Nvidia flagship</text><text x="150" y="89" text-anchor="end">HBM generation</text><text x="150" y="119" text-anchor="end">SK Hynix M15X fab</text><text x="150" y="149" text-anchor="end">Micron Singapore</text><text x="150" y="179" text-anchor="end">SK Hynix P&amp;T7</text><text x="150" y="209" text-anchor="end">SK Hynix Indiana</text><text x="150" y="239" text-anchor="end">Demand over supply</text><text x="160.0" y="282" text-anchor="middle">2026</text><text x="237.6" y="282" text-anchor="middle">2027</text><text x="315.2" y="282" text-anchor="middle">2028</text><text x="392.8" y="282" text-anchor="middle">2029</text><text x="470.4" y="282" text-anchor="middle">2030</text><text x="557" y="282" text-anchor="end">2031</text></g>
<line class="c-today" x1="224.4" y1="14" x2="224.4" y2="264"/><text class="c-today-t" x="228.4" y="12">today</text>
<circle class="c-dot c-s3" cx="198.8" cy="40" r="5"/><circle class="c-dot c-s3" cx="276.4" cy="40" r="5"/>
<g class="c-start"><circle cx="354.0" cy="40" r="4"/><circle cx="431.6" cy="40" r="4"/><circle cx="509.2" cy="40" r="4"/></g>
<text class="c-lab c-s3t" x="198.8" y="30" text-anchor="middle">Rubin</text><text class="c-lab c-s3t" x="276.4" y="30" text-anchor="middle">Rubin Ultra</text>
<text class="c-note" x="548" y="62" text-anchor="end">a new flagship each year, if the pace holds</text>
<circle class="c-dot c-s2" cx="198.8" cy="84" r="5"/><circle class="c-dot c-s2" cx="276.4" cy="84" r="5"/>
<text class="c-lab c-s2t" x="198.8" y="74" text-anchor="middle">HBM4</text>
<text class="c-lab c-s2t" x="286.4" y="89">HBM4E in volume</text>
<circle class="c-dot c-s2" cx="233.7" cy="114" r="5"/><text class="c-note" x="243.7" y="118">full capacity by end 2026</text>
<circle class="c-dot c-s2" cx="253.1" cy="144" r="5"/><text class="c-note" x="263.1" y="148">output from early 2027</text>
<g class="c-span"><line x1="299.0" y1="174" x2="324.9" y2="174"/></g><g class="c-start"><circle cx="299.0" cy="174" r="4"/></g><circle class="c-dot c-s2" cx="324.9" cy="174" r="5"/><text class="c-note" x="334.9" y="178">packaging by Feb 2028</text>
<text class="c-note" x="366.6" y="208" text-anchor="end">cleanroom Oct 2028</text><g class="c-span"><line x1="376.6" y1="204" x2="451.0" y2="204"/></g><g class="c-start"><circle cx="376.6" cy="204" r="4"/></g><circle class="c-dot c-s2" cx="451.0" cy="204" r="5"/><text class="c-note" x="461.0" y="208">output 2H 2029</text>
<rect class="c-bar" x="224.4" y="227" width="323.6" height="14" rx="2"/>
</svg>
<figcaption>Nvidia spec pages; Rubin Ultra by 2027 from Nvidia's blog of 13 October 2025, as in <a href="/journal/powering-the-rack/">Powering the rack</a>; Micron prepared remarks and Form 10-K (30 September and 9 October 2026); SK Hynix releases listed in the sources, Indiana from its release of 28 August 2026. Open circles are not announced chips or plant milestones; a year with no month is placed at its middle.</figcaption>
</figure>

So a line planned today will run stacks for chips a generation or two after Rubin. My reading: under standard HBM, the maker planned against a published standard. From HBM4E, part of what it builds is set by a buyer, one generation at a time, after the plant is standing. For now the shortage hides that risk. Micron has agreed most of its 2027 HBM already, and SK Hynix expects demand to outrun supply "through 2030". When the shortage ends, the makers will carry the plants; Nvidia will carry the choice.

<a id="heat-wall"></a>
## A custom base die may turn the memory wall into a heat wall

An open question is where NVHBM's heat goes. Nvidia's design moves the memory controller off the processor and into the base die. In a chip package the cooler presses on top, so the base die is the layer furthest from it, under as many as 16 thinned memory dies in an HBM4 stack. Samsung told Hot Chips, the chip design conference, in August 2026 that base-die power density climbs from 0.5 to over 2 watts per square millimetre over the next generations, as ServeTheHome reported its slides, and proposed a dedicated heat path to cope.

Heat costs memory speed. DRAM, the memory cells in every HBM die, leaks charge faster when hot, and Micron's DDR4 datasheets double the refresh rate above 85°C. My inference: refresh is time a die cannot serve reads, so a hot stack gives back some of the bandwidth it was built for. And under NVHBM the heat source is the buyer's design while the memory that suffers is the maker's, so when a stack fails a customer's tests, who owns the fault is not settled in anything I have read.

The test runs through 2027: custom HBM4E qualification news, any thermal derating of 16-high stacks, and new cooling aimed at the stack itself. What would kill the idea: NVHBM ships on time at full height with no derating. The fair counter is already on record. Nvidia claims 15% lower HBM power overall, and Samsung judged the heat of moving the controller into the base die acceptable, so the net heat there may not rise. That is the first thing to check.

## What would prove me wrong

The claim's test is simple. If, by the end of 2027, fewer than two of the three makers say in their own words that they ship HBM built to a customer's design in volume, it breaks. That is a genuine risk. Micron's HBM4E ramps only in 2027, and NVHBM has one named chip partner, Annapurna Labs, Amazon's in-house chip designer, "starting with Trainium4", Amazon's next AI chip, and no published date. Samsung and SK Hynix have said nothing dated about custom volume in releases I could open. HBM4 stays backward compatible with HBM3 controllers, and standard HBM4E remains on sale, so custom memory could stay one buyer's niche through 2027.

Three signs would move me before the deadline: an NVHBM date or a second partner at GTC, Nvidia's annual developer conference, in March 2027; Micron's quarterly remarks as HBM4E ramps through 2027; and Samsung's and SK Hynix's own results. A pass would show that buyers treat memory as worth designing, not prove the memory limit itself. That wider argument weakens if the chips after Rubin and AMD's MI400 stop raising memory per chip.

The strongest point against me is real, and I concede part of it. Nvidia's Groq 3 LPX, an inference rack of 256 chips, keeps part of each word's work in SRAM, very fast memory built into the chip: 500 megabytes and 150 terabytes a second per chip, about eight times one Rubin GPU's HBM. In Nvidia's design, published on 16 March 2026, Rubin GPUs keep attention over the KV cache on HBM, while the LPX chips run the feed-forward layers. So HBM is not the only answer to the memory wall. It does not move me on the claim. A chip built around memory bandwidth is evidence for the wall, and at 500 megabytes a chip, a 70 gigabyte model needs about 140 of them just to hold it, by my arithmetic.

Two other releases would not move me either. Smaller number formats halve the bytes per weight, but with the maths already at four bits, few halvings are left. Overflow is the other: Micron says SSDs, flash storage drives, are now used "for KV cache offload", and SK Hynix is showing high bandwidth flash as a cheaper tier. Both ease capacity more than bandwidth, since the weights still have to be read for every word.

How far ahead each year's HBM is sold is in [the chip supply chain](/journal/the-chip-supply-chain/).

<details class="claims-record">
<summary>The claims on record, word for word</summary>

The test this piece stands behind, quoted word for word:

**From HBM4E, the memory beside AI chips is built to the buyer's design** (31 October 2026)

Claim: "From HBM4E, high-bandwidth memory becomes a part built to the buyer's design: by 31 December 2027, at least two of SK Hynix, Samsung and Micron will have said, in their own results releases, filings or newsroom, that they are in volume production of, or shipping in volume, HBM whose base die carries a customer's own design, such as Nvidia's NVHBM."

Breaks if: "By 31 December 2027, fewer than two of SK Hynix, Samsung and Micron have said, in their own results releases, filings or newsroom, that they are in volume production of, or shipping in volume, HBM whose base die carries a customer's own design, such as Nvidia's NVHBM; a maker's own base die sold as 'custom HBM' does not count unless the maker says it carries the customer's design. Samples, development, qualification, design wins and plans do not count, and nor do press or research-firm reports."

There are no earlier claims on this subject; this is the first.

</details>

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

Rubin's bandwidth is the Vera Rubin NVL72 spec page figure, 19.2 TB/s per GPU, re-read 6 November 2026. A Nvidia platform blog gives "up to 22 TB/s"; the piece uses the product spec page. Memory per chip, which the table shows, has no chart of its own.

Base dies, in each maker's own words. SK Hynix: its plan of April 2024 to use the leading foundry's logic process for HBM4's base die; any report of who makes its shipping HBM4 base die rests on press and research firms. Samsung: its foundry's results of 30 July and 29 October 2026. Micron: its Form 10-K (9 October 2026) says the HBM4 base logic die is "designed and manufactured in-house"; its prepared remarks of 23 September 2025 say it is partnering with the leading foundry to make the HBM4E base logic die "for both standard and customized products". The report that Nvidia asked all three makers for 3 nanometre NVHBM base dies at the leading foundry is TrendForce's (19 October 2026), citing the Seoul Economic Daily, and is press only.

Groq 3 LPX: Nvidia's LPX page (read 6 November 2026) and developer blog (16 March 2026). Per chip, 500 MB of SRAM and 150 TB/s; per rack, 256 chips and 128 GB of SRAM. Nvidia claims up to 35 times the throughput per megawatt of GB200 NVL72 at 400 tokens a second per user. 150 against 19.2 TB/s, and 70 GB over 0.5 GB, are my arithmetic.

The heat beat: Samsung's power density figures are from ServeTheHome's live coverage of Samsung's Hot Chips talk (23 August 2026), not Samsung's own paper, and may carry transcription errors. The refresh rule is from Micron's DDR4 datasheets (a 7.8 µs refresh interval to 85°C, 3.9 µs above); I have not seen HBM4's own figure, so the piece says DRAM in general.

Not used: market shares, HBM prices, yields and any Nvidia and Groq deal value, all press only.

</details>

<section class="exposure">
<h3>Who is exposed if memory becomes a part built to the buyer's design</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>The memory makers</dt>
<dd><span class="names">SK Hynix</span>, <span class="names">Samsung</span> and <span class="names">Micron</span> make HBM, the stacked memory beside AI chips.</dd>
<dt>The base die</dt>
<dd>The leading foundry, which makes logic base dies and packages the stacks beside the processor, and <span class="names">Samsung</span>'s own foundry.</dd>
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

<p class="sources">Sources: Nvidia spec pages for the A100, H100, H200, DGX B200, HGX and Vera Rubin NVL72 (read 30 October 2026), its technical blogs of 17 November 2023 and 22 August 2025, its NVHBM blog (26 August 2026), Groq 3 LPX page and blog (16 March 2026) and Form 10-K (25 February 2026); AMD's MI300X page, its release of 2 June 2024 and Advancing AI deck (12 June 2025); JEDEC's HBM4 release (16 April 2025); SK Hynix releases of 3, 19 and 24 April 2024, 12 September 2025, 22 April, 28 August, 16 October and 28 October 2026; Samsung results of 30 April, 30 July and 29 October 2026; Micron's prepared remarks (23 September 2025 and 30 September 2026), Form 10-K (9 October 2026) and DDR4 datasheets; Samsung's Hot Chips talk as reported by ServeTheHome (23 August 2026); TrendForce (19 October 2026, press). Maths per byte and the read-time sum are my arithmetic. Personal research, not investment advice.</p>
