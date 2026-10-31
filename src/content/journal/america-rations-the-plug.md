---
title: "America rations the plug: who may be cut, who must hold on, who pays"
date: 2026-09-22T18:53:00+08:00
summary: "America's grids cannot build wires as fast as data centres arrive, so they are rationing the connection instead. Texas and the federal regulator are adding a cheaper plug the grid may cut first beneath the firm one, PJM's households pay for the power stations that are not being built, and after 3,800 megawatts of data centres dropped off Virginia's grid in one morning, the sites that stay must also hold on when the grid wobbles."
category: "Analysis"
cover: "/covers/america-rations-the-plug.svg"
tags: ["grid", "power", "data-centres"]
draft: false
---

On 3 August 2026 the Governor of Texas said ERCOT, which runs most of the state's grid, was weighing over 474 gigawatts of requests to connect. That is more than five times the most power Texas has ever used at once, and about nine tenths of it is data centres.

Twelve days earlier, a fault on a power line in Dominion Energy's part of Virginia cleared exactly as designed. Even so, about 3,800 megawatts of data centres switched themselves off the grid and onto their backup generators.

One grid has too many data centres asking to come on. The other has data centres that leave when nobody asked them to. America's answer to both is the same: it is not speeding up the connection, it is rationing it.

The reason is the wires. A firm connection is the grid's promise to carry a site's power at all times, short of an emergency. Before giving one, the grid operator lists the new lines, substations and transformers it needs, and those take years. A data centre's shell goes up far faster.

So grids are starting to sell the connection in tiers. The full tier still waits for the wires. A lower one switches on sooner, but the grid may cut it first when lines are strained, or lets it on only if the site brings its own power.

The second rule points the other way. A site must ride through a disturbance, staying connected through a brief dip or swell in voltage rather than fleeing to its generators. The grid wants data centres to stay on when it wobbles and to come off only when it asks. That makes what backs a site up, a generator, a battery or software that slows its chips, part of the connection itself.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture a block of flats whose fuse box is full, with the electrician booked for years. The landlord still lets new tenants in, on terms: your heater goes off first when the fuse runs hot, or you bring a camping stove.</p>
<p>And when a bulb flickers, you may not yank every plug at once. Nobody gets a bigger fuse sooner. The landlord only decides who goes dark first.</p>
</details>

Someone pays for the wait. PJM runs the grid from Chicago to Virginia, and its auction to keep power stations ready for 2028 fell 6,831 megawatts short of its own reliability target. New plants and upgrades added only 525 megawatts. The gap reaches household bills.

A megawatt the grid may cut is not the same product as a firm one. For anyone building a data centre in America, the question is no longer only how much power, but which kind, and on what terms it can be taken away.

<hr class="layer">
<p class="layer-label">For investors</p>

## Texas has far more asking than it can connect

<a id="ercot-rations-the-plug"></a>

The clearest picture of the rationing is the Texas queue, measured at each gate a request must pass. The Governor's 474 GW is the top. ERCOT told the state Senate on 29 July that only about 205 GW had the studies to enter its first batch. By 20 August, 6,608 MW across 17 sites had cleared every check except approval to switch on.

<figure class="chart">
<p class="chart-title">Texas has been asked for 474 gigawatts, and has cleared 6.6</p>
<p class="chart-sub">Requests to connect large loads to ERCOT at each gate, in gigawatts, summer 2026</p>
<svg viewBox="0 0 560 170" role="img" aria-label="Bar chart. Over 474 gigawatts of requests to connect to ERCOT, about 205 gigawatts with the studies to enter its first batch, and 17 large loads totalling 6,608 megawatts that had cleared every check except approval to switch on, which ERCOT then paused for data centres of 75 megawatts or more.">
<g class="c-axis">
<text x="190" y="49" text-anchor="end">Asked to connect</text>
<text x="190" y="99" text-anchor="end">Studied enough to enter</text>
<text x="190" y="149" text-anchor="end">Cleared all but switch-on</text>
</g>
<rect class="c-bar" x="200" y="30" width="280" height="28" rx="2"/>
<text class="c-lab c-s2t" x="488" y="49">474 GW</text>
<rect class="c-bar" x="200" y="80" width="121.1" height="28" rx="2"/>
<text class="c-lab c-s2t" x="329.1" y="99">about 205 GW</text>
<rect class="c-bar" x="200" y="130" width="3.9" height="28" rx="2"/>
<text class="c-lab c-s2t" x="211.9" y="149">6.6 GW, then paused</text>
<line class="c-base" x1="200" y1="20" x2="200" y2="168"/>
</svg>
<figcaption>Office of the Texas Governor (3 August 2026); ERCOT's Senate briefing (29 July 2026, preliminary) and its presentation to the Texas regulator (20 August 2026). The three figures are from different dates in the same summer.</figcaption>
</figure>

Then ERCOT paused even that last approval for data centres and crypto mines of 75 MW or more, while it audits every request. Under a seventieth of the queue reached the final gate, and the gate is shut while the audit runs; ERCOT aims to file its reports by 10 December 2026.

What Texas offers instead is a lower plug. A Provisional Controllable Load Resource connects early if ERCOT may reduce it "during periods of localized stress". A Withdrawal-Limited Private Use Network brings its own plant and takes only a capped amount from the grid. ERCOT is not clearing the queue. It is writing the terms on which most of it may connect.

## The regulator is pressing the same split on six grids

<a id="ferc-asks-for-a-softer-plug"></a>

The federal regulator is putting the same question to every organised grid it oversees. On 18 June 2026 FERC told six regional grid operators, PJM among them, to defend their rules for large loads or change them. PJM's tariff "appears to be unjust and unreasonable", it said, and it asked whether PJM could manage without an interim, non-firm service while network upgrades are built.

The grids are converging on a menu. Southwest Power Pool's lower tier, CHILLS, was accepted on 5 June: power as available, for up to seven years. On 9 October PJM's transmission owners told members that capacity "will not be procured" for interim customers until their upgrades are built. ISO New England and NYISO are designing non-firm services, and PJM files its answer in November 2026.

The firm plug is not getting faster. A cheaper one the grid may cut is being added beneath it, grid by grid.

## Households pay for the power stations that are not built

<a id="pjm-sends-the-bill"></a>

Where the plug is rationed, everyone else pays for the shortfall in power stations. PJM serves 67 million people across 13 states and Washington DC. Its capacity auction pays power stations to stand ready in a future year, and the last megawatt needed sets the price for all.

<figure class="chart">
<p class="chart-title">PJM's auction has sat at its price cap for three auctions running</p>
<p class="chart-sub">Price paid to power stations to stand ready, in dollars per megawatt of capacity per day, by delivery year</p>
<svg viewBox="0 0 560 336" role="img" aria-label="Bar chart of PJM capacity auction prices in dollars per megawatt-day by delivery year: 28.92 for 2024/25, 269.92 for 2025/26, then the cap in each of the next three years, 329.17 for 2026/27, 333.44 for 2027/28 and 325 for 2028/29. The 2027/28 auction fell about 6,500 megawatts short of the reliability requirement and the 2028/29 auction 6,831 megawatts short.">
<g class="c-grid"><line x1="60" y1="220" x2="540" y2="220"/><line x1="60" y1="170" x2="540" y2="170"/><line x1="60" y1="120" x2="540" y2="120"/><line x1="60" y1="70" x2="540" y2="70"/></g>
<g class="c-axis"><text x="52" y="274" text-anchor="end">0</text><text x="52" y="224" text-anchor="end">100</text><text x="52" y="174" text-anchor="end">200</text><text x="52" y="124" text-anchor="end">300</text><text x="52" y="74" text-anchor="end">400</text>
<text x="108" y="292" text-anchor="middle">2024/25</text>
<text x="204" y="292" text-anchor="middle">2025/26</text>
<text x="300" y="292" text-anchor="middle">2026/27</text>
<text x="396" y="292" text-anchor="middle">2027/28</text>
<text x="492" y="292" text-anchor="middle">2028/29</text>
</g>
<rect class="c-bar c-mute" x="80" y="255.5" width="56" height="14.5" rx="2"/>
<text class="c-lab c-s2t" x="108" y="247.5" text-anchor="middle">$28.92</text>
<rect class="c-bar c-mute" x="176" y="135" width="56" height="135" rx="2"/>
<text class="c-lab c-s2t" x="204" y="127" text-anchor="middle">$269.92</text>
<rect class="c-bar" x="272" y="105.4" width="56" height="164.6" rx="2"/>
<text class="c-lab c-s2t" x="300" y="97.4" text-anchor="middle">$329.17</text>
<rect class="c-bar" x="368" y="103.3" width="56" height="166.7" rx="2"/>
<text class="c-lab c-s2t" x="396" y="95.3" text-anchor="middle">$333.44</text>
<text class="c-note" x="396" y="312" text-anchor="middle">about 6,500</text><text class="c-note" x="396" y="327" text-anchor="middle">MW short</text>
<rect class="c-bar" x="464" y="107.5" width="56" height="162.5" rx="2"/>
<text class="c-lab c-s2t" x="492" y="99.5" text-anchor="middle">$325</text>
<text class="c-note" x="492" y="312" text-anchor="middle">6,831</text><text class="c-note" x="492" y="327" text-anchor="middle">MW short</text>
<text class="c-note" x="272" y="24">At the cap in each of the last three auctions</text>
<line class="c-base" x1="60" y1="270" x2="540" y2="270"/>
</svg>
<figcaption>PJM auction reports and releases (30 July 2024, 22 July 2025, December 2025, 14 July 2026). The cap differs slightly each year. Shortfalls are against PJM's own reliability requirement.</figcaption>
</figure>

The cap has not called up new plant. The 2028/2029 auction cleared only 525 MW of new plant and upgrades, against a shortfall of 6,831 MW. PJM's market monitor attributes $6.3 billion, 38.2% of that auction, to data centre load.

The tiers meet the bill here. PJM's interim tier buys no capacity for a site, so a site the grid may cut adds nothing to the auction until its upgrades land.

<a id="virginia-bills-the-empty-site"></a>

Virginia guards against the opposite risk, the site that never fills. Data centres took 28% of Dominion Energy's Virginia sales in 2025, and from January 2027 its largest customers sign 14 year terms with minimum bills, backed by collateral. Dominion's stated aim is "to minimize both cross-rate class subsidies and stranded costs". The floor protects households from the empty site, not the full one.

## The sites the grid cannot cut are leaving on their own

<a id="the-power-it-drops"></a>

The strongest evidence that rationing must run both ways is PJM's own account of one summer morning. At 07:56 on 22 July 2026 a fault on a 230 kV line in Dominion's zone cleared properly, with no relay misoperations. Still, about 3,800 MW of data centre load switched to backup generators.

The first wave of transfers raised the voltage, and the higher voltage set off a second. Frequency rose to 60.092 Hz, a sign the grid suddenly had more power than demand.

<figure class="chart">
<p class="chart-title">July's drop was the largest load transfer in PJM's history, and not its first</p>
<p class="chart-sub">Data centre load that switched to backup generation after a normally cleared fault, in megawatts</p>
<svg viewBox="0 0 560 290" role="img" aria-label="Bar chart of large load transfers to backup generation in PJM after grid faults: about 1,500 megawatts on 10 July 2024, about 1,500 megawatts on 17 February 2025 and about 3,800 megawatts on 22 July 2026, the largest in PJM history. A dashed line at 1,500 megawatts marks the size my claim says should not recur in 2028, after existing sites must ride through.">
<g class="c-grid"><line x1="70" y1="190" x2="540" y2="190"/><line x1="70" y1="140" x2="540" y2="140"/><line x1="70" y1="90" x2="540" y2="90"/><line x1="70" y1="40" x2="540" y2="40"/></g>
<g class="c-axis"><text x="62" y="244" text-anchor="end">0</text><text x="62" y="194" text-anchor="end">1,000</text><text x="62" y="144" text-anchor="end">2,000</text><text x="62" y="94" text-anchor="end">3,000</text><text x="62" y="44" text-anchor="end">4,000</text>
<text x="150.0" y="262" text-anchor="middle">10 Jul 2024</text>
<text x="290.0" y="262" text-anchor="middle">17 Feb 2025</text>
<text x="430.0" y="262" text-anchor="middle">22 Jul 2026</text>
</g>
<rect class="c-bar" x="110" y="165" width="80" height="75" rx="2"/>
<text class="c-lab c-s2t" x="150.0" y="157" text-anchor="middle">about 1,500 MW</text>
<rect class="c-bar" x="250" y="165" width="80" height="75" rx="2"/>
<text class="c-lab c-s2t" x="290.0" y="157" text-anchor="middle">about 1,500 MW</text>
<rect class="c-bar" x="390" y="50" width="80" height="190" rx="2"/>
<text class="c-lab c-s2t" x="430.0" y="42" text-anchor="middle">about 3,800 MW</text>
<line class="c-today" x1="70" y1="165" x2="540" y2="165"/>
<line class="c-base" x1="70" y1="240" x2="540" y2="240"/>
<text class="c-note" x="70" y="284">Dashed line: 1,500 MW, the size my test says must not recur in 2028</text>
</svg>
<figcaption>PJM's event review to its System Operations Subcommittee (31 July 2026) and Inside Lines (11 August 2026). PJM gives the earlier two events as about 1,500 MW each.</figcaption>
</figure>

The backup that protects each building is what threw the load at the grid. A data centre is built never to lose power, so at the first flicker it leaves. One site doing that protects its servers. A zone full of them doing it together moved more than seven times the new plant PJM's last auction added, in one morning, with no warning.

## So the grid will now decide when a site may leave

The fix is to make the building hold on, and the rule is being written. PJM proposed on 6 October that sites of 50 MW or more, with at least 25 MW behind power electronics, ride through set dips and swells. A site must stay on for a full second at up to 120% of normal voltage, the kind of swell that set off July's second wave.

Switching to backup power does not "by itself" count as compliance. New projects must comply from 16 January 2027, and existing sites by 16 January 2028, with limited exceptions where a site shows it cannot. ERCOT's own rule exempts sites approved before 14 November 2025.

The national rule is following. NERC's alert of 4 May 2026 "does not create a mandatory obligation", but FERC has ordered NERC to file binding standards by 31 December 2026. Rationing now has two halves: the grid decides whom it may cut, and forbids the rest to leave on their own.

## What backs a site up is now part of its connection

<a id="google-lets-the-grid-slow-its-chips"></a>

A site that may be cut, or must hold on, needs something to lean on, and the newest answer is the chip itself. By 19 March 2026 Google had deals with five utilities, covering 1 GW, to "limit or shift a portion" of its machine learning work at peak. At an Oracle site in Phoenix, software cut the power of 256 Nvidia chips by 25% for three hours, with no battery.

On 16 September Google, Nvidia and Emerald AI formed an alliance seeking faster connections for "credible, verifiable flexibility commitments". No public record yet shows a connection approved on a slowed chip.

<a id="what-the-battery-is-really-for"></a>
<a id="california-still-shifts-the-sun"></a>

Batteries were the obvious candidate, and the record says they are mostly doing something else. California's fleet earns about four times as much from shifting cheap midday power into the evening as from steadying the grid, and on its twelve hardest summer evenings of 2026, gas led every time. That is a time-shifter. Nobody publishes how many batteries sit at data centres, so they stay a line in this story, not a beat.

## What could leave the rationing on paper

The case against is that tiers can be written and never used. Developers want firm service, and CAISO's own proposal records that they "would only agree to be flexible temporarily". SPP's CHILLS has been accepted since June, yet no site is shown running on it. And nobody has published what riding through costs, so PJM's limited exceptions could swallow its rule.

Each objection is a reason to test use rather than paperwork, and the claim below does. It counts only a site of 50 MW or more actually switched on under a tier the grid may cut first, in at least two grids, by the end of 2027. Texas's power to shed every large load in an emergency does not count, because that is load shedding, not a tier.

For holding on, the test is the outcome. Another transfer of 1,500 MW or more in 2028, after existing sites were due to comply, would show the rule changed nothing on the ground.

## Nobody gets a bigger fuse sooner

Texas has more data centres asking than it can carry, and Virginia had data centres leaving that nobody asked to go. Both are answered by terms, not wires. The fuse box is still full and the electrician still booked, so the landlord now writes the tenancy: whose heater goes off first, who must not yank every plug at once, and who pays the bill meanwhile. For a data centre in America, the terms of the connection are now part of the product.

## Claims on record

The test this piece stands behind, quoted word for word from the claims page:

<a id="america-rations-the-plug"></a>

**America rations the plug** (30 October 2026)

Claim: "America is rationing the grid connection rather than speeding it up: by the end of 2027, data centres of 50 megawatts or more will be running on an early-connection tier the grid may cut first in at least two of its seven organised grids, and once PJM's ride-through deadline for existing sites passes, its data centres will stop dropping to backup power in blocks of 1,500 megawatts or more after normally cleared faults."

Breaks if: "By 31 December 2027, fewer than two of ERCOT, PJM, MISO, SPP, NYISO, ISO New England and CAISO have a load of 50 MW or more, mainly a data centre, actually energised under an early-connection tier the grid may cut first, such as ERCOT's Provisional Controllable Load Resource, SPP's CHILLS, PJM's Interim NITS or CAISO's flexible interim service, shown in a filed service agreement or the operator's own report; curtailment rights that apply to all large loads during emergency load shed, such as Texas Senate Bill 6, do not count. Or, between 16 January 2028 and 31 December 2028, PJM reports a transfer of 1,500 MW or more of large load to backup generation or off the grid after a normally cleared fault."

<details class="claims-earlier">
<summary>Two earlier claims on the plug and the battery, quoted word for word</summary>

**The grid's new problem is not the power AI uses, it is the power it drops** (22 September 2026)

Claim: "The grid's new problem with AI data centres is not the power they draw. It is the gigawatts they can drop in under a second."

Breaks if: "Ride-through turns out to be a cheap settings change rather than a constraint, or Virginia's 3.8 gigawatt trip proves to be a local fault rather than how these sites are built."

Where later evidence bears on it: the fault "cleared properly" and this was PJM's third such transfer in about two years, which supports the second limb. The first is open: nobody has published what compliance costs. Where I was wrong: the piece said NERC's alert "binds" planners and operators; NERC says it "does not create a mandatory obligation". Binding standards will come from NERC, which FERC ordered on 16 July to file them by 31 December 2026. PJM times the event to the minute, so "under a second" was my reading, not PJM's figure.

**The battery has quietly stopped being an energy product** (22 September 2026)

Claim: "Large batteries are increasingly bought as connection equipment that lets a site switch on early, not as a way to trade electricity."

Breaks if: "New storage stops clustering where computing load is and spreads out with renewable generation instead, or connection waits shorten enough that opening early stops being worth paying for."

Where later evidence bears on it: California's 17.3 GW fleet is a time-shifter, earning about four times as much from shifting energy as from balancing. My count of the 2026 summer narrows the claim to, at most, the newest buyers beside data centres. The Texas figure I relied on counts grid batteries, which also trade, and no one publishes the share at data centre sites. The nearest primary case, storage behind Google's Michigan site, is utility supply, not a connection condition.

</details>

## What would prove me wrong

The first test is use, not paperwork. If fewer than two grids have a real site of 50 MW or more on an early tier the grid may cut first by the end of 2027, the rationing is on paper only.

The second is whether holding on works. PJM's earlier transfers were about 1,500 MW each. If one that size recurs in 2028, after existing sites were due to comply, the rule did not change how the fleet behaves, however it was written.

## Research notes

No initiation note rests on these claims. The power a site brings itself is the subject of the notes on [GE Vernova](/research/ge-vernova/) and [Bloom Energy](/research/bloom-energy/). The protection and power gear inside the site are covered by [Vertiv](/research/vertiv/), [Schneider Electric](/research/schneider-electric/) and [Eaton](/research/eaton/), each resting on its own claim.

<details class="evidence">
<summary>The figures behind the charts</summary>

Every large American site now meets three questions: firm service or a tier the grid may cut, whether it must ride through faults, and who carries the wait.

| Grid | The cut-first tier | Must it ride through faults? | Who carries the wait |
|---|---|---|---|
| ERCOT (outside FERC) | Curtailable under local stress, or own generation with a capped draw (approved 18 June 2026) | Yes for new large computational loads; sites approved to energise, or with signed agreements, before 14 November 2025 exempt | New large loads can be cut in rotating outages (Senate Bill 6, 2025) |
| PJM | Interim service, non-firm until upgrades are built, no capacity bought (9 October 2026) | Proposed from 2027, existing sites included (6 October 2026) | Households, through the capacity auction |
| Southwest Power Pool | SPP's CHILLS: as available, up to seven years (accepted 5 June 2026) | Not shown | Not shown |
| MISO, NYISO, ISO New England, CAISO | Non-firm or interim flexible services in design (August 2026) | MISO drafting | Not yet filed |
| Dominion Energy, Virginia | None; firm, with a 14 year minimum bill from January 2027 | At least six automatic reclosing attempts | The customer if it never fills; shared if it does |

"Not shown" means I found no primary statement. ERCOT's and Dominion's ride-through terms are as PJM summarised them on 8 September 2026. MISO's and Southwest Power Pool's plans are known only from a counsel's summary (3 August 2026).

**Texas.** The 474 GW, five times the record peak and about 90% data centres are the Governor's (3 August 2026); ERCOT's own briefing gave 474 GW as of June. The 205 GW (preliminary), the 17 loads and 6,608 MW, the pause at 75 MW and the audit date are from ERCOT's documents of 29 July and 20 August 2026. Senate Bill 6 makes loads of 75 MW or more connected after 2025 curtailable in rotating outages, and lets ERCOT order large loads onto their backup generators in an emergency. Under a seventieth is 6.6 GW against 474 GW, my arithmetic.

**FERC.** The PJM show cause order (EL26-67, 18 June 2026) suggests a large load is a new site of 50 MW or more above 69 kV. CAISO's straw proposal is dated 11 August 2026.

**PJM's capacity auction.**

| Delivery year | Held | Result |
|---|---|---|
| 2025/2026 | July 2024 | $269.92 per MW-day, up from $28.92 |
| 2026/2027 | July 2025 | $329.17, the cap |
| 2027/2028 | December 2025 | $333.44, the cap; about 6,500 MW short |
| 2028/2029 | July 2026 | $325, the cap; $16.4 billion; 6,831 MW short of the reliability requirement; 525 MW of new plant and upgrades |

PJM's market monitor counts 21,470 MW of data centre load in the 2028/2029 forecast and attributes $6.3 billion, 38.2% of the latest auction, to it (27 July 2026). More than seven times is 3,800 MW against 525 MW, my arithmetic.

**Virginia.** Dominion's 10-K (23 February 2026) gives the 28% and defines its high load customers as 25 MW or more at a load factor of 75% or more; its 8-K (14 September 2026) names the class GS-5 and sets minimum payments for generation, transmission and distribution. Virginia's legislative auditor found shared generation and transmission are recovered over 20 to 40 years, far past a 14 year term, and estimated data centre growth could add $14 to $37 a month to a typical household's generation and transmission costs by 2040, in 2024 dollars (JLARC Report 598, 9 December 2024).

**The 22 July event.** PJM's deck gives about 3,800 MW, two stages, no relay misoperations and 60.092 Hz. Inside Lines calls it the largest load transfer in PJM's history, after transfers of about 1,500 MW on 10 July 2024 and 17 February 2025.

**PJM's ride-through proposal (6 October 2026).** It covers sites of 50 MW or more with at least 25 MW behind power electronics.

| Voltage, share of normal | Must stay connected for |
|---|---|
| Above 1.10, up to 1.20 | 1 second |
| 0.90 to 1.10 | Continuously |
| 0.80 to 0.90 | 2 seconds |
| 0.50 to 0.80 | 0.5 seconds |
| Below 0.50 | 0.25 seconds |

Frequency from 58.8 to 61.2 Hz must be ridden through continuously, and 57.0 to 58.8 Hz or 61.2 to 61.8 Hz for 299 seconds. Projects entering PJM's studies from 16 January 2027 must comply; existing sites by 16 January 2028, or a year after switching on. PJM targets a FERC filing in November. FERC's order to NERC (16 July 2026) asks for standards, with registry criteria, by 31 December 2026 and a workplan for more by 1 March 2027.

**Slower chips.** Google's first deals were announced on 4 August 2025. Indiana's regulator approved the first contract in April 2026 (Cause 46276), with credits and penalties; its size and delivery are confidential. The Phoenix trial is from Nature Energy (5 December 2025). DTE Energy says Google's 1 GW Van Buren Township load ramp is supported by up to 1,600 MW of renewables, 480 MW of storage and 350 MW of demand response (8-K, 28 September 2026); it does not say how much of the 350 MW the computing itself delivers.

**Batteries.** EIA reported on 20 February 2026 that developers planned 24 GW of utility-scale batteries in 2026, 12.9 GW or 53% of it in Texas; EIA counts grid batteries, and nobody publishes how many sit at data centres. From CAISO's five-minute fuel mix I counted the summer evenings, June to September, on which batteries were the largest source at the net peak, demand less wind and solar.

| Summer | Evenings batteries led, of 122 |
|---|---|
| 2023 | 0 |
| 2024 | 10 |
| 2025 | 52 |
| 2026 | 66 |

California's fleet was 17,307 MW at 30 September 2026. CAISO's market monitor finds batteries earned about $35 per kW-year from energy against $9 from regulation in 2025. In March 2025 PJM estimated a four-hour battery counted 94% against summer risk and 43% against winter risk, and named data centres as a main reason risk is moving to winter. Its binding ratings have run 50%, 58%, 59% and 57% for 2026/2027 to 2029/2030; its non-binding outlook falls to 42% for 2030/2031.

</details>

<section class="exposure">
<h3>Who is exposed if America rations the plug</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>Rules, grids and wires</dt>
<dd><span class="names">FERC</span>, <span class="names">NERC</span>, <span class="names">ERCOT</span> and <span class="names">PJM</span> set the terms. <span class="names">Dominion Energy</span>, <span class="names">Oncor</span> and <span class="names">American Electric Power</span> build the lines.</dd>
<dt>Backup on site</dt>
<dd><span class="names">GE Vernova</span> makes turbines, <span class="names">Caterpillar</span> generators, <span class="names">Bloom Energy</span> fuel cells and <span class="names">Tesla Energy</span> batteries.</dd>
<dt>Protection and slower chips</dt>
<dd><span class="names">Schneider Electric</span>, <span class="names">Eaton</span> and <span class="names">Vertiv</span> make switchgear and backup power. <span class="names">Emerald AI</span> makes software that slows AI work for <span class="names">Google</span> and others.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Developers counting on firm power from day one, and PJM households.</dd>
</dl>
</section>

---

<p class="sources">Sources: Office of the Texas Governor (3 August 2026); ERCOT Senate briefing (29 July 2026), regulator presentation (20 August 2026); PUCT (18 June 2026); Texas Senate Bill 6 (2025); FERC show cause orders (18 June 2026), abeyance orders (14 August 2026) and order to NERC (16 July 2026); PJM transmission owners (9 October 2026); NEPOOL counsel (3 August 2026); CAISO straw proposal (11 August 2026); PJM auction reports (30 July 2024 to 14 July 2026); Monitoring Analytics (27 July 2026); Dominion Energy 10-K (23 February 2026) and 8-K (14 September 2026); JLARC Report 598 (9 December 2024); PJM event review (31 July, 11 August 2026) and ride-through proposal (8 September, 6 October 2026); NERC Level 3 alert (4 May 2026); EIA (20 February 2026); CAISO fuel mix (my count), Key Statistics and market monitor (2026); PJM storage ratings (13 March 2025 to 19 August 2026); DTE Energy 8-K (28 September 2026); Google (4 August 2025, 19 March 2026); Indiana regulator, Cause 46276 (April 2026); Nature Energy (5 December 2025); Nvidia (16 September 2026). Leads: a YouTube review, "State of AI data centres 2026", and two videos by Leo Cui. Personal research, not investment advice.</p>
