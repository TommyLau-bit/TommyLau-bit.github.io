---
title: "Heat and water decide where AI goes: liquid to the chip, a choice on the roof"
date: 2026-08-21
summary: "AI data centres are blamed for drinking towns dry, yet a US government lab finds a liquid-cooled AI hall can stop evaporating water for almost no extra power over a year. Heat has forced cooling onto liquid at the chip, and Nvidia's newest rack takes that liquid at 45 degrees, warm enough for fans alone most hours. So water decides where and how each hall is cooled, not how many get built. The price of going dry is paid on the hottest afternoon, and the chillers for that afternoon are selling at record rates."
category: "Analysis"
format: "depth"
cover: "/covers/heat-and-water.svg"
tags: ["cooling", "data-centres", "liquid", "water"]
draft: false
updated: 2026-11-07
updateNote: "Rebuilt in depth: one watt of heat from the chip to the sky, every machine explained and drawn, with evidence to 7 November 2026."
---

<a id="heat-and-water"></a>

AI data centres are blamed for drinking towns dry. Yet a US government laboratory has found that a large liquid-cooled AI hall can stop evaporating water altogether, and barely change how much electricity it uses over a year.

That finding is the hinge of this piece. Heat decides how AI is cooled: with liquid, pressed against the chip. Water decides where and how that heat leaves the building, not how many halls get built. Liquid makes going without water cheap; it does not make it happen, and it does not make it free on the hottest afternoon.

So the claim is this. In AI data centres heat sets the cooling method, and water sets the roof and the site, not the count. Where an operator judges water scarce, it cools with air or recycled water, and I have found no powered AI campus cancelled over water rather than redesigned.

To see why, the piece follows the questions in order. Why every watt becomes heat, why air can no longer carry it, and how liquid takes it off the chip. Then how warm that liquid can run, the three ways to put heat into the sky, and what going dry costs. Then how water is counted, where most of it really goes, and what the four largest cloud operators do. Finally, the chillers, the worst afternoon, the towns, who is paid, and what would prove me wrong.

<details class="analogy">
<summary>The analogy</summary>
<p>Think of cooling down after a run. Sweat cools you by evaporating and works even on a hot day, but you must drink to replace it: that is the cooling tower. A fan on dry skin costs a little electricity and no water, but helps only while the air is cooler than you: that is the dry cooler.</p>
<p>On a sweltering afternoon the air is as warm as your skin, and the fan barely helps. Now picture skin at 45 degrees. The fan would win almost every day, and sweat, or an air conditioner, would be for the worst afternoons. Liquid at the chip gives the building that hot skin.</p>
</details>

<a id="cooling-is-half-the-job"></a>

## Why does every watt a chip uses become heat?

Because a chip does no lasting work in the physical world. It lifts nothing, moves nothing and stores almost nothing.

Electricity enters a server and leaves it as heat, apart from tiny amounts of light and signal that turn to heat nearby. So for cooling, a rack's power and its heat are the same number. A **watt** is one unit of energy each second, and a **kilowatt (kW)** is a thousand of them.

Nvidia, the leading AI chip designer, puts its GB200 NVL72 rack at about 120 kW in its user guide. A **rack** is the steel cabinet, about the size of a wardrobe, that holds a data centre's computers. That one cabinet releases as much heat as about eighty hairdryers on full, my arithmetic, and it does so all day and all night.

This is why cooling is half the job of an AI data centre. Every kilowatt the grid delivers to the chips must be carried back out of the building, or the chips slow down and then fail. The power piece of this journal follows the electricity in; this one follows the same energy out.

"Cooling" is really three jobs. At the chip, heat must be pulled off a small, very hot surface. Across the building, pumps and pipes carry that heat to the roof. Out of the building, it is released to the outside air. The first job is now settled for AI, and only the third can spend water.

## Why can air no longer carry the heat away?

Because air holds very little heat, so cooling a hot rack with air means moving enormous volumes of it.

A cubic metre of water carries about 3,600 times more heat than a cubic metre of air, for the same rise in temperature, my arithmetic from textbook values. That single ratio is most of the story of why liquid wins at high density.

To cool one kilowatt with air warming by 15 degrees across a server, about 120 cubic feet of air must pass every minute, my arithmetic. ASHRAE, the American body of heating and cooling engineers, gives the same scale. In a 2021 white paper it wrote that a 40 to 50 kW rack "could be up to 5000 cfm", cubic feet per minute, while the best floor tile delivers "1900 cfm".

So a 120 kW rack would need the air of about eight of the best floor tiles, pushed through one cabinet. Fans that hard eat power. ASHRAE found fans in dense servers using 10 to 20% of server power, against under 2% in many servers of the multicore era. Fan power rises roughly with the cube of fan speed, so pushing air harder gets expensive fast.

Fans also run on the same protected power as the chips. A rise from 2% to 10% fan power, ASHRAE noted, cuts the usable capacity of the protected supply by 8%. Every watt spent on fans is a watt the plug cannot give to computing.

<figure class="chart">
<p class="chart-title">One AI rack would need the air of eight of the best floor tiles</p>
<p class="chart-sub">Heat per rack, kilowatts, with the air needed to cool it in best-in-class floor tiles of 1,900 cubic feet a minute</p>
<svg viewBox="0 0 560 216" role="img" aria-label="Bar chart of heat per rack in kilowatts, with the air needed to cool it counted in best-in-class floor tiles of 1,900 cubic feet per minute. A typical rack in 2025, about 7.5 kilowatts, needs about half a tile. A dense air rack of 40 to 50 kilowatts, ASHRAE's 2021 example, needs up to 5,000 cubic feet per minute, about 2.6 tiles. Nvidia's GB200 NVL72, about 120 kilowatts, would need about 8 tiles. Vertiv's GB300 NVL72 design, up to 142 kilowatts, about 9 tiles."><g class="c-grid"><line x1="150.0" y1="32" x2="150.0" y2="196"/><line x1="215.0" y1="32" x2="215.0" y2="196"/><line x1="280.0" y1="32" x2="280.0" y2="196"/><line x1="345.0" y1="32" x2="345.0" y2="196"/><line x1="410.0" y1="32" x2="410.0" y2="196"/></g><g class="c-axis"><text x="150.0" y="26" text-anchor="middle">0 kW</text><text x="215.0" y="26" text-anchor="middle">40 kW</text><text x="280.0" y="26" text-anchor="middle">80 kW</text><text x="345.0" y="26" text-anchor="middle">120 kW</text><text x="410.0" y="26" text-anchor="middle">160 kW</text></g><text class="c-box-t" x="0" y="53">Typical rack, 2025</text><text class="c-note" x="0" y="68">survey average</text><rect class="c-bar c-mute" x="150" y="44" width="12.2" height="22" rx="2"/><text class="c-lab c-s1t" x="168.2" y="60">7.5 kW: half a tile</text><text class="c-box-t" x="0" y="95">Dense air rack</text><text class="c-note" x="0" y="110">ASHRAE, 2021</text><rect class="c-bar c-mute" x="150" y="86" width="73.1" height="22" rx="2"/><text class="c-lab c-s1t" x="229.1" y="102">40 to 50 kW: 2.6 tiles</text><text class="c-box-t" x="0" y="137">GB200 NVL72</text><text class="c-note" x="0" y="152">Nvidia user guide</text><rect class="c-bar" x="150" y="128" width="195.0" height="22" rx="2"/><text class="c-lab c-s1t" x="351.0" y="144">120 kW: about 8 tiles</text><text class="c-box-t" x="0" y="179">GB300 NVL72</text><text class="c-note" x="0" y="194">Vertiv's design</text><rect class="c-bar" x="150" y="170" width="230.8" height="22" rx="2"/><text class="c-lab c-s1t" x="386.8" y="186">142 kW: about 9 tiles</text><line class="c-base" x1="150" y1="32" x2="150" y2="196"/></svg>
<figcaption>Uptime Institute survey 2025, as reported by The Register; ASHRAE white paper (2021) for the dense air rack and the tile; Nvidia DGX GB200 User Guide; Vertiv's GB300 NVL72 datasheet, a design envelope, not an Nvidia figure. Tiles are my arithmetic at about 120 cubic feet a minute per kW.</figcaption>
</figure>

No standards body publishes one line where air stops working. The nearest anchor is ASHRAE's 40 to 50 kW rack at 5,000 cfm, more than two of the best floor tiles. Microsoft's cloud chief, Scott Guthrie, put it plainly on 18 September 2025: "Traditional air cooling can't handle the density of modern AI hardware."

## How does liquid take the heat off the chip?

Through a chain of sealed loops, each handing the heat to the next without the liquids ever mixing.

The first link is the **cold plate**: a copper block fixed onto the chip, with fine channels inside. Coolant runs through those channels and picks up the heat directly from the chip's surface. Nvidia's GB200 and GB300 compute trays carry cold plates on their processors, while network and storage parts stay on air.

The coolant in the rack's loop is not plain water. Nvidia describes it as "75% water and 25% propylene glycol" (21 June 2026). The glycol stops freezing and, with added inhibitors, keeps bacteria and corrosion out of fine channels.

That rack loop runs to a **coolant distribution unit (CDU)**: pumps, filters and a heat exchanger in one box. The heat exchanger passes the heat from the sealed rack loop into the building's own water, the **facility water**. The two liquids touch only through metal, like two pipes pressed side by side.

The CDU is the critical box in the room, so its reliability is watched closely. Google built its own, Project Deschutes, and reported fleet-wide CDU availability of about 99.999% since 2020 (30 April 2025). Carrier's chief executive described a CDU on 29 October 2026 as "effectively ... a mini-chiller".

The facility water then carries the heat to the roof, or to a yard beside the hall. There it meets the outside air, in the only step where water can be spent.

<figure class="illo">
<p class="illo-title">Only the last step can spend water</p>
<p class="illo-sub">One watt of heat, from an AI chip to the outside air, simplified</p>
<svg viewBox="0 0 940 262" role="img" aria-label="Drawing of one watt of heat travelling from an AI chip to the outside air in five steps. One: a copper cold plate on the chip, with coolant running through it. Two: the rack loop of water and glycol, entering at 45 degrees and leaving the chip at about 55. Three: the coolant distribution unit, pumps and a heat exchanger, where the rack loop hands its heat to the building water without the two mixing. Four: the facility water, arriving at the unit at about 41 degrees and carrying heat up to the roof. Five: the roof, a cooling tower or a dry cooler, where the heat leaves to the air. The first four steps are sealed loops that lose no water; only the fifth can spend water."><rect class="i-faint" x="16" y="34" width="719" height="160" rx="8"/><text class="i-cool-t" x="376" y="50" text-anchor="middle">sealed loops: no water lost</text><rect class="i-choke" x="775" y="34" width="160" height="160" rx="8"/><text class="i-hot-t" x="855" y="50" text-anchor="middle">can spend water</text><path class="i-hot" d="M142 96 H233"/><path class="i-hot" d="M226 91 l7 5 l-7 5"/><path class="i-cool" d="M233 150 H142"/><path class="i-cool" d="M149 145 l-7 5 l7 5"/><path class="i-hot" d="M337 96 H423"/><path class="i-hot" d="M416 91 l7 5 l-7 5"/><path class="i-cool" d="M423 150 H337"/><path class="i-cool" d="M344 145 l-7 5 l7 5"/><path class="i-hot" d="M527 96 H613"/><path class="i-hot" d="M606 91 l7 5 l-7 5"/><path class="i-cool" d="M613 150 H527"/><path class="i-cool" d="M534 145 l-7 5 l7 5"/><path class="i-hot" d="M717 96 H803"/><path class="i-hot" d="M796 91 l7 5 l-7 5"/><path class="i-cool" d="M803 150 H717"/><path class="i-cool" d="M724 145 l-7 5 l7 5"/><rect class="i-fill" x="44" y="140" width="92" height="28" rx="3"/><rect class="i-metal" x="64" y="122" width="52" height="18" rx="2"/><rect class="i-fill" x="56" y="88" width="68" height="34" rx="3"/><line class="i-thin" x1="64" y1="94" x2="64" y2="116"/><line class="i-thin" x1="77" y1="94" x2="77" y2="116"/><line class="i-thin" x1="90" y1="94" x2="90" y2="116"/><line class="i-thin" x1="103" y1="94" x2="103" y2="116"/><line class="i-thin" x1="116" y1="94" x2="116" y2="116"/><text class="i-k" x="90" y="82" text-anchor="middle">cold plate</text><rect class="i-fill" x="251" y="66" width="68" height="112" rx="3"/><rect class="i-fill" x="257" y="72" width="44" height="9" rx="1"/><rect class="i-fill" x="257" y="86" width="44" height="9" rx="1"/><rect class="i-fill" x="257" y="100" width="44" height="9" rx="1"/><rect class="i-fill" x="257" y="114" width="44" height="9" rx="1"/><rect class="i-fill" x="257" y="128" width="44" height="9" rx="1"/><rect class="i-fill" x="257" y="142" width="44" height="9" rx="1"/><rect class="i-fill" x="257" y="156" width="44" height="9" rx="1"/><line class="i-hot" x1="309" y1="70" x2="309" y2="174"/><line class="i-cool" x1="314" y1="70" x2="314" y2="174"/><rect class="i-fill" x="435" y="78" width="80" height="96" rx="4"/><circle class="i-metal" cx="459" cy="146" r="13"/><path class="i-line" d="M453 146 l6 -6 l6 6 l-6 6 z"/><path class="i-line" d="M483 90 l8 8 l-8 8 l8 8 l-8 8 l8 8 l-8 8 l8 8" style="fill:none"/><path class="i-line" d="M497 90 l8 8 l-8 8 l8 8 l-8 8 l8 8 l-8 8 l8 8" style="fill:none"/><line class="i-line" x1="615" y1="124" x2="715" y2="124"/><line class="i-hot" x1="657" y1="96" x2="657" y2="176"/><line class="i-cool" x1="673" y1="150" x2="673" y2="70"/><text class="i-n" x="681" y="78">to the roof</text><rect class="i-fill" x="799" y="112" width="112" height="44" rx="3"/><circle class="i-fill" cx="819" cy="100" r="13"/><line class="i-thin" x1="809" y1="100" x2="829" y2="100"/><circle class="i-fill" cx="855" cy="100" r="13"/><line class="i-thin" x1="845" y1="100" x2="865" y2="100"/><circle class="i-fill" cx="891" cy="100" r="13"/><line class="i-thin" x1="881" y1="100" x2="901" y2="100"/><line class="i-thin" x1="807" y1="118" x2="807" y2="150"/><line class="i-thin" x1="826" y1="118" x2="826" y2="150"/><line class="i-thin" x1="845" y1="118" x2="845" y2="150"/><line class="i-thin" x1="864" y1="118" x2="864" y2="150"/><line class="i-thin" x1="883" y1="118" x2="883" y2="150"/><line class="i-thin" x1="902" y1="118" x2="902" y2="150"/><path class="i-dash" d="M825 84 q6 -10 0 -20"/><path class="i-dash" d="M855 84 q6 -10 0 -20"/><path class="i-dash" d="M885 84 q6 -10 0 -20"/><text class="i-n" x="855" y="176" text-anchor="middle">tower or dry cooler</text><text class="i-hot-t" x="188" y="86" text-anchor="middle">about 55°C</text><text class="i-cool-t" x="188" y="170" text-anchor="middle">45°C in</text><text class="i-cool-t" x="570" y="170" text-anchor="middle">about 41°C</text><text class="i-t" x="90" y="216" text-anchor="middle">1. Chip</text><text class="i-n" x="90" y="234" text-anchor="middle">coolant runs through a</text><text class="i-n" x="90" y="250" text-anchor="middle">copper plate on the chip</text><text class="i-t" x="285" y="216" text-anchor="middle">2. Rack loop</text><text class="i-n" x="285" y="234" text-anchor="middle">water and glycol,</text><text class="i-n" x="285" y="250" text-anchor="middle">sealed inside the rack</text><text class="i-t" x="475" y="216" text-anchor="middle">3. CDU</text><text class="i-n" x="475" y="234" text-anchor="middle">pumps and a heat exchanger;</text><text class="i-n" x="475" y="250" text-anchor="middle">the liquids never mix</text><text class="i-t" x="665" y="216" text-anchor="middle">4. Facility water</text><text class="i-n" x="665" y="234" text-anchor="middle">the building's loop</text><text class="i-n" x="665" y="250" text-anchor="middle">carries heat upward</text><text class="i-t" x="855" y="216" text-anchor="middle">5. The roof</text><text class="i-n" x="855" y="234" text-anchor="middle">heat leaves to the air;</text><text class="i-n" x="855" y="250" text-anchor="middle">water is spent only here</text></svg>
<figcaption>Nvidia (16 March and 21 June 2026) for the temperatures and the coolant; Google (30 April 2025) on its own CDU. My drawing.</figcaption>
</figure>

There is a side branch: **immersion**, where whole servers sit in a bath of non-conducting liquid. Microsoft ran one rack of two-phase immersion in production at Quincy, Washington, in 2021. But the fluids that boil in two-phase tanks are PFAS chemicals, and 3M finished leaving PFAS manufacturing at the end of 2025. Nvidia's racks are built around cold plates, so for AI in 2026 cold plates are the mainstream and immersion a niche.

## How warm can the coolant run, and why does that matter?

Much warmer than most people expect, and every degree of warmth matters later, on the roof.

A chip tolerates a hot surface. The silicon itself runs at around 85 to 105 degrees, so coolant can be far cooler than the chip and still take its heat. The better the path from chip to coolant, the warmer the coolant may run for the same chip temperature.

Nvidia has written that warmth into its specification. Its racks for Vera Rubin, which Nvidia said in March would ship in the second half of 2026, are "designed to operate with 45°C (113°F) warm-water inlet temperatures" (16 March 2026). The coolant enters the chip at 45 degrees and "exits at roughly 55 degrees" (21 June 2026). For scale, Nvidia notes that "hot tubs sit at about 38 to 40 degrees Celsius".

Note which loop that is. The 45 degrees is the rack's own loop. The building's water can arrive at the CDU at about 41 degrees, Nvidia's design says, since the heat exchanger needs a few degrees of gap to work.

Rubin also removes the fans. Nvidia says its Blackwell systems run with "about 20% of capacity air-cooled", while Vera Rubin moves "to 100% liquid cooling" (25 March 2026). Its compute trays are "fanless". The hall keeps some air load in storage and network racks, but the AI rack itself no longer blows air.

ASHRAE names classes of facility water by their top temperature. In 2021 it renamed them W17, W27, W32, W40, W45 and W+, each number the warmest supply water the equipment must run on at full speed. Nvidia's 41 degree supply sits inside the W45 class.

That is a reversal worth noticing. In the same 2021 paper ASHRAE expected hotter chips to need colder water: future products "only capable of W32" and, eventually, temperatures "down into the W27 (W2) range". It warned that W45 water "will become increasingly difficult to use as the heat flux at the socket increases". Five years later the hottest rack on the market was designed to run on 45 degree coolant. Nvidia credits a tighter path from die to water.

Why it matters: Nvidia says running colder means "diverting a larger share of the facility's limited grid allocation into cooling instead of compute" (25 March 2026). The same post claims 45 degree cooling unlocks "up to 10% additional NVL72 racks", and elsewhere "up to 30% more GPUs", in the same power budget (16 March 2026). Those are the vendor's own estimates, not a measurement, but the direction follows from the physics below.

<a id="room-to-spare"></a>

## Can an old air-cooled hall take liquid?

Yes, but as a refit, and the refit is the slow part.

Jane Street, a trading firm, shows the refit. Its write-up of one of its new Texas data centres describes "4,032 GPUs across 56 racks, retrofitted for liquid cooling". The write-up gives no detail of the refit, but "retrofitted" means the liquid loop was added to a hall already standing. Its power comes on a fixed allocation from its utility, as told in [power first, chips last](/journal/america-rations-the-plug/#power-first-chips-last).

Its head of physical engineering, Dan Pontecorvo, described Jane Street's roof chillers on a podcast (25 July 2025). They blow outside air over coils, and he said they lose heat transfer ability once the returning water gets too warm. He recalled racks of 10 to 15 kW counting as dense; designs now plan for about 170 kW a rack.

The largest operators found the same wall. Amazon Web Services, Amazon's cloud arm, built its own in-row heat exchanger for AI racks, because liquid-ready new buildings would have taken years, the press reported in July 2025. Meta runs liquid-cooled racks inside air-cooled halls with heat exchangers at the rack. Both are bridges: liquid at the chip, air still in the room.

A hall designed for liquid from the start skips the bridge. It lays out pipes, CDUs and roof plant for warm water, and it can choose its roof without the old one's limits.

## What are the three ways to put heat into the outside air?

Sweat, a fan, and a fridge: a cooling tower, a dry cooler and a chiller. They differ in water, power and one key temperature.

A **cooling tower** sprays the warm water over packing while fans pull air through it. A small part evaporates and carries heat away with it. Evaporating one kilogram of water absorbs about 2,430 kilojoules, so shedding a kilowatt-hour of heat purely by evaporation takes about 1.5 litres, my arithmetic.

A tower loses more than it evaporates. Minerals left behind must be drained as **blowdown**, and droplets escape as **drift**. The US energy department's guidance puts it as "Make-Up = Evaporation + Blowdown + Drift". Many towers run at "two to four cycles of concentration", meaning blowdown adds a third or more to the evaporation.

The tower's great advantage is temperature. Evaporation can cool water below the air's own temperature, towards the **wet-bulb temperature**: what a thermometer wrapped in a wet cloth reads. In dry desert air at 40 degrees, the wet bulb can be about 20 to 24. Humid Singapore's is much closer to its air temperature.

A **dry cooler** is a large radiator with fans. The water stays sealed inside its coil, so none is lost, but it can only cool the water to a few degrees above the air: the **dry-bulb temperature**, the ordinary reading. On a 40 degree afternoon, a dry cooler cannot make water cooler than about 45.

Between them sits **adiabatic assist**: a dry cooler that wets pads in front of its coil on hot hours. It spends water only when it must, and much less than a tower over a year.

A **chiller** is a refrigerator for water. A compressor pumps heat from the loop to a hotter coil, so it can make water colder than the outside air, at the price of electricity. An **air-cooled chiller** throws that heat out with fans and uses no water. A **water-cooled chiller** throws it into a tower, which evaporates water.

How much electricity? A chiller's **coefficient of performance** is heat moved per unit of power used. A Vertiv datasheet for one air-cooled model gives about 4.2 to 4.6 at 35 degree outside air, so removing 1 kW of heat costs about a quarter of a kilowatt, and more as the air gets hotter.

<figure class="illo">
<p class="illo-title">The tower saves power with water; the dry cooler saves water with power</p>
<p class="illo-sub">Three machines that reject a data centre's heat, simplified</p>
<svg viewBox="0 0 940 294" role="img" aria-label="Drawing of three machines that put a data centre's heat into the outside air. A cooling tower sprays water over packing and evaporates about 1 to 2 litres per kilowatt-hour of heat; it can cool water below the air temperature, towards the wet-bulb temperature, for little power. A dry cooler is a radiator with fans; it uses no water but can only cool water to a few degrees above the air, and its fans use more power when it is hot. A chiller uses a compressor to make water colder than the air; an air-cooled chiller uses no water, and at 35 degree air it costs about a quarter of a kilowatt for each kilowatt of heat removed."><text class="i-head" x="10" y="20">Three ways to put the heat into the sky</text><rect class="i-ground" x="10" y="170" width="920" height="6"/><path class="i-fill" d="M100 170 L114 70 H206 L220 170 Z"/><line class="i-thin" x1="116" y1="110" x2="204" y2="110"/><line class="i-thin" x1="120" y1="124" x2="200" y2="124"/><line class="i-thin" x1="124" y1="138" x2="196" y2="138"/><line class="i-thin" x1="128" y1="152" x2="192" y2="152"/><circle class="i-fill" cx="160" cy="62" r="16"/><line class="i-thin" x1="148" y1="62" x2="172" y2="62"/><path class="i-dash" d="M138 42 q8 -10 0 -22"/><path class="i-dash" d="M160 42 q8 -10 0 -22"/><path class="i-dash" d="M182 42 q8 -10 0 -22"/><text class="i-cool-t" x="230" y="40">vapour</text><path class="i-fill" d="M380 80 L450 170 H490 L560 80 Z"/><line class="i-thin" x1="390" y1="92" x2="550" y2="92"/><line class="i-thin" x1="400" y1="108" x2="540" y2="108"/><line class="i-thin" x1="410" y1="124" x2="530" y2="124"/><line class="i-thin" x1="420" y1="140" x2="520" y2="140"/><line class="i-thin" x1="430" y1="156" x2="510" y2="156"/><circle class="i-fill" cx="420" cy="66" r="16"/><line class="i-thin" x1="408" y1="66" x2="432" y2="66"/><circle class="i-fill" cx="470" cy="66" r="16"/><line class="i-thin" x1="458" y1="66" x2="482" y2="66"/><circle class="i-fill" cx="520" cy="66" r="16"/><line class="i-thin" x1="508" y1="66" x2="532" y2="66"/><rect class="i-fill" x="690" y="86" width="180" height="84" rx="4"/><circle class="i-metal" cx="732" cy="132" r="22"/><text class="i-k" x="732" y="136" text-anchor="middle">comp</text><circle class="i-fill" cx="792" cy="72" r="16"/><line class="i-thin" x1="780" y1="72" x2="804" y2="72"/><circle class="i-fill" cx="838" cy="72" r="16"/><line class="i-thin" x1="826" y1="72" x2="850" y2="72"/><path class="i-hot" d="M784 132 H856"/><path class="i-cool" d="M784 150 H856"/><text class="i-t" x="160" y="204" text-anchor="middle">Cooling tower</text><text class="i-cool-t" x="160" y="224" text-anchor="middle">evaporates about 1 to 2 L per kWh</text><text class="i-n" x="160" y="244" text-anchor="middle">cools water below the air,</text><text class="i-n" x="160" y="260" text-anchor="middle">towards the wet bulb</text><text class="i-hot-t" x="160" y="282" text-anchor="middle">little power</text><text class="i-t" x="470" y="204" text-anchor="middle">Dry cooler</text><text class="i-cool-t" x="470" y="224" text-anchor="middle">uses no water</text><text class="i-n" x="470" y="244" text-anchor="middle">cools water only to a few</text><text class="i-n" x="470" y="260" text-anchor="middle">degrees above the air</text><text class="i-hot-t" x="470" y="282" text-anchor="middle">fan power, more when hot</text><text class="i-t" x="780" y="204" text-anchor="middle">Chiller</text><text class="i-cool-t" x="780" y="224" text-anchor="middle">air-cooled: no water</text><text class="i-n" x="780" y="244" text-anchor="middle">makes water colder than the</text><text class="i-n" x="780" y="260" text-anchor="middle">air with a compressor</text><text class="i-hot-t" x="780" y="282" text-anchor="middle">about 0.25 kW per kW at 35°C</text></svg>
<figcaption>US Department of Energy cooling tower guidance; Lawrence Berkeley National Laboratory (December 2024) for the tower's water; Vertiv Liebert AFC datasheet for the chiller at 35°C. The tower's 1 to 2 litres spans Nvidia's figure and the laboratory's median. My drawing.</figcaption>
</figure>

## Why does warm coolant let fans do most of the work?

Because a dry cooler works whenever the outside air is a few degrees cooler than the water, and warm water makes that almost always true.

Take an old air-cooled hall with chilled water at about 18 degrees, already warm by older standards. A dry cooler alone could do the job only when the outside air was below about 10 to 13. On most days the chiller had to run. My arithmetic assumes a gap of 5 to 8 degrees across the dry cooler, typical practice rather than a sourced figure.

Now take Nvidia's design, with the building's water at about 41 degrees. The same dry cooler does the job alone whenever the air is below about 33 to 36 degrees. In many climates that is nearly every hour of the year, though not in the hottest deserts.

Nvidia's own words match. Its cooling director, Ali Heydari, says on its blog that chillers may be needed in "maybe 1% of the year", and only "in some climates" (21 June 2026). The same post, linking to ENERGY STAR, says raising chiller plant temperatures by one degree "can cut cooling energy costs by about 4%".

One per cent of a year is about 88 hours. They are not random hours. They are the hottest afternoons, which come back later in this piece.

<figure class="illo">
<p class="illo-title">At 41 degrees, a dry cooler needs no help for most hours of the year in many climates</p>
<p class="illo-sub">Coolant temperatures, and the outside air at which a dry cooler alone does the job</p>
<svg viewBox="0 0 940 330.0" role="img" aria-label="Drawing of a temperature scale from 0 to 60 degrees. Coolant temperatures are marked: about 55 degrees out of the chip, 45 into the rack, about 41 for the building water, and about 18 for an old air-cooled hall's chilled water. Two shaded columns show the outside air temperatures at which a dry cooler alone can do the job, assuming a gap of 5 to 8 degrees: for the old air hall, below about 10 to 13 degrees; for a hall with 41 degree water, below about 33 to 36 degrees, which in many climates is nearly every hour of the year, though not in the hottest deserts."><text class="i-head" x="10" y="20">Each degree of coolant adds hours when fans alone can do the job</text><line class="i-line" x1="150" y1="300.0" x2="150" y2="50.0"/><line class="i-thin" x1="144" y1="300" x2="150" y2="300"/><text class="i-n" x="140" y="304" text-anchor="end">0°C</text><line class="i-thin" x1="144" y1="258" x2="150" y2="258"/><text class="i-n" x="140" y="262" text-anchor="end">10°C</text><line class="i-thin" x1="144" y1="217" x2="150" y2="217"/><text class="i-n" x="140" y="221" text-anchor="end">20°C</text><line class="i-thin" x1="144" y1="175" x2="150" y2="175"/><text class="i-n" x="140" y="179" text-anchor="end">30°C</text><line class="i-thin" x1="144" y1="133" x2="150" y2="133"/><text class="i-n" x="140" y="137" text-anchor="end">40°C</text><line class="i-thin" x1="144" y1="92" x2="150" y2="92"/><text class="i-n" x="140" y="96" text-anchor="end">50°C</text><line class="i-thin" x1="144" y1="50" x2="150" y2="50"/><text class="i-n" x="140" y="54" text-anchor="end">60°C</text><line class="i-thin" x1="150" y1="71" x2="168" y2="71"/><circle class="i-hot-f" cx="150" cy="71" r="4"/><text class="i-hot-t" x="174" y="75">out of the chip, about 55°C</text><line class="i-thin" x1="150" y1="112" x2="168" y2="112"/><circle class="i-hot-f" cx="150" cy="112" r="4"/><text class="i-hot-t" x="174" y="116">into the rack, 45°C</text><line class="i-thin" x1="150" y1="129" x2="168" y2="129"/><circle class="i-hot-f" cx="150" cy="129" r="4"/><text class="i-hot-t" x="174" y="133">building water, about 41°C</text><line class="i-thin" x1="150" y1="225" x2="168" y2="225"/><circle class="i-cool-f" cx="150" cy="225" r="4"/><text class="i-cool-t" x="174" y="229">old air hall's chilled water, about 18°C</text><rect class="i-cool-f" x="524" y="258" width="72" height="42" rx="2" style="opacity:.35"/><rect class="i-cool-f" x="524" y="246" width="72" height="12" rx="2" style="opacity:.18"/><line class="i-dash" x1="150" y1="246" x2="596" y2="246"/><text class="i-t" x="560" y="216" text-anchor="middle">Old air hall</text><text class="i-n" x="560" y="234" text-anchor="middle">fans alone below about 10 to 13°C</text><rect class="i-cool-f" x="764" y="162" width="72" height="138" rx="2" style="opacity:.35"/><rect class="i-cool-f" x="764" y="150" width="72" height="12" rx="2" style="opacity:.18"/><line class="i-dash" x1="150" y1="150" x2="836" y2="150"/><text class="i-t" x="800" y="120" text-anchor="middle">Hall at 41°C water</text><text class="i-n" x="800" y="138" text-anchor="middle">fans alone below about 33 to 36°C</text><text class="i-n" x="680" y="320" text-anchor="middle">shaded: outside air temperatures at which a dry cooler needs no chiller</text></svg>
<figcaption>Nvidia (16 March and 21 June 2026) for the coolant temperatures. The 18°C chilled water and the 5 to 8 degree gap across the dry cooler are typical practice, my assumptions. My drawing.</figcaption>
</figure>

## What does going dry cost a liquid-cooled hall?

Over a year, almost nothing in power, on the best public model. That is the US government laboratory's finding.

Lawrence Berkeley National Laboratory (LBNL), which studies energy for the US government, published its national data centre report in December 2024. It simulated nine cooling designs across 965 American weather stations, in over a million runs. Its results are yearly averages, and its liquid halls run at ASHRAE's W45 class.

The measure of power is **PUE**, power usage effectiveness: total power entering the building divided by power reaching the computers. At 1.1 the overhead for cooling and losses is a tenth. The measure of water is **WUE**, water usage effectiveness: litres of water per kWh of computing.

For a large liquid-cooled hall, the lab's medians, as I read them from its Figure 4.4, are close. With a cooling tower, PUE is about 1.13 and the hall consumes about 2.0 litres of water per kWh. With a dry cooler backed by an air-cooled chiller, PUE is about 1.10 and water is zero; that yearly figure already includes the chiller's hot hours. With adiabatic assist, about 1.10 and 0.13 litres.

So on the lab's medians the dry liquid hall is not worse in power than the wet one; if anything a shade better. The lab's own words: the higher temperature of liquid cooling means "less chiller run hours and less adiabatic assist".

An air-cooled hall is different. A midsize air hall with a water-cooled chiller and tower runs at about 1.52 and consumes about 2.9 litres. Swap to an air-cooled chiller and PUE rises to about 1.83 for near-zero water. Swap instead to a dry cooler backed by an air-cooled chiller and PUE is about 1.6. Dropping the tower costs an air hall 0.1 to 0.3 of PUE, depending on what replaces it.

<figure class="chart">
<p class="chart-title">In a liquid hall, going dry costs almost nothing in yearly power</p>
<p class="chart-sub">Simulated yearly medians: PUE, and water evaporated on site per kWh of computing</p>
<svg viewBox="0 0 560 302" role="img" aria-label="Paired bar charts of simulated yearly medians from Lawrence Berkeley National Laboratory. Midsize air-cooled hall: with a cooling tower, PUE about 1.52 and about 2.9 litres of water evaporated per kilowatt-hour; with an air-cooled chiller, about 1.83 and near zero water; with a dry cooler backed by an air-cooled chiller, about 1.6 and near zero. Large liquid-cooled hall: with a cooling tower, about 1.13 and 2.0 litres; dry cooler with adiabatic assist, about 1.10 and 0.13 litres; dry cooler backed by an air-cooled chiller, about 1.10 and no water."><g class="c-grid"><line x1="172.0" y1="42" x2="172.0" y2="276"/><line x1="252.0" y1="42" x2="252.0" y2="276"/><line x1="332.0" y1="42" x2="332.0" y2="276"/><line x1="366.0" y1="42" x2="366.0" y2="276"/><line x1="418.7" y1="42" x2="418.7" y2="276"/><line x1="471.3" y1="42" x2="471.3" y2="276"/><line x1="524.0" y1="42" x2="524.0" y2="276"/></g><g class="c-axis"><text x="172.0" y="292" text-anchor="middle">1</text><text x="252.0" y="292" text-anchor="middle">1.5</text><text x="332.0" y="292" text-anchor="middle">2</text><text x="366.0" y="292" text-anchor="middle">0</text><text x="418.7" y="292" text-anchor="middle">1</text><text x="471.3" y="292" text-anchor="middle">2</text><text x="524.0" y="292" text-anchor="middle">3</text></g><text class="c-lab c-s2t" x="172" y="20">PUE, yearly</text><text class="c-lab c-s2t" x="366" y="20">Water on site, litres per kWh</text><text class="c-box-t" x="0" y="64">Air-cooled hall, midsize</text><text class="c-note" x="0" y="91">With a cooling tower</text><rect class="c-bar c-mute" x="172" y="78" width="83.2" height="18" rx="2"/><text class="c-lab c-s1t" x="260.2" y="91">1.52</text><rect class="c-bar c-mute" x="366" y="78" width="152.7" height="18" rx="2"/><text class="c-lab c-s1t" x="523.7" y="91">2.9</text><text class="c-note" x="0" y="121">Air-cooled chiller</text><rect class="c-bar c-mute" x="172" y="108" width="132.8" height="18" rx="2"/><text class="c-lab c-s1t" x="309.8" y="121">1.83</text><rect class="c-bar c-mute" x="366" y="108" width="2.6" height="18" rx="2"/><text class="c-lab c-s1t" x="373.6" y="121">near 0</text><text class="c-note" x="0" y="151">Dry cooler, chiller backup</text><rect class="c-bar c-mute" x="172" y="138" width="96.0" height="18" rx="2"/><text class="c-lab c-s1t" x="273.0" y="151">1.60</text><rect class="c-bar c-mute" x="366" y="138" width="2.6" height="18" rx="2"/><text class="c-lab c-s1t" x="373.6" y="151">near 0</text><text class="c-box-t" x="0" y="180">Liquid-cooled hall, large</text><text class="c-note" x="0" y="207">With a cooling tower</text><rect class="c-bar" x="172" y="194" width="20.8" height="18" rx="2"/><text class="c-lab c-s1t" x="197.8" y="207">1.13</text><rect class="c-bar" x="366" y="194" width="105.3" height="18" rx="2"/><text class="c-lab c-s1t" x="476.3" y="207">2.0</text><text class="c-note" x="0" y="237">Dry cooler, adiabatic assist</text><rect class="c-bar" x="172" y="224" width="16.0" height="18" rx="2"/><text class="c-lab c-s1t" x="193.0" y="237">1.10</text><rect class="c-bar" x="366" y="224" width="6.8" height="18" rx="2"/><text class="c-lab c-s1t" x="377.8" y="237">0.1</text><text class="c-note" x="0" y="267">Dry cooler, chiller backup</text><rect class="c-bar" x="172" y="254" width="16.0" height="18" rx="2"/><text class="c-lab c-s1t" x="193.0" y="267">1.10</text><rect class="c-bar" x="366" y="254" width="1.5" height="18" rx="2"/><text class="c-lab c-s1t" x="371.0" y="267">none</text></svg>
<figcaption>Lawrence Berkeley National Laboratory, December 2024, Figure 4.4: medians as I read them from its chart, rounded. Yearly averages from typical weather; the laboratory publishes no worst-hour figure.</figcaption>
</figure>

Two warnings travel with these numbers. First, they are annual averages from typical weather. The lab publishes no worst-hour figure, and the worst hour is where a dry roof is weakest.

Second, the lab itself is cautious: its PUEs "assume systems are commissioned and operate as designed. This is rarely the case." And it warns that low site water "does not imply" good: "While air-cooled chillers use no water, they use more energy." In a liquid hall, though, the extra energy is small.

## How is water counted, and why do the numbers disagree?

Because companies count different things, and the words sound alike.

**Withdrawal** is all the water a site takes in, from a utility, a well or a river. **Discharge** is what it sends back, mostly to the sewer. **Consumption** is withdrawal minus discharge: water lost to the local system, mostly as vapour from towers. A town feels consumption most, since withdrawn water that comes back can be used again downstream.

WUE then divides one of those by the energy used by the computers, and each company picks its own numerator. Amazon Web Services divides water withdrawn. Meta divides water withdrawn. Microsoft divides water consumed for cooling and humidification. The lab counts water consumed.

So AWS's 0.12 litres per kWh in 2025, Meta's 0.19 in 2024 and Microsoft's 0.27 in its fiscal year to June 2025 are not one scale. Nor is Google's figure, which it gives as total gallons by site rather than as a ratio. Ranking them would be a mistake.

"High risk" differs too. Google rates each data centre's water source with its own framework, as low, medium or high risk of depletion or scarcity. Microsoft uses "water stress" from public datasets. AWS and Meta use the World Resources Institute's Aqueduct index. The four labels are not comparable.

## Where is most of a data centre's water: on the roof, or at the power station?

On a national average, at the power station, by about twelve to one. But that average needs three warnings before it carries any weight.

The lab estimates that American data centres consumed 66 billion litres of water on site in 2023. The power stations making their electricity consumed "nearly 800 billion liters". Per kWh a data centre bought, that is a "national average of 4.52 L/kWh", my check: 800 billion over 176 terawatt-hours.

So PUE is also a water number. Each kWh of computing buys PUE kWh from the grid, and each of those carries the power station's water. A hall's whole water bill, on the lab's averages, is its roof water plus PUE times 4.52 litres. The sum is mine, built only from the lab's numbers.

<figure class="chart">
<p class="chart-title">Counted whole, a dry liquid hall uses about half the water of an air hall with a tower</p>
<p class="chart-sub">Water consumed per kWh of computing, litres: at the power station for the electricity bought, plus on the roof</p>
<svg viewBox="0 0 560 232" role="img" aria-label="Stacked bar chart of water consumed per kilowatt-hour of computing, in litres, at the power station plus on the roof, my arithmetic from the laboratory's medians and its national average of 4.52 litres per kilowatt-hour bought. Midsize air hall with a tower: about 6.9 at the power station plus 2.9 on the roof, about 9.8 in all. Air hall with an air-cooled chiller: about 8.3, all at the power station. Large liquid hall with a tower: about 5.1 plus 2.0, about 7.1. Large liquid hall with a dry cooler: about 5.0, all at the power station."><rect class="c-bar c-mute" x="0" y="8" width="12" height="12" rx="2"/><text class="c-note" x="18" y="18">at the power station</text><rect class="c-bar c-alt" x="160" y="8" width="12" height="12" rx="2"/><text class="c-note" x="178" y="18">on the roof</text><g class="c-grid"><line x1="190.0" y1="52" x2="190.0" y2="216"/><line x1="252.0" y1="52" x2="252.0" y2="216"/><line x1="314.0" y1="52" x2="314.0" y2="216"/><line x1="376.0" y1="52" x2="376.0" y2="216"/><line x1="438.0" y1="52" x2="438.0" y2="216"/><line x1="500.0" y1="52" x2="500.0" y2="216"/></g><g class="c-axis"><text x="190.0" y="46" text-anchor="middle">0 L</text><text x="252.0" y="46" text-anchor="middle">2 L</text><text x="314.0" y="46" text-anchor="middle">4 L</text><text x="376.0" y="46" text-anchor="middle">6 L</text><text x="438.0" y="46" text-anchor="middle">8 L</text><text x="500.0" y="46" text-anchor="middle">10 L</text></g><text class="c-box-t" x="0" y="73">Air hall, tower</text><text class="c-note" x="0" y="88">midsize, PUE 1.52</text><rect class="c-bar c-mute" x="190" y="64" width="213.0" height="22" rx="2"/><rect class="c-bar c-alt" x="403.0" y="64" width="89.9" height="22" rx="2"/><text class="c-lab c-s1t" x="498.9" y="80">9.8</text><text class="c-box-t" x="0" y="115">Air hall, air-cooled chiller</text><text class="c-note" x="0" y="130">midsize, PUE 1.83</text><rect class="c-bar c-mute" x="190" y="106" width="256.4" height="22" rx="2"/><text class="c-lab c-s1t" x="452.4" y="122">8.3</text><text class="c-box-t" x="0" y="157">Liquid hall, tower</text><text class="c-note" x="0" y="172">large, PUE 1.13</text><rect class="c-bar c-mute" x="190" y="148" width="158.3" height="22" rx="2"/><rect class="c-bar c-alt" x="348.3" y="148" width="62.0" height="22" rx="2"/><text class="c-lab c-s1t" x="416.3" y="164">7.1</text><text class="c-box-t" x="0" y="199">Liquid hall, dry cooler</text><text class="c-note" x="0" y="214">large, PUE 1.10</text><rect class="c-bar c-mute" x="190" y="190" width="154.1" height="22" rx="2"/><text class="c-lab c-s1t" x="350.1" y="206">5.0</text><line class="c-base" x1="190" y1="52" x2="190" y2="216"/></svg>
<figcaption>My arithmetic from Lawrence Berkeley National Laboratory, December 2024: roof water and PUE from its Figure 4.4 medians; power station water is PUE times its national average of 4.52 litres per kWh bought, which includes hydroelectric reservoirs and ignores power contracts.</figcaption>
</figure>

On that sum, a midsize air hall with a tower uses about 9.8 litres per kWh in all, and a large dry liquid hall about 5.0. The comparison sets a midsize air hall against a large liquid one, so size accounts for part of the gap. In the air hall, dropping the tower saves 2.9 litres on the roof but spends about 1.4 again at the power station, through a higher PUE. In the liquid hall, the roof saving is kept almost whole.

Now the warnings. The first is that the 4.52 is a grid average for where data centres sat in 2023. It includes evaporation from hydroelectric reservoirs, whose water serves many purposes. A gas plant with a cooling tower consumes nearer 0.75 litres per kWh; wind and solar close to none.

The second is that the lab's method ignores power contracts and on-site generation. Meta publishes both views. On its grid's average, the water embedded in its electricity was 72,207 megalitres in 2024, about 23 times its direct use. Counting only its contracted renewables, it was 5,075 megalitres, about 1.6 times.

The third is geography. The power station's water is usually in another basin, often a river drawn and returned. A town sees the site's draw, not the plant's. So "most of the water is at the power station" is true on paper, and it does not answer the question a town is asking.

<a id="water-is-a-siting-problem"></a>

## What do the largest cloud operators actually do?

They evaporate where they judge water plentiful, and cool with air where they judge it scarce. Google says so in writing; the others show it in their designs.

**Google** consumed 10,523 million gallons of water at its data centres in 2025, about 40 billion litres, on its 2026 Environmental Report. About 81% of what its data centres withdrew was drinking-quality water, my arithmetic. Its company-wide consumption rose 34% in the year. Google says water cooling "requires less energy than air-cooling technologies", and it uses it where water allows.

It publishes consumption site by site. Council Bluffs, Iowa, its largest, consumed 1,346.0 million gallons in 2025; The Dalles, Oregon, 469.0. Google rated The Dalles' sources as not at high risk in 2022, and it cools there with water.

Where it judged water scarce, it chose air. In its 2025 report Google said the sources at Waltham Cross, in England, "present a high risk of water depletion and scarcity", so it "decided to utilize air cooling technology". It said it was taking "a similar approach" at Mesa, Arizona, and Canelones, Uruguay, then under development.

On 3 June 2026 Google made it policy: "If a water source is at high risk, we choose air cooling or recycled water." It also wrote that in many places water cooling can cut a data centre's energy use by "approximately 10%" against air. That sentence prices the trade across Google's fleet: about a tenth more energy to save the water, more than the lab finds for a liquid hall.

Mesa now has a row: 9.7 million gallons consumed in 2025, its first listed year, against 469.0 at The Dalles. But Mesa carries no "air-cooled facility" footnote in the 2026 table, unlike Phoenix and seven others, and it withdrew 19.4 million gallons. Google has not said why. Waltham Cross and Canelones have no row of their own yet.

<figure class="chart">
<p class="chart-title">Where Google judged the water scarce, it used almost none</p>
<p class="chart-sub">Water consumed in 2025 at four Google campuses, millions of gallons</p>
<svg viewBox="0 0 560 220" role="img" aria-label="Bar chart of water consumed in 2025 at four Google campuses, in millions of gallons. The Dalles, Oregon, where Google judged the water not at high risk, 469.0. Henderson, Nevada, a desert site whose source rating Google does not publish, 239.4. Quilicura, Santiago, Chile, which evaporates water, 143.0. Mesa, Arizona, which Google named as high water risk, 9.7. A dashed line marks the claim's limit of 50 million gallons a year."><g class="c-grid"><line x1="170.0" y1="32" x2="170.0" y2="196"/><line x1="236.8" y1="32" x2="236.8" y2="196"/><line x1="303.6" y1="32" x2="303.6" y2="196"/><line x1="370.4" y1="32" x2="370.4" y2="196"/><line x1="437.2" y1="32" x2="437.2" y2="196"/><line x1="504.0" y1="32" x2="504.0" y2="196"/></g><g class="c-axis"><text x="170.0" y="26" text-anchor="middle">0</text><text x="236.8" y="26" text-anchor="middle">100</text><text x="303.6" y="26" text-anchor="middle">200</text><text x="370.4" y="26" text-anchor="middle">300</text><text x="437.2" y="26" text-anchor="middle">400</text><text x="504.0" y="26" text-anchor="middle">500</text></g><text class="c-box-t" x="0" y="53">The Dalles, Oregon</text><text class="c-note" x="0" y="68">water judged not high risk</text><rect class="c-bar c-mute" x="170" y="44" width="313.3" height="22" rx="2"/><text class="c-lab c-s1t" x="489.3" y="60">469.0</text><text class="c-box-t" x="0" y="95">Henderson, Nevada</text><text class="c-note" x="0" y="110">desert; rating not published</text><rect class="c-bar c-mute" x="170" y="86" width="159.9" height="22" rx="2"/><text class="c-lab c-s1t" x="335.9" y="102">239.4</text><text class="c-box-t" x="0" y="137">Quilicura, Santiago</text><text class="c-note" x="0" y="152">evaporates water</text><rect class="c-bar c-mute" x="170" y="128" width="95.5" height="22" rx="2"/><text class="c-lab c-s1t" x="271.5" y="144">143.0</text><text class="c-box-t" x="0" y="179">Mesa, Arizona</text><text class="c-note" x="0" y="194">Google named it high risk</text><rect class="c-bar c-alt" x="170" y="170" width="6.5" height="22" rx="2"/><text class="c-lab c-s1t" x="182.5" y="186">9.7</text><line class="c-base" x1="170" y1="32" x2="170" y2="196"/><line class="c-today" x1="203.4" y1="32" x2="203.4" y2="196"/><text class="c-note" x="209.4" y="212">the claim's line: 50 million gallons a year</text></svg>
<figcaption>Google 2026 Environmental Report, per-site table; risk judgements from its 2025 report, pages 40 to 41. Waltham Cross and Canelones have no row of their own yet.</figcaption>
</figure>

Google's share of freshwater withdrawal from high-risk sources has edged down: 15% in 2023, 14% in 2024, 13% in 2025. It replenished, by its own count, 78% of its freshwater consumption in 2025, against a 2030 goal of 120%.

**Microsoft** went furthest on design. Since August 2024, it said on 9 December 2024, all its new data centre designs evaporate zero water for cooling, using chip-level liquid in a closed loop. The cost is "a nominal increase in our annual energy usage", and Microsoft says plainly that the change "will increase our power usage effectiveness (PUE)". It has published no number. Its first such sites, in Phoenix and Mount Pleasant, Wisconsin, were to pilot in 2026 and come online in late 2027.

Fairwater, its flagship AI campus at Mount Pleasant, shows what "zero water" means in practice. Over 90% of its capacity uses a closed loop filled once, Guthrie wrote on 18 September 2025. It is "supported by the second largest water-cooled chiller plant on the planet", with 172 fans twenty feet across. Microsoft means chillers that cool the loop's water; the heat leaves through those fans, not a tower. A closed loop still needs a vast chiller plant.

Microsoft's fleet is a mix. Its average WUE fell to 0.27 litres per kWh in fiscal 2025, and about 90% of its 2025 owned fleet uses "low- to zero-water cooling" (24 June 2026). Its evaporative assist runs only above 85°F: about 10% of the year in Virginia, up to 40% in Phoenix. And half of its fiscal 2025 withdrawals were in areas of water stress, on its own data. Phoenix withdrew 981 megalitres, about 1.03 litres per kWh of its electricity, my arithmetic.

**Amazon Web Services** reports water withdrawn per kWh of computing falling from 0.25 litres in 2021 to 0.12 in 2025. Its direct evaporative cooling "requires water for less than 10% of the year" where weather permits, and in some of its most water-stressed regions it uses none for cooling. Still, 22% of its 2025 withdrawals were in high or extremely high water stress regions, on the Aqueduct index.

**Meta** reported WUE of 0.19 litres per kWh withdrawn in 2024, with about 30% of withdrawals in high-stress areas, my arithmetic from its data. On 27 August 2026 it said that most of its newest AI halls use closed-loop liquid cooling. A typical such hall with dry coolers, it wrote, "uses less water annually than a couple of full-service restaurants".

## Is the chiller being designed out?

No. Its hours shrink, but its numbers grow, and the makers say so in their own results.

Warm coolant cuts the hours a chiller runs. But a chiller fleet is sized for the hottest hour plus spares, so the count of chillers follows the megawatts, not the hours. What changes is the type: air-cooled chillers, which use no water, rather than water-cooled ones with towers.

The makers' third-quarter results of 2026 show it. Carrier, the American heating and cooling maker, said its data centre orders had passed $3 billion so far in 2026, up nearly 350%. It reported "great demand for our new 2 megawatt and 3 megawatt air-cooled chillers" (29 October 2026). Its capacity, it said, was "just not enough".

Vertiv, which makes both power and cooling gear, said it was "on track to doubling chiller production capacity by year-end" (28 October 2026). Johnson Controls, whose York brand makes chillers, said chillers are still the largest part of its data centre range. Over time, its chief executive said, "perhaps one or two fewer chillers will be needed" at the margin (27 October 2026).

Munters, the Swedish maker, put chillers at 49% of its data centre orders over the past year, on its third-quarter slides as summarised. Fairwater's chiller plant makes the same point from the buyer's side.

So I concede that chiller hours per megawatt fall, and that in mild climates some new halls may run without chillers. But the megawatts keep rising, and the hottest hours still need cover. Chiller orders and the dry roof are not in conflict, because most of the chillers being ordered are themselves dry.

<a id="the-worst-afternoon"></a>

## What happens on the worst afternoon?

This is where going dry is really paid for: not in yearly kilowatt-hours, but in peak megawatts.

A grid connection caps a building's maximum draw, at every instant. So the computing a site can run is set by its worst hour's overhead, not its yearly average. A dry roof is weakest exactly then: on the hottest afternoon the outside air may be warmer than the water, and a chiller must carry the load.

Nvidia's engineers write it in those terms. Heat rejection is "sized for worst-case scenarios", and power "budgeted for cooling during the worst hour becomes available to compute during much of the year" (24 August 2026). Their illustrative 100 MW site sets aside 20 MW for facility overhead.

A rough bound shows the size of the stake; the inference is mine. Suppose a dry liquid hall runs at a PUE of about 1.1 most of the year. On its worst hour, a chiller carrying the full load at a performance of about 4 adds roughly 0.25, lifting the instant ratio to about 1.35. On a fixed plug, computing scales with one over that peak, so the hall fits about 15% fewer racks than one whose worst hour stays near 1.15, my assumption for a wet hall. That likely overstates the penalty, since a chiller making 41 degree water works across a smaller lift than the datasheet's.

If the chiller only trims a few degrees off part of the load, the penalty is far smaller. That is the open question: no operator publishes the worst-hour PUE of a dry-cooled liquid hall.

Water has a peak too. Researchers at the University of California, Riverside, estimated that evaporative cooling's water demand on the peak day can run six to ten times its average, in a release of 12 March 2026. Utilities must size plants, pumps and pipes for that day. Their paper adds that water limits can push operators onto "less efficient dry cooling, further stressing the power grid during summer peaks".

So the grid and the water main are both built for the same hot afternoon. A tower spends its most water just as the town's mains peak; a dry roof draws its most power just as the grid is tightest. Under a fixed plug, a little water for the hottest 88 hours may buy back peak megawatts. That is a working hypothesis, and the test is design-day PUE in permit files and utility filings.

<a id="towns-say-no"></a>

## Why are towns saying no to water, even for halls that use almost none?

Because a town cannot see a closed loop, and it can see a water main, a power line and a large building.

Tucson, Arizona, is the clearest case. Its council ended talks on the Project Blue campus in August 2025, after opposition on water and power, local press reported. The project moved to county land, and a renewed agreement in December 2025 required a closed-loop air-cooled design. Arizona's utility regulator approved its power supply on 3 December 2025, reports say. Amazon left; the developer stayed. It was redesigned, not cancelled.

Other places redesigned too. In Santiago, Chile, a court partly annulled Google's permit for its Cerrillos campus on 26 February 2024, citing the aquifer and climate. Google said it would restart with air-cooled chillers, press reported, and the regulator cleared the redesign in October 2026, reports say. Meanwhile Google's existing Santiago campus at Quilicura consumed 143.0 million gallons in 2025, so it evaporates water.

Google's Canelones campus in Uruguay was resized and switched to air cooling after the 2023 drought, as reported. Meta's planned campus at Talavera de la Reina, Spain, was redesigned from water to dry air cooling, reports say. Southern Nevada stopped permitting new buildings with evaporative cooling from 2024, as reported.

Some places refuse outright, at least for now. The utility authority serving Ypsilanti, Michigan, voted on 22 April 2026 for a moratorium of not less than 12 months on water and sewer service to data centres, pending studies. Pinal County, Arizona, refused rezoning for a campus near Eloy on 26 August 2026, despite a closed-loop pledge, local press reported.

Water is also priced to steer. Loudoun County, Virginia, says data centres take 9% of Loudoun Water's drinking-water use on an average day. Its utility proposed reclaimed water at $2.07 per 1,000 gallons for 2026, against $4.42 for drinking water within reserved capacity, in October 2024. In Malaysia, Johor's data centre task force will not consider areas with a low water reserve margin, as told in [the Johor piece](/journal/the-queue-not-the-chip/#johor-waits-on-the-treatment-plant).

I concede that water is now a permit-stage risk, and that a closed-loop promise no longer buys consent. That is a cost the engineering chain leaves out. But the claim's test is a campus with power already secured, cancelled outright over water. I have found none. So far water kills weak projects and moves strong ones.

## Does cooling hold halls back, the way power does?

Not on the evidence so far. The makers are straining, but no primary source names a hall held up by cooling gear.

The strain is real. Munters said its data centre margin fell on "component shortages and ramp-up inefficiencies" (23 October 2026), and that "constraints remain industry-wide". Carrier said its new chillers had "initial teething pains with the supply chain". Modine signed long-term supplier deals "to secure critical components" for its backlog (3 November 2026).

But when the makers name what paces their customers, they name power. Johnson Controls' finance chief said some customers face "power and some electrical infrastructure limitation", which sets when they take delivery (27 October 2026). Vertiv named power, permitting, sentiment and skilled labour as the pacing items, per a transcript of its call.

Trane, another chiller maker, said its firm data centre orders typically arrive 12 to 18 months before delivery (5 May 2026). That is long, but shorter than the wait for a grid connection or a large transformer. Cooling in 2026 is a margin and ramp problem for its makers, not a visible gate on halls.

## Who is paid as the loop and the roof change?

Almost every large maker now sells both the loop at the chip and the plant on the roof. The line between them dissolved in 2026.

**The loop.** Power equipment makers bought liquid cooling. Schneider Electric agreed on 17 October 2024 to buy control of Motivair, completed in early 2025. Eaton completed its purchase of Boyd Thermal for $9.55 billion on 12 March 2026. Ecolab, best known for treating water, completed its purchase of CoolIT, a maker of CDUs and cold plates, on 2 July 2026, paying $4,627 million net in cash.

**The roof makers moved into the loop.** Trane completed its purchase of LiquidStack, a CDU maker, on 3 March 2026, and plans to build its CDUs in its new Fort Worth factory. Johnson Controls added CDUs and, by its chief executive's account in October 2026, bought a cold plate maker. Carrier designed its own CDUs, from 1 MW up to a 5 MW unit it is already taking orders for.

**The loop makers moved onto the roof.** Vertiv completed its purchase of ThermoKey, an Italian dry cooler maker, on 12 June 2026, on top of its 2024 chiller deal. Its view, in its own words on 28 October 2026: "the mix is definitely moving towards liquid cooling", and "It doesn't mean that air cooling is going away".

The sales figures show the scale. Carrier reported more than $550 million of data centre sales in the third quarter of 2026. Modine's data centre segment sold $439.7 million in its quarter to September 2026, up 95%. Boyd added about $535 million to Eaton's quarter, my arithmetic from Eaton's growth figures. SPX, whose brands include Marley cooling towers, is building capacity for about $1.1 billion of yearly data centre revenue, without saying which products.

How much of a megawatt's cost is cooling? No maker publishes a cooling-only figure, and no primary source splits a data centre's spending between power and cooling. Vertiv puts its own opportunity at about $3.25 million to $3.75 million per megawatt of computing, power and cooling together (19 May 2026). I do not split it.

## Can the heat be used instead of thrown away?

Sometimes, and warm coolant makes it easier, but it is early.

Data centre heat is low grade. An air hall's exhaust runs at 25 to 35 degrees, while older district heating networks need about 70 to 90. A heat pump must lift it, using electricity. Coolant at 45 to 55 degrees shrinks that lift.

Meta's Odense campus in Denmark has fed heat-pumped server heat into the town's district heating since around 2020. In Finland, Fortum started its heat plants beside Microsoft's two data centres in May 2026, but Microsoft's waste heat is "to be integrated in phases starting next year", that is from 2027. At full run Fortum expects it to supply about 40% of district heat for about 250,000 customers.

Heat reuse helps a town and an operator's reports. It does not change the roof decision, since most AI halls sit far from any heat network.

## So who holds the scarce thing, and what should an investor watch?

The scarce thing is not water in general. It is the right to evaporate it in a given basin, and the power to go without it on the hottest afternoon.

If the claim is right, three parts of the chain gain. **The loop at the chip**: cold plates, CDUs and pipework go into every AI rack, whatever the roof. **The dry roof**: dry coolers, adiabatic coolers and air-cooled chillers gain on towers in new halls. **The dry site with power**: a site with a grid allocation and scarce water is more usable than it looks, because a liquid hall can go dry cheaply.

Others lose share of the roof. Cooling towers and the water treatment that serves them grow more slowly per megawatt in new AI halls, though not in total while evaporation remains the cheap choice where water is plentiful. Old air halls need refits before they can take AI racks at all.

The readings come yearly and quarterly. Google's per-site water table each summer is the main one: Mesa, and whether Waltham Cross and Canelones get rows. Microsoft's first zero-water sites come online in late 2027, and whether it publishes their PUE matters. The chiller makers' orders each quarter show whether the worst afternoon is still being bought.

## What would prove me wrong

Three things would break the claim, and each tests what operators and towns do, not physics.

The first is Google's own sites. If Mesa, Waltham Cross or Canelones consumes 50 million gallons or more in 2026 or 2027, the dry roof was not chosen where Google said it would be. Mesa consumed 9.7 million in 2025, about a fiftieth of The Dalles. But two of the three sites cannot be tested until Google lists them, and Mesa's missing air-cooled footnote deserves an answer.

The second is a wet campus on scarce water: Google, Microsoft, Amazon or Meta reporting a new campus that evaporates water from a source it rates high risk. This limb is hard to break, and a sceptic should say so. Only Google rates sources by name, and its 2026 policy allows "recycled water" at high-risk sites. A high-risk site cooled by evaporating reclaimed water would follow Google's policy, and arguably sit outside the test.

The third is a powered AI campus cancelled outright over water rather than redesigned. Project Blue is the live case, and so far it fits my claim: redesigned to closed-loop air, with power approved, as reported. A water utility refusing service to a campus whose grid power is already secured would move me first.

Henderson, Nevada, is the hardest fact I must face. Google's campus there, in a desert basin, consumed 158.8 million gallons in 2023, 207.4 in 2024 and 239.4 in 2025. Google publishes no rating of its source, and Southern Nevada has stopped permitting new evaporative cooling, as reported. Henderson is an existing campus, so it does not break the test of a new one. But if Google rated it high risk and kept evaporating, the claim's spirit would be weaker than its letter.

The claim stands on two legs. The first, that heat forces liquid to the chip, is physics: Nvidia's fanless Rubin trays settle it, and no test attacks it. The second, that water sets the roof and not the count, is economics and consent. The first two tests attack operators' choices; only the third attacks "not how many", and only it would overturn the idea.

Rising water totals would not move me. The lab projects the national average rising from just over 0.36 litres per kWh in 2023 to between 0.45 and 0.48 by 2028, partly from "the increased water consumption of liquid-cooled systems". More evaporation where water is plentiful is the trade working as designed.

At the scale of the chip, heat has decided: liquid, warm. At the scale of the roof, the operator trades water for power, and the chip maker's temperature sets the price. At the scale of the town and the grid, both bills are sized for the same hot afternoon, and that is where the next argument about water will be settled.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

**Heat and water decide where AI goes** (30 October 2026)

Claim: "In AI data centres heat sets the cooling method and water sets where and how the heat leaves the building, not how many halls get built: every Google campus that Google itself names as at high water risk (Mesa, Waltham Cross and Canelones) will consume under 50 million gallons of water in each of 2026 and 2027, and no hyperscaler will report a new evaporatively cooled campus drawing on a water source it rates at high risk."

Breaks if: "Google reports consumption of 50 million gallons or more in 2026 or 2027 at Mesa, Waltham Cross or Canelones; or Google, Microsoft, Amazon or Meta reports opening a data centre cooled by evaporating water from a source it rates at high risk of depletion or scarcity; or a large AI campus with its power already secured is cancelled outright over water rather than redesigned to cool without it."

Earlier pieces on this subject made no claim. "Electricity doesn't get used up making AI. It turns into heat. Cooling is half the job." (21 August 2026) and "Jane Street's AI data hall has room to spare, and no power to fill it" (25 September 2026) were Explainers, so the claim above is this page's first.

Where the evidence stands: Mesa consumed 9.7 million gallons in 2025 but carries no air-cooled footnote, and Waltham Cross and Canelones are not yet listed, so the first limb cannot yet be tested there. Google's policy of 3 June 2026 allows "air cooling or recycled water" at high-risk sources, a path the second limb may not catch. Project Blue was redesigned to closed-loop air cooling, and its power supply was approved, as reported; that fits the third limb but does not test it.

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

**Rack heat and air.** Nvidia DGX GB200 User Guide (read 7 November 2026): "The rack power consumption is approximately 120kW". Vertiv SmartIT for NVIDIA GB300 NVL72 datasheet: "Up to 142 kW per rack, with approximately 85% liquid and 15% air cooling", Vertiv's design, not an Nvidia figure. Nvidia's Gen 2 rack power for Vera Rubin, 330 kW, is a ceiling, not a draw. Uptime Institute survey, as reported by The Register (3 August 2025): typical rack about 7.5 kW in 2025. ASHRAE TC 9.9, white paper on the emergence of liquid cooling in mainstream data centres (2021): 40 to 50 kW rack "up to 5000 cfm"; best floor tile "1900 cfm"; fan power "10% to 20%"; UPS capacity down 8%; W17 to W+ classes; the expectation of colder water. Airflow per kW: my arithmetic, air at about 1.17 kJ per cubic metre per degree, 15 degree rise, about 120 cfm per kW; tiles at 1,900 cfm each. Water against air, about 4,160 against 1.17 kJ per cubic metre per degree.

**Coolant.** Nvidia Technical Blog (16 March 2026), Vera Rubin POD: 45°C inlet, 41°C to the CDU, fanless trays, "up to 30% more GPUs". Nvidia blog, "Hotter Than a Hot Tub" (21 June 2026): PG25, 45 in, about 55 out, chillers in "maybe 1% of the year" (Ali Heydari), one degree about 4% (linking to ENERGY STAR). Nvidia Technical Blog (25 March 2026): Blackwell about 20% air-cooled at about 1.25 PUE; Rubin 100% liquid at 1.1. Google Cloud blog (30 April 2025): Project Deschutes. Carrier third quarter 2026 call (29 October 2026, corrected transcript). Microsoft innovation story (April 2021) on two-phase immersion; 3M 2025 annual report on its PFAS exit.

**Towers, coolers and chillers.** US Department of Energy, FEMP Best Management Practice 10: make-up, blowdown, drift, cycles of concentration. Evaporation at about 2,430 kJ per kg against 3,600 kJ per kWh, about 1.5 litres, my arithmetic. Nvidia (21 June 2026): "roughly 2.6 million gallons per megawatt per year" for tower systems, about 1.1 litres per kWh at full load, my arithmetic, against LBNL's median of about 2.0. Vertiv Liebert AFC datasheet (March 2020): about 4.2 to 4.6 at 35°C air. The 5 to 8 degree dry cooler approach is typical practice, my assumption.

**LBNL.** Shehabi and others, the lab's 2024 report on United States data centre energy use (December 2024): Table 4.2 and 4.3, W45 for AI liquid; Figure 4.4 medians, as I read them from the box plot, rounded:

| Design | Hall | PUE, about | Site water, litres per kWh, about |
|---|---|---|---|
| Air: water-cooled chiller with tower | Midsize | 1.52 | 2.9 |
| Air: air-cooled chiller | Midsize | 1.83 | near 0 |
| Air: dry cooler with air-cooled chiller | Midsize | 1.6 | near 0 |
| Liquid: waterside economiser with tower | Large | 1.13 | 2.0 |
| Liquid: dry cooler with adiabatic assist | Large | 1.10 | 0.13 |
| Liquid: dry cooler with air-cooled chiller | Large | 1.10 | 0 |

The quotes "less chiller run hours", "rarely the case" and "use more energy" are from the same report, printed pages 42, 44 and 45. National water, printed pages 55 to 57: 66 billion litres direct in 2023; "nearly 800 billion liters" indirect on about 176 TWh; 4.52 litres per kWh; reservoir evaporation in scope; power contracts and on-site generation ignored. National WUE rising to 0.45 to 0.48 by 2028, printed pages 47 to 48.

**The whole-water sum,** my arithmetic: roof water plus PUE times 4.52. Air with tower 2.9 + 1.52 × 4.52 = about 9.8; air-cooled chiller 1.83 × 4.52 = about 8.3; liquid with tower 2.0 + 1.13 × 4.52 = about 7.1; liquid dry cooler 1.10 × 4.52 = about 5.0. Gas combined cycle with a tower about 0.75 litres per kWh: NREL's operational medians (2012), background. Meta 2025 Environmental Data Index: embedded water 72,207 ML against 3,123 ML consumed (2024); 5,075 ML for contracted renewables.

**Google.** 2026 Environmental Report (2025 data): data centres withdrew 13,562 and consumed 10,523 million gallons; potable 10,949 of withdrawal; per-site consumption, million gallons: Council Bluffs 1,346.0; The Dalles 469.0; Henderson 239.4 (207.4 in 2024, 158.8 in 2023); Quilicura 143.0; Mesa 9.7, withdrawal 19.4, no air-cooled footnote; risk shares 72%, 15%, 13%; replenishment 78%. 2025 Environmental Report, pages 40 to 41: Waltham Cross, Mesa, Canelones. 2024 report: 15% high risk in 2023. Google blog (3 June 2026): the five commitments, "air cooling or recycled water", "approximately 10%".

**Microsoft.** Blog (9 December 2024): zero-water designs from August 2024, "nominal increase", PUE rises, pilots in 2026, online late 2027. Guthrie (18 September 2025): Fairwater. Blog (24 June 2026): WUE 0.27, about 90% of owned fleet, 85°F threshold. 2026 Environmental Sustainability Report and Data Fact Sheet: WUE as cooling and humidification consumption; FY25 withdrawals 13,266 ML, 6,659 ML in water-stressed areas; Phoenix 981 ML on 954,206 MWh.

**AWS and Meta.** AWS 2025 Sustainability Summary: WUE withdrawal 0.25 (2021) to 0.12 (2025); 9.4 billion litres; 22% high or extremely high stress; direct evaporative cooling under 10% of the year. Meta 2025 Environmental Data Index: WUE 0.19 (2024), withdrawal basis; 1,704 of 5,637 ML in high-stress areas. Meta (27 August 2026): closed-loop liquid in most newest AI halls, "a couple of full-service restaurants". AWS in-row heat exchanger and Meta's air-assisted liquid cooling: press reports (2024 to 2025).

**Jane Street.** Its write-up of its newest Texas site: "4,032 GPUs across 56 racks, retrofitted for liquid cooling", undated. Signals and Threads podcast (25 July 2025), Dan Pontecorvo.

**Makers.** Carrier third quarter 2026 release and call (29 October 2026). Vertiv third quarter call (28 October 2026); ThermoKey completion (12 June 2026); investor conference (19 May 2026), page 31. Johnson Controls fourth quarter fiscal 2026 call (27 October 2026). Munters third quarter 2026 report (23 October 2026); the 49% chiller share from its slides, as summarised. Modine Form 8-K (3 November 2026). Trane Oppenheimer conference transcript (5 May 2026); LiquidStack completion (3 March 2026). Ecolab Form 10-Q, third quarter 2026, Note 3. Eaton third quarter 2026 release: Boyd acquired 12 March 2026 for $9.55 billion net; 31% contribution to Electrical Global growth on $2,727 million, so about $535 million, my arithmetic. SPX third quarter 2026 release. Schneider Electric Capital Markets Day transcript (11 December 2025): Motivair acquired in March 2025.

**Towns.** Chile's Second Environmental Court, ruling of 26 February 2024. Ypsilanti Community Utilities Authority Resolution 26-08 (22 April 2026). Loudoun County, its page on data centres and water; Loudoun Water board presentation (10 October 2024), proposed rates. Malaysia's Parliament, Hansard (28 October 2026). Press, as marked in the text: Project Blue (KJZZ, AZ Luminaria, AZPM, 2025 to 2026); Cerrillos restart and clearance (Meganoticias, El Desconcierto); Canelones (DCD); Talavera (iagua); Southern Nevada (Las Vegas Review-Journal); Pinal County (KTAR, 26 August 2026). University of California, Riverside release (12 March 2026) on "Small Bottle, Big Pipe" (arXiv 2603.02705).

**Heat reuse.** Fortum release (May 2026). Ramboll project page on Meta Odense.

**Worst afternoon.** Nvidia Technical Blog, "Maximizing AI Factory Performance per Watt with NVIDIA DSX MaxLPS" (24 August 2026). The 15% bound is my arithmetic: PUE 1.1 plus 0.25 for a chiller at a performance of 4 is about 1.35; a wet hall's worst hour is assumed at about 1.15; 1.15 over 1.35 is about 0.85. The performance of 4 is for 20°C water at 35°C air, so it overstates the lift for 41°C water.

</details>

<section class="exposure">
<h3>Who is exposed if heat sets the cooling and water sets where it goes</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>The loop at the chip</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span>, <span class="names">Eaton</span>, <span class="names">Ecolab</span>, <span class="names">nVent</span> and <span class="names">Delta</span> make cold plates and CDUs.</dd>
<dt>The roof</dt>
<dd><span class="names">Carrier</span>, <span class="names">Trane</span>, <span class="names">Johnson Controls</span>, <span class="names">Modine</span>, <span class="names">Munters</span> and <span class="names">SPX</span> make chillers, dry coolers and towers.</dd>
<dt>The halls that choose</dt>
<dd><span class="names">Microsoft</span>, <span class="names">Google</span>, <span class="names">Meta</span> and <span class="names">Amazon</span> run them; <span class="names">Nvidia</span> sets the coolant temperature.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Evaporative campuses in dry basins, and air-cooled halls that need a refit for liquid.</dd>
</dl>
</section>

---

<p class="sources">Sources: Lawrence Berkeley National Laboratory (December 2024); ASHRAE (2021); Nvidia's blogs and user guide; Google, Microsoft, Amazon Web Services and Meta reports and posts; Carrier, Vertiv, Johnson Controls, Trane, Munters, Modine, Eaton, Ecolab and SPX filings and calls; Chile's Second Environmental Court; Ypsilanti's utility authority; Loudoun County; press only where marked. Personal research, not investment advice.</p>
