# Sidecar: malaysia-keeps-the-wires-shared (draft, 29 Oct 2026; reframed after fact-check)

Old slug malaysia-sends-data-centres-the-bill is retired; all three files renamed.
Title: "Malaysia charges its data centres more for power, but the wires stay on the shared bill"
Shape: Analysis. Subject: Tenaga Nasional's tariff for data centres, set by the Energy Commission under Regulatory Period 4.
Body: 498 words. Checker: 0 failures, 0 warnings.

## What the fact-check changed
- The original claim ("Malaysia sends the grid bill to data centres, not households") does not hold. The high voltage ultra class raises only the energy charge (55.18 / 51.09 sen, 24.0% and 26.4% above HV ToU); its capacity (RM21.76/kW) and network (RM23.06/kW) charges equal ordinary HV ToU. The connected load charge is a penalty of RM8.50/kW of shortfall below 85% of phased declared MD (years 1 to 4; 75% in years 5 and 6), about a fifth of the RM44.82/kW full capacity plus network rate, and applies to all new MV/HV customers since 2021. TNB's RM16.27bn contingent capex, partly for data centres with signed ESAs, earns the same 7.3% return and is recovered through the shared regulated tariff.
- So the honest claim is the reverse framing: data centres pay more per unit and a penalty on idle bookings, but the wires built for them stay in the shared tariff base. It still builds on pjm-sends-the-bill (there a market price spreads the cost; here a regulator's tariff design does, and could stop doing so at a reset).

## Proposed claim (one sentence)
Malaysia charges its data centres more for each unit of electricity, but the wires built for them stay in the shared regulated tariff, and I expect the tariff for the period from 1 January 2028 to keep their capacity and network charges level with ordinary high voltage users.

Alternatives considered:
1. "The household network charge (12.85 sen/kWh) will rise in the period from 1 Jan 2028 because of data centre grid spending." Rejected as the main test: household charges can move for many reasons and are partly set by subsidy, so attribution would be arguable.
2. "Malaysia's data centres draw about a fifth of the demand connected for them." True and useful, but evidence, not a claim.
Chosen because the wires line is directly observable in the next published schedule, and ministers' own "user pays" statements make it a genuine risk to the claim.

## Proposed claims.ts entry
```ts
  {
    id: 'malaysia-keeps-the-wires-shared',
    claim: 'Malaysia charges its data centres more for each unit of electricity, but the wires built for them stay in the shared regulated tariff, and the tariff for the period from 1 January 2028 will keep their capacity and network charges level with ordinary high voltage users.',
    breaksIf: 'The tariff for the regulatory period starting 1 January 2028 gives data centres capacity or network charges above ordinary high voltage users, or bills the grid built for each campus to its developer rather than recovering it through the shared tariff.',
    watch: ['The Energy Commission tariff schedule from 1 January 2028', 'High voltage ultra capacity and network charges against ordinary high voltage, RM21.76 and RM23.06 per kW from July 2025', 'Whether data centre grid capex stays in Tenaga\'s regulated allowance', 'The household network charge, 12.85 sen per kWh from July 2025', 'Tenaga data centre load against maximum demand connected, 1.26 GW against 5.65 GW in June 2026'],
  },
```

## Map layer (stack.ts)
'grid' (The grid connection), next to pjm-sends-the-bill and two-governments-one-confession.

## Glossary
- "Connected load charge", Getting power to the building: "In Malaysia, a penalty on a large new customer that uses less than a set share of the maximum demand it declared, 85 per cent for the first four years, charged on each kilowatt of shortfall."
- "Maximum demand", Getting power to the building (if absent): "The most power a customer draws at once, in kilowatts or megawatts. Large customers pay capacity and network charges on it, because the wires must be sized for it."
- "High voltage ultra tariff", Getting power to the building: "Malaysia's tariff class, from 1 July 2025, for data centres supplied above 50 kilovolts. Its energy charge is higher than ordinary high voltage users pay; its wires charges are the same."

## numbers.ts (physical only)
{ layer: 'grid', value: '1.26 GW of 5.65 GW', what: 'Data centre load Tenaga Nasional supplied in June 2026, against the total maximum demand of data centre projects connected in Peninsular Malaysia.', piece: 'malaysia-keeps-the-wires-shared', asOf: 'June 2026' }

## LinkedIn post (§9)
Malaysia charges its data centres a quarter more for each unit of electricity, but not a sen more for the wires.

Since July 2025 data centres have had their own tariff class, and a penalty if they leave booked power unused. The grid built for them still sits in the tariff everyone shares, and in June they drew about a fifth of the demand connected for them. Whether that stays shared is decided at the next reset, in January 2028.

The piece covers how the bill is split, where the wires end up, and what would prove me wrong.

https://thephysicallayer.fyi/journal/malaysia-keeps-the-wires-shared/

#DataCentres #Grid #Malaysia

## Figures used in the body, with primary source
- 1 July 2025, high voltage ultra class; energy charge about a quarter above ordinary HV: Energy Commission, Jadual Tarif Elektrik di Semenanjung Bagi Tempoh 1 Julai 2025 Hingga 31 Disember 2027, https://myenergystats.st.gov.my/documents/d/guest/jadual-tarif-tnb-terkini (read 29 Oct 2026).
- Applies to data centres above 50 kV: government written reply (Fadillah Yusof) as reported by The Star, 20 Oct 2026, https://www.thestar.com.my/news/nation/2026/10/20/123gw-energy-capacity-approved-for-data-centres-as-of-august-parliament-told and 21 Oct 2026, https://www.thestar.com.my/news/nation/2026/10/21/data-centres-to-bear-costs . PRESS-REPORTED (Hansard not checked); the tariff schedule itself is primary.
- 85 per cent of phased declared MD, four years; penalty RM8.50/kW of shortfall vs RM21.76 + RM23.06 = RM44.82/kW UHV capacity plus network, so about a fifth: TNB, Connected Load Charge, https://www.tnb.com.my/commercial-industrial/charges-penalties (read 29 Oct 2026). "Government says it has raised it for data centres": same Star reports, PRESS-REPORTED.
- 1.26 GW drawn in June 2026, 5.65 GW total maximum demand in system for 42 projects (not the phased amount the CLC applies to; total secured is 8.35 GW across 61 projects): TNB Analyst Briefing 2QFY2026, 28 Aug 2026, p.3 to 4, https://www.tnb.com.my/assets/quarterly_results/Analyst_Briefing_-_2QFY2026.pdf
- DROPPED after fact-check: Liew Chin Tong quote (EdgeProp, 5 Nov 2025). It concerned revising projected capacity to cut stranded-asset risk and "cost transfers to other consumers", not tightening the rules. https://www.edgeprop.my/content/1914317/data-centres-consume-only-about-half-declared-power-capacity-govt-flags-potential-risk-stranded-assets
- RM16.3 billion contingent capex, partly for data centres with signed ESAs, same 7.3% return: TNB Investor Deck, October 2026, p.6, https://www.tnb.com.my/assets/conference_materials/TNB_Investor_Deck_Oct_2026.pdf (the only company financial figure in the piece).
- "Ministers say data centres should bear the grid costs they cause": Fadillah's cost-causation reply (The Star, 21 Oct 2026) and Johari, 15 Oct 2026 (investors to bear transmission upgrade costs), PRESS-REPORTED.
- 2027 tariff review (context only, no longer in body): Fadillah Yusof, Dewan Rakyat, as reported by The Sun, Oct 2026, https://thesun.my/news/govt-reviews-electricity-tariffs-for-2027-with-data-centres-in-focus/ . PRESS-REPORTED. RP4 schedule ends 31 Dec 2027 (Energy Commission schedule; ST media statement 20 Jun 2025, https://www.st.gov.my/jadual-elektrik-baharu-lebih-236-juta-pengguna-domestik-semenanjung-nikmati-kadar-lebih-adil), so the next period starts 1 Jan 2028.

## Other sources read (context, not in body)
- PETRA media statements, 20 Dec 2024 (RP4 base tariff approved; RM3,570m government cost of new schedule) https://www.st.gov.my/sites/default/files/2026-02/KM-bil63-ICPT-IBR-SEMENANJUNG-DISEMBER-2024.pdf and 27 Dec 2024 (85% of domestic users at 1,500 kWh and below unaffected; large commercial and industrial users to pay real cost) https://www.petra.gov.my/uploads/content-downloads/file_20241230082123.pdf
- Johari Abdul Ghani, Dewan Rakyat, 15 Oct 2026: DC operators pay for reserved capacity used or not; investors to bear transmission upgrade costs; no subsidy; DC supply kept separate from households. The Star https://www.thestar.com.my/news/nation/2026/10/15/data-centres-must-pay-for-unused-power-allocations-says-johari and EdgeProp https://www.edgeprop.my/content/1917859/data-centre-investors-must-fund-grid-upgrades-says-johari . PRESS-REPORTED. Not used in the body to keep the figure count down; strong support for a later update.
- The Edge, Digital Edge, 29 Dec 2025 to 4 Jan 2026, https://theedgemalaysia.com/node/786977 (ESA declared demand, CLC, shortfall charge).
- The Star, 28 May 2026 (TNB chief grid officer Hasmarizal Hassan, RM43bn grid modernisation, Johor cluster), https://www.thestar.com.my/business/business-news/2026/05/28/tnbs-rm43bil-grid-modernisation-gears-up-for-rapid-growth-in-data-centre-demand
- dcmarketinsights.com summary of the Oct 2026 statements (secondary, used only as a pointer to primaries).

## Video figures dropped or flagged (CNA Insider, "Who Will Be Prioritised?": The Dilemma Of Malaysia's AI Push, https://www.youtube.com/watch?v=H39gck73WCQ)
- "US$10.57 billion grid modernisation programme" (May 2026): FLAGGED and dropped. TNB states it in ringgit: RP4 allowed capex RM26.55bn base plus RM16.27bn contingent = RM42.82bn for 2025 to 2027 (Investor Deck Oct 2026, p.6), described by TNB's chief grid officer as "RM43 billion" (The Star, 28 May 2026). The US$ figure is a third-party conversion at about 4.05 RM/USD; at RP4's own forex assumption of 4.307 it would be about US$9.9bn. TNB gives no US$ figure. Only the contingent RM16.3bn is used.
- "Johor has a tiered pricing plan where large industrial users bear a greater share; data centres charged at different rates": the federal UHV class is the verified version; no Johor state tier was verified, dropped.
- "Residents will not face higher electricity bills": a government assurance; not used as fact, it is what the falsifier tests.
- 144bn / ~200bn ringgit investment applications, 3 to 5bn US$ GDP, 300 MW data centre = two cities of 300,000, 0.0039 W per prompt, 20 million litres a day, US$1.1bn Johor water plan, 41% water capacity, 65 approved projects, 13% of global ATP: out of scope or unverified, all dropped.

## Notes for publish
- Brief asked to check the Corridor for Renewable Energy / green tariff: Malaysia's live scheme is CRESS (Corporate Renewable Energy Supply Scheme); the Oct 2026 reply says data centres must source at least 30% renewable energy via CRESS or self-consumption solar. Not in the piece (second angle).
- No banned company names. No share prices or views. No em or en dashes in piece, cover or this file.

## Re-check, 29 Oct 2026 (primary sources): HOLD
Verdict: HOLD. Primary sources now cover the press-only definitions, but they undercut the reversed claim itself.

Definitions now primary:
- UHV applies to data centres at high and extra high voltage: Dewan Negara Hansard, 8 Dec 2025 (Deputy Minister Akmal Nasrullah, oral answer: "pengguna pusat data baharu dan sedia ada yang disambungkan pada voltan tinggi dan voltan amat tinggi"), https://www.parlimen.gov.my/files/hindex/pdf/DN-08122025.pdf ; TNB 36th AGM Q&A, Appendix C, p.3 ("Data centre customers are categorised under the Ultra High Voltage (UHV) tariff segment"), https://www.tnb.com.my/assets/energy_watch/AGM_Presentation_2026_Appendix_C.pdf
- High voltage = above 50 kV up to 230 kV, extra high voltage above 230 kV: TNB Connection Charge Book 2025, section 3, https://www.tnb.com.my/assets/files/TNB_Connection_Charges_Book_2025_ENG.pdf . Together with the Hansard, "above 50 kV" is now primary.
- Tariff review: Dewan Rakyat Hansard, 15 Oct 2026, pp.5 to 6 (Fadillah Yusof, oral answer): ST to study a "user-pay basis" next year, naming data centres; the fifth IBR period is set in 2027 for 2028 to 2032 (five years, not three), https://www.parlimen.gov.my/files/hindex/pdf/DR-15102026.pdf
- Newer load figure: Dewan Rakyat Hansard, 13 Oct 2026, pp.31 to 32: 62 data centres with ESAs, 8.771 GW maximum load; 45 operating at 6 GW maximum load; actual use about 1.37 GW, August 2026, https://www.parlimen.gov.my/files/hindex/pdf/DR-13102026.pdf

Still press-only: a raised connected load charge for data centres. TNB's book shows one RM8.50/kW rate for all MV and HV customers, no data centre rate. The Fadillah written reply (The Star, 20 and 21 Oct) was not found on parlimen.gov.my (the written-answer index is dynamic); the oral Hansard above covers the review.

Why HOLD (claim fails test 2 on primary evidence):
- TNB Connection Charge Book 2025, section 3.3 and Table 7: a high voltage customer pays a load charge equal to the project cost less the present value of 15 years of its own tariff margin at 7.3% WACC; if that is zero it posts a refundable 25% of project cost, forfeited below 75% of final MD within 6 years; plus a Project Minimum Monthly Charge of 2% of net capital cost for 5 years, and land for any transmission intake (PMU). So the wires built for each campus are already billed to the developer where its revenue does not cover them. The piece's falsifier ("bills the wires built for each campus to its developer") is the current rule, and the body line "the wires built for them stay on the shared bill" is wrong for connection assets.
- The government's primary position (DN Hansard 8 Dec 2025) is that the UHV class is the user-pays mechanism. Under a pooled revenue requirement, extra revenue on the energy line offsets the shared pool too, so "premium on energy, not wires" is a labelling point.
- Test 1: a distinct counterpart to pjm-sends-the-bill only if rebuilt. Test 3: as drafted, a PM would be misled.
- What survives: shared reinforcement (the RM16.3bn contingent capex) is pooled; the connection is not. A possible rebuild, for Tommy to decide: "Malaysia makes each data centre fund its own connection through a 15-year revenue test, and its higher energy rate shrinks that bill; the deeper grid stays pooled until RP5 (2028 to 2032)." New claim, not drafted.

Piece not changed (still draft: true); checker and build not rerun.
