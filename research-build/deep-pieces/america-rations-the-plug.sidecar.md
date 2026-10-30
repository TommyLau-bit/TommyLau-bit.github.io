# Sidecar: america-rations-the-plug (deep piece, cluster 2 with cluster 6 folded in)

Revised 30 Oct 2026 after the coordinator's fact-check (7 points; see the end of this file).

Cluster 2 of CONSOLIDATION-PLAN.md, "US grid connection rules", now also absorbing cluster 6 (batteries), which Tommy approved folding in on 30 Oct 2026. Drafted 30 Oct 2026 to BRIEF-DEEP.md and the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/america-rations-the-plug.md` (draft: true), kept outside `src/content/journal/` so the loader does not read it. Nothing committed, published or scheduled. No existing file edited.

Absorbs: live `the-power-it-drops`, `what-the-battery-is-really-for`; drafts `ercot-rations-the-plug`, `ferc-asks-for-a-softer-plug`, `pjm-sends-the-bill`, `google-lets-the-grid-slow-its-chips`, `california-still-shifts-the-sun`; held `virginia-bills-the-empty-site` (only its primary facts: Dominion 10-K and 8-K, JLARC; the SCC orders, the July 2026 line extension order and Valley Link are press-only and are not used).

## URGENT for Tommy: two scheduled publishes would contradict the merge

- `ercot-rations-the-plug` is due to publish on 2 Nov 2026 (first of the 20 publish tasks, per CONSOLIDATION-PLAN.md).
- `pjm-sends-the-bill` is due on the site Mon 9 Nov 2026 (brand/linkedin-posts.md entry 35, LinkedIn Mon 7 Dec, not marked scheduled).
If this deep piece replaces them, both publish tasks need pausing or retiring before they fire. I have not touched any scheduled task.

## Shape and counts

- Title: "America rations the plug: who can be cut, and what backs them up" (11 words, sentence case), as briefed. Slug `america-rations-the-plug` (new URL).
- Top layer (cold open, analogy, How it works, The number that matters): about 480 words, 12 figures counting dates, 0 company financial figures, 0 money figures. Analogy about 78 words (two `<p>`). Average sentence about 14 words.
- Investor layer: 2,499 words before the exposure map by whitespace count, tables included. Exposure map about 127 words, three groups plus the against block, exact disclaimer pair plus the evidence sentence the prototype uses. Whole file about 3,600 words.
- `brand/check-piece.py` on a scratch copy (rerun after fixes): one FAIL only, the cover file does not exist (by design, proposal below). Warnings: sources line length (as in the prototype) and average sentence about 24 words (driven by the verbatim claim quotes and the three-sentence Virginia section).
- One spelling trap fixed: the Leo Cui video title contains the US spelling of "centres", which fails the checker, so the credit describes the video instead of quoting its title.

## Thesis

America is not speeding up the plug; it is rationing it. Firm connections still wait years for network upgrades, so ERCOT and the six FERC-regulated grids are adding a lower tier that switches on sooner but can be cut first (or requires own generation), PJM's households carry the capacity shortfall, and Virginia puts a minimum bill under the empty site. The same sites must also ride through faults, because the backup generators that protect them threw 3.8 GW at PJM on 22 July 2026. So what backs a site up (generator, battery, or slower chips) is now part of the connection.

## How the live claims are treated (Claims on record)

Both quoted word for word from `src/data/claims.ts` with their original dates (both 22 Sep 2026). Never reworded.

- `the-power-it-drops`. PJM's own account (SOS deck 31 Jul 2026; Inside Lines 11 Aug 2026) supports the second limb of the falsifier: the fault "cleared properly", no relay misoperations, third such transfer since July 2024. The first limb (ride-through cheap or not) is open; PJM's proposal would make existing sites comply by 16 Jan 2028 with limited exceptions; no published cost. **"Where I was wrong"**: the live piece says NERC's Level 3 alert "binds the planners and operators". NERC's alert text says it "does not create a mandatory obligation to take the Essential Actions" and carries no penalties; FERC's order of 16 Jul 2026 (196 FERC ¶ 61,031, RD26-7-000) binds NERC only: it must file standards and registry criteria by 31 Dec 2026 and a workplan by 1 Mar 2027; binding standards on entities come from NERC after that. Also: PJM times the event to the minute (07:56), and its deck shows two stages (the first transfer raised voltage, triggering more), so "under a second" in the claim was my reading, not a PJM figure. The live piece also sourced the event to Utility Dive (press); the deep piece uses PJM's own documents.
- `what-the-battery-is-really-for`. "Where later evidence cuts against it", carrying `california-still-shifts-the-sun`'s narrowing openly: California's 17.3 GW fleet is a time-shifter (DMM: about $35/kW-yr energy vs $9 regulation, 2025); my count of summer 2026 narrows the claim to, at most, the newest buyers beside data centres. The EIA Texas 53% is planned grid-scale additions, which also trade; nobody publishes the share at data centre sites. Nearest primary case (DTE: Google's Van Buren load ramp supported by 480 MW storage) is utility-bought supply, not a connection condition.

Draft claims: none of the six drafts ever went live, so their proposed claims are not on record and are not quoted. FERC's use test is folded into the new deep claim (with ERCOT now in scope); the others go to its watch list (ERCOT's audit, PJM auctions, Google, California, Virginia).

## claims.ts changes (existing claim text untouched)

The `Claim` type already has `date` and `home`. At merge:
- `the-power-it-drops` and `what-the-battery-is-really-for`: add `home: 'america-rations-the-plug'` only (both already carry their `date`).
- `pjm-sends-the-bill`: **decision for Tommy.** This entry in claims.ts is a never-published proposed claim: its piece never went live, and the claims page filters it out. Treat it as not on record, like the proposed `seagate-sells-the-terabyte` and water entries, and decide at merge whether to delete it or keep it unpublished. Do not give it `home: 'america-rations-the-plug'`, which would surface it on /claims as if published. Its auction test is kept as a watch item of the new claim.

New entry:

```ts
  {
    id: 'america-rations-the-plug',
    claim: 'America is rationing the grid connection rather than speeding it up: by the end of 2027, data centres of 50 megawatts or more will be running on an early-connection tier the grid may cut first in at least two of its seven organised grids, and once PJM\'s ride-through deadline for existing sites passes, its data centres will stop dropping to backup power in blocks of 1,500 megawatts or more after normally cleared faults.',
    breaksIf: 'By 31 December 2027, fewer than two of ERCOT, PJM, MISO, SPP, NYISO, ISO New England and CAISO have a load of 50 MW or more, mainly a data centre, actually energised under an early-connection tier the grid may cut first, such as ERCOT\'s Provisional Controllable Load Resource, SPP\'s CHILLS, PJM\'s Interim NITS or CAISO\'s flexible interim service, shown in a filed service agreement or the operator\'s own report; curtailment rights that apply to all large loads during emergency load shed, such as Texas Senate Bill 6, do not count. Or, between 16 January 2028 and 31 December 2028, PJM reports a transfer of 1,500 MW or more of large load to backup generation or off the grid after a normally cleared fault.',
    watch: ['Service agreements for ERCOT PCLR, SPP CHILLS, PJM Interim NITS, CAISO FILI and NYISO and ISO-NE non-firm services', 'RTO and transmission owner filings in EL26-67 to EL26-72 (November 2026) and FERC\'s orders on them', 'ERCOT\'s audit reports (due by 10 December 2026) and the date approvals to energise resume', 'PJM\'s large computational load ride-through filing (November 2026), its limited exceptions, and NERC\'s standards due 31 December 2026', 'PJM event reports of large load transfers after normally cleared faults, from 16 January 2028', 'PJM base auctions against the cap and the reliability requirement, starting with 2029/2030 in December 2026', 'Whether any connection is approved on a computing cut, including DTE\'s 350 MW tied to Google\'s Van Buren site', 'CAISO battery lead at the evening net peak, summer 2027, and PJM\'s four-hour storage rating for 2030/2031'],
  },
```

Why it is a real test: "cut-first" now means an early-connection tier, so Texas's statutory load-shed right over every large load connected after 2025 no longer clears the first limb automatically. SPP's CHILLS exists but no site is shown running on it, and CAISO's record says developers want firm service and take flexibility only temporarily, so two grids with a real site can fail. The old ERCOT firm-share limb is dropped (SB 6 made it near-impossible to fail). The ride-through limb now tests outcome, not adoption (adoption is likely and is the-power-it-drops' own watch item): PJM's earlier transfers were about 1,500 MW each (10 Jul 2024, 17 Feb 2025), so a recurrence of that size in 2028, after existing sites were due to comply by 16 Jan 2028, breaks it whatever the rule says or however its limited exceptions are used. No causal "so".

Alternatives considered: (A) PJM auction at or near cap through 2027 as the lead: the mechanism is the bill, and the collar expires after four auctions; kept as watch. (B) Batteries required as a connection condition: no primary observable. (C) "PJM adopts ride-through for operating sites": likely, and hard to define against PJM's limited-exceptions clause; replaced by the event test.

## Redirect map

| Old URL | Redirect to |
|---|---|
| /journal/the-power-it-drops/ | /journal/america-rations-the-plug/#the-power-it-drops |
| /journal/what-the-battery-is-really-for/ | /journal/america-rations-the-plug/#what-the-battery-is-really-for |
| /journal/ercot-rations-the-plug/ | /journal/america-rations-the-plug/#ercot-rations-the-plug |
| /journal/ferc-asks-for-a-softer-plug/ | /journal/america-rations-the-plug/#ferc-asks-for-a-softer-plug |
| /journal/pjm-sends-the-bill/ | /journal/america-rations-the-plug/#pjm-sends-the-bill |
| /journal/google-lets-the-grid-slow-its-chips/ | /journal/america-rations-the-plug/#google-lets-the-grid-slow-its-chips |
| /journal/california-still-shifts-the-sun/ | /journal/america-rations-the-plug/#california-still-shifts-the-sun |
| /journal/virginia-bills-the-empty-site/ | /journal/america-rations-the-plug/#virginia-bills-the-empty-site |

Only the first two were ever live and strictly need redirects (their LinkedIn posts link them). The drafts never went live; redirects are cheap insurance (the PJM post text in brand/linkedin-posts.md already holds its URL). At merge, the two live originals go verbatim into `research-build/archive/pieces/`; the six draft files leave `src/content/journal/` (archive them too, so their sidecars' verification stays traceable).

Sections and anchors, in order: The mechanism in depth; ERCOT (#ercot-rations-the-plug); FERC (#ferc-asks-for-a-softer-plug); PJM (#pjm-sends-the-bill); Virginia (#virginia-bills-the-empty-site); The power it drops (#the-power-it-drops); What backs them up: batteries (#what-the-battery-is-really-for, #california-still-shifts-the-sun); The chip as the backup (#google-lets-the-grid-slow-its-chips); Claims on record; What would prove me wrong; Research notes.

## stack.ts

Layer `grid` ("The grid connection"). The deep piece is about the terms of connection, so grid, not onsite.
- grid: replace `'the-power-it-drops', 'pjm-sends-the-bill'` with `'america-rations-the-plug'` (the prototype's sidecar proposed keeping those two; they now move here).
- onsite: remove `'what-the-battery-is-really-for'`. The onsite layer keeps the battery mention through cluster 4 if Tommy wants; `california-still-shifts-the-sun`'s sidecar already argued grid-scale batteries belong under grid.

## Glossary (src/pages/glossary.astro, "Getting power to the building")

New:
- Firm service: A connection the grid operator plans to keep supplied at all times, without a right to cut it short of an emergency.
- Non-firm service: A connection the grid may cut first when lines are strained, offered so a site can switch on before the upgrades for firm service are built.
- Network upgrades: The new lines, substations and equipment a grid operator says it must build before it can give a new site firm service.
- Show cause order: A FERC order telling a grid operator to explain why its rules are still just and reasonable, or to propose changes.
- Large load (Texas): A single site drawing 75 megawatts or more, the threshold Texas law sets for the special connection rules data centres face.
- Large computational load: In PJM's October 2026 proposal, a data centre or similar site of 50 megawatts or more with at least 25 megawatts behind power electronics, which must ride through faults; switching to backup power does not by itself count.
- Early-connection tier: A connection that lets a site switch on before its grid upgrades are built, on condition the grid may cut it first, such as ERCOT's Provisional Controllable Load Resource or PJM's Interim NITS.
- Net peak: The evening hour when demand minus wind and solar is highest, which the rest of the grid must cover. In California it arrives around 8pm.
- Four-hour battery: A battery that can run at full power for four hours before it needs recharging, the most common size of grid battery in America.
- Demand response: An agreement to use less electricity when the grid asks, usually at peak, for payment or bill credits. Google's version slows or delays its AI computing.
- Minimum demand charge: A floor on a large customer's bill, set on the demand it contracted, paid whether or not it uses that much power.
- Stranded cost: The unpaid cost of a power station or line built for a customer that leaves or never uses it, which falls on other customers unless a contract covers it.

Existing entries to update (Tommy's call; not edited):
- Ride-through: "Now being considered as a condition of connecting a large data centre" is overtaken. Suggest: "...PJM proposed in October 2026 to require it of data centres of 50 MW or more, existing ones included, and FERC has ordered NERC to file standards by the end of 2026."
- BESS: "Increasingly bought not to trade electricity prices but to let a site switch on ahead of its grid connection" restates the narrowed claim as fact. Suggest: "Battery energy storage system. Most grid batteries shift cheap power into the evening peak; some beside data centres are bought to switch on early or ride out a cut."
- Capacity auction, Reliability requirement, Large-load tariff, FERC, PJM, NERC, Grid frequency, Behind the meter: already present, no change.

## numbers.ts (physical only)

New:
```ts
  { layer: 'grid', value: '474 GW', what: 'Requests to connect to ERCOT\'s Texas grid, more than five times the state\'s record peak, about 90 per cent from data centres.', piece: 'america-rations-the-plug', asOf: '3 August 2026' },
  { layer: 'grid', value: '6,831 MW', what: 'How far PJM\'s capacity auction for 2028/2029 fell short of its own reliability requirement. New power stations and upgrades cleared only 525 MW.', piece: 'america-rations-the-plug', asOf: '14 July 2026' },
  { layer: 'grid', value: '50 MW', what: 'The size from which PJM proposes a data centre must ride through faults rather than drop to backup power, existing sites included by 2028.', piece: 'america-rations-the-plug', asOf: '6 October 2026' },
```
Existing entries needing Tommy's decision at merge:
- `3.8 GW` (the-power-it-drops): text says demand "vanished from the grid in under a second". PJM says about 3,800 MW "transferred to back-up generation", in two stages, timed to the minute. Suggest new `what`: "Data centre load in Dominion Energy's zone that switched to backup generation after a normally cleared fault on 22 July 2026, the largest load transfer in PJM's history." Repoint `piece`, add a `note`.
- `53%` (what-the-battery-is-really-for, onsite): repoint `piece`; add a `note` that it counts planned grid-scale additions, not batteries at data centre sites.

## LinkedIn post (§9; one for the deep piece, opens on its sharpest number)

```
Texas has been asked to connect over 474 gigawatts of new demand, more than five times the most power it has ever used at once.

Most of it is data centres, and America cannot build wires that fast. So its grids are rationing the connection: a firm plug that waits years for new lines, and an earlier one the grid can cut first. The same sites must now stay on through faults, after 3,800 megawatts of data centres in Dominion's Virginia zone dropped to backup power in July.

The piece covers who can be cut, who pays for the wait, and what backs the sites up: generators, batteries or slower chips.

https://thephysicallayer.fyi/journal/america-rations-the-plug/

#DataCentres #Grid #Energy
```

## Cover proposal (not drawn)

`/covers/america-rations-the-plug.svg`. One idea: a large wall socket in the centre, drawn in amber, with two plugs. The left plug is solid amber with a thick cable (firm). The right plug is half amber, half dashed outline, with a small blue switch on its cable (cut first). Behind the right plug, a small amber battery block and a blue chip square as its backup. Caption in letter-spaced grey: "AMERICA RATIONS THE PLUG". Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Needed edits to other files (not made)

- `research-build/deep-pieces/the-queue-not-the-chip.sidecar.md` proposes a grid list keeping `the-power-it-drops` and `pjm-sends-the-bill`; at merge they become `america-rations-the-plug`.
- `research-build/archive/CONSOLIDATION-PLAN.md`: cluster 6 is now part of cluster 2 (11 pieces become 10).
- `brand/linkedin-posts.md` entry 35 (PJM) is superseded by the post above; the scheduled ERCOT (2 Nov) and PJM (9 Nov) publish tasks need pausing (see top).
- The exposure maps of the two live originals name a company on the never-name list; the deep piece's map does not. Those companies' pages lose these links at merge. Company names dropped from the cluster's maps: Talen, Vistra, NRG Energy, Constellation, Exelon, FirstEnergy, PSEG, Monitoring Analytics, MISO, Southwest Power Pool, NYISO, ISO New England, CAISO, CenterPoint Energy, AEP Texas, Indiana Michigan Power, Tennessee Valley Authority, Entergy Arkansas, Minnesota Power, DTE Energy, Oracle, Nebius, National Grid, Nvidia, AES, NextEra Energy, Sungrow, SMA Solar, Hitachi Energy, Siemens Energy, Amazon, Microsoft, Equinix, Digital Realty (most only appeared in unpublished drafts). Kept to stay near the 120-word map.

## Sources, every one with date

Opened by me on 30 Oct 2026:
- Office of the Texas Governor, release, 3 Aug 2026 ("approximately over 474 gigawatts", more than five times record peak, about 90 per cent data centres, audit before any project moves forward): https://gov.texas.gov/news/post/governor-abbott-directs-comprehensive-data-center-audit
- PJM, "July 22, 2026 Dominion Load Transfer Event", System Operations Subcommittee, 31 Jul 2026 (07:56; 230 kV fault; about 3,800 MW to backup generation; high voltage triggered further transfer; fault cleared properly, no relay misoperations; ACE +3,928; 60.092 Hz; recovered within 9 minutes; load 99,984 to 96,205 MW; similar events 10 Jul 2024 and 17 Feb 2025): https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/sos/2026/20260730/20260730-item-06---july-22-dominion-load-transfer-event---presentation.pdf
- PJM Inside Lines, "PJM, Dominion Review Large Load Transfer Event", 11 Aug 2026 (largest in PJM history; about 1,500 MW each in the two earlier events): https://insidelines.pjm.com/pjm-dominion-review-large-load-transfer-event/
- PJM, "PJM LCL Ride-through Requirements", Planning Committee, 8 Sep 2026 (November 2026 FERC filing target; ERCOT NOGRR282 exemptions for sites operational or approved, or with signed agreements, by 14 Nov 2025; Dominion's six reclosing attempts of 50 to 70 ms; MISO draft envelope): https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2026/20260908/20260908-item-05---1-large-load-ride-through---presentation.pdf
- PJM, "LCL Ride-Through Requirements" solution, Planning Committee, 6 Oct 2026 (LCL definition 50 MW aggregate and 25 MW through power electronics; voltage and frequency tables; new projects from 16 Jan 2027; transition sites by 16 Jan 2028 or COD plus one year; limited exceptions): https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2026/20261006/20261006-item-07-b---1-lcl-ride-through-requirements-solution---presentation.pdf
- NERC, Level 3 Alert, Essential Actions, Computational Load, initial distribution 4 May 2026 (acknowledge by 11 May, report by 3 Aug; "does not create a mandatory obligation"): https://www.nerc.com/globalassets/programs/bpsa/alerts/level-3-computational-load-alert.pdf
- FERC, Order Directing NERC to File Reliability Standard(s) Pertaining to Computational Load Integration, 196 FERC ¶ 61,031, RD26-7-000, 16 Jul 2026 (file by 31 Dec 2026; workplan by 1 Mar 2027): https://www.ferc.gov/sites/default/files/2026-07/RD26-7-000.pdf
- EIA Today in Energy, 20 Feb 2026 (24 GW planned 2026 battery additions; Texas 12.9 GW, 53%; California 3.4 GW; Arizona 3.2 GW): https://www.eia.gov/todayinenergy/detail.php?id=67205

From the drafts' sidecars (primary, verified there 29 Oct 2026, not re-opened today):
- ERCOT, Senate Business and Commerce briefing, 29 Jul 2026 (474 GW as of June; about 205 GW eligible for Batch Zero, preliminary): https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf
- ERCOT, Batch Zero Verification and Audit, PUCT, 20 Aug 2026 (pause for 75 MW or more data centres and crypto; 17 loads, 6,608 MW; report by 10 Dec 2026): https://www.ercot.com/files/docs/2026/08/20/Batch-Zero-Verification-and-Audit-PUCT-Presentation.pdf
- ERCOT Board, Item 14 Batch Zero Update, 11 Sep 2026: https://www.ercot.com/files/docs/2026/09/11/14-Batch-Zero-Update.pdf
- ERCOT Board, Item 9.1, 13 Apr 2026 (PCLR "during periods of localized stress"; WL-PUN): https://www.ercot.com/files/docs/2026/04/13/9.1-Batch-Study-Update.pdf ; ERCOT trending topic, 18 Jun 2026: https://www.ercot.com/files/docs/2026/06/18/ERCOT-Trending-Topic-New-Batch-Connection-Process-for-Large-Electricity-Users.pdf ; PUCT approval of PGRR145, 18 Jun 2026: https://www.ercot.com/files/docs/2026/06/22/145PGRR-130-PUCT-Report-061826.docx
- Texas SB 6, 89th Legislature, enrolled (PURA 37.0561(c), (e); 39.170(a), (b)): https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm
- FERC show cause orders, 18 Jun 2026: PJM EL26-67 (195 FERC ¶ 61,211) https://www.ferc.gov/sites/default/files/2026-06/EL26-67-000.pdf ; SPP EL26-68 https://www.ferc.gov/sites/default/files/2026-06/EL26-68-000.pdf ; NYISO EL26-69 https://www.ferc.gov/sites/default/files/2026-06/EL26-69-000.pdf ; MISO EL26-70 https://www.ferc.gov/sites/default/files/2026-06/EL26-70-000.pdf ; CAISO EL26-71 https://www.ferc.gov/sites/default/files/2026-06/EL26-71-000.pdf ; ISO-NE EL26-72 (cited from FERC's abeyance order)
- SPP CHILLS accepted 5 Jun 2026, as available, up to seven years: SPP order EL26-68, P 17
- FERC abeyance orders, 14 Aug 2026: PJM https://www.pjm.com/-/media/DotCom/documents/ferc/orders/2026/20260814-el26-67-000.pdf ; NYISO https://www.nysrc.org/wp-content/uploads/2026/08/Att-3-NYISO-Show-Cause-Order-Abeyance-8-14-2026-20260814-3068_EL26-69-000.pdf ; ISO-NE https://www.iso-ne.com/static-assets/documents/100038/el26-72-000_abeyance.pdf
- PJM TOs' notice to the Members Committee, 9 Oct 2026 (Interim NITS "a temporary, non-firm transmission service"; capacity "will not be procured"): https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20261028/20261028-notice-of-pjm-transmission-owners-consultation-with-the-members-committee---informational-posting-only.pdf
- ISO-NE joint motion for abeyance: https://www.iso-ne.com/static-assets/documents/100038/joint_motion_for_abeyance_iso-ne_and_pto_ac.pdf ; NEPOOL counsel memo, 3 Aug 2026 (MISO and SPP, "reported"): https://www.iso-ne.com/static-assets/documents/100038/nepool_counsel_memo_motion_for_abeyance.pdf
- CAISO Large Loads straw proposal, 11 Aug 2026, pp. 38 to 39: https://stakeholdercenter.caiso.com/InitiativeDocuments/Large-loads-Straw-Proposal-Aug-11-2026.pdf
- PJM 2025/2026 BRA report, 30 Jul 2024: https://www.pjm.com/-/media/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.ashx ; PJM release 22 Jul 2025: https://insidelines.pjm.com/pjm-auction-procures-134311-mw-of-generation-resources-supply-responds-to-price-signal/ ; PJM release 14 Jul 2026: https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf
- Monitoring Analytics, report to PJM Members Committee, 27 Jul 2026: https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20260727-web/item-02---marketing-monitoring-report---presentation.pdf
- (No longer cited in the piece after the trim) LBNL, Queued Up 2025, 15 Dec 2025: https://emp.lbl.gov/sites/default/files/2025-12/Queued%20Up%202025%20Edition%20-%2012.15.2025.pdf
- (No longer cited in the piece after the trim) New Jersey BPU, 12 Feb 2025: https://www.nj.gov/bpu/newsroom/2025/approved/20250212.html
- Dominion Energy 10-K for 2025, 23 Feb 2026: https://www.sec.gov/Archives/edgar/data/715957/000119312526063120/d-20251231.htm ; 8-K exhibit 99.1, 14 Sep 2026: https://www.sec.gov/Archives/edgar/data/715957/000119312526390654/d107020dex991.htm
- JLARC Report 598, 9 Dec 2024, pp. 44 to 49 and Table 4-2: https://jlarc.virginia.gov/pdfs/reports/Rpt598.pdf
- CAISO Today's Outlook fuel source history (pattern https://www.caiso.com/outlook/history/YYYYMMDD/fuelsource.csv, Jun to Sep 2023 to 2026, Tommy's count, method in the california-still-shifts-the-sun sidecar); CAISO Key Statistics, Sep 2026: https://www.caiso.com/documents/key-statistics-sep-2026.pdf ; DMM 2025 Annual Report, Jun 2026: https://www.caiso.com/documents/2025-annual-report-on-market-issues-and-performance.pdf
- PJM, winter risk and seasonal ELCC, 13 Mar 2025: https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2025/20250313-special/2026-2027-irm-fpr-elcc-and-winter-risk.pdf ; ELCC class ratings 2026/27, 2027/28, 2028/29 (pjm.com res-adeq/elcc); 2029/30 MC presentation 19 Aug 2026: https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20260819/20260819-item-05---2029-2030-bra-irm-fpr---presentation.pdf ; preliminary ratings DY2028/29 to 2042/43: https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/preliminary-elcc-class-ratings-for-period-dy28-dy42-elcc.pdf
- DTE Energy 8-K, 28 Sep 2026: https://www.sec.gov/Archives/edgar/data/936340/000093634026000159/dtebusinessupdate92826fi.htm
- Google, 4 Aug 2025: https://blog.google/inside-google/infrastructure/how-were-making-data-centers-more-flexible-to-benefit-power-grids/ ; 19 Mar 2026: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/demand-response-data-center-milestone/
- IURC Cause 46276 order (April 2026): https://secure.in.gov/iurc/files/ord_46276_042926.pdf
- Nature Energy, Colangelo, Coskun et al., online 5 Dec 2025: https://www.nature.com/articles/s41560-025-01927-1 ; Nvidia blog (Oracle, Phoenix), 1 Jul 2025: https://blogs.nvidia.com/blog/ai-factories-flexible-power-use/ ; AI Energy Management Alliance, 16 Sep 2026: https://blogs.nvidia.com/blog/ai-energy-management-alliance/
- Leads, credited once, not cited for any figure: third-party YouTube review "State of AI data centres 2026", data to 5 Oct 2026 (research-build/archive/sources/source-ai-datacentre-video/TRANSCRIPT.md); Leo Cui, "NVIDIA and Google give AI Data Centers a Dimmer Switch", https://www.youtube.com/watch?v=q5JflUbObe8 ; Leo Cui, "The Entire Energy Sector Explained: Oil, Gas, Electricity & the Grid", https://www.youtube.com/watch?v=0zZyEF4Cq9U . Upload dates of the videos are not in my notes.

## Figures dropped or flagged

- ERCOT: per the brief, the Governor-verified figures (474 GW, five times record peak, 90%) are attributed to the Governor's release; 205 GW, 17 loads, 6,608 MW, the 75 MW pause and 10 Dec are attributed to ERCOT's own documents, which ercot.com blocked (403, Cloudflare) and were read via indexed text, corroborated by the Governor and POWER or Utility Dive. Tommy or the publish step should open the 29 Jul and 20 Aug decks once in a browser. Not used: Docket 59220 525.5 MW condition; 9,456 MW approved to energise; 194.3 or 191.8 GW classifications (sources disagree); the Sep 11 QSA counts (1,959 MW, 6,874 MW, search summary only).
- PJM 2027/2028 auction: now shown as $333.44, the cap, about 6,500 MW short (coordinator's fact-check confirmed these as primary; the 14 Jul 2026 PJM release cites the ~6,500 MW prior shortfall).
- PJM event: 2,970 MW and 1,099 MW wave figures (Inside Lines article per search summary; the PJM deck gives only the total) not used. Some reports say "about 3,900 MW" or "nearly 4,000 MW"; the piece uses the deck's "approximately 3,800 MW".
- Virginia: SCC orders of 25 Nov 2025 and 31 Jul 2026, the 85% / 60% minimum percentages, ramp, exit fee, July 2026 line extension directive, Valley Link 765 kV, SB 253 / HB 1393 opt-out: press-only, all left out. The 25 MW and 75% load factor figures are Dominion's 10-K definition of its high load category; the GS-5 name is from the 8-K. "Dominion owns the grid across most of Virginia" was dropped from the body.
- Google: Google's 19 Mar 2026 post lists DTE among its contracts to limit or shift ML work, so the piece now says only that DTE's filing does not state how much of the 350 MW computing delivers; MPSC approval date of 1 Oct 2026 (search snippet only) not used; London trial figures (up to 40%, 96 GPUs) not used and never combined with Phoenix; Silicon Valley Power breaker and Nvidia Aurora (press) not used; "cheapest" dropped (nothing compares costs).
- Batteries: CEC 21,112 MW not used (includes out-of-state and behind-the-meter). PJM's 94% / 43% is an estimate for 2026/27 published March 2025, dated so.
- Utility Dive (12 Aug 2026), the live piece's only source for the event, replaced by PJM's own documents.
- "Under a second": not in any PJM document I read; flagged in the claim note.

## Could not verify today

- ERCOT decks (403); see above.
- SEC EDGAR refused my request with the required User-Agent ("ThePhysicalLayer research") as an undeclared automated tool; I did not retry around it. The DTE 8-K (28 Sep 2026) and Dominion 10-K and 8-K figures rest on the drafts' sidecars (29 Oct 2026).
- FERC Federal Register notices for MISO and SPP abeyance; whether MISO, SPP and CAISO abeyance was granted (not stated in the piece).
- Whether PJM filed its ride-through proposal yet (target November 2026; no filing found as of 30 Oct).
- Upload dates of the Leo Cui videos and the identity of the "State of AI data centres 2026" channel.

## Fact-check fixes applied (30 Oct 2026, coordinator)

1. PJM ride-through table: added "above 1.10, up to 1.20 pu: 1 second" (the 22 Jul second wave was a high-voltage trigger) and the 299 s bands at 57.0 to 58.8 and 61.2 to 61.8 Hz; added PJM's line that temporary substitution through other resources "shall not, by itself, constitute compliance" (Manual 14B D-2 draft, 6 Oct 2026).
2. ERCOT exemption: sites approved to energise, or with signed agreements, before 14 Nov 2025 (PJM deck, 8 Sep 2026), in the table and the text.
3. FERC's 16 Jul order binds NERC only: "Binding standards are coming: FERC ordered NERC on 16 July to file them, with registry criteria, by 31 December 2026, and a workplan for more by 1 March 2027." The-power-it-drops note matches.
4. PJM 13 Mar 2025: data centres "a main reason".
5. DTE: softened; Google's 19 Mar post counts DTE among its ML demand-response contracts. PJM 2027/28 row now $333.44 and about 6,500 MW short.
6. New claim reworked: cut-first = early-connection tier, statutory load shed excluded; ERCOT firm-share limb dropped; ride-through adoption limb replaced by a 2028 event test (1,500 MW or more after a normally cleared fault). claims.ts entry above matches the piece.
7. Trims: "orders could not be read" sentence, NJ BPU and LBNL lines (and their sources) cut; Virginia section three sentences; exposure map about 127 words with rules, grids and wires merged; "northern Virginia" replaced by Dominion's zone (top layer and numbers.ts suggestion). Note on pjm-sends-the-bill corrected: never-published proposed claim, not on record, Tommy's decision.
