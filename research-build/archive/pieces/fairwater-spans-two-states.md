---
title: "Microsoft's Fairwater runs one AI training job across two states. Power chose where."
date: 2026-10-29T17:54:08+08:00
summary: "Microsoft has joined its giant Fairwater AI data centres in Wisconsin and Atlanta with its own fibre, so they can train one AI model together. It built them so far apart because, it says, no single site has enough power and land for the biggest jobs. Light takes time to cross that distance, so only the work that needs the fewest conversations is split between them."
category: "Analysis"
cover: "/covers/fairwater-spans-two-states.svg"
tags: ["networking", "power", "data-centres"]
draft: true
---

Microsoft's Fairwater AI campus in Wisconsin went fully live in June. Its twin near Atlanta began work in October 2025. The two sit about 1,000 kilometres apart.

Microsoft has joined them with fibre of its own, so that both can work on the same training job.

The obvious design would be one enormous building. Asked why it built so far away, Microsoft named land and power.

Fairwater's largest jobs no longer fit one site's power and land. The fibre makes two sites one machine.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Your fuse box can run only so many ovens at once. Baking for a whole town, you borrow a second kitchen across the city. Inside each kitchen the cooks pass bowls hand to hand every few seconds, so they must share one counter.</p>
<p>Between the two kitchens, they phone once per batch to agree changes to the recipe. Any task that needs a call every few seconds stays in one kitchen.</p>
</details>

## Why only some of the work can travel

A pulse of light in a glass strand is quick, but not instant. It covers about 200 kilometres every thousandth of a second, roughly five microseconds for each kilometre. Over Fairwater's 1,000 kilometres, a message needs at least five milliseconds to arrive, and the switches and lasers on the way only add to that.

Training a model means showing it data, measuring its mistakes and adjusting its settings, over and over. Fairwater divides that work between its chips in two main ways.

Tensor parallelism cuts each calculation across several chips, which must swap results many times in every step. Data parallelism gives each group of chips its own copy of the model and different data, and the groups compare notes once a step.

Five milliseconds, repeated many times a step, would leave the chips idle. So the talkative tensor work stays inside one Fairwater building, where Microsoft stacks racks on two storeys to keep cables short. Only the quieter traffic, such as averaging between copies, crosses state lines.

Why not one bigger site? Microsoft says land and power. I read that as the grid queue at work: a bigger campus needs a bigger connection, and [that wait runs to years](/journal/the-queue-not-the-chip/). Some of Microsoft's fibre route was bought years ago and reused.

## What Microsoft says

In November 2025 Microsoft wrote that large training jobs are outpacing the power and space of a single facility. It added that the speed of light is now a key bottleneck in tying its chips together.

Its answer is the AI WAN, a wide area network built only to carry training traffic between distant sites. Separately, Microsoft says it delivered more than 190,000 kilometres of new fibre across America last year.

Google reached the same answer first. Its Gemini Ultra model was trained across several data centres, with the tightly linked work inside each pod and the data parallel work between them.

## What would prove me wrong

I am wrong if, by the end of 2027, Microsoft or another cloud giant builds one campus sized to hold its largest training job alone, a stated multi-gigawatt cluster on a single site, and says that is now how it trains.

I am also wrong if tensor work is shown running between sites, because then distance was never the limit.

<section class="exposure">
<h3>Who is exposed if power, not distance, decides where AI is trained</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The figures are the companies' own, used as evidence for the mechanism.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Microsoft</span> builds and runs the Fairwater AI data centres and the fibre network that links them.</dd>
<dt>Training across sites</dt>
<dd><span class="names">OpenAI</span> trains models on Microsoft's AI computers. <span class="names">Google</span> trains its Gemini models across data centres on its own chips.</dd>
<dt>The long-distance light</dt>
<dd><span class="names">Ciena</span> and <span class="names">Nokia</span> make the optical systems that link distant sites. <span class="names">Corning</span> and <span class="names">Prysmian</span> make the fibre.</dd>
<dt>Inside each building</dt>
<dd><span class="names">Nvidia</span> makes the racks of AI chips. <span class="names">Arista</span> and <span class="names">Cisco</span> make network switches.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Single campuses waiting on one ever larger grid connection, and any training method that cannot be split.</dd>
</dl>
</section>

---

<p class="sources">Sources: Microsoft's Fairwater posts of 18 September and 12 November 2025, its Mount Pleasant announcement of 23 June 2026 and Google's Gemini technical report of December 2023, with the lead from a YouTube video on the AI networking industry. Personal research, not investment advice.</p>
