# Sidecar: the-chip-supply-chain (deep piece, cluster 10)

Cluster 10, "The chip supply chain's slow parts". Drafted 30 Oct 2026 to BRIEF-DEEP.md, matching the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/the-chip-supply-chain.md` (draft: true), kept outside `src/content/journal/` so the loader does not read it. Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "The chip supply chain's slow parts are sold years before they are made" (12 words, sentence case, names the subject).
- Top layer (cold open, analogy, How it works, The number that matters): 541 words, about 13 figures counting dates and number words, 0 company financial figures. Analogy 73 words. Average sentence about 13.5 words.
- Investor layer: 2,498 words before the exposure map by the checker's whitespace count (the claims block alone is about 1,050, of which about 800 are fixed word-for-word quotes). Exposure map about 130 words. Whole body about 3,270.
- `brand/check-piece.py research-build/deep-pieces/the-chip-supply-chain.md` (deep mode): 0 failures, 1 warning ("average sentence is 26 words"). The warning comes from the markdown table rows and the long fixed claim quotes, which the checker reads as single sentences; the prose itself averages about 15. Not fixable without rewording claims.
- Uses `hr.layer` and `p.layer-label`, as the prototype; the prototype sidecar notes the CSS is not yet in `src/`.

## Frontmatter notes

- `date: 2026-10-30` is a placeholder. At go-live it becomes the real publish time (`YYYY-MM-DDTHH:MM:SS+08:00`). The four live claims keep their own `date` in claims.ts.
- New slug `the-chip-supply-chain`; none of the absorbed slugs is reused, so all seven live URLs need redirects.
- `cover: "/covers/nobody-makes-a-b200-alone.svg"` (existing) until a new cover is drawn; proposal below.
- Tags: the-stack, supply-chain, memory (all existing).

## Seagate: checked, never live

`src/content/journal/seagate-sells-the-terabyte.md` has had `draft: true` in every commit (only one commit, df6e5cd, "Drafts ... fact-checked and queued"). Its claims.ts entry has no `date`, and `brand/linkedin-posts.md` #36 shows it scheduled for the site on Wed 11 Nov 2026 and LinkedIn on Wed 9 Dec. So it is treated as proposed, not on record: the piece paraphrases it under "Proposed, never published" and folds its test into the new claim. **The 11 Nov publish task and the 9 Dec LinkedIn post (#36) must be paused or cancelled before 11 Nov, or the slug goes live separately.** Not done here (no edits; Tommy's go needed).

Decision for Tommy on its claims.ts entry: (a) delete it, since it never went live and the record rule covers published claims; or (b) keep it, with no `date`. **Never give it `home`** (coordinator, 30 Oct): `home` marks a claim on record in the deep piece, and this one is not. I recommend (a). The piece mentions it in two sentences under "Proposed, never published" and keeps Seagate on the watch list; it is no longer a limb of the new claim.

## Thesis and how it treats the old claims

Thesis: the chip moves at the pace of its few irreplaceable suppliers (one or few makers, a qualification wall, growth only by new plant), and they are sold years ahead. The lead-time table gives each company's own words, dated. The piece says openly that lengthening horizons fit buyers locking in supply in a boom as well as scarcity (ASML's CEO: demand "still fluctuating", July 2026), and hangs nothing on the cause.

Notes in Claims on record:
- tsmc-says-it-is-the-bottleneck: near half holds, on TSMC's own 3Q26 transcript (15 Oct 2026): Wei "the gap between demand and supply are still quite big"; Huang "while the tool supply is tight"; Wei on US data centre power checks, "The feedback is so far so good". ASML's warning is a forecast of tool supply and is stated not to test the 2028 half, which stays open.
- asml-booked-ahead: booking half stronger (14 Oct 2026 6-K: planned 2027 and 2028 supply "will not fully meet the demand"; customers interested in 2029 and 2030 orders). **Growth half at risk**: ASML is "investigating ways to increase capacity for 2028 beyond the 30% increase"; it breaks above 40% in one year, or if ASML announces new EUV cleanroom space, which a step beyond two 30% steps may need (Fouquet: both 30% steps fit the "existing footprint", as transcribed, Webull).
- ajinomoto-grows-with-the-package: "Where I was wrong": the breaksIf says the margin is disclosed only as rounded wording; the research note's correction found the results data sheets print Functional Materials sales and business profit in yen (54.2% FY2025, 57.7% Apr to Jun 2026). Test sharper; both halves hold.
- micron-three-times-the-wafer: both halves hold (30 Sep 2026 remarks; 10-K of 9 Oct 2026). The 10-K fact is stated plainly in the Micron section (base logic die "designed and manufactured in-house"), not framed as a correction, because the TSMC base-die lead (A14) was never published.
- Explainers without claims, corrected openly in their sections: the-two-seconds-after-you-hit-send ("which is never the chip": too strong; cross-linked to the 27 July claim at /journal/the-queue-not-the-chip/#claims-on-record) and the-countertop-is-the-bottleneck ("the kind of hard that money solves in quarters": Micron's fab dates run to 2030).

## New deep claim and falsifier (claims.ts)

Redesigned 30 Oct 2026 after the coordinator's fact-check (ASML 2028 near-certain; Micron 2028 duplicated the live Micron claim; Seagate grows by terabytes per drive, not new plant, so it contradicted the mechanism). Matches the piece word for word.

```ts
  {
    id: 'the-chip-supply-chain',
    claim: 'In the AI chip supply chain, the parts that only one or a few qualified makers can supply, and that grow only through new cleanrooms, stay sold more than a year ahead. In its results published between 1 December 2027 and 31 March 2028, ASML will describe its 2029 low NA EUV supply as close to fully covered by orders or short of demand, and by its fiscal first quarter 2029 results, around December 2028, Micron will have said most of its calendar 2029 HBM supply is agreed.',
    breaksIf: 'ASML, in its results published between 1 December 2027 and 31 March 2028, says its 2029 low NA EUV capacity exceeds customer orders, or does not describe 2029 as close to fully covered or short of demand; or Micron, by its fiscal first quarter 2029 results (around December 2028), has not said most of its calendar 2029 HBM supply is agreed, or reports unsold HBM and attributes it to customer demand. A shortfall caused by late cleanrooms or suppliers supports the claim rather than breaking it.',
    watch: ['How ASML describes 2028 and 2029 low NA EUV supply against demand, and the size of its 2028 capacity step (Capital Markets Day, 10 June 2027)', 'Whether Micron says most of next year\'s HBM is agreed, each autumn, and whether ID1 starts wafer output in mid 2027', 'How far ahead Seagate says data centre nearline supply is allocated (vast majority through calendar 2028 at 27 October 2026)', 'Whether TSMC publishes any CoWoS capacity or lead time figure', 'Whether Ajinomoto\'s Kani City film plant starts construction in 2028'],
  },
```

Why these limbs: both are the two steps in the chain that are single or few source, need new cleanroom to grow, and state a forward horizon in their own words. ASML (Q4 2027 results, late January 2028) is asked about 2029, a year and more out; on 14 Oct 2026 it named 2029 only as a year some customers want to order for, so this is not near-certain. Micron is asked about calendar 2029 by fiscal Q1 2029 (around December 2028), one year beyond the live Micron claim's 2028 test, so it does not duplicate it; memory's bust record makes it a real risk.

What separates this mechanism from the equipment queue (cluster 3): there, several makers have full factories and backlog measures the wait. Here a second maker cannot be bought at any price; a new one must first pass qualification. The piece says so in "The mechanism in depth".

A contrast limb (a quick-to-swap part that should not be sold years ahead) was considered and dropped: rack assemblers and connector makers (Foxconn, Quanta, Wistron) publish no supply horizon, so it would not be observable from primary disclosures. Seagate was dropped from the claim and kept on the watch list: it is few-maker and qualification-bound, but grows by density without new plant by choice, so it does not test the plant half.

Alternatives considered: (A) ASML's reported systems backlog: ASML stopped reporting bookings after Q4 2025 and its backlog includes DUV and metrology, so it is not an EUV horizon. (B) A TSMC CoWoS test: no published number. (C) An Ajinomoto film-binding test: Ajinomoto aims its expansion at demand to 2030.

Interaction with the TSMC claim: the new claim is about chip-side horizons, not the grid, so it does not test the TSMC claim's longer-run half; the TSMC note says ASML's warning does not either.

## Existing claims.ts entries (metadata only, at merge, Tommy to approve)

Add `home: 'the-chip-supply-chain'` to tsmc-says-it-is-the-bottleneck, asml-booked-ahead, ajinomoto-grows-with-the-package, micron-three-times-the-wafer. Their `date`, `claim`, `breaksIf` and `watch` are untouched. (claims.ts already has the `date` and `home` fields; the prototype sidecar called the second one `piece`, the file uses `home`.)

## Redirect map

| Old URL | Redirect to |
|---|---|
| /journal/nobody-makes-a-b200-alone/ | /journal/the-chip-supply-chain/#nobody-makes-a-b200-alone |
| /journal/the-two-seconds-after-you-hit-send/ | /journal/the-chip-supply-chain/#the-two-seconds-after-you-hit-send |
| /journal/tsmc-says-it-is-the-bottleneck/ | /journal/the-chip-supply-chain/#tsmc-says-it-is-the-bottleneck |
| /journal/asml-booked-ahead/ | /journal/the-chip-supply-chain/#asml-booked-ahead |
| /journal/ajinomoto-grows-with-the-package/ | /journal/the-chip-supply-chain/#ajinomoto-grows-with-the-package |
| /journal/the-countertop-is-the-bottleneck/ | /journal/the-chip-supply-chain/#the-countertop-is-the-bottleneck |
| /journal/micron-three-times-the-wafer/ | /journal/the-chip-supply-chain/#micron-three-times-the-wafer |

seagate-sells-the-terabyte was never live, so it needs no redirect; its anchor exists in case one is wanted. Sections and anchors in order: The mechanism in depth; One B200, sorted by how long each part takes to replace (#nobody-makes-a-b200-alone, #the-two-seconds-after-you-hit-send); ASML (#asml-booked-ahead); TSMC (#tsmc-says-it-is-the-bottleneck); Ajinomoto (#ajinomoto-grows-with-the-package); Micron (#the-countertop-is-the-bottleneck, #micron-three-times-the-wafer); Seagate (#seagate-sells-the-terabyte); Claims on record; What would prove me wrong; Research notes.

## stack.ts

Layer `chips`. At merge the chips list becomes `pieces: ['the-chip-supply-chain']` (all five current entries fold into it). This also empties the `memory` layer (countertop, micron, seagate all fold in). Two options for Tommy: (1) widen `chips` to name "Chips, memory and the factories that make them" and remove `memory`, which also means removing its stop in `src/components/Descent.astro`; or (2) keep `memory` and list the deep piece there instead, leaving `chips` to TI and the network cluster. I recommend (1): the deep piece's lead mechanism is the whole chip supply chain, and a layer with no piece fails the map's purpose.

## Glossary (heading "Chips, memory and the wiring between them")

Already present, no change: Wafer, Foundry, Fab, CoWoS, Advanced packaging, Die, Package, Qualification, Lithography, EUV, EUV scanner, Numerical aperture (NA), High NA, Photoresist, Package substrate, ABF, DRAM, DDR5, Trade ratio, Through-silicon via, Cleanroom, HBM, Nearline drive, Areal density, HAMR, Lead time, Business profit. Add:
- `Base die`: The logic chip at the foot of an HBM stack that talks to the processor. Micron designs and makes its HBM4 base die in-house.
- `Low NA EUV`: ASML's standard EUV machines, the ones its yearly capacity figures (around 65 in 2026) count. High NA is the newer, finer model.
- `Exabyte`: A billion gigabytes. Hard drive makers report how much storage they ship in exabytes.
- `Supply allocation`: A maker's commitment of future output to named customers. Seagate reports how far ahead its drive output is allocated.

## numbers.ts (physical only)

New:
```ts
  { layer: 'chips', value: '2029 and 2030', what: 'Years for which some of ASML\'s customers already want to order EUV machines, as ASML said its planned supply for 2027 and 2028 will not fully meet demand. ASML is the only maker.', piece: 'the-chip-supply-chain', asOf: 'October 2026' },
  { layer: 'chips', value: 'through 2028', what: 'How far ahead Seagate has allocated the vast majority of its data centre nearline drive supply, with some cloud agreements to 2030. It grows supply by more terabytes per drive, not more drives.', piece: 'the-chip-supply-chain', asOf: 'October 2026' },
```
Existing entries to repoint at merge (Tommy's decision, not edited): the TSMC fab-time entry, `~65 → ~85` (ASML), `70 → 120 mm` (Ajinomoto), `~3×` (Micron), `+26% on flat units` (Seagate, which points at a never-published draft) all change `piece` to `the-chip-supply-chain`; layer `memory` entries move to `chips` if option (1) above is taken. (The existing values contain an en dash and arrows; they are data, not prose, and were already approved.)

## LinkedIn post (§9)

```
ASML, the only maker of the machines that print the finest AI chips, says its planned supply for 2027 and 2028 "will not fully meet the demand" of its customers, and some want to order for 2030.

It is not alone. Micron has agreed most of its 2027 stacked memory, and Seagate has allocated most of its data centre drives through 2028. Each is a part only one or a few makers can supply, and each grows only as fast as a new building, so the chip side is booked as far ahead as a grid connection.

The piece covers the lead time at each step from the companies' own filings, one B200 sorted by how long each part takes to replace, and the claims I have on record.

https://thephysicallayer.fyi/journal/the-chip-supply-chain/

#Semiconductors #SupplyChain #AIInfrastructure
```
Note: the seven absorbed URLs keep their live posts via redirects. The Seagate post #36 (9 Dec) should be withdrawn, not rewritten.

## Cover proposal (not drawn)

`/covers/the-chip-supply-chain.svg`. A horizontal timeline from 2026 to 2032 in letter-spaced grey years. Five lanes, one per step (EUV, CoWoS, FILM, HBM, DRIVES), each a blue bar (compute colour) from today to its committed horizon or new plant date: EUV to 2028 with a faint dotted extension to 2030, HBM to 2027 with a plant marker at mid 2027, DRIVES to 2028, FILM a gap ending in a plant marker at 2032, CoWoS a bar with a "?" for no published figure. One amber vertical line at today. Caption: "THE CHIP SUPPLY CHAIN'S SLOW PARTS". Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Edits other files need (not made)

- `src/config.ts` READING_PATH stage 1 is `the-two-seconds-after-you-hit-send` ("One piece. Read it and the rest of the site makes sense."). After merge that slug is a section of this piece, which is not an on-ramp. Tommy should decide what replaces it; the redirect keeps the link working meanwhile. (Not adding a new piece; replacing a merged one.)
- `src/components/Descent.astro` lines 492, 610, 617 link and `reads()` the slugs nobody-makes-a-b200-alone, asml-booked-ahead, tsmc-says-it-is-the-bottleneck, ajinomoto-grows-with-the-package; `reads()` will need the deep piece (or anchored hrefs) once the originals leave `src/content/journal/`. The memory stop goes if option (1) above is taken.
- `src/content/journal/ten-thousand-chips-one-thought.md` line 50 links "the next piece" to the countertop slug; the redirect resolves it, but at the network cluster merge it should point at `/journal/the-chip-supply-chain/#the-countertop-is-the-bottleneck`.
- `research-build/archive/sources/source-watch-later/UNCAPPED-RESULTS.md` row A14 states the TSMC base-die lead; line 59 already records Micron's 10-K. No action beyond not using A14.
- At merge, the seven live files and the Seagate draft go verbatim into `research-build/archive/pieces/`.
- Consistency with the prototype: the prototype says the plug, not the chip, decides who builds in Johor; this piece says chip-side horizons now run as long as some grid queues. Not a contradiction (different places and steps), and both say the grid is the slower clock over the longer run.

## Sources, every one with date

Re-opened by me on 30 Oct 2026:
- ASML Q3 2026 results, 14 Oct 2026 (6-K): "we now expect that our supply as currently planned for both 2027 and 2028 will not fully meet the demand of our customers"; "investigating ways to increase capacity for 2028 beyond the 30% increase we previously communicated"; "some customers are expressing an interest in placing orders with us for 2029 and even 2030"; "Our customers continue to increase their short- and medium-term equipment demand forecasts with us". https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/pressreleasefinancialresul.htm ; presentation https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/a2026_10x14xpresentation.htm (no EUV unit split; Capital Markets Day 10 June 2027).
- TSMC 3Q26 earnings call transcript, 15 Oct 2026 (Refinitiv StreetEvents, posted by TSMC IR), re-opened by me: Wei "the gap between demand and supply are still quite big"; Huang "while the tool supply is tight, we always collaborate closely with our tool suppliers well in advance"; "The feedback is so far so good, and the CSPs have been well prepared" (on sending TSMC teams to check US data centre build-out and power supply): https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/eba4fac72873bf546b669bd2b5d973df5c93215d/TSMC%203Q26%20Transcript.pdf
- TSMC 3Q26 Management Report, 15 Oct 2026 (HPC 68% / 66% / 57% for 3Q26, 2Q26, 3Q25; revenue NT$1,494.24bn, +50.9% YoY; wafer shipments 4,476k vs 4,085k 12-inch equivalent, +9.6%; "strong demand for our leading-edge process technologies"): https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-10/f53a64fd40fc0b453f94e077e5aba8cad506f27b/3Q26%20ManagementReport.pdf ; release https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/a3q26e_withguidancexfinal.htm
- Micron Form 10-K, fiscal year ended 3 Sep 2026, filed 9 Oct 2026 (HBM4 base logic die and DRAM core dies "designed and manufactured in-house"; HBM "requires a higher number of wafers and more cleanroom space to produce the same number of bits as conventional DRAM"; some components "have long lead times, requiring us to place orders up to a year in advance"; HBM4E volume ramp in calendar 2027): https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm . Direct curl with the brief's User-Agent was refused by SEC as an undeclared tool; read through WebFetch, which quotes in short excerpts only.
- Seagate Supplemental Financial Information Q1FY27, 27 Oct 2026 ("Vast majority of Data Center nearline supply allocated through CY28, with some cloud supply agreements extending through CY30"; "address exabyte growth by increasing capacity per drive rather than increasing drive unit production"; Data Center 198EB, 90% of exabytes, up about 24% YoY; Mozaic 5 qualification shipments toward end of CY27): https://s24.q4cdn.com/101481333/files/doc_financials/2027/q1/STX-FQ1-27-Supplemental.pdf ; release 28 Oct 2026: https://www.sec.gov/Archives/edgar/data/1137789/000113778926000300/stxq12027pressreleasefinan.htm

From the absorbed pieces' sidecars (primary, verified there, not re-opened today):
- ASML Annual Report 2025 on Form 20-F, 25 Feb 2026 (only manufacturer; ZEISS "production capacity" limit; Oberkochen and Wetzlar; 24.9%; 48 EUV in 2025, 44 in 2024): https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/asml-20251231.htm
- ASML Q2 2026 results, 15 Jul 2026: https://www.sec.gov/Archives/edgar/data/937966/000162828026048235/pressreleasefinancialresul.htm . ASML's own transcript of the prepared remarks, 15 Jul 2026, re-opened by me: CEO Christophe Fouquet, "For 2027, we are now close to being fully covered with orders for Low NA EUV"; CFO Roger Dassen, "We now expect to ship around 65 Low NA EUV systems this year": https://ourbrand.asml.com/asset/1fd3908a-0381-47b5-9b69-a3094f656651/2026_07_15-ASML-Transcript-investor-call-Q2-2026.pdf . Q&A only in a third-party transcript (Webull), quoted "as transcribed": "existing footprint": https://www.webull.com/news/15235467245265920 . "Still fluctuating" dropped.
- TSMC earnings calls of 15 Jan, 16 Apr and 16 Jul 2026 (fab two to three years, ramp one to two, packaging limiting customers), as cited in the live TSMC piece: https://investor.tsmc.com/english/quarterly-results
- Ajinomoto results presentation, 7 May 2026 (package sizes; ABF volume split; Kani site): https://ajinomoto-ir.swcms.net/company/en/ir/event/presentation/main/011111114/teaserItems1/01/linkList/00/link/FY25Q4_Presentation_E_with%20script.pdf ; Kani City release, 7 May 2026: https://news.ajinomoto.co.jp/2026/05/20260507-02.html ; ASV Report 2026, September 2026: https://www.ajinomoto.co.jp/company/en/ir/library/annual/main/04/teaserItems1/0/linkList/0/link/ASV_Report_2026_A4_en.pdf ; ABF page: https://www.ajinomoto.com/innovation/our_innovation/buildupfilm
- Ajinomoto Functional Materials margin 54.2% (FY2025, data sheet of 7 May 2026) and 57.7% (Apr to Jun 2026, data sheet of 6 Aug 2026) from its results data sheets: taken from the published Ajinomoto research note's `correction` field (src/content/calls/ajinomoto.md); data sheet URL is in research-build/ajinomoto/data.py, not re-opened by me.
- Micron fiscal Q2 2024 prepared remarks, 20 Mar 2024 ("HBM3E consumes approximately three times the wafer supply as D5"), on investors.micron.com (the coordinator located it; the static-file link redirected for me, so I could not re-open it; the MarketBeat transcript carries the same words). The 17 Dec 2025 transcript line is dropped (it renders HBM as "HVM"). Micron 30 Sep and 24 Jun 2026 remarks: 24 Jun 2026 (https://s25.q4cdn.com/621799436/files/doc_financials/2026/q3/Q3-FY26-Prepared-Remarks.pdf), 30 Sep 2026 (https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf).
- Seagate: Form 10-K for year to 3 Jul 2026, filed 4 Aug 2026 (nearline 695 vs 497 EB; custom tools with long lead times): https://www.sec.gov/Archives/edgar/data/1137789/000113778926000159/stx-20260703.htm ; supplementals 27 Jan 2026 (https://s24.q4cdn.com/101481333/files/doc_financials/2026/q2/STX-FQ2-26-Supplemental.pdf) and 28 Apr 2026 (https://s24.q4cdn.com/101481333/files/doc_financials/2026/q3/STX-FQ3-26-Supplemental.pdf); call of 28 Jul 2026 (transcript, third party: https://www.marketbeat.com/earnings/reports/2026-7-28-seagate-technology-plc-stock/).
- Nvidia Form 10-K, 25 Feb 2026 (lead times beyond twelve months; deposits and capacity commitments; memory from SK Hynix, Micron, Samsung): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm ; Blackwell architecture page (208 billion transistors, two dies, TSMC 4NP): https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/

No third-party lead (video, SemiAnalysis) is used, so none is credited.

## Figures dropped or flagged

- TSMC third quarter call (15 Oct 2026): my first search found only press; the coordinator located TSMC's own transcript, now used (above). Focus Taiwan's CoWoS paraphrase is not used.
- TSMC 2026 capex US$60 to 64bn: press only today; not used.
- CoWoS supply gap of 20% narrowing to 10% (TrendForce, citing Economic Daily News): press, not used.
- "CoWoS-L" for the B200 (Huang via Reuters): press, dropped.
- Eight HBM stacks per B200 (AnandTech, TechInsights): press, dropped.
- Ajinomoto "more than 95%" (its own investor overview): not used; "market share" wording is banned by the checker and the ABF page wording is used instead.
- ABF price rise of 30% (May 2026), qualification of "30 to 36 months": secondary, not used.
- Mozaic "up to 44 TB": call transcript only (third party), dropped.
- HBM "five to six times the bandwidth and cost" from the countertop explainer: never sourced, dropped.
- SK Hynix and TSMC base-die partnership: press (2024 plan), not used; the piece states only Micron's 10-K.
- Revenue +50.9% on wafers +9.6% (TSMC): dropped in the trim; mix explains much of it, so it was not evidence of shortage.
- ASML 2026 Q3 EUV units: not disclosed separately (121 lithography systems in total); not used.

## Could not verify today

- SEC blocked direct downloads with the brief's User-Agent ("undeclared automated tool") after one submissions API call succeeded; filings were read through WebFetch, which returns short excerpts, so the Micron 10-K quotes are exact but brief. Not bypassed.
- TSMC's January, April and July 2026 call wording rests on the live TSMC piece; I did not re-open the transcripts.
- Ajinomoto's exact margins (54.2%, 57.7%) rest on the research note's correction; data sheets not re-opened.
- Micron's 2024 and 2025 call quotes rest on third-party transcripts as in the Micron sidecar; Micron's own 17 Dec 2025 PDF was not retrieved then either.
- ASML's July statements "close to being fully covered with orders" and "still fluctuating" rest on a third-party transcript (Webull), as in the live piece.
- Seagate's 10-K figures (695 and 497 EB) are from its sidecar, not re-opened.

## Fact-check fixes applied (30 Oct 2026)

1. TSMC note now cites TSMC's own 3Q26 transcript (gap "still quite big", tool supply tight, US power "so far so good"); ASML's warning said not to test the 2028 half.
2. ASML note: growth half also breaks on new EUV cleanroom space; "existing footprint" labelled as transcribed.
3. Cold open and LinkedIn use ASML's exact "will not fully meet the demand" (6-K, 14 Oct 2026).
4. Seagate horizon rewritten from its own supplementals (through CY26, 27 Jan; largely through CY27, 28 Apr; vast majority through CY28, 27 Oct: about a year every six months). The July third-party transcript is no longer cited in the piece.
5. "Still fluctuating" dropped.
6. Micron base die stated plainly from the 10-K; no correction framing.
7. "Close to being fully covered" re-sourced to ASML's own transcript; it was the CEO, not the CFO. **The live asml-booked-ahead piece says "Its chief financial officer said"; that original text is not edited (archive rule), but the deep piece now attributes it correctly.** Micron's three times to its 20 Mar 2024 prepared remarks; 17 Dec 2025 line dropped; Ajinomoto data sheets dated; Gifu now "six to nearly seven years" (land May 2026, operation in fiscal 2032, April 2032 to March 2033).
8. Table: "expects to ship around 65 ... its 2026 capacity"; Nvidia's "extended lead times" of more than 12 months stated separately from deposits and capacity commitments.
9. New claim redesigned (above): ASML and Micron moved to 2029, Seagate dropped to watch, mechanism separated from the equipment queue.
10. Top layer: "one to two more to fill" and the "By September"/"By October" dates dropped (about 13 figures by strict count, counting number words). Rough sort cut to one sentence; Seagate-proposed block two sentences; "never the chip" cross-linked to the 27 July claim.

Counts after fixes: top layer 541 words; investor layer 2,498 words before the map (checker's whitespace count). check-piece.py on a scratch copy: 0 failures, 1 warning (average sentence 26 words, from the table rows and fixed claim quotes).
