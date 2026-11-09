# Data centres in orbit: the physics and engineering, chip to deep space

Research slice for the depth rebuild of `src/content/journal/data-centres-in-space.md`. Compiled 7 November 2026. Research only; no site file edited.

Tags: **[primary]** read at the source named; **[press]** lead only, not for use as fact without a primary; **[calc]** my arithmetic, method shown (scripts in the session scratchpad, reproducible from the formulas here); **[background]** textbook physics or general engineering knowledge, no single source needed. Every date is the date of the document or, for web pages, the date I read it (7 Nov 2026).

Constants used in every [calc]: Stefan-Boltzmann constant σ = 5.670 × 10⁻⁸ W/m²K⁴; solar constant 1,361 W/m² (Starcloud uses 1,366); Earth radius 6,371 km; Earth's mean outgoing infrared about 239 W/m² [background, CERES-class global mean]; deep space sink about 3 K, negligible.

---

## Headline findings (for the rebuild)

1. **The array, not only the radiator, is the mass problem.** At SpaceX's own figures (250 W/m² array, 1,400 W/m² radiator), a 120 kW satellite needs about 480 m² of array against about 86 m² of radiator, 5.6 times the area [calc]. Heritage flexible arrays deliver 71 to 124 W/kg (Redwire ROSA product table) [primary], so the array alone weighs 8 to 14 kg per kW of electricity, already at or over SpaceX's 10 kg per kW whole-satellite budget [calc]. "The plug is free" is true of the fuel, not of the mass.
2. **"Ten kilograms per kilowatt for the radiator" holds only at ISS density.** The 14 kg/m² figure is right for the ISS radiator unit as flown (1,122.64 kg over 79.2 m², 14.2 kg/m²) [primary, calc]. But NASA Glenn lists the ISS radiator at "~9 kg/m2" (Jan 2025), pumped-loop radiators generally at "6 to 10 kg/m2" (2008), and a heat-pipe radiator at "3 kg/m2 double sided", tested at TRL 5 in 2011 [primary]. At SpaceX's 1,400 W/m² those give 6.4, 4.3 to 7.1, and 2.1 kg per kW [calc]. The radiator uses between a fifth and all of the budget depending on which heritage you pick.
3. **Starcloud's Earth load is understated about fourfold.** Its white paper multiplies the Earth's infrared by the coating's solar absorptivity (0.09). In the infrared a surface absorbs at its emissivity (0.92) [background]. Corrected, its own case gives about 63 W/m² from the Earth, not 14.46, and a net of about 585 W/m², not 633 [calc]. The live piece repeats the 14.
4. **1,400 W/m² sits above where AI chip coolant runs.** A two-sided panel at emissivity 0.92 needs about 67°C to shed 1,400 W/m² in shade with no Earth load, about 73°C with the Earth's infrared on a panel edge-on to the Earth at 650 km [calc]. Nvidia's newest racks take coolant at up to 45°C and it leaves the chip at about 55°C (Nvidia, 16 Mar and 21 Jun 2026, via the site's heat research) [primary, not re-opened]. A radiator cannot run hotter than the loop feeding it, so 1,400 W/m² implies a hotter loop than ground practice, a heat pump, or a figure counted per face. The transcript does not say which.
5. **The heat-pump verdict in the live piece is right for light radiators and wrong for heavy ones.** On mass, with an ISS-density radiator (14.2 kg/m²) a half-Carnot heat pump lifting a 45°C loop saves about 9% of the radiator-plus-array mass with 100 W/kg arrays, and about 28% with 250 W/kg arrays (lift capped at 120°C, pump hardware ignored) [calc]. With 3 to 6 kg/m² radiators and arrays at 250 W/kg or below it saves nothing to 10% [calc]. So "cannot buy back the radiator" holds only if radiators are light, which is the opposite of the heritage case the rest of the piece leans on.
6. **The Suncatcher paper was revised on 17 June 2026 (arXiv v2) and the live piece quotes v2 numbers under the v1 date.** v2 "Re-ran radiation test with improved methods": the silent-error rate changed from HBM errors at "one event/50 rad" and "1 per 10 million inferences" (v1, 22 Nov 2025) to logic and SRAM silent data corruption at "approximately one event/17 rad" and "1 per 3 million inferences" (v2) [primary].
7. **The dawn-dusk orbit is not eclipse-free at 650 km.** About 87 days a year with an eclipse each orbit, up to about 20 minutes of a 98-minute orbit [calc]. A 120 kW satellite riding through 20 minutes needs about 40 kWh of storage, 150 to 270 kg of cells at today's specific energy, or it throttles [calc]. Google's blog says the orbit "reduces the need for heavy onboard batteries", not removes it [primary].
8. **What binds first is mass across every subsystem at once, not radiation or latency.** A ground GB200 NVL72 rack is about 1.36 t for about 120 kW, 11 kg per kW [press]; heritage arrays are 8 to 14 kg per kW; heritage radiators 2 to 10; Google's dose estimate assumes 10 mm aluminium-equivalent shielding, 27 kg per m² of enclosure [calc]. Each alone is near the 10 kg per kW budget. Radiation is manageable for inference; ground bandwidth binds training, not inference.

---

## 1. Why heat leaves only by radiation, and what a radiator sheds

### 1.1 The mechanism

- In vacuum there is no fluid to carry heat away from the satellite, so convection is impossible; conduction can move heat within the craft but not off it. The only exit is thermal radiation [background]. SpaceX's prospectus: "thermal control must be accomplished through radiation rather than convection and conduction" (424B4, 12 Jun 2026, as quoted in the live piece and sidecar) [primary, read by the earlier drafter; EDGAR blocked my direct download today].
- Stefan-Boltzmann law: power radiated per unit area = ε σ T⁴, with T the surface temperature in kelvin and ε the emissivity (0 to 1) [background]. Stefan published the empirical law in 1879 and Boltzmann derived it in 1884 [background].
- Net heat rejected = emitted minus absorbed. Absorbed loads in LEO: direct sunlight (solar absorptivity α × 1,361 W/m² on any face the sun sees), Earth's infrared (ε × view factor × about 239 W/m²), and albedo (α × view factor × albedo × sunlight on the lit Earth below) [background].
- **Key subtlety (Kirchhoff's law):** a surface absorbs at a given wavelength exactly as well as it emits there. White paints and optical solar reflectors are chosen to have low solar absorptivity (sunlight is visible and near-infrared) and high infrared emissivity. The Earth's glow is infrared, so the radiator absorbs it at roughly its emissivity, about 0.9, not at its solar absorptivity [background]. This is the error in Starcloud's sum (section 1.4).
- Coatings: the ISS radiator panels carry a white "(Z-93) coating which provides optimum thermo-optical properties to maximize heat rejection" (NASA ISS ATCS overview, undated, p. 15) [primary]. Typical white paints have ε about 0.9 and α about 0.15 to 0.2 at beginning of life, rising with ultraviolet darkening; optical solar reflectors reach α about 0.07 to 0.1 [background]. Starcloud assumes ε 0.92 and α 0.09 [primary].

### 1.2 Gross flux from a two-sided panel in shade, no Earth load

Formula: q = 2 × ε × σ × T⁴ (both faces radiate) [calc].

| Panel temperature | ε = 0.92 | ε = 0.85 |
|---|---|---|
| 280 K (7°C) | 641 W/m² | 593 W/m² |
| 300 K (27°C) | 845 W/m² | 781 W/m² |
| 318 K (45°C, the W45 loop) | 1,069 W/m² | 988 W/m² |
| 330 K (57°C) | 1,237 W/m² | 1,143 W/m² |
| 340.4 K (67.2°C) | 1,400 W/m² | 1,293 W/m² |
| 350 K (77°C) | 1,566 W/m² | 1,447 W/m² |
| 373 K (100°C) | 2,023 W/m² | 1,869 W/m² |
| 400 K (127°C) | 2,671 W/m² | 2,468 W/m² |

[calc] These match the live piece's curve (581 at 0°C, 771 at 20°C, 1,069 at 45°C, 1,400 at 67.2°C, 2,023 at 100°C). Each 1% rise in kelvin gives about 4% more heat [calc].

### 1.3 Earth view factor and the Earth's infrared load

View factor from a flat face to the Earth, 650 km altitude [calc, analytic formula checked by numerical integration]:
- Face looking straight down (nadir): F = (R/(R+h))² = **0.823**.
- Face whose plane contains the nadir direction (a "vertical" panel, edge-on to the Earth): F = (1/π)[arctan(1/X) − X/H²], H = (R+h)/R, X = √(H² − 1), giving **0.241** per face.
- Face looking straight up (zenith): 0.

Earth infrared absorbed, ε 0.92, OLR 239 W/m² [calc]:
- Vertical two-sided panel: 2 × 0.92 × 0.241 × 239 = **106 W/m²** of panel.
- Horizontal panel (one face down, one up): 0.92 × 0.823 × 239 = **181 W/m²**.

So the best orientation is vertical and edge-on to both the sun and the Earth. In a dawn-dusk orbit the sun sits close to the orbit normal, so a panel lying in the plane of the orbit normal and the nadir is edge-on to both [background]. This is what Musk describes: radiators "oriented knife edge to the sun" (interview transcript, FWP filed 9 Jun 2026) [primary].

Albedo: below a dawn-dusk satellite the ground is at the day-night line, so reflected sunlight is small; with α 0.09 it adds only a few W/m² to a vertical panel [calc, rough; I did not integrate albedo over the terminator geometry].

### 1.4 Net flux and radiator mass per kW at 300, 330 and 350 K

Net = gross minus 106 W/m² Earth infrared (vertical panel, edge-on to the sun). The last column adds sunlight on one face at α 0.09 (123 W/m²), Starcloud's configuration [calc].

| T | Gross | Net, edge-on | Net, sun on one face | m² per kW (edge-on) |
|---|---|---|---|---|
| 300 K (27°C) | 845 | 739 | 617 | 1.35 |
| 330 K (57°C) | 1,237 | 1,132 | 1,009 | 0.88 |
| 340.4 K (67°C) | 1,400 | 1,294 | 1,172 | 0.77 |
| 350 K (77°C) | 1,566 | 1,460 | 1,337 | 0.68 |

Radiator mass per kW of heat rejected (edge-on net flux) at different areal densities [calc]:

| T | 3 kg/m² (heat pipe, TRL 5) | 6 kg/m² | 9 kg/m² (NASA GRC's ISS figure) | 14.2 kg/m² (ISS unit as flown) |
|---|---|---|---|---|
| 300 K | 4.1 | 8.1 | 12.2 | 19.2 |
| 330 K | 2.7 | 5.3 | 8.0 | 12.5 |
| 340 K | 2.3 | 4.6 | 7.0 | 11.0 |
| 350 K | 2.1 | 4.1 | 6.2 | 9.7 |

- Temperature for **1,400 W/m² net** with the vertical panel's Earth load: about **346.6 K, 73.5°C**, not 67°C [calc]. The live piece's "68°C allowing for the Earth's glow" uses Starcloud's understated Earth term.
- Caveats [background]: (a) the panel's average surface runs below the coolant because of fin efficiency (typically 70 to 90%), so the coolant must be warmer still; (b) heat to reject exceeds compute power by power-conversion and pump losses (a few to 10%); (c) these are beginning-of-life optical properties.

### 1.5 Starcloud's worked case, checked

Starcloud (then Lumen Orbit), "Why we should train AI in space", v1.03, September 2024, pp. 8 to 10 [primary]:
- "A 1m x 1m black plate kept at 20°C will radiate about 838 watts to deep space (radiating from both sides)" (p. 3). Check: 2 × σ × 293.15⁴ = 837.5 W with ε = 1 [calc]. Correct as a black body.
- "an average radiator temperature of around 20°C for an inlet temperature of 35°C and outlet temperature of 5°C" (p. 9).
- Emitted 770.48 W/m² both faces at ε 0.92 [primary]; check 2 × 0.92 × σ × 293.15⁴ = 770.5 [calc].
- Earth: "α * F * (Al * S + σ * Tearth⁴) = 0.09 * 0.25 * (0.3 * 1366 + 5.67 * 10⁻⁸ * (273.15 − 20)⁴) = 14.46 W/m2" (p. 9) [primary].
- Sun: "0.09 * 1366 = 122.94 W/m2" (p. 9); net "633.08 W/m2 when held at 20°C" (p. 9) [primary].
- **The error [calc]:** the infrared part uses α = 0.09. Split: albedo 0.09 × 0.25 × 0.3 × 1,366 = 9.22 W/m² (correct to use α here); Earth infrared 0.09 × 0.25 × 232.9 = 5.24 W/m² (should use ε 0.92: 53.6 W/m²). Corrected Earth load 62.8 W/m², net 770.48 − 122.94 − 62.8 = **about 585 W/m²**, 8% below Starcloud's 633. If both faces see the Earth (a vertical panel), the infrared load roughly doubles again.
- Heat pumps: "if heat pumps are used to increase the radiator temperature then this power output per square meter can be dramatically increased due to the T4 term in the Stefan-Boltzmann law, albeit at an added energy cost to run the heat pumps" (pp. 9 to 10) [primary].
- Arrays: thin silicon cells "<25 μm thickness and achieve power densities >1000 W/kg" (p. 7) [primary, cell-level claim, not an array].

### 1.6 Worked numbers for a SpaceX-style 120 kW satellite [calc]

- Radiator at 1,400 W/m² (Musk): 120 / 1.4 = **86 m²**; at Starcloud's corrected 585: 205 m².
- Array at 250 W/m² (Musk, electrical output): 120 / 0.25 = **480 m²**; add 10% for conversion and bus: about 530 m².
- 250 W/m² is 18.4% of 1,361 W/m², consistent with silicon cells after packing and temperature losses [calc]. Google uses 22% cells, 90% packing: 270 W/m² [primary, Suncatcher].
- Area ratio array to radiator: **5.6**.

---

## 2. Heritage radiator mass per kW, and where "10 kg per kW" comes from

### 2.1 ISS External Active Thermal Control System (EATCS)

NASA/Boeing, "Active Thermal Control System (ATCS) Overview", hosted at nasa.gov (undated; uploaded 2021) [primary]:
- "The EATCS is designed to provide 35 kW of heat rejection per loop for a total capability of 70 kW" (p. 5).
- Two rotating wings of three radiator ORUs; "Each Radiator ORU measures 76.4 feet (23.3 meters) by 11.2 feet (3.4 meters) and weighs 2,475 pounds (1,122.64 kilograms)" (p. 14). Eight panels per ORU, deployed on orbit.
- "Ammonia supply temperature is currently set at 37 °F (2.8 °C)" (p. 6); "a temperature goal of minus 40 °F at the radiator outlet" (p. 16; the source prints the minus sign as a dash).
- Each panel has 22 Inconel flow tubes in two independent flow paths, flex hoses between panels, white Z-93 coating (p. 15).
- Thermal Radiator Rotary Joint: "weighs 927 pounds (420.5 kilograms)" (p. 17); rotates ±105° under software limit.
- Photovoltaic Radiator: "can reject up to 14 kW of heat into deep space"; "weighs 1,633 pounds (740.7 kilograms)"; deployed 3.12 m by 13.6 m (p. 3).

Derived [calc]:
- Six ORUs: 6,736 kg for 70 kW = **96 kg per kW**; planform 475 m²; **147 W/m²**; **14.2 kg/m²**.
- Adding the two rotary joints (one per wing): 7,577 kg, **108 kg per kW**. Beam, valves and pumps excluded.
- Photovoltaic Radiator: 53 kg per kW, 330 W/m², 17.5 kg/m².
- Why so low a flux: the loop runs cold (supply 3°C, outlet minus 40°C) to cool a crewed cabin, the wings see sunlight and Earth at their design worst case, and 70 kW is a design capability, not a measured flux [background]. So ISS is a ceiling for heritage mass, not a design point for a 60°C compute loop.

### 2.2 Other NASA figures on areal density

- NASA, Schunk, Babiak and others, "Thermal Control System Architecture and Technology Challenges for a Lunar Surface Habitat", IEEE Aerospace 2022 (NTRS 20210026557): radiators "based on an areal density of the ISS Heat Rejection System thermal radiators (14 kg/m2)" [primary, read by the earlier scout; not re-opened today].
- NASA Glenn, Sanzi and Thaikattil, "Heat Pipe/Thermal Technologies at GRC", NESC webinar, 23 Jan 2025, p. 6 [primary]: ISS radiators "Pumped ammonia fluid with aluminum face-sheets", "Designed to operate <10 °C", "Area Density ~9 kg/m2", TRL 9. Heat-pipe radiators "Can be designed to operate from 125-300 C", "Lightweight design: areal density ~3 kg/m2", TRL 5.
  - **Discrepancy to resolve in the piece:** 9 kg/m² (Glenn 2025) versus 14 kg/m² (lunar habitat paper 2022) versus 14.2 (ORU mass over planform, my arithmetic). Most likely 9 is the panel and 14 the whole deployable unit with mechanisms; neither source says. Use a range, 9 to 14 kg/m².
- Same webinar, p. 8: Fission Surface Power full-scale Radiator Demonstration Unit (NETS 2011): "2.5 M x 3M panel", "Dissipated 6KWth", "Operated at 400 K", "Areal density of 3 kg/m2 double sided", TRL 5 [primary]. Derived: 800 W per m² of planform, 3.75 kg per kW at 400 K in test [calc].
- Juhasz, "High Conductivity Carbon-Carbon Heat Pipes for Light Weight Space Power System Radiators", NASA/TM-2008-215420, October 2008 [primary]:
  - "a radiator whose specific mass is less than one fourth that of a pumped loop design (<1.6 kg/m2 compared to 6 to 10 kg/m2) based on near term technology" (p. 6 of PDF).
  - The tested carbon-carbon heat pipe: "Its specific mass of 2.1 kg/m2 for two-sided heat rejection is a reduction of more than threefold over the specific mass of first-generation space station radiators" (PDF p. 12).
  - "approximately one fourth of the values commonly found in current space radiators, averaging 6 to 10 kg/m2" and "approaching 1.0 kg/m2, if survivability to launch vibrations can be demonstrated" (PDF p. 14).
  - Note these are high-temperature space-power radiators (hundreds of kelvin), where flux per m² is far higher; the kg/m² carries over, the W/m² does not.
- NASA has sought radiators at "500 to 600 K" approaching "2 to 3 kg m-2" (Glenn-hosted paper, per search summary) [press, lead only].
- Schriener and El-Genk, Nuclear Technology: cesium-titanium heat pipe panel with graphite fins at 2.98 kg/m², about 56 kWth at 600 K [press, lead only; journal not opened].

### 2.3 Pumped loops versus heat pipes [background unless tagged]

- **Pumped single-phase loop** (ISS ammonia): one fluid circuit through all panels; carries large loads over long distances and through rotary joints; a single puncture can drain a loop, so ISS uses two independent paths per panel and isolation valves (RBVMs) [primary for the ISS design, ATCS overview pp. 15 to 16]. Heavier: Glenn and Juhasz put pumped-loop radiators at 6 to 10 kg/m² [primary].
- **Heat pipes**: sealed tubes with a wick, passive, no pump; each pipe is independent, so a micrometeoroid hit loses one pipe, not the loop. Juhasz: "heat pipe radiators provide significantly higher survivability to micrometeoroid damage, owing to the parallel redundancy of heat pipes" [primary]. Limits: wick capillary limits on length and heat flux, and freezing or start-up at low temperature. Google's Suncatcher design names "a thermal system of heat pipes and radiators" (section 1.2) and prefers passive transport "to maximize reliability" (section 3) [primary].
- **Loop heat pipes and two-phase pumped loops** sit between the two; common on communications satellites for deployable radiators [background].
- **Deployable radiators**: needed because 86 m² does not fit in a fairing; the hinge or flexible line is the thermal choke point [press lead: search summary of small-satellite literature]. ISS ORUs are deployed by a mechanism and can be retracted (ATCS overview, p. 14) [primary].
- Starcloud-2: CEO claims the "largest commercial deployable radiator" and about "10 times lower mass per watt" than the ISS radiator [press, lead only; no figure on Starcloud's site, read 7 Nov 2026]. If true against 96 kg per kW, that is about 10 kg per kW of heat [calc], still the whole SpaceX budget.

### 2.4 The "10 kg per kW" in the live piece: where it comes from and whether it holds

Two different 10s:
1. **The whole-satellite budget.** SpaceX: "over 100 kilowatts of compute power per metric ton" (424B4, 12 Jun 2026; roadshow slide "100KW Compute power per metric ton", FWP 4 Jun 2026) [primary, per sidecar]. Inverse: 1,000 kg / 100 kW = 10 kg per kW [calc]. Holds as arithmetic. Note it is per kW of *compute* power, so array, bus losses, radiator, structure, shielding, batteries and chips all sit inside it.
2. **The radiator alone at ISS density.** 14 kg/m² ÷ 1.4 kW/m² = 10.0 kg per kW [calc]. Holds only if (a) 14 kg/m² is the right density, (b) 1,400 W/m² is a net figure, and (c) heat equals compute power. On (a): Glenn's 9 kg/m² gives 6.4 kg/kW; heat-pipe 3 kg/m² gives 2.1 kg/kW; Juhasz's tested 2.1 kg/m² gives 1.5 kg/kW. On (b): with the Earth load the panel must run about 6°C hotter for the same net. On (c): adding 10% losses raises each figure 10%.

**Verdict:** the arithmetic is right; the inference "radiators as heavy as the station's would use that whole budget alone" is true but is a statement about 1990s crewed-station heritage. Modern heritage (pumped loops 6 to 10 kg/m²) gives 4 to 7 kg per kW; demonstrated heat-pipe panels give about 2. The radiator is a large part of the budget, not necessarily all of it.

---

## 3. Solar power in orbit

### 3.1 Irradiance and the ground comparison

- Above the atmosphere: about 1,361 W/m² [background; Google uses "1.361kW/m2", Suncatcher section 4.4, PDF p. 12, primary].
- Continuous sunlight at 1,361 against a good ground site's yearly average of 4.5 to 5.5 kWh/m²/day (190 to 230 W/m² averaged) is 6 to 7 times the energy per m² [calc]. Google blog (4 Nov 2025, Travis Beals): "In the right orbit, a solar panel can be up to 8 times more productive than on earth" [primary]. SpaceX CFO Bret Johnsen: "roughly five times, if not more, energy per cell than they get terrestrially" (transcript FWP, 9 Jun 2026) [primary].

### 3.2 Dawn-dusk sun-synchronous orbit and eclipse

- Sun-synchronous: the Earth's equatorial bulge (J2) turns the orbital plane once a year, so the plane keeps the same angle to the sun; dawn-dusk means the plane rides the day-night line [background]. Google: "dawn-dusk, sun-synchronous low-Earth orbit (LEO) to enable near-continuous power generation" (section 1.2) [primary]. Starcloud's FCC narrative: 600 to 850 km "with a nominal 06:00 crossing time" (4 Feb 2026) [primary, per scout].
- **Eclipse season [calc]**, cylindrical Earth shadow, mean sun, 18:00 ascending node, no atmosphere:

| Altitude | SSO inclination | Period | Days a year with eclipse | Longest eclipse per orbit |
|---|---|---|---|---|
| 550 km | 97.6° | 95.6 min | about 97 | about 22 min |
| 650 km | 98.0° | 97.7 min | about 87 | about 20 min |
| 800 km | 98.6° | 100.9 min | about 73 | about 17 min |
| 1,000 km | 99.5° | 105.1 min | about 55 | about 13 min |
| 1,400 km | 101.4° | 113.8 min | none | none |

  Method: β = arcsin(orbit normal · sun vector); eclipse when |β| < arcsin(R/(R+h)); eclipse fraction = (1/180°) arccos(√(h² + 2Rh) / ((R+h) cos β)). The season falls around one solstice (which one depends on the 06:00 or 18:00 choice) [calc].
- Johnsen's "the sun is on those cells 24 hours a day" (9 Jun 2026) [primary] overstates it for any orbit below about 1,400 km [calc].
- Google's prototype is not in this orbit: NPR's correction (2 Oct 2026) says the prototype "is in a standard orbit and uses batteries"; the earlier version had wrongly said sun-synchronous without batteries [press, NPR via KUOW syndication].

### 3.3 Array specific power, state of the art

- NASA Small Spacecraft Technology State of the Art, Power chapter (page dated 7 May 2026) [primary]: "Space missions using solar arrays, regardless of spacecraft mass, are strongly clustered around ~30 W/kg"; deployable products in its table run from about 30 to 100 W/kg, with ROSA and fold-out arrays at 100 W/kg or above; triple-junction cells "nominal efficiency of 30% and a high of 34%"; silicon "around 20%".
- Redwire ROSA product page (read 7 Nov 2026) [primary], beginning-of-life power and mass by configuration: Diamond 3.3 kW, 36 kg; Opal 5.3 kW, 42.7 kg; Sapphire 12.9 kW, 160 kg; Tanzanite 17.6 kW, 180 kg; SunStone 28 kW, 331 kg; Phenacite 37 kW, 521 kg. Derived **71 to 124 W/kg**, 81 to 98 W/kg for the large wings [calc]. A search summary attributes a "100 to 120 W/kg" marketing figure to Redwire [press].
- iROSA on the ISS: "Each wing provides an additional 20+ kW of power over 10 years" (Redwire page) [primary].
- **Mass per kW of electricity [calc]:** 71 W/kg = 14.1 kg/kW; 85 = 11.8; 100 = 10.0; 124 = 8.1. For 120 kW plus 10% losses: 1.1 to 1.9 t of array. **At heritage specific power the array alone is SpaceX's whole budget.**
- Starlink arrays: not disclosed. Google's whole-satellite estimate for Starlink V2 mini, 575 kg and about 28 kW, is 49 W/kg for the whole craft (Suncatcher Table 1) [primary estimate, calc]. SpaceX says AI satellites will use "solar technology that we already are going to use on the V3 Starlink vehicle" (Ian Dahl, 9 Jun 2026) [primary] and need "approximately five times the solar array output compared to V3 satellite designs" (424B4, per sidecar) [primary].
- Gaalema, Indyk and Staley (arXiv 2604.07760, 9 Apr 2026, not peer reviewed): conventional implementations "less than 100" W/kg; integrated design "about 500 W/kg" [primary preprint, per scout].
- To fit 10 kg per kW with room for chips and radiator, the array must reach roughly 250 to 500 W/kg (2 to 4 kg per kW) [calc]. No flown array at scale has published that.

### 3.4 Degradation

- NASA SOA lists degradation causes ("radiation exposure, coverglass or adhesive darkening, surface contamination") but no rate [primary]. Typical design allowances are a few tenths of a percent to a couple of percent a year depending on cell, cover glass and orbit; thin uncovered silicon degrades faster [background; no primary found today]. Starcloud claims thin cells "anneal (heal) radiation damage at moderate temperatures" (white paper p. 8) [primary, company claim]. See "Could not verify".

### 3.5 Batteries

- NASA SOA: "Current commercial Li-ion energy cells typically provide 150-270 Wh/kg" [primary].
- 120 kW through a 20-minute eclipse: 40 kWh; 148 to 267 kg of cells before packaging, depth-of-discharge margin and thermal control (perhaps double that as a pack) [calc]. That is 1.2 to 2.2 kg per kW, or more, for the eclipse season alone; the alternative is to cut compute during eclipse, losing about 87 days × up to 20% of each orbit [calc].

---

## 4. Google's Suncatcher paper: what it assumes

"Towards a future space-based, highly scalable AI infrastructure system design", Agüera y Arcas, Beals, Biggs, Bloom, Fischbacher, Gromov, Köster, Pravahan, Manyika (Google). arXiv 2511.19468. **v1 22 Nov 2025; v2 17 Jun 2026** ("v2: Cleaned up references. Improved rough estimates. Fixed typos." and "Re-ran radiation test with improved methods", arXiv abstract page) [primary]. All quotes below are from v2 unless marked; section numbers are the paper's; page is the PDF page.

- **Orbit** (1.2, p. 2): "We envision launching the satellites into dawn-dusk, sun-synchronous low-Earth orbit (LEO) to enable near-continuous power generation with lower latency and launch costs than higher orbits."
- **Cluster** (2.2, p. 3): "an illustrative, planar 81-satellite constellation", "mean cluster altitude of 650 km", "Cluster radius is R=1km, with distance between next-nearest-neighbor satellites oscillating between (approximately) 100 and 200 m".
- **Formation flying** (2.2, p. 5): J2 drift reduced to "<3 m/s/year per km of maximal distance from reference orbit"; "formation flight should be feasible with only modest delta-v requirements beyond what would be needed for precise station-keeping of a single satellite". It also flags occlusion: designs must "pay attention to occlusion of outgoing 'rejected heat' IR radiation between satellites" (p. 5). [Thermal implication, calc/background: satellites 100 to 200 m apart in a plane can see each other's radiators, raising each one's sink temperature.]
- **Radiators and thermal** (1.2, p. 2): "Cooling would be achieved through a thermal system of heat pipes and radiators while operating at nominal temperatures." (3, p. 7): "Effective thermal management is a critical optimization challenge for power-dense TPUs operating in a vacuum. Advanced thermal interface materials and heat transport mechanisms, preferably passive to maximize reliability, are essential to efficiently move large heat loads from the chips to dedicated radiator surfaces." **No radiator area, mass, temperature or flux appears anywhere in v1 or v2** [primary, full-text search of both].
- **Mass philosophy** (1.2, p. 2): "We aim to be as mass-efficient as possible, maximizing compute per kilogram to minimize launch costs". (3, p. 7): "the floor on fuel price means that there will always be an incentive to minimize mass"; future designs "an integrated compute, radiator, and power design".
- **Optical links** (2.1, pp. 2 to 3): required "aggregate bandwidth per link, on the order of 10Tbps"; commercial optical ISLs offer "1 to 100 Gbps" (my rendering of the source's range); received power needed "on the order of hundreds of microwatts, compared to the ∼1 µW levels typical for traditional long-range ISLs"; bench demo "800Gbps unidirectional (1.6Tbps bidirectional)".
- **Ground link** (3, p. 7): "the current leader, NASA's TeraByte Infrared Delivery (TBIRD) mission, demonstrating 200Gbps ground-LEO communications in 2023". For a pilot, "radio suffices" (1.2).
- **Radiation** (2.3, pp. 5 to 6): v6e Trillium tested with a "67MeV proton beam"; orbit dose "∼150 rad(Si)/year" with "significant shielding (e.g. 10 mm Al equivalent)"; five-year requirement "∼750 rad(Si)"; HBM "irregularities after a cumulative dose of 2 krad(Si), which is almost 3× our minimum requirement"; "No hard failures were attributable to TID up to this level" (15 krad(Si)).
  - **v2:** "Core logic and on-chip SRAM were the most SEE-sensitive components, primarily manifesting as Silent Data Corruption (SDC)"; "approximately one event/17 rad ... on the order of 1 per 3 million inferences, assuming 1 inference per second"; host "one such event per 450 rad(Si) for CPU and 400 rad(Si) for RAM" (p. 6). Methods: SDC "between 14.4 rad and 20 rad per event depending on the specific workload"; HBM uncorrectable ECC "approximately 44rad per event (averaged over 203 events)"; system crashes "once per 5krad" (4.3, p. 10).
  - **v1 (22 Nov 2025) said instead:** HBM "was also the most SEE-sensitive component, primarily manifesting as uncorrectable ECC errors"; "approximately one event/50 rad ... on the order of 1 per 10 million inferences"; core logic and SRAM "more robust ... approximately 150rad per event" [primary, v1 PDF p. 6 and 10]. **v2 makes silent errors about three times more frequent than v1 and moves them from memory (detected) to logic (silent).**
  - Training: "the impact of SEEs on training jobs, and the efficacy of system-level mitigations, requires further study" (both versions).
- **Launch price threshold** (2.4, p. 6): "$200/kg is often cited, by SpaceX and others, as a threshold beyond which launch could cease to be the limiting cost factor for ambitious programmes". Abstract: "launch to low-Earth orbit (LEO) may reach ≲$200/kg by the mid-2030s". Learning rate "∼20%"; "If the learning rate is sustained, which would require ∼180 Starship launches/year, launch prices could fall to <$200/kg by ∼2035" (my comma for the source's dashes). Needs "∼370,000t additional cumulative mass, equivalent to ∼1800 Starship launches (assuming 200t capacity" (4.4, p. 11). "If, instead, 104,000t are launched (a 72% decrease from the above target), prices could be ∼$300/kg by the mid-2030s" (p. 12).
  - v1 also derived $200/kg from "$500/kg to Geostationary Transfer Orbit (GTO) as a viability threshold" for space solar power, via Falcon Heavy's GTO-to-LEO ratio of about 40%; **v2 removed that derivation** [primary, v1 p. 6].
- **Starship cost** (2.4, pp. 6 to 7): "launch costs to LEO may drop to ≲ $60/kg (10× component reuse)"; "≲ $15/kg" at 100× reuse; "launch price to customers would drop to <$250/kg" at 10× reuse and up to 75% margin. Methods: "∼$460/kg (no reuse)"; fuel floor "∼$8/kg" (4.4, p. 11).
- **Current price** (4.4, p. 12): "we use current launch price $3,600/kg, based on Falcon 9 (reusable configuration), since that is used for the Starlink constellation".
- **Starlink proxy** (4.4, p. 12): V2 mini "575kg (optimized design)"; "solar panel area ∼105m2"; "22% solar panel efficiency, 1.361kW/m2 solar insolation and 90% packing" give "∼28kW/satellite"; five-year life; "$14,700/kW/y (current prices), falling to $810/kW/y". Ground: power at $0.06 to $0.25 per kWh and PUE of about 1.09 to 1.4 give $570 to $3,000 per kW per year (paraphrased to avoid the source's range dashes).
- **Repair** (3, p. 7): "The simplest solution is redundant provisioning."
- Google blog, 4 Nov 2025 (Beals) [primary]: orbit "reduces the need for heavy onboard batteries"; "two prototype satellites by early 2027" with Planet.

---

## 5. Radiation, latency and bandwidth: what binds first

### 5.1 Radiation [primary from Suncatcher unless tagged]

- Total dose is not the gate for a five-year life at 10 mm Al equivalent: 2 krad(Si) onset versus 750 rad(Si) needed.
- **Shielding is mass [calc]:** 10 mm of aluminium is 2.7 g/cm², **27 kg per m²** of enclosure. A compute box of 4 m² surface would carry about 110 kg; Starcloud assumes "1kg of shielding per kW of compute" (white paper Table 1) [primary]. Google's 150 rad(Si)/year rests on that shielding.
- **Silent errors per chip, not per inference [calc]:** 150 rad/yr ÷ 17 rad/event = about 9 silent errors per chip per year. "1 per 3 million inferences" assumes one inference a second. For 72 accelerators (a GB300-class rack's count; Google tested TPUs, so illustrative only), about 635 a year, nearly 2 a day per satellite. Acceptable for inference with checking; open for training (Google's own words).
- Sun-synchronous orbits cross the South Atlantic Anomaly and the polar horns, so dose arrives in bursts [background].

### 5.2 Latency [calc]

- 650 km: one way 2.2 ms overhead, 4.3 ms at 25° elevation, 6.8 ms at 10°.
- A ground station sees a 650 km satellite for at most about 9 minutes above 10° elevation per pass in a 98-minute orbit. Continuous service needs relays: Starcloud files to use "nearly exclusively ... laser links" via third-party networks (FCC narrative, 4 Feb 2026) [primary, per scout].
- Dawn-dusk orbits pass over the poles and the terminator, so they sit far from population centres at midday; Google: "Maintaining a dawn-dusk orbit will increase latency to some ground locations" (1.2) [primary].

### 5.3 Bandwidth

- Ground: TBIRD, a 6U CubeSat at about 530 km, reached 200 Gbps on 28 April 2023 using two 100 Gbps channels, 4.8 TB error-free in one pass [press: Satellite Today 12 May 2023, IEEE Spectrum; MIT Lincoln Laboratory release; NASA NTRS 20250003969 "Two Years Demonstrating 200 Gbps Optical Downlink", May 2025]. No higher ground-LEO optical record found [press, not exhaustive].
- Between satellites: Google needs about 10 Tbps a link, 50 times TBIRD [calc].
- Optical ground links lose to cloud; site diversity is needed [background].

### 5.4 What binds first

On the primary record and the arithmetic: **mass per kW across array, radiator, compute hardware and shielding binds first**, because every one of them at heritage figures sits near the 10 kg per kW budget on its own:

| Item | Heritage or current figure | kg per kW | Tag |
|---|---|---|---|
| Solar array (ROSA, BOL) | 71 to 124 W/kg | 8 to 14 | primary, calc |
| Radiator at 1,400 W/m² | 9 to 14.2 kg/m² (ISS); 3 kg/m² (heat pipe, TRL 5) | 6.4 to 10; 2.1 | primary, calc |
| Compute hardware, ground rack | GB200 NVL72 about 1.36 t, about 120 kW | about 11 | press, calc |
| Batteries for 20 min eclipse | 150 to 270 Wh/kg cells | 1.2 to 2.2 (cells only) | primary, calc |
| Shielding | 1 kg per kW (Starcloud assumption) | about 1 | primary |

A space-built compute payload would shed the rack's steel, power shelves and copper, so 11 kg per kW is a ceiling, not a design point [background]. Radiation next (silent errors limit training, not inference); bandwidth limits training, not inference; latency is not the constraint for inference.

---

## 6. Heat pumps in orbit: the arithmetic

### 6.1 The live piece's area arithmetic, checked [calc]

Loop at 45°C (318.15 K), panel raised to 100°C (373.15 K), panel taken at the fluid temperature, no Earth or sun load, ε 0.92, array output 250 W/m²:
- Ideal (Carnot) work per kW lifted: (373.15 − 318.15) / 318.15 = 0.173 kW; at half of ideal 0.346 kW. **Matches the live piece.**
- Without pump: 1 kW at 1,069 W/m² = 0.935 m². With half-Carnot pump: 1.346 kW at 2,023 W/m² = 0.665 m². Saving 0.270 m². Extra array: 0.346 / 0.25 = 1.38 m². **Matches.** Ideal pump: saving 0.356 m² against 0.691 m² of array, about 1.9 times. **Matches "about twice".**
- Break-even: the pump saves *mass* if the array's kg per m² is below 0.270 / 1.383 = **0.195** of the radiator's kg per m² (half-Carnot), or 0.51 (ideal). **The live piece's "about a fifth" is right.**

### 6.2 The mass trade, which is what launch bills [calc]

Model: 1 kW of chip heat at loop temperature Tc; heat pump at 50% of Carnot lifts to Th; radiator mass = ρ_rad × (1 + W) / net flux(Th), with the vertical panel's 106 W/m² Earth load; array mass = W × (kg per kW of array). Pump compressor, fluid and extra electronics mass ignored, which favours the pump. Th capped at Tc + 75 K. Best Th chosen.

| Loop Tc | Radiator kg/m² | Array W/kg | No pump, kg/kW | Best with pump, kg/kW | Saving |
|---|---|---|---|---|---|
| 45°C | 3 | 100 or 250 | 3.1 | 3.1 (no pump) | 0% |
| 45°C | 3 | 500 | 3.1 | 2.8 at 112°C | 10% |
| 45°C | 6 | 100 | 6.2 | 6.2 (no pump) | 0% |
| 45°C | 6 | 250 | 6.2 | 5.6 at 112°C | 10% |
| 45°C | 14.2 | 100 | 14.7 | 13.4 at 106°C | 9% |
| 45°C | 14.2 | 250 | 14.7 | 10.6 at 120°C | 28% |
| 60°C | 3 | 100 or 250 | 2.5 | 2.5 (no pump) | 0% |
| 60°C | 6 | 250 | 5.1 | 4.8 at 105°C | 5% |
| 60°C | 14.2 | 100 | 12.0 | 11.6 at 99°C | 4% |
| 60°C | 14.2 | 250 | 12.0 | 9.2 at 135°C | 24% |

Reading [calc]:
- With heritage arrays (about 100 W/kg) and light radiators (3 to 6 kg/m²), **a heat pump never pays**. The live piece's conclusion holds there.
- With heavy ISS-class radiators, a pump saves 4 to 9% even with heritage arrays, and a quarter or more with 250 W/kg arrays. So the live heading "A heat pump cannot buy back the radiator" is **not true in general**; it is true only if radiators are already light.
- Warming the chip loop from 45°C to 60°C saves about 18% of radiator mass at every density (3.1 to 2.5; 6.2 to 5.1; 14.7 to 12.0) with no array penalty [calc]. **The cheapest lever is the chip's coolant temperature, not a heat pump.** That is the heat-and-water link.
- The pump's own hardware, the hotter working fluid (ammonia is unsuitable much above 100°C; water heat pipes run 125 to 300°C per Glenn [primary]), and moving parts in a 5-year no-repair craft all count against it [background].

---

## 7. Compute power per metric ton: the target against satellites flown

| Craft | Mass | Power | kW per tonne | kg per kW | Tag |
|---|---|---|---|---|---|
| SpaceX target, AI compute satellite | per tonne | "over 100 kilowatts of compute power per metric ton" | 100 | 10 | primary (424B4, 12 Jun 2026, per sidecar) |
| SpaceX AI1 web page | not given | "75 kW / ton" | 75 | 13.3 | primary (read 2 Nov 2026 by drafter) |
| SpaceX first generation (Johnsen) | 100 t a launch (target) | "About 5 megawatts per launch" | 50 | 20 | primary, calc |
| Starcloud white paper concept | about 100 t a launch | "~40 MW of compute" | about 400 | 2.5 | primary, calc |
| Starlink V2 mini (Google's estimate) | 575 kg | about 28 kW (estimate, all bus power) | 49 | 20.5 | primary estimate, calc |
| Starlink V1 (Google) | 260 kg | 7 kW (est.) | 27 | 37 | primary estimate, calc |
| OneWeb (Google) | 150 kg | 0.8 kW | 5.3 | 188 | primary estimate, calc |
| Iridium NEXT (Google) | 860 kg | 2 kW | 2.3 | 430 | primary estimate, calc |
| Starlink V3 | about 1.9 to 2 t | not disclosed | n/a | n/a | press |
| Starcloud-1 (Nov 2025) | 60 kg | not disclosed; one H100 (700 W board power [background]) | at most about 12 | at least about 86 | primary (Nvidia blog, 15 Oct 2025, per scout), calc |
| ISS radiator wings alone | 6,736 kg | 70 kW of heat | 10.4 (heat) | 96 | primary, calc |

Notes:
- Starlink figures are total bus power, not compute; a compute satellite must deliver most of its power to chips, so it is a generous comparison [calc].
- **Starcloud's 40 MW per 100 t launch fails on its own racks [calc]:** 300 racks at 120 kW at about 1.36 t each (GB200 NVL72, The Register, 21 Mar 2024 [press]) weigh about 408 t before any array or radiator; 40 MW of radiator at its own 633 W/m² is 63,000 m². The white paper's Table 1 bundles "compute module, solar & radiators" in one $5 million launch without itemising mass [primary].
- No AI compute satellite has published mass and power together. The best flown data point, Starcloud-1, is at least eight times short of 100 kW per tonne even if its GPU ran at full board power [calc].

---

## 8. What the live piece has wrong or out of date

1. **Live:** "Google's Suncatcher paper (arXiv, 22 November 2025)" and the radiation paragraph's "on the order of 1 per 3 million inferences"; sources line "arXiv 2511.19468, 22 November 2025"; evidence table "Google, Suncatcher paper, 22 November 2025".
   **Correction:** the 1-per-3-million figure and the 17 rad per event figure are from **v2, 17 June 2026**, which "Re-ran radiation test with improved methods". v1 (22 Nov 2025) said "1 per 10 million inferences" from HBM errors at one per 50 rad. Cite "arXiv 2511.19468, v1 22 November 2025, revised 17 June 2026" and quote v2. Add "assuming 1 inference per second", or better, state it per chip: about 9 silent errors per chip per year [calc]. Source: arXiv abstract page and both PDFs [primary].

2. **Live:** "Sunlight on one face costs Starcloud's panel about 123 W/m² and the Earth's glow about 14"; evidence table "14.46 W/m² from the Earth"; "67°C (68°C allowing for the Earth's glow)".
   **Correction:** Starcloud's 14.46 applies solar absorptivity (0.09) to the Earth's infrared; in the infrared the panel absorbs at its emissivity (0.92). Its own geometry then gives about 63 W/m² from the Earth and a net of about 585 W/m², not 633. A vertical two-sided panel at 650 km absorbs about 106 W/m² of Earth infrared, so 1,400 W/m² net needs about 73°C, not 68°C. Source: Starcloud white paper v1.03 p. 9 [primary]; [calc]; Kirchhoff's law [background]. The piece may keep 633 as "Starcloud's figure" but should not present the Earth's load as 14.

3. **Live:** "radiators as heavy as the International Space Station's would use that whole budget alone" (top layer), "a heritage radiator alone uses the whole 10 kg per kW" (closing), and the climax chart.
   **Correction:** true at 14 kg/m², but NASA Glenn (23 Jan 2025) gives the ISS radiator as "~9 kg/m2" and heat-pipe radiators as "~3 kg/m2" (TRL 5, 2011 full-scale test at 400 K); Juhasz (2008) gives pumped-loop radiators "6 to 10 kg/m2". At 1,400 W/m² that is 6.4 kg per kW (ISS per Glenn) and 2.1 (heat pipe). State the range and name which heritage. Sources: NESC webinar pp. 6 and 8; NASA/TM-2008-215420 [primary]; [calc].

4. **Live (thesis):** "In orbit the plug is free, and the heat is the bill"; "Solar arrays have flown for decades"; "the radiator loses the air and water it leans on ... The last step binds."
   **Correction (substantive, not a typo):** at SpaceX's own figures the array is 5.6 times the radiator's area, and heritage arrays (Redwire ROSA 71 to 124 W/kg) weigh 8 to 14 kg per kW: alone at or over the 10 kg per kW budget. The fuel is free; the collector is not. In mass the array is at least as large a bill as the radiator unless radiators stay at ISS density. The rebuild should present both surfaces, or argue explicitly why the radiator is harder (it cannot be made thinner than its loop, it must be leak-proof, it cannot exceed the chip's temperature). Sources: Redwire ROSA page [primary]; NASA SOA power chapter [primary]; transcript FWP 9 Jun 2026 [primary]; [calc].

5. **Live (heading):** "A heat pump cannot buy back the radiator, because solar is the weaker surface".
   **Correction:** the area arithmetic is right (and the piece's own break-even, array under about a fifth of the radiator's kg per m², is right), but on mass a heat pump saves about 9% with ISS-density radiators and 100 W/kg arrays, and about 28% with 250 W/kg arrays. It fails only when radiators are light (3 to 6 kg/m²). The heading should be conditional, and the piece is internally inconsistent: it argues ISS-heavy radiators in the climax and light radiators (implicitly) in the heat-pump section. Raising the chip loop from 45°C to 60°C cuts radiator mass about 18% with no array cost [calc].

6. **Live:** "On Musk's figures the array collects about 250 W per square metre".
   **Correction:** 250 W/m² is the array's *electrical output* ("250 watts per square meter for the solar array", transcript 9 Jun 2026 [primary]); it collects about 1,361 W/m² of sunlight, 18% conversion [calc]. Use "delivers".

7. **Live:** "in a dawn-dusk orbit the panels see the sun almost all the time, so there is no night"; Johnsen's "24 hours a day" implied.
   **Correction:** at 650 km a dawn-dusk orbit has about 87 days a year with an eclipse every orbit, up to about 20 minutes of each 98-minute orbit; eclipse-free only above about 1,400 km [calc]. Google says the orbit "reduces the need for heavy onboard batteries" (blog, 4 Nov 2025) [primary]. "Almost all the time" is fair for the year (eclipse is about 2 to 3% of annual time [calc, rough]); "no night" is not.

8. **Live:** "NPR, the American public broadcaster, reported the next day [2 October] that it carries four of Google's TPU chips"; evidence table "NPR, 2 October 2026".
   **Correction:** NPR published on **1 October 2026** (11:41 PDT, Ruwitch and Brumfiel), the launch day, with a correction appended 2 October. The correction matters: the prototype "is in a standard orbit and uses batteries", not a dawn-dusk orbit, so it does not test the orbit the design depends on. Source: NPR via KUOW syndication [press]. (Google's own launch date and 30 October post not re-opened in this slice.)

9. **Live:** "Elon Musk ... puts SpaceX's figure at about 1,400 W/m², from two-sided radiators"; chart "near 67°C".
   **Correction (add, not delete):** the transcript says "The radiators are radiating on both sides" and "1,400 watts per square meter is a very achievable goal", and separately "Over time ... above 1,400 watts per square meter". It does not say whether 1,400 is per m² of panel or per face. Read per panel it needs about 67 to 73°C, above the 45°C inlet and about 55°C chip outlet of Nvidia's newest liquid-cooled racks; read per face it needs about 131°C [calc: (2,800/(2 × 0.92 × σ))^¼ = 404 K]. Either way SpaceX implies a coolant hotter than ground practice. Sources: transcript FWP 9 Jun 2026 [primary]; Nvidia figures via `research-build/topics/heat-research/physics.md` [primary there, not re-opened].

10. **Live:** "At 650 km light takes about 2 milliseconds each way".
    **Correction (precision):** 2.2 ms straight overhead; 4.3 ms at 25° elevation and 6.8 ms at 10°, where most of a pass is spent [calc]. "A few milliseconds" is safer.

11. **Live:** ISS "wings, about 96 kg per kW as flown"; "ammonia loop runs at about 3°C".
    **Correction (precision):** 96 kg per kW counts the six radiator units only; with the two rotary joints (420.5 kg each) it is about 108 [primary, calc]. The supply is 2.8°C but the radiator outlet goal is minus 40°F (minus 40°C), so the panel runs colder than 3°C on average; that is why its flux is 147 W/m² [primary, ATCS overview pp. 6 and 16].

12. **Live:** "Google's ground test says radiation dose is not the gate ... a shielded five-year mission".
    **Add:** the shielding is "10 mm Al equivalent" (Suncatcher 2.3), 27 kg per m² of enclosure, so the dose result is bought with mass [primary, calc].

13. **Live:** "Google ... sees $200, where launch could stop being the limit, around 2035."
    **Precision:** fine, but v2's abstract says "≲$200/kg by the mid-2030s" and the ∼2035 date assumes "∼180 Starship launches/year" at 200 t each; at 72% less mass launched, "∼$300/kg". v2 dropped v1's $500/kg-to-GTO derivation, so the $200 now rests only on "often cited, by SpaceX and others" [primary].

14. **Live (sources line):** cites Suncatcher only as 22 November 2025; cites the ISS overview as "undated".
    **Correction:** add the v2 date. The ISS overview is undated but describes assembly stages and was uploaded to nasa.gov in February 2021 (URL path) [primary]; say "undated, describes the system at assembly".

---

## 9. Could not verify

- **SpaceX prospectus pages** (424B4, 12 Jun 2026): EDGAR returned an automated-access block to my direct download today; the quotes on radiation-only cooling, "100 kilowatts of compute power per metric ton", "substantially larger radiators", mass "continue to be refined" and "five times the solar array output compared to V3" rest on the earlier drafter's reading (sidecar, 2 Nov 2026). EDGAR full-text search today confirms "radiator", "per metric ton" and "kilowatts of compute" appear in the 424B4 and S-1/As.
- **Whether Musk's 1,400 W/m² is per panel or per face**, and what coolant temperature SpaceX assumes. Not in the transcript.
- **Starlink V3 mass and power, and any Starlink array W/kg.** Press gives about 1.9 to 2 t for V3; no SpaceX figure for power or array mass found.
- **Starcloud-1 power** and **Starcloud-2 mass, power and radiator areal density.** Starcloud's site (read 7 Nov 2026) gives no figures; "10 times lower mass per watt than the ISS radiator" and 8 kW are press-relayed CEO statements; launch "by 2027" per Starcloud's page.
- **The source of NASA Glenn's "~9 kg/m2" for ISS** versus the 2022 paper's 14 kg/m²; which mass each includes.
- **Measured radiator flux or areal density from any compute satellite in orbit.** None published.
- **Solar array degradation rates** for thin silicon or Starlink-class arrays in a 550 to 650 km sun-synchronous orbit; no primary found today.
- **iROSA wing mass** (Wikipedia gives 325 kg; source unclear).
- **GB200/GB300 NVL72 rack mass** from Nvidia itself (1.36 t is press).
- **Albedo load on a vertical radiator in a dawn-dusk orbit**: estimated as a few W/m², not integrated.
- **Google's Suncatcher prototype** mass, power, radiator and orbit details, beyond NPR's syndicated text; Google's 24 September and 30 October 2026 posts were not re-opened in this slice.
- **Any ground-to-LEO optical downlink record above TBIRD's 200 Gbps** since 2023; one search found none.
- **The Schunk and others (2022) 14 kg/m² quote** was not re-opened today (scout read it 2 Nov 2026).

---

## Sources (opened 7 Nov 2026 unless noted)

- Google, arXiv 2511.19468, v1 (22 Nov 2025) and v2 (17 Jun 2026): https://arxiv.org/abs/2511.19468 ; https://arxiv.org/pdf/2511.19468v1 ; https://arxiv.org/pdf/2511.19468 [primary]
- Google Research blog, Beals, 4 Nov 2025: https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/ [primary]
- NASA/Boeing, ISS ATCS Overview (undated): https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf [primary]
- NASA Glenn, Sanzi and Thaikattil, "Heat Pipe/Thermal Technologies at GRC", NESC webinar, 23 Jan 2025: https://nescacademy.nasa.gov/downloadFile/1439 [primary]
- Juhasz, NASA/TM-2008-215420, Oct 2008: https://ntrs.nasa.gov/api/citations/20080045532/downloads/20080045532.pdf [primary]
- NASA Small Spacecraft Technology State of the Art, Power (page dated 7 May 2026): https://www.nasa.gov/smallsat-institute/sst-soa/power-subsystems/ [primary]
- Redwire ROSA product page: https://rdw.com/product-archive/power/rosa/ [primary]
- Starcloud (Lumen Orbit) white paper v1.03, Sep 2024: https://starcloud.com/wp [primary]; Starcloud pages /starcloud-1 and /starcloud-2 [primary, company]
- SpaceX interview transcripts FWP, filed 9 Jun 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026041761/fwp_cfointerview.htm [primary]
- EDGAR full-text search, CIK 1181412 (7 Nov 2026) [primary, index only]
- NPR, Ruwitch and Brumfiel, 1 Oct 2026, corrected 2 Oct 2026, via KUOW: https://www.kuow.org/npr-news/2026-10-01/google-launches-project-suncatcher-a-step-towards-ai-data-centers-in-space [press]
- TBIRD: Satellite Today, 12 May 2023; IEEE Spectrum; MIT Lincoln Laboratory; NASA NTRS 20250003969 [press and primary index; not opened in full]
- The Register, 21 Mar 2024, GB200 NVL72 rack 1.36 t: https://www.theregister.com/2024/03/21/nvidia_dgx_gb200_nvk72 [press, via search summary]
- Earlier site research reused, not re-opened: `research-build/deep-pieces/gap-space.notes.md`, `data-centres-in-space.sidecar.md` (2 Nov 2026); `research-build/topics/heat-research/physics.md` (Nvidia coolant temperatures)
