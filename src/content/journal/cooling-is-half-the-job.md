---
title: "Electricity doesn't get used up making AI. It turns into heat. Cooling is half the job."
date: 2026-09-18
summary: "Almost every watt that goes into an AI chip comes out as heat, and one cabinet now gives off as much as eighty space heaters. Air can't carry that away. So the biggest plumbing change in the history of data centres is happening right now, and it doesn't care which chip company wins."
category: "Explainer"
cover: "/covers/cooling.svg"
tags: ["cooling", "data-centres", "liquid"]
---

There is a fact about computers that most people never think about, and once you know it the whole cooling industry makes sense.

Electricity is not consumed by computation. A chip does not use up power the way a kettle uses up water. Almost every watt that goes in comes back out again, as heat. A data centre is, in energy terms, a very expensive electric heater that happens to think on the way through.

So when a cabinet of AI chips draws 120 kilowatts, it is also giving off 120 kilowatts of heat. That is roughly eighty domestic space heaters running flat out inside a box the size of a fridge. A single flagship AI chip alone gives off more than a thousand watts, a space heater the size of a postcard.

Getting that heat out of the building is not a support function. It is half the job.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>A laptop gets warm on your knees. That is about 50 watts of heat. Now picture eighty hairdryers running inside a wardrobe with the door shut. That is one modern AI cabinet.</p>
<p>You cannot fix that with a fan. To carry that much heat away with air you would need something close to a gale blowing through the electronics.</p>
<p>Water is simply a better lorry for heat. Think of stepping out of a swimming pool on a breezy day and how much colder you feel than standing in the same breeze dry. Same air, but the water is carrying the heat off your skin. That is the whole industry shift in one image: the cooling is moving from blowing air at the problem to running liquid right onto the chip.</p>
</details>

## Why air stopped working

For twenty years data centres were cooled with air. Fans pushed cold air through the servers, warm air came out the back, and chillers cooled it down again. That worked because a normal server rack drew 5 to 10 kilowatts.

Air has a limit, and the industry has just passed it permanently. Somewhere between 30 and 50 kilowatts per rack, air simply cannot carry heat away fast enough. To cool a 120 kilowatt rack with air you would need something close to hurricane-force wind blowing through the electronics.

Water is a different animal. Per unit of volume it carries heat roughly three thousand times more effectively than air. So the industry is doing what car engines did a century ago: switching from air to liquid.

## Three ways to do it

**Rear-door heat exchanger.** A water-cooled radiator bolted to the back of the rack. The servers still cool themselves with air, but the hot air hits a cold radiator before it leaves. A transitional patch for existing buildings.

**Direct-to-chip.** This is the mainstream answer in 2026. A metal plate with liquid channels sits directly on each chip, the way a water block sits on a gaming PC's processor, and hoses run to a unit called a CDU, the coolant distribution unit, which is effectively the rack's heart, pumping liquid round the loop. The current flagship AI racks require this. It is not an option.

**Immersion.** Dunk the entire server in a tank of non-conductive fluid. Think of deep-frying a computer that never burns. The most extreme option, and the one that handles the most heat per rack.

## The number that turns physics into money

Data centre efficiency is measured by a single ratio called PUE, power usage effectiveness. It is the total electricity entering the building divided by the electricity that actually reaches the computers. A perfect score is 1.0. Everything above that is overhead, and most of the overhead is cooling.

Old air-cooled data centres run around 2.0, meaning for every watt reaching a chip, another watt was spent on fans and chillers. Modern liquid-cooled ones run around 1.1. Take that gap, multiply it by a gigawatt of demand and by the price of electricity, and it is real money every hour of every day. This is why Singapore, which rations data centre capacity by efficiency, set its bar at a PUE of 1.25 or better.

There is a catch on the water side. Some cooling designs evaporate millions of gallons a year, and in dry regions that has become a permitting fight. Water availability now decides where facilities can be built at all.

## Why this is the clearest picks-and-shovels lane in the stack

The thing I find compelling about cooling is that it is indifferent to who wins the chip war. Whether the chips are made by Nvidia, AMD, Google or someone not yet founded, they will give off heat, and the heat has to go somewhere. Heat is heat.

The industrial companies have said as much with their wallets. Within months of each other, Eaton bought Boyd Thermal and Schneider Electric bought Motivair, both specialist liquid-cooling businesses. When two disciplined electrical giants pay up for the same niche at the same time, they are telling you what they think every future data centre looks like. I read acquisitions like that as revealed preference. They are a better signal than any forecast.

## What I'm watching

Three things. Whether immersion moves from the fringe to the mainstream as racks pass 600 kilowatts, because at that density even direct-to-chip starts to strain. Whether water permitting becomes a hard cap on siting in the places with the cheapest power. And the PUE figures that operators actually publish, because the gap between a design target and a running building is where the money either is or isn't.

<section class="exposure">
<h3>Who is exposed if cooling moves to liquid</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The one-stop suppliers</dt>
<dd><span class="names">Vertiv</span> sells both the power gear and the liquid cooling, which is rare. <span class="names">Schneider Electric</span> and <span class="names">Eaton</span> bought their way in, Schneider acquiring Motivair and Eaton acquiring Boyd Thermal. Two disciplined industrials paying up for the same niche within months of each other is revealed preference, and it is a better signal than any forecast.</dd>
<dt>The specialists</dt>
<dd><span class="names">CoolIT</span> makes cold plates shipping inside many brand-name servers. <span class="names">nVent</span> makes loops and enclosures. <span class="names">Munters, Modine and Asetek</span> sit in adjacent parts of the thermal chain.</dd>
<dt>The component layer</dt>
<dd>Pumps, plates and distribution units from <span class="names">Delta, LiteOn</span> and the Taiwanese thermal suppliers feeding the rack builders.</dd>
<dt>Why this lane is unusually clean</dt>
<dd>Cooling does not care which chip company wins. Whether the silicon is <span class="names">Nvidia, AMD</span> or a hyperscaler's own design, it produces heat and the heat has to go somewhere.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Air-only cooling incumbents, and existing buildings whose floor loading, plumbing and electrical rooms cannot take liquid without a refit.</dd>
</dl>
</section>

---

<p class="sources">This piece explains mechanism: why air fails, how liquid cooling works, and what PUE measures. The figures used are physical and structural (heat per chip, the air ceiling, the water-versus-air ratio, typical PUE ranges). The two acquisitions are a matter of public record. I hold no view here on individual equipment makers. Personal research, not investment advice.</p>
