# The Physical Layer

Tommy's public journal on AI and energy infrastructure. Astro static site,
GitHub Pages, live at https://thephysicallayer.fyi

## Claims and Calls (read `CALLS-SPEC.md` first)

The site has a second core: buy-side pitches with Tommy's own calls, at
`/calls/<slug>/`, merged into the claims page (`/claims`, titled "Claims and
calls"). Before any work on pitches, calls, the claims page or share prices,
read `CALLS-SPEC.md`, which is the spec and records what was built.

- A pitch is `src/content/calls/<slug>.md`. It starts `draft: true` with
  `call.direction`, `call.target` and `call.conviction` null and Claude's view
  in `draftView`. **Only Tommy decides the call.** A pitch goes live only when
  he has set those three and given an explicit go; the build fails a
  non-draft pitch without them. Drafts show only under `npm run dev`.
- Pitches are never rewritten after publication. The monthly scorecard mark
  goes in `src/data/calls.ts`, with Tommy's approval.
- When a journal piece publishes, ask Tommy whether to draft a pitch on it.

## Before writing or editing any piece, read `WRITING-FORMAT.md`

It is the complete spec and it is not optional. Tommy will hand over raw notes
and expect a finished post that matches the existing six exactly. The spec
covers the two shapes a piece can take, every frontmatter field, the body
skeleton in order, the house style measured from the corpus, scope limits, the
cover art brief, the publish steps and the matching LinkedIn post.

`TEMPLATE.md` at the repo root is the fill-in skeleton. The content loader never
sees it.

## What his notes must contain

The claim in one sentence, the mechanism, one or two structural numbers, and who
operates in the layer. If one is missing, ask for that one thing. Do not invent
it. Everything else, including the title, analogy, section breaks, summary,
cover brief and LinkedIn post, is yours to write.

## Hard rules

- **The subject stays the subject.** If the notes are about one company,
  project or policy, it is named in the title, summary, cold open and thesis
  line, and every section keeps coming back to it. Never turn it into a generic
  industry piece that mentions it in passing. See WRITING-FORMAT.md §0.
- **The date is when it actually publishes.** `date` is the real go-live time,
  `YYYY-MM-DDTHH:MM:SS+08:00`, set at publish. Never a planned, staggered or
  future date. The checker fails a future date.

- **Scope is AI and energy infrastructure only.** No commodities, shipping,
  general equities or macro. The narrowness is the asset.
- **Financials as evidence, never a view on the shares, in journal pieces.** A
  company's own disclosed figures (revenue, margins, backlog, capex, order
  books) may appear in a piece when they test or confirm the physical
  mechanism, dated and sourced to the filing. Never a share price, market
  value, valuation multiple, target, rating, recommendation, or claim that a
  share is cheap or expensive, in a journal piece or on any page **except
  pitch pages (`/calls/<slug>/`) and the calls scorecard**. Keep them out of
  the exposure map, which stays "what they make" only. See WRITING-FORMAT.md
  §4a and CALLS-SPEC.md.
- **Never post to LinkedIn from Tommy's personal profile.** The company page
  only. Verify the composer identity reads "The Physical Layer" before submitting.
- **Do not add a new piece to `READING_PATH`.** The reading page is a capped
  on-ramp, not an index. See the README section on it.
- House style: no em dashes, British spelling, 14 to 20 word sentences,
  1,050 to 1,500 words.

## The site around each piece

A new piece is not published until the site around it is updated. Every time:

- **The map.** Add the slug to one layer in `src/data/stack.ts`. Every piece,
  no exceptions. If no layer fits, add a new layer in its physical place in
  the chain rather than forcing the piece into the nearest one.
- **The claims page.** For an Analysis piece, add an entry to
  `src/data/claims.ts`: the thesis in one sentence, the falsifier, and the
  evidence watched. The claim and test are never reworded later. The claims
  list keeps no statuses (Open, Holding and so on) and no reviews: Tommy
  decided it is a plain list of claims. Do not add status tracking to it or
  suggest it. Scoring lives only in the calls scorecard, for calls. If a pitch
  disagrees with a published claim, the pitch says so openly and, if needed,
  a new dated claim is added beside the old one. Never a silent fix.
- **The numbers.** If the piece rests on a new structural figure, add it to
  `src/data/numbers.ts`. Physical figures only, never anything about shares.
- **Companies** build themselves from the exposure map. Spell company names
  consistently. There are no topic pages; the map does that job.

**The top menu is fixed at five: Journal, Map, Claims, Glossary, About.** Tommy
found nine items too crowded. Do not add to it. Start here, Numbers and
Companies live in the footer and are linked from the map page; any new
reference page goes there too.

The checker fails a piece missing from the map, or an Analysis piece missing
from the claims page. See WRITING-FORMAT.md §6a.

**No email sign-ups.** Tommy has decided against a newsletter or sign-up form
anywhere on the site. Do not add one or suggest one. Readers follow via the
LinkedIn company page and RSS.

## Before every publish

```bash
python3 brand/check-piece.py src/content/journal/<slug>.md
python3 brand/check-call.py            # pitches
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py
npm run build
```

The checker must exit clean. Bump `OG_VERSION` in `src/config.ts` only when the
artwork of an existing card changes, because LinkedIn caches card images by URL.
