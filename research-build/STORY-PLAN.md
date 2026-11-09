# Story plan (agreed with Tommy, 9 Nov 2026). NOT STARTED: do nothing until Tommy says go.

Tommy wants every change made together, at once, once the plan is final. More changes may be added here first.

## The decision

The site tells one story, in a causal order: where does the next gigawatt for AI come from, and why is every answer a queue? Seven chapters (the seventh, solar and batteries, approved 9 Nov evening and drafted; see below). Rack power and cooling are removed, because they answer a different question (what happens to the power inside the building).

## The chain (Tommy's order)

| Ch. | Piece (slug) | Role in the story | Handoff to the next chapter |
|---|---|---|---|
| 1 | Johor and Singapore (the-queue-not-the-chip) | The plug, not the chip, is the limit | Malaysia is not alone: America now decides who gets cut |
| 2 | America rations the plug (america-rations-the-plug) | The grid rations: who waits, who is cut, who pays | And the grid cannot speed up, because its machines come from a few factories |
| 3 | The equipment queue (the-equipment-queue) | A handful of factories keep the wait, not clear it | So builders skip the grid, and meet the turbine queue instead |
| 4 | Building your own power (building-your-own-power) | Skipping the grid's queue joins GE Vernova's six-year queue | Gas is booked to 2032, so why not build solar and batteries, the fastest power there is? |
| 5 | Solar and batteries (solar-and-batteries) NEW, DRAFT | Fast to build, but the grid counts them as a fraction of a firm megawatt, and AI runs through every winter night | So buyers want power that runs all year: reactors |
| 6 | Nuclear for AI (nuclear-for-ai) | Old reactors first; new ones wait | The new reactors are small, and their fuel is the gate |
| 7 | Microreactors (microreactors) | The reactor is the easy part; the fuel is the gate | Ending: every route to the next gigawatt runs through a queue |

## Changes to make at launch (all at once, as drafts first, preview to Tommy, then one launch)

**Remove powering-the-rack and heat-and-water everywhere** (as orbit was on 9 Nov):
- Site: archive both pieces in research-build/archive/, redirect their URLs (and old merged URLs that point into them) to the homepage; remove the distribution and cooling layers from src/data/stack.ts; claims stay in claims.ts as record.
- Descent: drop the hall and rack stops; the walk ends where the power reaches the site. Keep the one continuous camera.
- Hero, tagline, About, share card text: "from the grid connection down to the rack" and "the cooling" go; the story ends at the power reaching the site.
- CVs 2T and 3: drop the water bullet (2T) and "and cooling" in the platform line; still no piece count.
- Email briefs PoweringTheRack and HeatAndWater: archive, update the rulebook mapping, refresh _SEND (2 CVs + 6 briefs).
- Study sheets 5 and 6: move to study-decks/archive/ but keep for Tommy to read (SemiAnalysis covers rack power and cooling).
- LinkedIn: delete scheduled company-page posts on rack power and cooling (main posts and minis); personal headline, About ("the grid, power equipment, nuclear and cooling") and Experience line ("Rack power · Cooling and water"); company page About.
- CLAUDE.md, memory (one-sector), roadmap ("eight pieces"), handover.

**Tell the story:**
- Homepage: six numbered chapters in the order above, each with a one-line reason linking it to the next, replacing the layer headings.
- Each piece: one opening line placing it in the story ("Chapter 3 ...") and one closing handoff line to the next chapter with its reason. No new facts, only links between facts already in the pieces.
- Descent cards: rewritten as the story; drawings and camera kept. Stop order to match the chapters where the camera allows.
- stack.ts: layers in chapter order.

## The seventh piece: solar and batteries (DRAFT, 9 Nov 2026; Tommy: "yes go ahead with adding the seventh piece")

Title: "Solar and batteries: fast to build, but short of a winter night". Slug solar-and-batteries. Not live, not committed: the piece, cover and both source folders are in .git/info/exclude.
- Source of record: research-build/deep-pieces/solar/solar.src.md; charts.py writes illos/; assemble.py builds src/content/journal/solar-and-batteries.md (draft: true) and holds the CLAIM until launch. Research notes: research-build/topics/solar-firm-research/. Fact-check: research-build/deep-pieces/solar/FACTCHECK.md.
- Claim approved by Tommy, 9 Nov 2026 evening ("Yes, keep it"): the tightened version in assemble.py (four-hour storage below 50% for 2030/31 and at or below 40% for 2031/32; tracking solar 10% or less). Do not reword it at launch.
- Launch steps (with the rest of the story, on Tommy's word): add the CLAIM from assemble.py to src/data/claims.ts (dated the launch day); add the slug to the onsite layer in src/data/stack.ts after building-your-own-power (or its own layer if the chapter list replaces layers); set draft: false and the real date; remove the four solar lines from .git/info/exclude (the piece, the cover, research-build/deep-pieces/solar/ and research-build/topics/solar-firm-research/; kept out because the repo is public), then commit them; descent card for the chapter; make-og; check-piece, build, link check; LinkedIn post on the company page (scheduled, logged in brand/linkedin-posts.md); email brief for _SEND and the rulebook mapping; study sheet PDF already in study-decks/.

## Considered and not worth a chapter
Building new transmission lines (partly in America and Equipment), the gas pipe (inside Own power), the workforce (no primary data), moving to where the power is (inside Johor).
