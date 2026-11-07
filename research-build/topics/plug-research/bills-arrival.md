# Plug research: who pays for the connection, and how capacity actually arrives

Research slice for the investor-grade rebuild of `america-rations-the-plug`, absorbing the US parts of `contracted-energised-running`. Gathered 7 November 2026. Read-only research; nothing in `src/` was edited.

Tags: **primary** = the regulator's, grid operator's or company's own document, opened by me; **call** = a company's own earnings call or podcast, from its own site or as transcribed; **press** = trade press, law firm or news summary of a primary document I could not open; **calc** = my arithmetic. No share prices, valuations or views on shares are recorded here (CoreWeave's and Jane Street's equity details were deliberately left out).

---

## 1. Fact tables: who pays

### 1a. PJM capacity auction and the household bill

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| 2028/29 Base Residual Auction clearing price | $325/MW-day UCAP, the FERC-approved cap, whole footprint; down 2.5% from $333.44 | Results 14 Jul 2026 | https://insidelines.pjm.com/pjm-capacity-auction-procures-138318-mw-of-generation-resources-as-work-continues-to-address-growing-electricity-demand/ | primary |
| 2028/29 shortfall and new plant | 6,831 MW short of the reliability requirement; 525 MW UCAP of new generation and uprates cleared | 14 Jul 2026 | same | primary |
| 2028/29 auction value | $16.4bn (cleared supply x price). PJM: "does not equate to the total cost to load" | 14 Jul 2026 | same | primary |
| Price the 2028/29 auction would have cleared at without the collar | $554.72/MW-day footprint; up to $776.69 in the Chicago region | Jul 2026 | APPA / New Project Media summarising PJM: https://www.publicpower.org/periodical/article/pjm-capacity-auction-procures-138318-mw-generation-resources-capacity-price-comes-cap-325 | press |
| Collar extended to 2028/29 and 2029/30 | FERC accepted PJM's tariff revisions (ER26-1556); floor $175, cap $325/MW-day reported | 28 Apr 2026 | https://www.jdsupra.com/legalnews/ferc-accepts-pjm-capacity-market-price-1132646/ ; PJM filing https://www.pjm.com/-/media/DotCom/documents/ferc/filings/2026/20260406-er26-1556-000.pdf | press (filing exists, not opened) |
| Market monitor: data-centre share of 2028/29 auction | $6.3bn of $16.4bn, 38.2% | 27 Jul 2026 | Monitoring Analytics, MC webinar, slide 4: https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20260727-web/item-02---marketing-monitoring-report---presentation.pdf | primary |
| Market monitor: four auctions combined | $29.4bn, 46.2% of total capacity market charges over 2025/26 to 2028/29 | 27 Jul 2026 | same | primary |
| Market monitor: 2027/28 auction | $6.5bn, 39.6% of that auction's cost | Jan 2026 | MC report 22 Jan 2026 https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20260122/20260122-item-06---market-monitoring-report---presentation.pdf (via Bloomberg 5 Jan 2026) | press (deck not opened) |
| Market monitor: 2025/26 auction | $9.3bn, 63% of the price increase attributed to data-centre load | 2025 | IEEFA summary https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10 | press |
| Data-centre load in each auction's forecast (all / above embedded) | 2025/26: 7,927 / 4,654 MW; 2026/27: 11,993 / 7,892; 2027/28: 17,071 / 13,018; 2028/29: 21,470 / 16,436 | 27 Jul 2026 | Monitoring Analytics slide 6 (link above) | primary |
| Monitor's position on who should pay | Data-centre load "should be removed from the capacity market and procured through a dedicated auction... ensure that data centers pay for their own capacity" | 27 Jul 2026 | slide 4 | primary |
| Effect on wholesale cost per MWh, H1 2026 | $114.50/MWh with data-centre capacity effect vs $103.40 without: +$11.11, 9.7% | 27 Jul 2026 | slide 14 | primary |
| Total wholesale cost, H1 2026 vs H1 2025 | $114.50 vs $76.16/MWh, +50.3% ($46.34bn vs $30.07bn). Energy +47.7% (63.5% of total); capacity +207.1% (17.1% of total); transmission +5.6% (17.4%) | 27 Jul 2026 | slides 11 to 12 | primary |
| Household bills, Pennsylvania, from 1 Jun 2026 | PECO price to compare 11.76 c/kWh, about +$4.94/month (3.1%) at 700 kWh; West Penn Power about +10.3%; Duquesne about +2.84%; PUC ties the rise to PJM capacity costs phasing in | PUC release 20 May 2026 | https://www.puc.pa.gov/press-release/2026/puc-alerts-consumers-to-june-1-electric-price-changes-and-higher-summer-energy-costs-5-20-26 (connection refused; figures via WHYY and others) | press |
| Virginia's legislative auditor on household cost | Data-centre growth could add $14 to $37/month to a typical household's generation and transmission costs by 2040, 2024 dollars | 9 Dec 2024 | JLARC Report 598 (sidecar, verified 29 Oct) https://jlarc.virginia.gov/pdfs/reports/Rpt598.pdf | primary (not re-opened) |

### 1b. Federal and regional decisions on who pays

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| DOE directs FERC to consider large-load interconnection rule (RM26-4) | ANOPR under DOE Act s.403; FERC asked to act by 30 Apr 2026; FERC said it would act by end June 2026 | 23 Oct 2025; FERC order 16 Apr 2026 | https://www.ferc.gov/RM26-4 ; Willkie memo (below) | press |
| FERC co-location order for PJM (EL25-49) | PJM tariff found unjust and unreasonable; PJM to add new transmission services for co-located loads, incl. an interim service; compliance due 2026 | 18 Dec 2025 | law-firm summaries, e.g. https://www.bdlaw.com/publications/ferc-orders-pjm-to-create-clear-rules-for-co-located-data-centers-and-large-loads/ | press |
| FERC show cause orders to six RTOs | Large load = new site 50 MW or more above 69 kV (not 20 MW as in the ANOPR); justify or revise tariffs in 60 days; reports in 30 days | 18 Jun 2026 | Willkie Farr memo 30 Jun 2026: https://www.willkie.com/publications/2026/06/ferc-directs-grid-operators-to-reform-procedures-for-large-loads-connecting-to-the-bulk-transmission ; orders 195 FERC ¶ 61,211 to 61,216 | press (orders listed in sidecar as primary) |
| FERC's cost guidance in those orders | Pro forma "Cost Recovery Agreements" with "minimum financial commitments toward necessary upgrades" so others are protected from stranded cost; post Network Upgrade cost data; escalating financial commitments; interim as-available service while upgrades are built | 18 Jun 2026 | Willkie memo, pp. 3 to 5 | press |
| White House and 13 PJM governors, Statement of Principles | Backstop auction for 15-year new capacity; extend collar through 2028/29 and 2029/30; backstop costs to LSEs serving new data centres that have not self-procured or agreed to be curtailable | 16 Jan 2026 | Latham summary https://www.lw.com/en/insights/us-data-center-demand-white-house-and-governors-issue-principles-while-pjm-issues-decisional-letter ; IL and NJ governors' letter https://www.pjm.com/-/media/DotCom/about-pjm/who-we-are/public-disclosures/2026/20260121-il-nj-govs-letter-re-national-energy-dominance-council-and-13-governors-statement-of-principles.pdf | press (letter exists, not opened) |
| PJM Board decision on large loads | New Large Loads that do not bring own generation by 1 Jun 2027 are curtailed in shortages before pre-emergency load management; exclude incremental new Large Loads from auction demand from 2029/30; "existing consumers should not pay higher capacity costs caused by new Large Loads"; registry at 50 MW within one mile; backstop up to 15-year terms, cost cap $555/MW-day; PJM "cannot directly allocate retail costs", needs the states | 27 Jul 2026 | https://insidelines.pjm.com/pjm-board-directs-action-on-resource-adequacy-affordability-and-large-loads/ | primary |
| FERC on PJM's backstop (ER26-3380) | Accepted, suspended to 28 Feb 2027 subject to refund, paper hearing | 29 Sep 2026 | https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/9154/20260929-er26-3380-000.pdf (sidecar) | primary (not re-opened) |
| FERC on PJM's large-load package (ER26-3515) | Accepted only Large Load definition and registry; rejected interim service, bring-your-own and removal from auction demand | 9 Oct 2026 | sidecar, 197 FERC ¶ 61,019 | primary (not re-opened) |
| PJM amended backstop filing | Aims to start 1 Mar 2027; changes cost allocation method, LSE credit and exit rules; target cut by bilateral contracts; reviewed at Special MC 22 Oct | late Oct 2026 | Utility Dive https://www.utilitydive.com/news/pjm-revised-data-center-backstop-procurement-ferc/873551/ ; APPA https://www.publicpower.org/node/31581 | press |

### 1c. Large-load tariffs that make the data centre pay

| Utility / state | Threshold | Minimum take | Term and ramp | Exit | Collateral | Date and source | Tag |
|---|---|---|---|---|---|---|---|
| Dominion, Virginia, Rate Schedule GS-5 | 25 MW or more on a contiguous site, load factor 75% or more | Distribution 85%, transmission 85%, generation 60% of contracted demand; PJM capacity expense excluded from the generation minimum | 14 years; ramp up to 4 years within the term, at least 20% a year; minimums continue after the term | Exit fee = all outstanding minimum charges for the remaining term | $1.5m per MW, cut up to 70% for credit, 1/14 released each year; letters of credit and guarantees allowed | SCC Final Order, Case PUR-2025-00058, 25 Nov 2025, pp. 23 to 27; applies to ESAs signed from 1 Jan 2027; effective 1 Jan 2027. Capacity may be cut 20% free, a further 30% if another customer takes it, 36 months' notice each. https://npr.brightspotcdn.com/b6/ac/706130b64d2b8eee6a9832b97e48/20251125-virginiascc-dominionenergyruling.pdf | primary |
| Dominion GS-5 cost of service | GS-5-type customers earned 6.28% overall and 3.01% on transmission at end-2024, lowest of all classes but outdoor lighting; GS-4 others 20.75% / 22.41% | same order, pp. 16 to 17 | | | | SCC directs alternative transmission cost allocations in next filing | primary |
| AEP Ohio, Schedule DCT | Data centres above 25 MW | 85% of subscribed demand | Up to 12 years incl. 4-year ramp | Three years of minimum charges | 50% of minimum charges unless credit standards met | PUCO order 9 Jul 2025, Case 24-508-EL-ATA; PUCO bulletin https://content.govdelivery.com/accounts/OHPUC/bulletins/3e8bb79 (confirms order and moratorium lift only); terms via POWER and New Project Media | primary (order) / press (terms) |
| Georgia Power | New customers over 100 MW | Minimum billing allowed; pay upstream generation, transmission and distribution costs as construction progresses | Contracts may run 15 years (from 5) | not stated | not stated | Georgia PSC release, 23 Jan 2025: https://psc.ga.gov/site/assets/files/8617/media_advisory_data_centers_rule_1-23-2025.pdf ; every such contract goes to the PSC | primary |
| Indiana Michigan Power (AEP) | 70 MW, or 150 MW aggregated per company | Not confirmed (80% widely reported) | At least 12 years, after up to 5-year ramp | Exit fee above 20% reduction; up to 20% cut free after 5 years on 42 months' notice | not stated | Settlement filed 22 Nov 2024; IURC approved Feb 2025 with change: cuts above 20% need IURC review. https://www.utilitydive.com/news/indiana-michigan-power-aep-amazon-google-microsoft-data-center-interconnect/733850/ | press |
| Oregon, POWER Act (HB 3546) | Data processing sites of 20 MW or more | PUC sets minimum payment commitments | Contracts of at least 10 years; separate rate class | | | 2025 session; PGE Schedule 96 approved May 2026. PUC report: https://www.oregon.gov/puc/forms/Forms%20and%20Reports/2026%20POWER%20Act%20Legislative%20Report.pdf | press (PUC report not opened) |
| Texas, SB 6 (89th Leg.) | 75 MW (PURA 37.0561(c)) | n/a | n/a | Security refundable as ramp milestones met | Uniform financial commitment per MW set by PUCT (37.0561(h)); flat study fee at least $100,000 (37.0561(f)); load must "contribute to the recovery" of interconnection cost (35.004(c-1)); PUCT to review 4CP transmission charges and amend rules by 31 Dec 2026 (s.6); net-metering deals may require others "held harmless for stranded or underutilized transmission assets" (39.169(d)) | Enrolled bill https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm | primary |
| Texas, PUCT rule (Project 58481, 16 TAC 25.194) | 75 MW or more | n/a | Energisation schedule window 24 months (proposal: 6) | Missed milestones: security applied to amounts owed within 60 days, balance returned | Flat $100,000 study fee whatever the size; proposed $50,000/MW non-refundable fee dropped | Adopted, reported 21 Sep 2026 (vote likely 18 Sep, my inference). https://utilitydive.com/news/texas-puc-adopts-data-center-interconnection-rules/830899 | press |

### 1d. What the tariffs did to the queue (the stage gap, made visible by a price)

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| AEP Ohio queue before tariff | "more than 30 GW of initial queue interest" | 2024 to 2025 | New Project Media https://newprojectmedia.com/policy-aep-ohio-touts-right-sized-load-as-data-center-pipeline-shrinks-further-under-new-tariff/ | press |
| Formal study requests once tariff took effect | 13,022.7 MW, 36 sites (9,807.7 MW Central Ohio) | 2025 | same, citing AEP Ohio letter to PUCO, 12 Feb (2026) | press |
| Signed ESAs | 12,219 MW before the tariff + 5,642 MW under it = 17,861 MW; in-service dates by 2030 | AEP letter 12 Feb 2026 | same | press |

---

## 2. Fact tables: how capacity actually arrives

### 2a. Utility pipelines against load actually billed

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| Dominion data-centre contracts, by stage | About 54 GW "under contract": 32,473 MW Engineering Letters of Authorization (ELOA), 9,356 MW Construction Letters of Authorization (CLOA), 11,997 MW Electric Service Agreements (ESA) | Contracts as of July 2026; deck 29 Sep 2026 | Dominion to PJM Load Analysis Subcommittee: https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2026/20260929/20260929-item-5ai---dominion_energy.pdf | primary |
| Dominion data-centre load actually billed | "Data center billing peak load as of August 2026 is 4.8 GW" (chart value 4,838 MW for 2026F; the chart's two series, coincident and billing, did not extract cleanly, so only the billing figure is used); 55 data-centre companies, about 500 metered accounts | As of Aug 2026 | same, slides 2 to 3 | primary |
| Dominion's own ramp assumption | "industry average ramp period is 5 years maturing at a utilization rate of 63% (Utilization Rate = Demand / Contract Capacity)" | 29 Sep 2026 | same, slide 5 | primary |
| What Dominion counts as firm | Firm = executed ESAs and CLOAs; ELOAs non-firm (2032 on); 19 GW (59%) of ELOAs excluded from the forecast | 29 Sep 2026 | same | primary |
| Contracted-to-billed ratio | About 54 GW under contract vs 4.8 GW billing peak: about 11 to 1; ESA alone (12.0 GW) about 2.5 to 1 | calc | | calc |
| ERCOT large loads approved vs operating | 9,042 MW with Approval to Energize; 3,883 MW non-simultaneous monthly peak counted operational | Mar 2026 TAC report | https://www.ercot.com/files/docs/2026/03/12/March-TAC-Report.pdf (403, read via search summary) | press |

### 2b. Companies: contracted vs active, by their own definitions

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| CoreWeave active vs contracted power | Q3 2025: ~590 MW active / ~2.9 GW contracted. Q4 2025: >850 MW / ~3.1 GW. Q1 2026: >1 GW / >3.5 GW. Q2 2026: 1.5 GW (added nearly 500 MW) / ~3.7 GW | 10 Nov 2025; 26 Feb 2026; 7 May 2026; 11 Aug 2026 | 8-K exhibits: https://www.sec.gov/Archives/edgar/data/1769628/000176962825000059/coreweave3q25earningspress.htm ; .../000176962826000094/coreweave4q25earningspress.htm ; .../000176962826000220/coreweave1q26earningspress.htm ; .../000176962826000362/coreweave2q26earningspress.htm | primary |
| CoreWeave ratio | 1.5 / 3.7 GW = about 41% of contracted power active at 30 Jun 2026 (20% at 30 Sep 2025) | calc | | calc |
| CoreWeave power still undelivered at two lease groups | 393 MW at one site (phases 2026 to 2028; rent capped at $14.7bn over the term); 355 MW at other sites (2026 to 2028) | 30 Jun 2026 | 10-Q, 12 Aug 2026: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm | primary |
| CoreWeave leases signed, not commenced | $35.5bn of future undiscounted payments, starting 2026 to 2029, terms 7 to 16 years | 30 Jun 2026 | same 10-Q | primary |
| CoreWeave 10-Q on New York | Cites a "moratorium on the development of data centers using 50 megawatts of power or more in the State of New York that was announced in July 2026" | 12 Aug 2026 | same 10-Q, risk factors | primary (CoreWeave's description; NY order not opened) |
| CoreWeave's delay case | Cut 2025 revenue outlook citing "temporary delays related to a third-party data center developer who is behind schedule"; CEO: "one delay at a singular data center", mostly resolved "within Q1 of next year" | 10 Nov 2025 | Q3 2025 call as reported, e.g. https://www.datacenterdynamics.com/en/news/coreweave-q3-earnings-show-revenue-backlog-doubled-to-556bn/ | call (as reported) |
| Nebius stage definitions | Q4 2025 letter: "contracted power, or power secured by contracts; connected power, or power connected into data centers; active power, or power being consumed by IT equipment" | 12 Feb 2026 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926013946/tm266173d1_ex99-2.htm | primary |
| Nebius US sites | Nine new sites announced Feb 2026 incl. US: Missouri, Alabama, Oklahoma, Minnesota. Q2 letter map lists New Jersey, Missouri, Oklahoma, Alabama, Minnesota, Kansas City, Pennsylvania | 12 Feb and 12 Aug 2026 | Q4 letter above; Q2 letter https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-2.htm | primary |
| Nebius capacity guidance | 5 GW contracted by end 2026 (from >4 GW); "deploy more than 1 GW per year, starting in 2027"; "brought additional capacity online across sites in the US and Europe"; all Microsoft tranches delivered; Q3 short-term deals >$40m/MW ACV | 12 Aug 2026 | Q2 letter | primary |
| Nebius per-site MW | Not disclosed in the letters. Vineland NJ: "up to 300 MW" (Nebius release 5 Mar 2025); Kansas City: 5 MW start, scalable to 40 MW; Independence MO: 1.2 GW campus approved Mar 2026, ground broken; Pennsylvania 1.2 GW announced May 2026, 250 to 350 MW live by end 2027 (CEO, press) | 2025 to 2026 | https://nebius.com/newsroom/nebius-accelerates-us-expansion-adding-up-to-300-mw-capacity-at-new-data-center-in-new-jersey ; DCD on Independence and Pennsylvania | primary (Vineland release) / press (rest) |
| Nebius Q3 2026 | No results yet (due 12 Nov 2026). Latest filings: 6-K 1 Oct 2026 (Inferize acquisition), 6-K 22 Oct 2026 (bridge loan); neither gives power figures | checked 7 Nov 2026 | EDGAR submissions, CIK 1513845 | primary |
| Oracle lease commitments not yet commenced | $288bn, "substantially all related to data center arrangements", commencing Q2 FY2027 to FY2029, terms 15 to 19 years, against $48.05bn of lease payments already on balance sheet | 31 Aug 2026 | Oracle 10-Q, 11 Sep 2026: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm | primary |
| Oracle remaining performance obligations | $664bn (from $455bn a year earlier); about 13% to be recognised in the next 12 months, 37% in months 13 to 36 | 31 Aug 2026 | same 10-Q | primary |
| Oracle capex | $28.5bn in Q1 FY2027 | quarter to 31 Aug 2026 | same 10-Q | primary |
| Microsoft on constraint (latest) | Hood: "some third-party capacity deliveries we expected in Q1 were delayed"; "3P GPU as a service contracts that have been delayed to H2"; "Customer demand continues to exceed available supply." Nadella: 24 new data centres in the quarter; "reducing dock-to-live times by about 20 percent quarter over quarter". No statement about power availability on this call | FY27 Q1 call, 28 Oct 2026 (date per press) | https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1 | call |
| Microsoft on constraint (earlier) | Nadella: the problem is not a compute glut but power and "warm shells"; "you may actually have a bunch of chips sitting in inventory that I can't plug in" | BG2 podcast, early Nov 2025 | as reported, e.g. https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-ceo-says-the-company-doesnt-have-enough-electricity-to-install-all-the-ai-gpus-in-its-inventory-you-may-actually-have-a-bunch-of-chips-sitting-in-inventory-that-i-cant-plug-in | call (podcast, as reported) |

### 2c. Abilene (Crusoe, Oracle, OpenAI)

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| Grid connection and backup | "1.2 GW grid interconnection"; campus to "feature natural gas turbines to power its back-up power supply"; Lancium plans "behind-the-meter battery storage and solar"; 8 buildings, about 4m sq ft; each building up to 50,000 GB200 (wording "NVL72s" in release) | 18 Mar 2025 | https://www.crusoe.ai/resources/newsroom/crusoe-expands-ai-data-center-campus-in-abilene-to-1-2-gigawatts | primary |
| Phase timing as first stated | Phase 1, two buildings, 200+ MW, energised H1 2025 expected; phase 2, six buildings, completion mid-2026 expected | 18 Mar 2025 | same | primary |
| On-site gas, size | About 360 MW initial on-site gas (GE LM2500XPRESS and Solar Titan 350 units), permitted through Texas "permits by rule" and standard permits; 10 turbines and 62 diesel generators in 2024 permits; a later major permit for 41 more turbines | 2024 to 2026 | Cleanview https://cleanview.co/reports/behind-the-meter-data-centers/full-report/stargate-abilene ; Texas Tribune / Route Fifty, Jul 2026 | press |
| Delivered to the customer | 6 of 8 buildings, 618 MW, 75% of capacity; 131,000 GPUs delivered there in the quarter | Oracle call 10 Sep 2026 | as transcribed (fool.com; Epoch AI quotes the same words) | call |
| Last two buildings | Oracle (June call) put them in its quarter to 30 Nov 2026; no confirmation found yet; final building topped out (press, undated) | as of 7 Nov 2026 | DCD https://datacenterdynamics.com/en/news/crusoe-tops-out-final-building-at-openai-stargate-data-center-campus-in-abilene-texas | press |
| Expansion dispute | Bloomberg and Reuters reported Oracle and OpenAI dropped a planned 600 MW expansion at the site; Oracle called the reports "false and incorrect" | 2026 (date not confirmed) | Tom's Hardware https://tomshardware.com/tech-industry/oracle-rebuts-incorrect-reporting-on-stargate-expansion | press |
| Microsoft campus next door | Crusoe's 900 MW Abilene campus for Microsoft; first building energised mid-2027 | 27 Mar 2026 | Crusoe release (in contracted-energised-running sidecar) | primary (not re-opened) |

### 2d. Jane Street

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| CoreWeave commitment | About $6bn "to use CoreWeave's AI cloud platform"; "next-generation compute across multiple facilities, including NVIDIA's Vera Rubin technology"; no MW, term or delivery date given | 15 Apr 2026 | https://investors.coreweave.com/news/news-details/2026/Jane-Street-Signs-6-Billion-AI-Cloud-Agreement-With-CoreWeave/default.aspx | primary |
| Own site | Reportedly seeking 100 to 200 MW for its own data centre to train internal models; talks early, no location or capacity decided; currently runs from a Dallas data centre | 4 Jun 2026 | Bloomberg Law https://news.bgov.com/crypto/jane-street-plans-new-data-center-as-compute-power-runs-scarce ; DCD | press |
| Texas site (existing) | 4,032 GPUs in 56 racks (Jane Street's own write-up, undated) | | sidecar | primary (not re-opened) |
| Other Jane Street capacity deals (Nebius, Lambda, others) | None found | | | |

---

## 3. Plain-English explainers

### The five stages an AI campus passes

1. **Announced (contracted).** The builder has signed for land and the right to power. At a utility this is a letter or an agreement: Dominion's ladder runs from an engineering letter (study the substation), to a construction letter (start building it), to an electric service agreement (the utility commits to serve, the customer to pay). Nothing exists yet but paper.
2. **Being built.** The shell, the cooling plant and the substation go up. Many crews can work at once, so this is rarely the slowest step.
3. **Energised.** The utility switches the connection on. This waits on made-to-order transformers and the utility's own lines and tests, so it is the step money speeds least. Gas turbines on site, as at Abilene, can bridge it.
4. **Delivered.** The finished, powered hall is handed to the tenant. Oracle reports Abilene at this stage, building by building.
5. **Running.** Chips are racked and drawing power for paying work. Nebius calls this "active power", CoreWeave the same. Only this stage earns.

The numbers between the stages are large. Dominion has about 54 GW of data centres under some form of contract and bills about 4.8 GW. CoreWeave has 3.7 GW contracted and 1.5 GW active. Oracle has US$288 billion of data-centre leases signed that have not yet started. Even Dominion's own planning assumes a site takes five years to reach 63% of the power it contracted.

### Who pays for the connection

Three bills hang on a new data centre, and each is paid differently.

- **The wires to the site.** Each tariff now makes the data centre carry its own lines and substation, with collateral up front: Dominion asks US$1.5 million a megawatt, AEP Ohio half the minimum charges, Texas a per-megawatt security set by its regulator.
- **The shared network and the power stations.** These are paid by everyone over 20 to 40 years. The minimum bills (Dominion 85% of contracted demand for the wires and 60% for generation, AEP Ohio 85%, terms of 10 to 15 years) make sure a site that never fills still pays its share. They protect against the empty site. They do not change who pays while the site is full.
- **The PJM capacity auction.** This is the bill for power stations standing ready, and it is shared across every customer in the zone. The market monitor puts 38.2% of the latest auction, US$6.3 billion, on data-centre load. Dominion's GS-5 minimum explicitly leaves PJM capacity out. The fixes on the table are PJM's backstop, with costs assigned by large-load growth, and its plan to cut new large loads off first in a shortage unless they bring their own supply. FERC has accepted neither in full, so households still share this bill.

---

## 4. What the live pieces have wrong or out of date

**america-rations-the-plug**

1. **Virginia is now primary, and fuller than the piece says.** The sidecar treated the SCC orders as press-only. The SCC Final Order of 25 November 2025 (PUR-2025-00058) is readable and sets GS-5: 25 MW and 75% load factor, 14-year term with a ramp of up to four years, minimum charges of 85% (distribution), 85% (transmission) and 60% (generation), US$1.5 million a megawatt collateral, an exit fee equal to all remaining minimums, and free reductions of up to 20%. "14 year terms with minimum bills" is right but undersells it. The table cell "Who carries the wait: the customer if it never fills; shared if it does" should add that PJM capacity cost is excluded from the generation minimum, so the auction bill stays shared even in Virginia.
2. **The household bill is not mainly the capacity auction.** The piece implies households carry the wait through the auction. The monitor's own figures show H1 2026 wholesale cost up 50.3%, of which energy rose 47.7% and was 63.5% of the total; capacity was 17.1%. The data-centre capacity effect was US$11.11/MWh, 9.7%. The piece should size the auction's share rather than imply it is the whole bill.
3. **Missing: the collar's uncapped price.** Without the collar the 2028/29 auction would have cleared at about US$554.72/MW-day (as reported from PJM). The collar was extended to 2028/29 and 2029/30 by FERC on 28 April 2026. Both sharpen "a price cannot buy what factories have not built".
4. **"In August PJM asked..."**: the PJM Board decided the package on 27 July 2026 (Inside Lines). The filing date should be checked before the sentence keeps "August".
5. **Missing: the other states.** The piece names only Virginia. AEP Ohio (85%, 12 years, 2025), Georgia (100 MW, 15 years, 2025), Indiana (70 MW, 12 years plus ramp, 2025), Oregon (20 MW, 10 years) and Texas SB 6 with the PUCT's rule of September 2026 (flat US$100,000 study fee, security forfeited on missed milestones) all now make the data centre carry its own connection risk. Texas must also rewrite its 4CP transmission charges by 31 December 2026, which is a dated watch item.
6. **Missing: the clearest primary evidence that minimum bills shrink the queue.** AEP Ohio went from more than 30 GW of interest to 13 GW of formal requests to 5.6 GW of new signed agreements once the tariff bit (press, citing AEP's letter of 12 February 2026).
7. **FERC's June orders carry a cost rule the piece omits**: pro forma cost recovery agreements with minimum financial commitments toward upgrades (law-firm summary). The piece covers them only as a tier.

**contracted-energised-running**

8. **Nebius's US footprint is missing.** The piece names only Vineland. Nebius's letters list US sites in New Jersey, Missouri (Kansas City and Independence, a 1.2 GW campus), Oklahoma, Alabama, Minnesota and Pennsylvania. No site-level MW is disclosed, so the piece should say so rather than imply Vineland is the US story.
9. **Nebius's connected definition differs between letters.** February 2026: "power connected into data centers"; May 2026: wired into "fully built and equipped" halls. The piece quotes only the second.
10. **CoreWeave is a cleaner contracted-to-active series than Nebius and is not used.** Four consecutive quarters, from CoreWeave's own releases: 2.9 GW against 590 MW (Q3 2025) rising to 3.7 GW against 1.5 GW (Q2 2026). Nebius has reported active power once.
11. **Microsoft's latest stated constraint is delivery, not power.** On the call of 28 October 2026 Hood blamed delayed third-party capacity and said demand still exceeds supply. Neither executive spoke of power. Any line that says Microsoft is "power-constrained" now needs the date of Nadella's podcast remark (November 2025).
12. **Abilene's on-site gas is larger than "backup only" suggests.** Crusoe's release says backup; permits reported by the press show about 360 MW of turbines permitted in 2024 and a major permit for 41 more. Primary permit documents were not opened. Also unaddressed: press reports (denied by Oracle) of a dropped 600 MW expansion.
13. **The Abilene test date is close.** The last two buildings were due in Oracle's quarter to 30 November 2026; nothing confirms delivery yet. Oracle's December results are the reading.
14. **Jane Street's CoreWeave deal has no MW, term or date.** The piece says it "fits" power-first. It is a dollar commitment for compute across multiple facilities, including Vera Rubin, which reads as renting finished, running capacity rather than buying the slow stages first. The own-site plan (100 to 200 MW, June 2026) is press only.

## 5. Two clean primary examples of the contracted-to-running gap

- **Dominion (utility side).** About 54 GW under contract in July 2026 (12.0 GW in service agreements) against a 4.8 GW billing peak in August 2026, with Dominion assuming sites mature over five years to 63% of contract. Source: Dominion to PJM, 29 September 2026.
- **CoreWeave (operator side).** 3.7 GW contracted against 1.5 GW active at 30 June 2026. In November 2025 a single late third-party building forced it to cut its revenue outlook, and its 10-Q still lists 748 MW of leased power undelivered, due between 2026 and 2028. Sources: 8-K exhibits and the 10-Q of 12 August 2026.

## 6. Could not verify

- PJM's household bill impact for 2026/27 or 2028/29 in PJM's own words (PJM gives none in its release); the PA PUC release refused connection, so utility percentages are press.
- The market monitor's January 2026 deck (US$6.5bn, 39.6% for 2027/28) and the 2025/26 63% figure: not opened, press only.
- The uncapped US$554.72 and US$776.69 figures: press citing PJM; not in the Inside Lines release.
- AEP Ohio's 85%, 12-year, three-year exit and 50% collateral terms from the PUCO order itself (bulletin confirms only the order). AEP's 12 February 2026 letter not opened.
- Indiana Michigan Power's minimum-demand percentage (80% reported, not confirmed).
- Oregon POWER Act signing date and the PUC's minimum payment levels; PGE Schedule 96 terms.
- PUCT Project 58481 final rule text and exact adoption date (18 September 2026 is my inference); per-MW security amount.
- FERC show cause orders' cost wording (read via Willkie memo only); RM26-4 final status (no final rule found).
- ERCOT's 9,042 MW approved and 3,883 MW operating (ercot.com returns 403).
- Census data-centre construction spending: third-party figures jump from US$50.7bn (April 2026) to US$96.5bn (September 2026) annualised and could not be checked against the C30 tables; not used.
- Nebius per-site MW, and any Q3 2026 figures (results 12 November 2026).
- Abilene phase two energisation date (Crusoe has given none), the on-site turbine MW in TCEQ permits, and the date of the 600 MW expansion reports.
- Microsoft call date (28 October 2026 from press; Microsoft's page title is FY27 Q1).
- The exact date and wording of Nadella's "chips sitting in inventory" remark (BG2 podcast, early November 2025).
- New York's July 2026 moratorium on 50 MW-plus data centres: seen only in CoreWeave's 10-Q.
