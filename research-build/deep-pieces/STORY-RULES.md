# Story rules for every deep piece (Tommy, 31 Oct 2026)

Tommy's brief: a piece is a story, not files stacked on top of each other. It grabs the reader, builds, reaches a climax, and ends by tying everything together, so the reader finishes thinking "that was beautiful". Within a minute or two the reader knows what the piece is about. The material is already there; the job is the telling.

The model is `src/content/journal/the-equipment-queue.md` (rewritten 31 Oct). The before version is `research-build/deep-pieces/pilot/the-equipment-queue.BEFORE.md`. The study behind these rules, eight well-told articles taken apart, is `research-build/deep-pieces/STORY-STUDY.md`.

These rules replace the old §D section skeleton ("How it works", "The number that matters", "The mechanism in depth", one section per company). Everything else in CLAUDE.md still holds: primary sources, no share views, no em dashes, British spelling, never name Fluence.

## The spine

1. **One spine, one claim.** Before writing, state the spine in one sentence. Every paragraph serves it. The piece's own claim (the claims.ts entry whose id is the slug, or the strongest one) is the only claim argued in the story.
2. **Open on a tension, never a definition.** Paragraph one is a paradox, a scene or a surprising fact a reader wants explained ("Hitachi Energy is building 40 factories and still expects three years of orders waiting").
3. **The claim, in plain words, by paragraph three.**
4. **Mechanism before evidence.** The reader learns why it happens before seeing company figures that show it has happened.
5. **Build to a climax.** The strongest piece of evidence (often a maker, regulator or operator measuring the whole system in its own words) sits about two thirds of the way in, with a chart.
6. **One counter-evidence answer.** The case against sits in "What would prove me wrong", under what would not move me, stated fairly and answered or conceded. No hedges scattered everywhere else.
7. **The plain-English top answers the opening; the investor layer proves it.** The analogy stays in the top; the investor layer does not repeat it or end on a recap (6 Nov 2026).

## The beats

8. **Headings are steps in the argument**, written as statements ("The makers will not overbuild"), never a company name or a topic label. The checker fails "How it works", "The number that matters" and "The mechanism in depth".
9. **No company gets its own section.** A company appears inside a beat as evidence, in about three sentences at most. A paragraph that could be pasted unchanged into another piece is a company note, not evidence: cut it or link the research note.
10. **One running measure** where the piece has one (years of work, months to connect, megawatts per rack), used in every beat that carries a number.
11. **Each section's first sentence states its point.** Skimming first sentences alone gives the whole argument.
12. **At most three numbers a paragraph, each translated** into what it means for the spine.
13. **Six to nine beats.** Plain-English top about 400 to 600 words; investor storyline about 900 to 2,000 words (charts, folded evidence and earlier claims do not count). Depth-format pieces: about 3,000 to 3,500 visible words in all (Tommy, 9 Nov 2026; DEPTH-FORMAT.md).

## Charts

14. **Two to four charts per piece, at the turns of the argument**: the trend that sets up the problem, the gap or mechanism that explains it, the climax. The checker fails fewer than two or more than five.
15. **Every chart proves one sentence.** Its title IS that sentence ("Every queue is longer than it was a year ago"), and the paragraph above leads into it. The subtitle says what is measured; the caption gives source, date and any caveat.
16. **Pick the form that shows the idea**: lines for a trend, bars for a gap or comparison, a dot timeline for announcement to delivery, a scatter for a relationship, a simple labelled diagram for a physical flow (grid to rack, chip to memory). A table with a time column should be a chart.
17. **Every number in a chart is a sourced figure in the piece or its sidecar.** Never a value invented or estimated to make the line look right; anything read off someone else's chart is labelled as such.

Chart mechanics (no colours inline, so dark mode works):

```html
<figure class="chart">
<p class="chart-title">The sentence this chart proves</p>
<p class="chart-sub">What is measured, and in what unit</p>
<svg viewBox="0 0 560 H" role="img" aria-label="Full description with every number shown">
  ... only these classes: c-grid (gridlines group), c-axis (axis text group), c-line + c-s1|c-s2|c-s3 (series:
  ink, amber, blue), c-dot + c-s1..3, c-lab + c-s1t|c-s2t|c-s3t (direct labels), c-zone + c-zone-t (shaded
  band), c-bar (amber bar), c-bar c-alt (blue), c-bar c-mute (grey), c-base (axis line), c-today + c-today-t,
  c-span / c-start / c-end / c-endt (dot timelines), c-plant (small ticks and notes), c-note (grey text),
  c-box + c-box-t (diagram boxes), c-arrow + c-arrow-head (diagram connectors; draw heads as small polygons) ...
</svg>
<figcaption>Source and date. Caveat in one line.</figcaption>
</figure>
```

Width 560; height to fit. Text 12 to 14px. Label lines directly rather than with a legend. Compute coordinates with a short script, never by eye. Phones scroll a chart sideways inside its frame, so keep labels inside the viewBox.

## The investor layer: message, proof, what would and would not change my view (Tommy, 6 Nov 2026)

Tommy reread three pieces after sending them to a CLSA analyst: the core idea is fully made above the divider, and the investor layer repeated it at greater length. Investors read thousands of analyses a day, so the investor layer is direct, strong and aggressive. This replaces the 31 Oct "jolt" endings (forward "out of the box" headings), which Tommy retired as a silly idea. The model is `src/content/journal/nuclear-for-ai.md` as of 6 Nov 2026.

18a. **The shape.** (1) The first investor heading states the whole message as a claim; its first paragraph gives the core numbers; the anchor chart follows. (2) Three to five proof beats, each opening with its point, every sentence carrying a fact, with the climax chart. (3) "What would prove me wrong" closes it in three parts: the claim's tests; the events that would move me before them; and what would not move me (the old counter-evidence beat, answered tightly). No recap, no analogy callback, no forward closing headings. Aim for about half the old argument length.
   - **Context and connectivity** (Tommy, 6 Nov 2026). On first mention in the investor layer, every company, plant, project, regulator, grid operator and acronym gets a short clause saying what it is ("Centrus, the only American company that has made HALEU"), even if the top introduced it. Each paragraph's first sentence ties back to the argument or the paragraph before. Keep links to sibling pieces where the idea touches them.
   - Whether something is "in the share price", entry points and share prices stay out (CLAUDE.md hard rule); say that work sits in the research notes and link them.
18c. **No stock moves.** Pieces are read one after another, so a phrase that works once becomes a tic across twelve. Banned: "That turns the usual picture round" and its variants, "Here is the part/number...", "Now set/follow...", "The second surprise", "Three dates will show..." as a closer, and any meta line about framing or novelty ("is my framing", "no secret", "widely reported", "the less obvious part"). "My framing" lives in the chart caption only. Before publishing, grep all pieces for repeated openers and closers.

18b. **Every claim stays word for word, folded at the foot.** The piece's own claim and every earlier claim go in one `<details class="claims-record">` ("The claims on record, word for word") after Research notes, quoted exactly as before with their "Breaks if" and later-evidence notes. The headline claim's `<a id>` sits at the first investor heading. claims.ts is never reworded. The old "## Claims on record" section and `claims-earlier` fold are retired.
19. **Every `<a id="...">` anchor in the old piece survives**, placed at the beat where that company or idea now appears. Old URLs redirect to them.
20. **Evidence tables move to the end**, inside `<details class="evidence">` ("The figures behind the charts"), with the arithmetic method and any corrections to earlier pieces. Filing dates, method notes and corrections stay out of the story.
21. "What would prove me wrong", "Research notes", the exposure map and the sources line stay, short and plain, after the story.
