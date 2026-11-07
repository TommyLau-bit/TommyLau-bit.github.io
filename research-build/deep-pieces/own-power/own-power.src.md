---
title: "Building your own power: GE Vernova's queue, not the grid's, sets the date"
date: 2026-11-07T17:20:00+08:00
summary: "AI campuses that cannot wait years for a grid connection are building their own gas power beside the building. That does not skip the queue. It swaps the grid's queue for the turbine makers', which at GE Vernova is six years of output and growing, and the quicker machines, the gas pipes and the air permits all have queues of their own."
category: "Analysis"
format: "depth"
cover: "/covers/building-your-own-power.svg"
tags: ["power", "data-centres", "grid", "supply-chain"]
draft: true
---

<a id="building-your-own-power"></a>

In late July 2026 a gas power plant in New Albany, Ohio, began feeding a Meta data centre with no grid connection between them. Williams, best known for running America's largest gas pipeline, built and runs it. Called Socrates, it is the clearest case of an AI campus making its own power. Its second half was approved in September 2025 and was due to run about fourteen months later.

That speed is the exception, and the reason sits in a factory in South Carolina. At the end of September 2026 GE Vernova, which makes many of the heavy gas turbines that power stations are built around, had 122 gigawatts of them under contract. It ships about 20 gigawatts a year. It is now selling places in its production line for 2032.

That is the claim of this piece. Building your own power does not skip the queue. It changes which queue you stand in: the grid's waiting list becomes the turbine makers', which at GE Vernova is about six years long and still growing. The quicker machines are filling too, and the gas pipe and the air permit have clocks of their own.

To see why, the piece follows the questions in order. Why campuses build their own power, and what that means. How a gas turbine works, and why its hottest blade is so hard to make. Why the makers will not simply build more factories, how long their queues are, and what buyers pay to stand in them. Then the quicker machines, why an island campus builds more machine than it uses, where the gas comes from, how long a pipe and a permit take, and whether going through the utility avoids it all. Finally, whether the queue is starting to clear, and what would prove me wrong.

<details class="analogy">
<summary>The analogy</summary>
<p>Picture a new restaurant whose street gas main is booked up for years: that is the grid connection. So the owner buys a stove for the kitchen: that is the turbine on site. Every restaurant in town has the same idea that week, and the famous stove maker's diary now runs six years ahead. It will not build a second factory, because twenty years ago it built too many and nearly went under.</p>
<p>A camping-stove shop sells smaller burners sooner, but its diary is filling too: those are the engines, fuel cells and smaller turbines. Any stove still needs a gas line into the kitchen, booked years ahead from an installer, and a council certificate for the chimney. So the restaurant opens when the slowest of the four arrives.</p>
</details>

## Why are AI campuses building their own power stations?

Because the grid cannot connect them fast enough, and a campus that waits years for power earns nothing from the chips inside it.

A large AI campus needs hundreds of megawatts, and some plan several gigawatts. A **megawatt** (MW) is a million watts, about the power drawn by a few hundred homes at once; a **gigawatt** (GW) is a thousand megawatts, about the output of one large power station. Few points on America's grid have that much spare capacity, so a campus usually needs new lines, new substations and often new power stations behind them. The wait for that is set out in [America rations the plug](/journal/america-rations-the-plug/); in many regions it runs to years.

Some states have gone further than a queue. In its outlook of September 2026 the Energy Information Administration (EIA), the government's energy statistics office, reported that Texas had paused the connection of new data centres to the grid "to facilitate a regulatory audit". The EIA cut its forecast for Texas power demand growth in 2027 from 14 per cent to 6 per cent as a result.

The chips do not wait. An AI accelerator loses value every year it sits unpowered, as newer chips arrive, and a campus is financed on the date it starts earning. So the owners asked a simple question: if the grid cannot bring power in, why not make it on site?

America has the fuel to do it. It produced 107.6 billion cubic feet of natural gas a day in 2025, the most in the world, and gas pipes already cross most of the country. A gas plant beside the building turns that gas into electricity without waiting for a high-voltage line. That is the way out this piece follows.

## What does "your own power" actually mean?

It means generating electricity on the campus's side of the utility's meter, either alongside a grid connection or with none at all.

Power made on the customer's side of the meter is called **behind the meter**: a well of one's own beside the water main. Behind-the-meter power comes in three forms.

**Islanded** means no grid connection at all: the campus's plant is its only supply, as at Socrates. **Bridging** means own power that runs until the grid connection arrives, then becomes backup or is removed. **Co-located with a grid tie** means a plant beside the campus that also connects to the grid, so each can lean on the other.

The rules treat them differently. In December 2025 the Federal Energy Regulatory Commission (FERC), which oversees wholesale power markets and interstate gas pipes, ruled that PJM, the grid operator for thirteen states from Illinois to Virginia, could no longer let large new loads simply net their own generation against what they draw. Texas law now lets its grid operator order a large campus's backup generators on, or its load off, in an emergency. So an islanded campus escapes those grid rules, at the price of carrying every risk itself.

Whichever form it takes, own power needs four things. A machine to burn the gas, a pipe to bring it, an air permit to burn it, and, for an island, enough spare machines to keep running when one fails. Each comes with its own queue. The machine's is the longest, so the piece starts there.

## How does a gas turbine turn gas into electricity?

It works like a jet engine bolted to the ground: it squeezes air, burns gas in it, and lets the hot gas spin a shaft that drives a generator.

<!--FIG:turbine-->

A **gas turbine** has three parts on one shaft. The **compressor** at the front squeezes incoming air to about 24 times atmospheric pressure. In the **combustor**, gas burns in that air at a very high temperature. The hot, high-pressure gas then rushes through the **turbine**, a set of bladed wheels it spins on the way out. The turbine turns the compressor and also a **generator**, which makes the electricity.

Run that way alone, it is a **simple-cycle** plant. Its exhaust leaves at about 670°C and goes up a chimney, wasting much of the heat. A **combined-cycle** plant puts that exhaust through a boiler to make steam, which drives a second, steam turbine. Same gas, about half as much electricity again.

The difference shows in the **efficiency**: the share of the gas's energy that ends up as electricity. GE Vernova's largest current unit, the 7HA.03, makes 430 MW in simple cycle at 43.3 per cent efficiency. Paired with a steam turbine, the same unit makes about 640 MW. Siemens Energy's SGT6-9000HL and Mitsubishi Heavy Industries' M501JAC, its two big rivals, quote more than 64 per cent in combined cycle.

Engineers measure this as the **heat rate**: the fuel burned to make one kilowatt-hour, in British thermal units (Btu). Lower is better. A kilowatt-hour holds 3,412 Btu of energy, so a heat rate of 7,884 means 43.3 per cent efficiency. EIA's tested average for America's combined-cycle plants in 2025 was 7,535 Btu per kilowatt-hour; for simple-cycle turbines it was 10,975.

So the combined cycle burns about a third less gas for each unit of power. It also needs a boiler, a steam turbine, cooling and more steel, which add time on site. That trade between fuel and speed runs through the rest of this piece.

## Why is the hottest blade the hardest part to make?

Because the gas that hits it is hotter than the metal can stand, and only a few foundries can make a blade that survives.

<!--FIG:blade-->

The hotter the gas entering the turbine, the more power and the higher the efficiency. Mitsubishi Heavy says gas enters its M501J turbines at 1,600°C, 100°C hotter than its previous series. GE Vernova does not publish the figure for its HA units. A common single-crystal blade alloy, CMSX-4, starts to melt at about 1,340°C, according to published metallurgy studies. So the first row of blades sits in gas more than 200°C above its own melting point.

It survives on three things. First, **single-crystal casting**: the whole blade is grown from molten nickel alloy as one metal crystal. Ordinary metal is made of many small crystals, and at red heat the boundaries between them creep and crack. A blade with no boundaries lasts. Second, **cooling passages**: the blade is cast hollow around ceramic cores, and air from the compressor runs through it and out of rows of tiny holes, laying a cooler film over the surface. Third, a **thermal barrier coating**: a thin ceramic skin on a metal bond coat, which holds the heat off the metal. Mitsubishi Heavy says these keep the blade metal at the temperature of older, cooler turbines.

The US Department of Energy funded much of this in the 1990s. Before then, it says, above about 1,260°C "available cooling technologies were insufficient". Its programme pushed firing temperatures to about 1,430°C with single-crystal blades and coatings, and GE unveiled the first such H-class turbine in February 2000.

<a id="howmet-casts-the-queue"></a>

Few companies can cast these blades. The biggest is Howmet Aerospace, which also makes jet engine parts and calls itself "the largest manufacturer of gas turbine blades in the world". Its annual report names its rivals: Precision Castparts, owned by Berkshire Hathaway, plus Doncasters in Britain and Consolidated Precision Products. It also says several of its largest customers have their own furnaces. Siemens Energy is expanding its blade and vane plant in Tampa, Florida, in investments it says are "deliberately designed to avoid overcapacity" (my translation of its German release of 3 February 2026). Mitsubishi Heavy has set aside about ¥500 billion of investment for combined-cycle plants that "includes hot parts production capacity".

Demand shows in Howmet's results. Its gas turbine revenue was US$349 million in the third quarter of 2026, up 45 per cent on a year earlier, and US$954 million in the first nine months, up 41 per cent. On its results call, as transcribed by a third party, its chief executive said "2031 is now also sold out" and that new capacity "will take two years to install". GE Vernova's own chief executive said in July that he could "see clearly the castings and forgings arriving in '27" for its next step in output in 2028.

So the hottest blade sets the pace of every heavy turbine. A new casting line takes about two years to install, and the casters build only what is ordered. I have found no published figure for how long a new line takes to qualify with a turbine maker, and I will not guess one.

## Why don't the makers just build more factories?

Because they did exactly that twenty years ago, and the orders vanished.

<!--FIG:boom-chart-->

Around 2000, American power markets opened up and gas was cheap, and independent developers ordered gas turbines by the hundred. In EIA's generator inventory, about 69 GW of gas capacity entered service in 2002 alone, and about 238 GW across 2000 to 2005, by my sums. EIA says the boom "created excess generating capacity": combined-cycle plants built to run 50 to 70 per cent of the time ran about 34 per cent in 2003.

The makers had built for the boom, and then it stopped. On 16 November 2017 Siemens said world demand for large gas turbines had "fallen drastically" and would level out at about 110 a year, against manufacturing capacity of about 400. It cut about 6,900 jobs. On 7 December 2017 GE's power business cut about 12,000, blaming "overcapacity". American gas additions ran below about 11 GW in most years from 2006, and fell to 2.4 GW in 2024.

That memory explains how the makers are expanding now. GE Vernova plans to raise output from 20 GW a year to 24 GW in 2028 and 30 GW in 2030, through "lean and incremental machinery in our existing factory footprint". It says this is "all funded by customer down payments" and that the capital spending is "modest". By July it had installed 325 new machine tools in its gas factories, heading for about 400 by the end of 2026. It has announced no new heavy turbine factory.

Siemens Energy and Mitsubishi Heavy are doing the same. Siemens Energy's own investor slides show its large-turbine capacity rising from about 35 units a year to about 50 from its 2027 financial year. Mitsubishi Heavy plans to double its combined-cycle production capacity against its 2024 financial year. Each is expanding inside walls it already owns, paid for by buyers, so that a downturn cannot strand it again.

## How long is the queue at GE Vernova?

About six years of its present output, and it grew by almost half in nine months.

<a id="ge-vernova-sells-the-wait"></a>

GE Vernova reports two kinds of commitment. A **firm order** is a contract for a machine. A **slot reservation agreement** is a paid place in the production line that can later become a firm order, or lapse. Together they are its gigawatts **under contract**.

<!--FIG:queue-chart-->

At the end of 2025 GE Vernova had 83 GW under contract. By 30 September 2026 it had 122 GW: 64 GW of firm orders and 58 GW of reservations. At 20 GW a year, that rose from 4.2 to 6.1 years of output. It expects at least 130 GW by the end of 2026.

The queue grows because buyers sign faster than the factory ships. In the first nine months of 2026 GE Vernova signed 52 GW of new contracts and shipped about 13 GW. The 20 GW a year is the pace it reached in the third quarter, when it shipped 5.3 GW; calendar 2026 shipments will be nearer 18 GW, by my estimate.

The furthest slots are far out. In July GE Vernova said it was "mostly sold out through '30" and expected to have sold more than half of its 2031 slots by the end of the year. On 28 October it said "we sold multiple slots for 2032 delivery". A heavy unit then needs about 18 months on site to be installed and commissioned, its chief executive said in July. So a slot bought today makes power around 2034.

Even the planned expansion does not clear it. At 24 GW a year, 122 GW is about 5.1 years of output; at 2030's 30 GW, about 4.1 years. Those steps arrive in 2028 and 2030, the same years existing slots deliver, so they help nobody deciding today.

## Is the wait shorter at the other makers?

No. The other two big makers are booked into the 2030s as well.

<a id="a-second-maker-books-years-out"></a>

<!--FIG:makers-chart-->

Siemens Energy, the German maker, reported 69 GW of firm backlog and 26 GW of reservations at 30 June 2026: 95 GW on GE Vernova's definition. It booked 15 GW and shipped 6 GW in that quarter, according to its own investor slides. Its full-year results, due in mid-November 2026, were not out when this was written.

Mitsubishi Heavy reported on 6 November 2026. It booked 19 large gas turbines, 8 GW, in the six months to September, against 23 units, 10 GW, a year earlier. Its backlog of large units rose to 83, about 37 GW, from 74 in March. In August its finance chief said combined-cycle projects then under discussion "will generally be delivered around 2030 to 2031", and that "Order pricing has not declined".

Together the three hold about 250 GW under contract, by my sum of figures on different dates and definitions. Who is in the queue matters too. GE Vernova said about 20 per cent of its roughly 100 gas customers were data centre projects; that is a share of customers, not of gigawatts, and no maker gives the second. The rest are mostly utilities, which want the same machines for the same reason: demand for power is rising for the first time in decades.

So switching maker does not help. A campus can shop between three queues, but all three run to roughly the same years.

## What does a buyer pay to stand in the queue?

A large deposit up front, at a price per kilowatt that has risen by about half in a year.

GE Vernova's buyers pay before the metal is cut. In its Power segment, which holds gas turbines with its nuclear and hydro businesses, contract liabilities and current deferred income doubled from US$16.5 billion at the end of 2025 to US$33.2 billion at 30 September 2026. Its quarterly report ties the rise mainly to down payments on gas orders and reservations. Those deposits pay for the expansion, which is why the maker carries little risk if demand cools.

The price has risen too. GE Vernova expects orders placed in 2026 to be priced about 50 per cent higher per kilowatt than those of 2025. Its third-quarter orders were priced more than 20 per cent above those of the fourth quarter of 2025, partly because more were aeroderivatives, the quicker machines that cost more per kilowatt.

<!--FIG:cost-chart-->

The whole plant costs far more than it did. EIA's planning figure for a large combined-cycle plant is US$868 per kilowatt, in 2023 dollars, from a study it commissioned in 2024. The plants utilities are actually filing for cost roughly two to nearly three times that. Duke Energy's three new combined-cycle plants run from about US$1,620 to about US$2,340 per kilowatt, by my division of its filed figures. Williams' five on-site plants, including Socrates, come to about US$3,500 per kilowatt of all their expected capital. That figure is my arithmetic from a financing in which outside investors paid for 49 per cent, and it may include pipe.

The buyers keep signing anyway, because power is a small cost beside the chips. What they are buying is a date. A reservation is not power; it is a place in a line, and the price of the place rises as the line lengthens.

## Is there a faster machine?

Yes, several, and they are filling up too.

<a id="the-way-out-has-its-own-queue"></a>
<a id="crusoe-borrows-the-jet-engine"></a>

The first is the **aeroderivative**: a smaller gas turbine built around an aircraft jet engine. GE Vernova's LM2500XPRESS makes about 35 MW at about 38 per cent efficiency; its LM6000 makes up to about 58 MW at about 41 per cent and starts in five minutes. GE Vernova's chief executive said in July that an aeroderivative ships about 24 months before a heavy unit and needs about six months on site, against 18. The cost is fuel: a simple-cycle machine burns about 46 per cent more gas per unit of power than a combined cycle, on EIA's tested averages.

Campuses bought them first. Crusoe, which builds AI campuses, ordered 29 LM2500XPRESS units from GE Vernova in December 2024 and mid-2025, nearly 1 GW. Each leaves the factory about 95 per cent assembled.

<!--FIG:aero-chart-->

Now the fast lane has a queue of its own. In 2025 GE Vernova took orders for 63 aeroderivatives and shipped 27. In the first nine months of 2026 it took 127 and shipped 39. Since the start of 2025 it has taken orders for 124 more than it shipped, more than two years of its recent shipments. On 28 October its chief executive said fourth-quarter orders would be lighter, "not because the demand is softer" but because "we're now going out so far in the future before we have availability".

<a id="the-engines-queue-too"></a>

The second is the **reciprocating gas engine**: a very large version of a car engine, with pistons, running on gas. Wärtsilä's 50SG makes about 18.9 MW at 50 per cent efficiency and reaches full load in two minutes. Engines lose little power in heat and come in small blocks, so a campus can add them a few at a time. On 5 October 2026 Wärtsilä announced a 282 MW order for a US data centre, due for delivery in 2028 and fully running in 2029. It was the company's seventh data-centre order in America, taking its sales there above 3 GW, up from above 1.6 GW in April. On 27 October it said "lead times for our engines continue to increase". Caterpillar, the other big engine maker, sold US$3,421 million of power generation equipment in the third quarter, up 30 per cent, mostly for data centres.

The third is the **fuel cell**, which turns gas into electricity chemically, without burning it. Bloom Energy makes solid oxide fuel cells in boxes that can be added in steps. Its product revenue rose 179 per cent in the third quarter of 2026, to US$1,073.6 million. Oracle, the cloud company, intends to buy up to 2.8 GW from it, 1.2 GW of it contracted. Bloom is doubling its factory to 2 GW a year by the end of 2026.

The fourth is renting. Companies that once powered oilfields now rent gas turbines and engines to campuses. Solaris Energy Infrastructure had 3.2 GW under long-term contract after a 900 MW, 15-year deal announced on 4 November 2026. It said it had bought equipment "ahead of long OEM queues": that is, before the makers' lines filled.

<a id="the-product-is-time"></a>

What these sellers have in common is that they sell time. A buyer pays more per kilowatt, or burns more gas, to start sooner. Bloom's product margin was 37.9 per cent in the third quarter, against 35.0 per cent a year earlier, by my calculation. But it sat near 35 per cent for two years before that, so its buyers paid in volume, not in price.

I concede the fast lane is still faster. An engine ordered this year arrives in 2028, against 2032 for a heavy slot sold now. But the gap narrows as every campus takes the same shortcut: Wärtsilä's order runs about three years from signing to a running plant. The fast lane buys a year or three, not a decade.

## Why does an island campus build more machine than it uses?

Because with no grid behind it, the campus must carry its own spares, its own margin for heat and its own buffer for sudden swings. I hold this as a hypothesis, not yet a finding.

<a id="an-island-buys-its-own-bench"></a>

<!--FIG:island-->

On the grid, thousands of plants share the load. When one trips, the rest cover it within seconds, and spare capacity is shared across a whole region. An island campus has nobody else. It must keep at least one unit spare in case another fails, a rule engineers call N+1. It must allow for hot days: on Wärtsilä's comparison, an aeroderivative loses nearly 26 per cent of its output at 45°C against standard conditions, while an engine loses under 2 per cent. And it must absorb sudden changes in its own load.

Those changes are real and large. PJM recorded three events in which data centres switched to their own backup generators at once after a single fault on a high-voltage line: about 1,500 MW on 10 July 2024, about 1,800 MW on 17 February 2025 and about 3,900 MW on 22 July 2026, the largest yet. On the grid, other plants absorbed the drop. An island would have to absorb it alone, usually with a large battery: every big island design I have found pairs its machines with batteries.

Socrates is the one dated point. Williams' annual report, filed in February 2026, said the project would give its customer "a combined 400 megawatts". Its quarterly reports since May say the two plants "together have an expected 556 MW of capacity". That is 1.39 MW built for each MW committed, by my arithmetic. Williams does not say why. An executive of another planned Texas campus told a trade publication its first engine fleet could need about 30 per cent more machine than load; that is press, not a filing.

If that holds, each megawatt of island load draws more than a megawatt from the makers' queues. 122 GW under contract would then serve fewer campus megawatts than it seems. The test is to set installed against committed capacity at every off-grid site I can date. If island sites run near one to one, or keep a grid tie as their spare, the margin is small and the idea is wrong.

## How much gas does a campus burn, and where does it come from?

A gigawatt campus burns about as much gas a day as a small city, and America has plenty; the limit is the pipe that carries it.

<!--FIG:gas-chart-->

Gas is measured in **billion cubic feet a day** (Bcf/d). At EIA's tested heat rates for 2025, one gigawatt running flat out burns about 0.175 Bcf/d in combined cycle, 0.205 in gas engines and 0.254 in simple-cycle turbines, by my arithmetic. A data centre runs close to flat out all year, which makes it a steady pipeline customer rather than an occasional one. All of America's power plants burned 35.8 Bcf/d in 2025.

<a id="permian-gas-follows-the-oil-rig"></a>

Much of the new gas comes from the Permian, the oil basin of west Texas and New Mexico. There it is **associated gas**: it comes up the same wells as the oil, whether or not anyone has a pipe for it. Drillers chase oil, and EIA says the basin's gas-to-oil ratio has risen 15 per cent since 2021. Permian marketed gas rose from 26.3 Bcf/d in the first quarter of 2025 to an estimated 30.2 Bcf/d in the third quarter of 2026. Over the same year the number of drilling rigs barely moved: 264 in the third quarter of 2026 against 258 a year earlier, on EIA's estimates.

The proof that the pipe, not the gas, is the limit is the price at Waha, the trading hub in west Texas where Permian gas is priced before it leaves the basin. When the pipes out are full, producers must pay buyers to take the gas, because shutting oil wells to stop it costs more. In May 2026 EIA said Waha spot prices had "averaged below zero for eight of the last nine months". In Appalachia, EQT, America's largest gas producer, held back 21 billion cubic feet equivalent of output in the third quarter for the same reason. Gas is plentiful at the well; the shortage is the pipe.

<a id="golden-pass-joins-the-gas-queue"></a>

Campuses also share the pipes with export terminals. **Liquefied natural gas** (LNG) is gas cooled to a liquid for shipping overseas. America exported 15.1 Bcf/d of it in 2025. Golden Pass LNG on the Texas coast shipped its first cargo on 22 April 2026, and when complete its three units will take about 2 Bcf/d. Texas's terminals take a steady 4 to 5 Bcf/d all year, about as much as the state's power plants burn in mild months. In February to April 2026, as in spring and late autumn 2025, they took more.

## How long does it take to build the pipe?

About four years for a short expansion beside an existing line, and longer for a new one across the country.

A new interstate pipe follows a fixed sequence. First comes an **open season**, when the pipeline company offers new capacity to all comers. Shippers that want it sign **precedent agreements**, binding contracts to take capacity once it is built. Most are **take-or-pay**: the shipper pays a fixed monthly charge for its booked space whether or not it sends any gas. Only then does the company apply to FERC for a certificate under the Natural Gas Act. It also needs water permits from the Army Corps of Engineers and the states, and only then does it build.

Transco's Southeast Supply Enhancement, an expansion of Williams' big East Coast pipeline, shows the timing. Its open season ran from 19 June to 14 July 2023. Williams applied to FERC on 29 October 2024 and won its certificate in January 2026. It targets gas flowing as early as the third quarter of 2027. That is about four years for 55 miles of new pipe laid beside an existing line, plus work at eight compressor stations. Duke Energy, Southern Company and Santee Cooper, three power companies, signed 93 per cent of its capacity, to fuel their own plants.

New long-distance lines take longer. Kinder Morgan, another pipeline company, decided in October 2026 to build Permian Link, about 434 miles and about 2.8 Bcf/d. It will serve new power generation for an "A-rated hyperscaler" from the third quarter of 2030, and its contracts are take-or-pay. That pipe could fuel about 16 GW of combined cycle, by my arithmetic, though Kinder Morgan does not say the hyperscaler takes all of it. More than 75 per cent of Kinder Morgan's US$14.4 billion project backlog supports power generation and local gas utilities.

The pipes are being signed for campuses directly. Energy Transfer, a Texas pipeline company, contracted about 900 million cubic feet a day to three Oracle data centres. It also signed a 20-year deal to carry gas to Entergy's plants for Meta's Hyperion campus from December 2028. Its new Hugh Brinson pipe out of the Permian went into full service on 1 September 2026.

Federal rules have eased; the courts and states have not. FERC removed a rule in October 2025 that had stopped construction while appeals were pending. But on 8 September 2026 a federal appeals court cancelled New Jersey's water approval for another Williams pipe. Even the compressors that push gas along are queuing behind the power plants. On 5 May 2026 USA Compression said some engine lead times had "tripled from 50 weeks to approximately 150 weeks", adding "It's the generator orders".

## Does a campus need a permit to burn the gas?

Yes, an air permit, and it can decide whether the plant is built at all.

A gas plant emits **nitrogen oxides** (NOx), gases that help form smog. Under the Clean Air Act a plant whose emissions pass set thresholds, typically 100 or 250 tons a year depending on the plant and the area, is a major source. It then needs a full review before construction, with the strictest controls and, in areas with poor air, offsets: cuts elsewhere bought to cover its own.

<a id="homer-city-inherits-the-air"></a>

Homer City shows how a big plant got through. Homer City Generation, a developer, is building up to 4,678 MW of gas plant on the site of a Pennsylvania coal plant that closed in 2023. It uses seven GE Vernova 7HA.02 combined-cycle units and ten Mitsubishi aeroderivatives. Its new plant adds 1,142.8 tons of NOx a year. Retiring the coal boilers removed 2,031.8 tons, and Pennsylvania let it **net** the one against the other, so it avoided the full review. A cut counts only within five years, so a coal site shut long ago has none to spend. Homer City targets first power in early 2028.

Texas has gone the other way. At the governor's direction, the Texas Commission on Environmental Quality, the state's air regulator, wrote on 19 October 2026 that it "has paused the issuance of all permits" for building infrastructure that directly supports data centres. Where possible it is also suspending the lighter authorisations that need no permit to be issued. Texas is where many of the largest island campuses are planned.

The best-known case is still in court. xAI, Elon Musk's AI company, ran gas turbines at its Memphis campus and at a power plant across the state line in Mississippi, describing many of them as temporary. On 30 October 2026, according to Earthjustice, which represents the plaintiffs, a federal court held that the Mississippi plant is not an exempt "mobile source". I have not read the order, and the case continues. Federal rules on temporary turbines remain unsettled: a rule of January 2026 created a route for them that does not yet apply.

So the permit is a clock of its own. For a plant on an old coal site with fresh cuts to net, it can be quick. For a new site in a state that has paused permits, it is now open-ended.

## Does going through the utility avoid the queue?

No. A utility building gas plants for a campus stands in the same turbine queue, on the same clock.

<a id="hyperion-the-plant-outlasts-the-lease"></a>

Meta's Hyperion campus in Louisiana is the largest example. In August 2025 Louisiana's regulator approved three gas plants, 2,262 MW in all, that Entergy Louisiana, the state's utility, will build for it, for service in 2028 and 2029. A second agreement, signed in March 2026, adds seven combined-cycle plants, 5,278 MW, for 2030 and 2031. Its vote is set for December 2026.

The utility route moves the risk rather than removing it. Meta's power agreement with Entergy carries minimum charges and an exit fee. The campus itself, majority owned by funds of Blue Owl, an investment firm, is leased to Meta from 2029 for four years, renewable to 20, according to Meta's annual report. So the plants are built to last decades for a tenant committed to four years, and the charges are what protect the utility's other customers.

The utility gains one thing: it can spread spare capacity across its whole system, so it does not need an island's extra machines. But it buys its turbines from the same three makers. Entergy's first plants arrive in 2028, and its second set in 2030 to 2031, the years the makers have already sold.

## So how long does each route take, from start to finish?

The fast routes take a year or two and deliver a few hundred megawatts; the gigawatt routes run to 2028 and beyond, and a turbine slot sold today arrives last.

<!--FIG:routes-->

Socrates is the fastest dated route: about fourteen months from approval for its second plant, 556 MW in all. Williams has four more plants, 2,032 MW, due from the second half of 2027 to the second half of 2028. It warns that "All expected in-service dates assume timely receipt of permits". Homer City targets early 2028, Hyperion's first Entergy plants 2028 and 2029, and Wärtsilä's engines 2029. The gas comes on similar dates: Transco's expansion from 2027, Permian Link from late 2030. A heavy turbine slot sold today ships in 2032 and runs about 18 months later.

So own power is fast for the first few hundred megawatts and slow for the next gigawatt. Headlines show the first. Whether it beats a comparable grid connection is still open. EIA's generator survey covers only plants "connected to the local or regional electric power grid", so off-grid plants such as Socrates are not counted, and the head-to-head cannot be measured from it.

## Are there signs the queue is starting to clear?

Some, and they are the strongest evidence against this piece.

<a id="plans-outrun-the-build"></a>

GE Vernova's signings fell to 11 GW in the third quarter of 2026, from about 20 GW in each of the two quarters before, while its shipments rose. Mitsubishi Heavy booked fewer large units in the half year than a year earlier. And all three makers are adding capacity. If signings keep falling while output climbs to 30 GW, the queue measured in years will shorten.

Three points hold for now. The pile shrinks only when signings fall below shipments, and 11 GW a quarter is 44 GW a year, above even the 30 GW planned for 2030. The queue is also hardening: in the third quarter 13 GW of reservations became firm orders, so firm orders now exceed reservations. And the plans still outrun the building. In EIA's generator inventory, planned gas capacity rose from 40.5 GW in September 2025 to 71.1 GW in September 2026. The part under construction or built rose only from 9.6 GW to 13.1 GW, by my arithmetic.

The new capacity also arrives late. Siemens Energy's step lands from its 2027 financial year, GE Vernova's in 2028 and 2030, Mitsubishi Heavy's over several years. A campus deciding today gains nothing from it.

## So who holds the scarce thing, and what should an investor watch?

The scarce things are places in the heavy turbine lines and the capacity to cast their hottest blades. The pipe and the permit come next.

**The turbine makers** hold the first. GE Vernova, Siemens Energy and Mitsubishi Heavy are paid deposits before they cut metal, at prices that have risen by about half in a year. They expand only inside their existing factories. Their risk is the one they remember from 2002: signings falling just as new capacity arrives.

**The blade casters** hold the second. Howmet and Precision Castparts sell into every step of every maker's expansion, and Howmet says its new capacity is sold out years ahead. Their constraint is time: about two years to install a casting line.

**The sellers of time** hold the shortcut. Aeroderivative and engine makers, Bloom's fuel cells and the rental fleets are paid to deliver sooner, in volume more than in price. Their lead is narrowing as their own lines fill.

**The pipelines** hold the fuel. Kinder Morgan, Williams and Energy Transfer sign take-or-pay contracts before they build, so they are paid whether or not the campus runs. Williams has gone further and builds the power plants itself.

The signals to watch are dated. GE Vernova's gigawatts under contract each quarter, starting with at least 130 GW at the end of 2026. Its aeroderivative orders against shipments in each filing. Whether its 24 GW step lands in 2028, and whether any maker announces a new heavy turbine factory. Socrates North's start, and whether Williams' next four plants get their permits on time. The Texas permit pause, and whether it ends after the state's audits. And installed against committed capacity at every island campus that publishes both.

## What would prove me wrong

Two tests break the claim, and both are dated to the end of 2027.

The first is the pile. If GE Vernova reports fewer gigawatts under contract at 31 December 2027 than at 31 December 2026, buyers are no longer joining the queue faster than the factory clears it. The first reading is the end of 2026, expected at 130 GW or more.

The second is the fast lane. Since the start of 2025 GE Vernova has taken orders for 124 more aeroderivatives than it shipped. If by the end of 2027 that backlog is no larger than its shipments in 2027, the shortcut has room again.

Some events would move me before either test. A new heavy turbine factory announced by any of the three makers would signal they expect demand to outlast the queue. A steady fall in signings below 5 GW a quarter, with reservations lapsing, would mean the queue is draining. And island campuses running at about one megawatt of machine per megawatt of load would kill my hypothesis that islands draw extra from the queue.

Two things would not move me. More fast signings of a few hundred megawatts: they are the exception the headlines show, not the gigawatt route. And price rises: they show the queue holding, not clearing.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

**Building your own power** (CLAIM_DATE)

Claim: "CLAIM_TEXT"

Breaks if: "BREAKS_TEXT"

EARLIER_CLAIMS

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

**The machines.** GE Vernova 7HA product pages (read 7 November 2026): 7HA.02, 384 MW simple cycle at 42.6% (heat rate 8,009 Btu/kWh); 7HA.03, 430 MW at 43.3% (7,884), ramp 75 MW a minute, about 640 MW in a one-on-one combined cycle. Siemens Energy HL-class fact sheet (2021): SGT6-9000HL 440 MW, more than 43.2%, pressure ratio more than 24:1, exhaust 675°C; combined cycle 655 MW one-on-one, more than 64%. Mitsubishi Heavy M501JAC: 453 MW at 44.0%, 664 MW one-on-one at more than 64%; turbine inlet temperature 1,600°C, "100°C higher than that of the G Series". Efficiency is 3,412 divided by heat rate. EIA Electric Power Annual, Table 8.2, average tested heat rates for natural gas, 2025: combined cycle 7,535 Btu/kWh, gas turbine 10,975, internal combustion 8,853. GE Vernova LM2500XPRESS about 35 MW, about 38.4%; LM6000 PF+ up to about 58 MW by variant, up to about 41.3%, five-minute start. Wärtsilä 18V50SG: 18,875 kW at 60 Hz, 50.0% efficiency, full load in two minutes (product leaflet). Heat derate: Wärtsilä's engines-versus-aeroderivatives comparison, at 45°C against ISO reference conditions.

**The blade.** CMSX-4 solidus about 1,339°C, from published metallurgy studies (for example, the Bundesanstalt für Materialforschung study of CMSX-4, Crystals 11, 152, 2021); not a maker's figure. US Department of Energy, "Breakthrough Gas Turbines": before its programme, above about 2,300°F (1,260°C) "available cooling technologies were insufficient"; it "pushed firing temperatures to 2,600 degrees F" (1,430°C) with single-crystal blades and thermal barrier coatings; GE unveiled its H System on 18 February 2000. Howmet 2025 Form 10-K (12 February 2026): rivals named; "Several of Howmet's largest customers have captive superalloy furnaces"; gas turbines about 11% of revenue in 2025. Howmet Form 10-Q for the third quarter of 2026: gas turbine revenue US$349m against US$241m; nine months US$954m against US$678m. Howmet's call of 29 October 2026, third-party transcript: "2031 is now also sold out"; new capacity "will take two years to install". GE Vernova's own transcript of 22 July 2026: "castings and forgings arriving in '27"; 325 machines installed in its gas factories, about 400 by year end. Siemens Energy release of 3 February 2026 (German): Tampa blades and vanes; "bewusst so ausgelegt, dass Überkapazitäten vermieden werden", my translation. Mitsubishi Heavy first-half results presentation, 6 November 2026: growth investment "GTCC: Includes hot parts production capacity, Approx. ¥500 bn"; "Double GTCC new unit production capacity".

**The boom.** EIA Preliminary Monthly Electric Generator Inventory (Form EIA-860M), September 2026, Operating and Retired sheets, energy source natural gas, nameplate MW summed by year entered service, my sums: 1998 2.2 GW; 1999 9.4; 2000 30.2; 2001 43.4; 2002 68.6; 2003 53.8; 2004 25.0; 2005 17.1; 2006 10.2; 2010 7.5; 2018 21.7; 2023 9.9; 2024 2.4; 2025 5.3; 2026 to September 3.7. Plants retired before the inventory's coverage are missing, so early years are slight undercounts. EIA Today in Energy (7 June 2011): the boom "created excess generating capacity"; plants intended to run 50 to 70% of the time ran about 34% in 2003. Siemens release of 16 November 2017: demand "expected to level out at around 110 turbines a year", capacity "around 400"; about 6,900 jobs. GE Power release of 7 December 2017: "approximately 12,000 positions"; "overcapacity". Siemens Energy Q3 FY2026 analyst presentation (5 August 2026), page 5: large gas turbine capacity about 35 units a year in FY2025 and FY2026, about 50 from FY2027, read from chart labels.

**GE Vernova's queue.**

| Quarter end | Firm orders | Reservations | Under contract | Signed | Shipped | Years of 20 GW |
|---|---|---|---|---|---|---|
| Dec 2025 | 40 GW | 43 GW | 83 GW | | | 4.2 |
| Mar 2026 | 44 GW | 56 GW | 100 GW | 21 GW | 4 GW | 5.0 |
| Jun 2026 | 53 GW | 63 GW | 116 GW | 20 GW | 3 GW | 5.8 |
| Sep 2026 | 64 GW | 58 GW | 122 GW | 11 GW | 5 GW | 6.1 |

Sources: GE Vernova results releases of 22 April, 22 July and 28 October 2026; years of output are my arithmetic. Third quarter: "Signed 11 gigawatts (GW) of new gas equipment contracts, including 8 GW of slot reservation agreements and 3 GW of orders. Converted 13 GW of existing slot reservation agreements to orders and shipped 5 GW". Form 10-Q to 30 September 2026: gas turbine sales 5.3 GW in the quarter and 12.8 GW in nine months; Power contract liabilities and current deferred income US$33,163m against US$16,527m at 31 December 2025. Calls: "mostly sold out through '30" (22 July 2026); "we sold multiple slots for 2032 delivery"; about 100 gas customers in 25 countries, about 80% traditional and 20% data centre projects, in its own words; 2026 gas orders priced "approximately 50% higher" per kilowatt than 2025's; third-quarter orders "more than 20% above 4Q 2025" (28 October 2026). Heavy unit "could take another 18 months at site after it's actually shipped"; aeroderivative commissioning "could be six months"; shipments "24 months apart" (22 July 2026).

**The other makers.** Siemens Energy Q3 FY2026 analyst presentation, page 6: "15 GW booked (12 GW converted from SRAs), 6 GW shipped"; "69 GW backlog / 26 GW SRAs". Mitsubishi Heavy first-half FY2026 presentation (6 November 2026): large frame gas turbine orders 19 units (8 GW) against 23 (10 GW) a year earlier; backlog 83 units (37 GW) against 74 (33 GW) at March 2026. Mitsubishi Heavy Q&A of 6 August 2026: "will generally be delivered around 2030 to 2031"; "Order pricing has not declined"; capacity "expected to double" against FY2024. The three makers' total, about 254 GW, is my sum across different dates and definitions.

**Plant cost.** EIA capital cost study for AEO2025 (Sargent & Lundy, January 2024), 2023 dollars: H-class two-on-one combined cycle, 1,227 MW, US$868/kW; one-on-one, 627 MW, US$921; H-class simple cycle, 419 MW, US$836; four aeroderivatives, 211 MW, US$1,606. Duke Energy Form 10-Q to 30 September 2026: Cayuga, two combined-cycle units, 1,476 MW, about US$3.3bn plus financing, about US$2,240/kW; Anderson County, 1,365 MW, about US$3.2bn with financing, about US$2,340/kW; Person County unit 2, 1,360 MW, about US$2.2bn with financing, about US$1,620/kW; divisions mine. ProPetro Form 8-K, 28 October 2026: about US$1.4m to US$1.5m per MW including balance of plant. Williams Form 8-K, 13 July 2026: outside investors committed US$5.34bn for 49% of its five power projects, US$4.4bn of it equal to 49% of expected growth capital, so about US$9.0bn in all, or about US$3,500 per kW of 2,588 MW, my arithmetic.

**Aeroderivatives.** GE Vernova 2025 Form 10-K and Form 10-Q to 30 September 2026: 63 ordered and 27 shipped in 2025; 127 ordered and 39 shipped in January to September 2026; ordered less shipped since 1 January 2025, 124 units, my arithmetic. Crusoe and GE Vernova, 22 July 2025: 29 LM2500XPRESS units, ten ordered in December 2024 and 19 in June 2025, each about 95% assembled at the factory.

**Engines, fuel cells and rental fleets.** Wärtsilä releases of 16 April 2026 (412 MW in Ohio, fourth US data-centre order, more than 1.6 GW sold) and 5 October 2026 (282 MW, 15 engines, delivery 2028, fully operational 2029, seventh order, more than 3 GW sold); interim report of 27 October 2026. Caterpillar Form 10-Q, third quarter of 2026: Power Generation sales US$3,421m against US$2,634m, primarily in data centre applications for the nine months, it said. Bloom Energy release of 22 October 2026: product revenue US$1,073.6m, up 179.4%; product margin 37.9% against 35.0%, my computation; 36.8% in 2024, 35.2% in 2025. Oracle "intends to procure up to 2.8 GW", 1.2 GW contracted (Bloom, April 2026). Bloom 2025 Form 10-K: factory capacity to 2 GW a year by the end of 2026. Solaris Energy Infrastructure, 4 November 2026: about 900 MW, 15 years; 3.2 GW long-term contracted; "Procured time-advantaged equipment ... ahead of long OEM queues".

**Islands.** Williams 2025 Form 10-K (24 February 2026): "a combined 400 megawatts of onsite power generation capacity to the customer"; Forms 10-Q of 4 May and 2 November 2026: "together have an expected 556 MW of capacity"; Socrates South "placed into service in late July 2026"; Socrates North "expected to be placed into service later in the fourth quarter of 2026", and "on track for in-service by mid-November" in the release of 2 November 2026. Ohio Power Siting Board case 25-188-EL-BGN, 18 September 2025. PJM Planning Committee, 6 October 2026, large load ride-through background: about 1,500 MW (10 July 2024), 1,800 MW (17 February 2025) and 3,900 MW (22 July 2026) of data-centre load "transferred to backup generation" after normally cleared faults. The 30% figure: a Prometheus Hyperscale executive to a trade publication (press). FERC, PJM co-location order, 193 FERC ¶ 61,217 (18 December 2025, EL25-49), and rehearing order 195 FERC ¶ 61,209 (18 June 2026). Texas Senate Bill 6 (2025): large loads must disclose on-site backup generation, which the grid operator may direct to deploy in an emergency.

**Gas.** One gigawatt for a day: 1,000,000 kW × 24 h × heat rate ÷ 1,036 Btu per cubic foot (EIA, 2025), my arithmetic. EIA Short-Term Energy Outlook, 6 October 2026: dry production 107.6 Bcf/d in 2025; LNG exports 15.1; power sector consumption 35.8. Permian, Tables 5a and 10a: rigs 302, 258, 242 and 264, and marketed gas 26.3, 28.3, 28.4 and 30.2 Bcf/d, in the first and third quarters of 2025 and 2026, the last an estimate. EIA STEO, September 2026: gas-to-oil ratio "nearly 4,200 cubic feet per barrel in 2025, 15% higher than in 2021"; May 2026: Waha "averaged below zero for eight of the last nine months". EQT release of 27 October 2026: 21 Bcfe curtailed in the third quarter. EIA Today in Energy, 23 April 2026: Golden Pass first cargo 22 April 2026, three trains, about 2.0 Bcf/d nominal. Texas LNG exports against Texas power burn, EIA monthly data released 30 October 2026: LNG larger in March, April, November and December 2025 and February to April 2026. EIA STEO, September 2026: Texas has paused the connection of new data centres to the grid "to facilitate a regulatory audit"; 2027 Texas load growth forecast cut from 14% to 6%.

**Pipes.** Transco Southeast Supply Enhancement, FERC docket CP25-10: application 29 October 2024; open season 19 June to 14 July 2023; 1,596,900 Dth a day; Duke, Southern and Santee Cooper 1,480,000 Dth a day, 93%, my arithmetic; certificate January 2026 and service "as early as the third quarter of 2027" (Williams Form 10-Q, 2 November 2026). Kinder Morgan, 21 October 2026: Permian Link about 2.8 Bcf/d and about 434 miles, for "new power generation for an A-rated hyperscaler", third quarter of 2030; backlog US$14.4bn, "More than 75%" supporting power generation and local distribution company demand. Energy Transfer releases of 5 November 2025 (about 900 MMcf a day to three Oracle data centres; 250,000 MMBtu a day for 20 years to Entergy Louisiana in Richland Parish, from December 2028) and 3 November 2026 (Hugh Brinson Phase I "placed into full service" 1 September 2026). FERC Order No. 915 (October 2025). Williams Form 10-Q, 2 November 2026: Third Circuit vacated New Jersey's water quality certification for Northeast Supply Enhancement, 8 September 2026. USA Compression call, 5 May 2026 (company transcript).

**Permits.** Pennsylvania DEP plan approval 32-00457A, 18 November 2025: NOx 1,142.8 tons a year added, 2,031.8 removed by retiring the coal units, on a 2021 to 2022 baseline. Homer City release of 26 March 2026: "first power in early 2028"; EIA's September 2026 inventory lists its first units for July 2028. Major source thresholds: 40 CFR 52.21(b)(1) and 40 CFR 70.2. Texas Commission on Environmental Quality, letter to the governor, 19 October 2026. Earthjustice release, 30 October 2026, on the Northern District of Mississippi's ruling on xAI's Southaven plant (party source; order not read). EPA final rule on stationary combustion turbines, 15 January 2026.

**Hyperion.** Louisiana Public Service Commission approval, August 2025 (docket U-37425): three plants, 2,262 MW, 2028 and 2029. Entergy Form 10-Q, 31 July 2026: second agreement, seven combined-cycle plants, 5,278 MW, 2030 and 2031, vote set for December 2026. Meta 2025 Form 10-K: minimum charges and exit fee; lease from 2029 for four years, renewable to 20.

**Routes chart.** Starts: Socrates North's siting approval (18 September 2025); Williams' financing of its five projects (13 July 2026); Homer City's air permit (18 November 2025); Hyperion's approval (August 2025); Wärtsilä's booking (third quarter of 2026); the second Entergy deal's signing (March 2026); Transco's open season (July 2023); Permian Link's sanction (21 October 2026); GE Vernova's call (28 October 2026). Ends are the dates each owner gives; years given without a month are placed mid-year.

**Plans against building.** EIA-860M "Planned" sheet, natural gas, all states: 40,482 MW in September 2025 and 71,102 MW in September 2026; under construction or complete (statuses U, V and TS) 9,569 MW and 13,146 MW, my sums.

</details>

<section class="exposure">
<h3>Who is exposed if building your own power means joining the makers' queues</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>Heavy turbines</dt>
<dd><span class="names">GE Vernova</span>, <span class="names">Siemens Energy</span> and <span class="names">Mitsubishi Heavy</span> make heavy gas turbines.</dd>
<dt>Blades</dt>
<dd><span class="names">Howmet Aerospace</span>, <span class="names">Precision Castparts</span> (Berkshire Hathaway), <span class="names">Doncasters</span> and <span class="names">Consolidated Precision Products</span> cast turbine blades and vanes.</dd>
<dt>The quicker machines</dt>
<dd><span class="names">GE Vernova</span> makes aeroderivatives; <span class="names">Wärtsilä</span> and <span class="names">Caterpillar</span> make gas engines; <span class="names">Bloom Energy</span> makes fuel cells; <span class="names">Solaris Energy Infrastructure</span> and <span class="names">ProPetro</span> rent power fleets.</dd>
<dt>Plants and campuses</dt>
<dd><span class="names">Williams</span> builds off-grid gas plants; <span class="names">Entergy</span> and <span class="names">Duke Energy</span> build utility plants; <span class="names">Homer City Generation</span> and <span class="names">Crusoe</span> build campuses with their own power.</dd>
<dt>Gas and pipes</dt>
<dd><span class="names">Kinder Morgan</span>, <span class="names">Williams</span> and <span class="names">Energy Transfer</span> run gas pipelines; <span class="names">EQT</span> produces gas.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>AI campuses counting on their own gas power as a fast route to gigawatts, and anyone reading a reserved turbine slot as power on a date.</dd>
</dl>
</section>

---

<p class="sources">Sources: GE Vernova releases, calls, Form 10-K and Forms 10-Q to 28 October 2026; Siemens Energy (3 February and 5 August 2026); Mitsubishi Heavy Industries (6 August and 6 November 2026); Howmet Aerospace filings and call to 29 October 2026; Wärtsilä, Caterpillar, Bloom Energy, Solaris and ProPetro releases and filings to 4 November 2026; Williams, Kinder Morgan, Energy Transfer, EQT, Duke Energy, Entergy and Meta filings; EIA data and outlooks to October 2026; FERC, PJM, Pennsylvania DEP and the Texas Commission on Environmental Quality; US Department of Energy. Leads came from Leo Cui's videos on GE Vernova and the energy sector. Personal research, not investment advice.</p>
