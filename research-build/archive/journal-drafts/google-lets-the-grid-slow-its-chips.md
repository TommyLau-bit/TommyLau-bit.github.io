# Google demand response draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/google-lets-the-grid-slow-its-chips.md` (draft: true)
Cover: `public/covers/google-lets-the-grid-slow-its-chips.svg`
Drafted 29 October 2026 from the approved Watch Later topic. Final claim wording needs Tommy's approval before publish.

## Proposed claim (revised after fact-check, 29 Oct 2026)

The AI chip is becoming the quickest spare power a stressed grid can add, with no new hardware: Google already lets utilities limit or shift its machine learning work at peak, and by 31 December 2027 a US utility or grid operator will publicly approve a data centre connection of 100 MW or more whose peak cut is stated to come from slowing or deferring computing, with no battery or generator counted towards it.

"Cheapest" was dropped: nothing public compares costs.

Test definitions: "publicly approved" means an order, tariff, filed agreement or operator rule. The cut must be stated in that record to come from computing. A utility backstop right to trip the site if the software fails does not disqualify it (so a Silicon Valley Power style breaker held in reserve is allowed); a cut delivered by the utility opening the switch does not count.

Has it already happened? Checked Google's five 1 GW utilities:
- I&M (IURC Cause 46276, April 2026): approved, but the cut size and how it is delivered are confidential; a consumer witness called it "a small percentage of the facility's total load". Does not meet the test.
- DTE (MPSC Case U-22058, approved 1 October 2026 per MPSC release, page 403 to me, confirmed via search snippet): 1 GW Google site in Van Buren Township; DTE's 28 Sep 2026 8-K says the load ramp is "supported by up to 1,600 MW of renewable generation, 480 MW of energy storage and 350 MW of demand response". This is the closest near-miss. It is a supply-side (resource adequacy) role, not a connection condition, and no public record found says the 350 MW is delivered by computing rather than backup generation. Does not meet the test as worded, but FLAG FOR TOMMY: if he reads DTE as meeting it, the claim is already confirmed and needs reframing. https://www.sec.gov/Archives/edgar/data/936340/000093634026000159/dtebusinessupdate92826fi.htm
- Entergy Arkansas (APSC, West Memphis, 2025): approved with Google saying it intends to integrate load flexibility; no public curtailment terms found. Does not meet it.
- Minnesota Power (Hermantown ESA, filed April 2026): only "explore" demand flexibility; no approval found. Does not meet it.
- TVA: no public filing with terms found.

### Alternatives considered

1. "Google's 1 GW of demand response is worth more to it than the electricity it saves, because it buys earlier connections." Rejected: connection dates and contract values are not disclosed, so it cannot be tested.
2. "Grid operators will create a non-firm large-load service by end-2027 because of FERC's June 2026 show cause orders." Rejected as the lead: about the regulator, not Google, and SPP's CHILLS (accepted 5 June 2026) arguably already is that. Kept as one line of evidence.

Line from neighbouring pieces: ercot-rations-the-plug (now linked, it goes live 2 Nov) is the grid cutting the plug or the site bringing its own power; the-power-it-drops is accidental trips and ride-through; what-the-battery-is-really-for is the battery as connection equipment. This piece is the chip's own slowdown as the counted resource.

## claims.ts entry

```ts
  {
    id: 'google-lets-the-grid-slow-its-chips',
    claim: 'The AI chip is becoming the quickest spare power a stressed grid can add, with no new hardware: Google already lets utilities limit or shift its machine learning work at peak, and a utility will soon connect a large data centre that counts on such a cut.',
    breaksIf: 'By 31 December 2027 no US utility or grid operator has publicly approved, by order, tariff, filed agreement or operator rule, a data centre connection of 100 MW or more whose peak cut is stated to come from slowing or deferring computing, with no battery or on-site generator counted towards it. A utility backstop right to trip the site if the software fails is allowed; a cut delivered by the utility opening the switch is not.',
    watch: ['New Google demand response contracts and whether their filings say how the cut is delivered', 'How DTE delivers the 350 MW of demand response tied to Google\'s Van Buren site', 'RTO responses to FERC\'s 18 June 2026 show cause orders on flexible large loads', 'SPP\'s conditional high impact large load service in use', 'Silicon Valley Power\'s Emerald AI pilot and Nvidia\'s Aurora site in Manassas'],
  },
```

## stack.ts

Layer `grid` ("The grid connection"). The piece is about the terms on which a site connects, so it sits beside the-power-it-drops and pjm-sends-the-bill (and ercot-rations-the-plug when that publishes):
`pieces: [..., 'the-power-it-drops', 'pjm-sends-the-bill', 'google-lets-the-grid-slow-its-chips']`
No new layer needed.

## Glossary (heading: "Getting power to the building")

- `Demand response`: An agreement to use less electricity when the grid asks, usually at peak, in return for payment or bill credits. Google's version slows or delays its AI computing rather than switching the building off.
- `Flexible large load`: FERC's term (June 2026) for a large site, not paired with its own generation, that is willing and able to limit how much it draws from the grid under certain conditions.
- `Power capping`: Software that limits how much power a chip may draw, so it runs slower and cooler for a while.

## numbers.ts (physical figures only)

```ts
  { layer: 'grid', value: '1 GW', what: 'Data centre demand Google has written into US utility contracts as demand response, met by limiting or shifting machine learning work.', piece: 'google-lets-the-grid-slow-its-chips', asOf: '19 March 2026' },
```

Optional: `{ layer: 'grid', value: '25% for 3 hours', what: 'Power cut on a 256-GPU AI cluster in Phoenix by software alone, with no battery, while agreed performance held.', piece: 'google-lets-the-grid-slow-its-chips', asOf: 'Nature Energy, published online 5 December 2025' }`

## LinkedIn post (§9)

```
Google now lets five American utilities ask it to hold back its AI computing when the grid is stretched.

It says the deals cover one gigawatt of data centre demand. The work is delayed rather than lost, so the energy moves in time instead of disappearing. If grids start counting that promise when they connect new sites, the AI chip becomes the quickest spare power a crowded network can add, with no battery or generator needed.

The piece covers how slowing a chip frees up a grid, what the tests and regulators show, and what would prove me wrong.

https://thephysicallayer.fyi/journal/google-lets-the-grid-slow-its-chips/

#DataCentres #Grid #Energy
```

## Figures in the body and their sources

- August 2025 deals announced (I&M filed the signed contract on 30 July 2025 per the IURC order) with Indiana Michigan Power and TVA, "first time" demand response targeting ML workloads, Fort Wayne site: Google, Michael Terrell, "How we're making data centers more flexible to benefit power grids", 4 August 2025. https://blog.google/inside-google/infrastructure/how-were-making-data-centers-more-flexible-to-benefit-power-grids/
- 1 GW across five utilities (I&M, TVA, Entergy Arkansas, Minnesota Power, DTE Energy); "limit or shift a portion of machine learning (ML) workloads"; "a key resource for new data centers to connect more rapidly": Google, "Google signed 1 GW of data center demand response", 19 March 2026. https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/demand-response-data-center-milestone/
- Credits for demand response participation (I&M witness Loveman), compliance standards and curtailment parameters (Commission finding), a penalty structure the Commission found adequate (the per-event-failure wording is a consumer witness's testimony, not a finding), terms confidential, intervenor testimony that the cut is "a small percentage of the facility's total load": Indiana Utility Regulatory Commission, order in Cause No. 46276 (filename dated 29 April 2026; approval date not legible in the text layer, so the piece says "April 2026"). https://secure.in.gov/iurc/files/ord_46276_042926.pdf ; I&M filed the contract on 30 July 2025 (press: T&D World, https://www.tdworld.com/distributed-energy-resources/demand-side-management/news/55307981/im-and-google-submit-joint-contract-proposal-focused-on-demand-response-for-data-center-operations)
- 256 GPUs, 25 per cent for three hours at peak, Phoenix, no hardware modification or energy storage: Colangelo, Coskun et al., "AI data centres as grid-interactive assets", Nature Energy, published online 5 December 2025 (vol. 11, Feb 2026, pp. 254 to 261), https://www.nature.com/articles/s41560-025-01927-1 (page sits behind a login redirect; title, journal and date confirmed from nature.com's index); preprint with the same figures, arXiv:2507.00909, 1 July 2025, https://arxiv.org/abs/2507.00909
- Oracle Cloud Infrastructure as host, Nvidia (A100) GPUs, Salt River Project as utility, EPRI DCFlex: Nvidia blog, 1 July 2025, https://blogs.nvidia.com/blog/ai-factories-flexible-power-use/ (read via a copy of the post; the arXiv abstract itself names neither Oracle nor Nvidia)
- 18 June 2026, six show cause orders, one to each RTO/ISO FERC oversees (ERCOT is outside FERC's reach), (PJM EL26-67, SPP EL26-68, NYISO EL26-69, MISO EL26-70, CAISO EL26-71, ISO-NE EL26-72) to justify or reform large-load rules; PJM order says the tariff "appears to be unjust and unreasonable" and preliminarily finds it lacks "transmission services that reflect ... flexible large loads that are willing and able to limit their use of the transmission system": FERC, 195 FERC ¶ 61,211, https://www.ferc.gov/sites/default/files/2026-06/EL26-67-000.pdf ; staff presentation https://www.ferc.gov/sites/default/files/2026-06/E-7%20to%20E-12%20SCO%20Presentation%20-%20June%20CM.pdf
- AI Energy Management Alliance, 16 September 2026, founders Emerald AI, Google, Nvidia, asks for "faster, risk-adjusted interconnection pathways" for "credible, verifiable flexibility commitments", technology-neutral and performance-based: Nvidia blog, https://blogs.nvidia.com/blog/ai-energy-management-alliance/
- Lead only, not cited for any figure: Leo Cui, "NVIDIA and Google give AI Data Centers a Dimmer Switch", YouTube, https://www.youtube.com/watch?v=q5JflUbObe8 (research-build/source-watch-later/nvidia-google-dimmer-switch/TRANSCRIPT.md)

## Context checked, not used in the body

- Silicon Valley Power and Emerald AI pilot in Santa Clara, announced 21 April 2026; press reports SVP's COO calling utility control of the load-side breaker "non-negotiable" (press only: Latitude Media, Implicator). Relevant to the second falsifier. https://www.latitudemedia.com/industry-news/silicon-valley-power-and-emerald-ai-launch-pilot-to-demonstrate-flexible-data-centers-in-santa-clara/
- Nvidia's Aurora, a 96 MW power-flexible AI factory in Manassas with Digital Realty, Emerald AI, EPRI and PJM, announced 29 October 2025; opening not confirmed (press only). A public connection approval there could satisfy the claim.
- SPP's conditional high impact large load service (CHILLS), accepted by FERC on 5 June 2026 per the June show cause orders: a non-firm service, but not specific to how the cut is delivered.
- Google and Voltus 1 GW virtual power plant in PJM, 22 October 2026: batteries and thermostats, a different mechanism, left out.
- Naming trap: "AEMA" in FERC's June orders (ANOPR comments of 21 November 2025) is the Advanced Energy Management Alliance, an older demand response trade group, not the AI Energy Management Alliance launched in September 2026. Do not conflate.

## Video figures dropped or flagged

- 25% for three hours (Phoenix): VERIFIED in Nature Energy and arXiv; used alone.
- "Up to 40%", "30% in roughly 30 seconds", "up to 10 hours", 96 Blackwell Ultra GPUs, 200+ events over five days (London, National Grid, Nebius, EPRI, Dec 2025, announced 3 March 2026): VERIFIED in National Grid's press release (https://nationalgrid-newsroom.prgloo.com/news/uk-first-trial-of-ai-grid-technology-successfully-demonstrates-the-ability-of-data-centres-to-adjust-power-needs) but DROPPED from the body for the numbers budget and so they are never set beside the Phoenix figure. They come from different tests and must never be combined.
- "Published in Nature Energy": VERIFIED (Nature Energy, online 5 December 2025).
- FERC "in June 2026 directed all six regional grid operators to justify or reform their rules": VERIFIED as the 18 June 2026 show cause orders. Distinct from the 1 June 2026 Eddystone order cited in constellation-restarts-the-reactor.
- AEMA launched 16 September 2026: VERIFIED on Nvidia's blog. Launch partner count (18 or 20 in press) DROPPED, conflicting and not on the primary page.
- 500 MW campus equal to 420,000 homes: DROPPED, illustrative and not sourced.
- The 100/60/30/85 units example and the three job types: the video's own illustration, not reused.
