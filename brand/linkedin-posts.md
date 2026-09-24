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
