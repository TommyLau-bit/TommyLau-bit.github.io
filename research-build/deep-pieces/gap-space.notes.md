# Gap scout: data centres in space (orbital compute), 2 Nov 2026

Scout only. No drafting. Every figure below was read at the URL given unless marked SECONDARY. "My arithmetic" is mine, from the primary figures, and must be labelled as such in any piece.

## Verdict in one line

NEW DEEP PIECE, provided it is framed as the physics and the disclosed design targets, not as a forecast that it will work. The primary record (Google preprint, SpaceX's SEC prospectus materials and the SEC staff's own comment letters, FCC applications, NASA ISS hardware figures, Starcloud's white paper and FCC filing, Planet's 8-K) is enough to carry one mechanism and one dated falsifiable claim.

## The mechanism the sources support

In a dawn-dusk sun-synchronous orbit the plug is nearly free: every operator files for that orbit for near-continuous sun, and none faces a grid queue. But heat can leave only by radiation, which scales with surface temperature to the fourth power. So the decisive number is mass per kilowatt launched (radiator plus solar plus chips plus bus), multiplied by launch price per kilogram. SpaceX's own target is 100 kW per tonne; ISS-heritage radiators alone, at Starcloud's own heat flux, would use more than twice that whole budget. The working hypothesis survives, with one sharpening: the radiator's temperature, set by how hot the chips' coolant may run, is the lever, which ties directly to heat-and-water (warm coolant lets a hall go dry on Earth; in orbit it shrinks the radiator).

Other constraints are real but secondary in the primary record: radiation (Google finds TPUs survive the dose; silent data corruption is the open issue for training), no repair (SpaceX risk factor), ground bandwidth (Google flags it; record 200 Gbps), spectrum (filings ask only Ka-band TT&C on a non-interference basis; data goes by laser). Spectrum and licensing are not the gate.

## Sources

### 1. Google, "Towards a future space-based, highly scalable AI infrastructure system design" (Project Suncatcher preprint). PRIMARY
- URL: https://arxiv.org/abs/2511.19468 (PDF https://arxiv.org/pdf/2511.19468; linked from Google Research blog via https://goo.gle/4qGsU8X). Blog: https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/ dated 4 November 2025.
- Authors Agüera y Arcas, Beals, Biggs, Bloom, Fischbacher, Gromov, Köster, Pravahan, Manyika (Google).
- Orbit: "dawn-dusk sun-synchronous low earth orbit (LEO) to enable near-continuous power generation". Illustrative cluster: 81 satellites, 1 km radius; blog gives mean altitude 650 km.
- Blog: "In the right orbit, a solar panel can be up to 8 times more productive than on earth."
- Cooling: "Cooling would be achieved through a thermal system of heat pipes and radiators while operating at nominal temperatures." Thermal management is listed among challenges "also discussed" but NOT quantified: "Effective thermal management is a critical optimization challenge for power-dense TPUs operating in a vacuum." No radiator area, mass or temperature is given anywhere in the paper. Key gap for the piece: Google's cost comparison rests on Starlink mass per kW, not on a designed compute satellite.
- Launch cost analysis: "$200/kg is often cited ... as a threshold beyond which launch could cease to be the limiting cost factor". Current price used: "$3,600/kg, based on Falcon 9 (reusable configuration)". Learning rate ~20%: "launch prices could fall to <$200/kg by ~2035" if "~180 Starship launches/year"; ~$300/kg if launched mass is 72% lower.
- Table 1, launched power price (launch cost amortised over life, $/kW/y): Starlink v2 mini 575 kg, 28 kW [est.], 5 y: $14,700 at $3,600/kg; $810 at $200/kg. Starlink v1 260 kg, 7 kW: $26,600 / $1,470. OneWeb 150 kg, 0.8 kW: $135,800 / $7,500. Iridium 860 kg, 2 kW, 12.5 y: $124,600 / $6,900.
- Terrestrial comparator: "power costs for ML-capable data centers in the US are reported to be $0.06-0.25/kWh and PUE ranges ~1.09-1.4, which yields annual power spend of $570-3,000/kW/y."
- Starlink v2 mini power is Google's estimate: ~105 m2 array (photometric), 22% cells, 1.361 kW/m2, 90% packing => ~28 kW. My arithmetic: 20.5 kg per kW, about 49 W/kg.
- Radiation (Trillium TPU v6e, 67 MeV protons): HBM irregularities after 2 krad(Si), "almost 3x" the 750 rad(Si) five-year shielded dose; no hard failures to 15 krad(Si). SDC "approximately one event/17 rad"; orbital dose ~150 rad(Si)/year; "on the order of 1 per 3 million inferences"; "the impact of SEEs on training jobs ... requires further study". Host SEFI one per 450 rad (CPU), 400 rad (RAM).
- Repair: "failed TPUs are manually replaced by technicians ... obviously impracticable in space. The simplest solution is redundant provisioning."
- Ground link: TBIRD "demonstrating 200Gbps ground-LEO communications in 2023". Inter-satellite: bench demo 800 Gbps each way (1.6 Tbps) per transceiver pair; target ~10 Tbps per link.

### 2. Planet Labs, Form 8-K Exhibit 99.1, results release, 10 December 2025. PRIMARY
- URL: https://www.sec.gov/Archives/edgar/data/1836833/000119312525314160/pl-ex99_1.htm
- "Suncatcher aims to put Google's Tensor Processing Units (TPUs) in space, where they can leverage the energy of the sun and shed excess heat into the cold of space."
- "Planet is contracted to deploy two prototype satellites, targeting launch in 2027."

### 3. SpaceX (Space Exploration Technologies Corp, SPCX), SEC record. PRIMARY
Filings list (EDGAR, CIK 1181412): DRS 30 Mar 2026; S-1 20 May 2026; S-1/A 1 and 3 Jun 2026; 424B4 12 Jun 2026; FWPs 4 to 9 Jun 2026; 10-Q Q3 22 Oct 2026. The 424B4 is over 10 MB and could not be read whole here; EDGAR full-text search confirms the phrases "orbital data centers", "radiative cooling", "100 kW", "thermal management", "one million satellites" and "compute satellites" all appear in the S-1, S-1/As and 424B4.

3a. FWP (roadshow, IPO site), filed 4 June 2026. https://www.sec.gov/Archives/edgar/data/1181412/000162828026040610/spacexfwp.htm
- Roadshow slide 44: "100KW Compute power per metric ton"; "100 Metric tons per launch over time"; "H2 2026 Commence payload delivery to orbit".
- Slide 64: "AI Satellite in design stage"; AI satellite changes include "Larger radiator".
- Slide 63: "Leverage radiative cooling architecture at lower cost relative to liquid or air cooling"; "Rocket reusability and high flight cadence reduces cost per kilogram to orbit eventually to the cost of fuel".
- Slide 52: Starship "99%+ Target Cost Reduction".
- Forward-looking statements: "potential deployment of our orbital AI compute satellites as early as 2028".
- Risk factors (from offset 100k): "the viability of orbital AI compute depends in part on the cost advantages of solar energy"; "To the extent that breakthrough developments in terrestrial energy access, such as advances in nuclear energy ... significantly reduce energy costs or alleviate infrastructure constraints ... the viability of our orbital AI compute infrastructure may be materially diminished." Also "AI compute satellites at scale need full Starship reusability to be economically compelling." "In-orbit refueling is complex, and we have not yet demonstrated or attempted it." "we have not, and no one else has, previously operated or attempted to operate orbital AI compute"; "will not be easily repaired or upgraded, such that any component failures could result in permanent capacity loss"; "the useful life of our satellites is inherently shorter than that of the information technology systems".
- NOTE for the piece: SpaceX itself ties the case to the ground plug. This is the cleanest link to the site's spine.

3b. FWP, interview transcripts, filed 9 June 2026 (posted 8 June 2026). https://www.sec.gov/Archives/edgar/data/1181412/000162828026041761/fwp_cfointerview.htm
- Bret Johnsen, CFO: "In 2028, we'll start flying if we stay on target." "in 2029, we'll have meaningful amounts of compute in space." "It's roughly 200 launches for every gigawatt that we put up." "About 5 megawatts per launch." "most of the cost is silicon." "roughly five times, if not more, energy per cell than they get terrestrially"; "in sun sync where the sun is on those cells 24 hours a day." On cooling: "extending the radiative cooling solutions that we're doing with Starlink".
- Elon Musk: "250 watts per square meter for the solar array"; "about 1,400 watts per square meter for the radiators"; "The 150-kilowatt peak power level roughly matches what say an NVIDIA GB300 rack would do"; "around 120 kilowatts average power"; reference design "NVIDIA Rubin chips, or ... GB300"; "a reference design for TPUs"; "cooling is actually much easier in space than it is on Earth"; aims "a gigawatt per year by the end of next year", "10 gigawatts a year" in 2.5 years, "maybe a hundred gigawatts" in 3.5 years, "this is not a promise".
- Ian Dahl: "about 120 kilowatts of average compute"; "the radiators themselves are about the same size as the existing solar rays [arrays] for the V3 vehicle".
- My arithmetic: 5 MW per 100 t launch is 50 kW per tonne, half the slide's 100 kW per tonne (the slide may be the long-run target, or payload-only). 120 kW at 1,400 W/m2 is about 86 m2 of radiator per satellite. 120 kW at 250 W/m2 is about 480 m2 of solar.
- My arithmetic (physics): 1,400 W/m2 from a two-sided, shaded radiator at emissivity 0.92 needs a surface near 340 K, about 67 C; at Starcloud's 20 C the same plate nets 633 W/m2. So SpaceX's figure implies coolant far warmer than the ASHRAE W45 (45 C) loop in heat-and-water. This is the heat-and-water link: the hotter the chips let the loop run, the smaller the radiator, by the fourth power.

3c. SEC staff comment letter, 24 April 2026 (UPLOAD). https://www.sec.gov/Archives/edgar/data/1181412/000000000026004247/filename2.txt
- Comment 26: staff note the orbital AI compute program "will require thousands of launches per year and delivery of approximately one million" tons to orbit, and ask SpaceX to disclose its assumptions for deploying 100 gigawatts of power to orbit annually, including "the total estimated solar collection area, total system mass, and on-orbit assembly requirements."
- Comment 31: staff quote SpaceX's "already solved the hardest part" and ask it to discuss "the material differences between connectivity satellites and AI compute satellites."
- Comment 16: asks that uncertain goals (Starship, orbital AI compute) be marked aspirational.
- Strong beat: the US securities regulator asked, in writing, for exactly the mass and area numbers this piece says decide the case.

3d. SpaceX response letter (DRSLTR), 7 May 2026. https://www.sec.gov/Archives/edgar/data/1181412/000162827926000584/filename1.htm
- To comment 26: "the disclosure on pages 5, 26, 27, 61, 138, 163, 181 and 182 of Submission No. 2 has been revised" and pp. 150 to 151 for the second bullet. To comment 31: pp. 149 to 150 revised. The letter itself does not restate mass or area. NOT VERIFIED: what the revised prospectus pages say on mass and area (424B4 too large to read here). Read pp. 149 to 151 of the 424B4 before drafting.

3e. SEC staff comment letter, 19 May 2026. https://www.sec.gov/Archives/edgar/data/1181412/000000000026005119/filename2.txt
- Comment 3: asks SpaceX to "clarify when you may potentially begin deploying AI compute satellites." Comment 15: Starship depreciation on a maximum useful life of 25 flights.

3f. SpaceX 10-Q, quarter to 30 September 2026, filed 22 October 2026. https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm
- Pages read show no orbital compute figures; capex is terrestrial (servers and networking $43,206m; construction in progress $23,745m "primarily comprised of servers and networking equipment"). Treat as: no orbital compute revenue or deployed capacity disclosed as of Q3 2026.

### 4. FCC, SpaceX Orbital Data Center System. PRIMARY
- Public notice DA 26-113, released 4 February 2026. https://docs.fcc.gov/public/attachments/DA-26-113A1.txt
- File SAT-LOA-20260108-00016, filed 30 Jan 2026: "up to one million satellites", "altitudes ranging from 500 km to 2,000 km", "in 30 degree and sun-synchronous orbit inclinations", shells "up to 50 km each". Spectrum only "18.3-19.3 GHz (space-to-Earth) and 28.6-29.1 GHz (Earth-to-space)" on a "non-interference, unprotected basis". Purpose: "first step towards becoming a Kardashev II-level civilization". No power or mass figures in the notice. Comments due 6 March 2026.
- SECONDARY (press): Amazon petitioned against it as lacking RF and orbital parameters; over 1,200 submissions. Status as of 2 Nov 2026 not verified (no grant found).

### 5. FCC, Starcloud Orbital Datacenter System application narrative, 4 February 2026. PRIMARY
- URL (ICFS attachment): https://api-prod.fcc.gov/icfs-attachment/exp/api/v1/5c6840321b3e365068b6a64ce54bcb49 ; file SAT-LOA-20260202-00073 per press (SECONDARY for the number).
- "up to 88,000 satellites"; "between 600 km and 850 km altitude in sun-synchronous orbit inclinations with a nominal 06:00 crossing time" (dawn-dusk). "near-constant solar power, radiative cooling". Communications "nearly exclusively on laser links" via third-party networks (Starlink, Amazon LEO, TeraWave, Kepler); Ka-band TT&C backup only. "Expansion and buildout of terrestrial energy infrastructure in the western world has not kept pace with the demand for AI". No satellite mass, power or radiator figures given.

### 6. Starcloud (formerly Lumen Orbit) white paper "Why we should train AI in space", v1.03, September 2024. PRIMARY (company claim)
- URL: https://starcloud.com/wp (PDF)
- Radiator physics: "A 1m x 1m black plate kept at 20°C will radiate about 838 watts to deep space (radiating from both sides), which is roughly three times the electricity generated per square meter by solar panels. As a result, these radiators need to be less than half the size of the solar arrays". Detailed: emissivity 0.92 gives 770.48 W/m2 two-sided; minus Earth 14.46 and sun 122.94 W/m2 absorbed = "633.08 W/m2 when held at 20°C". Heat pumps can raise radiator temperature "due to the T4 term".
- Launch assumption: "around $5 million per launch long term", 100 t to LEO SSO, "approximately $30 per kilogram"; ~40 MW per launch (300 racks at 120 kW).
- Table 1, 40 MW for 10 years: terrestrial energy $140m at $0.04/kWh vs space $2m solar; launch $5m "(single launch of compute module, solar & radiators)"; shielding $1.2m at 1 kg per kW. Totals $167m vs $8.2m. Note: radiator mass and cost are not itemised. Its launch price ($30/kg) is about 120 times Google's current $3,600/kg and below Google's own floor estimates.
- Scale: 5 GW with "a 4km x 4km deployed solar array and radiators".

### 7. Nvidia blog on Starcloud, 15 October 2025. PRIMARY (partner statement)
- URL: https://blogs.nvidia.com/blog/starcloud/
- "The 60-kilogram Starcloud-1 satellite, about the size of a small fridge"; first H100 in orbit, launch planned November; Starcloud projects energy "10x cheaper than land-based options, even including launch expenses"; plan for a "5-gigawatt orbital data center" with panels "approximately 4 kilometers in width and length".
- SECONDARY: Starcloud-1 launched November 2025 and trained nanoGPT and ran Gemma in orbit (CNBC 10 Dec 2025). Starcloud-2 (~8 kW, Blackwell, "largest commercial deployable radiator", claimed ~10x lower mass per watt than ISS radiator) slipped from October 2026 to 2027 per press; not launched as of 2 Nov 2026 as far as found. Starcloud raised $170m at $1.1bn (TechCrunch, 30 Mar 2026): not for use (valuation).

### 8. NASA / Boeing, "Active Thermal Control System (ATCS) Overview", hosted on nasa.gov (undated, uploaded 2021; describes assembly through 12A.1). PRIMARY
- URL: https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf
- "The EATCS is designed to provide 35 kW of heat rejection per loop for a total capability of 70 kW."
- Two rotating wings, each three radiator ORUs; "Each Radiator ORU measures 76.4 feet (23.3 meters) by 11.2 feet (3.4 meters) and weighs 2,475 pounds (1,122.64 kilograms)"; eight panels each; white Z-93 coating.
- PVR (solar array radiator): "can reject up to 14 kW"; "weighs 1,633 pounds (740.7 kilograms)", deployed 3.12 m x 13.6 m.
- My arithmetic: six ORUs = 6,736 kg for 70 kW, about 96 kg per kW of heat; 475 m2 planform, about 147 W per m2. PVR: about 53 kg per kW, 330 W/m2. (ISS loops run cold, a few degrees C, for crew modules; a compute loop can run far warmer, so these are a heritage ceiling, not a design point.)

### 9. NASA, Schunk, Babiak, Evans et al., "Thermal Control System Architecture and Technology Challenges for a Lunar Surface Habitat", IEEE Aerospace 2022 (NTRS 20210026557). PRIMARY
- URL: https://ntrs.nasa.gov/api/citations/20210026557/downloads/IEEE%202022%20Paper%20SH%20TCS%20Architecture%20and%20Technical%20Challenges%20Update.pdf
- Radiators "based on an areal density of the ISS Heat Rejection System thermal radiators (14 kg/m2)".
- My arithmetic, the crux: at Starcloud's own 633 W/m2 (20 C) and ISS areal density 14 kg/m2, the radiator alone is about 22 kg per kW, more than twice SpaceX's whole-satellite target of 10 kg per kW (100 kW per tonne) and above Google's whole Starlink v2 mini proxy of 20.5 kg/kW. At SpaceX's 1,400 W/m2, an ISS-density radiator for a 120 kW satellite (~86 m2) weighs about 1.2 t, the satellite's entire mass budget at 100 kW/t. So the target needs radiators several times lighter per m2 than ISS heritage, run much hotter, or both.

### 10. Gaalema, Indyk, Staley, "Reduced-Mass Orbital AI Inference via Integrated Solar, Compute, and Radiator Panels", arXiv 2604.07760, 9 April 2026. SECONDARY (independent preprint, not peer reviewed)
- URL: https://arxiv.org/abs/2604.07760
- Integrated design estimated at "about 500 W/kg", against "less than 100 for existing conventional implementations"; 16 MW, 150 t in one Starship hold; junction temperatures "near 40" C. Use only as a lead that the field itself treats W/kg as the figure of merit.

### 11. China, Three-Body Computing Constellation. SECONDARY (state media and city government site citing Zhejiang Lab)
- URLs: https://www.ehangzhou.gov.cn/2025-05/15/c_293651.htm ; https://subsites.chinadaily.com.cn/gansu/2025-05/15/c_1093014.htm
- 12 satellites launched 14 May 2025, Long March 2D, Jiuquan; Zhejiang Lab with ADA Space; first batch 5 POPS, 30 TB, laser links to 100 Gbps; goal 1,000 POPS. Press figures: 744 TOPS per satellite, 2,800 satellites. No power, mass or thermal figures. Zhejiang Lab's own page not found. Edge processing of satellite data, not a ground-hall substitute.

### 12. ESA / Thales Alenia Space ASCEND. SECONDARY
- Release (unreadable here): https://www.thalesgroup.com/en/news-centre/press-releases/thales-alenia-space-reveals-results-ascend-feasibility-study-space-data (June 2024)
- Press: needs a launcher "ten times less emissive" over its life to cut CO2; aim of 1 GW before 2050; 13 blocks, 10 MW by 2036 (TechSpot). Horizon Europe funded. Not verified at source.

### 13. Blue Origin FCC application (Project Sunrise). SECONDARY
- Press: up to 51,600 satellites, sun-synchronous 500 to 1,800 km, laser links via TeraWave; public notice around 19 March 2026. FCC document not opened. Verify before use.

## What could not be verified
- SpaceX's revised prospectus pages (pp. 149 to 151 of Submission 2 / 424B4) answering the SEC on solar area and total system mass: the 424B4 exceeds 10 MB and EDGAR blocked direct download (automated-tool block, not bypassed). Read these first; they may give the mass figure the claim turns on.
- Any measured radiator areal density for Starcloud's or SpaceX's radiators; Starcloud's "10x lower mass per watt than ISS" is press-relayed only.
- Starcloud-1's measured power, thermal results; Starcloud-2 date.
- FCC status of the SpaceX, Starcloud and Blue Origin applications as of 2 Nov 2026.
- An official current Falcon 9 price per kg (Google's $3,600/kg is its estimate); no published Starship price.
- Whether Google/Planet prototypes remain on track for 2027 beyond the December 2025 8-K.

## Candidate claim (for Tommy's approval; dated 2 Nov 2026)
"In orbit the power is nearly free and the heat is the bill: by 31 December 2028 no operator will report an AI compute satellite in service at SpaceX's own target of 100 kW of compute power per tonne launched, and no launch provider will publish a price to low Earth orbit at or below Google's $200 per kilogram threshold."
Breaks if: SpaceX, Starcloud, Google or any operator discloses (filing, release or regulator record) an orbital AI compute satellite operating at 100 kW or more per tonne of launched mass by 31 Dec 2028; or a launch provider publishes a list or contract price to LEO of $200/kg or less by then.
Watch: SpaceX 10-Qs/10-K (first AI satellite flights "as early as 2028", "demonstrate ... as soon as next year"); Starcloud-2 (2027); Google/Planet prototypes (2027); FCC actions on SAT-LOA-20260108-00016 and Starcloud's application.

## Map
Best fit: the existing `cooling` layer (the binding constraint is heat rejection; heat-and-water is the sibling), which needs no new Descent stop. Alternative: a new layer, e.g. `orbit` "Compute in orbit", kind energy, placed last in the chain, which would need its own stop in Descent.astro. Note the cooling layer's `constraint` line still carries the retired "30 and 50 kilowatts" band (heat-and-water corrected it); flag separately, not this scout's edit.
