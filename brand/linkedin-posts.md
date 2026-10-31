# LinkedIn Company Page posts: The Physical Layer

> **30 Oct 2026: all 11 scheduled LinkedIn posts DELETED on Tommy's go** (Schneider 2 Nov, Lumentum 4 Nov, B200 6 Nov, Ajinomoto 9 Nov, ASML 11 Nov, Micron 13 Nov, GE Vernova 16 Nov, Hitachi Energy 20 Nov, Eaton 23 Nov, Siemens Energy 25 Nov, Constellation 4 Dec). Verified: the page shows no scheduled posts. Texts below are kept for reference only. The 23 live posts (1 to 22 + the descent video) stay up. Restart: one LinkedIn post per merged deep piece as each is finished, Johor and Singapore first, 1 to 2 a week.

One per piece. Plain register, first person, no hashtag walls (three max), the link on its own line at the end so LinkedIn renders the card.

---

## 1 · The two seconds (post first; LinkedIn posted)

When you ask an AI a question, there is no answer sitting on a shelf.

A building the size of a factory manufactures every word for you, one at a time, while you watch it type. That single fact is why the AI story has quietly stopped being about chips and started being about electricity, water and copper.

I started The Physical Layer to explain that part of the buildout in plain English: the power, the grid connection, the cooling loop, the wiring between ten thousand chips. The layer where the physics is slow and the constraints are real.

First piece: what actually happens in the two seconds after you hit send.

https://thephysicallayer.fyi/journal/the-two-seconds-after-you-hit-send/

#AIInfrastructure #DataCentres #EnergyTransition

---

## 2 · The queue, not the chip (LinkedIn posted)

Everyone watches chip supply. Almost nobody watches the queue to plug a data centre into the grid.

A chip order arrives in months. A substation and its transformer take years. In Johor, data centre demand more than doubled in a year to roughly 3.8 GW, and the thing deciding whether a project goes ahead is no longer whether power exists, but whether you can connect to it.

I think the scarce asset is a finished connection to the wires, and it is not priced as scarce. I also say what would prove me wrong.

https://thephysicallayer.fyi/journal/the-queue-not-the-chip/

#AIInfrastructure #Grid #DataCentres

---

## 3 · Cooling is half the job (LinkedIn posted)

Electricity is not used up by computation. Almost every watt that goes into an AI chip comes back out as heat.

One cabinet now gives off as much heat as eighty space heaters. Air cannot carry that away, so the biggest plumbing change in the history of data centres is happening right now, and it does not care which chip company wins.

Why air died at 30 to 50 kW per rack, the three ways to cool with liquid, and what the PUE number actually measures.

https://thephysicallayer.fyi/journal/cooling-is-half-the-job/

#DataCentres #LiquidCooling #AIInfrastructure

---

## 4 · Ten thousand chips, one thought (LinkedIn posted)

A frontier AI model is too big to fit on any single chip. So it is sliced across thousands of them, and they have to swap notes for every single word.

If the wiring between them is even 10 per cent slow, the most expensive chips ever built sit idle. That is why a huge share of every AI dollar goes on cables and light, and why it is not extravagance. It is insurance on the other dollar.

https://thephysicallayer.fyi/journal/ten-thousand-chips-one-thought/

#AIInfrastructure #Networking #DataCentres

---

## 5 · The countertop is the bottleneck (LinkedIn posted)

When an AI writes its reply, the arithmetic is fast and the waiting for data is slow.

So the industry started stacking memory chips into little towers glued right next to the processor. Clever, expensive, and it explains which parts of the supply chain are actually scarce.

The view I hold: memory and packaging clear in quarters. Transformers and grid connections clear in years. They do not resolve together, and pricing them as one cycle is the mistake.

https://thephysicallayer.fyi/journal/the-countertop-is-the-bottleneck/

#AIInfrastructure #Semiconductors #DataCentres

---

## 6 · The rack runs out of copper (LinkedIn posted)

NVIDIA's next rack is designed to draw one megawatt. Feed that through today's 54-volt system and you need 200 kg of copper busbar in a single cabinet, and power shelves that take up more rack than the rack has.

So the industry is moving to 800 volts DC, borrowing the supply chain that electric-vehicle charging already built. Every figure in this one is traced to NVIDIA's own published architecture, not aggregators.

The constraint is moving out of the silicon and into the last fifty feet of power delivery.

https://thephysicallayer.fyi/journal/the-rack-runs-out-of-copper/

#AIInfrastructure #DataCentres #PowerElectronics

---

## 7 · The one part of the grid that money cannot hurry (LinkedIn posted)

Malaysia cut the wait to connect a new project to the grid from 36 months to 12, and pushed 33 projects through the scheme by March 2026.

That is a real achievement, and it is also the cleanest experiment anyone has run on the AI buildout, because of the thing it could not touch. A connection queue is two queues wearing one coat. The permission half is a policy variable and a government can rewrite it. The plant half is a large power transformer, built to order around a steel core made by very few mills worldwide, and it answers to nobody.

Policy compression has a floor, and the floor is made of steel and copper.

The piece covers why the first clock moved twenty four months, why the second one did not move at all, and what that gap does to any announced energisation date.

https://thephysicallayer.fyi/journal/the-part-money-cannot-hurry/

#AIInfrastructure #Grid #DataCentres

---

## 8 · The power it drops (LinkedIn posted)

On 22 July, 3.8 GW of data centre demand in northern Virginia switched itself off. PJM called it the largest event of its kind in its history.

Nobody lost power because the data centres stopped. The risk ran the other way. A grid is a tug of war rebalanced every second, and when one side lets go of the rope the other side falls over. Lose a generator and frequency falls, which every operator plans for. Lose a gigawatt of demand and it rises, which almost nobody planned for, because until recently no single customer was big enough to do it.

NERC issued its only alert of 2026 over this, a Level 3, binding the planning and operating spine of the grid. PJM is now weighing ride-through requirements. A data centre is quietly being reclassified from a customer into a piece of grid equipment with obligations.

The piece covers why a site protects itself by disappearing, why a sudden absence is harder than a sudden demand, and what happens to connection costs when behaviour becomes a condition of connecting.

https://thephysicallayer.fyi/journal/the-power-it-drops/

#AIInfrastructure #Grid #DataCentres

---

## 9 · The best argument against my own thesis (LinkedIn posted)

I have written twice that the constraint on AI is the wait to connect to the grid. The strongest objection is obvious: do not join the queue. Build your own power station on site and connect to nothing.

That objection is real and I take it seriously. Then you look at who makes the machines. GE Vernova reports 116 GW under contract, 53 GW firm and 63 GW in reserved manufacturing slots, mostly sold out through 2030. Siemens Energy reports 95 GW. The escape route from the queue is a queue, and it is already years deep.

The part usually left out: a turbine on your site still needs transformers, switchgear and a substation-grade yard, from the same constrained supply chain that makes a grid connection slow. You have swapped a queue you cannot control for one you can. That is worth something. It is not no queue.

The piece covers the objection at its strongest, why I think it relocates the problem rather than removing it, and the specific test that would prove me wrong.

https://thephysicallayer.fyi/journal/the-way-out-has-its-own-queue/

#AIInfrastructure #Grid #DataCentres

---

## 10 · What the battery is really for (LinkedIn posted)

Most people still think a grid battery is for storing cheap electricity and selling it later. That is no longer the job that explains who is buying them.

A battery now lets a data centre open before its grid connection is finished. The site draws what its partial connection allows, discharges to run harder during the day, and refills when demand is low. Nothing about that is an energy trade. It is a scheduling trick, and it is worth paying for because the alternative is eight months of not earning anything.

Developers planned 24 GW of utility-scale storage in the US this year. 12.9 GW of it, 53%, is in Texas, which is not half the American economy but is where the computing load is arriving. Storage is following the load, not the price.

If you model grid storage off electric vehicle adoption, you miss a buyer who does not care about cars and is working to a completely different clock.

https://thephysicallayer.fyi/journal/what-the-battery-is-really-for/

#AIInfrastructure #EnergyStorage #Grid

---

## 11 · Two governments, opposite policies, the same confession (LinkedIn posted)

There are two ways to find out what somebody thinks is scarce. Ask them, or watch what they do about it. The second is more reliable, because the first is a statement and the second is a cost.

Malaysia could make more grid connection, so it did. Tenaga committed RM43 billion and cut the wait for a connection from 36 months to 12, delivering 33 projects by March 2026. Note what the money bought: wires, substations and a faster approval process. Not power stations. A utility that thought it was short of electricity would be building generation.

Singapore cannot make more, so it rations. It froze new data centre approvals from 2019 to 2022, and now releases capacity in controlled batches with an efficiency condition attached, so the megawatts go to whoever wastes the fewest of them.

Nobody rations something that is plentiful. Two jurisdictions, different politics, different tools, opposite routes, same operational conclusion. One is spending to relieve a scarcity and the other is rationing access to it, and those are the only two things you can do about a scarce thing.

The piece also takes apart an official statistic in the middle of this that does not divide the way it should, and what the likely explanation says about announced capacity versus energised capacity.

https://thephysicallayer.fyi/journal/two-governments-one-confession/

#AIInfrastructure #Grid #DataCentres

---

## 12 · Bloom Energy is selling time (LinkedIn posted)

Bloom Energy's electricity costs more than the grid's. Oracle and one of America's biggest utilities are buying gigawatts of it anyway.

The US is not short of power in general. It is short of the ability to deliver a large new block of it to one site quickly, and grid waits now run past four years. Bloom's fuel cells switch on in months. Oracle swapped the gas turbines planned for its New Mexico campus for Bloom, and AEP signed for up to a gigawatt itself. Nobody bought Bloom because it was cheapest. They bought it because it was fastest.

The piece covers what Bloom actually makes, where the time premium shows up in Bloom's own margins, and the specific evidence that would prove me wrong.

https://thephysicallayer.fyi/journal/the-product-is-time/

#AIInfrastructure #FuelCells #DataCentres

---

## 13 · Vertiv is paid per megawatt (LinkedIn posted)

Vertiv makes no chips and writes no software, yet AI has made it one of the busiest suppliers in the buildout.

An ordinary server rack drew around 10 kW. An AI rack draws about 130, and air cannot carry that heat away, so every megawatt of building now needs liquid loops, coolant pumps and heavier power gear. Vertiv gets paid for every new building, and again for how much more equipment sits inside each one. Its own numbers show it: adjusted operating margin up 4.1 points to 22.6% last quarter, and service revenue growing faster than hardware.

The piece covers what Vertiv actually makes, where that second win shows up in its disclosures, and the specific evidence that would prove me wrong.

https://thephysicallayer.fyi/journal/every-megawatt-got-harder/

#AIInfrastructure #DataCentres #Cooling

---

## 14 · Jane Street has room to spare (LinkedIn posted)

Jane Street's new AI training centre in Texas has empty floor it cannot use.

The trading firm runs 4,032 Nvidia GPUs there, cooled by liquid, in a building designed for air. Each cabinet draws about 140 kW against 10 to 40 for an air-cooled one, so the power the utility agreed to supply now fills a fraction of the room. Its engineers run as close to that limit as they dare, with their own software ready to shut machines down before a breaker trips, because an idle GPU costs more than the hardware.

The piece covers why the floor went quiet, what it takes to put water where water was forbidden, and why power is so much harder to move around than cooling.

https://thephysicallayer.fyi/journal/room-to-spare/

#AIInfrastructure #DataCentres #LiquidCooling

---

## 15 · Jane Street commits to the power first (LinkedIn Wed 14 Oct, 11:30, scheduled)

At Jane Street, the chips are now the last thing ordered.

The firm's head of physical engineering says generators, transformers and some liquid-cooling equipment take more than a year to arrive, so the building and the power are settled before the chip order goes in. On one site the team kept backup generators to the core of the system rather than the whole building, and switched its GPUs on six months sooner. His words: maybe not the best engineering decision, but the best business decision.

The piece covers why the order flipped, the generator the firm chose not to buy, and what would prove me wrong.

https://thephysicallayer.fyi/journal/power-first-chips-last/

#AIInfrastructure #DataCentres #Power

---

## 16 · Marvell collects the toll (LinkedIn Fri 16 Oct, 11:30, scheduled)

Marvell is paid every time AI chips talk to each other, and it barely matters whose chips they are.

Copper stops carrying an AI signal after a few metres, so every link between cabinets turns electricity into light and back, and the chip doing that translation is very often Marvell's. Bigger clusters need more links, and every speed jump means new ones. Data centre work is now 79% of Marvell's revenue, and it is prepaying about $1 billion to suppliers to secure its next generation of optical chips.

The piece covers where copper stops and Marvell starts, what its own numbers show, and the change in optics that would prove me wrong.

https://thephysicallayer.fyi/journal/marvell-collects-the-toll/

#AIInfrastructure #Optics #DataCentres

---

## 17 · Oklo sells the electricity (LinkedIn Mon 19 Oct, 11:30, scheduled)

Oklo, the nuclear start-up building small reactors for AI data centres, does not plan to sell a single reactor.

It plans to build them with its own money, put them beside the data centre, keep them, and charge for the electricity under contracts lasting decades. That makes it a power company, and it means it earns nothing from power until its first reactor runs. So far only Meta has put binding money behind its agreement; the 12 gigawatt deal with Switch is still a framework.

The piece covers why a data centre wants a reactor next door, what Oklo's own numbers show, and the fuel and licence problems that could stop it.

https://thephysicallayer.fyi/journal/oklo-sells-the-electricity/

#AIInfrastructure #Nuclear #DataCentres

---

## 18 · Nebius is paid for what is switched on (LinkedIn Wed 21 Oct, 11:30, scheduled)

Microsoft and Meta, two of the biggest data centre builders on earth, both rent AI capacity from Nebius.

They were not short of chips. They were short of buildings with the power on. Nebius expects 5 gigawatts of power contracted by the end of 2026 and about 1 gigawatt connected, and its contracts pay only for capacity that is running, at $20 to $25 million per megawatt a year on its latest deals.

The piece covers what Nebius actually sells, what its own numbers show, and the Meta report that would prove me wrong.

https://thephysicallayer.fyi/journal/nebius-paid-for-what-is-switched-on/

#AIInfrastructure #DataCentres #Power

---

## 19 · Corning lays the glass (LinkedIn Fri 23 Oct, 11:30, scheduled)

Meta, Amazon and Nvidia have all signed deals this year with a 175-year-old glass company.

Corning makes the optical fibre AI chips talk through once copper runs out, about two metres from the chip. Every new chip generation replaces the plugs at each end, but the glass in the ceiling stays, and a campus of AI buildings needs far more of it between halls than inside them. Corning's data centre business grew 65% last quarter, and it says demand is running above what its factories can make.

The piece covers why the glass is hard to make, what Corning's own numbers show, and the 2001 fibre bust that could repeat.

https://thephysicallayer.fyi/journal/corning-lays-the-glass/

#AIInfrastructure #Optics #DataCentres

---

## 20 · Broadcom wins either way (LinkedIn Mon 26 Oct, 11:30, scheduled)

When OpenAI built its first chip to rely less on Nvidia, it built it with Broadcom.

Broadcom also makes the switch chips that let thousands of AI processors work as one machine, Nvidia's included. So whether the cloud giants keep buying Nvidia or design their own, the work runs through the same company. Its AI revenue was $16.7 billion last quarter, up 221% on a year earlier, with six custom chip customers behind it.

The piece covers why the switch sets the size of the machine, why the giants want their own chips, and the Google work that could prove me wrong.

https://thephysicallayer.fyi/journal/broadcom-wins-either-way/

#AIInfrastructure #Networking #DataCentres

---

## 21 · TI feeds the chip (LinkedIn Wed 28 Oct, 11:30, scheduled)

The AI processor that costs tens of thousands of dollars cannot run on the electricity delivered to it.

Power reaches the rack at 54 volts, soon 800, and the chip runs below one volt, so a crowd of small chips steps it down millimetres away. Texas Instruments makes many of them, some for cents, and is spending more than $60 billion on its own American factories to make them cheaper. Its data centre business doubled last quarter, from a base of 9% of revenue.

The piece covers why the last centimetre is the hard part, TI's factory bet, and what would prove me wrong.

https://thephysicallayer.fyi/journal/ti-feeds-the-chip/

#AIInfrastructure #Power #DataCentres

---

## 22 · TSMC says it is the bottleneck (LinkedIn Fri 30 Oct, 11:30, scheduled)

I have argued that the grid, not the chip, is what holds AI back. TSMC's chief executive disagrees.

Almost every advanced AI chip, whoever designs it, is made in TSMC's factories, and TSMC says a new one takes two to three years to build and one to two more to fill. Its 2026 spending of up to $64 billion adds almost nothing to this year's output, and its packaging capacity is so tight it is limiting customers' growth.

The piece covers why one company makes everyone's chips, the clock on a chip factory, and what would prove me wrong.

https://thephysicallayer.fyi/journal/tsmc-says-it-is-the-bottleneck/

#AIInfrastructure #Semiconductors #DataCentres

---

## 23 · Lumentum makes the light (LinkedIn Wed 4 Nov, 11:30, scheduled)

In March, Nvidia paid $2 billion to a laser company, and another $2 billion to its rival on the same day.

Past a couple of metres, AI chips talk to each other in light, and that light starts in a laser grown on indium phosphide, a crystal that only a few factories in the world can work at volume. Lumentum doubled its revenue in a year and says it will still be significantly behind demand at the end of 2026.

The piece covers why silicon cannot make light, what Lumentum's own numbers show, and what would prove me wrong.

https://thephysicallayer.fyi/journal/lumentum-makes-the-light/

#AIInfrastructure #Optics #DataCentres

---

## 24 · Schneider Electric sells the finished system (site live 7 Oct 2026; LinkedIn Mon 2 Nov, 11:30, scheduled)

Schneider Electric's fastest-growing business is not the breakers and switches it is best known for.

Its Systems business, which includes power rooms and cooling plants built and tested in a factory, grew 28% in the second quarter against 13% for its catalogue products. Schneider says data centres led that growth. I think the reason is on the building site: an AI hall cannot switch on until every panel is installed and tested, and the people who do that work are scarce.

The piece covers how Schneider splits what it sells, the shift in its own numbers, and why it is spending on design tools as well as factories.

https://thephysicallayer.fyi/journal/schneider-sells-the-finished-system/

#DataCentres #Electrification #EnergyInfrastructure

---

## 25 · GE Vernova sells the wait (site live 9 Oct 2026; LinkedIn Mon 16 Nov, 11:30, scheduled)

GE Vernova signed 41 gigawatts of gas turbine contracts in the first half of 2026 and shipped seven.

Most of those contracts are paid places in a queue for 2030 and 2031, and customers have handed over billions in deposits to hold them. GE Vernova is using that money to stretch the factories it already has, not to build new ones. For anyone planning to skip the grid queue with their own power, that is the number that sets the date.

The piece covers what a slot reservation is, where the deposits show up in GE Vernova's filings, and why the queue is likely to stay years long.

https://thephysicallayer.fyi/journal/ge-vernova-sells-the-wait/

#GasTurbines #DataCentres #EnergyInfrastructure

---

## 26 · Fluence (removed 12 Oct 2026: piece and note taken down by Tommy; its 18 Nov LinkedIn post deleted, slot left empty)

---

## 27 · Hitachi Energy plans the queue (site live Thu 22 Oct 2026; LinkedIn Fri 20 Nov, 11:30, scheduled)

Hitachi Energy is spending more than $9 billion on factories, and it still expects about three years of orders to be waiting in 2030.

It is the largest maker of the transformers and long-distance power links that connect data centres and power stations to the grid. Its unfilled orders reached $63.6 billion in June, about three years of sales, and it told investors that ratio should stay at two and a half to three times while its output nearly doubles. For anyone waiting on a substation, that is the plan for how long the queue lasts.

The piece covers what Hitachi Energy makes, how its queue is measured in years, and why its new factories keep the queue rather than clear it.

https://thephysicallayer.fyi/journal/hitachi-energy-plans-the-queue/

#Transformers #DataCentres #EnergyInfrastructure

---

## 28 · Eaton's order book outruns it (site live Mon 26 Oct 2026; LinkedIn Mon 23 Nov, 11:30, scheduled)

Eaton shipped 18% more electrical gear in the year to June, and its order book grew 33%.

Eaton makes the switchgear, backup power and wiring that sit between the grid and the racks in a data centre. It is spending more than $1 billion on two dozen capacity projects, yet the orders waiting in its North American business have grown from about eleven months of sales to about thirteen. The big new plants that could close the gap arrive in 2027.

The piece covers what Eaton makes, how its queue is measured in months, and what that queue does to its margin.

https://thephysicallayer.fyi/journal/eaton-order-book-outruns-it/

#DataCentres #Electrification #EnergyInfrastructure

---

## 29 · Siemens Energy measures the shortage (site live Wed 28 Oct 2026; LinkedIn Wed 25 Nov, 11:30, scheduled)

Siemens Energy has published its own estimate of the transformer shortage, and on its chart demand is still ahead of every factory in 2030.

It covers what Siemens Energy calls all market players for large power transformers in Europe and North America. Demand ran about 40 per cent ahead of capacity in 2025 and is still about 10 per cent ahead in 2030, even after capacity grows by about 60 per cent. A smaller shortage still adds to the pile of unfilled orders each year, and Siemens Energy's own grid backlog has grown from €33 billion to €51 billion in under two years.

The piece covers what the chart shows, why a narrowing gap still adds to the pile, and why Siemens Energy's grid business now out-earns its gas turbines.

https://thephysicallayer.fyi/journal/siemens-energy-measures-the-shortage/

#Transformers #DataCentres #EnergyInfrastructure

## 30 · Nobody makes a B200 alone (site live 7 Oct 2026; LinkedIn Fri 6 Nov, 11:30, scheduled)

Nobody makes an Nvidia B200 on their own, not even Nvidia.

One accelerator draws on factories mostly in Taiwan, machines from the Netherlands, mirrors from Germany, memory from South Korea and materials from Japan. Some of those suppliers could be swapped in months. Others would take years, because a replacement needs a new factory or years of testing before anyone trusts it, and that is the dependency that matters.

The piece follows one B200 from blueprint to wafer, through its memory and packaging, and into the rack.

https://thephysicallayer.fyi/journal/nobody-makes-a-b200-alone/

#Semiconductors #SupplyChain #AIInfrastructure

---

## 31 · Ajinomoto grows with the package (site live 7 Oct 2026; LinkedIn Mon 9 Nov, 11:30, scheduled)

The company best known for monosodium glutamate makes the insulating film inside nearly all high-performance processors, by its own account.

Ajinomoto's build-up film insulates each wiring layer in the base under a processor. By Ajinomoto's estimate, AI chip bases are growing from about 70 millimetres square with nine layers to about 100 with eleven, so by my reading each package needs far more film than chip counts suggest. Servers and networks have gone from 40 to 70 per cent of its film volume since fiscal 2017, and its next plant opens only in fiscal 2032.

The piece covers why the film grows faster than the chips, why chipmakers rarely switch to a rival, and what the 2032 plant date implies.

https://thephysicallayer.fyi/journal/ajinomoto-grows-with-the-package/

#Semiconductors #AIInfrastructure #SupplyChain

---

## 32 · ASML booked ahead (site live 7 Oct 2026; LinkedIn Wed 11 Nov, 11:30, scheduled)

The machines that print the finest AI chips are booked a year or two before they are built.

ASML is the only company that makes EUV lithography machines. It expects to ship about 65 of its standard model this year, its full capacity, and says 2027 is already close to fully ordered. Its output grows only as fast as ZEISS optics and its own cleanrooms allow, about 30 per cent a year, so a chipmaker adding capacity has to commit a year or two ahead, much like a data centre booking its grid connection.

The piece covers why only ASML can build them, the supplier behind the supplier, and what ASML itself says about whether it is short.

https://thephysicallayer.fyi/journal/asml-booked-ahead/

#Semiconductors #AIInfrastructure #SupplyChain

---

## 33 · Micron, three times the wafer (site live 7 Oct 2026; LinkedIn Fri 13 Nov, 11:30, scheduled)

Each bit of AI memory uses about three times the silicon of ordinary computer memory.

Micron, one of three companies that make the stacked memory beside AI chips, says so itself, and it sells most of each year's supply before the year starts. Every wafer that goes into AI memory is a wafer ordinary memory goes without, so while AI memory grows faster than the rest, phones, laptops and servers feel the squeeze too. New memory factories take years, and Micron names the need for more energy infrastructure among the things slowing them.

The piece covers why stacked memory eats wafers, why it is sold before it is made, and what would show the squeeze has eased.

https://thephysicallayer.fyi/journal/micron-three-times-the-wafer/

#Semiconductors #AIInfrastructure #SupplyChain

---

## The descent, from the grid to the chip (site live 9 Oct 2026; LinkedIn posted Fri 9 Oct, with the dark square video from brand/video/)

Everything in an AI data centre is one chain, so I drew it as one.

Scroll down the map on The Physical Layer and you descend through it: a high-voltage line, the site, the hall, one rack, one tray, one Nvidia B200, and finally the machine that prints its silicon with light.

At every level the choke point is circled in red. Transformers. Gas turbines. Copper in the rack. Packaging. The EUV machine only ASML builds.

That is the point of the drawing. The slowest link sets the pace for everything above it, and the slowest links are rarely the famous ones.

Nine stops, from kilometres down to nanometres, with every piece I have written pinned to the layer it explains.

https://thephysicallayer.fyi/map/

#AIInfrastructure #DataCentres #Semiconductors

---

## 34 · Constellation restarts the reactor (site live Fri 30 Oct 2026; RETIRED 1 Nov 2026: not in LinkedIn's queue, and the piece is now a section of Nuclear for AI, covered by posts 42 and 51; Tommy agreed to leave Fri 4 Dec empty)

The hardest part of restarting the Three Mile Island reactor was not the reactor. It was the wire.

Constellation can have the 835 megawatt unit ready for Microsoft in 2027, but a fresh grid connection would not have been fully ready until around 2030 or later. So it borrowed one, moving grid rights from two old units it had planned to retire. For AI campuses that want firm, carbon-free power this decade, that is the real constraint: a place on the grid that already exists.

The piece covers how a reactor restart works, why Constellation had to borrow a connection, and what would prove me wrong.

https://thephysicallayer.fyi/journal/constellation-restarts-the-reactor/

#NuclearEnergy #DataCentres #EnergyInfrastructure

---

## 35 · PJM sends the bill (site live Mon 9 Nov 2026, scheduled; LinkedIn Mon 7 Dec, 11:30)

PJM's capacity auction has cleared at its price cap three times running, and the latest one still came up almost 7 gigawatts short.

PJM runs the grid for 67 million people across 13 states, including northern Virginia's data centres. Data centre demand is rising faster than power stations can be built and connected, and its market monitor puts nearly two fifths of the latest auction's cost on that demand. That cost lands on household bills, which is where the AI build-out meets its political limit.

The piece covers how the capacity auction works, why a higher price cannot summon a plant in time, and what would prove the claim wrong.

https://thephysicallayer.fyi/journal/pjm-sends-the-bill/

#PowerGrid #DataCentres #EnergyInfrastructure

---

## 36 · Seagate sells the terabyte (site live Wed 11 Nov 2026, scheduled; LinkedIn Wed 9 Dec, 11:30)

Seagate shipped 26 per cent more hard drive storage in a year on roughly the same number of drives.

AI keeps producing data that has to live somewhere, and the spinning hard drive is still the cheapest place to keep it. Seagate is answering by packing more terabytes into each drive rather than building more, so most of what it can make is already promised into 2028. Storage grows only as fast as each disk can be packed.

The piece covers how a laser lets a disk hold more, why the makers will not simply build more drives, and what would prove me wrong.

https://thephysicallayer.fyi/journal/seagate-sells-the-terabyte/

#DataCentres #AIInfrastructure #Storage

---

## 37 · Water is a siting problem (site live Fri 13 Nov 2026, scheduled; LinkedIn Fri 11 Dec, 11:30)

Most of a data centre's water is not used at the data centre.

Lawrence Berkeley National Laboratory estimates American data centres consumed 66 billion litres of water on site in 2023, and the power stations feeding them about twelve times that. On site, water is a choice: evaporate it to save electricity, or spend a little more power and use none, as Microsoft's new designs do. That makes water a question of where campuses go, not how many get built.

The piece covers how a cooling tower trades water for power, where the water really goes, and what would prove me wrong.

https://thephysicallayer.fyi/journal/water-is-a-siting-problem/

#DataCentres #Water #Cooling

---

## 38 · Johor and Singapore: the plug, not the chip (site live 30 Oct 2026; LinkedIn Mon 2 Nov, 11:30, scheduled)

Malaysia's data centres draw less than a quarter of the power they have booked from the grid.

Johor holds two thirds of Malaysia's secured data centre capacity, and across the causeway Singapore allocates new capacity in rationed batches, 200 megawatts provisionally in August. In both, the connection decides who gets to build. In Johor, the halls then fill only as fast as tenants bring chips, some of which need an American licence.

The piece covers the three clocks every campus passes, what Tenaga and Singapore's regulators publish, and the claims I have on record.

https://thephysicallayer.fyi/journal/the-queue-not-the-chip/

#DataCentres #Grid #SoutheastAsia

---

## 39 · America rations the plug (site live 30 Oct 2026; LinkedIn Wed 4 Nov, 11:30, scheduled)

Texas has been asked to connect over 474 gigawatts of new demand, more than five times the most power it has ever used at once.

Most of it is data centres, and America cannot build wires that fast. So its grids are rationing the connection: a firm plug that waits years for new lines, and an earlier one the grid can cut first. The same sites must now stay on through faults, after 3,800 megawatts of data centres in Dominion's Virginia zone dropped to backup power in July.

The piece covers who can be cut, who pays for the wait, and what backs the sites up: generators, batteries or slower chips.

https://thephysicallayer.fyi/journal/america-rations-the-plug/

#DataCentres #Grid #Energy

---

## 40 · The equipment queue (site live 30 Oct 2026; LinkedIn Mon 9 Nov, 11:30, scheduled)

Hitachi Energy had $66.9 billion of orders waiting at the end of September, about three years of work, and it plans to keep it that way through 2030.

It is building or expanding more than 40 factories. So are Siemens Energy, Eaton and Schneider Electric, which make the transformers and switchgear an AI data centre cannot switch on without. Yet each reports a bigger pile of signed orders than a year ago, and Siemens Energy's own estimate has transformer demand in Europe and North America still ahead of every maker's capacity in 2030.

The piece puts the four makers side by side: years of work from each one's latest filing, every new plant with its date, and the claims I have on record.

https://thephysicallayer.fyi/journal/the-equipment-queue/

#Transformers #DataCentres #EnergyInfrastructure

---

## 41 · Building your own power (site live 30 Oct 2026; LinkedIn Wed 11 Nov, 11:30, scheduled)

GE Vernova has 122 gigawatts of gas turbines under contract and ships about 20 gigawatts a year.

AI campuses tired of waiting for the grid are building their own gas power, and they are queuing beside utilities for the same machines, with places now sold for 2032. Even the fast lane is full: GE Vernova took orders for 127 jet-engine turbines in nine months and shipped 39.

The piece covers the four clocks that replace the grid's, from turbine slots to blades, air permits and gas pipes, and the claims I have on record.

https://thephysicallayer.fyi/journal/building-your-own-power/

#GasTurbines #DataCentres #EnergyInfrastructure

---

## 42 · Nuclear for AI (site live 30 Oct 2026; LinkedIn Mon 16 Nov, 11:30, scheduled)

The only American plant that has made the near-20% uranium the new reactors need delivered 900 kilograms in one contract phase, and in June its contracted production stopped.

That fuel, HALEU, is what Oklo, TerraPower and Kairos Power need, and the next contracted American tonne is due in 2032. So the nuclear power AI gets this decade comes from reactors that already exist: Crane for Microsoft in 2027, uprates for Google through 2032, and two other restarts, each reusing a licensed site, a grid place and ordinary fuel.

The piece covers a dated ladder of every route from restart to advanced reactor, the gate each one waits on, and the enrichment supply behind them.

https://thephysicallayer.fyi/journal/nuclear-for-ai/

#NuclearEnergy #DataCentres #EnergyInfrastructure

---

## 43 · Powering the rack (site live 30 Oct 2026; LinkedIn Wed 18 Nov, 11:30, scheduled)

Nvidia says a one megawatt AI rack, wired the way racks are today, would need up to 200 kilograms of copper bar.

So the rack is moving from 54 volts to 800, and each megawatt now holds more power gear: Vertiv puts its own opportunity at US$3.25 million to 3.75 million per megawatt. On Nvidia's own dates, the new voltage reaches the rack before the building, which decides where silicon carbide and gallium nitride chips get used first.

The piece covers the power chain step by step, what Nvidia has actually said on timing, and the claims I have on record on Vertiv and Texas Instruments.

https://thephysicallayer.fyi/journal/powering-the-rack/

#DataCentres #Power #800VDC

---

## 44 · Heat and water (site live 30 Oct 2026; LinkedIn Mon 30 Nov, 11:30, scheduled)

A liquid-cooled AI hall can go from about 2 litres of water per kilowatt-hour to almost none, and barely change its power use.

That is what Lawrence Berkeley National Laboratory's simulations show when a cooling tower is swapped for a dry cooler. Heat has pushed AI chips onto liquid, and the liquid runs warm enough to cool without evaporating water. So water decides where and how AI halls are cooled, not how many get built. Google air-cools its campuses where it judges the water source at high risk: its Mesa, Arizona site used 9.7 million gallons in 2025, against 469 million at its water-cooled campus in Oregon.

The piece covers the cooling chain, PUE and water use by cooling method, Jane Street's retrofit, and the claims I have on record.

https://thephysicallayer.fyi/journal/heat-and-water/

#DataCentres #Cooling #Water

---

## 45 · Ten thousand chips, one thought (site live 30 Oct 2026; LinkedIn Mon 23 Nov, 11:30, scheduled)

Google's whole optical layer, mirror switches, plugs and fibre, came to under 3 per cent of a 4,096-chip AI pod's power.

The parts of an AI network that only carry or steer light, the fibre and the mirrors, last for years. The parts that make and read it, the lasers and the chips inside each plug, are bought again every time the chips get faster. Nvidia and Broadcom now build optics onto their switches, but both kept the lasers in a plug you can pull out by hand, and Nvidia's own blueprint for its newest systems still picks the plug-in switch.

The piece covers the three distances AI chips talk across, the bill of materials layer by layer, the claims I have on record and where I was wrong.

https://thephysicallayer.fyi/journal/ten-thousand-chips-one-thought/

#AIInfrastructure #Networking #Optics

---

## 46 · The chip supply chain (site live 30 Oct 2026; LinkedIn Wed 25 Nov, 11:30, scheduled)

ASML, the only maker of the machines that print the finest AI chips, says its planned supply for 2027 and 2028 "will not fully meet the demand" of its customers, and some want to order for 2030.

It is not alone. Micron has agreed most of its 2027 stacked memory, and Seagate has allocated most of its data centre drives through 2028. Each is a part only one or a few makers can supply, and each grows only as fast as a new building, so the chip side is booked as far ahead as a grid connection.

The piece covers the lead time at each step from the companies' own filings, one B200 sorted by how long each part takes to replace, and the claims I have on record.

https://thephysicallayer.fyi/journal/the-chip-supply-chain/

#Semiconductors #SupplyChain #AIInfrastructure

---

## 47 · Contracted, energised, running (site live 30 Oct 2026; LinkedIn Wed 2 Dec, 11:30, scheduled)

Nebius has signed rights to 5 gigawatts of power for the end of 2026. It expects 0.8 to 1 gigawatt connected, and at the end of 2025 about 170 megawatts were running chips.

Every AI campus passes five stages: announced, under construction, energised, delivered and running. At Abilene, Texas, the tenant's chips arrived with the power. In Malaysia, connected data centres drew about 22% of the power they had booked in June. Power switched on is necessary. It is not enough.

The piece sets Abilene, Nebius and Jane Street side by side, stage by stage, with the claims I have on record and where I was wrong.

https://thephysicallayer.fyi/journal/contracted-energised-running/

#DataCentres #AIInfrastructure #Power

---

## 48 · Hong Kong has the plug (site live Mon 2 Nov 2026, scheduled; LinkedIn Mon 7 Dec, 11:30)

Hong Kong's main utility has finished eight substations for data centres since 2024, nearly three times as many as in the six years before, and plans 18 by 2028.

It is obliged to meet demand at the lowest reasonable cost, and had about a quarter more capacity than its 2025 peak. Its one AI megasite drew a single bid, from a group that plans to let racks, not run chips. The hard part is the chip: under US rules Hong Kong is treated as China, so the hall's address decides the licence.

The piece covers CLP's substations and sales to data centres, the Sandy Ridge tender and its tenant, and the US licence rules by chip and route.

https://thephysicallayer.fyi/journal/hong-kong-has-the-plug/

#DataCentres #HongKong #ExportControls

---

## 49 · Update: Johor and Singapore, own power (update live 31 Oct 2026 in the rewrite; LinkedIn Wed 9 Dec, 11:30, to be scheduled 4 Nov)

A 100 MW data centre running on its own gas turbines in Singapore would burn 1 to 2% of its LNG terminal's capacity, and still would not add a single megawatt of computing.

In America, AI labs build their own gas power to escape the grid queue. In Singapore that is legal, but what is rationed is IT capacity, allocated by call and soon licensed hall by hall, so own power buys nothing. Across the causeway, Malaysia encourages data centres to generate their own power, but through solar with no export.

The update covers Singapore's licences for on-site power, why gas supply is a system risk rather than a campus cap, and Malaysia's solar steer.

https://thephysicallayer.fyi/journal/the-queue-not-the-chip/

#DataCentres #Singapore #Energy

---

## 50 · Update: Building your own power, the gas pipe (update live 31 Oct 2026 in the rewrite; LinkedIn Mon 14 Dec, 11:30, to be scheduled 6 Nov)

The newest Permian gas pipe, 2.8 billion cubic feet a day for one hyperscaler's own power plants, lands in the third quarter of 2030.

A new pipe is contracted take-or-pay by the gas buyer, and a recent one is due about four years after its first bids. That puts the fuel on the same clock as the heavy turbines, which are sold out to 2030. The fastest own-power route I can date from primary sources was built by a pipeline company: Williams' off-grid plants for Meta in Ohio.

The update covers the pipe's contract clock, Kinder Morgan's and Transco's newest lines, and the one test left open.

https://thephysicallayer.fyi/journal/building-your-own-power/

#NaturalGas #DataCentres #EnergyInfrastructure

---

## 51 · Update: Nuclear for AI, fuel contracts (update live 31 Oct 2026 in the rewrite; LinkedIn Wed 16 Dec, 11:30, to be scheduled 9 Nov)

America's reactor owners have not yet bought about half the uranium they expect to need to 2035.

At the end of 2025 they had at most 174 million pounds under contract for 2026 to 2035 and 186 million still to buy, most of it for 2031 to 2035. That is how utilities normally buy, a few years forward, so it is not a shortage. The harder gap is HALEU, the richer fuel new reactors need: the Energy Department has made ten conditional allocations from its own stock and published a tonnage for none of them.

I've updated my nuclear piece with the uranium contract book, the HALEU allocations, and why Kairos's government fuel is for Hermes 1, not the reactor it sold to TVA.

https://thephysicallayer.fyi/journal/nuclear-for-ai/

#Nuclear #Uranium #AIInfrastructure

---

## 52 · Memory, not maths (site live Sat 31 Oct 2026; LinkedIn Mon 21 Dec, 11:30, scheduled by Tommy on his phone)

Since 2020 the maths in Nvidia's top AI chip has grown about 112 times. The memory feeding it has grown about nine.

When a model writes an answer, one word at a time, it must read the whole model out of memory for every word, so the chip spends much of its time waiting. Memory, not maths, sets how fast AI answers and how many people one chip can serve. Rubin is the first Nvidia generation where that gap stopped widening, on the new HBM4 standard.

Now the biggest buyer is designing the memory itself. Nvidia's NVHBM moves its own memory controller into the base of each stack, and Micron says it is working with Nvidia on the first one. A standard part is becoming one built to a buyer's design.

The piece covers the memory wall in Nvidia's own spec sheets, how the base die became a logic chip, and where the new HBM capacity is being built.

https://thephysicallayer.fyi/journal/memory-not-maths/

#AIInfrastructure #Semiconductors #Memory
