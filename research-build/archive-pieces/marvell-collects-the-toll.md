---
title: "Marvell is paid every time AI chips talk to each other, whoever made the chips"
date: 2026-09-28T13:25:16+08:00
summary: "Marvell makes the small chips that turn electrical signals into light and back, so AI processors in different cabinets can share their work, and whichever company's AI chip wins, a growing cluster needs more of those links. Marvell also helps the big cloud companies design their own AI chips, which is the riskier half of the story."
category: "Analysis"
cover: "/covers/marvell-collects-the-toll.svg"
tags: ["networking", "optics", "data-centres"]
draft: false
---

Most people who follow AI hardware are watching one contest: Nvidia's chips against Google's, Amazon's and everyone else's. Marvell, the American chip designer, sits somewhere that contest barely reaches.

When two AI processors in different cabinets swap results, the signal leaves as electricity, crosses the hall as light and arrives as electricity again.

The chip doing that translation at each end is very often a Marvell part. It is a charge on how big the cluster gets, not a bet on which chip wins.

Marvell is paid every time AI chips talk, whoever made the chips.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Call to someone three streets away and your words smear into noise, however loudly you shout. A torch works instead, but someone has to turn your words into flashes, and someone at the far end has to turn them back.</p>
<p>Those two people do not care who is talking. The more people want to talk, and the faster, the more of them you need.</p>
</details>

## Where copper stops and Marvell starts

AI models are split across thousands of chips that swap partial results all the time. Inside a cabinet, copper wire carries that traffic. Between cabinets it cannot, because at today's speeds an electrical signal fades within a few metres.

So everything leaving the cabinet becomes light, through an optical transceiver, a plug the size of a packet of chewing gum. Inside are a laser, a light detector and an optical DSP, a digital signal processor that translates between electricity and light. The DSP is the hard part.

The light shines at four levels of brightness, and the DSP must tell them apart billions of times a second through noise. Every doubling in speed, from today's 800 gigabit plugs to the 1.6 terabit generation now arriving, makes that harder. Marvell bought this skill when it completed its purchase of Inphi, the leader in these chips, in 2021.

The plug neither knows nor cares whose chip sits behind the switch. Two things raise the number of plugs at once: bigger clusters need more links, and each faster chip generation means replacing them.

## What Marvell's own behaviour shows

Marvell has said it will pay suppliers in advance this financial year to secure parts, including its newest optical DSPs. Paying ahead to hold factory space is what a supplier does when demand outruns the factories.

Its sales have shifted the same way. Data centres went from about three quarters of Marvell's revenue to nearly four fifths of it in two quarters.

Marvell also designs custom AI chips with cloud companies. That half gets the headlines, but every such chip still has to talk to the others, so it still needs the links.

## What would prove me wrong

I am wrong if the translation moves off the plug at scale. Linear pluggable optics drop the DSP and let the switch chip clean the signal, and co-packaged optics put the light conversion on the switch itself.

If either spreads widely, the job moves to whoever makes the switch chip. I am also wrong if Marvell's interconnect growth stalls while clusters keep growing.

<section class="exposure">
<h3>Who is exposed if the link, not the chip, is the toll</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The figures are Marvell's own disclosures, used as evidence for the mechanism.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Marvell</span> makes optical DSPs, switch chips and custom AI chips.</dd>
<dt>The rivals in the link</dt>
<dd><span class="names">Broadcom</span> makes switch chips, DSPs and custom AI chips. <span class="names">Credo</span> and <span class="names">Astera Labs</span> make short-reach cables and retimer chips.</dd>
<dt>The plug, and the chips it connects</dt>
<dd><span class="names">Coherent</span>, <span class="names">Lumentum</span> and <span class="names">Innolight</span> make transceivers and lasers, assembled by <span class="names">Fabrinet</span>. <span class="names">Nvidia</span> makes GPUs and its own networking.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Copper beyond a few metres, and Marvell itself if co-packaged or linear optics move the translation onto a switch chip it does not make.</dd>
</dl>
</section>

---

<p class="sources">Sources: Marvell fiscal 2026 results and annual report, March 2026, and its second quarter fiscal 2027 results and earnings call, 27 August 2026. Personal research, not investment advice.</p>
