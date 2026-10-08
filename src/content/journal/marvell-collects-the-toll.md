---
title: "Marvell is paid every time AI chips talk to each other, whoever made the chips"
date: 2026-09-28T13:25:16+08:00
summary: "Marvell makes the small chips that turn electrical signals into light and back again, so AI processors in different cabinets can share their work. Whichever company's AI chip wins, the cluster still needs those links, and it needs more of them as it grows. Marvell also helps the big cloud companies design their own AI chips, which is the riskier half of the story."
category: "Analysis"
cover: "/covers/marvell-collects-the-toll.svg"
tags: ["networking", "optics", "data-centres"]
draft: false
---

Most people who follow AI hardware are watching one contest. Nvidia's chips against Google's, Amazon's and everyone else's. Marvell, the American chip designer, sits somewhere that contest barely reaches.

Marvell makes parts that let AI chips talk. When two processors in different cabinets swap results, the signal leaves as electricity, crosses the hall as light and arrives as electricity again.

The chip doing that translation at each end is very often a Marvell part. Marvell also helps cloud companies design their own AI chips, and that half gets the headlines.

The first half interests me more. It is a charge on how big the cluster gets, not a bet on which chip wins.

Marvell is paid every time AI chips talk, whoever made the chips.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Call to someone at the end of your garden and they hear you fine. Call to someone three streets away and your words smear into noise, however loudly you shout.</p>
<p>Shouting harder does not fix it. What works is a torch: flashes of light carry across distances a voice never will. But someone has to turn your words into flashes, and someone at the far end has to turn the flashes back into words, quickly and without a single mistake.</p>
<p>Those two people do not care who is talking. Every conversation needs them, and the more people want to talk, and the faster, the more of them you need. That is the job Marvell does inside an AI data centre.</p>
</details>

## Three words you need

**Optical DSP.** A DSP, a digital signal processor, is a chip that cleans up and reshapes a signal. The optical kind sits inside the plug at each end of a fibre cable and translates between electricity and light.

**800G and 1.6T.** How much data one of those plugs moves each second. The 800 gigabit plug is today's workhorse, and the 1.6 terabit plug is the generation now arriving.

**XPU.** An industry label for a custom AI chip, designed for one company's own work rather than sold to everyone. A GPU is a general tool. An XPU does one job, more cheaply.

## Where copper stops and Marvell starts

AI models are too large for one chip, so they are split across thousands that swap partial results all the time. A network even slightly slow leaves the most expensive silicon ever built waiting.

Inside a cabinet, copper wire carries most of that traffic. Between cabinets it cannot, because at today's speeds an electrical signal fades within a few metres. So everything leaving the cabinet becomes light and travels down glass fibre.

That change happens in a plug about the size of a packet of chewing gum, called an optical transceiver, which slots into the front of a network switch. Inside are a laser, a light detector and the optical DSP. The DSP is the hard part.

At these speeds the signal is not a simple on and off. The light shines at four levels of brightness, and the DSP must tell them apart billions of times a second through noise. Every doubling in speed makes that harder.

Marvell bought this skill. In 2021 it completed its purchase of Inphi, the leader in these chips, and the DSP inside many of today's plugs traces back to that deal.

## Why it works as a toll

The plug neither knows nor cares whether the chip behind the switch came from Nvidia, AMD, Google or Amazon. It only carries the conversation.

Two things raise the number of plugs. A bigger cluster needs more links between cabinets. And each faster generation of chips means replacing the links with faster ones. Both happen at once in an AI build.

Marvell's own behaviour suggests the demand is real. It has said it will pay suppliers in advance this financial year to secure parts, including its newest optical DSPs. Paying ahead to hold factory space is what a supplier does when demand outruns the factories.

Its sales have shifted the same way. Data centres went from about three quarters of Marvell's revenue to nearly four fifths of it in just two quarters.

## The second job, and where I stop

Marvell's other data centre business is custom chips. A cloud company knows what it wants its own AI chip to do. Marvell turns that into a working design and manages its manufacture with TSMC, the Taiwanese chip factory.

Broadcom does the same job and is larger at it. The customers are few and enormous, and each runs its own chip team. Marvell's ten largest customers bring in more than four fifths of its revenue.

That makes custom chips a very different business from the optics, with lumpier orders and stronger buyers. Marvell has said the custom work weighs on its gross margin, the share of each sale left after the cost of making it.

This is where I stop. Judging chip design programmes needs knowledge I do not claim. What I can say is physical: every custom chip Marvell helps build still has to talk to the others, so it still needs the links.

## What would prove me wrong

I am wrong if the translation moves off the plug at scale. Two approaches aim to do exactly that, and both save power, which matters when every watt spent moving data is not spent computing.

Linear pluggable optics drop the DSP from the plug and let the switch chip clean the signal. Co-packaged optics go further and put the light conversion on the switch itself. If either spreads widely, the job moves to whoever makes the switch chip.

I am also wrong if Marvell's interconnect growth stalls while clusters keep growing. That would mean someone else is collecting the toll.

So I watch whether the 1.6T links keep a DSP on board. I watch how much of Marvell's growth comes from optics rather than custom chips. And I watch whether its ten largest customers keep rising as a share of revenue.

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
<dd><span class="names">Nvidia</span> makes GPUs and its own networking, and partners with Marvell on NVLink Fusion, its link for mixing its chips with others in one rack.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone relying on copper beyond a few metres. And Marvell's own case, wherever co-packaged or linear optics move the translation onto a switch chip it does not make, or a large customer takes its custom chip work elsewhere.</dd>
</dl>
</section>

---

<p class="sources">Sources: Marvell fourth quarter and fiscal 2026 results, 5 March 2026, for data centre share. Marvell annual report on Form 10-K for fiscal 2026, filed 11 March 2026, for customer concentration. Marvell second quarter fiscal 2027 results and earnings call, 27 August 2026, for data centre share, capacity prepayments and gross margin commentary. Marvell announcement completing the Inphi acquisition, 20 April 2021. Nvidia and Marvell NVLink Fusion announcement, 31 March 2026. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
