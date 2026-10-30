---
title: "How ten thousand chips talk: the glass stays, the plug is bought again"
date: 2026-09-04
updated: 2026-10-30T14:20:52+08:00
updateNote: "Rewritten on 30 October 2026 as one deep piece, bringing together 5 earlier pieces, with a new section for investors."
summary: "An AI model is spread across thousands of chips that must swap results for every word they produce. Inside a rack they talk over copper; beyond it, over light made by lasers in small plugs and carried down glass fibre. The glass and the mirror switches stay for years, but the plugs are bought again at every speed step, and even the newest switches with built-in optics keep their lasers in a plug."
category: "Analysis"
cover: "/covers/ten-thousand-chips-one-thought.svg"
tags: ["networking", "optics", "the-stack"]
draft: false
---

A frontier AI model is too big for any single chip, so it is cut into pieces and spread across thousands. To produce each word, the pieces swap partial results, then do it all again.

How they talk depends on distance. Inside a rack, copper wire carries the traffic. Between racks, the signal becomes light, made by a laser in a small plug and sent down glass fibre.

The glass in the ceiling trays stays for years. The plugs at each end are bought again every time the chips get faster.

In the AI network, the glass stays and the plug is bought again.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A house is wired once. Want a brighter room and you buy new bulbs, while the wires in the walls stay put.</p>
<p>In an AI data centre the wires are glass fibre and the bulbs are lasers in plugs. Sealing bulbs into the ceiling saves power, but a dead one means taking the ceiling down. So builders kept the bulbs reachable.</p>
</details>

## How it works

The network covers three distances, and each has its own medium.

Inside a rack, dozens of chips are tied together so tightly they act as one machine. This is called scale-up, and it runs on copper, which is cheap and needs no translation.

Copper fades within a few metres at today's speeds. So the links between racks across a hall, called scale-out, run on light. At each end of a fibre sits an optical transceiver, a plug the size of a chewing gum packet. Inside it are a laser, a detector and a translator chip.

The furthest distance, between buildings, is called scale-across. There, even light is slow enough to matter.

Each new chip generation needs faster links, from 800 gigabits a second to 1.6 terabits. The plugs are replaced. The fibre usually is not, and neither are the mirror switches some clouds use, because they never read the data.

Switch makers now build the optics onto the switch itself, called co-packaged optics, to save power. But a part fixed to the switch cannot be swapped when it fails. So they kept the laser, the part that wears out first, in a plug.

## The number that matters

Fifteen times. That is how far SPIL, the Taiwanese packaging firm, aims to raise its capacity to build optical engines for co-packaged switches, the parts that turn electrical signals into light, mounted on the switch chip's own package rather than in a plug, by mid-2027, Nvidia said in October.

It is the size of the bet that optics move off the plug. It is a target, not a factory.

For now the plug is winning. In September Nvidia published its blueprint for a cluster of its newest systems, and picked the switch with ordinary plug-in optics.

Even if co-packaging spreads, the lasers stay in a module a technician can pull out by hand. What changes is who sells the translator inside the plug.

<hr class="layer">
<p class="layer-label">For investors</p>

<a id="ten-thousand-chips-one-thought"></a>
## The mechanism in depth

The network is priced by distance. Each distance sets the medium, and the medium sets which parts are bought once and which are bought again.

| Distance | Name | Medium today | What sets the limit | Evidence, dated |
|---|---|---|---|---|
| Inside a rack, a few metres | Scale-up | Copper | Copper signals fade past a few metres at today's speeds | Nvidia's GB200 NVL72 joins 72 GPUs in one NVLink domain at 130 TB/s; Google's TPU v4 joins 64 chips per cube by copper (paper, June 2023); Nvidia says its Kyber rack will carry "both copper and co-packaged optics scale-up", undated (16 March 2026) |
| Across a hall | Scale-out | Light, through plug-in transceivers and fibre | Plugs, power and switch tiers | One Tomahawk 6 moves 102.4 Tb/s, and two tiers join more than 100,000 chips (Broadcom, 3 June 2025); Google's mirror switches carry its pods' chip links past the rack, to 9,216 chips |
| Between sites, about 1,000 km | Scale-across | Dedicated long-distance fibre | The speed of light, about 5 microseconds per km | Microsoft joins Fairwater in Wisconsin and Atlanta; at least 5 ms one way |

Within scale-out, the parts split cleanly into those that turn over at each speed step and those that stay.

| Layer | What it does | Bought again at each speed step? | What co-packaged optics does to it | Who makes it | Evidence, dated |
|---|---|---|---|---|---|
| Switch silicon | Routes traffic between racks | Yes, with each switch generation | Optical engines move onto its package | Broadcom, Nvidia, Marvell | Broadcom's AI networking was about 27% of US$16.7 billion of AI revenue, quarter to 2 August 2026 |
| Optical DSP | Cleans and translates the signal inside each plug | Yes, one per plug | Removed; the switch drives the engine directly | Marvell, Broadcom | Marvell's data centre revenue was US$2.17 billion, 79% of the total, quarter to 1 August 2026 |
| Laser | Makes the light: EMLs in plugs, continuous lasers feeding co-packaged engines | Yes | Moved into a removable front-panel module | Lumentum, Coherent, Broadcom | Lumentum's GAAP gross margin rose from 33.3% to 47.4% in the year to the June 2026 quarter |
| Fibre | Carries the light | Usually not | Unchanged | Corning, Prysmian, Fujikura | Corning's optical segment sold US$2.38 billion in the September 2026 quarter, up 44% |
| Optical circuit switch | Steers light between fibres without reading it | No, it works at any data rate | Unchanged | Google, for itself; Lumentum | Google's whole optical layer was under 5% of a TPU v4 pod's cost and under 3% of its power (2023) |

How much does the network cost against the chips? My September Explainer said forty to sixty cents per chip dollar. I can find no primary source for that range, so I withdraw it.

The primary figures are narrower. In the quarter to April 2026, Nvidia sold US$14.8 billion of data centre networking against US$60.4 billion of compute, its last quarter with that split. That counts only Nvidia's own networking, not other makers' plugs, switches or fibre.

<a id="broadcom-wins-either-way"></a>
## The switch: Broadcom on both sides

Tomahawk 6 is Broadcom's flagship switch chip. Broadcom said on 3 June 2025 that two tiers of it can join more than 100,000 chips, and on 12 March 2026 that it was shipping in production volume.

Its chief of chips, Charlie Kawwas, said on 2 September 2026 that Tomahawk 6 is deployed at pretty much every AI customer building custom chips with Broadcom, and at some that are not. That is the half of Broadcom's toll paid by buyers who stay with Nvidia.

But the weight has moved. Networking fell from almost 40% of Broadcom's AI revenue in the quarter to 3 May 2026 to 27% in the quarter to 2 August. Custom chips made the rest.

Broadcom also makes lasers, and Kawwas said its indium phosphide factories are more than tripling capacity.

<a id="marvell-collects-the-toll"></a>
## The translator: Marvell's optical DSP

An optical DSP, a digital signal processor, sits inside each plug. It turns the switch's electrical signal into light at four brightness levels and back, through noise, billions of times a second. Marvell bought this business when it completed its purchase of Inphi in April 2021.

The plug needs one DSP, so DSP volume follows plug volume: more links per cluster, and new plugs at each speed step. Marvell's data centre business was US$2.17 billion in the quarter to 1 August 2026, 79% of its revenue.

On the call of 27 August 2026, chief executive Matt Murphy said pluggable modules remain the main form factor for scale-out, and he did not expect that to change.

Marvell is also hedging. It completed its purchase of Celestial AI on 2 February 2026, which it describes as "optical interconnect technology for scale-up connectivity". Where the translation leaves the plug, Marvell intends to be one of the firms taking it.

<a id="lumentum-makes-the-light"></a>
## The laser: why silicon cannot make it

Silicon is very poor at giving off light, so data centre lasers are grown on indium phosphide. Its wafers are small and brittle, and yields rest on process knowledge few factories have.

Lumentum's EMLs, electro-absorption modulated lasers, switch their beam on and off billions of times a second. In the June 2026 quarter, 200 gigabit EMLs passed a quarter of its EML revenue. Its GAAP gross margin, the share of each sale left after the cost of making it, rose from 33.3% to 47.4% in a year, which Lumentum put partly down to higher prices.

On 11 August 2026 chief executive Michael Hurlston said Lumentum was still shipping behind demand for EMLs. He said it was further behind on the high-power lasers that feed co-packaged optics. Its Greensboro factory is expected to bring first revenue in early 2028.

Co-packaging changes the laser's form, not its need. The engine on the switch is silicon photonics, optics built in silicon, but the light still comes from indium phosphide lasers in a front-panel module. Lumentum sells those lasers too: Hurlston's remark of 11 August was about them.

<a id="the-optics-you-cannot-unplug"></a>
## The package: optics onto the switch, lasers left in a plug

Ordinary plugs sit several inches of circuit board from the switch chip, and each needs its own DSP to push the signal across. Co-packaged optics mount optical engines on the switch package instead. Nvidia claims its co-packaged switches are 3.5 times more power efficient (18 March 2025).

Both makers ship them. Broadcom said on 8 October 2025 it was shipping Tomahawk 6 Davisson, with "Field-Replaceable ELSFP Laser Modules", a format the OIF standards body agreed in August 2023. Nvidia's blog of 26 August 2025 says Spectrum-X's optical engines are soldered on, while its lasers sit in removable modules for easy replacement.

That is the repair limit. A failed engine means replacing the switch, so the part that ages fastest was kept reachable.

Nvidia's results release of 26 August 2026 sells Spectrum-6 "supporting both pluggable and co-packaged optics". Its two DGX SuperPOD reference architectures for Vera Rubin both pick plug-in switches: the Spectrum-X version specifies the SN6600-LD (created 15 September 2026), and the InfiniBand version the Quantum-X800 Q3400-RD.

The other side is supply. On 21 October 2026 Nvidia said SPIL targets a 15-fold rise in co-packaged optical engine capacity by mid-2027, and another doubling by the end of 2028. Nvidia also lists "Spectrum-class optical scale-out" in its next platform, Feynman, without a date.

<a id="corning-lays-the-glass"></a>
## The glass: Corning

Fibre is the layer that stays when the plugs change, and the largest buyers have paid to secure it. Meta agreed in January 2026 to buy up to US$6 billion of Corning's fibre and cable through 2030. Amazon signed in June.

Corning's third quarter of 2026 was the claim's test. Optical Communications sold US$2,379 million, up 44% on a year earlier, and earned US$532 million of segment net income. That is 22.4% of sales, against 21.1% the quarter before and 17.9% a year earlier. Enterprise Networks, the data centre side, grew 84%.

Margin rising with sales is the opposite of what the claim's falsifier looks for. Capacity is coming: capital spending was US$1,299 million in the first nine months, against US$850 million a year earlier.

<a id="google-steers-the-light"></a>
## The mirrors: Google's optical circuit switches

Google joins the cubes of its TPU pods with Palomar, its own optical circuit switch. Two arrays of tilting gold-coated mirrors steer light from any of 136 fibres into any other, drawing at most 108 watts (Google's Apollo paper, August 2022).

Nothing in the box reads the data, so a faster chip sends more through the same mirrors. The mirrors take milliseconds to settle, so they set the pod's shape before a job rather than routing each packet.

Google's TPU v4 paper of June 2023 gives the cost. For 4,096 chips and 48 mirror switches, the whole optical layer, plugs and fibre included, came to under 5% of capital cost and under 3% of power. Ironwood pods of 9,216 chips still use them.

Google is no longer the only maker. Lumentum shipped more than US$90 million of optical circuit switches in its year to June 2026, without naming a buyer.

<a id="fairwater-spans-two-states"></a>
## Between sites: Microsoft's Fairwater

Light in fibre covers about 200 kilometres every millisecond. Microsoft's Fairwater campuses in Wisconsin and near Atlanta are about 1,000 km apart by my straight-line reckoning, so a message takes at least 5 ms one way.

Microsoft wrote on 12 November 2025 that large training jobs are outpacing the power and space of a single facility, and that the speed of light is now a key bottleneck. It joined the sites with a dedicated AI WAN, some of it on fibre bought years ago.

So only the least talkative work, such as averaging between copies of the model, can cross; the rest stays inside one building.

I have found no Microsoft or lab statement that a named model was trained across both Fairwater sites.

## Claims on record

Each claim is quoted word for word from the claims page, with the date its piece went live.

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

<a id="the-plug-stays"></a>

**New: how ten thousand chips talk** (30 October 2026)

Claim: "Between the racks of an AI cluster the optical plug stays the default through 2028: switches with co-packaged optics keep their lasers in removable front-panel modules, and Nvidia's reference designs for its newest systems keep specifying pluggable switches, as both Vera Rubin designs do today, with the Spectrum-X SN6600-LD and the InfiniBand Quantum-X800 Q3400-RD."

Breaks if: "By the end of 2028, either of Nvidia's DGX SuperPOD reference architectures for its newest systems specifies a co-packaged optics switch as the default or only option for the compute fabric, or Nvidia or Broadcom says most of the AI switches it ships carry co-packaged optics, or either ships a co-packaged AI switch as standard whose lasers are fixed to the package rather than in replaceable modules."

## What would prove me wrong

The first test is Nvidia's next reference architecture. If the blueprint for Feynman, or for any system before the end of 2028, specifies a co-packaged switch as the default or only option for the compute fabric, the plug has lost the hall.

The second is a statement of mix. If Nvidia or Broadcom says most AI switches it ships are co-packaged, the same holds.

The third is the laser. If a standard co-packaged switch fixes its lasers to the package, the repair limit I rest on was not binding. None of these tests says who wins the plug; only whether it stays.

## Research notes

Four initiation notes rest on these claims: [Marvell](/research/marvell/), [Broadcom](/research/broadcom/), [Corning](/research/corning/) and [Lumentum](/research/lumentum/). Each records where its piece was wrong.

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
