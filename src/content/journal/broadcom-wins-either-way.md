---
title: "Broadcom is paid whether the cloud giants stay with Nvidia or leave"
date: 2026-10-02T12:05:07+08:00
summary: "Broadcom makes the switch chips that let thousands of AI processors work as one machine, whoever made the processors. It also designs the custom AI chips that Google, Meta, OpenAI and others are building to rely less on Nvidia. So whichever way the biggest buyers turn, the work runs through Broadcom, and the risk sits with a handful of very powerful customers."
category: "Analysis"
cover: "/covers/broadcom-wins-either-way.svg"
tags: ["networking", "custom-chips", "the-stack"]
---

Most of the conversation about AI hardware is about one question. Will the cloud giants keep buying Nvidia's chips, or will they build their own and leave? It is treated as a contest with two sides.

On 24 June 2026, OpenAI showed its first custom AI chip, called Jalapeño. It was built to run OpenAI's models faster and more cheaply than the general chips it buys today. The company it chose to build it with was Broadcom.

That same Broadcom makes the switch chips at the heart of most large AI networks, including networks full of Nvidia processors. If the giants stay, their chips talk across Broadcom's switches. If they leave, Broadcom very often designs the chip they leave with.

Broadcom is paid whether the cloud giants stay with Nvidia or leave.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Buy a shirt off the rail and it fits most people reasonably well. Have one made and it fits you exactly, with no spare cloth anywhere. For one shirt, the rail wins. If you need ten thousand shirts for exactly the same body, having them made starts to pay.</p>
<p>The catch is that very few people can cut cloth at that standard, so the largest buyers end up queuing at the same few tailors.</p>
<p>Now imagine one of those tailors also makes the zip sewn into almost every shirt on the rail. Whether you buy ready-made or bespoke, part of what you pay reaches the same workshop. That workshop is Broadcom.</p>
</details>

## Three words you need

**Switch chip.** The processor inside a network switch, the box that takes data arriving from many chips and sends each piece to the right destination. Broadcom sells its switch chips to anyone who builds switches, which the industry calls merchant silicon.

**Ethernet.** The open standard for how machines talk over a network, used in offices for decades and now adapted for AI. Because no single company owns it, any maker's chip can join an Ethernet network.

**XPU.** An industry label for a custom AI chip, designed for one company's own workload rather than sold to everyone. Google's TPU, its tensor processing unit, is the best known. Jalapeño is the newest.

## The road: why the switch sets the size of the machine

An AI model is too large for one chip, so it is split across thousands that swap partial results constantly. As I wrote in an earlier piece, a slow network leaves the most expensive silicon ever built waiting. The switch decides how many chips can join without that wait.

Broadcom's current flagship, Tomahawk 6, began shipping in June 2025. It moves 102.4 terabits a second through a single chip, double any Ethernet switch before it. That is enough for 512 connections, each running at 200 gigabits a second.

The number of connections is what matters physically. Chips plug into a first layer of switches, and those switches plug into a second layer above. Each extra layer, called a tier, adds more switches, more optical plugs, more power and more delay on every message.

According to Broadcom, two tiers of Tomahawk 6 can connect about 128,000 AI chips. With switches half as large, the same cluster needs a third tier. Fewer tiers means fewer boxes, fewer plugs and fewer watts spent moving data rather than computing.

And the switch does not care whose chip is plugged into it. Nvidia processors, Google TPUs and OpenAI's new chip all speak Ethernet across the hall. That is the first half of the toll.

## The exit: why the giants want their own chips

A GPU, the graphics processor Nvidia sells, is built to run almost any AI workload well. That flexibility costs something. Part of the chip is there for jobs a particular company may never run, and it still occupies silicon and draws power.

That matters because, as earlier pieces on this site argue, power is the scarcest input in an AI data centre. A chip shaped around one company's own models can spend more of each watt on useful work. At the scale of a cloud giant, that difference compounds across hundreds of thousands of chips.

Few companies can turn that idea into working silicon. OpenAI said Jalapeño went from first design to tape-out, the moment a finished design is sent for manufacture, in nine months. It is built for inference, the work of answering questions rather than training models, and is due to be deployed with partners including Microsoft.

On its September earnings call, Broadcom said it now has six custom chip customers, naming Google, Meta, Anthropic and OpenAI. This is where I stop. Judging how good one chip design is against another needs semiconductor knowledge I do not claim. What I can say is physical: every one of those chips still has to talk to the others.

## What Broadcom's own numbers show

If both halves are real, Broadcom's AI revenue should be growing far faster than the company, and custom chips and networking should both be inside it.

**Growth.** In its third quarter of fiscal 2026, which ended on 2 August and was reported on 2 September 2026, AI semiconductor revenue was $16.7 billion. That was up 221 per cent on a year earlier and 54 per cent on the previous quarter.

**Mix.** On the call, Broadcom said custom accelerators were about 73 per cent of AI revenue in the quarter, leaving the rest largely to networking. Management said it expects AI networking to grow as fast as the custom chips over the next few years.

**Margin.** Gross margin, the share of each sale left after the cost of making it, fell as AI made up more of the mix. Custom chips carry expensive stacked memory bought from other companies, so they earn less on each dollar than switch chips do.

**Outlook.** Broadcom guided to $21.7 billion of AI revenue for the fourth quarter. It also said it has secured supply to reach about $115 billion of AI revenue in fiscal 2027. Those are Broadcom's forecasts, not mine.

It is worth keeping the rest in proportion. Infrastructure software, mostly VMware, the data centre software it bought in 2023, brought in $8.75 billion in the quarter, about 30 per cent of revenue. It is real and steady, but it is software, and it sits outside the layer this site covers.

## What would prove me wrong

The biggest risk is that the customers are few and strong. Six companies is a short list, and every one of them has its own chip team. Each is capable of taking work in-house or splitting it between designers.

That is already happening. Google has given one version of its next TPU to MediaTek, a rival chip designer. Broadcom says it is shipping its own version first. If the largest customer keeps moving work elsewhere, the exit half of my argument weakens.

The road half has a challenger too. Nvidia sells its own Ethernet switches, and the fast links inside each rack, called scale-up, are a separate fight that Broadcom has only just entered. If Nvidia's networking wins inside its own clusters, Broadcom collects only when a customer leaves.

So I watch four things. Whether networking holds its share of Broadcom's AI revenue. Whether the custom chip customer count keeps rising beyond six. What happens to the Google work between Broadcom and MediaTek. And whether gross margin keeps falling as custom chips grow, because a toll should not get thinner the more it is collected.

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

<p class="sources">Sources: Broadcom third quarter fiscal 2026 results, released 2 September 2026, for AI semiconductor revenue, segment revenue and fourth quarter guidance. Broadcom third quarter fiscal 2026 earnings call, 2 September 2026, for the custom chip and networking split, customer count, gross margin commentary, the fiscal 2027 outlook and the Google TPU work. Broadcom announcement of Tomahawk 6 shipping, 3 June 2025. OpenAI and Broadcom announcement of the Jalapeño chip, 24 June 2026. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
