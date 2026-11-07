# Research slice: THE TRANSFORMER (for "The equipment queue" depth rebuild)

Compiled 7 November 2026. Research notes only: nothing here is drafted onto the site, published or scheduled.

Labels: **primary** = government, regulator, national lab or the company's own release, filing or results. **press** = only found in trade press, a broker note or a third-party transcript. **calc** = my arithmetic. **verify** = found but not opened at source today.

PDFs read in full text today: DOE *Large Power Transformer Resilience* report to Congress (July 2024), DOE *Large Power Transformers and the U.S. Electric Grid* (June 2012), NIAC *Addressing the Critical Shortage of Power Transformers* (June 2024, the copy on cisa.gov is marked "DRAFT // PRE-DECISIONAL"), Siemens Energy Q3 FY2026 earnings release (5 Aug 2026).

Key URLs used repeatedly:
- DOE 2024: https://www.energy.gov/sites/default/files/2024-10/EXEC-2022-001242%20-%20Large%20Power%20Transformer%20Resilience%20Report%207-10-24.pdf
- DOE 2012: https://www.energy.gov/sites/prod/files/Large%20Power%20Transformer%20Study%20-%20June%202012_0.pdf
- NIAC 2024: https://cisa.gov/sites/default/files/2024-06/DRAFT_NIAC_Addressing%20the%20Critical%20Shortage%20of%20Power%20Transformers%20to%20Ensure%20Reliability%20of%20the%20U.S.%20Grid_Report_06052024_508c.pdf
- FRED PPI, electric power and specialty transformer manufacturing (PCU335311335311): https://fred.stlouisfed.org/series/PCU335311335311

---

## 1. What a transformer is and how it works

### Plain terms

A transformer changes voltage. Two coils of copper wire (windings) sit on a shared ring of special steel (the core). Alternating current in the first coil makes a magnetic field that swings back and forth in the core; that field makes a current in the second coil. The ratio of turns between the two coils sets the ratio of voltages. Nothing moves, so a unit can run 40 years or more.

Why step voltage up and down: line losses rise with the square of the current. For the same power, doubling the voltage halves the current and cuts the heat lost in the wire to a quarter (physics; calc). So power stations step up to transmission voltage, and substations step down again for distribution and for safe use.

| Fact | Figure | Date | Source | Label |
|---|---|---|---|---|
| Voltage ladder | Electricity "generally produced at 5 to 34.5 kV and distributed at 15 to 34.5 kV, but transmitted at 115 to 765 kV" | June 2012 | DOE 2012, p.6 fn.21 | primary |
| Why the ladder | Power is generated at relatively low voltage, transmitted at very high voltage "to minimize losses", and provided to end users at low voltages "to enhance safety" | July 2024 | DOE 2024, p.4 | primary |
| Share of US electricity through an LPT | About 90% of electricity consumed in the US passes through at least one LPT | July 2024 | DOE 2024, pp.2, 4 | primary |

### The parts

| Part | What it is | Number | Source | Label |
|---|---|---|---|---|
| Core | Stacked laminations of grain-oriented electrical steel (GOES), rolled so the crystals line up and magnetic flux runs easily along the strip | 80,000 to 120,000 kg (170,000 to 220,000 lb) of core steel in a 300 to 500 MVA unit | DOE 2012, p.13 | primary |
| Windings | Copper conductors, in large units continuously transposed conductor (CTC) copper, wrapped in insulation | Only copper used in LPTs today (aluminium was used in the 1970s and 1980s) | DOE 2012, p.11 | primary |
| Tank and oil | Steel tank holding core and windings in insulating oil, which insulates and carries heat to radiators and fans; ester oil is less flammable but needs a bigger tank | n/a | DOE 2012, p.7; DOE 2024, p.5 | primary |
| Bushings | Insulated plugs carrying the conductor through the tank wall to the line | 2012: HV bushings "often have a long lead time extending up to five months" | DOE 2012, p.9 | primary |
| Tap changer | Switches between winding taps to adjust the ratio a little, holding voltage steady as load changes | n/a (named as a part) | DOE 2012, p.7 | primary |
| Cost split | Raw materials 57% to 67% of LPT cost (2008 to 2010); of material cost, copper 18% to 27%, electrical steel 22% to 24% | 2012 | DOE 2012, p.11 | primary |
| Cost split, later | GOES and CTC copper "each account for roughly 25 percent of final LPT production costs" | 2020 Commerce survey, cited July 2024 | DOE 2024, pp.12, 14 | primary |
| Labour | Labour averages 36% of manufacturing cost (range 1% to 87%); 89% of 87 surveyed component makers reported difficulty finding qualified workers | 2020 Commerce survey, cited July 2024 | DOE 2024, p.16 | primary |
| Overload | LPTs "can be overloaded up to 10 to 20 percent above their rated power, but this accelerates insulation aging" | July 2024 | DOE 2024, p.5 | primary |

### How one is built (DOE's seven steps)

DOE 2012, p.9 (primary): 1 engineering and design; 2 core building ("requires highly-skilled work force"); 3 winding and assembly of core and windings; 4 drying, because moisture degrades insulation; 5 tank production, timed so the dried active part does not reabsorb moisture; 6 final assembly "in a clean environment; even a tiny amount of dust or moisture can deteriorate the performance"; 7 testing (voltage ratios, power ratings, impedances). About 1.3 transformers are produced per design (DOE 2012, p.6, industry source): almost every unit is custom.

Build time vs lead time: DOE 2012 says an LPT needs "a long-lead time (in excess of six months) to manufacture" (p.8). Factory "build slots" are the unit of capacity: "each slot can be used for an LPT, a smaller transformer, or a refurbishment of a transformer core, but capacity cannot easily be expanded except by building a new facility" (DOE 2024, p.14).

### Kinds and sizes

| Kind | What it does | Size | Source | Label |
|---|---|---|---|---|
| Large power transformer (LPT) | Connects big power stations to transmission and shifts between transmission voltages | 100 MVA or more (DOE definition); typically 115 kV or more on the high side; extra-high voltage is 345, 500, 765 kV | DOE 2024, p.2; DOE 2012, pp.4-5 | primary |
| Generator step-up (GSU) | Steps a power station's output (5 to 34.5 kV) up to transmission voltage | 2012 examples: 345 to 13.8 kV, 300 MVA; 765 to 26 kV, 500 MVA | DOE 2012, p.7 Table 2 | primary |
| Substation / medium power | Steps transmission down to sub-transmission or distribution; data centre grid connections usually sit here | 2012 example: 115 to 13.8 kV, 75 MVA, 110 tons | DOE 2012, Table 2 | primary |
| Distribution (pole or pad-mount) | Final step to customer voltage; pole-mounted on the power pole, pad-mounted on the ground in a locked cabinet | kVA scale; 60 to 80 million in US service, over 3 TW installed | NREL TP-6A40-87653 (Feb 2024), via NREL news release; DOE (27 Nov 2024) | primary (NREL figure verify at source; nrel.gov unreachable today) |
| Hyperscale pad-mount | Pad-mount units bought for hyperscale data centres | 1,573 units in 2025 rising to 9,395 by 2030 (forecast) | Wood Mackenzie release, 28 Apr 2026: https://www.woodmac.com/press-releases/data-center-demand-drives-us-electrical-equipment-market-to-$65b-reshaping-industry-dynamics/ | press (consultant) |

### Prices and weights (DOE 2012, Table 2, 2011 estimates, FOB factory; installed cost "about 25 to 30 percent higher")

| Voltage (primary to secondary) | MVA | Approx. price | Approx. weight |
|---|---|---|---|
| 230 to 115 kV | 300 | $2.0m | 170 tons |
| 345 to 138 kV | 500 | $4.0m | 335 tons |
| 765 to 138 kV | 750 | $7.5m | 410 tons |
| 765 to 345 kV | 500 | $4.5m | 235 tons |
| 115 to 13.8 kV | 75 | $1.0m | 110 tons |
| 345 to 13.8 kV (GSU) | 300 | $2.5m | 185 tons |
| 765 to 26 kV (GSU) | 500 | $5.0m | 325 tons |

Weight range: DOE 2012 says "approximately 100 and 400 tons"; DOE 2024 says "typically weigh between 150 and 400 tons" (p.2). So "a 345 kV LPT, 100 to 400 tons" is right in range; DOE's own 345 kV, 500 MVA example is 335 tons.

### Testing, moving and installing

| Fact | Figure | Source | Label |
|---|---|---|---|
| Normal rail limit | "Most railcars have a loading capacity of about 100 tons. Typical LPTs can weigh 2-3 times this limit" | DOE 2024, p.18; same in DOE 2012, p.10 | primary |
| Schnabel cars | "only about 30 of them in North America" (2012). DOE 2024 says "Only about three of these specialized transport cars are available in North America" (p.19). The 2024 line looks like a slip or a narrower class (18 and 20-axle cars); I would keep the dated 2012 figure and not use "three" | DOE 2012, pp.10-11; DOE 2024, p.19 | primary (conflict flagged) |
| Axles | Schnabel cars have 12 to 20 axles; LPTs typically need 18 and 20-axle cars | DOE 2024, p.19 | primary |
| Rail rental | Up to $2,500 a day plus fees (2014) | DOE 2024, p.19 | primary |
| Route clearance | "the clearance process can take nine months to complete" | DOE 2024, p.19 | primary |
| Road | Goldhoffer-type trailers for loads over 100 tons; example shown moving a 500,000 lb LPT | DOE 2024, p.20 | primary |
| Last miles | "the last 5 to 10 miles of transport are particularly expensive and challenging" | DOE 2024, p.12 | primary |
| Logistics cost | 3% to 20% of total LPT cost | DOE 2012, p.11; DOE 2024, p.19 | primary |
| Install from a ready spare, expedited | Teardown 3 days; transport 3 to 10 days (avg 7); place and assemble 3 days; wiring test 3; vacuum 3; oil fill 1; oil settling 5; commissioning test 1; total 3 to 4 weeks | DOE 2024, Table 1, pp.21-22 | primary |
| Shipping | Unit is drained of oil and stripped of radiators and bushings for transport, rebuilt and retested on site | DOE 2012, p.10 | primary |

### Service life and US fleet age

| Fact | Figure | Date | Source | Label |
|---|---|---|---|---|
| Design life | "on the order of 40 years" | July 2024 | DOE 2024, p.5 | primary |
| Average age | 38 to 40 years (2014 DOE estimate); "about 40 years, with some units still in operation after more than 70 years" | July 2024 | DOE 2024, pp.5, 14 | primary |
| Share over 25 years | More than 70% of US LPTs (2014 estimate) | July 2024 | DOE 2024, p.14; DOE 2012, p.iii | primary |
| LPTs in service | 4,900 to 6,799 (DOE 2022 estimate) | July 2024 | DOE 2024, p.4 | primary |
| Distribution fleet age | About 55% of in-service distribution transformers older than 33 years | 27 Nov 2024 | DOE: https://www.energy.gov/node/4847175 | primary |
| Distribution demand to 2050 | Capacity may need to rise 160% to 260% on 2021 levels | Feb 2024 | NREL TP-6A40-87653, via NREL news release and search summary | primary (verify; nrel.gov unreachable today) |

---

## 2. Lead times and prices over time

### Lead times

| When | Unit | Lead time | Source | Label |
|---|---|---|---|---|
| 2010 | LPT, order to delivery | 5 to 12 months US makers; 6 to 16 months foreign; up to 5 years in extremes | DOE 2012, p.9 | primary |
| Pre-COVID | LPT | "possible to place an order for a large transformer with a lead time of less than a year" | DOE 2024, p.12 | primary |
| 2019 to 2023 | Distribution | 3 to 6 months (2019) to 12 to 30 months (2023) | DOE Office of Electricity, Supply chain and market analysis page (undated): https://www.energy.gov/oe/supply-chain-and-market-analysis | primary |
| 2020 to 2022 | Distribution | About 2 to 3 months to about 12 months (+429%) | APPA member survey, Aug 2022 (95 utilities): https://www.publicpower.org/system/files/documents/2022%20Public%20Power%20Distribution%20Transformer%20Demand%20Survey%20Summary%20PUBLIC.pdf | primary (trade body; verify) |
| 2021 to 2024 | Power transformers | About 50 weeks (2021) to 120 weeks average (2024); large substation and GSU units 80 to 210 weeks | Wood Mackenzie, quoted by NIAC June 2024, p.8 | primary report quoting consultant |
| Feb 2024 | LPT, US | "lead times of up to five years" | Siemens Energy release, 14 Feb 2024 | primary |
| Feb 2024 | Distribution | "up to 2 years", about four times pre-2022 | NREL TP-6A40-87653 abstract (OSTI 2309697): https://www.osti.gov/biblio/2309697 | primary |
| July 2024 | LPT | "36-month lead times being commonly quoted and maximum lead times reaching as much as 60 months" | DOE 2024, p.2 | primary |
| Q2 2025 | Power transformers | 128 weeks average, down 10 weeks; GSU about 143 to 144 weeks | Wood Mackenzie (15 Oct 2025, in live piece) | press (consultant) |
| Q2 2025 | Distribution | About 30 weeks, down from over 100 in 2023 | Wood Mackenzie via CRS, via secondary sites | press (verify) |
| Jan 2026 | Large transformers, Hitachi Energy | "waiting times of up to 40 months"; "The gap between demand and supply is not really closing" (CEO Andreas Schierenbeck to S&P Global) | S&P Global Platts, reposted; original not opened | press |
| Q1 2026 | GSU | Over 160 weeks (Wood Mackenzie data, Reuters 9 Jul 2026) | Only via a blog citing Reuters | press (unverified; do not use) |
| Apr 2026 | Critical data centre electrical components generally | 18 to 36 months; makers "reportedly seeking 20% price increases on older purchase orders" | Wood Mackenzie release, 28 Apr 2026 | press (consultant) |

Note: no maker publishes a list lead time for complete large transformers. The Hitachi Energy components page (bushings 135 weeks, Ludvika) is the only public maker-quoted wait I know of; that sits in the parts slice.

### Prices

| Measure | Figure | Source | Label |
|---|---|---|---|
| US producer price index, electric power and specialty transformer manufacturing (Jun 1981 = 100) | Feb 2020 256.2; Jan 2021 262.0; Jan 2022 356.3; Jan 2024 428.6; Jan 2025 433.2; Jun 2026 456.6; Jul 2026 474.8; Sep 2026 475.1 (latest) | BLS via FRED PCU335311335311 | primary (recent months preliminary) |
| Change Feb 2020 to Sep 2026 | +85% | from above | calc |
| Change Jan 2021 to Jan 2022 (the jump year) | +36% | from above | calc |
| Change Jun to Jul 2026 | +4.0% in one month | from above | calc |
| NIAC's reading | "Transformer prices are 80 percent higher since the beginning of the pandemic" (FRED index chart) | NIAC June 2024, p.8 | primary. My calc on PCU335311335311 gives +67% Feb 2020 to Jan 2024, so NIAC may have used a different sub-index or month; cite NIAC's words, or use my PPI calc, not both |
| Unit costs since 2019 | Power transformers +77%; GSU +45%; distribution +78% to 95% | Wood Mackenzie opinion, 13 Aug 2025: https://www.woodmac.com/news/opinion/transformer-troubles-manufacturing-and-policy-constraints-hit-us-transformer-supply/ | press (consultant) |
| Distribution prices | "Up to 5 to 6 times higher over the past 2 years" (abstract wording as fetched) | NREL Feb 2024, OSTI abstract | primary (verify wording in PDF) |
| 2010 price level | $2m to $7.5m FOB for 75 to 500 MVA | DOE 2012, p.7 | primary |
| Grain-oriented steel price | "Prices have reached all-time highs since the COVID-19 pandemic" | Wood Mackenzie, 13 Aug 2025 | press |

So "prices up 60% to 80% since 2020" is safe if said as: the government's producer price index for transformer makers is up about 85% from February 2020 to September 2026 (calc), most of it in 2021 and 2022.

### Shortage gauges

| Gauge | Figure | Source | Label |
|---|---|---|---|
| Power transformer supply deficit, 2025 | 30% (distribution 6%) | Wood Mackenzie, 13 Aug 2025 | press |
| 2026 | Power transformers about 15% short, substations about 8%; 100 MVA+ segment "most acute" | Wood Mackenzie release, 31 Aug 2026 | press |
| Demand growth since 2019 | Power transformers +116%; GSU +274%; distribution +30% to 80% | Wood Mackenzie, 13 Aug 2025 | press |
| Market growth | Power transformer market above 10 MVA up nearly 300% since 2020 | Wood Mackenzie, 31 Aug 2026 | press |
| US demand (units) | About 750 new units over 60 MVA in 2019; about 900 a year expected by 2027; US makers reported demand jumps "as much as 70 percent year-over-year" in the last 1 to 2 years | DOE 2024, p.13 | primary |
| Siemens Energy's estimate | Demand for large and medium power transformers in Europe and North America about 40% over all makers' capacity in FY2025, about 10% in FY2030 | Siemens Energy CMD, 20 Nov 2025 (in live piece) | primary |

### Import dependence

| Fact | Figure | Date | Source | Label |
|---|---|---|---|---|
| LPT imports | 617 of 754 LPTs for US use imported (82%); 137 made domestically (18%); 4 exported | 2019 (Commerce 2020) | DOE 2024, pp.4, 14 | primary |
| Domestic LPT capacity | About 343 LPTs a year maximum, at about 40% utilisation | 2019 (Commerce 2020) | DOE 2024, p.14 | primary |
| Over 60 MVA | "Over 80 percent of these new units were imported" | 2019 | DOE 2024, p.13 | primary |
| Domestic share | "only 20%" of US LPT demand met domestically | 14 Feb 2024 | Siemens Energy release | primary |
| Goal | NIAC recommends domestic LPT production reach 50% by 2029, from about 20% | June 2024 | NIAC, p.16 | primary |
| Latest consultant view | About 80% of power transformers and about 50% of distribution transformers imported | 13 Aug 2025 | Wood Mackenzie | press |
| GOES imports | "Approximately 80 percent of GOES was imported in 2019"; by form: uncut rolls 20%, pre-cut laminations 88%, stacked cores 80%, wound cores 100%, complete LPTs 82% | 2019 (Commerce 2020) | DOE 2024, p.15 | primary. Note DOE also says imported GOES rolls "hovers around 20 percent": the 80% is all forms, the 20% is uncut rolls only |
| Antidumping | Antidumping duty order on large power transformers from Korea since 2012 (USITC 731-TA-1189); still under annual review (Hyundai and Iljin mandatory respondents, 2024-25 review initiated 25 Sep 2025) | 2012 to 2026 | Federal Register 2026-02646 and 2026-22343 | primary (margins not read) |
| Tariffs on steel parts | Commerce added GOES laminations and cores to the Section 232 steel derivative list at 50% on the steel content, 19 Aug 2025 | Aug 2025 | Cleveland-Cliffs release (interested party), Business Wire 17 Aug 2025 | press-grade (verify in the Federal Register notice) |

### The steel

| Fact | Figure | Source | Label |
|---|---|---|---|
| Sole US GOES maker | "Cleveland-Cliffs (through its 2020 acquisition of AK Steel) is the sole active domestic GOES supplier" | DOE 2024, p.15 | primary |
| Its share | Able to meet 12% to 20% of domestic GOES demand, "but is not currently profitable" (DOE 2022 and Commerce 2020) | DOE 2024, p.15 | primary (dated: 2020-22 data) |
| Top grade | Highest grade (PDR, domain-refined) only from Nippon Steel, Japan; not made in the US | DOE 2024, p.15 | primary |
| Others | ATI stopped GOES in 2016 (imports +155% next year); US Steel's Big River could make GOES but makes non-oriented steel for EV motors instead | DOE 2024, pp.15-16 | primary |
| DOE verdict | Domestic GOES "is a major weak link in the LPT supply chain" (DOE 2022) | DOE 2024, p.14 | primary |
| Expansion | $200m Butler Works project, up to 25% more GOES output by early 2028, with a $75m DOE award | Cleveland-Cliffs release 5 Oct 2026 (in live piece); one report says DOE's schedule shows 2029 | primary; 2029 point press |
| Cancelled plant | Cliffs dropped its $150m Weirton, West Virginia distribution transformer plant (announced Jul 2024, due H1 2026) with its Q1 2025 results, citing "changes in scope from the project partner" | May 2025, Crain's Cleveland, Weirton Daily Times | press (the July 2024 plan is Cliffs' own release) |
| Amorphous steel | Lower-loss core, but brittle; installed base about 600,000 US units vs 1.1m China, 1.3m India; Metglas the only US producer; not generally used in LPTs | DOE 2024, p.16 | primary |
| Efficiency rule | DOE final rule (22 Apr 2024): compliance from 23 Apr 2029; DOE says it can be met with about 75% of distribution transformer steel staying GOES (the 2023 proposal implied about 95% amorphous) | Federal Register 2024-07480; DOE statements via trade press | primary rule; 75% figure verify in rule text |
| Rule under review | 2026 DOE notice asking whether the transformer efficiency rules threaten national security, and about GOES and amorphous supply | Federal Register 2026-11971 (via policyrisk.com) | verify |

---

## 3. Makers: capacity and backlogs (latest primary)

| Maker | Latest backlog / orders | Date | Capacity moves | Source | Label |
|---|---|---|---|---|---|
| Hitachi Energy | $66.9bn backlog (+16% vs end FY2025); about 3.1 years of trailing revenue (calc in sidecar) | 30 Sep 2026 (results 28 Oct 2026) | US programme now "around $1.5 billion" (release body) / "more than $1.5 billion" (summary), up from "more than $1 billion" in Jun 2026; over $6bn group factory spend 2024-27 | Hitachi Q2 FY2026 results; Hitachi Energy releases 29 Jun and 15 Sep 2026 | primary |
| Siemens Energy, Grid Technologies | Q3 FY2026 orders €5,367m, revenue €3,624m, book-to-bill 1.48, backlog €51bn; 9M orders €18,328m, revenue €9,744m; "major contribution came from the substantial growth in the transformer business including data center projects"; revenue growth "supported by expanded production capacities" | 30 Jun 2026 (release 5 Aug 2026); FY2026 results not yet out on 7 Nov | FY2026 Grid outlook: comparable revenue growth 25% to 27%, margin before SI 18% to 20% | Siemens Energy Q3 FY2026 earnings release, pp.3-4 | primary |
| GE Vernova, Electrification (now includes Prolec GE) | Q3 2026 orders $5,371m (organic -9%, against big synchronous condenser orders a year earlier); revenue $3,862m (+51%, +16% organic, incl. $945m from acquisitions); book-to-bill about 1.4; equipment backlog $42.2bn, +$15.7bn (+60%) y/y, incl. $5bn from Prolec GE; EBITDA margin 19.1% | 30 Sep 2026 (release 28 Oct 2026) | $1bn Prolec GE capex 2026-28; FY2026 Electrification revenue guide $14.5bn to $15.0bn incl. about $3.1bn from Prolec GE | GE Vernova 8-K Ex.99: https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm | primary |
| Prolec GE deal | GE Vernova bought Xignux's 50% for $5.275bn, closed 2 Feb 2026; about 10,000 staff, 7 plants in the Americas, 5 in the US | 2 Feb 2026 | Goldsboro NC $140m (announced 14 May 2025): +200 medium power units a year, capacity doubled by 2030; Shreveport LA $34m third line (completed; date unclear) | GE Vernova release 2 Feb 2026 (Business Wire); Prolec GE release on Goldsboro | primary (Shreveport press) |
| HD Hyundai Electric | Q3 2026 orders $0.98bn (-19% y/y); backlog $8.843bn (+4.2% q/q), 68.1% North America; revenue KRW1.18tn | Q3 2026, preliminary | Second Montgomery, Alabama plant: about $200m, +50% extra-high-voltage capacity, adds 765 kV manufacture and testing; ground broken 6 Mar 2026, completion April 2027 | Broker summaries (stockhub.kr, Mirae); company release via Barchart/PR | Q3 press; plant company release |
| Hyosung Heavy Industries | Heavy industries Q3 2026 new orders KRW3.2tn (+122%); backlog KRW18.9tn; US 57% of backlog at Q2 | Q3 2026 | Memphis: $157m to lift capacity over 50% by 2028 (Nov 2025), about $300m invested in total; separate $32.5m 765 kV building (Mar 2026); says Memphis is the only US plant able to design and make 765 kV units | Mirae note via press; company release via PR Newswire (Dec 2025) | press / company PR |
| LS Electric | Backlog about KRW7tn; ultra-high-voltage transformers KRW3.35tn (48%) of backlog at 30 Jun 2026; Q3 North America sales about KRW500bn | Q3 2026 | Plans more North American production (Utah, Texas); Nov 2025 data centre transformer contract about KRW110bn | Korean press | press |
| WEG | n/a | n/a | $77m to raise specialty transformer capacity 50% at Washington, Missouri (23 Sep 2025) | Reuters and Brazilian press | press |
| Virginia Transformer | n/a (private) | n/a | Rincon, Georgia: $40m, about 400 jobs, +50% capacity (earlier "70%"), ground broken Apr 2026, completion March 2027; plant makes 2 to 500 MVA, 150,000 MVA installed capacity; new greenfield power transformer plant in Colbert County, Alabama, 600,000 sq ft, 1,100 jobs at full output (May 2026; no $ figure found) | vatransformer.com releases | primary (company) |
| Eaton | (in live piece: Electrical Americas backlog $16.0bn, 30 Sep 2026) | | Jonesville SC $340m three-phase transformers, 2027 | Eaton releases | primary |
| ABB | Not an LPT maker in the US: sold its power grids business, including transformers, to Hitachi (now Hitachi Energy) | | | general knowledge; cite Hitachi Energy history if used | verify |
| Others in the US | Niagara Power Transformers (Buffalo NY, about +50% after rebuild); Hitachi Energy Alamo TN bushings expansion | Oct 2026 | | Industrial Info Resources, 28 Oct 2026 | press |

### The "3.96 years" check (Siemens Energy)

- Grid Technologies revenue, previous four quarters to 30 Jun 2026: Q4 FY2025 €3,145m (FY2025 €11,305m less 9M FY2025 €8,160m) + 9M FY2026 €9,744m = **€12,889m** (calc; 9M figures primary from the Q3 release p.10; FY2025 from the sidecar's Q4 FY2025 shareholder letter).
- Backlog **€51bn** (release says "increased to €51bn", rounded to €1bn).
- €51bn / €12.889bn = **3.957** (calc). **Verified.** Rounding of the backlog alone moves it between 3.92 and 4.00 (calc), so "about four years" is the honest wording; "3.96" carries false precision.
- Caveat already in the piece and correct: the backlog includes HVDC and is not a quoted lead time.

### GE Vernova, rough years of work (calc, for context only)

Equipment backlog $42.2bn vs Electrification revenue over four quarters of roughly $13.4bn (Q4 2025 about $2.96bn, derived from "orders about $7.4bn, about 2.5 times revenue" in call summaries, plus 9M 2026 $10,459m) = about 3.1 (calc, approximate; denominator includes services revenue and only eight months of Prolec revenue while backlog includes all of Prolec's). Not like for like; use only as "about three years", if at all.

---

## 4. How long a new factory takes, and what has been announced

### Build and qualify

| Fact | Figure | Source | Label |
|---|---|---|---|
| Factory construction | "New factory construction takes 1-3 years" | DOE 2024, p.14 | primary |
| Tooling | "Specialty equipment such as winding machines or core tables can take 1-2 years to obtain from suppliers" | DOE 2024, p.15 | primary |
| Quick fixes | Cranes, air pallets, floor reallocation "can only expand capacity marginally, but at lower cost and quicker" | DOE 2024, p.15 | primary |
| Qualification | Utilities buy from prequalified makers; prequalification "is a lengthy process that can take years" (audit of production and quality, ISO certification, inspection) | DOE 2012, pp.8-9 | primary |
| Test space | Extra test space could ease bottlenecks because LPTs and smaller units share the same plants | DOE 2024, p.17 | primary |

### Announced to first output: dated examples

| Plant | Announced | Output due | Elapsed | Source | Label |
|---|---|---|---|---|---|
| Siemens Energy, Charlotte NC, $150m, LPTs | 14 Feb 2024 | "early 2026" as announced; no company confirmation of first unit found today | 2 yrs planned; slipping | Siemens Energy release | primary. Output 24 units a year rising to 57 at full capacity: Manufacturing Dive (press). 57 units would be about 17% of the 343-unit 2019 domestic maximum (calc) |
| Eaton, Jonesville SC, $340m | 12 Feb 2025 | 2027 | about 2 yrs | Eaton | primary |
| Prolec GE, Goldsboro NC, $140m | 14 May 2025 | double capacity by 2030 | up to 5 yrs | Prolec GE | primary |
| Hitachi Energy, South Boston VA, $457m, LPTs | 4 Sep 2025; ground broken 29 Jun 2026 | "operational by 2028" (spokesperson, press, Sep 2025); production ramp late 2028 or early 2029 (IIR, 28 Oct 2026); no date in Hitachi's releases | about 3 yrs | Hitachi Energy; IIR | primary (no date) / press (date) |
| WEG, Washington MO, $77m | 23 Sep 2025 | not stated | | Reuters | press |
| Hyosung, Memphis TN, $157m | Nov 2025 | 2028 | about 2.5 yrs | company release | primary (PR) |
| Siemens Energy US $1bn programme (Charlotte expansion; Greater Richland MS switchgear) | 3 Feb 2026 | not stated | | Siemens Energy | primary |
| HD Hyundai Electric, Montgomery AL second plant, about $200m | ground broken 6 Mar 2026 | April 2027 | about 13 months (expansion on existing site) | company release | primary (PR) |
| Virginia Transformer, Rincon GA, $40m | Nov 2025; ground broken Apr 2026 | March 2027 | about 16 months | company | primary |
| Hitachi Energy, Gallman MS, $528m (small and medium power transformers up to 230 kV per IIR; replaces nearby Crystal Springs plant, whose production moves there) | 15 Sep 2026 | 2029 | about 3 yrs | Hitachi Energy release | primary (product range press) |

Reading: greenfield large-transformer plants run about 2 to 3 years from announcement to first output (Charlotte, South Boston, Gallman, Jonesville). Expansions on existing sites run 1 to 1.5 years (HD Hyundai, Virginia Transformer). The live piece's "two to three years" holds for new halls; it should say expansions are faster.

### How many plants and dollars since 2022

- No DOE or NEMA tracker with a count was found. NEMA's public material (Sep 2024) welcomes NIAC's recommendations but gives no tally.
- Wood Mackenzie (13 Aug 2025): large transformer makers have announced capacity expansions since 2023 "totaling about US$1.8 billion" (press, consultant).
- Industrial Info Resources (28 Oct 2026): more than $3bn of current and planned construction tracked at US transformer plants, up from about $2bn in Aug 2026 and $1.85bn in Sep 2025 (press, tracker): https://www.industrialinfo.com/iirenergy/industry-news/article/strong-electrical-transformer-demand-drives-us-manufacturing-projects--364208
- My own sum of the dated US transformer-plant amounts above (Charlotte 150, Jonesville 340, Goldsboro 140, South Boston 457, WEG 77, Memphis 157, Montgomery 200, Rincon 40, Gallman 528) is about $2.1bn (calc), excluding undated programme money (Siemens Energy $1bn, Prolec $1bn capex, Virginia Transformer Alabama).

---

## 5. Spares and emergency programmes

| Programme | What it is | Key numbers | Source | Label |
|---|---|---|---|---|
| Utility self-supply | Most transmission owners keep their own spares, often in the same substation, exposed to the same events | n/a | DOE 2024, p.22 | primary |
| STEP (EEI Spare Transformer Equipment Program) | Started 2006; investor-owned utilities must hold and sell spares (up to 500 kV) to each other after a trigger | More than 50 members; $10,000 to join, $7,500 a year; triggers only on a presidentially declared terrorist attack or emergency; "to date STEP has never been utilized"; adds no new capacity | DOE 2024, pp.22-23 | primary |
| SpareConnect | Voluntary EEI-led network to find spares after non-terror events; no guarantee, no new capacity | n/a | DOE 2024, p.23 | primary |
| RESTORE (North American Transmission Forum) | Formal agreement to own, maintain and sell designated spares after a catastrophic trigger; used spares must be replaced within 18 months; buyer pays replacement cost | n/a | DOE 2024, pp.23-24 | primary |
| Grid Assurance | Company founded by AEP, FirstEnergy and Berkshire Hathaway; holds LPTs, breakers and bushings in two secure indoor warehouses | 31 subscribing utilities in parts of 23 states; five transformer classes, seven rating sets; stocked to a 98% chance of meeting modelled needs; units held up to 25 years "like-new"; owns no Schnabel cars; "has not yet actually provided a replacement LPT" | DOE 2024, pp.24-26 | primary |
| Recovery transformers | DHS/EPRI RecX 345 kV, three single-phase modules, energised in under six days (2012), used at one utility; WattStock FLEX swapped a 400 MVA unit in about seven days, programme shelved for lack of funding | | DOE 2024, pp.26-27 | primary |
| Federal reserve | DOE 2017 report to Congress recommended "a non-government solution"; DOE 2024 "does not advocate for a change" | | DOE 2024, p.ii | primary |
| DPA, 2022 | Presidential determination under DPA section 303 that transformers and grid components are essential to national defence, 6 Jun 2022 (FR 9 Jun 2022) | No transformer award found | White House; Federal Register 2022-12587 | primary |
| DPA, 2026 | Presidential Determination 2026-10, 20 Apr 2026 (FR 2026-08013, 23 Apr 2026): grid infrastructure, equipment and supply chain capacity, covering transformers, breakers, substations, conductors and "electrical core steel"; waives section 303(a)(1)-(6) | No projects or funding named as of ENR's report | whitehouse.gov; Foley (Apr 2026); ENR | primary (scope via law firm summary; verify text) |
| NIAC proposals | "Virtual" transformer reserve, standard designs, 50% domestic LPT output by 2029, DPA funding | June 2024 | NIAC | primary |
| Bulk-power order | Executive Order 14421 (DOE's numbering), 26 Aug 2026: lets DOE bar foreign-produced bulk-power equipment in transactions after that date; Wood Mackenzie and several law firms call it 14420 | | DOE: https://www.energy.gov/node/4860229; Wood Mackenzie 31 Aug 2026 | primary (number conflict flagged) |

NERC and FERC: I found no 2025 or 2026 NERC or FERC document that publishes its own transformer lead times; secondary sources say NERC's 2023 LTRA and 2025 summer assessment cite the Wood Mackenzie series. Treat NERC as not a primary source for lead times unless the LTRA text is opened.

---

## What the live piece has wrong or out of date

1. **"3.96" is over-precise.** The arithmetic checks out (€51bn / €12.889bn = 3.957, calc) but the backlog is rounded to €1bn, so the true ratio is anywhere from 3.92 to 4.00. Say "about four years" in the text; keep 3.96 only in the claim, where it is fixed.
2. **Lead times are a year stale.** The newest wait in the piece is Wood Mackenzie's 128 weeks for Q2 2025. Newer: Hitachi Energy's CEO said "up to 40 months" for large transformers in January 2026 (S&P Global, press), and Wood Mackenzie's 2026 shortage is 15% for power transformers (31 Aug 2026; already in the piece). The 160-week GSU figure (Reuters, July 2026) is unverified and should not be used.
3. **No price evidence.** The piece never says prices rose. Primary option: the BLS producer price index for transformer makers is up about 85% from February 2020 to September 2026 (calc from FRED), with a 4% jump in July 2026 alone.
4. **Import dependence missing.** In 2019, 82% of large power transformers for US use were imported and US plants could make about 343 a year (Commerce 2020, via DOE 2024). That is the base the new factories are building from.
5. **"A new hall takes two to three years"** is right for greenfield plants but too broad. DOE (2024) says one to three years, with winding machines and core tables taking one to two years to buy. Expansions on existing sites are landing in about a year (HD Hyundai Montgomery, April 2027; Virginia Transformer Rincon, March 2027).
6. **Gallman is not simply new capacity.** Production moves there from Hitachi Energy's nearby Crystal Springs plant, and per IIR it makes small and medium power transformers up to 230 kV, not large ones. "More than double its current plant's capacity" is Hitachi's own phrase, but the net gain is the increment over Crystal Springs.
7. **Hitachi Energy's US programme** is now "around $1.5 billion" (release, 15 Sep 2026), not "more than $1 billion" (29 June 2026). The piece's table does not state it, but any new text should use $1.5bn and should not confuse it with Hitachi Energy's separate 2024 global $1.5bn transformer plan (press).
8. **South Boston date.** Still no date in Hitachi's releases (the piece is right). IIR (28 Oct 2026) now reports production ramp-up in late 2028 or early 2029; press only.
9. **Charlotte.** Still no Siemens Energy confirmation of a first transformer (the piece is right). Its own February 2024 release also said US supply met "only 20%" of LPT demand, with lead times of "up to five years": both usable, dated.
10. **GE Vernova is under-used.** The piece names it but gives no figure beyond book-to-bill. Primary: Electrification equipment backlog $42.2bn at 30 September 2026, up 60% in a year, including $5bn from Prolec GE, which it bought outright for $5.275bn (closed 2 February 2026). Also note Q3 Electrification orders fell 9% organically (against a large prior-year order), the only grid maker with a falling quarter.
11. **Schnabel cars.** The piece's "about 30 in North America in 2012" matches DOE 2012. DOE's 2024 report says "only about three"; leave the 2012 figure, but do not cite the 2024 report for it.
12. **Weight.** "About 100 to 400 tons" matches DOE 2012; DOE 2024 says "typically 150 to 400". Either is fine if dated.
13. **Cleveland-Cliffs.** Correct as "the sole U.S. producer". Missing context: in DOE's data it met only 12% to 20% of US GOES demand, the top grade comes only from Nippon Steel, and Cliffs dropped its own Weirton transformer plant in May 2025 (press).
14. **Policy gaps.** The piece covers EO 14421 but not the 20 April 2026 DPA determination (2026-10) naming transformers and electrical core steel, nor the 2024 distribution transformer efficiency rule (compliance 2029), nor the Section 232 tariff on GOES laminations and cores (Aug 2025). EO number: DOE says 14421, Wood Mackenzie and most law firms say 14420; the piece follows DOE, which is right to keep, but expect readers to see 14420 elsewhere.
15. **Spares missing.** STEP has never been used, Grid Assurance has never supplied an LPT, and a ready spare can be energised in 3 to 4 weeks against a 2 to 3 year order (DOE 2024). That contrast answers "why not just keep spares?".

## Could not verify today
- NREL distribution transformer figures (60 to 80 million units; +160% to 260% by 2050): nrel.gov did not resolve; from NREL's news release via search.
- Siemens Energy Charlotte output (24 rising to 57 units a year): press only.
- Hyosung, HD Hyundai Electric and LS Electric Q3 2026 figures: broker notes and Korean press, not filings.
- Section 232 GOES laminations and cores inclusion: Cleveland-Cliffs' account; Federal Register notice not opened.
- DPA 2026-10 exact wording: law-firm summaries; whitehouse.gov text not opened in full.
- GE Vernova Q4 2025 Electrification revenue: derived, not read.
