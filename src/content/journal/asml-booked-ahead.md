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

In [the map of who makes Nvidia's flagship AI chip](/journal/nobody-makes-a-b200-alone/), I put them among the links with no second source. This piece asks how many ASML can make, and how far ahead they are spoken for.

The short answer is that ASML expects to ship every standard EUV machine it can build this year. It says next year is already close to fully ordered.

ASML's EUV machines are sold out and booked a year or two ahead, and their number grows only as fast as ZEISS and ASML's cleanrooms allow.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a new bakery. A builder can fit out the shop in months, and the owner can hire bakers. But the special oven comes from one workshop in the whole country.</p>
<p>That workshop makes a set number of ovens each year, and next year's are already promised. It can make a few more each year, but only as fast as its own glassmaker can make oven doors.</p>
<p>So a baker who wants to open in two years orders the oven today, before the walls go up. For leading-edge chips, ASML is that workshop.</p>
</details>

## Two words you need

**EUV scanner.** A lithography machine, which prints a chip's circuit pattern onto a silicon wafer using light. EUV means extreme ultraviolet, light of a very short wavelength that can draw the finest features.

**Low NA and High NA.** NA, numerical aperture, describes how wide a cone of light the machine's optics can gather. ASML's standard EUV machines are low NA, and its newer High NA machines print finer detail.

## Why only ASML builds them

ASML's annual report describes it as currently the only company in the world that makes EUV machines. The physics explains why nobody has followed.

EUV light is absorbed by almost everything, including air, so the whole light path sits in a high vacuum. Glass lenses would swallow the light too, so the machine steers it with mirrors instead.

Making the light is just as hard. A laser fires two pulses at a tiny, fast-moving drop of tin, up to 50,000 times a second. The pulses turn the tin into a glowing vapour, and that glow is the light.

The mirrors come from ZEISS, and the laser comes from Trumpf. Both are German.

## The supplier behind the supplier

Here is the physical limit that matters most. ASML's annual report says the number of machines it can produce "is limited by the production capacity" of Carl Zeiss SMT.

ZEISS is ASML's only supplier of the mirrors, lenses and other critical optics. ASML says they can be made only in limited numbers, and only at two ZEISS sites in Germany.

ASML owns about a quarter of the ZEISS business that holds this unit, and has agreed to lend it money for new investment. My reading is that a company pays for a supplier's factories only when that supplier sets its own limit.

## How far ahead the machines are booked

In July ASML put its capacity for standard EUV machines this year at around 65. It expects to ship all of them, so output and capacity are the same number.

Next year is nearly gone too. Roger Dassen, the chief financial officer, said ASML was "close to being fully covered with orders" for 2027. Orders for the year after are already arriving.

At the end of last year ASML held a backlog, signed orders not yet delivered, of €38.8 billion. By my arithmetic that is about nineteen months of its machine sales, which is what booking ahead looks like in money.

ASML plans to raise capacity by about 30 per cent next year, to around 85 machines, and is studying a similar step after that.

But it is bounded. Christophe Fouquet, the chief executive, said the increases come from ASML's existing buildings, without new cleanrooms, the dust-free halls where the machines are assembled. Behind that sits ZEISS, and each step is fixed a year or more before the machines ship.

## ASML says it is not short

Asked in July whether it was shipping too few machines, Fouquet answered that demand for the next two years had not settled, and that ASML's aim is to make its supply follow that demand. So ASML is not claiming a shortage. It sizes its output to the orders it holds.

That fits my claim, because those orders arrive a year or more before the machines do. A chipmaker that decides late joins the back of a queue that is already set.

My own judgement goes further, and it is a judgement, not the claim. If AI demand jumped suddenly, extra machines could not appear inside a year, so ASML's count would pace new leading-edge capacity. TSMC already says a new fab takes years, as I covered in [TSMC's own account of the bottleneck](/journal/tsmc-says-it-is-the-bottleneck/).

I read this as the same clock this site describes for power. What binds is rarely the chip design. It is the capacity that takes years to add, and an EUV machine is booked the way a grid connection is.

## What would prove me wrong

My claim has two halves. The machines are sold out and committed a year or two ahead, and their number grows only as fast as ZEISS and ASML's cleanrooms allow.

The first half fails if ASML says it has EUV capacity beyond what customers have ordered. It also fails if ASML ships more than 10 per cent fewer standard EUV machines than its stated capacity, around 65 for 2026 or around 85 for 2027, and itself blames customer demand or pushed-out orders.

It fails too if, by its fourth quarter results in January 2027, ASML no longer describes 2027 as close to fully covered with orders. The same goes if ASML says its EUV order lead times are shortening.

The second half fails if ASML raises its stated standard EUV capacity by more than 40 per cent in a single year. It also fails if ASML announces new EUV cleanroom space or a second source for its optics.

A shortfall caused by ZEISS or other suppliers would support the claim, not break it. Two things could blur the test: High NA machines may take over some layers, and export controls can change who ASML may ship to.

So I watch ASML's EUV count each quarter, and how it describes orders for the next two years.

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

<p class="sources">Sources: ASML Annual Report 2025 on Form 20-F, filed 25 February 2026, for sole supply from Carl Zeiss SMT and the ZEISS stake. ASML fourth quarter 2025 results, 28 January 2026, for backlog and system sales. ASML second quarter 2026 results and presentation, 15 July 2026, for capacity, and its investor call that day as transcribed. ASML EUV lithography systems page. ZEISS SMT EUV lithography page. The nineteen months is my own arithmetic. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
