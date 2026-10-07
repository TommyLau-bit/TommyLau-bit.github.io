---
title: "ASML's EUV machines are booked a year or two ahead, like a grid connection"
date: 2026-10-07T17:48:04+08:00
summary: "Every factory making the most advanced AI chips needs EUV machines, and ASML, a Dutch company, is the only maker. It expects to ship about 65 of its standard model this year, its full capacity, and says next year's machines are already close to fully ordered. Its output can grow only as fast as its German optics supplier allows, so a chipmaker that wants more must order a year or two ahead, much as a data centre books its grid connection."
category: "Analysis"
cover: "/covers/asml-booked-ahead.svg"
tags: ["the-stack", "supply-chain", "data-centres"]
draft: false
---

Here is a claim I am willing to be wrong about in public. A chipmaker planning new AI capacity has to book one machine a year or two ahead, the way a data centre books its grid connection.

That machine is ASML's EUV scanner. ASML, in Veldhoven in the Netherlands, builds the machines that print the finest layers of a leading-edge chip, and nobody else makes them.

In [the map of who makes an Nvidia B200](/journal/nobody-makes-a-b200-alone/), I put them among the links with no second source. This piece asks how many ASML can make, and how far ahead they are spoken for.

ASML expects to ship about 65 of its standard EUV machines in 2026, its full capacity. In July it said 2027 was already close to fully ordered.

ASML's EUV machines are sold out and booked a year or two ahead, and their number grows only as fast as ZEISS and ASML's cleanrooms allow.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a new bakery. A builder can fit out the shop in months, and the owner can hire bakers. But the special oven comes from one workshop in the whole country.</p>
<p>That workshop makes a set number of ovens each year, and next year's are already promised. It can make a few more each year, but only as fast as its own glassmaker can make oven doors.</p>
<p>So a baker who wants to open in two years orders the oven today, before the walls go up. For leading-edge chips, ASML is that workshop.</p>
</details>

## Three words you need

**EUV scanner.** A lithography machine, which prints a chip's circuit pattern onto a silicon wafer with light. EUV, extreme ultraviolet, uses light of 13.5 nanometres for the finest layers.

**Low NA and High NA.** NA, numerical aperture, describes how wide a cone of light the machine's optics gather. ASML's standard EUV machines are low NA, at 0.33. Its newer High NA machines, at 0.55, print finer detail.

**Installed base.** All the machines already working in customers' factories. ASML earns money servicing and upgrading them, and reports that business as Installed Base Management.

## Why only ASML builds them

In its 2025 annual report, ASML describes itself as "currently the world's only manufacturer of EUV lithography systems." The physics explains why nobody has followed.

EUV light is absorbed by almost everything, including air, so ASML keeps the whole light path in a high vacuum. Glass lenses would swallow it too, so the machine steers the light with mirrors instead.

Making the light is just as hard. ASML says a laser fires two pulses at a fast-moving drop of tin, up to 50,000 times a second. The pulses vaporise the tin, and that creates the light.

ZEISS, which makes the mirrors, says its projection optics alone hold about 20,000 parts. The laser that hits the tin comes from Trumpf, also German.

## The supplier behind the supplier

Here is the physical limit that matters most. ASML's annual report says the number of lithography systems it can produce "is limited by the production capacity" of Carl Zeiss SMT.

ZEISS is ASML's sole supplier of mirrors, lenses and other critical optics. ASML says ZEISS can make them "only in limited numbers" and only at its sites in Oberkochen and Wetzlar, Germany.

ASML owns 24.9 per cent of the ZEISS business that holds this unit, and has agreed to lend it money for capital spending above set thresholds. My reading is that a company finances a supplier's factories only when that supplier sets its own limit.

## The count, and how far ahead it is booked

ASML's annual reports give the number of EUV systems it recognised in sales each year. From 2020 to 2025 that was 31, 42, 40, 53, 44 and 48, including a few High NA machines.

That is 258 EUV systems recognised in sales from 2020 to 2025, by my sum. In the first half of 2026 ASML recognised 32 more, sixteen in each quarter.

On 15 July 2026, ASML put its 2026 capacity for low NA EUV at "around 65". Chief financial officer Roger Dassen said the same day: "we now expect to ship around 65 low NA EUV systems this year." Output and capacity are the same number.

Next year is nearly gone too. Dassen said ASML was "close to being fully covered with orders" for low NA EUV in 2027. For 2028, he said, ASML has "already received a significant number" of orders.

ASML ended 2025 with a backlog, signed orders not yet delivered, of €38.8 billion. By my arithmetic that is about nineteen months of 2025 system sales.

ASML plans to add 30 per cent to low NA capacity for 2027, about 85 machines, and is investigating another 30 per cent for 2028, about 110. For a machine this complex, that is fast.

But it is bounded. Chief executive Christophe Fouquet said, as transcribed, that the increases come from ASML's existing footprint, without new cleanrooms. Behind that sits ZEISS, and each number is fixed a year or more before the machines ship.

## ASML says it is not short

On the July call, an analyst from TD Cowen asked whether ASML was meeting demand rather than under-shipping.

Fouquet answered that demand for 2027 and 2028 had not settled, and that "the whole goal of our supply is to follow that demand." He added that "the capacity is there to meet the demand but the demand is still fluctuating."

Dassen called the 85 machines for 2027 "a nice representation of the balance" between what customers ask for and what ASML asks of its suppliers. So ASML is not claiming a shortage. It sizes its output to the orders it holds.

That is consistent with my claim, because those orders arrive a year or more before the machines. A chipmaker that decides late joins the back of a queue already set.

My own judgement goes further, and it is a judgement, not the claim. If AI demand jumped suddenly, the extra machines could not appear inside a year, so ASML's count would pace new leading-edge capacity. TSMC already says a new fab takes years, as I covered in [TSMC's own account of the bottleneck](/journal/tsmc-says-it-is-the-bottleneck/).

One way round the queue is upgrading machines already installed. ASML says its NXE:3800E prints 37 per cent more wafers an hour than the model before, and older machines can be upgraded to match.

Installed Base Management sales grew 26 per cent in 2025, to €8.2 billion. But ASML says those upgrades shifted "a substantial portion of EUV system revenue" into that line, so the growth is not purely a sign of shortage.

I read this as the same clock this site describes for power. What binds is rarely the chip design. It is the capacity that takes years to add, and an EUV machine is booked the way a grid connection is.

## What would prove me wrong

My claim has two halves. ASML's EUV machines are sold out and committed a year or two ahead, and their number grows only about 30 per cent a year.

The first half fails if machines start waiting for customers. That means ASML saying it has EUV capacity beyond what customers have ordered. Or shipping more than 10 per cent fewer low NA EUV machines than its stated capacity in 2026 or 2027, with ASML itself blaming customer demand or pushed-out orders.

It fails too if, by its fourth quarter results in January 2027, ASML no longer describes 2027 as close to fully covered. Or if ASML says its EUV order lead times are shortening.

The second half fails if ASML raises its stated low NA capacity by more than 40 per cent in a single year. It also fails if ASML announces new EUV cleanroom space or a second source for its optics.

A shortfall caused by ZEISS or other suppliers would support the claim, not break it. Two things could blur the test: High NA machines may take over some layers, needing "fewer systems overall", and export controls can change who ASML may ship to.

So I watch ASML's EUV count each quarter, with third quarter results due in mid October, and how it describes 2027 and 2028 orders. And High NA adoption, after Intel qualified it in July on some layers of 18A, its most advanced process.

<section class="exposure">
<h3>Who is exposed if ASML's machines stay booked a year or two ahead</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are ASML's own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">ASML</span> makes lithography systems, including every EUV machine, along with inspection tools and the service and upgrades for machines already installed.</dd>
<dt>The suppliers behind the machine</dt>
<dd><span class="names">ZEISS</span> makes the mirrors and optical systems inside ASML's machines. <span class="names">Trumpf</span> makes the high-power lasers that drive the EUV light source.</dd>
<dt>The chipmakers who need the machines</dt>
<dd><span class="names">TSMC</span>, <span class="names">Samsung</span> and <span class="names">Intel</span> make leading-edge logic chips. <span class="names">SK Hynix</span>, <span class="names">Samsung</span> and <span class="names">Micron</span> make DRAM memory.</dd>
<dt>The other lithography makers</dt>
<dd><span class="names">Nikon</span> and <span class="names">Canon</span> make lithography machines for layers that do not need EUV.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Chipmakers that decide late on new leading-edge capacity and find the machines already promised, and the AI chip designers waiting on them. And ASML's own case, if orders fall short of what it can build.</dd>
</dl>
</section>

---

<p class="sources">Sources: ASML Annual Report 2025 on Form 20-F, filed 25 February 2026, for EUV units, sole supply from Carl Zeiss SMT, single sourcing, Installed Base Management, field upgrades and the NXE:3800E. ASML annual reports for 2021 and 2023 for earlier EUV units. ASML fourth quarter 2025 results, 28 January 2026, for backlog and system sales. ASML second quarter 2026 results and presentation, 15 July 2026, for capacity, quarterly units and the Intel High NA milestone, and its investor call that day as transcribed. ASML EUV lithography systems page. ZEISS SMT EUV lithography page. The 258 systems and nineteen months are my own arithmetic. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
