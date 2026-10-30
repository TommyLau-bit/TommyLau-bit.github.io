# Journal handover

Read this first in every journal session, then CLAUDE.md and WRITING-FORMAT.md. Newest day on top. Rewrite START HERE at the end of each session.

## START HERE (as of Fri 30 Oct 2026, evening)

- The site is ten deep pieces, one per mechanism cluster, each in two layers (plain English, then "For investors"). An eleventh, Hong Kong, goes live on Mon 2 Nov.
- Nothing needs doing until the scheduled jobs below run. When each one reports, check it: page live, update note showing, LinkedIn post listed at the right time. Any "NOT DONE" goes to Tommy.
- New work follows "Two tracks for new work" in CLAUDE.md: a NEW deep piece for a new mechanism or market, or an UPDATE to an existing one. Ten is not a ceiling. Sourcing method is WRITING-FORMAT.md §E. Each candidate goes to Tommy as one line before any drafting.
- Briefs for agents are in research-build/deep-pieces/: BRIEF-DEEP.md, BRIEF-DEEP-FACTCHECK.md, BRIEF-GAP-SCOUT.md, BRIEF-UPDATE.md.
- Folder map: README.md. Anything old (original short pieces, their drafts and sidecars, pre-merge deep drafts, video transcripts, retired briefs, template and rules, unused images) is in research-build/archive/ and is never edited. Retired rules: research-build/archive/RETIRED-RULES.md. Keep the workspace this way: new history goes into archive/, never back at the top level.

### Scheduled jobs (scheduled-tasks; each runs at 8:00 Singapore time, only while the app is open; all saved in Auto mode)

| Date | Job | What it does | LinkedIn slot it books |
|---|---|---|---|
| Sun 1 Nov 09:00 | research-monthly-marks | Monthly track-record marks for the research notes, for Tommy's approval | none |
| Sun 1 Nov 09:30 | journal-monthly-sweep | Writes research-build/sweeps/2026-11.md; proposes only | none |
| Mon 2 Nov | publish-hong-kong-piece | Flips hong-kong-has-the-plug to live, stamps the claim date, makes the OG card | Mon 7 Dec, post 48 |
| Wed 4 Nov | publish-queue-own-power-update | Copies updates/the-queue-not-the-chip.md over the live piece | Wed 9 Dec, post 49 |
| Fri 6 Nov | publish-gas-pipe-update | Copies updates/building-your-own-power.md over the live piece | Mon 14 Dec, post 50 |
| Mon 9 Nov | publish-nuclear-fuel-update | Copies updates/nuclear-for-ai.md over the live piece | Wed 16 Dec, post 51 |

Each update job first checks the live file still matches the version Tommy approved (git hash). If anyone edits one of those three live pieces before its date, that job stops by design: re-merge by hand or re-point the job.

LinkedIn company page queue (11:30): posts 38 to 47 (the ten deep pieces) run Mon 2 Nov to Wed 2 Dec; Constellation post 34 on Fri 4 Dec; then posts 48 to 51 above. Headings in brand/linkedin-posts.md say which are scheduled.

### Open flags for Tommy (not acted on)
- Research notes hitachi.md (line 162) and siemens-energy.md (line 159) carry corrected dates; confirm the wording.
- The 3,885 MVA / 72.76% Johor utilisation figure is press-only and inconsistent. It still sits in claims.ts watch lists. Tommy is deciding.
- The 17 Sep 800 VDC note is reversed by powering-the-rack (briefing in its sidecar). Re-read before any call that touches it.
- Two old one-off scheduled tasks from the job-hunt side (linkedin-connections-reminder-5oct, marvell-investor-day-check) are finished but still listed; the app refused deleting them from here. Tommy can delete them in the Scheduled section.

## Fri 30 Oct 2026: what was done

1. **Constellation went live (morning).** The piece was published at 11:47 by its scheduled job. Its LinkedIn post is booked for Fri 4 Dec. The initiation note was drafted with no call (commit 9459e88).
2. **New rule book (13:41, 833a1e5).** The deep piece format replaces the short skeleton: fewer, deeper, layered (WRITING-FORMAT §D). The consolidation plan is research-build/archive/CONSOLIDATION-PLAN.md. The old LinkedIn queue was cleared, and the 20 paused publish tasks were deleted for good.
3. **Consolidation (16:24, 1b05101).** 61 pieces became ten deep pieces:
   - the-queue-not-the-chip
   - america-rations-the-plug (batteries folded in)
   - the-equipment-queue
   - building-your-own-power
   - nuclear-for-ai
   - powering-the-rack
   - heat-and-water
   - ten-thousand-chips-one-thought
   - the-chip-supply-chain
   - contracted-energised-running

   60 old URLs redirect to anchored sections. Every claim is kept word for word, with its date and a `home`. The originals are archived in research-build/archive/pieces/. Claims never published (pjm, seagate, water) were dropped.
4. **Site coherence (16:44, 3588c68).**
   - Dates are the honest first-published dates.
   - The homepage is the map, grouped by layer, and the "latest" feature is gone.
   - The menu is Journal / Research / Claims / Glossary / About. Start here was removed and the companies list trimmed.
   - Research notes now link to their deep pieces.
   - The OG cards are v9.
   - LinkedIn posts 38 to 47 were scheduled.
5. **Two-track rule (17:04, ff3671a).** It was written into CLAUDE.md and WRITING-FORMAT §E, and the monthly sourcing sweep task was set up (1st of each month, 09:30, proposes only).
6. **Gap research, then "All four", approved by Tommy and scheduled at his request (18:07, 298cb97).**
   - **NEW: hong-kong-has-the-plug,** "Hong Kong has the plug, and the chip needs a licence". Claim: CLP completes the 18 data centre substations in its 2024 to 2028 plan by 31 Dec 2028, and Sandy Ridge's first phase is energised by 31 Dec 2027. The old margin claim was dropped as near-certain. It sits in the grid layer, with three glossary terms and three numbers. It is committed as a draft, hidden from the site until 2 Nov.
   - **UPDATE: the-queue-not-the-chip.** New section on whether Singapore and Malaysia halls can build their own power. In Singapore it is legal but no way round the licensed-megawatt ration. Gas use would be 1 to 2% of regas capacity. Malaysia steers data centres to their own solar, with no export (Hansard 28 Oct, primary). The proposed new claim was dropped as a near-duplicate.
   - **UPDATE: building-your-own-power.** The gas pipe's contract clock: Transco SSE takes about 4 years, Kinder Morgan's Permian Link is due Q3 2030, and Williams' Socrates plants are covered. No new claim, because it could not be marked.
   - **UPDATE: nuclear-for-ai.** The EIA uranium contract book, HALEU allocations, and Kairos's Hermes 1 fuel contract. No new claim.

   Each went through drafting, a separate fact-check, fixes, and Tommy's OK. The approved copies and change lists are in research-build/deep-pieces/updates/, and the scout notes are research-build/deep-pieces/gap-*.notes.md.
7. **Workspace clean-up (end of day).** Everything no longer in use moved into research-build/archive/ (nothing deleted): the original pieces, old drafts and sidecars, pre-merge deep drafts, Watch Later and video transcripts, the consolidation plan, the old short-piece briefs and TEMPLATE.md, and 191 unused cover and card images. The empty "Journals " folder is gone. WRITING-FORMAT.md lost its retired history (640 to 590 lines; history in archive/RETIRED-RULES.md, no live rule changed). CLAUDE.md, README.md (now a folder map) and CALLS-SPEC.md were brought up to date. The six finished journal publish jobs were cleared from the scheduler.
