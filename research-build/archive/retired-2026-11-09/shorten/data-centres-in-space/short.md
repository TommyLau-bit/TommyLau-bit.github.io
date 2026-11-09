<a id="data-centres-in-space"></a>

SpaceX has asked American regulators for room to put up to one million AI computing satellites into orbit. It has also told them, in a letter of 29 May 2026, what one of those satellites would weigh: 3,000 kilograms.

That number is the hinge of this piece. In orbit the sunlight is free and there is no queue for the grid. But the solar array that collects the sunlight, and the radiator that throws its heat away, are both launched and paid for by the kilogram. On the mass SpaceX filed and the power it publishes, its satellite carries about 58 kilowatts of computing per tonne; its own page claims 75. The target is 100.

So the claim is this. In orbit the sunlight is free but the kilograms are the bill. By the end of 2028, no operator will report a computing satellite in service at SpaceX's target of 100 kilowatts per tonne launched, and no rocket company will publish a price low enough to make the sums easy.

{{ANALOGY}}

## Why would anyone put a data centre in orbit?

Because on the ground the scarce thing is the plug, and in orbit there is no plug to queue for.

A data centre on the ground needs a grid connection, and in America the wait for one now runs to years, as told in [America rations the plug](/journal/america-rations-the-plug/). It also needs land, water or air for cooling, and permits from towns that increasingly say no.

In orbit, sunlight arrives at about 1,361 watts per square metre, with no clouds and no night for much of the year. Google's project lead, Travis Beals, wrote that in the right orbit "a solar panel can be up to 8 times more productive than on earth" (4 November 2025). The right orbit is a **dawn-dusk sun-synchronous orbit**: a near-polar path that rides the line between day and night, so the panels face the sun almost all the time. Google's design uses it, and Starcloud, a start-up building computing satellites, has filed for it.

So the pitch is simple: free power, no queue, no water. The rest of this piece asks what that power costs to collect and what its heat costs to throw away, both counted in kilograms.

## What would an orbital data centre look like?

On SpaceX's own published design, a satellite a little wider than a jumbo jet's wings, mostly made of solar array.

SpaceX calls its system Starmind and its first satellite AI1. Its web page, read on 7 November 2026, gives the satellite a "Compute payload Up to 250 kW peak / 175 kW average". It lists a "Solar array 210 kW" at "250 W / m²", and a "Deployable liquid radiator 160 m²". A **kilowatt (kW)** is a thousand watts; 175 kW is about one and a half of Nvidia's GB200 racks, the AI cabinets now filling data halls on the ground.

At 250 watts per square metre, a 210 kW array covers about 840 square metres, my arithmetic: more than three tennis courts. The radiator, at 160 square metres, is about a fifth of that.

SpaceX's letter to the Federal Communications Commission (FCC), the American regulator of satellites, gives a "Mass" of 3,000 kg for satellites below 600 kilometres. The letter was filed on 29 May 2026, when SpaceX's published plans were smaller: its S-1 spoke of early satellites "generating 100 kilowatts of compute power". So the 3,000 kg may belong to the earlier design.

Google's design is a cluster rather than one large craft. Its research paper, "Towards a future space-based, highly scalable AI infrastructure system design", sketches 81 satellites flying in formation at about 650 kilometres, linked by lasers. Each would carry Google's own AI chips, its **TPUs**.

{{FIG1}}  <!-- The array is five times the radiator, and both are launched -->

## Why can heat leave only as light?

Because a vacuum has nothing in it to carry heat away.

On the ground, a data centre's heat leaves through air or water, as told in [heat and water](/journal/heat-and-water/). In orbit there is no breeze. SpaceX's prospectus says it plainly: "thermal control must be accomplished through radiation rather than convection and conduction" (12 June 2026).

Every warm object glows, mostly in infrared light we cannot see. The **Stefan-Boltzmann law** says the heat radiated rises with the fourth power of the surface's **absolute temperature**, measured in kelvin from absolute zero. Each 1% rise in absolute temperature sheds about 4% more heat. A panel at 67°C sheds about 1.8 times what it sheds at 20°C, on my arithmetic.

**Emissivity**, from 0 to 1, is how well a surface glows compared with a perfect black one. Good white coatings reach about 0.92. With emissivity near its limit and area costing mass, temperature is the only free lever.

{{FIG2}}  <!-- A radiator sheds more heat the hotter it runs, by the fourth power -->

## How large must the radiator be?

That depends on how hot it may run, and the chip decides that.

A radiator cannot run hotter than the coolant feeding it, and the coolant cannot run hotter than the chips allow. Nvidia's newest racks take coolant at up to 45°C, and it leaves the chip at about 55°C, Nvidia says (16 March and 21 June 2026). That is the ceiling for any panel carrying their heat.

Elon Musk, SpaceX's chief executive, gave SpaceX's figure in an interview the company filed with the SEC, the securities regulator (9 June 2026): radiators shedding about 1,400 watts per square metre, "radiating on both sides". Read as watts per square metre of panel, which the interview does not specify, a shaded two-sided panel at emissivity 0.92 sheds that only near 67°C, on my arithmetic. That is hotter than the coolant leaving Nvidia's chips today.

SpaceX's current page implies a cooler panel. Its 175 kW over 160 square metres is about 1,090 watts per square metre, which the same panel sheds near 47°C in deep shade, or near 54°C once the Earth's own infrared glow is counted, my arithmetic. That fits warm-water coolant with little to spare. At the cold end, Starcloud's white paper nets 633 watts per square metre from a panel at 20°C. Its sum counts the Earth's glow at about 14 watts, using the coating's absorption of sunlight. In the infrared a surface absorbs at its emissivity, about 0.92, so on my arithmetic the Earth adds about 63 watts and the net falls to about 585.

So a radiator sheds somewhere between about 600 and 1,400 watts per square metre, depending on how hot the chip lets it run. A 175 kW satellite needs between about 125 and 300 square metres.

## Why is a radiator heavy?

Because it is a large, thin, leak-proof panel that must unfold in orbit, survive debris and run for years with no repair crew.

The International Space Station gives the best-known weight. NASA lists six radiator units, each "1,122.64 kilograms", together rejecting 70 kW: about 14 kg per square metre of panel, my arithmetic. NASA Glenn, the agency's Ohio laboratory, lists heat-pipe radiators at "~3 kg/m2", a design tested at full scale in 2011. A **heat pipe** is a sealed tube with a wick inside that moves heat with no pump, so one puncture loses one pipe, not the loop.

At 1,400 watts per square metre, those weights give between about 2 and 10 kg per kW of heat, my arithmetic. The light end is a design tested on the ground, at 127°C, far hotter than a chip loop; the heavy end has flown for decades.

{{FIG3}}  <!-- Flown radiators are heavy; light ones have been tested only on the ground -->

Real radiators must fold under a rocket's nose, carry spare loops and armour against debris, and cannot be fixed. SpaceX's own risk factors say its orbital computing "will not be easily repaired or upgraded".

## Is the sunlight really free?

The sunlight is. The array that catches it is not, and it may weigh more than the radiator.

Redwire, which makes the roll-out arrays flying on the space station, publishes power and mass for its range. Its products deliver about 71 to 124 watts per kilogram, my arithmetic from its table. That is 8 to 14 kg of array for each kW of electricity, before any chip, radiator or structure. NASA's survey of small-satellite power says arrays "are strongly clustered around ~30 W/kg" (7 May 2026).

And the dawn-dusk orbit is not always sunny. At 650 kilometres, on my arithmetic, there are about three months a year with an eclipse on every orbit, up to about 20 minutes of each 98-minute circuit. Riding through it at 175 kW takes roughly 220 to 390 kg of battery cells.

## What does a kilowatt weigh in orbit?

More than SpaceX's target allows, on every published figure I can find.

SpaceX's prospectus speaks of 100 gigawatts a year "via satellites carrying over 100 kilowatts of compute power per metric ton". Turned upside down, that is 10 kg launched for each kW of computing. Everything sits inside that 10 kg: array, radiator, chips, structure, batteries and shielding.

Now add up the parts at today's published weights. The array is 8 to 14 kg per kW. The radiator is 2 to 10. A ground AI rack weighs about 11 kg per kW, though a space-built payload would shed its steel. Batteries for the eclipse season add 1 to 2. The array alone sits near or over the whole budget.

{{FIG4}}  <!-- The array alone uses most of SpaceX's 10 kilogram budget -->

SpaceX's own numbers say the same. Its page gives "Vehicle efficiency 75 kW / ton", a quarter short of the prospectus target. Its FCC mass of 3,000 kg, against its page's 175 kW average, gives about 58 kW per tonne, my arithmetic; even the 250 kW peak gives about 83. For comparison, Google's paper estimates a Starlink V2 mini, one of SpaceX's internet satellites, at 575 kg and about 28 kW. That is about 49 kW per tonne for the whole craft, and only part of that power goes to anything like computing.

{{FIG5}}  <!-- No published figure reaches SpaceX's target of 100 kW per tonne -->

## Can a heat pump shrink the radiator?

<a id="heat-pump-trade"></a>

Sometimes, but it costs array to save radiator, and warmer chips are the cheaper lever.

A **heat pump** moves heat from a cooler place to a hotter one, using work, like a fridge in reverse. It could take the chips' coolant at 45°C and raise the radiator to 100°C, where it sheds almost twice as much per square metre. But on my arithmetic, lifting 1 kW of heat that way takes about 0.35 kW of work, and that power needs more array. A pump saves mass only if the array weighs less than about a fifth as much per square metre as the radiator, which can be true with station-weight radiators but not with light ones.

The cheaper lever is the chip. Running the chips' coolant at 60°C instead of 45°C cuts radiator mass by about 18%, on my arithmetic, with no extra array at all. So in orbit a chip's temperature rating is a launch cost, the same lever that makes [warm water work on the ground](/journal/heat-and-water/).

## Could radiation, latency or bandwidth bind first?

Each is real, but each costs a margin. Mass costs on every kilowatt of every launch.

Google tested its Trillium TPU in a proton beam and, revising its paper on 17 June 2026, found silent errors in the chip's logic that come to about nine per chip per year, on my arithmetic. That figure rests on a mission dose that assumes "significant shielding (e.g. 10 mm Al equivalent)". Ten millimetres of aluminium weighs 27 kg per square metre of enclosure, my arithmetic, so the radiation result is bought with mass too.

Latency is short: light takes about 2 milliseconds each way from 650 kilometres straight overhead. Bandwidth to the ground is the narrow lane, so orbit suits answering questions, where a reply is a few kilobytes, more than training, which moves vast data.

## What has actually flown?

Small craft running single chips, and no weighed computing satellite near the target.

Starcloud-1, a 60 kg satellite, went up in November 2025 with one Nvidia H100 GPU, Starcloud says. It has published no power figure. If its chip ran at full power, about 700 watts, that is at most about 12 kW per tonne, my arithmetic.

Google and Planet, the satellite maker, launched a Suncatcher prototype on 1 October 2026. NPR, the American public broadcaster, reported that it carries four TPUs and would run "15 minutes at a time due to heat management constraints", and that it "is in a standard orbit and uses batteries". So Google's first data-centre-class chip in orbit is to run minutes at a time, and the limit NPR gave is heat. Google has published no mass.

China's Three-Body Computing Constellation had 20 satellites in orbit after a second batch on 14 October 2026, press reports say, and publishes no power or mass. The announced plans run in gigawatts; what has flown runs to a few kilowatts.

## What does launch cost, and when might it fall?

Thousands of dollars a kilogram today, and Google cites $200 as the level where launch could stop being the main cost.

Google's paper uses a "current launch price $3,600/kg, based on Falcon 9 (reusable configuration)", SpaceX's working rocket. That is Google's estimate, not a published price. Google expects launch "may reach ≲$200/kg by the mid-2030s", which "would require ∼180 Starship launches/year".

Starship, SpaceX's much larger rocket, is the reason anyone expects that fall. It reached orbit for the first time on its 14th flight, in the third quarter of 2026, SpaceX said (20 October 2026). SpaceX has published no Starship price per kilogram.

## How does the bill compare with a hall on the ground?

At today's launch price, the launch bill alone is five to 26 times a ground hall's power bill. At $200 a kilogram, it falls inside the ground's range.

Google turns launch cost into a "launched power price": the launch bill for each kilowatt, spread over a five-year life. For a Starlink-class satellite at $3,600 a kilogram, that is $14,700 per kW per year. An American AI hall's power bill, on Google's range of electricity prices and overheads, is $570 to $3,000 per kW per year.

At $200 a kilogram, the same satellite falls to $810, inside the ground range. That is the case for orbit in one number. But it counts launch only: chips, arrays and the satellite itself are left out on both sides.

{{FIG6}}  <!-- At today's fare orbit costs five to 26 times the ground; at $200 it falls inside its range -->

And the fare recurs. A satellite flown on a five-year life must be launched again when it wears out. On the ground, the hall and its [grid gear outlast three or four chip generations](/journal/the-equipment-queue/). The launched power price is kilograms per kilowatt times the fare, over the years of life. Halve either and the bill halves. So the strongest case against me is both falling at once.

## So who holds the scarce thing, and what should an investor watch?

In orbit the scarce thing is not power. It is mass to orbit, and the kilograms per kilowatt that decide how much of it each satellite needs.

If the claim is right, three parts of the chain gain. **The launcher**, paid per kilogram, gains whether orbit works or not. SpaceX flew both computing prototypes now in orbit, Starcloud's and Google's, and also designs its own computing satellite, which makes it toll keeper and competitor at once. **The lightweight makers**, of arrays, radiators and heat pipes, gain if orbit works at all, because every kilogram they save is a launch fare saved. Astro Digital built Starcloud-1, and Planet built Google's prototype with Google; Redwire makes roll-out arrays. **The ground plug** keeps its value while orbit stays heavy. SpaceX's own risk factors warn that if "advances in nuclear energy" or similar ease ground constraints, its orbital computing "may be materially diminished".

The SEC asked SpaceX in April 2026 for the "power-to-mass ratios" behind its goal and the "total system mass". The prospectus said the figures "continue to be refined".

The readings are specific. SpaceX's quarterly reports, for a satellite mass and kilowatts. Google's twin interconnected satellites, due in 2027, for a published mass and radiator. Starcloud-2, which its page says will be "fully operational in sun-synchronous orbit by 2027". And any published Starship price per kilogram.

## What would prove me wrong

Two observations would break the claim. An operator discloses, in a filing, a release or a regulator's record, a computing satellite in service at 100 kW or more of computing per tonne launched, by 31 December 2028. Or a launch provider publishes a price to low Earth orbit of $200 a kilogram or less by then.

The satellites that could be weighed against the target fly in 2027 and 2028. A satellite mass in SpaceX's reports at or near 1.75 tonnes for 175 kW, or a published mass for Google's pair, would move me sooner. So would a flown array above 250 watts per kilogram, or a flown radiator several times lighter per square metre than the station's. Designs would not move me: a preprint's 500 watts per kilogram assumes "custom solutions for all components", and is not a satellite in service.

The claim stands on two legs. The first, that a kilowatt in orbit is heavy, rests on physics and on the weights of flown hardware. The second, that the fare is high, rests on a price that reuse can move fast. The legs multiply, so a fall in both would break the idea even before either test is met.

Musk said that "cooling is actually much easier in space than it is on Earth". Off the chip, perhaps: there is no dust and no humidity. Out to the world, heat can leave only as light, a few hundred to about 1,400 watts per square metre, and every square metre is launched. At the scale of the fleet, 100 gigawatts a year needs "approximately one million metric tons to orbit annually", the prospectus says. In orbit the sunlight is free, and the kilograms are the bill.
