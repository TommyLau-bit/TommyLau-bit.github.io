# Brief: independent check of the new endings (31 Oct 2026)

Writers have replaced the end of each deep piece named in your instructions, following research-build/deep-pieces/BRIEF-ENDING.md. The rules are STORY-RULES.md 18a and 18b. The model is src/content/journal/the-equipment-queue.md. You did not write these endings. Assume there are mistakes and find them.

The version before the change is `git show HEAD:src/content/journal/<slug>.md`. The working tree holds the new one.

## For each piece
1. **The record survived.**
   - Every `<a id>` in the HEAD version is still present.
   - Every claim in the HEAD version's "Claims on record" and `claims-earlier` fold appears word for word inside the one `<details class="claims-record">`, with its "Breaks if" and later-evidence notes.
   - `python3 brand/check-piece.py src/content/journal/<slug>.md` reports 0 failures.
   - Nothing above the ending changed, except at most the paragraph that hands over to it.
2. **Every number is right.**
   - Each figure in the new ending, its diagrams, captions and aria-labels must match the piece, its sidecar (research-build/deep-pieces/<slug>.sidecar.md) or the sibling piece it cites. Open the sibling piece and check it.
   - Recompute any arithmetic.
   - For each new diagram, recompute from its scale where every bar, dot and line sits, and confirm it lands on its value.
   - Check that every label sits inside the 560-wide viewBox and that no two labels overlap. Estimate about 7.5px per character at 13 to 14px and 6.5px at 12px.
3. **Nothing is claimed beyond the evidence.**
   - The jolt must follow from the facts. Soften or cut any leap.
   - No share prices, valuations or views on shares.
   - No "Fluence".
   - No em or en dashes (`grep -c "—\|–"` must be 0).
   - British spelling.
4. **The ending works.**
   - Does it land a genuinely non-obvious idea, rather than restating the piece?
   - Is it a story, not a list?
   - Does it add without repeating the body?
   - Is it under about 550 words?
5. **Fix what you find**, directly in the piece file and only there. Keep fixes minimal. Do not touch any other file, git or `npm run build`. Rerun the checker after every fix.

## Report (under 200 words per piece)
For each piece:
- every error and its fix (old, then new);
- anything you could not verify;
- your verdict on the ending (electric / good / flat) and why, in two sentences;
- the checker output.
