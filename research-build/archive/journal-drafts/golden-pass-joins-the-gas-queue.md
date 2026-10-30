# Golden Pass LNG draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/golden-pass-joins-the-gas-queue.md` (draft: true)
Cover: `public/covers/golden-pass-joins-the-gas-queue.svg`
Drafted 29 October 2026 (Batch 3, Tier A item A15). Oil and gas physical system only: no LNG or gas price forecast, no spreads, no trading view, no views on shares. No money figures in the body at all.

## Verdict against the quality bar: PASS

1. New mechanism. The site has the supply side (permian-gas-follows-the-oil-rig: oil drilling and takeaway pipes set Permian supply) and the grid connection (ercot-rations-the-plug). It has nothing on who holds the pipe at the demand end. This piece adds that Gulf Coast pipe capacity is built to signed take-or-pay contracts, export terminals signed first, and data centre power is signing years later. It is the fuel cousin of the grid queue, not another order-book piece.
2. Primary sources. Every body figure is from EIA's own monthly series, an EIA Today in Energy note, a FERC docket notice in the Federal Register, Kinder Morgan's earnings releases on SEC EDGAR, or Entergy's own release.
3. Beyond the headline. The headline is "Golden Pass shipped its first cargo". What a PM would not know: Texas export terminals already shipped more gas than Texas power plants burned in February to April 2026; Golden Pass in July was running at about a tenth of nameplate; Golden Pass's ramp alone decides whether the annual line crosses in 2027; and the pipe into the Port Arthur corridor is shared with Entergy Texas's power plants under contracts signed in early 2025.

## Proposed claim

Golden Pass is the terminal that tips Texas: in calendar 2027, the gas Texas's LNG terminals ship abroad will exceed the gas delivered to Texas power plants, by EIA's monthly count, because export terminals signed for Gulf Coast pipe space years before data centre power did.

Title: "Golden Pass will send more Texas gas abroad than Texas power plants burn". Thesis line: "Golden Pass will tip Texas: from 2027, more Texas gas will leave as LNG than its power plants burn."

Why the test is not consensus: EIA publishes no Texas-level forecast of either series. On EIA's actuals, 2025 averaged 4.40 Bcf/d of Texas LNG exports against 5.69 Bcf/d to Texas power; January to July 2026 averaged 5.08 against 5.60. Without Golden Pass, Corpus Christi plus Freeport sit near 5.1 to 5.4 Bcf/d, below power. Golden Pass at full rate adds about 2.0 Bcf/d nominal. So the flip turns on Golden Pass's ramp, which keeps the subject central and gives a real chance of failure (Train 1 ramped slowly; Trains 2 and 3 have slipped once already).

### Alternatives considered

1. "US LNG gross exports average above 19 Bcf/d in the fourth quarter of 2027." Rejected: it is EIA's own STEO forecast (19.6 Bcf/d, October 2026 Table 5a), so it tests nothing a PM does not already have, and it does not touch Texas power or pipes.
2. "Trident enters service in the first quarter of 2027 and its capacity is fully contracted to LNG and industrial shippers, with no new data centre shipper before 2028." Rejected: Trident's shipper list is not public in primary form (Golden Pass's 1 Bcf/d commitment is press-only), so the test could not be read from a primary source.

Chosen because it is physical, dated, and read directly from two EIA series that anyone can check.

## claims.ts entry

```ts
  {
    id: 'golden-pass-joins-the-gas-queue',
    claim: 'Golden Pass is the terminal that tips Texas: in calendar 2027, the gas Texas LNG terminals ship abroad will exceed the gas delivered to Texas power plants, because export terminals signed for Gulf Coast pipe space years before data centre power did.',
    breaksIf: 'EIA\'s monthly data for calendar 2027 show natural gas delivered to Texas electric power consumers at or above the total LNG exported from Texas points of exit (Corpus Christi, Freeport, Golden Pass and any new Texas terminal).',
    watch: ['EIA, Texas natural gas deliveries to electric power consumers, monthly (series N3045TX2)', 'EIA, LNG exports by point of exit: Golden Pass TX, Corpus Christi TX, Freeport TX, monthly', 'FERC orders on Golden Pass Trains 2 and 3 commissioning (docket CP14-517 and successors)', 'Kinder Morgan quarterly releases on Trident in-service and on new take-or-pay contracts with power plants and data centres', 'EIA Short-Term Energy Outlook Table 5a, LNG gross exports and electric power consumption'],
  },
```

Data note for the test: EIA publishes calendar 2027 monthly values through December by about the end of February 2028, with revisions. The test uses LNG export volumes as EIA reports them (gas equivalent); feedgas into terminals is higher than exports because liquefaction burns some gas, so the comparison is conservative against the claim.

## stack.ts layer

Same proposed new layer as permian-gas-follows-the-oil-rig: `fuel` ("Fuel for power"), first in `STACK`, before `grid`. If the Permian piece publishes first, add this slug to that layer's `pieces`. If this piece publishes first, add the layer as written in the Permian sidecar:

```ts
  {
    id: 'fuel',
    name: 'Fuel for power',
    kind: 'energy',
    what: 'The fuels power stations burn or split, gas by pipeline and uranium made into reactor fuel, travel from where they are produced to the plant.',
    constraint: 'Fuel supply is set by producers, processors and pipelines with their own clocks, not by the power buyer at the end of the chain.',
    pieces: ['permian-gas-follows-the-oil-rig', 'golden-pass-joins-the-gas-queue'],
  },
```

The Descent.astro stop for this layer is drawn once, with whichever fuel piece publishes first.

## Glossary (heading: "Getting power to the building", beside the Permian terms)

- `LNG (liquefied natural gas)`: Natural gas chilled to about minus 162 degrees Celsius until it turns liquid, so a ship can carry it. An export terminal draws gas from pipelines and liquefies it.
- `Liquefaction train`: One production line inside an LNG export plant, a set of compressors and refrigeration that turns pipeline gas into liquid. Plants are built and started one train at a time.
- `Feedgas`: The gas piped into an LNG export plant. It is higher than the LNG exported, because the plant burns some to run itself.
- `Firm transport`: Pipeline space a shipper has contracted and pays for whether it uses it or not, usually under a take-or-pay agreement. It is served before interruptible space when a pipe is full.
- (Reuse existing `Take-or-pay agreement`; add "Pipelines are built on them" to its definition at publish if wanted. `Bcf a day` is proposed in the Permian sidecar.)

## numbers.ts (physical figures only, layer `fuel`)

```ts
  { layer: 'fuel', value: '4.4 vs 5.7 Bcf/d', what: 'Gas exported as LNG from Texas terminals against gas delivered to Texas power plants, 2025 average. In February to April 2026 export was ahead; Golden Pass at full rate adds about 2 Bcf/d to the export side.', piece: 'golden-pass-joins-the-gas-queue', asOf: '2025, EIA' },
```

## LinkedIn post (§9), slot to be assigned at publish

```
This spring, Texas export terminals shipped more gas abroad than Texas power plants burned.

Over a whole year power still leads, because summer runs every gas plant flat out. Golden Pass, the new QatarEnergy and ExxonMobil plant at Sabine Pass, is the swing: when its three trains run, export overtakes Texas power for the year. The pipes into the coast were signed for by export plants first, and data centres are signing for theirs years later.

The piece covers how an LNG plant books its gas, why new pipes follow signed contracts, and what would prove me wrong.

https://thephysicallayer.fyi/journal/golden-pass-joins-the-gas-queue/

#Energy #NaturalGas #DataCentres
```

## Figures used in the body, with primary source

1. First cargo April 2026 (22 April); first LNG March 2026: EIA Today in Energy, 23 April 2026. (Golden Pass's own release of 22 April 2026 seen only via press.)
2. Owned mostly by QatarEnergy, rest ExxonMobil (70/30): EIA Today in Energy, 23 April 2026.
3. Three trains, about 2 Bcf/d nominal in all (0.7 Bcf/d nominal, 0.8 peak per train; 2.4 Bcf/d peak total): EIA Today in Energy, 23 April 2026.
4. "Running at a fraction" and "in July Golden Pass shipped about a tenth": EIA, Golden Pass TX LNG exports, monthly, released 30 September 2026: Apr 3,619, May 3,464, Jun 3,449, Jul 6,772 MMcf. July = 0.22 Bcf/d, 11 per cent of 2.0 nominal (my arithmetic).
5. Trident from Katy to the Port Arthur corridor, Kinder Morgan's, announced January 2025, first phase in service Q1 2027: Kinder Morgan Q4 2024 release (EX-99.1, 22 January 2025) and Q1 2026 release (22 April 2026; "roughly 219-mile, 2 Bcf/d", phase one Q1 2027, phase two Q4 2028, 30 per cent of run-rate contracted EBITDA in 2027 "due to staggered contract start dates"). Q4 2025 release (21 January 2026) also confirms phase timing.
6. Golden Pass "helped set up" Trident: Entergy Texas release, 31 January 2025 ("developed with Golden Pass LNG"; Golden Pass CCO quote on supply access). Entergy Texas signed a transportation agreement; Trident supports nearly all Entergy Texas plants and proposed Legend and Lone Star stations.
7. April 2025 request to FERC for a spur to Trident: Federal Register notice, 30 April 2025, docket CP25-205-000 (filed 11 April 2025): about 1.1 miles of 42-inch supply lateral connecting with Trident Intrastate Pipeline LLC at a receipt manifold, plus a KMLP receipt point. Order status not checked.
8. Kinder Morgan's line for a hyperscaler's power plants, approved October, due 2030: NGPL Permian Link Project, FID, about 2.8 Bcf/d, "will serve new power generation for an A-rated hyperscaler", in service Q3 2030: Kinder Morgan Q3 2026 release, 21 October 2026. (Location of the power plants not stated; the piece does not say Texas.)
9. February, March and April 2026 Texas exports above Texas power burn; power leads over the year: EIA monthly series, released 30 September 2026. Texas deliveries to electric power consumers (N3045TX2): Feb 127,523, Mar 127,999, Apr 144,241 MMcf. Texas LNG exports (Corpus Christi + Freeport + Golden Pass): Feb 147,907, Mar 165,399, Apr 159,524 MMcf. 2025 averages 4.40 (LNG) vs 5.69 (power) Bcf/d; Jan to Jul 2026 5.08 vs 5.60.

No company financial figures in the body. Body 495 words (checker word count passes); checker 0 failures, 0 warnings; npm run build clean.

## Sources, one per line

- EIA, Golden Pass, Texas LNG exports to all countries, monthly (released 30 September 2026). https://www.eia.gov/dnav/ng/hist/ngm_epg0_eng_ygpt-z00_mmcfm.htm
- EIA, Corpus Christi, TX LNG exports, monthly (30 September 2026). https://www.eia.gov/dnav/ng/hist/ngm_epg0_eng_ycrp-z00_mmcfm.htm
- EIA, Freeport, TX LNG exports, monthly (30 September 2026). https://www.eia.gov/dnav/ng/hist/ngm_epg0_eng_yfpt-z00_mmcfm.htm
- EIA, Texas natural gas deliveries to electric power consumers, monthly (30 September 2026). https://www.eia.gov/dnav/ng/hist/n3045tx2m.htm
- EIA, Today in Energy, Golden Pass first cargo, 23 April 2026. https://www.eia.gov/todayinenergy/detail.php?id=67564
- EIA, Short-Term Energy Outlook, October 2026, Table 5a (US LNG gross exports 17.6 Bcf/d 2026, 18.6 Bcf/d 2027; background and alternative 1 only). https://www.eia.gov/outlooks/steo/archives/oct26.pdf
- Federal Register, Golden Pass LNG Terminal LLC, notice of amendment application, docket CP25-205-000, 30 April 2025. https://www.govinfo.gov/content/pkg/FR-2025-04-30/html/2025-07457.htm
- Kinder Morgan, Q4 2024 results, EX-99.1, 22 January 2025 (Trident announced). https://www.sec.gov/Archives/edgar/data/1506307/000150630725000002/kmi2024q48-kex991.htm
- Kinder Morgan, Q4 2025 results, EX-99.1, 21 January 2026 (Trident construction begun, phases). https://www.sec.gov/Archives/edgar/data/1506307/000150630726000002/kmi2025q48-kex991.htm
- Kinder Morgan, Q1 2026 results, EX-99.1, 22 April 2026 (Trident phase one Q1 2027). https://www.sec.gov/Archives/edgar/data/1506307/000150630726000033/kmi2026q18-kex991.htm
- Kinder Morgan, Q3 2026 results, EX-99.1, 21 October 2026 (Permian Link for a hyperscaler's power, Q3 2030; Creekside Lateral for data centres, Q4 2026 and Q4 2027). https://www.sec.gov/Archives/edgar/data/1506307/000150630726000130/kmi2026q38-kex991.htm
- Entergy Texas, "Entergy Texas partners with Kinder Morgan, Golden Pass LNG to fuel Southeast Texas growth", 31 January 2025. https://www.entergy.com/news/entergy-texas-partners-with-kinder-morgan-golden-pass-lng-to-fuel-southeast-texas-growth
- Press only, background, not cited for any body figure: S&P Global, 11 May 2026 (Golden Pass feedgas topped 400 MMcf/d on 8 May; ExxonMobil 1 May call: Train 2 mechanical completion Q4 2026, Train 3 Q2 2027) https://www.spglobal.com/energy/en/news-research/latest-news/natural-gas/051126-golden-pass-lng-exports-second-cargo-as-ramp-up-of-texas-facility-continues ; Argus, June 2026 (FERC approved preliminary Train 2 commissioning, not fuel gas) https://www.argusmedia.com/en/news-and-insights/latest-market-news/2843839-golden-pass-lng-approved-to-commission-train-2 ; RBN and others on Golden Pass's 1 Bcf/d commitment on Trident https://rbnenergy.com/daily-posts/analyst-insight/kinder-morgans-trident-pipeline-spears-fid
- Lead only, not cited for any figure: third-party YouTube video "The Entire Energy Sector Explained: Oil, Gas, Electricity & the Grid" (Leo Cui), https://www.youtube.com/watch?v=0zZyEF4Cq9U (research-build/source-watch-later/energy-sector-explained/TRANSCRIPT.md).

## Video figures dropped or flagged

- "Golden Pass loaded its first cargo in April 2026": confirmed by EIA (22 April 2026). Used.
- "US shipped out 15 billion cubic feet per day in 2025": EIA STEO October 2026 gives 15.1 Bcf/d for 2025. Confirmed, not used (national figure not needed).
- "Most of any country on Earth": not checked against a primary source. Dropped.
- "Minus 162 degrees Celsius, one six-hundredth of the volume": standard physics, not used in the body (kept in the glossary line for minus 162 only).
- "Cheniere sells much of its capacity under 20-year contracts with a fixed liquefaction fee": not used; contract terms and fees are financial and not needed for the mechanism.
- No wording, order or analogy from the video is used. The water-main analogy is original.

## Could not verify from primary material, not stated in the piece

- Golden Pass's contracted volume on Trident (1 Bcf/d, press only) and Entergy Texas's volume (not disclosed).
- Whether FERC has issued its order on CP25-205 (the piece says only that Golden Pass asked, in April 2025).
- Golden Pass Train 2 and 3 dates from a primary source dated after April 2026. EIA (23 April 2026) gave Train 2 in the second half of 2026 and Train 3 in the first half of 2027; press reports of ExxonMobil's 1 May call give Train 2 mechanical completion in Q4 2026 and Train 3 in Q2 2027. The piece does not state train dates; the falsifier names 2028 slippage as the likely failure route. ExxonMobil's 10-Qs for Q1 and Q2 2026 do not mention Golden Pass; its Q3 2026 results were not yet out on 29 October.
- Golden Pass's own news page (404). Its 22 April 2026 release was read only via press.
- Whether the Permian Link hyperscaler power plants are in Texas.
- Note for Tommy: Entergy Texas's plants are in MISO, not ERCOT. The piece says "Texas power plants" and "Southeast Texas", never ERCOT, for that reason. EIA's Texas power series covers all Texas plants, ERCOT and non-ERCOT.
