---
title: "Johor and Singapore: the plug, not the chip, decides who gets to build"
date: 2026-11-07T15:52:33+08:00
summary: "Malaysia's data centres draw about a fifth of the grid power they have connected, while Singapore turns most would-be builders away. Both show the same thing: in Johor and Singapore the right to draw power from the grid, not a supply of chips, decides who gets to build, and both governments now ration that right: Singapore since its 2019 pause, Malaysia since October 2026. Hong Kong is the mirror image: its utility must build to demand, and the chip licence is the gate."
category: "Analysis"
format: "depth"
cover: "/covers/the-queue-not-the-chip.svg"
tags: ["grid", "power", "johor", "singapore"]
draft: true
---

<a id="the-queue-not-the-chip"></a>
<a id="the-part-money-cannot-hurry"></a>

In June 2026 Malaysia's data centres were connected to 5.65 gigawatts of grid supply and drew 1.26 gigawatts of it. About 4.4 gigawatts sat connected and unused, probably most of it in Johor, which holds two thirds of the bookings. Johor is the Malaysian state across a one-kilometre causeway from Singapore.

That August Singapore chose four of more than 20 proposals for 200 megawatts of new data centre capacity. Then, on 28 October 2026, Malaysia's investment minister told Parliament that a data centre would get grid power only if the grid had spare margin after everyone else.

That is the claim of this piece. In Johor and Singapore the scarce thing is the right to draw power from the grid, not a supply of chips, and both governments now ration that right. Chips decide how fast a finished hall fills. Whether the hall may be built at all is settled at the plug.

To see why, the piece follows the questions in order. What it takes to plug a data centre in, and why so many came to Johor. How Singapore decides who may build. How much Johor has booked against how much it draws, and why the gap is so wide. Who fills the halls and what the chips have to do with it, what a Johor hall pays for its plug, and why Malaysia began rationing. Then water, building your own power, and Hong Kong, where the gate sits somewhere else entirely.

<details class="analogy">
<summary>The analogy</summary>
<p>Think of a restaurant. A party books a table for forty months ahead: that is the booked megawatt. The fire code caps how many may sit in the room, whatever the bookings say: that is Singapore's licence. The diners actually eating are the drawn power, and they are what the kitchen cooks for.</p>
<p>Malaysia, mostly Johor, has tables booked for forty and about nine people eating. Singapore's room is full, so the owner gives the last few seats to the most efficient kitchens. Bringing your own gas cylinder does not help, because the limit is on seats, not on gas. Hong Kong's restaurant must seat everyone who comes; its problem is that the best food needs an import licence.</p>
</details>

## What does it take to plug a data centre into the grid?

Five steps, from asking the utility for supply to racks running, and in Johor and Singapore only one of them is handed out by a government.

Start with the units, because every number in this piece uses them. A **watt** measures how fast energy is used; a kettle draws about 2,000 watts. A **megawatt (MW)** is a million watts, and a **gigawatt (GW)** is a thousand megawatts. One Nvidia GB200 NVL72 rack, the standard AI cabinet today, is rated at about 132 kilowatts, so 100 megawatts runs about 750 of them before cooling. A **kilovolt (kV)** is a thousand volts; the higher the voltage, the more power a line carries with less loss.

Power reaches a hall the way water reaches a tap. Power stations feed a high-voltage network, the motorway, running at 500, 275 and 132 kV in Peninsular Malaysia. A **substation** steps that voltage down through **transformers**, large oil-filled machines that change voltage, and a big campus has its own. Then cable carries the power into the halls, and a building's own equipment steps it down again to the racks.

The steps a campus walks run like this. First, the operator asks the utility for supply. Second, the government decides whether it may plug in at all: Singapore only through a call for applications, Malaysia now only from the grid's spare margin. Third, the operator signs a supply contract that books its finished size, years before its halls fill. Fourth, the substation, transformers and cable are built. Fifth, tenants fill the halls with chips, at their own pace.

<!--FIG:chain-->

The contract in step three carries the most important number in this piece. Malaysia calls it an **Electricity Supply Agreement (ESA)**, and it fixes the site's **maximum demand**: the most power the site may draw at any one moment. A campus books maximum demand for its finished size, then declares it in steps, year by year, as halls open. Hold on to that difference between the whole booking and the step a site stands on; it explains most of the gap this piece is about.

That gives three different megawatts, and headlines mix them up. **Booked** is the maximum demand in the supply contract. **Licensed**, in Singapore, is the computing load a regulator lets a hall run. **Drawn** is the power actually flowing at the meter. Press releases quote the first, Singapore rations the second, and Johor lives in the gap between the first and the third.

## Why did so many data centres come to Johor?

Because Singapore stopped building in 2019, and Johor next door could connect a campus in twelve months.

Singapore is where South East Asia's data centres first clustered, around its subsea cables and its customers. By 2019 its data centres used about 5.3 per cent of the country's electricity, and about 7 per cent in the first seven months of 2020, according to its communications ministry. In 2019 the government told the industry of a "temporary pause" in new data centres and began a review. Its stated reason was that data centres are "intensive users of resources like land, water, and energy".

The pause sent new building over the causeway. Johor has land, sits on the Peninsular grid of Tenaga Nasional (TNB), Malaysia's national utility, and is close enough to Singapore for its networks to reach. Then Tenaga sped up the slowest step it controls. Its **Green Lane Pathway**, launched on 8 August 2023 for data centres taking supply at 132 or 275 kV, cut the time to connect from 36 to 48 months to 12, plant included. Its first supply agreements went to Yondr, AirTrunk, YTL's data centre arm and GDS, whose international business is now DayOne.

<!--FIG:map-->

The map shows where they went. Most campuses sit in two clusters. One is around Iskandar Puteri and Kempas, near Johor Bahru, where DayOne's two largest parks and AirTrunk's sit. The other is inland at Sedenak and Kulai, where YTL, Princeton Digital Group and Bridge Data Centres build, and Microsoft has bought land. By June 2026 Johor held 29 of Malaysia's 61 secured data centre projects and about two thirds of their booked capacity, on Tenaga's count.

<a id="two-governments-one-confession"></a>

One popular explanation is weaker than it sounds. The Johor-Singapore Special Economic Zone, agreed on 7 January 2025, covers eleven sectors across southern Johor, from logistics to energy. Neither the agreement's release nor the zone's official pages name data centres; its energy aim is trading renewable power with Singapore. The data centres came for land and a fast plug. Singapore's ministers accept the overflow: some workloads "will naturally locate where land and energy are more abundant", and "we do not need to host every megawatt", the Senior Minister of State for digital development told Parliament on 7 October 2026.

## How does Singapore decide who may build?

By rationing: new capacity is handed out in competitive calls for applications, each won by the most efficient and greenest bidders, and soon every large hall will need a licence stating how much computing it may run.

Singapore lifted its pause in 2022 with a pilot call that ran from July to November 2022. Bidders had to reach a **PUE** of 1.3 or better. Power usage effectiveness is the total power entering a building divided by the power reaching its computers; 1.3 means 30 per cent extra for cooling, lighting and losses. In July 2023 about 80 megawatts went to four winners: AirTrunk with ByteDance, Equinix, GDS and Microsoft, from more than 20 proposals.

The second call, opened on 1 December 2025, was stricter. It offered at least 200 megawatts to bidders at a PUE of 1.25 or better, with at least half their power from "green pathways" built in Singapore: low-carbon fuels such as hydrogen or ammonia, fuel cells with carbon capture, or solar panels on the building. On 21 August 2026 the Economic Development Board (EDB) and the Infocomm Media Development Authority (IMDA), Singapore's investment board and digital regulator, provisionally gave 50 megawatts each to Digital Realty, Equinix, Keppel Data Centres and STT GDC. Again there were more than 20 proposals.

All four winners will build on Jurong Island, the refinery and chemicals island off Singapore's south-west coast. About 20 hectares there are reserved for a green data centre park with up to 700 megawatts of power, counting cooling as well as computers. Singapore is an island of about 735 square kilometres with no hinterland, so land, not only power, sets the ration.

<!--FIG:sg-chart-->

How big is the fleet? About 1.6 gigawatts, but that is **maximum IT load capacity**, the most the halls could deliver to their servers, and it already includes the 200 megawatts just awarded and not yet built. What the fleet actually used is a different number. In 2024 Singapore's data centres consumed about 6.5 terawatt-hours, "slightly more than 10%" of national electricity, the minister said on 7 October 2026. That is an average draw of about 740 megawatts, on my arithmetic.

<a id="singapore-licenses-the-old-halls"></a>

The ration is now being written into law. Singapore's Digital Infrastructure Bill, debated in Parliament on 6 and 7 October 2026, requires a licence for any hall with 3 megawatts or more of **critical IT load**, the power a hall can deliver to its servers, own-use halls included. Each licence states that load. The regulator can fine an operator up to S$1 million or 10 per cent of its Singapore turnover, or cut the load it may run. About 70 data centres are in scope, and the minister expects the law in force in 2027.

There is one honest gap in the ration. The call's launch papers name a second route, the Strategic Digital Infrastructure Scheme, for proposals with "uniquely differentiated value". On 6 October 2026 the minister referred to operators "awarded capacity under" it, but no award has been published. Singapore's digital ministry says new capacity is "primarily" allocated by call, not only. So Singapore's ration is real, but not every seat is handed out in public.

<a id="singapore-cannot-wait-for-the-cable"></a>

Why not simply buy more power? Because Singapore makes about 95 per cent of its electricity from imported gas, and its plan for clean power is imports that do not yet exist. It aims to import about 6 gigawatts of low-carbon electricity by 2035. As of August 2026, 13 import projects held **conditional approvals** for 9.25 gigawatts, the regulator's first nod, and only six Indonesian ones had moved to conditional licences. In October 2026 Sembcorp won conditional approval for up to 1.3 gigawatts more, from Vietnamese wind via Malaysia. Each needs subsea cable and converter stations, made to order by a handful of factories.

## How much has Johor booked, and how much does it draw?

Far more than it draws: in June 2026 Malaysia's data centres drew about 22 per cent of the maximum demand they had connected.

The numbers come from Tenaga's quarterly analyst briefings and answers to Malaysia's Parliament. At June 2026, 42 data centre projects were "in system", connected to Tenaga's grid, with 5.65 gigawatts of maximum demand. Another 16 projects with 2.21 gigawatts were under construction, and three with 0.49 gigawatts had signed but not started: 61 projects and 8.35 gigawatts in all. Johor held 29 of the 61 projects and 5.6 gigawatts of the total.

Against those bookings, the load actually drawn by Malaysia's data centres was 603 megawatts in June 2025, 850 in December and 1,256 in June 2026. Their electricity use doubled, from 1.9 terawatt-hours in the first half of 2025 to 4.0 in the first half of 2026. Even so, data centres were still only 6 per cent of the electricity Tenaga sold.

<!--FIG:fill-chart-->

<a id="the-plug-not-the-chip"></a>

So the draw is rising fast, and still far below the booking. In the year to June 2026 the load drawn roughly doubled, while the maximum demand in Tenaga's system grew by about 60 per cent. The share drawn crept only from about 17 per cent to about 22 per cent, because campuses kept connecting faster than their halls filled.

One limit applies to every figure here: they are Malaysia-wide. Nobody publishes how much Johor alone draws, not Tenaga, the Energy Commission or any minister. Johor's own numbers are bookings (5.6 gigawatts), a projection (4.43 gigawatts of data centre peak demand by 2030, on the energy ministry's planning figures as reported by Bernama on 19 October 2026) and counts of sites. Since Johor holds two thirds of the bookings, the national gap is mostly a Johor gap, but that is an inference, not a measurement.

## Why is so much booked and so little drawn?

Because a campus books its finished size and fills in steps on its tenants' schedule; some of the gap is speculation, and nobody publishes the split.

Picture the booking as a staircase. The whole staircase is the **final maximum demand** in the supply contract, the campus at its full size. Each year the operator **declares** the step it expects to stand on, a smaller figure. And the **draw** is where its feet actually are. Booked, declared and drawn are three different numbers for the same site.

<!--FIG:staircase-->

That is why the same draw gives three honest shares. On 28 October 2026 the Deputy Prime Minister told Parliament that data centres were using about 1,374 megawatts against 2,346 megawatts of contracted demand at August 2026: 58.5 per cent, his figure. On 13 October ministers had said the 45 operating data centres used about 1.37 gigawatts of 6 gigawatts of maximum load, about 23 per cent on my division. And on Tenaga's series, 1,256 megawatts of 5.65 gigawatts in June 2026 is about 22 per cent.

<!--FIG:ratio-chart-->

A year earlier the same pairing showed. In November 2025 Parliament heard that 603 megawatts were drawn against 1,276 declared, about 47 per cent, against a government target of 85 per cent. On Tenaga's measure the same 603 megawatts were about 17 per cent of the booking.

Part of the gap is plain ramp-up: a hall built in phases books for the whole. Part is overbooking. In November 2025 ministers told Parliament the Energy Commission had found a likelihood of "speculative" applications and revised its projections. Part may be headroom: a hall books for its hottest hour with every chip flat out, so even a full hall draws less than its booking. No published figure splits the gap between ramp, speculation and headroom, so I hang nothing on any one of them.

<a id="johor-plugs-in-before-it-fills"></a>

There is one more trap, and it is the most useful thing for an investor in this piece: a hall can be finished, let and paid for while drawing little. DayOne, the operator spun out of the international business of GDS, a Chinese data centre company, filed to list its shares in the United States on 5 October 2026. At 20 September 2026 it had about 789 megawatts of IT capacity in service in Johor, and about 1.4 gigawatts booked there. Across its whole portfolio, 99.1 per cent of the capacity in service was billing, being paid for by tenants.

Now set that against the meter. Halls draw more than their IT capacity, because cooling and losses add to it. At a PUE of about 1.3, DayOne's Johor halls alone would draw about a gigawatt if run flat out, on my arithmetic: three quarters of the 1.37 gigawatts all of Malaysia's data centres drew in August, leaving about 0.35 gigawatts for every other operator in the country. The bases differ (a rating against a measured draw, slightly different dates), so this is a pointer, not proof: capacity that is billing need not be capacity that is running.

The reason is the contract. DayOne describes contracts of mostly 10 to 15 years, "predominantly" take-or-pay, under which the tenant pays for the capacity reserved whether or not it uses it. Power itself is "generally charged based on customers' actual power consumption on a pass-through basis". The landlord is paid for the plug, not the power. Revenue follows the booking; electricity follows the chips.

## Who fills the halls, and what do the chips have to do with it?

A few very large tenants fill them, one above all, and American export rules set how fast that tenant can add new chips, not whether a hall gets built.

The tenants are **hyperscalers**, the handful of companies large enough to rent or build whole data centres at a time. Most Johor operators run **colocation**: the operator builds the hall, power and cooling, and the tenant brings and owns its servers. DayOne's filing shows how concentrated that is. Its largest customer, described only as "a global technology company with a leading short-form video platform", provided 69.4 per cent of its revenue in 2025 and 69.2 per cent in the first half of 2026. That customer's commitment grew from an initial 64 megawatts to 838 megawatts across Johor, Bangkok and Helsinki.

The filing never names it. SemiAnalysis, a chip research firm, identifies it as ByteDance, the Chinese owner of TikTok. Other operators publish less. AirTrunk says its first two Johor campuses, more than 420 megawatts, are "almost 100% contracted". YTL Power reports 298 megawatts contracted at its Kulai park and has doubled its plan there to 1.2 gigawatts. Bridge Data Centres lists two Johor campuses with 508 and 374 megawatts of planned capacity. None publishes how much is energised.

Now the chips. Since 17 November 2023 an American licence has been needed to export advanced AI chips to any company headquartered in China or Macau, or in the other countries of an arms-embargo group, or whose ultimate parent is, wherever it sits. On 31 May 2026 the US Bureau of Industry and Security (BIS), which licenses American chip exports, confirmed that this applies everywhere outside the United States, Malaysia included. A Chinese-owned tenant in Johor therefore needs a licence for every new shipment of top chips.

Three details narrow that gate, and the live debate often misses them. First, the same guidance says bona fide operators of data centres "are not required to cease the ongoing use" of chips already installed "until further notice". Second, the licence attaches to chips exported to the Chinese firm. A Chinese company renting computing from a non-Chinese owner in Johor receives no export and needs no licence; the Remote Access Security Act, which would close that gap, passed the US House in January 2026 and has not passed the Senate. Third, the stricter licence rule for all of Malaysia and Thailand that BIS announced in May 2025 had not been published as a regulation by 7 November 2026.

Malaysia has moved too. Since 14 July 2025 its trade ministry has required a permit for every export, transhipment or transit of high-performance American AI chips, aimed at chips passing through Malaysia rather than chips working there. In a trade agreement of 26 October 2025 Malaysia committed to "align with all unilateral export controls in force by the United States". And the risk is real: on 1 October 2026 the US Justice Department announced charges against a Californian for smuggling more than US$300 million of AI servers to China through Malaysia and Singapore.

So the chip matters, but in a precise way. It sets how fast a hall already built and let can fill, and how fast its main tenant can add new machines. It does not decide which campuses get built, because the plug and the contract come first. For halls already plugged in, chips do set the pace of filling. For anyone hoping to build next, the limit is the plug.

## What does a Johor data centre pay for its plug?

More than ordinary industry for each unit of energy, plus charges that punish a booking left idle and a premium for speed.

Malaysia's tariff reform of 1 July 2025 split the bill into charges for energy, for capacity and for the network. It also created an **ultra high voltage** class, which the government told the Senate on 8 December 2025 is for data centres connected at high and extra high voltage. Its energy rate is 55.18 sen per kilowatt-hour at peak and 51.09 off peak, against 44.52 and 40.43 for ordinary high voltage users: about a quarter more. (A sen is a hundredth of a ringgit.) The capacity and network charges, RM21.76 and RM23.06 per kilowatt a month, are the same.

<a id="malaysia-keeps-the-wires-shared"></a>

The charge that matters most is the one for not using what you booked. Tenaga's **connected load charge** bills RM8.50 a month for every kilowatt by which a new customer's demand falls short of the line. In years one to four the line is 85 per cent of the step declared for that year; in years five and six it is 75 per cent of the final maximum demand. Its own charges book says it exists to stop customers "over declaring" their needs. On my reading, a hall that declared 100 megawatts and peaked at 50 would pay about RM300,000 a month.

Speed now has a price as well. Tenaga's Connection Charge Book of 2025 charges for fast delivery. To be connected within 12 months a customer pays a premium of 15 per cent of the project's cost, within 18 months 10 per cent and within 24 months 5 per cent, with damages for delay either way. It does not say whether Green Lane customers pay it. And the campus pays for its own connection: the project's cost less 15 years of the margin Tenaga expects to earn from its load. If that comes to nothing, it posts a refundable deposit of 25 per cent of the project's cost, lost if it fails to reach 75 per cent of its final demand within six years.

Operators carry some of this risk themselves. DayOne's filing says it "typically" agrees to buy a minimum amount of power from utilities, so a shortfall by its tenants can land on it. The investment minister put the logic to Parliament on 28 October 2026 in one line: a data centre that asks for 300 megawatts and uses 100 pays for the other 200.

## Why did Malaysia start rationing the plug in October 2026?

Because the sums stopped adding up: approvals ran far ahead of the power stations and wires that would have to serve them.

<a id="malaysia-grants-only-the-spare-margin"></a>

On 28 October 2026 Investment Minister Johari Abdul Ghani told Parliament the new rule. A data centre gets grid power only if Tenaga's **reserve margin**, the spare generating capacity kept above peak demand, has room after other industry. Otherwise it must build its own power off the grid, with the energy ministry's approval. Of the 117 data centres Malaysia has approved, 27 will take their power that way, and 24 new applications are held until the 117 settle. Asked about a moratorium, he said, in effect, that "our moratorium is the way we process" (my translation).

The minister also gave the number behind the rule. If all 117 approved centres are completed, he said, they would need "about 23,000 or 23,500 megawatts". That was an oral estimate, given without its basis. But Peninsular Malaysia's highest demand ever, set on 6 August 2026, was 22,014 megawatts, and its installed generating capacity is about 29.2 gigawatts. The approved data centres alone would need about as much power as the whole peninsula uses at its peak.

<!--FIG:sums-chart-->

Demand is already running ahead of the plan. Malaysia's planning committee had projected a 2026 peak of 21.3 gigawatts, as reported in July 2026; the actual peak passed it by August. Tenaga is retiring 6.6 gigawatts of its own power stations by 2030, and the original 2,100 megawatt Tanjung Bin coal station in south-west Johor retires in 2031, according to grid operator data reported by The Edge. The bids reported for the new gas plants to replace them, tendered as NEWGEN26 for 2029 to 2031, are all outside Johor.

That pushes Johor's supply further away, onto the wires. Tenaga is building a new 500 kV backbone of about 500 kilometres, from Paka on the east coast to Kulai East in Johor, due by 2030. It lists a new 500/275/132 kV main intake substation at Sedenak West, in the heart of the inland cluster, as under way, with no completion date. And the spending has shifted. Of the base investment the regulator allowed Tenaga's regulated businesses for 2025 to 2027, only 13 per cent is labelled demand growth. In the first half of 2026, demand growth took RM2.3 billion of about RM5.5 billion of actual network spending, about 42 per cent.

<a id="phantom-load"></a>

Here is the question I cannot yet answer, and it matters for anyone valuing a Johor booking. An engineer sizing a grid does not add up every customer's maximum, because loads rarely peak together; the allowance is called the **diversity factor**. An allocation queue does add them up, because each booked megawatt is a promise the planner must keep. If the spare-margin test counts bookings rather than expected draw, the 4.4 gigawatts booked and idle could use up the margin on paper while wires and turbines sit half used.

The record fits that reading without proving it. The Energy Commission found likely speculative applications in 2025; the 24 new ones are parked; and press reports of a written answer in November 2026 describe operators now submitting ten-year staggered projections and receiving grid access in phases. If planning counts bookings, the cheapest new gigawatt in Johor is a reclaimed booking, not a new substation. Nothing published yet says which it counts.

On 28 October the Deputy Prime Minister also added two conditions. Every data centre must take at least 30 per cent of its capacity or energy from renewables, under a framework the Energy Commission is still drafting. And every power application is now assessed first by an Energy Focus Group, whose secretariat is the Energy Commission, before the national data centre task force decides.

## Is water the next gate in Johor?

It is now a stated one: since October 2026 Malaysia will not consider data centres in areas with a low water reserve margin.

<a id="johor-waits-on-the-treatment-plant"></a>

Data centres use water mainly for cooling, and the binding measure in Johor is treatment capacity, the plants that turn river water into supply. In 2025 Johor's plants could treat about 2,375 million litres a day, against demand of 2,034, a reserve margin of 14.3 per cent, according to SPAN, the national water regulator. That leaves about 340 million litres a day spare, on my arithmetic, inside the regulator's target band of 10 to 15 per cent.

The data centre projections are of the same size as that spare. In November 2025 the government's written answer put Johor's data centre water demand at 384 million litres a day by 2030, on planning permissions already granted, as reported by EdgeProp. On 28 October 2026 the Deputy Prime Minister told Parliament that areas with a low water reserve margin "will not be considered" for data centres, and that each centre must keep at least two days of water on site.

The state is answering with supply and with reuse. Two new treatment plants, Semanggar for the Kulai and Sedenak area and Layang 2, add about 210 million litres a day by 2027, according to the state's figures as reported. And 12 million litres a day of treated sewage water already goes to cool Johor data centres, a first for Malaysia, the Deputy Prime Minister told Parliament on 24 June 2026. Water does not yet bind the way power does, but it is now part of the same ration.

## Can a data centre get round the queue by building its own power?

In America it often can; in Singapore it cannot, and in Malaysia only once the grid's margin is gone, with a permit.

American AI builders often escape grid queues by putting gas turbines or engines on site, a route covered in [Building your own power](/journal/building-your-own-power/). In Singapore that is legal under licences from the Energy Market Authority, its power regulator. But it buys nothing that matters. The new licence states the critical IT load a hall may run, so a turbine in the yard adds electricity, not one licensed megawatt of computing. Singapore rations computing, not power.

In Malaysia own power is now the official answer for those the grid will not serve: 27 of the 117 approved centres will go off grid, with approval from the energy ministry through the Energy Commission. That moves the queue rather than removing it. A campus then needs its own gas supply, its own generating plant and its own permits, and, from the October rules, at least 30 per cent renewable power on top. Own power gets round a queue; it does not get round a ration.

## Why is Hong Kong the opposite case?

Because Hong Kong's utility is obliged to build to demand, so the plug is open, and the gate that binds is the American chip licence.

<a id="hong-kong-has-the-plug"></a>

CLP Power, the utility for Kowloon and the New Territories, works under a **Scheme of Control**, its regulatory deal with the government, which obliges it to meet demand in return for a regulated return on what it builds, to 2033. At the end of 2025 it had 9,258 megawatts of capacity for Hong Kong customers against a highest local demand of 7,455 megawatts, about a quarter to spare. Its data centre customers drew an average of about 283 megawatts in the first nine months of 2026, on my arithmetic from its sales. It had finished eight data centre substations by June 2026 and plans 18 in its 2024 to 2028 Development Plan.

<!--FIG:hk-chart-->

Hong Kong's one AI megasite shows the difference. Sandy Ridge, a site of more than 110,000 square metres in North District, was tendered to the whole industry and drew a single bid, from a subsidiary of Range Intelligent Computing, a company listed in Shenzhen. It was awarded on 2 March 2026 on a 50-year grant. CLP targets power "commencing operations in phases from mid-2027"; the government expects the site to operate in 2029.

The plug is not the problem; the chip is. Since December 2020 American export rules have treated Hong Kong as China. Every advanced AI chip shipped to a Hong Kong hall needs a licence. Since 15 January 2026 chips up to the class of Nvidia's H200, shipped from 2024, can be licensed case by case for end users in China; anything more powerful is presumed denied. So a Hong Kong hall is capped about two chip generations behind the frontier, however much power it has.

<a id="the-second-gate-is-beijing"></a>

There is even a second hand on that gate. Press reports in August 2026 put hundreds of thousands of H200s in Hong Kong, kept there while Beijing limits their import to the mainland. The chips are physically there and still not running. Johor and Singapore ration the plug and leave the chip open to most tenants; Hong Kong opens the plug and has the chip rationed from outside.

<a id="gates-in-series"></a>

Put the three cities side by side and the lesson for an investor is about which number to read. In Johor, read draw against booking. In Singapore, read the licence and the calls. In Hong Kong, read the chip rule. Spare power in Hong Kong forecasts nothing about AI computing, and booked power in Johor forecasts only the order of the queue.

## So who holds the scarce thing, and what should an investor watch?

Whoever holds a right to draw: a Singapore licence, a Johor booking with a live plug, or a place inside Malaysia's spare margin.

At the scale of a hall, Singapore licenses the load it may run, and in Johor a hall already plugged in fills at the speed of its tenant's chips. At the scale of a campus, the supply agreement books the finished size years ahead, so the booking, not the building, is what a campus holds that others cannot copy. At the scale of a country, Singapore lacks land and clean power, and Malaysia now hands data centres only the spare margin.

That points the value at three places, whoever wins each campus. **Halls with a live plug** are paid on take-or-pay contracts for capacity, with power passed through, so a hall can be energised, let and earning while drawing little. **The keeper of the margin**, Tenaga, earns its regulated return on the wires and charges idle bookings. **The plant on the slow clock**, the makers of transformers, switchgear and subsea cable covered in [The equipment queue](/journal/the-equipment-queue/), is paid by every winner.

For a fund, five numbers carry the story, each published on a schedule. Tenaga's quarterly data centre draw against maximum demand in its system. Any Johor-only split of that draw. Whether the spare-margin test counts bookings or expected draw. Singapore's next call, which EDB and IMDA will review 18 to 24 months from August 2026, and any published award under its second scheme. And any change in the American chip rules, above all a law reaching remote access.

## What would prove me wrong

Two tests break the claim. If Tenaga's briefing for June 2027 shows Malaysia's data centres drawing 40 per cent or more of the maximum demand of the data centre projects in its system, halls are filling about as fast as they connect, and the plug is not the scarce thing. On trend they fall short: if load doubles again to about 2.5 gigawatts while most of the 2.21 gigawatts under construction connects, the share is roughly a third.

The second test is the policy. If, before the end of 2027, Malaysia lets new data centres connect to the grid again without the spare-margin test, the government no longer treats the plug as scarce, and the ration was a pause, not a regime.

Some events would move me before either test. Regulators clawing back idle bookings would shrink the bottom of Tenaga's ratio and could push the share over 40 per cent without one more chip racked; I would mark the test broken and say why. A Singapore award outside a call, published under its second scheme, would show the ration bending. And a tightening of American rules to cover renting computing would move Johor's limit from the plug towards the chip.

Three things would not move me. Faster draw growth on its own: draw more than doubled in a year and the share still crept, because bookings grew too. Bigger headline pipelines: a booked gigawatt is a place in line, not a computer at work. And a Hong Kong substation opening early: there the plug was never the gate.

<details class="claims-record">
<summary>The claims on record, word for word</summary>

**Johor and Singapore: the plug, not the chip, decides who gets to build** (CLAIM_DATE)

Claim: "CLAIM_TEXT"

Breaks if: "BREAKS_TEXT"

EARLIER_CLAIMS

</details>

<details class="evidence">
<summary>The figures behind the charts</summary>

**Tenaga's series.** All draw figures are Malaysia-wide; no Johor-only draw is published. December 2025 counts capacity "in operation", not "in system".

| As at | Load drawn | Booked maximum demand | Share drawn | Source |
|---|---|---|---|---|
| June 2025 | 603 MW | 3.5 GW in system | about 17% | Tenaga briefing, 2QFY2025 |
| June 2025 | 603 MW | 1,276 MW declared | about 47%, target 85% | Dewan Rakyat Hansard, 5 November 2025 |
| September 2025 | 710 MW | not given | | Tenaga briefing, 28 August 2026 |
| December 2025 | 850 MW | about 4.5 GW in operation | about 19% | Tenaga briefing, 4QFY2025 |
| March 2026 | 1,054 MW | about 4.5 GW in system | about 23% | Tenaga briefing, 1QFY2026 |
| June 2026 | 1,256 MW | 5.65 GW in system, 42 projects | about 22% | Tenaga briefing, 28 August 2026 |
| August 2026 | about 1.37 GW | 6 GW at 45 operating sites; 8.77 GW signed by 62 | about 23% | Dewan Rakyat Hansard, 13 October 2026 |
| August 2026 | about 1,374 MW | 2,346 MW contracted | 58.5% | Dewan Rakyat Hansard, 28 October 2026 |

At June 2026, 2.21 GW was under construction (16 projects) and 0.49 GW signed (3), 8.35 GW across 61 projects; Johor 29 projects and "5.6GW out of 8.3GW" (Tenaga, slide 4). The 13 October share is my arithmetic; 58.5% is the minister's spoken figure (1,374 ÷ 2,346 = 58.6%). Counts differ by unit: Tenaga's 42 projects in system, 45 completed centres (energy ministry, August 2026), 55 operating and 117 approved (investment ministry, 28 October 2026).

**DayOne.** Form F-1, 5 October 2026, figures at 20 September 2026: Johor in service about 789 MW (Nusajaya 47.8% and Kempas 34.3% of 962 MW group), bookings about 1,398 MW (28.8% and 32.5% of 2,281 MW), group billings 953 MW, utilisation 99.1%. Largest customer 69.4% of 2025 and 69.2% of first-half 2026 revenue; anchor 64 MW to 838 MW. The draw comparison assumes a PUE of 1.3 (789 × 1.3 ≈ 1,026 MW), my arithmetic and an upper bound at full load.

**Singapore.** Pause and pilot: EDB and IMDA (20 July 2022, 14 July 2023); 2019 and 2020 shares: communications ministry written answer (27 July 2021). Roadmap "at least 300 MW": IMDA (30 May 2024). Second call: EDB and IMDA (1 December 2025, 21 August 2026). Fleet "more than 1.6 GW", maximum IT load capacity including the 200 MW: MDDI (8 September 2026) and closing speech (7 October 2026). 2024 use, 6.5 TWh, "slightly more than 10%": closing speech, 7 October 2026; 6.5 TWh ÷ 8,784 h ≈ 740 MW, my arithmetic. Strategic Digital Infrastructure Scheme: call fact sheet (1 December 2025), opening speech (6 October 2026). Imports: energy ministry import page (as of August 2026); Sembcorp: EMA (26 October 2026). Bill: Bill No. 20 of 2026; I found no record of its third reading.

**The sums.** Peak 22,014 MW (6 August 2026) and installed capacity 29.2 GW (June 2026): Tenaga briefing and October 2026 deck. "About 23,000 or 23,500 megawatt" for 117 centres: Johari Abdul Ghani, Dewan Rakyat, 28 October 2026, oral. 8.39 GW Peninsular data centre peak by 2030, 4,428 MW in Johor: energy ministry written answer as reported by Bernama (19 October 2026). 2026 projected peak of 21.3 GW: written answer as reported by the New Straits Times (1 July 2026). Tanjung Bin and NEWGEN26 bids: The Edge (14 August 2026), citing grid operator data.

**Charges.** Energy Commission tariff schedule from 1 July 2025; Tenaga Connection Charge Book 2025 (connected load charge pp. 15 to 17, connection charge pp. 44 to 45, fast track pp. 46 to 47). The RM300,000 example: (85 MW − 50 MW) × RM8.50 × 1,000, my arithmetic on my reading of the book. Grid spending: Tenaga investor deck (October 2026), RP4 base RM26.55 bn of which RM3.49 bn demand growth, contingent RM16.27 bn; first-half 2026 network spending RM2.6 bn security of supply, RM2.3 bn demand growth, RM0.6 bn energy transition (briefing, 28 August 2026).

**Water.** SPAN Water and Sewerage Fact Book 2025: Johor capacity 2,375 MLD, demand 2,034 MLD, margin 14.3% (2021 to 2025: 14.3, 11.5, 16.8, 15.7, 14.3%). 384 MLD by 2030: written answer reported by EdgeProp (19 November 2025). Rules: Dewan Rakyat, 28 October 2026. Reclaimed water: Dewan Rakyat, 24 June 2026. New plants: Johor State Assembly as reported by The Star (19 November 2025).

**Chips.** BIS guidance (31 May 2026), citing the licence requirement in force since 17 November 2023; BIS release (13 May 2025); Federal Register search to 7 November 2026 found no Malaysia or Thailand rule; MITI statement (14 July 2025); US-Malaysia Agreement on Reciprocal Trade, Article 5.2.1 (26 October 2025); Congressional Record (12 January 2026); 91 FR 1684 (15 January 2026); Justice Department (1 October 2026).

**Hong Kong.** CLP Power offering circular (1 April 2026) and Ten-year Summary; CLP quarterly statement (12 October 2026): 6.6% of 28,131 GWh over 6,552 hours ≈ 283 MW, my arithmetic; CLP annual and interim results (26 February and 6 August 2026) for substations. Sandy Ridge: Hong Kong government (2 March 2026, 22 April 2026). 15 CFR 742.6, as amended to 23 July 2026, China policy set 15 January 2026. Reuters (5 November 2026) for the stored H200s, press only.

</details>

<section class="exposure">
<h3>Who is exposed if the plug, not the chip, decides who builds in Johor and Singapore</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares. Figures in the piece are disclosures used as evidence for the mechanism.</p>
<dl>
<dt>The utilities</dt>
<dd><span class="names">Tenaga Nasional</span>, <span class="names">SP Group</span> and <span class="names">CLP Power</span> run the Peninsular Malaysian, Singapore, and Kowloon and New Territories grids.</dd>
<dt>Campus operators</dt>
<dd><span class="names">DayOne</span>, <span class="names">YTL Power</span>, <span class="names">AirTrunk</span>, <span class="names">Bridge Data Centres</span>, <span class="names">Princeton Digital Group</span>, <span class="names">Equinix</span>, <span class="names">Digital Realty</span>, <span class="names">Keppel Data Centres</span>, <span class="names">STT GDC</span> and <span class="names">Range Intelligent Computing</span> run data centres.</dd>
<dt>Plant on the slow clock</dt>
<dd><span class="names">Hitachi Energy</span> and <span class="names">Siemens Energy</span> make transformers. <span class="names">Prysmian</span>, <span class="names">Nexans</span> and <span class="names">NKT</span> make subsea cable.</dd>
<dt>What fills the halls</dt>
<dd><span class="names">Nvidia</span> makes AI chips; <span class="names">ByteDance</span> is the largest reported tenant.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Anyone reading booked megawatts as computing at work, and campuses resting on one tenant's chip licence.</dd>
</dl>
</section>

<p class="sources">Sources: Tenaga's Green Lane release (9 August 2023), analyst briefings to 28 August 2026, October 2026 investor deck, Connection Charge Book 2025 and 500 kV backbone release (28 August 2026); the Energy Commission's tariff schedule from 1 July 2025; Dewan Rakyat Hansard of 5 November 2025 and 24 June, 13, 15 and 28 October 2026, and Dewan Negara Hansard of 8 December 2025; SPAN's Water and Sewerage Fact Book 2025; DayOne's Form F-1 (5 October 2026); YTL Power's Annual Report 2026; AirTrunk (30 April 2026); EDB and IMDA (20 July 2022, 14 July 2023, 1 December 2025, 21 August 2026), IMDA (30 May 2024), Singapore's communications and digital ministries (27 July 2021, 3 March, 8 September, 6 and 7 October 2026), the Digital Infrastructure Bill and the energy ministry's import page; the Johor-Singapore Special Economic Zone agreement (7 January 2025); US Bureau of Industry and Security (13 May 2025, 31 May 2026), the Federal Register and 15 CFR 742.6, Malaysia's trade ministry (14 July 2025), the US-Malaysia trade agreement (26 October 2025) and the US Justice Department (1 October 2026); CLP Power filings and the Hong Kong government. Press used only where no primary text was found, and named in the figures: Bernama, The Edge, the New Straits Times, EdgeProp, The Star and Reuters. The ByteDance identification is SemiAnalysis's. Personal research, not investment advice.</p>
