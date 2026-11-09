Between June and August 2026, five new American test reactors reached criticality, the moment a nuclear chain reaction first sustains itself. On 24 August a critical experiment for the core of eVinci, a microreactor from Westinghouse, one of America's oldest reactor makers, followed in Nevada. Most were the first of their design, several were small enough to travel by road, and none needed a decade of concrete to build.

None of them has sold a single kilowatt-hour of electricity. Each was a physics test run at zero or very low power. The reactors exist. The fuel to run them at full power for years, in the quantities a real industry would need, does not yet exist anywhere in America.

That is the claim of this piece. A microreactor is a product you can build in a factory, but it needs a fuel that almost nobody makes: uranium enriched to just under 20 per cent and sealed inside ceramic grains the size of a poppy seed. Because that fuel is scarce, the government decides who gets it, and the first customer is the military, not the AI data centre.

To see why, the piece follows the questions in order. What a microreactor is and how small "small" means. How a reactor makes heat at all, and what has to change when one fits on a lorry. Why that forces a richer fuel, why the fuel comes as ceramic grains, and why almost nobody makes either. Then who gets the fuel first, why the Army buys before Google, and where all this leaves AI.

{{ANALOGY}}

## What is a microreactor, and how small is small?

A microreactor is a complete nuclear power plant small enough to be built in a factory and moved by lorry, ship or rail. Idaho National Laboratory, the government's lead nuclear research lab, describes them as factory-produced, transportable and "self-regulating", with power outputs typically 1 to 20 megawatts of electricity.

Those units need explaining first, because press releases mix them up. A watt measures how fast energy is used: a kettle draws about 2,000 watts while it boils. A megawatt is a million watts, about five hundred kettles boiling at once. A kilowatt-hour, the unit on an electricity bill, is a thousand watts drawn for one hour. Reactors quote two kinds of megawatt, and the gap between them is large.

**MWt**, megawatts thermal, is the heat the core makes. **MWe**, megawatts electric, is the electricity that comes out after that heat has driven a turbine. Turning heat into electricity loses most of it, so MWe is roughly a third of MWt. BANR, the microreactor of BWXT, the Virginia company that builds the US Navy's reactors, makes 75 MWt of heat and 20 MWe of electricity; Westinghouse's eVinci makes 15 MWt and 5 MWe. When this piece says a reactor is "1 MWe", it means one megawatt a customer could actually use.

"Small nuclear" also hides three different products. A **large reactor**, such as each of the two new units at Vogtle in Georgia, makes about 1,100 MWe. A **small modular reactor**, or SMR, is up to about 300 MWe a unit (the International Atomic Energy Agency's line), built on site from factory-made modules and sold to the grid. A **microreactor** is the smallest class, a fiftieth to a thousandth of a large reactor, and the only one designed to travel.

{{FIG1}}  <!-- One large AI campus needs about fifty of the biggest microreactors -->

What does 20 MWe actually buy? The average American home used 865 kilowatt-hours a month in 2024, according to the Energy Information Administration (EIA), the government's energy statistics office. That is an average draw of about 1.2 kilowatts, so 20 MWe running all year would supply about 17,000 homes.

In the units that matter to this site, one Nvidia GB200 NVL72 rack, the standard AI cabinet today, is rated by Nvidia at about 120 kilowatts. Twenty megawatts runs about 165 of them before any power is spent on cooling. A 1-gigawatt AI campus, the size large AI sites now plan, would need fifty of the very largest microreactors side by side. Hold on to that sum: it decides who buys these machines first.

## How does a reactor make heat at all?

A reactor is a kettle heated by splitting atoms; everything else in it exists to control that splitting and carry the heat away.

The atom that matters is uranium-235, written U-235. An atom has a dense centre, the nucleus, made of protons and neutrons. When a slow-moving neutron is absorbed by a U-235 nucleus, the nucleus becomes unstable and splits in two. This is **fission**. The two halves fly apart at enormous speed and crash into the material around them, and that crashing is heat. Each split also throws out two or three new neutrons.

Those new neutrons are the engine. If, on average, exactly one of them goes on to split another U-235 nucleus, the reaction sustains itself at a steady rate, and the reactor is called **critical**. That word sounds alarming but simply means "steady". If more than one neutron per split goes on to cause another, the power rises; if fewer, it falls. Running a reactor is the job of holding that number at exactly one.

The energy packed into the fuel is extraordinary. Splitting every U-235 atom in one kilogram releases about as much heat as burning roughly 3,000 tonnes of coal (my arithmetic, from the standard energy per fission). That density is why a reactor can run for years on fuel that fits in a small room, and why a reactor small enough to drive around is possible at all.

Three parts hold the chain at one. A **moderator**, usually water or graphite, slows the new neutrons down, because U-235 captures slow neutrons far more readily than fast ones. **Control material**, such as boron, soaks up spare neutrons and is moved in or out to steer the power. A **coolant**, which can be water, a gas such as helium, or a liquid metal such as sodium, carries the heat out to drive a turbine. A few designs skip the moderator and run on fast neutrons; Aurora, a 75 MWe design from the start-up Oklo, is one, and it is not a microreactor.

## What has to change when a reactor fits on a lorry?

Shrinking a reactor is not just a matter of making every part smaller, because a small core loses its neutrons.

Neutrons are made all through the core, but they escape through its surface. A large core has a great deal of volume for its surface, so most neutrons hit another atom long before they reach the edge. A small core has far more surface for its volume, so a much larger share simply leak out. Every escaped neutron is one that will never split an atom. A microreactor therefore starts with a handicap: it must hold the chain at exactly one while losing neutrons a large reactor would have used.

Designers fight the leak in three ways. They wrap the core in a **reflector**, a thick layer of graphite or beryllium that bounces escaping neutrons back in. They steer the reaction with **control drums** set in that reflector: cylinders with an absorbing face on one side, turned outward while the reactor runs and inward to soak up neutrons and stop it. Drums take little room and work lying flat on a trailer, unlike the long rods a large reactor lowers from above. Many designs also drop the pumps: eVinci carries its heat out through **heat pipes**, sealed metal tubes in which a liquid metal boils at the hot end and condenses at the cool end, moving heat with no moving parts; others blow helium gas through the core. And, most importantly, they put more U-235 into the fuel.

{{FIG2}}  <!-- Inside a microreactor: a reflector and turning drums stand in for size -->

The second constraint is time. A large water-cooled reactor stops every 18 to 24 months to swap about a third of its fuel. A microreactor is meant to run for years without anyone opening it, then be driven away and refuelled in a factory. Pele, the Pentagon's prototype microreactor, built by BWXT, is designed to run up to three years between refuellings; BWXT's BANR, four; eVinci, eight or more full-power years.

That means the core must start with a large surplus of U-235, enough to keep the chain at one as the atoms are used up and as the fragments of split atoms, which soak up neutrons themselves, build up inside the fuel. So the fuel must be richer twice over: once to beat the leak, and again to last for years. That double demand leads straight to the fuel this piece is about.

## Why can't a small core run on ordinary reactor fuel?

It can, but only by being bigger, refuelling sooner and producing far more expensive power, which defeats the point of a microreactor.

Start with what "ordinary fuel" is. Uranium as it comes out of the ground is only about 0.7 per cent U-235; almost all the rest is uranium-238, which barely splits in a reactor like these. Raising the U-235 share is called **enrichment**. It cannot be done with chemistry, because the two kinds of uranium behave identically in any chemical reaction. It is done physically: the uranium is turned into a gas, uranium hexafluoride (UF6), and spun in tall centrifuges at enormous speed. The slightly heavier U-238 drifts outward, the lighter U-235 stays nearer the middle, and thousands of passes through chains of centrifuges, called cascades, slowly concentrate it.

Today's water-cooled reactors burn **low-enriched uranium (LEU)**, enriched to about 3 to 5 per cent. A microreactor that wants to be small and run for years needs much more. **High-assay low-enriched uranium (HALEU)** is uranium enriched to more than 5 and less than 20 per cent; most designs use 19.75 per cent.

Why stop just short of 20? Because 20 per cent is the legal line. Uranium at 20 per cent or more is **highly enriched uranium**, which international safeguards treat as material that could be used directly in a weapon. Staying at 19.75 leaves a manufacturing margin under that line. HALEU is still far too dilute for a weapon, but it is not ordinary fuel either: above 10 per cent, the Nuclear Regulatory Commission (NRC), America's nuclear regulator, puts sizeable quantities into a stricter security category.

Richer fuel also costs far more enrichment work. Enrichment is measured in **separative work units (SWU)**, a measure of how much centrifuge effort goes into each kilogram. By the standard formula, a kilogram of uranium at 4.95 per cent needs about 8 SWU and 10 kilograms of natural uranium; a kilogram at 19.75 per cent needs about 41 SWU and 42 kilograms (my arithmetic). Each kilogram of HALEU is about five times the work of ordinary fuel, at any reasonable assumption about the waste stream.

Yet that work pays for itself many times over in a small core. Idaho National Laboratory's 2024 cost study of a reference microreactor found that raising enrichment from 5 to 19.75 per cent cut the cost of each unit of electricity by a factor of about fifteen. A low-enriched microreactor is possible. Aalo, a start-up, designs its 10 MWe Aalo-X to run on uranium enriched to 5 per cent or less, and a zero-power test core went critical in Idaho in July 2026. It pays in size and refuelling: Aalo's design is refuelled every one to three years. At least four of the five designs the Army chose in August 2026 run on HALEU.

## Why does the fuel come as tiny ceramic grains?

Because a microreactor runs too hot, too long and too unattended for the metal-clad pellets of an ordinary reactor, and the answer engineers found is to give every speck of uranium its own containment.

An ordinary reactor's fuel is a stack of uranium oxide pellets inside a thin tube of zirconium alloy, the cladding. The cladding is the barrier that keeps radioactive fragments in. It is designed to sit near the 300°C water around it, and US rules cap its peak temperature at 1,204°C even in an accident (10 CFR 50.46). Most microreactors are cooled by helium gas or heat pipes, not water, and they run much hotter, which gives more electricity from each unit of heat. They are also meant to cool themselves passively if everything stops. Zirconium tubes are the wrong tool for that job.

The answer is **TRISO**, short for tristructural isotropic. The name describes a particle whose coatings include three structural layers, two of carbon and one of ceramic, and which behaves the same in every direction. Each TRISO particle starts as a **kernel**, a tiny sphere of uranium about 0.4 millimetres across. It is then coated in four layers, each with its own job.

The first layer is a **porous carbon buffer**, about 0.1 millimetres thick and about half empty space. When an atom splits, its fragments fly outward and some are gases; the buffer catches the fragments and gives the gases room. The second, **inner pyrolytic carbon**, is a dense carbon skin, laid down by breaking up a hydrocarbon gas at high temperature, that seals the kernel. The third, **silicon carbide**, is the particle's pressure shell, a hard ceramic that holds the metallic fission products in. The fourth, **outer pyrolytic carbon**, protects the silicon carbide and bonds the particle into the graphite around it. The finished particle is just under a millimetre across, the size of a poppy seed.

{{FIG3}}  <!-- Every speck of uranium carries its own containment -->

Thousands of these particles are then pressed with graphite into a **compact**, a small cylinder about 12 millimetres wide and 25 millimetres long, or into a pebble the size of a billiard ball. Compacts are stacked in holes drilled through hexagonal graphite blocks; the graphite doubles as the moderator. A typical test compact holds 2,000 to 4,000 particles.

Does it work? The government's Advanced Gas Reactor programme has tested TRISO in Idaho since the 2000s. In the first campaign, AGR-1, about 298,000 particles were run in a reactor to around three times the burnup of ordinary fuel (burnup measures how much of the uranium is used). Not one particle failed outright. In heating tests afterwards, not one failed up to 1,700°C, against a normal running temperature of about 950 to 1,140°C. At 1,800°C, two of 16,500 failed after more than 200 hours. In 2020 the NRC accepted those results as evidence of how the particle performs.

So "meltdown-proof" is the wrong phrase, but the real record is strong: the particle holds its contents at temperatures far above anything a well-designed small gas-cooled core can reach after an accident. That is what lets a microreactor rely on passive cooling and sit near a base or a factory without the large exclusion zones of a conventional plant.

One honest caveat. The final qualification campaign, AGR-5/6/7, which tested the 15.5 per cent fuel planned by X-energy, the Maryland reactor developer backed by Amazon, stopped early in 2020 short of its burnup and temperature targets, and one of its capsules had between 180 and 440 particle failures. Idaho National Laboratory suspects problems with the test rig rather than the fuel, but has not established the cause, and I found no final statement that the fuel is qualified.

## How do HALEU and TRISO work together?

TRISO needs HALEU because a TRISO core holds very little uranium, so each atom of it must carry more U-235.

Look at the particle again. Most of it is carbon and ceramic, and the particles fill only about a quarter to two fifths of each compact. A test compact holds about 0.3 to 0.46 grams of uranium per cubic centimetre. A solid uranium oxide pellet holds about 9 grams (both my arithmetic, from national laboratory figures). An ordinary pellet packs roughly twenty to thirty times as much uranium into the same space.

A core with that little uranium cannot sustain a chain reaction for years at 5 per cent enrichment. Raising the U-235 share to between 10 and 19.75 per cent puts enough fissile atoms back into the core to beat the leak and last the years. Early American gas-cooled reactors used weapons-grade uranium above 90 per cent; today's non-military designs use 8 to 19.9 per cent.

The pairing is therefore not a choice of two good things. TRISO buys safety at high temperature and pays for it in uranium density; HALEU buys the density back. Take away either, and the small, hot, years-long core stops working.

It also stacks the costs. Idaho National Laboratory's central estimate for making TRISO fuel, in 2020 dollars, is about $4,000 per kilogram of uranium, against about $420 for ordinary water-reactor fuel: roughly nine and a half times more, before the extra enrichment is counted. The same report notes that no plant making tens or hundreds of tonnes of TRISO a year exists anywhere in the world.

## Why does almost nobody make this fuel?

Because the only commercial seller of HALEU was Russia, America's own production has been a single demonstration line, and nobody builds a fuel plant before there are reactors to buy its output.

Until recently, the Department of Energy (DOE) put it plainly: "There is no commercial source of HALEU outside of Russia currently available to fuel these reactors." Russia's state nuclear business also supplied about a quarter of the enrichment work bought by American reactor owners for their ordinary fuel: 26 per cent in 2025, by the EIA's figures. In May 2024 Congress banned imports of Russian enriched uranium, with waivers allowed only until 1 January 2028. Six months later Russia restricted its own exports to America. Both doors are closing.

At home there is one line. Centrus Energy, the only American company that has enriched HALEU, runs a cascade of sixteen centrifuges at Piketon, Ohio, built under a government contract. It delivered its first HALEU in November 2023, 900 kilograms of HALEU gas in its second phase to June 2025, and more than 1,900 kilograms of HALEU gas in all by mid-June 2026, Centrus said. That is about 1.3 tonnes of uranium. For scale, a single X-energy Xe-100, a mid-size advanced reactor, is expected to use about 0.45 tonnes of uranium in TRISO fuel every year.

Then the government stopped paying for production. From 30 June 2026 the DOE contract covered only maintenance and storage, and the department said it did not intend to buy more. On 20 October 2026 it handed Centrus's subsidiary title to the HALEU the line had made, to hold for resale to the government on request. On 4 November Centrus said the cascade now enriches HALEU for commercial customers. It gave no volume.

Why will nobody simply build a big HALEU plant? This is the chicken-and-egg problem at the centre of the piece. An enrichment plant takes the best part of a decade and billions of dollars to build and license. Its owner will not commit without signed buyers for years of output. The buyers, reactor companies, cannot sign for large volumes before their designs are licensed and their own customers have committed. Each side waits for the other.

The government's attempt to break the loop is real but small. In January 2026 the DOE awarded $2.7 billion of enrichment task orders. Centrus and a start-up, General Matter, each received $900 million for HALEU; Orano, the French nuclear fuel group, received $900 million for ordinary LEU. But Centrus's order, signed on 1 July 2026, mainly pays to build capacity: the HALEU it must deliver is one tonne of uranium, delivered as gas, by July 2032, with options for ten tonnes more. Orano has applied to enrich up to 8 per cent at a planned plant in Oak Ridge, Tennessee, and Urenco, the European enrichment group, is licensed to 10 per cent in New Mexico: both far below the 19.75 per cent microreactors use. General Matter aims to enrich by the end of the decade; reports of the DOE's lease of its Kentucky site gave 2034.

Enrichment is not even the last gap. Once enriched, the uranium gas must be turned back into a solid, oxide or metal, before it can be made into fuel. The Government Accountability Office (GAO), Congress's auditor, in August 2026, called that step, deconversion, "a capability that does not yet exist for HALEU". And moving HALEU gas between plants needs certified containers. The standard shipping package is certified only to 5 per cent. The NRC says only one package is approved for commercial quantities of HALEU, Orano's DN30-X, and that its "manufacturing … has not yet occurred".

{{FIG4}}  <!-- From mine to microreactor, three steps in a row have almost nobody on them -->

The TRISO step has its own small number of hands. BWXT, the Virginia company that makes the Navy's reactor fuel, has made TRISO for the government's tests since the 2000s and made the whole first core for Pele, delivered to Idaho in December 2025. Its chief executive said in November 2026 that the line produces "a couple of hundred kilograms a year" and could "at least quadruple". Standard Nuclear, built from the fuel assets of a bankrupt start-up, runs a line in Oak Ridge rated at 0.5 tonnes a year, under DOE authority rather than an NRC licence, and made its first commercial delivery of HALEU TRISO, about 50 kilograms of uranium, in June 2026 to Radiant, a start-up whose 1 MWe microreactor is called Kaleidos. X-energy's TRISO-X received an NRC licence in February 2026, the first new fuel fabrication licence in about fifty years by the DOE's count, for a plant that starts in 2028.

## How much fuel is there, against how much is needed?

Not enough, by the government's own numbers, and the gap is widest exactly where the microreactors sit.

Start with HALEU. Because commercial supply has only just begun, with no volume given, the government is releasing its own: uranium recovered from the spent fuel of EBR-II, an old Idaho test reactor (about 10 tonnes expected by December 2028, half already promised to Oklo), plus surplus highly enriched uranium blended down to under 20 per cent at Savannah River in South Carolina. The DOE told GAO it expects to provide about 21.2 tonnes by 2028. Congress had asked for 21 tonnes by mid-2026.

The demand, in the DOE's own words, is "more than 40 metric tons" by 2030, rising to about 50 tonnes a year by 2035. The whole government stock plus the one contracted new tonne covers about half of the first figure, and under half of a single year of the second.

{{FIG5}}  <!-- Everything America holds or has contracted covers about half the HALEU needed by 2030 -->

TRISO is tighter still, because it is a separate bottleneck downstream of the first. On nameplate figures, BWXT's line and Standard Nuclear's together make about 0.7 tonnes of uranium a year today (my arithmetic). Standard Nuclear's two new plants in Oak Ridge and Idaho were substantially complete in July 2026 and await DOE approval, which would lift the total to about 2.7 tonnes. With TRISO-X running and BWXT's line quadrupled, 2028 could see 8 to 11 tonnes.

Orders are arriving faster than that. In August and October 2026 alone, Antares, a microreactor start-up, signed for two tonnes from two suppliers, and Radiant for "multi-metric tons" through 2031 from Standard Nuclear. No microreactor company has published how much uranium one of its cores holds. BWXT's statement that a year of its line's output fuels Pele implies a core of roughly 100 to 200 kilograms, and Radiant's first 50 kilograms was only part of one core.

## Who gets the fuel first, and why them?

The government decides, in published rounds, and it favours the projects closest to running, those it funds itself, and those that can prove they can handle the fuel.

The DOE has run three rounds of its HALEU Availability Program. All allocations are conditional, and the DOE has published no quantities.

| Round | Date | Recipients | What the fuel is for |
|---|---|---|---|
| 1 | 9 April 2025 | TRISO-X, Kairos Power, Radiant, Westinghouse, TerraPower | TRISO fuel making, test reactors, the two flagship DOE demonstrations, two microreactor tests in Idaho |
| 2 | 26 August 2025 | Antares, Standard Nuclear, Abilene Christian University with Natura Resources | A microreactor for the DOE's pilot programme, TRISO fuel lines, a molten-salt research reactor |
| 3 | 23 July 2026 | NASA, Radiant | NASA's planned SR-1 Freedom mission to Mars; a Radiant microreactor at Buckley Space Force Base, Colorado |

The rules explain the order. By law the first claim goes to the DOE's two flagship demonstrations, X-energy's and TerraPower's, under its Advanced Reactor Demonstration Program. After that the DOE's published criteria favour projects the government funds or shares costs on, those with a licensing schedule, those with "objective evidence" that they can fabricate, ship and store the fuel, and requests for forms and amounts already "readily available in the DOE inventory". The DOE may take an allocation back after "significant delays". Fifteen companies asked in the first round; five were chosen.

Read the list again with that in mind. Two of the ten selections are fuel makers, TRISO-X and Standard Nuclear, because a kilogram of HALEU is useless to a microreactor until someone has coated it. Several of the rest are tests on government land, where the DOE itself is the regulator. And Radiant appears twice, the second time for a military base.

Which matters, because fuel first means running first, and running first means selling first. The order of the HALEU queue is, in effect, the order of the American microreactor industry.

## Why is the first customer the military, not a data centre?

Because the military can regulate its own reactors, values power that cannot be cut off, and is the one buyer for whom a first-of-a-kind price is acceptable.

Start with the regulator. A company that wants to sell electricity to a private customer needs an NRC licence, and no microreactor holds an NRC operating licence. But the DOE can authorise test reactors under its own authority, on its own land and, under its pilot programme, elsewhere; that is how the 2026 criticalities happened. And an Executive Order of May 2025 told the Army to have a reactor "regulated by the United States Army" operating at a domestic base by 30 September 2028. The government has built a lane for itself that private buyers cannot yet use.

Then the reason. The Army's own statements do not talk about cheap power. They talk about bases' "vulnerability to grid instability, natural disasters, or adversarial attacks", and about power for "contested logistics environments". The Air Force says its missions "will never be held at risk by a power outage". A reactor inside the fence that runs for years without a fuel convoy answers that directly.

The buyers have moved. On 26 August 2026 the Army chose five companies for its Janus programme, worth up to $2.2 billion from fiscal 2027 to 2031: Antares at Fort Bragg, BWXT at Fort Campbell, General Atomics at Fort Hood, Radiant at Fort Benning and Westinghouse at Fort Drum, with more than twenty reactors expected and the first targeted for September 2028. The companies will own, build and operate the reactors, and are paid as they hit technical milestones. The Air Force has paired Radiant with Buckley, Westinghouse with Malmstrom and Antares with Joint Base San Antonio, aiming for a reactor on a base by 2030 or sooner.

Finally, the price. Idaho National Laboratory's 2024 study estimated that a first-of-a-kind microreactor would produce electricity at about 32.5 cents a kilowatt-hour; once they are mass-produced, about 12 to 15 cents. American industrial customers paid an average of 8.6 cents in 2025, and commercial customers 13.4 cents. But an earlier INL report, drawing on the Nuclear Energy Institute (NEI), the industry's trade body, puts electricity at remote sites run on diesel generators at 15 to 60 cents. The comparison with diesel is the laboratory's, not the Army's, but it shows why a first unit makes sense on an isolated base and not on a grid-connected campus.

{{FIG6}}  <!-- A first microreactor costs far more than grid power, and about what remote sites pay for diesel -->

## So where do microreactors fit in AI?

At the edges, and later: the AI industry's own nuclear bets are on larger reactors, while microreactors serve sites the grid cannot reach.

The sums from the first section decide it. A 1-gigawatt campus would need fifty of the largest microreactors, each with its own fuel, security and licence, at prices above the grid's. So the companies building AI's biggest campuses have signed for bigger machines. Google agreed in October 2024 to buy power from 500 MW of Kairos Power's reactors, the first by 2030. Amazon backed X-energy's plan for more than 5 GW of Xe-100s by 2039. Meta agreed in January 2026 to deals worth up to 6.6 GW, including Oklo's 1.2 GW campus in Ohio. None of those is a microreactor.

The microreactor deals with data centre companies are preorders and pilots, not power contracts. Equinix, a large data centre operator, signed in August 2025 a "preorder agreement" for twenty of Radiant's Kaleidos units, with no dates or terms. Crusoe, which builds AI data centres, plans a 2027 demonstration in Idaho with an Aalo reactor powering one of its modular data centres, then larger Aalo units at its sites by the end of 2029. Notably, Aalo's reactor runs on ordinary LEU, which takes it out of the HALEU queue: that is the case to watch against this piece.

There is one place where AI and microreactors already meet. The May 2025 Executive Order asks for power at military bases that "cannot be disrupted by external threats or grid failures", including for AI computing at those installations. The first AI racks a microreactor powers are more likely to sit behind a base's fence than in a hyperscaler's hall. For everything else, microreactors become a data centre product only when the fuel queue stops setting the order, and that waits on tonnes of HALEU and TRISO that are years away.

## What would prove me wrong

Two tests break the claim. If, on or before 31 December 2030, a US data centre receives electricity from a microreactor under a commercial supply contract, the data centre was not behind the military after all. If the first microreactor to deliver sustained electricity to a customer in America is at a site that is neither military nor on government land, the government's queue did not set the order.

Some events would move me before either test. The DOE approving Standard Nuclear's two new TRISO plants, lifting US capacity to about 2.7 tonnes a year, would ease the second bottleneck early. Crusoe's Aalo demonstration running on ordinary LEU in 2027 would show a data centre can skip the HALEU queue entirely, at the cost of a larger reactor and more frequent refuelling. And an NRC final rule for microreactors, proposed in May 2026 with a target of licences in six to twelve months, would open the private lane.

Three things would not move me. More preorders: a preorder is not a power contract, and Equinix's has neither dates nor terms. More criticalities: a zero-power physics test proves the reactor, not the fuel supply. And headline enrichment awards: Centrus's $900 million mainly builds capacity, and the HALEU it must deliver by 2032 is one tonne of uranium, perhaps enough for five to ten microreactor cores once made into fuel. That is not an industry.
