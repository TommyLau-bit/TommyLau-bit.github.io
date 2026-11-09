<a id="the-queue-not-the-chip"></a>
<a id="the-part-money-cannot-hurry"></a>

In June 2026 Malaysia's data centres were connected to 5.65 gigawatts of grid supply and drew 1.26 gigawatts of it. About 4.4 gigawatts sat connected and unused, probably most of it in Johor, which holds two thirds of the bookings. Johor is the Malaysian state across a one-kilometre causeway from Singapore.

That August Singapore chose four of more than 20 proposals for 200 megawatts of new data centre capacity. Then, on 28 October 2026, Malaysia's investment minister told Parliament that a data centre would get grid power only if the grid had spare margin after everyone else.

That is the claim of this piece. In Johor and Singapore the scarce thing is the right to draw power from the grid, not a supply of chips, and both governments now ration that right. Chips decide how fast a finished hall fills. Whether the hall may be built at all is settled at the plug.

{{ANALOGY}}

## What does it take to plug a data centre into the grid?

Five steps, from asking the utility for supply to racks running, and in Johor and Singapore only one of them is handed out by a government.

A **megawatt (MW)** is a million watts, and a **gigawatt (GW)** is a thousand megawatts. One Nvidia GB200 NVL72 rack, the standard AI cabinet today, is rated by Nvidia at about 120 kilowatts, so 100 megawatts runs about 830 of them before cooling. Power stations feed a high-voltage network. A **substation** steps that voltage down through **transformers**, large oil-filled machines that change voltage, and cable carries the power into the halls.

The steps a campus walks run like this. First, the operator asks the utility for supply. Second, the government decides whether it may plug in at all: Singapore only through a call for applications, Malaysia now only from the grid's spare margin. Third, the operator signs a supply contract that books its finished size, years before its halls fill. Fourth, the substation, transformers and cable are built. Fifth, tenants fill the halls with chips, at their own pace.

{{FIG1}}

The contract in step three carries the most important number in this piece. Malaysia calls it an **Electricity Supply Agreement (ESA)**, and it fixes the site's **maximum demand**: the most power the site may draw at any one moment. A campus books maximum demand for its finished size, then declares it in steps, year by year, as halls open.

That gives three different megawatts, and headlines mix them up. **Booked** is the maximum demand in the supply contract. **Licensed**, in Singapore, is the computing load a regulator lets a hall run. **Drawn** is the power actually flowing at the meter. Press releases quote the first, Singapore rations the second, and Johor lives in the gap between the first and the third.

## Why did so many data centres come to Johor?

Because Singapore stopped building in 2019, and Johor next door could connect a campus in twelve months.

By 2019 Singapore's data centres used about 5.3 per cent of the country's electricity, according to its communications ministry. That year the government told the industry of a "temporary pause" in new data centres. Its stated reason was that data centres are "intensive users of resources like land, water, and energy".

The pause sent new building over the causeway. Johor has land and sits on the Peninsular grid of Tenaga Nasional (TNB), Malaysia's national utility. Then Tenaga sped up the slowest step it controls. Its **Green Lane Pathway**, launched on 8 August 2023 for data centres taking supply at 132 or 275 kilovolts (kV), cut the time to connect from 36 to 48 months to 12, plant included.

{{FIG2}}

Most campuses sit in two clusters. One is around Iskandar Puteri and Kempas, near Johor Bahru, where DayOne's two largest parks and AirTrunk's sit. The other is inland at Sedenak and Kulai, where YTL, Princeton Digital Group and Bridge Data Centres build. By June 2026 Johor held 29 of Malaysia's 61 secured data centre projects and 5.6 of their 8.35 gigawatts, on Tenaga's count.

Singapore's ministers accept the overflow: "we do not need to host every megawatt", the Senior Minister of State for digital development told Parliament on 7 October 2026.

<a id="two-governments-one-confession"></a>

## How does Singapore decide who may build?

By rationing: new capacity is handed out in competitive calls, each won by the most efficient and greenest bidders, and soon every large hall will need a licence.

Singapore lifted its pause in 2022 with a pilot call. Bidders had to reach a **PUE** of 1.3 or better. Power usage effectiveness is the total power entering a building divided by the power reaching its computers; 1.3 means 30 per cent extra for cooling, lighting and losses. In July 2023 about 80 megawatts went to four winners, from more than 20 proposals.

The second call, opened on 1 December 2025, was stricter. It asked for a PUE of 1.25 or better, with at least half the power from "green pathways" built in Singapore. On 21 August 2026 the Economic Development Board and the Infocomm Media Development Authority, Singapore's investment board and digital regulator, provisionally gave 50 megawatts each to Digital Realty, Equinix, Keppel Data Centres and STT GDC. All four will build on Jurong Island, the refinery and chemicals island off Singapore's south-west coast.

{{FIG3}}

The fleet is about 1.6 gigawatts, but that is **maximum IT load capacity**, the most the halls could deliver to their servers, and it already includes the 200 megawatts just awarded. What the fleet used is smaller. In 2024 Singapore's data centres consumed about 6.5 terawatt-hours, "slightly more than 10%" of national electricity, an average draw of about 740 megawatts on my arithmetic.

<a id="singapore-licenses-the-old-halls"></a>

The ration is now being written into law. Singapore's Digital Infrastructure Bill, debated in Parliament on 6 and 7 October 2026, requires a licence for any hall with 3 megawatts or more of **critical IT load**, the power a hall can deliver to its servers. Each licence states that load, and the regulator can fine an operator or cut the load it may run. The minister expects the law in force in 2027. One gap remains: a second route, the Strategic Digital Infrastructure Scheme, exists for proposals with "uniquely differentiated value". On 6 October 2026 the minister referred to operators "awarded capacity under" it, but no award has been published. So Singapore's ration is real, but not every seat is handed out in public.

<a id="singapore-cannot-wait-for-the-cable"></a>

Why not simply buy more power? Because Singapore makes about 95 per cent of its electricity from imported gas, and its clean plan rests on imports that do not yet exist. It aims to import about 6 gigawatts of low-carbon electricity by 2035. As of August 2026, 13 import projects held conditional approvals for 9.25 gigawatts, and each needs subsea cable made to order by a handful of factories.

## How much has Johor booked, and how much does it draw?

Far more than it draws: in June 2026 Malaysia's data centres drew about 22 per cent of the maximum demand they had connected.

At June 2026, 42 data centre projects were "in system", connected to Tenaga's grid, with 5.65 gigawatts of maximum demand. Another 16 projects with 2.21 gigawatts were under construction, and three with 0.49 gigawatts had signed but not started. Against those bookings, the load actually drawn was 603 megawatts in June 2025, 850 in December and 1,256 in June 2026.

{{FIG4}}

So the draw is rising fast, and still far below the booking. In the year to June 2026 the load drawn roughly doubled, while the maximum demand in Tenaga's system grew by about 60 per cent. The share drawn crept only from about 17 per cent to about 22 per cent, because campuses kept connecting faster than their halls filled.

These figures are Malaysia-wide: nobody publishes how much Johor alone draws. Since Johor holds two thirds of the bookings, the national gap is mostly a Johor gap, but that is an inference, not a measurement.

<a id="the-plug-not-the-chip"></a>

## Why is so much booked and so little drawn?

Because a campus books its finished size and fills in steps on its tenants' schedule; some of the gap is speculation, and nobody publishes the split.

Picture the booking as a staircase. The whole staircase is the **final maximum demand** in the supply contract, the campus at its full size. Each year the operator **declares** the step it expects to stand on, a smaller figure. And the **draw** is where its feet actually are.

{{FIG5}}

That is why the same draw gives three honest shares. On 28 October 2026 the Deputy Prime Minister told Parliament that data centres were using about 1,374 megawatts against 2,346 megawatts of contracted demand: 58.5 per cent, his figure. On 13 October ministers had said the 45 operating data centres used about 1.37 gigawatts of 6 gigawatts of maximum load, about 23 per cent on my division. And on Tenaga's series, 1,256 megawatts of 5.65 gigawatts in June 2026 is about 22 per cent.

{{FIG6}}

Part of the gap is plain ramp-up: a hall built in phases books for the whole. Part is overbooking: in November 2025 ministers told Parliament the Energy Commission had found a likelihood of "speculative" applications. Part may be headroom, because a hall books for its hottest hour. No published figure splits the three.

<a id="johor-plugs-in-before-it-fills"></a>

The most useful point for an investor is that a hall can be finished, let and paid for while drawing little. DayOne, the operator spun out of the international business of the Chinese data centre company GDS, filed to list its shares in the United States on 5 October 2026. At 20 September 2026 it had about 789 megawatts of IT capacity in service in Johor, and across its portfolio 99.1 per cent of the capacity in service was billing.

At a PUE of about 1.3, DayOne's Johor halls alone would draw about a gigawatt if run flat out, on my arithmetic: three quarters of the 1.37 gigawatts all of Malaysia's data centres drew in August. The bases differ, so this is a pointer, not proof: capacity that is billing need not be capacity that is running.

The reason is the contract. DayOne's are mostly 10 to 15 years and "predominantly" take-or-pay: the tenant pays for the capacity reserved whether or not it uses it. Power itself is passed through at the customer's actual use. The landlord is paid for the plug, not the power. Revenue follows the booking; electricity follows the chips.

## Who fills the halls, and what do the chips have to do with it?

A few very large tenants, one above all, and American export rules set how fast that tenant can add chips, not whether a hall gets built.

DayOne's largest customer, described only as "a global technology company with a leading short-form video platform", provided 69.4 per cent of its revenue in 2025. SemiAnalysis, a chip research firm, identifies it as ByteDance, the Chinese owner of TikTok. Since 17 November 2023 an American licence has been needed to export advanced AI chips to any company headquartered in China or Macau, or whose ultimate parent is, wherever it sits. On 31 May 2026 the US Bureau of Industry and Security confirmed that this applies in Malaysia too. A Chinese-owned tenant in Johor therefore needs a licence for every new shipment of top chips.

Three details narrow that gate. Chips already installed may keep running "until further notice". A Chinese firm renting computing from a non-Chinese owner receives no export and needs no licence; the Remote Access Security Act, which would close that gap, has passed the US House but not the Senate. And the stricter rule for all of Malaysia and Thailand announced in May 2025 had not been published as a regulation by 7 November 2026.

So the chip matters, but in a precise way. It sets how fast a hall already built and let can fill. It does not decide which campuses get built, because the plug and the contract come first.

## What does a Johor data centre pay for its plug?

More than ordinary industry for each unit of energy, plus a charge that punishes a booking left idle.

Since 1 July 2025 data centres connected at high and extra high voltage pay an **ultra high voltage** rate of 55.18 sen per kilowatt-hour at peak, against 44.52 for ordinary high voltage users: about a quarter more. A sen is a hundredth of a ringgit.

<a id="malaysia-keeps-the-wires-shared"></a>

The charge that matters most is the one for not using what you booked. Tenaga's **connected load charge** bills RM8.50 a month for every kilowatt by which a new customer's demand falls short of a line: 85 per cent of the step declared in years one to four. Its charges book says it exists to stop customers "over declaring". On my reading, a hall that declared 100 megawatts and peaked at 50 would pay about RM300,000 a month. The investment minister put it in one line: a data centre that asks for 300 megawatts and uses 100 pays for the other 200.

## Why did Malaysia start rationing the plug in October 2026?

Because the sums stopped adding up: approvals ran far ahead of the power stations and wires that would have to serve them.

<a id="malaysia-grants-only-the-spare-margin"></a>

On 28 October 2026 Investment Minister Johari Abdul Ghani told Parliament the new rule. A data centre gets grid power only if Tenaga's **reserve margin**, the spare generating capacity kept above peak demand, has room after other industry. Otherwise it must build its own power off the grid, with the energy ministry's approval. Of the 117 data centres Malaysia has approved, 27 will take their power that way, and 24 new applications are held. The Deputy Prime Minister added that every data centre must take at least 30 per cent of its capacity or energy from renewables.

The minister also gave the number behind the rule. If all 117 approved centres are completed, he said, they would need "about 23,000 or 23,500 megawatts", an oral estimate given without its basis. Peninsular Malaysia's highest demand ever, set on 6 August 2026, was 22,014 megawatts. The approved data centres alone would need about as much power as the whole peninsula uses at its peak.

{{FIG7}}

Supply is moving further away. Tenaga is retiring 6.6 gigawatts of its own power stations by 2030, and the original 2,100 megawatt Tanjung Bin coal station in south-west Johor retires in 2031, according to grid operator data reported by The Edge. The bids reported for the gas plants to replace them, tendered as NEWGEN26, are all outside Johor. Tenaga is building a new 500 kV backbone of about 500 kilometres, from Paka on the east coast to Kulai East in Johor, due by 2030.

<a id="phantom-load"></a>

Here is the question I cannot yet answer, and it matters for anyone valuing a Johor booking. An engineer sizing a grid does not add up every customer's maximum, because loads rarely peak together. An allocation queue does add them up, because each booked megawatt is a promise the planner must keep. If the spare-margin test counts bookings rather than expected draw, the 4.4 gigawatts booked and idle could use up the margin on paper while wires and turbines sit half used. The record fits that reading without proving it: the 24 new applications are parked, and press reports describe operators now submitting ten-year staggered projections and receiving grid access in phases. If planning counts bookings, the cheapest new gigawatt in Johor is a reclaimed booking, not a new substation. Nothing published yet says which it counts.

## Is water the next gate, and can own power get round the queue?

Water is now a stated gate of its own, and own power moves the queue rather than removing it.

<a id="johor-waits-on-the-treatment-plant"></a>

In 2025 Johor's plants could treat about 2,375 million litres of water a day against demand of 2,034, a reserve margin of 14.3 per cent, according to SPAN, the national water regulator. That leaves about 340 million litres a day spare, on my arithmetic. In November 2025 a government written answer, as reported, put Johor's data centre water demand at 384 million litres a day by 2030, on planning permissions already granted: about the size of that spare. Since October 2026, areas with a low water reserve margin "will not be considered" for data centres.

American AI builders often escape grid queues by putting gas power on site, as [Building your own power](/journal/building-your-own-power/) explains. In Singapore that buys nothing that matters, because the licence states the computing load a hall may run, not its power. In Malaysia own power is now the official answer for those the grid will not serve, but it needs its own gas, plant and permits, plus the 30 per cent renewable rule. Own power gets round a queue; it does not get round a ration.

## Why is Hong Kong the opposite case?

Because Hong Kong's utility is obliged to build to demand, so the plug is open, and the gate that binds is the American chip licence.

<a id="hong-kong-has-the-plug"></a>

CLP Power, the utility for Kowloon and the New Territories, works under a **Scheme of Control**, its regulatory deal with the government. It obliges CLP to meet demand in return for a regulated return on what it builds, to 2033. At the end of 2025 it had 9,258 megawatts of capacity for Hong Kong customers against a highest local demand of 7,455 megawatts, about a quarter to spare. Its data centre customers drew an average of about 283 megawatts in the first nine months of 2026, on my arithmetic, and it plans 18 data centre substations in its 2024 to 2028 Development Plan.

{{FIG8}}

<a id="the-second-gate-is-beijing"></a>

The plug is not the problem; the chip is. Since December 2020 American export rules have treated Hong Kong as China. Since 15 January 2026 chips up to the class of Nvidia's H200, shipped from 2024, can be licensed case by case for end users in China; anything more powerful is presumed denied. So a Hong Kong hall is capped about two chip generations behind the frontier, however much power it has. Press reports in August 2026 even put hundreds of thousands of H200s in Hong Kong, kept there while Beijing limits their import to the mainland. The chips are physically there and still not running.

<a id="gates-in-series"></a>

Put the three cities side by side and the lesson for an investor is which number to read. In Johor, read draw against booking. In Singapore, read the licence and the calls. In Hong Kong, read the chip rule.

## So who holds the scarce thing, and what should an investor watch?

Whoever holds a right to draw: a Singapore licence, a Johor booking with a live plug, or a place inside Malaysia's spare margin.

That points the value at three places, whoever wins each campus. **Halls with a live plug** are paid on take-or-pay contracts for capacity, with power passed through, so a hall can be energised, let and earning while drawing little. **The keeper of the margin**, Tenaga, earns its regulated return on the wires and charges idle bookings. **The plant on the slow clock**, the makers of transformers, switchgear and subsea cable covered in [The equipment queue](/journal/the-equipment-queue/), is paid by every winner.

Five numbers carry the story, each published on a schedule. Tenaga's quarterly data centre draw against maximum demand in its system. Any Johor-only split of that draw. Whether the spare-margin test counts bookings or expected draw. Singapore's next call, which will be reviewed 18 to 24 months from August 2026. And any change in the American chip rules, above all a law reaching remote access.

## What would prove me wrong

Two tests break the claim. If Tenaga's briefing for June 2027 shows Malaysia's data centres drawing 40 per cent or more of the maximum demand of the data centre projects in its system, halls are filling about as fast as they connect, and the plug is not the scarce thing. On trend they fall short: if load doubles again to about 2.5 gigawatts while most of the 2.21 gigawatts under construction connects, the share is roughly a third.

The second test is the policy. If, before the end of 2027, Malaysia lets new data centres connect to the grid again without the spare-margin test, the government no longer treats the plug as scarce, and the ration was a pause, not a regime.

One event would move me before either test. Regulators clawing back idle bookings would shrink the bottom of Tenaga's ratio and could push the share over 40 per cent without one more chip racked; I would mark the test broken and say why. Faster draw growth on its own would not move me: draw more than doubled in a year and the share still crept, because bookings grew too.

