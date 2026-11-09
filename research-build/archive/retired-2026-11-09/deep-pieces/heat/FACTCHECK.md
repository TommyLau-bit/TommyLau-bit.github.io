# Fact-check: heat-and-water depth draft (heat.src.md, charts.py, illos.py, assemble.py)

Checked 7 November 2026 against primary sources wherever they could be opened. No share prices, valuations, ratings or views on shares were found. No em or en dashes were found in heat.src.md, assemble.py, charts.py or illos.py. No quote contains "center"; one quote contains the US spelling "liters" (LBNL), which the checker does not fail.

Summary: 12 errors, 22 flags.

---

## Errors

### E1. Nvidia's "1% of the year" quote is inverted and unattributed (line 136)

Current: "Its blog says chillers are needed "outside of maybe 1% of the year ... in some climates" (21 June 2026)."

Source: Nvidia blog, Josh Parker, "Hotter Than a Hot Tub", 21 June 2026, https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/ . The words are Ali Heydari's: the design runs closed loop "outside of maybe 1% of the year when we might need chillers in some climates." The same post says chillers "may turn on just a few days a year" in favourable conditions. As written, the ellipsis makes the quote say chillers are needed outside of 1% of the year, which means 99% of the year: the opposite of the source.

Replace with: "Nvidia's cooling director, Ali Heydari, says on its blog that chillers may be needed in "maybe 1% of the year", and only "in some climates" (21 June 2026)."

Also fix the evidence fold (line 354), which reads chillers "maybe 1% of the year": keep, but add "(Ali Heydari)".

### E2. Google's air-cooled footnote covers eight sites, not seven (line 206)

Current: "But Mesa carries no "air-cooled facility" footnote in the 2026 table, unlike Phoenix and six others, and it withdrew 19.4 million gallons."

Source: Google 2026 Environmental Report, p.97 table and endnotes 226 to 235. Endnote 226 ("Air-cooled facility.") applies to Dublin, Montreal, Pflugerville, Phoenix, San Bernardo, Storey County, Sydney and Wilmer: Phoenix and seven others.

Replace with: "But Mesa carries no "air-cooled facility" footnote in the 2026 table, unlike Phoenix and seven others, and it withdrew 19.4 million gallons."

### E3. Jane Street's chillers: the podcast is about return water temperature, not outdoor air, and names no site (line 102)

Current: "The site's air-cooled chillers blow outside air over coils, and above a certain outdoor temperature they lose capacity."

Source: Signals and Threads, episode 24, 25 July 2025, https://signalsandthreads.com/the-thermodynamics-of-trading/ . Pontecorvo, who "runs the physical engineering team", says roof chillers "blow air over coil", and that chillers "lose their heat transfer abilities above a certain temperature". In context (about 12:07 to 12:51) that temperature is the warm water returning from the room units, not the outdoor air. He names no site, so the chillers cannot be tied to the Texas hall in the write-up.

Replace with: "On a 2025 podcast he described Jane Street's roof chillers, which blow outside air over coils, and said they lose heat transfer ability once the returning water gets too warm."

### E4. "Built for air ... pipes, pump units and new plant added" is not in Jane Street's write-up (line 100)

Current: "The hall was built for air and had pipes, pump units and new plant added."

Source: Jane Street, "A look inside our newest data center", undated (© 2026), https://www.janestreet.com/culture/street-view/a-look-inside-our-newest-data-center/ . It says only "4,032 GPUs across 56 racks, retrofitted for liquid cooling". It mentions no air design, pipes, pumps, CDUs, chillers or plant.

Replace with: "The write-up gives no detail of the refit, but "retrofitted" means the liquid loop was added to a hall already standing."

### E5. Fortum quote is not verbatim (line 302)

Current: "but Microsoft's waste heat enters only "in phases in 2027"."

Source: Fortum release, 6 May 2026, https://www.fortum.com/en/media/2026/05/fortum-has-started-heat-production-two-large-data-centre-sites-finland . The heat recovery is "to be integrated in phases starting next year"; the phrase "in phases in 2027" does not appear. The release also says "approximately 40 per cent of the total yearly 2 terawatt hour district heat demand" and "the 250,000 heat users".

Replace with: "but Microsoft's waste heat is "to be integrated in phases starting next year", that is from 2027."

### E6. arXiv quote is not verbatim (line 250)

Current: "Their paper also notes that operators short of water may fall back on "less efficient dry cooling", which can "further stress the power grid during summer peaks"."

Source: Han, Li, Wierman and Ren, "Small Bottle, Big Pipe", arXiv 2603.02705 (v1 3 March, v2 18 March 2026), https://arxiv.org/abs/2603.02705 . The abstract reads: "can force operators to rely on less efficient dry cooling, further stressing the power grid during summer peaks."

Replace with: "Their paper adds that water limits can push operators onto "less efficient dry cooling, further stressing the power grid during summer peaks"."

### E7. Johnson Controls CFO quote is not verbatim (line 278)

Current: "Johnson Controls' finance chief said customers "continue to face power and some electrical infrastructure limitation" affecting delivery timing (27 October 2026)."

Source: Q4 fiscal 2026 call, 27 October 2026, transcript at https://www.webull.com/news/15821044567232512 . Marc Vandiepenbeeck: "But in some case, we see customer that continues to face power and some electrical infrastructure limitation." He said this governs when customers take delivery, and that "the primary constraint is really not demand".

Replace with: "Johnson Controls' finance chief said some customers face "power and some electrical infrastructure limitation", which sets when they take delivery (27 October 2026)."

### E8. Johnson Controls has bought its cold plate maker, not just agreed to (line 288)

Current: "Johnson Controls added CDUs and agreed to buy a cold plate maker."

Source: same call, 27 October 2026: Weidemanis, "we've increased our offering, added CDUs, acquired a cold plate company".

Replace with: "Johnson Controls added CDUs and, by its chief executive's account in October 2026, bought a cold plate maker."

### E9. LBNL's dry liquid hall is not "a dry cooler alone" (line 150)

Current: "With a dry cooler alone, PUE is about 1.10 and water is zero."

Source: LBNL, 2024 United States Data Center Energy Usage Report, December 2024, Figure 4.4 (printed p.46), https://escholarship.org/content/qt32d6m0d1/qt32d6m0d1.pdf . The case is labelled "IT Liquid cooling: dry cooler (air-cooled chiller)": a dry cooler backed by an air-cooled chiller. The difference matters to the piece's own worst-afternoon argument, because the 1.10 already includes the chiller's hot hours averaged over a year. The evidence-fold table (line 367) and the lbnl-chart row label "Dry cooler" have the same problem.

Replace with: "With a dry cooler backed by an air-cooled chiller, PUE is about 1.10 and water is zero."

Table row (line 367): "| Liquid: dry cooler with air-cooled chiller | Large | 1.10 | 0 |". In charts.py, change the label 'Dry cooler' to 'Dry cooler, chiller backup' for the liquid row, matching the air row.

### E10. The 15% worst-hour bound compares against an unexplained 1.15 (line 246 and line 387)

Current: "On a fixed plug, computing scales with one over that peak, so the hall fits about 15% fewer racks than at 1.15."

Problem: the paragraph sets the hall's yearly PUE at about 1.1, then compares the 1.35 peak with 1.15, a number the piece never introduces. Against 1.1 the arithmetic gives 1.1 / 1.35 = 0.81, about 19% fewer racks; against 1.15 it gives 0.85, about 15% fewer. The reader cannot tell what 1.15 stands for.

Replace with: "On a fixed plug, computing scales with one over that peak, so the hall fits about 15% fewer racks than one whose worst hour stays near 1.15, my assumption for a wet hall."

Evidence fold (line 387), replace with: "The 15% bound is my arithmetic: PUE 1.1 plus 0.25 for a chiller at a performance of 4 is about 1.35; a wet hall's worst hour is assumed at about 1.15; 1.15 over 1.35 is about 0.85."

### E11. "Largest product line" is Johnson Controls' data centre portfolio, not the company (line 230)

Current: "Johnson Controls, whose York brand makes chillers, said chillers are still its largest product line."

Source: same call, 27 October 2026. Asked whether data centre orders were "still largely a chiller story", Weidemanis said "chillers is the largest part of our portfolio still", speaking of the data centre area.

Replace with: "Johnson Controls, whose York brand makes chillers, said chillers are still the largest part of its data centre range."

### E12. The claims-fold note calls earlier evidence "later" (line 345)

Current: "Where later evidence bears on it: Mesa consumed 9.7 million gallons in 2025 but carries no air-cooled footnote; ... Google's policy of 3 June 2026 ... Project Blue was redesigned to closed-loop air cooling and its power supply approved, which supports the third limb."

Problem: the claim in claims.ts is dated 30 October 2026. Every item in the note predates it: Google's 2026 Environmental Report (mid 2026), Google's blog of 3 June 2026, and Project Blue's redesign and power approval (December 2025). None is later evidence. The facts themselves check out (Mesa row and missing footnote: Google 2026 report p.97; policy wording: Google blog, 3 June 2026). Project Blue's power approval is press-reported (see F16).

Replace with: "Where the evidence stands: Mesa consumed 9.7 million gallons in 2025 but carries no air-cooled footnote, and Waltham Cross and Canelones are not yet listed, so the first limb cannot yet be tested there. Google's policy of 3 June 2026 allows "air cooling or recycled water" at high-risk sources, a path the second limb may not catch. Project Blue was redesigned to closed-loop air cooling, and its power supply was approved, as reported; that fits the third limb but does not test it."

---

## Flags

### F1. Nvidia's "30% more GPUs" omits the same post's 10% (line 92)

Current: "It claims 45 degree cooling "unlocks up to 30% more GPUs in the same power budget" (16 March 2026)."

Source: Nvidia Technical Blog, "NVIDIA Vera Rubin POD", 16 March 2026, https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/ . The quote is verbatim, but the post's own summary says 45°C cooling "unlocks up to 10% additional NVL72 racks in the same power budget". Quoting only the larger figure overstates the vendor's case.

Replace with: "The same post claims 45 degree cooling unlocks "up to 10% additional NVL72 racks", and elsewhere "up to 30% more GPUs", in the same power budget (16 March 2026)."

### F2. "The generation now shipping" is not confirmed at source (line 82)

Current: "Its racks for Vera Rubin, the generation now shipping, are ..."

Source: Nvidia, 16 March 2026: "NVIDIA Vera Rubin NVL72 is in full production, on track to ship in the second half of 2026." I found press reports of samples and planned autumn shipments, but no Nvidia statement that systems have shipped.

Replace with: "Its racks for Vera Rubin, which Nvidia said in March would ship in the second half of 2026, are ..."

### F3. "Asked for 45 degree coolant. Better cold plates won." (line 90)

Nvidia says its racks are "designed to operate with" 45°C inlet water: they accept it, they do not require it. "Better cold plates won" is inference; Nvidia credits "tightening the die-to-water thermal path" (25 March 2026).

Replace with: "Five years later the hottest rack on the market was designed to run on 45 degree coolant. Nvidia credits a tighter path from die to water."

### F4. ASHRAE wording stretched (lines 50 and 56)

Line 56: "which it already called hard". The ASHRAE sentence (2021 white paper, https://www.ashrae.org/File%20Library/Technical%20Resources/Bookstore/Emergence-and-Expansion-of-Liquid-Cooling-in-Mainstream-Data-Centers_WP.pdf ) only says airflow for high rack powers "should be carefully analyzed". Replace with: "The nearest anchor is ASHRAE's 40 to 50 kW rack at 5,000 cfm, more than two of the best floor tiles."

Line 50: "against under 2% a decade earlier". ASHRAE says fan power fell "to below 2% in many cases" during "the multicore period", with no decade stated. Replace with: "ASHRAE found fans in dense servers using 10 to 20% of server power, against under 2% in many servers of the multicore era."

The same sentence also runs on "and fan power rises roughly with the cube of fan speed", which reads as ASHRAE's finding; it is textbook physics. Consider a separate sentence: "Fan power rises roughly with the cube of fan speed, so pushing air harder gets expensive fast."

### F5. "In most climates that is nearly every hour of the year" (line 134; ladder aria text)

Nvidia's own wording is narrower: 45°C lets data centres "in many climates" use dry coolers (16 March 2026), and chillers are needed "in some climates" (21 June 2026). Hot sites such as Phoenix spend many hours above 36°C. The 5 to 8 degree approach is also the piece's own assumption.

Replace with: "In many climates that is nearly every hour of the year, though not in the hottest deserts."

### F6. "Its chilled water typically ran at around 18 degrees" (line 132)

Unsourced. Legacy chilled water plants commonly ran 7 to 12°C; 18°C is a modern elevated setpoint, which flatters the old hall. The ladder caption labels it an assumption, but the text says "typically".

Replace with: "Take an old air-cooled hall with chilled water at about 18 degrees, already warm by older standards."

### F7. The 15% bound uses a chiller efficiency measured for much colder water (line 246)

The COP of about 4 comes from the Vertiv Liebert AFC datasheet at 35°C air making 20°C water (26/20°C). Making 41°C water on a 45°C afternoon is a far smaller temperature lift, so the chiller would likely run at a higher COP and add less than 0.25. The piece already calls it a rough bound; say which way it leans.

Add after the bound: "That likely overstates the penalty, since a chiller making 41 degree water works across a smaller lift than the datasheet's."

### F8. Google's "about 10%" sits uneasily beside LBNL's near-zero (line 204)

Current: "That sentence prices the trade: about a tenth more energy to save the water."

Google's figure is "in many places" and covers its fleet, much of it air-cooled IT; LBNL's medians show almost no penalty for a liquid hall. The piece states both without reconciling them, and a reader will notice.

Replace with: "That sentence prices the trade across Google's fleet: about a tenth more energy to save the water, more than the lab finds for a liquid hall."

### F9. Fairwater's "water-cooled chiller plant" contradicts the piece's own definition (line 214, and line 232)

The piece defines a water-cooled chiller as one that "throws it into a tower, which evaporates water" (line 122). Guthrie (18 September 2025, https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/ ) calls Fairwater's plant "the second largest water-cooled chiller plant on the planet" while describing a closed loop and "172 20-foot fans". Microsoft appears to mean chillers that cool the water loop, rejecting heat through fans. A reader will see a zero-water campus built on the very machine the piece says evaporates water.

Add after the quote: "Microsoft means chillers that cool the loop's water; the heat leaves through those fans, not a tower."

### F10. The claim in paragraph three is stated more broadly than the evidence (line 18)

Current: "Where an operator judges water scarce, it cools with air, and no powered AI campus has yet been cancelled over water rather than redesigned."

Only Google publishes source-by-source risk judgements, its 2026 policy allows "air cooling or recycled water", and Mesa is not footnoted as air-cooled. The second half is a finding of absence.

Replace with: "Where an operator judges water scarce, it cools with air or recycled water, and I have found no powered AI campus cancelled over water rather than redesigned."

### F11. ENERGY STAR is linked, not named (line 136 and line 354)

The 21 June 2026 post cites "industry estimates" and links to energystar.gov; it does not name ENERGY STAR in the text.

Replace with: "The same post, linking to ENERGY STAR, says raising chiller plant temperatures by one degree "can cut cooling energy costs by about 4%"."

### F12. Trane's 12 to 18 months is for data centre purchase orders generally (line 280)

Current: "Trane, another chiller maker, said firm chiller orders arrive 12 to 18 months before delivery (5 May 2026)."

Source: Trane, Oppenheimer conference transcript, 5 May 2026 (Trane IR PDF). Donny Simmons: "in our backlog, it's firm purchase orders. And those purchase orders come typically 12 to 18 months in advance of when the delivery takes place", in a discussion of data centres and the Stellar plant business.

Replace with: "Trane, another chiller maker, said its firm data centre orders typically arrive 12 to 18 months before delivery (5 May 2026)."

### F13. Munters' 49% chiller share is not in Munters' own release (line 232)

The 23 October 2026 release (https://mfn.se/cis/a/munters-group/munters-group-ab-significant-order-growth-as-operational-improvements-progress-1524bc51 ) has no chiller share. The figure comes from a summary of the slides. The piece labels it "as summarised", which is honest; either open the slides or cut the sentence.

### F14. SPX's data centre capacity is not tied to towers in its release (line 292)

Current: "SPX, which makes Marley cooling towers, is building capacity for about $1.1 billion of yearly data centre revenue."

The 29 October 2026 release says "cooling equipment"; it does not split towers from other products.

Replace with: "SPX, whose brands include Marley cooling towers, is building capacity for about $1.1 billion of yearly data centre revenue, without saying which products."

### F15. "Quilicura is water-cooled" is an inference (line 262; sites-chart label)

Google's table gives 143.0 million gallons consumed and no air-cooled footnote; it does not say "water-cooled". The inference is sound, but label it.

Replace with: "Meanwhile Google's existing Santiago campus at Quilicura consumed 143.0 million gallons in 2025, so it evaporates water."

### F16. Project Blue: press-sourced, and not a strict test of the third limb (lines 260, 324, 345)

The power approval (Arizona Corporation Commission, 3 December 2025) and the county agreement are from press; the ACC order was not opened. The third limb concerns a campus "with its power already secured"; Project Blue's power was approved after the water fight and the redesign, so it fits the limb but does not test it. Amazon also left, which a sceptic could call a cancellation for the hyperscaler.

Line 324, replace with: "Project Blue is the live case, and so far it fits my claim: redesigned to closed-loop air, with power approved, as reported."

### F17. "Three positions gain" reads like portfolio language (line 310)

Replace with: "If the claim is right, three parts of the chain gain."

### F18. Southern Nevada's rule is press-only where it reappears (line 326)

Line 264 labels it "as reported"; line 326 states it as fact. Replace with: "Google publishes no rating of its source, and Southern Nevada has stopped permitting new evaporative cooling, as reported."

### F19. Vertiv's quotes come from a third-party transcript (lines 230, 278, 290)

Quotes check out against the Singju Post transcript of the 28 October 2026 call (https://singjupost.com/?p=64906 ), which is not Vertiv's own document. The "pacing items" Albertazzi named were "power availability, permitting, general sentiment, and construction site skilled labor availability". Consider: "Vertiv named power, permitting, sentiment and skilled labour as the pacing items."

### F20. LBNL comparisons pick particular rows (lines 154, 184; whole-chart)

The "air hall with a tower" is LBNL's midsize water-cooled chiller without an economiser (1.52, 2.9 litres). The same figure shows a midsize waterside economiser at about 1.38 and 2.5 litres, which would narrow the gap. The whole-water comparison also sets a midsize air hall against a large liquid hall, so size and cooling type move together. Add one clause: "The comparison sets a midsize air hall against a large liquid one, so size accounts for part of the gap."

### F21. "The lab projects ... between 0.45 and 0.48" needs its year (line 330)

LBNL (printed pp.47 to 48) projects the range by 2028. Replace with: "The lab projects the national average rising from just over 0.36 litres per kWh in 2023 to between 0.45 and 0.48 by 2028, partly from "the increased water consumption of liquid-cooled systems"."

### F22. Google Deschutes: attribution is right, but "its fleet" needs one word (line 68)

Google (30 April 2025, https://cloud.google.com/blog/topics/systems/enabling-1-mw-it-racks-and-liquid-cooling-at-ocp-emea-summit ): "fleet-wide CDU availability of ~99.999% since 2020". The piece is accurate; consider "fleet-wide CDU availability" so it is not read as data centre uptime, since the same post separately cites "about 99.999%" uptime for liquid-cooled TPU pods.

---

## Verified

- Nvidia DGX GB200 User Guide: "The rack power consumption is approximately 120kW"; compute trays liquid-cooled; networking and storage air-cooled. 120 / 1.5 kW is 80 hairdryers.
- Physics arithmetic: water against air about 4,160 / 1.17, about 3,560 times; 1 kW at a 15 degree rise is about 0.057 m³/s, about 120 cfm; 120 kW is about 14,500 cfm, 7.6 tiles of 1,900 cfm; 142 kW about 9 tiles; 7.5 kW about half a tile; 5,000 / 1,900 is 2.6. Evaporation 3,600 / 2,430 is 1.48 litres per kWh; blowdown at two to four cycles is a third to one times evaporation. One per cent of a year is 87.6 hours.
- ASHRAE 2021 white paper, verbatim: "up to 5000 cfm", "1900 cfm", "10% to 20%", UPS capacity cut "by 8%", W17 to W+ renaming, "only capable of W32 (W3)", "down into the W27 (W2) range", W45 "will become increasingly difficult to use as the heat flux at the socket increases".
- Guthrie, 18 September 2025: "Traditional air cooling can't handle the density of modern AI hardware"; over 90% closed loop; "second largest water-cooled chiller plant on the planet"; 172 20-foot fans.
- Nvidia 16 March 2026: "designed to operate with 45°C (113°F) warm-water inlet temperatures"; 41°C to CDUs; fanless compute and switch trays. 21 June 2026: "75% water and 25% propylene glycol", "exits at roughly 55 degrees", hot tubs "38 to 40", "about 4%", 2.6 million gallons per MW per year. 25 March 2026: Blackwell "about 20% of capacity air-cooled"; Rubin "100% liquid cooling"; "diverting a larger share ...". 24 August 2026: "sized for worst-case scenarios"; worst-hour quote; 20 MW of 100 MW to facility overhead.
- Google Deschutes ~99.999% since 2020 (30 April 2025). Carrier corrected transcript, 29 October 2026: "effectively a CDU is a mini-chiller" (Gitlin), orders over $3 billion "an increase of nearly 350%", "great demand for our new 2 megawatt and 3 megawatt air-cooled chillers", "just not enough", "teething pains", more than $550 million Q3 data centre sales, 1 to 5 MW CDUs.
- 3M FY2025 10-K: "3M completed its exit of PFAS manufacturing at the end of 2025."
- LBNL (December 2024): 18 cases, nine cooling systems, 965 weather stations, over 1 million simulations, W45 for liquid; "less chiller run hours and less adiabatic assist" (p.42); "rarely the case" (p.44); "does not imply", "While air-cooled chillers use no water, they use more energy" (p.45); 66 billion litres direct; "nearly 800 billion liters" on 176 TWh; 4.52 L/kWh; hydro reservoirs in scope; power purchase agreements ignored; 0.45 to 0.48. Figure 4.4 medians as read in the piece (1.52 and 2.9; 1.83 and near 0; about 1.6; 1.13 and 2.0; 1.10 and about 0.13; 1.10 and 0) match my reading of the chart.
- Arithmetic: 800 / 66 is 12.1; 800 / 176 is 4.55; whole water 2.9 + 1.52 × 4.52 = 9.8; 1.83 × 4.52 = 8.3; 2.0 + 1.13 × 4.52 = 7.1; 1.10 × 4.52 = 5.0; extra 0.31 × 4.52 = 1.4. Charts.py computes the same values.
- Google 2026 report: data centres withdrew 13,562, consumed 10,523 million gallons (about 39.8 billion litres); potable 10,949, 80.7%; consumption up 34%; "requires less energy than air-cooling technologies"; Council Bluffs 1,346.0, The Dalles 469.0, Henderson 239.4, Quilicura 143.0, Mesa 9.7 consumed and 19.4 withdrawn; The Dalles assessed not high risk in 2022 (endnote 79); 13% high risk; 78% replenished. 9.7 / 469 is about one forty-eighth. Google 2025 report: Waltham Cross "present a high risk of water depletion and scarcity", "decided to utilize air cooling technology", "a similar approach" at Mesa and Canelones "under development". Google blog, 3 June 2026: "If a water source is at high risk, we choose air cooling or recycled water"; "approximately 10%".
- Microsoft blog, 9 December 2024: August 2024, "nominal increase in our annual energy usage", "will increase our power usage effectiveness (PUE)", consumption-based WUE, Phoenix and Mt. Pleasant pilots in 2026, online late 2027. Blog, 24 June 2026: 0.27 L/kWh; about 90% of 2025 owned fleet "low- to zero-water"; 85°F; Virginia 10%; Phoenix up to 40%. 2026 Data Fact Sheet: FY25 withdrawals 13,266 ML, 6,659 ML (50%) in water-stressed areas; Phoenix 981 ML on 954,206 MWh, 1.03 L/kWh.
- AWS 2025 Sustainability Summary: WUE 0.25 (2021) to 0.12 (2025), withdrawal basis; 22% high or extremely high stress; direct evaporative cooling "less than 10% of the year"; no water for cooling in some most-stressed regions.
- Meta 2025 Environmental Data Index: WUE 0.19 (2024) on withdrawal; 1,704 of 5,637 ML (30%) in high-stress areas; embedded water 72,207 ML against 3,123 ML consumed (23 times); 5,075 ML for contracted renewables (1.6 times). Meta, 27 August 2026: majority of newest AI halls closed-loop liquid; "uses less water annually than a couple of full-service restaurants".
- Makers: Eaton Q3 2026 release, Boyd bought 12 March 2026 for $9.55 billion net, 31% contribution to Electrical Global's 58% growth on $2.7 billion, so Boyd about $535 million. Ecolab 10-Q: CoolIT completed 2 July 2026, $4,627 million net; CDUs and cold plates. Modine 8-K: Data Centers $439.7 million against $225.0 million, up 95%, quarter to 30 September 2026; "to secure critical components". SPX: "approximately $1.1 billion of annual data center revenue capacity". Munters release: "component shortages and ramp-up inefficiencies"; "constraints remain industry-wide". Vertiv (third-party transcript): "on track to doubling chiller production capacity by year-end"; "the mix is definitely moving towards liquid cooling"; "It doesn't mean that air cooling is going away". Johnson Controls: "perhaps one or two fewer chillers will be needed".
- UC Riverside release, 12 March 2026: daily evaporative demand "can spike six to 10 times higher than average usage".
- Chile's Second Environmental Court, ruling of 26 February 2024 (R-271-2020, joined with R-270-2020), partly annulling Cerrillos approval over the Santiago Central aquifer and climate change.
- Ypsilanti: YCUA Resolution 26-08, 22 April 2026, minimum 12-month moratorium on water and sewer for data centres (press and resolution number).
- Loudoun County: "On an average day, data centers in Loudoun account for 9% of total potable water use."
- Fortum, 6 May 2026: heat plants at Kolabacken and Hepokorpi started; about 40 per cent of 2 TWh demand; 250,000 heat users.
- Uptime survey via The Register (3 August 2025): average about 7.5 kW excluding outliers.
- Archived piece titles and dates in the claims fold match research-build/archive/pieces/ (21 August 2026; 25 September 2026).
