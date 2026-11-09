# Heat and water research: WATER, in the companies' and regulators' own numbers

Research slice for the depth rebuild of `heat-and-water`. Compiled 7 November 2026. Primary documents were downloaded and read with pypdf where possible: Google's 2024, 2025 and 2026 Environmental Reports; Microsoft's 2026 Environmental Sustainability Report and its 2026 Data Fact Sheet; the AWS 2025 Sustainability Summary; Meta's 2025 Sustainability Report and 2025 Environmental Data Index; LBNL's December 2024 data centre report; Loudoun Water's October 2024 rate presentation. Blogs were read on the company sites.

Tags: **[primary]** company report, regulator, court, utility or government document; **[press]** lead only, not to carry a number in the piece without a primary; **[calc]** my arithmetic from primary figures, method shown; **[background]** textbook or long-standing reference figure.

Units: 1 US gallon = 3.785 litres. 1 million gallons (Mgal) = 3.785 megalitres (ML). 1 ML = 1,000 m3.

---

## 0. Definitions first (they decide every comparison)

| Term | What it counts | Who uses it |
|---|---|---|
| **Withdrawal** | All water taken in from a utility, well or river, whatever happens to it next | Google per-site table; AWS WUE; Meta WUE; Microsoft per-site table |
| **Discharge** | Water sent back, mostly to the sewer, after use (cooling tower "blowdown", sanitary) | Google, Microsoft, Meta |
| **Consumption** | Withdrawal minus discharge: water lost to the local system, mostly as vapour from cooling towers or evaporative pads | Google per-site table; LBNL site WUE; Microsoft's WUE per its Dec 2024 definition |
| **Site (direct) water** | Water used at the data centre itself | All four companies |
| **Indirect (embedded) water** | Water consumed at the power stations making the electricity the site buys | LBNL; Meta (the only one of the four that publishes it) |
| **WUE** | Litres per kWh of IT energy. The numerator differs by company | see section 2 |
| **Water risk / stress** | Google: its own Data Center Water Risk Framework (low, medium, high "risk of water depletion or scarcity"). Microsoft: WRI Aqueduct plus Pacific Institute "water stress". AWS and Meta: WRI Aqueduct baseline water stress | not comparable across companies |

The point for the piece: Google's consumption figures and AWS's or Meta's withdrawal WUE are not the same quantity, and "high risk" means four different things at four companies. The claim's limb 2 ("a water source it rates at high risk") therefore needs each company's own rating, and only Google rates sources by name.

---

## 1. Google

### 1.1 Fleet totals [primary]

Google 2026 Environmental Report (FY2025), data tables p.96, opened 7 Nov 2026: https://sustainability.google/files/1699a2e19277e478b38a659f00cb38398a836e8c/download-1699a2e1.pdf

| Million gallons | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Withdrawal (data centres and offices) | 6,297 | 7,600 | 8,653 | 11,011 | 14,689 |
| Discharge | 1,735 | 2,035 | 2,301 | 2,876 | 3,820 |
| Consumption | 4,562 | 5,565 | 6,352 | 8,135 | 10,869 |

- 2025 split: data centres withdrew 13,562, discharged 3,039, consumed **10,523 Mgal**; offices and other consumed 346 (p.96). [primary]
- Data centre withdrawal by type, 2025: potable 10,949; non-potable 1,695; reclaimed wastewater 918 Mgal (p.97). [primary] Shares: **80.7% potable, 12.5% non-potable, 6.8% reclaimed**. [calc]
- Data centres consumed 77.6% of what they withdrew in 2025 (10,523 / 13,562). [calc]
- Text, p.35: "In 2025, we consumed 10.9 billion gallons (41 billion liters...)", "Our water consumption increased 34% from 2024 to 2025". [primary] 10,869 / 8,135 = +33.6%. [calc]
- Text, p.35: water is "a highly efficient means of cooling that requires less energy than air-cooling technologies". [primary]
- Rough intensity: 10,523 Mgal = 39.8 billion litres over 42.4 TWh of data centre electricity (p.93) is about **0.94 litres consumed per kWh of facility electricity in 2025** (0.96 in 2024). [calc] Caveat: the electricity line includes third-party-operated data centres while the water table covers only owned and operated ones, so the true owned-site figure is higher. This is the clearest sign that Google evaporates by design: its consumption per kWh is several times the withdrawal WUE AWS and Meta report.

### 1.2 Share of freshwater withdrawal by risk [primary]

| Year of data | Low | Medium | High | Source |
|---|---|---|---|---|
| 2023 | 69% | 16% | **15%** | 2024 report, p.80 data table and water section ("watersheds with high water scarcity") |
| 2024 | 72% | 14% | **14%** | 2025 report, p.110 |
| 2025 | 72% | 15% | **13%** | 2026 report, p.96 |

- The live piece's 15, 14, 13 series is right.
- Terminology changed: the 2024 report said "watersheds with ... water scarcity"; the 2025 report (endnote 163) says the percentages are "based on sources (which can include watersheds) at risk for both water scarcity or depletion" and "The scope of the metric remains unchanged". [primary]
- Method (2026 report, methodology p.88): data centres are rated with Google's Data Center Water Risk Framework into low, medium or high; offices with WRI Aqueduct and WWF Water Risk Filter. [primary]
- Endnote 79 (2026): The Dalles sources were assessed in 2022; Google "aim[s] to repeat these assessments across our existing data center portfolio every three to five years". [primary] So ratings of older sites can change.

### 1.3 Per-site table, 2025 and earlier [primary]

2026 report p.97 (2025 data); 2025 report pp.110 to 111 (2024 data); 2024 report p.80 (2023 data). Million gallons.

| Site | 2025 withdrawal | 2025 discharge | **2025 consumption** | 2024 consumption | 2023 consumption | Note |
|---|---|---|---|---|---|---|
| Council Bluffs, IA | 1,746.4 | 400.4 | **1,346.0** | 1,010.2 | 980.1 | largest |
| Mayes County, OK | 1,396.7 | 315.3 | **1,081.4** | 833.2 | | |
| Berkeley County, SC | 988.5 | 86.8 | **901.7** | 776.5 | | |
| New Albany, OH | 1,008.1 | 172.4 | **835.7** | 352.7 | | more than doubled |
| Papillion, NE | 677.8 | 129.6 | **548.2** | 416.9 | | |
| The Dalles, OR | 654.3 | 185.3 | **469.0** | 361.4 | 302.4 | rated not high risk (2022) |
| St. Ghislain, Belgium | 714.4 | 263.6 | **450.8** | 393.3 | | 686.8 non-potable |
| Montgomery County, TN | 499.5 | 74.8 | **424.7** | 321.8 | | |
| Eemshaven, Netherlands | 532.2 | 126.5 | **405.7** | 330.0 | | 528.6 non-potable |
| Douglas County, GA | 440.6 | 73.5 | **367.1** | 366.9 | | 394.3 reclaimed wastewater |
| Lockbourne, OH | 460.8 | 101.3 | **359.5** | 143.3 | | |
| Lenoir, NC | 378.3 | 34.0 | **344.3** | 327.8 | | |
| Bristow, VA | 359.6 | 92.0 | **267.6** | 84.4 | | |
| **Henderson, NV** | 401.7 | 162.3 | **239.4** | 207.4 | 158.8 | rating not published |
| Midlothian, TX | 263.6 | 43.4 | **220.2** | 182.3 | | |
| Sterling, VA | 258.4 | 58.6 | **199.8** | | | |
| Leesburg, VA | 238.1 | 47.4 | **190.7** | 191.6 | | |
| Omaha, NE | 241.8 | 57.9 | **183.9** | 32.1 | | |
| Jackson County, AL | 191.0 | 17.4 | **173.6** | 182.8 | | |
| **Quilicura, Chile** (Santiago) | 278.2 | 135.2 | **143.0** | 121.8 | | water-cooled, Santiago basin |
| Lancaster, OH | 307.1 | 171.3 | **135.8** | 101.1 | | |
| Inzai, Japan | 94.6 | 21.4 | **73.2** | 18.2 | | |
| Fredericia, Denmark | 88.8 | 17.0 | **71.8** | 37.8 | | |
| Ashburn, VA | 76.5 | 23.3 | **53.2** | 56.0 | | |
| Red Oak, TX | 67.0 | 16.6 | **50.4** | | | |
| New Haven, IN | 62.2 | 24.4 | **37.8** | | | |
| **Mesa, AZ** | 19.4 | 9.7 | **9.7** | not listed | | NOT footnoted air-cooled |
| Middenmeer, Netherlands | 13.6 | 4.3 | **9.3** | 6.5 | | |
| Storey County, NV | 66.7 | 60.0 | **6.7** | | | air-cooled (endnote 233) |
| Hanau, Germany | 3.4 | 1.5 | 1.9 | 0.6 | | |
| Hamina, Finland | 4.3 | 3.9 | 0.4 | 0.3 | | seawater cooling |
| Wilmer, TX | 2.6 | 2.3 | 0.3 | | | air-cooled |
| Frankfurt; Sydney; Dublin; Montreal; Pflugerville TX; Phoenix AZ; San Bernardo, Chile; Winschoten | 0.05 to 1.4 | | 0.05 to 0.2 | | | Dublin, Montreal, Pflugerville, Phoenix, San Bernardo, Sydney marked "Air-cooled facility" |
| Other data center locations | 1,020.3 | 101.1 | **919.2** | | | includes 523.8 reclaimed, 479.1 non-potable |
| **Data centres total** | 13,562 | 3,039 | **10,523** | 7,787 | | |

Findings from the table:

- **Mesa** consumed 9.7 Mgal (36.7 ML) in 2025, its first listed year. [primary] Under the claim's 50 Mgal line by a factor of five. But Mesa is **not** marked "Air-cooled facility" in 2026 (endnote 226 applies to Dublin, Montreal, Pflugerville, Phoenix, San Bernardo, Storey County, Sydney, Wilmer; Mesa has no endnote), and it withdrew 19.4 Mgal against Phoenix's 0.5. [primary] Possible explanations (construction water, humidification, adiabatic assist on hot days) are unpublished. [could not verify]
- **Waltham Cross and Canelones do not appear by name** in the 2025 table. [primary] If they are operating, they sit inside "Other data center locations" (919.2 Mgal consumed). The claim's first limb cannot be tested at those two sites until Google lists them.
- **Henderson** consumption rose 158.8 → 207.4 → 239.4 Mgal (2023 to 2025), +51% in two years. [primary, calc] Its PUE is 1.09 (2025). Google publishes no rating of its source.
- **Quilicura (Santiago)**: Google's existing Chilean campus is water-cooled and consumed 143.0 Mgal in 2025, in the same Santiago basin where Google redesigned its Cerrillos project to air cooling (section 4). [primary for the numbers; the basin link is mine]
- Reclaimed and non-potable supply concentrates in a few sites: Douglas County (89% reclaimed), Eemshaven (99% non-potable), St. Ghislain (96% non-potable). [calc]

### 1.4 What Google says about siting by water risk [primary]

- 2025 report, pp.40 to 41: Waltham Cross water sources "present a high risk of water depletion and scarcity", so Google "decided to utilize air cooling technology at this site". "We're taking a similar approach in other areas identified as having high water risk through our framework, such as our facilities under development in Mesa, Arizona and Canelones, Uruguay."
- Google blog, 15 Dec 2023, Ben Townsend: "If it's high risk, we will pursue alternative sources or cooling solutions" (per the existing sidecar; not re-opened).
- **New, 3 June 2026**: Google blog "Google's water stewardship commitments for local communities", Bikash Koley and Ben Townsend (https://blog.google/company-news/outreach-and-initiatives/sustainability/new-water-stewardship-commitments/). Five commitments: replenish "more water than we consume at our sites" by 2030; over US$500 million for water, wastewater and reuse infrastructure; "Protect at-risk watersheds with air-cooled solutions": "If a water source is at high risk, we choose air cooling or recycled water", and Google will "only consider water cooling if local resources are healthy and resilient"; report annual water use; pursue reclaimed water (Douglas County, Georgia named). Also: "In many places, water cooling can reduce data center energy use by approximately 10% compared to air cooling." [primary]
- Note: "air cooling **or recycled water**". A high-risk site cooled by evaporating recycled water would be consistent with Google's policy. The claim's limb 2 ("drawing on a water source it rates at high risk") arguably does not catch it, because the source would be the reclaimed supply. The piece should say so.
- Visakhapatnam, India: Google says its watershed assessment led to air cooling for the planned AI campus. [press, techenclave; Google's own statement not opened]

### 1.5 Replenishment [primary]

- 2025: 7,717 Mgal replenished, **78% of 9,947 Mgal freshwater consumption**; 165 projects in 97 watersheds; capacity 19,722 Mgal in 2030 once built (2026 report pp.37, 96).
- Series (2026 report p.96): replenished 271, 1,036, 4,590, 7,717 Mgal for 2022 to 2025; 6%, 18%, 63%, 78%. The 2025 report had said 64% for 2024; recalculated to 63% (2026 endnote 180). [primary]
- Target: 120% of freshwater consumed, on average across offices and data centres, by 2030 (2026 report p.72). The June 2026 blog adds "at our sites". [primary]
- The Dalles: Google built and transferred an aquifer storage and recovery system to the city in 2025 and says it has invested more than US$28 million in the city's water and wastewater (p.36). [primary]
- Henderson: Google has said its replenishment in the Colorado River Basin exceeded Henderson's freshwater consumption in 2023. [press, KTNV; Google statement not opened]

---

## 2. Microsoft, AWS, Meta

### 2.1 Microsoft [primary]

- **WUE**: 0.49 L/kWh in 2021; **0.30 in FY2024**; **0.27 in FY2025** (fiscal year to 30 June), 25% below the 2022 baseline, target 40% by 2030 (2026 Environmental Sustainability Report p.24; blog 9 Dec 2024). https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Sustainability-Report-PDF.pdf
- **Definition**: the 9 Dec 2024 blog: WUE "divides total annual water **consumption** for humidification and cooling by the total energy consumption for IT equipment". The 2026 report (endnote 12): "the ratio of the yearly amount of datacenter water use (for cooling and humidification) to energy use". So Microsoft's WUE is a cooling and humidification consumption figure, not withdrawal. **The live piece says Microsoft reports withdrawn water; that is wrong on Microsoft's own definition.**
- **Zero-water design** (blog, 9 Dec 2024): "Beginning in August 2024, Microsoft launched a new datacenter design" that evaporates zero water for cooling; "a nominal increase in our annual energy usage"; it "will increase our power usage effectiveness (PUE)", offset by elevated-temperature chillers; avoids "more than 125 million liters of water per year per datacenter" (based on the 0.30 WUE); Phoenix and Mt. Pleasant, Wisconsin pilot in 2026, new sites coming online late 2027; "our current fleet will still use a mix of air-cooled and water-cooled systems". https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/
- 2026 report p.18: chip-level liquid cooling "avoids evaporative cooling altogether by circulating liquid in a closed loop between servers and chillers"; "zonal cooling" sends warmer water to most IT and cooler liquid only to the hottest workloads. Phoenix WUE improved 23% in FY25 after changes to standard cooling systems (p.24). Amsterdam-region site harvests rainwater, expected to collect "more than three times the water annually required for cooling" (p.24).
- 24 June 2026 blog (per existing sidecar): about 90% of the 2025 owned fleet uses "low- to zero-water cooling".
- Fairwater, Wisconsin: more than 90% of capacity on closed-loop liquid filled once at construction; the rest on outside air with water on the hottest days; annual water use likened to a restaurant. [press, multiple outlets reporting Microsoft's September 2025 statements; blog not opened]
- **Company totals** (2026 Data Fact Sheet, Table 8 and 14, ML, all Microsoft, recalculated): withdrawal 11,590 (FY24) and **13,266 (FY25)**; consumption 6,693 and **8,170**; discharge 4,897 and 5,096. FY25 withdrawal from areas with water stress: 6,659 ML, **50% of withdrawals**; consumption in stressed areas 3,926 ML (48%). "Water stress" is the Pacific Institute concept, broader than scarcity. Consumption at offices is assumed at 10% of withdrawal; data centre volumes are estimated from water efficiency metrics since FY24. https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf
- **Per-site FY25 withdrawal** (Fact Sheet Table 15, owned data centres) with my intensity [calc, ML / MWh = L per kWh of facility electricity, withdrawal basis]:

| Site | Electricity MWh | Withdrawal ML | Non-potable share | L/kWh withdrawn [calc] |
|---|---|---|---|---|
| Phoenix, AZ | 954,206 | 981 | none | **1.03** |
| Quincy, WA | 1,381,569 | 1,292 | 74% | 0.94 |
| Singapore | 338,845 | 423 | 99% (NEWater) | 1.25 |
| San Antonio, TX | 1,440,710 | 420 | 79% | 0.29 |
| Boydton, VA | 3,113,847 | 362 | none | 0.12 |
| Des Moines, IA | 2,152,335 | 264 | none | 0.12 |
| Ashburn, VA | 828,925 | 239 | none | 0.29 |
| Cheyenne, WY | 1,091,460 | 188 | none | 0.17 |
| Querétaro, Mexico | 6,362 | 19 | none | (ramping) |
| Dublin, Ireland | 1,308,581 | 18 | none | 0.01 |
| Hollands Kroon, NL | 1,291,170 | 46 | none | 0.04 |

  Phoenix, a desert site, is Microsoft's most water-intensive owned site per kWh and draws no non-potable water. [calc] It is an existing site, not a new one.
- Replenishment: over 14.2 million m3 in FY25, "for the first time" more than global withdrawals; target now set against withdrawal, not consumption (2026 report p.24). [primary]

### 2.2 AWS [primary]

AWS 2025 Sustainability Summary, pp.3, 8: https://sustainability.aboutamazon.com/2025-aws-summary.pdf

- **WUE** "the liters of water **withdrawn** per kilowatt-hour (kWh) of IT load": 0.25 (2021), 0.19 (2022), 0.18 (2023), **0.15 (2024)**, **0.12 (2025)**, "a 20% improvement from 2024 and a 52% improvement from 2021". PUE 1.14 (2025).
- 2025 withdrawals: **9.4 billion litres** across leased, owned and shared data centres; "48% ... in regions classified as low water stress, and **22%** ... high or extremely high water stress" (WRI Aqueduct baseline water stress).
- "Where weather permits, we use Direct Evaporative Cooling, which requires water for less than 10% of the year." "In some of our highest water stressed regions, including the Middle East, South Africa, and India, we do not use any water to cool our data centers."
- In-Row Heat Exchanger for AI racks: expected 9% less water than evaporative air-cooled halls once fully operational. Liquid-to-chip cooling cuts mechanical energy "by up to 50% during peak cooling ... without increasing water usage on a per MW basis".
- 130 data centres contracted to use reclaimed water for cooling, in six countries; 31 with on-site water treatment; cooling water cut by 938 million litres in 2025; 75% of the way to "water positive" by 2030 (53% in 2024); 9.4 billion litres returned by active replenishment projects.
- The "industry average 0.84 L/kWh withdrawal" AWS compares itself with is derived from a consumption WUE of 0.56 assuming three cycles of concentration. [press quoting AWS's footnote; not opened in the PDF]
- Chile region (announced 7 May 2025, launch by end of 2026): AWS said the data centres would be "predominantly cooled by air" and use on average less water than two Chilean households a year. [primary: Amazon press release https://press.aboutamazon.com/aws/2025/5/amazon-to-invest-more-than-4-billion-to-launch-infrastructure-region-in-chile ; wording via search excerpts, page not opened in full]
- Aragón, Spain: Aragón's environment agency (INAGA) authorised a 48% increase in AWS's water allowance at El Burgo de Ebro, from 36,461 to 53,961 m3 a year, from the Canal Imperial de Aragón. [press, Xataka; authorisation date not confirmed] The Ebro basin authority (CHE) published Amazon Data Services Spain's Canal Imperial water application in the BOE on 18 June 2025 [primary, BOE-B-2025-22920, not opened]. AWS says its Aragón centres used about 68 million litres in 2025. [press, DCD citing AWS]

### 2.3 Meta [primary]

Meta 2025 Environmental Data Index (2024 data): https://sustainability.atmeta.com/asset/2025-environmental-data-index/

| ML | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|
| Total withdrawal | 3,726 | 5,043 | 4,893 | 5,274 | 5,637 |
| Data centres withdrawal | 3,000 | 3,418 | 3,618 | 3,881 | 4,145 |
| Total consumption | 2,202 | 2,569 | 2,638 | 3,078 | 3,123 |
| Withdrawal from high or extremely high baseline water stress | | 1,390 | 1,130 | 1,360 | 1,704 |
| Consumption in such areas | | 162 | 443 | 504 | 748 |
| **Data centre WUE** (withdrawal / IT kWh) | 0.30 | 0.26 | 0.20 | 0.18 | **0.19** |
| **Embedded water consumption in purchased electricity** | | 31,924 | 41,172 | 55,475 | **72,207** |
| of which for contracted renewables | | 3,313 | 2,895 | 3,810 | 5,075 |
| "Avoided water consumption" | | 28,611 | 38,278 | 51,664 | 67,132 |

- Definition: "Annual WUE is calculated by dividing our water withdrawal, in liters, by IT electricity load, in kWh." [primary]
- 2024: 30% of withdrawals and 24% of consumption were in high or extremely high stress areas. [calc]
- Sites, 2024 withdrawal ML: Clonee 571, Prineville 328, Fort Worth 311, Los Lunas NM 252, Altoona 242, Huntsville 209, Gallatin 205, Stanton Springs GA 146, Sarpy 142, Eagle Mountain UT 133, DeKalb 105, Henrico 92, New Albany 86, **Mesa AZ 57 (first year)**, Kansas City 41, Luleå 29, Forest City 16; leased 883. Construction water (1,019 ML) is excluded. [primary]
- Goal: water positive in 2030, restoring 200% of consumption in high stress regions and 100% in medium (2025 Sustainability Report p.49). [primary]
- New AI campuses: El Paso, Texas: "closed-loop, liquid-cooled", zero water for most of the year; El Paso Water agreement permits 0.75 Mgal/day average initially, 1.5 Mgal/day at build-out [press; Meta's 9 June 2026 letter to El Paso City Council is a primary lead, not opened]. Lebanon, Indiana (1 GW): closed-loop liquid, dry cooling with misting in hot months; allocation could reach 8 Mgal/day by 2031 at peak [press, CNBC 5 Nov 2026]. Talavera de la Reina, Spain: redesigned from water to dry air cooling, cooling water cut to about 600 m3 a year from roughly 200 million litres in the earlier plan [press, iagua, El Español; declaration of environmental impact not opened].

### 2.4 Side by side

| | Measure | Value | Year |
|---|---|---|---|
| Google | consumption per kWh of data centre electricity | about 0.94 L [calc, understated] | 2025 |
| Microsoft | WUE, cooling and humidification consumption per IT kWh | 0.27 L | FY2025 |
| Meta | WUE, withdrawal per IT kWh | 0.19 L | 2024 |
| AWS | WUE, withdrawal per IT kWh | 0.12 L | 2025 |
| LBNL, all US data centres | site consumption per IT kWh, modelled | just over 0.36 L | 2023 |

Do not rank these; the numerators differ. What the table shows honestly: Google chooses evaporation where water is rated plentiful and says so, and the others report numbers that partly reflect direct evaporative or air systems used only on hot days.

---

## 3. The power station's water

- **LBNL** (Shehabi et al., December 2024, printed pp.55 to 57; PDF https://escholarship.org/content/qt32d6m0d1/qt32d6m0d1.pdf, re-read 7 Nov 2026) [primary]:
  - Direct: US data centres consumed 21.2 billion litres in 2014 and **66 billion litres in 2023**; hyperscale and colocation were 84% of 2023's total; hyperscale alone 60 to 124 billion litres by 2028.
  - Indirect: "The total indirect water footprint of U.S. data centers is nearly 800 billion liters", on 176 TWh; "national average of **4.52 L/kWh** of indirect water consumption"; the all-US average is 4.35 L/kWh.
  - Method: EIA 930 interchange, EIA 923 generation, EIA water data and EPA GHG, by balancing authority (Siddik et al. 2024). The text names "hydroelectric reservoirs lose water through open surface evaporation" as consumption, so reservoir evaporation is in scope of the method. The method "does not incorporate any power purchase agreements ... or on-site 'behind the meter' generation".
  - Ratio 800 / 66 = **12.1** [calc].
  - p.47: "Some hyperscale facilities report WUE values for similar systems of 0.1-0.3 L/kWh."
- **Generation water by type** (NREL, Macknick et al. 2012, Environmental Research Letters, operational consumption medians) [background]: nuclear with cooling tower about 672 gal/MWh (**2.5 L/kWh**); coal with tower about 687 gal/MWh (2.6 L/kWh); gas combined cycle with tower about 198 gal/MWh (**0.75 L/kWh**); dry-cooled gas about 2 gal/MWh; wind and solar PV close to zero. Hydropower reservoir evaporation, where counted, is far higher per kWh than any of these. Values via search excerpts of the NREL/NETL tables; paper not re-opened.
- **Meta's own embedded water** [primary, calc]: 72,207 ML in purchased electricity in 2024 against 3,123 ML consumed directly by the whole company, **23 to 1** on a location basis. Counting only the water embedded in its contracted renewables, 5,075 ML, the ratio falls to **1.6 to 1**.

**Is "most of a data centre's water is at the power station" right?** On LBNL's location-based national average, yes: about twelve to one in 2023. But three qualifications belong in the piece:
1. It is a grid-mix average, and it includes reservoir evaporation at hydro plants, whose water serves many purposes. A data centre on a gas or nuclear grid with tower cooling has power-station water of roughly 0.75 to 2.5 L/kWh, not 4.5.
2. It ignores contracts. On Meta's own market-based figure, embedded water is only 1.6 times direct use.
3. The power station's water is usually in another basin, often river or once-through water. A town sees the site's draw, not the plant's. "Most" is true nationally and on paper; it does not answer the local question.

Suggested wording: "On the lab's grid-average accounting, about twelve litres evaporate at power stations for every litre on site; how much of that is really the data centre's depends on its power contracts and its grid."

---

## 4. Towns and regulators, dated

| Place | What happened | Date | Tag and source |
|---|---|---|---|
| **Tucson, Arizona (Project Blue)** | City council ended negotiations over annexation after opposition on water and power (vote reported as unanimous) | 6 Aug 2025 | [press] KVOA, Copper Courier |
| Tucson | Ordinance for users above 7.4 Mgal a month: water service application and conservation plan, council approval, plan updated every five years, use capped at 120% of application, penalty charges up to 2,000%; cost of connecting to reclaimed water must be shown if within one mile | passed about 19 Aug 2025 | [press] KTAR 21 Aug 2025; ordinance text not opened |
| Project Blue moves to Pima County land | Renewed county agreement (December 2025) requires a **closed-loop air-cooled** system and water rights through ADWR; Amazon left the project; Beale continues | Dec 2025 | [press] AZ Luminaria, KJZZ |
| Project Blue power | Arizona Corporation Commission approved TEP's energy supply agreement, 4 to 1; reported 286 MW; supply from about 1 May 2027; AG Mayes appealed | 3 Dec 2025 | [press] AZ Capitol Times, AZPM; ACC order not opened |
| Project Blue water | ADWR approved wells for an affiliate, up to 96.5 acre-feet (about 31 Mgal) a year; Tucson revoked a construction water meter and demanded 2 acre-feet back | May 2026 | [press] AZPM, Tucson Sentinel, KJZZ 12 May 2026 |
| Pima County | 120-day moratorium on new data centre projects not yet permitted, 3 to 2 | Sep 2026 (KJZZ 23 Sep) | [press] |
| Marana, Arizona | Town will not supply potable water to data centres for cooling or humidity control (December 2024); Ordinance 26-09 requires special use authorisation with water plans (April 2026) | Dec 2024; Apr 2026 | [press, CRS and Public Affairs Council citing the ordinances] |
| Arizona | AG Mayes asked for a statewide pause on new hyperscale approvals; not law | 31 Aug 2026 | [press] AZFamily |
| Pinal County, Arizona | La Osa rezoning refused 4 to 1 despite closed-loop pledge (in the live piece) | 26 Aug 2026 | [press] |
| **Southern Nevada** | No new commercial or industrial building permits with evaporative cooling; applications closed September 2023, permits ended February 2024; closed-loop or air-only designs still allowed | 2023 to 2024 | [press] Las Vegas Review-Journal, Boulder City Review, KTNV; SNWA or LVVWD rule text not opened |
| **Chile, Santiago (Cerrillos)** | Second Environmental Court partly annulled the permit (aquifer and climate) | 26 Feb 2024 | [primary] ruling R-271-2020 |
| Cerrillos | Google dropped the original permit and said it would restart with air-cooled chillers | Sep 2024 | [press] Meganoticias, CNN Chile, BNamericas |
| Cerrillos | SEA cleared the redesigned air-cooled project through a "pertinencia" ruling under new SEIA rules, without a new environmental assessment | reported 19 Oct 2026 | [press] El Desconcierto; SEA resolution not located |
| **Uruguay, Canelones** | After the 2023 drought Google "redefined" the size and switched to air cooling; foundation stone laid in Parque de las Ciencias (29 Aug, 2024 per coverage) | 2023 to 2024 | [press] DCD; Uruguay ministry note (gub.uy) not opened |
| **Netherlands** | National restriction on new hyperscale (over 70 MW and 10 ha) outside two designated areas, one being Hollands Kroon; Vitens will not connect new data centres in its area; PWN says drinking water has legal priority | 2022 to 2026 | [press] DCD; Rijkswaterstaat news July 2026 (primary lead, not opened) |
| **Ireland** | Water Conservation Order 24 Jul to 26 Aug 2026; a TD reported data centre public-supply use more than doubled in hot months across 57 connected sites; no data-centre-specific water rule; CRU Large Energy Users policy (electricity) | Jul to Aug 2026 | [press] Dublin People |
| **Spain, Aragón** | 48% water allowance increase for AWS El Burgo de Ebro; CHE favourable on Villanueva de Gállego with storage of two months' autonomy | 2025 to 2026 | [press]; BOE notice primary, not opened |
| **Spain, Talavera** | Meta redesigned to dry air cooling; regional government says no water objection | 2024 to 2026 | [press] |
| **Malaysia, Johor** | DCTF will not consider areas with low water reserve margin; two days' on-site storage; 12 MLD reclaimed water to Johor data centres; data centre tariff RM5.30 to 5.38/m3 (Johor RM5.33) from 1 Aug 2025; Johor reserve margin 14.3% (2025) | 24 Jun and 28 Oct 2026 (Hansard) | [primary] Hansard DR-24062026, DR-28102026; SPAN 2025; tariff [press]. Full detail: `research-build/topics/johor-research/malaysia-power.md` rows 33, 34, 63 to 71 |
| Johor state guideline | PUE 1.4 and WUE 1.8 benchmarks | | [press only; no state document located] |
| **Singapore** | 2019 pause justified by "land, water, and energy"; capacity rationed on PUE 1.25; Microsoft's Singapore site draws 99% non-potable (NEWater) | 2022, FY25 | [primary] EDB/IMDA 20 Jul 2022; Microsoft Fact Sheet Table 15 |
| **Querétaro, Mexico** | Microsoft bought an existing groundwater concession of 25 million litres a year for one Colón unit; aquifer (Valle de San Juan del Río) in deficit; Microsoft says outside air cools about 95% of the year | Sep 2024 | [press] Thomson Reuters Foundation. Microsoft FY25: Querétaro 19 ML withdrawn, 6,362 MWh [primary] |
| **Georgia** | Forsyth County bars data centre cooling on the county water system; DeKalb moratorium extended to early 2027 with watershed rules; Coweta referendum push; HB 1059 statewide moratorium bill (status unconfirmed) | 2025 to 2026 | [press] GPB, Appen Media |
| **Virginia, Loudoun** | Data centres are 9% of Loudoun Water potable use on an average day; over 750 Mgal of reclaimed water to about 40 customers in 2025; special exception process for water impacts from March 2025 | 2025 | [primary] Loudoun County "Data Centers: Water Considerations" page |
| Virginia, Prince William | QTS Digital Gateway terminated (litigation and opposition; not water-specific) | 2026 | [press] |
| Ypsilanti, Michigan | Water and sewer moratorium for data centres (in the live piece) | 22 Apr 2026 | [primary] YCUA Resolution 26-08 |
| Port St. Lucie, Florida (Project Jarvis) | 1 GW campus withdrawn after the planning board demanded a public water impact study | Feb 2026 | [press, aggregator]; power status unknown |
| US ballots | Voters passed 40 of 41 local measures restricting data centres "this week" | Nov 2026 | [press] CNBC 5 Nov 2026; measures not itemised |

### Claim limb 3: any power-secured campus cancelled outright over water?

- **None found with both conditions met on primary evidence.**
- Project Blue is the clearest test case and it **supports** the claim: water opposition ended the city route, the project redesigned to closed-loop air cooling and moved to county land, and its power contract was then approved (3 Dec 2025). It is redesigned, not cancelled (though Amazon left).
- Cerrillos (Google, Chile), Canelones (Google, Uruguay) and Talavera (Meta, Spain) were all **redesigned to air cooling**, not cancelled.
- Candidates to watch: Project Jarvis (withdrawn after a water study demand; no evidence power was secured), Pinal County's La Osa (refused at rezoning, no end user), Wake County and San Marcos (press). None is a hyperscaler campus with power secured on the record.

### Redesigned to dry cooling (evidence the trade works)

Cerrillos; Canelones; Waltham Cross (designed air-cooled); Mesa (Google says air-cooled); Project Blue; Talavera; AWS Chile region (predominantly air); Microsoft's zero-water designs (all new from August 2024); Meta El Paso and Lebanon (closed-loop, water only on hot days).

---

## 5. How water is priced and permitted

- **Arizona** [background, with press]: groundwater inside Active Management Areas (Phoenix, Tucson, Pinal and others) needs a right or permit from ADWR; industrial users can get non-irrigation rights or buy from a municipal provider. Outside AMAs pumping is largely unregulated (the "loophole" press flags). Project Blue's affiliate got ADWR approval for wells of up to 96.5 acre-feet a year [press]. Cities set their own terms: Tucson's large-user ordinance, Marana's potable ban for cooling [press]. In June 2026 Governor Hobbs signed a three-year moratorium on new sales-tax breaks for data centres [press, KJZZ].
- **Texas** [press]: the Texas Water Development Board's initial 2027 State Water Plan (approved 23 July 2026) has no data centre demand forecast; it refused a petition to add one, citing limited data. No law requires data centres to report water. HARC estimates 25 billion gallons in 2025 and up to 161 billion by 2030 (research group, not the state). Groundwater follows the rule of capture, moderated by local groundwater conservation districts [background].
- **Virginia, Loudoun Water** [primary, Loudoun Water board presentation, 10 Oct 2024; rates proposed, adoption at the 14 Nov 2024 hearing not verified]: commercial potable usage rates per 1,000 gallons, current then 2025, 2026, 2027: Tier 1 (within reserved capacity) $3.86, $4.13, **$4.42**, $4.73; Tier 2 (above reserved capacity) $6.63, $7.09, **$7.59**, $8.12. **Reclaimed water $1.80, $1.93, $2.07, $2.21**, priced on the cost of the Broad Run Water Reclamation Facility, rising 7% a year. A sample "Data Center" bill (346.97 ERCs) of $13,190 a quarter rising to $16,149 by 2027. Reclaimed water is a little under half the Tier 1 potable price. [calc] https://www.loudounwater.org/sites/default/files/2025-08/Board%20-%202024%20User%20Rates%20Reclaimed%20Water%20Rates%20Avilability%20Charges%20and%20Other%20Fee%20and%20Charges%20-%20Presentation%20-%20Carnes%20-%20Oct%2010%202024.pdf
- **Malaysia**: special data centre water tariff RM5.30 to 5.38/m3 from 1 August 2025 [press], about US$4.8 to 4.9 per 1,000 gallons at RM4.2 to the dollar [calc, exchange rate assumed]. Capital contribution rules from 1 September 2025 [press].
- **Reclaimed and non-potable shares disclosed** [primary, calc]: Google data centres 2025, 6.8% reclaimed and 12.5% non-potable of withdrawal; Microsoft FY25: Quincy 74%, San Antonio 79%, Singapore 99% non-potable; AWS: 130 data centres contracted for reclaimed water (no volume share); Meta: 515 ML "recycled" water in 2024 (definition not checked).

---

## 6. What cuts against the claim in 2026

1. **Henderson, Nevada**: Google's evaporatively cooled campus (press) consumed 239.4 Mgal in 2025, up 51% in two years, drawing on Colorado River water via Lake Mead (press, Las Vegas Valley Water District spokesperson). Google has never published its rating of the source. Southern Nevada banned evaporative cooling in new buildings from 2024, which tells you how the regional regulator rates it. It is an existing campus, opened 2020, so it does not break limb 2 ("new"), but it is the hardest fact the piece must face, and the piece should say so plainly.
2. **Quilicura, Santiago**: water-cooled, 143.0 Mgal consumed in 2025, in the basin where Google redesigned Cerrillos to air. Existing campus, opened 2015; same logic as Henderson.
3. **Microsoft Phoenix** (981 ML withdrawn FY25, 1.03 L/kWh, no non-potable) and **Meta Mesa** (57 ML in 2024, Meta's first year there) sit in desert basins. Both are existing or pre-claim. Meta does not say how Mesa is cooled or how it rates the source per site. [could not verify]
4. **AWS and Meta's ordinary practice**: AWS uses direct evaporative cooling "where weather permits" and 22% of its withdrawals are in high or extremely high stress regions; Meta 30%. Neither names a site's rating. If either opens a new evaporatively cooled campus in an Aqueduct "high stress" area, a strict reading of limb 2 breaks, but only if the company itself "reports" it, which none does site by site. The limb is hard to break because the disclosures are thin, which a sceptical PM will notice.
5. **Google's own 2026 escape hatch**: "air cooling or recycled water". A high-risk site cooled by evaporating reclaimed water would follow Google's policy and arguably sit outside limb 2.
6. **Mesa not marked air-cooled** in the 2026 table, with 19.4 Mgal withdrawn. Still far under 50 Mgal consumed.
7. **Peak water**: Meta Lebanon's allocation could reach 8 Mgal/day by 2031 on the hottest days (press); UC Riverside's preprint puts peak-day evaporative demand at 6 to 10 times average (in the live piece). Annual figures, which the claim uses, hide the peak a utility must build for.

---

## What the live piece has wrong or out of date

1. **Microsoft's WUE is not a withdrawal figure.** The piece's terms section says "Amazon Web Services ... and Microsoft report withdrawn water". Microsoft defines WUE as annual water **consumption** for humidification and cooling divided by IT energy (blog, 9 Dec 2024); the 2026 report says "water use (for cooling and humidification)". AWS and Meta do report withdrawal. Fix: "AWS and Meta divide water withdrawn by IT energy; Microsoft counts water consumed for cooling and humidification." The operators' table row "Microsoft ... Water withdrawn per kWh, average WUE" should read "water consumed for cooling and humidification per IT kWh, owned data centres, fiscal year to June 2025".
2. **Microsoft's fiscal year is certain, not "likely".** The 2026 report says "FY25 global average WUE of 0.27 L/kWh"; FY25 ended 30 June 2025. Drop "most likely".
3. **Siting record row on Waltham Cross, Mesa, Canelones** says Google "chose air cooling at all three". The 2025 report says Waltham Cross is air-cooled and Mesa and Canelones were "under development" with "a similar approach". In the 2026 table Mesa is not footnoted as air-cooled and withdrew 19.4 Mgal; Waltham Cross and Canelones are not listed by name. Fix the row and add that the claim's test at those two sites waits on Google listing them.
4. **Google's policy is now formal and wider.** Since 3 June 2026 Google says: "If a water source is at high risk, we choose air cooling or recycled water." The piece's siting table should cite this, and the claim box should acknowledge the recycled-water path.
5. **"Most of a data centre's water therefore follows its electricity"** is stated as fact. It holds on LBNL's location-based national grid average (12 to 1), which includes hydro reservoir evaporation and ignores power contracts. Meta's own data show 23 to 1 on a location basis but 1.6 to 1 on its contracted renewables. Qualify the sentence (suggested wording in section 3).
6. **Henderson row**: add the trend (158.8, 207.4, 239.4 Mgal for 2023 to 2025) and the Southern Nevada ban on evaporative cooling for new buildings from 2024 (press until the rule text is opened). Keep "Google does not publish its rating".
7. **Santiago row** stops at the February 2024 court ruling. Add Google's September 2024 restart on air cooling (press) and the October 2026 SEA clearance of the air-cooled redesign (press), and the fact that Google's existing Quilicura campus in Santiago is water-cooled (143.0 Mgal consumed, 2025, primary).
8. **Fleet row**: add the 2025 risk split (72% low, 15% medium, 13% high) and replenishment (78% of 2025 freshwater consumption, 7,717 Mgal). Note the 2023 figure was described as "watersheds", later "sources", scope unchanged per Google.
9. **Microsoft fleet facts missing**: 50% of FY25 withdrawals were in water-stressed areas (6,659 ML of 13,266 ML, Pacific Institute definition), and Phoenix withdrew 981 ML at about 1.03 L/kWh. These belong in the investor layer as the counterweight to "zero water" designs.
10. **AWS row**: correct as written (0.12 L withdrawn per IT kWh, 2025). Add the series (0.25 in 2021 to 0.12 in 2025), the 22% high or extremely high stress share and "Direct Evaporative Cooling ... less than 10% of the year".
11. **Meta is missing from the operators' table.** It publishes WUE 0.19 L/kWh (2024, withdrawal) and embedded electricity water. The old sidecar dropped Meta for lack of primary figures; they now exist in the 2025 Environmental Data Index.
12. **Johor link target**: the piece links to "Johor waits on the treatment plant" in the queue piece. Since 28 October 2026 the DCTF formally excludes areas with a low water reserve margin (Hansard), so the linked section needs updating (per `johor-research/malaysia-power.md` item 3).
13. **Claim limb 3 evidence**: the piece should name Project Blue as the live test (water opposition, redesign to closed-loop air cooling, power contract approved 3 Dec 2025, Amazon gone) rather than leave the limb abstract.

## Could not verify

- Google's water risk rating for Henderson, Quilicura or any site other than The Dalles (not high), Waltham Cross, Mesa and Canelones (high).
- Why Mesa withdrew 19.4 Mgal in 2025 and why it carries no air-cooled footnote.
- Whether Waltham Cross and Canelones were operating in 2025 and whether they sit in "Other data center locations".
- Whether LBNL's 4.52 L/kWh includes hydro reservoir evaporation in full (the text names it; the factor tables in Siddik et al. 2024 were not opened).
- The exact NREL factors (672, 687, 198 gal/MWh) against the paper's own tables; values taken from NETL and NREL-derived tables in search excerpts.
- Southern Nevada's evaporative cooling rule text (SNWA or LVVWD) and whether it covers Henderson's own utility.
- The SEA's October 2026 Cerrillos pertinencia resolution; Uruguay's ministry note on Canelones and its cooling; the ACC order on Project Blue; Tucson's ordinance text; Marana's ordinances.
- Loudoun Water's adopted 2026 rates (only the October 2024 proposal was read).
- Meta's site-level cooling at Mesa and its per-site stress ratings; AWS per-site water.
- Microsoft's Fairwater blog of September 2025 (press reports only).
- Whether any power-secured hyperscaler campus has been cancelled outright over water; none found.
- AWS's industry-average footnote (0.84 L/kWh from 0.56 consumption, three cycles of concentration) in the PDF itself.
- Netherlands national hyperscale restriction details and Vitens' connection decision (press and a Rijkswaterstaat lead only).

## Sources opened this session (7 Nov 2026)

- Google 2026 Environmental Report: https://sustainability.google/files/1699a2e19277e478b38a659f00cb38398a836e8c/download-1699a2e1.pdf (pp.35 to 37, 72, 88, 93 to 97, endnotes 77 to 85, 220 to 235)
- Google 2025 Environmental Report: https://www.gstatic.com/gumdrop/sustainability/google-2025-environmental-report.pdf (pp.40 to 42, 110 to 111, endnotes 163 to 177)
- Google 2024 Environmental Report: https://www.gstatic.com/gumdrop/sustainability/google-2024-environmental-report.pdf (water scarcity split and per-site table, p.80)
- Google blog, 3 Jun 2026: https://blog.google/company-news/outreach-and-initiatives/sustainability/new-water-stewardship-commitments/
- Microsoft 2026 Environmental Sustainability Report and 2026 Data Fact Sheet (URLs in section 2.1); Microsoft blog 9 Dec 2024 (URL in 2.1)
- AWS 2025 Sustainability Summary: https://sustainability.aboutamazon.com/2025-aws-summary.pdf
- Meta 2025 Sustainability Report: https://sustainability.atmeta.com/asset/2025-sustainability-report/ ; Meta 2025 Environmental Data Index: https://sustainability.atmeta.com/asset/2025-environmental-data-index/
- LBNL 2024 United States Data Center Energy Usage Report: https://escholarship.org/content/qt32d6m0d1/qt32d6m0d1.pdf (printed pp.47, 55 to 57)
- Loudoun Water board presentation, 10 Oct 2024 (URL in section 5); Loudoun County water page: https://www.loudoun.gov/6402/Data-Centers-Water-Considerations
- Press leads (not for numbers): KTAR 21 Aug 2025 (Tucson ordinance); CNBC 5 Nov 2026; KTNV, Las Vegas Review-Journal (Southern Nevada); El Desconcierto 19 Oct 2026 (Cerrillos); AZ Luminaria, AZPM, KJZZ, Tucson Sentinel (Project Blue); Xataka (Aragón); iagua, El Español (Talavera); Thomson Reuters Foundation (Querétaro); DCD (Canelones, Netherlands); Dublin People (Ireland); GPB, Appen Media (Georgia); Community Impact, E&E News (Texas).
