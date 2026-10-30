# Sidecar: johor-plugs-in-before-it-fills

Draft of 30 Oct 2026 (Batch 3, SemiAnalysis framing). Piece: `src/content/journal/johor-plugs-in-before-it-fills.md` (draft: true). Cover: `public/covers/johor-plugs-in-before-it-fills.svg`. Body 564 words, 9 figures, 1 company financial figure (DayOne's 69%). Checker 0 failures, 0 warnings. `npm run build` clean. Nothing committed, published or scheduled.

## Verdict: PASS (with one honest risk)

1. New mechanism: yes. The site has the connection queue (the-queue-not-the-chip, two-governments-one-confession) and energised-versus-announced (abilene-switched-on-in-stages). It does not have connected-versus-drawn, or a US licence that follows the tenant's headquarters, not its location, as the gate on filling a Johor hall.
2. Primary sources: yes. Tenaga's analyst briefing, the DayOne F-1 on EDGAR, the BIS guidance text, the MITI statement and the Dewan Rakyat Hansard. SemiAnalysis is credited for its framing only (free text).
3. Beyond the headline: yes. Malaysia's connected data centres draw about 22% of their booked maximum demand. Malaysia's own chip permit does not touch chips installed in Johor. DayOne earns about 69% of its revenue from one customer, which SemiAnalysis names as ByteDance.

Honest risk: low draw against booked maximum demand is partly normal ramp. Maximum demand is booked for the finished campus and filled over years. Nothing primary attributes the gap to chips or licences. So the claim tests the observable, the fill ratio, and the piece names licences as one pace-setter for Chinese tenants, not the cause of the whole gap.

## How it treats the-queue-not-the-chip (CLAUDE.md rule)

The piece says openly that the July claim needs a narrower reading: the wire is still scarce for a campus waiting to connect, but not for one already plugged in. It links the old piece. It does not edit it. Neither the old piece nor claims.ts is touched. A new dated claim is proposed below, to sit beside the old one. The scheduled abilene-switched-on-in-stages piece also says "Johor is short of connections, not chips". That is consistent with the narrower reading, so it needs no change.

## Credit to SemiAnalysis (their idea, not Tommy's)

The power-gated versus chip-gated split, "the grid is sold out" and about a terawatt of US load requests are SemiAnalysis's. The piece attributes all three in its opening paragraph and credits both articles in the sources line. "Inner Mongolia is China's Johor" and their Johor rents and capex point are not used. The ByteDance identification comes from their free text ("How Oracle Is Winning the AI Compute Market", 30 Jun 2025): DayOne's "largest customer (by committed power) is, by far, Bytedance". No paywalled content was used.

## The claim

**Proposed:** In Johor, the grid connection now runs ahead of the chips. Campuses already connected fill more slowly than they are plugged in, so Tenaga's reported actual data centre load stays under 40% of the maximum demand of the data centre projects in its system at June 2027.

Trend behind the 40% line, all from Tenaga briefings: 603 MW drawn in June 2025 against 3.5 GW of completed projects (about 17%). 850 MW in December 2025 against about 4.5 GW in operation (19%). 1,054 MW in March 2026 against about 4.5 GW (23%). 1,256 MW in June 2026 against 5.65 GW in system (22%). Load roughly doubles each year. If it doubles again to about 2.5 GW while 2.21 GW under construction mostly enters the system, the ratio is near 32%. Faster filling, or slower connection, could breach 40%. So the test is real, not safe.

**Alternatives considered:**
- A. "Johor is chip-gated for its Chinese tenants." Rejected. It is not observable at a primary source, since no one publishes licences or a tenant split, and it overclaims.
- B. "The JS-SEZ uses about a third of its installed grid capacity" (3,885 MVA against 1,272 MW). Rejected. It is press-only, it is internally inconsistent (see below), and it covers all load, not data centres.
Chose the fill ratio because Tenaga publishes it every quarter, and it is the cleanest primary test of "plugged in faster than filled".

## claims.ts entry (for publish; do not add now)

```ts
  {
    id: 'johor-plugs-in-before-it-fills',
    claim: 'In Johor the grid connection now runs ahead of the chips: campuses already connected fill more slowly than they are plugged in, so Tenaga\'s actual data centre load stays under 40% of the maximum demand of the data centre projects in its system at June 2027.',
    breaksIf: 'Tenaga\'s figures for June 2027 show actual data centre load at 40% or more of the maximum demand of data centre projects in its system, or Johor operators report finished halls left waiting for their grid connection.',
    watch: ['Tenaga\'s data centre load against maximum demand in system (1,256 MW against 5.65 GW, June 2026)', 'BIS licensing for advanced chips to entities headquartered in China, and any change to its data centre carve-out', 'DayOne\'s customer concentration and in-service capacity', 'Johor\'s share of Malaysia\'s secured data centre capacity (67%, June 2026)'],
  },
```

## stack.ts layer

`operators` (Who runs the capacity), beside nebius-paid-for-what-is-switched-on and power-first-chips-last. The piece is about turning connected power into working computing, not about the wire. That layer's constraint line already reads "Buyers pay for megawatts switched on, not megawatts signed."

## Glossary (heading "Getting power to the building")

- Maximum demand: The most power a customer may draw at once, booked in its supply agreement with the utility. A data centre books it for the finished campus and fills it over years. (Add only if no entry exists; the malaysia-keeps-the-wires-shared sidecar proposed the same term.)
- Energy supply agreement: In Malaysia, the contract between Tenaga and a large new customer that fixes the maximum demand the grid will provide.
- Export licence (heading "Chips and the factories"): US permission needed to ship controlled items. For advanced AI chips, it is required for any company headquartered in China, wherever its subsidiary is located.

## numbers.ts (physical)

```ts
  { layer: 'operators', value: '1.26 GW of 5.65 GW', what: 'Data centre load Tenaga Nasional supplied in June 2026, against the maximum demand booked by the data centre projects in its system across Malaysia.', piece: 'johor-plugs-in-before-it-fills', asOf: 'June 2026' },
```

## LinkedIn post (§9)

Malaysia's connected data centres draw less than a quarter of the power they have booked.

Johor holds two thirds of that capacity, and the story told about it is a grid bottleneck. For campuses already plugged in, Tenaga's own figures say otherwise: what fills the halls is the tenants' chips. For Chinese tenants, those chips need a US export licence, wherever the hall is.

The piece covers how a Johor hall gets filled, what Tenaga and DayOne report, and what would prove me wrong.

https://thephysicallayer.fyi/journal/johor-plugs-in-before-it-fills/

#DataCentres #Johor #Grid

## Figures in the body, with primary source

| Figure | Source | Status |
|---|---|---|
| About a terawatt of US load requests; "the grid is sold out" | SemiAnalysis, How AI Labs Are Solving the Power Crisis, 30 Dec 2025, free text | Third-party analysis, credited as theirs |
| Power-gated US, chip-gated China | SemiAnalysis, The Chinese AI Infrastructure Boom, 25 Sep 2026, free text | Third-party framing, credited |
| 5.65 GW maximum demand in system (42 projects); 1,256 MW actual load, June 2026 | TNB Analyst Briefing 2QFY2026, p.4 | Primary |
| Johor 67% of secured DC capacity (29 of 61 projects, 5.6 of 8.3 GW) | TNB Analyst Briefing 2QFY2026, p.4 | Primary |
| Licence needed for advanced computing items to entities headquartered in D:5 (includes China) or Macau, or whose ultimate parent is, even if located elsewhere; data centre operators need not cease ongoing use "until further notice" | BIS, Guidance Regarding Enforcement of License Requirements for Advanced Computing Items for Entities Headquartered in Country Group D:5 and Macau, 31 May 2026 | Primary |
| Malaysia's permit covers "exports, tranships and transits" of US-origin high-performance AI chips only | MITI press statement, 14 Jul 2025 | Primary |
| DayOne provides "space, power and cooling, to support our customers' IT equipment"; long-term take-or-pay contracts | DayOne Form F-1, 5 Oct 2026 | Primary |
| Largest customer, "a global technology company with a leading short-form video platform", 69.4% of 2025 and 69.2% of 1H 2026 revenue; restrictions on it could reduce demand and "could impact future deployments" | DayOne Form F-1, 5 Oct 2026 | Primary |
| Largest customer is ByteDance | SemiAnalysis, 30 Jun 2025, free text | Third-party, attributed |

Corroborating, not in the body: Dewan Rakyat Hansard, 13 Oct 2026, pp.31 to 33. As of August 2026, 62 data centres had signed ESAs for 8.771 GW of maximum load. 45 were operating with 6 GW of maximum load, and actual use was about 1.37 GW (about 23%). The deputy minister said data centres book more than they use, and that the Energy Commission is studying actual requirements. Primary.

## The 3,885 MVA figure (brief asked to verify): press-only, dropped

Provenance: a Facebook post by the Johor Menteri Besar, Onn Hafiz Ghazi, 16 Jan 2026, citing TNB data as of December 2025, reported by Bernama via Malay Mail and by RTM. It says the JS-SEZ had 3,885 MVA installed against about 1,272 MW of demand, "72.76 per cent utilisation". It also lists 4 approved PMUs at 630 MVA and 9 planned at 1,620 MVA. I found no TNB, MIDA, IRDA, JS-SEZ authority or Energy Commission document carrying it. The figure is internally inconsistent: 1,272 / 3,885 is about 33%, not 72.76%. It also covers all JS-SEZ load, not data centres only. So it was not used. Note that the published claims.ts watch item for the-queue-not-the-chip ("Johor-Singapore zone utilisation past 72.76 per cent") carries the same unreconciled figure. That is for Tommy's attention only; the claim is never reworded.

## Other candidates tested

- Chips via MITI: fails as a gate on Johor halls. The permit covers chips leaving Malaysia, not chips installed in it. The US BIS licence does bind China-headquartered tenants' new chips. The piece uses it as one pace-setter, not the whole story.
- Water: not repeated. SPAN's primary data puts Johor at 14.3% in 2025, inside SPAN's 10 to 15% band (johor-waits-on-the-treatment-plant sidecar).
- Grid charges: not repeated. TNB bills each campus's own connection to its developer (malaysia-keeps-the-wires-shared sidecar).
- Rents and capex: SemiAnalysis's point (Johor rents and build costs higher, capex inflation and overrun risk). It is theirs, I found no primary source behind it, and it is not used.

## Source URLs (accessed 30 Oct 2026)

- https://www.tnb.com.my/assets/quarterly_results/Analyst_Briefing_-_2QFY2026.pdf (28 Aug 2026)
- https://www.tnb.com.my/assets/quarterly_results/Analyst_Briefing_-_2QFY2025.pdf, _4QFY2025.pdf, _1QFY2026.pdf (trend only)
- https://www.sec.gov/Archives/edgar/data/2118192/000119312526414188/d223752df1.htm (DayOne F-1, 5 Oct 2026)
- https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf (31 May 2026)
- https://www.miti.gov.my/miti/resources/Media%20Release/[FINAL]%5FMITI%5FPress%5FStmt%5FMalaysia%5FRegulates%5FTrade%5Fof%5FUS%5FAI%5FChips%5F2025-07-14.pdf (14 Jul 2025)
- https://www.parlimen.gov.my/files/hindex/pdf/DR-13102026.pdf (13 Oct 2026)
- https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power (30 Dec 2025, free text only)
- https://newsletter.semianalysis.com/p/the-chinese-ai-infrastructure-boom (25 Sep 2026, free text only)
- https://newsletter.semianalysis.com/p/how-oracle-is-winning-the-ai-compute-market (30 Jun 2025, free text only)
- https://www.malaymail.com/news/malaysia/2026/01/16/js-sez-projects-wont-affect-johors-electricity-or-water-supply-says-mb/205652 (press, 3,885 MVA, not used)
- https://berita.rtm.gov.my/nasional/senarai-berita-nasional/senarai-artikel/johor-jamin-pelaburan-js-sez-tidak-jejas-bekalan-asas-rakyat/ (press, not used)

## Publish notes

Link targets: only the-queue-not-the-chip (live). Not linked: either held Johor draft. No banned company names. No dashes in the piece, cover or this file. Reset `date` at publish.
