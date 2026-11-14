# the-equipment-queue: changes, 14 Nov 2026

Source for every new figure: Siemens Energy, Earnings Release Q4 FY 2026 (July 1 to September 30, 2026), 11 November 2026.
- Release page: https://siemens-energy.com/global/en/home/press-releases/earnings-release-q4-fy-2026--siemens-energy-reports-a-record-yea.html
- PDF: https://assets.siemens-energy.com/dam/23e549e5-fb37-4db4-99d3-b4ff00539ccb/ER_Q4_26_EN_final-pdf_Original%20file.pdf

## New figures (Grid Technologies)
- Order backlog €52bn at 30 Sept 2026 (was €51bn at 30 June); "Book-to-bill ratio was 1.30 and order backlog increased to €52bn."
- Q4 FY2026: orders €5,651m, revenue €4,362m (record), book-to-bill 1.30.
- FY2026: orders €23,979m, revenue €14,106m (comparable growth 26.2%), book-to-bill 1.70 (my arithmetic).
- FY2027 guidance: comparable revenue growth 22 to 24%.
- Years of work: 52 / 14.106 = 3.69 (3.65 to 3.72 on rounding), down from about 3.96 at 30 June 2026, still above 3.56 at 30 Sept 2024. My arithmetic.
- Drift: holding 3.69 at 23% growth needs book-to-bill about 1.7; at 1.30 the ratio reaches about 3.1 by 30 June 2028 (quarterly run, my arithmetic). At 1.70 it holds about 3.7.

## Edits (copy only; live file untouched)
- Thesis para: "about four years ... up from three and a half" -> "about 3.7 years ... still more than the 3.56 of September 2024".
- Years-of-work chart: new Siemens point Sept 2026 at 3.69 (244.5, 67.0); label "about 3.7"; aria-label updated; title "getting longer" -> "has held at years"; caption drops "Siemens Energy's latest is 30 June 2026".
- Evidence para, "number the claim rests on", "trap" para, peak case, test 1 and test 2 text, years-of-work table row, trailing-revenue note, drift arithmetic note, peak note, "Where later evidence" line for the Siemens claim (now "Holding"), sources line date.
- Unchanged: claims.ts, claims-record quotes (3.96 and €51bn stay there as recorded), anchors, date.
- Visible words 3,548 -> 3,597. Checker: 0 failures, 2 existing warnings (exposure map, sources line length).

## Knock-on
- Chapter 2 (america-rations-the-plug, line 50) says Siemens Energy and Hitachi Energy hold "about four and three years". Siemens is now about 3.7; suggest "nearly four and about three" or "about 3.7 and 3.1".
- Claim the-equipment-queue: test is 3.6 at 30 June 2028; ratio now 3.69, close to the line.

## Not landed / nothing found (10 to 14 Nov 2026)
- Hitachi Energy: no new primary release found bearing on the mechanism (latest: Gallman 15 Sept, London Ontario insulation factory Oct 2026; Hitachi results already carried, 28 Oct).
- DOE, Commerce: no new transformer or GOES action found (web search only; Federal Register not combed line by line).
- Siemens Energy annual report and analyst presentation not read; no grid capacity statement in the release.

## LinkedIn draft (substantial: the claim's test number moved)
Siemens Energy's grid business now holds about 3.7 years of signed work, down from about four in June. The pile did not shrink: its backlog rose to €52bn at 30 September. Record sales of €4.4bn in the quarter simply ate into it faster. That is the trap in measuring a queue in years. With grid revenue guided up 22 to 24 per cent next year, orders must run about 1.7 times sales just to hold the ratio. The full year managed 1.70; the fourth quarter 1.30. The new transformer halls arrive from 2027. Whether they shorten the wait depends on that one ratio. The equipment queue, with the fiscal 2026 figures, on The Physical Layer.

## Fact-check (14 Nov)

Source re-opened: Siemens Energy Earnings Release Q4 FY 2026, PDF downloaded fresh and text re-extracted (dated Munich, 11 November 2026).
- Grid Technologies backlog €52bn at 30 Sept 2026 ("Book-to-bill ratio was 1.30 and order backlog increased to €52bn"): PASS.
- Q4 orders €5,651m, revenue €4,362m, "new quarterly high": PASS. 5,651/4,362 = 1.2955, 1.30: PASS.
- FY2026 orders €23,979m, revenue €14,106m, comparable growth 26.2%; FY2027 guide 22% to 24%: PASS. 23,979/14,106 = 1.70: PASS.
- Years of work 52/14.106 = 3.686; 51.5 to 52.5 gives 3.65 to 3.72; June 51/12.889 = 3.96: PASS.
- Hold condition 1 + 3.69 x 0.23/1.23 = 1.69, "about 1.7": PASS. Smooth quarterly run, trailing revenue growing 22/23/24%: at 1.30, 3.09/3.05/3.02 at 30 June 2028 ("about 3.1" PASS at the midpoint); at 1.70, 3.70 (holds): PASS.
- Threshold: every reference says 3.6 at 30 June 2028, matching claims.ts (claim and breaksIf). No "below 3" or other threshold anywhere in the draft: PASS.
- Chart: y = 280 minus 57.75 per year; 3.69 maps to 66.9 (drawn 67.0); x 244.5 = 30 Sept 2026, same as Hitachi and Eaton latest: PASS. Title "has held at years" FIXED to "still runs to years" (Siemens fell; "held" spun it).
- Thesis paragraph: did not say the ratio fell. FIXED: "down from about four in June but above the 3.56 of September 2024".
- "The backlog rose by €1bn": both figures rounded. FIXED to "about €1bn".
- Peak case skipped the 1.48 quarter. FIXED: "from 1.48 in June's quarter and 2.28 in March's".
- Test 1 trimmed (growth guide already in the trap paragraph) to bring visible words to 3,592.
- Claims.ts and claims-record quotes (3.96, €51bn) untouched: PASS. "Holding" on the Siemens shortage claim matches its breaksIf (orders above revenue for the year; backlog rose): PASS.
- Sources line date 11 November 2026: PASS. No dashes, British spelling: PASS.
- Checker: 0 failures, 2 existing warnings. Not checked: the knock-on in america-rations-the-plug (not in this draft).
