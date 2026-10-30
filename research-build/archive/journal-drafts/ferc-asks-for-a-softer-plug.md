# FERC large-load show cause orders draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/ferc-asks-for-a-softer-plug.md` (draft: true)
Cover: `public/covers/ferc-asks-for-a-softer-plug.svg`
Drafted 29 October 2026 (batch 3, Tier A item A3). The claim wording needs Tommy's approval before publish.

## Quality bar (CLAUDE.md, 29 Oct 2026), revised after fact-check

1. New mechanism. The centre is the federal menu of service tiers: FERC is splitting "a connection" into a firm tier that still waits for network upgrades and a lower interim non-firm tier that switches on sooner, can be cut first, and converts to firm when upgrades finish. In PJM the lower tier carries no capacity: under terms PJM's transmission owners set out (notice of 9 Oct 2026), no capacity is procured and no capacity charges assessed for an Interim NITS customer until its upgrades are in service. Distinct from ercot-rations-the-plug (one state grid outside FERC rationing access; no tiered tariff product, no capacity link) and from google-lets-the-grid-slow-its-chips (the chip as the flexible resource; the orders were one line of evidence there).
2. Primary sources: FERC orders, FERC abeyance orders, PJM motion and workshop deck, PJM TO notice, ISO-NE joint motion, FERC's NYISO abeyance order, CAISO straw proposal. MISO and SPP plans are described in the piece as "reported" (counsel memo; their motions were not found on misoenergy.org or spp.org by search; FERC Federal Register notices confirm both filed abeyance motions on 3 August 2026).
3. Beyond the headline: the lower tier is outside PJM capacity procurement; filings land 16 to 20 November 2026; CAISO's record says developers want firm and take flexibility only temporarily.

## Proposed claim

FERC's June 2026 orders are splitting the grid connection into tiers rather than speeding up the firm one: by the end of 2027, data centres of 50 MW or more will be running on interim non-firm service in at least two of the six regions FERC oversees, and in PJM that interim load will carry no capacity until its upgrades are built.

### Alternatives considered

1. "Fewer than four of six RTOs will have a FERC-accepted non-firm service by end-2027" (the first draft). Dropped after fact-check: too easy, SPP already passes and five of six have proposed one.
2. "Firm study-to-service times for large loads will not fall in any RTO by end-2027." Not observable: no common published firm-service lead time across six RTOs.

Chosen because it tests use, not paperwork (a real site energised on the lower tier, which can go either way given CAISO's evidence that developers want firm), and the PJM capacity leg could fail if consumer advocates persuade FERC that interim load must be capacity-backed.

## claims.ts entry

```ts
  {
    id: 'ferc-asks-for-a-softer-plug',
    claim: 'FERC\'s June 2026 orders are splitting the grid connection into tiers rather than speeding up the firm one: by the end of 2027, data centres of 50 megawatts or more will be running on interim non-firm service in at least two of the six regions FERC oversees, and in PJM that interim load will carry no capacity until its upgrades are built.',
    breaksIf: 'By 31 December 2027, fewer than two of PJM, MISO, SPP, NYISO, ISO-NE and CAISO have a large load of 50 MW or more actually energised under an interim non-firm transmission service (shown in a service agreement filed at FERC or the operator\'s own report); or FERC requires PJM to procure capacity for interim non-firm large loads.',
    watch: ['RTO and transmission owner Section 205 filings due 16 to 20 November 2026 in EL26-67 to EL26-72, and FERC\'s orders on them in 2027', 'Service agreements for Interim NITS, CHILLS, CAISO FILI and NYISO non-firm service filed at FERC', 'PJM Interim NITS rate (ER26-3537) and whether capacity stays unprocured for interim customers', 'Protests by consumer advocates on capacity for interim load'],
  },
```

## stack.ts

Layer `grid` ("The grid connection"), after `pjm-sends-the-bill` (and after `ercot-rations-the-plug` if that publishes first). No new layer needed.

## Glossary (heading: "Getting power to the building")

- `FERC` already exists. No change.
- `Firm service` (proposed by the ERCOT sidecar; add once): A connection the grid operator plans to keep supplied at all times, without a right to cut it short of an emergency.
- `Non-firm service`: Transmission service the grid may cut first when lines are strained, offered so a site can switch on before the upgrades for firm service are built.
- `Network upgrades`: The new lines, substations and equipment a grid operator says it must build before it can give a new site firm service.
- `Show cause order`: A FERC order telling a utility or grid operator to explain why its rules are still just and reasonable, or to propose changes.
- `Large load (FERC)`: In FERC's June 2026 orders, a suggested definition of a new site of 50 megawatts or more connected above 69 kilovolts, not paired with its own generation.

## numbers.ts (physical figures only)

None essential. Optional: `{ layer: 'grid', value: '50 MW', what: 'The size above which FERC suggests a new site connected above 69 kilovolts counts as a large load, in its June 2026 orders to the six regional grid operators.', piece: 'ferc-asks-for-a-softer-plug', asOf: '18 June 2026' }`

## LinkedIn post (§9)

```
FERC asked America's regional grids to connect data centres faster, and what is coming back is a connection sold in two tiers.

The top tier still waits years for new wires. The lower tier switches on sooner but can be cut first, and in PJM no capacity is bought for it until the wires arrive. California's operator says developers still want firm power, so whether anyone actually runs on the lower tier is the real test.

The piece covers how FERC's menu works, what the operators have filed, and what would prove me wrong.

https://thephysicallayer.fyi/journal/ferc-asks-for-a-softer-plug/

#DataCentres #Grid #Energy
```

## Sources, one per line (figure: source, date)

- 18 June 2026, six show cause orders under FPA section 206; tariffs "appear to be unjust and unreasonable"; PJM order asks whether tariff is just and reasonable without "(1) an interim non-firm network transmission service while Network Upgrades are being constructed (i.e., interim NITS) and (2) permanent firm and non-firm contract demand transmission services"; suggested large load definition 50 MW or greater, above 69 kV, not co-located (n.2 and P 58). This definition is the PJM order's only; SPP's order uses SPP's own HILL definition (10 MW at or below 69 kV, or 50 MW above), so the piece says "In its PJM order": FERC, PJM Interconnection, L.L.C., 195 FERC ¶ 61,211, Docket EL26-67-000, https://www.ferc.gov/sites/default/files/2026-06/EL26-67-000.pdf
- Other orders: SPP EL26-68 https://www.ferc.gov/sites/default/files/2026-06/EL26-68-000.pdf ; NYISO EL26-69 https://www.ferc.gov/sites/default/files/2026-06/EL26-69-000.pdf ; MISO EL26-70 https://www.ferc.gov/sites/default/files/2026-06/EL26-70-000.pdf ; CAISO EL26-71 (195 FERC ¶ 61,214) https://www.ferc.gov/sites/default/files/2026-06/EL26-71-000.pdf ; ISO-NE EL26-72 (195 FERC ¶ 61,215; the ferc.gov URL on the same pattern returned "page not found", cited from FERC's own abeyance order below).
- Five categories of reform, 60-day response, 45-day abeyance window, 200 million Americans in over 30 states (not used in piece): FERC staff presentation, Items E-7 to E-12, 18 June 2026, https://www.ferc.gov/sites/default/files/2026-06/E-7%20to%20E-12%20SCO%20Presentation%20-%20June%20CM.pdf
- SPP CHILLS accepted 5 June 2026, non-firm, as available, subject to curtailment and interruption, maximum term seven years: described in the SPP show cause order, EL26-68-000, P 17 (citing Sw. Power Pool, Inc., 195 FERC ¶ 61,196).
- PJM motion for 90-day abeyance from 17 August 2026, Section 205 filing "by early to mid-November": PJM, Docket EL26-67-000, filed 27/28 July 2026, https://www.pjm.com/-/media/DotCom/documents/other-fed-state/20260728-el26-67-000.pdf
- FERC granted abeyance, ISO-NE, 14 August 2026, 196 FERC ¶ 61,132: https://www.iso-ne.com/static-assets/documents/100038/el26-72-000_abeyance.pdf
- FERC granted abeyance, NYISO, 14 August 2026, 196 FERC ¶ 61,130: https://www.nysrc.org/wp-content/uploads/2026/08/Att-3-NYISO-Show-Cause-Order-Abeyance-8-14-2026-20260814-3068_EL26-69-000.pdf
- FERC granted abeyance, PJM, 14 August 2026, 196 FERC ¶ 61,129 (motions of PJM, Indicated PJM TOs and Silver Run; PJM to file by early/mid-November, TOs by 16 November): https://www.pjm.com/-/media/DotCom/documents/ferc/orders/2026/20260814-el26-67-000.pdf
- MISO and SPP abeyance motions filed 3 August 2026: FERC notices, https://public-inspection.federalregister.gov/2026-16167.pdf and https://public-inspection.federalregister.gov/2026-16174.pdf . Grants for MISO, SPP and CAISO not confirmed; the piece no longer states a pause or a 20 November date.
- PJM Transmission Owners' notice to the Members Committee, 9 October 2026 (posted for 28 October MC): PJM intends to offer large loads the three co-located load services (Firm Contract Demand, Non-Firm Contract Demand, Interim NITS) plus proposed Fractional NITS (firm, based on available capacity, pending upgrades); Interim NITS is "a temporary, non-firm transmission service"; "capacity will not be procured on behalf of Interim NITS customers and generation capacity charges will not be assessed until such time as the Network Upgrades are in place"; Interim NITS rate filed 17 August 2026 in ER26-3537-000 (the rate only; the no-capacity terms are from this notice, so the piece says "under terms PJM's transmission owners set out"); cost recovery agreement term of 10 to 20 years under consideration: https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20261028/20261028-notice-of-pjm-transmission-owners-consultation-with-the-members-committee---informational-posting-only.pdf
- PJM conceptual approach, Co-Located Load Order Workshop, 30 July 2026: New Services Request process cut to about 12 months; non-firm NITS "controllable under operational procedure", "similar to energy only generation": https://www.pjm.com/-/media/DotCom/committees-groups/workshops/cllsco/2026/20260730/20260730-item-03---show-cause-for-large-loads-conceptual-approach---presentation.pdf
- CAISO Large Loads straw proposal, 11 August 2026, pp. 38 to 39: Flexible Interim Load Interconnection (FILI) "until network upgrades are complete, at which time the large load would switch over to receiving firm service" and permanent FLIP; "developers consistently express that they are only interested in acquiring firm service and would only agree to be flexible temporarily": https://stakeholdercenter.caiso.com/InitiativeDocuments/Large-loads-Straw-Proposal-Aug-11-2026.pdf
- MISO (non-firm large load service, firm step-up option, filings by 16 November), NYISO (firm and non-firm variants of financial reservation service, filing 16 November), ISO-NE (interim and permanent flexible load service, filing 16 November), SPP (PALS non-firm service and CHILLS enhancements, 95-day abeyance to 20 November), CAISO (filing 16 November): NEPOOL Counsel (Day Pitney) memorandum summarising the six abeyance motions, 3 August 2026, posted by ISO-NE: https://www.iso-ne.com/static-assets/documents/100038/nepool_counsel_memo_motion_for_abeyance.pdf . FLAG: a stakeholder counsel summary. Used in the piece ONLY for MISO and SPP, worded "are reported to include". ISO-NE confirmed from its own joint motion ("interim non-firm network transmission service" and non-firm contract level service): https://www.iso-ne.com/static-assets/documents/100038/joint_motion_for_abeyance_iso-ne_and_pto_ac.pdf . NYISO confirmed from FERC's abeyance order, 196 FERC ¶ 61,130 ("design firm and non-firm transmission services for transmission customers serving large loads").

## Video figures dropped or flagged

Lead: "NVIDIA and Google give AI Data Centers a Dimmer Switch", Leo Cui, https://www.youtube.com/watch?v=q5JflUbObe8 . Credited once in the sources line.
- "In June 2026, federal regulators directed all six regional grid operators to justify or reform their rules": VERIFIED (18 June 2026 orders). The only video fact this piece relies on, and only as the lead.
- 500 MW campus, 420,000 homes, the 100-unit worked example: dropped (illustrative, not about FERC).
- Phoenix 256 GPUs and 25 per cent, London 96 Blackwell Ultra GPUs, up to 40 per cent, about 30 per cent in 30 seconds, AEMA launch 16 September: dropped (covered by google-lets-the-grid-slow-its-chips, and not about FERC).
- The UNCAPPED-RESULTS outline's "compliance filings due within 60 days" is out of date: all six sought abeyance, so the substantive filings are due 16 to 20 November 2026, not August. PJM's 17 August filing was a partial compliance filing in the separate co-located load docket (EL25-49; ER26-3537 for the TOs' Interim NITS rate).
- "PJM's non-capacity-backed load proposals" (named in my instructions): not used by that name. PJM's 2025 non-capacity-backed load idea was not traced to a current filing; the live equivalent is Interim NITS with no capacity procured, sourced above.
