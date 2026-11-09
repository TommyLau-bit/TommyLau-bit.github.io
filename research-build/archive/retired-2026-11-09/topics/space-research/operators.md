# Orbital compute: who is doing what, in their own filings and statements

Research slice for the depth rebuild of `data-centres-in-space`. Compiled 7 November 2026. Newest first within each section.

Tags: [primary] = read today at the source (filing, regulator record, company page or release); [primary, prior read] = read at source on 2 Nov 2026 for the live piece and confirmed today only by EDGAR full-text search for the phrase; [press] = lead only, not for use as evidence; [calc] = my arithmetic, method shown. Financial figures appear only as evidence of the physical build; no share prices or valuations.

## Headline findings

1. **SpaceX has put a satellite mass on the public record.** Its FCC letter of 29 May 2026 on the orbital data centre application gives, for the shells below 600 km, a satellite of **3,000 kg**, **800 m² total area** and **100 m² of "Bus & Radiator Area"** [primary]. The live piece says no compute satellite has been weighed in public; that is now out of date.
2. **SpaceX's own AI1 page has changed.** Read 7 Nov 2026: compute payload "Up to 250 kW peak / 175 kW average", "Vehicle efficiency 75 kW / ton", solar array 210 kW at 250 W/m², "Deployable liquid radiator 160 m²" [primary]. The piece still uses Musk's June draft of 150 kW peak and 120 kW sustained.
3. **On SpaceX's own figures, no stated design reaches 100 kW per tonne.** 175 kW over the filed 3,000 kg is 58 kW per tonne; even the 250 kW peak is 83 [calc]. The page's own 75 kW per ton is a quarter short of the prospectus target.
4. **The new radiator figure is cooler than the piece assumes.** 175 kW over 160 m² is about 1,090 W/m², which a two-sided panel sheds near 47°C, not the 67°C the piece infers from 1,400 W/m² [calc]. At the space station's 14 kg/m², 160 m² of radiator alone is 2,240 kg, three quarters of the filed 3,000 kg [calc].
5. **What has flown is small.** Starcloud-1 (60 kg, one Nvidia H100, launched 2 Nov 2025), Google and Planet's Suncatcher prototype (launched 1 Oct 2026, first answer 30 Oct 2026, no mass or power published), Axiom's two ODC nodes on Kepler relays (January 2026, press only) and China's Three-Body constellation (20 satellites after 14 Oct 2026, figures in operations per second, not kilowatts). None has published kilowatts per tonne.
6. **No licence yet.** No FCC grant found for SpaceX's one million (SAT-LOA-20260108-00016), Starcloud's 88,000 (SAT-LOA-20260202-00073, accepted for filing 13 Mar 2026) or Blue Origin's 51,600. The FCC's new Part 100 licensing regime (adopted 22 Jul 2026) keeps the debris rules.
7. **SpaceX's compute today is on the ground.** 1.7 GW of nameplate compute at end Q3 2026, a US$40 billion GPU finance lease for data centres (8-K, 26 Oct 2026), and no orbital compute in either 10-Q [primary].

---

## 1. SpaceX (Space Exploration Technologies Corp, CIK 1181412)

### 1a. SEC record, newest first

| Date | Document | What it says on orbital compute | Tag |
|---|---|---|---|
| 6 Nov 2026 | 8-K (event 4 Nov) | Director resignation only. No mention of satellites or compute. | [primary] |
| 26 Oct 2026 | 8-K, Item 8.01 (event 24 Oct) | Binding commitment for a master finance lease with an Apollo-managed entity for "graphics processing unit pods and related equipment" at data centres SpaceX selects; aggregate principal about US$40 billion; schedules about five to five and a quarter years; schedules expected to begin H1 2027. Terrestrial; no orbital mention. | [primary] |
| 22 Oct 2026 | 10-Q, quarter to 30 Sep 2026 | No mention of orbital compute, AI1, Starmind or radiators. Capex is terrestrial: servers and networking equipment US$43,206m gross at 30 Sep 2026 (US$22,694m at 31 Dec 2025); construction in progress US$23,745m, "primarily comprised of servers and networking equipment as well as data center infrastructure"; nine-month purchases of property, plant and equipment US$48,069m. xAI acquired 2 Feb 2026; the AI segment is now the "SI segment". EDGAR full-text search for "compute satellites", "orbital compute", "orbital data", "radiators", "Starmind" returns no 10-Q hit. | [primary] |
| 20 Oct 2026 | 8-K Ex. 99.1, Q3 results release | No orbital compute mention. "Completed Starship Flight 14, our first orbital Starship flight, delivering 26 Starlink V3 satellites"; Starbase Louisiana "designed to support thousands of Starship flights a year, with the first launch targeted for 2029". | [primary] |
| 4 Aug 2026 | 10-Q, quarter to 30 Jun 2026 | No full-text hit for any orbital compute term. | [primary] (search only) |
| 12 Jun 2026 | 424B4 final prospectus | Phrases "continue to be refined" (mass), "substantially larger radiators", "as early as 2028", "100 kilowatts of compute", "radiators" all present. Live piece quotes: "thermal control must be accomplished through radiation rather than convection and conduction"; 100 GW a year "via satellites carrying over 100 kilowatts of compute power per metric ton"; "approximately one million metric tons to orbit annually". | [primary, prior read] |
| 9 Jun 2026 | FWP, interview transcripts | Johnsen: "In 2028, we'll start flying if we stay on target"; "About 5 megawatts per launch"; "roughly 200 launches for every gigawatt". Musk: 250 W/m² solar, "about 1,400 watts per square meter for the radiators", 150 kW peak, about 120 kW average. Dahl: radiators "about the same size as the existing solar [arrays] for the V3 vehicle". | [primary, prior read] |
| 4 Jun 2026 | FWP, roadshow | "100KW Compute power per metric ton"; "100 Metric tons per launch over time"; "2028 Begin deployment on Starship"; "AI Satellite in design stage"; "Larger radiator"; "potential deployment of our orbital AI compute satellites as early as 2028". Risk factors: "we have not, and no one else has, previously operated or attempted to operate orbital AI compute"; "will not be easily repaired or upgraded"; "the useful life of our satellites is inherently shorter than that of the information technology systems"; "AI compute satellites at scale need full Starship reusability to be economically compelling"; nuclear advances could mean viability "may be materially diminished"; "we expect to incur significant capital expenditures over a period of years". | [primary] (re-read today) |
| 20 May 2026 | CORRESP | Contains "as early as 2028" (answer to staff comment 3 of 19 May). | [primary] (search only) |
| 19 May 2026 | SEC staff letter | Comment 3: "clarify when you may potentially begin deploying AI compute satellites". | [primary, prior read] |
| 24 Apr 2026 | SEC staff letter | Comment 26: asks for "total estimated solar collection area, total system mass, and on-orbit assembly requirements" and "power-to-mass ratios". Comment 31: "the material differences between connectivity satellites and AI compute satellites". | [primary, prior read] |
| 30 Mar 2026 | DRS (confidential draft, now public) | Already contains "100 kilowatts of compute", "orbital data", "radiators". | [primary] (search only) |

Capex specific to orbital compute: none disclosed separately in either 10-Q [primary]. The prospectus says only that significant capital expenditure is expected over years [primary].

### 1b. SpaceX company statements, newest first

- **20 Oct 2026, Q3 call** (transcript via stockanalysis.com; the call is primary, the transcript is a third party's). Shotwell: "we'll begin flying mobile V2 and Starmind satellites in 2027." Musk: "mass to orbit with the Starmind constellation"; "the constraint on deployment of superintelligence is more in power and cooling and infrastructure than it is in chips"; expects Starship "to fly weekly at some point in the first half of next year". Johnsen: "We ended the third quarter with 1.7 gigawatts of nameplate compute capacity" (ground); pricing "slightly above the high end of the $30 to $50 per watt range". Shotwell: "We'll attempt an on-orbit refueling early next year". No kW, mass or radiator figure for Starmind on the call. [primary, third-party transcript]
- **7 Nov 2026, read today: spacex.com/spacexsi/starmind** (the old /spacexai/ path redirects). AI1 overview: "Deployed height 30 m / 98 ft"; "Wingspan 75 m / 246 ft"; "Compute payload Up to 250 kW peak / 175 kW average"; "Vehicle efficiency 75 kW / ton". Thermal tab: "Deployable liquid radiator 160 m²", "Active fluid cooling", "Redundant pumping loops", "Integrated micrometeoroid shielding". Solar tab: "Solar array 210 kW", "Solar power density 250 W / m²", SpaceX-made cells from Bastrop. Text: "Gigasat Factory in Bastrop ... planned to enable rapid production and deployment of thousands of AI satellites starting as soon as late 2027"; "We are AI chip vendor agnostic"; cooling claim "reduce cooling power overhead by an order of magnitude". Limiting factors named: "mass to orbit, power generation, AI chips". No mass stated. [primary]
- **6 Oct 2026, Starmind space safety page** (reported): up to 1 million Starmind satellites plus up to 100,000 Starlink; Nicolls (X post): clusters of "10-ish satellites connected with 10 terabits or so". [press]
- **Earlier AI1 page version, July 2026** (reported by Notebookcheck, 11 Jul 2026): 150 kW peak, 120 kW average, 110 m² of liquid radiators, 70 m wingspan, 20 m tall; another report gives 70 kW per tonne. [press] [calc]: 150 kW over 110 m² is 1,364 W/m², close to Musk's 1,400.
- **4 Aug 2026**: SpaceX X post: "SpaceX is partnering with @Nvidia to design the Starmind AI1 satellite compute payload"; Vera CPUs and Rubin GPUs; prototype testing "early 2027" per the report. [press, relaying an X post]
- **Q2 call, week of 4 Aug 2026**: plans to start launching orbital data centres with Vera Rubin chips in 2027 (reported). [press]
- **June 2026**: the system named Starmind (reported). [press]

### 1c. FCC record, SpaceX Orbital Data Center System, ICFS SAT-LOA-20260108-00016 (call sign S00798)

- **29 May 2026, SpaceX letter to the FCC** (supplement "at the Commission's request"; ICFS attachment 52755717cf894b1068ecb8a42f851ce9) [primary]:
  - Representative configuration, six groups, 1,000,000 satellites in all: Group 1, 550 to 568 km, 26 to 32 degrees, 99,900; Group 2, 565 to 585 km, 97.7 degrees, 99,980; Group 3, 686 to 718 km, 30 degrees, 249,750; Group 4, 707 to 744 km, 97.2 degrees, 244,860; Group 5, 946 to 978 km, 30 degrees, 249,750; Group 6, 967 to 1,002 km, 99.4 degrees, 253,880.
  - "SpaceX will launch and operate its satellites beginning with the orbital shells at nominal altitudes below 600 km".
  - **DAS table for the four shells below 600 km: Area-to-Mass 0.1333 m²/kg; Total Area 800 m²; "Bus & Radiator Area" 100 m²; Mass 3000 kg**; passive decay 1.2 to 1.9 years; passive decay collision probability 2.66E-04 to 7.00E-04.
  - Solar arrays: "lightweight, flexible thin-film photovoltaic materials"; DAS run on the bus cross-section, "excluding the solar arrays".
  - Disposal: controlled re-entry below 600 km; asks a waiver to use "Earth disposal orbits or heliocentric orbits" above 600 km. Reserve "at least 50 m/s of delta-V"; about 60 collision avoidance manoeuvres.
  - Casualty risk: no component re-enters with more than 15 joules, "therefore the casualty risk is considered zero". Small debris design criterion "below 1e-4".
  - Ka band is "cold backup only"; may also carry "downlinking AI inference results for end users before disposing of a satellite".
  - [calc] The table's area-to-mass (0.1333) times 3,000 kg is 400 m², half the 800 m² total, so SpaceX appears to use a mean cross-section; do not read 0.1333 as a design ratio.
  - Caveat: filed when the public design was 150 kW peak / 120 kW average; the mass may refer to that design.
- **16 Mar 2026**: SpaceX consolidated opposition and response (cited in the letter above; gave a first representative configuration at 686 to 1,002 km). [primary, cited not opened]
- **6 Mar 2026**: Amazon (Amazon Leo) petition to deny; Blue Origin comment calling it "facially incomplete" (reported). FCC Chairman Carr publicly criticised Amazon's petition (reported, around 9 to 11 Mar 2026). [press]
- **4 Feb 2026, Public Notice DA 26-113**: accepted for filing; filed 30 Jan 2026; "up to one million satellites"; 500 to 2,000 km; 30 degree and sun-synchronous; Ka band on "a non-interference, unprotected basis"; waivers of 25.156(d)/25.157 (processing round), 25.164 (milestones), 25.165 (surety bond), 25.114(a)(1) (Schedule S); comments 6 Mar, responses 16 Mar, replies 23 Mar 2026; "first step towards becoming a Kardashev II-level civilization". [primary]
- **Status, 7 Nov 2026**: no grant, partial grant or denial found. [primary search of FCC public notices found none; ICFS not reachable from here]
- **September 2026** (reported, not found at the FCC): a 12-page SpaceX debris and re-entry response of about 18 Sep 2026 citing up to 4,000 kg per Starmind satellite; a public notice of 18 Sep 2026 said to accept 100,000 Starmind satellites for filing. Treat as unverified. [press]

### 1d. xAI link

- SpaceX "completed its acquisition of X.AI Holdings Corp. ('xAI')" on 2 Feb 2026; SpaceXAI Corp. (formerly X.AI Corp.) is a subsidiary; SI segment revenue US$7,022m in Q3 2026 (US$359m a year earlier), "continuous access to reserved compute capacity". [primary, 10-Q 22 Oct 2026]
- Starmind's role for xAI/Grok: no filing ties orbital capacity to Grok. [primary, absence]

### 1e. SpaceX, the numbers set side by side [calc]

| Basis | Compute or power | Mass | kW per tonne |
|---|---|---|---|
| Prospectus target (Jun 2026) | per tonne | | 100 |
| AI1 page, 75 kW/ton, at 175 kW average | 175 kW | 2.33 t implied | 75 |
| FCC letter mass, current page average | 175 kW | 3.0 t | 58 |
| FCC letter mass, solar array | 210 kW | 3.0 t | 70 |
| FCC letter mass, current page peak | 250 kW | 3.0 t | 83 |
| FCC letter mass, June design average | 120 kW | 3.0 t | 40 |
| Reported 4,000 kg (press), current average | 175 kW | 4.0 t | 44 |
| Johnsen, 5 MW per 100 t launch (Jun 2026) | | | 50 |

Radiator [calc, two faces, emissivity 0.92, no sunlight or Earth glow, Stefan-Boltzmann]: 175 kW / 160 m² = 1,094 W/m², panel near 320 K (47°C); 210 kW / 160 m² = 1,313 W/m², near 62°C; 250 kW / 160 m² = 1,563 W/m², near 77°C. At ISS heritage 14 kg/m², 160 m² weighs 2,240 kg, 75% of 3,000 kg. Solar: 210 kW at 250 W/m² is 840 m² of array, close to the FCC table's 800 m² total area.

---

## 2. Starcloud (formerly Lumen Orbit), Redmond, Washington

- **7 Nov 2026, starcloud.com/starcloud-2** [primary]: "Our first commercial mission, Starcloud-2, features a GPU cluster, persistent storage, 24/7 access, and proprietary thermal and power systems in a smallsat form factor. It will be fully operational in sun-synchronous orbit by 2027." No kW, mass or radiator figure. Starcloud-3 page is blank; Starcloud-4 page points to the white paper.
- **7 Nov 2026, starcloud.com/starcloud-1** [primary]: "launched in November 2025 with the first Nvidia H100 GPU in space"; "In December, StarCloud-1 became the first satellite to run a version of Gemini in space and the first spacecraft to train an LLM - the nano GPT model from Andrej Karpathy." Note: the Hassabis quote on the same page says Gemma, Google's open model, not Gemini. No power, run time or thermal data published.
- **29 Sep 2026, Astro Digital / Proem Acquisition Corp. I, Form 425 (SEC)** [primary]: Astro Digital, which is merging with the SPAC (agreement 26 Sep 2026), says "We designed and built Starcloud-1 on our Corvus-Micro platform in one and a half years"; it "launched in November 2025 carrying the first NVIDIA H100 GPU into orbit" and "has since run AI inference on orbit, including onboard image processing"; "The Corvus XL roadmap is designed for compute class payloads".
- **21 Aug 2026** (TechCrunch via TheNextWeb): Johnston says launch "is pretty constrained right now" because Falcon 9 "is scheduled to end in 2028"; Starcloud-2 as a pair of 8 kW satellites on rideshares in 2027; a later goal of 200 kW craft; a new raise reported. [press] No SpaceX filing gives a Falcon 9 end date [primary, absence in EDGAR search].
- **13 Mar 2026, FCC Report SAT-01982** [primary]: SAT-LOA-20260202-00073, call sign S00803, "Date filed: 2026-02-04", accepted for filing: "up to 88,000 satellites to operate as a distributed datacenter in space", sun-synchronous, 600 to 850 km, optical links to other LEO systems; back-up TT&C 18.8 to 19.3 and 28.6 to 29.1 GHz; waivers of 25.156, 25.157, 25.164, 25.165, 25.114(a)(1). Opposition: American Astronomical Society comment urging denial; Center for Space Environmentalism comment, April 2026 [press]. Status 7 Nov 2026: no grant found.
- **4 Feb 2026, application narrative** (Ezra Feilden, CTO) [primary]: "near-constant solar power, radiative cooling"; "Each deployed satellite will be functionally identical in size, mass, maneuverability, communications and control systems"; communications "nearly exclusively on laser links" via Starlink, Amazon LEO, TeraWave, Kepler; "Expansion and buildout of terrestrial energy infrastructure in the western world has not kept pace with the demand for AI". No mass, power or radiator figure.
- **Funding** [press]: US$170m Series A (March 2026); a further raise reported August 2026. Form D filings by many SPVs named for Starcloud, March to November 2026 [primary, EDGAR full-text search], which show only that investor vehicles were formed. Amounts and valuations not for use.
- **15 Oct 2025, Nvidia blog** [primary, partner statement, prior read]: "The 60-kilogram Starcloud-1 satellite, about the size of a small fridge"; plan for a "5-gigawatt orbital data center" with panels "approximately 4 kilometers in width and length".
- **2 Nov 2025, launch**: Bandwagon-4, Falcon 9 from Cape Canaveral, 18 payloads (Spaceflight Now, Space.com). [press]
- **Sep 2024, white paper v1.03** [primary, prior read]: 633.08 W/m² net at 20°C; about US$30/kg long-term launch assumption.
- [calc, assumption flagged] If all of a 700 W H100's power were counted as compute, Starcloud-1 would be at most about 12 kW per tonne (0.7 kW / 0.06 t). Starcloud has published no power figure, so this is an upper bound for illustration only.

---

## 3. Google and Planet (Project Suncatcher)

- **30 Oct 2026, Google blog, "We've received our first response..."** (Travis Beals, Senior Director, Paradigms of Intelligence) [primary]: "On October 1, we launched our prototype satellite"; first AI response from "a data center class TPU in orbit"; prompt to the onboard "Gemma 4 open model"; received "As the satellite passed by Svalbard, Norway"; next "a series of tests to evaluate how TPUs perform under thermal stress and radiation exposure in orbit"; next milestone "twin interconnected satellites in 2027". No TPU count, power, mass, thermal or run-time figure.
- **1 Oct 2026, Google blog, "Project Suncatcher prototype satellite is in orbit"** (Beals) [primary]: built with Planet; "launched into orbit aboard the Transporter-18 rideshare mission with SpaceX"; "is operating as expected". The post says a peer-reviewed paper is now available in *Joule* [primary statement; the Joule paper itself not opened].
- **2 Oct 2026, NPR**: four TPUs; Gemma runs "15 minutes at a time due to heat management constraints"; radiators "one of the heaviest components" (Beals). [press, used in the live piece]
- **24 Sep 2026, Google blog** (prior read): co-developed with Planet; Transporter-18; two satellites in 2027 to test laser links. [primary, prior read]
- **10 Dec 2025, Planet 8-K Ex. 99.1** [primary, prior read]: "Planet is contracted to deploy two prototype satellites, targeting launch in 2027." EDGAR full-text search finds no later Planet filing mentioning Suncatcher (searched 7 Nov 2026) [primary, absence]. So Planet's filings say two prototypes in 2027, while Google flew one in October 2026 and plans a pair in 2027: whether the October satellite is one of the two contracted is not stated anywhere I found.
- **22 Nov 2025, arXiv 2511.19468** [primary, prior read]: design paper; 575 kg and about 28 kW for Starlink V2 mini (Google's estimate); US$3,600/kg; US$200/kg threshold.

---

## 4. Others with dated statements

- **Nvidia.** 16 Mar 2026 (GTC keynote; release reported 17 Mar): Space-1 Vera Rubin Module for orbital data centres, "up to 25 times the AI compute of an H100 GPU"; also IGX Thor and Jetson Orin for space; users named: Aetherflux, Axiom Space, Kepler Communications, Planet, Sophia Space, Starcloud. No availability date or power figure in the coverage. [press; nvidianews release URL now redirects, not read] 4 Aug 2026: partner on SpaceX's AI1 compute payload (SpaceX X post, reported) [press]. Nvidia is an investor in Starcloud (logo on starcloud.com, read 7 Nov 2026) [primary].
- **Blue Origin.** Project Sunrise FCC application, filed 19 Mar 2026: up to 51,600 satellites, sun-synchronous, 500 to 1,800 km, complementing its 5,408-satellite TeraWave network; waivers asked include processing round and the half-deployment milestone; SpaceX filed against it (20 Mar 2026). File number and acceptance not found. [press]
- **Amazon (Amazon Leo, formerly Kuiper).** Petition to deny SpaceX's application, 6 Mar 2026: a "lofty ambition rather than a real plan" (reported). Amazon has filed no orbital compute system of its own that I found. [press] Note SpaceX's 29 May letter cites the FCC's Kuiper orbital debris approval (38 FCC Rcd 1112, 2023) as precedent for not filing DAS logs [primary].
- **Aetherflux.** 9 Dec 2025: "Galactic Brain" orbital data centre, first satellite targeted for Q1 2027, after a 2026 power-beaming demonstration (company Medium post and press). [press] Named by Nvidia as a space computing user [press].
- **Axiom Space.** Two orbital data centre (ODC) nodes hosted on Kepler Communications optical relay satellites, launched 11 Jan 2026 on Falcon 9 from Vandenberg; follow-on from AxDCU-1 on the ISS (2025); an ISS ODC node planned for 2027. No power or mass published. [press; no Axiom or Kepler release opened]
- **Sophia Space.** TILE ("Thermal Integrated LEO Edge") compute modules that cool passively; 23 Jun 2026 release: demo on an Apex Nova bus in 2027; Redwire memorandum of understanding (reported 30 Sep 2026). [press]
- **Lonestar Data Holdings (lunar).** "Freedom" storage payload flew on Intuitive Machines' IM-2 Athena lander (launched 26 Feb 2025; the lander tipped on landing, March 2025). Storage, not compute. Reported later agreement with Sidus Space for cis-lunar storage satellites. [press]
- **Astro Digital** (bus maker for Starcloud-1): see section 2. [primary]
- **Sidus Space.** Shareholder letter, 8-K 21 Jul 2026: "We also see significant long-term opportunity in orbital data centers"; Fortis VPX availability "early 2027". [primary] No orbital compute hardware flown.
- **Relativity Space.** Eric Schmidt, chief executive since 2025, has said orbital data centres motivated his purchase (X post, reported). No orbital compute programme announced; Terran R not yet flown to orbit. [press]
- **China.** Three-Body Computing Constellation (ADA Space with Zhejiang Lab): 12 satellites launched 14 May 2025 on Long March 2D from Jiuquan; first batch "5 POPS" in total, 30 TB storage, laser links to 100 Gbps (Hangzhou city government site, 15 May 2025) [press, state source, prior read]; press gives 744 TOPS per satellite and a 2,800-satellite goal. Second batch: 8 satellites on LandSpace Zhuque-2E Y4 from Jiuquan, 14 Oct 2026, bringing the constellation to 20 (China in Space, citing LandSpace) [press]. A 192-hour laser link reported 29 Jul 2026 [press]. 100 satellites targeted by 2027 [press]. No power, mass or thermal figure published.
- **Hyperscalers other than Google.** None has filed an orbital compute system with the FCC that I found. Microsoft and Meta: no dated statement found. [absence]

---

## 5. What has flown, against what is announced

| Item | Flown | Date | Compute | Power | Mass | Source tag |
|---|---|---|---|---|---|---|
| Starcloud-1 | Yes | 2 Nov 2025 | 1 Nvidia H100; trained nanoGPT, ran Gemma (Dec 2025) | Not published | 60 kg | [primary] Nvidia blog, Starcloud page; launch date [press] |
| Three-Body, batch 1 | Yes | 14 May 2025 | 5 POPS across 12 satellites | Not published | Not published | [press, state source] |
| Three-Body, batch 2 | Yes | 14 Oct 2026 | 8 satellites; not stated | Not published | Not published | [press] |
| Axiom ODC nodes | Yes, hosted on Kepler | 11 Jan 2026 | Not stated | Not published | Not published | [press] |
| Suncatcher prototype | Yes | 1 Oct 2026 | Data-centre-class TPU (four, per NPR); Gemma 4 answer 30 Oct | Not published (about 1 kW in press) | Not published | [primary] Google blog; TPU count [press] |
| Starcloud-2 | No | "by 2027" | GPU cluster; 8 kW each (press) | 8 kW [press] | Not published | [primary] page |
| Suncatcher pair | No | 2027 | Laser-link test | Not published | Not published | [primary] |
| Aetherflux first node | No | Q1 2027 target | Not stated | Not published | Not published | [press] |
| SpaceX AI1 / Starmind | No | "as soon as late 2027"; flights "in 2027" | 175 kW average, 250 kW peak | 210 kW solar | 3,000 kg (FCC, 29 May 2026) | [primary] |

Announced capacity: SpaceX, up to one million satellites and 100 GW a year (prospectus); Starcloud, up to 88,000 satellites and a 5 GW design; Blue Origin, 51,600 satellites [press]. [calc] Everything flown so far is a few kilowatts at most per satellite, while the announcements are in gigawatts: a gap of roughly six orders of magnitude.

---

## 6. Regulators and rules that bind large constellations

- **FCC Space Modernization Report and Order (FCC 26-47), adopted 22 Jul 2026** [press, law-firm summaries; order not opened]: new Part 100 replaces Part 25 licensing; "default to yes" presumption; drops surety bonds for NGSO systems licensed outside a processing round (which bears on SpaceX's and Starcloud's bond waiver requests); keeps existing debris mitigation rules and adds a duty to share space situational awareness data; Further Notice on experimental space licences.
- **FCC deployment milestones (Part 25.164)**: 50% in six years and 100% in nine for processing-round NGSO systems; SpaceX, Starcloud and Blue Origin all asked for waivers [primary for SpaceX and Starcloud requests].
- **FCC precedent, 9 Jan 2026, DA 26-36 (cited in DA 26-113)**: Starlink Gen2 upgrade, 7,500 more satellites (15,000 total Gen2), deferring 14,988 including those above 600 km; half of the authorised number due by 1 Dec 2028 (reported). [primary citation; terms press]
- **FCC orbital debris rules applied in the record**: small-debris collision probability 0.01 or less per satellite; casualty risk below 1 in 10,000; disposal by re-entry for satellites below 2,000 km unless waived (25.114(d)(14)) [primary, as quoted in SpaceX's 29 May 2026 letter]. The five-year post-mission disposal rule for LEO (FCC 22-74, Sep 2022) [from memory; not re-opened today].
- **ITU**: Resolution 35 (WRC-19) milestones for NGSO filings (10% within two years after the bringing-into-use period, 50% within five, 100% within seven) [from memory; not re-opened today]. SpaceX asks altitude and inclination tolerances "that align with those of the ITU under Resolution 8" [primary, 29 May letter]. Blue Origin reportedly told the FCC it had not yet made an ITU filing for Sunrise [press].
- **Astronomy and debris objections**: American Astronomical Society comments against Starcloud's application and against SpaceX's (2026) [press]; academic criticism of SpaceX's September debris analysis (Hugh Lewis, University of Birmingham, quoted by SatNews, 19 Sep 2026) [press].

---

## 7. What the live piece has wrong or out of date

1. **Live text:** "In April American regulators asked SpaceX for its system's mass; it is still being refined. Orbit can still work, but no compute satellite has been weighed in public." Also "Nobody has published what a compute satellite weighs" and "The mass is the number withheld."
   **Correction:** SpaceX's FCC letter of 29 May 2026 gives a mass of 3,000 kg, total area 800 m² and bus and radiator area 100 m² for its satellites in the shells below 600 km. The prospectus wording ("continue to be refined") is still the SEC position, but a mass is on the FCC record. Say: the SEC asked and got no total; the FCC record carries 3,000 kg per satellite; no flown compute satellite has been weighed.
   **Source:** SpaceX letter to FCC, ICFS SAT-LOA-20260108-00016, 29 May 2026, p. 6 table [primary].

2. **Live text:** "Musk's draft first satellite, 120 kW sustained, about one rack of GB300 chips ... can therefore weigh no more than about 1.2 tonnes in all, with 480 m² of solar array." And the evidence row "150 kW peak, 120 kW sustained".
   **Correction:** SpaceX's AI1 page now gives 250 kW peak and 175 kW average compute, a 210 kW solar array at 250 W/m², a 160 m² deployable liquid radiator and 75 kW per ton. At 100 kW per tonne, 175 kW allows 1.75 t; SpaceX's filed mass is 3.0 t. Solar at 210 kW is 840 m² [calc]. Nvidia Vera Rubin, not GB300, is the named payload (Aug 2026, press).
   **Source:** spacex.com/spacexsi/starmind, read 7 Nov 2026 [primary]; SpaceX FCC letter 29 May 2026 [primary].

3. **Live text:** "SpaceX's web page for AI1, its first AI satellite, gives '75 kW / ton', a quarter short if read as compute per tonne launched."
   **Correction:** Still right, and now testable against the filed mass: 175 kW over 3,000 kg is 58 kW per tonne; 250 kW peak is 83 [calc]. The 75 figure implies 2.33 t at 175 kW, so the page and the FCC mass differ, perhaps because the mass was filed for the earlier 120 kW design.
   **Source:** as above [primary] [calc].

4. **Live text:** "SpaceX assumes 1,400 watts shed per square metre, which on my arithmetic means a panel near 67°C" (and the chart point and choke-point diagram "1,400 W/m², near 67°C").
   **Correction:** That was Musk's June 2026 interview figure. The current page's 160 m² radiator for 175 kW average works out at about 1,090 W/m², a panel near 47°C on the same arithmetic; at the 210 kW array it is about 1,310 W/m², near 62°C [calc]. The earlier July page (110 m² for 150 kW peak) matched 1,400 [press]. The piece should date the 1,400 figure and add the current one. At 14 kg/m², the 160 m² radiator alone would weigh 2,240 kg, 75% of the filed 3,000 kg [calc].
   **Source:** SpaceX AI1 page, read 7 Nov 2026 [primary]; FWP 9 Jun 2026 [primary, prior read].

5. **Live text (claim watch list in claims.ts, also echoed in the piece's SEC table):** first flights "as early as 2028".
   **Correction:** That is the prospectus wording of 12 June 2026. SpaceX now says "we'll begin flying ... Starmind satellites in 2027" (Shotwell, 20 Oct 2026) and the Gigasat Factory enables deployment "starting as soon as late 2027" (AI1 page). The piece body already cites Shotwell; the table row and the claims.ts watch wording are stale. (Claims are never reworded; the watch list is Tommy's call.)
   **Source:** Q3 call transcript, 20 Oct 2026 [primary, third-party transcript]; spacex.com/spacexsi/starmind [primary].

6. **Live text:** "Starcloud's application of 4 February 2026 to the FCC ... asks for up to 88,000 satellites; SpaceX's, accepted for filing that day, asks for up to one million."
   **Correction:** Accurate but incomplete. Starcloud's application (SAT-LOA-20260202-00073, filed 4 Feb 2026) was accepted for filing on 13 March 2026. Neither application has been granted as of 7 Nov 2026.
   **Source:** FCC Report No. SAT-01982, 13 Mar 2026 [primary]; DA 26-113, 4 Feb 2026 [primary].

7. **Live text:** "Google's Suncatcher paper (arXiv, 22 November 2025), a research design..."
   **Correction:** Google's blog of 1 Oct 2026 says a peer-reviewed version is now published in *Joule*. Cite the journal version if its figures match (not opened today).
   **Source:** Google Research blog, 1 Oct 2026 [primary].

8. **Live text:** "Google and Planet launched a Suncatcher prototype on a SpaceX rideshare on 1 October 2026 ... carries four of Google's TPU chips and runs Gemma".
   **Correction:** Launch, rideshare and the 30 Oct first answer are confirmed by Google. Google names the model as "Gemma 4". The count of four TPUs is NPR's, not Google's; keep it labelled as a press report. Planet's only filing still says two prototypes "targeting launch in 2027", so whether the October satellite is one of the contracted two is unstated.
   **Source:** Google blogs, 1 and 30 Oct 2026 [primary]; Planet 8-K, 10 Dec 2025 [primary].

9. **Live text:** "The filings count capacity" and "Gigawatts are announced, and kilograms are not" as the section's spine.
   **Correction:** Kilograms are now partly announced: 3,000 kg (FCC), 75 kW per ton (SpaceX page). What is missing is a flown, weighed compute satellite. The spine should move from "mass withheld" to "the stated mass misses the stated target".
   **Source:** items 1 to 3 [primary].

10. **Live text:** "SpaceX flies the rockets every orbital builder needs" and the launch-fare section, which does not mention Starship's progress.
    **Correction:** Add that Starship reached orbit for the first time on Flight 14 in Q3 2026, delivering 26 Starlink V3 satellites, and that SpaceX targets weekly flights in H1 2027 and a ship-and-booster catch on Flight 15. Still no published price per kilogram.
    **Source:** SpaceX Q3 2026 release, 8-K Ex. 99.1, 20 Oct 2026 [primary]; Q3 call [primary, third-party transcript].

11. **Live text:** exposure map and body name only SpaceX, Starcloud, Google, Nvidia and Planet.
    **Correction (out of date, not wrong):** Astro Digital built Starcloud-1's bus (SEC Form 425, 29 Sep 2026) [primary]; Blue Origin has its own 51,600-satellite filing [press]; China's Three-Body constellation has 20 satellites in orbit after 14 Oct 2026 [press]. Whether to add any is an editorial call.

12. **Live text:** "Starcloud's next two satellites, of 8 kW each, on rideshares in 2027."
    **Correction:** Starcloud's own page says only that Starcloud-2 "will be fully operational in sun-synchronous orbit by 2027"; the 8 kW and the pair remain press figures. Also, Starcloud's page says Starcloud-1 ran "a version of Gemini", while the endorsement on the same page says Gemma; use Gemma.
    **Source:** starcloud.com/starcloud-1 and /starcloud-2, read 7 Nov 2026 [primary].

---

## 8. Could not verify

1. The September 2026 SpaceX FCC debris and re-entry filing (reported 18 Sep 2026) and its "up to 4,000 kg" Starmind mass; and the reported FCC public notice of 18 Sep 2026 accepting 100,000 Starmind satellites. Not found on docs.fcc.gov; ICFS not reachable from here.
2. Whether the 3,000 kg in the 29 May 2026 letter refers to the 120 kW design or the current 175 kW design.
3. FCC grant status of SAT-LOA-20260108-00016 and SAT-LOA-20260202-00073 beyond the absence of any public notice found; Blue Origin's file number and acceptance.
4. The 424B4 pages (about pp. 149 to 154) were not re-read today; the key phrases are confirmed present by EDGAR full-text search, and the 4 Jun 2026 roadshow FWP was re-read.
5. Musk's "more than 250 kW of solar power" per Starmind (X post, reported 2 Oct 2026); the page now says 210 kW array and 250 kW peak compute, so the press wording may conflate the two.
6. Nvidia's Space-1 Vera Rubin release text (newsroom URL redirects); module power and availability.
7. Axiom ODC node launch and specifications (no Axiom or Kepler release opened).
8. Starcloud-1 power draw, H100 duty cycle and thermal results; Starcloud-2 power (8 kW) and date; Starcloud funding amounts.
9. Three-Body figures (POPS, TOPS, satellite count) from ADA Space or Zhejiang Lab directly; the third batch.
10. The *Joule* version of Google's Suncatcher paper.
11. FCC 22-74 five-year disposal rule and ITU Resolution 35 milestone percentages: stated from memory, not re-opened today.
12. FCC 26-47 (Part 100) order text: summarised from law-firm notes.
13. Number of TPUs and power on the Suncatcher prototype (NPR and aggregators only).
14. Aetherflux's Q1 2027 schedule and whether its 2026 power-beaming demonstration flew.
15. The exact TechCrunch wording and date (21 Aug 2026) of Johnston's Falcon 9 remark.

## Sources opened today (7 Nov 2026)

- SpaceX EDGAR submissions index, data.sec.gov/submissions/CIK0001181412.json; EDGAR full-text search (efts.sec.gov) for the phrases listed in 1a.
- SpaceX 10-Q, 22 Oct 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm
- SpaceX 8-K and Ex. 99.1, 20 Oct 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026066482/spaceexplorationtechnologi.htm
- SpaceX 8-K, 26 Oct 2026: https://www.sec.gov/Archives/edgar/data/1181412/000110465926118614/tm2628247d1_8k.htm
- SpaceX 8-K, 6 Nov 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026071689/spcx-20261104.htm
- SpaceX roadshow FWP, 4 Jun 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026040610/spacexfwp.htm
- SpaceX letter to FCC, 29 May 2026: https://api-prod.fcc.gov/icfs-attachment/exp/api/v1/52755717cf894b1068ecb8a42f851ce9
- FCC DA 26-113, 4 Feb 2026: https://docs.fcc.gov/public/attachments/DA-26-113A1.pdf
- FCC Report SAT-01982, 13 Mar 2026: https://docs.fcc.gov/public/attachments/DOC-419509A1.txt
- Starcloud FCC narrative, 4 Feb 2026: https://api-prod.fcc.gov/icfs-attachment/exp/api/v1/5c6840321b3e365068b6a64ce54bcb49
- SpaceX AI1 page: https://www.spacex.com/spacexsi/starmind (overview, thermal and solar tabs)
- Starcloud pages: https://www.starcloud.com/starcloud-1 , /starcloud-2 , /starcloud-3 , /starcloud-4 , /blog
- Proem Acquisition Corp. I Form 425, 29 Sep 2026: https://www.sec.gov/Archives/edgar/data/0002087446/000121390026104181/ea030690302-425_proem1.htm
- Sidus Space 8-K Ex. 99.1, 21 Jul 2026: https://www.sec.gov/Archives/edgar/data/1879726/000149315226034080/ex99-1.htm
- Google blogs: https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-prototype/ (1 Oct 2026) and https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-satellite-response/ (30 Oct 2026)
- Q3 2026 call transcript (third party): https://stockanalysis.com/stocks/spcx/transcripts/723936-q3-2026/
- Press leads: Teslarati (6 Oct 2026), Notebookcheck (11 Jul 2026, updated 5 Oct), SatNews (19 Sep 2026), Advanced Television (21 Sep 2026), Interesting Engineering (4 Aug 2026), The Register (17 Mar 2026), China in Space (Oct 2026), TheNextWeb (Aug 2026), Spaceflight Now (1 Nov 2025).
