# Singapore old halls draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/singapore-licenses-the-old-halls.md` (draft: true)
Cover: `public/covers/singapore-licenses-the-old-halls.svg`
Drafted 29 October 2026 (batch 3, Tier A item A4). The claim needs Tommy's approval before publish.

## Verdict: PASS, with the outline corrected (read this first)

The outline said the Act "binds existing halls to an efficiency ceiling, forcing retrofits or derating". The primary sources do not support that as stated. The Bill (clause 35) imposes a duty to meet "minimum facility-level energy efficiency requirements ... as may be prescribed": no PUE number and no date are in the Bill. The minister said on 6 October that the six-month licence window "does not mean that all regulatory requirements must be met within six months. The timelines for meeting these requirements will be set out together with the detailed requirements", and on 7 October that the details "will be developed with industry over the coming year" with the Act expected in force in 2027. So the piece says what is set (licence, stated critical IT load, power to cut it, efficiency weighed at renewal, existing halls in scope) and what is not (the PUE level and deadline).

Thresholds: both 3 MW and 10 MW are right, for different licences. The DC licence (Part 4, sustainability) applies at 3 MW critical IT load, the Bill's definition of "data centre". The major FDI licence (Part 3, security and resilience) applies to data centre facility services in halls of at least 10 MW (Schedule, "major data centre facility service"). The piece uses only 3 MW.

Quality bar:
1. New mechanism: yes. Existing pieces cover efficiency as an entry test for new capacity (PUE 1.25 in two-governments-one-confession) and green power for new awards (singapore-cannot-wait-for-the-cable). This is efficiency as a condition of keeping capacity already installed: every hall carries a licence stating its critical IT load, which IMDA can reduce (clause 39(2)(b)) for failing the efficiency duty. It extends the rationing argument to the installed fleet without contradicting it.
2. Primary sources: the Bill text and MDDI's own releases and ministerial speeches. One item is press-only: the vote on 7 October (see below).
3. Beyond the headline: the headline is "PUE rules for all data centres". The PM learns that no number or date exists yet, the lever is licensed megawatts, in-house enterprise halls are caught, customer-owned servers are not covered at the outset, and about 70 halls are in scope.

Consistency with two-governments-one-confession: its falsifier says Singapore is wrong if the "efficiency ceiling moves on a fixed schedule rather than with scarcity". This piece does not say the schedule is fixed; the minister ties pacing to "investment and depreciation cycles". No contradiction.

## Fact-check corrections applied (29 October 2026)

- Tan Kiat How is Senior Minister of State, moving the Bill for the Minister; "the minister" replaced with his name and title.
- The 7 October vote stays PRESS ONLY; the piece now says "by press accounts" and "the Bill as introduced". Committee-stage amendments unknown.
- Falsifier rebuilt: the near-certain "no PUE limit before 1 January 2028" limb is dropped. The test now turns on the first regulations by 31 December 2028, plus a second limb on any capacity cut before 2030. claims.ts entry matches.
- Reconciliation with two-governments-one-confession added in the body: pacing follows investment and depreciation cycles, not a climate timetable.
- DC-CFA2 called a call for applications, not an award; the licence is described as needed once the Act takes effect (expected 2027).

## Proposed claim

Singapore's Digital Infrastructure Act, once in force, puts every data centre of 3 MW or more, including the roughly 70 already running, on an IMDA licence that states the critical IT load it may run and lets IMDA cut it for missing efficiency rules, but leaves the PUE level and deadline for existing halls to regulations not yet written; those first rules, by the end of 2028, will give existing halls a compliance date, paced to investment and depreciation cycles so that no existing hall loses licensed megawatts over efficiency before 2030.

### Alternatives considered

1. The outline's "existing halls must retrofit or be derated" claim. Rejected: not what the law says yet; there is no number to force anything.
2. "Singapore will free power for new capacity by retiring old halls" (the closing speech's "upgrade, redevelop or ... retire" and the Jurong Island redevelopment line). Rejected as the lead: no primary figure for how much capacity would be freed (the 2024 roadmap's 300 MW is press-reported), so it would be speculation.

Chosen because it is exactly what the Bill and the minister say, it is two-sided and dated, and it names the real lever.

## claims.ts entry

```ts
  {
    id: 'singapore-licenses-the-old-halls',
    claim: 'Singapore\'s Digital Infrastructure Act, once in force, puts every data centre of 3 MW or more, including the roughly 70 already running, on an IMDA licence that states the critical IT load it may run and lets IMDA cut it for missing efficiency rules, but leaves the PUE level and deadline for existing halls to regulations not yet written; those first rules, by the end of 2028, will give existing halls a compliance date, paced to investment and depreciation cycles so that no existing hall loses licensed megawatts over efficiency before 2030.',
    breaksIf: 'By 31 December 2028, IMDA\'s first facility-level energy efficiency regulations or codes of practice exempt existing data centres or set them no compliance date (including if none have been issued by then), or IMDA reduces any existing data centre\'s licensed critical IT load on efficiency grounds before 1 January 2030.',
    watch: ['Commencement notice for Part 4 of the Act, expected in 2027', 'IMDA consultation on the facility-level energy efficiency regulations and codes of practice', 'The PUE level and compliance date set for existing data centres', 'Any order reducing a licensee\'s critical IT load under clause 39(2)(b)'],
  },
```

## stack.ts

Layer `grid` ("The grid connection"), after `singapore-cannot-wait-for-the-cable` (or after `two-governments-one-confession` if that draft is not yet in). The piece is about who may hold connected megawatts in Singapore, the same rationing object as two-governments-one-confession. `cooling` was considered, since PUE is mostly cooling overhead, but the lever in the law is licensed capacity, not cooling technology. Other agents may be editing this list; merge at publish.

## Glossary (heading: "Inside the data centre", or wherever PUE sits)

- `Critical IT load`: The most power a data centre is designed to deliver to its servers and network equipment. Singapore uses it to decide which halls need a licence (3 MW and up) and states it on each licence.
- `DC licence`: The licence IMDA will require, under Singapore's Digital Infrastructure Act, to operate any data centre of 3 MW or more. It states the critical IT load the hall may run and carries efficiency duties.

PUE already exists in the glossary; no change.

## numbers.ts (physical figures only)

```ts
  { layer: 'grid', value: '3 MW', what: 'Critical IT load from which a Singapore data centre needs an IMDA licence under the Digital Infrastructure Act, existing halls included. About 70 data centres are in scope.', piece: 'singapore-licenses-the-old-halls', asOf: 'October 2026' },
```

## LinkedIn post (§9)

```
Singapore's new data centre law reaches the halls already running, and the lever is the megawatts on their licence.

About 70 existing data centres will need an IMDA licence that states how much computing power each may run, and the regulator can cut that figure if a hall misses the efficiency rules. What the law does not yet say is the efficiency number, or the date old halls must meet it. Those come in regulations still being written, with the Act expected in force in 2027.

The piece covers how the licence works, why an old hall cannot simply catch up, and what is still left open.

https://thephysicallayer.fyi/journal/singapore-licenses-the-old-halls/

#Singapore #DataCentres #EnergyInfrastructure
```

## Figures in the body (10, 0 money figures)

| Figure | Primary source |
|---|---|
| New capacity award required PUE 1.25 or better | EDB and IMDA DC-CFA2 fact sheet, 1 December 2025 (as used in two-governments-one-confession and the cable sidecar) |
| About 70 data centres in scope | Closing speech, 7 October 2026: "There are about 70 data centres in Singapore today, which will be required to meet the sustainability requirements." |
| A large share of capacity in existing halls | Opening speech, 6 October 2026: "a significant proportion of Singapore's data centre capacity is housed in existing facilities" |
| Parliament approved the Bill in October | PRESS ONLY for the vote date (7 October: W.Media, Rajah & Tann, RecordOwl). Primary support: the closing speech of 7 October refers to "the approved Act". sso.agc.gov.sg returned 403; not bypassed. The enacted text is not yet published, so the piece rests on Bill No. 20 of 2026 as introduced. Any committee-stage amendment is unverified. |
| 3 MW critical IT load; licence covers own-use halls | Bill clause 2 ("data centre" definition), clause 23(2); opening speech: "regardless of whether they serve third-party customers or are used by the operator for its own purposes" |
| 3 MW about a large suburban shopping mall | Opening speech, 6 October 2026 |
| Licence states the critical IT load | Bill clause 26(2) |
| Efficiency "as may be prescribed", measured by PUE | Bill clause 35(a); opening speech ("measured through Power Usage Effectiveness") |
| Fine, or reduce critical IT load short of revocation | Bill clauses 39(1)(a)(i), 39(2)(b), 40 (fine up to the higher of S$1 million or 10% of Singapore turnover, not stated in the piece) |
| Efficiency weighed at renewal | Bill clause 25(1)(b), 25(2)(b) |
| No number, no date; regulations and codes of practice | Bill clauses 35 and 37; opening speech; closing speech |
| In force 2027; six months to apply; not a compliance deadline | Closing speech 7 October; opening speech 6 October; Bill clause 71(2) |
| "reasonable time to improve"; upgrade, redevelop or retire | Closing speech, 7 October 2026 |
| Pacing by "investment and depreciation cycles" | Opening speech, 6 October 2026 |

Mechanism statement, not a sourced figure: old halls' chillers, air handling and shell were built for older servers, so improvement needs new plant or a rebuild. General physical description, consistent with cooling-is-half-the-job.

## Video figures dropped or flagged

The video (Tan Kiat How to The Straits Times, the day after First Reading) has no figures. Its only factual line, that the Bill was tabled for First Reading "yesterday", matches MDDI (8 September 2026). Its framing ("disciplined and calibrated", "uplift the entire standard") is not reproduced. Nothing dropped.

Not used, and why:
- Green Data Centre Roadmap goal of PUE 1.3 or lower for all data centres over about ten years: I could not open the IMDA page or booklet (JavaScript page; the factsheet link returned HTML). Press only (DatacenterDynamics, 30 May 2024). Left out.
- PUB Water Usage Effectiveness target of 2 cubic metres per MWh, for new and existing halls: in the closing speech, but water is a separate thread. Left out for length.
- Customer-owned servers not covered at the outset: MDDI consultation response, 8 September 2026 (paragraphs 14 and 16). Strong, but cut for length; good for a research note.
- About two-thirds of the 70 also above 10 MW: closing speech. Cut for length.

## Sources (every figure)

- Digital Infrastructure Bill, Bill No. 20 of 2026, as introduced 8 September 2026: https://www.parliament.gov.sg/api/media/27325093-8be6-4ca2-bc3e-5e7a5f70b2f1/Digital-Infrastructure-Bill-20-2026.pdf (clauses 2, 3(3) and (5), 23, 24, 25, 26, 27, 35, 36, 37, 39, 40, 71; Schedule para 3 for the 10 MW major DC facility service)
- MDDI, New Digital Infrastructure Bill to strengthen the foundations for Singapore's digital economy, 8 September 2026: https://www.mddi.gov.sg/newsroom/new-digital-infrastructure-bill-to-strengthen-the-foundations-for-singapore-s-digital-economy/ (3 MW and 10 MW, PUE requirements, "will apply to existing and new DCs", transition time, more than 1.6 GW in Singapore)
- MDDI, Public consultation on the Digital Infrastructure Bill (outcome), 8 September 2026: https://www.mddi.gov.sg/newsroom/public-consultation-on-the-digital-infrastructure-bill/ (consultation 1 to 22 July 2026; no mandatory IT equipment efficiency at the outset; customer-owned equipment not covered; six months is for the licence application)
- MDDI, Opening speech by SMS Tan Kiat How for the Second Reading, 6 October 2026: https://www.mddi.gov.sg/newsroom/opening-speech-by-sms-tan-kiat-how-for-the-second-reading-of-the-digital-infrastructure-bill/
- MDDI, Closing speech by SMS Tan Kiat How for the Second Reading, 7 October 2026: https://www.mddi.gov.sg/newsroom/closing-speech-by-sms-tan-kiat-how-for-the-second-reading-of-the-digital-infrastructure-bill/
- Official Report, Vol 96 Issue 38, 6 October 2026, via sgparliament.com (unofficial mirror of Hansard): https://www.sgparliament.com/debate/34204 (debate text; did not reach the third reading)
- Press only, for the 7 October passage: W.Media https://w.media/?p=44136 ; Rajah & Tann https://www.rajahtannasia.com/?p=198889 (403, not opened) ; RecordOwl https://recordowl.com/news/digital-infrastructure-bill-passed-imda-licences
- EDB and IMDA, Launch of second DC-CFA, 1 December 2025 (PUE 1.25 at 100% IT load): https://www.edb.gov.sg/content/dam/edb-en/about-edb/media-releases/news/launch-of-second-data-centre-call-for-application/Launch%20of%20second%20data%20centre-call%20for%20application.pdf
- Lead: The Straits Times video, "Singapore will grow data centre capacity in a disciplined and calibrated way: Tan Kiat How", https://www.youtube.com/watch?v=jB5W_3t_Utw (credited once in the sources line).

Not checked: SS 564 and IMDA's existing licence conditions and codes. The Act's codes do not exist yet; SS 564 is not cited in the Bill or the speeches (the opening speech names the Green Data Centre Roadmap and BCA-IMDA Green Mark as inputs), so nothing in the piece depends on it.
