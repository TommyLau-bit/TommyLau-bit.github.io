<a id="the-equipment-queue"></a>

Hitachi Energy, the grid business of Japan's Hitachi, is building or expanding more than 40 factories to make the heavy electrical gear that AI data centres need. At its investor day in June 2026 it told investors what it expects when they open: a pile of signed orders still worth two and a half to three years of sales.

Siemens Energy tells the same story from Germany. It has added factory space and is spending more than €2bn on more, and its grid business now carries about four years of signed work, up from three and a half when the building began.

That is the claim of this piece. The makers of transformers and switchgear are building fast enough to keep the queue, not to clear it, and on their own figures the queue will still hold years of work in 2030. A data centre's real start date is set by that queue, often before the site is chosen.

{{ANALOGY}}

## What electrical gear does an AI data centre need before it can switch on?

A chain of five or six separate machines, each from its own factory, that steps the grid's voltage down and protects every step from faults.

Power arrives at a large campus at **transmission voltage**, often 115 to 345 **kilovolts** (kV), thousands of volts. A server runs on a few dozen volts. Between the two sit the machines this piece is about.

{{FIG1}}  <!-- Between the grid and the chip sit five or six machines, each from its own factory, each with its own queue -->

First comes a **substation**, a fenced yard where the grid's line ends. In it sit high-voltage **circuit breakers**, giant switches that open within hundredths of a second on a fault, and **power transformers**, which step the voltage down to **medium voltage**. Next comes **medium-voltage switchgear**, a row of steel cabinets full of breakers that routes power to each hall. Smaller transformers then step down to **low voltage**, and inside each hall come low-voltage switchgear, a **UPS** (an uninterruptible power supply, bridging a grid fault on batteries) and **backup generators**.

The site switches on only when the last one arrives. The slowest of them, by years, is the large power transformer at the front of the chain.

## What does a transformer actually do, and why can't a data centre buy one off the shelf?

Grid power is alternating current, which reverses direction 60 times a second in America and 50 in Europe and most of Asia. A transformer changes its voltage with two copper coils on a shared steel core, and nearly every large one is designed for one site and built to order.

{{FIG2}}  <!-- A transformer is steel, copper and oil with no moving parts, and every part has its own supplier -->

The ratio of turns in the two coils sets the ratio of voltages. The US Department of Energy estimates that about 90 per cent of the electricity Americans use passes through at least one **large power transformer**, a unit rated at 100 MVA or more. An **MVA**, a megavolt-ampere, measures how much power the unit can carry; for this gear it reads close to megawatts.

A large unit is mostly steel, copper and oil, with no moving parts beyond its **tap changer**, which adjusts the ratio a little. Tall insulated plugs called **bushings** carry each conductor through the tank wall.

The department's 2012 study calls these units "custom-designed equipment", each engineered for one substation. An industry source told it that only about 1.3 units are built to each design. Utilities also buy only from makers they have **prequalified**, by auditing the factory, which the department calls "a lengthy process that can take years". So there is no shelf stock and no spot market. A campus joins the order book of a maker its utility already trusts, and waits its turn.

The wait hides three clocks. **Build time** is how long one transformer spends in the factory: months, not years. **Lead time** is how long a buyer waits from order to delivery. **Years of work** is how far ahead a maker's signed orders run at its current pace. Headlines quote the second. This piece is mostly about the third, which keeps the second long.

## Why is the steel in the core so hard to get?

Because it is a special grade, and America has one mill that makes it.

**Grain-oriented electrical steel**, or GOES, is rolled and heat-treated so its crystals line up, which makes the core waste far less power as heat. The Department of Energy's report to Congress of July 2024 names Cleveland-Cliffs as "the sole active domestic GOES supplier". On data from 2020 to 2022, that mill could meet only 12 to 20 per cent of American demand, and the highest grade comes only from Nippon Steel in Japan. About 80 per cent of GOES used in America in 2019 was imported in some form.

More is coming, slowly: on 5 October 2026 Cleveland-Cliffs announced a $200m project to lift its output by up to 25 per cent by early 2028. Even then one mill would remain a minority supplier.

## Where do the months go in the factory?

Into a few fixed stations, each needing skilled hands, a clean hall and heavy cranes, which a maker cannot multiply quickly.

The core is stacked from thousands of thin steel sheets by hand, work the department says "requires highly-skilled work force". The copper is wound around it, the assembly is dried in ovens, fitted in a clean hall and tested at high voltage. The 2012 study put the time to make one large unit at "in excess of six months". The binding constraint is not the hours but the stations: winding lines, drying ovens, crane bays and test bays. The 2024 report says capacity "cannot easily be expanded except by building a new facility".

So a transformer that leaves the factory in months can still take years from order to switch-on, and most of that time is spent waiting for a slot at the stations.

## How long is the wait, and how is it measured?

Years for a large unit, by every published measure, against months before the pandemic.

In 2010, the Department of Energy found, American makers delivered in five to 12 months from order. Its July 2024 report gives the new normal: "36-month lead times being commonly quoted and maximum lead times reaching as much as 60 months". Before the pandemic a large unit could be ordered with a lead time of less than a year.

Wood Mackenzie, an energy research firm, put power transformers at 128 weeks on average in the second quarter of 2025, a consultant's survey figure used here only as a cross-check. Smaller **distribution transformers**, which serve streets and buildings, have eased to about 30 weeks on its count. The large units, built on the scarce stations, have not followed.

## How full are the makers' order books?

Every maker of this gear that publishes a backlog has more years of work waiting than when its factory building began.

**Backlog** is the pile of signed orders not yet delivered. **Book-to-bill** is orders divided by sales in the same period; above 1, the pile is growing. **Years of work** is backlog divided by the previous four quarters' sales, my arithmetic from each filing.

{{FIG3}}  <!-- The wait is getting longer, and the new factories are still to come -->

Hitachi Energy had $66.9bn of orders waiting at 30 September 2026, about 3.1 years of its sales, up from about 2.8 in March 2025. Siemens Energy's grid business, Grid Technologies, had €51bn at 30 June 2026, about four years, up from 3.56 in September 2024. GE Vernova's grid business, Electrification, had $42.2bn of equipment backlog at 30 September 2026, 60 per cent more than a year earlier, including $5bn from Prolec GE, the transformer maker it bought outright in February 2026.

<a id="eaton-order-book-outruns-it"></a>

Eaton is the inside-the-fence test. Its Electrical Americas business sells the switchgear and power rooms between the substation and the racks. Its backlog of $16.0bn at 30 September 2026 was 1.05 years of sales, up from 0.89 at the end of 2024, though flat since June 2026, the first sign that this queue may be levelling off.

The ratios are not comparable with each other, because the grid makers also carry **HVDC** links, high-voltage direct current lines that take years to build. The direction is the point: all of them rose in the same two years the factory programmes were announced.

## Why don't the makers build enough factories to clear the queue?

Because a factory lasts decades and one AI cycle may not, and the makers have said in their own words that they will not build ahead of signed orders.

<a id="hitachi-energy-plans-the-queue"></a>

At its investor day on 10 June 2026, Hitachi showed its energy backlog growing towards about $100bn by fiscal 2030, and said it expected the backlog to "remain stable at 2.5-3x" revenue. Hitachi says it invests only in projects whose profitability is secured. ABB, the Swiss maker of switchgear and power gear, said in October 2026 its capital spending will stay "around $1 billion", with new capacity partly from "selectively leveraging third-party assembly": borrowed floor space, which can be handed back.

There are three reasons. A transformer hall runs for decades, and an AI build-out that slows in 2029 would leave it idle for most of its life. The makers also remember the last boom, from 2008 to 2011, which ended with an anti-dumping order on Korean makers. And the queue pays: a long order book lets a maker choose its orders and price them.

## When do the new factories arrive, and how much do they add?

Mostly from 2027, and greenfield plants take two to three years from announcement to first product.

{{FIG4}}  <!-- Most of the new floor space lands from 2027 on -->

The department says winding machines and core tables alone "can take 1-2 years to obtain from suppliers". Eaton's Jonesville plant in South Carolina, announced in February 2025, is due in 2027. Hitachi Energy's Gallman plant in Mississippi, announced in September 2026, is due in 2029, and it replaces the nearby Crystal Springs plant, so the net gain is the difference.

The base is small. The Commerce Department's 2020 survey found American plants could make about 343 large transformers a year, while 754 were needed in 2019. Of those, 617, or 82 per cent, were imported. America's own halls would need to double just to meet 2019's demand, before any AI campus.

## What does Siemens Energy's own chart say about the shortage?

That demand for large transformers in Europe and North America runs ahead of every maker's capacity in every year to 2030, by a narrowing margin.

<a id="siemens-energy-measures-the-shortage"></a>

At its capital market day on 20 November 2025, Siemens Energy set regional demand for large and medium power transformers against the capacity of all makers. It is the only published estimate of the gap from a maker itself.

{{FIG5}}  <!-- Siemens Energy's own forecast: the shortage narrows, but never closes -->

Demand ran about 40 per cent ahead of capacity in fiscal 2025. By fiscal 2030 the gap narrows to about 10 per cent, as capacity nearly doubles from fiscal 2023, by my reading of the chart's bars. Every year that demand exceeds output, the shortfall joins the pile.

The number the claim rests on is Siemens Energy's grid ratio: €51bn of signed, undelivered orders at 30 June 2026, divided by €12.9bn of Grid Technologies revenue over the previous four quarters. The backlog is rounded to the nearest billion, so the true ratio lies between 3.92 and 4.00; the claim records it as 3.96. It is not a quoted lead time, because the HVDC links lift it, so the direction matters more than the level.

The trap is that the ratio can fall while the pile grows. Siemens Energy's grid revenue is growing about 25 per cent a year on its own guidance. At that pace the ratio holds only if orders run about 1.8 times sales; at the third quarter's 1.48 it would fall to about 3.4 by mid-2028, while each year's shortfall still joins the pile.

## Where do America's large transformers come from?

Mostly from abroad, and increasingly from Korea, while China supplies little.

{{FIG6}}  <!-- America's imports of large transformers more than tripled in three years, and China supplies little -->

United Nations trade data show American imports of liquid-filled transformers above 10 MVA rising from $1.26bn in 2022 to $4.15bn in 2025, 3.3 times in three years. Mexico was the largest supplier in 2025, at 19 per cent, and Korea's share rose from 7 to 18 per cent. China supplied 2.2 per cent by value in 2025. The average unit imported in 2025 cost about $0.83m, so this customs line is dominated by mid-sized units, not only the very largest.

The queue in America is filled by imports from makers who also serve their home grids, so a boom in Europe or Asia can lengthen the American wait. The new American halls replace imports as much as they add supply.

## What do tariffs and the emergency order change?

They raise the cost of the steel and parts more than the finished unit, and they let the government shut out some foreign gear, which together tilt the queue toward a few makers.

{{FIG7}}  <!-- Until 2028 the finished transformer is taxed less than the steel it is made from -->

Under America's **Section 232** tariffs, imposed on national security grounds, large power transformers pay 15 per cent until 31 December 2027, then 25 per cent. The GOES strip itself, and copper wire, pay 50 per cent. So until the end of 2027 a finished unit pays a third as much as the steel it is built from. That favours importing whole units, or ready-made cores, over making cores from imported steel in a new American hall, and the rate on the finished unit rises just as the first new halls open.

On 26 August 2026 the President signed Executive Order 14421, declaring a national emergency over the **bulk-power system**, the high-voltage network. It lets the Department of Energy bar foreign-produced equipment, including transformers, breakers, UPS systems and backup generators, where it finds a link to a covered foreign entity and an undue risk. It is not a blanket ban, and no rule had been published by 7 November.

## What are prices doing?

Rising again, faster than in 2023 and 2024, which is not what a market where the shortage is easing looks like.

{{FIG8}}  <!-- Prices jumped in 2022, slowed, and are rising faster again -->

The Bureau of Labor Statistics' producer price index for transformer makers averaged 255.3 in 2020. By September 2026 it was 475.1, 86 per cent higher, preliminary for the latest month. Prices jumped 34 per cent in 2021 and 18 per cent in 2022, then rose only about 4 per cent in 2023 and 2 per cent in 2024. In 2025 they rose 5 per cent, and in the year to September 2026 nearly 8 per cent. If the shortage were clearing, the index would flatten or fall. It has done the opposite.

## Does the gear inside the fence queue too?

Yes, by a year or two rather than three or four, and the makers say so in their own words about when 2026's orders will ship.

{{FIG9}}  <!-- Inside the fence, this year's orders ship in one to three years -->

ABB told analysts in October 2026 that its data centre gear has lead times of 12 to 24 months, so this year's orders ship in 2027 and 2028. Schneider Electric, the French maker of power and cooling gear, says its record backlog gives "visibility into 2027 and 2028". Generators queue longest: Caterpillar told analysts it is accepting some large engine orders into 2029 and turbine orders into 2030.

<a id="schneider-sells-the-finished-system"></a>

Schneider also sells power rooms built in its own plants as modules. Prefabrication shortens the install, not the order book: the modules still need gear from the same queues.

AI racks change the low-voltage end far more than the grid end. A rack of Nvidia's GB200 chips draws up to 132 kilowatts, about fifteen times the typical rack's almost 9, and Nvidia plans racks of a megawatt from 2027, as [Powering the rack](/journal/powering-the-rack/) explains.

{{FIG10}}  <!-- An AI rack draws fifteen times the power of an average one, and Nvidia plans over a hundred times -->

A 100 MW campus needs the same substation, medium-voltage switchgear and generators whether it runs 11,000 racks at 9 kilowatts or 760 at 132. What changes is the gear nearest the rack: busways, power shelves and, from 2027, rectifiers and new direct-current breakers. That reshuffles the low-voltage order book; it does not shorten the grid-side queue.

## Will the parts be the next queue?

Possibly: some bushings now wait longer than a whole transformer did before the pandemic, though other parts are flowing freely.

<a id="the-parts-list"></a>

A transformer ships only when its slowest part arrives. Hitachi Energy publishes delivery times for the components it sells to other transformer makers. On 29 October 2026 it gave 135 weeks for its GSBK and ARF high-voltage bushings from Ludvika, Sweden; in 2012 the Department of Energy heard such bushings took up to five months. Tap changers, another bought-in part, are quoted at 10 to 22 weeks from Ludvika, so the strain is not everywhere.

{{FIG11}}  <!-- A high-voltage bushing from Sweden now waits longer than a whole transformer did in 2010 -->

Two moves fit the reading that parts are binding. On 28 October 2026 GE Vernova agreed to pay about $9.0bn for Trench, which makes bushings, and called it "vertically integrating an existing supplier". And Hitachi Energy is spending $106m at Alamo, Tennessee, on what it calls the "largest bushings manufacturing facility in North America". The inference is mine, and it is a hypothesis: if parts gate output, a new hall adds floor space before it adds transformers. Swedish bushing waits falling below a year would kill it.

## Has the shortage peaked?

The rate of increase probably has, but every order book is still growing, and a narrower gap still adds to the pile.

The case for a peak is real. Siemens Energy's grid book-to-bill fell to 1.48 in the quarter to June 2026, from 2.28 in the quarter before. Eaton's Electrical Americas ratio went flat. Wood Mackenzie's estimate of the power transformer shortage fell from 30 per cent for 2025 to 15 per cent for 2026.

The case against is stronger. Every book-to-bill is still above 1, so every pile is still growing. GE Vernova's grid equipment backlog is up 60 per cent in a year, or about 40 per cent without the Prolec GE purchase. Transformer prices are rising faster than in 2023 and 2024. A real peak shows up as price cuts and idle halls. Neither is visible yet.

Spares do not change this. Installing a ready spare takes three to four weeks, but spares exist to replace a failed unit at an existing substation, not to serve new load.

## So who holds the scarce thing, and what should an investor watch?

Whoever owns the slowest station: the large transformer halls, the steel, and a few parts.

If the queue is kept, three positions gain. **The grid makers**: Hitachi Energy, Siemens Energy and GE Vernova, with HD Hyundai Electric, Hyosung and LS Electric from Korea, hold years of signed work and the choice of which orders to take. **The inside-the-fence makers**: Eaton, Schneider Electric, ABB, Siemens, Vertiv, Legrand, nVent, Hubbell and Powell make switchgear, UPS systems and power rooms, with a shorter queue. Caterpillar, Cummins, Generac and Rolls-Royce make the backup generators. **The parts behind the parts**: bushings, tap changers and core steel come from a few suppliers.

Four numbers carry the story. Siemens Energy's grid ratio and Eaton's Electrical Americas ratio each quarter, which are the claim's tests. Book-to-bill at the grid makers, which shows whether the pile is still growing. And Hitachi Energy's component delivery page, which shows whether the parts are easing.

A utility can clear a site's place in the grid queue, as in [America rations the plug](/journal/america-rations-the-plug/), and the site still waits for its transformer. Nvidia launches a new flagship chip about every year, and a transformer ordered today joins a pile that would take three or four of those generations to clear. So a data centre's real start date is set years before the chips it will run are on sale.

## What would prove me wrong

Three tests can break the claim. The first is the ratio drifting down. If by 30 June 2028 Siemens Energy's grid order book has fallen below 3.6 years of its sales, or Eaton's Electrical Americas below one year, the first wave of new plants has shortened the queue and the claim fails. This test is closer than it looks: Siemens Energy's grid sales grow about 25 per cent a year, so at the third quarter's book-to-bill of 1.48 the ratio would reach about 3.4 by mid-2028. Orders must run about 1.8 times sales to hold it, and Eaton's ratio has already gone flat.

The second is orders cooling as the plants open. If book-to-bill falls below 1 at the grid makers just as the 2027 halls start, the makers built into a slowdown. For now Siemens Energy's grid business is at 1.48 and GE Vernova's at about 1.4.

The third is someone breaking ranks. If makers outside this group, in Korea, Brazil or China, add capacity to clear the queue and American buyers accept their units, it empties faster. The Korean makers are adding capacity in Alabama and Tennessee; if they build ahead of orders, the wait shortens.

The claim stands on two legs. The first is time: halls take two to three years, and steel, ovens and test bays cap output, but that expires as the halls land from 2027. The second is choice: the makers size halls to signed orders, a business decision they can drop. The wait in 2030 rests on the second leg. Two things would not move me. More factory announcements: they are the headline, not the order book. And price rises: they show the queue holding, not clearing.
