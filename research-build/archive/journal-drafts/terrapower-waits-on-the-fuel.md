# TerraPower draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/terrapower-waits-on-the-fuel.md` (draft: true)
Cover: `public/covers/terrapower-waits-on-the-fuel.svg`
Drafted 29 October 2026 from the Watch Later batch (lead: smr-explained). Claim needs Tommy's approval before publish.
Checker: 0 failures, 0 warnings. Body 561 words, 13 figures, 1 money figure. Fact-check edits applied 29 Oct 2026.

## Proposed claim

Kemmerer Unit 1's start date is set by its HALEU fuel, not its construction permit: its first core depends on a South African enrichment plant that had not enriched any uranium as of August 2026 and on Energy Department stocks of undisclosed size, while America's only HALEU cascade stopped producing in June 2026, so I expect fuel load to slip past the end of 2030.

How the outline claim was refined: the outline said fuel load slips "unless the first core comes from DOE stock or abroad". The primary sources show that TerraPower's plan already is DOE stock plus abroad (ASP Isotopes in South Africa, signed 16 May 2025). So the claim now tests whether that plan delivers, rather than treating it as an escape hatch. The chicken-and-egg point (no plant without orders, no orders without fuel) is kept in the mechanism, but softened: Centrus has signed HALEU supply contracts with Oklo, Radiant, Antares and X-energy in 2026, all with deliveries "before the end of the decade", and says deployment depends on funding and offtake. The piece does not claim nobody is ordering.

### Alternatives considered

1. "The Natrium fleet Meta wants is sized by HALEU supply, not by reactor permits or factory slots: by 2032 the West will not enrich enough HALEU for more than one or two Natrium cores a year." Rejected as the lead: needs a verified core mass (only press estimates of 15 to 20 tonnes were found) and a forward capacity model, which belongs in a research note.
2. "Centrus's commercial HALEU plant, not any reactor developer, is the pacing item for American advanced nuclear." Rejected: makes Centrus the subject and repeats ground near the Oklo piece; Tommy approved TerraPower as the subject.

Chosen because it has a sharp, dated test (fuel in the reactor by end 2030, TerraPower's own completion year) and an unusually clean way to tell fuel delay from construction delay (the second falsifier).

## claims.ts entry

```ts
  {
    id: 'terrapower-waits-on-the-fuel',
    claim: 'TerraPower\'s Kemmerer Unit 1 start date is set by its HALEU fuel, not its construction permit: its first core depends on a South African enrichment plant that had not enriched any uranium as of August 2026 and on Energy Department stocks of undisclosed size, so fuel load slips past the end of 2030.',
    breaksIf: 'Fuel is loaded into Kemmerer Unit 1 by 31 December 2030; or Kemmerer runs late for another reason, such as construction or the operating licence, while its full first core has already been delivered.',
    watch: ['First enrichment of uranium at ASP Isotopes\' Pelindaba plant, and its South African licences', 'The quantity of the Energy Department\'s HALEU commitment to TerraPower', 'Whether the Energy Department funds further production from Centrus\'s Piketon cascade', 'TerraPower\'s operating licence application, targeted for 2028', 'Delivery of fabricated first-core fuel to the Kemmerer site'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"), placed after `oklo-sells-the-electricity`:
`pieces: [..., 'constellation-restarts-the-reactor', 'oklo-sells-the-electricity', 'terrapower-waits-on-the-fuel']`

Why: it keeps the three nuclear pieces together, where readers will look, and the layer's `what` already names small reactors. Honest wrinkle: Kemmerer is a grid plant (sited at a retiring PacifiCorp coal plant), not beside a data centre, just as Crane is not. If Tommy prefers, a new layer could sit above `onsite`, upstream in the chain:
- name: "Fuel for the power plants"; what: "Uranium is mined, enriched and made into fuel before any reactor can make power."; constraint: "Enrichment for the new reactors barely exists outside Russia, and a plant takes years to build." That would need its own stop in `Descent.astro`. I recommend `onsite` for now.

## Glossary (heading: "Getting power to the building")

- `Enrichment`: Raising the share of uranium-235, the atom that splits, in uranium. It is done by spinning uranium gas in fast centrifuges. Ordinary reactors use up to about 5 per cent; HALEU runs from 5 to 20.
- `Cascade (enrichment)`: A line of centrifuges linked so each one passes slightly richer gas to the next. Centrus's demonstration cascade in Ohio has sixteen.
- `First core`: The full initial load of fuel a new reactor needs before it can start. It is far larger than a yearly refuelling.

Existing `HALEU` and `Fast reactor` entries already fit.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '900 kg', what: 'HALEU the Energy Department extended Centrus\'s demonstration cascade in Piketon, Ohio, to make over one more year from June 2025; it is the only American enrichment plant that has made HALEU, and that production finished in mid-June 2026.', piece: 'terrapower-waits-on-the-fuel', asOf: 'June 2026' },
```

Optional: `{ layer: 'onsite', value: '345 MW', what: 'Steady output of TerraPower\'s Natrium reactor at Kemmerer, Wyoming; molten salt storage lets the plant deliver up to 500 MW for several hours.', piece: 'terrapower-waits-on-the-fuel', asOf: 'construction permit, March 2026' }`

## LinkedIn post (§9)

```
TerraPower has its permit to build a new reactor in Wyoming. What it does not have yet is the fuel.

Natrium runs on HALEU, uranium enriched to between 5 and 20 per cent, and outside Russia almost nobody makes it. The first load for Kemmerer is promised by a South African plant that has not yet enriched any uranium, and the only American line finished its contracted production in June. With Meta planning up to eight more Natrium plants, fuel, not paperwork, now sets the pace of this kind of nuclear power.

The piece covers how enrichment works, where the fuel gap shows, and what would prove me wrong.

https://thephysicallayer.fyi/journal/terrapower-waits-on-the-fuel/

#NuclearEnergy #DataCentres #EnergyInfrastructure
```

## Sources (every figure)

- NRC, News Release No. 26-028, 4 March 2026: https://content.govdelivery.com/accounts/USNRC/bulletins/40ca5a7
  - Commission authorised the construction permit for US SFR Owner (TerraPower subsidiary), Kemmerer Unit 1; 345 MWe, storage boost to 500 MWe; first commercial reactor construction approval in about ten years; separate operating licence required. Staff issued the permit shortly after (World Nuclear News, 5 March 2026: https://world-nuclear-news.org/articles/nrc-issues-construction-permit-for-first-natrium-plant).
- TerraPower, "NRC Approves the Natrium Reactor Construction Permit", 4 March 2026: https://www.terrapower.com/NRC-Approves-Natrium-Reactor-Construction-Permit
  - "initial 27-month review schedule", "completed in 18 months" (the piece's "nine months inside its original schedule"); first plant "expected to be completed in 2030".
- TerraPower, construction start, 23 April 2026: https://www.terrapower.com/TerraPower-Commences-Construction-on-Americas-First-Utility-Scale-Advanced-Nuclear-Power-Plant (no fuel or operation date given).
- TerraPower, "TerraPower and Meta Enter Agreement for 8 Natrium Advanced Nuclear Plants", 9 January 2026: https://www.terrapower.com/terrapower-announces-deal-with-meta
  - Up to 8 plants; up to 2.8 GW baseload, up to 4 GW with storage; two units with early development funding, energy rights for up to six more; initial units "as early as 2032". The video's "roughly 2.8 GW" is CONFIRMED. Binding status not stated in the release.
- World Nuclear News, "HALEU fuel availability delays Natrium reactor project", 15 December 2022: https://www.world-nuclear-news.org/articles/haleu-fuel-availability-delays-natrium-reactor-pro (also CNBC, 16 December 2022). PRESS-REPORTED TerraPower statement: Levesque, "a minimum of a two-year delay", against the "proposed 2028 in-service date"; Russia's invasion made "the only commercial source of HALEU fuel" no longer viable. TerraPower's own newsletter text was not found on its site.
- ASP Isotopes Form 10-Q for the period to 30 June 2026, filed 14 August 2026: https://www.sec.gov/Archives/edgar/data/1921865/000119312526352603/aspi-20260630.htm
  - Two TerraPower supply agreements dated 16 May 2025; initial core agreement "intended to support the supply of the required first fuel cores for the initial loading of TerraPower's Natrium project in Wyoming"; long-term agreement up to 150 tonnes of HALEU, 2028 to 2037; "we have not applied our enrichment technologies to the enrichment of U-235, nor received permission or regulatory approval to conduct testing of our enrichment technologies on U-235, except for the activities contemplated by the Services Contract with Necsa"; TerraPower loan disbursements conditional on "all required licenses and permits to perform uranium enrichment in South Africa"; drawdowns planned from Q3 2026. Note: the May 2025 8-K said first cores in the "2027/2028 timeframe"; the August 2026 10-Q no longer gives a date.
- ASP Isotopes Form 10-K for 2025: https://www.sec.gov/Archives/edgar/data/1921865/000119312526151294/aspi-20251231.htm (same language; Necsa services contract February 2026).
- World Nuclear News, "Joint venture to produce HALEU in South Africa", 19 October 2026: https://world-nuclear-news.org/articles/joint-ventureto-produce-haleu-in-south-africa
  - QLE and Necsa binding heads of agreement; "Work is already under way to refurbish the infrastructure housing a previous test bench facility"; no production date. PRESS (trade), based on company announcement.
- Centrus Energy Form 10-Q for the period to 30 June 2026, filed 6 August 2026: https://www.sec.gov/Archives/edgar/data/1065059/000162828026053863/leu-20260630.htm
  - 16-centrifuge cascade under the 2019 demonstration contract; 900 kg Phase 2 target; "Production under Option 1a was completed in mid-June"; Option 1b is three months of "cascade maintenance and HALEU storage, with no HALEU production"; FY2027 DOE budget "does not include funding for the operation of this cascade"; "DOE has communicated that it does not currently intend to exercise further options"; $900.0 million task order announced 5 January 2026, contract signed 1 July 2026, firm fixed price, to "deploy a specified amount of enrichment capacity and deliver, by July 2032, one metric ton" of HALEU at 19.75 per cent, with DOE options for two further 5 MTU lots; Import Ban Act enacted May 2024, effective 11 August 2024.
- Centrus second quarter 2026 results, 5 August 2026: https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053433/ex991-10q2026_08x05.htm
- Centrus 8-Ks of 9 and 17 September 2026 (Radiant and Antares HALEU contracts, deliveries before the end of the decade): https://www.sec.gov/Archives/edgar/data/1065059/000162828026061036/leu-20260909.htm and https://www.sec.gov/Archives/edgar/data/1065059/000162828026062535/leu-20260917.htm
- DOE, first HALEU allocations, 9 April 2025: https://www.energy.gov/articles/us-department-energy-distribute-first-amounts-haleu-us-advanced-reactor-developers
  - TerraPower among five conditional commitments; material from NNSA and other DOE sources; quantities not disclosed; "HALEU is not currently available from domestic suppliers."
- DOE, HALEU Allocation Process (rounds to 23 July 2026): https://www.energy.gov/ne/us-department-energy-haleu-allocation-process
- DOE, HALEU Enrichment Services (Task Order 2, 5 January 2026: Centrus and General Matter, $900 million each): https://www.energy.gov/ne/haleu-enrichment-services
- DOE, "Centrus Reaches 900 Kilogram Mark for HALEU Production", June 2025: https://www.energy.gov/node/4851599 (about 900 kg a year; extension for another 900 kg).
- Public Law 118-62, Prohibiting Russian Uranium Imports Act, 13 May 2024: https://www.govinfo.gov/content/pkg/PLAW-118publ62/html/PLAW-118publ62.htm
  - Ban begins 90 days after enactment; "Any waiver issued under subparagraph (A) shall terminate not later than January 1, 2028."
- World Nuclear Association, Uranium Enrichment, updated 27 October 2026: https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment (capacity table from WNA Nuclear Fuel Report 2025; Centrus "more than 1,900 kg" cumulative).
- TerraPower and Framatome, uranium metallization, 4 November 2025: https://www.terrapower.com/framatome-and-terrapower-achieve-breakthrough-in-uranium-metallization-for-advanced-reactor-fuel-commercialization
- GNF and TerraPower, Natrium Fuel Facility at Wilmington, 21 October 2022: https://www.terrapower.com/global-nuclear-fuel-and-terrapower-announce-natrium-fuel-facility
- Lead only, credited once in the sources line: Leo Cui, "Small Modular Reactors (SMR) Explained", YouTube: https://www.youtube.com/watch?v=uojk6TaosEg

## Video figures: dropped or flagged

- "$900m task order each" for Centrus and General Matter: CONFIRMED (DOE enrichment services page; Centrus 10-Q). Only Centrus's is used in the piece. Correction to the video's framing: the DOE awards were announced 5 January 2026; Centrus signed its contract on 1 July 2026. The video's "finalized in July 2026" matches the signing, not the award.
- "1,900 kg cumulative output": CONFIRMED only by WNA ("more than 1,900 kg"); the 10-Q supports roughly 20 + 900 + a further year's run but gives no cumulative total. DROPPED from the piece; the annual rate (about 900 kg, DOE) is used instead.
- "44% Russian share of enrichment": NOT SUPPORTED as stated. WNA's table gives Rosatom about 43 per cent of world capacity in 2022 and 2025 (27,100 and 29,133 of 62,641 and 68,076 thousand SWU), falling to about 38 per cent by 2030. DROPPED.
- "Meta up to roughly 2.8 GW": CONFIRMED (TerraPower release). The piece uses "up to eight more plants" in words instead, to stay inside the figure budget.
- Construction permit authorised 4 March, issued 9 March 2026: authorisation confirmed (NRC); the 9 March issue date is press-only and not used.
- Video's "target around 2030" for Kemmerer: TerraPower's own wording is completion "in 2030". A 2025 interview (Neutron Bytes, 20 November 2025, TerraPower COO Eric Williams) gives fuel load 2030 and power on the grid 2031; PRESS-ONLY, not used in the piece.
- Video's 500 MW storage boost: confirmed (NRC), not used.

## Could not verify / left out

- The mass of a Natrium first core. Press estimates are 15 to 20 tonnes of HALEU (Neutron Bytes); no TerraPower or NRC figure found. Left out. If confirmed, it is the single most powerful number for the research note (one tonne by July 2032 from Centrus's new contract against a core of many tonnes).
- The size of DOE's HALEU commitment to TerraPower: never disclosed. The piece says so.
- Whether ASP's Pelindaba plant will use its aerodynamic separation process or its laser process: the filings are ambiguous. Not mentioned.
- "Only American enrichment plant that has made HALEU": supported by DOE ("not currently available from domestic suppliers") and WNA. DOE also makes small amounts by downblending weapons-grade uranium, which is why the piece says "enrichment plant".
- The second falsifier (late for another reason while the core is on site) relies on TerraPower or the NRC disclosing fuel delivery; watch the operating licence docket.
