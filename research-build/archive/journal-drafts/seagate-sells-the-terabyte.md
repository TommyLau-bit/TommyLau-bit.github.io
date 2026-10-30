# Sidecar: seagate-sells-the-terabyte (DRAFT, for Tommy's approval)

Piece: src/content/journal/seagate-sells-the-terabyte.md (draft: true)
Cover: public/covers/seagate-sells-the-terabyte.svg
Checker: 0 failures, 0 warnings. Body 559 words, 7 figures, 0 money figures.

## Subject choice
Seagate, not Western Digital. Seagate's own supplemental (27 Jan 2026) states the mechanism in its words: exabytes "up 26% YoY on similar number of units", and its CEO said on 28 July 2026 "We're not really increasing the box count." Seagate also discloses the allocation horizon each quarter, so the horizon moving out (through CY26 in January, CY27 in April, into CY28 in July) is visible in primary documents. Western Digital says similar things (LTAs discussed into 2029 to 2031, 5 Aug 2026 call) but its HAMR is a year behind and it does not state the flat-units point as cleanly.

## Proposed claim
Seagate is meeting AI's demand for storage by putting more terabytes in each hard drive, not by making more drives, so its high-capacity supply stays committed well over a year ahead.

Alternatives considered:
1. "AI turns hard drives from a commodity into a reserved product, sold years ahead like turbines." Rejected: repeats the GE Vernova and Micron "sold ahead" angle without the distinctive mechanism.
2. "HAMR is the only route by which hard drive supply can grow, so Seagate's laser drives set the pace of cold storage for AI." Rejected: depends on Western Digital's HAMR timing and on qualification forecasts; harder to test plainly and closer to a product bet.
Chosen because the flat-units, rising-density mechanism is physical, Seagate states it itself, and it is testable on two observables (units versus terabytes per drive; the allocation horizon).

## claims.ts entry
```ts
  {
    id: 'seagate-sells-the-terabyte',
    claim: 'Seagate is meeting AI\'s demand for storage by putting more terabytes in each hard drive, not by making more drives, so its high-capacity supply stays committed well over a year ahead.',
    breaksIf: 'Seagate grows supply by making many more drives, through a new drive factory or drive numbers rising faster than terabytes per drive; or, at any quarterly results before the end of 2027, Seagate says most of its nearline output for the next calendar year is not yet committed.',
    watch: ['Seagate nearline exabytes shipped versus drive units', 'Average terabytes per nearline drive', 'How far ahead Seagate says nearline output is allocated (into calendar 2028 as of July 2026)', 'Any new Seagate drive or head and disk factory'],
  },
```

## stack.ts layer
Put it in 'memory' (the layer already carries the countertop piece's storage paragraph and Seagate/Western Digital in its exposure map). Suggest, optionally, widening the layer at publish so storage is not forced in:
- name: 'Memory and storage'
- what: 'Stacked memory sits beside each processor feeding it the model\'s numbers, and hard drives further back keep the data AI produces.'
- constraint unchanged.
A separate 'storage' layer is not justified by one piece; it would also need a hand-drawn stop in Descent.astro.

## Glossary (heading: 'Chips, memory and the wiring between them')
- ['Nearline drive', 'A high-capacity hard drive for data that is kept rather than constantly used. The cheapest place per terabyte to store the data AI produces.']
- ['Areal density', 'How much data fits on each patch of a hard drive\'s disk. Raising it is how drive makers add storage without adding drives.']
- ['HAMR', 'Heat-assisted magnetic recording. A tiny laser warms a spot on the disk for an instant so it can hold a smaller magnetic bit. Seagate sells it as Mozaic.']
- ['Qualification', 'only if not already present: The testing a customer runs on a part before trusting it in production.']

## numbers.ts (physical)
```ts
  { layer: 'memory', value: '+26% on flat units', what: 'How much more hard drive storage Seagate shipped in a year on a similar number of drives. Supply grows by packing each drive, not by making more.', piece: 'seagate-sells-the-terabyte', asOf: 'December quarter 2025' },
```

## LinkedIn post
Seagate shipped 26 per cent more hard drive storage in a year on roughly the same number of drives.

AI keeps producing data that has to live somewhere, and the spinning hard drive is still the cheapest place to keep it. Seagate is answering by packing more terabytes into each drive rather than building more, so most of what it can make is already promised into 2028. Storage grows only as fast as each disk can be packed.

The piece covers how a laser lets a disk hold more, why the makers will not simply build more drives, and what would prove me wrong.

https://thephysicallayer.fyi/journal/seagate-sells-the-terabyte/

#DataCentres #AIInfrastructure #Storage

## Sources (every figure)
- "about two fifths more data centre storage in its last financial year": nearline exabytes 695 in FY2026 vs 497 in FY2025 (+40%). Seagate Form 10-K, fiscal year ended 3 July 2026, filed 4 Aug 2026, MD&A revenue table. https://www.sec.gov/Archives/edgar/data/1137789/000113778926000159/stx-20260703.htm
- "vast majority of exabytes shipped into large data center deployments" and "AI-enhanced applications are further accelerating data creation": same 10-K, Item 1 Business.
- Factory equipment "frequently custom made ... lead times ... can be significant": same 10-K, risk factors.
- Competitors Western Digital and Toshiba: same 10-K, Competition.
- "26 per cent more storage ... on similar number of units", December quarter 2025 (190EB, up 26% YoY); nearline "allocated through CY26": Seagate Supplemental Financial Information Q2FY26, 27 Jan 2026. https://s24.q4cdn.com/101481333/files/doc_financials/2026/q2/STX-FQ2-26-Supplemental.pdf
- Allocation "largely allocated through CY27", qualification at cloud customers: Seagate Supplemental Financial Information Q3FY26, 28 Apr 2026. https://s24.q4cdn.com/101481333/files/doc_financials/2026/q3/STX-FQ3-26-Supplemental.pdf
- "the vast majority of our nearline exabytes are now allocated into calendar 2028" (Dave Mosley, CEO, prepared remarks); "We're not really increasing the box count" (Mosley, Q&A); "The gap between supply and demand is now a little bit bigger than a few quarters ago" (Gianluca Romano, CFO, Q&A); Mozaic 4+ "up to 44 TB per drive": Seagate fiscal Q4 2026 earnings call, 28 July 2026. Transcript checked at https://www.marketbeat.com/earnings/reports/2026-7-28-seagate-technology-plc-stock/ (Seagate's own webcast at investors.seagate.com is the record; a fact-checker should confirm the quotes against it).
- Q4 FY2026 results press release, 28/29 July 2026 (8-K): https://www.sec.gov/Archives/edgar/data/1137789/000113778926000153/stxq42026pressreleasefinan.htm
- Western Digital cross-check (not cited in body): Q4 FY2026 results, 5 Aug 2026. https://www.sec.gov/Archives/edgar/data/106040/000162828026053305/a4ex991-pressreleaseq426.htm

## Not verified / left out
- "Inference inflection": not found in Seagate's July 2026 call or its 2026 releases. Closest verified wording: "a new era of structural growth as AI applications amplify data creation" (Q3 FY26 release, 29 Apr 2026). Not used.
- Cost per terabyte versus flash: no primary figure found; stated in words only, consistent with the countertop piece.
- CFO's "units were absolutely flat" with heads and disks up 15 to 20 per cent (28 July call): period ambiguous in the transcript, so not used.
- Exposure map component makers (Resonac disks, Hoya glass blanks, TDK heads) are from general industry knowledge, not Seagate filings; confirm before publish or drop the group.
- Seagate's Q4 FY26 supplemental PDF was not retrievable; Q4 figures come from the 10-K, press release and call.
