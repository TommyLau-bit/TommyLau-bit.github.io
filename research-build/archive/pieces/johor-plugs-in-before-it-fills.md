---
title: "Johor's data centres are plugged in faster than they can be filled"
date: 2026-10-30T12:39:00+08:00
summary: "Johor is Malaysia's data centre hub, and the usual story is that its grid connections are the bottleneck. Tenaga's own figures now say otherwise for the campuses already connected: they draw less than a quarter of the power booked for them. What fills Johor's halls is the tenants' chips, and for its largest tenant those chips need an American licence."
category: "Analysis"
cover: "/covers/johor-plugs-in-before-it-fills.svg"
tags: ["johor", "grid", "data-centres"]
draft: true
---

SemiAnalysis sorts AI building into two kinds. America is power-gated: about a terawatt of requests wait on its utilities, and in its words "the grid is sold out". China is chip-gated, with plenty of power and too few chips.

Johor, the Malaysian state across the causeway from Singapore, fits neither box.

In July I argued that [a finished grid connection](/journal/the-queue-not-the-chip/) was Johor's scarce thing. For the campuses already connected, Tenaga Nasional's own figures now say it is not.

Johor's data centres are plugged in faster than they can be filled.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture a new block of flats where every flat has its electricity meter fitted and switched on before anyone moves in. Every flat is let, and the rent is being paid.</p>
<p>The lights still come on slowly, because tenants arrive when their furniture does. Counting meters tells you the block is ready. Counting lit windows tells you how full it is, and that depends on the removal vans.</p>
</details>

## How a Johor hall gets filled

An operator in Johor, such as DayOne, builds the shell, the cooling and the power. It then signs an energy supply agreement with Tenaga, Malaysia's grid utility, booking a maximum demand: the most power the site may ever draw at once.

DayOne's own filing says it supplies space, power and cooling, and its customers bring their own computers. Its long take-or-pay contracts pay for the capacity, not for the power the computers draw. So a Johor hall can be energised, let and billed while drawing little power.

Filling it is the tenant's job, and it has a queue of its own. Chips must be bought, shipped, racked and tested. For a company headquartered in China there is one more step. On 31 May 2026 the US Commerce Department confirmed that exporting advanced AI chips to such a company needs a licence, wherever its subsidiary sits. A Johor subsidiary is covered.

Malaysia's own permit, from July 2025, covers chips leaving the country, not chips installed in it.

Building more substations cannot speed this up. The pace is set by chip deliveries and, for Chinese tenants, by licence decisions that no Malaysian utility controls.

## What Tenaga and DayOne report

Across Malaysia in June, the data centres in Tenaga's system had booked 5.65 gigawatts of maximum demand. They drew about 1.26 gigawatts, less than a quarter. Johor holds two thirds of Malaysia's secured data centre capacity.

DayOne's largest customer, which it describes as a short-form video company, provided 69% of its revenue in the first half of 2026. SemiAnalysis names that customer as ByteDance. DayOne warns that export controls on it could cut future demand for its halls.

So my July claim needs a narrower reading. The wire is still scarce for a Johor campus waiting to connect, which is why Tenaga built its Green Lane. For one already plugged in, the pace is set by how fast tenants bring chips, and partly in Washington.

## What would prove me wrong

I am wrong if Tenaga's figures for June 2027 show data centres drawing 40% or more of the maximum demand in its system. That would mean tenants fill halls about as fast as they are connected.

I am also wrong if Johor operators start reporting finished halls left waiting for their grid connection. Then the wire would be the gate again.

<section class="exposure">
<h3>Who is exposed if Johor's halls fill slower than they connect</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The figures are the companies' own disclosures, used as evidence for the mechanism.</p>
<dl>
<dt>The subject's builders</dt>
<dd><span class="names">DayOne</span> and <span class="names">YTL Power</span> build and run data centre campuses in Johor.</dd>
<dt>The utility</dt>
<dd><span class="names">Tenaga Nasional</span> owns Malaysia's grid and signs each campus's supply agreement.</dd>
<dt>What fills the halls</dt>
<dd><span class="names">Nvidia</span> makes the AI chips. <span class="names">Oracle</span> runs cloud computing in the region.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone reading booked or energised megawatts in Johor as computing at work, and campuses that rest on one tenant's licence.</dd>
</dl>
</section>

---

<p class="sources">Sources: Tenaga Nasional analyst briefing, 28 August 2026, DayOne's share listing filing, 5 October 2026, US Commerce Department guidance, 31 May 2026, and Malaysia's trade ministry, 14 July 2025, with the framing from SemiAnalysis, "How AI Labs Are Solving the Power Crisis" (30 December 2025) and "The Chinese AI Infrastructure Boom" (25 September 2026). Personal research, not investment advice.</p>
