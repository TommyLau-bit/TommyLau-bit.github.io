# The Physical Layer — the formula

How every piece on this site is built. Derived from the first six, not invented.
If you hand Claude raw notes and say "make this a journal post", this is the
contract it works to. Nothing here is a suggestion.

---

## 0. What Claude needs from you

Send notes in any shape. Bullet points, a voice-note transcript, a half-written
paragraph, a screenshot of a chart. The only things that must be in there:

1. **The claim.** One sentence. What is true that most people have wrong?
2. **The mechanism.** Why it is true, physically. Not "the market thinks", but
   what actually happens in the wire, the loop, the rack, the queue.
3. **The number that matters.** One or two. Structural, not financial. The air
   ceiling in kW per rack. The ratio of water to air. Two years for a substation.
4. **Who operates in the layer.** Names of real companies, and who is hurt.

If a piece of that is missing Claude will ask for that one thing rather than
invent it. Everything else, including the title, the analogy, the section
breaks, the summary and the LinkedIn post, Claude writes.

---

## 1. The two shapes

Every piece is one of these. Pick before writing.

**Explainer** (four of the first six). Teaches a mechanism. The reader finishes
knowing how something works. No prediction, so no falsifier needed. Examples:
the two seconds, cooling, the network, memory.

**Analysis** (two of the first six). Makes a claim about what the market has
mispriced. Carries a prediction, so it **must** contain a `## What would prove
me wrong` section. Examples: the queue, the copper rack.

A third label, **Note**, exists in the schema for something short. Unused so far.

---

## 2. Frontmatter

```yaml
---
title: "The rack runs out of copper before it runs out of chips"
date: 2026-08-07
summary: "AI computers are getting so power-hungry that the copper bars carrying electricity inside each cabinet would soon weigh more than the computers. So the industry is about to change how power enters the building. That change, not the chips, is what decides who gets to build."
category: "Explainer"
cover: "/covers/copper-rack.svg"
tags: ["power", "data-centres", "800VDC"]
---
```

| Field | Rule |
|---|---|
| `title` | Sentence case, never title case. A claim or a plain question, 8 to 16 words. May be two sentences. Must be understandable by someone who has never read the site. |
| `date` | `YYYY-MM-DD`. A weekday. Keep roughly a fortnight clear of the last piece, so the cadence stays honest. |
| `summary` | Two or three sentences, plain English, zero jargon. **The hardest-working field on the site**: it renders in the "In plain English" box at the top of the piece, on the home-page card, on the reading page, as the meta description, and as the LinkedIn card subtitle. Write it last, after the piece exists. |
| `category` | `Explainer`, `Analysis` or `Note`. Shown on the card and on the social image. |
| `cover` | `/covers/<slug>.svg`. Effectively required: it is the background of the social card. See §7. |
| `tags` | Two to four, lowercase, kebab-case. Reuse existing ones where they fit: `power`, `data-centres`, `cooling`, `networking`, `memory`, `the-stack`, `grid`, `explainer`. |
| `draft` | Optional, defaults false. `true` hides the piece everywhere while you finish it. |
| `shortLabel` | Legacy. Nothing reads it any more. Leave it out. |

The filename is the slug and the URL: `src/content/journal/<slug>.md` becomes
`thephysicallayer.fyi/journal/<slug>/`. Short, lowercase, hyphenated, no dates
in it. It can never change once published without breaking links.

---

## 3. The body, in order

### 3.1 Cold open, three to five short paragraphs

No throat-clearing, no "in this piece I will". Open on one of four moves, all
of which the first six use:

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

Two to four `<p>`. Rules:

- Objects a person already owns or has stood next to. Laptops on knees,
  hairdryers, a wardrobe, a swimming pool on a breezy day, a kitchen countertop,
  a queue at a counter.
- **No finance comparisons.** Not portfolios, not spreads, not P/E. The whole
  point is that the reader has no finance background.
- Build in order: the familiar thing, then the scale, then why the naive fix
  fails, then the image that transfers.

### 3.3 Four to six `##` sections

Headings are short and plain, sentence case, no numbering. Recurring shapes,
all drawn from the first six:

| Shape | Real examples |
|---|---|
| Definitions, placed early | "Two words you need", "Three words that unlock the rest" |
| The mechanism | "Why air stopped working", "Where copper dies and light takes over" |
| The options, as bold lead-ins | "Three ways to do it" |
| The number that turns physics into money | "The number that turns physics into money", "Two numbers that end the argument" |
| Why the market misreads it | "Why the market still treats it as a chip problem" |
| Where the value goes | "Where the value goes if I'm right", "Who benefits, if I'm right" |
| **The falsifier. Analysis only, mandatory** | "What would prove me wrong" |
| The honest limit | "The uncomfortable footnote", "Where I stop" |
| Forward look | "What I'm watching", "How I'd say this in a room" |

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
  add one further statement after it, as the memory piece does when it says the
  author holds no investment view on memory.
- Three to six `<dt>` groups. Each `<dd>` says **what the company makes**, and
  nothing else.
- Company names go inside `<span class="names">`.
- The `<dl class="against">` block is **mandatory for any piece making a
  directional claim**, which is every Analysis piece and almost every Explainer.
  The single exemption is a whole-stack orientation map, where the box lists the
  entire industry and there is genuinely no loser. The two-seconds piece is the
  one example.
- **Never**: market share, backlogs, revenue, margins, ratings, price targets,
  valuation, or any view on shares.
- Where the AI layer map says you hold no view, say so inside the box. The
  memory piece ends its map with a `<dt>Where I stop</dt>` doing exactly that.

### 3.5 The sources line

After the closing `---`, one paragraph, no heading:

```html
<p class="sources">...</p>
```

Two variants, both used:

- **Mechanism piece.** State that it explains mechanism, that the figures are
  structural rather than financial, and any position you are not taking.
  "This piece explains mechanism: why air fails, how liquid cooling works, and
  what PUE measures. The figures used are physical and structural. I hold no
  view here on individual equipment makers."
- **Sourced piece.** Name the institutions and documents, with dates.
  "Sources: Energy Market Authority, EDB and JTC, Tenaga Nasional disclosures,
  Wood Mackenzie, EIA and ERCOT... Figures as reported on the dates cited."

Every variant ends with the same five words: **Personal research, not investment
advice.**

---

## 4. House style, measured from the first six

These are not preferences. They are what the existing corpus does.

| Rule | Evidence across the six pieces |
|---|---|
| No em dashes, no en dashes | 0 of either |
| Parentheses almost never | 4 in total |
| Semicolons sparingly | 8 in total |
| British spelling always | centres, energised, analysed. 0 US spellings |
| Sentences short | 14 to 20 words average |
| Paragraphs short | 1 to 4 sentences, 18 to 28 paragraphs per piece |
| Length | 1,050 to 1,500 words, which reads as 5 to 6 minutes |

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

Never appears anywhere on the site: a price, a target, a rating, a
recommendation, a portfolio position, or a claim about a share being cheap or
expensive.

---

## 5. Scope

AI and energy infrastructure. Nothing else.

Power, grid connection, substations and queues, data centre construction,
cooling, rack power delivery, networking and optics, memory and packaging, and
the supply chains that gate any of them.

Not on this site: commodities, shipping, general equities, macro, anything that
belongs in the separate market-views notes. The narrowness is the asset.

Do not write above your own layer map. If a piece would require claims about
wafer-fab process technology or semiconductor design, stop at the layer where
the mechanism is still physical.

---

## 6. The glossary is part of the job

Any term a new reader could stumble on must exist in `src/pages/glossary.astro`,
grouped under one of the four existing headings. Adding a piece that introduces
a term without adding the glossary entry is an incomplete publish.

---

## 7. The cover image

`public/covers/<slug>.svg`, `viewBox="0 0 800 600"`.

Dark background, same family as the others: a near-black gradient, amber
`#f59e0b` and `#b45309` for anything energy or heat, blue `#60a5fa` and
`#1d4ed8` for anything compute or data. One diagram idea only, drawn in flat
shapes, with a small uppercase caption in letter-spaced grey.

It has to survive being cropped to a 16:9 social card with a dark scrim over the
left two thirds, so keep the subject centred and to the right, and keep it
legible at thumbnail size.

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
3. Any new terms added to the glossary.
4. Regenerate the social cards. They are written to
   `public/og/<slug>-<OG_VERSION>.png`. If the artwork of an **existing** card
   changes, bump `OG_VERSION` in `src/config.ts` first, because LinkedIn caches
   by URL.
5. Build clean, then push. GitHub Pages publishes in about a minute.
6. Run the new URL through LinkedIn's Post Inspector so the card is cached
   before anyone shares it:
   `linkedin.com/post-inspector/inspect/<url-encoded URL>`
7. Add the LinkedIn post to `brand/linkedin-posts.md` and schedule it from the
   **company page only**. Never from the personal profile.

Do **not** add the piece to `READING_PATH`. See the README section on why the
reading page is not a table of contents.

---

## 9. The LinkedIn post that goes with it

One per piece, in `brand/linkedin-posts.md`. Fixed shape, four blocks separated
by blank lines:

```
[One sentence. The counterintuitive fact, stated flat.]

[Two or three sentences. The scale, the consequence, and the reason it matters
beyond one company.]

[One sentence saying what the piece actually covers, as a list of three.]

https://thephysicallayer.fyi/journal/<slug>/

#Tag #Tag #Tag
```

Rules: plain register, first person, three hashtags maximum, the link alone on
its own line at the end so LinkedIn renders the card. Posts go out 8:30 AM
Singapore time, on a weekday, roughly every other day while there is a backlog.

---

## 10. The checker

Most of this document is machine-checkable, so it is checked.

```bash
python3 brand/check-piece.py                         # every published piece
python3 brand/check-piece.py src/content/journal/my-slug.md
```

It validates the frontmatter, both mandatory blocks, the fixed disclaimer, the
sources tail, the section count, the falsifier on Analysis pieces, banned
punctuation, US spellings, rating and valuation language, length and average
sentence length. Failures exit non-zero. Warnings are advisory and do not fail.

Run it before you build. All six existing pieces pass.

---

## 11. The finished-piece checklist

- [ ] One of the two shapes, and if Analysis, it carries a falsifier section
- [ ] Cold open ends on the thesis, alone on its line
- [ ] Analogy block present, fixed summary line, household objects, no finance
- [ ] Four to six `##` sections, sentence case
- [ ] Exposure map present, with the fixed disclaimer and an "on the other side" block
- [ ] No price, target, rating, market share or recommendation anywhere
- [ ] Sources paragraph, ending "Personal research, not investment advice."
- [ ] Every jargon term defined in place, and present in the glossary
- [ ] No em dashes. British spelling. 1,050 to 1,500 words
- [ ] Cover SVG in place, social card regenerated, build clean
