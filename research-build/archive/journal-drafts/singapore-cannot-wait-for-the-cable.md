# Singapore import cables draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/singapore-cannot-wait-for-the-cable.md` (draft: true)
Cover: `public/covers/singapore-cannot-wait-for-the-cable.svg`
Drafted 29 October 2026 from the Watch Later batch. The claim needs Tommy's approval before publish.

## Fact-check corrections applied (29 October 2026)

- Existing imports: imports have flowed since 23 June 2022 under the LTMS-PIP over existing interconnections (up to 100 MW, then up to 200 MW, licence extended to 2026; EMA, 20 September 2024, per the fact-check), and Keppel holds EMA's first Electricity Importer Licence for it. I did not open that page myself, so the piece says only that a little power already arrives over the existing link to Malaysia, rated up to 1 GW (EMA, 26 October 2026), and that all 13 new projects are conditional. "Only approved on paper" in the summary is now "only conditionally approved".
- Five-year plan: the piece now says five gas plants add about a quarter to generating capacity by 2031 (EMA: about 26% from about 12 GW), and names the landing sites and the second Malaysia link studies (up to 2 GW by 2030). The word "mainly" is gone.
- DC-CFA2: "such as" list, so imports are "not mentioned", not excluded. The rule was at least 50% and the winners chose to exceed it. "Burnt" is replaced by "used". "Cannot wait for the cable" is presented as my reading, and the piece says neither agency gives a reason.
- Claim and falsifier now share one window: no delivery before 1 January 2029. The falsifier says which power counts.
- The lead is called a Straits Times video, not an interview. The cable factory and ship scarcity line is cut. "From 2028" is kept: I opened EMA's 5 September 2024 page, which says the five licensees aim for commercial operations "from 2028". The 1.3 GW Sembcorp approval and its 2035 date are kept: I opened the 26 October 2026 PDF.
- Cover label changed from "NOT LAID YET" to "NEW CABLES: 2029 AT THE EARLIEST".

## Why the claim changed from the outline (read this first)

The outline was "Singapore ties new data centre capacity to green power it does not yet have, so it is really waiting on import cables". The primary sources do not support that. The DC-CFA2 rules (EDB and IMDA fact sheet, 1 December 2025) list the eligible green pathways as biomethane, low-carbon ammonia, low-carbon hydrogen, novel fuel cells with carbon capture, and vertical or building-applied solar. Imported electricity is not named. The award fact sheet (21 August 2026) repeats the same list and puts all four sites on Jurong Island. So the data centres are deliberately not waiting on the cable.

The honest reframe keeps the subject and the mechanism (no land, so green power must come by subsea cable on a slow equipment clock) and flips the conclusion: Singapore cannot wait for the cable, so it told data centres to make green power at home. EMA's own five-year plan (26 October 2026) backs this: demand to 2031 is met mainly by five new gas plants, and for imports it only commits to developing landing sites. The suggested slug `singapore-waits-on-the-cable` would now mislead, so the slug is `singapore-cannot-wait-for-the-cable`.

Caveat: the DC-CFA2 list says "such as", so it is not formally exhaustive. The piece says imports are "not on the list", which is accurate.

## Proposed claim

Singapore's 13 conditionally approved low-carbon import projects, its main route to future green power, will not deliver power into Singapore before 1 January 2029, so the green power it named for new data centre capacity is made on the island, from clean fuels and solar, rather than imported. That this is why imports were left out is my reading; EDB and IMDA give no reason.

### Alternatives considered

1. No DC-CFA2 award is supplied through an Indonesian import cable before 2029 (the outline's test). Rejected: true but trivially so, since DC-CFA2 never allowed imports as a pathway. It would test nothing.
2. Singapore's next megawatts to 2031 come by gas, not by cable (EMA five-year plan). Rejected as the lead: strong evidence, but it is a gas-supply story and drifts from the data centre subject. Kept as the second piece of evidence.

Chosen because it is what the primary sources show, it keeps the data centre call as the subject, it extends two-governments-one-confession (rationing) and the-part-money-cannot-hurry (the equipment clock) to a new physical object, the subsea cable, and it has two dated, observable falsifiers.

## claims.ts entry

```ts
  {
    id: 'singapore-cannot-wait-for-the-cable',
    claim: 'Singapore\'s conditionally approved low-carbon import projects, its main route to future green power, will not deliver power into Singapore before 1 January 2029, so the green power it named for new data centre capacity is made on the island, from clean fuels and solar, rather than imported.',
    breaksIf: 'Any of the conditionally approved import projects (the 13 counted by EMA on 7 August 2026, or any approved since) delivers power into Singapore before 1 January 2029, over a new cable or a second Malaysia interconnector, or EDB and IMDA\'s next data centre call lets newly imported electricity count towards its green energy share. Power over the existing Malaysia link under older schemes such as LTMS-PIP does not count.',
    watch: ['The first Electricity Importer Licence EMA issues to one of the conditional projects', 'Commercial operation of the first conditional project against the 2028 and 2029 dates its developers give', 'The eligible green pathways in the next Data Centre Call for Application, reviewed 18 to 24 months from August 2026', 'Feasibility studies for the second Malaysia interconnector of up to 2 GW, and EMA\'s import landing sites'],
  },
```

## stack.ts

Layer `grid` ("The grid connection"). Place after `two-governments-one-confession`, which it builds on:
`pieces: ['the-queue-not-the-chip', 'the-part-money-cannot-hurry', 'hitachi-energy-plans-the-queue', 'siemens-energy-measures-the-shortage', 'two-governments-one-confession', 'singapore-cannot-wait-for-the-cable', 'the-power-it-drops', 'pjm-sends-the-bill']`

(Another agent may also be adding to this list; merge at publish.)

## Glossary (heading: "Getting power to the building")

- `Subsea power cable`: An armoured high-voltage cable laid along the seabed to carry electricity between countries or from offshore wind. Made to order in a few specialist factories and laid by specialist ships.
- `Converter station`: The plant at each end of a direct current link that turns alternating current into direct current and back. Built to order, and one of the slowest parts of a subsea link.
- `Electricity Importer Licence`: In Singapore, the full licence from the Energy Market Authority that lets an import project start construction and commercial operation. Comes after a Conditional Approval and a Conditional Licence.
- `Data Centre Call for Application (DC-CFA)`: Singapore's competitive process for handing out new data centre capacity, run by EDB and IMDA. Winners must meet efficiency and green energy conditions.

The existing `HVDC` entry already fits; no change needed.

## numbers.ts (physical figures only)

```ts
  { layer: 'grid', value: '~6 GW', what: 'Low-carbon electricity Singapore aims to import by 2035, all of it by subsea cable from its neighbours. Every project approved so far is still conditional.', piece: 'singapore-cannot-wait-for-the-cable', asOf: 'October 2026' },
```

Optional second: `{ layer: 'grid', value: '95%', what: 'Share of Singapore\'s electricity that comes from natural gas. Too little land for renewables at scale is why green power must be imported.', piece: 'singapore-cannot-wait-for-the-cable', asOf: '26 October 2026' }`

## LinkedIn post (§9)

```
Singapore handed out 200 megawatts of new data centre capacity in August, and the green power its rules name is all made on the island.

Singapore's plan for clean electricity rests on importing about 6 gigawatts from its neighbours by 2035, but all 13 new import projects are still conditional and the earliest aim to start in 2028. The data centre rules name clean fuels and solar on the island instead, and the winners will use them for more than half their power. I read that as a government declining to wait for the cable.

The piece covers why Singapore must import green power, what a subsea link needs before it carries a megawatt, and what the data centre rules reveal.

https://thephysicallayer.fyi/journal/singapore-cannot-wait-for-the-cable/

#Singapore #DataCentres #EnergyInfrastructure
```

## Figures in the body (counted by the checker within the 15 limit, 0 money figures)

| Figure | Primary source |
|---|---|
| August, 200 MW to four operators, more than half green | EDB and IMDA fact sheet, 21 August 2026 |
| Green pathways list, Jurong Island | EDB and IMDA fact sheets, 1 December 2025 and 21 August 2026 |
| About 6 GW of imports by 2035 | EMA release, 30 May 2025 (Singa Renewables) |
| About 95% of electricity from natural gas | EMA release, 26 October 2026 (Five-Year Energy Infrastructure Plan) |
| Existing Malaysia link up to 1 GW (EMA, 26 October 2026); 13 conditional new import projects; Indonesia, Malaysia, Vietnam, Cambodia, Australia | EMA release, 7 August 2026 |
| Conditional status; full importer licence lets construction start | EMA releases, 5 September 2024 and 30 May 2025 |
| At least 50% green | EDB and IMDA fact sheet, 1 December 2025 |
| Five new gas plants add about a quarter to capacity by 2031; import landing sites; second Malaysia link studies | EMA release, 26 October 2026 |
| Earliest 2028 (five Indonesian conditional licences); around 2029 (Johor 900 MW, Singa); 2035 (Sembcorp 1.3 GW) | EMA releases, 5 September 2024, 30 May 2025, 7 August 2026, 26 October 2026 |

Mechanism statements, not figures: subsea cable from a few specialist factories laid by a small fleet of ships; converter stations built to order. These are physical description, consistent with hitachi-energy-plans-the-queue.

## Sources (every figure)

- EDB and IMDA fact sheet, Launch of Second Data Centre Call for Application, 1 December 2025: https://www.edb.gov.sg/content/dam/edb-en/about-edb/media-releases/news/launch-of-second-data-centre-call-for-application/Launch%20of%20second%20data%20centre-call%20for%20application.pdf
  - At least 200 MW; at least 50% (winners chose to exceed it) from eligible green energy pathways "such as biomethane, low-carbon ammonia, low-carbon hydrogen, novel fuel cells with carbon capture & storage technology, or vertical building-integrated photovoltaics/building-applied photovoltaics"; PUE 1.25 at 100% IT load or better; Green Mark DC Platinum. No mention of electricity imports.
- EDB and IMDA fact sheet, Four data centre proposals selected under DC-CFA2, 21 August 2026: https://www.edb.gov.sg/content/dam/edb-en/about-edb/media-releases/news/four-data-centre-proposals-selected-as-part-of-second-data-centre/Fact%20Sheet%20-Four%20data%20centre%20proposals%20selected%20as%20part%20of%20second%20data%20centre.pdf
  - 200 MW provisionally allocated, 50 MW each to Digital Realty, Equinix, Keppel Data Centres, ST Telemedia Global Data Centres; more than 20 proposals; more than 50% from green energy; all on Jurong Island low-carbon DC park; next call reviewed in 18 to 24 months.
- EMA, Singapore Indonesia make substantive progress on electricity imports, 5 September 2024: https://ema.gov.sg/news-events/news/media-releases/2024/singapore-indonesia-make-substantive-progress-on-electricity-imports
  - Five Conditional Licences, 2 GW (Pacific Medco 0.6, Adaro 0.4, EDP Renewables APAC 0.4, Vanda RE 0.3, Keppel 0.3); Conditional Approvals 1.4 GW (Singa 1, Shell 0.4); aim for commercial operations "from 2028"; Electricity Importer Licence issued once conditional obligations are met.
- EMA, Conditional Licence to Singa Renewables, 30 May 2025: https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2025/20250530-Media-Release-Singapore-Grants-Conditional-Licence-to-Singa-Renewables.pdf.coredownload.pdf
  - 1 GW from Indonesia; sixth Conditional Licence; commercial operations "from 2029 onwards"; target "up to around 6 GW of low-carbon electricity by 2035".
- EMA, Conditional Approvals for 900 MW from Peninsular Malaysia, 7 August 2026: https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2026/20260807-Media-Release-Conditional-Approval-for-900MW-of-Electricity-Trade-Between-Peninsular%20Malaysia-SG.pdf.coredownload.pdf
  - Sembcorp Utilities 300 MW, Southern Solar Alliance (Ditrolic) 600 MW, Johor solar and batteries, commercial operations "around 2029"; 13 import projects from Australia, Cambodia, Indonesia, Malaysia and Vietnam; earlier 1 GW Sarawak approval; SGEI, SP Group and TNB studying a second interconnector of up to 2 GW.
- EMA, Conditional Approval to Sembcorp Utilities for 1.3 GW, 26 October 2026: https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2026/20262610-EMA-Media-Release-EMA-Grants-Conditional-Approval-to-Sembcorp-Utilities.pdf.coredownload.pdf
  - With MY Energy Consortium (Petronas, TNB) and PTSC; Vietnam offshore wind and Malaysia solar; import "by 2035".
- EMA, Five-Year Energy Infrastructure Plan to Meet Unprecedented Future Demand, 26 October 2026: https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2026/20262610-EMA-Media-Release-Five-Year-Energy-Infra-Plan-to-Meet-Unprecedented-Future-Demand.pdf.coredownload.pdf
  - Peak demand 8.6 GW (August 2026), 9.9 to 13 GW by 2031, mainly semiconductors and data centres; five new gas plants 2026 to 2031, capacity up about 26% from about 12 GW; natural gas about 95% of electricity; "progressively develop sufficient electricity import landing sites"; existing Malaysia link up to 1 GW; second interconnector up to 2 GW by 2030 if realised; solar 2.3 GWp today, 3 GWp by 2030, 4 GWp by 2035. (Not all used in the piece; good material for a research note.)
- MDDI, New Digital Infrastructure Bill, 8 September 2026: https://www.mddi.gov.sg/newsroom/new-digital-infrastructure-bill-to-strengthen-the-foundations-for-singapore-s-digital-economy/
  - First Reading 8 September 2026; resilience licensing for data centres of 10 MW and above; sustainability licensing for 3 MW and above; green energy commitments made to win capacity (for example under DC-CFA) can be enforced as licence conditions. Not used in the piece to stay inside the word limit. Passage on 7 October 2026 is press-only (W.Media, Rajah & Tann); not stated.
- MDDI reply to parliamentary question on data centre capacity limits, 3 March 2026: https://www.mddi.gov.sg/newsroom/mddi-s-response-to-pq-on-limits-on-singapore-s-total-data-centre-capacity/ (background: no pre-determined upper limit, "within the envelope of our resource constraints").
- Lead: The Straits Times video, "Singapore will grow data centre capacity in a disciplined and calibrated way: Tan Kiat How", https://www.youtube.com/watch?v=jB5W_3t_Utw (recorded the day after the Bill's First Reading, so about 9 September 2026; date not confirmed). Credited once in the sources line. I did not find a gov.sg write-up of these remarks, so no quote from him is used in the piece.

## Video figures dropped or flagged

- The Singapore video carries no figures. Its one substantive claim, that the Digital Infrastructure Act was tabled for First Reading "yesterday", is confirmed by MDDI (8 September 2026). The minister's phrasing ("not pursuing capacity for capacity's sake", "disciplined and calibrated") is not quoted, because I could not find it on gov.sg.
- Skimmed southeast-asia-dc-boom (third-party field-trip video): its figures (Johor case timeline from land in February 2024 to keys in October 2026, Siam AI 100 MW, Vietnam occupancy under 20%, Google's $1 billion in Thailand, FPT's value) are unverified and off-subject. None used.

## Press-only or unverified, left out

- 9.25 GW total of approved imports and "none has begun construction" (Wood Mackenzie, via Singapore Business Review and Business Times, 2026). Wood Mackenzie's site refused the connection, so not verified and not used. The piece says instead that every approval is conditional, which EMA's releases support.
- 1.4 GW of existing data centre capacity and 7% of national electricity (IMDA Green DC Roadmap, May 2024): the MDDI factsheet copy would not download; not used.
- Corrected by the fact-check: Keppel holds EMA's first Electricity Importer Licence (LTMS-PIP, over existing interconnections). None of the 13 new projects holds one, as far as EMA's releases show.
