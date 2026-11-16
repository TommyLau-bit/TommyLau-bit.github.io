# The journal run (trigger: "1")

Set by Tommy, 10 Nov 2026. When Tommy says **"1"** (or "journal run", "check the updates"), run this whole job:
the journal website and everything connected to it. The job-hunt trigger is "2"; this is its twin.

Saying "1" is Tommy's go-ahead for updates, fixes and loose ends that pass fact-check: they go live
in the same run. New pieces, new chapters, company studies and calls are drafted and then WAIT for
his explicit word.

## 0. Read first

- research-build/HANDOVER.md, START HERE (what is due, what has not landed, open flags)
- CLAUDE.md (hard rules) and WRITING-FORMAT.md (§D, §E)
- study-decks/ROADMAP - buy side to PM.md, the growth list at the end
- memory index (MEMORY.md) for standing rules: LinkedIn, CVs, briefs, study deck, illustrations

## 1. What has landed

- Go through the dated "Not landed yet" list in START HERE. For each item whose date has passed, check
  it at its primary source.
- For every chapter, also look for new primary evidence since the last run: regulators, grid operators,
  filings, government records, company releases. Press reports are leads only.
- Use one writer agent per chapter with new material (brief: research-build/deep-pieces/updates/BRIEF-10NOV.md,
  dated afresh), then one INDEPENDENT fact-check agent per draft (BRIEF-FACTCHECK-10NOV.md).
  Never let the writer check its own work.

## 2. Improve and build on

- Growth list items (updates, build-ons) that now have primary evidence.
- Fix anything found wrong in place, never as a dated correction (CLAUDE.md).
- Improvements to a piece's clarity are allowed. Keep pieces at or below 3,600 visible words; pay for
  additions with cuts. Never reword claims or the claims record.
- A NEW piece or chapter: only if it clears the quality bar and sits on the chain with a handoff line.
  Draft it fully, then stop and ask Tommy. Never publish it on "1" alone.

## 3. Ship

- `python3 brand/check-piece.py` on every changed piece (0 failures), make-og, `npm run build`,
  check no anchor was lost, commit, push, wait for the deploy, read the live page.
- A piece built from a source file (e.g. solar.src.md + assemble.py) gets the same edit in its source.

## 4. Loose ends: everything that quotes the site

Check each against what changed; fix only what is now wrong or stale.

- **Power page:** src/data/power.ts (stats, sources), src/data/power-ratings.ts (formulas). Each card quotes the
  pieces; when a piece's number changes, change the card's stat and recheck its rating. Photos and credits in
  src/data/power-photos.ts; journal lead photos in src/data/journal-photos.ts.
- **Study deck:** study-decks/Study deck - power for AI data centres.md and PDF (tools/deck2pdf.py).
  Same four parts per chapter, plain words. Never commit study-decks/.
- **Email briefs:** ~/Desktop/jobs/research coverage/briefs/ and _SEND. Rebuild a brief when its
  piece's claim, chart or a quoted fact changes, then refresh _SEND.
- **Scheduled emails:** Gmail in:scheduled. Any email quoting a changed fact or an old brief is fixed
  (memory: gmail-scheduled-edit for how).
- **CV 2T:** only when a fact on it is now wrong (memory: feedback-cv-churn). Never count pieces on a CV.
- **LinkedIn:** company page (About, specialties, the scheduled post queue) and Tommy's personal profile
  (About, Experience topic line, Featured) when chapters or topics change. Never post from the
  personal profile. Never change the profile URL.
- **LinkedIn posts:** each new piece or substantial update gets one company-page post, scheduled by
  Claude in the Mon/Wed/Fri 11:30 slots and marked in brand/linkedin-posts.md. Queued posts that quote
  a now-wrong fact are fixed.
- **The map and illustrations:** src/data/stack.ts (layers, CHAPTERS, handoff lines), the descent
  (src/components/Descent.astro) and OG cards, whenever a chapter is added, removed or its story moves.
  Illustrations to the standard in memory (feedback-illustration-quality).
- **Interview prep docs** in ~/Desktop/jobs/interview prep/ that are still in use, if they quote a changed fact.

## 5. Company studies and calls

Plan agreed 11 Nov 2026 (full plan: study-decks/ROADMAP - buy side to PM.md, "The plan"). A "1" run never
starts a study or call; Tommy starts each one himself ("start Centrus").
- Company studies: three, cap five, emerging names only: Centrus Energy, then Bloom Energy, then Oklo or
  Solaris (ASP Isotopes watch only). Written by Tommy, fact-checked and pushed back on by Claude, in
  ~/Desktop/jobs/company studies/, NEVER on the site. No price, valuation, target or call.
- Calls: two, from those studies, private, interviews only, never published or emailed.
- Once a study or call exists, every "1" run also checks it against new filings and results.

## 6. Close

- Rewrite HANDOVER START HERE: what went live, the new dated "Not landed yet" list, open flags.
- Update memory where a standing rule changed.
- Report to Tommy in plain words: what went live, what is waiting and on what date, and any decision
  that is his (new piece, chapter, study, call).

## Never

Publish a new piece or chapter without his word. Add company notes or calls to the site. Share prices,
valuations or views on shares in any piece. Em dashes. Schedule recurring tasks without him (the run
happens when he says "1").
