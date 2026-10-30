# Sidecar: contracted-energised-running (deep piece 11 of 11)

Cluster 11, "Contracted, energised, running: how AI campuses really arrive" (operators layer). Drafted 30 Oct 2026 to BRIEF-DEEP.md, matching the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/contracted-energised-running.md` (draft: true). Kept outside `src/content/journal/`. Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "Contracted, energised, running: how Abilene, Nebius and Jane Street's AI capacity really arrives" (names all three subjects, per CLAUDE.md "the subject stays the subject").
- Top layer: about 471 words, 10 figures, 0 company financial figures, no Oracle transcript figure. Analogy about 73 words.
- Investor layer: about 2,410 words before the exposure map; exposure map about 120 words with the exact disclaimer pair.
- `brand/check-piece.py` on a scratch copy: 0 failures, 0 warnings. (Two quoted US spellings, "energized" and "data centers", were paraphrased out to pass.)
- Layout still needs CSS for `hr.layer` and `p.layer-label` (as the prototype sidecar notes).

## Frontmatter notes

- `date: 2026-09-25` is a placeholder only (the earliest absorbed live date, power-first-chips-last). At go-live it becomes the real publish time. Both live claims keep their own dates through the `date` field already in claims.ts.
- New slug `contracted-energised-running`. No absorbed slug is kept, because none names the cluster.
- `cover: "/covers/abilene-switched-on-in-stages.svg"` (existing file) until a new cover is drawn; proposal below.
- Tags: power, data-centres, neocloud, grid (all existing).

## Thesis and the consistency fix

Thesis: an AI campus arrives in five stages (announced or contracted, under construction, energised, delivered, running). Energised is the last stage the builder controls; only running is computing. How fast running follows energised depends on the tenant.

The fix the coordinator asked for, made openly in the section "Abilene and Johor: energised is not the same as running":
- The Abilene draft's "Johor is short of connections, not chips" is quoted and withdrawn, citing the-queue-not-the-chip's Tenaga figure (1,256 MW drawn against 5.65 GW booked, about 22%, June 2026, Malaysia-wide; Johor 29 of 61 projects, 5.6 of 8.3 GW secured).
- The draft's "in months" is kept only where shown: at Abilene the tenant's GB200 racks arrived in June 2025, the window Crusoe gave for energising the first two buildings, so chips came with the power. It is not generalised.
- A three-column table (Abilene, Nebius, Johor) shows why they differ: who fills the hall, how the builder is paid (DayOne take-or-pay with power passed through), whether chips need a US licence (BIS, 31 May 2026), and the energised-to-running gap.
- No cause is hung on Malaysia's gap: ramp, overbooking (deputy minister, 13 Oct 2026) and licensed chips are all named, none chosen. Bold line: "Energised is necessary but not sufficient."

## Claims on record: notes

- nebius-paid-for-what-is-switched-on: "Where I was wrong". Buyers pay for active power, not connected; this repeats the correction already published in the Nebius note (6 Oct 2026). 800 MW test unresolved until end-2026 results. Prepayments have not faded (about 70% of Q2 2026 deals, "an all-time high").
- power-first-chips-last: no later fact cuts against it; the note says it rests on one firm's own account and no outage record exists to test the generator limb. The CoreWeave commitment is noted as consistent.
- abilene-switched-on-in-stages: its proposed claim (sidecar of 29 Oct) never went live and is not in claims.ts. The new deep claim replaces it; nothing to quote.

## New claims.ts entry (existing entries untouched)

```ts
  {
    id: 'contracted-energised-running',
    claim: 'An AI campus\'s capacity arrives in stages, and energised power is the last one its builder controls: at Abilene, whose tenant ordered its chips with the campus, and at Nebius, which installs its own chips under contracts with delivery dates, computing follows the power within months, so contracted or announced gigawatts overstate it, while in Malaysia, where Johor holds two thirds of secured data centre capacity, halls can be energised and let well before they run.',
    breaksIf: 'Crusoe reports the Abilene campus energised or complete by the end of 2026 but Oracle has not reported all eight buildings delivered to its customer by its results for the quarter ending 28 February 2027, or Nebius reports at least 800 megawatts connected at the end of 2026 but, at 30 June 2027, reports active power below 800 megawatts or, if it reports no active figure, annualised revenue below US$9.6 billion, 800 megawatts at its stated 2026 base of US$12 million a megawatt.',
    watch: ['Oracle\'s Abilene delivery figures in its December 2026 and March 2027 results (Oracle reports delivery, not running, by site)', 'Any Crusoe statement that phase two is energised or complete', 'Nebius connected power at the end of 2026, and active power or annualised revenue at 30 June 2027 (about 170 MW active and US$1.25bn, end 2025; US$3.0bn, June 2026)', 'Tenaga\'s data centre load against booked maximum demand (1,256 MW against 5.65 GW, June 2026)'],
  },
```

At merge, the two live entries gain only `home: 'contracted-energised-running'`; `claim`, `breaksIf`, `watch` and `date` are untouched (both already carry `date`). The Nebius research note keeps pointing at `nebius-paid-for-what-is-switched-on`.

Why the tests are real: Oracle's June timetable put the last Abilene buildings in its quarter to 30 Nov 2026, and Crusoe expects completion by end 2026, so a slip to after March 2027 is a clear miss. That limb tests delivery, the nearest stage Oracle publishes, and the piece says so. For Nebius (revised after fact-check), the test is six months after the connected guide falls due: active power below 800 MW at 30 June 2027, or, if no active figure, annualised revenue below US$9.6bn (800 MW x the stated US$12m 2026 base). Because new deals price at US$20m or more, revenue below US$9.6bn means fewer than 800 MW billing, so the test isolates lag from price. The claim makes no causal call on Johor; its fill test lives in the-queue-not-the-chip's claim (under 40% at June 2027), so it is not duplicated here.

Alternatives considered: (A) "only energised megawatts count" (the Abilene draft): contradicted by Johor and by Nebius's own connected-to-active lag. (B) a Nebius active-power test alone: Nebius has reported active power only once (end 2025), so not reliably observable. (C) a market-wide "under construction overstates" claim: no primary observable.

## Redirect map

| Old URL | Redirect to |
|---|---|
| /journal/nebius-paid-for-what-is-switched-on/ | /journal/contracted-energised-running/#nebius-paid-for-what-is-switched-on |
| /journal/power-first-chips-last/ | /journal/contracted-energised-running/#power-first-chips-last |
| /journal/abilene-switched-on-in-stages/ | /journal/contracted-energised-running/#abilene-switched-on-in-stages (scheduled draft, never live; redirect optional) |

The Abilene publish task (scheduled) must be paused or retired at merge, or it will publish the draft with the withdrawn Johor line. Its LinkedIn post in brand/linkedin-posts.md should be dropped. Originals go verbatim to `research-build/archive/pieces/`.

Sections and anchors, in order: How it works; The number that matters; The mechanism in depth; Abilene (#abilene-switched-on-in-stages); Nebius (#nebius-paid-for-what-is-switched-on); Jane Street (#power-first-chips-last); Abilene and Johor; Claims on record; What would prove me wrong; Research notes.

## stack.ts

Layer `operators` ("Who runs the capacity"); its constraint line, "Buyers pay for megawatts switched on, not megawatts signed", still fits. At merge:
`pieces: ['contracted-energised-running']`

## Glossary (src/pages/glossary.astro)

"Getting power to the building":
- Contracted power: Power a data centre builder has secured rights to, through land and power commitments. Nebius's term; it says nothing about whether a building exists.
- Connected power: Power wired into fully built and equipped data centres. Nebius's term; it comes before the chips run.
- Active power: Power drawn by installed, running computers and available to earn revenue. Nebius's term; the stage customers pay for.
- Delivered capacity: Data centre capacity handed over to the tenant who will run computers in it. It comes after a building is energised and before the computers run at full load.
- Capacity in service: A builder's term for capacity ready for customers and fully fitted out. DayOne counts it separately from capacity merely energised.
- Prepayment: Money a customer pays before capacity is delivered, often covering part of the cost of building it.
- Annualised revenue (run-rate): The last month's revenue times twelve, so it counts only what is billing that month.

Existing `Announced versus energised megawatts`: suggest adding "Abilene shows the difference: work began in 2024, and its buildings were energised and handed over across 2025 and 2026." Already present otherwise: Substation, Transformer, Maximum demand (added by the prototype), Export licence (prototype).

## numbers.ts (physical only)

Keep the existing `5 GW vs ~1 GW` entry, repointing `piece` to `contracted-energised-running` (the redirect also works). New:
```ts
  { layer: 'operators', value: '6 of 8', what: 'Buildings at the Abilene, Texas AI campus Oracle said it had delivered to its customer, 618 MW and about three quarters of capacity, more than two years after work began in June 2024. From Oracle\'s results call, as transcribed.', piece: 'contracted-energised-running', asOf: '10 September 2026' },
  { layer: 'operators', value: '~170 MW', what: 'Active power at Nebius at the end of 2025, power drawn by running computers, against more than 2 GW contracted by February 2026.', piece: 'contracted-energised-running', asOf: 'end of 2025' },
```

## LinkedIn post (§9)

```
Nebius has signed rights to 5 gigawatts of power for the end of 2026. It expects 0.8 to 1 gigawatt connected, and at the end of 2025 about 170 megawatts were running chips.

Every AI campus passes five stages: announced, under construction, energised, delivered and running. At Abilene, Texas, the tenant's chips arrived with the power. In Malaysia, connected data centres drew about 22% of the power they had booked in June. Power switched on is necessary. It is not enough.

The piece sets Abilene, Nebius and Jane Street side by side, stage by stage, with the claims I have on record and where I was wrong.

https://thephysicallayer.fyi/journal/contracted-energised-running/

#DataCentres #AIInfrastructure #Power
```

## Cover proposal (not drawn)

`/covers/contracted-energised-running.svg`. A staircase of five steps seen side-on, labelled in letter-spaced grey: CONTRACTED, BUILT, ENERGISED, DELIVERED, RUNNING. Steps one to three in dark outline with a thin amber cable rising along them; only the top step holds a lit row of small blue chip squares. A faint second staircase behind it stops, lit amber, at ENERGISED with empty squares (Johor). Caption: "CONTRACTED, ENERGISED, RUNNING". Background `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Sources, every one with date

Re-opened by me on 30 Oct 2026:
- Nebius Q4 2025 shareholder letter, 12 Feb 2026 (about 170 MW active against 100 MW target; more than 2 GW contracted; 800 MW to 1 GW connected guide; ARR US$1.25bn): https://www.sec.gov/Archives/edgar/data/1513845/000110465926013946/tm266173d1_ex99-2.htm
- Nebius Q1 2026 shareholder letter, 13 May 2026 (definitions of contracted, connected, active; contracted capacity exceeds 3.5 GW; owned over 75%; connected guide kept; ARR definition): https://www.sec.gov/Archives/edgar/data/1513845/000110465926059872/tm2614392d1_ex99-2.htm
- Nebius Q2 2026 shareholder letter, 12 Aug 2026 (5 GW contracted target; ARR US$3.0bn; 70% of deals with prepayments covering 50 to 60% of capex; over US$9bn prepayments expected in 2026; US$20 to 25m per MW; "2026 base $12M"; capacity arriving late 2026, revenue primarily 2027; all Microsoft tranches delivered; second Meta capacity early 2027; guidance reaffirmed): https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-2.htm
- Nebius Form 6-K on the Microsoft agreement, 8 Sep 2025 (about US$17.4bn through 2031; tranches 2025 and 2026; termination right and liquidated damages for late delivery): https://www.sec.gov/Archives/edgar/data/1513845/000110465925088312/tm2525580d1_6k.htm
- Nebius Form 6-K, 22 Oct 2026 (US$3.5bn bridge loan; no power figures; not used in the body): https://www.sec.gov/Archives/edgar/data/1513845/000110465926117978/tm2628078d1_6k.htm
- Oracle results release, 10 Sep 2026, Exhibit 99.1 (850 MW additional data centre capacity delivered in the quarter; more than 300,000 GPUs delivered; no Abilene figures): https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/orcl-ex99_1.htm
- Crusoe, 30 Sep 2025 (construction June 2024; first two buildings energised within a year; first GB200 racks June 2025; first phase running): https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live
- Crusoe, Blue Owl and Primary Digital, 21 May 2025 (phase one two buildings 200+ MW from June 2024, energised H1 2025 expected; phase two six buildings from March 2025, energised mid-2026 expected; 1.2 GW): https://www.crusoe.ai/resources/newsroom/crusoe-blue-owl-capital-and-primary-digital-infrastructure-enter-joint-venture
- Crusoe, 27 Mar 2026 (two 100 MW buildings energised in under a year; phase two completion by end 2026): https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
- Jane Street write-up of its newest data centre, undated page (4,032 GPUs, 56 racks, whole grid interconnect wattage in a small fraction of the space): https://www.janestreet.com/culture/street-view/a-look-inside-our-newest-data-center/
- CoreWeave, 15 Apr 2026 (Jane Street committed about US$6bn; the release's equity price is deliberately not used): https://coreweave.com/news/jane-street-signs-6-billion-ai-cloud-agreement-with-coreweave

From earlier sidecars or live pieces (verified there, not re-opened today):
- Crusoe, 18 Mar 2025 (1.2 GW grid interconnection; turbines for backup; Lancium): https://www.crusoe.ai/resources/newsroom/crusoe-expands-ai-data-center-campus-in-abilene-to-1-2-gigawatts
- Oracle calls of 10 Jun 2026 (42% delivered; 35% within 90 days; rest the following quarter) and 10 Sep 2026 (6 of 8 buildings, 618 MW, 75%; 131,000 GPUs), SECONDARY, via The Motley Fool transcripts: https://www.fool.com/earnings/call-transcripts/2026/06/10/oracle-orcl-q4-2026-earnings-call-transcript/ ; https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/
- Jane Street podcast with Dwarkesh Patel, Yaron Minsky and Dan Pontecorvo, published 21 May 2026 (as sourced in the live piece power-first-chips-last; video linked from Jane Street's page: https://www.youtube.com/watch?v=xKZ_8ULR91Y). I did not re-watch it.
- Tenaga Nasional Analyst Briefing 2QFY2026, 28 Aug 2026: https://www.tnb.com.my/assets/quarterly_results/Analyst_Briefing_-_2QFY2026.pdf
- Dewan Rakyat Hansard, 13 Oct 2026: https://www.parlimen.gov.my/files/hindex/pdf/DR-13102026.pdf
- DayOne Form F-1, 5 Oct 2026: https://www.sec.gov/Archives/edgar/data/2118192/000119312526414188/d223752df1.htm
- BIS guidance, 31 May 2026: https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf
- Lead only, credited in the sources line: the YouTube video "State of AI data centres 2026" (transcript at research-build/archive/sources/source-ai-datacentre-video/TRANSCRIPT.md).

## Figures dropped or flagged

- Oracle's Abilene figures (42%, 35%, 618 MW, 75%, 6 of 8, 131,000 GPUs): Oracle's investor site is script-rendered and I found no primary transcript or prepared remarks; its 10 Sep release and 10-Q do not mention Abilene. Kept, labelled in the body as "as transcribed" and in the sources line as The Motley Fool's transcripts. The top layer says "Oracle told investors"; a fact-checker may prefer to cut "six of its eight" from the top layer if a labelled figure is not acceptable there.
- Nebius contracted "more than 1 GW (August 2025)" and the slide history: from a chart whose labels extracted out of order; dropped.
- Nebius connected power actual: never reported; the table says "not given". "Several months" from connection to revenue (Q2 call): call only, not in the letter; the body says only "months, on Nebius's own sequence".
- The 580 to 750 MW billing estimate is my arithmetic from Nebius's figures, labelled as such.
- Cushman & Wakefield (50 / 38 / 285 GW, Americas) and Knight Frank (Johor above 1 GW live, 0.7% vacancy): consultants, not primary under the quality rule; dropped. The Abilene draft's numbers.ts option with C&W is withdrawn.
- OpenAI 23 Sep 2025 Stargate flagship announcement: checked only via press in the Abilene sidecar; not used.
- Bloomberg on Meta selling spare capacity (1 Jul 2026): press; appears only inside the quoted Nebius falsifier.
- ByteDance as DayOne's largest customer: SemiAnalysis's identification; not used, so no credit needed. The F-1's own description is used.
- Crusoe's 1.2 GW and Oracle's 618 MW = 75% (implying about 824 MW) are different yardsticks; the body says so and does not compare them.
- Phase-two energisation dates: not disclosed by Crusoe; none stated.
- Crusoe's 900 MW Microsoft campus next door (first building to be energised mid-2027, on-site power plant): not used; a separate project.
- CoreWeave's US$1bn equity purchase at a stated share price: excluded (share prices never appear in a journal piece).

## Edits other drafts need (not made)

- `src/content/journal/abilene-switched-on-in-stages.md` (scheduled draft): superseded by this piece. Pause its publish task and drop its LinkedIn post at merge; do not publish the "Johor is short of connections, not chips" line.
- `src/data/numbers.ts`: repoint the Nebius `5 GW vs ~1 GW` entry at merge.
- `src/content/calls/nebius.md`: untouched; it links `/journal/nebius-paid-for-what-is-switched-on/`, which resolves via the redirect.
- `room-to-spare` (cluster 8) uses the same Jane Street write-up; no conflict found.

## Could not verify today

- Oracle's Abilene call figures on a primary copy (see above).
- The Jane Street podcast wording (more than a year; six months sooner; TPU half as dense as GB300 NVL72): taken from the live piece, which has no sidecar; I could not fetch a transcript.
- Whether Abilene's phase two is now energised: no Crusoe statement found as of 30 Oct 2026.
- Nebius Q3 2026 results (expected about mid-November) are not out; the 800 MW test is open.

## Fact-check fixes applied (30 Oct 2026)

1. Jane Street: "racks take up the whole grid connection" now attributed to Dwarkesh Patel, quoted in Jane Street's write-up. The TPU versus GB300 NVL72 comparison is dropped: I could not confirm on a primary source whether the podcast said GB200 or GB300.
2. Nebius guidance: the 800 MW to 1 GW connected and US$7 to 9bn run-rate guides are cited to the 12 Feb and 13 May letters. The 12 Aug letter is cited only for "full-year 2026 guidance across all metrics".
3. "Owned sites over 75% of contracted power" removed; that cell now reads "Not reported separately".
4. "Nebius's own sequence" dropped, as it was call-only. The Nebius licence cell now reads "Not disclosed"; the gap cell reads "Not disclosed; a lag on my arithmetic".
5. Claim: Nebius installs its own chips; the Malaysia limb now names Johor's two thirds of secured capacity; "years" is removed from the claim, the top layer, the analogy and the bold line.
6. Falsifier: the Nebius limb is re-dated to 30 June 2027 (active MW, else ARR below US$9.6bn). The Abilene limb is stated as a delivery test in the claim wording and in "What would prove me wrong". The claims.ts entry above matches.
7. Nebius claim note: the prepayment evidence is dated as predating the claim; the third limb is addressed, with Bloomberg's July Meta report marked as press and unconfirmed. Jane Street note: "Since it went live", and the CoreWeave commitment is marked as predating the claim.
8. "Six of its eight" cut from the top layer and replaced with Crusoe's primary end-2026 completion. The "Three cautions" paragraph and the mechanism table's Jane Street column are cut. The exposure map now says Oracle runs Abilene's cloud and OpenAI uses it, Microsoft, Meta and Jane Street rent capacity, and Jane Street also runs its own. A link to /journal/heat-and-water/#room-to-spare is added in the Jane Street section. That deep piece does not exist yet, so the link resolves only once cluster 8 publishes under that slug.

check-piece.py on a scratch copy after the fixes: 0 failures, 0 warnings.
