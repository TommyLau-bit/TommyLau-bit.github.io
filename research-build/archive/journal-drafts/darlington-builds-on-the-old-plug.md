# Darlington SMR draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/darlington-builds-on-the-old-plug.md` (draft: true)
Cover: `public/covers/darlington-builds-on-the-old-plug.svg`
Drafted 29 October 2026 from the Watch Later batch (topic approved in outline). Claim wording needs Tommy's approval before publish.

## Proposed claim (revised after fact-check, 29 Oct 2026)

Darlington is the first real test of whether small reactors get cheaper with repetition: OPG is building four identical BWRX-300s on an existing nuclear site with a short new grid link inside an existing corridor, its licences and crews, so the first unit should reach the grid by the end of 2030, and when OPG seeks approval for units 2 to 4 (expected 2028) the three together should come in at or below the roughly C$13.2bn its 2025 budget leaves for them.

Main claim: repetition. Supporting point: the old site (unit 1 on the grid by end-2030, already a year after GE Vernova's "end of 2029").

### Alternatives considered

1. "Darlington unit 1 reaches the grid by end-2030 because it reuses an existing nuclear connection." Rejected as the lead: it largely repeats constellation-restarts-the-reactor (existing connection beats a new one). Kept as the supporting test.
2. "A public utility, not a vendor or a private developer, is the only owner that can carry a first-of-a-kind SMR fleet." Rejected: hard to falsify on a date, and leans on oklo-sells-the-electricity's build-risk point. Kept as one line.

Chosen because it is new to the site (whether repetition lowers cost, the core SMR promise), is tied to the site argument (the old plug is what keeps one crew on one site long enough to learn), and has a dated, observable test from OPG's own process: the 2028 approval of units 2 to 4 and the end-2030 grid target.

## claims.ts entry

```ts
  {
    id: 'darlington-builds-on-the-old-plug',
    claim: 'Darlington is the first real test of whether small reactors get cheaper with repetition: built on an existing nuclear site with its grid corridor, licences and crews, OPG\'s first BWRX-300 should reach the grid by the end of 2030, and the three units after it should cost less than the first.',
    breaksIf: 'When OPG seeks approval to build units 2 to 4, expected in 2028, the three together are budgeted above the roughly C$13.2 billion its 2025 budget leaves for them (C$20.9 billion less C$6.1 billion for unit 1 and C$1.6 billion for shared systems), on the same basis; or unit 1 has not sent power to Ontario\'s grid by 31 December 2030.',
    watch: ['The first level of the unit 1 reactor building, OPG\'s next milestone, due by the end of 2026', 'The CNSC hearing and decision on the licence to operate applied for on 25 March 2026', 'The budget OPG files when it seeks approval for units 2 to 4, expected in 2028, against about C$13.2 billion', 'Unit 1 first power to the grid against the end-2030 target, already moved from GE Vernova\'s end of 2029'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"), after `oklo-sells-the-electricity`:
`pieces: ['the-way-out-has-its-own-queue', 'ge-vernova-sells-the-wait', 'the-product-is-time', 'what-the-battery-is-really-for', 'constellation-restarts-the-reactor', 'oklo-sells-the-electricity', 'darlington-builds-on-the-old-plug']`

Strictly Darlington is grid-connected generation, not power beside a data centre, but the layer already holds the nuclear pieces (Crane, Oklo) and its `what` line names small reactors. No new layer needed. If another agent's draft (terrapower-waits-on-the-fuel) also lands here, keep both.

## Glossary

- Heading "Getting power to the building": `Boiling water reactor`: A water-cooled nuclear reactor in which the water around the fuel boils, and the steam goes straight to the turbine, with no separate steam generator. The BWRX-300 is a small one.
- Heading "Getting power to the building": `Licence to construct`: Canada's nuclear regulator, the CNSC, licenses a reactor in stages: preparing the site, constructing, then operating. Each needs its own hearing and decision.
- `SMR` already exists and already says later units should be cheaper and quicker: no change.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '22 km', what: 'Length of the new 500 kV line Hydro One plans to connect the Darlington small reactors, built inside an existing corridor beside existing lines.', piece: 'darlington-builds-on-the-old-plug', asOf: '27 March 2023' },
```

Optional: `{ layer: 'onsite', value: '4 x 300 MW', what: 'Ontario Power Generation\'s Darlington New Nuclear Project: four identical BWRX-300 small modular reactors, 1,200 MW in all, the first under construction in the G7.', piece: 'darlington-builds-on-the-old-plug', asOf: '8 May 2025' }`

## LinkedIn post (§9)

```
The first small modular reactor in the G7 is being built beside an old one, and that is the point.

Ontario Power Generation is building four identical BWRX-300 reactors at Darlington, on a nuclear site with its grid corridor, licences and crews already in place. That should get the first unit to the grid by the end of 2030, a year later than first promised. The bigger question is the one every small reactor promise rests on: whether the second, third and fourth come in cheaper than the first.

The piece covers why the old site matters, what OPG has built so far, and the 2028 decision that tests whether repetition pays.

https://thephysicallayer.fyi/journal/darlington-builds-on-the-old-plug/

#NuclearEnergy #SMR #EnergyInfrastructure
```

## Figures in the body and where each comes from

| Figure | Source | Status |
|---|---|---|
| Four identical reactors; first SMR in the G7 | Ontario release, 8 May 2025 | Primary |
| 300 MW BWRX-300, GE Vernova Hitachi, boiling water reactor | Ontario release, 8 May 2025 (BWRX-300, 1,200 MW for four); GE Vernova release, 27 Jan 2025 ("boiling water reactor design") | Primary |
| Existing station four reactors, rebuilding finished early 2026 | OPG announcement of 2 Feb 2026 as reported by ANS Nuclear News, 3 Feb 2026 (four 878 MW CANDU units, refurbishment construction complete) | Press only |
| 22 km line inside existing corridor beside existing lines, Hydro One | Hydro One release, 27 March 2023 | Primary (2023 plan; a separate 2025 Bowmanville switching station expansion by Hydro One, AtkinsRéalis as engineer, is press only and not used) |
| Site preparation licence first issued 2012 | REMOVED from the piece after fact-check: the 2012 issue date is secondary-only (search summaries, Power Magazine, Enerdata); CNSC primary pages confirm only renewal in 2021 and validity to 2031. CMD-24-H3-Ref-R1-1 not opened | Dropped |
| Demand +65% by 2050; data centres 8.6% of 2050 demand | IESO 2026 Annual Planning Outlook summary page; IESO release 27 March 2026 | Primary |
| Licence to construct, April 2025 | CNSC release, 4 April 2025 (valid to 31 March 2035) | Primary |
| Foundation lowered April 2026 | Basemat lift 22 April 2026: OPG story and Ontario announcement as reported by Ontario Construction News, 5 May 2026, and Nuclear News; CNSC project page shows hold point 1 (reactor building foundation) lifted 30 March 2026 | Date press only; hold point primary |
| Licence to operate applied for | CNSC project page: 25 March 2026, 20-year licence | Primary |
| Date moved: GE Vernova "by the end of 2029" (27 Jan 2025) to OPG grid by end of 2030 | GE Vernova release (primary); OPG target via Nuclear News (press) | Mixed |
| About C$13.2bn left for units 2 to 4 (falsifier) | Derived from Ontario release, 8 May 2025: C$20.9bn less C$6.1bn and C$1.6bn; stated in words in the piece | Primary, derived. Company financial figure 2 of 2 |
| Minority public stakes | Prime Minister's release, 23 Oct 2025: Canada Growth Fund 15%, Building Ontario Fund 7.5%, OPG majority owner (percentages not in piece) | Primary |
| First unit C$6.1 billion, shared systems separate (C$1.6bn, not used); costs expected to decline with each later unit | Ontario release, 8 May 2025 (quick facts) | Primary. Company financial figure 1 of 2 in the body |
| Approval of units 2 to 4 expected in 2028 | Nuclear News (ANS), 5 June 2026, in its own words, not a Sinnathamby quote | Press only |
| Grid by the end of 2030 | OPG, Nuclear News (ANS), 5 June 2026 ("connect to the grid by the end of 2030"); WNN, 23 May 2025 ("in service in 2030") | Press only |

Not used in the body but checked: C$20.9bn four-unit budget (Ontario release, primary, includes site preparation, engineering and all four units); C$1.6bn common systems (Ontario, primary); unit 4 about C$4.1bn (WNN, 23 May 2025, press only); federal C$2bn and Ontario C$1bn equity, 15% and 7.5% stakes (Prime Minister's release, 23 Oct 2025, primary).

Schedule note for Tommy: GE Vernova's January 2025 release said commercial operation "by the end of 2029". From the May 2025 investment decision, the target reads as completion by the end of the decade and grid in 2030; OPG told Nuclear News in June 2026 "connect to the grid by the end of 2030". I used OPG's latest. OPG's own pages and its OEB rate filing (EB-2025-0297, which says unit 1 enters commercial operation in the 2027 to 2031 term; a search summary says it gives commercial operation in October 2030, unopened and unverified) returned 403 or would not connect, so the exact OPG wording of the end-2030 date is press-confirmed only. Worth a check of OPG's Q3 2026 report when it is out.

## Sources (every figure)

- Ontario Ministry of Energy and Mines, "Ontario Leads the G7 by Building First Small Modular Reactor", 8 May 2025 (read via the newsroom API): https://news.ontario.ca/en/release/1005889/ontario-leads-the-g7-by-building-first-small-modular-reactor (API: https://api.news.ontario.ca/api/v1/releases/1005889?language=en)
- CNSC, "Commission authorizes Ontario Power Generation Inc. to construct 1 BWRX-300 reactor", 4 April 2025: https://www.canada.ca/en/nuclear-safety-commission/news/2025/04/commission-authorizes-ontario-power-generation-inc-to-construct-1-bwrx-300-reactor-at-the-darlington-new-nuclear-project-site.html
- CNSC Darlington New Nuclear Project page (hold point lifted 30 March 2026; licence to operate application 25 March 2026; site preparation licence to 2031), accessed 29 Oct 2026: https://www.cnsc-ccsn.gc.ca/eng/reactors/new-reactor-power-plant-projects/new-reactor-power-plant-facilities/darlington-new-nuclear-project/
- CNSC, site preparation licence renewal, 12 Oct 2021 (licence first issued 2012): https://www.canada.ca/en/nuclear-safety-commission/news/2021/10/cnsc-renews-ontario-power-generations-site-preparation-licence-for-its-darlington-new-nuclear-project.html
- Hydro One, community engagement on proposed Clarington transmission line, 27 March 2023: https://hydroone.mediaroom.com/2023-03-27-Hydro-One-begins-community-engagement-on-proposed-transmission-line-in-Clarington-to-support-Ontarios-growing-energy-needs
- IESO, 2026 Annual Planning Outlook summary: https://ieso.ca/Sector-Participants/Planning-and-Forecasting/Annual-Planning-Outlook/2026-APO-Summary ; release 27 March 2026: https://ieso.ca/Sector-Participants/IESO-News/2026/03/Mar-27-IESOs-2026-Annual-Planning-Outlook-Shows-Long-Term-Energy-Demand-Continues-to-Rise
- GE Vernova, "GE Hitachi awards contract for BWRX-300 reactor pressure vessel to BWXT", 27 Jan 2025: https://www.gevernova.com/news/press-releases/ge-hitachi-awards-contract-bwrx-300-reactor-pressure-vessel-bwxt
- Prime Minister of Canada, investment in Darlington, 23 Oct 2025 (checked, not used): https://www.pm.gc.ca/en/news/news-releases/2025/10/23/prime-minister-carney-announces-major-new-investment-power-canadas
- Press only: ANS Nuclear News, "North American construction is back, smaller and faster, at OPG's Darlington", 5 June 2026: https://www.ans.org/news/article-8047/north-american-construction-is-back-smaller-and-faster-at-opgs-darlington/
- Press only: ANS Nuclear News, OPG completes Darlington refurbishment construction, 3 Feb 2026: https://www.ans.org/news/2026-02-03/article-7729/opg-completes-darlington-refurbishment-construction/
- Press only: World Nuclear News, budget explainer, 23 May 2025: https://world-nuclear-news.org/articles/what-is-the-budget-for-canadas-first-smr-project
- Press only: Ontario Construction News, basemat installed, 5 May 2026: https://ontarioconstructionnews.com/ontario-marks-smr-milestone-with-installation-of-2-1m-pound-reactor-foundation-at-darlington
- Lead: Leo Cui, "Small Modular Reactors (SMR) Explained", YouTube: https://www.youtube.com/watch?v=uojk6TaosEg (credited once in the sources line)

## Video figures dropped or flagged

- Per-kW divisions (about C$20,300/kW for unit 1, about C$25,700 with shared systems, about C$17,400 for four units): the video's own arithmetic. Recomputed (6.1bn / 300 MW = C$20,333/kW; 7.7bn / 300 MW = C$25,667; 20.9bn / 1,200 MW = C$17,417): arithmetic correct, but dropped, since per-kW figures invite comparison with overnight costs the video itself warns against, and they would break the money budget.
- "These are 2026 Canadian dollars": not verified. Ontario and WNN say the budget includes interest, escalation and contingency; the dollar year is not in the primary release. Dropped; the claims.ts falsifier says "on the basis OPG uses for unit 1".
- C$1.6bn shared systems and C$7.7bn first phase: verified (Ontario), dropped for the money budget.
- C$20.9bn four-unit budget: verified (Ontario); not stated in the piece, used in words to derive the C$13.2bn falsifier figure.
- "OPG has just completed a major refurbishment" leaving a workforce ready: refurbishment completion press-confirmed; the workforce transfer is the video's framing, not stated by a primary source, so the piece says only "crews" and "experienced nuclear crew".
- Blue Energy plans: unverified, left out as instructed.
- Every other SMR project in the video (Linglong One, TerraPower, Dow/X-energy, NuScale/TVA, Army microreactors, criticality list): out of scope for this piece.

## Not verified / limits

- OPG's own website, files.opg.com and the OEB document server blocked (403) or refused connection; not bypassed. End-2030 grid date and the 2028 approval for units 2 to 4 rest on OPG executives quoted by Nuclear News.
- The 2023 Hydro One 22 km line plan may have been modified by the 2025 Bowmanville switching station expansion; the piece uses only the 2023 primary description.

## Fact-check changes, 29 Oct 2026

1. Constellation line now "would have held up ... had it not borrowed a connection", matching constellation-restarts-the-reactor.
2. IESO: data centres 8.6 per cent of all Ontario demand in 2050.
3. "Inherit its grid lines" removed from summary and open; the piece says the grid link is new but short (22 km inside an existing corridor).
4. Falsifier: units 2 to 4 together above about C$13.2bn left in the 2025 budget; date slip from end-2029 to end-2030 stated in the evidence section.
5. Risk line now names OPG majority ownership, federal and provincial minority stakes, and Ontario's power customers.
6. Reordered: opens on the 2028 budget decision, then the learning mechanism, then the site, demand, progress and the date slip.
7. 2012 site licence removed (secondary-only).
