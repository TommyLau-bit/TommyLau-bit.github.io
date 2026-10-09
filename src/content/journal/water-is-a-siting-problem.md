---
title: "Data centre water decides where AI campuses go, not how many get built"
date: 2026-10-09T16:42:46+08:00
summary: "Data centres use water mainly to cool themselves, by letting it evaporate, because that saves electricity. Where water is short, a site can stop evaporating and pay with a little more power instead. So data centre water shapes where campuses go and how they are cooled, and most of their water is used at the power station anyway."
category: "Analysis"
cover: "/covers/water-is-a-siting-problem.svg"
tags: ["cooling", "data-centres", "power"]
draft: true
---

A Google data centre planned for Santiago, Chile, was challenged over the city's aquifer, the underground store of water it relies on.

Google did not walk away. It asked to swap the building's water cooling towers for air-cooled chillers, which would end its draw from three wells. In February 2024 a court still sent the permit back, and the project went back to the start.

That is the story of data centre water in miniature.

Data centre water decides where AI campuses go and how they are cooled. It does not decide how many get built.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>On a hot day you can cool off two ways. Sit by a fan with a wet flannel on your neck, and the evaporating water does the work for almost no electricity. Or shut the windows and run the air conditioner, which uses no water but far more power.</p>
<p>A data centre makes the same choice on its roof. Where water is short, it switches on the air conditioner. The bill moves from the tap to the meter.</p>
</details>

## How the water leaves

Engineers separate withdrawal, water taken in and mostly returned, from consumption, water lost for good. For a data centre, the water that matters is consumed, and almost all of it leaves as vapour.

A cooling tower, the open unit on many data centre roofs, evaporates water to carry heat away. That is cheap, so the chillers, the building's giant refrigerators, run less. Microsoft says it plainly: water has been evaporated on site to reduce the power demand of the cooling systems.

Liquid cooling at the chip does not settle this by itself. The loop to the chip is sealed, but its heat still has to leave the building. It goes either through a tower that evaporates water or through a dry cooler, a huge radiator with fans, that evaporates none.

In a dry basin, water supply cannot simply catch up. An aquifer under drought cannot be enlarged, and local water rights are already spoken for. So a data centre in that basin gives up water and pays in electricity instead.

## Where the water really goes

The best national count is Lawrence Berkeley National Laboratory's December 2024 report on American data centres. It estimates they consumed 66 billion litres of water on site in 2023.

The power stations making their electricity are estimated to have consumed nearly 800 billion litres, about twelve times as much. Most of a data centre's water follows its electricity, not its cooling design.

Microsoft has drawn the same conclusion in its designs. Since August 2024 its new data centre designs evaporate no water for cooling. The cost, in its own words, is a nominal increase in energy use.

## What would prove me wrong

I am wrong if a large AI campus with its power already secured is cancelled outright over water, rather than redesigned to cool without it.

I am also wrong if Microsoft's water per kilowatt-hour of computing climbs back above 0.30 litres, its fiscal 2024 level, as its AI campuses grow. It reported 0.27 for fiscal 2025. Either would mean water is binding, not being traded away.

<section class="exposure">
<h3>Who is exposed if water decides where, not how many</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The operators who publish their water</dt>
<dd><span class="names">Microsoft</span>, <span class="names">Google</span>, <span class="names">Meta</span> and <span class="names">Amazon</span> run data centres and report their water use each year.</dd>
<dt>Cooling that needs less water</dt>
<dd><span class="names">Vertiv</span>, <span class="names">Schneider Electric</span>, <span class="names">nVent</span> and <span class="names">CoolIT</span> make liquid cooling loops and pump units.</dd>
<dt>Chillers and dry coolers</dt>
<dd><span class="names">Trane</span>, <span class="names">Carrier</span> and <span class="names">Johnson Controls</span> make air-cooled chillers. <span class="names">Munters</span> makes air handlers and coolers.</dd>
<dt>Water treatment</dt>
<dd><span class="names">Ecolab</span> makes treatment for cooling tower and recycled water.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Campuses planned around cheap evaporative cooling in dry basins, and sites whose power allocation cannot stretch to the extra electricity that dry cooling needs.</dd>
</dl>
</section>

---

<p class="sources">Sources: Lawrence Berkeley National Laboratory, its report on United States data centre energy use, December 2024; Microsoft, its announcement of zero-water cooling designs, 9 December 2024; Chile's Second Environmental Court, ruling of 26 February 2024, which records Google's 2022 cooling change. Personal research, not investment advice.</p>
