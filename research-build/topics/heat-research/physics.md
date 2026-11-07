# Heat research slice 1: the physics and engineering of cooling, chip to roof

For the depth rebuild of `heat-and-water`. Research only, 7 November 2026. Nothing here is published.

Tags: **[primary]** the maker, regulator, lab or standards body's own document, opened by me; **[press]** lead only, not for the piece without a primary; **[calc]** my arithmetic, method shown; **[background]** textbook physics or standard definitions, safe to state without a dated source.

Page references to the LBNL report give both the printed page number and the PDF page, because earlier sidecar notes used PDF pages. PDF page = printed page + 1.

---

## 1. Why almost every watt becomes heat, and how much a rack sheds

**The physics [background].** A chip does no lasting mechanical work, lifts nothing and stores almost nothing. Electrical energy that enters a server leaves it as heat, apart from tiny amounts carried out as light in optical links and signals on cables, which are themselves absorbed as heat nearby. So for cooling purposes, rack power in kilowatts equals rack heat in kilowatts. A watt is one joule per second; a 120 kW rack releases 120 kilojoules every second, about eighty 1.5 kW hairdryers on full [calc].

**Rack heat by generation.** Nvidia publishes very few rack totals. What exists:

| Rack | Figure | Source, date | Tag |
|---|---|---|---|
| GB200 NVL72 | "The rack power consumption is approximately 120kW"; eight power shelves at "33kW per power shelf" input | Nvidia DGX GB200 User Guide, hardware page, docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html (read 7 Nov 2026) | primary |
| GB200 NVL72 | "provisioned rack power" 125 kW under static provisioning, 90 kW with Nvidia's MaxLPS software, on a representative inference workload | Nvidia Technical Blog, "Maximizing AI Factory Performance per Watt with NVIDIA DSX MaxLPS", Sarah McKenney and Harry Petty, 24 Aug 2026 | primary |
| Blackwell (GB200) | hyperscale halls now support "over 135 kW per rack"; NVLink "full-rack power density of 120 kW" | Nvidia blog, Marc Hamilton, "NVIDIA Blackwell Platform Boosts Water Efficiency by Over 300x", 22 Apr 2025 | primary |
| GB300 NVL72 | No Nvidia rack total found. Vertiv's reference rack for it: "Up to 142 kW per rack, with approximately 85% liquid and 15% air cooling" | Vertiv SmartIT for NVIDIA GB300 NVL72 datasheet (SL-80699, file metadata March 2025) | primary (Vertiv, not Nvidia) |
| GB300 NVL72 | 132 kW nominal, about 155 kW peak (HPE); 135 kW (Lenovo); 132 kW (Supermicro) | OEM pages via search, see rack-research/architecture.md | press |
| Vera Rubin NVL72 | 136 kW provisioned, 101 kW with MaxLPS. Caution: the text says Vera Rubin, the figure's caption and alt text say GB300 NVL72 | Nvidia, 24 Aug 2026 (MaxLPS post) | primary, internally inconsistent |
| Vera Rubin NVL72 | Nvidia's Gen 2 rack power architecture is rated "330 kW per rack", a ceiling not a draw; TrendForce estimates about 225 kW | rack-research/architecture.md | primary (ceiling) / press |
| Kyber, Rubin Ultra | About 600 kW as shown at GTC, 18 Mar 2025 (keynote, via press). Nvidia re-introduced Kyber on 16 Mar 2026 as a standalone NVL144 with no kW and no date; press reported a slip to 2028, Nvidia said "Our roadmap is intact" | Nvidia Technical Blog, "NVIDIA Vera Rubin POD", 16 Mar 2026; Tom's Hardware, Jul 2026 | primary (no kW) / press |
| 800 V racks | 800 VDC scales racks "from 100 kW to over 1 MW"; 1 MW racks from 2027 | Nvidia Technical Blog, 20 May 2025 | primary |
| Google | 48 V racks scaled "from 10 kilowatts to 100 kilowatts"; "ML will require more than 500 kW per IT rack before 2030" | Google Cloud blog, Iyengar and Huffman, 30 Apr 2025 | primary |
| Typical rack | about 7.5 kW average in 2025 (6.8 kW in 2024) | Uptime survey via The Register, 3 Aug 2025 | press |

**Takeaway for the piece.** Nvidia's own number for a Blackwell rack is about 120 kW (GB200). "About 140 kW" is Vertiv's GB300 design envelope (142 kW) and the Jane Street tour figure, not an Nvidia figure. The Rubin rack power is not published by Nvidia as a draw. Use ranges, not a single Rubin number.

---

## 2. Why air fails above some rack density

**Heat capacity [background, calc].** Air at about 30°C holds 1.16 kg per cubic metre and 1.006 kJ per kg per degree, so a cubic metre of air carries about 1.17 kJ per degree. A cubic metre of water carries about 4,160 kJ per degree. Water carries about 3,600 times more heat per unit volume than air for the same temperature rise [calc]. That ratio is the whole story of why liquid wins at density.

**Airflow per kilowatt [calc].** Airflow needed = heat ÷ (volumetric heat capacity × temperature rise across the server).
- At a 15°C rise: 0.057 m³ per second per kW, about **120 cubic feet per minute (cfm) per kW**.
- At 20°C: about 90 cfm per kW. At 10°C: about 180 cfm per kW.
- A 120 kW rack at a 15°C rise needs about 14,500 cfm; a 142 kW rack about 17,200 cfm.
- Check against ASHRAE [primary]: "Air flows of a 40 to 50 kW rack could be up to 5000 cfm. Floor tile best-in-class is 1900 cfm." That is 100 to 125 cfm per kW, matching the calc. A 120 kW rack would need the air of about eight best-in-class floor tiles [calc]. ASHRAE TC 9.9, "Emergence and Expansion of Liquid Cooling in Mainstream Data Centers", white paper, 2021.

**Fan power [primary].** Same ASHRAE paper (2021): during the multicore era server fan power fell "to below 2% in many cases"; now "A fan power percentage of 10% to 20% is not uncommon for some of the denser servers." "In a 50 kW rack, the fan power translates to be at least 5 kW." Fans run on the same UPS as the server, so a rise from 2% to 10% fan power "equates to reducing the data center UPS capacity by 8%". Fan power rises roughly with the cube of fan speed [background], so pushing air harder gets expensive fast.

**Where the line sits.** No standards body publishes a single kW-per-rack limit for air. ASHRAE (2021) frames it by chip: as socket power moves "through 300 W toward 400 W, standard 1U and 2U servers become more difficult" to air cool. The live map's line "Air stops working somewhere between 30 and 50 kilowatts per rack" has no primary source (flagged in heat-and-water.sidecar.md). The ASHRAE 40 to 50 kW, 5,000 cfm sentence is the nearest primary anchor. Microsoft (Scott Guthrie, 18 Sep 2025) [primary]: "Traditional air cooling can't handle the density of modern AI hardware."

**ASHRAE air classes [press for the numbers; the book is paywalled].** Inlet air temperature at the server. Recommended range for A1 to A4: 18 to 27°C. Allowable: A1 15 to 32°C; A2 10 to 35°C; A3 5 to 40°C; A4 5 to 45°C. The fifth edition (2021) added **H1** for high-density air-cooled servers: recommended 18 to 22°C; allowable lower bound quoted as 5°C or 15°C in different secondary sources, upper 25°C. ASHRAE (2021 white paper) [primary] confirms H1 was defined for dense equipment, "with the suggestion that they be segregated into a more controlled portion of the data center". Read the class numbers as secondary until the ASHRAE Thermal Guidelines 5th edition table is seen.

**ASHRAE liquid classes [primary].** ASHRAE (2021 white paper, p.4): "the W classes are being renamed with the upper temperature limits incorporated in the name. All classes will carry a lower temperature limit of 2°C ... W17 (previously W1), W27 (W2), W32 (W3), W40 (new), W45 (W4), and W+ (W5)." The number is the highest **facility water supply temperature** the equipment must run on at full, unthrottled performance ("operating within a particular environmental class requires full performance of the equipment over the entire environmental range of the specified class"). W+ is above 45°C. Included in Thermal Guidelines 5th edition (2021).

**ASHRAE's own warning, which Nvidia then went against [primary].** The same paper (2021, pp.13 to 14): "It is highly likely, however, that the DLC products of today might have the ability to operate on W45 (W4). In the future, they may be replaced by newer, higher-powered products only capable of W32 (W3) operation, and eventually cooling requirements may drive facility water temperatures down into the W27 (W2) range." And: "ultra-high water temperatures of W45 and beyond will become increasingly difficult to use as the heat flux at the socket increases." Also: "Most cold plate solutions today can live easily on W32 water with case temperatures in the 80°C to 90°C range." This is a strong piece of tension for the rebuild: in 2021 the standards body expected hotter chips to need colder water; in 2026 Nvidia specified 45°C water for its hottest rack. A reader should be told both.

---

## 3. Cold plates, CDUs, loops, coolant, flow and temperatures

**The chain [background, with primary anchors].**
1. **Cold plate**: a copper block screwed onto the chip package with fine internal channels; coolant runs through it and picks up heat by conduction and convection. GB200 and GB300 compute trays use cold plates on CPUs and GPUs (Nvidia DGX GB200 User Guide: "The compute trays are cooled by liquid"; networking and storage stay on air) [primary].
2. **Technology cooling system (TCS) or secondary loop**: the sealed loop through the racks. Nvidia's coolant: "75% water and 25% propylene glycol" (Nvidia blog, Josh Parker, 21 Jun 2026) [primary], the mix called **PG25**; glycol stops freezing and, with inhibitors, bacterial growth and corrosion [background].
3. **Coolant distribution unit (CDU)**: pumps, filters and a liquid-to-liquid heat exchanger that hands heat from the sealed rack loop to the building's water without the two mixing. In-rack or in-row. Vertiv's GB300 rack pairs with a "CoolChip CDU 121, 121 kW in-rack" or external CDU1350/CDU2300 units [primary, Vertiv datasheet]. Google's CDU is Project Deschutes, "~99.999%" fleet CDU availability since 2020 (Google, 30 Apr 2025) [primary].
4. **Facility water system (FWS)**: the building loop to the roof plant. This is the loop the ASHRAE W class describes.
5. **Heat rejection**: tower, dry cooler, adiabatic cooler, chiller (section 5).

**Approach across the CDU.** Nvidia (16 Mar 2026, Vera Rubin POD post) [primary]: "All MGX racks are universally designed to operate with 45°C (113°F) warm-water inlet temperatures" and the design can "provide 41°C (105.8°F) water to coolant distribution units (CDUs)". So the building water arrives at about 41°C and the rack loop leaves the CDU at about 45°C: a 4°C approach. CoolIT CDUs quoted at a "5°C approach temperature" (Nvidia, 22 Apr 2025) [primary]. **Correction to the live piece below: 45°C is the rack-loop inlet, not the building water.**

**Return temperature.** Nvidia (21 Jun 2026) [primary, verified, Josh Parker, "Hotter Than a Hot Tub: The 45°C Breakthrough to Cool AI's Biggest Machines"]: "the coolant entering a fully liquid-cooled chip at 45 degrees Celsius exits at roughly 55 degrees." Up to "45 degrees Celsius, or 113 degrees Fahrenheit". "Hot tubs sit at about 38 to 40 degrees Celsius."

**Flow per kW [calc].** Flow = heat ÷ (density × specific heat × temperature rise). With a 10°C rise (45 in, 55 out):
- Water: about 1.44 litres per minute per kW.
- PG25 (specific heat about 3.95 kJ/kg·K, density about 1.02 kg/L at 40 to 50°C [background, approximate]): about **1.5 litres per minute per kW**.
- A 120 kW rack: about 180 L/min; a 142 kW rack about 210 L/min, if all heat went to liquid. With 85% to liquid, about 180 L/min for 142 kW [calc].
- One CDU maker quotes 1.2 LPM/kW (press). Lenovo's GB300 NVL72 table reportedly lists 59 LPM at 25°C supply and 119 LPM at 40°C supply (press via GPU Smith): warmer supply means a smaller temperature rise is allowed, so more flow is needed. Do not use without the Lenovo document.

**Earlier generations' coolant temperatures.** Press variously says Blackwell needed 35°C or ran around 40°C; Nvidia's own lines: "Lower inlet temperatures of 35°C require data centers to divert massive amounts of facility power or water for cooling" (16 Mar 2026) [primary], but I found no Nvidia document stating the GB200 or GB300 rack inlet limit. Flagged below.

**Share of heat to liquid vs air.**
- Blackwell: "NVIDIA Blackwell systems reduce cooling overhead, operating around 1.25 PUE, with about 20% of capacity air-cooled" (Nvidia Technical Blog, "Scaling Token Factory Revenue and AI Efficiency by Maximizing Performance per Watt", Moseley, Perez and Mahajan, 25 Mar 2026) [primary].
- GB300 rack: "approximately 85% liquid / 15% air" (Vertiv datasheet) [primary, Vertiv]. 15% of 142 kW is about 21 kW still to air per rack [calc], itself more than two typical 7.5 kW racks.
- Jane Street hall: 85 to 90% through cold plates (video tour, 15 May 2026; in the live piece, not re-verified here).
- Vera Rubin: "moving to 100% liquid cooling and tightening the die-to-water thermal path, enabling AI factories to run at 1.1 PUE" (Nvidia, 25 Mar 2026) [primary]; "MGX racks can be 100% liquid-cooled"; "cable-free, hose-free, and fanless compute and NVLink switch trays" (16 Mar 2026) [primary]; "no fans anywhere in the system" (21 Jun 2026) [primary]. The hall still has air-cooled storage, networking and CPU-only racks; Microsoft's Fairwater keeps "the remaining 10%" of capacity on outdoor air (18 Sep 2025) [primary].

**Why warm coolant works for the chip [background].** The silicon junction tolerates roughly 85 to 105°C. Heat flows from junction to coolant through the die, the lid or bare die, the thermal interface material and the cold plate. The better that path (Nvidia: "tightening the die-to-water thermal path"), the warmer the coolant can be for the same junction temperature. Nvidia: "Maintaining 45 °C inlet water preserves silicon temperatures and reliability" (25 Mar 2026) [primary].

---

## 4. Immersion cooling

**What it is [background].** Servers are submerged in a non-conducting liquid. **Single-phase**: a hydrocarbon or synthetic oil stays liquid and is pumped through a heat exchanger. **Two-phase**: a fluid that boils at around 50°C absorbs heat as it boils (latent heat), the vapour condenses on a cooled coil in the tank lid and rains back.

**Who has used it [primary/press].** Microsoft ran two-phase immersion in production in one rack of 48 servers at Quincy, Washington, with Wiwynn, disclosed 6 April 2021 (Microsoft innovation story, news.microsoft.com/innovation-stories/datacenter-liquid-cooling/; earlier tests found 5 to 15% lower server power) [primary page found via search, numbers via press]. Crypto miners and some HPC sites use single-phase tanks [background].

**Two-phase fluids are PFAS.** 3M's 10-K for 2025 says it "completed its exit of PFAS manufacturing at the end of 2025" (SEC EDGAR, 3M FY2025 10-K) [primary, via search snippet]. Two-phase vendors (Zutacore, LiquidStack, Wiwynn) referenced 3M Novec; Solvay's Galden replacement is also a PFAS (DCD, 2023) [press]. Single-phase is unaffected.

**Does it matter for AI racks now?** Nvidia's rack designs (GB200, GB300, Vera Rubin) are built around cold plates, with Rubin trays "hose-free" and plumbed to blind-mate manifolds [primary]. I found no Nvidia statement qualifying any NVL72 rack for immersion, and no Nvidia statement forbidding it. LBNL's liquid category lumps "rear door heat exchanger, direct-to-chip, and immersion" together (Table 4.2, printed p.42) [primary]. Conclusion for the piece: immersion is a side branch for AI in 2026; the mainstream path is single-phase cold plates. Say so in one paragraph, labelled as the state of play, not a forecast.

---

## 5. Heat rejection: towers, dry coolers, adiabatic, chillers, and the hottest afternoon

**Dry bulb and wet bulb [background].** Dry-bulb is the ordinary air temperature. Wet-bulb is what a thermometer wrapped in a wet cloth reads in moving air: evaporation cools it, and the drier the air the more it cools. In a desert at 40°C dry bulb, wet bulb might be about 20 to 24°C; in humid Singapore at 33°C dry bulb, about 27 to 28°C. Wet bulb is never above dry bulb.

**Cooling tower [background, primary for terms].** Warm water is sprayed over fill while fans pull air through; a small part evaporates and takes heat with it. A tower can cool water to a few degrees above the **wet-bulb** temperature (its "approach"), so below the air temperature. US DOE FEMP, Best Management Practice #10 [primary, undated page]: "Make-Up = Evaporation + Blowdown + Drift"; **cycles of concentration** is "the ratio of the concentration of dissolved solids in the blowdown water compared to the make-up water", approximately the ratio of make-up to blowdown volume; "Many systems operate at two to four cycles of concentration, while six cycles or more may be possible." **Blowdown** is draining concentrated water to stop scale; **drift** is droplets carried off as mist.

**Litres per kWh [calc].** Evaporating 1 kg of water at about 30°C takes about 2,430 kJ (latent heat) [background]. One kWh of heat is 3,600 kJ, so if all heat left by evaporation, about **1.5 litres per kWh of heat**. In practice a share leaves as sensible heat to the air, while blowdown adds water: at 4 cycles, blowdown is a third of evaporation [calc from FEMP relation, blowdown = evaporation ÷ (cycles − 1)]. Net: roughly 1.5 to 2 litres consumed per kWh of heat. Cross-checks:
- LBNL's liquid hall with a tower: median about 2.0 L per kWh of IT energy (Figure 4.4) [primary, my reading].
- Nvidia: "roughly 2.6 million gallons per megawatt per year for conventional cooling-tower-based systems" (21 Jun 2026) [primary] = about **1.1 L/kWh** at full load all year [calc: 2.6 million × 3.785 L ÷ 8,760 MWh]. Nvidia's figure is about half LBNL's median. Use either with its source; do not mix.

**Dry cooler [background, primary].** A large radiator with fans; water stays sealed and the coil can only cool it to a few degrees above the **dry-bulb** temperature, never below. LBNL (Table 4.2, printed p.41) [primary]: "When the outdoor dry bulb temperature is low, the dry coolers efficiently reject heat using ambient air alone."

**Adiabatic or hybrid [primary].** LBNL (Table 4.2, printed p.41): "spraying or circulating water through pads upstream of the heat exchanger coils enhances cooling, especially when the dry bulb temperature is high and the wet bulb temperature is low (typically in dry seasons). This system conserves water compared to evaporative cooling towers." Water is used only in hot hours.

**Chiller [background, primary datasheet].** A refrigeration machine: a compressor drives refrigerant round a loop to pump heat from the cold water to a hotter condenser, cooled by air (air-cooled chiller) or by a tower (water-cooled chiller). It can make water colder than the outside air, at the cost of compressor power. Efficiency is the **coefficient of performance (COP)**, heat moved ÷ electricity used. Vertiv Liebert AFC (EMEA datasheet rev0, March 2020) [primary via search]: EER about 4.2 to 4.6 W/W at 35°C air with 26/20°C water; "freecooling will be available up to around 32°C ambient" at that water temperature [primary marketing]. So a chiller removing 1 kW of heat uses about 0.22 to 0.24 kW at 35°C, worse as the air gets hotter [calc, background].

**Why warm coolant lets dry coolers work most hours [calc, background].** If the building water must reach 41°C (Nvidia's CDU supply, 16 Mar 2026) and a dry cooler's approach is about 5 to 8°C [background, typical; no primary found], the dry cooler alone does the job whenever outside air is below about 33 to 36°C. At 18°C chilled water (the old air-cooled hall), it could do it only below about 10 to 13°C. Each degree of coolant temperature adds hours of free cooling. Nvidia [primary]: chillers needed "outside of maybe 1% of the year ... in some climates" (21 Jun 2026); "raising chiller plant temperatures by just one degree can cut cooling energy costs by about 4%" (21 Jun 2026, citing ENERGY STAR). 1% of a year is about 88 hours [calc].

**The hottest afternoon [primary + inference].**
- Nvidia (24 Aug 2026, MaxLPS) [primary]: "Heat rejection systems are sized for worst-case scenarios, yet many sites require far less chiller compressor power under typical operating conditions, especially when dry coolers can handle a larger portion of the load." "Chillers remain important during hot conditions and for resilience, using them only when needed reduces overall cooling power and average annual power usage effectiveness (PUE)." "power budgeted for cooling during the worst hour becomes available to compute during much of the year." Its illustrative 100 MW site: "20 MW is allocated to facility overhead, 10 MW to rack losses", leaving 60 MW for AI load.
- Nvidia (25 Mar 2026) [primary]: running cooling colder means "diverting a larger share of the facility's limited grid allocation into cooling instead of compute"; "unlocks up to 30% more GPUs in the same power budget with 45°C liquid cooling" (16 Mar 2026).
- **Bounded inference [calc, label it].** Nvidia's illustrative split reserves 20 MW of 100 MW for facility overhead at peak, a design-hour ratio of 100 ÷ 80 = 1.25, against the annual 1.1 PUE it claims for Rubin. If a dry-cooled hall's worst hour needs a chiller to carry the full load at a COP near 4, cooling adds about 0.25 kW per kW of IT, taking the instantaneous ratio from about 1.1 to about 1.35. On a fixed grid connection, IT capacity scales with 1 ÷ peak PUE: 1 ÷ 1.35 against 1 ÷ 1.15 is about **15% fewer racks** from the same plug [calc]. If the chiller only trims a few degrees on part of the load, the penalty is much smaller. **No operator publishes design-day PUE for a dry-cooled liquid hall; this is the open question, and the test the live piece already proposes.**
- NREL (thermosyphon hybrid cooler at its ESIF data centre, via search summary) [press-level until opened; nrel.gov was unreachable 7 Nov 2026]: hybrid systems run "wet during peak design periods to save energy ... and dry during low design periods to save water". The trade is real and known.
- Peak water: Han, Li, Wierman and Ren, "Small Bottle, Big Pipe" (arXiv 2603.02705, v1 3 Mar 2026, v2 18 Mar 2026) [primary]: operators can be forced to "less efficient dry cooling" when water capacity is short, which can "further stress the power grid during summer peaks"; they recommend coordinated water and power planning. The 6 to 10 times peak-to-average figure the live piece cites is in UC Riverside's news release (12 Mar 2026), not the abstract; I did not reopen the release.

---

## 6. LBNL, December 2024: what it simulated and found

Shehabi et al., "2024 United States Data Center Energy Usage Report", LBNL-2001637, December 2024. PDF: escholarship.org/content/qt32d6m0d1/qt32d6m0d1.pdf (downloaded 7 Nov 2026) [primary throughout].

**Method.** "For each case, 50 simulation scenarios are developed" across 18 simulation cases; "climate data from 965 weather stations were collected" (printed pp.39 and 43; PDF 40 and 44); "over 1 million simulations". Nine cooling systems (Table 4.2, printed pp.40 to 42). Results are **annual averages**; ranges show best practice in favourable climates (low) to "poor efficiency values in hot, humid climates" (high) (printed p.44). **There is no peak-hour or design-day output.**

**Liquid assumption.** Table 4.3 (printed p.43, PDF 44): "AI (IT Liquid Cooling)" uses ASHRAE liquid class **W45**, UPS efficiency 90 to 99%. Air-cooled AI and hyperscale use A2; midsize and colo A1.

**Simulated medians, Figure 4.4 (printed p.46, PDF 47), read by me from the box plot, so approximate:**

| System | Size | PUE median | Site WUE median, L/kWh |
|---|---|---|---|
| Direct expansion | Small | about 2.05 | about 0.05 |
| Water-cooled chiller | Small | about 1.7 | about 3.2 |
| Direct expansion | Midsize | about 1.85 | about 0.05 |
| Air-cooled chiller | Midsize | about 1.83 | about 0.05 |
| Dry cooler (air-cooled chiller), air IT | Midsize | about 1.6 | about 0.05 |
| Airside economiser (air-cooled chiller) | Midsize | about 1.58 | near 0 |
| Water-cooled chiller | Midsize | about 1.52 | about 2.9 |
| Airside economiser (water-cooled chiller) | Midsize | about 1.45 | about 1.3 |
| Waterside economiser (water-cooled chiller) | Midsize | about 1.38 | about 2.5 |
| Dry cooler with adiabatic assist, air IT | Large | about 1.2 | about 0.25 |
| Airside economiser & adiabatic (air-cooled chiller) | Large | about 1.17 | about 0.02 |
| Airside economiser & adiabatic (water-cooled chiller) | Large | about 1.14 | about 0.4 |
| Waterside economiser (water-cooled chiller), air IT | Large | about 1.12 | about 2.2 |
| **IT liquid: waterside economiser with tower** | Large | **about 1.13** | **about 2.0** |
| **IT liquid: dry cooler with adiabatic assist** | Large | **about 1.10** | **about 0.13** |
| **IT liquid: dry cooler (air-cooled chiller)** | Large | **about 1.10** | **0** |

Two readings matter. (1) For liquid halls, the dry cooler's median PUE is not higher than the tower's; on my reading it is marginally lower, about 1.10 against 1.13, and its range is narrower. LBNL does not explain this in text; probable reasons are tower pump and fan energy and the supplementary chiller assumed (water-cooled for the tower case, air-cooled for the dry case) [inference]. "Barely moves" is safe; "costs a little power" is not supported by LBNL's medians. (2) An air hall going from tower to air-cooled chiller costs about 0.3 of PUE (1.52 to 1.83), but going from tower to dry cooler with an air-cooled chiller costs only about 0.1 (1.52 to 1.6), a fairer comparison the live piece does not show.

**Key text quotes.**
- "Note that simulated PUEs assume systems are commissioned and operate as designed. This is rarely the case, and generally system performance does not meet design expectations." (printed p.44, PDF 45)
- "Data centers employing water-cooled chiller systems without economizers exhibit the highest WUE" (p.44).
- "in IT liquid-cooled data centers, WUE values can be further reduced through improved heat transfer and elevated coolant/facility water temperature setpoints" (p.44).
- "The above discussion does not imply low site WUEs are necessarily good. ... While air-cooled chillers use no water, they use more energy." (printed p.45, PDF 46)
- Liquid dry cooler: "The higher operating temperature of liquid cooling systems facilitates better water and energy efficiency/performance (less chiller run hours and less adiabatic assist)." (printed pp.41 to 42)
- Liquid waterside economiser: "While highly energy-efficient, this system consumes substantial amounts of water, like all evaporative cooling systems." (printed p.42)
- "Some hyperscale facilities report WUE values for similar systems of 0.1-0.3 L/kWh, which is much higher than the values simulated here" (printed p.47, PDF 48), about the airside economiser and adiabatic system.

**Cooling mix, Figure 4.2 (printed p.39, PDF 40), my reading:** AI-specialised space in 2023 was roughly 22% liquid with waterside economiser and tower, 22% liquid dry cooler with adiabatic assist, 22% liquid dry cooler, about 15% airside economiser and adiabatic (air-cooled chiller), about 15% airside economiser and adiabatic (water-cooled chiller). So about two thirds liquid, and about two thirds of that liquid share already dry or dry-with-assist [calc from reading]. These are model allocations from Dell'Oro revenue data plus expert input, not a census (printed p.38).

**Aggregates, Figure 4.5 (printed p.47):** 2023 medians PUE / WUE: small 1.91 / 0.32; midsize and colo 1.68 / 0.67; hyperscale 1.22 / 0.32; AI specialised 1.14 / 0.61.

**National trend (printed pp.47 to 48):** average PUE "falls from 1.6 in 2014 to 1.4 in 2023" and to "between 1.15 and 1.35" by 2028. Average site WUE "stays just over 0.36 L/kWh through 2023 ... After 2023, the average WUE rises slightly, reaching between 0.45 and 0.48 L/kWh, reflecting increasing WUEs in the hyperscale and colocation data centers, along with the increased water consumption of liquid-cooled systems."

**National water (printed pp.55 to 57, PDF 56 to 58):**
- Direct (site) consumption: "In 2014, data centers consumed 21.2 billion liters"; by 2023 "the 66-billion-liter total", hyperscale and colocation 84% of it. "Hyperscale data centers in 2028 are expected to consume between 60 and 124 billion liters." Figure 5.9 totals for 2028, read from the chart: about 145 (low) to about 275 (high) billion litres [my reading].
- Indirect: "The total indirect water footprint of U.S. data centers is nearly 800 billion liters", on about 176 TWh in 2023; "national average of 4.52 L/kWh of indirect water consumption"; "the average water intensity factor for electricity use in the U.S. overall is 4.35 L/kWh". 800 ÷ 176 = 4.5 [calc check].
- Indirect counts consumption, "withdrawn water that is permanently removed from the immediate water cycle due to evaporation", including **evaporation from hydroelectric reservoirs** (printed p.56). That inflates the power-station figure relative to thermal-plant cooling alone; worth one sentence in the piece.
- Method ignores "power purchase agreements ... or on-site 'behind the meter' generation" (printed p.57).

---

## 7. PUE and WUE: definitions and boundaries

**PUE [primary + background].** LBNL (printed p.39): "Power Usage Effectiveness (PUE) is defined as the total electricity demand of the data center divided by the electricity demand of the IT equipment." Introduced by The Green Grid (2007) and standardised as ISO/IEC 30134-2 (2016) [background]. Measured over a year of energy (kWh/kWh), so it averages away the worst hour. It counts cooling, power conversion losses, lighting; it does not count IT fans as overhead (server fans sit inside "IT"), so moving from fans to pumps can make PUE look better or worse than the real change [background]. It says nothing about water.

**WUE [primary + background].** LBNL (printed p.39): "Water Usage Effectiveness is similarly defined as the total water consumption of the data center divided by the electricity demand of the IT equipment", litres per kWh. The Green Grid, WP#35, "Water Usage Effectiveness (WUE): A Green Grid Data Center Sustainability Metric", 1 Mar 2011, editor Michael Patterson [primary listing; text behind registration]: site WUE = annual site water ÷ IT energy; source WUE adds the water used to make the electricity [background on formula]. LBNL distinguishes "WUE (site)" from "WUE (source)" (printed pp.39 and 45).

**Consumed against withdrawn.** LBNL counts consumption (evaporated, gone). Microsoft's water-intensity goal is "measured as withdrawals per MW, 2022 baseline" (Microsoft, 24 Jun 2026) [primary]; AWS reports "liters of water withdrawn per kilowatt-hour of IT Load" (AWS sustainability page) [primary, per sidecar]. Not comparable to LBNL without saying so.

**Indirect water at the power station.** US average 4.35 L/kWh; data-centre-weighted 4.52 L/kWh, 2023 (LBNL, printed p.57) [primary]. A whole-water figure per kWh of IT is site WUE + PUE × 4.52 [calc method, as the live piece does].

---

## 8. Heat reuse

**Why it is hard [background].** Data centre heat is low grade: 25 to 35°C from air halls. District heating networks run at about 70 to 90°C supply in older systems, so a heat pump must lift the temperature, using electricity. Warm liquid at 45 to 55°C shrinks that lift, so each unit of heat needs less heat-pump power, and some low-temperature networks (about 50 to 60°C) could take it almost directly [background, inference]. Nobody I found has published a district heating scheme fed directly by Rubin-class return water.

**Primary examples.**
- **Meta, Odense, Denmark.** Tietgenbyen energy centre, ready late 2019; heat pumps lift server heat to 70 to 75°C; about 45 MW of heat into Fjernvarme Fyn's network; Ramboll gives about 215,000 MWh a year and over 12,000 homes; Fjernvarme Fyn said about 11,000 households in 2025; Meta's 2018 plan was 100,000 MWh and 6,900 homes (Ramboll project page; Meta 2018) [primary for Ramboll and Meta pages via search; numbers to be re-opened before use].
- **Microsoft and Fortum, Espoo and Kirkkonummi, Finland.** Announced March 2022 as the world's largest data-centre heat-recovery scheme. Fortum (May 2026) [primary, Fortum release "Fortum has started heat production at two large data centre sites in Finland", via search]: its heat plants at Kolabacken and Hepokorpi have started, for now on air-source heat pumps and electric boilers; waste heat from Microsoft's two data centres starts "in phases in 2027"; at full run about 40% of district heat for about 250,000 customers in Espoo, Kauniainen and Kirkkonummi (about 2 TWh a year of demand). Fortum's own older page still says production in the "2025-2026 heating season" [primary, undated page]. So as of 7 Nov 2026 no Microsoft heat is yet delivered, on what I found.
- **Germany, Energy Efficiency Act (EnEfG, 2023).** Per law-firm summaries [press, not the statute]: new data centres from 1 July 2026 must reach PUE 1.2 or less and an energy reuse factor of 10%, rising to 15% from 1 July 2027 and 20% from 1 July 2028; existing sites PUE 1.5 from July 2027 and 1.3 from July 2030; threshold 300 kW non-redundant connection. Verify against §§ 11 to 12 of the enacted text before use.

---

## 9. Microsoft's zero-water design

**The announcement [primary].** Steve Solomon, VP Datacenter Infrastructure Engineering, "Sustainable by design: Next-generation datacenters consume zero water for cooling", Microsoft Cloud blog, 9 Dec 2024:
- "Beginning in August 2024", all new Microsoft datacentre designs use the approach; chip-level cooling in a closed loop "filled during construction"; no evaporation. Water still used for restrooms and kitchens.
- Trade-off, verbatim: "Replacement of evaporative systems with mechanical cooling will increase our power usage effectiveness (PUE)". Chip-level cooling allows warmer temperatures and "economizing chillers" at elevated water temperatures; the result is "a nominal increase in our annual energy usage compared to our evaporative datacenter designs across the global fleet". No PUE number published.
- Saving: "more than 125 million liters of water per year per datacenter", on FY2024 average WUE of 0.30 L/kWh (39% better than 0.49 in 2021). 125 million L ÷ 0.30 L/kWh implies about 417 GWh of IT energy a year, about 48 MW average IT load per datacentre [calc].
- Pilots: Phoenix, Arizona and Mount Pleasant, Wisconsin "in 2026", coming online "late 2027".

**Fairwater, Mount Pleasant [primary].** Scott Guthrie, "Inside the world's most powerful AI datacenter", 18 Sep 2025: "Over 90% of our datacenter capacity uses this system", closed loop, "water only needed to fill up once"; "Fairwater is supported by the second largest water-cooled chiller plant on the planet"; heated water goes to outdoor fins where "172 20-foot fans chill and recirculate the water". The remaining capacity uses outdoor air and switches to water "only on the hottest days". Note: "water-cooled chiller plant" here means chillers serving a water loop, rejecting heat through fans; Microsoft's wording, ambiguous; do not write "towers" for it.

**Fleet status [primary].** Judy Priest and Steve Solomon, Microsoft blog, 24 Jun 2026: average WUE fell "from 2.3 L/kWh to 0.27 L/kWh in 2025"; "About 90% of the 2025 owned fleet uses low- to zero-water cooling"; direct air cooling with evaporative assist uses water only above 85°F (29.4°C): none year-round in parts of Northern Europe, under 5% of the time in Dublin and Amsterdam, about 10% of the year in Virginia, up to 40% in Phoenix. Water-intensity goal measured as withdrawals per MW. No PUE figures.

---

## What the live piece has wrong or out of date

1. **"Nvidia's newest rack takes it [the building's water] at up to 45 degrees" (step-three paragraph) and the diagram's "Rack loop ... up to 45°C in".** 45°C is the rack-loop (TCS) inlet. Nvidia's own design sends about **41°C** facility water to the CDU (Nvidia, 16 Mar 2026). Say: the rack takes coolant at up to 45°C; the building's water can arrive at about 41°C.
2. **"One Blackwell-generation Nvidia rack sheds about 140 kilowatts" and "about 140 kW for the GB300 NVL72".** Nvidia's own published figure is about 120 kW for GB200 NVL72 (DGX GB200 User Guide); Nvidia publishes no GB300 rack total that I found. 140 kW is Vertiv's 142 kW GB300 design envelope and the Jane Street tour. Attribute it, or use "120 to 140 kW".
3. **"Part of every server still runs on air" and "The chip sets the ceiling ... fans the rest".** True for Blackwell (Nvidia: about 20% of capacity air-cooled, 25 Mar 2026; Vertiv GB300: 85/15). Out of date for Vera Rubin: Nvidia says 100% liquid-cooled, fanless compute and switch trays (16 Mar, 25 Mar, 21 Jun 2026). Keep Blackwell's split, add that Rubin removes it; the hall still has some air load (storage, networking, CPU racks).
4. **"Heat rejection is still 'sized for worst-case scenarios' (24 August 2026)", attributed to "Nvidia's own engineers".** Verified: Nvidia Technical Blog, McKenney and Petty, 24 Aug 2026 (MaxLPS). Fine; cite the post by title in the sources line, since "Nvidia's posts of ... 24 August 2026" is vague.
5. **"Rubin ... takes coolant at up to 45°C and returns it at about 55°C (21 June 2026)".** Verified: Josh Parker, Nvidia blog, 21 Jun 2026. Keep. Note that 45°C inlet was first stated for Rubin/MGX racks on 16 Mar 2026, and the 55°C is "exits [the chip] at roughly 55", not the rack loop's measured return.
6. **"Going dry costs a liquid AI hall almost nothing in power" and "PUE stays near 1.1".** Supported, and slightly stronger than the piece says: on LBNL's Figure 4.4 medians the liquid dry cooler (about 1.10) is not worse than the liquid tower (about 1.13). But these are annual averages from typical-year weather; LBNL publishes no worst-hour figure. The piece should say "annual" every time it cites the 1.1, because its own peak-hour argument depends on the difference.
7. **The air-hall comparison (PUE 1.5 rises to 1.8).** Correct as read, but it compares a tower with an air-cooled chiller. LBNL also simulates a midsize air hall with a dry cooler (about 1.6, near-zero water). A fair line: dropping the tower costs an air hall 0.1 to 0.3 of PUE depending on what replaces it.
8. **"A cooling tower evaporates about 2 litres per kWh in a large liquid-cooled hall" (diagram).** That is LBNL's simulated median per kWh of IT energy. Nvidia's own figure (2.6 million gallons per MW per year, 21 Jun 2026) is about 1.1 L/kWh. Say "about 1 to 2 litres, depending on whose model".
9. **"W45 is the class set by ASHRAE ... for facility water up to about 45 degrees".** Correct, but incomplete: the classes run W17, W27, W32, W40, W45, W+, all with a 2°C floor, renamed in 2021; and ASHRAE's own 2021 white paper expected future, hotter chips to need colder water (W32, then W27). Nvidia going to 45°C for its hottest rack is a reversal worth a sentence.
10. **The 4.52 L/kWh power-station figure.** Correct (LBNL, printed p.57), but it includes evaporation from hydroelectric reservoirs and is a 2023 data-centre-weighted average (US overall 4.35). Add one clause.
11. **"The lab estimates American data centres consumed 66 billion litres on site in 2023".** Correct. Add the projection: about 145 to 275 billion litres by 2028 on my reading of Figure 5.9, with hyperscale alone 60 to 124 billion (LBNL text).
12. **"Microsoft ... since August 2024 all its new designs evaporate no water for cooling, at 'a nominal increase' in annual energy use".** Correct (9 Dec 2024). Add that the first sites (Phoenix, Mount Pleasant) were to pilot in 2026 and come online in late 2027, Microsoft publishes no PUE for the design, and its trade-off sentence explicitly says PUE rises. Fairwater's "second largest water-cooled chiller plant" shows chillers are central, not marginal, in its zero-water design.
13. **Evidence fold, "LBNL: liquid's warmer water means fewer chiller hours".** Supported; LBNL's words are "less chiller run hours and less adiabatic assist" (printed p.42). Quote them.
14. **Chiller "maybe 1% of the year".** Nvidia's words, said of "some climates". Fine as quoted, but the IT Brief report (24 Jun 2026) attributes the line to Ali Heydari, Nvidia's director of data centre cooling; the blog has it unattributed. Attribute to Nvidia's blog only.
15. **Sources line cites LBNL "Figures 4.2, 4.4, 4.5 and 4.7" and "Tables 4.2 and 4.3".** Fine. Page numbers in the sidecar are PDF pages; the printed page numbers are one lower. Use printed pages in the rebuild.

---

## Could not verify

- An Nvidia rack power figure for GB300 NVL72 or Vera Rubin NVL72 actual draw; the MaxLPS post's 136 kW "Vera Rubin" figure conflicts with its own caption (GB300).
- Nvidia's stated coolant inlet limit for GB200 or GB300 (press says 35°C or about 40°C; no Nvidia document found).
- ASHRAE Thermal Guidelines 5th edition air-class table (A1 to A4, H1) from ASHRAE itself; numbers above are secondary. H1 lower allowable limit conflicts (5°C or 15°C).
- A primary dry-cooler datasheet giving fan power per kW rejected and approach at 40 to 45°C ambient; the 5 to 8°C approach is typical practice, not sourced.
- Any operator's design-day (worst-hour) PUE for a dry-cooled liquid hall. This is the open question behind "the worst afternoon".
- ASHRAE 0.4% design dry-bulb temperatures for Phoenix, Dallas, Northern Virginia, Johor (needed to say how many hours exceed about 33 to 36°C).
- NREL ESIF thermosyphon figures (nrel.gov unreachable on 7 Nov 2026).
- UC Riverside's 6 to 10 times peak-day figure (in the 12 Mar 2026 news release, not in the paper's abstract; not reopened).
- Germany EnEfG figures from the enacted statute (only law-firm summaries read).
- Any Nvidia position on immersion for NVL72 racks.
- Uptime's 2025 or 2026 survey share of operators using direct liquid cooling (the 19% figure circulating is secondary and inconsistent).
- Meta Odense heat figures from Fjernvarme Fyn directly (Ramboll and press only).

## Source list (primary, opened or quoted)

- Nvidia blog, Josh Parker, "Hotter Than a Hot Tub: The 45°C Breakthrough to Cool AI's Biggest Machines", 21 Jun 2026: https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
- Nvidia Technical Blog, "NVIDIA Vera Rubin POD: Seven Chips, Five Rack-Scale Systems, One AI Supercomputer", 16 Mar 2026: https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/
- Nvidia Technical Blog, Moseley, Perez and Mahajan, "Scaling Token Factory Revenue and AI Efficiency by Maximizing Performance per Watt", 25 Mar 2026: https://developer.nvidia.com/blog/scaling-token-factory-revenue-and-ai-efficiency-by-maximizing-performance-per-watt/
- Nvidia Technical Blog, McKenney and Petty, "Maximizing AI Factory Performance per Watt with NVIDIA DSX MaxLPS", 24 Aug 2026: https://developer.nvidia.com/blog/maximizing-ai-factory-performance-per-watt-with-nvidia-dsx-maxlps/
- Nvidia blog, Marc Hamilton, "NVIDIA Blackwell Platform Boosts Water Efficiency by Over 300x", 22 Apr 2025: https://blogs.nvidia.com/blog/blackwell-platform-water-efficiency-liquid-cooling-data-centers-ai-factories/
- Nvidia DGX GB200 User Guide, hardware: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Vertiv SmartIT for NVIDIA GB300 NVL72 datasheet SL-80699: https://www.vertiv.com/4a9fd7/globalassets/shared/vertiv-smartit-for-nvidia-gb300-nvl72_datasheet_englis_sl-80699.pdf
- ASHRAE TC 9.9, "Emergence and Expansion of Liquid Cooling in Mainstream Data Centers", 2021: https://www.ashrae.org/File%20Library/Technical%20Resources/Bookstore/Emergence-and-Expansion-of-Liquid-Cooling-in-Mainstream-Data-Centers_WP.pdf
- LBNL, Shehabi et al., 2024 United States Data Center Energy Usage Report, December 2024: https://escholarship.org/uc/item/32d6m0d1
- US DOE FEMP, Best Management Practice #10, Cooling Tower Management: https://www.energy.gov/femp/best-management-practice-10-cooling-tower-management
- The Green Grid, WP#35, WUE, 1 Mar 2011: https://thegreengrid.org/en/resources/library-and-tools/238-WP
- Microsoft, Steve Solomon, 9 Dec 2024: https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/
- Microsoft, Scott Guthrie, 18 Sep 2025: https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/
- Microsoft, Priest and Solomon, 24 Jun 2026: https://blogs.microsoft.com/blog/2026/06/24/inside-microsofts-two-decade-push-to-cut-water-intensity-while-scaling-for-growth/
- Microsoft, two-phase immersion, Apr 2021: https://news.microsoft.com/innovation-stories/datacenter-liquid-cooling/
- Google Cloud blog, 30 Apr 2025: https://cloud.google.com/blog/topics/systems/enabling-1-mw-it-racks-and-liquid-cooling-at-ocp-emea-summit
- Han, Li, Wierman, Ren, "Small Bottle, Big Pipe", arXiv 2603.02705: https://arxiv.org/abs/2603.02705
- Fortum, May 2026: https://www.fortum.com/en/media/2026/05/fortum-has-started-heat-production-two-large-data-centre-sites-finland
- Ramboll, Meta Odense: https://www.ramboll.com/en-us/projects/energy/meta-surplus-heat-to-district-heating
- Vertiv Liebert AFC EMEA datasheet rev0 03.2020: https://www.vertiv.com/49dc08/globalassets/products/thermal-management/free-cooling-chillers/liebert-afc-ds-en-emea-rev0---03.2020.pdf

Press leads only: IT Brief UK, 24 Jun 2026 (Heydari quote); Upsite Technologies, 31 Jul 2024 (W-class table); TechTarget and ASHRAE Journal May 2022 (air classes); DCD 2023 (PFAS and two-phase); White & Case, Linklaters, Gleiss Lutz (EnEfG); Tom's Hardware and DCD (Kyber, Jul 2026); The Register, 3 Aug 2025 (Uptime rack density).
