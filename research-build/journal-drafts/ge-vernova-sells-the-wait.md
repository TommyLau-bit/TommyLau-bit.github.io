# GE Vernova draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/ge-vernova-sells-the-wait.md` (draft: true)
Cover: `public/covers/ge-vernova-sells-the-wait.svg`
Drafted 7 October 2026. Claim needs Tommy's approval before publish.

## Proposed claim

GE Vernova is expanding gas turbine output inside its existing factories, paid for by customers' deposits, so its queue will stay at four or more years of its planned output through 2030 rather than clear.

### Alternatives considered

1. GE Vernova's grid equipment queue (Electrification book-to-bill about 1.7, backlog $40.6bn, up 69%) is now the deeper constraint than its turbine queue. Rejected as the lead: dollars and gigawatts are not comparable, and the transformer argument is already the-part-money-cannot-hurry. Kept as one section.
2. A heavy-duty turbine signed with GE Vernova today makes power in 2032 to 2033, no faster than the grid queue it was meant to skip. Rejected as the lead: it mostly extends the-way-out-has-its-own-queue. Kept as evidence in "The queue, measured in years".

Chosen because it is new to the site (deposits and the existing footprint explain *why* the queue persists), it is tested directly on GE Vernova's own filings (contract liabilities, GW under contract, output steps), and it has a clean numeric falsifier.

## claims.ts entry

```ts
  {
    id: 'ge-vernova-sells-the-wait',
    claim: 'GE Vernova is expanding gas turbine output inside its existing factories, paid for by customers\' deposits, so its queue will stay at four or more years of its planned output through 2030 rather than clear.',
    breaksIf: 'Before 2030, gigawatts under contract fall below four years of the annual output GE Vernova has planned for that year (20 GW now, 24 from 2028, 30 from 2030), or GE Vernova announces a new heavy-duty turbine factory, or Power deposits and price per kilowatt fall while orders stay strong.',
    watch: ['Gigawatts under contract against planned annual output, each quarter', 'Power segment contract liabilities in each filing', 'Whether slot reservations convert into orders or lapse', 'Whether the 24 gigawatt output step lands in 2028'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"). Suggested position: directly after `the-way-out-has-its-own-queue`, which it builds on:
`pieces: ['the-way-out-has-its-own-queue', 'ge-vernova-sells-the-wait', 'the-product-is-time', 'what-the-battery-is-really-for', 'oklo-sells-the-electricity']`

## Glossary (heading: "Getting power to the building")

- `Heavy-duty gas turbine`: The large turbine at the centre of a power station, each producing hundreds of megawatts. Built to order, and the slowest part of building your own power to get hold of.
- `Aeroderivative`: A smaller gas turbine adapted from a jet engine. Less power each, but quicker to ship and switch on, so it is often used as a bridge until a heavy-duty machine arrives.
- `Contract liabilities`: Cash a company has collected from customers for equipment it has not yet delivered. Used on this site only as evidence: deposits rising ahead of deliveries mean buyers are paying to hold a place.
- `Castings and forgings`: The large shaped metal parts at the hot heart of a turbine, made by a small number of specialist suppliers. Their arrival sets how fast turbine output can step up.

The existing "Slot reservation agreement" entry already fits; no change needed. Optionally add "paid" to its first sentence ("A paid commitment to a future manufacturing slot") since the 10-Q confirms down payments on SRAs.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '~6 years', what: 'Gas turbine capacity GE Vernova has under contract, 116 gigawatts, against its output of 20 gigawatts a year. The queue for building your own power, measured in factory time.', piece: 'ge-vernova-sells-the-wait', asOf: '30 June 2026' },
```

Optional second: `{ layer: 'onsite', value: '18 months', what: 'Time a heavy-duty gas turbine can take to commission at site after leaving the factory, by GE Vernova\'s account. A turbine shipped in 2031 makes power in 2033.', piece: 'ge-vernova-sells-the-wait', asOf: 'July 2026' }`

Note: the existing '116 GW' entry (the-way-out-has-its-own-queue, asOf 1 September 2026) stays as is.

## LinkedIn post (§9)

```
GE Vernova signed 41 gigawatts of gas turbine contracts in the first half of 2026 and shipped seven.

Most of those contracts are paid places in a queue for 2030 and 2031, and customers have handed over billions in deposits to hold them. GE Vernova is using that money to stretch the factories it already has, not to build new ones. For anyone planning to skip the grid queue with their own power, that is the number that sets the date.

The piece covers what a slot reservation is, where the deposits show up in GE Vernova's filings, and why the queue is likely to stay years long.

https://thephysicallayer.fyi/journal/ge-vernova-sells-the-wait/

#GasTurbines #DataCentres #EnergyInfrastructure
```

## Sources (every figure)

- GE Vernova 2Q 2026 press release (8-K exhibit), 22 July 2026: https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm
  - 116 GW under contract (53 backlog, 63 SRA), up from 100; signed 20 GW (18 SRA, 2 orders), converted 10, shipped 3 GW; at least 125 GW by year end 2026; Electrification orders $6.3bn, book-to-bill ~1.7.
- GE Vernova 2Q 2026 earnings call transcript, 22 July 2026: https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf
  - ~3 GW a quarter to 5 GW a quarter from 3Q 2026 (20 GW annualised); 24 GW in 2028; 30 GW in 2030 "utilizing lean and incremental machinery in our existing factory footprint ... all funded by customer down payments"; castings and forgings arriving in 2027 for the 2028 step; mostly sold out through 2030, more than half of 2031 slots sold by year end; ~20% of GW under contract for data centres, ~100 customers in 26 countries; more than half of GW under contract are HA units; 1H26 equipment orders priced more than 20% above 4Q25; heavy-duty "another 18 months at site", aero commissioning "could be six months", heavy-duty shipped 2030 to 2031 "commissioned in '32 and '33"; "very balanced with demand relative to supply" for next six years; 30 GW needed for outages by mid next decade; Electrification equipment backlog $41bn up 69%; data centre orders over $5bn in 1H26, more than double FY25; air-insulated switchgear ~9,000 units last year, ~10,500 this year from existing factories.
- GE Vernova Form 10-Q for the quarter ended 30 June 2026, filed 22 July 2026: https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev-20260630.htm
  - Note 9: Power contract liabilities and current deferred income $16,527m (31 Dec 2025) to $27,679m (30 Jun 2026); cash from operations $10.7bn vs $1.5bn (1H26 vs 1H25), "primarily due to higher down payments on orders and slot reservation agreements at Power"; Note 8: Prolec GE remaining 50% acquired 2 Feb 2026 for $5,254m cash, ~10,000 employees, seven manufacturing sites in the Americas, five in the US.
- GE Vernova 1Q 2026 press release, 22 April 2026: https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm
  - 83 GW at year end 2025 to 100 GW; signed 21 GW (19 SRA, 2 orders); shipped 4 GW. (1H26 totals in the piece: 41 GW signed, 7 GW shipped.)
- Background only, not cited in the piece: GE Vernova 2025 investor update recap, 9 December 2025: https://www.gevernova.com/news/articles/ge-vernova-2025-investor-update-recap (80 GW year end 2025 forecast; Electrification backlog plan $30bn to $60bn by 2028).

## Could not verify / left out

- Whether slot reservation deposits are non-refundable, and their size per GW (press reports only, e.g. a $25m reservation fee; not in GE Vernova's own filings).
- The ~$200m Hai Phong, Vietnam transformer facility (secondary reports only).
- Third-party gas turbine price forecasts (e.g. $600/kW by 2027) are a consultancy figure, not GE Vernova's.
- The "about six years" ratio is my arithmetic (116 / 20), not a company figure; the piece says "almost six years".
- "Mostly sold out through 2030" and the 2032 to 2033 commissioning dates are management statements on the call, reported as theirs.
- The piece says GE Vernova was spun out of General Electric in 2024 (April 2024 spin-off; common knowledge, not re-sourced here).
