# Siemens Energy draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/siemens-energy-measures-the-shortage.md` (draft: true)
Cover: `public/covers/siemens-energy-measures-the-shortage.svg`
Drafted 7 October 2026. Claim needs Tommy's approval before publish.

Latest Siemens Energy disclosure used: Q3 FY2026 earnings release (quarter to 30 June 2026), published 5 August 2026. Full-year FY2026 results (year to 30 September 2026) are due in November 2026 and will give the next data point.

## Proposed claim

By Siemens Energy's own estimate, demand for large and medium power transformers in Europe and North America exceeds the combined capacity of all market players in the region in every year through its fiscal 2030, which ends on 30 September 2030, so unfilled orders keep accumulating even as the gap narrows: Grid Technologies' orders stay above its revenue each fiscal year and its backlog in euros keeps growing.

Second fact-check fixes (7 October 2026): €600m and ~€2bn described as transformer and switchgear capex; Q3 wording now "largest contribution to Grid's order growth"; Gamesa weak orders attributed to the prior-year offshore comparison (two orders over €3bn), quality point removed; caveat that the chart's capacity may count only factories in the region, so imports could fill part of the gap; one sentence that the tests use global Grid figures (about 38% HVDC and offshore) as a stand-in for the chart, so HVDC lumpiness can move them either way; Gas caveat on older lower-priced orders; backlog definition reworded; cover widened to x 690.

Reworked 7 October 2026 after first fact-check: the claim is now about the absolute backlog (the pile), not backlog divided by revenue. On the chart's own numbers the years-of-sales ratio can fall (about 4 years with a 10% gap and ~6% a year capacity growth gives (4 + 0.1)/1.06 = 3.9), so the piece says explicitly that the wait in years may shorten while the pile grows.

### Alternatives considered

1. Grid equipment, not gas turbines, carries Siemens Energy's biggest scarcity premium: Grid Technologies out-earns Gas Services (9M FY26 margin before SI 18.3% vs 16.6%) with about 95% of its revenue from new equipment, against 60% service at Gas, and will stay ahead through FY2028. Rejected as the lead: management targets the same 18 to 20% for both in FY2028, Gas Services is still working off older low-priced turbine orders, so the comparison tests repricing lag as much as scarcity. Kept as evidence in "Grid against gas, inside one company", with the caveat that Gas Services is still working off older, lower-priced turbine orders.
2. Grid margins are a delayed echo of the queue: Siemens Energy credits the "improved margin profile of the processed order backlog", and the FY2028 Grid margin target (13 to 15% reported, set Nov 2024) was reached in FY2026 guidance (18 to 20% before SI). Rejected as the lead: a margin forecast sits too close to a view on the shares and is hard to falsify on the physical mechanism. Kept as one paragraph.

Caveat on the chart: "all market players" in Europe and North America may count only factories in the region, so imports could fill part of the gap; the piece flags this as part of my own reading.

Chosen because it is new to the site: Siemens Energy has published an industry-wide demand and capacity estimate for transformers (all makers, Europe and North America, in GVA), which no other piece uses. The new argument is that a narrowing gap still adds to the pile of unfilled orders every year, correctly limited to the absolute backlog. The Grid versus Gas Services contrast inside one company (94.8% new units vs 60% service; 18.3% vs 16.6% margin) is the second distinct strand. It does not use the years-of-sales ratio that hitachi-energy-plans-the-queue and eaton-order-book-outruns-it rest on. Tested on Siemens Energy's own figures: annual Grid orders against revenue, quarterly Grid backlog in euros, and any revision of the chart.

## claims.ts entry

```ts
  {
    id: 'siemens-energy-measures-the-shortage',
    claim: 'By Siemens Energy\'s own estimate, demand for large and medium power transformers in Europe and North America exceeds the combined capacity of all market players in the region in every year through its fiscal 2030, which ends on 30 September 2030, so unfilled orders keep accumulating even as the gap narrows: Grid Technologies\' orders stay above its revenue each fiscal year and its backlog in euros keeps growing.',
    breaksIf: 'Before 30 September 2030: Grid Technologies\' orders fall below its revenue for any full fiscal year; or its order backlog in euros, as Siemens Energy reports it (€51bn at 30 June 2026), falls for two consecutive quarters; or Siemens Energy publishes a revised estimate showing transformer capacity meeting demand in Europe and North America before fiscal 2030.',
    watch: ['Grid Technologies orders against revenue, each fiscal year', 'Grid Technologies backlog in euros, each quarter', 'Whether the Charlotte large power transformer plant ships in 2027 and the Nuremberg expansion opens by 2028', 'Whether Siemens Energy updates its transformer market and capacity chart'],
  },
```

## stack.ts

Layer `grid` ("The grid connection"). Suggested position after `hitachi-energy-plans-the-queue` if that is published first, otherwise after `the-part-money-cannot-hurry`:
`pieces: ['the-queue-not-the-chip', 'the-part-money-cannot-hurry', 'hitachi-energy-plans-the-queue', 'siemens-energy-measures-the-shortage', 'two-governments-one-confession', 'the-power-it-drops']`

## Glossary (heading: "Getting power to the building")

- `GVA`: Gigavolt-ampere, a thousand MVA. The unit for how much power a transformer can carry, and the unit Siemens Energy uses to measure transformer demand and factory capacity.
- `HVDC` (only if not already added with the Hitachi Energy piece): High voltage direct current. A way of carrying very large amounts of power over long distances or under the sea with less loss than alternating current. Each link needs a converter station at either end and takes years to build.
- `Profit margin before special items`: Profit before one-off costs such as restructuring, as a share of revenue. Siemens Energy's main measure of how profitable each business is. Used on this site only as evidence of pricing power. (Heading: the one holding Gross margin and Adjusted operating margin.)
- `Capital markets day`: A briefing where a company sets out its plans and targets to investors, usually every few years. (Same heading as the margin terms.)

Existing entries already cover transformer (the grid kind), switchgear, substation, backlog, book-to-bill, lead time, MVA.

## numbers.ts

Physical:

```ts
  { layer: 'grid', value: '~40% → ~10%', what: 'How far demand for large and medium power transformers in Europe and North America runs ahead of the combined capacity of all market players in the region, in GVA, by Siemens Energy\'s estimate: about 40 per cent in fiscal 2025, still about 10 per cent in fiscal 2030, after industry capacity nearly doubles from fiscal 2023 (about 60 per cent more than fiscal 2025).', piece: 'siemens-energy-measures-the-shortage', asOf: '20 November 2025' },
```

Optional, absolute backlog (flag if Tommy prefers physical only):
`{ layer: 'grid', value: '€51bn', what: 'Orders Siemens Energy\'s grid business has signed but not yet delivered, up from €33bn in September 2024 while its revenue grew about 40 per cent.', piece: 'siemens-energy-measures-the-shortage', asOf: '30 June 2026' }`

## LinkedIn post (§9)

```
Siemens Energy has published its own estimate of the transformer shortage, and on its chart demand is still ahead of every factory in 2030.

It covers what Siemens Energy calls all market players for large power transformers in Europe and North America. Demand ran about 40 per cent ahead of capacity in 2025 and is still about 10 per cent ahead in 2030, even after capacity grows by about 60 per cent. A smaller shortage still adds to the pile of unfilled orders each year, and Siemens Energy's own grid backlog has grown from €33 billion to €51 billion in under two years.

The piece covers what the chart shows, why a narrowing gap still adds to the pile, and why Siemens Energy's grid business now out-earns its gas turbines.

https://thephysicallayer.fyi/journal/siemens-energy-measures-the-shortage/

#Transformers #DataCentres #EnergyInfrastructure
```

## Arithmetic (my own, from Siemens Energy disclosures, euros as reported)

Grid Technologies revenue: FY2024 9.28bn (Q4 FY24 letter); FY2025 11.305bn; quarterly Q1 FY25 2.480, Q2 FY25 2.861, Q3 FY25 2.819, Q4 FY25 3.145, Q1 FY26 3.054, Q2 FY26 3.067, Q3 FY26 3.624 (Q4 FY25 = 11.305 less 8.160 nine-month = 3.145, matches the Q4 letter).
Trailing four quarters at 30 June 2026: 3.145 + 3.054 + 3.067 + 3.624 = 12.890bn.
Grid backlog: 30 Sep 2024 €33bn; 30 Sep 2025 €42bn; 31 Dec 2025 €45bn; 31 Mar 2026 €49bn; 30 Jun 2026 €51bn (all rounded to €1bn in the releases).
Backlog / trailing revenue (no longer used in the piece or claim): Sep 2024 33/9.28 = 3.56; Sep 2025 42/11.305 = 3.72; Dec 2025 45/11.879 = 3.79; Mar 2026 49/12.085 = 4.05; Jun 2026 51/12.890 = 3.96.
Revenue growth FY2024 to trailing June 2026: 12.890/9.28 = +39%.
9M FY26 Grid book-to-bill: 18.328/9.744 = 1.88.
Products backlog estimate: €16bn (CMD, as of Q4 FY25) against products revenue of about €5.1bn (transformers ~30% + switchgear ~15% of €11.3bn FY25 third-party revenue) = ~3.1 years. My estimate.
Revenue mix 9M FY26 (external): Grid new units 9,040 / (9,040 + 498) = 94.8%; Gas service 6,084 / (4,050 + 6,084) = 60.0%.
Chart reading (CMD Grid deck p7, indexed to FY23 capacity = 100%, measured from the pixel positions of the rendered slide): capacity ~100 / ~116 / ~168 / ~188; market ~119 / ~163 / ~194 / ~210 for FY23 / FY25 / FY28 / FY30. Implied gaps ~41% (FY25) and ~12% (FY30) against labelled ~40% and ~10%. Only the gap labels are Siemens Energy's figures; the rest is my reading, and the piece says so.
Caveats: backlog figures are rounded to €1bn, so the ratio moves about ±0.04 on rounding alone; euro reporting means dollar orders shrink on paper when the dollar weakens; HVDC & offshore are 66% of the €24bn solutions backlog with 5 to 7 year average reach, so mix can hold the ratio up; the chart covers Europe and North America power transformers only, while the Grid backlog is global and includes HVDC, substations and switchgear; my inference that a positive gap means the queue still grows assumes "market" is yearly demand and the bars yearly output, which the slide does not state.

## Sources (every figure)

- Siemens Energy, Capital Market Day 2025, Grid Technologies presentation (Tim Holt), 20 November 2025: https://assets.siemens-energy.com/dam/d8d5d849-a7a9-4b19-a969-b39b004f6c26/251120_CMD-2025_Grid_Technologies_FINAL-pdf_Original%20file.pdf
  - p3: backlog €42bn (products €16bn, solutions €24bn, digital and service €2bn) as per Q4 FY25; ~20% of all power transformers and ~30% of all HVDCs in global installations.
  - p6: solutions backlog split, HVDC & offshore 66% (average reach 5 to 7 years), substations 21% (2 to 3 years), grid stabilisation 13% (3 to 4 years).
  - p7: "Market remains tight… example: power transformers"; market/capacity gap ~40% (FY25), ~10% (FY30); footnote: large and medium power transformers in Europe and North America, all market players, Siemens Energy internal assessment, in GVA; FY23 to 25 ~€600m investments (~20% additional capacity); FY26 and beyond "Flexible ramp-up plan (~2x capacity)"; further ~€2bn into factory network by FY28 (capex for transformers and switchgear incl. real estate).
  - p10: FY28 targets: margin before SI 18 to 20%, revenue CAGR high-teens.
  - p12: Grid margin before SI FY22 3.6%, FY23 7.6%, FY24 10.5%, FY25 15.8%; revenue FY22 to FY25 6.3, 7.2, 9.3, 11.3bn; FY26 guidance 16 to 18% (as at Nov 2025).
  - p13: FY25 revenue shares: transformers ~30%, switchgear ~15%, HVDC & offshore ~25%, substations ~20%, grid stabilisation ~5%, digital & service ~5%.
- Siemens Energy, Capital Market Day 2025, Gas Services presentation (Karim Amin), 20 November 2025: https://assets.siemens-energy.com/dam/5fc093ca-4fd8-482c-8390-b39b004f66f3/251120_CMD-2025_Gas_Services_FINAL-pdf_Original%20file.pdf (FY28 Gas margin target 18 to 20%; capacity sold out until FY28; used for the alternatives, not cited in the piece).
- Siemens Energy, Capital Market Day 2025, CEO presentation, 20 November 2025: https://assets.siemens-energy.com/dam/e79f8fab-3911-40bb-9297-b39b003ffd7f/251120_CMD-2025_CEO_FINAL-pdf_Original%20file.pdf (capacity expansion +30 to 50% in power transformers and medium and large gas turbines, FY26 to 28; not cited in the piece).
- Siemens Energy, Shareholder Letter Q4 FY2025 (results 14 November 2025, CMD 20 November 2025): https://assets.siemens-energy.com/dam/9478ef65-c3f9-49de-97b0-b3aa00d5712d/2025-11-14--Shareholder-Letter-Q4-FY2025-EN_final-pdf_Original%20file.pdf
  - FY2025 Grid orders €21,423m, revenue €11,305m, margin before SI 15.8%; Gas Services 13.0%; Siemens Gamesa (13.1)%; Grid backlog "quadrupled since FY21 to €42bn"; "every fifth power transformer and even 30% of all HVDCs installed worldwide"; "investing over €2bn to expand transformer and switchgear capacity"; FY28 Grid target 18 to 20%.
- Siemens Energy, Shareholder Letter Q4 FY2024, 13 November 2024: https://assets.siemens-energy.com/dam/17e152fd-ddd4-4c4f-883f-b22e01021076/2024-11-13-Shareholder-Letter-Q4-FY2024-EN_final-pdf_Original%20file.pdf
  - FY2024 Grid revenue €9,280m, margin before SI 10.5%; Grid backlog €33bn as of 30 September 2024; FY28 Grid target "Margin reported" 13 to 15%.
- Siemens Energy, Earnings Release Q1 FY2026, 11 February 2026: https://assets.siemens-energy.com/dam/eb218e11-1294-4e27-a750-b3ee0059367f/Earnings-Release-Q1-FY26-EN-pdf_Original%20file.pdf
  - Grid orders €5,964m, revenue €3,054m, backlog €45bn; "stronger margin of the processed order backlog"; Gamesa backlog €34bn.
- Siemens Energy, Earnings Release Q2 FY2026, 12 May 2026: https://assets.siemens-energy.com/dam/fb695b3d-e910-4f47-81b5-b4480034f6a1/Earnings-Release-Q2-FY26-EN-pdf_Original%20file.pdf
  - Grid orders €6,996m, revenue €3,067m, backlog €49bn; FY2026 Grid outlook raised to revenue growth 25 to 27% and margin before SI 18 to 20% (from 19 to 21% and 16 to 18%).
- Siemens Energy, Earnings Release Q3 FY2026, 5 August 2026: https://assets.siemens-energy.com/dam/d0147174-31a9-4a78-b062-b49d00428fc4/earnings-release-q3-fy2026-en-pdf_Original%20file.pdf
  - Grid orders €5,367m, revenue €3,624m, margin before SI 19.9%, backlog €51bn; "substantial growth in the transformer business including data center projects"; "improved margin profile of the processed order backlog"; 9M Grid orders €18,328m, revenue €9,744m, margin 18.3%; 9M Gas Services margin 16.6%; 9M external revenue split (Grid new units €9,040m, service €498m; Gas new units €4,050m, service €6,084m); Gamesa 9M orders €3,452m, revenue €7,624m, margin (0.2)%, backlog €31bn.
- Siemens Energy press release, Nuremberg transformer factory, 5 September 2025: https://www.siemens-energy.com/global/en/home/press-releases/siemens-energy-invests--220-million.html
  - €220m; "transformers have been manufactured since 1912"; capacity "by approximately 50 percent"; new areas "expected to be available by 2028".
- Siemens Energy release on Charlotte, 14 February 2024 (per fact-check): first large power transformers "early 2026". City of Charlotte announcement, 13 February 2024: https://www.charlottenc.gov/CS-Prep/City-News/Siemens-Energy-Charlotte-Expansion ($149.9m, large power transformers).
- Reuters, 26 June 2025, via IENE summary 27 June 2025: https://www.iene.eu/energy-news/siemens-energy-targets-us-transformer-production-in-2027-can-further-expand-factory-p7892.html (Tim Holt: first Charlotte LPTs "early 2027"; original Reuters page not fetched by me, confirmed in fact-check).

## Could not verify / left out

- Charlotte slip (early 2026 at announcement, early 2027 per Holt to Reuters) confirmed by the fact-check; I read Reuters only via a syndicated summary.
- "#1 in Products" is Siemens Energy's own ranking; the piece attributes it as such so it does not contradict the Hitachi Energy draft's "largest by its own estimate".
- The chart's capacity and demand index values (115, 170, 190; 165, 195, 210) are my reading of an unlabelled chart; only the ~40% and ~10% gaps are Siemens Energy's labels. The piece says so.
- Siemens Energy does not say whether its "~2x capacity" ramp-up refers to its own transformer capacity or which years; the piece does not use it.
- No Siemens Energy figure for its own transformer delivery times was found; the piece gives no lead time.
- Q3 FY2026 earnings call commentary was not used (no primary transcript checked).
