---
title: "Marvell is paid every time AI chips talk to each other, whoever made the chips"
date: 2026-09-28T13:25:16+08:00
summary: "Marvell makes the small chips that turn electrical signals into light and back again, so AI processors in different cabinets can share their work. Whichever company's AI chip wins, the cluster still needs those links, and it needs more of them as it grows. Marvell also helps the big cloud companies design their own AI chips, which is the riskier half of the story."
category: "Analysis"
cover: "/covers/marvell-collects-the-toll.svg"
tags: ["networking", "optics", "data-centres"]
---

Most people who follow AI hardware are watching one contest. Nvidia's GPUs against Google's chips, Amazon's chips and everyone else's. Marvell sits somewhere that contest barely reaches.

Marvell makes the parts that let AI chips talk. When two processors in different cabinets swap results, the signal leaves one as electricity, crosses the hall as light and arrives at the other as electricity again. The chip doing the translation at each end is very often a Marvell part.

It also helps the largest cloud companies design their own AI processors. That half gets the headlines. The first half interests me more, because it is a charge on how big the cluster gets rather than a bet on which chip wins.

Marvell is paid every time AI chips talk, whoever made the chips.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Call to someone at the end of your garden and they hear you fine. Call to someone three streets away and your words smear into noise, however loudly you shout.</p>
<p>Shouting harder does not fix it. What works is a torch: flashes of light carry across distances a voice never will. But someone has to turn your words into flashes, and someone at the far end has to turn the flashes back into words, quickly and without a single mistake.</p>
<p>Those two people do not care who is talking. Every conversation needs them, and the more people want to talk, and the faster, the more of them you need. That is the job Marvell does inside an AI data centre.</p>
</details>

## Three words you need

**Optical DSP.** A DSP, a digital signal processor, is a chip that cleans up and reshapes a signal. The optical kind sits inside the plug at each end of a fibre cable and handles the translation between electricity and light.

**800G and 1.6T.** How much data one of those plugs moves per second: 800 gigabits for the current workhorse, 1.6 terabits for the generation now ramping. Each step doubles the traffic through the same small plug.

**XPU.** An industry label for a custom AI chip, designed for one company's own workload rather than sold to everyone. A GPU is a general tool. An XPU does one job, more cheaply.

## Where copper stops and Marvell starts

AI models are too large for one chip, so they are split across thousands, and those chips exchange partial results constantly. As I wrote in an earlier piece, a network even slightly slow leaves the most expensive silicon ever built waiting.

Inside a cabinet, copper carries most of that traffic. Between cabinets it cannot. At today's speeds an electrical signal degrades within a few metres, so everything leaving the rack is converted to light and sent down glass fibre.

That conversion lives in a plug about the size of a pack of gum, called an optical transceiver, which slots into the front of a network switch. Inside it are a laser, a light detector and the optical DSP. The DSP is the hard part.

Signals at these speeds are not simple on and off pulses. The standard, called PAM4, sends four levels of brightness so each pulse carries two bits. Telling four levels apart, billions of times a second, through noise and distortion, takes a lot of processing. Every doubling in speed makes it harder.

Marvell bought this capability. In April 2021 it completed its purchase of Inphi, the leader in these electro-optical chips, and the DSP inside many of today's transceivers traces back to that deal.

Here is why it works as a toll. The plug neither knows nor cares whether the chip behind the switch came from Nvidia, AMD, Google or Amazon. A bigger cluster means more links, and a faster generation of chips means replacing the links. Both raise the count.

## The second job, and where I stop

Marvell's other data centre business is custom silicon. A cloud company knows what it wants its own AI chip to do. Marvell turns that into a working design and manages its manufacture with TSMC, the Taiwanese foundry that makes it.

Broadcom does the same job and is larger at it. The customers are few and enormous, and each one also runs its own chip team. That makes custom silicon a very different business from the optics, with lumpier programmes and stronger buyers.

This is where I stop. Judging chip design programmes needs knowledge of semiconductor design I do not claim. What I can say is physical: every custom chip Marvell helps build still has to talk to the others, so it still needs the links.

## What Marvell's own numbers show

If the toll is real, data centre revenue should outgrow the rest of Marvell, and the company should be scrambling for supply of optical parts.

**Mix.** In the fourth quarter of fiscal 2026, reported on 5 March 2026, data centre revenue was 74 per cent of the total. By the second quarter of fiscal 2027, reported on 27 August 2026, it was 79 per cent, $2.17 billion, up 46 per cent on a year earlier.

**Scale.** Fiscal 2026 revenue was $8.195 billion, up 42 per cent. Management's own outlook is about $12 billion for fiscal 2027 and $18 billion for fiscal 2028. Those are Marvell's forecasts, not mine.

**Supply.** On the same call, Marvell said it would make about $1 billion of capacity prepayments to suppliers in fiscal 2027, to secure supply of 1.6T optical DSPs and switch chips. Paying ahead to hold manufacturing capacity is what a supplier does when demand is outrunning the factories.

**Concentration.** In fiscal 2026, Marvell's ten largest customers made up 82 per cent of revenue, according to its annual report. That is the cost of selling into a handful of giant buildings.

The margin tells the same split. Marvell flagged the custom ramp as a drag on gross margin, the share of each sale left after the cost of making it, in the third quarter. Custom work is the part where powerful buyers set the price.

## What would prove me wrong

I am wrong if the translation moves off the plug. Two approaches aim to do exactly that. Linear pluggable optics drop the DSP from the transceiver and let the switch chip do the cleaning. Co-packaged optics go further and put the light conversion on the switch package itself.

Both save power, which matters when each watt spent moving data is a watt not spent computing. If either spreads at scale, the translation job moves to whoever makes the switch chip. Marvell makes switch chips and is developing co-packaged parts, but it would be competing on different ground.

I am also wrong if Marvell's interconnect growth stalls while clusters keep growing. That would mean the toll is being collected by someone else.

So I watch three things. Whether 1.6T links keep a DSP on board. How much of Marvell's growth comes from optics rather than custom chips. And whether the ten largest customers keep rising as a share of revenue.

<section class="exposure">
<h3>Who is exposed if the link, not the chip, is the toll</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are Marvell's own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Marvell</span> makes optical DSPs, Ethernet switch chips, data centre interconnect modules and custom AI chips designed with cloud companies.</dd>
<dt>The larger rival</dt>
<dd><span class="names">Broadcom</span> makes Ethernet switch chips, optical DSPs and custom AI chips for the largest cloud companies.</dd>
<dt>The short-reach specialists</dt>
<dd><span class="names">Credo</span> makes active electrical cables and DSPs for links inside and between racks. <span class="names">Astera Labs</span> makes retimer chips that clean up signals across circuit boards.</dd>
<dt>The module makers</dt>
<dd><span class="names">Coherent</span>, <span class="names">Lumentum</span> and <span class="names">Innolight</span> make the transceivers and lasers the DSPs sit inside, assembled in volume by <span class="names">Fabrinet</span>.</dd>
<dt>The ecosystem owner</dt>
<dd><span class="names">Nvidia</span> makes GPUs and its own networking, and invested $2 billion in Marvell in March 2026 as part of a partnership around NVLink Fusion, its link for mixing its chips with others in one rack.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone relying on copper beyond a few metres. And Marvell's own case, wherever co-packaged or linear optics move the translation onto a switch chip it does not make, or a large customer takes its custom chip work elsewhere.</dd>
</dl>
</section>

---

<p class="sources">Sources: Marvell fourth quarter and fiscal 2026 results, released 5 March 2026, for full year revenue and data centre share. Marvell annual report on Form 10-K for fiscal 2026, filed 11 March 2026, for customer concentration. Marvell second quarter fiscal 2027 results and earnings call, 27 August 2026, for data centre revenue, the fiscal 2027 and 2028 outlook, capacity prepayments and gross margin commentary. Marvell announcement completing the Inphi acquisition, 20 April 2021. Nvidia and Marvell NVLink Fusion announcement, 31 March 2026. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
