# Heat and water rebuild: the makers and operators, in their own figures

Research slice for the depth rebuild of `heat-and-water`. Compiled 7 November 2026. Every fact is dated and tagged: [primary] filing, release, company deck or company blog opened; [call] earnings or conference call transcript (company-hosted transcripts are marked [call, company PDF]); [press] lead only, not opened at source; [calc] my arithmetic. Financials are evidence of the physical mechanism only; no share prices, valuations or views on shares.

Big picture in one paragraph: in 2026 the line between "loop makers" (cold plates, CDUs) and "roof makers" (chillers, towers, dry coolers) dissolved. Every large chiller maker bought or built a CDU line (Trane bought LiquidStack, Johnson Controls bought Alloy and makes CDUs, Carrier designed its own), the loop makers bought roof plant (Vertiv bought ThermoKey, a dry-cooler maker, and is doubling chiller capacity), and a water-treatment company bought a CDU maker (Ecolab, CoolIT). Chiller orders are at records, but the chillers being ordered for AI halls are mostly air-cooled, which evaporate no water. The makers say chillers shrink at the margin, not that they disappear.

---

## 1. Liquid cooling makers (the loop: cold plates, CDUs, manifolds)

A **CDU (coolant distribution unit)** is the pump-and-heat-exchanger box between the sealed rack loop and the building's water loop. Carrier's CEO calls it "effectively ... a mini-chiller" (29 Oct 2026, below).

### Vertiv

| Date | Fact | Source | Tag |
|---|---|---|---|
| FY2025 | Portfolio by revenue: Power Management about 35%, Thermal Management about 30%, IT Systems 7%, Infrastructure Solutions 8%, Services and Spares 20%; market segment Data Centers about 85%. The slide prints the percentages in a grid, so the pairing of 35% to Power and 30% to Thermal is my reading of the layout; it sums to 100 either way | 2026 Investor Conference deck, 19 May 2026, p10, https://s205.q4cdn.com/554782763/files/doc_presentations/2026/05/19/Vertiv-2026-Investor-Conference_May-19-2026.pdf | primary (pairing inferred) |
| 19 May 2026 | "#1 in thermal management" (citing Dell'Oro, March 2026) | same, p10 | primary (vendor claim, third-party data) |
| 19 May 2026 | "~$3.25M - $3.75M per MW", "Vertiv Data Center Weighted Mix Opportunity", "Data center $/MW up ~10-15% vs. prior range"; footnote "Management estimates of current dollar per megawatt of IT power". Power and thermal together; no split | same, p31 | primary |
| 19 May 2026 | Deal timeline on one slide: THERMAL: CoolTera (Dec 2023, "direct-to-chip liquid cooling"); THERMAL: BSE (Dec 2024, "Centrifugal chiller technology and heat-recovery"); SERVICES: PurgeRite ("Critical fluid management", Dec 2025); THERMAL: ThermoKey ("Heat rejection and heat exchange technologies", expected close about Q2 2026); THERMAL: Strategic Thermal Labs ("Cold plate design and server-side liquid cooling", Apr 2026); BMarko (structural, Apr 2026) | same, p37 | primary |
| 4 Dec 2025 | PurgeRite (flushing, purging and filtration of liquid cooling loops) closed; about $1.0bn upfront plus up to $250m earnout; total consideration $1,138.3m net of cash | 8-K 5 Dec 2025; Q3 2026 10-Q (via rack-research/makers.md) | primary |
| 27 Apr 2026 | Acquired Strategic Thermal Labs, "a specialist in advanced liquid-cooling technologies"; adds "proven cold-plate design, server-side liquid cooling, and high-density thermal validation expertise". Price not disclosed | Vertiv release, https://investors.vertiv.com/news/news-details/2026/Vertiv-Strengthens-Liquid-Cooling-System-Capability-with-Acquisition-of-Strategic-Thermal-Labs/default.aspx | primary |
| 12 Jun 2026 | Completed ThermoKey (Rivarotta, Italy): dry coolers and microchannel heat exchangers; Vertiv already used ThermoKey technology in its products | Vertiv release (investors.vertiv.com, "Vertiv Completes Acquisition of ThermoKey, Expanding Heat Rejection Portfolio for AI Data Centers"); content read via press copies | primary title, press detail |
| 9M 2026 | About $278m cash on 2026 acquisitions | Q3 2026 10-Q, cash flow ("Acquisition of businesses, net of cash acquired (278.1)") and release p. cash flow table | primary |
| 18 Mar 2026 | CEO Giordano Albertazzi: "We've been growing capacity specifically in the liquid cooling and the service behind that really, really, really rapidly" | 24/7 Wall St interview | press |
| 28 Oct 2026 | Q3 2026: net sales $4,313m, +61% (55% organic, about 6% acquisitions); "more than 100% organic orders growth year over year"; FY2026 guide $14,650m, 38% organic. No thermal or liquid cooling split | Q3 2026 release, https://s205.q4cdn.com/554782763/files/content_files/Vertiv-Third-Quarter-2026-Earnings-Release.pdf | primary |
| 28 Oct 2026 | Albertazzi: "the mix is definitely moving towards liquid cooling in the market"; "It doesn't mean that air cooling is going away"; coordination of "the liquid cooling, the air cooling, and the heat rejection" is the "total thermal chain"; "We are also on track to doubling chiller production capacity by year-end"; expanding "Slovakia campus for power and thermal management" | Q3 2026 call, singjupost transcript, https://singjupost.com/?p=64906 | call |
| 28 Oct 2026 | Asked about "compressors that have been burning out" (Scott Davis, Melius), Albertazzi: "Absolutely, we're not perfect", answered in general quality terms | same | call |
| Feb 2026 onward | Stopped quarterly orders and backlog disclosure; last backlog $15.0bn at 31 Dec 2025; chairman Dave Cote, 28 Oct 2026: "we're not planning to share orders data going forward" | via rack-research/makers.md | call |
| Product | CoolChip CDU range 100 kW to 2.3 MW; CDU 2300 launched in EMEA June 2026 | press | press |

Reading: Vertiv does not disclose liquid cooling revenue. Its own words say the mix shifts to liquid while chiller capacity doubles. Its 2026 deals span every link: cold plate design (STL), loop service (PurgeRite), dry coolers (ThermoKey), chillers (BSE, 2024).

### Schneider Electric (Motivair)

| Date | Fact | Source | Tag |
|---|---|---|---|
| 17 Oct 2024 | Agreed to buy 75% of Motivair for $850m, remaining 25% in 2028 | Schneider release (via press) | press, matches live piece |
| 11 Dec 2025 | Rich Whitmore (Motivair CEO): "we were acquired in March this year" (2025); "now able to start producing liquid cooling hardware in multiple factories around the world"; "Today, we're north of 130 kilowatts of rack and we're moving to ... a megawatt"; "400-kilowatt liquid-cooled racks deployed at scale" | Capital Markets Day transcript (LSEG StreetEvents), pp. 22 to 23, https://www.se.com/ww/en/assets/pdf/capital-markets-day-transcript | primary |
| 11 Dec 2025 | CFO Hilary Maxson: "$1.2 million to $3.3 million per megawatt" opportunity; the most complex AI sites not expected "to trend to the top of that range" | same, p63 (via rack-research/makers.md) | primary |
| 16 Oct 2026 | Q3 2026 revenue €11,460m, +16.9% organic; "Demand within the pure Data Center segment remained very strong, up triple-digit globally"; Systems (35% of revenue) +22% organic "with Data Center driving growth, notably in prefabricated solutions ... continued strength in 3-phase UPS and cooling". No cooling or Motivair figure | Q3 2026 revenues release, copy at https://www.webdisclosure.com/press-release/third-quarter-revenues-2026-odiihfxJLgs | primary |
| May 2026 | Vera Rubin NVL72 reference design: MaxQ 188 kW per rack, MaxP 227 kW per rack, 2.5 MW CDU | Schneider blog, 8 May 2026 (search snippet; the blog returned 403 in an earlier slice) | press |
| 21 Jun 2026 | Nvidia's liquid cooling blog names Motivair, "the advanced cooling division of Schneider Electric", as its only named cooling partner | https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/ | primary |

### Eaton (Boyd Thermal)

| Date | Fact | Source | Tag |
|---|---|---|---|
| 3 Nov 2025 | Agreement to buy Boyd Thermal for $9.5bn; Boyd 2026 sales forecast $1.7bn, of which $1.5bn liquid cooling | Eaton release (403 on fetch; figures from multiple press summaries) | press |
| 12 Mar 2026 | "On March 12, 2026, Eaton acquired Boyd Thermal for $9.55 billion, net of cash acquired"; Boyd "employs more than 6,000 people with manufacturing sites across North America, Asia, and Europe" | Q3 2026 release, Ex 99, https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm | primary |
| Q3 2026 | Electrical Global sales $2.7bn ($2,727m), +58%: 27 points organic, "31% contribution from Boyd Thermal in its second full quarter post-acquisition"; Electrical Global backlog +121%; Electrical total backlog +46% | same | primary |
| Q3 2026 | Boyd's Q3 sales about $535m: 31% of a Q3 2025 Electrical Global base of about $1,726m ($2,727m / 1.58) | [calc] from the release | calc |
| 3 Nov 2026 | Boyd 2026 revenue outlook raised to about $1.9bn (about $1.6bn inside Eaton's 2026 results); Boyd sales +24% on Q2; "nearly triple-digit" growth; Boyd backlog "nearly tripled"; growth attributed to AI and "adoption of liquid-cooling architectures" | Q3 2026 call, MarketBeat and finsee summaries | call (via press) |
| 2025 to 2026 | Eaton per-MW content about $3.4m with Boyd (up from $2.9m) | MarketBeat / Kavout summaries of Q2 2026 call | press; not in Eaton's own text |

Reading: Boyd's forecast rose from $1.7bn at announcement to about $1.9bn within eight months. That is the fastest-moving published liquid cooling figure from any maker.

### Ecolab (CoolIT Systems): new in 2026, not in the live piece

| Date | Fact | Source | Tag |
|---|---|---|---|
| 20 Mar 2026 | Agreement to acquire CoolIT Systems "for $4,750 million, subject to certain adjustments" | Ecolab 10-Q Q3 2026, Note 3, https://www.sec.gov/Archives/edgar/data/0000031462/000162828026068208/ecl-20260930.htm | primary |
| 2 Jul 2026 | "the Company completed its acquisition of CoolIT Systems", paying "$4,627 million in cash, net of cash acquired"; CoolIT is "a pure-play data center liquid cooling company" designing "coolant distribution units, cold plates and direct-to-chip cooling technologies"; sits in Global Water segment, High Tech operating segment | same | primary |
| 2 Jul 2026 | CoolIT year-to-date sales up more than 100%; Ecolab targets $4bn of annual sales in its high tech business by 2030 | Ecolab closing release, https://s204.q4cdn.com/218790897/files/doc_news/Ecolab-Closes-CoolIT-Acquisition-and-Expands-AI-Cooling-Platform-as-Global-High-Tech-Business-Targets-4-Billion-by-2030-2026.pdf (title and figures via search snippets) | primary title, press figures |
| Mar 2026 | About $550m of CoolIT sales expected in the next 12 months | Reuters via BusinessDay, 20 Mar 2026 | press |
| Mar 2026 | KKR: since 2023 CoolIT expanded manufacturing to over 300,000 sq ft and "increased coolant distribution unit (CDU) capacity by 25x" | KKR release, Business Wire 25 Mar 2026 (via press) | press |

### Trane Technologies (LiquidStack): new in 2026

| Date | Fact | Source | Tag |
|---|---|---|---|
| 10 Feb 2026 / 3 Mar 2026 | Agreed and then completed acquisition of LiquidStack (Carrollton, Texas; direct-to-chip and immersion cooling, CDUs). Price not found | Trane release, Business Wire 3 Mar 2026 | primary title (press copies) |
| 5 May 2026 | Donny Simmons: "the factory that we're building in Fort Worth for Stellar, we're also going to be producing CDUs in that factory that would be LiquidStack CDUs" | Oppenheimer conference transcript, Trane IR PDF, https://s2.q4cdn.com/950394465/files/doc_events/2026/May/05/Oppenheimer-Conference-Transcript-2026.pdf | call, company PDF |
| 29 Oct 2026 | Simmons on CDUs: "We've got orders in the pipeline now that we're projecting to come in for that portfolio"; Regnery refers to "the 250 MW from LiquidStack" | Q3 2026 call, Motley Fool transcript | call |
| 2026 | LiquidStack 300 MW CDU order from a US operator; short-term aim of CDU output for 3 GW across two plants | MSP Channel / DigitalisationWorld | press, date not pinned |

### Johnson Controls (CDUs, Alloy Enterprises cold plates)

| Date | Fact | Source | Tag |
|---|---|---|---|
| Feb 2026 | Agreement to buy Alloy Enterprises (cold plates by "Stack Forging"); close expected Q3 2026; terms undisclosed | DCD, Metal AM | press |
| 27 Oct 2026 | CEO Joakim Weidemanis: "we've increased our offering, added CDUs, acquired a cold plate company"; CFO Marc Vandiepenbeeck: "We are ramping up capacity for CDU in all three regions" (mostly committed), "Only a small portion of that billion-plus dollar pipeline has converted to date" | Q4 FY2026 call, Webull transcript, https://www.webull.com/news/15821044567232512 | call |

### Carrier (own CDUs, no acquisition)

| Date | Fact | Source | Tag |
|---|---|---|---|
| 29 Oct 2026 | David Gitlin: CDUs "we introduced our 1 megawatt. We have a 2.6 megawatt, close to 3 megawatt unit ... in the next couple of months ... a 5 megawatt unit that comes out towards the end of this year. We're already booking orders for even the 5 megawatt unit"; hyperscalers "have been placing orders for the CDUs"; "We looked at some acquisitions in the space, and we said, effectively a CDU is a mini-chiller" | Q3 2026 corrected transcript (FactSet CallStreet), Carrier IR, https://s205.q4cdn.com/164393362/files/content_files/2026-10-29-CARR-Q3-2026-Earnings-Call-CORRECTED-TRANSCRIPT.pdf | call, company PDF |

### nVent

| Date | Fact | Source | Tag |
|---|---|---|---|
| 31 Jul 2026 | Data centre sales expected above $2bn in 2026, more than double 2025; Blaine 2 (third Minnesota liquid cooling plant) planned H1 2027; modular liquid cooling platform to launch later in 2026 | Q2 2026 call summaries (Benzinga, MarketBeat) | press |
| 30 Oct 2026 | Q3 2026 sales $1.515bn, +44% organic; infrastructure vertical organic sales "up over 70%"; infrastructure "nearly 60%" of sales year to date (12% at spin); "we have been taking orders for our new modular cooling products and platform"; Blaine 1 in production; Blaine 2 "about midway through next year"; on supply: "It is a lot of work to increase volumes with the velocity required"; backlog $2.6bn; organic orders up low double digits | Q3 2026 call, Motley Fool transcript (automated; Blaine 2 timing inconsistent within it) | call |

### Delta Electronics, and Nvidia's lists

| Date | Fact | Source | Tag |
|---|---|---|---|
| 2025 | Delta liquid cooling revenue about NT$48bn (KGI) or about 9% of revenue; Q1 2026 liquid cooling NT$15.0bn, down 22% on the quarter (KGI, 20 Apr 2026) | KGI research PDF | press (broker) |
| May 2026 | Daikin and Delta MOU to co-develop CDUs for ASEAN and Oceania | refindustry | press |
| GTC, Mar 2026 | Nvidia named four Vera Rubin cold plate suppliers; reports name AVC, Cooler Master, Jentech and Delta. One Chinese report (10jqka, 29 Oct 2026) gives April 2026 shares of about 54% Cooler Master, 23% AVC, 15% Jentech, 6% Delta. Auras (Shuang Hong) re-added to the recommended list in Sept 2026 | Digitimes 18 Mar 2026; ITES China; 10jqka; uanalyze | press |
| CDUs | Nvidia runs approved (AVL) and recommended (RVL) vendor lists for CDUs and has not published them; Delta's 1.5 MW liquid-to-liquid CDU reported on both; Boyd reported RVL for cold plates, manifolds and CDUs; LiquidStack says its 1 MW CDU is on the recommended list | cnyes; Boyd site; LiquidStack | press / vendor claim |
| Oct 2026 (GTC Berlin) | DSX POD reference design for factory-built Vera Rubin halls; 17 partners including Schneider and Vertiv; deliveries early 2027 | letsdatascience, HPCwire | press |

Asetek: no data centre cooling figures found (its business is now mainly gaming and simulators); not worth carrying.

---

## 2. Heat rejection makers (the roof: chillers, towers, dry coolers)

Terms for the piece: an **air-cooled chiller** is a refrigeration machine whose condenser is cooled by fans, so it evaporates no water; a **water-cooled chiller** rejects its heat through a cooling tower, which does. Most "chiller" orders for AI halls in 2026 are air-cooled, so chiller growth and the dry roof are not in conflict.

### Trane Technologies

| Date | Fact | Source | Tag |
|---|---|---|---|
| 18 Feb 2026 (approx.) | Acquired Stellar Energy Americas (modular, factory-built chiller plants) | press | press |
| Feb 2026 | Dave Regnery at Barclays: "I have not seen a reference design or data center of the future that does not include chillers" | fintool summary (page now redirects) | press; verbatim not checked at source |
| 5 May 2026 | Simmons: Stellar backlog "virtually 100% data center"; Chris Kuehn: Stellar brought "about $1 billion of backlog", a "$350 million revenue business" last year aiming for "$1 billion revenue-plus" in two to three years; capex guide raised to "2% to 3%" from "1% to 2%"; "purchase orders come typically 12 to 18 months in advance of when the delivery takes place"; long-term capacity agreements with some hyperscalers give two to three years' visibility; Stellar capacity "probably 2x" | Oppenheimer transcript, Trane IR PDF (above) | call, company PDF |
| Q2 2026 call (30 Jul 2026) | Applied capacity expanded fourfold over three years; market "increasingly weighted toward air-cooled systems and closed-loop designs, rather than evaporative cooling"; system sales can include chillers, air handlers and CDUs | MarketBeat / Webull summaries | press |
| 16 Mar 2026 | Trane and Nvidia: optimisations give "nearly 10%" better thermal performance than its original 1 GW reference design; Continuum Rubin DSX reference designs include water-cooled CenTraVac chillers with Stellar modular plants | Business Wire 16 Mar 2026; trane.com reference design page | press / vendor page |
| 29 Oct 2026 | Q3 2026: bookings $7,248m, +21% (20% organic); revenue $6,760m, +18%; "Backlog of $12.5 billion, up 73 percent; Americas Commercial HVAC up approximately 80 percent". The release does not mention data centres | Q3 2026 release, https://www.sec.gov/Archives/edgar/data/0001466258/000146625826000001/exhibit991-q32026earningsr.htm | primary |
| 29 Oct 2026 | Regnery: "the data center orders will be more lumpy, and they are larger"; of mega projects "over 90% of those are data centers"; "Stellar today is predominantly almost 100% data centers"; Kuehn: Stellar about "$500 million of revenue" in 2026; new factory "commissioning in Texas"; Regnery: "I expect more reference designs, not less" | Q3 2026 call, Motley Fool transcript (automated, names garbled in places) | call |

### Carrier

| Date | Fact | Source | Tag |
|---|---|---|---|
| 29 Oct 2026 | "Data center orders increased 300% and year-to-date data center orders have exceeded $3 billion, an increase of nearly 350%"; "more than $550 million in data center sales in the third quarter"; full-year data centre sales commitment "$2 billion"; record backlog "more than $8.5 billion", which "excludes minimum volume commitments under long-term agreements"; "signed an agreement with a hyperscaler for more than $3 billion" | Q3 2026 corrected transcript (above) and release, https://www.sec.gov/Archives/edgar/data/0001783180/000178318026000035/a99-q32026earningsexhibit.htm | call, company PDF; primary |
| 29 Oct 2026 | "great demand for our new 2 megawatt and 3 megawatt air-cooled chillers"; competition test on "restart time and operating at full efficiency at high ambient temperatures"; new chillers had "initial teething pains with the supply chain" because "it's hard to dual source right out of the gate" | same transcript | call, company PDF |
| 29 Oct 2026 | "we've increased our capacity significantly ... both for air-cooled and water-cooled chillers, but given our backlog and given our pipeline, just not enough"; Fort Worth site "to more than double our capacity in the Americas", customer deliveries "late summer of next year" (2027) | same | call, company PDF |

### Johnson Controls (York chillers, Silent-Aire)

| Date | Fact | Source | Tag |
|---|---|---|---|
| 27 Oct 2026 | Q4 FY2026: orders +44% organic; backlog $23.0bn, +43% organic; Americas orders +58%, backlog $17.8bn, +54%, "supported by sustained demand for data centers". No chiller figure in the release | Q4 FY2026 release, https://www.sec.gov/Archives/edgar/data/0000833444/000083344426000101/q4exh991xq4fy26earningsrel.htm | primary |
| 27 Oct 2026 | Weidemanis: "chillers is the largest part of our portfolio still"; "there will be some situations over time where on the margin, perhaps one or two fewer chillers will be needed" (redundancy and peak design mean customers are not yet cutting chiller counts); air-cooled vs water-cooled mix "has not changed materially recently"; "almost all of the data centers that are being built today have closed loop water cooling systems"; can "stand up new physical plant capacity within 12 months"; CFO: customers "continue to face power and some electrical infrastructure limitation" affecting delivery timing | Q4 FY2026 call, Webull transcript | call |
| 30 Jul 2026 | Data centres expected to be a high-teens percentage of FY2026 sales; absorption chillers and CDUs could raise value per data centre megawatt | MarketBeat summary of Q3 FY2026 call | press |

### Modine (Airedale, data centre chillers and air handlers)

| Date | Fact | Source | Tag |
|---|---|---|---|
| 3 Nov 2026 | Q2 FY2027 (to 30 Sep 2026): Data Centers net sales $439.7m vs $225.0m (+95%); six months $788.3m vs $408.7m; segment gross margin 19.7%, down 470 bp; "record orders and backlog in our Data Centers segment" (no dollar figures); "higher capital expenditures to increase production capacity in the Data Centers segment"; inventory $697.5m vs $506.1m at 31 Mar 2026; long-term agreements with suppliers "to secure critical components"; new risk factor: "opposition to data center development from local communities" | Q2 FY2027 release, 8-K Ex 99.1, https://www.sec.gov/Archives/edgar/data/0000067347/000110465926122032/mod-ex99d1.htm | primary |
| 4 Nov 2026 | Chiller sales lower year on year on "timing of shipments", "significant increase in 2H27"; quarterly order intake above $1bn, fourth straight record; $400m hyperscale programme award | earnings call deck, https://s205.q4cdn.com/270741342/files/content_files/Earnings-Call-FY27-Q2-vFinal.pdf (via search summary) | primary (not opened in full) |

### Munters (Data Center Technologies: chillers, CRAHs, CDUs)

| Date | Fact | Source | Tag |
|---|---|---|---|
| 23 Oct 2026 | Group order intake +70%; DCT "order intake more than doubling year-on-year"; DCT net sales +15% year on year; "DCT's margin fell, reflecting changed product mix, component shortages and ramp-up inefficiencies"; "constraints remain industry-wide"; scaling capacity "after expanding our campus in Daleville, Virginia" | Q3 2026 interim report release, https://mfn.se/cis/a/munters-group/munters-group-ab-significant-order-growth-as-operational-improvements-progress-1524bc51 | primary |
| 23 Oct 2026 | DCT order intake SEK 4,907m (+129% organic); DCT net sales SEK 1,789m; adjusted EBITA margin 9.7% vs 19.5%; DCT backlog SEK 22,927m, book-to-bill 2.7; ramp "approximately one quarter behind the original plan"; "the absolute vast majority of the limiting factor is external"; DCT order mix, last twelve months: chillers 49%, CRAHs 33%, CDUs 10% | Q3 2026 slides and call, Investing.com summary | press |
| Late 2025 | SEK 2.1bn order (CRAHs, CDUs, chillers) from a US colocation firm, deliveries Q4 2026 to Q1 2028; SEK 840m chiller order from a new US colocation customer; April 2026 SEK 2.0bn modular AI cooling order | Munters releases on mfn.se (titles in search) | primary titles |

### SPX Technologies (Marley cooling towers, data centre cooling)

| Date | Fact | Source | Tag |
|---|---|---|---|
| 29 Oct 2026 | HVAC revenue $525.0m, +35.5% (22.3% organic); organic growth from "higher volumes of cooling equipment, mainly associated with increased data center demand, resulting from increased capacity"; capacity projects "on track to support approximately $1.1 billion of annual data center revenue capacity at full production"; HVAC margin down to 23.0% on growth costs | Q3 2026 release, https://www.sec.gov/Archives/edgar/data/0000088205/000008820526000060/q32026pressrelease.htm | primary |
| 15 Sep 2026 | Closed FIS Water ("highly engineered water management and control solutions" for commercial and industrial cooling) for $405.0m net | Q3 2026 10-Q, Notes 1 and 3 | primary |
| 29 Oct 2026 | Organic HVAC backlog about $1.1bn, +69%; 2026 data centre revenue about $450m to $460m | call summaries (StockStory, Quartr) | press |

Which SPX products carry the data centre revenue (towers, adiabatic coolers, air handlers) is not split in what I opened.

### Daikin

Daikin does not break out data centre cooling revenue (per aggregator; not confirmed in Daikin's own filings). Daikin Applied bought DDC Solutions (rack-level cooling cabinets, 2025) and reportedly Chilldyne (liquid cooling), is opening two plants in 2026 for data centre demand, and showed an oil-free magnetic-bearing air-cooled chiller for data centres at AHR, Jan 2026 [press].

### Baltimore Aircoil, Evapco, Güntner

All three are private (Baltimore Aircoil is part of Amsted Industries). No disclosed data centre revenue, orders or backlog found.

### Do the makers say chillers are designed out?

No maker says so. In their own words:
- Trane, Feb 2026: no reference design without chillers [press]; Trane's own Rubin reference designs keep chillers [vendor page].
- Johnson Controls, 27 Oct 2026: "perhaps one or two fewer chillers" at the margin; chillers still the largest product line [call].
- Carrier, 29 Oct 2026: its hottest products are 2 and 3 MW air-cooled chillers, tested on "high ambient" performance [call].
- Vertiv, 28 Oct 2026: doubling chiller production capacity by end 2026 [call].
- Munters, LTM to Q3 2026: chillers 49% of data centre orders [press].
- Nvidia, 21 Jun 2026: chillers "maybe 1% of the year ... in some climates" (Ali Heydari) [primary].
- Microsoft's Fairwater AI campus (18 Sep 2025): "supported by the second largest water-cooled chiller plant on the planet", with "172 20-foot fans" [primary]. An AI hall built on closed-loop liquid still needs a giant chiller plant.

The consistent reading: warm coolant cuts chiller running hours, but chiller count is set by the hottest hour plus redundancy, so the installed chiller fleet keeps growing with the megawatts. What changes is the type: air-cooled chillers (no water) win over water-cooled chillers with towers.

---

## 3. Content per MW and the power versus cooling split

| Who | Figure | Scope | Date | Source | Tag |
|---|---|---|---|---|---|
| Vertiv | About $3.25m to $3.75m per MW of IT, up about 10% to 15% on the prior range | Power and thermal together, weighted mix, its own opportunity | 19 May 2026 | Deck p31 | primary |
| Vertiv | Thermal about 30% and power about 35% of FY2025 revenue | Revenue mix, not per MW | 19 May 2026 | Deck p10 (pairing inferred from layout) | primary |
| Schneider | $1.2m to $3.3m per MW; complex AI sites below the top | All its data centre content | 11 Dec 2025 | CMD transcript p63 | primary |
| Eaton | About $3.4m per MW with Boyd, from about $2.9m | Power plus liquid cooling | Q2 2026 call | MarketBeat summary | press |
| Johnson Controls | Modular data centres carry "higher" dollars per MW than gigawatt campuses; no number | Its own | 27 Oct 2026 | call | call |
| Industry | Liquid cooling about $1m to $2m per MW; mechanical share of facility cost rising from about 22% to 33% in liquid-cooled halls (attributed to Turner and Townsend); electrical 40% to 45% | Construction cost | 2026 | blogs citing JLL, Turner and Townsend | press |

No maker publishes a cooling-only per-MW figure, and no primary source gives the power versus cooling split of a data centre's capex. The best primary proxy is Vertiv's own revenue mix (thermal a little smaller than power). Do not put a cooling share of capex in the piece as fact.

---

## 4. Operators

| Who | Date | Fact | Source | Tag |
|---|---|---|---|---|
| Jane Street | undated page (© 2026) | "4,032 GPUs across 56 racks, retrofitted for liquid cooling" at "one of our new Texas data centers"; tour by Dwarkesh Patel with Ron Minsky (co-leads the tech group) and Dan Pontecorvo (physical engineering); the tour "traced the path from power and cooling up through the network fabric". No cold plate share, no plant description, no date on the page | https://www.janestreet.com/culture/street-view/a-look-inside-our-newest-data-center/ | primary |
| Jane Street | 25 Jul 2025 | Pontecorvo: air-cooled chillers on the roof "blow air over coil"; chillers lose capacity above a certain outdoor temperature; racks went from "10 to 15 KW" being high to designs of "170 kw per rack" | Signals and Threads ep. 24, https://signalsandthreads.com/the-thermodynamics-of-trading/ | primary |
| Microsoft | 18 Sep 2025 | Fairwater (Mount Pleasant, Wisconsin): closed loop "only needed to fill up once"; "second largest water-cooled chiller plant on the planet"; "172 20-foot fans"; "Over 90% of our datacenter capacity uses this system"; "The remaining 10% of traditional servers use outdoor air for cooling, switching to water only during the hottest days" | Scott Guthrie, https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/ | primary |
| Microsoft | 9 Dec 2024; 24 Jun 2026 | Zero-evaporation designs since Aug 2024 at "a nominal increase" in energy; about 90% of 2025 owned fleet "low- to zero-water cooling" | in live piece; not re-opened | primary (per live piece) |
| Meta | 27 Aug 2026 | "The majority of Meta's newest AI-optimized data centers use closed-looped, liquid cooling"; a typical AI hall "using a closed-loop liquid cooling system with dry coolers uses less water annually than a couple of full-service restaurants" | about.fb.com, Tom Shaw, https://about.fb.com/news/2026/08/closed-loop-cooling-explained-the-plumbing-behind-metas-ai/ | primary |
| Meta | 8 Oct 2026 | Air-cooled sites "use water for only a few months of the year to cool down air"; in water-stressed regions "the closed-loop design ... is the default"; loop is "a water and glycol mixture" | https://about.fb.com/news/2026/10/debunking-the-biggest-data-center-myths/ | primary |
| Meta | 2024 to 2025 | Air-assisted liquid cooling (rack-level pumps and heat exchangers) lets it run direct-to-chip racks in air-cooled halls | DCD, Data Center Frontier | press |
| AWS | Jul 2025 | In-Row Heat Exchanger (IRHX): cold plates, a water-distribution cabinet, pumping unit and in-row fan coils; built because third-party liquid cooling would have meant new liquid-ready buildings taking years | CNBC, Dell'Oro | press |
| AWS | 2026 sustainability report | IRHX expected to cut water use about 9% against evaporative air-cooled halls once fully operational (a projection); 938m litres of cooling water saved in 2025; WUE 0.12 L/kWh; PUE 1.14 | DCD summary of Amazon report (403 on fetch) | press (company figures) |
| Google | 30 Apr 2025 | Project Deschutes, Google's own CDU, about 99.999% fleet CDU availability since 2020; racks 10 to 100 kW, more than 500 kW before 2030 | Google Cloud blog (via rack-research/architecture.md) | primary |
| Digital Realty | May 2024 | Direct liquid cooling offered at about 170 data centres, 30 to 150 kW per rack | release via press | press, no 2026 update found |
| Equinix | Dec 2023 | Direct-to-chip support planned for over 100 IBX sites in 45 metros | release via press | press, no 2026 update found |

---

## 5. Is cooling, not power, delaying halls?

Evidence is of strain, not of halls standing idle for cooling:
- Munters, 23 Oct 2026: data centre ramp "approximately one quarter behind the original plan", "component shortages", constraints "industry-wide" [primary for shortages, press for the quarter-late figure].
- Carrier, 29 Oct 2026: new air-cooled chillers had "initial teething pains with the supply chain"; capacity "just not enough to keep up"; Fort Worth from late summer 2027 [call, company PDF].
- Modine, 3 Nov 2026: long-term supplier deals "to secure critical components to meet our existing backlog"; segment margin down 470 bp on material and component costs [primary].
- nVent, 30 Oct 2026: "It is a lot of work to increase volumes with the velocity required" [call].
- Vertiv, 28 Oct 2026: an analyst cited "compressors that have been burning out"; Vertiv did not deny or quantify [call]. Vertiv saw "nothing out of the ordinary" in project slippage, with power, permitting and labour as "pacing items" [call].
- Johnson Controls, 27 Oct 2026: customers face "power and some electrical infrastructure limitation" affecting delivery timing; demand is not the constraint [call].
- Trane, 5 May 2026: firm orders arrive 12 to 18 months before delivery, some to 24 months [call, company PDF].
- Press only: CDU lead times 6 to 9 months (one engineering blog); "custom cooling systems" lead times five times longer than a few years ago (Bisnow). Neither is primary.

Verdict for the piece: no primary source names a hall delayed by cooling equipment. The makers name power and electrical gear as the customers' pacing items, and name component shortages as their own. Cooling is a margin and ramp problem for makers in 2026, not a visible gate on halls.

---

## What the live piece has wrong or out of date

1. **Ecolab is misdescribed.** The exposure map says only "Ecolab treats cooling water", and the text says fewer towers mean less treatment. Ecolab bought CoolIT, a CDU and cold plate maker, for $4,627m net, closing 2 July 2026 (10-Q, Note 3). Ecolab now sits in the liquid loop too, and the "fewer towers, less treatment" line should note that the water-treatment company has moved to the loop.
2. **CoolIT is no longer independent.** List it as Ecolab's. LiquidStack is Trane's (completed 3 March 2026); Boyd is Eaton's; Motivair is Schneider's. The exposure map should name the parents.
3. **The "loop makers" and "roof makers" split is out of date.** Trane (LiquidStack CDUs), Johnson Controls (CDUs, Alloy cold plates), Carrier (own 1 to 5 MW CDUs) and Munters (CDUs, 10% of data centre orders) now make the loop. Vertiv now makes roof plant: ThermoKey dry coolers (completed 12 June 2026) and chillers (BSE, Dec 2024; chiller capacity doubling by end 2026). Rewrite both exposure-map lines.
4. **"Chillers shrink as a share of each megawatt" needs the makers' evidence beside it.** The concession is right in hours, but in 2026 chiller orders hit records: Carrier's 2 to 3 MW air-cooled chillers, Vertiv doubling chiller output, chillers 49% of Munters' data centre orders, Johnson Controls saying only "one or two fewer" at the margin. The piece should say plainly that chiller hours fall while chiller orders rise, because count is set by the worst hour and redundancy.
5. **The piece misses the air-cooled chiller.** Its taxonomy has tower, dry cooler and chiller, with the chiller costing "the most power". Most AI hall chillers now ordered are air-cooled and use no water. The dry roof in practice is dry coolers plus air-cooled trim chillers, not dry coolers alone. Add the term where chillers first appear.
6. **"Schneider Electric ... agreed to take control of Motivair ... on 17 October 2024"** is right for the agreement but should add that it completed in early 2025 ("acquired in March this year", Whitmore, CMD, 11 Dec 2025).
7. **Jane Street's 85 to 90% cold plate share is not in Jane Street's write-up.** The page gives "4,032 GPUs across 56 racks, retrofitted for liquid cooling" (verified) but no heat split and no date. Keep 85 to 90% only if the video itself was checked, with a timestamp; otherwise cut it. "15 May 2026" is not on the page either. "Newest Texas site" is fine for the page title; the body says "one of our new Texas data centers".
8. **Microsoft's flagship AI hall is missing.** Fairwater runs over 90% on a closed loop backed by "the second largest water-cooled chiller plant on the planet" and 172 fans, with the other 10% on outdoor air and water "only during the hottest days" (18 Sep 2025). It is the best primary case for the piece's own worst-afternoon point.
9. **Meta's own figure is missing.** "The majority of Meta's newest AI-optimized data centers use closed-looped, liquid cooling" with dry coolers (27 Aug 2026). The third test names Meta but the evidence fold has no Meta line.
10. **Exposure map gaps:** add SPX (Marley towers; about $1.1bn of annual data centre revenue capacity being built; FIS Water bought for $405m, 15 Sep 2026), Delta Electronics (CDUs, Vera Rubin cold plates), Daikin (chillers, DDC rack cooling) and Eaton via Boyd. Munters makes chillers, CRAHs and CDUs, not only "coolers".
11. **Per-MW content:** if the rebuild uses one, Vertiv's $3.25m to $3.75m per MW (19 May 2026) is power and cooling together. No maker publishes cooling alone, and no primary source splits capex between power and cooling.
12. **Nvidia's "maybe 1% of the year" quote** is verified in Nvidia's blog and is Ali Heydari's; the piece should name him. The same post says chillers may run "a few days a year" and names Motivair as its only cooling partner.

## Could not verify

- Jane Street's 85 to 90% of server heat to cold plates, and the 15 May 2026 date of the video (the page carries neither).
- Regnery's Feb 2026 "no reference design ... that does not include chillers" in a primary transcript (summary page now redirects).
- Any maker's liquid cooling revenue as a disclosed line: Vertiv, Schneider, Trane, Johnson Controls and Carrier do not split it. Boyd's $1.9bn 2026 outlook is call-only; CoolIT's sales are not disclosed in Ecolab's Q3 filing.
- Vertiv's FY2025 portfolio pairing (35% power, 30% thermal) beyond the slide layout; the deck could not be rendered as an image.
- Munters' 49% chiller share and "one quarter behind plan" in Munters' own report (from slide summaries).
- SPX's organic HVAC backlog ($1.1bn, +69%) and 2026 data centre revenue ($450m to $460m) in SPX's own text; which SPX products carry the data centre sales.
- Trane's LiquidStack price; Johnson Controls' Alloy close date and price.
- Nvidia's CDU vendor lists (not published); cold plate supplier shares are from Taiwanese and Chinese press.
- Daikin, Baltimore Aircoil, Evapco and Güntner data centre figures (not disclosed or private).
- Any primary, dated case of an AI hall delayed by cooling equipment rather than power.
- AWS's 9% IRHX water figure at Amazon's own page (DCD page returned 403).
- Equinix and Digital Realty liquid-ready counts after 2024.
