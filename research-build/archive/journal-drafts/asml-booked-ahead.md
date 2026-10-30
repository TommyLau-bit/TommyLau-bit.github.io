# ASML draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/asml-booked-ahead.md` (draft: true)
Cover: `public/covers/asml-booked-ahead.svg`
Drafted 7 October 2026 from Tommy's B200 video notes ("Lithography" bullet). Every figure re-sourced to ASML's SEC filings (20-F and 6-K exhibits), ASML's and ZEISS's EUV pages, and ASML's 15 July 2026 investor call. The video is not cited. Claim needs Tommy's approval before publish.

## Proposed claim

ASML's EUV output is sold out and committed a year or two ahead (2026 shipments of around 65 low NA systems equal its stated capacity, 2027 is "close to being fully covered with orders"), and it grows only as fast as ZEISS optics and ASML's cleanrooms allow, about 30 per cent a year, so a chipmaker adding leading-edge AI capacity must commit to scanners a year or two ahead, much as a data centre books a grid connection.

The stronger reading, that ASML's count paces new leading-edge AI chip capacity, is presented in the piece as Tommy's judgement only, not as the claim. ASML's own position (Fouquet: "the whole goal of our supply is to follow that demand"; "the capacity is there to meet the demand but the demand is still fluctuating"; Dassen: 85 is "a nice representation of the balance") is quoted in context, in answer to TD Cowen's question whether ASML was meeting demand rather than under-shipping, and answered openly in "ASML says it is not short".

Revised twice on 7 October 2026 after fact-checks: earlier slugs `asml-sets-the-pace` and `asml-booked-years-ahead` and claim ("sells every machine it can build, so its output sets the pace for AI chip factories") narrowed; files renamed.

### Alternatives considered

1. ZEISS's optics output, not ASML's own assembly, is the true ceiling on EUV supply. Rejected as the lead: ASML's 20-F says so in general terms, but ZEISS publishes no unit or capacity figures, so nothing observable could falsify it. Kept as the section "The supplier behind the supplier".
2. ASML's machine count sets the pace of new AI chip factories. Rejected as the claim: ASML says it sizes capacity to orders and is not short, so its disclosures cannot separate "pace-setter" from "fully booked". Kept as labelled judgement.

Chosen because every part is stated by ASML and reported against: capacity and expected shipments (around 65), order coverage for 2027 and 2028, the 30 per cent capacity steps, and quarterly EUV units. It extends the B200 Explainer (EUV has no second source) and the TSMC piece (fab build times) with the booking horizon, and it fails visibly on ASML's own words.

## claims.ts entry

```ts
  {
    id: 'asml-booked-ahead',
    claim: 'ASML\'s EUV machines are sold out and committed a year or two ahead, and their number grows only as fast as ZEISS optics and ASML\'s cleanrooms allow, about 30 per cent a year, so a chipmaker adding leading-edge AI capacity must commit to scanners a year or two ahead, much as a data centre books a grid connection.',
    breaksIf: 'The booking half fails if ASML says it has EUV capacity beyond what customers have ordered; or ships more than 10 per cent fewer low NA EUV systems than its stated capacity (around 65 for 2026, around 85 for 2027) and itself attributes the shortfall to customer demand or pushed-out orders; or by its fourth quarter 2026 results (January 2027) no longer describes 2027 as close to fully covered with orders; or says its EUV order lead times are shortening. The growth half fails if ASML raises its stated low NA EUV capacity by more than 40 per cent in a single year, or announces new EUV cleanroom space or a second source for its optics. A shortfall caused by ZEISS or other suppliers supports the claim rather than breaking it.',
    watch: ['ASML\'s EUV units each quarter, and low NA (NXE) units in its annual report', 'How ASML describes order coverage for 2027 and 2028', 'Whether ASML confirms the further 30 per cent low NA capacity increase for 2028', 'High NA adoption after Intel qualified it on select 18A layers in July 2026'],
  },
```

Notes on the test: ASML's quarterly presentation reports "Sales in lithography units" by technology (EUV includes High NA: 2025's 48 = 44 NXE + 4 EXE; 2024's 44 = 42 + 2). The capacity figures are ASML's stated low NA capacity. ASML stopped reporting quarterly bookings after Q4 2025, so bookings cannot be the test; order coverage and lead times are described on calls. High NA's "fewer systems overall" and export controls could lower low NA units without slack; the piece names both.

## stack.ts

Layer `chips` ("Chips and the factories that make them"), after `nobody-makes-a-b200-alone` and before `ajinomoto-grows-with-the-package` (lithography comes before packaging in the physical chain):
`pieces: ['the-two-seconds-after-you-hit-send', 'tsmc-says-it-is-the-bottleneck', 'nobody-makes-a-b200-alone', 'asml-booked-ahead', 'ajinomoto-grows-with-the-package']`
If Ajinomoto has not been added yet, simply append `asml-booked-ahead` after the B200 piece.

## Glossary (heading "Chips, memory and the wiring between them")

Already present: Lithography, EUV, Fab, Wafer, Backlog. Add:
- `EUV scanner`: The machine that prints a chip's finest layers with extreme ultraviolet light. Only ASML builds them; it expects to ship about 65 of its standard model in 2026.
- `Numerical aperture (NA)`: How wide a cone of light a lithography machine's optics gather. ASML's standard EUV machines are 0.33 NA (low NA); its newer High NA machines are 0.55 and print finer detail.
- `High NA`: ASML's newest EUV machines, with 0.55 numerical aperture. Intel qualified one for some layers of its 18A process in July 2026.
- `Installed base`: All the machines already working in customers' factories. ASML reports its service and upgrade sales on them as Installed Base Management.
- `18A`: Intel's most advanced chip manufacturing process. (Only if Tommy wants it; it appears once, defined in place.)

## numbers.ts

```ts
  { layer: 'chips', value: '~65 → ~85', what: 'ASML\'s capacity for standard (low NA) EUV machines in 2026, all expected to ship, and its plan for 2027, already close to fully ordered by July 2026. Every leading-edge chip factory needs them.', piece: 'asml-booked-ahead', asOf: 'July 2026' },
```

## LinkedIn post (§9)

```
The machines that print the finest AI chips are booked a year or two before they are built.

ASML is the only company that makes EUV lithography machines. It expects to ship about 65 of its standard model this year, its full capacity, and says 2027 is already close to fully ordered. Its output can grow only as fast as ZEISS can make the optics, so a chipmaker adding capacity has to commit a year or two ahead, much like a data centre booking its grid connection.

The piece covers why only ASML can build them, the supplier behind the supplier, and what ASML itself says about whether it is short.

https://thephysicallayer.fyi/journal/asml-booked-ahead/

#Semiconductors #AIInfrastructure #SupplyChain
```

## Sources (each figure, with URL)

- ASML Annual Report 2025 on Form 20-F, filed 25 February 2026: https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/asml-20251231.htm
  - "ASML is currently the world's only manufacturer of EUV lithography systems" (Our products and services).
  - EUV systems recognised (units) 48 in 2025, 44 in 2024 (Financial performance KPIs, p. 54); four EXE and 44 NXE in 2025, two EXE and 42 NXE in 2024 (p. 55 to 56).
  - Risk factors: "The number of lithography systems we are able to produce is limited by the production capacity of one of our key suppliers, Carl Zeiss SMT, our sole supplier of lenses, mirrors, illuminators, collectors and other critical optical components"; EUV parts single-sourced where "multi-sourcing economically impractical".
  - Note 26: Carl Zeiss SMT "capable of developing and producing these items only in limited numbers and only through the use of manufacturing and testing facilities in Oberkochen and Wetzlar, Germany"; ASML holds 24.9% of Carl Zeiss SMT Holding GmbH & Co. KG, which owns 100% of Carl Zeiss SMT GmbH; 2021 framework agreement commits ASML to finance ZEISS SMT capex above certain thresholds through loans.
  - Customers: in 2025 four customers each exceeded 10% of total net sales, together €20.0bn or 61.2%.
  - NXE:3800E shipped at full specification, 220 wafers per hour, 37% more than the NXE:3600D; field upgrades to the installed base on track. (The CEO Q&A in the same report says "160 to 230"; the piece uses the product section's 220 and 37%.)
  - CFO letter: "a significant number of TWINSCAN NXE:3800E field upgrades, which resulted in a substantial portion of EUV system revenue being shifted to installed base revenue."
  - Net service and field option sales (Installed Base Management) €8,193.0m in 2025, up 26.2% from €6,494.2m; drivers: growing installed base, higher tool use, NXE field upgrades.
  - High NA: EXE platform "saves valuable fab space by requiring fewer systems overall".
  - Export controls "may have a material impact on our business for example on the sales volume, mix and timing".
- ASML Annual Report 2023 on Form 20-F, filed 14 February 2024 (EUV systems recognised 53 in 2023, 40 in 2022): https://www.sec.gov/Archives/edgar/data/937966/000093796624000008/asml-20231231.htm
- ASML Annual Report 2021 on Form 20-F, filed 9 February 2022 (EUV systems recognised 31 in 2020, 42 in 2021): https://www.sec.gov/Archives/edgar/data/937966/000093796622000013/asml-20211231.htm
- ASML Q4 and full-year 2025 results, 28 January 2026 (6-K exhibit 99.1): https://www.sec.gov/Archives/edgar/data/937966/000162828026003701/pressreleasefinancialresul.htm
  - Backlog at end-2025 €38,797m; 2025 net bookings €28,035m; Q4 net bookings €13.2bn of which €7.4bn EUV. Net system sales 2025 €24,474m (presentation slide 9: https://www.sec.gov/Archives/edgar/data/937966/000162828026003701/a2026_01x28xpresentation009.jpg).
- ASML Q2 2026 results, 15 July 2026 (6-K exhibit 99.1): https://www.sec.gov/Archives/edgar/data/937966/000162828026048235/pressreleasefinancialresul.htm
  - CEO statement: "we are planning to add 30% to our 2026 low NA EUV capacity of around 65 for 2027, and we are investigating to increase capacity with another 30% for 2028"; Capital Markets Day 10 June 2027.
- ASML Q2 2026 presentation, 15 July 2026 (6-K exhibit 99.2): slide 8 EUV units 16 in Q1 2026 and 16 in Q2 2026 (https://www.sec.gov/Archives/edgar/data/937966/000162828026048235/presentationinvestorrela008.jpg); slide 6 Intel quote, "qualifying the High NA EUV process option on select Intel 18A product layers" (https://www.sec.gov/Archives/edgar/data/937966/000162828026048235/presentationinvestorrela006.jpg).
- ASML Q2 2026 investor call, 15 July 2026, transcript as published by Webull (ASML's own transcript page returned HTTP 403 to automated fetches; check against asml.com before publish): https://www.webull.com/news/15235467245265920
  - Dassen: "We are now close to being fully covered with orders for low NA EUV, and we are planning to increase our low NA EUV capacity by around 30%"; "we think the 85 is a nice representation of the balance..."; "we're investigating, you know, the 110 scenario for EUV in low NA by 2028"; "Installed base management sales are expected to grow over 30% this year"; "the long order lead times that we have".
  - Dassen: "we now expect to ship around 65 low NA EUV systems this year"; "Looking ahead to 2028, we have already received a significant number of low NA EUV orders."
  - Krish Sankar (TD Cowen), as transcribed: "You are meeting the demand not under shipping, is that correct?" Fouquet: demand for 2027 and 2028 not yet at "a stable state"; "the whole goal of our supply is to follow that demand"; "short answer is yes, the capacity is there to meet the demand but the demand is still fluctuating".
  - Fouquet: capacity increases "are based on our existing footprint" without new cleanroom (the "optimizing the existing clean room space" wording appears only in this transcript, so the piece paraphrases "as transcribed").
- ASML EUV lithography systems page, read 7 October 2026: https://www.asml.com/en/products/euv-lithography-systems
  - "EUV light is absorbed by everything, even air"; whole light path in high vacuum; multilayer mirrors instead of lenses; CO2 laser fires two pulses at a fast-moving drop of tin, "up to 50,000 times per second"; 13.5 nm "unique to ASML".
- ZEISS SMT EUV lithography page, read 7 October 2026: https://www.zeiss.com/semiconductor-manufacturing-technology/inspiring-technology/euv-lithography.html
  - Projection optics: six mirrors, around 20,000 parts weighing 2 tonnes; high-power CO2 laser from TRUMPF (spelled Trumpf in the piece and map, matching the B200 piece). (The Germany 0.1 mm comparison is already in the B200 piece and not repeated.)
- TSMC fab build and ramp times are cited through the published piece `tsmc-says-it-is-the-bottleneck` (TSMC earnings calls of 15 January and 16 April 2026).

My own arithmetic, labelled in the piece: 31 + 42 + 40 + 53 + 44 + 48 = 258 EUV systems recognised in sales from 2020 to 2025 (a sales count including High NA, not an installed base). Backlog €38.8bn ÷ 2025 net system sales €24.5bn × 12 = about 19 months (backlog includes DUV and metrology orders, so it is all systems, not EUV only). 65 × 1.3 ≈ 85; 85 × 1.3 ≈ 110 (ASML's CFO used both numbers on the call).

## Could not verify / left out

- Machine weight (~180 tonnes), "several cargo planes", "40 containers, 20 trucks", months to install: only trade press, no ASML page found. Dropped. (The 20-F says ASML historically shipped by air and now uses ocean freight for some deliveries; not used.)
- High NA price (about €350m in press): not in ASML's filings. Dropped.
- Installed base as a total count of EUV machines in the field: ASML does not state it in the 2025 20-F. The piece uses the labelled sum of units recognised 2020 to 2025 instead; the asml.com page says the 100th EUV system shipped at the start of 2020, not used.
- Number of EUV scanners per fab, or how many fabs ASML's output can equip: no primary source. The piece keeps this as a labelled inference.
- "Nikon and Canon do not make EUV": not stated in a primary source I could reach. The exposure map says only that they make lithography machines for layers that do not need EUV; ASML's "world's only manufacturer" covers the rest.
- Which chipmakers use EUV: ASML does not name customers (other than Intel's High NA quote). The map lists TSMC, Samsung, Intel, SK Hynix and Micron by what they make, not as named ASML customers.
- Q3 2026 results date: 14 October 2026 per third-party calendars (akrostec.com); ASML's investor site timed out. The piece says "mid October".
- DUV dropped from the exposure map (not defined in the piece); the map now says ASML "makes lithography systems, including every EUV machine".
- China and export controls: kept to ASML's own general risk wording; China sales share not used.

## Second fact-check fixes (7 October 2026)

Title and slug changed to "booked a year or two ahead" / `asml-booked-ahead` (evidence: 2027 close to fully covered, significant 2028 orders). Falsifier now covers both halves, including the 30 per cent growth limit (fails above 40 per cent in a year, new EUV cleanroom space, or a second optics source), and the shortfall test uses ASML's own stated reason. Trumpf spelled as in the B200 piece. Cover legend now reads "EUV SOLD (ALL)" for 2020 to 2025 (includes High NA) against "LOW NA CAPACITY" for 2026, with 2027 "PLAN" and 2028 "INVESTIGATING".
