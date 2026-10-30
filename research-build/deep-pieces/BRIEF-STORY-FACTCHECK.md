# Brief: independent check of a rewritten deep piece (31 Oct 2026)

A writer has rewritten the deep pieces named in your instructions as stories (rules: research-build/deep-pieces/STORY-RULES.md; model: src/content/journal/the-equipment-queue.md). You did not write them. Your job is to make sure nothing false, lost or sloppy reaches Tommy, and that the story actually works. Assume there are mistakes and find them.

## For each piece
1. **The record survived.** Compare it with the version before the rewrite: `git show a16b1ad:src/content/journal/<slug>.md`, or the updates/ copy if the instructions name one. Check three things:
   - Every `<a id="...">` in the old file is still present.
   - Every claims.ts entry with `home` or `id` equal to the slug is quoted word for word. `python3 brand/check-piece.py src/content/journal/<slug>.md` checks this, and it must report 0 failures.
   - No sourced material that mattered to the argument was silently dropped. Folding into the evidence block is fine.
2. **Every number is right.** Each figure in the storyline, chart labels, chart aria-labels and captions must match the old piece, the sidecar (research-build/deep-pieces/<slug>.sidecar.md), the update copy or a primary source the writer named. Recompute any arithmetic the writer did ("about seven times", ratios, shares). For each chart, recompute where its points sit from the axis scale and confirm that every bar, line and dot lands on its value. A chart that misstates a value is a failure.
3. **Nothing is claimed beyond the evidence.** Look for interpretive sentences that state as fact something the sources only suggest, and soften or cut them. Also check: no press-only figure in the body, no share prices or views on shares, no "Fluence", no em or en dashes (`grep -c "—\|–"` must be 0), British spelling.
4. **The story works.** Read it as a newcomer.
   - Is the claim clear by paragraph three?
   - Do the headings read as an argument?
   - Is there a climax, a fair counter-evidence beat, and an ending that answers the opening?
   - Does any company get a section of its own in disguise?
   - Is any paragraph confusing or repetitive?
5. **Fix what you find**, directly in the piece file and only there. Keep fixes minimal and exact. Do not rewrite the voice, and do not touch any other file, git, or `npm run build`. Rerun the checker after every fix.

## Report (under 250 words per piece)
For each piece:
- every error found and how you fixed it (old, then new);
- anything you could not verify;
- your verdict on the story (works / works with reservations / does not work) and why, in two sentences;
- the final checker output.
