# Sidecar: powering-the-rack (deep piece, cluster 7)

Cluster 7, "Powering the rack: from 54 V to 800 V" (map layer `distribution`). Drafted 30 Oct 2026 to BRIEF-DEEP.md, matching the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/powering-the-rack.md` (draft: true). Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "Powering the rack: from 54 volts to 800, and the gear each megawatt now needs".
- Top layer (cold open, analogy, How it works, The number that matters): about 470 words, 15 figures by the checker's count, 2 company financial figures (Vertiv's US$3.25m to 3.75m per MW and the 10 to 15% change, one paragraph, one money figure). Analogy about 68 words.
- Investor layer: about 2,470 words before the exposure map (inside 1,200 to 2,500; tight, so any addition needs a cut). Exposure map about 130 words. Whole body about 3,210 words.
- Revised 30 Oct 2026 after the coordinator's fact-check (7 points); see "Fact-check fixes applied" below.
- `brand/check-piece.py` on a scratch copy: 0 failures; 1 warning (average sentence 25 words, inflated by table cells; prose sentences run about 14 to 20).
- Frontmatter: `date: 2026-10-30` is a placeholder and becomes the real publish time. `cover: "/covers/copper-rack.svg"` (existing) until a new cover is drawn.

## Thesis and the old claims

Thesis: the rack has outgrown its wiring, so each megawatt holds more power gear, and 800 VDC reaches the rack (power racks, row power centres fed from AC rooms) years before it reaches the building (facility rectifier or solid-state transformer).

GaN vs SiC (Tommy's interview probe), as the piece states it on makers' own releases: SiC at the top of the chain where voltages run to kilovolts (Infineon and SolarEdge SST block on SiC, 13.8 to 34.5 kV to 800 to 1,500 VDC, 5 Nov 2025; Navitas SiC 650 V to 6,500 V); GaN at or below the 800 V bus (Navitas high-voltage GaN rated 650 V, 100 V GaN for lower-voltage DC-DC on GPU boards; TI's GaN 800 V to 6 V converter, 97.6% peak, 16 Mar 2026), with the two contesting the 800 V step; silicon power stages at the last step (incumbent; TI names no material). SemiAnalysis credited once for the phased framing and the SiC/GaN split.

800 VDC timing: only Nvidia's own dated statements in the body (20 May 2025: 1 MW racks "starting in 2027", full-scale production "will coincide with NVIDIA Kyber rack-scale systems in 2027"; 13 Oct 2025: Kyber "576 NVIDIA Rubin Ultra GPUs by 2027", "will occur in phases"; 11 Aug 2026: power rack 2H 2026, row power center up to 2 MW per row expected 2027, DC power block undated, joint white paper with Google and Microsoft March 2026, 80+ manufacturers, SST spec v0.3 July 2026). The July 2026 press reports of a Kyber slip to 2028 (attributed to SemiAnalysis via CNBC, Tom's Hardware, SDxCentral) and a reported Nvidia denial (boerse-global.de) are press only: kept out of the body, which says only that timing is contested in press reports. Note Tommy's own reading brief says not to cite the slip notes as read.

"Where later evidence cuts against it" notes:
- every-megawatt-got-harder: "Where I was wrong" on service outgrowing products (organic Q3 2026: services and spares 18.1% vs products 63.6%; the Vertiv note made the same correction on 6 Oct). Margin limb holds (25.2%, up 2.9 points; organic orders more than 100%). Stated openly that a margin rising on 55% organic growth fits operating leverage as well as richer content, so the claim now rests on Vertiv's own per-MW estimate.
- ti-feeds-the-chip: the business is growing (about 95%, about 13% of revenue, Q3 2026) but before 800 V racks ship in volume; TI's call names power density and higher voltages together (Beckman, 21 Oct). Cause named by the claim not yet shown; first limb untestable before 2027; part-empty limb not near (industrial more than 40%).
- every-megawatt-got-harder, added after fact-check: the in-house limb is partly met, and was from the start: Google's blog (30 Apr 2025) says it has liquid-cooled TPUs since 2018 "at GigaWatt scale" (the heat-and-water cluster cites it). Said openly in the claim note.
- the-rack-runs-out-of-copper (Explainer, no claim): its "flagship racks sit near 200 kilowatts" corrected in the body (Vertiv GB200 NVL72 design up to 132 kW; 200 kW is Nvidia's 54 V limit). Its "several hundred homes" and "electric car charging built the parts" lines are not carried (no primary source opened).

## Proposed claims.ts change (existing entries untouched)

At merge, the two live entries gain only `home: 'powering-the-rack'` (field already in the type; `date` already set: 2026-09-25T12:30:00+08:00 and 2026-10-02T12:49:47+08:00). `claim`, `breaksIf`, `watch` not touched. Tommy to approve.

New entry:

```ts
  {
    id: 'powering-the-rack',
    claim: '800 volts reaches the AI rack before it reaches the building: until 2028, 800 VDC enters data halls through power racks and row power centres fed from AC power rooms, and no data hall of 10 MW or more goes into service fed by a facility-level rectifier or solid-state transformer. 800 VDC here includes ±400 VDC, 800 V pole to pole.',
    breaksIf: 'Before 1 January 2028, Nvidia, a data centre operator or its equipment supplier states that a data hall of 10 MW or more is in service with 800 VDC distributed from a facility-level rectifier or solid-state transformer, rather than from power racks or row power centres fed by AC. 800 VDC includes ±400 VDC, 800 V pole to pole.',
    watch: ['Nvidia\'s 800 VDC power rack shipping (due second half of 2026) and row power centre (expected 2027)', 'A date for Nvidia\'s DC power block for direct medium-voltage conversion', 'Foxconn\'s 40 MW Kaohsiung-1 site, built for 800 VDC: how it is fed when it goes into service', 'The solid-state transformer specification past version 0.3 (July 2026)', 'Vertiv\'s next stated per-MW opportunity (US$3.25m to 3.75m, May 2026)', 'Data centre as a share of TI\'s revenue (about 13%, Q3 2026)'],
  },
```

Why it is a real test: Nvidia's own August 2026 post dates the rack and row units but not the facility block (StorageReview, 15 Aug 2026, reports an "Option C" of 4.8 MW DC Power Blocks as a long-term vision targeting 2029, and Option B row Power Centers for Q3 2027, but cites no Nvidia document; I found the 2029 date on no Nvidia page, so it stays out of the body). If Nvidia itself dates the facility block to 2029, the claim gets easier, though not trivial; the SST spec is at v0.3; but Vertiv's 2H 2026 portfolio includes centralized rectifiers and Foxconn's Kaohsiung-1 is being built for 800 VDC, so a building-fed hall before 2028 is possible. Alternatives considered: a TI data centre share threshold (a company-financial test, and it tests demand not the 800 V mechanism) and a Vertiv margin test (cannot separate content from volume, as the piece says).

## Redirect map

| Old URL | Redirect to |
|---|---|
| /journal/every-megawatt-got-harder/ | /journal/powering-the-rack/#every-megawatt-got-harder |
| /journal/the-rack-runs-out-of-copper/ | /journal/powering-the-rack/#the-rack-runs-out-of-copper |
| /journal/ti-feeds-the-chip/ | /journal/powering-the-rack/#ti-feeds-the-chip |

Sections and anchors, in order: How it works; The number that matters; [For investors] The mechanism in depth; 800 VDC timing: what Nvidia itself has said; Content per megawatt; The copper limit (#the-rack-runs-out-of-copper); Vertiv (#every-megawatt-got-harder); Texas Instruments (#ti-feeds-the-chip); Claims on record; What would prove me wrong; Research notes.

## stack.ts

Layer `distribution`. At merge: `pieces: ['powering-the-rack', 'schneider-sells-the-finished-system', 'eaton-order-book-outruns-it']` (the latter two move when cluster 3 merges). Layer text needs no change.

## Glossary (src/pages/glossary.astro), "Inside the building"

Already present, no change: UPS, Busway, 800 VDC, Busbar, Power stage, eFuse, Wide-bandgap semiconductor. Suggested edit to "Wide-bandgap semiconductor" (Tommy to decide): add "Silicon carbide takes the highest voltages, near the grid; gallium nitride switches faster at lower voltages, nearer the chip." New:
- Solid-state transformer: A transformer built from power semiconductors rather than only copper and steel, converting medium-voltage grid power straight to direct current. Silicon carbide does the switching.
- Rectifier: Equipment that turns alternating current into direct current. In an 800 VDC building one large rectifier replaces many small power supplies.
- Power rack: A cabinet of power converters standing beside the computer racks, feeding them 800 VDC from an existing AC power room. Nvidia's first 800 VDC product.
- Power shelf: The unit inside today's rack that turns 415 VAC into 54 VDC for the trays.
- Hot-swap controller: A chip that lets a live server tray be pulled or inserted without shorting the rack's power.
- Content per megawatt: What one supplier's equipment is worth in each megawatt of data centre computing power, as the supplier estimates it.

## numbers.ts (physical only)

New:
```ts
  { layer: 'distribution', value: '18,500 A', what: 'Current needed to deliver one megawatt at 54 volts. At 800 volts it is about 1,250 amps, which is why the rack is moving to 800 VDC.', piece: 'powering-the-rack', asOf: 'physics' },
  { layer: 'distribution', value: '2 MW', what: 'Power per row of racks from Nvidia\'s 800 VDC row power centre, expected in 2027. Its power rack comes first, in the second half of 2026.', piece: 'powering-the-rack', asOf: 'August 2026' },
```
Existing entries needing Tommy's decision at merge: `1 MW` and `200 kg` (piece: the-rack-runs-out-of-copper) repoint to powering-the-rack; the 1 MW `asOf` "due 2027" is Nvidia's May 2025 "starting in 2027" and could carry a note. `2.25×` (ti-feeds-the-chip) repoint. Vertiv's US$ per MW is a financial figure, so it stays out of numbers.ts.

## LinkedIn post (§9)

```
Nvidia says a one megawatt AI rack, wired the way racks are today, would need up to 200 kilograms of copper bar.

So the rack is moving from 54 volts to 800, and each megawatt now holds more power gear: Vertiv puts its own opportunity at US$3.25 million to 3.75 million per megawatt. On Nvidia's own dates, the new voltage reaches the rack before the building, which decides where silicon carbide and gallium nitride chips get used first.

The piece covers the power chain step by step, what Nvidia has actually said on timing, and the claims I have on record on Vertiv and Texas Instruments.

https://thephysicallayer.fyi/journal/powering-the-rack/

#DataCentres #Power #800VDC
```

## Cover proposal (not drawn)

`/covers/powering-the-rack.svg`. A tall dark rack in profile; on its left a thick bundle of amber copper bars labelled faintly "54 V"; beside the rack a narrower second cabinet (the power rack) fed by two thin amber lines labelled "800 V"; the building's power room in the background drawn in grey dashed outline, still AC, unlit. Caption in letter-spaced grey: "POWERING THE RACK: FROM 54 VOLTS TO 800". Background as `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Edits other files need (not made)

- `src/config.ts` line 39: READING_PATH ids include 'the-rack-runs-out-of-copper'; change to 'powering-the-rack' at merge (the redirect works meanwhile).
- `src/content/calls/vertiv.md` and `texas-instruments.md`: no edit; `claims` ids unchanged.
- Cluster 3 (equipment queue) and cluster 8 (cooling) should use the same Vertiv per-MW wording ("management estimate of opportunity per MW of IT power, 19 May 2026") if they cite it, and not call it revenue.
- Inbound links to the three old slugs resolve through the redirects.

## Sources, every one with date

Opened by me on 30 Oct 2026:
- Nvidia Technical Blog, "NVIDIA 800 VDC Architecture Will Power the Next Generation of AI Factories", 20 May 2025: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/
- Nvidia Technical Blog, "Building the 800 VDC Ecosystem for Efficient, Scalable AI Factories", 13 Oct 2025 (35 kVAC/415 VAC/54 VDC chain; 64:1 LLC to 12 VDC; "can be less than 90%"; 157%; phases; partner list): https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/
- Nvidia blog, gigawatt AI factories at OCP, 13 Oct 2025 (Kyber 576 Rubin Ultra GPUs by 2027; Foxconn Kaohsiung-1 40 MW; operators "designing for"; Vertiv 800 VDC MGX reference architecture): https://blogs.nvidia.com/blog/gigawatt-ai-factories-ocp-vera-rubin
- Nvidia blog, "Why Scaling AI Compute Performance Requires a New Power Architecture", 11 Aug 2026: https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory
- Vertiv 2026 Investor Conference deck, 19 May 2026, p.31 (US$3.25m to 3.75m per MW, up about 10 to 15% vs prior range, management estimate per MW of IT power): https://s205.q4cdn.com/554782763/files/doc_presentations/2026/05/19/Vertiv-2026-Investor-Conference_May-19-2026.pdf
- Vertiv Q3 2026 results, Form 8-K Ex. 99.1, 28 Oct 2026 (US$4,313m, +61%; organic 55.0%; products 63.6%, services and spares 18.1%; adj. margin 25.2%, +290 bp; organic orders more than 100%; FY guide US$14.45bn to 14.85bn, 23.5% to 24.5%): https://www.sec.gov/Archives/edgar/data/0001674101/000162828026067707/q32026exhibit991vrt10282026.htm
- Vertiv, 800 VDC portfolio scheduled 2H 2026, 19 May 2025: https://www.vertiv.com/en-us/about/news-and-insights/corporate-news/vertiv-accelerates-ai-infrastructure-evolution-in-alignment-with-nvidia-800-vdc-power-architecture-announcement/
- Vertiv, GB200 NVL72 reference design up to 132 kW per rack, 7 MW, 15 Oct 2024: https://www.vertiv.com/en-us/about/news-and-events/corporate-news/vertiv-codevelops-with-nvidia-complete-power-and-cooling-blueprint-for--nvidia-gb200-nvl72-platform/
- Texas Instruments Q3 2026 release, 21 Oct 2026 (US$6.06bn, +28%): https://www.sec.gov/Archives/edgar/data/0000097476/000009747626000165/q32026txnex99-eredgar.htm
- TI Q3 2026 earnings call, 21 Oct 2026 (data centre about 95%, about 13% of revenue; industrial more than 40%; gross margin 64%; power density remarks), read via transcript: https://www.webull.com/news/15789174635930624
- TI, 800 VDC architecture release, 16 Mar 2026 (two stages; GaN 800 V to 6 V, 97.6% peak; 30 kW PSU; 800 V hot-swap), read via the Stock Titan reproduction: https://www.stocktitan.net/news/TXN/ti-unveils-complete-800-vdc-power-architecture-for-future-generation-qfwa969zknb7.html
- Infineon and SolarEdge SST, 5 Nov 2025, via Semiconductor Today: https://www.semiconductor-today.com/news_items/2025/nov/infineon-051125.shtml
- Navitas 800 VDC products, Oct 2025, via Compound Semiconductor (23 Oct 2025): https://compoundsemiconductor.net/article/122800/Navitas_announces_support_for_800V_DC
- Navitas 800 V to 6 V board at GTC, release dated 16 Mar 2026 (coordinator gives 17 Mar): 16 x 650 V GaNFast FETs, stacked full bridge, 25 V silicon MOSFETs on the centre-tapped output, 1 MHz. Peak efficiency quoted as 96.5% in one copy and 97.5% in Navitas's Q1 2026 results release, so the piece gives no efficiency figure: https://www.financialcontent.com/article/gnwcq-2026-3-16-navitas-debuts-revolutionary-800-v6-v-power-delivery-board-at-nvidia-gtc-2026
- Google blog, 30 Apr 2025 (TPUs liquid-cooled since 2018 "at GigaWatt scale"): as cited by the heat-and-water cluster, not re-opened by me.
- StorageReview, 15 Aug 2026 (Options A, B, C; 4.8 MW; 2029): press, not used in the body: https://www.storagereview.com/news/nvidia-moves-800-vdc-power-architecture-from-concept-to-production-just-dont-turn-off-ac-power-yet
- SemiAnalysis, "Inside the 800VDC Revolution, Part 1", 26 May 2026, free text only: https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part

From the live pieces and research notes (verified there, not re-opened today): Vertiv Q2 2026 release, 29 Jul 2026 (US$3.27bn; margin 22.6%, +4.1; organic products 19.7%, services 10.1%); TI Form 10-K for 2025 (data centre 9%; 300 mm about 40% cheaper); TI calls of 27 Jan 2026 (about US$1.5bn) and 22 Jul 2026 (doubled; 800 V "phased in"); TI Sherman production 17 Dec 2025. Infineon's May 2025 Nvidia release (materials "grid to core"; share of power semiconductors similar or higher) read only via iConnect007 reprint.

## Figures dropped or flagged

- Kyber slip to 2028 (July 2026 press, attributed to SemiAnalysis) and Nvidia's reported denial: press only, out of the body.
- SemiAnalysis's 82.0% vs 87.4% efficiency, US$3.6m to 4.8m electrical content per MW, SST US$1.0m to 1.5m per MW, 600 kW+ racks, Vera Rubin 180 to 220 kW, phase dates: not primary; only the framing is credited.
- Eaton's US$3.4m per MW: seen only in conference summaries (Quartr, press); no Eaton filing opened. Dropped. Vertiv's prior per-MW range (US$2.75m to 3.5m in a Substack; US$3m to 3.5m in summaries): not on Vertiv's slide, dropped.
- Wolfspeed's 10 kV SiC and SST white paper (Mar 2026): not used.
- ST's 12 kW 800 V board (650 V GaN stacked, 1,200 V SiC): ST blog blocked (HTTP 473), not used.
- Infineon 12 kW GaN plus SiC reference design: secondary only, not used.
- "Several hundred homes" (copper piece) and "electric car charging built the parts" (copper piece and Tommy's 17 Sep note): not carried; no primary opened.
- Nvidia's two copper measures differ (85% more power same conductor size, May 2025; 157% same wire gauge, Oct 2025); the piece quotes both and says so.
- TI note's own correction (61% gross margin and "full factories") concerns the note's reading, not the live claim; not repeated in the piece.

## Could not verify today

- TI's 16 Mar 2026 release and Q3 call read through a reproduction and a transcript site, not ti.com or TI's own transcript. SEC EDGAR blocked curl with the brief's User-Agent (it asks for contact details, which I did not add); WebFetch read the Vertiv and TI 8-K exhibits.
- Navitas and Infineon statements read through trade-press reproductions, not the companies' own pages.
- "Silicon is the incumbent" at the final power stage is stated without a primary figure.
- Whether Vertiv's 800 VDC portfolio has shipped on its 2H 2026 schedule: not found in the Q3 release.

## Fact-check fixes applied (30 Oct 2026)

1. Vertiv claim note: Google's liquid-cooled TPUs since 2018 named; the in-house limb is said to be partly met from the start.
2. GaN at 800 V: stacking stated, with Navitas's GTC board (16 x 650 V GaN, stacked full bridge, 25 V silicon output). The split now reads SiC on the grid side in kilovolts, GaN at or below the bus, silicon on the low-voltage side. "Silicon at the last step" is labelled my reading. Infineon's OptiMOS-in-Delta proxy not used.
3. "More space than the rack has" replaced with Nvidia's "up to 64 U ... leaving no room for compute", in both layers.
4. TI: "a record for the market" becomes "its first new peak in four years". The power-density line now quotes Beckman's density and higher-voltage lines together. The 95% and 13% are labelled management's words on the call, per transcript. My transcript source gives these lines to Ilan (CEO), not the CFO, so the piece says "TI management" rather than naming either.
5. DC power block: no Nvidia page found with a date; StorageReview's 2029 Option C is press only. The piece now says Nvidia's own posts do not date it. The claim and falsifier now define 800 VDC to include ±400 VDC (800 V pole to pole). The claims.ts entry above matches.
6. A reversal line added in the timing section (see briefing below).
7. Vertiv Q2 row and TI's Sherman and 300 mm paragraph cut. Investor layer about 2,470 words.

## Briefing for Tommy: what changed since the 17 Sep note (for interviews)

- **What the note said.** It led with the building-level design (13.8 kV AC rectified straight to 800 VDC at the perimeter). It named the alternative, a dedicated rack of power supplies beside every compute rack, as the downside case: if the industry took that path, the move would slow, stay partial and shrink into a component refresh. It counted about 30 vendors. It said 800 VDC "is a wide-bandgap semiconductor story" but gave no SiC and GaN split.
- **What changed.** On 11 Aug 2026 Nvidia made that sidecar its first product: the 800 VDC power rack, due 2H 2026. Then comes a row power centre (up to 2 MW per row, 2027). The facility-level DC power block is described but undated in Nvidia's own posts. Nvidia now counts more than 80 manufacturers. So the sidecar is phase one of the transition, not its failure mode, and the building converts last.
- **Why it matters.** Rack-first means the AC room stays and power racks are added, so there is more gear per megawatt in the near term. SiC demand for solid-state transformers comes later. GaN and silicon at the tray come first.
- **GaN against SiC, the answer to give.** SiC sits on the grid side, in kilovolt switching for solid-state transformers (Infineon and SolarEdge, SiC block, 13.8 to 34.5 kV to 800 to 1,500 VDC). GaN sits at or below the 800 V bus. Its high-voltage parts are rated 650 V, so they take 800 V by stacking: Navitas's GTC board uses 16 x 650 V GaN in a stacked full bridge to go from 800 V to 6 V, with 25 V silicon on the output, and TI's 800 V to 6 V converter is also GaN. Silicon remains at the final sub-1 V step; that is my reading, not a sourced figure.
- **On timing, say:** "Nvidia's own dates are the power rack in the second half of 2026 and the row unit in 2027. Kyber was 'by 2027' as of October 2025. The press has reported a slip, which I have not seen confirmed by Nvidia, so I don't build on it."
- **Say plainly when asked:** "My September note called the sidecar the downside case. Nvidia has made it the first step, so I changed my view on the order, not on the direction."
