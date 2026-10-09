# Brief: fact-check one DRAFT journal piece (READ ONLY)

Audit a draft Analysis piece for Tommy Lau's journal, The Physical Layer. Do NOT edit, create or delete any file. Report only.

Materials (slug given in your instructions):
- The piece: /Users/tommylau/Desktop/journal/src/content/journal/<slug>.md (draft: true is expected)
- Its sidecar with proposed claim, claims entry, glossary, numbers, LinkedIn post and the source list: /Users/tommylau/Desktop/journal/research-build/journal-drafts/<slug>.md
- The cover: /Users/tommylau/Desktop/journal/public/covers/<slug>.svg
- The spec: /Users/tommylau/Desktop/journal/WRITING-FORMAT.md and CLAUDE.md
- Other pieces that mention the company (grep src/content/journal), to check consistency.

Check, in order:
1. **Every figure and quote against primary sources**: the company's own filings, results releases, annual reports, investor presentations and call transcripts; agencies and grid operators for structural numbers. Load web tools with ToolSearch "select:WebSearch,WebFetch". Attribute each quote to the right person, date and venue. Prioritise the numbers the claim rests on.
2. **Arithmetic and derived figures** (ratios, years of output, growth rates): recompute.
3. **The claim and falsifier**: is the claim a fair reading of the evidence, testable, and is the falsifier observable? Does the proposed claims.ts entry match the piece's thesis line and "What would prove me wrong" section?
4. **House rules**: subject named in title, summary, cold open and thesis line and carried through; no share price, market value, valuation multiple, target, rating or view on shares anywhere; exposure map says only what companies make, with the exact disclaimer sentence pair; analogy block uses household objects, no finance; no em or en dashes; British spelling; jargon defined on first use; the short skeleton of WRITING-FORMAT §3 (cold open ending on the thesis, two-paragraph analogy, three ## sections: how it works, the evidence, what would prove me wrong; exposure map of three or four groups; one or two sentence sources line), body 450 to 600 words and never over 700, and the §4b numbers budget (15 figures at most, 3 company financial figures at most); no mention of Claude, a paper portfolio, a radar, a watch list or an "earlier read".
5. **Consistency with other pieces** on the site (no contradictions with what earlier pieces say about the company or the mechanism, unless the piece says so openly).
6. **Cover**: follows WRITING-FORMAT §7 (800x600, plain background rect after defs, one bold idea, caption names the company); no text that would be unreadable at thumbnail size.

Report back (under 450 words), grouped:
- **ERRORS** (wrong as stated): location, what it says, what is correct, primary source URL and date.
- **ARITHMETIC** slips.
- **UNVERIFIABLE**: claims you could not confirm.
- **RULES / PRESENTATION** issues.
- One-line verdict: ready for Tommy's approval as is, or after which fixes.
Be precise and conservative: only call something an error with the primary source in hand.
