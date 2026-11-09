# Fact-check: solar-and-batteries.md (draft)

Adversarial check, 9 November 2026. Read only; no other file was edited. The primary documents were downloaded and their text read directly, apart from where this report says otherwise.

## ERRORS (each needs a fix before publishing)

1. **Caption of the ratings-trend chart and the evidence fold: solar's preliminary ratings.** The piece says "PJM gives solar's preliminary ratings only as stable at 7 to 10 per cent". That is wrong. PJM's preliminary table gives a number for every year. For tracking solar from 2030/31 to 2042/43 it gives 8, 8, 7, 7, 8, 8, 8, 8, 8, 7, 8, 7, 7. The "10" is the binding 2028/29 rating, not a preliminary one.
   Source: PJM, "Preliminary ELCC Class Ratings For Period Delivery Year 2028/29 – Delivery Year 2042/43" (4 Sep 2026), https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/preliminary-elcc-class-ratings-for-period-dy28-dy42-elcc.pdf
   Fix: change the caption to "PJM's preliminary ratings hold tracking solar at 7 to 8 per cent to 2042/43". In the fold, write "tracking solar 8 (2030/31), 8, 7, 7, 8, 8 (2035/36), 7 (2042/43)". Better still, plot the preliminary solar line, since the data exist.

2. **A quote is cut so that it drops PJM's qualifier.** The piece quotes PJM: "storage resources cannot charge other storage resources during winter energy-constrained events." PJM's sentence goes on: "...during winter energy-constrained events **in the model**". Dropping "in the model" turns a modelling assumption into a statement about physics. A PJM analyst would object.
   Source: PJM, "Preliminary ELCC Class Ratings for Period 2028/2029 through 2042/2043" (discussion, 4 Sep 2026), p. 8, https://www.pjm.com/-/media/DotCom/planning/res-adeq/elcc/discussion-of-preliminary-elcc-class-ratings-for-period-dy28-dy42-elcc.pdf
   Fix: quote it in full, ending "...events in the model", and do the same in the evidence fold.

3. **Meitner is described as already running.** The "would not move me" paragraph says: "A campus that runs mostly on solar: Meitner already does, and still needs gas." Meitner was announced on 4 June 2026 and is not operating. Its mix is "wind, solar, and battery storage", not mostly solar.
   Source: Intersect release, 4 Jun 2026, https://www.intersect.com/news/google-and-intersect-deepen-texas-roots-with-new-data-center-and-energy-investments-in-gray-and-roberts-counties
   Fix: "A campus planned to run mostly on clean power: Meitner is, and it still plans firming gas."

4. **The Meitner quote leaves out words without showing it.** The source sentence reads: "The majority of the site's power will come from clean energy **starting on Day One**, with a minority share of the site's demand met by firming on-site gas to ensure reliable operations." The piece's first fragment ends at "clean energy," and leaves out "starting on Day One".
   Fix: either quote the full first part ("...from clean energy starting on Day One") or use an ellipsis.

5. **The auction figures conflate two totals.** The piece says PJM "secured 138,318 megawatts of firm capacity, 6,831 megawatts short of its reliability requirement". But 138,317.8 MW is the RPM auction alone. The 6,831.3 MW shortfall is measured against the total of 149,181.6 MW, which includes 10,863.8 MW of FRR (Fixed Resource Requirement) commitments. The report also says the auction "cleared 6,831.3 MW UCAP less than the Reliability Requirement", so the shortfall figure is right; only the pairing misleads.
   Source: PJM, 2028/2029 BRA Report, 14 Jul 2026, Executive Summary p. 3, https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2028-2029/2028-2029-bra-results-report.pdf ; PJM release, 14 Jul 2026.
   Fix: "It secured 138,318 megawatts in the auction, and with utilities' own committed plants 149,182 megawatts, still 6,831 megawatts short of its reliability requirement."
   Also: "closed on 14 July 2026" should read "whose results PJM published on 14 July 2026". The report gives no closing date for the bidding window.

6. **The evidence fold says Alphabet's release was not read. It now has been.** Alphabet's release, "Alphabet Announces Agreement to Acquire Intersect to Advance U.S. Energy Innovation", is dated 22 December 2025: $4.75bn cash plus assumed debt, closing expected in the first half of 2026. It excludes Intersect's operating assets in Texas and its operating and in-development assets in California.
   https://abc.xyz/investor/news/news-details/2025/Alphabet-Announces-Agreement-to-Acquire-Intersect-to-Advance-U-S--Energy-Innovation-2025-DVIuVDM9wW/default.aspx
   Intersect's 4 Jun 2026 release says "Google closed on its acquisition of Intersect in March 2026". The excluded assets were carved out as IPX Power on 10 Mar 2026.
   Fix: cite the abc.xyz release in the fold and drop "as reported; I have not read Alphabet's release". In the exposure map, "Intersect Power, owned by Alphabet" is loose, because the Intersect Power operating assets went to IPX Power. Write "Intersect, owned by Alphabet since March 2026".

7. **The schematic winter-day chart contradicts itself.** The solar curve peaks at about y=85, below the data centre load line at y=58.5. Solar therefore never exceeds the load, so there is no surplus to charge the 4-hour battery that the chart then shows covering the full load from 16:30 to 20:30. The daytime gap between the solar curve and the load is also left unmarked, which implies that solar covers the day.
   Fix: either draw solar oversized, peaking above the load, with the surplus shaded as "charging the battery", or label the daytime shortfall too. The caption already says the drawing is schematic, but it should still be physically consistent.

8. **The colour key on the ratings bar chart is wrong.** The caption says "Batteries in amber, firm plants in blue". But both solar bars use the same `c-bar` class as the battery, so solar shows in amber as well.
   Fix: give solar its own class or reword the caption.

9. **2025 additions: the measure is not named.** 56.6 GW and 29.5 GW are *net summer* capacity. Table 4.6 gives nameplate as 57.7 GW total and 29.6 GW of solar (the row is "Solar Thermal and Photovoltaic").
   Source: EIA, Electric Power Annual 2025, Table 4.6, https://www.eia.gov/electricity/annual/html/epa_04_06.html
   Fix: add "(net summer capacity)" in the fold. The body can stay as it is.

10. **Fold, CEC reading: "Weekends and summers looked the same".** The CEC chart does not show that. On summer weekdays load ran about 88% to 94% of peak, against about 83% to 86% in winter. Weekends, as an annual average, ran about 85% to 87%. Summer runs about 7 to 8 points above winter, and its daily swing (about 6 points) is twice winter's.
   Fix: "Summer weekdays ran higher, about 88 to 94 per cent, and weekends about 85 to 87: never far from flat."

## ARITHMETIC (all correct)

- 1/0.07 = 14.29, so "about 14" is right. 1/0.57 = 1.754, so 1.75 is right. 1/0.96 = 1.042, so 1.04 is right. 1/0.23 = 4.35, so "about 4.3" is acceptable ("about 4.4" would be equally fair).
- 1/0.240 = 4.17, so 4.2 is right. 1/0.131 = 7.63, so 7.6 is right.
- 43.4/86 = 50.5%, giving 51. 24/86 = 27.9%, giving 28. 11.8/86 = 13.7%, giving 14. 6.3/86 = 7.3%, giving 7. These match EIA's own 51/28/14.
- "About four fifths": (43.4 + 24)/86 = 78.4%. Fair.
- "Halved": tracking solar went from 14 to 7. Correct, though the path was not steady (14, 11, 8, 10, 7). Fixed solar only fell from 9 to 6.
- Auction mix, from Table 6 (cleared UCAP of 149,843 including FRR): gas 45.6%, nuclear 20.5%, coal 17.9%, solar 1.4%. These match the release's 46/20/18/1.
- Chart coordinates: all three data charts were checked point by point against their scales (capacity factors, the 2029/30 bars and the ratings trend). Every point matches the figures in the fold.
- Night: a sunset at 16:30 and sunrise at 7:30 give 15 hours. Chicago on 21 December is about 14h53m. The gap from 20:30 to 7:30 is 11 hours. All fine.

## VERIFIED AGAINST PRIMARY (no change needed)

- **PJM ELCC class ratings:**
  - 2025/26 (Members Committee, 20 Mar 2024, slide 6): tracking solar 14, fixed 9, 4-hr storage 59, nuclear 95.
  - 2026/27: 11, 8, 50, 95.
  - 2027/28: 8, 7, 58, 95.
  - 2028/29: 10, 7, 59, 96.
  - 2029/30: 7, 6, 57, 96; gas CC 75; onshore wind 37.
  - Preliminary 4-hr storage: 42, 34, 30, 26, 24, 23 (2035/36) and 19 (2042/43). Nuclear 96 falling to 92, so "above 90 per cent throughout" is true.
- **2026 ELCC/RRS (30 Oct 2026):**
  - Table 26: winter holds 96.3% of EUE (expected unserved energy) for 2029/30.
  - Table 35: in loss-of-load hours (2028/29 run), fixed solar delivers 4.70% and tracking solar 7.61%.
  - Loss-of-load hours fall at the winter morning and evening peaks (p. 57).
  - The "more total ICAP than the 2027/2028 Capacity Model to serve the same peak load levels" quote is accurate (p. 4).
- **2028/29 BRA:** $325.00, the cap. The release does cite "the continued trend of the addition of large data center loads to the load forecast". The mix is 46/20/18/1.
- **FERC, 196 FERC ¶ 61,245, issued 29 Sep 2026:** "the 2029/2030 BRA opens on December 9, 2026", stated as PJM's statement within the order.
- **EIA:**
  - 20 Feb 2026 article: 86 GW, "a record if realized"; solar 43.4 (51%), batteries 24 (28%), wind 11.8 (14%), gas 6.3 (3.3 CC, 2.8 CT).
  - EPM Tables 6.07.A/B (released 23 Oct 2026): every monthly and annual figure matches.
  - AEO2026 EMM Table 3: lead times of 1 year for batteries, 2 for tracking PV, 3 for CC and 6 for nuclear.
  - 25 Mar 2022 article: the "typically cycled once per day" quote is accurate.
- **CEC slide 10 (12 Aug 2026):** "about 83% at the lowest, about 86% mid-afternoon" on a winter weekday is a fair reading. The low is about 83.2% at hour 3 and the high about 86.3% at hour 15.
- **WP-356** (Haas abstract page): February 2026; authors Chojkiewicz, Manocha, Paliwal, Callaway and Phadke; 68 existing plants; eight years of hourly weather.
- **Google, 10 Dec 2024 (Porat):** the "reducing both the timeline to operation and the amount of new transmission required" quote is accurate.
- **Quantum page:** Haskell County, TX; 640 MW of solar and 1.3 GWh of batteries; "began operations in June 2026"; the Google campus "recently began construction". The page no longer shows an "840 MW" figure.
- **Public Law 119-21 (approved 4 Jul 2025):**
  - §45Y(d)(4) and §48E(e)(4): no credit for wind or solar placed in service after 31 Dec 2027.
  - §70513(g)(5): the termination applies only to construction beginning more than 12 months after enactment.
  - §48E(e)(4)(C): storage is excepted.
  - The applicable year is fixed at calendar 2032, so credits are 100% for construction beginning in 2033, 75% in 2034, 50% in 2035, then none.
  - Storage MACR thresholds: 55% (2026), 60%, 65%, 70%, 75% (after 2029).
- **IRS Notice 2025-42:** the Physical Work Test is the only method, and the 5% safe harbour is kept only for solar of 1.5 MW AC or less. It applies from 2 Sep 2025.
- **House style:** no em or en dashes; Fluence is not named; no share prices or valuations.

## UNVERIFIABLE (or not checked against primary)

- **WP-356 full text:** the PDF sits behind an eScholarship bot check. The quote "backup ... occurs primarily during winter nights" and the "not peer reviewed" statement could not be checked against the PDF; they rest on the research notes. The abstract page was read.
- **Posting dates of the PJM rating documents** (28 Feb 2025, 1 Aug 2025, 25 Feb 2026, 7 Aug 2026, 4 Sep 2026): the PDFs carry no dates, so these rest on the notes. The values in them are verified.
- **CEC deck of 21 Nov 2024** ("~67% of installed capacity"): not opened. The 2026 deck does carry "Utilization factor (67%): requested capacity vs. max demand", which supports it.
- **"Microsoft, Google, Amazon and Meta have signed for old reactors":** no source in this piece's fold. Add primary releases or rely explicitly on the linked nuclear piece.
- **"The gas turbine makers sold out to 2032":** rests on the linked piece; not checked here.
- **The sources line cites EIA Today in Energy of 7 Aug 2026,** but nothing in the body uses it. Remove it or use it.
- **Whether Quantum stayed with Alphabet or went to IPX Power:** not stated anywhere I could read. Alphabet's release names the Haskell County site as a continuing joint project, which suggests it stayed.

## OVERSTATEMENTS AND CONCESSIONS

1. **ELCC is a marginal, modelled number, not a physical property.** PJM rates a class by "the EUE reduction that a marginal addition of each class produces compared to ... perfect capacity" (RRS p. 52; Discussion p. 4). So "megawatts needed per firm megawatt" (1/ELCC) holds only at the margin, under PJM's model, its weather years and its portfolio. Say so once, briefly.

2. **PJM's own sensitivities show how fragile the storage number is.** This is the biggest omission (RRS Appendix IV, pp. 82 to 84).
   - If new large loads (data centres) are modelled as constant through the year, instead of being added during it, the 2029/30 rating for 4-hr storage rises from 57% to **66%** and tracking solar from 7% to 9% (Table 40).
   - Dropping the single cold winter of 1993/94 also lifts 4-hr storage from 57% to 66% (Table 43).
   - So part of the winter risk that penalises storage comes from a modelling choice about how data-centre load ramps in. A sceptic will say the piece's mechanism is partly PJM's assumption. Concede it, or the piece is exposed.

3. **Storage's *final* ratings have not fallen.** They run 59, 50, 58, 59, 57. All the decline is in non-binding preliminary numbers that PJM says "will likely differ from the official results". So "PJM's ratings move against storage as storage grows" overstates. Write "PJM *expects* its ratings to move against storage". Also, the falling solar figure sits in a paragraph about storage: solar fell because of winter risk, not because storage grew.

4. **PJM's stated "main driver" is different.** For storage, PJM gives it as winter risk periods lasting multiple hours "due to flat load shapes and the protracted duration of Unlimited Resources' forced outages under cold weather", that is, gas plants tripping. The piece's mechanism, that more batteries mean longer hours, is PJM's secondary point (the portfolio shift). PJM's "flat load shapes" is actually useful support for the data-centre link; consider quoting it.

5. **Causation from AI load to solar's rating.** The summary and the claim say an AI data centre draws power through winter nights, "so the grid counts them as a fraction". But solar's low PJM rating came before the data-centre load wave: it was already 14% in 2025/26, and the cause is the cold-weather winter peak and gas outages. Data centres add to winter risk (see the sensitivity above) but did not create it. Reword as two facts side by side, not cause and effect.

6. **The Berkeley paper cuts against the piece.** Its headline finding is that solar and storage met **over 95%** of a constant load at 68 sites, at a levelised cost of $60 to $138/MWh, with gas covering at most 5%. It also finds backup needs "overlap little with grid stress" in most regions. The piece cites only "winter nights". A fair reading must concede that the paper finds solar and storage can carry most of a flat load, and that the hard part is the last few per cent. That is the winter-night point, but stated honestly. The paper's "system peaks on summer afternoons" is also not PJM's picture, where risk is in winter, so say which grids it refers to.

7. **Lead times are selective.** The same EIA table gives an industrial-frame gas combustion turbine **2 years**, the same as solar. "Solar and batteries are the one route where nobody is waiting on a scarce machine" also ignores the interconnection queue (LBNL median over 5 years, all technologies) and transformers. Both affect solar too, and the paragraph itself cites the grid wait. Concede both.

8. **The CEC data are existing California data centres, not AI campuses.** They are largely colocation and enterprise loads. "An AI data centre ... does not [empty at night]" goes beyond the source. The same chart also shows data-centre load highest on *summer afternoons*, when solar is strongest. Concede it.

9. **Solar at 1% of the auction is circular.** UCAP already applies the 7 to 10% rating, so solar's small share of cleared UCAP restates the rating rather than adding evidence. "The largest thing being built" is also a national figure, set beside a PJM auction share.

10. **"About an eighth of its rating" in December is a US-wide average,** weighted to Texas, California and Arizona, yet the paragraph is set in "the northern states". Northern-state December output is lower. Say "nationally".

11. **"The capacity charge ... is the price of the difference"** overreaches. PJM's release puts the shortfall on load growth ("demand ... continues to grow faster than electricity supply"). The accreditation effect PJM quantifies is +0.4 IRM points (2028/29 against 2027/28). Soften to "part of the price".

12. **ERCOT.** Both Google parks are in ERCOT, while every rating in the piece is PJM's. ERCOT's risk hours and its solar ELCC differ (ERCOT figures are not verified here). Either say the ratings are PJM's and Texas has its own, or drop ERCOT from the exposure map, which says ERCOT "rate[s] each plant's firm value" without a figure.

13. **"Move me" event 1 is close to met already.** PJM rates 8-hr storage at 69% for 2029/30 against 57% for 4-hr, which already counts as "well above". Give it a threshold, for example 8-hr above 75% in a BRA.

14. **The tax gloss.** "At least 55 per cent of its cost" should be the material assistance cost ratio of its *manufactured products*, not total project cost. "Aimed at Chinese suppliers": the law covers China, Russia, Iran and North Korea. Write "chiefly Chinese".

## CLAIM

- **Supported:** yes. Every number in the claim box is on record.
- **Leg 1, PJM's 2030/31 ratings (tracking solar 10% or less, 4-hr storage 50% or less):** near-certain to pass.
  - PJM's preliminary 2030/31 values are tracking solar **8%** and 4-hr storage **42%**.
  - Solar has not been above 11% since 2025/26.
  - The only real risk is a change of method or load modelling. The constant-large-load sensitivity adds about 9 points to storage, which would take 42 to about 51.
  - PJM computes the 2030/31 ratings in December 2026 or January 2027, so this resolves within weeks of publishing.
  - As written it is not "genuinely uncertain". Pass odds: about 85 to 90% for storage and about 98% for solar.
- **Leg 2, no 300 MW campus on solar and batteries alone, off-grid with no fuel, by end-2028:** a near-certain pass and a strawman, because nobody is claiming they will do it. It tests the opposite of no one's position, not the mechanism.
- **Does it test the mechanism it names?** Only partly. The named mechanism is that winter-night risk makes storage worth less as it grows. Suggested tighter tests, choose one or two:
  - (a) "PJM's 4-hr storage rating for 2030/31 is **below 50%** and for 2031/32 **at or below 40%**, below every 4-hr rating PJM has used in an auction." This is a real test of "falls as storage grows", and a method change could break it.
  - (b) "Winter's share of expected unserved energy in PJM's 2027 ELCC/RRS stays above 90% for the auctioned year." This tests the winter-risk premise directly.
  - (c) Drop leg 2, or replace it with something uncertain, such as "the next two hyperscaler co-located solar parks announced in the US include on-site firming (gas or other fuel)".
- The claim's "so" clause carries a cause the evidence does not show (see concession 5). Make it two statements.

## VERDICT

Nearly every number checks out against the primary sources. Fix the solar caption error, the clipped PJM quote ("in the model"), Meitner described as running, the spliced quote, the RPM/FRR conflation and the self-contradicting schematic. Concede PJM's own sensitivity that lifts storage to 66%, the pro-solar finding of the Berkeley paper and the marginal nature of ELCC. Tighten the claim, which as written is a near-certain pass.

## APPLIED (9 Nov 2026, evening)

All ten errors fixed in solar.src.md, charts.py and assemble.py. Concessions added: gas turbine also two years; connection queue and transformers; California data centres, not AI campuses, and summer higher; "nationally" for the eighth; Berkeley's 95% headline; ELCC marginal and model-dependent; binding battery ratings not yet fallen ("PJM expects"); PJM's main driver quoted ("flat load shapes"); the 57 to 66 sensitivities; the circular 1% share; "part of what the capacity charge prices"; ERCOT note; "chiefly Chinese", manufactured parts. Unused 7 Aug 2026 EIA source removed. Claim tightened to option (a) plus solar: four-hour storage below 50% (2030/31) and at or below 40% (2031/32), tracking solar at 10% or less; the off-grid campus leg dropped; the "so" removed. Move-me event 1 given a threshold (eight-hour above 75%). Checker: 0 failures.
