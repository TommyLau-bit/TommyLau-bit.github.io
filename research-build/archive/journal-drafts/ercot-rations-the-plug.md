# ERCOT large-load queue draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/ercot-rations-the-plug.md` (draft: true)
Cover: `public/covers/ercot-rations-the-plug.svg`
Drafted 29 October 2026. Topic approved by Tommy; the final claim wording needs his approval before publish.

## Proposed claim

ERCOT will not clear its 474 gigawatt queue of large new loads. When it reopens to large data centres, most new capacity will be rationed: connected on condition that ERCOT may cut it, or that the site brings its own power.

### Alternatives considered

1. "The 474 GW queue is mostly paper: less than half had the studies to enter Batch Zero, so the real Texas pipeline is a fraction of the headline." Rejected as the lead: true but descriptive, and it echoes the announced versus energised point the site has already made. Kept as the evidence section.
2. "Texas will make data centres bring their own power before they connect." Rejected as the lead: too narrow, since ERCOT's own design offers two rationed routes (curtailable and own-generation), and it overlaps the-way-out-has-its-own-queue. Folded into the claim as one of the two routes.

Chosen because it is new to the site (the grid operator choosing how to ration a connection it cannot build fast enough, rather than a government speeding up paperwork or a price auction), it rests on a physical mechanism (lines and substations cannot be built at data centre speed, so the grid sells interruptible access), and it has a dated observable: whether approvals resume by mid-2027 and on what terms.

Builds on the-queue-not-the-chip (linked: transformers and the connection bind) and pairs with the-power-it-drops (ride-through: the grid wants large loads to stay on through faults but be removable on command) and two-governments-one-confession (Singapore rations by efficiency; Texas rations by interruptibility). Contradicts none.

## claims.ts entry

```ts
  {
    id: 'ercot-rations-the-plug',
    claim: 'ERCOT will not clear its queue of about 474 gigawatts of large-load requests. When it reopens to large data centres, most new capacity will come with ERCOT\'s right to cut it, or a condition that the site brings its own power.',
    breaksIf: 'By 30 June 2027 ERCOT is again approving data centres of 75 MW or more to energise, and most of the capacity newly allocated in Batch Zero, its first batch, is firm service, with no curtailment right and no own-generation condition.',
    watch: ['ERCOT\'s verification, audit and community impact reports, which it aims to file by 10 December 2026', 'The date approvals to energise large data centres resume', 'How Batch Zero capacity splits between firm service, the Provisional Controllable Load Resource route and Withdrawal-Limited Private Use Networks', 'PUCT rules implementing SB 6 curtailment and backup generation provisions'],
  },
```

Note for Tommy: if ERCOT is still closed on 30 June 2027 the claim is untested, not confirmed (the piece says so). If you prefer a falsifier that also fires on a still-closed door, the alternative is "or ERCOT is still not approving any large data centre to energise on 30 June 2027", but that would test the speed of the audit rather than the rationing mechanism, so I left it out.

## stack.ts

Layer `grid` ("The grid connection"). Suggested position after `the-power-it-drops` (and after `pjm-sends-the-bill` if that publishes first):
`pieces: [..., 'the-power-it-drops', 'pjm-sends-the-bill', 'ercot-rations-the-plug']`
The layer's constraint sentence (connection waits run to years) fits. No new layer needed.

## Glossary (heading: "Getting power to the building", beside Interconnection queue and Large-load tariff)

- `ERCOT`: The Electric Reliability Council of Texas, which runs the grid and wholesale power market for most of Texas. Its grid is largely cut off from the rest of the United States, so it cannot lean on its neighbours.
- `Large load (Texas)`: A single site drawing 75 megawatts or more, the threshold Texas law sets for the special connection rules data centres face.
- `Curtailable connection`: A connection on condition that the grid operator may cut the site's power when lines are strained. ERCOT's version is called a Provisional Controllable Load Resource.
- `Firm service`: A connection the grid operator plans to keep supplied at all times, without a right to cut it short of an emergency.

## numbers.ts (physical figures only)

```ts
  { layer: 'grid', value: '474 GW', what: 'Large new loads asking to connect to ERCOT\'s Texas grid, about 90 per cent of them data centres. More than five times the most power Texas has ever used at one moment.', piece: 'ercot-rations-the-plug', asOf: 'June 2026' },
```

Optional second: `{ layer: 'grid', value: '6.6 GW', what: 'Seventeen large Texas sites that passed every ERCOT check except the final approval to switch on, held while the state audits data centres.', piece: 'ercot-rations-the-plug', asOf: '20 August 2026' }`

## LinkedIn post (§9)

```
Texas has requests to connect about 474 gigawatts of new demand, more than five times the most power the state has ever used at once.

About 90 per cent of it is data centres, and in August ERCOT stopped letting large new ones switch on while every project is audited. Lines and substations cannot be built at data centre speed, so I expect Texas to reopen on rationed terms: connect if ERCOT may cut you, or bring your own power. That would set the template for every grid short of wires.

The piece covers how ERCOT's rationing works, what its own queue figures show, and what would prove me wrong.

https://thephysicallayer.fyi/journal/ercot-rations-the-plug/

#DataCentres #Grid #Energy
```

## Sources, one per line (figure: source, date)

- 474 GW of large-load requests, about 90 per cent data centres, as of June 2026; about 205 GW eligible for Batch Zero on existing studies (preliminary); 315 projects without a qualifying study excluded: ERCOT, "ERCOT Update", Senate Committee on Business and Commerce, 29 July 2026. https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf (POWER Magazine reproduces ERCOT's chart caption as 474.7 GW, of which 420.8 GW or 90.2 per cent data centres: https://www.powermag.com/abbott-orders-full-audit-of-texas-data-center-interconnection-queue-threatens-to-deny-grid-access/)
- "Over 474 gigawatts", "more than five times Texas' record peak", "approximately 90 percent" data centres; audit to be completed "before any data center project moves forward": Office of the Texas Governor, press release, 3 August 2026. https://gov.texas.gov/news/post/governor-abbott-directs-comprehensive-data-center-audit
- Pause wording ("paused approvals to energize data centers or virtual currency mining facilities ... that are 75 MW or greater", "until the completion of the verification and audit and community impact review"); Community Impact Review Report to be filed with the Commission by 10 December 2026; 17 large loads, 6,608 MW, awaiting only approval to energise; medium loads not affected: ERCOT, "Batch Zero Verification and Audit", PUCT open meeting presentation, 20 August 2026. https://www.ercot.com/files/docs/2026/08/20/Batch-Zero-Verification-and-Audit-PUCT-Presentation.pdf
- Commission granted ERCOT's three good-cause exceptions on 20 August 2026; impact on Batch Zero timeline "TBD": ERCOT Board, Item 14 Batch Zero Update, 11 September 2026. https://www.ercot.com/files/docs/2026/09/11/14-Batch-Zero-Update.pdf
- ERCOT aiming at a 10 December filing (Chad Seely quote); Batch Zero study will miss 9 April 2027: Utility Dive, 21 August 2026. https://www.utilitydive.com/news/ercot-texas-puc-data-center-audit/828472/
- Provisional Controllable Load Resource (ERCOT may reduce consumption "during periods of localized stress"; firm and flexible split) and Withdrawal-Limited Private Use Network routes: ERCOT Board Item 9.1 Batch Study Update, 13 April 2026, https://www.ercot.com/files/docs/2026/04/13/9.1-Batch-Study-Update.pdf ; ERCOT Trending Topic, New Batch Connection Process for Large Electricity Users, 18 June 2026, https://www.ercot.com/files/docs/2026/06/18/ERCOT-Trending-Topic-New-Batch-Connection-Process-for-Large-Electricity-Users.pdf ; PUCT approval of Batch Zero (PGRR145), 18 June 2026, https://www.ercot.com/files/docs/2026/06/22/145PGRR-130-PUCT-Report-061826.docx
- 75 MW threshold (PURA Sec. 37.0561(c)); curtailment protocol for loads interconnected after 31 December 2025 during firm load shed (Sec. 39.170(a)); competitive demand reduction from large loads (Sec. 39.170(b)); ERCOT may direct a large load to deploy on-site backup generation or curtail (Sec. 37.0561(e)): Texas Senate Bill 6, 89th Legislature, enrolled text, 2025. https://capitol.texas.gov/tlodocs/89R/billtext/html/SB00006F.htm
- Lead only, not cited for any figure: third-party YouTube video "State of AI data centres 2026", data to 5 October 2026 (research-build/source-ai-datacentre-video/TRANSCRIPT.md).

### Verification notes

- ercot.com and the PUCT Interchange block automated fetches (HTTP 403 and a Cloudflare challenge), so the ERCOT PDFs above were read through their indexed text in search results, not opened directly. Every ERCOT figure used is corroborated by a second source (Governor's release, POWER, Utility Dive). Tommy or the publish step should open the 29 July and 20 August ERCOT decks once in a browser to confirm.
- Not used, could not verify from primary material: PUCT Docket 59220 (reported 525.5 MW uncompensated curtailment condition on co-located data centres, decided 24 July 2026); the 9,456 MW "approved to energise" figure; the 194.3 or 191.8 GW Batch Zero classification figures (sources disagree).
- The pause covers data centres and crypto mining facilities of 75 MW or more. It is a pause on approvals to energise plus a pause on the Batch Zero study, not a stop on new applications.
