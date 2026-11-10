---
title: "America rations the plug: who may be cut, who must hold on, who pays"
date: 2026-09-22T18:53:00+08:00
summary: "America cannot build grid wires as fast as data centres ask for them, so its grids are rationing the connection instead of speeding it up. Most of its grids are writing a cheaper plug the grid may cut first, though no data centre yet runs on one; sites must now hold on when the voltage dips, after 3,900 megawatts left Virginia's grid in one morning; and households still share the bill for the wait. Meanwhile signed gigawatts run far ahead of running ones: Dominion has about 54 gigawatts of data centres under contract and bills 4.8."
category: "Analysis"
format: "depth"
cover: "/covers/america-rations-the-plug.svg"
tags: ["grid", "power", "data-centres"]
draft: false
---

<a id="america-rations-the-plug"></a>
<a id="ercot-rations-the-plug"></a>

On 3 August 2026 the Governor of Texas said ERCOT, which runs most of the state's grid, was weighing over 474 gigawatts of requests to connect. That is more than five times the most power Texas has ever used at once, and about nine tenths of it is data centres.

Twelve days earlier, a fault on a power line in Dominion Energy's part of Virginia was cleared exactly as designed. Even so, about 3,900 megawatts of data centres switched themselves off the grid onto their own backup. And in September Dominion told PJM, the grid operator, that it had about 54 gigawatts of data centres under contract, against 4.8 gigawatts it actually bills.

That is the claim of this piece. America cannot build wires as fast as data centres ask for them, so it is rationing the connection rather than speeding it up: a firm plug for those who wait, a cheaper plug the grid may cut first for those who will not, and rules that make every site hold on when the grid wobbles. The gap between signed and running gigawatts is where the wait shows, and households still share the bill for it.

<details class="analogy">
<summary>The analogy</summary>
<p>Picture a restaurant whose gas main is full, with the bigger one booked for years. A table with full service waits for the new main: that is firm service. Diners seated now on the terrace get their burners turned down first when the kitchen is slammed, and must bring a camping stove: that is the cut-first tier and its backup.</p>
<p>When the lights flicker, nobody may run for the door at once, because a stampede tips the room over: that is holding on. Meanwhile someone pays for gas bottles rented until the main is dug: that is the bill for the wait. And the bookings book is fuller than the dining room ever will be: that is the gap between signed and running.</p>
</details>

## How does a data centre get connected to the grid?

It applies to its local utility, waits while the utility and the grid operator study what the wires can carry, waits again while the upgrades are built, and only then switches on.

A data centre is a **load**, a user of power, and loads join by a less formal path than power stations.

<figure class="illo">
<p class="illo-title">Four of the five steps are paperwork; the third is steel and copper</p>
<p class="illo-sub">From application to running, for a large data centre in an American grid, simplified</p>
<svg viewBox="0 0 940 282" role="img" aria-label="The five steps from application to running for a large data centre in America. One, apply: the developer files its site, megawatts and a deposit with the local utility, in weeks. Two, study: the utility and grid operator check what the wires can carry; FERC wants studies done in 60 to 90 days. Three, build the upgrades: new lines, substations and transformers, made by factories and built by the utility, which takes years and is the step no rule can hurry; it is shaded. Four, switch on: firm service waits for step three, or the site switches on now on a tier the grid may cut first. Five, run: the site must hold on through voltage dips, with its UPS batteries and generators, and pays its share of the bill every year."><line class="i-ground" x1="10" y1="190" x2="930" y2="190"/><path class="i-line" d="M154 130 H218"/><path class="i-line" d="M211 125 l7 5 l-7 5" style="fill:none"/><path class="i-line" d="M342 130 H408"/><path class="i-line" d="M401 125 l7 5 l-7 5" style="fill:none"/><path class="i-line" d="M532 130 H598"/><path class="i-line" d="M591 125 l7 5 l-7 5" style="fill:none"/><path class="i-line" d="M722 130 H788"/><path class="i-line" d="M781 125 l7 5 l-7 5" style="fill:none"/><rect class="i-fill" x="58" y="70" width="56" height="74" rx="3"/><line class="i-thin" x1="66" y1="86" x2="106" y2="86"/><line class="i-thin" x1="66" y1="98" x2="100" y2="98"/><line class="i-thin" x1="66" y1="110" x2="106" y2="110"/><line class="i-thin" x1="66" y1="122" x2="100" y2="122"/><text class="i-k" x="86" y="138" text-anchor="middle">300 MW</text><ellipse class="i-metal" cx="132" cy="182" rx="16" ry="5"/><ellipse class="i-metal" cx="132" cy="174" rx="16" ry="5"/><ellipse class="i-metal" cx="132" cy="166" rx="16" ry="5"/><ellipse class="i-metal" cx="132" cy="158" rx="16" ry="5"/><line class="i-thin" x1="236" y1="90" x2="270" y2="70"/><line class="i-thin" x1="270" y1="70" x2="310" y2="96"/><line class="i-thin" x1="236" y1="90" x2="250" y2="140"/><line class="i-thin" x1="250" y1="140" x2="296" y2="150"/><line class="i-thin" x1="296" y1="150" x2="326" y2="130"/><line class="i-thin" x1="310" y1="96" x2="326" y2="130"/><line class="i-thin" x1="270" y1="70" x2="296" y2="150"/><circle class="i-fill" cx="236" cy="90" r="5"/><circle class="i-fill" cx="270" cy="70" r="5"/><circle class="i-fill" cx="310" cy="96" r="5"/><circle class="i-fill" cx="250" cy="140" r="5"/><circle class="i-fill" cx="296" cy="150" r="5"/><circle class="i-fill" cx="326" cy="130" r="5"/><circle class="i-line" cx="298" cy="118" r="20" style="fill:none"/><line class="i-line" x1="312" y1="132" x2="330" y2="152"/><rect class="i-choke" x="396" y="40" width="148" height="150" rx="6"/><path class="i-line" d="M420 190 L436 58 L452 190 M426 150 H446 M430 110 H442 M412 76 H460" style="fill:none"/><rect class="i-fill" x="470" y="112" width="56" height="78" rx="4"/><rect class="i-fill" x="476" y="88" width="8" height="24" rx="3"/><rect class="i-fill" x="494" y="88" width="8" height="24" rx="3"/><rect class="i-fill" x="512" y="88" width="8" height="24" rx="3"/><line class="i-thin" x1="478" y1="130" x2="518" y2="130"/><line class="i-thin" x1="478" y1="146" x2="518" y2="146"/><path class="i-line" d="M610 130 H650 L680 92 H712 M650 130 L680 168 H712" style="fill:none"/><circle class="i-fill" cx="650" cy="130" r="5"/><text class="i-n" x="674" y="84">firm</text><text class="i-hot-t" x="674" y="160">cut first</text><rect class="i-fill" x="794" y="84" width="74" height="106" rx="3"/><rect class="i-metal" x="802" y="100" width="14" height="78" rx="1"/><rect class="i-metal" x="824" y="100" width="14" height="78" rx="1"/><rect class="i-metal" x="846" y="100" width="14" height="78" rx="1"/><rect class="i-cool-f" x="876" y="132" width="26" height="58" rx="2"/><text class="i-k" x="889" y="126" text-anchor="middle">UPS</text><rect class="i-metal" x="906" y="150" width="30" height="40" rx="2"/><line class="i-thin" x1="912" y1="150" x2="912" y2="140"/><text class="i-k" x="921" y="136" text-anchor="middle">gen</text><text class="i-t" x="92" y="214" text-anchor="middle">1. Apply</text><text class="i-n" x="92" y="231" text-anchor="middle">site, megawatts, deposit</text><text class="i-n" x="92" y="247" text-anchor="middle">to the local utility</text><text class="i-k" x="92" y="267" text-anchor="middle">weeks</text><text class="i-t" x="280" y="214" text-anchor="middle">2. Study</text><text class="i-n" x="280" y="231" text-anchor="middle">what the wires can carry</text><text class="i-n" x="280" y="247" text-anchor="middle">utility and grid operator</text><text class="i-k" x="280" y="267" text-anchor="middle">FERC wants 60 to 90 days</text><text class="i-t" x="470" y="214" text-anchor="middle">3. Build the upgrades</text><text class="i-n" x="470" y="231" text-anchor="middle">lines, substations, transformers</text><text class="i-n" x="470" y="247" text-anchor="middle">factories and the utility</text><text class="i-hot-t" x="470" y="267" text-anchor="middle">years: no rule hurries it</text><text class="i-t" x="660" y="214" text-anchor="middle">4. Switch on</text><text class="i-n" x="660" y="231" text-anchor="middle">firm, or on a tier cut first</text><text class="i-n" x="660" y="247" text-anchor="middle">utility and grid operator</text><text class="i-k" x="660" y="267" text-anchor="middle">firm waits for step 3</text><text class="i-t" x="850" y="214" text-anchor="middle">5. Run</text><text class="i-n" x="850" y="231" text-anchor="middle">hold on in a dip, pay the bill</text><text class="i-n" x="850" y="247" text-anchor="middle">the site</text><text class="i-k" x="850" y="267" text-anchor="middle">every year after</text><text class="i-head" x="10" y="22">Who decides each step, and how long it takes</text></svg>
<figcaption>FERC's PJM show cause order (18 June 2026) for the study target and who handles load requests; the equipment queue for the build. My drawing.</figcaption>
</figure>

Five steps follow. The developer applies with a site, a size in **megawatts (MW)**, a schedule for ramping up and a deposit. A megawatt is a million watts, the draw of about a thousand homes; a **gigawatt (GW)** is a thousand megawatts. The utility and the grid operator study whether the wires can carry it. The study lists the **upgrades** the site needs: new or bigger lines, substations, transformers and breakers. The upgrades are built. Then the utility gives "approval to energise", and the site switches on and ramps up.

What the site gets at the end is **firm service**, the grid's promise to carry it at all times short of an emergency. To promise that, the grid must have both the wires to reach the site and enough power stations standing ready for its peak. Both are now short.

## Which step takes longest, and why can no rule hurry it?

Building the upgrades. Every other step is paperwork that a regulator can redraw in months; the upgrades are steel, copper and factory slots.

On 18 June 2026 FERC, the federal power regulator, said a study listing the upgrades, a cost estimate and a build time "should take no more than 60-90 days". The build is the long part. FERC's own record notes that a data centre "may only take 1-2 years to construct", while the lines and substations to serve it take longer. PJM's answer, to be filed on 16 November, is one 12-month process a year for power stations and large loads alike.

Each large transformer is designed for the voltages of one substation, so none comes off a shelf. The grid businesses of Siemens Energy and Hitachi Energy hold about four and three years of signed work, as [the equipment queue](/journal/the-equipment-queue/) measures it.

So a rule can make the paperwork faster. It cannot make a transformer arrive sooner.

## How long is the line?

Far longer than anything that will be built: the requests are counted in hundreds of gigawatts, and what reaches the last gate in single figures.

<figure class="chart">
<p class="chart-title">Texas has been asked for 474 gigawatts, and has cleared 6.6</p>
<p class="chart-sub">Large loads asking to connect to ERCOT, at each gate, gigawatts</p>
<svg viewBox="0 0 560 314" role="img" aria-label="Bar chart in gigawatts. All of ERCOT in summer 2026: 474 of requests to connect large loads as of June; about 205 eligible for the first batch study, preliminary, 29 July; 17 loads totalling 6.6 that had cleared every step but approval to energise on 20 August, after which ERCOT paused that approval for data centres of 75 megawatts or more. Oncor alone, at 30 September 2026: 293 of data centre requests; about 45 classified on condition of ERCOT's audit, 24 as base load, including 10 already energised, and 21 as studied load."><g class="c-grid"><line x1="200.0" y1="28" x2="200.0" y2="294"/><line x1="252.0" y1="28" x2="252.0" y2="294"/><line x1="304.0" y1="28" x2="304.0" y2="294"/><line x1="356.0" y1="28" x2="356.0" y2="294"/><line x1="408.0" y1="28" x2="408.0" y2="294"/><line x1="460.0" y1="28" x2="460.0" y2="294"/></g><g class="c-axis"><text x="200.0" y="22" text-anchor="middle">0</text><text x="252.0" y="22" text-anchor="middle">100</text><text x="304.0" y="22" text-anchor="middle">200</text><text x="356.0" y="22" text-anchor="middle">300</text><text x="408.0" y="22" text-anchor="middle">400</text><text x="460.0" y="22" text-anchor="middle">500</text></g><text class="c-lab c-s2t" x="0" y="56">All of ERCOT, summer 2026</text><text class="c-box-t" x="0" y="79">Requests to connect</text><text class="c-note" x="0" y="94">large loads, June 2026</text><rect class="c-bar c-mute" x="200" y="70" width="246.5" height="22" rx="2"/><text class="c-lab c-s1t" x="452.5" y="86">474 GW</text><text class="c-box-t" x="0" y="121">Eligible for the first batch</text><text class="c-note" x="0" y="136">preliminary, 29 July</text><rect class="c-bar c-mute" x="200" y="112" width="106.6" height="22" rx="2"/><text class="c-lab c-s1t" x="312.6" y="128">205 GW</text><text class="c-box-t" x="0" y="163">Cleared all but the last gate</text><text class="c-note" x="0" y="178">17 loads, 20 August</text><rect class="c-bar" x="200" y="154" width="3.4" height="22" rx="2"/><text class="c-lab c-s1t" x="209.4" y="170">6.6 GW, then paused</text><text class="c-lab c-s2t" x="0" y="212">Oncor alone, the largest wires company</text><text class="c-box-t" x="0" y="235">Data centre requests</text><text class="c-note" x="0" y="250">30 September 2026</text><rect class="c-bar c-mute" x="200" y="226" width="152.4" height="22" rx="2"/><text class="c-lab c-s1t" x="358.4" y="242">293 GW</text><text class="c-box-t" x="0" y="277">Classified, on condition</text><text class="c-note" x="0" y="292">base and studied load</text><rect class="c-bar" x="200" y="268" width="23.4" height="22" rx="2"/><text class="c-lab c-s1t" x="229.4" y="284">45 GW, 10 already on</text><line class="c-base" x1="200" y1="28" x2="200" y2="294"/></svg>
<figcaption>Office of the Texas Governor (3 August 2026); ERCOT's Senate briefing (29 July 2026, preliminary) and its presentation to the Texas regulator (20 August 2026); Oncor Form 8-K exhibit (5 November 2026). ERCOT's figures are from different dates in the same summer.</figcaption>
</figure>

Texas shows the funnel most clearly. ERCOT's 474 GW, as of June 2026, counts requests, not demand. On 29 July ERCOT told the state Senate that about 205 GW was eligible for its first batch study, a preliminary figure. By 20 August, 17 loads totalling 6,608 MW had cleared every check except the approval to energise. Then ERCOT paused that approval for data centres of 75 MW or more, while it audits every request at the Governor's order.

Under a seventieth of the list reached the last gate, and the gate is shut until the audit reports, due by 10 December 2026. "Five times the record peak" divides requests by ERCOT's highest hour, 91.1 GW on 22 July 2026. It does not mean Texas needs five grids: a developer unsure which site will get power first files for several. Oncor, the largest wires company in Texas, alone held 795 requests at 30 September 2026, about 293 GW of them from data centres.

## If the wires cannot be hurried, what are the grids doing instead?

Selling the connection in two grades: a firm plug that waits for the upgrades, and a cheaper one that switches on now on whatever spare capacity exists, and is cut first when the grid is tight.

The second grade is **non-firm** or **interim service**. The site connects before its upgrades are built and runs as long as the wires have room. When they do not, the grid turns it down before anyone with firm service. When the upgrades arrive it converts to firm.

<a id="ferc-asks-for-a-softer-plug"></a>

The push came from Washington. On 18 June 2026 FERC ordered six regional grid operators to defend their large-load rules or change them, including a service for loads willing to be cut. It found that PJM's tariff, its rulebook, "appears to be unjust, unreasonable, or unduly discriminatory or preferential". PJM and its utilities file their answers by 16 November 2026.

The status of each grid's cheaper plug, at 7 November 2026:

| Grid | The cut-first or early tier | Status | Any data centre running on it? |
|---|---|---|---|
| ERCOT, Texas | Provisional Controllable Load Resource | Approved 18 June 2026; may not run before 2027 | None found |
| SPP, central states | CHILLS: power as available, for up to seven years | In force 1 July 2026 | None found; no signed agreement published |
| PJM, Chicago to Virginia | Interim NITS: "a temporary, non-firm transmission service" | Ordered by FERC for loads beside a power station; tariff text awaits FERC; for all large loads, to be filed 16 November 2026 | None found |
| CAISO, California | Flexible interim connection | Board approved 28 October 2026 | None |
| NYISO, New York | Bring new capacity or accept non-firm service | Filing in November or December | None |
| ISO New England | To be filed by 16 November | Not filed | None |
| MISO, the Midwest | No cut-first tier; a fast track for loads that bring new power stations | Awaiting FERC | None |

## Is any data centre actually running on a cut-first plug?

Not that any primary record shows. On 7 November 2026 I could find no data centre of 50 MW or more switched on under any of these tiers, in any of the seven grids.

The one tier in force for ordinary large loads is SPP's CHILLS, and no signed CHILLS agreement is public.

So the claim's test is still open. By 31 December 2027 at least two of the seven grids must have a real data centre running on such a tier, shown in a filed agreement. Rules written do not count.

The strongest counter-evidence is PJM's own plan for a fourth service, Fractional NITS, "a firm service, based on available system capacity": firm power for part of a site now, the rest when the upgrades arrive. If developers take part of a site firm rather than all of it cut first, the rationing happens by size, not grade, and my test breaks.

<a id="the-hours-a-cut-first-site-can-run"></a>
## How many hours a year would a cut-first site be cut?

Nobody publishes it, which is the gap an investor should notice. A cut-first megawatt is worth the hours it is allowed to run, and no tier states them.

The best estimate is academic. Duke University's Nicholas Institute calculated in February 2025 how much new load America's 22 largest grids could take without new power stations, if that load accepted cuts in the tightest hours. Its answer, as the institute and the trade press summarise it, runs from 76 GW to 126 GW.

<figure class="chart">
<p class="chart-title">If new load accepts a few cuts a year, existing grids can take far more of it</p>
<p class="chart-sub">New load America's 22 largest grids could add without new capacity, gigawatts, by the share of its yearly energy it gives up</p>
<svg viewBox="0 0 560 170" role="img" aria-label="Bar chart of new load the 22 largest US grids could add without new capacity if that load accepts cuts, from Duke University's Nicholas Institute, February 2025. 76 gigawatts if it gives up 0.25 per cent of its yearly energy, about 85 hours of cuts a year; 98 gigawatts at 0.5 per cent, about 177 hours; 126 gigawatts at 1 per cent, about 366 hours."><g class="c-grid"><line x1="200.0" y1="28" x2="200.0" y2="150"/><line x1="285.7" y1="28" x2="285.7" y2="150"/><line x1="371.4" y1="28" x2="371.4" y2="150"/><line x1="457.1" y1="28" x2="457.1" y2="150"/></g><g class="c-axis"><text x="200.0" y="22" text-anchor="middle">0</text><text x="285.7" y="22" text-anchor="middle">40</text><text x="371.4" y="22" text-anchor="middle">80</text><text x="457.1" y="22" text-anchor="middle">120</text></g><text class="c-box-t" x="0" y="49">Cut 0.25% of its energy</text><text class="c-note" x="0" y="64">about 85 hours a year</text><rect class="c-bar" x="200" y="40" width="162.9" height="22" rx="2"/><text class="c-lab c-s1t" x="368.9" y="56">76 GW</text><text class="c-box-t" x="0" y="91">Cut 0.5%</text><text class="c-note" x="0" y="106">about 177 hours a year</text><rect class="c-bar" x="200" y="82" width="210.0" height="22" rx="2"/><text class="c-lab c-s1t" x="416.0" y="98">98 GW</text><text class="c-box-t" x="0" y="133">Cut 1%</text><text class="c-note" x="0" y="148">about 366 hours a year</text><rect class="c-bar" x="200" y="124" width="270.0" height="22" rx="2"/><text class="c-lab c-s1t" x="476.0" y="140">126 GW</text><line class="c-base" x1="200" y1="28" x2="200" y2="150"/></svg>
<figcaption>Duke University Nicholas Institute, Rethinking Load Growth (11 February 2025), as summarised by the institute and the trade press; I could not open the report itself. Hours are the model's, not a contract's.</figcaption>
</figure>

The cuts in that model are small and partial. At 0.5% of a year's energy, the new load is cut for about 177 hours a year, and in 88% of those hours at least half of it keeps running. A typical cut lasts about two hours. The real contracts are confidential. Until a filed agreement states the hours, any model that values a cut-first megawatt like a firm one is guessing.

## What keeps a site running when the grid cuts it?

Three things: its own generators, batteries, or chips that slow down. Each has its own limit, and the generators' limit is set by an air permit, not by the grid.

**Generators.** Almost every data centre already has diesel generators for outages. But under the federal air rule for emergency engines, running outside an emergency is capped at 100 hours a year for maintenance and testing, of which only 50 may earn money. A cut beyond that, outside a declared emergency, needs engines permitted to run as power stations, which is why [building your own power](/journal/building-your-own-power/) matters to this piece.

<a id="google-lets-the-grid-slow-its-chips"></a>

**Chips that slow.** By 19 March 2026 Google had deals with five utilities, covering 1 GW, under which it can "limit or shift a portion" of its machine learning work at peak. No record yet shows a connection approved on a slowed chip.

<a id="what-the-battery-is-really-for"></a>
<a id="california-still-shifts-the-sun"></a>

**Batteries.** A large battery at a site could carry it through a cut. But the batteries America is building mostly move solar power into the evening: California's fleet earned about $35 per kilowatt a year from shifting energy, against $9 from steadying the grid. And in PJM's capacity market a megawatt of **demand response**, load that agrees to be cut on call, counts for more than a megawatt of four-hour battery.

<figure class="chart">
<p class="chart-title">PJM counts a megawatt that can be cut for more than a megawatt of battery</p>
<p class="chart-sub">Share of each megawatt PJM counts towards its capacity needs</p>
<svg viewBox="0 0 560 296" role="img" aria-label="Bar chart of how much of each megawatt PJM counts in its capacity market. Demand response: 91 per cent for 2028/29, 90 per cent for 2029/30 and 84 per cent for 2030/31, preliminary. A four-hour battery: 59, 57 and 42 per cent for the same years."><g class="c-grid"><line x1="160.0" y1="28" x2="160.0" y2="282"/><line x1="245.0" y1="28" x2="245.0" y2="282"/><line x1="330.0" y1="28" x2="330.0" y2="282"/><line x1="415.0" y1="28" x2="415.0" y2="282"/><line x1="500.0" y1="28" x2="500.0" y2="282"/></g><g class="c-axis"><text x="160.0" y="22" text-anchor="middle">0%</text><text x="245.0" y="22" text-anchor="middle">25%</text><text x="330.0" y="22" text-anchor="middle">50%</text><text x="415.0" y="22" text-anchor="middle">75%</text><text x="500.0" y="22" text-anchor="middle">100%</text></g><text class="c-lab c-s2t" x="0" y="56">Demand response</text><text class="c-box-t" x="0" y="79">2028/29</text><text class="c-note" x="0" y="94">binding</text><rect class="c-bar" x="160" y="70" width="309.4" height="18" rx="2"/><text class="c-lab c-s1t" x="475.4" y="86">91%</text><text class="c-box-t" x="0" y="111">2029/30</text><text class="c-note" x="0" y="126">binding</text><rect class="c-bar" x="160" y="102" width="306.0" height="18" rx="2"/><text class="c-lab c-s1t" x="472.0" y="118">90%</text><text class="c-box-t" x="0" y="143">2030/31</text><text class="c-note" x="0" y="158">preliminary</text><rect class="c-bar" x="160" y="134" width="285.6" height="18" rx="2"/><text class="c-lab c-s1t" x="451.6" y="150">84%</text><text class="c-lab c-s2t" x="0" y="182">Four-hour battery</text><text class="c-box-t" x="0" y="205">2028/29</text><text class="c-note" x="0" y="220">binding</text><rect class="c-bar c-alt" x="160" y="196" width="200.6" height="18" rx="2"/><text class="c-lab c-s1t" x="366.6" y="212">59%</text><text class="c-box-t" x="0" y="237">2029/30</text><text class="c-note" x="0" y="252">binding</text><rect class="c-bar c-alt" x="160" y="228" width="193.8" height="18" rx="2"/><text class="c-lab c-s1t" x="359.8" y="244">57%</text><text class="c-box-t" x="0" y="269">2030/31</text><text class="c-note" x="0" y="284">preliminary</text><rect class="c-bar c-alt" x="160" y="260" width="142.8" height="18" rx="2"/><text class="c-lab c-s1t" x="308.8" y="276">42%</text><line class="c-base" x1="160" y1="28" x2="160" y2="282"/></svg>
<figcaption>PJM preliminary effective load carrying capability ratings, delivery years 2028/29 to 2042/43. The 2030/31 ratings are not yet binding.</figcaption>
</figure>

## Why did 3,900 megawatts of data centres leave Virginia's grid in one morning?

Because every site did exactly what it was set to do, at the same moment. No equipment failed; the fault was in the sum.

<a id="the-power-it-drops"></a>

At 07:56 on 22 July 2026 a 230,000 volt line faulted in Dominion's zone. A **fault** is current rushing to the ground, through a failed part or a branch on a line, and while it lasts voltage sags across the whole area. Breakers opened within hundredths of a second, and PJM found no relay misoperated. The grid did its job.

<figure class="illo">
<p class="illo-title">Each site counts the dips and leaves on the third; PJM's rule says stay</p>
<p class="illo-sub">A fault the grid clears normally, as one data centre sees it, and PJM's proposed ride-through rule, simplified, not to scale in time</p>
<svg viewBox="0 0 940 350" role="img" aria-label="Left: what a data centre sees in a fault the grid clears normally. Voltage on the line falls to about a third of normal for about a twentieth of a second, the fault is cleared, and the line is retried twice, each retry another dip. The UPS counts the dips; a common setting is three within a minute, after which the site moves to its generators and stays there until staff switch it back. Its draw from the grid falls to nothing, and with that load gone the voltage overshoots. Right: PJM's proposed rule, how long a site must stay connected at each voltage: above 1.2 times normal it may trip; 1.1 to 1.2, one second; 0.9 to 1.1, always; 0.8 to 0.9, two seconds; 0.5 to 0.8, half a second; below half, a quarter of a second. It must then return to 90 per cent of its earlier draw within two seconds."><text class="i-head" x="10" y="18">What the site sees on the line, and what it does</text><line class="i-faint" x1="70" y1="65.0" x2="548" y2="65.0"/><text class="i-k" x="62" y="69.0" text-anchor="end">normal</text><line class="i-faint" x1="70" y1="127.5" x2="548" y2="127.5"/><text class="i-k" x="62" y="131.5" text-anchor="end">half</text><line class="i-ground" x1="70" y1="190" x2="548" y2="190"/><path class="i-line" d="M70 65.0 H130 L134 152.5 H142 L146 65.0 H250 L254 152.5 H262 L266 65.0 H370 L374 152.5 H382 L386 65.0 H410 C422 65.0 426 53.7 440 53.7 H466 C480 53.7 490 65.0 510 65.0 H548" style="fill:none"/><text class="i-n" x="138" y="168.5" text-anchor="middle">fault</text><text class="i-n" x="258" y="168.5" text-anchor="middle">retry</text><text class="i-n" x="378" y="168.5" text-anchor="middle">retry</text><text class="i-k" x="138" y="34" text-anchor="middle">cleared in about 0.05 s</text><text class="i-hot-t" x="450" y="45.7" text-anchor="middle">voltage overshoots</text><text class="i-k" x="62" y="236" text-anchor="end">draw</text><path class="i-cool" d="M70 230 H382 L386 260 H548" style="fill:none"/><circle class="i-fill" cx="138" cy="284" r="11"/><text class="i-t" x="138" y="289" text-anchor="middle">1</text><circle class="i-fill" cx="258" cy="284" r="11"/><text class="i-t" x="258" y="289" text-anchor="middle">2</text><circle class="i-hot-f" cx="378" cy="284" r="11"/><text class="i-t" x="378" y="289" text-anchor="middle">3</text><text class="i-n" x="70" y="316">The UPS counts the dips. A common setting: three within a minute,</text><text class="i-n" x="70" y="332">and the site moves to its generators until staff switch it back.</text><text class="i-hot-t" x="396" y="289">the site leaves the grid</text><text class="i-head" x="620" y="18">PJM's proposed rule: stay on for at least</text><text class="i-k" x="630" y="57" text-anchor="end">above 1.2</text><text class="i-n" x="648" y="57">may trip</text><text class="i-k" x="630" y="97" text-anchor="end">1.1 to 1.2</text><rect class="i-fill" x="640" y="80" width="92" height="24" rx="2"/><text class="i-n" x="740" y="97">1 s</text><text class="i-k" x="630" y="137" text-anchor="end">0.9 to 1.1</text><rect class="i-cool-f" x="640" y="120" width="218" height="24" rx="2"/><text class="i-n" x="866" y="137">always</text><text class="i-k" x="630" y="177" text-anchor="end">0.8 to 0.9</text><rect class="i-fill" x="640" y="160" width="120" height="24" rx="2"/><text class="i-n" x="768" y="177">2 s</text><text class="i-k" x="630" y="217" text-anchor="end">0.5 to 0.8</text><rect class="i-fill" x="640" y="200" width="66" height="24" rx="2"/><text class="i-n" x="714" y="217">0.5 s</text><text class="i-k" x="630" y="257" text-anchor="end">below 0.5</text><rect class="i-fill" x="640" y="240" width="39" height="24" rx="2"/><text class="i-n" x="687" y="257">0.25 s</text><text class="i-n" x="620" y="292">Voltage as a share of normal. Then back to 90%</text><text class="i-n" x="620" y="308">of its earlier draw within 2 seconds.</text><line class="i-faint" x1="600" y1="30" x2="600" y2="340"/></svg>
<figcaption>NERC incident review (January 2025) for the counting rule and the 2024 event; PJM's Markets and Reliability Committee deck (28 October 2026) for the rule. My drawing.</figcaption>
</figure>

Servers cannot tolerate even a short sag, so every data centre has a **UPS**, an uninterruptible power supply: batteries that take over the servers in milliseconds. Many sites also run a counting rule. A typical setting, NERC, which writes the grid's reliability standards, found, is three dips within one minute, after which the site moves to its generators until staff switch it back by hand.

Every site in the area sees the same dip and follows similar settings, so thousands of megawatts leave together. On 22 July about 2,900 MW left at once. With that load gone, voltage rose to about 1.14 times normal, and the high voltage set off a second wave of about 1,000 MW a minute later.

<figure class="chart">
<p class="chart-title">July's drop was the largest in PJM's history, and the third in two years</p>
<p class="chart-sub">Data centre load that moved to backup after a fault the grid cleared normally, megawatts</p>
<svg viewBox="0 0 560 306" role="img" aria-label="Bar chart of data centre load in PJM that switched to backup power after a fault the grid cleared normally, in megawatts. 10 July 2024: about 1,500, after six dips in 82 seconds. 17 February 2025: about 1,800, after four dips. 22 July 2026: about 3,900, in two waves, about 2,900 and then about 1,000 a minute later. For scale, the new plant and enlarged plants cleared in PJM's 2028/29 capacity auction: 525. A dashed line at 1,500 megawatts marks the size my test says must not recur in 2028."><g class="c-grid"><line x1="70" y1="190.0" x2="540" y2="190.0"/><line x1="70" y1="140.0" x2="540" y2="140.0"/><line x1="70" y1="90.0" x2="540" y2="90.0"/><line x1="70" y1="40.0" x2="540" y2="40.0"/></g><g class="c-axis"><text x="62" y="244.0" text-anchor="end">0</text><text x="62" y="194.0" text-anchor="end">1,000</text><text x="62" y="144.0" text-anchor="end">2,000</text><text x="62" y="94.0" text-anchor="end">3,000</text><text x="62" y="44.0" text-anchor="end">4,000</text></g><rect class="c-bar" x="106" y="165.0" width="68" height="75.0" rx="2"/><text class="c-lab c-s2t" x="140" y="157.0" text-anchor="middle">about 1,500 MW</text><text class="c-box-t" x="140" y="260" text-anchor="middle">10 Jul 2024</text><text class="c-note" x="140" y="275" text-anchor="middle">six dips in 82 s</text><rect class="c-bar" x="226" y="150.0" width="68" height="90.0" rx="2"/><text class="c-lab c-s2t" x="260" y="142.0" text-anchor="middle">about 1,800 MW</text><text class="c-box-t" x="260" y="260" text-anchor="middle">17 Feb 2025</text><text class="c-note" x="260" y="275" text-anchor="middle">four dips</text><rect class="c-bar" x="346" y="95.0" width="68" height="145.0" rx="2"/><rect class="c-bar c-alt" x="346" y="45.0" width="68" height="50.0" rx="2"/><text class="c-lab c-s2t" x="380" y="37.0" text-anchor="middle">about 3,900 MW</text><text class="c-box-t" x="380" y="260" text-anchor="middle">22 Jul 2026</text><text class="c-note" x="380" y="275" text-anchor="middle">two waves</text><rect class="c-bar c-mute" x="456" y="213.8" width="68" height="26.2" rx="2"/><text class="c-lab c-s2t" x="490" y="205.8" text-anchor="middle">525 MW</text><text class="c-box-t" x="490" y="260" text-anchor="middle">New plant</text><text class="c-note" x="490" y="275" text-anchor="middle">2028/29 auction</text><text class="c-note" x="420" y="113.0">2,900</text><text class="c-note" x="420" y="63.0">+1,000 a minute later</text><line class="c-today" x1="70" y1="165.0" x2="540" y2="165.0"/><line class="c-base" x1="70" y1="240" x2="540" y2="240"/><text class="c-note" x="70" y="298">Dashed line: 1,500 MW, the size my test says must not recur in 2028</text></svg>
<figcaption>NERC incident review (January 2025); PJM's Planning Committee deck (6 October 2026), which gives the February 2025 event as about 1,800 MW and July 2026 as about 3,900 MW; earlier PJM material gave about 1,500 and 3,800. PJM release on the 2028/29 auction (14 July 2026).</figcaption>
</figure>

It was not the first time. On 10 July 2024 about 1,500 MW of data centres moved to backup, NERC's review found, and on 17 February 2025 another fault moved about 1,800 MW. July's drop was about seven times the 525 MW of new and enlarged power stations that PJM's last capacity auction added.

## What is ride-through, and who now requires it?

**Ride-through** is a rule that a site must stay connected through a brief voltage or frequency disturbance, and be back to nearly its earlier draw within seconds. Texas has one in force; PJM files its own on 16 November.

The site must not open its breaker to the grid or jump to its generators. PJM's proposal covers sites of 50 MW or more with at least 25 MW behind power electronics. Between 90% and 110% of normal voltage a site must never leave, and deeper dips set shorter minimum times. New projects would comply from 16 January 2027, and existing sites by the later of 16 January 2028 or a year after switching on.

Texas went first. ERCOT's ride-through rule for large computing loads has been in force since 1 August 2026. The national standard is slower: NERC's first three standards for computing loads passed their final ballot in October, but on PJM's reading they only collect data. A minimum is expected in a standard in 2027.

## Who pays for the wait?

For now, everyone on the grid, through the auction that pays power stations to stand ready. In PJM that price has sat at its cap three times running.

<a id="pjm-sends-the-bill"></a>

PJM's **capacity auction** pays power stations, per megawatt per day, to be available in a delivery year three years ahead. It buys readiness, not energy, and the last megawatt needed sets everyone's price. When data centres join the forecast, PJM must buy more readiness, and the price rises for every customer.

<figure class="chart">
<p class="chart-title">PJM's auction has sat at its cap three times running, and the cap rises in December</p>
<p class="chart-sub">Price paid to power stations to stand ready, dollars per megawatt of capacity per day, by delivery year</p>
<svg viewBox="0 0 560 314" role="img" aria-label="Bar chart of PJM capacity auction prices in dollars per megawatt-day, by delivery year: 28.92 for 2024/25; 269.92 for 2025/26; then the cap three times running, 329.17 for 2026/27, 333.44 for 2027/28 and 325 for 2028/29. Without the cap the 2028/29 auction would have cleared at about 554.72, as reported from PJM. The auction for 2029/30, held in December 2026, has a cap of 337.83."><g class="c-grid"><line x1="60" y1="231.7" x2="540" y2="231.7"/><line x1="60" y1="193.3" x2="540" y2="193.3"/><line x1="60" y1="155.0" x2="540" y2="155.0"/><line x1="60" y1="116.7" x2="540" y2="116.7"/><line x1="60" y1="78.3" x2="540" y2="78.3"/><line x1="60" y1="40.0" x2="540" y2="40.0"/></g><g class="c-axis"><text x="52" y="274.0" text-anchor="end">$0</text><text x="52" y="197.3" text-anchor="end">$200</text><text x="52" y="120.7" text-anchor="end">$400</text><text x="52" y="44.0" text-anchor="end">$600</text></g><rect class="c-bar c-mute" x="69" y="258.9" width="52" height="11.1" rx="2"/><text class="c-lab c-s2t" x="95" y="250.9" text-anchor="middle">$28.92</text><text class="c-box-t" x="95" y="288" text-anchor="middle">2024/25</text><rect class="c-bar c-mute" x="149" y="166.5" width="52" height="103.5" rx="2"/><text class="c-lab c-s2t" x="175" y="158.5" text-anchor="middle">$269.92</text><text class="c-box-t" x="175" y="288" text-anchor="middle">2025/26</text><rect class="c-bar" x="229" y="143.8" width="52" height="126.2" rx="2"/><text class="c-lab c-s2t" x="255" y="135.8" text-anchor="middle">$329.17</text><text class="c-box-t" x="255" y="288" text-anchor="middle">2026/27</text><text class="c-note" x="255" y="303" text-anchor="middle">cap</text><rect class="c-bar" x="309" y="142.2" width="52" height="127.8" rx="2"/><text class="c-lab c-s2t" x="335" y="134.2" text-anchor="middle">$333.44</text><text class="c-box-t" x="335" y="288" text-anchor="middle">2027/28</text><text class="c-note" x="335" y="303" text-anchor="middle">cap</text><rect class="c-bar" x="389" y="145.4" width="52" height="124.6" rx="2"/><text class="c-lab c-s2t" x="415" y="137.4" text-anchor="middle">$325</text><text class="c-box-t" x="415" y="288" text-anchor="middle">2028/29</text><text class="c-note" x="415" y="303" text-anchor="middle">cap</text><rect class="c-zone" x="469" y="140.5" width="52" height="129.5" rx="2"/><line class="c-today" x1="465" y1="140.5" x2="525" y2="140.5"/><text class="c-lab c-s2t" x="495" y="132.5" text-anchor="middle">cap $337.83</text><text class="c-box-t" x="495" y="288" text-anchor="middle">2029/30</text><text class="c-note" x="495" y="303" text-anchor="middle">December</text><rect class="c-bar c-mute" x="389" y="57.4" width="52" height="88.1" rx="2" style="opacity:.35"/><text class="c-note" x="381" y="61.4" text-anchor="end">$554.72 without the cap, reported</text><line class="c-base" x1="60" y1="270" x2="540" y2="270"/></svg>
<figcaption>PJM auction reports and releases to 14 July 2026, and its 2029/30 planning parameters (31 August 2026). The uncapped 2028/29 price is as reported by the American Public Power Association from PJM's figures. The cap differs slightly each year.</figcaption>
</figure>

The price jumped from $28.92 a megawatt per day for 2024/25 to $269.92 for 2025/26. Since then it has hit the cap, the most the auction may pay, three times running. The cap has not called up new plant. The 2028/29 auction fell 6,831 MW short of PJM's own reliability requirement. PJM's independent market monitor argued that by 21 September 2026, 4,017 MW of forecast data centre load had been cancelled or delayed, on its arithmetic cutting the shortfall to 3,055 MW.

## How much of a household's bill is that?

Less than the headlines imply. Capacity was about a sixth of PJM's wholesale cost in the first half of 2026; data centres' share of it added about a tenth to the cost of each megawatt-hour.

The monitor attributes $6.3 billion, 38.2% of the 2028/29 auction, to data centre load.

<figure class="chart">
<p class="chart-title">Capacity tripled, but energy is still most of the cost</p>
<p class="chart-sub">PJM total wholesale cost of power, dollars per megawatt-hour, first half of each year</p>
<svg viewBox="0 0 560 200" role="img" aria-label="Stacked bar chart of PJM's total wholesale cost of power, in dollars per megawatt-hour. First half of 2025: 76.16, of which energy about 49, capacity about 6 and transmission about 19. First half of 2026: 114.50, of which energy about 73, capacity about 20 and transmission about 20. As published by PJM's market monitor."><g class="c-grid"><line x1="120.0" y1="30" x2="120.0" y2="150"/><line x1="215.0" y1="30" x2="215.0" y2="150"/><line x1="310.0" y1="30" x2="310.0" y2="150"/><line x1="405.0" y1="30" x2="405.0" y2="150"/><line x1="500.0" y1="30" x2="500.0" y2="150"/></g><g class="c-axis"><text x="120.0" y="22" text-anchor="middle">$0</text><text x="215.0" y="22" text-anchor="middle">$30</text><text x="310.0" y="22" text-anchor="middle">$60</text><text x="405.0" y="22" text-anchor="middle">$90</text><text x="500.0" y="22" text-anchor="middle">$120</text></g><text class="c-box-t" x="0" y="60">First half 2025</text><rect class="c-bar c-mute" x="120.0" y="44" width="155.9" height="26"/><text class="c-note" x="197.9" y="86" text-anchor="middle">$49</text><rect class="c-bar" x="275.9" y="44" width="20.2" height="26"/><text class="c-note" x="286.0" y="86" text-anchor="middle">$6</text><rect class="c-bar c-alt" x="296.1" y="44" width="59.7" height="26"/><text class="c-note" x="325.9" y="86" text-anchor="middle">$19</text><rect class="c-bar c-mute" x="355.8" y="44" width="5.4" height="26" style="opacity:.5"/><text class="c-lab c-s1t" x="367.2" y="62">$76.16</text><text class="c-box-t" x="0" y="120">First half 2026</text><rect class="c-bar c-mute" x="120.0" y="104" width="230.2" height="26"/><text class="c-note" x="235.1" y="146" text-anchor="middle">$73</text><rect class="c-bar" x="350.2" y="104" width="62.0" height="26"/><text class="c-note" x="381.2" y="146" text-anchor="middle">$20</text><rect class="c-bar c-alt" x="412.2" y="104" width="63.1" height="26"/><text class="c-note" x="443.8" y="146" text-anchor="middle">$20</text><rect class="c-bar c-mute" x="475.3" y="104" width="7.3" height="26" style="opacity:.5"/><text class="c-lab c-s1t" x="488.6" y="122">$114.50</text><rect class="c-bar c-mute" x="120" y="178" width="12" height="12"/><text class="c-note" x="138" y="188">energy</text><rect class="c-bar" x="230" y="178" width="12" height="12"/><text class="c-note" x="248" y="188">capacity</text><rect class="c-bar c-alt" x="340" y="178" width="12" height="12"/><text class="c-note" x="358" y="188">transmission</text><line class="c-base" x1="120" y1="30" x2="120" y2="150"/></svg>
<figcaption>PJM market monitor, report to the Members Committee (27 July 2026). It gives each part; the small remainder is other charges.</figcaption>
</figure>

In the first half of 2026, PJM's total wholesale cost was $114.50 per megawatt-hour. Energy, the power actually used, was 63.5% of it. Capacity tripled, to 17.1% of the total. The monitor puts the data centre effect on capacity at $11.11 per megawatt-hour, 9.7% of the wholesale cost. What reaches a household depends on its state. In Pennsylvania the regulator tied June 2026 rises of about 3% to 10% to PJM's capacity costs, as reported.

## Can the bill be moved to the data centres?

Only part of the way. FERC can send the bill to a zone, the area one utility serves; only the states can send it to a customer.

<a id="ferc-keeps-the-bill-shared"></a>

On 27 July 2026 PJM's board proposed that new sites of 50 MW or more that did not bring their own power stations would be cut first in a shortage. On 9 October FERC rejected that service, finding that parts of it appeared to be "an impermissible intrusion on retail rate regulation". "States have a crucial role", it said, "by designating which retail customers must be curtailed".

<a id="the-bill-changes-address"></a>

The fight moved to the **reliability backstop**, a one-time purchase of about 6,800 MW of new capacity. On 29 September FERC suspended it to 28 February 2027, mainly over the bill: PJM's measure of load growth could miss some new large loads. PJM refiled on 29 October: each zone would pay by its large-load growth between the actual 2026 summer peak and the 2028/29 forecast. Contracts run up to 15 years, averaging at most $555 a megawatt per day.

Which customers in a zone pay, FERC wrote, is for the states. In January all 13 PJM governors pledged to steer that cost to new data centres "that have not otherwise procured capacity or agreed to be curtailable". So the bill and the plug are one decision. A site would escape the charge by buying its own capacity or taking the plug the grid may cut first. None of it is in force.

<a id="virginia-bills-the-empty-site"></a>

The states have instead written long contracts with minimum bills. Virginia's new rate class for Dominion, GS-5, covers 25 MW or more for 14 years, with a minimum bill of 85% of contracted demand for distribution and for transmission, and 60% for generation. But PJM capacity costs are excluded from the generation minimum, so the auction stays shared.

## Of all the gigawatts signed, how many are running?

A fraction. Signed power runs far ahead of power at work, at the utility and at the operator alike.

<a id="contracted-energised-running"></a>

An AI campus passes five stages. **Contracted**: land and the right to power are signed. **Built**: the shell, cooling plant and substation go up. **Energised**: the utility switches the connection on. **Delivered**: the finished hall is handed to the tenant. **Running**: chips are drawing power for paying work. Only the last stage earns.

<figure class="chart">
<p class="chart-title">Dominion has about 54 gigawatts of data centres under contract, and bills 4.8</p>
<p class="chart-sub">Dominion Energy's data centre contracts in Virginia by stage, July 2026, and its data centre billing peak, August 2026, gigawatts</p>
<svg viewBox="0 0 560 212" role="img" aria-label="Bar chart of Dominion Energy's data centre contracts in Virginia, in gigawatts, as of July 2026: 32.5 under engineering letters of authorisation, 9.4 under construction letters and 12.0 under electric service agreements, about 54 in all. Data centre billing peak load in August 2026: 4.8."><g class="c-grid"><line x1="200.0" y1="28" x2="200.0" y2="192"/><line x1="282.9" y1="28" x2="282.9" y2="192"/><line x1="365.7" y1="28" x2="365.7" y2="192"/><line x1="448.6" y1="28" x2="448.6" y2="192"/></g><g class="c-axis"><text x="200.0" y="22" text-anchor="middle">0</text><text x="282.9" y="22" text-anchor="middle">10</text><text x="365.7" y="22" text-anchor="middle">20</text><text x="448.6" y="22" text-anchor="middle">30</text></g><text class="c-box-t" x="0" y="49">Engineering letters</text><text class="c-note" x="0" y="64">study the substation</text><rect class="c-bar c-mute" x="200" y="40" width="269.3" height="22" rx="2"/><text class="c-lab c-s1t" x="475.3" y="56">32.5 GW</text><text class="c-box-t" x="0" y="91">Construction letters</text><text class="c-note" x="0" y="106">start building it</text><rect class="c-bar c-mute" x="200" y="82" width="77.9" height="22" rx="2"/><text class="c-lab c-s1t" x="283.9" y="98">9.4 GW</text><text class="c-box-t" x="0" y="133">Service agreements</text><text class="c-note" x="0" y="148">both sides committed</text><rect class="c-bar c-alt" x="200" y="124" width="99.4" height="22" rx="2"/><text class="c-lab c-s1t" x="305.4" y="140">12.0 GW</text><text class="c-box-t" x="0" y="175">Billed at peak</text><text class="c-note" x="0" y="190">August 2026</text><rect class="c-bar" x="200" y="166" width="39.8" height="22" rx="2"/><text class="c-lab c-s1t" x="245.8" y="182">4.8 GW</text><line class="c-base" x1="200" y1="28" x2="200" y2="192"/></svg>
<figcaption>Dominion Energy to PJM's Load Analysis Subcommittee (29 September 2026). Dominion counts engineering letters as non-firm.</figcaption>
</figure>

An engineering letter pays Dominion to design the substation; a construction letter pays it to start building; an electric service agreement commits both sides. As of July 2026 Dominion had about 54 GW of data centres under one of the three, of which 12 GW was under service agreements. In August its data centres' billing peak was 4.8 GW. Its planning assumes the average site takes five years to reach 63% of the power it contracted. Its forecast leaves 19 GW of the engineering letters out altogether, and expects its data centres to draw about 7.8 GW at peak in 2030.

The operators show the same gap. CoreWeave, which rents out AI computing, had 3.7 GW contracted and 1.5 GW active at 30 June 2026, about 41%.

<figure class="chart">
<p class="chart-title">At the operators too, signed power runs far ahead of power at work</p>
<p class="chart-sub">Contracted, connected and active power, gigawatts</p>
<svg viewBox="0 0 560 314" role="img" aria-label="Bar chart in gigawatts. CoreWeave at 30 June 2026: 3.7 contracted, 1.5 active. Nebius: 5 contracted, its target for the end of 2026; 0.8 to 1 connected, its guide for the end of 2026; about 0.17 active at the end of 2025, its latest active figure."><g class="c-grid"><line x1="200.0" y1="28" x2="200.0" y2="294"/><line x1="249.1" y1="28" x2="249.1" y2="294"/><line x1="298.2" y1="28" x2="298.2" y2="294"/><line x1="347.3" y1="28" x2="347.3" y2="294"/><line x1="396.4" y1="28" x2="396.4" y2="294"/><line x1="445.5" y1="28" x2="445.5" y2="294"/></g><g class="c-axis"><text x="200.0" y="22" text-anchor="middle">0</text><text x="249.1" y="22" text-anchor="middle">1</text><text x="298.2" y="22" text-anchor="middle">2</text><text x="347.3" y="22" text-anchor="middle">3</text><text x="396.4" y="22" text-anchor="middle">4</text><text x="445.5" y="22" text-anchor="middle">5</text></g><text class="c-lab c-s2t" x="0" y="56">CoreWeave, 30 June 2026</text><text class="c-box-t" x="0" y="79">Contracted</text><text class="c-note" x="0" y="94">signed power</text><rect class="c-bar c-mute" x="200" y="70" width="181.6" height="22" rx="2"/><text class="c-lab c-s1t" x="387.6" y="86">3.7 GW</text><text class="c-box-t" x="0" y="121">Active</text><text class="c-note" x="0" y="136">chips drawing power</text><rect class="c-bar" x="200" y="112" width="73.6" height="22" rx="2"/><text class="c-lab c-s1t" x="279.6" y="128">1.5 GW</text><text class="c-lab c-s2t" x="0" y="170">Nebius</text><text class="c-box-t" x="0" y="193">Contracted</text><text class="c-note" x="0" y="208">end 2026 target</text><rect class="c-bar c-mute" x="200" y="184" width="245.5" height="22" rx="2"/><text class="c-lab c-s1t" x="451.5" y="200">5 GW</text><text class="c-box-t" x="0" y="235">Connected</text><text class="c-note" x="0" y="250">end 2026 guide</text><rect class="c-bar c-alt" x="200" y="226" width="39.3" height="22" rx="2"/><rect class="c-bar c-mute" x="239.3" y="226" width="9.8" height="22" rx="2"/><text class="c-lab c-s1t" x="255.1" y="242">0.8 to 1 GW</text><text class="c-box-t" x="0" y="277">Active</text><text class="c-note" x="0" y="292">end 2025, latest</text><rect class="c-bar" x="200" y="268" width="8.3" height="22" rx="2"/><text class="c-lab c-s1t" x="214.3" y="284">about 0.17 GW</text><line class="c-base" x1="200" y1="28" x2="200" y2="294"/></svg>
<figcaption>CoreWeave earnings release (11 August 2026); Nebius shareholder letters (12 February and 12 August 2026). Nebius has never reported connected and active power for the same date; its third-quarter letter is due on 12 November 2026.</figcaption>
</figure>

<a id="nebius-paid-for-what-is-switched-on"></a>

Nebius, another operator, expects 5 GW contracted by the end of 2026, against 800 MW to 1 GW connected. Revenue follows the last stage: its US$17.4 billion agreement with Microsoft is "subject to the satisfaction of the deployment and availability of the GPU Services". Oracle's customers have signed US$664 billion of future revenue, of which it expects only about 13% in the next twelve months, because revenue starts as halls are delivered. So any model that sizes revenue or chip demand from contracted gigawatts runs early, by quarters or years.

## Where does the time go between signing and running?

Mostly before energised, in the stage the builder controls least. After that, the tenant sets the pace.

<a id="power-first-chips-last"></a>

Jane Street, the trading firm that builds its own AI halls, buys power first, because generators, transformers and some liquid cooling kit can take more than a year. It picks a chip once the building is nearly ready.

<a id="abilene-switched-on-in-stages"></a>

At Abilene, Texas, Crusoe builds, Oracle leases the campus and OpenAI uses the computing. Work on the first two buildings began in June 2024, and Crusoe says they were energised within a year.

<figure class="chart">
<p class="chart-title">Abilene arrived building by building, and the chips arrived with the power</p>
<p class="chart-sub">Construction start to running, and handover of capacity to Oracle's customer</p>
<svg viewBox="0 0 560 250" role="img" aria-label="Timeline of the Abilene campus. Phase one, two buildings: construction began in June 2024, the first Nvidia GB200 racks arrived in June 2025, and it was running by 30 September 2025. Phase two, six buildings: construction began in March 2025 and Crusoe expects completion by the end of 2026. Handover to Oracle's customer: 42 per cent of capacity by 10 June 2026, 75 per cent, six of eight buildings, by 10 September 2026, and the rest due in the quarter ending 30 November 2026.">
<g class="c-grid"><line x1="175" y1="20" x2="175" y2="205"/><line x1="293.3" y1="20" x2="293.3" y2="205"/><line x1="411.7" y1="20" x2="411.7" y2="205"/><line x1="530" y1="20" x2="530" y2="205"/></g>
<g class="c-axis"><text x="175" y="226" text-anchor="middle">2024</text><text x="293.3" y="226" text-anchor="middle">2025</text><text x="411.7" y="226" text-anchor="middle">2026</text><text x="530" y="226" text-anchor="middle">2027</text>
<text x="165" y="54" text-anchor="end">Phase one, 2 buildings</text>
<text x="165" y="114" text-anchor="end">Phase two, 6 buildings</text>
<text x="165" y="174" text-anchor="end">Handed to the customer</text>
</g>
<line class="c-today" x1="509.9" y1="14" x2="509.9" y2="205"/><text class="c-today-t" x="509.9" y="12" text-anchor="middle">today</text>
<g class="c-span"><line x1="224.3" y1="50" x2="381.8" y2="50"/><line x1="313.1" y1="110" x2="530" y2="110"/><line x1="463.9" y1="170" x2="519.8" y2="170"/></g>
<g class="c-start"><circle cx="224.3" cy="50" r="4"/><circle cx="313.1" cy="110" r="4"/></g>
<g class="c-end"><circle cx="381.8" cy="50" r="4.5"/><circle cx="530" cy="110" r="4.5"/><circle cx="463.9" cy="170" r="4.5"/><circle cx="493.5" cy="170" r="4.5"/><circle cx="519.8" cy="170" r="4.5"/></g>
<g class="c-plant"><line x1="347.2" y1="56" x2="347.2" y2="66"/><text x="347.2" y="80" text-anchor="middle">first racks, June 2025</text></g>
<g class="c-endt"><text x="390.8" y="54">running by 30 Sep 2025</text><text x="530" y="96" text-anchor="end">complete by end 2026, expected</text><text x="463.9" y="156" text-anchor="middle">42%</text><text x="493.5" y="156" text-anchor="middle">75%</text><text x="519.8" y="192" text-anchor="end">the rest due by 30 Nov 2026</text></g>
</svg>
<figcaption>Crusoe releases (21 May 2025, 30 September 2025, 27 March 2026); Oracle's results calls of 10 June and 10 September 2026, as transcribed by The Motley Fool, since I found no primary copy. Crusoe gives no energisation date for phase two. Oracle reports handover, not chips at work, by site.</figcaption>
</figure>

The first racks of Nvidia's GB200 chips arrived in June 2025, and the first phase was running by 30 September. Oracle reported six of eight buildings, 618 MW, handed over by 10 September 2026, as transcribed from its calls. The chips came with the power, so energised set the pace. Even so, more than two years passed between the start of work and three quarters of the campus handed over.

## So who holds the scarce thing, and what should an investor watch?

Whoever controls a site's terms: firm or cut first, for how many hours, with what backup and what bill. Those terms sit in tariff filings and contracts, public and rarely read.

Almost nobody discloses which plug they bought: that is the gap investors cannot see.

If the claim is right, four kinds of business gain. **Backup that runs for hours**: gas turbines, engines, fuel cells and long batteries. **Kit that holds on**: ride-through turns the UPS and switchgear into compliance equipment. **Load that can slow**, if a slowed chip is ever accepted as a connection term. **The makers of the upgrades**, whose queue is the reason for all of it.

The readings come quickly: the grids' large-load filings on 16 November, ERCOT's audit by 10 December, and PJM's 2029/30 auction in December.

## What would prove me wrong

Three tests can break the claim. First, if by the end of 2027 fewer than two of the seven organised grids have a real data centre of 50 MW or more switched on under a cut-first tier, shown in a filed agreement, the rationing is on paper only. Texas's power to shed every large load in an emergency is load shedding, not a tier.

Second, if PJM reports another transfer of 1,500 MW or more after a normally cleared fault in 2028, after existing sites were due to comply, holding on changed nothing. Third, if makers add factories fast enough and PJM's new yearly process works, developers take firm service and the lower tier empties. A firm partial plug such as PJM's planned Fractional NITS taking the place of the cut-first one would point the same way.

The stages have tests of their own, from my earlier claims. At Abilene, if the campus is energised but Oracle has still not reported all eight buildings delivered by its March 2027 results, fitting out, not power, is setting the pace. At Nebius, if it connects at least 800 MW by the end of 2026 but has fewer than 800 MW active at 30 June 2027, its halls are waiting for chips, not power. And if transformer and generator lead times fall back to months while chips become the longest wait again, power first and chips last breaks.

What would not move me is the view that contracted gigawatts are fine because everything gets built eventually. Eventually is the whole question.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

**America rations the plug** (30 October 2026)

Claim: "America is rationing the grid connection rather than speeding it up: by the end of 2027, data centres of 50 megawatts or more will be running on an early-connection tier the grid may cut first in at least two of its seven organised grids, and once PJM's ride-through deadline for existing sites passes, its data centres will stop dropping to backup power in blocks of 1,500 megawatts or more after normally cleared faults."

Breaks if: "By 31 December 2027, fewer than two of ERCOT, PJM, MISO, SPP, NYISO, ISO New England and CAISO have a load of 50 MW or more, mainly a data centre, actually energised under an early-connection tier the grid may cut first, such as ERCOT's Provisional Controllable Load Resource, SPP's CHILLS, PJM's Interim NITS or CAISO's flexible interim service, shown in a filed service agreement or the operator's own report; curtailment rights that apply to all large loads during emergency load shed, such as Texas Senate Bill 6, do not count. Or, between 16 January 2028 and 31 December 2028, PJM reports a transfer of 1,500 MW or more of large load to backup generation or off the grid after a normally cleared fault."

Five earlier claims on the plug, the battery and the stages, word for word:

**Contracted, energised, running** (30 October 2026)

Claim: "An AI campus's capacity arrives in stages, and energised power is the last one its builder controls: at Abilene, whose tenant ordered its chips with the campus, and at Nebius, which installs its own chips under contracts with delivery dates, computing follows the power within months, so contracted or announced gigawatts overstate it, while in Malaysia, where Johor holds two thirds of secured data centre capacity, halls can be energised and let well before they run."

Breaks if: "Crusoe reports the Abilene campus energised or complete by the end of 2026 but Oracle has not reported all eight buildings delivered to its customer by its results for the quarter ending 28 February 2027, or Nebius reports at least 800 megawatts connected at the end of 2026 but, at 30 June 2027, reports active power below 800 megawatts or, if it reports no active figure, annualised revenue below US$9.6 billion, 800 megawatts at its stated 2026 base of US$12 million a megawatt."

Where later evidence bears on it: Open. Oracle put Abilene's last two buildings in its quarter to 30 November 2026; its December results are the reading, and nothing confirms delivery by 7 November. Nebius reports its connected power on 12 November. The Malaysian limb is followed in the piece on Johor and Singapore.

**The grid's new problem is not the power AI uses, it is the power it drops** (22 September 2026)

Claim: "The grid's new problem with AI data centres is not the power they draw. It is the gigawatts they can drop in under a second."

Breaks if: "Ride-through turns out to be a cheap settings change rather than a constraint, or Virginia's 3.8 gigawatt trip proves to be a local fault rather than how these sites are built."

Where later evidence bears on it: The fault "cleared properly" and this was PJM's third such transfer in about two years, which supports the second limb; PJM later put the July event at about 3,900 MW. The first limb is open: nobody has published what compliance costs. PJM times the event to the minute, and its second wave came a minute after the first, so "under a second" is my reading, not PJM's figure.

**The battery has quietly stopped being an energy product** (22 September 2026)

Claim: "Large batteries are increasingly bought as connection equipment that lets a site switch on early, not as a way to trade electricity."

Breaks if: "New storage stops clustering where computing load is and spreads out with renewable generation instead, or connection waits shorten enough that opening early stops being worth paying for."

Where later evidence bears on it: California's 17.3 GW fleet is a time-shifter, earning about four times as much from shifting energy as from balancing. My count of the 2026 summer narrows the claim to, at most, the newest buyers beside data centres. Texas's planned 12.9 GW counts grid batteries, which also trade, and no one publishes the share at data centre sites. PJM rates a four-hour battery below demand response, and falling.

**Nebius has lined up five gigawatts of power. It expects about one switched on this year.** (30 September 2026)

Claim: "AI buyers pay for connected power, and Nebius's edge is turning contracted power into connected power faster than they can."

Breaks if: "Prepayments fade, or Nebius misses 800 megawatts connected by the end of 2026, or its customers start selling their own spare capacity."

Where later evidence bears on it: Against the first limb: on Nebius's own definitions buyers pay for active power, chips installed and running, which comes after connection. The 800 MW limb is unresolved until Nebius reports the end of 2026. Its letter of 12 August put prepayments in about 70% of second quarter deals, and nothing since shows them fading. I have found no primary evidence of a Nebius customer selling its spare capacity.

**Jane Street now commits to the power first and picks the chips last** (25 September 2026)

Claim: "The order builders commit in reveals the constraint, and at Jane Street power now comes first and chips last."

Breaks if: "Chips become the longest wait again while transformer and generator lead times fall back to months, or dropping full generator backup proves a false saving."

Where later evidence bears on it: Nothing I have found cuts against it. It rests on one firm's own account, and I have no published outage record to test the generator saving either way. Jane Street's US$6 billion commitment to CoreWeave in April gives no megawatts or dates: a builder short of finished power also rents it.

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

**The two queues.** Lawrence Berkeley National Laboratory, Queued Up, 2025 edition (15 December 2025): about 2,290 GW of generation and storage in queues at the end of 2024; median 55 months from request to operation for projects completed in 2024; it counts power stations and storage only, not loads. FERC, PJM show cause order, EL26-67-000, 195 FERC ¶ 61,211 (18 June 2026): load requests "submitted to transmission owners, who have their own study processes and requirements"; study "should take no more than 60-90 days"; data centres "may only take 1-2 years to construct", quoting comments in the record; draft definition of a large load as a new site of 50 MW or more above 69 kV, not co-located.

**Texas.** Office of the Texas Governor (3 August 2026): "approximately over 474 gigawatts of requests to connect", "more than five times Texas' record peak electricity demand", about 90% data centres. ERCOT Senate briefing (29 July 2026): 474 GW as of June, about 205 GW eligible for Batch Zero, preliminary. ERCOT presentation to the Public Utility Commission of Texas (20 August 2026): 17 loads, 6,608 MW, cleared all but approval to energise; approvals paused for data centres and crypto loads of 75 MW or more; verification report by 10 December 2026. ERCOT's record hourly peak of 91.1 GW on 22 July 2026 (EIA, 3 August 2026), so 474 GW is about 5.2 times; 6.6 GW is under a seventieth of 474 GW, my arithmetic. Oncor Form 8-K exhibit (5 November 2026): 795 requests in the large commercial and industrial transmission queue at 30 September 2026, about 293 GW from data centres; Batch Zero classifications of about 24 GW base load, including 10 GW already energised, and 21 GW studied load, "conditional pending the results of an ERCOT audit ... expected in December 2026"; final transmission plan "not expected until fall of 2027". AEP Form 8-K exhibit (28 October 2026): 15 GW of new load commitments signed in the third quarter; contracted load expected to grow to 84 GW by 2031, counting only executed agreements or letters of agreement.

**The tiers.** Department of Energy, advance notice of proposed rulemaking, RM26-4-000 (23 October 2025), for loads over 20 MW, asking for final action by 30 April 2026 (law-firm summaries); no final rule by 7 November 2026. FERC show cause orders EL26-67 to EL26-72 (18 June 2026), for PJM, SPP, NYISO, MISO, CAISO and ISO New England; PJM and PJM transmission owner filings due 16 November 2026 after a 90-day abeyance; responses 16 November (SPP 20 November), answers 16 December (docket summaries). ERCOT Provisional Controllable Load Resource, part of PGRR145 and NPRR1325, approved by the Texas regulator 18 June 2026; system implementation at 2027 priority (summary of ERCOT's Technical Advisory Committee report). SPP CHILLS, 195 FERC ¶ 61,196 (5 June 2026), effective 1 July 2026, non-firm for up to seven years; the generation condition and docket number are from trade press. PJM Interim NITS: FERC co-location orders, EL25-49-000 (18 December 2025) and EL25-49-002 (18 June 2026); PJM transmission owners' notice to the Members Committee (9 October 2026): "capacity will not be procured on behalf of Interim NITS customers", and Fractional NITS, "a firm service, based on available system capacity". FERC order ER26-3515-000, 197 FERC ¶ 61,019 (9 October 2026): Large Load definition of 50 MW at a single electrical site, affiliated facilities within one mile counted as one, no voltage threshold, accepted from 12 October 2026. CAISO board approval 28 October 2026 (American Public Power Association); CAISO straw proposal (11 August 2026): developers "would only agree to be flexible temporarily". NYISO (Energy Central, 3 November 2026; filing date reported as 16 November or December). MISO's Large Load Addition Resource Study, filed 2 October 2026 (Utility Dive, 5 October 2026). "None found" means I found no primary record by 7 November 2026.

**Hours of cuts.** Duke University Nicholas Institute, Rethinking Load Growth (11 February 2025), 22 largest balancing authorities: 76, 98 and 126 GW at 0.25%, 0.5% and 1% of annual energy curtailed; about 85, 177 and 366 hours; 88% of curtailment hours with at least half the new load running; average event about two hours. I could not open the report; these figures are from the institute's summary and trade press. Indiana Utility Regulatory Commission, Cause 46276 order (April 2026): size, contract length, curtailment amounts and event performance confidential pending subdocket 46276 S1; the quoted testimony is the order's summary. Texas Senate Bill 6 (2025), PURA 39.170(a): loads at transmission voltage connected after 31 December 2025 must be able to be curtailed during firm load shed. I did not read SPP's CHILLS curtailment terms; "no cap" means I found none.

**Backup.** Federal air rule for emergency stationary engines, 40 CFR 63.6640(f), and the parallel new source rules: no limit on emergency running; 100 hours a year for maintenance and testing, of which up to 50 may be non-emergency, and may earn money only when the local balancing authority or transmission operator dispatches the engine to mitigate local conditions that could lead to voltage collapse or line overloads. EPA letter to NRG Energy (24 June 2026): a programme passing on PJM's local dispatch meets the criteria; EPA's earlier interpretation for Duke Energy (30 April 2025). Virginia HB 507 (2026) and DEQ guidance APG-576 (revised 9 April 2026): Tier 4-equivalent controls for data centre generators in applications from 1 July 2026 (law-firm summaries). Texas Senate Bill 6, PURA 37.0561(e): large loads disclose backup able to serve at least 50% of on-site demand; the provision "does not authorize or require a violation of any emissions limitation".

**Chips that slow.** Google blogs of 4 August 2025 and 19 March 2026: 1 GW of demand response with five utilities, to "limit or shift a portion" of machine learning workloads. DTE Energy Form 8-K (28 September 2026): up to 1,600 MW of renewables, 480 MW of storage and 350 MW of demand response for the Van Buren Township site. Michigan Public Service Commission approval (1 October 2026); the Attorney General's rehearing petition (Michigan Public, 30 October 2026). Phoenix trial: Emerald AI and others, arXiv 2507.00909 (1 July 2025), 256 GPUs, 25% for three hours. Nvidia blog (16 September 2026) on the AI Energy Management Alliance.

**Batteries.** CAISO Key Statistics, October 2026: 17,285 MW of batteries at 31 October 2026 (17,307 MW at 30 September, the count covering commercial units only). CAISO Department of Market Monitoring, 2025 annual report: about $35 per kW-year from energy against $9 from regulation. The evenings count is mine, from CAISO's five-minute fuel mix, June to September: batteries the largest source at the net peak, demand less wind and solar, on 0, 10, 52 and 66 of 122 evenings in 2023 to 2026. PJM preliminary effective load carrying capability ratings, delivery years 2028/29 to 2042/43: demand response 91%, 90% and 84%; four-hour storage 59%, 57% and 42%, for 2028/29, 2029/30 and 2030/31, the last non-binding.

**The 22 July event.** PJM System Operations Subcommittee deck (31 July 2026) and Planning Committee deck (6 October 2026): about 2,900 MW and then about 1,000 MW "a minute later", about 3,900 MW in all (3,800 MW in PJM's July and August decks); 230 kV fault after a mechanical failure; no relay misoperations or stuck breakers; peak voltage about 1.138 per unit; Eastern Interconnection frequency 60.092 Hz; recovery within nine minutes against 30 allowed; "all observed CILR events have involved already operational facilities", among draft recommendations of NERC's Large Loads Working Group. NERC incident review, Considering Simultaneous Voltage-Sensitive Load Reductions (January 2025): 10 July 2024, about 1,500 MW, all of it data centre load, six faults in 82 seconds, fault durations of 42 to 66 milliseconds, a typical trigger of three disturbances within one minute, most load not returning for hours. PJM's 6 October deck gives the 17 February 2025 event as about 1,800 MW; earlier PJM material gave about 1,500 MW. Seven times is 3,900 MW against 525 MW, my arithmetic.

**Ride-through.** PJM Markets and Reliability Committee deck (28 October 2026) and Planning Committee deck (8 September 2026): large computational loads of 50 MW or more with at least 25 MW through power electronics; voltage: above 1.20 per unit may trip, 1.10 to 1.20 for one second, 0.90 to 1.10 continuously, 0.80 to 0.90 for two seconds, 0.50 to 0.80 for half a second, below 0.50 for a quarter of a second; frequency 58.8 to 61.2 Hz continuously, 57.0 to 58.8 and 61.2 to 61.8 Hz for 299 seconds; recovery to 90% of prior power within two seconds; new projects from 16 January 2027, existing sites by the later of 16 January 2028 or a year after commercial operation; acceleration to 90 days; "limited exceptions when demonstrated that requirements cannot be met"; FERC filing 16 November 2026; ramp-rate filing in the second quarter of 2027. Dominion's floor of six reclosing attempts, as PJM summarised it (8 September 2026). ERCOT NOGRR 282: approved by the Texas regulator 9 July 2026, effective 1 August 2026; sites operational, approved to energise or with signed agreements on or before 14 November 2025 exempt; the 0.5 to 0.8 per unit band fully enforced from 1 January 2028. FERC order RD26-7-000 (16 July 2026). NERC Project 2026-02, final ballot announced 15 October 2026; PJM's deck of 31 July 2026: phase one "will not address the minimum voltage or frequency ride-through"; a minimum "expected to become part of a Reliability Standard in 2027". NERC registry petition (21 October 2026): 50 MW at 100 kV, about 68 GW (law-firm summary). Choukse and others, on power stabilisation for AI training sites, arXiv 2508.14318 (August 2025). Nvidia technical blog on the GB300 NVL72 power shelf (28 July 2025): 65 joules per GPU, peak grid demand cut 30% in a training run.

**PJM's capacity auction.**

| Delivery year | Held | Result |
|---|---|---|
| 2024/25 | December 2022 | $28.92 per MW-day |
| 2025/26 | July 2024 | $269.92 |
| 2026/27 | July 2025 | $329.17, the cap |
| 2027/28 | December 2025 | $333.44, the cap; 6,623 MW short of the reliability requirement, counting capacity utilities supply outside the auction (FERC, 29 September 2026) |
| 2028/29 | July 2026 | $325, the cap; $16.4 billion; 6,831 MW short; 525 MW of new and enlarged power stations |
| 2029/30 | December 2026 | cap $337.83, floor $181.91; requirement 158,712 MW |

PJM releases and auction reports; the 2029/30 parameters are from PJM's planning period parameters report (posted 31 August 2026). The uncapped 2028/29 price of $554.72 is from the American Public Power Association's report of PJM's figures; it is not in PJM's release. FERC accepted the collar's extension (ER26-1556, 28 April 2026, law-firm summary). The 4,017 MW of cancelled or delayed data centre load and the 3,055 MW shortfall are the market monitor's, as FERC recounted them in its order of 29 September 2026 (ER26-3380).

**The household bill.** Monitoring Analytics, the PJM market monitor, report to the Members Committee (27 July 2026): data centre load $6.3 billion, 38.2% of the 2028/29 auction; $29.4 billion over the four auctions from 2025/26; total wholesale cost $114.50 per MWh in the first half of 2026 against $76.16 a year earlier, up 50.3%; energy up 47.7% and 63.5% of the total; capacity up 207.1% and 17.1%; transmission up 5.6% and 17.4%; data centre capacity effect $11.11 per MWh, 9.7%. Energy $49.21, capacity $6.39 and transmission $18.82 in the first half of 2025; $72.68, $19.61 and $19.88 in the first half of 2026; energy was $155.39 per MWh in January 2026 and $82.06 in February, in Winter Storm Fern. Pennsylvania Public Utility Commission (20 May 2026), as reported. Virginia Joint Legislative Audit and Review Commission, Report 598 (9 December 2024).

**Moving the bill.** PJM Board decision (Inside Lines, 27 July 2026). FERC ER26-3515 (9 October 2026), paragraphs 77, 94 and 95. FERC ER26-3380 and EL26-108, 196 FERC ¶ 61,245 (29 September 2026): backstop accepted, suspended to 28 February 2027, subject to refund, paper hearing; relying on Load Adjustments "may be inconsistent or not reasonably capture forecasted load growth or actual large load growth"; costs go first to Electric Distributor zones, "with the ultimate cost allocation to the LSEs as determined by the state"; the backstop was suspended for a paper hearing on three issues (cost allocation, transmission owner exit rules, collateral); it quotes the White House and the governors of all 13 PJM states agreeing to "use all available authorities" so that their states' load-serving entities allocate the backstop cost to new data centre loads "that have not otherwise procured capacity or agreed to be curtailable" (Department of Energy, Statement of Principles Regarding PJM, January 2026). PJM, Inside Lines (29 October 2026), on its amended filing: procurement from 1 March 2027, bid window closing 28 March, results 10 May; target of about 6,800 MW to be recalculated and reduced by bilateral contracts; costs "based on Large Load growth between the actual summer peak load in 2026 and the forecast for the 2028/2029 Delivery Year", assigned to each zone by its contribution; terms of up to 15 years; maximum willingness to pay a MW-weighted average of $555 per MW-day.

**The states.** Virginia State Corporation Commission, final order, Case PUR-2025-00058 (25 November 2025), pages 23 to 27, Rate Schedule GS-5. AEP Ohio data centre tariff, PUCO Case 24-508-EL-ATA (9 July 2025); terms from trade press. Georgia Public Service Commission (23 January 2025). Indiana Michigan Power settlement (approved February 2025, trade press). Oregon POWER Act (2025). Texas Senate Bill 6, PURA 37.0561, and the Texas regulator's large-load rule (adopted September 2026, trade press). AEP Ohio queue: more than 30 GW of interest, 13,022.7 MW of formal requests and 5,642 MW signed under the tariff, from AEP's letter to PUCO of 12 February 2026 as reported by New Project Media.

**Signed against running.** Dominion Energy to PJM's Load Analysis Subcommittee (29 September 2026): contracts as of July 2026 of 32,473 MW under engineering letters of authorisation, 9,356 MW under construction letters and 11,997 MW under electric service agreements; data centre billing peak load of 4.8 GW as of August 2026; "industry average ramp period is 5 years maturing at a utilization rate of 63%". CoreWeave earnings releases: about 470 MW active and 2.2 GW contracted at 30 June 2025; 1.5 GW and about 3.7 GW at 30 June 2026 (11 August 2026). Nebius shareholder letters (12 February, 13 May and 12 August 2026): 5 GW contracted target and 800 MW to 1 GW connected guide for the end of 2026; about 170 MW active at the end of 2025; the Microsoft agreement. Oracle Form 10-Q (11 September 2026): US$288 billion of lease commitments not yet commenced, and US$664 billion of remaining performance obligations, about 13% to be recognised in the next twelve months, substantially all for data centres, in its words, commencing from the second quarter of fiscal 2027 to fiscal 2029. Percentages and ratios are my arithmetic.

**Abilene and the tenants.** Crusoe releases (18 March 2025, 21 May 2025, 30 September 2025, 27 March 2026): 1.2 GW grid interconnection, gas turbines for backup. Oracle results calls of 10 June and 10 September 2026, as transcribed by The Motley Fool: 42% of capacity and then six of eight buildings, 618 MW. Crusoe gives no energisation date for phase two. Dwarkesh Patel podcast with Dan Pontecorvo (21 May 2026). Microsoft fiscal 2027 first-quarter call (28 October 2026). Satya Nadella on the BG2 podcast (November 2025, as reported).

</details>

<section class="exposure">
<h3>Who is exposed if America rations the plug</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>Rules and wires</dt>
<dd><span class="names">FERC</span>, <span class="names">NERC</span>, <span class="names">ERCOT</span> and <span class="names">PJM</span> set the terms. <span class="names">Dominion Energy</span>, <span class="names">Oncor</span> and <span class="names">American Electric Power</span> build the lines.</dd>
<dt>Backup on site</dt>
<dd><span class="names">GE Vernova</span> makes turbines, <span class="names">Caterpillar</span> engines, <span class="names">Bloom Energy</span> fuel cells and <span class="names">Tesla Energy</span> batteries.</dd>
<dt>Kit that holds on, and chips that slow</dt>
<dd><span class="names">Schneider Electric</span>, <span class="names">Eaton</span> and <span class="names">Vertiv</span> make UPS and switchgear. <span class="names">Emerald AI</span> makes software that slows AI work for <span class="names">Google</span> and others.</dd>
<dt>Between signing and running</dt>
<dd><span class="names">CoreWeave</span>, <span class="names">Nebius</span> and <span class="names">Oracle</span> rent out computing; <span class="names">Crusoe</span> builds campuses.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Developers counting on firm power from day one, models that count signed gigawatts as running ones, and PJM's households while the bill stays shared.</dd>
</dl>
</section>

---

<p class="sources">Sources: FERC orders EL26-67 (18 June 2026), ER26-3380 (29 September 2026) and ER26-3515 (9 October 2026); PJM's amended backstop filing (29 October 2026); PJM decks to its committees (31 July, 8 September, 6 and 28 October 2026), auction reports and the market monitor's report (27 July 2026); ERCOT and the Texas Governor (July and August 2026); NERC's incident review (January 2025); the Virginia State Corporation Commission's GS-5 order (25 November 2025); Dominion to PJM (29 September 2026); Oncor, AEP, CoreWeave, Nebius and Oracle filings; Duke University (February 2025). Trade press only where marked. Personal research, not investment advice.</p>
