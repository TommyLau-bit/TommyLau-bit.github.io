# BWXT and microreactors: a study guide

Prepared 6 November 2026 for Tommy Lau. Purpose: to be able to explain and defend every fact here from your own head, in front of a nuclear sell-side analyst.

How to read this guide:

- Every number carries a source code in square brackets, such as [S1], and a date. The full list is in section 14.
- "Fact" means a company filing, a government release or a regulator document says it. "Estimate" means a study or a company target. "My arithmetic" means I worked it out from sourced numbers, and you should be able to redo it.
- Where I could not verify something, I say so. Section 14 ends with that list.
- Nothing here is a price view. Section 9 reports how the market argues the bull and bear cases.

---

## 1. The one-paragraph version

BWX Technologies (ticker BWXT) is the company that builds the nuclear reactors for every American submarine and aircraft carrier, and makes their fuel. It calls itself the sole manufacturer of both [S52]. About three quarters of its revenue comes from the US government [S5], and naval propulsion alone is about half of group revenue [S7, 29 Sep 2026]. That business is close to a monopoly, paid on cost-based contracts, and very visible: the order backlog was $8.56 billion at 30 September 2026, about 2.25 times this year's guided revenue of $3.8 billion [S1, 2 Nov 2026; my arithmetic]. Around that core it is building three growth lines: commercial reactor parts and services (mostly Canada's CANDU fleet), government uranium work (a $1.5 billion contract to rebuild American defence enrichment), and advanced reactors. In advanced reactors it holds two things few others have: the only working production line for TRISO fuel at meaningful scale in the US (a couple of hundred kilograms a year today [S6]), and a microreactor, Project Pele, that is physically built and due to ship to Idaho in 2027 with power targeted for 2028 [S18; S6]. In August 2026 the Army picked BWXT's larger BANR microreactor (22 MWe) for Fort Campbell [S14; S17]. The shares fell 42% in the year to 5 November 2026, to $114.96, about 18 times this year's guided EBITDA [S13; my arithmetic].

---

## 2. Nuclear basics you need

### 2.1 Fission in four sentences

A uranium-235 atom absorbs a slow neutron and splits into two lighter atoms, releasing heat and two or three new neutrons. If, on average, exactly one of those neutrons causes another split, the chain reaction holds steady. That steady state is called "criticality". A reactor is "critical" when it sustains the chain reaction, which says nothing about how much power it makes: a "zero-power" critical test makes almost no heat and no electricity. This distinction matters in section 7, because every reactor that went critical under the 2026 DOE programme did so at zero or very low power.

A "moderator" (water or graphite) slows neutrons so they split U-235 more easily. A "fast" reactor has no moderator and uses fast neutrons; it needs richer fuel. The "coolant" carries the heat away: water, helium gas, liquid sodium, molten salt or, in heat-pipe designs, sodium sealed inside metal pipes.

### 2.2 Enrichment levels

Natural uranium is about 0.7% U-235; the rest is U-238, which does not split easily. Enrichment raises the U-235 share by spinning uranium hexafluoride gas in centrifuges. Enrichment work is measured in SWU (separative work units).

| Name | U-235 share | Used for | Notes |
|---|---|---|---|
| Natural | about 0.7% | Canada's CANDU reactors | CANDU needs no enrichment, because it uses heavy water as moderator |
| LEU (low-enriched uranium) | below 20%; ordinary power reactors use about 3% to 5% | The existing US fleet of large water reactors | Supply leans on Russia, Urenco, Orano |
| LEU+ | about 5% to 10% | Longer fuel cycles in existing reactors; some SMRs | A marketing term, not a legal one |
| HALEU (high-assay LEU) | 5% to just under 20% (most designs use about 19.75%) | Most microreactors and advanced reactors | Still legally "low enriched"; the US has almost no commercial production |
| HEU (highly enriched uranium) | 20% and above | Naval reactors, weapons, some research reactors | Naval fuel is HEU; public estimates put it near weapons grade, but the exact figure is classified and I did not verify it |

Why HALEU? Richer fuel lets a small core run for years without refuelling. Project Pele is designed to run up to three years without refuelling [S18]; BANR about four years [S16]; Antares's R1 six years or more (trade sources, not an Antares document I read).

Link to your nuclear-for-ai piece: that piece already explains HALEU and Centrus. Section 6 below updates it, and one fact in it is now out of date (see section 6.1).

### 2.3 Fuel forms

- **UO2 pellets.** Ceramic uranium dioxide pellets stacked in zirconium alloy tubes. Standard fuel for large water reactors and for Aalo's sodium reactor, which uses 5% LEU from Urenco [Aalo, S30].
- **TRISO particles.** A uranium kernel about the size of a poppy seed [S18], wrapped in layers of carbon and silicon carbide. Each particle is its own tiny containment vessel. TRISO is pressed into pellets ("compacts") or pebbles. It tolerates very high temperatures, which is why it suits small reactors that rely on passive cooling. Almost every microreactor in section 5 uses TRISO.
- **Metallic fuel.** Uranium-zirconium alloy, used by Oklo's Aurora sodium fast reactor (from recovered EBR-II material for its first core, per your nuclear-for-ai piece).
- **Uranium zirconium hydride (UZrH).** Used in TRIGA research reactors and in General Atomics' Janus design [S16].

### 2.4 Reactor types in this guide

| Type | Coolant / moderator | Who | Notes |
|---|---|---|---|
| PWR (pressurised water reactor) | Water under pressure | Most of the world's fleet; Last Energy's PWR-5/PWR-20 | Mature, ordinary fuel |
| Naval PWR | Water | BWXT for the US Navy | Compact, HEU fuel, cores last decades |
| HTGR (high-temperature gas reactor) | Helium (or nitrogen) gas, graphite moderator, TRISO | Pele, BANR, Radiant Kaleidos, X-energy, NANO KRONOS, Valar | High outlet temperature, passive safety |
| Heat-pipe reactor | Sodium sealed in pipes carries heat out, no pumps | Westinghouse eVinci, Antares R1 | Few moving parts; scale tops out at a few MWe |
| Sodium fast reactor | Liquid sodium, no moderator | Oklo Aurora | Larger; Oklo's is 75 MWe |
| Sodium thermal reactor | Sodium coolant, graphite moderator | Aalo | Uses ordinary LEU, not HALEU |
| Molten salt / fluoride salt | Salt coolant | Kairos (salt-cooled, TRISO pebbles); Natura; Terrestrial | Kairos is an SMR-class developer, not micro |

### 2.5 Microreactor versus SMR

- **Microreactor:** Idaho National Laboratory describes them as factory-built, transportable and self-regulating, "with power outputs in the 1 to 20 MWe range typically" [S45, Aug 2024]. The Army's Janus programme spans 100 kWe to 20 MWe [S16, 27 Aug 2026].
- **SMR (small modular reactor):** the IAEA uses "up to 300 MWe" per unit [S54; standard definition, not re-fetched this session]. Examples: GE Vernova's BWRX-300 at Darlington (300 MWe) and Oklo's Aurora (75 MWe).
- **MWe versus MWt.** MWe is electrical output; MWt (or MWth) is heat. Conversion is roughly a third: BANR is 75 MWt for 22 MWe [S6; S17]. Always ask which one a company is quoting.

---

## 3. BWXT

### 3.1 History in five lines

- BWXT is the old Babcock & Wilcox. Its naval work dates to "the 1950s" [S5].
- On 30 June 2015 it spun off its Power Generation business (fossil boilers) as Babcock & Wilcox Enterprises, and the remaining nuclear company became BWX Technologies [S5, 10-K FY2024].
- It tried and shelved an SMR, mPower, "for financial reasons" (management at the 2026 Investor Day [S7]).
- CEO: Rex Geveden. CFO: Mike Fitzgerald, who succeeded Robb LeMasters in 2025 [S6; search result on the 2025 CFO change, not re-fetched].
- 2025 to 2026 deals: bought Aerojet Ordnance Tennessee (closed 3 January 2025, about $101 million), Kinectrics (Canadian nuclear services and testing, closed 20 May 2025, CAD 782.7 million headline), and Precision Components Group (closed 1 July 2026, about $216.8 million); agreed on 31 July 2026 to sell its medical isotope business to Nordic Capital for up to $800 million, keeping a minority stake, expected to close in 2026 or Q1 2027 [S2, 10-Q Q3 2026].

### 3.2 Segments and who pays

**Government Operations** (73% of 2025 revenue [S3; my arithmetic])
- Naval Nuclear Propulsion Program: reactors, components and fuel for Virginia-class and Columbia-class submarines and Ford-class carriers [S5; S11]. Naval propulsion is about 50% of total BWXT revenue and about 70% of this segment (management, Investor Day, 29 Sep 2026 [S7]).
- Nuclear Fuel Services (NFS), Erwin, Tennessee: makes naval fuel and downblends Cold War HEU stockpiles into lower enrichments [S5]. A September 2025 naval fuel award was $174 million [S11], and the 2026 annual fuel contract was booked at $189 million [S6].
- Special materials for NNSA (the National Nuclear Security Administration, the part of DOE that runs the weapons complex): high-purity depleted uranium (HPDU) plant at Jonesborough, Tennessee, under a 10-year, $1.6 billion contract of 30 September 2025, up to 300 tonnes a year [S10].
- Defence enrichment: the $1.5 billion, sole-source DUECE contract (Domestic Uranium Enrichment Centrifuge Experiment) of September 2025 for a pilot centrifuge plant at Erwin, with centrifuges made at a new Oak Ridge facility. It first makes LEU for defence needs, then is repurposed for HEU for naval propulsion. NNSA states it will not make fuel for commercial power [S9]. Management said on 2 November 2026 it is "on track to test a prototype centrifuge by the end of this year" [S6].
- Site management joint ventures (for example Hanford, Savannah River, Y-12) [S6].
- Advanced Technologies: Project Pele, BANR, NASA and DoD reactor work, TRISO fuel [S5; S18].

**Commercial Operations** (27% of 2025 revenue [S3; my arithmetic])
- Heavy components for reactors (steam generators, heat exchangers, pressure vessels) from Cambridge, Ontario; the company has supplied "more than 1,300 large, heavy components worldwide" [S5]. The Cambridge expansion raised heavy component capacity by about 50% [S6].
- CANDU fuel and fuel-handling systems for Canadian reactors, including refurbishment of Ontario's fleet [S5].
- Kinectrics (engineering, testing, life extension) and, from July 2026, Precision Components Group (about 75% to 80% naval work, reported in Commercial) [S2; S6].
- Medical isotopes, which are being sold [S2].
- A planned US heavy components plant for steam generators and reactor vessels, with a final investment decision expected by end 2026 [S6].

### 3.3 What only BWXT can do (and how sure we are)

| Capability | Status | How sure |
|---|---|---|
| Naval reactors and naval fuel | BWXT calls itself the sole manufacturer of US naval reactors and sole provider of naval fuel [S52]. Its 10-K says it has "limited competition" and has supplied the fleet since the 1950s [S5]. | Company wording. I found no Navy document stating exclusivity. |
| HEU downblending | NFS at Erwin downblends government HEU stockpiles [S5]. | Fact (10-K). |
| TRISO at scale | Lynchburg line makes "a couple of hundred kilograms per year", enough to fuel all of Pele's core, and management says it can "at least quadruple" with changes [S6, 2 Nov 2026]. At the Investor Day it said it is the largest TRISO supplier and that rivals deliver "very modest amounts" [S7]. | Company statement. Standard Nuclear's filing gives a comparable figure for itself (0.5 tonnes of uranium a year; section 6.3), so "only" overstates it; "largest proven" is defensible. |
| Defence enrichment | DUECE pilot plant, sole-source, $1.5 billion [S9]. | Fact. Not for commercial power. |
| Built microreactor | Pele core built and installed in Lynchburg, core barrel complete September 2026 [S18; S6]. | Fact. Not yet operated. |

### 3.4 Business model, and why margins and visibility look the way they do

- **Contract types.** Government Operations is mostly "fixed-price incentive fee" contracts, which reimburse allowable costs plus a fee that moves with performance. Advanced technology work is mostly cost-plus. Site joint ventures are cost-reimbursable with award fees. Commercial is partly fixed-price, the rest mainly time-and-materials [S5, 10-K FY2024].
- **Why margins are steady but capped.** Cost-based contracts limit losses but also limit upside. Government Operations runs at about 20% to 21% adjusted EBITDA margin each year (table below), rising to 22.6% in Q3 2026 on productivity [S1; S6]. Commercial runs at about 13% to 14%, because it is fixed-price manufacturing with more competition.
- **Why visibility is high.** Navy work is "program of record", so management says the company has been "a little bit immune" to continuing resolutions, the stop-gap budgets Congress passes when it misses deadlines [S6]. Backlog covers about nine quarters of revenue [S7].
- **Revenue recognition.** Revenue is recognised over time on a cost-to-cost basis [S2]. This means estimate changes on long contracts move profit. A 2022 short report by Jehoshaphat Research criticised a long run of positive estimate revisions [S51, 16 Jan 2022]. It is old and I found no finding against the company, but an analyst may raise it.
- **Lumpy bookings.** Q3 2026 bookings were $538 million against $2,245 million a year earlier, because big multi-year naval contracts land in particular quarters [S1].

### 3.5 Key financials

All figures in US$ millions unless stated. Adjusted EBITDA and non-GAAP EPS are company-defined measures.

| | 2023 [S4] | 2024 [S3] | 2025 [S3] | 2026 guide [S1] | 9M 2026 [S1] |
|---|---|---|---|---|---|
| Revenue | 2,496.3 | 2,703.7 | 3,198.4 | about 3,800 | 2,714.8 |
| of which Government Ops | 2,031.3 | 2,183.0 | 2,350.1 | about 2,600 (Investor Day [S7]) | 1,818.3 |
| of which Commercial Ops | 466.3 | 524.0 | 853.1 | about 1,200 (Investor Day [S7]) | 900.4 |
| GAAP operating income | 383.1 | 380.6 | 404.5 | n/a | 352.9 |
| GAAP operating margin (my arithmetic) | 15.3% | 14.1% | 12.6% | n/a | 13.0% |
| Adjusted EBITDA | 471.9 | 498.7 | 574.3 | about 667 | n/a |
| Adjusted EBITDA margin (my arithmetic) | 18.9% | 18.4% | 18.0% | 17.6% | n/a |
| Gov Ops adj. EBITDA margin (my arithmetic) | 21.1% | 20.2% | 20.4% | n/a | Q3: 22.6% |
| Commercial adj. EBITDA margin (my arithmetic) | 12.9% | 14.0% | 12.9% | n/a | Q3: 13.2% |
| Non-GAAP EPS ($) | 3.02 | 3.33 | 4.01 | 4.72 to 4.77 | n/a |
| Capex | 151.3 | 153.6 | 184.6 | about 6% of revenue [S6] | 136.2 |
| Free cash flow | 212.4 | 254.8 | 295.3 | 350 to 360 | n/a |
| Year-end backlog | 3,997.6 | 4,842.5 | 7,260.7 | 8,556.2 at 30 Sep | |

Notes:
- Segment revenues do not add exactly to the total because of eliminations.
- Commercial's jump in 2025 is mostly acquisitions (Kinectrics from May 2025). Q3 2026 Commercial growth was 25%, of which 15% organic [S6].
- Backlog more than doubled from end 2023 to Q3 2026, driven by naval awards of about $2.1 billion (February 2025) and $2.6 billion (July 2025) [S11], and the DUECE and HPDU contracts [S9; S10].
- Backlog at 30 September 2026: Government $6,481.8 million, Commercial $2,074.4 million [S1]. About $500 million came with Precision Components Group [S6].

**Q3 2026 results (released 2 November 2026) [S1]:** revenue $953.0 million (up 10%, 7% organic); GAAP operating income $132.1 million; adjusted EBITDA $179.7 million (up 19%); non-GAAP EPS $1.26 (up 26%); free cash flow $150.5 million. 2026 guidance: revenue about $3.8 billion reaffirmed; EPS narrowed to $4.72 to $4.77; adjusted EBITDA about $667 million; free cash flow raised at the low end to $350 to $360 million.

**2027 preliminary outlook [S1; S6]:** high-single-digit revenue growth; high-single-digit to low-double-digit growth in adjusted EBITDA and EPS; Commercial margin up 50 to 100 basis points; free cash flow flat to slightly up (pension contribution of about $10 million linked to Kinectrics, working capital, and milestone timing on HPDU and enrichment).

**2030 targets (Investor Day, 29 September 2026; reaffirmed 2 November) [S7; S6]:** revenue $5.5 to $6.0 billion; adjusted EBITDA $1.1 to $1.2 billion, margin rising from 17.5% to about 20%; free cash flow $525 to $575 million; capex 5% to 6% of revenue; more than $2 billion cumulative free cash flow 2026 to 2030. My arithmetic: the midpoints imply about 11% a year revenue growth and about 15% a year EBITDA growth from 2026. Management said the targets do not depend on acquisitions [Investing.com summary, S49].

**Balance sheet [S2; S12]:** long-term debt $2,022 million and cash $569 million at 30 September 2026. The debt includes $1.1 billion of 0% convertible notes due November 2030, priced on 5 November 2025 with a conversion price of about $262.51 per share and capped calls up to $396.24 [S12]. Shares outstanding 91.6 million at 30 October 2026 [S2]. Fitch gave an investment-grade rating and Moody's moved its outlook to positive [S6].

---

## 4. BWXT and microreactors specifically

### 4.1 Project Pele (the DoD prototype)

| Item | Detail | Source |
|---|---|---|
| Customer | Department of Defense (now styled Department of War) Strategic Capabilities Office (SCO), with DOE, INL and the Army | [S18; S20] |
| Award | June 2022, cost-type contract of about $300 million depending on options; original plan was delivery in 2024 | [S19, 9 Jun 2022] |
| Size | 1.5 MWe ("1 to 5 MWe" in 2022 framing) | [S18; S19] |
| Type | High-temperature gas-cooled reactor, TRISO HALEU fuel made by BWXT | [S18] |
| Portability | Designed for truck and C-17 transport | [S18] |
| Refuelling | No refuelling for up to three years | [S18] |
| Fuel | TRISO production for the initial core finished November 2025; first fuel arrived at INL in early December 2025 | [S18; S20, 3 Dec 2025] |
| Build | Core assembly began July 2025; core barrel cartridge installed September 2026 | [S18] |
| Next step | Ship to INL in 2027 | [S6, 2 Nov 2026] |
| First power | Target 2028 ("first fully tested advanced microreactor power system to power military equipment") | [S18] |

What to say: Pele is real hardware, but it has slipped about four years against the 2022 plan (delivery 2024 then; first power 2028 now). It is a demonstration for the military, not a product. No first-power date was given on the Q3 2026 call [S6].

### 4.2 BANR (BWXT Advanced Nuclear Reactor)

- 22 MWe from 75 MWt (Geveden corrected 20 to 22 MWe on the Q3 call) [S6; S17].
- Gas-cooled high-temperature reactor. POWER magazine reports nitrogen coolant, about 600°C core outlet, uranium oxycarbide (UCO) TRISO at 19.75% enrichment and about four years between refuelling [S16, 27 Aug 2026]. Coolant detail is from trade press, not a BWXT document I could read (the BWXT release returned a 403 error).
- Described as scaled up from Pele [S16; S7].
- BWXT plans an NRC manufacturing licence application, aiming for review in under 24 months [S16].
- Customers so far:
  - **Army Janus, Fort Campbell, Kentucky** (selected 26 August 2026). Groundbreaking targeted late 2028, operations early 2030s [S15; S16].
  - **Prodigy Clean Energy, Belledune, New Brunswick**: BANR selected on 5 October 2026 for a transportable nuclear power plant of up to 50 MWe using two BANRs; the province signed a letter of intent to buy the power; in service "early 2030s"; no definitive agreement yet [S17].
  - **Tata Chemicals Soda Ash**: letter of intent for up to eight BANR units in Wyoming, per POWER [S16]. I did not find the primary release.
- Management will not sell BANR "at the expense of other considerations", stressing that component risk differs from project delivery risk [S6]. Read: BWXT does not want to take fixed-price construction risk on a whole plant.

### 4.3 The Army's Janus programme

- Announced 26 August 2026. Five companies, five bases, up to $2.2 billion of Army money over FY2027 to FY2031, through milestone-based Other Transaction Authority (OTA) agreements with the Defense (War) Innovation Unit. Vendors own, build and operate the reactors. The Army expects more than 20 microreactors across bases [S14].
- Pairings [S14]: Antares at Fort Bragg; BWXT at Fort Campbell; General Atomics at Fort Hood; Radiant at Fort Benning; Westinghouse at Fort Drum.
- The first reactor will be "regulated by the Army", with a target of operation by September 2028, which comes from Executive Order 14299 [S14; S43].
- Split of the $2.2 billion is not disclosed. POWER reports Radiant's share at up to $750 million for 15 Kaleidos units by 2030 [S16].
- Phase one for BWXT covers site selection, NRC processes and TRISO production; costs and operating plans are still being defined [S6].

### 4.4 Air Force ANPI

The Air Force's Advanced Nuclear Power for Installations initiative (announced April 2026, per POWER) uses long-term power purchase agreements with NRC-licensed, contractor-owned plants: Radiant at Buckley Space Force Base, Antares at Joint Base San Antonio, Westinghouse at Malmstrom, with a goal of one reactor operating by 2030 [S16]. Oklo's Eielson project in Alaska is a separate 30-year power purchase structure targeting 2030 pending NRC licensing [S16]. BWXT is not in ANPI as far as I found.

### 4.5 DOME at INL

DOME (Demonstration of Microreactor Experiments) is INL's test bed for fuelled microreactor tests. Radiant's Kaleidos left El Segundo in mid-August 2026 for DOME, received DOE approval of its safety analysis for full power on 29 October 2026, and still needs a DOE readiness review before fuelling and a five-phase test campaign [S26]. It missed the July 2026 target. Pele is a separate test at INL; I could not confirm which INL facility will host Pele's operation (its fuel sits at the Transient Reactor Test Facility [S20]).

### 4.6 Data centres

BWXT management did not discuss data centres directly on the Q3 2026 call; hyperscalers came up only in comments on how project risk is shared [S6]. The Investor Day cited about 60 GW of incremental AI power demand as a market driver, without tying microreactors to it [S7]. BWXT's realistic data-centre exposure is indirect: TRISO fuel and components sold to developers (Kairos is Google's partner; BWXT and Kairos agreed in September 2025 to study commercial TRISO production [S37]), and heavy components for larger reactors.

---

## 5. The microreactor landscape

Status as of the latest dated source. "Critical" means a zero-power criticality test unless stated. None of these has yet delivered electricity to a paying customer, as far as I could find.

| Developer and design | Size | Fuel | Coolant | Customer / buyer | Route | Latest status (date) | Claimed first power |
|---|---|---|---|---|---|---|---|
| **BWXT Pele** | 1.5 MWe | TRISO HALEU | Gas (HTGR) | DoD SCO | DoD/DOE | Core barrel installed Sep 2026; ships to INL 2027 [S18; S6] | 2028 [S18] |
| **BWXT BANR** | 22 MWe / 75 MWt | UCO TRISO 19.75% | Gas (nitrogen per POWER) | Army Janus (Fort Campbell); Prodigy (Canada) | Army; NRC manufacturing licence planned | Selected Aug and Oct 2026 [S14; S17] | Operations early 2030s [S15] |
| **Westinghouse eVinci** | about 5 MWe (Westinghouse's long-stated figure, not re-verified this session; size for Janus not disclosed) | TRISO 19.75% | Heat pipes | Saskatchewan Research Council (pilot by 2029); Army Janus (Fort Drum); Air Force ANPI (Malmstrom) | NRC (topical reports approved, e.g. nuclear design methodology, 9 Jan 2026) | Zero-power criticality 24 Aug 2026 at the Nevada National Security Site with Los Alamos and INL [S25] | SRC pilot by 2029 [S55] |
| **Radiant Kaleidos** | 1 MWe (3 MWt) | TRISO HALEU | Helium | Army Janus (15 units, Fort Benning, up to $750m per POWER); Air Force ANPI (Buckley); Equinix preorder of 20 units | DOE authorisation for test; NRC Part 70 licence for Oak Ridge R-50 factory, review target 18 Dec 2026 | At INL DOME; full-power safety analysis approved 29 Oct 2026; awaiting readiness review [S26; S27] | Power to Buckley by 2028 [S39]; all Janus units by 2030 [S16] |
| **Antares R1** | 100 kWe to 1 MWe | TRISO HALEU (BWXT and Standard Nuclear) | Sodium heat pipes, nitrogen Brayton cycle | Army Janus (Fort Bragg); Air Force ANPI (San Antonio) | DOE authorisation (Mark-0, Mark-1) | Mark-0 critical 4 Jun 2026 at INL, first under the pilot programme [S21] | Mark-1 electricity 2027 [S34]; R1 deployments 2028 [S16] |
| **Oklo Aurora** | 75 MWe (not micro; an SMR) | Metallic HALEU | Sodium (fast) | Meta campus; Equinix; Eielson (Alaska) | DOE authorisation at INL | Ground broken Sep 2025; DOE preliminary safety analysis approved Jun 2026. Oklo's separate Groves isotope test reactor went critical 5 Aug 2026 in Texas [S23; S31] | Aurora-INL 2028 (nuclear-for-ai piece, from Oklo 7 Aug 2026) |
| **X-energy XENITH** | Not verified (trade sources say several MWe) | TRISO-X | Gas (HTGR) | DoD, Air Force ANPI enhanced engineering phase (Aug 2025) | NRC pre-application (2026 engagement plan filed 1 Jun 2026) | No 2026 hardware milestone found [S33] | Not found |
| **NANO Nuclear KRONOS MMR** | 15 MWe / 45 MWt | TRISO | Helium | University of Illinois Urbana-Champaign (research reactor) | NRC construction permit application submitted 31 Mar 2026; review started Jun 2026 | NRC review under way [S28] | Company expects permit in 2027 and construction from H2 2027 [S28] |
| **Kairos Power Hermes** | 35 MWt test reactor (not micro) | TRISO pebbles, HALEU | Fluoride salt | Google; TVA (Hermes 2) | NRC construction permits | NRC extended Hermes 1 construction deadline to 30 Apr 2029 [S32] | Not dated by Kairos in sources I found |
| **Aalo** | Aalo-X 10 MWe; Aalo Pod 50 MWe (five units) | UO2, 5% LEU (Urenco) | Sodium, graphite moderated | Data centres (target) | DOE authorisation for Aalo-X; NRC for Pod | Aalo-X critical 4 Jul 2026 at INL [S22] | Pod commercial 2029 (company) [S30] |
| **Last Energy PWR-5 / PWR-20** | PWR-5 pilot (5 MW); PWR-20 commercial | LEU | Water (PWR) | Data centre fleets (company claims) | DOE authorisation at Texas A&M RELLIS | Preliminary safety analysis approved May 2026; not yet critical as of Sep 2026 [S29] | Pilot criticality "in coming months" (Sep 2026) |
| **Valar Atomics Ward 250** | 100 kWt | TRISO | Helium | Planned 30 MW Utah data centre with Nvidia (per ANS) | DOE authorisation | Critical 18 Jun 2026 in Utah; 10 kWt on 22 Jun [S21; S50] | Not found |
| **Deployable Energy Unity** | 1 MWe | Not verified | Gas (HTGR) | Not found | DOE Nuclear Energy Launch Pad | Critical 1 Jul 2026 at INL [S21] | Not found |
| **General Atomics (GA-EMS)** | about 5 MWe, scalable to 20 MWe | UZrH (not TRISO) | Not verified | Army Janus (Fort Hood) | Army | Selected Aug 2026 [S16] | Not disclosed |

Things to notice:
1. Five of the six critical tests of 2026 were zero-power or near-zero-power physics tests. None made electricity.
2. TRISO is near-universal. HALEU is near-universal. Aalo and Last Energy are the exceptions, using ordinary LEU, which is a strategic advantage while HALEU is scarce.
3. Military buyers came first: Janus and ANPI pair the same vendors (Radiant, Antares, Westinghouse) with bases [S16].
4. Oklo's Aurora is often called a microreactor in the press. At 75 MWe it is not. If Max says "Oklo's small units", be ready to correct politely.

---

## 6. The fuel choke point

### 6.1 HALEU supply

- **Centrus, Piketon, Ohio.** The only American company that has enriched HALEU, on a 16-centrifuge demonstration cascade [nuclear-for-ai, S53]. Your piece says its DOE-contracted production finished in mid-June 2026 and DOE ordered maintenance only from 30 June. **New fact since your piece:** Centrus's Q3 2026 release (4 November 2026) says it is now "Enriching HALEU for the commercial market from existing 16-centrifuge cascade", with DOE giving it rights to use the centrifuges commercially; no customer, volume or price was disclosed [S38]. DOE has said it does not intend to exercise further options under the HALEU operation contract, and the proposed FY2027 DOE budget does not fund the cascade [S38]. Centrus named X-energy, Radiant and Antares as having agreements with prepayments [S38, call of 5 Nov 2026]. Centrus has begun shipping new centrifuges from Oak Ridge to Piketon for its commercial expansion [S38].
- **DOE HALEU allocations.** Three rounds of conditional allocations from government stock: April 2025 (TRISO-X, Kairos, Radiant, Westinghouse, TerraPower), August 2025 (Antares, Standard Nuclear, Natura with Abilene Christian University), 23 July 2026 (NASA and Radiant, the latter for its Buckley Space Force Base unit due by 2028) [S39]. No tonnages published.
- **Executive Order 14299** directs DOE to release at least 20 tonnes of HALEU into a fuel bank for private projects [S43].
- **Russia.** Russia sold 26% of the enrichment US reactor owners bought in 2025; waivers that let owners keep buying end by 1 January 2028 [nuclear-for-ai, citing EIA August 2026; carried over, not rechecked]. Russia was historically the main commercial HALEU seller, which is why the gap opened.
- **Urenco.** Building a HALEU line at Capenhurst, UK, with up to 27 tonnes a year (expandable to 54), production from 2031, per a secondary source [S40]. Urenco has said it is exploring HALEU at its New Mexico plant [S40]. Treat as unverified against a Urenco primary document.
- **Orano.** Project IKE enrichment plant in Tennessee under NRC review; HALEU plans not verified [S40].
- **BWXT.** DUECE is defence-only and NNSA says it will not supply commercial power [S9]. Management discussed adding LEU and HALEU to the NNSA scope and said commercial sales might face a cost disadvantage against Urenco [S6; S7]. So BWXT is not, today, a commercial HALEU supplier.

### 6.2 Why HALEU paces microreactors

Nobody builds an enrichment plant until reactors exist to burn the output, and no reactor runs without fuel (your nuclear-for-ai argument). Microreactors make it worse in one way and easier in another:
- Worse: almost every design needs HALEU in TRISO form, so it needs two scarce steps (enrichment and TRISO fabrication).
- Easier: each unit is small. My arithmetic, rough: Oklo's 5-tonne award covers one 75 MWe core. A 1 MWe microreactor needs a far smaller core than that, so government stock can fuel the first few dozen microreactors. The constraint bites at fleet scale, not at the first units.

### 6.3 TRISO fabrication capacity (tonnes of uranium a year, MTU)

| Maker | Today | Planned | Source |
|---|---|---|---|
| BWXT, Lynchburg | "A couple of hundred kilograms per year"; can "at least quadruple" with changes. Antares agreement for an initial 1 MTU through the end of the decade (27 Oct 2026). More than $25 million authorised to expand Lynchburg. | Multi-tonne greenfield plant in Wyoming, conditional on anchor demand (for example Kairos) and commercial HALEU | [S6; S34; S16; S7] |
| Standard Nuclear, Oak Ridge | SN-0 operating under DOE authorisation, 0.5 MTU a year (yield 63.3%) | SN-TN about 1 MTU at commissioning in H2 2026, building ceiling 2.5 MTU; long-term up to 20 MTU. Agreements with Antares (1 MTU, options to 8) and Radiant | [S35, 10-Q Q2 2026; S16] |
| X-energy TRISO-X, Oak Ridge | NRC Part 70 licence (40 years, first Category II fuel fabrication licence) issued February 2026 | TX-1 commercial production projected early 2028 (slipped from December 2027) | [S36] |

What to say: today the whole US TRISO industry makes well under one tonne of uranium a year. BWXT and Standard Nuclear are roughly the same order of size. BWXT's edge is proof (it fuelled Pele and Antares's Mark-0), not volume.

---

## 7. Regulation and the 2025 to 2026 policy push

### 7.1 Three routes to operate a reactor in the US

1. **NRC licence.** The independent regulator. Needed for commercial power sold off federal sites. Construction permit plus operating licence (Part 50), or a combined licence (Part 52), or now Part 53.
2. **DOE authorisation.** DOE can authorise reactors on its own sites, or for research and testing under its pilot programme. Faster, but for tests and demonstrations, not ordinary commercial sales.
3. **Military authorisation.** Executive Order 14299 lets the Army regulate a reactor on a military base [S43]. Janus uses this [S14].

### 7.2 Executive orders of 23 May 2025

Four orders, published in the Federal Register on 29 May 2025:
- **EO 14299** (national security): Army to operate an Army-regulated reactor at a domestic base by 30 September 2028; DOE to designate AI data centres at DOE sites as critical defence facilities; at least 20 tonnes of HALEU into a fuel bank [S43].
- **EO 14300** (NRC reform): fixed deadlines of 18 months for new reactor licences; a wholesale rule revision [secondary sources; I did not read the order's primary text].
- **EO 14301** (DOE testing): "Secretary shall approve at least three reactors pursuant to this pilot program with the goal of achieving criticality in each of the three reactors by July 4, 2026" [S42].
- **EO 14302** (industrial base): sets the 400 GW by 2050 goal from about 100 GW today [secondary sources only].

### 7.3 Did the July 4, 2026 target happen? Yes, at zero power.

| # | Reactor | Date | Place | Programme |
|---|---|---|---|---|
| 1 | Antares Mark-0 | 4 Jun 2026 | INL | Reactor Pilot Program [S21; S24] |
| 2 | Valar Ward 250 | 18 Jun 2026 | Utah San Rafael Energy Lab | Reactor Pilot Program [S21; S50] |
| 3 | Deployable Energy Unity | 1 Jul 2026 | INL | Nuclear Energy Launch Pad, not the original pilot list [S21] |
| 4 | Aalo-X | 4 Jul 2026, early hours | INL | Reactor Pilot Program [S22] |
| 5 | Oklo Groves isotope test reactor | 5 Aug 2026 | Texas (private land) | Reactor Pilot Program [S23] |

Separately, outside the pilot programme: Valar's NOVA core went critical on 17 November 2025 at Los Alamos's criticality centre in Nevada [S50], and Westinghouse's eVinci did a zero-power criticality test there on 24 August 2026 [S25].

How to say it: DOE met the goal (three or four by 4 July, depending on whether you count Deployable Energy). But all were physics tests at zero or tiny power. Not one has made electricity. The next real milestone is electricity: Antares Mark-1 (2027), Kaleidos at DOME (pending), Last Energy's PWR-5.

I found no sixth criticality reported up to early November 2026. Not verified as complete.

### 7.4 NRC changes

- **Part 53**, a new optional, technology-inclusive licensing framework, was published 30 March 2026 and took effect 29 April 2026 [S41]. It is the first new reactor licensing framework since 1989 (per trade coverage).
- The NRC is reviewing Radiant's factory licence on an eight-month target, due 18 December 2026, against a typical 18 months [S27].
- The NRC licensed TRISO-X's fuel plant in February 2026 [S36].
- Deadline to watch: EO 14300's final rules are due around 23 November 2026 (18 months after the order), per secondary sources. I could not confirm progress.

### 7.5 Military procurement

- Army Janus: five vendors, $2.2 billion, first reactor by September 2028 (section 4.3) [S14].
- Air Force ANPI: Radiant, Antares, Westinghouse tracks; Oklo at Eielson (section 4.4) [S16].
- Pele: SCO prototype, 2028 power target (section 4.1) [S18].

---

## 8. Economics

Separate the facts from the estimates. There are no observed costs for a commercial microreactor yet, because none has been sold and operated.

### 8.1 Estimates of microreactor cost

| Estimate | Figure | Basis | Source |
|---|---|---|---|
| NEI estimate, quoted by INL | First-of-a-kind $0.14 to $0.41 per kWh (two-unit 5 MWe plant), falling to $0.09 to $0.33 at 50 units | Study | [S44, Jun 2021] |
| INL bottom-up estimate (LMTR-20 reference design, based on DOE's MARVEL reactor) | First-of-a-kind overnight cost about $14,600 per kWe, excluding first fuel; Nth-of-a-kind about $6,000 per kWe and LCOE about $120 per MWh ($0.12 per kWh) | Bottom-up study | [S45, Aug 2024] |
| INL meta-analysis, SMRs (300 MWe) for comparison | Overnight cost $5,500 to $10,000 per kWe (2022 dollars) for early units; $2,000 to $6,250 by 2050 | Meta-analysis | [S46, Jul 2024] |
| Army Janus implied value (my arithmetic) | $2.2 billion for "more than 20" reactors is about $110 million per reactor of government money, before private capital | Contract ceiling, not cost | [S14] |
| Radiant Janus implied value (my arithmetic) | Up to $750 million for 15 units of 1 MWe is about $50 million per MWe | Contract value, which may include operations over years; not a cost | [S16] |

Overnight cost means the cost to build as if overnight, before financing. LCOE (levelised cost of electricity) spreads all lifetime costs over all lifetime output.

### 8.2 What microreactors compete with

| Alternative | Price | Source |
|---|---|---|
| Diesel in remote places | $0.15 to $0.60 per kWh; small rural Alaska communities $0.35 to $0.60 (average $0.52) | [S44, citing University of Alaska Anchorage 2020] |
| Alaska mine diesel case | Present value about $0.16 per kWh at $3.02 per gallon | INL 2023 study, via search summary; not read in full |
| US average industrial grid power, 2024 | 8.13 cents per kWh | [S47] |

Fact for the bull case: Pele's page says one unit offsets up to 1.5 million gallons of diesel a year [S18]. My arithmetic: 1.5 MWe running all year is 13,140 MWh; at about 12.7 kWh per gallon that is about 1.0 million gallons, so the claim is the right order of magnitude.

### 8.3 Why data centres are a hard first customer

1. **Price.** A data centre on the grid pays around 8 cents per kWh (2024 industrial average). The INL Nth-of-a-kind estimate is about 12 cents, and first units cost far more [S45; S47]. Microreactors beat diesel at a remote base; they do not yet beat the grid.
2. **Scale.** A 1 MWe unit is tiny against a campus of hundreds of MW. Even Equinix's 20-unit Radiant preorder is about 20 MWe [S48].
3. **Fuel.** HALEU and TRISO are scarce (section 6), and the military and DOE are ahead in the queue.
4. **Licensing.** A data centre off a federal site needs an NRC licence; military and DOE sites have faster routes (section 7).
5. **Reliability needs.** Data centres need redundancy, so one microreactor still needs backup; that pushes cost up.
6. **Who pays for first-of-a-kind risk.** Military programmes pay milestones (Janus) or sign long PPAs (ANPI) [S14; S16]. Data-centre buyers mostly sign preorders or letters of intent, as your nuclear-for-ai piece found with Oklo and Meta.

Where data centres might come in early: remote or off-grid sites, places where the grid connection takes years, or as a premium for "firm, clean" power. These are arguments, not evidence yet.

---

## 9. Bull case, bear case, and what is priced in

This section reports how the market argues it. It is not a view.

### 9.1 The bull case (as argued)

- **Monopoly core.** Sole supplier of naval reactors and fuel; Virginia-class at about two a year and Columbia-class deliveries heavy into the mid-2030s [S7]. Naval shipbuilding growth of 4% to 6% a year, with possible upside from SSN-AUKUS (submarines for Australia under the AUKUS pact) and "battleship cores", per management [S7].
- **Visibility.** Backlog $8.56 billion, about 2.25 times 2026 revenue [S1]; cost-based contracts; resilient to continuing resolutions [S6].
- **New government franchises.** DUECE enrichment ($1.5 billion) and HPDU ($1.6 billion) put BWXT at the centre of rebuilding US defence uranium supply; management cited a GAO figure of $37 billion to reconstitute defence fuels capability [S9; S10; S7].
- **Commercial growth.** Canada life extension (CAD 50 billion through 2032) and new build, AP1000 and SMR content (management estimates $350 to $700 million addressable per CANDU reactor, "low hundreds of millions" per AP1000, $50 to $100 million per SMR) [S7]. Commercial revenue grew 25% in Q3 2026 [S1].
- **Optionality in microreactors and fuel.** Only microreactor builder with hardware built (Pele), a Janus win (BANR), a first international win (Prodigy), and the proven TRISO line [S6; S14; S17].
- **Margin path.** EBITDA margin from 17.5% to about 20% by 2030 [S7].

### 9.2 The bear case (as argued)

- **Valuation for a defence contractor.** Even after the fall, about 24 times 2026 EPS guidance and about 18 times 2026 EBITDA (section 9.3), above typical defence prime multiples (a market argument; I did not verify peer multiples).
- **Microreactors are small money and far away.** BANR operations early 2030s [S15]; Pele power 2028, four years late versus the 2022 plan [S18; S19]; no first-power date given in Q3 [S6]. Microreactors do not drive the 2030 targets.
- **Commercial orders keep slipping.** Management expects firm US orders "by year-end 2026, and no later than H1 2027" and firm commercial orders in 2027 [S6]. The market has heard similar timing before. Revenue slightly missed consensus in Q3 [S49].
- **Lower-quality growth mix.** Commercial margins are about 13% versus about 22% in Government; selling the higher-margin medical business dilutes Commercial [S6].
- **Concentration and budget risk.** About 76% of revenue from the US government [S5]; contracts can be terminated or modified [S5].
- **Cash conversion.** 2027 free cash flow guided only flat to slightly up despite EBITDA growth [S6].
- **Balance sheet change.** $1.1 billion of 0% convertibles (conversion at about $262.51) and long-term debt of about $2.0 billion [S12; S2].
- **Sector sentiment.** Nuclear stocks sold off broadly in the second half of 2026; trade commentary blamed higher rates and risk-off markets, and BWXT fell about 6% on 4 November with the group [Motley Fool commentary, not a primary source]. Several brokers cut targets in September to October 2026 (per secondary reports).

### 9.3 What is priced in (as of the close on 5 November 2026)

| Measure | Value | Source |
|---|---|---|
| Share price | $114.96 (close, 5 Nov 2026) | [S13] |
| A year earlier | $198.12 (close, 5 Nov 2025) | [S12] |
| Change | about minus 42% | my arithmetic |
| Recent path | $130.47 on 2 Nov (results day), $131.82 on 3 Nov, $121.50 on 4 Nov, $114.96 on 5 Nov | [S13] |
| Market value | about $10.5 billion (91.6 million shares) | [S13; S2] |
| Enterprise value | about $12.0 billion | [S13] |
| Price / 2026 non-GAAP EPS guidance midpoint ($4.745) | about 24.2 times | my arithmetic |
| Forward P/E (data vendor) | 23.1 times | [S13] |
| EV / 2026 adjusted EBITDA guidance ($667m) | about 18.0 times | my arithmetic |
| EV / 2027 EBITDA if it grows 9% | about 16.5 times | my arithmetic, using the low end of guidance |

Caveats: EV here does not credit the up to $800 million medical sale proceeds, which would lower it. Data vendor figures are third-party and dated 5 November 2026.

Reading: at about 18 times EBITDA, the market is paying for the 2030 plan (EBITDA of $1.1 to $1.2 billion), not for microreactors. If 2030 EBITDA hits $1.15 billion, today's EV is about 10 times that (my arithmetic). The argument is about whether the commercial ramp and margin expansion arrive on time.

---

## 10. The 10 numbers to memorise

| # | Number | What it is | Source | Date |
|---|---|---|---|---|
| 1 | $8.56bn | Total backlog (Government $6.48bn, Commercial $2.07bn) | [S1] | 30 Sep 2026 |
| 2 | $3.8bn and about $667m | 2026 revenue and adjusted EBITDA guidance (17.6% margin) | [S1] | 2 Nov 2026 |
| 3 | $5.5 to 6.0bn and $1.1 to 1.2bn | 2030 revenue and adjusted EBITDA targets (about 20% margin) | [S7] | 29 Sep 2026 |
| 4 | about 76% and about 50% | US government share of revenue (2024); naval propulsion share of revenue (management) | [S5; S7] | FY2024; 29 Sep 2026 |
| 5 | 22.6% versus 13.2% | Q3 2026 adjusted EBITDA margin, Government versus Commercial | [S1; my arithmetic] | Q3 2026 |
| 6 | $1.5bn | DUECE defence enrichment pilot plant contract (sole-source; not for commercial fuel) | [S9] | Sep 2025 |
| 7 | a couple of hundred kg a year | BWXT Lynchburg TRISO output; Antares took an initial 1 MTU through 2030 | [S6; S34] | 2 Nov 2026; 27 Oct 2026 |
| 8 | 1.5 MWe, about $300m, 2028 | Pele size, 2022 contract value, first-power target (was 2024 delivery) | [S18; S19] | Nov 2026; Jun 2022 |
| 9 | 22 MWe / 75 MWt; $2.2bn; Sep 2028 | BANR size; Army Janus funding for five vendors; Army's first-reactor target | [S6; S14] | Aug to Nov 2026 |
| 10 | $114.96; about 18x | Share price; EV / 2026 EBITDA guidance | [S13; my arithmetic] | 5 Nov 2026 close |

---

## 11. Questions Max might ask, with model answers

**1. "What does BWXT actually do, in one line?"**
It builds the reactors and fuel for the US Navy's submarines and carriers, which is about half its revenue, and uses that know-how to sell reactor parts, fuel and services to Canada's CANDU fleet, the US weapons complex and new reactor developers.

**2. "Why are Government margins higher than Commercial?"**
Government work is near-monopoly and mostly fixed-price incentive fee or cost-plus, so costs are covered and fees reward performance; it runs at about 20% to 22% EBITDA margin. Commercial is fixed-price or time-and-materials manufacturing with competitors such as Doosan and IHI for big components, so about 13% [S5; S1; S6].

**3. "How much of the backlog turns into revenue soon?"**
Backlog is $8.56 billion, about 2.25 years of revenue. A third-party reading of the 10-Q says about 46% converts by end 2027; I could not open that part of the filing myself, so I would say "about half within roughly two years, per the 10-Q as reported" and offer to check. (Unverified: see section 14.)

**4. "Is BWXT a HALEU play?"**
Not directly. DUECE is defence-only by NNSA's own statement. BWXT's commercial fuel exposure is TRISO fabrication, which needs someone else's HALEU. Management has said commercial enrichment could face a cost disadvantage against Urenco [S9; S7].

**5. "What is Pele's status and why does it matter?"**
Core built, core barrel installed September 2026, fuel at INL since December 2025, ships in 2027, power targeted 2028. It is four years behind its 2022 plan. It matters because it is the template for BANR and gives BWXT the only operating-ready military microreactor design [S18; S19; S6].

**6. "BANR versus Pele?"**
Pele is a 1.5 MWe transportable prototype for the Pentagon. BANR is a 22 MWe (75 MWt) fixed plant using the same family of gas-cooled TRISO technology, picked for Fort Campbell and for Prodigy in New Brunswick. Operations early 2030s [S6; S15; S17].

**7. "Which microreactors actually went critical?"**
Under DOE authorisation: Antares (4 June), Valar (18 June), Deployable Energy (1 July), Aalo (4 July), Oklo's Groves isotope reactor (5 August). Plus Westinghouse's eVinci zero-power test in Nevada on 24 August. All zero or near-zero power; none has made electricity [S21; S22; S23; S25].

**8. "Who gets power first: the military or data centres?"**
The military, on the evidence. EO 14299 sets September 2028 for an Army-regulated reactor; Janus pays milestones; ANPI signs PPAs. Data centres have preorders and letters of intent, cheap grid alternatives and need NRC licences [S43; S14; S16].

**9. "What's the cost per MWh?"**
No observed costs exist. INL's bottom-up study puts a first-of-a-kind microreactor at about $14,600 per kWe and a mature fleet at about $120 per MWh. Remote diesel is $150 to $600 per MWh; US industrial grid power was about $81 per MWh in 2024. So it competes with diesel, not with the grid [S45; S44; S47].

**10. "What's the TRISO bottleneck?"**
US output is well under a tonne of uranium a year today: BWXT a couple of hundred kilograms, Standard Nuclear 0.5 tonnes capacity at SN-0, TRISO-X not producing until early 2028. And all of them depend on HALEU, which comes from government stock plus Centrus's small cascade [S6; S35; S36; S38].

**11. "What's priced in?"**
At $114.96 on 5 November, about $12 billion EV, about 18 times 2026 EBITDA guidance and about 24 times 2026 EPS guidance. That pays for the 2030 plan, not for microreactors, which are a small part of it [S13; S1; my arithmetic].

**12. "What would make you wrong about microreactors being slow?"**
If Kaleidos or Antares's Mark-1 produces sustained electricity at INL in 2027 and a Janus unit operates on a base by September 2028, the military timeline is real. If a data-centre operator takes delivery of power from a microreactor before a base does, my ordering is wrong.

**13. "What's in Centrus's latest release that matters for your piece?"**
Centrus says it is now enriching HALEU for the commercial market from its 16-centrifuge cascade, with DOE's permission, but DOE won't fund the cascade further and gave no volume. That updates my piece, which said production stopped in June [S38].

**14. "Why did BWXT fall after a beat?"**
Q3 adjusted EPS beat, revenue was slightly light, and the sector sold off. The market debates the timing of commercial orders and the 2027 cash flow outlook [S49; S6]. I would not claim a single cause.

---

## 12. A possible dated claim for a future journal piece

**Draft claim (for Tommy to adopt, change or drop):**
"The first microreactor (20 MWe or less) to deliver electricity to a paying customer in the US will do so on a military installation under a defence contract, not at a data centre, and not before 2028: no microreactor will have delivered electricity to any paying customer outside a DOE or national laboratory site by 30 June 2028."

**Why it is defensible today:**
- Every 2026 criticality was at zero power at a lab or test site [S21; S22; S23; S25].
- Earliest dated customer deliveries are 2028: Radiant to Buckley [S39], Antares R1 [S16], Janus first reactor by September 2028 [S14], Pele power 2028 at INL [S18].
- Data-centre buyers hold preorders, not delivery contracts [S48; nuclear-for-ai].

**What would prove it wrong:**
1. Any microreactor of 20 MWe or less delivers electricity under a paying contract (PPA, milestone service contract or sale) at a site that is not a DOE or national laboratory site on or before 30 June 2028.
2. Or the first such delivery, whenever it comes, is to a data centre or other commercial customer rather than a military site.

**What would move the view before the test:**
- Radiant's NRC factory licence on time (18 December 2026 target) and Kaleidos reaching full power at DOME [S27; S26].
- Last Energy's PWR-5 at Texas A&M selling power, since RELLIS is a university campus, not a DOE site [S29]. This is the most likely early break; watch it.
- A disclosed price per MWh in any Janus or ANPI contract.

**What would not move it:** more zero-power criticality tests; more letters of intent from data-centre operators.

Link to nuclear-for-ai: that piece's claim is about 100 MW of HALEU reactors on American grids by end 2030. Janus and ANPI add HALEU microreactors, but my arithmetic on announced units (Radiant's 15 MWe at Benning, Antares's few MWe, BANR's 22 MWe in the early 2030s) stays well under 100 MW by 2030, and most of it would be behind the meter on bases, not on the grid. So the microreactor programme does not threaten that claim, but say so explicitly in any new piece.

---

## 13. Glossary

- **Adjusted EBITDA:** earnings before interest, tax, depreciation and amortisation, with company-chosen adjustments.
- **ANPI:** Advanced Nuclear Power for Installations, the Air Force's microreactor programme using power purchase agreements.
- **Backlog:** signed orders not yet turned into revenue.
- **BANR:** BWXT Advanced Nuclear Reactor, 22 MWe gas-cooled TRISO microreactor.
- **CANDU:** Canadian reactor using natural uranium and heavy water.
- **Cost-plus / fixed-price incentive fee:** contract types where the government pays costs plus a fee; the incentive version adjusts the fee for performance against a target cost.
- **Criticality:** a self-sustaining chain reaction. Zero-power criticality makes no useful heat.
- **DOME:** Demonstration of Microreactor Experiments, INL's microreactor test bed.
- **DUECE:** Domestic Uranium Enrichment Centrifuge Experiment, NNSA's defence enrichment pilot, built by BWXT.
- **EO:** executive order.
- **FOAK / NOAK:** first-of-a-kind / Nth-of-a-kind (a mature, repeated build).
- **HALEU:** uranium enriched to between 5% and just under 20% U-235.
- **HEU:** uranium enriched to 20% or more.
- **HPDU:** high-purity depleted uranium, used in the weapons programme.
- **HTGR:** high-temperature gas-cooled reactor.
- **INL:** Idaho National Laboratory, DOE's lead nuclear lab.
- **Janus:** the Army's programme to own-build-operate microreactors at bases.
- **LCOE:** levelised cost of electricity.
- **LEU / LEU+:** low-enriched uranium (below 20%; power reactors use 3% to 5%); LEU+ is 5% to 10%.
- **Microreactor:** factory-built reactor of about 1 to 20 MWe.
- **MWe / MWt:** megawatts of electricity / of heat.
- **NNSA:** National Nuclear Security Administration, part of DOE.
- **NRC:** Nuclear Regulatory Commission.
- **OTA:** Other Transaction Authority, a flexible federal contracting route outside standard procurement rules.
- **Part 53 / Part 70:** NRC rules; Part 53 is the new optional reactor licensing framework; Part 70 licenses possession and use of special nuclear material (for example fuel plants).
- **SCO:** Strategic Capabilities Office, a Pentagon office that ran Pele.
- **SMR:** small modular reactor, up to about 300 MWe.
- **SWU:** separative work unit, the measure of enrichment effort.
- **TRISO:** tristructural isotropic fuel particle; uranium kernel coated with carbon and silicon carbide layers.
- **Zero-power test:** a criticality test to check the physics, with no meaningful heat output.

---

## 14. Sources

Dates are publication dates, or "accessed 6 Nov 2026" where the page is undated or live.

- [S1] BWXT, Q3 2026 results release (Form 8-K, Exhibit 99.1), 2 Nov 2026. https://www.sec.gov/Archives/edgar/data/0001486957/000148695726000053/bwxt_93026xerexhibit991.htm
- [S2] BWXT, Form 10-Q for the quarter ended 30 Sep 2026 (filed early Nov 2026). https://www.sec.gov/Archives/edgar/data/0001486957/000148695726000051/bwxt-20260930.htm
- [S3] BWXT, Q4 and full-year 2025 results release, 23 Feb 2026. https://www.sec.gov/Archives/edgar/data/1486957/000148695726000005/bwxt_123125xerexhibit991.htm
- [S4] BWXT, Q4 and full-year 2023 results release, 27 Feb 2024. https://www.sec.gov/Archives/edgar/data/1486957/000148695724000009/bwxt_123123xerexhibit991.htm
- [S5] BWXT, Form 10-K for 2024 (filed Feb 2025). https://www.sec.gov/Archives/edgar/data/1486957/000148695725000008/bwxt-20241231.htm
- [S6] BWXT Q3 2026 earnings call transcript (Motley Fool), 2 Nov 2026. https://www.fool.com/earnings/call-transcripts/2026/11/02/bwxt-q3-2026-earnings-call-transcript/
- [S7] BWXT Investor Day transcript, 29 Sep 2026 (StockAnalysis). https://stockanalysis.com/stocks/bwxt/transcripts/742527-investor-day-2026/
- [S8] BWXT, notice of Investor Day on 29 Sep 2026 (Aug 2026). https://bwxt.gcs-web.com/news-releases/news-release-details/bwx-technologies-hold-investor-day-september-29-2026
- [S9] BWXT, "BWXT Awarded Contract for NNSA Defense Fuels Program", 16 Sep 2025, https://www.businesswire.com/news/home/20250916252069/en/BWXT-Awarded-Contract-for-NNSA-Defense-Fuels-Program ; ANS Nuclear Newswire, 17 Sep 2025, https://www.ans.org/news/2025-09-17/article-7374/nnsa-awards-bwxt-15b-defense-fuels-contract/
- [S10] BWXT, high-purity depleted uranium contract, 30 Sep 2025. https://www.businesswire.com/news/home/20250930874054/en/BWXT-Awarded-Contract-to-Produce-High-Purity-Depleted-Uranium-for-National-Defense-Purposes
- [S11] BWXT, $2.1bn naval contracts (Feb 2025), https://www.bwxt.com/bwxt-announces-2-1-billion-in-contracts-for-naval-nuclear-reactor-components-2/ ; $2.6bn naval contracts (17 Jul 2025), https://www.bwxt.com/bwxt-announces-2-6-billion-in-contracts-for-naval-nuclear-reactor-components/ ; $174m naval fuel (30 Oct 2025), https://www.businesswire.com/news/home/20251030077254/en/BWXT-Awarded-174-Million-Naval-Nuclear-Fuel-Contract-in-September
- [S12] BWXT, pricing of $1.1bn convertible notes, 5 Nov 2025. https://www.businesswire.com/news/home/20251106927527/en/BWX-Technologies-Announces-Pricing-of-Upsized-Convertible-Senior-Notes-Offering
- [S13] StockAnalysis, BWXT statistics and price history, data to 5 Nov 2026 close (accessed 6 Nov 2026). https://stockanalysis.com/stocks/bwxt/statistics/ and https://stockanalysis.com/stocks/bwxt/history/
- [S14] US Army, "Army reaches agreement with private industry for nuclear micro-reactors", 26 Aug 2026. https://www.army.mil/article/294891/army_reaches_agreement_with_private_industry_for_nuclear_micro_reactors
- [S15] BWXT, "U.S. Army Chooses BWXT Advanced Nuclear Reactor (BANR) for Janus Program", 26 Aug 2026. https://www.businesswire.com/news/home/20260826436761/en/U.S.-Army-Chooses-BWXT-Advanced-Nuclear-Reactor-BANR-for-Janus-Program (I could not open it directly; details via [S16] and reprints)
- [S16] POWER magazine, "The Janus Five", 27 Aug 2026. https://www.powermag.com/the-janus-five-20-commercial-nuclear-microreactors-starting-in-2028/
- [S17] World Nuclear News, "BWXT's BANR microreactor selected for Canadian project", Oct 2026, https://world-nuclear-news.org/articles/bwxts-banr-microreactor-selected-for-canadian-project ; ANS, 7 Oct 2026, https://www.ans.org/news/2026-10-07/article-8471/bwxts-banr-selected-for-canadian-project/
- [S18] BWXT, Project Pele page (accessed 6 Nov 2026). https://www.bwxt.com/sectors/defense-space/land/project-pele/
- [S19] BWXT, "BWXT to Build First Advanced Microreactor in United States", 9 Jun 2022. https://www.businesswire.com/news/home/20220609005154/en/BWXT-to-Build-First-Advanced-Microreactor-in-United-States
- [S20] US Army, TRISO fuel delivery to Project Pele, 3 Dec 2025. https://www.army.mil/article/289323/army_leaders_applaud_triso_fuel_delivery_as_project_pele_moves_toward_first_microreactor_demonstration
- [S21] ANS Nuclear News, "The deadline arrives: Checking in on the Reactor Pilot Program", 2 Jul 2026. https://www.ans.org/news/article-8178/the-deadline-arrives-checking-in-on-the-reactor-pilot-program/
- [S22] DOE, "Department of Energy Celebrates Fourth Criticality Ahead of July 4th Goal", 6 Jul 2026. https://www.energy.gov/articles/department-energy-celebrates-fourth-criticality-ahead-july-4th-goal
- [S23] DOE Office of Nuclear Energy, "Celebrates Fifth Advanced Reactor Criticality", 6 Aug 2026. https://www.energy.gov/ne/articles/office-nuclear-energy-celebrates-fifth-advanced-reactor-criticality
- [S24] DOE, Reactor Pilot Program page (accessed 6 Nov 2026). https://www.energy.gov/ne/us-department-energy-reactor-pilot-program
- [S25] Westinghouse, "eVinci Microreactor Achieves Zero-Power Criticality", 25 Aug 2026, https://info.westinghousenuclear.com/news/westinghouse-evinci-microreactor-achieves-zero-power-criticality ; World Nuclear News, https://world-nuclear-news.org/articles/criticality-testing-milestone-for-westinghouses-evinci-microreactor
- [S26] Radiant, DOE safety analysis approval for full power, 29 Oct 2026, https://www.financialcontent.com/article/bizwire-2026-10-29-radiant-achieves-industry-milestone-as-the-only-microreactor-design-to-secure-doe-safety-analysis-approval-for-full-power-operations ; Radiant, "Kaleidos Has Left the Building", Aug 2026, https://www.radiantnuclear.com/blog/kaleidos-shipped/
- [S27] ANS, "NRC to review Radiant R-50 Part 70 license application", 6 May 2026. https://www.ans.org/news/2026-05-06/article-8009/nrc-to-review-radiant-r50-part-70-license-application/
- [S28] NRC, KRONOS applicant page (accessed 6 Nov 2026), https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/applicant-projects/kronos ; ANS, 2 Apr 2026, https://www.ans.org/news/2026-04-02/article-7904/uiuc-submits-mmr-construction-permit-application/
- [S29] KBTX, "Nuclear reactor at RELLIS could be running within months", 11 Sep 2026, https://www.kbtx.com/2026/09/11/nuclear-reactor-rellis-could-be-running-within-months/ ; World Nuclear News on PWR-5 safety analysis, May 2026, https://world-nuclear-news.org/articles/last-energy-texas-micro-modular-reactor-clears-safety-analysis
- [S30] Aalo, Aalo-X page (accessed 6 Nov 2026). https://aalo.com/aalo-x
- [S31] Oklo, Form 10-Q for Q2 2026 (Aug 2026). https://www.sec.gov/Archives/edgar/data/0001849056/000162828026054571/oklo-20260630.htm
- [S32] World Nuclear News, "Regulator extends Hermes 1 reactor construction deadline", 2026. https://world-nuclear-news.org/articles/regulator-extends-hermes-1-reactor-construction-deadline
- [S33] X-energy, XENITH page (accessed 6 Nov 2026), https://x-energy.com/reactors/xenith ; X-energy and DoD release, 14 Aug 2025, https://www.businesswire.com/news/home/20250814780056/en/X-energy-U.S.-Department-of-Defense-to-Advance-Commercial-Microreactor-for-National-Security
- [S34] POWER magazine, "Antares secures BWXT fuel agreement", 27 Oct 2026. https://www.powermag.com/antares-secures-bwxt-fuel-agreement-advances-doe-review-for-electricity-producing-mark-1/
- [S35] Standard Nuclear, Form 10-Q for Q2 2026 (Aug 2026). https://www.sec.gov/Archives/edgar/data/0002086716/000162828026059189/nucl-20260630.htm
- [S36] ANS, "NRC grants license for TRISO-X fuel manufacturing using HALEU", 17 Feb 2026. https://www.ans.org/news/2026-02-17/article-7762/nrc-grants-license-for-trisox-fuel-manufacturing-using-haleu/
- [S37] World Nuclear News, "Kairos, BWXT team up for commercial TRISO fuel production", Sep 2025. https://world-nuclear-news.org/articles/kairos-bwxt-team-up-for-commercial-triso-fuel-production
- [S38] Centrus, Q3 2026 results release, 4 Nov 2026, https://www.sec.gov/Archives/edgar/data/0001065059/000162828026070229/ex991-10q2026_11x04.htm ; Centrus Q3 2026 call transcript, 5 Nov 2026, https://www.fool.com/earnings/call-transcripts/2026/11/05/centrus-energy-leu-q3-2026-earnings-call-transcript/
- [S39] DOE, "Energy Department to Distribute Third Round of HALEU to NASA and Radiant", 23 Jul 2026. https://www.energy.gov/ne/articles/energy-department-distribute-third-round-haleu-nasa-and-radiant
- [S40] International Panel on Fissile Materials blog, "Plans to expand the enrichment capacity", Jun 2026 (secondary). https://fissilematerials.org/blog/2026/06/plans_to_expand_the_enric.html
- [S41] Federal Register, Part 53 final rule, 30 Mar 2026. https://www.govinfo.gov/content/pkg/FR-2026-03-30/pdf/2026-06048.pdf
- [S42] Federal Register, Executive Order 14301, 29 May 2025. https://www.govinfo.gov/content/pkg/FR-2025-05-29/html/2025-09799.htm
- [S43] Executive Order 14299, "Deploying Advanced Nuclear Reactor Technologies for National Security", 23 May 2025. https://www.presidency.ucsb.edu/documents/executive-order-14299-deploying-advanced-nuclear-reactor-technologies-for-national
- [S44] INL, "Global Market Analysis of Microreactors", INL/EXT-21-63214, Jun 2021. https://gain.inl.gov/content/uploads/4/2024/04/Document-INL-EXT-21-63214.pdf
- [S45] INL, "Technoeconomic Evaluation of Microreactor Using Detailed Bottom-up Estimate", INL/RPT-24-80433, Aug 2024. https://gain.inl.gov/content/uploads/4/2025/03/2024-Document-INL-RPT-24-80433.pdf
- [S46] INL, "Meta-Analysis of Advanced Nuclear Reactor Cost Estimations", INL/RPT-24-77048 Rev. 2, Jul 2024. https://inldigitallibrary.inl.gov/sites/sti/sti/Sort_107010.pdf
- [S47] EIA, average retail price by sector, 2024 (Table 4). https://www.eia.gov/electricity/sales_revenue_price//pdf/table_4.pdf
- [S48] NEI Magazine, "Equinix signs nuclear data centre deals" (date not verified). https://www.neimagazine.com/news/equinix-signs-nuclear-data-centre-deals/
- [S49] Investing.com, BWXT Q3 2026 earnings call summary ("shares fall after hours"), 2 Nov 2026. https://www.investing.com/news/transcripts/earnings-call-transcript-bwx-technologies-posts-q3-2026-eps-beat-shares-fall-after-hours-93CH-4993167
- [S50] World Nuclear News, Valar NOVA criticality, Nov 2025, https://world-nuclear-news.org/articles/valar-atomics-project-achieves-early-criticality-milestone ; ANS, 18 Nov 2025, https://www.ans.org/news/2025-11-18/article-7548/valar-achieves-cold-criticality-at-lanl/
- [S51] The Bear Cave #100, 16 Jan 2022 (reports the Jehoshaphat Research short report). https://thebearcave.substack.com/p/the-bear-cave-100
- [S52] BWXT company boilerplate calling itself sole manufacturer of naval reactors and sole provider of naval fuel (e.g. BWXT release on USS Gerald R. Ford, date not verified). https://www.bwxt.com/?p=878
- [S53] Tommy Lau, "Nuclear power for AI comes from old reactors first. The new ones wait on fuel.", The Physical Layer, 29 Sep 2026, with evidence to 21 Oct 2026. Local file: /Users/tommylau/Desktop/journal/src/content/journal/nuclear-for-ai.md
- [S54] IAEA, small modular reactors topic page (not re-fetched this session). https://www.iaea.org/topics/small-modular-reactors
- [S55] POWER magazine, "Westinghouse Secures First Customer for eVinci Nuclear Microreactor" (Saskatchewan Research Council). https://www.powermag.com/westinghouse-secures-first-customer-for-evinci-nuclear-microreactor/

### What I could not verify

1. The 10-Q statement that about 46% of backlog converts to revenue by end 2027. Reported by a third party (FourWeekMBA); the fetch of the 10-Q cut off before that note.
2. BWXT's revenue split by contract type for 2025 or 2026 (the 10-K for 2024 describes types, not percentages).
3. That BWXT is the "sole" naval reactor and fuel supplier, from a government rather than company source.
4. BANR coolant (nitrogen) and fuel form (UCO TRISO): from POWER, not a BWXT document I could open.
5. Tata Chemicals' letter of intent for up to eight BANRs (POWER only).
6. Which INL facility will host Pele's operation.
7. The precise enrichment of naval fuel (classified; public estimates only).
8. X-energy XENITH's current size and any 2026 hardware milestone.
9. Deployable Energy's fuel; General Atomics' Janus coolant.
10. Executive Orders 14300 and 14302 text (only secondary summaries read), including the 400 GW by 2050 goal and the NRC 18-month deadline.
11. Urenco's Capenhurst HALEU figures (27 tonnes, 2031) and Orano's HALEU plans: secondary source only.
12. The Russia figures (26% share, waivers to 1 January 2028): carried over from nuclear-for-ai, not rechecked.
13. Whether any sixth DOE-authorised criticality has happened since 5 August 2026.
14. Peer valuation multiples for defence primes (used only as "as argued" in the bear case).
15. Who builds the Navy's microreactor at NSWC Crane (Geveden said "a competitor").
16. Why the shares fell 42%: commentary only, no single verified cause.

### Where newer facts bear on nuclear-for-ai

1. **Contradiction, needs updating.** The piece's heading "America stopped making HALEU in June 2026" and its line that DOE "ordered maintenance and storage only" are overtaken. Centrus's Q3 release (4 Nov 2026) says it is now enriching HALEU for the commercial market from the same 16-centrifuge cascade, with DOE permission, though DOE will not fund operation in FY2027 and no volume is disclosed [S38].
2. **Partly affected.** "None has a commercial fuel supply being made today" (on TerraPower, Oklo, Kairos) still holds for named customers, since Centrus names none of them for the restarted output; Centrus names X-energy, Radiant and Antares as prepaying customers [S38].
3. **Consistent.** Oklo Aurora-INL 75 MWe and 2028; the DOE HALEU rounds (three rounds, nine recipients, latest 23 July 2026); TerraPower and Kairos dates; the 1 tonne by July 2032 task order.
4. **New context the piece does not cover.** Oklo's Groves isotope reactor went critical on 5 August 2026 (a test reactor, not power) [S23]; Kairos Hermes 1's construction deadline moved to 30 April 2029 [S32]; Janus and ANPI could add HALEU microreactors, but well under 100 MW by 2030 and mostly behind the meter on bases, so the piece's 100 MW grid test is not threatened by them.
