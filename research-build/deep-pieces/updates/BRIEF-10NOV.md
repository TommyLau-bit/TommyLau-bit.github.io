# Brief: site update round, 10 Nov 2026 (Tommy: "site updates, all of them, do it now")

You update ONE live chapter of The Physical Layer (power for AI data centres, seven chapters).
Today is 10 Nov 2026 (MYT). You draft; the live file is NOT touched.

## Read first
- CLAUDE.md (Hard rules), WRITING-FORMAT.md §D and §E, research-build/deep-pieces/STORY-RULES.md
- research-build/deep-pieces/BRIEF-UPDATE.md (the update rules; where it conflicts with this file, this file wins)
- the live piece src/content/journal/<slug>.md in full, and its claims in src/data/claims.ts
- your chapter's items below and any notes file named there (notes are leads, not sources)

## Job
1. For each item listed for your chapter, find out at PRIMARY sources (regulator, grid operator, company filing or release, government record, Hansard) whether new evidence has landed that the piece does not already carry. Many items are scheduled for later dates (e.g. 24 Nov, 9 Dec, 31 Dec): if it has not happened by 10 Nov 2026, do not write about it; list it as "not landed yet".
2. Build-ons (where listed): add a short section or paragraphs inside the existing chapter, sourced, plain English first.
3. Write the result into a COPY: research-build/deep-pieces/updates/<slug>.md (copy the live file first, then edit only the copy).

## Rules
- Only add what clears the bar: new, primary-sourced, dated, something a PM learns. Skip trivia. If nothing has landed, say so and make no copy.
- The piece is short on purpose: visible words must stay at or below 3,600 (check with `python3 brand/check-piece.py <copy>`; it warns above 3,600). Make room by trimming repetition or secondary detail, never claims, figures that charts depend on, anchors (`{#...}` ids and `<a id>`), or "What would prove me wrong".
- Facts in the text that are now out of date: edit them so they are simply right (no "Correction", no "Update", no "as of" notes announcing a change, no `updated` fields). The piece never says it was updated.
- Never reword claims.ts entries or the claims-record quotes. No new claims.ts entries.
- Every new figure: primary source, dated, added to the sources line. Explain every new term or company name where it first appears.
- House style: no em or en dashes, British spelling, 14 to 20 word sentences, plain words. No share prices, valuations, targets or views on shares. Never name Fluence.
- Keep the `date` frontmatter unchanged.

## Also write research-build/deep-pieces/updates/<slug>.CHANGES.md
Every change (added, cut, edited), each new figure with source URL and date, the "not landed yet" list, and a draft LinkedIn post (about 120 words, opens with the sharpest new number, no em dashes) only if the update is substantial.

## Report back (under 250 words)
What changed, visible word count, checker result, what has not landed, anything you could not verify at a primary source.
