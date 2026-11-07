---
title: "Data centres in orbit: the sunlight is free and the kilograms are the bill"
date: 2026-11-02T16:55:31+08:00
summary: "SpaceX, Google and a start-up called Starcloud plan AI data centres in orbit, where the sun almost never sets and nobody queues for the grid. But the sunlight is free only at the source: every square metre of solar array that collects it, and of radiator that throws its heat away, has to be launched. On the mass SpaceX filed and the power it publishes, its satellite carries about 58 kilowatts of computing per tonne against its target of 100, and today's launch price is far above the $200 a kilogram at which Google's paper says launch could stop being the main cost."
category: "Analysis"
format: "depth"
cover: "/covers/data-centres-in-space.svg"
tags: ["cooling", "data-centres", "space", "power"]
draft: false
updated: 2026-11-07
updateNote: "Rebuilt in depth: what an orbital data centre weighs, part by part, against the launch fare, with evidence to 7 November 2026."
---

<a id="data-centres-in-space"></a>

SpaceX has asked American regulators for room to put up to one million AI computing satellites into orbit. It has also told them, in a letter of 29 May 2026, what one of those satellites would weigh: 3,000 kilograms.

That number is the hinge of this piece. In orbit the sunlight is free and there is no queue for the grid. But the solar array that collects the sunlight, and the radiator that throws its heat away, are both launched and paid for by the kilogram. On the mass SpaceX filed and the power it publishes, its satellite carries about 58 kilowatts of computing per tonne; its own page claims 75. The target is 100.

So the claim is this. In orbit the sunlight is free but the kilograms are the bill. By the end of 2028, no operator will report a computing satellite in service at SpaceX's target of 100 kilowatts per tonne launched, and no rocket company will publish a price low enough to make the sums easy.

To see why, the piece follows the questions in order. Why anyone would put a data centre in orbit, and what one would look like. Then why heat can leave only as light, how large and heavy the radiator must be, and whether the sunlight is really free. Then what a kilowatt weighs, whether a heat pump helps, and what else could bind first. Finally, what has flown, what launch costs, how the bill compares with the ground, who is paid, and what would prove me wrong.

<details class="analogy">
<summary>The analogy</summary>
<p>Picture a laptop sealed in a vacuum flask on a sunny windowsill. The sunshine is free, but the laptop needs a solar panel the size of a tablecloth to catch enough of it. The flask keeps tea hot and here traps the laptop's heat.</p>
<p>The only way out is a black fin poking through the lid, glowing the heat away. A hotter fin can be smaller, so how hot the laptop may run sets the fin's size. And the panel and the fin both go up by courier, charged by the kilogram: that is the launch fare.</p>
</details>

## Why would anyone put a data centre in orbit?

Because on the ground the scarce thing is the plug, and in orbit there is no plug to queue for.

A data centre on the ground needs a grid connection, and in America the wait for one now runs to years, as told in [America rations the plug](/journal/america-rations-the-plug/). It also needs land, water or air for cooling, and permits from towns that increasingly say no.

In orbit, sunlight arrives at about 1,361 watts per square metre, with no clouds and no night for much of the year. Google's project lead, Travis Beals, wrote that in the right orbit "a solar panel can be up to 8 times more productive than on earth" (4 November 2025). SpaceX's finance chief, Bret Johnsen, put it at "roughly five times, if not more" (9 June 2026).

The right orbit is a **dawn-dusk sun-synchronous orbit**: a near-polar path that rides the line between day and night, so the panels face the sun almost all the time. Google's design uses it, and Starcloud, a start-up building computing satellites, has filed for it.

So the pitch is simple: free power, no queue, no water. The rest of this piece asks what that power costs to collect and what its heat costs to throw away, both counted in kilograms.

## What would an orbital data centre look like?

On SpaceX's own published design, a satellite a little wider than a jumbo jet's wings, mostly made of solar array.

SpaceX calls its system Starmind and its first satellite AI1. Its web page, read on 7 November 2026, gives the satellite a "Compute payload Up to 250 kW peak / 175 kW average". It lists a "Solar array 210 kW" at "250 W / m²", and a "Deployable liquid radiator 160 m²". The wingspan is 75 metres.

A **kilowatt (kW)** is a thousand watts. For scale, 175 kW is about one and a half of Nvidia's GB200 racks, the AI cabinets now filling data halls on the ground.

At 250 watts per square metre, a 210 kW array covers about 840 square metres, my arithmetic: more than three tennis courts. The radiator, at 160 square metres, is about a fifth of that. The 250 watts is what the array delivers as electricity, about 18% of the sunlight that falls on it.

SpaceX's letter to the Federal Communications Commission (FCC), the American regulator of satellites, filled in the rest. For satellites below 600 kilometres it gives a "Mass" of 3,000 kg, a "Total Area" of 800 m², and a "Bus & Radiator Area" of 100 m². The letter was filed on 29 May 2026, when SpaceX's published plans were smaller: its S-1 spoke of early satellites "generating 100 kilowatts of compute power", and its interviews of early June of about 120 kW average and 150 kW peak. So the 3,000 kg may belong to the earlier design.

Google's design is a cluster rather than one large craft. Its research paper, "Towards a future space-based, highly scalable AI infrastructure system design", sketches 81 satellites flying in formation at about 650 kilometres, 100 to 200 metres apart, linked by lasers. Each would carry Google's own AI chips, its **TPUs**.

<figure class="illo">
<p class="illo-title">The array is five times the radiator, and both are launched</p>
<p class="illo-sub">SpaceX's AI1 computing satellite, as published, drawn to scale</p>
<svg viewBox="0 0 940 386" role="img" aria-label="Scale drawing of SpaceX's AI1 computing satellite as published on its Starmind page. Two solar wings span 75 metres and cover about 840 square metres, delivering 210 kilowatts at 250 watts per square metre. A small bus at the centre carries chips drawing 175 kilowatts on average and 250 at peak. A radiator of 160 square metres, about a fifth of the array's area, sheds that heat at about 47 to 54 degrees, counting the Earth's glow, from both faces. A tennis court is drawn beside it for scale. The mass filed with the FCC is 3,000 kilograms, about 58 kilowatts per tonne against a target of 100."><rect class="i-cool-f" x="95" y="34" width="350" height="120" rx="2"/><line class="i-thin" x1="145" y1="34" x2="145" y2="154"/><line class="i-thin" x1="195" y1="34" x2="195" y2="154"/><line class="i-thin" x1="245" y1="34" x2="245" y2="154"/><line class="i-thin" x1="295" y1="34" x2="295" y2="154"/><line class="i-thin" x1="345" y1="34" x2="345" y2="154"/><line class="i-thin" x1="395" y1="34" x2="395" y2="154"/><line class="i-thin" x1="95" y1="94.0" x2="445" y2="94.0"/><rect class="i-cool-f" x="495" y="34" width="350" height="120" rx="2"/><line class="i-thin" x1="545" y1="34" x2="545" y2="154"/><line class="i-thin" x1="595" y1="34" x2="595" y2="154"/><line class="i-thin" x1="645" y1="34" x2="645" y2="154"/><line class="i-thin" x1="695" y1="34" x2="695" y2="154"/><line class="i-thin" x1="745" y1="34" x2="745" y2="154"/><line class="i-thin" x1="795" y1="34" x2="795" y2="154"/><line class="i-thin" x1="495" y1="94.0" x2="845" y2="94.0"/><rect class="i-metal" x="445.0" y="69.0" width="50" height="50" rx="2"/><text class="i-cool-t" x="270" y="174" text-anchor="middle">solar array, about 840 m²</text><text class="i-cool-t" x="670" y="174" text-anchor="middle">210 kW at 250 W/m²</text><line class="i-line" x1="95.0" y1="20" x2="845.0" y2="20"/><line class="i-line" x1="95.0" y1="15" x2="95.0" y2="25"/><line class="i-line" x1="845.0" y1="15" x2="845.0" y2="25"/><text class="i-n" x="470.0" y="14" text-anchor="middle">wingspan 75 m</text><line class="i-dash" x1="470.0" y1="119.0" x2="470.0" y2="216"/><rect class="i-hot-f" x="390.0" y="216" width="160" height="100" rx="2"/><line class="i-thin" x1="398.0" y1="228" x2="542.0" y2="228"/><line class="i-thin" x1="398.0" y1="241" x2="542.0" y2="241"/><line class="i-thin" x1="398.0" y1="254" x2="542.0" y2="254"/><line class="i-thin" x1="398.0" y1="266" x2="542.0" y2="266"/><line class="i-thin" x1="398.0" y1="278" x2="542.0" y2="278"/><line class="i-thin" x1="398.0" y1="291" x2="542.0" y2="291"/><line class="i-thin" x1="398.0" y1="304" x2="542.0" y2="304"/><text class="i-hot-t" x="562.0" y="246">radiator, 160 m²</text><text class="i-n" x="562.0" y="264">sheds 175 kW at 47 to 54°C,</text><text class="i-n" x="562.0" y="280">glowing from both faces</text><text class="i-n" x="437.0" y="206" text-anchor="end">chips: 175 kW average, 250 peak</text><rect class="i-faint" x="40" y="216" width="238" height="110"/><line class="i-thin" x1="159" y1="216" x2="159" y2="326"/><text class="i-n" x="159" y="344" text-anchor="middle">a tennis court, for scale</text><text class="i-t" x="470.0" y="372" text-anchor="middle">Mass filed with the FCC: 3,000 kg. At 175 kW, about 58 kW per tonne; the target is 100.</text></svg>
<figcaption>SpaceX Starmind page, read 7 November 2026, for the wingspan, array, radiator and power; SpaceX letter to the FCC, 29 May 2026, for the mass, which may belong to an earlier, smaller design. The wing and radiator shapes are my assumptions; their areas are SpaceX's. My drawing.</figcaption>
</figure>

## Why can heat leave only as light?

Because a vacuum has nothing in it to carry heat away.

On the ground, a data centre's heat leaves through air or water, as told in [heat and water](/journal/heat-and-water/): fans blow it, towers evaporate it, radiators hand it to the breeze. In orbit there is no breeze. SpaceX's prospectus says it plainly: "thermal control must be accomplished through radiation rather than convection and conduction" (12 June 2026).

Every warm object glows, mostly in infrared light we cannot see. The **Stefan-Boltzmann law**, from 1879, says how much: the heat radiated rises with the fourth power of the surface's absolute temperature. **Absolute temperature** is measured in kelvin, from absolute zero, so 27°C is about 300 kelvin.

The fourth power is the whole game. Each 1% rise in absolute temperature sheds about 4% more heat. A panel at 67°C sheds about 1.8 times what the same panel sheds at 20°C, on my arithmetic.

**Emissivity**, from 0 to 1, is how well a surface glows compared with a perfect black surface. Good white coatings reach about 0.92 and reflect most sunlight. With emissivity near its limit and area costing mass, temperature is the only free lever.

<figure class="chart">
<p class="chart-title">A radiator sheds more heat the hotter it runs, by the fourth power</p>
<p class="chart-sub">Heat radiated to deep space by a two-sided panel, watts per square metre, by temperature</p>
<svg viewBox="0 0 560 280" role="img" aria-label="Line chart of the heat a two-sided panel radiates to deep space, in watts per square metre, against its temperature from 0 to 110 degrees Celsius, at emissivity 0.92. The curve rises with the fourth power of absolute temperature: about 581 watts at 0 degrees, 771 at 20, about 1,090 near 47, 1,400 at 67 and about 2,020 at 100. A shaded band marks Nvidia's coolant temperatures of 45 to 55 degrees. Points mark Starcloud's panel at 20 degrees, SpaceX's published design at about 1,090 watts, and Musk's 1,400 watts, which needs about 67 degrees."><g class="c-grid"><line x1="56" y1="250.0" x2="540" y2="250.0"/><line x1="56" y1="200.0" x2="540" y2="200.0"/><line x1="56" y1="150.0" x2="540" y2="150.0"/><line x1="56" y1="100.0" x2="540" y2="100.0"/><line x1="56" y1="50.0" x2="540" y2="50.0"/></g><g class="c-axis"><text x="48" y="254.0" text-anchor="end">0</text><text x="48" y="204.0" text-anchor="end">500</text><text x="48" y="154.0" text-anchor="end">1,000</text><text x="48" y="104.0" text-anchor="end">1,500</text><text x="48" y="54.0" text-anchor="end">2,000</text><text x="56.0" y="270" text-anchor="middle">0°C</text><text x="144.0" y="270" text-anchor="middle">20°C</text><text x="232.0" y="270" text-anchor="middle">40°C</text><text x="320.0" y="270" text-anchor="middle">60°C</text><text x="408.0" y="270" text-anchor="middle">80°C</text><text x="496.0" y="270" text-anchor="middle">100°C</text></g><rect class="c-zone" x="254.0" y="30" width="44.0" height="220"/><text class="c-note" x="276.0" y="22" text-anchor="middle">Nvidia coolant, 45 to 55°C</text><polyline class="c-line c-s1" points="56.0,191.9 64.8,190.2 73.6,188.4 82.4,186.6 91.2,184.8 100.0,182.9 108.8,181.0 117.6,179.1 126.4,177.1 135.2,175.0 144.0,173.0 152.8,170.8 161.6,168.7 170.4,166.4 179.2,164.2 188.0,161.9 196.8,159.5 205.6,157.1 214.4,154.7 223.2,152.2 232.0,149.7 240.8,147.1 249.6,144.4 258.4,141.8 267.2,139.0 276.0,136.2 284.8,133.4 293.6,130.5 302.4,127.5 311.2,124.5 320.0,121.5 328.8,118.4 337.6,115.2 346.4,112.0 355.2,108.7 364.0,105.3 372.8,101.9 381.6,98.5 390.4,95.0 399.2,91.4 408.0,87.7 416.8,84.0 425.6,80.3 434.4,76.4 443.2,72.5 452.0,68.6 460.8,64.5 469.6,60.4 478.4,56.3 487.2,52.0 496.0,47.7 504.8,43.4 513.6,38.9 522.4,34.4 531.2,29.8 540.0,25.2"/><circle class="c-dot c-s2" cx="144.0" cy="173.0" r="5"/><text class="c-lab c-s2t" x="152.0" y="195.0" text-anchor="start">Starcloud's panel, 20°C: 771</text><circle class="c-dot c-s2" cx="262.8" cy="140.4" r="5"/><text class="c-lab c-s2t" x="270.8" y="162.4" text-anchor="start">SpaceX's page: about 1,090</text><circle class="c-dot c-s2" cx="350.8" cy="110.3" r="5"/><text class="c-lab c-s2t" x="342.8" y="100.3" text-anchor="end">Musk's 1,400 needs about 67°C</text><line class="c-base" x1="56" y1="250" x2="540" y2="250"/></svg>
<figcaption>Stefan-Boltzmann law at emissivity 0.92, both faces, ignoring sunlight and the Earth's glow, my arithmetic. Coolant band: Nvidia, 16 March and 21 June 2026. Points: Starcloud white paper (September 2024); SpaceX Starmind page; interview SpaceX filed with the SEC, 9 June 2026.</figcaption>
</figure>

## How large must the radiator be?

That depends on how hot it may run, and the chip decides that.

A radiator cannot run hotter than the coolant feeding it, and the coolant cannot run hotter than the chips allow. On the ground, Nvidia's newest racks take coolant at up to 45°C, and it leaves the chip at about 55°C, Nvidia says (16 March and 21 June 2026). That is the ceiling for any panel carrying their heat.

Elon Musk, SpaceX's chief executive, gave SpaceX's figure in an interview the company filed with the SEC (9 June 2026): radiators shedding about 1,400 watts per square metre, "radiating on both sides". Read as watts per square metre of panel, which the interview does not specify, a shaded two-sided panel at emissivity 0.92 sheds that only near 67°C, on my arithmetic. That is hotter than the coolant leaving Nvidia's chips today.

SpaceX's current page implies a cooler panel. Its 175 kW average over 160 square metres is about 1,090 watts per square metre, which the same panel sheds near 47°C in deep shade, or near 54°C once the Earth's glow is counted, my arithmetic. That is about the temperature at which coolant leaves Nvidia's chips, so it fits warm-water coolant with little to spare.

The sun and the Earth shine back. A panel flown edge-on to the sun avoids most direct sunlight, but it still sees the Earth's own infrared glow. At 650 kilometres, a two-sided panel edge-on to the Earth absorbs about 106 watts per square metre of that glow, my arithmetic. To shed 1,400 watts net, it must then run near 73°C.

Starcloud's white paper (September 2024) nets 633 watts per square metre from a panel at 20°C. Its sum counts the Earth's glow at about 14 watts, using the coating's absorption of sunlight. In the infrared a surface absorbs at its emissivity, about 0.92, so on my arithmetic the Earth adds about 63 watts. The net falls to about 585.

So a radiator sheds somewhere between about 600 and 1,400 watts per square metre, depending on how hot the chip lets it run. A 175 kW satellite needs between about 125 and 300 square metres.

## Why is a radiator heavy?

Because it is a large, thin, leak-proof panel that must unfold in orbit, survive debris and run for years with no repair crew.

A space radiator is a sheet of metal with fine tubes running through it, carrying coolant from the chips. The tubes spread the heat across the sheet, and the sheet glows it away. The International Space Station's radiators carry ammonia through Inconel tubes in two separate paths per panel, so one puncture cannot drain everything.

The station gives the best-known weight. NASA's overview of its cooling system lists six radiator units, each "1,122.64 kilograms", together rejecting 70 kW. That is about 96 kg per kW, and about 14 kg per square metre of panel, my arithmetic. The station's loop runs cold, about 3°C at supply, to cool a crew, and on its rated 70 kW each square metre sheds only about 147 watts.

That is a heavy heritage, and newer designs are lighter. NASA Glenn, the agency's Ohio laboratory, lists the station's radiators at "~9 kg/m2" and heat-pipe radiators at "~3 kg/m2", a design tested at full scale in 2011 (23 January 2025). A NASA paper of 2008 put pumped-loop radiators at "6 to 10 kg/m2". A **heat pipe** is a sealed tube with a wick inside that moves heat with no pump, so one puncture loses one pipe, not the loop.

At 1,400 watts per square metre, those weights give between about 2 and 10 kg per kW of heat, my arithmetic. The light end is a design tested on the ground, at 127°C, far hotter than a chip loop; the heavy end has flown for decades.

<figure class="chart">
<p class="chart-title">Flown radiators are heavy; light ones have been tested only on the ground</p>
<p class="chart-sub">Space radiator mass, kilograms per square metre of panel</p>
<svg viewBox="0 0 560 204" role="img" aria-label="Bar chart of space radiator mass per square metre of panel. The International Space Station's radiators as flown, from NASA's unit masses, about 14.2 kilograms. The same radiators as NASA Glenn lists them, about 9. Pumped-loop designs in a 2008 NASA paper, 6 to 10. A heat-pipe radiator tested on the ground in 2011, about 3."><g class="c-grid"><line x1="190.0" y1="32" x2="190.0" y2="196"/><line x1="258.5" y1="32" x2="258.5" y2="196"/><line x1="327.0" y1="32" x2="327.0" y2="196"/><line x1="395.5" y1="32" x2="395.5" y2="196"/><line x1="464.0" y1="32" x2="464.0" y2="196"/></g><g class="c-axis"><text x="190.0" y="26" text-anchor="middle">0 kg</text><text x="258.5" y="26" text-anchor="middle">4 kg</text><text x="327.0" y="26" text-anchor="middle">8 kg</text><text x="395.5" y="26" text-anchor="middle">12 kg</text><text x="464.0" y="26" text-anchor="middle">16 kg</text></g><text class="c-box-t" x="0" y="53">Space station, as flown</text><text class="c-note" x="0" y="68">NASA unit masses</text><rect class="c-bar c-mute" x="190" y="44" width="243.2" height="22" rx="2"/><text class="c-lab c-s1t" x="439.2" y="60">14.2 kg/m²</text><text class="c-box-t" x="0" y="95">Space station, NASA Glenn</text><text class="c-note" x="0" y="110">listed figure</text><rect class="c-bar c-mute" x="190" y="86" width="154.1" height="22" rx="2"/><text class="c-lab c-s1t" x="350.1" y="102">~9</text><text class="c-box-t" x="0" y="137">Pumped-loop designs</text><text class="c-note" x="0" y="152">NASA paper, 2008</text><rect class="c-bar c-alt" x="292.8" y="128" width="68.5" height="22" rx="2"/><text class="c-lab c-s1t" x="367.2" y="144">6 to 10</text><text class="c-box-t" x="0" y="179">Heat-pipe radiator</text><text class="c-note" x="0" y="194">tested on the ground, 2011</text><rect class="c-bar" x="190" y="170" width="51.4" height="22" rx="2"/><text class="c-lab c-s1t" x="247.4" y="186">~3</text><line class="c-base" x1="190" y1="32" x2="190" y2="196"/></svg>
<figcaption>NASA space station cooling overview, unit masses and areas, my arithmetic; NASA Glenn, 23 January 2025; Juhasz, NASA/TM-2008-215420.</figcaption>
</figure>

Three things keep real radiators from the light end. They must fold to fit under a rocket's nose and unfold in orbit, so they need hinges and flexible lines. They must survive tiny debris for years, so they carry spare loops and armour. And they cannot be fixed. SpaceX's own risk factors say its orbital computing "will not be easily repaired or upgraded".

## Is the sunlight really free?

The sunlight is. The array that catches it is not, and it may weigh more than the radiator.

On SpaceX's own page the array is about 840 square metres and the radiator 160: more than five times the area. An array is thinner than a radiator, but unless the radiator is station-heavy, not five times lighter.

Redwire, which makes the roll-out arrays flying on the space station, publishes power and mass for its range. Its products deliver about 71 to 124 watts per kilogram, my arithmetic from its table. That is 8 to 14 kg of array for each kW of electricity, before any chip, radiator or structure.

NASA's survey of small-satellite power says arrays "are strongly clustered around ~30 W/kg", with the best roll-out designs at about 100 or above (7 May 2026). A preprint by Gaalema, Indyk and Staley (9 April 2026, not peer reviewed) argues an integrated design could reach "about 500 W/kg". No array at this scale has flown at that weight.

And the dawn-dusk orbit is not always sunny. At 650 kilometres, on my arithmetic, there are about three months a year with an eclipse on every orbit, up to about 20 minutes of each 98-minute circuit. Riding through 20 minutes at 175 kW takes about 58 kilowatt-hours of battery, roughly 220 to 390 kg of cells. Google's blog says the orbit "reduces the need for heavy onboard batteries", not that it removes it.

So the plug in orbit is free only at the source. The array that replaces the grid connection is launched like everything else.

## What does a kilowatt weigh in orbit?

More than SpaceX's target allows, on every published figure I can find.

SpaceX's prospectus speaks of 100 gigawatts a year "via satellites carrying over 100 kilowatts of compute power per metric ton". Turned upside down, that is 10 kg launched for each kW of computing. Everything sits inside that 10 kg: array, radiator, chips, structure, batteries and shielding.

Now add up the parts, each at today's published weights. The array is 8 to 14 kg per kW. The radiator is 2 to 10. A ground AI rack weighs about 11 kg per kW, on a press figure of about 1.36 tonnes for a GB200 rack, though a space-built payload would shed its steel. Batteries for the eclipse season add 1 to 2. The array alone, or a ground rack alone, sits near or over the whole budget, and a station-weight radiator would too.

<figure class="chart">
<p class="chart-title">The array alone uses most of SpaceX's 10 kilogram budget</p>
<p class="chart-sub">Kilograms launched per kilowatt, by part, at today's published weights</p>
<svg viewBox="0 0 560 222" role="img" aria-label="Range bar chart of kilograms launched per kilowatt for each part of an orbital data centre, against SpaceX's target of 10 kilograms for the whole craft, shown as a dashed line. Solar array, from Redwire's product range, 8 to 14. Radiator, at 1,400 watts per square metre, 2 to 10. Chips and rack, from a ground GB200 rack, about 11, a ceiling since a space payload sheds steel. Eclipse batteries, cells only, 1 to 2. The array alone, or a ground rack alone, sits near or over the whole budget."><g class="c-grid"><line x1="170.0" y1="32" x2="170.0" y2="196"/><line x1="247.5" y1="32" x2="247.5" y2="196"/><line x1="325.0" y1="32" x2="325.0" y2="196"/><line x1="402.5" y1="32" x2="402.5" y2="196"/><line x1="480.0" y1="32" x2="480.0" y2="196"/></g><g class="c-axis"><text x="170.0" y="26" text-anchor="middle">0 kg</text><text x="247.5" y="26" text-anchor="middle">4 kg</text><text x="325.0" y="26" text-anchor="middle">8 kg</text><text x="402.5" y="26" text-anchor="middle">12 kg</text><text x="480.0" y="26" text-anchor="middle">16 kg</text></g><text class="c-box-t" x="0" y="53">Solar array</text><text class="c-note" x="0" y="68">Redwire's range</text><rect class="c-bar" x="325.0" y="44" width="116.2" height="22" rx="2"/><text class="c-lab c-s1t" x="447.2" y="60">8 to 14</text><text class="c-box-t" x="0" y="95">Radiator</text><text class="c-note" x="0" y="110">at 1,400 W/m²</text><rect class="c-bar" x="210.7" y="86" width="155.0" height="22" rx="2"/><text class="c-lab c-s1t" x="371.7" y="102">2 to 10</text><text class="c-box-t" x="0" y="137">Chips and rack</text><text class="c-note" x="0" y="152">ground GB200, a ceiling</text><rect class="c-bar c-mute" x="170" y="128" width="213.1" height="22" rx="2"/><text class="c-lab c-s1t" x="389.1" y="144">about 11</text><text class="c-box-t" x="0" y="179">Eclipse batteries</text><text class="c-note" x="0" y="194">cells only</text><rect class="c-bar c-alt" x="193.2" y="170" width="19.4" height="22" rx="2"/><text class="c-lab c-s1t" x="218.6" y="186">1 to 2</text><line class="c-base" x1="170" y1="32" x2="170" y2="196"/><line class="c-today" x1="363.8" y1="32" x2="363.8" y2="196"/><text class="c-note" x="357.8" y="214" text-anchor="end">SpaceX's whole budget: 10 kg per kW</text></svg>
<figcaption>My arithmetic from Redwire's product table, the radiator figures above at 1,400 W/m², a press figure for a GB200 rack (The Register, 21 March 2024) and NASA's battery cell range. SpaceX prospectus, 12 June 2026, for the target.</figcaption>
</figure>

SpaceX's own numbers say the same. Its page gives "Vehicle efficiency 75 kW / ton", a quarter short of the prospectus target. Its FCC mass of 3,000 kg, against its page's 175 kW average, gives about 58 kW per tonne, my arithmetic; even the 250 kW peak gives about 83. Johnsen's "About 5 megawatts per launch", for the first satellite on today's Starship, would be about 50 if each launch carried the 100 tonnes SpaceX targets over time, my arithmetic.

For comparison, Google's paper estimates a Starlink V2 mini, one of SpaceX's internet satellites, at 575 kg and about 28 kW. That is about 49 kW per tonne for the whole craft, and only part of that power goes to anything like computing.

<figure class="chart">
<p class="chart-title">No published figure reaches SpaceX's target of 100 kW per tonne</p>
<p class="chart-sub">Kilowatts of computing per tonne launched</p>
<svg viewBox="0 0 560 306" role="img" aria-label="Bar chart of kilowatts of computing per tonne launched. SpaceX's prospectus target, 100. SpaceX's page, vehicle efficiency 75. AI1 at its 250 kilowatt peak over the 3,000 kilograms filed with the FCC, about 83. AI1 at its 175 kilowatt average, about 58. Five megawatts per Starship launch, divided by the 100 tonnes SpaceX targets over time, 50. Google's estimate for a Starlink V2 mini, whole craft, about 49. Starcloud-1, at most about 12."><g class="c-grid"><line x1="170.0" y1="32" x2="170.0" y2="298"/><line x1="240.8" y1="32" x2="240.8" y2="298"/><line x1="311.7" y1="32" x2="311.7" y2="298"/><line x1="382.5" y1="32" x2="382.5" y2="298"/><line x1="453.3" y1="32" x2="453.3" y2="298"/></g><g class="c-axis"><text x="170.0" y="26" text-anchor="middle">0</text><text x="240.8" y="26" text-anchor="middle">25</text><text x="311.7" y="26" text-anchor="middle">50</text><text x="382.5" y="26" text-anchor="middle">75</text><text x="453.3" y="26" text-anchor="middle">100</text></g><text class="c-box-t" x="0" y="53">SpaceX target</text><text class="c-note" x="0" y="68">prospectus</text><rect class="c-bar c-alt" x="170" y="44" width="283.3" height="22" rx="2"/><text class="c-lab c-s1t" x="459.3" y="60">100</text><text class="c-box-t" x="0" y="91">SpaceX page</text><text class="c-note" x="0" y="106">"vehicle efficiency"</text><rect class="c-bar c-mute" x="170" y="82" width="212.5" height="22" rx="2"/><text class="c-lab c-s1t" x="388.5" y="98">75</text><text class="c-box-t" x="0" y="129">AI1 peak, FCC mass</text><text class="c-note" x="0" y="144">250 kW / 3 t</text><rect class="c-bar" x="170" y="120" width="235.2" height="22" rx="2"/><text class="c-lab c-s1t" x="411.2" y="136">83</text><text class="c-box-t" x="0" y="167">AI1 average, FCC mass</text><text class="c-note" x="0" y="182">175 kW / 3 t</text><rect class="c-bar" x="170" y="158" width="164.3" height="22" rx="2"/><text class="c-lab c-s1t" x="340.3" y="174">58</text><text class="c-box-t" x="0" y="205">Per Starship launch</text><text class="c-note" x="0" y="220">5 MW / 100 t, if full</text><rect class="c-bar" x="170" y="196" width="141.7" height="22" rx="2"/><text class="c-lab c-s1t" x="317.7" y="212">50</text><text class="c-box-t" x="0" y="243">Starlink V2 mini</text><text class="c-note" x="0" y="258">whole craft, Google</text><rect class="c-bar c-mute" x="170" y="234" width="138.8" height="22" rx="2"/><text class="c-lab c-s1t" x="314.8" y="250">49</text><text class="c-box-t" x="0" y="281">Starcloud-1</text><text class="c-note" x="0" y="296">at most, one H100</text><rect class="c-bar c-mute" x="170" y="272" width="34.0" height="22" rx="2"/><text class="c-lab c-s1t" x="210.0" y="288">12</text><line class="c-base" x1="170" y1="32" x2="170" y2="298"/></svg>
<figcaption>SpaceX prospectus, Starmind page, FCC letter and filed interview; Google's Suncatcher paper, Table 1; Nvidia blog for Starcloud-1's 60 kg. Ratios are my arithmetic; Starcloud-1 assumes its chip at full power.</figcaption>
</figure>

## Can a heat pump shrink the radiator?

<a id="heat-pump-trade"></a>

Sometimes, but it costs array to save radiator, and warmer chips are the cheaper lever.

A **heat pump** moves heat from a cooler place to a hotter one, using work, like a fridge in reverse. In orbit it could take the chips' coolant at 45°C and raise the radiator to 100°C. By the fourth power, the hotter panel sheds almost twice as much per square metre. Starcloud's white paper notes the gain, "albeit at an added energy cost".

The energy comes from the array. On my arithmetic, lifting 1 kW of heat from 45°C to 100°C at half the ideal efficiency takes about 0.35 kW of work. The hotter panel saves about 0.27 square metres of radiator, net of the pump's own heat. The extra power needs about 1.4 square metres of array, at 250 watts per square metre.

So in area a pump never pays. In mass, it depends on what each square metre weighs. A pump saves mass only if the array weighs less than about a fifth as much per square metre as the radiator.

With station-weight radiators, that can be true. On my arithmetic, with a radiator at 14 kg per square metre, a pump saves about 9% of radiator-plus-array mass with arrays at 100 watts per kilogram, and 2 to 15% across Redwire's range. It saves about 28% with arrays at 250 watts per kilogram. With light radiators of 3 to 6 kg per square metre, it saves little or nothing.

The cheaper lever is the chip. Running the chips' coolant at 60°C instead of 45°C cuts radiator mass by about 18%, on my arithmetic, with no extra array at all. So in orbit a chip's temperature rating is a launch cost, the same lever that makes [warm water work on the ground](/journal/heat-and-water/).

## Could radiation, latency or bandwidth bind first?

Each is real, but each costs a margin. Mass costs on every kilowatt of every launch.

**Radiation** comes in two kinds. **Total dose**, measured in rad, builds up and wears a chip out, like sunburn. A **single event** is one particle flipping a bit, which can give a silent wrong answer. Google tested its Trillium TPU in a proton beam. Memory showed irregularities only after 2 krad, almost three times the 750 rad a shielded five-year mission expects.

Google revised its paper on 17 June 2026 and re-ran the test "with improved methods". Silent errors in the chip's logic now come at "approximately one event/17 rad", about "1 per 3 million inferences, assuming 1 inference per second". On my arithmetic that is about nine silent errors per chip per year. Their effect on training "requires further study".

The dose figure assumes "significant shielding (e.g. 10 mm Al equivalent)". Ten millimetres of aluminium weighs 27 kg per square metre of enclosure, my arithmetic, so the radiation result is bought with mass too.

**Latency** is short: light takes about 2 milliseconds each way from 650 kilometres straight overhead, and about 7 when it is 10 degrees above the horizon. But a ground station sees each satellite for only minutes, so constant service needs laser relays between satellites.

**Bandwidth** to the ground is the narrow lane. Google's design needs links between satellites "on the order of 10Tbps", while the ground record it cites is NASA's TBIRD, "demonstrating 200Gbps ground-LEO communications in 2023". Orbit suits answering questions, where a reply is a few kilobytes, more than training, which moves vast data.

## What has actually flown?

Small craft running single chips, and no weighed computing satellite near the target.

Starcloud-1, a 60 kg satellite "about the size of a small fridge", as Nvidia's blog described it before launch, went up in November 2025 with one Nvidia H100 GPU, Starcloud says. Astro Digital, which built it, says it has since run AI inference in orbit (SEC filing, 29 September 2026). Starcloud has published no power figure. If its chip ran at full power, about 700 watts, that is at most about 12 kW per tonne, my arithmetic.

Google and Planet, the satellite maker, launched a Suncatcher prototype on 1 October 2026, on a SpaceX rideshare. On 30 October Google said it had received its first answer from the satellite's "Gemma 4 open model", over Svalbard, with thermal and radiation tests still to come. NPR, the American public broadcaster, reported that it carries four TPUs and would run Gemma "15 minutes at a time due to heat management constraints". It also reported, in a correction, that the prototype "is in a standard orbit and uses batteries".

That is worth pausing on. Google's first data-centre-class chip in orbit is to run minutes at a time, NPR reported, and the limit it gave is heat. It is not in the orbit the design depends on, and Google has published no mass.

China's Three-Body Computing Constellation, built by ADA Space with Zhejiang Lab, had 20 satellites in orbit after a second batch on 14 October 2026, press reports say. It states its computing in operations per second, not kilowatts, and publishes no power or mass. Axiom Space put two computing nodes on Kepler's relay satellites in January 2026, as reported.

The announced plans run in gigawatts. SpaceX has asked the FCC for up to one million satellites; Starcloud for up to 88,000, accepted for filing on 13 March 2026. Neither had been granted in any FCC public notice I could find, as of 7 November 2026. What has flown runs to a few kilowatts.

## What does launch cost, and when might it fall?

Thousands of dollars a kilogram today, and Google cites $200 as the level where launch could stop being the main cost.

Google's paper uses a "current launch price $3,600/kg, based on Falcon 9 (reusable configuration)", SpaceX's working rocket. That is Google's estimate, not a published price. It describes $200 a kilogram as "often cited, by SpaceX and others, as a threshold beyond which launch could cease to be the limiting cost factor".

When might it arrive? Google expects launch "may reach ≲$200/kg by the mid-2030s". That assumes prices keep falling about 20% for each doubling of mass launched, which "would require ∼180 Starship launches/year". If far less mass is launched, Google's paper puts the price nearer $300 by the mid-2030s.

Starship, SpaceX's much larger rocket, is the reason anyone expects that fall. It reached orbit for the first time on its 14th flight, in the third quarter of 2026, delivering 26 Starlink V3 satellites, SpaceX said (20 October 2026). SpaceX has published no Starship price per kilogram.

Seats may bind before price. Starcloud's chief executive, Philip Johnston, told TechCrunch in August 2026 that launch is constrained, as reported. If one company owns the only rocket of Starship's size and builds its own computing satellite too, its satellites may fly first.

## How does the bill compare with a hall on the ground?

At today's launch price, the launch bill alone is five to 26 times a ground hall's power bill. At $200 a kilogram, it falls inside the ground's range.

Google turns launch cost into a "launched power price": the launch bill for each kilowatt, spread over a five-year life. For a Starlink-class satellite at $3,600 a kilogram, that is $14,700 per kW per year. An American AI hall's power bill, on Google's range of electricity prices and overheads, is $570 to $3,000 per kW per year.

At $200 a kilogram, the same satellite falls to $810, inside the ground range. That is the case for orbit in one number. But it counts launch only: chips, arrays and the satellite itself are left out on both sides.

<figure class="chart">
<p class="chart-title">At today's fare orbit costs five to 26 times the ground; at $200 it falls inside its range</p>
<p class="chart-sub">Launched power price, dollars per kilowatt per year over a five-year life, launch only</p>
<svg viewBox="0 0 560 162" role="img" aria-label="Bar chart of Google's launched power price in dollars per kilowatt per year over a five-year life. A Starlink-class satellite at a launch price of 3,600 dollars a kilogram, 14,700 dollars. The same craft at 200 dollars a kilogram, 810. The power bill of an American AI hall on the ground, 570 to 3,000."><g class="c-grid"><line x1="170.0" y1="32" x2="170.0" y2="154"/><line x1="264.4" y1="32" x2="264.4" y2="154"/><line x1="358.9" y1="32" x2="358.9" y2="154"/><line x1="453.3" y1="32" x2="453.3" y2="154"/></g><g class="c-axis"><text x="170.0" y="26" text-anchor="middle">$0k</text><text x="264.4" y="26" text-anchor="middle">$5k</text><text x="358.9" y="26" text-anchor="middle">$10k</text><text x="453.3" y="26" text-anchor="middle">$15k</text></g><text class="c-box-t" x="0" y="53">Orbit, $3,600/kg</text><text class="c-note" x="0" y="68">Starlink-class, today</text><rect class="c-bar" x="170" y="44" width="277.7" height="22" rx="2"/><text class="c-lab c-s1t" x="453.7" y="60">$14,700</text><text class="c-box-t" x="0" y="95">Orbit, $200/kg</text><text class="c-note" x="0" y="110">the same craft</text><rect class="c-bar c-alt" x="170" y="86" width="15.3" height="22" rx="2"/><text class="c-lab c-s1t" x="191.3" y="102">$810</text><text class="c-box-t" x="0" y="137">Ground power bill</text><text class="c-note" x="0" y="152">US AI hall, Google's range</text><rect class="c-bar c-mute" x="180.8" y="128" width="45.9" height="22" rx="2"/><text class="c-lab c-s1t" x="232.7" y="144">$570 to $3,000</text><line class="c-base" x1="170" y1="32" x2="170" y2="154"/></svg>
<figcaption>Google's Suncatcher paper. Launch cost only: chips, arrays and the satellite itself are left out on both sides.</figcaption>
</figure>

And the fare recurs. A satellite flown on a five-year life must be launched again when it wears out. SpaceX's risk factors say its satellites' useful life "is inherently shorter" than that of the systems they host. On the ground, the hall and its [grid gear outlast three or four chip generations](/journal/the-equipment-queue/).

The two halves of the bill multiply. The launched power price is kilograms per kilowatt times the fare, over the years of life. Halve either and the bill halves. So the strongest case against me is both falling at once.

## Who regulates it?

The FCC licenses the radio links and checks the debris plans; nobody yet licenses orbital computing as such.

SpaceX's application, accepted for filing on 4 February 2026, asks for "up to one million satellites" between 500 and 2,000 kilometres. Amazon petitioned to deny it, as reported. SpaceX's letter of 29 May asks for the freedom, and a waiver, to dispose of satellites above 600 kilometres into higher Earth orbits or around the sun, rather than only by burning them up in the atmosphere.

The FCC adopted new satellite licensing rules on 22 July 2026, according to law-firm summaries, keeping its debris rules. If all million weighed the 3,000 kg filed for the lowest shells, that would be about three million tonnes in orbit, my arithmetic, so debris is not a footnote.

The SEC, the securities regulator, asked SpaceX in April 2026 for the "power-to-mass ratios" behind its goal and the "total system mass". The prospectus said the figures "continue to be refined". SpaceX's quarterly report to 30 September 2026 does not mention orbital computing.

## Who is paid if the kilograms are the bill?

Whoever charges by the kilogram, and whoever makes each kilogram do more.

**The launcher.** SpaceX flew both computing prototypes now in orbit, Starcloud's and Google's, and is paid per kilogram whoever's satellite goes up. It also designs its own computing satellite, which makes it toll keeper and competitor at once.

**The builders of the craft.** Astro Digital built Starcloud-1, and Planet built Google's prototype with Google. A lighter array and radiator is their whole edge. Redwire makes roll-out arrays; heat pipes and deployable radiators are a specialist trade.

**The chips.** Nvidia announced a space computing module in March 2026, and SpaceX said in August that Nvidia is helping design AI1's payload, as reported. Google designs its own TPUs. A chip that runs hotter makes the radiator smaller.

**The plug on the ground.** While orbit stays heavy, AI stays on the ground and the grid queue keeps its value. SpaceX's own risk factors warn that if "advances in nuclear energy" or similar ease ground constraints, its orbital computing "may be materially diminished". Its own computing today is on the ground: 1.7 gigawatts of nameplate capacity at the end of the third quarter, its quarterly report says.

## So who holds the scarce thing, and what should an investor watch?

In orbit the scarce thing is not power. It is mass to orbit, and the kilograms per kilowatt that decide how much of it each satellite needs.

If the claim is right, three parts of the chain gain. **The launcher**, paid per kilogram, gains whether orbit works or not. **The lightweight makers**, of arrays, radiators and heat pipes, gain if orbit works at all, because every kilogram they save is a launch fare saved. **The ground plug** keeps its value while orbit stays heavy.

The readings are specific. SpaceX's quarterly reports, for a satellite mass and kilowatts. Google's twin interconnected satellites, due in 2027, for a published mass and radiator. Starcloud-2, which its page says will be "fully operational in sun-synchronous orbit by 2027". And any published Starship price per kilogram.

## What would prove me wrong

Two observations would break the claim. An operator discloses, in a filing, a release or a regulator's record, a computing satellite in service at 100 kW or more of computing per tonne launched, by 31 December 2028. Or a launch provider publishes a price to low Earth orbit of $200 a kilogram or less by then.

The satellites that could be weighed against the target fly in 2027 and 2028. Gwynne Shotwell, SpaceX's president, said on its call of 20 October 2026 that it will begin flying Starmind satellites in 2027. SpaceX's page says its factory should enable production and deployment of thousands of satellites "starting as soon as late 2027". Google's pair is due in 2027.

A satellite mass in SpaceX's reports at or near 1.75 tonnes for 175 kW, or a published mass for Google's pair, would move me sooner. So would a flown array above 250 watts per kilogram, or a flown radiator several times lighter per square metre than the station's.

Designs would not move me. The preprint's 500 watts per kilogram assumes "custom solutions for all components". Musk calls 1,400 watts per square metre "a very achievable goal". Neither is a satellite in service.

The claim stands on two legs. The first, that a kilowatt in orbit is heavy, rests on physics and on the weights of flown hardware; a weighed satellite at target attacks it. The second, that the fare is high, rests on a price that reuse can move fast; a published $200 attacks it. The legs multiply, so a fall in both would break the idea even before either test is met.

Musk said in the interview SpaceX filed that "cooling is actually much easier in space than it is on Earth". I disagree, in part. Off the chip, perhaps: there is no dust and no humidity. Out to the world, heat can leave only as light, a few hundred to about 1,400 watts per square metre, and every square metre is launched.

At the scale of the chip, its temperature sets the radiator by the fourth power. At the scale of the satellite, the array uses most of a 10 kg budget, and the radiator between a fifth and all of it. At the scale of the fleet, 100 gigawatts a year needs "approximately one million metric tons to orbit annually", the prospectus says: about 10,000 Starship flights at 100 tonnes each, on my arithmetic. In orbit the sunlight is free, and the kilograms are the bill.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

**In orbit the sunlight is free and the kilograms are the bill** (2 November 2026)

Claim: "In orbit the sunlight is free but the kilograms that collect it and shed its heat are the bill: by 31 December 2028 no operator will report an AI compute satellite in service at SpaceX's own target of 100 kilowatts of compute power per metric ton launched, and no launch provider will publish a price to low Earth orbit at or below Google's $200 per kilogram threshold."

Breaks if: "By 31 December 2028, SpaceX, Starcloud, Google or any other operator discloses in a filing, release or regulator's record an orbital AI compute satellite in service at 100 kilowatts or more of compute power per metric ton of launched mass, or a launch provider publishes a list or contract price to low Earth orbit of $200 per kilogram or less."

This piece absorbs no earlier piece, so it carries no older claims.

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

**SpaceX's design.** SpaceX Starmind page, read 7 November 2026: "Compute payload Up to 250 kW peak / 175 kW average"; "Vehicle efficiency 75 kW / ton"; "Solar array 210 kW"; "Solar power density 250 W / m²"; "Deployable liquid radiator 160 m²"; wingspan 75 m; production "as soon as late 2027". SpaceX letter to the FCC, ICFS SAT-LOA-20260108-00016 (29 May 2026), table for shells below 600 km: mass 3,000 kg, total area 800 m², bus and radiator area 100 m². Interview transcripts filed with the SEC (9 June 2026): 250 W/m² solar, "about 1,400 watts per square meter for the radiators", "radiating on both sides", 150 kW peak and about 120 kW average, "About 5 megawatts per launch", "cooling is actually much easier in space than it is on Earth". Prospectus (424B4, 12 June 2026): radiation-only cooling, "over 100 kilowatts of compute power per metric ton", "approximately one million metric tons to orbit annually", mass "continue[s] to be refined". Roadshow (4 June 2026): "will not be easily repaired or upgraded"; useful life "inherently shorter"; "advances in nuclear energy". Third quarter release (20 October 2026): Starship Flight 14, first orbital flight, 26 Starlink V3 satellites. Third quarter call (20 October 2026, transcript): Starmind flights in 2027; 1.7 GW of ground compute. SEC staff letters (24 April and 19 May 2026). 10-Q, quarter to 30 September 2026: no mention of orbital compute.

**Radiators.** Flux is 2 × 0.92 × 5.67 × 10⁻⁸ × T⁴, T in kelvin: 581 W/m² at 0°C, 771 at 20°C, 1,069 at 45°C, about 1,094 near 47°C, 1,400 at 67°C, 2,023 at 100°C. Earth infrared on a two-sided panel edge-on to the Earth at 650 km: 2 × 0.92 × 0.241 × 239 = about 106 W/m²; 1,400 W/m² net then needs about 73°C. Starcloud white paper v1.03 (September 2024): 770.48 W/m² emitted, 122.94 from sunlight, 14.46 from the Earth, 633.08 net; with the Earth's infrared absorbed at emissivity 0.92, about 63 and 585, my arithmetic. NASA ISS Active Thermal Control System overview (undated): six radiator units of 1,122.64 kg, 23.3 m by 3.4 m, 70 kW; 96 kg per kW, about 147 W/m², 14.2 kg/m², my arithmetic. NASA Glenn, heat pipe and thermal technologies webinar (23 January 2025): ISS radiators about 9 kg/m²; heat-pipe radiators about 3 kg/m², tested 2011. Juhasz, NASA/TM-2008-215420 (October 2008): pumped-loop radiators "6 to 10 kg/m2". Radiator kg per kW at 1,400 W/m²: 3 kg/m² gives 2.1; 9 gives 6.4; 14.2 gives 10.1.

**Arrays and batteries.** Redwire ROSA product table (read 7 November 2026): beginning-of-life configurations from 3.3 kW and 36 kg to 37 kW and 521 kg, 71 to 124 W/kg, my arithmetic. NASA Small Spacecraft Technology State of the Art, power (7 May 2026): "~30 W/kg" cluster; lithium-ion cells "150-270 Wh/kg". Gaalema, Indyk and Staley (arXiv 2604.07760, 9 April 2026). Eclipse at 650 km in a dawn-dusk orbit: about 87 to 90 days a year, depending on the model, up to about 20 minutes per orbit, my arithmetic from a cylindrical shadow model; 175 kW for 20 minutes is about 58 kWh.

**The budget chart,** kg per kW, my arithmetic from the figures above: array 8 to 14; radiator 2.1 to 10; ground AI rack about 11, from a press figure of about 1.36 tonnes for a GB200 NVL72 rack at about 120 kW (The Register, 21 March 2024), a ceiling since a space payload sheds steel; eclipse batteries 1.2 to 2.2, cells only.

**Kilowatts per tonne.** 175 kW / 3.0 t = 58; 250 / 3.0 = 83; 5 MW / 100 t = 50. Google's paper, Table 1: Starlink V2 mini 575 kg, about 28 kW, 49 kW per tonne. Starcloud-1: 60 kg (Nvidia blog, 15 October 2025); 0.7 kW / 0.06 t = about 12, an upper bound since no power is published.

**Google.** Paper, arXiv 2511.19468, v1 22 November 2025, revised 17 June 2026; Google's blog of 1 October 2026 says a peer-reviewed version is in Joule. Orbit, 81-satellite cluster at 650 km, 10 mm aluminium shielding, 2 krad, 750 rad, "approximately one event/17 rad", "1 per 3 million inferences, assuming 1 inference per second", "10Tbps", TBIRD's "200Gbps", "$3,600/kg", the $200 threshold, "≲$200/kg by the mid-2030s", "∼180 Starship launches/year", about $300 at lower volume, $14,700 and $810 per kW per year, the ground range of $570 to $3,000. Silent errors per chip: 150 rad a year over 17 rad, about 9. Google blogs: 4 November 2025 (Beals: "up to 8 times", batteries), 1 October 2026 (launch), 30 October 2026 (Gemma 4 answer over Svalbard).

**What has flown.** Starcloud-1: Nvidia blog (15 October 2025); Astro Digital, Form 425 (29 September 2026). NPR (1 October 2026, corrected 2 October), as a press report: four TPUs, 15 minutes at a time, standard orbit with batteries. Three-Body constellation and Axiom nodes: press reports. FCC: DA 26-113 (4 February 2026); Report SAT-01982 (13 March 2026) for Starcloud's acceptance.

**Fleet.** One million satellites × 3,000 kg = 3 million tonnes; one million tonnes a year / 100 tonnes = 10,000 flights, my arithmetic.

</details>

<section class="exposure">
<h3>Who is exposed if the kilograms are the bill in orbit</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures and published estimates used as evidence for the mechanism.</p>
<dl>
<dt>The launcher and builders</dt>
<dd><span class="names">SpaceX</span> launches and designs its own computing satellite; <span class="names">Starcloud</span>, <span class="names">Astro Digital</span> and <span class="names">Planet Labs</span> build craft.</dd>
<dt>The light parts</dt>
<dd><span class="names">Redwire</span> makes roll-out solar arrays.</dd>
<dt>The chips</dt>
<dd><span class="names">Nvidia</span> and <span class="names">Google</span> design the chips orbital craft carry.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone counting orbital gigawatts announced as computing to come.</dd>
</dl>
</section>

---

<p class="sources">Sources: SpaceX's SEC filings, FCC letter and Starmind page; Google's Suncatcher paper and blogs; Starcloud's white paper and FCC application; NASA's space station, Glenn and small-satellite documents; Redwire; Nvidia; Astro Digital; FCC public notices; NPR and TechCrunch as press reports. Personal research, not investment advice.</p>
