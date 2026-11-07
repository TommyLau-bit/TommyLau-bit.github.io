# Nuclear for AI: uprates, new builds on ordinary fuel, deal structures

Research slice for the depth rebuild of `nuclear-for-ai`. Compiled 7 November 2026.
Every row: figure, date, source title, URL. "press" = trade or news report only, no primary found.
"calc" = my arithmetic from the cited figures.

Access notes: nrc.gov blocks scripted fetches on some paths (403). The NRC figures below were read
through the pages that did load; where only a mirror or trade report was reachable it is marked.

---

## 1. Uprates

### 1a. What an uprate physically is

An uprate is an NRC licence amendment that raises the maximum thermal power (MWt) a reactor may run at.
More heat from the core makes more steam, and more steam through the turbine makes more electricity.
The core runs hotter in total (more fresh fuel assemblies or a reworked loading pattern), and the
"balance of plant" (everything downstream of the reactor: turbine, generator, transformers, pumps) must
carry the extra steam and current. How much has to change depends on the size of the step.

| Type | Typical gain | What changes physically | Source |
|---|---|---|---|
| Measurement uncertainty recapture (MUR) | Less than 2% | Better feedwater flow meters, so the plant knows its power more exactly and can run closer to its licensed limit. No major hardware. | NRC, "Types of Power Uprates", reviewed 15 Sep 2026, https://www.nrc.gov/licensing-applications/operating-reactor-licensing/power-uprates/types-power-uprates |
| Stretch | Typically up to 7%, within the plant's design capacity; plant-specific | Usually instrument setpoint changes; no major plant modifications | same |
| Extended (EPU) | Above stretch; approved as high as 20% | "Significant modifications to major balance-of-plant equipment": high-pressure turbines, condensate pumps and motors, main generators, and/or transformers | same |

Note for the piece: the live text says an uprate means "bigger turbines fitted while it is shut to refuel".
That is true only of extended uprates. Seven of Constellation's twelve listed filings are MURs, which are
meter upgrades. See section 6.

### 1b. History and the NRC lists

| Fact | Figure | Date | Source |
|---|---|---|---|
| Uprates approved since 1977 | 172 | page reviewed 15 Sep 2026 | NRC, "Approved Applications for Power Uprates", https://www.nrc.gov/reactors/operating/licensing/power-uprates/status-power-apps/approved-applications.html |
| Total added by those approvals | 24,089 MWt (8,030 MWe) | same | same |
| Most recent approval on the list | Millstone 3, MUR, 1.6%, 59 MWt, approved 9 Nov 2021. The last ten approvals (2017 to 2021) were all MURs of 1.4 to 1.7% | same | same |
| Uprate applications under NRC review | None | page updated 15 Sep 2026 | NRC, "Pending Applications for Power Uprates", https://www.nrc.gov/licensing-applications/operating-reactor-licensing/power-uprates/status-power-uprate-applications/pending-applications-power-uprates (read via search result; fetch blocked) |
| Uprate capacity added over the past 20 years | About 6 GW; about 2 GW more may come from future requests | page reviewed 29 Oct 2026 | NRC, "Power Uprates", https://www.nrc.gov/facilities-safety/operating-reactors/operating-reactor-licensing/power-uprates |
| NRC review targets | 12 months EPU, 9 months stretch, 6 months MUR | 2025 to 2026 | NRC "Power Uprate Review Readiness" page (via search result), https://www.nrc.gov/facilities-safety/operating-reactors/operating-reactor-licensing/power-uprates/power-uprate-review-readiness |

**Expected-applications list (NRC, last updated 8 Sep 2026)**
https://www.nrc.gov/facilities-safety/operating-reactors/operating-reactor-licensing/power-uprates/status-of-power-uprate-applications/expected-applications-for-power-uprates

| Measure | Figure |
|---|---|
| Expected applications, all owners | 31 in the yearly summary (10 MUR, 2 stretch, 19 EPU); the itemised table lists 30 (one EPU short). The page does not reconcile the two |
| Total expected | 7,336 MWt, about 2,421 MWe |
| Window | Q4 2026 to Q3 2032 |
| Constellation entries | 12, plants marked "Proprietary": 5 EPU (Q4 2026, two in Q4 2027, Q4 2028, Q4 2030) and 7 MUR (two Q1 2027, two Q2 2027, Q4 2027, Q2 2030, Q3 2030) |
| Other owners | Duke (Brunswick 1-2 MUR; McGuire 1-2, Catawba 1 EPU), PSEG (Salem 1-2 stretch), Southern (Hatch 1-2 EPU Q2 2027; Vogtle 1-2 EPU Q4 2028), Wolf Creek MUR, Energy Northwest (Columbia EPU Q2 2028), Vistra (Perry 1 Q3 2029, Beaver Valley 2 Q3 2030, Beaver Valley 1 Q3 2031, Davis-Besse Q3 2032, all EPU), one proprietary EPU |

What it shows: the pipeline has turned from small meter upgrades (every approval 2017-2021) to extended
uprates (19 of 31), the type that needs turbines, generators and transformers. 2,421 MWe expected is
less than a third of the 8,030 MWe approved in 44 years, but it is arriving in about six. No application
is currently under review, so none of the AI-funded uprates has yet reached the NRC.

### 1c. The AI-funded uprate deals

| Deal | MW of uprate | Units / sites | Money | Timing | Structure | Source |
|---|---|---|---|---|---|---|
| Google–Constellation, 6 Oct 2026 | 890 MW new capacity | 11 Constellation-owned units at six sites in Illinois, Pennsylvania, New Jersey; units not named | More than US$4.3bn of Constellation investment; work covers "turbines, steam generators, and digital control systems" | First uprate "expected to be delivered by 2028" (Constellation); 890 MW "before the end of 2032" (Google) | 20-year PPA; power added to the PJM grid (front of meter). Separate 15-year energy supply agreement for 2,700 MW from Constellation's existing PJM fleet, a financial deal "without taking resources off of the grid". Constellation calls it "a direct response to PJM's 'Bring Your Own Power' proposal" | Constellation release, 6 Oct 2026, https://www.constellationenergy.com/news/2026/10/google-and-constellation-announce-landmark-agreement-to-bring-890-mw-of-new-nuclear-capacity-to-pjm-grid.html ; Google blog, 6 Oct 2026, https://blog.google/company-news/why-were-backing-americas-existing-nuclear-plants/ |
| (sites named) | Braidwood, Byron, LaSalle, Quad Cities (IL), Limerick (PA), Salem (NJ; Constellation owns 43%, PSEG operates) | | | | | press: ANS Nuclear Newswire, 6 Oct 2026, quoting a Constellation spokesman, https://www.ans.org/news/2026-10-06/article-8467/ |
| Amazon–Constellation, Calvert Cliffs (MD), 30 Sep 2026 | About 190 MW | Calvert Cliffs, 1,790 MW plant | More than US$3bn in Maryland, "including improvements across the entire plant"; supports relicensing for another 20 years | Uprate online 2030 to 2032 | 20-year PPA for 690 MW including the 190 MW; "all electricity generated by Calvert Cliffs will continue flowing to the PJM regional grid" (front of meter); separate retail supply agreement for Amazon in PJM | Constellation release, 30 Sep 2026, https://www.constellationenergy.com/news/2026/09/constellation-and-amazon-announce-20-year-power-purchase-agreement-at-calvert-cliffs.html |
| Meta–Constellation, Clinton (IL), 3 Jun 2025 | 30 MW | Clinton, 1,121 MW | Not disclosed | PPA starts June 2027; uprates "fully complete in 2029" (10-K) | 20-year PPA for 1,121 MW; replaces Illinois zero-emission credits from mid-2027; supports relicensing; front of meter | Constellation release, 3 Jun 2025, https://www.constellationenergy.com/news/2025/constellation-meta-sign-20-year-deal-for-clean-reliable-nuclear-energy-in-illinois.html ; Constellation 10-K FY2025, https://www.sec.gov/Archives/edgar/data/1868275/000186827526000032/ceg-20251231.htm |
| Meta–Vistra, Jan 2026 | 433 MW: Perry 213, Davis-Besse 80, Beaver Valley 140 | Ohio, Pennsylvania | Uprate capex 2026 to 2034, under 20% by end 2028 | Part of uprate output by 2031, all by end 2034 | 20-year PPAs for 2,609 MW: 1,268 MW Perry + 908 MW Davis-Besse operating, plus the 433 MW of uprates; operating deliveries from late 2026, full by end 2027 | Vistra 8-K, Jan 2026, https://www.sec.gov/Archives/edgar/data/1692819/000119312526008508/d20785d8k.htm ; Vistra 10-Q Q1 2026, https://www.sec.gov/Archives/edgar/data/0001692819/000169281926000014/vistra-20260331.htm |
| Google–Georgia Power, filed 21 Sep 2026 | About 96 MW (Georgia Power's share) | EPUs at Vogtle 1-2 and Hatch 1-2 | Subscription agreement redacted; Georgia Power claims about US$900m customer benefit | NRC filings: Hatch Q2 2027, Vogtle 1-2 Q4 2028 | New "NU-1" tariff; Google receives the zero-emission credits. Needs Georgia PSC approval | press: ANS, 23 Sep 2026, https://www.ans.org/news/2026-09-23/article-8424/google-georgia-power-announce-partnership-to-uprate-plants/ ; WNN, https://world-nuclear-news.org/articles/google-agreement-to-support-Georgia-plant-uprates |
| DOE loan to Constellation, 27 Oct 2026 | No MW given; covers Braidwood, Byron, Clinton, Dresden, LaSalle, Quad Cities, Calvert Cliffs, Limerick | | Conditional commitment up to US$5bn, DOE Office of Energy Dominance Financing; "not ... a final decision to proceed with any individual uprate" | none stated | Release says the Google and Amazon agreements drive "more than $7 billion" of investment for about 1,080 MW | Constellation release, 27 Oct 2026, https://www.constellationenergy.com/news/2026/10/constellation-secures-conditional-doe-loan-commitment-of-up-to-5-billion-to-expand-nuclear-output.html |

Sum of uprate MW contracted to hyperscalers (calc): 890 + 190 + 30 + 433 + 96 = **1,639 MW**.

### 1d. Constellation's earlier uprates

| Project | Figure | Date | Source |
|---|---|---|---|
| Byron and Braidwood (IL) | US$800m, new high-efficiency main turbines; announced as about 135 MW, now cited as 158 MW; 45Y credit "helps make these investments economic" | Announced 21 Feb 2023; low-pressure turbines on Byron 1 fitted in spring 2026 outage; high-pressure turbines 2027 and 2028 | Constellation release, 21 Feb 2023, https://www.constellationenergy.com/news/2023/Constellation-Making-Major-Investment-in-Two-Illinois-Nuclear-Plants-to-Increase-Clean-Energy-Output.html ; Constellation 2025 federal factsheet (158 MW), https://www.constellationenergy.com/content/dam/constellationenergy/pdfs/2025_Constellation_Factsheet_FederalR.pdf ; press: WIFR, 17 Apr 2026, https://www.wifr.com/2026/04/17/byron-nuclear-plant-completes-first-phase-multi-million-dollar-upgrade-project/ |
| Limerick (PA) digital upgrade | US$167m; NRC amended the licences to replace analogue safety instrumentation and control with one digital plant protection system, the first such major retrofit at an operating US plant. Not an uprate itself, but the "digital control systems" Google's deal funds | NRC release 26-002, 5 Jan 2026 | NRC, https://www.nrc.gov/sites/default/files/cdn/doc-collection-news/2026/26-002.pdf ; Constellation, Jan 2026, https://www.constellationenergy.com/news/2026/01/nrc-greenlights-constellations-167-million-digital-modernization-plan-for-limerick-clean-energy-center.html |
| Calvert Cliffs | About 190 MW (Amazon deal above) | 30 Sep 2026 | above |
| Clinton and Dresden licences renewed; US$370m of upgrades | | Dec 2025 | Constellation, https://www.constellationenergy.com/news/2025/12/nrc-renews-operating-licenses-for-clinton-and-dresden.html |

### 1e. Cost per kW: uprate, restart, new build (all calc; investment figures are not always uprate-only)

| Project | Spend | MW | US$ or C$ per kW | Caveat |
|---|---|---|---|---|
| Google uprates | >US$4.3bn | 890 | about US$4,800/kW | Includes steam generator and digital work on 11 units |
| Byron/Braidwood | US$800m | 158 | about US$5,100/kW | Turbines only |
| Constellation Google + Amazon | >US$7bn | ~1,080 | about US$6,500/kW | Calvert Cliffs figure includes plant-wide work and relicensing |
| Crane restart (for reference) | US$1.6bn (press) | 835 | about US$1,900/kW | Restart, not uprate; DOE loan US$1bn closed 18 Nov 2025 |
| Vogtle 3 and 4 | About US$31bn owners' cost, about US$35bn with Westinghouse's US$3.7bn settlement (press, AP) | 2,234 (2 x 1,117) | about US$14,000 to 15,700/kW | Final, after overruns |
| Darlington BWRX-300, four units | C$20.9bn (incl. interest, escalation, contingency) | 1,200 | about C$17,400/kW | Unit 1 alone C$6.1bn + C$1.6bn common = C$7.7bn for 300 MW, about C$25,700/kW |

Read: an uprate costs roughly a third of a new large reactor per kW, and it lands on a licensed site with a grid connection.

---

## 2. New builds on ordinary fuel

Ordinary fuel = low-enriched uranium (LEU) up to 5% U-235. HALEU = 5% to just under 20%.

| Design | Fuel | Where used |
|---|---|---|
| Westinghouse AP1000 (1,117 MW) | LEU, under 5% | Vogtle 3-4; Fermi America plan; V.C. Summer completion study; US-government partnership |
| GE Vernova Hitachi BWRX-300 (300 MW) | LEU, standard GNF boiling-water fuel; enriched in the US or Europe | Darlington (Canada), Clinch River (TVA) |
| TerraPower Natrium (345 MW, 500 MW with storage) | HALEU | Kemmerer; Meta deal |
| Oklo Aurora (75 MW at INL) | HALEU, metal | INL; Meta Ohio campus |
| Kairos KP-FHR / Hermes | HALEU in TRISO pebbles | Hermes 1 and 2, Google |
| X-energy Xe-100 (80 MW) | HALEU in TRISO pebbles | Dow (Texas), Energy Northwest for Amazon |

Sources: DOE, "What is HALEU", https://www.energy.gov/ne/articles/what-high-assay-low-enriched-uranium-haleu ; OPG/GVH fuel route from ANS Nuclear News, 5 Jun 2026 (press), https://www.ans.org/news/article-8047/north-american-construction-is-back-smaller-and-faster-at-opgs-darlington/ ; designs per company materials cited elsewhere in the live piece.

### 2a. OPG Darlington New Nuclear Project (Canada)

| Fact | Figure / date | Source |
|---|---|---|
| Scope | Four BWRX-300, 1,200 MW total | Ontario approval, 8 May 2025 (press: WNN, https://world-nuclear-news.org/articles/what-is-the-budget-for-canadas-first-smr-project) |
| Total cost | C$20.9bn, 2024 dollars incl. interest and contingency | same; OPG Q1 2025 results |
| Unit 1 | C$6.1bn, plus C$1.6bn common systems = C$7.7bn released | OPG Q1 2025 results, https://www.newswire.ca/news-releases/opg-reports-2025-first-quarter-financial-results-824344588.html (fetch blocked; via search result); ANS, 5 Jun 2026 |
| Later units | Falling to about C$4.1bn for unit 4 | press: WNN, above |
| Licence to construct | 4 April 2025, valid to 31 March 2035, three regulatory hold points | CNSC project page (last modified 25 Aug 2026), https://www.cnsc-ccsn.gc.ca/eng/reactors/new-reactor-power-plant-projects/new-reactor-power-plant-facilities/darlington-new-nuclear-project/ |
| Hold point 1 (reactor building foundation) removed | 30 March 2026 | same |
| Basemat set in 35 m reactor shaft | 22 April 2026 | OPG story (fetch blocked; via search), https://www.opg.com/news-and-media/story/laying-the-foundation-for-the-g7s-first-small-modular-reactor ; ANS, 5 Jun 2026 |
| Licence to operate applied for | 25 March 2026, 20-year licence for one unit | CNSC page above |
| Operating licence hearing | Not yet scheduled (as of 25 Aug 2026) | CNSC page above |
| First unit timing | Construction complete by end of the decade; grid connection by end of 2030 (OPG, June 2026). Ontario said commercial service by end of 2030 (May 2025, press) | press: ANS, 5 Jun 2026; OPG story above |
| Units 2-4 | Approval milestone 2028; complete mid-2030s | press: ANS, 5 Jun 2026 |

### 2b. TVA Clinch River (Tennessee)

| Fact | Figure / date | Source |
|---|---|---|
| Design | One BWRX-300, 300 MW, on the existing Early Site Permit site at Oak Ridge | GE Vernova release, 29 Sep 2026, https://www.gevernova.com/news/press-releases/nrc-issues-first-us-construction-permit-bwrx-300-small-modular-reactor-tva-clinch-river |
| Application | April 2025 (GE Vernova); docketed July 2025 | same; ANS, 15 Jul 2025 |
| Construction permit | Issued; announced 29 Sep 2026; first US BWRX-300 permit | same |
| What it allows | Construction only; separate operating licence needed before fuel load | same; press: WSMV, 29 Sep 2026 |
| Commercial operation target | 2033; no construction start date; cost sharing still under negotiation | press: WSMV, 29 Sep 2026, https://www.wsmv.com/2026/09/29/tennessee-utility-receives-federal-permit-build-first-advanced-small-nuclear-reactor-us-heres-what-know/ |
| Context | The NRC's second major reactor approval of 2026 after the Natrium (Kemmerer) construction permit in March | press: same |

### 2c. Large reactors: Westinghouse AP1000

| Fact | Figure / date | Source |
|---|---|---|
| US government partnership | At least US$80bn of new Westinghouse reactors; government arranges financing and helps permitting; gets 20% of Westinghouse cash distributions above US$17.5bn after final investment decision; may require an IPO with warrants for 20% | Cameco/Brookfield release, 28 Oct 2025, https://www.businesswire.com/news/home/20251027603867/en |
| Sites | None named. Cameco said deployment would begin with two AP1000s on federal sites (press) | press: WNN, https://world-nuclear-news.org/articles/brookfield-cameco-team-with-us-government-for-ap1000-deployment |
| Status at 30 Oct 2026 | No definitive agreements reported. New: a Sept 2026 US Commerce–Republic of Korea non-binding framework for up to US$120bn of Korean investment, financing up to eight large US reactors including six AP1000s, "subject to definitive agreements"; no US sites; no new US AP1000 order | Cameco Q3 2026 release, 30 Oct 2026, https://www.sec.gov/Archives/edgar/data/0001009001/000119312526439858/d106072dex991.htm |
| V.C. Summer 2-3 (SC) | Santee Cooper picked Brookfield (Oct 2025) to finish the two half-built AP1000s ("Fairfield Nuclear Project"); MOU Dec 2025; feasibility and FID target pending; Santee Cooper targets 25% | press: ANS, https://www.ans.org/news/article-7493/santee-cooper-opts-to-reboot-summer-reactor-project/ |
| Fermi America (Amarillo, TX), "Project Matador" | COL application for four AP1000s filed June 2025, accepted Sept 2025 (first new COLA accepted in 15 years); NRC environmental scoping notice 20 Mar 2026; plans first AP1000 2032, then 2034, 2035, 2036; about 6 GW nuclear planned; no binding tenant (Q1 2026); CEO and CFO left April 2026 | Fermi 10-Q Q1 2026, https://www.sec.gov/Archives/edgar/data/0002071778/000207177826000032/frmi-20260331.htm ; Fermi FY2025 letter (8-K), https://www.sec.gov/Archives/edgar/data/2071778/000207177826000007/frmiex991fy2025shletter.htm ; press: ANS, 10 Sep 2025 |

### 2d. Vogtle 3 and 4, the last US build

| Fact | Figure / date | Source |
|---|---|---|
| Size | Two AP1000s, 1,114 MW nameplate each (Unit 4) | EIA FAQ, March 2026, https://www.eia.gov/tools/faqs/faq.php?id=207&t=3 |
| Commercial operation | Unit 3: 31 July 2023; Unit 4: 29 April 2024 | Georgia Power filing to Georgia PSC, https://services.psc.ga.gov/api/v1/External/Public/Get/Document/DownloadFile/219797/100951 ; EIA FAQ id=228 |
| Original plan | About US$14bn, operation 2016 and 2017 | press, multiple |
| Final cost | About US$31bn to the four owners, about US$35bn with Westinghouse's US$3.7bn payment | press: AP |
| Georgia Power's share | About US$13.7bn capital and financing, subject to PSC verification | Georgia Power PSC filing above |
| Duration | NRC combined licences Feb 2012 to Unit 4 operation April 2024: about 12 years; seven years late | calc from above |

---

## 3. How the AI deals are structured

**Front of the meter**: the plant sells into the grid; the buyer's data centre draws from the grid like any
customer and pays grid charges. The PPA is a financial contract. **Behind the meter / co-located**: the
data centre sits at the plant and takes power before it reaches the grid, avoiding some transmission
charges. That is what FERC and the grid owners objected to.

### 3a. Talen–Amazon, Susquehanna

| Step | Figure / date | Source |
|---|---|---|
| Original co-location | March 2024 PPA: up to 960 MW to the AWS campus next to Susquehanna | Talen 10-Q Q2 2026 definitions, https://www.sec.gov/Archives/edgar/data/0001622536/000162253626000066/tln-20260630.htm |
| FERC rejects amended ISA | 1 Nov 2024, Docket ER24-2172, 2-1 vote. Would have raised co-located load from 300 MW to 480 MW; existing 300 MW left in place | press: WNN, https://world-nuclear-news.org/articles/regulator-rejects-amended-susquehanna-power-agreement ; Utility Dive |
| Restructured | 11 June 2025: up to 1,920 MW through 2042, ramping to full volume no later than 2032, front of the meter; Talen is retail supplier, PPL Electric does transmission and delivery; also explore SMRs and uprates | Talen release, 11 Jun 2025, https://www.sec.gov/Archives/edgar/data/1622536/000162828025030559/a20250611pressreleasebusin.htm |
| Talen's revenue figure | About US$18bn over life at full volume | press: Utility Dive, citing Talen investor presentation |
| Transition done | "The transition to the revised AWS PPA occurred in April 2026" | Talen 10-Q Q2 2026, above |

### 3b. FERC's PJM co-location order

| Step | Content | Date | Source |
|---|---|---|---|
| Show cause | FERC asks PJM why its tariff lacks co-location rules | 20 Feb 2025 | 190 FERC ¶ 61,115 |
| December Order | PJM tariff found unjust and unreasonable for lacking clear co-location terms. Eligible customer serving co-located load must take one of three services: (1) network service (NITS), with a new interim non-firm NITS until upgrades are built; (2) new Firm Contract Demand; (3) new Non-Firm Contract Demand (pay on net withdrawals, capped, curtailable above contract). Existing generators adding co-located load must be studied, pay for upgrades, and cannot serve the load until upgrades are in service. Behind-the-meter generation netting rules found no longer just; new materiality threshold with three-year transition and grandfathering. Paper hearing set on rates | 18 Dec 2025, 193 FERC ¶ 61,217, Docket EL25-49-000 et al. | FERC order as summarised in the June order below; Baker Botts summary, https://www.bakerbotts.com/thought-leadership/publications/2025/december/ferc-issues-order-providing-guidance-for-co-locating-power-plants-with-data-centers-within-pjm |
| PJM compliance filing | Second compliance filing, Docket ER26-1479 | 23 Feb 2026 | June order, below |
| Rehearing and compliance order | Rehearing requests (Exelon, FirstEnergy, Constellation and others) addressed; December Order modified and set aside in part; PJM compliance accepted in part, rejected in part; rates, terms and conditions set for Interim NITS, FCD and NFCD; further PJM and transmission-owner compliance within 60 days; BTMG threshold to be load-based | 18 Jun 2026, 195 FERC ¶ 61,209, Docket EL25-49-002 | FERC order, https://www.ferc.gov/sites/default/files/2026-06/EL25-49-002_0.pdf |
| Extension | 90 days granted; deadline for PJM and transmission owners now **16 Nov 2026**; PJM made a partial filing on 17 Aug 2026 covering Interim NITS | Notice 14 Aug 2026 | FERC notice, https://www.pjm.com/-/media/DotCom/documents/ferc/orders/2026/20260814-el25-49-002-et-al.pdf |
| Linked | Large Load Show Cause Order, 195 FERC ¶ 61,211 (2026) | 2026 | same notice |

So by November 2026 there are rules for co-location in PJM but they are not finished, while every
large nuclear-for-AI deal announced since mid-2025 has gone front of the meter.

### 3c. Deal table

| Deal | MW | Term | Meter | Binding? | Date | Source |
|---|---|---|---|---|---|---|
| Microsoft–Constellation, Crane restart | 835 | 20-year PPA | Front (feeds PJM) | Binding PPA | 20 Sep 2024 | Constellation release (in live piece); DOE loan US$1bn closed 18 Nov 2025, https://www.constellationenergy.com/news/2025/11/us-government-backs-constellations-plan-to-launch-crane-clean-energy-center-adding-835-mws-of-new-baseload-power-to-the-grid.html |
| Amazon–Talen, Susquehanna | up to 1,920 | to 2042 | Front since April 2026 (was co-located) | Binding PPA | 11 Jun 2025 | above |
| Meta–Constellation, Clinton | 1,121 incl. 30 uprate | 20 years from June 2027 | Front | Binding PPA | 3 Jun 2025 | above |
| Google–NextEra, Duane Arnold restart | 615 | 25-year PPA; CIPCO buys the rest on same terms | Front (grid) | Binding PPA; restart needs NRC approval | 27 Oct 2025 | press: ANS, 28 Oct 2025, https://www.ans.org/news/2025-10-28/article-7501/nextera-and-google-ink-a-deal-to-restart-duane-arnold/ ; WNN |
| Amazon–Constellation, Calvert Cliffs | 690 incl. 190 uprate | 20 years | Front | Binding PPA | 30 Sep 2026 | above |
| Google–Constellation | 890 uprate (+2,700 existing, 15-yr) | 20 years | Front | Binding PPA | 6 Oct 2026 | above |
| Google–Georgia Power | ~96 uprate | not public | Tariff subscription (NU-1) | Needs PSC approval | 21 Sep 2026 | press, above |
| Meta–Vistra | 2,609 incl. 433 uprate | 20-year PPAs | Front (PJM) | Binding PPAs | Jan 2026 | Vistra 8-K above |
| Meta–TerraPower | 2 Natrium units (up to 690 MW) funded; rights to up to 6 more (2.1 GW) by 2035; 2.8 GW + 1.2 GW storage in all | not stated | not stated | Meta funds development of 2 units; the other 6 are rights, not orders | 9 Jan 2026 | TerraPower, https://www.terrapower.com/terrapower-announces-deal-with-meta ; Meta, https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/ |
| Meta–Oklo | up to 1.2 GW, Pike County, Ohio, into PJM | not stated | Front (PJM) | Prepay framework; Oklo says not a PPA | 9 Jan 2026 | Meta above; Oklo 10-Q 6 Nov 2026 (in live piece) |
| Google–Kairos | 500 MW by 2035 (master plant development agreement) | | | Framework | 14 Oct 2024 | Kairos, https://www.kairospower.com/updates/google-kairos-power-tva-collaborate-to-meet-americas-growing-energy-needs |
| Google–Kairos–TVA, Hermes 2 | up to 50 | not stated | Front (TVA grid serving Google's TN and AL data centres) | Binding utility PPA | 18 Aug 2025 | same |
| Amazon–X-energy | >5 GW by 2039 target; equity investment in X-energy (2024) | | | Target, not contract | Oct 2024 | X-energy release, https://x-energy.com/news/amazon-invests-in-x-energy-to-support-advanced-small-modular-nuclear-reactors-and-expand-carbon-free-power/ ; X-energy 424B4 2026, https://www.sec.gov/Archives/edgar/data/0002088896/000110465926049515/tm2527015-22_424b4.htm |
| Amazon–Energy Northwest, Cascade (WA) | 320 MW (4 Xe-100), option to 960 MW (12); public utilities may take up to 50% | | | Development and funding agreement; NRC construction permit application targeted by end 2026, not yet filed | Oct 2024 | same X-energy filings |

Pattern: binding 20-year PPAs sit on existing reactors and their uprates; advanced-reactor deals are
funding frameworks, rights or targets. All the binding ones put power into the grid, not behind the meter.

---

## 4. Why hyperscalers want nuclear

| Fact | Figure | Date | Source |
|---|---|---|---|
| US nuclear capacity factor | 91.1% (2025); 90.8% (2024); 93.0% (2023) | EIA Electric Power Monthly, released 23 Oct 2026 | EIA Table 6.07.B, https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b |
| Wind | 33.8% (2025) | same | same |
| Solar PV (utility scale) | 24.0% (2025) | same | same |
| Gas combined cycle | 58.7% (2025) | same | EIA Table 6.07.A, https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a |
| Coal | 48.8% (2025) | same | same |
| Nuclear generation 2025 | 785,304 GWh | same release | EIA Table 1.1, https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_1_01 |
| Nuclear share of US electricity 2025 | 17.7% of utility-scale generation (785,304 / 4,425,029 GWh); 17.4% including small-scale solar | calc from Table 1.1 | same |
| Google's goal | 24/7 carbon-free energy on every grid where it operates by 2030 (hourly matching); hourly CFE was 66% in 2024 (2025 report). 2025 figure not retrieved from the 2026 report | 2025, 2026 | https://sustainability.google/reports/google-2026-environmental-report/ ; press: Bloomberg Law, 19 May 2026, says goal "remains" |
| Google's nuclear tally | "over 1.5 GW of new nuclear capacity through uprates and restarts" enabled | 6 Oct 2026 | Google blog above |
| DOE goal | 5 GW from uprates and restarts by 2030; Google expects its deals to meet about 25% | 6 Oct 2026 | Google blog above |

Why it matters: an hourly 24/7 goal cannot be met by solar at 24% or wind at 34% without storage.
Nuclear at 91% is the only carbon-free source that runs nearly every hour.

---

## 5. US fleet for scale

| Fact | Figure | Date | Source |
|---|---|---|---|
| Operating reactors | 94 at 54 plants in 28 states. Palisades and Crane are reported by their owners as "operating but out of service" in EIA's survey | March 2026 | EIA FAQ, https://www.eia.gov/tools/faqs/faq.php?id=207&t=3 |
| Capacity | 98,408 MW time-adjusted (2025 average) | 2025 | EIA Table 6.07.B |
| Largest state | Illinois, 11 reactors, 11,592 MW, 12% of US nuclear capacity | March 2026 | EIA FAQ id=207 |
| Average age | About 44 years | March 2026 | EIA FAQ, https://www.eia.gov/tools/faqs/faq.php?id=228&t=3 |
| Oldest / newest | Nine Mile Point 1 (Dec 1969) / Vogtle 4 (Apr 2024) | | same |
| Licence terms | 40 years initial; 20-year renewal to 60; second 20-year renewal to 80 | | same |
| 80-year licences | Recent: Browns Ferry 1-3 (Dec 2025), St. Lucie 1-2 (spring 2026), Robinson 2 (2026), Hatch 1-2 (June 2026, under 12 months); earlier Turkey Point 3-4, Peach Bottom 2-3, Surry 1-2, North Anna 1-2, Monticello, V.C. Summer 1, Oconee 1-3, Point Beach 1-2. No authoritative total retrieved | 2020 to 2026 | press: ANS, 12 Jun 2026, https://www.ans.org/news/article-8118/hatch-slr-approved-by-nrc-in-under-12-months/ ; NRC SLR page, https://www.nrc.gov/reading-rm/doc-collections/fact-sheets/subsequent-license-renewal.html |
| Pending 80-year renewals | Nine Mile Point 1, Cooper; Ginna expected mid-2026; about nine more in 2027 | Jun 2026 | press: ANS, 12 Jun 2026 |

---

## 6. What the live piece has wrong or out of date

1. **Uprate definition is too narrow.** The piece says an uprate means fitting "bigger turbines ... while it is shut to refuel". Per the NRC, MURs (<2%) are feedwater meter upgrades and stretch uprates (up to 7%) are mostly setpoint changes. Only extended uprates (up to 20%) need new turbines, generators and transformers. Seven of Constellation's twelve listed filings are MURs.
2. **Uprates are bigger than the piece shows.** The ladder counts only Google's 890 MW. AI buyers have also contracted Calvert Cliffs ~190 MW (Amazon, 30 Sep 2026), Vistra 433 MW (Meta, Jan 2026), Clinton 30 MW (Meta), Georgia Power ~96 MW (Google, pending PSC). Total 1,639 MW (calc). The piece's "ordinary fuel 3,440 MW" understates the lane its claim says comes first.
3. **New: DOE conditional loan of up to US$5bn for Constellation uprates (27 Oct 2026)** across eight plants. Not in the piece.
4. **Darlington date.** The piece says "GE Vernova spoke of operation by the end of 2029" (27 Jan 2025). OPG's own target since 2025 is construction done by end of decade and grid connection by end of 2030 (ANS, 5 Jun 2026; Ontario, May 2025). Basemat set 22 April 2026. Use OPG's date, not the vendor's. The operating-licence hearing is not yet scheduled.
5. **Talen–Amazon is now done.** The piece says the parties agreed on 11 June 2025 to move in front of the meter. Talen's 10-Q: the transition "occurred in April 2026".
6. **FERC's co-location order is missing.** 18 Dec 2025 order (EL25-49), June 2026 rehearing/compliance order, compliance deadline extended to 16 Nov 2026. This is the rulebook that pushed deals in front of the meter.
7. **No uprate is under NRC review** (pending list empty, 15 Sep 2026) and the last approval was Millstone 3 in Nov 2021. The piece's "NRC amendment where heat rises" is right, but it should say none of the AI-funded uprates has been filed yet; Constellation's first EPU filing is listed for Q4 2026.
8. **Clinch River is missing.** First US BWRX-300 construction permit, 29 Sep 2026, ordinary fuel, target 2033 (press). It is the US counterpart to Darlington and a better fit for a US claim test.
9. **"Twelve Constellation applications, the last due in late 2030"** is correct (first Q4 2026). Note the NRC list's own totals do not reconcile (31 in summary vs 30 itemised).
10. **Fleet count.** EIA's 94 operating reactors (March 2026) include Palisades and Crane as "out of service"; worth saying if the piece cites 94.
11. **Large AP1000s.** Nothing in the piece. Status: US$80bn US–Westinghouse partnership (Oct 2025) and a Korea framework (Sept 2026) remain non-binding; no US site or order as of 30 Oct 2026 (Cameco Q3). Fermi America's four-unit COLA is in review, first unit planned 2032.
