---
title: "How ten thousand chips talk: the glass stays, and the plug survives its replacement"
date: 2026-09-04
summary: "An AI model is spread across thousands of chips that swap results for every word they produce, over copper inside a rack and over light between racks. The glass that carries the light stays for years, while the plugs that make it are bought again at every speed step. Switch makers have built optics onto the switch to retire the plug, yet they kept the laser in one, and Nvidia's newest blueprints still pick the plug."
category: "Analysis"
cover: "/covers/ten-thousand-chips-one-thought.svg"
tags: ["networking", "optics", "the-stack"]
updated: 2026-11-06
updateNote: "Now follows one message from rack to rack and asks where heat lets the laser live, with evidence to 6 November 2026."
draft: false
---

Nvidia and Broadcom have spent years building network switches that do away with the optical plug. Both now sell them. Yet both kept the laser, the part that makes the light, in a plug a technician can pull out by hand.

And when Nvidia published its blueprints for clusters of its newest systems in September, both blueprints picked the switch with ordinary plugs.

That is not hesitation. In an AI network the parts that only carry light stay for years. The parts that make it are bought again whenever chips get faster, so they are kept within reach.

The plug is not on its way out between racks.

A frontier AI model is too big for one chip, so it is cut across thousands that swap results for every word they write.

"The network" joining them is three networks, split by distance. Inside a rack, copper ties dozens of chips into one machine: scale-up. Across a hall, racks talk by light in glass fibre, with a plug at each end: scale-out. A third joins campuses. This piece is about the middle one.

<details class="analogy">
<summary>The analogy</summary>
<p>A house is wired once. The wiring in the walls is the glass fibre. The bulbs are the plugs, and the filament in each is the laser. Want a brighter room, a faster chip, and you buy new bulbs. The wires stay, and so does the wall switch, which never cares how bright the bulb is: that is the mirror switch.</p>
<p>Plastering the bulbs into the ceiling would save a little power: that is co-packaging. But a dead filament would mean taking the ceiling down. So builders fixed the fitting and left the bulb in a socket a hand can reach.</p>
</details>

Trace one message between two racks. First, the chip hands its result to its network card over copper. Second, a plug turns it into light: a translator chip, the DSP, cleans the signal and a laser flashes it out. Third, the light crosses the hall in glass fibre.

Fourth, at a switch, a switch chip reads the address between two plugs and sends it on. Fifth, a detector in the last plug hands it to the other chip.

<figure class="chart">
<p class="chart-title">The plug is the step bought again, and its laser is the scarce part</p>
<p class="chart-sub">One message from a GPU in rack A to a GPU in rack B, in order</p>
<svg viewBox="0 0 560 196" role="img" aria-label="Diagram of five steps in order. One, card: GPU A hands its partial results to its network card over copper. Two, plug: a translator chip and a laser turn the signal into light; this is the choke point, bought again at every speed step, from 800 gigabits a second to 1.6 terabits, and its laser comes from a few factories. Three, glass: fibre carries the light across the hall at any speed. Four, switch: a switch chip of 102.4 terabits a second reads the address and sends the message on, through more plugs. Five, receive: a detector turns light back into current for GPU B.">
<rect class="c-box" x="5.0" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="13.0" y="66">1. Card</text>
<text class="c-note" x="13.0" y="88">GPU A hands</text>
<text class="c-note" x="13.0" y="106">its results to</text>
<text class="c-note" x="13.0" y="124">its card over</text>
<text class="c-note" x="13.0" y="142">copper</text>
<line class="c-arrow" x1="106.4" y1="97" x2="111.4" y2="97"/><polygon class="c-arrow-head" points="116.4,97 110.4,93 110.4,101"/>
<rect class="c-zone" x="113.4" y="14" width="108.4" height="144" rx="4"/>
<text class="c-zone-t" x="167.6" y="30" text-anchor="middle">THE CHOKE POINT</text>
<rect class="c-box" x="117.4" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="125.4" y="66">2. Plug</text>
<text class="c-note" x="125.4" y="88">Translator and</text>
<text class="c-note" x="125.4" y="106">laser turn it</text>
<text class="c-note" x="125.4" y="124">into light</text>
<text class="c-note" x="125.4" y="142">Bought again</text>
<line class="c-arrow" x1="218.8" y1="97" x2="223.8" y2="97"/><polygon class="c-arrow-head" points="228.8,97 222.8,93 222.8,101"/>
<rect class="c-box" x="229.8" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="237.8" y="66">3. Glass</text>
<text class="c-note" x="237.8" y="88">Fibre crosses</text>
<text class="c-note" x="237.8" y="106">the hall</text>
<text class="c-note" x="237.8" y="124">Carries any</text>
<text class="c-note" x="237.8" y="142">speed</text>
<line class="c-arrow" x1="331.2" y1="97" x2="336.2" y2="97"/><polygon class="c-arrow-head" points="341.2,97 335.2,93 335.2,101"/>
<rect class="c-box" x="342.2" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="350.2" y="66">4. Switch</text>
<text class="c-note" x="350.2" y="88">Reads the</text>
<text class="c-note" x="350.2" y="106">address and</text>
<text class="c-note" x="350.2" y="124">sends it on</text>
<text class="c-note" x="350.2" y="142">102.4 Tb/s</text>
<line class="c-arrow" x1="443.6" y1="97" x2="448.6" y2="97"/><polygon class="c-arrow-head" points="453.6,97 447.6,93 447.6,101"/>
<rect class="c-box" x="454.6" y="44" width="100.4" height="106" rx="4"/>
<text class="c-box-t" x="462.6" y="66">5. Receive</text>
<text class="c-note" x="462.6" y="88">A detector</text>
<text class="c-note" x="462.6" y="106">turns light</text>
<text class="c-note" x="462.6" y="124">to current</text>
<text class="c-note" x="462.6" y="142">for GPU B</text>
<text class="c-lab c-s2t" x="117.4" y="180" text-anchor="start">Replaced from 800 Gb/s to 1.6 Tb/s; few laser fabs</text>
</svg>
<figcaption>Broadcom (3 June 2025), Nvidia and Lumentum disclosures to November 2026. My framing of the chain.</figcaption>
</figure>

The second step binds. Glass carries any speed, so fibre outlives several chip generations. The plug is bought again at every speed step, from 800 gigabits a second to 1.6 terabits, one at each end of every fibre. Its laser comes from a handful of factories.

Switch makers want the optics fixed onto the switch, called co-packaged optics, because it saves power. But a fixed part cannot be swapped when it fails, and lasers are among the least reliable parts of data centre optics. So they left the laser in a plug, and co-packaging removes the translator.

The case against is a factory plan and real money. SPIL, a Taiwanese packaging firm, aims for fifteen times its co-packaged optics capacity by mid-2027, Nvidia said in October: a target, not a factory. In November the laser maker Lumentum reported a co-packaging win backed by more than $5 billion of purchase commitments.

That money goes to a laser maker, and every co-packaged switch now shipping keeps its laser in a pull-out box. Faster chips decide how often the plug is bought. Heat and repair decide where its laser lives.

<hr class="layer">
<p class="layer-label">For investors</p>


<a id="ten-thousand-chips-one-thought"></a>
## The glass is bought once, the light is bought again, so the plug stays between racks

<a id="the-plug-stays"></a>

The plug stays the default between racks through 2028, and the popular story that co-packaged optics kills the transceiver is wrong. Broadcom and Nvidia, both makers of AI network switches, both ship switches with co-packaged optics, the light-making parts fixed onto the switch, yet both kept the laser in a module a hand can pull out. In September 2026 both of Nvidia's DGX SuperPOD blueprints for Vera Rubin, its newest systems, picked plug-in switches. If that holds, the plug, the laser and the glass keep getting paid, and the casualty is narrow: the translator chip inside the plug.

The reason is a split by job. The parts that make or read light are bought again at every speed step, while the parts that only carry it stay for years.

<figure class="chart">
<p class="chart-title">Only the parts that make or read the light are bought again</p>
<p class="chart-sub">One link between racks, by whether each part is replaced at a speed step</p>
<svg viewBox="0 0 560 230" role="img" aria-label="Diagram of one link between racks. On the left, bought again at each speed step: the switch chip, which reads and routes traffic, and the plug, which holds the DSP that translates the signal and the laser that makes the light. On the right, staying for years: the glass fibre, which carries light, and the mirror switch, which steers light without reading it, at any data rate.">
<rect class="c-zone" x="10" y="10" width="265" height="200"/>
<text class="c-zone-t" x="22" y="32">Bought again</text>
<rect class="c-zone" x="285" y="10" width="265" height="200"/>
<text class="c-zone-t" x="297" y="32">Stays for years</text>
<rect class="c-box" x="20" y="70" width="110" height="56" rx="4"/>
<text class="c-box-t" x="75" y="103" text-anchor="middle">Switch chip</text>
<text class="c-note" x="75" y="146" text-anchor="middle">reads and routes</text>
<rect class="c-box" x="150" y="70" width="110" height="56" rx="4"/>
<text class="c-box-t" x="205" y="103" text-anchor="middle">Plug</text>
<text class="c-note" x="205" y="146" text-anchor="middle">DSP and laser</text>
<line class="c-arrow" x1="130" y1="98" x2="144" y2="98"/><polygon class="c-arrow-head" points="150,98 143,94 143,102"/>
<line class="c-arrow" x1="260" y1="98" x2="404" y2="98"/><polygon class="c-arrow-head" points="410,98 403,94 403,102"/>
<text class="c-box-t" x="345" y="88" text-anchor="middle">Glass fibre</text>
<text class="c-note" x="345" y="146" text-anchor="middle">carries light</text>
<rect class="c-box" x="410" y="70" width="125" height="56" rx="4"/>
<text class="c-box-t" x="472.5" y="103" text-anchor="middle">Mirror switch</text>
<text class="c-note" x="472.5" y="146" text-anchor="middle">steers light,</text>
<text class="c-note" x="472.5" y="162" text-anchor="middle">never reads it</text>
<text class="c-note" x="142.5" y="196" text-anchor="middle">replaced from 800 Gb/s to 1.6 Tb/s</text>
<text class="c-note" x="417.5" y="196" text-anchor="middle">works at any data rate</text>
</svg>
<figcaption>My sort, from Nvidia, Broadcom, Marvell, Lumentum, Corning and Google disclosures to October 2026. Google's whole optical layer, mirror switches, plugs and fibre included, was under 5% of a 4,096-chip TPU v4 pod's cost and under 3% of its power (2023).</figcaption>
</figure>

## Distance sets the medium, and only light crosses a hall

Each distance needs its own medium, because an electrical signal gives up within a few metres. Loss in a wire rises with frequency, and every speed step raises the frequency, so copper's useful reach shrinks. That is why Nvidia's GB200 NVL72 rack packs 72 GPUs into one NVLink domain, its chip-to-chip copper network, at 130 TB/s.

Across a hall it is light. Light in glass barely fades over a hall, but a GPU speaks electricity, so every fibre needs a converter at each end. That converter is the plug: a translator chip, the DSP, to clean and re-time the signal, a laser to send and a detector to receive. One Broadcom Tomahawk 6 switch chip moves 102.4 Tb/s, and Broadcom says two tiers of them join more than 100,000 chips, through a plug at each end of each fibre.

<a id="fairwater-spans-two-states"></a>

Beyond the hall, even light is slow. It covers about 200 kilometres a millisecond in fibre. Fairwater, Microsoft's pair of AI campuses in Wisconsin and near Atlanta, are about 1,000 km apart by my straight-line reckoning, so a message takes at least 5 ms one way. Only the least talkative work, such as averaging between copies of the model, can cross. I have found no Microsoft or lab statement that a named model was trained across both sites.

<a id="lumentum-makes-the-light"></a>
## Six physical facts make the laser the hardest part to add

Of everything in the plug, the laser is the part supply cannot quickly follow.

**The wrong material.** Silicon is poor at emitting light, so data centre lasers are grown on indium phosphide, a different crystal with its own fabs, tools and know-how.

**Small, brittle wafers.** Indium phosphide wafers are small and break easily, so each yields fewer chips and loses more along the way. Coherent, a maker of lasers and transceivers, is moving to six-inch wafers to fix that.

**Few factories.** A handful of makers yield fast lasers well: Lumentum, a US maker of lasers and optical parts, Coherent and Broadcom, which says its indium phosphide factories are more than tripling capacity. More output comes from a new fab, not a new shift.

**Years to build.** Lumentum's new fab in Greensboro, North Carolina, expects first revenue in early 2028.

**Heat.** The Optical Internetworking Forum, the industry body that sets standards for optical links, listed in March 2023 that lasers "require lower temp than Si and SiPho", silicon and silicon photonics, and that their reliability turns on temperature, current and power.

**Everyone orders at once.** Lumentum's 200 gigabit EMLs, the fast-switching lasers in today's plugs, passed a quarter of its EML revenue in the June 2026 quarter. On 11 August it was still shipping behind demand, and further behind on lasers for co-packaged optics. It put part of a year's rise in gross margin, the share of each sale left after the cost of making it, down to higher prices. In the quarter to 26 September its GAAP gross margin reached 51.0%, against 34.0% a year earlier. The laser starts to look like the slow parts in [the chip supply chain](/journal/the-chip-supply-chain/).

<a id="the-optics-you-cannot-unplug"></a>
## The headline retired the plug, and the spec sheet kept it

Read fast, co-packaging ends the plug and everyone who makes it. It mounts optical engines on the switch package, which Nvidia claims makes its switches 3.5 times more power efficient, and that saving is why it exists. Broadcom said on 8 October 2025 it was shipping Tomahawk 6 Davisson, its co-packaged switch, and Nvidia sells its own.

The spec sheets tell a narrower story. Davisson ships with "Field-Replaceable ELSFP Laser Modules". Nvidia's Spectrum-X engines are soldered on, while its lasers sit in removable modules for easy replacement. A failed engine means replacing the whole switch, so the laser, which Nvidia calls one of the most persistent reliability problems in data centre optics, was kept reachable.

The blueprint went further. Nvidia's results release of 26 August 2026 offers Spectrum-6, a switch in its Spectrum-X range, "supporting both pluggable and co-packaged optics". Yet its DGX SuperPOD reference architectures for Vera Rubin, created 15 September 2026, specify plug-in switches in both versions: the SN6600-LD for Spectrum-X and the Quantum-X800 Q3400-RD for InfiniBand, its other network standard. A reference architecture is the blueprint customers copy, so its choice is the default. Nvidia's switch manual lists a co-packaged twin of the Spectrum-X pick, the SN6810-LD, at the same 102.4 Tb/s and with the same liquid cooling, so neither capacity nor cooling forced the choice.

<figure class="chart">
<p class="chart-title">Co-packaged switches arrived, and the newest blueprints still picked the plug</p>
<p class="chart-sub">Dated steps in moving optics onto the switch, by maker</p>
<svg viewBox="0 0 560 260" role="img" aria-label="Timeline. Nvidia announced co-packaged optics switches on 18 March 2025. On 26 August 2025 it said their lasers sit in removable modules. On 8 October 2025 Broadcom said it was shipping Tomahawk 6 Davisson with field-replaceable laser modules. On 26 August 2026 Nvidia sold Spectrum-6 with either pluggable or co-packaged optics. On 15 September 2026 both Vera Rubin reference architectures picked pluggable switches. The shaded span runs from today to the end of 2028, when the claim is tested.">
<rect class="c-zone" x="355.3" y="20" width="184.7" height="200"/>
<text class="c-zone-t" x="377.3" y="38">Tested to 2028</text>
<g class="c-grid"><line x1="200" y1="20" x2="200" y2="220"/><line x1="285" y1="20" x2="285" y2="220"/><line x1="370" y1="20" x2="370" y2="220"/><line x1="455" y1="20" x2="455" y2="220"/><line x1="540" y1="20" x2="540" y2="220"/></g>
<g class="c-axis"><text x="200" y="240" text-anchor="middle">2025</text><text x="285" y="240" text-anchor="middle">2026</text><text x="370" y="240" text-anchor="middle">2027</text><text x="455" y="240" text-anchor="middle">2028</text><text x="540" y="240" text-anchor="middle">2029</text><text x="190" y="64" text-anchor="end">Nvidia co-packaged switch</text><text x="190" y="102" text-anchor="end">Nvidia, where lasers go</text><text x="190" y="140" text-anchor="end">Broadcom Davisson</text><text x="190" y="178" text-anchor="end">Nvidia Spectrum-6</text><text x="190" y="216" text-anchor="end">Vera Rubin blueprints</text></g>
<g class="c-end"><circle cx="217.9" cy="60" r="4.5"/><circle cx="255.2" cy="98" r="4.5"/><circle cx="265.2" cy="136" r="4.5"/><circle cx="340.2" cy="174" r="4.5"/><circle cx="344.8" cy="212" r="4.5"/></g>
<g class="c-endt"><text x="226.9" y="64">announced</text><text x="264.2" y="102">removable modules</text><text x="274.2" y="140">ships, lasers replaceable</text><text x="349.2" y="178">sold both ways</text><text x="353.8" y="216">both pick the plug</text></g>
</svg>
<figcaption>Nvidia releases of 18 March 2025 and 26 August 2026, technical blog of 26 August 2025 and DGX SuperPOD Vera Rubin reference architectures (15 September 2026); Broadcom release of 8 October 2025. Shaded: from today to the end of 2028, the date in my claim.</figcaption>
</figure>

## Four terms carry the argument

**Scale-up, scale-out, scale-across.** Teammates, the league and away games. Scale-up joins GPUs inside a rack into one machine over copper NVLink. Scale-out joins racks across a hall over Ethernet or InfiniBand, the two network standards Nvidia sells, through optics. Scale-across joins campuses by long fibre.

**CPO and NPO.** A bulb plastered into the ceiling, and a lamp on the desk. Co-packaged optics puts the optical engines on the switch package; near-packaged optics puts them on the board beside it, easier to replace. Both attack the DSP. Neither removes the laser.

**Gb/s and GB/s.** Coins and eight-coin rolls. Network links are quoted in bits, GPU links in bytes, and NVLink's 1.8 TB/s per Blackwell GPU counts both directions while an 800 gigabit plug is quoted each way. Converted, that is 7.2 Tb/s each way, about nine times an 800 gigabit link, by my arithmetic.

**EML and continuous laser.** A flicked torch and a lamp left on. An EML switches its own light on and off fast, as in today's plugs. A continuous laser just shines, and a modulator on the engine does the switching. Co-packaged engines need the second kind, at high power.

## Fifteen times measures engines, against a base nobody gave

The figure thrown against this claim is SPIL's. On 21 October 2026 Nvidia said SPIL, a Taiwanese chip packaging firm, targets a 15-fold rise in co-packaged optical engine capacity by mid-2027, and another doubling by the end of 2028.

<figure class="chart">
<p class="chart-title">The case against: capacity for co-packaged engines is set to rise about thirtyfold</p>
<p class="chart-sub">SPIL's co-packaged optical engine capacity, as a multiple of October 2026</p>
<svg viewBox="0 0 560 170" role="img" aria-label="Bar chart. SPIL's co-packaged optical engine capacity, as a multiple of its level in October 2026: 1 today, 15 by mid 2027, and about 30 by the end of 2028 after another doubling. These are targets reported by Nvidia, not built factories.">
<g class="c-axis"><text x="108" y="41" text-anchor="end">October 2026</text><text x="108" y="87" text-anchor="end">Mid 2027</text><text x="108" y="133" text-anchor="end">End of 2028</text></g>
<rect class="c-bar" x="120" y="22" width="9" height="28" rx="2"/>
<text class="c-lab c-s2t" x="139" y="41">1x</text>
<rect class="c-bar" x="120" y="68" width="135" height="28" rx="2"/>
<text class="c-lab c-s2t" x="265" y="87">15x, target</text>
<rect class="c-bar" x="120" y="114" width="270" height="28" rx="2"/>
<text class="c-lab c-s2t" x="400" y="133">about 30x, target</text>
<line class="c-base" x1="120" y1="12" x2="120" y2="160"/>
</svg>
<figcaption>Nvidia release, 21 October 2026: a 15-fold rise by mid-2027 and another doubling by the end of 2028. About 30 times is my arithmetic. These are targets, not built factories, and no laser capacity is mentioned.</figcaption>
</figure>

It measures capacity to build engines, the part fixed onto the switch, not switches shipped, lasers made or demand. It is a multiple of October 2026's level, about 30 times by the end of 2028 on my arithmetic, and Nvidia gave no base, so fifteen times a small number can still be small. And it is a target, not a factory.

The trap is that engines need torches. Each takes continuous lasers fed from a removable front-panel module, Nvidia's release gave no figure for them, and Lumentum said in August it was further behind demand on exactly those lasers than on its plug lasers. If the plan is built, what moves is the translator. Where the switch drives its engines directly, the DSP leaves the plug.

## The value sits with the light, the glass and the mirrors

Sorting parts by whether they read light or only carry it shows who is paid per speed step and who per campus.

**The light, paid at every speed step.** Lasers come from Lumentum, Coherent and Broadcom's fabs, and plugs from assemblers such as Coherent, Innolight, Eoptolink and Fabrinet. Laser makers are paid on both routes, an EML in a plug or a continuous laser in a front-panel module.

<a id="broadcom-wins-either-way"></a>

The switch chip is bought again too. Tomahawk 6 reached volume production in March 2026, and Broadcom said on 2 September it is deployed at pretty much every AI customer building custom chips with Broadcom.

<a id="marvell-collects-the-toll"></a>

**The translator, paid while the plug keeps it.** The optical DSP sits inside each plug, so its volume follows plug volume. Marvell, a chip designer that bought this business with Inphi in 2021, had data centre revenue of US$2.17 billion in the quarter to 1 August 2026, 79% of its total. Its chief executive said on 27 August that plugs remain the main form for links between racks. This is the one position co-packaging puts at risk.

<a id="corning-lays-the-glass"></a>

**The glass, paid per campus.** Fibre does not care how fast the chips are. Meta, the owner of Facebook, agreed in January 2026 to buy up to US$6 billion of fibre and cable from Corning, the glass and fibre maker, through 2030, and Amazon, the online retailer and cloud provider, signed in June. Corning's optical sales rose 44% in the third quarter of 2026, with the data centre side up 84%: glass grows with new halls, not with speed steps.

<a id="google-steers-the-light"></a>

**The mirrors, which never read the data.** Google joins the cubes of its TPU pods with Palomar, its own optical circuit switch, whose tilting mirrors steer light between 136 fibres. A faster chip sends more through the same mirrors, and Google's Ironwood pods of 9,216 chips still use them. Lumentum shipped more than US$90 million of such switches in its year to June 2026, and on 2 November its chief executive said demand visibility for them had "expanded significantly in recent months".

## What would prove me wrong

Three tests break the claim by the end of 2028. The first is the blueprint: if the reference design for Feynman, Nvidia's next platform, or any newer system makes a co-packaged switch the default or only option for the compute fabric, the plug has lost the hall. Nvidia already lists "Spectrum-class optical scale-out" in Feynman, undated, so a dated Feynman blueprint would move me first.

The second is the mix: if Nvidia or Broadcom says most AI switches it ships are co-packaged, the same. It is the only test that also covers cloud giants building their own designs on Davisson, which no blueprint shows. The third is the laser moving in: if either ships a standard co-packaged switch with its lasers fixed to the package, the repair limit I rest on was not binding, and the mechanism is wrong, not just the timing.

The claim stands on two legs. One is economic: the makers and readers of light are bought again at each speed step, and power savings are the money that could tip customers to co-packaging. The first two tests attack it, and it can fail on timing. The other is physical: lasers fail more than other optical parts and want to run cooler than silicon, so they are kept where they can be swapped. Money cannot repeal that; only a laser that survives the package's heat can, and the third test attacks it.

When someone says co-packaged optics kills the transceiver, I disagree. It moves the translator onto the switch. On every co-packaged switch shipping, the laser stays in a plug a hand can pull, and Nvidia's newest blueprint picked the plug switch. Broadcom's claim to be "the leader in leading edge optical DSPs", by a third-party transcript of 2 September, contests who sells the translator, not whether the plug stays.

<a id="optics-comes-for-scale-up"></a>
## Optics is coming for the rack, copper's last island

Nvidia plans to stretch the GPU's own network across racks with light. Its technical blog of 16 March 2026 says Vera Rubin Ultra's NVL576 will join eight racks into one NVLink domain "with copper and direct optical connections", and Kyber, the rack Nvidia calls the foundation for its Feynman generation, is to reach 1,152 GPUs with direct optical links between racks. Scale-up carries about nine times the bandwidth per GPU of scale-out, so if it goes optical the lasers per GPU multiply. No date for a blueprint with optical scale-up has been given.

I concede that "copper inside the rack" is a 2026 statement, and some traffic between racks may never touch a plug. But my claim and its tests name the scale-out switch, which this plan leaves alone. The Register, a technology news site, reported in April that NVL576 keeps copper inside the rack and pluggable optics on its spine layer. And every optical route needs lasers from the same few indium phosphide fabs, in the year Greensboro first earns revenue. Marvell's purchase of Celestial AI, completed on 2 February 2026 for "optical interconnect technology for scale-up connectivity", is a bet on exactly this.

<a id="the-money-buys-lasers"></a>
## Real money has moved to co-packaging, and it bought lasers

The first big money in co-packaging is real. On 2 November 2026 Lumentum reported "our second major NPO/CPO win, backed by purchase commitments exceeding $5 billion". The same day Marvell, the DSP seller, agreed to buy Lumentum, citing its indium phosphide manufacturing and high-power lasers; the deal is expected to close in the first half of 2028.

I concede the plug's share of new optics spend will shrink. But the money went to a laser maker, which is what the claim expects, and the release lumps near-packaged optics, which keep engines replaceable on the board, with co-packaged, giving no split. What would worry me is a split showing mostly co-packaged optics with lasers fixed on the package: that would hit the third test early.

<a id="heat-decides-the-laser"></a>
## Heat may decide where the laser lives, so the plug follows the optics

The debate is framed as plug against no plug; my hypothesis is that it is really about where the laser can sit. It stands on the OIF's heat finding, the same slides' "hot swap" role for a pluggable laser box if one laser fails, and the removable laser modules feeding every co-packaged switch I have read.

The inference is mine. Switch and GPU chips run hotter each generation, so the closer optics move to them, the further the laser must move away, into a box that can be cooled and swapped. The plug does not die; its contents change from a DSP and a laser to lasers alone, and if scale-up goes optical that box multiplies.

The test is one question put to every new co-packaged switch and optical NVLink design: where are the lasers? What would kill the idea is a standard product with lasers on the package that survive its heat, such as lasers grown on silicon. Two points cut against it: the OIF slides expected a co-packaged switch to need 4 to 16 laser modules, against 32 or 64 plugs, and I have no laser failure data of my own.

## The same sort works at the plug, the rack and the campus

Inside one plug, the DSP, laser and detector are all bought again at each speed step, and co-packaging so far takes only the translator. At the rack, 72 GPUs act as one because copper reaches a few metres, each speed step shrinks that island, and every optical route out of it needs lasers. At the campus, glass is laid once per hall and Corning grows with new sites, while between sites even light costs 5 ms, so only the quietest work crosses. One question sorts all three: does a part make or read the light, or only carry it.


<details class="claims-record">
<summary>The claims on record, word for word</summary>

The test this piece stands behind, quoted word for word:

**The plug stays the default between racks through 2028** (30 October 2026)

Claim: "Between the racks of an AI cluster the optical plug stays the default through 2028: switches with co-packaged optics keep their lasers in removable front-panel modules, and Nvidia's reference designs for its newest systems keep specifying pluggable switches, as both Vera Rubin designs do today, with the Spectrum-X SN6600-LD and the InfiniBand Quantum-X800 Q3400-RD."

Breaks if: "By the end of 2028, either of Nvidia's DGX SuperPOD reference architectures for its newest systems specifies a co-packaged optics switch as the default or only option for the compute fabric, or Nvidia or Broadcom says most of the AI switches it ships carry co-packaged optics, or either ships a co-packaged AI switch as standard whose lasers are fixed to the package rather than in replaceable modules."

Four earlier claims on the network:

**Marvell is paid every time AI chips talk, whoever made the chips** (28 September 2026)

Claim: "Marvell is paid every time AI chips talk, through the signal processor in each optical plug, whoever made the chips."

Breaks if: "The translation moves off the plug at scale, through linear pluggable or co-packaged optics, or Marvell's interconnect growth stalls while clusters keep growing."

Where later evidence bears on it: holding on the co-packaged leg for scale-out, since Nvidia's own reference design picks the pluggable switch. The main way that leg could break is SPIL's 15-fold target, if it is built. Two points cut against the claim. Hock Tan said on Broadcom's call of 2 September 2026, by a third-party transcript, "We're now the leader in leading edge optical DSPs", so the DSP is contested. And Marvell's filings describe its US$1 billion of prepayments as capacity reservations with foundries and partners for the whole business, not for optical DSPs alone. On 2 November 2026 Marvell agreed to buy Lumentum, the laser maker, in a deal expected to close in the first half of 2028.

**Broadcom is paid whether the cloud giants stay with Nvidia or leave** (2 October 2026)

Claim: "Broadcom is paid whether the cloud giants stay with Nvidia or leave for their own chips."

Breaks if: "Custom chip customers move work to other designers, as Google has partly done with MediaTek, or Nvidia's own networking wins inside its clusters."

Where later evidence bears on it: holding, but networking, the half paid if the cloud giants stay with Nvidia, has shrunk to 27% of AI revenue. Broadcom's 8-K of 6 April 2026 shows Anthropic accesses Google's TPU design through Broadcom, rather than designing its own chips.

**Corning makes the glass AI chips talk through** (1 October 2026)

Claim: "Glass fibre is the part of the AI network that outlives every chip generation, and Corning is paid each time a campus grows."

Breaks if: "Fibre stops being scarce as Corning and Chinese producers expand, shown by the segment's margin falling while its sales rise."

Where later evidence bears on it: holding. The segment's margin rose to 22.4% as sales grew 44% in the third quarter of 2026. Nvidia's US$500 million in Corning bought two warrants, by Corning's 8-K of 6 May 2026: a pre-funded warrant over 3 million shares and a second over 15 million. Supply is secured by a US$1.0 billion customer deposit, in the second quarter 10-Q. That 10-Q values the second warrant at US$296 million and deducts it from revenue as Corning delivers. So the largest buyer is paid as well as paying: the scarcity is shared, not kept, which leaves the claim standing but thinner.

**Nvidia paid Lumentum $2 billion for lasers** (5 October 2026)

Claim: "The AI network's bottleneck has moved to the laser, which only a few indium phosphide factories can make at volume."

Breaks if: "Lumentum's gross margin slides towards the low forties as new capacity arrives, or Coherent's six-inch wafers take the 200 gigabit EML orders, or silicon photonics routes around the EML."

Where later evidence bears on it: holding, with Lumentum still shipping behind demand and its GAAP gross margin at 51.0% in the quarter to 26 September 2026, by its results of 2 November. SPIL's 15-fold target bears on the silicon photonics leg: co-packaged engines need continuous lasers, not EMLs, so if it is built, part of the market routes around the EML. It does not route around the laser: on its call of 11 August 2026 Lumentum said it was further behind still on the high-power lasers for co-packaged optics. Lumentum's 8-K of 2 March 2026 shows Nvidia's US$2 billion bought 2,876,415 convertible preferred shares; the lasers sit under a separate purchase commitment of undisclosed size.

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

The three distances, with the evidence for each:

| Distance | Name | Medium today | What sets the limit | Evidence, dated |
|---|---|---|---|---|
| Inside a rack, a few metres | Scale-up | Copper | Copper signals fade past a few metres at today's speeds | Nvidia's GB200 NVL72 joins 72 GPUs in one NVLink domain at 130 TB/s; Google's TPU v4 joins 64 chips per cube by copper (paper, June 2023); Nvidia says its Kyber rack will carry "both copper and co-packaged optics scale-up", undated; its technical blog of the same day gives Vera Rubin Ultra NVL576, eight racks "with copper and direct optical connections", and Kyber NVL1152 with direct optical links between racks (16 March 2026) |
| Across a hall | Scale-out | Light, through plug-in transceivers and fibre | Plugs, power and switch tiers | One Tomahawk 6 moves 102.4 Tb/s, and two tiers join more than 100,000 chips (Broadcom, 3 June 2025); Google's mirror switches carry its pods' chip links past the rack, to 9,216 chips |
| Between sites, about 1,000 km | Scale-across | Dedicated long-distance fibre | The speed of light, about 5 microseconds per km | Microsoft joins Fairwater in Wisconsin and Atlanta; at least 5 ms one way |

The parts of a link between racks, by whether they are bought again:

| Layer | What it does | Bought again at each speed step? | What co-packaged optics does to it | Who makes it | Evidence, dated |
|---|---|---|---|---|---|
| Switch silicon | Routes traffic between racks | Yes, with each switch generation | Optical engines move onto its package | Broadcom, Nvidia, Marvell | Broadcom's AI networking was about 27% of US$16.7 billion of AI revenue, quarter to 2 August 2026, down from almost 40% in the quarter to 3 May |
| Optical DSP | Cleans and translates the signal inside each plug | Yes, one per plug | Removed; the switch drives the engine directly | Marvell, Broadcom | Marvell's data centre revenue was US$2.17 billion, 79% of the total, quarter to 1 August 2026; Marvell completed its purchase of Celestial AI, "optical interconnect technology for scale-up connectivity", on 2 February 2026 |
| Laser | Makes the light: EMLs in plugs, continuous lasers feeding co-packaged engines | Yes | Moved into a removable front-panel module | Lumentum, Coherent, Broadcom | Lumentum's GAAP gross margin was 51.0% in the quarter to 26 September 2026, against 47.4% in the June quarter and 34.0% a year earlier (non-GAAP 53.2%, 50.4% and 39.4%), by its results of 2 November 2026, which also report an NPO/CPO win backed by more than US$5 billion of purchase commitments; its Greensboro factory is expected to bring first revenue in early 2028; Broadcom says its indium phosphide factories are more than tripling capacity |
| Fibre | Carries the light | Usually not | Unchanged | Corning, Prysmian, Fujikura | Corning's optical segment sold US$2,379 million in the September 2026 quarter, up 44%, with segment net income of US$532 million (22.4%, against 21.1% the quarter before and 17.9% a year earlier); capital spending US$1,299 million in nine months, against US$850 million |
| Optical circuit switch | Steers light between fibres without reading it | No, it works at any data rate | Unchanged | Google, for itself; Lumentum | Google's whole optical layer was under 5% of a TPU v4 pod's cost and under 3% of its power, for 4,096 chips and 48 mirror switches (2023); the mirrors take milliseconds to settle, so they set the pod's shape before a job rather than routing each packet |

How much the network costs against the chips. The primary figures are narrow: in the quarter to April 2026, Nvidia sold US$14.8 billion of data centre networking against US$60.4 billion of compute, its last quarter with that split. That counts only Nvidia's own networking, not other makers' plugs, switches or fibre.

The scale-up ratio is my arithmetic: Nvidia gives Blackwell's NVLink as 1.8 TB/s per GPU, or 14.4 Tb/s; counted as both directions, that is 7.2 Tb/s each way, nine times an 800 Gb/s link. Nvidia's switch manual lists the SN6600-LD, pluggable, and the SN6810-LD, co-packaged, both at 102.4 Tb/s and both liquid-cooled (read 6 November 2026). The heat facts are from OIF's co-packaging panel at OFC (9 March 2023). The SPIL multiple of about 30 is my arithmetic from Nvidia's "15-fold" and "another doubling"; Nvidia gives no base figure. The Fairwater distance is my great-circle reckoning; Microsoft gives none.

</details>

<section class="exposure">
<h3>Who is exposed if the plug stays and the glass lasts</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>Switches</dt>
<dd><span class="names">Broadcom</span>, <span class="names">Nvidia</span> and <span class="names">Marvell</span> make switch chips. <span class="names">Arista</span> and <span class="names">Cisco</span> build the boxes.</dd>
<dt>Inside the plug</dt>
<dd><span class="names">Marvell</span> and <span class="names">Broadcom</span> make optical DSPs; <span class="names">Lumentum</span> and <span class="names">Coherent</span>, lasers. <span class="names">Coherent</span>, <span class="names">Innolight</span>, <span class="names">Eoptolink</span> and <span class="names">Fabrinet</span> build transceivers. The leading foundry and <span class="names">SPIL</span> make co-packaged engines.</dd>
<dt>Glass and mirrors</dt>
<dd><span class="names">Corning</span>, <span class="names">Prysmian</span> and <span class="names">Fujikura</span> make fibre. <span class="names">Google</span>, <span class="names">Lumentum</span> and <span class="names">Coherent</span> make optical circuit switches. <span class="names">Ciena</span> links distant sites.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Copper past a few metres, and plug DSP makers if co-packaged switches become the default.</dd>
</dl>
</section>

---

<p class="sources">Sources: Broadcom releases (June 2025 to March 2026), results and call (2 September 2026) and 8-K (6 April 2026); Marvell results, 10-Q and call (27 and 28 August 2026), Celestial AI release (2 February 2026) and Lumentum agreement (2 November 2026); Lumentum and Nvidia release and 8-K (2 March 2026), Lumentum results (11 August and 2 November 2026), call (11 August) and 10-K (17 August 2026); Corning results (28 July and 27 October 2026), 8-K (6 May 2026) and the Meta and Amazon agreements (27 January, 8 June 2026); Nvidia releases (18 March 2025, 26 August 2026, 21 October 2026), technical blogs (2025 and 16 March 2026), GTC update (16 March 2026), CFO commentary for the first quarter of fiscal 2027, SN6000 switch manual and DGX SuperPOD reference architecture (15 September 2026); OIF's co-packaging panel (March 2023) and ELSFP agreement (August 2023); Google's Apollo (2022) and TPU v4 (2023) papers, Ironwood documentation and TPU 8t post (April 2026); Microsoft's Fairwater posts (12 November 2025). The distance framing and several leads came from Leo Cui's video "The Entire AI Networking Industry Explained", a free YouTube video. Personal research, not investment advice.</p>
