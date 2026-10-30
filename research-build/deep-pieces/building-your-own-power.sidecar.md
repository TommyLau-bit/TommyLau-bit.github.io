# Sidecar: building-your-own-power (deep piece, cluster 4 of 11)

Cluster 4, "Building your own power: turbines, blades and gas". Drafted 30 Oct 2026 to BRIEF-DEEP.md, matching the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/building-your-own-power.md` (draft: true). Kept outside `src/content/journal/` so the loader does not read it. Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "Building your own power: GE Vernova's queue, not the grid's, sets the date" (12 words, sentence case, names the subject that runs through every section).
- New slug `building-your-own-power` (per the brief). All three live slugs redirect into it.
- Top layer (cold open, analogy, How it works, The number that matters): about 497 words, 10 figures, 0 money figures. Analogy about 65 words. Average sentence about 18 words across the body.
- Investor layer: about 2,500 words before the exposure map (my counter, tables and quoted claims included; at the 2,500 ceiling, so do not add without cutting). Exposure map about 128 words including the fixed disclaimer pair. Whole body about 3,400 words.
- `brand/check-piece.py` on a scratch copy: 0 failures, 1 warning (sources line 251 words; the prototype's is longer).
- `date: 2026-09-22` is a placeholder (the earliest absorbed claim's date); it becomes the real publish time at go-live. The three live claims keep their own dates through `date` in claims.ts (already present).
- `cover:` points at the existing `/covers/ge-vernova-sells-the-wait.svg` until a new cover is drawn (proposal below).
- Tags: power, data-centres, grid (all existing).

## Thesis and how it treats the old pieces

Thesis: building your own power does not skip the queue; it changes which queue you stand in. Four clocks replace the grid's: the machine (heavy-duty slots, the aeroderivative lane, Bloom's factory), the castings inside it, the air permit, and the fuel. GE Vernova is the subject throughout (title, cold open, number, two sections, new claim).

How each absorbed piece is used:
- ge-vernova-sells-the-wait (live): updated to the 28 Oct 2026 Q3 release and call. Queue table Q4 2025 to Q3 2026 (83, 100, 116, 122 GW; firm/SRA split; signed; shipped; years of 20 GW). Output steps 20 / 24 / 30 GW from the 22 Jul call, confirmed unchanged in substance on 28 Oct (the Q3 release and call do not restate 24 and 30; they confirm the 5 GW a quarter, 20 GW a year, pace). Correction: the $27.7bn is the Power segment, which also holds nuclear and hydro (first made in the GE Vernova note).
- the-way-out-has-its-own-queue (live): its order-book figures came from POWER Magazine, a trade report; replaced by GE Vernova primary figures. Siemens Energy's 95 GW dropped (press only; the 69 GW firm figure for Q3 FY26 is also press only).
- the-product-is-time (live): "Where I was wrong" carried from the Bloom note (margin rose by mix; Oracle "intends", 1.2 GW contracted). Updated with the Q3 2026 release (22 Oct 2026): product margin 37.9% vs 35.0% a year earlier, my computation; stated as one quarter, not a trend.
- homer-city-inherits-the-air (scheduled draft): netting mechanism kept as "the permit is a clock too", all DEP figures as verified in its sidecar. Its proposed claim is not carried (it never went live).
- hyperion-the-plant-outlasts-the-lease (scheduled draft): reframed as the utility-built route. The "15-year" power agreement term is DROPPED (press only; term redacted in the public settlement). "The commission declined to act" in Feb 2026 is DROPPED (Louisiana Illuminator and Earthjustice only, not in an Entergy filing). Added from its verified-but-unused list: second Meta agreement, seven CCGTs, 5,278 MW, 2030 and 2031 (Entergy 10-Q Q2 2026).
- permian-gas-follows-the-oil-rig (scheduled draft): kept under the oil exception, physical system only. Matterhorn's FID date dropped (press-confirmed only). The Waha below-zero fact (EIA) is kept as evidence of a pipe limit, with no price view; Tommy may prefer to cut it as the one price-adjacent sentence.
- howmet-casts-the-queue (held): respected the hold. No 2028 to 2030 capacity dates and no "more than half" share (press transcript only). Used only primary: Howmet's "largest manufacturer" deck line, gas turbine revenue +38% Q2 and +45% Q3 2026, GE Vernova's "castings and forgings arriving in '27" and "significant supply chain capacity" for 30 GW. The piece says openly that the foundry is not one company's gate (captive furnaces per Howmet 10-K; Siemens Energy Florida blade and vane capacity, 11 Feb 2026) and that I hold no claim that one caster sets the 30 GW date.
- crusoe-borrows-the-jet-engine (held): respected the hold. The engine-source mechanism is stated as NOT shown by the filings ("The filings do not show that this engine source is what makes the machine faster"). Kept: the order, units and assembly facts, the 24 / 6 / 18 month timings, the units table, and "expected" (not confirmed) operation. GE Aerospace's $407m of engine and parts sales dropped in the trim (it covers all engine sales, not provably aeroderivative).
- golden-pass-joins-the-gas-queue (held): respected the hold. "Export signed first" is stated as NOT held: Trident was developed with Golden Pass and Entergy Texas signed for space for its power plants within days of launch (Entergy Texas, 31 Jan 2025). Kept only EIA facts (first cargo, ~2 Bcf/d nominal, July ~a tenth, Feb to Apr 2026 Texas LNG exports above Texas power burn) and Kinder Morgan's Permian Link for a hyperscaler's generation (Q3 2030). No 2027 crossover claim.

## Proposed claims.ts change (existing entries' text untouched)

At merge, the three live entries gain only `home: 'building-your-own-power'` (they already carry `date`: 2026-09-22T18:56:00+08:00, 2026-09-24T13:43:00+08:00, 2026-10-09T11:22:31+08:00). `claim`, `breaksIf` and `watch` unchanged. The research notes keep pointing at `ge-vernova-sells-the-wait` and `the-product-is-time`.

New entry (matches the piece word for word):

```ts
  {
    id: 'building-your-own-power',
    claim: 'Building your own gas power swaps the grid\'s queue for the makers\' queues, and the fast lane is queued too: GE Vernova\'s gas turbine gigawatts under contract at 31 December 2027 will be no lower than at 31 December 2026, and at 31 December 2027 its aeroderivative backlog, units ordered less units shipped since 1 January 2025, will still exceed its aeroderivative units shipped in the previous twelve months.',
    breaksIf: 'GE Vernova reports fewer gigawatts of gas turbines under contract, firm orders and slot reservations together, at 31 December 2027 than at 31 December 2026, or at 31 December 2027 its aeroderivative units ordered less units shipped since 1 January 2025 are equal to or fewer than its aeroderivative units shipped in calendar 2027.',
    watch: ['GE Vernova gigawatts under contract each quarter (122 GW at 30 September 2026; at least 130 GW expected at 31 December 2026)', 'GE Vernova aeroderivative units ordered and shipped, each 10-Q and 10-K (cumulative backlog since 1 January 2025: 124 units at 30 September 2026, about 2.3 years of trailing twelve-month shipments)', 'Power segment contract liabilities and current deferred income (US$33.2bn at 30 September 2026)', 'Earliest delivery year of heavy-duty slots sold (2032, October 2026), the 24 GW step in 2028, and any new heavy-duty factory', 'Howmet and Siemens Energy casting capacity dates', 'Permian rig count and Texas LNG exports against Texas power burn (EIA)'],
  },
```

Revised 30 Oct 2026 after the fact-check: the 120 GW floor (below GE Vernova's own expectation of growth) is replaced by "no lower at end 2027 than at end 2026"; the orders-versus-shipments limb is replaced by an aeroderivative backlog measured in years (cumulative orders less shipments since 1 January 2025, 124 units now, about 2.3 years of trailing shipments), which breaks if it falls to one year or less. Either breach would not by itself say why (faded demand, lapses, faster output), and the falsifier section says so.

Alternatives considered: (A) a head-to-head test, on-site energisation against grid connection dates for comparable sites: not observable from primary sources. (B) Howmet sets the 30 GW date: held, primary dates missing and other casters adding capacity. (C) Texas LNG overtakes Texas power burn in 2027 (Golden Pass's claim): its mechanism was contradicted; the crossover alone is a gas balance forecast.

## Redirect map

| Old URL | Redirect to |
|---|---|
| /journal/ge-vernova-sells-the-wait/ | /journal/building-your-own-power/#ge-vernova-sells-the-wait |
| /journal/the-way-out-has-its-own-queue/ | /journal/building-your-own-power/#the-way-out-has-its-own-queue |
| /journal/the-product-is-time/ | /journal/building-your-own-power/#the-product-is-time |
| /journal/homer-city-inherits-the-air/ | /journal/building-your-own-power/#homer-city-inherits-the-air (scheduled, not yet live; only if it goes live first) |
| /journal/hyperion-the-plant-outlasts-the-lease/ | /journal/building-your-own-power/#hyperion-the-plant-outlasts-the-lease (as above) |
| /journal/permian-gas-follows-the-oil-rig/ | /journal/building-your-own-power/#permian-gas-follows-the-oil-rig (as above) |

Held drafts (howmet-casts-the-queue, crusoe-borrows-the-jet-engine, golden-pass-joins-the-gas-queue) were never live; anchors exist anyway. LinkedIn posts in `brand/linkedin-posts.md` (lines ~135, 183, 365) link the three live URLs and resolve through the redirects. At merge, the three live originals go verbatim to `research-build/archive/pieces/` (folder does not exist yet) and the six draft files leave `src/content/journal/`.

Sections and anchors, in order: The mechanism in depth; GE Vernova: the queue is the product (#ge-vernova-sells-the-wait); The fast lane: aeroderivatives and Crusoe (#the-way-out-has-its-own-queue, #crusoe-borrows-the-jet-engine); Under the turbine: the blades (#howmet-casts-the-queue); Bloom Energy: paying for an earlier date (#the-product-is-time); Homer City: the permit is a clock too (#homer-city-inherits-the-air); Hyperion: when the utility builds the plant (#hyperion-the-plant-outlasts-the-lease); The fuel: Permian gas and the pipes to the coast (#permian-gas-follows-the-oil-rig, #golden-pass-joins-the-gas-queue); Claims on record; What would prove me wrong; Research notes.

## Scheduled tasks affected (not touched)

homer-city-inherits-the-air is scheduled to go live Fri 4 Dec (LinkedIn Wed 6 Jan) per UNCAPPED-RESULTS.md; hyperion and permian also have publish tasks in the queue. All become sections of this piece and should be paused with Tommy's go, per the consolidation plan.

## stack.ts

Layer `onsite` ("Power on site"). At merge the list becomes:
`pieces: ['building-your-own-power', 'what-the-battery-is-really-for', 'constellation-restarts-the-reactor', 'oklo-sells-the-electricity']`
(the battery and nuclear entries move when clusters 5 and 6 merge). The Permian and Golden Pass sidecars proposed a new `fuel` layer plus a hand-drawn Descent stop; not needed now, since the fuel is a section of this piece. If cluster 5 (nuclear fuel, Eunice, TerraPower) wants a fuel layer, add it then.

## Glossary (src/pages/glossary.astro), "Getting power to the building"

Already present, no change: Behind the meter, Slot reservation agreement, Solid oxide fuel cell, NOx, Heavy-duty gas turbine, Aeroderivative, Castings and forgings, Contract liabilities, Take-or-pay agreement.

New:
- Gigawatts under contract: GE Vernova's count of gas turbine capacity held by firm orders and slot reservations together. Set against its yearly output, it measures the queue in years.
- Netting: counting a recent emissions cut at the same site against a new plant's increase, so the project avoids the full review for that pollutant.
- Emission reduction credit: a certified, permanent cut in pollution elsewhere that a new plant buys to offset its own emissions.
- Combined cycle gas plant: a power station that burns gas in a turbine, then uses the waste heat to raise steam for a second turbine.
- Electric service agreement: the contract between a utility and a large customer to supply and pay for power, often with minimum monthly charges and a fee for leaving early.
- Investment casting: making a metal part by pouring molten metal into a ceramic shell formed around a wax copy. How turbine blades are made.
- Superalloy: a nickel-based metal that keeps its strength close to its melting point; the material of the hottest turbine blades.
- Associated gas: natural gas that flows out of an oil well with the crude, so its supply follows oil drilling. Most Permian gas.
- Rig count: the number of drilling rigs at work, counted weekly by Baker Hughes.
- Bcf a day: billion cubic feet of gas a day.
- LNG (liquefied natural gas): gas chilled until liquid so a ship can carry it.
- Liquefaction train: one production line in an LNG export plant.

## numbers.ts (physical only)

Update with a `note` (Tommy to approve): the existing `~6 years` entry (piece ge-vernova-sells-the-wait, asOf 30 June 2026) to:
```ts
  { layer: 'onsite', value: '~6 years', what: 'Gas turbine capacity GE Vernova has under contract, 122 gigawatts, against its output of 20 gigawatts a year. It is now selling places for delivery in 2032.', piece: 'building-your-own-power', asOf: '30 September 2026', note: 'Was 116 GW at 30 June 2026.' },
```
Repoint `piece` to building-your-own-power on: `116 GW` (the-way-out-has-its-own-queue; suggest retiring it in favour of the entry above), `54 to 60%` entry (the-product-is-time; a "typical published" range, not primary; flag for Tommy, or keep with the redirect). Note that the existing entry writes that range with an en dash, which the house style bans.

New:
```ts
  { layer: 'onsite', value: '127 vs 39', what: 'Aeroderivative gas turbines GE Vernova took orders for, against those it shipped, in the first nine months of 2026. The fast route to on-site power has its own queue.', piece: 'building-your-own-power', asOf: '30 September 2026' },
  { layer: 'onsite', value: '4,678 MW', what: 'Maximum capacity Pennsylvania permitted for the gas plant on the former Homer City coal site, cleared of NOx review by netting against the old boilers\' cuts.', piece: 'building-your-own-power', asOf: '18 November 2025' },
  { layer: 'onsite', value: '302 → 242', what: 'Rigs drilling in the Permian Basin in early 2025 and early 2026. Gas output rose by about a twelfth over the same year, because the gas comes up oil wells.', piece: 'building-your-own-power', asOf: 'Q1 2026' },
```

## LinkedIn post (§9)

```
GE Vernova has 122 gigawatts of gas turbines under contract and ships about 20 a year.

AI campuses tired of waiting for the grid are building their own gas power, and they are queuing beside utilities for the same machines, with places now sold for 2032. Even the fast lane is full: GE Vernova took orders for 127 jet-engine turbines in nine months and shipped 39.

The piece covers the four clocks that replace the grid's, from turbine slots to blades, air permits and gas pipes, and the claims I have on record.

https://thephysicallayer.fyi/journal/building-your-own-power/

#GasTurbines #DataCentres #EnergyInfrastructure
```

## Cover proposal (not drawn)

`/covers/building-your-own-power.svg`. One idea: a data centre block on the right, its grid cable cut short at a small amber barrier; on the left, a single large amber gas turbine with a long row of small queued turbine silhouettes behind it running off the frame, and a thin amber pipe entering from the top edge. Caption in letter-spaced grey: "BUILDING YOUR OWN POWER: THE TURBINE QUEUE". Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Sources, with dates

Opened or re-read by me on 30 Oct 2026:
- GE Vernova 3Q 2026 results release, 28 Oct 2026 (122 GW, 64 backlog and 58 SRA; signed 11 GW, 8 SRA and 3 orders; converted 13; shipped 5; at least 130 GW by year end; 55 heavy-duty incl. 21 HA and 57 aeroderivative units ordered; Electrification equipment backlog $42.2bn, +60%, incl. $5bn Prolec GE): https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm
- GE Vernova 3Q 2026 call transcript, 28 Oct 2026 (5 GW quarter run rate; 52 GW signed year to date; slots for 2032; ~100 customers, ~20% data centres; 3Q orders priced >20% above 4Q25 with more aero mix; FY26 per kW ~50% above FY25; 4Q per kW lower on mix; 32 turbines shipped incl. 13 aero; aero "going out so far in the future before we have availability", 4Q aero lighter; working capital benefit "driven primarily by down payments" at Power and Electrification; GW under contract to keep growing in 2027; Trench acquisition): https://www.gevernova.com/sites/default/files/gev_webcast_transcript_10282026.pdf
- GE Vernova Form 10-Q, Q3 2026, filed 28 Oct 2026 (Note 9, per the coordinator's fact-check: Power contract liabilities and current deferred income US$33,163m at 30 Sep 2026, from US$16,527m at 31 Dec 2025; the consolidated US$45,669m includes Prolec GE and is not used). Aero units 127/39 per the Crusoe sidecar's reading, consistent with the release (57 ordered in Q3) and call (13 shipped in Q3): https://www.sec.gov/Archives/edgar/data/1996810/000199681026000163/gev-20260930.htm
- Bloom Energy Q3 2026 results, 8-K Ex. 99.1, 22 Oct 2026 (revenue $1,235,837k vs $519,048k; product revenue $1,073,610k vs $384,314k; product cost $666,978k vs $249,794k; product margin 37.9% vs 35.0%, my computation): https://www.sec.gov/Archives/edgar/data/0001664703/000162828026066890/ex991_q326financialresults.htm
- Bloom Energy and Oracle, 24 Jul 2025 ("within 90 days"): https://www.bloomenergy.com/news/oracle-and-bloom-energy-collaborate-to-deliver-power-to-data-centers-at-the-speed-of-ai/

From the absorbed sidecars and notes (primary, verified there, not re-opened today):
- GE Vernova 2Q 2026 release, 22 Jul 2026: https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm
- GE Vernova 2Q 2026 call transcript, 22 Jul 2026 (20 / 24 / 30 GW; "lean and incremental machinery in our existing factory footprint ... all funded by customer down payments"; castings and forgings in '27; 18 months on site, aero about six, ships 24 months sooner; sold out through 2030): https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf
- GE Vernova Form 10-Q, Q2 2026, 22 Jul 2026 (Power contract liabilities $16,527m to $27,679m; cash rise "primarily due to higher down payments"): https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev-20260630.htm
- GE Vernova 1Q 2026 release, 22 Apr 2026: https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm
- GE Vernova 2025 Form 10-K, 29 Jan 2026 (aero units 63/27 in 2025; GE Aerospace and Aero Alliance supply): https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/gev-20251231.htm
- Q4 2025 queue split 40 / 43 GW: GE Vernova Q4 2025 release, 28 Jan 2026, as charted in the GE Vernova note.
- GE Vernova and Crusoe, 22 Jul 2025: https://www.gevernova.com/news/press-releases/ge-vernova-crusoe-announce-major-29-unit-aeroderivative-gas-turbine-deliver-ai-data-centers ; case study: https://www.gevernova.com/gas-power/resources/case-studies/crusoe-ai-data-centers-lm2500xpress
- Howmet Technology and Markets Day, 10 Mar 2026: https://www.howmet.com/wp-content/uploads/sites/3/2026/03/Howmet-Aerospace-Technology-and-Markets-Day-2026.pdf ; Q2 release, 6 Aug 2026: https://www.sec.gov/Archives/edgar/data/0000004281/000110465926091610/tm2622325d1_ex99-1.htm ; Q3 release, 29 Oct 2026: https://www.sec.gov/Archives/edgar/data/4281/000110465926119857/tm2628456d1_ex99-1.htm ; 2025 10-K, 12 Feb 2026: https://www.sec.gov/Archives/edgar/data/4281/000000428126000012/hwm-20251231.htm
- Siemens Energy Q1 FY26 analyst presentation, 11 Feb 2026, p.7 (Florida blade and vane capacity), as cited in the Howmet sidecar (URL not recorded there).
- Bloom: Oracle 13 Apr 2026, AEP Nov 2024, 2025 10-K (Fremont 1 to 2 GW), product margins 2024 to H1 2026: as sourced in the Bloom Energy note.
- Pennsylvania DEP, plan approval 32-00457A, technical review memo and comment response, 18 Nov 2025: https://files.dep.state.pa.us/RegionalResources/NWRO/NWROPortalFiles/Homer-City/Air/Final-AQ-Plan-Approval/ ; 25 Pa. Code 127.203a and 127.210; EHB dockets 2025-135-L and 2025-136-L; Clean Air Council notice of appeal, 17 Dec 2025; Homer City releases 26 Mar and 20 Oct 2026; AWS narrative 27 Aug 2026 (all URLs in the homer-city sidecar).
- Entergy 2025 10-K, 19 Feb 2026: https://www.sec.gov/Archives/edgar/data/65984/000006598426000174/etr-20251231.htm ; Entergy 10-Q Q2 2026, 31 Jul 2026: https://www.sec.gov/Archives/edgar/data/65984/000006598426000283/etr-20260630.htm ; Meta 2025 10-K, 29 Jan 2026: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm ; Meta release 21 Oct 2025; LPSC U-37425 term sheet, 7 Aug 2025.
- EIA STEO October 2026 (Tables 5a, 10a): https://www.eia.gov/outlooks/steo/archives/oct26.pdf ; September 2026: https://www.eia.gov/outlooks/steo/archives/sep26.pdf ; Today in Energy 3 Feb 2025: https://www.eia.gov/todayinenergy/detail.php?id=64445 ; 23 Apr 2026: https://www.eia.gov/todayinenergy/detail.php?id=67564 ; monthly LNG exports by point and Texas power deliveries (N3045TX2), 30 Sep 2026: https://www.eia.gov/dnav/ng/hist/n3045tx2m.htm and https://www.eia.gov/dnav/ng/hist/ngm_epg0_eng_ygpt-z00_mmcfm.htm
- Railroad Commission of Texas, Statewide Rule 32 handout: https://www.rrc.texas.gov/media/wftn5jh5/statewide-rule-32-flaring-handout.pdf
- Kinder Morgan Q1 2026 release, 22 Apr 2026: https://www.sec.gov/Archives/edgar/data/1506307/000150630726000033/kmi2026q18-kex991.htm ; Q3 2026, 21 Oct 2026: https://www.sec.gov/Archives/edgar/data/1506307/000150630726000130/kmi2026q38-kex991.htm ; Entergy Texas, 31 Jan 2025: https://www.entergy.com/news/entergy-texas-partners-with-kinder-morgan-golden-pass-lng-to-fuel-southeast-texas-growth
- Leads only (credited once in the sources line): Leo Cui, "GE Vernova Explained: The Power Bottleneck Behind the AI Boom", https://www.youtube.com/watch?v=TiHQJVK9Kk4 ; Leo Cui, "The Entire Energy Sector Explained", https://www.youtube.com/watch?v=0zZyEF4Cq9U ; "State of AI data centres 2026" (data to 5 Oct 2026). Upload dates not recorded in the transcripts, so the sources line gives none.

## Figures dropped or flagged

- Siemens Energy 95 GW (live piece, POWER Magazine) and 69 GW firm (Q3 FY26, press summaries): dropped, not primary.
- "Grid can take five years", Bloom "54 to 60 per cent" efficiency, "35 to 40 per cent" turbine: dropped from the body (the live piece calls them typical published figures).
- Hyperion "15-year" agreement and the Feb 2026 "declined to act": dropped, press only.
- Howmet "more than half" share and 2028 to 2030 capacity dates: dropped, press transcript only.
- Crusoe: engine-source causation stated as unshown; operation "expected", not confirmed; GE Aerospace $407m dropped in the trim.
- Golden Pass: "export signed first" stated as not held; Golden Pass's 1 Bcf/d on Trident (press) not used; no crossover forecast.
- Matterhorn FID date (press-confirmed): dropped. Waha below zero on 42% of 2024 days (EIA): kept as pipe evidence; Tommy may cut it.
- Oil exception: no oil or gas price forecast, breakeven or trading view anywhere.
- Company-wide contract liabilities (US$45.7bn, includes Prolec GE): dropped. Power segment US$33.2bn at 30 Sep 2026 used, labelled as including nuclear and hydro, and added to the GE Vernova claim note.

## Fact-check fixes applied (30 Oct 2026)

1. Power deposits US$33.2bn at 30 Sep 2026 (Note 9); company-wide US$45.7bn dropped; added to the GE Vernova claim note.
2. "First quarter at 5 GW" corrected to the CEO's "the first quarter of our 5GW" (better-priced shipments); 20 GW run rate reached by 22 Jul; nine-month shipments 12.8 GW; top layer says "a pace of about 20 a year".
3. Data centres: "about 20% of its roughly 100 gas customers", not a fifth of demand.
4. Aero availability quote attributed to GE Vernova's availability, with "not because the demand is softer".
5. Output plan "not restated" on 28 Oct.
6. The way-out note: limb two (own generation against grid connections) untested only; the aero vs heavy-duty comparison removed from it.
7. 50% price rise stated as a full-year expectation, mix cited for Q3 only; blades "lengthways or form a single crystal"; GE note uses "Where later evidence stands: holding"; Waha sentence framed as a historical pipe limit with EIA's cause, the "physical system only" line replaced; Crusoe primary-power clause added.
8. New claim and falsifier replaced (above); claims.ts entry matches.
9. Claims on record notes trimmed (block now about 580 words, mostly the fixed quotes); exposure map merged to two groups, about 128 words with the disclaimer (Precision Castparts, ExxonMobil, Occidental no longer in this map; their company pages lose this link).

check-piece.py on a scratch copy after fixes: 0 failures, 1 warning (sources line length). Investor layer trimmed to fit the checker's 2,600 limit (Fremont sentence, Entergy customers line, Trident wording, Homer City window wording shortened).

## Could not verify today

- The 20 / 24 / 30 GW steps are from the 22 Jul call; neither the 28 Oct release nor the call restates 24 and 30, so the piece says "given on 22 July and not changed on 28 October".
- SEC EDGAR refused curl with the brief's User-Agent (it asks for contact details, which I did not add); I read EDGAR pages through the fetch tool instead, which truncated the Q3 10-Q.

## Edits other drafts need (not made)

- hyperion, permian and golden-pass drafts link `/journal/ge-vernova-sells-the-wait/`, `/journal/the-way-out-has-its-own-queue/` and `/journal/permian-gas-follows-the-oil-rig/`; they leave `src/content/journal/` at merge, so nothing to fix. No other journal piece links the absorbed slugs.
- The GE Vernova note and Bloom note keep their `claims` ids; their "the October piece" / "my September piece" wording still reads correctly through the redirects.
