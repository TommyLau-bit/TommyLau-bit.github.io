---
title: "Nvidia and Broadcom moved the optics onto the switch, but kept the lasers in a plug"
date: 2026-10-29T18:40:26+08:00
summary: "Nvidia and Broadcom now make network switches with the light-making parts built in beside the main chip, which saves power. Both still put the lasers in removable plugs, and Nvidia's own design for its newest AI clusters uses the ordinary plug-in version of its switch. I expect built-in optics to stay an option, not the default, through 2028."
category: "Analysis"
cover: "/covers/the-optics-you-cannot-unplug.svg"
tags: ["networking", "optics", "data-centres"]
draft: true
---

Nvidia's September 2026 blueprint for a cluster of its newest Vera Rubin systems picks a switch, the box that routes traffic between racks. It picks the version with ordinary plug-in optics.

Nvidia also makes that switch with co-packaged optics, where the light-making parts sit on the switch chip's own package. So does Broadcom, with its Tomahawk 6 Davisson.

Yet both firms left one part outside: the lasers sit in modules on the front panel.

Nvidia and Broadcom moved the optics onto the switch. They left the lasers, and the choice, in a plug.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A light panel sealed into the ceiling is neater and cheaper to run than a lamp with a screw-in bulb. But when it fails, someone has to take the ceiling down. So the best sealed panels keep the part that dies first in a small box you can reach.</p>
<p>Nvidia and Broadcom sealed the optics into the switch and kept the lasers in that box. Most buyers, for now, still take the lamp.</p>
</details>

## Why the lasers stayed outside

Nvidia's co-packaged switches hold their lasers in plug-in modules on the front panel, each feeding light to the engines on the chip. Its own blog says this allows quick diagnosis and easy replacement. Broadcom lists field-replaceable laser modules on Davisson, in a format a standards body agreed in 2023.

The reason is the optical engine, the part that turns the chip's signal into light. It is fixed to the switch package, and on Nvidia's Spectrum-X version it is soldered on. If it fails, the repair is the whole switch, not a module. So the lasers, which age fastest, were kept where a technician can reach them.

The gain is power. Ordinary plugs sit several inches of circuit board from the chip, and each needs its own signal processor to push the signal across. Nvidia claims its co-packaged switches are 3.5 times more power efficient.

Supply cannot make this the default quickly either. Nvidia says its packaging partner SPIL aims to raise co-packaged engine capacity 15 times by mid-2027, a target rather than a factory.

## What Nvidia and Broadcom do

Broadcom said it was shipping Davisson in October 2025. Nvidia's results release of 26 August 2026 describes its Spectrum-6 switches as "supporting both pluggable and co-packaged optics". The buyer chooses.

Nvidia's blueprint chose the plug, and its server network cards take plug-in modules too. Neither company's latest earnings call mentioned co-packaged optics. Meta's lab test of Broadcom's co-packaged optics, reported by Broadcom, logged a million port hours without a link dropping. Reliability is not the obstacle; repair and choice are.

## What would prove me wrong

I am wrong if, by the end of 2028, Nvidia's blueprint for its newest systems specifies co-packaged switches, or Nvidia or Broadcom says most AI switches it ships carry them.

That would also break one leg of my Marvell claim: that Marvell is paid through the signal processor in each optical plug, unless co-packaged or linear optics move that job off the plug at scale, or its growth stalls.

<section class="exposure">
<h3>Who is exposed if co-packaged optics stay an option, not the default</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The subjects</dt>
<dd><span class="names">Nvidia</span> makes Quantum-X and Spectrum-X Photonics switches and server network cards. <span class="names">Broadcom</span> makes Tomahawk switch chips, co-packaged optics and lasers.</dd>
<dt>Who builds the optical engines</dt>
<dd><span class="names">TSMC</span> makes the silicon photonics. <span class="names">SPIL</span> packages and tests the engines. <span class="names">Lumentum</span> makes laser chips.</dd>
<dt>The plug</dt>
<dd><span class="names">Marvell</span> makes optical signal processors. <span class="names">Coherent</span>, <span class="names">Innolight</span> and <span class="names">Eoptolink</span> make pluggable transceivers.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Operators who must replace a whole switch when a soldered engine fails, and makers of plug signal processors if co-packaged optics become the default.</dd>
</dl>
</section>

---

<p class="sources">Sources: Nvidia and Broadcom product releases, technical blogs and manuals, 2025 and 2026, Nvidia's DGX SuperPOD reference architecture of September 2026, both companies' earnings calls of August and September 2026, and the OIF laser module standard, with the lead from Leo Cui's networking video. Personal research, not investment advice.</p>
