# Abilene draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/abilene-switched-on-in-stages.md` (draft: true)
Cover: `public/covers/abilene-switched-on-in-stages.svg`
Drafted 29 October 2026. Topic approved by Tommy; the final claim wording needs his approval before publish.

## Proposed claim

At Abilene, the date each building was energised, not the date it was announced or started, set when capacity arrived, so energised megawatts are the only capacity figure worth quoting.

### Alternatives considered

1. "Under construction" gigawatts (Cushman & Wakefield: 37.7 GW in the Americas, H1 2026) will mostly arrive later than their builders say, because the connection, not the building, sets the date. Rejected as the lead: a market-wide forecast with no clean single observable, and it loses Abilene as the subject.
2. At Abilene, delivery to the tenant follows energisation within a quarter, so delivered and energised capacity are effectively the same number. Rejected as the lead: narrower and duller, but it is folded into the falsifier.

Chosen because it keeps Abilene as the subject, builds on nebius-paid-for-what-is-switched-on (contracted vs connected) by moving from one company's disclosure to one campus's timeline, and has a dated, company-disclosed test (Oracle's own June 2026 timetable).

## claims.ts entry

```ts
  {
    id: 'abilene-switched-on-in-stages',
    claim: 'At Abilene, the date each building was energised, not the date it was announced or started, set when capacity arrived, so energised megawatts are the only capacity figure worth quoting.',
    breaksIf: 'Crusoe reports the Abilene campus energised or complete by the end of 2026, but Oracle has still not reported all eight buildings delivered by its results in March 2027, a quarter after the timetable it gave in June 2026 (its quarter to 30 November 2026). Then fitting out, not power, is setting the pace.',
    watch: ['Oracle\'s Abilene delivery update in its December 2026 results', 'Any Crusoe statement that phase two is energised or complete', 'Whether Oracle reports all eight buildings delivered by March 2027', 'Cushman & Wakefield\'s next count of capacity under construction against operating'],
  },
```

## stack.ts

Layer `operators` ("Who runs the capacity"). Its constraint sentence, "Buyers pay for megawatts switched on, not megawatts signed", fits exactly. Suggested position directly after the Nebius piece it builds on:
`pieces: ['nebius-paid-for-what-is-switched-on', 'abilene-switched-on-in-stages', 'power-first-chips-last']`

## Glossary (heading: "Getting power to the building")

- Existing `Announced versus energised megawatts` already covers the core term; no change needed. Optionally add one sentence: "Abilene shows the difference: announced in 2024, its buildings were energised and handed over across 2025 and 2026."
- New `Delivered capacity`: Data centre capacity handed over to the tenant who will run computers in it. It comes after a building is energised and before the computers are working at full load.
- New `Capacity in service`: A builder's term for capacity that is ready for customers and fully fitted out. DayOne's share listing filing counts it separately from capacity that is merely energised.

## numbers.ts (physical figures only)

```ts
  { layer: 'operators', value: '6 of 8', what: 'Buildings at the Abilene, Texas AI campus Oracle had delivered to its customer, about three quarters of the capacity, more than two years after work began in June 2024.', piece: 'abilene-switched-on-in-stages', asOf: '10 September 2026' },
```

Optional second: `{ layer: 'grid', value: '50 / 38 / 285 GW', what: 'Data centre capacity across the Americas operating, under construction and planned, by Cushman & Wakefield\'s count, with no split for AI. Only the first is capacity anyone can use.', piece: 'abilene-switched-on-in-stages', asOf: 'H1 2026' }`

## LinkedIn post (§9)

```
The AI campus at Abilene, Texas has been switching on in pieces for more than two years. Announced, started, energised, handed over and put to work: each was a different date.

Work began in June 2024. Crusoe says the first two buildings were energised within a year, and Oracle told investors in September 2026 that six of the eight had been handed over. Most capacity headlines count gigawatts announced or under construction. The figure that tells you when computing is actually available is the one connected to power.

The piece covers the five stages a campus passes through, why the grid connection sets the pace, and the test that would prove me wrong.

https://thephysicallayer.fyi/journal/abilene-switched-on-in-stages/

#DataCentres #AIInfrastructure #EnergyInfrastructure
```

## Figures in the body and their primary source

- June 2024 construction start; "within a year, the first two buildings were energized"; first phase "up and running", September 2025; eight-building campus: Crusoe, 30 September 2025: https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
- 1.2 GW grid interconnection; gas turbines "to power its back-up power supply"; Lancium's power plan: Crusoe, 18 March 2025: https://www.crusoe.ai/resources/newsroom/crusoe-expands-ai-data-center-campus-in-abilene-to-1-2-gigawatts
- Phase two (six buildings) "expected to be energized in mid-2026"; phase one 200+ MW: Crusoe, Blue Owl and Primary Digital, 21 May 2025: https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture
- Phase two "expected to reach completion by the end of 2026"; first two 100 MW buildings energised in under a year: Crusoe, 27 March 2026: https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
- 42% of Abilene capacity delivered; another 35% within 90 days and the remainder in the following quarter (the quarter to 30 November 2026): Oracle FQ4 FY2026 call, 10 June 2026, Clay Magouyrk (transcript via Motley Fool): https://www.fool.com/earnings/call-transcripts/2026/06/10/oracle-orcl-q4-2026-earnings-call-transcript/
- "6 of the 8 campus buildings, representing 618 megawatts and 75% of total capacity have now been delivered to the customer"; 131,000 GPUs delivered there in Q1: Oracle FQ1 FY2027 call, 10 September 2026, Clay Magouyrk: https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/
- Abilene as Stargate's flagship site: OpenAI, Oracle and SoftBank announcement of five new Stargate sites, 23 September 2025 (checked via Reuters-based coverage, e.g. https://www.neowin.net/amp/openai-announces-five-new-ai-data-center-sites-for-stargate-project/ ; OpenAI's own page not fetched): https://openai.com/index/five-new-stargate-sites/
- 50.3 GW operating, 37.7 GW under construction (91.7% precommitted), 285 GW planned, H1 2026: Cushman & Wakefield Americas Data Center Update H1 2026, published 14 September 2026: https://www.cushmanwakefield.com/es-cl/insights/americas-data-center-update
- Johor "over 1GW of live IT capacity at the start of the year", "just 0.7% colocation vacancy": Knight Frank, Data Centre Atlas 2026 (PDF modified 26 June 2026), Johor page: https://www.knightfrank.co.uk/site-assets/research/report-pdfs/data-centres/data-centre-atlas-2026-final.pdf
- DayOne capacity in service 49 MW at end 2023 and 962 MW at 20 September 2026; "The majority of our in-service capacity and Bookings are concentrated at two data center campuses located in the same market"; separate definitions of energised and Capacity In Service: DayOne Data Centers Ltd Form F-1, 5 October 2026: https://www.sec.gov/Archives/edgar/data/0002118192/000119312526414188/d223752df1.htm
- Lead sheet only, credited in the sources line: third-party YouTube video "State of AI data centres 2026" (data to 5 October 2026), transcript at research-build/source-ai-datacentre-video/TRANSCRIPT.md.

## Could not verify / left out / flags

- Oracle did NOT give a new date for the last buildings on the 10 September 2026 call (checked twice against the transcript). The only Oracle timetable found is the June 2026 one (remainder in the quarter after the next 90 days, i.e. to 30 November 2026). The falsifier rests on that plus Crusoe's end-2026 completion. Oracle's own release and data-centres page returned 403, so the wording was checked on the Motley Fool transcript, not oracle.com. A fact-checker should confirm against Oracle's IR transcript.
- Video: DayOne's in-service capacity "across Johor and Batam grew nearly 20-fold in less than three years". The filing gives portfolio-wide figures (49 MW to 962 MW, 19.6x is my arithmetic) and does not split them by Johor and Batam; it says only that most of it sits at two campuses in one market. The piece states the portfolio figures and does not use "20-fold" or attribute the 962 MW to Johor.
- Video: Cushman & Wakefield's count covers "data centers of every kind". The C&W page does not define scope; the piece says only that the count does not separate AI campuses from other data centres. The 38 GW in the piece is 37.7 rounded; 50 GW is 50.3.
- Knight Frank: the 1,110 MW Johor live capacity figure appears in press coverage (The Edge, 30-31 July 2026) but the Atlas PDF text says "over 1GW". The piece uses "above 1 gigawatt".
- Units: Oracle's 618 MW as 75% implies about 824 MW total, against Crusoe's 1.2 GW grid interconnection. They are probably different yardsticks (IT capacity against grid connection) and the piece does not set them side by side.
- Bloomberg/Reuters report of a cancelled ~600 MW Abilene expansion (press, not primary): left out; it is about an expansion, not the eight buildings tested here.
- Not used from the video: xAI Colossus 950 MW (Epoch AI estimate), Meta Hyperion, Synergy 55% / Texas 71%, JLL frontier markets and Middle East 1.6 GW, Northern Virginia 0.2% vacancy, ERCOT pause, Stargate UAE, China computing power. None verified, none in the piece.
- Actual energisation dates for the six phase-two buildings are not disclosed; the piece says only that they "were meant to be energised by the middle of this year" (Crusoe, May 2025) and that delivery "followed close behind".
