---
title: "Nuclear for AI: the old reactors come first because they already own the hard parts"
date: 2026-11-07T16:40:12+08:00
summary: "AI companies want nuclear power because it runs almost every hour of the year without carbon, and in America it arrives in the order of what each project already holds. Restarted and upgraded reactors already have a licensed site, a place on the grid and ordinary fuel, so they deliver this decade. The new reactors have permits and buyers, but most need a richer fuel made on one demonstration line, so they wait."
category: "Analysis"
format: "depth"
cover: "/covers/nuclear-for-ai.svg"
tags: ["power", "nuclear", "grid", "supply-chain"]
draft: true
---

<a id="nuclear-for-ai"></a>

The earliest new nuclear power that Microsoft has bought for AI will come from a reactor that shut in 2019. Constellation, America's largest nuclear plant owner, is bringing the former Three Mile Island Unit 1 in Pennsylvania back to life, renamed Crane, and says it will run again in the second half of 2027.

Meanwhile the new reactors have nearly everything a press release needs. TerraPower, the reactor company founded by Bill Gates, has a construction permit in Wyoming. Oklo, a start-up that plans to sell power from its own small reactors, has broken ground in Idaho and signed Meta. Kairos Power, a California reactor developer, has a utility contract to sell power for Google. Yet on their own dates, none of them will send meaningful power to an American grid before the 835 megawatts of a reactor built in the 1970s.

That is the claim of this piece. Nuclear power for AI arrives in the order of what each project already holds, not in the order of how advanced its reactor is. A restart or an upgrade of an existing reactor keeps a licensed site, a place on the grid and ordinary fuel. Most new designs need a richer fuel that America makes on one small demonstration line, so they wait.

To see why, the piece follows the questions in order. Why AI companies want nuclear at all, and what "new" nuclear power can mean. What every project needs before it can sell a kilowatt-hour. How a closed reactor comes back, why Crane had to borrow a grid connection, and why holding one did not save Palisades. What an uprate is, where the power actually goes, and who has signed what. Then the new reactors: those on ordinary fuel, and those waiting on HALEU. Finally, whether the old fleet's own fuel is safe, and what all of it adds up to by 2030.

<details class="analogy">
<summary>The analogy</summary>
<p>You need a cooker working this month. The old one in the garage still has its socket in the wall and runs on gas from any supplier. It needs a safety check and a new hose, and then it cooks. Fitting a bigger burner to the cooker you already use, while the kitchen is shut for cleaning, gets you a little more heat for very little money.</p>
<p>The new model is better, but it runs on cartridges that one small shop fills a few at a time, and the council keeps the only spare box. The shop will not build a factory until enough new cookers are sold, and nobody buys a cooker without cartridges. So the old cooker makes dinner for years before the new one does. One catch: a quarter of the gas for the old cooker has come from a supplier you have just banned.</p>
</details>

## Why do AI companies want nuclear power at all?

Because a nuclear plant runs almost every hour of the year without burning anything, and an AI data centre needs power every hour of the year.

The measure that shows this is the **capacity factor**: the electricity a plant actually produced in a year, as a share of what it would have produced running flat out all year. America's nuclear plants had a capacity factor of 91.1 per cent in 2025, according to the Energy Information Administration (EIA), the government's energy statistics office. Gas plants of the efficient combined-cycle kind managed 58.7 per cent, wind 33.8 per cent and large solar farms 24.0 per cent.

<!--FIG:cf-chart-->

Those low figures are not faults. Wind and solar run when the weather allows, and gas plants are turned down when cheaper power is available. But a data centre full of AI chips is most valuable when it runs without pause. Its owner wants a supply that matches it hour by hour.

That matters most to the companies that promised it. Google has a goal of **24/7 carbon-free energy**: by 2030, every hour of electricity it uses on every grid should be matched by carbon-free power on that same grid in that same hour. In 2024 it reached 66 per cent. Solar alone cannot fill the night, and batteries can shift hours but not seasons. Nuclear is the only carbon-free source that runs nearly every hour at the scale of many gigawatts.

America already has a large nuclear fleet to draw on. The EIA counts 94 reactors at 54 plants, with about 98 gigawatts of capacity, which made 17.7 per cent of the country's electricity in 2025 (my division of its figures). Their average age is about 44 years. They were licensed for 40 years, renewable to 60 and now to 80, so most can run for decades more.

A reactor itself is simpler than its reputation. It is a kettle heated by splitting uranium atoms: the heat boils water, the steam spins a turbine, and the turbine turns a generator. The [microreactors piece](/journal/microreactors/) explains the physics step by step. What matters here is that a reactor makes a great deal of steady heat from very little fuel, for years at a time.

## What does "new" nuclear power for AI actually mean?

It means one of three things, and they arrive in this order: restarting a closed reactor, squeezing more power out of a running one, or building a new one.

A **restart** brings back a reactor that its owner shut and began to decommission. Three are under way in America: Crane (835 MW) in Pennsylvania, Palisades (about 800 MW) in Michigan and Duane Arnold (615 MW) in Iowa.

An **uprate** lets a running reactor make more heat, and so more electricity, under a licence change from the Nuclear Regulatory Commission (NRC), the federal nuclear regulator. The steps are small, from under 2 per cent to as much as 20 per cent of a plant's output, but they come on sites that already work.

A **new build** starts from bare ground, and it comes in three kinds. A **large reactor**, such as the two finished at Vogtle in Georgia in 2023 and 2024, makes about 1,100 MW. A **small modular reactor** (SMR), up to about 300 MW, is designed to be built largely from factory-made parts. An **advanced reactor** uses a different coolant or fuel from today's water-cooled fleet, and most of those need HALEU.

**HALEU**, high-assay low-enriched uranium, is the fuel that divides the field. Natural uranium is only about 0.7 per cent uranium-235, the kind of atom that splits. Concentrating it is called **enrichment**, and it is done by spinning uranium as a gas in fast centrifuges, so the slightly heavier atoms drift outward. Today's reactors burn fuel enriched to about 5 per cent. HALEU is concentrated to just under 20 per cent, which lets a small or fast-neutron core run for years. Making it takes roughly five times the enrichment work per kilogram of ordinary 5 per cent fuel, and almost nobody makes it yet.

## What does a nuclear project need before it can sell a kilowatt-hour?

Four things, each with its own clock: a place on the grid, a reactor that works, a licence to run it, and fuel. The slowest of the four sets the date.

The **grid place** is the right to connect a power station to the high-voltage network at a set size. Getting a new one means joining a queue while the grid operator studies what lines and substations must be built. The **reactor** must be built, or repaired and tested. The **licence** comes from the NRC, which must approve the design, the site, the operators and the security plan. And the **fuel** must be mined, enriched, made into fuel assemblies and delivered.

<!--FIG:clocks-->

This is the whole argument in one picture. A restart or an uprate begins with most of the clocks already run. Its site is licensed, it has held or can borrow a grid place, and it burns ordinary fuel that a mature industry supplies. What is left is repair work and paperwork. A new build starts the grid, reactor and licence clocks at zero, and for most advanced designs the fuel clock runs years behind the other three.

## How does a closed reactor come back to life?

Through a regulatory path that did not exist until 2023, a few years of repair and hiring, and about US$1.6 billion in Crane's case.

<a id="constellation-restarts-the-reactor"></a>

Crane shut on 20 September 2019, for economic reasons: it could not earn enough selling power into the market. Its fuel was removed six days later. The plant was placed in **SAFSTOR**, a form of decommissioning in which a closed plant is kept intact and guarded while its radioactivity decays, before the dismantling starts. That choice is what makes a restart possible at all.

The rules were written for one-way traffic. Once an owner tells the NRC that a reactor has shut for good and its fuel is out, the federal rule known as 10 CFR 50.82(a)(2) says its licence no longer allows it to run or to hold fuel in the reactor. There was no procedure for going back. Holtec, a private nuclear company, built one for Palisades from February 2023.

The path has four parts, and the NRC approves them together. An **exemption** from that rule lets the owner withdraw, once, its certification that the plant had closed. **Licence amendments** restore the operating licence and its technical rules, the emergency plan and the security plan. And an **environmental assessment** checks the effects of running again. For Palisades it took about 30 months, from the first filing to approval on 24 July 2025.

Crane is following the same path, about a year behind. Constellation filed in November 2024. The NRC allowed it to receive new fuel on 1 July 2026 and finished its environmental assessment on 18 September 2026. The exemption and the three amendments are still under review, and an NRC schedule letter of January 2026 targets a decision by 4 March 2027.

The physical work is mostly in the parts that make electricity, not in the reactor itself. Constellation ordered three new **main power transformers**, the giant units that step the generator's output up to grid voltage, and paid US$35 million extra for them to arrive in 2026. It has inspected the steam generators, turbines and condensers. It had about 500 full-time staff by September 2025, nearly 80 per cent of what it needs, with operators trained and licensed afresh.

The money is modest by nuclear standards. Constellation says it has invested about US$1.6 billion, and the Energy Department's lending office lent US$1 billion of it in November 2025. Microsoft buys the output under a 20-year contract signed in September 2024, at an undisclosed price. That is roughly US$1,900 per kilowatt of capacity, on my arithmetic. A new large reactor costs several times as much.

Few closed reactors can follow. Once an owner moves from SAFSTOR to active dismantling, the reactor vessel and its internals are cut up and removed, and nothing remains to restart. Apart from the three, no closed American reactor has a restart application at the NRC. The Energy Secretary has called for reopening Indian Point in New York, at a cost he put at a little more than US$10 billion, but nothing has been filed.

## Why did Crane have to borrow a place on the grid?

Because its own place expired a year after it closed, and a fresh one might not have been fully ready until the end of 2030 or later.

The grid here is run by **PJM**, the operator of the high-voltage network and power market for thirteen states from New Jersey to Illinois. A power station in PJM holds **capacity interconnection rights**: the right to put a set number of megawatts into the network as reliable capacity that it can be paid to keep available. Under PJM's tariff, a closed plant's rights end one year after it shuts, unless a new request claims them. Crane's lapsed in 2020.

So Crane had to apply again like a new plant. In May 2025 PJM picked it for a fast track for projects it judged important to reliability. Its first study, in October 2025, found that Crane's full output could be delivered only once a list of new transmission was built, including long new lines at 765 and 500 kilovolts, some due as late as December 2030. Until then Crane would be only partly deliverable, reviewed year by year.

Constellation told FERC that, without help, full delivery could be at risk until at least 31 December 2030. A typical project waits longer still: the median for American power projects finished in 2025 was 61 months from asking to connect to running, according to Lawrence Berkeley National Laboratory's 2026 survey. A reactor can be repaired faster than the grid around it can be rebuilt.

<!--FIG:crane-chart-->

So Constellation borrowed a plug from its own fleet. Eddystone Units 3 and 4, two of its oil and gas units near Philadelphia, were due to retire in May 2025. The Energy Department has kept them running ever since, under six emergency orders in a row, the latest to 20 November 2026. On 1 June 2026 the Federal Energy Regulatory Commission (FERC), which regulates interstate power markets, granted Constellation a one-time waiver to move their 760 MW of rights to Crane.

What that buys is less certain than the headlines suggest. FERC said the transfer could "potentially" let Crane run fully before the end of 2030, and that PJM's studies still decide. Rights moved to a different connection point need not transfer one for one. The reactor's own date, the second half of 2027, never depended on the plug. What the borrowed rights may change is how soon all 835 MW count.

## If holding a grid place is enough, why is Palisades late?

Because a grid place makes a restart possible, not quick. Palisades kept its place, and its reactor work set the pace instead.

<a id="palisades-waits-on-the-reactor"></a>

Palisades sits on the grid of **MISO**, the operator for much of the Midwest. There a closed plant can stay "suspended", keeping its connection, for at most 36 months in any five years. Palisades shut in May 2022, so its time ran out in May 2025. FERC extended it by 22 months, to 1 March 2027. Holtec owns the land and the connection equipment, and the plant was reconnected to its 345 kilovolt switchyard on 11 September 2026.

The reactor was harder. Its **steam generators**, the large heat exchangers where hot reactor water boils separate water into steam, had worn tubes. Holtec repaired them by sleeving the tubes rather than replacing the generators, under an NRC amendment of October 2025. Loading fuel began on 30 August 2026. Then a fuel assembly tilted about 30 degrees after it was placed, and loading stopped.

Recovering one assembly took a month. Holtec needed an emergency licence amendment, which the NRC approved on 13 October 2026, and a purpose-built tool to lift the assembly out. On the same day the NRC published an inspection finding a "chilled work environment" in two departments, meaning staff felt unable to raise safety concerns freely. Holtec has given no new restart date.

The deadline is commercial. Palisades sells its output to two power cooperatives, Wolverine and Hoosier, under 28-year contracts. If the plant is not in service by March 2027, either side may end them, and Holtec would owe its share of a US$100 million termination payment. Holtec's filing for a share listing in September 2026 still said the restart would come in 2026. It withdrew that filing on 25 September.

The third restart shows the same lesson the other way round. NextEra Energy, the Florida power group, kept Duane Arnold's grid place through a FERC waiver of August 2025. It folds the rights of solar projects planned at the site back into one nuclear connection of up to 619 MW, provided the plant runs by 31 December 2029. The Energy Department lent up to US$1.9 billion in September 2026. Google buys most of the output under a 25-year contract, and CIPCO, an Iowa power cooperative, the rest on the same terms.

Duane Arnold's harder job is physical. A storm in August 2020 wrecked its cooling towers just before a planned closure, and those were later demolished. NextEra must build new ones and order a generator, and the NRC is still reviewing the same exemption and amendments as at Crane. NextEra's date is the first quarter of 2029 at the latest.

<!--FIG:restarts-->

## What is an uprate, and why is it the cheapest new nuclear megawatt?

An uprate is a licence change that lets a running reactor make more heat. It comes on a site that already has everything else, which is why it costs a fraction of a new plant per kilowatt.

<a id="constellation-squeezes-the-reactors"></a>

More heat from the core makes more steam, and more steam through the turbine makes more electricity. The NRC sorts uprates into three types by size, and the size decides what has to change in the plant.

A **measurement uncertainty recapture** uprate adds less than 2 per cent. The plant fits more accurate meters on the water flowing into its steam generators, so it knows its true power more exactly and can run closer to its licensed limit. A **stretch** uprate adds up to about 7 per cent, mostly by resetting instruments within the margins the plant was designed with. An **extended** uprate adds up to 20 per cent, and needs new turbines, generators, pumps or transformers.

<!--FIG:uprate-->

America has done this before, on a large scale. The NRC has approved 172 uprates since 1977, adding 8,030 MW of electricity, the output of about seven large reactors. Then the work stopped. The last ten approvals, from 2017 to 2021, were all small meter upgrades, and the last of them came in November 2021. As of September 2026, no uprate application was under NRC review at all.

AI buyers have restarted it. The NRC's list of expected applications, updated on 8 September 2026, shows 31 uprates from the fourth quarter of 2026 to 2032, adding about 2,421 MW. Nineteen of them are extended uprates, the kind that need new heavy equipment. Twelve are Constellation's, five of them extended.

The deals behind them are specific. On 6 October 2026 Google agreed a 20-year contract to buy the power from 890 MW of uprates at eleven Constellation reactors on six sites, which Constellation will invest more than US$4.3 billion to build. Amazon has signed for about 190 MW at Calvert Cliffs in Maryland, and Meta for 30 MW at Clinton in Illinois and 433 MW at three plants of Vistra, a Texas power company. Google has signed for about 96 MW in Georgia, still awaiting state approval. Together that is about 1,640 MW, on my sum.

That is cheap power by nuclear standards. Google's 890 MW for US$4.3 billion is about US$4,800 per kilowatt, and Constellation's earlier turbine uprate at Byron and Braidwood about US$5,100. The two new reactors at Vogtle cost their owners roughly US$14,000 per kilowatt, after years of overruns (my arithmetic, from reported totals). On 27 October 2026 the Energy Department offered Constellation a conditional loan of up to US$5 billion for its uprates.

<!--FIG:cost-chart-->

The catches are timing and equipment. Heavy work can be done only while a reactor is shut to reload fuel, every 18 to 24 months, so the megawatts arrive in steps: Constellation's first by 2028, Google's last before the end of 2032. Extended uprates need the same transformers and generators everyone else is waiting for, so they join [the equipment queue](/journal/the-equipment-queue/). And none of these AI-funded uprates had reached the NRC by September 2026.

## Does the nuclear power actually go to the data centre?

Almost never directly. On the PJM and MISO grids, every binding nuclear deal for AI now sells power into the grid, and the data centre draws its electricity from the grid like any other customer.

A deal can be done two ways. **Behind the meter**, or co-located, the data centre sits beside the plant and takes power before it reaches the grid, so it avoids some of the charges for using the high-voltage network. **In front of the meter**, the plant sells all its output into the grid, and the buyer signs a **power purchase agreement** (PPA): a long contract to pay a set price for a set amount of the plant's power, while drawing its actual electricity from the grid wherever its data centres are.

<!--FIG:meter-->

The first big co-location deal hit a wall. Talen Energy, owner of the Susquehanna nuclear plant in Pennsylvania, agreed in March 2024 to supply up to 960 MW to an Amazon campus next to the plant. In November 2024 FERC rejected a change that would have raised the co-located load from 300 to 480 MW. The grid owners had argued that a data centre on the grid's doorstep still leans on the grid, and should pay for it.

So the deal moved in front of the meter. On 11 June 2025 Talen and Amazon agreed up to 1,920 MW through 2042, delivered through the grid, with the local utility handling delivery. Talen's quarterly report says the switch took effect in April 2026.

Then FERC wrote rules. In an order of 18 December 2025 it found PJM's rules unjust for lacking clear terms for co-location, and required a co-located data centre to take one of three transmission services, two of them new, either firm or interruptible. A plant adding co-located load must now be studied, pay for any grid upgrades, and wait for them. A follow-up order came in June 2026, and PJM's compliance is due by 16 November 2026.

The practical result is simple. Crane, Clinton, Susquehanna, Duane Arnold, Calvert Cliffs, Meta's Vistra plants and Google's uprates all feed the grid. The exception is in Texas, on ERCOT's separate grid: Vistra has a binding 20-year contract for 1,200 MW from its Comanche Peak plant, with a buyer its chief executive has named as Amazon, and the plan is a campus beside the plant. Outside Texas, a nuclear deal for AI is a financial contract that adds carbon-free power to the same grid the data centre uses, matched on paper. That is exactly what Google's hourly goal counts.

## Who has signed what, and how binding is it?

The binding contracts sit on reactors that already exist. The deals with new reactors are mostly funding, options and targets.

<a id="oklo-sells-the-electricity"></a>

Count the megawatts. Long, binding power purchase agreements on existing American reactors and their uprates cover about 9,880 MW: Crane, Susquehanna, Clinton, Duane Arnold, Calvert Cliffs, Google's Constellation uprates, Meta's Vistra plants and Vistra's Comanche Peak in Texas (my sum of the companies' figures; Duane Arnold's includes the cooperative's share). Google's separate 15-year deal for 2,700 MW is an energy supply contract across Constellation's existing plants, not a power purchase agreement on named plants, so I leave it out.

The new-reactor side reads differently. Meta has funded development of two TerraPower reactors, up to 690 MW and as early as 2032, with rights to up to six more. Oklo's 1.2 GW campus for Meta in Ohio rests on a framework under which Meta prepays for future power; Oklo says it is not a power purchase agreement. Google has a framework with Kairos Power for 500 MW by 2035. Amazon has a target of more than 5 GW from X-energy by 2039.

<a id="kairos-signs-before-it-switches-on"></a>

The one binding contract on a new reactor is small. On 18 August 2025 TVA, the federal power company for Tennessee and its neighbours, agreed to buy up to 50 MW from Kairos Power's Hermes 2 reactor at Oak Ridge from 2030, for Google's data centres in the region. Hermes 2's permit covers test reactors of 35 thermal megawatts each, and at a third efficiency even two of them cannot make 50 megawatts of electricity, so the contract implies a larger plant the NRC has not yet been asked to license. Its fuel source is not yet named.

<!--FIG:deals-chart-->

The split follows the clocks. A buyer can sign a firm 20-year price on a reactor that already has a licence, a grid place and fuel, because the seller can promise delivery. A buyer of a reactor that does not yet exist is buying an option on four clocks finishing, and it pays for development rather than for power.

## What about new reactors that burn ordinary fuel?

They avoid the fuel problem but not the other three clocks. None of the commercial designs will send power to an American grid before 2030; the ordinary-fuel reactors that have run so far are zero-power test cores.

<a id="darlington-builds-on-the-old-plug"></a>

The closest is in Canada. Ontario Power Generation (OPG), the province's state-owned power company, is building the first of four **BWRX-300s**, a 300 MW boiling-water small reactor designed by GE Vernova and Hitachi, at its Darlington nuclear station. It burns ordinary fuel and sits on a site with an existing nuclear licence and grid corridor. It was licensed to build on 4 April 2025, set its foundation on 22 April 2026 and applied to operate on 25 March 2026. OPG targets connection to the grid by the end of 2030.

Its cost shows why a first small reactor is not cheap. Ontario approved C$20.9 billion for all four units, including interest and contingency. The first unit, with the systems all four share, is C$7.7 billion for 300 MW, about C$25,700 per kilowatt (my arithmetic). Later units should cost less, which is the point of building the same design four times.

America's first follows. On 29 September 2026 the NRC issued the first American construction permit for a BWRX-300, to TVA at its Clinch River site in Tennessee. It still needs a separate licence to operate, and TVA's target, reported in the press, is 2033.

Large reactors are further back. Vogtle's two units, the last built in America, entered service in July 2023 and April 2024, seven years late and at roughly twice their planned cost. The US government announced a partnership in October 2025 for at least US$80 billion of new AP1000 reactors from Westinghouse, one of America's oldest reactor makers, the same 1,100 MW design. By 30 October 2026 it had produced no American site or order. Fermi America, a Texas developer of power for data centres, plans four AP1000s there, the first in 2032.

## Why do the advanced reactors wait on fuel?

Because most of them need HALEU, and America makes it on one line of sixteen centrifuges whose government contract has ended.

<a id="terrapower-waits-on-the-fuel"></a>

The [microreactors piece](/journal/microreactors/) follows that fuel from mine to core, step by step. Here only four facts matter. The only American line that has made HALEU is Centrus Energy's cascade of sixteen centrifuges in Piketon, Ohio. By June 2026 it had made more than 1,900 kg of HALEU as gas, about 1.3 tonnes of uranium, in all its years of running (my conversion).

Its government work has run out. The Energy Department ordered maintenance and storage only from 30 June 2026. Centrus said on 4 November that the cascade now enriches for commercial buyers, with no volume given, and the government's 2027 budget proposal does not fund it. Its lease on the site is fixed to end on 1 October 2027.

What comes next is planned, not built. Centrus owes the government one tonne of uranium as HALEU by July 2032, and its build-out, with first new centrifuges in 2029, includes 12 tonnes a year of HALEU capacity, contingent on customers. Against that, the Energy Department expects "more than 40 metric tons" to be needed by 2030, and its own stock, about 21 tonnes by 2028, goes out by allocation to a few first cores.

<!--FIG:advanced-->

Each of the reactors linked to AI buyers meets that wall. **TerraPower** won an NRC construction permit on 4 March 2026 for Kemmerer 1, a 345 MW sodium-cooled reactor in Wyoming, and targets 2030. It will sell to the grid in Wyoming; Meta's deal funds later units of the same design. Its first core depends on a conditional allocation of government HALEU made in April 2025, its size not public, and its later fuel on ASP Isotopes, a company that plans to enrich in South Africa. In an Exchange Act filing of 15 October 2026, ASP said it had still not applied its technology to uranium-235.

**Oklo** broke ground on its 75 MW Aurora at the Idaho National Laboratory in September 2025. Its quarterly report of 6 November 2026 targets its first powerhouse in 2028 to 2029. That first core rests on five tonnes of government HALEU. **Kairos Power's** Hermes 2 has no named fuel source. **X-energy**, Amazon's partner, finished its NRC safety review for a four-reactor plant in Texas on 30 October 2026, and expects power in the early 2030s.

Test reactors have gone critical in 2026, as the microreactors piece describes, but all at zero or very low power, and none is connected to a grid.

The fuel loop has its first cracks. X-energy and Radiant agreed prepayments with Centrus in August and September 2026, and Meta's first payment under its Oklo framework left escrow on 2 November 2026 and went straight to Centrus, as a credit towards fuel orders. Buyers, not the government, are now paying for HALEU before the reactors exist. But no tonnage is public, and new centrifuges take years. The crack moves fuel in the 2030s, not this decade.

## Is the old fleet's own fuel safe?

Mostly, but it has a deadline. A quarter of the enrichment America's reactors bought in 2025 came from Russia, and that supply runs out of road at the end of 2027.

<a id="eunice-cannot-fill-the-gap"></a>

Enrichment is measured in **separative work units** (SWU), a measure of the effort of enriching rather than the amount of uranium. In 2025 American reactor owners bought 12.71 million SWU. Of that, 3.28 million, 25.8 per cent, came from Russia, and only 2.93 million from American plants, according to the EIA's 2025 Uranium Marketing Annual Report.

The door is closing from both sides. America's Prohibiting Russian Uranium Imports Act banned Russian enriched uranium from August 2024, with waivers that all end by 1 January 2028. Russia, for its part, has licensed each shipment to America one by one since November 2024, under an export curb that runs to 31 December 2027. Centrus, which resells Russian enrichment, says well over half the fuel it expects to deliver through 2027 comes from its Russian contract.

<!--FIG:swu-chart-->

The replacements arrive slowly, at different speeds. Urenco, the European enricher, runs America's only commercial enrichment plant, at Eunice in New Mexico, with about 4.3 million SWU a year, and is adding 700,000 by spring 2027. A further 2.1 million comes from 2032. Orano, the French nuclear fuel group, plans 4 million SWU at Oak Ridge in the early 2030s, and Centrus starts its first new machines in 2029.

There is a cushion. American owners held 118 million pounds of uranium at the end of 2025, against 40.9 million pounds loaded into reactors that year. Much of that is natural uranium, which does not replace enrichment. But 51.8 million pounds was already enriched and 7.8 million was finished fuel, more than a year's loading. It is a squeeze on price and timing, not a wall like HALEU's.

<a id="the-box-stops-at-five"></a>

One more limit applies to both lanes: the shipping container. The standard package for enriched uranium gas is certified only up to 5 per cent. The one package approved for HALEU had not been manufactured as of April 2026, according to the NRC. Urenco needed a one-off exemption to ship up to 50 cylinders of fuel enriched between 5 and 10 per cent in 2026 and 2027.

## So what reaches the grid by 2030?

Mostly old reactors. On the companies' own dates, about 2,250 MW of restarts and roughly 1,640 MW of AI-funded uprates should arrive in steps from 2027 to 2034, all on ordinary fuel, though much of the uprate capacity lands after 2030. New reactors on HALEU add at most 470 MW by the end of 2030, if every one of them runs to schedule.

<!--FIG:ladder-->

Set the projects side by side and the pattern is the claim. Crane in 2027, Duane Arnold by early 2029 and Palisades whenever its reactor is ready all reuse sites, licences and fuel. Uprates arrive outage by outage from 2028 to 2034. Oklo's 75 MW is due in 2028 to 2029 on government stock, Kemmerer's 345 MW and Hermes 2's 50 MW in 2030. Darlington, on ordinary fuel, is in Canada and due at the end of 2030.

These are plans, and plans slip. The comparison counts capacity, not energy, and the dates differ in firmness: Palisades has none, and the uprates stretch past 2030. What the figures rank is which lane can deliver first, not how much power each will produce.

The HALEU test is narrower than it looks, and I should say so. Aurora's 75 MW alone cannot break it, because its first core is government stock. Kemmerer 1 on its own would, and so would Aurora and Hermes 2 together. So the claim is a bet that Kemmerer misses 2030 and that Hermes 2, with no named fuel and a permit too small for its contract, does too.

## So who holds the scarce thing, and what should an investor watch?

The scarce things are licensed sites with grid places, and enrichment capacity outside Russia. Both are held by a few companies, and neither can be built quickly with money alone.

**The owners of the existing fleet** hold the first. Constellation, Vistra, NextEra, Talen and Holtec own reactors that buyers will pay to keep, restart or enlarge, under 20-year contracts. That is why hyperscalers now fund uprates. The risks are execution and equipment: Palisades shows one tilted fuel assembly can cost months, and extended uprates queue for the same transformers as everyone else.

**The enrichers** hold the second. Urenco, Orano and Centrus sell the separative work both lanes need: the old fleet to replace Russia by 2028, and the new one for HALEU. Their constraint is time, because a new enrichment plant takes most of a decade from licence to full output.

**The new reactor developers** hold permits, sites and option-like contracts, and need fuel. TerraPower, Oklo, Kairos and X-energy are funded by the same companies that sign firm contracts with the old fleet. For them the date to watch is not a groundbreaking but the first tonne of HALEU delivered for a commercial core.

The signals to watch are dated. Crane's first power in the second half of 2027, and whether Palisades meets its March 2027 contract deadline. The first AI-funded extended uprate filed at the NRC. Whether Centrus's plan for 12 tonnes a year of HALEU becomes a contract, and whether ASP Isotopes enriches any uranium. And how much Russian enrichment still arrives as both governments' deadlines fall at the end of 2027.

## What would prove me wrong

Two tests break the claim. If reactors fuelled with HALEU together send electricity to American grids from 100 MW or more of capacity by 31 December 2030, fuel was not the gate. If fewer than two of Crane, Palisades and Duane Arnold have delivered power to the grid by 31 December 2029, an existing site is not the fast lane.

Some events would move me before either test. Centrus contracting its 12 tonne a year build-out with firm customers, or ASP Isotopes enriching its first uranium-235, would start a commercial HALEU supply that does not wait for the reactors. A large HALEU allocation from the Energy Department beyond first cores would do the same. And a second restart stalling as Palisades has would weaken the first limb.

Three things would not move me. More signings with new reactor developers: a framework or option is not a delivery contract. More test reactors going critical: a zero-power physics test proves a reactor, not a fuel supply. And Darlington: it burns ordinary fuel, it is in Canada, and if it runs on time it supports the claim that fuel, not the reactor, is what holds the advanced designs back.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

**Nuclear for AI: the old reactors come first because they already own the hard parts** (CLAIM_DATE)

Claim: "CLAIM_TEXT"

Breaks if: "BREAKS_TEXT"

EARLIER_CLAIMS

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

**Capacity factors.** EIA Electric Power Monthly, Tables 6.07.A and 6.07.B (released 23 October 2026), 2025: nuclear 91.1%, natural gas combined cycle 58.7%, coal 48.8%, wind 33.8%, utility-scale solar photovoltaic 24.0%. Nuclear 90.8% in 2024 and 93.0% in 2023. Nuclear generation 785,304 GWh of 4,425,029 GWh utility-scale, 17.7% (my division, Table 1.1). Fleet: 94 reactors at 54 plants, the EIA's count of March 2026, which includes Palisades and Crane as "out of service"; 98,408 MW time-adjusted average for 2025; average age about 44 years. Google's hourly carbon-free share: 66% in 2024 (2025 environmental report).

**Restarts.**

| Plant | Size | Closed | Grid place | Money | Buyer | Date given |
|---|---|---|---|---|---|---|
| Crane (ex-Three Mile Island 1), Pennsylvania, Constellation | 835 MW | 20 September 2019 | Rights lapsed; re-entered PJM's queue; 760 MW of Eddystone rights moved by FERC waiver, 1 June 2026 (ER26-2028-000) | About US$1.6bn invested; DOE loan US$1bn, 18 November 2025 | Microsoft, 20 years (20 September 2024) | Second half of 2027 (6 August 2026); NRC target for its approvals 4 March 2027 |
| Palisades, Michigan, Holtec | About 800 MW | 20 May 2022 | MISO suspension extended to 1 March 2027 (FERC, 28 February 2025, ER25-1083) | DOE loan up to US$1.52bn, US$1.0bn drawn by 30 June 2026; Michigan US$300m | Wolverine and Hoosier, 28 years each; either may end if not in service by March 2027 | None since fuel loading stopped (21 September 2026) |
| Duane Arnold, Iowa, NextEra | 615 MW | 10 August 2020 | Up to 619 MW kept through MISO's replacement process; operation by 31 December 2029 (FERC, 25 August 2025, ER25-2989) | DOE loan up to US$1.9bn, 8 September 2026 | Google, 25 years (27 October 2025); CIPCO the rest | First quarter 2029 at the latest |

NRC restart path: exemption from 10 CFR 50.82(a)(2), amendments to the operating licence, emergency plan and security plan, and an environmental assessment. Palisades: first filing 1 February 2023, approval 24 July 2025, back on an operating basis 25 August 2025. Crane: filings from 4 November 2024; new-fuel amendment 1 July 2026; final environmental assessment 18 September 2026; NRC target 4 March 2027 (schedule letter of 7 January 2026, ML25345A027, which I saw only in a search excerpt). Palisades: tilted assembly, emergency amendment 30 September to 13 October 2026 (ML26282A040); "chilled work environment" inspection report 13 October 2026 (ML26286A257). Holtec's registration statement of 8 September 2026 was withdrawn on 25 September 2026; its facts on the contracts and loans are used as filed.

Cost per kilowatt, my arithmetic: Crane US$1.6bn ÷ 835 MW ≈ US$1,900. Google uprates US$4.3bn ÷ 890 MW ≈ US$4,800. Byron and Braidwood US$800m ÷ 158 MW ≈ US$5,100. Vogtle 3 and 4: about US$31bn to the owners (press, AP) ÷ 2,234 MW ≈ US$14,000; Georgia Power's own share, net of the Toshiba payment and before financing, about US$9,800 (Southern Company 10-K for 2024). Darlington unit 1 with common systems C$7.7bn ÷ 300 MW ≈ C$25,700.

**Crane's grid timeline.** PJM tariff part VII, section 328(C)(3): rights end one year after deactivation. PJM picked Crane for its Reliability Resource Initiative on 2 May 2025. Phase I study results of 31 October 2025 listed contingent facilities with in-service dates as late as December 2030. FERC order 195 FERC ¶ 61,162 (1 June 2026), paragraph 38: "absent the waiver, Crane... may not be able to obtain full deliverability until at least December 31, 2030"; paragraphs 38 to 39: the transfer could "potentially" enable full operation before then, and PJM's studies control. Eddystone's emergency orders under section 202(c) of the Federal Power Act: 202-25-4 (30 May 2025) to 202-26-40 (to 20 November 2026). Queue time: Lawrence Berkeley National Laboratory, Queued Up: 2026 Edition (June 2026), median 61 months from interconnection request to operation for projects built in 2025.

**Uprates.** NRC, Types of Power Uprates and Approved Applications (reviewed 15 September 2026): 172 approved since 1977, 24,089 MWt (8,030 MWe); last approval Millstone 3, 9 November 2021. Pending list empty (15 September 2026). Expected applications (8 September 2026): 31 in the summary (10 measurement uncertainty, 2 stretch, 19 extended), 30 itemised, 7,336 MWt, about 2,421 MWe, fourth quarter 2026 to 2032; Constellation 12 (5 extended, 7 measurement uncertainty). AI-funded uprates: Google and Constellation 890 MW (6 October 2026); Amazon and Constellation, Calvert Cliffs, about 190 MW (30 September 2026); Meta and Vistra 433 MW (Perry 213, Davis-Besse 80, Beaver Valley 140; Vistra 8-K, January 2026); Meta and Constellation, Clinton, 30 MW (3 June 2025); Google and Georgia Power about 96 MW (filed 21 September 2026, press, awaiting state approval). Sum about 1,639 MW, my arithmetic. DOE conditional commitment to Constellation up to US$5bn (27 October 2026).

**Deals.** Binding power purchase agreements on existing reactors, megawatts as the companies give them: Crane 835 (Microsoft); Susquehanna up to 1,920 (Amazon, in front of the meter since April 2026); Clinton 1,121 including 30 of uprate (Meta, from June 2027); Duane Arnold 615 (Google and CIPCO); Calvert Cliffs 690 including 190 of uprate (Amazon); Constellation uprates 890 (Google); Vistra 2,609 including 433 of uprate (Meta); Comanche Peak 1,200 (Vistra 8-K, 29 September 2025; buyer named as Amazon by Vistra's chief executive, 26 February 2026), in Texas, with a campus planned beside the plant. Sum 9,880 MW, my arithmetic; Google's 2,700 MW, 15-year energy supply agreement across existing Constellation plants is excluded. TerraPower's units for Meta could come as early as 2032; Kemmerer 1 is not part of that deal. New reactors: TerraPower, two units up to 690 MW funded and rights to up to six more (Meta, 9 January 2026); Oklo up to 1.2 GW, a prepayment framework, not a power purchase agreement (Oklo, 6 November 2026); Kairos 500 MW by 2035, a framework (Google, 14 October 2024); Hermes 2 up to 50 MW, a binding utility contract (TVA, 18 August 2025); X-energy more than 5 GW by 2039, a target (Amazon, October 2024). FERC co-location: rejection of the Susquehanna amendment, 1 November 2024 (ER24-2172); PJM co-location order 193 FERC ¶ 61,217 (18 December 2025, EL25-49); rehearing and compliance order 195 FERC ¶ 61,209 (18 June 2026); compliance due 16 November 2026.

**HALEU.** Centrus: "cumulative total of more than 1,900 kg" of HALEU as UF6 by mid-June 2026 (release, 1 July 2026); UF6 is about 67.6% uranium by mass, so about 1.28 tonnes of uranium (my arithmetic). Maintenance-only order 30 June 2026; task order of 1 July 2026 for 1 tonne of uranium by July 2032, with two options of 5 tonnes; build-out including 12 tonnes a year of HALEU capacity, first new capacity by 2029 (1 July 2026); lease fixed to end 1 October 2027 (quarterly report, 4 November 2026); commercial enrichment, no volume, and US$5.4bn of contingent commitments, US$5.1bn under definitive agreements (4 November 2026). DOE: "more than 40 metric tons (MT) of HALEU will be needed by 2030" (Record of Decision, 14 January 2025); stock about 21.2 tonnes by 2028 (DOE to GAO, GAO-26-107385, 20 August 2026). Oklo: five tonnes recovered from EBR-II fuel for its first core. ASP Isotopes: 8-K of 15 October 2026. X-energy: NRC final safety evaluation, 30 October 2026. Pilot programme criticalities: Antares (4 June), Valar (18 June), Aalo (4 July), Oklo's Groves test reactor (5 August 2026), all zero or low power. HALEU needs about 41 SWU per kilogram at 19.75% against about 7.8 at 4.95%, about five times, with tails at 0.25% (my arithmetic, as in the microreactors piece).

**Separative work, 2025.** EIA 2025 Uranium Marketing Annual Report, Table 16: Russian-origin 3,284 thousand SWU of 12,710 thousand purchased by owners and operators, 25.8%; US-origin 2,930 thousand. Public Law 118-62: waivers end no later than 1 January 2028. Russian decree 1544 (14 November 2024), extended by decree 1516 to 31 December 2027 (Centrus quarterly report). Urenco USA: about 4.3 million SWU, 700,000 being added, sixth of eight cascades running in October 2026, a further 2.1 million producing from 2032 (Urenco, 29 June and 8 October 2026). Orano IKE, Oak Ridge: initial 4 million SWU, licence sought for 7 million, up to 8% U-235 (Federal Register, 12 August 2026); production ramping from 2031 to 2032 (Orano). Centrus Piketon: first new capacity 2029, no SWU figure published. Inventories: owners 118.3 million pounds of U3O8 equivalent at the end of 2025 (Table 22, preliminary); 40.9 million pounds loaded in 2025.

**Shipping.** NRC environmental assessment for Urenco USA (Federal Register, 15 April 2026): the DN30 package (certificate 9362) limited to 5% U-235; the DN30-X (certificate 9388) the only approved package for commercial HALEU quantities, "manufacturing... has not yet occurred"; 40 to 50 cylinders between 5 and 10% in 2026 and 2027 for one customer.

**The ladder.** Restarts 835 + 800 + 615 = 2,250 MW. HALEU reactors with a date by 2030: Aurora-ID 75 MW (2028 to 2029), Kemmerer 1 345 MW (2030), Hermes 2 up to 50 MW (2030); sum 470 MW, my arithmetic. Darlington 1, 300 MW, OPG, grid by the end of 2030, in Canada and outside the claim's test.

</details>

<section class="exposure">
<h3>Who is exposed if the old reactors come first and the new ones wait on fuel</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>Owners of the existing fleet</dt>
<dd><span class="names">Constellation</span>, <span class="names">Vistra</span>, <span class="names">NextEra Energy</span>, <span class="names">Talen Energy</span> and <span class="names">Holtec</span> run, restart and uprate reactors.</dd>
<dt>Enrichers</dt>
<dd><span class="names">Urenco</span>, <span class="names">Orano</span> and <span class="names">Centrus Energy</span> enrich uranium; <span class="names">ASP Isotopes</span> plans to.</dd>
<dt>New reactor developers</dt>
<dd><span class="names">TerraPower</span>, <span class="names">Oklo</span>, <span class="names">Kairos Power</span> and <span class="names">X-energy</span> on HALEU; <span class="names">GE Vernova Hitachi</span> (BWRX-300) and <span class="names">Westinghouse</span> on ordinary fuel.</dd>
<dt>The buyers</dt>
<dd><span class="names">Microsoft</span>, <span class="names">Google</span>, <span class="names">Amazon</span> and <span class="names">Meta</span> sign the long contracts.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>AI campuses counting on HALEU reactors this decade, and <span class="names">Rosatom</span>, Russia's state nuclear company, which loses its American enrichment customers.</dd>
</dl>
</section>

---

<p class="sources">Sources: NRC plant pages, orders, amendments, schedule letters and uprate lists (to 15 September 2026); FERC orders ER26-2028 (1 June 2026), ER25-1083 (28 February 2025), ER25-2989 (25 August 2025), ER24-2172 (1 November 2024) and EL25-49 (18 December 2025, 18 June 2026); Department of Energy releases and section 202(c) orders; Constellation (20 September 2024, 18 November 2025, 3 June 2025, 6 August, 30 September, 6 and 27 October 2026); Holtec's withdrawn registration statement (8 September 2026); NextEra and Google (27 October 2025); Vistra 8-K (January 2026); Talen (11 June 2025) and its quarterly report for June 2026; Google (6 October 2026); OPG, the Canadian Nuclear Safety Commission and GE Vernova (29 September 2026); Southern Company's 2024 annual report; Cameco (30 October 2026); Centrus (1 July and 4 November 2026); Oklo (6 November 2026); ASP Isotopes (15 October 2026); TerraPower (4 March 2026); X-energy (30 October 2026); Kairos, TVA and Google (18 August 2025); the EIA's Electric Power Monthly and 2025 Uranium Marketing Annual Report; Public Law 118-62; Urenco (29 June 2026) and the Federal Register; Lawrence Berkeley National Laboratory (June 2026). Personal research, not investment advice.</p>
