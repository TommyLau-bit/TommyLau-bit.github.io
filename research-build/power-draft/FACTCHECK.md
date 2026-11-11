# Fact-check: src/data/power.ts (13 player cards), 11 Nov 2026

Method: every stat citing a piece was grepped in src/content/journal/*.md. Every NEW primary figure was fetched by me: EIA/S&L capital cost PDF, EIA AEO2026 EMM Assumptions PDF (Table 3), EIA EPM Tables 6.07.A and 6.07.B (live pages, release 23 Oct 2026), Bloom 2025 10-K and Solaris 10-Q (sec.gov, with EDGAR index dates), PA DEP Homer City Tech Review Memo PDF, PJM 2029/30 ELCC class ratings PDF (PDF metadata created 7 Aug 2026), NRC uprate page and NRC TerraPower page. All "my arithmetic" figures redone. Anchors regenerated with github-slugger from each piece's headings: all 15 anchors exist.

Verdicts per card: 9 stats + ability + weakness + makers + anchors = 13 lines x 13 cards = 169 checks.

## grid (Grid connection)
- sizeMW 389: OK. 6,608 / 17 = 388.7 (america-rations-the-plug, ERCOT to PUCT 20 Aug 2026).
- monthsToPower 12 to 48: OK (the-queue-not-the-chip: Green Lane, 8 Aug 2023, "36 to 48 months to 12, plant included"). Note: display mixes before and after; "12 months (Green Lane); 36 to 48 before" would be clearer, and since 28 Oct 2026 allocation in Malaysia is rationed, so 12 is not today's wait.
- costPerKW n/a: OK.
- capacityFactor n/a: OK ("at all times short of an emergency", america-rations line 42).
- fuelDays n/a: OK.
- permitMonths n/a: OK (FERC show cause 18 Jun 2026: "no more than 60-90 days").
- bottleneck 36 to 60 months: OK (the-equipment-queue line 82, DOE July 2024).
- fuel: OK.
- elcc n/a: OK.
- ability: OK. weakness: OK.
- makers Siemens Energy, Hitachi Energy (transformers): OK.
- anchors: OK.
- Note (not a stat): GROUPS line "It is the cheapest power there is" has no number behind it on the card (cost is n/a). Unsupported.

## heavy-sc (Heavy-frame simple cycle)
- sizeMW 430 (Siemens 440, MHI 453): OK (building-your-own-power line 311).
- monthsToPower 81 to 92: OK. Oct 2026 to Jan 2032 = 63, to Dec 2032 = 74; +18 = 81 to 92. Piece: "around 2034".
- costPerKW US$836 (2023$, 419 MW): OK. Confirmed in EIA/S&L PDF ("January 2024", 2023 dollars). Exact day 10 Jan 2024 not on the document (cover says January 2024).
- capacityFactor 13.6%: OK. EPM 6.07.A, "Natural Gas, Gas Turbine" 2025 = 13.6% (final; release 23 Oct 2026). Correctly labelled as dispatch, not availability.
- fuelDays 0: OK.
- permitMonths n/a: OK (Homer City memo covers 7HA.02 combined cycle and FT8 aeros only).
- bottleneck 122 GW, 6.1 years: OK. "about 250 GW" for three makers: piece says about 254 GW; acceptable.
- fuel 7,884 Btu/kWh, 43.3%: OK; fleet 10,975 OK.
- elcc 59%: OK. PJM PDF: "Gas Combustion Turbine 59%".
- ability: OK. weakness: OK ("we sold multiple slots for 2032 delivery").
- makers: OK. anchors: OK (equipment-queue anchor is about electrical gear, a loose fit).

## ccgt (Combined cycle)
- sizeMW 640 (655, 664; EIA 1,227): OK.
- monthsToPower 29 to 52: OK. Aug 2025 to Jan 2028 = 29; to Dec 2029 = 52. Docket U-37425, 2,262 MW in piece.
- costPerKW US$868 (2023$, 1,227 MW): OK (S&L PDF). Duke 1,620 to 2,340: OK (piece).
- capacityFactor 58.7%: OK (6.07.A "Natural Gas, Combined Cycle" 2025).
- fuelDays 0: OK.
- permitMonths 7.5: WRONG in wording, number OK. Received 4 Apr 2025, memo signed 18 Nov 2025 = 7.5 months, confirmed. But (a) the memo lists "ten (10) Mitsubishi Power FT8 ... aeroderivative gas turbines", not "up to ten"; (b) "avoided the full Clean Air Act review" is overstated: the project netted out of PSD for NOx and CO only (net -889.0 tpy NOx, -2,991.7 tpy CO); it is still a major source under PSD for PM, PM10, PM2.5, H2SO4 and GHG and subject to NNSR for VOC (369.035 t of ERCs). Source: https://files.dep.state.pa.us/regionalresources/NWRO/NWROPortalFiles/Homer-City/Air/Final-AQ-Plan-Approval/Tech%20Review%20Memo%20Signed%2020251118.pdf (18 Nov 2025). Fix: "netted out of PSD review for NOx and CO against the retired coal boilers".
- bottleneck: OK (MHI 6 Aug 2026 Q&A, 2028 to 2030).
- fuel 7,535: OK.
- elcc 75%: OK ("Gas Combined Cycle 75%").
- ability ~30% less gas: OK (7,535 vs 10,975 = 31%; piece line 49). weakness: OK.
- makers: OK. anchors: OK.

## aero (Aeroderivative)
- sizeMW 35 to 58: OK.
- monthsToPower 45 to 56: OK. Ship 2030: Oct 2026 to Jan 2030 = 39, Dec 2030 = 50; +6 = 45 to 56.
- costPerKW US$1,606 (2023$, 211 MW): OK (S&L PDF).
- capacityFactor 13.6%: OK (same class as heavy, labelled so).
- fuelDays 0: OK.
- permitMonths 7.5: WRONG in wording, same two errors as ccgt (ten FT8s, not "up to ten"; netted out of PSD for NOx/CO only).
- bottleneck 124 units, ~2.5 years: OK (124 / 50 = 2.48).
- fuel 10,975, LM6000 41.3%: OK. Note: 10,975 is the all-gas-turbine fleet average (mostly old frames), labelled as such.
- elcc 59%: OK.
- ability: OK. weakness 46%: OK (10,975 / 7,535 = 1.457).
- makers GE Vernova only: OK but incomplete. Homer City's own aeros are Mitsubishi Power FT8 MOBILEPAC (DEP memo); Siemens Energy also makes aeroderivatives. Consider adding Mitsubishi Power.
- anchors: OK.

## recip (Gas engine)
- sizeMW 18.9: OK (18,875 kW; 15 x 18.875 = 283 ≈ 282 MW).
- monthsToPower 27 to 38: OK. Oct 2026 to Jan 2029 = 27, Dec 2029 = 38.
- costPerKW 1,400 to 1,500: OK (piece: ProPetro 8-K 28 Oct 2026, US$1.4m to 1.5m per MW incl. balance of plant). The piece does not itself say "gas engines"; PROPWR's fleet is built on Caterpillar reciprocating engines (secondary report of its April 2026 8-K). Nominal builder figure vs EIA 2023$ elsewhere: see fix list.
- capacityFactor 18.0%: OK (6.07.A "Natural Gas, Internal Combustion" 2025 = 18.0%).
- fuelDays 0: OK.
- permitMonths n/a: UNVERIFIED in part. Roman's TCEQ air permit application is in solar-and-batteries (line 188); "not decided" is not in any piece or primary record I saw.
- bottleneck: OK (Wärtsilä 27 Oct 2026, no months).
- fuel 8,853, 50.0%: OK.
- elcc n/a: UNVERIFIED. PJM Manual 21B's Diesel Utility class (92% for 2029/30) is defined to include reciprocating internal combustion engines (RICE); whether gas-fired RICE fall in it, or in Gas CT, is not settled by what I read. "PJM publishes no ELCC class for this machine" may be wrong. Check Manual 21B s2.4 / RAA Schedule 9.2 (https://www.pjm.com/-/media/DotCom/committees-groups/committees/pc/2026/20261006/20261006-item-05-b---3-manual-21b-periodic-review---redline.pdf).
- ability (two minutes): OK. weakness: OK.
- makers Wärtsilä, Caterpillar: OK. anchors: OK.

## fuelcell (Bloom)
- sizeMW 10: OK. EMM Table 3, "Fuel cells 2028 10 3 $7,818 1.06 $8,287 ... 6,469" (AEO2026, April 2026).
- monthsToPower 3: OK. 10-K: "In certain project scopes, onsite generation can enable power availability within approximately 90 days"; "subject to permitting and site conditions" is also in the 10-K. Filed 9 Feb 2026 (EDGAR). EIA lead time 3 years: OK. Labelled as company claim: good.
- costPerKW US$7,818 (2025$): OK, total with optimism factor US$8,287 OK.
- capacityFactor n/a: OK (6.07.A has no fuel cell column).
- fuelDays 0: OK.
- permitMonths n/a: OK (10-K: NY, NJ, NC "specific air permitting exemptions for fuel cells"; "permitting process will be lengthened").
- bottleneck 2 GW: OK ("from 1 gigawatt to 2 gigawatts by the end of 2026"); Oracle 2.8 GW in piece.
- fuel 6,469: OK.
- elcc n/a: OK (PJM list has no fuel cell class).
- ability: OK. weakness "highest gas machine here": OK, though it compares 2025$ with 2023$.
- makers: OK. anchors: OK.

## fleet (Rented fleet, Solaris)
- sizeMW ~29: OK. 10-Q: "secured seven turbines from private parties for approximately $163.0 million in cash ... over 200 MW ... beginning in the first quarter of 2027". 200 / 7 = 28.6. Filed 6 Nov 2026 (EDGAR).
- monthsToPower 2 to 14: WRONG (minor). Nov 2026 to Jan 2027 = 2; to Dec 2027 = 13 by the month-count method every other card uses. Should be 2 to 13. (The 10-Q's "beginning in the first quarter of 2027" is the better anchor: 2 to 4 months for those seven units.)
- costPerKW n/a: UNVERIFIED wording. The 10-Q says the turbines were "secured ... from private parties"; it does not say "second-hand". Use "from private parties".
- capacityFactor n/a: OK. fuelDays 0: OK. permitMonths n/a: OK.
- bottleneck 3.2 GW: OK (piece line 158, release 4 Nov 2026).
- fuel: OK. elcc 59%: OK.
- ability "due to run from early 2027": OK (Q1 2027). weakness: OK.
- makers Solaris, ProPetro: OK (piece line 361: "rent power fleets"; operators, not makers). anchors: OK.

## solar
- sizeMW 150 MWac: OK (S&L Case 16). Quantum 640 MW: OK.
- monthsToPower 24: OK (EMM Table 3 lead time 2 years).
- costPerKW US$1,502 (2023$): OK (S&L table: "Tracking 150 MWAC 150 N/A $1,502").
- capacityFactor 24.0 / 13.1 / 31.9: OK (6.07.B confirmed).
- fuelDays: OK.
- permitMonths n/a: UNVERIFIED parenthesis. "LBNL Queued Up 2026, 61-month median for generators built in 2025" is not in any piece (the piece cites the 2025 edition, 55 months for 2024) and I did not find it. Drop or source it.
- bottleneck 14 MW per firm MW: OK (1 / 0.07 = 14.3; piece line 91).
- fuel: OK.
- elcc 7% (fixed 6%, 14% in 2025/26): OK (PJM PDF; operators.md; piece line 82).
- ability, weakness: OK.
- makers "Intersect Power (developer)": OK as labelled. anchors: OK.

## battery
- sizeMW 150 MW / 600 MWh: OK (S&L Case 19).
- monthsToPower 12: OK (EMM Table 3 lead time 1 year).
- costPerKW US$1,744 (US$436/kWh): OK (S&L).
- capacityFactor n/a: OK. fuelDays 0.167: OK.
- permitMonths n/a: OK.
- bottleneck 23% by 2035/36: OK (piece line 101, preliminary 4 Sep 2026).
- fuel: OK. elcc 57% (42, 23, 19): OK (PJM PDF; piece).
- ability, weakness: OK. makers: OK as labelled. anchors: OK.

## restart
- sizeMW 615 to 835: OK (nuclear-for-ai line 47).
- monthsToPower 34 to 39: OK. Sep 2024 to Jul 2027 = 34, Dec 2027 = 39.
- costPerKW ~US$1,900: headline OK (1.6bn / 835 MW). WRONG in basis: "Palisades about US$2,800" cannot be derived from the piece: DOE loan up to US$1.52bn plus Michigan US$300m = US$1.82bn / 800 MW ≈ US$2,275 (loan alone ≈ US$1,900). Duane Arnold US$1.9bn / 615 ≈ US$3,090: OK. Source label "Constellation (FERC filing)" is not what the piece says ("Constellation says it has invested"); unverified label.
- capacityFactor 91.1%: OK (6.07.B).
- fuelDays 548 to 730: OK (18 x 30.4 = 547.2, so 547; trivial).
- permitMonths ~30 (Crane ~28): OK. 1 Feb 2023 to 24 Jul 2025 = 29.8; Nov 2024 to 4 Mar 2027 = 28.
- bottleneck: OK. fuel: OK. elcc 96%: OK ("Nuclear 96%").
- ability, weakness: OK. makers (owners): OK. anchors: OK.

## uprate
- sizeMW ~78: OK. 2,421 / 31 = 78.1; 8,030 / 172 = 46.7.
- monthsToPower up to 26 (target): OK. Oct 2026 to Dec 2028 = 26. Labelled as target: good.
- costPerKW ~US$4,800 (Byron/Braidwood 5,100): OK.
- capacityFactor 91.1%: OK. fuelDays: OK.
- permitMonths 6 to 12: OK. NRC page (updated 29 Oct 2026) cites the 7 May 2024 letter: 12 months extended, 9 stretch, 6 MUR. Labelled as targets: good. The clause "the acceptance review is extra" is not on that page: unverified clause.
- bottleneck "None filed yet": OK (piece: pending list empty 15 Sep 2026).
- fuel, elcc: OK. ability, weakness: OK. makers (owners): OK. anchors: OK.

## newreactor
- sizeMW 50 to 345: OK.
- monthsToPower 46 to 57: OK. Mar 2026 to Jan 2030 = 46, Dec 2030 = 57. Note: 4 Mar 2026 is the Commission's vote (and the NRC hearing); permit CPAR-1 was issued 9 Mar 2026 (NRC page "Construction Permit Decision 03/09/2026"). The months do not change.
- costPerKW ~US$9,800: OK (piece line 325). Note it is an AP1000 on ordinary fuel, on a HALEU card; the basis says so.
- capacityFactor n/a, fuelDays n/a: OK.
- permitMonths ~23: OK. NRC page: submitted 28 Mar 2024, permit decision 9 Mar 2026 = 23.4 months.
- bottleneck: OK (>40 t by 2030; 21.2 t by 2028; sixteen machines).
- fuel HALEU: OK. elcc n/a: OK.
- ability: OK.
- weakness: WRONG wording. "against about 21 in stock": the DOE figure is a stock expected to reach about 21.2 t by 2028 (GAO-26-107385, 20 Aug 2026), not stock held now. Fix: "against about 21 tonnes expected by 2028".
- makers: WRONG. "GE Vernova Hitachi" makes the BWRX-300, which burns ordinary fuel (nuclear-for-ai line 190); the card's examples and fuel line are HALEU reactors only. Remove it, or broaden the card's fuel line.
- anchors: OK.

## micro
- sizeMW 1 to 20 (Kaleidos 1, Pele 1.5, BANR 20): OK.
- monthsToPower ~25 (target): OK. 26 Aug 2026 to Sep 2028 = 25.
- costPerKW n/a: OK (INL US$325/MWh FOAK; 12 to 15 cents mass-produced).
- capacityFactor n/a: OK. fuelDays 1,096 to 2,922: OK (x 365.25).
- permitMonths n/a: OK (proposed May 2026 rule, 6 to 12 months).
- bottleneck 0.7 t: OK. fuel: OK. elcc: OK.
- ability: OK. weakness 32.5 vs 8.6: OK.
- makers: OK (microreactors piece line 229). anchors: OK.

## House rules
- No em or en dashes in card text (only the file's comment rule line). OK.
- No share prices, valuations or views on shares. OK.
- British spelling (modelling, programme, refuelling, per cent). OK.

## Tally
OK 159, WRONG 6, UNVERIFIED 4 (of 169 checks).

## Required fixes, most serious first
1. ccgt and aero permitMonths basis: replace "avoided the full Clean Air Act review" with "netted out of PSD review for NOx and CO against the retired coal boilers" (it stayed under PSD for PM and GHG and NNSR for VOC), and "up to ten aeroderivatives" with "ten Mitsubishi FT8 aeroderivatives" (DEP memo, 18 Nov 2025).
2. newreactor makers: remove "GE Vernova Hitachi" (BWRX-300 burns ordinary fuel; the card is HALEU-only).
3. newreactor weakness: "about 21 in stock" -> "about 21 tonnes expected by 2028".
4. restart costPerKW basis: Palisades "about US$2,800" is not supported; the piece's figures give about US$2,275 (US$1.52bn DOE loan ceiling + US$300m Michigan over 800 MW), or drop it. Source label "FERC filing" -> "Constellation, as cited in the piece".
5. Cost comparability (affects ratings): costPerKW mixes EIA 2023$ (S&L), EIA 2025$ (fuel cell) and nominal builder figures (engines, nuclear). For the EIA-based cards, consider one basis: AEO2026 EMM Table 3, 2025$: frame CT US$1,158, aero US$2,275, CC multi-shaft US$1,032, fuel cell US$7,818, solar US$1,484, battery US$1,521.
6. fleet monthsToPower: 2 to 14 -> 2 to 13 (same month-count as other cards), or anchor on the 10-Q's first-quarter 2027 start.
7. fleet costPerKW basis: "second-hand turbines" -> "turbines secured from private parties" (10-Q wording).
8. recip elcc: PJM's Diesel Utility class (92%) is defined to include RICE; confirm in Manual 21B whether gas engines are classed before saying "no ELCC class".
9. solar permitMonths: remove or source the "Queued Up 2026, 61-month median" parenthesis.
10. Smaller: recip permit "not decided" unsourced; uprate "acceptance review is extra" not on the NRC page; GROUPS grid line "cheapest power there is" has no number behind it; newreactor date could read "approved 4 March, issued 9 March 2026"; grid months display could separate Green Lane (12) from before (36 to 48).


## Potential (EIA-860M, September 2026), checked 11 Nov 2026 by an independent agent

File september_generator2026.xlsx re-downloaded, sha256 matched; latest release (23 Oct 2026, next 24 Nov). Recomputed from scratch: combined cycle 47,146.2 MW OK; gas GT >=100 MW 16,645.6 and <100 MW 6,349.7 OK (gas only; two petroleum GT units of 114 MW excluded); gas IC 952.0 OK (gas only); fuel cells planned 0, operating 373.8 MW OK; solar 122,025.2 OK; batteries 64,234.6 OK; planned nuclear 4,968.0 OK (Kemmerer 500 L; four Matador 1,117 P); restarts Palisades 811.8 (OA) and Crane 980.8 (OS) = 1,792.6 OK, but the file has no "return date" column (dates are in Other Modification): wording fixed; uprates 13 units 1,048.7 MW summer OK; no rental figure in this file OK. The 100 MW heavy/aero split is a proxy, labelled as such.


## Filled gaps, checked 11 Nov 2026 by an independent agent

TNB Connection Charges Book 2025 Table 7 figures OK (worked example, not a real project); rate fixed from RM4.2 to about RM4.07 (Bank Negara, 11 Nov 2026), so about US$505/kW, shown as about US$500. EIA EPA Table 11.1 OK (2025 SAIDI 269.2 with major events, 99.949%). PJM 2029/30 ELCC OK: Diesel Utility 92%, Nuclear 96%, Gas CT 59%, Gas CC 75%; Manual 21B puts RICE in Diesel technology type (wording now "under PJM's rules"). Bloom 10-K 99.9% fleet availability verbatim OK; fuel cells sit in PJM's Other Unlimited Resource Class (wording fixed). Solaris 10-Q US$163.0m, over 200 MW, so at most US$815/kW OK (turbine price only, wording fixed). TerraPower Natrium refuelling every 24 months verbatim OK; Oklo 10 years UNVERIFIED at primary level, kept as Oklo's own target; Kairos online refuelling attributed to Kairos. INL microreactor OCC 23,592 FOAK / 10,825 NOAK OK (6.2 MWe, excludes fuel; noted).


## Grid speed (Dominion), checked 12 Nov 2026 by an independent agent

Dominion to PJM LAS (29 Sep 2026) slide 5 "Non-firm load - includes load from ELOAs (2032 and beyond)" OK; ramp "5 years maturing at a utilization rate of 63%" OK and is a ramp after energisation, not a wait; slide 6 32,473 MW ELOAs, 19,044 MW not in forecast (59%) OK. GS-5 report (May 2026) p.2: energisation dates to 25 GW "between now and 2031", 45 GW with no dates yet OK. "At least 5 to 6 years from a 2026 request" is a fair floor but our inference, not a Dominion figure: wording says so. Replaces Johor's 12 to 48 months as the grid's Speed (grade C to E): Tommy, 12 Nov, asked why build your own if the grid only rated C.
