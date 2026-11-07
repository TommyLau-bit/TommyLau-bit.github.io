# The gas turbine and its makers: research for "Building your own power" (depth rebuild)

Compiled 7 November 2026. Slice: how the machine works, why the hot section binds, the makers' queues, the 2000s boom and 2017 bust, and plant cost.
Tags: **primary** = company filing, release, own presentation or own transcript, regulator, EIA/DOE. **transcript (3rd-party)** = call transcript hosted by a third party (wording can contain transcription errors). **press** = press or analyst report only. **calc** = my arithmetic.

---

## 1. How a gas turbine makes power

**Plain terms.** A gas turbine is a jet engine bolted to the ground. A compressor at the front squeezes air to about 24 times atmospheric pressure. In the combustor, gas burns in that air. The hot, high-pressure gas then expands through the turbine, spinning it. The turbine drives the compressor and also a generator. Simple cycle stops there and throws the hot exhaust away (about 670°C). Combined cycle runs the exhaust through a boiler (a heat recovery steam generator) to raise steam for a second, steam turbine. Same gas, about half as much power again.

**Heat rate** is the gas needed per unit of power, in Btu per kWh; lower is better. Efficiency = 3,412 ÷ heat rate (3,412 Btu is one kWh of heat).

### Unit specs, primary

| Machine | Simple cycle output | Simple cycle efficiency (heat rate) | Combined cycle | Source |
|---|---|---|---|---|
| GE Vernova 7HA.02 (60 Hz) | 384 MW | 42.6% (8,009 Btu/kWh) | 7HA family "63–64%" | GE Vernova 7HA product page, read 7 Nov 2026, https://www.gevernova.com/gas-power/products/gas-turbines/7ha |
| GE Vernova 7HA.03 (60 Hz) | 430 MW | 43.3% (7,884 Btu/kWh); ramp 75 MW/min | 1x1 about 640 MW; ">64%" quoted for 2x1 (1,282 MW at Dania Beach) | same page; 7HA.03 page https://www.ge.com/power/gas/gas-turbines/7ha/7ha-03 (1x1 640 MW, via search snippet; press for the 2x1 figure) |
| Siemens Energy SGT6-9000HL (60 Hz) | 440 MW | >43.2% (<7,898 Btu/kWh); pressure ratio >24:1; exhaust 675°C | 1x1 655 MW, 2x1 1,310 MW, >64% (<5,331 Btu/kWh) | HL-class fact sheet (2021), https://assets.siemens-energy.com/dam/6a81abd9-6c46-42c9-9034-b036013f322b/210923-HL-ClassFactSheet-05-pdf_Original%20file.pdf |
| Siemens Energy SGT5-9000HL (50 Hz) | 593 MW | >43% | 1x1 880 MW, >64% | same |
| MHI M501JAC (60 Hz) | 453 MW | 44.0% LHV | 1x1 664 MW, >64.0% LHV | MHI M501J page, read 7 Nov 2026, https://power.mhi.com/products/gasturbines/lineup/m501j |

Check: 3,412 ÷ 7,884 = 43.3%; 3,412 ÷ 5,331 = 64.0% (calc). Combined cycle uses about a third less gas per kWh than simple cycle: 5,331 against 7,884 (calc, Siemens/GE figures mixed for illustration; on Siemens alone 5,331 against 7,898 = 32.5% less).

### Temperatures: the flame is hotter than the metal can stand

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| M501J turbine inlet temperature | 1,600°C ("100°C higher than that of the G Series") | page read 7 Nov 2026 | MHI M501J page (above) | primary |
| MHI design target for air-cooled JAC | 1,650°C turbine inlet | 2019 | MHI Technical Review vol. 56 no. 3, https://power.mhi.com/randd/technical-review/pdf/index_67e.pdf | primary (development target, not a rating) |
| MHI says the blade metal stays at conventional temperature | "at the level of conventional gas turbines", using "advanced thermal barrier coating (TBC)" and cooling | read 7 Nov 2026 | MHI M501J page | primary |
| Siemens HL key technologies | "Advanced combustion system for higher firing temperatures"; "Innovative multi-layer coating for better blade robustness and less cooling-air consumption"; "Ultra-efficient internal cooling features for blades and vanes" | 2021 | HL fact sheet | primary |
| DOE: before the 1990s programme, above about 2,300°F (1,260°C) "available cooling technologies were insufficient"; the programme "pushed firing temperatures to 2,600 degrees F" (1,430°C), with "single-crystal turbine blades" and TBCs; GE unveiled the H System on 18 Feb 2000 | 2,300°F; 2,600°F | DOE page (undated, describes 1992–2001) | DOE Office of Fossil Energy, "Breakthrough Gas Turbines", https://www.energy.gov/node/612326 | primary |
| GE does not publish an HA firing temperature on its product pages | n/a | 7 Nov 2026 | GE 7HA page | primary (absence) |
| Melting range of a typical single-crystal blade alloy (CMSX-4, second-generation, 3% rhenium) | solidus about 1,339°C (1,612 K); liquidus about 1,375°C (1,648 K) | papers, various | academic, via search: HIP study and surface-tension study of CMSX-4 (e.g. https://opus4.kobv.de/opus4-bam/files/52097/crystals-11-00152-v2.pdf) | academic, not maker; verify before citing a number |
| Cooling plus ceramic coating lower metal surface temperature | ">300°C" | n/a | ORNL-listed TBC article (search result) | academic/secondary |

**The point for the piece (calc and framing):** a 1,600°C gas stream is about 250 to 260°C above the temperature at which a CMSX-4-type blade alloy begins to melt (1,600 − 1,339 = 261°C, calc). The blade survives on three things, all made by few hands: (1) **single-crystal casting**, the whole blade grown as one metal crystal so there are no grain boundaries to creep and crack at heat; (2) **internal cooling passages**, cast in by ceramic cores, through which compressor air flows and bleeds out of film-cooling holes to lay a cool film over the surface; (3) a **thermal barrier coating**, a ceramic topcoat (yttria-stabilised zirconia) on a metal bond coat. Suggest the piece says "hotter than the blade metal's melting point" and cites MHI 1,600°C plus a named alloy reference, or keeps it qualitative ("hotter than the metal can stand uncooled") if the alloy figure cannot be sourced to a maker.

---

## 2. Why the hot section binds: the casters

### Who casts blades and vanes

| Fact | Figure / quote | Date | Source | Tag |
|---|---|---|---|---|
| Howmet's competitors in investment castings incl. airfoils | Berkshire Hathaway "through its 2016 acquisition of Precision Castparts Corporation"; "Doncasters Group Limited (U.K.) and Consolidated Precision Products Corp." | 12 Feb 2026 | Howmet 2025 Form 10-K, https://www.sec.gov/Archives/edgar/data/4281/000000428126000012/hwm-20251231.htm | primary |
| Captive casting | "Several of Howmet's largest customers have captive superalloy furnaces for producing airfoil" castings | 12 Feb 2026 | same | primary |
| Gas turbines share of Howmet revenue | about 11% in 2025 (10% in 2024) | 12 Feb 2026 | same | primary |
| Siemens Energy's own blade line | Siemens Energy and Chromalloy formed Advanced Airfoil Components, a 210,000 sq ft, US$139m casting plant in Hillsborough County, Florida, for Siemens blades and vanes (opened about 2011) | c.2010–2011 | foundrymag.com, americanmachinist.com | press |
| Siemens Energy expands Tampa blades and vanes | "In Tampa, the plant is being expanded to manufacture gas turbine blades and vanes, which are central components in the supply chain that also supplies the Berlin plant" (my translation of the German release); part of US$1bn US programme; investments "deliberately designed to avoid overcapacity" (translation) | 3 Feb 2026 | Siemens Energy press release (German), https://www.siemens-energy.com/de/de/home/press-releases/siemens-energy-investiert-eine-milliarde-dollar-und-schafft-1-50.html | primary (translated; find the English version before quoting) |
| MHI invests in hot parts | Planned growth investment "GTCC: Includes hot parts production capacity, Approx. ¥500 bn"; "Double GTCC new unit production capacity" | 6 Nov 2026 | MHI 1H FY2026 presentation, pp. 25–26, https://www.mhi.com/finance/library/result/pdf/fy20262q/presentation.pdf | primary |

### Howmet's latest numbers (gas turbines end market)

| Period | Gas turbines revenue | Prior year | Growth | Source | Tag |
|---|---|---|---|---|---|
| Q3 2026 | $349m | $241m | +45% (company states 45%) | Form 10-Q for Q3 2026, end-market table, https://www.sec.gov/Archives/edgar/data/0000004281/000000428126000036/hwm-20260930.htm ; release 29 Oct 2026, https://www.sec.gov/Archives/edgar/data/0000004281/000110465926119857/tm2628456d1_ex99-1.htm | primary |
| 9M 2026 | $954m | $678m | +40.7% | same 10-Q | primary; % calc |
| Q2 2026 | n/a here | | +38% | live piece, Howmet release 6 Aug 2026 | primary (from piece) |

Release quotes (29 Oct 2026, CEO John Plant): "45% year-over-year gas turbines revenue growth, which demonstrates both the extraordinary addition to output and, even more importantly, the increase in market share"; demand continues "beyond previous expectations, which supports the outlook beyond 2028"; capex "elevated spend beyond 2027 to support growth in both aerospace and defense as well as gas turbines". Engine Products Q3 revenue $1,451m vs $1,087m (+33%). Primary.

Howmet Q3 2026 call, 29 Oct 2026 (transcript (3rd-party), https://www.earningswhispers.com/transcript/HWM/Q32026; wording may contain transcription errors):
- "2031 is now also sold out"; "2032 will likely be sold out in the next one or two quarters".
- "the new capacity currently being installed is totally sold out"; impact "likely to be felt in the outer years beyond 2028".
- Doubling of gas turbine sales from the 2025 base now expected in three years rather than three to five; "maybe we will rise to two and a half times inside five years", about US$2.5bn "by the end of the decade".
- New capacity "will take two years to install, and then there will be a multi-year runway after that"; "probably now at seven new manufacturing plants and considering three more".
- On a customer's turbines: "the availability of turbines was restricted in the industry by the availability of turbine blades"; "these might take another 18 months to two years to achieve".
- A new large IGT blade "for a customer that doesn't start until 2031".
Use as dated transcript evidence, and check against Howmet's own webcast if any line carries the argument.

Howmet capacity sites (press): Wichita Falls, Texas superalloy foundry expansion (city incentive US$5.275m approved Sept 2026; construction could start Feb 2027), Morristown, Tennessee ceramic cores from Q2 2025; earlier Q2 2025 call tied new IGT airfoil capacity in Michigan, Tennessee, Japan and Europe to late 2026 and 2027 (industrialinfo.com, press).

### GE Vernova on castings and forgings (primary, own transcript)

GE Vernova 2Q 2026 call, 22 Jul 2026, https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf (Scott Strazik):
- "we can see clearly the castings and forgings arriving in '27 for that next step-up in output in '28 to 24 gigawatts annualized."
- "We have 325 machines in our gas factories that have now been installed, and we're on track to have approximately 400 new machines installed in Gas Power by the end of this year." (machines = machine tools)
- 30 GW in 2030 via "lean and incremental machinery in our existing factory footprint, and have already secured significant supply chain capacity, all funded by customer down payments."
- "We will invest in incremental machines beyond 400 to ultimately get to the 30 gigawatts ... leveraging the existing industrial footprint"; "the CAPEX is modest".
- Heavy-duty "could take another 18 months at site after it's actually shipped from Greenville"; aero commissioning "could be six months"; shipments "24 months apart".

**How long a casting line takes (best available):** about two years to install new capacity, per Howmet's CEO (transcript, 3rd-party); GE Vernova sees castings and forgings arriving in 2027 for its 2028 output step, about a year of lead (primary). No primary figure found for qualification time of a new single-crystal line at an OEM; say so rather than guess.

---

## 3. The makers' queues

### GE Vernova: gas turbine gigawatts under contract (primary)

| Quarter end | Firm orders (backlog) | Slot reservations | Under contract | Signed in quarter | Shipped in quarter | Source |
|---|---|---|---|---|---|---|
| 31 Dec 2025 | 40 GW | 43 GW | 83 GW | | | releases (as in live piece) |
| 31 Mar 2026 | 44 | 56 | 100 | 21 | 4 | release 22 Apr 2026 (live piece) |
| 30 Jun 2026 | 53 | 63 | 116 | 20 | 3 | release 22 Jul 2026 (live piece) |
| 30 Sep 2026 | 64 | 58 | 122 | 11 (8 SRAs + 3 orders); 13 GW of SRAs converted | 5 | release 28 Oct 2026, https://www.sec.gov/Archives/edgar/data/1996810/000199681026000162/gevpressrelease3q26.htm (verified today) |
| 31 Dec 2026 (guide) | | | at least 130 | about 13+ ("modestly larger than the third quarter") | | release and 3Q call |

Q3 2026 verified directly in the release: "Signed 11 gigawatts (GW) of new gas equipment contracts, including 8 GW of slot reservation agreements and 3 GW of orders. Converted 13 GW of existing slot reservation agreements to orders and shipped 5 GW of equipment; resulting in backlog growth from 53 to 64 GW and a decrease in slot reservation agreements from 63 to 58 GW."

**Units and gigawatts, Form 10-Q for Q3 2026** (filed 28 Oct 2026), https://www.sec.gov/Archives/edgar/data/1996810/000199681026000163/gev-20260930.htm (primary):

| | Q3 2026 | Q3 2025 | 9M 2026 | 9M 2025 |
|---|---|---|---|---|
| Orders, gas turbines (units) | 112 | 29 | 262 | 114 |
| of which heavy-duty | 55 | 20 | 135 | 69 |
| of which HA | 21 | 13 | 48 | 28 |
| of which aeroderivatives | 57 | 9 | 127 | 45 |
| Orders, GW | 16.6 | 7.4 | 36.7 | 19.6 |
| Sales, gas turbines (units) | 32 | 20 | 86 | 60 |
| of which heavy-duty | 19 | 14 | 47 | 44 |
| of which HA | 7 | 6 | 15 | 19 |
| of which aeroderivatives | 13 | 6 | 39 | 16 |
| Sales, GW | 5.3 | 4.0 | 12.8 | 12.2 |

Note: "orders" GW (16.6) include SRA conversions; "signed" (11) is new contracts. Calendar 2026 shipments will be about 18 GW (12.8 + roughly 5 in Q4, calc), not 20; 20 GW is the annualised rate reached in Q3.

Power segment equipment RPO: $54,422m at 30 Sep 2026 vs $24,707m at 31 Dec 2025 and $18,977m at 30 Sep 2025 (10-Q, primary).

Power contract liabilities and current deferred income: $33,163m at 30 Sep 2026 vs $16,527m at 31 Dec 2025 (10-Q, primary; verified). The 10-Q ties the nine-month inflow of $19.5bn to "down payments on orders and slot reservation agreements at Power, and down payments at Electrification" (company-wide line).

3Q call, 28 Oct 2026, own transcript https://www.gevernova.com/sites/default/files/gev_webcast_transcript_10282026.pdf (primary):
- "This quarter, we sold multiple slots for 2032 delivery".
- "approximately 100 customers in 25 different countries, of which approximately 80% are traditional customers and 20% are for data centers." (Reads as share of customers; not a share of GW.)
- "3Q orders were priced more than 20% above 4Q 2025 equipment orders based on higher priced turbines and a greater mix of aeroderivatives"; "Full year 2026 Gas orders pricing per kW will be approximately 50% higher than full year 2025 orders"; Q4 price per kW lower than Q3 "due to fewer aeroderivatives and relatively more 50Hz units".
- "We shipped a total of 32 gas turbines in the quarter, a 60% increase year over year, including 13 aeroderivatives."
- "backlog is now greater than our SRA balance".
- Aero: Q4 lighter "Not because the demand is softer, but more because we're now going out so far in the future before we have availability, right. Because we're sold out so far." Aeros also used "in strategic partnerships where we also secure heavy duty and Electrification equipment combined."
- "HA fleet running or on contract will be at least 400 units by the end of 2027"; "every gigawatt of HA to generate half a billion dollars of high margin services revenue over the first 20 years".
- No financing strain: "no change in our cash terms required to secure the equipment".
- 2027: "real growth in our gigawatts on contract throughout 2027", quarterly profile "more likely to feel like 3Q and 4Q".

2Q call, 22 Jul 2026 (primary): "making us mostly sold out through '30, and to have sold more than half of the 30 gigawatts of '31 production slots by the end of this year".

Output plan (primary, 2Q call): 20 GW a year now (5 GW a quarter from Q3 2026, up from about 3), 24 GW in 2028, 30 GW in 2030, in existing factories.

Years of output (calc): 122 ÷ 20 = 6.1; 122 ÷ 24 = 5.1; 122 ÷ 30 = 4.1. At 130 GW: 6.5 years at 20 GW.

### Siemens Energy (primary, now confirmable)

| Fact | Figure | Date | Source | Tag |
|---|---|---|---|---|
| Gas Services Q3 FY26 orders | €9,967m (+61.9% comparable), revenue €3,756m, book-to-bill 2.65, profit before special items €648m (17.3%) | quarter to 30 Jun 2026, published 5 Aug 2026 | Earnings release Q3 FY2026 (copy hosted at https://egyptoil-gas.com/wp-content/uploads/2026/08/earnings-release-q3-fy2026-en-pdf_Original20file.pdf; find the siemens-energy.com original before citing) | primary (third-party copy) |
| Gas Services order backlog | €73bn | 30 Jun 2026 | same | primary |
| Demand drivers | "Demand from the U.S., including large orders related to data centers, and orders from the Middle East and Asia for new power plants" | 5 Aug 2026 | same | primary |
| GW: firm backlog and reservations | "15 GW booked (12 GW converted from SRAs), 6 GW shipped"; "High level of firm customer commitments (69 GW backlog / 26 GW SRAs)" | 30 Jun 2026 | Q3 FY26 analyst presentation p.6, https://assets.siemens-energy.com/dam/3e846440-66dd-4a56-be75-b49d004e6741/2026-08-05_Q3_Analyst_presentation-pdf_Original%20file.pdf | primary |
| Under contract, GE Vernova's definition | 69 + 26 = 95 GW | 30 Jun 2026 | calc from presentation | calc |
| Capacity, large gas turbines (100–600 MW), units a year | about 35 (FY25, FY26), about 50 (FY27), 50+ (FY28); "LGT capacity expansion to become effective in FY27" | Aug 2026 | same presentation p.5 (chart labels; year mapping read from chart order, check visually) | primary |
| Capacity, medium gas turbines (20–100 MW), units | 50 (FY25), about 80 (FY26), about 100 (FY28); "Additional MGT capacity has come online in H2 FY26" | Aug 2026 | same p.5 | primary |
| Shipments 2026 | CEO: could deliver 15–16 GW this year | 5 Aug 2026 call | Utility Dive | press |
| Lead times | CFO: "three years or more" | 5 Aug 2026 call | Utility Dive | press |
| Market size | CEO: addressable gas turbine market could reach 120 GW a year, about half US | 5 Aug 2026 | Utility Dive | press |
| Fiscal 2026 results (year to 30 Sep 2026) | **Not out on 7 Nov 2026.** Reported date 11 Nov 2026 (press only; FY25 was 13 Nov 2025) | | admiralmarkets.com, trading-treff.de | press |

Calc: at Siemens' own 6 GW a quarter (24 GW a year), 95 GW is about 4.0 years; at the CEO's 15–16 GW for 2026, about 6 years (calc; mixed bases, use with care).

### Mitsubishi Heavy Industries (primary, new today)

1H FY2026 results, announced 6 Nov 2026, presentation https://www.mhi.com/finance/library/result/pdf/fy20262q/presentation.pdf:

| Large frame gas turbines | 1H FY25 | FY25 | 1H FY26 |
|---|---|---|---|
| Order intake, units (GW) | 23 (10 GW) | 35 (16 GW) | 19 (8 GW) |
| of which Americas | 12 | 19 | 11 |
| of which Asia | 11 | 12 | 8 |
| of which EMEA | 0 | 4 | 0 |
| Contract backlog, units (GW) | 67 (29 GW) | 74 (33 GW) | 83 (37 GW) |

- GTCC order intake 1H FY26 ¥1,568.7bn vs ¥1,438.7bn; full-year FY26 GTCC orders forecast raised to ¥3,000bn (from ¥2,400bn), against ¥2,652.6bn in FY25. "In GTCC, order intake particularly strong in North America and Asia."
- Advances received at 1H FY26 end: ¥2.6 trillion (group).
- Growth investments from FY2027: "GTCC: Includes hot parts production capacity, Approx. ¥500 bn"; engines for "power generation systems targeting data centers" ¥100bn. "Double GTCC new unit production capacity". "Booked orders for data center equipment."
- Q1 FY26 had 10 units (four US); so Q2 FY26 was 9 units (calc). The 1H Q&A summary is not yet posted (7 Nov).
- From Q1 FY26 Q&A (6 Aug 2026, in live piece): delivery mostly 2028–2030 for Q1 bookings; combined cycle projects under discussion "will generally be delivered around 2030 to 2031"; capacity "expected to double" against FY2024; "Order pricing has not declined". https://www.mhi.com/finance/library/result/pdf/fy20261q/qa_20261q.pdf

Calc: MHI backlog 37 GW; its 2026 shipment rate is not disclosed in GW, so no years-of-output figure.

### Three makers side by side (calc, mixed dates)

| Maker | Firm backlog | Reservations | Total | Date |
|---|---|---|---|---|
| GE Vernova | 64 GW | 58 GW | 122 GW | 30 Sep 2026 |
| Siemens Energy | 69 GW | 26 GW | 95 GW | 30 Jun 2026 |
| MHI (large frame) | 37 GW (83 units) | not disclosed | 37 GW+ | 30 Sep 2026 |
| Sum | | | about 254 GW | calc, mixed dates and definitions |

Analyst view, for context only (press): Wood Mackenzie, 1 Apr 2026: global orders 110 GW at end-2025 against manufacturing capacity of 60–70 GW; turbine prices US$600/kW by end-2027, up 195% since 2019; turbines 20–30% of combined cycle project cost. https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis

### Data centre share, all primary statements found
- GE Vernova: about 20% of about 100 gas customers "are for data centers" (28 Oct 2026).
- Siemens Energy: "large orders related to data centers" (5 Aug 2026); "especially for data center related gas turbines" (presentation).
- MHI: "Booked orders for data center equipment"; ¥100bn for engines targeting data centres (6 Nov 2026).
- No maker gives a GW share. Siemens Q1 FY26 "22 GW commitments, 15 GW SRAs in data center segment" is press only.

---

## 4. History: boom, bust, and why makers will not overbuild

### US natural gas capacity by year entered service (calc from EIA-860M)

Source: EIA, Preliminary Monthly Electric Generator Inventory (Form EIA-860M), September 2026 file, Operating plus Retired sheets, energy source NG, nameplate MW summed by operating year, https://www.eia.gov/electricity/data/eia860m/ . This counts surviving and retired units; units retired before the Retired sheet's coverage are missing, so early years are slight undercounts. Nameplate, not summer capacity. Calc.

| Year | GW | Year | GW |
|---|---|---|---|
| 1998 | 2.2 | 2012 | 11.5 |
| 1999 | 9.4 | 2014 | 9.4 |
| 2000 | 30.2 | 2016 | 9.4 |
| 2001 | 43.4 | 2017 | 10.8 |
| **2002** | **68.6** | 2018 | 21.7 |
| 2003 | 53.8 | 2020 | 7.1 |
| 2004 | 25.0 | 2022 | 7.1 |
| 2005 | 17.1 | 2023 | 9.9 |
| 2006 | 10.2 | 2024 | 2.4 |
| 2008 | 8.8 | 2025 | 5.3 |
| 2010 | 7.5 | 2026 (to Sep) | 3.7 |

2000–2005 total about 238 GW (calc). Peak 2002.

EIA statements (primary):
- "U.S. electric generating capacity additions averaged 35 GW annually from 2000 through 2005", nearly all gas, about two-thirds combined cycle (Today in Energy, 16 Jul 2014, https://www.eia.gov/todayinenergy/detail.php?id=17131). Note EIA's 35 GW is net summer capacity of all fuels; my 40 GW a year average for gas is nameplate (calc), so do not mix them in one sentence.
- The 2000–2004 combined cycle boom "created excess generating capacity"; combined cycle plants intended to run 50–70% of the time ran about 34% in 2003 (Today in Energy, 7 Jun 2011, https://www.eia.gov/todayinenergy/detail.php?id=1690).
- Record combined cycle additions in 2002 and 2003; "about half of the existing U.S. CCGT fleet currently operating entered service between 2000 and 2006" (Today in Energy, 4 Nov 2022, https://www.eia.gov/todayinenergy/detail.php?id=54539).

### The 2017 bust (primary)
- **Siemens, 16 Nov 2017:** "Global demand for large gas turbines (generating more than 100 megawatts) has fallen drastically and is expected to level out at around 110 turbines a year. By contrast, the technical manufacturing capacity of all producers worldwide is estimated at around 400 turbines." About 6,900 jobs cut worldwide, about 6,100 at Power and Gas; closures of Görlitz and Leipzig. Press release PR2017110073COEN, https://assets.new.siemens.com/siemens/assets/api/uuid:a2de2860-1d0a-47ae-83c1-8bab86aac736/press-release-siemens-tackles-structural-market-changes-and-stre.pdf
- **GE Power, 7 Dec 2017:** "approximately 12,000 positions"; "$1 billion in structural cost reductions in 2018"; "Traditional power markets including gas and coal have softened"; "Volumes are down significantly in products and services driven by overcapacity." https://www.ge.com/news/press-releases/ge-power-announces-global-headcount-reduction-12000-jobs-part-plan-take-out-1
- Calc: 110 of 400 is about 28% utilisation of world capacity in Siemens' own 2017 estimate.

### The lesson in the makers' own words now (primary)
- GE Vernova: growth "in our existing factory footprint ... all funded by customer down payments" (22 Jul 2026); "the CAPEX is modest".
- Siemens Energy: US investments "deliberately designed to avoid overcapacity" (3 Feb 2026, translated).
- MHI: builds "the order book while carefully monitoring progress on the capacity expansion" (6 Aug 2026 Q&A, in live piece).
- Howmet: expansion "will be completed without adding any debt" (29 Oct 2026, transcript 3rd-party).

---

## 5. Cost of a new plant

### EIA planning assumptions (primary) versus utility filings (primary)

| Estimate | $/kW | Dollar basis | Date | Source |
|---|---|---|---|---|
| EIA AEO2020, combined cycle multi-shaft (1,083 MW) | 954 | 2019$ overnight | Jan 2020 | EIA AEO2020 cost and performance table, https://www.eia.gov/outlooks/archive/aeo20/assumptions/pdf/table_8.2.pdf |
| EIA AEO2020, single-shaft (418 MW) | 1,079 | 2019$ | Jan 2020 | same |
| EIA AEO2023, multi-shaft | 1,176 | 2022$ | Mar 2023 | https://www.eia.gov/outlooks/aeo/assumptions/pdf/elec_cost_perf.pdf |
| EIA capital cost study for AEO2025 (Sargent & Lundy), H-class 2x2x1, 1,227 MW net | 868 | 2023$ | Jan 2024 | https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf |
| same, H-class 1x1 single shaft, 627 MW | 921 | 2023$ | Jan 2024 | same |
| same, H-class simple cycle, 419 MW | 836 | 2023$ | Jan 2024 | same |
| same, 4 x aeroderivative simple cycle, 211 MW | 1,606 | 2023$ | Jan 2024 | same |
| Duke Energy Indiana, Cayuga, two 1x1 combined cycle, 1,476 MW winter | about 2,236 (US$3.3bn "plus actual AFUDC") | nominal, excl. financing | 10-Q to 30 Sep 2026 | Duke Energy Form 10-Q, https://www.sec.gov/Archives/edgar/data/0001326160/000132616026000051/duk-20260930.htm ; $/kW calc |
| Duke Energy Carolinas, Anderson County SC, 1,365 MW combined cycle | about 2,344 (US$3.2bn incl. financing, preliminary) | nominal | filed 30 Oct 2025; in 10-Q | same; calc |
| Duke Energy Progress, Person County unit 2, 1,360 MW | about 1,618 (US$2.2bn incl. financing, preliminary) | nominal | filed Jan 2026; in 10-Q | same; calc |
| Evergy Kansas Central, 50% of 710 MW Viola combined cycle | about 2,222 (US$788.75m for 355 MW) | nominal | KCC approval 7 Jul 2025 | KCC/CURB documents, https://www.kcc.ks.gov/news-7-7-25 (via search; verify the US$788.75m in the order); calc |

Notes:
- The EIA AEO2025 study (2023 dollars) is about where AEO2020 was in 2019 dollars; utility filings in 2025–2026 run at roughly $1,600 to $2,350 per kW, about two to two and a half times EIA's planning figure (calc). Utility figures include owner's costs, transmission or financing in varying mixes, so the comparison is directional.
- GridLab, Energy Futures Group and Halcyon (10 Sep 2025): recent combined cycle projects report about $2,000/kW, against $1,116/kW and $1,427/kW for plants due in 2026 and 2027; public datasets "underestimating current market costs" (https://gridlab.org/wp-content/uploads/2025/09/PRESS-RELEASE_Cost-of-Gas-1.pdf). Advocacy group analysis of filings: press-grade.
- NextEra's CEO said on the Q1 2025 call the cost of a gas plant "has tripled" in a few years (transcripts, 3rd-party); the $785/kW (2022) to $2,400/kW figures are press only (gasoutlook.com).
- Turbine price: GE Vernova, FY2026 gas orders price per kW "approximately 50% higher than full year 2025 orders" (28 Oct 2026, primary). Wood Mackenzie US$600/kW turbine by end-2027 (press/analyst).

---

## What the live piece has wrong or out of date

1. **MHI figures are a quarter old.** The piece cites Q1 FY26 (10 units). MHI's 1H FY26 results of 6 Nov 2026 give 19 large frame units (8 GW) ordered in the half, against 23 (10 GW) a year earlier, and a backlog of 83 units (37 GW), up from 74 (33 GW) at March 2026. GTCC order forecast raised to ¥3,000bn. Add the ¥500bn hot-parts investment. Note MHI's half-year unit orders fell year on year: a small point for the "signings slowing" counter-argument.
2. **Siemens Energy can come back in, from a primary source.** The piece dropped Siemens' 95 GW as press only. Siemens' own Q3 FY26 analyst presentation (5 Aug 2026, p.6) states "69 GW backlog / 26 GW SRAs": 95 GW on GE Vernova's definition. It also shows large-turbine capacity rising from about 35 units a year to about 50 in FY27. Its FY26 results (reported date 11 Nov 2026) are not out yet; refresh after.
3. **Siemens Florida source.** The sources line cites "Siemens Energy, 11 February 2026" (Q1 presentation, URL not recorded). Replace with Siemens Energy's release of 3 Feb 2026 (Tampa blades and vanes, "avoid overcapacity"), which has a URL.
4. **"Ships about 20 gigawatts a year" needs care.** 20 GW is the annualised rate from Q3 2026 (5.3 GW shipped in Q3 per the 10-Q). Shipments in the first nine months of 2026 were 12.8 GW, so calendar 2026 will be about 18 GW (calc). Say "now ships at about 20 GW a year".
5. **"About 20% of GE Vernova's roughly 100 gas customers are data centres"** matches the transcript's wording, which is ambiguous ("20% are for data centers"). It is a customer count, not a share of gigawatts; do not let a rebuilt piece turn it into a share of the queue.
6. **Howmet: add the new primary numbers.** Q3 gas turbines revenue $349m vs $241m; nine months $954m vs $678m (10-Q). Its CEO said 2031 is "sold out" and 2032 likely within one or two quarters (transcript, 3rd-party: mark it so).
7. **"Big forgings" paragraph quotes GE on "castings and forgings arriving in '27"** correctly (verified against the 22 Jul 2026 own transcript).
8. **Verified unchanged:** 122 GW (64 + 58), 11 GW signed, 13 GW converted, 5 GW shipped; slots sold for 2032; ~50% higher 2026 pricing per kW; Power contract liabilities $16,527m to $33,163m; aero 127 ordered / 39 shipped in 9M 2026; 20/24/30 GW plan; "lean and incremental machinery in our existing factory footprint ... all funded by customer down payments"; 18 months on site.
9. **Glossary gap for the rebuild:** the piece explains simple and combined cycle but not heat rate, firing temperature, single-crystal casting, thermal barrier coating or 50/60 Hz (GE's Q4 pricing comment turns on 50 Hz mix). STORY-RULES 18a needs each explained at first use.
10. **Missing context the rebuild should add:** the 2002 peak (about 69 GW of gas entering service, calc from EIA-860M) and Siemens' 2017 "110 turbines a year" against "400" capacity explain why makers now expand only inside existing walls and on deposits. And cost: utility filings now at about $1,600–2,350/kW against EIA's $868–921/kW (2023$).
