# Solar, storage and the 24-hour load: build speed, load shape, hyperscaler projects

Gathered 9 Nov 2026. Primary sources unless marked PRESS ONLY. "Derived" means my own arithmetic from a primary number, not a source's statement. Grid-operator accreditation (PJM ELCC, ERCOT) and tax credits are covered in operators.md and are left out here.

---

## A. What the US is building (EIA)

**1. Planned 2026 additions: 86 GW, solar about half.**
- Solar 43.4 GW (51%), battery storage 24 GW (28%), wind 11.8 GW (14%), natural gas 6.3 GW (combined cycle 3.3 GW, combustion turbines 2.8 GW). Gas share is about 7%, derived (6.3 / 86).
- EIA calls the 86 GW total "a record if realized." The data come from the Preliminary Monthly Electric Generator Inventory (EIA-860M), December 2025 data.
- Texas holds 40% of planned solar and 53% of planned battery storage.
- Source: EIA, Today in Energy, "New U.S. electric generating capacity expected to reach a record high in 2026", 20 Feb 2026. https://www.eia.gov/todayinenergy/detail.php?id=67205

**2. 2025 actual additions (final): 56.6 GW.**
- By energy source (MW, net summer): solar 29,459.1; wind 6,082.0; natural gas 4,589.6; nuclear none; total 56,609.0.
- Batteries have no line of their own. They sit inside "Other Energy Sources", 16,380.1 MW.
- Retirements were 5,114.4 MW, including 859.6 MW of gas.
- Source: EIA, Electric Power Annual 2025, Table 4.6, "Utility-Scale Capacity Additions, Retirements and Changes by Energy Source, 2025". https://www.eia.gov/electricity/annual/html/epa_04_06.html
- The earlier preliminary EIA figures, in the 20 Feb 2026 article in fact 1, were 53 GW in total, 27.2 GW of solar and 15 GW of batteries ("a record"). Use the final figures.

**3. Battery fleet: 43.6 GW at end-2025, nearly 52 GW by mid-2026.**
- Additions were 8.3 GW in the first half of 2026.
- Planned: 14 GW in the second half of 2026, 26 GW in 2027 and 14 GW in 2028.
- The article gives no MWh figure and no average duration.
- Source: EIA, Today in Energy, "Battery storage capacity averaged 70% growth over the last three years", 7 Aug 2026. https://www.eia.gov/todayinenergy/detail.php?id=67925

**4. Battery duration: the latest EIA average found is about 3 hours (fleet built through 2020).**
- Quote: batteries built through 2020 could "produce their rated nameplate power capacity for about 3.0 hours on average before recharging."
- Quote: batteries of four to eight hours "are typically cycled once per day".
- Source: EIA, Today in Energy, "Duration of utility-scale batteries depends on how they're used", 25 Mar 2022. https://www.eia.gov/todayinenergy/detail.php?id=51798
- The AEO2026 reference battery is a "four-hour lithium-ion battery" (Table 3, EMM Assumptions, April 2026; see fact 8).

**5. 2025 capacity factors, utility-scale (final).**

| Technology | 2025 | 2024 |
|---|---|---|
| Nuclear | 91.1% | 90.8% |
| Natural gas combined cycle | 58.7% | 60.5% |
| Wind | 33.8% | 34.3% |
| Solar photovoltaic | 24.0% | 23.2% |
| Natural gas combustion turbine | 13.6% | 13.9% |

- Sources: EIA, Electric Power Monthly (released 23 Oct 2026, August 2026 data).
  - Table 6.07.A, fossil fuels: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_a
  - Table 6.07.B, non-fossil: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_6_07_b
- The tables have no storage column.

**6. Solar collapses in winter: monthly capacity factors, 2025.**

| Month | Solar PV | Wind | Nuclear |
|---|---|---|---|
| Jan | 16.2% | 37.4% | 98.3% |
| Feb | 18.7% | 37.2% | 93.6% |
| Mar | 23.6% | 43.1% | 85.4% |
| Apr | 27.5% | 40.7% | 81.8% |
| May | 29.3% | 32.1% | 84.9% |
| Jun | 31.9% | 32.2% | 93.4% |
| Jul | 31.9% | 27.5% | 96.7% |
| Aug | 29.7% | 23.8% | 96.6% |
| Sep | 26.7% | 23.1% | 92.4% |
| Oct | 22.4% | 33.8% | 81.0% |
| Nov | 16.9% | 35.4% | 90.2% |
| Dec | 13.1% | 39.2% | 99.2% |

- Source: EIA, Electric Power Monthly, Table 6.07.B (URL as in fact 5). Nuclear's spring and autumn dips are refuelling outages.
- Derived: 1 / 0.240 = about 4.2 MW of solar nameplate per MW of average output over the year. In December it is 1 / 0.131 = about 7.6 MW. That is the average only, before storage losses and before the night is covered.
- EIA reports round-trip efficiency of about 80% for utility-scale batteries (Today in Energy id=46756). I found this in search results only and did not open the article.

---

## B. How long each takes to build

**7. Time in the queue: the median exceeds five years, all technologies combined.**
- LBNL, "Queued Up: 2026 Edition, Characteristics of Power Plants Seeking Transmission Interconnection As of the End of 2025". Authors: Rand, Cheyette, Talley, Zhang, Gorman, Wiser, Seel, Jeong, Kahrl. Published 05/2026.
- Quote (publication page): "the median duration from IR to COD was over 5 years for projects built in 2025."
- Publication page: https://eta-publications.lbl.gov/publications/us-interconnection-queue-data-0
- PDF: https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf (behind a bot check, so not read).
- Search snippets attribute three figures to the 2026 edition: 61 months for projects built in 2025 (36 in 2015, 22 in 2008), 45 months from request to agreement, and 31 months from agreement to operation. These are UNVERIFIED and should be checked in the PDF.
- Search snippets give 55 months for 2024 builds from the 2025 edition. UNVERIFIED.
- APPA (publicpower.org, 1 Jul 2026) repeats "exceeds 5 years". That is PRESS, citing LBNL.
- I found no breakdown of the median duration by technology (solar against gas against storage).

**8. Build time once permitted: EIA's lead times by technology (AEO2026).**

| Technology | Lead time (years) | First available year | Reference size (MW) |
|---|---|---|---|
| Battery storage (4-hour lithium-ion) | 1 | 2026 | 150 |
| Solar PV with tracking | 2 | 2027 | 150 |
| Solar PV with storage | 2 | 2027 | 150 MW PV plus 50 MW, 4-hour battery |
| Combustion turbine, aeroderivative | 2 | 2027 | 211 |
| Combustion turbine, industrial frame | 2 | 2027 | 419 |
| Onshore wind | 3 | 2028 | 200 |
| Combined cycle, single-shaft | 3 | 2028 | 627 |
| Combined cycle, multi-shaft | 3 | 2028 | 1,227 |
| Nuclear, light water reactor | 6 | 2031 | 2,156 |
| Nuclear, small modular reactor | 6 | 2031 | 480 |

- Source: EIA, "Assumptions to the Annual Energy Outlook 2026: Electricity Market Module", April 2026, Table 3 "Cost and performance characteristics of new central station electricity generating technologies", p. 6. Cost data from Sargent & Lundy, January 2024. https://www.eia.gov/outlooks/aeo/assumptions/pdf/EMM_Assumptions.pdf
- Caveat: these are modelling lead times. They exclude the interconnection queue (fact 7) and today's gas-turbine order backlog.
- Overnight costs (2025$/kW): battery $1,521, PV with tracking $1,484, PV with storage $1,903, CC multi-shaft $1,032, LWR $8,255 total.

---

## C. Data centre load shape

**9. California Energy Commission: data centres run at about 80 to 96% of their own peak every hour.**
- The CEC builds hourly load profiles from interval (AMI) meter data from existing data centres.
- Slide 10, "Hourly Load Factor Profiles (2025 IEPR)", charts the average annual load factor by hour, weekday against weekend, and the weekday profile summer against winter. The y-axis runs from 80% to 96%.
- I could not render the chart. The exact line values are unread; the axis range is from the slide's text layer.
- The slide deck also uses a "Utilization factor (67%): requested capacity vs. max demand".
- Source: CEC, "Data Center Data Collection and Forecasting", Demand Analysis Working Group, 12 Aug 2026. https://www.energy.ca.gov/sites/default/files/2026-08/Data_Center_Data_Collection_and_Forecasting_ada.pdf
- An earlier CEC deck (Jenny Chen, 21 Nov 2024) defines the two measures:
  - "Hourly Load Factor = Data center consumption for the hour ÷ (data center peak demand)".
  - "Peak demand of data center: ~67% of installed capacity", from historical AMI data for a sample of data centres.
  - URL: https://www.energy.ca.gov/sites/default/files/2024-11/Data_Center_Forecasts_ada.pdf
- Reading: the load is flat against its own peak, but the peak sits well below nameplate.

**10. Silicon Valley Power (municipal utility): system load factor of about 80% because of data centres.**
- SVP's 2021 comments to CAISO say data centre block loads give an average annual load factor "as high as 80%".
- The draft IRP gives 80%. An SVP CEC presentation used a 79% load factor and a peak of about 67% of nameplate.
- I saw these through search snippets only. The primary SVP and CAISO documents were not opened.
- URLs to verify:
  - https://www.caiso.com/documents/svpcomments-2020-2021transmissionplanningprocess-feb092021stakeholdercall.pdf
  - https://www.siliconvalleypower.com/home/showpublisheddocument/85748/638702110758000000
- Status: UNVERIFIED (primary exists, not read).

**11. LBNL 2024 report: CAUTION, it does not say data centres are flat.**
- It assumes a 50% average capacity utilisation for converting energy to power.
- Quote (Executive Summary, p. 6): "Assuming an average capacity utilization rate of 50%, this annual energy use range would translate to a total power demand for data centers between 74 and 132 GW." The range is 325 to 580 TWh in 2028, or 6.7% to 12.0% of US electricity.
- Server assumptions (p. 27): "AI accelerated and non-accelerated servers doing training are assumed to have a constant 80% operational time throughout the whole period, while the same servers doing inferencing have a constant 40% operational time". AI server idle power is 20% of rated power (p. 27).
- These are server utilisation assumptions, not a measured facility load shape. The report gives no hourly or load-factor data.
- Source: Shehabi et al., "2024 United States Data Center Energy Usage Report", LBNL, December 2024 (published 19 Dec 2024). https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
- I read a mirror copy. The official PDF is behind a bot check.
- Implication for the piece: do not cite LBNL for "flat around the clock". Cite the CEC metered profiles (fact 9). The WP-356 authors note, quoting NERC 2025, that data centres "are known to exhibit spiky load profiles" at short timescales.

---

## D. Hyperscaler solar plus storage at data centres

**12. Google, Intersect and TPG Rise Climate: co-located "power-first" parks (10 Dec 2024).**
- Google quote: "industrial parks with gigawatts of data center capacity in the U.S., co-located with new clean energy plants"
  - The first phase was "expected to be operational by 2026 and fully complete in 2027".
  - The aim was "reducing both the timeline to operation and the amount of new transmission required".
  - Source: Google blog, Ruth Porat, 10 Dec 2024. https://blog.google/inside-google/infrastructure/new-approach-to-data-center-and-clean-energy-growth/
- Intersect release, same date: "a targeted $20 billion in renewable power infrastructure investment by the end of the decade". The funding round was "more than $800 million". The design includes "added battery storage". https://intersect.com/news/intersect-power-forms-strategic-partnership-with-google-and-tpg-rise-climate-to-co-locate-data-center-load-and-clean-power-generation

**13. Alphabet bought Intersect: US$4.75bn cash plus debt.**
- Announced 22 Dec 2025.
- Excludes Intersect's operating assets in Texas and its operating and in-development assets in California.
- Pichai said the deal lets Google add capacity faster and match new generation to new data centre load.
- Sources: PRESS, quoting Alphabet's release (Axios, PV Tech, Latitude Media). I did not open the Alphabet release on abc.xyz.
- Closing on 12 Mar 2026 is reported by Cleary Gottlieb, counsel. PRESS/ADVISER ONLY: https://www.clearygottlieb.com/news-and-insights/news-listing/alphabet-completes-4-75-billion-acquisition-of-intersect-power

**14. Quantum, Haskell County, Texas: the first park.**
- 640 MW of solar and 1.3 GWh of batteries. The battery MW rating is not stated.
- "The project began operations in June 2026." It is co-located with a Google data centre campus that "recently began construction".
- No gas is mentioned. The data centre MW is not disclosed.
- The same page lists "840 MW PV" in a header field but "640 MW" in the text. Use 640 MW, which POWER (4 Jun 2026) also reports.
- Source: Intersect portfolio page. https://www.intersect.com/portfolio/quantum

**15. Meitner Energy Center, Gray and Roberts Counties, Texas: Google's second park needs gas.**
- Announced 4 Jun 2026. The project includes "a data center co-located with more than a gigawatt of wind, solar, and battery storage systems".
- Quote: "The majority of the site's power will come from clean energy starting on Day One."
- Quote: "with a minority share of the site's demand met by firming on-site gas to ensure reliable operations."
- Sources:
  - Intersect release, 4 Jun 2026. https://www.intersect.com/news/google-and-intersect-deepen-texas-roots-with-new-data-center-and-energy-investments-in-gray-and-roberts-counties
  - Google blog, 4 Jun 2026: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/meitner-energy-center/ The fetched page names no technologies; the gas wording is in Intersect's release.
- No MW split, gas size, data centre load or in-service date is disclosed.

**16. Meta and Enbridge "Cowboy" project, near Cheyenne, Wyoming: 365 MW solar and a 200 MW / 1,600 MWh battery.**
- Tesla supplies the batteries. Power is delivered through Cheyenne Light, Fuel and Power under a large-load tariff, with a battery tolling agreement. Service is due by end-2027, at about US$1.2bn.
- Announced late May 2026. PRESS ONLY (PV Tech, Utility Dive, ESS News); I did not open Enbridge's own release.
- 200 MW / 1,600 MWh is an 8-hour battery, derived.
- URL: https://www.utilitydive.com/news/enbridge-meta-build-365-mw-200-mw-solarstorage-project/820905/

**17. Meta and Ørsted: Eleven Mile, Arizona.**
- 300 MW of solar plus a 300 MW / 1,200 MWh (4-hour) battery. Meta's PPA (Dec 2023) covers most of the output, serving the Mesa data centre area via SRP.
- PRESS ONLY. Battery supplier deliberately omitted.

**18. Microsoft and NiSource/NIPSCO, Indiana.**
- A 20-year electric service contract for a Microsoft data centre, starting 2028.
- NiSource's GenCo contracted a 600 MW stand-alone battery (reported as 600 MWAC / 2,400 MWh, 4-hour) under a tolling agreement with AGP, October 2026.
- The 10-Q defines GenCo's plan for "two 239 MW F-frame CTs" (gas) in its Pool Resource Assets.
- The battery MWh, the counterparty and the dates are reported from the 8-K of about 15 Oct 2026, which I did not read. PARTLY VERIFIED: the gas CT wording is from the 10-Q; the battery terms are PRESS ONLY (Baxtel, DCD).
- 10-Q: https://www.sec.gov/Archives/edgar/data/0001111711/000111171126000100/nix-20260930.htm

**19. Tesla Energy storage deployments (SEC 8-K exhibits 99.1).**

| Period | GWh | Release |
|---|---|---|
| FY2024 | 31.4 | PRESS (energy-storage.news); not checked in a filing |
| Q4 2025 | 14.2 | 8-K filed 2 Jan 2026 |
| FY2025 | 46.7 | 8-K filed 2 Jan 2026 |
| Q1 2026 | 8.8 | 8-K filed 2 Apr 2026 |
| Q2 2026 | 13.5 | 8-K filed 2 Jul 2026 |
| Q3 2026 | 13.7 | 8-K filed 2 Oct 2026 |

- Quotes from the Q4 2025 release: Tesla "deployed 14.2 GWh of energy storage products", "a record for deployments", and "Energy storage deployments for 2025 were 46.7 GWh."
- Derived: 36.0 GWh in the first nine months of 2026.
- Release URLs:
  - Q4 2025: https://www.sec.gov/Archives/edgar/data/1318605/000162828026000016/exhibit9914.htm
  - Q1 2026: https://www.sec.gov/Archives/edgar/data/1318605/000162828026022956/exhibit9911111.htm
  - Q2 2026: https://www.sec.gov/Archives/edgar/data/1318605/000162828026046717/exhibit99111111.htm
  - Q3 2026: https://www.sec.gov/Archives/edgar/data/1318605/000162828026064366/exhibit991111111.htm
- 10-Q Q3 2026 energy generation and storage revenue: $2,881m (Q3 2026) against $3,415m (Q3 2025). https://www.sec.gov/Archives/edgar/data/1318605/000162828026066775/tsla-20260930.htm

**20. xAI Colossus, Memphis: batteries not documented in a primary record I could find.**
- TVA's board approved 150 MW (7 Nov 2024), with MLGW as the customer. TVA reportedly cited xAI's Megapack commitment.
- The battery figures vary between sources: 150 MW in Tom's Hardware, about 120 MW / 119 units in Cleanview. All are PRESS ONLY.
- The Shelby County Health Department permits I found cover gas turbines (15 permitted, July 2025), not batteries.

---

## E. How much solar and storage a 24/7 load needs

**21. UC Berkeley working paper WP-356 (Energy Institute at Haas, Feb 2026). Not LBNL, not peer-reviewed.**
- Authors: Chojkiewicz, Manocha, Paliwal, Callaway, Phadke. All UC Berkeley affiliations as printed (Energy and Resources Group, Goldman School, EECS).
- Method: "Using eight years of hourly weather data, we co-optimize load and hybrid solar+storage+gas configurations at 68 existing plants near data center developments, meeting over 95% of demand with solar+storage." Storage is up to six hours, gas covers at most 5% of energy, and the model assumes "a conservative constant demand assumption".
- Cost: LCOE of $60-138/MWh (2028 commissioning, 2025$).
- Key line for the argument (p. 7): "backup for a solar+storage system supplying a constant load occurs primarily during winter nights".
- Fig. 2 caption (p. 8): "backup is mostly needed on winter nights, while system peaks occur on summer afternoons."
- Example (p. 9): in BPA, at the Coyote Springs II plant, during a cold, low-sun week in January 2022, the least-cost plan runs gas continuously on 3 and 5 January.
- The solar-to-load ratios are computed (p. 18), but the text does not print them; they sit in figures and supplementary material I could not read.
- Source: https://escholarship.org/uc/item/4kf8w5pc

**22. NREL: winter nights and 4-hour storage.**
- A 2023 NREL capacity-value study (docs.nrel.gov fy23osti/85878) is reported to find that winter net-peak problems at night cannot be eased with solar and need well over 4 hours of storage.
- I saw this in search snippets only and did not read it. UNVERIFIED.

---

## Most useful for the argument

1. Solar is the build: 43.4 GW planned for 2026, half of 86 GW, against 6.3 GW of gas (EIA, 20 Feb 2026). Batteries take 1 year and solar 2 years against 6 for nuclear (EIA AEO2026 Table 3).
2. Solar's 2025 capacity factor was 24.0%, against nuclear's 91.1% (EPM 6.07.A/B). In December solar fell to 13.1% while nuclear ran at 99.2%. That is about 4.2 MW of solar per MW of average output a year, and about 7.6 MW in December (derived).
3. Batteries in the fleet hold about 3 to 4 hours (EIA; AEO reference 4-hour). Even Meta's 8-hour Wyoming battery covers a night, not a week of cloud.
4. Data centres are flat: hourly load factors of 80 to 96% of peak in CEC metered data, and SVP reports about 80% annual system load factor.
5. Google's own second solar park (Meitner, June 2026) needs "firming on-site gas" for a "minority share" of demand. The Berkeley study finds backup is needed "primarily during winter nights". Both are the night-and-winter gap in the operators' own words.

## Could not verify

- The LBNL Queued Up PDFs (2025 and 2026 editions) are behind a Cloudflare bot check. Technology-specific medians and the 61/45/31-month figures are unread; only "over 5 years" is confirmed.
- The LBNL 2024 report has no flat-load or load-factor statement. It assumes 50% average utilisation.
- The CEC slide 10 line values were not read; only the 80 to 96% axis range is confirmed.
- SVP and CAISO load-factor documents were not opened.
- The Alphabet release on Intersect and the Enbridge release on Cowboy were not opened (press only).
- NiSource's 8-K battery terms were not read.
- Ørsted Eleven Mile is press only.
- xAI Memphis battery size: no primary record found.
- EIA's current fleet-average battery duration: none found after the March 2022 article (through-2020 data).
- No NREL or LBNL study giving a solar-MW-per-firm-MW ratio for a 24/7 load was found. WP-356 computes the ratios but does not print them in its text.
- Microsoft solar-plus-storage contracts tied directly to a data centre with MWh: none confirmed from primary sources.
