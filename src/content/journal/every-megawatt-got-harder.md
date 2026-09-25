---
title: "Vertiv is paid per megawatt, and AI has made every megawatt harder to build"
date: 2026-09-25T12:30:00+08:00
summary: "Vertiv makes the equipment that keeps electricity flowing into a data centre and carries the heat back out. An AI cabinet now draws more than ten times the power of an ordinary one, so every unit of capacity needs more of that equipment, and more complicated versions of it. Vertiv gets paid for every new building, and again for how much harder each one has become."
category: "Analysis"
cover: "/covers/every-megawatt-got-harder.svg"
tags: ["power", "cooling", "data-centres"]
draft: false
---

A single Nvidia AI chip gives off more than a thousand watts. Put 72 of them in one cabinet and that cabinet draws about 130 kilowatts, roughly what a hundred American homes use, in the footprint of a fridge.

All of that power has to arrive without a flicker, and all of it leaves again as heat. So every AI building has two physical jobs besides thinking. Get the electricity in without anything failing, and get the heat out before the chips cook.

Vertiv does neither of the glamorous things. It makes no chips and writes no software. It makes the equipment that does those two jobs, and very little else.

For decades that was a steady, unremarkable business. AI changed not only how many buildings go up, but how much of Vertiv's equipment sits inside each one.

Vertiv is paid per megawatt, and AI has made every megawatt harder to build.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think about the electrician who wires new houses. For decades every house needed the same job: a fuse box, some sockets, a few lights. The electrician was paid per house, and each house looked much like the last.</p>
<p>Now every new house wants an induction hob, a heat pump and a car charger. The old fuse box cannot carry that, and nobody charges a car off an extension lead. The job inside each house has grown, and it needs someone who knows what they are doing.</p>
<p>So the electrician gains twice. More houses are being built, and each one is a bigger job than it used to be. That is Vertiv's position inside an AI data centre.</p>
</details>

## Four things Vertiv makes

Vertiv's roots go back to Liebert, which has cooled computer rooms since the mainframe era. It spent decades inside Emerson Electric, was sold off in 2016 and listed in New York in 2020. Almost everything it sells falls into four groups.

**Backup power.** The UPS, the uninterruptible power supply, is a large battery system sitting between the grid and the servers. If utility power dips for even half a second, the UPS carries the whole load until the generators start. Without it, one flicker can wreck a training run that took weeks.

**Power distribution.** Switchgear, the heavy equipment that connects and isolates circuits safely, and busway, metal power rails running above the racks. This is the wiring that carries electricity from the edge of the building to every cabinet.

**Thermal management.** Everything from precision air conditioning to full liquid cooling. The centrepiece for AI is the CDU, the coolant distribution unit, which pumps liquid to cold plates clamped onto each chip and passes the heat into the building's water loop.

**Service.** Vertiv's own engineers install, maintain and monitor all of it. Once the gear is inside a building, the same company tends to look after it for years.

## Why each megawatt now needs more

For twenty years a typical server rack drew somewhere between 5 and 12 kilowatts. Air conditioning handled that easily, with cold air in at the front and hot air out of the back.

An AI rack draws more than ten times as much, and Nvidia's roadmap points towards 600 kW and eventually a megawatt in one cabinet. As I have written before, air stops working somewhere between 30 and 50 kW per rack. Beyond that, the heat has to leave through liquid, which carries it thousands of times better than air.

That shift changes what a megawatt of building contains. An air-cooled hall needs fans and chillers. A liquid-cooled hall needs those plus CDUs, pipework to every rack, heat exchangers and sensors on every loop. The same megawatt now carries more equipment, more engineering and more that can go wrong.

The power side is changing the same way. At these densities the copper inside each rack becomes impractical, so the industry is moving to 800 volts of direct current delivered straight to the rack. Vertiv has been designing its 800 VDC equipment alongside Nvidia since May 2025, with the product line planned for the second half of 2026, ahead of Nvidia's 2027 rack generation.

AI did not only create demand for more data centres. It made the inside of each one denser, hotter and more complicated.

## Where the second win shows up in Vertiv's numbers

If the claim is right, Vertiv's own figures should show more than volume. They should show each sale getting richer, and the installed gear needing more care.

**Orders.** In the fourth quarter of 2025, Vertiv's organic orders, new orders excluding acquisitions and currency effects, rose about 252 per cent on a year earlier. Its book-to-bill ratio, new orders divided by sales shipped, was about 2.9. Backlog, orders signed but not yet delivered, ended 2025 at $15.0 billion, up 109 per cent.

**Margin.** In the second quarter of 2026, sales reached $3.27 billion, up 24 per cent, or 18 per cent organically. Adjusted operating margin, the share of each sale left after running costs with one-off items stripped out, rose 4.1 points to 22.6 per cent. A supplier widening its margin that fast while volume grows is not discounting to win work. That is what richer content per order looks like in money.

**Service.** In the same quarter, service revenue grew 33 per cent against 22 per cent for products. Liquid loops and high-voltage gear need more upkeep than a room of air conditioners. Service outgrowing hardware is what I would expect if each building has become harder to keep running.

Geography agrees. Organic sales grew 21 per cent in the Americas and 26 per cent in Asia Pacific, where AI capacity is going up fastest, and fell 2 per cent across Europe, the Middle East and Africa.

## Why the one-stop shop matters, and where it is weak

The large electrical groups, Schneider Electric, Eaton, ABB and Siemens, all sell into data centres. For each of them it is one division among many. The building-cooling firms, Trane, Carrier and Johnson Controls, know heat well but have little on the power side. The liquid-cooling specialists move fast but usually make one product and lack a global service force.

Vertiv's case is that a builder racing to open an AI hall would rather buy power, cooling and service from one supplier than coordinate five. When a building full of chips is waiting to switch on, one fewer handover is one fewer delay.

That lead is real, but not guaranteed. Schneider and Eaton have both bought liquid-cooling specialists, and the biggest cloud operators are designing cooling in-house. A business resting on a few very large buyers can have its year changed by one of them pausing.

There is also a gap in the evidence. Since the first quarter of 2026, Vertiv's results have not included a backlog figure. That was the cleanest single measure of forward demand, so I now have to read demand through sales and margin instead.

## What would prove me wrong

I am wrong if Vertiv's growth only ever tracks the number of megawatts being built. That would make it a volume business riding the buildout, not a supplier whose content per megawatt is rising.

The numbers give a sharper test. If each megawatt really needs more of what Vertiv makes, margin should keep widening as volume grows, and service should keep outgrowing products. Margin shrinking while orders stay strong would mean liquid cooling is becoming a commodity that anyone can bolt on.

I am also wrong if the biggest buyers pull cooling in-house at scale, or split the job between specialists.

So I watch four things. Adjusted operating margin, quarter by quarter. The split between service and product revenue. Whether Vertiv's 800 VDC line ships on Nvidia's timetable. And whether Vertiv ever brings back a backlog number.

<section class="exposure">
<h3>Who is exposed if every megawatt keeps getting harder</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. The financial figures in this piece are Vertiv's own disclosures, used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
<dl>
<dt>The subject</dt>
<dd><span class="names">Vertiv</span> makes uninterruptible power supplies, switchgear, busway, precision air conditioning, coolant distribution units and liquid cooling systems for data centres, and services them.</dd>
<dt>The electrical groups</dt>
<dd><span class="names">Schneider Electric</span>, <span class="names">Eaton</span>, <span class="names">ABB</span> and <span class="names">Siemens</span> make switchgear, power distribution and backup power across many industries. Schneider added Motivair and Eaton added Boyd Thermal for liquid cooling.</dd>
<dt>The building-cooling firms</dt>
<dd><span class="names">Trane</span>, <span class="names">Carrier</span> and <span class="names">Johnson Controls</span> make chillers and large-scale air conditioning for buildings, including data centres.</dd>
<dt>The liquid-cooling specialists</dt>
<dd><span class="names">nVent</span> makes liquid cooling loops and enclosures. <span class="names">Modine</span> makes data centre chillers and air handlers. <span class="names">CoolIT</span> makes cold plates and coolant distribution units.</dd>
<dt>The roadmap setter</dt>
<dd><span class="names">Nvidia</span> designs the AI racks whose power and heat set the specification.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Air-only cooling suppliers, and older halls whose electrical rooms and plumbing cannot take liquid without a refit. And Vertiv's own case, wherever the largest buyers design their own cooling or liquid cooling becomes a commodity.</dd>
</dl>
</section>

---

<p class="sources">Sources: Vertiv fourth quarter and full year 2025 results, released 11 February 2026, for organic orders, book-to-bill and backlog. Vertiv first quarter 2026 results, released 22 April 2026. Vertiv second quarter 2026 results, released 29 July 2026, for sales, adjusted operating margin, the product and service split, regional organic growth and full year guidance. Vertiv announcements on the Nvidia 800 VDC architecture, May and October 2025. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
