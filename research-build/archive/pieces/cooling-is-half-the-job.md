---
title: "Electricity doesn't get used up making AI. It turns into heat. Cooling is half the job."
date: 2026-08-21
summary: "Almost every watt that goes into an AI chip comes out as heat, and one cabinet now gives off as much as eighty space heaters. Air can't carry that away. So the biggest plumbing change in the history of data centres is happening right now, and it doesn't care which chip company wins."
category: "Explainer"
cover: "/covers/cooling.svg"
tags: ["cooling", "data-centres", "liquid"]
---

There is a fact about computers that most people never think about, and once you know it the whole cooling industry makes sense.

A chip does not use up power the way a kettle uses up water. Almost every watt that goes in comes back out as heat.

So when a cabinet of AI chips draws 120 kilowatts, it gives off 120 kilowatts of heat. That is roughly eighty space heaters running flat out inside a box the size of a fridge.

Getting that heat out of the building is not a support function. It is half the job.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A laptop gets warm on your knees. Now picture eighty hairdryers running inside a wardrobe with the door shut. That is one modern AI cabinet, and no fan will fix it.</p>
<p>Step out of a swimming pool on a breezy day and you feel far colder than standing dry in the same breeze. The water carries the heat off your skin. Cooling is moving from blowing air to running liquid onto the chip.</p>
</details>

## Why air stopped working

For twenty years data centres were cooled with air. Fans pushed cold air through the servers, and that worked because a normal rack drew 5 to 10 kilowatts.

Somewhere between 30 and 50 kilowatts per rack, air simply cannot carry heat away fast enough. Water, per unit of volume, carries heat roughly three thousand times better.

So the mainstream answer in 2026 is direct-to-chip. A metal plate with liquid channels sits on each chip, and hoses run to a CDU, the coolant distribution unit, which pumps liquid round the loop like the rack's heart. Current flagship AI racks require it. The most extreme option, immersion, dunks the whole server in non-conductive fluid.

None of this can be bolted on quickly. Many buildings designed for air have floors, plumbing and electrical rooms that cannot take liquid without a refit.

## What the industrial companies did

Cooling is indifferent to who wins the chip war. Whether the chips come from Nvidia, AMD or Google, the heat has to go somewhere.

The industrial companies have said as much with their own money. Within months of each other, Eaton bought Boyd Thermal and Schneider Electric bought Motivair, both specialist liquid-cooling businesses. Two electrical giants buying into the same niche tells you what they think every future data centre looks like.

## What binds: efficiency and water

Efficiency is measured by PUE, power usage effectiveness: the electricity entering the building divided by what reaches the computers. Old air-cooled halls run around 2.0, modern liquid-cooled ones around 1.1, and Singapore rations capacity by it.

Water is the other limit. Some cooling designs evaporate millions of gallons a year, and in dry regions water now decides where a facility can be built at all.

<section class="exposure">
<h3>Who is exposed if cooling moves to liquid</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The one-stop suppliers</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span> and <span class="names">Eaton</span> make power gear and liquid cooling.</dd>
<dt>The specialists</dt>
<dd><span class="names">CoolIT</span> makes cold plates, <span class="names">nVent</span> loops and enclosures, <span class="names">Munters</span> air handlers, <span class="names">Modine</span> chillers and <span class="names">Asetek</span> cooling loops.</dd>
<dt>The component layer</dt>
<dd><span class="names">Delta, LiteOn</span> and other Taiwanese suppliers make pumps, plates and distribution units.</dd>
<dt>The chips that make the heat</dt>
<dd><span class="names">Nvidia, AMD</span> and the cloud giants design the silicon, and all of it gives off heat.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Air-only cooling incumbents, and existing buildings that cannot take liquid without a refit.</dd>
</dl>
</section>

---

<p class="sources">This piece explains mechanism: why air fails, how liquid cooling works and what PUE measures, using physical figures and two acquisitions of public record. I hold no view here on individual equipment makers. Personal research, not investment advice.</p>
