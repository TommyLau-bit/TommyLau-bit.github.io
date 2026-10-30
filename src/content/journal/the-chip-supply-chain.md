---
title: "The chip supply chain's slow parts are sold years before they are made"
date: 2026-07-14
updated: 2026-10-31T08:00:00+08:00
updateNote: "Rewritten on 31 October 2026 as one story with three charts; earlier claims are kept word for word at the end."
summary: "Most of the companies behind an AI chip could be replaced within months, but a few could not: each is one of very few qualified makers, and each can add supply only by building. Those few, from ASML's scanners to Micron's stacked memory, sell their output a year or more before they make it, and through 2026 they sold further and further ahead. The chip side of AI grows at the pace of its cleanrooms."
category: "Analysis"
cover: "/covers/the-chip-supply-chain.svg"
tags: ["the-stack", "supply-chain", "memory"]
draft: false
---

In October, ASML told its investors something few suppliers say in a boom. ASML is the only company that builds the machines that print the finest chips, and it said its planned supply for 2027 and 2028 "will not fully meet the demand" of its customers. Some want to order for 2029 and even 2030.

Nvidia designs the B200, one of the chips behind today's AI boom, but makes none of it. Dozens of companies in at least five countries do. Most of them could be replaced within months. A handful could not.

Those few sell their output a year or more before they make it, because the only way to make more is a new building. The chip side of AI grows at the pace of its slowest cleanrooms, and they are booked years ahead.

The slow parts share three traits. There is one maker, or very few. A rival's part must pass qualification, the months or years of testing a customer runs before trusting it. And more output needs new plant: a cleanroom, the dust-free hall where chips are made, or a whole factory.

Money buys the building, but not the time to build it. TSMC's chief says a new chip factory takes two to three years just to build. Ajinomoto, which makes the insulating film inside chip packages, will open its next film plant six to nearly seven years after it bought the land.

Buyers know this, so they commit early. Nvidia's annual report describes lead times of more than a year, which it secures with deposits and capacity commitments. Micron has already agreed most of next year's stacked memory, and Seagate has allocated most of its data centre hard drives through 2028.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a kitchen refit. Cupboards, taps and paint come from any shop this week. The stone worktop comes from one cutter with one saw, booked a year ahead, and a second saw means building a new workshop.</p>
<p>Hiring more fitters does not help. The kitchen is finished when the worktop arrives. An AI chip has five or six worktops, each from a different cutter.</p>
</details>

Those are horizons this journal usually finds in [grid connections and transformers](/journal/the-queue-not-the-chip/), not in chips. A booking is not proof of scarcity on its own, because buyers in a boom order early and sometimes twice. But a part that only one maker can build, and only in a new building, is booked early for a reason.

<hr class="layer">
<p class="layer-label">For investors</p>

<a id="nobody-makes-a-b200-alone"></a>
<a id="the-two-seconds-after-you-hit-send"></a>
## Most of a chip can be bought this year; a few steps cannot

An AI chip passes through many hands, and only a few of them are hard to replace. Nvidia's B200 holds 208 billion transistors on two dies, the chips cut from a wafer, made by TSMC; Nvidia's 10-K names SK Hynix, Micron and Samsung for its memory. My own rough sort runs from parts swapped in months, such as rack assembly and connectors, to steps with no second source, EUV machines first and Ajinomoto's film close by.

<figure class="chart">
<p class="chart-title">Behind one AI chip, each slow step has one maker or a handful</p>
<p class="chart-sub">The steps behind an Nvidia B200, with how far ahead each is sold, in its maker's words</p>
<svg viewBox="0 0 560 222" role="img" aria-label="Diagram of the steps behind one Nvidia B200. ASML's EUV scanner, with planned supply short of demand through 2028, prints TSMC's wafer, for which TSMC gives no lead time. TSMC packages the chip, a step tight enough to limit customers' growth. Ajinomoto's build-up film goes into the package, with its next plant operating in fiscal 2032. Micron's HBM, one of three makers, goes into the package, with most of 2027 agreed. The finished B200 goes to Nvidia, the buyer, and the data it produces is stored on hard drives from makers such as Seagate, allocated through 2028.">
<rect class="c-box" x="10" y="30" width="125" height="56" rx="4"/>
<text class="c-box-t" x="72.5" y="54" text-anchor="middle">ASML scanner</text>
<text class="c-note" x="72.5" y="73" text-anchor="middle">short to 2028</text>
<rect class="c-box" x="148" y="30" width="125" height="56" rx="4"/>
<text class="c-box-t" x="210.5" y="54" text-anchor="middle">TSMC wafer</text>
<text class="c-note" x="210.5" y="73" text-anchor="middle">no figure given</text>
<rect class="c-box" x="286" y="30" width="125" height="56" rx="4"/>
<text class="c-box-t" x="348.5" y="54" text-anchor="middle">TSMC package</text>
<text class="c-note" x="348.5" y="73" text-anchor="middle">limits customers</text>
<rect class="c-box" x="424" y="30" width="125" height="56" rx="4"/>
<text class="c-box-t" x="486.5" y="54" text-anchor="middle">Nvidia B200</text>
<text class="c-note" x="486.5" y="73" text-anchor="middle">the buyer</text>
<rect class="c-box" x="148" y="146" width="125" height="56" rx="4"/>
<text class="c-box-t" x="210.5" y="170" text-anchor="middle">Ajinomoto film</text>
<text class="c-note" x="210.5" y="189" text-anchor="middle">plant fiscal 2032</text>
<rect class="c-box" x="286" y="146" width="125" height="56" rx="4"/>
<text class="c-box-t" x="348.5" y="170" text-anchor="middle">Micron HBM</text>
<text class="c-note" x="348.5" y="189" text-anchor="middle">2027 mostly agreed</text>
<rect class="c-box" x="424" y="146" width="125" height="56" rx="4"/>
<text class="c-box-t" x="486.5" y="170" text-anchor="middle">Seagate drives</text>
<text class="c-note" x="486.5" y="189" text-anchor="middle">allocated to 2028</text>
<line class="c-arrow" x1="135" y1="58" x2="142" y2="58"/><polygon class="c-arrow-head" points="148,58 141,62 141,54"/>
<line class="c-arrow" x1="273" y1="58" x2="280" y2="58"/><polygon class="c-arrow-head" points="286,58 279,62 279,54"/>
<line class="c-arrow" x1="411" y1="58" x2="418" y2="58"/><polygon class="c-arrow-head" points="424,58 417,62 417,54"/>
<line class="c-arrow" x1="261" y1="146" x2="296.7" y2="91"/><polygon class="c-arrow-head" points="300,86 299.5,94 292.8,89.7"/>
<line class="c-arrow" x1="348.5" y1="146" x2="348.5" y2="92"/><polygon class="c-arrow-head" points="348.5,86 352.5,93 344.5,93"/>
<line class="c-arrow" x1="486.5" y1="86" x2="486.5" y2="140"/><polygon class="c-arrow-head" points="486.5,146 482.5,139 490.5,139"/>
</svg>
<figcaption>ASML results, 14 October 2026; TSMC calls of 16 July and 15 October 2026; Ajinomoto release, 7 May 2026; Micron prepared remarks, 30 September 2026; Seagate supplemental, 27 October 2026. Micron is one of three HBM makers, with SK Hynix and Samsung; Seagate one of three hard drive makers, with Western Digital and Toshiba. TSMC publishes no lead time for wafers or packaging.</figcaption>
</figure>

This is not the equipment queue for transformers, where several makers run full factories and the backlog measures the wait. At these steps a second maker cannot be bought at any price. There is one, or a few, and a new one must first pass the customer's qualification.

<a id="tsmc-says-it-is-the-bottleneck"></a>
## A slow step grows only as fast as a building

Each slow step adds supply on a construction clock, not an order clock. TSMC's chief, C.C. Wei, said on 15 January 2026 that a new fab takes two to three years to build, and on 16 April that it needs one to two more to ramp. So a fab begun today reaches full output in three to five years.

The scanner is bound by its optics. ASML's Form 20-F of 25 February 2026 says its output is "limited by the production capacity" of Carl Zeiss SMT, sole supplier of the critical optics, and ASML owns 24.9% of the ZEISS SMT holding company. Its planned step of about 30% for 2027 fits its "existing footprint", in a third-party transcript of its July call; a larger step may need new cleanroom space.

<figure class="chart">
<p class="chart-title">New supply for the slow steps arrives from 2027 into the 2030s</p>
<p class="chart-sub">When each maker's added capacity starts, by its own dates</p>
<svg viewBox="0 0 560 286" role="img" aria-label="Timeline of new supply. ASML plans about 30 per cent more low NA EUV capacity for 2027 within its existing buildings. Micron's Idaho fab ID1 starts output in mid 2027, ID2 in late 2028, and its New York fab in 2030. A new TSMC fab begun today would take two to three years to build and one to two more to ramp, three to five years in all. Ajinomoto bought land at Kani City in May 2026 for a film plant operating in fiscal 2032, which runs from April 2032 to March 2033.">
<g class="c-grid"><line x1="200" y1="20" x2="200" y2="246"/><line x1="248.6" y1="20" x2="248.6" y2="246"/><line x1="297.1" y1="20" x2="297.1" y2="246"/><line x1="345.7" y1="20" x2="345.7" y2="246"/><line x1="394.3" y1="20" x2="394.3" y2="246"/><line x1="442.9" y1="20" x2="442.9" y2="246"/><line x1="491.4" y1="20" x2="491.4" y2="246"/><line x1="540" y1="20" x2="540" y2="246"/></g>
<g class="c-axis"><text x="200" y="266" text-anchor="middle">2026</text><text x="297.1" y="266" text-anchor="middle">2028</text><text x="394.3" y="266" text-anchor="middle">2030</text><text x="491.4" y="266" text-anchor="middle">2032</text><text x="190" y="44" text-anchor="end">ASML, about 30% more</text><text x="190" y="80" text-anchor="end">Micron Idaho ID1</text><text x="190" y="116" text-anchor="end">Micron Idaho ID2</text><text x="190" y="152" text-anchor="end">Micron New York</text><text x="190" y="188" text-anchor="end">A TSMC fab begun now</text><text x="190" y="224" text-anchor="end">Ajinomoto, Kani City</text></g>
<line class="c-today" x1="240.2" y1="14" x2="240.2" y2="246"/><text class="c-today-t" x="240.2" y="12" text-anchor="middle">today</text>
<g class="c-span"><line x1="240.2" y1="184" x2="483" y2="184"/><line x1="216.8" y1="220" x2="503.6" y2="220"/></g><g class="c-start"><circle cx="240.2" cy="184" r="4"/><circle cx="216.8" cy="220" r="4"/></g><g class="c-end"><circle cx="248.6" cy="40" r="4.5"/><circle cx="272.9" cy="76" r="4.5"/><circle cx="338.4" cy="112" r="4.5"/><circle cx="418.6" cy="148" r="4.5"/><circle cx="385.9" cy="184" r="4.5"/><circle cx="483" cy="184" r="4.5"/><circle cx="503.6" cy="220" r="4.5"/></g><g class="c-endt"><text x="257.6" y="44">2027, same buildings</text><text x="281.9" y="80">mid 2027</text><text x="347.4" y="116">late 2028</text><text x="427.6" y="152">2030</text><text x="483" y="175" text-anchor="end">3 to 5 years</text><text x="503.6" y="211" text-anchor="end">fiscal 2032</text></g>
</svg>
<figcaption>ASML results, 15 July 2026; Micron prepared remarks of 30 September 2026 and Form 10-K (9 October 2026); TSMC calls of 15 January and 16 April 2026; Ajinomoto Kani City release, 7 May 2026. Hollow dot: land bought, or today. The TSMC row is my arithmetic from its stated ranges, not a named plant. Ajinomoto's fiscal 2032 runs from April 2032 to March 2033.</figcaption>
</figure>

Until those buildings open, more orders can only push the horizon further out. On 24 June 2026 Micron even named "the need for enhanced energy infrastructure" among the limits on new fabs, so the chip's clock leans on the grid's.

## Each AI chip takes more of every slow step

The squeeze is worse than chip counts suggest, because an AI chip uses more of each slow part than an ordinary one.

<a id="the-countertop-is-the-bottleneck"></a>
<a id="micron-three-times-the-wafer"></a>

Memory is the plainest case. Micron's prepared remarks of 20 March 2024 said HBM3E, its stacked high-bandwidth memory, "consumes approximately three times the wafer supply" of DDR5, standard server memory, per bit. Its Form 10-K of 9 October 2026 says HBM needs "a higher number of wafers and more cleanroom space" per bit, so every shift towards HBM takes cleanroom from ordinary memory too.

<a id="ajinomoto-grows-with-the-package"></a>

The film is sold by area, not by chip. Ajinomoto makes ABF, the insulating sheet laid across each copper wiring layer of the board under the processor, and its presentation of 7 May 2026 puts that board at about 70 millimetres square with nine layers up to 2023, and about 100 with eleven in 2026. By my arithmetic, area times layers, today's board takes about two and a half times the film; servers and networks were 70% of its film volume in fiscal 2025, against 40% in fiscal 2017.

TSMC's factories are turning towards AI too. In TSMC's management report of 15 October 2026, high performance computing, which includes AI processors, was 68% of third quarter revenue, against 57% a year before. On 16 July Wei had said packaging capacity was limiting customers' growth.

<a id="asml-booked-ahead"></a>
## The only maker of the scanner says it cannot meet two years of demand

The strongest evidence that the slow parts are sold ahead comes from the one company that cannot be replaced at all. ASML is, in its own words, "the world's only manufacturer of EUV lithography systems".

On 15 July 2026 it expected to ship around 65 low NA EUV systems, its 2026 capacity, and its chief executive said ASML was "close to being fully covered with orders" for 2027. Three months later the wording hardened: "we now expect that our supply as currently planned for both 2027 and 2028 will not fully meet the demand of our customers". It added that "some customers are expressing an interest in placing orders with us for 2029 and even 2030".

The other slow steps moved the same way through 2026. Each was sold further ahead each time it spoke.

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
<figcaption>ASML results and transcript, 15 July and 14 October 2026; Seagate supplementals, 27 January, 28 April and 27 October 2026; Micron remarks, 17 December 2025 and 30 September 2026. Wording differs by maker, from "close to being fully covered" to "will not fully meet the demand"; each is quoted in the figures below.</figcaption>
</figure>

Seagate went from allocated through 2026 in January to the vast majority through 2028 in October, about a year added every six months. Micron had agreed all its 2026 HBM by December 2025, and "the vast majority of our calendar 2027 HBM bit supply" by 30 September 2026. Buyers commit this early because they know the clock: Nvidia's 10-K describes "extended lead times" of more than 12 months, and it secures supply with deposits and long-term capacity commitments.

## What could shorten the horizons

The case against is strong, and I take it at full strength. Buyers in a boom order early and sometimes twice, so a lengthening horizon fits hoarding as well as scarcity, and the filings cannot separate the two. Memory has a long record of gluts, and ASML is already studying a 2028 step beyond its 30%.

<a id="seagate-sells-the-terabyte"></a>

Some slow steps can also stretch without a building. Seagate's nearline shipments rose to 695 exabytes in its year to 3 July 2026, from 497, and on 27 October it said it meets that growth "by increasing capacity per drive rather than increasing drive unit production". Elsewhere the evidence is thin: Ajinomoto aims its current expansion at demand to 2030, so its film is not shown to bind before the Gifu plant opens, and TSMC publishes no packaging capacity or lead time.

These limits are real, and they shape the test. A double order does not create a second ASML, and a hoarded scanner still had to be built in the same cleanroom. Seagate's horizon lengthened even without new plant, which shows few makers and qualification at work, but it cannot test the building clock, so it stays on watch. My claim rests on the two steps that state a horizon and grow only by cleanroom: ASML and Micron.

## The chip waits for its worktops

A supplier in a boom says it cannot meet demand when its supply is a building, not an order. That is the whole chip side of AI: most parts can be bought this year, and the few that cannot are booked a year or more ahead, then further ahead each time their makers speak. I once wrote that the bottlenecks near the chip clear in quarters; the makers' own dates say years. The kitchen is finished when the last worktop arrives, and the worktops are cut in buildings that take years to raise.

## Claims on record

The test this piece stands behind, quoted word for word from the claims page:

<a id="the-chip-supply-chain"></a>

**The chip supply chain's slow parts stay sold more than a year ahead** (30 October 2026)

Claim: "In the AI chip supply chain, the parts that only one or a few qualified makers can supply, and that grow only through new cleanrooms, stay sold more than a year ahead. In its results published between 1 December 2027 and 31 March 2028, ASML will describe its 2029 low NA EUV supply as close to fully covered by orders or short of demand, and by its fiscal first quarter 2029 results, around December 2028, Micron will have said most of its calendar 2029 HBM supply is agreed."

Breaks if: "ASML, in its results published between 1 December 2027 and 31 March 2028, says its 2029 low NA EUV capacity exceeds customer orders, or does not describe 2029 as close to fully covered or short of demand; or Micron, by its fiscal first quarter 2029 results (around December 2028), has not said most of its calendar 2029 HBM supply is agreed, or reports unsold HBM and attributes it to customer demand. A shortfall caused by late cleanrooms or suppliers supports the claim rather than breaking it."

<details class="claims-earlier">
<summary>Four earlier claims on the chip's slow parts, and one proposed, quoted word for word</summary>

**TSMC's chief says the AI bottleneck is its factories, not the power grid** (2 October 2026)

Claim: "On today's horizon, TSMC's factories bind before the grid does. Over the longer run, I still expect the grid to be the slower clock."

Breaks if: "For today: TSMC's tightness eases while data centres with chips on order still wait for power. For the longer run: TSMC still calls capacity tight in 2028 while grid connection waits shorten."

Where later evidence bears on it: the near half holds. On TSMC's 15 October 2026 call Wei said the gap between demand and supply is "still quite big", the finance chief called tool supply tight, and Wei said TSMC's own checks on US data centre power were "so far so good". ASML's warning is a forecast of tool supply and does not test the 2028 half, which is still open.

**ASML's EUV machines are booked a year or two ahead, like a grid connection** (7 October 2026)

Claim: "ASML's EUV machines are sold out and committed a year or two ahead, and their number grows only as fast as ZEISS optics and ASML's cleanrooms allow, about 30 per cent a year, so a chipmaker adding leading-edge AI capacity must commit to scanners a year or two ahead, much as a data centre books a grid connection."

Breaks if: "The booking half fails if ASML says it has EUV capacity beyond what customers have ordered; or ships more than 10 per cent fewer low NA EUV systems than its stated capacity (around 65 for 2026, around 85 for 2027) and itself attributes the shortfall to customer demand or pushed-out orders; or by its fourth quarter 2026 results (January 2027) no longer describes 2027 as close to fully covered with orders; or says its EUV order lead times are shortening. The growth half fails if ASML raises its stated low NA EUV capacity by more than 40 per cent in a single year, or announces new EUV cleanroom space or a second source for its optics. A shortfall caused by ZEISS or other suppliers supports the claim rather than breaking it."

Where later evidence bears on it: the booking half is stronger than I wrote. The growth half is at risk: ASML is studying a 2028 step beyond 30%. It breaks above 40% in one year, or if ASML announces new EUV cleanroom space, which a step beyond two 30% steps may need.

**As AI chip packages grow, Ajinomoto's insulating film grows with them** (7 October 2026)

Claim: "Ajinomoto's build-up film is used by the area and layer count of each chip package, so as AI packages grow wider and taller its film volume shifts to AI servers faster than chip counts imply, and because a rival film takes a long time to qualify, Ajinomoto keeps that growth at high margins."

Breaks if: "In any of Ajinomoto's annual results presentations through fiscal 2029 (the year to March 2030), servers and networks fall below 70 per cent of its ABF volume by application, its fiscal 2025 level (the split is rounded to five points, so a flat 70 per cent passes); or the business profit margin of its Functional Materials business, part of the Healthcare and Others segment, falls below 50 per cent in a year when that business's sales still grow. Ajinomoto discloses the margin only as rounded wording ("over 50%"); if it stops doing so, the test rests on the volume split alone."

Where later evidence bears on it: I was wrong. Ajinomoto does not disclose the margin only as rounded wording. Its results data sheets print Functional Materials sales and business profit in yen, so the margin can be computed exactly. The test is sharper than I wrote, and both halves hold.

**Micron sells AI memory before the year starts, and each bit takes three times the wafer** (7 October 2026)

Claim: "Micron sells most of each year's HBM before that year starts, and because each HBM bit takes about three times the wafer of ordinary DRAM, every year HBM grows faster than conventional DRAM it takes wafers from ordinary memory and keeps that market short too, through calendar 2028."

Breaks if: "The first half fails if, by its fiscal first quarter 2028 results (around December 2027), Micron has not said most of its calendar 2028 HBM supply is agreed; or if Micron reports unsold HBM or cuts HBM output and itself attributes it to customer demand. The second half fails if, before the end of calendar 2028, Micron stops expecting the DRAM industry to be supply-constrained in 2027 or 2028 while still expecting industry HBM bits to grow faster than conventional DRAM; or if Micron states that any current HBM generation needs less than about three times the wafer of DDR5 per bit. A shortage prolonged by late cleanrooms supports the claim rather than breaking it."

Where later evidence bears on it: both halves hold, on Micron's September remarks.

**Proposed, never published: Seagate sells the terabyte**

Drafted in October 2026 and never published, so it is not on record. Seagate's 27 October results support it, and the drives stay on watch.

</details>

## What would prove me wrong

Both tests rest on the companies' own words, a year or more before the supply they describe. ASML has named 2029 only as a year some customers want to order for, and memory has a long record of gluts, so either could fail.

Seagate and TSMC stay on the watch list: one grows without new plant, the other publishes no number.

## Research notes

Four initiation notes rest on these claims, unchanged: [TSMC](/research/tsmc/), [ASML](/research/asml/), [Ajinomoto](/research/ajinomoto/) and [Micron](/research/micron/).

<details class="evidence">
<summary>The figures behind the charts</summary>

Each slow step, with what is committed ahead in the company's own words:

| Step | Who can make it | Committed ahead, in the company's words | What adds supply, and when | Source, dated |
|---|---|---|---|---|
| EUV scanner | ASML only; optics from ZEISS only | Expects to ship around 65 low NA machines, its 2026 capacity; supply planned for 2027 and 2028 "will not fully meet the demand" | About 30% more for 2027 in existing buildings; 2028 under study | ASML, 15 July and 14 October 2026 |
| Wafers and CoWoS packaging | TSMC, in practice the only source for the B200 | No lead time published; packaging tight enough to limit customers' growth | A new fab: two to three years to build, one to two to ramp | TSMC calls, 15 January, 16 April, 16 July 2026 |
| Substrate film | Ajinomoto, "product of choice for nearly all high-performance CPUs" | No order horizon published | Gunma line 2025; Kani City, Gifu, operating fiscal 2032 | Ajinomoto, 7 May and September 2026 |
| HBM wafers | Micron, SK Hynix, Samsung | All of 2026 agreed by December 2025; "the vast majority" of 2027 by September 2026 | Idaho ID1 mid 2027, ID2 late 2028, New York 2030 | Micron, 17 December 2025, 30 September 2026 |
| Nearline hard drives | Seagate, Western Digital, Toshiba | "Vast majority" of data centre nearline supply allocated through 2028 | More terabytes per drive, not more drives | Seagate, 27 October 2026 |
| The buyer | Nvidia | "Extended lead times" of more than 12 months; separately, deposits and long-term capacity commitments | Not Nvidia's to add | Nvidia 10-K, 25 February 2026 |

The horizon chart, point by point. Seagate: allocated through 2026 (supplemental, 27 January 2026), largely through 2027 (28 April), the vast majority of data centre nearline supply through 2028, with some cloud agreements through 2030 (27 October). ASML: "close to being fully covered with orders" for 2027 (chief executive, ASML's own transcript, 15 July 2026); 2027 and 2028 "will not fully meet the demand" (14 October). Micron: all 2026 HBM agreed (December 2025); "the vast majority of our calendar 2027 HBM bit supply" (30 September 2026).

Other figures. Ajinomoto expects the board to reach about 120 millimetres square with thirteen layers from 2031. Its Functional Materials business earned a business profit margin of 54.2% in fiscal 2025 and 57.7% in April to June 2026, on its results data sheets of 7 May and 6 August 2026; its ASV Report 2026 says customer trust "serves as a barrier for new entrants", and how long a rival takes to qualify is unpublished. Micron's 10-K says the base logic die under each HBM4 stack is "designed and manufactured in-house", so its stacks meet TSMC only at packaging. Micron expects DRAM to stay supply constrained in 2027 and 2028. Seagate shipped 26% more exabytes in the December quarter of 2025 "on similar number of units". On 15 October 2026 TSMC's finance chief said "the tool supply is tight".

Method. The horizons fit scarcity, but also buyers locking in supply in a boom, and the filings cannot separate the two. They do show supply: each maker grows only as fast as a building it has not finished. "Existing footprint" is from a third-party transcript of ASML's July call.

Corrections to earlier pieces. My July explainer said the slowest thing in the chain "is never the chip". Never was too strong; the dates above run as long as some grid queues. I still expect the grid to be the slower clock over the longer run, as my [27 July claim](/journal/the-queue-not-the-chip/#claims-on-record) says. My September explainer called memory and packaging "the kind of hard that money solves in quarters"; Micron's fab dates run to 2030. The live ASML piece attributed "close to being fully covered" to the finance chief; ASML's own transcript gives it to the chief executive.

</details>

<section class="exposure">
<h3>Who is exposed if the chip side's slow parts stay sold years ahead</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>The one-maker steps</dt>
<dd><span class="names">ASML</span> makes EUV scanners, <span class="names">ZEISS</span> their optics, <span class="names">Trumpf</span> their lasers. <span class="names">Ajinomoto</span> makes build-up film.</dd>
<dt>Factories and packaging</dt>
<dd><span class="names">TSMC</span> makes and packages AI chips. <span class="names">Ibiden</span> and <span class="names">Unimicron</span> make package substrates.</dd>
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

<p class="sources">Sources: ASML Annual Report 2025 on Form 20-F (25 February 2026) and its results of 15 July and 14 October 2026; TSMC earnings calls of 15 January, 16 April, 16 July and 15 October 2026 and its third quarter management report (15 October 2026); Ajinomoto's results presentation and Kani City release (7 May 2026), ASV Report 2026 (September 2026) and results data sheets; Micron's earnings calls and prepared remarks of 20 March 2024, 17 December 2025, 24 June and 30 September 2026, and its Form 10-K (9 October 2026); Seagate's supplemental information of 27 January, 28 April and 27 October 2026, its call of 28 July 2026 and Form 10-K (4 August 2026); Nvidia's Blackwell pages and Form 10-K (25 February 2026). Personal research, not investment advice.</p>
