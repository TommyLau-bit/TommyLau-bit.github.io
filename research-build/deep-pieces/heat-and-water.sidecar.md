# Sidecar: heat-and-water (deep piece, cluster 8)

Cluster 8, "Heat and water decide where AI goes". Drafted 30 Oct 2026 to BRIEF-DEEP.md, matching the-queue-not-the-chip prototype. Piece: `research-build/deep-pieces/heat-and-water.md` (draft: true), kept outside `src/content/journal/`. Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "Heat and water decide where AI goes: liquid to the chip, a choice on the roof" (16 words, sentence case; the plan's working title plus the mechanism).
- Top layer (cold open, analogy, How it works, The number that matters): about 520 words, 8 figures, 0 company financial figures. Analogy about 69 words.
- Investor layer: about 1,930 words before the exposure map; map about 130 words including heading and the exact disclaimer pair plus the prototype's evidence sentence. Whole body about 2,710 words.
- Revised 30 Oct 2026 after the coordinator's fact-check (8 points); see "Fact-check fixes applied" at the end.
- `brand/check-piece.py`, run on a scratch copy: 0 failures, 0 warnings (after replacing "Data Center" in the LBNL report title in the sources line with a description).
- Category is Analysis (the piece carries a claim). The two absorbed live pieces were Explainers.

## Frontmatter notes

- `date: 2026-08-21` is a placeholder (cooling-is-half-the-job's date); at go-live it becomes the real publish time.
- New slug `heat-and-water`. None of the three absorbed slugs is reused: cooling-is-half-the-job is a mechanism Explainer, room-to-spare is about one building, water-is-a-siting-problem never went live.
- `cover: "/covers/cooling.svg"` (existing) until a new one is drawn.
- Tags: cooling, data-centres, liquid, water. "water" is a new tag; drop it if the tag list is closed.

## Thesis and decisions

Thesis: heat decides how AI is cooled (liquid to the chip); water decides where and how the heat leaves the building, not how many halls get built. The new mechanism, which no live piece has, comes from LBNL's simulations: because a liquid loop runs warm, swapping a cooling tower for a dry cooler costs almost no PUE in a liquid-cooled hall (about 1.1 either way) while water falls from about 2 L/kWh to 0. In an air-cooled midsize hall the same swap costs about 0.3 of PUE. The piece says plainly that LBNL also projects average WUE rising, partly from liquid-cooled systems: liquid makes waterless cheap, it does not make it happen.

**Room-to-spare: kept here, with a note for cluster 11.** Its evidence is cooling and density (140 kW racks, a hall "retrofitted for liquid cooling", 85 to 90% of heat through cold plates, cooling proved the flexible part). That is the heat half of this piece's chain, so the section and anchor live here, as the approved plan says. Its headline thesis, power not floor space sets the limit, belongs to cluster 11 (with power-first-chips-last, the same Jane Street tour). The section here states the power point in two sentences and links to power-first-chips-last; the cluster 11 deep piece should link to `/journal/heat-and-water/#room-to-spare` rather than repeat the density figures. If Tommy prefers, the redirect could point at cluster 11 instead; the section would then shrink to one paragraph here.

**Water claim status: proposed, not on record (for Tommy's decision).** `water-is-a-siting-problem` has an entry in `src/data/claims.ts` (no `date`, no `home`), but its piece never went live, and claims.astro shows a claim only once its home piece is live. Treated like seagate's in the-chip-supply-chain: a proposed claim, not on record, so it is NOT quoted under Claims on record. The deep piece's new claim is the first on record for this cluster. Its text, for Tommy:

> Claim: "Data centre water decides where AI campuses go and how they are cooled, not how many get built, because a site can swap evaporated water for a little extra electricity, and most of a data centre's water is consumed at the power station."
> Breaks if: "A large AI campus with its power already secured is cancelled outright over water rather than redesigned to cool without it, or Microsoft's water per kilowatt-hour of computing climbs back above 0.30 litres, its fiscal 2024 level (0.27 in fiscal 2025), as its AI campuses grow."

Options: (a) remove the entry at merge, since the new claim carries its cancellation limb and its mechanism; (b) keep it with `home: 'heat-and-water'`, dated at go-live. Recommend (a). Notes if kept: Microsoft's 0.27 counts withdrawals and is probably fiscal-year, matching the claim's wording; the "little extra electricity" is near zero for liquid-cooled halls but about 0.3 of PUE for air-cooled midsize halls (LBNL).

Johor's water is not repeated; one sentence links to `/journal/the-queue-not-the-chip/#johor-waits-on-the-treatment-plant`. Singapore's PUE 1.25 condition is linked to `#two-governments-one-confession`.

## Proposed claims.ts change (existing entries untouched)

Existing `water-is-a-siting-problem` entry: Tommy's decision, see Water claim status above (recommend removing it at merge; if kept, add only `home: 'heat-and-water'` and no `date`).

New entry:

```ts
  {
    id: 'heat-and-water',
    claim: 'In AI data centres heat sets the cooling method and water sets where and how the heat leaves the building, not how many halls get built: every Google campus that Google itself names as at high water risk (Mesa, Waltham Cross and Canelones) will consume under 50 million gallons of water in each of 2026 and 2027, and no hyperscaler will report a new evaporatively cooled campus drawing on a water source it rates at high risk.',
    breaksIf: 'Google reports consumption of 50 million gallons or more in 2026 or 2027 at Mesa, Waltham Cross or Canelones; or Google, Microsoft, Amazon or Meta reports opening a data centre cooled by evaporating water from a source it rates at high risk of depletion or scarcity; or a large AI campus with its power already secured is cancelled outright over water rather than redesigned to cool without it.',
    watch: ['Google\'s per-site water table each year (Mesa 9.7 million gallons consumed in 2025; Waltham Cross and Canelones not yet listed)', 'Google\'s share of freshwater withdrawal from high-risk sources (15%, 14%, 13% for 2023 to 2025)', 'New campuses disclosed by Microsoft, Amazon and Meta with their cooling and water source', 'Henderson, Nevada (239.4 million gallons consumed in 2025) and how Google rates its source', 'Permit refusals on water grounds, and whether projects redesign or leave'],
  },
```

Why these tests (rewritten after fact-check): the first draft's Google share test (at or below 15%) was the default outcome, since the series is falling (15%, 14%, 13% for 2023 to 2025), and an AWS WUE rise could confirm rather than break the thesis (more evaporation where water is plentiful is the trade working). The new test is site-level and comes from Google's own words: it named Waltham Cross, Mesa and Canelones as high water risk and air-cooled (2025 report pp.40 to 41). Mesa consumed 9.7 million gallons in 2025 against 469 at The Dalles; 50 million is about five times Mesa and about a tenth of a water-cooled campus, so crossing it means evaporative cooling, not humidification. The hyperscaler limb tests the policy beyond Google; the cancellation limb is kept. Honest gap: Henderson, Nevada, a dry basin, consumed 239.4 million gallons in 2025, and Google does not publish its rating of that source; the piece says so openly. Waltham Cross and Canelones have no row in the 2026 table yet (not operating or not reported), so they bite only once listed.

## Redirect map

| Old URL | Redirect to |
|---|---|
| /journal/cooling-is-half-the-job/ | /journal/heat-and-water/#cooling-is-half-the-job |
| /journal/room-to-spare/ | /journal/heat-and-water/#room-to-spare |

water-is-a-siting-problem was never live, so no redirect is needed; its anchor exists anyway. At merge its draft leaves `src/content/journal/` and goes, with the two live originals, verbatim into `research-build/archive-pieces/`. Its scheduled publish task (13 Nov) should be paused with the others, on Tommy's go.

Sections and anchors, in order: The mechanism in depth; Why heat forced liquid to the chip (#cooling-is-half-the-job); Inside one hall: Jane Street's retrofit (#room-to-spare); Water: a choice made site by site (#water-is-a-siting-problem); Claims on record; What would prove me wrong; Research notes.

## stack.ts

Layer `cooling`: `pieces: ['heat-and-water']`. The layer's `constraint` text, "Air stops working somewhere between 30 and 50 kilowatts per rack", has no primary source (see Figures flagged). Proposed: "Heat must leave the building through a cooling tower that evaporates water or a dry cooler that uses more power." Needs Tommy's go.

## Glossary (src/pages/glossary.astro, "Inside the building")

New:
- Airside economiser: Cooling a data hall with outside air whenever the weather allows, so the chillers can rest. Often paired with a little evaporated water on hot days (adiabatic cooling).
- Waterside economiser: Cooling a building's water loop with a cooling tower or cold outside air instead of a chiller whenever conditions allow. Efficient, but a tower evaporates water.
- Adiabatic cooling: Cooling air by evaporating a small amount of water into it or over pads in front of a coil. Uses far less water than a cooling tower, and only on hot days.
- Heat rejection: The last step of cooling, where a building's heat is released to the outside air, by evaporating water or through a dry radiator.
- Water risk (watershed): How likely the local water supply is to run short or be depleted. Google rates the sources it draws from as low, medium or high risk and reports the split.

Existing entries needing a decision (not edited):
- `WUE` says "consumes on site". AWS reports water withdrawn per kWh of IT load. Suggest adding: "Companies differ: some report water consumed, others water withdrawn."
- `Rack` says "a current AI rack is near 200" kW; this piece uses Jane Street's 140 kW for a GB300 NVL72. Not contradictory (different racks), but worth a source check.
- `PUE` ("old air-cooled sites near 2.0, modern liquid-cooled near 1.1") is now backed by LBNL's simulations; no change.
- Already present, no change: Cooling tower, Dry cooler, Chiller, Water withdrawal and consumption, Cold plate, CDU, Direct-to-chip cooling, Immersion cooling, Busway, Hyperscaler, TPU.

## numbers.ts (physical only)

New:
```ts
  { layer: 'cooling', value: '~2 L to ~0', what: 'Water evaporated per kilowatt-hour in a large liquid-cooled hall using a cooling tower, against a dry cooler, in LBNL\'s simulations. PUE stays about 1.1 either way.', piece: 'heat-and-water', asOf: '2024' },
  { layer: 'cooling', value: '9.7 vs 469', what: 'Million gallons of water consumed in 2025 at Google\'s air-cooled Mesa campus, where it judged the source high risk, against its water-cooled campus at The Dalles, Oregon.', piece: 'heat-and-water', asOf: '2025' },
```
Existing entries needing Tommy's decision at merge (not edited):
- `85–90%` (Jane Street): repoint `piece` to heat-and-water.
- `~12×` (LBNL water): repoint `piece` to heat-and-water.
- `~140 kW` (layer distribution, piece room-to-spare): repoint to heat-and-water.
- `30–50 kW` (cooling-is-half-the-job): no primary source; suggest removing.
- `5–10 kW` traditional rack (cooling-is-half-the-job): no primary source found; Jane Street's tour gives 10 to 40 kW for an air-cooled cabinet. Suggest replacing or removing.

## LinkedIn post (§9)

```
A liquid-cooled AI hall can go from about 2 litres of water per kilowatt-hour to almost none, and barely change its power use.

That is what Lawrence Berkeley National Laboratory's simulations show when a cooling tower is swapped for a dry cooler. Heat has pushed AI chips onto liquid, and the liquid runs warm enough to cool without evaporating water. So water decides where and how AI halls are cooled, not how many get built. Google air-cools its campuses where it judges the water source at high risk: its Mesa, Arizona site used 9.7 million gallons in 2025, against 469 million at its water-cooled campus in Oregon.

The piece covers the cooling chain, PUE and water use by cooling method, Jane Street's retrofit, and the claims I have on record.

https://thephysicallayer.fyi/journal/heat-and-water/

#DataCentres #Cooling #Water
```

## Cover proposal (not drawn)

`/covers/heat-and-water.svg`. A single rack seen side on, glowing amber, with one blue pipe leaving it and forking on the roof: left fork to a small cooling tower with three grey vapour curls, right fork to a flat radiator with a fan and no vapour. Caption in letter-spaced grey: "HEAT AND WATER DECIDE WHERE AI GOES". Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Sources, every one with date

Opened by me on 30 Oct 2026:
- Lawrence Berkeley National Laboratory, Shehabi et al., "2024 United States Data Center Energy Usage Report", LBNL-2001637, December 2024: https://escholarship.org/uc/item/32d6m0d1 (PDF https://escholarship.org/content/qt32d6m0d1/qt32d6m0d1.pdf; curl got a CloudFront 403, WebFetch retrieved it, text extracted with pypdf). PDF pages: Table 4.2 (cooling systems) pp.41 to 43; Table 4.3 (W45 for AI liquid) p.44; Figure 4.2 (cooling distribution 2023) p.40; Figure 4.4 (simulated PUE and WUE by system) p.47; "rarely the case" p.45; hyperscalers report 0.1 to 0.3 L/kWh p.48; Figure 4.5 (aggregate 2023: small 1.91/0.32, midsize and colo 1.68/0.67, hyperscale 1.22/0.32, AI specialised 1.14/0.61) p.48; PUE 1.6 (2014) to 1.4 (2023) p.48; WUE just over 0.36 to 0.45 to 0.48, "increased water consumption of liquid-cooled systems" p.49; 66 billion litres p.56; "nearly 800 billion liters", 4.52 L/kWh p.58; 965 weather stations p.44.
- Google 2026 Environmental Report (FY2025): https://sustainability.google/files/1699a2e19277e478b38a659f00cb38398a836e8c/download-1699a2e1.pdf . Fleet PUE 1.09 (pp.34, 95); water "highly efficient means of cooling that requires less energy than air-cooling technologies", 10.9 billion gallons (41 billion litres) data centres and offices, +34% (p.35); The Dalles risk framework, 469 million gallons, 6 to 10% overhead Q4 2025 (p.35); data table: data centre consumption 10,523 million gallons, withdrawal 14,689 total (11,011 in 2024), freshwater withdrawal 72% low, 15% medium, 13% high risk (p.96); Uptime 2025 average PUE 1.54 cited in footnote 7.
- Google Cloud blog, "Enabling 1 MW IT racks and liquid cooling at OCP EMEA Summit", Iyengar and Huffman, 30 Apr 2025: https://cloud.google.com/blog/topics/systems/enabling-1-mw-it-racks-and-liquid-cooling-at-ocp-emea-summit ("GigaWatt scale across more than 2000 TPU Pods", TPU v3 in 2018, ~99.999% CDU availability since 2020, 10 kW to 100 kW, more than 500 kW per rack before 2030).
- AWS sustainability page, 2025 figures: https://aws.amazon.com/sustainability/ (PUE 1.14 in 2025, 1.15 in 2024; "global data center WUE of 0.12 liters of water withdrawn per kilowatt-hour of IT Load (L/kWh) in 2025", "a 20% improvement from 2024").
- Microsoft, "Inside Microsoft's two-decade push to cut water intensity while scaling for growth", Priest and Solomon, 24 Jun 2026: https://blogs.microsoft.com/blog/2026/06/24/inside-microsofts-two-decade-push-to-cut-water-intensity-while-scaling-for-growth/ (0.27 L/kWh "in 2025"; about 90% of 2025 owned fleet "low- to zero-water cooling").
- Jane Street, "A look inside our newest data center" (undated page): https://www.janestreet.com/culture/street-view/a-look-inside-our-newest-data-center/ (guides Ron Minsky, co-head of the tech group, and Dan Pontecorvo, physical engineering; "4,032 GPUs across 56 racks, retrofitted for liquid cooling"; Dwarkesh Patel, quoted: "the whole grid interconnect wattage of the datacenter taken up by racks that fit in a small fraction of the space originally allotted for chips"). Dates: Patel's post with the tour video is 15 May 2026 (search results); the separate longer sit-down conversation is the one power-first-chips-last dates 21 May 2026. The piece uses 15 May for the tour.
- Google 2025 Environmental Report: https://www.gstatic.com/gumdrop/sustainability/google-2025-environmental-report.pdf , pp.40 to 41 (Waltham Cross water sources "present a high risk of water depletion and scarcity", air cooling chosen; same for Mesa, Arizona and Canelones, Uruguay, under development). Opened 30 Oct 2026.
- Google 2026 Environmental Report per-site table p.97: Mesa, AZ 9.7 million gallons consumed; Henderson, NV 239.4; The Dalles 469.0; Council Bluffs 1,346.0. Opened 30 Oct 2026.
- Google Cloud blog, "Assessing watershed health in data center host communities", Ben Townsend, 15 Dec 2023: https://cloud.google.com/blog/topics/sustainability/assessing-watershed-health-in-data-center-host-communities ("If it's high risk, we will pursue alternative sources or cooling solutions"; Mesa air-cooled).
- Google high-risk withdrawal share 15% (FY2023, 2024 report) and 14% (FY2024, 2025 report): from the coordinator's fact-check; 13% (2025) opened by me in the 2026 report p.96.
- AWS WUE series 0.25, 0.19, 0.18, 0.15, 0.12 (2021 to 2025): 0.15 for 2024 is primary (AWS 2024 Sustainability Report summary, per the fact-check). The 2024 wording may define WUE differently from 2025's "litres withdrawn per kWh of IT load"; the piece uses only the 2025 figure.
- The Green Grid, WP#35, WUE, 1 Mar 2011: https://www.thegreengrid.org/product/114 (metric origin and date only; full text behind sign-in, not read).
- Schneider Electric / Motivair, 17 Oct 2024: https://www.motivaircorp.com/news/schneider-electric-acquires-controlling-interest-i/ (seen in search results; not opened).
- Eaton completes Boyd Thermal, 12 Mar 2026: https://www.businesswire.com/news/home/20260312582488/en (seen in search results; not opened).

From the water sidecar (primary, verified 9 Oct 2026, not re-opened):
- Microsoft, "Sustainable by design: Next-generation datacenters consume zero water for cooling", 9 Dec 2024: https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/
- Chile, Segundo Tribunal Ambiental, Rol R-271-2020 (joined R-270-2020), 26 Feb 2024: https://media-front.elmostrador.cl/2024/02/2024.02.26_Sentencia_R-271-2020_Acum._R_N°_270-2020.pdf

From the live piece room-to-spare (not re-opened): Jane Street's video tour with Dwarkesh Patel, 15 May 2026 (140 kW, 10 to 40 kW, 85 to 90%, pipes flexible, busway and breakers, fixed utility allocation).

## Figures dropped or flagged

- "Air fails between 30 and 50 kW per rack" (cooling-is-half-the-job, stack.ts, numbers.ts): no primary source found; dropped, and said so openly in the section.
- "Water carries heat roughly three thousand times better per unit volume": physics, not a dated source; the top layer says "thousands of times more" instead.
- "A normal rack drew 5 to 10 kW" (cooling-is-half-the-job): no primary; replaced by Jane Street's 10 to 40 kW air-cooled cabinet.
- "Some cooling designs evaporate millions of gallons a year": vague, dropped; Google's 469 million gallons at The Dalles used instead.
- Eaton and Schneider deal values (US$9.5bn, about US$850m): money figures, kept out; dates only.
- Uptime Institute 1.54: used only as cited in Google's own report footnote. Uptime's own press release (30 Jul 2025) gives no number; the 19% liquid cooling adoption figure circulating is secondary only and NOT used.
- No primary industry-wide liquid cooling share found. The piece uses LBNL's Figure 4.2, as read by me (roughly two thirds of AI specialised space on liquid in 2023), labelled as a model estimate.
- LBNL Figure 4.4 values are my readings of box-plot medians from the chart image, rounded (PUE to 0.1, WUE to about 0.1 to 0.2). The piece says "as I read them from its Figure 4.4, rounded". A fact-checker should re-read the chart.
- Meta's PUE and WUE: only secondary figures found (about 0.20 L/kWh at new campuses); not used. Meta stays in the exposure map as an operator.
- Google's Santiago restart "from scratch" on air cooling (press only, BioBioChile): not used; the piece keeps only the court record.
- Google's 2026 pledge to air-cool where water is high risk: press only (9to5Google, Shopifreaks); not used.
- Semafor's 7.6 million litres a day for the Chile design: not used.
- Exposure map trimmed: ABB, Asetek, Delta and LiteOn no longer appear in this cluster's map; their company pages lose these links at merge.

## Edits other drafts need (not made)

- `src/content/journal/johor-waits-on-the-treatment-plant.md` (held) links to water-is-a-siting-problem; at merge, point it to `/journal/heat-and-water/#water-is-a-siting-problem` (its own text is archived; the queue deep piece already carries its section).
- `src/content/journal/power-first-chips-last.md` (cluster 11): the cluster 11 deep piece should link to `/journal/heat-and-water/#room-to-spare` for the density and cooling evidence.
- `research-build/journal-drafts/schneider-sells-the-finished-system.md` cites "cooling is already covered by cooling-is-half-the-job, room-to-spare and every-megawatt-got-harder"; update the slugs at merge.
- stack.ts cooling `constraint` and glossary `WUE` as above.

## Could not verify today

- Jane Street figures from the video (140 kW, 10 to 40 kW, 85 to 90%, busway, fixed utility allocation) rest on the live piece; Jane Street's write-up confirms only 4,032 GPUs, 56 racks, liquid retrofit and the small fraction of space.
- AWS 2024 WUE of 0.15 is primary per the fact-check; no longer used in the piece or claim.
- Microsoft's 0.27 counts withdrawals (per the fact-check) and is labelled "water withdrawn" and "likely its fiscal year to June" in the operator table.
- Microsoft's 0.27 is "in 2025" in its June 2026 post, not explicitly fiscal 2025, which is how the water claim (fixed text) words it. The piece notes this.
- The Schneider and Eaton releases were seen only in search results; dates match across several reports.
- The Green Grid white paper text was not read (sign-in).

## Note for powering-the-rack (cluster 7)

Google's in-house CDUs (Project Deschutes, "redundant" pump and heat exchanger, about 99.999% availability since 2020, design contributed to the Open Compute Project; Google Cloud blog, 30 Apr 2025) bear on the Vertiv claim every-megawatt-got-harder, whose falsifier includes "the biggest buyers take cooling in-house". The Vertiv note says it found no report of one doing so at scale; Google has, for its TPUs, since 2018. The powering-the-rack deep piece should say so in that claim's note, and the Vertiv note's risk line may need a "where I was wrong" at its next mark (Tommy's call; notes are never rewritten).

## Fact-check fixes applied (30 Oct 2026)

1. Google high-risk share now a series (15%, 14%, 13%) in the siting table and sidecar.
2. AWS 2024 0.15 recorded as primary; AWS limb dropped from the claim.
3. Google's high-risk air-cooling policy used (2025 report pp.40 to 41; Dec 2023 blog), with Mesa 9.7 against The Dalles 469, and Henderson's 239.4 stated openly.
4. Microsoft's 0.27 labelled "water withdrawn", year flagged as likely fiscal; calendar vs fiscal noted above the operator table.
5. Jane Street guides named as its write-up does (Ron Minsky, Dan Pontecorvo); the grid-interconnect words attributed to Dwarkesh Patel; tour dated 15 May 2026, the 21 May date belongs to the separate conversation.
6. New claim rewritten to a site-level test (Google's named high-risk campuses under 50 million gallons a year; no hyperscaler evaporative campus on a high-risk source; cancellation limb kept); claims.ts entry above matches the piece word for word.
7. water-is-a-siting-problem's claim treated as proposed and not on record; removed from Claims on record; text kept above for Tommy.
8. Exposure map cut to about 130 words (Asetek, Delta and LiteOn removed, chips folded into the operators line). Those three company pages lose this cluster's link at merge.
