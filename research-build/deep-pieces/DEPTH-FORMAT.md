# The depth format (Tommy, 7 Nov 2026). Pilot: microreactors

Tommy's brief, after the CLSA call and studying microreactors: the journal is for investors and analysts, deep and detailed, "actual quality work", as if months went into each piece. Fewer pieces (five or six perfect ones beat fourteen surface ones). **Deep means detail, not complexity.** The test: a reader reads it once, properly, and understands everything. No question is left unanswered and no term is left unexplained.

Status: APPROVED (Tommy, 7 Nov 2026, on the microreactors draft: "This is exactly what I want. Exactly. It's perfect. And I expect every article to also have this level of depth and this level of quality."). The microreactors piece is the reference. This file replaces STORY-RULES for every rebuilt piece; STORY-RULES governs only live pieces not yet rebuilt. Approval of the format is not approval to publish: microreactors goes live only on Tommy's word.

## How it is written: the question chain

1. **Ask the questions a first-time reader would ask, in the order they would ask them.** Each answer opens the next question. Microreactors: what is it, and how small? → how does a reactor make heat? → what changes when it fits on a lorry? → why can't it use ordinary fuel? → why ceramic grains? → how do the two work together? → why does nobody make it? → how much is there against how much is needed? → who gets it first, and why? → why the military, not data centres? → where does that leave AI? → what would prove me wrong?
2. **Headings are those questions.** Each section's first sentence answers its question in one line. The rest of the section earns that answer.
3. **Every term is explained where it first appears**, in plain words, with a sense of scale: MWe against MWt, the kettle for a watt, enrichment as physical spinning not chemistry, criticality as "steady" not "dangerous". Bold the term at its definition. No glossary.
4. **Go one level beneath what the headline says.** For every "X needs Y", say why physically (leakage, density, temperature limits), what the alternative would cost (INL: 5% enrichment makes microreactor power ~15x dearer), and who tried the alternative (Aalo on LEU).
5. **Say what is unknown.** Where no figure is published (core loadings), say so and give the best bounded inference, labelled.
6. **One spine, one claim, stated by paragraph three.** Open on a tension. The claim in claims.ts is falsifiable with dates.
7. House style still holds: no em or en dashes, British spelling, sentences mostly 14 to 22 words, no share prices or views on shares, financials only as evidence, every number primary and dated.

## Figures

- **Illustrations** (`<figure class="illo">`, `illo-title`, `illo-sub`, figcaption): hand-drawn line art in the style of the homepage descent, showing the physical thing: a core cutaway, a zoom from fuel block to particle, the supply chain with its choke points shaded. Classes in global.css (`i-line`, `i-thin`, `i-fill`, `i-metal`, `i-fuel`, `i-cool`, `i-hot`, `i-choke`, `i-t`, `i-n`, `i-k`...). Generate with a Python script per figure (coordinates computed, never by eye), preview at laptop and phone width, light and dark.
- **Charts** (`<figure class="chart">`) prove one sentence each, as in STORY-RULES 14 to 17.
- Three to twelve figures in all (checker). Pilot has three illustrations and three charts.

## Structure on the page

- Frontmatter `format: "depth"`. No `<hr class="layer">` divider: one continuous piece.
- The page lists the question headings under the summary as "In this piece".
- The analogy block stays, before the first heading.
- After "What would prove me wrong": the claims-record fold, "The figures behind the charts" fold (every number with source and method), the exposure map and the sources line.

## Process (the pilot's, reuse it)

1. Tommy's study notes, fact-checked with pushback written into the notes file (study-decks/).
2. Three parallel research agents on the primary sources, one per slice, each writing a file to research-build/topics/<topic>-research/ with every fact sourced and a "what the deck or live piece has wrong" list.
3. Draft in research-build/deep-pieces/<slug>/<slug>.src.md with `<!--FIG:name-->` markers; `assemble.py` injects the figures and the claim text into src/content/journal/<slug>.md.
4. A separate adversarial fact-check agent (FACTCHECK.md) before Tommy reads it.
5. check-piece (depth mode), build, link check, preview at laptop and phone widths, light and dark.
6. Tommy reads it, says he can defend it, and only then publishes it (date set at the real publish time, map entry in stack.ts, LinkedIn post).
