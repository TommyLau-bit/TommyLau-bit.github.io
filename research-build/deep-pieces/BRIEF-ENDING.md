# Brief: give each deep piece an electric ending (31 Oct 2026)

Tommy read the rewritten pieces and liked the opening and the build. His complaint is the second half. The pieces ended on "Claims on record", which reads like a summary of what the reader has just read, so a strong start finishes poorly. A first fix (a "what to watch" checklist with bold labels) was still topics piled up. He wants the ending to be electric: the part where a reader thinks "I hadn't thought of that, now that you mention it". He wants diagrams, because they help readers see the idea.

## Read first
1. `research-build/deep-pieces/STORY-RULES.md`, especially rules 18a and 18b (the new ending rules).
2. The model, `src/content/journal/the-equipment-queue.md`, from the heading "The gear outlives the chip it was ordered for" to the end. Compare it with its version before this change, `research-build/deep-pieces/pilot/the-equipment-queue.ENDING-BEFORE.md`. What changed:
   - The old "## Claims on record" section and the `claims-earlier` fold are gone.
   - After the counter-evidence beat and the closing paragraph, there are two forward headings, each built on one non-obvious idea with its own diagram:
     - two clocks side by side: chip launches every year against order books of three to four years;
     - a two by two that shows where each quarter's result would land.
   - "What would prove me wrong" and "Research notes" follow.
   - Then one `<details class="claims-record">` holds every claim word for word.
3. CLAUDE.md "Hard rules".
4. For each of your pieces:
   - the piece itself;
   - its sidecar, `research-build/deep-pieces/<slug>.sidecar.md`, if one exists;
   - its claims.ts entries;
   - the sibling pieces it touches. Read their headlines and figures; the best jolts often join two pieces.

## What to do, per piece
1. **Find the jolt.** List three candidate ideas a smart reader would not have reached alone, using only facts already in this piece, its sidecar or a sibling piece on the site. Good shapes:
   - two clocks that do not match;
   - who quietly gains or pays;
   - a second-order effect;
   - what the claim implies somewhere nobody is looking;
   - an inversion of the usual picture.
   Pick the strongest one or two. Be honest: no idea that needs a fact the site does not have, and no hype.
2. **Rewrite the ending only.** Start after the counter-evidence beat and the paragraph that answers the opening (keep those two, editing them only if they must hand over to the new ending).
   - Write one or two statement headings, each with one diagram, about 350 to 550 words of ending in all.
   - Then write "## What would prove me wrong", kept short and plain. Reuse the existing text, tightened.
   - Then "## Research notes", as it is now.
   - Then the claims fold:
     - It is one `<details class="claims-record">`, with the summary "The claims on record, word for word".
     - It holds the piece's own claim, introduced by "The test this piece stands behind, quoted word for word from the claims page:".
     - Any earlier claims follow, introduced by a line like "Earlier claims on this subject:". Quote every one exactly as now, with its "Breaks if" and later-evidence notes.
     - There is no nested details inside it.
   - Then the existing `<details class="evidence">`, the exposure map and the sources, unchanged.
3. **Fold the useful questions in briefly, where they serve the idea, never as a list:**
   - what to watch and when;
   - who gains and who pays;
   - what depends on it (link sibling pieces as `/journal/<slug>/`);
   - how long it should hold;
   - whether it is new or already widely known.
   One sentence says that whether it is in share prices is not this journal's question, and points to the research notes.
4. **Move the piece's own `<a id="<slug>"></a>` anchor** to just under the first new forward heading. Keep every other `<a id>` exactly where it is.
5. **Diagrams.** Use inline SVG with the exact chart markup and only the classes in STORY-RULES.md; copy the model's two figures as templates.
   - A piece carries at most 5 charts in all. If it has 4 now, add one; if 3, add one or two.
   - Compute every coordinate with a python3 script in your scratch space, never by eye.
   - Width 560. Keep every label inside the viewBox: estimate about 7.5px per character at 13 to 14px and 6.5px at 12px, and check that no two labels overlap.
   - Every number shown must be a sourced figure from the piece, its sidecar or the named sibling piece. Label your own framing as "My framing" in the caption.
   - The aria-label states every number.
6. **Check.** Run `python3 brand/check-piece.py src/content/journal/<slug>.md` until it reports 0 failures. `grep -c "—\|–"` on the file must return 0.
   - Do NOT run `npm run build`, the dev server or git.
   - Do NOT edit any file but your pieces.
   - Do not touch frontmatter, except the `draft` flag, which stays as it is.
7. **House style.** British spelling; sentences of 14 to 20 words; no em or en dashes; no share prices, valuations or views on shares; never name Fluence. Plain enough for a smart newcomer.

## Report (under 200 words per piece)
For each piece:
- the jolt in one sentence, plus the two you rejected and why;
- the new headings;
- each new diagram's title and form, and which sourced figures it uses;
- the ending word count;
- the checker result;
- anything you were unsure of.
