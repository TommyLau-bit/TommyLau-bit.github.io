# Rack research: the physics and architecture of power from building to chip

Research slice for the rebuild of `powering-the-rack`. Compiled 7 November 2026.
Tags: **[primary]** company, standards body or regulator document read directly; **[press]** trade press or analyst, a lead only; **[calc]** my arithmetic. No share prices, valuations or views on shares.

The single most important source found is Nvidia's second white paper, *800 VDC Architecture: Industry Alignment & Execution* (Jared Huntington and Mike Tu, Nvidia, © 2026, 36 pages), linked from https://www.nvidia.com/en-us/data-center/technologies/800-vdc-architecture/ (direct PDF: https://dam-cdn.nvd.orangelogic.com/AssetLink/7rj0u54stc41tk6s57dbs2p0qdte5874.pdf). It has no printed date; it refers to "2026 GTC Taipei" (1 to 4 June 2026) in the past tense, so it dates from June 2026 or later, and it is almost certainly the "White Paper V2" the OCP blog of 11 August 2026 links to. Below it is called **WP2**. The first white paper, *800 VDC Architecture for Next-Generation AI Infrastructure* (same authors, PDF created 9 October 2025, released for the OCP Global Summit, October 2025), is **WP1**: https://dam-cdn.nvd.orangelogic.com/AssetLink/qq0vy0u48xfr0c81i2m1781pwea64n8v.pdf

The live piece has not used either white paper. WP2 changes three things in it (dates, the 54 volt limit, protection). See section 6.

---

## 1. Plain-English explainers

**Volts, amps, watts.** Voltage is the push, current (amps) is the flow of charge, power (watts) is the two multiplied. For a fixed power, double the voltage and the current halves. A megawatt is a million watts.

**Why 54 volts needs huge current at rack scale [calc].** Current = power / voltage.

| Rack power | Current at 54 V DC | Current at 800 V DC |
|---|---|---|
| 120 kW (GB200 NVL72, Nvidia's figure) | about 2,220 A | 150 A |
| 600 kW (Kyber as shown at GTC 2025) | about 11,100 A | 750 A |
| 1 MW | about 18,500 A | 1,250 A |

A household circuit carries 10 to 32 A. A 1 MW rack at 54 V would carry roughly 600 to 1,800 household circuits' worth of current down one copper bar.

**I squared R [calc].** Heat in a conductor = current² × resistance. A solid copper bar 100 mm by 10 mm (1,000 mm²) has about 17 micro-ohms of resistance per metre (copper resistivity 1.68 × 10⁻⁸ ohm-metre). At 18,500 A that bar would turn about 5.8 kW per metre into heat, like five kettles per metre, and drop 0.31 V. At 1,250 A the same bar loses about 26 W per metre. Cutting current 14.8 times cuts heat in the same bar about 219 times (14.8²). In practice designers take the gain as thinner, lighter copper rather than a cooler bar, because bars are sized to carry their current at a safe temperature. That is why Nvidia says a 1 MW rack at 54 V needs up to 200 kg of copper busbar [primary, Nvidia Technical Blog, 20 May 2025].

**The chain of boxes, top to bottom.**
- **Transformer (grid side).** Copper and steel coils that step alternating current from medium voltage (13.8 kV or 34.5 kV) down to 415 or 480 V. It works only on AC.
- **UPS.** Battery backup in the power room. Today it converts AC to DC to charge batteries and back to AC to feed the hall (double conversion).
- **Busway and power whips.** Insulated copper bars along a row, and the flexible cables ("whips") that drop from them into each rack.
- **Power shelf and PSU.** A power supply unit (PSU) is one converter module, a few kW each; a power shelf is a drawer of six of them. In GB200 NVL72 racks, eight shelves of six 5.5 kW PSUs turn AC into about 50 V DC [primary, Nvidia DGX GB200 User Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html, read 7 Nov 2026].
- **Busbar.** The thick copper spine running up the back of the rack carrying that 50 to 54 V to every tray.
- **Intermediate bus converter (IBC).** On each compute tray, steps 54 V down to 12 V (or, in 800 V designs, 800 V straight to 12 V or 6 V).
- **Voltage regulator (VRM, power stages).** Dozens of small converters millimetres from the GPU, stepping 12 V to below 1 V. At an assumed 0.8 V, a megawatt is about 1.25 million amps spread across thousands of power stages [calc].

**AC versus DC.** Alternating current reverses direction 50 or 60 times a second. That reversal is what lets a passive copper and steel transformer change its voltage, which is why grids are AC. Direct current flows one way, which is what chips use. Every data centre therefore converts AC to DC somewhere; the argument is about where. DC also needs fewer wires: 800 V DC uses three conductors (positive, return, earth) against four for three-phase AC [primary, Nvidia Technical Blog, 13 Oct 2025].

**Solid-state transformer (SST).** An electronic replacement for the transformer plus rectifier. Fast silicon carbide switches chop the incoming medium-voltage AC at thousands of times a second; at that frequency a small transformer can do the job of a large 50 or 60 Hz one; the output is rectified straight to 800 V DC. The OCP SST specification defines it as a "megawatt-scale power electronic converter" that "replaces conventional 50/60Hz line-frequency Medium Voltage transformer, rectifier units and energy storage" [primary, OCP SST Specification rev 0.3.0, effective 22 June 2026].

**Transformer rectifier unit (TRU) or medium-voltage rectifier.** The old-technology route to the same end: a conventional transformer feeding a large rectifier. Used for decades in mining, electrolysis, rail and battery storage. Nvidia calls it "a faster and proven path for quick 800 VDC deployment" than the SST [primary, WP1 p.15]. This matters for the claim, which counts a facility-level rectifier, not just an SST, as the building step.

**Sidecar / power rack.** A cabinet the size of a server rack placed beside one or two compute racks. It takes the hall's existing 415 or 480 V AC whips, converts to 800 V DC (and holds batteries), and feeds the compute rack through a DC cable. It moves the power shelves out of the compute rack so the rack can hold more GPUs. Microsoft and Meta's Mt Diablo (October 2024) is a ±400 V sidecar; Nvidia's power rack is an 800 V one.

**Row power centre (Nvidia "Option B" Power Center).** One larger end-of-row cabinet, up to about 2 MW, feeding a whole row over an overhead 800 V DC busway, still fed with AC from the existing power room.

**DC power block (Nvidia "Option C").** A containerised unit of about 4.8 MW (TRU or SST) that takes medium-voltage AC at the building edge and makes 800 V DC for a whole data hall, removing the 480 V layer.

**±400 V versus 800 V.** ±400 V is 400 V above earth on one conductor and 400 V below earth on another: 800 V between them, but no conductor more than 400 V from earth, with a midpoint. Nvidia's 800 V is single-ended ("unipolar"): 800 V between positive and return.

---

## 2. Nvidia's 800 V DC architecture: documents, dates, partners

### 2.1 Dated documents

| Date | Document | Key content | Tag |
|---|---|---|---|
| 20 May 2025 (page also shows an update "July 31") | Nvidia Technical Blog, "NVIDIA 800 VDC Architecture Will Power the Next Generation of AI Factories", https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/ | Racks "exceed 200 kilowatts, this approach begins to hit physical limits"; 1 MW racks "starting in 2027"; full-scale production "will coincide with NVIDIA Kyber rack-scale systems in 2027"; 54 V at MW scale needs "up to 64 U" of power shelves and "up to 200 kg of copper busbar", up to 200,000 kg for 1 GW; up to 5% end-to-end efficiency gain vs 54 V; 85% more power through the same conductor and 45% less copper vs 415 VAC; maintenance cost down up to 70%; TCO down up to 30%; 13.8 kV AC to 800 V DC at the perimeter by industrial rectifiers; SST "being studied"; GTC 2025 showed an 800 V sidecar powering 576 Rubin Ultra GPUs in one Kyber rack | primary |
| 13 Oct 2025 | Nvidia Technical Blog, "Building the 800 VDC Ecosystem for Efficient, Scalable AI Factories", https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/ | Transition "will occur in phases" (no dates); Kyber's 64:1 LLC converter 800 V to 12 V, 26% less area; 800 V DC carries 157% more power than 415 VAC at same gauge; AC end-to-end efficiency "can be less than 90%"; capacitors near racks, BESS at the utility connection; rack swings 30% to 100% in milliseconds; 35 kV to 415 V example | primary |
| Oct 2025 (PDF 9 Oct 2025) | WP1, OCP Global Summit 2025 | See 2.2 | primary |
| 13 Oct 2025 | Nvidia blog, "NVIDIA, Partners Drive Next-Gen Efficient Gigawatt AI Factories in Buildup for Vera Rubin", https://blogs.nvidia.com/blog/gigawatt-ai-factories-ocp-vera-rubin/ | Kyber "will house 576 NVIDIA Rubin Ultra GPUs by 2027" (as cited in the live piece; not re-read) | primary (via piece) |
| 16 Mar 2026 | Nvidia Technical Blog, "NVIDIA Vera Rubin POD", https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/ | Vera Rubin NVL72 "on track to ship in the second half of 2026"; Kyber "will first be introduced with Vera Rubin Ultra as a standalone NVL144 system"; NVL576 = eight racks of 72; Intelligent Power Smoothing with 6x rack-level energy storage (400 J per GPU), peak current down up to 25%; no Kyber date, no rack kW | primary |
| 30 Mar 2026 | OCP, *Data Center Facility: Low Voltage Direct Current Power Distribution* white paper v1.0, https://www.opencompute.org/documents/dcf-power-distribution-lvdc-white-paper-version-1-0-final-pdf-1 | 155 pages; sub-project leads from Eaton and ABB; workstream leads ABB, Siemens, Google, Eaton, UL Solutions, Schneider; contributors include Nvidia, Microsoft, AWS, Vertiv. Broad industry framework, not an Nvidia document. Codes and breaker standards (section 5) | primary |
| 1 to 4 Jun 2026 | Nvidia blog, GTC Taipei at Computex, https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/ | Vera Rubin "ramping into full production"; 800 V power racks "a bridge for existing AC-based facilities toward hybrid AC and 800 VDC" | primary |
| 22 Jun 2026 (history 20 May 2026; PDF 2 Jul 2026) | OCP SST Specification rev 0.3.0, authors Google, Microsoft, Nvidia, https://www.opencompute.org/documents/ocp-sst-design-specification-v0-3-final-pdf/ | SKU A 13.8 kV in, 5 MW; SKU B 34.5 kV in, 5 or 10 MW; output 800 V DC unipolar; ≥98% efficiency at 50 to 100% load (power train only); floating or high-resistance earth; 10 to 20 ft container; "first draft" | primary |
| Jun 2026 or later | WP2 | See 2.3. The key document | primary |
| 11 Aug 2026 | Nvidia blog, "Why Scaling AI Compute Performance Requires a New Power Architecture" (Harry Petty), https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/ | Joint white paper March 2026; LVDC SST spec v0.3 July 2026; more than 80 makers; power rack "second half of 2026", needs no change to the building; row power center up to 2 MW, "expected in 2027"; DC power block for new facilities, no date | primary |
| 11 Aug 2026 | OCP news, "Powering the Next Era of AI: How Google, Microsoft and Nvidia Are Standardizing...", Jason Adrian and Mike Tu (Nvidia), http://www.opencompute.org/news/powering-the-next-era-of-ai-how-google-microsoft-and-nvidia-are-standardizing-and-accelerating-the-industry-transition-to-lvdc/ | Mt Diablo ±400 V sidecar "supports current solutions"; side power rack can make ±400 V or 0 to 800 V; Mt Diablo 2.0 to support native 800 V, "coming later"; MVAC to 800 VDC workstream started by the three; 80+ partners; work with UL Solutions, NFPA, IEEE, IEC | primary |

### 2.2 WP1 (October 2025): what it says

- **Why:** GPU power rises about 20% a generation, but larger NVLink domains make rack power rise "2x, 4x or 8x"; Hopper to GB300: GPU TDP +75%, performance 50x, rack density 3.4x. A secondary goal is to push power parts out of the NVLink radius, "the highest value real estate in the rack".
- **Conductor table (48 A wire):** 415 VAC 0.6 kW/mm², 480 VAC +16%, 800 VDC +157%, 1,500 VDC +382%.
- **Voltage options under evaluation:** 800 V (Nvidia MGX); 750 V (ODCA, VDE-SPEC 90037, Europe); ±400 V (OCP), described as introducing "complexity in grounding, phase balancing, and fault detection"; 1,500 V a "potential long-term target" held back by UL/NEC rules for indoor IT and arc-flash in confined racks.
- **Why single-ended 800 V, not ±400 V:** bipolar needs "specialized three-pole breakers and protection devices that are not widely available"; single-ended 800 V "aligns with existing two-pole breaker designs". The IT rack is built to accept ±400 V sources too, with fuses on both inputs.
- **Transition vs end state:** the side power rack is "transitional", for white-space retrofit, and "not the optimal solution end-to-end due to the extra stages of conversion". Facility rectifiers from LV AC: about 1.5 MVA strings, about 99% efficient, mature. MV rectifiers and SSTs: 35 kV AC to 800 V DC, up to 7.5 MVA a unit, 98.5% or better.
- **Reference block:** 17.5 MW, five 3.5 MW MV rectifiers (5-to-make-4), 5,000 A DC board, 1,500 A busducts each with load-break contactor, solid-state circuit breaker and blocking diode, four 1.1 MW racks.
- **Safety:** touch-safe connectors with mechanical interlocks borrowed from EV chargers; codes "must" be updated.
- **Energy storage:** capacitors under 100 ms; batteries beyond 10 s; swings as fast as 400 µs; a 50% duty square wave 50% over average raises RMS losses 25%.

### 2.3 WP2 (mid-2026): what changed

- **Coexistence, not replacement.** "800 VDC is not intended to replace existing 415/480 VAC systems, but rather to complement and coexist alongside them." The three options are "not sequential requirements, but flexible deployment options". The AC option remains "the default and broadly adopted solution" in Nvidia's DSX reference design (480 VAC, 100 A whips, 4-to-make-3).
- **Rack power roadmap (Nvidia, its Figure 3):** Gen 1 up to 145 kW (60 A whips, 8-to-make-6); Gen 2, "newly released" with Vera Rubin NVL72, 330 kW per rack with AC or DC input; Gen 3 100% liquid-cooled power shelves, up to 570 kW in one rack position, **still on the 54 V plane**; Gen 4 the planned native 800 V in-rack distribution. "Near-term generations will continue leveraging the proven 54 VDC distribution plane." Current and near-term systems take 800 V input through 800 V to 54 V power shelves.
- **Option A, Power Rack:** about 660 kW per power rack; 12 x 100 A AC whips at 415 to 480 VAC (IEC 60309); AC to 800 V shelves of 6 x 18.3 kW PSUs, 1,200 J storage each; optional BBUs 4 x 20 kW (80 kW for 60 s); 125 A 800 V cables with interlock and short pin; 1:1 or 2:1 compute to power rack; compute rack holds an 800 V to 54 V shelf of 6 x 15 kW. **"The Power Rack is entering production in Q3 2026."** Certified under UL 62368-1 (IT equipment) "while limiting data hall-level 800 VDC exposure"; "can be certified now for both UL and IEC region deployments". Next gen: liquid-cooled, 55 kW per RU.
- **Option B, Power Center:** end-of-row rectification, adjustable to 2 MW (about 1.6 MW units in 4-to-make-3 giving a 4.8 MW cluster); SiC modular shelves or IGBT rectifiers derived from UPS; 1,250 A feeder, overhead busway, 125 A tap cans with MCCB or SSCB; "retrofit deployment without modification to upstream AC electrical rooms". **"The expected Option B deployment will be as soon as Q3 2027."**
- **Option C, DC Power Block:** about 4.8 MW blocks, TRU or SST, outdoor containerised; 6,000 A DC switchboard, 1,250 A busway; 20 MW deployment unit of four scalable units; supports racks "approaching 1 MW". TRU "remain highly practical for approximately 5 MW-class"; options include UPS-derived IGBT converters, aggregated rack power shelves, and the "Panama" phase-shifting-transformer architecture. **No date for the TRU version.** SST: "most commercially available SST platforms today remain focused on approximately 15kV-class input"; 34.5 kV needs more development; **"The next generation SST is expected to be launched toward 2029"**, with blocks scaling toward 10 MW.
- **Next 12 months:** "accelerating equipment development, validating system-level performance, conducting pilot deployments, and advancing standards".

Press reading of the same roadmap: StorageReview (15 Aug 2026) lists Option A Q3 2026, Option B Q3 2027, Option C 2029; https://www.storagereview.com/news/nvidia-moves-800-vdc-power-architecture-from-concept-to-production-just-dont-turn-off-ac-power-yet [press]. My reading of WP2 is narrower: 2029 attaches to the next-generation SST, not to every power block.

### 2.4 Partner lists [primary]

- **20 May 2025:** silicon (10): Analog Devices, Infineon, Innoscience, MPS, Navitas, onsemi, Renesas, ROHM, STMicroelectronics, Texas Instruments. Power system components (5): Delta, Flex Power, Lead Wealth, LiteOn, Megmeet. Data centre power systems (3): Eaton, Schneider Electric, Vertiv.
- **13 Oct 2025:** silicon (14): AOS, Analog Devices, Efficient Power Conversion, Infineon, Innoscience, MPS, Navitas, onsemi, Power Integrations, Renesas, Richtek, ROHM, STMicroelectronics, Texas Instruments. Components (6): Bizlink, Delta, Flex, Lead Wealth, LITEON, Megmeet. Data centre power systems (9): ABB, Eaton, GE Vernova, Heron Power, Hitachi Energy, Mitsubishi Electric, Schneider Electric, Siemens, Vertiv.
- **11 Aug 2026:** "more than 80" makers and infrastructure firms (unnamed).

### 2.5 2026 status: who has shown or shipped what

| Item | Status | Source | Tag |
|---|---|---|---|
| Nvidia power rack | "entering production in Q3 2026"; "second half of 2026" | WP2; Nvidia blog 11 Aug 2026 | primary |
| Optional, not standard, on Vera Rubin | Ready for customer shipments 3Q26 as "an optional configuration"; adoption rises after Rubin Ultra 2H27; widespread 2028 | TrendForce, 25 Jun 2026, https://www.trendforce.com/presscenter/news/20260625-13121.html | press |
| Flex 800 VDC power rack | Launched 16 Mar 2026 for Vera Rubin; "from approximately 125 kW to up to 880 kW" per rack; BBU and capacitor backup options; no ship date | Flex release, https://investors.flex.com/news/news-details/2026/Flex-Launches-800-VDC-Power-Rack-for-Next-Generation-NVIDIA-AI-Infrastructure/default.aspx | primary |
| Delta 660 kW in-row power rack | Six 110 kW shelves, 80 kW BBU each (480 kW); shown GTC Mar 2026 and OCP Oct 2026; ship date in a secondary summary only (Q3 2026) | Dell'Oro, 19 Oct 2026; datacenter.news | press |
| APC (Schneider) 800 V sidecar | Shown at GTC 2026 | Glenn Lockwood blog, 23 Mar 2026 | press |
| OCP Global Summit, 12 to 15 Oct 2026 | Sidecars from Delta, Lite-On, xFusion (300 kW to 1.2 MW prototype), Rittal (2 MW demonstrator with Bosch EV power electronics); 800 V protection hardware from ABB, Schneider, Siemens, Eaton; SSTs from DG Matrix (Interport 360 Flex, up to 34.5 kV in, 800 V out), Heron Power, SolarEdge (cell under validation), Sungrow, Delta; "volumes remain modest, field reliability is unproven" | Dell'Oro, 19 Oct 2026, https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/ | press |
| Vertiv | Q1 2026 call: portfolio launch 2H26, shipping 2027 (press summary); Q3 2026 call: 2027 validation, deployment 2028 (in live piece) | transcripts | press |
| Envision Ulanqab | 10 kV to 800 V on SSTs, "now powering live computing workloads", no size (2 Nov 2026) | in live piece | primary (via piece) |

No named first deployment of an Nvidia-spec 800 V power rack in a customer hall was found as of 7 November 2026.

### 2.6 Has the timetable moved?

- **Power gear:** no slip found. H2 2026 / Q3 2026 for the power rack is consistent across Nvidia's blog and WP2.
- **Row unit:** "2027" (blog) is "as soon as Q3 2027" (WP2): late 2027 at the earliest.
- **Building:** was "not dated"; WP2 now says next-generation SST "toward 2029". TRU-based power blocks are described as practical but not dated.
- **Kyber:** May 2025 tied 800 V full-scale production to Kyber in 2027. GTC 2026 re-introduced Kyber as a standalone NVL144 system (Nvidia, 16 Mar 2026), with no date or kW in that post. SemiAnalysis reported in early July 2026 that Kyber slipped to 2028 on midplane manufacturability; Nvidia told Tom's Hardware "Our roadmap is intact" [press: https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028 ; https://www.datacenterdynamics.com/en/news/nvidia-pushes-kyber-release-to-2028-following-manufacturing-concerns-report/]. TrendForce (Jun 2026) still had Rubin Ultra in 2H27.
- **54 V ceiling moved:** May 2025 said 54 V hits physical limits above 200 kW. WP2 now plans 54 V in-rack to 570 kW (Gen 3, liquid-cooled shelves), with native 800 V in-rack only at Gen 4. 800 V reaches the rack's input first; the rack's internal 54 V busbar survives longer than the piece implies.

---

## 3. The rival path: ±400 V (Mt Diablo)

- **Origin:** Microsoft Azure Infrastructure Blog, "Mt Diablo: Disaggregated Power Fueling the Next Wave of AI Platforms", 15 Oct 2024 (OCP Global Summit 2024), with Meta; power conversion moves into a separate rack. https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/mt-diablo-disaggregated-power-fueling-the-next-wave-of-ai/ba-p/4268799 [primary, read via search snippet only]. Press: 400 V DC, "hundreds of kW up to 1MW", 15 to 35% more accelerators per rack (Neowin) [press].
- **Google joins:** Google Cloud blog, 30 April 2025, Madhusudan Iyengar and Amber Huffman, https://cloud.google.com/blog/topics/systems/enabling-1-mw-it-racks-and-liquid-cooling-at-ocp-emea-summit [primary]. Verbatim: move "from 48 volts direct current (VDC) to the new +/-400 VDC, which will enable IT racks to scale from 100 kilowatts up to 1 megawatt"; 48 V scaled "from 10 kilowatts to 100 kilowatts IT racks"; "ML will require more than 500 kW per IT rack before 2030"; 400 V chosen to "leverage the supply chain established by electric vehicles"; first embodiment an "AC-to-DC sidecar power rack" improving end-to-end efficiency "by ~ 3%"; Mt Diablo 0.5 draft "in May"; "Longer term, we are exploring directly distributing higher-voltage DC power within the data center". Google said nothing on SSTs.
- **Deschutes is cooling, not power.** Project Deschutes is Google's coolant distribution unit (fifth generation to be contributed to OCP); ~99.999% fleet CDU availability since 2020 [primary, same blog]. Do not cite it as a power architecture.
- **Meta:** OCP LVDC white paper: Mt Diablo lets the ORv3 HPR IT rack move from AC-fed 33 kW (HPR v1) or 72 kW (HPR v2) shelves to DC-fed HPR v4 100 kW shelves in the same 1 OU, a 39% gain in power per shelf [primary, OCP 30 Mar 2026].
- **Convergence:** Nvidia's IT rack accepts ±400 V sources (WP1). Nvidia, Google and Microsoft now co-author the OCP SST spec, which specifies **800 V unipolar** output (22 Jun 2026). The OCP blog (11 Aug 2026) says the ±400 V Mt Diablo spec "supports current solutions" and Mt Diablo 2.0 will support native 800 V. In effect the hyperscaler path is converging on Nvidia's single-ended 800 V for the building, while ±400 V sidecars serve today. Microsoft contributed new Mt Diablo versions at OCP October 2026 [press, Dell'Oro].
- **Europe:** ODCA and Current/OS use 700 V and 350 V nominal (ODCA moved from 650 V); VDE-SPEC 90037 750 V [primary, OCP LVDC paper; WP1].

---

## 4. Rack power over time (dated, sourced)

| Rack | Power | Source | Tag |
|---|---|---|---|
| Typical enterprise and colo rack, 2024 | below 8 kW average | Uptime Global Data Center Survey 2024 | press (Uptime summary) |
| Typical rack, 2025 | average 7.5 kW excluding outliers (6.8 kW in 2024); one fifth of operators deploy 30 kW or more at their densest | Uptime 2025 survey via The Register, 3 Aug 2025 | press |
| Typical rack, 2026 | "Average modal rack densities continue their slow upward trajectory"; growing number with peak 30 kW+; no figure in release | Uptime 16th survey, Business Wire, 28 Jul 2026 | primary (release) |
| Google 48 V racks | 10 kW to 100 kW | Google, 30 Apr 2025 | primary |
| GB200 NVL72 | "approximately 120kW" (8 shelves x 6 x 5.5 kW PSUs, 33 kW per shelf, 50 to 51 V busbar) | Nvidia DGX GB200 User Guide | primary |
| GB200 NVL72 reference design | up to 132 kW per rack | Vertiv, 15 Oct 2024 (in piece) | primary |
| Nvidia Gen 1 rack power | up to 145 kW | WP2 | primary |
| GB300 NVL72 | 132 kW nominal, about 155 kW peak (HPE); 135 kW (Lenovo); 132 kW (Supermicro); about 150 kW (TrendForce). Nvidia publishes no GB300 rack figure that I found | OEM datasheets via search; TrendForce 25 Jun 2026 | press |
| Vera Rubin NVL72 | Nvidia: Gen 2 power architecture "330 kW per rack" capability (a ceiling, not a draw); TrendForce: about 225 kW | WP2; TrendForce | primary / press |
| Gen 3 (liquid-cooled 54 V shelves) | up to 570 kW | WP2 | primary |
| Kyber / Rubin Ultra NVL576 (as shown) | about 600 kW, 2H 2027 (Huang, GTC keynote, 18 Mar 2025) | DCD, Tom's Hardware, Mar 2025 | press (keynote quote) |
| Rubin Ultra rack | about 660 kW | TrendForce, 25 Jun 2026 | press |
| Nvidia power rack (Option A) | about 660 kW | WP2 | primary |
| Kyber re-introduced NVL144 | no kW stated by Nvidia | Nvidia, 16 Mar 2026 | primary |
| 800 V target | 1 MW racks "starting in 2027" (May 2025); native 800 V racks "approaching 1 MW" (WP2, undated) | Nvidia | primary |
| Google | more than 500 kW per rack before 2030 | Google, 30 Apr 2025 | primary |

Note on naming: Nvidia called Vera Rubin's 72-package rack "NVL144" at GTC 2025 and reverted to "NVL72" at GTC 2026 (Lockwood, press; Nvidia's 2026 posts use NVL72). Whether Kyber NVL144 counts 144 packages (576 dies, as before) or is half the GTC 2025 density is not settled in what I could read.

---

## 5. Safety and building rules for DC at 800 V

### 5.1 The physics of the off switch
- AC passes through zero 100 or 120 times a second; mechanical breakers use that moment to quench the arc. DC never does, so an arc "can sustain without zero-crossings; harder to extinguish" [primary, WP2 Table 1].
- But DC faults in converter-fed systems often carry *less* energy: "Often lower in converter-limited systems" vs AC's "higher fault contribution from utility and rotating machines" [primary, WP2]. Arc-flash energy depends on fault current (I) and clearing time (t), so Nvidia's plan attacks both: current-limited sources (rectifiers, DC/DC stages, SSTs, batteries with current limiting) and fast clearing (SSCBs) [primary, WP2].
- Series arcs (loose connections) do not draw enough current to trip a breaker and need dedicated arc-fault detection (signature analysis, connector temperature) [primary, WP2].
- Shock: DC "often causes a single muscle contraction"; AC can cause "muscle lock-on" [primary, WP2].

### 5.2 Protection hardware, Nvidia's plan
- **Day 1 is mechanical:** "MCCBs are expected to serve as the primary branch protection device for initial production systems"; clearing "up to approximately 20 ms", so feeds need redundancy or hold-up time [primary, WP2].
- **SSCBs later:** "expected to become the preferred long-term protection solution"; Nvidia's two target ratings: 125 A air-cooled for in-rack 800 V to 54 V shelves, and 1,250 A (likely liquid-cooled) for future native 800 V rack interfaces; broader use "dependent on supply chain readiness, regulatory certification, product availability, and cost" [primary, WP2]. SSCBs clear in sub-millisecond times vs several ms for fuses and mechanical breakers (WP2 Figure 15, sourced to Siemens).
- **Grounding:** four schemes under evaluation (high-resistance midpoint, high-resistance return, floating, solid); "preferred grounding approach will ultimately be determined through system-level studies" [primary, WP2]. The SST spec says floating or high-resistance earth, "detailed design TBD" [primary, OCP SST rev 0.3.0].
- **Connectors:** interlocked whips: connector locks, then upstream contactor closes; release opens contactor first [primary, WP2]. StorageReview reports the spec mandates high-resistance grounding, insulation monitoring, arc-fault detection and connector interlocks [press].

### 5.3 SSCB makers [mixed]
- Infineon with SolarEdge, SiC, few-microsecond trip, between SST and rack (9 Sep 2026, in live piece) [primary via piece]; "getting closer to market" at OCP Oct 2026 [press, Dell'Oro].
- ABB SACE Infinitus: claims world's first fully IEC 60947-2 certified SSCB, up to 2,500 A and 1,250 V DC (ABB product page) [primary, ABB's own claim]; ABB's 800 V data-centre items are the Infinitus SST and Tmax XT DC moulded-case breakers [press summary of ABB pages].
- Atom Power: says its Gen 1 Atom Switch was the first listed to UL 489I (2019) [primary claim, via search snippet].
- Siemens, Eaton, Schneider, ABB showed 800 V protection on Nvidia's MGX wall, OCP Oct 2026 [press]. Vertiv working on standardising how SSCBs report faults [press].

### 5.4 Standards and dates
| Standard | Status | Source | Tag |
|---|---|---|---|
| NFPA 70 (NEC) 2026 | Current edition. Covers AC and DC premises wiring, "not voltage or system limited"; "data center specific infrastructure requirements do not currently exist" | OCP LVDC white paper, 30 Mar 2026, p.145 | primary |
| NFPA 70 (NEC) 2029 | "next revision will be completed in the third quarter of 2028", task groups on DC systems and data centres; "Until formal installation codes like the 2029 NEC are finalized, organizations must lean on interim guidance" (Outlines of Investigation, risk assessment, hardware-in-the-loop) | same | primary |
| NFPA 70E | Workplace electrical safety; applies to AC and DC over 50 V (arc flash, shock) | same | primary |
| NFPA 855 (2026), NFPA 75 (next 2028) | Energy storage; IT equipment fire protection | same | primary |
| UL 489I | Solid-state and hybrid circuit breakers up to 1,000 VAC and 1,500 VDC; first edition 22 Oct 2025 (earlier existed as an Outline of Investigation) | ANSI webstore listing via search; Schneider blog 11 Sep 2026 | press (listing not opened) |
| IEC 60947-10:2026 | Semiconductor circuit-breakers, up to 1,000 V AC / 1,500 V DC; edition 1.0 published May 2026 (11 or 12 May); EN adoption Aug 2026. OCP in March 2026 said "to be published soon" | SCC, IEC preview, OCP LVDC paper | primary (catalogue entries) |
| UL 2367 | Solid-state overcurrent protectors on boards, limited to 5 A and 250 VA, does not address above 60 V; supplementary only | OCP LVDC white paper | primary |
| UL 248 | Branch fuses limited to 600 V | OCP LVDC white paper | primary |
| UL 62368-1 / IEC 62368-1 | IT equipment; Nvidia's power rack certified under it, which is why it can ship now | WP2 | primary |
| NEC Article 690 / IEC 62477-1 | Set 1,500 V DC as low-voltage limit in PV and industrial converters | WP1 | primary |

Also: Nvidia, CSPs, OEMs and **UL Solutions** are working on a narrowed certification scope; "Authority Having Jurisdiction (AHJ) engagement has become an important enabler", with inspection guidelines and training for inspectors in development [primary, WP2]. This is primary support for the piece's "new rules for inspectors", which now cites only a sponsored trade article.

### 5.5 What has to change in the building, and when [mixed; inference labelled]
- **Now (rack level):** nothing upstream. Power rack takes existing AC whips, certified as IT equipment, 800 V confined to the cable between two racks [primary, WP2].
- **Row level (as soon as Q3 2027):** 800 V busway and tap cans in the white space, DC breakers (MCCB day 1), interlocked whips, RCM/IMD; AC room unchanged [primary, WP2].
- **Hall level (TRU undated; next-gen SST toward 2029):** new MV switchgear feeding containerised power blocks; 6,000 A DC boards; grounding scheme chosen; arc-flash methods for DC accepted by regulators; DC UPS and BESS integration [primary, WP2].
- **Codes:** the first NEC edition with data-centre DC work in it is 2029, finalised Q3 2028 [primary]. US states adopt NEC editions with a lag, often one to three years [my general knowledge, not verified for this note]. So a code-backed 800 V building in the US is plausibly a 2029 to 2031 event, absent local variances [inference].

---

## 6. What the live piece has wrong or out of date

1. **"The building step described but not dated" / "Nvidia giving its DC power block a date before 2028" as a watch item.** WP2 (Nvidia, mid-2026) says the next-generation SST "is expected to be launched toward 2029". The DC power block in its TRU form is described as practical at 5 MW class but not dated. Update: Nvidia's own dates are now Q3 2026 (rack), as soon as Q3 2027 (row), toward 2029 (next-gen SST). The falsifier still stands; one "move me" trigger is half met.
2. **"Row power centre in 2027."** Nvidia's white paper says "as soon as Q3 2027". Tighten.
3. **"Above 200 kW racks hit physical limits", "a megawatt at 54 volts leaves no choice, so the rack moves now".** Nvidia's own 2026 roadmap keeps the 54 V in-rack plane to 570 kW (Gen 3, liquid-cooled shelves) and moves in-rack distribution to 800 V only at Gen 4. What moves now is the rack's *input*: 800 V arrives at an 800 V to 54 V shelf. The piece should say 800 V reaches the rack's door first and its spine later; the 200 kW line is Nvidia's 2025 statement, superseded in practice.
4. **Chart "Nvidia Kyber, from 2027, 1 MW" and "Kyber is to house 576 Rubin Ultra GPUs by 2027, at around a megawatt".** Kyber as shown at GTC 2025 was about 600 kW, not 1 MW (1 MW was the 800 V target "starting in 2027"). Nvidia re-introduced Kyber in March 2026 as a standalone NVL144 with no kW and no date in that post; SemiAnalysis reported a slip to 2028 (Nvidia: "roadmap intact"). Do not put Kyber at 1 MW in 2027 without qualification.
5. **"Vertiv, ... GB200 NVL72 ... up to 132 kW".** Fine as Vertiv's design figure, but Nvidia's own number is about 120 kW (DGX GB200 User Guide). Use Nvidia's for the chart; Vertiv's as the design envelope.
6. **"85% more power through the same conductor ... cuts copper by 45%" (May 2025).** Nvidia's later figure is 157% more power per conductor area (Oct 2025 blog and WP1, 48 A wire basis). The two are on different bases; if one is used, say which and when, or use both.
7. **"Nvidia, Google and Microsoft publish a joint 800 VDC white paper through OCP in March 2026".** The 30 March 2026 OCP LVDC white paper is a broad industry paper (sub-project leads at Eaton and ABB; contributors include Google, Microsoft, Nvidia, AWS, Vertiv, UL). Nvidia's blog frames it as joint; better: "an OCP white paper the three helped write". The three-company document is the SST specification.
8. **"Solid-state transformer specification ... version 0.3 by July 2026".** More precisely: revision 0.3.0, effective 22 June 2026, "first draft", authored by Google, Microsoft and Nvidia; published on OCP in early July. It specifies 13.8 kV (5 MW) and 34.5 kV (5 or 10 MW) units with 800 V unipolar output at ≥98%.
9. **"An 800 volt building needs new protection, much of it solid-state."** Nvidia's plan is mechanical MCCBs on day 1 (up to about 20 ms clearing), SSCBs as the long-term preference. And DC faults from converter-fed sources can carry less energy than AC faults. Refine the "off switch" section: the new protection is grounding, insulation monitoring, interlocks and current-limited sources first, SSCBs later. Rack-first is also certification-first: the power rack ships under UL 62368-1 because 800 V stays inside the rack pair (WP2).
10. **"Local code officials ... a sponsored trade article of 26 October 2026".** Replace with WP2's primary statement on AHJ engagement, and the OCP paper's NEC timetable (2029 edition, finalised Q3 2028).
11. **"The move 'will occur in phases'".** Still Nvidia's October 2025 phrase, but WP2 now says the options are "not sequential requirements" and that 800 V will "coexist" with AC "for the foreseeable future". The piece's ordered-phase story is Nvidia's 2025 framing; its 2026 framing is a menu with AC as default. Strengthens the claim's "AC room stays", weakens "phases in order".
12. **Falsifier risk the piece underplays: the TRU.** The claim breaks on a 10 MW hall fed by "a facility-level rectifier or solid-state transformer". Nvidia's own papers call MV rectifiers and TRUs mature and "a faster and proven path"; WP1's reference design was a 17.5 MW MV-rectifier block. The building step need not wait for SSTs. The piece's SiC-SST framing of the building step should mention TRUs.
13. **Envision "10 kV straight to an 800 volt bus".** Note: WP2 says most commercial SSTs are 15 kV class; a 10 kV SST is consistent with that, while 34.5 kV US-style feeds need more development. Supports the piece's point that China's greenfield path differs.
14. **"Google, which ... scaled its 48 volt architecture".** Fine. But "AC, DC and ±400 volts" para: add that Nvidia picked single-ended 800 V because ±400 V needs three-pole breakers not widely available (WP1), and that the hyperscaler SST spec itself specifies 800 V unipolar, so the camps are converging.
15. **Figure "Tray steps to 12 V, GaN in new 800 V designs".** Nvidia's Kyber converter is a 64:1 LLC with matrix transformer, 800 V to 12 V, +1% efficiency, 26% less area (WP1, Oct 2025 blog). Current Vera Rubin power racks still deliver 54 V in-rack, so the 800-to-12 step is Gen 4, not 2026.
16. **Rack power chart lacks the typical rack.** Uptime: about 7.5 kW average (2025). A GB200 rack is about 16 typical racks; a 600 kW rack about 80 [calc].

## 7. Could not verify

- The exact publication date of WP2 (undated; internal evidence June 2026 or later; OCP blog of 11 Aug 2026 links a "White Paper V2").
- Any Nvidia primary figure for GB300 NVL72 or Vera Rubin NVL72 actual rack draw (only Nvidia's 330 kW Gen 2 capability, and OEM and TrendForce figures).
- Kyber NVL144's power and whether it is half the GTC 2025 density; Kyber's current date (2027 vs SemiAnalysis's 2028). Nvidia's only on-record line is "Our roadmap is intact" (to Tom's Hardware, July 2026).
- Any customer hall where an Nvidia-spec 800 V power rack is in service; Delta, LiteOn ship dates (secondary only).
- UL 489I first-edition date (ANSI listing seen only via search snippet); Atom Power's UL 489I claim.
- Microsoft's Mt Diablo blog text (search snippet only) and the Meta co-announcement date.
- Whether Mt Diablo 2.0 has been published (OCP blog of Aug 2026 says "coming later"; one press item claims a final spec effective 8 Oct 2026).
- State adoption lag for NEC 2029 (general knowledge, not checked).
- The "July 31" update on Nvidia's 20 May 2025 blog: what changed.
- Nvidia's 13 Oct 2025 "576 Rubin Ultra GPUs by 2027" sentence was not re-read this session (cited from the live piece).

## Source list
- Nvidia Technical Blog, 20 May 2025: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
- Nvidia Technical Blog, 13 Oct 2025: https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/
- WP1 (Oct 2025): https://dam-cdn.nvd.orangelogic.com/AssetLink/qq0vy0u48xfr0c81i2m1781pwea64n8v.pdf
- WP2 (2026): https://dam-cdn.nvd.orangelogic.com/AssetLink/7rj0u54stc41tk6s57dbs2p0qdte5874.pdf (linked from https://www.nvidia.com/en-us/data-center/technologies/800-vdc-architecture/)
- Nvidia Technical Blog, 16 Mar 2026: https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/
- Nvidia blog, GTC Taipei, June 2026: https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/
- Nvidia blog, 11 Aug 2026: https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/
- Nvidia DGX GB200 User Guide: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- OCP LVDC white paper v1.0, 30 Mar 2026: https://www.opencompute.org/documents/dcf-power-distribution-lvdc-white-paper-version-1-0-final-pdf-1
- OCP SST Specification rev 0.3.0, 22 Jun 2026: https://www.opencompute.org/documents/ocp-sst-design-specification-v0-3-final-pdf/
- OCP news, 11 Aug 2026: http://www.opencompute.org/news/powering-the-next-era-of-ai-how-google-microsoft-and-nvidia-are-standardizing-and-accelerating-the-industry-transition-to-lvdc/
- Google Cloud blog, 30 Apr 2025: https://cloud.google.com/blog/topics/systems/enabling-1-mw-it-racks-and-liquid-cooling-at-ocp-emea-summit
- Microsoft Azure Infrastructure Blog, 15 Oct 2024: https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/mt-diablo-disaggregated-power-fueling-the-next-wave-of-ai/ba-p/4268799
- Flex release, 16 Mar 2026: https://investors.flex.com/news/news-details/2026/Flex-Launches-800-VDC-Power-Rack-for-Next-Generation-NVIDIA-AI-Infrastructure/default.aspx
- Uptime 16th survey release, 28 Jul 2026 (Business Wire, via 01net.it): https://www.01net.it/uptime-institute-16th-annual-2026-global-data-center-survey-deployment-of-high-density-racks-rising-fast-operators-face-continued-recruiting-and-retention-pressures/
- IEC 60947-10:2026 (SCC catalogue): https://scc-ccn.ca/standardsdb/standards/2058651
- ABB SACE Infinitus: https://www.abb.com/global/en/areas/electrification/low-voltage/circuit-breakers/solid-state-circuit-breakers/sace-infinitus
- Press leads: TrendForce 25 Jun 2026 https://www.trendforce.com/presscenter/news/20260625-13121.html ; StorageReview 15 Aug 2026 (link above); Dell'Oro 19 Oct 2026 (link above); Glenn Lockwood 23 Mar 2026 https://blog.glennklockwood.com/2026/03/gtc-2026-recap.html ; Tom's Hardware and DCD on Kyber slip, July 2026 (links above); The Register on Uptime 2025, 3 Aug 2025 https://www.theregister.com/2025/08/03/capacity_planning_concern_datacenter_ops/ ; Schneider blog on IEC 60947-10, 11 Sep 2026 https://blog.se.com/energy-management-energy-efficiency/2026/09/11/1-new-iec-standard-for-semiconductor-circuit-breakers/
