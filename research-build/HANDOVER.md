# Journal handover

Read this first in every journal session, then CLAUDE.md and WRITING-FORMAT.md. Newest day on top. Rewrite START HERE at the end of each session.

## START HERE (as of Sat 31 Oct 2026, early morning)

- **Every piece is now a story** (Tommy, 30 to 31 Oct). Tommy read the equipment queue and found the merged pieces stapled together. Overnight, with his go for everything, all ten live pieces and Hong Kong were rewritten as stories with charts, the three approved updates were folded into their pieces, and a new memory piece was researched and written. The rules are research-build/deep-pieces/STORY-RULES.md (one spine and claim by paragraph three, argument headings, no company sections, 2 to 4 inline SVG charts, earlier claims kept word for word in a fold). The model is the-equipment-queue. The checker enforces the core. Read STORY-RULES.md before touching any piece.
- **Tommy reads them all on Sat 31 Oct and will say what to change.** Act on his notes first.
- **Standing decision (30 Oct): do not keep modifying what does not need it.** Change a piece only on Tommy's word or new evidence on its mechanism.
- **Investor first, on every page** (30 Oct, in CLAUDE.md): lists and tables before decoration, counts at the top, jump links on long pages.
- New work follows "Two tracks for new work" in CLAUDE.md. Sourcing is WRITING-FORMAT.md §E. Each candidate goes to Tommy as one line before drafting.
- Briefs for agents are in research-build/deep-pieces/: BRIEF-REWRITE.md and BRIEF-STORY-FACTCHECK.md (story format), BRIEF-GAP-SCOUT.md, BRIEF-UPDATE.md, BRIEF-DEEP.md and BRIEF-DEEP-FACTCHECK.md (structure now per STORY-RULES.md).
- Folder map: README.md. History lives in research-build/archive/ and is never edited.

### Workspace layout (cleaned 30 Oct 2026; keep it this way)

| Where | What |
|---|---|
| Top level | CLAUDE.md (rule book), WRITING-FORMAT.md (piece spec), CALLS-SPEC.md (notes spec), README.md (folder map), plus the site's own folders (src, public, brand) |
| research-build/HANDOVER.md | This file |
| research-build/deep-pieces/ | Live working area: the four agent briefs, one sidecar per deep piece (verified sources), gap-*.notes.md, updates/ (approved copies waiting for 4, 6, 9 Nov; can move to archive/ after 9 Nov) |
| research-build/<company>/, BRIEF-note*.md, CHANGELOG.md | Research notes: build scripts and sources, briefs, post-publication corrections |
| research-build/archive/ | History, never edited: pieces/ (61 originals), journal-drafts/ (their old drafts and sidecars), deep-drafts/ (pre-merge deep piece drafts), sources/ (Watch Later and video transcripts), old-images/ (191 unused covers and cards), misc/, plus CONSOLIDATION-PLAN.md, RETIRED-RULES.md, the old short-piece briefs and TEMPLATE-short-skeleton.md |
| public/covers, public/og | Only images a live or scheduled piece uses (11 covers, 10 cards; Hong Kong's card is made at publish) |

### Scheduled jobs (scheduled-tasks; 8:00 Singapore time unless shown, only while the app is open)

| Date | Job | What it does |
|---|---|---|
| Sun 1 Nov 09:00 | research-monthly-marks | Monthly track-record marks for the research notes, for Tommy's approval |
| Sun 1 Nov 09:30 | journal-monthly-sweep | Writes research-build/sweeps/2026-11.md; proposes only |
| Mon 2 Nov | publish-hong-kong-piece | Flips the rewritten hong-kong-has-the-plug live, stamps the claim date, makes its card, schedules LinkedIn post 48 (Mon 7 Dec) |
| Wed 4 Nov | publish-queue-own-power-update | LinkedIn only: schedules post 49 (Wed 9 Dec). The update itself went live in the 31 Oct rewrite |
| Fri 6 Nov | publish-gas-pipe-update | LinkedIn only: post 50 (Mon 14 Dec) |
| Mon 9 Nov | publish-nuclear-fuel-update | LinkedIn only: post 51 (Wed 16 Dec) |

The old hash guards are gone: the three update jobs no longer touch the pieces. research-build/deep-pieces/updates/ is history now and can move to archive/.

LinkedIn company page queue (11:30): posts 38 to 47 Mon 2 Nov to Wed 2 Dec; Constellation post 34 Fri 4 Dec; then 48 to 51 above; memory post 52 (see the day record).

### Open flags for Tommy (not acted on)
- LinkedIn post 52 (memory): scheduled by Tommy on his phone for Mon 21 Dec, 11:30 (31 Oct). Not checked by Claude, since Chrome was not connected; confirm it in the company page's scheduled list at the next Chrome session.
- Memory replaced the "Memory deep piece" candidate flag: it is live (31 Oct).
- Research notes hitachi.md (line 162) and siemens-energy.md (line 159) carry corrected dates; confirm the wording.
- CLOSED 30 Oct: the press-only 72.76% Johor utilisation figure no longer appears as fact in claims.ts watch lists (Tommy: "Yes, fix them"). The two watch items now read as Malaysia's contracted against used load (Hansard, Aug 2026) and as whether the press figure is confirmed at source.
- The 17 Sep 800 VDC note is reversed by powering-the-rack (briefing in its sidecar). Re-read before any call that touches it.
- Two old one-off scheduled tasks from the job-hunt side (linkedin-connections-reminder-5oct, marvell-investor-day-check) are finished but still listed; the app refused deleting them from here. Tommy can delete them in the Scheduled section.

## Sat 31 Oct 2026 (overnight, Tommy's go for everything): what was done

1. **Diagnosis.** Tommy read the equipment queue and found it messy: five old pieces stapled together, a section per company, five claims, tables instead of charts, no story. He asked for every piece to read like a good film: hook, build, climax, an ending that ties it up, with charts.
2. **Study and rules.** An agent took apart eight well-told articles (Construction Physics, Works in Progress, Our World in Data, Epoch AI, SemiAnalysis, plus two wire stories as contrasts): research-build/deep-pieces/STORY-STUDY.md. Distilled into STORY-RULES.md, written into CLAUDE.md ("Every piece is a story") and WRITING-FORMAT.md §D. The checker now fails topic-label headings and fewer than two charts, and ignores charts and folded blocks when counting words.
3. **Charts.** Inline SVG in each piece, themed by the colour tokens (light and dark), classes listed in STORY-RULES.md, styles at the end of global.css. Phones scroll a chart sideways inside its frame. 38 charts in all, every one checked for label overflow and against its source figures.
4. **Pilot: the-equipment-queue** (13aeae7), rewritten by Claude: paradox opening, three charts (years of work, factory timeline, Siemens Energy's shortfall), one claim, four earlier claims folded word for word, evidence tables and corrections in a fold.
5. **The other nine live pieces and Hong Kong**, rewritten by five writer agents to BRIEF-REWRITE.md, each then checked by a separate agent to BRIEF-STORY-FACTCHECK.md (record kept, every number and chart point recomputed, overclaims softened; about 50 fixes in all). Titles changed on america-rations-the-plug, ten-thousand-chips-one-thought, powering-the-rack and hong-kong-has-the-plug (slugs unchanged). the-queue-not-the-chip now leads with the dated the-plug-not-the-chip claim. Commits 092f199, 247fbb8, 143c06f.
6. **The three approved updates** (Johor own power, gas pipe, nuclear fuel) were folded into their rewrites and went live with them. Their 4, 6 and 9 Nov jobs now only schedule LinkedIn posts 49 to 51. Hong Kong's 2 Nov job publishes the rewritten piece. Posts 48 and 50 reworded to match the checked pieces.
7. **New piece: memory-not-maths** (59fb6c1, live 31 Oct 00:02). Spine: when AI writes an answer the chip waits on memory, so memory sets the pace, and from HBM4E the biggest buyer (Nvidia's NVHBM) designs the base of the memory stack. Three charts (maths against bandwidth since the A100, memory per chip, the controller moving into the base die). Claim `memory-not-maths` (two of three makers shipping customer-designed base dies in volume by end 2027). Scouted, written, then fact-checked against reopened primary sources (11 fixes). Layer 06 now has its own piece; glossary adds Memory wall, KV cache, Memory controller, NVHBM; numbers.ts adds two memory figures. LinkedIn post 52 scheduled by Tommy for Mon 21 Dec.
8. **Social cards** bumped to v10 (old v9 in archive/old-images).
9. **Not done / for Tommy:** read the twelve pieces and say what to change. Two pieces were judged "works with reservations" by their checkers: the-chip-supply-chain (a middle beat still tours memory, film and TSMC) and powering-the-rack (Vertiv and TI beats sit close to company sections). contracted-energised-running rests partly on writer arithmetic (Nebius billing range) and Oracle figures from third-party transcripts, labelled as such.

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
7. **Workspace clean-up (end of day).** Everything no longer in use moved into research-build/archive/ (nothing deleted): the original pieces, old drafts and sidecars, pre-merge deep drafts, Watch Later and video transcripts, the consolidation plan, the old short-piece briefs and TEMPLATE.md, and 191 unused cover and card images. The empty "Journals " folder is gone. WRITING-FORMAT.md lost its retired history (640 to 590 lines; history in archive/RETIRED-RULES.md, no live rule changed). CLAUDE.md, README.md (now a folder map) and CALLS-SPEC.md were brought up to date. The six finished journal publish jobs were cleared from the scheduler (their SKILL.md files stay on disk in ~/.claude/scheduled-tasks/, as do the folders of the 24 publish tasks deleted earlier; harmless and not shown in the app). Build and checkers clean; git working tree empty (commit 9c19117). Tommy confirmed the day's work and asked for no further modification for its own sake.
8. **Homepage articles first (a8c9c2e).** Under the hero, every deep piece is listed by layer with its date (text only; Claude's call, from Tommy's investor brief); the map follows as the guided walk. Old card grid and jump chips removed.
9. **Investor-first upgrade across the site (cd00a01; Tommy gave Claude the call and the go).**
   - Research: stat strip (notes, long, short, no call, marking), then the calls table first (company, date, call, price, target, latest, return, status, note and model links; company column sticks on phones), then compact note rows with no thumbnails.
   - Claims: plain header and counts, jump links by layer, claims grouped by map layer, newest first; each shows date and piece above the claim text. Claim ids and wording unchanged.
   - Every deep piece: a "For investors" line under the summary linking to each investor-layer section (built from the headings below the divider; piece files untouched, so the 4, 6, 9 Nov update jobs' hash guards still match).
   - Glossary: plain header with section jump links and counts.
   - Phone header on every page: one compact row (theme button beside the name, tagline hidden), so content starts on the first screen.
   - CLAUDE.md records the rule. Verified desktop and phone, light and dark, no sideways scroll; build and checkers clean; live and confirmed.
10. **Homepage list spacing (79ac2e6, late evening).** Tommy found the list squeezed. CSS only: more space above and between layer rows, between pieces within a layer, and a slightly larger title size. Checked on desktop and phone, in light and dark. Live.
11. **Homepage rows read as articles (0ca23c6).** Each title is split at its colon (or first full stop) into a bold sans headline and a grey line under it, date on the right; no underline until hover. Checked desktop, phone, light and dark. Live.
12. **Memory candidate raised (not started).** Tommy noticed Layer 06 Memory has no piece of its own (it points at the-chip-supply-chain). Candidate put to him: a NEW deep piece on why AI is bound by memory, not maths, and how HBM4's logic base die makes memory a custom part qualified per customer. Not the Micron sold-ahead / three-times-wafer point, which the chip piece and its claim already own. Next step if he says go: gap scout with BRIEF-GAP-SCOUT.md, which must confirm a distinct mechanism and a primary-sourced claim before any drafting.
