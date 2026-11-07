# Fact-check: america-rations-the-plug-depth.md (7 November 2026)

Adversarial check of the draft against primary sources. No em or en dashes. No share prices or valuations. No mention of Claude or AI assistance. British spelling holds; "localized", "authorize" and "utilization" appear only inside quotations. All twelve quoted claim and test sentences in the claims fold match `src/data/claims.ts` word for word. Every chart's SVG geometry matches its labels and aria-label. I checked them all by scale: ERCOT funnel, Duke, ELCC, the three events against 525 MW, the auction prices including the $554.72 ghost bar, the wholesale stack, Dominion, CoreWeave and Nebius, and the Abilene timeline. The only small slip there: the Abilene "today" line sits at about 31 October, not 7 November.

SEC EDGAR refused curl with the plain "ThePhysicalLayer research" user agent ("undeclared automated tool"), and I did not add an email address. I read the EDGAR exhibits through a fetch tool instead. ERCOT and PUCT were not tried, as instructed.

## Findings, most serious first

**1. "Every grid is writing a cheaper plug the grid may cut first" contradicts the piece's own table.**
Text (summary): "Every grid is writing a cheaper plug the grid may cut first, though no data centre yet runs on one". Body: "Every grid calls it something different".
The status table says MISO has "No cut-first tier", only a fast track for loads that bring power stations. It also says ISO New England has "Not filed", with detailed rules in 2027. MISO's LARS filing of 2 October 2026 pairs loads over 200 MW with new generation; it is not a curtailable tier (Utility Dive, 5 October 2026). The summary is the line most readers see.
Source: the piece's own table; https://utilitydive.com/news/miso-large-load-generation-study-lars-ferc/832114
Fix (summary): "Most of America's grids are writing a cheaper plug the grid may cut first, though no data centre yet runs on one". Fix (body): "Most grids now offer or are writing one, each under its own name".

**2. PJM's Interim NITS is not "in force" yet, and the 9 October notice is the transmission owners', not PJM's.**
Text (table): "In force only for loads sited beside a power station". Body: "PJM's notice of 9 October says capacity 'will not be procured' for interim customers".
FERC's rehearing order of 18 June 2026 set the rates, terms and conditions for Interim NITS. It found PJM's compliance only partial and ordered further compliance filings within 60 days. PJM filed on 17 August 2026, and FERC let the transmission owners' compliance slip to 16 November. I found no FERC order accepting the tariff text. The 9 October document is the "Notice of PJM Transmission Owners Consultation with the Members Committee". It says: "because Interim NITS is an interruptible service, capacity will not be procured on behalf of Interim NITS customers and generation capacity charges will not be assessed until such time as the Network Upgrades are in place". The second half of that sentence matters to the bill section, because interim customers would not pay capacity charges.
Source: EL25-49-002, 195 FERC ¶ 61,209 (https://www.ferc.gov/sites/default/files/2026-06/EL25-49-002_0.pdf), opening paragraphs; PJM transmission owners' notice, 9 October 2026, p. 6 (https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20261028/20261028-notice-of-pjm-transmission-owners-consultation-with-the-members-committee---informational-posting-only.pdf); PJM extension motion (ER26-1479).
Fix (table): "Ordered by FERC for loads beside a power station, December 2025 and June 2026; PJM's tariff text still awaits FERC; for all large loads, to be filed 16 November 2026". Fix (body): "PJM's transmission owners wrote on 9 October that capacity 'will not be procured' for interim customers, and that they pay no capacity charges until their upgrades are built: they get the wires early, but no power station is held ready for them." Fold: change "PJM transmission owners' notice" wording to match. It already says this, so only the body needs it.

**3. The Dominion ratio mixes two different gaps: sites not yet built, and sites that never draw their full contract.**
Text: "Even the firmest contracts, the service agreements, are two and a half times what Dominion bills." And the summary: "about 54 gigawatts of data centres under contract and bills 4.8".
The deck's figures are right: 32,473 + 9,356 + 11,997 = 53,826 MW, "Approximately 54GW of capacity under contract"; "Data center billing peak load as of August 2026 is 4.8 GW". But the same slide defines "Utilization Rate = Demand / Contract Capacity" maturing at 63%. So even a fully running site bills about 63% of its contract. Part of the 2.5 times is utilisation, not waiting. The deck also does not say whether the 54 GW counts only contracts for future energisation or also covers sites already billing. Slide 4 says its model uses "All existing load plus executed contracts for future energization". Dominion's own forecast on slide 10 is the cleaner signed-against-running number. It shows contract capacity of 11,590 MW against coincident demand of 5,075 MW in 2027, and 17,570 MW against 7,777 MW in 2030. It also excludes 19,044 MW (59%) of the engineering letters from the forecast altogether.
Source: Dominion Energy to PJM Load Analysis Subcommittee, 29 September 2026, slides 2, 4, 5, 6 and 10 (https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2026/20260929/20260929-item-5ai---dominion_energy.pdf).
Fix: "Even the firmest contracts, the service agreements, are two and a half times what Dominion bills, though a site that is fully running still bills only about 63% of its contract, on Dominion's own figures. Dominion's own forecast is the sharper reading: it leaves 19 GW of the engineering letters out altogether, and expects its data centres to draw about 7.8 GW at peak in 2030."

**4. Ride-through does not require a site to keep drawing what it drew during the dip.**
Text: "**Ride-through** is a rule that a site must stay connected through a brief voltage or frequency disturbance, and keep drawing roughly what it drew before."
PJM's proposed envelope says that below 0.9 per unit a site "May reduce P proportional to voltage drop" or "as needed". It "shall return to >90% of pre-disturbance level within 2 sec. after V returns". The rule about staying within 10% of earlier draw applies to frequency disturbances only. The later paragraph gets this right.
Source: PJM Planning Committee deck, 8 September 2026, slides 5 and 6 (https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2026/20260908/20260908-item-05---1-large-load-ride-through---presentation.pdf).
Fix: "**Ride-through** is a rule that a site must stay connected through a brief voltage or frequency disturbance. It may draw less during a deep dip, but must be back to nearly its earlier draw within seconds."

**5. AEP Ohio's queue shrinkage leaves out the 12.2 GW signed before the tariff, and it is press only.**
Text: "In Ohio, AEP had more than 30 GW of interest before the tariff. Once it applied, 13 GW became formal requests, and 5.6 GW signed under the new terms".
The same New Project Media report, citing AEP Ohio's letter of 12 February 2026, gives 12,219 MW of agreements signed before the tariff plus 5,642 MW under it, 17,861 MW in all. Read alone, "5.6 GW signed" overstates the shrinkage. The piece also calls this "the clearest evidence", but its source is trade press, not the letter.
Source: https://newprojectmedia.com/policy-aep-ohio-touts-right-sized-load-as-data-center-pipeline-shrinks-further-under-new-tariff/ (press).
Fix: "In Ohio, AEP had more than 30 GW of interest before the tariff. Once it applied, 13 GW became formal requests, and 5.6 GW signed under the new terms, on top of 12.2 GW signed before it, the trade press reported from AEP's letter to the regulator." Change "the clearest evidence" to "evidence".

**6. The wholesale cost split is published by the monitor, and the gas explanation is not in its report.**
Text: "Energy ... rose 48%, mostly with gas prices." Chart caption and fold: "The split into parts is my arithmetic from its shares and growth rates."
The monitor's table gives the parts directly. First half of 2025: energy $49.21, capacity $6.39, transmission $18.82, total $76.16. First half of 2026: energy $72.68, capacity $19.61, transmission $19.88, total $114.50. The chart already matches these to the cent, so only the attribution is wrong. The report does not attribute the energy rise to gas. Its monthly table shows energy at $155.39 per MWh in January 2026 and $82.06 in February, against $40 to $48 from March to June, and it names Winter Storm Fern.
Source: Monitoring Analytics, Market Monitor Report to the Members Committee webinar, 27 July 2026, slides 11, 12 and 15 (https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20260727-web/item-02---marketing-monitoring-report---presentation.pdf).
Fix: "Energy, the power actually used, was 63.5% of it and rose 48%, mostly in a bitter January and February." Caption: "PJM market monitor, report to the Members Committee (27 July 2026), which gives each part; the small remainder is other charges." Fix the aria-label and fold to match.

**7. FERC rejected "certain aspects", not the whole service, as an intrusion.**
Text: "It found the cut-first service appeared to be 'an impermissible intrusion on retail rate regulation'".
P 77: "We find that certain aspects of PJM's proposal appear to present an impermissible intrusion on retail rate regulation ... Therefore, we reject PJM's proposed IRAS framework." The quotes at P 94 and P 95 check.
Source: ER26-3515-000, 197 FERC ¶ 61,019 (https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/9207/20261009-er26-3515-000.pdf).
Fix: "It rejected the cut-first service, finding that parts of it appeared to be 'an impermissible intrusion on retail rate regulation'".

**8. The 525 MW is new generation and uprates, and the "seven times" compares unlike things.**
Text: "July's drop was about seven times the 525 MW of new power stations and upgrades PJM's last capacity auction added". Similar wording in the auction section.
PJM's release: "The auction cleared 525 MW UCAP of new generation and generation uprates." "Upgrades" will be read as the transmission upgrades this piece is about. 3,900/525 = 7.4, which is fine. But a momentary block of load moving to backup is not the same quantity as a year's accredited new supply. Keep it as a sense of scale.
Source: PJM release, 14 July 2026 (https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf).
Fix: "...about seven times the 525 MW of new power stations and enlarged ones that PJM's last capacity auction added, for scale". Chart label "New plant" is fine.

**9. "The grid recovered within nine minutes" overstates a narrow measure.**
Text: "PJM caught it: the grid recovered within nine minutes, inside the 30 its standard allows."
PJM's deck: "BAAL excursion recovered within 9 minutes. BAL-001-2 R2 requires recovery within 30 minutes." That is PJM's supply and demand balance limit, not the whole grid. Thousands of megawatts were still to come back.
Source: PJM deck, "July 22, 2026 Dominion Load Transfer Event", 31 July 2026, slide 3 (https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/sos/2026/20260730/20260730-item-06---july-22-dominion-load-transfer-event---presentation.pdf).
Fix: "PJM caught it: its balance of supply and demand was back inside limits within nine minutes, against the 30 its standard allows."

**10. CoreWeave's "a year earlier" is three quarters earlier.**
Text: "about 41%, up from 20% a year earlier." Fold: "about 590 MW active and 2.9 GW contracted at 30 September 2025".
590/2,900 = 20%, but 30 September 2025 is three quarters before 30 June 2026. A year earlier, at 30 June 2025, CoreWeave reported about 470 MW active and 2.2 GW contracted, about 21%.
Source: CoreWeave Q2 2025 release (https://www.sec.gov/Archives/edgar/data/1769628/000176962825000039/coreweave2q25earningspress.htm) and Q2 2026 release, 11 August 2026 ("Expanded active power by nearly 500 MWs to reach 1.5 GW"; "approximately 3.7 GW").
Fix: "about 41%, up from about 21% a year earlier". Fold: "about 470 MW active and 2.2 GW contracted at 30 June 2025".

**11. AEP's 84 GW is incremental contracted load.**
Text: "expects 84 GW of contracted load by 2031".
AEP: "AEP's incremental contracted load is expected to grow to 84 GW by 2031", counted only if backed by "fully executed electric service agreements" or "letters of agreement". 15 GW in the third quarter checks, as do "11 states".
Source: AEP 8-K exhibit 99.1, 28 October 2026 (https://www.sec.gov/Archives/edgar/data/4904/000000490426000069/a3q20268kpressreleaseex991.htm).
Fix: "expects 84 GW of additional contracted load by 2031".

**12. Source labels: the 28 October deck is the Markets and Reliability Committee's, and "already running" is NERC's working group.**
Illustration caption and fold: "PJM's Members Committee deck (28 October 2026)". The file sits under committees/mrc and its cover reads "MRC, October 28, 2026". The table, dates, 50 and 25 MW, 90 days and "limited exceptions when demonstrated that requirements cannot be met" all check. Text: "PJM notes that every such event so far has involved sites already running". On PJM's 6 October slide 13 this sits under "Draft LLWG Recommendations", NERC's Large Loads Working Group, as presented by PJM.
Source: https://www.pjm.com/-/media/DotCom/committees-groups/committees/mrc/2026/20261028/20261028-item-06---large-load-show-cause-response---presentation.pdf ; PJM Planning Committee deck, 6 October 2026 (https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2026/20261006/20261006-item-07-a---1-lcl-ride-through-requirements-background---presentation.pdf).
Fix: "PJM's Markets and Reliability Committee deck (28 October 2026)" in the caption and fold. "NERC's large-load working group notes, in a draft PJM presented, that every such event so far has involved sites already running."

**13. The Oracle sentence conflates Oracle's lease payments with its customers' payments.**
Text: "At 31 August 2026 it had US$288 billion of data centre leases signed but not yet started ... Its customers pay when halls are delivered, not when leases are signed."
The $288bn is what Oracle will pay its landlords. The 10-Q does not say when Oracle's customers pay. The second sentence is a fair inference, but it is not in the filing. Oracle's remaining performance obligations were "$664 billion as of August 31, 2026, of which we expect to recognize approximately 13% as revenues over the next twelve months". That is the customer-side figure, and it makes the same point from a primary source.
Source: Oracle 10-Q, 11 September 2026 (https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm).
Fix: "...beginning between late 2026 and 2029. On the other side, its customers have signed US$664 billion of future revenue, of which Oracle expects only about 13% in the next twelve months, because revenue starts as halls are delivered."

**14. "PJM's new yearly process" appears in the tests but nowhere in the body.**
Text (What would prove me wrong): "if makers add factories fast enough and PJM's new yearly process works". The MRC deck describes it: a single 12-month process for generation, transmission service and large loads, with four months of screening, seven months of study and one month to finalise agreements.
Fix: add one sentence where FERC's 60 to 90 day study target appears: "PJM's answer, to be filed on 16 November, is one yearly 12-month process for power stations and large loads alike: four months of screening, seven of study and one to sign."

**15. The market monitor "argued", it did not "find" a fact FERC accepted, and the split by zone is worth a line.**
Text: "PJM's independent market monitor found by 21 September 2026 that 4,017 MW ... had been cancelled or delayed".
FERC recounts this as the monitor's argument ("The Market Monitor asserts ..."). 42% of the 9,481 MW increase checks, as does 3,055 MW. FERC adds: "of this 4,017 MW, the Dominion Electric Distributor accounts for 51%, while the AEP-Ohio Electric Distributor accounts for 29%". That links straight to the Dominion section.
Source: ER26-3380-000, 29 September 2026, p. 45 (https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/9154/20260929-er26-3380-000.pdf).
Fix: "PJM's independent market monitor argued that by 21 September 2026, 4,017 MW ... had been cancelled or delayed, half of it in Dominion's zone."

**16. "As PJM's risk moves to long winter nights" is not in the source.**
Text: "and the gap is widening as PJM's risk moves to long winter nights."
The ELCC ratings document gives the numbers (91, 90, 84; 59, 57, 42, all confirmed) but no reason.
Fix: "and on PJM's own projections the gap widens." Or source the winter-risk reason from a PJM document.

**17. Microsoft: the finance chief was explaining lower capital spending.**
Text: "On 28 October 2026 its finance chief blamed something else: 'some third-party capacity deliveries we expected in Q1 were delayed'."
Full sentence: "Capital expenditures were $45.2 billion, as some third-party capacity deliveries we expected in Q1 were delayed." The quote and date check. The transcript has no use of "power", in the sense of electricity, by either executive.
Source: https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1
Fix: "On 28 October 2026 its finance chief explained lower spending another way: 'some third-party capacity deliveries we expected in Q1 were delayed'."

**18. The Nebius definition of active power: wording to confirm.**
Text: Nebius defines active power as "power being consumed by installed, operational IT equipment and available for revenue generation".
The 12 February 2026 letter says "active power, or power being consumed by IT equipment". I could not find the longer wording, which may be in the 13 May letter. The Microsoft quote checks against the 6-K of 8 September 2025: "Subject to the satisfaction of the deployment and availability of the GPU Services", with "liquidated damages for late delivery". The 12 August letter adds: "we've delivered all capacity tranches to Microsoft under the contract". That is worth a clause, since it means the Microsoft revenue is no longer waiting on stages.
Fix: keep the long definition only if the 13 May letter carries it; otherwise use the February wording. Optionally add "and Nebius said in August it had delivered every tranche."

**19. Oncor's 24 GW is large load, not only data centres.**
Text: "about 293 GW of them from data centres. Of those, ERCOT had classified about 24 GW as base load".
Oncor: "approximately 24 GW of large load has been classified as base load including 10 GW of already energized load ... 21 GW has been classified as studied load". It also says "final load classifications are subject to change". The 795 requests, 293 GW, the audit wording and "fall of 2027" all check.
Source: Oncor 8-K exhibit 99.1, 5 November 2026 (https://www.sec.gov/Archives/edgar/data/1193311/000119312526448721/d159004dex991.htm).
Fix: "Of all its large loads, ERCOT had classified about 24 GW as base load..."

**20. Virginia's Tier 4 rule applies to permit applications from 1 July 2026, and it is law-firm sourced.**
Text: "from 1 July 2026 every new data centre generator needs controls equal to the strictest federal tier, Tier 4."
Fix: "from 1 July 2026 every new permit application for data centre generators must meet controls equal to the strictest federal tier, Tier 4, law firms report."

**21. House rules: three phrases read like an investment view.**
"If the claim is right, four positions gain." "Eventually is the whole trade". "that is where I would look for a gap". None names a share, but "positions", "trade" and "look for a gap" read as trading advice in a piece that must carry no view on shares.
Fix: "If the claim is right, four kinds of business gain." "Eventually is the whole question". "Almost nobody discloses which plug they bought, and that is the gap in what investors can see."

**22. Is "no data centre runs on a cut-first tier" still true on 7 November 2026? Yes, on everything I could find.**
I found no executed CHILLS agreement and no CHILLS customer named by SPP, FERC or the press. I found no FERC order accepting PJM's Interim NITS tariff text, and nothing showing ERCOT's PCLR implemented in its systems. CAISO, NYISO and ISO-NE have filed nothing yet. The sentence "Not that any primary record shows" is properly hedged. One caution for the table: SPP's "for up to seven years" is a bridge period, after which CHILLS eligibility lapses if firm service is not completed (press reading of the order). The piece's 2033 sentence is already marked as my reading.

## Things a portfolio manager would ask that the piece leaves out

- **Who pays the cut-first customer's capacity bill?** Interim NITS customers pay the transmission rate but no generation capacity charge until upgrades are built (finding 2). That is both a reason developers may take it and a cost moved elsewhere.
- **Dominion's own forecast** (finding 3): 7.8 GW of data centre demand in 2030 and 19.5 GW in 2047, against about 54 GW signed. The deck also says Dominion's market is "mainly cloud/AI inference", which bears on the training-swing paragraph.
- **Where the cancellations are**: half of the monitor's 4,017 MW is in Dominion's zone and 29% in AEP Ohio (finding 15). These are the two utilities the piece uses as examples of signed load.
- **Texas's own signed-against-running gap**: ERCOT's March 2026 report reportedly showed 9,042 MW approved to energise against 3,883 MW operating. This is press only, because ercot.com blocks automated fetches, but it is the Texas version of the Dominion chart.
- **Abilene's on-site gas** is larger than "backup" suggests: about 360 MW of turbines permitted in 2024, and a later permit for 41 more (press). Also the reported, and denied, dropped 600 MW expansion.
- **What ride-through compliance costs**: the piece concedes nobody has published it. A PM will also ask whether PJM's "limited exceptions" could hollow it out for legacy sites, and whether NERC's registration (68 GW) brings penalties.
- **New York**: CoreWeave's 10-Q cites a July 2026 moratorium on data centres of 50 MW or more in New York. That is relevant to the NYISO row, but I saw it only in CoreWeave's description.

## Confirmed against primary sources

- FERC EL26-67 (18 June 2026): "appears to be unjust, unreasonable, or unduly discriminatory or preferential"; "Requests to physically interconnect loads are submitted to transmission owners, who have their own study processes and requirements"; "should take no more than 60-90 days" (the source reads "60-90 days calendar days"); "may only take 1-2 years to construct" (comment quoted in fn., about new large loads); the preliminary definition of 50 MW, above 69 kV, not co-located; the four areas; DOE ANOPR of 23 October 2025 (fn. 5); CHILLS order 195 FERC ¶ 61,196 (fn. 1).
- FERC ER26-3515 (9 October 2026): filed 13 August; accepts only the definition and registry, effective 12 October 2026; 50 MW cumulative peak, one-mile radius; P 77, P 94 ("equivalent quantities of load growth"), P 95 ("States have a crucial role to play in this challenge by designating which retail customers must be curtailed").
- FERC ER26-3380 (29 September 2026): suspended five months to 28 February 2027; up to 15 years; target 6,831 MW adjusted downward; 6,623 MW short for 2027/28; the White House council and "the governors of all 13 PJM states" (January 2026) on cost allocation; 4,017 MW, 42%, 3,055 MW.
- PJM transmission owners' notice (9 October 2026): "a temporary, non-firm transmission service"; "capacity will not be procured on behalf of Interim NITS customers"; Fractional NITS "a firm service, based on available system capacity"; filing by 16 November 2026.
- PJM 2028/29 release (14 July 2026): $325, down 2.5% from $333.44; 6,831 MW short; 525 MW UCAP; $16.4bn; more than 67 million people; collar for four auctions, third consecutive. Planning parameters 2029/30: cap $337.83, floor $181.91, ER26-1556, requirement 158,712 MW.
- PJM decks: 22 July 2026, 07:56, 230 kV fault "following a mechanical failure", "Fault cleared properly", "no relay misoperations or stuck breakers"; about 2,900 MW then about 1,000 MW "a minute later", about 3,900 MW (3,800 MW in the 31 July deck); the first transfer "caused high voltage conditions and triggered the transfer of additional load"; 60.092 Hz; about 1.138 per unit (about 261.74 kV); ACE +3,928 MW; nine minutes against 30. 10 July 2024 about 1,500 MW; 17 February 2025 about 1,800 MW, four sags. NERC phase one "will not address the minimum voltage or frequency ride-through"; a minimum "expected to become part of a Reliability Standard in 2027"; registration at 50 MW and 100 kV.
- PJM ride-through (28 October MRC and 8 September PC decks): the full voltage and frequency tables; 50 MW with 25 MW through power electronics; 16 January 2027 (filing date plus 61 days); legacy sites by the later of 16 January 2028 or a year after operation; 90 days; limited exceptions; 90% within two seconds; ramp-rate filing in Q2 2027; Dominion six reclosing attempts of 50 to 70 ms; ERCOT exemption for sites operational, approved or signed by 14 November 2025, and the 0.5 to 0.8 band fully enforced from 1 January 2028 (as PJM summarised NOGRR 282).
- NERC incident review (January 2025): lightning arrester; three reclose attempts at each end; six faults in 82 seconds; 42 to 66 ms; 0.25 to 0.40 per unit; "exclusively data center-type load"; three disturbances in one minute; about 1,260 MW "did not return for hours".
- Market monitor (27 July 2026): $6.3bn, 38.2%; $29.4bn, 46.2%; $114.50 against $76.16, +50.3%; energy 63.5%, +47.7%; capacity 17.1%, +207.1%; transmission 17.4%, +5.6%; $11.11, 9.7%, from $103.40.
- PJM ELCC ratings: demand response 91, 90, 84; four-hour storage 59, 57, 42; 2030/31 non-binding.
- Dominion to PJM (29 September 2026): 32,473, 9,356 and 11,997 MW as of July 2026; 4.8 GW billing peak as of August 2026; five years to 63%; engineering letters non-firm, 59% excluded.
- Virginia SCC final order PUR-2025-00058 (25 November 2025), pp. 23 to 26: every GS-5 term in the table, including the exclusion of PJM capacity expense from the generation minimum.
- Texas Governor (3 August 2026): "approximately over 474 gigawatts", "more than five times Texas' record peak", about 90% data centres. ERCOT record 91.1 GW on 22 July 2026 (EIA; ERCOT's unofficial 91,134 MW); 474/91.1 = 5.2; 6.6/474 is under a seventieth.
- Oncor 8-K (5 November 2026): 795 requests, about 293 GW from data centres, 24 GW base including 10 GW energised, 21 GW studied, conditional on the December audit, final plan "not ... until fall of 2027".
- AEP 8-K (28 October 2026): 15 GW signed in Q3, 84 GW by 2031, executed agreements or letters only, 11 states.
- CoreWeave (11 August 2026): 1.5 GW active, about 3.7 GW contracted; 41% is right.
- Nebius: 12 February 2026 letter, "800 MW to 1 GW of connected power by the end of 2026" and "~170MW of active power"; 12 August letter, 5 GW contracted by end 2026, about 70% of deals with prepayments; 6-K of 8 September 2025, the $17.4bn and the deployment condition.
- DTE 8-K (28 September 2026): Google 1.0 GW; up to 1,600 MW renewables, 480 MW storage, 350 MW demand response (the 8-K does not name Van Buren Township).
- Google blog (19 March 2026): 1 GW with I&M, TVA, Entergy Arkansas, Minnesota Power and DTE; "limit or shift a portion of machine learning (ML) workloads".
- EPA letter to NRG (24 June 2026): PJM is the local balancing authority; dispatch passed on without change; 40 CFR 63.6640(f)(4)(ii) 50 hours.
- Nvidia (16 September 2026): AI Energy Management Alliance, founded by Emerald AI, Google and Nvidia; "faster, risk-adjusted pathways for customers that make credible and verifiable flexibility commitments". The count of "18 others" is not on that page.
- LBNL Queued Up 2025: about 2,290 GW; the typical project built in 2024 took 55 months; generators and storage only.
- Microsoft FY27 Q1 call, 28 October 2026: the Hood quote, and no remark on electric power.
- Crusoe: the first two Abilene buildings operational on 30 September 2025 (Crusoe announcement, as reported).

## Could not verify

- ERCOT and PUCT documents (not fetched, as instructed): 205 GW eligible (29 July); 17 loads and 6,608 MW (20 August); the 75 MW pause; 10 December report; PCLR approval on 18 June 2026 and its 2027 implementation; NOGRR 282 approval on 9 July and 1 August effect, from ERCOT's own text.
- Duke Nicholas Institute report text: 76, 98 and 126 GW; 85, 177 and 366 hours; 88%; about two hours. The piece already says it could not open the report.
- Oracle 10-Q lease note ($288bn, "substantially all", Q2 FY2027 to FY2029). The fetch truncated before the note; the research file records it as read in primary form today.
- Nebius 13 May 2026 letter and the long definition of active power.
- CAISO Key Statistics October 2026 (17,285 MW): the PDF is image-based. CAISO DMM $35 and $9; the evening count of 0, 10, 52 and 66, which is the author's own.
- The uncapped $554.72 (APPA from PJM's figures, as the piece says); the collar extension order of 28 April 2026 (planning parameters confirm docket ER26-1556); the PJM Board decision wording of 27 July 2026; the refiled backstop of 29 October.
- CHILLS effective date of 1 July 2026, the generation condition, and the absence of an hours cap; the CAISO board vote of 28 October; NYISO timing; MISO LARS.
- NERC final ballot in October, the registry petition (68 GW, comments by 20 November), and FERC RD26-7 itself (cited in PJM decks).
- Indiana IURC Cause 46276 order and its quoted testimony; the Michigan PSC approval text and the Attorney General's rehearing petition; Pennsylvania PUC June increases; JLARC $14 to $37.
- Virginia HB 507 and DEQ APG-576; AEP Ohio, Georgia, Indiana Michigan Power and Oregon terms (Georgia's 15 years and 100 MW are primary in the research file).
- Phoenix trial details beyond the arXiv abstract; the Choukse paper and Nvidia GB300 blog (primary in the research file, not re-read).
- Jane Street on the Dwarkesh Patel podcast (21 May 2026), including "six months sooner"; Nadella on BG2 (November 2025, as reported).
- Oracle's 42%, 618 MW and six of eight buildings (Motley Fool transcripts, as the piece says); Crusoe's "energised within a year" and "complete by end 2026"; the first GB200 racks in June 2025.
- Dominion's description of what each letter pays for. The deck names the three contracts but does not describe them.
