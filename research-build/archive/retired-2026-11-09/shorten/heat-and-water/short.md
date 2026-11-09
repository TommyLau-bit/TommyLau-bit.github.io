<a id="heat-and-water"></a>

AI data centres are blamed for drinking towns dry. Yet a US government laboratory has found that a large liquid-cooled AI hall can stop evaporating water altogether, and barely change how much electricity it uses over a year.

That finding is the hinge of this piece. Heat decides how AI is cooled: with liquid, pressed against the chip. Water decides where and how that heat leaves the building, not how many halls get built. Liquid makes going without water cheap; it does not make it happen, and it does not make it free on the hottest afternoon.

So the claim is this. In AI data centres heat sets the cooling method, and water sets the roof and the site, not the count. Where an operator judges water scarce, it cools with air or recycled water, and I have found no powered AI campus cancelled over water rather than redesigned.

{{ANALOGY}}

<a id="cooling-is-half-the-job"></a>

## Why does every watt a chip uses become heat?

Because a chip does no lasting work in the physical world, so for cooling a rack's power and its heat are the same number.

Nvidia, the leading AI chip designer, puts its GB200 NVL72 rack at about 120 kilowatts (kW) in its user guide. A **rack** is the steel cabinet, about the size of a wardrobe, that holds a data centre's computers. That one cabinet releases as much heat as about eighty hairdryers on full, my arithmetic, all day and all night.

This is why cooling is half the job of an AI data centre. Every kilowatt the grid delivers to the chips must be carried back out of the building, or the chips slow down and then fail. Cooling is really three jobs: pulling heat off the chip, carrying it across the building, and releasing it outside. The first job is now settled for AI, and only the third can spend water.

## Why can air no longer carry the heat away?

Because air holds very little heat, so cooling a hot rack with air means moving enormous volumes of it.

A cubic metre of water carries about 3,600 times more heat than a cubic metre of air, for the same rise in temperature, my arithmetic from textbook values. ASHRAE, the American body of heating and cooling engineers, wrote in 2021 that a 40 to 50 kW rack "could be up to 5000 cfm", cubic feet per minute, while the best floor tile delivers "1900 cfm".

So a 120 kW rack would need the air of about eight of the best floor tiles, pushed through one cabinet. Fans that hard eat power: ASHRAE found fans in dense servers using 10 to 20% of server power, against under 2% in many older servers. Every watt spent on fans is a watt the plug cannot give to computing.

{{FIG1}}  <!-- One AI rack would need the air of eight of the best floor tiles -->

Microsoft's cloud chief, Scott Guthrie, put it plainly on 18 September 2025: "Traditional air cooling can't handle the density of modern AI hardware."

## How does liquid take the heat off the chip?

Through a chain of sealed loops, each handing the heat to the next without the liquids ever mixing.

The first link is the **cold plate**: a copper block fixed onto the chip, with fine channels inside through which coolant runs. Nvidia describes that coolant as "75% water and 25% propylene glycol" (21 June 2026). The rack loop runs to a **coolant distribution unit (CDU)**: pumps, filters and a heat exchanger in one box. Google built its own CDU, Project Deschutes, and reported fleet-wide availability of about 99.999% since 2020 (30 April 2025). It passes the heat into the building's own water, the **facility water**, which carries it to the roof. There it meets the outside air, in the only step where water can be spent.

{{FIG2}}  <!-- Only the last step can spend water -->

Immersion, where whole servers sit in a bath of non-conducting liquid, is a side branch. Nvidia's racks are built around cold plates, so for AI in 2026 cold plates are the mainstream and immersion a niche.

## How warm can the coolant run, and why does that matter?

Much warmer than most people expect, and every degree of warmth matters later, on the roof.

The silicon itself runs at around 85 to 105 degrees, so coolant can be far cooler than the chip and still take its heat. Nvidia's racks for Vera Rubin, which it said would ship in the second half of 2026, are "designed to operate with 45°C (113°F) warm-water inlet temperatures" (16 March 2026). The coolant "exits at roughly 55 degrees" (21 June 2026). The building's water can arrive at the CDU at about 41 degrees, Nvidia's design says, and Rubin's compute trays are "fanless".

Running the hottest rack on 45 degree coolant reverses what ASHRAE expected in 2021, when it warned that 45 degree water "will become increasingly difficult to use as the heat flux at the socket increases". Why it matters: Nvidia says running colder means "diverting a larger share of the facility's limited grid allocation into cooling instead of compute" (25 March 2026). It claims warm cooling unlocks "up to 10% additional NVL72 racks" in the same power budget, a vendor estimate rather than a measurement.

<a id="room-to-spare"></a>

## Can an old air-cooled hall take liquid?

Yes, but as a refit, and the refit is the slow part. Jane Street, a trading firm, describes one Texas hall with "4,032 GPUs across 56 racks, retrofitted for liquid cooling". It secures its power first and picks its chips last, as told in [power first, chips last](/journal/america-rations-the-plug/#power-first-chips-last). Amazon Web Services built its own in-row heat exchanger, the press reported in July 2025, and Meta uses heat exchangers at the rack: liquid at the chip, air still in the room.

## What are the three ways to put heat into the outside air?

Sweat, a fan, and a fridge: a cooling tower, a dry cooler and a chiller. They differ in water, power and one key temperature.

A **cooling tower** sprays the warm water over packing while fans pull air through it, and a small part evaporates. Shedding a kilowatt-hour of heat purely by evaporation takes about 1.5 litres, my arithmetic, and drained water adds a third or more. Its advantage is that evaporation cools water towards the **wet-bulb temperature**, what a thermometer in a wet cloth reads, below the air's own.

A **dry cooler** is a large radiator with fans. The water stays sealed inside its coil, so none is lost, but it can only cool the water to a few degrees above the ordinary air temperature. **Adiabatic assist** is a dry cooler that wets pads in front of its coil on hot hours, spending water only when it must.

A **chiller** is a refrigerator for water. A compressor can make water colder than the outside air, at the price of electricity. An **air-cooled chiller** throws that heat out with fans and uses no water; a **water-cooled chiller** throws it into a tower. A datasheet from Vertiv, which makes both power and cooling gear, for one air-cooled model implies removing 1 kW of heat costs about a quarter of a kilowatt at 35 degree outside air, and more as the air gets hotter.

{{FIG3}}  <!-- The tower saves power with water; the dry cooler saves water with power -->

## Why does warm coolant let fans do most of the work?

Because a dry cooler works whenever the outside air is a few degrees cooler than the water, and warm water makes that almost always true.

An old air-cooled hall with chilled water at about 18 degrees could use a dry cooler alone only when the air was below about 10 to 13. With Nvidia's building water at about 41 degrees, the same dry cooler works alone whenever the air is below about 33 to 36. My arithmetic assumes a typical gap of 5 to 8 degrees across the dry cooler. In many climates that is nearly every hour of the year, though not in the hottest deserts.

Nvidia's cooling director, Ali Heydari, says chillers may be needed in "maybe 1% of the year", and only "in some climates" (21 June 2026). One per cent of a year is about 88 hours. They are not random hours: they are the hottest afternoons.

{{FIG4}}  <!-- At 41 degrees, a dry cooler needs no help for most hours of the year in many climates -->

## What does going dry cost a liquid-cooled hall?

Over a year, almost nothing in power, on the best public model. That is the US government laboratory's finding.

Lawrence Berkeley National Laboratory (LBNL), which studies energy for the US government, published its national data centre report in December 2024. It simulated nine cooling designs across 965 American weather stations, in over a million runs. The measure of power is **PUE**, power usage effectiveness: total power entering the building divided by power reaching the computers. At 1.1 the overhead is a tenth.

For a large liquid-cooled hall, the lab's medians, as I read them from its Figure 4.4, are close. With a cooling tower, PUE is about 1.13 and the hall consumes about 2.0 litres of water per kWh. With a dry cooler backed by an air-cooled chiller, PUE is about 1.10 and water is zero. With adiabatic assist, about 1.10 and 0.13 litres. The lab's own words: liquid cooling's higher temperature means "less chiller run hours and less adiabatic assist".

An air-cooled hall is different. Dropping the tower costs an air hall 0.1 to 0.3 of PUE, depending on what replaces it.

{{FIG5}}  <!-- In a liquid hall, going dry costs almost nothing in yearly power -->

Two warnings travel with these numbers. They are annual averages from typical weather, and the lab publishes no worst-hour figure, which is where a dry roof is weakest. And the lab warns its PUEs "assume systems are commissioned and operate as designed. This is rarely the case."

## Where is most of a data centre's water: on the roof, or at the power station?

On a national average, at the power station, by about twelve to one. But a town sees the site's draw, not the plant's.

The lab estimates that American data centres consumed 66 billion litres of water on site in 2023, while the power stations making their electricity consumed "nearly 800 billion liters". That is a "national average of 4.52 L/kWh" per kWh a data centre bought. So PUE is also a water number: a hall's whole water bill, on the lab's averages, is its roof water plus PUE times 4.52 litres. The sum is mine, built only from the lab's numbers.

{{FIG6}}  <!-- Counted whole, a dry liquid hall uses about half the water of an air hall with a tower -->

On that sum, a midsize air hall with a tower uses about 9.8 litres per kWh in all, and a large dry liquid hall about 5.0. The comparison sets a midsize air hall against a large liquid one, so size accounts for part of the gap. In the air hall, dropping the tower saves 2.9 litres on the roof but spends about 1.4 again at the power station, through a higher PUE. But the 4.52 includes evaporation from hydroelectric reservoirs and ignores power contracts. And the power station's water is usually in another basin. So "most of the water is at the power station" is true on paper, and it does not answer the question a town is asking.

<a id="water-is-a-siting-problem"></a>

## What do the largest cloud operators actually do?

They evaporate where they judge water plentiful, and cool with air where they judge it scarce. Google says so in writing; the others show it in their designs.

**Google** consumed 10,523 million gallons of water at its data centres in 2025, on its 2026 Environmental Report, and publishes consumption site by site. Council Bluffs, Iowa, its largest, consumed 1,346.0 million gallons in 2025; The Dalles, Oregon, 469.0. Google rated The Dalles' sources as not at high risk in 2022, and it cools there with water.

Where it judged water scarce, it chose air. In its 2025 report Google said the sources at Waltham Cross, in England, "present a high risk of water depletion and scarcity", so it "decided to utilize air cooling technology". It said it was taking "a similar approach" at Mesa, Arizona, and Canelones, Uruguay.

On 3 June 2026 Google made it policy: "If a water source is at high risk, we choose air cooling or recycled water." It also wrote that in many places water cooling can cut a data centre's energy use by "approximately 10%" against air. That prices the trade across Google's fleet, more than the lab finds for a liquid hall.

Mesa now has a row: 9.7 million gallons consumed in 2025, its first listed year, against 469.0 at The Dalles. But Mesa carries no "air-cooled facility" footnote in the 2026 table, unlike Phoenix and seven others, and Google has not said why. Waltham Cross and Canelones have no row of their own yet.

{{FIG7}}  <!-- Where Google judged the water scarce, it used almost none -->

**Microsoft** went furthest on design. Since August 2024, it said on 9 December 2024, all its new data centre designs evaporate zero water for cooling, using chip-level liquid in a closed loop. The cost is "a nominal increase in our annual energy usage", with no number published. Its first such sites, in Phoenix and Mount Pleasant, Wisconsin, were to pilot in 2026 and come online in late 2027. **Amazon Web Services** says its direct evaporative cooling "requires water for less than 10% of the year" where weather permits. **Meta** said on 27 August 2026 that most of its newest AI halls use closed-loop liquid cooling.

## Is the chiller being designed out?

No. Its hours shrink, but its numbers grow, and the makers say so in their own results.

A chiller fleet is sized for the hottest hour plus spares, so the count of chillers follows the megawatts, not the hours. What changes is the type: air-cooled chillers, which use no water, rather than water-cooled ones with towers.

Carrier, the American heating and cooling maker, said its data centre orders had passed $3 billion so far in 2026, up nearly 350%. It reported "great demand for our new 2 megawatt and 3 megawatt air-cooled chillers" (29 October 2026). Vertiv said it was "on track to doubling chiller production capacity by year-end" (28 October 2026). So chiller orders and the dry roof are not in conflict, because most of the chillers being ordered are themselves dry.

The makers are straining: Munters, the Swedish maker, said "constraints remain industry-wide" (23 October 2026). But when they name what paces their customers, they name power. The finance chief of Johnson Controls, whose York brand makes chillers, said some customers face "power and some electrical infrastructure limitation" (27 October 2026). No primary source names a hall held up by cooling gear.

<a id="the-worst-afternoon"></a>

## What happens on the worst afternoon?

This is where going dry is really paid for: not in yearly kilowatt-hours, but in peak megawatts.

A grid connection caps a building's maximum draw, at every instant. So the computing a site can run is set by its worst hour's overhead, not its yearly average. A dry roof is weakest exactly then, when the outside air may be warmer than the water and a chiller must carry the load. Nvidia's engineers write that heat rejection is "sized for worst-case scenarios" (24 August 2026).

A rough bound shows the stake; the inference is mine. Suppose a dry liquid hall runs at a PUE of about 1.1 most of the year. On its worst hour, a chiller carrying the full load adds roughly 0.25, lifting the instant ratio to about 1.35. On a fixed plug, the hall then fits about 15% fewer racks than one whose worst hour stays near 1.15, my assumption for a wet hall. That likely overstates the penalty, since a chiller making 41 degree water works across a smaller lift. No operator publishes the worst-hour PUE of a dry-cooled liquid hall.

Water has a peak too. Researchers at the University of California, Riverside, estimated that evaporative cooling's water demand on the peak day can run six to ten times its average (12 March 2026). Utilities must size plants, pumps and pipes for that day. So the grid and the water main are both built for the same hot afternoon. A tower spends its most water just as the town's mains peak; a dry roof draws its most power just as the grid is tightest. Under a fixed plug, a little water for the hottest 88 hours may buy back peak megawatts; that is a working hypothesis.

<a id="towns-say-no"></a>

## Why are towns saying no to water, even for halls that use almost none?

Because a town cannot see a closed loop, and it can see a water main, a power line and a large building.

Tucson, Arizona, is the clearest case. Its council ended talks on the Project Blue campus in August 2025, after opposition on water and power, local press reported. The project moved to county land, and a renewed agreement in December 2025 required a closed-loop air-cooled design. Arizona's utility regulator approved its power supply on 3 December 2025, reports say. It was redesigned, not cancelled.

Others redesigned too. Google said it would restart its Cerrillos campus in Santiago, Chile, with air-cooled chillers after a court partly annulled its permit, press reported. Meta's planned campus at Talavera de la Reina, Spain, was redesigned from water to dry air cooling, reports say. Some places refuse outright: Pinal County, Arizona, refused rezoning for a campus near Eloy on 26 August 2026, despite a closed-loop pledge, local press reported. In Malaysia, Johor will not consider areas with a low water reserve margin, as told in [the Johor piece](/journal/the-queue-not-the-chip/#johor-waits-on-the-treatment-plant).

I concede that water is now a permit-stage risk, and that a closed-loop promise no longer buys consent. But the claim's test is a campus with power already secured, cancelled outright over water. I have found none. So far water kills weak projects and moves strong ones.

## So who holds the scarce thing, and what should an investor watch?

The scarce thing is not water in general. It is the right to evaporate it in a given basin, and the power to go without it on the hottest afternoon.

If the claim is right, three parts of the chain gain. **The loop at the chip**: cold plates, CDUs and pipework go into every AI rack, whatever the roof. **The dry roof**: dry coolers, adiabatic coolers and air-cooled chillers gain on towers in new halls. **The dry site with power**: a site with a grid allocation and scarce water is more usable than it looks, because a liquid hall can go dry cheaply. Almost every large maker now sells both the loop and the roof. Trane, another chiller maker, completed its purchase of LiquidStack, a CDU maker, on 3 March 2026, and Vertiv completed its purchase of ThermoKey, an Italian dry cooler maker, on 12 June 2026.

The readings come yearly and quarterly. Google's per-site water table each summer is the main one: Mesa, and whether Waltham Cross and Canelones get rows. Microsoft's first zero-water sites come online in late 2027, and whether it publishes their PUE matters. The chiller makers' orders each quarter show whether the worst afternoon is still being bought.

## What would prove me wrong

Three things would break the claim, and each tests what operators and towns do, not physics.

The first is Google's own sites. If Mesa, Waltham Cross or Canelones consumes 50 million gallons or more in 2026 or 2027, the dry roof was not chosen where Google said it would be. Mesa consumed 9.7 million in 2025, about a fiftieth of The Dalles. But two of the three sites cannot be tested until Google lists them.

The second is a wet campus on scarce water: Google, Microsoft, Amazon or Meta reporting a new campus that evaporates water from a source it rates high risk. This limb is hard to break: only Google rates sources by name, and its 2026 policy allows "recycled water" at high-risk sites.

The third is a powered AI campus cancelled outright over water rather than redesigned. Project Blue is the live case, and so far it fits my claim. A water utility refusing service to a campus whose grid power is already secured would move me first.

Henderson, Nevada, is the hardest fact I must face. Google's campus there, in a desert basin, consumed 158.8 million gallons in 2023, 207.4 in 2024 and 239.4 in 2025. Google publishes no rating of its source. Henderson is an existing campus, so it does not break the test of a new one. But if Google rated it high risk and kept evaporating, the claim's spirit would be weaker than its letter.

Rising water totals would not move me. More evaporation where water is plentiful is the trade working as designed. At the scale of the chip, heat has decided: liquid, warm. At the scale of the roof, the operator trades water for power, and the chip maker's temperature sets the price. At the scale of the town and the grid, both bills are sized for the same hot afternoon, and that is where the next argument about water will be settled.
