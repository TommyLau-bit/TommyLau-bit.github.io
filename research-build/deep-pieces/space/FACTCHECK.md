# Fact-check: data centres in orbit (space.src.md, charts.py, illos.py, assemble.py)

Independent check, 7 November 2026. Piece not edited. Each item quotes the current text exactly, for string-match replacement.

## What was checked at the primary source today

- SpaceX 424B4 (12 June 2026), read in full text in the browser: "radiation rather than convection and conduction", "over 100 kilowatts of compute power per metric ton", "approximately one million metric tons to orbit annually", "continue to be refined" (context: "The precise solar collection area, total system mass per satellite, and on-orbit assembly requirements associated with this goal continue to be refined"), "will not be easily repaired or upgraded" (subject: "orbital AI compute infrastructure"), "is inherently shorter", "advances in nuclear energy ... may be materially diminished". All verbatim.
- SpaceX interview transcripts FWP (folder dated 9 June 2026; video uploaded 8 June): Johnsen "roughly five times, if not more, energy per cell"; Musk "about 1,400 watts per square meter for the radiators", "The radiators are radiating on both sides.", "a very achievable goal", "cooling is actually much easier in space than it is on Earth"; Johnsen "About 5 megawatts per launch" (context below, E6). The 150 kW and 120 kW figures appear in no SpaceX filing before this FWP (EDGAR full-text search).
- SEC staff letter 24 April 2026, comment 26: "power-to-mass ratios underlying the 100-gigawatt annual deployment goal"; "total estimated solar collection area, total system mass". Verified.
- SpaceX Q3 release (8-K, 20 Oct 2026): Flight 14 "our first orbital Starship flight, delivering 26 Starlink V3 satellites" (flight was 28 Sep 2026, inside Q3); nameplate compute 1.7 GW. 10-Q to 30 Sep 2026: no orbital compute term (read in full in the browser; the only "in space" is "humanity's presence in space"). Q3 call (third-party transcript): Shotwell "we'll begin flying mobile V2 and Starmind satellites in 2027". Verified.
- SpaceX Starmind page (all three tabs, read 7 Nov 2026): every figure in the piece verified verbatim (250 kW peak / 175 kW average, 75 kW / ton, 75 m wingspan, 210 kW array, 250 W / m², 160 m² radiator, "as soon as late 2027"). The thermal tab also lists "Redundant pumping loops" and "Integrated micrometeoroid shielding", which supports the "spare loops and armour" sentence.
- SpaceX FCC letter of 29 May 2026 (ICFS SAT-LOA-20260108-00016): table for 550 to 585 km, area-to-mass 0.1333, total area 800 m², "Bus & Radiator Area" 100 m², mass 3000 kg. Verified. FCC DA 26-113 (4 Feb 2026) and Report SAT-01982 (13 Mar 2026, Starcloud, 88,000, filed 4 Feb): verified.
- Google arXiv 2511.19468 v2 (17 June 2026, "Re-ran radiation test with improved methods"): every quote and number in the piece verified (81 satellites, 650 km, 100 to 200 m, 2 krad, 750 rad, "approximately one event/17 rad", "1 per 3 million inferences, assuming 1 inference per second", "requires further study", "10Tbps", TBIRD quote, "$3,600/kg, based on Falcon 9 (reusable configuration)", "often cited, by SpaceX and others", "≲$200/kg by the mid-2030s", "∼180 Starship launches/year", about $300, $14,700, $810, $570 to $3,000, 575 kg, 28 kW). Google blogs 4 Nov 2025 ("up to 8 times more productive than on earth"; "reduces the need for heavy onboard batteries"), 1 Oct 2026 (Transporter-18, Planet, Joule), 30 Oct 2026 (Gemma 4, Svalbard, thermal and radiation tests, twin satellites 2027): verified.
- Starcloud white paper v1.03 (September 2024): 770.48, 14.46, 122.94, the α = 0.09 Earth term, "albeit at an added energy cost": verified. Starcloud-2 page: "fully operational in sun-synchronous orbit by 2027": verified.
- NASA ISS ATCS overview (1,122.64 kg, 23.3 m by 3.4 m, 70 kW, 22 Inconel tubes in two flow paths, 2.8°C supply); NASA Glenn webinar 23 Jan 2025 ("~9 kg/m2"; heat-pipe "~3 kg/m2"; "Full Scale Radiator Demonstration (RDU) ... NETS 2011"); Juhasz NASA/TM-2008-215420, October 2008 ("6 to 10 kg/m2"); NASA SST state of the art power, 7 May 2026 ("~30 W/kg", "150-270 Wh/kg"); Redwire ROSA table (six configurations, 71 to 124 W/kg); Gaalema, Indyk and Staley arXiv 2604.07760 (9 Apr 2026, "about 500 W/kg", "custom solutions for all components"); Astro Digital Form 425 ("it has since run AI inference on orbit"). All verified.
- NPR via KUOW (1 Oct 2026, corrected 2 Oct 2026): four TPUs, "15 minutes at a time due to heat management constraints", "standard orbit and uses batteries". Verified, with a tense issue (F9).

All "my arithmetic" figures were recomputed (σ = 5.670 × 10⁻⁸, ε 0.92, two faces): 581 / 771 / 1,069 / 1,096 at 47°C / 1,400 at 67.2°C / 2,023 at 100°C; 1.81 times from 20°C to 67°C; 1% gives 4.06%; Earth view factor 0.241 per face, 106 W/m², 73.5°C for 1,400 net; Starcloud corrected 62.8 and 584.8 W/m²; ISS 96.2 kg/kW, 147 W/m², 14.2 kg/m²; 840 m² array (3.2 tennis courts, 18.4% of 1,361); 125 to 299 m² of radiator; radiator 2.1 / 6.4 / 10.1 kg/kW; Redwire 71.0 to 124.1 W/kg; batteries 148 to 267 kg at 40 kWh; 58.3 / 83.3 / 50 / 48.7 / 11.7 kW per tonne; heat pump 0.346 kW work, 0.270 m² saved, 1.38 m² array, break-even 0.195; pump mass saving 9.0% (14.2 kg/m², 100 W/kg) and 27.8% (250 W/kg, 120°C cap); 45 to 60°C coolant saves 18.3% (with Earth load); 27 kg/m² of aluminium; 2.17 ms overhead; 8.8 silent errors a year; 3 million tonnes; 10,000 flights; orbital period 97.6 min; eclipse up to 19.7 min. All hold except where flagged below.

No share price, valuation, target or view on shares found. No em or en dashes in any of the four files. No American spellings outside verbatim quotes ("meter" and "ton" appear only inside quotes; "licenses" is the British verb).

---

## Errors (wrong as stated)

**E1. The order of SpaceX's published designs (line 50).**
Current: "The letter was filed on 29 May 2026, when SpaceX's public design was smaller: about 120 kW average, 150 kW peak."
Problem: the 150 kW peak and 120 kW average figures first appear in the interview transcripts SpaceX filed on 9 June 2026 (video uploaded 8 June), after the letter. EDGAR full-text search finds "150 kilowatts" and "120 kilowatts" in no filing before that FWP. On 29 May the filed figure was the S-1's "early satellites generating 100 kilowatts of compute power" (S-1, 20 May 2026; also in the 424B4).
Fix: "The letter was filed on 29 May 2026, when SpaceX's published plans were smaller: its S-1 spoke of early satellites "generating 100 kilowatts of compute power", and its interviews of early June of about 120 kW average and 150 kW peak."

**E2. Nvidia's blog could not report the launch (line 166).**
Current: "Starcloud-1, a 60 kg satellite "about the size of a small fridge", launched in November 2025 with one Nvidia H100 GPU, Nvidia's blog said."
Problem: the Nvidia blog is dated 15 October 2025, before the launch (2 November 2025). It describes the satellite's mass and size, not the launch. The launch in November 2025 with the H100 is stated by Starcloud's own page and by Astro Digital's Form 425.
Fix: "Starcloud-1, a 60 kg satellite "about the size of a small fridge", as Nvidia's blog described it before launch, went up in November 2025 with one Nvidia H100 GPU, Starcloud says."

**E3. Google's chip was not the first data-centre-class chip in orbit (line 170).**
Current: "That is worth pausing on. The first data-centre-class chip in orbit runs minutes at a time, and its first published limit is heat."
Problem: Starcloud-1 carried an Nvidia H100, a data-centre GPU, into orbit in November 2025, eleven months before Google's prototype; the piece says so four lines earlier. Google's blog says "a data center class TPU in orbit", not the first data-centre-class chip. Also, NPR's wording is a plan ("The chips will run ... for 15 minutes at a time"), and the heat limit is a press report, not something Google published.
Fix: "That is worth pausing on. Google's first data-centre-class chip in orbit is to run minutes at a time, NPR reported, and the limit it gave is heat."

**E4. The eclipse battery uses the old 120 kW design (line 112 and the evidence fold, line 268).**
Current (line 112): "Riding through 20 minutes at 120 kW takes about 40 kilowatt-hours of battery, roughly 150 to 270 kg of cells."
Current (line 268): "120 kW for 20 minutes is 40 kWh."
Problem: everywhere else the piece uses SpaceX's current page, 175 kW average. 120 kW is the superseded June design. At 175 kW, 20 minutes is 58 kWh, 216 to 389 kg of cells at 150 to 270 Wh/kg, my recomputation. The per-kW figure (1.2 to 2.2 kg) in the budget chart is unchanged.
Fix (line 112): "Riding through 20 minutes at 175 kW takes about 58 kilowatt-hours of battery, roughly 220 to 390 kg of cells."
Fix (line 268): "175 kW for 20 minutes is about 58 kWh."

**E5. "Each part alone" overstates the budget chart (line 122, the budget-chart title in assemble.py, the aria label in charts.py).**
Current (line 122): "Each item alone sits near the whole budget."
Current (assemble.py, budget-chart title): "Each part alone uses most of SpaceX\'s 10 kilogram budget"
Current (charts.py, budget-chart aria, end): "Each part alone sits near the whole budget."
Problem: on the piece's own figures, eclipse batteries are 1 to 2 kg per kW (10 to 20% of the budget) and the radiator's light end is 2.1 kg per kW. Only the array (8 to 14) and a ground rack (about 11) sit near or over 10 on their own; the radiator reaches 10 only at station weight.
Fix (line 122): "The array alone, or a ground rack alone, sits near or over the whole budget, and a station-weight radiator would too."
Fix (assemble.py title): "The array alone uses most of SpaceX\'s 10 kilogram budget"
Fix (charts.py aria end): "The array alone, or a ground rack alone, sits near or over the whole budget."

**E6. Johnsen's 5 megawatts is not tied to 100 tonnes (line 126; kwpt chart in charts.py; evidence fold line 272).**
Current (line 126): "Johnsen's "About 5 megawatts per launch", at the 100 tonnes a launch SpaceX targets for Starship, is about 50."
Current (charts.py kwpt row): "('Per Starship launch', '5 MW / 100 t', 50, 50, 'c-bar', '50'),"
Current (charts.py kwpt aria): "Five megawatts per Starship launch of 100 tonnes, 50."
Problem: in the transcript Johnsen gives 5 MW "with the existing first iteration of our satellite and our V3 version of Starship we just flew". 100 tonnes is SpaceX's target "over time" (roadshow, "100 Metric tons per launch over time"), not the payload of the launch Johnsen describes. Dividing one by the other is the piece's assumption; if V3 Starship carries less than 100 t, the ratio is higher.
Fix (line 126): "Johnsen's "About 5 megawatts per launch", for the first satellite on today's Starship, would be about 50 if each launch carried the 100 tonnes SpaceX targets over time, my arithmetic."
Fix (charts.py row sub-label): "'5 MW / 100 t, if full'"
Fix (charts.py aria): "Five megawatts per Starship launch, divided by the 100 tonnes SpaceX targets over time, 50."

---

## Flags (imprecise, overstated or unverifiable)

**F1. "SpaceX's own published design" mixes two sources (summary, line 4; line 16).**
Current (line 4): "SpaceX's own published design comes to about 58 kilowatts of computing per tonne against its target of 100,"
Current (line 16): "On SpaceX's own published figures, its satellite carries about 58 kilowatts of computing per tonne, against its own target of 100."
Problem: 58 combines the FCC mass (which the piece itself says may belong to the earlier design) with the current page's power. SpaceX's own page says 75 kW per ton. The top of the piece should not present 58 as SpaceX's design figure.
Suggested (line 4): "SpaceX's filed mass and published power come to about 58 kilowatts of computing per tonne, and its own page claims 75, against its target of 100,"
Suggested (line 16): "On the mass SpaceX filed and the power it publishes, its satellite carries about 58 kilowatts of computing per tonne; its own page claims 75. The target is 100."

**F2. What Google says about $200 (summary, line 4; line 178).**
Current (line 4): "and today's launch price is far above the level Google says would make orbit pay."
Current (line 178): "Thousands of dollars a kilogram today, and Google says $200 is where launch stops being the main cost."
Problem: the paper says $200 "is often cited, by SpaceX and others, as a threshold beyond which launch could cease to be the limiting cost factor". It does not say orbit then pays; it compares launch with ground power only.
Suggested (line 4): "and today's launch price is far above the $200 a kilogram at which Google's paper says launch could stop being the main cost."
Suggested (line 178): "Thousands of dollars a kilogram today, and Google cites $200 as the level where launch could stop being the main cost."

**F3. Musk's 1,400 is not stated as per square metre of panel (line 76).**
Current: "On my arithmetic, a shaded two-sided panel at emissivity 0.92 sheds that only near 67°C."
Problem: the transcript gives "about 1,400 watts per square meter for the radiators" and, separately, "The radiators are radiating on both sides". It does not say whether 1,400 is per square metre of panel or per face. Read per face, it needs about 131°C. The piece's reading is the generous one; say so.
Suggested: "Read as watts per square metre of panel, which the interview does not specify, a shaded two-sided panel at emissivity 0.92 sheds that only near 67°C, on my arithmetic."

**F4. SpaceX's 47°C ignores the Earth's glow the piece adds two paragraphs later (line 78; illos.py craft labels and aria).**
Current (line 78): "Its 175 kW average over 160 square metres is about 1,090 watts per square metre, which the same panel sheds near 47°C. That fits warm-water coolant, but it needs more area for each kilowatt."
Current (illos.py): "sheds 175 kW at about 47°C," and in the aria "sheds that heat at about 47 degrees, glowing from both faces."
Problem: with the 106 W/m² of Earth infrared the piece itself uses at 650 km, 1,094 W/m² net needs about 54°C, my arithmetic, which is the coolant's chip-outlet temperature (about 55°C) and leaves no margin for the panel running cooler than its loop.
Suggested (line 78): "Its 175 kW average over 160 square metres is about 1,090 watts per square metre, which the same panel sheds near 47°C in deep shade, or near 54°C once the Earth's glow is counted, my arithmetic. That is about the temperature at which coolant leaves Nvidia's chips, so it fits warm-water coolant with little to spare."
Suggested (illos.py label): "sheds 175 kW at about 47°C," → "sheds 175 kW at 47 to 54°C," and in the aria "at about 47 degrees" → "at about 47 to 54 degrees, counting the Earth's glow".

**F5. The light heat-pipe radiator was built and tested hot (line 94, line 96).**
Current (line 96): "The light end is a design tested on the ground; the heavy end has flown for decades."
Problem: NASA Glenn's slide says heat-pipe radiators "Can be designed to operate from 125-300 C", and the 2011 full-scale unit "Operated at 400 K" (127°C). Its ~3 kg/m² has not been shown at the 45 to 70°C of a chip loop, where water heat pipes carry less heat and other working fluids are needed.
Suggested: "The light end is a design tested on the ground, at 127°C, far hotter than a chip loop; the heavy end has flown for decades."

**F6. The heat-pump saving with "today's arrays" assumes 100 W/kg (line 144).**
Current: "On my arithmetic, with a radiator at 14 kg per square metre, a pump saves about 9% of radiator-plus-array mass with today's arrays."
Problem: recomputed, 9% holds at 100 W/kg. Across Redwire's own 71 to 124 W/kg the saving runs from about 2% to about 15%.
Suggested: "On my arithmetic, with a radiator at 14 kg per square metre, a pump saves about 9% of radiator-plus-array mass with arrays at 100 watts per kilogram, and 2 to 15% across Redwire's range."

**F7. Google's shielding is an example, "e.g." (line 156).**
Current: "The shielding behind that dose figure is "10 mm Al equivalent"."
Problem: the paper says "significant shielding (e.g. 10 mm Al equivalent)". The quote drops "e.g.", which turns an example into a specification.
Suggested: "The dose figure assumes "significant shielding (e.g. 10 mm Al equivalent)"."

**F8. Latency near the horizon (line 158).**
Current: "and about 7 near the horizon."
Problem: about 6.8 ms is at 10 degrees above the horizon; at the horizon itself it is about 9.8 ms, my arithmetic.
Suggested: "and about 7 when it is 10 degrees above the horizon."

**F9. NPR's 15 minutes is a plan (line 168).**
Current: "NPR, the American public broadcaster, reported that it carries four TPUs and runs Gemma "15 minutes at a time due to heat management constraints"."
Problem: NPR wrote "The chips will run a version of the company's Gemma AI model for 15 minutes at a time due to heat management constraints". Future tense, at launch.
Suggested: "NPR, the American public broadcaster, reported that it carries four TPUs and would run Gemma "15 minutes at a time due to heat management constraints"."
Optional addition from the same NPR report: Beals said "the radiators are one of the heaviest components on the current mission", which supports the spine (label as reported).

**F10. The TechCrunch quote is not verified at source, and "the only large rocket" (line 186).**
Current: "Starcloud's chief executive, Philip Johnston, told TechCrunch on 21 August 2026 that launch "is pretty constrained right now", as reported. If one company owns the only large rocket and builds its own computing satellite too, its satellites may fly first."
Problem: I could not find the TechCrunch article or the exact words; the research notes had them via TheNextWeb. Other launchers fly (Blue Origin's New Glenn among heavy ones), so "the only large rocket" overstates; Starship is the only one in the 100-tonne class.
Suggested: "Starcloud's chief executive, Philip Johnston, told TechCrunch in August 2026 that launch is constrained, as reported. If one company owns the only rocket of Starship's size and builds its own computing satellite too, its satellites may fly first."

**F11. "Several times" understates the gap (line 190; price-chart title in assemble.py).**
Current (line 190): "At today's launch price, power in orbit costs several times a ground hall's power bill."
Current (assemble.py): "At today\'s fare orbit costs several times the ground; at $200 it falls inside its range"
Problem: $14,700 against $570 to $3,000 is about 5 to 26 times.
Suggested (line 190): "At today's launch price, the launch bill alone is five to 26 times a ground hall's power bill."
Suggested (assemble.py): "At today\'s fare orbit costs five to 26 times the ground; at $200 it falls inside its range"

**F12. The disposal request is for flexibility and a waiver (line 206).**
Current: "SpaceX's letter of 29 May asks to dispose of satellites above 600 kilometres into higher orbits or around the sun, rather than by burning them up in the atmosphere."
Problem: the letter "seeks flexibility to use a disposal method other than atmospheric reentry" between 600 and 2,000 km and asks a waiver for those it does not re-enter; it will tailor plans and may still re-enter some.
Suggested: "SpaceX's letter of 29 May asks for the freedom, and a waiver, to dispose of satellites above 600 kilometres into higher Earth orbits or around the sun, rather than only by burning them up in the atmosphere."

**F13. 3,000 kg is given only for the shells below 600 km (line 208; claims.ts watch list).**
Current (line 208): "A million satellites of 3,000 kg each would be about three million tonnes in orbit, my arithmetic, so debris is not a footnote."
Problem: the letter's mass table covers only the four shells below 600 km; six groups make up the million, and SpaceX says it may build different hardware for different shells (DA 26-113, note 3). Fine as an illustration if labelled.
Suggested: "If all million weighed the 3,000 kg filed for the lowest shells, that would be about three million tonnes in orbit, my arithmetic, so debris is not a footnote."
claims.ts (watch list, not the claim or test): "mass filed with the FCC at 3,000 kg per satellite, 29 May 2026" is imprecise rather than wrong; the precise form is "3,000 kg per satellite for the shells below 600 km". Not a wrong fact, so no change is required under the claims rule.

**F14. "Every orbital builder needs" (line 216).**
Current: "SpaceX flies the rockets every orbital builder needs and is paid per kilogram whoever's satellite goes up."
Problem: other launchers exist. What is true: both flown compute satellites (Starcloud-1 on Bandwagon-4, Google's prototype on Transporter-18) went up on SpaceX rideshares.
Suggested: "SpaceX flew both computing prototypes now in orbit, Starcloud's and Google's, and is paid per kilogram whoever's satellite goes up."

**F15. Planet's role (line 218).**
Current: "Astro Digital built Starcloud-1, and Planet built Google's prototype."
Problem: Google says the prototype was "built in partnership with Planet". Close, but the primary does not say Planet built it alone.
Suggested: "Astro Digital built Starcloud-1, and Planet built Google's prototype with Google."

**F16. 1.7 GW is nameplate, and a filing says it (line 222).**
Current: "Its own computing today is on the ground: 1.7 gigawatts at the end of the third quarter, its finance chief said."
Problem: the figure is "nameplate compute"; it is in the Q3 release and the 10-Q (primary), not only on the call.
Suggested: "Its own computing today is on the ground: 1.7 gigawatts of nameplate capacity at the end of the third quarter, its quarterly report says."

**F17. What the page says about late 2027 (line 236).**
Current: "SpaceX's page says production starts "as soon as late 2027"."
Problem: the page says the factory "is planned to enable rapid production and deployment of thousands of AI satellites starting as soon as late 2027". Production at scale, not the start of production.
Suggested: "SpaceX's page says its factory should enable production and deployment of thousands of satellites "starting as soon as late 2027"."

**F18. The repair quote's subject (line 100).**
Current: "SpaceX's own risk factors say its satellites "will not be easily repaired or upgraded"."
Problem: the 424B4's subject is "orbital AI compute infrastructure", not satellites in general.
Suggested: "SpaceX's own risk factors say its orbital computing "will not be easily repaired or upgraded"."

**F19. Jumbo jet wingspan (line 42).**
Current: "On SpaceX's own published design, a satellite about as wide as a jumbo jet's wings, mostly made of solar array."
Problem: a Boeing 747-400 spans about 64 m and a 747-8 about 68 m; 75 m is wider (an A380 is about 80 m). Background figures, not from the piece's sources.
Suggested: "On SpaceX's own published design, a satellite a little wider than a jumbo jet's wings, mostly made of solar array."

**F20. "Not five times lighter" depends on which radiator (line 106).**
Current: "An array is thinner than a radiator, but not five times lighter."
Problem: on the piece's own numbers, Redwire arrays at 250 W/m² weigh about 2 to 3.5 kg per square metre. That is about as heavy per square metre as a 3 kg/m² heat-pipe radiator, but four to seven times lighter than the station's 14.2 kg/m².
Suggested: "An array is thinner than a radiator, but unless the radiator is station-heavy, not five times lighter."

**F21. "Each use most of a 10 kg budget" (line 246).**
Current: "At the scale of the satellite, the array and the radiator each use most of a 10 kg budget."
Problem: same as E5. The array does (8 to 14); the radiator uses between a fifth and all of it (2 to 10).
Suggested: "At the scale of the satellite, the array uses most of a 10 kg budget, and the radiator between a fifth and all of it."

**F22. Eclipse days are model-dependent (line 112).**
Current: "there are about 87 days a year with an eclipse on every orbit, up to about 20 minutes of each 98-minute circuit."
Problem: my recomputation (cylindrical shadow, J2 sun-synchronous inclination 98.0°, true sun) gives about 90 days and 19.7 minutes; the notes' 87 used a mean sun. Both round to about three months.
Suggested: "there are about three months a year with an eclipse on every orbit, up to about 20 minutes of each 98-minute circuit." (and "about 87 days" in the evidence fold to "about 87 to 90 days, depending on the model")

**F23. The FCC grant status is an absence, not a record (line 174).**
Current: "Neither has been granted, as of 7 November 2026."
Problem: no grant appears in FCC public notices searched; ICFS itself was not checked. Fair, but the wording claims a record.
Suggested: "Neither had been granted in any FCC public notice I could find, as of 7 November 2026."

**F24. Station radiator flux is a design capability (line 92).**
Current: "The station's loop runs cold, about 3°C, to cool a crew, so each square metre sheds only about 147 watts."
Problem: 70 kW is the EATCS total capability "at assembly complete", and the 2.8°C is the supply setpoint; the outlet goal is far colder. Fine as an order of magnitude; "so" implies a single cause.
Suggested: "The station's loop runs cold, about 3°C at supply, to cool a crew, and on its rated 70 kW each square metre sheds only about 147 watts."

## claims.ts, entry 'data-centres-in-space'

No wrong fact found. The 100 kW per metric ton target, the $200 figure, the FCC file number, the 88,000 and one million counts, the Starmind "as soon as late 2027" wording, the Planet 8-K's two prototypes "targeting launch in 2027" and the ISS 14 kg/m² all check against the sources. Two imprecisions, neither a wrong fact, so neither needs a change under the rule: the claim calls $200 "Google's ... threshold", while the paper cites it as "often cited, by SpaceX and others"; and the 3,000 kg applies to the shells below 600 km (F13).

## Could not verify

- The exact TechCrunch wording and date for Johnston (F10).
- FCC grant status beyond public notices (ICFS not checked) (F23).
- Nvidia's own Space-1 Vera Rubin release text (March 2026); secondary coverage confirms a March 2026 GTC announcement.
- The Nvidia blog of 15 Oct 2025 was not opened directly; secondary coverage confirms "about 60 kilograms" and "the size of a small fridge".
- The Register's 1.36 t GB200 rack figure (press, labelled as such in the piece).
