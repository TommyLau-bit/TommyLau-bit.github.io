# TRISO fuel: research slice for the microreactors piece

Compiled 7 Nov 2026. Primary sources unless marked LEAD (trade press, lead only). "My arithmetic" = calculated by me, not quoted.

Sources (short names):
- **Review 2019**: Demkowicz, Liu, Hunn, "Coated particle fuel: Historical perspectives and current progress", J. Nucl. Mater. 515 (Mar 2019), INL/ORNL. https://www.osti.gov/servlets/purl/1494898
- **AGR-1 2016**: Demkowicz et al., "Key results from irradiation and PIE of AGR-1 UCO TRISO fuel", INL/CON-16-38197, Nov 2016. https://www.osti.gov/servlets/purl/1358266
- **AGR-5/6/7 2021**: Demkowicz, "AGR-5/6/7 Irradiation Results and Reporting", INL/MIS-21-63273, 13 Jul 2021. https://inldigitallibrary.inl.gov/sites/sti/sti/Sort_47193.pdf
- **INL D1-3**: Advanced Fuel Cycle Cost Basis, Module D1-3, INL/EXT-21-64514, Sep 2021. https://fuelcycleoptions.inl.gov/Shared%20Documents/2021_Module_D1-3.pdf
- **INL D1-1**: Module D1-1 (LWR fabrication), INL/RPT-23-71501 Rev 2, Sep 2023. https://fuelcycleoptions.inl.gov/Shared%20Documents/Module_D1-1_rev2.docx.pdf
- **SN 10-Q**: Standard Nuclear 10-Q, quarter to 30 Jun 2026 (filed Aug 2026). https://www.sec.gov/Archives/edgar/data/0002086716/000162828026059189/nucl-20260630.htm
- **XE 10-Q**: X-Energy 10-Q, quarter to 30 Jun 2026. https://www.sec.gov/Archives/edgar/data/0002088896/000119312526347752/xe-20260630.htm
- **BWXT Q3**: BWXT Q3 2026 call, 2 Nov 2026 (Motley Fool transcript, https://fool.com/earnings/call-transcripts/2026/11/02/bwxt-q3-2026-earnings-call-transcript; check against webcast).
- **DOE 2019**: "TRISO particles: the most robust nuclear fuel on Earth", 9 Jul 2019, updated Jun 2023. https://www.energy.gov/ne/articles/triso-particles-most-robust-nuclear-fuel-earth

## 1. Structure

- **Kernel**: 350 to 600 µm (Review 2019). US AGR kernels (Review 2019, Table 2): AGR-1 UCO 350 µm at 19.7%; AGR-2 UCO 427 µm at 14.0% and UO2 508 µm at 9.6%; AGR-5/6/7 UCO 426 µm at 15.5%. Xe-100: UCO 425 µm, up to 15.5% (X-energy topical report, NRC ML21246A289).
- **Why UCO**: in UO2, oxygen freed by fission forms CO gas. That pressurises the particle ("pressure-vessel" failure) and, in a temperature gradient, drives the kernel into the coatings ("amoeba" migration). The US adopted UCO (about 80% UO2 / 20% UC2) by the early 1980s because prismatic cores run hotter and denser in power than German pebble beds, which kept UO2 (Review 2019 §2.2). AGR-1: UCO "effectively controlled oxygen partial pressure" (AGR-1 2016).
- **Four layers** (AGR-1 nominal thickness; job per Review 2019):
  1. Porous carbon **buffer**, 100 µm, about 50% dense: room for fission gas, absorbs recoil.
  2. **IPyC**, 40 µm: seals the kernel from HCl during SiC deposition, base for the SiC, holds gas.
  3. **SiC**, 35 µm: structural shell, main barrier to metallic fission products.
  4. **OPyC**, 40 µm: protects the SiC, bonds to the matrix, extra gas barrier.
  German reference: 95/40/35/40 µm on a 500 µm UO2 kernel (Review 2019, Table 1).
- **Whole particle**: about 780 µm (AGR-1) or 855 µm (425 µm kernel) (my arithmetic: kernel + 2 × 215 µm). "Poppy seed" (DOE 2019).
- **Compacts (prismatic)**: particles are over-coated with graphite and resin, pressed and carbonised into cylinders of about 25 × 12.3 mm, which go into hexagonal graphite blocks (Review 2019). Particles per compact (packing fraction), gU (Review 2019, Table 2):
  - AGR-1: 4,140 (37%), 0.91 gU.
  - AGR-2 UCO: 3,180 (37%), 1.26 gU.
  - AGR-5/6/7: 2,240 (25%) or 3,430 (38%), 0.89 or 1.36 gU.
- **Pebbles**: 60 mm sphere, 50 mm fuelled zone. German type: "around ten thousand" particles (Review 2019). Xe-100: about 19,000 particles per pebble and about 224,000 pebbles per core (X-energy topical reports, NRC ML21246A289, ML25262A126). Packing about 9.5% (my arithmetic).

## 2. Performance

- **AGR-1** (ORNL lab coater; BWXT kernels): 72 compacts, about 298,000 particles, 620 EFPD in INL's Advanced Test Reactor. Burnup 11.3 to 19.6% FIMA; compact temperatures 955 to 1,136 °C. **Zero TRISO failures in reactor and in heating tests to 1,700 °C** (AGR-1 2016).

  | AGR-1 (AGR-1 2016, Table 2) | Particles | SiC failures | Full TRISO failures (95% bound) |
  |---|---|---|---|
  | In reactor | 298,000 | 4 (1.3×10⁻⁵) | 0 (≤1.1×10⁻⁵) |
  | 1,600 °C, ~300 h | 33,100 | 3 (9.1×10⁻⁵) | 0 (≤9.1×10⁻⁵) |
  | 1,700 °C | 12,400 | 7 (5.6×10⁻⁴) | 0 (≤2.5×10⁻⁴) |
  | 1,800 °C | 16,500 | 23 (1.4×10⁻³) | 2 after >200 h (1.2×10⁻⁴) |

  The in-service bound beats the NGNP specification (≤2.0×10⁻⁴) and the HTR-Modul specification (≤1.6×10⁻⁴) (Table 3).
- **What fails first**: the SiC layer. At 1,600 °C the cause was as-made defects; higher up it was palladium and fission-product corrosion. Caesium release through intact SiC stayed below 5×10⁻⁶ per compact until SiC failed. Silver leaks through intact SiC; at 1,800 °C silver release rose after about 100 h in the fine-grained variant (AGR-1 2016).
- **AGR-2** (first BWXT particles, 150 mm coater): UCO 114,000 particles to 7.3 to 13.2% FIMA at peaks of 1,080 to 1,360 °C; UO2 18,500 particles to 9.0 to 10.7%. No definite in-pile failures. UO2 caesium release in heating tests reached about 10⁻² at 1,600 °C and 10⁻¹ at 1,700 °C, far above UCO (Review 2019).
- **AGR-3/4**: fission-product transport test with "designed-to-fail" particles (Review 2019).
- **AGR-5/6/7** (final qualification plus margin test, all BWXT-made): 194 compacts, about 570,000 particles at 15.5%. Targets: 18% FIMA, peaks of about 1,500 °C.
  - **Ended early, July 2020: 361 EFPD, peak 15.3% FIMA, peak time-average temperature 1,432 °C**, after a fission-gas surge in Capsule 1 (Oct 2019).
  - Estimated failures: **180 to 440 in Capsule 1**, 1 to 4 in Capsule 2, ≤15 in Capsule 3, 0 in Capsules 4 and 5 (AGR-5/6/7 2021).
  - INL analysed operating anomalies, including oxidation, as the cause. PIE was still being published in 2024-25 (OSTI 3002189).
- **DOE 2019**: tested "up to 1,800 °C" for over 300 h. AGR-1's 19% burnup is "three times" current LWR fuel.
- **SiC decomposition**: above about 1,900 °C (Review 2019).
- **NRC**: EPRI topical report EPRI-AR-1(NP) on UCO TRISO, submitted 31 May 2019. **NRC safety evaluation August 2020**; approved version EPRI-AR-1(NP)-A. It accepts AGR-1 and AGR-2 as a performance demonstration for particles within the measured property envelope (Table 5-5). Fuel forms and wider conditions are left to future submittals (ADAMS ML20216A453, ML20210M241; NRC blocked download, so these come via search snippets).

## 3. Why HALEU and TRISO go together

- **Uranium density**:
  - AGR-5/6/7 compact: 0.89 to 1.36 gU in about 2.97 cm³, so **0.30 to 0.46 gU/cm³** (my arithmetic, Review 2019 Table 2).
  - LWR UO2 pellet at about 95% of theoretical density: **about 9.2 gU/cm³** (my arithmetic; textbook density).
  - So there is **about 20 to 30 times less uranium per unit of fuel volume** in a compact, and pebbles are more dilute still. Most of the fuel element is carbon.
- **So enrichment rises**: per INL D1-3, TRISO designs run "considerably above" the 3 to 5% of LWRs. Early US HTGRs used more than 90%; US non-military designs now use 8 to 19.9%. Xe-100: 15.5% (XE 10-Q). Pele: ≤19.8 wt% (DOE-Idaho NEPA document, via search).
- **Why not LWR pellets in zirconium**: US rules cap zirconium cladding at **2,200 °F (1,204 °C) in a loss-of-coolant accident** (10 CFR 50.46(b)(1)), and in service it sits near 300 °C water. TRISO *operates* at 955 to 1,136 °C (AGR-1) and holds fission products at 1,600 °C for hundreds of hours. A small gas-cooled core with no water can then cool passively, because each particle is its own containment. High burnup (19.6% FIMA) lets a small core run for years.

## 4. Why it is hard to make

- **Steps** (Review 2019):
  1. Sol-gel kernels: uranium in nitric acid, gelled as droplets, washed, dried and sintered; carbon is added for UCO.
  2. Fluidised-bed chemical vapour deposition, with argon floating the kernels: acetylene for the buffer, acetylene plus propylene for the PyC layers, methyltrichlorosilane in hydrogen for the SiC.
  3. Over-coat, press into compacts or pebbles, carbonise and heat-treat.
  4. Quality control per lot: thickness, density, defects, contamination.
- **Scale-up**: AGR-1 used a 50 mm ORNL lab coater; AGR-2 and AGR-5/6/7 used BWXT's 150 mm coater (Review 2019). Each step needed a new irradiation of 2 to 3 years plus years of examination.
- **Yield**: Standard Nuclear's blended process yield is **63.3%**; the coating step alone runs at about 95 to 97% (SN 10-Q).
- **Cost** (INL "what-it-takes", 2020 $/kgU, fabrication only, no enrichment):
  - TRISO: low 1,000, mode 4,000, mean 4,667, high 9,000. The high end is for plants under 5 MTU/yr, "the type to be expected in the next 10 years" (INL D1-3).
  - PWR UO2: 242 / 421 / 605 (INL D1-1).
  - So TRISO is **about 9.5 times** LWR at the mode (my arithmetic).
  - INL: no plant of tens to hundreds of MTU/yr exists "in the U.S. (or in the world for that matter)".

## 5. Makers, capacity and status

- **BWXT, Lynchburg**:
  - Made the AGR-2 and AGR-5/6/7 particles (Review 2019).
  - **Full Pele core delivered to INL, announced 2 Dec 2025.** No kgU given (https://www.bwxt.com/bwxt-delivers-full-core-of-triso-nuclear-fuel-for-project-pele-microreactor/). LEAD: trade press reports 40,000 compacts.
  - BWXT Q3, Rex Geveden: "a couple of hundred kilograms a year on that Lynchburg line... enough capacity for fully fueling the core of the Pele reactor"; "we can at least quadruple the output". A greenfield plant (Wyoming) waits on Kairos demand and commercial HALEU.
  - **Antares deal, 27 Oct 2026: initial 1 MTU**, through the end of the decade, on the Pele and Mark-0 line (Business Wire release). Janus fuel goes on the same line.
- **Standard Nuclear** (bought Ultra Safe Nuclear's fuel assets at a Section 363 auction) (SN 10-Q):
  - **SN-0, Oak Ridge: 0.5 MTU/yr, operating under DOE authorisation (10 CFR 830), not an NRC licence.**
  - Building capacity 3.0 MTU/yr (SN-0 plus 2.5 at SN-TN).
  - SN-TN and SN-ID (Idaho, DOE land) were "substantially complete" on 22 Jul 2026. Each starts at up to 1 MTU/yr; together up to 5 MTU/yr. DOE approval targeted for Q4 2026.
  - SN-TN20 is planned at up to 20 MTU/yr.
  - The move from DOE to NRC licensing is only at the engagement-plan stage.
  - **First commercial HALEU TRISO delivery: about 50 kgU to Radiant at INL's DOME, June 2026**; the rest of the core followed after quarter end.
  - Radiant: "multi-metric tons" through 2031 (20 Aug 2026).
  - Antares: 1 MTU firm by end-2030, options for 7 MTU more (26 Aug 2026).
  - Backlog $576.9m. Q3 results due 12 Nov 2026.
- **TRISO-X (X-energy), TX-1, Oak Ridge**:
  - **NRC licence SNM-7007, 13 Feb 2026**, Part 70, 40 years. NRC release 26-019: "the first-ever U.S. approval of a category II fuel fabrication facility". Approved 3 months early; applied 5 Apr 2022.
  - "First new fuel fabrication license issued in approximately 50 years" is **DOE's** wording (DOE, 25 Feb 2026, https://www.energy.gov/ne/articles/triso-x-receives-nrc-special-nuclear-material-license-advanced-fuel-fabrication). X-energy says "over 50 years"; the NRC release does not say it.
  - **700,000 pebbles a year, 5 MTU, enough for 11 Xe-100s.** Production "early 2028" (DOE) or first half of 2028 (X-energy). TX-2, in design, would serve up to 44 Xe-100s a year (XE 10-Q).
  - DOE HALEU allocation about 7.6 MTU; Centrus enrichment deal 6 Aug 2026 (XE 10-Q).
- **Kairos Power**: its own annular TRISO pebbles. It is installing HALEU equipment at Los Alamos's Low-Enriched Fuel Fabrication Facility and expects to produce there "in 2026" with DOE HALEU. No capacity is disclosed (https://www.kairospower.com/vertical-integration, accessed 7 Nov 2026).
- **Others**: Westinghouse eVinci has Urenco HALEU (agreement in principle), and its test fuel goes via INL to ORNL and TRISO-X. No own line found. No Nano Nuclear TRISO plant found.
- **US capacity** (my arithmetic, uranium):
  - Today: BWXT about 0.2 plus SN-0 0.5 is **about 0.7 MTU/yr**.
  - End-2026 if SN-TN and SN-ID are approved: about **2.7 MTU/yr**.
  - 2028, adding TX-1 and a quadrupled BWXT: about **8 to 9 MTU/yr**, up to about 11.

## 6. Demand

- **Xe-100**: 5 MTU/yr for 11 units is **about 0.45 MTU per unit per year** (my arithmetic, XE 10-Q). LEAD: an X-energy 2020 slide gives about 7 gU per pebble, implying about 1.6 tU per first core (unverified).
- **Pele**: not published. A couple of hundred kg a year fuels a full core, so the core is **of order 100 to 200 kgU** (inference).
- **Radiant Kaleidos (1 MWe)**: more than 50 kgU per core (SN 10-Q); the total is not disclosed.
- **eVinci, Antares**: no core loading found. Antares has contracted 2 MTU firm (BWXT 1, Standard Nuclear 1) plus 7 MTU of options.
- **So**: firm orders signed from Aug to Oct 2026 already exceed three years of today's output. One Xe-100 needs about two-thirds of current US output every year.

## Conflicts and things I could not verify

- Core loadings for Pele, Kaleidos, eVinci and Antares: no primary figure found. The Pele EIS (Feb 2022) is not checked.
- The NRC EPRI safety-evaluation text was blocked. One INL slide dates the -A report to November 2020 rather than August.
- "First licence in about 50 years": DOE and X-energy say it, the NRC does not. BWXT Lynchburg already makes TRISO under an existing NRC licence (Category I, naval). The licence number and category are from memory, not verified.
- AGR-5/6/7 missed its burnup and temperature targets, with hundreds of failures in Capsule 1. No final qualification conclusion found for the 15.5% fuel.
- DOE says "no to minimal damage" at 1,800 °C; INL shows 2 full and 23 SiC failures there.
- Pele's 40,000 compacts and its arrival date (5 Nov versus 2 Dec 2025) are trade press only.
- The LWR pellet density and the Motley Fool BWXT transcript both need checking.

## Things the deck has wrong

1. **"Every particle must be perfect"**: no. Specifications allow about 2×10⁻⁴ failures, and SN's 63.3% yield shows defects are screened out. Say "defects must be rare and measured".
2. **"Tested to 1,800 °C"**: true, but particles failed there. The clean claim is "zero failures to 1,700 °C".
3. **Standard Nuclear "building to 2.5 MTU"**: building capacity is 3.0 MTU including SN-0. The two new plants start at 1 MTU each and could reach up to 5; SN-TN20 targets up to 20.
4. **Missing**: Standard Nuclear runs under **DOE authorisation, not an NRC licence**.
5. **"Well under a tonne"**: right today, stale if SN-TN and SN-ID are approved in Q4 2026 (about 2.7 MTU/yr). Even quadrupled, BWXT (about 0.8 MTU/yr) needs over a year for Antares's 1 MTU alone.
6. DOE's article says "three layers" in its text; cite INL's four.
7. **Missing**: TRISO fabrication costs about 9.5 times LWR fabrication per kgU, before the HALEU premium.
