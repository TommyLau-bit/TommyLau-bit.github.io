# Eunice draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/eunice-cannot-fill-the-gap.md` (draft: true)
Cover: `public/covers/eunice-cannot-fill-the-gap.svg`
Drafted 29 October 2026, batch 3, Tier A item A2 (leads: smr-explained, energy-sector-explained). The claim needs Tommy's approval before publish.
Checker: 0 failures, 0 warnings. Body 510 words, 14 figures, 0 money figures. `npm run build` clean (249 pages).

## Slug note

The suggested slug `the-fleet-runs-out-of-enrichment` was not used. The primary sources do not support "the fleet runs out": owners hold roughly a year of reloads as enriched uranium and fabricated fuel, and European plants are expanding. The honest claim is about who fills the gap, so the slug is `eunice-cannot-fill-the-gap`.

## How it differs from terrapower-waits-on-the-fuel

TerraPower is HALEU (5 to 20 per cent) for the first core of one advanced reactor that does not run yet. This piece is ordinary LEU for the roughly ninety reactors already running, the replacement of a supplier rather than the creation of a market, and its mechanism is different: the permit is not the gate (Eunice has been licensed for 10 million SWU since 2015), the gate is centrifuges built only against long-term contracts. The TerraPower draft mentions the 2028 waiver end in one sentence; this piece builds on it and does not contradict it ("the only commercial enrichment plant" here, "the only American enrichment plant that has made HALEU" there, both true).

## Proposed claim

When the last waivers under Public Law 118-62 end on 1 January 2028, Urenco's Eunice plant, which Urenco calls America's only commercial-scale producer of enriched uranium, remains the only American source: US-origin enrichment bought by US reactor owners in 2028 stays within Eunice's capacity (no more than 5.5 million SWU), so the quarter Russia supplied in 2025 is replaced mainly by European enrichment and owners' stockpiles, not by new American plants, none of which enriches commercial LEU before 2029.

Threshold change after fact-check (29 Oct 2026): the first draft's test (US-origin at a third or more) could trip just because Urenco sells more of Eunice's roughly 5.0 million SWU to US buyers (a third of 12.7 million is 4.2 million; US-origin was already 28% in 2023). The test now asks whether American supply exceeds what Eunice can physically make, which only new American plants could cause. 5.5 million leaves a margin over Eunice's nominal 5.0 million after expansion.

### Alternatives considered

1. "The 2028 cliff will idle American reactors." Rejected: not supported. Owners held 51.8 million lb U3O8e of enriched UF6 plus 7.8 million lb of unloaded fuel at end 2025 (EIA), against 40.9 million lb loaded in 2025, and Europe is adding capacity. This is the video's implied framing and the outline's; it fails on the evidence.
2. "Eunice's expansion, not its licence, is paced by long-term contracts: Urenco will not commit the 2.1 million SWU plant before customers sign." Rejected as the lead: true and in the piece as mechanism, but Urenco has already announced the plant for 2029 construction and 2032 output, so the test is soft.

Chosen because it has a clean public test, a dated EIA table (Table 16, report for 2028 due around August 2029) that will print the answer, plus a physical failure test (a refuelling delayed or a reactor shut for lack of fuel).

## claims.ts entry

```ts
  {
    id: 'eunice-cannot-fill-the-gap',
    claim: 'When the last Russian uranium waivers end on 1 January 2028, Urenco\'s Eunice plant remains the only American source of enrichment for US reactors, so American-made enrichment cannot rise above what Eunice can make, and the quarter Russia supplied in 2025 is replaced mainly by European enrichment and owners\' stockpiles, not by new American plants.',
    breaksIf: 'The Energy Information Administration\'s Uranium Marketing Annual Report for 2028, due around August 2029, shows owners and operators of US reactors buying more than 5.5 million SWU of US-origin enrichment, more than Eunice can make; or an American reactor delays a refuelling or shuts in 2028 for lack of enriched uranium.',
    watch: ['EIA Uranium Marketing Annual Report, Table 16, US-origin and Russia-origin SWU for 2027 and 2028', 'Urenco Eunice cascades seven and eight, due by early 2027', 'First production from Orano\'s Georges Besse 2 extension, scheduled for 2028', 'Any DOE waiver or change to Public Law 118-62 before 1 January 2028', 'NRC decision on Orano\'s Project IKE licence, expected by 30 April 2027', 'Centrus\'s first new centrifuges at Piketon, expected in 2029'],
  },
```

## stack.ts

Two options; Tommy decides.
- Default: layer `onsite` ("Power on site"), after `terrapower-waits-on-the-fuel`, keeping the nuclear pieces together, as the TerraPower sidecar proposed.
- Recommended now that there are two fuel pieces: a new layer above `onsite`, upstream in the chain, as the TerraPower sidecar sketched: name "Fuel for the power plants"; what: "Uranium is mined, enriched and made into fuel before any reactor can make power."; constraint: "Enrichment outside Russia is short for today's reactors and barely exists for the new ones, and a plant takes years to build." Pieces: `['eunice-cannot-fill-the-gap', 'terrapower-waits-on-the-fuel']`. Needs its own stop in `Descent.astro`. Honest wrinkle for either: the fleet is grid power, not power beside a building.

## Glossary (heading: "Getting power to the building")

- `SWU`: Separative work unit, the standard measure of enrichment work. America's reactors buy about 13 to 15 million a year.
- `Enrichment`, `Cascade (enrichment)`: already proposed in the TerraPower sidecar; add once, whichever piece publishes first.
- `LEU`: not used as an abbreviation in the piece, so not needed.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '4.3 million SWU', what: 'Yearly capacity of Urenco\'s Eunice plant in New Mexico, America\'s only commercial enrichment plant, before its 700,000 SWU expansion finishes in early 2027; the NRC has licensed the site for up to 10 million SWU since 2015.', piece: 'eunice-cannot-fill-the-gap', asOf: 'June 2026' },
  { layer: 'onsite', value: '26%', what: 'Share of the enrichment bought by US reactor owners in 2025 that came from Russia; US-origin enrichment was 23%.', piece: 'eunice-cannot-fill-the-gap', asOf: 'EIA, August 2026' },
```
(Use the new layer id instead of `onsite` if the fuel layer is added.)

## LinkedIn post (§9)

```
America's working nuclear plants still buy about a quarter of their enrichment from Russia, and that ends at the start of 2028.

The only American plant that does this work, Urenco's site at Eunice in New Mexico, is licensed for more than twice what it runs, but each new line of centrifuges is built only against long-term contracts. Its expansion adds about a fifth of what Russia supplied, so the reactors that power data centres will lean on Europe and on their stockpiles.

The piece covers how enrichment works, where the gap shows, and what would prove me wrong.

https://thephysicallayer.fyi/journal/eunice-cannot-fill-the-gap/

#NuclearEnergy #DataCentres #EnergyInfrastructure
```

## Figures in the body, each with its primary source

| Figure | Source |
|---|---|
| About a quarter of enrichment from Russia; Russia 26%, US-origin 23% of SWU bought in 2025 | EIA, 2025 Uranium Marketing Annual Report, August 2026, p.3 and Table 16 (Russia 3,284 of 12,710 thousand SWU; US 2,930) |
| Waivers end by the start of 2028; ban enacted May 2024, in force 90 days later (11 August 2024) | Public Law 118-62, sec. 2(d)(1) and (d)(2)(C) |
| "Only commercial-scale producer" of enriched uranium in the US (Urenco's wording) | Urenco, 2 April 2026; Centrus 10-Q ("no commercial enrichment facility producing LEU using DOE centrifuge technology") |
| "Ahead of schedule" | Urenco, 2 April 2026 ("ahead of schedule", "on budget") |
| Rosatom about 43% of world capacity, the largest | WNA, Uranium Enrichment page (table from WNA Nuclear Fuel Report 2025): 27,100 of 62,641 thousand SWU in 2022 (43.3%), 29,133 of 68,076 in 2025 (42.8%). Centrus 10-Q to 30 June 2026 also says 43%. |
| Licensed for 10 million SWU in 2015 | NRC letter, 23 March 2015, Amendment 63 to SNM-2010, "Expansion of enrichment capacity from 3.7 to 10 million separative work units" |
| Runs at about 4.3 million SWU; 700,000 SWU added 2025 to early 2027; new plant producing from 2032; bigger expansions depend on long-term contracts | Urenco, 29 June 2026 (4.3 million, 700,000, construction 2029, initial cascades 2032) and 2 April 2026 ("depending on customer needs and long-term contracts") |
| Centrus first new centrifuges in Ohio in 2029 | Centrus Form 10-Q to 30 June 2026 |
| Orano Oak Ridge in licence review, NRC to finish by April 2027 ("next spring") | NRC acceptance letter to Orano Enrichment USA, 21 May 2026 (expedited schedule, completion estimated 30 April 2027) |
| About a fifth of Russia's 2025 volume; half already running by April | 700 / 3,284 = 21%, comparing Eunice's added capacity with Russian-origin SWU purchased by US owners (Urenco; EIA Table 16). 350,000 SWU installed by 2 April 2026 (Urenco), so part of the addition already sits inside the 2025 and 2026 figures. |
| Orano French expansion first production 2028 | Orano, 10 October 2024 (foundation stone; first production 2028, full commissioning 2030, +2.5 million SWU) |
| Stockpiles hold roughly a year of reloads | EIA Table 22: owners' enriched UF6 51.8 and unloaded fabricated fuel 7.8 million lb U3O8e at end 2025, against 40.9 (2025) and 48.1 (2024) million lb loaded, Table 18 |

No press-only figure is used in the body. Fact-check edits applied 29 Oct 2026: falsifier threshold, title (stockpiles added), cover label ("ALL OTHER SOURCES", since the 51% includes withheld China and Other SWU), heading and one sentence varied from the TerraPower piece, Urenco's own "commercial-scale producer" wording.

Constellation as "America's largest nuclear fleet" repeats the wording of the published Constellation piece.

## Sources (URL and date)

- Public Law 118-62, Prohibiting Russian Uranium Imports Act, 13 May 2024: https://www.govinfo.gov/content/pkg/PLAW-118publ62/html/PLAW-118publ62.htm
- EIA, 2025 Uranium Marketing Annual Report, August 2026: https://www.eia.gov/uranium/marketing/pdf/umar.pdf
- Urenco, "Urenco USA reaches half-way point of current U.S. capacity expansion", 2 April 2026: https://www.urenco.com/news/usa/2026/urenco-usa-reaches-half-way-point-of-current-u.s-capacity-expansion
- Urenco, "Urenco USA continues successful installation of US uranium enrichment capacity", 29 June 2026: https://www.urenco.com/news/usa/2026/urenco-usa-continues-successful-installation-of-us-uranium-enrichment-capacity
- Urenco, Full Year 2025 audited results, 12 March 2026: https://www.urenco.com/news/global/2026/full-year-2025-audited-results (2.5 million SWU programme, Almelo and Gronau expansions; not used for figures)
- NRC, Amendment 63 letter to Louisiana Energy Services, 23 March 2015: https://www.nrc.gov/docs/ML1504/ML15049A402.pdf
- NRC, acceptance of Orano Enrichment USA licence application, 21 May 2026: https://www.nrc.gov/docs/ML2613/ML26134A324.pdf
- NRC, Urenco USA LEU+ amendments (to under 10 wt%, Amendments 105 and 110, the latter 31 July 2025): https://www.nrc.gov/docs/ML2519/ML25196A455.pdf (context only, not in the piece)
- Orano, foundation stone of the Georges Besse 2 extension, 10 October 2024: https://www.orano.group/en/news/news-group/2024/october/laying-of-the-foundation-stone-of-the-georges-besse-2-plant-extension
- Orano USA, Project IKE licence submission, 27 March 2026: https://www.orano.group/usa/en/our-news/news-releases/2026/orano-finishes-scheduled-license-submission-for-project-ike-uranium-enrichment-facility-to-NRC (no capacity or start year given)
- Centrus Energy Form 10-Q to 30 June 2026, filed 6 August 2026: https://www.sec.gov/Archives/edgar/data/1065059/000162828026053863/leu-20260630.htm (waivers for committed US deliveries 2024 to 2027; pending application of 11 December 2024; "well over one-half" of LEU delivered through 2027 sourced from TENEX; Russian decree extended to 31 December 2027; first new Piketon centrifuges 2029; Russia 43%)
- WNA, Uranium Enrichment: https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment
- Leads only, credited once: Leo Cui, "Small Modular Reactors (SMR) Explained" (https://www.youtube.com/watch?v=uojk6TaosEg) and "The Entire Energy Sector Explained" (https://www.youtube.com/watch?v=0zZyEF4Cq9U), YouTube.

## Video figures: dropped or flagged

- "Russia roughly 44% of world enrichment capacity" (both videos): NOT SUPPORTED. WNA's table gives 43.3% (2022) and 42.8% (2025); Centrus's 10-Q says 43%. The piece uses "about 43 per cent".
- "Ban enacted May 2024, took effect that August": CONFIRMED (PL 118-62: 90 days after 13 May 2024).
- "Waivers on or before 1 January 2028": CONFIRMED (sec. 2(d)(2)(C)).
- "Uranium prices at multi-year highs" (energy video): not checked, not used (price, out of scope).
- Urenco and Orano "expanding Western enrichment": confirmed and used with primary figures.

## Not verified or left out

- DOE's own list of waiver determinations: no energy.gov page found; waiver status taken from Centrus's 10-Q only. Whether DOE granted Centrus's pending December 2024 application is not disclosed.
- Orano Project IKE capacity and start year: not stated in any 2026 Orano release; press reports of early 2030s not used.
- Russia's own export decree (TENEX needs a licence per shipment through 31 December 2027): confirmed in Centrus's 10-Q, left out of the piece for length.
- How much of Eunice's output goes to US versus foreign buyers: not disclosed; the cover's 23% is US-origin SWU bought by US owners, which in practice is Eunice.
