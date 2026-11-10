# Brief: independent fact-check of ONE update draft (10 Nov 2026)

You did not write this draft. Be adversarial. Working directory /Users/tommylau/Desktop/journal.

Files for slug <slug> in research-build/deep-pieces/updates/: <slug>.md (the draft), <slug>.diff (live vs draft), <slug>.CHANGES.md (the writer's log with sources).

## Check
1. Every ADDED or EDITED sentence in the diff: re-open its primary source yourself (regulator, operator, filing, government record, company release). Confirm each number, date, name and quote word for word, and that the sentence does not say more than the source.
2. Every CUT: the remaining text still reads; no later sentence, chart, table, anchor or "What would prove me wrong" item now refers to something that was cut; no term is now used before it is explained.
3. House style in changed lines: no em or en dashes, British spelling, plain words, terms and companies explained at first use, no share prices or views on shares, no "updated"/"correction" language, claims and claims-record quotes untouched.
4. The sources line includes each new source.

## Fix
Fix problems directly in the draft <slug>.md (never the live file in src/). If a claim cannot be confirmed at a primary source, remove it (restore the live wording if it was an edit). Then run `python3 brand/check-piece.py research-build/deep-pieces/updates/<slug>.md` (0 failures required; visible words at or below 3,600).

Append a "## Fact-check (10 Nov)" section to <slug>.CHANGES.md: each item checked, PASS/FIXED/REMOVED, with the source.

## Report (under 200 words)
Verdict, every fix made, anything you could not check.
