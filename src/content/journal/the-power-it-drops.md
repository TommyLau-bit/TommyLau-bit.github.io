---
title: "The grid's new problem is not the power AI uses, it is the power it drops"
date: 2026-10-08
summary: "On one day in July, 3.8 gigawatts of data centre demand in Virginia switched itself off in moments. That was the largest event of its kind in the region's history. The worry is no longer only whether the grid can supply these buildings, but what happens to everyone else when they suddenly stop drawing power."
category: "Analysis"
cover: "/covers/the-power-it-drops.svg"
tags: ["grid", "power", "data-centres"]
draft: false
---

On 22 July this year, data centres in northern Virginia tripped offline and took 3.8 gigawatts of demand off the grid.

PJM, the operator that runs the grid across Virginia and the mid-Atlantic, called it the largest event of its kind in its history.

Nobody lost power because the data centres stopped. The risk ran the other way.

Everything written about AI and electricity asks whether there is enough. That is the easy half of the question.

The hard half is what the grid does when several gigawatts of demand vanish in under a second.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture a tug of war. Two teams, pulling hard, perfectly balanced. Nobody moves because the forces cancel out.</p>
<p>Now one team lets go of the rope. The other team does not gently slow down. They fall over backwards, because all the force they were applying is suddenly pulling against nothing.</p>
<p>An electricity grid is that rope, and it is rebalanced every second of every day. Generation pulls one way, demand pulls the other. When a very large block of demand lets go at once, the generators are still pushing, and that energy has to go somewhere.</p>
</details>

## Why a computer protects itself by disappearing

A data centre is full of expensive, delicate equipment, and it is built to protect that equipment first.

When the voltage on the incoming supply dips, even briefly, the site's protection systems read it as a threat. They disconnect from the grid and switch to backup power. From the building's point of view this is exactly right. It is doing the job it was designed to do.

The trouble is the scale, and the fact that they all make the same decision at the same moment.

A voltage dip is usually caused by a fault somewhere else on the network, and faults are normal. The network is built to ride through them. What it was not built for is hundreds of megawatts, or thousands, deciding independently and simultaneously that a two-tenths-of-a-second wobble means it is time to leave.

## Why a sudden absence is harder than a sudden demand

Grid frequency is the measure of that tug of war. In most of the world it sits at 50 hertz, in North America at 60, and it only stays there while generation and demand match.

Lose a large generator and frequency falls, because demand now exceeds supply. Every operator plans for that. It is the classic failure and the whole system is designed around it.

Lose a large block of demand and frequency rises instead, because supply now exceeds demand. Voltage can spike on the local network at the same time. This is the less rehearsed direction, and until recently there was no load anywhere big enough or synchronised enough to do it at this scale.

That is what changed. A single campus can now be a thousand megawatts. It behaves less like a town and more like a power station, except that a power station is required to stay connected through a disturbance and a data centre, until now, was not.

## The rule makers have already moved

This is not a forecast. It has happened, and the response is on the record.

On 4 May 2026, NERC, the body that sets reliability rules for the North American grid, issued an Essential Actions to Industry alert titled the Level 3 Computational Load Alert. It is the only alert NERC issued in 2026.

A Level 3 is its most urgent category, and the entities it binds tell you what the concern is: transmission planners, planning coordinators, transmission owners, balancing authorities, reliability coordinators and transmission operators. That is the planning and operating spine of the grid, instructed to go and re-examine how these loads behave.

PJM has gone further and is considering interconnection requirements around what engineers call ride-through, meaning the ability to stay connected through a disturbance rather than disconnecting from it.

**The significance is not the engineering. It is the reclassification.** A data centre used to be a customer. It is becoming a piece of grid equipment with obligations, which is how generators have always been treated.

## What this does to the queue

I have argued that the binding constraint on the AI buildout is the connection queue, and that within it the transformer is the part nobody can hurry. This adds a third thing, and it is a nastier one, because it is a condition rather than a delay.

If staying connected through a fault becomes a requirement of connecting at all, then the cost of a connection now includes whatever it takes to comply. New protection settings. Possibly equipment that smooths the transition. Possibly storage on site, which was already being written into rack designs to absorb fast swings.

A queue you can wait in is a schedule problem. A standard you must meet is a design problem, and design problems are solved before the building opens, not after.

## What would prove me wrong

The obvious falsifier is that this turns out to be cheap. If ride-through compliance is mostly a matter of changing protection settings, a software and configuration exercise, then it is a footnote rather than a constraint and I am overreading it.

I would also be wrong if the Virginia event proves to be a local fault condition rather than a general property of how these sites are built. One region's wiring is not a global rule, and I am drawing a broad conclusion from a concentrated cluster.

So I watch whether PJM's requirements become firm rules rather than consultation, whether other operators outside North America follow, and whether the next comparable disturbance produces a smaller load loss than 3.8 gigawatts. A falling number would mean the industry fixed it quietly, which is the outcome I would most like to be corrected by.

<section class="exposure">
<h3>Who is exposed if load behaviour becomes a condition of connecting</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. I have no view here on the shares of any grid operator or data centre owner.</p>
<dl>
<dt>Protection and control</dt>
<dd><span class="names">Schneider Electric</span>, <span class="names">Eaton</span> and <span class="names">Hitachi Energy</span> make the switchgear, protection relays and control equipment whose settings decide when a site disconnects.</dd>
<dt>Power conditioning inside the building</dt>
<dd><span class="names">Vertiv</span> makes uninterruptible power supplies and power distribution equipment that sit between the grid and the computers.</dd>
<dt>Storage used to smooth a swing</dt>
<dd><span class="names">Fluence</span> and <span class="names">Tesla Energy</span> build grid-scale battery systems, which are increasingly specified to absorb fast changes rather than only to shift energy across the day.</dd>
<dt>The people writing the rules</dt>
<dd><span class="names">NERC</span> sets North American reliability standards and <span class="names">PJM</span> operates the grid where the July event happened.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Operators of existing sites whose protection was specified before any of this was a requirement, and who may have to retrofit. Anyone whose connection cost estimate assumes the site can behave as a passive consumer.</dd>
</dl>
</section>

---

<p class="sources">Sources: NERC's published alerts register, which lists the Essential Actions to Industry Level 3 Computational Load Alert dated 4 May 2026 and the registered entity types it binds. PJM's characterisation of the 22 July 2026 northern Virginia event as 3.8 gigawatts of load tripping offline, the largest of its kind in its history, and its consideration of ride-through requirements, as reported by Utility Dive on 12 August 2026. The description of frequency, voltage and protection behaviour is mechanism rather than forecast. Figures are as reported on the dates cited. Personal research, not investment advice.</p>
