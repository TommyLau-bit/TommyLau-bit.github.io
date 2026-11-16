# The Physical Layer

**★ JOURNAL ONLY (Tommy, 6 Nov 2026 ~17:30, permanent until he says otherwise).** After the Max Hopkins (CLSA) call: the pieces are good but Tommy could not back them up, and 33 notes was far too many. The site is the journal, the Power roster and About only (Power added by Tommy, 11 Nov 2026: one page of player cards for every way to power an AI data centre, five ratings each worked out from a sourced number; data in src/data/power.ts). The Research page, the paper book and all initiation notes and models are OFF the site (source, PDFs and models archived in research-build/archive/research-page-2026-11-06/; old /research, /calls and /companies URLs land on the homepage). Pieces carry no "Research notes" section and no note links. Both scheduled tasks (`physical-layer-book-daily`, `journal-daily-scan`) are DISABLED: nothing is published, drafted onto the site or scheduled without Tommy. Depth over breadth: Tommy must be able to defend every piece from his own head; never add a page, note or feature he has not asked for. One sector (Tommy, 9 Nov 2026): the journal covers power for AI data centres only, told as one story in seven chapters (Tommy, 9 Nov 2026 evening): Johor, America, the equipment queue, building your own power, solar and batteries, nuclear, microreactors, from the grid connection to the reactor. Powering the rack and Heat and water were removed (archived in research-build/archive/rack-and-heat-pieces-2026-11-09/, URLs redirect home); the orbit piece was removed everywhere (archived in research-build/archive/orbit-piece-2026-11-09/), and a new piece must sit on that chain. Never state a count of pieces on the CVs, which change only when the work does. Company notes never return to the site (Tommy, 8 Nov 2026): the site is the mechanism only; company studies Tommy writes himself (BWXT first) go to the jobs folder, never here. Show output only, never how the site is run.


Tommy's public journal on AI and energy infrastructure. Astro static site,
GitHub Pages, live at https://thephysicallayer.fyi

**Trigger "1" = the journal run** (Tommy, 10 Nov 2026; the job hunt is "2"): the whole job on the site and everything that quotes it, step by step in `research-build/THE_JOURNAL_RUN.md`. "1" is his go-ahead for fact-checked updates and loose ends; new pieces, chapters, company studies and calls still wait for his word.

**Every journal session starts with `research-build/HANDOVER.md`** (what is
scheduled, open flags, what was done each day). Rewrite its START HERE at the
end of the session.

## Retired machinery (deep clean, 9 Nov 2026)

The research notes, the paper book, calls and the daily scan are gone from the repo; their
source is in `research-build/archive/research-page-2026-11-06/` (with `CALLS-SPEC.md` and the
note build folders in `notes/`) and the full instructions as they were are in
`research-build/archive/retired-2026-11-09/CLAUDE.pre-clean.md`. Old note and company URLs
redirect home from the fixed lists in `src/data/retired-urls.ts`; never add to them.

- **No dated corrections, ever** (Tommy, 2 Nov 2026, permanent). When a fact in a piece is
  found wrong, edit it so it is simply right: the sentence, the chart, the evidence table.
  No "Correction" paragraphs, no "Where I was wrong", no `correction` field. The claims in
  claims.ts are corrected in place when a fact in them is wrong (Tommy, 7 Nov 2026), never
  otherwise reworded; the archived original text of merged pieces is never edited.

## Before writing or editing any piece, read `WRITING-FORMAT.md`

It is the complete spec and it is not optional: the deep piece format (§D),
sourcing (§E), frontmatter, house style, scope, the cover, the publish
checklist and the matching LinkedIn post. Agent briefs for drafting,
fact-checking, gap scouting and updates are in `research-build/deep-pieces/`.

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
  share is cheap or expensive, in a journal piece or on any page. Keep them out of
  the exposure map, which stays "what they make" only. See WRITING-FORMAT.md
  §4a.
- **Never post to LinkedIn from Tommy's personal profile.** The company page
  only. Verify the composer identity reads "The Physical Layer" before submitting.
- **Scheduling the LinkedIn post is the last step of publishing, and it is
  Claude's job** (Tommy, 12 Oct 2026). A piece is not done until its post is
  scheduled on the company page and marked "scheduled" in
  `brand/linkedin-posts.md`. Never finish with a reminder for Tommy to do it.
  Every scheduled publish task ends with this step. See WRITING-FORMAT.md §8
  step 7.
- **The deep piece: fewer, deeper, layered** (Tommy, 30 Oct 2026). Every
  piece is a deep piece, one per mechanism or market, with two layers on one
  page: a plain-English top readable by a layman, and an investor layer below
  it where every number is primary and dated. Share prices, valuations and
  views on shares never appear.
- **Every piece is a story** (Tommy, 31 Oct 2026). It grabs the reader, builds,
  reaches a climax with the strongest evidence and charts, and ends by tying
  everything together. One spine and one claim, stated by paragraph three; no
  section per company; two to four charts, each proving one sentence. The rules
  are `research-build/deep-pieces/STORY-RULES.md`, and the checker enforces the
  core of them. Spec: WRITING-FORMAT.md §D.
- **Two tracks for new work** (Tommy, 30 Oct 2026; replaces "no new
  standalone pieces"). Ten is not a ceiling. (1) **A new deep piece** when the
  topic is a distinct mechanism or market none of the existing pieces covers
  and it can carry the full §D format: plain-English top, investor layer, its
  own dated claim, primary sources. It never repeats an existing mechanism
  with a different company name. (2) **An update** to an existing deep piece
  when new evidence lands on a mechanism the site already covers (results, a
  regulator's order, a filing, a transcript that adds a fact): a section or
  table refresh or a new dated claim beside the old ones, a separate
  fact-check and Tommy's OK. The piece never says it was updated: no
  `updated` or `updateNote` fields, no update line (Tommy, 9 Nov 2026, permanent).
  Both tracks must clear the quality bar, and each new piece or substantial
  update gets one LinkedIn post. Sourcing method: WRITING-FORMAT.md §E.
- **Merging keeps the record** (Tommy, 30 Oct 2026). When pieces merge, every
  old URL redirects to its section in the deep piece (`/journal/<deep>/#<old-slug>`),
  every claim stays in claims.ts word for word with its original date, and the
  deep piece keeps each one in its "Claims on record" block (earlier claims
  folded inside `<details class="claims-earlier">`, 31 Oct 2026). Research notes are
  untouched and keep pointing at the same claim ids. The original text of each
  merged piece is kept in `research-build/archive/pieces/` and never edited.
- House style: no em dashes, British spelling, 14 to 20 word sentences.

## The site around each piece

A new piece is not published until the site around it is updated. Every time:

- **The map.** Add the slug to one layer in `src/data/stack.ts` (four layers since 9 Nov 2026: grid, equipment, power beside the site, nuclear; no rack, cooling, chip, memory, network or orbit layers) AND place it in `CHAPTERS` in the same file with its handoff line (`next`) to the following chapter; the homepage, the chapter line and the next-chapter box on each piece, and the descent all read it. A new chapter must sit on the chain and hand off to the next with a reason already in the pieces. Every piece,
  no exceptions. The descent at the top of the homepage reads the same file; a new
  layer also needs its own stop drawn in `src/components/Descent.astro`. If no layer fits, add a new layer in its physical place in
  the chain rather than forcing the piece into the nearest one.
- **The claim.** For an Analysis piece, add an entry to `src/data/claims.ts`:
  the thesis in one sentence, the falsifier, and the evidence watched. It shows
  in the piece's claim box and claims fold (there is no claims page since
  6 Nov 2026), and the checker needs it. The claim and test are never reworded
  later; no statuses. A wrong fact in a piece's text is simply fixed in place.
- **No glossary, numbers or company pages** (Tommy, 6 Nov 2026: "amateur";
  removed, old URLs redirect). Every term and name is explained in the piece
  where it first appears (STORY-RULES 18a). Do not add these pages back.
  Spell company names consistently in the exposure map.

**The top menu is fixed at three: Journal, Power and About** (Power added by Tommy, 11 Nov 2026; Research removed 6 Nov 2026 under the JOURNAL ONLY banner; Claims, Glossary, Numbers and Companies were removed as amateur). Do not
add to it, and do not add reference pages to the footer.
The homepage is the map: under the hero, a compact list of every deep piece
by layer (grid to chip, anchored `/#<layer>`), then the descent below it as the
guided walk. `/map/` redirects to `/` (`/map/#<layer>` lands on `/#<layer>`).
Start here was removed and `/start/` redirects to `/`.

**Investor first, on every page** (Tommy, 30 Oct 2026). A visitor finds what
they came for at once: lists and tables before decoration, counts at the top,
no thumbnails in lists, no "In plain English" boxes on index pages (pieces keep
theirs), jump links where a page is long. Research opens on the book's morning
sheet; each deep piece shows "For investors" jump links under its summary.
Keep new pages to this standard.

The checker fails a piece missing from the map, or an Analysis piece missing
from `claims.ts`. See WRITING-FORMAT.md §6a.

**No email sign-ups.** Tommy has decided against a newsletter or sign-up form
anywhere on the site. Do not add one or suggest one. Readers follow via the
LinkedIn company page and RSS.

## Before every publish

```bash
python3 brand/check-piece.py src/content/journal/<slug>.md
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py
npm run build
```

The checker must exit clean. Bump `OG_VERSION` in `src/config.ts` only when the
artwork of an existing card changes, because LinkedIn caches card images by URL.
