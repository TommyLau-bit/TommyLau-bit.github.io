---
title: "Data centres in orbit: the plug is free and the heat is the bill"
date: 2026-11-02T16:55:31+08:00
summary: "SpaceX, Google and a start-up called Starcloud plan AI data centres in orbit, where the sun almost never sets and nobody queues for the grid. But in a vacuum heat can leave only by glowing away from large radiators, and every kilogram of radiator has to be launched. Weight per kilowatt, times the price of a launch, decides whether orbit can compete with a hall on the ground."
category: "Analysis"
cover: "/covers/data-centres-in-space.svg"
tags: ["cooling", "data-centres", "space", "power"]
updated: 2026-11-06
updateNote: "Now follows one watt from sunlight to deep space and tests whether a heat pump can shrink the radiator, with evidence to 6 November 2026."
draft: false
---

SpaceX has told American regulators it wants to put AI data centres into orbit. The Federal Communications Commission has accepted for review its application for up to one million satellites.

The pitch is power. In the right orbit the sun almost never sets, and there is no queue for the grid. But every watt a chip uses comes back out as heat, and a vacuum has no air or water to carry it.

So orbit is a contest of weight, because radiators and solar panels are launched, priced by the kilogram. My claim: by the end of 2028, nobody will report a compute satellite in service at SpaceX's own target for power per tonne launched, and no rocket company will publish a price low enough to make the sums easy.

In orbit the plug is free, and the heat is the bill.

"Cooling" is three jobs. Off the chip: heat moves from silicon into a liquid. Across the building: the liquid carries it to the edge. Out to the world: the heat is thrown away for good. On the ground, air and water do the last job cheaply; in orbit only light can.

The case runs in five steps. First, in a dawn-dusk orbit the panels see the sun almost all the time, so there is no night and no grid to queue for. Second, every watt the chips use comes back as heat, and in a vacuum heat leaves only as light from a radiator. Third, a radiator sheds heat with the fourth power of its absolute temperature, so how hot the coolant may run sets its size. SpaceX assumes 1,400 watts shed per square metre, which on my arithmetic means a panel near 67°C. Fourth, area becomes weight. SpaceX targets 100 kilowatts of computing per tonne launched, and radiators as heavy as the International Space Station's would use that whole budget alone. Fifth, weight becomes money. Google, designing its own orbital system, estimates today's launch price at about $3,600 a kilogram, and sees $200, where launch could stop being the limit, around 2035.

<details class="analogy">
<summary>The analogy</summary>
<p>Picture a laptop sealed in a vacuum flask on a sunny windowsill. The sunshine charges it for nothing: that is the solar array. The flask is the vacuum, which keeps tea hot and here traps the laptop's heat.</p>
<p>The only way out is a black fin poking through the lid, glowing the heat away: that is the radiator. A hotter fin can be smaller, so how hot the laptop may run sets the fin's size. And every fin goes up by courier, charged by the kilogram: that is the launch fare.</p>
</details>

Follow one watt from array to wires to chip to coolant to radiator, and the costly step stands out.

<figure class="chart">
<p class="chart-title">Only the last step has no air or water to help, and it sets the satellite's weight</p>
<p class="chart-sub">One watt on a SpaceX-style compute satellite, from sunlight to deep space</p>
<svg viewBox="0 0 560 196" role="img" aria-label="Diagram of five steps in order. One, sun: the solar array turns sunlight into electricity, about 250 watts per square metre on SpaceX's design figure. Two, bus: wires and converters step the voltage down, and their losses become heat. Three, chip: every watt of computing comes back out as heat. Four, loop: a pumped liquid carries the heat to the edge of the satellite. Five, radiator: a panel glows the heat into space as light, about 1,400 watts per square metre on SpaceX's figure, which needs a panel near 67°C. This is the choke point.">
<rect class="c-box" x="5.0" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="13.0" y="66">1. Sun</text>
<text class="c-note" x="13.0" y="88">Array turns</text>
<text class="c-note" x="13.0" y="106">sunlight into</text>
<text class="c-note" x="13.0" y="124">power, about</text>
<text class="c-note" x="13.0" y="142">250 W/m²</text>
<line class="c-arrow" x1="106.4" y1="97" x2="111.4" y2="97"/><polygon class="c-arrow-head" points="116.4,97 110.4,93 110.4,101"/>
<rect class="c-box" x="117.4" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="125.4" y="66">2. Bus</text>
<text class="c-note" x="125.4" y="88">Wires step</text>
<text class="c-note" x="125.4" y="106">the voltage</text>
<text class="c-note" x="125.4" y="124">down; losses</text>
<text class="c-note" x="125.4" y="142">become heat</text>
<line class="c-arrow" x1="218.8" y1="97" x2="223.8" y2="97"/><polygon class="c-arrow-head" points="228.8,97 222.8,93 222.8,101"/>
<rect class="c-box" x="229.8" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="237.8" y="66">3. Chip</text>
<text class="c-note" x="237.8" y="88">Every watt</text>
<text class="c-note" x="237.8" y="106">of compute</text>
<text class="c-note" x="237.8" y="124">comes back</text>
<text class="c-note" x="237.8" y="142">as heat</text>
<line class="c-arrow" x1="331.2" y1="97" x2="336.2" y2="97"/><polygon class="c-arrow-head" points="341.2,97 335.2,93 335.2,101"/>
<rect class="c-box" x="342.2" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="350.2" y="66">4. Loop</text>
<text class="c-note" x="350.2" y="88">Pumped liquid</text>
<text class="c-note" x="350.2" y="106">carries heat</text>
<text class="c-note" x="350.2" y="124">to the edge</text>
<text class="c-note" x="350.2" y="142">of the craft</text>
<line class="c-arrow" x1="443.6" y1="97" x2="448.6" y2="97"/><polygon class="c-arrow-head" points="453.6,97 447.6,93 447.6,101"/>
<rect class="c-zone" x="450.6" y="14" width="108.4" height="144" rx="4"/>
<text class="c-zone-t" x="504.8" y="30" text-anchor="middle">THE CHOKE POINT</text>
<rect class="c-box" x="454.6" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="462.6" y="66">5. Radiator</text>
<text class="c-note" x="462.6" y="88">Glows heat</text>
<text class="c-note" x="462.6" y="106">into space</text>
<text class="c-note" x="462.6" y="124">1,400 W/m²</text>
<text class="c-note" x="462.6" y="142">near 67°C</text>
<text class="c-lab c-s2t" x="555.0" y="180" text-anchor="end">Heat leaves only as light, and every m² is launched</text>
</svg>
<figcaption>SpaceX interview transcript filed with the SEC (9 June 2026) for 250 and 1,400 W/m²; the 67°C is my arithmetic. My framing of the chain.</figcaption>
</figure>

The last step binds. Solar arrays have flown for decades, and pumped loops work without gravity. Only the radiator loses the air and water it leans on down here, and every square metre of it is launched. It is the [same lever as warm water on the ground](/journal/heat-and-water/): the warmer the coolant, the smaller the panel.

In April American regulators asked SpaceX for its system's mass; it is still being refined. Orbit can still work, but no compute satellite has been weighed in public.

<hr class="layer">
<p class="layer-label">For investors</p>

## In orbit the power is nearly free, and the heat is the bill

<a id="data-centres-in-space"></a>

SpaceX, the rocket company planning AI compute satellites, sets a goal of 100 kilowatts of computing per tonne launched: 10 kg for each kW. At the radiator weight of the International Space Station, the crewed outpost whose radiators were designed decades ago, 14 kg per m², a radiator shedding SpaceX's assumed 1,400 W/m² uses all 10 kg on its own. At the 633 W/m² of Starcloud, a start-up with its own orbital plan, it needs about 22. Nobody has published what a compute satellite weighs, and the SEC, the US securities regulator, asked.

A fund should care because orbital gigawatts are being announced as computing to come, and the number that decides whether they arrive, mass per kilowatt, is the one missing. Until a satellite is weighed in service, orbital compute is a design, not capacity.

<figure class="chart">
<p class="chart-title">At the space station's weight, the radiator alone uses SpaceX's whole budget</p>
<p class="chart-sub">Kilograms launched per kilowatt</p>
<svg viewBox="0 0 560 280" role="img" aria-label="Bar chart in kilograms launched per kilowatt. SpaceX's target for a whole AI compute satellite is 10, from 100 kilowatts per metric ton. A radiator alone at the space station's areal density of 14 kilograms per square metre, shedding SpaceX's 1,400 watts per square metre, is 10. A whole Starlink V2 mini satellite is about 20.5, on Google's estimate. A radiator alone at station density shedding Starcloud's 633 watts per square metre is about 22.1. The station's own radiator wings as flown are about 96 kilograms per kilowatt, off the scale.">
<g class="c-grid">
<line x1="270" y1="14" x2="270" y2="228"/>
<line x1="320" y1="14" x2="320" y2="228"/>
<line x1="370" y1="14" x2="370" y2="228"/>
<line x1="420" y1="14" x2="420" y2="228"/>
<line x1="470" y1="14" x2="470" y2="228"/>
<line x1="520" y1="14" x2="520" y2="228"/>
</g>
<g class="c-axis"><text x="260" y="38" text-anchor="end">SpaceX target, whole satellite</text><text x="260" y="90" text-anchor="end">Radiator alone, ISS weight, at 1,400 W/m²</text><text x="260" y="142" text-anchor="end">Starlink V2 mini, whole satellite</text><text x="260" y="194" text-anchor="end">Radiator alone, ISS weight, at 633 W/m²</text><text x="270" y="246" text-anchor="middle">0</text><text x="320" y="246" text-anchor="middle">5</text><text x="370" y="246" text-anchor="middle">10</text><text x="420" y="246" text-anchor="middle">15</text><text x="470" y="246" text-anchor="middle">20</text><text x="520" y="246" text-anchor="middle">25</text></g>
<rect class="c-bar" x="270" y="18" width="100" height="30" rx="2"/>
<text class="c-lab c-s2t" x="378" y="38">10 kg</text>
<rect class="c-bar c-mute" x="270" y="70" width="100" height="30" rx="2"/>
<text class="c-lab c-s1t" x="378" y="90">10 kg</text>
<rect class="c-bar c-alt" x="270" y="122" width="205" height="30" rx="2"/>
<text class="c-lab c-s3t" x="483" y="142">20.5 kg</text>
<rect class="c-bar c-mute" x="270" y="174" width="221" height="30" rx="2"/>
<text class="c-lab c-s1t" x="499" y="194">22.1 kg</text>
<line class="c-today" x1="370" y1="14" x2="370" y2="228"/>
<line class="c-base" x1="270" y1="14" x2="270" y2="228"/>
<text class="c-note" x="270" y="268">ISS radiator wings as flown: about 96 kg per kW, off this scale</text>
</svg>
<figcaption>SpaceX prospectus (12 June 2026); Google, Suncatcher paper (22 November 2025); NASA, IEEE Aerospace 2022 lunar habitat paper (14 kg/m²); NASA ISS thermal control overview (six units of 1,122.64 kg for 70 kW). Radiator bars are my arithmetic and treat heat to reject as equal to compute power, which understates it.</figcaption>
</figure>

## Heat leaves only as light, so the radiator's temperature sets its size

SpaceX's final prospectus (12 June 2026), the filing for its share listing, says it plainly: "thermal control must be accomplished through radiation rather than convection and conduction." Starcloud's white paper (September 2024) nets 633 W/m² from a black plate at 20°C. Elon Musk, SpaceX's chief executive, puts SpaceX's figure at about 1,400 W/m², from two-sided radiators "knife edge to the sun". On my arithmetic, a shaded two-sided panel of emissivity 0.92 reaches that only near 67°C.

<figure class="chart">
<p class="chart-title">A radiator sheds heat with the fourth power of its temperature</p>
<p class="chart-sub">Heat radiated per square metre of a two-sided panel in shade, watts, by panel temperature</p>
<svg viewBox="0 0 560 275" role="img" aria-label="Line chart of heat radiated per square metre by a two-sided panel in shade with emissivity 0.92: about 581 watts at 0°C, 771 at 20°C, 1,069 at 45°C, 1,400 at about 67°C and 2,023 at 100°C. SpaceX assumes 1,400 watts per square metre, which implies about 67°C. Starcloud computes 633 watts per square metre at 20°C with sunlight on one face. The International Space Station's radiator wings reject about 147 watts per square metre as built, with an ammonia loop at about 3°C. A marker at 45°C shows the warm-water cooling class used on the ground.">
<g class="c-grid">
<line x1="60" y1="240" x2="520" y2="240"/>
<line x1="60" y1="190" x2="520" y2="190"/>
<line x1="60" y1="140" x2="520" y2="140"/>
<line x1="60" y1="90" x2="520" y2="90"/>
<line x1="60" y1="40" x2="520" y2="40"/>
</g>
<g class="c-axis">
<text x="52" y="244" text-anchor="end">0</text>
<text x="52" y="194" text-anchor="end">500</text>
<text x="52" y="144" text-anchor="end">1,000</text>
<text x="52" y="94" text-anchor="end">1,500</text>
<text x="52" y="44" text-anchor="end">2,000</text>
<text x="60" y="260" text-anchor="middle">0°C</text>
<text x="152" y="260" text-anchor="middle">20°C</text>
<text x="244" y="260" text-anchor="middle">40°C</text>
<text x="336" y="260" text-anchor="middle">60°C</text>
<text x="428" y="260" text-anchor="middle">80°C</text>
<text x="520" y="260" text-anchor="middle">100°C</text>
</g>
<line class="c-plant" x1="267" y1="30" x2="267" y2="240"/>
<text class="c-note" x="271" y="40">45°C: warm-water loop</text>
<text class="c-note" x="271" y="55">on the ground (W45)</text>
<polyline class="c-line c-s1" points="60,181.9 83,177.5 106,172.9 129,168.1 152,162.9 175,157.6 198,151.9 221,145.9 244,139.7 267,133.1 290,126.2 313,119 336,111.5 359,103.6 382,95.3 405,86.7 428,77.7 451,68.3 474,58.5 497,48.3 520,37.7"/>
<circle class="c-dot c-s2" cx="369.1" cy="100" r="5"/>
<text class="c-lab c-s2t" x="361.1" y="88" text-anchor="end">SpaceX: 1,400 W/m², about 67°C</text>
<circle class="c-dot c-s2" cx="152" cy="176.7" r="5"/>
<text class="c-lab c-s2t" x="162" y="196.7">Starcloud: 633 W/m² at 20°C, sun on one face</text>
<circle class="c-dot c-s3" cx="73.8" cy="225.3" r="5"/>
<text class="c-lab c-s3t" x="83.8" y="229.3">ISS wings as built: about 147 W/m², loop at 3°C</text>
<text class="c-lab c-s1t" x="516" y="55.7" text-anchor="end">ideal panel</text>
<line class="c-base" x1="60" y1="240" x2="520" y2="240"/>
</svg>
<figcaption>The curve is my arithmetic: two faces, emissivity 0.92, no sunlight or Earth glow, by the Stefan-Boltzmann law. Starcloud white paper (September 2024); SpaceX interview transcript filed with the SEC (9 June 2026); NASA ISS Active Thermal Control System overview (undated), my arithmetic from 70 kW over six radiator units. The coolant must run warmer than the panel.</figcaption>
</figure>

The sums fit on a napkin. A black surface at 27°C sheds about 460 W per square metre per face, and each 1% rise in absolute temperature sheds about 4% more. So 20°C to 67°C, about 16% hotter in kelvin, sheds about 1.8 times the heat. Area is heat divided by that flux: a 120 kW satellite needs about 86 m² of radiator at 1,400 W/m², a fifth of a basketball court, and about 190 m² at 633. The space station shows the other extreme: its ammonia loop runs at about 3°C to cool a crew, and on my arithmetic its main radiators reject about 147 W per square metre.

## Six things keep the radiator heavy, and a better chip changes none of them

A chip improves every year; a radiator obeys a law from 1879.

**One lever.** Radiated heat depends on area, emissivity and temperature. Good coatings already reach an emissivity of about 0.92, and area costs mass, which leaves temperature.

**The chip's ceiling.** The coolant cannot run hotter than the chip tolerates, and the panel runs cooler than the coolant, so the silicon caps the radiator.

**Sun and Earth shine back.** Sunlight on one face costs Starcloud's panel about 123 W/m² and the Earth's glow about 14, which is why designs fly the radiator edge-on to the sun.

**It must unfold.** Eighty-six square metres do not fit under a rocket's nose. Folding panels need hinges and flexible lines, and the station's radiator wings even rotate.

**Leaks and punctures.** A pumped loop over a large, thin panel is a large target; spare loops and armour are mass.

**No repair crew.** SpaceX's risk factors say its satellites' useful life "is inherently shorter" than that of the systems they host, so it "must periodically launch replacement satellites". Google's Suncatcher paper (arXiv, 22 November 2025), a research design for orbital computing, answers failing chips the same way: "The simplest solution is redundant provisioning."

## Gigawatts are announced, and kilograms are not

The filings count capacity. Starcloud's application of 4 February 2026 to the FCC, the US regulator of satellite radio, asks for up to 88,000 satellites; SpaceX's, accepted for filing that day, asks for up to one million. SpaceX's prospectus speaks of 100 gigawatts a year "via satellites carrying over 100 kilowatts of compute power per metric ton". Analysts read these like a utility's connection queue.

The mass is the number withheld. The SEC's comment letter of 24 April 2026 asked for the "power-to-mass ratios" behind the 100 gigawatt goal, and for "total system mass". The prospectus answered on design only, "substantially larger radiators"; on mass it says the figures "continue to be refined". Its 10-Q for the quarter to September, filed on 22 October, does not mention orbital compute.

## Four terms carry the argument

**Emissivity and the Stefan-Boltzmann law.** Heat radiated is emissivity times a constant times area times absolute temperature to the fourth power. Emissivity, from 0 to 1, is how well a surface glows; temperature is the volume knob.

**Dawn-dusk sun-synchronous orbit.** A polar orbit that rides the line between day and night, so the panels almost never see shade. Google's design uses it and Starcloud files for it. SpaceX's finance chief, Bret Johnsen, said cells there get "roughly five times, if not more" the energy they get on the ground.

**Kilograms per kilowatt.** Kilowatts per tonne turned upside down, as litres per 100 km is to miles per gallon: 100 kW per tonne is 100 W/kg, or 10 kg per kW.

**Total dose and single events.** Dose, in rad(Si), builds up and wears a chip out, like sunburn. A single event is one particle flipping a bit now, like a stray hailstone, and risks a silent wrong answer.

## Radiation, latency and bandwidth are real, but none binds first

Google's ground test says radiation dose is not the gate. Its Trillium TPU, Google's own AI chip, showed memory irregularities in a proton beam only after 2 krad(Si), almost three times the 750 rad(Si) a shielded five-year mission expects. The open risk is silent errors, which Google's paper puts "on the order of 1 per 3 million inferences"; their effect on training "requires further study".

The distance is short and the wait is not. At 650 km light takes about 2 milliseconds each way, on my arithmetic, but a satellite passes over a ground station for minutes, so constant service needs laser relays.

Bandwidth to the ground is the narrow lane. Google's design needs links between satellites "on the order of 10 Tbps", while the ground record it cites is NASA's TBIRD mission, "demonstrating 200Gbps ground-LEO communications in 2023". Orbit suits inference, where an answer is a few kilobytes, not moving training data.

Each costs some redundancy or a relay; the radiator costs mass on every kilowatt of every launch.

## Ten kilograms per kilowatt is a heritage ceiling set against a whole-satellite budget

The number is built from heat, flux and weight. One kW of heat at SpaceX's 1,400 W/m² needs 0.714 m² of radiator, and at the station's 14 kg/m² that is 10.0 kg; at Starcloud's 633 W/m² it is 1.58 m² and 22.1 kg. Musk's draft first satellite, 120 kW sustained, about one rack of GB300 chips from Nvidia, the leading AI chip designer, can therefore weigh no more than about 1.2 tonnes in all, with 480 m² of solar array.

The 10 kg is the budget for the whole satellite, chips, solar, structure and radiator, and the stated designs fall short of it. SpaceX's web page for AI1, its first AI satellite, gives "75 kW / ton", a quarter short if read as compute per tonne launched. Johnsen's "About 5 megawatts per launch", at the 100 tonnes a launch SpaceX targets for Starship, its next, larger rocket, is 50 kW per tonne. A Starlink V2 mini, one of SpaceX's internet satellites and Google's best proxy, is about 20.5 kg per kW.

The trap is reading the station figure as a law. Its wings, about 96 kg per kW as flown, were built for a crew with a cold loop and rotating joints, so 14 kg per m² is a heritage ceiling; a purpose-built panel can be lighter. The target needs radiators several times lighter per square metre than the station's, or hotter than 67°C, or both, and no filing I read says which.

Kilograms become a bill at the launch fare. Google's "launched power price" spreads launch cost over the satellite's life. At $3,600/kg, "based on Falcon 9 (reusable configuration)", SpaceX's working rocket, and a five-year life, a Starlink-class satellite comes to $14,700 per kW per year. An American AI hall's power bill, on Google's range of power prices and PUE (total power over power reaching the computers), is $570 to $3,000.

<figure class="chart">
<p class="chart-title">At today's launch price, power in orbit costs several times a ground hall's power bill</p>
<p class="chart-sub">Launch cost per kilowatt per year for a Starlink-class satellite, against the power bill of a US AI hall, US dollars</p>
<svg viewBox="0 0 560 200" role="img" aria-label="Bar chart in US dollars per kilowatt per year. A Starlink-class satellite launched at 3,600 dollars a kilogram costs 14,700 dollars per kilowatt per year over a five-year life. At 200 dollars a kilogram it costs 810. A US AI data centre's power bill is 570 to 3,000 dollars per kilowatt per year.">
<g class="c-axis"><text x="230" y="44" text-anchor="end">Starlink-class, at $3,600/kg</text><text x="230" y="98" text-anchor="end">Same satellite, at $200/kg</text><text x="230" y="152" text-anchor="end">US ground hall power bill</text></g>
<rect class="c-bar c-mute" x="240" y="24" width="257.2" height="30" rx="2"/>
<text class="c-lab c-s1t" x="505.2" y="44" text-anchor="start">$14,700</text>
<rect class="c-bar c-alt" x="240" y="78" width="14.2" height="30" rx="2"/>
<text class="c-lab c-s3t" x="262.2" y="98">$810</text>
<rect class="c-bar" x="250" y="132" width="42.5" height="30" rx="2"/>
<text class="c-lab c-s2t" x="300.5" y="152">$570 to $3,000</text>
<line class="c-base" x1="240" y1="16" x2="240" y2="172"/>
<g class="c-axis"><text x="240" y="190" text-anchor="middle">0</text><text x="327.5" y="190" text-anchor="middle">5k</text><text x="415" y="190" text-anchor="middle">10k</text><text x="502.5" y="190" text-anchor="middle">15k</text></g>
</svg>
<figcaption>Google, Suncatcher paper (22 November 2025), Table 1 and text. The $3,600 per kilogram is Google's estimate for Falcon 9, not a published price; the ground range is Google's, from reported power prices and PUE. Launch cost only: chips, solar arrays and the satellite itself are excluded on both sides.</figcaption>
</figure>

At $200/kg, the figure Google says "is often cited, by SpaceX and others" as where launch stops being the limiting cost, the same satellite falls to $810, inside the ground range; Google projects that price around 2035. And the fare recurs: on the ground the hall and its [grid gear outlast three or four chip generations](/journal/the-equipment-queue/), while a satellite flown in 2027 on a five-year life wears out before that.

## The launcher is paid on every kilogram, and the ground plug keeps its value

If the heat is the bill, value sits where kilograms are charged. SpaceX flies the rockets every orbital builder needs and is paid per kilogram whoever's satellite goes up, so heavier radiators mean more launches. It also designs its own compute satellite, which makes it toll keeper and competitor at once.

The builders carry the weight risk. Starcloud builds compute satellites, and Planet, the satellite imaging company, co-developed Google's prototype. A lighter radiator is their whole edge, and its weight is unpublished.

The plug on the ground is the quiet side of the trade. What pushes builders up is the [American plug queue](/journal/america-rations-the-plug/). While orbit stays heavy, AI stays on the ground and the queue keeps its value. SpaceX's own risk factors warn that if "advances in nuclear energy" or similar "alleviate infrastructure constraints", the viability of its orbital compute "may be materially diminished".

## What would prove me wrong

Two observations break the claim. An operator discloses, in a filing, a release or a regulator's record, an AI compute satellite in service at 100 kW or more of compute power per tonne launched, by 31 December 2028. Or a launch provider publishes a price to low Earth orbit of $200 per kilogram or less by then.

The satellites that could be weighed against the target fly in 2027. Gwynne Shotwell, SpaceX's president, said on its call of 20 October that it will begin flying Starmind, its first compute satellites, in 2027, and Planet is contracted to deploy two Suncatcher prototypes, "targeting launch in 2027". A satellite mass in SpaceX's reports, a published mass for Google's 2027 pair, or a published price would move me sooner. The early warning would be a flown radiator measured several times lighter per square metre than the station's, or one running near 100°C.

Designs and assumptions would not move me. A preprint (Gaalema, Indyk and Staley, arXiv, 9 April 2026; not peer reviewed) argues integrated panels could reach "about 500 W/kg", or 2 kg per kW. It assumes "custom solutions for all components". SpaceX calls its 1,400 W/m² a very achievable goal. Neither is a satellite in service.

The claim stands on two legs. The first, that the radiator is heavy, rests on physics that money cannot change; a weighed satellite at target or a measured light radiator attacks it. The second, that the fare is high, rests on a price that reuse can move fast; a published $200 attacks it. The legs multiply: launched power price is kilograms per kilowatt times the fare, over the years of life. Halve either and the bill halves, so the strongest case against me is both falling together.

Musk said in an interview SpaceX filed with the SEC that "cooling is actually much easier in space than it is on Earth", and I disagree. Off the chip, perhaps: there is no dust or humidity. Out to the world, heat can leave only as light, at a few hundred to about 1,400 W/m², and every square metre is launched.

## Google's first chip in orbit already runs to a heat budget

Google and Planet launched a Suncatcher prototype on a SpaceX rideshare on 1 October 2026. NPR, the American public broadcaster, reported the next day that it carries four of Google's TPU chips and runs Gemma, Google's open model, "15 minutes at a time due to heat management constraints". Travis Beals, who leads the project, told NPR the radiators are "one of the heaviest components". On 30 October Google said the satellite had sent down its first answer, over Svalbard, with thermal and radiation tests still to come.

I concede the timing: a data-centre-class chip reached orbit months before the satellites this claim looks to, and its first published limit is heat. But a chip running minutes at a time is a first test, not 100 kW per tonne, with no mass and no thermal results published. The first real weighing would be the 2027 pair.

## A launch seat may bind before the fare

Philip Johnston, Starcloud's chief executive, told TechCrunch, the technology news site, on 21 August 2026 that launch "is pretty constrained right now" because Falcon 9 "is scheduled to end in 2028"; I found no such date in SpaceX's filings. The same report has Starcloud's next two satellites, of 8 kW each, on rideshares in 2027.

I concede the frame: this piece prices launch per kilogram, and for some years it may be a queue instead, the plug problem moved to the launch pad. But scarce seats make a published $200 a kilogram less likely by 2028, not more. What changes is who gets paid: if one company owns the only big rocket and a compute satellite of its own, its satellites fly first, and orbit looks less like a market than one firm's private grid.

<a id="heat-pump-trade"></a>
## A heat pump cannot buy back the radiator, because solar is the weaker surface

The obvious fix for a big radiator is a heat pump, and the hypothesis I am testing is that it costs more surface than it saves. Starcloud's white paper says pumps that raise the radiator's temperature lift its output "due to the T4 term", "albeit at an added energy cost". That energy comes from the array. On Musk's figures the array collects about 250 W per square metre, against about 1,400 shed by the radiator.

On my arithmetic, an estimate, lifting 1 kW of heat from a 45°C loop to a 100°C panel at half the ideal efficiency takes about 0.35 kW of work. The hotter two-sided panel, shedding about 2,023 W/m² instead of 1,069, saves about 0.27 m² of radiator, net of the pump's own heat. The extra power needs about 1.4 m² of array. Even a perfect pump adds about twice the area it saves.

If that holds, the radiator's size is a chip-design decision. It is a seed, not a finding, because launch bills kilograms, not square metres. The test is published mass per square metre for flown arrays and radiators: if thin arrays weigh under about a fifth as much as radiators, a pump still saves mass and the idea dies, and a panel that is array and radiator at once would change the sums.

## At every scale the heat is paid for in launches

At the scale of the chip, the temperature it tolerates sets the radiator by the fourth power, so a chip's temperature rating is an orbital cost number.

At the scale of the satellite, a heritage radiator alone uses the whole 10 kg per kW.

At the scale of the fleet, 100 gigawatts a year needs about one million tonnes to orbit, the prospectus says, or about 10,000 Starship flights at 100 tonnes each on my arithmetic. In orbit the heat is paid for in square metres, then kilograms, then launches, and at fleet scale the launch pad binds.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

The test this piece stands behind, quoted word for word:

**In orbit the plug is free and the heat is the bill** (2 November 2026)

Claim: "In orbit the power is nearly free and the heat is the bill: by 31 December 2028 no operator will report an AI compute satellite in service at SpaceX's own target of 100 kilowatts of compute power per metric ton launched, and no launch provider will publish a price to low Earth orbit at or below Google's $200 per kilogram threshold."

Breaks if: "By 31 December 2028, SpaceX, Starcloud, Google or any other operator discloses in a filing, release or regulator's record an orbital AI compute satellite in service at 100 kilowatts or more of compute power per metric ton of launched mass, or a launch provider publishes a list or contract price to low Earth orbit of $200 per kilogram or less."

This piece absorbs no earlier piece, so it carries no older claims.

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

The radiator physics:

| Measure | Figure | Source |
|---|---|---|
| Plate at 20°C, emissivity 0.92, two faces | 770.48 W/m² emitted; 633.08 W/m² net after 122.94 W/m² of sunlight (absorptivity 0.09) and 14.46 W/m² from the Earth | Starcloud (then Lumen Orbit) white paper, September 2024 |
| SpaceX's design assumptions | Solar 250 W/m²; radiators "about 1,400" W/m², double-sided, "knife edge to the sun"; 150 kW peak, 120 kW sustained | Interview transcript, FWP filed 9 June 2026 |
| Panel temperature for 1,400 W/m² | About 340 K, 67°C (68°C allowing for the Earth's glow) | My arithmetic: two faces, emissivity 0.92 |
| ISS main radiators | 70 kW for two loops; six units, each 23.3 m by 3.4 m and 1,122.64 kg; ammonia supply 37°F | NASA ISS Active Thermal Control System overview, undated |
| ISS, derived | 6,736 kg for 70 kW, about 96 kg per kW; 475 m², about 147 W/m² and 14.2 kg/m² | My arithmetic |
| ISS areal density used by NASA | 14 kg/m² | Schunk, Babiak and others, IEEE Aerospace 2022 (NTRS 20210026557) |

The curve in the first chart is 2 × 0.92 × 5.67 × 10⁻⁸ × T⁴, with T in kelvin: 581 W/m² at 0°C, 771 at 20°C, 1,069 at 45°C, 1,400 at 67.2°C and 2,023 at 100°C. The ISS point is total capacity over planform area at design, not a measured flux.

Mass per kilowatt:

| Measure | Figure | Source |
|---|---|---|
| SpaceX target | "over 100 kilowatts of compute power per metric ton"; 100 GW a year needs "approximately one million metric tons to orbit annually" | Prospectus (424B4), 12 June 2026, about p. 153; S-1/A No. 2, 3 June 2026 |
| SpaceX first generation | "About 5 megawatts per launch"; "roughly 200 launches for every gigawatt" | Johnsen, transcript filed 9 June 2026 |
| SpaceX first flights | "we'll begin flying Mobile V2 and Starmind satellites in 2027" | Shotwell, third-quarter call, 20 October 2026 (ir.spacex.com transcript) |
| AI1 design figure | "75 kW / ton" vehicle efficiency; basis not stated | SpaceX AI1 web page, read 2 November 2026 |
| Starship capacity | "100 Metric tons per launch over time" | Roadshow slides, FWP filed 4 June 2026 |
| Starlink V2 mini | 575 kg; about 28 kW, Google's estimate from about 105 m² of array | Google, Suncatcher paper, 22 November 2025 |
| Radiator at 14 kg/m² | 22.1 kg per kW at 633 W/m²; 10.0 at 1,400 W/m² | My arithmetic |

The 50 kW per tonne for the first generation is my arithmetic, 5 MW over 100 tonnes; if the first launches carry less mass, the figure is higher. A 120 kW satellite at 1,400 W/m² needs about 86 m² of radiator, about 1.2 tonnes at station density, and about 480 m² of solar at 250 W/m².

Launch price:

| Measure | Figure | Source |
|---|---|---|
| Current price used | $3,600/kg, Falcon 9 reusable, Google's estimate | Google, Suncatcher paper |
| Threshold | $200/kg, "often cited, by SpaceX and others" | same |
| Launched power price, Starlink V2 mini, five years | $14,700 per kW per year at $3,600/kg; $810 at $200/kg | same, Table 1 |
| Other satellites at $3,600/kg | Starlink V1 $26,600; OneWeb $135,800; Iridium $124,600 per kW per year | same, Table 1 |
| US AI hall power | $0.06 to $0.25 per kWh, PUE 1.09 to 1.4: $570 to $3,000 per kW per year | same |
| Projection | Below $200/kg by about 2035 at a learning rate near 20%, about 180 Starship launches a year | same |
| Starcloud's assumption | About $5 million a launch long term, about $30/kg | Starcloud white paper, September 2024 |

The SEC record:

| Document | What it says | Date |
|---|---|---|
| Staff comment 26 | Asks for "power-to-mass ratios" and "total estimated solar collection area, total system mass, and on-orbit assembly requirements" | 24 April 2026 |
| Staff comment 31 | Asks for "the material differences between connectivity satellites and AI compute satellites" | 24 April 2026 |
| Staff comment 3 | Asks SpaceX to "clarify when you may potentially begin deploying AI compute satellites" | 19 May 2026 |
| Prospectus | Mass per satellite "continue[s] to be refined"; "substantially larger radiators"; deployment "as early as 2028" | 424B4, 12 June 2026 |
| 10-Q | No mention of orbital compute | Quarter to 30 September 2026, filed 22 October 2026 |

The first prototype and the launch seat:

| Measure | Figure | Source |
|---|---|---|
| Suncatcher prototype | Co-developed with Planet; Transporter-18 rideshare with SpaceX; next, two satellites in 2027 to test laser links | Google blog, 24 September 2026 |
| Launch and first answer | Launched 1 October; Gemma answer downlinked over Svalbard; thermal and radiation tests next; "twin interconnected satellites in 2027"; no mass given | Google blog, 30 October 2026 |
| Run time | Four TPUs; Gemma "15 minutes at a time due to heat management constraints"; radiators "one of the heaviest components" | NPR, 2 October 2026 (press report) |
| Launch seats | Falcon 9 "scheduled to end in 2028"; Starcloud's two 8 kW satellites on rideshares in 2027 | Starcloud's chief executive, TechCrunch, 21 August 2026 (press report) |

The heat pump arithmetic is mine and an estimate: loop at 45°C (318 K), panel at 100°C (373 K), the panel taken at loop temperature in both cases. Ideal work per unit of heat lifted is (373 minus 318) / 318 = 0.173; at half of ideal, about 0.35. Without a pump, 1 kW at 1,069 W/m² needs 0.94 m²; with one, 1.35 kW at 2,023 W/m² needs 0.67 m², a saving of 0.27 m². The pump's 0.35 kW at 250 W/m² of array needs 1.4 m². With an ideal pump the saving is 0.36 m² against 0.69 m² of array. Sunlight on the radiator is ignored, as for a panel flown edge-on.


</details>

<section class="exposure">
<h3>Who is exposed if the heat is the bill in orbit</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures and published estimates used as evidence for the mechanism.</p>
<dl>
<dt>The orbital compute builders</dt>
<dd><span class="names">SpaceX</span> builds rockets and satellites and is designing an AI compute satellite. <span class="names">Starcloud</span> builds compute satellites.</dd>
<dt>The chips</dt>
<dd><span class="names">Google</span> designs the TPU chips its Suncatcher prototypes would carry. <span class="names">Nvidia</span> makes the GB300 and Rubin chips in SpaceX's reference design.</dd>
<dt>The satellite maker</dt>
<dd><span class="names">Planet Labs</span> builds satellites, including Google's Suncatcher prototypes.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone counting orbital gigawatts announced as compute to come, and designs that rest on radiators lighter than any yet flown at this scale.</dd>
</dl>
</section>

---

<p class="sources">Sources: Google, "Towards a future space-based, highly scalable AI infrastructure system design" (arXiv 2511.19468, 22 November 2025); SpaceX's SEC record: roadshow free writing prospectus (4 June 2026), interview transcripts (9 June 2026), S-1/A No. 2 (3 June 2026), final prospectus (12 June 2026), SEC staff comment letters (24 April and 19 May 2026) and 10-Q for the quarter to 30 September 2026 (22 October 2026); SpaceX's third-quarter call transcript (20 October 2026) and its AI1 web page (read 2 November 2026); FCC public notice DA 26-113 (4 February 2026) and Starcloud's FCC application narrative (4 February 2026); Starcloud (Lumen Orbit) white paper, version 1.03 (September 2024); NASA's ISS Active Thermal Control System overview and Schunk and others, IEEE Aerospace 2022; Planet Labs' 8-K (10 December 2025); Google's Suncatcher blog posts (24 September and 30 October 2026); NPR (2 October 2026) and TechCrunch (21 August 2026), as press reports; Gaalema, Indyk and Staley (arXiv 2604.07760, 9 April 2026). Figures as stated on the dates cited. Personal research, not investment advice.</p>
