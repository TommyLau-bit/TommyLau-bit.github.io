# Fact-check: the-equipment-queue-depth.md (7 November 2026)

Adversarial check of the draft against primary sources. The checker passes (0 failures, 2 warnings on length). No em or en dashes, no share prices or valuations, no mention of Claude. All five claims in the claims fold match `claims.ts` word for word, with matching dates.

## Findings, most serious first

**1. The drift arithmetic understates the risk to the claim (reasoning).**
Text: "If orders run 10 per cent above output, and output grows 6 per cent a year, the ratio drifts from about four to about 3.8, then about 3.7".
The arithmetic is right (3.84, then 3.72), but 6 per cent output growth is far below Siemens Energy's own figures. Grid Technologies revenue rose 28.6% comparable in Q3 FY2026 (3,624 against 2,819), and the guidance for FY2026 is 25 to 27% comparable growth (Q2 shareholder letter, 22 May 2026). Ratio after one year = R/(1+g) + (b-1). At g = 25% and the Q3 book-to-bill of 1.48: 3.96 becomes about 3.65 after one year and about 3.40 after two, **below the 3.6 test by June 2028**. To hold 3.96 at 25% growth, book-to-bill has to be about 1.8. The nine-month figure (1.88) clears that bar; Q3's 1.48 does not.
Source: Siemens Energy Earnings Release Q3 FY2026, 5 August 2026 (segment tables; https://assets.siemens-energy.com, also mirrored at https://egyptoil-gas.com/wp-content/uploads/2026/08/earnings-release-q3-fy2026-en-pdf_Original20file.pdf); Q2 shareholder letter (https://assets.siemens-energy.com/dam/352bf02e-bbc1-4061-b00d-b45200cd6b3b/2026-05-22-Shareholder-Letter-Q2-FY2026_EN-pdf_Original%20file.pdf).
Fix: keep the illustration but add, in "The trap" paragraph and in "What would prove me wrong": "Siemens Energy's grid revenue is growing about 25 per cent a year on its own guidance. At that pace the ratio holds only if orders run about 1.8 times sales; at the third quarter's 1.48 it would fall to about 3.4 by mid-2028, below the test." Update the evidence fold's drift note to match.

**2. Tariffs: since 8 June 2026, imported cores can pay the same 15% as the finished unit (Proclamation 11032).**
Text: "Until the end of 2027 a finished large transformer is taxed less than the core it is built around, and a third as much as its steel. That favours importing whole units over building them from imported steel in a new American hall." Tariff chart caption: "Cores and laminations: 25%".
Proclamation 11032 (1 June 2026, 91 FR 34085, effective 8 June) added a note to Annex I-B: "any part classifiable in Chapters 84, 85, or 87 ... listed in this Annex ... shall be subject to the tariff rate outlined in clause (5) of Proclamation 11021 when imported exclusively for use in the manufacturing of ... fixed industrial equipment listed in Annex III". HS 8504.23.00 is on Annex III. Cores and laminations (8504.90.9634, 9638, 9642, Chapter 85) are on Annex I-B. So a US maker importing cores for a large transformer can pay the clause (5) rate, which is 15% including the Column 1 duty. The April annex did not have this note. GOES strip (7225 and 7226, Chapter 72) stays at 50%.
Confirmed: 8504.23 is on Annex III; clause (5) says Column 1 duty plus the 232 duty "shall be 15 percent" until 31 December 2027 and Annex I-B rates apply from 1 January 2028 (so the 2028 rate is 25% **on top of** the Column 1 duty); 8504.21 and 8504.22 and the cores are 25% (Annex I-B); 7225, 7226, 7408 and 7413 are 50% (Annex I-A). Proclamation 11021 itself: https://www.govinfo.gov/content/pkg/FR-2026-04-09/html/2026-06960.htm.
Source: Annex I-B and Annex III (June 2026), https://www.whitehouse.gov/wp-content/uploads/2026/06/Annex-I-B.pdf and .../Annex-III.pdf; Proclamation 11032, FR Doc 2026-11314 (4 June 2026).
Fix: "Until the end of 2027 a finished large transformer pays 15 per cent, a third as much as the GOES strip it is built from. Since June, cores imported to build these transformers in America can also pay 15 per cent, but the strip itself pays 50. That favours importing whole units, or ready-made cores, over making cores from imported steel in a new American hall." Chart caption: add "cores imported for making large transformers can pay 15% since 8 June 2026."

**3. The EU Council quote is conditional, and it comes from a lobbying note.**
Text: "In June 2026 Italy, Bulgaria and the Czech Republic warned the EU's Council that for some classes there was 'only one manufacturer of dry-air solutions', with capacity 'lower than the European demand'."
The note (ST 10693/1/26 REV 1, 24 June 2026, an AOB item from those three states) says: "If fluoronitrile-based solutions disappear from the EU market, only one manufacturer of dry-air solutions remains". It is a warning about a future case, made in support of fluoronitrile gear (made by GE Vernova and Hitachi Energy). "For some classes" does not appear. The note also cites a four-year derogation under Article 11(5). The single dry-air maker it means is Siemens Energy (Blue), which is in this piece.
Source: https://data.consilium.europa.eu/doc/document/ST-10693-2026-REV-1/en/pdf
Fix: "In June 2026 Italy, Bulgaria and the Czech Republic warned the EU's Council that if the other gas-free designs are pushed out, 'only one manufacturer of dry-air solutions remains', with capacity 'lower than the European demand'. They were arguing for those other designs, and the rules allow time-limited exemptions."

**4. Schneider's "declined slightly" is about power generation, not grid demand.**
Text (peak section): "Schneider said demand in its Power and Grid business 'declined slightly'."
Power & Grid is an end market, not a business. The Q3 release (16 October 2026) says it declined slightly because strong demand from grid customers in several regions was offset by declines in power generation. As written, it reads as evidence that grid demand is peaking, and the release says the reverse.
Source: Schneider Electric Q3 2026 revenues release, 16 October 2026 (https://www.webdisclosure.com/press-release/third-quarter-revenues-2026-odiihfxJLgs).
Fix: "Schneider said demand from its power and grid customers 'declined slightly', though only because power generation fell while grid customers stayed strong." Or cut the sentence.

**5. GE Vernova's "+60%" is partly bought.**
Text: "The case against is stronger ... GE Vernova's grid backlog is up 60 per cent in a year." Earlier in the piece the $5bn from Prolec GE is disclosed; in the peak section it is not.
$5bn of the $15.7bn rise came with Prolec GE (closed 2 February 2026). Without it the rise is about 40% ((15.7 - 5) / 26.5). Using 60% as evidence against a peak overstates the organic signal.
Source: GE Vernova Q3 2026 release, 28 October 2026, https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm
Fix: "GE Vernova's grid equipment backlog is up 60 per cent in a year, or about 40 per cent without the Prolec GE purchase."

**6. "The wait ... in 2030" conflates years of work with lead time.**
Text (thesis): "on their own figures the wait will still be measured in years in 2030". The piece itself later says the ratio "is not a quoted lead time". Neither Hitachi ("2.5 to 3 times revenue") nor Siemens Energy (demand above capacity) publishes a wait for 2030.
Fix: "on their own figures the queue will still hold years of work in 2030."

**7. The 135 weeks covers two bushing series, not all 245 to 550 kV bushings.**
Text: "On 29 October 2026 it gave 135 weeks for its high-voltage bushings of 245 to 550 kilovolts from Ludvika". The illustration says "some now wait 135 weeks from Sweden", which is fine.
On the same page, Ludvika's GSA-OA/ARF AF/ED 245 kV bushings are 40 weeks. Only GSBK and ARF 245 to 550 are 135. Guarulhos, Brazil (updated 21 September 2026) quotes GOE bushings up to 1675 at 20 weeks standard. That makes China not the only shorter source, which matters for the next paragraph.
Source: https://www.hitachienergy.com/in/en/products-and-solutions/insulation-and-components/transformer-insulation-components/delivery-times-for-transformer-components (Ludvika updated 29 Oct 2026; Hefei 4 Aug 2026). All other page figures check: GOH 46, GOB+ 40, GSA 40, GOE 27, tap changers UB/VUBB 10 to UZ 22, Hefei ARF 245 and 420 at 14, ARF 550 at 16.
Fix: "135 weeks for its GSBK and ARF high-voltage bushings of 245 to 550 kilovolts from Ludvika". Optionally add that Hitachi's Brazilian plant quotes about 20 weeks for some lower-voltage bushings.

**8. The emergency order also covers UPS systems and backup generators; the "smaller gear" inference is weak.**
Text: "including substation transformers and high-voltage breakers" and "the larger effect may be on parts and on smaller gear".
The definition (Sec. 5(b)) also lists "uninterruptible power supply systems supporting critical infrastructure", "backup generators", instrument transformers, protective relaying and others. It excludes "facilities used in the local distribution of electric energy", and the bulk-power system is defined as 69 kV and up. So the order touches inside-the-fence gear the piece discusses (UPS, generators), but not distribution gear as such. Section 3(b) requires rules within 120 days "as needed". The 24 December arithmetic is right. The RFI (91 FR 57322) was published 9 September 2026, with comments closing 9 October.
Source: https://www.whitehouse.gov/presidential-actions/2026/08/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system/ ; RFI https://public-inspection.federalregister.gov/2026-18370.pdf
Fix: "...including substation transformers, high-voltage breakers, and even UPS systems and backup generators that support critical infrastructure..." Then "...so the larger effect may be on parts and on the other gear the order names, and on the confidence of buyers..." Also say "120 days to write any rules it needs".

**9. The Uptime figure is the average of typical (modal) densities.**
Text: "the average data centre rack drew almost 9 kilowatts".
The Uptime 2025 survey gives an average modal density of "almost 9 kW" (research file), and 7.5 kW once outliers are excluded (The Register, 3 August 2025, reporting the survey). "The average rack" overstates the precision.
Fix: "the typical rack density reported by operators averaged almost 9 kilowatts". Keep "about fifteen times" (132/9 = 14.7).

**10. Schnabel cars: DOE 2024 gives a different count, and "up to 20 axles" is wrong.**
Text: "special railcars with up to 20 axles ... the department counted only about 30 in North America in 2012."
DOE 2012 says the car in its Figure 4 "has 20 axles"; that is not a maximum, because larger Schnabel cars exist. DOE's July 2024 report says "Only about three of these specialized transport cars are available in North America" (p. 19, possibly a narrower class). A reader checking the 2024 report will see the conflict.
Fix: "special railcars, some with 20 axles or more ... the department counted about 30 in North America in 2012, and its 2024 report says only about three of the largest kind are available."

**11. Prices: the biggest jump was 2021.**
Text: "Transformer prices jumped 18 per cent in 2022, then rose only about 4 per cent in 2023 and 2 per cent in 2024."
BLS PCU335311335311, December to December: 2021 +34.4% (258.8 to 347.7); 2022 +18.0%; 2023 +3.8%; 2024 +1.6%; 2025 +5.4%; September 2025 to September 2026 +7.8%. The 2020 average is 255.33, September 2026 is 475.065 (P), and +86% is confirmed. Switchgear: +12.0% (2025) and +12.3% (year to September 2026), and +88% is confirmed. All stated figures check out, but leaving out 2021 makes 2022 look like the first shock.
Source: BLS API, series PCU335311335311 and PCU335313335313, read 7 November 2026.
Fix: "Transformer prices jumped 34 per cent in 2021 and 18 per cent in 2022, then rose..."

**12. Siemens chart: the base year is missing from the body text.**
Text: "By fiscal 2030 the gap narrows to about 10 per cent, as capacity nearly doubles". The caption says doubling "from fiscal 2023 to fiscal 2030", so the body reads as fiscal 2025 to fiscal 2030.
Fix: "as capacity nearly doubles from fiscal 2023".

**13. DOE 2012 consolidation date.**
Text: "In the 2000s, the Department of Energy recorded in 2012, transformer makers consolidated 'to remove excess capacity...'".
The source says "Over the past few decades" (section 5.2.1, describing changes "since the 1980s").
Fix: "Over the preceding decades, the Department of Energy recorded in 2012, ..."

**14. EEI comparison mixes a plan with an actual.**
Text: "plan about $239bn of capital spending in 2026 ... against $204bn in 2024." I could not find the $239bn at source. The wording already says "plan", so it is acceptable if the 9 July 2026 EEI document is confirmed. Fix if unconfirmed: cut it, or use EEI's verified figure for 2025 (about $208bn, a projection).

**15. Hitachi: wording to confirm.**
The June 2026 energy deck (Japanese version, TSE disclosure, 9 June 2026) confirms these points: backlog "2.5 to 3 times revenue, stable"; about $11bn (FY2020), $60bn (FY2025) and about $100bn (FY2030) at FY2026 budget rates; investment of more than $6bn in 2024 to 2027 against $3bn in 2020 to 2023; more than 40 brownfield and greenfield plants. It also says it invests "only in projects with secured profitability". I did not find the English "not building over-capacity" Q&A wording. The deck also shows more than $2bn for North America in 2024 to 2027, while the piece says "its American programme alone is now around $1.5bn". Those can be consistent (US against North America), but a PM may ask.
Fix: keep "not building over-capacity" only if the English Q&A summary is in hand. Otherwise use "invests only in projects whose profitability is secured" (Hitachi deck, 10 June 2026).

**16. Gallman capacity wording.**
Press coverage of the 15 September 2026 release says Gallman is "more than twice the size" of Crystal Springs and will "roughly double" production. The piece says "more than double the old plant's capacity". Check the release wording and match it.

**17. Things a PM would ask that the piece leaves out (optional).**
(a) Cleveland-Cliffs is not the only future US source of GOES: Flux Steel Works has announced an Ohio GOES plant (commercial production 2029, press). One outlet also notes that DOE's own timetable for Butler is 2029. (b) Prolec GE's plants in Mexico supply part of the largest import line (Mexico, 19%), so some "imports" are GE Vernova's own output. (c) Generac flags cancellation rights in its data centre contracts (28 October 2026), which is relevant to how firm the generator backlogs are.

## Confirmed against primary sources
- Siemens Energy Grid Technologies: Q3 FY2026 orders €5,367m, revenue €3,624m, book-to-bill 1.48, backlog €51bn; nine months revenue €9,744m (orders €18,328m, 1.88); Q4 FY2025 revenue €3,145m; Q2 book-to-bill 2.28 (12 May 2026 release); 51/12.889 = 3.96, range 3.92 to 4.00 on rounding.
- Eaton (8-K exhibit 99, 3 November 2026): Electrical Americas Q3 sales $4,172m (Q3 2025 $3,410m), margin 29.8%, up 230 basis points sequentially (so Q2 was 27.5%), against 30.3% a year earlier; twelve-month organic orders +39%; total Electrical twelve-month book-to-bill 1.2 and backlog +46%. 10-Q: total backlog about $26.2bn, "approximately 72%" within twelve months. 15,993/15,229 = 1.050.
- GE Vernova: Electrification orders $5,371m, -9% organic, book-to-bill about 1.4, equipment backlog $42.2bn, up $15.7bn (60%), including $5bn from Prolec GE (closed 2 February 2026). Trench: $9.0bn (at EUR/USD 1.12), "vertically integrating an existing supplier", portfolio "bushings, cable terminations, instrument transformers, coils and capacitors", close expected late 2027.
- Korean anti-dumping final results (FR Doc 2026-16663, published 14 August 2026): HD Hyundai 0.00, Iljin 0.00, LS Electric 4.32, Hyosung 4.32. The 2024-25 preliminary results show the same rates.
- EO 14421 (26 August 2026): not a blanket ban; "initiated after the date"; covered foreign entity plus undue risk; 120 days. Presidential Determination 2026-10 (20 April 2026) names transformers, high-voltage circuit breakers and "electrical core steel".
- UN Comtrade (reporter US, HS 850423): 2022 $1,258m (1,865 units); 2023 $1,927m; 2024 $2,978m; 2025 $4,145m (5,021 units). 2025: Mexico $803m (19.4%), Korea $748m (18.0%), Brazil $531m (12.8%), Austria $431m (10.4%), Netherlands $260m, "Other Asia nes" (Taiwan) $248m, Canada $213m. 2022: Mexico 31.2%, Korea 7.4%. 3.3 times, +39% in 2025, $0.83m per unit.
- IMF copper: 2020 average $6,175; September 2026 $14,473; 2.34 times.
- DOE 2012: "custom-designed equipment"; about 1.3 transformers per design; 80,000 to 120,000 kg of core steel at 300 to 500 MVA; bushings "up to five months"; "highly- skilled work force"; "even a tiny amount of dust or moisture can deteriorate the performance"; "in excess of six months"; prequalification "a lengthy process that can take years"; 100 to 400 tons; about 100 tons per railcar; about 30 Schnabel cars; 5 to 12 and 6 to 16 months (2010); Korea $33m (2005) to $279m (2011).
- DOE 2024: 90%; 100 MVA; "36-month lead times being commonly quoted and maximum lead times reaching as much as 60 months"; under a year before the pandemic; "cannot easily be expanded except by building a new facility"; 1 to 3 years to build; winding machines and core tables "1–2 years" (the source uses an en dash, so the piece's hyphenated quote is fine); route clearance nine months; "roughly 25 percent"; "sole active domestic GOES supplier"; 12 to 20 percent; Nippon Steel PDR; about 80% imported in 2019; "major weak link"; 137 + 617 = 754 units, 82%; about 343 a year; spare installation 3 to 4 weeks (Table 1); "to date STEP has never been utilized"; Grid Assurance "has not yet actually provided a replacement LPT".
- Hitachi Alamo: $106m, "largest bushings manufacturing facility in North America", mid-2027, up to 800 kV. ABB: capex "around $1 billion", not expected to rise further in the mid-term, "selectively leveraging third-party assembly". Schneider: "visibility into 2027 and 2028" (the release says "increasing visibility into 2027 and 2028"). Generac: about $4.5bn; Amazon $2.4bn in 2027 and 2028. Cleveland-Cliffs: $200m, up to 25%, $75m from DOE, early 2028. Siemens Energy Charlotte: $150m (state figure $149.8m), early 2026 as announced, "up to five years".
- Arithmetic: 18,519 A at 54 V; 1,250 A at 800 V; 11,111 and 758 racks; 132/9 = 14.7; 66.9/21.6 = 3.10; Korea exports 738/109 = 6.8 times; 279/33 = 8.5 times.

## Could not verify
- The Eaton Electrical Americas backlog of $15,993m and the earlier ratios (0.89, 0.93, 1.049). The segment backlog table in the 10-Q was not readable through SEC access today. The segment sales for Q4 2025 to Q2 2026 were not checked either.
- Hitachi Energy's $66.9bn backlog and $21.6bn trailing revenue (Hitachi results, 28 October 2026); the earlier 2.8 point.
- The English "remain stable at 2.5-3x" and "not building over-capacity" (the Japanese deck confirms the substance of the first); Hitachi's $1.5bn US programme (15 September 2026).
- Siemens Energy 3.56 (September 2024); the 20% capacity for €600m and more than €2bn by FY2028 (shareholder letter, 14 November 2025); the capital market day chart percentages; the Charlotte release date (the governor announced it on 13 February 2024).
- EEI $239bn and $204.1bn; NREL "up to two years" (the local copy would not open); all Wood Mackenzie figures (128 weeks, 30 weeks, 30% and 15% shortage, the 31 August 2026 note); Reuters, 26 June 2025.
- Comtrade January to August 2026 ($3,011m against $2,743m; China 4.7%) and China's $90m in 2025; Korea's 57% export share.
- Plant details: HD Hyundai Montgomery, Virginia Transformer Rincon, Hyosung Memphis, Prolec GE Goldsboro, Eaton Jonesville and Bellevue, Hitachi South Boston, Siemens Energy Nuremberg and Greater Richland.
- Caterpillar, Cummins and ABB call remarks (third-party summaries, labelled as such); Powell and Vertiv figures; Schneider's "about a quarter" and $1.2m to $3.3m per MW; Nvidia's 200 kg and its 2027 date; GB200 132 kW; the EU F-gas dates (2028 above 52 to 145 kV, 2032 above 145 kV; consistent with the Council note's "2028, and 2032").
- Whether USMCA treatment (Proclamation 11032, clause on Canada and Mexico) changes the rate on Mexican large transformers, Mexico being the largest supplier.
- The BIS inclusions notice (90 FR 40326) adding 8504.23 from 18 August 2025.
