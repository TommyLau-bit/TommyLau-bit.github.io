# Gap scout: can Singapore and Johor data centres build their own power behind the meter?

Scouted 30 Oct 2026. Lead: SemiAnalysis's free framing that US labs escape the grid queue with on-site gas (a lead only). Hypothesis from an earlier scout tested below.

## Verdict in one line

UPDATE to the-queue-not-the-chip (new section after "Singapore's old halls", plus one line in "Malaysia's bill"), not a new deep piece. Behind-the-meter power is legal in Singapore but does not get a campus round the ration, because Singapore rations IT load (the DC call and the hall licence), not the grid plug. Malaysia's government says it wants data centres to self-generate, but its own words steer them to solar with no export, plus backup generators usable for demand control. The earlier hypothesis that gas import capacity is the cap is wrong for one campus.

## Singapore: the law allows it (PRIMARY)

1. EMA, Information Guide for Embedded Generation, February 2014 (PDF metadata: modified 11 Aug 2023). https://www.ema.gov.sg/content/dam/corporate/licences/content-files/EMA-Industry-Licences-Info-Guide-for-Embedded-Generators.pdf PRIMARY
   - s1.1: embedded generation "refers to the onsite generation and supply of electricity primarily for internal use"; a consumer with EG "is allowed to connect his load facilities to the power grid for additional and/or backup electricity supply".
   - s2.1 conditions: units on land contiguous to the load; units, load and land at least 50% owned by the same consumer; non-contiguous land allowed with a dedicated point-to-point connection; may be outsourced to a third party "provided that such outsourcing does not create market power or add to the existing market power of the third party".
   - s4.2.1: unit capacity 1 MW to under 10 MW needs a Wholesaler (Generation) Licence; 10 MW or more needs a Generation Licence. Table 6: 1 to 10 MW not grid-connected is exempted; the text extraction of the 10 MW row for an islanded unit is garbled (reads as Generation Licence either way, not certain). An Electrical Installation Licence is needed regardless.
   - s5.2: 10 MW or more aggregate at one station must register as a generation registered facility, "subject to dispatch by PSO"; s5.4 on-site quantities are declared ex ante and treated as must-run.
   - s3.2.2: net treatment of market charges only if the consumer uses at least 50% of its output annually.
2. EMA FAQ "Which licence should I apply for if I wish to generate electricity" (ema.gov.sg; Incapsula blocked direct fetch, NOT bypassed). Search snippet shows the same tiers: below 1 MW exempted; 1 to under 10 MW Wholesaler Licence; 10 MW or more Generation Licence. Treat as corroboration only.
3. EMA, Final Determination, Emission Standards Framework for Power Generation Units, 26 Oct 2023. https://www.ema.gov.sg/content/dam/corporate/partnerships/consultations/emissions-standards-for-power-generation-units/decision/EMA-Consultations-Final-Determination-Emission-Standards-for-Power-Generation-Units-20231026.pdf.coredownload.pdf PRIMARY
   - s3.14: "New and repowered fossil fuel-fired embedded generation (EG) units with generation licences will be required to be at least 30% hydrogen-ready or start combusting low-carbon fuels at the point of commissioning".
   - s3.15: EGs "will not be subject to an emission intensity limit" (grid plants: 0.355 tCO2e/MWh, s3.3).
   - s3.17(ii): standby units "installed solely for buildings' own backup purposes" are exempt.
4. EMA RFP to Build, Own and Operate New Generation Capacity 2026, version 4, issued 8 Sep 2026. https://www.ema.gov.sg/content/dam/corporate/partnerships/proposals/request-for-proposal-to-build-own-and-operate-new-generation-capacity-2026/EMA-Calls-for-Proposals-Version-4-RFP-to-Build-Operate-New-Generation-Capacity-2026.pdf.coredownload.pdf PRIMARY
   - s1.1: EMA "coordinates the orderly planting of new generation capacity in Singapore via the Centralised Process".
   - Table 1b footnote: projected generation includes "consumers with own / embedded generation".
   - Annex C: gas connection via PowerGas; customer must "Appoint a Shipper to submit application for connection"; isolation valve land handed over at least 21 months before gas-in.
   - Reserve margin floor 27% (footnote 6). Each unit at least 600 MW (s2.1).
   - Tracked-change text shows upper-bound 2031 peak demand of 13.0 GW (and 11.4 GW); the 26 Oct release uses 9.9 to 13 GW, the 29 Apr release 9.6 to 11.4 GW. So EMA's upper bound for 2031 rose between April and October 2026 (my reading of the two releases; the PDF shows both figures).

## Singapore: the gas side (PRIMARY)

5. EMA media release, Five-Year Energy Infrastructure Plan, 26 Oct 2026. https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2026/20262610-EMA-Media-Release-Five-Year-Energy-Infra-Plan-to-Meet-Unprecedented-Future-Demand.pdf.coredownload.pdf PRIMARY
   - Peak demand 8.6 GW at August 2026; 9.9 to 13 GW by 2031, "mainly" from semiconductors, data centres and electric transport.
   - Five new gas plants 2026 to 2031, capacity up about 26% from about 12 GW; RFP closed September 2026 for plants by 2032; more RFPs possible.
   - Gas about 95% of electricity. LNG regasification "from 10 million tonnes per annum (Mtpa) to 15 Mtpa when the second LNG terminal at Jurong Port is operational by 2030"; expansion of the first terminal studied.
   - Grid spend up to S$5.3bn 2025 to 2029, 11 times the previous five years; seven new transmission substations by 2031. Second Malaysia interconnector up to 2 GW by 2030 under study (existing link 1 GW). Pulau Tekong energy cluster feasibility.
6. EMA media release, RFP launch, 29 Apr 2026. PRIMARY. 2031 unit and up to two 2032 units, each at least 600 MW, hydrogen-ready CCGT; bids 24 Jun 2026 (2031) and 30 Sep 2026 (2032); peak 9.6 to 11.4 GW by 2031.
7. EMA media release, award to Tuas Power, 20 Aug 2026. PRIMARY. 670 MW CCGT by December 2031. Annex: Keppel Sakra 600 MW (2026, operating), Sembcorp 600 MW (2026), YTL PowerSeraya 600 MW (2027), PacificLight 670 MW (2029), Tuas Power at least 600 MW (2031).
8. EMA media factsheet, Centralising Gas Procurement, 23 Oct 2023. PRIMARY. Gasco to centralise procurement "for the power sector"; applies "to all future gas demand from the power sector"; "Other industrial gas customers can continue to procure gas through licensed gas importers and will not be subject to this central procurement framework." Whether a data centre's embedded generator counts as power sector or industrial customer: NOT FOUND.
9. SLNG, terminal overview page (fetched 30 Oct 2026). https://www.slng.com.sg/slng-terminal-overview PRIMARY (company). "annualised average gas supply capacity of 10 Mtpa"; three 180,000 m3 tanks and one 260,000 m3; supplies about half of gas for power, pipeline the rest; capacity to meet all power generation needs at current demand.
10. My arithmetic (label as such): a 100 MW campus on its own CCGT at about 50% efficiency burns about 200 MW thermal, about 6.3 PJ a year, about 0.13 Mt of LNG at 48 GJ/t: about 1.3% of SLNG's 10 Mtpa. So regas capacity is not the cap for one campus; it is a system cap.

## Singapore: what the ration actually gates (PRIMARY, already in the queue piece)

11. Digital Infrastructure Bill No. 20 of 2026, clauses 2, 23, 26(2), 35, 39(2)(b), 40 (as cited in the-queue-not-the-chip): licence for any hall of 3 MW or more critical IT load, licence states the critical IT load, regulator can cut it. Own power does not raise a licensed IT load.
12. EDB and IMDA DC-CFA2 (1 Dec 2025; awards 21 Aug 2026), as cited in the queue piece: capacity allocated in MW with PUE 1.25 and 50% green conditions.
13. EDB/JTC, Jurong Island data centre park, 27 Oct 2025. https://www.edb.gov.sg/en/business-insights/insights/jurong-island-to-host-singapores-largest-green-data-centre-park-10-per-cent-of-land-set-aside-for-new-energies.html PRIMARY. About 20 ha, up to 700 MW; "Operators can leverage the island's ecosystem, such as shared energy storage infrastructure and utilities"; no on-site generation for the park mentioned.

Leads only (SECONDARY): DayOne's first Singapore site said to carry on-site solid oxide fuel cells (company-linked press); Bridge Data Centres and PacificLight MoU for power from the 2029 plant (a supply deal, not behind the meter); Keppel DC floating park and LNG-to-power studies (exploration). None verified at primary.

## Indonesia piped gas cut (PRIMARY, ESDM confirms)

14. ESDM, "Pangkas Ekspor Gas 8 Persen, Bahlil: Tak Ada Kontrak yang Dilanggar", 26 Oct 2026. https://www.esdm.go.id/id/media-center/arsip-berita/pangkas-ekspor-gas-8-persen-bahlil-tak-ada-kontrak-yang-dilanggar PRIMARY
   - Total piped exports from Natuna and Sumatra 409.55 BBTUD; 31 BBTUD cut; "about 8%"; within the contract minimum ("kita baru sekitar 8%, terkecuali kita potong 10%, nah itu baru kita melanggar kontrak").
   - Reason: maintenance shutdowns at some wells, priority to PLN and domestic industry. No end date given.
   - SKK Migas's own release not reached (skkmigas.go.id behind a Cloudflare check, not bypassed). Press quotes SKK Migas: 15 BBTUD Natuna, 16 BBTUD Sumatra, from 24 Oct, 18 days (SECONDARY, not confirmed).
   - EMA's "under 2% of daily gas demand" is press-reported only (SECONDARY); no ema.gov.sg statement found.

## Malaysia and Johor (PRIMARY)

15. Dewan Rakyat Hansard, 28 Oct 2026 (DR-28102026), oral answer by Deputy Prime Minister Fadillah Yusof to Machang, pp. 7 to 9. https://www.parlimen.gov.my/files/hindex/pdf/DR-28102026.pdf PRIMARY
   - Data centres "digalakkan untuk membangunkan kemudahan penjanaan sendiri (self-generation) melalui inisiatif solar for self-consumption ... tanpa mengeksport lebihan tenaga ke grid nasional", to avoid cost shifting to other users.
   - Government approved at least 30% renewable energy of data centre capacity or consumption; ST "sedang membangunkan kerangka dan garis panduan menyeluruh mengenai kemudahan penjanaan sendiri".
   - Data centres must have backup generators usable "bagi tujuan kawalan permintaan" when operating reserve is low.
   - Every data centre supply application goes through ST's Energy Focus Group, then the Data Centre Task Force.
   - "sehingga Ogos 2026, permintaan elektrik pusat data yang dikontrakkan berjumlah 2,346 megawatt. Manakala penggunaan sebenarnya, ada sekitar 1,374 megawatt sahaja ... 58.5 peratus".
   - Same answer given 27 Oct 2026 (DR-27102026, pp. 132 to 133), adding TNB capex RM43bn under RP4 2025 to 2027.
16. Dewan Rakyat Hansard, 28 Oct 2026, MITI Minister Johari Abdul Ghani, winding up, about p. 98. PRIMARY. Data centre power to be separated from subsidised industry, priced "ikut harga pasaran dunia" through TNB; data centres a chance for PETRONAS, which exports "lebih kurang dalam 30 juta metrik tan setahun"; 117 data centres needing "23,000 ataupun 23,500 megawatt" if all complete.
17. Energy Commission, Guidelines for Solar PV for Self-Consumption in Peninsular Malaysia (Pin.1/2026, dated June 2026). https://www.st.gov.my/sites/default/files/2026-07/Guidelines-for-Solar-Photovoltaic-for-Self-Consumption-In-Peninsular-Malaysia.pdf PRIMARY. SELCO is solar only; no capacity limit for non-domestic consumers (s. on capacity); licence under section 9 of the Electricity Supply Act where required. No gas route in it.
18. Tenaga analyst briefing 2QFY2026 (28 Aug 2026), slides 7 and 8. PRIMARY. 6.6 GW of plant retirement by 2030; NEWGEN26 new CCGT capacity for Peninsular Malaysia, COD 2029 to 2031; TNB submitted its bid on 1 July 2026; Kapar CCGT 1,400 MW and Paka 1,400 MW in its pipeline.

SECONDARY or unverified for Malaysia: NEWGEN26 size of 6 to 8 GW (The Edge, Baker McKenzie; the ST notice URLs returned 400 and 404); "five submissions" (The Edge); Johor gas power gap (BMI, quoted by an MP in Hansard 28 Oct; Wood Mackenzie June 2026); Pengerang RGT capacity in Mtpa (PetGas page 404); The Star 3 Oct 2026 column on Selco and gas plants beside data centres (paywalled, commentary). No Gas Malaysia Bursa filing on a data centre gas supply found.

## Flag for the queue piece's fact-checker (not my gap)

The 28 Oct Hansard figure of 2,346 MW contracted against 1,374 MW used (58.5%) uses a different denominator from the piece's Tenaga series (5.65 GW in system; 6 GW at 45 operating sites, 13 Oct Hansard). Same draw, different booked figure. The 40% falsifier rests on Tenaga's maximum demand "in system", so the piece should say which denominator it tests, or a reader will see 58.5% and think it has already broken.

## What I could not verify

- Whether an islanded (not grid-connected) unit of 10 MW or more needs a Generation Licence (2014 table garbled at that row; current FAQ blocked).
- Whether a data centre's embedded gas unit buys through Gasco or a licensed importer.
- Any Singapore or Johor data centre running gas behind the meter today (none found at primary).
- ST's promised self-generation framework: not yet published.
- SKK Migas's own text; EMA's own statement on the cut.
