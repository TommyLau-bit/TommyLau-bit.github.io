# CAISO battery fleet draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/california-still-shifts-the-sun.md` (draft: true)
Cover: `public/covers/california-still-shifts-the-sun.svg`
Drafted 29 October 2026 (batch 3, Tier A item A11, with the reserved PJM accreditation topic folded in). Claim needs Tommy's approval before publish.
Checker: 0 failures, 0 warnings. Body about 515 words, 0 money figures. Revised 29 Oct after fact-check (causation, Tommy's wording, PJM dating, falsifier threshold). `npm run build` passed (249 pages).

## Read this first: the counter-case to Tommy's own claim

The brief asked for this to be said openly. The piece says it in its first line and again at the end of the evidence section, and links to `what-the-battery-is-really-for`.

- Tommy's published claim: "Large batteries are increasingly bought as connection equipment that lets a site switch on early, not as a way to trade electricity."
- What CAISO's own data shows: California's fleet (about 17.3 GW installed, 30 Sep 2026) is a time-shifter. CAISO's market monitor (2025 annual report, June 2026) finds batteries earned about $35/kW-yr from energy against $9/kW-yr from regulation in 2025, and that battery capacity scheduled for ancillary services "has decreased in favor of energy". Over half of the fleet is physically paired with solar or wind (DMM 2024 battery special report). Batteries were the largest single source at the evening net peak on 66 of 122 summer days in 2026, up from none in 2023.
- My verdict: the evidence weakens Tommy's claim as a general description of grid batteries. It does not refute it as a claim about the newest buyers beside data centres. His wording is "increasingly" and "becoming", and the piece quotes it that way and says openly that it narrows his claim to those buyers. A second caution for Tommy: the evidence his piece uses, Texas taking 53% of 2026 planned additions (EIA), is mostly grid-scale ERCOT batteries, which also trade; I did not verify how much of it sits at data centre sites, and nobody publishes that split. I recommend Tommy reads this before approving, because once both pieces are live the site openly carries the qualification.
- Separate flag: the published battery piece's exposure map still names the system builder whose own piece Tommy took down (first name under "The system builders"). I have not touched that file.

## Proposed claim

California's batteries are still time-shifters, not connection equipment: they already lead CAISO's evening net peak on most summer days, but the fleet does not grow with a heatwave, so through summer 2027 gas still leads on at least eleven of the twelve hardest evenings, and a battery's worth depends on when each grid's risky hours fall, as PJM's seasonal ratings show.

### Alternatives considered

1. The outline's own claim, "by summer 2027 batteries are the largest single source on the evening net peak on most days". Rejected: CAISO's five-minute data shows it already happened in summer 2026 (66 of 122 days, every day in June), so it is no longer a forecast and could not be proved wrong.
2. "PJM's accreditation of four-hour batteries falls as more join" (the reserved topic) as a standalone piece. Rejected as the lead: PJM's binding ratings have moved up and down (50%, 58%, 59%, 57% for 2026/27 to 2029/30), so "falls as more join" is only true of PJM's non-binding outlook; on its own it is thin. Folded in, it becomes the second half of one mechanism: the same battery is worth 94% against PJM's summer risk and 43% against its winter risk.

Chosen because what is new is my own: the five-minute count across four summers, the finding that the fleet does its usual work on the hardest evenings while gas takes the whole of the heatwave's extra demand, and PJM's 94% against 43% seasonal split. The general idea that a battery's value depends on duration against the risky hours is the video's thesis, so the piece leads with the count and the PJM split, not with that idea. It rests entirely on CAISO and PJM data and tells a PM what the headline ("batteries now run California's evenings") leaves out.

## claims.ts entry

```ts
  {
    id: 'california-still-shifts-the-sun',
    claim: 'California\'s batteries are still time-shifters, not connection equipment: they already lead CAISO\'s evening net peak on most summer days, but the fleet does not grow with a heatwave, so through summer 2027 gas still leads on at least eleven of the twelve hardest evenings, and a battery\'s worth depends on when each grid\'s risky hours fall.',
    breaksIf: 'From June to September 2027, batteries are the largest source at CAISO\'s evening net peak on two or more of the twelve evenings with the highest net load, or PJM\'s ELCC class rating for four-hour storage in its 2030/2031 Base Residual Auction is 57 per cent or higher.',
    watch: ['CAISO Today\'s Outlook five-minute fuel mix at the daily net peak, June to September 2027', 'CAISO installed battery capacity in its monthly Key Statistics', 'PJM\'s ELCC class ratings for the 2030/2031 Base Residual Auction, due to be calculated in December 2026 and January 2027', 'Whether CAISO\'s market monitor reports battery revenue shifting from energy towards capacity or connection uses'],
  },
```

## stack.ts

Layer `grid` ("The grid connection"), after `pjm-sends-the-bill`. These are grid-scale batteries serving the public grid, not batteries beside a building, so `onsite` (where `what-the-battery-is-really-for` sits) would be wrong. No new layer. If Tommy prefers the two battery pieces side by side, `onsite` is the fallback, but it misdescribes the fleet.

## Glossary (heading: "Getting power to the building")

- **Net peak**: The evening hour when demand minus wind and solar output is highest, which the rest of the grid must cover. In California it arrives around 8pm.
- **Four-hour battery**: A battery that can run at full power for four hours before it needs recharging, the most common size of grid battery in America.
- **ELCC (effective load carrying capability)**: How much of a power source's nameplate size a grid operator counts on during its riskiest hours. PJM uses it to decide how much capacity each kind of plant or battery can sell. (Not used by name in the piece; add only if Tommy wants the term on the glossary for later pieces.)

## numbers.ts (physical figures only)

- CAISO installed battery capacity: 17,307 MW, as of 30 September 2026 (CAISO Key Statistics, September 2026).
- PJM four-hour battery accreditation: 94% against summer risk, 43% against winter risk (PJM estimated seasonal ELCC class ratings for 2026/2027, 13 March 2025).

## LinkedIn post

California's batteries now supply more power than any other source at the evening peak on most summer days.

They do the famous job: charge on midday sun, empty after dark. But on the twelve hardest evenings this year, gas led every time: the batteries did their usual evening's work and the heatwave's extra demand fell to gas. PJM estimates the same battery is worth 94 per cent of its size against summer risk and 43 per cent against winter risk.

The piece covers what the net peak is, what this summer's data showed, and why the same battery is worth less on a grid whose risk sits in winter.

https://thephysicallayer.fyi/journal/california-still-shifts-the-sun/

#EnergyStorage #Grid #California

## Method for my own count (so a checker can reproduce it)

Data: CAISO Today's Outlook fuel source files, `https://www.caiso.com/outlook/history/YYYYMMDD/fuelsource.csv`, every day 1 June to 30 September for 2023, 2024, 2025 and 2026 (488 files, downloaded 29 Oct 2026). For each day: total = sum of all columns (Batteries is net of charging, Imports net); net load = total minus Solar minus Wind; the net peak is the five-minute interval with the highest net load between 16:00 and 22:55. At that interval I compared Batteries with every other column.

Results (Jun to Sep, days on which Batteries was the largest column at the net peak):
- 2023: 0 of 122. 2024: 10 of 122. 2025: 52 of 122. 2026: 66 of 122 (June 30 of 30, July 14, August 4, September 18).
- 2026 median net peak time 20:00. Highest five-minute battery output in the 2026 window 13,441 MW.
- Twelve 2026 evenings with the highest net load: gas larger than batteries on all twelve. Hardest, 9 Sep 2026 at 19:00: net load 45,418 MW, gas 22,286 MW, batteries 10,679 MW, imports 4,991 MW.
- Gap gas minus batteries at the net peak on the twelve hardest 2026 evenings: 2,684 MW (14 Jul) to 11,701 MW (27 Aug). Five of the twelve under 4.3 GW. Batteries at the net peak on those twelve averaged 10,953 MW against 10,318 MW over all 122 days; daily battery discharge averaged 45.9 GWh against 46.7 GWh. So the data shows the fleet doing its usual work on the hardest days, not running dry; the piece no longer claims four hours ran out.
- The twelve cluster in two heatwaves (19 to 27 Aug, 8 to 10 Sep) plus 14 to 15 Jul and 3 Aug. In 2025 the hardest twelve also clustered (21 Aug to 3 Sep, 15 to 23 Sep); gaps 2,664 to 13,110 MW; batteries led none of the hardest 40 in 2025 and one of the hardest 40 in 2026.
- Why the threshold is two of twelve: battery output at the net peak rose about 1.4 GW from 2025 to 2026 and the fleet about 2 GW, against a smallest 2026 gap of 2.7 GW and a second of 3.4 GW. One flip is plausible, two needs a gain like 2024 to 2025's, so it can genuinely go either way. The test depends on summer 2027 weather; a mild summer makes the hardest twelve easier for batteries.
- Cross-check: CAISO demand file for 20 Jun 2026 at 20:00 showed 27,825 MW demand against 28,537 MW summed supply, consistent.
This is my own computation from CAISO's published data, not a figure CAISO states. The piece says "my own count" in the sources line.

## Figures in the piece and their sources

- About 17 GW of batteries: CAISO Key Statistics, September 2026 (17,307 MW installed as of 30 Sep 2026). Primary.
- CAISO runs most of California's grid: CAISO Key Statistics ("Serves ~80% of California demand"). Primary.
- Net peak around 8pm; 66 of 122 days; none in 2023; twelve hardest evenings gas led; 9 September gas about 22 GW and batteries about 11 GW: my count from CAISO Today's Outlook data. Primary data.
- Batteries earned about four times as much from energy as from regulation in 2025 ($35/kW-yr against $9/kW-yr): CAISO Department of Market Monitoring, 2025 Annual Report on Market Issues and Performance, June 2026, executive summary. Primary.
- Fleet grew by about 2 GW in the past year: same DMM report, resource adequacy highlights ("16.8 GW of capacity from battery resources, which is an increase of around 2 GW from last year"). Primary.
- Most CAISO batteries are four-hour: DMM 2024 Special Report on Battery Storage, 29 May 2025 ("Most large-scale storage systems in operation have a maximum duration of 4 hours"). Primary.
- PJM data centres the main reason winter demand is catching up with summer (about 60% of the narrowing gap), and 94% summer against 43% winter for four-hour storage (PJM's estimated seasonal ratings for the 2026/27 delivery year, used as an illustration; the piece dates it March 2025 and says only that risk is shifting towards winter): PJM, "2026/27 BRA IRM, FPR, and ELCC Class Ratings Shift Towards More Winter Risk", Special Planning Committee, 13 March 2025. Primary.
- 57% for four-hour storage (2029/2030 BRA) and the outlook falling (42% for 2030/31, 34% for 2031/32, 19% by 2042/43, non-binding): PJM Members Committee presentation of 19 August 2026, and PJM "Preliminary ELCC Class Ratings for Period Delivery Year 2028/29 to 2042/43" (file dated 4 Sep 2026). Primary.
No figure is press-only.

## Sources

- CAISO Today's Outlook fuel source history, https://www.caiso.com/outlook/history/20260909/fuelsource.csv (pattern for every day, Jun to Sep 2023 to 2026), accessed 29 Oct 2026
- CAISO demand history, https://www.caiso.com/outlook/history/20260620/demand.csv, accessed 29 Oct 2026
- CAISO Key Statistics, September 2026, https://www.caiso.com/documents/key-statistics-sep-2026.pdf (data as of 13 Oct 2026)
- CAISO Key Statistics, August 2026, https://www.caiso.com/documents/key-statistics-aug-2026.pdf
- CAISO Department of Market Monitoring, 2025 Annual Report on Market Issues and Performance, June 2026, https://www.caiso.com/documents/2025-annual-report-on-market-issues-and-performance.pdf
- CAISO Department of Market Monitoring, 2024 Special Report on Battery Storage, 29 May 2025, https://www.caiso.com/documents/2024-special-report-on-battery-storage-may-29-2025.pdf
- CAISO 2026 Summer Loads and Resources Assessment, May 2026, https://www.caiso.com/documents/2026-summer-loads-and-resources-assessment.pdf (background only)
- PJM ELCC Class Ratings for the 2026/2027 BRA, https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/2026-27-bra-elcc-class-ratings.pdf (4-hr storage 50%)
- PJM ELCC Class Ratings for the 2027/2028 BRA, https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/2027-28-bra-elcc-class-ratings.pdf (58%)
- PJM ELCC Class Ratings for the 2028/2029 BRA, https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/28-29-bra-elcc-class-ratings.pdf (59%)
- PJM, IRM, FPR and ELCC for 2029/2030 BRA, Members Committee, 19 Aug 2026, https://www.pjm.com/-/media/DotCom/committees-groups/committees/mc/2026/20260819/20260819-item-05---2029-2030-bra-irm-fpr---presentation.pdf (57%, higher winter risk share)
- PJM Preliminary ELCC Class Ratings DY2028/29 to DY2042/43, https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/preliminary-elcc-class-ratings-for-period-dy28-dy42-elcc.pdf (file dated 4 Sep 2026)
- PJM, 2026/27 BRA IRM, FPR and ELCC Class Ratings Shift Towards More Winter Risk, 13 Mar 2025, https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2025/20250313-special/2026-2027-irm-fpr-elcc-and-winter-risk.pdf
- California Energy Commission, 21,112 MW of battery resources, Aug 2026, https://www.energy.ca.gov/news/2026-08/california-surpasses-21000-megawatts-battery-resources-supporting-states (background, not used: includes out-of-state and behind-the-meter batteries)
- EIA Today in Energy, planned 2026 additions, https://www.eia.gov/todayinenergy/detail.php?id=67205 (context for the counter-case note only)
- Lead: Leo Cui, "The Entire Energy Sector Explained: Oil, Gas, Electricity & the Grid", YouTube, https://www.youtube.com/watch?v=0zZyEF4Cq9U

## Video figures dropped or flagged

- "Battery fleet grew from about half a gigawatt in 2020 to more than 13 by early 2025": confirmed by DMM (500 MW in 2020 to 13,000 MW in Dec 2024) but dropped as out of date; the piece uses CAISO's 17.3 GW of Sep 2026.
- "More than twenty gigawatts of replacement power within roughly three hours": not used. CAISO's record three-hour ramp is 24,567 MW (16 Mar 2026, Key Statistics), but the piece does not need it.
- "PJM credits a four-hour battery at only half of its nameplate": true only for the 2026/27 auction (50%); later binding ratings are 58%, 59% and 57%. The piece uses 57% and the 94% summer against 43% winter split instead. "That credit can decline as more storage enters": true only of PJM's non-binding outlook (42% for 2030/31 down to 19% by 2042/43); the piece frames it as "PJM's own outlook".
- "100 MW four-hour battery can run at 50 MW for eight hours" and "eight-hour or ten-hour period": the video's own illustration, not used.
- "2,060 GW in US interconnection queues" and "one third of primary energy becomes useful service": out of scope for this piece, not used.
- The video's structure (duck curve, belly and neck) and wording were not reused; the analogy (a hot water tank and a houseful of relatives) is my own.
