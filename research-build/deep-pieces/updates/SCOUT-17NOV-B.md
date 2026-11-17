# Scout B, 17 Nov 2026 (window 14 to 17 Nov 2026, plus anything the 14 Nov scout missed)

Chapters: the-queue-not-the-chip, nuclear-for-ai, microreactors, and the Power page's reactor restart card (src/data/power.ts).
Method: SEC EDGAR filings (submissions API and the documents themselves), the Federal Register API (published documents and today's public inspection list), the Energy Commission (st.gov.my) homepage and newsroom, and web searches as leads only. nrc.gov was not opened (it returned 403 on the last run). Nothing in the repo was edited.

## Headline

One real find, two days before the window and missed by the 14 Nov scout: **Oklo and Centrus signed definitive HALEU contracts on 12 November 2026** (item 6a). It turns a "letter" in nuclear-for-ai into a contract. Everything else either did not land or confirms what the pieces already say.

## 1. Constellation Q3 2026 (Crane, uprates, Palisades, Duane Arnold)

PARTLY LANDED, and it raises a sourcing point on the Power card.
- Q3 release, 9 Nov 2026 (8-K exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1868275/000186827526000116/ceg-20261109991.htm; also https://www.constellationenergy.com/news/2026/11/constellation-reports-third-quarter-2026-results.html): **no mention of Crane at all.** It says nothing about Palisades, Duane Arnold, Microsoft or the NRC either.
- Q3 10-Q, filed 9 Nov 2026 (https://www.sec.gov/Archives/edgar/data/1868275/000186827526000119/ceg-20260930.htm): Crane appears only as the Eddystone rights transfer (FERC waiver June 2026, "we subsequently transferred the CIRs to Crane"), the DOE loan guarantee "for up to $1.0 billion" with "no borrowings on this loan as of the date of this filing", and capex. **No restart date anywhere in the 10-Q.**
- Q3 slides (exhibit 99.2, same 8-K): no Crane date in the text layer.
- **Source of "second half of 2027".** The Q2 release of 6 Aug 2026 (https://www.sec.gov/Archives/edgar/data/1868275/000186827526000097/ceg-20260806991.htm) says only: the NRC fuel licence amendment is "a major milestone moving us closer to restarting operations in 2027". It does **not** say second half. On the Q3 call (9 Nov), the chief executive reportedly said the restart "remains on track for the second half of 2027", ahead of schedule, with fuel assemblies and transformers on site (ANS Nuclear Newswire, 12 Nov 2026, https://www.ans.org/news/article-8576/constellation-q3-updates-new-peak-uprates-restart-midterm-elections/). That is press on a company call, not the transcript; I could not reach a primary transcript.
  - Touches: power.ts line 804 ("to power in the second half of 2027") and its source at line 805 ("Constellation (20 September 2024, 6 August 2026)"); nuclear-for-ai lines 115, 251, 263 (second half of 2027). The date itself still stands (the company repeated it on 9 Nov), but **the 6 August release does not carry the "second half" wording.** Recommend the source line be checked against wherever the piece took "second half" from (possibly the 6 Aug call, not the release). If no primary written source says "second half", the honest wording on the primary record is "in 2027".
- **Uprates.** Release and 10-Q: Google deal, "approximately 890 MW ... with the first uprate expected in 2028"; Calvert Cliffs "190 MW capacity expansion expected to come online between 2030 and 2032". Slides: uprate capacity 110 MW in 2027 to 2028, 1,165 in 2029 to 2030, 605 in 2031 to 2032 (my reading of the slide's text layer, labels and order to be checked against the image); "$1.3B of uprate investment already included in 2026 - 2027 growth capital guidance". **No AI-funded uprate in Q4 2026 is named anywhere**, and no uprate filing at the NRC. Matches nuclear-for-ai line 144 ("Constellation's first by 2028").
- New since the piece, and older than the window: DOE conditional loan commitment (October 2026) for "up to $5.0 billion" for uprates, 30-year term, Treasuries plus 0.375%; slides say it "covers up to 80% of eligible costs from 2023 - 2035". Nuclear-for-ai has no line on uprate financing. An optional fact only; it does not test the claim.
- Older and not in the piece: NRC environmental assessment and finding of no significant impact for Crane, 91 FR 60988, 25 Sep 2026 (https://www.federalregister.gov/documents/2026/09/25/2026-19603/constellation-energy-generation-llc-christopher-m-crane-clean-energy-center-environmental-assessment). The piece gives only the 4 March 2027 target decision. Optional: one clause showing the environmental half is done.
- Palisades, Duane Arnold: nothing primary in the window. The Federal Register has only the Holtec Pioneer SMR-300 construction permit receipt notices (10 and 17 Nov, 91 FR 72577 and 73817; application received 30 Sep 2026). These are new reactors at the Palisades site, not the restart. Not relevant to any sentence.

## 2. NRC Part 57 microreactor final rule

NOT LANDED (17 Nov). The Federal Register, docket NRC-2025-0379, still shows only the proposed rule (91 FR 23628, 1 May 2026) and its correction (91 FR 27870, 15 May 2026). Today's public inspection list for the NRC has two ACRS documents, the Pioneer notice and the TRISO-X order, but no Part 57. The deadline is reportedly 23 Nov (EO 14300, press only). Microreactors line 182 ("proposed in May 2026") stays right. Recheck on 23 to 25 Nov: the public inspection list shows a rule a day before it publishes.

## 3. NRC 50.43(f) rule

CONFIRMED, no change. Federal Register API: "NRC Reviews of Reactor Designs Previously Authorized by U.S. Department of Energy or Department of War", 91 FR 67195, published 26 Oct 2026, doc 2026-21801, docket NRC-2025-1503, effective_on 2026-11-25; DATES: "This final rule is effective on November 25, 2026." No correction or delay notice since. https://www.federalregister.gov/documents/2026/10/26/2026-21801/nrc-reviews-of-reactor-designs-previously-authorized-by-us-department-of-energy-or-department-of-war . Matches microreactors.CHANGES.md.

## 4. Tenaga Nasional Q3 results

NOT LANDED. No Q3 FY2026 results or briefing found (searches; TNB's IR pages returned 404 on direct fetch, and I did not get into Bursa's announcement pages). Last year's Q3 came out in late November. The piece's June 2026 point (1,256 MW against 5.65 GW, lines 15, 96, 136, 335) remains the latest Tenaga figure.

## 5. Energy Commission paper on a wholesale market for large users

NOT FOUND. The st.gov.my homepage and newsroom (read 17 Nov) list nothing on it. The newest items are the November AFA notice (30 Oct), new commissioners (2 Nov), the EMA MOU renewal (press release, 26 Oct) and a weekly bulletin (9 to 15 Nov, Facebook video). The "Market Structure & Access" page has general text only. The 10 Nov wholesale market remarks remain press only (The Edge, https://theedgemalaysia.com/node/825311). Same status as on 14 Nov: fails the bar on sourcing.

## 6. Centrus, Oklo, Kairos, X-energy, Standard Nuclear

### 6a. Oklo and Centrus definitive HALEU contracts: LANDED (12 Nov 2026, primary)
- Source: Centrus 8-K, Item 8.01, dated 12 Nov 2026, exhibit 99.1 (joint release), https://www.sec.gov/Archives/edgar/data/1065059/000162828026073175/oklo_metasecurefuelfromc.htm
- What it says: Oklo "signed multiple definitive, multi-year contracts" with Centrus for HALEU. They "formalize the June 2026 letter of intent" and "include enough HALEU to support up to five Aurora powerhouses for multiple years", with "fuel deliveries ... scheduled to begin in 2029" from Piketon. Oklo makes "prepayments" towards the new enrichment capacity, "supported by Meta's prepayment for future Oklo power production", for "the first phase of Oklo's planned 1.2 GW power campus in Ohio". Centrus: "$5.4 billion in customer contracts and commitments to purchase LEU and HALEU from the new capacity". **No tonnage, price or SWU figure is given.**
- Sentences it touches in nuclear-for-ai:
  - Line 306 (old Oklo claim, "where later evidence bears on it"): "a conditional HALEU supply agreement with Centrus on 30 September 2026" is now definitive (12 Nov). The limb "the letters of intent stay letters" moves further on fuel. On power it does not move: still no binding PPA, since the release calls Meta's arrangement a "prepayment for future Oklo power production".
  - Line 263 ("whether its 12 tonnes a year of HALEU becomes a contract") and line 269 ("Centrus contracting its 12 tonne a year build-out with firm customers ... would start a commercial HALEU supply"): **partly met**. There is a definitive contract with a firm customer for deliveries from 2029, but no volume is published, so it cannot be set against the 12 tonnes. Careful wording is needed; this is not yet the full test.
  - Line 219 ("the fuel loop has its first cracks: X-energy ... prepayment ... Meta's first payment ... went straight to Centrus"): the definitive contracts reinforce it. The "fuel in the 2030s, not this decade" framing should be checked against "deliveries ... begin in 2029".
  - Line 215 (Oklo's first core rests on five tonnes of government HALEU): unchanged. The release says the first Idaho unit uses the EBR-II fuel, and Centrus fuel serves Ohio and later Aurora-INL refuelling.
- Quality bar: primary (SEC exhibit), a new fact on a mechanism already covered (HALEU supply), and it moves a dated signal. Candidate for an update, subject to fact-check and Tommy's OK.

### 6b. X-energy 10-Q (12 Nov 2026): confirms, no change
https://www.sec.gov/Archives/edgar/data/2088896/000119312526456659/xe-20260930.htm . Amazon "announced options to bring more than 5 GWe ... by 2039"; Energy Northwest "four reactors representing 320 MWe", operations "in the early 2030s"; Long Mott construction permit announced 9 Nov; TX-1 "completed vertical construction in September 2026". Matches nuclear-for-ai lines 169 and 215. No edit needed.

### 6c. TRISO-X confirmatory order (Federal Register, 17 Nov 2026): minor, not added
91 FR 73818, doc 2026-23395, https://www.federalregister.gov/documents/2026/11/17/2026-23395/in-the-matter-of-triso-x-llc-confirmatory-order-modifying-license . It resolves an apparent violation (notified 9 Jun 2026) over the TX-1 process building's main force resisting system "during construction", settled by mediation. It does not change TX-1's capacity or date. It touches microreactors line 131 ("With TRISO-X running ...") only as a background risk. Does not clear the bar.

### 6d. Standard Nuclear 10-Q (12 Nov 2026): already cited
https://www.sec.gov/Archives/edgar/data/2086716/000162828026073090/nucl-20260930.htm . The microreactors figcaption (line 113) already cites "quarterly reports to 30 June and 30 September 2026". No new check made on the February 2027 DOE approval target. Worth a one-line confirm in the fact-check pass.

### 6e. Kairos, Radiant, DOE HALEU: NOT LANDED
- Kairos: nothing dated 14 to 17 Nov found. The latest is the Samsung C&T term sheet (Sep 2026, press).
- Radiant Kaleidos: no report of operation at power. Microreactors line 157 ("has not yet run at power") stands. The DOE readiness review is reportedly still pending (press, early Nov).
- DOE HALEU allocation: no fourth round found. Microreactors' three-round table (lines 143 to 145) stands.
- BWXT 8-K (13 Nov 2026, Items 1.01, 2.03): a financing agreement. Not read in full; not a fuel fact.

## Recommended for Tommy (short list)
1. Oklo and Centrus definitive HALEU contracts (6a): an update candidate for nuclear-for-ai lines 306, 263 and 269, with careful wording (no volume published).
2. The Crane "second half of 2027" source line (power.ts 805; nuclear-for-ai figcaption 115): repoint it to a primary that says "second half", or keep the date and note that the written record says "in 2027". Fact-check pass, not new content.
3. Recheck on 23 to 25 Nov: Part 57 on the Federal Register public inspection list; TNB Q3 results (late Nov).
