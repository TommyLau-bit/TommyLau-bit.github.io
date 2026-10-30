# Constellation uprates draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/constellation-squeezes-the-reactors.md` (draft: true)
Cover: `public/covers/constellation-squeezes-the-reactors.svg`
Drafted 29 October 2026 (batch 3, Tier A item A13). Claim needs Tommy's approval before publish.
Checker: 0 failures, 0 warnings. Body about 509 words, 0 money figures.

Relation to existing pieces: `constellation-restarts-the-reactor` (publishes 30 Oct) is about the grid place at Crane and names the Google uprates only as "its next move", with one line saying uprates help "only as far as each design allows". `palisades-waits-on-the-reactor` (draft) is about a restart where the reactor sets the date. This piece is about uprates as a mechanism: the site, licence and grid place are reused, but each step needs new kit, often an NRC licence amendment, and a refuelling outage, so a fleet uprate arrives as a staircase. It links to neither, to avoid making it read as a Constellation sequel; a link to the Crane piece could be added in "How an uprate works" at publish if wanted. It does not contradict the Crane piece's watch item ("whether the first of the 890 MW Google uprates lands in 2028").

## Proposed claim

Constellation's 890 megawatts for Google will arrive in small steps, one refuelling outage at a time, not as one reactor's worth: most of it rests on extended uprates whose NRC applications Constellation will not file until late 2027 or after, the last in late 2030, so well under half is in service by the end of 2029 and the rest lands by 2032.

### Alternatives considered

1. "Uprates escape the grid connection queue because they reuse an existing place on the grid." Rejected: the Crane piece already makes the reuse-the-grid-place point, and I could not verify how PJM treats Constellation's incremental megawatts (PJM studies an uprate as its own interconnection request, and has a fast track, the Expedited Interconnection Track, for uprates over 250 MW), so the claim would not rest on primary sources.
2. "Most of the extra megawatts in America's nuclear uprate wave come from a handful of extended uprates, not the many small measurement fixes." Rejected as the lead: true from the NRC list but a fleet-wide count, not about Constellation, and no MW split per unit is public. Kept as the "seven of twelve are the smallest kind" line.

Chosen because it is new to the site (the outage calendar and the licence amendment as the pace-setters of uprate power), rests on the NRC's own list and Constellation's and Google's own statements, and tells a PM something the headline does not: "890 MW, equal to a large reactor" is a staircase through 2032, mostly back-loaded.

## claims.ts entry

```ts
  {
    id: 'constellation-squeezes-the-reactors',
    claim: 'Constellation\'s 890 megawatts of uprates for Google will arrive in small steps, one refuelling outage at a time, not as one reactor\'s worth: most of it rests on extended uprates whose NRC applications Constellation will not file until late 2027 or after, so well under half is in service by the end of 2029 and the rest lands by 2032.',
    breaksIf: 'Constellation reports more than half of the 890 MW of Google uprates in service by 31 December 2029, or files every one of its planned extended power uprate applications with the NRC by 31 December 2027.',
    watch: ['The NRC\'s expected uprate applications list: whether Constellation\'s extended uprate filings move earlier or later', 'NRC licence amendments issued for Constellation uprates, and in which refuelling outage each is installed', 'Constellation\'s quarterly reports of uprate megawatts placed in service, starting with the first expected by 2028', 'Calvert Cliffs\' 190 MW uprate for Amazon against its 2030 to 2032 window'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"), placed directly after `constellation-restarts-the-reactor` and before `oklo-sells-the-electricity`:
`pieces: [..., 'constellation-restarts-the-reactor', 'constellation-squeezes-the-reactors', 'oklo-sells-the-electricity']`
Same honest wrinkle as Crane: these reactors feed the PJM grid, not a campus beside them; the layer is where firm power for AI is made. No new layer.

## Glossary (heading: "Getting power to the building")

The Crane sidecar already proposes `Uprate`. If it is in by publish, add only:
- `Refuelling outage`: The planned shutdown, every 18 to 24 months at Constellation's units, when a reactor takes new fuel and heavy equipment can be swapped.
- `Extended power uprate`: The largest kind of uprate, approved for up to 20 per cent more power, needing new turbines, pumps, generators or transformers and a licence amendment from the Nuclear Regulatory Commission.
- `Measurement uncertainty recapture`: The smallest kind of uprate, under 2 per cent, won by measuring the water fed to the reactor more precisely so it can run closer to its licensed limit.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '18 to 24 months', what: 'How often Constellation\'s reactors shut down to refuel, the only window in which heavy uprate equipment can be fitted.', piece: 'constellation-squeezes-the-reactors', asOf: '2025 annual report' },
```

Optional: `{ layer: 'onsite', value: '890 MW', what: 'New nuclear capacity Constellation is adding for Google by upgrading eleven reactors it already runs, the first step by 2028 and all of it before the end of 2032.', piece: 'constellation-squeezes-the-reactors', asOf: '6 October 2026' }`

## LinkedIn post (§9)

```
Constellation is adding a large reactor's worth of nuclear power for Google without building a reactor, and it will not arrive as one.

The 890 megawatts come from upgrading eleven reactors it already runs. Each step needs new turbines or generators, often a licence change from the regulator, and a refuelling shutdown that comes round only every 18 to 24 months. The regulator's own list shows most of the big applications are not due until late 2027 or after, so for AI buyers counting on upgrade power, the calendar is the outage schedule.

The piece covers how an uprate works, why the refuelling outage sets the pace, and what would prove me wrong.

https://thephysicallayer.fyi/journal/constellation-squeezes-the-reactors/

#NuclearEnergy #DataCentres #EnergyInfrastructure
```

## Sources (every figure)

- Constellation and Google, "Google and Constellation Announce Landmark Agreement to Bring 890 MW of New Nuclear Capacity to PJM Grid as Part of Long-Term Power Deal", 6 October 2026: https://www.constellationenergy.com/news/2026/10/google-and-constellation-announce-landmark-agreement-to-bring-890-mw-of-new-nuclear-capacity-to-pjm-grid.html
  - 890 MW (verified); 11 Constellation-owned units (verified) in Illinois, Pennsylvania and New Jersey, "six nuclear sites"; 20-year PPA; "first uprate expected to be delivered by 2028"; work on "turbines, steam generators, and digital control systems"; "increasing thermal and electrical efficiency"; more than $4.3 billion investment (not used); separate 2,700 MW 15-year supply deal (not used). Plants are not named.
- Google, "Why we're backing America's existing nuclear plants", Amanda Peterson Corio, 6 October 2026: https://blog.google/company-news/why-were-backing-americas-existing-nuclear-plants/
  - "Before the end of 2032, these uprate projects will add 890 MW of firm, 24/7 clean power to the PJM grid"; 11 reactors at six plants.
- NRC, "Expected Applications for Power Uprates", page last updated 8 September 2026: https://www.nrc.gov/facilities-safety/operating-reactors/operating-reactor-licensing/power-uprates/status-of-power-uprate-applications/expected-applications-for-power-uprates
  - Twelve Constellation Energy Generation rows, plant names proprietary: EPU Q4 2026; MUR Q1 2027 (2); MUR Q2 2027 (2); EPU Q4 2027 (2); MUR Q4 2027; EPU Q4 2028; MUR Q2 2030; MUR Q3 2030; EPU Q4 2030. So 7 MUR, 5 EPU; 4 of 5 EPUs filed Q4 2027 or later. Read twice via a fetch tool (direct download returned 403, so not bypassed); both reads agreed. The list covers all Constellation uprates (Google, Amazon at Calvert Cliffs, Meta at Clinton), so the piece says "a dozen from Constellation", not "a dozen for Google". PSEG's Salem 1 and 2 stretch uprates (Q2 2027) are listed under PSEG; Constellation owns part of Salem, so they may be among the New Jersey units in the Google deal (not verified, not stated).
- NRC fact sheet, "Power Uprates for Nuclear Plants": https://www.nrc.gov/reading-rm/doc-collections/fact-sheets/power-uprates.html
  - MUR "less than 2 percent"; stretch "typically between 2 percent and 7 percent"; EPU "approved for increases as high as 20 percent". The EPU hardware sentence ("significant modifications to major balance-of-plant equipment such as the high pressure turbines, condensate pumps and motors, main generators, and/or transformers") is the NRC's "Types of Power Uprates" page text as returned by search (https://www.nrc.gov/reactors/operating/licensing/power-uprates/type-power.html); the page itself returned 403 to direct fetch, so check it at publish.
- Constellation Form 10-K for 2025, filed 24 February 2026: https://www.sec.gov/Archives/edgar/data/1868275/000186827526000032/ceg-20251231.htm
  - "refueling outages are planned to occur once every 18 to 24 months"; equipment upgrades performed during scheduled refuelling outages; average refuelling outage 22 days in 2025 (not used); uprates qualify for the 45Y credit (not used); nation's largest nuclear fleet.
- Constellation Form 10-Q for Q2 2026, filed 6 August 2026: https://www.sec.gov/Archives/edgar/data/1868275/000186827526000104/ceg-20260630.htm
  - Checked: no uprate disclosure (the Google deal postdates it). Q3 2026 results not yet out on 29 Oct.
- Constellation and Amazon, 20-year PPA at Calvert Cliffs, 30 September 2026: https://www.constellationenergy.com/news/2026/09/constellation-and-amazon-announce-20-year-power-purchase-agreement-at-calvert-cliffs.html
  - Verified: about 190 MW of uprate "coming online between 2030 and 2032", within a 690 MW 20-year agreement, plus licence renewal. Used only in the claims watch list and the exposure map (Amazon as buyer); cut from the body for the figure budget.
- Constellation, conditional DOE loan commitment of up to $5 billion for uprates, 27 October 2026: https://www.constellationenergy.com/news/2026/10/constellation-secures-conditional-doe-loan-commitment-of-up-to-5-billion-to-expand-nuclear-output.html
  - Google and Amazon deals together about 1,080 MW (890 + 190), more than $7 billion; candidate plants Braidwood, Byron, Clinton, Dresden, LaSalle, Quad Cities, Calvert Cliffs, Limerick. Not used (money); context for the research note.
- Exposure map context (what they make only): Vistra (Perry, Beaver Valley, Davis-Besse), Duke Energy (McGuire, Catawba, Brunswick), Southern Company via Southern Nuclear (Hatch, Vogtle) and PSEG (Salem) all appear on the NRC list above. GE Vernova and Siemens Energy are named as makers of steam turbines and generators, not as Constellation's suppliers (no supplier is disclosed).
- PJM interconnection context (not used): PJM Expedited Interconnection Track for new or uprated capacity over 250 MW, approved by FERC in 2026, per Troutman Pepper (https://www.troutmanenergyreport.com/2026/03/pjm-proposes-expedited-generator-interconnection-track/) and Utility Dive; press only.

## Video figures dropped or flagged

- 890 MW across eleven reactors: verified against Constellation and Google; used.
- "Amazon's deal at Calvert Cliffs also needs license extensions": verified (Constellation release, 30 Sep 2026: 190 MW uprate 2030 to 2032, relicensing); kept out of the body, used in the watch list and map only.
- "More than $3 billion at Calvert Cliffs" and "more than $4 billion for the Google upgrades": verified ($3 billion; $4.3 billion) but dropped (money budget, not needed for the mechanism).
- "Many upgrades and new agreements are due to start between 2028 and 2032": consistent with primary sources (2028 first uprate, before end 2032); the piece cites the companies, not the video.
- Google's separate 2,700 MW agreement: verified, dropped (existing power on new terms, not new output).
- Crane, Clinton/Meta, fleet capacity factor, earnings, cash flow, debt, share price, market value and multiple from the video: all dropped (covered elsewhere or out of scope; no share views).
- Outline wording "none before 2028": not quite what the sources say. Constellation says the first uprate is "expected to be delivered by 2028", so the piece says "the first uprate by 2028", not "none before 2028".

## Could not verify / left out

- Which units get which uprate type, and the MW per unit: not public (NRC lists plant names as proprietary). "Extended uprates carry the bulk of the megawatts" is inferred from the NRC size ranges (MUR under 2 per cent, EPU up to 20 per cent); stated as such in the piece, without numbers.
- NRC review durations per uprate type: no primary source fetched (NRC pages 403), so the piece gives none.
- How PJM will treat the incremental megawatts (new interconnection requests, capacity rights): not verified, so left out, despite the release's line that uprates avoid "interconnection bottlenecks".
