# Sidecar: ten-thousand-chips-one-thought (deep piece, cluster 9)

Cluster 9, "How ten thousand chips talk: copper, glass, lasers and mirrors". Drafted 30 Oct 2026 to BRIEF-DEEP.md, matching the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/ten-thousand-chips-one-thought.md` (draft: true). Kept outside `src/content/journal/`. Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "How ten thousand chips talk: the glass stays, the plug is bought again" (13 words). Subject: the AI cluster network, named in title, summary, open and thesis line.
- Thesis line: "In the AI network, the glass stays and the plug is bought again."
- Top layer (open, analogy, How it works, The number that matters): about 476 words, about 8 figures (800 gigabits, 1.6 terabits, fifteen times, mid-2027, October, September, three distances), 0 company financial figures. Analogy about 69 words.
- Investor layer: about 2,487 words before the exposure map (tables included). Exposure map about 124 words with the exact disclaimer pair ("Co-packaged engines" merged into "Inside the plug"; "no view on chip design" dropped).
- `brand/check-piece.py` on a scratch copy: 0 failures, 0 warnings. 0 em or en dashes.
- Category changes from Explainer to Analysis, because the deep piece now carries claims and a new one.

## Frontmatter notes

- Slug kept: `ten-thousand-chips-one-thought` (live Explainer; in `READING_PATH` in `src/config.ts` line 49, which needs no change, and in `brand/linkedin-posts.md`).
- `date: 2026-09-04` is a placeholder (the Explainer's date). It becomes the real publish time at go-live.
- `cover: "/covers/network.svg"` (existing) until a new cover is drawn; proposal below.
- Tags unchanged: networking, optics, the-stack.

## Sections and anchors, in order

Top: How it works; The number that matters. Investor: The mechanism in depth (#ten-thousand-chips-one-thought; distance table and layer-by-layer bill of materials); The switch: Broadcom on both sides (#broadcom-wins-either-way); The translator: Marvell's optical DSP (#marvell-collects-the-toll); The laser: why silicon cannot make it (#lumentum-makes-the-light); Optics onto the switch, lasers left in a plug (#the-optics-you-cannot-unplug); The glass: Corning (#corning-lays-the-glass); The mirrors: Google's optical circuit switches (#google-steers-the-light); Between sites: Microsoft's Fairwater (#fairwater-spans-two-states); Claims on record; What would prove me wrong; Research notes; exposure map; sources.

## Thesis and how it treats the old claims and pieces

The network is priced by distance: copper inside the rack (scale-up), light through plugs and fibre across the hall (scale-out), dedicated fibre between sites (scale-across). Within scale-out, the parts that read or make the signal (switch silicon, DSP, laser) are bought again at each speed step; the parts that only carry or steer light (fibre, mirror switches) stay. Co-packaged optics removes the plug's DSP but both Nvidia and Broadcom kept the lasers in removable modules, and Nvidia's own Vera Rubin reference design picks the pluggable switch.

"Where I was wrong" notes, all carried openly in Claims on record (claims and breaksIf quoted word for word, untouched):
- marvell-collects-the-toll: holding on the co-packaged leg for scale-out (Nvidia reference design picks pluggable; Murphy, 27 Aug 2026). From the co-packaged optics sidecar, carried openly: SPIL's 15x target is the main way that leg could break; Hock Tan's line "We're now the leader in leading edge optical DSPs" (2 Sep 2026, third-party transcript) means the DSP is contested. Plus the Marvell note's correction: the US$1 billion prepayments were not tied to optical DSPs.
- broadcom-wins-either-way: holding but the stay half has shrunk (networking 27% of AI revenue, quarter to 2 Aug 2026, from almost 40%). Correction from the note: Anthropic accesses Google's TPU design through Broadcom (8-K, 6 Apr 2026).
- corning-lays-the-glass: holding, and now tested on a newer fact: Q3 2026 segment margin 22.4% on sales up 44% (8-K, 27 Oct 2026). Correction: the 8-K of 6 May 2026 (Item 3.02) shows the US$500m bought two warrants, a pre-funded one over 3m shares and a traditional one over 15m shares at US$180; the US$1.0bn customer deposit that secures supply is from the Q2 10-Q, which values the second warrant at US$296m and deducts it from revenue. The note says this means scarcity is shared with the largest buyer, not kept.
- lumentum-makes-the-light: holding (still shipping behind demand, 11 Aug 2026). From the CPO sidecar, carried openly: SPIL's 15x bears on the silicon photonics leg (co-packaged engines use continuous lasers, not EMLs), but does not route around the laser: Lumentum said on its 11 Aug 2026 call it was further behind still on high-power lasers for co-packaged optics. Correction from the note: the US$2bn bought 2,876,415 convertible preferred shares.
- ten-thousand-chips-one-thought (Explainer, no claim): the body openly withdraws its "forty to sixty cents of network per chip dollar" (no primary source found) and replaces it with Nvidia's own Q1 FY2027 split (US$14.8bn networking, US$60.4bn compute), stated as Nvidia-only.

Draft claims not carried as claims (none was ever live): the CPO draft's claim becomes the core of the new deep claim (with the laser-on-package limb added); the Google OCS spread claim and the Fairwater single-campus claim go into the new claim's watch list.

## Proposed claims.ts change (existing entries untouched apart from merge metadata)

The type already has `date` and `home`. At merge, the four live entries gain only `home: 'ten-thousand-chips-one-thought'`; their `date` values are already set. `claim`, `breaksIf` and `watch` are not touched. Tommy should approve the `home` additions explicitly.

New entry:

```ts
  {
    id: 'the-plug-stays',
    home: 'ten-thousand-chips-one-thought',
    claim: 'Between the racks of an AI cluster the optical plug stays the default through 2028: switches with co-packaged optics keep their lasers in removable front-panel modules, and Nvidia\'s reference designs for its newest systems keep specifying pluggable switches, as both Vera Rubin designs do today, with the Spectrum-X SN6600-LD and the InfiniBand Quantum-X800 Q3400-RD.',
    breaksIf: 'By the end of 2028, either of Nvidia\'s DGX SuperPOD reference architectures for its newest systems specifies a co-packaged optics switch as the default or only option for the compute fabric, or Nvidia or Broadcom says most of the AI switches it ships carry co-packaged optics, or either ships a co-packaged AI switch as standard whose lasers are fixed to the package rather than in replaceable modules.',
    watch: ['Which switch the next DGX SuperPOD reference architectures specify (for Vera Rubin: pluggable SN6600-LD in the Spectrum-X design, 15 Sep 2026; pluggable Q3400-RD Quantum-X800 in the InfiniBand design), and Feynman\'s "Spectrum-class optical scale-out"', 'SPIL co-packaged optical engine capacity against the 15x mid-2027 target (Nvidia, 21 Oct 2026)', 'Any Nvidia or Broadcom statement of the shipped mix of co-packaged and pluggable switches', 'Laser shortage statements from Lumentum and Broadcom, and Lumentum\'s fiscal 2027 annual report on optical circuit switch buyers other than Google', 'Whether a second cloud giant states optical circuit switches join chips in a production AI cluster, and whether any lab says a named model was trained across Fairwater sites'],
  },
```

Known limit (fact-check, 30 Oct 2026): hyperscalers deploying Broadcom's Tomahawk 6 Davisson in their own designs are tested only through the shipped-mix limb (an Nvidia or Broadcom statement that most AI switches shipped are co-packaged); no reference-design limb covers them.

Why it is a real test: Nvidia already sells Spectrum-6 both ways, is funding a 15x then about 30x rise in co-packaged engine capacity, and lists optical scale-out in Feynman (undated). A Feynman reference design picking a co-packaged switch before end-2028 is plausible, so the claim can fail. The causal "so the network is bought again at the plug" sits in the thesis, not the claim, since nothing primary measures replacement rates.

The id `the-plug-stays` avoids colliding with the existing slug-ids; if the convention is that a deep piece's new claim id is its slug, use `ten-thousand-chips-one-thought` instead (no existing claim has that id, since the Explainer had none).

## Redirect map

| Old URL | Redirect to |
|---|---|
| /journal/marvell-collects-the-toll/ | /journal/ten-thousand-chips-one-thought/#marvell-collects-the-toll |
| /journal/broadcom-wins-either-way/ | /journal/ten-thousand-chips-one-thought/#broadcom-wins-either-way |
| /journal/corning-lays-the-glass/ | /journal/ten-thousand-chips-one-thought/#corning-lays-the-glass |
| /journal/lumentum-makes-the-light/ | /journal/ten-thousand-chips-one-thought/#lumentum-makes-the-light |
| /journal/the-optics-you-cannot-unplug/ | /journal/ten-thousand-chips-one-thought/#the-optics-you-cannot-unplug |
| /journal/google-steers-the-light/ | /journal/ten-thousand-chips-one-thought/#google-steers-the-light |
| /journal/fairwater-spans-two-states/ | /journal/ten-thousand-chips-one-thought/#fairwater-spans-two-states |

The three drafts were never live, but all three are scheduled (the-optics-you-cannot-unplug for 7 Dec, LinkedIn 8 Jan, per UNCAPPED-RESULTS.md), so their redirects are listed in case any post or link was prepared. Their publish tasks need pausing or removing at merge (Tommy's go needed). At merge, the four live originals and the three drafts go verbatim into `research-build/archive-pieces/` and the drafts leave `src/content/journal/`.

## stack.ts

Layer `network` ("The network between chips"). At merge:
`pieces: ['ten-thousand-chips-one-thought']`
(removing marvell-collects-the-toll, broadcom-wins-either-way, corning-lays-the-glass, lumentum-makes-the-light). The drafts' suggested additions are void. No new layer: scale-across stays inside `network`.

## Glossary (src/pages/glossary.astro, "Chips, memory and the wiring between them")

New (checked absent 30 Oct 2026):
- Scale-across: Linking AI data centres in different places, sometimes hundreds of kilometres apart, so they can work on one training job. Only the least talkative work can cross, because light takes about five microseconds per kilometre of fibre.
- Optical circuit switch: A box of tiny tilting mirrors that bounces light from one fibre into another without reading it. It uses almost no power and works at any data rate, but takes milliseconds to change, so it sets the shape of a network rather than routing each packet. Google's is called Palomar.
- Optical engine: The small assembly that turns a chip's electrical signal into light and back. In co-packaged optics it sits on the switch package.
- External laser source: A removable front-panel module holding the lasers that feed co-packaged optics, so the part most likely to wear out can still be replaced by hand. The OIF standard form is ELSFP.
- Tensor parallelism: Cutting each calculation across several chips, which must swap results many times a step. It needs the shortest links, so it stays inside one building.
- Data parallelism: Giving each group of chips its own copy of the model and different data, then averaging what they learned once a step. It is the work that can cross between sites.
- AI WAN: Microsoft's wide area network built only to carry AI training traffic between distant data centres, such as its Fairwater sites.
- Reference architecture: A vendor's published blueprint for building a cluster from its products, naming which switch, cards and cabling to use.

Check, and add only if absent as a defined term: Co-packaged optics (CPO) (the word appears once in the glossary today), NVLink, TPU.
Already present: Scale-up, Scale-out, Optical transceiver, DSP, EML, Indium phosphide, Silicon photonics, Linear pluggable optics, Switch chip, Ethernet, Gross margin.

## numbers.ts (physical only)

New:
```ts
  { layer: 'network', value: '<3%', what: 'Share of a Google TPU v4 pod\'s power taken by its whole optical switching layer, mirror switches, plugs and fibre included, for 4,096 chips. Google\'s figure for cost is under 5%.', piece: 'ten-thousand-chips-one-thought', asOf: '2023' },
  { layer: 'network', value: '~5 microseconds per km', what: 'How long light takes to cover each kilometre of glass fibre. Across the roughly 1,000 km between Microsoft\'s Fairwater sites that is at least 5 ms one way.', piece: 'ten-thousand-chips-one-thought', asOf: '2026' },
  { layer: 'network', value: '15×', what: 'Rise in co-packaged optical engine capacity SPIL targets by mid-2027, with another doubling by the end of 2028, according to Nvidia. A target, not built capacity.', piece: 'ten-thousand-chips-one-thought', asOf: 'October 2026' },
```
Existing entries needing Tommy's decision at merge (not edited):
- `102.4 Tb/s` (broadcom-wins-either-way, asOf 'June 2025'): its "about 128,000 AI chips" is not Broadcom's own text. It appears in Broadcom's release of 12 March 2026 only as a quote from an analyst (Bob Wheeler, LightCounting). Broadcom's own figure is "100,000+ XPUs in a two-tier scale-out network" (3 June 2025), which the deep piece uses. Reword the entry to "more than 100,000 AI chips", keep asOf 'June 2025', repoint `piece`.
- `16×` (corning-lays-the-glass): "according to Corning", but I could not find the Corning primary source or date on 30 Oct 2026. Not used in the deep piece. Keep only if Tommy has the source; otherwise drop.
- `~2 m` (corning-lays-the-glass): no primary source found; the deep piece says "a few metres". Suggest softening the value to "a few metres" or dropping.
- `800G → 1.6T` (lumentum-makes-the-light): fine; repoint `piece`.
All four existing network entries need `piece` repointed to ten-thousand-chips-one-thought (the redirects would also work).

## LinkedIn post (§9)

```
Google's whole optical layer, mirror switches, plugs and fibre, came to under 3 per cent of a 4,096-chip AI pod's power.

The parts of an AI network that only carry or steer light, the fibre and the mirrors, last for years. The parts that make and read it, the lasers and the chips inside each plug, are bought again every time the chips get faster. Nvidia and Broadcom now build optics onto their switches, but both kept the lasers in a plug you can pull out by hand, and Nvidia's own blueprint for its newest systems still picks the plug-in switch.

The piece covers the three distances AI chips talk across, the bill of materials layer by layer, the claims I have on record and where I was wrong.

https://thephysicallayer.fyi/journal/ten-thousand-chips-one-thought/

#AIInfrastructure #Networking #Optics
```
This URL already has a live post (September). A new cover means bumping `OG_VERSION` and running Post Inspector (§8 step 6).

## Cover proposal (not drawn)

`/covers/ten-thousand-chips-one-thought.svg` (network.svg stays for the archive). A cross-section from left to right in three bands labelled by distance: a rack with short amber copper strands; a hall where a single blue fibre runs along a ceiling tray, with a small plug at each end drawn open to show one amber laser dot; and a long thin line fading to a second building at the far right. Above the switch box, one plug is drawn half pulled out, the laser still glowing. Caption in letter-spaced grey: "THE GLASS STAYS. THE PLUG IS BOUGHT AGAIN." Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Edits other drafts and files need (not made)

- `src/data/numbers.ts`: the four repoints and the 128,000 date fix above.
- The live Broadcom piece (archived verbatim, so not edited) says two tiers "can connect about 128,000 AI chips", sourced to 3 June 2025. That figure is an analyst's quote (Bob Wheeler, LightCounting) in Broadcom's 12 March 2026 release, not Broadcom's text; Broadcom's own 3 June 2025 figure is "100,000+ XPUs". The deep piece uses Broadcom's own figure.
- `src/content/journal/the-countertop-is-the-bottleneck.md` and any piece linking `/journal/ten-thousand-chips-one-thought/`: the URL survives unchanged. The Explainer's closing link to "the next piece" (the countertop) is not carried; cluster 10 will absorb that piece, so READING_PATH order still works.
- Cluster 2 / cluster 1 pieces linking `fairwater-spans-two-states` (if any are drafted later) should link `/journal/ten-thousand-chips-one-thought/#fairwater-spans-two-states`.
- `brand/linkedin-posts.md`: the three drafts' prepared posts (CPO, Google, Fairwater) are void; replace with the one post above.
- `src/data/claims.ts` watch item for marvell-collects-the-toll ("Whether 1.6T links keep a DSP on board") is untouched; the deep claim's watch list carries the CPO evidence.

## Sources, every one with date

Re-opened by me on 30 Oct 2026:
- Corning Q3 2026 results, 8-K Exhibit 99.1, 27 Oct 2026 (Optical Communications sales 2,379 / 2,072 / 1,652 and net income 532 / 438 / 295, US$m, Q3 26 / Q2 26 / Q3 25; Enterprise Networks +84%; capex 1,299 vs 850 nine months; expansions "backed by long-term customer agreements that share the cost and risk"): https://www.sec.gov/Archives/edgar/data/0000024741/000002474126000273/glw-20261027xex99xq32026.htm
- Nvidia, supply chain capacity release, 21 Oct 2026 (SPIL 15x optical-engine capacity for CPO by mid-2027, another doubling by end-2028; no lasers mentioned): https://nvidianews.nvidia.com/news/nvidia-and-supply-chain-partners-expand-capacity-to-accelerate-ai-infrastructure-buildout
- Nvidia Q2 FY2027 results release, 26 Aug 2026 (Spectrum-6 "supporting both pluggable and co-packaged optics"; Data Center US$89.0bn): https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/
- Nvidia CFO commentary Q1 FY2027 (data centre compute US$60.4bn, networking US$14.8bn, "under the previous sub-markets"): https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q127/Q1FY27-CFO-Commentary.pdf ; Q2 FY2027 commentary no longer gives the split: https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf
- Nvidia GTC 2026 live updates, 16 Mar 2026 (Kyber "for both copper and co-packaged optics scale-up"; Feynman "Spectrum-class optical scale-out"; no dates): https://blogs.nvidia.com/blog/gtc-2026-news/
- Nvidia GB200 NVL72 product page (72-GPU NVLink domain, 130 TB/s), read 30 Oct 2026: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- Broadcom, Tomahawk 6 in production volume, 12 Mar 2026 (shipping in volume; the 128K two-tier figure there is an analyst quote, Bob Wheeler of LightCounting, not used), wire copy: https://mfn.se/all/a/broadcom/broadcom-now-shipping-worlds-first-102-4-tbps-switch-in-production-volume-efdafd93

From the cluster's notes and sidecars (primary, verified there, not re-opened today):
- Marvell: 8-K Ex 99.1 and 10-Q for the quarter to 1 Aug 2026 (data centre US$2.17bn, 79%), filed 27 and 28 Aug 2026; call 27 Aug 2026 (Murphy on pluggables); Celestial AI completion, 2 Feb 2026: https://investor.marvell.com/news-events/press-releases/detail/1005/marvell-completes-acquisition-of-celestial-ai ; prepayment correction per `src/content/calls/marvell.md`.
- Broadcom: Q3 FY2026 8-K Ex 99.1, 2 Sep 2026: https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm ; call 2 Sep 2026 (73% custom, 27% networking, Kawwas on Tomahawk 6 and InP lasers; Hock Tan's optical DSP line) via third-party transcript: https://www.webull.com/news/15511095937917952 ; 8-K 6 Apr 2026 (Anthropic via Google TPU) per `src/content/calls/broadcom.md`; Tomahawk 6 announcement 3 Jun 2025; TH6-Davisson release 8 Oct 2025 (wire copy): https://mfn.se/all/a/broadcom/broadcom-announces-tomahawk-r-6-davisson-the-industrys-first-102-4-tbps-ethernet-switch-with-co-packaged-optics-824cfbb5
- Lumentum: 8-K and joint release with Nvidia, 2 Mar 2026 (2,876,415 preferred shares at US$695.31); results and call 11 Aug 2026 (GAAP gross margin 33.3% to 47.4%, behind demand on EMLs and further behind on CPO lasers, 200G over a quarter of EML revenue, Greensboro early 2028); 10-K filed 17 Aug 2026 (OCS "more than $90.0 million"): https://www.sec.gov/Archives/edgar/data/1633978/000162828026057358/lite-20260627.htm
- Corning: Q2 2026 results 28 Jul 2026 (US$2.07bn, 21.1%); 8-K 6 May 2026, Item 3.02 (US$500m for two warrants: pre-funded over 3m shares, traditional over 15m at US$180); Q2 10-Q filed 29 Jul 2026 (US$1.0bn deposit; second warrant valued US$296m, deducted from revenue) per `src/content/calls/corning.md`; Meta 27 Jan 2026, Amazon 8 Jun 2026.
- Nvidia DGX SuperPOD Vera Rubin reference architecture, InfiniBand version (Q3400-RD Quantum-X800, pluggable), per fact-check 30 Oct 2026: https://docs.nvidia.com/dgx-superpod-reference-architecture-with-dgx-vera-rubin-nvl72.pdf
- Nvidia CPO: announcement 18 Mar 2025 (3.5x; lists Lumentum as a silicon photonics ecosystem partner, not as a laser supplier, so not used for that): https://nvidianews.nvidia.com/news/nvidia-spectrum-x-co-packaged-optics-networking-switches-ai-factories ; blog 27 Mar 2025: https://developer.nvidia.com/blog/a-new-era-in-data-center-networking-with-nvidia-silicon-photonics-based-network-switching/ ; blog 26 Aug 2025 (soldered engines, swappable lasers): https://developer.nvidia.com/blog/how-industry-collaboration-fosters-nvidia-co-packaged-optics ; DGX SuperPOD Vera Rubin reference architecture (created 15 Sep 2026): https://docs.nvidia.com/dgx-superpod-spectrum-x-reference-architecture-with-dgx-vera-rubin-nvl72.pdf ; SN6000 manual: https://networking-docs.nvidia.com/sn6000hw/introduction
- OIF ELSFP implementation agreement, 8 Aug 2023: https://www.businesswire.com/news/home/20230808055417/en/OIF-Announces-External-Laser-Small-Form-Factor-Pluggable-ELSFP-Implementation-Agreement-Paving-the-Way-for-Advancements-in-Co-Packaged-Optics-Applications
- Google: Apollo paper, 22 Aug 2022: https://arxiv.org/abs/2208.10041 ; TPU v4 paper, ISCA June 2023: https://arxiv.org/abs/2304.01433 ; TPU7x docs (9,216): https://docs.cloud.google.com/tpu/docs/tpu7x ; TPU 8t post (9,600; undated page, April 2026 by press): https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/
- Microsoft: Guthrie blog, 12 Nov 2025: https://blogs.microsoft.com/blog/2025/11/12/infinite-scale-the-architecture-behind-the-azure-ai-superfactory/ ; Source feature, 12 Nov 2025: https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/ ; Gemini report, Dec 2023: https://arxiv.org/abs/2312.11805
- Lead, credited once from free text: Leo Cui, "The Entire AI Networking Industry Explained": https://www.youtube.com/watch?v=HP5oFnEtDQA (publication date not recorded in the transcript; the sources line gives no date).

## Figures dropped or flagged

- "Forty to sixty cents of network per chip dollar" (live Explainer): no primary source; withdrawn openly in the body.
- "By early 2026 roughly two thirds of new AI cluster networking was Ethernet" (live Explainer): analyst figure, not primary. Dropped.
- "A network 10 per cent slower can leave billions of dollars of silicon idle" (live Explainer): illustrative, unsourced. Dropped.
- "A large cluster uses hundreds of thousands of transceivers" (live Explainer): unsourced. Dropped.
- Corning "16 times more fibre per 72-chip rack": Corning primary not found 30 Oct 2026. Dropped from the body; numbers.ts flagged.
- Copper reach "about two metres": not found at a primary source. Body says "a few metres".
- 5,000 or 5,184 copper cables in the NVL72 spine: press only. Dropped.
- Nvidia Q2 FY2027 networking: Nvidia no longer reports the split; the 138% growth figure is secondary only. Body uses Q1 FY2027 and says it is the last quarter with the split.
- Fairwater 1,000 km: my great-circle calculation (1,044 km); Microsoft gives no distance. Body says "by my straight-line reckoning". Press "700 miles" not used.
- Microsoft's "120,000 fiber miles" and Google's Gemini detail beyond the split: cut for length.
- Corning's Q3 call commentary (e.g. sold out, demand above capacity): not checked; the body uses only the 8-K's wording.
- Marvell's Investor Day fiscal 2031 targets (interconnect about US$37.5bn of the midpoint): a presentation, not guidance or a filing. Left out of the body.
- Broadcom's "Field-Replaceable ELSFP Laser Modules" and Davisson "now shipping" are from a wire copy (Broadcom's investor site returned 403 in the CPO sidecar's check; not bypassed).
- Hock Tan's optical DSP line: third-party transcript only (Webull/Benzinga); the body says so. Confirm against Broadcom's replay before the next Marvell note.
- Company financial figures in the investor layer (Marvell, Broadcom, Lumentum, Corning, Nvidia) are each the company's own disclosure, dated, and tied to the mechanism; none in the top layer.

## Could not verify today

- Re-opened: Corning Q3 8-K, Nvidia 21 Oct and 26 Aug 2026 releases, Nvidia Q1 and Q2 FY2027 CFO commentaries, GTC 2026 page (first two thirds only), NVL72 page, Broadcom 12 Mar 2026 release.
- Not re-opened, resting on the notes and draft sidecars (verified 29 Oct and 6 to 8 Oct 2026): every Marvell, Broadcom and Lumentum figure; Corning Q2 and the warrant; all CPO, Google and Microsoft primary items.
- The Nvidia Q1 FY2027 quarter end is given as "April 2026" (Nvidia's fiscal quarter, late April); exact day not re-checked.
- Whether Lumentum's next results (5 Nov 2026) or Broadcom's (9 Dec 2026) change any note: after today.

## Fact-check fixes applied (30 Oct 2026)

1. Tomahawk 6: "128,000 chips" replaced by Broadcom's own "more than 100,000 chips" in two tiers (3 June 2025) in the distance table and Broadcom section; production volume dated 12 March 2026. numbers.ts and live-piece notes corrected above.
2. Lumentum as a CPO laser seller now rests on its own 11 August 2026 call, not Nvidia's 18 March 2025 partner list.
3. Corning: two warrants for the US$500m (8-K 6 May 2026), deposit from the Q2 10-Q, and the US$296m warrant deducted from revenue read as scarcity shared, not kept.
4. New claim names both Vera Rubin reference architectures (SN6600-LD, Q3400-RD, both pluggable); falsifier limb now "as the default or only option"; known Davisson limit noted.
5. Trims: Fairwater parallelism paragraph cut to one sentence; TPU 8t sentence cut; three filler sentences cut; exposure map merged.
