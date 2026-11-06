---
title: "The chip supply chain's slow parts are sold years before they are made"
date: 2026-07-14
summary: "Most of the companies behind an AI chip could be replaced within months, but a few could not: each is one of very few qualified makers, and each can add supply only by building. Those few, from ASML's scanners to Micron's stacked memory, sell their output a year or more before they make it, and through 2026 they sold further and further ahead. The chip side of AI grows at the pace of its cleanrooms."
category: "Analysis"
cover: "/covers/the-chip-supply-chain.svg"
tags: ["the-stack", "supply-chain", "memory"]
updated: 2026-11-06
updateNote: "Now follows one B200 from printed die to rack and shows the step where every slow part meets, with evidence to 6 November 2026."
draft: false
---

In October, ASML told investors something few suppliers say in a boom. It is the only company that builds the machines that print the finest chips, and it said its planned supply for 2027 and 2028 "will not fully meet the demand" of its customers. Some want to order for 2029 and even 2030.

Nvidia designs the B200, one of the chips behind the AI boom, but makes none of it. Dozens of companies in at least five countries do, and most could be replaced within months. A handful could not.

Those few sell their output a year or more before they make it, because the only way to make more is a new building.

The chip side of AI grows at the pace of its slowest cleanrooms.

"Sold out" covers three different things. Booked means output promised ahead, and buyers in a boom book early and sometimes twice. Short means the maker turns customers away. Stuck means only one or a few qualified makers exist, and more output needs a new cleanroom, the dust-free hall where chips are made. This piece is about stuck, because stuck is why booked and short last.

<details class="analogy">
<summary>The analogy</summary>
<p>Think of a kitchen refit. Cupboards, taps and paint come from any shop this week: those are the connectors and racks. The stone worktop comes from one cutter with one saw, booked a year ahead: that is a stuck step, like the scanner or the memory. A second saw means a new workshop, which is the new cleanroom.</p>
<p>The fitter can start only once the worktop, the sink and the hob have all arrived. That fitting day is packaging, where every slow part meets. More fitters do not help: the kitchen waits for its last delivery.</p>
</details>

Follow the B200 from printed die to rack. It is a worked example from Nvidia's Blackwell generation, the one before this year's Rubin.

First, a scanner prints the chip's dies on a silicon wafer, and only ASML makes the scanner for the finest layers. Second, memory makers stack HBM, towers of memory chips that sit beside the processor, and there are three of them. Third, the board under the chip, the substrate, is built up from an insulating film Ajinomoto supplies for nearly all high-end processors. Fourth, packaging joins dies, memory and board, and for the B200 the leading foundry, the contract maker that also prints the dies, is in practice the only source. Fifth, many makers add boards and racks, swappable within months.

<figure class="chart">
<p class="chart-title">Every slow part meets at the package, and the package binds today</p>
<p class="chart-sub">One Nvidia B200, from printed die to rack, with how far ahead each step is sold</p>
<svg viewBox="0 0 560 196" role="img" aria-label="Diagram of five steps in order. One, print: ASML's EUV scanner prints the dies; ASML says its planned supply for 2027 and 2028 will not fully meet demand. Two, stack: HBM memory from three makers; Micron has agreed the vast majority of its 2027 HBM. Three, board: the substrate, built up from Ajinomoto's film, whose next plant operates in fiscal 2032. Four, package: the dies, memory and board are joined; for the B200 the leading foundry is in practice the only source, and it says packaging limits its customers' growth. This is the choke point. Five, rack: boards, cables and connectors from many makers, replaceable within months.">
<rect class="c-box" x="5.0" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="13.0" y="66">1. Print</text>
<text class="c-note" x="13.0" y="88">ASML scanner</text>
<text class="c-note" x="13.0" y="106">prints dies</text>
<text class="c-note" x="13.0" y="124">Supply short</text>
<text class="c-note" x="13.0" y="142">to 2028</text>
<line class="c-arrow" x1="106.4" y1="97" x2="111.4" y2="97"/><polygon class="c-arrow-head" points="116.4,97 110.4,93 110.4,101"/>
<rect class="c-box" x="117.4" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="125.4" y="66">2. Stack</text>
<text class="c-note" x="125.4" y="88">HBM memory,</text>
<text class="c-note" x="125.4" y="106">three makers</text>
<text class="c-note" x="125.4" y="124">Micron: 2027</text>
<text class="c-note" x="125.4" y="142">mostly agreed</text>
<line class="c-arrow" x1="218.8" y1="97" x2="223.8" y2="97"/><polygon class="c-arrow-head" points="228.8,97 222.8,93 222.8,101"/>
<rect class="c-box" x="229.8" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="237.8" y="66">3. Board</text>
<text class="c-note" x="237.8" y="88">Substrate of</text>
<text class="c-note" x="237.8" y="106">Ajinomoto film</text>
<text class="c-note" x="237.8" y="124">Next plant</text>
<text class="c-note" x="237.8" y="142">fiscal 2032</text>
<line class="c-arrow" x1="331.2" y1="97" x2="336.2" y2="97"/><polygon class="c-arrow-head" points="341.2,97 335.2,93 335.2,101"/>
<rect class="c-zone" x="338.2" y="14" width="108.4" height="144" rx="4"/>
<text class="c-zone-t" x="392.4" y="30" text-anchor="middle">THE CHOKE POINT</text>
<rect class="c-box" x="342.2" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="350.2" y="66">4. Package</text>
<text class="c-note" x="350.2" y="88">Dies, memory</text>
<text class="c-note" x="350.2" y="106">and board meet</text>
<text class="c-note" x="350.2" y="124">B200: one</text>
<text class="c-note" x="350.2" y="142">source</text>
<line class="c-arrow" x1="443.6" y1="97" x2="448.6" y2="97"/><polygon class="c-arrow-head" points="453.6,97 447.6,93 447.6,101"/>
<rect class="c-box" x="454.6" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="462.6" y="66">5. Rack</text>
<text class="c-note" x="462.6" y="88">Boards, cables</text>
<text class="c-note" x="462.6" y="106">connectors</text>
<text class="c-note" x="462.6" y="124">Many makers,</text>
<text class="c-note" x="462.6" y="142">months</text>
<text class="c-lab c-s2t" x="442.6" y="180" text-anchor="end">The foundry says packaging limits its customers</text>
</svg>
<figcaption>ASML results, 14 October 2026; Micron prepared remarks, 30 September 2026; Ajinomoto Kani City release, 7 May 2026; the leading foundry's calls of 16 July and 15 October 2026, which publish no packaging capacity or lead time. My framing of the chain.</figcaption>
</figure>

The fourth step binds today. A package needs every slow part at the same moment, it has one source for this chip, and the foundry itself says packaging is limiting its customers' growth. The scanner's shortfall is still a forecast.

Money buys the building, but not the time to build it. The foundry's chief says a new chip factory takes two to three years just to build, and Ajinomoto will open its next film plant six to nearly seven years after buying the land. So buyers commit early: Nvidia describes lead times of more than a year.

Those are horizons this journal usually finds in [grid connections and transformers](/journal/the-queue-not-the-chip/), not in chips. A part that only one maker can build, and only in a new building, is booked early for a reason.

<hr class="layer">
<p class="layer-label">For investors</p>

<a id="nobody-makes-a-b200-alone"></a>
<a id="the-two-seconds-after-you-hit-send"></a>
## The chip's slow parts are sold years ahead, because only a building adds more

<a id="the-chip-supply-chain"></a>

A few steps of an AI chip are booked years before they are made. ASML, the only maker of EUV scanners, the extreme ultraviolet machines that print a chip's finest layers, said in October that its planned supply for 2027 and 2028 "will not fully meet the demand" of its customers. Micron, one of three makers of HBM, the high bandwidth memory stacked beside AI chips, has agreed "the vast majority" of its 2027 HBM. A new fab at the leading foundry, the contract maker that prints the AI chips themselves, takes three to five years to reach full output.

Chip forecasts are usually built from demand. At the slow steps supply was fixed years earlier by buildings, so the useful question is who has booked them, not who wants chips.

<a id="asml-booked-ahead"></a>

The plainest evidence comes from the one maker that cannot be replaced. ASML is, in its own words, "the world's only manufacturer of EUV lithography systems". On 15 July 2026 its chief executive said it was "close to being fully covered with orders" for 2027. Three months later it said planned supply for 2027 and 2028 would fall short, and that some customers wanted to order "for 2029 and even 2030".

<figure class="chart">
<p class="chart-title">Through 2026, each maker said it was sold further ahead</p>
<p class="chart-sub">The latest calendar year each described as sold, agreed, allocated or short of demand, by the date it said so</p>
<svg viewBox="0 0 560 300" role="img" aria-label="Chart of how far ahead three makers said they were sold, by the date they said it. Seagate: data centre drive supply allocated through 2026 on 27 January 2026, largely through 2027 on 28 April, and the vast majority through 2028 on 27 October. ASML: close to fully covered with orders for 2027 on 15 July 2026; planned supply for 2027 and 2028 will not fully meet demand on 14 October, with some customers interested in ordering for 2029 and 2030. Micron: all 2026 HBM agreed by 17 December 2025, and the vast majority of 2027 by 30 September 2026.">
<g class="c-grid"><line x1="60" y1="250" x2="540" y2="250"/><line x1="60" y1="198" x2="540" y2="198"/><line x1="60" y1="146" x2="540" y2="146"/><line x1="60" y1="94" x2="540" y2="94"/><line x1="60" y1="42" x2="540" y2="42"/></g>
<g class="c-axis"><text x="52" y="254" text-anchor="end">2026</text><text x="52" y="202" text-anchor="end">2027</text><text x="52" y="150" text-anchor="end">2028</text><text x="52" y="98" text-anchor="end">2029</text><text x="52" y="46" text-anchor="end">2030</text><text x="140" y="285" text-anchor="middle">Jan 2026</text><text x="220" y="285" text-anchor="middle">Apr</text><text x="300" y="285" text-anchor="middle">Jul</text><text x="380" y="285" text-anchor="middle">Oct</text><text x="460" y="285" text-anchor="middle">Jan 2027</text></g>
<rect class="c-zone" x="60" y="32" width="480" height="72"/>
<text class="c-note" x="532" y="50" text-anchor="end">Some ASML customers ask to order for 2029 and 2030</text>
<polyline class="c-line c-s1" points="162.8,250 242.6,198 402.1,146"/>
<circle class="c-dot c-s1" cx="162.8" cy="250" r="3.5"/><circle class="c-dot c-s1" cx="242.6" cy="198" r="3.5"/><circle class="c-dot c-s1" cx="402.1" cy="146" r="3.5"/>
<polyline class="c-line c-s2" points="311,198 390.7,146"/>
<circle class="c-dot c-s2" cx="311" cy="198" r="3.5"/><circle class="c-dot c-s2" cx="390.7" cy="146" r="3.5"/>
<polyline class="c-line c-s3" points="126.8,250 378.5,198"/>
<circle class="c-dot c-s3" cx="126.8" cy="250" r="3.5"/><circle class="c-dot c-s3" cx="378.5" cy="198" r="3.5"/>
<text class="c-lab c-s2t" x="404.7" y="136">ASML scanners</text>
<text class="c-lab c-s1t" x="414.1" y="166">Seagate drives</text>
<text class="c-lab c-s3t" x="390.5" y="218">Micron HBM</text>
</svg>
<figcaption>ASML results and transcript, 15 July and 14 October 2026; Seagate supplementals, 27 January, 28 April and 27 October 2026; Micron remarks, 17 December 2025 and 30 September 2026. Wording differs by maker, from "close to being fully covered" to "will not fully meet the demand"; each is quoted in the figures below. SK Hynix is not drawn: its release of 28 October 2026 puts more than half of its 2027 and 2028 capacity under long-term agreements, and press accounts of its call report memory effectively sold out through 2029.</figcaption>
</figure>

The other slow steps moved the same way through 2026. Micron had agreed all its 2026 HBM by December 2025, and most of 2027 by 30 September 2026. Seagate, one of three hard drive makers, went from allocated through 2026 in January to the vast majority of its data centre drives through 2028 in October. Buyers commit this early because they know the clock. The annual report of Nvidia, which designs the B200 but makes none of it, describes "extended lead times" of more than 12 months, and separately deposits and long-term capacity commitments.

<a id="seagate-sells-the-terabyte"></a>

Seagate stays on watch rather than in the claim. It meets growth "by increasing capacity per drive rather than increasing drive unit production", so it shows few makers at work but cannot test the building clock.

## Six things keep the slow steps slow, and a bigger cheque fixes none of them

Each slow step is held by a monopoly, a test or a building, often all three.

**One maker.** ASML is the only maker of EUV scanners. A rival scanner cannot be bought at any price; one would first have to be built, then qualified.

**A choke inside the choke.** ASML's output is "limited by the production capacity" of Carl Zeiss SMT, sole supplier of its critical optics. The only maker has an only supplier. Its planned step of about 30% for 2027 fits its "existing footprint", in a third-party transcript of its July call.

**Qualification.** A new part must pass the customer's own testing, months or years of it, before it is trusted. Ajinomoto, whose insulating film builds up the board under nearly all high-end processors, says customer trust "serves as a barrier for new entrants".

<a id="tsmc-says-it-is-the-bottleneck"></a>

**The building.** The leading foundry's chief said on 15 January 2026 that a new fab takes two to three years to build, and on 16 April that it needs one to two more to ramp. Ajinomoto bought land at Kani City in May 2026 for a film plant that operates in fiscal 2032.

<a id="the-countertop-is-the-bottleneck"></a>
<a id="ajinomoto-grows-with-the-package"></a>

**Each chip takes more.** Nvidia's H100 of 2022 carried 80 gigabytes of memory, and Rubin, this year's flagship, carries 288. The board under a high-end package grew from about 70 millimetres square with nine copper wiring layers up to 2023 to about 100 with eleven in 2026. By my arithmetic, area times layers, that board takes about two and a half times the film.

**Everyone books at once.** Buyers know the clock, so they book early and sometimes twice. That lengthens the queue even when the true need is smaller.

## Forecasts run on the chip's yearly clock, and supply on the building's

The market misses the slow steps because it models the fast one. Nvidia launched Blackwell in 2024, Blackwell Ultra in 2025 and Rubin in 2026, and chip forecasts follow that yearly clock.

The slow steps grow only by cleanroom, the dust-free hall where chips are made. A fab begun today reaches full output when Rubin's third to fifth successors would be on sale, if the yearly pace holds. Supply for 2029 is being settled by bookings made now, and a designer that books only once its chip is finished joins the back of the line. Each maker's own dates for new supply show how far out that line runs.

<figure class="chart">
<p class="chart-title">New supply for the slow steps arrives from 2027 into the 2030s</p>
<p class="chart-sub">When each maker's added capacity starts, by its own dates</p>
<svg viewBox="0 0 560 286" role="img" aria-label="Timeline of new supply. ASML plans about 30 per cent more low NA EUV capacity for 2027 within its existing buildings. Micron's Idaho fab ID1 starts output in mid 2027, ID2 in late 2028, and its New York fab in 2030. A new fab at the leading foundry begun today would take two to three years to build and one to two more to ramp, three to five years in all. Ajinomoto bought land at Kani City in May 2026 for a film plant operating in fiscal 2032, which runs from April 2032 to March 2033.">
<g class="c-grid"><line x1="200" y1="20" x2="200" y2="246"/><line x1="248.6" y1="20" x2="248.6" y2="246"/><line x1="297.1" y1="20" x2="297.1" y2="246"/><line x1="345.7" y1="20" x2="345.7" y2="246"/><line x1="394.3" y1="20" x2="394.3" y2="246"/><line x1="442.9" y1="20" x2="442.9" y2="246"/><line x1="491.4" y1="20" x2="491.4" y2="246"/><line x1="540" y1="20" x2="540" y2="246"/></g>
<g class="c-axis"><text x="200" y="266" text-anchor="middle">2026</text><text x="297.1" y="266" text-anchor="middle">2028</text><text x="394.3" y="266" text-anchor="middle">2030</text><text x="491.4" y="266" text-anchor="middle">2032</text><text x="190" y="44" text-anchor="end">ASML, about 30% more</text><text x="190" y="80" text-anchor="end">Micron Idaho ID1</text><text x="190" y="116" text-anchor="end">Micron Idaho ID2</text><text x="190" y="152" text-anchor="end">Micron New York</text><text x="190" y="188" text-anchor="end">A new fab begun now</text><text x="190" y="224" text-anchor="end">Ajinomoto, Kani City</text></g>
<line class="c-today" x1="240.2" y1="14" x2="240.2" y2="246"/><text class="c-today-t" x="240.2" y="12" text-anchor="middle">today</text>
<g class="c-span"><line x1="240.2" y1="184" x2="483" y2="184"/><line x1="216.8" y1="220" x2="503.6" y2="220"/></g><g class="c-start"><circle cx="240.2" cy="184" r="4"/><circle cx="216.8" cy="220" r="4"/></g><g class="c-end"><circle cx="248.6" cy="40" r="4.5"/><circle cx="272.9" cy="76" r="4.5"/><circle cx="338.4" cy="112" r="4.5"/><circle cx="418.6" cy="148" r="4.5"/><circle cx="385.9" cy="184" r="4.5"/><circle cx="483" cy="184" r="4.5"/><circle cx="503.6" cy="220" r="4.5"/></g><g class="c-endt"><text x="257.6" y="44">2027, same buildings</text><text x="281.9" y="80">mid 2027</text><text x="347.4" y="116">late 2028</text><text x="427.6" y="152">2030</text><text x="483" y="175" text-anchor="end">3 to 5 years</text><text x="503.6" y="211" text-anchor="end">fiscal 2032</text></g>
</svg>
<figcaption>ASML results, 15 July 2026; Micron prepared remarks of 30 September 2026 and Form 10-K (9 October 2026); the leading foundry's calls of 15 January and 16 April 2026; Ajinomoto Kani City release, 7 May 2026. Hollow dot: land bought, or today. The new-fab row is my arithmetic from its stated ranges, not a named plant. Ajinomoto's fiscal 2032 runs from April 2032 to March 2033.</figcaption>
</figure>

## Four sets of terms carry the argument

**Low NA and High NA EUV.** NA, numerical aperture, is how wide a cone of light the optics gather; higher prints finer. Low NA is ASML's standard scanner, behind its 2026 capacity of around 65 and named in my test. High NA is the newer, finer machine: a standard oven against a prototype, never counted together.

**Wafer, die, interposer and substrate.** The wafer is the 300 millimetre silicon disc a scanner prints on; a die is one chip cut from it. The interposer is the silicon tray holding dies and HBM side by side, and the substrate is the board below, built up with Ajinomoto's film: dough, biscuit, tray and table.

**HBM and the trade ratio.** HBM stacks memory dies and wires them through vertically, a tower block beside the processor where ordinary memory is a bungalow. The trade ratio is the wafer HBM needs per bit against standard memory.

**Agreed, allocated and short.** Micron says "agreed", Seagate "allocated", ASML "will not fully meet the demand". They differ in strength, like a booked table, a seating plan and a queue at the door, so I quote the exact word.

## About three times the wafer is a ratio of silicon, and it does not multiply

<a id="micron-three-times-the-wafer"></a>

The number behind the memory half of the argument is Micron's. HBM3E, its current stacked memory, "consumes approximately three times the wafer supply" of DDR5, standard server memory, per bit. It is a ratio of wafer, not of price or of chips, and it means each HBM bit added takes wafer from ordinary memory.

Micron does not publish why it is about three. My understanding is that each HBM die is larger per bit, because the vertical wiring and the wide interface take area, and that stacking many dies loses some to yield. Micron gives the ratio, not the recipe.

The trap is to multiply it by the memory per chip. Rubin carries 3.6 times the H100's memory, but the H100 already used HBM, so the two are separate facts. And the three times compares HBM3E with DDR5; Micron's annual report says only that HBM needs "a higher number of wafers and more cleanroom space" per bit.

<figure class="chart">
<p class="chart-title">Each AI chip carries 3.6 times the memory, at about three times the wafer per bit</p>
<p class="chart-sub">Wafer needed for the same bits, HBM3E against DDR5; and memory per Nvidia chip, in gigabytes</p>
<svg viewBox="0 0 560 210" role="img" aria-label="Two groups of bars. Wafer needed for the same number of bits: DDR5, ordinary memory, 1 times; HBM3E, AI memory, about 3 times, by Micron. Memory carried by each chip: Nvidia's H100 of 2022 carries 80 gigabytes and Rubin of 2026 carries 288, 3.6 times as much.">
<text class="c-note" x="10" y="24">Wafer for the same number of bits</text>
<text class="c-note" x="10" y="122">Memory carried by each chip</text>
<g class="c-axis"><text x="160" y="51" text-anchor="end">DDR5, ordinary memory</text><text x="160" y="87" text-anchor="end">HBM3E, AI memory</text><text x="160" y="149" text-anchor="end">Nvidia H100, 2022</text><text x="160" y="185" text-anchor="end">Nvidia Rubin, 2026</text></g>
<rect class="c-bar" x="170" y="36" width="90" height="20" rx="2"/><text class="c-lab c-s2t" x="268" y="51">1x</text>
<rect class="c-bar" x="170" y="72" width="270" height="20" rx="2"/><text class="c-lab c-s2t" x="448" y="87">about 3x</text>
<rect class="c-bar c-alt" x="170" y="134" width="75.0" height="20" rx="2"/><text class="c-lab c-s3t" x="253.0" y="149">80 GB</text>
<rect class="c-bar c-alt" x="170" y="170" width="270.0" height="20" rx="2"/><text class="c-lab c-s3t" x="448.0" y="185">288 GB</text>
<line class="c-base" x1="170" y1="30" x2="170" y2="98"/><line class="c-base" x1="170" y1="128" x2="170" y2="196"/>
</svg>
<figcaption>Micron prepared remarks, 20 March 2024; Nvidia spec pages, as in <a href="/journal/memory-not-maths/">Memory, not maths</a>. My framing. The two are not multiplied: the H100 already used HBM, and Micron's three times compares HBM3E with DDR5.</figcaption>
</figure>

The ratio is why the squeeze spills over, because both kinds of memory come out of the same cleanrooms. Micron expects DRAM as a whole to stay supply constrained in 2027 and 2028, so anyone who needs ordinary server memory pays for the AI chip's. [Memory, not maths](/journal/memory-not-maths/) follows that thread.

## Packaging binds today, and it has to be boxed in because nobody publishes its size

Packaging, where every slow part meets, binds now, and nobody outside the leading foundry can count it. The foundry says packaging capacity is limiting its customers' growth, yet publishes no capacity or lead time.

The real question is whether packaging caps AI chip shipments, and when that eases. Rather than guess a number, I would box it in from four sides. From above, buyers' spending on AI accelerators, divided by a price per package, gives units. From below, the foundry's spending on packaging, new plants and their dates, and orders for bonding and test tools give a ceiling on supply.

The other two sides come from the inputs. As a tracer, every HBM stack ends up in a package, so the bits memory makers say are booked, divided by memory per chip, give the high-end packages memory allows. As a ceiling, no package can be made without its interposer, substrate and film.

Capacity is quoted in wafers, but packages are growing, so a wafer count can rise while the package count stays flat. Where the four sides disagree is where the research lies, and the answer is a range tested with people in the chain, not a point.

## The gains collect at the one-maker steps, the memory makers and the board makers

The one-maker steps set terms when supply is short and no second source exists. They are ASML; ZEISS, which makes its optics; Trumpf, which makes the lasers inside its scanners; and Ajinomoto for the film. Their limit is their own buildings.

The memory makers carry the cycle. Micron, SK Hynix and Samsung, the three HBM makers, are booked years ahead, now partly under long-term agreements, and a booked boom pays well. But memory has a long record of gluts, and SK Hynix's third quarter operating margin of 80% invites new supply.

The board makers are the quiet position. Ibiden and Unimicron make the substrates under the package, every package from any packager needs one, and boards grow by area. Intel, which sells its EMIB packaging to other chipmakers, has named an industry-wide shortage of advanced organic substrates as a limit on that packaging.

On the other side sit chip designers without committed capacity and buyers who order late, because supply goes to whoever commits first.

## What would prove me wrong

The claim has three ways to fail, and they strike at different parts of it.

The first is ASML's 2029. If ASML, in results published between 1 December 2027 and 31 March 2028, does not describe its 2029 supply of low NA EUV as close to fully covered or short of demand, the claim breaks. The early sign is the size of its 2028 step: ASML is already studying one beyond 30%, and its Capital Markets Day, an investor day, on 10 June 2027 is where I expect to learn it.

The second is Micron's 2029 HBM. If by around December 2028 Micron has not said most of its 2029 HBM is agreed, or reports unsold HBM and blames demand, the claim breaks. The test asks about 2029 because Micron's new Idaho fabs open in mid 2027 and late 2028, so 2029 comes after both.

The third is a second source. If Intel's EMIB packaging qualifies in volume and a flagship accelerator moves to it, the one-maker trait weakens at packaging. It is not in my dated test, but it attacks the mechanism, so I watch it.

Underneath, the claim rests on two legs. The booking is behaviour, driven by fear of missing supply, so it can unwind in a slowdown or a double order found out; the first two tests attack it, and memory's glut record is its soft spot. The building clock is construction, which money cannot hurry. The third test nibbles at it, but a second packager also needs a building and a qualification. The second leg is why the first exists.

The objection I meet most is that long bookings are just double ordering in a boom. Buyers do order twice, and the filings cannot separate hoarding from scarcity. But a double order does not create a second ASML, and a hoarded scanner still had to be built in the same cleanroom.

## SK Hynix has pushed memory's horizon out to 2029

SK Hynix, one of the three HBM makers, has turned bookings into contracts. Its results release of 28 October 2026 says long-term agreements with 14 major customers cover more than 50% of its 2027 and 2028 capacity, and it expects demand to exceed supply through 2030. Press accounts of its call report it describing DRAM and HBM as effectively sold out through 2029, two years past Micron's stated horizon.

Some of this is weaker than it looks. Only just over half of 2027 and 2028 is under contract, and an 80% margin is what a peak looks like.

But contracts move the risk onto buyers, and new supply runs on the building clock, dated in advance: Micron's Idaho fabs in mid 2027 and late 2028, and New York in 2030. A glut would show in dated plant openings before it showed in prices. My test stays on Micron's 2029 HBM, judged around December 2028.

## A second packager is forming, and it meets the same board

For custom chips a second route through packaging is forming. Intel said on its call of 29 October 2026 that EMIB sees "significant external customer traction", and its chief expects customers ready to announce within two quarters.

That much I grant: packaging is moving from one maker to a few for custom chips, though the leading foundry stays in practice the only source for the B200.

The change is not here yet, since the customers are still to be named. It came after years of qualification, which is the trait at work rather than failing. And on the same call Intel named the substrate shortage as its limit. The single source cracks; the building clock does not, and the bottleneck moves down the package rather than disappearing.

<a id="the-board-underneath"></a>
## The bottleneck may walk down the package, to the board underneath

My hypothesis is that more packaging pulls harder on the film, not less. Ajinomoto's film is sold by area times layers, not by chip, and Ajinomoto expects the board under a high-end package to reach about 120 millimetres square with thirteen layers from 2031. The leading foundry plans to bring packages of 9.5 times the largest area a scanner prints in one shot to volume production in 2027, on its release of 23 April 2025. Press reports of its slides put the board under a package of about nine such fields beyond 120 millimetres square.

If that roadmap ships on time, my inference is that the largest boards reach the film maker's 2031 size about four years early. Ajinomoto aims its current expansion at demand to 2030, and its next plant opens in fiscal 2032. A second packager would not relieve that, because it needs the same boards.

The test is Ajinomoto's half-year volume split and any capacity brought forward, Ibiden's and Unimicron's capital spending, and whether the 9.5-field package reaches volume in 2027. The idea dies if that class stays a small share of packages, so that 2031 describes the typical board, or if Ajinomoto adds film inside existing plants faster than board area grows. Until then the film is not shown to bind before 2030, and I watch it.

## At every scale, the slow part is booked before the chip exists

At the scale of the wafer, the scanner is short of demand to 2028 and memory is reported sold out to 2029 by one of its makers. The wafer is spoken for before the chip that uses it is designed.

At the scale of the package, dies, memory, interposer and film must all arrive at once. Packages are growing towards nine scanner fields in area, so each wafer yields fewer of them, and the second packager now forming meets the same board.

At the scale of the building, a fab takes three to five years to full output, and it needs power too: on 24 June 2026 Micron named "the need for enhanced energy infrastructure" among the limits on new fabs. Under the chip's clock sit the grid's, the queues in [Johor and Singapore](/journal/the-queue-not-the-chip/) and [the equipment queue](/journal/the-equipment-queue/), and at each scale whoever booked first gets the chip.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

The test this piece stands behind, quoted word for word:

**The chip supply chain's slow parts stay sold more than a year ahead** (30 October 2026)

Claim: "In the AI chip supply chain, the parts that only one or a few qualified makers can supply, and that grow only through new cleanrooms, stay sold more than a year ahead. In its results published between 1 December 2027 and 31 March 2028, ASML will describe its 2029 low NA EUV supply as close to fully covered by orders or short of demand, and by its fiscal first quarter 2029 results, around December 2028, Micron will have said most of its calendar 2029 HBM supply is agreed."

Breaks if: "ASML, in its results published between 1 December 2027 and 31 March 2028, says its 2029 low NA EUV capacity exceeds customer orders, or does not describe 2029 as close to fully covered or short of demand; or Micron, by its fiscal first quarter 2029 results (around December 2028), has not said most of its calendar 2029 HBM supply is agreed, or reports unsold HBM and attributes it to customer demand. A shortfall caused by late cleanrooms or suppliers supports the claim rather than breaking it."

Four earlier claims on the chip's slow parts:

**The leading foundry's chief says the AI bottleneck is its factories, not the power grid** (2 October 2026)

Claim: "On today's horizon, TSMC's factories bind before the grid does. Over the longer run, I still expect the grid to be the slower clock."

Breaks if: "For today: the leading foundry's tightness eases while data centres with chips on order still wait for power. For the longer run: the leading foundry still calls capacity tight in 2028 while grid connection waits shorten."

Where later evidence bears on it: the near half holds. On the leading foundry's 15 October 2026 call its chief said the gap between demand and supply is "still quite big", the finance chief called tool supply tight, and the chief said the foundry's own checks on US data centre power were "so far so good". ASML's warning is a forecast of tool supply and does not test the 2028 half, which is still open.

**ASML's EUV machines are booked a year or two ahead, like a grid connection** (7 October 2026)

Claim: "ASML's EUV machines are sold out and committed a year or two ahead, and their number grows only as fast as ZEISS optics and ASML's cleanrooms allow, about 30 per cent a year, so a chipmaker adding leading-edge AI capacity must commit to scanners a year or two ahead, much as a data centre books a grid connection."

Breaks if: "The booking half fails if ASML says it has EUV capacity beyond what customers have ordered; or ships more than 10 per cent fewer low NA EUV systems than its stated capacity (around 65 for 2026, around 85 for 2027) and itself attributes the shortfall to customer demand or pushed-out orders; or by its fourth quarter 2026 results (January 2027) no longer describes 2027 as close to fully covered with orders; or says its EUV order lead times are shortening. The growth half fails if ASML raises its stated low NA EUV capacity by more than 40 per cent in a single year, or announces new EUV cleanroom space or a second source for its optics. A shortfall caused by ZEISS or other suppliers supports the claim rather than breaking it."

Where later evidence bears on it: the booking half has firmed. On 14 October ASML said its supply planned for 2027 and 2028 "will not fully meet the demand". The growth half is at risk: ASML is studying a 2028 step beyond 30%. It breaks above 40% in one year, or if ASML announces new EUV cleanroom space, which a step beyond two 30% steps may need.

**As AI chip packages grow, Ajinomoto's insulating film grows with them** (7 October 2026)

Claim: "Ajinomoto's build-up film is used by the area and layer count of each chip package, so as AI packages grow wider and taller its film volume shifts to AI servers faster than chip counts imply, and because a rival film takes a long time to qualify, Ajinomoto keeps that growth at high margins."

Breaks if: "In any of Ajinomoto's annual results presentations through fiscal 2029 (the year to March 2030), servers and networks fall below 70 per cent of its ABF volume by application, its fiscal 2025 level (the split is rounded to five points, so a flat 70 per cent passes); or the business profit margin of its Functional Materials business, part of the Healthcare and Others segment, falls below 50 per cent in a year when that business's sales still grow. Ajinomoto discloses the margin only as rounded wording ("over 50%"); if it stops doing so, the test rests on the volume split alone."

Where later evidence bears on it: holding. Ajinomoto's results data sheets print Functional Materials sales and business profit in yen, so the margin can be computed exactly, and both halves hold.

**Micron sells AI memory before the year starts, and each bit takes three times the wafer** (7 October 2026)

Claim: "Micron sells most of each year's HBM before that year starts, and because each HBM bit takes about three times the wafer of ordinary DRAM, every year HBM grows faster than conventional DRAM it takes wafers from ordinary memory and keeps that market short too, through calendar 2028."

Breaks if: "The first half fails if, by its fiscal first quarter 2028 results (around December 2027), Micron has not said most of its calendar 2028 HBM supply is agreed; or if Micron reports unsold HBM or cuts HBM output and itself attributes it to customer demand. The second half fails if, before the end of calendar 2028, Micron stops expecting the DRAM industry to be supply-constrained in 2027 or 2028 while still expecting industry HBM bits to grow faster than conventional DRAM; or if Micron states that any current HBM generation needs less than about three times the wafer of DDR5 per bit. A shortage prolonged by late cleanrooms supports the claim rather than breaking it."

Where later evidence bears on it: both halves hold, on Micron's September remarks.

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

Each slow step, with what is committed ahead in the company's own words:

| Step | Who can make it | Committed ahead, in the company's words | What adds supply, and when | Source, dated |
|---|---|---|---|---|
| EUV scanner | ASML only; optics from ZEISS only | Expects to ship around 65 low NA machines, its 2026 capacity; supply planned for 2027 and 2028 "will not fully meet the demand" | About 30% more for 2027 in existing buildings; 2028 under study | ASML, 15 July and 14 October 2026 |
| Wafers and packaging | The leading foundry, in practice the only packaging source for the B200; Intel's EMIB courts custom chips | No lead time published; packaging tight enough to limit customers' growth | A new fab: two to three years to build, one to two to ramp | The leading foundry's calls, 15 January, 16 April, 16 July 2026; Intel call, 29 October 2026 |
| Substrate film | Ajinomoto, "product of choice for nearly all high-performance CPUs" | No order horizon published | Gunma line 2025; Kani City, Gifu, operating fiscal 2032 | Ajinomoto, 7 May and September 2026 |
| HBM wafers | Micron, SK Hynix, Samsung | All of 2026 agreed by December 2025; "the vast majority" of 2027 by September 2026 | Idaho ID1 mid 2027, ID2 late 2028, New York 2030 | Micron, 17 December 2025, 30 September 2026 |
| Nearline hard drives | Seagate, Western Digital, Toshiba | "Vast majority" of data centre nearline supply allocated through 2028 | More terabytes per drive, not more drives | Seagate, 27 October 2026 |
| The buyer | Nvidia | "Extended lead times" of more than 12 months; separately, deposits and long-term capacity commitments | Not Nvidia's to add | Nvidia 10-K, 25 February 2026 |

The horizon chart, point by point. Seagate: allocated through 2026 (supplemental, 27 January 2026), largely through 2027 (28 April), the vast majority of data centre nearline supply through 2028, with some cloud agreements through 2030 (27 October). ASML: "close to being fully covered with orders" for 2027 (chief executive, ASML's own transcript, 15 July 2026); 2027 and 2028 "will not fully meet the demand" (14 October). Micron: all 2026 HBM agreed (December 2025); "the vast majority of our calendar 2027 HBM bit supply" (30 September 2026).

Other figures. Ajinomoto expects the board to reach about 120 millimetres square with thirteen layers from 2031. Its Functional Materials business earned a business profit margin of 54.2% in fiscal 2025 and 57.7% in April to June 2026, on its results data sheets of 7 May and 6 August 2026; its ASV Report 2026 says customer trust "serves as a barrier for new entrants", and how long a rival takes to qualify is unpublished. Micron's 10-K says the base logic die under each HBM4 stack is "designed and manufactured in-house", so its HBM4 stacks meet the leading foundry only at packaging; for HBM4E, which ramps in 2027, Micron said on 23 September 2025 that the leading foundry will make the base die, for standard and custom versions. SK Hynix said in April 2024 it would use the leading foundry's logic process for its HBM4 base die; Samsung makes its own in its foundry. Micron expects DRAM to stay supply constrained in 2027 and 2028. Seagate shipped 26% more exabytes in the December quarter of 2025 "on similar number of units". On 15 October 2026 the leading foundry's finance chief said "the tool supply is tight". SK Hynix's third quarter 2026: revenue of 104.6 trillion won, operating profit of 83.3 trillion, an 80% margin, with long-term agreements with 14 major customers (release, 28 October 2026); "sold out through 2029" is from press accounts of its call. Intel's EMIB remarks are from its call of 29 October 2026; reported names of custom chips moving to it are press only and not used. The leading foundry's 9.5-field package is from its release of 23 April 2025; the board beyond 120 millimetres is from press reports of its 2024 slides.

Method. The horizons fit scarcity, but also buyers locking in supply in a boom, and the filings cannot separate the two. They do show supply: each maker grows only as fast as a building it has not finished. "Existing footprint" is from a third-party transcript of ASML's July call.

</details>

<section class="exposure">
<h3>Who is exposed if the chip side's slow parts stay sold years ahead</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>The one-maker steps</dt>
<dd><span class="names">ASML</span> makes EUV scanners, <span class="names">ZEISS</span> their optics, <span class="names">Trumpf</span> their lasers. <span class="names">Ajinomoto</span> makes build-up film.</dd>
<dt>Factories and packaging</dt>
<dd>The leading foundry makes and packages AI chips; <span class="names">Intel</span> offers its EMIB packaging to others. <span class="names">Ibiden</span> and <span class="names">Unimicron</span> make package substrates.</dd>
<dt>Memory and storage</dt>
<dd><span class="names">Micron</span>, <span class="names">SK Hynix</span> and <span class="names">Samsung</span> make HBM. <span class="names">Seagate</span>, <span class="names">Western Digital</span> and <span class="names">Toshiba</span> make hard drives.</dd>
<dt>The buyer</dt>
<dd><span class="names">Nvidia</span> designs AI chips.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Chip designers without committed capacity, and buyers who order late.</dd>
<dt>Where I stop</dt>
<dd>I have no view on the memory equities.</dd>
</dl>
</section>

---

<p class="sources">Sources: ASML Annual Report 2025 on Form 20-F (25 February 2026) and its results of 15 July and 14 October 2026; the leading foundry's earnings calls of 15 January, 16 April, 16 July and 15 October 2026, its third quarter management report (15 October 2026) and its symposium release (23 April 2025); SK Hynix's third quarter results release (28 October 2026); Intel's earnings call (29 October 2026); Ajinomoto's results presentation and Kani City release (7 May 2026), ASV Report 2026 (September 2026) and results data sheets; Micron's earnings calls and prepared remarks of 20 March 2024, 23 September and 17 December 2025, 24 June and 30 September 2026, and its Form 10-K (9 October 2026); Seagate's supplemental information of 27 January, 28 April and 27 October 2026, its call of 28 July 2026 and Form 10-K (4 August 2026); Nvidia's Blackwell pages and Form 10-K (25 February 2026). Personal research, not investment advice.</p>
