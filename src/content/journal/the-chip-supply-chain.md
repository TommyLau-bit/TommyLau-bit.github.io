---
title: "The chip supply chain's slow parts are sold years before they are made"
date: 2026-10-30T14:20:52+08:00
summary: "An Nvidia AI chip is built by dozens of companies, and most of them could be replaced within months. A few could not: ASML's lithography machines, TSMC's factories and packaging lines, Ajinomoto's insulating film, Micron's stacked memory and Seagate's hard drives each come from one or a handful of makers that grow only by building new plant. Those parts are sold a year or more before they are made, and they set how fast the chip side of AI can grow."
category: "Analysis"
cover: "/covers/the-chip-supply-chain.svg"
tags: ["the-stack", "supply-chain", "memory"]
draft: false
---

Nvidia designs the B200, one of the chips behind today's AI boom, but it makes none of it. Dozens of companies in at least five countries do.

Most of them could be replaced within months. A handful could not, because a second source would need a new factory, years of testing, or both.

Those few sell their output a year or more before they make it. In October, ASML, the only maker of the machines that print the finest chips, said its planned supply for 2027 and 2028 "will not fully meet the demand" of its customers.

The chip moves at the pace of its few irreplaceable suppliers, and they are sold years ahead.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a kitchen refit. Cupboards, taps and paint come from any shop this week. The stone worktop comes from one cutter with one saw, booked a year ahead, and a second saw means building a new workshop.</p>
<p>Hiring more fitters does not help. The kitchen is finished when the worktop arrives. An AI chip has five or six worktops, each from a different cutter.</p>
</details>

## How it works

A chip passes through many hands. Nvidia draws the design. TSMC, a Taiwanese company that makes chips for others, prints it onto silicon discs called wafers, using machines only ASML builds. TSMC then joins the processor to its memory in a step called packaging, on a base made with Ajinomoto's insulating film. The memory comes from three makers, Micron among them. Behind the chips, hard drives from makers like Seagate keep the data AI produces.

Most suppliers in that chain are easy to swap. Several firms can assemble a rack or make a connector.

The slow ones share three traits. There is one maker, or very few. A rival's part must pass qualification, the months or years of testing a customer runs before trusting it. And the only way to make more is new plant: a cleanroom, the dust-free hall where chips are made, or a whole factory.

So supply cannot simply catch up. Money buys the building, but not the time to build it. TSMC's chief says a new chip factory takes two to three years just to build. Ajinomoto's next film plant opens six to nearly seven years after it bought the land.

Buyers know this, so they commit early. Nvidia's annual report describes lead times of more than a year, and it secures supply with deposits and capacity commitments.

## The number that matters

In October ASML said some customers are interested in ordering machines for 2029 and even 2030.

The other slow parts tell the same story. Micron has already agreed most of next year's stacked memory supply, and Seagate has allocated most of its data centre drive supply through 2028.

Those are horizons this journal usually finds in [grid connections and transformers](/journal/the-queue-not-the-chip/), not in chips. I once wrote that the bottlenecks near the chip clear in quarters. The makers' own dates say years.

A booked machine is not proof of scarcity on its own, because buyers in a boom order early and sometimes twice. But a part that only one maker can build, and only in a new building, is booked early for a reason.

<hr class="layer">
<p class="layer-label">For investors</p>

## The mechanism in depth

Each slow step has few makers, a qualification wall and a plant clock.

| Step | Who can make it | Committed ahead, in the company's words | What adds supply, and when | Source, dated |
|---|---|---|---|---|
| EUV scanner | ASML only; optics from ZEISS only | Expects to ship around 65 low NA machines, its 2026 capacity; supply planned for 2027 and 2028 "will not fully meet the demand" | About 30% more for 2027 in existing buildings; 2028 under study | ASML, 15 July and 14 October 2026 |
| Wafers and CoWoS packaging | TSMC, in practice the only source for the B200 | No lead time published; packaging tight enough to limit customers' growth | A new fab: two to three years to build, one to two to ramp | TSMC calls, 15 January, 16 April, 16 July 2026 |
| Substrate film | Ajinomoto, "product of choice for nearly all high-performance CPUs" | No order horizon published | Gunma line 2025; Kani City, Gifu, operating fiscal 2032 | Ajinomoto, 7 May and September 2026 |
| HBM wafers | Micron, SK Hynix, Samsung | All of 2026 agreed by December 2025; "the vast majority" of 2027 by September 2026 | Idaho ID1 mid 2027, ID2 late 2028, New York 2030 | Micron, 17 December 2025, 30 September 2026 |
| Nearline hard drives | Seagate, Western Digital, Toshiba | "Vast majority" of data centre nearline supply allocated through 2028 | More terabytes per drive, not more drives | Seagate, 27 October 2026 |
| The buyer | Nvidia | "Extended lead times" of more than 12 months; separately, deposits and long-term capacity commitments | Not Nvidia's to add | Nvidia 10-K, 25 February 2026 |

Horizons lengthened in 2026. Seagate's supplementals moved from allocated through 2026 (27 January) to largely through 2027 (28 April) to the vast majority through 2028 (27 October), about a year added every six months. ASML's moved from 2027 nearly covered in July to 2027 and 2028 short in October. That fits scarcity, but also buyers locking in supply in a boom, and the filings cannot separate the two. They do show supply: each maker grows only as fast as a building it has not finished.

This is not the equipment queue of transformers and switchgear, where several makers have full factories and backlog measures the wait. Here a second maker cannot be bought at any price: there is one, or a few, and a new one must first pass the customer's qualification.

<a id="nobody-makes-a-b200-alone"></a>
<a id="the-two-seconds-after-you-hit-send"></a>
## One B200, sorted by how long each part takes to replace

Nvidia's B200 holds 208 billion transistors on two dies, the chips cut from a wafer, made by TSMC; its 10-K names SK Hynix, Micron and Samsung for memory.

My own rough sort runs from parts swapped in months, such as rack assembly and connectors, to those with no second source, EUV machines first and Ajinomoto's film close by.

Where I was wrong: my July explainer said the slowest thing in the chain "is never the chip". Never was too strong; the dates above run as long as some grid queues. I still expect the grid to be the slower clock over the longer run, as my [27 July claim](/journal/the-queue-not-the-chip/#claims-on-record) says.

<a id="asml-booked-ahead"></a>
## ASML: the scanner sold into 2028

An EUV scanner prints a chip's finest layers with extreme ultraviolet light. ASML's Form 20-F of 25 February 2026 calls it "the world's only manufacturer of EUV lithography systems", its output "limited by the production capacity" of Carl Zeiss SMT, sole supplier of the critical optics. ASML owns 24.9% of the ZEISS SMT holding company.

On 15 July 2026 it expected to ship around 65 low NA systems, its 2026 capacity, and planned about 30% more for 2027. Its chief executive said ASML was "close to being fully covered with orders" for 2027 (ASML's own transcript); both 30% steps fit the "existing footprint", as transcribed.

On 14 October the wording hardened: "we now expect that our supply as currently planned for both 2027 and 2028 will not fully meet the demand of our customers". It is studying a larger 2028 step, and "some customers are expressing an interest in placing orders with us for 2029 and even 2030".

**The only maker of the machine says it cannot meet two years of demand.**

<a id="tsmc-says-it-is-the-bottleneck"></a>
## TSMC: the factory and the package

TSMC makes chips others design. Its chief, C.C. Wei, said on 15 January 2026 that a new fab takes two to three years to build, and on 16 April one to two more to ramp. On 16 July he said packaging capacity was limiting customers' growth. CoWoS, its packaging step, joins each AI processor to its stacked memory.

In TSMC's management report of 15 October 2026, high performance computing, which includes AI processors, was 68% of third quarter revenue, against 57% a year before.

On its 15 October 2026 call Wei said "the gap between demand and supply are still quite big", and the finance chief said "the tool supply is tight". TSMC publishes no CoWoS lead time or capacity figure, so the step everyone calls tight has no dated number.

<a id="ajinomoto-grows-with-the-package"></a>
## Ajinomoto: film sold by area, not by chip

Ajinomoto, the seasoning maker, makes ABF, Ajinomoto Build-up Film, the insulating sheet laid across each copper wiring layer of a package substrate, the board under the processor. Ajinomoto's presentation of 7 May 2026 estimates the board at about 70 millimetres square with nine layers up to 2023, about 100 with eleven in 2026, and about 120 with thirteen from 2031. By my arithmetic, area times layers, today's board takes about two and a half times the film.

Servers and networks were 70% of its film volume in fiscal 2025, up from 40% in fiscal 2017. The Functional Materials business around the film earned a business profit margin of 54.2% in fiscal 2025 and 57.7% in April to June 2026, on Ajinomoto's results data sheets of 7 May and 6 August 2026.

Its ASV Report 2026 says customer trust "serves as a barrier for new entrants"; how long a rival takes to qualify is unpublished. Ajinomoto aims its current expansion at demand to 2030, so the film is not shown to bind before the Gifu site opens.

<a id="the-countertop-is-the-bottleneck"></a>
<a id="micron-three-times-the-wafer"></a>
## Micron: memory that eats wafers

Inference is bound by memory bandwidth, so DRAM, working memory, is stacked into towers of HBM, high-bandwidth memory, beside the processor. Micron's prepared remarks of 20 March 2024 said HBM3E "consumes approximately three times the wafer supply" of DDR5, standard server memory, per bit. Its Form 10-K of 9 October 2026 says HBM needs "a higher number of wafers and more cleanroom space" per bit.

Micron had agreed all its 2026 HBM by December 2025, and "the vast majority of our calendar 2027 HBM bit supply" by 30 September 2026. It expects DRAM to stay supply constrained in 2027 and 2028. Its Idaho fab ID1 starts output in mid 2027, ID2 in late 2028, New York in 2030. On 24 June 2026 it named "the need for enhanced energy infrastructure" among the limits on new fabs.

Micron's 10-K says the base logic die under each HBM4 stack is "designed and manufactured in-house", so its stacks meet TSMC only at packaging.

Where I was wrong: my September explainer called memory and packaging "the kind of hard that money solves in quarters". Micron's fab dates run to 2030; the near-chip clocks are years.

<a id="seagate-sells-the-terabyte"></a>
## Seagate: storage grown by the terabyte

For data AI keeps, the hard drive is still the cheapest home per terabyte. Seagate's Form 10-K for the year to 3 July 2026 shows nearline exabytes up to 695 from 497. In the December quarter of 2025 Seagate shipped 26% more exabytes "on similar number of units". On 27 October 2026 it said it meets exabyte growth "by increasing capacity per drive rather than increasing drive unit production". Some cloud agreements run through 2030. Seagate grows without new drive plant by choice, so its horizon tests qualification and few makers, not the plant clock.

## Claims on record

Each live claim is quoted word for word from the claims page, dated when its piece went live.

**TSMC's chief says the AI bottleneck is its factories, not the power grid** (2 October 2026)

Claim: "On today's horizon, TSMC's factories bind before the grid does. Over the longer run, I still expect the grid to be the slower clock."

Breaks if: "For today: TSMC's tightness eases while data centres with chips on order still wait for power. For the longer run: TSMC still calls capacity tight in 2028 while grid connection waits shorten."

Where later evidence points: the near half holds. On TSMC's 15 October 2026 call Wei said the gap between demand and supply is "still quite big", the finance chief called tool supply tight, and Wei said TSMC's own checks on US data centre power were "so far so good". ASML's warning is a forecast of tool supply and does not test the 2028 half, which is still open.

**ASML's EUV machines are booked a year or two ahead, like a grid connection** (7 October 2026)

Claim: "ASML's EUV machines are sold out and committed a year or two ahead, and their number grows only as fast as ZEISS optics and ASML's cleanrooms allow, about 30 per cent a year, so a chipmaker adding leading-edge AI capacity must commit to scanners a year or two ahead, much as a data centre books a grid connection."

Breaks if: "The booking half fails if ASML says it has EUV capacity beyond what customers have ordered; or ships more than 10 per cent fewer low NA EUV systems than its stated capacity (around 65 for 2026, around 85 for 2027) and itself attributes the shortfall to customer demand or pushed-out orders; or by its fourth quarter 2026 results (January 2027) no longer describes 2027 as close to fully covered with orders; or says its EUV order lead times are shortening. The growth half fails if ASML raises its stated low NA EUV capacity by more than 40 per cent in a single year, or announces new EUV cleanroom space or a second source for its optics. A shortfall caused by ZEISS or other suppliers supports the claim rather than breaking it."

Where later evidence points: the booking half is stronger than I wrote. The growth half is at risk: ASML is studying a 2028 step beyond 30%. It breaks above 40% in one year, or if ASML announces new EUV cleanroom space, which a step beyond two 30% steps may need.

**As AI chip packages grow, Ajinomoto's insulating film grows with them** (7 October 2026)

Claim: "Ajinomoto's build-up film is used by the area and layer count of each chip package, so as AI packages grow wider and taller its film volume shifts to AI servers faster than chip counts imply, and because a rival film takes a long time to qualify, Ajinomoto keeps that growth at high margins."

Breaks if: "In any of Ajinomoto's annual results presentations through fiscal 2029 (the year to March 2030), servers and networks fall below 70 per cent of its ABF volume by application, its fiscal 2025 level (the split is rounded to five points, so a flat 70 per cent passes); or the business profit margin of its Functional Materials business, part of the Healthcare and Others segment, falls below 50 per cent in a year when that business's sales still grow. Ajinomoto discloses the margin only as rounded wording ("over 50%"); if it stops doing so, the test rests on the volume split alone."

Where I was wrong: Ajinomoto does not disclose the margin only as rounded wording. Its results data sheets print Functional Materials sales and business profit in yen, so the margin can be computed exactly. The test is sharper than I wrote, and both halves hold.

**Micron sells AI memory before the year starts, and each bit takes three times the wafer** (7 October 2026)

Claim: "Micron sells most of each year's HBM before that year starts, and because each HBM bit takes about three times the wafer of ordinary DRAM, every year HBM grows faster than conventional DRAM it takes wafers from ordinary memory and keeps that market short too, through calendar 2028."

Breaks if: "The first half fails if, by its fiscal first quarter 2028 results (around December 2027), Micron has not said most of its calendar 2028 HBM supply is agreed; or if Micron reports unsold HBM or cuts HBM output and itself attributes it to customer demand. The second half fails if, before the end of calendar 2028, Micron stops expecting the DRAM industry to be supply-constrained in 2027 or 2028 while still expecting industry HBM bits to grow faster than conventional DRAM; or if Micron states that any current HBM generation needs less than about three times the wafer of DDR5 per bit. A shortage prolonged by late cleanrooms supports the claim rather than breaking it."

Where later evidence points: both halves hold, on Micron's September remarks.

**Proposed, never published: Seagate sells the terabyte**

Drafted in October 2026 and never published, so it is not on record. Seagate's 27 October results support it, and the drives stay on the watch list below.

<a id="the-chip-supply-chain"></a>

**New: the chip supply chain's slow parts** (30 October 2026)

Claim: "In the AI chip supply chain, the parts that only one or a few qualified makers can supply, and that grow only through new cleanrooms, stay sold more than a year ahead. In its results published between 1 December 2027 and 31 March 2028, ASML will describe its 2029 low NA EUV supply as close to fully covered by orders or short of demand, and by its fiscal first quarter 2029 results, around December 2028, Micron will have said most of its calendar 2029 HBM supply is agreed."

Breaks if: "ASML, in its results published between 1 December 2027 and 31 March 2028, says its 2029 low NA EUV capacity exceeds customer orders, or does not describe 2029 as close to fully covered or short of demand; or Micron, by its fiscal first quarter 2029 results (around December 2028), has not said most of its calendar 2029 HBM supply is agreed, or reports unsold HBM and attributes it to customer demand. A shortfall caused by late cleanrooms or suppliers supports the claim rather than breaking it."

## What would prove me wrong

Both tests rest on the companies' own words, a year or more before the supply they describe. ASML has named 2029 only as a year some customers want to order for, and memory has a long record of gluts, so either could fail.

Seagate and TSMC stay on the watch list: one grows without new plant, the other publishes no number.

## Research notes

Four initiation notes rest on these claims, unchanged: [TSMC](/research/tsmc/), [ASML](/research/asml/), [Ajinomoto](/research/ajinomoto/) and [Micron](/research/micron/).

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

<p class="sources">Sources: ASML Annual Report 2025 on Form 20-F (25 February 2026) and its results of 15 July and 14 October 2026; TSMC earnings calls of 15 January, 16 April and 16 July 2026 and its third quarter management report (15 October 2026); Ajinomoto's results presentation and Kani City release (7 May 2026), ASV Report 2026 (September 2026) and results data sheets; Micron's earnings calls and prepared remarks of 20 March 2024, 17 December 2025, 24 June and 30 September 2026, and its Form 10-K (9 October 2026); Seagate's supplemental information of 27 January, 28 April and 27 October 2026, its call of 28 July 2026 and Form 10-K (4 August 2026); Nvidia's Blackwell pages and Form 10-K (25 February 2026). Personal research, not investment advice.</p>
