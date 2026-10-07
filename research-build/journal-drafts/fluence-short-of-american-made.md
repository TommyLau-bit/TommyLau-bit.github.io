# Fluence draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/fluence-short-of-american-made.md` (draft: true)
Cover: `public/covers/fluence-short-of-american-made.svg`
Drafted 7 October 2026. Claim needs Tommy's approval before publish.

## Proposed claim

Through fiscal 2027, Fluence's American deliveries, where its data centre orders sit, will be limited by how fast it can make systems that count as American-made, not by demand.

### Alternatives considered

1. Fluence's data centre orders confirm that grid batteries are now bought as connection equipment. Rejected as the lead: the evidence only half supports it. Data centres are about a tenth of Fluence's storage pipeline (16 of 163.7 GWh), so it would overstate. Kept as one section, which openly corrects the size claim in what-the-battery-is-really-for.
2. Fluence's gross margin collapse (5.1% vs 14.8%) shows that customers pay for a date and claw it back as liquidated damages when it slips. Rejected as the lead: margin is also hit by new-product overruns and cell prices, so it cannot carry the claim alone. Kept as evidence.

Chosen because it is new to the site (the tax rules make "made in America" the scarce input, not cells or demand), it is tested directly in Fluence's own disclosures (Fluence says it will publish US production, actual and forecast, and a FY2027 plan with FY2026 results), and it avoids the backlog device used by the five sibling drafts.

## claims.ts entry

```ts
  {
    id: 'fluence-short-of-american-made',
    claim: 'Through fiscal 2027, Fluence\'s American deliveries, where its data centre orders sit, will be limited by how fast it can make systems that count as American-made, not by demand.',
    breaksIf: 'Fluence\'s published American production figures show Houston at about 11 units a day, or a 15 GWh a year pace, by the end of March 2027, and its plan for the year to September 2027 is not cut again for American production, or American orders fall while its American lines have spare capacity.',
    watch: ['Houston units a day and US run-rate in Fluence\'s published US production figures', 'Any further cut to the fiscal 2027 plan for American production', 'Liquidated damages and gross margin in each quarterly filing', 'Whether the $550 million hyperscaler award becomes a signed order'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"). Place directly after `what-the-battery-is-really-for`, which it tests:
`pieces: ['the-way-out-has-its-own-queue', ..., 'what-the-battery-is-really-for', 'fluence-short-of-american-made', 'oklo-sells-the-electricity']`
(Keep whatever ge-vernova-sells-the-wait placement is decided for that draft.)

## Glossary (heading: "Getting power to the building")

- `Battery integrator`: A company that designs a complete grid battery system, buys the cells and other parts, has contract factories assemble them and runs the control software. Fluence and Tesla Energy are examples. It does not make the cells.
- `Domestic content bonus`: A larger American tax credit for a power or storage project when enough of its equipment is made in the United States. It makes where a battery system was built part of what the buyer is paying for.
- `Prohibited foreign entity`: The American tax law's term for, in short, companies tied to China, Russia, Iran or North Korea. From 2026, projects claiming clean energy tax credits must limit material from them, and the limit tightens each year.
- `Liquidated damages`: Penalties fixed in a contract in advance, paid when a supplier misses a delivery milestone. Used on this site only as evidence of what a delay is worth to the buyer.

(Existing `BESS`, `Behind the meter` and `Inverter` entries already fit.)

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '11 vs under 1', what: 'Battery systems a day Fluence\'s Houston plant was meant to produce in August 2026, against what it actually averaged. The American-made kind is the scarce kind.', piece: 'fluence-short-of-american-made', asOf: 'September 2026' },
```

Alternative if a company-primary figure is preferred: `{ layer: 'onsite', value: '15 GWh', what: 'Planned yearly capacity of the Houston plant that assembles Fluence\'s American-made battery systems.', piece: 'fluence-short-of-american-made', asOf: 'August 2026' }`

## LinkedIn post (§9)

```
Fluence's new Houston battery factory spent this summer running on generators, because its own grid connection was late.

Fluence sells data centres a way to switch on before their grid connection is ready. Its overseas factories are working well, by its own account, but American tax rules reward systems made in America, and the Houston line averaged under one unit a day in August against a plan of eleven. In the United States the scarce thing is not the battery, it is the battery that qualifies.

The piece covers how the tax rules turn "made in America" into the constraint, what data centre buyers are actually paying Fluence for, and the test that would prove me wrong.

https://thephysicallayer.fyi/journal/fluence-short-of-american-made/

#EnergyStorage #DataCentres #EnergyInfrastructure
```

## Sources (every figure)

- Fluence 3Q FY2026 results release (8-K exhibit 99.1), 5 August 2026: https://www.sec.gov/Archives/edgar/data/1868941/000186894126000028/flncq3fy26earningspressrel.htm
  - Revenue ~$649.8m; GAAP gross margin ~5.1% vs ~14.8%; ~$850m data centre business through July incl. first large behind-the-meter order and ~$550m hyperscaler awards in July; FY2026 revenue guidance cut to $2.9 to $3.1bn (midpoint $3.0bn) from $3.2 to $3.6bn (midpoint $3.4bn); $400m of deliveries pushed to FY2027 due to an international CM facility and "construction related delays that affected the completion and start-up of a new U.S. contract manufacturing facility".
- Fluence 3Q FY2026 earnings call, 6 August 2026 (also: $2.7bn orders signed through 3Q, utilities and IPPs ~90%; one of two new China facilities needed quality rework, now at full production in 4Q) (transcript as published by The Motley Fool, 12 August 2026): https://www.fool.com/earnings/call-transcripts/2026/08/12/fluence-energy-flnc-q3-2026-earnings-call-transcript/
  - Houston: fully automated, expected capacity 15 GWh/yr, Fluence is off-taker, construction and automation delays, "we've been running the plant with generators ... we could not do all the works in parallel", grid connection "in the next couple of weeks"; full production expected fiscal 1Q 2027; Houston "will expand our annual capacity for domestic content significantly"; data centre pipeline 16 GWh, up more than 35% on 2Q; $300m behind-the-meter order with a developer, lead to order in 3 months / "less than 3 months"; developers "speed to power", hyperscalers "quality of power solutions"; operating system's ability to "smooth loads and handle periods of low voltage have contributed to new awards and orders"; $550m awards "are not yet purchase orders"; data centre systems 2-hour duration; "the other 90% today or our other segments" (garbled transcript; denominator not stated); CFO: 4Q deliveries "mostly in the U.S., and that's mostly the deliveries that we have under our domestic content". Note: the transcript mislabels the CEO as "Julian Jose Marquez"; the CEO is Julian Nebreda.
- Fluence Form 10-Q for the quarter ended 30 June 2026, filed 5 August 2026: https://www.sec.gov/Archives/edgar/data/1868941/000186894126000029/flnc-20260630.htm
  - Liquidated damages definition (accounted as variable consideration reducing contract price); revenue offset by LDs from project delays; gross profit decline due to LDs, cost overruns on newer offerings (incl. US-produced projects), higher battery prices; storage pipeline 163.7 GWh (45.6 GW) at 30 June 2026; PFE compliance belief citing Treasury guidance of 12 February 2026; Houston named among contract manufacturer facilities being scaled.
- Fluence 8-K, 16 September 2026, exhibit 99.1 (revised guidance): https://www.sec.gov/Archives/edgar/data/1868941/000110465926108270/tm2625477d1_ex99-1.htm
  - FY2026 revenue ~$2.4bn vs prior midpoint ~$3.0bn; adjusted EBITDA loss ~$200m; "Demand for our products has remained strong both domestically and internationally, and our international supply chain has continued to work well"; Houston ramp delays "the primary reason"; plan to provide FY2027 business plan with FY2026 results; forward-looking list includes "plans relating to reporting U.S. production levels in the future, both actual and forecast".
- Fluence 8-K exhibit 99.2, 16 September 2026 (COO appointment), background only: https://www.sec.gov/Archives/edgar/data/1868941/000110465926108270/tm2625477d1_ex99-2.htm
- Latitude Media, "What's going on with Fluence?", 21 September 2026: https://www.latitudemedia.com/news/whats-going-on-with-fluence/
  - Reports the 16 September call: 11 units/day assumed for Aug to Sep; under 1/day in August; 3/day early September; automated welding below target; manual welding.
- BEST Magazine, "Welding problems at US plant force Fluence to cut revenue forecast by $600m", September 2026 (corrected 24 September 2026): https://www.bestmag.co.uk/welding-problems-fluence-cut-revenue-forecast/
  - Same rates; more than 80% of the reduction attributable to US production (the piece says "about 80 per cent" because sources differ); facility does enclosure welding and final assembly, Fluence is off-taker; grid connection expected fiscal 1Q 2027, generators installed.
- Fluence Form 10-K for the year ended 30 September 2025, filed 25 November 2025: https://www.sec.gov/Archives/edgar/data/1868941/000186894125000081/flnc-20250930.htm
  - Fiscal year ends 30 September (verified); US supply chain in Arizona, Texas, Tennessee, South Carolina and Utah; Utah module production from September 2024 using Tennessee-made cells; ITC domestic content bonus thresholds raised by OBBBA; PFE "material assistance" rules for ITC projects starting construction in 2026 and after, rising annually; Section 301 tariff on Chinese non-EV lithium-ion batteries 7.5% to 25% from 1 January 2026; risk factor that competitors may offer US domestic content "in greater quantity, with better pricing, and on a faster timeline"; Arizona contract manufacturer delays in FY2025 from labour availability and training lead times.

## Could not verify / flags for the fact-checker

- The 16 September call transcript itself was not accessible (Seeking Alpha paywall, Fluence IR blocked). The units-a-day figures, the welding detail and the "more than 80 per cent" share come from consistent trade press reports of the call (Latitude Media, BEST Magazine, mgrid.org). The piece attributes them "as reported by several trade publications". Verify against the replay before publishing.
- "Companies tied to China, Russia, Iran or North Korea" is my summary of the OBBBA prohibited foreign entity definition, not Fluence's wording.
- "An American buyer who wants the larger credit cannot be served from Vietnam or China" is labelled in the piece as my reading.
- 16 GWh data centre pipeline vs 163.7 GWh total storage pipeline: possibly different bases (call vs 10-Q). The piece says so and labels "under a tenth" as my arithmetic.
- Fixed after fact-check: the piece now uses the CEO's prepared remark that of $2.7bn of orders signed in the nine months to 30 June 2026, "utilities and IPPs making up approximately 90% of this total" (Motley Fool transcript, 6 August call).
- Whether Houston actually reached grid connection or full production after mid-September: not disclosed yet.
- Left out: the reported ~$56m late-delivery penalties and $25m corrective cost (secondary only); the EVE Energy 206 GWh supply deal (secondary only, international market); AESC as named cell supplier (only in an analyst question).

## Fact-check fixes applied 7 October 2026

1. 90 per cent now refers to utilities and IPPs in $2.7bn of 9M orders. 2. Added the China line rework as part of the August cut. 3. "About 80 per cent". 4. By 16 September, generators in place and power no longer constraining; welding the limit. 5. PFE definition labelled "in short". 6. Falsifier names ~11 units a day or 15 GWh/yr pace in published US production figures. 7. Unit figures attributed to trade press reports of the 16 September call. 8. Cover caption moved inside frame (y=478, diagram shifted up 14px).
