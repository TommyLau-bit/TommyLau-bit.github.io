# Brief: rewrite deep pieces as stories (31 Oct 2026)

Tommy read the merged deep pieces and found them messy: several old articles stapled together, one section per company, five claims in one piece, tables where a chart should be, no storyline. He wants each piece to read like a good film: grab the reader, build, reach a climax with the strongest evidence and charts, and end by tying everything together. He has approved rewriting every piece. He reads them in the morning, so make them excellent.

## Read first, in this order
1. `research-build/deep-pieces/STORY-RULES.md`, the rules. Follow every one.
2. The model, `src/content/journal/the-equipment-queue.md`, and its before version, `research-build/deep-pieces/pilot/the-equipment-queue.BEFORE.md`. Study exactly what changed and why.
3. `research-build/deep-pieces/STORY-STUDY.md`, the craft study behind the rules.
4. CLAUDE.md, the "Hard rules" section.
5. For each of your pieces: the live file `src/content/journal/<slug>.md`, its sidecar `research-build/deep-pieces/<slug>.sidecar.md` (verified sources) and every claims.ts entry whose `home` or `id` is the slug.

## What to do, per piece
1. Write the spine in one sentence. Pick the headline claim: the claims.ts entry whose id is the slug if there is one, otherwise the strongest. Plan 6 to 9 beats and 2 to 4 charts before writing.
2. Rewrite `src/content/journal/<slug>.md` in place.
   - Keep: `date`, `category`, `cover`, `tags`, `draft`.
   - Set `updated: 2026-10-31T08:00:00+08:00` and `updateNote` to one sentence, e.g. "Rewritten on 31 October 2026 as one story with N charts; earlier claims are kept word for word at the end." If the piece has a pending update, the note also names what the update added.
   - The `title` and `summary` may be improved to match the spine. The title stays 8 to 16 words, and the slug never changes.
3. Use only facts already in the piece, its sidecar or its approved update copy. A new figure is allowed only if you open its primary source, and you must list it in your report with URL and date. Never put press-only figures in the body.
4. Keep every `<a id="...">` anchor from the old file. Quote every claim word for word: the headline claim in full under "## Claims on record", the rest inside `<details class="claims-earlier">`. Move evidence tables, method notes and corrections into `<details class="evidence">` at the end. Keep the exposure map, the sources line, "What would prove me wrong" and "Research notes", short and plain.
5. Build the charts exactly as STORY-RULES.md describes, using inline SVG and only the listed classes. Compute coordinates with a script (python3 in your scratch space, not in the repo). Check that every point matches its source figure and that no label runs outside the viewBox.
6. Run `python3 brand/check-piece.py src/content/journal/<slug>.md` until it reports 0 failures, and fix any warnings you can. Also run `grep -c "—\|–"` on the file, which must return 0.
   - Do NOT run `npm run build` or the dev server, because other writers are working at the same time.
   - Do NOT edit `src/data/*`, `src/styles/*`, `src/pages/*`, `brand/*`, any other piece, or git. If you need a claims.ts, numbers.ts, glossary or CSS change, describe it in your report and I will make it.
7. House style: British spelling, sentences of 14 to 20 words on average, no em or en dashes. No share prices, valuations or views on shares. Never name Fluence. Readable by a layman at the top; precise and primary-sourced below the divider.

## Report (under 300 words per piece)
For each piece: the spine; the beats as headings; each chart's title and form; the headline claim id; word counts (top, investor storyline); the checker result; any new figure with its source; any change you need in shared files; anything you were unsure of.
