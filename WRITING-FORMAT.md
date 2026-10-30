# The Physical Layer: the formula

How every piece on this site is built. If you hand Claude raw notes and say "make this a journal
post", this is the contract it works to. Nothing here is a suggestion. Retired rules are kept as
history in `research-build/archive/RETIRED-RULES.md` and are not in force.

> ## THE FIRST RULE. FEWER, DEEPER, LAYERED. (Tommy, 30 Oct 2026, permanent)
> The journal is a small set of deep pieces, one per mechanism cluster, each written in two layers on
> one page (§D): a plain-English top a layman can follow in about five minutes, and an investor layer
> below it with the numbers, the mechanism, the company and site sections, the claims on record and
> the falsifier. A PM or investor who reads any piece first must come away thinking the author knows
> the subject in depth. New work takes one of two tracks (CLAUDE.md, "Two tracks for new work"): a new
> deep piece for a distinct mechanism or market, or an update to an existing deep piece; sourcing is §E.
> Every piece must clear the quality bar in CLAUDE.md. The old whole-piece word and figure caps now
> apply only to the top layer (§D, §4b).

---

## D. THE DEEP PIECE (Tommy, 30 Oct 2026). The format for every piece. §3 and §4b below now apply only where they say so.

Every piece is a deep piece, one per mechanism or market, in two layers on one page. The top layer
is for a layman; the investor layer carries the depth.

**Top layer: In plain English** (about 400 to 550 words, 15 figures at most, a layman can follow it)
1. Summary (frontmatter, §2).
2. Cold open ending on the thesis alone on its line, as §3.1.
3. The analogy block, as §3.2.
4. `## How it works`: the mechanism, why supply cannot simply catch up.
5. `## The number that matters`: one or two figures and what they mean.
Then a divider line: `<hr class="layer">` followed by `<p class="layer-label">For investors</p>`.

**Investor layer** (about 1,200 to 2,500 words; numbers allowed, every one primary-sourced and dated)
6. `## The mechanism in depth`: the full chain, with a table where it helps (lead times, backlog in
   years of work, MW booked against drawn, per-unit content). Tables are markdown tables.
7. One `##` section per company, site or market the cluster covers, each opening with an anchor
   `<a id="<old-slug>"></a>` for every merged piece it replaces, so redirects land there. Each section
   carries that piece's evidence, now with the numbers.
8. `## Claims on record`: every claim from the merged pieces, quoted word for word from claims.ts
   with its original date and falsifier, then any new dated claim for the deep piece. Never reworded.
   Where later evidence cuts against an old claim, say so here openly, in the "Where I was wrong" style.
9. `## What would prove me wrong`: the deep piece's own falsifier.
10. `## Research notes`: links to each initiation note in `/research/` that rests on these claims.
11. The exposure map (§3.4 rules unchanged; up to six groups).
12. Sources (one paragraph naming institutions and documents with dates, ending "Personal research,
    not investment advice."). Credit third-party leads (videos, SemiAnalysis) once.

Still forbidden anywhere in a piece: share prices, market values, valuation multiples, targets,
ratings or any view on shares (those live in the research notes). Financials appear only as evidence
for the mechanism (§4a). No em or en dashes. British spelling.

---

## E. Finding new material (Tommy, 30 Oct 2026)

Every lead is a lead only until its figures are read at the primary source. Six channels, in order of
value:

1. **The calendar.** Each deep piece's companies, grid operators and regulators publish on a known
   schedule: quarterly results and filings, regulator orders and dockets (FERC, PJM, ERCOT, NERC, EMA,
   IMDA, Energy Commission, Tenaga, SPAN, NRC), statistical releases (EIA, CAISO). These test the claims
   on record and feed updates. A monthly sweep lists what landed for each piece.
2. **The claims' own watch lists.** Every claim in claims.ts names the evidence to watch; that list is the
   standing to-do for updates.
3. **Videos and podcasts Tommy saves** (YouTube Watch Later). Claude pulls the transcripts, maps each one to
   the deep pieces, and proposes only what is new: an update, or a candidate new deep piece. Third-party
   work is a lead sheet: never copied or paraphrased, credited once.
4. **Analyst framing from free text** (for example SemiAnalysis previews) as a map of gaps: where the site
   can add a mechanism or an APAC angle they do not cover. Never paywalled content.
5. **Gaps in the map.** A market or mechanism the map has no piece for (for example Hong Kong, or fuel for
   power) is a candidate new deep piece; it needs its own primary sources before drafting.
6. **Tommy's own work:** interviews, calls and job-hunt research that surface a question the site cannot
   yet answer.

Every candidate is proposed to Tommy as one line (update to which piece, or new deep piece, plus the claim
it would carry) before any drafting.

---

## 0. What Claude needs from you

Send notes in any shape. Bullet points, a voice-note transcript, a half-written
paragraph, a screenshot of a chart. The only things that must be in there:

1. **The claim.** One sentence. What is true that most people have wrong?
2. **The mechanism.** Why it is true, physically. Not "the market thinks", but
   what actually happens in the wire, the loop, the rack, the queue.
3. **The number that matters.** One or two, no more (§4b). Structural first. The air
   ceiling in kW per rack. The ratio of water to air. Two years for a substation.
   A company's disclosed financials can support it, never replace it. See §4a.
4. **Who operates in the layer.** Names of real companies, and who is hurt.

If a piece of that is missing Claude will ask for that one thing rather than
invent it. Everything else, including the title, the analogy, the section
breaks, the summary and the LinkedIn post, Claude writes.

**The subject stays the subject.** If the notes are about one company, one project or one policy, that is the
subject of the piece, and it stays the subject. Name it in the title, in the
summary, in the cold open and in the thesis line, and carry it through every
section. Use it to explain the layer, but never abstract it away into a
generic industry piece that mentions it only in passing. The exposure map lists
it first.

---

## 1. The category

The `category` field takes `Explainer`, `Analysis` or `Note` (§2). An **Analysis** piece makes a
claim about what the market has mispriced. It carries a prediction, so it **must** contain a
`## What would prove me wrong` section and an entry in `src/data/claims.ts`. Every deep piece
carries a dated claim and its own falsifier (§D), and every live piece is Analysis.

---

## 2. Frontmatter

```yaml
---
title: "The rack runs out of copper before it runs out of chips"
date: 2026-09-24T13:43:00+08:00
summary: "AI computers are getting so power-hungry that the copper bars carrying electricity inside each cabinet would soon weigh more than the computers. So the industry is about to change how power enters the building. That change, not the chips, is what decides who gets to build."
category: "Explainer"
cover: "/covers/copper-rack.svg"
tags: ["power", "data-centres", "800VDC"]
---
```

| Field | Rule |
|---|---|
| `title` | Sentence case, never title case. A claim or a plain question, 8 to 16 words. May be two sentences. Must be understandable by someone who has never read the site. If the piece is about one company or project, the title names it. |
| `date` | The real moment the piece goes live, as `YYYY-MM-DDTHH:MM:SS+08:00` in Singapore time. Set it when you publish, never a planned, back-dated or future date. The full time keeps pieces published on the same day in order. The checker fails any date in the future. |
| `summary` | Two or three sentences, plain English, zero jargon. **The hardest-working field on the site**: it renders in the "In plain English" box at the top of the piece, on the home-page card, as the meta description, and as the LinkedIn card subtitle. Write it last, after the piece exists. |
| `category` | `Explainer`, `Analysis` or `Note`. Shown on the card and on the social image. |
| `cover` | `/covers/<slug>.svg`. Effectively required: it is also the social card, on its own. See §7. |
| `tags` | Two to four, lowercase, kebab-case. Reuse existing ones where they fit: `power`, `data-centres`, `cooling`, `networking`, `memory`, `the-stack`, `grid`, `explainer`. |
| `draft` | Optional, defaults false. `true` hides the piece everywhere while you finish it. |
| `shortLabel` | Legacy. Nothing reads it any more. Leave it out. |

The filename is the slug and the URL: `src/content/journal/<slug>.md` becomes
`thephysicallayer.fyi/journal/<slug>/`. Short, lowercase, hyphenated, no dates
in it. It can never change once published without breaking links.

---

## 3. The body, in order

These rules apply to the top layer of a deep piece (§D), and §3.4 and §3.5 to the exposure map and sources below the divider.

### 3.1 Cold open, three or four short paragraphs, about 80 words

No throat-clearing, no "in this piece I will". Open on one of four moves:

- **A question the reader has never asked.** "Start with a question you have probably never asked: where does the answer come from?"
- **A claim offered up for attack.** "Here is a claim I am willing to be wrong about in public: the thing holding back the AI buildout is not the chip. It is the wire."
- **A correction.** "There is a widespread assumption that AI is limited by how fast a chip can do maths. For the part of the job you actually experience, that is wrong."
- **A fact with a payoff.** "There is a fact about computers that most people never think about, and once you know it the whole cooling industry makes sense."

The open **ends on the thesis, alone on its own line**, short and flat:

> Getting that heat out of the building is not a support function. It is half the job.

### 3.2 The analogy block

Immediately after the open, before the first `##`. The summary line is fixed
text and never changes.

```html
<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>The everyday comparison. Domestic scale, household objects.</p>
<p>Why the obvious fix does not work.</p>
<p>The one image that carries the whole argument.</p>
</details>
```

Two `<p>`, about 70 words in all. Rules:

- Objects a person already owns or has stood next to. Laptops on knees,
  hairdryers, a wardrobe, a swimming pool on a breezy day, a kitchen countertop,
  a queue at a counter.
- **No finance comparisons.** Not portfolios, not spreads, not P/E. The whole
  point is that the reader has no finance background.
- Build in order: the familiar thing, then the scale, then why the naive fix
  fails, then the image that transfers.

### 3.3 Section headings

Headings are short and plain, sentence case, no numbering.

- **How it works.** The physical mechanism, with any jargon defined in the sentence where it
  appears. It includes, in two or three sentences, why supply cannot simply catch up.
- **What would prove me wrong** (investor layer, §D). Names the observable that would kill the
  claim. Same test as the claims page, said plainly.

Where a section lists options, use bold lead-ins rather than bullets:

```markdown
**Direct-to-chip.** This is the mainstream answer in 2026. A metal plate with
liquid channels sits directly on each chip...
```

### 3.4 The exposure map

Just before the closing `---`.

```html
<section class="exposure">
<h3>Who is exposed if cooling moves to liquid</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>The one-stop suppliers</dt>
<dd><span class="names">Vertiv</span> sells both the power gear and the liquid cooling, which is rare.</dd>
<dt>The specialists</dt>
<dd><span class="names">CoolIT</span> makes cold plates shipping inside many brand-name servers.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Air-only cooling incumbents, and existing buildings whose plumbing cannot take liquid without a refit.</dd>
</dl>
</section>
```

- `<h3>` is always "Who is exposed if \<the claim\> is right", phrased for the piece.
- The `<p class="note">` disclaimer **opens with this exact sentence pair** and
  is never reworded: "This maps who operates in each layer. It is not a
  recommendation, and naming a company is not a view on its shares." A piece may
  add one further statement after it, as every live piece does when it says the
  figures are disclosures used as evidence for the mechanism.
- Three or four `<dt>` groups (up to six in a deep piece, §D), one short line each, about 120 words for the whole map. Each `<dd>`
  says **what the company makes**, and nothing else. When trimming, merge groups rather than drop
  names: company pages are built from these names.
- Company names go inside `<span class="names">`.
- The `<dl class="against">` block is **mandatory for any piece making a
  directional claim**, which is every Analysis piece and almost every Explainer.
  The single exemption is a whole-stack orientation map, where the box lists the
  entire industry and there is genuinely no loser.
- **Never** in the map: market share, backlogs, revenue, margins, ratings,
  price targets, valuation, or any view on shares. Financial evidence belongs
  in the body under §4a, not here. The map says what companies make.
- Where the AI layer map says you hold no view, say so inside the box. The
  chip supply chain piece ends its map with a `<dt>Where I stop</dt>` doing exactly that.

### 3.5 The sources line

After the closing `---`, one paragraph, no heading:

```html
<p class="sources">...</p>
```

Name the institutions and documents, with dates (§D item 12).
"Sources: Energy Market Authority, EDB and JTC, Tenaga Nasional disclosures,
Wood Mackenzie, EIA and ERCOT... Figures as reported on the dates cited."

Every sources line ends with the same five words: **Personal research, not investment
advice.**

---

## 4. House style

- No em dashes, no en dashes.
- Parentheses almost never.
- Semicolons sparingly.
- British spelling always: centres, energised, analysed.
- Sentences short: 14 to 20 words on average.
- Paragraphs short: 1 to 4 sentences.
- Length: top layer about 400 to 550 words (a five minute read); investor layer about 1,200 to
  2,500 words (Tommy, 30 Oct 2026, §D).

Voice:

- **Second person for the reader's own experience.** "A laptop gets warm on your knees."
- **First person for judgement, and only for judgement.** "I read acquisitions
  like that as revealed preference." "I have no view on the memory equities."
- Confident about mechanism, explicitly uncertain about prediction.
- Numbers: words for small counts, digits for technical quantities. "eighty
  space heaters", but "120 kilowatts" and "30 to 50 kilowatts".
- Units spelled out on first use, abbreviated after. Kilowatts, then kW.
- **Every piece of jargon is defined in the sentence where it first appears**,
  even when it is in the glossary. "a unit called a CDU, the coolant
  distribution unit, which is effectively the rack's heart".

Never appears in a journal piece, or anywhere on the site except pitch pages
(`/research`, its note pages, PDFs and track record): a share price, a market value, a
valuation multiple, a target, a rating, a recommendation, a portfolio position,
or a claim about a share being cheap or expensive. Pitches follow
`CALLS-SPEC.md`.

---

## 4a. Financial evidence

A company's reported numbers are allowed when they are evidence for the
physical argument. The test: **does the figure tell the reader whether the
mechanism is real, or does it tell them what to do with the shares?** Only the
first is allowed.

Allowed, in the top layer within the §4b budget of three, and in the investor layer without a cap (§4b):

- Revenue, product versus service mix, growth rates, gross margin, cash flow,
  capex, backlog, order books, contracted capacity, customer concentration.
- Always the company's own disclosure, with the period and the filing or
  release date. Never a figure lifted from a video, a newsletter or a forecast
  by someone else.
- Always tied to the mechanism in the next sentence. "Margin rose while volume
  more than doubled, which is what a time premium looks like in money" is the
  shape. A number left standing alone is decoration.
- Where a piece makes a claim, a financial figure can be the falsifier. "If
  the premium is for time, margin should compress as grid waits shorten" is
  exactly the kind of test an Analysis piece wants.
- Jargon is still defined in place. "Gross margin, the share of each sale left
  after the cost of making it."

Never, in a journal piece:

- Share price, share price moves, market value, P/E or any other valuation
  multiple, what the price implies or assumes, targets, ratings, buy or sell
  language, "cheap", "expensive", "priced for perfection".
- Management guidance presented as your own forecast. Report it as theirs.

Anything that crosses into a view on the shares belongs in a pitch, never in
the journal piece. A research note is separate (`src/content/calls/<slug>.md`, published as a PDF and model at `/research`)
with its own rules in `CALLS-SPEC.md`: it may carry prices, valuation, a
target and Tommy's call, and links back to the claim it rests on. The journal
piece stays free of all of it. The sources line names the filings used,
and the exposure disclaimer adds that the figures are used as evidence for the
mechanism and imply nothing about value.

---

## 4b. Numbers (rewritten 30 Oct 2026)

**Now:** the top layer keeps the budget below (15 figures at most, 3 company financial figures at
most, never two money figures in one paragraph), so a layman can follow it. The investor layer has no
figure cap: every number is primary-sourced and dated, tied to the mechanism, and tables are welcome.
Still never anywhere: share prices, market values, valuation multiples, targets, ratings or any view on
shares; those live in the research notes.

### The top-layer budget (Tommy, 8 Oct 2026)

The top layer is for a layman with no finance background. It explains. A top layer that reads like
an accounting booklet has failed, however accurate it is.

- **15 figures at most** in the top layer, counting dates. Most pieces need fewer.
- **3 company financial figures at most** (revenue, growth, margin, orders,
  backlog, capex, deal sizes). Prefer one. Say it in words where you can:
  "Systems has outgrown catalogue parts for a year" beats a table of quarters.
- **Never two money figures in the same paragraph**, and never a paragraph that
  walks through a set of accounts, segments or quarters.
- Structural, physical numbers (kilowatts, years of waiting, distances) are the
  ones worth keeping. Financial detail, segment splits, quarter-by-quarter
  comparisons, guidance and deal arithmetic go in the investor layer or the research note, never
  in the top layer.
- A falsifier may still name one disclosed figure as its test, stated once and
  plainly. The precise wording lives on the claims page.
- If you need a number to make the point land, use it. If the point lands
  without it, cut it.

---

## 5. Scope

AI and energy infrastructure. Nothing else.

Power, grid connection, substations and queues, data centre construction,
cooling, rack power delivery, networking and optics, memory and packaging, and
the supply chains that gate any of them.

Not on this site: commodities, shipping, general equities, macro, anything that
belongs in the separate market-views notes. The narrowness is the asset.

The one exception is oil (Tommy, 29 Oct 2026): it is part of the energy sector,
and the site covers the energy sector. An oil piece explains the physical
system, such as production, pipelines, refining and where oil meets power and
gas, in the same format and under the same rules as every other piece. It
carries no oil price forecast, no trading view and no view on shares; those
stay in the market-views notes. Other commodities remain out.

Do not write above your own layer map. If a piece would require claims about
wafer-fab process technology or semiconductor design, stop at the layer where
the mechanism is still physical.

---

## 6. The glossary is part of the job

Any term a new reader could stumble on must exist in `src/pages/glossary.astro`,
grouped under one of the four existing headings. Adding a piece that introduces
a term without adding the glossary entry is an incomplete publish.

---

## 6a. The site around the piece

A piece is not finished when the Markdown is. Four other pages read from it,
and two of them need a line from you. The checker fails the piece until they
have it.

**The map, `src/data/stack.ts`. Every piece.** Add the slug to the `pieces`
list of the one layer it explains. The map, the "On the map" line under the
piece and the company pages all read from this. If no layer genuinely fits, add
a new layer to `STACK` in its physical place in the chain, with a plain `what`
and `constraint` sentence, rather than forcing the piece into the nearest one.

**The descent at the top of the homepage (`src/components/Descent.astro`).** A piece in an existing
layer needs nothing more: the layer text and piece counts are read from `stack.ts`. A **new
layer** appears in the layer index and the closing funnel on its own, but its own stop in the
descent (a drawing, in its physical place in the chain, plus its step cards) is drawn by hand
as part of publishing that piece. The stop counter counts drawn stops itself.

**The claims page, `src/data/claims.ts`. Every Analysis piece.** Add one
entry: `claim` is the thesis in one sentence, `breaksIf` is the falsifier from
"What would prove me wrong", and `watch` is its list of evidence. The page
lists every claim with its date, newest first. The claim and the test are fixed
on the day the piece goes live and are never reworded afterwards.

There are no statuses and no reviews. The page is a plain, dated record of what
was claimed and what would prove it wrong, by decision. Do not add status
tracking back.

**The numbers, `src/data/numbers.ts`. Optional.** If the piece rests on a
structural figure that is not already there, add it: power, distance, time or
capacity, never anything about the shares. When a figure is overtaken, update
it there with a `note`, and give the piece `updated` and `updateNote` in its
frontmatter rather than quietly editing history.

**Editing a published piece for length or clarity needs no update line** (Tommy, 8 Oct
2026). Shortening, tidying or rewording a piece without changing what it says is
just editing: no `updated`, no `updateNote`. The update line is only for a figure
that was overtaken and corrected. The claim and test on the claims page are
still never reworded.

**No email sign-ups.** The site has no newsletter or sign-up form, by
decision. Do not add one. LinkedIn and RSS are how readers follow.

**Companies. Automatic.** The company list is built from the names in each
exposure box's `<span class="names">`. A company gets a page of its own only if it has a research
note, a heading in a piece's investor layer, or at least two mentions in a piece's running prose
outside the exposure map; every other company URL redirects to `/companies/` (Tommy, 30 Oct 2026;
`companyPages` in `src/lib/exposure.ts`). Spell a company the same way each
time; `ALIAS` in `src/lib/exposure.ts` catches the odd variant. Tags show as
plain labels on the piece; there are no topic pages, because the map does that
job.

**The top menu is fixed at five: Journal, Research, Claims, Glossary, About**
(Tommy, 30 Oct 2026). Do not add a sixth. The homepage is the map. A new
reference page goes in the footer, the way Numbers and Companies are.

---

## 7. The cover image

`public/covers/<slug>.svg`, `viewBox="0 0 800 600"`.

Dark background, same family as the others: a near-black gradient, amber
`#f59e0b` and `#b45309` for anything energy or heat, blue `#60a5fa` and
`#1d4ed8` for anything compute or data. One diagram idea only, drawn in flat
shapes, with a small uppercase caption in letter-spaced grey.

Draw it bold. The diagram fills a centred frame, roughly x 110 to 690 and
y 110 to 480, with no empty band on either side. Labels are 16 to 20 px, strokes
4 to 6 px, and there is as little text as the idea allows. Tiny secondary lines
of text do not survive thumbnail size, so leave them out. Where the piece has a
named subject, the caption names it too.

The social card is the cover and nothing else: no title, no scrim, no logo.
Words over the artwork look cluttered, and LinkedIn already prints the title
under the image. `brand/make-og.py` frames each card around the cover's own
drawing at 1200 by 630 and stretches the cover's background to fill the width.
It needs the background as a plain `<rect width="800" height="600" fill="url(#id)"/>`
directly after `<defs>`.

---

## 8. Publish checklist

```bash
cd ~/Desktop/journal
python3 brand/check-piece.py src/content/journal/<slug>.md
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py
npm run build
git add -A && git commit -m "New piece: <title>" && git push
```

In order:

1. `src/content/journal/<slug>.md` written and complete, both blocks present.
2. `public/covers/<slug>.svg` in place, then `brand/check-piece.py` passes.
3. Any new terms added to the glossary. The slug added to a layer in
   `src/data/stack.ts`, and for an Analysis piece, its entry in
   `src/data/claims.ts` (§6a).
4. Regenerate the social cards. They are written to
   `public/og/<slug>-<OG_VERSION>.png`. If the artwork of an **existing** card
   changes, bump `OG_VERSION` in `src/config.ts` first, because LinkedIn caches
   by URL.
5. Build clean, then push. GitHub Pages publishes in about a minute.
6. Run the new URL through LinkedIn's Post Inspector so the card is cached
   before anyone shares it:
   `linkedin.com/post-inspector/inspect/<url-encoded URL>`
   The same step usually fixes a changed cover after the fact: re-running Post
   Inspector on a URL updates the thumbnail on most posts that already link to
   it. Not all. A post whose link preview was ever edited or dismissed in the
   composer keeps its old thumbnail for good. Check the scheduled list after
   re-running, and for any that did not update, delete the post and schedule a
   fresh copy with the same text. Never remove a link preview from a post while
   editing it; LinkedIn will not regenerate it inside that edit.
7. **The last step, and it is Claude's job, not Tommy's (Tommy, 12 Oct 2026,
   permanent).** Add the LinkedIn post to `brand/linkedin-posts.md`, then
   schedule it yourself from the **company page only**, never the personal
   profile, in Tommy's Chrome (Claude in Chrome; the built-in browser is not
   signed in). Confirm the composer's author reads "The Physical Layer" before
   typing. Schedule, never post now. Verify it in the scheduled list, then mark
   the post "scheduled" in the file and push. **A piece is not published, and
   the job is not finished, until its LinkedIn post is scheduled.** Never end a
   publish, by hand or by scheduled task, with a reminder for Tommy to do it.
   If something blocks it, say "NOT DONE: LinkedIn post not scheduled" at the
   top of the report. A scheduled publish task carries this as its final step.

---

## 9. The LinkedIn post that goes with it

One per new piece and one per substantial update (CLAUDE.md, "Two tracks for new work"), in
`brand/linkedin-posts.md`. Fixed shape, four blocks separated by blank lines:

```
[One sentence. The counterintuitive fact, stated flat.]

[Two or three sentences. The scale, the consequence, and the reason it matters
beyond one company.]

[One sentence saying what the piece actually covers, as a list of three.]

https://thephysicallayer.fyi/journal/<slug>/

#Tag #Tag #Tag
```

Rules: plain register, first person, three hashtags maximum, the link alone on
its own line at the end so LinkedIn renders the card. Posts go out at 11:30 AM
Singapore time on Mondays, Wednesdays and Fridays only (Tommy, 7 Oct 2026), each
new post taking the next free slot after the last scheduled one. The record of
the queue is `brand/linkedin-posts.md`: every post's heading carries its slot and
"scheduled" once it is in LinkedIn. LinkedIn's desktop list shows only the first
ten scheduled posts, so take the next free slot after the latest date marked
scheduled in the file.

---

## 10. The checker

Most of this document is machine-checkable, so it is checked.

```bash
python3 brand/check-piece.py                         # every published piece
python3 brand/check-piece.py src/content/journal/my-slug.md
```

It validates the frontmatter, both mandatory blocks, the fixed disclaimer, the
sources tail, the falsifier on Analysis pieces, banned punctuation, US spellings,
rating and valuation language, and average sentence length. A piece with
`<hr class="layer">` is checked as a deep piece (§D): it fails without exactly one divider and
its label, the top layer's two sections, the investor layer's Claims on record and falsifier in
order, a claims.ts entry, and every claim it carries quoted word for word and anchored. It also
fails if the top layer is outside 300 to 600 words or has more than 15 figures, if the investor
layer passes 2,600 words before the exposure map, or if the top layer has more than 4 money
figures. Failures exit non-zero. Warnings are advisory and do not fail.

Run it before you build. Every published piece passes with no failures.

---

## 11. The finished-piece checklist

- [ ] Category set (§1); a `## What would prove me wrong` section and a dated claim (§D)
- [ ] If the notes are about one company or project, it is named in the title, summary, open and thesis, and stays the subject throughout
- [ ] `date` is the real publish time, not a planned or future one
- [ ] Cold open ends on the thesis, alone on its line
- [ ] Analogy block present, fixed summary line, household objects, no finance
- [ ] Top layer has `## How it works` and `## The number that matters`; investor layer sections in §D order, sentence case
- [ ] Exposure map present, with the fixed disclaimer and an "on the other side" block
- [ ] No share price, valuation, target, rating or recommendation anywhere
- [ ] Any financial figure is the company's own, dated, sourced, and tied to the mechanism
- [ ] Sources paragraph, ending "Personal research, not investment advice."
- [ ] Every jargon term defined in place, and present in the glossary
- [ ] On the map in `stack.ts`; if Analysis, on the claims page in `claims.ts`
- [ ] No em dashes. British spelling. Top layer about 400 to 550 words; investor layer about 1,200 to 2,500 (§D)
- [ ] Numbers (§4b): top layer within its budget; every investor-layer number primary-sourced and dated
- [ ] Claims on record quote every merged claim word for word with its original date (§D)
- [ ] Cover SVG in place, social card regenerated, build clean
