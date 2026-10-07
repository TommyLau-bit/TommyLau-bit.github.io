---
title: "Nobody makes an Nvidia B200 alone, and the weak links are measured in years"
date: 2026-10-07T16:36:29+08:00
summary: "Nvidia's B200, one of the chips behind today's AI boom, is designed in California but built by dozens of companies in at least five countries. Some of those suppliers could be swapped out in months. Others would take years, because a replacement needs new factories or years of testing before anyone trusts it."
category: "Explainer"
cover: "/covers/nobody-makes-a-b200-alone.svg"
tags: ["the-stack", "supply-chain", "data-centres"]
draft: false
---

Pick up an Nvidia B200 and ask a simple question: who made it? The honest answer is nobody, not alone.

Nvidia designed it, but Nvidia runs no chip factories. TSMC made its two slabs of logic, mostly in Taiwan, using machines only ASML in the Netherlands can build. Nvidia buys its memory from three makers, two of them South Korean. The bare silicon came from a short list of wafer makers, the largest of them Japanese.

The B200 holds 208 billion transistors, according to Nvidia. Placing one every second, without a break, would take about 6,600 years.

So the useful question is not who makes each part.

The B200's real dependency is how long each part would take to replace.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of a wedding cake. One baker designs it, but the flour, the eggs, the icing and the stand all come from different shops, and some are the only shop in town that makes that thing.</p>
<p>If the eggs run out, you buy eggs elsewhere tomorrow. If the one shop that makes the sugar flowers closes, you wait while someone else learns, then test their flowers on a few cakes before trusting them on the day.</p>
<p>A B200 is that cake with hundreds of suppliers. The ones that matter are not the biggest. They are the ones that would take longest to learn.</p>
</details>

## Three words you need

**Die.** A single chip cut from a wafer, the thin silicon disc on which hundreds are made together. A B200 joins two large logic dies so they behave as one processor.

**Package.** The finished component you could hold, with dies, memory and wiring mounted together on a base.

**Qualification.** The months or years of testing a customer runs before trusting a new supplier's part. It is why a cheaper alternative cannot simply be swapped in.

## From blueprint to wafer

Design is Nvidia's own work, and this journal leaves it alone. What matters is tape-out, when the finished design goes to the factory.

The design becomes masks, plates carrying the circuit pattern for one layer of the chip. The most advanced masks are themselves mirrors, made on blank plates from Japanese suppliers such as AGC and Hoya.

The wafers begin as single crystals of ultra-pure silicon, sliced into discs 300 millimetres across. Two Japanese companies, Shin-Etsu and SUMCO, are among the largest makers.

Then comes lithography, printing the pattern onto the wafer with light. The finest layers use extreme ultraviolet light, EUV, at a wavelength of 13.5 nanometres. ASML describes the technology as unique to itself.

The light bounces off mirrors made by ZEISS in Germany. ZEISS says that if one were enlarged to the size of Germany, its largest bump would be 0.1 millimetres high.

TSMC makes the dies on a custom version of its four nanometre process, called 4NP. Nvidia says each die is as large as the factory's printing field allows, which is why there are two.

## Memory, the package and the test

Beside the logic sit eight stacks of HBM, high-bandwidth memory: memory chips piled vertically and wired through their own silicon. Nvidia's annual report names SK Hynix, Micron and Samsung as its memory suppliers.

Each maker's stacks must be qualified for each accelerator, so they are ordered far ahead. In December 2025 Micron said it had agreed price and volume for its entire 2026 supply of HBM.

The dies and memory are joined in TSMC's CoWoS packaging, short for chip on wafer on substrate. For Blackwell, Nvidia's chief executive said in January 2025, that means largely CoWoS-L. The chips sit on an interposer, a slab of extremely fine wiring with small silicon bridges between neighbours.

The interposer is mounted on a package substrate, a laminated circuit board that carries power and signals out to the computer. A small group of makers, such as Ibiden in Japan and Unimicron in Taiwan, builds the substrates for AI processors.

Inside each substrate is insulating film from Ajinomoto, a company better known for seasoning. Ajinomoto says its film has become the choice for nearly all high-performance central processors. In May 2026 it announced it would buy land for a new film plant, with construction from 2028 and operations from 2032.

Finally the package is tested across temperature, voltage and speed, on machines from companies such as Advantest and Teradyne.

## Into the rack

In Nvidia's GB200 NVL72 rack, 72 Blackwell processors sit beside 36 Grace processors, Nvidia's own central processors built on Arm designs. Nvidia's switch chips join all 72 so they act as one machine.

Between racks, signals pass through switches, usually Nvidia's own in its clusters, with Broadcom's chips the alternative, and travel as light down Corning's glass. Transceivers, which turn electricity into light and back, use lasers from Coherent and Lumentum and often Marvell's signal chips.

Power reaches the building as hundreds of volts of alternating current and the processor at less than one volt, through conversion chips from companies such as Texas Instruments, Infineon and Monolithic Power Systems. Liquid carries the heat away through cold plates, metal blocks with liquid channels clamped on each chip, and pumps from companies such as Vertiv. Foxconn, Quanta and Wistron assemble the whole thing.

## The clock on each part

My own rough sort, by how long each supplier would take to replace, gives four groups.

**Swappable fastest.** Rack assembly, connectors and much of the power hardware. Several firms can do the work, so moving it probably takes months rather than years.

**A handful, each slow to qualify.** HBM, substrates, test equipment and photoresist, the light-sensitive coating that lithography prints into. Rivals exist, but each new part must be proven on each new chip, which takes quarters or years.

**Short of capacity.** TSMC's fabs, its chip factories, and its packaging lines. For the B200 they are in practice also the only source of the 4NP dies and CoWoS-L. On its July 2026 call, TSMC said packaging capacity was so tight it was limiting customers' growth. Its chief has said a new fab takes two to three years to build and one to two more to fill.

**No second source at all.** EUV machines and their mirrors. I put Ajinomoto's film close by, though rival films exist and its own claim covers central processors. Replacing either is not a purchasing decision, and Ajinomoto's own new plant opens only in 2032.

Nvidia's annual report shows the cost. It says lead times have run beyond twelve months, and that it has paid premiums and deposits and signed long-term capacity commitments. That is a chip designer paying for time in other people's factories.

## Where I stop

A sole supplier with spare capacity is a manageable risk. One whose replacement would take a decade is a different kind of risk.

I make no prediction about the slowest links. ASML's machines, Ajinomoto's film and HBM will each get their own piece. This one is the map.

<section class="exposure">
<h3>Who operates at each stage of a B200</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Nvidia's and Micron's disclosures are used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Nvidia</span> designs the B200, the Grace processor and the switch chips that join them, using processor designs licensed from <span class="names">Arm</span>.</dd>
<dt>The factory and its machines</dt>
<dd><span class="names">TSMC</span> makes and packages the dies. <span class="names">ASML</span> builds the EUV machines, with mirrors from <span class="names">ZEISS</span> and lasers from <span class="names">Trumpf</span>. <span class="names">Applied Materials, Lam Research, Tokyo Electron</span> and <span class="names">KLA</span> make deposition, etching and inspection tools.</dd>
<dt>The materials</dt>
<dd><span class="names">Shin-Etsu</span> and <span class="names">SUMCO</span> make wafers, <span class="names">JSR</span> and <span class="names">Tokyo Ohka Kogyo</span> photoresist, <span class="names">AGC</span> and <span class="names">Hoya</span> mask blanks, and <span class="names">Ajinomoto</span> substrate film.</dd>
<dt>Memory, substrate and test</dt>
<dd><span class="names">SK Hynix, Micron</span> and <span class="names">Samsung</span> make the stacked memory, <span class="names">Ibiden</span> and <span class="names">Unimicron</span> substrates, and <span class="names">Advantest</span> and <span class="names">Teradyne</span> test equipment.</dd>
<dt>The rack around it</dt>
<dd><span class="names">Broadcom</span> and <span class="names">Marvell</span> make network chips, <span class="names">Coherent</span> and <span class="names">Lumentum</span> optics, <span class="names">Corning</span> fibre, <span class="names">Texas Instruments, Infineon</span> and <span class="names">Monolithic Power</span> power chips, and <span class="names">Vertiv</span> cooling. <span class="names">Foxconn, Quanta</span> and <span class="names">Wistron</span> assemble.</dd>
</dl>
<dl class="against">
<dt>Where I stop</dt>
<dd>This maps one product's whole supply chain, so it has no loser. I hold no view on any of these companies as investments.</dd>
</dl>
</section>

---

<p class="sources">Sources: Nvidia's Blackwell architecture page and GTC release of 18 March 2024 for transistors, dies and process, and its GTC 2024 presentation, as reported, for the memory stacks. Nvidia GB200 NVL72 page. Nvidia Form 10-K, filed 25 February 2026, for suppliers, lead times and capacity commitments. Jensen Huang on CoWoS-L, 16 January 2025, as reported by Reuters. Nvidia on the first Blackwell wafer at TSMC Arizona, 17 October 2025. TechInsights teardown, 15 April 2025, for the eight memory packages. TSMC earnings calls of January and July 2026. ASML and ZEISS EUV pages. Ajinomoto's film page and its release of 7 May 2026. Micron earnings call, 17 December 2025. The 6,600 years is my own arithmetic. Personal research, not investment advice.</p>
