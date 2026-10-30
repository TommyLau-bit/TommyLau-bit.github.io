# Howmet Aerospace draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/howmet-casts-the-queue.md` (draft: true)
Cover: `public/covers/howmet-casts-the-queue.svg`
Drafted 29 October 2026 from the Watch Later batch (topic approved in outline by Tommy). Claim wording needs Tommy's approval before publish.

**Refresh before publish (30 Nov):** Howmet's third quarter 2026 results were still not on EDGAR at 18:03 SGT on 29 October 2026 (release due about 7:00 AM ET that day). Not yet checked. Re-check the gas turbine growth line, any new capacity dates and the share statement against that release and call before publishing.

**Re-check, 29 Oct 2026 (evening SGT): HOLD stands.**
- Q3 2026 release (8-K exhibit 99.1, filed 29 Oct 2026, https://www.sec.gov/Archives/edgar/data/4281/000110465926119857/tm2628456d1_ex99-1.htm): gas turbines revenue up 45 per cent year on year; Plant cites "the increase in market share" (no figure), demand that "supports the outlook beyond 2028", and capex "elevated spend beyond 2027" for aerospace, defence and gas turbines. No capacity dates, no more-than-half share, no 2028 to 2030 additions. Q3 deck not yet at the expected Howmet URL (404); Q3 10-Q not yet filed.
- Q2 10-Q (as retrievable) and the 10 March 2026 markets day deck carry no capacity dates: the deck says only "Investments (Completed + Planned Next 3-4 Years)" (p.25) and shows the Exeter and Nomi DS furnace work (p.24). The 2028 to 2030 timing and the more-than-half share remain press-transcript only.
- New facts that cut against Howmet as the single gate: Siemens Energy is adding its own gas turbine blade and vane capacity in Florida (Q1 FY26 analyst deck, 11 Feb 2026, p.7); GE Aerospace agreed to buy Consolidated Precision Products, which this piece lists as an independent caster (announced 8 Sep 2026, close expected 2H 2027; press coverage only, release not retrieved); SpaceX plans a blade and vane foundry at Bastrop (press only). GE Vernova already says it has "secured significant supply chain capacity" for 30 GW (22 July call).
- Overlap: ge-vernova-sells-the-wait already says "the pace is set by castings and forgings". Without a primary date the narrowed claim adds a named supplier, not a new mechanism. A distinct angle would be the race to own casting capacity (Siemens Florida, GE Aerospace and CPP, SpaceX), but that is a different piece and needs its own primary sourcing.

## Proposed claim

GE Vernova's step beyond 24 gigawatts to 30 gigawatts a year rests on blade casting capacity that Howmet Aerospace, the largest maker of gas turbine blades, is adding from 2028 to 2030, so the 30 gigawatt year arrives no sooner than that capacity does.

### Alternatives considered

1. Single-crystal blades are the specific choke point. Rejected: Howmet's own chief executive said on 6 August 2026 that single crystal is under 5 per cent of industrial gas turbine blades, with the market split roughly equally between equiaxed and directionally solidified parts. The outline's "grown as one crystal" mechanism was therefore broadened to "grains run lengthways, or a single crystal".
2. Howmet's gas turbine sales will double in three to five years (its own Technology and Markets Day target, about $1bn in 2025 to $2bn+). Rejected: that is a company revenue forecast, which would turn the piece into a view on Howmet's growth rather than on the physical gate.

Chosen because it makes the caster the subject and the gate, which ge-vernova-sells-the-wait gives only one clause ("the pace is set by castings and forgings"), and it is tested on two companies' own stated dates. It builds on, and does not contradict, the-way-out-has-its-own-queue (the escape route is a queue) and ge-vernova-sells-the-wait (the queue is kept on purpose; this piece says what physically paces the expansion).

Note on the falsifier as outlined: the outline suggested "GE Vernova reaches its higher output before Howmet's new capacity comes on". GE Vernova's own call (22 July 2026) says castings and forgings arriving in 2027 support the 24 GW step in 2028, so a 24 GW test would be met by design and is not a fair test. The falsifier uses the 30 GW step instead, against Howmet's 2028 to 2030 additions, plus a second, supplier-side test.

## claims.ts entry

```ts
  {
    id: 'howmet-casts-the-queue',
    claim: 'GE Vernova\'s step beyond 24 gigawatts to 30 gigawatts a year rests on blade casting capacity that Howmet Aerospace, the largest maker of gas turbine blades, is adding from 2028 to 2030, so the 30 gigawatt year arrives no sooner than that capacity does.',
    breaksIf: 'GE Vernova reaches an annualised gas turbine output of 30 gigawatts on its 2030 timetable while Howmet says its new gas turbine casting capacity has slipped beyond 2030, or GE Vernova or Siemens Energy says castings no longer limit how fast it can raise output.',
    watch: ['GE Vernova gigawatts shipped each quarter against its 24 and 30 GW steps', 'Howmet statements on when new gas turbine casting capacity (Japan, Europe, Virginia) comes on, and any slip past 2030', 'Whether GE Vernova or Siemens Energy still name castings as what paces their ramp', 'Howmet gas turbine revenue growth each quarter'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"). Suggested position: after `ge-vernova-sells-the-wait`. Its constraint line ("Skipping the grid queue means joining the queue for the equipment instead") fits: this piece is the queue under the equipment queue. No new layer needed.

## Glossary (heading "Getting power to the building")

- `Investment casting`: Making a metal part by pouring molten metal into a ceramic shell formed around a wax copy that is then melted out. How turbine blades with internal cooling channels are made, by a handful of specialist foundries.
- `Directionally solidified`: A cast blade cooled so its metal grains all run along its length, which makes it far stronger at high temperature. A single-crystal blade goes further and has no grain boundaries at all.
- `Superalloy`: A nickel-based metal designed to keep its strength close to its melting point. The material of the hottest turbine blades.
- `Thermal barrier coating`: A thin ceramic layer sprayed on a turbine blade as a heat shield, so the metal beneath stays cooler than the gas around it.

(Existing entry "Castings and forgings" already covers the general term.)

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '2028 to 2030', what: 'When Howmet says its larger new gas turbine blade casting capacity comes on (equipment ordered in August 2026 adds capacity in August 2028 at the earliest; said on its call, press transcript only).', piece: 'howmet-casts-the-queue', asOf: '6 August 2026' },
```

## LinkedIn post (§9)

GE Vernova's climb to 30 gigawatts of gas turbines a year waits on another company's furnaces.

Howmet Aerospace, the largest maker of gas turbine blades, said on its August call that equipment ordered then adds capacity in August 2028 at the earliest, with larger additions across 2028 to 2030. GE Vernova says castings arriving in 2027 carry its 2028 step; the step after rests on that new foundry capacity. If AI campuses are counting on new turbines, the date that matters is when the blades get poured.

I cover why the blade is the hard part, what the turbine maker and the caster both say, and what would prove me wrong.

https://thephysicallayer.fyi/journal/howmet-casts-the-queue/

#GasTurbines #AIInfrastructure #Energy

## Fact-check changes, 29 Oct 2026

- Grain structure limited to "most of the hottest" blades (lengthways grains), "a small share" single crystal, ordinary blades equiaxed (deck p.22; Plant: equal split equiaxed and DS, single crystal under 5%).
- Cold open now uses Howmet's own deck wording, "largest maker of gas turbine blades in the world" (p.12). The more-than-half share, "equipment ordered that month would add capacity in August 2028 at the earliest" and "2028 to 2030" are attributed to Plant on the 6 August 2026 call (press-only copy).
- Dropped "a new blade furnace takes about two years" (he said "the next piece of machine equipment"). Dropped the yield-growth remark as a company statement; the How section's point that a foundry can grow by wasting less is my inference about the mechanism.
- Temperature now "above 1,400 degrees Celsius" (DOE figure is GE's H System, 2000).
- How section rewritten in a new order (yield, casting, structure, then supply), away from the video's sequence.
- Claim narrowed to the 24 to 30 GW step, since GE Vernova says 24 GW rests on castings arriving in 2027 and it has "already secured significant supply chain capacity" for 30 GW. Falsifier in the piece and claims.ts now match.

## Figures in the body, with sources

- 30 GW a year by 2030, 24 GW in 2028, 20 GW now ("half as much again"): GE Vernova 2Q 2026 call, 22 July 2026 (CEO Scott Strazik prepared remarks): "reached our 20-gigawatt annualized run rate and are on track for 24 gigawatts in '28 ... 30 gigawatts of annual output in '30". Primary (GE Vernova's own transcript PDF). 3Q 2026 release, 28 Oct 2026, consistent: shipped 5 GW in the quarter (a 20 GW a year pace); 122 GW under contract. The 3Q release itself does not restate the 20/24/30 steps; I could not retrieve a 3Q call transcript (the expected gevernova.com URL returned 404), so the steps rest on the July call.
- "castings and forgings arriving in '27" for 24 GW in 2028: same GE Vernova 22 July 2026 call, Strazik. Primary. This is the one direct quote in the piece.
- More than half of the world's industrial gas turbine blades: Howmet Q2 2026 call, 6 August 2026, John Plant (Executive Chairman and CEO) in Q&A: "Howmet Aerospace has a market share in excess of 50% globally for turbine blades in the IGT markets". Howmet's own figure, attributed. PRESS-ONLY COPY: read from the Benzinga transcript as mirrored by Webull; Howmet does not post call transcripts. Howmet's own Technology and Markets Day deck (10 March 2026, p.12) says, on primary paper, "Howmet is the largest manufacturer of gas turbine blades in the world". If Tommy wants primary-paper only, swap the cold open line to "Howmet Aerospace says it is the largest maker of gas turbine blades in the world".
- New capacity committed now arrives August 2028 at the earliest; larger additions across 2028, 2029 and 2030; wait for new equipment about two years; growth mainly from yield on the existing asset base: same Howmet 6 August 2026 call, Plant ("you can say it's earliest August of '28"; "really we're looking at 2028, 2029, and even the more recent ones '29 into 2030"; "mainly from achieving yield improvements on the existing asset base"). PRESS-ONLY COPY, as above.
- Gas turbine sales up 38 per cent in the second quarter: Howmet Q2 2026 earnings release (8-K exhibit 99.1, 6 August 2026) and Q2 2026 earnings presentation; 10-Q table gives $321m against $233m. Primary.
- Above 1,400 degrees Celsius in the largest machines (DOE figure is GE's H System, 2000): US Department of Energy, "Breakthrough" Gas Turbines (H System, firing temperature 2,600 degrees F, about 1,430 C; "Above 2300 degrees F, available cooling technologies were insufficient to protect the turbine blades"). Primary (agency).
- Grains run lengthways or single crystal, hollow cored blades with cooling channels, ceramic coatings, Howmet builds its own furnaces and tools: Howmet Technology and Markets Day, 10 March 2026, pp.20 to 24 (equiaxed, directionally solidified and single crystal structures; cored, multi-wall cooling; thermal barrier coatings; "Build In-House our Own Furnaces, Equipment & Tools"; new DS casting furnaces in Exeter, UK and Nomi, Japan). Primary.
- Few independent foundries (Precision Castparts owned by Berkshire Hathaway, Doncasters, Consolidated Precision Products): Howmet 2025 Form 10-K, filed 12 February 2026, "Competitive Conditions". Primary. The same section notes "Several of Howmet's largest customers have captive superalloy furnaces", which is why the piece says "independent" foundries and the falsifier allows for blades "coming from somewhere else".
- "each new blade design has to be proved with the turbine maker before it ships": general industry practice; Howmet's markets day deck lists qualifications as milestones and its CEO refers to "new project introductions over the next two or three years". No duration is stated in the piece because none was verified.

## Every source, with URL and date

- Howmet Aerospace Form 10-K for 2025, filed 12 February 2026: https://www.sec.gov/Archives/edgar/data/4281/000000428126000012/hwm-20251231.htm (also https://www.howmet.com/wp-content/uploads/sites/3/2026/05/yearend202510k.pdf)
- Howmet Aerospace Technology and Markets Day, 10 March 2026: https://www.howmet.com/wp-content/uploads/sites/3/2026/03/Howmet-Aerospace-Technology-and-Markets-Day-2026.pdf
- Howmet Aerospace Q2 2026 earnings release (8-K exhibit 99.1), 6 August 2026: https://www.sec.gov/Archives/edgar/data/0000004281/000110465926091610/tm2622325d1_ex99-1.htm
- Howmet Aerospace Q2 2026 earnings presentation, 6 August 2026: https://www.howmet.com/wp-content/uploads/sites/3/2026/08/Howmet-Aerospace-2026-Q2-Earnings-Presentation.pdf
- Howmet Aerospace Form 10-Q for the quarter ended 30 June 2026, filed 6 August 2026: https://www.sec.gov/Archives/edgar/data/4281/000000428126000025/hwm-20260630.htm
- Howmet Aerospace Q2 2026 earnings call transcript (press copy, Benzinga via Webull), call of 6 August 2026: https://www.webull.com/news/15750768953811968
- GE Vernova 2Q 2026 earnings call transcript, 22 July 2026: https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf
- GE Vernova 3Q 2026 earnings release (8-K exhibit 99), 28 October 2026: https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm
- GE Vernova Form 10-Q for the quarter ended 30 September 2026, filed 28 October 2026 (checked; no capacity targets in the retrieved text): https://www.sec.gov/Archives/edgar/data/1996810/000199681026000163/gev-20260930.htm
- US Department of Energy, DOE Technology Successes, "Breakthrough" Gas Turbines (undated page): https://www.energy.gov/node/612326
- Lead only: YouTube, "GE Vernova Explained: The Power Bottleneck Behind the AI Boom" (Leo Cui), https://www.youtube.com/watch?v=TiHQJVK9Kk4, transcript in research-build/source-watch-later/ge-vernova-power-bottleneck/TRANSCRIPT.md

## Video figures dropped or flagged

- "Howmet ... says it supplies more than half of the world's industrial gas turbine blades": CONFIRMED as Howmet's own figure (Plant, 6 Aug 2026 call, "in excess of 50%"), but only from a press transcript copy; Howmet's own deck says "largest manufacturer". Flagged, see above.
- "adding capacity that arrives between 2028 and 2030": CONFIRMED by Plant on the same call (press copy). Kept, with the more precise "August 2028 at the earliest".
- "gas that GE has said exceeds 2,600 degrees Fahrenheit, hotter than the metal could survive unprotected": GE's own statement not located. Replaced with the DOE figure (2,600 F, about 1,400 C) and "hotter than bare metal could survive". The outline's "hotter than the metal's melting point" was NOT verified against a primary source and is not used.
- "each blade is cast as a single metal crystal": FLAGGED AS MISLEADING for IGT. Howmet's CEO says single crystal is under 5 per cent of IGT blades. Piece says grains run lengthways or a single crystal.
- "only a handful of suppliers can do it at scale": supported in substance by Howmet's 10-K competitor list; worded as "a handful of foundries" and "a few independent foundries".
- GE Vernova "about 20 gigawatts a year": confirmed (22 July call; 5 GW shipped in 3Q 2026).
- Video's 2018 GE blade oxidation problem, the 78 GW to 40 GW market collapse, the $22bn goodwill write-down and margin history: not used (history of GE, not the casting gate; not verified).
- Video's transformer, grid connection and Nadella "warm shells" points: not used (covered by other pieces).

## Checks

- `python3 brand/check-piece.py src/content/journal/howmet-casts-the-queue.md`: 0 failures, 0 warnings.
- Body 535 words (729 including exposure map and sources).
