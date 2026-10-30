# Fairwater draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/fairwater-spans-two-states.md` (draft: true)
Cover: `public/covers/fairwater-spans-two-states.svg`
Drafted 29 October 2026 from the Watch Later batch. Topic approved by Tommy; the final claim wording needs his approval before publish.

## Proposed claim

Microsoft's Fairwater campuses in Wisconsin and Atlanta are joined into one training machine because no single site's power and land now fits the largest training runs, so the fibre joins sites chosen for their power; because light in fibre takes about five microseconds per kilometre, only the quieter work, such as data parallel averaging, crosses between sites while tensor work stays inside one building. My own reading, not Microsoft's words, is that the grid connection queue is why a single site cannot simply grow.

### Alternatives considered

1. Microsoft's AI WAN fibre, not the campuses, is the scarce asset that lets it place training wherever power appears. Rejected as the lead: Microsoft gives a fibre mileage but no test that could prove scarcity, and it drifts into the Corning piece's territory.
2. Cross-site training will stay limited to data parallel work because of the speed of light. Rejected as the lead: pure physics, true by construction, and it loses the power argument that ties it to the site's thesis. Kept as the second half of the falsifier.

Chosen because it keeps Fairwater as the subject, takes the site's grid-connection argument one step further (on my reading, the queue now shapes the computer, not just its timing), and has a dated test of the cause: a single campus built to hold the largest job alone.

## claims.ts entry

```ts
  {
    id: 'fairwater-spans-two-states',
    claim: 'Microsoft runs Fairwater in Wisconsin and Atlanta as one training machine because no single site\'s power and land now fits the largest training runs, so fibre joins sites chosen for their power, and only the quieter work crosses between them.',
    breaksIf: 'By the end of 2027 Microsoft or another cloud giant builds one campus sized to hold its largest training job alone, a stated multi-gigawatt cluster on a single site, and says that is now how it trains. Or tensor parallel work is shown running between sites, which would mean distance was never the limit.',
    watch: ['Any hyperscaler announcing a single-site, multi-gigawatt training cluster for its largest job', 'Microsoft adding a third Fairwater site to the AI WAN', 'Microsoft or lab statements that a named model was trained across Fairwater sites', 'Technical reports describing which kinds of parallel work cross between sites'],
  },
```

## stack.ts

Layer `network` ("The network between chips"). Its constraint sentence, "A slow link leaves the most expensive silicon in the building waiting", fits: this piece is the far end of that network, where the slow link is set by the speed of light. Suggested position right after the Explainer it builds on:
`pieces: ['ten-thousand-chips-one-thought', 'fairwater-spans-two-states', 'marvell-collects-the-toll', 'broadcom-wins-either-way', 'corning-lays-the-glass', 'lumentum-makes-the-light']`

No new layer proposed. A "between sites" layer could be argued, but one piece does not justify a new descent stop.

## Glossary (heading: "Chips, memory and the wiring between them")

- `Tensor parallelism`: Cutting each calculation in a model across several chips, which must swap results many times in every training step. It needs the fastest, shortest links, so it stays inside one building.
- `Data parallelism`: Giving each group of chips its own copy of the model and different data, then averaging what they learned once a step. It talks least, so it is the work that can cross between distant sites.
- `AI WAN`: Microsoft's wide area network built only to carry AI training traffic between distant data centres, such as its Fairwater sites in Wisconsin and Atlanta.

## numbers.ts (physical figures only)

```ts
  { layer: 'network', value: '~5 µs per km', what: 'How long light takes to cover each kilometre of glass fibre, at about two thirds of its speed in a vacuum. Across 1,000 km that is at least 5 ms one way, and switches and lasers only add to it.', piece: 'fairwater-spans-two-states', asOf: '2026' },
```

(If the µs symbol is unwanted on the numbers page, write "~5 microseconds per km".)

## LinkedIn post (§9)

```
Microsoft is training AI across two data centres about 1,000 kilometres apart, in Wisconsin and near Atlanta.

It says the largest training jobs have outgrown the power and space of a single facility, so it joined the sites with dedicated fibre. Every kilometre of glass costs light about five microseconds, so only the quietest part of the work can cross the gap. When power decides where chips go, the network has to stretch to meet it.

The piece covers why Fairwater is split, which work can travel and which cannot, and the test that would prove me wrong.

https://thephysicallayer.fyi/journal/fairwater-spans-two-states/

#AIInfrastructure #DataCentres #Networking
```

## Figures used and their sources

- Wisconsin Fairwater fully operational, June 2026: Microsoft, "Microsoft completes construction on first datacenter facility in Mount Pleasant, Wisconsin", 23 June 2026. https://news.microsoft.com/source/2026/06/23/microsoft-completes-construction-on-first-datacenter-facility-in-mount-pleasant-wisconsin/ (Brad Smith: "With our Fairwater datacenter now fully operational...")
- Atlanta Fairwater began operation October 2025; land and power "at this point necessary" to spread the work across locations; Wisconsin and Atlanta joined by the AI WAN on dedicated fibre; some fibre "acquired by Microsoft years ago and repurposed"; supports OpenAI: Microsoft Source feature, "From Wisconsin to Atlanta: Microsoft connects datacenters to build its first AI superfactory", 12 November 2025. https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/
- Large training jobs "quickly outpacing the power and space constraints of a single facility"; "The speed of light is now a key bottleneck"; two-storey building "to minimize cable lengths"; "we delivered over 120,000 new fiber miles across the US last year" (converted to more than 190,000 km; the piece states it separately from the AI WAN and does not say it was laid for Fairwater): Scott Guthrie, "Infinite scale: The architecture behind the Azure AI superfactory", Official Microsoft Blog, 12 November 2025. https://blogs.microsoft.com/blog/2025/11/12/infinite-scale-the-architecture-behind-the-azure-ai-superfactory/
- AI WAN "to enable large-scale distributed training across multiple, geographically diverse Azure regions": Scott Guthrie, "Inside the world's most powerful AI datacenter", 18 September 2025. https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/
- Gemini Ultra trained "across multiple datacenters", "model parallelism within superpods and data-parallelism across superpods": Gemini Team, Google, "Gemini: A Family of Highly Capable Multimodal Models", arXiv 2312.11805, first posted 19 December 2023 (v4 read, 17 June 2024). https://arxiv.org/abs/2312.11805 . Google does not say how far apart those data centres were, so the piece does not claim a distance for Google.
- Light in fibre: stated as standard physics, not cited to a data sheet. Silica fibre has a group index of about 1.46 to 1.47, so light travels at about two thirds of its vacuum speed, roughly 200,000 km/s, about 5 microseconds per km. The Corning SMF-28 ULL sheet first used for this could not be confirmed by the fact-checker (PDF returned 403), so Corning is no longer cited.
- About 1,000 km apart: my own great-circle calculation between Atlanta (33.75 N, 84.39 W) and Mount Pleasant, Wisconsin (42.73 N, 87.88 W), 1,044 km. Microsoft gives no distance. The fibre route is longer than the straight line, so "at least five milliseconds each way" is a floor. Press reports say "700 miles" (about 1,130 km) but that is not Microsoft's figure and is not used.

No company financial figures are used.

## Video figures dropped or flagged

Lead: YouTube video on the AI networking industry, transcript in `research-build/source-watch-later/ai-networking-industry/TRANSCRIPT.md`. Credited once in the sources line. Its structure, wording and analogies are not reused; the kitchen and fuse box analogy is new.

- "About half a millisecond of one-way delay per hundred kilometres": standard physics. The piece states it in its own terms (about 200 km per millisecond, five microseconds per km) and drops the video's "before any equipment adds its own" phrasing and its word "chatty". The mechanism section now opens on the fibre itself, then the two kinds of work, then why the site cannot grow, so it does not follow the video's order.
- "Light in glass travels at roughly two thirds of speed in vacuum": verified (1/1.46 = 0.68). Used.
- "Amazon's largest cluster for Anthropic spans many buildings": dropped. It is one campus, not several sites, so it is not evidence for multi-site training.
- "Google has publicly described training across data centers": verified against the Gemini report and used, without any distance claim.
- "Arista books real revenue against this today": dropped, unverified and a financial claim.
- The video's Atlanta rack density figure: not used. Microsoft's own blog gives about 140 kW per rack, but the piece does not need it.
- The video's 1 ms blink comparison and 100,000-accelerator framing: not used.
- The video's view that scale-across "isn't a new tier of AI infrastructure": not used as an argument; the piece files Fairwater under the existing network layer, which happens to agree.

## Not verified, so not used

- Whether any single training job has actually run across both Fairwater sites. Microsoft describes the capability; I found no Microsoft or lab statement that a named model was trained across both. That gap is what the falsifier tests.
- GPU counts and megawatts per site: Microsoft gives none (Epoch AI estimates exist, press only).
- Any third Fairwater site joined to the AI WAN as of 29 October 2026.
