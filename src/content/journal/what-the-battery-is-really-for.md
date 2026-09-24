---
title: "The battery has quietly stopped being an energy product"
date: 2026-09-22T19:01:00+08:00
summary: "Most people still think of grid batteries as a way to store cheap electricity and sell it later. That is no longer the main reason they are being bought. A battery now lets a data centre switch on before its grid connection is finished, and absorbs the violent swings that AI computing creates. It has become a way of getting connected."
category: "Analysis"
cover: "/covers/what-the-battery-is-really-for.svg"
tags: ["grid", "power", "data-centres"]
draft: false
---

Ask most people what a grid battery is for and you get the same answer. Store electricity when it is cheap and plentiful, release it when it is scarce.

That is a real job and batteries still do it.

It is no longer the job that explains who is buying them.

The battery has been quietly reassigned. It is becoming a piece of connection equipment, bought by people who are not primarily interested in storing energy at all.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Think about moving into a flat where the gas has not been connected yet. You want to cook tonight, not in four months when the engineer finally comes.</p>
<p>So you buy a camping stove. You did not buy it because you wanted a camping stove. You bought it because it lets you start living in the flat before the utility is ready for you.</p>
<p>A grid battery is now doing the same job at industrial scale. It is bought so a building can open before its connection is finished, and once the connection arrives, it stays useful for something else entirely.</p>
</details>

## Three jobs, and only one of them is the famous one

A battery sitting next to a large computing site is now doing up to three different things, and they have almost nothing to do with each other.

**Getting open early.** A site with a partial connection can draw a limited amount of power continuously. A battery lets it run at higher output for part of the day by discharging, then refill slowly when demand is low. The building opens and starts earning while the wires are still being finished. Nothing about that is an energy trade. It is a scheduling trick.

**Absorbing the violence.** AI workloads swing hard and fast. I have written about what happens when a gigawatt of demand disappears in under a second. A battery between the grid and the computers can smooth some of that, which matters more now that grid operators are starting to treat sudden load changes as a reliability problem rather than a curiosity.

**Buying low and selling high.** The original job. Still there, still real, and increasingly the least interesting reason anyone is writing the cheque.

## Where this is visibly happening

The United States gives the clearest picture because the data is published.

Developers planned to add **24 gigawatts** of utility-scale battery storage in 2026. **12.9 gigawatts of that, 53 per cent of the national total, is in Texas.**

Texas is not half the American economy. It is, however, where an enormous amount of new computing load is arriving, on a grid that is separate from the rest of the country and that has been unusually open about the strain.

When over half of a country's new storage lands in one state, and that state is also where the load growth is, the simplest explanation is usually the right one. The storage is following the load, not the electricity price.

## Why this breaks the usual way of counting

For a decade, forecasts of battery demand were built on the electric vehicle industry. Cells were cheap because cars needed them, and grid storage was treated as a side effect of automotive scale.

That relationship still exists in manufacturing. It no longer explains demand.

If you model grid storage as a function of electric vehicle adoption, you will miss a buyer who does not care about cars, is not price sensitive in the same way, and is buying for a reason that did not exist five years ago. A data centre developer buying a battery to open eight months early is not comparing it to the cost of stored electricity. They are comparing it to eight months of not earning anything.

**That is a completely different willingness to pay, and it is attached to a completely different clock.**

## The honest limit

I want to be careful about how far this goes.

A battery is a bridge, not a connection. It does not remove the need for the substation, the transformer or the queue. It changes when a site can start operating relative to that equipment arriving, which is valuable, and it does not make the equipment arrive sooner.

So this is not a counterargument to the thing I have been writing about all year. It is a symptom of it. You do not buy a bridge unless the gap is real.

## What would prove me wrong

The clean falsifier is location. If the next few years of storage additions stop clustering where the computing load is, and spread out in line with renewable generation instead, then the buyer I am describing is smaller than I think and the old model is still the right one.

I would also be wrong if connection timelines shorten enough that opening early stops being worth paying for. That is the same falsifier that sits under everything else in this journal, and it points the same way: watch the queue, not the battery.

So I watch where new storage is built relative to new computing load, whether grid operators start requiring this kind of equipment rather than merely permitting it, and whether anyone begins reporting storage bought for connection reasons separately from storage bought for trading. Right now that distinction is invisible in the published numbers, which is part of why I think it is underrated.

<section class="exposure">
<h3>Who is exposed if the battery is really a connection product</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The system builders</dt>
<dd><span class="names">Fluence</span> and <span class="names">Tesla Energy</span> build grid-scale battery systems and the software that decides when they charge and discharge.</dd>
<dt>The power electronics between battery and grid</dt>
<dd><span class="names">Sungrow</span> and <span class="names">SMA Solar</span> make the inverters that convert between the battery's direct current and the grid's alternating current.</dd>
<dt>The equipment that connects it either way</dt>
<dd><span class="names">Hitachi Energy</span>, <span class="names">Schneider Electric</span> and <span class="names">Eaton</span> make the transformers and switchgear a storage installation still needs.</dd>
<dt>Where I stop</dt>
<dd>I have no view on battery cell manufacturers or on the materials that go into cells. That sits in a different layer and I do not cover it here.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone forecasting grid storage demand as a function of electric vehicle adoption, since that misses the buyer described here. Developers who assumed a battery removes the need for a connection rather than bridging the wait for one.</dd>
</dl>
</section>

---

<p class="sources">Sources: United States Energy Information Administration data on planned utility-scale battery storage additions for 2026, including the national figure of 24 gigawatts and the Texas share of 12.9 gigawatts, as published in February 2026. The description of how storage is used alongside a partial connection, and of its role in smoothing fast load changes, is mechanism rather than forecast. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
