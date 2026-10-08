---
title: "Nvidia paid Lumentum $2 billion for lasers, because silicon cannot make light"
date: 2026-10-05T14:01:18+08:00
summary: "Lumentum makes the tiny lasers that turn data into light, so AI chips can talk to each other across a data centre. Those lasers have to be grown on a fragile crystal that only a few factories in the world can work at volume, and demand is running well ahead of supply. That is why Nvidia, a chip company, paid to make sure Lumentum builds more of them."
category: "Analysis"
cover: "/covers/lumentum-makes-the-light.svg"
tags: ["networking", "optics", "lasers"]
---

In March, Nvidia, the company that designs most of the world's AI chips, agreed to invest $2 billion in Lumentum. Lumentum does not make chips. It makes lasers.

The deal came with a large purchase commitment and rights to future factory capacity. On the same day Nvidia made a similar investment in Coherent, Lumentum's closest rival. Nvidia was not buying a stake for its own sake. It was buying a place in the queue.

The reason is simple once you see it. Every AI chip has to talk to thousands of others, and past a couple of metres it talks in light.

Something has to make that light, and Lumentum makes it from a crystal that very few factories on earth can work.

The bottleneck Nvidia paid to clear is not a chip. It is the laser at the start of the fibre.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture signalling to a friend across the street at night. Shouting works across a room, but across a street you get hoarse and they still cannot hear you. Click a torch on and off in Morse code instead and the message arrives clearly, for almost no effort.</p>
<p>Now imagine the torch is the size of a grain of sand and has to click billions of times a second. You cannot make its bulb from ordinary glass. It needs a special glass that only a few glassblowers can work, and many of their pieces crack in the kiln.</p>
<p>Every new AI chip wants a faster torch, and there are still only a few glassblowers. Nvidia has paid one of them, Lumentum, to keep a kiln running for it.</p>
</details>

## Three words you need

**Optical transceiver.** The plug at each end of a fibre that converts electricity into light and back again. Lumentum sells the lasers inside these plugs, and also sells finished plugs of its own.

**EML.** Short for electro-absorption modulated laser, Lumentum's flagship product. It makes a beam of light, and switches it on and off billions of times a second to spell out data.

**Indium phosphide.** The crystal these lasers are grown on, usually shortened to InP. When you see it in this piece, read it as the material that can actually glow.

## Why the conversation needs light

Training an AI model splits the work across thousands of chips that must constantly swap partial results. If the network cannot keep up, the most expensive silicon ever built sits waiting.

Copper carried that conversation for decades. At today's speeds a copper signal smears into noise within a couple of metres, and pushing it further costs more and more power.

That power is the real cost. An AI data centre is limited by how much electricity it can get, not by floor space. Light down glass travels further and uses far less energy per bit.

Each chip generation makes this worse, not better. A faster chip needs a faster link, which is why the industry is climbing from 800 gigabits a second per plug to 1.6 terabits. Each step needs more lasers, and better ones: the next plugs need lasers carrying 200 gigabits a second each.

## Why almost nobody can make the laser

The obvious question is why every chip factory does not simply make lasers too. The answer is the material. Silicon, the base of every processor, is excellent at computing and very poor at giving off light.

So the laser has to be grown on indium phosphide instead, and InP is miserable to work with. The wafers, the thin discs that chips are built on, are small and brittle. A painful share of each batch is thrown away.

Getting good yields depends on years of mostly secret process knowledge. It cannot be bought, hired or rushed. Lumentum's EMLs come out of two InP factories in Japan, both of which it is expanding.

New capacity arrives slowly. Lumentum is converting a factory in Greensboro, North Carolina, to InP. Its chief executive, Michael Hurlston, expects first revenue from it only in early 2028.

The layer is also tangled. Lumentum sells lasers to module makers such as Innolight, which then compete with its own finished modules. It is a supplier and a rival to the same customers.

## What Lumentum's own results show

If the laser is the bottleneck, Lumentum should be selling more, earning more on each sale and still failing to keep up. All three appear in its results for the quarter to June 2026.

Revenue roughly doubled on a year earlier. Gross margin, the share of each sale left after the cost of making it, rose from about a third to nearly half.

Lumentum put that gain partly down to fuller factories and higher prices on some products. That is what scarcity looks like in money.

And it still cannot keep up. Hurlston said Lumentum is shipping behind customer demand for EMLs, and expects to be significantly behind at the end of the year even as output rises.

The next generation is already arriving. The faster lasers the next plugs need are a growing share of Lumentum's laser sales, and it expects them to be most of its shipments by the middle of 2027.

## What would prove me wrong

This industry has a history, and it is not kind. Optical parts have run through repeated cycles of shortage, expansion and glut. Lumentum's own revenue fell by almost a quarter in fiscal 2024, when customers stopped ordering to work through stock.

The margin I just described may be the shortage talking. Everyone is now adding capacity, including Lumentum with Nvidia's money. Coherent makes InP on six-inch wafers, which it says cut the cost of each laser.

The second threat is a different design. Silicon photonics builds most of the optics in silicon and feeds it with a simpler, always-on laser. For shorter links, that can route around the EML altogether.

So I am wrong if any of three things happens. Lumentum's gross margin slides towards the low forties as new capacity arrives, which would mean the advantage was scarcity, not skill.

Or Coherent's cheaper six-inch wafers take the orders for the newest 200 gigabit EMLs. Or silicon photonics routes around the EML.

Alongside those, I watch whether the giant cloud companies keep spending. A supplier this far down the chain is hit first when they pause.

<section class="exposure">
<h3>Who is exposed if the laser, not the chip, is the bottleneck</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are Lumentum's own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Lumentum</span> makes EMLs, CW lasers and other InP lasers for data centres, alongside finished transceivers, optical switches, telecom lasers, 3D sensing lasers and industrial lasers.</dd>
<dt>Other laser makers</dt>
<dd><span class="names">Coherent</span> makes InP lasers and finished transceivers. <span class="names">Broadcom</span>, <span class="names">Mitsubishi Electric</span> and <span class="names">Sumitomo Electric</span> make lasers for data centre optics.</dd>
<dt>The module assemblers</dt>
<dd><span class="names">Innolight</span> and <span class="names">Eoptolink</span> build finished transceivers around bought-in lasers. <span class="names">Fabrinet</span> assembles optics under contract.</dd>
<dt>The crystal</dt>
<dd><span class="names">AXT</span> makes the InP substrates that lasers are grown on.</dd>
<dt>The buyer who paid ahead</dt>
<dd><span class="names">Nvidia</span> has invested in Lumentum and Coherent and signed multi-year agreements for laser and optical products.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Copper links wherever a connection runs beyond a couple of metres. Module makers without a secured laser supply while EMLs are short. And Lumentum itself, if new InP capacity or silicon photonics arrives faster than the demand for EMLs.</dd>
</dl>
</section>

---

<p class="sources">Sources: Nvidia and Lumentum announcement of their strategic agreements, 2 March 2026, and Nvidia's announcement of its Coherent agreement the same day. Lumentum fourth quarter and fiscal 2026 results, released 11 August 2026, for revenue and gross margin. Lumentum fourth quarter fiscal 2026 earnings call, 11 August 2026, for EML supply, the next-generation mix, Japanese wafer fabs and the Greensboro conversion. Lumentum fiscal 2024 results, released 14 August 2024. Coherent announcement of six-inch InP wafer fabrication, March 2024. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
