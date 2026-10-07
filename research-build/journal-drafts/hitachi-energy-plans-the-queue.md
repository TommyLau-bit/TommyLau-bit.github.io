# Hitachi Energy draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/hitachi-energy-plans-the-queue.md` (draft: true)
Cover: `public/covers/hitachi-energy-plans-the-queue.svg`
Drafted 7 October 2026. Claim needs Tommy's approval before publish.

## Proposed claim

Hitachi Energy is adding factories only as fast as signed orders justify, and its order backlog will stay at or above about 2.5 times annual revenue, roughly three years of work, through fiscal 2030, which ends on 31 March 2031, so the queue for its transformers and HVDC links will not clear.

### Alternatives considered

1. HVDC converter capacity, not transformers, is now the slowest grid queue (Q1 FY2026 Power Grids orders +94% on several large European HVDC awards; HVDC executes over three to four years; capacity reservation agreements such as RWE's). Rejected: Hitachi does not split HVDC from transformers in its backlog, so it cannot be tested on its own disclosures, and the link to AI data centres is indirect.
2. Data centres are escaping the utility transformer queue by buying standardised, containerised grid kit (Hitachi Energy data centre orders +150% in FY2025, target five times FY2024 by FY2027, "fast delivery times and standardization"). Rejected as the lead: absolute data centre order figures are shown only as a chart, and the "escape route" argument overlaps the onsite pieces. Kept as one paragraph.

Chosen because it is new to the site: the-part-money-cannot-hurry and the-queue-not-the-chip argue the transformer sets the pace; this piece shows the world's largest maker saying, in its own plan, that the queue will not clear by 2030 even after $9bn+ of capacity, because capacity follows orders. It is tested on Hitachi's own quarterly figures, and the falsifier is a ratio with a named denominator that stays valid as the business grows. It complements ge-vernova-sells-the-wait (same "the queue is kept" shape, different equipment, and here the company states the ratio itself).

## claims.ts entry

```ts
  {
    id: 'hitachi-energy-plans-the-queue',
    claim: 'Hitachi Energy is adding factories only as fast as signed orders justify, and its order backlog will stay at or above about 2.5 times annual revenue, roughly three years of work, through fiscal 2030, which ends on 31 March 2031, so the queue for its transformers and HVDC links will not clear.',
    breaksIf: 'Hitachi Energy\'s order backlog divided by its revenue over the previous four quarters, both in US dollars as Hitachi reports them (about 3.06 at 30 June 2026), falls below 2.5 at two consecutive quarter ends before 31 March 2031, the end of fiscal 2030; or its orders for any full fiscal year up to fiscal 2030 fall below its revenue for that year.',
    watch: ['Hitachi Energy backlog divided by trailing four quarters of revenue, each quarter', 'Hitachi Energy annual orders against annual revenue', 'Whether the South Boston, Virginia (2028) and Mississippi (2029) transformer plants start on time', 'Hitachi Energy\'s published delivery times for its own transformer components, including the 140 weeks quoted for some Ludvika bushings', 'Whether Hitachi announces capacity ahead of signed orders'],
  },
```

## stack.ts

Layer `grid` ("The grid connection"). Suggested position after `the-part-money-cannot-hurry`, which it builds on:
`pieces: ['the-queue-not-the-chip', 'the-part-money-cannot-hurry', 'hitachi-energy-plans-the-queue', 'two-governments-one-confession', 'the-power-it-drops']`

## Glossary (heading: "Getting power to the building")

- `HVDC`: High voltage direct current. A way of carrying very large amounts of power over long distances or under the sea with less loss than alternating current. Each link needs a converter station at either end and takes years to build.
- `Bushing`: The insulated sleeve that carries a high voltage conductor through the earthed steel tank of a transformer. A specialist component with its own waiting list.
- `Capacity reservation`: An agreement in which a buyer books a manufacturer's future factory or engineering capacity before placing firm orders for specific equipment. The grid equipment cousin of a slot reservation agreement.
- `Framework agreement`: A multi-year supply deal that sets terms and an upper value in advance, with individual orders called off under it as projects firm up.

Existing entries already cover transformer (the grid kind), switchgear, substation, backlog, book-to-bill, lead time, grain-oriented electrical steel.

## numbers.ts (time-based; flag if Tommy prefers purely physical figures only)

```ts
  { layer: 'grid', value: '~3 years', what: 'Orders Hitachi Energy, the largest maker of grid transformers, has signed but not yet delivered, $63.6 billion, against its revenue over the previous four quarters. It plans to keep this at 2.5 to 3 times through 2030. A proxy for the queue, not a lead time.', piece: 'hitachi-energy-plans-the-queue', asOf: '30 June 2026' },
```

Optional second, physical: `{ layer: 'grid', value: '140 weeks', what: 'Delivery time Hitachi Energy quotes for some of its high voltage transformer bushings from its Ludvika plant in Sweden. Even one component of a large transformer has a wait of over two and a half years.', piece: 'hitachi-energy-plans-the-queue', asOf: '6 October 2026' }`

## LinkedIn post (§9)

```
Hitachi Energy is spending more than $9 billion on factories, and it still expects about three years of orders to be waiting in 2030.

It is the largest maker of the transformers and long-distance power links that connect data centres and power stations to the grid. Its unfilled orders reached $63.6 billion in June, about three years of sales, and it told investors that ratio should stay at two and a half to three times while its output nearly doubles. For anyone waiting on a substation, that is the plan for how long the queue lasts.

The piece covers what Hitachi Energy makes, how its queue is measured in years, and why its new factories keep the queue rather than clear it.

https://thephysicallayer.fyi/journal/hitachi-energy-plans-the-queue/

#Transformers #DataCentres #EnergyInfrastructure
```

## Fact-check changes (7 October 2026)

Claim restated as a floor (at or above about 2.5 times revenue) so claim and falsifier test the same thing; the June 2026 ratio of 3.06 is already above Hitachi's stated 2.5 to 3 range. Window runs to 31 March 2031, the end of fiscal 2030. Piece notes the US$100bn 2030 figure includes framework agreements and capacity reservations and that plan figures are at Hitachi's budget rate. Title now says "more than $9 billion on factories" (the total includes about $3bn spent 2020 to 2023). Cover uses the reported $57.9bn and plan figures labelled as such. Bushing range corrected to 245 to 550 kV.

## Arithmetic (my own, from Hitachi disclosures, US dollars)

Hitachi Energy revenue: FY2024 15.7bn (19.8 less 4.1 YoY increase); FY2025 19.8bn. Quarterly: Q1 FY25 4.41 (5.40 less 0.99 YoY increase); Q2 FY25 4.8; Q3 FY25 5.3; Q4 FY25 5.29 (19.8 less the first three quarters); Q1 FY26 5.40. Trailing four quarters at 30 June 2026: 20.79.
Hitachi Energy backlog: end FY2024 ~43.5bn (57.9 / 1.33; also 49.7 / 1.14 = 43.6); 30 Sep 2025 49.7; 31 Dec 2025 56.7; 31 Mar 2026 57.9; 30 Jun 2026 63.6.
Backlog / trailing revenue: Mar 2025 2.77; Mar 2026 2.92; Jun 2026 3.06. FY2030 plan: ~100 / 36 = 2.78.
FY2025 orders / revenue: 32.8 / 19.8 = 1.66 (FY2024: 27.9 / 15.7 = 1.78).
Caveats: USD backlog includes euro and other currency contracts translated at period rates, so FX moves the ratio; quarterly revenue figures are rounded to 0.1bn in the decks; the June 2026 ratio is already slightly above Hitachi's stated 2.5 to 3 range; the 2030 backlog figure includes framework agreements and capacity reservations per Schierenbeck, so the reported quarterly backlog may be on a narrower basis.

## Sources (every figure)

- Hitachi, Outline of Consolidated Financial Results for FY2025 (year ended 31 March 2026), 27 April 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/04/260427/2025_Anpre.pdf
  - p8 "The Business of Hitachi Energy": revenue $19.8bn FY25 (+26%); orders $32.8bn FY25, $27.9bn FY24 (nominal); backlog $57.9bn; FY23 to 25 capex $2.6bn; "Lead time from order to revenues" chart (products to about year 3, systems to year 6, services to about year 2: my reading of the chart); backlog conversion bands FY26, FY27, after FY28.
  - p16: Hitachi Energy backlog 57.9bn USD (+33% vs end FY2024).
  - Hitachi Energy revenue 19.8 BUSD (YoY +4.1 BUSD).
- Hitachi, Outline of Consolidated Financial Results for Q1 FY2026, 29 July 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/07/260729/2026_1Qpre.pdf
  - Hitachi Energy backlog 63.6bn USD (+10% vs end FY2025); Q1 revenue 5.40 BUSD (+0.99 / +22%); FY2026 forecast 23.65 BUSD; Power Grids orders ¥1,871.6bn (+94%), "several large HVDC project awards in Europe"; FY2026 group capex ¥670bn "primarily in Energy's Power Grids business".
- Hitachi, Outline of Consolidated Financial Results for Q3 FY2025, 29 January 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/articles/2026/01/260129/2025_3Qpre.pdf
  - Backlog 56.7bn USD; Q3 revenue 5.3 BUSD.
- Hitachi, Outline of Consolidated Financial Results for Q2 FY2025, 30 October 2025: https://www.hitachi.com/New/cnews/month/2025/10/251030/2025_2Qpre.pdf
  - Backlog 49.7bn USD (+14% vs end FY2024); Q2 revenue 4.8 BUSD.
- Hitachi Investor Day 2026, Energy Business Strategy (Andreas Schierenbeck), 10 June 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/06/260610/20260610_01_energy_en.pdf
  - p9: installed 1 of 6 transformers and 1 in 4 HV switchgear in the world, >175 GW HVDC, #1 share (internal estimates). p10: backlog ~11 (FY2020), ~60 (FY2025), ~100 (FY2030) BUSD; revenue 9, 20, 36 BUSD; "Order backlog to revenue ratio expected to remain stable at 2.5-3x, execution is key"; "investments in bankable business cases". p11: $3B (2020 to 2023), >$6B (2024 to 2027), >$9B total; North America >$2B, Europe >$1.8B, India $450M, China $300M, South America $200M; ">40 brownfield & greenfield factories". p13: data centre order growth >150% FY2025. p17: data centre orders 5x FY2024 by FY2027; "fast delivery times and standardization (e.g. containerized or SST 800V)".
- Hitachi Investor Day 2026 Q&A summary, 10 June 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/06/260610/20260610_06_qa_session_en.pdf
  - Schierenbeck: HVDC "normally cover three to four years in execution"; "we are forecasting for 2030 a backlog of around 100 billion, including framework agreements and capacity reservations"; "we are only investing if we have a bankable business case"; "we are not building over-capacity". (Hitachi's published summary, translated; not a verbatim transcript.)
- Hitachi Integrated Report 2026: https://www.hitachi.com/content/dam/hitachi/global/en/ir/media/library/integrated/2026/ar2026e.pdf
  - Backlog "approximately 3 times annual revenues and is expected to remain at 2.5 to 3 times revenues going forward"; "over 9 billion dollars in investments"; "more than 40 projects globally"; data centre orders "increased by more than 150% year over year in fiscal 2025".
- Hitachi Energy, E.ON framework agreement, 28 July 2025: https://www.hitachienergy.com/news-and-events/press-releases/2025/07/hitachi-energy-and-e-on-sign-deal-worth-up-to-700-million-usd-for-critical-grid-infrastructure-to-bolster-energy-security-and-resilience-in-germany
  - Up to $700m; "will deliver a considerable part of the transformers by reserving manufacturing capacity".
- Hitachi Energy, South Boston groundbreaking, 29 June 2026: https://www.hitachienergy.com/us/en/news-and-events/press-releases/2026/06/hitachi-energy-breaks-ground-on-the-nation-s-largest-facility-for-the-production-of-large-power-transformers-in-south-boston-virginia
  - $457m, large power transformers, ~825 jobs.
- Manufacturing Dive, September 2025 (exact day not checked): https://www.manufacturingdive.com/news/hitachi-unveils-1b-grid-manufacturing-investment-virginia-transformer/759512/
  - Hitachi's Kurt Steinert: South Boston "should be operational by 2028". (Original Hitachi announcement 4 September 2025: https://www.hitachi.com/en-us/press/hitachi-announces-historic-1-billion-usd-manufacturing-investment-to-power-americas-energy-future/ gives no start date.)
- Hitachi Energy, Mississippi factory, 15 September 2026: https://www.hitachienergy.com/us/en/news-and-events/press-releases/2026/09/hitachi-deepens-commitment-to-u-s-manufacturing-with-528-million-mississippi-transformer-factory
  - $528m, Gallman; "transformer production at the facility scheduled to start in 2029"; "will more than double capacity".
- Hitachi Energy, Delivery times for transformer components (Ludvika updated 6 October 2026): https://www.hitachienergy.com/us/en/products-and-solutions/insulation-and-components/transformer-insulation-components/delivery-times-for-transformer-components
  - GSBK and ARF 245 to 550 kV bushings (ARF 245, 300, 362, 420, 550): 140 weeks.

## Could not verify / left out

- No Hitachi Energy figure for its own large power transformer lead time. Nikkei (25 March 2026) headlined waits of more than 30 months, and Manufacturing Dive cites up to three years industry-wide, but neither quotes Hitachi Energy, so the piece gives no transformer lead time.
- The order-to-revenue horizons (about three years for products, up to six for systems) are my reading of a chart without numeric labels; the piece says so.
- The investor day Q&A quotes come from Hitachi's published summary, which is translated and edited, not a verbatim transcript. Check against the webcast if possible.
- The Q1 FY2026 call quotes (CFO Kato on transformers and switchgear being "extremely strong") came only from third-party transcripts; left out.
- RWE HVDC capacity reservation agreement: found in search snippets only, not fetched; left out of the piece.
- Wayback Machine was offline, so I could not check how the 140-week bushing delivery time has moved over time.
- That Hitachi Energy is the world's largest maker is Hitachi's own internal market share estimate; the summary says "by its own estimate".
