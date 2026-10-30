# Co-packaged optics draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/the-optics-you-cannot-unplug.md` (draft: true)
Cover: `public/covers/the-optics-you-cannot-unplug.svg`
Drafted 29 October 2026 from Tier A item A7 (UNCAPPED-RESULTS.md). The final claim wording needs Tommy's approval before publish.

## Verdict against the quality bar: PASS (with an honest warning on the Marvell claim)
1. New mechanism (partial, said honestly): the repair limit of co-packaged optics is the video's own point, not ours. The original part is what both vendors did about it: the lasers kept in removable front-panel modules, Spectrum-6 sold both ways, and Nvidia's own Vera Rubin reference architecture (15 Sep 2026) specifying the pluggable SN6600-LD rather than its co-packaged SN6800/SN6810. The site has no piece on any of this.
2. Primary sources: Nvidia's own releases, technical blogs and results release, Nvidia's hosted call transcript, Broadcom's product and reliability releases, the OIF implementation agreement, Marvell's release. No analyst port-share figure is used.
3. Beyond the headline: "CPO is shipping" is the headline. What a PM learns: both CPO designs keep the lasers swappable, so laser makers sell into either design while the plug's signal processor is what CPO removes; Spectrum-X's optical engines are soldered; Nvidia sells Spectrum-6 both ways; neither company mentioned CPO on its latest call; but Nvidia is funding 15x, then about 30x, optical-engine capacity, and Marvell bought Celestial AI.

## This piece and marvell-collects-the-toll (said openly, not a silent fix)
The Marvell claim in full: Marvell is paid every time AI chips talk, through the signal processor in each optical plug, whoever made the chips; it breaks if the translation moves off the plug at scale, through linear pluggable optics (LPO) or co-packaged optics, or if Marvell's interconnect growth stalls while clusters keep growing. This piece tests only the co-packaged leg, for scale-out switches, and the piece says so in its falsifier section. As of 29 Oct 2026 that leg holds: Nvidia's own reference design picks the pluggable switch. It does not test the LPO leg or the growth leg.

Points for Tommy on the Marvell claim (none is a reason to change it yet):
- SPIL's 15x optical-engine capacity by mid-2027, doubling again by end-2028 (Nvidia, 21 Oct 2026), is an intention, not built capacity. If it is met, it is the main way the co-packaged leg could break later.
- Inside the rack is not a Marvell plug-DSP threat in kind: the Marvell piece says copper serves inside the cabinet, so co-packaged scale-up links (Kyber, GTC 16 Mar 2026) would mostly replace copper, not plug DSPs. Left out of the body.
- Marvell completed its purchase of Celestial AI on 2 Feb 2026; Marvell's release describes it as "optical interconnect technology for scale-up connectivity". Left out of the body.
- Hock Tan, Broadcom Q3 FY2026 call, 2 Sep 2026 (secondary transcript copy, Webull): "We're now the leader in leading edge optical DSPs". That bears directly on the Marvell piece (a rival claiming the DSP lead), not on this one. Worth checking against Broadcom's own replay before the next Marvell note.

## This piece and lumentum-makes-the-light
Lumentum's falsifier includes "silicon photonics, optics built in silicon with a simpler laser, routes around the EML". Co-packaged engines are silicon photonics fed by continuous-wave (CW) lasers in the external modules, so SPIL's 15x target is evidence on that leg of the Lumentum falsifier, if it is built. Lumentum is also named by Nvidia as a laser supplier to its co-packaged switches (18 Mar 2025 partner list), so this cuts both ways.

## Proposed claim
Through 2028, co-packaged optics stay an option on Nvidia's and Broadcom's AI switches, not the default: because a part built onto the switch cannot be swapped by hand, both keep the lasers in removable front-panel modules, and Nvidia's own reference design for its newest systems keeps specifying the pluggable switch.

### Alternatives considered
1. "CPO stays a small minority of AI switch ports through 2028" (the scout's wording). Rejected: the only port-share figures are analyst estimates (Dell'Oro, LightCounting), not primary, so the claim could not be tested from primary sources.
2. "CPO switches still need pluggables at the server end of every link." Rejected as the lead: true today (Nvidia's ConnectX-9 cards have OSFP cages) but close to tautological and silent on the switch, where the contest is. Kept as one line of evidence.
Chosen because it rests on the repair mechanism, uses only company and standards-body documents, and has a clean observable: whether the pluggable version of the newest switch disappears or a vendor says CPO is most of what it ships.

## claims.ts entry

```ts
  {
    id: 'the-optics-you-cannot-unplug',
    claim: 'Through 2028, co-packaged optics stay an option on Nvidia\'s and Broadcom\'s AI switches, not the default: because a part built onto the switch cannot be swapped by hand, both keep the lasers in removable front-panel modules, and Nvidia\'s own reference design for its newest systems keeps specifying the pluggable switch.',
    breaksIf: 'By the end of 2028, Nvidia\'s DGX SuperPOD reference architecture for its newest systems specifies a co-packaged optics switch for the compute fabric, or Nvidia or Broadcom says most of the AI switches it ships carry co-packaged optics.',
    watch: ['Which Spectrum or Quantum switch the next DGX SuperPOD reference architecture specifies (today the pluggable SN6600-LD, 15 Sep 2026)', 'Any Nvidia or Broadcom statement of the shipped mix of co-packaged and pluggable switches', 'SPIL optical-engine capacity against the 15x mid-2027 target', 'Whether Nvidia\'s next switch generation is still offered with pluggable optics', 'Field (not lab) reliability data from Meta, Microsoft or another large operator'],
  },
```

## stack.ts
Layer `network`. Suggested position after `marvell-collects-the-toll` (it tests that piece from the other side):
`pieces: ['ten-thousand-chips-one-thought', 'marvell-collects-the-toll', 'the-optics-you-cannot-unplug', 'broadcom-wins-either-way', 'corning-lays-the-glass', 'lumentum-makes-the-light']`
No new layer needed.

## Glossary (heading with the networking terms, beside Optical transceiver and DSP)
- **Co-packaged optics (CPO)**: optical engines mounted on the same package as a switch chip, millimetres away, instead of in plugs at the front panel. Saves power; a failed engine cannot be swapped by hand.
- **External laser source**: a removable front-panel module holding the lasers that feed co-packaged optics, so the part most likely to wear out can still be replaced by hand. (OIF's standard form is ELSFP.)
- **Optical engine**: the small assembly that turns a chip's electrical signal into light and back.

## numbers.ts
None proposed. The only physical figure (eight lasers per external laser source module, Nvidia blog 26 Aug 2025) is product-specific, not structural.

## Figures used in the body, with primary source
- Reference design picks the pluggable switch: Nvidia DGX SuperPOD reference architecture with DGX Vera Rubin NVL72 and Spectrum-X compute fabric (PDF created 15 Sep 2026) specifies the Spectrum-6 SN6600-LD; Nvidia's SN6000 hardware manual describes SN6600-LD as "64 RHS type OSFP cages supporting 128 ports" and the SN6810-LD and SN6800 as the co-packaged models.
- Lasers "on easily accessible external laser source (ELS) pluggable OSFP modules on the switch front panel", "facilitating quick diagnosis and easy replacement": Nvidia technical blog, 27 Mar 2025.
- Davisson shipping: Broadcom release, 8 Oct 2025 ("now shipping"; also "currently sampling" to early access customers).
- 3.5 times power efficiency: Nvidia announcement, 18 Mar 2025 (vendor claim, labelled as such in the piece).
- Spectrum-X optical engines soldered (solder reflow); Quantum-X socketed; external laser source with eight lasers, swappable "without disturbing the surrounding switch infrastructure": Nvidia technical blog, 26 Aug 2025.
- Broadcom "Field-Replaceable ELSFP Laser Modules", 16 optical engines, 102.4 Tbps: Broadcom TH6-Davisson release, 8 Oct 2025 (read via the MFN wire copy; Broadcom's investor site returned 403, not bypassed).
- OIF ELSFP implementation agreement, Aug 2023: OIF release via Business Wire, 8 Aug 2023.
- SPIL 15x by mid-2027: Nvidia release, 21 Oct 2026. Body calls it "a target rather than a factory"; the earlier "shows how small the base is" line was cut.
- Spectrum-6 "supporting both pluggable and co-packaged optics": Nvidia Q2 FY2027 results release, 26 Aug 2026.
- No mention of co-packaged optics on Nvidia's call: Nvidia-hosted FactSet transcript, 26 Aug 2026 (searched for optic, photonic, CPO, pluggable, laser: no hits).
- No mention on Broadcom's Q3 FY2026 call, 2 Sep 2026, which did discuss Tomahawk 6 and lasers "far surpassing supply": third-party transcript copy (Webull). **Flag: not from Broadcom's own site; worth confirming against the official replay.**
- Meta lab test, 1 million cumulative 400G-equivalent port device hours flap-free, high-temperature lab: Broadcom release, Oct 2025, citing Meta's ECOC 2025 paper (S. Amiralizadeh, 30 Sep 2025). The piece says "Broadcom's co-packaged optics, reported by Broadcom", not which generation. Meta's paper itself was not publicly readable.
- Nvidia server network cards take plug-in modules: Nvidia ConnectX-9 SuperNIC user manual, Specifications page ("Single cage OSFP"; "Dual-port QSFP112").
- Kyber and Celestial AI: no longer in the body (see the Marvell section).
- Company financial figures: none.

## Video figures dropped or flagged
- "Broadcom says a co-packaged version of its 102.4 terabit switch is in production": Broadcom's own release says "now shipping" but also "currently sampling" to early access customers. Piece says only that it carries co-packaged optics and has shipped.
- "Nvidia has begun shipping a co-packaged InfiniBand platform; its Ethernet system remains on stated rollout schedule": not used. Spectrum-X Photonics full production (Aug 2026) is press-only (StorageReview, 15 Aug 2026; no Nvidia release found), so the revised piece makes no Nvidia co-packaged shipping-date claim. It dates only Broadcom's Davisson (Oct 2025, Broadcom's release) and quotes Nvidia's 26 Aug release on Spectrum-6 supporting both.
- Video's power and reliability multiples were not used from the video; the one multiple in the piece is Nvidia's own 18 Mar 2025 claim, labelled as a vendor claim. Nvidia's "10x resiliency", "63x signal integrity", "5x lower power" (press variant), and Meta's 0.34% annual failure rate and 2.6 million hour MTBF (SemiAnalysis, press) dropped.
- Broadcom Bailly "50 million hours with no unrecoverable failures" (OFC 2026, secondary blog): dropped, press only.
- Feynman CPO in 2028 (Nikkei Xtech via Wccftech, 3 May 2026): press only, kept out of the body (the body cites only Nvidia's Kyber statement).
- Early CPO customers list (CoreWeave, Lambda, OCI, Microsoft, IBM, Nebius): press only, dropped.
- No Microsoft published reliability work on CPO found.

## LinkedIn post (§9)

Nvidia and Broadcom now build the optics into their AI switches, yet both kept the lasers in plugs you pull out by hand.

A part soldered next to a switch chip cannot be swapped when it fails, so the parts most likely to wear out stay removable. And Nvidia's own blueprint for its newest AI clusters picks the plug-in version of its switch. That decides how fast built-in optics spread, and who keeps selling the plug.

The piece covers why the lasers stayed outside, what both companies have said and shipped, and what would prove me wrong.

https://thephysicallayer.fyi/journal/the-optics-you-cannot-unplug/

#AI #DataCentres #Networking

## Sources, one per line (figure: source, date)
- Nvidia Spectrum-X and Quantum-X Photonics announcement, 18 Mar 2025: https://nvidianews.nvidia.com/news/nvidia-spectrum-x-co-packaged-optics-networking-switches-ai-factories
- Nvidia technical blog, Scaling AI factories with co-packaged optics, 18 Aug 2025: https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/
- Nvidia technical blog, How industry collaboration fosters Nvidia co-packaged optics, 26 Aug 2025: https://developer.nvidia.com/blog/how-industry-collaboration-fosters-nvidia-co-packaged-optics
- Nvidia GTC 2026 live updates, 16 Mar 2026: https://blogs.nvidia.com/blog/gtc-2026-news/
- Nvidia Q2 FY2027 results release, 26 Aug 2026: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/
- Nvidia Q2 FY2027 call transcript (Nvidia-hosted), 26 Aug 2026: https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf
- Nvidia and supply chain partners expand capacity, 21 Oct 2026: https://nvidianews.nvidia.com/news/nvidia-and-supply-chain-partners-expand-capacity-to-accelerate-ai-infrastructure-buildout
- Broadcom TH6-Davisson release, 8 Oct 2025 (wire copy): https://mfn.se/all/a/broadcom/broadcom-announces-tomahawk-r-6-davisson-the-industrys-first-102-4-tbps-ethernet-switch-with-co-packaged-optics-824cfbb5
- Broadcom CPO quality and reliability release, Oct 2025 (reproduced): https://www.storagenewsletter.com/2025/10/21/broadcom-showcases-industry-quality-and-reliability-of-co-packaged-optics/
- Broadcom Q2 FY2026 call, 3 Jun 2026 (transcript copy): https://stockanalysis.com/stocks/avgo/transcripts/581106-q2-2026/
- Broadcom Q3 FY2026 call, 2 Sep 2026 (transcript copy; also the Hock Tan optical DSP line): https://www.webull.com/news/15511095937917952
- OIF ELSFP implementation agreement, 8 Aug 2023: https://www.businesswire.com/news/home/20230808055417/en/OIF-Announces-External-Laser-Small-Form-Factor-Pluggable-ELSFP-Implementation-Agreement-Paving-the-Way-for-Advancements-in-Co-Packaged-Optics-Applications
- Marvell completes acquisition of Celestial AI, 2 Feb 2026: https://investor.marvell.com/news-events/press-releases/detail/1005/marvell-completes-acquisition-of-celestial-ai
- Nvidia ConnectX-9 SuperNIC user manual, Specifications: https://networking-docs.nvidia.com/connectx9hw/specifications
- Nvidia technical blog, A new era in data center networking with silicon photonics-based network switching, 27 Mar 2025: https://developer.nvidia.com/blog/a-new-era-in-data-center-networking-with-nvidia-silicon-photonics-based-network-switching/
- Nvidia DGX SuperPOD reference architecture, DGX Vera Rubin NVL72 with Spectrum-X compute fabric (PDF created 15 Sep 2026): https://docs.nvidia.com/dgx-superpod-spectrum-x-reference-architecture-with-dgx-vera-rubin-nvl72.pdf
- Nvidia Spectrum-6 SN6000 hardware user manual, Introduction: https://networking-docs.nvidia.com/sn6000hw/introduction
- Lead (credited once in the piece): Leo Cui, "The Entire AI Networking Industry Explained", https://www.youtube.com/watch?v=HP5oFnEtDQA

### Copying and order (fact-check, 29 Oct)
Reworded the passages close to the video ("replaced by hand", "different repair problem", "inches to millimetres") and changed the order: the piece now leads with Nvidia's reference design choosing the pluggable switch and the lasers kept outside, then the repair reason, then power, then shipment status in the evidence. The video goes CPO, trade-off, shipment status.

### Verification notes
- Broadcom's investor site returned 403 and was not bypassed; wire and reproduced copies used.
- One fetched transcript page (fool.com) carried embedded instructions aimed at the reader tool; they were ignored and that page was not used as a source.
