<a id="powering-the-rack"></a>

Nvidia has done something unusual for a chipmaker. It has written down why its own design cannot go on. Wired the way racks are today, it said in May 2025, a rack drawing one megawatt would need up to 200 kilograms of copper bar, and its power supplies would leave no room in the rack for the computers.

So the industry is moving the rack from 54 volts to 800. Yet in its 2026 white paper Nvidia writes that 800 volts "is not intended to replace existing 415/480 VAC systems". Alternating current, the kind the grid delivers, "remains the default" for today's AI data centres, and 800 volts comes as "an additional deployment option".

That is the claim of this piece. 800 volts reaches the AI rack before it reaches the building. Until 2028 it arrives in a cabinet beside the rack, fed from the old power room, and no data hall of 10 megawatts or more runs on 800 volts made at the building's edge. So for now every megawatt carries both the old gear and the new.

{{ANALOGY}}

## Why does an AI rack need a new kind of power at all?

Because one rack of AI chips now draws what a street of houses draws, and each new generation multiplies it.

A **rack** is the steel cabinet, about the size of a wardrobe, that holds a data centre's computers. Its power is counted in **kilowatts (kW)**, thousands of watts; a kettle draws two or three. The typical rack averaged about 7.5 kW in 2025, Uptime Institute's survey of operators found, as The Register reported it.

Nvidia's GB200 NVL72, the AI rack that went into volume in 2025, draws about 120 kW, on Nvidia's own figure. It holds 72 of Nvidia's graphics processors, its **GPUs**, the chips that do the AI work. One such rack draws as much as about sixteen typical racks.

{{FIG1}}  <!-- One AI rack now draws about what sixteen ordinary racks draw, and the roadmap keeps climbing -->

The climb comes from how AI chips are linked. **NVLink**, Nvidia's link that lets GPUs share work as if they were one chip, runs over short copper cables. So the more GPUs that must act as one, the more of them are packed into one rack. Nvidia's 2026 white paper gives the roadmap: a first generation of rack power carrying up to 145 kW, a second able to carry 330 kW, and a third up to 570 kW. Only a fourth carries 800 volts all the way inside the rack.

Beyond that, the targets get vague. Nvidia said in May 2025 that 800 volts would serve "1 MW IT racks and beyond, starting in 2027", with its Kyber rack. In March 2026 it re-introduced Kyber with no power figure and no date.

## Why does a low voltage become a problem at a megawatt?

Because power is voltage times current, so a lower voltage needs more current, and current is what heats copper.

**Voltage**, in volts, is the push behind electricity. **Current**, in amps, is the flow of charge. **Power**, in watts, is the two multiplied. A **megawatt (MW)** is a million watts, the draw of several hundred homes.

So a megawatt at 54 volts needs 1,000,000 divided by 54, about 18,500 amps. At 800 volts it needs 1,250. A conductor's heat is its current squared times its **resistance**, how hard it is for charge to flow through it. Cutting the current 14.8 times cuts the heat in the same copper bar about 219 times, which is 14.8 squared.

In practice designers do not keep the bar and enjoy a cool rack. They take the gain as thinner, lighter copper, because a bar is sized to carry its current at a safe temperature. That, on my reading, is what Nvidia's 200 kilograms measures.

## How does power travel from the grid to the chip today?

Through five conversions, each made by different firms, and the current rises at every step down.

{{FIG2}}  <!-- The current climbs at every step down, and the power room changes last -->

It arrives as **alternating current (AC)**, which reverses direction 50 or 60 times a second. That reversal is what lets a **transformer**, coils of copper on a steel core, step the voltage up or down. The feed into a large site is **medium voltage**, typically 13.8 to 35 kilovolts.

In the **power room**, transformers step it down to 415 or 480 volts AC. The **UPS**, the uninterruptible power supply, sits there too, so that a dip on the grid never reaches the computers. Insulated copper bars along a row of racks carry the 415 volts out. Inside the rack, **power shelves**, drawers of power supply units, turn it into **direct current (DC)**, which flows one way and is what chips use; Nvidia's later racks run at 54 volts.

A thick copper **busbar** runs up the back of the rack and carries that voltage to every tray of computers. There converters step it to 12 volts, then to below 1 volt for the chip itself. At one megawatt, my arithmetic gives about 18,500 amps on the rack's 54 volt busbar and, at an assumed 0.8 volts at the chip, about 1.25 million amps, spread over thousands of power stages.

That is why every design converts to low voltage as late and as close to the chip as it can.

<a id="the-rack-runs-out-of-copper"></a>

## What breaks first when a rack nears a megawatt on 54 volts?

Space inside the rack runs out before the copper does, so the power supplies must leave the rack first.

Nvidia made the case in May 2025. Above 200 kW, it wrote, racks begin "to hit physical limits". A megawatt rack at 54 volts would need up to 200 kg of copper busbar. Its power shelves "would consume up to 64 U of rack space for Kyber at MW scale". A **U**, or rack unit, is 44.45 millimetres of height, and a standard full-height rack holds 42. By my arithmetic, 64 U of shelves would stand about 2.8 metres tall, taller than the rack.

Space matters twice. Nvidia's first 800 volt white paper (October 2025) calls the space near the GPUs, within reach of NVLink's short cables, "the highest value real estate in the rack". Every slot a power shelf takes is a slot that cannot hold a GPU tray.

Nvidia's 2026 white paper keeps the 54 volt busbar inside the rack up to 570 kW, and says "near-term generations will continue leveraging the proven 54 VDC distribution plane". So 800 volts arrives at the rack's door before it reaches its spine. The new cabinet beside the rack makes 800 volts and sends it in over a short cable, where a shelf turns it back into 54 volts. The power supplies leave; the copper spine stays a while longer.

## Why 800 volts, and not 400 or 1,500?

Because 800 volts cuts the copper enough to matter while staying inside the rules and breakers that exist; higher voltages run into both.

{{FIG3}}  <!-- At 800 volts the same copper carries more than two and a half times the power -->

On Nvidia's October 2025 comparison, at the same wire size, 800 volts DC carries 157% more power than the 415 volts AC that runs along today's rows. Higher would cut more copper, but the first white paper calls 1,500 volts only a "potential long-term target". American electrical rules for indoor IT equipment, and the danger of an **arc flash**, the blast when a fault arcs through air, in a confined rack, hold it back.

Lower is the other camp. In October 2024 Microsoft and Meta proposed **Mt Diablo**, a separate power rack beside the compute rack, at **±400 volts**: 800 volts between two conductors, but no wire more than 400 volts from earth. Google joined in April 2025. Nvidia picked a single 800 volt pair because ±400 volts needs "specialized three-pole breakers and protection devices that are not widely available". The camps are converging, and this piece counts ±400 volts as 800 volts, since that is the voltage pole to pole.

## Where can the grid's alternating current become 800 volts?

In three places: in a cabinet beside the rack, in a larger cabinet at the end of a row, or in a block at the building's edge. Only the last removes the old power room.

{{FIG4}}  <!-- Two options keep the old power room; only the third removes it -->

Nvidia's 2026 white paper names them Options A, B and C. **The power rack**, Option A, is a cabinet rated about 660 kW beside one or two compute racks. It takes the hall's existing AC feeds at 415 to 480 volts and turns them into 800 volts DC. "The Power Rack is entering production in Q3 2026," Nvidia writes.

**The row power centre**, Option B, is one larger cabinet at the end of a row, adjustable to 2 MW. It still takes AC from the existing power room, and Nvidia expects it "as soon as Q3 2027".

**The DC power block**, Option C, is the end state. A containerised unit of about 4.8 MW stands outside the building and turns medium voltage AC straight into 800 volts DC. The 415 and 480 volt layer, its transformers and its AC power room go. The claim's test counts only Option C, or anything like it: 800 volts made at the scale of the facility.

## Why does the rack go first?

Because a power rack can ship as computer equipment into a hall that changes nothing, while the building step needs new equipment, new rules and a new room.

The first reason is certification. Nvidia's power rack is certified under UL 62368-1, the safety standard for IT equipment, and the 800 volts stays inside the pair of racks and the cable between them. A building-wide bus falls under the building's electrical code, which is not ready.

The second is the room itself. The power room's transformers and switchgear are booked years ahead, as [the equipment queue](/journal/the-equipment-queue/) shows. My inference, from those order books: a hall opening in 2028 has probably already ordered gear for an AC power room. And no owner tears out a working power room, built to run for decades, for one generation of racks.

The third is that the building's new converter is not ready, and the fourth is that its breakers and codes are not either; the next sections take each. A fifth is the backup. Today's UPS sits in the AC room; in Nvidia's end state, capacitors sit beside the racks and batteries at the grid connection. That is a redesign of the hall's backup, not a swap.

The price of going first is extra gear. Nvidia's first white paper calls the power rack "transitional" and "not the optimal solution end-to-end due to the extra stages of conversion". The AC room stays and a power rack joins it, so the gear per megawatt rises before it falls.

## What is a solid-state transformer, and why is it not ready?

It is an electronic replacement for the transformer and rectifier at the building's edge, and its first specification is still a draft.

A **solid-state transformer (SST)** chops the incoming medium voltage with fast switches, thousands of times a second. At that speed a small transformer can do the work of a large one, and the output is turned straight into 800 volts DC. Its specification, written by Google, Microsoft and Nvidia at the Open Compute Project, an industry body where large buyers publish hardware designs, reached revision 0.3.0 on 22 June 2026, a "first draft".

That draft sets two sizes: a 5 MW unit taking 13.8 kV, and a 5 or 10 MW unit taking 34.5 kV, both making 800 volts at 98% efficiency or better in their power train.

The higher voltage is the harder one. Nvidia's 2026 white paper says "most commercially available SST platforms today remain focused on approximately 15kV-class input", and dates its next generation SST fed at 34.5 kV "toward 2029".

{{FIG5}}  <!-- Most dated 800 volt products reach the building in late 2027 or later -->

The makers' own dates sit at the same distance. Eaton said on 3 November 2026 that its first 15 kV units ship this year. In May it had said it expected orders for 800 volt DC projects in the second half of 2026, "for shipments starting in late 2027". ABB says its SST will be "commercially available in the second half of 2027". Schneider Electric did not see the SST "at large" before 2027, and Vertiv, a maker of data centre power and cooling gear, dates its data hall level 800 volt systems to deployment in 2028.

## Could a building go to 800 volts without waiting for the solid-state transformer?

Yes, with an old technology, and that is the biggest risk to my claim.

A **transformer rectifier unit** is a conventional transformer feeding a large rectifier, a converter that turns AC into DC. Mines, aluminium smelters and railways have used them for decades. Nvidia's first white paper calls them "a faster and proven path for quick 800 VDC deployment". Its reference design was built on them: a block of five 3.5 MW rectifiers. My claim counts any "facility-level rectifier", so a 10 MW hall on rectifier units before 2028 would break it.

Why has none been named? On my reading, because the rectifier is the easy part. A building-wide 800 volt bus still needs DC switchboards, a chosen earthing scheme, breakers for faults the hall has never had, and an inspector willing to sign it off.

One owner has gone through them on its own ground. On 2 November 2026 Envision, a Chinese group that makes wind turbines and batteries, said an 800 volt system on solid-state transformers, converting 10 kV straight to an 800 volt DC bus, is "now powering live computing workloads". It is at its campus in Ulanqab, Inner Mongolia.

That is the falsifier's shape, and I concede the building step is closer than "toward 2029" sounds. What keeps the claim standing is size. The test needs 10 MW, and Envision gives no size for the 800 volt system; the 3 GW it cites is the plan for the whole campus. Nvidia named Foxconn's 40 MW Kaohsiung-1 in Taiwan as being built for 800 volts, and five cloud providers as "designing for" 800 volt data centres. Each is a design, not a running hall. I found no named customer hall running even an Nvidia-specification power rack; TrendForce, a market research firm, expects widespread use in 2028. As of 7 November 2026 I found no named hall of 10 megawatts or more running on 800 volts from the building.

<a id="the-off-switch"></a>

## Why is switching off 800 volts of direct current harder than switching off AC?

Because AC passes through zero a hundred or more times a second, which puts out the spark when a breaker opens, and DC never does.

When a breaker's contacts pull apart under load, current jumps the gap as an **arc**, a spark of glowing gas. Alternating current falls to zero 100 or 120 times a second, and a mechanical breaker uses that moment to snuff the arc. Direct current holds steady, so an arc "can sustain without zero-crossings", Nvidia's 2026 white paper says.

{{FIG6}}  <!-- AC puts out its own arc a hundred times a second; DC never does -->

On day one the breakers are mechanical: **moulded case circuit breakers**, the ordinary kind in a sealed plastic case, clearing in "up to approximately 20 ms". Later come **solid-state circuit breakers**, which cut current with semiconductors in millionths of a second, with no arc at all. Nvidia calls them "the preferred long-term protection solution". The devices exist: ABB and Siemens have launched them, and Infineon and SolarEdge announced one for 800 volt data centres.

What is missing is the rulebook. America's electrical code, the NEC, covers DC, but it has no requirements written for data centres yet, an Open Compute Project paper of March 2026 says. Its 2029 edition, with task groups on DC systems and data centres, "will be completed in the third quarter of 2028". Until then each local inspector who signs off a building decides, and even the earthing is undecided.

So the rack goes first for safety reasons too. Inside a power rack the 800 volts stays between two cabinets. My inference: a building-wide bus fed by megawatt converters is a larger and newer kind of fault, and the rules for it are two years from finished.

<a id="ti-feeds-the-chip"></a>

## Do the power chips show 800 volts yet?

Not yet: the chip side is growing fast, but on density at today's voltages, and 800 volts is still being sampled.

Every converter is built around a **power semiconductor**, a switch. **Silicon carbide (SiC)** and **gallium nitride (GaN)** hold about ten times the electric field of silicon, so they suit high voltages. SiC belongs where voltages run to kilovolts, as in solid-state transformers and breakers. GaN belongs at and below the 800 volt bus. Silicon stays at the last step, next to the GPU.

{{FIG7}}  <!-- Today the money at the chip is in silicon, not in GaN at 800 volts -->

Scale settles where the money is today. Monolithic Power Systems, which makes power stages beside processors, booked US$506.7 million in its Enterprise Data segment in the third quarter of 2026. Navitas, a GaN chip maker, had entire revenue of US$14.0 million in the same quarter. The money flowing now is in silicon at the chip, in racks still running at 48 and 54 volts. Monolithic Power's Enterprise Data revenue rose 164.6%, and its release says it has begun sampling GaN parts for 800 volt data centre designs. onsemi's AI data centre revenue rose 175%, to about US$180 million.

Texas Instruments tells the same story. Its data centre sales were "up about 95% year-on-year" in the third quarter, per the call transcript, about 13% of revenue. But "800 volt" does not appear in that transcript.

## Who is paid while the building waits?

The makers of power racks, which sell a cabinet for each new row, and the makers of AC power rooms, which keep selling to every hall built in the meantime.

The cabinets are here. Delta and Flex each launched an 800 volt power rack at Nvidia's March 2026 conference, and Lite-On showed one. Vertiv's sidecar of up to 900 kW has "Commercial launch expected in early 2027", later than it first said.

Meanwhile the AC side keeps selling. Eaton's data centre sales grew 65% in the third quarter of 2026 and its data centre orders 101%, its chief executive said on the call. Fibrebond, the maker of prefabricated power rooms Eaton bought in 2025, makes rooms of AC switchgear, the gear a power rack plugs into.

<a id="every-megawatt-got-harder"></a>

Vertiv puts a figure on what a megawatt holds. Its management estimated in May 2026 that it could sell about US$3.25 million to 3.75 million of power and cooling gear into each megawatt of IT power, up about 10 to 15% on its earlier range. That is an estimate of opportunity, not reported revenue, and part of the rise may reflect scope Vertiv has bought. Schneider Electric's estimate, "$1.2 million to $3.3 million per megawatt", has a different scope and does not suggest the most complex sites keep climbing.

## So who holds the scarce thing, and what should an investor watch?

The rack moves on the chip's schedule; the building moves on the schedule of equipment, codes and inspectors. Whoever sells into today's AC room while also selling the cabinet beside the rack is paid twice in the meantime.

If the claim is right, three kinds of business gain first. **The cabinet builders** sell a new cabinet for each new row. **The AC room's makers**, of transformers, switchgear and UPS, keep selling to every hall built while the building waits. **The chips near the processor**, mostly silicon, ride density at 48 and 54 volts now and 800 volts later. SiC makers wait longest, for the volume that comes only when buildings convert.

The readings come soon. Eaton expected orders for 800 volt DC projects in the second half of 2026. Vertiv's sidecar is due in early 2027, Nvidia's row power centre as soon as the third quarter of 2027, and ABB's SST in the second half of 2027. The NEC's 2029 edition is due in the third quarter of 2028.

## What would prove me wrong

The test is a named hall. If, before 1 January 2028, Nvidia, a data centre operator or its equipment supplier says a hall of 10 MW or more is in service on 800 volts made by a facility-level rectifier or solid-state transformer, the building did not wait for the rack. The likeliest route is not an SST but a transformer rectifier unit, which Nvidia itself calls proven. Envision stating 10 MW or more, or Foxconn's Kaohsiung-1 going live on a building block, would do it.

Two events would move me before the test. The SST specification reaching a finished version, or a maker shipping an SST for a named hall before 2028, would show the building catching up. And if power racks ship but Vertiv cuts its per-megawatt estimate, or halls drop the AC room as racks arrive, more gear first is wrong even if the order holds.

Plans would not move me. Nvidia said in May 2025 that full-scale production would come with Kyber in 2027, and Kyber's own date is now unclear. Kaohsiung-1 and the five cloud providers are designs.

At the scale of the chip, the material follows the voltage. At the scale of the rack, current and space force the move now. At the scale of the building, rooms booked years ahead, a draft specification and a code two years from finished set the pace, unless one owner builds the end state on its own ground.
