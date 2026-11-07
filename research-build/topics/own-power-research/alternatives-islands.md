# Own power: the faster machines, off-grid campuses and their rules

Research slice for the "Building your own power" depth rebuild. Compiled 7 November 2026.

Labels: **PRIMARY** = filing, regulator, grid operator, court, company release or datasheet. **press** = press or law-firm summary only, not seen at source. **calc** = my arithmetic. Every figure is as at the date given; nothing here is a view on any share.

Context already in the live piece (not repeated unless something changed): GE Vernova queue (122 GW at 30 Sep 2026), aeroderivative orders 127 vs 39 shipped (9M 2026), Wärtsilä lead times "continue to increase" (27 Oct 2026), Socrates 556 MW vs 400 MW, Homer City netting, Hyperion 2,262 MW and 5,278 MW, NERC 1,800 MW event (Feb 2025), Bloom Q3 product revenue and Oracle 2.8 GW.

---

## 1. The alternatives to a heavy turbine

### 1a. Unit size, efficiency, start time (makers' ISO ratings)

| Machine | Type | Unit size | Efficiency (simple cycle, LHV) | Start | Source |
|---|---|---|---|---|---|
| GE Vernova LM2500XPRESS | Aeroderivative (jet-engine based) | about 34 to 36 MW | about 38.4 to 38.5% | not stated at source | GE LM2500XPRESS page, https://www.ge.com/power/en/lm2500xpress and https://www.gevernova.com/gas-power/products/gas-turbines/lm2500 PRIMARY |
| GE Vernova LM6000 (PF+) | Aeroderivative | about 44 to 58 MW by variant; LM6000VELOX PF+ Sprint 56.9 MW | up to about 41.3% (PF+); 41.0% (VELOX Sprint) | 5 minutes (GE LM6000 page) | GE LM6000 fact sheet https://www.ge.com/content/dam/gepower-pgdp/global/en_US/documents/product/lm6000-pf-plus-fact-sheet.pdf PRIMARY |
| Siemens Energy SGT-800 | Industrial (medium) turbine | 47.5 to 57.0 MW | over 40%; over 58.5% in combined cycle | n/a | Siemens SGT-800 brochure https://assets.new.siemens.com/siemens/assets/api/uuid:daeb2935-2ea5-4400-a5dc-653de64ca7d3/gas-turbine-sgt-800.pdf PRIMARY |
| Siemens Energy SGT-A35 | Aeroderivative | about 35 MW class | not found at source | | NOT VERIFIED |
| Mitsubishi Power FT8 MOBILEPAC | Aeroderivative, trailer-mounted | about 30 MW | not found | | press (MHI marketing; 2021 Mexico fast-track, five units) |
| Solar Turbines (Caterpillar) SMT-130 | Industrial turbine | about 16.5 MW (calc: 247 MW / 15 units at xAI Memphis) | | | calc from press-reported permit |
| Wärtsilä 18V50SG | Reciprocating gas engine | 18,875 kW (60 Hz) | 50.0% (60 Hz), heat rate 7,207 kJ/kWh; 5% tolerance | 2 minutes to full load | Wärtsilä 50SG leaflet https://wartsila.com/docs/default-source/power-plants-documents/downloads/product-leaflets/w50sg_leaflet.pdf PRIMARY |
| Wärtsilä 34SG | Reciprocating gas engine | about 10.3 MW (calc: 412 MW / 40 engines) | | | calc from Wärtsilä release 16 Apr 2026 |
| Caterpillar G3520K | Reciprocating gas genset | about 2.5 MW class | | | press (Joule release does not give unit size) |
| Caterpillar 10 MW engine | Reciprocating | 10 MW | | Restarted platform; ProPetro says "more than 1 gigawatt" of its secured capacity is these units | ProPetro 8-K, 28 Oct 2026 PRIMARY |
| INNIO Jenbacher J620 / J624 | Reciprocating | 3.22 MW / 4.80 MW | | | press (Cleanview tracker) |
| Bloom Energy solid oxide fuel cell | Fuel cell, modular | boxes added in steps | not taken | Bloom's aim: data centre power in 90 days (24 Jul 2025, in piece) | Bloom |

Heat derate (already in piece): aeroderivative loses nearly 26% of output at 45°C against ISO; engines under 2% (Wärtsilä comparison, maker's figure).

### 1b. Dated orders and deliveries

| Maker / route | Fact | Date | Source | Label |
|---|---|---|---|---|
| GE Vernova aero, Crusoe | 29 LM2500XPRESS, 10 units ordered Dec 2024 and 19 in Jun 2025, "almost 1 GW" (29 x about 35 MW = 1,015 MW, calc) | Release 22 Jul 2025 | https://www.gevernova.com/news/press-releases/ge-vernova-crusoe-announce-major-29-unit-aeroderivative-gas-turbine-deliver-ai-data-centers | PRIMARY. Which sites get them is NOT disclosed; tying them to Abilene is an analyst inference (Cleanview) |
| Wärtsilä 50SG | 282 MW, 15 x 50SG, for a data centre being developed by "a major US independent power producer"; booked Q3 2026; delivery 2028; "fully operational in 2029". Wärtsilä's "seventh data center-related order in the United States", US data centre capacity sold "more than 3 GW". Release does not say prime or backup power | 5 Oct 2026 | https://www.wartsila.com/media/news/05-10-2026-wartsila-to-supply-282-mw-onsite-power-solution-for-a-u-s-data-center-as-ai-growth-intensifies-demand-for-reliable-power-3797450 | PRIMARY |
| Wärtsilä 34SG | 412 MW, 40 x 34SG, hyperscale data centre in Ohio; booked Q2 2026; deliveries aligned to commercial operation "early 2028"; its "fourth data center related order in the USA", over 1.6 GW sold to US data centres. Trade press says primary power without reliance on the grid | 16 Apr 2026 | https://www.wartsila.com/media/news/16-04-2026-wartsila-s-34sg-engine-makes-its-data-center-debut-with-new-412-mw-u-s-project-3740972 | PRIMARY (order); press (primary-power wording) |
| Wärtsilä, read across | US data centre engine sales rose from over 1.6 GW (4 orders, 16 Apr) to over 3 GW (7 orders, 5 Oct): about 1.4 GW more in under six months | | | calc |
| Wärtsilä 50SG, Texas | 790 MW, 42 x 50SG, data centre under construction in Texas | 2026 (H1) | DatacenterDynamics | press |
| Caterpillar / Joule | Fleet of G3520K gensets for Joule's Utah campus, described as 4 GW total, plus 1.1 GWh grid-forming battery storage; no unit count or value | 7 Aug 2025 | Joule, Caterpillar and Wheeler release (via datacenterfrontier.com, rermag.com) | press of company release |
| Caterpillar results | Power Generation sales $3,421m in Q3 2026 vs $2,634m (in piece); 9M 2026 $9,336m, up 33%, "primarily in data center applications"; unsatisfied performance obligations on contracts over one year $49.4bn at 30 Sep 2026, about one-third to be recognised within twelve months (whole company) | 10-Q, Q3 2026 | https://www.sec.gov/Archives/edgar/data/0000018230/000001823026000057/cat-20260930.htm | PRIMARY |
| Caterpillar lead times | "taking some large reciprocating orders as far out as 2029 and turbine orders into 2030" (CEO, Q3 call) | 29 Oct 2026 | third-party transcript | press, not verified at webcast |
| Bloom Energy | Q3 2026 revenue $1,235.8m (+138.1%), product revenue $1,073.6m (+179.4%); GAAP gross margin 33.8%. Release does not mention Oracle, AEP or factory capacity | 22 Oct 2026 | https://www.sec.gov/Archives/edgar/data/0001664703/000162828026066890/ex991_q326financialresults.htm | PRIMARY |
| Bloom / Oracle | Oracle "intends to procure up to 2.8 GW"; initial 1.2 GW contracted, deployment under way | Release about 14 Apr 2026 | https://www.bloomenergy.com/news/bloom-energy-and-oracle-expand-strategic-partnership-to-deploy-up-to-2-8-gw-to-accelerate-ai-infrastructure-build-out/ | PRIMARY (company); agreement not found on EDGAR |
| Bloom / AEP | Up to 1 GW | Nov 2024 | in piece | PRIMARY |
| Bloom factory | Fremont capacity from 1 GW to 2 GW a year by end 2026; each added GW about $100m to $150m and six to nine months to install; site could reach about 5 GW | 2025 Form 10-K, 9 Feb 2026 | https://www.sec.gov/Archives/edgar/data/1664703/000162828026006516/be-20251231.htm | PRIMARY (via search summary; confirm wording in 10-K) |
| Batteries as buffer | xAI installed 168 Tesla Megapacks at Colossus (Memphis); more than $375m of Megapacks planned for Colossus 2 | 2025 | DatacenterDynamics | press |
| Batteries as buffer | Joule: 1.1 GWh grid-forming storage with the gensets; GW Ranch: 1.8 GW battery storage in plan; ProPetro's first data centre job is gas engines plus battery (60 MW, Midwest) | 2025 to 2026 | company releases | press of company releases |

### 1c. The rental fleets (mobile and modular power for hire)

| Company | Fact | Date | Source | Label |
|---|---|---|---|---|
| Solaris Energy Infrastructure | New 15-year, about 900 MW agreement (option for 15 more) with "a leading, investment-grade, diversified industrial and technology company"; deployments from 1H 2027, scaling through 2028; long-term contracted capacity 3.2 GW; pro forma generation capacity about 3.5 GW in 2029; "Procured time-advantaged equipment ... ahead of long OEM queues" | Release 4 Nov 2026 (contract signed 29 Oct) | https://www.sec.gov/Archives/edgar/data/0001697500/000162828026070286/sei-ex99x9302026.htm | PRIMARY |
| Solaris | Weighted average deployed capacity 818 MW in Q3 2026; Power Solutions revenue $284.2m vs $104.9m | 10-Q Q3 2026 | https://www.sec.gov/Archives/edgar/data/0001697500/000162828026071604/sei-20260930.htm | PRIMARY (via search summary) |
| ProPetro (PROPWR) | About 510 MW under contract (230 MW Targa, mostly oil and gas); 250 to 275 MW deployed by end 2026; "more than 500 megawatts by early 2028"; one hyperscaler job live in the Midwest, "built largely on 2.6-megawatt units"; "several hundred megawatts" of data centre deals in negotiation, could deploy "as early as late 2027"; cost about $1.4m to $1.5m per MW including balance of plant | 8-K 28 Oct 2026 | https://www.sec.gov/Archives/edgar/data/0001680247/000168024726000122/exhibit991-earningsrelea.htm | PRIMARY |
| VoltaGrid / Oracle | Up to 2.3 GW of modular gas generation for Oracle in Texas, INNIO Jenbacher engines, gas from Energy Transfer | 15 Oct 2025 | VoltaGrid release (via POWER, DCD) | press of company release |
| VoltaGrid / xAI | 14 mobile generators of 2.5 MW (35 MW) for xAI Memphis | 2024/25 | press | press |
| GE TM2500 (Fermi) | Seven GE TM2500 Gen 4 mobile units leased from MPS for Project Matador; pick-up 1 Jul to 30 Sep 2027; lease start expected Q3 2027 | 10-Q Q2 2026 | https://www.sec.gov/Archives/edgar/data/0002071778/000207177826000051/frmi-20260630.htm | PRIMARY |

Note for the piece: ProPetro's own cost, $1.4m to $1.5m per MW for engines and balance of plant, is a primary capital-cost point for the engine route (company guidance, not an audited cost).

---

## 2. Named off-grid and bridging campuses

| Campus | Machines on site | Load or commitment | Machine to load | Dates | Source / label |
|---|---|---|---|---|---|
| **Williams Socrates** (New Albany, Ohio; Meta affiliate) | Socrates North and South, "together have an expected 556 MW of capacity" | 400 MW "to the customer" (2025 10-K) | 1.39 (calc) | South "placed into service in late July 2026"; North "expected to be placed into service later in the fourth quarter of 2026" (10-Q) and "on track for in-service by mid-November" (release, 2 Nov). 10-year mainly fixed-price PPA; accounted as an operating lease | Williams 10-Q Q3 2026, https://www.sec.gov/Archives/edgar/data/107263/000010726326000036/wmb-20260930.htm PRIMARY |
| **Williams' next four** | Apollo (Ohio) 490 MW, 2H 2027, 12.5 yrs; Aquila (Utah) 520 MW, 2H 2027 and 1H 2028, 12.5 yrs; Socrates the Younger (Ohio) 340 MW, 2H 2028, 10 yrs; Neo (Ohio) 682 MW, 2H 2028, 12.5 yrs. "All expected in-service dates assume timely receipt of permits" | Customer and load not disclosed | n/a | Five projects total 2,588 MW (calc). July 2026: 49% interest (per Q2 10-Q) in the five sold for $5.34bn committed capital | Same 10-Q PRIMARY |
| **xAI Colossus 1** (Memphis, Tennessee) | Shelby County Health Department permit for 15 Solar SMT-130 turbines, up to 247 MW, issued 2 Jul 2025, expires 2 Jan 2027; stated purpose backup; imaging showed 24 on site; 168 Megapacks | Not disclosed | n/a | Appeal dismissed by Shelby County Air Pollution Control Board 6 to 1, 15 Dec 2025 | press (Action News 5, TechCrunch, Ars Technica); permit itself not opened |
| **xAI Colossus 2 / Southaven** (Mississippi plant serving Memphis data centre) | MDEQ Permit Board approved 41 permanent turbines (about 1.2 GW, press) on 10 Mar 2026; SELC says up to 27 unpermitted turbines were running; trackers put temporary units at 19 to 59 on various dates | Target about 1 GW (2025, press) | n/a | NAACP Clean Air Act suit: N.D. Miss. denied xAI's motion to dismiss, 30 Oct 2026, holding the plant is not a "mobile source" exempt from permitting; preliminary injunction not yet ruled; DOJ had backed xAI (Jun 2026) | Earthjustice release 30 Oct 2026 (party), Mississippi Today; court order not opened. press/party |
| **Stargate Abilene** (Crusoe, Oracle, OpenAI; Texas) | 10 gas turbines and 62 backup diesel generators under minor permits (permits by rule, standard permits) in 2024; major permit sought for 41 more turbines and 18 generators; permits allow continuous use but Crusoe told Floodlight the turbines are for backup; analyst count 360 MW initial | Campus about 1.2 GW (press) | n/a | Crusoe said on 18 Mar 2025 its Abilene turbines back up the grid (in piece) | Floodlight / Texas Tribune, 9 Jul 2026; Cleanview. press |
| **Oracle Frontier** (Shackelford County, Texas; VoltaGrid) | Oracle fact sheet (per tracker): off-grid microgrid on Jenbacher engines; 2.3 GW headline vs about 2.58 GW gross (250 J620 + 370 J624, calc by tracker) | Not disclosed at source | about 1.12 (gross vs headline, press) | First building targeted 2H 2026 (tracker) | Cleanview. press |
| **Meta Hyperion** (Louisiana) | Entergy plants 2,262 MW approved Aug 2025 (in piece); second agreement for seven CCGTs and about 240 miles of line, fast-tracked 4 to 1 on 15 Apr 2026, vote December 2026 | Hyperion described as 5 to over 7 GW | n/a | Grid-connected via Entergy, not islanded. No primary evidence of temporary on-site turbines found | Entergy (in piece); KPLC 15 Apr 2026 press |
| **Homer City** (Pennsylvania) | Seven 7HA.02 plus ten FT8 (in piece), up to 4,678 MW | Not disclosed | n/a | "early 2028" target (Mar 2026); EIA lists July 2028 for first units. No newer primary found | in piece |
| **Fermi America Project Matador** (Amarillo, Texas) | "approximately 11 gigawatts of private-grid power generation", expandable to about 17 GW; six Siemens SGT-800 acquired (Firebird), financing for six more SGT-800; three Siemens SGT6-5000F; seven TM2500 leased for Q3 2027 | Ground lease NTP needs a Phase 1 tenant of at least 200 MW; AMD credit support for a 222 MW lease reported (press) | n/a | No revenue at 30 Jun 2026; Q1 10-Q raised going-concern doubt; EIA lists 300 MW under construction (in piece) | Fermi 10-Q Q2 2026 PRIMARY; AMD press |
| **Pacifico GW Ranch** (Pecos County, Texas) | TCEQ air permit for up to 7.65 GW gas (late Jan 2026); plan 5 GW by 2031 with 1.8 GW battery and 750 MW solar; first 1 GW targeted 1H 2027; off-grid by design | Load not disclosed | 7.65 / 5 = 1.53 on the headline, but 5 GW is a generation target, not load (calc, weak) | | Pacifico release 26 Jan 2026 (Business Wire) PRIMARY company; TCEQ permit not opened |
| **Prometheus** (Pecos, Texas, 1.5 GW plan) | Executive: initial reciprocating-engine fleet "could require about 30% more installed generation than the underlying facility load" for N+1 redundancy; not a final design | 1.5 GW plan | about 1.3 (stated, not designed) | | Data Center Knowledge. press |
| **Joule** (Utah) | Caterpillar G3520K fleet, 4 GW described, 1.1 GWh battery | Not disclosed | n/a | Launch targeted 2026 | company release via trade press |

### "More machine than load": what the evidence now says

- One primary ratio: Socrates 1.39 (Williams 10-K vs 10-Qs). Williams still gives no reason.
- One stated rule of thumb, not primary: Prometheus, about 30% extra for N+1 on engines (press).
- One gross-vs-net gap, not primary: VoltaGrid/Oracle about 2.58 GW gross vs 2.3 GW (press).
- Buffers: every large islanded or semi-islanded design found pairs engines or turbines with batteries (xAI Megapacks, Joule 1.1 GWh, GW Ranch 1.8 GW, ProPetro hybrid). The battery is the cheap answer to load swings; spare engines answer outages and maintenance.
- Why swings matter: PJM's own count (6 Oct 2026) of data-centre loads that transferred to backup generation after normally cleared 230 kV faults: about 1,500 MW (10 Jul 2024), about 1,800 MW (17 Feb 2025) and about 3,900 MW (22 Jul 2026, "the largest CILR event to date", about 2,900 MW at once then about 1,000 MW a minute later; Eastern Interconnection frequency 60.092 Hz). An island campus has no grid to absorb that; its own machines and batteries must. PRIMARY: https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2026/20261006/20261006-item-07-a---1-lcl-ride-through-requirements-background---presentation.pdf
- Wording point: PJM says the load "transferred to backup generation". The data centres did not vanish; their own on-site backup picked them up. That cuts both ways for the piece: own machines already carry the load when the grid wobbles.
- Verdict: hypothesis still alive, now with one primary ratio and two corroborating statements. Not yet a finding.

---

## 3. Rules

### 3a. Air permits

| Rule / action | Fact | Date | Source | Label |
|---|---|---|---|---|
| Federal major source thresholds | Title V: 100 tons a year of any regulated pollutant (lower in serious and worse ozone nonattainment areas; NOx 50 tpy in the Ozone Transport Region, which includes Pennsylvania). PSD (federal pre-construction review): 250 tpy, or 100 tpy for 28 listed source categories, which include fossil-fuel steam electric plants above 250 MMBtu/h heat input (so a combined cycle with a steam turbine falls in the 100 tpy class; a simple-cycle turbine plant does not) | Standing law, 40 CFR 52.21(b)(1), 40 CFR 70.2 | eCFR | PRIMARY (from statute; cite eCFR text before publishing) |
| Homer City netting | in piece (PA DEP 32-00457A) | 18 Nov 2025 | | PRIMARY |
| EPA turbine NSPS | Final NSPS amendments for stationary combustion turbines, 91 Fed. Reg. 1910; new subcategory for small and medium turbines in "temporary" use; conditional exclusion from "stationary" only if a turbine meets the nonroad engine definition and is certified to Title II standards, which EPA has not yet adopted, so the nonroad route is not yet open | 15 Jan 2026 | Federal Register; EPA "Clean Air Act Resources for Data Centers" page https://www.epa.gov/node/297395 | PRIMARY (rule); interpretation from law-firm summaries |
| EPA islanded generators | "EPA Issues Clarification on Islanded Power Generators and Acid Rain Program Provisions"; summaries say the Acid Rain Program generally does not apply to off-grid generators serving private facilities | 16 Jul 2026 | EPA data centre page | PRIMARY (title); content press |
| EPA, emergency hours | Engine running under DOE section 202(c) emergency orders in spring and summer 2026 counts as emergency operation, outside the 50-hour non-emergency limit | 2026 | EPA data centre page | PRIMARY |
| EPA "begin actual construction" | Proposed redefinition | 11 May 2026 | EPA data centre page | PRIMARY (proposal) |
| Further easing | Administration considering a classification for temporary gas turbines | Sep 2026 | Axios, 10 Sep 2026 | press |
| Memphis | Shelby County permit for 15 turbines, 247 MW, to 2 Jan 2027 (see table 2) | 2 Jul 2025 | | press |
| Mississippi | MDEQ 41 turbines; federal court 30 Oct 2026: not a mobile source, permits needed regardless of "temporary" label (see table 2) | 10 Mar / 30 Oct 2026 | | press/party |
| **Texas pause** | Governor Abbott's letter to TCEQ: issue no permits for data centre projects until ERCOT and the Texas Water Development Board finish audits of water and power use (expected around December, press). TCEQ's reply: it "has paused the issuance of all permits related to the construction or development of infrastructure directly supporting data centers", is screening pending applications, and "where possible, is suspending" claimed authorisations that need no affirmative permit (permits by rule and similar) | Letter 21 Sep 2026; TCEQ reply 19 Oct 2026 | https://www.tceq.texas.gov/downloads/response/tceq-response-gov-abbott-dc-directive.pdf | PRIMARY (TCEQ letter); Abbott letter press |
| Texas pre-pause | Floodlight found at least 38 Texas data centres with minor permits for on-site power (no public notice) | 9 Jul 2026 | Floodlight / Texas Tribune | press |
| Texas, after pause | Public Citizen and FracTracker say some data-centre permits kept moving (stormwater; three major-source air permit notices the day after); TCEQ says those were suspended and "No permits have been approved" (governor's office) | 20 Oct 2026 | Texas Tribune | press |

### 3b. Texas SB 6 (2025) and PUCT rules

| Item | Fact | Source | Label |
|---|---|---|---|
| Threshold | Large load demand threshold 75 MW unless the commission sets lower (PURA 37.0561(c)) | SB 6 enrolled text, https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm | PRIMARY |
| Disclosure | Large loads must disclose "on-site backup generating facilities" to their utility | same | PRIMARY |
| Backup can be called | In an emergency, after market services, ERCOT may direct the utility to require a large load to deploy backup generation or curtail; this applies to backup that "can serve at least 50 percent of on-site demand" (fetch summary; check exact section wording) | same | PRIMARY, wording to re-check |
| Curtailment kit | Loads interconnected after 31 Dec 2025 must install curtailment equipment before connection (PURA 39.170) | same | PRIMARY |
| Net metering with existing plants | PURA 39.169: notice to ERCOT; PUCT may approve, deny or condition; deemed approved if no action in time. Rule 16 TAC 25.205 (Project 58479) adopted (Texas Register, 10 Apr 2026 issue; adoption 26 Mar 2026 per law firm): covers only generators registered stand-alone as of 1 Sep 2025, loads of 75 MW or more; ERCOT study 120 days, PUCT 60 days; capacity made available "first and foremost through the full curtailment" of the co-located load | Texas Register https://www.sos.texas.gov/texreg/archive/April102026/Adopted%20Rules/16.ECONOMIC%20REGULATION.html | PRIMARY |
| First case | PUCT Docket 59220, order 24 Jul 2026: approved net metering of a 260 MW data centre (Armstrong County; Crusoe load assets moved to Ensign Infrastructure in Mar 2026) with a stand-alone generator; emergency curtailment of the data centre not capped at the paired generator's size | White & Case summary | press (law firm) |
| Interconnection standards | Draft 16 TAC 25.194 (Project 58481) published 12 Mar 2026 for loads of 75 MW or more; adoption not confirmed. PUCT approved ERCOT "batch" study protocol revisions for 75 MW+ loads on 18 Jun 2026 | law-firm summaries | press |

Point for the piece: a new-build gas plant beside a data centre (Socrates-style, or a new Texas campus) is outside 25.205, which covers only existing plants. A Texas campus that keeps a grid tie must also accept that ERCOT can order its backup on or its load off.

### 3c. FERC and PJM: behind-the-meter netting

| Item | Fact | Source | Label |
|---|---|---|---|
| December order | 18 Dec 2025, PJM Interconnection, 193 FERC 61,217 (EL25-49): tariff unjust and unreasonable for lack of co-location rules; three transmission services for co-located load (network service including an interim service, Firm Contract Demand with an "anti-toggling" rule, Non-Firm Contract Demand); PJM's retail behind-the-meter generation netting rules "no longer just and reasonable" for large loads because netting shifts costs; grandfathering of existing arrangements; transition reported as three years | Willkie memo 2 Jul 2026; Mayer Brown, Mintz | press (law firm) of FERC order |
| Compliance | 16 Apr 2026: FERC partly accepted, partly rejected PJM's compliance filing | Willkie | press |
| Rehearing | 18 Jun 2026, 195 FERC 61,209 (EL25-49-002): reaffirmed; BTMG netting still unjust; further tariff changes. Same day six show cause orders to MISO, CAISO, ISO-NE, NYISO, PJM, SPP on large-load connection, incl. PJM EL26-67 (ride-through, ramp limits) | https://www.ferc.gov/sites/default/files/2026-06/EL25-49-002_0.pdf ; PJM deck 6 Oct 2026 | PRIMARY (order exists, PJM deck); detail press |
| PJM next step | PJM plans to file revisions for EL26-67 "target: November 2026" | PJM deck 6 Oct 2026 | PRIMARY |

### 3d. NERC and data-centre load swings

| Item | Fact | Date | Source | Label |
|---|---|---|---|---|
| Events | 1,500 MW (10 Jul 2024), 1,800 MW (17 Feb 2025), 3,900 MW (22 Jul 2026), all "transferred to backup generation" after properly cleared 230 kV faults | PJM deck 6 Oct 2026 | PJM link above | PRIMARY |
| NERC Level 3 alert | "Essential Actions to Industry: Computational Load Modeling, Studies, Instrumentation, Commissioning, Operations, Protection and Control"; issued 4 May 2026 (press); responses due 3 Aug 2026 (press); seven essential actions | May 2026 | PJM deck names it; NYSRC copy https://www.nysrc.org/wp-content/uploads/2026/06/NYSRC-LLWG-5-Att.-5-NERC-Level-3-Alert-1.pdf | PRIMARY (existence); dates press |
| Registration | Proposed "Computational Load Entity" registration for loads of 20 MW or more, posted 1 Apr 2026 | 2026 | press | press |
| Standards | Project 2026-02 Computational Loads; draft CLO-001-1, CLO-002-1, CLO-003-1; FERC RD26-7-000 directs NERC to file by 31 Dec 2026; NERC white paper "Large Load Disturbance Performance" expected Dec 2026 | Oct 2026 | PJM deck | PRIMARY |
| Draft requirement | Post-fault active power recovery of at least 90% of pre-disturbance consumption; ERCOT's voltage ride-through as minimum baseline | Oct 2026 | PJM deck (draft LLWG recommendations) | PRIMARY (draft) |

---

## 4. Cost per MWh: on-site gas vs grid (all estimates)

| Item | Figure | Date | Source | Label |
|---|---|---|---|---|
| Lazard LCOE+ 2026 (v19), unsubsidised, gas combined cycle | $51 to $129/MWh | Jul 2026 | Utility Dive, 16 Jul 2026, on Lazard's report | press of Lazard (Lazard PDF not opened) |
| Lazard 2026, gas peaking | $144 to $276/MWh; capital costs and LCOE rose | Jul 2026 | same | press of Lazard |
| Lazard 2025 (for comparison) | CCGT $48 to $109; peaking $149 to $251 | Jun 2025 | pv magazine; https://www.lazard.com/media/uounhon4/lazards-lcoeplus-june-2025.pdf | press / PRIMARY PDF not opened |
| Turbine price | Wood Mackenzie: $600/kW by end 2027, up 195% since 2019 | Jul 2026 | Utility Dive | press |
| Engine route capex | ProPetro: about $1.4m to $1.5m per MW including balance of plant | 28 Oct 2026 | ProPetro 8-K | PRIMARY |
| Grid price, US industrial average | 9.64 c/kWh ($96.4/MWh) Aug 2026 vs 8.98 Aug 2025 | EIA EPM Table 5.6.A, released 23 Oct 2026 | https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a | PRIMARY (preliminary) |
| Grid, by state, Aug 2026 | Texas 7.21, Ohio 9.75, Virginia 9.98, Louisiana 6.10, Pennsylvania 10.47, Tennessee 6.92 c/kWh | same | same | PRIMARY |
| Gas price | Henry Hub forecast $3.48/MMBtu (2026), $3.16 (2027) | STEO, 6 Oct 2026 | https://www.eia.gov/outlooks/steo/report/natgas.php | PRIMARY |

Fuel cost alone (calc; maker LHV efficiency converted to HHV at 1.108, Henry Hub with no delivery basis):
- Wärtsilä 50SG at 50.0% LHV: heat rate about 7.57 MMBtu/MWh HHV; at $3.48, about $26/MWh; at $3.16, about $24/MWh.
- LM6000 PF+ at 41.3% LHV: about 9.15 MMBtu/MWh; about $32/MWh at $3.48.
- LM2500XPRESS at 38.4% LHV: about 9.85 MMBtu/MWh; about $34/MWh at $3.48.
- Capital on top (calc, rough): $1.45m/MW engines, recovered over 10 years at 8% (capital recovery factor 0.149) is about $216k/MW-year; at 90% load factor (7,884 MWh), about $27/MWh; with 1.39 MW built per MW used (Socrates ratio), about $38/MWh. Add operations and maintenance (not sourced here). So an engine island lands roughly $60 to $80/MWh before O&M margin and gas delivery basis, against $72 (Texas) to $105 (Pennsylvania) grid industrial prices. Treat as illustrative arithmetic, not a finding.
- Bloom: no primary cost-per-kWh statement found; its Q3 release gives none. Its claim on record is speed, not price (in piece).

Reading: on-site gas is not obviously dearer than grid power for a high-load-factor campus; the overbuild and the gas pipe are what move it. That supports the piece's frame that buyers pay for time, not price.

---

## What the live piece has wrong or out of date

1. **Load swings understated and slightly mis-worded.** Piece cites only 1,800 MW (Feb 2025) "dropping off". PJM (6 Oct 2026) now lists a 3,900 MW event on 22 Jul 2026, the largest, and describes all three as load "transferred to backup generation". Add the July 2026 event, the NERC Level 3 alert (May 2026) and FERC's 31 Dec 2026 deadline for NERC standards (RD26-7).
2. **Texas permit pause missing.** Since 21 Sep 2026 (Abbott) and 19 Oct 2026 (TCEQ letter), Texas has paused data-centre permits, including where possible permits by rule. This is now the sharpest "permit" fact for on-site gas (Abilene, Fermi, GW Ranch, Frontier) and belongs in step four of the chain.
3. **Federal permit position changed.** EPA's 15 Jan 2026 turbine rule and the 30 Oct 2026 court ruling (xAI Southaven not a "mobile source") are absent; the piece has no xAI case at all, the best-known on-site gas campus.
4. **"The fastest dated route, Socrates, is 400 MW"** is now thin: Williams has four more projects, 2,032 MW, due 2H 2027 to 2H 2028, all "assume timely receipt of permits" (Q3 10-Q). Also Socrates North's in-service date is "later in the fourth quarter" in the 10-Q, "mid-November" in the release; neither confirmed as of 7 Nov.
5. **Engines' order book understated.** Piece cites one 282 MW order; Wärtsilä says that was its seventh US data-centre order, over 3 GW sold, up from over 1.6 GW in April (412 MW Ohio, operation early 2028).
6. **Rental fleets absent.** Solaris (3.2 GW contracted, 900 MW new deal, "ahead of long OEM queues") and ProPetro (cost per MW, 2028 deployment) show a fourth fast lane: renting time. Supports "the product is time".
7. **Behind-the-meter rules missing.** FERC's December 2025 PJM order (BTMG netting no longer just and reasonable for large loads) and Texas SB 6/25.205 (only existing plants; backup can be called by ERCOT) change what "behind the meter" buys. The four-terms box defines behind the meter without these.
8. **"Islanded" hypothesis evidence.** Still one primary ratio; add Prometheus' 30% N+1 statement (press) and the battery pairing pattern. Keep as hypothesis.
9. **Crusoe's 29 units** are not disclosed for any one site; avoid implying they are for Abilene. Piece is fine as written ("the buyers are the campuses themselves").
10. **Cost absent.** The piece never says what own power costs. Section 4 gives a labelled estimate; Lazard 2026 peaking at $144 to $276/MWh vs CCGT $51 to $129 and grid industrial 9.64 c/kWh (Aug 2026).
11. **Bloom/Oracle date**: the 2.8 GW expansion is dated about 14 Apr 2026 (release); piece gives no date. Bloom's Q3 release does not mention Oracle.
12. Homer City: no newer primary date; EIA's July 2028 flag stands (already in evidence box).

Not verified and should not be used without a check: SGT-A35 specs; Shelby County permit text; MDEQ permit text; Abilene turbine count from TCEQ; Hyperion MW total for the second agreement beyond Entergy's 5,278 MW; exact SB 6 section numbering for the 50% backup clause; Lazard PDF figures (seen only via Utility Dive).
