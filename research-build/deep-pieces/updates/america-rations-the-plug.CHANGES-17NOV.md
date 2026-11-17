# america-rations-the-plug: changes, 17 Nov 2026

Copy: research-build/deep-pieces/updates/america-rations-the-plug.md (live file untouched). Diff: america-rations-the-plug.diff.
Checker: 0 failures, 2 standing warnings (exposure map 157 words; sources line now 114 words). Visible words 3,598 (live was 3,601).
Claims.ts, the claim box and the "Breaks if" quotes: untouched. No chart changes (no charted number moved). `date` unchanged.

## How the filings were read
FERC eLibrary's public API works without a browser session: `GET https://elibrary.ferc.gov/eLibraryWebAPI/api/File/GetFileListFromP8/<accession>` lists the files with their IDs, and `POST https://elibrary.ferc.gov/eLibraryWebAPI/api/File/DownloadP8File` with JSON `{"FileType":"","accession":"","fileid":0,"FileIDAll":"","fileidLst":["<file ID>"],"Islegacy":false}` returns the PDF. Every transmittal letter below was opened and read this way.

## Changes in the body
- **Which step takes longest**: "PJM's answer, to be filed on 16 November, is one 12-month process a year" became "filed on 16 November, is a single 12-month study each year ... Its first cycle would open in late November 2027 and finish in 2029." (PJM ER27-531 transmittal, pp. 2, 30 to 31, 82.) Cut "The build is the long part." (repeats the next sentence).
- **FERC paragraph**: "PJM and its utilities file their answers by 16 November 2026" became "Five answered with new tariff filings between 13 and 16 November 2026; SPP's answer is due on 20 November."
- **Tiers table**: date line 7 Nov became 17 Nov. Rows rewritten from the transmittal letters:
  - PJM: filed for all large loads 16 Nov, proposed from 16 Mar 2027.
  - CAISO: Flexible interim connection, cut first until upgrades are built; filed 16 Nov, proposed from 16 Feb 2027 (was "Board approved 28 October").
  - NYISO: non-firm service cut when the local price reaches $200/MWh; filed 16 Nov; the price cut from 1 June 2028 (was "Bring new capacity or accept non-firm service | Filing in November or December").
  - ISO New England: interim and permanent non-firm service cut above $250/MWh; filed 13 Nov; awaits FERC (was "To be filed by 16 November | Not filed").
  - MISO: **was wrong, now fixed.** "No cut-first tier; a fast track for loads that bring new power stations" became "Interim NITS; GRITS, part non-firm for good, cut above $100 per MWh | Filed 16 November 2026; GRITS not before 1 January 2029".
  - "Any data centre running on it?" column unchanged (none of the new tiers is in force).
- **Fractional NITS paragraph**: "PJM's own plan for a fourth service" became "a fourth service PJM's transmission owners floated in October" (the evidence fold already sourced it to the owners' 9 Oct notice; neither PJM's nor the owners' 16 Nov transmittal letter names it).
- **Hours section**: "Nobody publishes it ... and no tier states them" became "No tier guarantees a number of hours ... MISO says past prices would have left its non-firm service running in more than 95% of hours." (GRITS letter p. 6.) Cut "The cuts in that model are small and partial." and "The real contracts are confidential." for length.
- **Ride-through**: "Texas has one in force; PJM files its own on 16 November" became "PJM filed its own on 16 November." ("Texas went first" follows two paragraphs later.)
- **22 July section**: cut "The grid did its job." (length).
- **Household bill**: cut the Pennsylvania sentence ("rises of about 3% to 10% ... as reported"), a trade-press figure, for length; its source removed from the fold.
- **Watch line**: "the grids' large-load filings on 16 November" became "SPP's large-load filing by 20 November".

## Changes in the evidence fold and sources line
- **The tiers**: the "due 16 November" line replaced with each filing: docket, date, what the letter says, quoted where quoted, proposed effective dates. The Energy Central NYISO line and the Utility Dive MISO LARS line removed (superseded by primary filings).
- **Ride-through**: "FERC filing 16 November 2026" became the filed docket, ER27-522-000, effective date requested, the duty set in tariff with bands left to PJM's manuals, the existing-load timing, the annual report on the new services, and PJM's "approximately 10 GW" of computational load.
- **Sources line**: added "the grids' large-load filings (13 and 16 November 2026) and PJM's ride-through filing (16 November 2026)".

## New figures and sources (all FERC eLibrary transmittal letters, read in full or in the relevant sections)
- ISO New England, NEPOOL and PTOs, ER27-484-000, accession 20261113-5007, filed 13 Nov 2026: Firm, Interim and Non-Firm Contract Demand Service; interim "a temporary, non-firm transmission service", up to seven years or until upgrades are in service, whichever is longer; non-firm needs no capacity designation; both re-dispatched above "a Large Load Re-Dispatch Price of $250/MWh"; requested effective 14 Nov 2026; loads with a system impact study agreement before 1 June 2027 keep their study.
- PJM, ER27-531-000, accession 20261116-5340, filed 16 Nov 2026: Fast Energization Process, "a single, 12-month process" for generation and large-load requests; opens the business day after Decision Point II of Cycle 01, "late November 2027"; "The first Fast Energization Cycle would therefore finish in 2029"; Interim NITS extended to Large Loads, "as-available on an interruptible basis", energy only; Firm and Non-Firm Contract Demand Transmission Service in new Part XI; Part XI effective 16 Mar 2027; Fast Energization provisions at an indefinite date; 60-day comment period, 120-day action date requested.
- PJM Transmission Owners, ER27-520-000, accession 20261116-5300, filed 16 Nov 2026: rates for FCDS, NFCDS and Interim NITS; pro forma Cost Recovery Agreement with minimum contribution; upgrade costs allocated to zones with large loads for 15 years, then regional.
- CAISO, ER27-506-000, accession 20261116-5179 (refiled ER27-532-000), filed 16 Nov 2026: Flexible Interim Load Interconnection (FILI), energisation before upgrades under a three-party curtailment agreement the CAISO "will post" on its website; no temporal or capacity cap; permanent version planned in 2027; tariff effective 16 Feb 2027; large load 50 MW or more.
- NYISO, ER27-517-000, accession 20261116-5282, filed 16 Nov 2026: Firm and Non-Firm Withdrawal Service; non-firm curtailed by "a mandatory bid cap of $200/MWh"; LLIP provisions from 1 Feb 2027, market participation provisions from 1 June 2028, BTM:NG sunset 1 May 2029.
- MISO and MISO TOs, ER27-526-000, accession 20261116-5323, filed 16 Nov 2026: Large Load Project Review, cost recovery agreements, Firm Service Step Up and Interim NITS ("a non-firm Transmission Service option" for a load progressing to full NITS; curtailed in a transmission emergency after non-firm point-to-point, before NITS); proposed effective 14 Feb 2027; 30-day comment period.
- MISO, ER27-527-000, accession 20261116-5326, filed 16 Nov 2026: GRITS, "a permanent firm and non-firm contract demand-based" service; example of 500 MW load taking 200 MW firm; non-firm interrupted when LMP exceeds the $100/MWh GRITS Offer Cap, which on past data "permits service more than 95% of all Hours"; also curtailed on a Capacity Advisory; non-firm part outside the capacity obligation; proposed effective 16 Mar 2027, implementation "January 1, 2029" at the earliest; rates in a later filing.
- PJM, ER27-522-000, accession 20261116-5309, filed 16 Nov 2026: Large Computational Load (Large Load with 25 MW or more through power electronic conversion); ride-through framework in tariff, details in Manuals; effective 16 Jan 2027 requested; existing loads within one year of the effective date or of Commercial Operation Date, whichever is later; annual report on demand for and use of Interim NITS, FCD and NFCD; "approximately 10 GW of computational load"; 1.5 GW (10 July 2024), 1.8 GW (17 Feb 2025), 3.9 GW (22 July 2026) events match the piece.

## Read and unread
- Read (transmittal letters): ISO-NE ER27-484; PJM ER27-531; PJM TOs ER27-520; PJM ER27-522; CAISO ER27-506; NYISO ER27-517; MISO ER27-526; MISO ER27-527.
- Not read: the tariff sheets, testimony and affidavits behind each letter (so the ride-through bands in the fold remain from PJM's committee decks, not the filed tariff, which leaves them to the Manuals); CAISO's refiled ER27-532 (assumed identical, not opened); CAISO TOs (PG&E ER27-513, SCE ER27-508, SDG&E ER27-521 and others); NY TOs ER27-529 and LSPGNY ER27-518; PJM Inside Lines releases of 16 Nov (scout read them; the transmittals cover the same ground). The "up to 30 GW more by 2030" figure was not added (the ER27-522 letter says PJM's forecast has 32 GW of peak growth 2024 to 2030, 30 GW of it data centres; not needed).

## Not landed yet
- SPP response to EL26-68: due 20 Nov 2026; not filed.
- FERC action on any of the filings above (PJM asked for an order within 120 days).
- ERCOT Batch Zero audit: due by 10 Dec 2026.
- PJM 2029/30 capacity auction: opens 9 Dec 2026.
- NERC Project 2026-02 standards filing: FERC deadline 31 Dec 2026.
- Signed agreements under ERCOT PCLR, SPP CHILLS or any new tier: none checked beyond the 7 Nov search; the body keeps "On 7 November 2026 I could find no data centre ...".

## Draft LinkedIn post (substantial update: every grid but SPP has now filed its answer)

$100, $200, $250. Those are the prices at which MISO, New York and New England now propose to cut a data centre's power first.

On 13 and 16 November five of America's grid operators answered FERC's June order on large loads. Each filed a cheaper plug that can be cut: MISO's GRITS, a permanent part-firm, part-non-firm service, cut above $100 a megawatt-hour; NYISO above $200; ISO New England above $250. PJM extended its interim service to every large load and filed one 12-month study a year, though its first cycle would not finish until 2029. MISO's permanent service starts no earlier than 2029.

Rules are now written almost everywhere. No data centre runs on one yet. That is the test.

thephysicallayer.fyi/journal/america-rations-the-plug/

## Fact-check (17 Nov)

Independent check. Every transmittal letter re-downloaded from FERC eLibrary (GetFileListFromP8 / DownloadP8File) and read at the cited passages.

- ISO New England row and fold, ER27-484-000 (20261113-5007, filed 13 Nov): PASS. Interim Contract Demand Service "a temporary, non-firm transmission service", "no more than seven years, or the length of time required to place the required Large Load Network Upgrades in-service, whichever is longer" (p. 30); Non-Firm needs no capacity designation; both re-dispatched when LMP "exceeds a Large Load Re-Dispatch Price of $250/MWh" (pp. 13, 31); effective date requested 14 Nov 2026 (p. 1).
- NYISO row and fold, ER27-517-000 (20261116-5282): PASS. Non-Firm Withdrawal Service curtailed when nodal LBMP "reaches $200 MW/h" (p. 3); "a mandatory bid cap of $200/MWh" in Part IV; Part IV market participation provisions effective 1 June 2028, LLIP provisions 1 Feb 2027 (pp. 4 to 5).
- CAISO row and fold, ER27-506-000 (20261116-5179): PASS. FILI service "until network upgrades are complete"; "declines to propose any kind of temporal or capacity cap"; "The CAISO will post these agreements on the CAISO website"; permanent version of FILI planned in 2027 (pp. 36 to 37); effective 16 Feb 2027. Refiling confirmed: accession 20261116-5343, "Resubmission under different filing code", ER27-532.
- PJM row and fold, ER27-531-000 (20261116-5340): PASS. Fast Energization studies generation and large-load requests "in a single, 12-month process" (p. ii) and "annually ... in a single cluster over a 12-month period" (p. 20); submission window opens the business day after Decision Point II of Cycle 01, "expected to be late November 2027"; "The first Fast Energization Cycle would therefore finish in 2029" (p. 31); Interim NITS "as-available on an interruptible basis", energy only, extended to Large Loads (p. 34); Part XI effective 16 Mar 2027. The row's quote "a temporary, non-firm transmission service" is unchanged from live and does not appear in this letter (ISO-NE uses it; PJM calls Interim NITS "by definition a temporary service"); left as live, sourced in the fold to the FERC co-location orders, not re-checked.
- MISO row and fold, ER27-526-000 (20261116-5323) and ER27-527-000 (20261116-5326): PASS. Interim NITS "provides a non-firm Transmission Service option" for a load progressing to full NITS; effective 14 Feb 2027. GRITS "a permanent firm and non -firm contract demand -based" service; non-firm interrupted when LMP at its CPNode exceeds the $100/MWh GRITS Offer Cap, which on historical data "permits service more than 95% of all Hours" (p. 6); effective 16 Mar 2027, "the earliest MISO will be able to implement GRITS is January 1, 2029" (p. 2); rate in a later filing.
- Hours paragraph ("MISO says past prices would have left its non-firm service running in more than 95% of hours"): PASS (GRITS letter p. 6).
- PJM Transmission Owners, ER27-520-000 (20261116-5300): PASS for rates for FCDS, NFCDS and Interim NITS, pro forma CRA, 15-year zonal allocation then Schedule 12 regional. Neither 16 Nov PJM letter names Fractional NITS: confirmed.
- Fractional NITS attribution in the body: FIXED. The draft said "a fourth service PJM's transmission owners floated in October". The owners' notice of 9 Oct 2026 (PJM Members Committee posting, 28 Oct) says "the PJM Transmission Owners understand that PJM plans to propose a fourth new transmission service", so it was PJM's plan, reported by the owners. Restored the live wording "PJM's own plan for a fourth service", which also matches "PJM's planned Fractional NITS" in "What would prove me wrong". Fold now reads: Fractional NITS, which "PJM plans to propose".
- Ride-through, ER27-522-000 (20261116-5309): PASS. Effective 16 Jan 2027 requested (61 days after filing); Large Computational Load = Large Load (50 MW) "containing 25 MW or greater" through power electronic conversion; ride-through framework in tariff, details "set forth in PJM's Manuals"; transitional loads comply within one year of the effective date or of COD, whichever is later; annual report on demand for and use of NITS, Interim NITS, FCD and NFCD; "approximately 10 GW of computational load"; 1.5 GW, 1.8 GW and 3.9 GW events match.
- FERC paragraph ("Five answered ... between 13 and 16 November; SPP's answer is due on 20 November"): PASS for the five. SPP date consistent but not confirmed at a primary order: the 4 Aug 2026 FERC notice (FR Doc. 2026-16174) shows a motion for a 95-day abeyance of EL26-68, which from a mid-August deadline lands on about 20 November; I did not find the order granting it.
- Cuts: PASS. "Texas has one in force" cut; "Texas went first" two paragraphs later still explains it. Household bill: Pennsylvania sentence and its fold source both gone, nothing else refers to it. Duke paragraph reads without "The cuts in that model are small and partial." Watch line reads.
- "No cut-first tier" (MISO): gone from the draft; no other occurrence in the piece or in src/. claims.ts and the claims fold: nothing made false (the "Breaks if" list of tiers is "such as" and MISO is among the seven grids). Note for Tommy, not changed: MISO's Firm Service Step Up (ER27-526, "permits NITS service to increase as the required capability becomes available") and PJM's Fast Energization "schedule of interim withdrawal rights" (ER27-531 p. 67) are filed versions of the firm partial plug the piece names as its strongest counter-evidence.
- Dating: the table is "at 17 November" but "None found" rests on the 7 November search (fold says so). Not changed.
- House style in changed lines: no em or en dashes, British spelling, no "updated"/"correction" wording. Claims and claims-record quotes untouched.
- Sources line: PASS, includes the 13 and 16 Nov filings and the ride-through filing.
- Checker after fixes: 0 failures, 2 standing warnings; visible words under 3,600. Diff regenerated.
