# nuclear-for-ai: update round, 17 Nov 2026

Copy: research-build/deep-pieces/updates/nuclear-for-ai.md (copied afresh from the live file). Diff: nuclear-for-ai.diff. Live file untouched. `date` unchanged. Claim text and "Breaks if" quotes identical to live (checked by diff); only the Oklo "Where later evidence bears on it" line edited.
Visible words: 3,596 (live 3,599). Checker: 0 failures, 1 warning (sources line 198 words; was 195 on the live piece).

## Added / edited

1. **Oklo and Centrus definitive HALEU contracts** (fuel section, the "first cracks" paragraph). Old: "...went straight to Centrus as a credit towards fuel orders. The crack moves fuel in the 2030s, not this decade." With deliveries scheduled from 2029 that last sentence was no longer simply right. New: "On 12 November 2026 Oklo signed definitive contracts for Centrus HALEU for up to five reactors, publishing no tonnage. Deliveries are scheduled to begin in 2029, so the crack moves fuel from the turn of the decade."
   - Centrus 8-K (Items 8.01, 9.01), filed 12 Nov 2026, accession 0001628280-26-073175, exhibit 99.1 (joint release): https://www.sec.gov/Archives/edgar/data/1065059/000162828026073175/oklo_metasecurefuelfromc.htm . Quotes: "multiple definitive, multi-year contracts"; "formalize the June 2026 letter of intent"; "enough HALEU to support up to five Aurora powerhouses for multiple years"; deliveries from Piketon "scheduled to begin in 2029"; "supported by Meta's prepayment for future Oklo power production"; Centrus "$5.4 billion in customer contracts and commitments to purchase LEU and HALEU". No tonnage, price or SWU figure. First Idaho Aurora still uses recovered EBR-II fuel (same release), so the Oklo first-core sentence is unchanged.
   - No Oklo 8-K on EDGAR for 10 to 17 Nov 2026 (full-text search, "HALEU" and "Centrus"); the Centrus exhibit is the only filed copy.
2. **Watch list**: "Whether its 12 tonnes a year of HALEU becomes a contract" now "How much of its 12 tonnes a year is contracted, since Oklo published no tonnage". A contract exists; its size against 12 t/yr cannot be measured.
3. **Oklo claim, "Where later evidence bears on it"**: adds "and definitive multi-year contracts announced on 12 November for up to five Aurora powerhouses, with deliveries from 2029 and no tonnage published". The power limb is unchanged: Meta's arrangement is still a prepayment for future power, not a PPA.
4. **Evidence fold (HALEU)**: the 8-K quotes above added. Sources line: Centrus 12 November 2026.
5. **Crane "second half of 2027" source fixed.** The 6 Aug 2026 release says only "restarting operations in 2027". The primary written source for "second half" is Constellation's FERC waiver request, docket ER26-2028-000, 31 Mar 2026 (accession 20260331-5562), page 17: Constellation "expects Crane to be physically able to generate in the second half of 2027, and to receive relevant Nuclear Regulatory Commission approvals to do so in early 2027". Read in the filed PDF (copy at https://www.rtoinsider.com/wp-content/uploads/2026/04/20260331-5562_2026.03.31-Crane-Waiver-Request.pdf). The date in the text stays; attribution fixed in two figcaptions (Crane plug chart; restarts milestones chart), the evidence fold (Crane's grid timeline, quote added) and the sources line (Constellation 31 March 2026 added). The CEO repeated "second half of 2027" on the 9 Nov Q3 call (ANS, 12 Nov, press; no primary transcript found), so the date is current.
   - Same fix is needed on the Power page: src/data/power.ts line 804/805 cites "Constellation (20 September 2024, 6 August 2026)" for "second half of 2027". Not touched (outside this chapter); flag for the lead.

## Cut (to pay for the additions)

- Sodium paragraph: "A fast core also turns more of its uranium-238, most of the fuel, into plutonium, which then splits too." (secondary detail, used nowhere else).
- "as a credit towards fuel orders" (the fold keeps the Meta payment); "under its Oklo framework" to "Oklo".
- "in all its years of running" to "over its life"; "so this is a buying schedule" to ": a buying schedule".

## Checked, not added

- DOE conditional loan commitment of up to US$5.0bn for Constellation uprates (Oct 2026) and Google's first uprate "expected in 2028": the second is already in the piece; the loan is financing, not a clock, and does not test the claim. Not added (also no word room). Not opened at a primary source this round.
- Line 269 ("Centrus contracting its 12 tonne a year build-out with firm customers ... would start a commercial HALEU supply"): left word for word. Oklo's contracts meet it only in part: a firm customer and a definitive contract, but no volume published, deliveries not before 2029, and the US$5.4bn total mixes LEU and HALEU. Not yet the full test.
- ASP Isotopes 10-Q (filed 16 Nov 2026, https://www.sec.gov/Archives/edgar/data/1921865/000119312526463698/aspi-20260930.htm): uranium enrichment still described as a future initiative; nothing enriched. No change.
- X-energy 10-Q (12 Nov): matches the piece. Constellation Q3 release and 10-Q (9 Nov): no Crane date, no uprate filing at the NRC.

## Not landed yet

- First AI-funded extended uprate filed at the NRC.
- Piketon long-term lease (DOE target 31 Dec 2026).
- ASP Isotopes first uranium-235 enrichment.
- Palisades restart date; Crane NRC decision (target 4 March 2027).
- A published HALEU tonnage under any Centrus commercial contract.

## Could not verify at a primary source

- The 9 Nov call wording "second half of 2027" (press only; the 31 Mar FERC filing carries the date instead).
- NRC pages (nrc.gov not opened this round).

## LinkedIn

Update is modest (one contract, one source fix); no post drafted.

## Fact-check (17 Nov)

Independent check of the draft against primary sources. Checker after fixes: 0 failures, 1 warning (sources line 198 words, as before); visible words under 3,600; no em or en dashes; claim text and "Breaks if" quotes untouched; live file untouched.

1. **Oklo and Centrus contracts, fuel section** (Centrus 8-K, accession 0001628280-26-073175, filed and accepted 12 Nov 2026, Item 8.01 and exhibit 99.1, read on EDGAR). FIXED.
   - "definitive", "multi-year", "up to five Aurora powerhouses for multiple years", Piketon deliveries "scheduled to begin in 2029", no tonnage, price or SWU: PASS, word for word.
   - "On 12 November 2026 Oklo signed": the filing gives no signing date; the 8-K says Centrus "issued a press release announcing that it had signed" on 12 November. Changed to "Oklo announced".
   - "up to five reactors": the filing says "powerhouses". Changed to "up to five Aurora reactors" so the reader ties it to the 75 MW Aurora named two paragraphs up (one reactor per Aurora powerhouse).
   - "from the turn of the decade": vaguer than the filing and reads as about 2030. Changed to "only at the decade's end", which matches a 2029 start and keeps the link to the claim (HALEU reactors deliver little before 2031).
   - The draft text does not mention the Meta prepayment link; nothing overstated there.
2. **Evidence fold (HALEU)**: the quote "supported by Meta's prepayment for future Oklo power production" belongs to "The HALEU purchase", not to the Oklo prepayments. FIXED to "Oklo prepayments, the purchase "supported by ..."". Other fold quotes ("multiple definitive, multi-year contracts", "formalize the June 2026 letter of intent", US$5.4bn of LEU and HALEU contracts and commitments): PASS.
3. **Oklo "Where later evidence bears on it" line**: "announced on 12 November", "up to five Aurora powerhouses", "deliveries from 2029", "no tonnage published": PASS (same exhibit).
4. **Watch list** ("How much of its 12 tonnes a year is contracted, since Oklo published no tonnage"): PASS; "its" reads as Centrus from the sentence before.
5. **Crane "second half of 2027", Constellation FERC waiver request, ER26-2028**: PASS. Opened on FERC eLibrary: accession 20260331-5562, "Constellation Energy Generation, LLC's Request for Prospective, Limited Waiver under ER26-2028", file "2026.03.31 - Crane Waiver Request.pdf" (38 pages). The eLibrary download and the RTO Insider copy are byte-identical (SHA-256 b6ea2af0...97a4a, 681,226 bytes). Page 17, item (2), word for word: "Constellation expects Crane to be physically able to generate in the second half of 2027, and to receive relevant Nuclear Regulatory Commission approvals to do so in early 2027". (The filed document's caption reads "Docket No. ER26-____"; the number ER26-2028 is eLibrary's.) Figcaptions, fold and sources line (Constellation 31 March 2026) consistent.
6. **Cuts**: PASS. No "plutonium", "uranium-238" or fast-core breeding reference remains anywhere in the draft (text, aria-labels, folds); the sodium paragraph reads straight from pressure to "The price is a coolant...". "as a credit towards fuel orders" is not relied on anywhere. "over its life" and ": a buying schedule" read cleanly.
7. **Sources line**: Centrus 12 November and Constellation 31 March present. PASS.

Not checked: the 9 Nov call wording (press only, as the writer says). Still open for the lead: src/data/power.ts cites Constellation 2024 and 6 August 2026 for "second half of 2027"; the primary written source is the 31 March 2026 FERC waiver request.
