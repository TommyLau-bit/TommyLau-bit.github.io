# The deck-style rewrite of all 13 pieces (6 Nov 2026, evening)

Branch `deck-style-rewrite` (commits 66d5973 Johor, 257d82a the other 12). NOT merged, NOT pushed, NOT live. Publish only on Tommy's word.

## What every piece now carries (Tommy's approved list)
1. The split up front: one paragraph splitting the fuzzy word, saying which part the piece is about.
2. The chain with the choke point: five steps in prose plus one diagram in the top layer, binding step shaded "THE CHOKE POINT", then why that step binds.
3. One analogy, mapped part by part.
4. Falsifiers said plainly: the tests, what would move me first, what would not.
5. The out-of-the-box angle as its own beat just before "What would prove me wrong", framed as a hypothesis with its test and what would kill it. Each has a new anchor.

Kept: every claim and Breaks if word for word (checker), every old anchor (verified against main), evidence folds, sources, the 18a investor-layer shape. Charts stay at four or fewer per piece. Every piece has `updated: 2026-11-06` plus an `updateNote`, which also answers the back-dating flag (the `date` field is unchanged). **Set `updated` to the real publish day when it goes live.**

## Per piece: split / choke point / analogy / new beat
| Piece | Split | Choke point | Analogy | New beat anchor |
|---|---|---|---|---|
| the-queue-not-the-chip | megawatts: booked, licensed, drawn | 2. allocation | restaurant: table booked, fire code, diners eating | #phantom-load |
| contracted-energised-running | capacity: contracted, energised, running | 3. energise | food court: lease, gas line, cook | #headroom-option |
| the-equipment-queue | the wait: build time, lead time, years of work | 3. heavy stations | hairdresser: cut, first slot, diary, second chair | #the-parts-list |
| building-your-own-power | power: plug, machine, fuel | 2. the maker's line | restaurant buys its own stove | #an-island-buys-its-own-bench |
| america-rations-the-plug | large-load rules: who is cut, who holds on, who pays | 3. upgrades | restaurant on a booked gas main | #the-hours-a-cut-first-site-can-run |
| heat-and-water | cooling: chip, building, out of the building | 5. the roof | sweat vs a fan on dry skin | #the-worst-afternoon |
| hong-kong-has-the-plug | capacity: generation, connection, chip | 4. the licence | food court, stoves from abroad | #gates-in-series |
| nuclear-for-ai | restart, uprate, new build | 3. enrichment | the cooker and its cartridges | #the-box-stops-at-five |
| powering-the-rack | 800 volts: rack, row, building | 2. the AC room | a restaurant's new ovens | #the-off-switch |
| memory-not-maths | memory: capacity, bandwidth, latency | 2. reading the weights | chef and hatch | #heat-wall |
| the-chip-supply-chain | sold out: booked, short, stuck | 4. packaging | a kitchen refit | #the-board-underneath |
| ten-thousand-chips-one-thought | the network: scale-up, scale-out, between campuses | 2. the plug | the house: wiring, bulbs, filament | #heat-decides-the-laser |
| data-centres-in-space | cooling: off the chip, across, out to the world | 5. the radiator | laptop in a vacuum flask | #heat-pump-trade |

## DECK_FINDINGS facts fixed (each checked at its primary source unless marked)
- memory-not-maths: TSMC removed everywhere. Indiana is now cleanroom Oct 2028 and mass production 2H 2029 (SK hynix, 28 Aug 2026), in text and chart. Base dies given in each maker's own words. Rubin 19.2 TB/s per the spec page.
- nuclear-for-ai: Oklo and Centrus now have a HALEU supply agreement (30 Sep 2026, conditional), and Meta's first funding went to Centrus on 2 Nov (Oklo 10-Q, filed **6 Nov**, not 4 Nov). The claim text is unchanged; a note under it cites Centrus's 4 Nov release. Aurora: the Q2 10-Q says 2028 and the Q3 10-Q says 2028-2029, both stated and not called a delay. The 6x SWU figure is labelled as my arithmetic.
- data-centres-in-space: "first weighings come in 2027" fixed. Google's prototype launched 1 Oct and downlinked 30 Oct, with no mass published.
- america-rations-the-plug: PJM shortfall is 6,623 MW (FERC ER26-3380, 29 Sep). The FERC filing is set for 16 Nov (PJM deck, 28 Oct). ERCOT peak is 91.1 GW (EIA). NERC's 26 Oct adoption and PJM's 29 Oct refiling are labelled as press.
- heat-and-water: "a Blackwell-generation rack" (Rubin in production per Nvidia's 26 Aug release). The Ypsilanti pause is added (YCUA Resolution 26-08, 22 Apr 2026). The Pinal vote was 26 Aug (press), not 7 Sep.
- contracted-energised-running: the denominator is named; "five to six times" is now exact. The three Malaysian bottoms match the Johor piece. The Bloom/Vineland power block is labelled press.
- the-equipment-queue: Eaton years of work flat at 1.049 to 1.050, and the margin gap is 0.5 pt (Q3 10-Q, 3 Nov). The Charlotte dot reads "early 2027, press report". A transformer takes months to build; the years are the queue.
- hong-kong-has-the-plug: the second gate in Beijing (Reuters 5 Nov, two sources, labelled). "Little has moved" softened to unclear. Typo fixed.
- powering-the-rack: Envision Ulanqab is live with no size (one disclosure from the claim's line). Vertiv: 2027 validation and first revenue, 2028 deployment (call transcript, labelled).
- the-chip-supply-chain: SK hynix LTAs cover over 50% of 2027 and 2028 (release). "Sold out to 2029" is labelled as press. Intel EMIB customers due within two quarters (call 29 Oct). "Only source" is narrowed to the B200, now framed as a Blackwell worked example.
- ten-thousand-chips-one-thought: Lumentum GAAP gross margin 51.0% (results **2 Nov**, not 5 Nov). Also folded in: Marvell agreed to buy Lumentum (8-K, 2 Nov), with no deal terms.
- the-queue-not-the-chip: the Bill passed on 7 Oct. The 58.5% series is traced to Hansard 5 Nov 2025 (603 of 1,276 MW declared, 47%, target 85%). 30% renewable rule (Hansard 28 Oct).

## TSMC (Tommy's decision, 6 Nov, relayed by the jobs session: "Keep it word for word")
TSMC now appears once on the whole built site: the 2 Nov claim sentence in the-chip-supply-chain's claims fold. Its Breaks if and watch list, the Ajinomoto claim's watch list, numbers.ts and the homepage descent (Descent.astro) all say "the leading foundry".

## Checks run on the branch
check-piece 13/13 clean; build clean, 229 pages; 292 HTML files, 585 internal links, 0 broken; 277 redirects land; every old anchor present; no em or en dash in /journal. check-call still fails on missing note PDFs, as it does on main, because the notes came off the site on 6 Nov. Not this branch's doing.

## Open for Tommy / next session
- Siemens Energy FY results (11 Nov) and Nebius Q3 (12 Nov) may date figures in the-equipment-queue and contracted-energised-running. Re-check before publishing if after those dates.
- Press-only items stay labelled. Do not upgrade them without a primary source.
- The Leo Cui credit in nuclear-for-ai's sources line predates this branch and is unchanged.
