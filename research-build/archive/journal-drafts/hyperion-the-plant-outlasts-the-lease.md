# Sidecar: hyperion-the-plant-outlasts-the-lease (draft, 29 Oct 2026)

Piece: src/content/journal/hyperion-the-plant-outlasts-the-lease.md (draft: true)
Cover: public/covers/hyperion-the-plant-outlasts-the-lease.svg
Title: "Meta can hand back its Hyperion campus after four years. The power plants stay"

## The claim

**Proposed (one sentence):** At Meta's Hyperion campus the longest and hardest commitment is the power, not the building: Meta's lease of the campus can end after a four-year first term from 2029, but the gas plants Entergy Louisiana is building for it carry a power agreement that runs well past the lease (Entergy has said 15 years), backed by Meta's own guarantee, and stay in Louisiana's power system for decades, so the Blue Owl financing changed who holds the building and not who is bound to the power.

**Alternatives considered:**
1. "Hyperion's gas plants, not its buildings, set when the campus can run: the lease starts in 2029 because Entergy's plants arrive in 2028 and 2029." Dropped: the timing link is inferred, Meta never says the lease date was set by the plants.
2. "The financing moved Hyperion's risk to bond investors, but Louisiana households hold the tail risk on the plants." Dropped: the tail-risk half rests on redacted contract terms (the early termination fee size is not public) and repeats pjm-sends-the-bill.

Chose the proposed claim because every leg is in a primary document (Meta 10-K and 10-Q for the lease and guarantee, Entergy 10-K and the LPSC term sheet for the plants, guarantee, reporting duty and planned 2040s plants), and the falsifier is observable through a reporting duty the settlement itself creates.

**Flag on the 15-year term (Tommy, please read):** the length of the electric service agreement's "Original Term" is redacted in the public settlement term sheet and does not appear in Entergy's or Meta's SEC filings. "15-year" is Entergy's own description as reported: Entergy Louisiana VP Larry Hand called it "the 15-year power agreement" (Louisiana Illuminator, 27 Feb 2026), and Entergy's 27 March 2026 release, as quoted by the Shreveport Bossier Journal, refers to "the prior 15-year agreement". I could not open Entergy's own copy of that release. The piece therefore says "Entergy describes it as a 15-year agreement", attributed, not stated as a filed fact. If Tommy wants only filed facts, swap that sentence for "Its length is confidential, but it runs well past the lease" and drop "fifteen" from the falsifier.

## Proposed src/data/claims.ts entry

```ts
  {
    id: 'hyperion-the-plant-outlasts-the-lease',
    claim: 'At Meta\'s Hyperion campus the binding, long-dated commitment is the power, not the building: Meta\'s lease can end after a four-year first term from 2029, while the gas plants built for it carry a power agreement that runs well past the lease (Entergy has said 15 years), backed by Meta\'s own guarantee, so the financing moved who holds the building and not who is bound to the power.',
    breaksIf: 'Before Meta\'s first Hyperion lease term ends in 2033, the electric service agreement with Entergy Louisiana is shortened or cancelled, or Meta\'s parent guarantee behind it is released or replaced by the joint venture\'s; or the power agreement is cut back to match the lease.',
    watch: ['Entergy letters to the LPSC on any material change to the Meta electric service agreement (due within 30 days, docket U-37425)', 'Franklin Farms Units 1 and 2 in service in 2028 and Waterford 5 in 2029, per Entergy filings', 'Meta\'s Hyperion lease starting in 2029 and whether it is renewed at the first option', 'The LPSC vote on the second Meta agreement and seven more plants, scheduled for December 2026'],
  },
```

## Map layer (src/data/stack.ts)

`grid` (The grid connection), beside pjm-sends-the-bill: the mechanism is a utility building generation and lines to serve a load under a regulator's order and a service contract, not power made behind the meter. Second choice: `operators`, if Tommy reads it as a piece about how a campus is held.

## Glossary (src/pages/glossary.astro)

Under "Getting power to the building":
- **Combined cycle gas plant**: a power station that burns gas in a turbine, then uses the turbine's waste heat to raise steam for a second turbine, getting more electricity from the same gas.
- **Electric service agreement**: the contract between a utility and a large customer to supply and pay for power, often with minimum monthly charges and a fee for leaving early.
- **Minimum monthly charge**: the part of a large customer's bill that is due whether or not it uses the power, so the utility recovers what it built.

Under "What the factory makes" or wherever finance-adjacent terms sit (only if Tommy wants it):
- **Residual value guarantee**: a tenant's promise to pay the owner part of any fall in a building's value if the tenant leaves early.

## numbers.ts (physical figures only)

```ts
  { layer: 'grid', value: '2.3 GW', what: 'New gas generation the Louisiana regulator approved in August 2025 to serve Meta\'s Hyperion campus: three combined cycle plants due in 2028 and 2029.', piece: 'hyperion-the-plant-outlasts-the-lease', asOf: '20 August 2025' },
```

(Entergy's figure is 2,262 MW.)

## LinkedIn post (§9)

```
Meta can hand back its Hyperion AI campus in Louisiana after four years. The gas plants built to power it are on a far longer clock.

Funds managed by Blue Owl own most of the campus and Meta rents it, but the power contract with Entergy runs well past the lease and stays backed by Meta. When regulators were asked whether the new ownership weakened it, they declined to act. For AI campuses, the financing moves the building around; the power is the part that binds.

I look at how Hyperion is powered, what the regulator was asked, and what would prove me wrong.

https://thephysicallayer.fyi/journal/hyperion-the-plant-outlasts-the-lease/

#AIInfrastructure #DataCentres #Energy
```

## Figures in the body and where each is verified

| Figure | Primary source |
|---|---|
| Blue Owl funds about 80% / Meta 20% (said as "majority owned") | Meta release, 21 Oct 2025; Meta 10-Q Q3 2025 Note 13 |
| About $27 billion development cost | Meta release, 21 Oct 2025; Meta 10-K 2025 |
| Four-year initial lease, renewals to 20 years, starts 2029 | Meta 10-Q Q3 2025 Note 13; Meta 10-K 2025; Meta 10-Q Q3 2026 |
| Residual value guarantee, first 16 years, capped | Meta release, 21 Oct 2025; Meta 10-Q Q3 2025 |
| LPSC approval August 2025 (vote 20 Aug, 4:1) | LPSC minutes, 20 Aug 2025; Entergy 10-K 2025 |
| Three combined cycle plants, 2,262 MW (~2.3 GW) | Entergy 10-K 2025 |
| Franklin Farms 1 and 2 in 2028, Waterford 5 in 2029 | Entergy 10-K 2025; Entergy release 20 Aug 2025 |
| Minimum monthly charges, early termination fee, parent guaranty | LPSC U-37425 settlement term sheet IV.B, IV.C (public version, 7 Aug 2025); Entergy 10-K 2025 |
| Plants treated as system resources for all ELL customers | Settlement term sheet I.A.3 |
| Entergy must report Meta's renewal status before adding resources that depend on it; notify within 30 days of material ESA change | Settlement term sheet IV.D.1.a and IV.D.4 |
| Plants pencilled in for 2041 to 2044 ("Otherwise Needed Generators") | Settlement term sheet footnote 12 |
| January 2026 motion to investigate the financing; Entergy opposed (February 2026) | Entergy 10-K 2025 |
| Commission declined to act, February 2026 | Louisiana Illuminator, 27 Feb 2026; Earthjustice release, 25 Feb 2026 (not in an Entergy filing: news-sourced) |
| "15-year" power agreement | Entergy statements as reported (see flag above); NOT in a public filing |
| Lease first term ends 2033 | Derived: commences 2029 plus four years (Meta 10-K 2025) |

## Lead-sheet figures from the video and what happened to them

From "State of AI data centres 2026" (transcript chapter "Who Pays for the Expansion?"), used as a lead only:
- 80/20 ownership, ~$27bn cost, PIMCO bonds, four-year lease with options, capped RVG for 16 years: all verified in Meta's release and filings. PIMCO not used in the piece (financing kept light).
- "Regulators approved new gas power plants in August 2025": verified (LPSC minutes).
- "No operating capacity had been reported by October cutoff": not verified either way, not used.
- No household take-home-pay analogy or video structure used.

## Not used, but verified, for the research note later

- Meta initial lease commitment about $12.3 billion (Meta 10-Q Q3 2025); RVG threshold begins at about $28 billion and declines (Meta 10-K 2025); Meta maximum exposure to its data centre ventures $68.4 billion at 30 Sep 2026, now covering a Louisiana and a Texas venture (Meta 10-Q Q3 2026).
- Blue Owl funds' cash contribution $7.0 billion; Meta one-time distribution $2.6 billion (Meta 10-Q Q3 2025; Meta's release says about $3 billion).
- Entergy Louisiana issued mortgage bonds due April 2036 and April 2056 in February 2026, partly to fund Franklin Farms 1 and 2 and Waterford 5 (Entergy 10-Q Q2 2026). A strong "longest clock" image, left out to keep the money light.
- Second Meta agreement (Evest LLC, March 2026): seven more combined cycle plants, 5,278 MW, in service 2030 and 2031, plus a 500 kV line; LPSC consideration set for its December 2026 meeting (Entergy 10-Q Q2 2026). Whether Evest's data centre is part of Hyperion is not stated in filings ("a second new data center ... in north Louisiana"), so the piece does not count it as Hyperion.
- Settlement estimate of Meta's investment "at least $10 billion" (joint motion, 7 Aug 2025), superseded by the ~$27bn JV figure.

## Sources (URL, date)

- Meta, "Meta Announces Joint Venture with Funds Managed by Blue Owl Capital to Develop Hyperion Data Center", 21 Oct 2025: https://investor.atmeta.com/investor-news/press-release-details/2025/Meta-Announces-Joint-Venture-with-Funds-Managed-by-Blue-Owl-Capital-to-Develop-Hyperion-Data-Center/default.aspx
- Meta 10-Q for quarter ended 30 Sep 2025, filed 30 Oct 2025 (Note 13): https://www.sec.gov/Archives/edgar/data/1326801/000162828025047240/meta-20250930.htm
- Meta 10-K for 2025, filed 29 Jan 2026: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
- Meta 10-Q for quarter ended 30 Sep 2026, filed 22 Oct 2026: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm
- Entergy 10-K for 2025, filed 19 Feb 2026 ("Additional Generation and Transmission Resources"): https://www.sec.gov/Archives/edgar/data/65984/000006598426000174/etr-20251231.htm
- Entergy 10-Q for quarter ended 30 Jun 2026, filed 31 Jul 2026: https://www.sec.gov/Archives/edgar/data/65984/000006598426000283/etr-20260630.htm
- Entergy 10-Q for quarter ended 31 Mar 2026, filed 1 May 2026: https://www.sec.gov/Archives/edgar/data/65984/000006598426000222/etr-20260331.htm
- Entergy Louisiana release, LPSC approval, 20 Aug 2025: https://www.entergy.com/news/entergy-louisiana-receives-lpsc-approval-for-major-infrastructure-investments-to-support-metas-data-center-and-improve-reliability
- LPSC docket U-37425, joint motion for Rule 57 approval with Final Stipulated Settlement Term Sheet (public redacted version), 7 Aug 2025: https://www.all4energy.org/wp-content/uploads/2025/08/2025-08-07-ELL-Joint-Mtn-for-Rule-57-Approval.pdf
- LPSC minutes, Business and Executive Session, 20 Aug 2025: https://lpsc.louisiana.gov/docs/minutes/August-20-2025-Minutes.pdf
- Louisiana Illuminator, "Meta's data center ownership transfer doesn't concern Louisiana power regulators", 27 Feb 2026 (via Yahoo copy): https://lailluminator.com/2026/02/27/no-investigation-of-data-center-ownership-transfer/ and https://www.yahoo.com/news/articles/meta-data-center-ownership-transfer-184400871.html
- The Lens, LPSC approval report, 21 Aug 2025 (Larry Hand on 2041): https://thelensnola.org/?p=604759
- Shreveport Bossier Journal, Entergy and Meta expansion agreement, 30 Mar 2026 (quotes Entergy's "prior 15-year agreement"): https://shreveportbossierjournal.com/2026/03/30/entergy-louisiana-meta-announce-massive-expansion-agreement-seven-new-power-plants-2-65-billion-in-customer-savings/
- T&D World, Entergy Louisiana additional agreement with Meta, 1 Apr 2026: https://www.tdworld.com/utility-business/news/55368019/entergy-louisiana-announces-additional-agreement-with-meta-to-support-hyperscale-data-center-in-northeast-louisiana
- Lead sheet only: "State of AI data centres 2026" video, data to 5 Oct 2026, transcript at research-build/source-ai-datacentre-video/TRANSCRIPT.md
