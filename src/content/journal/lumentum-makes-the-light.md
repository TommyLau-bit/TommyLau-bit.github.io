---
title: "Nvidia paid Lumentum $2 billion for lasers, because silicon cannot make light"
date: 2026-10-05T14:01:18+08:00
summary: "Lumentum makes the tiny lasers that turn data into light, so AI chips can talk to each other across a data centre. Those lasers have to be grown on a fragile crystal that only a few factories in the world can work at volume, and demand is running well ahead of supply. That is why Nvidia, a chip company, paid $2 billion to make sure Lumentum builds more of them."
category: "Analysis"
cover: "/covers/lumentum-makes-the-light.svg"
tags: ["networking", "optics", "lasers"]
---

On 2 March 2026, Nvidia, the company that makes most of the world's AI chips, agreed to invest $2 billion in Lumentum. Lumentum does not make chips. It makes lasers. On the same day Nvidia put another $2 billion into Coherent, Lumentum's closest rival.

The Lumentum deal came with a multibillion-dollar purchase commitment and rights to future factory capacity for advanced laser parts. The money is meant to help Lumentum build a new factory in America. Nvidia was not buying a stake for its own sake. It was buying a place in the queue.

The reason is simple once you see it. Every AI chip Nvidia sells has to talk to thousands of others, and past a couple of metres it talks in light. Something has to make that light, and Lumentum makes it from a crystal that very few factories on earth can work.

The bottleneck Nvidia paid to clear is not a chip. It is the laser at the start of the fibre.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture signalling to a friend across the street at night. Shouting works across a room, but across a street you get hoarse and they still cannot hear you. Click a torch on and off in Morse code instead and the message arrives clearly, for almost no effort.</p>
<p>Now imagine the torch is the size of a grain of sand and has to click billions of times a second. You cannot make its bulb from ordinary glass. It needs a special glass that only a few glassblowers can work, and many of their pieces crack in the kiln.</p>
<p>Every new AI chip wants a faster torch, and there are still only a few glassblowers. Nvidia has paid one of them, Lumentum, to keep a kiln running for it.</p>
</details>

## Three words you need

**Optical transceiver.** The plug at each end of a fibre that converts electricity into light and back again. It snaps into the front of a network switch. Lumentum sells the lasers inside these plugs to the companies that assemble them, and also sells finished plugs of its own.

**EML.** Short for electro-absorption modulated laser, Lumentum's flagship product. It does two jobs at once. It makes a beam of light, and it switches that beam on and off billions of times a second to spell out data in ones and zeros.

**Indium phosphide.** The crystal these lasers are grown on, usually shortened to InP. When you see it in this piece, read it as the material that can actually glow.

## Why the conversation needs light

Training an AI model splits the work across thousands of chips that must constantly swap partial results. As I wrote in an earlier piece, an AI cluster is less a pile of chips than a conversation. If the network cannot keep up, the most expensive silicon ever built sits waiting.

Copper carried that conversation for decades. At today's speeds a copper signal smears into noise within about two metres. Pushing it further means spending more and more power just to be heard at the other end.

That power is the real cost. An AI data centre is limited by how much electricity it can get, not by floor space. Every watt spent moving data is a watt not spent computing. Light down glass travels further, carries more, and uses far less energy per bit over distance.

Each chip generation makes this worse, not better. A faster chip needs a faster link, which is why the industry keeps climbing from 400 gigabits a second per plug to 800, then to 1.6 terabits. Each step needs more lasers, and better ones, at the start of every fibre.

## Why almost nobody can make the laser

The obvious question is why every chip factory does not simply make lasers too. The answer is the material. Silicon, the base of every processor and phone, is excellent at computing and very poor at giving off light. That is built into the structure of the crystal itself.

So the laser has to be grown on indium phosphide instead, and InP is miserable to work with. The wafers, the thin discs that chips are built on, are small and brittle. They crack. A painful share of each batch comes out unusable and is thrown away.

Getting good yields depends on years of accumulated and mostly secret process knowledge. It cannot be bought, hired or rushed. Lumentum's EMLs come out of two InP wafer factories in Japan, both of which it is expanding.

New capacity arrives slowly. Lumentum is converting a factory in Greensboro, North Carolina, from gallium arsenide, a different light-emitting crystal, to InP. Its chief executive, Michael Hurlston, said in August he expects first revenue from it in early 2028, reaching full output by the end of 2028.

The layer is also tangled. Lumentum sells lasers to module makers such as Innolight, which then compete with Lumentum's own finished modules. It is a supplier and a rival to the same customers at once.

## What Lumentum's own numbers show

If the laser is the bottleneck, Lumentum should be selling more, earning more on each sale and still failing to keep up. All three appear in its results for the quarter to 27 June 2026, released on 11 August 2026.

**Growth.** Revenue was $1.01 billion, up from $481 million a year earlier. For the full fiscal year it was $3.01 billion, against $1.65 billion the year before. Hurlston called it another record quarter for EMLs.

**Profit per sale.** Gross margin, the share of each sale left after the cost of making it, was 47.4 per cent, up from 33.3 per cent a year earlier. Operating margin, what remains after running the whole business, went from a small loss to 27.8 per cent. Lumentum attributed the gain partly to fuller factories and higher prices on some products, which is what scarcity looks like in money.

**Supply.** Hurlston said Lumentum is still shipping behind customer demand for EMLs. He expects to be significantly behind demand at the end of the year even as output rises.

**The next generation.** EMLs carrying 200 gigabits per lane, the speed the next plugs need, were already over a quarter of Lumentum's EML revenue. The company expects them to be most of its shipments by the middle of 2027.

## What would prove me wrong

This industry has a history, and it is not kind. Optical components have run through repeated cycles of shortage, expansion and glut. Lumentum's own revenue fell 23 per cent in fiscal 2024, to $1.36 billion, when customers stopped ordering to work through stock.

The margin I just cited may be the shortage talking. Everyone is now adding capacity, including Lumentum with Nvidia's money. Coherent makes InP on six-inch wafers, which it says give about four times the area of three-inch ones and cut the cost of each laser.

The second threat is a different design. Silicon photonics builds most of the optics in silicon and feeds it with a simpler laser that stays on continuously, called a CW laser. For shorter links, that can route around the EML altogether. Lumentum makes CW lasers too, but more companies can make those.

So I watch three things. Whether gross margin holds as the new factories come online, because a slide toward the low forties would mean the advantage was scarcity, not skill. Whether 200 gigabit EMLs keep growing as a share of Lumentum's laser sales, or whether Coherent's cheaper wafers start taking those orders. And whether the hyperscalers, the giant cloud companies, keep spending, because a supplier this far down the chain is hit first when they pause.

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

<p class="sources">Sources: Nvidia and Lumentum announcement of their strategic agreements, 2 March 2026, and Nvidia's announcement of its Coherent agreement the same day. Lumentum fourth quarter and fiscal 2026 results, released 11 August 2026, for revenue, gross and operating margins and segment sales. Lumentum fourth quarter fiscal 2026 earnings call, 11 August 2026, for EML supply, 200 gigabit mix, Japanese wafer fabs and the Greensboro conversion. Lumentum fiscal 2024 results, released 14 August 2024. Coherent announcement of six-inch InP wafer fabrication, March 2024. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
