# HALEU fuel supply: research slice for the microreactors piece

Compiled 7 Nov 2026. Primary sources unless marked LEAD (trade press or a search summary only).

## 1. Physics

- **Definition.** "Greater than 5 and less than 20 weight percent" U-235 (DOE HALEU FAQ, undated, https://www.energy.gov/ne/haleu-frequently-asked-questions).
- **Why small, long-life cores need it.** DOE says HALEU gives "a higher concentration of fissile material, improving reactor fuel energy density to either obtain higher powers or longer fuel cycle times", and makes designs "more compact". DOE, *HALEU Allocation Process*, 28 Aug 2025, fn. 1, https://www.energy.gov/sites/default/files/2025-08/HALEU%20Allocation%20Process%2008282025%20%28Final%29_0.pdf
- **Mechanism (my plain-English explanation, standard physics).**
  - A chain reaction needs each fission to cause one more.
  - In a small core, more neutrons escape through the surface (leakage). Richer fuel makes up for them.
  - A core must also start with spare U-235 to last while fuel burns and fission products absorb neutrons. Richer fuel holds that reserve, so the core runs years without refuelling at high burnup.
- **Why 19.75%, not 20%.** 20% is the HEU line. The NRC glossary defines HEU as 20% or more (https://www.nrc.gov/reading-rm/basic-ref/glossary/high-enriched-uranium). The IAEA treats HEU as direct-use material: its significant quantity is 25 kg U-235, against 75 kg for uranium under 20% (IAEA *Safeguards Glossary* 2022, seen only via a secondary source: LEAD). Contracts specify "nominal 19.75 weight percent" (Centrus 10-Q Q2 2026), which leaves a margin below the line.
- **SWU, my arithmetic.** I used V(x) = (2x−1)·ln(x/(1−x)), feed 0.711% and tails 0.25%.

  | Product | SWU per kg | kg natural U per kg |
  |---|---|---|
  | 4.95% LEU | 7.8 | 10.2 |
  | 10% LEU+ | 18.9 | 21.2 |
  | 19.75% HALEU | 41.0 | 42.3 |

  The 19.75% to 4.95% ratio is 5.2x in work and 4.1x in feed. At 0.20% tails the work ratio is still 5.2x (45.1 vs 8.7); at 0.30% it is 5.3x (37.8 vs 7.1).
- **LEU+ (5–10%)** is for today's water reactors: longer cycles and accident-tolerant fuel. It stays below the 10% Category II security line (section 6).
  - The NRC authorised Urenco USA to enrich to 10% on 30 Sep 2025 (Urenco release, https://www.urenco.com/news/global/2025/urenco-usa-authorised-to-produce-up-to-10-enriched-uranium-by-nrc).
  - Urenco USA's first run was 8.5% on 11 Dec 2025 (WNN, LEAD).
  - The NRC's rule for water-reactor fuel above 5% was proposed in Sep 2023. I found no final rule.

## 2. Russia

- **The only commercial seller.**
  - DOE NE, 7 Nov 2023: "There is no commercial source of HALEU outside of Russia currently available". https://www.energy.gov/ne/articles/centrus-produces-nations-first-amounts-haleu
  - GAO-26-107385, 20 Aug 2026: the US has "no commercial scale capacity to enrich HALEU". GAO also says "only Russia and China have the infrastructure to produce HALEU at scale", quoting WNA. https://files.gao.gov/reports/GAO-26-107385/index.html
- **Prohibiting Russian Uranium Imports Act**, PL 118-62. Signed 13 May 2024; the ban took effect 11 Aug 2024 (90 days later). Waivers end no later than 1 Jan 2028. Annual caps: 476,536 kg (2024), 470,376 (2025), 464,183 (2026), 459,083 (2027). https://www.govinfo.gov/content/pkg/PLAW-118publ62/html/PLAW-118publ62.htm
- **Russia's own restriction.** A decree of 14 Nov 2024 rescinded TENEX's general licence to export LEU to the US. Each shipment now needs a specific licence, and the decree is "extended through December 31, 2027". Centrus 10-Q Q3 2026, https://www.sec.gov/Archives/edgar/data/1065059/000162828026070557/leu-20260930.htm
- **Russian SWU bought by US reactor owners** (EIA 2025 UMAR, Table 16, https://www.eia.gov/uranium/marketing/pdf/umartable16figure15.pdf; shares are my arithmetic).

  | Year | Russian SWU | Share of total |
  |---|---|---|
  | 2021 | 3,953k | 27.8% |
  | 2022 | 3,409k | 24.0% |
  | 2023 | 4,141k | 27.2% |
  | 2024 | 3,043k | 20.1% |
  | 2025 | 3,284k of 12,710k | 25.8% |

  US-origin SWU was 23% in 2025, and the average price was US$108.70/SWU.

## 3. DOE HALEU Availability Program

**Sources of government HALEU**

- **What the law allows.** Only material "not needed for national security". Sources: surplus stock at Y-12, Savannah River and INL, plus Piketon output. NDAA FY2024 §3131(h) told DOE to "seek to make available 21 metric tons": 3 MT by Sep 2024, 8 MT by Dec 2025 and 10 MT by Jun 2026. The two Pathway 1 demonstrations (X-energy, TerraPower) come first (DOE *Allocation Process*, 28 Aug 2025).
- **EBR-II.** "Nearly 5 metric tons" had been recovered by Aug 2023, against about 10 MT expected by Dec 2028. 5 MT goes to Oklo. DOE NE, 31 Aug 2023, https://www.energy.gov/node/4832691
- **Savannah River, downblending.** "Approximately 2.2 metric tons" of HEU will be downblended to HALEU, starting "as early as 2025" and running 2 to 4 years. FR 2025-14017, 25 Jul 2025, https://www.federalregister.gov/documents/2025/07/25/2025-14017. WNA puts the yield at about 3.1 t (LEAD).
- **Savannah River, H-Canyon.** HEU will be recovered from spent fuel and downblended. Shipments start "as early as 2029", about 12 a year for about 13 years. No tonnage is given. DOE Amended ROD, Feb 2026, https://www.energy.gov/sites/default/files/2026-02/arod-eis-0279-spent-nuclear-fuel-mgmt-2026-02.pdf
- **Total.** DOE expects "about 21.2 MTU of HALEU by 2028" and 23.4 MTU by the end of 2030. DOE officials said demand will likely exceed that (GAO, 20 Aug 2026). The 21 t target has slipped about two years.
- **Money.** The Inflation Reduction Act gave the program US$700m. US$485m was obligated by Apr 2026 (GAO).

**Allocation rounds (all conditional; no quantities published)**

- **9 Apr 2025.** TRISO-X, Kairos, Radiant, Westinghouse, TerraPower. 15 companies applied; these five "met prioritization criteria". https://www.energy.gov/articles/us-department-energy-distribute-first-amounts-haleu-us-advanced-reactor-developers
- **26 Aug 2025.** Antares (Reactor Pilot Program microreactor), Standard Nuclear (TRISO lines), and Abilene Christian University with Natura. Selected "based on prioritization criteria established through the program". https://www.energy.gov/articles/us-department-energy-distribute-next-round-haleu-us-nuclear-industry
- **23 Jul 2026.** NASA (SR-1 Freedom Mars mission). Radiant, a second selection, for a microreactor at Buckley Space Force Base, Colorado, the Air Force's "preferred location". https://www.energy.gov/ne/articles/energy-department-distribute-third-round-haleu-nasa-and-radiant
- **Totals.** 10 selections and 9 recipients. No other 2026 round found.
- **DOE's published criteria:**
  - government funding or a cost share with DOE;
  - fit with DOE's goals;
  - a licensing schedule;
  - "objective evidence" of the ability to fabricate, ship and store;
  - whether the material is "readily available in the DOE inventory".
  
  DOE may rescind an allocation after "significant delays".

**Executive Order 14299** (23 May 2025)

- §5(b): DOE "shall release into a readily available fuel bank not less than 20 metric tons" of HALEU for private projects authorised at DOE sites.
- §3(a): an Army-regulated reactor must operate on a base by 30 Sep 2028. https://www.govinfo.gov/content/pkg/DCPD-202500632/html/DCPD-202500632.htm

## 4. Centrus

- **Contracts.** A 16-centrifuge cascade under a 2019 demonstration contract (US$115m). The HALEU Operation Contract followed in Nov 2022, with options for up to nine more years (10-Q Q3 2026, filed 4 Nov 2026).
- **Output.**

  | Phase | Dates | Output | Source |
  |---|---|---|---|
  | Phase 1 | 7 Nov 2023 | "more than 20 kilograms" | Centrus, https://investors.centrusenergy.com/node/19281 |
  | Phase 2 | Jun 2025 | 900 kg UF6; late because DOE-supplied 5B cylinders came late | 10-Q |
  | Phase 3 (Option 1a) | mid-Jun 2026 | target "another 900 kilograms"; Centrus gives no figure | GAO |

  Phases 1 and 2 make the ~920 kg (my sum). GAO says Centrus was "on track for 1.8 MTU", so about 1.8 t by Jun 2026. The 900 kg/yr rate is from Centrus and DOE, 7 Nov 2023.
- **Production stops.** On 30 Jun 2026 DOE cut Option 1b to "cascade maintenance and HALEU storage, with no HALEU production" for US$15.0m. DOE "does not currently intend to exercise further production options".
- **New, 20 Oct 2026.** Under a "HALEU Transfer Agreement", DOE gave ACO title to the HALEU, feed and tails. ACO took on security and facility costs and agreed "to hold the HALEU for resale to DOE upon request". The Piketon lease is fixed to end on 1 Oct 2027 (10-Q Q3 2026).
- **4 Nov 2026 release.** "Enriching HALEU for the commercial market from existing 16-centrifuge cascade". The FY2027 budget "does not include further funding". US$5.4bn of contingent LEU and HALEU commitments. No volume given. https://www.sec.gov/Archives/edgar/data/0001065059/000162828026070229/ex991-10q2026_11x04.htm
- **DOE task orders, 5 Jan 2026.** US$2.7bn "over the next ten years", paid on milestones:
  - Centrus's ACO, US$900m for HALEU capacity;
  - General Matter, US$900m for HALEU capacity;
  - Orano Federal Services, US$900m for LEU;
  - GLE, a separate US$28m.
  
  https://www.energy.gov/articles/us-department-energy-awards-27-billion-restore-american-uranium-enrichment
- **Centrus's order, signed 1 Jul 2026.** Firm fixed price of US$900m to deploy capacity and deliver "by July 2032, one metric ton" of 19.75% HALEU UF6. DOE has two options of 5 MTU each at US$17.0m per MTU, about US$17,000/kg (my arithmetic). Centrus 10-Q Q2 2026, https://www.sec.gov/Archives/edgar/data/0001065059/000162828026053863/leu-20260630.htm
- **NRC licence SNM-2011.** Amendment 13 (11 Jun 2021) allowed 600 kg of HALEU UF6. Amendment 29 (effective 1 Jul 2025) covers Phase III. Seen in an NRC ADAMS search summary only (ML25162A133); the NRC server blocked the fetch.
- **Customers (Q3 10-Q).**
  - Oklo: definitised, deliveries from 2029.
  - X-energy (LEU and HALEU), Radiant and Antares: "long-term supply agreements", all with "prepayments".
- **Radiant.** Release of 8–9 Sep 2026: a "definitive multi-year contract" for multiple Kaleidos units. Deliveries come "before the end of the decade", Radiant prepays, and the fuel is "unobligated", so usable for defence. No volume. https://www.sec.gov/Archives/edgar/data/0001065059/000162828026061036/ex991-centrusandradianta.htm. The Facebook-video claim is verified.

## 5. Other future supply

- **General Matter.** A 100-acre DOE lease at Paducah (Aug 2025), plus at least 7,600 UF6 cylinders. The company targets the end of the decade; DOE's announcement said 2034 (both LEAD). US$900m task order.
- **Orano, Project IKE, Oak Ridge.** Licensed for a maximum of "8-weight percent", so **LEU+, not HALEU** (NRC notice, FR 2026-16372, 12 Aug 2026, https://www.govinfo.gov/content/pkg/FR-2026-08-12/html/2026-16372.htm).
- **Urenco.**
  - US: LEU+ to 10% at Eunice. It told the NRC it has "contracted HALEU orders" (above 5%) needing 40 to 50 cylinders in 2026–27 (FR 2026-07319). It held a 2024 HALEU contract but got no task order.
  - UK: £196m for a Capenhurst HALEU plant producing "by 2031" (gov.uk, May 2024). GAO cites 10 MTU/yr in the early 2030s.
- **GLE (laser), Paducah.** The NRC docketed the application on 4 Aug 2025. Final EIS due Sep 2026, safety evaluation due Jan 2027 (NRC project page, https://www.nrc.gov/materials/fuel-cycle-fac/laser; LEAD until opened). Its first product is LEU from tails.
- **ASP Isotopes / QLE.** A HALEU plant is planned at Pelindaba, South Africa, "subject to the receipt of all required permits and licenses". TerraPower provides a conditional loan and a 10-year offtake (10-Q Q2 2026, https://www.sec.gov/Archives/edgar/data/0001921865/000119312526352603/aspi-20260630.htm). A JV with Necsa, 80/20, was agreed 15 Oct 2026 (SENS, LEAD). It has not enriched uranium.

## 6. After enrichment

- **Deconversion.** DOE picked six companies on 8 Oct 2024: BWXT, Centrus, Framatome, GE Vernova, Orano and Westinghouse. Each has a US$2m minimum, up to US$800m in total (LEAD). GAO, Aug 2026, calls it "a capability that does not yet exist for HALEU". I found no task order.
- **Shipping.** NRC notice, 15 Apr 2026 (FR 2026-07319, https://www.govinfo.gov/content/pkg/FR-2026-04-15/html/2026-07319.htm):
  - the standard DN30/30B package (CoC 9362) is certified only to 5%;
  - Orano's DN30-X (CoC 9388, with 30B-10 or 30B-20 cylinders) is the "only one approved UF6 transportation package for commercial HALEU quantities";
  - "manufacturing of this approved transportation package has not yet occurred".
  
  The Urenco exemption was granted 4 Jun 2026 (FR 2026-11192).
- **Security.** Under 10% is Category III. "10 kilograms or more of U-235 in uranium enriched to 10 to 20" is Category II (10 CFR 70.4; NRC, https://www.nrc.gov/materials/new-fuels/security-safeguards). The NRC sees "no near-term updates" needed to material control and accounting (MC&A) for HALEU. **No primary figure found for what Category II costs a fuel plant.**

## 7. Demand

- **DOE, 5 Jun 2023.** About 22 MTU "by the mid-2020s" for first cores, then 8 to 12 MTU/yr, rising "to over 50 MTU by 2035" (FR 2023-11877, https://www.govinfo.gov/content/pkg/FR-2023-06-05/html/2023-11877.htm). The same notice quotes NEI's survey of up to 600 MTU/yr by 2035.
- **DOE ROD, 14 Jan 2025.** "More than 40 metric tons (MT) of HALEU will be needed by 2030" (FR 2025-00610, https://www.govinfo.gov/content/pkg/FR-2025-01-14/html/2025-00610.htm).
- **GAO's summary of DOE's 2024 EIS.** About 50 MTU/yr by 2035 and about 500 MTU/yr by 2050.
- **My arithmetic.** Contracted new production (1 MTU by 2032) plus the government stock (21.2 MTU by 2028) is about half of DOE's 40+ t by 2030.

## Conflicts and things I could not verify

- **EO 14299 deadline.** DOE's Allocation Process says the order requires release of 20 t "within 90 days". The order puts the 90 days on the inventory review in §5(a), not on the release.
- **Centrus cumulative output.** Centrus never states a total. The ~1.8 t rests on GAO's "on track".
- **Orano limit.** One search result said 10%; the FR notice says 8%. Use 8%.
- **General Matter start date.** End of decade against 2034. Both LEAD.
- **Not opened** (NRC 403s and others):
  - NRC Amendment 29;
  - GLE's schedule;
  - DOE's deconversion release;
  - the IAEA glossary page;
  - the gov.uk tonnage.
- **Not found:**
  - per-allocation tonnages;
  - the cost of Category II;
  - any Space Force allocation of its own. Buckley is Radiant's allocation.
- **Tenex as HALEU seller.** No primary document names Tenex as the HALEU seller. Use DOE's "no commercial source outside of Russia".

## Things the deck or the live piece has wrong

1. **Live piece, Centrus chart.** It says "0.9 tonnes... phase two alone; earlier phases' output is not stated". Phase 1 (>20 kg) is stated, and Phase 3 ran to mid-Jun 2026. GAO puts the total at about 1.8 t, so the chart understates output by about half.
2. **Live piece: government HALEU "recovered from old reactor fuel", "no tonnage published".** The stock also includes downblended HEU (2.2 t, Savannah River). DOE's 21.2 MTU by 2028 is published, via GAO.
3. **Both: the 20 Oct 2026 HALEU Transfer Agreement is missing.** DOE gave ACO title to the HALEU it produced, to hold for resale to DOE. The Piketon lease ends 1 Oct 2027.
4. **Deck slide 394: "no volume, no buyer named".** The Q3 10-Q names X-energy, Radiant and Antares agreements with prepayments, and Oklo as definitised. The volume is still undisclosed.
5. **Deck notes: "Urenco Capenhurst 27 t/yr".** No source found. The sources give 10 t/yr, early 2030s.
6. **Live piece: "roughly six times" the SWU.** Correct against 4.5% fuel. Against 4.95% it is about 5.2x. Say which.
7. **Deck: "5% to under 20%".** Strictly, it is above 5%. Minor.
8. **Verified, no change needed:** Russia 25.8% (2025) and waivers ending by 1 Jan 2028.
