# Rack research: power semiconductors and switches for 800 V

Slice for the investor-grade rebuild of `powering-the-rack`. Compiled 7 November 2026.
Tags: **primary** (company filing, release or own web page, standards body, Nvidia blog), **call** (earnings call, from a transcript unless noted), **press** (trade or financial press, leads only), **calc** (my arithmetic), **background** (standard engineering, not tied to one source). No share prices, valuations or views on shares.

---

## 1. Plain-English explainers

### What a power semiconductor does in a converter
- A converter changes one voltage into another by switching current on and off very fast, then smoothing the chopped result with coils (inductors), transformers and capacitors. The power semiconductor is the switch. **background**
- Two losses matter. Conduction loss: the switch is not a perfect wire when on, so it heats. Switching loss: in each on or off transition the switch briefly carries voltage and current at once. **background**
- Switching faster lets the coils and transformers shrink (they store less energy per cycle), so faster switches buy power density, which is what a crowded rack needs. But each transition costs a little, so faster only pays if the switch's transitions are cheap. **background**
- The switch's material sets three limits: how much voltage it can block, how hot it can run, how fast it can switch. **background**

### Silicon, silicon carbide (SiC), gallium nitride (GaN)
- Material values already in the live piece (halbleiter.org, read 6 Nov 2026): bandgap 1.12 eV silicon, 3.26 4H-SiC, 3.4 GaN; critical field about 0.3, 2.8, 3.3 MV/cm; thermal conductivity 1.5, 4.9, 1.3 W/cm.K. **primary (reference table)**
- Silicon: cheapest, mature, 300 mm wafers. Best where voltages are low (tens of volts) and at the last step next to the GPU, where power stages switch around 1 MHz from 12 V or 6 V. Above roughly 600 V silicon MOSFETs get thick and lossy; silicon IGBTs block high voltage but switch slowly. **background**
- SiC: blocks high voltage (650 V to 3.3 kV and above in products), runs hot, conducts heat about three times better than silicon. Switches faster than silicon IGBTs but slower than GaN. Natural home: medium-voltage and kilovolt stages (solid-state transformers, grid-side rectifiers, AC to DC front ends at 1,200 V) and solid-state breakers. **background**; Navitas sells SiC from 650 V to 6,500 V (live piece source); Navitas selected by US government for 10 kV SiC (Navitas Q3 2026 release, 3 Nov 2026, https://www.sec.gov/Archives/edgar/data/0001821769/000162828026069489/exhibit991-navitassemicond.htm). **primary**
- GaN: fastest switching (low charge per transition), so it wins where frequency and density matter. Most power GaN is lateral GaN-on-silicon rated 650 V or below, which is why designs stack 650 V parts to handle 800 V. **background**. That is changing:
  - Power Integrations: 1,250 V and 1,700 V PowiGaN, white paper at OCP Global Summit, October 2025, claiming >98% efficiency in 800 VDC stages. **press** (MarketChameleon/GamesBeat, 13 Oct 2025, https://marketchameleon.com/articles/b/2025/10/13/power-integrations-industry-first-1250v-1700v-gan-technology-800vdc-ai-data-centers)
  - onsemi: vertical GaN (GaN-on-GaN, made in Syracuse), demonstrated an 800 V to 6 V converter on vertical GaN at the OCP Summit (October 2026). **call/press** (onsemi Q3 2026 call, 2 Nov 2026, per MarketBeat summary https://www.marketbeat.com/instant-alerts/transcript-onsemi-q3-earnings-call-highlights-2026-11-02/)
  - Renesas: GaN rated 48 V to 400 V, stacked to 800 V, converters up to 98% efficiency (October 2025). **press** (InsideHPC, Oct 2025, https://insidehpc.com/2025/10/renesas-gan-power-semiconductors-support-nvidias-800-volt-direct-current-ai-data-center-architecture/)

### Where each sits in the 800 V chain
| Stage | What it does | Material used today or proposed | Evidence |
|---|---|---|---|
| Solid-state transformer (SST) at building edge | Medium-voltage AC (10 to 35 kV) straight to 800 V DC | SiC (high voltage, heat) | Infineon and SolarEdge SST block on Infineon SiC, 13.8 to 34.5 kV in, 800 to 1,500 V DC out (5 Nov 2025, live piece); ABB Infinitus portfolio "built around" its SST technology (21 Sep 2026, https://new.abb.com/news/detail/138900/abbs-new-direct-current-portfolio-aims-to-rewire-ai-data-center-energy-infrastructure). **primary** |
| Sidecar or power rack | 415/480 V AC to 800 V DC beside the compute rack (first phase) | SiC 1,200 V or GaN (stacked 650 V, or 1,250 V and above) in the AC to DC front end; SiC JFETs for hot-swap and protection | Infineon described SiC JFETs for protection and hot-swap and GaN near 1 MHz for its MGX 800 VDC work (May 2026). **press** (pulse.bot, https://www.pulse.bot/hardware/news/infineon-joins-nvidias-mgx-ai-factory-ecosystem-84e00286-3d7a-44fc-a546-63ad78f945e9/). Schneider sidecar at Computex, 2 to 5 June 2026 **press** |
| Power shelf (today's 54 V rack) | 415 V AC to 54 V DC inside the rack | Silicon or SiC power-factor stage, 650 V GaN or silicon in DC-DC stage | **background** |
| Intermediate bus converter (on the compute tray) | 800 V DC to 12 V or 6 V | High-voltage GaN on the 800 V side; low-voltage silicon or 100 V GaN on the output side | TI 800 V to 6 V, GaN power stages, 97.6% peak, >2,000 W/in3 (16 Mar 2026, https://www.barchart.com/story/news/779479/ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia) **primary**; Navitas GTC board: 16 x 650 V GaN stacked with 25 V silicon on output (live piece) **primary**; ST 800 V to 12 V and 800 V to 6 V to Nvidia's reference design (17 Mar 2026) **press** (https://themachinemaker.com/news/stmicroelectronics-expands-800v-dc-power-solutions-for-ai-data-centers-in-collaboration-with-nvidia/); Navitas 800 V to 12 V board with Nvidia, and 800 V to 6 V board at Computex 2026 (Navitas Q2 and Q3 2026 releases) **primary** |
| Voltage regulator next to GPU | 12 V or 6 V to below 1 V, thousands of amps | Silicon power stages (low-voltage MOSFETs with driver); some low-voltage GaN | TI 6 V to sub-1 V multiphase buck (16 Mar 2026) **primary**; MPS, Infineon, Renesas, ADI, TI make these (Nvidia partner list) |
| Solid-state breaker | Cuts a DC fault in microseconds | SiC (JFET or MOSFET), bidirectional silicon (B-TRAN), GaN for auxiliary supply | Section 4 |

Note: Vicor disputes the intermediate bus approach. Its management called an 800 V to 6 V bus design structurally misguided on its Q1 2026 call and argued for 800 V rack distribution with its own modules. **call (per press summary, pulse.bot)**. Worth one line as the dissent.

---

## 2. Supply: who makes SiC and GaN for this market

### Nvidia's named 800 V silicon partners (primary)
- **20 May 2025 Technical Blog, updated 31 July 2025** ("NVIDIA 800 V HVDC architecture will power the next generation of AI factories", https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/). Silicon providers: Analog Devices, Infineon, Innoscience, MPS, Navitas, onsemi, Renesas, ROHM, STMicroelectronics, Texas Instruments (10). Power components: Delta, Flex Power, Lead Wealth, LiteOn, Megmeet. Data centre power systems: Eaton, Schneider Electric, Vertiv. **primary**
- **13 October 2025 Technical Blog** ("Building the 800 VDC ecosystem for efficient, scalable AI factories", https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/). Silicon providers: AOS, Analog Devices, Efficient Power Conversion (EPC), Infineon, Innoscience, MPS, Navitas, onsemi, Power Integrations, Renesas, Richtek, ROHM, STMicroelectronics, Texas Instruments (14). Power components: Bizlink, Delta, Flex, Lead Wealth, LITEON, Megmeet. Data centre power systems: ABB, Eaton, GE Vernova, Heron Power, Hitachi Energy, Mitsubishi Electric, Schneider Electric, Siemens, Vertiv. The post does not discuss SiC, GaN or breakers; says the transition "will occur in phases". **primary**
- Not on either list: Wolfspeed, Vicor, Coherent. Innoscience is the only Chinese silicon provider on the list (TrendForce, press).

### Company by company (dated, own figures where found)
**Infineon** (sells Si, SiC and GaN)
- Q3 FY2026 analyst call intro statement, 5 Aug 2026 (https://www.infineon.com/row/public/documents/corporate/investors/presentations/2026/2026-08-05-q3-fy26-intro-statement-analyst-call-v01-00-en.pdf) **primary**:
  - "Demand for our AI power solutions continues to outstrip available supply, we are in allocation."
  - Dedicated AI power revenue to exceed €1.6bn in FY2026 (to 30 Sep 2026), ahead of the planned €1.5bn; more than double FY2025; plus about €500m a year of non-AI data centre power.
  - Several customers have signed or are negotiating multi-year capacity reservation agreements, cumulative "high single-digit billion Euro" sales over multiple years.
  - The €2.5bn-plus FY2027 AI data centre target will be revised upwards at the November earnings call.
  - Lead times rising, an "early-upcycle pattern as supply starts to tighten."
  - Q3 revenue €4,172m; FY2026 investment about €2.7bn.
  - Will supply 1.2 kV SiC power modules to Siemens for circuit breakers.
- FY2025 AI power revenue over €700m (press summaries; base for "more than double"). **press**
- 300 mm GaN: about €1.1bn at Villach by 2034, volume production from end 2027; EU approved €319m Austrian state aid on 27 Oct 2026. **press** (electrive 28 Oct 2026; Semiconductor Today 27 Oct 2026, https://semiconductor-today.com/news_items/2026/oct/infineon-271026.shtml). Pilot 300 mm GaN in Villach in 2024; 2.3 times the chips of a 200 mm wafer. **press**
- **Watch:** Infineon FY2026 results and FY2027 guidance due in November 2026 (after 7 Nov). Check before publishing.

**onsemi** (Si, SiC, vertical GaN)
- Q3 2026 release, 2 Nov 2026 (https://www.sec.gov/Archives/edgar/data/0001097864/000114036126041580/ef20084671_ex99-1.htm) **primary**: revenue $1,722.3m; "AI data center revenue grew 39% sequentially and 175% year-over-year"; agreement to acquire Ferric ("next generation AI processor power delivery"); 2030 AI data centre target raised by $500m to more than $3bn.
- Call, 2 Nov 2026 **call** (MarketBeat summary): AI data centre revenue about $180m in Q3; about $620m expected for 2026; roughly double again in 2027; Q4 up mid-teens percent; supply constrained in some technologies. 800 V to 6 V vertical GaN demo at OCP. Ferric price $600m plus up to $175m earn-outs (press).

**STMicroelectronics** (Si, SiC, GaN)
- 17 Mar 2026: 800 VDC to 12 V and 800 VDC to 6 V architectures to Nvidia's reference design. **press**
- Q3 2026 (29 Oct 2026): data centre revenue about $1.3bn expected for 2026, up from "more than $1bn" in July; 2027 goal well above $2bn. Mostly silicon photonics, not power. **press** (TNW, https://thenextweb.com/news/stmicroelectronics-q3-2026-results-ai-data-centres). Verify against ST's own release; do not attribute to 800 V.
- ST and Innoscience GaN agreement (March 2025). **could not verify this session** (memory lead).

**Wolfspeed** (SiC, materials and devices)
- Chapter 11 filed June 2025 (prepackaged), emerged 29 Sep 2025. **press** (CNYBJ; BusinessWire). Debt cut about 70% (Motley Fool, press).
- Renesas, which had a $2.062bn wafer-supply deposit with Wolfspeed, converted it under the restructuring and booked a ¥235bn loss in H1 2025 (Renesas release, 24 Jul 2025, https://www.businesswire.com/news/home/20250724609612/en/). **primary**
- 150 mm device production at Durham shut down; all device production moved to 200 mm at Mohawk Valley (Marcy, NY); Durham now materials. **press** (Semiconductor Today, May/Aug 2026; Wolfspeed BusinessWire 4 Feb 2026).
- FY2026 10-K (year to 28 Jun 2026): https://www.sec.gov/Archives/edgar/data/0000895419/000089541926000054/wolf-20260628.htm. Press summaries say data centre revenue more than doubled FY2025 to FY2026 and rose about 20% quarter on quarter in Q4 FY2026; Q4 revenue about $150m, down 24% year on year. **press, check against the 10-K**

**Navitas** (GaN and SiC)
- 8-K, 1 Jul 2025: TSMC "will end GaN production in July 2027"; 650 V parts move to Powerchip (PSMC) "over the next approximately 12-24 months". **primary** (in live piece). TSMC's own statement: "gradually exit the GaN business over the next two years" **press** (TrendForce, LEDinside).
- PSMC 200 mm GaN-on-silicon at Fab 8B, Zhunan. **press** (Compound Semiconductor).
- **New since the piece's GaN section was written:** GlobalFoundries partnership, 20 Nov 2025, 200 mm GaN-on-silicon at Burlington, Vermont, for AI data centres and grid (GF release, https://investors.gf.com/news-releases/news-release-details/globalfoundries-and-navitas-semiconductor-partner-accelerate-us). **primary**. Q3 2026 release (3 Nov 2026): "first shipments of the latest Gen 5 GaNFast devices manufactured in the United States through GlobalFoundries". **primary**
- Q2 2026 call (27 Jul 2026): secured buffer capacity at TSMC to support existing customers "through 2029 and beyond"; inventory build to bridge the 8-inch transition; management expects the 800 V transition in 2027, in steps. **call (MarketBeat summary)**
- Q3 2026: revenue $14.0m (+38% y/y); Q4 guide $16.0m; AI data centres plus grid to exceed one-third of sales by year end (Q2 release). **primary**. Small company: scale context for any "GaN supply" claim.

**Innoscience** (GaN, China, IDM with own 200 mm fabs)
- Interim results to 30 Jun 2026 (HKEX, 28 Aug 2026, https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0828/2026082803672.pdf): AI and data centre chip shipments +183% y/y; revenue +50.6%; total shipments 547m chips; gross margin 11.6%; company says shipments "mainly reflect customer design-ins". **primary**
- Legal dispute with Infineon over GaN patents. **press** (eeNews), not checked.

**Texas Instruments**: see section 3.

**Monolithic Power Systems** (silicon power stages and modules next to the processor)
- Q3 2026 release, 29 Oct 2026 (https://www.sec.gov/Archives/edgar/data/0001280452/000162828026068202/mpwr-20260930xexx991.htm): Enterprise Data revenue $506.7m, +33.2% q/q, +164.6% y/y, 42.1% of revenue; total $1,202.4m. **primary** (figures via search excerpt of the 8-K; re-read before use). 2026 Enterprise Data growth floor raised to 150% **call/press**.

**Vicor** (modules, 48 V and 800 V factorised power)
- Q3 2026 reported 20 Oct 2026; revenue about $197m (+79% y/y) **press**; gross margin 68.3% with royalty income **call**. 8-K: https://www.sec.gov/Archives/edgar/data/0000751978/000119312526425697/d153882dex991.htm. No separate data centre figure found.

**Power Integrations**: 1,250 V and 1,700 V GaN (Oct 2025) **press**; on Nvidia's Oct 2025 list **primary**; rack AC to DC GaN samples by end 2025, main DC-DC product planned 2027 (Q3 2025 call) **call**. Q3 2026 results not found.

**Renesas**: GaN for 800 V (Oct 2025); 650 V GaN in dual-side-cooled package for 800 V HVDC (30 Sep 2026) **press**. Wolfspeed deposit loss above **primary**. Whether Renesas formally dropped its own SiC plans: **could not verify**.

**EPC, AOS, Richtek, ROHM, ADI**: on Nvidia's list (primary). AOS: 1,200 V SiC, 650 V and 100 V GaN for 800 VDC **press** (Power Electronics News). No data centre revenue figures sought.

### Wafers, capacity, shortages
- SiC: industry moving from 150 mm to 200 mm. Wolfspeed's device output is now all 200 mm **press**. Chinese 150 mm SiC substrates moved from shortage to oversupply by late 2024 with steep price falls; Chinese makers (SICC, TankeBlue) pivoting to 200 mm and developing 300 mm. **press** (SemiMedia, Digitimes, TrendForce). No reliable 200 mm price series found. Read: SiC is not short; the bottleneck story does not run through SiC substrates.
- GaN: 200 mm GaN-on-silicon is the volume standard (PSMC, GlobalFoundries Burlington, Innoscience). 300 mm GaN is Infineon's bet, volume from end 2027 **press**. TSMC exits by July 2027 **primary (Navitas 8-K)**.
- Tightness: the clearest primary statement is Infineon's "we are in allocation" for AI power and rising lead times (5 Aug 2026). onsemi says supply constrained in some technologies (call, 2 Nov 2026). This is for AI power products broadly (mostly silicon power stages, controllers and some SiC/GaN), not specifically for 800 V parts.

---

## 3. Texas Instruments (claim `ti-feeds-the-chip`)

**Data centre revenue, TI's own words**
| Period | Statement | Source |
|---|---|---|
| FY2025 | "Data center was $1.5 billion, up 64% year on year and was 9% of revenue." First year TI reported data centre as its own end market. | Q4 2025 call, 27 Jan 2026 **call** (AlphaStreet transcript excerpt; MarketBeat) |
| Q4 2025 | Up about 70% y/y; exit run rate about $450m a quarter | **call (Fintool summary)** |
| Q2 2026 | "Data center doubled year-on-year and grew around 20% sequentially" | Q2 call, 22 Jul 2026 **call** (Webull transcript). Release: revenue $5.46bn, "broad growth led by industrial, data center and automotive" **primary** (https://www.sec.gov/Archives/edgar/data/0000097476/000009747626000148/q22026txnex99-eredgar.htm) |
| Q3 2026 | "Data center was up about 95% year-on-year and grew about 20% sequentially"; about 13% of revenue (per analyst and summaries); "We are not seeing any slowdown." | Q3 call, 21 Oct 2026 **call** (Webull/Motley Fool transcript, https://www.webull.com/news/15789174635930624) |
| Q3 2026 | Revenue $6,055m (+28% y/y); Analog $4,911m (+32%); gross profit $3,887m; capex $463m vs $1,197m a year earlier; release gives no data centre figure | 8-K exhibit, 21 Oct 2026 **primary** (https://www.sec.gov/Archives/edgar/data/0000097476/000009747626000165/q32026txnex99-eredgar.htm) |
- calc: 13% x $6,055m = about $790m in Q3 2026, roughly a $3.1bn annual run rate, against $1.5bn for all of 2025. Label as derived from management's rounded share.
- calc: gross margin 64.2% in Q3 2026 ($3,887m / $6,055m); CFO said up 280 bp q/q, "really driven by higher revenue" **call**. Relevant to the claim's watch item "gross margin as new Sherman capacity comes online".

**What TI says drives it** (Q3 2026 call) **call**
- "Power density is critical." (Ilan)
- "When there is more power there is more opportunity for TI." "When there is higher voltages, more opportunity for TI." (Mike Beckman, investor relations)
- About 10,000 part numbers sold into data centre.
- The phrase "800 volt" does not appear in the Q3 transcript (search of the Webull copy). So TI does not attribute the growth to 800 V; it names density and higher voltage together. The live piece's reading ("the growth so far is density, not 800 volts") is consistent with the call.

**48 V and 800 V products**
- 16 Mar 2026 (GTC): "complete 800 VDC power architecture" with Nvidia: 800 V to 6 V isolated bus converter with integrated GaN, 97.6% peak efficiency, >2,000 W/in3; 6 V to sub-1 V multiphase buck for GPU cores; also an 800 V hot-swap controller and a 30 kW AC to DC supply. **primary** (TI release via Barchart, https://www.barchart.com/story/news/779479/ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia); the hot-swap and 30 kW items are from an aggregator **press**.
- 97.6% is peak, not full-load or system efficiency. Note in the piece.
- TI's 48 V and 54 V parts (hot-swap and eFuse controllers, 48 V to 12 V converters, power stages) are the parts shipping in today's racks. Specific part numbers not checked this session.

**Own fabs**
- More than $60bn across seven US fabs, announced 18 June 2025: Sherman (up to $40bn, SM1 to SM4), Richardson (RFAB1, RFAB2), Lehi (LFAB1, LFAB2). **press** (Tom's Hardware, Business Facilities 20 Jun 2025); TI's own release not retrieved.
- SM1 in Sherman began production on 17 Dec 2025; will ramp "to tens of millions of chips per day" at full scale. **primary** (TI blog, https://www.ti.com/about-ti/newsroom/company-blog/the-future-starts-with-the-first-our-newest-300mm-wafer-fab-is-in-production.html)
- Lehi: foundry business moved into LFAB1, "plenty of clean room in Lehi I"; LFAB2 shell in "the last stages of completion" (Q3 2026 call) **call**.
- TI's GaN is made in-house (Dallas, and Aizu, Japan, with a 2024 plan to quadruple GaN output): **could not verify this session**.

**For the claim box**: claim says the 800 V move turns TI's chips into a growing data centre business. The growing business is real and in TI's own words; the cause named (800 V) is not yet shown, because volume racks run at 48 to 54 V and TI itself pairs density with voltage. That is what the live piece already says. No change needed beyond updating the numbers above.

---

## 4. The off switch: DC fault interruption at 800 V

**Why it is hard** **background**: AC current crosses zero 100 or 120 times a second, and a mechanical breaker extinguishes its arc there. DC has no zero, so a mechanical DC breaker must force the current down against a sustained arc (bigger contacts, arc chutes, slower). A solid-state breaker (SSCB) uses semiconductors to cut current in microseconds with no arc, at the price of on-state loss (heat) all the time. Infineon, 10 Sep 2026: "Without a natural current zero, mechanical interruption faces challenges with arcing" (live piece). Ideal Power CEO, 12 Oct 2026: "Mechanical breakers are too slow, while previous semiconductor-based breakers have historically been disqualified by high power loss." **primary**

**Nvidia's own design note** (20 May 2025 blog, updated 31 Jul 2025) **primary**: overcurrent protection at the power room/hall, hall/row and row/rack boundaries, with "emerging solid-state devices or safety breakers" as options beside fuse-and-disconnect; "Innovations will still be required to fully deliver possible overcurrent protection reliability and maintenance gains."

**Products and dates**
| Maker | Product | Date | Ratings / certification | Tag and source |
|---|---|---|---|---|
| ABB | SACE Infinitus SSCB | Marine launch earlier (date not verified); Japan premiere CEATEC Oct 2023 | ABB claims world's first SSCB with full IEC 60947-2 certification; up to 2,500 A frame, up to 1,250 V DC (ABB product page per search); breaking in about 15 microseconds | **primary (ABB pages, via search; page fetch timed out)** https://new.abb.com/low-voltage/products/circuit-breakers/sace-infinitus |
| ABB | Infinitus source-to-rack DC portfolio (SST, DC distribution, DC protection) | 21 Sep 2026 | Several components in production within 12 months; first DC-native facilities on the full portfolio in two to three years; 25 to 40% of new data centre capacity installed in 2030 could be DC | **primary** https://new.abb.com/news/detail/138900/ |
| ABB and Nvidia | Collaboration on 800 VDC including SSCB | 13 to 14 Oct 2025 | | **primary** (ABB release) |
| Siemens | SENTRON 3QD2 semiconductor circuit breaker and SIRIUS 3RF5 solid-state switch, low-voltage DC | April 2026, Hannover Messe | Interrupts short circuits in microseconds, "up to 1,000 times faster"; positioned for data centres and AI factories; Infineon supplies 1.2 kV CoolSiC modules | **primary** (https://press.siemens.com/global/en/pressrelease/siemens-launches-groundbreaking-portfolio-era-direct-current-technology; Infineon 5 Aug 2026 statement). 800 V data centre rating not confirmed |
| Infineon and SolarEdge | SSCB for 800 VDC data centres on CoolSiC JFETs, SolarEdge leads design | 10 Sep 2026 (Semiconductor Today date; live piece says 9 Sep) | Faults cut "within a few microseconds"; no rating, availability or certification stated | **press/primary** https://semiconductor-today.com/news_items/2026/sep/infineon-100926.shtml |
| Power Integrations and Ideal Power | SSCB combining 1,700 V InnoMux-2 GaN IC (self-powering from the 800 V bus) with B-TRAN bidirectional silicon switch | 12 Oct 2026 | Working prototype; reference design in development; no certification | **primary** (POWI release PDF, https://s25.q4cdn.com/829851629/files/doc_news/Power-Integrations-and-Ideal-Power-Collaborate-on-Efficient-Always-On-Solid-State-Circuit-Breakers-for-800-VDC-AI-Data-Centers-2026.pdf) |
| Atom Power | Atom Switch digital SSCB (AC building distribution) | Gen 1 May 2019, Gen 2 Dec 2019 (SiC) | UL 489I listed; company calls it the first | **press** (Control Engineering; Semiconductor Today Dec 2019) |
| Eaton | 800 VDC architecture for AI factories; bought Resilient Power Systems (SST) | Architecture 25 Sep 2025; acquisition completed 6 Aug 2025 | No dedicated Eaton 800 V SSCB launch found; Eaton markets Bussmann DC fuses and high-speed DC protection for ±400/800 VDC | **primary** (Eaton news index) / **press** |
| Schneider Electric | 800 VDC sidecar, up to 1.2 MW racks, Computex 2 to 5 Jun 2026 | | Protection described generally (fault current and arc-flash analysis); no SSCB named | **press** |

**Standards**
- IEC 60947-2 (low-voltage circuit breakers) is what ABB cites for SSCB certification. **primary (ABB claim)**
- UL 489I is the listing Atom Power cites for solid-state breakers. **press**. Whether UL 489I covers DC data centre buses at 800 V, and the status of any UL/IEC work specific to 800 VDC data centres, **could not verify**.
- Nvidia (13 Oct 2025): industry "must align on common voltage ranges, connector interfaces, and safety practices for 800 VDC environments". **primary**

**Read for the piece**: the live section says the building step "waits on a new class of breaker". The class exists: ABB has a certified SSCB (IEC 60947-2, to 1,250 V DC by its own page), Siemens launched one in April 2026, and three 800 V data centre efforts were announced in Sep to Oct 2026. What is missing is data-centre-specific ratings at 800 V, field record, and settled rules, not the device. Reword to "a new class of breaker that exists but is not yet rated, standardised or proven in data halls".

---

## 5. What the live piece has wrong or out of date

1. **"GaN ... takes 800 volts by stacking parts rated at 650."** True of the Navitas and Renesas designs, but no longer the only route: Power Integrations has 1,250 V and 1,700 V GaN (Oct 2025), onsemi showed 800 V to 6 V on vertical GaN (OCP, Oct 2026). Say "mostly by stacking 650 V parts, though 1,200 V-class GaN is arriving".
2. **GaN supply section is incomplete.** It cites the TSMC exit and the PSMC move but omits Navitas's second US source (GlobalFoundries Burlington, partnership 20 Nov 2025, first Gen 5 shipments announced 3 Nov 2026) and the TSMC buffer capacity through 2029 (Q2 2026 call). Both weaken the requalification-timing risk the piece leans on.
3. **"I concede this is not a shortage call."** Keep, but add the strongest primary fact on supply: Infineon, 5 Aug 2026, "we are in allocation" for AI power, with multi-year capacity reservation agreements worth a high single-digit billion euros and rising lead times. That is AI power broadly, not GaN at 800 V. onsemi says supply constrained in some technologies (2 Nov 2026).
4. **"SiC makers wait longest."** Consistent with evidence, but note SiC is in oversupply at the substrate level (Chinese 150 mm prices collapsed, press) and Wolfspeed restructured through Chapter 11 (June to 29 Sep 2025), while SiC enters data halls early in breakers (Siemens with Infineon 1.2 kV SiC; Infineon and SolarEdge SiC JFETs). The piece already makes the breaker point; add the supply fact.
5. **Off switch section.** Treats solid-state breakers as an emerging class. Add ABB SACE Infinitus (IEC 60947-2, ABB's "first" claim), ABB Infinitus portfolio (21 Sep 2026: first DC-native facilities "within two to three years", which supports the building-waits claim), Siemens 3QD2 (April 2026), Power Integrations and Ideal Power (12 Oct 2026, prototype only). Infineon and SolarEdge date: the piece says 9 Sep 2026, Semiconductor Today dates it 10 Sep 2026. Check Infineon's release dateline.
6. **Nvidia partner lists.** If the piece names "Nvidia's partners", use the 13 Oct 2025 list of 14 silicon providers (adds AOS, EPC, Power Integrations, Richtek to the May 2025 list of 10). The "Who makes it" table could add Power Integrations, onsemi and ST to the GaN row and onsemi, MPS to the board-to-chip row.
7. **TI numbers are right** as far as checked (9%, about $1.5bn in 2025; doubled Q2 2026; about 95% and about 13% in Q3 2026). Add: up 64% in 2025; about $790m in Q3 2026 (calc); "800 volt" not mentioned on the Q3 call; SM1 in production since 17 Dec 2025; Q3 capex down to $463m.
8. **Data centre revenue at peers, for scale (none in the piece):** onsemi AI DC $180m in Q3 2026, about $620m for 2026 (call); Infineon >€1.6bn AI power FY2026 (primary); MPS Enterprise Data $506.7m Q3 2026 (primary); Navitas total revenue only $14.0m in Q3 2026 (primary). GaN pure plays are tiny next to silicon power-stage makers, which supports "silicon stays at the last step" and suggests the money flowing now is in silicon VRs, not GaN.
9. **Infineon FY2027 AI target** will be revised at its November 2026 results, which fall just after this research date. Re-check before publishing.

## 6. Could not verify

- TSMC's own statement on the GaN exit (only press quotes; Navitas 8-K is primary).
- PSMC 200 mm qualification status for Navitas in 2026.
- Whether Renesas formally abandoned its own SiC production plans (only the ¥235bn Wolfspeed deposit loss is primary).
- ABB SACE Infinitus original launch date and the 1,250 V DC rating (ABB page timed out; ratings from search excerpt of ABB's page).
- Whether any SSCB holds a UL listing or IEC certification for 800 V DC data centre use; status of UL 489I scope at 800 V DC.
- Siemens 3QD2 voltage rating (Infineon supplies 1.2 kV modules; Siemens 800 V data centre rating not confirmed).
- Eaton or Schneider dedicated SSCB product for 800 VDC.
- ST's own Q3 2026 data centre figure (press only) and ST and Innoscience GaN agreement terms.
- Wolfspeed data centre revenue growth from the 10-K itself (press summaries only).
- MPS and Vicor figures read from the 8-K only through search excerpts; Vicor revenue from press.
- TI's in-house GaN fabs (Dallas, Aizu) and specific 48 V part numbers.
- TI's 13% Q3 2026 share is from analyst wording and summaries; the verbatim management sentence found is "up about 95% year-on-year and grew about 20% sequentially".
- Power Integrations Q3 2026 results.
- Any SiC or GaN lead-time figure in weeks from a primary source.
