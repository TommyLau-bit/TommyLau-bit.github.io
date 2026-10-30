# Micron draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/micron-three-times-the-wafer.md` (draft: true)
Cover: `public/covers/micron-three-times-the-wafer.svg`
Drafted 7 October 2026 from Tommy's B200 video notes ("Memory wall" bullet). Every figure re-sourced to Micron's own prepared remarks, call transcripts and 8-K, Micron's HBM4 page, and SK Hynix's 2Q26 release. The video is not cited. Claim needs Tommy's approval before publish.

## Subject choice

Micron, not SK Hynix. Micron's US disclosures state the physical mechanism in numbers (the HBM trade ratio, "approximately three times" DDR5's wafer per bit) and report each year's HBM contract status on a fixed calendar, so both halves of the claim are testable in its own words. SK Hynix's English release confirms the same squeeze (quoted once) but gives no trade ratio or contract coverage. SK Hynix and Samsung are in the exposure map.

## One finding that contradicts the notes

The notes say HBM has "more pricing power than commodity DRAM". Micron's own wording says the opposite for 2026: its 2027 HBM agreements carry "significant price increases year over year, narrowing the gross margin gap with conventional DRAM", and Mehrotra said 2026 HBM prices "were negotiated with our customers last year". So HBM, priced a year ahead, has earned less than ordinary DRAM sold into the shortage. The piece reports this as Micron's wording, with my reading labelled. It does not contradict the countertop piece (which says HBM costs five to six times as much and is "priced like a luxury"; it makes no margin comparison).

## Proposed claim

Micron sells most of each year's HBM before that year starts, and because each HBM bit takes about three times the wafer of ordinary DRAM (Micron's figure, and higher for HBM4), every year HBM grows faster than conventional DRAM it takes wafers from ordinary memory and keeps that market short too.

### Alternatives considered

1. HBM behaves less like a commodity than ordinary DRAM because it is qualified per accelerator and contracted ahead. Rejected as the lead: the pricing half is contradicted by Micron's own 2026 margin wording, and "less like a commodity" has no clean observable test. Kept as the "Sold before it is made" section.
2. SK Hynix leads HBM and its lead lasts because qualification is slow. Rejected: no primary source states a ranking without straying into share, SK Hynix publishes no qualification timeline, and it drifts toward a competitive call on one company.

Chosen because it stays physical (wafers, die size, base die, stacking yield, cleanroom timing), extends the countertop Explainer and the B200 map without repeating them, ties to the site's argument (Micron itself names "enhanced energy infrastructure" among the limits on new fabs), and both halves fail visibly on Micron's own calls.

## claims.ts entry

```ts
  {
    id: 'micron-three-times-the-wafer',
    claim: 'Micron sells most of each year\'s HBM before that year starts, and because each HBM bit takes about three times the wafer of ordinary DRAM, every year HBM grows faster than conventional DRAM it takes wafers from ordinary memory and keeps that market short too, through calendar 2028.',
    breaksIf: 'The first half fails if, by its fiscal first quarter 2028 results (around December 2027), Micron has not said most of its calendar 2028 HBM supply is agreed; or if Micron reports unsold HBM or cuts HBM output and itself attributes it to customer demand. The second half fails if, before the end of calendar 2028, Micron stops expecting the DRAM industry to be supply-constrained in 2027 or 2028 while still expecting industry HBM bits to grow faster than conventional DRAM; or if Micron states that any current HBM generation needs less than about three times the wafer of DDR5 per bit. A shortage prolonged by late cleanrooms supports the claim rather than breaking it.',
    watch: ['Whether Micron says next year\'s HBM is agreed, on each December call', 'Micron\'s industry DRAM supply outlook and whether HBM still outgrows conventional DRAM', 'Any new trade ratio Micron gives for HBM4 or HBM4E', 'Whether Micron\'s ID1 fab in Idaho starts wafer output in mid 2027'],
  },
```

Notes on the test: Micron's DRAM outlook ("the industry to remain supply constrained in both years") covers DRAM as a whole, including HBM, so the falsifier uses that wording rather than inventing a "conventional only" statement Micron does not make. Blurs, named in the piece: Micron's multi-year take-or-pay strategic customer agreements now cover ordinary memory too, so "sold ahead" may stop separating HBM; and customers using less HBM per chip would ease the squeeze for a reason the claim allows (it is conditional on HBM outgrowing conventional DRAM).

## stack.ts

Layer `memory` ("Memory"), after the countertop piece:
`pieces: ['the-countertop-is-the-bottleneck', 'micron-three-times-the-wafer']`

## Glossary (heading "Chips, memory and the wiring between them")

Already present: HBM, Wafer, Die, Qualification, Gross margin, Fab. Add:
- `DRAM`: Dynamic random access memory, the working memory in every phone, laptop and server. HBM is DRAM too, stacked, so the two compete for the same factories.
- `Trade ratio`: How many wafers of ordinary DRAM a memory maker gives up to make the same number of HBM bits. Micron puts it at about three for HBM3E against DDR5, and higher for HBM4.
- `Through-silicon via`: A vertical connection drilled through a memory chip so a stack of chips can be wired top to bottom. It is what lets HBM be piled up beside a processor.
- `Cleanroom`: The dust-free hall where chips are made. A memory maker's output is limited by how much cleanroom it has, and a new one takes years.
- `DDR5`: The standard memory used in servers and PCs today, mounted on boards a few centimetres from the processor.
- `Take-or-pay agreement`: A contract where the customer pays for an agreed volume whether or not it takes delivery. Micron now signs multi-year ones for memory.

## numbers.ts

```ts
  { layer: 'memory', value: '~3×', what: 'The wafer HBM3E uses for each bit stored, against ordinary DDR5 memory, by Micron\'s estimate, restated in December 2025, when it said the ratio only increases with future generations. Every HBM bit is about three ordinary bits not made.', piece: 'micron-three-times-the-wafer', asOf: 'December 2025' },
```

## LinkedIn post (§9)

```
Each bit of AI memory uses about three times the silicon of the memory in your laptop.

Micron, one of three companies that make the stacked memory beside AI chips, says so itself, and it sells most of each year's supply before the year starts. Every wafer that goes into AI memory is a wafer ordinary memory goes without, so as AI memory grows faster than the rest, phones, laptops and servers feel the squeeze too. New memory factories take years, and Micron says one thing slowing them is energy infrastructure.

The piece covers why stacked memory eats wafers, why it is sold before it is made, and what would show the squeeze has eased.

https://thephysicallayer.fyi/journal/micron-three-times-the-wafer/

#Semiconductors #AIInfrastructure #SupplyChain
```

## Sources (each figure, with URL)

- Micron fiscal Q1 2024 prepared remarks, 20 December 2023 (downloaded PDF; q4cdn path https://s25.q4cdn.com/621799436/files/doc_financials/2024/q1/Q1-FY24-Prepared-Remarks.pdf):
  - "Across the industry, the HBM3E die is roughly twice the size of equivalent-capacity D5. Additionally, the HBM product includes a logic interface die and has a substantially more complex packaging stack that impacts yields. These factors result in HBM consuming more than two times the wafer supply as D5 to produce a given number of bits."
  - "Micron is in the final stages of qualifying our industry-leading HBM3E to be used in NVIDIA's next generation Grace Hopper GH200 and H200 platforms."
- Micron fiscal Q2 2024 earnings call, 20 March 2024, transcript: https://www.marketbeat.com/earnings/transcripts/103021
  - "Industry-wide, HBM3E consumes approximately three times the wafer supply as D5 to produce a given number of bits in the same technology node. With increased performance and packaging complexity across the industry, we expect the trade ratio for HBM4 to be even higher than the trade ratio for HBM3E."
  - "Our HBM is sold out for calendar 2024, and the overwhelming majority of our 2025 supply has already been allocated."
  - "Our HBM3E product will be part of NVIDIA's H200 Tensor Core GPUs, and we are making progress on additional platform qualifications with multiple customers."
- Micron fiscal Q1 2026 prepared remarks, 17 December 2025, transcript: https://transcripts.platformaeronaut.com/transcripts/MU-1Q26-transcript
  - "We have completed agreements on price and volume for our entire calendar 2026 HBM supply, including Micron's industry-leading HBM4."
  - "The dramatic increase in [HBM] demand is further challenging the supply environment due to the three to one trade ratio with DDR5 and this trade ratio only increases with future generations of [HBM]." (transcript renders HBM as "HVM")
- Micron fiscal Q2 2024 call, 20 March 2024 (same marketbeat transcript): "The trade ratio of 3:1, increasing demand in HBM, increased profitability of HBM is putting non-HBM part of the memory in tight supply." (not quoted in the piece; the June 2026 wording is used instead)
- Micron fiscal Q3 2026 prepared remarks, 24 June 2026: https://s25.q4cdn.com/621799436/files/doc_financials/2026/q3/Q3-FY26-Prepared-Remarks.pdf
  - Greenfield pace "constrained by several factors, including long lead time for fab construction across the world, shortage of workers with critical trade skills, complex regulations including permitting, and the need for enhanced energy infrastructure"; "HBM's growth and increasing trade ratio with every new generation further pressures non-HBM supply".
- Micron fiscal Q4 2026 prepared remarks, 30 September 2026: https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf
  - "We have completed agreements for the vast majority of our calendar 2027 HBM bit supply with significant price increases year over year, narrowing the gross margin gap with conventional DRAM."
  - Fiscal Q4 DRAM revenue $39.8bn, up 27% sequentially; bit shipments up mid-single-digit percentage; prices up high-teens percentage.
  - CMBU gross margin 83%, "flat sequentially, driven by higher pricing, offset by higher HBM mix" (not used in the piece, background for the margin point).
  - Industry DRAM bits mid-20s % in 2026, low-20s % in 2027 and 2028, "the industry to remain supply constrained in both years"; "We expect industry HBM bit shipments to grow faster than conventional DRAM through calendar 2028."
  - ID1 wafer output mid-calendar 2027; ID2 late calendar 2028; first New York fab initial wafer output calendar 2030; "Production from new DRAM and NAND fabrication facilities takes time to ramp and gradually becomes more meaningful starting a few quarters after initial output."
  - Strategic customer agreements: "multi-year take-or-pay agreements"; 26 signed.
- Micron fiscal Q4 2026 earnings call, 30 September 2026, transcript: https://stockanalysis.com/stocks/mu/transcripts/699706-q4-2026/
  - C.J. Muse (Cantor Fitzgerald) asked about HBM pricing moving closer to conventional DRAM and whether it starts 1 January. Mehrotra: "for 2026, our prices for HBM were negotiated with our customers last year"; 2027 "a large part of the volume is already sold out ... and the prices are much higher than 2026 prices".
  - Vivek Arya (BofA) asked whether 2028 pricing could stay favourable given incremental capacity or customers de-speccing. Mehrotra: clean rooms "take a long while to build"; "With HBM going from HBM3E to [HBM4] and HBM4E, and with the trade ratio that exists, that again creates headwinds with respect to supply growth." (The transcript garbles "HBM4" as "a greater max of four"; the piece quotes only "with the trade ratio that exists".)
  - Krish Sankar (TD Cowen): "there's been talk of maybe one large customer de-speccing HBM ... If those wafers get reallocated to DDR, would that increase DDR supply quite a bit?" Mehrotra: "we actually see the overall HBM demand outpacing the industry demand in 2027 as well as in 2028"; "These optimizations also have diminishing return for any further optimizations." He did not address the wafer reallocation directly (the piece says so).
- Micron fiscal Q4 2026 results press release, 30 September 2026, Form 8-K exhibit 99.1 (fiscal year ended 3 September 2026): https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm
- Micron HBM4 product page, read 7 October 2026: https://www.micron.com/products/memory/hbm/hbm4 (12-high, 36GB per stack; TSVs; logic die interfacing with the system).
- SK Hynix 2Q26 results, 29 July 2026: https://news.skhynix.com/en/q2-2026-business-results/ ("a structural shift is occurring where demand for both AI memory and conventional memory is expanding in tandem"; "a market environment where customer demand exceeds supply capabilities"; Yongin Phase 1 cleanroom opening in early 2027; LTAs with around 10 customers, not used).
- Nvidia buys HBM from SK Hynix, Micron and Samsung: Nvidia Form 10-K filed 25 February 2026, as cited in the B200 piece.

## Could not verify / left out

- "SK Hynix early lead, Micron strong second": no primary ranking found; dropped, and any share wording would trip the checker.
- Samsung struggling to qualify a generation with a major customer: widely reported from Samsung's Q3 2024 call (October 2024), but the English Samsung release and presentation I could reach do not contain the sentence. Dropped.
- A numeric trade ratio for HBM4 or HBM4E: Micron says only that the three to one ratio "only increases with future generations" (17 Dec 2025). The piece calls three a floor on that basis.
- Micron's 17 December 2025 statements are now cited to the prepared remarks transcript (platformaeronaut); Micron's own PDF did not download, so a final check against investors.micron.com is still worth doing.
- Sumit Sadana's 25 June 2024 remark on 2025 pricing: not confirmed from a transcript, not used. The piece says 2025 was "allocated", Micron's March 2024 word.
- How long an HBM qualification takes: no primary figure. Not stated.
- Micron's FY2026 10-K was not yet on EDGAR when checked; not used.

## Fact-check fixes (7 October 2026)

Trade ratio restated with Micron's 17 Dec 2025 wording; 2025 described as "allocated", not agreed; Micron's own "further pressures non-HBM supply" (June 2026) quoted, with the stronger "stays short through 2028" labelled as my reading; SK Hynix paraphrase fixed to "exceeds supply capabilities" (market, 29 Jul 2026 release); falsifier first half dated "by its fiscal Q1 2028 results around December 2027"; DRAM revenue flagged as including HBM, with Micron's "tight DRAM industry conditions"; reconciliation sentence with the countertop piece added; 17 Dec 2025 source replaced. Piece trimmed to clear the word-count warning.
