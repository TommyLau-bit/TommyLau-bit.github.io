# Switchgear inside the fence: the electrical chain from substation to rack

Research for the depth rebuild of "The equipment queue". Gathered 7 November 2026. Not for publication as is.

Tags on every fact: **primary** (company filing, results release, own investor-day transcript, regulator, standards body, Uptime, DOE/NREL/CRS), **call** (said on an earnings call, read through third-party coverage, not the company's own text), **press** (trade press, analyst, aggregator), **calc** (my arithmetic). No share prices, valuations or views on shares anywhere below.

---

## 1. The chain in plain terms

Power arrives at the fence at transmission or sub-transmission voltage and is stepped down, switched, protected, backed up and divided five or six times before it reaches a server. Each step is a separate box from a separate factory, and each has its own queue.

| Step | What it does (plain English) | Typical rating | Who makes it | Source / tag |
|---|---|---|---|---|
| 1. Utility or campus substation: high-voltage breakers, disconnects | The main switch and fuse for the whole site: opens in a few hundredths of a second if a fault occurs on the grid side | 69 to 500 kV; breakers to 800 kV | Hitachi Energy, Siemens Energy, GE Vernova, Mitsubishi Electric, Toshiba, Hyosung (US JV with Quanta), Meidensha (vacuum, MV/HV), Pennsylvania Switchgear | Ratings: IEEE C37 / IEC 62271 classes (standards, not opened); Hyosung HICO Breaker LLC "up to 800 kV" (Quanta 8-K Ex 99.1, June 2026, primary) |
| 2. Power transformer at the substation | Steps transmission voltage down to medium voltage (typically 13.8 kV or 34.5 kV in the US) | Tens to hundreds of MVA | Hitachi Energy, Siemens Energy, GE Vernova/Prolec, HD Hyundai, Hyosung, WEG and others (covered in transformers.md) | 13.8 kV is the input Nvidia quotes for its 800 VDC design (Nvidia blog, 20 May 2025, primary) |
| 3. Medium-voltage (MV) switchgear | The site's main distribution board at 5 to 38 kV: a row of metal cabinets with breakers that route power to each data hall and isolate faults | 5 to 38 kV (US ANSI classes 15 kV, 27 kV, 38 kV) | Eaton, Schneider Electric, ABB, Siemens, Powell, nVent (via Maverick Power, Oct 2026), Legrand (partly), Mitsubishi, Meidensha | Schneider Mt. Juliet makes MV "air-insulated switchgear (AIS), gas-insulated switchgear (GIS)" (release 11 Nov 2025, primary); nVent: Maverick makes "Medium-voltage switchgear" (Q3 2026 deck, 30 Oct 2026, primary) |
| 4. Unit substation / dry-type or pad-mount transformer | Steps MV down to low voltage, in the US usually 480 V (415 V in Europe-style designs), one unit per block of load | Typically 2 to 3.5 MVA each | Eaton (Jonesville plant from 2027), Schneider, ABB, Siemens, Hitachi Energy, Hammond, many regional makers | Eaton Jonesville "three-phase transformers", production 2027 (in live piece, primary); size range is industry norm, not opened |
| 5. Low-voltage (LV) switchgear and switchboards | Distributes 480 V to UPS, cooling and halls; contains the air circuit breakers and moulded-case breakers | Up to about 6,000 A per lineup | Eaton, Schneider (Columbia, Missouri breakers), ABB (Emax 3 breakers, Senatobia), Siemens, nVent/Maverick, Legrand, Hubbell (components) | nVent: Maverick makes "Low-voltage switchgear" (deck, primary); ABB $15m Emax 3 line Senatobia (press) |
| 6. UPS and batteries | Bridges the seconds between a grid fault and the generator starting; conditions power | Modules of 0.5 to 1.25 MW, paralleled | Vertiv, Schneider, Eaton, ABB, Legrand, Delta, Huawei | Uptime: UPS failures are the top power-related cause of outages, 42% (Global Data Center Survey 2025, citing its Resiliency Survey, primary) |
| 7. Busway, PDUs, remote power panels, static transfer switches | Carry power along rows and into racks; switch between two feeds | Busway to about 6,000 A; rack PDU tens of kW | Eaton (Henrico campus, PDUs, STS, RPPs, from 2027), Legrand, Vertiv, Schneider, nVent, Hubbell | Eaton Henrico: "static transfer switches, power distribution units, and remote power panels", 350,000 sq ft, production 2027 (release 10 Dec 2025, read via press) |
| 8. Backup generators | Diesel (sometimes gas) engines that carry the site if the grid fails for minutes to days | 2 to 3.5 MW per set, dozens per campus | Caterpillar, Cummins, Rolls-Royce (mtu), Generac, Kohler/Rehlko, Mitsubishi Heavy | Ratings industry norm, not opened; maker figures in section 3 |
| 9. 800 V DC and solid-state transformers (new, AI racks) | Replace the AC chain from MV to the rack with one conversion to 800 V DC at the edge of the hall, fed to MW-scale racks | 1 MW racks "starting in 2027" | Nvidia ecosystem: Eaton, Schneider, Vertiv (May 2025); later ABB, GE Vernova, Hitachi Energy, Siemens, Mitsubishi Electric, Heron Power, Delta (press) | See table 1b |

Note: the ratings in steps 1 and 3 to 8 are engineering norms I have not tied to a document; a standards citation (IEEE C37.20.2 for MV metal-clad switchgear, IEEE C37.20.1 for LV switchgear, ANSI C84.1 for 480 V) should be added before any number is printed.

### 1b. The 800 V DC plan, dated

| Date | What | Figure | Source | Tag |
|---|---|---|---|---|
| 20 May 2025 | Nvidia announces 800 VDC architecture; 13.8 kV AC converted "directly to 800 VDC at the data center perimeter" using industrial rectifiers; SSTs studied as one of two options | Full-scale production to "coincide with NVIDIA Kyber rack-scale systems in 2027"; 1 MW racks "starting in 2027" | https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/ | primary |
| 20 May 2025 | Why: 54 V in-rack busbars hit limits above 200 kW per rack | A 1 MW rack at 54 V "requires up to 200 kg of copper busbar"; up to 200,000 kg in a 1 GW site; up to 64U of a Kyber rack for 54 V power shelves | same | primary |
| 20 May 2025 | Claimed gains | 85% more power through the same conductor; copper down 45% vs 415 VAC; up to 5% efficiency; maintenance up to 70% lower; TCO up to 30% lower | same | primary (Nvidia's own projections) |
| 20 May 2025 | Partners named | Data centre power systems: Eaton, Schneider Electric, Vertiv | same | primary |
| 19 May 2025 | Vertiv 800 VDC portfolio | "scheduled for release in the second half of 2026" | Vertiv release (vertiv.com news release, "Vertiv accelerates AI infrastructure evolution ...") | primary; no 2026 confirmation found |
| 20 Aug 2025 | Eaton completes Resilient Power Systems (MV solid-state transformer developer) | Terms not disclosed | Eaton release 16 Jul 2025 (businesswire 20250716246545); close 20 Aug 2025 per press | primary (signing) / press (close) |
| 11 Dec 2025 | Schneider CMD: SST not before 2027 | Frederic Godemel: "Up to 2027, we don't see at large new technology like [SST]"; "you still have power conversion, you still have battery" | Schneider CMD transcript, https://www.se.com/ww/en/assets/pdf/capital-markets-day-transcript | primary |
| 11 Dec 2025 | Schneider: rack density now | "north of 130 kilowatts of rack", moving to "a megawatt per" rack (Rich Whitmore, Motivair) | same | primary |
| 20 Oct 2026 | ABB Infinitus DC portfolio | "a Solid State Transformer commercially available in the second half of 2027" | ABB Q3 2026 release, https://www.eqs-news.com/news/category/abb-ltd-q3-2026-results/50d2285d-3931-4dd6-87c9-175ebf9be15a_en | primary |
| Aug 2026 | OCP SST specification v0.3 shared by Nvidia, Google, Microsoft; staged roll-out (hybrid rack H2 2026, row power centre 2027, up to 2 MW per row) | | Data Center Richness / IT Brief | press, not confirmed at Nvidia |

Plain-English point for the piece: at 54 V a 1 MW rack would draw about 18,500 A; at 800 V about 1,250 A (calc, I = P/V). Current, not voltage, sets the copper. That is the whole case for 800 V DC.

What 800 V DC does to the equipment queue (my inference, label as such): it removes some low-voltage AC gear (rack power shelves, some PDUs, possibly LV switchboards and UPS in their current form) and adds rectifiers, DC busway, DC breakers and possibly SSTs. It does not remove the substation, the MV switchgear or the generators. Schneider's own engineer says the "building blocks will be there". So it reshuffles the inside-the-fence order book from about 2027; it does not shorten the grid-side queue.

---

## 2. How much electrical equipment per MW, and why AI racks change it

| Figure | Value | Date | Source | Tag |
|---|---|---|---|---|
| Schneider's revenue opportunity per MW of new data centre | "$1.2 million to $3.3 million per megawatt"; for the most complex AI sites it would not expect "to trend to the top of that range" | 11 Dec 2025 | Schneider CMD transcript (Hilary Maxson, CFO), se.com | primary |
| Schneider data centre exposure | "pure data center of 25% with networks at 4%" of group revenue, expected at end 2025; pure data centre to grow 12% to 14% a year 2025 to 2030 | 11 Dec 2025 | same | primary |
| Schneider data centre portfolio split | Secure power systems 32% (three-phase UPS, prefab, electrical distribution, LV/MV); lifecycle services 16% | 11 Dec 2025 | same | primary |
| Eaton data centre content per MW | About $3.4m per MW (up from $2.9m, with Boyd Thermal) | Q2 2026 call, 31 Jul 2026 | MarketBeat / Kavout summaries | call / press; Eaton's own slide not opened |
| nVent data centre opportunity per MW | "~$2M / MW with Maverick Power" | 30 Oct 2026 | nVent Q3 2026 deck, https://s22.q4cdn.com/268397047/files/content_files/2026-Q3-Earnings-Deck.pdf | primary |
| Vertiv content per MW (power and cooling) | $2.5 to 3m traditional; $3 to 3.5m high density | Investor event 18 Nov 2024 | Wallstreetcn via Longport; Investing.com | press; slide not found |
| All-in US data centre build cost | Average $11.7m per MW across 19 markets (2025 guide); 2026 guide $8.9m to $23.3m per MW, costs up 21% per MW since late 2024, excluding chips | 2025 and 2026 guides | Cushman & Wakefield via IREI / CRE Daily | press (guide not opened) |
| Electrical share of build cost | 40% to 45% | undated | Dgtl Infra via aggregator | press, weak |
| Average rack today | Average modal density "almost 9 kW", up from 8.3 kW; 7.5 kW excluding sites at 30 kW+; "More than 80%" of operators have no racks above 30 kW | Survey Apr to May 2025, published Jul 2025 | Uptime Institute Global Data Center Survey 2025, https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2025.Annual.Survey.Report.pdf | primary |
| GB200 NVL72 rack | "up to 132 kW per rack" (Schneider/Nvidia reference design) | Dec 2024 | Schneider release, businesswire 20241210368442 | primary (search snippet, release not opened in full) |
| Vera Rubin NVL72 rack | About 190 to 230 kW (estimates) | 2026 | hashrateindex, spheron | press, no Nvidia figure found |
| Kyber / Rubin Ultra NVL576 | About 600 kW per rack (stated at GTC March 2025 keynote); 1 MW racks from 2027 (Nvidia blog) | 2025 | keynote via press; blog primary | press / primary |

Calcs:
- GB200 rack (132 kW) is about 15 times Uptime's average rack (about 9 kW); a 1 MW Kyber-class rack is about 110 times (calc).
- A 100 MW hall at 9 kW is about 11,000 racks; at 132 kW about 760 racks (calc). Same MW, same substation, same MV switchgear, same generators per MW; far fewer racks, far more power per row. So per MW, AI changes the low-voltage end (busway, PDUs, power shelves, liquid cooling) much more than the grid end.
- Schneider's $1.2m to $3.3m per MW is its own addressable content, not the whole electrical bill; against Cushman's $11.7m per MW average that is about 10% to 28% (calc, mixing two sources, illustration only).

Why AI changes the amount (sourced points): (1) density moves the bottleneck to LV distribution and copper (Nvidia, 200 kg per MW rack); (2) Schneider says the most complex AI sites will not trend to the top of its per-MW range, because design optimises "token per watt" (CMD); (3) GPU power swings need energy storage at sub-second scale (Nvidia blog, "Energy storage solutions to help data center infrastructure handle load spikes"); (4) the per-MW figures from Schneider, Eaton, nVent and Vertiv are each company's opportunity, not comparable with each other.

---

## 3. Makers' latest primary figures (to 7 November 2026)

### 3a. Inside-the-fence electrical

| Maker | Period, date reported | Orders | Backlog | Sales / growth | Data centre line | Source | Tag |
|---|---|---|---|---|---|---|---|
| Eaton, Electrical Americas | Q3 2026, 3 Nov 2026 | Rolling 12-month organic orders +39% | Up 33% y/y ($15,993m per 10-Q, as in live piece) | $4.2bn record (Note 3: $4,172m vs $3,410m), +22% organic; margin 29.8% | Release gives no data centre figure; call: data centre sales +54% | 8-K Ex 99, https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm ; 10-Q https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000040/etn-20260930.htm | primary; +54% call |
| Eaton, Electrical Global | Q3 2026 | Rolling 12-month organic orders +51% | +121% (includes Boyd Thermal) | $2.7bn ($2,727m), +58% (27% organic, 31% Boyd); margin 21.1% | | same | primary |
| Eaton, total Electrical | Q3 2026 | Rolling 12-month book-to-bill 1.2 | +46% y/y | | | same | primary |
| Eaton, whole company | 30 Sep 2026 | | About $26.2bn; "approximately 72% ... targeted for delivery ... in the next twelve months" (so about 28% later: calc) | Capex $721m 9M 2026 vs $527m | | 10-Q Note 3 and cash flow | primary |
| Eaton, deals | | | | Boyd Thermal closed 12 Mar 2026 ($9.55bn net); COL Group (MV distribution products) agreed 25 Sep 2026, €810m, close Q1 2027; Fibrebond (modular power enclosures) 1 Apr 2025, $1.43bn | | 8-K Ex 99 | primary |
| Schneider Electric | Q3 2026, 16 Oct 2026 | Pure data centre demand "up triple-digit globally" | "another record backlog"; no figure; backlog "providing increasing visibility into 2027 and 2028" | €11,460m, +16.9% org; Energy Management +18.8% org; North America (40% of revenue) +19.9% org; Products +17% "majority volume-driven" | Data centre sales "up strong double-digit"; prefab a key driver | https://www.webdisclosure.com/press-release/third-quarter-revenues-2026-odiihfxJLgs | primary |
| Schneider, softness in same release | Q3 2026 | "Power & Grid (P&G) demand declined slightly"; "Industry and Infrastructure were down overall" (NA Energy Management) | | | | same | primary |
| ABB, group | Q3 2026, 20 Oct 2026 | $12,055m, +40% comparable; book-to-bill 1.24 | Group $32.3bn, +37% comparable (Quartr) | Revenue $9,701m, +14% | Data centre segment "triple-digit increase" | ABB release via EQS | primary; backlog press |
| ABB, Electrification | Q3 2026 | About $7.67bn, +70% comparable; Americas +117% | About $16.0bn (Q2 $13.7bn) | About $5.2bn, +19% comparable (Yahoo call summary) | Orders ex data centres up high teens; data centre lead times "12 to 24 months" (call) | Futurum, Investing.com, Utility Dive | press; NOT confirmed against ABB's segment table |
| ABB capex | | "around $1 billion and do not expect it to rise further in the mid-term"; "incremental capacity expansion ... selectively leveraging third-party assembly" | | | | ABB release | primary |
| Vertiv | Q3 2026, 28 Oct 2026 | "more than 100% organic orders growth year over year"; no dollar figure; book-to-bill 2.9 (call) | Not disclosed quarterly; last $15.0bn at 31 Dec 2025, +109% | $4,313m, +61% (55% organic); Americas +66% organic; FY2026 guide $14,650m, +38% organic | Capex about 4% of revenue | Release PDF, https://s205.q4cdn.com/554782763/files/content_files/Vertiv-Third-Quarter-2026-Earnings-Release.pdf ; Q4 2025 release 11 Feb 2026 | primary; 2.9 is call |
| Vertiv disclosure change | Feb 2026 | Will no longer report orders or backlog quarterly; full year in 10-K | | | | Q4 2025 call (Motley Fool transcript) | call |
| Siemens, Smart Infrastructure | Q3 FY2026, 6 Aug 2026 | €8.0bn, +42% comparable, quarterly record, "driven primarily by the electrification and electrical products businesses, which won several large orders from data center customers in the U.S. and Europe" | | €6.4bn, +13% comparable; margin 20.0% "due primarily to higher revenue, improved capacity utilization" | Data centre orders "around €6 billion" in nine months, triple-digit growth | Siemens release, https://assets.new.siemens.com/siemens/assets/api/uuid:84d1a90b-542e-4775-a907-06f29940eb71/HQCOPR202608037434EN.pdf | primary; Q4 FY2026 not out on 7 Nov |
| Legrand | H1 2026, 29 Jul 2026 | | | Organic +9.8% | Datacentres organic growth above 30%, 32% of revenue; CEO expects about 30% for 2026 | Business Wire 20260728474035 (403 on fetch) via electricaltrends, Reuters | press; nine-month 2026 not found |
| Hubbell, Electrical Solutions | Q3 2026, 27 Oct 2026 | "Orders and end market demand remained strong, driving continued backlog build" | Not given | $845m, +51% (22% organic, 29% acquisitions) | CEO: "led by strong datacenter markets and bolstered by content gains and capacity expansion investments"; data centre sales >80% organic (press) | 8-K Ex 99.1, https://www.sec.gov/Archives/edgar/data/0000048898/000162828026067421/exhibit991_10272026.htm | primary; >80% press |
| Hubbell, Utility Solutions | Q3 2026 | | | $1,028m, +9% (about 5% organic); Grid Infrastructure +13%; Grid Automation -4% (meter component shortage) | | same | primary |
| nVent | Q3 2026, 30 Oct 2026 | "Record orders, grew low double digits" | $2.6bn, up sequentially | $1,515m, +44% organic | Maverick Power closed 1 Oct 2026: LV and MV switchgear for data centres; ~$2m per MW | Release https://www.sec.gov/Archives/edgar/data/0001720635/000162828026068391/q32026nvtpressrelease.htm ; deck | primary |
| Powell Industries | Q3 FY2026 (to 30 Jun 2026), 3 Aug 2026 | "a record $934 million of new orders", +158%; book-to-bill 3.0 | $2.4bn, +69% (from $1.6bn at 31 Dec 2025) | Revenue $312m, +9% | One data centre order "exceeding $400 million", "behind-the-meter design of on-site generation assets"; Jacintoport yard expansion due by end FY2026; "evaluating greenfield capacity expansions" | 8-K Ex 99.1, https://www.sec.gov/Archives/edgar/data/0000080420/000008042026000103/ex991-powlq3xfy2026earning.htm | primary; Q4 FY2026 not out (last year 18 Nov) |
| GE Vernova, Electrification | Q3 2026, 28 Oct 2026 | $5.4bn, -9% organic (prior-year synchronous condensers); book-to-bill about 1.4 | Equipment backlog $40.6bn at Q2 (incl. $5bn Prolec GE) | | H1 2026 data centre orders over $5bn (call) | 8-K, https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm | primary; H1 DC call |

### 3b. Backup generation

| Maker | Period, date | Figure | Source | Tag |
|---|---|---|---|---|
| Caterpillar | Q3 2026, 29 Oct 2026 | Total backlog about $78.1bn, up about $6.0bn on Q2, largest increase in Power & Energy; Power Generation sales $3.42bn, +30%, mainly turbines and large reciprocating engines "primarily in data center applications" | 10-Q https://www.sec.gov/Archives/edgar/data/0000018230/000001823026000057/cat-20260930.htm ; release via Manufacturing Dive | primary (backlog), press for segment wording |
| Caterpillar | Q3 2026 | Unsatisfied obligations on contracts over one year $49.4bn, "about one-third" in next 12 months (so about two-thirds later: calc) | 10-Q Note 3 | primary |
| Caterpillar | Q3 2026 call | Accepting "certain large reciprocating engine orders into 2029 and turbine orders into 2030"; capacity the main constraint | MarketBeat / sec-api summaries | call |
| Caterpillar | 2024 | $725m Lafayette, Indiana large-engine plant expansion | Equipment World, CompressorTech2 | press |
| Cummins, Power Systems | Q3 2026, 5 Nov 2026 | Sales about $2.3bn, +15%; EBITDA $582m, 25.4%; "Global demand for power generation equipment remains exceptionally strong, driven by data center buildout"; BESS award for "a large U.S. data center project" | 8-K Ex 99, https://www.sec.gov/Archives/edgar/data/0000026172/000002617226000035/cmi2026q38-kex99.htm | primary |
| Cummins | Q2 2026 call, 4 Aug 2026 | 2026 growth "constrained by available capacity for larger generator-set configurations" | MarketBeat | call |
| Generac | Q3 2026, 28 Oct 2026 | Net sales $1.29bn, +16%; data centre backlog "approximately $4.5 billion" (about $1.6bn three months earlier, press); Amazon agreement, "initial deliveries are expected to total a combined $2.4 billion in 2027 and 2028"; risk factor: "increase in contract risk related to terms with certain data center customers, including cancellation rights" | 8-K Ex, https://www.sec.gov/Archives/edgar/data/0001474735/000143774926033685/ex_1032565.htm | primary |

### 3c. Statements that orders are slowing or lead times shortening

| Who | Statement | Date | Tag |
|---|---|---|---|
| nVent | Orders "grew low double digits", second quarter running (65% a year earlier, press) | 30 Oct 2026 | primary / press |
| GE Vernova Electrification | Orders -9% organic, attributed to a large prior-year base; book-to-bill still about 1.4 | 28 Oct 2026 | primary |
| ABB CEO | Record orders cannot be promised every quarter | 20 Oct 2026 call | call |
| Eaton Electrical Americas | Backlog / trailing sales flat at 1.05 (June and Sept), while total Electrical backlog +46% | 3 Nov 2026 | primary + calc (live piece) |
| Schneider | Power & Grid demand "declined slightly"; NA Industry and Infrastructure down | 16 Oct 2026 | primary |
| Vertiv | Stops disclosing orders and backlog quarterly, so a slowdown would not be visible until the 10-K | Feb 2026 | call |
| Generac | Flags cancellation rights in data centre contracts | 28 Oct 2026 | primary |
| Uptime | "some of the more severe supply chain issues are easing" (secondary paraphrase of survey) | Jul 2025 | press |
| Distribution transformers | Wait fell to about 30 weeks by Q2 2025 from about two years in 2024 (Wood Mackenzie via CRS) | CRS, 23 Apr 2026 | primary (CRS) citing consultancy |

No maker in my slice said in its own text that switchgear, UPS or generator lead times are shortening. Several (Caterpillar, Cummins, ABB) said the opposite on calls.

---

## 4. Lead times and prices

Primary statements on lead times inside the fence are scarce: no maker in this slice publishes a switchgear, UPS or generator lead time in its filings. What exists:

| Item | Figure | Date | Source | Tag |
|---|---|---|---|---|
| ABB data centre deliveries | Lead times 12 to 24 months, so 2026 intake ships 2027 to 2028 | 20 Oct 2026 | Futurum (call) | call |
| Eaton, all segments | 72% of $26.2bn backlog for delivery within 12 months | 30 Sep 2026 | 10-Q | primary |
| Caterpillar large engines / turbines | Orders accepted into 2029 / 2030 | 29 Oct 2026 | call | call |
| Caterpillar contracts over one year | About one-third of $49.4bn in the next 12 months | 30 Sep 2026 | 10-Q | primary |
| Generac / Amazon | Deliveries 2027 and 2028 for an order signed in 2026 | 28 Oct 2026 | 8-K | primary |
| Schneider | Backlog gives "visibility into 2027 and 2028" | 16 Oct 2026 | release | primary |
| Distribution transformers (pad-mount, the unit-substation class) | Up to 2 years in 2024, "a fourfold increase compared to pre-2022"; prices up 5 to 6 times in two years (NREL abstract); about 30 weeks by Q2 2025 (WoodMac via CRS) | Feb 2024; Apr 2026 | NREL, Major Drivers of Long-Term Distribution Transformer Demand (https://research-hub.nrel.gov/en/publications/major-drivers-of-long-term-distribution-transformer-demand/); CRS R48933 | primary |
| Transformer prices (PPI) | Roughly 40% from 2020 to 2024 (BLS PPI WPU11740999, as CRS reports it) | 23 Apr 2026 | CRS R48933, https://www.everycrsreport.com/files/2026-04-23_R48933_e69524fc8f52951a242ed35c91713fade25fe8ac.html | primary |
| HV breakers | About 125 weeks (Wood Mackenzie data) | 2025 | trade press | press |
| HV breakers, one US maker | 33 to 35 weeks quoted by Pennsylvania Switchgear | 2025 | Switchgear Magazine | press (maker's own marketing) |
| MV switchgear (15 kV) | 52 to 80 weeks; 38 kV 78 to 104 weeks (Terrapin June 2026); JLL US average about 43 weeks; SourceBlue 28 to 48 weeks MV | 2026 | Industrial Sage, Data Center Scope | press, conflicting, contractor data |
| MV switchgear prices | Up about 50% (Wood Mackenzie) / 45% to 50% since 2020 | 2025 | trade press | press |
| Large diesel gensets (>1.25 MW) | 52 to over 105 weeks | 2026 | eIndustrify | press, weak |

For the piece: the honest primary statement is the shape, not a number. Orders signed in 2026 are scheduled for 2027 and 2028 delivery at ABB, Generac, Schneider and Caterpillar, by their own words. That is a one to three year wait inside the fence, shorter than the grid transformer's but of the same kind.

---

## 5. High-voltage circuit breakers and SF6

What SF6 is: sulphur hexafluoride, the gas that quenches the arc inside most high-voltage breakers and gas-insulated switchgear. It is the strongest greenhouse gas known, GWP 24,300 (IPCC AR6, quoted by Germany's UBA, primary).

| Item | Figure | Date | Source | Tag |
|---|---|---|---|---|
| EU F-gas Regulation (EU) 2024/573, Art. 13(9): ban on putting into operation new switchgear using F-gases | MV up to 24 kV: 1 Jan 2026. MV above 24 kV to 52 kV: 1 Jan 2030. HV above 52 kV to 145 kV (up to 50 kA): 1 Jan 2028. HV above 145 kV or above 50 kA: 1 Jan 2032. HV classes framed as GWP below 1 | Regulation 2024 | ESB Networks, UBA factsheet, Spanish ministry guide, ABB; EUR-Lex text not opened | primary-derived (regulator/TSO pages); confirm against EUR-Lex |
| Trigger | Date of putting into operation; orders before 11 Mar 2024 unaffected; derogation if no suitable alternative was available | | UBA | primary |
| Servicing | From 1 Jan 2035 only reclaimed or recycled SF6 for maintenance | | UBA, https://www.umweltbundesamt.de/en/topics/climate-energy/fluorinated-greenhouse-gases-fully-halogenated-cfcs/application-domains-emission-reduction/switchgear | primary |
| Supply effect, EU | Italy, Bulgaria and Czech Republic warn that without an ecodesign act, fluoronitrile-based SF6-free gear is also banned at the 2028 and 2032 dates, leaving "only one manufacturer of dry-air solutions ... with a manufacturing capacity lower than the European demand"; TSOs "must place orders in 2025-26 (today)"; EU market for SF6-free HV switchgear "approaches €1 billion per year and could exceed €3 billion by 2030"; Commission postponed the switchgear ecodesign act to 2028 | Council note 24 Jun 2026 | Council of the EU ST 10693/1/26 REV 1, https://data.consilium.europa.eu/doc/document/ST-10693-2026-REV-1/en/pdf | primary |
| Who is which (my reading, not in the note) | Dry air / vacuum: Siemens Energy (Blue); fluoronitrile (g3 / C4-FN): GE Vernova, Hitachi Energy (EconiQ) | | maker product pages | to confirm |
| California (CARB) | Amended 2021, effective 1 Jan 2022: phases out acquisition of new SF6 gas-insulated equipment, starting 1 Jan 2025 and running through 2033 by voltage class; schedule set where "two or more manufacturers" said non-SF6 gear would be available, plus three years | 2022 | CARB, https://ww2.arb.ca.gov/es/our-work/programs/elec-tandd/about ; EPA state page; Trinity Consultants | primary (class dates not opened; 17 CCR 95352 tables to be read) |
| New York | Voltage-based phase-out of SF6 GIE from 2027; 1% system emission limit from 2030 | | EPA, https://epa.gov/eps-partnership/state-and-regional-regulations-related-sf6-emissions-electric-transmission-and | primary |
| Hitachi Energy EconiQ 420 kV | First fully tested SF6-free 420 kV breaker (63 kA, 5,000 A); first US install at Eversource 345 kV | 2022 | Hitachi Energy release 30 Aug 2022 | primary |
| New US HV breaker capacity | Hyosung HICO Breaker LLC with Quanta, Canonsburg, Pennsylvania, gas circuit breakers up to 800 kV | Jun 2026 | Quanta 8-K Ex 99.1, https://www.sec.gov/Archives/edgar/data/0001050915/000119312526324855/d56853dex991.htm | primary; start date conflicting (press: Oct 2026) |
| Hyosung target | 25% of US HV gas breaker market by 2030; semi-finished parts from Changwon | 2026 | Switchgear Magazine, Korea Times | press |
| Siemens Energy | New HV switchgear plant, Greater Richland, Mississippi, no date | 3 Feb 2026 | Siemens Energy release (in live piece sidecar) | primary |
| Meidensha | $9.3m Gray Court, SC vacuum breaker expansion, due May 2026 | Oct 2025 | SC governor's office | primary-ish |

Plain point: an AI campus with its own substation needs HV breakers from the same handful of makers as the utilities, and in Europe those makers are retooling to a new gas or to vacuum at the same time as demand peaks. The EU's own member states say the 2028 ban could leave one dry-air supplier short of capacity. That is a second, regulatory queue for breakers, separate from the transformer queue.

---

## What the live piece has wrong or out of date (my slice only)

1. **The inside-the-fence chain is almost absent.** The piece explains the transformer in depth but gives switchgear one line ("like a block of flats' fuse box"). There is no UPS, busway, generator or 800 V DC step, and no sense that each box has its own queue. A first-time investor cannot tell what Eaton, Vertiv or Schneider actually sell.
2. **Generators are missing entirely.** Caterpillar (engine orders into 2029, call), Cummins ("constrained by available capacity for larger generator-set configurations", call) and Generac ($4.5bn data centre backlog, deliveries 2027 to 2028, primary) are the clearest inside-the-fence queue, and none is in the piece or the exposure map.
3. **"Eaton's gear mostly ships within a year"** is right in substance but should be sourced and dated: 72% of Eaton's $26.2bn total backlog is targeted within 12 months (10-Q, 30 Sep 2026), so 28% is not (calc).
4. **Eaton book-to-bill.** The piece says Electrical Americas book-to-bill 1.3 over twelve months. Eaton's Q3 release gives 1.2 for total Electrical; I could not confirm 1.3 for Electrical Americas in the text I could read. Recheck the 10-Q MD&A table before keeping 1.3.
5. **"Eaton's ratio has already gone flat"** needs the other half: Eaton's total Electrical backlog rose 46% and Electrical Global's 121% (with Boyd). The flat ratio is one segment.
6. **"Orders cooling" test (second test) is missing current signals.** nVent orders slowed to low double digits for a second quarter; GE Vernova Electrification orders fell 9% organically (book-to-bill still about 1.4); Schneider's Power & Grid demand "declined slightly". None is in the piece; they cut slightly against it and should be conceded.
7. **ABB is in the exposure map but not in the evidence.** ABB's Q3 2026 data centre orders rose triple digits (primary), Electrification orders about +70% (press, segment table not yet confirmed), and ABB says capex will stay "around $1 billion": a maker deliberately not building to clear the queue, which supports the piece's central claim and is not used.
8. **Vertiv can no longer be tested.** It stopped quarterly orders and backlog disclosure (Feb 2026). If Vertiv stays in the exposure map, the piece should say its queue is not observable between 10-Ks. Its book-to-bill of 2.9 in Q3 2026 is a call figure only.
9. **Schneider: two primary facts the piece lacks.** Data centres were 25% (plus networks 4%) of group revenue at end 2025, and Schneider sizes its own content at $1.2m to $3.3m per MW (CMD, 11 Dec 2025). Mt. Juliet MV switchgear plant opened 11 November 2025, so the factory table's "Through 2027" for Schneider is partly delivered.
10. **800 V DC is not mentioned.** Nvidia's own plan (May 2025) has 800 V DC in production with Kyber in 2027; ABB's SST is due H2 2027; Schneider says no SST at scale before 2027. This is the main technical change to the inside-the-fence order book in the piece's test window (to mid 2028) and should be named, with the caveat that it reshuffles low-voltage gear and leaves the substation and MV switchgear in place.
11. **HV breakers and SF6 are absent.** The EU's 2028 ban on SF6 above 52 kV and the June 2026 Council note warning of a single dry-air supplier "with a manufacturing capacity lower than the European demand" are a primary, dated second queue for switchgear that fits the piece's "the slowest station sets the wait" ending.
12. **Exposure map, inside the fence:** add Legrand, Hubbell, nVent, Powell (switchgear and power rooms), and Caterpillar, Cummins, Generac, Rolls-Royce (backup generators). Vertiv's switchgear exposure is narrow (busway and E+I switchgear); describe it as UPS, power and cooling.

## Could not verify today

- ABB Electrification segment orders, backlog and margin for Q3 2026 (ABB's own news page timed out; figures above are press).
- Eaton $3.4m per MW (call only); Vertiv $3 to 3.5m per MW (press of 2024 slide).
- Legrand nine-month 2026 release (not found; likely early November).
- CARB voltage-class dates (17 CCR 95352 tables not opened).
- EUR-Lex text of Art. 13(9) (fetch returned blank; dates confirmed by ESB Networks, UBA and the Spanish ministry guide).
- Typical ratings in section 1 (standards not opened).
- Vera Rubin rack power (no Nvidia figure found).
- Siemens Q4 FY2026, Siemens Energy FY2026 and Powell Q4 FY2026 results: not out on 7 November 2026.
