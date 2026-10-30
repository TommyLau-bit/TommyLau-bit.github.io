# Brief: draft ONE update to a live deep piece (30 Oct 2026)

Tommy approved this update under the "Two tracks for new work" rule in CLAUDE.md. You write a REVISED COPY for review; the live file is not touched.

## Read first
CLAUDE.md (all Hard rules, especially "Quality over quantity", "The deep piece", "Merging keeps the record", "Two tracks for new work"), WRITING-FORMAT.md §D and §E, the live piece src/content/journal/<slug>.md in full, its sidecar research-build/deep-pieces/<slug>.sidecar.md, the scout notes named in your instructions, and src/data/claims.ts.

## Rules for the update
- Copy the live piece to research-build/deep-pieces/updates/<slug>.md and edit only the copy.
- Add the new material where the scout notes say, with every figure primary-sourced and dated (re-open the source; the notes are leads). Press-only figures stay out of the body.
- Quoted claims under "Claims on record" are never reworded. A new dated claim may be added beside the old ones, in the same format (claim and breaks if), dated "30 October 2026" for now (it becomes the update's go-live date).
- Keep the investor layer under the checker's 2,600 words before the exposure map: if the addition pushes it over, trim elsewhere (repetition, secondary detail), never claims.
- Frontmatter: set `updated` to 2026-10-30T12:00:00+08:00 as a placeholder, and rewrite `updateNote` to one sentence saying what this update added (keep the first-published `date`).
- Add new sources to the sources line. No em or en dashes. British spelling. No share prices or views on shares. Never name Fluence.
- Run `python3 brand/check-piece.py research-build/deep-pieces/updates/<slug>.md` (expect only warnings and possibly map/claims messages because the copy is outside src; report them).

## Also write
research-build/deep-pieces/updates/<slug>.CHANGES.md: a short list of every change (added, cut, corrected), each new figure with its primary source URL and date, the new claims.ts entry if any (as TypeScript, `date` and `home` set), and a draft LinkedIn post (one per substantial update, opening with the sharpest new number).

## Report (under 250 words)
What was added and cut, the new claim if any, investor-layer word count, checker result, anything you could not verify.
