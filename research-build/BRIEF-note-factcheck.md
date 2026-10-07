# Brief: fact-check one published research note (READ ONLY)

You are auditing a research note that is live or drafted on Tommy Lau's site, The Physical Layer. Do NOT edit, create or delete any file in /Users/tommylau/Desktop/journal. Report only.

Materials for your note (slug and Company given in your instructions):
- Text of record: /Users/tommylau/Desktop/journal/src/content/calls/<slug>.md (frontmatter: call box, keyPoints, correction, revisitIf, wrongIf; body: full argument and sources line)
- PDF: /Users/tommylau/Desktop/journal/public/research/<DATE>_<Company>_Initiation.pdf (extract text with pypdfium2)
- Model: /Users/tommylau/Desktop/journal/public/research/<DATE>_<Company>_Model.xlsx (openpyxl; cached values present)
- Figures file: /Users/tommylau/Desktop/journal/research-build/<slug>/data.py (or *_data.py)
- The journal piece it rests on (path in the md `claims`, under src/content/journal/<claim>.md)

Check, in this order:
1. **Company figures against primary sources.** Every reported number (revenue, margins, EPS, guidance, backlog, capex, share counts, cash, debt, deal terms, dates of releases and results) against the company's own releases and filings (SEC EDGAR, investor relations). Load web tools with ToolSearch "select:WebSearch,WebFetch". Prioritise the numbers the thesis and valuation rest on. Spot-check the rest.
2. **Market data.** The reference close and its date, 52-week high/low, and any consensus or peer multiple (check the stated source and date is plausible; Yahoo chart API or stockanalysis.com).
3. **Arithmetic.** Recompute every derived figure: market value, EV, multiples, growth rates, scenario values, weighted value, sensitivity grid, upside percentages, unit economics. Check the md, the PDF and the model agree with each other.
4. **Dates and events.** Next results date, deal dates, quotes and who said them.
5. **The "Where I was wrong" passage.** Is the correction itself accurate, and does it fairly describe what the journal piece said (quote the piece)?
6. **Internal consistency and presentation.** Contradictions between sections, the call box vs the conclusion, keyPoints vs body, labels (own estimate vs company figure), anything a PM would catch. Typos.

Report back (under 500 words), grouped:
- **ERRORS** (wrong as stated): each with location (md line or PDF page), what it says, what is correct, and the source with URL and date. Say whether fixing it would change the call, target, scenario values or revisit levels.
- **ARITHMETIC** slips, same format.
- **UNVERIFIABLE**: claims you could not confirm either way.
- **PRESENTATION** issues worth fixing.
- A one-line verdict: is the note safe to leave live as is?
Be precise and conservative: only call something an error if you have the primary source.
