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

## Claims and pitches (superseded 2 Nov 2026)

- Notes and pieces are independent and need not agree; a wrong fact is fixed in place, never flagged with a correction.

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

## Redesign, 6 Oct 2026 (supersedes "The structure" above)

Tommy found the first build (a long web pitch with charts, merged into the claims page) messy and confusing. His direction: a clean page for analysts and PMs to read his calls and see his thinking, like the initiation note plus CV pack he attaches to cold emails. Reference: the Andromeda investor-letters page (a single clean list, newest first). What is built now:

- **Menu:** Journal, Map, **Research**, Glossary, About. Claims moved to the footer. `/claims` is back to the plain claims list, with one line pointing to Research.
- **`/research`:** a library list, newest first. Each entry has page one of the note as a thumbnail, the date, "Initiation", the call, the company and ticker, the one-line title, and links to the PDF, the Excel model and the summary page. Below it is a compact track record table (`#scorecard`).
- **The note:** a PDF initiation note in Tommy's house style (`~/Desktop/jobs/research coverage/_note_template/`, matched to his MarcoPolo, EGP and Concord notes), with a live-formula Excel model. Both sit in `public/research/<date>_<Company>_Initiation.pdf` and `_Model.xlsx`. Build scripts are in `research-build/<slug>/`.
- **`/research/<slug>/`:** a short summary page with the call box, two download buttons, three to five key points (`keyPoints`), and the claim it rests on, if any. No charts and no long body on the web; the Markdown body is the note's text of record. `/calls/...` redirects here.
- **Journal pieces:** if a note rests on a piece's claim, the claim box under the piece links to it.
- **Drafts** render only under `npm run dev`. The build fails a non-draft note without Tommy's call (`src/lib/calls.ts`).
- **No call** is a decided verdict (`direction: "NO CALL"`, no target, `revisitIf` required). It is marked monthly with the price move shown.
- **Scorecard data:** `src/data/calls.ts`. Monthly, add one `Mark` per open call and set `SCORECARD_REFRESHED`. A resolved call gets `resolved` with a short post-mortem. Never delete.
- **Checker:** `python3 brand/check-call.py`.
- **Notes and pieces are independent** (Tommy, 2 Nov 2026, permanent; replaces "journal piece first"): a note may cover a company the journal never mentions and need not rest on a claim (`claims` may be empty). Notes and pieces do not need to match.
- **No dated corrections, ever** (2 Nov 2026, permanent): a wrong fact in a piece or note is edited so it is right. No "Where I was wrong", no `correction` field, no "Correction" paragraphs.
- **Monthly marks:** the scheduled task `research-monthly-marks` prepares them early each month for Tommy's approval.

## Briefs for agents (in research-build/)
- `BRIEF-note.md`: drafting an initiation note (text of record, PDF, model). `BRIEF-note-factcheck.md`: the read-only fact-check of a note.
- Journal pieces use the deep-piece briefs in `research-build/deep-pieces/` (`BRIEF-DEEP.md`, `BRIEF-DEEP-FACTCHECK.md`, `BRIEF-UPDATE.md`).
Process: one company at a time; draft, then an independent fact-check, then fix, then Tommy decides the call.

## To publish a note (only with Tommy's explicit go)

1. Tommy sets `call.direction`, `call.target`, `call.conviction`, and confirms `call.wrongIf`.
2. Refresh `call.price` and `call.priceDate` to the latest close, and rework any figure that moved with it.
3. Rewrite the conclusion (and title, if needed) to match his call. Delete `draftView`.
4. Set `draft: false` and `date` to the real go-live time, `+08:00`.
5. Build the PDF and model into `public/research/`, with a page-one PNG for the thumbnail. Recalculate the model so its values are cached (`soffice --headless --calc --convert-to xlsx` into a temp folder, then copy back), or it shows blank in Mail and Gmail previews. Set `files` and `keyPoints`.
6. `python3 brand/check-call.py`, then `npm run build`, then push.

## Pending (7 Oct 2026)

- Published so far: Vertiv (long), Nebius, TSMC, Texas Instruments, Corning, Bloom Energy, Lumentum, Schneider Electric, Micron, ASML, Ajinomoto (no call), Oklo (short), Broadcom (long), Marvell (long, 8 Oct 2026, target US$355, medium; rebuilt on the Investor Day deck of 6 Oct, which had not been filed on Form 8-K), GE Vernova (no call, 9 Oct 2026, medium), Hitachi (no call, 22 Oct 2026, medium), Eaton (long, 26 Oct 2026, target US$430, low), Siemens Energy (long, 28 Oct 2026, target €160, medium), Constellation (no call, 30 Oct 2026, medium). On 2 Nov 2026, on Tommy's instruction to follow the draft views without waiting for his approval: CLP Holdings (no call, medium), SpaceX (no call, medium), SK Hynix (long, target KRW 2,000,000, medium), Nvidia (long, target US$245, low), Seagate (no call, low), Samsung Electronics (long, target KRW 270,000, low). Later on 2 Nov 2026, same instruction: Mitsubishi Heavy (no call, medium), Infineon (no call, low), Kinder Morgan (no call, medium), Coherent (long, target US$275, low), Wärtsilä (long, target €30, low), Williams (no call, medium), Caterpillar (no call, medium), Entergy (no call, medium).
- Notes to be drafted automatically after each scheduled journal piece goes live (STEP 8 of the publish tasks): Hitachi Ltd (14 Oct), Eaton (16 Oct), Siemens Energy (20 Oct). Drafts only; Tommy decides each call.
