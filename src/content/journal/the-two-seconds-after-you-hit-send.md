---
title: "What actually happens in the two seconds after you hit send"
date: 2026-09-18
summary: "When you ask an AI a question, no answer is waiting on a shelf. A building the size of a factory manufactures every word for you, one at a time, in real time. Understanding that one fact explains why the whole industry is suddenly about electricity, water and copper."
category: "Explainer"
cover: "/covers/two-seconds.svg"
tags: ["explainer", "inference", "the-stack"]
---

Start with a question you have probably never asked: where does the answer come from?

When you search Google, the answer already exists. The internet was read and indexed years ago, and your query is a lookup. The expensive work was done in advance, which is why a search costs a fraction of a cent.

When you ask an AI assistant, nothing exists yet. The model writes the reply from scratch, one word at a time, every single time, even if a million people asked the same thing this morning. There is no shelf. There is a factory.

That is the whole story of the AI buildout in one sentence. Generating text is a manufacturing process, and manufacturing needs a plant, power, cooling and logistics. Multiply one query by hundreds of millions of people a week and you get the reason companies are spending hundreds of billions of dollars on buildings.

## Three words that unlock the rest

**Token.** The thing the factory makes. A token is a chunk of text, roughly three quarters of a word. Your question is chopped into tokens on the way in, and the answer is manufactured token by token on the way out. It is also the unit the labs charge for. A token is the widget coming off the line.

**FLOP.** The unit of labour. One floating-point operation is a single multiply or add. Producing one token takes hundreds of billions of them. Not per answer, per word. A chip's speed in FLOPs per second is how many workers it has on the floor.

**Training versus inference.** Training is building the model: adjusting over a trillion internal settings across months of computation. It happens once per model. Inference is running it: every question anyone asks, billions of times a day. The instinct is that training is where the money goes. It isn't. By 2026 most AI computation is inference. The money is in running the factory, not building it.

## The journey, slowed down

Here is what happens between your thumb and the first word of the reply.

**The trip.** Your question leaves your phone as radio waves, reaches a tower or router, becomes pulses of light in glass fibre travelling at about two thirds the speed of light, and often crosses hundreds of miles to reach a data centre.

**The front door.** A gateway checks who you are, applies limits, runs a safety screen, and staples your question to the system's instructions and your past conversation.

**Tokenisation.** The text is chopped into tokens and turned into numbers. From here on, everything is arithmetic.

**Prefill: the model reads.** It takes in the whole prompt at once, in parallel, in a burst of billions of calculations. This produces something called the KV cache, which is the model's working memory of your conversation. The short pause before the first word appears is prefill happening.

**Decode: the model writes.** One token at a time. Each word requires a full pass through the entire network, hundreds of billions of calculations, and then it does it again for the next word. When you watch an answer type itself out, you are watching an assembly line run.

**The trip home.** Each token streams back down the same fibre. Total elapsed time, about two seconds.

## Why it costs cents and not dollars

There is one trick behind the curtain that makes this affordable, and it is worth knowing because it explains a lot of the hardware.

Your question is not processed alone. It is grouped with hundreds of other people's questions and run through the same chip at the same time, the way a delivery driver batches orders on one route. This is called batching, and it is the difference between a query costing cents and costing dollars.

Two more tricks stack on top. The working memory from your conversation is reused rather than recomputed for every word. And the model's numbers are rounded to lower precision, like a slightly compressed photo, near-identical to the eye at a fraction of the cost. Together these software tricks alone cut the cost of a token by several times. When you see the price of an AI service fall sharply in a year, most of that is this layer, not a new chip.

## The factory in layers

Every AI data centre is the same seven layers, bottom to top:

1. **Power.** Generation, grid connection, transformers, backup. The raw material.
2. **Cooling.** Liquid loops, pumps and chillers. Half the job, as you will see.
3. **Compute.** The chips themselves.
4. **Memory and storage.** Fast memory stacked beside the chip, slower storage behind it.
5. **Networking.** The links that let ten thousand chips act as one machine.
6. **Software.** The layer that makes the hardware usable and affordable.
7. **Models and apps.** The labs, the APIs, the subscription you pay for.

One sentence for the whole thing: electricity flows through silicon and becomes computation and heat; water carries the heat away; light coordinates the computation; words ship out the door.

## Why the story moved from chips to electricity

For fifty years, better software meant hiring cleverer programmers. Intelligence was a research problem. Then, around 2020, researchers found that making a model bigger, feeding it more data and spending more computation made it predictably smarter. Spend ten times more, get a reliably better model.

That turned intelligence into something you can purchase, and large companies know exactly how to compete on purchasing: outspend everyone. Software used to be the escape from the physical world, with no factory and no marginal cost. AI reversed it. The frontier of software is now poured in concrete, measured in megawatts and cooled with water.

Software became heavy industry. And heavy industry is gated by the slowest thing in the chain, which is never the chip. It is the building, the wires and the water. That is what the rest of this journal is about.

---

<p class="sources">This piece is a plain-language explainer, written from my own study notes on the AI infrastructure stack. It describes mechanism, not market figures; where numbers appear they are structural (how a token is made, what a FLOP is) rather than financial. Personal research, not investment advice.</p>
