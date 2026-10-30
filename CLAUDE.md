# The Physical Layer

Tommy's public journal on AI and energy infrastructure. Astro static site,
GitHub Pages, live at https://thephysicallayer.fyi

## Research: initiation notes and calls (read `CALLS-SPEC.md` first)

The site has a second core: Tommy's initiation notes, each a PDF in his house
style with its live Excel model, listed at `/research` like an investor-letters
page. Each note has a short summary page at `/research/<slug>/` (call box,
three to five key points, downloads, the claim it rests on). Tommy's
direction (6 Oct 2026): the page is for analysts and PMs, the same pack he
attaches to cold emails, so it stays clean and simple. No long web pitch, no
charts on the web page; the depth lives in the PDF and the model. Before any
work on notes, calls, the research page or share prices, read `CALLS-SPEC.md`.

- A note's text of record is `src/content/calls/<slug>.md`; the PDF and xlsx
  are built from it with the template in `~/Desktop/jobs/research
  coverage/_note_template/` (scripts kept in `research-build/<slug>/`) and
  saved in `public/research/`. A draft has `draft: true`, the call fields null
  and Claude's view in `draftView`. **Only Tommy decides the call** (LONG,
  SHORT or NO CALL). The build fails a non-draft note without it.
- Notes are never rewritten after publication. The monthly mark goes in
  `src/data/calls.ts`, with Tommy's approval.
- When a later note finds a journal claim was wrong, the note says so openly
  ("Where I was wrong", and what changed the view). The claim is never edited
  or deleted, and the archived original text of a piece is never edited. The
  page itself may be deepened (30 Oct 2026), and says openly where a later
  finding cuts against a claim on record.
- **Journal piece first, always** (Tommy, 6 Oct 2026). A note or call is only
  written on a company that already has its own section and claim in a deep
  piece. If Tommy asks for a note on a company with none, write that first.
- When a journal piece publishes, ask Tommy whether to draft a note on it.
- Once a month (scheduled task `research-monthly-marks`) the track record
  marks are prepared for Tommy to approve; nothing is pushed without his go.

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

- **Quality over quantity** (Tommy, 29 Oct 2026). The site is for investors and
  portfolio managers looking for insight, not a feed of every related topic. A
  piece publishes only if it clears all three: (1) a mechanism the site does not
  already have (no second "order book outruns the factory" piece), (2) a claim
  resting on primary sources (filings, regulators, grid operators), not press
  reports of them, and (3) something a PM would learn beyond the headline. A
  draft that fails is held, not published. Recommend short lists.
- **Scope is AI and energy infrastructure only.** No commodities, shipping,
  general equities or macro. The narrowness is the asset. **One exception:
  oil** (Tommy, 29 Oct 2026), because it is part of the energy sector. Oil
  pieces explain the physical system (production, pipelines, refining, how it
  meets power and gas) under the same rules as every piece: no price
  forecasts, trading views or views on shares. See WRITING-FORMAT.md §5.
- **Financials as evidence, never a view on the shares, in journal pieces.** A
  company's own disclosed figures (revenue, margins, backlog, capex, order
  books) may appear in a piece when they test or confirm the physical
  mechanism, dated and sourced to the filing. Never a share price, market
  value, valuation multiple, target, rating, recommendation, or claim that a
  share is cheap or expensive, in a journal piece or on any page **except
  research notes (`/research`, its note pages and PDFs, and the track record)**. Keep them out of
  the exposure map, which stays "what they make" only. See WRITING-FORMAT.md
  §4a and CALLS-SPEC.md.
- **Never post to LinkedIn from Tommy's personal profile.** The company page
  only. Verify the composer identity reads "The Physical Layer" before submitting.
- **Scheduling the LinkedIn post is the last step of publishing, and it is
  Claude's job** (Tommy, 12 Oct 2026). A piece is not done until its post is
  scheduled on the company page and marked "scheduled" in
  `brand/linkedin-posts.md`. Never finish with a reminder for Tommy to do it.
  Every scheduled publish task ends with this step. See WRITING-FORMAT.md §8
  step 7.
- **The deep piece: fewer, deeper, layered** (Tommy, 30 Oct 2026; replaces
  the 8 and 9 Oct length and numbers rules, which are retired, and applies to
  every future piece). The journal is being consolidated from 61 short pieces
  into about 11 deep pieces, one per mechanism cluster. New topics deepen an
  existing deep piece; there are no new standalone pieces.
  Each deep piece has two layers on one page: a plain-English top (claim, why
  it matters, the key number, analogy; about 400 to 550 words, still readable
  by a layman) and an investor layer below it (the numbers, the mechanism or
  model, company and site sections, claims on record, exposure map, falsifier,
  links to research notes). The old 15-figure and 450 to 600 word limits apply
  to the top layer only; every investor-layer number is primary and dated. Share prices, valuations and views on shares still never
  appear in a journal piece. Spec: WRITING-FORMAT.md §D. Plan:
  research-build/CONSOLIDATION-PLAN.md.
- **Merging keeps the record** (Tommy, 30 Oct 2026). When pieces merge, every
  old URL redirects to its section in the deep piece (`/journal/<deep>/#<old-slug>`),
  every claim stays in claims.ts word for word with its original date, and the
  deep piece shows each one in its "Claims on record" block. Research notes are
  untouched and keep pointing at the same claim ids. The original text of each
  merged piece is kept in `research-build/archive-pieces/` and never edited.
- House style: no em dashes, British spelling, 14 to 20 word sentences.

## The site around each piece

A new piece is not published until the site around it is updated. Every time:

- **The map.** Add the slug to one layer in `src/data/stack.ts`. Every piece,
  no exceptions. The descent at the top of the homepage reads the same file; a new
  layer also needs its own stop drawn in `src/components/Descent.astro`. If no layer fits, add a new layer in its physical place in
  the chain rather than forcing the piece into the nearest one.
- **The claims page.** For an Analysis piece, add an entry to
  `src/data/claims.ts`: the thesis in one sentence, the falsifier, and the
  evidence watched. The claim and test are never reworded later. The claims
  list keeps no statuses (Open, Holding and so on) and no reviews: Tommy
  decided it is a plain list of claims. Do not add status tracking to it or
  suggest it. Scoring lives only in the research track record, for calls. If a note
  disagrees with a published claim, the pitch says so openly and, if needed,
  a new dated claim is added beside the old one. Never a silent fix.
- **The numbers.** If the piece rests on a new structural figure, add it to
  `src/data/numbers.ts`. Physical figures only, never anything about shares.
- **Companies** build themselves from the exposure map. Spell company names
  consistently. A company gets a page of its own only if it has a research
  note, a heading in a piece's investor layer, or at least two mentions in a
  piece's running prose outside the exposure map; every other company URL
  redirects to `/companies/` (Tommy, 30 Oct 2026; `companyPages` in
  `src/lib/exposure.ts`). There are no topic pages; the map does that job.

**The top menu is fixed at five: Journal, Research, Claims, Glossary, About**
(Tommy, 30 Oct 2026). Tommy found nine items too crowded. Do not add to it.
The map is the homepage: the descent sits at the top of `/`, then the layer
sections with their deep pieces, so Journal is the map and `/map/` redirects
to `/` (`/map/#<layer>` lands on `/#<layer>`). Start here was removed and
`/start/` redirects to `/`. Numbers and Companies live in the footer, with
Claims also there; any new reference page goes in the footer too.

The checker fails a piece missing from the map, or an Analysis piece missing
from the claims page. See WRITING-FORMAT.md §6a.

**No email sign-ups.** Tommy has decided against a newsletter or sign-up form
anywhere on the site. Do not add one or suggest one. Readers follow via the
LinkedIn company page and RSS.

## Before every publish

```bash
python3 brand/check-piece.py src/content/journal/<slug>.md
python3 brand/check-call.py            # research notes
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py
npm run build
```

The checker must exit clean. Bump `OG_VERSION` in `src/config.ts` only when the
artwork of an existing card changes, because LinkedIn caches card images by URL.
