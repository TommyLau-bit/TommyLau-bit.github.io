Between June and August 2026, five new American test reactors reached criticality, the moment a nuclear chain reaction first sustains itself. On 24 August a critical experiment for the core of eVinci, a microreactor from Westinghouse, one of America's oldest reactor makers, followed in Nevada. Most were the first of their design, several were small enough to travel by road, and none needed a decade of concrete to build.

None of them has sold a single kilowatt-hour of electricity. Each was a physics test run at zero or very low power. The reactors exist. The fuel to run them at full power for years, in the quantities a real industry would need, does not yet exist anywhere in America.

That is the claim of this piece. A microreactor is a product you can build in a factory, but it needs a fuel that almost nobody makes: uranium enriched to just under 20 per cent and sealed inside ceramic grains the size of a poppy seed. Because that fuel is scarce, the government decides who gets it, and the first customer is the military, not the AI data centre.

{{ANALOGY}}

## What is a microreactor, and how small is small?

A microreactor is a complete nuclear power plant small enough to be built in a factory and moved by lorry, ship or rail. Idaho National Laboratory puts typical output at 1 to 20 megawatts of electricity.

Reactors quote two kinds of megawatt. **MWt**, megawatts thermal, is the heat the core makes. **MWe**, megawatts electric, is the electricity that comes out after that heat has driven a turbine, roughly a third of MWt. BANR, the microreactor of BWXT, the Virginia company that builds the US Navy's reactors, makes 75 MWt and 20 MWe. Westinghouse's eVinci makes 15 MWt and 5 MWe.

"Small nuclear" hides three products. A **large reactor**, such as each of the two new units at Vogtle in Georgia, makes about 1,100 MWe. A **small modular reactor**, or SMR, is up to about 300 MWe a unit, built on site from factory-made modules. A **microreactor** is the smallest class, a fiftieth to a thousandth of a large reactor, and the only one designed to travel.

{{FIG1}}

What does 20 MWe buy? One Nvidia GB200 NVL72 rack, the standard AI cabinet today, is rated by Nvidia at about 120 kilowatts. Twenty megawatts runs about 165 of them before any power is spent on cooling. A 1-gigawatt AI campus, the size large AI sites now plan, would need fifty of the very largest microreactors side by side. Hold on to that sum: it decides who buys these machines first.

## What has to change when a reactor fits on a lorry?

A small core leaks neutrons and must run for years unopened, so it needs more uranium-235, the atom that splits, in its fuel.

A reactor is a kettle heated by splitting atoms. When a slow neutron is absorbed by a nucleus of uranium-235, written U-235, the nucleus splits in two; this is **fission**. The halves fly apart and their crashing is heat. Each split also throws out two or three new neutrons. If exactly one of them goes on to split another atom, the reaction holds steady and the reactor is called **critical**.

Neutrons are made all through the core but escape through its surface. A small core has far more surface for its volume, so a much larger share simply leak out. Every escaped neutron is one that will never split an atom. Designers fight the leak with a **reflector**, a thick layer of graphite or beryllium that bounces neutrons back in. They steer the reaction with **control drums** set in that reflector, cylinders with an absorbing face turned inward to stop the reactor. Many designs also drop the pumps: eVinci carries its heat out through **heat pipes**, sealed tubes with no moving parts. And, most importantly, they put more U-235 into the fuel.

{{FIG2}}

The second constraint is time. A large water-cooled reactor stops every 18 to 24 months to swap about a third of its fuel. A microreactor is meant to run for years unopened, then be driven away and refuelled in a factory. Pele, the Pentagon's prototype microreactor, built by BWXT, is designed to run up to three years between refuellings; BWXT's BANR, four; eVinci, eight or more full-power years. So the fuel must be richer twice over: once to beat the leak, and again to last for years.

## Why can't a small core run on ordinary reactor fuel?

It can, but only by being bigger, refuelling sooner and producing far more expensive power, which defeats the point of a microreactor.

Uranium as mined is only about 0.7 per cent U-235. Raising that share is called **enrichment**, done by spinning uranium gas, uranium hexafluoride (UF6), through chains of centrifuges called cascades. Today's water-cooled reactors burn **low-enriched uranium (LEU)**, at about 3 to 5 per cent. **High-assay low-enriched uranium (HALEU)** is enriched to more than 5 and less than 20 per cent; most designs use 19.75 per cent. Uranium at 20 per cent or more is **highly enriched uranium**, which safeguards treat as usable in a weapon, so 19.75 leaves a manufacturing margin under that line. HALEU is still far too dilute for a weapon, but above 10 per cent the Nuclear Regulatory Commission (NRC), America's nuclear regulator, puts sizeable quantities into a stricter security category.

Richer fuel costs far more enrichment work, measured in **separative work units (SWU)**. A kilogram at 4.95 per cent needs about 8 SWU; a kilogram at 19.75 per cent needs about 41 SWU (my arithmetic). Each kilogram of HALEU is about five times the work of ordinary fuel.

Yet that work pays for itself many times over in a small core. Idaho National Laboratory's 2024 cost study of a reference microreactor found that raising enrichment from 5 to 19.75 per cent cut the cost of each unit of electricity by a factor of about fifteen. A low-enriched microreactor is possible: Aalo, a start-up, designs its 10 MWe Aalo-X to run on uranium enriched to 5 per cent or less, and is refuelled every one to three years. At least four of the five designs the Army chose in August 2026 run on HALEU.

## Why does the fuel come as tiny ceramic grains?

Because a microreactor runs too hot, too long and too unattended for metal-clad pellets. The answer engineers found is to give every speck of uranium its own containment.

An ordinary reactor's fuel is uranium oxide pellets inside a thin tube of zirconium alloy, designed to sit near 300°C water. Most microreactors are cooled by helium gas or heat pipes, run much hotter, and are meant to cool themselves passively if everything stops. Zirconium tubes are the wrong tool for that job.

The answer is **TRISO**, short for tristructural isotropic. Each particle starts as a **kernel** of uranium about 0.4 millimetres across. Four coatings follow: a porous carbon buffer that catches fission fragments and gases, a dense carbon skin, a hard **silicon carbide** shell that holds the metallic fission products in, and an outer carbon layer. The finished particle is just under a millimetre across, the size of a poppy seed. Thousands are pressed with graphite into a **compact**, a small cylinder about 12 millimetres wide.

{{FIG3}}

Does it work? In the government's first Advanced Gas Reactor campaign, AGR-1, about 298,000 particles were run in a reactor to around three times the burnup of ordinary fuel (burnup measures how much of the uranium is used). Not one particle failed outright. In heating tests afterwards, not one failed up to 1,700°C, against a normal running temperature of about 950 to 1,140°C. In 2020 the NRC accepted those results as evidence of how the particle performs. "Meltdown-proof" is the wrong phrase, but the record is strong. That is what lets a microreactor rely on passive cooling and sit near a base or a factory without the large exclusion zones of a conventional plant.

One honest caveat. The final qualification campaign, AGR-5/6/7, which tested the 15.5 per cent fuel planned by X-energy, the reactor developer backed by Amazon, stopped early in 2020 short of its targets, and one capsule had between 180 and 440 particle failures. Idaho National Laboratory suspects the test rig rather than the fuel, but has not established the cause, and I found no final statement that the fuel is qualified.

## How do HALEU and TRISO work together?

TRISO needs HALEU because a TRISO core holds very little uranium, so each atom of it must carry more U-235.

Most of a particle is carbon and ceramic. A test compact holds about 0.3 to 0.46 grams of uranium per cubic centimetre; a solid uranium oxide pellet holds about 9 grams (both my arithmetic, from national laboratory figures). A core that dilute cannot sustain a chain reaction for years at 5 per cent enrichment. TRISO buys safety at high temperature and pays for it in uranium density; HALEU buys the density back. Take away either, and the small, hot, years-long core stops working.

It also stacks the costs. Idaho National Laboratory's central estimate for making TRISO fuel, in 2020 dollars, is about $4,000 per kilogram of uranium, against about $420 for ordinary water-reactor fuel. The same report notes that no plant making tens or hundreds of tonnes of TRISO a year exists anywhere in the world.

## Why does almost nobody make this fuel?

Because the only commercial seller of HALEU was Russia, America's own production has been a single demonstration line, and nobody builds a fuel plant before there are reactors to buy its output.

Until recently, the Department of Energy (DOE) put it plainly: "There is no commercial source of HALEU outside of Russia currently available to fuel these reactors." In May 2024 Congress banned imports of Russian enriched uranium, with waivers allowed only until 1 January 2028. Six months later Russia restricted its own exports to America.

At home there is one line. Centrus Energy, the only American company that has enriched HALEU, runs a cascade of sixteen centrifuges at Piketon, Ohio, built under a government contract. It had delivered more than 1,900 kilograms of HALEU gas by mid-June 2026, Centrus said, about 1.3 tonnes of uranium. For scale, a single X-energy Xe-100, a mid-size advanced reactor, is expected to use about 0.45 tonnes of uranium in TRISO fuel every year. From 30 June 2026 the DOE contract covered only maintenance and storage, and the department said it did not intend to buy more. On 4 November Centrus said the cascade now enriches HALEU for commercial customers. It gave no volume.

Why will nobody simply build a big HALEU plant? An enrichment plant takes the best part of a decade and billions of dollars to build and license. Its owner will not commit without signed buyers. The buyers, reactor companies, cannot sign for large volumes before their designs are licensed and their own customers have committed. Each side waits for the other.

The government's attempt to break the loop is real but small. In January 2026 the DOE awarded $2.7 billion of enrichment task orders; Centrus and a start-up, General Matter, each received $900 million for HALEU. But Centrus's order mainly pays to build capacity: the HALEU it must deliver is one tonne of uranium, delivered as gas, by July 2032. Orano, the French nuclear fuel group, has applied to enrich up to 8 per cent in Tennessee, and Urenco, the European enrichment group, is licensed to 10 per cent in New Mexico: both far below 19.75. General Matter aims to enrich by the end of the decade.

Enrichment is not even the last gap. The Government Accountability Office (GAO), Congress's auditor, in August 2026, called deconversion, turning the gas back into a solid, "a capability that does not yet exist for HALEU". And the NRC says only one shipping package is approved for commercial quantities of HALEU, and that its "manufacturing … has not yet occurred".

{{FIG4}}

The TRISO step has its own small number of hands. BWXT, which makes the Navy's reactor fuel, has made TRISO for the government's tests since the 2000s and made the whole first core for Pele, delivered to Idaho in December 2025. Its chief executive said in November 2026 that the line produces "a couple of hundred kilograms a year" and could "at least quadruple". Standard Nuclear, built from the fuel assets of a bankrupt start-up, runs a line in Oak Ridge rated at 0.5 tonnes a year, under DOE authority rather than an NRC licence. In June 2026 it made its first commercial delivery of HALEU TRISO, about 50 kilograms of uranium, to Radiant, a start-up whose 1 MWe microreactor is called Kaleidos. X-energy's TRISO-X received an NRC licence in February 2026, for a plant that starts in 2028.

## How much fuel is there, against how much is needed?

Not enough, by the government's own numbers, and the gap is widest exactly where the microreactors sit.

Because commercial supply has only just begun, the government is releasing its own HALEU, recovered from the spent fuel of an old Idaho test reactor and blended down from surplus highly enriched uranium. The DOE told GAO it expects to provide about 21.2 tonnes by 2028. The demand, in the DOE's own words, is "more than 40 metric tons" by 2030, rising to about 50 tonnes a year by 2035. The whole government stock plus the one contracted new tonne covers about half of the first figure.

{{FIG5}}

TRISO is tighter still, a separate bottleneck downstream of the first. On nameplate figures, BWXT's line and Standard Nuclear's together make about 0.7 tonnes of uranium a year today (my arithmetic). Standard Nuclear's two new plants, substantially complete in July 2026 and awaiting DOE approval, would lift the total to about 2.7 tonnes. With TRISO-X running and BWXT's line quadrupled, 2028 could see 8 to 11 tonnes.

Orders are arriving faster than that. In August and October 2026 alone, Antares, a microreactor start-up, signed for two tonnes from two suppliers, and Radiant for "multi-metric tons" through 2031 from Standard Nuclear. No microreactor company has published how much uranium one of its cores holds. BWXT's statement that a year of its line's output fuels Pele implies a core of roughly 100 to 200 kilograms, and Radiant's first 50 kilograms was only part of one core.

## Who gets the fuel first, and why them?

The government decides, in published rounds, and it favours the projects closest to running, those it funds itself, and those that can prove they can handle the fuel.

The DOE has run three rounds of its HALEU Availability Program. All allocations are conditional, and the DOE has published no quantities.

| Round | Date | Recipients | What the fuel is for |
|---|---|---|---|
| 1 | 9 April 2025 | TRISO-X, Kairos Power, Radiant, Westinghouse, TerraPower | TRISO fuel making, test reactors, the two flagship DOE demonstrations, two microreactor tests in Idaho |
| 2 | 26 August 2025 | Antares, Standard Nuclear, Abilene Christian University with Natura Resources | A microreactor for the DOE's pilot programme, TRISO fuel lines, a molten-salt research reactor |
| 3 | 23 July 2026 | NASA, Radiant | NASA's planned SR-1 Freedom mission to Mars; a Radiant microreactor at Buckley Space Force Base, Colorado |

By law the first claim goes to the DOE's two flagship demonstrations, X-energy's and TerraPower's. After that the DOE favours projects the government funds, those with a licensing schedule, and those with "objective evidence" that they can fabricate, ship and store the fuel. Fifteen companies asked in the first round; five were chosen. Two of the ten selections are fuel makers, TRISO-X and Standard Nuclear, because a kilogram of HALEU is useless to a microreactor until someone has coated it. Several of the rest are tests on government land, and Radiant appears twice, the second time for a military base. Fuel first means running first, and running first means selling first. The order of the HALEU queue is, in effect, the order of the American microreactor industry.

## Why is the first customer the military, not a data centre?

Because the military can regulate its own reactors, values power that cannot be cut off, and is the one buyer for whom a first-of-a-kind price is acceptable.

A company that wants to sell electricity to a private customer needs an NRC licence, and no microreactor holds an NRC operating licence. But the DOE can authorise test reactors under its own authority; that is how the 2026 criticalities happened. And an Executive Order of May 2025 told the Army to have a reactor "regulated by the United States Army" operating at a domestic base by 30 September 2028. The government has built a lane for itself that private buyers cannot yet use. The Army's statements talk not about cheap power but about bases' "vulnerability to grid instability, natural disasters, or adversarial attacks".

The buyers have moved. On 26 August 2026 the Army chose five companies for its Janus programme, worth up to $2.2 billion from fiscal 2027 to 2031: Antares at Fort Bragg, BWXT at Fort Campbell, General Atomics at Fort Hood, Radiant at Fort Benning and Westinghouse at Fort Drum, with more than twenty reactors expected and the first targeted for September 2028. The companies will own, build and operate the reactors, and are paid as they hit technical milestones.

Finally, the price. Idaho National Laboratory's 2024 study estimated that a first-of-a-kind microreactor would produce electricity at about 32.5 cents a kilowatt-hour; once mass-produced, about 12 to 15 cents. American industrial customers paid an average of 8.6 cents in 2025. But an earlier INL report, drawing on the Nuclear Energy Institute (NEI), the industry's trade body, puts electricity at remote sites run on diesel generators at 15 to 60 cents. The comparison with diesel is the laboratory's, not the Army's, but it shows why a first unit makes sense on an isolated base and not on a grid-connected campus.

{{FIG6}}

## So where do microreactors fit in AI?

At the edges, and later: the AI industry's own nuclear bets are on larger reactors, while microreactors serve sites the grid cannot reach.

A 1-gigawatt campus would need fifty of the largest microreactors, each with its own fuel, security and licence, at prices above the grid's. So AI's biggest builders have signed for bigger machines. Google agreed in October 2024 to buy power from 500 MW of Kairos Power's reactors. Amazon backed X-energy's plan for more than 5 GW of Xe-100s by 2039. Meta agreed in January 2026 to deals worth up to 6.6 GW, including Oklo's 1.2 GW campus in Ohio. None of those is a microreactor.

The microreactor deals with data centre companies are preorders and pilots, not power contracts. Equinix, a large data centre operator, signed in August 2025 a "preorder agreement" for twenty of Radiant's Kaleidos units, with no dates or terms. Crusoe, which builds AI data centres, plans a 2027 demonstration in Idaho with an Aalo reactor powering one of its modular data centres, then larger Aalo units at its sites by the end of 2029. Aalo's reactor runs on ordinary LEU, which takes it out of the HALEU queue: that is the case to watch against this piece.

There is one place where AI and microreactors already meet. The May 2025 Executive Order asks for power at military bases that "cannot be disrupted by external threats or grid failures", including for AI computing at those installations. The first AI racks a microreactor powers are more likely to sit behind a base's fence than in a hyperscaler's hall. For everything else, microreactors become a data centre product only when the fuel queue stops setting the order.

## What would prove me wrong

Two tests break the claim. If, on or before 31 December 2030, a US data centre receives electricity from a microreactor under a commercial supply contract, the data centre was not behind the military after all. If the first microreactor to deliver sustained electricity to a customer in America is at a site that is neither military nor on government land, the government's queue did not set the order.

Some events would move me before either test. The DOE approving Standard Nuclear's two new TRISO plants, lifting US capacity to about 2.7 tonnes a year, would ease the second bottleneck early. Crusoe's Aalo demonstration running on ordinary LEU in 2027 would show a data centre can skip the HALEU queue entirely. And an NRC final rule for microreactors, proposed in May 2026 with a target of licences in six to twelve months, would open the private lane.

Three things would not move me. More preorders: a preorder is not a power contract. More criticalities: a zero-power physics test proves the reactor, not the fuel supply. And headline enrichment awards: Centrus's $900 million mainly builds capacity, and the HALEU it must deliver by 2032 is one tonne of uranium, perhaps enough for five to ten microreactor cores once made into fuel. That is not an industry.
