---
title: "Google joins its AI chips with tiny mirrors that never read the data"
date: 2026-10-29T18:37:08+08:00
summary: "Google links the racks in its giant AI chip pods through boxes of tiny tilting mirrors that bounce light from one fibre into another. Because nothing in the box reads the data, it uses almost no power, needs no extra plugs, and works just as well when the chips get faster. That is a large part of how Google's pods have grown past nine thousand chips."
category: "Analysis"
cover: "/covers/google-steers-the-light.svg"
tags: ["networking", "optics", "data-centres"]
draft: true
---

Google's Ironwood AI pods hold 9,216 chips each. The fibres between their racks run through boxes of tiny tilting mirrors.

Each mirror bounces a beam of light from one fibre into another. Nothing in the box reads the data, so nothing in it has to work hard.

Google designed those boxes itself, and they are a large part of why a Google pod can be this big, built rack by rack and rewired from a keyboard.

Inside its pods, Google does not switch the network. It steers the light.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Shine a torch at a bathroom mirror and tilt it. The beam lands wherever you aim, and the mirror works the same whether the torch flickers slowly or fast. A post room is the opposite: every letter is opened, read and resent.</p>
<p>A post room needs more staff for every extra sack of letters. Google filled its pods with mirrors, aimed once before the work starts and then left alone.</p>
</details>

## How a mirror replaces a switch

An ordinary network switch is a chip. Light from each fibre is turned into electricity by an optical transceiver, the plug that converts between the two, then read, sorted and turned back into light by another plug. Every hop costs two plugs and the power to read every packet, the small parcels data travels in.

Google's optical circuit switch, called Palomar, skips all of that. Inside, two arrays of gold-coated mirrors tilt on two axes, so light from any of 136 fibres can be steered into any other. Holding a mirror still takes almost no power, and Google says the whole box draws at most 108 watts. Because nothing reads the signal, a faster chip sends more data through the same mirrors.

The catch is how fast the mirrors move. They take milliseconds to settle, so they set the shape of the pod before a job rather than the route of each packet. Copper joins 64 chips inside each rack into a cube, and the mirrors join the cubes.

Supply cannot simply follow. Google picks the best mirrors from each die, aligns lenses to under a micron and steers each mirror by camera. It kept going, its engineers wrote, after other organisations gave up.

## What Google's own papers show

Google's 2023 paper on its TPU v4 pods puts a price on the mirrors. For 4,096 chips joined by 48 mirror switches, the whole optical layer, switches, plugs and fibre included, came to under 5 per cent of the system's cost and under 3 per cent of its power.

The mirrors also let each cube go into service as soon as it was installed, and let a job route around failed machines. For Ironwood, Google says the switches route around interruptions and restore the workload while services keep running. Its next training pods, announced in April, reach 9,600 chips and still use them.

Google is no longer the only maker of these switches. Lumentum shipped more than $90 million of them in its year to June 2026, without naming a buyer. I expect the mirrors to leave Google's pods for other clouds' AI clusters.

## What would prove me wrong

I am wrong if, by the end of 2027, no second cloud giant has said in its own paper, blog or filing that optical circuit switches join chips in a production AI cluster.

Lumentum's annual report for fiscal 2027 could also settle it, by describing a buyer besides Google. If neither happens, the mirrors stayed a Google habit.

<section class="exposure">
<h3>Who is exposed if mirrors, not switch chips, join Google's AI pods</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The figures are the companies' own disclosures, used as evidence for the mechanism.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Google</span> designs its TPU AI chips and designs the Palomar mirror switches that join them.</dd>
<dt>Other optical circuit switch makers</dt>
<dd><span class="names">Lumentum</span> makes optical circuit switches. <span class="names">Coherent</span> is developing switches built on liquid crystal.</dd>
<dt>The light at each end</dt>
<dd><span class="names">Innolight</span> and <span class="names">Coherent</span> make transceivers. <span class="names">Corning</span> makes the fibre.</dd>
<dt>The electrical route</dt>
<dd><span class="names">Nvidia</span> makes NVLink and InfiniBand switches. <span class="names">Broadcom</span> makes Ethernet switch chips, and <span class="names">Arista</span> the switches.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Electrical switch chips, and the plugs at every hop, wherever a layer of mirrors replaces them, and Google itself if mirrors cannot keep up as pods grow.</dd>
</dl>
</section>

---

<p class="sources">Sources: Google's Apollo (2022) and TPU v4 (2023) papers, its Ironwood posts of 2025, TPU7x documentation and TPU 8t post of 23 April 2026, and Lumentum's and Coherent's fiscal 2026 annual reports, with the lead from a YouTube video on AI networking. Personal research, not investment advice.</p>
