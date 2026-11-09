# Gap scout: map layer 06, Memory (30 Oct 2026)

Scout notes for a new deep piece on HBM. Every figure is marked PRIMARY (company spec page, filing, results release, newsroom, standards body) or SECONDARY (press, TrendForce, analysts). Secondary items are leads only and stay out of the body.

## Already taken (must not be this piece's mechanism or claim)

- the-chip-supply-chain.md, its sidecar, calls/micron.md and claims.ts `micron-three-times-the-wafer` and `the-chip-supply-chain` own: Micron sells most of each year's HBM ahead; each HBM bit takes about three times the wafer of DDR5, so HBM starves conventional DRAM through 2028; Micron's fab dates (ID1 mid 2027, ID2 late 2028, New York 2030); Micron's in-house HBM4 base die (one line).
- The chip piece also carries one unsourced line, "Inference is bound by memory bandwidth". It never shows it. This piece does.
- UNCAPPED-RESULTS A14 ("HBM now queues at TSMC's logic fabs too") was held on 29 Oct because Micron's HBM4 base die is in-house and SK hynix-TSMC was only a 2024 plan. That is why the spine below is not "HBM queues at TSMC". It is "the buyer now designs the memory", which rests on Nvidia's, Micron's and Samsung's own 2026 words.

## Verdict: NEW DEEP PIECE

1. Mechanism the site lacks: the memory wall (inference speed and users per chip set by HBM bandwidth and capacity, not by compute) and its consequence, HBM turning from a standard part into one built to the buyer's design. No piece explains either. Distinct from "sold ahead" (the chip piece) and from the trade ratio (Micron claim).
2. Primary sources: Nvidia and AMD spec pages and decks; Nvidia's technical blog on decode being memory bound; JEDEC's HBM4 release; SK hynix, Samsung and Micron releases, results and 10-K; Nvidia's NVHBM blog.
3. Beyond the headline: since the A100, peak maths per chip has grown about twelve times faster than memory bandwidth; Rubin is the first step that held the ratio, and it did so on HBM4; the next step moves the buyer's memory controller into the memory stack, which makes HBM a per-customer part with a per-customer qualification.

Spine: AI answers are paced by how fast memory feeds the chip, so memory has become the part chip makers compete on, and from HBM4E the biggest buyer designs the bottom of the memory stack itself, which turns a standard part into a custom one.

## 1. Memory, not maths: primary statements

| # | Fact | Source | Date | Type |
|---|---|---|---|---|
| 1.1 | Decode phase: "this is a memory-bound operation"; "Model execution is frequently memory-bandwidth bound", "in particular, bandwidth-bound in the weights"; after all optimisations "it's still very likely to be memory bound" | Nvidia Technical Blog, "Mastering LLM Techniques: Inference Optimization", Verma and Vaidya, https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | 17 Nov 2023 | PRIMARY (company) |
| 1.2 | KV cache "Growing linearly with batch size and sequence length"; Llama 2 7B, 16-bit, batch 1, 4,096 tokens: "~2 GB" | same | 17 Nov 2023 | PRIMARY |
| 1.3 | AI platforms' "value proposition is enhanced by the performance and capacity of memory and storage. Running an AI application on a platform with greater memory capability enables more scalable growth in usage" | Micron Q4 FY26 prepared remarks, https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf | 30 Sep 2026 | PRIMARY |
| 1.4 | AMD slide: "Highest memory bandwidth & capacity drives performance" (MI350 rack); MI355X "Supports up to 520B Parameter AI Model" | AMD Advancing AI 2025 distribution deck, pp. 22, 88, https://www.amd.com/content/dam/amd/en/documents/corporate/events/advancing-ai-2025-distribution-deck.pdf | 12 Jun 2025 | PRIMARY |
| 1.5 | SK hynix VP Hosik Kim: CPU and GPU-centric architectures "face a bottleneck known as the 'memory wall'" | SK hynix newsroom, OCP Global Summit 2026, https://news.skhynix.com/en/ocp-global-summit-2026/ | 16 Oct 2026 | PRIMARY (company) |
| 1.6 | "in low-latency, small-batch inference, memory bandwidth can limit performance"; bandwidth "has not kept pace" with compute | SK hynix newsroom guest column by Raja Koduri (OXMIQ Labs), https://news.skhynix.com/en/ai-ecosystem-series-ep4/ | 21 Oct 2026 | SECONDARY (guest author on a company site; not used as body fact) |
| 1.7 | Blackwell Ultra: "288 GB HBM3E ... enabling 300B+ parameter models to reside entirely on-chip without offloading" | Nvidia Technical Blog, "Inside NVIDIA Blackwell Ultra", https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/ | 22 Aug 2025 | PRIMARY |
| 1.8 | Micron: "AI context memory storage used for KV cache offload" expanding SSD market (counter-evidence beat) | Micron Q4 FY26 prepared remarks | 30 Sep 2026 | PRIMARY |
| 1.9 | SK hynix shows HBF (high bandwidth flash) as a capacity tier; "HBM's high-speed processing can be leveraged in environments where fast response times are critical" | SK hynix OCP 2026 newsroom | 16 Oct 2026 | PRIMARY |

My arithmetic (labelled in piece): a 70bn-parameter model at 8 bits is about 70 GB; at 8 TB/s one full read takes about 9 ms, so one stream at batch one tops out near 110 words a second however fast the maths. Illustration only, ignores KV cache and overlap.

## 2. The spec sheets (chart 1 and chart 2)

Compute is peak dense tensor maths in the smallest number format each chip supports for AI. Nvidia pages quote sparse figures; dense is half (Nvidia HGX page: "Dense is ½ sparse spec shown").

| Chip | Year | Memory | Bandwidth | Peak dense, smallest format | Source | Type |
|---|---|---|---|---|---|---|
| A100 80GB SXM | 2020 | 80 GB HBM2e | 2,039 GB/s | 312 TFLOPS FP16 (624 with sparsity) | nvidia.com/en-us/data-center/a100/ | PRIMARY |
| H100 SXM | 2022 | 80 GB | 3.35 TB/s | 1,979 TFLOPS FP8 (3,958 sparse); blog table rounds to 2 PF | nvidia.com/en-us/data-center/h100/; Blackwell Ultra blog Table 2 | PRIMARY |
| H200 SXM | 2024 | 141 GB HBM3e | 4.8 TB/s | same as H100 (3,958 FP8 sparse) | nvidia.com/en-us/data-center/h200/ | PRIMARY |
| Blackwell (B200/GB200 GPU) | 2024 | 192 GB HBM3E | 8 TB/s | 10 PF NVFP4 dense (20 sparse) | Blackwell Ultra blog Table 2 (22 Aug 2025). DGX B200 page: 1,440 GB, 64 TB/s, 72 PF FP4 dense for 8 GPUs, i.e. 180 GB and 9 PF each | PRIMARY |
| Blackwell Ultra (B300) | 2025 | 288 GB HBM3E, eight 12-high stacks, 8,192-bit | 8 TB/s | 15 PF NVFP4 dense | Blackwell Ultra blog | PRIMARY |
| Rubin (Vera Rubin NVL72) | 2026 | 288 GB HBM4 | 19.2 TB/s | 35 PF NVFP4 training, dense; 50 PF NVFP4 inference, sparse | nvidia.com/en-us/data-center/vera-rubin-nvl72/ (footnotes 2 sparse, 3 dense); page says "Available Now" | PRIMARY |
| AMD MI300X | 2023 | 192 GB HBM3 | 5.3 TB/s | n/a | amd.com MI300X page, endnote MI300-05A (17 Nov 2023) | PRIMARY |
| AMD MI325X | 2024 | 288 GB announced Jun 2024 (6 TB/s); shipped spec not checked | | | AMD release 2 Jun 2024 | PRIMARY, not used |
| AMD MI355X | 2025 | 288 GB HBM3E | 8 TB/s | 10 PF MXFP4 | AMD deck p. 23 | PRIMARY |
| AMD MI400 | 2026 | 432 GB HBM4 | 19.6 TB/s | 40 PF FP4 | AMD deck p. 95, "Specs based on engineering projections" | PRIMARY (projection) |

Derived (my arithmetic): A100 to Rubin, compute x112 (312 TF to 35 PF), bandwidth x9.4 (2.039 to 19.2 TB/s). Maths per byte: A100 153, H100 about 597, Blackwell 1,250, Blackwell Ultra 1,875, Rubin about 1,823. Rubin is the first generation where the ratio did not rise. Memory per chip H100 80 GB to Rubin 288 GB, 3.6 times.

Caveat for the piece: halving the number format also halves the bytes per weight, so in numbers moved the gap is narrower than the raw ratio. The direction holds at fixed format too for A100 to Blackwell Ultra (FP16 dense 312 TF to 2.5 PF, x8, against bandwidth x3.9), and Rubin at BF16 dense (4 PF) actually narrows it.

V100 dropped: nvidia.com no longer carries its spec page.

## 3. HBM4 and the base die

| # | Fact | Source | Date | Type |
|---|---|---|---|---|
| 3.1 | JEDEC JESD270-4 HBM4: 2048-bit interface, up to 8 Gb/s, up to 2 TB/s per stack; 32 channels (16 in HBM3); 4, 8, 12, 16-high; 24 or 32 Gb dies; 64 GB cube (32Gb 16-high); backward compatible with HBM3 controllers | JEDEC release as reprinted by StorageNewsletter, https://www.storagenewsletter.com/2025/04/17/jedec-and-industry-leaders-collaborate-to-release-jesd270-4-hbm4-standard/ (jedec.org, BusinessWire and HPCwire returned 403; not bypassed) | 16-17 Apr 2025 | PRIMARY via reprint |
| 3.2 | SK hynix HBM4 development complete: "2,048 I/O terminals, double from the previous generation"; over 10Gbps against the JEDEC 8Gbps; Advanced MR-MUF | SK hynix newsroom, https://news.skhynix.com/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/ | 12 Sep 2025 | PRIMARY |
| 3.3 | SK hynix and TSMC MOU: SK hynix plans to "adopt TSMC's advanced logic process for HBM4's base die"; "produce customized HBM that meets a wide range of customer demand for performance and power efficiency"; HBM4 "slated to be mass produced from 2026" | SK hynix newsroom, https://news.skhynix.com/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership/ | 19 Apr 2024 | PRIMARY (a plan; no later SK hynix release I could open confirms TSMC makes its shipping HBM4 base die) |
| 3.4 | Samsung Q1 2026: "industry's first mass product sales of HBM4 ... for NVIDIA's Vera Rubin platform"; Foundry "targeting earnings improvement on increased HBM4 base-die supply" | Samsung newsroom, https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2026-results | 30 Apr 2026 | PRIMARY |
| 3.5 | Samsung Q2 2026: "shipping the industry's first HBM4E samples to major customers"; Foundry earnings "driven by HBM base-die demand"; H2 plan to "expand sales of LPU and base-die products based on the 4nm process" | https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results | 30 Jul 2026 | PRIMARY |
| 3.6 | Samsung Q3 2026: Foundry "notable revenue and earnings improvement on HBM base-die sales growth"; memory "significantly scaled up sales of HBM4" | https://news.samsung.com/global/samsung-electronics-announces-third-quarter-2026-results | 29 Oct 2026 | PRIMARY |
| 3.7 | Micron 10-K: HBM4 base logic die and DRAM core dies "designed and manufactured in-house"; "HBM4E customization options offer us further differentiation opportunities and even deeper R&D engagement with customers"; HBM4E volume ramp calendar 2027 on 1-gamma | Micron Form 10-K, https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm (read via WebFetch, first 100k characters) | 9 Oct 2026 | PRIMARY |
| 3.8 | Micron: "working with NVIDIA on the industry's first custom-HBM4E implementation, NVHBM, to be adopted on next generation of GPUs and NVLink Fusion platforms" | Micron Q4 FY26 prepared remarks | 30 Sep 2026 | PRIMARY |
| 3.9 | Nvidia NVHBM: "Traditional HBM architectures place the memory controller on the XPU die"; NVHBM "integrates NVIDIA's custom memory controller into the HBM base die"; up to 30% more bandwidth, 15% lower HBM power, up to 25% more XPU area, against standard HBM4E; "available from multiple memory providers"; Annapurna Labs first, "starting with Trainium4"; no date | Nvidia blog, Jesse Clayton, https://blogs.nvidia.com/blog/2026/08/26/nvlink-fusion-nvhbm/ | 26 Aug 2026 | PRIMARY |
| 3.10 | Nvidia buys memory from "SK Hynix Inc., Micron Technology, Inc., and Samsung"; extended lead times of more than 12 months; deposits and long-term supply agreements | Nvidia Form 10-K, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm | 25 Feb 2026 | PRIMARY |

Leads only (SECONDARY): SK hynix HBM4 base die on TSMC 12nm-class in mass production, and SK hynix weighing Intel for HBM4E base dies (TrendForce, 31 Aug 2026); TSMC N12FFC+/N5 base die offer (Tom's Hardware 2024); Micron HBM4E base die to be made by TSMC for standard and custom (press on Micron's Sep 2025 call; Micron's own text I could open does not name TSMC); Samsung custom HBM sampling from 2027 (fnnews 2026); Samsung HBM revenue share figures (press; never body). TSMC 2Q26 and 3Q26 transcripts returned HTML to my client; not bypassed, so no TSMC remark on base dies is used.

## 4. Where it is made

| # | Fact | Source | Date | Type |
|---|---|---|---|---|
| 4.1 | M15X, Cheongju: "expand production capacity of the next-generation DRAM including HBM"; next to M15, "which has been expanding TSV capabilities"; long-run investment over 20 trillion won | SK hynix newsroom, https://news.skhynix.com/en/sk-hynix-to-produce-dram-from-m15x-in-cheongju/ | 24 Apr 2024 | PRIMARY |
| 4.2 | Q3 2026: will "ramp up M15X to maximum capacity by the end of the year" "to increase HBM4 production"; HBM4 to pass HBM3E in volume and revenue in Q4 2026; LTAs for more than 50% of 2027 to 2028 capacity with 14 customers; demand over supply "through 2030"; Yongin Phase 1 full operation next year | SK hynix newsroom, https://news.skhynix.com/en/q3-2026-business-results/ | 28 Oct 2026 | PRIMARY |
| 4.3 | P&T7, Cheongju: "a dedicated advanced packaging fab essential for manufacturing AI memory products such as HBM"; wafer test line by October 2027, wafer level packaging by February 2028; fifth SK hynix production site in Cheongju | SK hynix newsroom, https://news.skhynix.com/en/skhynix-chungju-pt7/ | 22 Apr 2026 | PRIMARY |
| 4.4 | West Lafayette, Indiana: $3.87bn advanced packaging plant for HBM; mass production "in the second half of 2028"; first of its kind in the US | SK hynix newsroom, https://news.skhynix.com/sk-hynix-signs-investment-agreement-of-advanced-chip-packaging-with-indiana/ | 3 Apr 2024 | PRIMARY |
| 4.5 | Micron Singapore HBM advanced packaging facility: "initial output expected in early calendar 2027"; Tongluo, Taiwan, meaningful shipments mid 2027 | Micron Q4 FY26 prepared remarks | 30 Sep 2026 | PRIMARY |
| 4.6 | SK hynix's HBM3E-era base die was its own; HBM4 moves to a logic process (MOU, 3.3) | as above | | PRIMARY plan |

Not verified on primary sources: where Samsung assembles HBM (Cheonan and Onyang are press); where SK hynix assembles HBM today (P&T7 release does not say); any HBM output share by country. Concentration is therefore told as "two of the three makers are Korean and their new HBM lines are in Korea", not as a share.

## 5. Claim (proposed, not yet in claims.ts)

id `memory-not-maths`, dated 2026-10-31: by 31 Dec 2027 at least two of the three makers say in their own results, filings or newsroom that they are in volume production or shipping in volume HBM with a customer-specific base die. Not near-certain: Micron's HBM4E ramps in 2027 and NVHBM has no date; Samsung has said nothing primary on custom timing; SK hynix's own words are a 2024 plan. Does not duplicate any Micron claim (no sold-ahead, no trade ratio, no fab dates).

## 6. Not used, and why

- HBM "five to six times the bandwidth and cost" (glossary line): no source found; suggest the glossary drop the price half.
- SK hynix "HBM requires at least twice as large capabilities" (24 Apr 2024): a wafer-intensity point, too close to Micron's trade ratio claim.
- Market shares: press only.
