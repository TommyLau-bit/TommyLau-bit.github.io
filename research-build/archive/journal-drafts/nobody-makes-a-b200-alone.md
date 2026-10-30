# Nvidia B200 draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/nobody-makes-a-b200-alone.md` (draft: true)
Cover: `public/covers/nobody-makes-a-b200-alone.svg`
Shape: Explainer. No claims.ts entry. Drafted 7 October 2026 from Tommy's video notes; every figure re-sourced below, the video is not cited.

## stack.ts

Layer `chips` ("Chips and the factories that make them"). Add after `tsmc-says-it-is-the-bottleneck`:
`pieces: ['the-two-seconds-after-you-hit-send', 'tsmc-says-it-is-the-bottleneck', 'nobody-makes-a-b200-alone']`
(The checker skips the map test while `draft: true`; it will fail at publish until this line is added.)

## Exposure map decision

Treated as a whole-stack orientation map of one product's supply chain (WRITING-FORMAT §3.4), so there is no "On the other side" loser. The `<dl class="against">` block is kept as "Where I stop", the memory piece's precedent, saying the map has no loser and I hold no view on the companies.

New company names this creates pages for: Arm, ASML, ZEISS, Trumpf, Applied Materials, Lam Research, Tokyo Electron, KLA, Shin-Etsu, SUMCO, JSR, Tokyo Ohka Kogyo, AGC, Hoya, Ajinomoto, Ibiden, Unimicron, Advantest, Teradyne, Wistron. Existing spellings reused: Nvidia, TSMC, SK Hynix, Micron, Samsung, Broadcom, Marvell, Coherent, Lumentum, Corning, Texas Instruments, Infineon, Monolithic Power, Vertiv, Foxconn, Quanta.

## Glossary (heading "Chips, memory and the wiring between them")

Already present: Wafer, Foundry, Fab, CoWoS, Advanced packaging, HBM, Tape-out, Cold plate, Optical transceiver, Switch chip. Add:
- `Die`: A single chip cut from a wafer. An Nvidia B200 joins two large logic dies so they behave as one processor.
- `Package`: The finished chip component you could hold, with dies, memory and wiring mounted together on a base.
- `Qualification`: The months or years of testing a customer runs before trusting a new supplier's part. It is why a cheaper alternative cannot simply be swapped in.
- `Mask`: A plate carrying the circuit pattern for one layer of a chip. The most advanced masks are mirrors rather than stencils.
- `Lithography`: Printing a chip's circuit pattern onto a wafer with light, layer by layer.
- `EUV`: Extreme ultraviolet lithography, using light of 13.5 nanometres for a chip's finest layers. Only ASML builds the machines.
- `Photoresist`: The light-sensitive coating on a wafer that lithography prints the pattern into. Made by a few Japanese chemical companies and slow to change.
- `Interposer`: A slab of extremely fine wiring that the processor and its memory sit on side by side, so they can talk at short range.
- `Package substrate`: The laminated circuit board under the interposer that carries power and signals out to the rest of the computer.
- `ABF`: Ajinomoto Build-up Film, the insulating film between the wiring layers of a package substrate. Ajinomoto says it is the product of choice for nearly all high-performance CPUs.

## numbers.ts (optional)

```ts
  { layer: 'chips', value: '2026 → 2032', what: 'Ajinomoto\'s planned new plant for the insulating film inside chip package substrates: land announced in May 2026, construction from 2028, operations from 2032.', piece: 'nobody-makes-a-b200-alone', asOf: 'May 2026' },
```

## LinkedIn post (§9)

```
Nobody makes an Nvidia B200 on their own, not even Nvidia.

One accelerator draws on factories mostly in Taiwan, machines from the Netherlands, mirrors from Germany, memory from South Korea and materials from Japan. Some of those suppliers could be swapped in months. Others would take years, because a replacement needs a new factory or years of testing before anyone trusts it, and that is the dependency that matters.

The piece follows one B200 from blueprint to wafer, through its memory and packaging, and into the rack.

https://thephysicallayer.fyi/journal/nobody-makes-a-b200-alone/

#Semiconductors #SupplyChain #AIInfrastructure
```

## What I dropped or corrected from the notes, and why

- EDA figures (about $770bn industry revenue, EDA under 2 per cent, Synopsys and Cadence about three quarters): dropped. Design is out of scope (§5), and the figures were not needed.
- "Silicon interposer": corrected. Huang said on 16 January 2025 that Blackwell uses "largely CoWoS-L", which uses local silicon bridges in a wider interposer rather than one full silicon slab. The piece says "a slab of extremely fine wiring with small silicon bridges".
- ZEISS mirror "largest bump under 1 mm at the size of Germany": corrected to ZEISS's own 0.1 millimetres.
- Ajinomoto "over 95 per cent": not found on Ajinomoto's own pages (only trade press). Replaced by Ajinomoto's wording, "product of choice for nearly all high-performance CPUs". The word "market share" is also banned by the checker.
- EUV machine about 180 tonnes, multiple cargo planes, "a few hundred machines", "dozens a year": only in trade press; ASML's 2025 unit count could not be confirmed from a primary source in this session. Dropped. Kept ASML's own 13.5 nm, tin drops up to 50,000 times a second, and "unique to ASML".
- TSMC about 70 per cent of foundry revenue: third-party estimate, dropped. "25 companies 25 years ago, three today" and "about a thousand process steps": unsourced, dropped.
- Samsung struggling to qualify one HBM generation: not sourced from a primary document, dropped. Memory suppliers taken from Nvidia's 10-K.
- "Three years from first architecture decision to a running rack": unsourced, dropped.
- SMIC and Huawei, export controls, onshoring subsidies, car-chip shortage, Arm royalties and RISC-V: out of scope, dropped.
- "The wafers started in Japan": softened to "the bare silicon came from a short list of wafer makers, the largest of them Japanese", because the origin of any particular B200's wafers is not disclosed.
- "6,600 years" kept as my own arithmetic: 208 billion seconds divided by 31.56 million seconds a year is about 6,590 years.

## Points for the fact-checker

- The eight HBM stacks: Nvidia's GTC 2024 presentation as reported by AnandTech, confirmed by TechInsights' teardown (15 April 2025).
- "Shin-Etsu and SUMCO are among the largest makers" rests on Shin-Etsu Handotai's own description of itself as the largest silicon wafer producer; SUMCO's rank is from general knowledge.
- "A small group of makers, such as Ibiden and Unimicron, builds the substrates for AI processors": descriptive, no share figure used.
- TSMC July 2026 packaging quote and fab timelines are reused from the published TSMC piece, which cites the calls.

## Sources (every figure)

- Nvidia Blackwell architecture page (208 billion transistors, two reticle-limited dies, 10 TB/s link, TSMC 4NP), read 7 October 2026: https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
- Nvidia GTC release, 18 March 2024 (208 billion transistors, 4NP, GB200 joins two B200s to a Grace CPU, NVL72 of 72 GPUs and 36 CPUs): https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing
- Nvidia GB200 NVL72 page (36 Grace CPUs, 72 Blackwell GPUs, liquid cooled, NVLink Switch, Arm Neoverse V2 cores), read 7 October 2026: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- TechInsights teardown of Nvidia Blackwell, 15 April 2025 ("eight HBM packages"), reported at https://www.electronicspecifier.com/?p=38230
- Nvidia, 17 October 2025, first Blackwell wafer produced at TSMC Arizona, volume production starting there: reported by HPCwire: https://hpcwire.com/2025/10/17/blackwell-rises-from-phoenix-fab (Nvidia blog URL not confirmed)
- AnandTech, 18 March 2024, reporting Nvidia's GTC presentation (eight HBM3e stacks, 192GB, 8 TB/s): https://www.anandtech.com/show/21310
- Nvidia Form 10-K for fiscal year ended 25 January 2026, filed 25 February 2026 (TSMC and Samsung wafers; memory from SK Hynix, Micron and Samsung; CoWoS; Hon Hai, Wistron, Fabrinet; lead times of more than 12 months; premiums, deposits, long-term supply agreements and capacity commitments): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- Jensen Huang, Taichung, 16 January 2025, "As we move into Blackwell, we will use largely CoWoS-L", as reported by Reuters (via Business Day): https://www.businessday.co.za/bd/companies/2025-01-16-nvidias-advanced-packaging-needs-remain-strong-huang-says
- TSMC earnings calls of 15 January, 16 April and 16 July 2026 (fab build two to three years, ramp one to two years, packaging capacity limiting customers' growth), as cited in the published piece tsmc-says-it-is-the-bottleneck: https://investor.tsmc.com/english/quarterly-results
- ASML EUV lithography systems page (13.5 nm, tin drops hit up to 50,000 times a second, mirrors in high vacuum, technology unique to ASML), read 7 October 2026: https://www.asml.com/en/products/euv-lithography-systems
- ZEISS SMT EUV lithography page (mirror at the size of Germany, largest unevenness 0.1 mm; TRUMPF laser; 50,000 tin droplets a second), read 7 October 2026: https://www.zeiss.com/semiconductor-manufacturing-technology/inspiring-technology/euv-lithography.html
- Ajinomoto Build-up Film page ("product of choice for nearly all high-performance CPUs", adopted 1999, amino acid chemistry origin), read 7 October 2026: https://www.ajinomoto.com/innovation/our_innovation/buildupfilm
- Ajinomoto release, 7 May 2026 (land in Kani City, Gifu, about ¥1.2bn, ABF plant, construction from 2028, operation from 2032): https://news.ajinomoto.co.jp/2026/05/20260507-02.html
- Micron fiscal first quarter 2026 earnings call, 17 December 2025 (price and volume agreed for entire calendar 2026 HBM supply), as reported: https://newsquawk.com/headlines/micron-technology-inc-mu-ceo-says-co-has-completed-agreements-on-price-and-volume-for-calendar-2026-hbm-supply-expect-tight-memory-market-conditions-to-persist-beyond-calendar-2026-17-12-2025
- Shin-Etsu Handotai Europe company page (largest producer of semiconductor silicon), read 7 October 2026: https://www.sehe.com/?p=180

## Fact-check fixes (7 October 2026)

Ajinomoto now "announced it would buy land" (location agreement May, purchase contract June 2026). TSMC made the dies "mostly in Taiwan" (first Blackwell wafer at TSMC Arizona, 17 October 2025). Memory: "Nvidia buys its memory from three makers". The four replacement-time groups are framed as my own rough sort; "swappable fastest" hedged to "probably months rather than years"; TSMC noted as in practice the only source of 4NP dies and CoWoS-L for the B200; Ajinomoto placed "close by" the no-second-source group as my reading, noting rival films (such as Sekisui and Resonac) exist and its own claim covers CPUs. Between racks: Nvidia's own switches named first, Broadcom as the alternative. Power: "hundreds of volts of alternating current" to agree with the TI piece's 54 volt rack figure; body says Monolithic Power Systems (the exposure map keeps the existing spelling "Monolithic Power" so the company page is not split). TechInsights teardown added to the sources. Cover bars recoloured blue (compute) per §7. Trimmed five sentences to stay under 1,500 words.
