# Kairos Hermes 2 draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/kairos-signs-before-it-switches-on.md` (draft: true)
Cover: `public/covers/kairos-signs-before-it-switches-on.svg`
Drafted 29 October 2026, batch 3, Tier A item A12 (lead: smr-explained). Claim needs Tommy's approval before publish.
Checker: 0 failures, 0 warnings. Revised after fact-check 29 Oct 2026 (Unit 2 date, Kairos's counter-view, docketed falsifier, softer cover caption).

## Quality bar verdict: PASS, with the claim reframed

1. New mechanism. The outline said "TRISO fuel and molten salt systems, not construction, gate first power past 2030". Research showed that would mostly repeat the TerraPower draft (fuel, not permit) and could not rest on primary sources: Kairos has published nothing on Hermes 2 fuel supply, and its salt and pebble lines are running. What the primary record does show is new to the site: the buyer contract has run ahead of the licence. The NRC permits cover two 35 MWt non-power test reactors, issued under the research section of the Atomic Energy Act, due finished by 31 December 2027. The contract is for 50 MW from a single reactor, from 2030. That is the opposite of TerraPower (permit done, fuel missing) and distinct from Oklo (business model), Darlington (repetition) and Crane (grid place).
2. Primary sources: NRC permit CPTR-7 text, NRC project page, Federal Register notices, the statute, Kairos and Google releases. TVA's own pages were 403; TVA's position is taken from the joint release on kairospower.com and Google's blog.
3. What a PM learns: the "first Gen IV PPA" headline hides that the plant sold is not the plant permitted, the permit class carries a statutory cap on energy sales, and Unit 1's permit expires at end 2027 (Unit 2 end 2028) with excavation not yet started; Kairos says (press) no amendment is needed. The thing to watch is NRC docket 50-611/612, not the fuel market.

## Proposed claim (revised after fact-check, 29 Oct 2026)

Kairos Power's Hermes 2 contract has run ahead of an open licensing question: TVA is buying up to 50 MW from a single reactor from 2030, while the NRC's construction permits describe two 35 MWt non-power test reactors (70 MWt in all). Kairos says (press-reported) that the permits still cover a single reactor of about 125 MWt with no amendment; the NRC has not said, and will decide at the operating licence stage, under a licence class (section 104c research, with its 50 per cent energy-sales cap, or commercial) that is still open. So that review, not the contract, sets first power, and I expect TVA's first Hermes 2 power after 2030.

Kairos's counter-view, stated in the piece and labelled as trade press: in August 2025 Kairos told POWER magazine (repeated by ANS, 1 June 2026) that it reviewed the single 50 MWe / 125 MWt redesign, found the permit conditions "not substantively affected", that "an amendment is not required", and that it informed NRC staff; the design goes into a future operating licence application. PRESS ONLY; not independently read by the drafter (search did not surface the article), supplied by the fact-check.

### Alternatives considered

1. Outline claim: "Its TRISO fuel and molten-salt systems, not construction, gate first power to TVA past 2030." Rejected: collapses into the TerraPower fuel claim, and Kairos's fuel and salt facts are company PR, not evidence of a gate (pebble production is ahead; Hermes 2 HALEU source undisclosed, so cannot be shown binding either way). Fuel kept as one line and as the second falsifier.
2. "Kairos builds step by step, a non-power reactor first, so Hermes 1's slip to 2028 sets Hermes 2's date." Rejected as the lead: Kairos does not say Hermes 2 must wait for Hermes 1 to operate, so the dependency is inference. Kept as evidence of how first-of-a-kind dates move.
3. "A buyer committed before any electricity exists" (the brief's suggestion). Folded in: the cold open makes the point, but on its own it is a headline, not a mechanism.

## claims.ts entry

```ts
  {
    id: 'kairos-signs-before-it-switches-on',
    claim: 'Kairos Power has sold TVA up to 50 MW from a single Hermes 2 reactor from 2030, while its NRC construction permits describe two 35 MWt non-power test reactors. Kairos says the permits still cover the bigger reactor; the NRC will decide at the operating licence stage, under a licence class still open, so that review, not the contract, sets first power, and TVA\'s first Hermes 2 power arrives after 2030.',
    breaksIf: 'Hermes 2 delivers electricity to TVA\'s grid by 31 December 2030; or the NRC issues Hermes 2 an operating licence for the single reactor, under the existing construction permits, by 31 December 2029 and the plant still runs late for another reason, such as fuel or construction.',
    watch: ['Kairos\'s Hermes 2 operating licence application and the NRC\'s acceptance and review schedule (dockets 50-611 and 50-612)', 'Whether the NRC accepts the single reactor under the existing permits or requires an amendment', 'Which licence class Hermes 2 operates under: section 104c research or commercial', 'Requests to extend the permits\' completion dates (Unit 1 31 December 2027, Unit 2 31 December 2028)', 'A named HALEU source for Hermes 2\'s first core', 'Hermes 1 construction completion, expected by Kairos in 2028'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"), after the other nuclear pieces:
`pieces: [..., 'oklo-sells-the-electricity', 'terrapower-waits-on-the-fuel', 'kairos-signs-before-it-switches-on']`
Same wrinkle as TerraPower and Crane: Hermes 2 feeds TVA's grid, not a data centre fence, but the layer's `what` names small reactors and keeps the nuclear pieces together. If Tommy creates a nuclear or fuel layer for TerraPower and Eunice, this one belongs beside them.

## Glossary (heading: "Getting power to the building")

- `Construction permit`: The NRC's permission to build a reactor of the design described in the application. A separate operating licence is needed before it can run.
- `Test reactor (non-power)`: A reactor licensed for research and testing under section 104c of the Atomic Energy Act. The law caps how much of its running costs can go to selling energy.
- `Thermal and electrical megawatts`: A reactor's rating in heat (MWt) is larger than its output of electricity (MWe), because a steam plant turns well under half its heat into power.
Existing `PPA` and `HALEU` entries already fit.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '2 x 35 MWt', what: 'What the NRC permitted at Kairos Power\'s Hermes 2 site in Oak Ridge: two non-power test reactors of 35 thermal megawatts each sharing one power system, against the single reactor of up to 50 electrical megawatts sold to TVA.', piece: 'kairos-signs-before-it-switches-on', asOf: 'construction permits, 21 November 2024' },
```

## LinkedIn post (§9)

```
Kairos Power has sold the electricity from Hermes 2 to TVA, for Google's data centres. Its permit describes a smaller plant.

The NRC permitted two small research reactors at Oak Ridge. The contract is for up to 50 megawatts from one bigger reactor from 2030. Kairos says its permit still covers it; the regulator will decide when it reviews the licence to run the plant, and that review, not the contract, now sets the date.

The piece covers how a nuclear permit works, where the gap shows, and what would prove me wrong.

https://thephysicallayer.fyi/journal/kairos-signs-before-it-switches-on/

#NuclearEnergy #DataCentres #EnergyInfrastructure
```

## Sources (every figure)

- NRC, Construction Permit No. CPTR-7, Hermes 2 Test Reactor Facility Unit 1, Docket 50-611, issued 21 November 2024 (ML24324A021): https://www.nrc.gov/docs/ML2432/ML24324A021.pdf
  - Unit 2 permit CPTR-8 (ML24324A022): latest completion 31 December 2028, per the fact-check (the drafter got 403 and did not read it). The summary no longer gives a completion date.
  - Issued "pursuant to Sections 104c and 185a of the Act ... for a utilization facility ... useful in the conduct of research and development"; condition 3.A: "The earliest date for the completion of the construction of the facility is July 1, 2027, and the latest date for completion is December 31, 2027"; condition 3.C: "authorizes the applicant to construct a non-power test reactor facility described in the application"; para 5: permit "shall expire on the latest completion date". CPTR-8 (Unit 2, ML24324A022) returned 403 and was not read; the piece says "the plant's first unit".
- NRC, Hermes 2 project page (updated 15 September 2026): https://www.nrc.gov/reactors/non-power/new-facility-licensing/hermes2-kairos
  - Two test reactors, 35 MWth each; permits issued 21 November 2024; no amendment or operating licence application listed.
- Federal Register, 89 FR 94767, 29 November 2024, Hermes 2 construction permits CPTR-7 and CPTR-8: https://www.federalregister.gov/documents/2024/11/29/2024-28025/kairos-power-llc-hermes-2-test-reactor-facility-construction-permits
- Federal Register search for Kairos Hermes, 29 October 2026 (38 documents, newest first): no Hermes 2 amendment, extension or operating licence notice: https://www.federalregister.gov/api/v1/documents.json?conditions[term]=Kairos%20Hermes&order=newest
- 42 U.S.C. 2134(c)(3), Atomic Energy Act section 104c as amended by Public Law 118-67 (ADVANCE Act, July 2024): https://www.law.cornell.edu/uscode/text/42/2134
  - "(B) not more than 50 percent of the annual costs to the licensee of owning and operating the facility are devoted to the sale of energy" (and 75 per cent for energy plus non-energy services). The piece paraphrases (B).
- Federal Register, 91 FR 21335, 21 April 2026, Hermes test reactor EA and FONSI: https://www.govinfo.gov/content/pkg/FR-2026-04-21/html/2026-07700.htm
  - CPTR-6 amendment requested 24 March 2026; latest completion date from 31 December 2026 to 30 April 2029; Kairos "now expects construction to finish in 2028"; reasons: non-nuclear demonstrations of first-of-a-kind techniques and removal of legacy structures; safety-related construction began May 2025.
- Federal Register, 91 FR 28629, 18 May 2026, order extending Hermes completion date, issued 13 May 2026: https://www.federalregister.gov/documents/2026/05/18/2026-09880/in-the-matter-of-kairos-power-llc-hermes-test-reactor-extension-of-latest-date-for-completion-of
- Kairos Power, "Google, Kairos Power, TVA Collaborate to Meet America's Growing Energy Needs", 18 August 2025: https://www.kairospower.com/updates/google-kairos-power-tva-collaborate-to-meet-americas-growing-energy-needs
  - "up to 50 megawatts (MW) of reliable, 24/7 energy to the TVA grid"; "increase Hermes 2's output from 28 MW to 50 MW generated by a single reactor"; "scheduled to begin operations in 2030"; Google receives clean energy attributes for data centres in Montgomery County, Tennessee and Jackson County, Alabama. Binding status of the PPA not stated, so the piece does not call it binding. "First U.S. utility" is TVA's own description, attributed in the piece.
- Google, "Our first advanced nuclear reactor project with Kairos Power and Tennessee Valley Authority", 18 August 2025: https://blog.google/outreach-initiatives/sustainability/google-first-advanced-nuclear-reactor-project-with-kairos-power-and-tennessee-valley-authority/
- Kairos Power, "U.S. Department of Energy to Provide HALEU for Hermes Demonstration Reactor", 20 January 2026: https://www.kairospower.com/updates/u-s-department-of-energy-to-provide-haleu-for-hermes-demonstration-reactor (HALEU for Hermes 1 startup and operation; nothing on Hermes 2).
- POWER magazine, August 2025, and ANS Nuclear Newswire, 1 June 2026 (PRESS ONLY): Kairos's statement that the single 50 MWe, about 125 MWt reactor needs no permit amendment and that NRC staff were informed. The 125 MWt figure is press-only.
- Kairos Power and Samsung C&T release, 21 September 2026: https://www.kairospower.com/updates/kairos-power-and-samsung-c-t-agree-to-pursue-strategic-investment-and-collaboration-for-kp-fhr-deployment ("broke ground in Oak Ridge, Tennessee, in April 2026"; "grid-connected, 50 MWe reactor"; Samsung C&T to support power generation systems and balance of plant). Note Kairos says permits came "in December 2024"; the NRC record says 21 November 2024, which the piece uses.
- Kairos Power newsletter, "The Path to Deployment", 1 October 2026: https://kairospower.com/updates/the-path-to-deployment (crews removing legacy material "to prepare for excavation"; BWXT TRISO collaboration; no Hermes 2 dates).
- Kairos Power, Tennessee page: https://www.kairospower.com/locations/tennessee (Hermes "will pave the way for Hermes 2").
- Lead only, credited once in the sources line: Leo Cui, "Small Modular Reactors (SMR) Explained", YouTube (smr-explained transcript).

## Video figures: dropped or flagged

- "Hermes 2 is a 50 megawatt demonstration plant": CONFIRMED as "up to 50 MW" (Kairos release); the NRC permits are for 2 x 35 MWt, which is the point of the piece.
- "Construction began in April 2026": CONFIRMED as groundbreaking in April 2026 (Kairos, 21 September 2026). The 17 April date is PRESS ONLY (ANS, E&E News), not used. Note the NRC's Hermes 2 permit counts construction differently; Kairos's October newsletter says excavation had not begun.
- "An actual PPA for up to fifty megawatts": CONFIRMED (Kairos, Google).
- "Hermes 1 is a low-power test reactor that will not generate electricity": CONFIRMED (NRC CPTR-6 record, Kairos).
- Video's six criticality milestones, Army $2.2 billion, NuScale 72 modules: not about Kairos, not used.

## Could not verify / left out

- The October 2026 $643 million financing (including $275 million from DOE): PRESS ONLY (Bloomberg via Neutron Bytes, 16 October 2026; no Kairos release). Left out.
- Whether Kairos plans to stay under the section 104c research class or seek a commercial (section 103) licence: no primary statement. E&E News (April 2026, press) says Kairos expects approval to run it as a plant. The piece only states the statutory limit and that no request is on the public record.
- Whether Kairos has filed a Hermes 2 change that is not yet public: the NRC project page (15 September 2026) and Federal Register list none; ADAMS could not be searched directly (host unreachable) and two NRC PDFs returned 403, not bypassed. If an amendment request surfaces before publish, the evidence paragraph needs one line updated, but the claim survives (review still pending).
- Hermes 2 thermal rating for the single reactor: not disclosed. The piece argues only that 2 x 35 MWt cannot give 50 MWe, which holds for any steam cycle.
- TVA's own release and budget justification (tva.com) returned 403; not used.
