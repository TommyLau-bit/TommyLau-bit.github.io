---
title: "Corning makes the glass AI chips talk through. Nvidia, Meta and Amazon have all paid to secure it."
date: 2026-10-01T12:01:55+08:00
summary: "Corning, the 175-year-old glass company, makes the optical fibre that carries data between AI chips once copper wire runs out of reach. Every chip generation needs faster plugs at each end of that fibre, but the glass itself stays in the walls and keeps working. That is why three of the biggest AI buyers have signed multi-year deals to make sure Corning builds more of it."
category: "Analysis"
cover: "/covers/corning-lays-the-glass.svg"
tags: ["networking", "optics", "data-centres"]
---

In January, Meta agreed to pay Corning up to $6 billion for fibre optic cable through 2030. In May, Nvidia paid $500 million as part of a partnership for Corning to build more of it in America. In June, Amazon signed a multi-year, multibillion-dollar supply deal of its own.

Corning does not make a single chip. It makes no lasers, no switches and no processors. It is the company that made the glass for Edison's light bulb and the glass on the front of most phones.

What those three buyers want is the strand of glass between the chips. It is the one part of the AI network that is laid once and then outlives every chip generation that talks through it.

Corning owns the part of the AI network that does not go out of date.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think of the water pipes in your house. You might replace the taps, the shower head and the boiler several times. The pipes inside the walls stay where they were put when the house was built.</p>
<p>Now imagine every new boiler pushed twice as much water as the last. You would still change the boiler. But you would be very glad someone had laid wide, smooth pipes in the first place, because tearing out the walls is the expensive part.</p>
<p>In an AI data centre the boilers are the chips and the plugs. The pipes are glass fibre. Corning lays the pipes, and every time the building grows, it needs more of them.</p>
</details>

## Three words you need

**Optical fibre.** A strand of glass thinner than a human hair that carries data as pulses of light. It has two layers. The core in the middle carries the light, and the cladding wrapped around it keeps the light in.

**Passive.** Equipment with no electronics in it. A fibre, a cable or a connector does not compute or convert anything. It only carries. Corning's AI business sits almost entirely in this passive layer.

**Optical transceiver.** The thumb-sized plug at each end of a fibre that turns electrical signals into light and back again. Coherent and Lumentum make them, and every new chip generation needs a faster one.

## Why the glass is hard to make

Training an AI model splits the work across thousands of chips that must swap partial results every few moments. As I wrote in an earlier piece, a slow link leaves the most expensive silicon ever built sitting idle while it waits.

Inside a cabinet, copper wire carries most of that traffic. At today's speeds a copper signal fades into noise within about two metres, roughly the height of a rack. Beyond that, everything travels as light down glass.

In 1970 three Corning scientists made glass clear enough to carry light for kilometres. The trick is that the cladding bends light slightly less than the core. Light striking the boundary at a shallow angle is reflected back inward, an effect called total internal reflection, so it stays trapped for very long distances.

Making that glass is unforgiving work. Purified silica is laid down with small additives that tune how it bends light, then drawn into a hair-thin strand at more than a kilometre a minute. The width is held to millionths of a metre, and the coating must be flawless.

A small error lets light leak, and leaked light shortens the distance a signal can travel. That accumulated process knowledge, built up since 1970, is the reason a new entrant cannot simply buy its way in.

## Where the extra fibre comes from

The demand comes from two directions at once, and both grow faster than the chip count.

**Inside the rack.** According to Corning, a modern AI rack of 72 GPUs wired to act as one machine needs about sixteen times more fibre than a traditional cloud switch rack. Every chip needs many more connections to every other chip.

**Between buildings.** The largest clusters now draw so much power that they no longer fit in one building. They spread across campuses, sometimes kilometres apart, and every building has to be stitched to every other with very large fibre counts.

The second direction matters most. Double the number of buildings and the links between them more than double, because each new hall must reach all the others. That is a physical relationship, not a forecast.

Then there is the part that makes the glass different from everything plugged into it. When the industry moves from 800 gigabits a second per link to 1.6 terabits, the transceivers at each end are replaced. The fibre in the ceiling trays usually stays, carrying each new generation in turn.

## What Corning's own numbers show

If the mechanism is real, Corning's fibre business should be growing faster than the rest of the company, earning more on each sale, and running short of factory space. All three show up in its filings.

**Growth.** In the second quarter of 2026, reported on 28 July 2026, Optical Communications sales rose 32 per cent to $2.07 billion. Within that, Enterprise Networks, the data centre business, grew 65 per cent, and Corning said its AI products grew significantly faster still.

**Profit per sale.** The segment's net income rose 77 per cent to $438 million in the same quarter, about 21 per cent of its sales. Profit growing more than twice as fast as sales is what full factories and firm demand look like in money.

**Supply.** Corning said demand for its high-density data centre products is running above its production capacity. Under the Nvidia partnership it plans to expand American optical connectivity capacity tenfold and American fibre production by more than half.

**Concentration.** In its annual report for 2025, Corning said two end customers made up 28 per cent of Optical Communications sales, which totalled $6.27 billion that year. When the buyers are this few and this large, they set the terms.

It is also worth keeping the scale in proportion. Optical Communications was 38 per cent of Corning's segment sales in 2025. The rest is display glass, phone cover glass, car exhaust filters, solar materials and laboratory and pharmaceutical glass. Corning is a glass company with a fast-growing AI business inside it, not an AI company.

## What would prove me wrong

The obvious risk is that fibre stops being scarce. Corning is expanding hard, and so are producers in China. Scarcity is what lets a supplier hold its terms, and the hyperscalers, the giant cloud companies, will push hard on price the moment supply loosens.

Corning has lived through this exact film. In the telecom fibre boom of the late 1990s it expanded on forecasts of near-endless demand. When the boom broke, it reported a $4.8 billion loss for the second quarter of 2001, mostly writing down the value of businesses it had bought, and cut thousands of jobs.

The difference this time is the customer. In 2001 Corning sold to borrowed-money telecom start-ups that went bankrupt. Today it sells to Amazon, Meta and Nvidia, under multi-year agreements. That is a real difference, but it does not repeal the cycle.

So I watch three things. Whether Enterprise Networks keeps growing faster than the rest of Optical Communications. Whether the segment holds its profit margin while sales rise, because a falling margin on rising sales would mean the scarcity is ending. And whether the two largest customers grow as a share of the segment.

<section class="exposure">
<h3>Who is exposed if the glass, not the plug, is the part that lasts</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are Corning's own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Corning</span> makes optical fibre, cable, connectors and preassembled connectivity systems for data centres, alongside display, phone and specialty glass.</dd>
<dt>Other fibre and cable makers</dt>
<dd><span class="names">Prysmian</span>, <span class="names">Fujikura</span> and <span class="names">Sumitomo Electric</span> make optical fibre and high-count cable. <span class="names">YOFC</span> makes optical fibre and preforms in China.</dd>
<dt>The plug makers</dt>
<dd><span class="names">Coherent</span>, <span class="names">Lumentum</span> and <span class="names">Innolight</span> make the transceivers and lasers at each end of the fibre.</dd>
<dt>The traffic control</dt>
<dd><span class="names">Arista</span> and <span class="names">Cisco</span> make the network switches the fibre connects.</dd>
<dt>The buyers who paid ahead</dt>
<dd><span class="names">Meta</span>, <span class="names">Amazon</span> and <span class="names">Nvidia</span> have each signed multi-year agreements with Corning to secure fibre and connectivity supply.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Copper cable makers wherever a link stretches beyond a couple of metres. And Corning itself, if the industry's new fibre capacity arrives faster than the campuses that need it.</dd>
</dl>
</section>

---

<p class="sources">Sources: Meta announcement of its agreement with Corning, 27 January 2026. Nvidia and Corning partnership announcement, May 2026. Amazon and Corning agreement announcement, 8 June 2026. Corning second quarter 2026 results, released 28 July 2026, for Optical Communications sales, net income, Enterprise Networks growth and capacity commentary. Corning annual report on Form 10-K for 2025 for segment sales, mix and customer concentration. Corning commentary on fibre required by 72-GPU AI racks. Corning results for the second quarter of 2001. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
