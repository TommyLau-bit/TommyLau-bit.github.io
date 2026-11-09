<a id="powering-the-rack"></a>

Nvidia has done something unusual for a chipmaker. It has written down why its own design cannot go on. Wired the way racks are today, it said in May 2025, a rack drawing one megawatt would need up to 200 kilograms of copper bar, and its power supplies would leave no room in the rack for the computers.

So the industry is moving the rack from 54 volts to 800. Yet in its 2026 white paper Nvidia writes that 800 volts "is not intended to replace existing 415/480 VAC systems". Alternating current, the kind the grid delivers, "remains the default" for today's AI data centres, and 800 volts comes as "an additional deployment option".

That is the claim of this piece. 800 volts reaches the AI rack before it reaches the building. Until 2028 it arrives in a cabinet beside the rack, fed from the old power room, and no data hall of 10 megawatts or more runs on 800 volts made at the building's edge. So for now every megawatt carries both the old gear and the new.

To see why, the piece follows the questions in order. Why a rack needs a new kind of power, what volts and amps are, and how power travels from the grid to the chip. Then what breaks first at a megawatt, why the answer is 800 volts, and the three places the conversion can happen. Then why the rack goes first, what holds the building back, and why switching off direct current is hard. Finally, which chips do the work, who is paid while the building waits, and what would prove me wrong.

{{ANALOGY}}

## Why does an AI rack need a new kind of power at all?

Because one rack of AI chips now draws what a street of houses draws, and each new generation multiplies it.

A **rack** is the steel cabinet, about the size of a wardrobe, that holds a data centre's computers. Its power is counted in **kilowatts (kW)**, thousands of watts; a kettle draws two or three. The typical rack in the world's data centres averaged about 7.5 kW in 2025, Uptime Institute's survey of operators found, as The Register reported it. That is the draw of a few kettles.

Nvidia's GB200 NVL72, the AI rack that went into volume in 2025, draws about 120 kW, on Nvidia's own figure in its user guide. It holds 72 of Nvidia's graphics processors, its **GPUs**, the chips that do the AI work. One such rack draws as much as about sixteen typical racks.

{{FIG1}}  <!-- One AI rack now draws about what sixteen ordinary racks draw, and the roadmap keeps climbing -->

The climb comes from how AI chips are linked. Each GPU uses only about a fifth more power than the generation before, Nvidia wrote in its first 800 volt white paper (October 2025). But **NVLink**, Nvidia's link that lets GPUs share work as if they were one chip, runs over short copper cables. So the more GPUs that must act as one, the more of them are packed into one rack, and rack power rises "2x, 4x or 8x".

Nvidia's 2026 white paper gives the roadmap. Its first generation of rack power carried up to 145 kW. The second, released with its Vera Rubin rack, can carry 330 kW, a ceiling rather than a measured draw. A third, with liquid-cooled power supplies, can support up to 570 kW in one rack position, and only a fourth carries 800 volts all the way inside the rack.

Beyond that, the targets get vague. Nvidia said in May 2025 that 800 volts would serve "1 MW IT racks and beyond, starting in 2027", with its Kyber rack. At its March 2025 conference Kyber was shown at about 600 kW, as the keynote was reported. In March 2026 Nvidia re-introduced Kyber with no power figure and no date. A report by SemiAnalysis, a research firm, said in July that it had slipped to 2028; Nvidia replied that its roadmap was intact. Google, which designs its own AI chips, expects "more than 500 kW per IT rack before 2030".

## What are volts, amps and watts, and why does the current matter?

Power is voltage times current, so for the same power a lower voltage needs more current, and current is what heats copper.

**Voltage**, in volts, is the push behind electricity. **Current**, in amps, is the flow of charge. **Power**, in watts, is the two multiplied. Think of water in a hose: voltage is the pressure, current the flow, and power what the water can do. A **megawatt (MW)** is a million watts, the draw of several hundred homes.

So a megawatt at 54 volts needs 1,000,000 divided by 54, about 18,500 amps. At 800 volts it needs 1,250. A household circuit carries 10 to 32 amps, so a one megawatt rack at 54 volts would push the current of several hundred to nearly two thousand household circuits down one copper bar.

Current costs heat. A conductor's heat is its current squared times its **resistance**, how hard it is for charge to flow through it. Double the current and the heat quadruples, as friction in a pipe climbs steeply with the flow.

Take a solid copper bar 100 millimetres by 10. My arithmetic, from copper's standard resistivity, gives about 17 millionths of an ohm per metre. At 18,500 amps that bar turns about 5.8 kW into heat in every metre, two kettles' worth, and loses about a third of a volt per metre. At 1,250 amps the same bar loses about 26 watts a metre.

Cutting the current 14.8 times cuts the heat in the same bar about 219 times, which is 14.8 squared. In practice designers do not keep the bar and enjoy a cool rack. They take the gain as thinner, lighter copper, because a bar is sized to carry its current at a safe temperature. That, on my reading, is what Nvidia's 200 kilograms measures.

## How does power travel from the grid to the chip today?

Through five conversions, each made by different firms, and the current rises at every step down.

{{FIG2}}  <!-- The current climbs at every step down, and the power room changes last -->

It arrives as **alternating current (AC)**, which reverses direction 50 or 60 times a second. That reversal is what lets a **transformer**, coils of copper wound on a steel core with no moving parts, step the voltage up or down. It is why grids run on AC. The feed into a large site is **medium voltage**, typically 13.8 to 35 kilovolts, thousands of volts.

In the **power room**, transformers step it down to 415 or 480 volts AC. The **UPS**, the uninterruptible power supply, sits there too. It turns AC into direct current to charge its batteries, then back into AC for the hall, so that a dip on the grid never reaches the computers.

From the power room, **busway**, insulated copper bars along a row of racks, carries the 415 volts out. Flexible cables called **whips** drop from it into each rack. Inside the rack, **power shelves**, drawers of power supply units, turn it into **direct current (DC)**, which flows one way and is what chips use. In the GB200 rack, eight shelves of six 5.5 kW supplies make about 50 volts; Nvidia's later racks run at 54.

A thick copper **busbar** runs up the back of the rack and carries that voltage to every tray of computers. On each tray an **intermediate bus converter** steps 54 volts down to 12. Then **voltage regulators**, dozens of tiny converters millimetres from each GPU, step 12 volts down to below 1 volt for the chip itself.

The current tells the story. At one megawatt, my arithmetic gives about 16 amps per phase on a 35 kV feed and about 1,390 amps per phase at 415 volts. It is about 18,500 amps on the rack's 54 volt busbar, about 83,000 at 12 volts and, at an assumed 0.8 volts at the chip, about 1.25 million amps, spread over thousands of power stages.

That is why every design converts to low voltage as late and as close to the chip as it can. Each conversion also wastes a little: Nvidia's October 2025 post says a facility on AC end to end "can be less than 90%" efficient from grid to chip.

<a id="the-rack-runs-out-of-copper"></a>

## What breaks first when a rack nears a megawatt on 54 volts?

Space inside the rack runs out before the copper does, so the power supplies must leave the rack first.

Nvidia made the case in May 2025. Above 200 kW, it wrote, racks begin "to hit physical limits". A megawatt rack at 54 volts would need up to 200 kg of copper busbar, and up to 200,000 kg across a one gigawatt site. A **gigawatt (GW)** is a thousand megawatts.

Its power shelves "would consume up to 64 U of rack space for Kyber at MW scale". A **U**, or rack unit, is 44.45 millimetres of height, and a standard full-height rack holds 42. By my arithmetic, 64 U of shelves would stand about 2.8 metres tall, taller than the rack. Nothing would be left for the computers.

Space matters twice. The first white paper calls the space near the GPUs, within reach of NVLink's short cables, "the highest value real estate in the rack". Every slot a power shelf takes is a slot that cannot hold a GPU tray. So moving power parts out of the rack is worth doing even before the copper becomes the limit.

Nvidia's own 2026 roadmap shows what moves first. The 200 kW line was its 2025 statement. Its 2026 white paper keeps the 54 volt busbar inside the rack up to 570 kW, with liquid-cooled power shelves, and says "near-term generations will continue leveraging the proven 54 VDC distribution plane". Native 800 volt distribution inside the rack waits for its fourth generation.

So 800 volts arrives at the rack's door before it reaches its spine. The new cabinet beside the rack makes 800 volts and sends it in over a short cable. A shelf inside the compute rack turns it back into 54 volts for the busbar. The power supplies leave; the copper spine stays a while longer.

## Why 800 volts, and not 400 or 1,500?

Because 800 volts cuts the copper enough to matter while staying inside the rules and breakers that exist; higher voltages run into both.

{{FIG3}}  <!-- At 800 volts the same copper carries more than two and a half times the power -->

The gain from voltage depends on the comparison. Against 54 volts inside the rack, current falls about fifteenfold. Against the 415 volts AC that runs along today's rows, the gain is smaller but still large. On Nvidia's October 2025 comparison, at the same wire size, 800 volts DC carries 157% more power than 415 volts AC. Its May 2025 post gave 85% more power and 45% less copper, on a different basis; both are Nvidia's, five months apart.

DC also needs fewer wires. Three-phase AC uses four conductors; 800 volts DC uses three, a positive, a return and an earth.

Higher would cut more copper. On Nvidia's table, 1,500 volts carries 382% more power than 415 volts AC. But the first white paper calls 1,500 volts only a "potential long-term target". American electrical rules for indoor IT equipment, and the danger of an arc flash in a confined rack, hold it back. 1,500 volts is the top of what codes call low voltage in solar farms, not in a room where technicians work.

Lower is the other camp. In October 2024 Microsoft and Meta proposed **Mt Diablo**, a separate power rack beside the compute rack, at **±400 volts**. That is 400 volts above earth on one conductor and 400 volts below it on another: 800 volts between them, but no wire more than 400 volts from earth. Google joined in April 2025, writing that ±400 volts "will enable IT racks to scale from 100 kilowatts up to 1 megawatt". It picked 400 volts to borrow parts made for electric cars, and said its first sidecar improved end-to-end efficiency "by ~ 3%".

Nvidia picked a single 800 volt pair for a practical reason. Its first white paper says ±400 volts needs "specialized three-pole breakers and protection devices that are not widely available", while single-ended 800 volts "aligns with existing two-pole breaker designs". Its compute racks accept ±400 volt sources too. Europe has its own variants at 750 volts and at 700 and 350 volts.

The camps are converging. Mt Diablo's specification reached version 1.0.0 on 8 October 2026, with Microsoft, Meta and Google as authors: an AC-fed power rack delivering ±400 volts to a nearby compute rack, 800 kW to 1.1 MW at 480 volts in. But the building-scale specification the same hyperscalers wrote with Nvidia specifies a single 800 volt output. This piece counts ±400 volts as 800 volts, since that is the voltage pole to pole.

## Where can the grid's alternating current become 800 volts?

In three places: in a cabinet beside the rack, in a larger cabinet at the end of a row, or in a block at the building's edge. Only the last removes the old power room.

{{FIG4}}  <!-- Two options keep the old power room; only the third removes it -->

Nvidia's 2026 white paper names them Options A, B and C. **The power rack**, Option A, is a cabinet the size of a rack, rated about 660 kW, standing beside one or two compute racks. It takes twelve of the hall's existing AC whips at 415 to 480 volts and turns them into 800 volts DC on shelves of six 18.3 kW supplies, with optional batteries. "The Power Rack is entering production in Q3 2026," Nvidia writes.

**The row power centre**, Option B, is one larger cabinet at the end of a row, adjustable to 2 MW. It feeds the whole row over an overhead 800 volt busway, with tap boxes dropping into each rack. It still takes AC from the existing power room, a "retrofit deployment without modification to upstream AC electrical rooms". Nvidia expects it "as soon as Q3 2027".

**The DC power block**, Option C, is the end state. A containerised unit of about 4.8 MW stands outside the building and turns medium voltage AC straight into 800 volts DC. The 415 and 480 volt layer, its transformers and its AC power room go. Nvidia describes 20 MW deployment units of four such blocks. It gives no date for the version built from conventional parts, but groups all three options under "near-term deployment readiness". The later date is for the next generation SST fed at 34.5 kV: it "is expected to be launched toward 2029".

Nvidia now presents the three as "not sequential requirements, but flexible deployment options". In October 2025 it had said the move "will occur in phases". Either way, AC remains the default for today's deployments in its reference design, which Nvidia says will be updated to add 800 volt options. The claim's test counts only Option C, or anything like it: 800 volts made at the scale of the facility.

## Why does the rack go first?

Because a power rack can ship as computer equipment into a hall that changes nothing, while the building step needs new equipment, new rules and a new room.

The first reason is certification. Nvidia's power rack is certified under UL 62368-1, the safety standard for IT equipment, "while limiting data hall-level 800 VDC exposure". The 800 volts stays inside the pair of racks and the cable between them. It "can be certified now for both UL and IEC region deployments", the white paper says. A row of 800 volt busway or a building-wide bus falls under the building's electrical code, which is not ready.

The second is the room itself. The power room's transformers and switchgear are booked years ahead; their makers hold years of orders, as [the equipment queue](/journal/the-equipment-queue/) shows. My inference, from those order books, not from any maker's statement: a hall opening in 2028 has probably already ordered gear for an AC power room. And no owner tears out a working power room, built to run for decades, for one generation of racks.

The third is that the building's new converter is not ready, and the fourth is that its breakers and codes are not either; the next sections take each. A fifth is the backup. Today's UPS sits in the AC room. In Nvidia's end state, capacitors sit beside the racks to absorb swings shorter than a tenth of a second, and batteries sit at the grid connection. That is a redesign of the hall's backup, not a swap.

The price of going first is extra gear. Nvidia's first white paper calls the power rack "transitional", for retrofitting halls, and "not the optimal solution end-to-end due to the extra stages of conversion". In June 2026 it described power racks as "a bridge for existing AC-based facilities toward hybrid AC and 800 VDC". A bridge means the AC room stays and a power rack joins it, so the gear per megawatt rises before it falls.

## What is a solid-state transformer, and why is it not ready?

It is an electronic replacement for the transformer and rectifier at the building's edge, and its first specification is still a draft.

A transformer's size is set by how often the current reverses. At the grid's 50 or 60 cycles a second, stepping megawatts down needs tonnes of steel and copper. A **solid-state transformer (SST)** first chops the incoming medium voltage with fast switches, thousands of times a second. At that speed a small transformer can do the work of a large one, and the output is turned straight into 800 volts DC.

The Open Compute Project, an industry body where large buyers publish hardware designs, defines it as a "megawatt-scale power electronic converter". It replaces "conventional 50/60Hz line-frequency Medium Voltage transformer, rectifier units and energy storage". Its specification, written by Google, Microsoft and Nvidia, reached revision 0.3.0 on 22 June 2026, a "first draft".

That draft sets two sizes: a 5 MW unit taking 13.8 kV, and a 5 or 10 MW unit taking 34.5 kV, both making 800 volts at 98% efficiency or better in their power train. Even the earthing is open: floating or high-resistance, "detailed design TBD".

The higher voltage is the harder one. Nvidia's 2026 white paper says "most commercially available SST platforms today remain focused on approximately 15kV-class input", and 34.5 kV needs more development. Hence its date for the next generation: "toward 2029".

{{FIG5}}  <!-- Most dated 800 volt products reach the building in late 2027 or later -->

The makers' own dates sit at the same distance. Eaton said on 3 November 2026 that its 15 kV, 2 MW unit had passed all its UL tests in October, with ten pilots running and "multiple 15 kV projects that we are going to ship this year". In May it had said it expected orders for 800 volt DC projects in the second half of 2026, "for shipments starting in late 2027". ABB says its SST will be "commercially available in the second half of 2027". Siemens and Reinhausen are developing one for up to 36 kV, with no date.

Schneider Electric was bluntest. At its investor day in December 2025 it said it did not see the SST "at large" before 2027. Vertiv dates its data hall level 800 volt systems to validation in 2027 and deployment in 2028. Most makers date their volume building-scale products to late 2027 or later. Eaton is the exception in timing: its first 15 kV units ship this year, though its 800 volt DC projects ship from late 2027.

## Could a building go to 800 volts without waiting for the solid-state transformer?

Yes, with an old technology, and that is the biggest risk to my claim.

A **transformer rectifier unit**, or medium voltage rectifier, is a conventional transformer feeding a large rectifier, a converter that turns AC into DC. Mines, aluminium smelters, electrolysers and railways have used them for decades. Nvidia's first white paper calls them "a faster and proven path for quick 800 VDC deployment" than the SST.

That white paper's reference design was built on them: a 17.5 MW block of five 3.5 MW medium voltage rectifiers, any four of which carry the load, feeding a 5,000 amp DC switchboard. Its 2026 paper says such units "remain highly practical for approximately 5 MW-class" blocks. My claim counts any "facility-level rectifier", not only an SST. So a 10 MW hall on rectifier units before 2028 would break it, with no new transformer technology needed.

Why has none been named? On my reading, because the rectifier is the easy part. A building-wide 800 volt bus still needs DC switchboards, a chosen earthing scheme, breakers for faults the hall has never had, and an inspector willing to sign it off. Those are the same gates whatever makes the 800 volts.

One owner has gone through them on its own ground. On 2 November 2026 Envision, a Chinese group that makes wind turbines and batteries, said an 800 volt system on solid-state transformers, converting 10 kV medium voltage straight to an 800 volt DC bus, is "now powering live computing workloads". It is at its campus in Ulanqab, Inner Mongolia, open since August 2026.

That is an operator, a building-level converter and live load: the falsifier's shape. I concede the building step is closer than "toward 2029" sounds. Strictly, Envision already shows 800 volts entering a hall without a power rack; what keeps the claim standing is size. The test needs 10 MW, and Envision gives no size for the 800 volt system; the 3 GW it cites is the plan for the whole campus. A 10 kV input also fits Nvidia's point that today's SSTs are 15 kV class. If Envision states 10 MW or more before 2028, the claim breaks.

<a id="the-off-switch"></a>

## Why is switching off 800 volts of direct current harder than switching off AC?

Because AC passes through zero a hundred or more times a second, which puts out the spark when a breaker opens, and DC never does.

When a breaker's contacts pull apart under load, current jumps the gap as an **arc**, a spark of glowing gas. Alternating current falls to zero 100 or 120 times a second, and a mechanical breaker uses that moment to snuff the arc. Direct current holds steady, so an arc "can sustain without zero-crossings", Nvidia's 2026 white paper says. "Without a natural current zero, mechanical interruption faces challenges with arcing," Infineon said in September 2026.

{{FIG6}}  <!-- AC puts out its own arc a hundred times a second; DC never does -->

There is a counterweight. On a converter-fed DC system, a fault often carries less energy. A fault on AC draws on the grid and spinning machines, while DC fed through power electronics is "often lower in converter-limited systems". The heat of an **arc flash**, the blast when a fault arcs through air, depends on the current and on how long it flows. Nvidia's plan attacks both: sources that limit their own current, and breakers that clear fast.

On day one the breakers are mechanical. Nvidia expects **moulded case circuit breakers**, the ordinary kind in a sealed plastic case, "to serve as the primary branch protection device for initial production systems". They clear in "up to approximately 20 ms", twenty thousandths of a second, so feeds need backup or stored energy to ride through.

Later come **solid-state circuit breakers**, which cut current with semiconductors in microseconds, millionths of a second, with no arc at all. Their price is a little heat all the time, because a semiconductor is not a perfect wire when on. Nvidia calls them "the preferred long-term protection solution", in two target sizes, 125 amps and 1,250 amps. Wider use depends on "supply chain readiness, regulatory certification, product availability, and cost".

The devices exist. ABB says its SACE Infinitus was the first solid-state breaker fully certified to the international standard for circuit breakers, rated up to 1,250 volts DC on its own page. Siemens launched one for low voltage DC in April 2026, with Infineon supplying 1.2 kV silicon carbide modules. Infineon and SolarEdge, an inverter maker, announced one for 800 volt data centres in September 2026; Power Integrations and Ideal Power showed a prototype in October.

What is missing is the rulebook. An international standard for semiconductor circuit breakers, IEC 60947-10, was published only in May 2026. America's electrical code, the NEC, covers DC, but it has no requirements written for data centres yet, an Open Compute Project paper of March 2026 says. Its next edition, for 2029, with task groups on DC systems and data centres, "will be completed in the third quarter of 2028".

Until then, the paper says, firms "must lean on interim guidance". Each local **authority having jurisdiction**, the inspector who signs off a building, decides. Nvidia's 2026 paper says engaging those authorities "has become an important enabler", with inspection guidelines and training in development. Even the earthing is undecided: four schemes are under study, to be settled "through system-level studies".

So the rack goes first for safety reasons too. Inside a power rack, the converters limit how much current a fault can draw, and the 800 volts stays between two cabinets. My inference: a building-wide bus fed by megawatt converters, batteries and capacitors is a larger and newer kind of fault, and the rules for it are two years from finished.

## Which chips do the switching, and why does the material matter?

Every converter in the chain is built around a power switch, and the switch's material decides how much voltage it can hold, how hot it can run and how fast it can flick.

A converter changes one voltage into another by switching current on and off very fast, then smoothing the result with coils and capacitors. The **power semiconductor** is the switch. It loses energy two ways: a little when on, because it is not a perfect wire, and a little in every flick, because for an instant it carries voltage and current at once.

Faster switching lets the coils and transformers around it shrink, since they store less energy per cycle. In a crowded rack, that density is the prize. But faster only pays if each flick is cheap.

The material sets the limits. Its **bandgap** is the energy an electron needs to break loose and conduct. Silicon's is 1.12 electron volts. **Silicon carbide (SiC)** and **gallium nitride (GaN)** have about three times as much, so they hold about ten times the electric field before breaking down. A switch blocking 800 volts can be about a tenth as thick, so it loses less when on and flicks faster.

Silicon carbide also moves heat about three times better than silicon. Gallium nitride flicks fastest of the three but moves heat slightly worse. So SiC belongs where voltages run to kilovolts and heat is the enemy: solid-state transformers, the grid side of rectifiers, and solid-state breakers. Infineon and SolarEdge, for example, are developing a megawatt-scale SST on Infineon's SiC.

GaN belongs at and below the 800 volt bus. Most power GaN is rated 650 volts or less, so designs mostly stack two to block 800. That is changing: Power Integrations now offers 1,250 and 1,700 volt GaN, and onsemi showed an 800 to 6 volt converter on its vertical GaN in October 2026.

On the compute tray, Texas Instruments' converter steps 800 volts to 6 with GaN at 97.6% efficiency, a peak figure, not a full-load one (March 2026). Nvidia's own Kyber design steps 800 to 12 volts in one stage of 64 to 1, in 26% less board area. Silicon stays at the last step, next to the GPU, where voltages are low and silicon is cheapest.

Not everyone accepts the plan. Vicor, which makes power modules, called an 800 to 6 volt bus design misguided on its first quarter 2026 call, as press reported it, and argues for its own modules instead.

## Are those chips in short supply?

Power chips for AI are tight, but the tightness is in silicon near the chip; silicon carbide is not short, and GaN's supply is changing hands.

Infineon, the German power chip maker, said on 5 August 2026: "Demand for our AI power solutions continues to outstrip available supply, we are in allocation." Several customers had signed or were negotiating multi-year capacity reservations, worth "a high single-digit billion Euro amount" of sales. Lead times were rising, which it called "a typical early-upcycle pattern".

Its AI power revenue was to pass €1.6 billion in the year to September 2026, more than double the year before, with about €500 million of other data centre power on top. It said it would raise its target of €2.5 billion or more for 2027 in November. onsemi said on 2 November that supply was constrained in some technologies.

On my reading, that is AI power broadly, mostly silicon power stages and controllers, not 800 volt parts. Silicon carbide is the opposite story. Wolfspeed, an American SiC maker, went through a prepackaged Chapter 11 and emerged on 29 September 2025. Renesas, which had prepaid it US$2.06 billion for wafers, booked a ¥235 billion loss. Chinese SiC wafers moved from shortage to oversupply, press reports say.

GaN's supply is being reshuffled as the rack pulls it forward. Navitas, a GaN chip maker, said in July 2025 that TSMC, the Taiwanese foundry, "will end GaN production in July 2027". It is moving its 650 volt parts to Powerchip, also in Taiwan, "over the next approximately 12-24 months".

Navitas has since added a second source. GlobalFoundries is to make its GaN at Burlington, Vermont, under a partnership of 20 November 2025, and Navitas announced first shipments of its newest US-made parts on 3 November 2026. It also says it has bought buffer capacity at TSMC to support existing customers "through 2029 and beyond", per its July call.

Infineon is to invest about €1.1 billion by 2034 in GaN on 300 millimetre wafers at Villach in Austria. Volume production is due from the end of 2027, and the EU approved €319 million of Austrian state aid on 27 October 2026, as reported. Innoscience, a Chinese GaN maker with its own fabs, said its shipments for AI and data centres rose 183% in the first half of 2026.

{{FIG7}}  <!-- Today the money at the chip is in silicon, not in GaN at 800 volts -->

Scale settles where the money is today. Monolithic Power Systems, which makes power stages beside processors, booked US$506.7 million in its Enterprise Data segment in the third quarter of 2026. Navitas's entire revenue in the same quarter was US$14.0 million. The money flowing now is in silicon at the chip, in racks still running at 48 and 54 volts. I concede GaN is a small share of a rack's cost, and silicon or SiC can make the 800 volt step less efficiently, so this is not a shortage call.

## Who is paid while the building waits?

The makers of power racks, which sell a cabinet for each new row, and the makers of AC power rooms, which keep selling to every hall built in the meantime.

The cabinets are here. Delta and Flex each launched an 800 volt power rack at Nvidia's March 2026 conference, and Lite-On showed one. Flex says its rack takes a compute rack "from approximately 125 kW to up to 880 kW". Delta's 660 kW rack holds six 110 kW shelves with batteries. Its chairman said in July that mass shipments would begin in the third quarter, as the Taipei Times reported. Schneider Electric is developing a sidecar for racks of up to 1.2 MW.

Vertiv, a maker of data centre power and cooling gear, now gives later dates than it first did. In May and October 2025 it said its 800 volt range would be released in the second half of 2026. Its May 2026 investor deck says its PowerDirect 5000, a sidecar of up to 900 kW, has "Commercial launch expected in early 2027". A July blog still spoke of commercialisation from the second half of 2026, with deployments beginning in 2027. Rack and pod products are under customer validation in 2026, for deployment in 2027; the data hall level follows in 2028.

Meanwhile the AC side keeps selling. Eaton's data centre sales grew 65% in the third quarter of 2026 and its data centre orders 101%, its chief executive said on the call. Fibrebond, the maker of prefabricated power rooms Eaton bought in 2025, earned US$375 million in its first year and has "jumped already to $600 million". These are rooms of AC switchgear, the gear a power rack plugs into.

<a id="every-megawatt-got-harder"></a>

Vertiv puts a figure on what a megawatt holds. Its management estimated in May 2026 that it could sell about US$3.25 million to 3.75 million of power and cooling gear into each megawatt of IT power, up about 10 to 15% on its earlier range. That is an estimate of opportunity, not reported revenue. Part of the rise may reflect scope Vertiv has bought, such as PurgeRite, which flushes and fills liquid cooling loops, closed in December 2025 for about US$1.0 billion upfront.

Since the estimate Vertiv has bought more. It agreed in September 2026 to buy Utility Innovation Group, which designs microgrids and on-site power for data centres, for about US$1.45 billion plus up to US$1.15 billion more, and closed in late October.

Schneider Electric's estimate cuts the other way. Its finance chief put its own opportunity at "$1.2 million to $3.3 million per megawatt" in December 2025. She added that the most complex AI sites were not expected to "trend to the top of that range" over five years. The two estimates have different scopes and cannot be compared, and Schneider's does not suggest the most complex sites keep climbing.

Vertiv's results fit growth more than richer gear. In the third quarter of 2026 its sales grew 55.0% organically, stripping out acquisitions and currency. Its adjusted operating margin, the share of each sale left after running costs with one-off items removed, widened 2.9 points to 25.2%. On the call, per a transcript, its finance chief credited "strong sales volume increase, operating leverage, and continued productivity", not richer content.

Services, the steadier part of the business, grew 18.1% organically against 63.6% for products, and fell from 19.0% to 16.7% of sales. Organic orders more than doubled. But Vertiv stopped reporting quarterly orders and backlog in February, and its executive chairman said in October it is "not planning to share orders data going forward".

<a id="ti-feeds-the-chip"></a>

## Does the chip side show 800 volts yet?

It shows a data centre business growing fast, but not yet because of 800 volts; the growth is density at today's voltages.

Texas Instruments makes the small, cheap power chips beside the processor: hot-swap controllers, which let a board be plugged in live, converters and power stages. Its data centre sales were US$1.5 billion in 2025, up 64% and 9% of revenue. In the second quarter of 2026 they doubled. In the third they were "up about 95% year-on-year", per the call transcript, and about 13% of revenue. On a third-quarter revenue of US$6.06 billion, my arithmetic puts that near US$790 million, about a US$3.1 billion yearly pace.

The cause is not yet 800 volts. Racks shipping in volume today run at 48 and 54 volts, and "800 volt" does not appear in the transcript of TI's October call. Its executives named density and voltage together: "Power density is critical", and "When there is higher voltages, more opportunity for TI."

TI is filling new capacity as it grows. Its first fab at Sherman, Texas, a 300 millimetre plant called SM1, began production on 17 December 2025. Capital spending fell to US$463 million in the quarter from US$1,197 million a year earlier, and its gross margin was about 64%, by my arithmetic from the release. Industrial sales grew more than 40%, so on my reading the new lines are unlikely to be running part-empty.

The peers show the same. Monolithic Power's Enterprise Data revenue rose 164.6% in the third quarter, and its release says it has begun sampling GaN parts for 800 volt data centre designs. onsemi's AI data centre revenue rose 175%, to about US$180 million, and it agreed to buy Ferric, which makes power delivery for AI processors. The money arrives with density first; 800 volts is still being sampled.

## Is any hall running on 800 volts from the building yet?

Not one of 10 megawatts or more that anyone has named, as of 7 November 2026.

Envision's system is live but unsized. Nvidia named Foxconn's 40 MW Kaohsiung-1 in Taiwan as being built for 800 volts in October 2025, and five cloud providers selling AI computing as "designing for" 800 volt data centres. Each is a design, not a running hall.

I found no named customer hall running even an Nvidia-specification power rack. TrendForce, a market research firm, expects the power rack to ship as "an optional configuration" on Vera Rubin, with adoption rising after Rubin Ultra and widespread use in 2028. At the Open Compute Project's summit in October 2026, sidecars and solid-state transformers were everywhere on the show floor. But "volumes remain modest, field reliability is unproven", the research firm Dell'Oro wrote.

## So who holds the scarce thing, and what should an investor watch?

The rack moves on the chip's schedule; the building moves on the schedule of equipment, codes and inspectors. Whoever sells into today's AC room while also selling the cabinet beside the rack is paid twice in the meantime.

If the claim is right, three kinds of business gain first. **The cabinet builders**: makers of power racks and row power centres sell a new cabinet for each new row. **The AC room's makers**: transformer, switchgear and UPS makers keep selling to every hall built while the building waits. **The chips near the processor**: power stages and converters, mostly silicon, ride density at 48 and 54 volts now and 800 volts later.

Others wait. SiC makers wait longest for the volume that comes only when buildings convert, though SiC enters early inside breakers. Makers of 54 volt power shelves inside the compute rack lose their slot as the supplies move next door. The in-rack copper busbar survives until the fourth generation.

The readings come soon. Infineon reports its year in November and is to raise its AI target. Eaton says several 15 kV SST projects ship this year, and expected orders for 800 volt DC projects in the second half of 2026. Vertiv's sidecar is due in early 2027, Nvidia's row power centre as soon as the third quarter of 2027, and ABB's SST in the second half of 2027. The NEC's 2029 edition is due in the third quarter of 2028.

## What would prove me wrong

The test is a named hall. If, before 1 January 2028, Nvidia, a data centre operator or its equipment supplier says a hall of 10 MW or more is in service on 800 volts made by a facility-level rectifier or solid-state transformer, the building did not wait for the rack. The likeliest route is not an SST but a transformer rectifier unit, which Nvidia itself calls proven. Envision stating 10 MW or more, or Foxconn's Kaohsiung-1 going live on a building block, would do it.

Two events would move me before the test. The SST specification reaching a finished version, or a maker shipping an SST for a named hall before 2028, would show the building catching up. And if power racks ship but Vertiv cuts its per-megawatt estimate, or halls drop the AC room as racks arrive, more gear first is wrong even if the order holds.

The claim stands on two legs. The rack must move: that is current against copper and rack space, and no falsifier attacks it; only a rack that stops growing would. The building waits: that rests on equipment, standards and protection, which money and a greenfield owner can speed. The named hall attacks that leg, and Vertiv's estimate attacks its consequence.

Plans would not move me. Nvidia said in May 2025 that full-scale production would come with Kyber in 2027, and Kyber's own date is now unclear. Kaohsiung-1 and the five cloud providers are designs. Nor would the view that 800 volts is a silicon carbide story today: on Nvidia's and Vertiv's own dates the first products are power racks fed by AC rooms, so GaN and tray converters move first, and SiC transformers wait for buildings.

At the scale of the chip, the material follows the voltage. At the scale of the rack, current and space force the move now. At the scale of the building, rooms booked years ahead, a draft specification and a code two years from finished set the pace, unless one owner builds the end state on its own ground.
