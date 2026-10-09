<!-- Copy to src/content/journal/<slug>.md and fill in.
     This file lives at the repo root on purpose, so the site never loads it.
     The rules behind every slot are in WRITING-FORMAT.md.
     date is the real moment you publish, Singapore time. Never a future date.
     FIRST RULE (WRITING-FORMAT §3 and §4b): about a five minute read for a person
     reading to understand. 450 to 600 words in the body, never over 700. 15 figures
     at most, 3 company financial figures at most. Explanation here, numbers in the
     research notes. Model piece: ge-vernova-sells-the-wait.md.
-->
---
title: "A claim or a plain question, sentence case, 8 to 16 words"
date: 2026-00-00T00:00:00+08:00
summary: "Two or three sentences, plain English, no jargon. This is the hardest-working line on the site: it renders in the In plain English box, on the home card, on the reading page, as the meta description and as the LinkedIn card subtitle. Write it last."
category: "Explainer"
cover: "/covers/<slug>.svg"
tags: ["", ""]
---

<!-- COLD OPEN: three or four short paragraphs, about 80 words.
     Open on a question the reader has never asked, a claim you offer up for
     attack, a correction of a common assumption, or a fact with a payoff.
     No throat-clearing. -->

<!-- Close the open on the thesis, alone on its own line, short and flat. -->

<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>The everyday comparison, household objects, and why the obvious fix fails. No finance.</p>
<p>The one image that carries the whole argument.</p>
</details>

## <!-- How it works, about 200 words. The mechanism, jargon defined in place,
        and in two or three sentences why supply cannot simply catch up. -->

## <!-- The evidence, about 100 words. The company's own disclosure, one figure,
        tied to the mechanism in the next sentence. -->

## What would prove me wrong

<!-- About 60 words. MANDATORY for Analysis pieces. For an Explainer, replace this
     section with the constraint: what binds and why.
     Name the observable that would kill the claim, not a hedge. -->

<section class="exposure">
<h3>Who is exposed if <!-- the claim --> is right</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt><!-- Category --></dt>
<dd>What they make: <span class="names">Company, Company</span>.</dd>
<dt><!-- Category --></dt>
<dd>What they make: <span class="names">Company</span>.</dd>
<!-- Three or four groups, one short line each, about 100 words for the whole map. -->
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd><!-- Who loses if this is right. Mandatory. --></dd>
</dl>
</section>

---

<p class="sources"><!-- One or two sentences: the documents and dates, or that the piece explains mechanism. --> Personal research, not investment advice.</p>

<!-- BEFORE PUBLISHING: the site around the piece (WRITING-FORMAT.md §6a).
     1. Map: add the slug to one layer's `pieces` in src/data/stack.ts. Every piece.
        If no layer fits, add a new layer in its physical place in the chain.
     2. Claims: Analysis pieces only. Add { id, claim, breaksIf, watch } to
        src/data/claims.ts. One-sentence claim, the falsifier, the evidence watched.
        Never reworded later. No statuses, no reviews.
     3. Numbers: optional. A new structural figure goes in src/data/numbers.ts.
     4. Company pages build themselves from the exposure map. No topic pages.
     The top menu stays at five items: Journal, Map, Research, Glossary, About.
     No email sign-ups anywhere on the site.
     brand/check-piece.py fails the piece if step 1, or step 2 for Analysis, is missing. -->
