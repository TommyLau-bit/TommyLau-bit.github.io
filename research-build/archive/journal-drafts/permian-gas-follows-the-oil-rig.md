# Permian associated gas draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/permian-gas-follows-the-oil-rig.md` (draft: true)
Cover: `public/covers/permian-gas-follows-the-oil-rig.svg`
Drafted 29 October 2026. First piece under the oil exception (WRITING-FORMAT §5): physical system only. No oil or gas price forecast, no trading view, no breakeven prices, no views on shares. The one historical price fact used (Waha below zero on 42 per cent of 2024 trading days) is evidence that the pipe, not the buyer, binds; it carries no forecast. Topic approved by Tommy; the final claim wording needs his approval before publish.

## Proposed claim

Permian gas is a by-product of oil wells, so how much there is for Texas power plants and data centres is set by oil drilling and pipeline space, not by power buyers: through 2027, power buyers will not pull new Permian drilling, so gas-directed rigs stay at or below one in ten of the basin's rigs and no producer adds Permian rigs or wells to meet gas contracts with power plants or data centres.

Title (revised after fact-check): "Oil drillers, not power buyers, decide how much Permian gas there is". Thesis line: "In the Permian, gas follows the oil well, not the data centre." 

### Alternatives considered

1. "Pipelines, not wells, cap how much Permian gas reaches Texas power buyers, so Waha keeps trading at a deep discount until Blackcomb and Hugh Brinson fill." Rejected: the test would be a price spread, which edges towards a price call, and it drops the oil-drilling half of the mechanism.
2. "Permian gas output rises faster than Permian oil output every year through 2027, because the gas-to-oil ratio keeps climbing." Rejected as the lead: true per EIA but narrow and technical for a layman, and it does not touch the power buyer at all. Kept as a supporting line (the 4,200 cubic feet per barrel ratio).

Chosen because it is new to the site (the fuel behind the grid and behind on-site turbines, one step upstream of every existing layer), it rests on a physical mechanism (associated gas, fast shale decline, pipeline takeaway), and it has a dated, cleanly observable test in EIA's own regional series. It builds on the-way-out-has-its-own-queue (linked: on-site power swaps the grid queue for equipment queues; this piece adds that the fuel has its own master, the oil driller) and sits beside ercot-rations-the-plug and abilene-switched-on-in-stages (Texas grid and campus) without repeating them. GE Vernova appears only in the exposure map. Contradicts none.

Note on the brief's outline: the brief allowed for rigs falling through 2027. In fact Permian rigs bottomed in early 2026 (242 in Q1 2026) and have since recovered (264 in Q3 2026 per EIA; about 272 in late October per Reuters and RBN summaries of Baker Hughes, press only). After the fact-check, the falsifier was changed from an output threshold (28.4 Bcf/d, about 15 per cent below EIA's own Q4 2027 forecast, so close to consensus and unable to separate oil-push from buyer-pull) to two buyer-pull tests: a numeric gas-directed rig share from Baker Hughes, and a producer statement tying new Permian drilling to power-buyer gas contracts. The current baseline share of gas-directed Permian rigs was not verified (Baker Hughes site 403); it should be read in a browser before publish.

## claims.ts entry

```ts
  {
    id: 'permian-gas-follows-the-oil-rig',
    claim: 'Permian gas is a by-product of oil wells, so how much there is for Texas power plants and data centres is set by oil drilling and pipeline space, not by power buyers. Through 2027, power buyers will not pull new drilling in the Permian.',
    breaksIf: 'By 31 December 2027, Baker Hughes\' weekly rig count shows more than one in ten Permian rigs drilling for gas rather than oil, or a Permian producer says it is adding rigs or wells to meet gas contracts with power plants or data centres.',
    watch: ['Baker Hughes weekly split of Permian rigs into oil-directed and gas-directed', 'Permian producers\' statements on drilling plans and gas sales contracts with power plants and data centres', 'EIA Short-Term Energy Outlook Table 10a, Permian active rigs and new wells drilled per rig', 'EIA Short-Term Energy Outlook Table 5a, Permian region marketed natural gas production', 'In-service dates and flows on Blackcomb, Hugh Brinson, the Gulf Coast Express expansion and Traverse'],
  },
```

## stack.ts: proposed new layer (no existing layer fits)

No existing layer covers fuel supply. The physical chain runs fuel, then the power station, then the grid connection, then the site. So the new layer goes first in `STACK`, before `grid`:

```ts
  {
    id: 'fuel',
    name: 'Fuel for power',
    kind: 'energy',
    what: 'The fuels power stations burn or split, gas by pipeline and uranium made into reactor fuel, travel from where they are produced to the plant.',
    constraint: 'Fuel supply is set by producers, processors and pipelines with their own clocks, not by the power buyer at the end of the chain.',
    pieces: ['permian-gas-follows-the-oil-rig'],
  },
```

The layer is written generically so that other fuel pieces (for example terrapower-waits-on-the-fuel, if it publishes) can join it; the Permian point stays in the piece. The header comment in stack.ts ("from the grid connection inward") would need one word changed at publish, e.g. "from the fuel and the grid connection inward".

**Descent.astro needs a new stop drawn by hand** (not edited here, per brief): a new stop above the grid connection stop, in its physical place at the top of the descent, with its drawing (e.g. a wellhead and a pipeline running to a power station) and step cards. The layer index, closing funnel and stop counter pick the layer up on their own (WRITING-FORMAT §6a).

## Glossary (heading: "Getting power to the building", beside Behind the meter)

- `Associated gas`: Natural gas that flows out of an oil well alongside the crude. It is produced because the oil is drilled for, so its supply follows oil drilling rather than gas demand. Most Permian gas is made this way.
- `Casinghead gas`: The Texas legal term for gas produced from an oil well. Burning it off at the well needs an exception from the Railroad Commission of Texas.
- `Gas-to-oil ratio`: Cubic feet of gas produced for every barrel of oil. In the Permian it averaged nearly 4,200 in 2025 and is rising, so each barrel brings more gas.
- `Rig count`: The number of drilling rigs at work, counted weekly by Baker Hughes. It measures how many new wells are being drilled, not how much is being produced.
- `Takeaway capacity`: How much gas the pipelines leaving a field can carry. When production outruns it, gas is stranded, prices at the local hub (Waha, for the Permian) can fall below zero, and some is flared.
- `Bcf a day`: Billion cubic feet of gas a day, the usual unit for gas production and pipeline capacity.

## numbers.ts (physical figures only, layer `fuel`)

```ts
  // fuel for power
  { layer: 'fuel', value: '302 → 242', what: 'Rigs drilling in the Permian Basin in early 2025 and early 2026. Over the same year the basin\'s gas output rose by about a twelfth, because gas comes up oil wells as a by-product.', piece: 'permian-gas-follows-the-oil-rig', asOf: 'Q1 2026' },
```

Optional second: `{ layer: 'fuel', value: '~1/3 a year', what: 'Share of the Permian\'s gas output that wells already flowing lose each year, from EIA\'s monthly estimate of about 0.8 Bcf/d. New wells must replace it for supply just to hold level.', piece: 'permian-gas-follows-the-oil-rig', asOf: 'Q3 2026' }`

## LinkedIn post (§9), slot to be assigned at publish (next free Mon/Wed/Fri 11:30 after the latest scheduled post)

```
Most of the gas from the Permian Basin, which Texas power stations burn, is a by-product of oil wells.

In the year to early 2026 the Permian Basin lost a fifth of its drilling rigs, yet its gas output rose by about a twelfth. Oil drillers and pipeline space decide how much gas there is, not the buyers of the power, so a gas-fired plant in West Texas is tied to decisions made about oil.

The piece covers how associated gas is made, why pipelines decide how much gets out, and what would prove me wrong.

https://thephysicallayer.fyi/journal/permian-gas-follows-the-oil-rig/

#Energy #DataCentres #NaturalGas
```

## Figures used in the body, with primary source (after fact-check)

1. "Most Permian gas is made this way" and wells bring more gas per barrel than they used to (gas-to-oil ratio nearly 4,200 cubic feet per barrel in 2025, 15 per cent above 2021; the number itself is cut from the piece): EIA STEO, September 2026, natural gas production section, p. 8 to 9.
2. "Roughly a third of the basin's gas output a year": EIA STEO October 2026, Table 10a, existing natural gas production change, Permian region, -827.5 MMcf/d a month (Q3 2026), LOWESS-smoothed; my arithmetic 0.8 x 12 = 9.6 Bcf/d against 29.5 Bcf/d for 2026 (Table 5a), about 33 per cent.
3. Rule 32: flaring allowed for a short window after completion (10 producing days) and for small low-pressure volumes; beyond that, an exception from the Railroad Commission; unavailable pipeline is a recognised ground: Railroad Commission of Texas, Statewide Rule 32 handout and exception slides.
4. Matterhorn Express opened October 2024 (EIA Today in Energy, 3 February 2025); FID May 2022, so "nearly two and a half years" (Business Wire URL date and Oil & Gas Journal; PRESS-CONFIRMED for the FID date). Capacity 2.5 Bcf/d cut from the piece.
5. Waha below zero on 42 per cent of 2024 trading days, attributed by EIA to Permian production exceeding pipeline takeaway; presented only as a pipeline limit, no price comment: EIA Today in Energy, 3 February 2025.
6. Rigs fell by a fifth in the year to early 2026 (302 in Q1 2025 to 242 in Q1 2026), new wells drilled per rig 4.8 to 5.5: EIA STEO October 2026, Table 10a (Baker Hughes rig data).
7. Gas output rose by about a twelfth over the same year (26.3 to 28.4 Bcf/d, +8.0 per cent): EIA STEO October 2026, Table 5a, Permian region.

Body: 534 words; checker 0 failures, 0 warnings.

## Sources, one per line

- EIA, Short-Term Energy Outlook, October 2026 (released 6 October 2026), Tables 4a, 5a, 10a and 10b. https://www.eia.gov/outlooks/steo/ ; https://www.eia.gov/outlooks/steo/tables/pdf/5atab.pdf ; https://www.eia.gov/outlooks/steo/tables/pdf/10atab.pdf ; https://www.eia.gov/outlooks/steo/tables/pdf/4atab.pdf ; full report https://www.eia.gov/outlooks/steo/archives/oct26.pdf
- EIA, Short-Term Energy Outlook, September 2026, natural gas production section (GOR, associated gas, Hugh Brinson began interstate shipments in June 2026). https://www.eia.gov/outlooks/steo/archives/sep26.pdf
- EIA, Today in Energy, "Natural gas spot prices fell across key regional trading hubs in 2024", 3 February 2025 (Matterhorn October 2024, 2.5 Bcf/d; Waha 42 per cent). https://www.eia.gov/todayinenergy/detail.php?id=64445
- EIA, Today in Energy, "Natural gas pipeline capacity from the Permian Basin is set to increase", 10 September 2024 (Matterhorn route to Katy; Permian gas "primarily associated gas"). https://www.eia.gov/todayinenergy/detail.php?id=63044
- EIA, Today in Energy, "Most planned natural gas pipeline capacity additions in 2026 and 2027 originate in Texas", 26 May 2026 (Blackcomb 2.5 Bcf/d, Q3 2026 target; Hugh Brinson 2.2 Bcf/d). https://www.eia.gov/todayinenergy/detail.php?id=67707 (background only, not cited in the body)
- EIA, Today in Energy, "U.S. natural gas production reached a record high in July 2026", 2 October 2026 (Permian-led record; rising GOR; Hugh Brinson flows). https://www.eia.gov/todayinenergy/detail.php?id=68225 (background only)
- Railroad Commission of Texas, Statewide Rule 32 flaring handout and exception slides. https://www.rrc.texas.gov/media/wftn5jh5/statewide-rule-32-flaring-handout.pdf ; https://www.rrc.texas.gov/media/mfbl4out/statewide-rule-32-exception-to-flaring-venting-of-produced-gas-seyed-k-mahjour.pdf
- WhiteWater, "Matterhorn Express Pipeline Reaches Final Investment Decision", Business Wire, 19 May 2022 (403 to automated fetch). https://www.businesswire.com/news/home/20220519005711/en/Matterhorn-Express-Pipeline-Reaches-Final-Investment-Decision
- Press only, background, not cited in the body: Oil & Gas Journal, "Permian gas-pipeline debottlenecking advancing at full speed", 8 June 2026 (Waha negative on 118 of the first 131 days of 2026; project list). https://www.ogj.com/pipelines-transportation/pipelines/article/55378380/permian-gas-pipeline-debottlenecking-advancing-at-full-speed ; Reuters via BOE Report, 9 October 2026 (Permian 274 rigs, highest since June 2025). https://boereport.com/2026/10/09/us-energy-firms-add-rigs-for-fourth-time-in-five-weeks-to-highest-since-2024-baker-hughes-says/
- Lead only, not cited for any figure: third-party YouTube video "The Entire Energy Sector Explained: Oil, Gas, Electricity & the Grid" (Leo Cui), https://www.youtube.com/watch?v=0zZyEF4Cq9U (research-build/source-watch-later/energy-sector-explained/TRANSCRIPT.md).

## Video figures dropped or flagged

- "13.6 million barrels a day" US crude in 2025: EIA's October 2026 STEO estimate is 13.66 million b/d (Table 4a), so the video rounds down; it would read 13.7. Dropped: national oil output is not needed for the mechanism.
- "About 5 per cent fewer rigs" in the Lower 48 in 2025: not verified (EIA Table 10a has no 2024 baseline in this edition; Baker Hughes blocked). Dropped. The piece uses EIA's Permian-only series instead (302 to 242, a fifth fewer).
- "Nearly half of American crude from the Permian": consistent with EIA (6.58 of 13.66 million b/d in 2025, 48 per cent). Not used.
- Dallas Fed survey breakeven (about $65 a barrel) and WTI average: excluded entirely, per brief and the oil exception.
- GE Vernova backlog 83 to 116 GW: not used here (covered by ge-vernova-sells-the-wait).
- The video's general shale "treadmill" framing is replaced by EIA's own decline series; no wording, order or analogy from the video is used. The sawdust analogy is original.

## Not used, could not verify from primary material

- A current Baker Hughes count of Permian gas-directed rigs (Baker Hughes site 403; press summaries give only Permian totals). The falsifier's "drilling mainly for gas" leg is therefore stated in words; Tommy may prefer a numeric threshold once the split is read from Baker Hughes in a browser.
- Blackcomb's in-service status as of 29 October 2026 (targeted Q3 2026 by EIA in May; Wood Mackenzie expected Q4 at reduced initial capacity). Not stated in the piece.
- A first-year Permian well decline percentage from EIA. EIA does not publish one currently; industry figures (65 to 85 per cent, IHS; over 70 per cent, Rystad) are not EIA's. The piece uses EIA's monthly existing-well decline instead.
- 2026 Permian flaring volumes from the Railroad Commission. Not used.
