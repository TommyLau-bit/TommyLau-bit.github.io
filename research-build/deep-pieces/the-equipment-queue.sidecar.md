# Sidecar: the-equipment-queue (deep piece, cluster 3 of 11)

Cluster 3, "The equipment queue: transformers and switchgear". Drafted 30 Oct 2026 to BRIEF-DEEP.md, matching the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/the-equipment-queue.md` (draft: true). Kept outside `src/content/journal/` so the loader does not read it. Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "The equipment queue: transformer and switchgear makers are building to keep the wait, not to end it" (17 words; names the cluster and the mechanism; the four companies are named in the summary, cold open and every section).
- Top layer (cold open, analogy, How it works, The number that matters): about 480 words, under 15 figures (checker passes), 0 money figures. Three company-derived figures only (Hitachi about three years, Siemens Energy about four, Eaton about a year). Analogy about 67 words.
- Investor layer (after fact-check fixes): about 2,410 words before the exposure map by the prototype's counting (2,476 for the prototype on the same counter); `check-piece.py` counts it under its 2,600 limit. Exposure map about 129 words. Whole body about 3,160 words.
- `brand/check-piece.py` on a scratch copy: 0 failures, 1 warning ("average sentence is 27 words"). The warning is an artefact: the checker does not split sentences inside the quoted claims and tables (the five Claims on record blocks count as 120 to 170 word "sentences"). Prose outside tables and claim blocks averages about 18 words.
- Layout needs the same `hr.layer` and `p.layer-label` CSS as the prototype.

## Frontmatter notes

- `date: 2026-10-07` is a placeholder only (the earliest absorbed live date, Schneider). At go-live it becomes the real publish time.
- New slug `the-equipment-queue` (none of the four absorbed slugs is the natural home; all four redirect to anchors).
- `cover: "/covers/hitachi-energy-plans-the-queue.svg"` is a placeholder until a new cover is drawn; proposal below.
- Tags: grid, power, data-centres (all existing).

## Thesis and how it treats the old claims

Thesis: the makers of transformers and switchgear are adding factories fast enough to keep their queues, not to clear them. Measured as backlog over the previous four quarters of the same business's revenue (years of work), the queue is about 3.1 years at Hitachi Energy (30 Sep 2026), about 4.0 at Siemens Energy Grid Technologies (30 Jun 2026) and 1.05 at Eaton Electrical Americas (30 Jun 2026). Schneider publishes no backlog figure ("record backlog" only), so its section carries the site labour and prefabrication strand instead.

The piece states the ratio's limits openly: not like for like (HVDC in the two grid makers), raised by price, early booking and currency as well as by a longer wait, and able to fall while the pile grows (Siemens Energy's own arithmetic, (4 + 0.1)/1.06 = 3.87).

Latest-results check (as at 30 Oct 2026):
- Hitachi: Q2 FY2026 results out 28 Oct 2026. Hitachi Energy backlog $66.9bn (+16% vs end FY2025; ¥10.5tn), Q2 revenue $5.60bn (+$0.83bn, +17%). Ratio about 3.1, up from 3.06. Claim holds. Noted in the claim block.
- Schneider: Q3 2026 revenues out 16 Oct 2026. Systems +22% organic, Products +17%, Systems 35% of Q3. Systems still faster, but the gap narrowed from 15 points to 5 and the nine-month Systems share is about 34% by my arithmetic, on the claim's line. Said openly in the claim block as "Where later evidence cuts against it".
- Eaton: Q3 2026 not out on 30 Oct (the research note gives 3 November; not confirmed at source). No figure moved.
- Siemens Energy: FY2026 results not out on 30 Oct (the research note gives 11 November; not confirmed at source). Q3 FY2026 (5 Aug 2026) is still the latest. No figure moved.

Notes under Claims on record:
- schneider-sells-the-finished-system: "Where later evidence cuts against it": not broken, but close (Q3 2026 Products 17%, "majority volume-driven", vs Systems 22%; nine-month share about 34%, 33.9% to 34.9% from rounded shares); the share test checks the outcome, not the labour cause.
- hitachi-energy-plans-the-queue: holds (about 3.1 at 30 Sep 2026); its South Boston "by 2028" was a trade press quote, not Hitachi.
- eaton-order-book-outruns-it: no new figures; rise slowed to 0.01; some may be price.
- siemens-energy-measures-the-shortage: no new figures; its Charlotte "slipped a year" rested on a press report (Reuters via IENE), and Siemens Energy's own last stated date is "early 2026"; its 3 February 2026 release gives none.

## Proposed claims.ts change (existing entries untouched)

The type already has `date` and `home`. At merge, the four existing entries gain only `home: 'the-equipment-queue'` (their `date` fields are already set: Schneider 2026-10-07T14:17:41+08:00, Hitachi 2026-10-22T12:51:38+08:00, Eaton 2026-10-26T08:03:14+08:00, Siemens Energy 2026-10-28T11:50:30+08:00). `claim`, `breaksIf` and `watch` are not touched. This is metadata, but it changes existing entries, so Tommy should approve it explicitly.

New entry (revised 30 Oct 2026 after fact-check point 4):

```ts
  {
    id: 'the-equipment-queue',
    claim: 'The first wave of new transformer and switchgear plants will not shorten the equipment queue in years of work: at 30 June 2028, Siemens Energy Grid Technologies\' order backlog will still be at least 3.6 times its revenue over the previous four quarters (3.96 at 30 June 2026), and Eaton Electrical Americas\' backlog at least 1.0 times its sales over the previous four quarters (1.05), even though Siemens Energy\'s own chart allows its ratio to fall while the pile grows.',
    breaksIf: 'At 30 June 2028, as each company reports it, Siemens Energy Grid Technologies\' order backlog in euros divided by its revenue over the previous four quarters is below 3.6, or Eaton Electrical Americas\' backlog divided by its sales over the previous four quarters is below 1.0.',
    watch: ['Siemens Energy Grid Technologies backlog over trailing four quarters of revenue, each quarter (3.96 at 30 June 2026; backlog rounded to €1bn)', 'Eaton Electrical Americas backlog over trailing four quarters of sales, each quarter (1.05 at 30 June 2026)', 'Whether Eaton\'s Jonesville and Bellevue plants start in 2027 and Siemens Energy\'s Nuremberg expansion opens by 2028', 'Dates for Siemens Energy\'s Charlotte expansion and Greater Richland switchgear plant (none in its 3 February 2026 release)', 'Whether Siemens Energy updates its transformer demand and capacity chart', 'Hitachi Energy\'s ratio (about 3.1 at 30 September 2026), tested by its own claim'],
  },
```

What is new, made explicit in the piece: (1) the Siemens Energy limb tests years of work, which its October claim does not (that claim tests the absolute pile in euros) and which its own chart lets fall; (2) the Eaton limb runs a year past its 2027 plants, to mid 2028, at 1.0 rather than its old 0.93 floor to end 2027; (3) Hitachi is left out because its own claim already tests its ratio (2.5 floor) to 2031, so a Hitachi limb would only tighten an existing test.

Thresholds: Siemens Energy 3.6 is about 91% of 3.957; Eaton 1.0 is about 95% of 1.049 and equals its December 2025 level. Test date 30 June 2028 is Siemens Energy's Q3 FY2028 (reported about August 2028) and Eaton's Q2 2028 (about late July 2028). Window: after Jonesville and Bellevue (2027) and as Nuremberg's new areas fall due (by 2028). Gallman (2029) and the undated South Boston, Charlotte expansion and Richland plants fall outside or are undated; the claim no longer says "after the plants have started".

Why it is a genuine test: at orders 10% above output and output growing 6% a year, Siemens Energy's 3.96 becomes (3.96 + 0.1) / 1.06 = 3.83 after one year and (3.83 + 0.1) / 1.06 = 3.71 after two, close to 3.6. Eaton's ratio rose only 0.01 in the latest quarter, and its new plants land inside the window. The "real risk" paragraph no longer uses Hitachi's 2030 plan, since that plan's $100bn includes framework agreements and capacity reservations and is not on the basis of reported backlog.

Alternatives considered: (A) the first draft's three-maker 90% test at 31 December 2027: dropped, because the Eaton and Hitachi limbs nearly restated their own falsifiers and the window missed most new plants. (B) absolute backlog growth: too easy to pass on price and FX, and already Siemens Energy's claim. (C) a lead time test: no maker publishes a transformer lead time.

## Redirect map

| Old URL | Redirect to |
|---|---|
| /journal/schneider-sells-the-finished-system/ | /journal/the-equipment-queue/#schneider-sells-the-finished-system |
| /journal/hitachi-energy-plans-the-queue/ | /journal/the-equipment-queue/#hitachi-energy-plans-the-queue |
| /journal/eaton-order-book-outruns-it/ | /journal/the-equipment-queue/#eaton-order-book-outruns-it |
| /journal/siemens-energy-measures-the-shortage/ | /journal/the-equipment-queue/#siemens-energy-measures-the-shortage |

All four are live, with LinkedIn posts in `brand/linkedin-posts.md` (lines about 351, 383, 397, 411); those resolve through the redirects. At merge the four originals go verbatim into `research-build/archive-pieces/`.

Sections and anchors, in order: How it works; The number that matters; (divider) The mechanism in depth (years-of-work table, factory table); Hitachi Energy (#hitachi-energy-plans-the-queue); Siemens Energy (#siemens-energy-measures-the-shortage); Eaton (#eaton-order-book-outruns-it); Schneider Electric (#schneider-sells-the-finished-system); Claims on record; What would prove me wrong; Research notes; exposure map; sources.

## stack.ts

Layer `grid` ("The grid connection"): the lead mechanism is the transformer queue at the grid connection. At merge:
- grid: replace `'hitachi-energy-plans-the-queue', 'siemens-energy-measures-the-shortage'` with `'the-equipment-queue'`.
- distribution: remove `'schneider-sells-the-finished-system', 'eaton-order-book-outruns-it'`. That leaves the-rack-runs-out-of-copper, every-megawatt-got-harder and ti-feeds-the-chip until cluster 7 merges. If Tommy wants the inside-the-fence gear visible on the distribution stop, the alternative is to list `the-equipment-queue` in distribution instead; a slug should sit in one layer only.

## Glossary (src/pages/glossary.astro)

Already present, no change: Transformer (the grid kind), Switchgear, Backlog, Book-to-bill, Organic growth, Lead time, HVDC, Bushing, GVA, Capacity reservation, Framework agreement, Supply capacity agreement, Basis point, Revenue mix, UPS, Prefabricated module, Commissioning, Inside the fence.

New, under "Getting power to the building" (finance-as-evidence terms sit there):
- Years of work: A company's order backlog divided by its revenue over the previous four quarters. It shows how long its factories would take to clear the orders already signed if no new order came in. A proxy for the wait, not a quoted delivery time: price rises and early bookings also lengthen it.

## numbers.ts (physical only)

Existing entry, repoint at merge (Tommy's decision): `~40% → ~10%` (Siemens Energy chart) has `piece: 'siemens-energy-measures-the-shortage'`; repoint to `the-equipment-queue` (the redirect also works).

New, physical:
```ts
  { layer: 'grid', value: '2 to 3 years', what: 'From announcement to planned first output at new transformer plants: Siemens Energy Charlotte (February 2024 for early 2026), Eaton Jonesville (February 2025 for 2027), Hitachi Energy Gallman (September 2026 for 2029).', piece: 'the-equipment-queue', asOf: '15 September 2026' },
```
The years-of-work ratios are financial (backlog over revenue), so they are left out of numbers.ts, consistent with "physical figures only". If Tommy accepts time-based proxies, the Hitachi and Eaton sidecars' `~3 years` and `~13 months` entries could be added, noting Eaton is 12.6 months.

## LinkedIn post (§9)

```
Hitachi Energy had $66.9 billion of orders waiting at the end of September, about three years of work, and it plans to keep it that way through 2030.

It is building or expanding more than 40 factories. So are Siemens Energy, Eaton and Schneider Electric, which make the transformers and switchgear an AI data centre cannot switch on without. Yet each reports a bigger pile of signed orders than a year ago, and Siemens Energy's own estimate has transformer demand in Europe and North America still ahead of every maker's capacity in 2030.

The piece puts the four makers side by side: years of work from each one's latest filing, every new plant with its date, and the claims I have on record.

https://thephysicallayer.fyi/journal/the-equipment-queue/

#Transformers #DataCentres #EnergyInfrastructure
```

## Cover proposal (not drawn)

`/covers/the-equipment-queue.svg`. One idea: a factory loading dock seen side on, with three doors of different widths (labelled small in letter-spaced grey: HITACHI ENERGY, SIEMENS ENERGY, EATON). In front of each, a queue of amber transformer silhouettes, the queue lengths roughly 3, 4 and 1 units deep; behind the doors, new bays drawn in thin outline marked 2027, 2028, 2029. A fourth door shows a finished blue box (Schneider's prefabricated room) rolling out whole. Caption: "THE EQUIPMENT QUEUE". Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Needed edits to other files (not made)

- `research-build/deep-pieces/the-queue-not-the-chip.md`: links `/journal/hitachi-energy-plans-the-queue/` and `/journal/siemens-energy-measures-the-shortage/` (Malaysia's queue section). Repoint to `/journal/the-equipment-queue/#hitachi-energy-plans-the-queue` and `#siemens-energy-measures-the-shortage`, or leave to the redirects. Its mechanism table cites "Hitachi Energy's unfilled orders equal about three years of sales (June 2026)", still true; optionally update to "about 3.1 years (September 2026)". Its sidecar's stack.ts proposal keeps hitachi and siemens slugs in grid; at merge those become `the-equipment-queue`.
- `research-build/deep-pieces/america-rations-the-plug.md` line 29 links `/journal/siemens-energy-measures-the-shortage/`; repoint to `/journal/the-equipment-queue/#siemens-energy-measures-the-shortage`.
- Live and scheduled pieces linking the absorbed slugs (ercot-rations-the-plug, ferc-asks-for-a-softer-plug, google-lets-the-grid-slow-its-chips, singapore-cannot-wait-for-the-cable) resolve through the redirects; no edit needed.
- `src/content/calls/eaton.md` and `src/content/calls/siemens-energy.md` give results dates (3 and 11 November) the piece does not repeat. No change proposed (notes are never rewritten).

## Sources, every one with date

Opened by me on 30 Oct 2026:
- Hitachi, Outline of Consolidated Financial Results for Q2 FY2026, 28 Oct 2026 (pp.4, 19, 24: Hitachi Energy backlog ¥10.5tn, $66.9bn, +16% vs end FY2025; Q2 revenue $5.60bn, +$0.83bn, +17%; FY2026 forecast $23.65bn; Q2 orders "driven by large HVDC project awards in Europe and data center orders"): https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/10/261028/2026_2Qpre.pdf
- Schneider Electric, Third Quarter Revenues 2026, 16 Oct 2026 (€11,460m, +16.9% organic; Products 48%, +17%; Systems 35%, +22%; Software and Services 17%, +7%; data centre demand "up triple-digit globally", sales "up strong double-digit", "notably in prefabricated solutions"; no backlog figure): https://www.webdisclosure.com/press-release/third-quarter-revenues-2026-odiihfxJLgs
- Schneider Electric, Half Year 2026 Results, 30 July 2026 ("record backlog"; no euro figure; mix and gross margin): https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2026/07/FCECO082813_20260730.pdf
- Schneider Electric US investment release, 25 Mar 2025 (over $700m through 2027; Mt. Juliet medium voltage; El Paso and Welcome switchgear; Columbia breakers; no production dates): https://www.se.com/us/en/about-us/newsroom/news/press-releases/Schneider-Electric-Plans-to-Invest-Over-700-million-in-the-U-S-Supporting-Energy-AI-Sectors-and-Job-Growth-67bdeb3ee4475a5955011b6a
- Siemens Energy release on Charlotte, 14 Feb 2024 ($150m; first transformers "expected to be manufactured in early 2026"): https://siemens-energy.com/global/en/home/press-releases/siemens_energy_addresses_shortage_US_powertransformers_invests_new_factory.html
- Hitachi Energy, South Boston groundbreaking, 29 Jun 2026 ($457m; no start date): https://www.hitachienergy.com/us/en/news-and-events/press-releases/2026/06/hitachi-energy-breaks-ground-on-the-nation-s-largest-facility-for-the-production-of-large-power-transformers-in-south-boston-virginia
- Hitachi Energy, Mississippi factory, 15 Sep 2026 ($528m, Gallman; "will more than double capacity"; production 2029): https://www.hitachienergy.com/us/en/news-and-events/press-releases/2026/09/hitachi-deepens-commitment-to-u-s-manufacturing-with-528-million-mississippi-transformer-factory
- Eaton 2Q 2026 earnings release (8-K Ex. 99), 31 Jul 2026 (EA sales $3.95bn, +18% organic; margin 27.5%; 12-month orders +41%; backlog +33%; no capacity or lead time statement): https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000027/etn06302026exhibit99.htm

From the cluster sidecars (primary, verified there, not re-opened today):
- Hitachi FY2025 results, 27 Apr 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/04/260427/2025_Anpre.pdf
- Hitachi Q1 FY2026 results, 29 Jul 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/07/260729/2026_1Qpre.pdf
- Hitachi Q3 FY2025 results, 29 Jan 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/articles/2026/01/260129/2025_3Qpre.pdf
- Hitachi Investor Day energy presentation, 10 Jun 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/06/260610/20260610_01_energy_en.pdf
- Hitachi Investor Day Q&A summary, 10 Jun 2026: https://www.hitachi.com/content/dam/hitachi/global/en/press/files/2026/06/260610/20260610_06_qa_session_en.pdf
- Hitachi Energy delivery times for transformer components (Ludvika updated 6 Oct 2026): https://www.hitachienergy.com/us/en/products-and-solutions/insulation-and-components/transformer-insulation-components/delivery-times-for-transformer-components
- Siemens Energy CMD Grid Technologies presentation, 20 Nov 2025: https://assets.siemens-energy.com/dam/d8d5d849-a7a9-4b19-a969-b39b004f6c26/251120_CMD-2025_Grid_Technologies_FINAL-pdf_Original%20file.pdf
- Siemens Energy Shareholder Letter Q4 FY2025, 14 Nov 2025: https://assets.siemens-energy.com/dam/9478ef65-c3f9-49de-97b0-b3aa00d5712d/2025-11-14--Shareholder-Letter-Q4-FY2025-EN_final-pdf_Original%20file.pdf
- Siemens Energy Shareholder Letter Q4 FY2024, 13 Nov 2024: https://assets.siemens-energy.com/dam/17e152fd-ddd4-4c4f-883f-b22e01021076/2024-11-13-Shareholder-Letter-Q4-FY2024-EN_final-pdf_Original%20file.pdf
- Siemens Energy earnings releases Q1, Q2, Q3 FY2026 (11 Feb, 12 May, 5 Aug 2026): https://assets.siemens-energy.com/dam/eb218e11-1294-4e27-a750-b3ee0059367f/Earnings-Release-Q1-FY26-EN-pdf_Original%20file.pdf ; https://assets.siemens-energy.com/dam/fb695b3d-e910-4f47-81b5-b4480034f6a1/Earnings-Release-Q2-FY26-EN-pdf_Original%20file.pdf ; https://assets.siemens-energy.com/dam/d0147174-31a9-4a78-b062-b49d00428fc4/earnings-release-q3-fy2026-en-pdf_Original%20file.pdf
- Siemens Energy Nuremberg release, 5 Sep 2025: https://www.siemens-energy.com/global/en/home/press-releases/siemens-energy-invests--220-million.html
- Eaton Forms 10-Q (30 Sep 2024, 30 Sep 2025, 31 Mar 2026, 30 Jun 2026) and 2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1551182/000155118224000041/etn-20240930.htm ; https://www.sec.gov/Archives/edgar/data/1551182/000155118225000036/etn-20250930.htm ; https://www.sec.gov/Archives/edgar/data/1551182/000155118226000013/etn-20260331.htm ; https://www.sec.gov/Archives/edgar/data/1551182/000155118226000030/etn-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1551182/000155118226000007/etn-20251231.htm
- Eaton plant releases (Business Wire): Jonesville 12 Feb 2025 https://www.businesswire.com/news/home/20250212663224/en/ ; Bellevue 8 Apr 2026 https://www.businesswire.com/news/home/20260408952863/en/ ; North Little Rock 2 Sep 2026 https://secure.businesswire.com/news/home/20260902691655/en/
- Schneider results: FY2024 (20 Feb 2025), H1 2025 (31 Jul 2025) https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2025/07/FCECO079331_20250731.pdf , Q3 2025 (30 Oct 2025), FY2025 (26 Feb 2026) https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf , Q1 2026 (30 Apr 2026) https://www.se.com/ww/en/assets/pdf/release-q1-revenues-2026
- Schneider Capital Markets Day transcript, 11 Dec 2025: https://www.se.com/ww/en/assets/pdf/capital-markets-day-transcript
- Schneider and Switch, 19 Nov 2025 (read via Switch's copy): https://www.switch.com/schneider-electric-and-switch-expand-partnership-with-1-9-billion-supply-capacity-agreement-to-power-ai-factories/

## Arithmetic

- Hitachi Energy trailing four quarters at 30 Sep 2026: Q3 FY25 5.3 + Q4 FY25 about 5.3 + Q1 FY26 5.40 + Q2 FY26 5.60 = about 21.6; 66.9 / 21.6 = 3.10 (3.09 using Q2 FY25 = 5.60 less 0.83 = 4.77 to derive Q4 FY25 = 5.32). 31 Mar 2026: 57.9 / 19.77 = 2.93. 31 Mar 2025: about 43.5 / 15.7 = 2.77. Plan FY2030: 100 / 36 = 2.78. FY2025 orders / revenue 32.8 / 19.8 = 1.66.
- Siemens Energy Grid: trailing at 30 Jun 2026 3.145 + 3.054 + 3.067 + 3.624 = 12.890; 51 / 12.89 = 3.96. Sep 2024 33 / 9.28 = 3.56; Sep 2025 42 / 11.305 = 3.72; Mar 2026 49 / 12.085 = 4.05. 9M FY26 orders / revenue 18.328 / 9.744 = 1.88. Products backlog €16bn / about €5.1bn products revenue = about 3.1 years (my estimate, from the CMD revenue shares).
- Eaton EA trailing sales: Jun 2025 12,229; Dec 2025 13,276; Jun 2026 14,467. Ratios 0.89 (Dec 2024, 10,141 / 11,436), 0.93, 1.00, 1.05 (15,175 / 14,467 = 1.049, 12.6 months). Sep 2025 0.95 and Mar 2026 1.04 cut from the table for length.
- Schneider nine-month Systems share: Q1 9,767 x 33% + Q2 11,459 x 35% + Q3 11,460 x 35% = about 11,245 of 32,686 = about 34.4%, from rounded shares, so "about 34%". Q1 revenue = H1 21,226 less Q2 11,459.
- Ratio can fall while pile grows: (4 + 0.1) / 1.06 = 3.87.

## Figures dropped or flagged

- Eaton CEO quotes "Scaling capacity to turn demand into revenue remains the clear priority" and "15 years of backlog at 2025 build rates": DROPPED. They come only from a third-party (Motley Fool) call transcript; the 8-K release has neither. The piece says so in the Eaton section.
- Hitachi Energy South Boston "operational by 2028": DROPPED as a date. Trade press (Manufacturing Dive) quoting a Hitachi manager; Hitachi's own releases (4 Sep 2025, 29 Jun 2026) give none. Flagged openly as a correction to the live piece.
- Siemens Energy Charlotte "early 2027": DROPPED. Reuters via IENE only. Siemens Energy's own last stated date (14 Feb 2024) is "early 2026"; I found no Siemens Energy confirmation of production or of a new date.
- Hitachi Energy data centre orders "more than doubled" (>150% FY2025, Investor Day): primary but cut for length.
- Siemens Energy "~20% of all power transformers" installed (CMD): cut for length; Hitachi's one in six used instead.
- Schneider: Foxconn prefab partnership (15 Jun 2026) and the Blum call quote: DROPPED (trade press and a third-party transcript). Foxconn therefore leaves the exposure map; its company page loses this link at merge.
- Schneider: Aamir Paul's electrician figures (conflict with BLS), the BLS 821,000 electricians, PTC deal and Motivair: not used.
- Schneider "Products growth predominantly driven by volumes" (search summary of the Q3 release): not confirmed in my fetch of the release; not used.
- Eaton Fibrebond caveat (in both June backlogs, one quarter of June 2025 trailing sales): cut for length; still valid.
- Eaton group capex about $1.15bn for 2026 (10-Q): kept.
- Exposure map: Foxconn dropped (above). GE Vernova, ABB, Siemens, Vertiv, Prysmian, Nexans and NKT retained from the four maps.

## Could not verify today

- Siemens Energy FY2026 and Eaton Q3 2026 results dates (the research notes say 11 and 3 November); the piece only says neither was out on 30 Oct 2026.
- Eaton plant details (Bellevue over $30m and first half 2027; North Little Rock $242m and doubling Fibrebond capacity): Eaton's own Business Wire releases, read through trade press quoting them because Business Wire blocks fetching. Jonesville confirmed via the release text reproduced on silicon.co.uk.
- Hitachi Q2 FY2026 Hitachi Energy orders in US dollars: not given in the deck pages I read (Power Grids orders are in yen); the table uses fiscal 2025 orders against revenue.
- The Hitachi Q&A quotes are Hitachi's published, translated summary, not a verbatim transcript; the piece says so.
- Schneider's Q4 2025 Systems share of the quarter was not in my notes; the table says "not given".

## Fact-check fixes applied (30 Oct 2026)

1. Siemens Energy's own release of 3 February 2026 (New York; https://assets.siemens-energy.com/dam/1c3629cd-ed4e-4790-a9d2-b3e60098637b/Press-Release-investments-USA-pdf_Original%20file.pdf) found and read: $1bn US programme; "increasing manufacturing and servicing capabilities for large power transformers" at Charlotte; "a new high-voltage switchgear facility" in the Greater Richland area, Mississippi, hiring up to 300. It gives NO site amounts and NO dates. Added to the factory table (one row, "Not stated"). The about US$421m for North Carolina and Richland "by 2028" are trade press only (e.g. Plant Services, MSBA, 3 to 5 Feb 2026); not used. The Charlotte correction stands and now says no Siemens Energy release, including that of 3 February 2026, gives a new date.
2. Hitachi ">$9bn" now shown as over $3bn (2020 to 2023) plus over $6bn (2024 to 2027). Siemens Energy "over €2bn" (shareholder letter, 14 November 2025). Hitachi March 2026 ratio 2.93 (57.9 / 19.77).
3. Schneider: Q3 2026 release says Products growth was "majority volume-driven" (confirmed in the release, 16 October 2026); added to the section and the claim note as cutting further against the claim. Nine-month Systems share stated as about 34% from rounded shares (33.9% to 34.9%).
4. New claim re-dated to 30 June 2028, factory clause dropped, Hitachi limb dropped, what is new made explicit; "real risk" paragraph rewritten without Hitachi's plan; "little new floor space before 2027" replaced with Siemens Energy's 20% added in fiscal 2023 to 2025 and most announced floor space due from 2027 on. claims.ts entry above matches the piece word for word.
5. Cuts: Hitachi bushings paragraph, Schneider Q2 and Q3 2025 table rows, the €16bn products backlog sentence, the Switch sentence, the 3.9 example in the mechanism section (kept in the falsifier), Hitachi Q2 revenue sentence, Eaton capex sentence. Sources line updated (delivery times page, Switch release and Schneider 2025 H1 and Q3 releases removed; Siemens Energy 3 February 2026 added). The 140-week bushing numbers.ts entry was removed from this sidecar with the paragraph.
6. Rerun of check-piece.py on a scratch copy: 0 failures, 1 warning (sentence average, the claim-block artefact above). Top layer about 481 words; investor layer about 2,410 words on the prototype's counter, under the checker's 2,600 limit.

## Flags for Tommy (not edited; published notes are never rewritten)

- `src/content/calls/hitachi.md` line 162: "Hitachi expects the South Boston, Virginia transformer plant to operate by 2028". Hitachi's own releases give no South Boston date; the date is a trade press quote.
- `src/content/calls/siemens-energy.md` line 159: "The Charlotte transformer plant slipped by a year to 2027". Rests on Reuters via IENE; Siemens Energy's last stated date is early 2026 and its 3 February 2026 release gives none.
- `src/data/claims.ts` watch lists: hitachi-energy-plans-the-queue says "South Boston, Virginia (2028)"; siemens-energy-measures-the-shortage says "Whether the Charlotte large power transformer plant ships in 2027". Watch items are fixed with the claim, so they stay; the deep piece's correction stands openly in its Claims on record notes.
