# Sidecar: data-centres-in-space (new deep piece, "Two tracks for new work", track 1)

Approved by Tommy on 2 Nov 2026 after the scout (`gap-space.notes.md`). Drafted 2 Nov 2026 to STORY-RULES.md on the model of `hong-kong-has-the-plug`. Piece: `research-build/deep-pieces/data-centres-in-space.md` (draft: true, date is a placeholder), outside `src/content/journal/` so the loader does not read it. Nothing committed, published or scheduled. Only these two files written.

Map change from Tommy (2 Nov 2026, via the coordinator): the piece gets its own new last layer, `orbit`, not the `cooling` layer. The main session adds the layer to stack.ts and draws its stop in Descent.astro. The piece text does not mention the cooling layer by name; it links to `heat-and-water` as the ground-side sibling.

## What changed from the scout, and why

- **Unverified item resolved.** The scout could not read SpaceX's revised prospectus pages. I read the S-1/A No. 2 (3 Jun 2026) and the final 424B4 (12 Jun 2026) in full text. Both answer the SEC's comment 26 with: "The precise solar collection area, total system mass per satellite, and on-orbit assembly requirements associated with this goal continue to be refined as part of our ongoing engineering efforts." So no mass figure is disclosed. This became the climax beat.
- **The SEC letter is stronger than the scout said.** Comment 26 (24 Apr 2026) also asks for "power-to-mass ratios underlying the 100-gigawatt annual deployment goal". Used.
- **Prospectus wording of the target.** "Deployment of 100 gigawatts per year via satellites carrying over 100 kilowatts of compute power per metric ton will require thousands of launches per year and the transport of approximately one million metric tons to orbit annually" (424B4 p. 153, and S-1/A No. 2). Also "targeted to generate approximately 100 kW of compute power per ton, which initially will require approximately five times the solar array output compared to V3 satellite designs". The claim uses "per metric ton" to match.
- **Interview transcript date.** EDGAR shows the FWP (accession 0001628280-26-041761) filed and accepted on 9 Jun 2026, not 8 Jun. The piece says 9 June.
- **Suncatcher paper date.** arXiv 2511.19468 v1 is dated 22 Nov 2025; 4 Nov 2025 is the Google blog announcement, which I did not re-open. The piece cites the paper as 22 November 2025.
- **Speaker attribution.** The 150/120 kW, 250 W/m² and 1,400 W/m² figures are Elon Musk's words in the transcript (Ian Dahl gave 150 kW peak and "about 120 kilowatts of average compute"). The piece attributes them to Musk.
- **Slide numbers dropped.** The "100KW Compute power per metric ton" text sits on the roadshow page titled "More milestones ahead"; I could not confirm the scout's slide numbers (44, 63, 64) from the extracted text, so the piece cites the prospectus wording instead.
- **The 10-Q bears, by absence.** SpaceX's 10-Q to 30 Sep 2026 (filed 22 Oct 2026) contains no mention of orbital compute, AI compute satellites or radiators. Used once.
- **Physics framing.** The 1,400 W/m² to about 67°C conversion is mine (two faces, emissivity 0.92, shade), labelled so. The heat-and-water link is stated as the same lever run the other way (warm loop drops the water on the ground; warm coolant shrinks the radiator in orbit), with a link, not a repeat.
- **Forward beat (the jolt).** SpaceX's own risk factor ("the useful life of our satellites is inherently shorter than that of the information technology systems and infrastructure they host") reverses the equipment-queue finding that ground gear outlives three or four chip generations. With Google's five-year Starlink life and its ~2035 projection for <$200/kg, a satellite flown in 2028 wears out before launch is cheap. Labelled "my framing"; SpaceX gives no AI satellite life.

## Shape and counts

- Title: "Data centres in orbit: the plug is free and the heat is the bill" (13 words, names the subject).
- Top layer: 537 words (checker count), 9 figures, 2 money figures in separate paragraphs. Analogy about 67 words (vacuum flask and fin; returns in the investor layer's closing paragraph).
- Investor layer: 1,843 words before the exposure map (storyline to "What would prove me wrong" about 1,695). Exposure map 131 words, three groups plus the against block.
- Average sentence 16.8 words. No em or en dashes.
- Headings in order: The plug in orbit is the sun, and it has no queue / Heat leaves only as light, so the radiator's temperature sets its size / Every kilogram is a launch bill, so the measure is kilowatts per tonne / At today's launch price, the free plug costs more than ground power / The regulator asked for the mass, and the prospectus does not give it (climax) / What could make orbit cheaper than I think (counter) / In orbit the building wears out before the chip (forward, anchor `data-centres-in-space`) / What would prove me wrong / Research notes.
- Charts (4), coordinates computed by script:
  1. "A radiator sheds heat with the fourth power of its temperature" (curve 2εσT⁴, Starcloud 633 at 20°C, SpaceX 1,400 at ~67°C, ISS ~147 W/m², W45 marker).
  2. "At today's launch price, power in orbit costs several times a ground hall's power bill" (Google Table 1: $14,700 and $810 per kW-year against $570 to $3,000).
  3. "At the space station's weight, the radiator alone uses SpaceX's whole budget" (kg per kW: target 10; radiator 10.0 at 1,400; Starlink V2 mini 20.5; radiator 22.1 at 633; ISS wings 96 off scale). Climax.
  4. "A compute satellite launched in 2028 wears out before launch reaches $200 a kilogram" (prototypes 2027, first flights 2028, five-year life to ~2033, claim date, ~2035).

## Checker output

`python3 brand/check-piece.py research-build/deep-pieces/data-centres-in-space.md`:

```
  FAIL  data-centres-in-space: cover /covers/data-centres-in-space.svg does not exist in public/covers/
1 piece(s): 1 failure(s), 0 warning(s)
```

Expected: the cover is not drawn (brief: new files in research-build only). Map and claims checks are skipped while `draft: true`; with `draft: false` they will fail until the stack.ts and claims.ts entries below are merged. I ran the checker's `deep_checks` against the claims.ts entry below: the claim is quoted word for word, no failures.

## New claims.ts entry

```ts
  {
    id: 'data-centres-in-space',
    date: '2026-11-02',
    home: 'data-centres-in-space',
    claim: 'In orbit the power is nearly free and the heat is the bill: by 31 December 2028 no operator will report an AI compute satellite in service at SpaceX\'s own target of 100 kilowatts of compute power per metric ton launched, and no launch provider will publish a price to low Earth orbit at or below Google\'s $200 per kilogram threshold.',
    breaksIf: 'By 31 December 2028, SpaceX, Starcloud, Google or any other operator discloses in a filing, release or regulator\'s record an orbital AI compute satellite in service at 100 kilowatts or more of compute power per metric ton of launched mass, or a launch provider publishes a list or contract price to low Earth orbit of $200 per kilogram or less.',
    watch: ['SpaceX\'s 10-Qs and 10-K for AI compute satellite mass, power and first flights ("as early as 2028"; mass per satellite "continue[s] to be refined", 12 June 2026)', 'Google and Planet\'s two Suncatcher prototypes, targeting launch in 2027 (Planet 8-K, 10 December 2025)', 'Starcloud\'s releases and FCC filings on satellite mass, power and radiators', 'FCC action on SpaceX\'s application SAT-LOA-20260108-00016 (up to one million satellites) and Starcloud\'s (up to 88,000)', 'Any published launch price per kilogram to low Earth orbit, Falcon 9 or Starship (Google\'s current estimate $3,600/kg)', 'Measured radiator areal density or heat flux from any compute satellite in orbit (ISS heritage 14 kg per m²)'],
  },
```

The claim keeps the scout's wording, changing only "100 kW of compute power per tonne launched" to "100 kilowatts of compute power per metric ton launched", the prospectus's own unit. `home` equals `id`, so it can be omitted if the file's convention prefers; `date` is the day the claim was approved and drafted, as briefed.

Why it is a real test: SpaceX's own date for first flights is "as early as 2028", and its CFO's first-generation figure (5 MW a launch) is half the target at 100 tonnes a launch. A prototype or a first satellite could hit 100 kW per tonne by end-2028 if radiators prove light, and Starcloud or SpaceX could publish a price sheet. It can fail either way.

## stack.ts: new last layer (Tommy, 2 Nov 2026; the main session adds it and draws its Descent stop)

```ts
  {
    id: 'orbit',
    name: 'Data centres in orbit',
    kind: 'energy',
    what: 'Satellites in near-constant sunlight run AI chips on solar power and shed the heat by radiating it into cold space.',
    constraint: 'Every kilogram of radiator and solar panel must be launched, so the weight of each kilowatt decides the cost.',
    pieces: ['data-centres-in-space'],
  },
```

Separate flag, not this piece's edit: the `cooling` layer's `constraint` still reads "Air stops working somewhere between 30 and 50 kilowatts per rack", the band heat-and-water retired.

## Glossary (src/pages/glossary.astro)

Under the cooling heading (or a new orbit heading if the main session adds one):
- Dawn-dusk sun-synchronous orbit: a low orbit that follows the line between day and night, so a satellite's solar panels face the sun almost all the time. Every orbital compute design files for it.
- Radiator (in space): a panel that sheds heat by glowing it into cold space, the only way heat leaves a satellite. The heat it sheds rises with its absolute temperature to the fourth power.
- Stefan-Boltzmann law: the physical law that heat radiated by a surface rises with its absolute temperature to the fourth power, so a slightly hotter radiator can be much smaller.
- Emissivity: how well a surface radiates heat compared with a perfect black surface, from 0 to 1. Starcloud's sums use 0.92.
- Areal density: mass per square metre of a panel. The space station's radiators are about 14 kg per m².
- Launched power price: Google's measure of the launch cost of each kilowatt of satellite power, spread over the satellite's life, in dollars per kW per year.
- Check for duplicates at merge: PUE and ASHRAE W45 should already exist from heat-and-water.

## numbers.ts (physical only)

```ts
  { layer: 'orbit', value: '100 kW per tonne', what: 'SpaceX\'s target of compute power per metric ton launched for its AI compute satellites: 100 GW a year would need about one million tonnes to orbit annually. Mass per satellite is not disclosed.', piece: 'data-centres-in-space', asOf: '12 June 2026' },
  { layer: 'orbit', value: '633 vs 1,400 W/m²', what: 'Heat a two-sided radiator sheds per square metre: Starcloud\'s figure at 20°C, against SpaceX\'s assumption, which implies a panel near 67°C. Heat shed rises with temperature to the fourth power.', piece: 'data-centres-in-space', asOf: 'June 2026' },
  { layer: 'orbit', value: '14 kg/m²', what: 'Areal density of the space station\'s radiators. At SpaceX\'s 1,400 W/m², a radiator this heavy alone is 10 kg per kW, the whole of SpaceX\'s satellite budget.', piece: 'data-centres-in-space', asOf: '2022' },
```

(All three are physical. The launch price per kilogram stays out of numbers.ts as a money figure.)

## LinkedIn post (§9; opens on the sharpest number)

```
SpaceX wants AI satellites that weigh 10 kilograms for every kilowatt of computing, and a radiator as heavy as the space station's would use all of it on its own.

In the right orbit the sun almost never sets and there is no queue for the grid, so the power is nearly free. But in a vacuum heat leaves only by glowing off a radiator, and every kilogram has to be launched. The SEC asked SpaceX for the total mass of its system; the prospectus said it is still being refined.

The piece covers the radiator physics, the launch price that would make the sums work, and why a satellite flown in 2028 wears out before launch gets cheap.

https://thephysicallayer.fyi/journal/data-centres-in-space/

#DataCentres #AIInfrastructure #Space
```

## Cover brief (not drawn)

`/covers/data-centres-in-space.svg`, viewBox 800 by 600, background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py. Near-black gradient with a thin curved Earth limb along the bottom edge, half lit. Centre: one satellite drawn bold. A long blue-edged solar wing to the left (sunlit, with an amber sun disc at the far left edge), a small blue rack box in the middle with chip squares, and a large black radiator panel extending to the right into shadow, glowing amber with heat lines radiating outward. A small weight tag (a kettlebell outline) hangs from the radiator. Caption in letter-spaced grey: "DATA CENTRES IN ORBIT: THE HEAT IS THE BILL". One idea: free sunlight in, heat glowing out, weight attached.

## Sources, every one with date (opened by me on 2 Nov 2026 unless marked)

- Google, "Towards a future space-based, highly scalable AI infrastructure system design" (Suncatcher), arXiv 2511.19468 v1, 22 Nov 2025: https://arxiv.org/abs/2511.19468 ; PDF https://arxiv.org/pdf/2511.19468 (dawn-dusk orbit, cooling sentence, Table 1, $3,600/kg, $200/kg "often cited", ~2035, ~180 Starship launches a year, $570 to $3,000/kW/y, 575 kg and 28 kW, five-year life, radiation results). Google blog of 4 Nov 2025 NOT re-opened.
- SpaceX roadshow FWP, filed 4 Jun 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026040610/spacexfwp.htm ("100KW Compute power per metric ton", "100 Metric tons per launch over time", "Larger radiator", radiative cooling and cost per kilogram lines, risk factors on solar and nuclear, repair, useful life, full Starship reusability, "as early as 2028").
- SpaceX interview transcripts FWP, filed 9 Jun 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026041761/fwp_cfointerview.htm (Johnsen: five times energy per cell, 5 MW a launch, 200 launches a gigawatt, "In 2028, we'll start flying if we stay on target"; Musk: 150 kW peak, 120 kW sustained, 250 and 1,400 W/m², double-sided, edge-on, Rubin or GB300 reference design; Dahl: radiators about the size of the V3 solar arrays).
- SpaceX S-1/A No. 2, 3 Jun 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm
- SpaceX final prospectus 424B4, 12 Jun 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm (pp. 152 to 154: radiation-only thermal control; 100 kW per metric ton; one million tonnes; mass "continue to be refined"; "substantially larger radiators"; five times V3 solar output).
- SEC staff comment letter, 24 Apr 2026: https://www.sec.gov/Archives/edgar/data/1181412/000000000026004247/filename2.txt (comments 26 and 31).
- SEC staff comment letter, 19 May 2026: https://www.sec.gov/Archives/edgar/data/1181412/000000000026005119/filename2.txt (comment 3).
- SpaceX 10-Q, quarter to 30 Sep 2026, filed 22 Oct 2026: https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm (no orbital compute mention).
- EDGAR full-text search (2 Nov 2026) for "total system mass" and "power-to-mass" in CIK 1181412, which located the filings above.
- FCC public notice DA 26-113, released 4 Feb 2026: https://docs.fcc.gov/public/attachments/DA-26-113A1.txt (up to one million satellites, 500 to 2,000 km, 30 degree and sun-synchronous, Ka-band TT&C "on a non-interference, unprotected basis").
- Starcloud FCC application narrative, 4 Feb 2026: https://api-prod.fcc.gov/icfs-attachment/exp/api/v1/5c6840321b3e365068b6a64ce54bcb49 (up to 88,000 satellites, 600 to 850 km, 06:00 crossing, laser links, terrestrial energy "has not kept pace").
- Starcloud (Lumen Orbit) white paper "Why we should train AI in space", v1.03, Sep 2024: https://starcloud.com/wp (838 and 770.48 W/m², 633.08 W/m² at 20°C, emissivity 0.92, absorptivity 0.09, $30/kg, 1 kg shielding per kW).
- NASA ISS Active Thermal Control System overview (Boeing, hosted by NASA, undated): https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf (70 kW, radiator units 23.3 m by 3.4 m and 1,122.64 kg, eight panels, Z-93, PVR 14 kW and 740.7 kg, ammonia supply 37°F).
- NASA, Schunk, Babiak and others, "Thermal Control System Architecture and Technology Challenges for a Lunar Surface Habitat", IEEE Aerospace 2022 (NTRS 20210026557): https://ntrs.nasa.gov/api/citations/20210026557/downloads/IEEE%202022%20Paper%20SH%20TCS%20Architecture%20and%20Technical%20Challenges%20Update.pdf (14 kg/m²).
- Planet Labs 8-K Exhibit 99.1, 10 Dec 2025: https://www.sec.gov/Archives/edgar/data/1836833/000119312525314160/pl-ex99_1.htm ("Planet is contracted to deploy two prototype satellites, targeting launch in 2027"). EDGAR full-text search finds no later Planet filing mentioning Suncatcher.
- Gaalema, Indyk and Staley, "Reduced-Mass Orbital AI Inference via Integrated Solar, Compute, and Radiator Panels", arXiv 2604.07760, 9 Apr 2026: https://arxiv.org/abs/2604.07760 (abstract read: >100 kW per launched metric ton, about 500 W/kg, 16 MW and 150 t, custom solutions assumed). Used only in the counter-evidence beat, labelled not peer reviewed.

## Figures dropped or flagged

- Dropped (press only or not re-opened): Starcloud's "10 times lighter" radiator claim; Starcloud-1's launch and in-orbit runs (CNBC); Starcloud-2's slip to 2027; Starcloud's funding and valuation (never for use); China's Three-Body constellation; ESA/Thales ASCEND; Blue Origin's Project Sunrise (51,600 satellites); Amazon's FCC petition and comment counts; Google blog's "up to 8 times more productive" solar line (blog not re-opened); Nvidia blog's "10x cheaper" energy claim.
- Not used: SpaceX roadshow "Starship 99%+ Target Cost Reduction" (baseline unclear in extracted text); Musk's gigawatt-a-year ramp (an aspiration he says is "not a promise"; not needed); Google's inter-satellite link and ground link figures (secondary constraints).
- Flagged as Google's estimate, not a published price: $3,600/kg. I found no launch provider's published price per kilogram to low Earth orbit (spacex.com/rideshare did not render to the fetch tool).
- Derived and labelled as mine: ~67°C for 1,400 W/m²; the 2εσT⁴ curve; 1.8 times the heat from 20°C to 67°C; ISS ~96 kg per kW, ~147 W/m², 14.2 kg/m²; 22.1 and 10.0 kg per kW for a 14 kg/m² radiator; 20.5 kg per kW for Starlink V2 mini; 50 kW per tonne for SpaceX's first generation at 100 t a launch; 86 m² radiator, 480 m² solar and 1.2 t for a 120 kW satellite; 37°F as about 3°C; wear-out around 2033 on a five-year life.
- Caveat stated in the chart caption: the radiator bars treat heat to reject as equal to compute power, which understates it (solar absorption, power conversion losses).

## Could not verify today

- FCC status of SpaceX's and Starcloud's applications after the comment period (no grant found in search; the piece says only "accepted for filing").
- Whether Google and Planet's prototypes remain on track for 2027 beyond the December 2025 8-K.
- Any measured radiator areal density or heat flux for a compute satellite.
- The scout's roadshow slide numbers (44, 63, 64).

## Edits other files may need (not made)

- stack.ts (new `orbit` layer) and Descent.astro (its stop): the main session, per Tommy.
- claims.ts, numbers.ts and glossary.astro entries above.
- `public/covers/data-centres-in-space.svg` to be drawn from the brief above; then make-og.py.
- `cooling` layer constraint still carries the retired 30 to 50 kW band (separate flag).
- Optional: a one-line link from heat-and-water's W45 paragraph to this piece (update-track edit, Tommy's call).
