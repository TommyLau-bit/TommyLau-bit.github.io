# Data centre water draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/water-is-a-siting-problem.md` (draft: true)
Cover: `public/covers/water-is-a-siting-problem.svg`
Drafted 9 October 2026. Claim needs Tommy's approval before publish. Not committed.

## Proposed claim

Data centre water decides where AI campuses go and how they are cooled, not how many get built, because a site can swap evaporated water for a little extra electricity, and most of a data centre's water is consumed at the power station anyway.

### Alternatives considered

1. "The real water cost of AI sits at the power station, about twelve times the on-site figure." Rejected as the lead: it is a statistic, not a mechanism, and on its own it is hard to falsify. Kept as the evidence section.
2. "Liquid cooling will shrink data centre water use." Rejected: LBNL's own projection has average on-site water per kWh rising after 2023 (0.36 to 0.45-0.48 L/kWh), partly because of liquid-cooled systems. The chip loop is sealed; the roof (cooling tower or dry cooler) decides the water. The piece says so.

Chosen because it fits the site's argument (power is the scarce thing, so water is traded away by spending power), it agrees with the popular "water is a distraction" view only as far as the primary evidence goes, and it has two clean falsifiers: a powered campus cancelled outright on water, or Microsoft's WUE rising.

## claims.ts entry

```ts
  {
    id: 'water-is-a-siting-problem',
    claim: 'Data centre water decides where AI campuses go and how they are cooled, not how many get built, because a site can swap evaporated water for a little extra electricity, and most of a data centre\'s water is consumed at the power station.',
    breaksIf: 'A large AI campus with its power already secured is cancelled outright over water rather than redesigned to cool without it, or Microsoft\'s water per kilowatt-hour of computing climbs back above 0.30 litres, its fiscal 2024 level (0.27 in fiscal 2025), as its AI campuses grow.',
    watch: ['Microsoft\'s reported WUE each year', 'Whether Microsoft\'s zero-water sites in Phoenix and Mount Pleasant come online from late 2027 as planned', 'Permit refusals on water grounds in dry regions, and whether projects redesign or leave', 'On-site against power station water in the next national estimate'],
  },
```

## stack.ts

Layer `cooling`. Suggested order: `pieces: ['cooling-is-half-the-job', 'room-to-spare', 'water-is-a-siting-problem']`

## Glossary (heading: "Inside the building")

- `Cooling tower`: An open unit, often on the roof, that cools water by letting some of it evaporate. Cheap in electricity, but the evaporated water is lost for good.
- `Dry cooler`: A large radiator with fans that sheds heat to the outside air without evaporating any water. Saves water, costs more electricity on hot days.
- `Water withdrawal and consumption`: Withdrawal is water taken in and mostly returned, as at many power stations. Consumption is water lost for good, mostly as vapour. For data centres, consumption is the figure that matters.
- `WUE`: Water usage effectiveness. Litres of water a data centre consumes on site for each kilowatt-hour its computers use. Lower is better; zero means no water evaporated for cooling.
- Existing `Chiller` entry: none found; optionally add `Chiller`: a large refrigerator for a building's cooling water, which runs harder and draws more power when no water is evaporated.

## numbers.ts (physical figures only)

```ts
  { layer: 'cooling', value: '~12×', what: 'Water consumed at the power stations supplying American data centres, nearly 800 billion litres, against 66 billion litres consumed on site. Most of a data centre\'s water follows its electricity.', piece: 'water-is-a-siting-problem', asOf: '2023' },
```

## LinkedIn post (§9)

```
Most of a data centre's water is not used at the data centre.

Lawrence Berkeley National Laboratory estimates American data centres consumed 66 billion litres of water on site in 2023, and the power stations feeding them about twelve times that. On site, water is a choice: evaporate it to save electricity, or spend a little more power and use none, as Microsoft's new designs do. That makes water a question of where campuses go, not how many get built.

The piece covers how a cooling tower trades water for power, where the water really goes, and what would prove me wrong.

https://thephysicallayer.fyi/journal/water-is-a-siting-problem/

#DataCentres #Water #Cooling
```

## Sources (every figure)

- Lawrence Berkeley National Laboratory, Shehabi et al., "2024 United States Data Center Energy Usage Report", LBNL-2001637, December 2024: https://escholarship.org/uc/item/32d6m0d1 (PDF: https://escholarship.org/content/qt32d6m0d1/qt32d6m0d1.pdf; original eta-publications.lbl.gov link redirects there)
  - p. 55: direct (on-site) water 66 billion litres in 2023, 21.2 billion in 2014; hyperscale 60 to 124 billion litres in 2028.
  - p. 57: indirect water footprint "nearly 800 billion liters" in 2023 (176 TWh); 4.52 L/kWh indirect vs national grid average 4.35.
  - p. 48: average site WUE just over 0.36 L/kWh through 2023, rising to 0.45-0.48 after, partly from liquid-cooled systems.
  - p. 41-42: cooling towers evaporate water, "concerns regarding data center water consumption and availability at the local level"; dry coolers conserve water.
  - 6.7% to 12.0% of US electricity by 2028 (background, not in piece).
  - "about twelve times" in the piece = 800 / 66.
- Microsoft, "Sustainable by design: Next-generation datacenters consume zero water for cooling", 9 December 2024: https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/
  - "Traditionally, water has been evaporated on-site to reduce the power demand of the cooling systems."
  - "Starting August 2024, all new Microsoft datacenter designs began using this next-generation cooling technology."
  - WUE 0.30 L/kWh in the last fiscal year (FY2024), 39% better than 0.49 in 2021; "a nominal increase in our annual energy usage"; avoids more than 125 million litres per datacenter per year; Phoenix and Mt. Pleasant pilots in 2026, online from late 2027.
- Chile, Segundo Tribunal Ambiental, ruling Rol R-271-2020 (joined R-270-2020), dated 26 February 2024 (announced 27 February): https://media-front.elmostrador.cl/2024/02/2024.02.26_Sentencia_R-271-2020_Acum._R_N°_270-2020.pdf (verification code on www.tribunalambiental.cl)
  - Records that on 16 February 2022 Google filed with the SEA to replace water-based cooling towers with air-cooled chillers, eliminating groundwater use from the three wells it held rights to; SEA ruled on 7 June 2022 that no new assessment was needed. Court partly annulled the permit over the Santiago Central Aquifer assessment and climate change.
- Google restarting the Cerrillos project "from scratch" with air-cooled technology on the same site: reported 17 September 2024 (BioBioChile, https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2024/09/17/amp/alcaldesa-de-cerrillos-rechaza-nuevo-plan-de-data-center-de-google-la-prioridad-es-el-medioambiente.shtml). See below.

## Could not verify / left out

- Google's own September 2024 letter to Chile's SEA was not retrieved; the "start again on the same site, cooled by air" line rests on press reports of it (BioBioChile, Semafor) plus the court record of the 2022 air-cooling filing. If Tommy wants primary only, cut the last clause of that sentence to "and the project went back to the start."
- Semafor reported the original design at 7.6 million litres of potable water a day; not in the court text I checked, so left out.
- One secondary source (Climate Case Chart) dates the ruling 26 September 2024; the signed ruling itself is dated 26 February 2024, which is what the piece uses.
- Not used: Tucson "Project Blue", Arizona and Spain permit fights, Meta "water positive", Amazon recycled water, USGS national totals, golf course comparisons. No primary source checked for them in this pass.
- Microsoft's FY2025 WUE (if published in its 2025/2026 environmental report) not checked; the falsifier uses the FY2024 figure from the December 2024 post.
