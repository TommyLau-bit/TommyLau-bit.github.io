---
title: "America rations the plug: who can be cut, and what backs them up"
date: 2026-09-22T18:53:00+08:00
updated: 2026-10-30T14:20:52+08:00
updateNote: "Rewritten on 30 October 2026 as one deep piece, bringing together 2 earlier pieces, with a new section for investors."
summary: "America's grids cannot build wires as fast as data centres arrive, so they are rationing the connection instead. Texas and the federal regulator are splitting it into a full connection that waits for new lines and a cheaper one the grid can cut first, while households pay for the shortfall. The same data centres must now stay on when the grid wobbles and come off when it asks, so what backs them up, generators, batteries or slower chips, has become part of the connection."
category: "Analysis"
cover: "/covers/america-rations-the-plug.svg"
tags: ["grid", "power", "data-centres"]
draft: false
---

On 3 August 2026 the Governor of Texas said ERCOT, which runs most of the state's grid, was considering over 474 gigawatts of requests to connect. That is more than five times the most power Texas has ever used at once, and about 90 per cent of it is data centres.

Twelve days earlier, a fault on a line in Dominion Energy's part of Virginia cleared exactly as designed. Even so, about 3,800 megawatts of data centres switched themselves to backup power.

One grid has too many data centres asking to come on. The other has data centres that leave when nobody asked them to.

America is not speeding up the plug. It is rationing it.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture a block of flats whose fuse box is full, with the electrician booked for years. The landlord still lets new tenants in, on terms: your heater goes off first when the fuse runs hot, or you bring a camping stove.</p>
<p>And when a bulb flickers, you may not yank every plug at once. Nobody gets a bigger fuse sooner. The landlord only decides who goes dark first.</p>
</details>

## How it works

A firm connection is the grid's promise to carry a site's power at all times, short of an emergency. Before giving one, the operator lists the network upgrades it needs: new lines, substations and transformers.

Those take years. Transformers alone [wait years in the makers' queues](/journal/the-equipment-queue/#siemens-energy-measures-the-shortage). A data centre shell goes up far faster.

So grids are selling the plug in tiers. The full tier still waits for the wires. A lower tier switches on sooner but can be cut first when lines are strained, or comes on only if the site brings its own power.

Rationing comes with a second duty that points the other way. A site must ride through a disturbance, staying connected through a brief dip rather than fleeing to its generators. The grid wants it to stay on when the grid wobbles, and to come off only when the grid asks.

That makes what backs the site up part of the connection. It can be a generator, a battery, or software that slows its chips.

Someone pays for the wait. Where power stations cannot be built in time, the shortfall reaches household bills.

## The number that matters

In July 2026 PJM, the grid from Chicago to Virginia, ran its auction for power stations to stand ready in 2028. It fell 6,831 megawatts short of PJM's own reliability target. New plants and upgrades added only 525 megawatts.

In Texas, ERCOT stopped approving large data centres to switch on while it audits every request. In June, federal regulators told six regional grid operators, PJM among them, to justify or fix their rules for large loads.

A megawatt the grid can cut is not the same product as a firm one. The rationing is in which one you get.

<hr class="layer">
<p class="layer-label">For investors</p>

## The mechanism in depth

Every large American site now meets three questions: firm service or a tier the grid may cut, whether it must ride through faults, and who carries the wait.

| Grid | The cut-first tier | Must it ride through faults? | Who carries the wait |
|---|---|---|---|
| ERCOT (outside FERC) | Curtailable under local stress, or own generation with a capped draw (approved 18 June 2026) | Yes for new large computational loads; sites approved to energise, or with signed agreements, before 14 November 2025 exempt | New large loads can be cut in rotating outages (Senate Bill 6, 2025) |
| PJM | Interim service, non-firm until upgrades are built, no capacity bought (9 October 2026) | Proposed from 2027, existing sites included (6 October 2026) | Households, through the capacity auction |
| Southwest Power Pool | SPP's CHILLS: as available, up to seven years (accepted 5 June 2026) | Not shown | Not shown |
| MISO, NYISO, ISO New England, CAISO | Non-firm or interim flexible services in design (August 2026) | MISO drafting | Not yet filed |
| Dominion Energy, Virginia | None; firm, with a 14 year minimum bill from January 2027 | At least six automatic reclosing attempts | The customer if it never fills; shared if it does |

"Not shown" means I found no primary statement. ERCOT's and Dominion's ride-through terms are as PJM summarised them on 8 September 2026.

<a id="ercot-rations-the-plug"></a>
## ERCOT: a queue five times the peak, rationed at the door

The headline figures are the Governor's, of 3 August 2026: over 474 GW of requests, more than five times ERCOT's record peak, about 90% from data centres. He ordered an audit of every data centre in the queue before any project moves forward.

The rest are from ERCOT's own documents, each consistent with the Governor's release or a second report. On 29 July ERCOT told the Senate that only about 205 GW had the studies to enter Batch Zero, its first batch. On 20 August it told the regulator that 17 large loads, 6,608 MW, had cleared every check except approval to energise. It paused that approval for data centres and crypto mines of 75 MW or more, and aims to file its audit reports by 10 December 2026.

A Provisional Controllable Load Resource connects early if ERCOT may reduce it "during periods of localized stress". A Withdrawal-Limited Private Use Network brings its own plant and takes a capped amount from the grid. Beneath both, Senate Bill 6 makes loads of 75 MW or more connected after 2025 curtailable in rotating outages, and lets ERCOT order large loads onto their backup generators in an emergency.

**ERCOT is not clearing the queue. It is writing the terms on which most of it may connect.**

<a id="ferc-asks-for-a-softer-plug"></a>
## FERC: the same split, written into six tariffs

On 18 June 2026 FERC sent show cause orders, which tell an operator to defend its rules or change them, to PJM, MISO, Southwest Power Pool, NYISO, ISO New England and CAISO. PJM's tariff "appears to be unjust and unreasonable", it said. The PJM order suggests a large load is a new site of 50 MW or more above 69 kV, and asks whether PJM can do without "an interim non-firm network transmission service while Network Upgrades are being constructed".

The answers converge on a menu. Southwest Power Pool's lower tier was accepted on 5 June. PJM's transmission owners told members on 9 October that capacity "will not be procured" for interim customers until their upgrades are built. ISO New England and NYISO are designing non-firm services; MISO's and Southwest Power Pool's plans are known only from a counsel's summary. PJM and its transmission owners file in November 2026.

CAISO's straw proposal of 11 August 2026 adds that developers "would only agree to be flexible temporarily".

**The firm plug is not getting faster. A cheaper, cuttable one is being added beneath it.**

<a id="pjm-sends-the-bill"></a>
## PJM: the auction that sends the bill

PJM serves 67 million people across 13 states and Washington DC. Its capacity auction pays power stations to stand ready in a future year. The last megawatt needed sets the price for all.

| Delivery year | Held | Result |
|---|---|---|
| 2025/2026 | July 2024 | $269.92 per MW-day, up from $28.92 |
| 2026/2027 | July 2025 | $329.17, the cap |
| 2027/2028 | December 2025 | $333.44, the cap; about 6,500 MW short |
| 2028/2029 | July 2026 | $325, the cap; $16.4 billion; 6,831 MW short of the reliability requirement; 525 MW of new plant and upgrades |

PJM's market monitor counts 21,470 MW of data centre load in the 2028/2029 forecast and attributes $6.3 billion, 38.2% of the latest auction, to it (27 July 2026).

Here the tiers meet the bill. PJM's interim tier buys no capacity, so a cuttable site adds nothing to the auction until its upgrades land.

<a id="virginia-bills-the-empty-site"></a>
## Virginia: a floor under the empty site

Data centres took 28% of Dominion Energy's Virginia electricity sales in 2025 (10-K, 23 February 2026), and from January 2027 its high load customers, 25 MW or more at a load factor of 75% or more, sign 14 year terms with minimum payments for generation, transmission and distribution, backed by collateral, in a class it calls GS-5 (8-K, 14 September 2026). Dominion's stated purpose is "to minimize both cross-rate class subsidies and stranded costs", so the floor insures against the empty site, not the full one. Virginia's legislative auditor found shared generation and transmission are recovered over 20 to 40 years, far past a 14 year term, and estimated data centre growth could add $14 to $37 a month to a typical household's generation and transmission costs by 2040, in 2024 dollars (JLARC Report 598, 9 December 2024).

<a id="the-power-it-drops"></a>
## The power it drops: why the plug must also hold

PJM's account is precise. At 07:56 on 22 July 2026 a fault on a 230 kV line in Dominion's zone cleared properly, with no relay misoperations. About 3,800 MW of load still transferred to backup generation: the first transfer raised voltage, which triggered more. Frequency rose to 60.092 Hz. It was PJM's largest load transfer; others of about 1,500 MW came on 10 July 2024 and 17 February 2025.

NERC's Level 3 alert of 4 May 2026 demanded acknowledgement and a report, but "does not create a mandatory obligation". Binding standards are coming: FERC ordered NERC on 16 July to file them, with registry criteria, by 31 December 2026, and a workplan for more by 1 March 2027.

PJM's proposal of 6 October covers sites of 50 MW or more with at least 25 MW behind power electronics.

| Voltage, share of normal | Must stay connected for |
|---|---|
| Above 1.10, up to 1.20 | 1 second |
| 0.90 to 1.10 | Continuously |
| 0.80 to 0.90 | 2 seconds |
| 0.50 to 0.80 | 0.5 seconds |
| Below 0.50 | 0.25 seconds |

Frequency from 58.8 to 61.2 Hz must be ridden through continuously, and 57.0 to 58.8 Hz or 61.2 to 61.8 Hz for 299 seconds. The high-voltage row matters, because high voltage set off the second wave on 22 July. Switching to backup power does not "by itself" count as compliance; the site must ride through. Projects entering PJM's studies from 16 January 2027 must comply; existing sites by 16 January 2028, or a year after switching on, with limited exceptions where a site shows it cannot. PJM targets a FERC filing in November. ERCOT's rule exempts sites approved to energise, or with signed agreements, before 14 November 2025.

**The backup that protects the building is what threw 3.8 GW at the grid. The fix is to make the building hold on.**

<a id="what-the-battery-is-really-for"></a>
<a id="california-still-shifts-the-sun"></a>
## What backs them up: batteries, and the case against my claim

EIA reported on 20 February 2026 that developers planned 24 GW of utility-scale batteries in 2026, 12.9 GW or 53% of it in Texas. I read that as storage following computing load, but EIA counts grid batteries, and nobody publishes how many sit at data centres.

California is the honest test. From CAISO's five-minute fuel mix I counted the summer evenings, June to September, on which batteries were the largest source at the net peak, demand less wind and solar.

| Summer | Evenings batteries led, of 122 |
|---|---|
| 2023 | 0 |
| 2024 | 10 |
| 2025 | 52 |
| 2026 | 66 |

On the twelve hardest evenings of 2026, gas led every time. The fleet, 17,307 MW at 30 September, did its usual work and the extra demand fell to gas. CAISO's market monitor finds batteries earned about $35 per kW-year from energy against $9 from regulation in 2025. That is a time-shifter.

A battery's worth depends on when risky hours fall. In March 2025 PJM estimated a four-hour battery counted 94% against summer risk and 43% against winter risk, and named data centres as a main reason risk is moving to winter. Its binding ratings have run 50%, 58%, 59% and 57% for 2026/2027 to 2029/2030; its non-binding outlook falls to 42% for 2030/2031.

At data centres the evidence is thin: DTE Energy says Google's 1 GW Van Buren Township load ramp is supported by up to 1,600 MW of renewables, 480 MW of storage and 350 MW of demand response (8-K, 28 September 2026). That is storage behind a data centre, bought by the utility as supply. Google's March 2026 post counts DTE among its contracts to limit or shift machine learning work.

<a id="google-lets-the-grid-slow-its-chips"></a>
## The chip as the backup: Google's slower plug

Google's first such deals were announced on 4 August 2025. By 19 March 2026 they covered 1 GW across five utilities, each able to have Google "limit or shift a portion" of its machine learning work at peak. Indiana's regulator approved the first contract in April 2026 (Cause 46276), with credits and penalties; its size and delivery are confidential.

At an Oracle site in Phoenix, software cut the power of 256 Nvidia chips by 25% for three hours at peak, with no battery (Nature Energy, 5 December 2025). On 16 September 2026 Google, Nvidia and Emerald AI formed an alliance seeking faster connections for "credible, verifiable flexibility commitments".

No public record yet shows a connection approved on a slowed chip. DTE's filing does not say how much of its 350 MW the computing itself delivers.

## Claims on record

Quoted word for word from the claims page, with the date each piece went live.

**The grid's new problem is not the power AI uses, it is the power it drops** (22 September 2026)

Claim: "The grid's new problem with AI data centres is not the power they draw. It is the gigawatts they can drop in under a second."

Breaks if: "Ride-through turns out to be a cheap settings change rather than a constraint, or Virginia's 3.8 gigawatt trip proves to be a local fault rather than how these sites are built."

Where later evidence bears on it: the fault "cleared properly" and this was PJM's third such transfer in about two years, which supports the second limb. The first is open: nobody has published what compliance costs. Where I was wrong: the piece said NERC's alert "binds" planners and operators; NERC says it "does not create a mandatory obligation". Binding standards will come from NERC, which FERC ordered on 16 July to file them by 31 December 2026. PJM times the event to the minute, so "under a second" was my reading, not PJM's figure.

**The battery has quietly stopped being an energy product** (22 September 2026)

Claim: "Large batteries are increasingly bought as connection equipment that lets a site switch on early, not as a way to trade electricity."

Breaks if: "New storage stops clustering where computing load is and spreads out with renewable generation instead, or connection waits shorten enough that opening early stops being worth paying for."

Where later evidence bears on it: California's 17.3 GW fleet is a time-shifter, earning about four times as much from shifting energy as from balancing. My count of the 2026 summer narrows the claim to, at most, the newest buyers beside data centres. The Texas figure I relied on counts grid batteries, which also trade, and no one publishes the share at data centre sites. The nearest primary case, storage behind Google's Michigan site, is utility supply, not a connection condition.

<a id="america-rations-the-plug"></a>

**New: America rations the plug** (30 October 2026)

Claim: "America is rationing the grid connection rather than speeding it up: by the end of 2027, data centres of 50 megawatts or more will be running on an early-connection tier the grid may cut first in at least two of its seven organised grids, and once PJM's ride-through deadline for existing sites passes, its data centres will stop dropping to backup power in blocks of 1,500 megawatts or more after normally cleared faults."

Breaks if: "By 31 December 2027, fewer than two of ERCOT, PJM, MISO, SPP, NYISO, ISO New England and CAISO have a load of 50 MW or more, mainly a data centre, actually energised under an early-connection tier the grid may cut first, such as ERCOT's Provisional Controllable Load Resource, SPP's CHILLS, PJM's Interim NITS or CAISO's flexible interim service, shown in a filed service agreement or the operator's own report; curtailment rights that apply to all large loads during emergency load shed, such as Texas Senate Bill 6, do not count. Or, between 16 January 2028 and 31 December 2028, PJM reports a transfer of 1,500 MW or more of large load to backup generation or off the grid after a normally cleared fault."

## What would prove me wrong

The first test is use, not paperwork. Developers want firm service, so early-connection tiers could sit on every tariff and stay empty. If fewer than two grids have a real site of 50 MW or more on one by the end of 2027, the rationing is on paper only. Texas's power to shed every large load in an emergency does not count: that is load shed, not a tier.

The second is whether the duty to hold on works. PJM's earlier transfers were about 1,500 MW each. If one that size recurs in 2028, after existing sites were due to comply, the rule did not change how the fleet behaves, however it was written.

## Research notes

No initiation note rests on these claims. The power a site brings itself is the subject of the notes on [GE Vernova](/research/ge-vernova/) and [Bloom Energy](/research/bloom-energy/). The protection and power gear inside the site are covered by [Vertiv](/research/vertiv/), [Schneider Electric](/research/schneider-electric/) and [Eaton](/research/eaton/), each resting on its own claim.

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

<p class="sources">Sources: Office of the Texas Governor (3 August 2026); ERCOT's Senate briefing (29 July 2026), regulator presentation (20 August 2026) and board materials (13 April and 11 September 2026); PUCT approval of Batch Zero (18 June 2026); Texas Senate Bill 6 (2025); FERC's show cause orders (18 June 2026), abeyance orders (14 August 2026) and order to NERC (16 July 2026); the PJM transmission owners' notice (9 October 2026); ISO New England's abeyance motion and the NEPOOL counsel memorandum (3 August 2026); CAISO's large loads straw proposal (11 August 2026); PJM auction reports and releases (30 July 2024, 22 July 2025, December 2025, 14 July 2026); Monitoring Analytics (27 July 2026); Dominion Energy's 10-K (23 February 2026) and 8-K (14 September 2026); JLARC Report 598 (9 December 2024); PJM's event review (31 July and 11 August 2026) and ride-through proposal (8 September and 6 October 2026); NERC's Level 3 alert (4 May 2026); EIA (20 February 2026); CAISO's fuel mix, my own count, Key Statistics (September 2026) and market monitor (June 2026); PJM's storage ratings (13 March 2025 to 19 August 2026); DTE Energy's 8-K (28 September 2026); Google (4 August 2025, 19 March 2026); the Indiana Utility Regulatory Commission, Cause 46276 (April 2026); Nature Energy (5 December 2025); Nvidia (16 September 2026). Leads came from a third-party YouTube review, "State of AI data centres 2026" (data to 5 October 2026), and two YouTube videos by Leo Cui, on Nvidia and Google's "dimmer switch" for AI data centres and on the energy sector explained. Personal research, not investment advice.</p>
