# Ajinomoto draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/ajinomoto-grows-with-the-package.md` (draft: true)
Cover: `public/covers/ajinomoto-grows-with-the-package.svg`
Drafted 7 October 2026 from Tommy's B200 video notes ("Packaging" bullet), every figure re-sourced to Ajinomoto, Sekisui, LG Chem or Nvidia documents. The video is not cited. Claim needs Tommy's approval before publish.

## Proposed claim

Ajinomoto's build-up film is consumed by the area and layer count of each chip package, so as AI packages grow wider and taller its volume shifts to AI servers faster than chip counts imply, and because a rival film takes a long time to qualify, Ajinomoto keeps that growth at high margins.

### Alternatives considered

1. ABF supply, not substrate or CoWoS capacity, sets a hidden floor under advanced packaging growth until the Kani City plant opens in fiscal 2032. Rejected as the lead: Ajinomoto says nothing about turning customers away, it has said its expansion is aimed at demand to 2030, and nothing in its disclosures would show the film binding before substrates or CoWoS. Kept as a labelled inference in "The plant that opens in 2032".
2. Ajinomoto's position is protected by qualification time, not price, so it can raise prices without losing volume. Rejected as a standalone claim: the reported 30 per cent price rise (May 2026) appears only in secondary press with no Ajinomoto source, and price is not disclosed. Folded in as the margin half of the test.

Chosen because it rests on two series Ajinomoto itself publishes each May (film volume by application, and the Functional Materials business profit margin), it extends rather than repeats the B200 Explainer and the TSMC piece (they say packaging is tight; this says the film scales with package area, not chip count), and both halves can fail on Ajinomoto's own numbers.

## claims.ts entry

```ts
  {
    id: 'ajinomoto-grows-with-the-package',
    claim: 'Ajinomoto\'s build-up film is used by the area and layer count of each chip package, so as AI packages grow wider and taller its film volume shifts to AI servers faster than chip counts imply, and because a rival film takes a long time to qualify, Ajinomoto keeps that growth at high margins.',
    breaksIf: 'In any of Ajinomoto\'s annual results presentations through fiscal 2029 (the year to March 2030), servers and networks fall below 70 per cent of its ABF volume by application, its fiscal 2025 level (the split is rounded to five points, so a flat 70 per cent passes); or the business profit margin of its Functional Materials business, part of the Healthcare and Others segment, falls below 50 per cent in a year when that business\'s sales still grow. Ajinomoto discloses the margin only as rounded wording ("over 50%"); if it stops doing so, the test rests on the volume split alone.',
    watch: ['Ajinomoto\'s ABF volume by application, each May', 'Functional Materials business sales growth and business profit margin, each year', 'Whether construction at the Kani City, Gifu site starts in 2028 and operation in fiscal 2032', 'Whether Sekisui Chemical or LG Chem announce adoption of their build-up film in AI server substrates'],
  },
```

Notes on the test: both series appear in the May results presentation (slide "Functional Materials (Electronic Materials and Others)") and the volume split also in the ASV Report. The split is rounded to 5 points, so 70 per cent is the floor rather than a trend line. Functional Materials is a business inside the Healthcare and Others reportable segment, not a segment, and includes non-film products (adhesives such as PLENSET). Ajinomoto plans to merge Ajinomoto Fine-Techno into the parent on 1 April 2027 (board vote planned 26 November 2026), so its stand-alone accounts would stop; the test uses the Functional Materials business, not the subsidiary. Gifu depreciation begins after the test window.

## stack.ts

Layer `chips` ("Chips and the factories that make them"), after the B200 Explainer:
`pieces: ['the-two-seconds-after-you-hit-send', 'tsmc-says-it-is-the-bottleneck', 'nobody-makes-a-b200-alone', 'ajinomoto-grows-with-the-package']`

## Glossary (heading "Chips, memory and the wiring between them")

Already present: Package substrate, ABF, Qualification, CoWoS. Add:
- `Build-up film`: The insulating sheet laid between each layer of copper wiring in a chip's package substrate. Ajinomoto's ABF is the best known; Sekisui Chemical and LG Chem make or develop rivals.
- `Thermosetting`: A material that hardens permanently when heated and cannot be melted again, like a baked enamel. Ajinomoto's build-up film is one.

Heading where finance-as-evidence terms sit ("Getting power to the building" per the Schneider sidecar):
- `Business profit`: Ajinomoto's main measure of operating profit, reported for each segment. Used on this site only as evidence of how scarce a product is.

## numbers.ts

```ts
  { layer: 'chips', value: '70 → 120 mm', what: 'Ajinomoto\'s estimate of how the base of an advanced chip package grows: about 70 millimetres square with nine wiring layers up to 2023, about 100 with eleven in 2026, about 120 with thirteen from 2031. Each layer needs its own sheet of insulating film.', piece: 'ajinomoto-grows-with-the-package', asOf: 'May 2026' },
```

(The B200 sidecar proposed a Kani City "2026 → 2032" figure that was never added; if Tommy wants it, attach it to this piece instead.)

## LinkedIn post (§9)

```
The company best known for monosodium glutamate makes the film inside almost every powerful chip.

Ajinomoto's build-up film insulates each wiring layer in the base under a processor. AI chip bases are growing from about 70 millimetres square with nine layers to about 100 with eleven, by Ajinomoto's own estimate, so each package needs far more film than chip counts suggest. Servers and networks have gone from 40 to 70 per cent of its film volume, and its next plant opens only in 2032.

The piece covers why the film grows faster than the chips, why chipmakers rarely switch to a rival, and what the 2032 plant date implies.

https://thephysicallayer.fyi/journal/ajinomoto-grows-with-the-package/

#Semiconductors #AIInfrastructure #SupplyChain
```

## Sources (each figure, with URL)

- Ajinomoto FY2025 results presentation "Forecast for FY2026 and Initiatives for Enhancing Corporate Value", Shigeo Nakamura, 7 May 2026: https://ajinomoto-ir.swcms.net/company/en/ir/event/presentation/main/011111114/teaserItems1/01/linkList/00/link/FY25Q4_Presentation_E_with%20script.pdf
  - Slide 25: ABF volume by application, servers and networks (high-end) 40% FY17, 60 FY22, 65 FY23, 70 FY24, 70 FY25, outlook 75 to 85 FY30; PC 45 FY17, 20 FY25, 10 to 15 FY30. Functional Materials sales 131% of prior year FY25; business profit margin "over 50%" FY25, "about 30%" FY18. FY26 plan 110% (initial).
  - Slide 26: package sizes (company estimates): up to 2023 HPC about 70 mm square, 9 layers; 2026 AI about 100 mm, 11 layers; 2031 onward about 120 mm, 13 layers. "package boards are increasingly large and multi-layered and the use of ABF is also increasing".
  - Slide 27: "investment in expanded production aimed at 2030 (total: ¥25 billion from 2023 onward)"; third site after Gunma and Kawasaki, operation in FY2032.
- Ajinomoto Q1 FY2026 presentation, Masataka Kaji, 6 August 2026: https://ajinomoto-ir.swcms.net/company/en/ir/event/presentation/main/011111113/teaserItems1/01/linkList/00/link/FY25Q4_Presentation_E.pdf (file name says FY25Q4, content is Q1 FY2026)
  - Slide 14: Functional Materials Q1 FY2026 sales 154%, business profit 177% of prior year; ABF sales "strong for high-performance boards used in AI, servers, networks"; "product mix is also improving"; FY2026 forecast revised up.
  - Slide 15: Ajinomoto Fine-Techno FY2025 sales ¥98,383 million, operating profit ¥53,012 million; merger into the parent planned 1 April 2027.
  - Slide 9: assumed exchange rate ¥150 to the US dollar (used for the $670 million conversion).
- Ajinomoto H1 FY2025 presentation with script, 6 November 2025: https://www.ajinomoto.co.jp/company/en/ir/event/presentation/main/011111112/teaserItems1/01/linkList/02/link/FY25Q2_Presentation_E_with%20script.pdf (background only; seven consecutive quarters of growth, AI servers plus PC recovery)
- Ajinomoto ASV Report 2026 (integrated report), published September 2026 (PDF dated 2 September 2026; report says "End of August 2026"): https://www.ajinomoto.co.jp/company/en/ir/library/annual/main/04/teaserItems1/0/linkList/0/link/ASV_Report_2026_A4_en.pdf
  - p. 44 to 45: "The volume of ABF used is also rising along with this trend"; volume by application chart; trust built over "more than 25 years" ... "This relationship is precisely what serves as a barrier for new entrants"; "a rise in the share of high-priced products"; High-speed Development System cycle (sample, evaluation by customer, redevelop, approval of customer); "A new manufacturing facility started operations in our Gunma plant in 2025"; Gifu operations "in fiscal 2032".
- Ajinomoto investor overview "AJINOMOTO CO., INC (2802) (As of September 2026)": https://ajinomoto-ir.swcms.net/company/en/ir/library/first_presentation/main/0/teaserItems1/00/file/First%20presentation_E_202312.pdf
  - p. 18: "More than a 95% share of the global market for insulating films for high-performance semiconductors"; Electronic materials and others sales ¥100.7bn (FY25). p. 3: AJI-NO-MOTO commercialised 1909.
- Ajinomoto Build-up Film page, read 7 October 2026: https://www.ajinomoto.com/innovation/our_innovation/buildupfilm
  - "a product of choice for nearly all high-performance CPUs"; first adopted by a major semiconductor manufacturer in 1999; thermosetting film of epoxy resins, hardener and inorganic microparticle filler; surface receptive to laser processing and direct copper plating.
- Ajinomoto and Ajinomoto Fine-Techno release, 7 May 2026: https://news.ajinomoto.co.jp/2026/05/20260507-02.html
  - announced it would buy land (location agreement May, purchase contract June 2026) at Kani Mitake Interchange industrial park, Kani City, Gifu; about ¥1.2bn; construction from 2028, operation from 2032 (fiscal 2032 in the results deck and ASV Report); for ABF demand after 2030; third site after Kawasaki and Gunma.
- Sekisui Chemical semiconductor materials page, read 7 October 2026: https://www.sekisui.co.jp/electronics/en/device/semicon/
  - Build-up film (interlayer insulating film) for FC-BGA substrates, NX04 and NQ07 series; FC-BGA used in PCs, servers and networks.
- LG Chem blog, "Designing the Core Layer of High-Performance Packages: LG Chem's BUF R&D Team", 21 July 2026: https://blog.lgchem.com/en/2026/07/21_buf_interview/
  - "We develop BUF applied to high-performance semiconductor package substrates used in AI servers, HPC systems"; warpage under heat and repeated thermal and mechanical stress.
- Nvidia fourth quarter and fiscal 2026 results, 25 February 2026 (Form 8-K exhibit): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm
  - Data Center full-year revenue $193.7 billion.

My own arithmetic, labelled in the piece: area times layers 70²×9 = 44,100; 100²×11 = 110,000 (about 2.5 times); 120²×13 = 187,200 (about 4.2 times), assuming film per layer scales with board area. ¥100.7bn ÷ 150 = about $670m; ÷ $193.7bn = about 0.35 per cent (periods differ by two months: Ajinomoto to March 2026, Nvidia to January 2026). Six years from land (May 2026) to operation (fiscal 2032, from April 2032).

## Could not verify / left out

- Ajinomoto's "more than 95 per cent" is its own claim in the investor overview, so it is used attributed and called Ajinomoto's estimate. The B200 sidecar said it was not on Ajinomoto's pages; it is in the September 2026 investor overview. The phrase "market share" is avoided.
- How long a rival film takes to qualify: no primary source gives a figure (the "30 to 36 months" and "multi-year" figures are from blogs and an activist investor's deck). The piece says nobody publishes it, and presents "slow" as inference from Ajinomoto's own description.
- Resonac as a rival film maker: only secondary sources found; left out. Sekisui and LG Chem are named from their own pages.
- A reported 30 per cent ABF price rise (May 2026) and analyst supply-gap forecasts (10, 21, 42 per cent): secondary press only, no Ajinomoto source; left out.
- "¥25 billion to raise capacity 50 per cent by 2030": the 50 per cent figure is from press interviews, not an Ajinomoto document; only the ¥25 billion total is used. Plant locations for that spending are not stated in the deck sentence, so the piece names the two sites separately.
- Shinko Electric Industries (exposure map, full name kept after the 2025 JIC-led buyout): its own English site (https://www.shinko.co.jp/english/, read 7 October 2026) lists flip-chip type packages; FC-BGA substrate line confirmed by the fact-check.
- The film's cost per package is not disclosed; the "cheap relative to the product" point is made with segment revenue against Nvidia's data centre revenue and labelled as my arithmetic and inference.
- The May 2026 results call transcript was not available; no management quotes beyond the presentations and ASV Report are used.

## Fact-check fixes (7 October 2026)

Kani now "announced it would buy land", construction planned from 2028, operation in fiscal 2032, matching the B200 piece. Summary uses Ajinomoto's "nearly all high-performance" processors wording, with the AI growth link marked as my reading. Functional Materials called a business inside Healthcare and Others throughout. Fine-Techno merger now "plans to merge" (1 April 2027, board vote 26 November 2026). Falsifier states that a flat 70 per cent passes and that the margin is rounded wording only, with the volume split as fallback. Thesis line and claim both end "at high margins". CoWoS appears only in the exposure map. Shinko named in full as Shinko Electric Industries.
