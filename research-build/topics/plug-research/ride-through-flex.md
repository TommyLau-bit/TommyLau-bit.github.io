# Ride-through and flexibility: research for the rebuild of "America rations the plug"

Gathered 7 November 2026 for the depth rebuild. Read-only research; nothing on the site changed.
Tags: **primary** = I read the regulator's, grid operator's, statute's or company's own document; **primary (indexed)** = the primary document exists at the URL but I read it through search snippets or a summary, not the full text; **press** = trade press or law-firm summary; **calc** = my arithmetic.

---

## 1. Plain-English explainers (for the top layer)

### Ride-through: why a data centre drops off the grid when nothing is broken

- **Normal voltage and the dip.** Every grid line runs at a set voltage (here 230 kV, or 230,000 volts). When a line is struck, a tree touches it or a part fails, current rushes to the ground. That is a **fault**. While it lasts, voltage across the whole area **sags**: in July 2024 it fell to between a quarter and two fifths of normal near the fault.
- **Fault clearing.** Protection relays sense the fault and open breakers at both ends of the line within a few hundredths of a second (42 to 66 milliseconds in 2024, 5.9 cycles or 0.098 s in 2025). That is a "normally cleared fault": the grid did its job. Many lines then **reclose** automatically, trying the line again in case the fault was brief. If it is still there, each retry is another dip.
- **What the data centre does.** Servers cannot tolerate even a short sag, so each site has a **UPS** (uninterruptible power supply): batteries behind power electronics that take over the load in milliseconds. A **static UPS** hands the load back to the grid once voltage returns. A **rotary (DRUPS)** unit uses a flywheel, starts its diesel engine and usually stays off the grid until staff switch it back by hand. Many sites also run a **counting rule**: typically three dips within one minute and the site moves to its generators and stays there until manually reconnected.
- **Why they drop in blocks.** Every site in the area sees the same dip at the same moment and follows similar settings, so hundreds or thousands of megawatts leave together. No single site misbehaved. With load gone and generators still running, frequency rises and voltage overshoots (to 1.138 times normal in July 2026), and the high voltage can trip a second wave of sites (about 1,000 MW a minute later in July 2026). Operators must then pull back generation and switch out capacitor banks, and later manage thousands of megawatts coming back.
- **Ride-through** is a rule that a site must stay connected, and keep drawing roughly the power it drew before, for a set time at each depth of dip: in PJM's proposal a quarter of a second below half voltage, half a second between half and 80%, two seconds between 80% and 90%, and continuously between 90% and 110%. The UPS may still carry the servers internally, but the site must not open its breaker to the grid or jump to generators, and it must recover to 90% of its prior draw within two seconds of voltage returning.

### Curtailment: what "flexible" or "cut-first" load means in hours

- **Curtailment** is the grid (or the utility) telling a customer to reduce its draw for a period, for pay or as a condition of service. **Demand response** is the paid, programmed version. **Firm service** is the promise not to do this short of an emergency.
- A data centre can deliver a cut in three ways: slow or pause its computing (software, as in Google's machine-learning demand response and Emerald AI's trials); run its own backup (generators or batteries) while keeping the servers on; or shed whole halls.
- **The headroom idea.** Duke's Nicholas Institute calculated how much new load existing grids could take if that load agreed to be cut in the rare hours when the system is tight. Its answer: about 76 GW if the new load gives up 0.25% of its yearly energy, 98 GW at 0.5%, 126 GW at 1%. In hours: 85, 177 and 366 hours a year, and in 88% of those hours at least half the new load stays on. So "flexible" in that study means a partial cut lasting about two hours, tens of times a year, not a full shutdown.
- **The catch for generators.** If the cut is delivered by diesel generators, the air permit, not the grid contract, may set the maximum: federally 50 non-emergency hours a year for emergency engines, and only when dispatched for local reliability.

---

## 2. Fact tables

### 2a. PJM's large load transfer events (customer-initiated load reductions, CILR)

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| Event 1: data centre load moved to backup after a normally cleared 230 kV fault | about 1,500 MW | 10 Jul 2024, about 19:00 ET | NERC Incident Review "Considering Simultaneous Voltage-Sensitive Load Reductions" (Jan 2025) https://nerc.com/pa/rrm/ea/Documents/Incident_Review_Large_Load_Loss.pdf ; PJM PC deck 6 Oct 2026 (below) | primary |
| Event 1 cause | lightning arrester failure; three auto-reclose attempts at each end; six faults in 82 seconds; fault durations 42 to 66 ms; voltage 0.25 to 0.40 pu in the area | 10 Jul 2024 | NERC incident review | primary |
| Event 1: load "exclusively data center-type"; none disconnected by utility equipment, all by customer protection and controls | 1,500 MW | 10 Jul 2024 | NERC incident review | primary |
| Event 1: most sustained loss came on the third dip (third reclose); "did not return for hours" | about 1,260 MW | 10 Jul 2024 | NERC incident review | primary |
| Event 1: frequency high 60.047 Hz, back to 60.0 in about 4 minutes; voltage peaked 1.07 pu; operators removed shunt capacitors | | 10 Jul 2024 | NERC incident review | primary |
| Counting scheme: typical trigger three voltage disturbances within one minute; load stays on backup until manually reconnected | 3 dips / 1 min | Jan 2025 | NERC incident review | primary |
| UPS types: centralised static UPS typically 2 to 5 MW each; rack-level UPS 3 to 4 kW; DRUPS (flywheel plus diesel) usually returns to grid manually | | Jan 2025 | NERC incident review | primary |
| Event 2 | **about 1,800 MW** (PJM's Oct 2026 deck); earlier PJM materials and Inside Lines said about 1,500 MW | 17 Feb 2025 | PJM Planning Committee, "PJM LCL Operational Review", 6 Oct 2026, slide 5 and 7 https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2026/20261006/20261006-item-07-a---1-lcl-ride-through-requirements-background---presentation.pdf | primary |
| Event 2 cause | sustained single line-to-ground 230 kV fault; one end locked out, other completed reclosing; four voltage sags; clearing 5.9 cycles (0.0983 s); frequency about 60.042 Hz; voltage about 1.05 pu | 17 Feb 2025 | PJM PC deck 6 Oct 2026 | primary |
| Event 3 | about 3,800 MW (SOS 30/31 Jul and OC 6 Aug decks); **about 3,900 MW** in PJM's later PC deck; "largest CILR event to date" | 22 Jul 2026, 07:56 | PJM SOS deck (dated 31 Jul 2026 on slide) https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/sos/2026/20260730/20260730-item-06---july-22-dominion-load-transfer-event---presentation.pdf ; PJM PC deck 6 Oct 2026 | primary |
| Event 3 stages | about 2,900 MW at once, then about 1,000 MW "a minute later"; the first transfer raised voltage and triggered the second | 22 Jul 2026 | PJM PC deck 6 Oct 2026 slide 8; SOS deck slide 3 | primary |
| Event 3 cause | 230 kV line fault after a mechanical failure; fault cleared properly; no relay misoperations or stuck breakers | 22 Jul 2026 | PJM SOS deck; PC deck | primary |
| Event 3 grid impact | reporting ACE +3,928 MW; Eastern Interconnection frequency 60.092 Hz; peak voltage about 1.138 pu (about 261.74 kV); 655 rate-of-change alarms and 428 frequency alarms; BAAL excursion recovered within 9 minutes (standard allows 30) | 22 Jul 2026 | PJM PC deck 6 Oct 2026 slide 9; SOS deck slide 3 | primary |
| NERC CEO letter: PJM event "at more than 3 GW, it was the largest seen to date" | >3 GW | 13 Aug 2026 | NERC, Jim Robb letter https://www.nerc.com/globalassets/who-we-are/news/2026/08/august-13-2026-ceo-letter.pdf | primary |
| PJM LLWG note: "all observed CILR events have involved already operational facilities" (argument for making existing sites comply) | | 6 Oct 2026 | PJM PC deck 6 Oct 2026 slide 13 | primary |
| NERC 2026 State of Reliability: data centre load reductions over 1,000 MW in 2025 (count differs by source: "several" vs two) | | Jun/Jul 2026 | Data Center Knowledge; mgrid.org summary | press |
| 3,900 MW is about 7.4 times the 525 MW of new plant and uprates cleared in the 2028/29 auction (3,800 MW gives 7.2) | | | | calc |

### 2b. NERC: alerts, standards, registration

| Fact | Figure / detail | Date | Source | Tag |
|---|---|---|---|---|
| NERC Large Loads Task Force formed | | Aug 2024 (task force); later renamed Large Loads Working Group | NERC primer https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/primer-for-computational-loads.pdf | primary |
| White paper "Characteristics and Risks of Emerging Large Loads" (rapid demand swings, cyclical ramping, stability risk) | | Jul 2025 | Cited in PJM PC deck 6 Oct 2026; NERC Level 2 alert | primary (indexed) |
| Level 2 alert "Large Load Interconnection, Study, Commissioning, and Operations"; acknowledge by 16 Sep 2025, report by 28 Jan 2026 | | Sep 2025 | PJM compliance updates; NERC Level 2 PDF https://www.nerc.com/pa/rrm/bpsa/Alerts%20DL/NERC%20Alert%20Level%202%20%20Large%20Loads.pdf | primary (indexed) |
| Level 2 responses: entities "generally did not have sufficient processes, procedures, or methods" for computational loads | | May 2026 | Level 3 alert text | primary |
| White paper on gaps in existing practices and standards | | Mar 2026 | PJM PC deck 6 Oct 2026 | primary |
| Level 3 alert (Essential Actions), Computational Load Modeling, Studies, Instrumentation, Commissioning, Operations, Protection and Control; acknowledge by 11 May, report by 3 Aug 2026 | seven essential actions | 4 May 2026 | https://www.nerc.com/globalassets/programs/bpsa/alerts/level-3-computational-load-alert.pdf | primary |
| Level 3 alert "does not create a mandatory obligation"; no penalties | | 4 May 2026 | Level 3 alert p.2 | primary |
| Level 3 alert includes facility-level "ride-through" performance and behaviour "during power oscillations" among items to study | | 4 May 2026 | Level 3 alert | primary |
| Reliability Guideline: Risk Mitigation for Emerging Large Loads (voluntary) | | May 2026 (approved 30 Apr per press) | NERC primer | primary |
| NERC Project 2026-02 Computational Loads launched; SAR posted 1 Apr; drafting approved 20 May 2026 | | 16 Mar 2026 | NERC primer | primary |
| FERC order directing NERC to file computational load standards and registry criteria by 31 Dec 2026, workplan by 1 Mar 2027 | RD26-7-000, 196 FERC ¶ 61,031 | 16 Jul 2026 | Sidecar (FERC order); PJM decks cite RD26-7-000 | primary |
| Standards in Project 2026-02: CLO-001-1 (interconnection, studies, commissioning, modelling data), CLO-002-1 (operational data and communications), CLO-003-1 (protection coordination and disturbance monitoring), plus FAC-001/FAC-002 revisions | | 2026 | PJM PC deck 6 Oct 2026 slide 12; POWER | primary |
| **Phase 1 "will not address the minimum voltage or frequency ride-through"**; CLO-001-1 collects ride-through *data* only | | 31 Jul 2026 | PJM SOS deck slide 12 | primary |
| NERC LLWG white paper "Large Load Disturbance Performance" defining a minimum ride-through floor; posted for comment 30 Jul; final expected Dec 2026; "expected to become part of a Reliability Standard in 2027" | | 2026 to 2027 | PJM SOS deck slide 14; PC deck 6 Oct slide 11 | primary |
| Final ballot passed | | announced 15 Oct 2026 | POWER, Utility Dive | press |
| NERC board adoption of the standards | | 26 Oct 2026 | American Public Power Association | press (not confirmed on NERC's site) |
| Board approved Rules of Procedure changes creating Computational Load Owner (CLO) and Operator (CLOP) registration | | 8 Oct 2026 | POWER | press |
| Registration threshold: 50 MW or more total connected load at 100 kV or more (draft in April was 20 MW at 60 kV with over 1 MW of IT load) | 50 MW / 100 kV | final 2026; draft Apr 2026 | PJM SOS deck slide 13; Level 3 alert footnote 1 (draft) | primary |
| NERC petition to FERC to approve registry criteria expeditiously; comments due 20 Nov 2026 | captures about 68,288 MW, about 86% of projected computational load at end-2027 | filed 21 Oct 2026 | DWT summary https://www.dwt.com/blogs/energy--environmental-law-blog/2026/11/nerc-data-center-registration-ferc-petition | press (of primary) |
| NERC: proposed obligations would not convert firm service into interruptible service | | 2026 | APPA summary | press |

### 2c. PJM's ride-through proposal

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| LCL defined: 50 MW or more with at least 25 MW served through power electronic conversion | 50 / 25 MW | 6 Oct and 28 Oct 2026 | PJM MRC deck 28 Oct 2026 https://www.pjm.com/-/media/DotCom/committees-groups/committees/mrc/2026/20261028/20261028-item-06---large-load-show-cause-response---presentation.pdf | primary |
| Voltage table: >1.20 pu may trip; 1.10 to 1.20: 1.0 s; 0.90 to 1.10: continuous; 0.80 to 0.90: 2.0 s; 0.50 to 0.80: 0.5 s; <0.50: 0.25 s | | 28 Oct 2026 | PJM MRC deck slide 6 | primary |
| Frequency: 58.8 to 61.2 Hz continuous; 57.0 to 58.8 and 61.2 to 61.8 Hz for 299 s; keep power within 10% of pre-disturbance | | 28 Oct 2026 | PJM MRC deck; PC deck 8 Sep 2026 | primary |
| Recovery: back above 90% of pre-disturbance power within 2 s of voltage returning; cooling load may trip below 0.35 pu; overcurrent capped at 150% of normal maximum | | 8 Sep 2026 | PJM PC deck 8 Sep 2026 https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2026/20260908/20260908-item-05---1-large-load-ride-through---presentation.pdf | primary |
| New projects comply from 16 Jan 2027 (filing date plus 61 days); legacy sites by later of 16 Jan 2028 or COD plus one year; PJM may accelerate to 90 days for risky sites; limited exceptions "when demonstrated that requirements cannot be met" | | 28 Oct 2026 | PJM MRC deck slide 6 | primary |
| FERC filing date | 16 Nov 2026 (target; not yet filed at 7 Nov) | | PJM MRC deck slide 5 | primary |
| Ramp-rate filing Q2 2027; design-envelope filing Q4 2027 | | | PJM MRC deck slide 7 | primary |
| Utility rules already in PJM: Dominion requires ride-through of at least six reclosing attempts of 50 to 70 ms; AEP two consecutive excursions outside 0.92 to 1.05 pu | | 8 Sep 2026 | PJM PC deck 8 Sep 2026 slide 15 | primary |
| PJM's LLWG recommends ERCOT's envelope as the minimum baseline | | 6 Oct 2026 | PJM PC deck 6 Oct slide 13 | primary |

### 2d. ERCOT ride-through and Texas SB 6

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| NOGRR 282 (Large Electronic, later Computational, Load ride-through): TAC 29 Apr, Board 2 Jun, PUCT approved 9 Jul 2026, effective 1 Aug 2026 | | 2026 | ERCOT PUCT report https://www.ercot.com/files/docs/2026/07/11/282NOGRR-45-PUCT-Report-070926.docx ; issue page https://www.ercot.com/mktrules/issues/NOGRR282 | primary (indexed) |
| Exempt: sites operational or approved to energise on or before 14 Nov 2025, or with signed interconnection agreement before then | | | PJM PC deck 8 Sep 2026 slide 10 (summarising NOGRR 282) | primary |
| ERCOT band 0.5 to 0.8 pu fully enforced from 1 Jan 2028 | | | PJM PC deck 8 Sep 2026 slide 10 | primary |
| ERCOT over-frequency ride-through stricter, under-frequency looser than MISO and IEEE 2800 | | | PJM PC deck 8 Sep 2026 slide 16 | primary |
| SB 6: loads interconnected after 31 Dec 2025 at transmission voltage must have equipment so they can be curtailed during firm load shed | | 2025 | SB 6 enrolled text, PURA 39.170(a) https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm | primary |
| SB 6: large loads must disclose on-site backup able to serve at least 50% of on-site demand; ERCOT may direct them to deploy backup or curtail in an energy emergency | 50% | 2025 | SB 6 text, PURA 37.0561(e) | primary |
| SB 6: this "does not authorize or require a violation of any emissions limitation in state or federal law" | | 2025 | SB 6 text | primary |
| SB 6: competitively procured demand reduction service for loads of 75 MW or more, 24-hour notice, stay curtailed for the whole EEA event; price-responsive loads excluded | 75 MW | 2025 | SB 6 text, PURA 39.170(b) | primary |

### 2e. Load swings from AI training (oscillation)

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| Synchronous training alternates compute-heavy and communication-heavy phases, so power swings; amplitude grows with job size; swing frequencies could damage grid equipment if they align with critical utility frequencies | | 20 Aug 2025 (v2 21 Aug) | Choukse et al., "Power Stabilization for AI Training Datacenters", arXiv:2508.14318 (Microsoft, Nvidia, OpenAI authors) https://arxiv.org/abs/2508.14318v2 | primary |
| Nvidia GB300 NVL72 power shelf: 65 joules of storage per GPU (capacitors); power cap ramps load up; "GPU burn" keeps drawing when work stops then tapers; peak grid demand cut 30% in a Megatron training run | 30%, 65 J/GPU | 28 Jul 2025 (updated 27 Aug) | Nvidia technical blog https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/ | primary (company) |
| Nvidia: generation can take one minute to 90 minutes to respond; "repeating power transients could cause resonance" | | 28 Jul 2025 | Nvidia blog | primary (company) |
| NERC Level 3 alert asks for computational load behaviour "during power oscillations" and expected ramp rates in MW per minute | | 4 May 2026 | Level 3 alert | primary |
| PNNL methodology for oscillations induced by large loads (RATLLE screening tool) | | 22 Sep 2026 | https://www.pnnl.gov/publications/methodology-evaluate-grid-reliability-impact-oscillations-induced-large-loads | primary (indexed) |
| NERC 2025 white paper example: a 50 MW block of a 200 MW training site ramping rapidly; forced oscillations 0.1 to 30 Hz | | Jul 2025 | Keentel, HSI summaries of NERC paper | press |
| PJM to set LCL ramp-rate rules (Q1 2027) and file Q2 2027 | | | PJM MRC deck 28 Oct 2026 | primary |

### 2f. Flexibility: Google, DTE, Duke, EPRI, Emerald

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| Google: first data centre demand response targeting ML workloads, with Indiana Michigan Power (new Fort Wayne site) and TVA; built on 2024 OPPD pilot that cut ML demand in three grid events | 3 events | 4 Aug 2025 | Google blog (Michael Terrell) https://blog.google/inside-google/infrastructure/how-were-making-data-centers-more-flexible-to-benefit-power-grids/ | primary (company) |
| Google: 1 GW of demand response in long-term contracts; utilities I&M, TVA, Entergy Arkansas, Minnesota Power, DTE; can "limit or shift a portion" of ML workloads; no hours or events stated | 1 GW | 19 Mar 2026 | https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/demand-response-data-center-milestone/ | primary (company) |
| Indiana: I&M–Google contract (clean capacity plus demand response) approved as modified; size of load, contract length, curtailment amounts and event performance kept confidential pending subdocket 46276 S1 | | order file dated 29 Apr 2026 | IURC Cause 46276 order https://secure.in.gov/iurc/files/ord_46276_042926.pdf | primary |
| Indiana: consumer witness said "the curtailment requirement represents only a small percentage of the facility's total load", leaving a net increase in I&M's peak even during events; contract includes Google participation in a PJM emergency DR offering | | 2026 | IURC Cause 46276 order (testimony summary) | primary |
| DTE: Google's 1 GW Van Buren Township ramp supported by up to 1,600 MW renewables, 480 MW storage and 350 MW demand response | 350 MW | 28 Sep 2026 | DTE 8-K (per live piece's sidecar) https://www.sec.gov/Archives/edgar/data/936340/000093634026000159/dtebusinessupdate92826fi.htm | primary (not re-read; EDGAR) |
| Michigan PSC approved DTE–Google special contracts (20 years, minimum bill 80% of contract capacity) | | 1 Oct 2026 | MPSC release https://www.michigan.gov/mpsc/commission/news-releases/2026/10/01/mpsc-approves-dte-electric-google-data-center-and-contracts-protects-customers-from-project-cost (403 to me; title and press) | primary (indexed) |
| Attorney General Nessel petitioned for rehearing | | by 30 Oct 2026 | Michigan Public, 30 Oct 2026 | press |
| Press reports a different split: 300 MW of capacity credits and 250 MW of demand response | | Mar 2026 | Crain's Detroit, via search | press (conflicts with 8-K) |
| Duke Nicholas Institute, "Rethinking Load Growth" (Norris, Profeta, Patiño-Echeverri, Cowie-Haskell), 22 largest balancing authorities, 95% of US load | 76 GW at 0.25%; 98 GW at 0.5%; 126 GW at 1% | 11 Feb 2025 | https://nicholasinstitute.duke.edu/sites/default/files/publications/rethinking-load-growth.pdf (blocked to me) | primary (indexed) |
| Duke: curtailment hours a year | 85 / 177 / 366 hours | 11 Feb 2025 | Facilities Dive; S&P | press (of primary) |
| Duke: share of curtailment hours with at least half the new load still running | 88% | 11 Feb 2025 | Facilities Dive | press (of primary) |
| Duke: average curtailment event about 1.7 to 2 hours | | 11 Feb 2025 | Nicholas Institute takeaways (via search) | press (of primary) |
| Duke at 0.5%: PJM 18 GW, MISO 15 GW, ERCOT 10 GW, SPP 10 GW, Southern 8 GW | | 11 Feb 2025 | Facilities Dive; POWER | press (of primary) |
| Phoenix trial: 256-GPU cluster in a hyperscale data centre cut power 25% for three hours during peak grid events, keeping quality of service | 25% / 3 h | arXiv 1 Jul 2025 | Emerald AI et al., arXiv:2507.00909 https://arxiv.org/abs/2507.00909 | primary (preprint) |
| Phoenix test day 3 May 2025, with Oracle (OCI), Nvidia, Salt River Project, EPRI DCFlex; 15-minute ramp down | | 3 May 2025 | Introl, Capacity Global | press |
| EPRI DCFlex expanded to nine demonstration sites (incl. Manassas, Virginia, and London) | 9 sites | Feb 2026 | EPRI / Renewable Energy World | press |
| EPRI Flex MOSAIC: classifies large-load flexibility by speed, duration, magnitude and frequency; with 65+ utilities and operators | | 23 Mar 2026 | EPRI release https://www.globenewswire.com/news-release/2026/03/23/3260463/0/en/EPRI-Launches-Flex-MOSAIC-to-Reduce-Time-to-Power-for-Data-Centers.html | primary (company release) |
| AI Energy Management Alliance (Emerald AI, Google, Nvidia + 18 others) seeks "risk-adjusted interconnection pathways" for verifiable flexibility; 100 MW "power-flexible AI factory" in Manassas, Virginia | | 16 to 17 Sep 2026 | Nvidia blog https://blogs.nvidia.com/blog/ai-energy-management-alliance/ ; SiliconANGLE | primary (company) |
| Emerald AI joins EPRI DCFlex as full member; six flexibility demonstrations to date | 6 | 2 Nov 2026 | search summary | press |
| PJM values demand response at 91% (2028/29), 90% (2029/30), 84% (2030/31, non-binding) of nameplate in its capacity market | | 2026 | PJM preliminary ELCC ratings DY2028/29 to DY2042/43 https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/preliminary-elcc-class-ratings-for-period-dy28-dy42-elcc.pdf | primary |

### 2g. Backup generators as the flex: air rules and permits

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| Federal rule: emergency engines may run up to 50 hours a year non-emergency to supply power under a financial arrangement only if dispatched by the local balancing authority or local T&D operator to avert voltage collapse or line overloads, under NERC/regional/state protocols; power only to the facility or local system | 50 h (within 100 h for maintenance and testing) | 40 CFR 63.6640(f)(4)(ii); 60.4211(f)(3)(i); 60.4243(d)(3)(i) | EPA fact sheet https://www.epa.gov/system/files/documents/2025-05/rice-memo-on-duke-energy-regulatory-interpretation-04_17_25.pdf | primary |
| Subpart ZZZZ (the NESHAP) applies only at area sources | | | EPA fact sheet footnote 1 | primary |
| EPA fact sheet and FAQ on backup generators for grid reliability, citing Duke Energy's PowerShare Mandatory 50 | | 1 May 2025 (letter 30 Apr 2025) | EPA fact sheet | primary |
| EPA letter to NRG: its PowerPay! programme, in which **PJM** is the local balancing authority and NRG passes on PJM's local transmission-emergency dispatch, meets the 50-hour criteria | 50 h | 24 Jun 2026 | https://www.epa.gov/system/files/documents/2026-08/nrg-energy-response_6-24-26.pdf | primary |
| The 2013 rule's 100-hour emergency demand response provision (EEA Level 2) was vacated by the D.C. Circuit in 2015 | | 2015 | EPA NRG letter | primary |
| EPA letter to East Kentucky Power Cooperative (residential backup programme) | | 24 Jun 2026 | https://www.epa.gov/system/files/documents/2026-08/east-kentucky-power-cooperative-response_6-24-26.pdf | primary (not read) |
| Virginia DEQ APG-576 revised: Tier 4-equivalent controls presumptive BACT for data centre generators, applications from 1 Jul 2026; DEQ expects most gen-sets to be permitted as non-emergency units | | 9 Apr 2026 | Williams Mullen; Data Center Knowledge | press (of primary) |
| Virginia HB 507 (Ch. 397, 2026 Acts; Va. Code 10.1-1322.6(B)): no air permit for a data centre application on or after 1 Jul 2026 unless each gen-set's limit is Tier 4-equivalent; regulations 9VAC5-50-610 to 630 effective 4 Nov 2026 | | 2026 | Williams Mullen | press (of primary) |
| Virginia DEQ withdrew its 2023 proposed variance letting Northern Virginia data centres run generators in grid stress | | 2023 | Virginia Mercury | press |
| Texas: emergency engines commonly permitted by TCEQ if run no more than 10% of the primary source's annual operation (30 TAC 106.511) | 10% | | E&E/secondary; rule text blocked to me | press |

### 2h. Batteries: what they are for

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| CAISO installed battery capacity (commercial units only, excludes pumped storage) | 17,285 MW | 31 Oct 2026 | CAISO Key Statistics, Oct 2026 https://www.caiso.com/documents/key-statistics-oct-2026.pdf | primary |
| CAISO installed battery capacity (previous issue) | 17,307 MW | 30 Sep 2026 | CAISO Key Statistics, Sep 2026 | primary |
| Batteries earned about $35/kW-year from energy versus $9 from regulation | | 2025 | CAISO DMM 2025 annual report (per live piece) | primary (not re-read) |
| CAISO battery discharge record about 12.99 GW, covering about 36% of demand at the evening peak | | 9 Jul 2026 | GCN; EnergyGPS | press (unverified) |
| PJM 4-hour storage capacity rating: 59% (2028/29), 57% (2029/30), 42% (2030/31 non-binding), 34% (2031/32), falling to 19% by 2042/43; 2030/31 binding ratings to be calculated Dec 2026/Jan 2027 | | 2026 | PJM preliminary ELCC ratings DY28 to DY42 | primary |
| EIA: 24 GW utility batteries planned for 2026, 12.9 GW (53%) in Texas | | 20 Feb 2026 | EIA (per live piece) | primary (not re-read) |
| UPS batteries at data centres are the ride-through equipment: they hold servers for seconds to minutes until generators start | | Jan 2025 | NERC incident review | primary |

### 2i. How many hours a cut-first load is actually cut

| Case | What is public | Source | Tag |
|---|---|---|---|
| Google–OPPD pilot | three grid events in 2024; no hours | Google blog 4 Aug 2025 | primary (company) |
| Google–I&M | hours, events and MW confidential (subdocket 46276 S1); intervenors asked for annual reporting of events and hours | IURC order Apr 2026 | primary |
| Phoenix (Emerald AI) | one event: 25% for 3 hours | arXiv 2507.00909 | primary (preprint) |
| Duke model | 85 to 366 hours a year, mostly partial, about 2-hour events | Duke 2025 | press (of primary) |
| Emergency engines | at most 50 paid non-emergency hours a year federally | 40 CFR 63.6640(f)(4)(ii) | primary |
| SB 6 large-load demand reduction service | for the whole EEA event, after 24 hours' notice | SB 6 | primary |
| SPP CHILLS, ERCOT PCLR, PJM Interim NITS | no published cap on curtailment hours found | live piece; my search | n/a |

No public record I found shows a data centre's actual curtailed hours in a year under any tier.

---

## 3. What the live piece has wrong or out of date

1. **17 February 2025 event size.** The piece says about 1,500 MW (chart, caption, text, claims record). PJM's own latest deck (Planning Committee, 6 Oct 2026, slides 5 and 7) gives **about 1,800 MW**. Earlier PJM material and Dominion said about 1,500. Fix: use PJM's 6 Oct figure (1,800 MW) or state both with dates. The chart's second bar and the caption ("PJM gives the earlier two events as about 1,500 MW each") need changing. The claim's 1,500 MW falsifier threshold is unaffected (claims are not reworded).
2. **22 July 2026 event size.** The piece says about 3,800 MW throughout. PJM's later, more detailed deck says **about 3,900 MW** (2,900 MW then about 1,000 MW a minute later). PJM's 31 July and 6 August decks said 3,800. Either keep 3,800 with "PJM later put it at about 3,900", or move to 3,900; the "two stages" wording can now carry the numbers. Note the second stage came "a minute later", which further undercuts "drop in under a second" in the 22 Sept claim (the claim wording stays; the evidence note already says it is my reading).
3. **"The holding-on rule is getting teeth" overstates NERC.** NERC's first computational load standards (CLO-001/002/003) do **not** set minimum ride-through: PJM's 31 July deck says phase 1 "will not address the minimum voltage or frequency ride-through"; CLO-001-1 only requires ride-through *data*. A ride-through floor is expected in a standard in **2027**. The binding ride-through in PJM is PJM's own tariff filing (16 Nov), and in Texas NOGRR 282. The board adoption on 26 October is still only from APPA.
4. **NERC registration.** The piece does not mention it; NERC petitioned FERC on 21 Oct 2026 to approve registry criteria (50 MW, 100 kV; about 68 GW, 86% of computational load by end-2027), comments due 20 Nov. Worth one line: data centres themselves become NERC-registered entities.
5. **ERCOT's ride-through is in force.** The evidence table says "Yes for new large computational loads"; add that NOGRR 282 was approved by the PUCT on 9 July 2026, effective 1 August 2026, with the 0.5 to 0.8 pu band fully enforced from 1 January 2028. The table's "as PJM summarised them on 8 September" can now cite ERCOT's own PUCT report.
6. **Phoenix trial source.** The piece cites "Nature Energy (5 December 2025)". I could confirm only the arXiv preprint (2507.00909, 1 July 2025) and press saying it was later published in Nature Energy. Check the Nature Energy DOI and date before keeping it.
7. **Backup engine hours: the PJM path is now open.** The piece frames the 50-hour route through Duke's programme (a local balancing authority). EPA's 24 June 2026 letter to NRG accepted a programme where **PJM** is the local balancing authority dispatching locally. So a data centre in PJM can, in principle, be paid to run its emergency engines up to 50 hours a year. Strengthens the hours section; also SB 6 says Texas's backup-generation orders do not authorise breaking emission limits, which supports "permits may set the hours".
8. **Virginia permits are tightening, not loosening.** If the rebuild mentions Virginia generators: from 1 July 2026 new data centre gen-sets need Tier 4-equivalent controls (HB 507; DEQ APG-576 revised 9 April 2026), and DEQ expects most to be permitted as non-emergency units, which could allow more run hours than emergency classification.
9. **CAISO fleet figure.** Latest is 17,285 MW at 31 October 2026 (17,307 MW at 30 September). The small fall reflects CAISO counting only fully commercial units. Update if the piece says "latest".
10. **DTE 350 MW.** Status moved: MPSC approved the contracts on 1 October 2026 and the Attorney General has petitioned for rehearing (by 30 October). Press figures (250 MW demand response, 300 MW credits) conflict with the 8-K's 350 MW; keep the 8-K figure and say how much is computing is not disclosed.
11. **Indiana.** The order is dated by file name 29 April 2026 (the piece says April 2026: fine). Add that the load size, curtailment amounts and event performance are confidential pending subdocket 46276 S1, and the consumer advocate's witness called the curtailment "a small percentage" of the site's load. That is the best primary evidence for "nobody publishes the hours".
12. **Alliance name.** The 16 September group is the "AI Energy Management Alliance" (Emerald AI, Google, Nvidia and 18 others), with a 100 MW flexible site in Manassas, Virginia. The piece's quote "credible, verifiable flexibility commitments" I did not find verbatim; press has "verifiable flexibility". Check the Nvidia blog before keeping the quotation marks.
13. **PJM demand response rating.** New, useful: PJM rates demand response at 84% for 2030/31 (non-binding) versus 4-hour storage at 42%, so a cuttable megawatt counts for more in PJM's capacity market than a battery megawatt.

## 4. Could not verify

- NERC board adoption on 26 October 2026 from NERC's own site (only APPA).
- NERC 2026 State of Reliability count of CILR events over 1,000 MW (sources say "several" or two).
- Duke report text itself (Nicholas Institute and DukeSpace block automated access): the 76/98/126 GW, 85/177/366 hours, 88% and about 2-hour figures rest on Facilities Dive, S&P and the institute's summary as indexed.
- Nature Energy publication of the Phoenix trial (title, DOI, 5 December 2025 date).
- DTE 8-K 350 MW (EDGAR not re-read this session) and the MPSC order text (403); the Van Buren case number.
- TCEQ hour limits for emergency engines (30 TAC 106.511 text blocked); any Texas data-centre-specific rule.
- Virginia DEQ's own APG-576 text (read only through law-firm summaries); exact wording "no longer appropriate".
- CAISO battery discharge record and share at the evening peak (only low-quality press); CAISO evening net peak 2026 from CAISO directly.
- Actual curtailment hours for any data centre under any cut-first tier or DR contract: none published.
- PJM ride-through filing: not filed as of 7 November (target 16 November 2026).
- SPP CHILLS curtailment-hour cap (not read).
- NERC July 2025 white paper's specific example (50 MW block of a 200 MW training site) and oscillation band (0.1 to 30 Hz): secondary summaries only.
