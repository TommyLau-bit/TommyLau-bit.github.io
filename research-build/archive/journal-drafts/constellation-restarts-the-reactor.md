# Constellation draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/constellation-restarts-the-reactor.md` (draft: true)
Cover: `public/covers/constellation-restarts-the-reactor.svg`
Drafted 9 October 2026. Claim needs Tommy's approval before publish.
Checker: 0 failures, 0 warnings. Body about 515 words, 15 figures, 1 money figure.

## Proposed claim

The fastest nuclear power Constellation can bring to AI this decade comes from reactors that already hold a place on the grid: at Crane the reactor can be ready by 2027, but a fresh grid connection would not have been fully ready until around 2030 or later.

### Alternatives considered

1. "Restarts and uprates at existing sites are the only firm carbon-free power AI can get in volume before 2030, and few sites can be restarted." Rejected as the lead: true in outline but mostly a supply count, hard to falsify cleanly, and close to the Oklo piece's framing. Kept as the "why supply cannot catch up" paragraph.
2. "Big tech's long contracts, not power prices, are what make restarts happen (Microsoft for Crane, Google for 890 MW of uprates)." Rejected: about financing rather than physics, and drifts towards commercial terms that belong in a research note.

Chosen because the evidence is unusually sharp and new to the site: a closed reactor lost its grid place, PJM's study pushed full connection to the end of 2030 or later, and Constellation fixed it only by moving 760 MW of rights from two Eddystone units it had planned to retire, approved by FERC on 1 June 2026. It ties nuclear to the site's core argument (the connection, not the generator, binds) and has a dated, observable test.

## claims.ts entry

```ts
  {
    id: 'constellation-restarts-the-reactor',
    claim: 'The fastest nuclear power Constellation can bring to AI this decade comes from reactors that already hold a place on the grid: at Crane the reactor can be ready by 2027, but a fresh grid connection would not have been fully ready until around 2030 or later.',
    breaksIf: 'Crane, with the 760 MW of grid rights transferred from Eddystone, has still not delivered power to the grid at full output by 31 December 2028, which would mean the reactor work and not the connection set the pace; or restarts and uprates that need new grid capacity are connected as quickly as those that reuse an existing one.',
    watch: ['Crane\'s first power to the grid against the 2027 target', 'Whether Crane reaches full deliverability before PJM\'s transmission upgrades finish', 'Palisades and Duane Arnold restart dates, and whether reactor work or the connection sets them', 'Whether the first of the 890 MW Google uprates lands in 2028'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"), placed directly before `oklo-sells-the-electricity`, its natural partner (power this decade versus the 2030s bet):
`pieces: ['the-way-out-has-its-own-queue', 'ge-vernova-sells-the-wait', 'the-product-is-time', 'what-the-battery-is-really-for', 'fluence-short-of-american-made', 'constellation-restarts-the-reactor', 'oklo-sells-the-electricity']`

Why `onsite` and not `grid`: the layer is where firm power is made for AI campuses, and its existing `what` sentence already names reactors; nuclear readers will look for it beside Oklo. The argument does lean on the grid connection, so `grid` is defensible, but putting a generator in the connection layer would blur the map. Optional small edit to the layer's `what` at publish: "Turbines, fuel cells, batteries and reactors, new or restarted, make or store power for the site." (Crane is not literally on site: it feeds the PJM grid under a virtual PPA, which is the honest wrinkle; the layer is about who makes firm power for AI.)

## Glossary (heading: "Getting power to the building")

- `Restart (nuclear)`: Bringing a closed reactor back into service after repairs, inspections and regulatory approval. Only a handful of closed American reactors are intact enough to try.
- `Uprate`: Raising the output of a reactor that is already running, usually with new turbines, pumps and controls, within limits set by the reactor's design and its licence.
- `Capacity interconnection rights`: In PJM, a power plant's right to deliver a set amount of power onto the grid at its connection point. A plant that closes gives them up; a plant that retires can, with approval, hand them to another.
- `FERC`: The Federal Energy Regulatory Commission, the American regulator of interstate electricity transmission and wholesale power markets.
- `Nuclear Regulatory Commission`: The federal safety regulator that licenses American reactors, including any restart.

Existing PJM and PPA entries already fit.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '835 MW', what: 'Output of the Crane reactor at Three Mile Island that Constellation is restarting for Microsoft, enough for a large AI campus running around the clock.', piece: 'constellation-restarts-the-reactor', asOf: 'target 2027' },
```

Optional second: `{ layer: 'grid', value: '760 MW', what: 'Grid rights Constellation moved from two Eddystone units it had planned to retire to Crane so the restart need not wait until 2030 or later for new transmission lines.', piece: 'constellation-restarts-the-reactor', asOf: '1 June 2026' }`

## LinkedIn post (§9)

```
The hardest part of restarting the Three Mile Island reactor was not the reactor. It was the wire.

Constellation can have the 835 megawatt unit ready for Microsoft in 2027, but a fresh grid connection would not have been fully ready until around 2030 or later. So it borrowed one, moving grid rights from two old units it had planned to retire. For AI campuses that want firm, carbon-free power this decade, that is the real constraint: a place on the grid that already exists.

The piece covers how a reactor restart works, why Constellation had to borrow a connection, and what would prove me wrong.

https://thephysicallayer.fyi/journal/constellation-restarts-the-reactor/

#NuclearEnergy #DataCentres #EnergyInfrastructure
```

## Sources (every figure)

- Constellation, "Constellation to Launch Crane Clean Energy Center, Restoring Jobs and Carbon-Free Power to The Grid", 20 September 2024: https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html
  - 20-year PPA with Microsoft; about 835 MW; unit shut 20 September 2019 "for economic reasons"; original target 2028; NRC approval required. (1979 accident at Unit 2 is the public record of TMI.)
- Constellation third quarter 2024 results, 4 November 2024: https://www.constellationenergy.com/news/2024/Constellation-Reports-Third-Quarter-2024-Results.html
  - "approximately $1.6 billion of cash from operations for capital expenditures necessary to restart the plant, with an estimated in-service date of 2028."
- Constellation, one-year update, September 2025: https://www.constellationenergy.com/news/2025/09/one-year-later-crane-clean-energy-center-still-in-the-spotlight-and-ahead-of-schedule.html (restart pulled forward to 2027 after PJM accepted the early interconnection request filed February 2025).
- US Department of Energy, "Energy Department Closes Loan to Restart Nuclear Power Plant in Pennsylvania", 18 November 2025: https://www.energy.gov/articles/energy-Department-closes-loan-restart-nuclear-power-plant-pennsylvania
  - $1 billion LPO loan, 835 MW. Not used in the piece (one money figure only); available for the research note.
- Constellation request for limited waiver at FERC, docket ER26-2028-000, filed 31 March 2026 (accession 20260331-5562): https://www.rtoinsider.com/wp-content/uploads/2026/04/20260331-5562_2026.03.31-Crane-Waiver-Request.pdf (PDF would not render for me; facts below confirmed via the FERC order coverage and Constellation's own Q2 release).
  - PJM system impact study listed hundreds of miles of new transmission lines as contingent facilities; transfer of CIRs from Eddystone Units 3 and 4 (380 MW each, 760 MW).
- FERC order granting the waiver, 1 June 2026, docket ER26-2028-000 (as reported by Utility Dive, https://www.utilitydive.com/news/constellation-three-mile-island-crane-nuclear-ferc-waiver/821836/): 760 MW of CIRs transferable; waiver "could potentially increase Crane's interim deliverability and enable Crane to be fully operational before December 31, 2030."
- CEO Joe Dominguez on the fourth quarter 2025 earnings call (February 2026), as reported 2 April 2026 by Power Engineering, https://www.power-eng.com/business/constellation-files-at-ferc-to-keep-crane-nuclear-restart-on-2027-timeline/ : interconnection could be "pushed into the 2030s"; still expects to start the unit in 2027.
- Constellation second quarter 2026 results, 6 August 2026: https://www.constellationenergy.com/news/2026/08/constellation-reports-second-quarter-2026-results.html
  - FERC approved transfer of CIRs from Eddystone Units 3 and 4 to Crane; NRC approved Crane fuel licence amendment; restart expected 2027.
- Constellation and Google, "Google and Constellation Announce Landmark Agreement to Bring 890 MW of New Nuclear Capacity to PJM Grid", 6 October 2026: https://www.constellationenergy.com/news/2026/10/google-and-constellation-announce-landmark-agreement-to-bring-890-mw-of-new-nuclear-capacity-to-pjm-grid.html
  - 890 MW from uprates at 11 units in Illinois, Pennsylvania and New Jersey; 20-year PPA; first uprate 2028; all before end 2032; more than $4.3 billion investment (not used in the piece); separate 2,700 MW 15-year supply deal.
- Google, "Why we're backing America's existing nuclear plants", Amanda Peterson Corio, 6 October 2026: https://blog.google/company-news/why-were-backing-americas-existing-nuclear-plants/
  - Quote used: "The fastest new megawatt is often the one that can be provided by existing infrastructure."
- Constellation Form 10-K for 2025: https://www.sec.gov/Archives/edgar/data/1868275/000186827526000032/ceg-20251231.htm
  - Nation's largest nuclear fleet, about 22 GW, 14 stations, 25 units (the piece says "America's largest nuclear fleet", no figure).
- Exposure map context (not cited in the body): Holtec Palisades restart, no firm date as of July 2026 (ANS, 8 July 2026, https://www.ans.org/news/2026-07-08/article-8187/); NextEra Duane Arnold restart planned with Google (Oct 2025 announcement); Vistra uprates of 433 MW with a DOE conditional loan (Power Engineering, 7 October 2026).

## Could not verify / left out

- The FERC order and Constellation's waiver request themselves: the PDF did not render, so their details rest on trade press reporting of the order plus Constellation's Q2 2026 release confirming the transfer. Fact-check against FERC eLibrary, docket ER26-2028-000, before publish.
- The "into the 2030s" phrasing is the CEO's, from trade-press reporting of the Q4 2025 call; the transcript itself was not read. FERC's own phrasing is full operation "before December 31, 2030".
- That Crane's interconnection rights lapsed on closure is inferred from Constellation having to file a new PJM interconnection request in February 2025; the piece says only that it "gave up its place on the grid".
- "Only a handful of closed American reactors are intact enough to restart" is a general statement (Palisades, Duane Arnold, Crane are the known cases); no single primary count was found.
- Palisades: Holtec's February 2026 target passed; no firm restart date as of July 2026. The map says "is restarting", which stays true.
- Left out: the $1 billion DOE loan and the $4.3 billion uprate investment (money budget), the 22 GW fleet figure, the 2,700 MW supply deal.
