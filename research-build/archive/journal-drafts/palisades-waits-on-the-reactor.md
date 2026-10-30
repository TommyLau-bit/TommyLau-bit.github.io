# Palisades draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/palisades-waits-on-the-reactor.md` (draft: true)
Cover: `public/covers/palisades-waits-on-the-reactor.svg`
Drafted 29 October 2026 (batch 3, Tier A item A1). Claim needs Tommy's approval before publish.
Checker: 0 failures, 0 warnings. Body about 520 words, 15 figures, 1 money figure.
Links to `constellation-restarts-the-reactor` (scheduled draft): publish this one after Crane is live, or drop the link.

## Quality bar (CLAUDE.md, 29 Oct 2026)

1. New mechanism: a grid connection that is held, not lost, but on a clock. MISO's suspension rule (36 cumulative months in five years, then the connection is terminated) and FERC's one-time waiver to 1 March 2027. The site has no piece on an expiring grid place; Crane is the opposite case (connection lost, borrowed from Eddystone).
2. Primary sources: FERC order 190 FERC ¶ 61,132; MISO's filed GIA with its Appendix B milestones; Holtec's S-1/A on EDGAR; Holtec's NRC licence amendment request and RAI response; Holtec's own releases. Only the NRC approval date and the older February 2026 target rest on press, and neither is in the body.
3. Beyond the headline: the same date closes both the grid waiver and the buyers' right to walk away (with a $100 million termination payment). A plant with a held connection still slipped twice, and the slip came from the plant. A PM learns that "holds a grid place" makes a restart possible, not quick.

## Proposed claim

At Palisades the grid connection was held, not lost, so Holtec's restart date is set by work on the reactor and plant, not by the wire, and the held connection, like the buyers' contracts, runs only to March 2027.

### Alternatives considered

1. "Palisades will miss 1 March 2027 and need a second FERC waiver." Rejected: a forecast of a schedule with no disclosed date to anchor it, and a waiver could be avoided by the GIA's "significant steps" clause, so it would be weakly falsifiable either way.
2. "A restart that keeps its grid place still takes years, so restarts are not quick power for AI." Rejected as the lead: true but generic, and it drifts toward contradicting the Crane piece rather than mirroring it. Kept as the "on the other side" line.

Chosen because it is the exact mirror of Crane (there the wire was the slow part; here the wire was held and the reactor is), it rests on FERC, MISO, EDGAR and NRC documents, and the falsifier is observable: what the last item before first grid power turns out to be.

## claims.ts entry

```ts
  {
    id: 'palisades-waits-on-the-reactor',
    claim: 'At Palisades the grid connection was held, not lost, so Holtec\'s restart date is set by work on the reactor and plant, not by the wire, and the held connection, like the buyers\' contracts, runs only to March 2027.',
    breaksIf: 'By 30 June 2027, the plant is ready to run but Palisades\' first power to the grid waits on its switchyard, the transmission lines or MISO; or Palisades loses its MISO interconnection service for a reason other than the plant\'s own readiness.',
    watch: ['Palisades\' first synchronisation to the grid, and what Holtec and the NRC say was the last item before it', 'Whether FERC or MISO is asked to extend the 1 March 2027 suspension deadline', 'Whether Wolverine or Hoosier Energy uses its right to end its contract if the plant is not in service by March 2027', 'Completion of the remaining Appendix B steps in the MISO grid agreement'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"), directly after `constellation-restarts-the-reactor`, its mirror:
`pieces: ['the-way-out-has-its-own-queue', 'ge-vernova-sells-the-wait', 'the-product-is-time', 'what-the-battery-is-really-for', 'constellation-restarts-the-reactor', 'palisades-waits-on-the-reactor', 'oklo-sells-the-electricity']`
(Insert `darlington-builds-on-the-old-plug` and `terrapower-waits-on-the-fuel` wherever their own sidecars place them.) Same honest wrinkle as Crane: Palisades feeds the MISO grid, not a fenced campus; the layer is where firm power for AI is made.

## Glossary (heading: "Getting power to the building")

- `MISO`: The Midcontinent Independent System Operator, which runs the grid and wholesale power market across much of the American Midwest and South.
- `Suspension (of a power plant)`: In MISO, a plant that stops running but keeps its grid connection, for at most 36 cumulative months in any five years, after which the connection is ended unless regulators allow more time.
- `Switchyard`: The outdoor yard of breakers and switches that links a power plant to the high-voltage transmission lines.
- `Fuel assembly`: A bundle of fuel rods, held in a frame, that is lowered into a reactor core as one unit.

Existing `Restart (nuclear)`, `FERC`, `Nuclear Regulatory Commission`, `PPA` and `Interconnection queue` entries already fit.

## numbers.ts (physical figures only)

```ts
  { layer: 'grid', value: '36 months', what: 'How long a power plant in MISO may stay suspended, keeping its grid connection, before the connection is ended; Palisades was granted a one-time extension to 1 March 2027.', piece: 'palisades-waits-on-the-reactor', asOf: '28 February 2025' },
```

## LinkedIn post (§9)

```
Palisades never lost its place on the grid. It is still not running.

Holtec kept the Michigan plant's grid connection alive under a one-time federal extension, and its wires were reconnected in September. The latest delay came from the reactor: a tilted fuel bundle that stopped fuel loading for seven weeks. And the grid place it kept, like the contracts for its power, runs only to March 2027.

The piece covers how a held grid connection works, where the reactor set the date, and what would prove me wrong.

https://thephysicallayer.fyi/journal/palisades-waits-on-the-reactor/

#NuclearEnergy #EnergyInfrastructure #DataCentres
```

## Sources (every figure)

- FERC, Order Granting Waiver Request, Holtec Palisades, LLC, Docket ER25-1083-000, 190 FERC ¶ 61,132, issued 28 February 2025 (eLibrary accession 20250228-3040): https://elibrary.ferc.gov/eLibrary/search (docket ER25-1083)
  - MISO Tariff 38.2.7.n: suspension for "a maximum of thirty-six (36) cumulative months during any five (5) year period", then interconnection service is terminated (38.2.7.k).
  - Palisades interconnection service set to end 20 May 2025; one-time 22-month extension to 1 March 2027 granted.
  - Palisades entered suspended status May 2022; Holtec owner since June 2022; "initial target of October 2025" for return to commercial operation.
  - PPAs with Wolverine and Hoosier oblige return to service by 1 March 2027.
  - Holtec asserted, and FERC relied on, "no network upgrades or other interconnection process impacts"; MISO supported the waiver. Without it Holtec would need a new interconnection request.
  - 820 MW net (the order's figure; the piece uses Holtec's 800 MW).
- MISO, transmittal letter and public Second Amended and Restated GIA, SA 1838, Project J102, among Holtec Palisades, METC and MISO, filed 3 February 2025, Docket ER25-1151-000 (accession 20250203-5242); accepted by letter order 3 April 2025 (accession 20250403-3045).
  - Appendix B "Article 2.3.1 Milestones": reactor head insulation, operator certification and startup plan by 31 Dec 2026; replace switchyard feed 26H5 and NRC reinstatement of operating authority by 15 Jan 2027; reactor startup testing by 1 Feb 2027. "Dates subject to change as agreed by the Parties."
- Holtec Nuclear Corporation, Form S-1/A, filed 8 September 2026: https://www.sec.gov/Archives/edgar/data/2104277/000119312526384287/d40440ds1a.htm
  - About 800 MW, all contracted under fixed-price PPAs; PPAs with Wolverine Power Cooperative and Hoosier Energy, initial term 28 years.
  - "our existing PPAs for the Palisades site require the site to be in-service by March 2027. If the site is not in-service by that date, we and our counterparties each have the right to terminate"; terminating counterparty owed a share of "an aggregate $100 million termination payment".
  - Restart expected in 2026 "in advance of our commitment date with our counterparties of March 2027"; fuel loading commenced 30 August 2026; NRC July 2025 approval; operations status 25 August 2025; $1.52 billion DOE loan and $300 million Michigan grant (money figures not used in the piece); Holtec owns "the land and interconnection breakers".
  - The registration was withdrawn on 25 September 2026 (Form RW): https://www.sec.gov/Archives/edgar/data/2104277/000119312526402799/d40440drw.htm (not used in the piece; share-related, kept out).
- Palisades Energy, Emergency Licence Amendment Request for recovery of fuel assembly DD41, 30 September 2026, NRC ADAMS ML26273A469: https://www.nrc.gov/docs/ML2627/ML26273A469.pdf
  - Mode 6 and fuel loading began 30 August 2026; DD41 "tilted over after being released by the refueling machine", resting at about 30 degrees; emergency processing requested because delay "would result in a delay in the resumption of activities necessary to... restore the plant to power operation".
- Holtec Palisades, Response to Third RAI, 12 October 2026, NRC ADAMS ML26285A034: https://www.nrc.gov/docs/ML2628/ML26285A034.pdf
- Holtec Highlights HH-41.22, "Progress Report on Palisades' March to Startup", 21 September 2026: https://holtecinternational.com/hh-41-22/
  - Reconnected to the 345 kV switchyard on 11 September 2026 after restoration work with ITC; final commissioning continuing; fuel loading paused.
- Holtec Highlights HH-41.24, fuel assembly recovery, 21 October 2026: https://holtecinternational.com/hh-41-24/
  - Assembly recovered with a purpose-built fuel movement device under an NRC-approved licence amendment; remaining work is fuel loading, testing and readiness; no restart date.
- Holtec Highlights HH-47.17, fuel loading begins, 30 August 2026: https://holtecinternational.com/hh-47-17/

Press, context only (not relied on for any figure in the body):
- NRC approval of the DD41 amendment on about 12 or 13 October 2026: Michigan Public, 14 October 2026, https://www.michiganpublic.org/transportation-infrastructure/2026-10-14/regulators-approve-plan-to-remove-damaged-fuel-assembly-at-palisades. The NRC approval letter itself returned 403 to me and was not read. The piece says only "won emergency approval from the regulator", which Holtec's own 21 October release confirms.
- Holtec's earlier target of grid reconnection by end of February 2026: ANS Nuclear Newswire, 8 July 2026, https://www.ans.org/news/2026-07-08/article-8187/ (press only, so the piece says only that the October 2025 target passed).
- Nuclear Engineering International, "Palisades restart delayed", 28 September 2026: https://www.neimagazine.com/news/palisades-restart-delayed/
- FERC waiver summary: Troutman Pepper Locke, March 2025, https://www.troutmanenergyreport.com/2025/03/ferc-grants-waiver-request-to-prevent-termination-of-interconnection-service-to-the-palisades-nuclear-plant/

## Fact-check fixes (29 Oct 2026)

- Video credit removed from the sources line: the video was not used for any fact.
- Summary now says the latest delay, not every delay, came from the plant.
- Switchyard line softened to "the switchyard was reconnected": the GIA step "Replace Palisades Switchyard Interconnection Feed 26H5" (due 15 Jan 2027) may still be open, and Holtec said full switchyard function was still being commissioned on 21 Sep 2026.
- Falsifier rewritten so neither leg confirms the thesis: leg one requires the plant to be ready while power waits on the wire; leg two is a loss of the grid place for a reason other than the plant's readiness.
- October 2025: kept, sourced to the FERC order, which records "an initial target of October 2025" from Holtec. The piece now says "the first target Holtec gave regulators". I read the order myself (eLibrary accession 20250228-3040, downloaded as ER25-1083-000.docx): its header reads 190 FERC ¶ 61,132, Docket No. ER25-1083-000, issued 28 February 2025. The fact-checker could not re-open it; it is in eLibrary under that docket.
- Exposure note now credits FERC, MISO and Holtec for the figures; the contract line now says either side may end the contracts.

## Video figures dropped or flagged

- The outline for this topic came from a scout's background knowledge, not the video: neither transcript (`constellation-microsoft-nuclear`, `smr-explained`) discusses the Palisades restart. The Constellation video covers Crane only, which the site already has.
- `smr-explained` mentions Holtec's SMR-300 at about 340 MW and its two-unit Palisades application: dropped, a different topic (Pioneer 1 and 2).
- The outline's falsifier ("no grid power by 30 Jun 2027") was reworked: no grid power by a date would not show whether the reactor or the wire was slow, so the test now asks what held up first power. The 30 June 2027 date is kept.
- Left out of the body: the $1.52 billion DOE loan, the $300 million Michigan grant, 820 MW net, the 28-year term, the Appendix B dates other than the final step, the SMR-300 plans, and the withdrawn listing.
