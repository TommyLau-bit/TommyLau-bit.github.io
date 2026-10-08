---
title: "Broadcom is paid whether the cloud giants stay with Nvidia or leave"
date: 2026-10-02T12:05:07+08:00
summary: "Broadcom makes the switch chips that let thousands of AI processors work as one machine, whoever made the processors. It also designs the custom AI chips that Google, Meta, OpenAI and others are building to rely less on Nvidia. So whichever way the biggest buyers turn, the work runs through Broadcom, and the risk sits with a handful of very powerful customers."
category: "Analysis"
cover: "/covers/broadcom-wins-either-way.svg"
tags: ["networking", "custom-chips", "the-stack"]
draft: false
updated: 2026-10-08T16:00:00+08:00
updateNote: "Shortened and made plainer on 8 October 2026. The claim and the test of it are unchanged."
---

Most talk about AI hardware comes down to one question. Will the cloud giants keep buying Nvidia's chips, or build their own and leave?

It is treated as a contest with two sides. Broadcom, the American chip designer, sits on both of them at once.

In June 2026 OpenAI showed its first custom AI chip, called Jalapeño, built to run its own models faster and more cheaply. The company it chose to build it with was Broadcom.

That same Broadcom makes the switch chips at the heart of most large AI networks, including networks full of Nvidia processors. If the giants stay, their chips talk across Broadcom's switches. If they leave, Broadcom often designs the chip they leave with.

Broadcom is paid whether the cloud giants stay with Nvidia or leave.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Buy a shirt off the rail and it fits most people reasonably well. Have one made and it fits you exactly, with no spare cloth anywhere. For one shirt, the rail wins. If you need ten thousand shirts for exactly the same body, having them made starts to pay.</p>
<p>The catch is that very few people can cut cloth at that standard, so the largest buyers end up queuing at the same few tailors.</p>
<p>Now imagine one of those tailors also makes the zip sewn into almost every shirt on the rail. Whether you buy ready-made or bespoke, part of what you pay reaches the same workshop. That workshop is Broadcom.</p>
</details>

## Three words you need

**Switch chip.** The processor inside a network switch, the box that takes data from many chips and sends each piece to the right place. Broadcom sells these chips to anyone who builds switches.

**Ethernet.** The open standard for how machines talk over a network, used in offices for decades and now adapted for AI. Because nobody owns it, any maker's chip can join.

**XPU.** An industry label for a custom AI chip, designed for one company's own work rather than sold to everyone. Google's TPU, its tensor processing unit, is the best known.

## The road: why the switch sets the size of the machine

An AI model is too large for one chip, so it is split across thousands that swap partial results all the time. A slow network leaves the most expensive silicon ever built sitting idle, waiting for the next answer.

Broadcom's current flagship switch chip, Tomahawk 6, began shipping in 2025. It moves 102.4 terabits a second through a single piece of silicon, double any Ethernet switch chip before it.

That matters physically. Chips plug into a first layer of switches, and those switches plug into a second layer above. Each extra layer, called a tier, adds more boxes, more optical plugs, more power and more delay.

According to Broadcom, two tiers of its new switches can connect about 128,000 AI chips. With switches half as large, the same cluster would need a third tier. Fewer tiers means fewer watts spent moving data rather than computing.

And the switch does not care whose chip is plugged into it. Nvidia processors, Google's chips and OpenAI's new one all speak Ethernet across the hall. That is the first half of the toll.

## The exit: why the giants want their own chips

A GPU, the graphics processor Nvidia sells, is built to run almost any AI job well. That flexibility has a cost. Part of the chip serves work a particular company may never run, and it still draws power.

Power is the scarcest input in an AI data centre, as earlier pieces on this site argue. A chip shaped around one company's own models spends more of each watt on useful work, across hundreds of thousands of chips.

Few companies can turn that idea into working silicon. OpenAI said Jalapeño went from first design to tape-out, the moment a finished design is sent to the factory, in nine months.

Broadcom says it now has six custom chip customers, naming Google, Meta, Anthropic and OpenAI. This is where I stop. Judging one chip design against another needs knowledge I do not claim. What I can say is physical: every one of those chips still has to talk to the others.

## What Broadcom's own results show

If both halves are real, Broadcom's AI business should be growing far faster than the rest of the company, with custom chips and networking both inside it.

It is. In the quarter to early August 2026, Broadcom's AI chip revenue more than tripled on a year earlier, to $16.7 billion. Custom chips made up about three quarters of it, and networking most of the rest.

The shift has a cost. Custom chips carry expensive stacked memory bought from other companies. So gross margin, the share of each sale left after the cost of making it, has slipped as they grow.

Broadcom also sells a large software business, mostly VMware, bought in 2023. It is steady, but it is software, and it sits outside the layer this site covers.

## What would prove me wrong

The biggest risk is that the customers are few and strong. Six companies is a short list, and every one of them has its own chip team that could take work in-house.

So I am wrong if custom chip customers move their work to other designers. That has already begun. Google has given one version of its next TPU to MediaTek, a rival chip designer, although Broadcom says it is shipping its own version first.

I am also wrong if Nvidia's own networking wins inside its clusters. Nvidia sells its own switches, and the fast links inside each rack are a separate fight Broadcom has only just entered. Then Broadcom collects only when a customer leaves.

So I watch whether networking holds its share of Broadcom's AI sales, and whether the customer list grows. I watch the Google work with MediaTek. And I watch margin, because a toll should not get thinner the more it is collected.

<section class="exposure">
<h3>Who is exposed if Broadcom is paid either way</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are Broadcom's own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Broadcom</span> makes Ethernet switch chips, optical components and custom AI chips designed with cloud and AI companies, alongside infrastructure software.</dd>
<dt>The custom chip customers</dt>
<dd><span class="names">Google</span>, <span class="names">Meta</span>, <span class="names">Anthropic</span> and <span class="names">OpenAI</span> design their own AI chips with Broadcom for their own data centres.</dd>
<dt>The rival designers</dt>
<dd><span class="names">Marvell</span> designs custom AI chips and makes optical DSPs and switch chips. <span class="names">MediaTek</span> designs one version of Google's next TPU.</dd>
<dt>The switch builders</dt>
<dd><span class="names">Arista</span> and <span class="names">Cisco</span> make the network switches many Broadcom chips sit inside.</dd>
<dt>The chip foundry</dt>
<dd><span class="names">TSMC</span> manufactures both the custom chips and the switch chips.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Single-vendor networking, wherever open Ethernet replaces it between racks. And Broadcom itself, wherever a large customer brings chip design in-house or splits it with another designer.</dd>
</dl>
</section>

---

<p class="sources">Sources: Broadcom third quarter fiscal 2026 results and earnings call, 2 September 2026, for AI semiconductor revenue, the custom chip and networking split, customer count, gross margin commentary and the Google TPU work. Broadcom announcement of Tomahawk 6 shipping, 3 June 2025. OpenAI and Broadcom announcement of the Jalapeño chip, 24 June 2026. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
