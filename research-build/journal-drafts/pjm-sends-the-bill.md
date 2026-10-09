# PJM capacity auction draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/pjm-sends-the-bill.md` (draft: true)
Cover: `public/covers/pjm-sends-the-bill.svg`
Drafted 9 October 2026. Claim needs Tommy's approval before publish.

## Proposed claim

PJM's capacity auction cannot summon new power stations as fast as data centres add demand, so it will keep clearing at or near its price ceiling, with households paying.

### Alternatives considered

1. "A tenfold price rise summoned only 525 MW of new plant: the interconnection queue, not money, gates supply." Rejected as the lead: it largely repeats the-queue-not-the-chip and the-part-money-cannot-hurry. Kept as the mechanism.
2. "Within two years most PJM states will make data centres bring or pay for their own capacity." Rejected as the lead: a policy forecast, not a physical mechanism, and hard to score cleanly across 13 states. Kept as the last line of the falsifier.

Chosen because it is new to the site (who pays for scarce firm capacity, the honest counterweight), rests on a physical mechanism (forecast load rises faster than plants can be built and connected), and is tested by public auction results PJM publishes twice a year.

## claims.ts entry

```ts
  {
    id: 'pjm-sends-the-bill',
    claim: 'PJM\'s capacity auction cannot summon new power stations as fast as data centres add demand, so it will keep clearing at or near its price ceiling, with households paying.',
    breaksIf: 'A PJM base auction clears below $325 per MW-day, the cap in force in 2026, and meets its reliability requirement while the data centre load forecast is still rising; or new generation cleared in an auction outruns the data centre load added to its forecast.',
    watch: ['Clearing price against the cap in each base auction, starting with 2029/2030 in December 2026', 'Shortfall against the reliability requirement in each auction', 'New generation cleared against data centre load added to the forecast', 'Large-load tariffs and bring-your-own-capacity rules adopted by PJM states, and the refiled Reliability Backstop Procurement'],
  },
```

## stack.ts

Layer `grid` ("The grid connection"). Suggested position after `the-power-it-drops`:
`pieces: ['the-queue-not-the-chip', 'the-part-money-cannot-hurry', 'hitachi-energy-plans-the-queue', 'siemens-energy-measures-the-shortage', 'two-governments-one-confession', 'the-power-it-drops', 'pjm-sends-the-bill']`

The layer's `constraint` sentence is about connection waits; it still fits, since the piece's mechanism is that new supply waits years to connect. No new layer needed.

## Glossary (heading: "Getting power to the building")

- `Capacity auction`: An auction in which a grid operator pays power stations, by the day, to promise they will be available when the grid is under most strain, a few years ahead. The cost is shared across every customer's bill. PJM's is called the Base Residual Auction.
- `Reliability requirement`: The amount of capacity a grid operator says it needs to keep the chance of running short to about one day in ten years. PJM's last two auctions fell short of it for the first time.
- `Large-load tariff`: Special terms a utility sets for very large new customers such as data centres, for example paying for most of the power they reserve whether they use it or not, so other customers do not carry the cost of serving them.

## numbers.ts (physical figures only)

```ts
  { layer: 'grid', value: '6,831 MW', what: 'How far PJM\'s capacity auction for 2028/2029 fell short of its own reliability requirement. New power stations and upgrades cleared only 525 MW.', piece: 'pjm-sends-the-bill', asOf: '14 July 2026' },
```

Optional second: `{ layer: 'grid', value: '~5 years', what: 'Median time for a US power project of 200 MW or more from asking to connect to switching on (56 months), by Lawrence Berkeley National Laboratory.', piece: 'pjm-sends-the-bill', asOf: 'December 2025' }`

## LinkedIn post (§9)

```
PJM's capacity auction has cleared at its price cap three times running, and the latest one still came up almost 7 gigawatts short.

PJM runs the grid for 67 million people across 13 states, including northern Virginia's data centres. Data centre demand is rising faster than power stations can be built and connected, and its market monitor puts nearly two fifths of the latest auction's cost on that demand. That cost lands on household bills, which is where the AI build-out meets its political limit.

The piece covers how the capacity auction works, why a higher price cannot summon a plant in time, and what would prove the claim wrong.

https://thephysicallayer.fyi/journal/pjm-sends-the-bill/

#PowerGrid #DataCentres #EnergyInfrastructure
```

## Sources (every figure)

- PJM 2025/2026 Base Residual Auction Report, 30 July 2024: https://www.pjm.com/-/media/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.ashx
  - RTO price $28.92/MW-day (2024/25) to $269.92 (2025/26): "almost tenfold"; total cost $2.2bn to $14.7bn (not used).
- PJM release, 22 July 2025 (2026/2027 BRA): https://insidelines.pjm.com/pjm-auction-procures-134311-mw-of-generation-resources-supply-responds-to-price-signal/
  - Cleared at the FERC-approved cap of $329.17/MW-day; floor $177.24.
- PJM 2027/2028 BRA report and MRC presentation, 17 to 19 December 2025: https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2027-2028/2027-2028-bra-report.pdf
  - Cleared at the cap of $333.44/MW-day; about 6,600 MW short of the reliability requirement; 774 MW new generation and uprates (from the PJM report as summarised; PDF images did not extract, figures confirmed against PJM's 14 July 2026 release, which cites the ~6,500 MW prior shortfall).
- PJM release, 14 July 2026 (2028/2029 BRA): https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf
  - 67 million people, 13 states and DC; cap and floor agreed "for four capacity auctions", third consecutive with the collar; cleared at the cap of $325/MW-day; total value $16.4bn; 6,831 MW short of the reliability requirement; "first in PJM history in which the entire RTO fell short"; 525 MW UCAP new generation and uprates; next BRA (2029/2030) in December.
- Monitoring Analytics (PJM Independent Market Monitor), Market Monitoring Report to PJM Members Committee, 27 July 2026: https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20260727-web/item-02---marketing-monitoring-report---presentation.pdf
  - Data centre load: $6.3bn, 38.2% of $16.4bn ("nearly two fifths"); $29.4bn, 46.2% over the last four auctions; data centre load in the 2028/29 forecast 21,470 MW (16,436 MW above embedded); IMM position that data centres should be removed from the capacity market and procured in a dedicated auction.
- Lawrence Berkeley National Laboratory, Queued Up: 2025 Edition, 15 December 2025: https://emp.lbl.gov/sites/default/files/2025-12/Queued%20Up%202025%20Edition%20-%2012.15.2025.pdf
  - Median 200+ MW project nearly 5 years (56 months) from interconnection request to commercial operation (projects online 2010 to 2024).
- New Jersey Board of Public Utilities, 12 February 2025: https://www.nj.gov/bpu/newsroom/2025/approved/20250212.html
  - BGS auction: average bills up 17.23% to 20.20% from 1 June 2025; causes cited: demand growth incl. data centres, lagging new generation interconnection, PJM market dynamics.
- Governor of Pennsylvania press release, 2026 (complaint and collar extension): https://www.pa.gov/governor/newsroom/2026-press-releases/governor-shapiro-s-legal-action-again-prevents-price-hike-across
  - December 2024 FERC complaint; January 2025 settlement capping two auctions; FERC approved extension for two more (April 2026).
- AEP Ohio / PUCO, 9 July 2025: https://www.aep.com/news/stories/view/10327/
  - PUCO approved AEP Ohio's data centre tariff: new data centres over 25 MW pay for at least 85% of subscribed demand for up to 12 years, including a four-year ramp.
- Background, not cited in the piece: FERC order of 29 September 2026 (ER26-3380) suspending PJM's Reliability Backstop Procurement to 28 February 2027: https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/9154/20260929-er26-3380-000.pdf (read via secondary summaries only).

## Could not verify / left out

- AEP Ohio's data centre pipeline falling from about 30 GW to 13 GW after the tariff: secondary reports only (AEP Ohio release could not be fetched). Left out.
- The 2027/2028 BRA report PDF did not extract as text; its figures (cap $333.44, ~6,600 MW short, 774 MW new, 5,100 MW of 5,250 MW forecast increase from data centres) came via secondary summaries and PJM's own later release. Not used in the piece except as "the cap for the third time running".
- "About two years ahead" is my reading of the compressed schedule (July 2026 auction for June 2028), not a PJM phrase.
- The FERC backstop suspension is from secondary summaries plus the order's title; not used in the piece.
