---
title: "America rations the plug: who may be cut, who must hold on, who pays"
date: 2026-11-07T18:00:00+08:00
summary: "America cannot build grid wires as fast as data centres ask for them, so its grids are rationing the connection instead of speeding it up. Every grid is writing a cheaper plug the grid may cut first, though no data centre yet runs on one; sites must now hold on when the voltage dips, after 3,900 megawatts left Virginia's grid in one morning; and households still share the bill for the wait. Meanwhile signed gigawatts run far ahead of running ones: Dominion has about 54 gigawatts of data centres under contract and bills 4.8."
category: "Analysis"
format: "depth"
cover: "/covers/america-rations-the-plug.svg"
tags: ["grid", "power", "data-centres"]
draft: true
---

<a id="america-rations-the-plug"></a>
<a id="ercot-rations-the-plug"></a>

On 3 August 2026 the Governor of Texas said ERCOT, which runs most of the state's grid, was weighing over 474 gigawatts of requests to connect. That is more than five times the most power Texas has ever used at once, and about nine tenths of it is data centres.

Twelve days earlier, a fault on a power line in Dominion Energy's part of Virginia was cleared exactly as designed. Even so, about 3,900 megawatts of data centres switched themselves off the grid onto their own backup. And in September Dominion told PJM, the grid operator, that it had about 54 gigawatts of data centres under contract, against 4.8 gigawatts it actually bills.

That is the claim of this piece. America cannot build wires as fast as data centres ask for them, so it is rationing the connection rather than speeding it up: a firm plug for those who wait, a cheaper plug the grid may cut first for those who will not, and rules that make every site hold on when the grid wobbles. The gap between signed and running gigawatts is where the wait shows, and households still share the bill for it.

To see why, the piece follows the questions in order. How a data centre gets connected, which step takes longest, and how long the line is. What the grids are doing instead of speeding up, whether anyone runs on the cheaper plug yet, how many hours it would be cut, and what backs a site up when it is. Then why 3,900 megawatts left Virginia's grid in a morning, and what ride-through demands. Then who pays for the wait, how much of a household's bill that is, and what states make data centres pay. Finally, how much of the signed power is running, where the time goes, who holds the scarce thing, and what would prove me wrong.

<details class="analogy">
<summary>The analogy</summary>
<p>Picture a restaurant whose gas main is full, with the bigger one booked for years. A table with full service waits for the new main: that is firm service. Diners seated now on the terrace get their burners turned down first when the kitchen is slammed, and must bring a camping stove: that is the cut-first tier and its backup.</p>
<p>When the lights flicker, nobody may run for the door at once, because a stampede tips the room over: that is holding on. Meanwhile someone pays for gas bottles rented until the main is dug: that is the bill for the wait. And the bookings book is fuller than the dining room ever will be: that is the gap between signed and running.</p>
</details>

## How does a data centre get connected to the grid?

It applies to its local utility, waits while the utility and the grid operator study what the wires can carry, waits again while the upgrades are built, and only then switches on.

America has two connection queues, and the famous one is the wrong one. The queue for power stations, run by the grid operators under federal rules, is counted every year by Lawrence Berkeley National Laboratory. At the end of 2024 it held about 2,290 gigawatts of plants and batteries, with a median of 55 months from request to running. A data centre is not in that queue. It is a **load**, a user of power, and loads join by a different and less formal path.

The physical hook-up of a load is the local utility's job. In PJM, which runs the grid from Chicago to Virginia, "requests to physically interconnect loads are submitted to transmission owners", the utilities that own the lines, each with its own studies. PJM then checks the result across the whole region. The retail sale and the siting stay with the state. Texas works the same way, except that its grid operator, ERCOT, sits outside federal regulation, and the utility files each request into ERCOT's own process.

<!--FIG:path-->

Five steps follow. The developer applies with a site, a size in **megawatts (MW)**, a schedule for ramping up and a deposit. A megawatt is a million watts, the draw of about a thousand homes; a **gigawatt (GW)** is a thousand megawatts. The utility and the grid operator then study whether the wires can carry it: whether lines overheat, voltage sags or the network becomes unstable.

The study lists the **upgrades** the site needs: new or bigger lines, substations, transformers and breakers, with a contract saying who pays. The upgrades are built. Then the utility gives "approval to energise", and the site switches on and ramps up over months or years.

What the site gets at the end is **firm service**, the grid's promise to carry it at all times short of an emergency. To promise that, the grid must have both the wires to reach the site and enough power stations standing ready for its peak. Both are now short.

## Which step takes longest, and why can no rule hurry it?

Building the upgrades. Every other step is paperwork that a regulator can redraw in months; the upgrades are steel, copper and factory slots.

On 18 June 2026 FERC, the federal power regulator, said a study listing the upgrades, a cost estimate and a build time "should take no more than 60-90 days". The build is the long part. FERC's own record notes that a data centre "may only take 1-2 years to construct", while the lines and substations to serve it take longer. No official statistic counts how long a load waits from request to switch-on; nobody publishes one.

Six things keep the upgrades slow.

**Built to order.** Each large transformer is designed for the voltages of one substation, so none comes off a shelf. The grid businesses of Siemens Energy and Hitachi Energy hold about four and three years of signed work, as [the equipment queue](/journal/the-equipment-queue/) measures it.

**Craft, not a production line.** Winding, drying and high voltage testing take months per unit, by trained hands. No maker can add a shift the way a developer adds a rack of servers.

**Coupled studies.** Each request changes the grid the next one is studied on, so studies run in batches, and one request that drops out can force the rest to be studied again.

**Land and permits.** A new line crosses farms, counties and sometimes states, each on its own clock.

**Everyone at once.** Utilities, power stations and data centres want the same transformers and breakers in the same years.

**One network.** Lines are limited by heat, voltage and stability, so a site can overload a line miles away, and the upgrade list is rarely one item.

So a rule can make the queue fairer and its paperwork faster. It cannot make a transformer arrive sooner. That is why the grids are rationing.

## How long is the line?

Far longer than anything that will be built: the requests are counted in hundreds of gigawatts, and what reaches the last gate in single figures.

<!--FIG:texas-chart-->

Texas shows the funnel most clearly. ERCOT's 474 GW, as of June 2026, counts requests, not demand. On 29 July ERCOT told the state Senate that about 205 GW was eligible for its first batch study, a preliminary figure. By 20 August, 17 loads totalling 6,608 MW had cleared every check except the approval to energise. Then ERCOT paused that approval for data centres of 75 MW or more, while it audits every request at the Governor's order.

Under a seventieth of the list reached the last gate, and the gate is shut until the audit reports, due by 10 December 2026. The comparison in the headline also needs care. "Five times the record peak" divides requests by ERCOT's highest hour, 91.1 GW on 22 July 2026, so 474 GW is about 5.2 times. It does not mean Texas needs five grids.

Why do lists balloon? A developer that does not know which site will get power first files for several, and each request costs little to keep alive. Oncor, the largest wires company in Texas, alone held 795 requests at 30 September 2026, about 293 GW of them from data centres. Of those, ERCOT had classified about 24 GW as base load, including 10 GW already switched on, and 21 GW as studied load, all on condition that the audit confirms them. Oncor does not expect the final transmission plan for that batch until the autumn of 2027.

Outside Texas the numbers are signed agreements rather than requests, and still large. AEP, the utility across eleven states, signed 15 GW of new load in its third quarter and expects 84 GW of contracted load by 2031, counting only executed agreements. Dominion's 54 GW in Virginia is the subject of a later section.

## If the wires cannot be hurried, what are the grids doing instead?

Selling the connection in two grades: a firm plug that waits for the upgrades, and a cheaper one that switches on now on whatever spare capacity exists, and is cut first when the grid is tight.

The second grade is **non-firm** or **interim service**. The site connects before its upgrades are built and runs as long as the wires have room. When they do not, the grid turns it down before anyone with firm service. When the upgrades arrive it converts to firm. Every grid calls it something different: a Provisional Controllable Load Resource in Texas, CHILLS in the central states, Interim NITS in PJM.

<a id="ferc-asks-for-a-softer-plug"></a>

The push came from Washington. On 23 October 2025 the Energy Secretary used a rarely used power to send FERC a proposed rule on connecting large loads, starting at 20 MW, and asked for final action by 30 April 2026. FERC did not write a national rule. On 18 June 2026 it instead ordered six regional grid operators to defend their large-load rules or change them. It found that PJM's tariff, its rulebook, "appears to be unjust, unreasonable, or unduly discriminatory or preferential".

FERC asked each grid for four things: clear application and study rules, published upgrade costs with a standard agreement on who pays them, a service for loads willing to be cut, and rules for loads sited beside power stations. PJM and its utilities file their answers by 16 November 2026. The answers to those filings are due by 16 December.

The status of each grid's cheaper plug, at 7 November 2026:

| Grid | The cut-first or early tier | Status | Any data centre running on it? |
|---|---|---|---|
| ERCOT, Texas | Provisional Controllable Load Resource: may be reduced "during periods of localized stress" | Approved by the Texas regulator, 18 June 2026; ERCOT's systems may not run it before 2027 | None found |
| SPP, central states | CHILLS: power as available, for up to seven years | Accepted by FERC 5 June 2026, in force 1 July 2026 | None found; no signed agreement published |
| PJM, Chicago to Virginia | Interim NITS: "a temporary, non-firm transmission service" until upgrades are built | In force only for loads sited beside a power station; for all large loads, to be filed 16 November 2026 | None found |
| CAISO, California | Flexible interim connection, which the grid may remotely disconnect | Board approved 28 October 2026; filing by 16 November | None |
| NYISO, New York | Bring new capacity or accept non-firm service | Committee approved; filing in November or December | None |
| ISO New England | To be filed by 16 November; detailed rules in 2027 | Not filed | None |
| MISO, the Midwest | No cut-first tier; a fast track for loads that bring new power stations, filed 2 October 2026 | Awaiting FERC | None |

Each rule also draws its own line for what counts as large. Texas's Senate Bill 6 starts at 75 MW. FERC's draft definition is a new site of 50 MW or more connected above 69,000 volts, beside no power station. PJM's, accepted on 9 October, is 50 MW at a site, counting buildings within one mile as one and with no voltage test. A 60 MW site is a large load in PJM and not in Texas.

## Is any data centre actually running on a cut-first plug?

Not that any primary record shows. On 7 November 2026 I could find no data centre of 50 MW or more switched on under any of these tiers, in any of the seven grids.

The one tier in force for ordinary large loads is SPP's CHILLS, since 1 July 2026. Press readings of SPP's standard agreement say it requires the load to be backed by a power station already running, and no signed CHILLS agreement is public. If CHILLS's seven years run from each site's own switch-on, which is my reading of the order rather than its words, a site switching on under it now could still be cut first in 2033.

PJM's Interim NITS exists only for loads beside a power station, from FERC's orders of December 2025 and June 2026. PJM's notice of 9 October says capacity "will not be procured" for interim customers: they get the wires before their upgrades, but no power station is held ready for them. Texas's tier is approved in the rules but, on ERCOT's own planning, may not be built into its systems until 2027.

So the claim's test is still open, and the first readings come this month. By 31 December 2027 at least two of the seven grids must have a real data centre running on such a tier, shown in a filed agreement. Rules written do not count.

The strongest counter-evidence is PJM's own plan. Its utilities say PJM also intends a fourth service, Fractional NITS, "a firm service, based on available system capacity": firm power for part of a site now, the rest when the upgrades arrive. If developers take part of a site firm rather than all of it cut first, the cheaper plug may stay empty and the rationing happens by size, not by grade. That would still be rationing, but it would break my test.

Developers' reluctance is the other risk. California's grid operator recorded in August that developers "would only agree to be flexible temporarily". But the choice is a cut-first plug now or a firm one in years, and for chips that lose value every month, years is dearer. That is why the test counts sites switched on, not tiers written.

<a id="the-hours-a-cut-first-site-can-run"></a>
## How many hours a year would a cut-first site be cut?

Nobody publishes it, which is the gap an investor should notice. A cut-first megawatt is worth the hours it is allowed to run, and no tier states them.

The best estimate is academic. Duke University's Nicholas Institute calculated in February 2025 how much new load America's 22 largest grids could take without new power stations, if that load accepted cuts in the tightest hours. Its answer, as the institute and the trade press summarise it, runs from 76 GW to 126 GW.

<!--FIG:duke-chart-->

The cuts in that model are small and partial. At 0.5% of a year's energy, the new load is cut for about 177 hours a year, and in 88% of those hours at least half of it keeps running. A typical cut lasts about two hours. "Flexible" in that study means turning down for an afternoon a few dozen times a year, not switching off for weeks.

The real contracts are confidential. Indiana's regulator approved a contract in April 2026 under which Google's new site may be cut, but kept its size, its curtailment amounts and its performance in events confidential. A consumer advocate's witness said "the curtailment requirement represents only a small percentage of the facility's total load". SPP's CHILLS states no cap on the hours it may cut, as far as I found. Texas's Senate Bill 6 lets the grid cut every large load connected after 2025 in a rolling blackout, but that is emergency load shedding, not a tier, and my test does not count it.

So a cut-first site's capacity is not its megawatts but the hours it can live through. Until a filed agreement states them, any model that values a cut-first megawatt like a firm one is guessing.

## What keeps a site running when the grid cuts it?

Three things: its own generators, batteries, or chips that slow down. Each has its own limit, and the generators' limit is set by an air permit, not by the grid.

**Generators.** Almost every data centre already has diesel generators for outages. But under the federal air rule for emergency engines, running outside an emergency is capped at 100 hours a year for maintenance and testing, of which only 50 may earn money. Even those 50 count only when the local grid operator dispatches the engine to avert voltage collapse or overloaded lines.

On 24 June 2026 EPA, the federal environmental regulator, confirmed that a programme in which PJM itself dispatches engines locally meets those terms. So in PJM a site may, in principle, be paid to run its engines up to 50 hours a year. A cut beyond that, outside a declared emergency, needs engines permitted to run as power stations. Virginia is tightening, not loosening: from 1 July 2026 every new data centre generator needs controls equal to the strictest federal tier, Tier 4. Texas's Senate Bill 6 says its emergency backup orders do not authorise breaking any emissions limit.

So a site that leans on diesel to live through cuts may have a capacity set by an air permit that no grid filing mentions. Gas turbines, engines and fuel cells permitted to run as power plants avoid the cap, which is why [building your own power](/journal/building-your-own-power/) matters to this piece.

<a id="google-lets-the-grid-slow-its-chips"></a>

**Chips that slow.** By 19 March 2026 Google had deals with five utilities, covering 1 GW, under which it can "limit or shift a portion" of its machine learning work at peak. In Michigan, DTE Energy says Google's 1 GW site at Van Buren Township is supported by up to 1,600 MW of renewables, 480 MW of storage and 350 MW of demand response, without saying how much of that the computing delivers. Michigan's regulator approved the contracts on 1 October; the state's Attorney General has asked it to rehear them.

The engineering works in trials. At a Phoenix site of Oracle, the cloud provider, software cut the power of 256 chips from Nvidia, the AI chip designer, by 25% for three hours during peak hours, the trial's paper reports. In September 2026 Google, Nvidia and Emerald AI, which makes the software, formed the AI Energy Management Alliance with 18 others, to seek faster connections for flexibility that can be verified. No record yet shows a connection approved on a slowed chip.

<a id="what-the-battery-is-really-for"></a>
<a id="california-still-shifts-the-sun"></a>

**Batteries.** A large battery at a site could carry it through a cut. But the batteries America is building are mostly doing something else. California's fleet reached 17,285 MW at 31 October 2026, and its market monitor finds it earned about $35 per kilowatt a year from shifting energy, against $9 from steadying the grid. On my count of the summer evenings, batteries were the largest source at California's evening peak on 66 of 122 evenings in 2026, up from none in 2023. They move solar power into the evening. Nobody publishes how many sit at data centres.

PJM's own ratings say which backup it values more. In its capacity market a megawatt of **demand response**, load that agrees to be cut on call, counts for more than a megawatt of four-hour battery, and the gap is widening as PJM's risk moves to long winter nights.

<!--FIG:ratings-chart-->

## Why did 3,900 megawatts of data centres leave Virginia's grid in one morning?

Because every site did exactly what it was set to do, at the same moment. No equipment failed; the fault was in the sum.

<a id="the-power-it-drops"></a>

At 07:56 on 22 July 2026 a 230,000 volt line faulted in Dominion's zone after a mechanical failure. A **fault** is current rushing to the ground, through a failed part or a branch on a line. While it lasts, voltage sags across the whole area. Protection relays sensed it and opened breakers within hundredths of a second, and PJM found no relay misoperated and no breaker stuck. The grid did its job.

<!--FIG:ridethrough-->

Servers cannot tolerate even a short sag, so every data centre has a **UPS**, an uninterruptible power supply: batteries behind power electronics that take over the servers in milliseconds. Many sites also run a counting rule. A typical setting, NERC found, is three dips within one minute, after which the site moves to its generators and stays there until staff switch it back by hand. Lines that reclose automatically, trying again in case the fault was brief, add a dip each time.

Every site in the area sees the same dip at the same moment and follows similar settings, so thousands of megawatts leave together. On 22 July about 2,900 MW left at once. With that load gone and power stations still running, voltage rose to about 1.14 times normal, and the high voltage set off a second wave of about 1,000 MW a minute later. Frequency across the whole eastern grid rose to 60.092 hertz.

<!--FIG:events-chart-->

It was not the first time. On 10 July 2024 a failed lightning arrester gave six faults in 82 seconds on a line set to reclose three times at each end, and about 1,500 MW moved to backup, NERC's review found. All of the load was data centres, NERC said, and most of it did not return for hours. On 17 February 2025 another 230,000 volt fault moved about 1,800 MW, on PJM's latest count.

July's drop was about seven times the 525 MW of new power stations and upgrades PJM's last capacity auction added, with no warning. PJM caught it: the grid recovered within nine minutes, inside the 30 its standard allows. But operators then had to pull back generation and manage thousands of megawatts coming back. PJM notes that every such event so far has involved sites already running, not new ones.

## What is ride-through, and who now requires it?

**Ride-through** is a rule that a site must stay connected through a brief voltage or frequency disturbance, and keep drawing roughly what it drew before. Texas has one in force; PJM files its own on 16 November.

The UPS may still carry the servers inside the building. What changes is that the site must not open its breaker to the grid or jump to its generators. PJM's proposal covers sites of 50 MW or more with at least 25 MW behind power electronics. Below half of normal voltage a site must hold on for a quarter of a second, from half to 80% for half a second, and from 80% to 90% for two seconds. Between 90% and 110% it must never leave. After the dip it must return to 90% of its earlier draw within two seconds.

New projects would comply from 16 January 2027, and existing sites by the later of 16 January 2028 or a year after switching on. PJM may bring a site it sees as risky into line within 90 days, and allows "limited exceptions" where the requirements "cannot be met". Utilities inside PJM already set their own floors: Dominion asks sites to ride through at least six reclosing attempts.

Texas went first. ERCOT's ride-through rule for large computing loads, approved by the Texas regulator on 9 July 2026, has been in force since 1 August. Sites running or approved before 14 November 2025 are exempt, and its toughest band, half to 80% of voltage, is fully enforced from 1 January 2028.

The national standard is slower than headlines suggest. FERC ordered NERC, which writes the grid's reliability standards, to file standards for computing loads by 31 December 2026. NERC's first three passed their final ballot in October. But on PJM's reading they "will not address the minimum voltage or frequency ride-through"; they only collect data. A minimum is expected in a standard in 2027. NERC has also asked FERC to register sites of 50 MW or more at 100,000 volts or above as regulated entities, about 68 GW of computing load; comments close on 20 November.

There is a second reason to care. A large AI training job alternates between computing and exchanging results, so its power can swing by large amounts several times a second. Engineers at Microsoft, Nvidia and OpenAI warned in August 2025 that such swings could damage grid equipment if they match the grid's own frequencies. Nvidia's newest rack design stores energy in each power shelf and ramps load smoothly, and in one training run cut the peak drawn from the grid by 30%. PJM plans ramp-rate rules for 2027.

I concede that a standard is not behaviour, and nobody has published what compliance costs. A UPS that carries the load through a deep dip without jumping to generators may need more batteries or different settings. But July was settings acting together, not broken kit, and a rule that names the settings changes them. That is why my test counts transfers in 2028, not rules adopted.

## Who pays for the wait?

For now, everyone on the grid, through the auction that pays power stations to stand ready. In PJM that price has sat at its cap three times running.

<a id="pjm-sends-the-bill"></a>

PJM serves 67 million people. Its **capacity auction** pays power stations, per megawatt per day, to be available in a delivery year three years ahead. It buys readiness, not energy, like a team paying its bench whether or not it plays, and the last megawatt needed sets everyone's price. When data centres join the forecast, PJM must buy more readiness, and the price rises for every customer.

<!--FIG:auction-chart-->

The price jumped from $28.92 a megawatt per day for 2024/25 to $269.92 for 2025/26. Since then it has hit the cap, the most the auction is allowed to pay, three times running. The cap is a collar agreed by PJM and the states. FERC extended it in April 2026 to the auctions for 2028/29 and 2029/30. Without it, the 2028/29 auction would have cleared at about $554.72, as reported from PJM's figures.

The cap has not called up new plant. The 2028/29 auction, held in July 2026, fell 6,831 MW short of PJM's own reliability requirement and cleared only 525 MW of new plant and upgrades. A price cannot buy what factories have not built. The next auction, for 2029/30, runs in December 2026 with a cap of $337.83, the last under the collar.

The shortfall may be smaller than it looks. PJM's independent market monitor found by 21 September 2026 that 4,017 MW of the data centre load in PJM's forecast had been cancelled or delayed, about two fifths of the forecast increase. On its arithmetic that would cut the 2028/29 shortfall to 3,055 MW. The forecast counts the signed gigawatts this piece questions later, and some of them will not arrive.

## How much of a household's bill is that?

Less than the headlines imply. Capacity was about a sixth of PJM's wholesale cost in the first half of 2026; data centres' share of it added about a tenth to the cost of each megawatt-hour.

The market monitor attributes $6.3 billion, 38.2% of the 2028/29 auction, to data centre load, and $29.4 billion over the last four auctions. Those are large numbers. But the auction is only one part of what power costs.

<!--FIG:bill-chart-->

In the first half of 2026, PJM's total wholesale cost was $114.50 per megawatt-hour, 50% more than a year earlier. Energy, the power actually used, was 63.5% of it and rose 48%. Capacity tripled, to 17.1% of the total. The monitor puts the data centre effect on capacity at $11.11 per megawatt-hour, 9.7% of the wholesale cost.

What reaches a household depends on its state. In Pennsylvania, where retail prices follow wholesale costs, the regulator tied June 2026 rises of about 3% to 10% to PJM's capacity costs, as reported. Virginia's legislative auditor estimated in December 2024 that data centre growth could add $14 to $37 a month to a typical household's generation and transmission costs by 2040, in 2024 dollars.

## Can the bill be moved to the data centres?

PJM tried, and FERC said no to most of it. The bill can only move as far as the states, which set retail rates, decide.

<a id="ferc-keeps-the-bill-shared"></a>

On 27 July 2026 PJM's board decided that "existing consumers should not pay higher capacity costs caused by new Large Loads". It proposed that new sites of 50 MW or more that did not bring their own power stations would be cut first in a shortage, and would be dropped from the demand the auction buys for. On 9 October FERC accepted only PJM's definition of a large load and its register. It found the cut-first service appeared to be "an impermissible intrusion on retail rate regulation", and that PJM had not shown why new large loads differ from other growth. "States have a crucial role", it said, "by designating which retail customers must be curtailed".

<a id="the-bill-changes-address"></a>

The fight moved to a one-time purchase. On 29 September FERC accepted PJM's Reliability Backstop Procurement, to buy about 6,800 MW of new capacity on terms of up to 15 years, but suspended it to 28 February 2027 and set a hearing. In January the White House energy council and all 13 PJM governors had asked that its costs fall on utilities serving data centres that neither bring capacity nor agree to be cut. PJM refiled on 29 October, the trade press reported, aiming to launch on 1 March 2027 with costs assigned by large-load growth.

None of it is in force, and the December auction still counts firm data centre load. If the charge lands, households carry less of the wait. Either way, firm power gets dearer for a data centre, which pushes the next site towards the plug the grid may cut first.

## What do states make data centres pay?

Long contracts with minimum bills, so that a site which never fills still pays for its wires. They protect against the empty site, not against the shared auction.

<a id="virginia-bills-the-empty-site"></a>

Virginia's is the most detailed. On 25 November 2025 the State Corporation Commission set Dominion's new rate class, GS-5, for contracts signed from 1 January 2027:

| Term | Virginia's GS-5 |
|---|---|
| Who | 25 MW or more on one site, using at least 75% of its peak on average |
| Length | 14 years, with up to four to ramp up, at least 20% a year |
| Minimum bill | 85% of contracted demand for distribution and for transmission, 60% for generation |
| Left out | PJM capacity costs are excluded from the generation minimum |
| Collateral | $1.5m per megawatt, cut by up to 70% for good credit, released yearly |
| Leaving early | An exit fee equal to all remaining minimum charges |
| Shrinking | Up to 20% free, a further 30% if another customer takes it, each on 36 months' notice |

The fourth row matters. The minimum bill guarantees that a site pays for its wires if it never fills. It does not move the capacity auction, which stays shared across every customer in Dominion's zone.

Other states have done the same. AEP Ohio's data centre tariff of July 2025 sets a minimum of 85% of subscribed demand for up to 12 years. Georgia lets contracts for customers over 100 MW run 15 years. Indiana Michigan Power requires at least 12 years after a ramp, Oregon at least ten, and Texas makes every load of 75 MW or more pay at least $100,000 for its study, with security forfeited if it misses its milestones.

Minimum bills shrink the queue, which is the clearest evidence that much of it was never firm. In Ohio, AEP had more than 30 GW of interest before the tariff. Once it applied, 13 GW became formal requests, and 5.6 GW signed under the new terms, the trade press reported from AEP's letter to the regulator.

## Of all the gigawatts signed, how many are running?

A fraction. Signed power runs far ahead of power at work, at the utility and at the operator alike.

<a id="contracted-energised-running"></a>

An AI campus passes five stages, and each has its own figure. **Contracted**: land and the right to power are signed. **Built**: the shell, cooling plant and substation go up. **Energised**: the utility switches the connection on. **Delivered**: the finished, powered hall is handed to the tenant. **Running**, which operators call active: chips are installed and drawing power for paying work. Only the last stage earns.

Dominion's ladder of contracts shows the first stage in detail. An engineering letter pays Dominion to design the substation; a construction letter pays it to start building; an electric service agreement commits both sides.

<!--FIG:dominion-chart-->

As of July 2026 Dominion had about 54 GW of data centres under one of the three, of which 12 GW was under service agreements. In August its data centres' billing peak was 4.8 GW. Dominion's own planning assumes the average site takes five years to reach 63% of the power it contracted. Even the firmest contracts, the service agreements, are two and a half times what Dominion bills.

The operators show the same gap from the other side. CoreWeave, which rents out AI computing, reports both its contracted and its active power each quarter. At 30 June 2026 it had 3.7 GW contracted and 1.5 GW active, about 41%, up from 20% a year earlier.

<!--FIG:operators-chart-->

<a id="nebius-paid-for-what-is-switched-on"></a>

Nebius, another operator, expects 5 GW contracted by the end of 2026, against 800 MW to 1 GW connected. Its only active figure, about 170 MW at the end of 2025, is a year older. Nebius defines active power as "power being consumed by installed, operational IT equipment and available for revenue generation". Revenue follows that last stage: its US$17.4 billion agreement with Microsoft is "subject to the satisfaction of the deployment and availability of the GPU Services", with damages for late delivery.

The biggest signed pile is Oracle's. At 31 August 2026 it had US$288 billion of data centre leases signed but not yet started, beginning between late 2026 and 2029. Its customers pay when halls are delivered, not when leases are signed. So any model that sizes revenue or chip demand from contracted gigawatts runs early, by quarters or years.

## Where does the time go between signing and running?

Mostly before energised, in the stage the builder controls least. After that, the tenant sets the pace, and a tenant with chips ready can fill a hall within months.

<a id="power-first-chips-last"></a>

The order a builder commits in shows which stage binds. Jane Street, the trading firm that builds its own AI halls, buys power first. Its head of physical engineering, Dan Pontecorvo, said on Dwarkesh Patel's podcast on 21 May 2026 that generators, transformers and some liquid cooling kit can take more than a year. So the firm commits to a site early, holds slightly more power than it needs, and picks a chip once the building is nearly ready. It backed up only the core of its system rather than the whole site, and switched its chips on six months sooner. A training job restarts from its last saved point, so an outage costs hours, while waiting for a generator costs months.

<a id="abilene-switched-on-in-stages"></a>

The fastest case still arrived building by building. At Abilene, Texas, Crusoe, the campus builder, builds; Oracle leases the campus and runs the cloud inside; and OpenAI uses the computing. The campus has a 1.2 GW grid connection, with gas turbines on site, which Crusoe calls backup. Work on the first two buildings began in June 2024, and Crusoe says they were energised within a year.

<!--FIG:abilene-chart-->

The first racks of Nvidia's GB200 chips arrived in June 2025, and the first phase was running by 30 September. Oracle reported 42% of capacity handed to its customer by 10 June 2026, and six of eight buildings, 618 MW, by 10 September, as transcribed from its calls. The chips came with the power, so energised set the pace. Even so, more than two years passed between the start of work and three quarters of the campus handed over.

The tenants' own words have shifted. In November 2025 Microsoft's chief executive, Satya Nadella, said on a podcast that the problem was power and finished buildings: "you may actually have a bunch of chips sitting in inventory that I can't plug in". On 28 October 2026 its finance chief blamed something else: "some third-party capacity deliveries we expected in Q1 were delayed". Neither executive spoke of power on that call. A late hall is a late hall, whichever stage made it late.

## So who holds the scarce thing, and what should an investor watch?

Whoever controls a site's terms: firm or cut first, for how many hours, with what backup and what bill. Those terms sit in tariff filings and contracts, public and rarely read.

In most models a 300 MW site is a 300 MW site whatever its plug. Its value sits in the terms. A tenant paying for near-constant uptime needs firm power, or backup for every cut. A cut-first site carries that backup, or signs tenants whose work can pause, such as training runs that save their state and resume. Almost nobody discloses which plug they bought, and that is where I would look for a gap.

If the claim is right, four positions gain. **Backup that runs for hours**: gas turbines, engines and fuel cells permitted to run, and long batteries, because a cut-first site must live through its cuts. **Kit that holds on**: ride-through turns the UPS and switchgear into compliance equipment for every PJM site of 50 MW or more, a market made by rule whose cost nobody has published. **Load that can slow**: if a slowed chip is ever accepted as a connection term, the cheapest backup is software. **The makers of the upgrades**, whose queue is the reason for all of it.

The readings come quickly. On 12 November Nebius reports its connected power. On 16 November PJM, its utilities, CAISO and ISO New England file their large-load rules, and PJM its ride-through rule; SPP answers on 20 November. ERCOT's audit reports by 10 December, and PJM's 2029/30 auction runs in December. Oracle's December results are the next word on Abilene's last two buildings.

## What would prove me wrong

Three tests can break the claim. First, if by the end of 2027 fewer than two of the seven organised grids have a real data centre of 50 MW or more switched on under a cut-first tier, shown in a filed agreement, the rationing is on paper only. Texas's power to shed every large load in an emergency is load shedding, not a tier.

Second, if PJM reports another transfer of 1,500 MW or more after a normally cleared fault in 2028, after existing sites were due to comply, holding on changed nothing. Third, if makers add factories fast enough and PJM's new yearly process works, developers take firm service and the lower tier empties. A firm partial plug such as PJM's planned Fractional NITS taking the place of the cut-first one would point the same way.

The claim stands on two legs. The rules are written by FERC, ERCOT, PJM, the states and NERC, and they change month by month; the first two tests attack that leg. The wires are gated by physics, and no order from FERC shortens a winding; the third test attacks that leg, the one I hold most firmly.

The stages have tests of their own, from my earlier claims. At Abilene, if the campus is energised but Oracle has still not reported all eight buildings delivered by its March 2027 results, fitting out, not power, is setting the pace. At Nebius, if it connects at least 800 MW by the end of 2026 but has fewer than 800 MW active at 30 June 2027, its halls are waiting for chips, not power. And if transformer and generator lead times fall back to months while chips become the longest wait again, power first and chips last breaks.

What would not move me is the view that contracted gigawatts are fine because everything gets built eventually. Eventually is the whole trade: revenue, the payback on capital spending and chip demand all hang on the stage a megawatt has reached.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

**America rations the plug** (CLAIM_DATE)

Claim: "CLAIM_TEXT"

Breaks if: "BREAKS_TEXT"

EARLIER_CLAIMS

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

**The 22 July event.** PJM System Operations Subcommittee deck (31 July 2026) and Planning Committee deck (6 October 2026): about 2,900 MW and then about 1,000 MW "a minute later", about 3,900 MW in all (3,800 MW in PJM's July and August decks); 230 kV fault after a mechanical failure; no relay misoperations or stuck breakers; peak voltage about 1.138 per unit; Eastern Interconnection frequency 60.092 Hz; recovery within nine minutes against 30 allowed; "all observed CILR events have involved already operational facilities". NERC incident review, Considering Simultaneous Voltage-Sensitive Load Reductions (January 2025): 10 July 2024, about 1,500 MW, all of it data centre load, six faults in 82 seconds, fault durations of 42 to 66 milliseconds, a typical trigger of three disturbances within one minute, most load not returning for hours. PJM's 6 October deck gives the 17 February 2025 event as about 1,800 MW; earlier PJM material gave about 1,500 MW. Seven times is 3,900 MW against 525 MW, my arithmetic.

**Ride-through.** PJM Members Committee deck (28 October 2026) and Planning Committee deck (8 September 2026): large computational loads of 50 MW or more with at least 25 MW through power electronics; voltage: above 1.20 per unit may trip, 1.10 to 1.20 for one second, 0.90 to 1.10 continuously, 0.80 to 0.90 for two seconds, 0.50 to 0.80 for half a second, below 0.50 for a quarter of a second; frequency 58.8 to 61.2 Hz continuously, 57.0 to 58.8 and 61.2 to 61.8 Hz for 299 seconds; recovery to 90% of prior power within two seconds; new projects from 16 January 2027, existing sites by the later of 16 January 2028 or a year after commercial operation; acceleration to 90 days; "limited exceptions when demonstrated that requirements cannot be met"; FERC filing 16 November 2026; ramp-rate filing in the second quarter of 2027. Dominion's floor of six reclosing attempts, as PJM summarised it (8 September 2026). ERCOT NOGRR 282: approved by the Texas regulator 9 July 2026, effective 1 August 2026; sites operational, approved to energise or with signed agreements on or before 14 November 2025 exempt; the 0.5 to 0.8 per unit band fully enforced from 1 January 2028. FERC order RD26-7-000 (16 July 2026). NERC Project 2026-02, final ballot announced 15 October 2026; PJM's deck of 31 July 2026: phase one "will not address the minimum voltage or frequency ride-through"; a minimum "expected to become part of a Reliability Standard in 2027". NERC registry petition (21 October 2026): 50 MW at 100 kV, about 68 GW (law-firm summary). Choukse and others, on power stabilisation for AI training sites, arXiv 2508.14318 (August 2025). Nvidia technical blog on the GB300 NVL72 power shelf (28 July 2025): 65 joules per GPU, peak grid demand cut 30% in a training run.

**PJM's capacity auction.**

| Delivery year | Held | Result |
|---|---|---|
| 2024/25 | December 2022 | $28.92 per MW-day |
| 2025/26 | July 2024 | $269.92 |
| 2026/27 | July 2025 | $329.17, the cap |
| 2027/28 | December 2025 | $333.44, the cap; 6,623 MW short of the reliability requirement, counting capacity utilities supply outside the auction (FERC, 29 September 2026) |
| 2028/29 | July 2026 | $325, the cap; $16.4 billion; 6,831 MW short; 525 MW of new plant and upgrades |
| 2029/30 | December 2026 | cap $337.83, floor $181.91; requirement 158,712 MW |

PJM releases and auction reports; the 2029/30 parameters are from PJM's planning period parameters report (posted 31 August 2026). The uncapped 2028/29 price of $554.72 is from the American Public Power Association's report of PJM's figures; it is not in PJM's release. FERC accepted the collar's extension (ER26-1556, 28 April 2026, law-firm summary). The 4,017 MW of cancelled or delayed data centre load and the 3,055 MW shortfall are the market monitor's, as FERC recounted them in its order of 29 September 2026 (ER26-3380).

**The household bill.** Monitoring Analytics, the PJM market monitor, report to the Members Committee (27 July 2026): data centre load $6.3 billion, 38.2% of the 2028/29 auction; $29.4 billion over the four auctions from 2025/26; total wholesale cost $114.50 per MWh in the first half of 2026 against $76.16 a year earlier, up 50.3%; energy up 47.7% and 63.5% of the total; capacity up 207.1% and 17.1%; transmission up 5.6% and 17.4%; data centre capacity effect $11.11 per MWh, 9.7%. The chart's split into parts is my arithmetic from those shares and growth rates. Pennsylvania Public Utility Commission (20 May 2026), as reported. Virginia Joint Legislative Audit and Review Commission, Report 598 (9 December 2024).

**Moving the bill.** PJM Board decision (Inside Lines, 27 July 2026). FERC ER26-3515 (9 October 2026), paragraphs 77, 94 and 95. FERC ER26-3380 (29 September 2026): backstop accepted, suspended to 28 February 2027, subject to refund, paper hearing. White House and governors' Statement of Principles (16 January 2026, law-firm summary). PJM's amended backstop filing (29 October 2026) is from trade press: bids from 1 March 2027, terms of up to 15 years, a target of about 6,800 MW to be recalculated, costs by large-load growth.

**The states.** Virginia State Corporation Commission, final order, Case PUR-2025-00058 (25 November 2025), pages 23 to 27, Rate Schedule GS-5. AEP Ohio data centre tariff, PUCO Case 24-508-EL-ATA (9 July 2025); terms from trade press. Georgia Public Service Commission (23 January 2025). Indiana Michigan Power settlement (approved February 2025, trade press). Oregon POWER Act (2025). Texas Senate Bill 6, PURA 37.0561, and the Texas regulator's large-load rule (adopted September 2026, trade press). AEP Ohio queue: more than 30 GW of interest, 13,022.7 MW of formal requests and 5,642 MW signed under the tariff, from AEP's letter to PUCO of 12 February 2026 as reported by New Project Media.

**Signed against running.** Dominion Energy to PJM's Load Analysis Subcommittee (29 September 2026): contracts as of July 2026 of 32,473 MW under engineering letters of authorisation, 9,356 MW under construction letters and 11,997 MW under electric service agreements; data centre billing peak load of 4.8 GW as of August 2026; "industry average ramp period is 5 years maturing at a utilization rate of 63%". CoreWeave earnings releases: about 590 MW active and 2.9 GW contracted at 30 September 2025; 1.5 GW and about 3.7 GW at 30 June 2026 (11 August 2026). Nebius shareholder letters (12 February, 13 May and 12 August 2026): 5 GW contracted target and 800 MW to 1 GW connected guide for the end of 2026; about 170 MW active at the end of 2025; the Microsoft agreement. Oracle Form 10-Q (11 September 2026): US$288 billion of lease commitments not yet commenced, substantially all for data centres, in its words, commencing from the second quarter of fiscal 2027 to fiscal 2029. Percentages and ratios are my arithmetic.

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

<p class="sources">Sources: FERC orders EL26-67 (18 June 2026), ER26-3380 (29 September 2026) and ER26-3515 (9 October 2026); PJM decks to its committees (31 July, 8 September, 6 and 28 October 2026), auction reports and the market monitor's report (27 July 2026); ERCOT and the Texas Governor (July and August 2026); NERC's incident review (January 2025); the Virginia State Corporation Commission's GS-5 order (25 November 2025); Dominion to PJM (29 September 2026); Oncor, AEP, CoreWeave, Nebius and Oracle filings; Duke University (February 2025). Trade press only where marked. Personal research, not investment advice.</p>
