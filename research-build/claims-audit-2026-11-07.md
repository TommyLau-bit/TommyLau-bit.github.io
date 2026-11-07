# Claims audit, src/data/claims.ts (7 November 2026)

Read-only audit of every claim id except `data-centres-in-space` (already audited). Rule applied: a claim, falsifier or watch item is WRONG only where a fact in it (figure, date, entity, document name, or a status already false when written) is wrong. Judgements, predictions and tests are never WRONG because events moved on. STALE means true when written but since overtaken; no change recommended.

Evidence: the nine live depth pieces, their FACTCHECK.md files, the sidecars and research slices, the archived originals in research-build/archive/pieces/ and journal-drafts/, and for the retired homes (memory-not-maths, the-chip-supply-chain, ten-thousand-chips-one-thought) the archived deep text plus a web check where a fact looked doubtful. SEC EDGAR refused curl with the plain "ThePhysicalLayer research" user agent (HTTP 403), as it did for the plug fact-checker; no email was added, so no EDGAR document was re-opened in this pass.

Counts: 42 claims audited. OK with no items: 31. Claims with at least one item: 11. WRONG items: 2 (both borderline, see below). STALE items: 6. Notes (not wrong, no change): 9.

## WRONG

Both are the same kind of fault: a watch item written as an open question ("who wins") on 22 September 2026, when Singapore had already announced the winners on 21 August 2026. That is a status already false when written. They are borderline because the error is in a question's tense, not in a figure; if Tommy prefers to treat a watch question as wording, leave them and record them as STALE.

### the-part-money-cannot-hurry (dated 22 September 2026)
- WRONG. Current substring: `'Who wins Singapore\'s capacity award under the 1.25 ceiling'`
  Replacement: `'Who won Singapore\'s capacity award under the 1.25 ceiling (four operators, 50 MW each, 21 August 2026)'`
  Source: EDB and IMDA fact sheets of 21 August 2026 (50 MW each to Digital Realty, Equinix, Keppel DC and STT GDC), confirmed OK in research-build/deep-pieces/johor/FACTCHECK.md row 67 and in the live piece the-queue-not-the-chip ("On 21 August 2026 the Economic Development Board (EDB) and the Infocomm Media Development Authority...").

### two-governments-one-confession (dated 22 September 2026)
- WRONG. Current substring: `'Who wins the Singapore capacity award'`
  Replacement: `'Who won the Singapore capacity award (four operators, 50 MW each, 21 August 2026)'`
  Source: as above.

## Per claim

### microreactors
OK. Standard Nuclear SN-TN and SN-ID DOE approval targeted Q4 2026, Crusoe and Aalo at INL in 2027 on LEU of 5% or less, Part 57 proposed 1 May 2026 (91 FR 23628), first Janus reactor by September 2028, three DOE allocation rounds to date: all confirmed in microreactors/FACTCHECK.md.

### johor-singapore-rights
OK. 1,256 MW of 5.65 GW (Tenaga briefing, 28 August 2026); Singapore review 18 to 24 months from August 2026; Remote Access Security Act passed the House only; Sedenak West substation (no date) and the 500 kV backbone to Kulai East by 2030 (Tenaga, 28 August 2026), all confirmed in johor/FACTCHECK.md.
- Note: "the Energy Focus Group's margin test". The spare-margin rule was stated by the investment minister; the Energy Focus Group assesses each application first (Hansard, 28 October 2026). Attributing the test to the group that applies it is a fair reading, not a wrong fact.

### the-queue-not-the-chip (27 July 2026)
- Note: breaksIf "cut them from 36 months to 12". Tenaga's release of 9 August 2023 says 36 to 48 months to 12. The claim gives the low end of a stated range, so it understates the cut but is not false. No change (falsifiers are not reworded).
- Note: "The Green Lane project count beyond 33". The 33 projects by March 2026 is press only (TNB chief grid officer via Bernama, 29 May 2026; Tenaga-hosted clip); no TNB primary found, so the live piece dropped it. Not shown wrong.
- STALE: "Who wins Singapore's capacity award". Open when written (27 July); the award was announced 21 August 2026 (four operators, 50 MW each).
- OK: 2,346 MW contracted, about 1,374 MW used, August 2026 (Hansard, 28 October 2026, p. 9).

### the-part-money-cannot-hurry
- WRONG: see above.
- OK: "the press-reported 72.76 per cent Johor-Singapore zone utilisation" is correctly labelled press (Johor Menteri Besar's post of 16 January 2026, via Bernama); "Green Lane project count beyond 33" as in the note above.

### two-governments-one-confession
- WRONG: see above.
- OK: "Whether Johor's 72.76 per cent utilisation figure is restated or explained" (a press figure, framed as a question).

### the-power-it-drops
- Note: "Virginia's 3.8 gigawatt trip". PJM's 31 July 2026 deck gave about 3,800 MW and its 15 September deck about 3,900 MW for the 22 July 2026 event (plug/FACTCHECK.md; own-power/FACTCHECK.md item 22). Both are PJM's own figures, so 3.8 is not wrong. No change.

### the-way-out-has-its-own-queue
OK.

### what-the-battery-is-really-for
OK.

### the-product-is-time
OK.

### power-first-chips-last
OK.

### every-megawatt-got-harder
OK. "Whether Vertiv brings back a backlog figure": Vertiv's executive chairman said it is "not planning to share orders data going forward" (rack/FACTCHECK.md, not re-opened); consistent.

### oklo-sells-the-electricity
OK.

### marvell-collects-the-toll
OK.

### nebius-paid-for-what-is-switched-on
OK. "800 megawatts connected by the end of 2026" matches Nebius's "800 MW to 1 GW of connected power by the end of 2026" (letter, 12 February 2026).

### corning-lays-the-glass
OK.

### broadcom-wins-either-way
OK. Six custom chip customers and the MediaTek TPU split are as the archived piece reported them; nothing found to contradict.

### ti-feeds-the-chip
OK.

### tsmc-says-it-is-the-bottleneck
OK. Arizona's second fab in the second half of 2027 is TSMC's stated timing; nothing found to contradict.

### lumentum-makes-the-light
OK.

### schneider-sells-the-finished-system
OK. Systems 34% of FY2025 revenue (Products 47%, Systems 34%, Software and Services 19%, revenue EUR40,152m), Schneider FY2025 results, as recorded in research-build/archive/journal-drafts/schneider-sells-the-finished-system.md.

### ge-vernova-sells-the-wait
OK. 20 GW now, 24 GW in 2028, 30 GW in 2030 matches the live piece ("raise output from 20 GW a year to 24 GW in 2028 and 30 GW in 2030") and own-power/FACTCHECK.md.

### hitachi-energy-plans-the-queue
- STALE: "including the 140 weeks quoted for some Ludvika bushings". Hitachi Energy's delivery-times page, updated 29 October 2026, now gives 135 weeks for GSBK and ARF bushings of 245 to 550 kV from Ludvika (equipment/FACTCHECK.md item on bushings; live piece uses 135). The claim is dated 22 October, before that update, so 140 is taken as the figure then shown.
- OK: South Boston, Virginia (2028) and Mississippi (Gallman, 2029) plants; fiscal 2030 ends 31 March 2031. The 3.06 at 30 June 2026 could not be re-opened (Hitachi results); not shown wrong.

### eaton-order-book-outruns-it
OK. Nebraska (Bellevue) switchgear and South Carolina (Jonesville) transformer plants in 2027 match the live piece. 1.05 at June 2026 matches the piece's 1.049; the 1.04 for March 2026 and 0.93 for June 2025 could not be re-opened (EDGAR blocked; equipment/FACTCHECK.md also could not verify the earlier ratios). Not shown wrong.

### siemens-energy-measures-the-shortage
OK. EUR51bn at 30 June 2026 (Q3 FY2026 release, 5 August 2026); Charlotte (announced for early 2026, early 2027 by press) and Nuremberg by 2028 as in the live piece.

### ajinomoto-grows-with-the-package
OK. Kani City, Gifu, operating in fiscal 2032 (Ajinomoto release, 7 May 2026); Functional Materials margin 54.2% in fiscal 2025. The 2028 construction start was not re-opened; not shown wrong.

### asml-booked-ahead
OK. "Intel qualified it on select 18A layers in July 2026" checked: ASML's Q2 2026 release of 15 July 2026 says Intel Foundry uses High NA EUV on Intel 18A for a subset of Core Ultra Series 3 products, with select layers dual-qualified on NXE and EXE (ASML Q2 2026 presentation slide 6, as cited in the draft notes; reported e.g. by The FPS Review, 16 July 2026). Capacity of around 65 for 2026 and around 85 for 2027 matches ASML's call as recorded.

### micron-three-times-the-wafer
OK. "About three times the wafer" (Micron, 20 March 2024: HBM3E "consumes approximately three times the wafer supply" of DDR5); ID1 wafer output in mid 2027 (Micron prepared remarks, 30 September 2026, and 10-K, 9 October 2026, as in the retired piece).

### constellation-restarts-the-reactor
OK.
- Note: claim text "a fresh grid connection would not have been fully ready until around 2030 or later". FERC's order (195 FERC 61,162, 1 June 2026) says Crane "may not be able to obtain full deliverability until at least December 31, 2030". "Would" is firmer than "may", and "around 2030" is softer than "at least 31 December 2030", but this is a characterisation inside the claim's judgement, which nuclear/FACTCHECK.md item 15 rated OVERSTATED, not WRONG. No change.
- OK: 760 MW of rights from Eddystone (FERC order); Google's 890 MW of uprates (Constellation, 6 October 2026).

### the-plug-not-the-chip
OK. 1,256 MW against 5.65 GW, June 2026; 1.37 GW of 6 GW operating, August 2026 (Hansard, 13 October 2026); Country Group D:5 licensing; review 18 to 24 months from August 2026. "Digital Infrastructure Act" names the law the bill (Bill No. 20 of 2026) will become; it is the subject of a future watch item, not a status claim.

### america-rations-the-plug
OK. ER26-3515 rejection of 9 October 2026; ride-through filing November 2026 and legacy deadline 16 January 2028; PJM 2029/30 auction in December 2026 (cap US$337.83); ERCOT audit by 10 December 2026; DTE 350 MW of demand response for Google (DTE 8-K, 28 September 2026, which does not itself name Van Buren; the site name is press, not shown wrong). "NERC's standards due 31 December 2026" and "CAISO FILI" not re-opened; not shown wrong.

### the-equipment-queue
OK. Siemens Energy 3.96 at 30 June 2026 (EUR51bn over EUR12.889bn); Eaton 1.05; Jonesville and Bellevue in 2027; Nuremberg by 2028; Hitachi about 3.1 at 30 September 2026 (US$66.9bn over US$21.6bn, Hitachi results of 28 October 2026 as used by the piece, not re-opened).

### building-your-own-power
OK. 122 GW at 30 September 2026 and at least 130 GW expected at year end (GE Vernova 3Q26 release, 28 October 2026); 124 aeroderivative units, about 2.5 years (10-Q unit tables: 124 / 50 units trailing twelve months = 2.5; own-power/FACTCHECK.md item 6 asked for exactly this wording, which is already in place); US$33.2bn (US$33,163m, 10-Q); 2032 slots.

### nuclear-order-of-holdings
OK. Crane second half of 2027, Duane Arnold first quarter 2029 at the latest, Palisades without a date since fuel loading stopped (fuel load began 30 August, assembly tilted, NRC emergency amendment 30 September to 13 October 2026); Piketon lease fixed to end 1 October 2027 (Centrus 10-Q, 4 November 2026); Russian curb (decree 1516) and US waivers (PL 118-62) both ending with 2027; 760 MW.

### nuclear-for-ai (30 October 2026)
- STALE: "(maintenance only since 30 June 2026)". The maintenance-only option ran from 30 June to 30 September 2026 (Centrus 10-Q Q3 2026, via research-build/topics/nuclear-research/fuel-advanced.md), and on 4 November 2026 Centrus said the cascade now enriches HALEU for commercial buyers, no volume or start date given. Since no start date is published, it cannot be shown that the status was false on 30 October.
- STALE: claim text "commercial enrichment at the level they need has stopped in America". Same Centrus statement of 4 November 2026. Judgement inside the claim; never reworded.
- Note: "Palisades (no date since 21 October 2026)" against the newer claim's "since its fuel loading stopped in September 2026". Not a conflict: Holtec's release of 21 October 2026 recovered the tilted assembly and gave no new date (archived pre-depth nuclear piece).
- Note: "Aurora-INL" here and "Aurora-ID" in nuclear-order-of-holdings name the same Oklo plant; Oklo uses both. No change.
- OK: Kemmerer Unit 1 2030, Hermes 2 2030, one tonne by July 2032, waivers end 1 January 2028.

### powering-the-rack
OK. Power rack due second half of 2026 and row power centre 2027 (Nvidia white paper); Vertiv US$3.25m to 3.75m per MW (May 2026); TI about 13% (CEO, 21 October 2026 call).
- Note: "version 0.3 (July 2026)". The specification is rev 0.3.0, effective 22 June 2026, with the PDF dated 2 July 2026 (rack/FACTCHECK.md). Published in July; not wrong.

### heat-and-water
OK. Mesa 9.7 million gallons consumed in 2025; Henderson 239.4; 15%, 14%, 13% for 2023 to 2025; Waltham Cross and Canelones not yet in the table (Google Environmental Reports 2024 to 2026; heat/FACTCHECK.md).

### the-plug-stays
OK. SN6600-LD and Q3400-RD in the Vera Rubin reference architectures of 15 September 2026; SPIL 15-fold by mid 2027 (Nvidia, 21 October 2026).

### the-chip-supply-chain
OK. Seagate "vast majority" through 2028 (27 October 2026). ASML Capital Markets Day of 10 June 2027 not re-opened; not shown wrong.

### contracted-energised-running
OK. About 170 MW active and US$1.25bn annualised at end 2025 (Nebius letter, 12 February 2026); US$3.0bn at June 2026 (letter, 12 August 2026); US$12 million a megawatt "2026 base"; Oracle's quarter ending 28 February 2027.
- STALE (minor, no change): "1,256 MW against 5.65 GW, June 2026" is labelled "booked maximum demand"; the live Johor piece calls the 5.65 GW "in system" (connected) and 8.35 GW the full pipeline. The Johor piece's own chart labels 5.65 GW "Booked", so this is wording, not a wrong figure.

### hong-kong-has-the-plug
OK. Eight substations by June 2026, one more in the second half of 2026, 18 planned (CLP results, 26 February and 6 August 2026; "additional 12 data centres substations" on top of six); 9,258 MW against 7,455 MW; +12.8% and 6.6% (CLP, 12 October 2026); Range's 2028 and the government's 2029.

### memory-not-maths
OK. NVHBM (Nvidia, 26 August 2026); HBM4E ramp in 2027; Trainium4 as NVHBM's first named partner, as quoted in the retired piece.

## STALE list (no change recommended)
1. the-queue-not-the-chip: "Who wins Singapore's capacity award": decided 21 August 2026.
2. hitachi-energy-plans-the-queue: 140 weeks: now 135 weeks (Ludvika page, 29 October 2026).
3. nuclear-for-ai watch: "maintenance only since 30 June 2026": option ended 30 September; commercial enrichment announced 4 November 2026.
4. nuclear-for-ai claim: "commercial enrichment ... has stopped in America": same Centrus statement.
5. the-power-it-drops: 3.8 GW: PJM's later deck says about 3.9 GW (both PJM figures).
6. contracted-energised-running: "booked maximum demand" for the 5.65 GW in-system figure (wording only).
