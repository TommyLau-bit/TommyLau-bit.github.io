# Sidecar: virginia-bills-the-empty-site (draft, 29 Oct 2026, batch 3 item A10)

Title: "Virginia now bills data centres for the grid they leave empty. Growth stays shared"
Shape: Analysis. Subject: Dominion Energy Virginia's GS-5 rate class (Virginia SCC, 2025 biennial review, case PUR-2025-00058), effective January 2027.
Body: about 565 words, 15 figures, 1 money range (the JLARC household figure; no company financial figure). Checker: 0 failures, 0 warnings. Build: clean.

## Verdict against the quality bar: PASS (reframed)
The scout outline ("Virginia bills data centres directly for the wires, the opposite of Malaysia") is wrong as stated. The Malaysia re-check lesson applied:
- Dedicated connection assets: Dominion ALREADY recovered the substation built for a data centre from that data centre, through contractual minimum payments, and charged directly for surplus equipment (JLARC 2024, primary). So, like TNB, the connection was never simply on the shared bill.
- Shared network: transmission and generation are allocated by class (GS-4 data centres carried about 16% of transmission and 26% of generation costs in Dominion's allocation, JLARC Table 4-1) and still are.
- What GS-5 adds is a 14 year take-or-pay floor on booked demand for generation, transmission and distribution, with collateral (Dominion 10-K, primary). That is stranded-cost insurance, not a charge for growth.
1. New mechanism: yes. The site has a capacity market spreading costs (pjm-sends-the-bill) and a held Malaysia tariff piece; nothing on minimum bills as insurance against no-shows, or on the mismatch between a 14 year floor and 20 to 40 year asset lives.
2. Primary sources: the claim rests on Dominion's 10-K and JLARC Report 598. The two SCC orders could not be read (see blocks); details from them are labelled press-only below and kept out of the claim itself, except as the falsifier's trigger.
3. PM learning: the headline is "data centres pay their fair share". The finding is that the floor covers the empty-site case only; full campuses still share network growth by peak share, and the floor ends decades before the lines are paid off.

## Proposed claim
Virginia's GS-5 class makes each new data centre guarantee 14 years of minimum payments for the grid it books, which protects households if the campus never fills, but not from the network lines built for campuses that do fill: those stay on the shared bill by each class's share of demand, and are paid off over 20 to 40 years, long after the contract ends.

Alternatives considered:
1. "Virginia bills data centres directly for their wires" (the outline). Rejected: the substation was already billed to the site before GS-5 (JLARC 2024), and GS-5 is a floor, not direct assignment.
2. "The July 2026 order will make data centres pay up front for the lines that connect them." Rejected as the main claim: rests only on press reports of an order I could not read, and is a near-certainty once filed, so it teaches little.
Chosen because it rests on primary text, separates dedicated from shared assets precisely, and the pending line extension docket gives a live, dated test.

## Proposed claims.ts entry
```ts
  {
    id: 'virginia-bills-the-empty-site',
    claim: 'Virginia\'s GS-5 class makes each new data centre guarantee 14 years of minimum payments for the grid it books, which protects households if a campus never fills, but the shared network lines built for campuses that do fill stay on the pooled bill by each class\'s share of demand, and are paid off over decades, long after the contract ends.',
    breaksIf: 'By the end of 2027, Virginia\'s regulator makes GS-5 customers pay directly for shared network transmission, such as the planned 765 kV Valley Link line, rather than through their class share of demand, or extends the minimum term to cover the lines\' recovery life.',
    watch: ['The SCC ruling on Dominion\'s amended line extension policy, filed under the 31 July 2026 Rider T1 order', 'Whether Valley Link or other 500 kV and 765 kV lines are assigned to GS-5 directly', 'GS-5 transmission allocation in the 2027 biennial review, for rates from January 2028', 'The GS-5 minimum term, 14 years from January 2027'],
  },
```

## Map layer (stack.ts)
'grid' (The grid connection), next to pjm-sends-the-bill.

## Glossary
- "Minimum demand charge", Getting power to the building: "A floor on a large customer's bill, set on the demand it contracted, that it pays whether or not it uses that much power."
- "Stranded cost", Getting power to the building: "The unpaid cost of a power station or line built for a customer that leaves or never uses it, which falls on other customers unless a contract covers it."
- "GS-5", Getting power to the building: "Dominion Energy Virginia's rate class, from January 2027, for customers of 25 megawatts or more, mostly data centres, with 14 year contracts and minimum payments."

## numbers.ts (physical only)
{ layer: 'grid', value: '28%', what: 'Share of Dominion Energy Virginia\'s electricity sales that went to data centres in 2025.', piece: 'virginia-bills-the-empty-site', asOf: '2025' }

## LinkedIn post (§9)
From January 2027, a new data centre in Virginia must sign a 14 year contract and pay for the grid it books, used or not.

That protects households if a campus never fills. It does not stop them sharing the new lines built for campuses that do fill, and those lines are paid off over 20 to 40 years, long after the contract ends.

The piece covers how Dominion's new floor works, what it leaves out, and what would prove me wrong.

https://thephysicallayer.fyi/journal/virginia-bills-the-empty-site/

#DataCentres #Grid #Virginia

## Figures in the body, with source
- January 2027 start; 14 year contract; collateral over the term; "demand minimums for distribution, transmission and generation revenues for high load customers at connection"; purpose "to minimize both cross-rate class subsidies and stranded costs": Dominion Energy / Virginia Power Form 10-K for 2025, filed 23 Feb 2026, Business section, https://www.sec.gov/Archives/edgar/data/715957/000119312526063120/d-20251231.htm . PRIMARY.
- 28% of Virginia Power's electricity sales to data centres in 2025 (26% in 2024): same 10-K. PRIMARY.
- 25 MW threshold: 10-K defines the high load revenue category as customers "with actual or anticipated forecast demand of 25 MW or higher and annual load factor of 75% or higher" (same 10-K and Q2 2026 10-Q). The SCC release of 25 Nov 2025 states GS-5 is for customers of 25 MW or more, effective 1 Jan 2027, but its page was blocked to me; its text is quoted consistently in press (WYDaily 26 Nov 2025, Annandale Today). PRIMARY for the threshold via the 10-K; GS-5 name confirmed primary by Dominion's 8-K exhibit 99.1 of 14 Sep 2026 ("Dominion Energy's GS-5 rate class"), https://www.sec.gov/Archives/edgar/data/715957/000119312526390654/d107020dex991.htm
- Substation already recovered from the data centre through contractual minimum payments; surplus equipment charged directly; data centres paying full cost of service; GS-4 includes most data centres: JLARC Report 598, Data Centers in Virginia, 9 Dec 2024, pp. 44 to 46, https://jlarc.virginia.gov/pdfs/reports/Rpt598.pdf . PRIMARY.
- $14 to $37 a month by 2040, 2024 constant dollars, typical 1,000 kWh Dominion household, generation and transmission only (half-unconstrained to unconstrained with VCEA): JLARC Report 598, Table 4-2, p. 48. PRIMARY.
- 20 to 40 years recovery of generation and transmission capital: JLARC Report 598, p. 46. PRIMARY. JLARC p. 49 also: "if a data center ceases operation before then ... costs will be recovered from other customers."
- July 2026 order (Rider T1, filed 31 Jul 2026, SCC document 8dt001): Dominion to file an amended line extension policy with a mandatory contribution in aid of construction for defined "direct connect" transmission facilities within 90 days in a new docket, which may consider upstream costs and a blended GS-5 approach; Valley Link "could" be "directly assigned to the GS-5 rate class": PRESS-ONLY. Utility Dive, 12 Aug 2026, https://utilitydive.com/news/dominion-energy-scc-transmission-costs-data-center/827693 ; WTOP / Virginia Mercury, 5 Aug 2026, https://wtop.com/virginia/2026/08/scc-orders-dominion-to-develop-tariff-to-assign-more-transmission-costs-to-data-centers/ ; WHSV, 5 Aug 2026 (governor's statement). Governor's office release of 23 Jul 2026 on its filing in the case: https://www.governor.virginia.gov/newsroom/news-releases/2026/july-releases/name-1121668-en.html . Ninety days from 31 Jul is 29 Oct 2026, so Dominion's filing should land about now; check it before publish.
- 765 kV Valley Link: PRESS (WTOP, 5 Aug 2026, 115 mile line Lynchburg to Culpeper). Check against PJM RTEP before publish.

## Context read, not in the body
- Rider T1 pending in Q2 2026: total revenue requirement $1,539m ($540m in base rates plus $999m rider), Dominion Q2 2026 10-Q, filed 31 Jul 2026, https://www.sec.gov/Archives/edgar/data/715957/000119312526327487/d-20260630.htm . PRIMARY.
- 2025 biennial review outcome: base rate increase $566m from Jan 2026 plus $210m from Jan 2027, ROE 9.80%: 10-K above. PRIMARY.
- Minimum percentages: 85% of contracted transmission and distribution demand and 60% of generation demand (SCC release text as quoted by WYDaily, 26 Nov 2025, https://wydaily.com/latest/regional-national/2025/11/26/scc-creates-new-class-for-large-scale-energy-users/ ; Thomas Jefferson Institute; one source reads the 60% as collateral). PRESS-ONLY and conflicting on 60%, so the body says only "a minimum". Also press-only: ramp of up to four years at 20% a year minimum, exit fee, three years' notice, pre-2016 customers exempt (Thomas Jefferson Institute commentary quoting the order).
- 2026 legislation SB 253 / HB 1393 (governor's amendments, April 2026; reported one-time GS-5 opt-out for sites with over 200 full-time staff): PRESS-ONLY, not used; check final enacted text on LIS before publish, since an opt-out would matter to the claim.
- NextEra Energy's proposed merger with Dominion (8-K and 425 filings from Sep 2026) commits support for GS-5; not used (no share or deal content in the piece).
- JLARC p. 49 cites AEP Ohio's proposal of an 85% minimum for at least 12 years for data centres over 25 MW, the model GS-5 resembles.

## Blocks (not bypassed)
- scc.virginia.gov (press release and docket PDFs 89g601, 8dt001 and others): CloudFront geo-block from this location, and 403 to the fetch tool. The Nov 2025 and Jul 2026 orders were not read. A fact-checker in the US, or the SCC docket via another route Tommy approves, should read both before publish: Final Order PUR-2025-00058 (25 Nov 2025) for the GS-5 terms, and the 31 Jul 2026 Rider T1 order.
- dominionenergy.com tariff pages: 403. GS-5 tariff sheets not read.
- loudounnow.com: 429. virginiamercury.com: 403.

## Video figures dropped or flagged (Leo Cui, "The Entire Energy Sector Explained: Oil, Gas, Electricity & the Grid", https://www.youtube.com/watch?v=0zZyEF4Cq9U)
- "Data centres already consume roughly a quarter of the state's electricity": FLAGGED and replaced. Primary figure is Dominion's own: 28% of Virginia Power's electricity sales in 2025 (10-K). That is one utility's sales, not the state's; no state figure was verified, so the state version is dropped.
- "Their share could approach half by 2030 under some projections": dropped, unverified.
- "4 to 5% of US electricity in 2024, 9 to 17% by 2030": out of scope for this piece, dropped.
- Video gives no GS-5 detail; the GS-5 outline came from the scout's memory and is verified above (exists, 25 MW, Jan 2027, 14 years, minimums: confirmed; percentages press-only).

## Relation to other pieces
- Builds on pjm-sends-the-bill (capacity costs reach households through the market) without contradicting it: GS-5's generation minimum does not change PJM capacity prices.
- Consistent with the held malaysia-keeps-the-wires-shared re-check: in both places the dedicated connection is already billed to the site; the open question in both is the shared network. If that Malaysia piece is rebuilt, the two could link.

## Notes for publish
- Re-read the two SCC orders and Dominion's line extension filing (due about 29 Oct 2026) before publish; if the new docket already assigns network lines to GS-5, the claim needs rework.
- Check SB 253 / HB 1393 final text for any GS-5 opt-out.
- No banned names, no share prices or views, no em or en dashes in piece, cover or this file.
