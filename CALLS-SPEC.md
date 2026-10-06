# Claims and Calls: the second core of the site

Agreed with Tommy on 6 Oct 2026. **Read this before any work on pitches, calls or the claims page.**
Status: LIVE 6 Oct 2026. First two pitches published with Tommy's calls: Vertiv LONG, target US$300, medium conviction; Nebius NO CALL, medium conviction.

## Why this exists

The site does two jobs.

1. **The journal (unchanged).** Welcomes new readers to data centre infrastructure and energy, and explains it simply, with analogies. This stays the core.
2. **Claims and Calls (new).** Does the job Tommy is trying to land: a buy-side analyst's work. Research a company or piece of infrastructure, form a view, write the pitch a PM would read, make the call. Boris Petersik (Tantallon CIO, call of 5 Oct 2026) put it this way: a journal only stays a journal if you let it.

## The structure

- **One page, `/claims`, becomes "Claims and calls".** The top menu stays at five items (Journal, Map, Claims, Glossary, About); only the page title changes. Each journal claim is listed exactly as published, with its pitch (if any) linked underneath it.
- **A pitch page per call** (proposed route `/calls/<slug>`), in the depth of Tommy's initiation notes (EGP Energy, Concord New Energy): real data, charts, analysis, thesis, the call, the conclusion. Sections, in order:
  1. **The call box:** company and ticker, LONG or SHORT, price and date at publication, target, conviction, what proves it wrong.
  2. **The claim behind it:** the journal piece and its claim, linked.
  3. **Thesis.** The explanation keeps the journal's analogy style, at buy-side depth.
  4. **What the market prices in versus our view** (variant perception).
  5. **Valuation**, with the working shown.
  6. **Charts from real, dated, sourced data.**
  7. **Risks**, and what would change the view.
  8. **Conclusion.**
- **A calls scorecard** on the same page: every call ever made, dated, marked against its target and falsifier. Right or wrong, nothing is ever deleted.

## The process (non-negotiable)

1. **Claude drafts the full pitch:** data, charts, valuation, thesis, a draft view.
2. **Claude gives Tommy the summary and breakdown.** Tommy reads everything and decides the call: direction, target and conviction. **The final call is Tommy's.** He must be able to defend it in 20 seconds without notes.
3. **Only then is it published**, with Tommy's explicit go for that pitch. Nothing is published undecided.
4. **Every new journal piece is a candidate pitch.** When a piece publishes, Claude asks whether to draft a pitch on the company or infrastructure in it.

## Claims and pitches must agree

- **Published claims are never reworded** (the existing rule in `src/data/claims.ts`). This protects the record.
- Every pitch is checked against the claim(s) it rests on. **If they disagree, the pitch says so openly** ("In July I argued X. The evidence since says Y, so this call narrows it / goes further"), and if needed a **new dated claim** is added alongside the old one. Never a silent fix.

## Updates: monthly, not daily

- Pitches are **never reposted or rewritten** after publication, so readers never wonder why they are seeing the same piece again.
- **Once a month** the scorecard alone gets one dated refresh: latest prices, target and falsifier checks, any call that has resolved. A resolved call gets a short dated post-mortem on the scorecard.
- Each monthly refresh and each new pitch goes live only with Tommy's approval, since it republishes the public site.

## Rule changes this needs (to make in the build session)

- **`WRITING-FORMAT.md` §4 / §4a and `CLAUDE.md` "Financials as evidence":** share prices, valuation, targets and calls stay banned in **journal pieces** and on every page **except pitch pages and the calls scorecard**. The exposure map stays "what they make" only.
- **`CLAUDE.md` claims-page rule:** the claims list itself keeps no statuses. Scoring lives only in the calls scorecard.
- **The pitch disclaimer:** each pitch page states that it is the author's own analysis, not investment advice, and that the author holds no position unless stated.
- **Never an em dash.** British spelling. Same house style.

## First pitches

- **Vertiv (VRT, NYSE):** from "Vertiv is paid per megawatt, and AI has made every megawatt harder to build" (25 Sep 2026).
- **Nebius (NBIS, Nasdaq):** from "Nebius has lined up five gigawatts of power. It expects about one switched on this year" (30 Sep 2026).

Useful prior work (in the jobs folder, read only): the paused Physical Layer Radar's reads on both names, in `~/Desktop/jobs/lanes/paper_portfolio/PL_RADAR_TRACKER.md` and `live_book.json`. For NBIS this includes an open gap between ACV per MW and the ARR guide that the pitch must resolve. These were Claude's reads, not Tommy's calls; use them as research inputs only.

## Related, outside this folder

- The **Physical Layer Radar** (Claude's paper book) is **PAUSED** as of 6 Oct 2026. Its scheduled task `model-portfolio-daily` is disabled; its files stay in `~/Desktop/jobs/lanes/paper_portfolio/`. It is not part of the site.

## What was built (6 Oct 2026)

- **Pitches:** `src/content/calls/<slug>.md`, schema in `src/content.config.ts`. Frontmatter holds the call box (`call`), the claim ids it rests on (`claims`), Claude's `draftView`, and the `charts` data. The body runs: The thesis; What the market prices in, and where I differ; Valuation, with the working; `<div class="charts-slot"></div>` (charts render there); Risks, and what would change my view; Conclusion; the sources line.
- **Page:** `src/pages/calls/[slug].astro` renders the call box, the linked claim, the body, the charts (`src/components/Chart.astro`) and the disclaimer. `/calls/` redirects to the scorecard.
- **Drafts** render only under `npm run dev`, with a banner and Claude's draft view in the call box. The production build excludes them, and **fails** any pitch with `draft: false` that lacks a date, direction, target or conviction (`src/lib/calls.ts`).
- **Claims page** (`/claims`, "Claims and calls"): each claim lists its pitch underneath, and the scorecard sits at `#scorecard`.
- **Scorecard data:** `src/data/calls.ts`. Monthly, add one `Mark` per open call (date, close, falsifier check) and set `SCORECARD_REFRESHED`. A resolved call gets `resolved` with a short post-mortem. Never delete.
- **Checker:** `python3 brand/check-call.py` checks sections, order, sources tail, claim ids, banned punctuation and US spellings, and that a published pitch carries Tommy's call and a real date.

- **No call** is a decided verdict (`direction: "NO CALL"`, no target). It needs `call.revisitIf`, what would turn it into a call. It is marked on the scorecard like any call, with the price move shown instead of a return.
- **Corrections:** when a pitch finds its journal piece was wrong, the pitch says so in a "Where I was wrong in September" passage (what was wrong, what changed the view), and the pitch's `correction` field puts one sentence under the claim on `/claims`. The piece and the claim are never edited. Tommy's rule (6 Oct 2026): do not change what was said before; say it was wrong and why.

## To publish a pitch (only with Tommy's explicit go)

1. Tommy sets `call.direction`, `call.target`, `call.conviction`, and confirms `call.wrongIf`.
2. Refresh `call.price` and `call.priceDate` to the latest close, and rework any figure that moved with it.
3. Rewrite the conclusion (and title, if needed) to match his call. Delete `draftView`.
4. Set `draft: false` and `date` to the real go-live time, `+08:00`.
5. `python3 brand/check-call.py`, then `npm run build`, then push.
