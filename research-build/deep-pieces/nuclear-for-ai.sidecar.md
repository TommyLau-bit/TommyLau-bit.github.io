# Sidecar: nuclear-for-ai (deep piece 5 of 11)

Cluster 5, "Nuclear for AI: restarts first, new reactors later". Drafted 30 Oct 2026 to BRIEF-DEEP.md, matching the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/nuclear-for-ai.md` (draft: true). Kept outside `src/content/journal/`. Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "Nuclear power for AI comes from old reactors first. The new ones wait on fuel." (14 words, two sentences, sentence case.) Category Analysis.
- Top layer (cold open, analogy, How it works, The number that matters): 443 words, 13 figures (5, 20, 5, 2028, sixteen, mid-June 2026, one tonne, July 2032, 835 MW, 2027, "a quarter", "eleven", "two"), 0 company financial figures. Analogy 75 words.
- Investor layer: about 2,500 words before the exposure map by raw token count, which counts table pipes and cells; prose alone is well under. Exposure map 134 words. Whole body about 3,280.
- `brand/check-piece.py` (now §D-aware) on the file: 0 failures, 1 warning (average sentence 24 words, inflated by the two tables; the prototype has the same).
- Sections and anchors, in order: The mechanism in depth (ladder table); Crane (#constellation-restarts-the-reactor); Palisades (#palisades-waits-on-the-reactor); Uprates (#constellation-squeezes-the-reactors); Darlington (#darlington-builds-on-the-old-plug); Oklo (#oklo-sells-the-electricity); Kemmerer (#terrapower-waits-on-the-fuel); Hermes 2 (#kairos-signs-before-it-switches-on); The fuel, enrichment table (#eunice-cannot-fill-the-gap); Claims on record; What would prove me wrong; Research notes.

## Frontmatter notes

- `date: 2026-10-30` is a placeholder; at go-live it becomes the real publish time. The two live claims keep their own `date` fields in claims.ts (already set: 2026-09-29T12:49:48+08:00 and 2026-10-30T11:47:00+08:00), so nothing is re-dated.
- Slug `nuclear-for-ai` is new, as the brief set. Both live URLs therefore redirect (below). Alternative for Tommy: keep the deep piece at `constellation-restarts-the-reactor` (published today, LinkedIn post scheduled Fri 4 Dec) and redirect only Oklo. I followed the brief.
- `cover: "/covers/constellation-restarts-the-reactor.svg"` (existing) until a new cover is drawn; proposal below.
- Tags: power, nuclear, grid, supply-chain (all existing).

## Thesis, and how the old pieces are treated

Thesis: nuclear power for AI arrives in the order of what each project already owns. Restarts and uprates reuse a licensed site, a grid place and ordinary fuel, so they deliver this decade; the HALEU reactors have permits, ground broken and buyers, but their fuel has stopped in America and has not started at the plants contracted to replace it.

Each absorbed piece becomes one rung of the dated ladder (restart borrowed plug, restart held plug, uprate, small reactor on old site, advanced x3) with its four gates (grid place, reactor work, licence class, fuel), plus an enrichment supply table covering both ordinary enrichment (Eunice) and HALEU (TerraPower, Oklo, Kairos).

Held drafts, handled per their hold reasons:
- constellation-squeezes-the-reactors (held: "key inference from the NRC list to Google's units"): the piece uses the NRC list only as Constellation-wide, says it covers Amazon's and Meta's uprates too and withholds plant names, "so it is not Google's schedule. That is why I held a separate claim on it." Its claim is not quoted or adopted.
- darlington-builds-on-the-old-plug (held: "schedule dates press-only"): the piece uses only CNSC, Ontario, Hydro One and GE Vernova primary facts. OPG's end-2030 grid date and the 2028 approval of units 2 to 4 are left out, and the piece says Darlington's claim is held until OPG's filings can be read at source. The IESO 65% / 8.6% line was cut in the trim.

The Oklo "Centrus enriches HALEU" wrinkle is handled openly in the fuel section and in the Oklo "Where I was wrong" note: Centrus's contracted production under Option 1a finished mid-June 2026, DOE "does not currently intend to exercise further options", the next contracted tonne is due by July 2032, and the Oklo supply is a letter of intent of 18 June 2026, deliveries from 2029, "subject to negotiation of definitive agreements" (Centrus 10-Q, re-read 30 Oct 2026). No definitive Centrus-Oklo agreement found (search 30 Oct 2026).

## Claims on record: notes added

- constellation-restarts-the-reactor: holds; test open. Two cautions stated: Palisades shows a held grid place makes a restart possible, not quick; the uprates come in outage-sized steps through 2032.
- oklo-sells-the-electricity: "Where I was wrong" on two points: (1) the piece said Meta's agreement "includes a binding prepayment to secure fuel"; the 10-Q calls it a mechanism to prepay, no amount, not a PPA (the Oklo note already says this); (2) the exposure map's "Centrus Energy enriches uranium to HALEU levels" (see above). The claim itself holds. The Oklo note's separate cash correction (US$1.6bn, not US$1.9bn) refers to the original published text, which the current live text no longer contains; left to the note.

## Proposed claims.ts change (existing entries untouched except `home`)

At merge, the two live entries gain only `home: 'nuclear-for-ai'` (both already carry `date`). `claim`, `breaksIf` and `watch` untouched. Draft claims (Palisades, TerraPower, Kairos, Eunice) were never live and are not in claims.ts, so they are not quoted.

New entry:

```ts
  {
    id: 'nuclear-for-ai',
    claim: 'Nuclear power for AI arrives in the order of what each project already has: restarts and uprates of existing American reactors, which reuse a licensed site, a grid place and ordinary fuel, deliver this decade, while reactors fuelled with HALEU deliver little before 2031, because government stock covers only a few first cores and commercial enrichment at the level they need has stopped in America and not started at the plants contracted to replace it.',
    breaksIf: 'Reactors fuelled with HALEU together send electricity to American grids from 100 MW or more of capacity on or before 31 December 2030; or none of Crane, Palisades or Duane Arnold has delivered power to the grid by 31 December 2029.',
    watch: ['First electricity to a grid from Aurora-INL (target 2028), Kemmerer Unit 1 (complete 2030) and Hermes 2 (operations 2030)', 'First enrichment of uranium at ASP Isotopes\' Pelindaba plant, and the size of the Energy Department\'s HALEU commitments', 'Whether Centrus agrees with the Energy Department to operate the Piketon HALEU cascade privately (maintenance only since 30 June 2026), and progress on the one tonne due by July 2032', 'A definitive Centrus and Oklo HALEU agreement', 'Crane (2027), Palisades (no date since 21 October 2026) and Duane Arnold (first quarter 2029 at the latest) first power to the grid', 'Constellation uprate megawatts in service and the NRC\'s expected uprate list', 'EIA Uranium Marketing Annual Report: Russian and US-origin SWU after the waivers end on 1 January 2028'],
  },
```

Why the test is real (revised after fact-check, 30 Oct 2026): the cause now names government stock as covering only a few first cores, so Aurora-INL (75 MW, 5 t of government HALEU) can run without breaking the claim; the 100 MW threshold means a second HALEU reactor (Hermes 2, 50 MW, source unnamed) or Kemmerer (345 MW, ASP plus a conditional DOE promise) must also deliver. Oklo targets 2028 and TerraPower and Kairos 2030, so the limb can fail inside the window. The restart limb is now "none of" the three by end 2029, with no cause judgement to score. Alternatives considered: (A) "no new reactor of any kind by 2030" rejected, because Darlington uses ordinary fuel and its schedule is press-only; (B) an enrichment-volume test (EIA US-origin SWU) rejected as the Eunice draft's own test.

## Redirect map

| Old URL | Redirect to | Status today |
|---|---|---|
| /journal/constellation-restarts-the-reactor/ | /journal/nuclear-for-ai/#constellation-restarts-the-reactor | live (30 Oct); LinkedIn scheduled Fri 4 Dec |
| /journal/oklo-sells-the-electricity/ | /journal/nuclear-for-ai/#oklo-sells-the-electricity | live (29 Sep) |
| /journal/palisades-waits-on-the-reactor/ | /journal/nuclear-for-ai/#palisades-waits-on-the-reactor | scheduled draft (site 9 Dec, LinkedIn 11 Jan) |
| /journal/eunice-cannot-fill-the-gap/ | /journal/nuclear-for-ai/#eunice-cannot-fill-the-gap | scheduled draft (site 4 Jan, LinkedIn 15 Jan) |
| /journal/kairos-signs-before-it-switches-on/ | /journal/nuclear-for-ai/#kairos-signs-before-it-switches-on | scheduled draft (site 18 Jan, LinkedIn 20 Jan) |
| /journal/terrapower-waits-on-the-fuel/ | /journal/nuclear-for-ai/#terrapower-waits-on-the-fuel | draft (check its publish task) |

Held drafts constellation-squeezes-the-reactors and darlington-builds-on-the-old-plug were never live; anchors exist anyway. Inbound links on the site to the two live URLs (Palisades and Darlington drafts link to Crane; Darlington links to Oklo; the Constellation piece links to Oklo) resolve through these redirects. At merge the drafts leave `src/content/journal/` and go verbatim, with the two live originals, into `research-build/archive/pieces/`. The scheduled publish tasks for Palisades, Eunice, Kairos (and TerraPower if any) and their LinkedIn posts need pausing or repointing; Tommy's decision.

## stack.ts

Layer `onsite`. At merge, replace `'constellation-restarts-the-reactor', 'oklo-sells-the-electricity'` with `'nuclear-for-ai'`. Optional `what` edit: "Turbines, fuel cells, batteries and reactors, new or restarted, make or store power for the site." Honest wrinkle: every project here feeds a grid, not a fenced campus. A separate "Fuel for the power plants" layer, proposed in the TerraPower and Eunice sidecars, is no longer needed now that the fuel lives inside this piece.

## Glossary (src/pages/glossary.astro, "Getting power to the building")

Already present: HALEU, Fast reactor, SMR, Restart (nuclear), Uprate, Nuclear Regulatory Commission, FERC, PJM, PPA.
Add (wording from the cluster sidecars, checked against the piece):
- Enrichment: Raising the share of uranium-235, the atom that splits, by spinning uranium gas through fast centrifuges. Ordinary reactors use up to about 5 per cent; HALEU runs from 5 to 20.
- Cascade (enrichment): A line of centrifuges linked so each passes slightly richer gas to the next. Centrus's demonstration cascade in Ohio has sixteen.
- SWU: Separative work unit, the standard measure of enrichment work. American reactor owners bought about 12.7 million in 2025.
- First core: The full initial load of fuel a new reactor needs before it can start, far larger than a yearly reload.
- MISO: The grid operator and wholesale market across much of the American Midwest and South.
- Suspension (of a power plant): In MISO, a plant that stops running but keeps its connection, for at most 36 cumulative months in any five years.
- Capacity interconnection rights: In PJM, a plant's right to deliver a set amount of power onto the grid at its connection point; a retiring plant can, with approval, hand them to another.
- Refuelling outage: The planned shutdown, every 18 to 24 months at Constellation's units, when a reactor takes new fuel and heavy equipment can be swapped.
- Extended power uprate: The largest kind of uprate, approved for up to 20 per cent more power, needing new heavy equipment and an NRC licence amendment.
- Construction permit: The NRC's permission to build a reactor of the design described; a separate operating licence is needed to run it.
- Test reactor (non-power): A reactor licensed for research under section 104c of the Atomic Energy Act; the law caps the share of its running costs that can go to selling energy.
- Thermal and electrical megawatts: A reactor's heat rating (MWt) is larger than its electrical output (MWe), because a steam plant turns well under half its heat into power.
- Boiling water reactor: A water-cooled reactor in which the water around the fuel boils and its steam drives the turbine directly.

## numbers.ts (physical only)

Repoint existing: `835 MW` (piece constellation-restarts-the-reactor) and `75 MW` (piece oklo-sells-the-electricity) to `piece: 'nuclear-for-ai'` (the redirects also work). New:
```ts
  { layer: 'onsite', value: '900 kg', what: 'HALEU delivered by Centrus\'s sixteen-centrifuge demonstration cascade in Ohio, the only American enrichment line that has made it. Its contracted production finished in mid-June 2026; the next contracted tonne is due by July 2032.', piece: 'nuclear-for-ai', asOf: 'August 2026' },
  { layer: 'onsite', value: '760 MW', what: 'Grid rights FERC let Constellation move to the Crane restart from two Eddystone units it had planned to retire, so Crane need not wait for new lines; a fresh connection was not fully deliverable before the end of 2030.', piece: 'nuclear-for-ai', asOf: '1 June 2026' },
  { layer: 'onsite', value: '26%', what: 'Share of the enrichment bought by US reactor owners in 2025 that came from Russia; every waiver under the ban ends by 1 January 2028.', piece: 'nuclear-for-ai', asOf: 'EIA, August 2026' },
```

## LinkedIn post (§9)

```
The only American plant that has made the near-20% uranium the new reactors need delivered 900 kilograms in one contract phase, and in June its contracted production stopped.

That fuel, HALEU, is what Oklo, TerraPower and Kairos Power need, and the next contracted American tonne is due in 2032. So the nuclear power AI gets this decade comes from reactors that already exist: Crane for Microsoft in 2027, uprates for Google through 2032, and two other restarts, each reusing a licensed site, a grid place and ordinary fuel.

The piece covers a dated ladder of every route from restart to advanced reactor, the gate each one waits on, and the enrichment supply behind them.

https://thephysicallayer.fyi/journal/nuclear-for-ai/

#NuclearEnergy #DataCentres #EnergyInfrastructure
```
Note: 900 kg is Phase 2 only (to June 2025); Phase 1 and Option 1a also produced HALEU, quantities not stated in the 10-Q.

## Cover proposal (not drawn)

`/covers/nuclear-for-ai.svg`. One idea: a ladder of four rungs drawn bold. Top two rungs (RESTART, UPRATE) carry amber cooling towers already plugged into an amber grid line; the bottom two (SMR, ADVANCED) carry towers drawn in outline, each with a small empty fuel canister beside it in blue, and a gap in the line. Caption in letter-spaced grey: "NUCLEAR FOR AI: OLD REACTORS FIRST". Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Edits other drafts need (not made)

- `research-build/archive/journal-drafts/terrapower-waits-on-the-fuel.md` (sidecar) says "Centrus has signed HALEU supply contracts with Oklo, Radiant, Antares and X-energy in 2026". For Oklo it is a letter of intent (18 June 2026), subject to definitive agreements. Fix that line if the sidecar is reused.
- `src/content/journal/oklo-sells-the-electricity.md` exposure map ("Centrus Energy enriches uranium to HALEU levels"): not edited; the original text is kept verbatim in the archive, and the deep piece's note says why it no longer holds.
- `src/content/calls/oklo.md` keeps pointing at the same claim id; no change. Its "Centrus letter of intent from 2029" matches the deep piece.
- If the deep piece publishes before 4 Dec, the scheduled LinkedIn post for constellation-restarts-the-reactor (4 Dec) still works via the redirect; Tommy may prefer to swap it for the post above.

## Sources (URL and date)

Re-opened by me on 30 Oct 2026:
- Centrus Energy Form 10-Q to 30 June 2026, filed 6 Aug 2026: https://www.sec.gov/Archives/edgar/data/1065059/000162828026053863/leu-20260630.htm (Option 1a production completed mid-June; DOE does not intend further options; 900 kg Phase 2 delivered; US$900m task order, 1 MTU by July 2032; Oklo LOI June 2026, up to five reactors, deliveries from 2029 subject to definitive agreements; first new Piketon centrifuges 2029)
- Centrus 8-K, 18 Jun 2026 (Oklo LOI), via search: https://www.boardroomalpha.com/sec/leu-8-k-2026-06-18-0001628280-26-044360 (summary only; the 10-Q is the cited source)
- Holtec Highlights HH-41.24, 21 Oct 2026: https://holtecinternational.com/hh-41-24/ (assembly recovered; no restart date; no newer Palisades release on the page)
- NextEra, DOE loan for Duane Arnold, 8 Sep 2026: https://newsroom.nexteraenergy.com/2026-09-08-U-S-Department-of-Energy-Closes-Up-to-1-9-Billion-Loan-to-Restart-NextEra-Energys-Duane-Arnold-Energy-Center (615 MW; restart "no later than the first quarter of 2029, pending regulatory approvals"; Iowa certificate June 2026; NRC oversight; no grid detail)

From the cluster sidecars and research notes (primary, verified there, not re-opened today):
- Constellation, 20 Sep 2024: https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html
- Constellation Q3 2024 results, 4 Nov 2024: https://www.constellationenergy.com/news/2024/Constellation-Reports-Third-Quarter-2024-Results.html
- Constellation Q2 2026 results, 6 Aug 2026: https://www.constellationenergy.com/news/2026/08/constellation-reports-second-quarter-2026-results.html
- Constellation FERC waiver request, docket ER26-2028-000, 31 Mar 2026 (as read for the Constellation note): https://www.rtoinsider.com/wp-content/uploads/2026/04/20260331-5562_2026.03.31-Crane-Waiver-Request.pdf ; FERC order 1 Jun 2026, docket ER26-2028-000
- Constellation and Google, 6 Oct 2026: https://www.constellationenergy.com/news/2026/10/google-and-constellation-announce-landmark-agreement-to-bring-890-mw-of-new-nuclear-capacity-to-pjm-grid.html ; Google, 6 Oct 2026: https://blog.google/company-news/why-were-backing-americas-existing-nuclear-plants/
- Constellation Form 10-K 2025: https://www.sec.gov/Archives/edgar/data/1868275/000186827526000032/ceg-20251231.htm
- NRC expected uprate applications, updated 8 Sep 2026: https://www.nrc.gov/facilities-safety/operating-reactors/operating-reactor-licensing/power-uprates/status-of-power-uprate-applications/expected-applications-for-power-uprates ; NRC uprate fact sheet: https://www.nrc.gov/reading-rm/doc-collections/fact-sheets/power-uprates.html
- FERC order, Holtec Palisades, ER25-1083-000, 190 FERC ¶ 61,132, 28 Feb 2025 (eLibrary 20250228-3040); MISO GIA SA 1838, ER25-1151-000
- Holtec Form S-1/A, 8 Sep 2026: https://www.sec.gov/Archives/edgar/data/2104277/000119312526384287/d40440ds1a.htm
- Palisades emergency LAR, 30 Sep 2026: https://www.nrc.gov/docs/ML2627/ML26273A469.pdf ; Holtec HH-41.22, 21 Sep 2026: https://holtecinternational.com/hh-41-22/
- CNSC, 4 Apr 2025: https://www.canada.ca/en/nuclear-safety-commission/news/2025/04/commission-authorizes-ontario-power-generation-inc-to-construct-1-bwrx-300-reactor-at-the-darlington-new-nuclear-project-site.html ; CNSC project page: https://www.cnsc-ccsn.gc.ca/eng/reactors/new-reactor-power-plant-projects/new-reactor-power-plant-facilities/darlington-new-nuclear-project/
- Ontario, 8 May 2025: https://news.ontario.ca/en/release/1005889/ontario-leads-the-g7-by-building-first-small-modular-reactor
- Hydro One, 27 Mar 2023: https://hydroone.mediaroom.com/2023-03-27-Hydro-One-begins-community-engagement-on-proposed-transmission-line-in-Clarington-to-support-Ontarios-growing-energy-needs
- GE Vernova, 27 Jan 2025: https://www.gevernova.com/news/press-releases/ge-hitachi-awards-contract-bwrx-300-reactor-pressure-vessel-bwxt
- Oklo Form 10-Q to 30 Jun 2026 (7 Aug 2026), 10-K 2025, business update 7 Aug 2026, groundbreaking 22 Sep 2025, Oklo and Meta 9 Jan 2026: as cited in `src/content/calls/oklo.md`
- NRC, Kemmerer permit, 4 Mar 2026: https://content.govdelivery.com/accounts/USNRC/bulletins/40ca5a7 ; TerraPower, 4 Mar 2026: https://www.terrapower.com/NRC-Approves-Natrium-Reactor-Construction-Permit ; TerraPower construction start, 23 Apr 2026: https://www.terrapower.com/TerraPower-Commences-Construction-on-Americas-First-Utility-Scale-Advanced-Nuclear-Power-Plant ; TerraPower and Meta, 9 Jan 2026: https://www.terrapower.com/terrapower-announces-deal-with-meta
- ASP Isotopes 10-Q to 30 Jun 2026, 14 Aug 2026: https://www.sec.gov/Archives/edgar/data/1921865/000119312526352603/aspi-20260630.htm
- DOE HALEU allocations, 9 Apr 2025: https://www.energy.gov/articles/us-department-energy-distribute-first-amounts-haleu-us-advanced-reactor-developers ; DOE HALEU enrichment services (5 Jan 2026): https://www.energy.gov/ne/haleu-enrichment-services
- NRC CPTR-7, 21 Nov 2024: https://www.nrc.gov/docs/ML2432/ML24324A021.pdf ; NRC Hermes 2 page: https://www.nrc.gov/reactors/non-power/new-facility-licensing/hermes2-kairos ; Hermes extension order, 13 May 2026: https://www.federalregister.gov/documents/2026/05/18/2026-09880/in-the-matter-of-kairos-power-llc-hermes-test-reactor-extension-of-latest-date-for-completion-of ; 42 U.S.C. 2134: https://www.law.cornell.edu/uscode/text/42/2134
- Kairos, TVA and Google, 18 Aug 2025: https://www.kairospower.com/updates/google-kairos-power-tva-collaborate-to-meet-americas-growing-energy-needs ; Kairos newsletter, 1 Oct 2026: https://kairospower.com/updates/the-path-to-deployment
- Public Law 118-62, 13 May 2024: https://www.govinfo.gov/content/pkg/PLAW-118publ62/html/PLAW-118publ62.htm
- EIA 2025 Uranium Marketing Annual Report, Aug 2026: https://www.eia.gov/uranium/marketing/pdf/umar.pdf
- Urenco, 29 Jun 2026: https://www.urenco.com/news/usa/2026/urenco-usa-continues-successful-installation-of-us-uranium-enrichment-capacity ; Urenco, 2 Apr 2026: https://www.urenco.com/news/usa/2026/urenco-usa-reaches-half-way-point-of-current-u.s-capacity-expansion
- NRC Eunice Amendment 63, 23 Mar 2015: https://www.nrc.gov/docs/ML1504/ML15049A402.pdf ; NRC acceptance of Orano application, 21 May 2026: https://www.nrc.gov/docs/ML2613/ML26134A324.pdf
- Orano, 10 Oct 2024: https://www.orano.group/en/news/news-group/2024/october/laying-of-the-foundation-stone-of-the-georges-besse-2-plant-extension
- Leads, credited once: Leo Cui, "Small Modular Reactors (SMR) Explained" (https://www.youtube.com/watch?v=uojk6TaosEg), "The Entire Energy Sector Explained" (https://www.youtube.com/watch?v=0zZyEF4Cq9U), and his Constellation video.

## Figures dropped or flagged

- Duane Arnold's grid fix: FERC order of 25 Aug 2025 (eLibrary accession 20250825-3034) reportedly let NextEra fold the interconnection rights of three solar projects at the site back into the nuclear plant's MISO agreement, up to 619 MW, operation deadline 31 Dec 2029. Press only (Utility Dive 26 Aug 2025; eLibrary did not render, Troutman 403). Not in the body; the ladder says "Not stated by NextEra". If confirmed at source, it is a third "borrowed plug" and strengthens the top rung; add one line to the Palisades section.
- Kairos's single reactor of about 125 MWt and its "no amendment needed" statement: press only (POWER, ANS). The 125 MWt figure is out; the body says only "Kairos says its permits still cover the larger reactor" (a press-reported position, no figure). Flag for Tommy.
- TerraPower's 2022 "at least two years" delay and Russian HALEU plan: press only (WNN, CNBC). Dropped.
- ASP/Necsa test-bench refurbishment (WNN, 19 Oct 2026): trade press. Dropped.
- Darlington: end-2030 grid date, 2028 approval of units 2 to 4, C$13.2bn derived test, basemat date of 22 Apr 2026, refurbishment completion: press or derived; dropped (the reason the draft is held). IESO 65% / 8.6%: primary, cut in the trim.
- Constellation uprates: per-unit split and Google-specific schedule: not public; the piece says so. Calvert Cliffs 190 MW and the US$4.3bn: not used.
- Natrium storage boost to 500 MW, 2.8 GW for Meta: primary, cut in the trim.
- Crane US$1bn DOE loan, Palisades US$1.52bn DOE loan, Duane Arnold US$1.9bn loan: not used (money, not mechanism).
- Rosatom ~43% of world capacity (WNA, secondary compiler): not used.
- Constellation Q3 2026 results (9 Nov, unconfirmed) and Oklo Q3: not out on 30 Oct; re-check Crane and Aurora dates before publish.

## Could not verify today

- The FERC Crane order and waiver request were read for the Constellation note, not by me today; the figures match that note and the 6 Aug 2026 release.
- Palisades "NRC operating basis restored, July 2025" rests on Holtec's S-1/A as recorded in the Palisades sidecar.
- No Crane, Palisades or Duane Arnold update after 22 Oct 2026 found (searches 30 Oct).
- Oklo and TerraPower figures rest on the Oklo note and TerraPower sidecar readings of the filings; EIA, Urenco, Orano and NRC enrichment figures rest on the Eunice sidecar.

## Fact-check fixes applied (30 Oct 2026)

1. Exposure map: the file on disk carried the equipment-queue map (not mine; overwritten after my first pass). Rewritten, 131 words, exact disclaimer pair: plant owners (Constellation, NextEra Energy, Holtec), reactor makers (Oklo, TerraPower, Kairos Power, GE Vernova Hitachi), enrichers (Centrus Energy, Urenco, Orano, ASP Isotopes), buyers, and On the other side. General Matter and Ontario Power Generation no longer named in the map.
2. HALEU defined as "just under 20 per cent"; top layer now says Centrus is the only line that has made HALEU "at the level these reactors need" (Urenco USA reached 8.5% on 11 Dec 2025 under NRC permission up to 10% of 30 Sep 2025, per the fact-check; not used in the piece). Glossary HALEU entry already says 5 to 20; consider adding "advanced reactors mostly need just under 20".
3. Centrus: DOE exercised Option 1b on 30 June 2026, three months of maintenance and storage, no production; Centrus is "working with DOE on future agreements to enable the Company to privately operate the cascade", no assurance (10-Q, re-read 30 Oct). In the fuel section, the top layer ("ordered only maintenance since"), the Oklo note and the watch list.
4. 900 kg labelled Phase 2 only, to June 2025, in the table and LinkedIn post.
5. Oklo: "does not call it a power purchase agreement"; the note now says the "letters of intent stay letters" limb currently points towards a break.
6. Hermes 2: the press-only Kairos "permits still cover it" line cut; "removing legacy items to prepare for site excavation" (Kairos, 1 October 2026, https://kairospower.com/updates/the-path-to-deployment) in the table, body and sources.
7. New claim re-aimed (above); falsifier section rewritten to match.
8. Cut: Darlington cost sentence (C$6.1bn, C$1.6bn, C$20.9bn now unused), Natrium-for-Meta paragraph, NRC uprate-size sentence; also trimmed Groves, the Palisades contract detail ($100m payment now unused) and the TENEX line.

Counts after fixes: top layer 445 words; investor layer 2,495 by raw count before the map; map 131. check-piece.py on a scratch copy: 0 failures, 2 warnings (sources line 207 words; average sentence 25, inflated by tables).
