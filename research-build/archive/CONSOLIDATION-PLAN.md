# Journal consolidation plan (approved by Tommy, 30 Oct 2026)

Corpus today: 61 pieces = 33 live + 28 drafts (20 scheduled to 18 Jan, 8 held), plus 19 live research notes, each resting on one live piece's claim.

## Proposed merged pieces (61 become 11)

| # | Cluster (map layer) | Merged deep piece (working title) | Absorbs | Depth added below the plain-English top |
|---|---|---|---|---|
| 1 | Grid connection, Southeast Asia (grid) | Johor and Singapore: the plug, not the chip | the-queue-not-the-chip, two-governments-one-confession, the-part-money-cannot-hurry, singapore-cannot-wait-for-the-cable, singapore-licenses-the-old-halls, johor-plugs-in-before-it-fills; held: johor-waits-on-the-treatment-plant, malaysia-keeps-the-wires-shared | Tenaga booked vs drawn load series, Green Lane timings, EMA import and gas plan, DC-CFA2 and the licence law, water margin (SPAN), tariff structure; Tommy's APAC flagship and the answer to SemiAnalysis's power vs chip framing |
| 2 | Grid connection, US rules (grid) | America rations the plug: ERCOT, FERC and PJM | ercot-rations-the-plug, ferc-asks-for-a-softer-plug, pjm-sends-the-bill, google-lets-the-grid-slow-its-chips, the-power-it-drops; held: virginia-bills-the-empty-site | Queue sizes, the service-tier menu by RTO, capacity prices, ride-through rules, chip-level demand response; one table of who pays and who can be cut |
| 3 | Grid equipment queue (grid / distribution) | The equipment queue: transformers and switchgear | siemens-energy-measures-the-shortage, hitachi-energy-plans-the-queue, eaton-order-book-outruns-it, schneider-sells-the-finished-system | Backlog-to-revenue (years of work) for each maker side by side, factory additions and dates; links to 4 research notes |
| 4 | Power on site: gas (onsite + new fuel layer) | Building your own power: turbines, blades and gas | ge-vernova-sells-the-wait, the-way-out-has-its-own-queue, the-product-is-time, homer-city-inherits-the-air, hyperion-the-plant-outlasts-the-lease, permian-gas-follows-the-oil-rig; held: howmet-casts-the-queue, crusoe-borrows-the-jet-engine, golden-pass-joins-the-gas-queue | Turbine slots and output steps, aeroderivative vs heavy frame, air permits (netting), utility-built plants, fuel supply; links to GE Vernova and Bloom notes |
| 5 | Nuclear (onsite) | Nuclear for AI: restarts first, new reactors later | constellation-restarts-the-reactor, palisades-waits-on-the-reactor, oklo-sells-the-electricity, terrapower-waits-on-the-fuel, kairos-signs-before-it-switches-on, eunice-cannot-fill-the-gap; held: constellation-squeezes-the-reactors, darlington-builds-on-the-old-plug | A dated ladder (restart, uprate, SMR, advanced) with each gate (grid place, reactor, permit, fuel); enrichment supply table; links to Constellation and Oklo notes |
| 6 | Batteries and flexibility (onsite) | What the battery is for, grid by grid | what-the-battery-is-really-for, california-still-shifts-the-sun | CAISO count, PJM accreditation, connection-equipment use; the counter-case stated openly |
| 7 | Inside the building (distribution) | Powering the rack: from 54 V to 800 V | every-megawatt-got-harder, the-rack-runs-out-of-copper, ti-feeds-the-chip | Content per MW, 800 VDC phases, power chips; links to Vertiv and TI notes |
| 8 | Cooling and water (cooling) | Heat and water decide where AI goes | cooling-is-half-the-job, room-to-spare, water-is-a-siting-problem | PUE and WUE, liquid cooling share, siting cases |
| 9 | The network (network) | How ten thousand chips talk: copper, glass, lasers and mirrors | ten-thousand-chips-one-thought, marvell-collects-the-toll, broadcom-wins-either-way, corning-lays-the-glass, lumentum-makes-the-light, the-optics-you-cannot-unplug, google-steers-the-light, fairwater-spans-two-states | Layer-by-layer bill of materials (switch, DSP, laser, fibre, OCS), scale-up vs scale-out vs scale-across; links to 4 notes |
| 10 | Chips and memory (chips / memory) | The chip supply chain's slow parts | nobody-makes-a-b200-alone, the-two-seconds-after-you-hit-send, tsmc-says-it-is-the-bottleneck, asml-booked-ahead, ajinomoto-grows-with-the-package, the-countertop-is-the-bottleneck, micron-three-times-the-wafer, seagate-sells-the-terabyte | Lead times per step (EUV, CoWoS, substrate film, HBM wafers, drives); links to TSMC, ASML, Ajinomoto, Micron notes |
| 11 | Who runs the capacity (operators) | Contracted, energised, running: how campuses really arrive | nebius-paid-for-what-is-switched-on, power-first-chips-last, abilene-switched-on-in-stages | Stage ladder with Abilene, Nebius, Jane Street; link to Nebius note |

## How old URLs, claims and notes survive
- Every old URL redirects to its section in the merged piece (/journal/<merged>/#<old-slug>). LinkedIn posts already scheduled (to 4 Dec) keep working.
- Every claim in claims.ts stays word for word, with its original date and falsifier. The merged piece carries each one in a dated "Claims on record" block. claims.ts needs one new field (which piece it now lives in); check-piece.py, check-call.py and the claims page need small code changes.
- The 19 research notes stay as they are; their `claims` keep pointing at the same claim ids.
- Rules this breaks, which need Tommy's explicit sign-off in CLAUDE.md / WRITING-FORMAT.md: "pieces are never edited" (originals become sections, kept verbatim in an archive or in the claim block), the 450 to 600 word and 15-figure budgets (§3, §4b, set 8 to 9 Oct), and "explanation in the journal, numbers in the research".

## Scheduled tasks
Recommend pausing all 20 remaining publish tasks (first: ERCOT, 2 Nov) until the plan is approved; their drafts become sections of the merged pieces. Do not pause without Tommy's go.

## Homepage
Already shipped on 29 Oct (commit 06de973). Pausing means leaving it as is, or reverting to the flat grid; with 11 pieces, a layer layout may still fit.
