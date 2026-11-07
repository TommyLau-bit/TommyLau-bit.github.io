# Building your own power: the fuel and the pipe

Research slice for the depth rebuild of `building-your-own-power`. Compiled 7 November 2026.
Every figure is primary unless marked **press**. **calc** = my arithmetic, shown. No prices are forecast; the gas prices cited are dated history that explains the physical system.

Units used throughout: Bcf/d = billion cubic feet a day. MMcf/d = million cubic feet a day. One dekatherm (Dth) = one MMBtu = one million British thermal units, roughly a thousand cubic feet of gas. US gas delivered to consumers carried 1,036 Btu per cubic foot in 2025 (EIA, https://www.eia.gov/dnav/ng/ng_cons_heat_a_EPG0_VGTH_btucf_a.htm).

---

## 1. How much gas a data centre burns

**Heat rate** = the fuel a plant burns to make one kilowatt-hour. Lower is more efficient. EIA's average *tested* heat rates for natural gas plants in 2025 (EIA Electric Power Annual, Table 8.2, https://www.eia.gov/electricity/annual/html/epa_08_02.html):

| Plant type (EIA prime mover) | 2025 heat rate, Btu/kWh | 2015 |
|---|---|---|
| Combined cycle (turbine plus steam turbine on its exhaust) | 7,535 | 7,655 |
| Gas turbine alone (simple cycle, incl. aeroderivatives) | 10,975 | 11,302 |
| Internal combustion (reciprocating gas engines) | 8,853 | 9,322 |
| Steam boiler | 10,293 | 10,372 |

**calc: gas burned by 1 GW of generation running round the clock** (1 GW × 24 h × heat rate ÷ 1,036 Btu/cf):

| 1 GW running at | Combined cycle | Simple-cycle turbine | Gas engines |
|---|---|---|---|
| 100% load | 0.175 Bcf/d (180,840 MMBtu/d) | 0.254 Bcf/d (263,400 MMBtu/d) | 0.205 Bcf/d (212,472 MMBtu/d) |
| 90% load | 0.157 Bcf/d | 0.229 Bcf/d | 0.185 Bcf/d |

Notes:
- Tested heat rates are at test conditions; real part-load and hot-day running is worse, so these are floors. A data centre runs near flat out all year, which is what makes it a pipe customer rather than a peaker.
- The off-grid choice costs fuel: a simple-cycle island burns about 46% more gas per MWh than a combined cycle (10,975 / 7,535, calc). That is the fuel side of "the fast machine".

**Scale against real pipes and deals (calc, 100% load):**

| Pipe or contract | Gas | Equals this much generation |
|---|---|---|
| Kinder Morgan Permian Link, "approximately 2.8 Bcf/d" | 2.8 Bcf/d | about 16 GW combined cycle, or 11 GW simple cycle |
| Transco Southeast Supply Enhancement, 1,596,900 Dth/d | 1.6 Bcf/d | about 8.8 GW combined cycle |
| Energy Transfer to Oracle, "approximately 900 MMcf per day" to three data centres | 0.9 Bcf/d | about 5.2 GW combined cycle, 3.5 GW simple cycle |
| Energy Transfer to Entergy Louisiana (Richland Parish, Hyperion's parish), 250,000 MMBtu/d | 0.25 Bcf/d | about 1.4 GW combined cycle |
| Energy Transfer to CloudBurst, up to 450,000 MMBtu/d for "up to approximately 1.2 GW" (**press** for the MW) | 0.43 Bcf/d | implies 15,600 Btu/kWh at full load; contract carries headroom over any heat rate in the table (calc) |
| EQT to Homer City, "up to 665,000 MMBtu" a day (agreement in principle) | 0.64 Bcf/d | 84% of 4.4 GW combined cycle at full load (calc) |
| Williams Socrates, 556 MW of engines/turbines | about 0.11 Bcf/d at engine heat rate | one site |

Caveat for Permian Link: Kinder Morgan says the project "will serve new power generation for an A-rated hyperscaler"; it does not say the hyperscaler holds all 2.8 Bcf/d. Write it as "a pipe big enough for about 16 GW of combined cycle", not "a 16 GW customer".

Against the national system: the whole US electric power sector burned 35.8 Bcf/d in 2025 (EIA STEO Oct 2026, Table 5a). One 2.8 Bcf/d pipe is about 8% of that (calc).

---

## 2. US gas supply

### 2a. National balance (EIA Short-Term Energy Outlook, 6 October 2026, Table 5a, https://www.eia.gov/outlooks/steo/tables/pdf/5atab.pdf; next STEO 10 November 2026)

| Bcf/d | 2025 (history) | 2026 (EIA estimate/forecast, shaded) |
|---|---|---|
| Marketed production | 118.4 | 123.5 |
| Dry production | 107.6 | 112.2 |
| LNG gross exports | 15.1 | 17.6 |
| Pipeline exports (mainly Mexico) | 9.5 | 10.0 |
| Electric power consumption | 35.8 | 37.0 |
| Total US consumption | 91.9 | 92.4 |

The 2026 column is EIA's own estimate including forecast months; cite as "EIA expects", never as fact. Latest actual month (EIA Natural Gas Monthly, released 30 Oct 2026, data for August 2026, https://www.eia.gov/naturalgas/monthly/):
- Dry production 115.84 Bcf/d in August 2026, up 6.6% (7.19 Bcf/d) on August 2025's 108.65.
- LNG exports 16.61 Bcf/d, up 14.2% year on year, to 34 countries.
- Deliveries to electric power 50.19 Bcf/d in August 2026, up 9.9% from 45.68 (summer peak month).

LNG exports actual (EIA monthly, MMcf, https://www.eia.gov/dnav/ng/hist/n9133us2m.htm): 2025 average 15.09 Bcf/d (calc from monthly sum); January to August 2026 average 17.29 Bcf/d (calc).

### 2b. The Permian: why its gas comes with oil

EIA, STEO May 2026: "Most of the Permian's natural gas production is associated natural gas" and operators "are influenced by crude oil prices." EIA, STEO September 2026: the Permian gas-to-oil ratio "averaged nearly 4,200 cubic feet per barrel in 2025, 15% higher than in 2021", so gas grows faster than oil. Plain English: drillers go for oil; gas comes up the same well whether or not anyone has a pipe for it.

EIA STEO Oct 2026, Tables 5a and 10a (https://www.eia.gov/outlooks/steo/tables/pdf/10atab.pdf):

| Permian | Q1 2025 | Q3 2025 | Q1 2026 | Q3 2026 |
|---|---|---|---|---|
| Active rigs | 302 | 258 | 242 | 264 |
| New wells drilled per rig (quarter) | 4.8 | 5.1 | 5.5 | 5.6 |
| Marketed gas, Bcf/d | 26.3 | 28.3 | 28.4 | 30.2 |
| Drilled but uncompleted wells | 1,295 | 1,023 | 850 | 844 |

- Q1 2025 to Q1 2026: gas +8%, rigs -20% (calc). Q3 2025 to Q3 2026: gas +6.7%, rigs +2% (calc). Q3 2026 rig and gas figures are EIA estimates in the October STEO.
- Contrast basin: Haynesville (gas-directed, Louisiana/east Texas, nearest the LNG coast) rigs doubled from 31 (Q1 2025) to 62 (Q3 2026); marketed gas 14.7 to 17.2 Bcf/d. A second supply engine that responds to gas demand rather than oil.
- EIA, STEO Sept 2026: "Permian and Haynesville regions together account for more than 70% of production growth in our forecast."

### 2c. Waha: dated proof the pipe is the limit

Waha hub, west Texas, is where Permian gas is priced before it leaves the basin. When pipes out are full, gas has nowhere to go and producers pay buyers to take it (a negative price), because shutting oil wells to stop the gas costs more.

| Date | Fact | Source |
|---|---|---|
| May 2026 | "the region faces severe pipeline constraints, as evidenced by record-low Waha Hub spot prices, which have averaged below zero for eight of the last nine months" | EIA STEO May 2026, https://www.eia.gov/outlooks/steo/archives/may26.pdf |
| Feb 2026 | Record 12 straight sessions below zero | **press** Reuters via EnergyNow, https://energynow.com/2026/02/us-natgas-prices-at-waha-hub-in-texas-in-negative-territory-for-record-12th-day |
| Mar 2026 | Record 25th straight day below zero | **press** Reuters via P&GJ, https://pgjonline.com/news/2026/march/permian-pipeline-constraints-push-waha-gas-prices-negative-for-25th-straight-day |
| 16 Apr 2026 | All-time low daily average of minus $9.52/MMBtu; negative on 118 of first 131 flow days of 2026 | **press** NGI, https://naturalgasintel.com/news/permian-natural-gas-prices-surpass-2024s-negative-run/ |
| Count by year | Daily average below zero 17 times in 2019, 6 in 2020, 1 in 2023, 49 in 2024, 39 in 2025 | **press** Reuters (via P&GJ above) |
| Jun to Sep 2026 | Hugh Brinson began shipments in June (EIA); Phase I "placed into full service" 1 September 2026 (Energy Transfer) | EIA STEO Sept 2026; ET Q3 release (below) |

No EIA Today in Energy article on 2026 Waha was found; EIA's STEO sentence is the primary anchor. Daily Waha prints are licensed data (NGI, Platts), so any day count is press. Appalachia shows the same pattern: EQT curtailed 21 Bcfe of output in Q3 2026 "to optimize in-basin pricing" and guides 10 to 20 Bcfe of curtailment in Q4 (EQT Q3 2026 release, 27 Oct 2026, https://www.sec.gov/Archives/edgar/data/33213/000003321326000054/eqt-ex991earningsreleasexl.htm). Gas is plentiful at the well; the shortage is pipe.

### 2d. LNG: the other new buyer

| Terminal | Dated fact | Source |
|---|---|---|
| Plaquemines (Louisiana, Venture Global) | First exports Dec 2024 (3,649 MMcf); 110,558 MMcf in Dec 2025, about 3.6 Bcf/d (calc) | EIA, https://www.eia.gov/dnav/ng/hist/ngm_epg0_eng_yplaq-z00_mmcfm.htm |
| Corpus Christi Stage 3 (Texas, Cheniere) | Train 5 "completed in February" (STEO Mar 2026) / "reached substantial completion in March" (STEO Apr 2026); exports 2.6 Bcf/d avg Jan to Aug 2026 vs 2.0 in 2025 (calc) | EIA STEO archives; https://www.eia.gov/dnav/ng/hist/ngm_epg0_eng_yccpl-z00_mmcfm.htm |
| Golden Pass (Texas, QatarEnergy/ExxonMobil) | First cargo from Train 1 on 22 April 2026, the 9th US LNG terminal; three trains of 0.7 Bcf/d nominal, 2.0 Bcf/d nominal in all (2.4 peak); Train 2 targeted 2H 2026, Train 3 1H 2027 | EIA Today in Energy, 23 April 2026, https://www.eia.gov/todayinenergy/detail.php?id=67564 |
| Golden Pass exports | 3,619 MMcf Apr 2026; 6,742 MMcf Aug 2026 (about 0.22 Bcf/d, calc: still ramping) | EIA, https://www.eia.gov/dnav/ng/hist/ngm_epg0_eng_ygpt-z00_mmcfm.htm |

### 2e. Texas: LNG exports against Texas power burn (EIA monthly, MMcf)

Texas LNG = Corpus Christi + Freeport + Golden Pass (Sabine Pass and Cameron are in Louisiana). Texas power = deliveries to electric power consumers (https://www.eia.gov/dnav/ng/hist/n3045tx2m.htm). Both released 30 Oct 2026.

| Month | Texas LNG exports | Texas power burn | LNG larger? |
|---|---|---|---|
| Mar 2025 | 130,782 | 112,797 | yes |
| Apr 2025 | 132,630 | 127,703 | yes |
| Nov 2025 | 149,189 | 141,050 | yes |
| Dec 2025 | 160,022 | 154,182 | yes |
| Jan 2026 | 147,250 | 169,939 | no |
| Feb 2026 | 147,907 | 127,650 | yes |
| Mar 2026 | 165,399 | 129,002 | yes |
| Apr 2026 | 159,524 | 144,871 | yes |
| May 2026 | 148,941 | 178,368 | no |
| Aug 2026 | 147,324 (4.75 Bcf/d) | 248,696 (8.02 Bcf/d) | no |

- calc: 2025 full year, Texas LNG 4.4 Bcf/d against Texas power 5.74 Bcf/d.
- Reading: LNG is flat all year; power burn swings with the seasons. LNG overtakes power in the mild shoulder months and has done so since spring 2025, so "February to April 2026" is true but not new. The durable point: Texas export terminals take a steady 4.4 to 5.3 Bcf/d out of the same Gulf Coast pipes the power plants use, year round.

Context (outside my slice but bears on the fuel): EIA STEO Aug 2026: "On August 3, the Texas governor announced a pause on new data center development"; STEO Sept 2026: Texas "has paused the connection of new data centers to the grid to facilitate a regulatory audit". EIA cut its 2027 Texas load growth forecast from 14% to 6%. A grid pause is a direct push toward behind-the-meter gas in Texas; the piece team should check the order itself.

---

## 3. Pipes

### 3a. How a new interstate pipe gets built (the chain a first-time investor needs)

1. **Open season.** The pipeline company offers new capacity to all comers for a fixed window. Transco SSE: 19 June to 14 July 2023 (Transco FERC application, CP25-10, 29 Oct 2024).
2. **Precedent agreements.** Shippers sign binding contracts to take capacity once built. This is the moment demand is locked in: Kinder Morgan sanctions only after "securing sufficient long-term, take-or-pay transportation agreements" (KMI, 21 Oct 2026).
3. **FERC pre-filing (optional for pipes, mandatory for LNG).** Environmental review starts before the application; 18 CFR 157.21 sets at least six months of pre-filing. SSE pre-filed Q1 2024 (Williams SSE fact sheet, Aug 2026).
4. **Certificate application under Natural Gas Act section 7(c)**, then FERC's environmental review (an EA or EIS). SSE: filed 29 Oct 2024; FERC environmental assessment Nov 2025 (**press**, P&GJ).
5. **Certificate of public convenience and necessity.** SSE: issued 29 January 2026 (Williams 10-Q: "In January 2026, Transco received FERC approval"), about 15 months after filing (calc).
6. **Other federal and state permits** (Clean Water Act section 404 from the Army Corps; state water quality certificates) and **FERC notice to proceed**. SSE: Army Corps 404 permit Feb 2026, challenged by environmental groups April 2026 (**press**, okenergytoday). Williams' NESE shows the risk: on 8 Sept 2026 the Third Circuit vacated New Jersey's water quality certification (Williams 10-Q, 2 Nov 2026).
7. **Construction and in service.** SSE: target construction start Q2 2026, in service as early as Q3 2027 (fact sheet; 10-Q).

**SSE end to end:** open season mid-2023 to service Q3 2027 at earliest is about four years (calc), for 55 miles of loop beside an existing line (26.4 miles Virginia, 28.4 North Carolina) plus compressor work at eight stations. A greenfield long-haul line takes longer: Permian Link (434 miles) sanctioned Oct 2026 for Q3 2030; Southeast Connector (about 470 miles) for Q4 2030 onward.

**Take-or-pay, defined.** The shipper pays a fixed reservation charge for its booked capacity every month whether or not it moves any gas. The pipe's revenue does not depend on whether the data centre runs. Kinder Morgan: "The larger $13.7 billion portion of the backlog represents stable, primarily take-or-pay cash flows" (Q3 2026 release; the figure is as printed, against a $14.4 billion total backlog, so treat with care and check the call transcript). Williams: Transco expansions are "fully contracted with firm transportation agreements" (10-Q, Q3 2026).

### 3b. Dated projects serving power and data centres

| Project | Owner | Capacity | Who signed / what for | Cost | Status, in service | Source |
|---|---|---|---|---|---|---|
| Southeast Supply Enhancement (CP25-10) | Williams (Transco) | 1,597 Mdth/d (1,596,900 Dth/d) | Duke, Southern, Santee Cooper 93% for power; nine local distributors | about $1.53 bn (**press**, OGJ) | FERC certificate Jan 2026; "as early as the third quarter of 2027" | Williams 10-Q 2 Nov 2026, https://www.sec.gov/Archives/edgar/data/107263/000010726326000036/wmb-20260930.htm ; FERC application 29 Oct 2024 |
| SSE II | Williams | 150+ MMcf/d | not disclosed | n/d | announced Q3 2026 | Williams Q3 release, 2 Nov 2026 |
| Power Express | Williams | 800 Mdth/d, Virginia | not disclosed | n/d | FERC filing as early as Q2 2027; service as early as Q3 2030 | Williams 10-Q |
| Dalton Lateral II | Williams | up to 460 Mdth/d to a Georgia power plant | power plant | n/d | file 2027; service as early as Q4 2029 | Williams 10-Q |
| Delta Access | Williams | 2,250 Mdth/d, "to serve growing power generation and LNG demand" | n/d | $1.5 bn (Aug 2026 release) | Q1 2029 | Williams 10-Q |
| Permian Link | Kinder Morgan (NGPL) | about 2.8 Bcf/d, about 434 miles | "new power generation for an A-rated hyperscaler", long-term take-or-pay | about $4.2 bn (KMI share about $1.6 bn) | FID Oct 2026; Q3 2030 | KMI release 21 Oct 2026, https://www.sec.gov/Archives/edgar/data/1506307/000150630726000130/kmi2026q38-kex991.htm |
| Southeast Connector | Kinder Morgan (SNG) | up to 2.6 Bcf/d, about 470 miles, Marcellus/Utica to Southeast | take-or-pay shippers | KMI share $3.1 bn | FID Oct 2026; phases from Q4 2030 | same |
| Creekside Lateral | Kinder Morgan | more than 750 MMcf/d contracted (1.3 Bcf/d capacity), Central Texas | "data center and industrial customers", take-or-pay | about $235 m | phases Q4 2026 and Q4 2027 | same |
| Hugh Brinson | Energy Transfer | Phase I about 1.5 Bcf/d, about 400 miles of 42-inch, Waha to Maypearl (south of Dallas–Fort Worth); Phase II about 2.2 Bcf/d with compression | "strong investment grade counterparties" (**press** for specs, ET release 6 Dec 2024 via BIC/UI) | about $2.7 bn both phases (**press**) | Phase I "placed into full service" 1 Sept 2026, ahead of schedule; Phase II Q1 2027 | ET Q3 2026 release, 3 Nov 2026, https://www.sec.gov/Archives/edgar/data/1276187/000127618726000066/ex991eterq32026.htm |
| Oracle supply | Energy Transfer | about 900 MMcf/d to three Oracle data centres, two in Texas | Oracle, long-term; sourced via a new lateral from Hugh Brinson and the North Texas pipeline | n/d | deliveries near Abilene began Feb 2026 (**press**) | ET Q3 2025 release, 5 Nov 2025, https://www.sec.gov/Archives/edgar/data/1276187/000127618725000116/ex991eterq32025.htm |
| Entergy Louisiana, Richland Parish | Energy Transfer | 250,000 MMBtu/d firm transport, 20 years | Entergy, to fuel its plants in Richland Parish (the Hyperion plants) | n/d | from Dec 2028 | same |
| CloudBurst | Energy Transfer (Oasis pipeline) | up to 450,000 MMBtu/d | CloudBurst campus near San Marcos, Texas, behind the meter, conditional on CloudBurst FID | n/d | Feb 2025 deal; FID not confirmed | **press**, OGJ / Business Wire 7 Feb 2025 |
| Fermi America | Energy Transfer affiliate | gas supply to Fermi's planned Texas campus | Fermi; about $30 m a year for 15 years | n/d | Sept 2025; "contingent upon ... conditions precedent ... which has not yet occurred" (at 10-K) | ET 2025 10-K, 19 Feb 2026 |
| Desert Southwest (Transwestern expansion) | Energy Transfer | 1.5 Bcf/d, 516 miles of 42-inch, nine compressor stations | Arizona utilities incl. APS and SRP (**press**) | about $5.3 bn | FID Aug 2025; Q4 2029 | **press**, ET release 6 Aug 2025 |
| MRT laterals | Energy Transfer | 150,000 MMBtu/d to two Missouri power plants under construction | power plants | reimbursable | late 2027 and mid-2028 | ET Q3 2026 release |
| South Mississippi Pipeline | Energy Transfer | 1.2 Bcf/d, 215 miles of 36-inch | long-term demand-based contracts | about $1.6 bn | FID Nov 2026; 2030 | ET Q3 2026 release |
| Homer City supply | EQT | up to 665,000 MMBtu/d via Texas Eastern and Eastern Gas Transmission | Homer City campus, exclusive supplier | n/a | agreement in principle 15 July 2025; no definitive deal found in EQT filings | **press**, Homer City release via Business Wire |
| Shippingport (Frontier Group) | EQT | about 800 MMcf/d | former 2.7 GW Bruce Mansfield coal site | n/a | in principle, July 2025 | **press**, S&P Global interview 21 July 2025 |
| MVP Boost / Southgate | EQT (operator) | +0.6 Bcf/d on MVP; Southgate 0.55 Bcf/d to North Carolina | n/d | Boost $400–540 m; Southgate $370–430 m | both mid-2028 | EQT 10-Q, 28 Oct 2026 |
| POWER Pipeline | EQT | 42-inch, Marcellus PA to Clarington hub, Ohio | open season launched Q3 2026 | n/d | n/d | EQT Q3 release, 27 Oct 2026 |

**Kinder Morgan backlog:** $14.4 bn at 30 Sept 2026, $13.2 bn of it natural gas, up $4.7 bn in the quarter; "More than 75% of the total backlog is associated with projects supporting power generation and local distribution company demand" (KMI, 21 Oct 2026). **press**: 60% the quarter before.

### 3c. Williams' "Power Innovation": a pipeline company building the power plant

Williams 10-Q, 2 Nov 2026 (https://www.sec.gov/Archives/edgar/data/107263/000010726326000036/wmb-20260930.htm):

| Project | State | MW | PPA term | Expected in service |
|---|---|---|---|---|
| Socrates (North + South) | Ohio (New Albany) | 556 | 10 years, option to extend 5 | South in service late July 2026; North "later in the fourth quarter of 2026" (release: "on track for in-service by mid-November") |
| Apollo | Ohio | 490 | 12.5 years | 2H 2027 |
| Aquila | Utah | 520 | 12.5 years | 2H 2027 and 1H 2028 |
| Socrates the Younger | Ohio | 340 | 10 years | 2H 2028 |
| Neo | Ohio | 682 | 12.5 years | 2H 2028 |
| **Total** | | **2,588 (calc)** | "primarily fixed-price" PPAs | "All expected in-service dates assume timely receipt of permits" |

- Capital: Blackstone-led investors committed $5.34 bn for 49% of the five; $4.4 bn of that equals 49% of expected total growth capex (Williams 8-K, 13 July 2026), so total capex is about $9.0 bn (calc), roughly $3.5 m per MW (calc, includes the pipe laterals). Williams called the portfolio "more than 2.6 gigawatts announced" (13 July); the 10-Q project MW sum to 2,588.
- Williams excludes "$857 million of cash purchases of certain reimbursable long-lead Power equipment" from leverage (Q3 release): it is buying machines before projects close, with the customer reimbursing if cancelled.
- 2026 growth capex guidance $7.3 to 7.9 bn, "excluding acquisitions and certain long-lead time equipment for power projects" (10-Q).

---

## 4. Equipment, labour and permitting

### 4a. Compressors: the engine queue reaches the pipe

| Date | Fact | Source |
|---|---|---|
| 5 May 2026 | USA Compression: "Certain new engine lead times have recently tripled from 50 weeks to approximately 150 weeks"; CEO: lead times "were running around 55 to 70 weeks ... And then overnight Cat went to 100 weeks or 108 weeks"; "A lot of it is driven by the generation. It's the generator orders"; coolers still 25 to 30 weeks | USAC Q1 2026 call transcript (company IR), https://s21.q4cdn.com/958148870/files/doc_earnings/2026/q1/transcript/USAC-USQ_Transcript_2026-05-05-1.pdf |
| 5 May 2026 | USAC has ordered engines for 2027, 2028 and part of 2029 | same |
| Aug 2026 | "certain new engine lead times continue to be as high as 200 weeks" | **press** (GuruFocus summary of USAC Q2 call) |
| Aug 2026 | SSE compressor scope includes a Solar Titan 130 gas turbine (23,465 hp) at Station 155 and two 33,000 hp electric motor drives at Station 165 | Williams SSE fact sheet, Aug 2026 |

The mechanism worth a sentence: the same Caterpillar-class gas engines that make on-site power also drive field and pipeline compression, so data-centre generator orders lengthen the queue for the compressors that move the gas to them. Source is one compression company's call; label it as theirs.

### 4b. Steel

- Section 232 tariffs on steel, including derivative articles, rose from 25% to 50% from 4 June 2025 (Proclamation 10947, 3 June 2025; **press** summaries by White & Case, KPMG; whitehouse.gov text not opened). Line pipe is a steel article. No pipeline company filing found quantifying the cost effect; do not assert one.
- Labour: no primary source found on pipeline construction crew shortages in 2025–26. Leave out.

### 4c. Permitting changes 2025–26

| Date | Change | Source |
|---|---|---|
| 18 June 2025 | FERC waived its Order 871 construction hold through 30 June 2026 and temporarily raised blanket certificate cost limits (projects in service by 31 May 2027) from $41 m to $61.65 m | **press** law-firm alerts (Akin Gump, Mondaq) |
| 10 Oct 2025 | FERC Order No. 915 removed 18 CFR 157.23, which barred authorising construction while rehearing requests were pending (Docket RM25-9-000, 90 FR 48221); order on rehearing published 24 Feb 2026, "not changing the outcome of the Final Rule" | Federal Register, 24 Feb 2026, https://www.govinfo.gov/content/pkg/FR-2026-02-24/pdf/2026-03658.pdf |
| 21 May 2026 | FERC proposed roughly doubling blanket certificate cost thresholds and widening eligible projects (RM25-12-001); final rule not confirmed | **press** White & Case |
| 15 Oct 2026 | FERC proposed ending routine air dispersion modelling for compressor stations and LNG | **press** Akin Gump |
| 8 Sept 2026 | Courts still bite: Third Circuit vacated New Jersey's water certificate for Transco NESE | Williams 10-Q |

Reading: the federal rules got faster in 2025–26; the state water permits and courts did not, and the pipe still needs signed shippers first.

---

## What the live piece has wrong or out of date

1. **Socrates North date.** Live: "on track for service by mid-November" (Q3 release). The 10-Q filed the same day says "later in the fourth quarter of 2026". Use both or the 10-Q; check at publish whether it is in service.
2. **"Texas LNG exports exceeded the gas burned by Texas power plants in February to April 2026."** True (EIA), but it also happened in March–April and November–December 2025. It is a shoulder-season pattern, not a 2026 turn. Reframe: Texas terminals take a steady 4.4 Bcf/d (2025) to about 5 Bcf/d (2026) year round, while power burn swings from about 4 to 8 Bcf/d.
3. **Permian table is two quarters stale.** October STEO has Q3 2026: 264 rigs, 30.2 Bcf/d (EIA estimate). The "rigs fell by a fifth, gas rose by a twelfth" contrast is a Q1-to-Q1 framing; by Q3 rigs were back up 2% on a year earlier. Keep Q1 if wanted, but date it and add Q3.
4. **"The gas itself is plentiful" with no proof of where it is scarce.** Missing the decisive dated fact: Waha below zero eight of nine months to May 2026 (EIA), and EQT curtailing 21 Bcfe in Q3 2026. These show the pipe, not the gas, is the limit.
5. **Golden Pass**: "shipped its first cargo in April 2026" is right (22 April, EIA). Add that it was still ramping at about 0.22 Bcf/d in August against 2.0 Bcf/d nominal for three trains.
6. **Transco SSE**: the live piece does not give the FERC certificate date (29 January 2026) or the construction start (target Q2 2026), and dates the pipe from open season only. "About four years for 55 miles" stands (calc).
7. **Kinder Morgan backlog**: correct ($14.4 bn; more than 75% power and local utilities). Permian Link is 434 miles and about $4.2 bn; the piece omits both. Avoid implying the hyperscaler holds all 2.8 Bcf/d.
8. **Missing major actors**: Energy Transfer (Hugh Brinson in service 1 Sept 2026; 900 MMcf/d to Oracle; 250,000 MMBtu/d to Entergy for Richland Parish from Dec 2028, which ties the pipe to Hyperion) and Williams' four further plants (2,588 MW in all, about $9 bn). Williams is now a power producer at scale, not one 400 MW site.
9. **Heat-rate scale is absent.** The piece never says how much gas a campus burns. 1 GW of combined cycle is about 0.17 Bcf/d; simple cycle about 0.25 Bcf/d. That turns "a pipe" into a number.
10. **Texas grid pause** (3 Aug 2026, EIA STEO Aug/Sept) is not mentioned and bears directly on why Texas campuses build their own power. Verify the order before use.
