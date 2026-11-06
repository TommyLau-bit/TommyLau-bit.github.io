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

## The process (6 Oct 2026; superseded 6 Nov 2026 by "The book" and "Research page" below: new notes are published by the book's Sunday run, and the site shows no calls)

1. **Claude drafts the full pitch:** data, charts, valuation, thesis, a draft view.
2. **Claude gives Tommy the summary and breakdown.** Tommy reads everything and decides the call: direction, target and conviction. **The final call is Tommy's.** He must be able to defend it in 20 seconds without notes.
3. **Only then is it published**, with Tommy's explicit go for that pitch. Nothing is published undecided.
4. **Every new journal piece is a candidate pitch.** When a piece publishes, Claude asks whether to draft a pitch on the company or infrastructure in it.

## Claims and pitches (superseded 2 Nov 2026)

- Notes and pieces are independent and need not agree; a wrong fact is fixed in place, never flagged with a correction.

## Updates: every two weeks, not daily (biweekly since 6 Nov 2026)

- Pitches are **never reposted or rewritten** after publication, so readers never wonder why they are seeing the same piece again.
- **Every two weeks** the scorecard alone gets one dated refresh: latest prices, target and falsifier checks, any call that has resolved. A resolved call gets a short dated post-mortem on the scorecard.
- Each refresh and each new pitch goes live only with Tommy's approval, since it republishes the public site.

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
- **No call** is a decided verdict (`direction: "NO CALL"`, no target, `revisitIf` required). It is marked every two weeks with the price move shown, and the report says whether its revisit level is crossed.
- **Scorecard data:** `src/data/calls.ts`. Every two weeks, add one `Mark` per open call and set `SCORECARD_REFRESHED`. A resolved call gets `resolved` with a short post-mortem. Never delete.
- **Checker:** `python3 brand/check-call.py`.
- **Notes and pieces are independent** (Tommy, 2 Nov 2026, permanent; replaces "journal piece first"): a note may cover a company the journal never mentions and need not rest on a claim (`claims` may be empty). Notes and pieces do not need to match.
- **Research table grouped by launch** (Tommy, 2 Nov 2026): `/research/` shows one table, grouped into the coverage launches in `LAUNCHES` (src/data/calls.ts), newest first, each ordered by map layer. A note outside every launch is grouped by its month automatically; name a new launch only when several notes on one sector go out together. A note whose first claim's layer misfiles it may set `layer:` (Nvidia: chips). Publication dates are never changed.
- **No dated corrections, ever** (2 Nov 2026, permanent): a wrong fact in a piece or note is edited so it is right. No "Where I was wrong", no `correction` field, no "Correction" paragraphs.
- **Note marks are retired** (Tommy, 6 Nov 2026): the notes are no longer marked or shown with calls; the book is the only scorecard. The tasks `research-biweekly-reprice` and `research-monthly-marks` are retired (the monthly one's 1 Nov run stalled on a permission prompt).

## Research page: the book is the record, the notes are the reasoning (Tommy, 6 Nov 2026, permanent)

Tommy found the page messy: two scorecards (the notes' own calls and the book) and no obvious place to start. Now one record and one library:
- /research/ is a PM's morning sheet, like the Radar dashboard (Tommy, 6 Nov 2026: the tables were still hard to read): one intro line; a masthead (equity, change, cash, open, closed); "This morning" (a headline and three bullets, `story` in book.json); then tabs: The book (position cards with a stop-to-target bar, closed trades with post-mortems, morning log), Watchlist (cards: buy above X, risk Y to make Z, "N times the risk", a bar), Idea bench, Calendar (`catalysts`), Notes, How it works (plain English, including reward against risk with a live example). All in src/components/Book.astro; the notes table is passed in as a slot. **The notes tab** is a library grouped by layer: company, published, price then, base value (src/data/notes.ts), gap, where it stands in the book, note and model links. No call, target, stop, return or status columns.
- Each note page shows "What the note found" (price at publication, base value, where it stands in the book, what would prove the thesis wrong) instead of a call box.
- **The notes' own calls are no longer shown or scored.** Tommy chose to drop the October initiation calls (Oklo out at target, Marvell and six others stopped out) from the page rather than keep them as closed trades; their record stays in src/data/calls.ts and git history, frozen. The PDFs keep their original text.
- A new note adds its base value to src/data/notes.ts (the book's target source); the `call` fields in front matter stay for the PDF and the checker, but the site does not display them.

## The book: a US$100,000 paper portfolio on the site (Tommy, 6 Nov 2026, permanent)

Tommy: the Physical Layer Radar paper book (Oct 2026, ~/Desktop/jobs/lanes/paper_portfolio/) was the perfected version; carry it onto the website exactly, on top of the initiation notes and models, which continue as before. His choices: Claude makes every call, the book starts fresh on 6 Nov 2026, it runs daily and publishes on its own, and it tops the Research page.

- Data: `src/data/book.json` (equity, cash, positions, closed, watch, avoid, equityCurve, exposure, log); shown by `src/components/Book.astro` at the top of /research/.
- Daily run: scheduled task `physical-layer-book-daily`, every day 07:30 SGT (Sundays: weekly review and one new note, no entries; Saturdays act on Friday's US close). It prices every name at verified closes, takes exits, marks, takes entries, rebuilds the watchlist, writes a log line, and commits and pushes book.json (and calls.ts every second Friday) on its own. Reports in research-build/book/.
- Calls: Claude makes every call (Radar rule). Tommy may disagree in one line; it is logged, the call stays Claude's.
- Sizes: HIGH 12 per cent, MEDIUM 7, LOW 4 of equity; max 15 per cent in a name, 10 open positions, 80 per cent invested; half size if results are within 10 trading days.
- Entry (long; shorts mirrored): the note's base value at least 15 per cent above the close (short: 25 per cent below); the 20-session closing low is at least 3 sessions old; the close is above the previous 5-session closing high (Tommy's ICC break and continuation); stop 1 per cent under that 20-session low; target the lower of the base value and the 60-session closing high; reward to risk at least 2:1. Fill at the close.
- Exit: first close through the target ("Target hit") or the stop ("Stopped out"), or a non-price wrongIf leg ("Thesis broken"). Stops never widen; at +1R the stop moves to entry. Every exit gets a post-mortem scored on process.
- Drawdown: 10 per cent below peak equity stops new entries until a review is logged.
- **Idea bench and new notes** (Tommy, 6 Nov 2026, as in the Radar): every weekday run scouts one or two new physical-layer names onto `bench` (never traded); every Sunday the strongest ready name is promoted to a full initiation note and Excel model by BRIEF-note.md, independently fact-checked, and published automatically (Tommy chose fully automatic), with its base value added to src/data/notes.ts. The monthly journal sweep is unchanged.
- Never backdated: the book opened in cash on 6 Nov 2026 because every candidate was at a fresh 20-day low after the October and November sell-off.
- The notes' own calls (calls.ts) are frozen history since 6 Nov 2026 and not shown; see "Research page" above. The section below applied to them for one day.

## Risk management: every view has a stop and a target (Tommy, 6 Nov 2026; now applied through the book, see above)

Tommy: a call without a stop and an exit is not how a PM runs a book; investors ask why he is still in. Adapted from his ICC trading rules (~/Desktop/trading/ICC_Trading_Strategy_v9.pdf: stops and targets at structure, closes not wicks, 2:1 minimum, a drawdown that forces a review) to twelve month equity calls.

- **Target:** the note's target. The first daily close at or through it takes the call out: "Out: target hit", measured at that close. To stay in, Tommy writes a dated new target and reason (a re-underwrite) before the next mark.
- **Stop:** set at publication and stored in `src/data/calls.ts` (`risk`). It sits at the most recent weekly closing swing low (a weekly close below the two weeks either side) that lies 5 to 20 per cent below the call price; if none, 20 per cent below. If the note's wrong-if names a tighter price level, that level is the stop. Shorts are mirrored (swing high above). The first daily close through it takes the call out: "Out: stopped out", measured at that close.
- **2:1 at publication:** a new view needs its target at least twice as far from the price as its stop (Tommy's minimum reward to risk). A view that cannot clear 2:1 is a no call.
- **Drawdown review:** if the open views together are down 10 per cent or more on average since their calls, every open view is reviewed before the next mark (Tommy's max drawdown rule).
- **No calls** carry no position, so no stop. Their price bands and revisit levels are reported, not traded.
- **Exits** are recorded as `exit` {date, price, reason} with a `resolved` post-mortem (Right for a target hit, Wrong for a stop). The research table shows the stop, the exit price and "Out: target hit / stopped out, date"; returns of a call that is out are measured at its exit.
- **How the first application was done (6 Nov 2026):** levels written in a note counted from its date (Oklo out at its US$28 target on 16 Oct, +22.2%; Marvell out at its US$230 level on 16 Oct, -20.0%). Stops set under this rule counted from 6 Nov; a call already through its new stop left at the 5 Nov close (Broadcom, Coherent, Eaton, Nvidia, SK Hynix, Vertiv). This is stated on the research page. Never backdate a new stop as if it had been set earlier: that would turn the record into a backtest.
- **Exits are automatic** (Tommy, 6 Nov 2026): the daily task `physical-layer-book-daily` checks every close against each stop and target and publishes exits and marks on its own.

## Briefs for agents (in research-build/)
- `BRIEF-note.md`: drafting an initiation note (text of record, PDF, model). `BRIEF-note-factcheck.md`: the read-only fact-check of a note.
- Journal pieces use the deep-piece briefs in `research-build/deep-pieces/` (`BRIEF-DEEP.md`, `BRIEF-DEEP-FACTCHECK.md`, `BRIEF-UPDATE.md`).
Process: one company at a time; draft, then an independent fact-check, then fix, then the call is set (by the Sunday run, or by Tommy in a session).

## To publish a note (by the book's Sunday run automatically, or by a session on Tommy's word; since 6 Nov 2026)

1. The Sunday run (from the draft view) or Tommy sets `call.direction`, `call.target`, `call.conviction`, and confirms `call.wrongIf`. Add the note's base value and Yahoo symbol to src/data/notes.ts (BASE_VALUE, SYMBOL) and set `layer:`; without them the book cannot trade it.
2. Refresh `call.price` and `call.priceDate` to the latest close, and rework any figure that moved with it.
3. Rewrite the conclusion (and title, if needed) to match his call. Delete `draftView`.
4. Set `draft: false` and `date` to the real go-live time, `+08:00`.
5. Build the PDF and model into `public/research/`, with a page-one PNG for the thumbnail. Recalculate the model so its values are cached (`soffice --headless --calc --convert-to xlsx` into a temp folder, then copy back), or it shows blank in Mail and Gmail previews. Set `files` and `keyPoints`.
6. `python3 brand/check-call.py`, then `npm run build`, then push.

## Pending (7 Oct 2026)

- Published so far: Vertiv (long), Nebius, TSMC, Texas Instruments, Corning, Bloom Energy, Lumentum, Schneider Electric, Micron, ASML, Ajinomoto (no call), Oklo (short), Broadcom (long), Marvell (long, 8 Oct 2026, target US$355, medium; rebuilt on the Investor Day deck of 6 Oct, which had not been filed on Form 8-K), GE Vernova (no call, 9 Oct 2026, medium), Hitachi (no call, 22 Oct 2026, medium), Eaton (long, 26 Oct 2026, target US$430, low), Siemens Energy (long, 28 Oct 2026, target €160, medium), Constellation (no call, 30 Oct 2026, medium). On 2 Nov 2026, on Tommy's instruction to follow the draft views without waiting for his approval: CLP Holdings (no call, medium), SpaceX (no call, medium), SK Hynix (long, target KRW 2,000,000, medium), Nvidia (long, target US$245, low), Seagate (no call, low), Samsung Electronics (long, target KRW 270,000, low). Later on 2 Nov 2026, same instruction: Mitsubishi Heavy (no call, medium), Infineon (no call, low), Kinder Morgan (no call, medium), Coherent (long, target US$275, low), Wärtsilä (long, target €30, low), Williams (no call, medium), Caterpillar (no call, medium), Entergy (no call, medium).
- Notes to be drafted automatically after each scheduled journal piece goes live (STEP 8 of the publish tasks): Hitachi Ltd (14 Oct), Eaton (16 Oct), Siemens Energy (20 Oct). Drafts only; Tommy decides each call.
