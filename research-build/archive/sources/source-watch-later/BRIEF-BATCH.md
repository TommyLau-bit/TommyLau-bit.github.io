# Batch brief: one journal piece from the Watch Later batch (29 Oct 2026)

Tommy approved nine topics found in his YouTube Watch Later transcripts. You draft ONE of them. It stays a draft: do not commit, push or publish.

## Follow the house brief
Follow `/Users/tommylau/Desktop/journal/research-build/BRIEF-journal-piece.md` exactly, and read everything it says to read (CLAUDE.md, WRITING-FORMAT.md, the model piece ge-vernova-sells-the-wait.md, stack.ts, claims.ts, numbers.ts, the glossary, cover examples). Differences from that brief:
- The topic and claim are agreed in outline in your instructions. Research first, then refine the wording so it is falsifiable, dated and true to what the primary sources show. If the evidence does not support the claim, reframe honestly or report that it fails; never force it.
- The subject may be a company, project, grid, regulator or physical system. It is named in the title, summary, cold open, thesis line and every section (WRITING-FORMAT §0).
- Oil is in scope as a physical system since 29 Oct 2026 (WRITING-FORMAT §5), with no price forecasts or trading views.

## Source discipline (critical)
- The lead came from a third-party YouTube video. Its transcript is in `research-build/source-watch-later/<folder>/TRANSCRIPT.md` (named in your instructions). It is someone else's work, often a paid membership channel: a lead sheet only. Do not reproduce its structure, wording, order or analogies. Write your own household-object analogy. Credit the video once, inside the one or two sentence sources line.
- Verify EVERY figure against its primary source (company filings and releases, regulators, grid operators, agencies, court or docket documents). Load web tools with ToolSearch "select:WebSearch,WebFetch". If a site blocks you (403, Cloudflare, bot check), do not try to get round it; use another primary copy (SEC EDGAR, a regulator's mirror) or drop the figure. Never state an unverified figure. Label anything confirmed only from press as such in the sidecar.
- Never send Tommy's email or any personal data in a request header, URL or payload. For SEC EDGAR use a generic User-Agent such as "ThePhysicalLayer research".
- Build on existing pieces, never repeat or contradict them. `research-build/source-watch-later/EXISTING-COVERAGE.md` lists every piece and claim; also treat as covered the three scheduled drafts `ercot-rations-the-plug`, `abilene-switched-on-in-stages`, `hyperion-the-plant-outlasts-the-lease`. Grep `src/content/journal/` for your subject and read the nearest pieces in full. Link to one or two where natural.
- No share prices, valuations, targets or views on shares. Never an em dash or en dash anywhere (piece, sidecar, cover). British spelling. Do not name Fluence anywhere (Tommy took its piece down).

## Outputs (as the house brief)
`src/content/journal/<slug>.md` (draft: true), `public/covers/<slug>.svg`, `research-build/journal-drafts/<slug>.md` (claim and two alternatives, claims.ts entry, stack.ts layer or a proposed new layer, glossary, numbers, LinkedIn post per §9, every source URL with date, and a section listing video figures dropped or flagged). Do NOT edit stack.ts, claims.ts, numbers.ts, glossary.astro or linkedin-posts.md. Touch only your own three files. Eight other agents are drafting other pieces in the same folders at the same time; if `npm run build` fails because of another agent's file or a concurrent build, wait a minute and retry, and say so if it persists. `python3 brand/check-piece.py src/content/journal/<slug>.md` must pass with 0 failures and 0 warnings.

## Report back (under 300 words)
Slug, title, final claim and falsifier, the figures used with primary source (and which are press-only), every video figure you dropped or flagged, map layer, word count, checker and build result.
