# LinkedIn Company Page posts — The Physical Layer
One per piece. Plain register, first person, no hashtag walls (three max), the link on its own line at the end so LinkedIn renders the card.

---

## 1 · The two seconds (post first)

When you ask an AI a question, there is no answer sitting on a shelf.

A building the size of a factory manufactures every word for you, one at a time, while you watch it type. That single fact is why the AI story has quietly stopped being about chips and started being about electricity, water and copper.

I started The Physical Layer to explain that part of the buildout in plain English: the power, the grid connection, the cooling loop, the wiring between ten thousand chips. The layer where the physics is slow and the constraints are real.

First piece: what actually happens in the two seconds after you hit send.

https://thephysicallayer.fyi/journal/the-two-seconds-after-you-hit-send/

#AIInfrastructure #DataCentres #EnergyTransition

---

## 2 · The queue, not the chip

Everyone watches chip supply. Almost nobody watches the queue to plug a data centre into the grid.

A chip order arrives in months. A substation and its transformer take years. In Johor, data centre demand more than doubled in a year to roughly 3.8 GW, and the thing deciding whether a project goes ahead is no longer whether power exists, but whether you can connect to it.

I think the scarce asset is a finished connection to the wires, and it is not priced as scarce. I also say what would prove me wrong.

https://thephysicallayer.fyi/journal/the-queue-not-the-chip/

#AIInfrastructure #Grid #DataCentres

---

## 3 · Cooling is half the job

Electricity is not used up by computation. Almost every watt that goes into an AI chip comes back out as heat.

One cabinet now gives off as much heat as eighty space heaters. Air cannot carry that away, so the biggest plumbing change in the history of data centres is happening right now, and it does not care which chip company wins.

Why air died at 30 to 50 kW per rack, the three ways to cool with liquid, and what the PUE number actually measures.

https://thephysicallayer.fyi/journal/cooling-is-half-the-job/

#DataCentres #LiquidCooling #AIInfrastructure

---

## 4 · Ten thousand chips, one thought

A frontier AI model is too big to fit on any single chip. So it is sliced across thousands of them, and they have to swap notes for every single word.

If the wiring between them is even 10 per cent slow, the most expensive chips ever built sit idle. That is why a huge share of every AI dollar goes on cables and light, and why it is not extravagance. It is insurance on the other dollar.

https://thephysicallayer.fyi/journal/ten-thousand-chips-one-thought/

#AIInfrastructure #Networking #DataCentres

---

## 5 · The countertop is the bottleneck

When an AI writes its reply, the arithmetic is fast and the waiting for data is slow.

So the industry started stacking memory chips into little towers glued right next to the processor. Clever, expensive, and it explains which parts of the supply chain are actually scarce.

The view I hold: memory and packaging clear in quarters. Transformers and grid connections clear in years. They do not resolve together, and pricing them as one cycle is the mistake.

https://thephysicallayer.fyi/journal/the-countertop-is-the-bottleneck/

#AIInfrastructure #Semiconductors #DataCentres

---

## 6 · The rack runs out of copper

NVIDIA's next rack is designed to draw one megawatt. Feed that through today's 54-volt system and you need 200 kg of copper busbar in a single cabinet, and power shelves that take up more rack than the rack has.

So the industry is moving to 800 volts DC, borrowing the supply chain that electric-vehicle charging already built. Every figure in this one is traced to NVIDIA's own published architecture, not aggregators.

The constraint is moving out of the silicon and into the last fifty feet of power delivery.

https://thephysicallayer.fyi/journal/the-rack-runs-out-of-copper/

#AIInfrastructure #DataCentres #PowerElectronics

---

## 7 · The one part of the grid that money cannot hurry

Malaysia cut the wait to connect a new project to the grid from 36 months to 12, and pushed 33 projects through the scheme by March 2026.

That is a real achievement, and it is also the cleanest experiment anyone has run on the AI buildout, because of the thing it could not touch. A connection queue is two queues wearing one coat. The permission half is a policy variable and a government can rewrite it. The plant half is a large power transformer, built to order around a steel core made by very few mills worldwide, and it answers to nobody.

Policy compression has a floor, and the floor is made of steel and copper.

The piece covers why the first clock moved twenty four months, why the second one did not move at all, and what that gap does to any announced energisation date.

https://thephysicallayer.fyi/journal/the-part-money-cannot-hurry/

#AIInfrastructure #Grid #DataCentres

---

## 8 · The power it drops

On 22 July, 3.8 GW of data centre demand in northern Virginia switched itself off. PJM called it the largest event of its kind in its history.

Nobody lost power because the data centres stopped. The risk ran the other way. A grid is a tug of war rebalanced every second, and when one side lets go of the rope the other side falls over. Lose a generator and frequency falls, which every operator plans for. Lose a gigawatt of demand and it rises, which almost nobody planned for, because until recently no single customer was big enough to do it.

NERC issued its only alert of 2026 over this, a Level 3, binding the planning and operating spine of the grid. PJM is now weighing ride-through requirements. A data centre is quietly being reclassified from a customer into a piece of grid equipment with obligations.

The piece covers why a site protects itself by disappearing, why a sudden absence is harder than a sudden demand, and what happens to connection costs when behaviour becomes a condition of connecting.

https://thephysicallayer.fyi/journal/the-power-it-drops/

#AIInfrastructure #Grid #DataCentres

---

## 9 · The best argument against my own thesis

I have written twice that the constraint on AI is the wait to connect to the grid. The strongest objection is obvious: do not join the queue. Build your own power station on site and connect to nothing.

That objection is real and I take it seriously. Then you look at who makes the machines. GE Vernova reports 116 GW under contract, 53 GW firm and 63 GW in reserved manufacturing slots, mostly sold out through 2030. Siemens Energy reports 95 GW. The escape route from the queue is a queue, and it is already years deep.

The part usually left out: a turbine on your site still needs transformers, switchgear and a substation-grade yard, from the same constrained supply chain that makes a grid connection slow. You have swapped a queue you cannot control for one you can. That is worth something. It is not no queue.

The piece covers the objection at its strongest, why I think it relocates the problem rather than removing it, and the specific test that would prove me wrong.

https://thephysicallayer.fyi/journal/the-way-out-has-its-own-queue/

#AIInfrastructure #Grid #DataCentres

---

## 10 · What the battery is really for

Most people still think a grid battery is for storing cheap electricity and selling it later. That is no longer the job that explains who is buying them.

A battery now lets a data centre open before its grid connection is finished. The site draws what its partial connection allows, discharges to run harder during the day, and refills when demand is low. Nothing about that is an energy trade. It is a scheduling trick, and it is worth paying for because the alternative is eight months of not earning anything.

Developers planned 24 GW of utility-scale storage in the US this year. 12.9 GW of it, 53%, is in Texas, which is not half the American economy but is where the computing load is arriving. Storage is following the load, not the price.

If you model grid storage off electric vehicle adoption, you miss a buyer who does not care about cars and is working to a completely different clock.

https://thephysicallayer.fyi/journal/what-the-battery-is-really-for/

#AIInfrastructure #EnergyStorage #Grid

---

## 11 · Two governments, opposite policies, the same confession

There are two ways to find out what somebody thinks is scarce. Ask them, or watch what they do about it. The second is more reliable, because the first is a statement and the second is a cost.

Malaysia could make more grid connection, so it did. Tenaga committed RM43 billion and cut the wait for a connection from 36 months to 12, delivering 33 projects by March 2026. Note what the money bought: wires, substations and a faster approval process. Not power stations. A utility that thought it was short of electricity would be building generation.

Singapore cannot make more, so it rations. It froze new data centre approvals from 2019 to 2022, and now releases capacity in controlled batches with an efficiency condition attached, so the megawatts go to whoever wastes the fewest of them.

Nobody rations something that is plentiful. Two jurisdictions, different politics, different tools, opposite routes, same operational conclusion. One is spending to relieve a scarcity and the other is rationing access to it, and those are the only two things you can do about a scarce thing.

The piece also takes apart an official statistic in the middle of this that does not divide the way it should, and what the likely explanation says about announced capacity versus energised capacity.

https://thephysicallayer.fyi/journal/two-governments-one-confession/

#AIInfrastructure #Grid #DataCentres

---

## 12 · Bloom Energy is selling time

Bloom Energy's electricity costs more than the grid's. Oracle and one of America's biggest utilities are buying gigawatts of it anyway.

The US is not short of power in general. It is short of the ability to deliver a large new block of it to one site quickly, and grid waits now run past four years. Bloom's fuel cells switch on in months. Oracle swapped the gas turbines planned for its New Mexico campus for Bloom, and AEP signed for up to a gigawatt itself. Nobody bought Bloom because it was cheapest. They bought it because it was fastest.

The piece covers what Bloom actually makes, where the time premium shows up in Bloom's own margins, and the specific evidence that would prove me wrong.

https://thephysicallayer.fyi/journal/the-product-is-time/

#AIInfrastructure #FuelCells #DataCentres

---

## 13 · Vertiv is paid per megawatt

Vertiv makes no chips and writes no software, yet AI has made it one of the busiest suppliers in the buildout.

An ordinary server rack drew around 10 kW. An AI rack draws about 130, and air cannot carry that heat away, so every megawatt of building now needs liquid loops, coolant pumps and heavier power gear. Vertiv gets paid for every new building, and again for how much more equipment sits inside each one. Its own numbers show it: adjusted operating margin up 4.1 points to 22.6% last quarter, and service revenue growing faster than hardware.

The piece covers what Vertiv actually makes, where that second win shows up in its disclosures, and the specific evidence that would prove me wrong.

https://thephysicallayer.fyi/journal/every-megawatt-got-harder/

#AIInfrastructure #DataCentres #Cooling

---

## 14 · Jane Street has room to spare

Jane Street's new AI training centre in Texas has empty floor it cannot use.

The trading firm runs 4,032 Nvidia GPUs there, cooled by liquid, in a building designed for air. Each cabinet draws about 140 kW against 10 to 40 for an air-cooled one, so the power the utility agreed to supply now fills a fraction of the room. Its engineers run as close to that limit as they dare, with their own software ready to shut machines down before a breaker trips, because an idle GPU costs more than the hardware.

The piece covers why the floor went quiet, what it takes to put water where water was forbidden, and why power is so much harder to move around than cooling.

https://thephysicallayer.fyi/journal/room-to-spare/

#AIInfrastructure #DataCentres #LiquidCooling

---

## 15 · Jane Street commits to the power first

At Jane Street, the chips are now the last thing ordered.

The firm's head of physical engineering says generators, transformers and some liquid-cooling equipment take more than a year to arrive, so the building and the power are settled before the chip order goes in. On one site the team kept backup generators to the core of the system rather than the whole building, and switched its GPUs on six months sooner. His words: maybe not the best engineering decision, but the best business decision.

The piece covers why the order flipped, the generator the firm chose not to buy, and what would prove me wrong.

https://thephysicallayer.fyi/journal/power-first-chips-last/

#AIInfrastructure #DataCentres #Power

---

## 16 · Marvell collects the toll

Marvell is paid every time AI chips talk to each other, and it barely matters whose chips they are.

Copper stops carrying an AI signal after a few metres, so every link between cabinets turns electricity into light and back, and the chip doing that translation is very often Marvell's. Bigger clusters need more links, and every speed jump means new ones. Data centre work is now 79% of Marvell's revenue, and it is prepaying about $1 billion to suppliers to secure its next generation of optical chips.

The piece covers where copper stops and Marvell starts, what its own numbers show, and the change in optics that would prove me wrong.

https://thephysicallayer.fyi/journal/marvell-collects-the-toll/

#AIInfrastructure #Optics #DataCentres

---

## 17 · Oklo sells the electricity

Oklo, the nuclear start-up building small reactors for AI data centres, does not plan to sell a single reactor.

It plans to build them with its own money, put them beside the data centre, keep them, and charge for the electricity under contracts lasting decades. That makes it a power company, and it means it earns nothing from power until its first reactor runs. So far only Meta has put binding money behind its agreement; the 12 gigawatt deal with Switch is still a framework.

The piece covers why a data centre wants a reactor next door, what Oklo's own numbers show, and the fuel and licence problems that could stop it.

https://thephysicallayer.fyi/journal/oklo-sells-the-electricity/

#AIInfrastructure #Nuclear #DataCentres

---

## 18 · Nebius is paid for what is switched on

Microsoft and Meta, two of the biggest data centre builders on earth, both rent AI capacity from Nebius.

They were not short of chips. They were short of buildings with the power on. Nebius expects 5 gigawatts of power contracted by the end of 2026 and about 1 gigawatt connected, and its contracts pay only for capacity that is running, at $20 to $25 million per megawatt a year on its latest deals.

The piece covers what Nebius actually sells, what its own numbers show, and the Meta report that would prove me wrong.

https://thephysicallayer.fyi/journal/nebius-paid-for-what-is-switched-on/

#AIInfrastructure #DataCentres #Power

---

## 19 · Corning lays the glass

Meta, Amazon and Nvidia have all signed deals this year with a 175-year-old glass company.

Corning makes the optical fibre AI chips talk through once copper runs out, about two metres from the chip. Every new chip generation replaces the plugs at each end, but the glass in the ceiling stays, and a campus of AI buildings needs far more of it between halls than inside them. Corning's data centre business grew 65% last quarter, and it says demand is running above what its factories can make.

The piece covers why the glass is hard to make, what Corning's own numbers show, and the 2001 fibre bust that could repeat.

https://thephysicallayer.fyi/journal/corning-lays-the-glass/

#AIInfrastructure #Optics #DataCentres

---

## 20 · Broadcom wins either way

When OpenAI built its first chip to rely less on Nvidia, it built it with Broadcom.

Broadcom also makes the switch chips that let thousands of AI processors work as one machine, Nvidia's included. So whether the cloud giants keep buying Nvidia or design their own, the work runs through the same company. Its AI revenue was $16.7 billion last quarter, up 221% on a year earlier, with six custom chip customers behind it.

The piece covers why the switch sets the size of the machine, why the giants want their own chips, and the Google work that could prove me wrong.

https://thephysicallayer.fyi/journal/broadcom-wins-either-way/

#AIInfrastructure #Networking #DataCentres

---

## 21 · TI feeds the chip

The AI processor that costs tens of thousands of dollars cannot run on the electricity delivered to it.

Power reaches the rack at 54 volts, soon 800, and the chip runs below one volt, so a crowd of small chips steps it down millimetres away. Texas Instruments makes many of them, some for cents, and is spending more than $60 billion on its own American factories to make them cheaper. Its data centre business doubled last quarter, from a base of 9% of revenue.

The piece covers why the last centimetre is the hard part, TI's factory bet, and what would prove me wrong.

https://thephysicallayer.fyi/journal/ti-feeds-the-chip/

#AIInfrastructure #Power #DataCentres

---

## 22 · TSMC says it is the bottleneck

I have argued that the grid, not the chip, is what holds AI back. TSMC's chief executive disagrees.

Almost every advanced AI chip, whoever designs it, is made in TSMC's factories, and TSMC says a new one takes two to three years to build and one to two more to fill. Its 2026 spending of up to $64 billion adds almost nothing to this year's output, and its packaging capacity is so tight it is limiting customers' growth.

The piece covers why one company makes everyone's chips, the clock on a chip factory, and what would prove me wrong.

https://thephysicallayer.fyi/journal/tsmc-says-it-is-the-bottleneck/

#AIInfrastructure #Semiconductors #DataCentres

---

## 23 · Lumentum makes the light

In March, Nvidia paid $2 billion to a laser company, and another $2 billion to its rival on the same day.

Past a couple of metres, AI chips talk to each other in light, and that light starts in a laser grown on indium phosphide, a crystal that only a few factories in the world can work at volume. Lumentum doubled its revenue in a year and says it will still be significantly behind demand at the end of 2026.

The piece covers why silicon cannot make light, what Lumentum's own numbers show, and what would prove me wrong.

https://thephysicallayer.fyi/journal/lumentum-makes-the-light/

#AIInfrastructure #Optics #DataCentres

---

## 24 · Schneider Electric sells the finished system (site live 7 Oct 2026; LinkedIn scheduled by Tommy)

Schneider Electric's fastest-growing business is not the breakers and switches it is best known for.

Its Systems business, which includes power rooms and cooling plants built and tested in a factory, grew 28% in the second quarter against 13% for its catalogue products. Schneider says data centres led that growth. I think the reason is on the building site: an AI hall cannot switch on until every panel is installed and tested, and the people who do that work are scarce.

The piece covers how Schneider splits what it sells, the shift in its own numbers, and why it is spending on design tools as well as factories.

https://thephysicallayer.fyi/journal/schneider-sells-the-finished-system/

#DataCentres #Electrification #EnergyInfrastructure

---

## 25 · GE Vernova sells the wait (site live 9 Oct 2026; LinkedIn Fri 6 Nov, 11:30)

GE Vernova signed 41 gigawatts of gas turbine contracts in the first half of 2026 and shipped seven.

Most of those contracts are paid places in a queue for 2030 and 2031, and customers have handed over billions in deposits to hold them. GE Vernova is using that money to stretch the factories it already has, not to build new ones. For anyone planning to skip the grid queue with their own power, that is the number that sets the date.

The piece covers what a slot reservation is, where the deposits show up in GE Vernova's filings, and why the queue is likely to stay years long.

https://thephysicallayer.fyi/journal/ge-vernova-sells-the-wait/

#GasTurbines #DataCentres #EnergyInfrastructure

---

## 26 · Fluence is short of American-made (site live 12 Oct 2026; LinkedIn Mon 9 Nov, 11:30)

Fluence's new Houston battery factory spent this summer running on generators, because its own grid connection was late.

Fluence sells data centres a way to switch on before their grid connection is ready. Its overseas factories are working well, by its own account, but American tax rules reward systems made in America, and the Houston line averaged under one unit a day in August against a plan of eleven. In the United States the scarce thing is not the battery, it is the battery that qualifies.

The piece covers how the tax rules turn "made in America" into the constraint, what data centre buyers are actually paying Fluence for, and the test that would prove me wrong.

https://thephysicallayer.fyi/journal/fluence-short-of-american-made/

#EnergyStorage #DataCentres #EnergyInfrastructure

---

## 27 · Hitachi Energy plans the queue (site live 14 Oct 2026; LinkedIn Wed 11 Nov, 11:30)

Hitachi Energy is spending more than $9 billion on factories, and it still expects about three years of orders to be waiting in 2030.

It is the largest maker of the transformers and long-distance power links that connect data centres and power stations to the grid. Its unfilled orders reached $63.6 billion in June, about three years of sales, and it told investors that ratio should stay at two and a half to three times while its output nearly doubles. For anyone waiting on a substation, that is the plan for how long the queue lasts.

The piece covers what Hitachi Energy makes, how its queue is measured in years, and why its new factories keep the queue rather than clear it.

https://thephysicallayer.fyi/journal/hitachi-energy-plans-the-queue/

#Transformers #DataCentres #EnergyInfrastructure

---

## 28 · Eaton's order book outruns it (site live 16 Oct 2026; LinkedIn Fri 13 Nov, 11:30)

Eaton shipped 18% more electrical gear in the year to June, and its order book grew 33%.

Eaton makes the switchgear, backup power and wiring that sit between the grid and the racks in a data centre. It is spending more than $1 billion on two dozen capacity projects, yet the orders waiting in its North American business have grown from about eleven months of sales to about thirteen. The big new plants that could close the gap arrive in 2027.

The piece covers what Eaton makes, how its queue is measured in months, and what that queue does to its margin.

https://thephysicallayer.fyi/journal/eaton-order-book-outruns-it/

#DataCentres #Electrification #EnergyInfrastructure

---

## 29 · Siemens Energy measures the shortage (site live 20 Oct 2026; LinkedIn Mon 16 Nov, 11:30)

Siemens Energy has published its own estimate of the transformer shortage, and on its chart demand is still ahead of every factory in 2030.

It covers what Siemens Energy calls all market players for large power transformers in Europe and North America. Demand ran about 40 per cent ahead of capacity in 2025 and is still about 10 per cent ahead in 2030, even after capacity grows by about 60 per cent. A smaller shortage still adds to the pile of unfilled orders each year, and Siemens Energy's own grid backlog has grown from €33 billion to €51 billion in under two years.

The piece covers what the chart shows, why a narrowing gap still adds to the pile, and why Siemens Energy's grid business now out-earns its gas turbines.

https://thephysicallayer.fyi/journal/siemens-energy-measures-the-shortage/

#Transformers #DataCentres #EnergyInfrastructure
