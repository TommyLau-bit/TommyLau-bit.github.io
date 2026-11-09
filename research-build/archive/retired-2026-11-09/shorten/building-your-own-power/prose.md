<a id="building-your-own-power"></a>

In late July 2026 a gas power plant in New Albany, Ohio, began feeding a Meta data centre with no grid connection between them. Williams, best known for running America's largest gas pipeline, built and runs it. Called Socrates, it is the clearest case of an AI campus making its own power. Its second half was approved in September 2025 and was due to run about fourteen months later.

That speed is the exception, and the reason sits in a factory in South Carolina. At the end of September 2026 GE Vernova, which makes many of the heavy gas turbines that power stations are built around, had 122 gigawatts of them under contract. It ships about 20 gigawatts a year. It is now selling places in its production line for 2032.

That is the claim of this piece. Building your own power does not skip the queue. It changes which queue you stand in: the grid's waiting list becomes the turbine makers', which at GE Vernova is about six years long and still growing. The quicker machines are filling too, and the gas pipe and the air permit have clocks of their own.

To see why, the piece follows the questions in order. Why campuses build their own power, and what that means. How a gas turbine works, and why its hottest blade is so hard to make. Why the makers will not simply build more factories, how long their queues are, and what buyers pay to stand in them. Then the quicker machines, why an island campus builds more machine than it uses, where the gas comes from, how long a pipe and a permit take, and whether going through the utility avoids it all. Finally, whether the queue is starting to clear, and what would prove me wrong.

{{ANALOGY}}

## Why are AI campuses building their own power stations?

Because the grid cannot connect them fast enough, and a campus that waits years for power earns nothing from the chips inside it.

A large AI campus needs hundreds of megawatts, and some plan several gigawatts. A **megawatt** (MW) is a million watts, about the power drawn by a few hundred homes at once; a **gigawatt** (GW) is a thousand megawatts, about the output of one large power station. Few points on America's grid have that much spare capacity, so a campus usually needs new lines, new substations and often new power stations behind them. The wait for that is set out in [America rations the plug](/journal/america-rations-the-plug/); in many regions it runs to years.

Some states have gone further than a queue. On 3 August 2026 the governor of Texas told the state's grid operator and utility regulator to pause approvals for data centres waiting to connect until each had been audited. The audit has no end date. In its outlook the following week, the Energy Information Administration (EIA), the government's energy statistics office, cut its forecast for Texas power demand growth in 2027 from 14 per cent to 6 per cent.

The chips do not wait. An AI accelerator loses value every year it sits unpowered, as newer chips arrive, and a campus is financed on the date it starts earning. So the owners asked a simple question: if the grid cannot bring power in, why not make it on site?

America has the fuel to do it. It produced 107.6 billion cubic feet of natural gas a day in 2025, the most in the world, and gas pipes already cross most of the country. A gas plant beside the building turns that gas into electricity without waiting for a high-voltage line. That is the way out this piece follows.

## What does "your own power" actually mean?

It means generating electricity on the campus's side of the utility's meter, either alongside a grid connection or with none at all.

Power made on the customer's side of the meter is called **behind the meter**: a well of one's own beside the water main. Behind-the-meter power comes in three forms.

**Islanded** means no grid connection at all: the campus's plant is its only supply, as at Socrates. **Bridging** means own power that runs until the grid connection arrives, then becomes backup or is removed. **Co-located with a grid tie** means a plant beside the campus that also connects to the grid, so each can lean on the other.

The rules treat them differently. In December 2025 the Federal Energy Regulatory Commission (FERC), which oversees wholesale power markets and interstate gas pipes, ruled that PJM, the grid operator for thirteen states and Washington DC, must limit how much of a large new load can be netted against its own generation on site. Texas law now lets its grid operator order a large campus's backup generators on, or its load off, in an emergency. So an islanded campus escapes those grid rules, at the price of carrying every risk itself.

Whichever form it takes, own power needs four things. A machine to burn the gas, a pipe to bring it, an air permit to burn it, and, for an island, enough spare machines to keep running when one fails. Each comes with its own queue. The machine's is the longest, so the piece starts there.

## How does a gas turbine turn gas into electricity?

It works like a jet engine bolted to the ground: it squeezes air, burns gas in it, and lets the hot gas spin a shaft that drives a generator.

{{FIG1}}  <!-- A gas turbine is a jet engine on the ground; a combined cycle adds a steam loop to use its waste heat -->

A **gas turbine** has three parts on one shaft. The **compressor** at the front squeezes incoming air to about 24 times atmospheric pressure. In the **combustor**, gas burns in that air at a very high temperature. The hot, high-pressure gas then rushes through the **turbine**, a set of bladed wheels it spins on the way out. The turbine turns the compressor and also a **generator**, which makes the electricity.

Run that way alone, it is a **simple-cycle** plant. Its exhaust leaves at about 670°C and goes up a chimney, wasting much of the heat. A **combined-cycle** plant puts that exhaust through a boiler to make steam, which drives a second, steam turbine. Same gas, about half as much electricity again.

The difference shows in the **efficiency**: the share of the gas's energy that ends up as electricity. GE Vernova's largest unit for America's 60-hertz grid, the 7HA.03, makes 430 MW in simple cycle at 43.3 per cent efficiency. Paired with a steam turbine, the same unit makes about 640 MW. Siemens Energy's SGT6-9000HL and Mitsubishi Heavy Industries' M501JAC, its two big rivals, quote more than 64 per cent in combined cycle.

Engineers measure this as the **heat rate**: the fuel burned to make one kilowatt-hour, in British thermal units (Btu). Lower is better. A kilowatt-hour holds 3,412 Btu of energy, so a heat rate of 7,884 means 43.3 per cent efficiency. EIA's tested average for America's combined-cycle plants in 2025 was 7,535 Btu per kilowatt-hour; for simple-cycle turbines it was 10,975.

So the combined cycle burns about 30 per cent less gas for each unit of power. It also needs a boiler, a steam turbine, cooling and more steel, which add time on site. That trade between fuel and speed runs through the rest of this piece.

## Why is the hottest blade the hardest part to make?

Because the gas that hits it is hotter than the metal can stand, and only a few foundries can make a blade that survives.

{{FIG2}}  <!-- The gas is hotter than the blade alloy's melting point, so the blade lives on its crystal, its cooling and its coat -->

The hotter the gas entering the turbine, the more power and the higher the efficiency. Mitsubishi Heavy says gas enters its M501J turbines at 1,600°C, 100°C hotter than its previous series. GE Vernova does not publish the figure for its HA units. A common single-crystal blade alloy, CMSX-4, starts to melt at about 1,340°C, according to published metallurgy studies. So the first rows of vanes and blades sit in gas more than 200°C above the melting point of a typical blade alloy.

It survives on three things. First, **single-crystal casting**: the whole blade is grown from molten nickel alloy as one metal crystal. Ordinary metal is made of many small crystals, and at red heat the boundaries between them creep and crack. A blade with no boundaries lasts. Second, **cooling passages**: the blade is cast hollow around ceramic cores, and air from the compressor runs through it and out of rows of tiny holes, laying a cooler film over the surface. Third, a **thermal barrier coating**: a thin ceramic skin on a metal bond coat, which holds the heat off the metal. Mitsubishi Heavy says these keep the blade metal "at the level of conventional gas turbines".

The US Department of Energy funded much of this in the 1990s. Before then, it says, above about 1,260°C "available cooling technologies were insufficient". Its programme pushed firing temperatures to about 1,430°C with single-crystal blades and coatings, and GE unveiled the first such H-class turbine in February 2000.

<a id="howmet-casts-the-queue"></a>

Few companies can cast these blades. The biggest is Howmet Aerospace, which also makes jet engine parts; its own 2026 brochure calls it "the largest manufacturer of gas turbine blades in the world". Its annual report names its rivals: Precision Castparts, owned by Berkshire Hathaway, plus Doncasters in Britain and Consolidated Precision Products. It also says several of its largest customers have their own furnaces. Siemens Energy is expanding its blade and vane plant in Tampa, Florida, in investments it says are "deliberately designed to avoid overcapacity" (my translation of its German release of 3 February 2026). Mitsubishi Heavy has set aside about ¥500 billion of investment for combined-cycle plants that "includes hot parts production capacity".

Demand shows in Howmet's results. Its gas turbine revenue was US$349 million in the third quarter of 2026, up 45 per cent on a year earlier, and US$954 million in the first nine months, up 41 per cent. On its results call, as transcribed by a third party, its chief executive said "2031 is now also sold out" and that new capacity "will take two years to install". GE Vernova's own chief executive said in July that he could "see clearly the castings and forgings arriving in '27" for its next step in output in 2028.

So the hottest blade sets the pace of every heavy turbine. A new casting line takes about two years to install, and the casters build only what is ordered. I have found no published figure for how long a new line takes to qualify with a turbine maker, and I will not guess one.

## Why don't the makers just build more factories?

Because they did exactly that twenty years ago, and the orders vanished.

{{FIG3}}  <!-- America built about 238 GW of gas plant in six years, then the orders fell away -->

Around 2000, American power markets opened up and gas was cheap, and independent developers ordered gas turbines by the hundred. In EIA's generator inventory, about 69 GW of gas capacity entered service in 2002 alone, and about 238 GW across 2000 to 2005, by my sums. EIA says the boom "created excess generating capacity": combined-cycle plants built to run 50 to 70 per cent of the time ran about 34 per cent in 2003.

The makers had built for the boom, and then it stopped. On 16 November 2017 Siemens said world demand for large gas turbines had "fallen drastically" and would level out at about 110 a year, against manufacturing capacity of about 400. It announced about 6,900 job cuts, most in its power and gas businesses. On 7 December 2017 GE's power business announced about 12,000, blaming "overcapacity". American gas additions ran below about 11 GW in most years from 2006, and fell to 2.4 GW in 2024.

That memory explains how the makers are expanding now. GE Vernova plans to raise output from 20 GW a year to 24 GW in 2028 and 30 GW in 2030, through "lean and incremental machinery in our existing factory footprint". It says this is "all funded by customer down payments". By July it had installed 325 new machines in its gas factories, heading for about 400 by the end of 2026. It has announced no new heavy turbine factory.

Siemens Energy and Mitsubishi Heavy are doing the same. Siemens Energy's own investor slides show its large-turbine capacity rising from about 35 units a year to about 50 from its 2027 financial year. Mitsubishi Heavy plans to double its combined-cycle production capacity against its 2024 financial year. Each is expanding inside walls it already owns, paid for by buyers, so that a downturn cannot strand it again.

## How long is the queue at GE Vernova?

About six years of its present output, and it grew by almost half in nine months.

<a id="ge-vernova-sells-the-wait"></a>

GE Vernova reports two kinds of commitment. A **firm order** is a contract for a machine. A **slot reservation agreement** is a paid place in the production line that can later become a firm order, or lapse. Together they are its gigawatts **under contract**.

{{FIG4}}  <!-- GE Vernova's turbine queue grew by almost half in nine months -->

At the end of 2025 GE Vernova had 83 GW under contract. By 30 September 2026 it had 122 GW: 64 GW of firm orders and 58 GW of reservations. At 20 GW a year, that rose from 4.2 to 6.1 years of output. It expects at least 130 GW by the end of 2026.

The queue grows because buyers sign faster than the factory ships. In the first nine months of 2026 GE Vernova signed 52 GW of new contracts and shipped about 13 GW. The 20 GW a year is the pace it reached in the third quarter, when it shipped 5.3 GW; calendar 2026 shipments will be nearer 18 GW, by my estimate.

The furthest slots are far out. In July GE Vernova said it was "mostly sold out through '30" and expected to have sold more than half of its 2031 slots by the end of the year. On 28 October it said "we sold multiple slots for 2032 delivery". A heavy unit then needs about 18 months on site to be installed and commissioned, its chief executive said in July. So a slot bought today makes power around 2034.

Even the planned expansion does not clear it. At 24 GW a year, 122 GW is about 5.1 years of output; at 2030's 30 GW, about 4.1 years. Those steps arrive in 2028 and 2030, the same years existing slots deliver, so they help nobody deciding today.

## Is the wait shorter at the other makers?

Slightly at best. The other two big makers are booked to the end of the decade as well.

<a id="a-second-maker-books-years-out"></a>

{{FIG5}}  <!-- All three big makers are booked for years -->

Siemens Energy, the German maker, reported 69 GW of firm backlog and 26 GW of reservations at 30 June 2026: 95 GW on GE Vernova's definition. It booked 15 GW and shipped 6 GW in that quarter, according to its own investor slides. Its full-year results, due in mid-November 2026, were not out when this was written.

Mitsubishi Heavy reported on 6 November 2026. It booked 19 large gas turbines, 8 GW, in the six months to September, against 23 units, 10 GW, a year earlier. Its backlog of large units rose to 83, about 37 GW, from 74 in March. According to the company's summary of its August call, combined-cycle projects then under discussion "will generally be delivered around 2030 to 2031". Orders booked in that quarter were due between 2028 and 2030, it said, and "Order pricing has not declined". It also said it was being selective in the projects it takes.

Together the three hold about 250 GW under contract, by my sum of figures on different dates and definitions. Who is in the queue matters too. In October GE Vernova said about 20 per cent of its roughly 100 gas customers were data centre projects. That is a share of customers; in April, according to press reports of its call, it put the share of its gigawatts under contract at about a fifth too. The rest are mostly utilities, which want the same machines for the same reason: demand for power is rising for the first time in decades.

So switching maker helps only at the margin. Mitsubishi Heavy's newest orders deliver from 2028, but it is choosing its customers, and all three makers are booked to the end of the decade.

## What does a buyer pay to stand in the queue?

A large deposit up front, at a price per kilowatt that has risen by about half in a year.

GE Vernova's buyers pay before the metal is cut. In its Power segment, which holds gas turbines with its nuclear, hydro and steam businesses, contract liabilities and current deferred income doubled from US$16.5 billion at the end of 2025 to US$33.2 billion at 30 September 2026. Its quarterly report ties the rise mainly to down payments on gas orders and reservations. Those deposits pay for the expansion, which is why the maker carries little risk if demand cools.

The price has risen too. GE Vernova expects orders placed in 2026 to be priced about 50 per cent higher per kilowatt than those of 2025. Its third-quarter orders were priced more than 20 per cent above those of the fourth quarter of 2025, partly because more were aeroderivatives, the quicker machines that cost more per kilowatt.

{{FIG6}}  <!-- New gas plants now cost two to three times the government's planning figure -->

The whole plant costs far more than it did. EIA's planning figure for a large combined-cycle plant is US$868 per kilowatt, in 2023 dollars, from a study it commissioned in 2024. Duke Energy's three new combined-cycle plants run from about US$1,620 to about US$2,340 per kilowatt, by my division of its filed figures: roughly two to nearly three times EIA's figure, which is in older dollars. Cayuga's figure leaves out financing, so it is low. Williams' five on-site plants, including Socrates, come to about US$3,500 per kilowatt of all their expected capital, four times EIA's figure. That figure is my arithmetic from a financing in which outside investors paid for 49 per cent, and it may include pipe.

The buyers keep signing anyway, because power is a small cost beside the chips. What they are buying is a date. A reservation is not power; it is a place in a line, and the price of the place rises as the line lengthens.

## Is there a faster machine?

Yes, several, and they are filling up too.

<a id="the-way-out-has-its-own-queue"></a>
<a id="crusoe-borrows-the-jet-engine"></a>

The first is the **aeroderivative**: a smaller gas turbine built around an aircraft jet engine. GE Vernova's LM2500XPRESS makes about 35 MW at about 38 per cent efficiency; its LM6000 makes up to about 58 MW at about 41 per cent and starts in five minutes. GE Vernova's chief executive said in July that an aeroderivative ships about 24 months before a heavy unit and needs about six months on site, against 18. The cost is fuel: a simple-cycle machine burns about 46 per cent more gas per unit of power than a combined cycle, on EIA's tested averages.

Campuses bought them first. Crusoe, which builds AI campuses, ordered 29 LM2500XPRESS units from GE Vernova in December 2024 and mid-2025, nearly 1 GW. Each leaves the factory about 95 per cent assembled.

{{FIG7}}  <!-- Even the fast lane takes orders faster than it can ship them -->

Now the fast lane has a queue of its own. In 2025 GE Vernova took orders for 63 aeroderivatives and shipped 27. In the first nine months of 2026 it took 127 and shipped 39. Since the start of 2025 it has taken orders for 124 more than it shipped, about two and a half years of its shipments over the past twelve months. On 28 October its chief executive said fourth-quarter orders would be lighter, "not because the demand is softer" but because "we're now going out so far in the future before we have availability".

<a id="the-engines-queue-too"></a>

The second is the **reciprocating gas engine**: a very large version of a car engine, with pistons, running on gas. Wärtsilä's 50SG makes about 18.9 MW at 50 per cent efficiency and reaches full load in two minutes. Engines lose little power in heat and come in small blocks, so a campus can add them a few at a time. On 5 October 2026 Wärtsilä announced a 282 MW order for a US data centre, due for delivery in 2028 and fully running in 2029. It was the company's seventh data-centre order in America, taking its sales there above 3 GW, up from above 1.6 GW in April. On 27 October it said "lead times for our engines continue to increase". Caterpillar, which makes both engines and turbines, sold US$3,421 million of power generation equipment in the third quarter, up 30 per cent, a rise it put down mainly to data centres.

The third is the **fuel cell**, which turns gas into electricity chemically, without burning it. Bloom Energy makes solid oxide fuel cells in boxes that can be added in steps. Its product revenue rose 179 per cent in the third quarter of 2026, to US$1,073.6 million. Oracle, the cloud company, intends to buy up to 2.8 GW from it, 1.2 GW of it contracted. Bloom is doubling its factory to 2 GW a year by the end of 2026.

The fourth is renting. Companies that once powered oilfields now rent gas turbines and engines to campuses. Solaris Energy Infrastructure signed a 900 MW, 15-year contract on 29 October 2026, taking its long-term contracts to 3.2 GW. It also bought 200 MW of equipment it can put to work in 2027, "ahead of long OEM queues": sooner, that is, than a new order from the makers would arrive.

<a id="the-product-is-time"></a>

What these sellers have in common is that they sell time. A buyer pays more per kilowatt, or burns more gas, to start sooner. Bloom's product margin was 37.9 per cent in the third quarter, against 35.0 per cent a year earlier and 35 to 37 per cent in each of the two years before, by my calculation. Its product revenue nearly tripled, so most of the gain came in volume, not price.

I concede the fast lane is still faster. An engine ordered this year arrives in 2028, against 2032 for a heavy slot sold now. But the gap narrows as every campus takes the same shortcut: Wärtsilä's order runs about three years from signing to a running plant. The fast lane buys a year or three, not a decade.

## Why does an island campus build more machine than it uses?

Because with no grid behind it, the campus must carry its own spares, its own margin for heat and its own buffer for sudden swings. I hold this as a hypothesis, not yet a finding.

<a id="an-island-buys-its-own-bench"></a>

{{FIG8}}  <!-- On the grid, other plants cover a trip or a swing; an island must carry its own spares and buffer -->

On the grid, thousands of plants share the load. When one trips, the rest cover it within seconds, and spare capacity is shared across a whole region. An island campus has nobody else. It must keep at least one unit spare in case another fails, a rule engineers call N+1. It must allow for hot days: on Wärtsilä's comparison, an aeroderivative loses nearly 26 per cent of its output at 45°C against standard conditions, while an engine loses under 2 per cent. And it must absorb sudden changes in its own load.

Those changes are real and large. PJM recorded three events in which data centres switched to their own backup generators at once after faults on high-voltage lines: about 1,500 MW on 10 July 2024, about 1,800 MW on 17 February 2025 and about 3,900 MW on 22 July 2026, the largest yet. The last came in two waves: the first transfer raised voltages, which tripped more load onto backup. On the grid, other plants absorbed the drop. An island would have to absorb it alone, usually with a large battery: every big island design I have found pairs its machines with batteries.

Socrates is the one dated point. Williams' annual report, filed in February 2026, said the project would give its customer "a combined 400 megawatts". Its quarterly reports since May say the two plants "together have an expected 556 MW of capacity". That is 1.39 MW built for each MW committed, by my arithmetic. Williams does not say why. An executive of another planned Texas campus told a trade publication its first engine fleet could need about 30 per cent more machine than load; that is press, not a filing.

If that holds, each megawatt of island load draws more than a megawatt from the makers' queues. 122 GW under contract would then serve fewer campus megawatts than it seems. The test is to set installed against committed capacity at every off-grid site I can date. If island sites run near one to one, or keep a grid tie as their spare, the margin is small and the idea is wrong.

## How much gas does a campus burn, and where does it come from?

A gigawatt campus burns about 64 billion cubic feet of gas a year in combined cycle, and America has plenty; the limit is the pipe that carries it.

{{FIG9}}  <!-- A gigawatt of fast machines burns about 46 per cent more gas than a combined cycle -->

Gas is measured in **billion cubic feet a day** (Bcf/d). At EIA's tested heat rates for 2025, one gigawatt running flat out burns about 0.175 Bcf/d in combined cycle, 0.205 in gas engines and 0.254 in simple-cycle turbines, by my arithmetic. A data centre runs close to flat out all year, which makes it a steady pipeline customer rather than an occasional one. All of America's power plants burned 35.8 Bcf/d in 2025.

<a id="permian-gas-follows-the-oil-rig"></a>

Much of the new gas comes from the Permian, the oil basin of west Texas and New Mexico. There it is **associated gas**: it comes up the same wells as the oil, whether or not anyone has a pipe for it. Drillers chase oil, and EIA says the basin's gas-to-oil ratio has risen 15 per cent since 2021. Permian marketed gas rose from 26.3 Bcf/d in the first quarter of 2025 to an estimated 30.2 Bcf/d in the third quarter of 2026, while the number of drilling rigs fell from 302 to 264, on EIA's estimates.

The proof that the pipe, not the gas, is the limit is the price at Waha, the trading hub in west Texas where Permian gas is priced before it leaves the basin. When the pipes out are full, producers must pay buyers to take the gas, because shutting oil wells to stop it costs more. In May 2026 EIA said Waha spot prices had "averaged below zero for eight of the last nine months". In Appalachia, EQT, America's largest gas producer, held back 21 billion cubic feet equivalent of output in the third quarter for the same reason. Gas is plentiful at the well; the shortage is the pipe.

<a id="golden-pass-joins-the-gas-queue"></a>

Campuses also share the pipes with export terminals. **Liquefied natural gas** (LNG) is gas cooled to a liquid for shipping overseas. America exported 15.1 Bcf/d of it in 2025. Golden Pass LNG on the Texas coast shipped its first cargo on 22 April 2026, and when complete its three units will have about 2 Bcf/d of export capacity, and more at peak. Texas's terminals take a steady 4 to 5 Bcf/d all year, about as much as the state's power plants burn in mild months. In February to April 2026, as in spring and late autumn 2025, they took more.

## How long does it take to build the pipe?

About four years for a short expansion beside an existing line, and longer for a new one across the country.

A new interstate pipe follows a fixed sequence. First comes an **open season**, when the pipeline company offers new capacity to all comers. Shippers that want it sign **precedent agreements**, binding contracts to take capacity once it is built. Most are **take-or-pay**: the shipper pays a fixed monthly charge for its booked space whether or not it sends any gas. Only then does the company apply to FERC for a certificate under the Natural Gas Act. It also needs water permits from the Army Corps of Engineers and the states, and only then does it build.

Transco's Southeast Supply Enhancement, an expansion of Williams' big East Coast pipeline, shows the timing. Its open season ran from 19 June to 14 July 2023. Williams applied to FERC on 29 October 2024 and won its certificate in January 2026. It targets gas flowing as early as the third quarter of 2027. That is about four years for 55 miles of new pipe laid beside an existing line, plus work at eight compressor stations. Duke Energy, Southern Company and Santee Cooper, three power companies, signed 93 per cent of its capacity, to fuel their own plants.

New long-distance lines take longer. Kinder Morgan, another pipeline company, decided in October 2026 to build Permian Link, about 434 miles and about 2.8 Bcf/d. It will serve new power generation for an "A-rated hyperscaler" from the third quarter of 2030, and its contracts are take-or-pay. That pipe could fuel about 16 GW of combined cycle, by my arithmetic, though Kinder Morgan does not say the hyperscaler takes all of it. More than 75 per cent of Kinder Morgan's US$14.4 billion project backlog supports power generation and local gas utilities.

The pipes are being signed for campuses directly. Energy Transfer, a Texas pipeline company, contracted about 900 million cubic feet a day to three Oracle data centres. It also signed a 20-year deal to carry gas to Entergy's plants for Meta's Hyperion campus from December 2028. Its new Hugh Brinson pipe out of the Permian went into full service on 1 September 2026.

Federal rules have eased; the courts and states have not. In October 2025 FERC removed a rule that had stopped construction while challenges to a pipeline's approval were still before FERC itself. But on 8 September 2026 a federal appeals court cancelled New Jersey's water approval for another Williams pipe. Even the compressors that push gas along are queuing behind the power plants. On 5 May 2026 USA Compression said some engine lead times had "tripled from 50 weeks to approximately 150 weeks", adding "It's the generator orders".

## Does a campus need a permit to burn the gas?

Yes, an air permit, and it can decide whether the plant is built at all.

A gas plant emits **nitrogen oxides** (NOx), gases that help form smog. Under the Clean Air Act a plant whose emissions pass set thresholds, typically 100 or 250 tons a year depending on the plant and the area, is a major source. It then needs a full review before construction, with the strictest controls and, in areas with poor air, offsets: cuts elsewhere bought to cover its own.

<a id="homer-city-inherits-the-air"></a>

Homer City shows how a big plant got through. Homer City Generation, a developer, is building up to 4,678 MW of gas plant on the site of a Pennsylvania coal plant that closed in 2023. It uses seven GE Vernova 7HA.02 combined-cycle units and ten trailer-mounted Mitsubishi aeroderivatives. Its new plant adds 1,142.8 tons of NOx a year. Retiring the coal boilers removed 2,031.8 tons, and Pennsylvania let it **net** the one against the other, so it avoided the full review. A cut counts only within five years, so a coal site shut long ago has none to spend. Homer City targets first power in early 2028.

Texas has gone the other way. At the governor's direction, the Texas Commission on Environmental Quality, the state's air regulator, wrote on 19 October 2026 that it "has paused the issuance of all permits" for building infrastructure that directly supports data centres. Where possible it is also suspending the lighter authorisations that need no permit to be issued. Texas is where many of the largest island campuses are planned.

The best-known case is still in court. xAI, Elon Musk's AI company, now part of SpaceX, ran gas turbines at its Memphis campus and at a power plant across the state line in Mississippi, describing many of them as temporary. On 30 October 2026, in refusing to dismiss a suit brought by the NAACP, a federal court held that the Mississippi plant was not an exempt "mobile source", according to the plaintiffs' lawyers and local reporting. The case continues. A federal rule of January 2026 set lighter emission limits for temporary turbines, but it does not settle whether they need a full air permit.

So the permit is a clock of its own. For a plant on an old coal site with fresh cuts to net, it can be quick. For a new site in a state that has paused permits, it is now open-ended.

## Does going through the utility avoid the queue?

No. A utility building gas plants for a campus stands in the same turbine queue, on the same clock.

<a id="hyperion-the-plant-outlasts-the-lease"></a>

Meta's Hyperion campus in Louisiana is the largest example. In August 2025 Louisiana's regulator approved three gas plants, 2,262 MW in all, that Entergy Louisiana, the state's utility, will build for it, for service in 2028 and 2029. A second agreement, signed in March 2026, adds seven combined-cycle plants, 5,278 MW, for 2030 and 2031. Its vote is set for December 2026.

The utility route moves the risk rather than removing it. Meta's power agreement with Entergy carries minimum charges and an exit fee. The campus itself, 80 per cent owned by funds of Blue Owl, an investment firm, is leased to Meta from 2029 for an initial four years, renewable to 20. Meta guarantees part of the campus's value for its first 16 years if it walks away. So the plants are built to last decades on a lease that can be shorter, and the minimum charges and exit fee are what protect the utility's other customers.

The utility gains one thing: it can spread spare capacity across its whole system, so it does not need an island's extra machines. But it buys its turbines from the same three makers. Entergy's first plants arrive in 2028, and its second set in 2030 to 2031, the years the makers have already sold.

## So how long does each route take, from start to finish?

The fast routes take a year or two and deliver a few hundred megawatts; the gigawatt routes run to 2028 and beyond, and a turbine slot sold today arrives last.

{{FIG10}}  <!-- Own power is quick for a few hundred megawatts; gigawatts and new turbines take years -->

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
