# The Physical Layer

Tommy's public journal on AI and energy infrastructure. Astro static site,
GitHub Pages, live at https://thephysicallayer.fyi

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

- **Scope is AI and energy infrastructure only.** No commodities, shipping,
  general equities or macro. The narrowness is the asset.
- **Never a price, target, rating, market share, backlog, financial or
  recommendation** anywhere on the site.
- **Never post to LinkedIn from Tommy's personal profile.** The company page
  only. Verify the composer identity reads "The Physical Layer" before submitting.
- **Do not add a new piece to `READING_PATH`.** The reading page is a capped
  on-ramp, not an index. See the README section on it.
- House style: no em dashes, British spelling, 14 to 20 word sentences,
  1,050 to 1,500 words.

## Before every publish

```bash
python3 brand/check-piece.py src/content/journal/<slug>.md
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py
npm run build
```

The checker must exit clean. Bump `OG_VERSION` in `src/config.ts` only when the
artwork of an existing card changes, because LinkedIn caches card images by URL.
