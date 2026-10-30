---
title: "The grid's new problem is not the power AI uses, it is the power it drops"
date: 2026-09-22T18:53:00+08:00
summary: "On one day in July, 3.8 gigawatts of data centre demand in Virginia switched itself off in moments. That was the largest event of its kind in the region's history. The worry is no longer only whether the grid can supply these buildings, but what happens to everyone else when they suddenly stop drawing power."
category: "Analysis"
cover: "/covers/the-power-it-drops.svg"
tags: ["grid", "power", "data-centres"]
draft: false
---

On 22 July this year, data centres in northern Virginia tripped offline and took 3.8 gigawatts of demand off the grid. PJM, the operator that runs the grid across Virginia and the mid-Atlantic, called it the largest event of its kind in its history.

Nobody lost power because the data centres stopped. The risk ran the other way.

Everything written about AI and electricity asks whether there is enough. That is the easy half of the question.

The hard half is what the grid does when gigawatts of demand vanish in under a second.

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Picture a tug of war, two teams pulling hard and perfectly balanced. Now one team lets go of the rope. The other does not slow gently. It falls over backwards, because all its force is suddenly pulling against nothing.</p>
<p>An electricity grid is that rope, rebalanced every second. Generation pulls one way and demand the other. When a large block of demand lets go at once, the generators are still pushing.</p>
</details>

## Why a computer protects itself by disappearing

A data centre is built to protect its expensive, delicate equipment first. When the voltage on its supply dips, even briefly, its protection systems read a threat. They disconnect from the grid and switch to backup power. From the building's point of view, this is exactly right.

The trouble is scale, and every site making the same decision at the same moment. A dip usually comes from a fault elsewhere, and the network is built to ride through faults. It was not built for thousands of megawatts deciding together that a two-tenths-of-a-second wobble means leave.

Grid frequency measures the tug of war. In North America it sits at 60 hertz, and only while generation and demand match. Lose a large generator and frequency falls, the classic failure every operator plans for. Lose a large block of demand and frequency rises instead, the less rehearsed direction.

A single campus can now be a thousand megawatts. It behaves like a power station, except that a power station must stay connected through a disturbance and a data centre, until now, did not.

## The rule makers have already moved

On 4 May 2026, NERC, the body that sets reliability rules for the North American grid, issued its Level 3 Computational Load Alert. Level 3 is its most urgent category, and it binds the planners and operators who form the spine of the grid.

PJM is considering requirements for ride-through, the ability to stay connected through a disturbance rather than drop off.

The significance is the reclassification. A data centre used to be a customer. It is becoming grid equipment with obligations, and a standard you must meet is a design problem, solved before the building opens.

## What would prove me wrong

The obvious falsifier is that this turns out to be cheap. If ride-through is mostly a change of protection settings, it is a footnote rather than a constraint.

I am also wrong if the Virginia event proves to be a local fault rather than how these sites are built. One region's wiring is not a global rule. A comparable disturbance that drops far less than 3.8 gigawatts would mean the industry fixed it quietly.

<section class="exposure">
<h3>Who is exposed if load behaviour becomes a condition of connecting</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. I have no view here on the shares of any grid operator or data centre owner.</p>
<dl>
<dt>Protection and power inside the site</dt>
<dd><span class="names">Schneider Electric</span>, <span class="names">Eaton</span> and <span class="names">Hitachi Energy</span> make switchgear and protection relays. <span class="names">Vertiv</span> makes uninterruptible power supplies.</dd>
<dt>Storage used to smooth a swing</dt>
<dd><span class="names">Fluence</span> and <span class="names">Tesla Energy</span> build grid-scale battery systems.</dd>
<dt>The people writing the rules</dt>
<dd><span class="names">NERC</span> sets North American reliability standards and <span class="names">PJM</span> operates the grid where the July event happened.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Existing sites whose protection was specified before any of this, and anyone whose connection cost assumes the site can behave as a passive consumer.</dd>
</dl>
</section>

---

<p class="sources">Sources: NERC's alerts register for the Level 3 Computational Load Alert of 4 May 2026, and PJM's account of the 22 July 2026 event and its ride-through work, as reported by Utility Dive on 12 August 2026. Personal research, not investment advice.</p>
