# Brief: draft a research initiation for The Physical Layer (Tommy Lau)

You are drafting ONE initiation note for Tommy's site. Tommy decides the call; you draft everything and give a draft view. Nothing is published, committed or pushed by you.

## Read first (all of it)
- /Users/tommylau/Desktop/journal/CALLS-SPEC.md (process, rules, the redesign section)
- /Users/tommylau/Desktop/journal/CLAUDE.md (house style: British spelling, NEVER an em dash or en dash anywhere, short sentences)
- The journal piece your note rests on (path below) and its entry in src/data/claims.ts.
- Worked example, copy its structure exactly:
  - Text of record: src/content/calls/vertiv.md (frontmatter fields: title, summary, company, ticker, exchange, claims, correction (only if needed), keyPoints, files, draft, call, draftView, charts; body sections in this exact order: "## The thesis", "## What the market prices in, and where I differ", "## Valuation, with the working", `<div class="charts-slot"></div>`, "## Risks, and what would change my view", "## Conclusion", then `<p class="sources">Sources: ... Personal research, not investment advice.</p>`). Also src/content/calls/nebius.md for a NO CALL example (call.revisitIf).
  - PDF + model build: research-build/vertiv/ (data.py single source of figures, build_charts.py, build_model.py, check_model.py, build_note.py, common.py, render.py) and research-build/nebius/. Template docs: ~/Desktop/jobs/research coverage/_note_template/README.md.
  - Look at public/research/2026-10-06_Vertiv_Initiation.pdf (5 pages) for the target depth and look.

## Research rules
- Real, dated, sourced data only. Company figures from the company's own releases and filings (SEC EDGAR, investor relations; for TSMC its monthly revenue reports and quarterly management reports). Prices from the Yahoo Finance chart API (curl with a browser User-Agent: https://query1.finance.yahoo.com/v8/finance/chart/<TICKER>?range=3y&interval=1mo and range=5d&interval=1d); use the latest available close and state its date. Consensus and peer multiples from Yahoo quoteSummary / stockanalysis.com / MarketBeat, labelled with source and date. If something cannot be verified, say "not verified" or leave it out. Never invent.
- Load web tools with ToolSearch "select:WebSearch,WebFetch".
- Your own estimates are always labelled as yours.

## The analysis
- Thesis in the journal's analogy style, at buy-side depth, built on the piece's claim.
- **Claims and notes must agree.** Check the claim and the piece's evidence against what you find. If the piece got something wrong, the note says so openly in a "**Where I was wrong in September**" (or "...in October") passage: what was wrong, and what changed the view. Add a one-sentence `correction` in frontmatter. NEVER edit the journal piece or claims.ts. If nothing was wrong, omit both.
- Variant perception: what the price implies vs your view, with numbers.
- Valuation with the working: the method that fits the business, a key financials table (history, guidance, your estimates), bear/base/bull with probabilities (25/50/25 unless you justify otherwise), a 3x3 sensitivity grid, peers.
- Risks, catalysts with dates (verify the next results date; if unconfirmed say so), what would change the view.
- Draft view: LONG, SHORT or NO CALL, a 12-month target (none for NO CALL, then give `revisitIf`), conviction High/Medium/Low, and one-paragraph reasoning. Be honest: a calibrated NO CALL beats a forced LONG. The scorecard is public.
- `call` block: direction null, target null, conviction null (Tommy decides), price and priceDate filled, horizon "12 months, to October 2027", wrongIf filled. `draft: true`. No `date` field.
- keyPoints: 3 to 5 plain sentences (the web summary page shows only these plus the call box).
- Body 1,500 to 3,200 words.

## Outputs (use YOUR slug and company name; date stamp = the day you draft it (YYYY-MM-DD), kept as a single DATE constant in data.py so it can be changed at publish)
- src/content/calls/<slug>.md
- public/research/<DATE>_<Company>_Initiation.pdf (4 to 6 pages, house style; banner shows Claude's draft view with the word DRAFT, e.g. "DRAFT: LONG" or "DRAFT: NO CALL", driven by one CALL dict in data.py so the final rebuild is a one-line change)
- public/research/<DATE>_<Company>_Model.xlsx (live formulas, blue inputs, tabs like the Vertiv model; verify every output against the note with a check script, LibreOffice headless recalc is available)
- public/research/<DATE>_<Company>_Initiation-p1.png (page one, pypdfium2 at 2x)
- research-build/<slug>/ build scripts (copy common.py and render.py in)
- files block in the md pointing at those paths; pages set.
- Run WeasyPrint with DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib.
- Note sign-off "Tommy Lau | The Physical Layer | thephysicallayer.fyi"; About this note links the journal piece and https://thephysicallayer.fyi/research/, and states "I hold no position in <Company>." plus "Personal research, not investment advice."

## Checks before you finish
- `python3 brand/check-call.py src/content/calls/<slug>.md` passes (warnings about thumb are fine only if the PNG is missing).
- Extract PDF text: zero em dashes, en dashes, Unicode minus signs.
- Model check script passes.
- `npm run build` still succeeds (draft notes are excluded from production, that is expected).
- Touch only your own files. Other agents are building other companies in the same folders at the same time.

## Report back (under 400 words)
Company, price and date, draft view (direction, target, conviction) with the 3-line reasoning, bear/base/bull values, the main variant point, any "where I was wrong" finding, next results date, page count, and anything you could not verify.

## Lessons from the batch 1 fact-check (follow these too)
- **Never mention Claude, a paper portfolio, a radar or any "earlier read" in the note, the md or the model.** If a research input raised a question, ask the question in your own words ("The obvious objection is...", "The piece left one question unanswered...").
- **"Where I was wrong" must be exactly right.** Quote the piece's actual sentence, read it in context (e.g. "the same quarter" means the quarter named just before), and prove the mechanism from primary line items (income statement lines, segment tables), not summaries. Say "what showed me the slip" rather than "what changed my view" if the view did not change. Do not claim the piece "left out" something without checking it is not there.
- Cite the exact filing for each fact (8-K vs 10-Q vs 10-Q/A vs shareholder letter vs call). If a 10-Q/A exists, use it.
- Every arithmetic statement about the sensitivity grid must match the grid (e.g. "either X or Y" vs "both").
- Dates of highs/lows: check intraday high date vs highest close date separately.
- First person singular throughout the PDF ("What would change my mind", not "our"). "We initiate" is not used; write "My call".
- Recalculate the model so values are cached: after building, run `soffice --headless --calc --convert-to xlsx --outdir <tmp> <model.xlsx>` and copy the result back over the original; confirm with openpyxl data_only that no formula cell is None.
- Label every own estimate as such, and say which consensus source each year comes from if they differ.

## Draft view rule (added 7 Oct 2026)
Apply the band to the BASE value consistently: LONG if the base value is 15% or more above the price, SHORT if 25% or more below, NO CALL in between. If you depart from it, say so explicitly with the reason. For a directional call set draftView.target and write wrongIf as a thesis test for that direction (not just the bear or bull values); revisitIf only for NO CALL; revisit levels and wrongIf thresholds must not coincide or contradict.
