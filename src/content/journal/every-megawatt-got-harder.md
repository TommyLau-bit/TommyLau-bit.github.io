---
title: "Vertiv is paid per megawatt, and AI has made every megawatt harder to build"
date: 2026-09-25T12:30:00+08:00
summary: "Vertiv makes the equipment that keeps electricity flowing into a data centre and carries the heat back out. An AI cabinet now draws more than ten times the power of an ordinary one, so every unit of capacity needs more of that equipment, and more complicated versions of it. Vertiv gets paid for every new building, and again for how much harder each one has become."
category: "Analysis"
cover: "/covers/every-megawatt-got-harder.svg"
tags: ["power", "cooling", "data-centres"]
draft: false
updated: 2026-10-08T16:00:00+08:00
updateNote: "Shortened and made plainer on 8 October 2026. The claim and the test of it are unchanged."
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

Vertiv's roots go back to Liebert, which has cooled computer rooms since the mainframe era. Almost everything it sells today falls into four groups.

**Backup power.** The UPS, the uninterruptible power supply, is a large battery system between the grid and the servers. If utility power dips for even half a second, it carries the whole load until the generators start.

**Power distribution.** Switchgear, the heavy equipment that connects and isolates circuits safely, and busway, metal power rails running above the racks. This carries electricity from the edge of the building to every cabinet.

**Thermal management.** Everything from precision air conditioning to full liquid cooling. The centrepiece for AI is the coolant distribution unit, which pumps liquid to metal plates clamped onto each chip.

**Service.** Vertiv's own engineers install, maintain and monitor all of it. Once the gear is inside a building, the same company tends to look after it for years.

## Why each megawatt now needs more

For twenty years a typical server rack drew a dozen kilowatts or less. Air conditioning handled that easily, with cold air in at the front and hot air out of the back.

An AI rack draws more than ten times as much, and Nvidia's roadmap points towards a megawatt in one cabinet. Air stops working somewhere between 30 and 50 kilowatts per rack. Beyond that, the heat has to leave through liquid, which carries it far better than air.

That shift changes what a megawatt of building contains. An air-cooled hall needs fans and chillers. A liquid-cooled hall needs those plus pumps, pipework to every rack, heat exchangers and sensors on every loop.

The same megawatt now carries more equipment, more engineering and more that can go wrong. Much of that is equipment Vertiv makes.

The power side is changing the same way. At these densities the copper inside each rack becomes impractical, so the industry is moving to 800 volts of direct current. Vertiv has been designing that equipment alongside Nvidia, with the product line planned for the second half of 2026.

AI did not only create demand for more data centres. It made the inside of each one denser, hotter and more complicated.

## Where the second win shows up

If the claim is right, Vertiv's own results should show more than volume. They should show each sale getting richer, and the installed gear needing more care.

Orders came first. In the last quarter of 2025 Vertiv was signing new orders at nearly three times the rate it shipped goods. Buyers were committing well ahead of delivery.

Then the margin moved. Operating margin is the share of each sale left after running costs. In the second quarter of 2026, Vertiv's operating margin, on its own adjusted measure, widened by more than four points.

A supplier widening its margin that fast while volume grows is not discounting to win work. I read that as richer content per order, showing up in money.

Service tells the same story. In the same quarter, service revenue grew faster than product sales. Liquid loops and high-voltage gear need more upkeep than a room of air conditioners, so this is what I would expect.

## Why the one-stop shop matters, and where it is weak

The large electrical groups, Schneider Electric, Eaton, ABB and Siemens, all sell into data centres. For each of them it is one division among many.

The building-cooling firms, Trane, Carrier and Johnson Controls, know heat well but have little on the power side. The liquid-cooling specialists move fast but usually make one product and lack a global service force.

Vertiv's case is that a builder racing to open an AI hall would rather buy power, cooling and service from one supplier. When a building full of chips is waiting to switch on, one fewer handover is one fewer delay.

That lead is real, but not guaranteed. Schneider and Eaton have both bought liquid-cooling specialists, and the biggest cloud operators are designing cooling in-house. A business resting on a few very large buyers can have its year changed by one of them pausing.

There is also a gap in the evidence. Since early this year, Vertiv's results have stopped including a backlog figure, the orders signed but not yet delivered. So I now read demand through sales and margin instead.

## What would prove me wrong

I am wrong if Vertiv's growth only ever tracks the number of megawatts being built. That would make it a volume business riding the buildout, not a supplier whose content per megawatt is rising.

I am also wrong if its margin shrinks while orders stay strong. That would mean liquid cooling is becoming a commodity that anyone can bolt on.

And I am wrong if the biggest buyers take cooling in-house at scale, or split the job between specialists.

So I watch four things. Adjusted operating margin, quarter by quarter. Service revenue against product revenue. Whether Vertiv's 800 volt line ships on Nvidia's timetable. And whether Vertiv ever brings back a backlog figure.

<section class="exposure">
<h3>Who is exposed if every megawatt keeps getting harder</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Where this piece draws on Vertiv's own disclosures, they are used as evidence for the mechanism, and I draw no conclusion from them about value.</p>
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

<p class="sources">Sources: Vertiv fourth quarter and full year 2025 results, released 11 February 2026, for orders. Vertiv first quarter 2026 results, released 22 April 2026. Vertiv second quarter 2026 results, released 29 July 2026, for sales, adjusted operating margin and the product and service split. Vertiv announcements on the Nvidia 800 VDC architecture, May and October 2025. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
