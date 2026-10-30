---
title: "Nvidia paid Lumentum $2 billion for lasers, because silicon cannot make light"
date: 2026-10-05T14:01:18+08:00
summary: "Lumentum makes the tiny lasers that turn data into light, so AI chips can talk across a data centre. They are grown on a fragile crystal that only a few factories can work at volume, and demand is running well ahead of supply, which is why Nvidia, a chip company, paid Lumentum to build more of them."
category: "Analysis"
cover: "/covers/lumentum-makes-the-light.svg"
tags: ["networking", "optics", "lasers"]
---

In March, Nvidia, the company that designs most of the world's AI chips, agreed to invest $2 billion in Lumentum. Lumentum does not make chips. It makes lasers.

The deal came with a large purchase commitment and rights to future factory capacity. Nvidia was buying a place in the queue.

Every AI chip has to talk to thousands of others, and past a couple of metres it talks in light. Lumentum makes that light from a crystal very few factories on earth can work.

The bottleneck Nvidia paid to clear is not a chip. It is the laser at the start of the fibre.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Shouting across a street at night leaves you hoarse, but clicking a torch in Morse code carries the message easily. Now imagine the torch is the size of a grain of sand and clicks billions of times a second.</p>
<p>Its bulb needs a special glass that only a few glassblowers can work, and many pieces crack in the kiln. Nvidia has paid one of them, Lumentum, to keep a kiln running for it.</p>
</details>

## Why almost nobody can make the laser

Training an AI model splits the work across thousands of chips that constantly swap results. At today's speeds a copper signal smears into noise within a couple of metres, so the links become light down glass fibre.

The light starts in an optical transceiver, the plug at each end of a fibre that turns electricity into light and back. Lumentum's flagship is the EML, an electro-absorption modulated laser, which switches its beam on and off billions of times a second. Each chip generation needs faster plugs, from 800 gigabits a second to 1.6 terabits, and every step needs more and better lasers.

Silicon, the base of every processor, is very poor at giving off light. So the laser is grown on indium phosphide, InP, a crystal whose wafers are small and brittle, with a painful share of each batch thrown away. Good yields depend on years of mostly secret process knowledge that cannot be bought or rushed.

New capacity arrives slowly. Lumentum is converting a factory in Greensboro, North Carolina, to InP, and expects first revenue from it only in early 2028.

## What Lumentum's own results show

If the laser is the bottleneck, Lumentum should be earning more on each sale and still failing to keep up. Both appear in its results for the quarter to June 2026.

Gross margin, the share of each sale left after the cost of making it, rose from about a third to nearly half. Lumentum put that partly down to fuller factories and higher prices, which is what scarcity looks like in money.

And it still cannot keep up. Its chief executive said Lumentum is shipping behind customer demand for EMLs, and expects to be significantly behind at year end.

## What would prove me wrong

Optical parts have run through repeated cycles of shortage, expansion and glut, and that margin may be the shortage talking.

So I am wrong if Lumentum's gross margin slides towards the low forties as new capacity arrives. I am also wrong if Coherent's cheaper six-inch InP wafers take the orders for the newest 200 gigabit EMLs, or if silicon photonics, optics built in silicon with a simpler laser, routes around the EML.

<section class="exposure">
<h3>Who is exposed if the laser, not the chip, is the bottleneck</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The figures are Lumentum's own disclosures, used as evidence for the mechanism.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Lumentum</span> makes EMLs and other InP lasers, plus finished transceivers.</dd>
<dt>Other laser makers</dt>
<dd><span class="names">Coherent</span>, <span class="names">Broadcom</span>, <span class="names">Mitsubishi Electric</span> and <span class="names">Sumitomo Electric</span> make lasers for data centre optics.</dd>
<dt>The modules and the crystal</dt>
<dd><span class="names">Innolight</span>, <span class="names">Eoptolink</span> and <span class="names">Fabrinet</span> build finished transceivers. <span class="names">AXT</span> makes InP substrates.</dd>
<dt>The buyer who paid ahead</dt>
<dd><span class="names">Nvidia</span> designs the AI chips these lasers connect.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Copper beyond a couple of metres, module makers without secured lasers, and Lumentum itself if new InP capacity or silicon photonics outruns demand.</dd>
</dl>
</section>

---

<p class="sources">Sources: Nvidia and Lumentum announcement, 2 March 2026, and Lumentum fourth quarter fiscal 2026 results and earnings call, 11 August 2026. Personal research, not investment advice.</p>
