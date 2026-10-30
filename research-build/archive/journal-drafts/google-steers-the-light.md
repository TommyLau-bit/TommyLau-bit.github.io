# Google steers the light: sidecar for Tommy and the publish step

Piece: `src/content/journal/google-steers-the-light.md` (draft: true)
Cover: `public/covers/google-steers-the-light.svg`
Drafted 29 October 2026, batch 3, Tier A item A5 (lead: ai-networking-industry video). Topic approved in outline; the final claim wording needs Tommy's approval before publish.

## Quality bar (CLAUDE.md, 29 Oct 2026)

1. New mechanism: yes. The site covers the plug (Marvell's DSP), the laser (Lumentum), the fibre (Corning), switch silicon in passing (Broadcom) and distance between sites (Fairwater). None covers a switching layer that passes light without converting it. This piece is about removing plugs and switch chips, which runs against the "more plugs per cluster" logic of the Marvell and Lumentum pieces rather than repeating it.
2. Primary sources: Google's own papers (Mission Apollo, TPU v4 at ISCA 2023), Google Cloud documentation and blogs, Lumentum's 10-K and proxy, Coherent's 10-K. No press figure is used in the body.
3. What a PM learns beyond the headline: the mirror layer is cheap (under 5% of cost, under 3% of power for TPU v4, optics and fibre included); a mirror switch's cost does not rise with data rate, so it is not replaced each chip generation the way transceivers are; mirrors set the pod's shape in milliseconds, so they cannot route packets and the chips' own links still do that; and the device is now a product with outside revenue (Lumentum).

## Proposed claim

Inside its TPU pods Google joins chips with mirror switches that steer light without reading it, keeping switching to a few per cent of a pod's cost and power, and the mirrors will leave Google: by the end of 2027 a second cloud giant will state in its own paper, blog or filing that optical circuit switches join chips in a production AI cluster, or Lumentum's fiscal 2027 annual report will name or describe a buyer other than Google.

(Revised after fact-check, 29 Oct 2026: the earlier "Google keeps mirrors between the cubes of every pod" test was dropped as untestable.)

### Alternatives considered

1. The outline's claim: no second cloud runs optical circuit switches at scale by end-2027. Rejected as the direction (the final claim predicts the opposite, using the same observable): Lumentum does not name its OCS buyers, and press coverage of its August 2025 results reports two hyperscale customers with a third for 2026. If Google is one of them, a second cloud may already be buying, and nothing primary would let a reader test it. Also it is a claim about rivals, not about Google's mechanism.
2. Optical circuit switches become a mass-market product, with Lumentum's OCS line reaching a stated revenue level. Rejected as the lead: it would be an "order book" piece about Lumentum, the template Tommy flagged, and Lumentum already has a piece.

Chosen because it keeps Google as the subject, rests on Google's own published engineering, and has a dated observable: what Google says joins its next pods.

## claims.ts entry

```ts
  {
    id: 'google-steers-the-light',
    claim: 'Inside its TPU pods Google joins chips with mirror switches that steer light without reading it, keeping switching to a few per cent of a pod\'s cost and power, and by the end of 2027 the mirrors will have left Google: another cloud giant, or Lumentum\'s own filings, will show them joining chips in an AI cluster that is not Google\'s.',
    breaksIf: 'By the end of 2027 no second hyperscaler has stated in its own paper, blog or filing that optical circuit switches join chips in a production AI cluster, and Lumentum\'s fiscal 2027 annual report names or describes no optical circuit switch customer other than Google.',
    watch: ['Papers, blogs and filings from Microsoft, Amazon, Meta and Oracle on optical circuit switches in AI clusters', 'Customer descriptions in Lumentum\'s fiscal 2027 annual report', 'Coherent optical circuit switch disclosures', 'What joins the chips in Google\'s pods after TPU 8t'],
  },
```

## stack.ts

Layer `network` ("The network between chips"). Suggested position after Marvell, since it is the layer that removes plugs:
`pieces: ['ten-thousand-chips-one-thought', 'marvell-collects-the-toll', 'google-steers-the-light', 'broadcom-wins-either-way', 'corning-lays-the-glass', 'lumentum-makes-the-light']`
(If Fairwater publishes first, keep its suggested slot too.) No new layer proposed.

## Glossary (heading: "Chips, memory and the wiring between them")

- `Optical circuit switch`: A box of tiny tilting mirrors that bounces light from one fibre into another without turning it into electricity or reading it. It uses almost no power and is largely data rate agnostic, but it takes milliseconds to change, so it sets the shape of a network rather than routing each packet. Google calls its own Palomar.
- `Packet`: One of the small parcels data is cut into to travel through a network. An ordinary switch reads each one to decide where it goes.
- `TPU`: Tensor processing unit, Google's own AI chip. Google links thousands of them into a pod that works as one machine.

## numbers.ts (physical figures only)

```ts
  { layer: 'network', value: '108 W', what: 'Maximum power drawn by one of Google\'s 136-port Palomar mirror switches, which steer light between fibres without reading it. Google\'s paper calls this a fraction of the power of an electrical switch of the same capacity.', piece: 'google-steers-the-light', asOf: '2022' },
  { layer: 'network', value: '<3%', what: 'Share of a Google TPU v4 pod\'s power taken by its whole optical switching layer, switches, plugs and fibre included, for 4,096 chips.', piece: 'google-steers-the-light', asOf: '2023' },
```

## LinkedIn post (§9)

```
Google joins the racks of its biggest AI chip pods through boxes of tiny mirrors that never read the data.

Each mirror tilts to bounce light from one fibre into another, so there is no chip to power and no extra plug to buy at the switch. In Google's own accounting, the whole optical layer of a 4,096-chip pod came to under 3 per cent of its power. The plugs at each end are replaced when the chips get faster, but a mirror does not care how fast the light flickers.

The piece covers how the mirrors work, what Google's own papers show they cost, and the test that would prove me wrong.

https://thephysicallayer.fyi/journal/google-steers-the-light/

#AIInfrastructure #Networking #Optics
```

## Figures used and their sources

- Ironwood pod of 9,216 chips: Google Cloud TPU7x documentation, "A TPU7x Pod scales up to 9,216 chips (144 cubes)", read 29 October 2026. https://docs.cloud.google.com/tpu/docs/tpu7x . Also Google, "Ironwood: The first Google TPU for the age of inference", 9 April 2025 ("scales up to 9,216 liquid cooled chips", "nearly 10 MW"). https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/
- Ironwood uses OCS to route around interruptions and restore the workload while services keep running (piece now uses Google's words): Google Cloud blog, "Announcing Ironwood TPUs General Availability and new Axion VMs", 7 November 2025 ("our Optical Circuit Switching (OCS) technology acts as a dynamic, reconfigurable fabric, instantly routing around interruptions"). https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads
- TPU 8t superpod of 9,600 chips, OCS reconfigures around failures: Google, "Our eighth generation TPUs: two chips for the agentic era" ("A single TPU 8t superpod now scales to 9,600 chips"; "Optical Circuit Switching (OCS) that reconfigures hardware around failures with no human intervention"). https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/ . The page shows no date; the 22 April 2026 Cloud Next date is PRESS-CONFIRMED only (HPCwire, 22 April 2026). The piece's sources line now dates it 23 April 2026 per the fact-check.
- Palomar: 136x136, two 2D MEMS mirror arrays tilted on two axes, gold-coated mirrors, millisecond switching, maximum power 108 W "a fraction of the power of an EPS system with the same switch capacity", 176 mirrors per die down-selected to 136, camera-based mirror control, sub-micron lens alignment, data rate agnostic: Urata, Liu et al. (Google), "Mission Apollo: Landing Optical Circuit Switching at Datacenter Scale", arXiv 2208.10041, 22 August 2022. https://arxiv.org/abs/2208.10041
- TPU v4: 4,096 chips, 64 cubes of 4x4x4 joined by copper in each rack, 48 OCSes, optical fabric "<5% of the total TPU v4 supercomputer capital costs and <3% of total power", accounting "includes the entire optical fabric, including the optics modules, fiber, and OCS"; each cube put into production as soon as installed; routes around failed hosts; Google Platforms Optics team "kept advancing the state-of-the-art of OCSes and optical transceivers after other organizations gave up": Jouppi et al. (Google), "TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings", ISCA 2023, 17 to 21 June 2023, arXiv 2304.01433. https://arxiv.org/abs/2304.01433
- Lumentum OCS revenue "more than $90.0 million" in fiscal 2026 (year to 27 June 2026), "initial phase of optical circuit switch shipments": Lumentum 10-K for fiscal 2026, filed 17 August 2026. https://www.sec.gov/Archives/edgar/data/1633978/000162828026057358/lite-20260627.htm . Not used in the body but relevant: Lumentum proxy, 6 October 2026, says OCS is "rapidly scaling past a $100 million quarterly revenue run rate". https://www.sec.gov/Archives/edgar/data/1633978/000130817926000420/lite2026-def14a.htm
- Coherent developing OCS "based on our digital liquid-crystal technology": Coherent 10-K for fiscal 2026, filed 14 August 2026. https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/iivi-20260630.htm

One company financial figure is used (Lumentum's OCS revenue). No figure is press-only except the April 2026 date of the TPU 8t announcement.

## Video figures dropped or flagged

Lead: YouTube video on the AI networking industry, transcript `research-build/source-watch-later/ai-networking-industry/TRANSCRIPT.md`. Credited once in the sources line. Its OCS mention is two sentences inside a scale-up comparison; the piece's structure, the torch and post room analogy and the wording are my own.

- "Scales to over nine thousand chips in one pod": verified as Ironwood's 9,216 (Google docs). Updated: the newer TPU 8t pod is 9,600 (Google blog). Both used.
- "Real optic circuit switches, physical mirrors steering beams of light to reconfigure the shape of the network": verified against the Apollo and TPU v4 papers.
- The video's comparison with NVLink and Amazon's NeuronLink: not used.

## Checked and not used

- Lumentum's OCS customers: not named in any filing. Press coverage of August 2025 results reports two hyperscale customers plus a third for 2026, and an OCS backlog above $400 million (press only). Not used, and the reason the outline's "no second cloud" claim was dropped.
- Whether Lumentum supplies Google's Palomar: no primary source. The piece does not link them.
- Google's Jupiter data centre network savings from OCS (SIGCOMM 2022): not read at source, not used.
- TPU 8i's pod of 1,152 chips and its OCS use: press only, not used.
- Next Platform (28 April 2026) suggests OCS is not used to scale out across Virgo fabrics; the piece only claims OCS inside the pod, which Google states.

## Fact-check changes, 29 Oct 2026

- Lumentum line no longer says the design is spreading; it says Google is no longer the only maker and that the 10-K names no buyer.
- Thesis scoped to the pod ("Inside its pods..."); the Virgo Network is not shown to run on mirrors.
- Falsifier replaced (second hyperscaler statement, or Lumentum FY2027 10-K customer); claim now predicts the mirrors spread.
- Ironwood wording follows Google's own; numbers.ts and glossary wording aligned to the paper; sources line adds TPU 8t post, TPU7x docs and Coherent's 10-K; LinkedIn line no longer implies fibre is replaced.
