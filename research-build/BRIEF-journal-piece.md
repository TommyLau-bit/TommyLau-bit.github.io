# Brief: draft ONE company journal piece for The Physical Layer (Tommy Lau)

You are drafting one Analysis piece about one company for Tommy's journal. It stays a DRAFT: Tommy approves the claim before anything is published. Do not commit, push or publish.

## Read first, all of it
- /Users/tommylau/Desktop/journal/CLAUDE.md
- /Users/tommylau/Desktop/journal/WRITING-FORMAT.md (the complete spec: shapes, frontmatter, body skeleton in order, house style, §4a financial evidence, scope, cover, LinkedIn post, checker). Follow it exactly.
- Three recent company Analysis pieces as models: src/content/journal/every-megawatt-got-harder.md (Vertiv), src/content/journal/the-product-is-time.md (Bloom Energy), src/content/journal/corning-lays-the-glass.md (Corning). Match their structure, length, voice and density.
- Pieces that already mention your company, so the new piece builds on them and does not contradict them (grep src/content/journal for the company name).
- src/data/stack.ts (map layers), src/data/claims.ts (claim format), src/data/numbers.ts, src/pages/glossary.astro.
- Cover examples in public/covers/ (e.g. every-megawatt-got-harder.svg, the-product-is-time.svg).

## The piece
- Shape: Analysis. The company is the subject: named in the title, summary, cold open and thesis line, and every section comes back to it (WRITING-FORMAT §0).
- You must propose the claim, because Tommy has not supplied notes. Research the company first, then choose ONE claim about the physical mechanism that makes the company matter in the AI and energy buildout, which its own disclosures can test, and which could be proved wrong. It must fit the site's existing argument (the grid connection queue, equipment lead times, power arriving before chips) without merely repeating another piece.
- Required content (CLAUDE.md "What his notes must contain"): the claim in one sentence, the mechanism, one or two structural numbers, and who operates in the layer.
- Financials only as evidence for the mechanism, dated and sourced to the company's own filings (§4a). NEVER a share price, market value, valuation multiple, target, rating, or any view on the shares. The exposure map says what companies make, nothing else.
- Real, dated, sourced data only, from the company's own reports, filings and investor materials (annual reports, quarterly results, capital markets days), plus grid operators and agencies for structural numbers. If you cannot verify something, leave it out. Load web tools with ToolSearch "select:WebSearch,WebFetch".
- House style: no em dashes or en dashes anywhere, British spelling, 14 to 20 word sentences, 1,050 to 1,500 words, first person only for judgement, jargon defined where it first appears, the analogy block with household objects (no finance comparisons), a "## What would prove me wrong" section.
- NEVER mention Claude, a paper portfolio, a radar, a watch list or any "earlier read". The piece is Tommy's.
- Frontmatter: `draft: true`, `date` set to the current Singapore time (it will be reset at publish), category "Analysis", cover path, two to four tags reusing existing ones where they fit.

## Outputs
1. src/content/journal/<slug>.md (choose a short, lowercase, hyphenated slug with no dates, in the style of the existing ones).
2. public/covers/<slug>.svg following §7 (800x600, dark gradient background as a plain rect right after <defs>, amber for energy, blue for compute, one bold diagram, caption naming the company).
3. research-build/journal-drafts/<slug>.md, a sidecar for Tommy and the publish step, containing:
   - The proposed claim in one sentence, and two alternative claims you considered, one line each, with why you chose this one.
   - The proposed src/data/claims.ts entry (id, claim, breaksIf, watch) as TypeScript.
   - Which src/data/stack.ts layer the slug goes in (or a proposed new layer, with `what` and `constraint` sentences, placed physically).
   - Any glossary terms to add (term, one-line definition, which heading), and any structural figure for src/data/numbers.ts (physical figures only).
   - The LinkedIn post per §9.
   - Every source used, with URL and date, one per line, so a fact-checker can verify each figure.
Do NOT edit stack.ts, claims.ts, numbers.ts, glossary.astro or linkedin-posts.md yet; those go in at publish.

## Checks before finishing
- `python3 brand/check-piece.py src/content/journal/<slug>.md` passes (fix every failure; warnings explained).
- `npm run build` still succeeds (drafts are excluded from production).
- Touch only your own files.

## Report back (under 300 words)
Slug, title, the proposed claim and the two alternatives, the mechanism in two lines, the structural numbers used, the falsifier, the map layer, word count and checker result, anything you could not verify.
