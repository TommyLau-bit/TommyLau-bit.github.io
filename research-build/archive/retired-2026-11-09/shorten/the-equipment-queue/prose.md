<a id="the-equipment-queue"></a>

Hitachi Energy, the grid business of Japan's Hitachi, is building or expanding more than 40 factories to make the heavy electrical gear that AI data centres need. At its investor day in June 2026 it told investors what it expects when they open: a pile of signed orders still worth two and a half to three years of sales.

Siemens Energy tells the same story from Germany. It has added factory space and is spending more than €2bn on more, and its grid business now carries about four years of signed work, up from three and a half when the building began.

That is the claim of this piece. The makers of transformers and switchgear are building fast enough to keep the queue, not to clear it, and on their own figures the queue will still hold years of work in 2030. A data centre's real start date is set by that queue, often before the site is chosen.

To see why, the piece follows the questions in order. What gear a data centre needs between the grid and the chip, and what a transformer actually does. Why it cannot be bought off the shelf, why its steel is scarce, and where the months go in the factory. How long the wait is, how full the makers' order books are, and why they will not build enough to clear them. Then where America's transformers come from, what tariffs and an emergency order change, and what prices are doing. Then the gear inside the fence, what AI racks change, and whether the parts are the next queue. Finally, whether the shortage has peaked, why spares do not solve it, who holds the scarce thing, and what would prove me wrong.

{{ANALOGY}}

## What electrical gear does an AI data centre need before it can switch on?

A chain of five or six separate machines, each from its own factory, that steps the grid's voltage down and protects every step from faults.

Power arrives at a large campus at **transmission voltage**, often 115,000 to 345,000 volts, written 115 to 345 **kilovolts** (kV). A **volt** is the electrical pressure that pushes current along a wire, and those are the pressures of the long-distance lines that cross a country. A server runs on a few dozen volts. Between the two sit the machines this piece is about.

{{FIG1}}  <!-- Between the grid and the chip sit five or six machines, each from its own factory, each with its own queue -->

The first is a **substation**: a fenced yard where the grid's line ends at the campus. In it sit high-voltage **circuit breakers**, giant switches that open in a few hundredths of a second if a fault occurs, and one or more **power transformers**, which step the voltage down to **medium voltage**, in America usually 13,800 or 34,500 volts.

Next comes **medium-voltage switchgear**: a row of steel cabinets full of breakers, the campus's main fuse board, which routes power to each data hall and cuts off any branch that fails. Smaller transformers then step the voltage down again to **low voltage**, usually 480 volts in America.

Inside each hall, **low-voltage switchgear** divides that power again. A **UPS**, an uninterruptible power supply, uses batteries to bridge the seconds between a grid fault and the **backup generators** starting; those are diesel or gas engines that can carry the site for days. Last come the busbars and power distribution units that carry current along the rows and into each rack.

Each box is a separate product, from a separate factory, with its own waiting list. The site switches on only when the last one arrives. The slowest of them, by years, is the large power transformer at the front of the chain, so the piece starts there.

## What does a transformer actually do?

It changes the voltage of alternating current, using two coils of copper wound on a shared core of special steel, with no moving parts.

{{FIG2}}  <!-- A transformer is steel, copper and oil with no moving parts, and every part has its own supplier -->

Grid power is **alternating current**: it reverses direction 60 times a second in America and 50 in Europe and most of Asia. Feed that current into one coil, and it makes a magnetic field in the steel core that swings back and forth with it. That swinging field passes through the second coil and makes a current flow in it.

The trick is in the turns. If the second coil has a tenth as many turns of wire as the first, its voltage is a tenth as high. So a transformer is a lever for voltage: the ratio of turns sets the ratio of voltages, and the core carries the force between them.

Why bother? Because a wire wastes power as heat, and the waste rises with the square of the current. For the same power, double the voltage and the current halves, so the heat lost falls to a quarter. That is why power stations step up to very high voltage for the long lines, and why substations step it down again for use.

The US Department of Energy estimates that about 90 per cent of the electricity Americans use passes through at least one **large power transformer**, which it defines as a unit rated at 100 MVA or more. An **MVA**, a megavolt-ampere, measures how much power the unit can carry, like the bore of a pipe. A data centre's load is stated in **megawatts**, the water that actually flows; for this gear the two are close enough to read together.

A large unit is mostly steel, copper and oil. The core alone holds 80 to 120 tonnes of steel in a unit of 300 to 500 MVA, the department found in 2012. The windings sit around it, wrapped in paper insulation. Both stand in a steel tank of insulating oil, which carries heat out to radiators and fans.

Two more parts matter later. **Bushings** are the tall insulated plugs that carry each conductor through the tank wall to the line outside. A **tap changer** switches between points on the winding, adjusting the ratio a little to hold voltage steady as load changes. Nothing else moves, so a transformer can run for 40 years or more.

## Why can't a data centre buy one off the shelf?

Because nearly every large transformer is designed for one site, by a maker the buyer has approved in advance, and is built to order.

The Department of Energy's 2012 study of large power transformers calls them "custom-designed equipment". Each is engineered for one substation's voltages, rating, space and route to site. An industry source told the department that only about 1.3 units are built to each design, so almost every unit is its own drawing.

Buyers also limit whom they buy from. Utilities purchase only from makers they have **prequalified**, which means auditing the factory, its quality system and its test results. The department calls that "a lengthy process that can take years". A new maker, or a new factory, cannot simply start selling to a utility the day it opens.

So there is no shelf stock to buy, and no spot market. A campus that needs a transformer joins the order book of a maker its utility already trusts, and waits its turn there.

The wait hides three clocks, and they are easily confused. **Build time** is how long one transformer spends in the factory: months, not years. **Lead time** is how long a buyer waits from order to delivery. **Years of work** is how far ahead a maker's signed orders run at its current pace. Headlines quote the second. This piece is mostly about the third, which keeps the second long.

## Why is the steel in the core so hard to get?

Because it is a special grade, rolled so its crystals line up, and America has one mill that makes it.

Ordinary steel is a jumble of tiny crystals pointing every way, so a magnetic field loses energy turning them back and forth. **Grain-oriented electrical steel**, or GOES, is rolled and heat-treated so the crystals line up along the strip. Magnetic flux then runs easily one way, and the core wastes far less power as heat. The best grades have their surface scored by laser to cut the loss further.

In America one company makes it. The Department of Energy's report to Congress of July 2024 names Cleveland-Cliffs, through the AK Steel business it bought in 2020, as "the sole active domestic GOES supplier". Using data from 2020 to 2022, it said that mill could meet only 12 to 20 per cent of American demand. The highest grade, it added, comes only from Nippon Steel in Japan.

The rest is imported, in some form. The department found that about 80 per cent of GOES used in America in 2019 was imported, counting the cut strips, the stacked cores and the steel inside finished transformers. It called the domestic supply "a major weak link" in the chain.

The steel also matters for cost. The same report, citing a 2020 Commerce Department survey, says the steel and the copper windings "each account for roughly 25 percent" of the cost of making a large transformer. When either price jumps, the maker's margin on an order priced months earlier takes the hit.

More is coming, slowly. On 5 October 2026 Cleveland-Cliffs announced a $200m project at its Butler Works mill in Pennsylvania to lift its output by up to 25 per cent by early 2028, backed by a $75m Department of Energy award. Even then, on the department's 2020 to 2022 figures, one mill would remain a minority supplier.

## Where do the months go in the factory?

Into a few fixed stations, each needing skilled hands, a clean hall and heavy cranes, which a maker cannot multiply quickly.

The Department of Energy lists seven steps. Engineering and design come first. Then the core is built, stacking thousands of thin steel sheets by hand, work the department says "requires highly-skilled work force". The copper is wound and fitted around it, and the whole assembly is dried in ovens, because moisture ruins the paper insulation.

The tank is made so that it is ready just as the dried assembly is, before it soaks up damp again. Final assembly happens in a clean hall: "even a tiny amount of dust or moisture can deteriorate the performance", the department found. Then every unit is tested at high voltage before it ships.

The department's 2012 study put the time to make one large unit at "in excess of six months". That is build time. The binding constraint is not the hours but the stations: winding lines, drying ovens, crane bays and test bays. Its 2024 report puts it plainly: capacity "cannot easily be expanded except by building a new facility".

Moving the finished unit is a project of its own. A large transformer weighs about 100 to 400 tons, while most railcars carry about 100. The heaviest ride on **Schnabel cars**, special railcars, some with 20 axles or more, that cradle the load between two arms. The department counted about 30 in North America in 2012, and its 2024 report says only about three of the largest kind are available. Clearing a route can take nine months, it says.

To travel at all, the unit is drained of oil and stripped of its bushings and radiators. On site it is rebuilt, filled, dried under vacuum and tested again. So a transformer that leaves the factory in months can still take years from order to switch-on, and most of that time is spent waiting for a slot at the stations.

## How long is the wait, and how is it measured?

Years for a large unit, by every published measure, against months before the pandemic.

No maker publishes a list price or lead time for a complete large transformer, so the wait has to be pieced together. The oldest dated benchmark is the Department of Energy's: in 2010, American makers delivered in five to 12 months from order, and foreign makers in six to 16.

The department's July 2024 report gives the new normal: "36-month lead times being commonly quoted and maximum lead times reaching as much as 60 months". Before the pandemic, it notes, a large unit could be ordered with a lead time of less than a year. Siemens Energy itself, announcing its first American transformer plant in February 2024, cited waits of "up to five years".

Consultants give quarterly averages. Wood Mackenzie, an energy research firm, put power transformers at 128 weeks on average in the second quarter of 2025, about two and a half years. Those are a consultant's survey figures, not a regulator's, and the piece uses them only as a cross-check.

Smaller units have eased. The National Renewable Energy Laboratory reported in February 2024 that **distribution transformers**, the smaller units on poles and pads that serve streets and buildings, were taking up to two years. By the second quarter of 2025 Wood Mackenzie put them at about 30 weeks. The large units, built on the scarce stations, have not followed.

## How full are the makers' order books?

Every maker of this gear that publishes a backlog has more years of work waiting than when its factory building began.

**Backlog** is the pile of signed orders not yet delivered: the hairdresser's diary. **Book-to-bill** is orders in a period divided by sales in the same period; above 1, the diary is growing. **Years of work** is backlog divided by the same business's sales over the previous four quarters. It is my arithmetic from each filing, and it measures how long the factories would take to clear the pile if no new order came.

{{FIG3}}  <!-- The wait is getting longer, and the new factories are still to come -->

Hitachi Energy had $66.9bn of orders waiting at 30 September 2026, about 3.1 years of its sales, up from about 2.8 in March 2025. Siemens Energy's grid business, Grid Technologies, had €51bn at 30 June 2026, about four years. It was 3.56 in September 2024. GE Vernova's grid business, Electrification, had $42.2bn of equipment backlog at 30 September 2026, 60 per cent more than a year earlier, including $5bn from Prolec GE, the transformer maker it bought outright in February 2026.

<a id="eaton-order-book-outruns-it"></a>

Eaton is the inside-the-fence test. Its Electrical Americas business sells the switchgear, power rooms and distribution gear that sit between the substation and the racks. Its backlog of $16.0bn at 30 September 2026 was 1.05 years of sales, up from 0.93 in June 2025 and 0.89 at the end of 2024. Organic orders over the previous twelve months were up 39 per cent.

The ratios are not comparable with each other, and the direction is the point. The two grid makers carry **HVDC** links, high-voltage direct current lines that take years to build and pad their order books. Eaton's gear mostly ships within a year: 72 per cent of its whole company backlog is due for delivery within twelve months, its September 2026 filing says. What matters is that all of them rose in the same two years the factory programmes were announced.

Eaton's ratio has since stopped rising: 1.049 in June 2026 and 1.050 in September. I return to that below, because it is the first sign that the inside-the-fence queue may be levelling off.

## Why don't the makers build enough factories to clear the queue?

Because a factory lasts decades and one AI cycle may not, and the makers have said in their own words that they will not build ahead of signed orders.

<a id="hitachi-energy-plans-the-queue"></a>

At its investor day on 10 June 2026, Hitachi showed its energy backlog growing towards about $100bn by fiscal 2030, and said it expected the backlog to "remain stable at 2.5-3x" revenue. Hitachi says it invests only in projects whose profitability is secured. It plans more than $6bn of factory spending from 2024 to 2027, double the previous four years, and its American programme alone is now around $1.5bn.

ABB, the Swiss maker of switchgear and power gear inside the fence, said the same thing differently in October 2026. Its capital spending will stay "around $1 billion" and it does "not expect it to rise further in the mid-term". New capacity will come partly by "selectively leveraging third-party assembly": borrowed floor space, which can be handed back.

The first reason is the life of the asset. A transformer hall runs for decades. An AI build-out that slows in 2029 would leave a hall built to clear the 2026 queue standing idle for most of its life. Sizing to signed orders, not to the wait, protects the return on every dollar spent.

The second is memory. Over the preceding decades, the Department of Energy recorded in 2012, transformer makers consolidated "to remove excess capacity and move their operations offshore". The last boom, from 2008 to 2011, ended with Korean makers accused of selling below American prices and an anti-dumping order that is still in force. Every maker in this piece remembers what too many halls did to prices.

The third is that the queue pays. A long order book lets a maker choose its orders and price them. It carries a risk: Eaton's Electrical Americas margin fell to 27.5 per cent in the second quarter of 2026, as higher metal costs met orders priced months earlier. In the third quarter it recovered to 29.8 per cent, half a point below the 30.3 per cent of a year earlier.

## When do the new factories arrive, and how much do they add?

Mostly from 2027, and greenfield plants take two to three years from announcement to first product.

{{FIG4}}  <!-- Most of the new floor space lands from 2027 on -->

The Department of Energy's 2024 report says a new factory takes one to three years to build, and that winding machines and core tables alone "can take 1-2 years to obtain from suppliers". The dated plants bear that out. Eaton's Jonesville transformer plant in South Carolina, announced in February 2025, is due in 2027. Hitachi Energy's Gallman plant in Mississippi, announced in September 2026, is due in 2029.

Expansions on an existing site are faster. HD Hyundai Electric broke ground on a second plant at Montgomery, Alabama, in March 2026 and expects to finish it in April 2027. Virginia Transformer expects its Rincon, Georgia, expansion in March 2027, about sixteen months after it was announced. Both are company statements, and both add to sites that already have qualified lines and trained staff.

Some plants slip. Siemens Energy announced its Charlotte, North Carolina, plant on 14 February 2024 for production in early 2026. Reuters reported on 26 June 2025 that a Siemens Energy board member now expected the first transformers in early 2027. No company release I could find confirms a start.

How much do they add? The base is small. The Commerce Department's 2020 survey, cited by the Department of Energy, found that American plants could make about 343 large transformers a year, while 754 were needed in 2019. Of those, 617, or 82 per cent, were imported. So America's own halls would need to double just to meet 2019's demand, before any AI campus.

Not every announcement is new capacity either. Hitachi Energy's Gallman plant replaces its nearby Crystal Springs plant, whose production moves there; it will be more than twice the size of the old plant, Hitachi says, so the net gain is the difference.

## What does Siemens Energy's own chart say about the shortage?

That demand for large transformers in Europe and North America runs ahead of every maker's capacity in every year to 2030, by a narrowing margin.

<a id="siemens-energy-measures-the-shortage"></a>

At its capital market day on 20 November 2025, Siemens Energy set demand for large and medium power transformers in Europe and North America against the capacity of all makers in the region. It is the only published estimate of the gap from a maker itself.

{{FIG5}}  <!-- Siemens Energy's own forecast: the shortage narrows, but never closes -->

Demand ran about 40 per cent ahead of capacity in fiscal 2025. By fiscal 2030 the gap narrows to about 10 per cent, as capacity nearly doubles from fiscal 2023, by my reading of the chart's bars. A smaller gap is still a gap: every year that demand exceeds output, the shortfall joins the pile.

The number the claim rests on is Siemens Energy's grid ratio, about four years: €51bn of signed, undelivered orders at 30 June 2026, divided by €12.9bn of Grid Technologies revenue over the previous four quarters. The backlog is rounded to the nearest billion, so the true ratio lies between 3.92 and 4.00. The claim records it as 3.96.

It is not a quoted lead time. A new order can be slotted ahead of HVDC work shipping in 2030, and the HVDC links lift the ratio above what a transformer buyer faces. That is why the direction matters more than the level.

The trap is that the ratio can fall while the pile grows. If orders run 10 per cent above output, and output grows 6 per cent a year, the ratio drifts from about four to about 3.8, then about 3.7, while each year's shortfall still joins the pile. The real test is harder. Siemens Energy's grid revenue is growing about 25 per cent a year on its own guidance. At that pace the ratio holds only if orders run about 1.8 times sales; at the third quarter's 1.48 it would fall to about 3.4 by mid-2028. Price rises, early bookings and currency moves can lift the ratio too, and no maker splits its backlog into price and volume.

## Where do America's large transformers come from?

Mostly from abroad, and increasingly from Korea, while China supplies little.

{{FIG6}}  <!-- America's imports of large transformers more than tripled in three years, and China supplies little -->

United Nations trade data, which carry the American customs figures, show imports of the largest class of liquid-filled transformers, those above 10 MVA, rising from $1.26bn in 2022 to $4.15bn in 2025. That is 3.3 times in three years. In the first eight months of 2026 they grew more slowly, about 10 per cent on the same months of 2025.

Mexico was the largest supplier in 2025, at 19 per cent, though its share has fallen from 31 per cent in 2022. Korea's rose from 7 to 18 per cent, then Brazil, Austria, the Netherlands, Taiwan and Canada. Korea's own customs data show its exports of these units to America rising 6.8 times from 2022 to 2025, to 57 per cent of all its exports of them.

China is small in this trade: 2.2 per cent of American imports by value in 2025, and 4.7 per cent in the first eight months of 2026. The average unit imported in 2025 cost about $0.83m, so this customs line is dominated by mid-sized units, not only the very largest.

The pattern matters for the claim. The queue in America is filled by imports from makers who also serve their home grids, so a boom in Europe or Asia can lengthen the American wait. And the new American halls are replacing imports as much as adding supply.

## What do tariffs and the emergency order change?

They raise the cost of the steel and parts more than the finished unit, and they let the government shut out some foreign gear, which together tilt the queue toward a few makers.

{{FIG7}}  <!-- Until 2028 the finished transformer is taxed less than the steel it is made from -->

America's **Section 232** tariffs, imposed on national security grounds, now reach transformers. From 18 August 2025 large transformers and their cores paid 50 per cent on their steel content. Proclamation 11021, in force from 6 April 2026, changed the basis to the full value of the goods and set new rates.

Large power transformers now pay 15 per cent, until 31 December 2027, when the rate rises to 25 per cent. Distribution transformers up to 10 MVA pay 25 per cent, and so do the cores and laminations a maker might import to build its own. The GOES strip itself, and copper wire, pay 50 per cent.

The order of those rates is odd. Until the end of 2027 a finished large transformer pays 15 per cent, a third as much as the GOES strip it is built from. Since 8 June, cores imported to build these transformers in America can also pay 15 per cent, but the strip itself pays 50. That favours importing whole units, or ready-made cores, over making cores from imported steel in a new American hall. The rate on the finished unit then rises, just as the first new halls open.

An older remedy is still in place. The anti-dumping order on Korean large transformers, issued in 2012 after the last boom, was continued in 2024. Its latest final results, published on 14 August 2026, set rates of zero for HD Hyundai Electric and Iljin, and 4.32 per cent for LS Electric and Hyosung Heavy Industries.

Then came the emergency order. On 26 August 2026 the President signed Executive Order 14421, declaring a national emergency over the **bulk-power system**, the high-voltage network of generation and transmission. It lets the Department of Energy bar foreign-produced equipment, including substation transformers, high-voltage breakers, and even UPS systems and backup generators that support critical infrastructure, in transactions begun after that date. The bar applies where the department finds a link to a covered foreign entity and an undue risk.

So it is not a blanket ban. The order gave the department 120 days to write any rules it needs, so by 24 December 2026; its request for comments closed on 9 October, and no rule had been published by 7 November. Earlier, on 20 April 2026, a presidential determination under the Defense Production Act named transformers, high-voltage breakers and "electrical core steel" essential to national defence.

What the order changes is the fast lane for some buyers. Wood Mackenzie expects much of its impact to fall on data centres that bought Chinese units to cut their wait. China's share of imports was small, so the larger effect may be on parts and on the other gear the order names, and on the confidence of buyers who had a second source in mind.

## What are prices doing?

Rising again, faster than in 2023 and 2024, which is not what a market where the shortage is easing looks like.

{{FIG8}}  <!-- Prices jumped in 2022, slowed, and are rising faster again -->

The Bureau of Labor Statistics' producer price index for transformer makers, which tracks the prices they charge, averaged 255.3 in 2020. By September 2026 it was 475.1, 86 per cent higher. The switchgear makers' index rose 88 per cent over the same span. Both are preliminary for the latest month.

The timing tells the story. Transformer prices jumped 34 per cent in 2021 and 18 per cent in 2022, then rose only about 4 per cent in 2023 and 2 per cent in 2024. In 2025 they rose 5 per cent, and in the year to September 2026 nearly 8 per cent. Switchgear prices rose 12 per cent in each of the last two years.

Part of that is metal. The International Monetary Fund's copper price was $14,473 a tonne in September 2026, 2.3 times its 2020 average, and the 2025 and 2026 tariffs raised the cost of imported steel and wire. Part of it is the queue: makers with years of work can pass costs on and choose which orders to take.

For the claim, prices are a check, not a test. If the shortage were clearing, the price index would flatten or fall, as it did for distribution transformers' lead times. It has done the opposite.

## Does the gear inside the fence queue too?

Yes, by a year or two rather than three or four, and the makers say so in their own words about when 2026's orders will ship.

{{FIG9}}  <!-- Inside the fence, this year's orders ship in one to three years -->

The inside-the-fence makers publish few lead times, but they say when orders will ship. ABB told analysts in October 2026 that its data centre gear has lead times of 12 to 24 months, so this year's orders ship in 2027 and 2028. Schneider Electric, the French maker of power and cooling gear, says its record backlog gives "visibility into 2027 and 2028".

Generators queue longest. Generac reported a data centre backlog of about $4.5bn in October 2026, and an agreement with Amazon whose "initial deliveries are expected to total a combined $2.4 billion in 2027 and 2028". Caterpillar told analysts it is accepting some large engine orders into 2029 and turbine orders into 2030. Cummins said in August 2026 that its growth was "constrained by available capacity for larger generator-set configurations".

Smaller makers show the strain in their ratios. Powell Industries, which builds switchgear and power rooms in Texas, booked a record $934m of orders in the quarter to June 2026, three times its sales, including one data centre order above $400m. Vertiv, which makes UPS, power and cooling gear, reported orders up more than 100 per cent in its third quarter, but no longer publishes its backlog each quarter.

<a id="schneider-sells-the-finished-system"></a>

One answer to the queue is to build more of the room in the factory. Schneider sells power rooms built and tested in its own plants, delivered as modules, which cut the hours that scarce electricians must spend on site. Data centres were about a quarter of its revenue by the end of 2025, in its own words, and it sizes its content at $1.2m to $3.3m for each megawatt of new data centre.

Prefabrication shortens the install, not the order book. The modules still need breakers, transformers and switchgear from the same queues, and Schneider publishes no backlog figure to test. Eaton has bought its way into the same idea, with Fibrebond, a maker of modular power enclosures, in 2025.

## What do AI racks change about the gear?

They concentrate power into far fewer racks, which changes the low-voltage end of the chain far more than the grid end.

{{FIG10}}  <!-- An AI rack draws fifteen times the power of an average one, and Nvidia plans over a hundred times -->

The Uptime Institute's 2025 survey found the typical rack density reported by operators averaged almost 9 kilowatts. A rack of Nvidia's GB200 chips draws up to 132 kilowatts, about fifteen times as much. Nvidia has said it will support racks of a megawatt from 2027.

The physics is current. Current is power divided by voltage, so a megawatt rack fed at 54 volts would draw about 18,500 amps, my arithmetic, and Nvidia says it would need up to 200 kilograms of copper busbar. Fed at 800 volts it draws about 1,250 amps. Nvidia's 2025 plan was to convert medium-voltage power to 800 volts of direct current at the edge of the hall. It now offers 800 volts as an option beside today's alternating current, arriving first in a cabinet beside the rack, as [Powering the rack](/journal/powering-the-rack/) explains.

For the equipment queue the point is narrower. A 100 MW campus needs the same substation, the same medium-voltage switchgear and the same generators whether it runs 11,000 racks at 9 kilowatts or 760 at 132. What changes is the gear nearest the rack: busways, power shelves and, from 2027, rectifiers and new direct-current breakers. That reshuffles the low-voltage order book; it does not shorten the grid-side queue.

## Will the parts be the next queue?

Possibly: some bushings now wait longer than a whole transformer did before the pandemic, though other parts are flowing freely.

<a id="the-parts-list"></a>

A transformer ships only when its slowest part arrives. Hitachi Energy publishes delivery times for the components it sells to other transformer makers, and the page is the only maker-quoted wait I know of. On 29 October 2026 it gave 135 weeks for its GSBK and ARF high-voltage bushings of 245 to 550 kilovolts from Ludvika, Sweden; other series from the same plant quote 27 to 46 weeks. In 2012 the Department of Energy heard such bushings took up to five months.

{{FIG11}}  <!-- A high-voltage bushing from Sweden now waits longer than a whole transformer did in 2010 -->

The same family of bushings ships in 14 to 16 weeks from Hitachi Energy's plant in Hefei, China, per the same page, updated in August. Those units may not suit every American utility's specification, and the emergency order makes Chinese-made gear harder to use. Tap changers, another bought-in part, are quoted at 10 to 22 weeks from Ludvika, so the strain is not everywhere.

Two moves fit the reading that the parts are binding. On 28 October 2026 GE Vernova agreed to pay about $9.0bn for Trench, which makes bushings, instrument transformers and coils, and called it "vertically integrating an existing supplier"; closing is expected in late 2027. And Hitachi Energy is spending $106m at Alamo, Tennessee, on what it calls the "largest bushings manufacturing facility in North America", due by mid-2027.

Breakers face a regulatory queue of their own. Most high-voltage breakers quench their arc in sulphur hexafluoride, SF6, the most powerful greenhouse gas known. The European Union bans new switchgear using such gases in stages, reaching equipment above 52,000 volts from 2028. In June 2026 Italy, Bulgaria and the Czech Republic warned the EU's Council that if the other gas-free designs are pushed out, "only one manufacturer of dry-air solutions remains", with capacity "lower than the European demand". They were arguing for those other designs, and the rules allow time-limited exemptions.

The inference is mine, and it is a hypothesis. If the parts gate output, a new hall in 2027 adds floor space before it adds transformers, and years of work stay high for a reason no factory count shows. Swedish bushing waits falling below a year, or makers saying parts no longer hold them back, would kill it.

## Has the shortage peaked?

The rate of increase probably has, but every order book is still growing, and a narrower gap still adds to the pile.

The case for a peak is real, and I concede it. Siemens Energy's grid book-to-bill fell to 1.48 in the quarter to June 2026, from 2.28 in the quarter before. GE Vernova's Electrification orders fell 9 per cent organically in its third quarter, against a large order a year earlier. Eaton's Electrical Americas ratio went flat. Schneider said demand from its power and grid customers "declined slightly", though only because power generation fell while grid customers stayed strong.

Consultants say the same. Wood Mackenzie's estimate of the power transformer shortage fell from 30 per cent for 2025 to 15 per cent for 2026. Imports of large transformers grew only about 10 per cent in the first eight months of 2026, after 39 per cent in 2025.

The case against is stronger. Every book-to-bill above is still above 1, so every pile is still growing. GE Vernova's grid equipment backlog is up 60 per cent in a year, or about 40 per cent without the Prolec GE purchase. Transformer prices are rising faster than in 2023 and 2024. American investor-owned utilities plan about $239bn of capital spending in 2026, their trade body says, against $204bn in 2024. And the Ludvika bushings wait 135 weeks.

The last cycle shows what a real peak looks like. The Department of Energy's 2012 study records Korean exports of large transformers to America rising from $33m in 2005 to $279m in 2011. Then demand slowed, makers cut prices to fill new halls, and the American makers filed a dumping case. A peak shows up as price cuts and idle halls. Neither is visible yet.

## Why not just keep spare transformers?

Because spares are few, are held for disasters rather than new load, and none of the shared schemes has yet supplied a single unit.

A spare is the one thing that beats the queue. The Department of Energy's 2024 report sets out the steps to install a ready spare, from teardown to commissioning test, and they total three to four weeks. Against a three-year order, that is a bargain, and utilities do keep their own spares, often in the same substation.

The shared schemes are thin. The Edison Electric Institute's Spare Transformer Equipment Program, started in 2006, triggers only after a declared terrorist attack or emergency, and "to date STEP has never been utilized", the department wrote. Grid Assurance, a company set up by utilities to hold spares in secure warehouses, "has not yet actually provided a replacement" large transformer.

Spares also do not help a new campus. They exist to replace a failed unit at an existing substation. A data centre needs a new unit for a new connection, and taking a utility's spare would leave that utility exposed. So spares shorten outages, not the queue for new load.

## So who holds the scarce thing, and what should an investor watch?

Whoever owns the slowest station: the large transformer halls, the steel, and a few parts.

If the queue is kept, three positions gain. **The grid makers**: Hitachi Energy, Siemens Energy and GE Vernova, with HD Hyundai Electric, Hyosung and LS Electric from Korea, make the large transformers and high-voltage breakers. They hold years of signed work and the choice of which orders to take.

**The inside-the-fence makers**: Eaton, Schneider Electric, ABB, Siemens, Vertiv, Legrand, nVent, Hubbell and Powell make switchgear, UPS systems and power rooms, with a shorter queue. Caterpillar, Cummins, Generac and Rolls-Royce make the backup generators, where the waits run into 2029.

**The parts behind the parts**: bushings, tap changers and core steel come from a few suppliers. When a grid maker buys one outright, as GE Vernova is buying Trench, it shows which part it was waiting for.

Four numbers carry the story. Siemens Energy's grid ratio and Eaton's Electrical Americas ratio each quarter, which are the claim's tests. Book-to-bill at the grid makers, which shows whether the pile is still growing. And Hitachi Energy's component delivery page, which shows whether the parts are easing.

At the scale of the grid, a connection alone does not start a hall. A utility can clear a site's place in the grid queue, as in [America rations the plug](/journal/america-rations-the-plug/), and the site still waits for its transformer. Nvidia launches a new flagship chip about every year. A transformer ordered today joins a pile that would take three or four of those generations to clear, so a data centre's real start date is set years before the chips it will run are on sale.

## What would prove me wrong

Three tests can break the claim. The first is the ratio drifting down. If by 30 June 2028 Siemens Energy's grid order book has fallen below 3.6 years of its sales, or Eaton's Electrical Americas below one year, the first wave of new plants has shortened the queue and the claim fails. This test is closer than it looks: Siemens Energy's grid sales grow about 25 per cent a year, so at the third quarter's book-to-bill of 1.48 the ratio would reach about 3.4 by mid-2028. Orders must run about 1.8 times sales to hold it.

That is a genuine risk. A narrowing gap lowers years of work while the pile still grows, as the arithmetic above shows, and Eaton's ratio has already gone flat. Eaton's total electrical book-to-bill over twelve months was 1.2 in September 2026; Eaton's new Jonesville and Bellevue plants land in 2027, a year before the test.

The second is orders cooling as the plants open. If book-to-bill falls below 1 at the grid makers just as the 2027 halls start, the makers built into a slowdown. For now Siemens Energy's grid business is at 1.48 and GE Vernova's at about 1.4. Years of work falling while the first plants open on time would move me before the test date, because that is the queue clearing.

The third is someone breaking ranks. If makers outside this group, in Korea, Brazil or China, add capacity to clear the queue and American buyers accept their units, it empties faster. The Korean makers are adding capacity in Alabama and Tennessee; if they build ahead of orders, the wait shortens.

The claim stands on two legs. The first is time: halls take two to three years, and steel, ovens and test bays cap output. That is physics, but it expires as the halls land from 2027. The second is choice: the makers size halls to signed orders, a business decision they can drop. The wait in 2030 rests on the second leg.

Two things would not move me. More factory announcements: they are the headline, not the order book. And price rises: they show the queue holding, not clearing.
