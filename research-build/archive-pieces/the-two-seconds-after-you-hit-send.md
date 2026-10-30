---
title: "What actually happens in the two seconds after you hit send"
date: 2026-07-14
summary: "When you ask an AI a question, no answer is waiting on a shelf. A building the size of a factory manufactures every word for you, one at a time, in real time. Understanding that one fact explains why the whole industry is suddenly about electricity, water and copper."
category: "Explainer"
cover: "/covers/two-seconds.svg"
tags: ["explainer", "inference", "the-stack"]
---


Start with a question you have probably never asked: where does the answer come from?

When you search Google, the answer already exists. The internet was indexed years ago, and your query is a lookup.

When you ask an AI assistant, nothing exists yet. The model writes the reply from scratch, one word at a time, even if a million people asked the same thing this morning.

There is no shelf. There is a factory.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a restaurant rather than a library. A library already has the book on the shelf. A restaurant has no finished meal waiting, and every order is cooked from scratch.</p>
<p>The trick that keeps your meal cheap is that the chef cooks one big pan and plates fifty servings. Your AI question is cooked the same way, alongside hundreds of strangers' questions on the same chip.</p>
</details>

## How the factory makes a word

The thing the factory makes is a **token**, a chunk of text about three quarters of a word. Your question is chopped into tokens on the way in, and the answer is made token by token on the way out.

The unit of labour is a **FLOP**, a floating-point operation, meaning a single multiply or add. Producing one token takes hundreds of billions of them. Not per answer, per word.

**Training** is building the model, once, over months of computation. **Inference** is running it, every time anyone asks anything. By 2026 most AI computation is inference. The money is in running the factory, not building it.

What keeps it affordable is **batching**: your question runs through the chip together with hundreds of others at the same moment. That is the difference between a query costing cents and costing dollars.

## The journey, slowed down

Your question leaves your phone as radio waves, then travels as light in glass fibre, often hundreds of miles to a data centre.

There the model reads your whole prompt at once, a step called prefill. That is the short pause before the first word. Then it writes, one token at a time, each needing a full pass through the network. When an answer types itself out, you are watching an assembly line run. Total time, about two seconds.

Underneath sit seven layers: power, cooling, chips, memory, networking, software, and the models and apps on top. Cooling alone is [half the job](/journal/cooling-is-half-the-job/). Electricity flows through silicon and becomes computation and heat, water carries the heat away, and light coordinates it all.

## Why the story moved from chips to electricity

Around 2020, researchers found that a bigger model, fed more data and more computation, got predictably smarter. That turned intelligence into something you can buy, and large companies know how to outspend everyone.

Software used to be the escape from the physical world. AI reversed it. The frontier of software is now poured in concrete, measured in megawatts and cooled with water.

Heavy industry is gated by the slowest thing in the chain, which is never the chip. It is the building, the wires and the water.

<section class="exposure">
<h3>Who sits in each layer</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>Power and cooling</dt>
<dd>Grid, backup and liquid cooling gear: <span class="names">Hitachi Energy, Siemens Energy, GE Vernova, Schneider Electric, Eaton, ABB, Caterpillar, Cummins</span>, and <span class="names">Vertiv, Schneider Electric, Eaton, nVent, CoolIT, Munters</span>.</dd>
<dt>Chips and memory</dt>
<dd><span class="names">Nvidia, AMD, Broadcom</span> design chips, <span class="names">TSMC</span> makes them, <span class="names">Foxconn, Quanta, Wiwynn, Supermicro, Dell</span> assemble servers. Memory and drives: <span class="names">SK Hynix, Samsung, Micron, Seagate, Western Digital, Kioxia</span>.</dd>
<dt>Networking</dt>
<dd><span class="names">Broadcom, Nvidia, Arista, Marvell, Astera Labs, Coherent, Lumentum, Fabrinet, Corning, Amphenol</span> make the links.</dd>
<dt>Buildings, models and apps</dt>
<dd>Campuses: <span class="names">Equinix, Digital Realty, AirTrunk, Princeton Digital Group, STT GDC, Keppel Data Centres, Vantage</span>. Labs: <span class="names">OpenAI, Anthropic, Google, Meta, Microsoft, Amazon</span>.</dd>
</dl>
</section>

---

<p class="sources">This piece is a plain-language explainer, written from my own study notes on the AI infrastructure stack, and its numbers are structural rather than financial. Personal research, not investment advice.</p>
