---
title: "Data centres in orbit: the plug is free and the heat is the bill"
date: 2026-11-02T16:55:31+08:00
summary: "SpaceX, Google and a start-up called Starcloud plan AI data centres in orbit, where the sun almost never sets and nobody queues for the grid. But in a vacuum heat can leave only by glowing away from large radiators, and every kilogram of radiator has to be launched. Weight per kilowatt, times the price of a launch, decides whether orbit can compete with a hall on the ground."
category: "Analysis"
cover: "/covers/data-centres-in-space.svg"
tags: ["cooling", "data-centres", "space", "power"]
draft: false
---

SpaceX has told American regulators it wants to put AI data centres into orbit. The Federal Communications Commission has accepted its application for up to one million satellites for review.

The pitch is power. In the right orbit the sun almost never sets, and there is no queue for the grid. But every watt a chip uses comes back out as heat, and in a vacuum there is no air or water to carry it away. Heat can leave only by glowing off a radiator, a panel that faces cold space.

So orbit is a contest of weight, because radiators and solar panels must be launched and launch is priced by the kilogram. My claim: by the end of 2028, nobody will report a compute satellite in service at SpaceX's own target for power per tonne launched, and no rocket company will publish a price low enough to make the sums easy.

In orbit the plug is free, and the heat is the bill.

<details class="analogy">
<summary>The analogy</summary>
<p>Picture a laptop sealed inside a vacuum flask on a sunny windowsill. The sun charges it for nothing, but the flask that keeps tea hot also traps the laptop's heat.</p>
<p>The only way out is a large black fin poking out of the flask, glowing the heat away. A hotter fin can be smaller. And every fin goes up by courier, charged by the kilogram.</p>
</details>

The orbit these plans favour is called dawn-dusk sun-synchronous. The satellite rides the line between day and night, so its panels face the sun almost all the time. SpaceX's finance chief says a solar cell there gets about five times the energy it would on the ground.

The radiator is the hard part. The heat a panel sheds rises with its temperature to the fourth power, so a slightly hotter panel sheds far more. Starcloud, a start-up, works out about 633 watts per square metre for a panel at 20°C with the sun on one face. SpaceX assumes 1,400, which on my arithmetic means a panel near 67°C.

That is the same lever as on the ground. [Warm coolant lets a hall stop using water](/journal/heat-and-water/); in orbit, warm coolant shrinks the radiator.

Weight is where the sums turn. SpaceX targets 100 kilowatts of computing for every tonne it launches. Radiators as heavy for their size as the International Space Station's, even at SpaceX's 1,400, would use that whole budget alone, before a single chip or solar panel.

The regulator noticed. In April the Securities and Exchange Commission asked SpaceX to disclose the total mass of its system. The final prospectus said the mass of each satellite was still being refined.

Then there is the fare. Google, which is designing its own orbital system, estimates today's launch price at about $3,600 a kilogram. At that price its own sums put power in orbit at several times what an American hall pays for electricity.

Google cites $200 a kilogram as the point where launch could stop being the limit, and sees prices reaching it around 2035 if rockets keep getting cheaper at their past pace.

Orbit can still work. The free plug is simply paid for in kilograms, and no compute satellite in service has yet been weighed.

<hr class="layer">
<p class="layer-label">For investors</p>

## In orbit the power is nearly free, and the heat is the bill

<a id="data-centres-in-space"></a>

SpaceX, the rocket company planning AI compute satellites, sets a goal of 100 kilowatts of computing per tonne launched: 10 kg for each kW. At the radiator weight of the International Space Station, whose radiators were designed decades ago, 14 kg per m², a radiator shedding SpaceX's assumed 1,400 W/m² uses all 10 kg on its own. At the 633 W/m² of Starcloud, a start-up with its own orbital plan, it needs about 22. Nobody has published what a compute satellite weighs, and the SEC, the US securities regulator, asked.

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

## The sun has no queue, which is why the designs go up

Power is the reason to go up at all, so the designs converge on one orbit that nearly removes the night. Google's Suncatcher paper (arXiv, 22 November 2025), a research design for orbital computing, puts its satellites in "dawn-dusk, sun-synchronous low-Earth orbit". Starcloud's application of 4 February 2026 to the FCC, the US regulator of satellite radio, asks for up to 88,000 satellites on the same dawn-dusk line. SpaceX's, accepted for filing that day, asks for up to one million, between 500 and 2,000 km. SpaceX's finance chief, Bret Johnsen, said cells there get "roughly five times, if not more, energy per cell than they get terrestrially".

What pushes them up is the [American plug queue](/journal/america-rations-the-plug/). Starcloud's filing says the buildout of terrestrial energy in the western world "has not kept pace with the demand for AI". SpaceX's risk factors warn that if "advances in nuclear energy" or similar "alleviate infrastructure constraints", the viability of its orbital compute "may be materially diminished".

## Heat leaves only as light, so the radiator's temperature sets its size

Free power still has to leave as heat, and SpaceX's final prospectus (12 June 2026), the filing for its share listing, says it plainly: "thermal control must be accomplished through radiation rather than convection and conduction." Heat shed rises with absolute temperature to the fourth power. Starcloud's white paper (September 2024) nets 633 W/m² from a black plate at 20°C. Elon Musk, SpaceX's chief executive, puts SpaceX's figure at about 1,400 W/m², from two-sided radiators "knife edge to the sun". On my arithmetic, a shaded two-sided panel of emissivity 0.92 reaches that only near 67°C.

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

That gap is large because of the fourth power. Going from 20°C to 67°C raises absolute temperature by about 16%, but sheds about 1.8 times the heat per square metre. It is the lever [Heat and water](/journal/heat-and-water/) found on the ground, where a warm loop lets a dry cooler replace a cooling tower. In orbit, the warmer the coolant the chips accept, the smaller the radiator. The space station shows the other extreme: its ammonia loop runs at about 3°C because it cools a crew, and on my arithmetic its six main radiator units reject about 147 W per square metre.

## Every kilogram is a launch bill, and no design yet meets 10 kg per kW

Radiator area becomes weight, and weight is what launch charges for. SpaceX's prospectus says 100 gigawatts a year "via satellites carrying over 100 kilowatts of compute power per metric ton" needs "approximately one million metric tons to orbit annually". Musk's draft first satellite is 120 kW sustained, about one rack of Nvidia GB300 chips. On my arithmetic, that needs about 86 m² of radiator at 1,400 W/m² and about 480 m² of solar array. At 10 kg per kW, the whole satellite could weigh no more than about 1.2 tonnes.

The stated designs fall short. SpaceX's web page for AI1, its first AI satellite, gives "75 kW / ton", a quarter short of the target if read as compute per tonne launched. Johnsen's "About 5 megawatts per launch", at the 100 tonnes a launch SpaceX targets over time, is 50 kW per tonne, half the goal. Google's best proxy, a Starlink V2 mini, one of SpaceX's internet satellites, is about 20.5 kg per kW on my arithmetic, twice the target for a satellite that would also carry the chips.

## The regulator asked for the mass, and the prospectus does not give it

If the designs are short of the target, the mass is the number that matters, and the SEC's comment letter of 24 April 2026 asked for the "power-to-mass ratios" behind the 100 gigawatt goal, and for "total system mass". The final prospectus (424B4, 12 June 2026) answered on design only: "substantially larger radiators", and about "five times the solar array output compared to V3 satellite designs". On mass it says the figures "continue to be refined". Its next quarterly report, the 10-Q for the quarter to 30 September 2026, filed on 22 October, does not mention orbital compute at all.

Heritage hardware shows why the missing number matters. The station's own wings are six units of 1,122.64 kg each for 70 kW, about 96 kg per kW. The target needs radiators several times lighter per square metre than the station's, or run hotter than 67°C, or both. No filing I read says which.

## At today's launch price, orbital power costs several times a ground hall's

Every kilogram also has a fare. Google's "launched power price" spreads launch cost over the satellite's life. At $3,600/kg, "based on Falcon 9 (reusable configuration)", SpaceX's working rocket, and a five-year life, a Starlink-class satellite comes to $14,700 per kW per year. An American AI hall's power bill, on Google's range of power prices and PUE (total power over power reaching the computers), is $570 to $3,000 per kW per year.

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

At $200/kg, the figure Google says "is often cited, by SpaceX and others" as the point where launch stops being the limiting cost, the same satellite falls to $810, inside the ground range. Google projects prices could fall below it by about 2035 if SpaceX's learning rate holds, which it says would take about 180 launches a year of Starship, SpaceX's next, larger rocket. I found no launch provider's published price per kilogram for a whole rocket to low Earth orbit; the $3,600 is Google's estimate.

The fare is not paid once, because the short life turns the launch bill into rent. SpaceX's risk factors say its satellites' useful life "is inherently shorter" than that of the systems they host, so it "must periodically launch replacement satellites". On the ground, the hall and its [grid gear outlast three or four chip generations](/journal/the-equipment-queue/). SpaceX says Starmind, its first compute satellites, fly in 2027. On the five-year life Google uses, one flown then would wear out around 2032, before Google's curve reaches $200 a kilogram.

<figure class="chart">
<p class="chart-title">On Google's numbers, a compute satellite launched in 2027 wears out before launch reaches $200 a kilogram</p>
<p class="chart-sub">Dated plans for orbital compute, a five-year satellite life, and Google's projection for launch prices</p>
<svg viewBox="0 0 560 225" role="img" aria-label="Timeline from 2025 to 2037. Google and Planet target two Suncatcher prototypes for launch in 2027. SpaceX says its first AI compute satellites fly in 2027; on a five-year life they wear out around 2032. This piece's claim is tested on 31 December 2028. Google's learning curve reaches launch prices below 200 dollars a kilogram around 2035.">
<g class="c-grid">
<line x1="130" y1="30" x2="130" y2="196"/>
<line x1="164" y1="30" x2="164" y2="196"/>
<line x1="198" y1="30" x2="198" y2="196"/>
<line x1="232" y1="30" x2="232" y2="196"/>
<line x1="266" y1="30" x2="266" y2="196"/>
<line x1="300" y1="30" x2="300" y2="196"/>
<line x1="334" y1="30" x2="334" y2="196"/>
<line x1="368" y1="30" x2="368" y2="196"/>
<line x1="402" y1="30" x2="402" y2="196"/>
<line x1="436" y1="30" x2="436" y2="196"/>
<line x1="470" y1="30" x2="470" y2="196"/>
<line x1="504" y1="30" x2="504" y2="196"/>
<line x1="538" y1="30" x2="538" y2="196"/>
</g>
<g class="c-axis"><text x="130" y="214" text-anchor="middle">2025</text><text x="198" y="214" text-anchor="middle">2027</text><text x="266" y="214" text-anchor="middle">2029</text><text x="334" y="214" text-anchor="middle">2031</text><text x="402" y="214" text-anchor="middle">2033</text><text x="470" y="214" text-anchor="middle">2035</text><text x="538" y="214" text-anchor="middle">2037</text><text x="120" y="60" text-anchor="end">Google and Planet</text><text x="120" y="104" text-anchor="end">SpaceX AI satellite</text><text x="120" y="148" text-anchor="end">This claim</text><text x="120" y="188" text-anchor="end">Launch at $200/kg</text></g>
<line class="c-today" x1="192.4" y1="24" x2="192.4" y2="196"/><text class="c-today-t" x="192.4" y="20" text-anchor="middle">today</text>
<circle class="c-dot c-s3" cx="215" cy="56" r="5"/><text class="c-lab c-s3t" x="225" y="60">two prototypes, 2027</text>
<g class="c-span"><line x1="198" y1="100" x2="368" y2="100"/></g><g class="c-start"><circle cx="198" cy="100" r="4"/></g><g class="c-end"><circle cx="368" cy="100" r="4.5"/></g><g class="c-endt"><text x="377" y="104">worn out, about 2032</text></g>
<text class="c-note" x="198" y="88">first flights in 2027, five-year life</text>
<circle class="c-dot c-s2" cx="266" cy="144" r="5"/><text class="c-lab c-s2t" x="276" y="148">31 December 2028</text>
<circle class="c-dot c-s1" cx="470" cy="184" r="5"/><text class="c-lab c-s1t" x="460" y="188" text-anchor="end">Google's curve: about 2035</text>
</svg>
<figcaption>Planet 8-K (10 December 2025); SpaceX third-quarter call transcript (20 October 2026); Google, Suncatcher paper (22 November 2025), five-year life for Starlink and the 2035 projection, which assumes about 180 Starship launches a year. My framing; SpaceX has not stated an AI satellite's life.</figcaption>
</figure>

## What would prove me wrong

Two observations break the claim. An operator discloses, in a filing, a release or a regulator's record, an AI compute satellite in service at 100 kW or more of compute power per tonne launched, by 31 December 2028. Or a launch provider publishes a price to low Earth orbit of $200 per kilogram or less by then.

The first weighings come in 2027. Planet, the satellite imaging company, is contracted to deploy two Suncatcher prototypes, "targeting launch in 2027", and Gwynne Shotwell, SpaceX's president, said on its call of 20 October that it will begin flying Starmind satellites in 2027. A satellite mass in SpaceX's quarterly or annual reports, or a published price sheet or contract, would move me before the test date.

The case against my claim rests on designs and tests, and those would not move me. The station's radiators were designed decades ago for a crew, with a cold loop and rotating joints, so 14 kg per m² is a heritage ceiling, not a law. A preprint (Gaalema, Indyk and Staley, arXiv, 9 April 2026; not peer reviewed) argues integrated panels could reach "about 500 W/kg", or 2 kg per kW. Its 16 MW, 150 tonne satellite would just beat SpaceX's target, at about 107 kW per tonne, though it assumes "custom solutions for all components". Google's Trillium TPU showed memory irregularities in a proton beam only after 2 krad(Si), almost three times the 750 rad(Si) a shielded five-year mission expects. SpaceX calls its 1,400 W/m² a very achievable goal. The preprint is a design, Google's result is a ground test and SpaceX's figure is an assumption. The claim asks for a satellite in service at the target, or a published price, and on 2 November 2026 neither exists.

The ground-side mechanisms it leans on are in [Heat and water](/journal/heat-and-water/) and [America rations the plug](/journal/america-rations-the-plug/).

<details class="claims-record">
<summary>The claims on record, word for word</summary>

The test this piece stands behind, quoted word for word from the claims page:

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
<dd><span class="names">Planet Labs</span> builds satellites, including the two Suncatcher prototypes.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone counting orbital gigawatts announced as compute to come, and designs that rest on radiators lighter than any yet flown at this scale.</dd>
</dl>
</section>

---

<p class="sources">Sources: Google, "Towards a future space-based, highly scalable AI infrastructure system design" (arXiv 2511.19468, 22 November 2025); SpaceX's SEC record: roadshow free writing prospectus (4 June 2026), interview transcripts (9 June 2026), S-1/A No. 2 (3 June 2026), final prospectus (12 June 2026), SEC staff comment letters (24 April and 19 May 2026) and 10-Q for the quarter to 30 September 2026 (22 October 2026); SpaceX's third-quarter call transcript (20 October 2026) and its AI1 web page (read 2 November 2026); FCC public notice DA 26-113 (4 February 2026) and Starcloud's FCC application narrative (4 February 2026); Starcloud (Lumen Orbit) white paper, version 1.03 (September 2024); NASA's ISS Active Thermal Control System overview and Schunk and others, IEEE Aerospace 2022; Planet Labs' 8-K (10 December 2025); Gaalema, Indyk and Staley (arXiv 2604.07760, 9 April 2026). Figures as stated on the dates cited. Personal research, not investment advice.</p>
