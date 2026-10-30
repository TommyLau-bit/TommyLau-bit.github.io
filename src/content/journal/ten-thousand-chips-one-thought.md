---
title: "How ten thousand chips talk: the glass stays, and the plug survives its replacement"
date: 2026-09-04
updated: 2026-10-31T08:00:00+08:00
updateNote: "Rewritten on 31 October 2026 as one story with three charts; earlier claims are kept word for word at the end."
summary: "An AI model is spread across thousands of chips that swap results for every word they produce, over copper inside a rack and over light between racks. The glass that carries the light stays for years, while the plugs that make it are bought again at every speed step. Switch makers have built optics onto the switch to retire the plug, yet they kept the laser in one, and Nvidia's newest blueprints still pick the plug."
category: "Analysis"
cover: "/covers/ten-thousand-chips-one-thought.svg"
tags: ["networking", "optics", "the-stack"]
draft: false
---

Nvidia and Broadcom have spent years building network switches that do away with the optical plug. Both now sell them. Yet both kept the laser, the part that makes the light, in a plug a technician can pull out by hand.

And when Nvidia published its blueprints for clusters of its newest systems in September, both blueprints picked the switch with ordinary plugs.

That is not hesitation. In an AI network, the parts that only carry light, the glass fibre and the mirror switches some clouds use, stay for years. The parts that make and read the light are bought again every time the chips get faster, so they are kept where a hand can reach them. The plug is not on its way out. On the makers' own designs it is still the default between racks, and I expect it to stay so through 2028.

The network exists because a frontier AI model is too big for any one chip. It is cut into pieces and spread across thousands. To produce each word, the pieces swap partial results, then do it all again.

How they talk depends on distance. Inside a rack, dozens of chips are tied together by copper so tightly they act as one machine. Copper fades within a few metres at today's speeds, so between racks the signal becomes light. At each end of a fibre sits a plug the size of a chewing gum packet, holding a laser, a detector and a translator chip. Between buildings, hundreds of kilometres apart, even light is slow enough to matter.

Each new chip generation needs faster links, from 800 gigabits a second to 1.6 terabits. The plugs are replaced. The fibre usually is not, and neither are the mirror switches, because they never read the data.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A house is wired once. Want a brighter room and you buy new bulbs, while the wires in the walls stay put.</p>
<p>In an AI data centre the wires are glass fibre and the bulbs are lasers in plugs. Sealing bulbs into the ceiling saves power, but a dead one means taking the ceiling down. So builders kept the bulbs reachable.</p>
</details>

Switch makers want the optics on the switch itself, called co-packaged optics, because it saves power. But a part fixed to the switch cannot be swapped when it fails, and lasers have long been among the least reliable parts of data centre optics. So they left the laser in a plug.

The case against is a factory plan. SPIL, a Taiwanese packaging firm, aims to raise its capacity for co-packaged optical parts fifteen times by mid-2027, Nvidia said in October. That is a target, not a factory. Even if it is built, the lasers stay in a module a hand can pull out. What it changes is who sells the translator inside the plug.

<hr class="layer">
<p class="layer-label">For investors</p>

<a id="ten-thousand-chips-one-thought"></a>
## Distance sets the medium, and the medium sets what is bought again

The network is priced by distance, because each distance needs its own medium. Inside a rack it is copper: Nvidia's GB200 NVL72 joins 72 GPUs in one NVLink domain at 130 TB/s, and Google's TPU v4 joins 64 chips per cube the same way. Copper needs no translation, which is why it holds the shortest links.

Across a hall it is light. One Broadcom Tomahawk 6 switch chip moves 102.4 Tb/s, and Broadcom said on 3 June 2025 that two tiers of them join more than 100,000 chips. Those links run through a plug at each end and a fibre between.

<a id="fairwater-spans-two-states"></a>

Between sites it is long fibre, and there the limit is physics. Light in fibre covers about 200 kilometres a millisecond, and Microsoft's Fairwater campuses in Wisconsin and near Atlanta are about 1,000 km apart by my straight-line reckoning, so a message takes at least 5 ms one way. Microsoft wrote on 12 November 2025 that the speed of light is now a key bottleneck. So only the least talkative work, such as averaging between copies of the model, can cross. I have found no Microsoft or lab statement that a named model was trained across both sites.

Within the hall, the parts split cleanly by what they do to the signal.

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

## Every speed step buys the switch, the translator and the laser again

The parts that read or make the signal are replaced at each speed step, and in 2026 all three were selling strongly, the laser faster than it could be made.

<a id="broadcom-wins-either-way"></a>

The switch chip comes first. Broadcom said on 12 March 2026 that Tomahawk 6 was shipping in production volume, and its chief of chips, Charlie Kawwas, said on 2 September that it is deployed at pretty much every AI customer building custom chips with Broadcom, and at some that are not.

<a id="marvell-collects-the-toll"></a>

The translator comes next. An optical DSP, a digital signal processor, sits inside each plug and turns the switch's electrical signal into light and back, so DSP volume follows plug volume. Marvell, which bought this business with Inphi in 2021, had data centre revenue of US$2.17 billion in the quarter to 1 August 2026, 79% of its total, and its chief executive said on 27 August that plugs remain the main form for links between racks.

<a id="lumentum-makes-the-light"></a>

The laser is the hardest to add. Silicon is very poor at giving off light, so data centre lasers are grown on indium phosphide, on small, brittle wafers that few factories can yield well. Lumentum's EMLs, the fast-switching lasers in today's plugs, show the speed step directly: in the June 2026 quarter, 200 gigabit EMLs passed a quarter of its EML revenue. Its chief executive said on 11 August that it was still shipping behind demand, and its gross margin had risen from 33.3% to 47.4% in a year, partly on higher prices.

## The glass and the mirrors are bought once

The parts that only carry or steer light do not care how fast the chips are, so they are bought when a building is built and then left alone.

<a id="corning-lays-the-glass"></a>

Fibre is the clearest case, and the largest buyers have paid to secure it. Meta agreed in January 2026 to buy up to US$6 billion of Corning's fibre and cable through 2030, and Amazon signed in June. Corning's optical sales rose 44% in the third quarter of 2026, with the data centre side up 84%, and the segment's margin rose to 22.4% from 17.9% a year earlier: glass grows with new campuses, not with speed steps.

<a id="google-steers-the-light"></a>

The mirror switch is the other. Google joins the cubes of its TPU pods with Palomar, its own optical circuit switch, in which tilting mirrors steer light from any of 136 fibres into any other, drawing at most 108 watts. Nothing in the box reads the data, so a faster chip sends more through the same mirrors, and Google's Ironwood pods of 9,216 chips still use them. Lumentum shipped more than US$90 million of such switches in its year to June 2026, so Google is no longer the only maker.

## Co-packaging was built to retire the plug

The plug's weakness is distance on the circuit board, and co-packaged optics was designed to remove it. An ordinary plug sits several inches of board from the switch chip, and each needs its own DSP to push the signal across. Co-packaged optics mounts small optical engines on the switch package itself, which Nvidia claims makes its switches 3.5 times more power efficient (18 March 2025).

<a id="the-optics-you-cannot-unplug"></a>

Both makers now ship such switches. Broadcom said on 8 October 2025 it was shipping Tomahawk 6 Davisson, and Nvidia sells its own. Done fully, this would remove the plug, and the DSP inside it, from the links between racks.

## The laser stayed in a plug, where it can be replaced

Neither maker went all the way. The engines that turn electricity into light are fixed to the package, but the lasers that feed them sit in modules at the front of the switch.

Nvidia's technical blog of 26 August 2025 says Spectrum-X's optical engines are soldered on, while its lasers sit in removable modules for easy replacement. Broadcom's Davisson ships with "Field-Replaceable ELSFP Laser Modules", a format the OIF standards body agreed in August 2023. A failed engine means replacing the whole switch, so the laser, which Nvidia calls one of the most persistent reliability problems in data centre optics, was kept reachable.

The laser itself is still bought. Co-packaged engines take continuous lasers rather than the fast-switching kind in today's plugs, and on 11 August 2026 Lumentum said it was further behind demand on those than on its plug lasers. Co-packaging changes the laser's form, not its need, and not its place in a plug.

## Nvidia's own blueprint still picks the plug

The strongest evidence comes from the company with the most to gain from co-packaging. Nvidia sells both kinds of switch: its results release of 26 August 2026 offers Spectrum-6 "supporting both pluggable and co-packaged optics".

Yet when Nvidia published its DGX SuperPOD reference architectures for Vera Rubin, its newest systems, both picked plug-in switches. The Spectrum-X version, created 15 September 2026, specifies the SN6600-LD; the InfiniBand version specifies the Quantum-X800 Q3400-RD. A reference architecture is the blueprint customers copy, so its choice is the default.

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

So the order of events is the argument. Nvidia announced co-packaged switches, shipped them, sold them alongside plugs, and then, for its own flagship clusters, chose plugs.

## What could retire the plug

The case against is real, and Nvidia is funding it. On 21 October 2026 it said SPIL targets a 15-fold rise in co-packaged optical engine capacity by mid-2027, and another doubling by the end of 2028. Nvidia also lists "Spectrum-class optical scale-out" in Feynman, its next platform, without a date.

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

The translator in the plug is contested too. Broadcom's chief executive said on 2 September 2026, by a third-party transcript, "We're now the leader in leading edge optical DSPs".

None of this retires the plug by itself. A target is not a factory, and even a co-packaged switch keeps its lasers in front-panel modules. What it does threaten is the DSP: where the switch drives the engine directly, the translator leaves the plug. If a Feynman blueprint picks a co-packaged switch before the end of 2028, my claim breaks.

## The glass stays, and so does the plug

The makers built switches to retire the plug, and then kept one. The reason is the split at the heart of the network: glass and mirrors that only carry light are bought once, while the parts that make light need replacing and change with every speed step. A part that must be replaced has to be reachable. The house is wired once, and the bulbs stay where a hand can reach them.

## Claims on record

The test this piece stands behind, quoted word for word from the claims page:

<a id="the-plug-stays"></a>

**The plug stays the default between racks through 2028** (30 October 2026)

Claim: "Between the racks of an AI cluster the optical plug stays the default through 2028: switches with co-packaged optics keep their lasers in removable front-panel modules, and Nvidia's reference designs for its newest systems keep specifying pluggable switches, as both Vera Rubin designs do today, with the Spectrum-X SN6600-LD and the InfiniBand Quantum-X800 Q3400-RD."

Breaks if: "By the end of 2028, either of Nvidia's DGX SuperPOD reference architectures for its newest systems specifies a co-packaged optics switch as the default or only option for the compute fabric, or Nvidia or Broadcom says most of the AI switches it ships carry co-packaged optics, or either ships a co-packaged AI switch as standard whose lasers are fixed to the package rather than in replaceable modules."

<details class="claims-earlier">
<summary>Four earlier claims on the network, quoted word for word</summary>

**Marvell is paid every time AI chips talk, whoever made the chips** (28 September 2026)

Claim: "Marvell is paid every time AI chips talk, through the signal processor in each optical plug, whoever made the chips."

Breaks if: "The translation moves off the plug at scale, through linear pluggable or co-packaged optics, or Marvell's interconnect growth stalls while clusters keep growing."

Where later evidence bears on it: holding on the co-packaged leg for scale-out, since Nvidia's own reference design picks the pluggable switch. The main way that leg could break is SPIL's 15-fold target, if it is built. Two points cut against the piece. Hock Tan said on Broadcom's call of 2 September 2026, by a third-party transcript, "We're now the leader in leading edge optical DSPs", so the DSP is contested. And where I was wrong: the piece tied Marvell's US$1 billion of prepayments to optical DSPs; its filings describe capacity reservations with foundries and partners for the whole business.

**Broadcom is paid whether the cloud giants stay with Nvidia or leave** (2 October 2026)

Claim: "Broadcom is paid whether the cloud giants stay with Nvidia or leave for their own chips."

Breaks if: "Custom chip customers move work to other designers, as Google has partly done with MediaTek, or Nvidia's own networking wins inside its clusters."

Where later evidence bears on it: holding, but the stay half has shrunk to 27% of AI revenue. Where I was wrong: the piece said Anthropic designs its own chips with Broadcom. Broadcom's 8-K of 6 April 2026 shows Anthropic accesses Google's TPU design through Broadcom.

**Corning makes the glass AI chips talk through** (1 October 2026)

Claim: "Glass fibre is the part of the AI network that outlives every chip generation, and Corning is paid each time a campus grows."

Breaks if: "Fibre stops being scarce as Corning and Chinese producers expand, shown by the segment's margin falling while its sales rise."

Where later evidence bears on it: holding. The segment's margin rose to 22.4% as sales grew 44% in the third quarter of 2026. Where I was wrong: the piece said Nvidia paid Corning to build more fibre. Corning's 8-K of 6 May 2026 shows the US$500 million bought two warrants: a pre-funded warrant over 3 million shares and a second over 15 million. Supply is secured by a US$1.0 billion customer deposit, in the second quarter 10-Q. That 10-Q values the second warrant at US$296 million and deducts it from revenue as Corning delivers. So the largest buyer is paid as well as paying: the scarcity is shared, not kept, which leaves the claim standing but thinner.

**Nvidia paid Lumentum $2 billion for lasers** (5 October 2026)

Claim: "The AI network's bottleneck has moved to the laser, which only a few indium phosphide factories can make at volume."

Breaks if: "Lumentum's gross margin slides towards the low forties as new capacity arrives, or Coherent's six-inch wafers take the 200 gigabit EML orders, or silicon photonics routes around the EML."

Where later evidence bears on it: holding, with Lumentum still shipping behind demand. SPIL's 15-fold target bears on the silicon photonics leg: co-packaged engines need continuous lasers, not EMLs, so if it is built, part of the market routes around the EML. It does not route around the laser: on its call of 11 August 2026 Lumentum said it was further behind still on the high-power lasers for co-packaged optics. Where I was wrong: the headline. Lumentum's 8-K of 2 March 2026 shows Nvidia's US$2 billion bought 2,876,415 convertible preferred shares; the lasers sit under a separate purchase commitment of undisclosed size.

</details>

## What would prove me wrong

The first test is Nvidia's next reference architecture. If the blueprint for Feynman, or for any system before the end of 2028, specifies a co-packaged switch as the default or only option for the compute fabric, the plug has lost the hall.

The second is a statement of mix: if Nvidia or Broadcom says most AI switches it ships are co-packaged, the same holds. The third is the laser: if a standard co-packaged switch fixes its lasers to the package, the repair limit I rest on was not binding. None of these tests says who wins the plug, only whether it stays.

## Research notes

Four initiation notes rest on these claims: [Marvell](/research/marvell/), [Broadcom](/research/broadcom/), [Corning](/research/corning/) and [Lumentum](/research/lumentum/). Each records where its piece was wrong.

<details class="evidence">
<summary>The figures behind the charts</summary>

The three distances, with the evidence for each:

| Distance | Name | Medium today | What sets the limit | Evidence, dated |
|---|---|---|---|---|
| Inside a rack, a few metres | Scale-up | Copper | Copper signals fade past a few metres at today's speeds | Nvidia's GB200 NVL72 joins 72 GPUs in one NVLink domain at 130 TB/s; Google's TPU v4 joins 64 chips per cube by copper (paper, June 2023); Nvidia says its Kyber rack will carry "both copper and co-packaged optics scale-up", undated (16 March 2026) |
| Across a hall | Scale-out | Light, through plug-in transceivers and fibre | Plugs, power and switch tiers | One Tomahawk 6 moves 102.4 Tb/s, and two tiers join more than 100,000 chips (Broadcom, 3 June 2025); Google's mirror switches carry its pods' chip links past the rack, to 9,216 chips |
| Between sites, about 1,000 km | Scale-across | Dedicated long-distance fibre | The speed of light, about 5 microseconds per km | Microsoft joins Fairwater in Wisconsin and Atlanta; at least 5 ms one way |

The parts of a link between racks, by whether they are bought again:

| Layer | What it does | Bought again at each speed step? | What co-packaged optics does to it | Who makes it | Evidence, dated |
|---|---|---|---|---|---|
| Switch silicon | Routes traffic between racks | Yes, with each switch generation | Optical engines move onto its package | Broadcom, Nvidia, Marvell | Broadcom's AI networking was about 27% of US$16.7 billion of AI revenue, quarter to 2 August 2026, down from almost 40% in the quarter to 3 May |
| Optical DSP | Cleans and translates the signal inside each plug | Yes, one per plug | Removed; the switch drives the engine directly | Marvell, Broadcom | Marvell's data centre revenue was US$2.17 billion, 79% of the total, quarter to 1 August 2026; Marvell completed its purchase of Celestial AI, "optical interconnect technology for scale-up connectivity", on 2 February 2026 |
| Laser | Makes the light: EMLs in plugs, continuous lasers feeding co-packaged engines | Yes | Moved into a removable front-panel module | Lumentum, Coherent, Broadcom | Lumentum's GAAP gross margin rose from 33.3% to 47.4% in the year to the June 2026 quarter; its Greensboro factory is expected to bring first revenue in early 2028; Broadcom says its indium phosphide factories are more than tripling capacity |
| Fibre | Carries the light | Usually not | Unchanged | Corning, Prysmian, Fujikura | Corning's optical segment sold US$2,379 million in the September 2026 quarter, up 44%, with segment net income of US$532 million (22.4%, against 21.1% the quarter before and 17.9% a year earlier); capital spending US$1,299 million in nine months, against US$850 million |
| Optical circuit switch | Steers light between fibres without reading it | No, it works at any data rate | Unchanged | Google, for itself; Lumentum | Google's whole optical layer was under 5% of a TPU v4 pod's cost and under 3% of its power, for 4,096 chips and 48 mirror switches (2023); the mirrors take milliseconds to settle, so they set the pod's shape before a job rather than routing each packet |

How much the network costs against the chips. My September Explainer said forty to sixty cents per chip dollar. I can find no primary source for that range, so I withdraw it. The primary figures are narrower: in the quarter to April 2026, Nvidia sold US$14.8 billion of data centre networking against US$60.4 billion of compute, its last quarter with that split. That counts only Nvidia's own networking, not other makers' plugs, switches or fibre.

The SPIL multiple of about 30 is my arithmetic from Nvidia's "15-fold" and "another doubling"; Nvidia gives no base figure. The Fairwater distance is my great-circle reckoning; Microsoft gives none.

</details>

<section class="exposure">
<h3>Who is exposed if the plug stays and the glass lasts</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>Switches</dt>
<dd><span class="names">Broadcom</span>, <span class="names">Nvidia</span> and <span class="names">Marvell</span> make switch chips. <span class="names">Arista</span> and <span class="names">Cisco</span> build the boxes.</dd>
<dt>Inside the plug</dt>
<dd><span class="names">Marvell</span> and <span class="names">Broadcom</span> make optical DSPs; <span class="names">Lumentum</span> and <span class="names">Coherent</span>, lasers. <span class="names">Innolight</span>, <span class="names">Eoptolink</span> and <span class="names">Fabrinet</span> build transceivers. <span class="names">TSMC</span> and <span class="names">SPIL</span> make co-packaged engines.</dd>
<dt>Glass and mirrors</dt>
<dd><span class="names">Corning</span>, <span class="names">Prysmian</span> and <span class="names">Fujikura</span> make fibre. <span class="names">Google</span> and <span class="names">Lumentum</span> make optical circuit switches. <span class="names">Ciena</span> links distant sites.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Copper past a few metres, and plug DSP makers if co-packaged switches become the default.</dd>
</dl>
</section>

---

<p class="sources">Sources: Broadcom releases (3 June 2025, 8 October 2025, 12 March 2026), third quarter fiscal 2026 results and call (2 September 2026) and 8-K (6 April 2026); Marvell results, 10-Q and call (27 and 28 August 2026) and Celestial AI release (2 February 2026); Lumentum and Nvidia joint release and 8-K (2 March 2026), Lumentum results and call (11 August 2026) and 10-K (17 August 2026); Corning results (28 July and 27 October 2026), 8-K (6 May 2026) and the Meta and Amazon agreements (27 January, 8 June 2026); Nvidia releases (18 March 2025, 26 August 2026, 21 October 2026), technical blogs (27 March, 26 August 2025), GTC update (16 March 2026), CFO commentary for the first quarter of fiscal 2027 and DGX SuperPOD reference architecture (15 September 2026); the OIF ELSFP agreement (August 2023); Google's Apollo (2022) and TPU v4 (2023) papers, Ironwood documentation and TPU 8t post (April 2026); Microsoft's Fairwater posts (12 November 2025). The distance framing and several leads came from Leo Cui's video "The Entire AI Networking Industry Explained", a free YouTube video. Personal research, not investment advice.</p>
