# Sidecar: homer-city-inherits-the-air (draft, 29 Oct 2026)

Piece: src/content/journal/homer-city-inherits-the-air.md (draft: true)
Cover: public/covers/homer-city-inherits-the-air.svg
Title: "Homer City's new gas plant is built on the old coal plant's air"
Batch 3, Tier A item A8. Reframed from the outline ("arrives turbine by turbine"), see below.

## Why the outline was reframed

The outline claim ("under half of seven turbines running by end-2028", delivery slots and gas setting the steps) cannot rest on primary sources: no unit-by-unit schedule, GE Vernova slot dates or EQT ramp is public. The developer only says first turbine deliveries 2026 and first power early 2028. A turbine-by-turbine piece would also repeat abilene-switched-on-in-stages (staged arrival) and ge-vernova-sells-the-wait (slots), and the grid-position and water reuse angle repeats darlington-builds-on-the-old-plug and constellation-restarts-the-reactor.

The DEP permit record shows a mechanism the site does not have: the retired coal boilers' recent emissions let a plant more than twice the size net out of federal major-source review for NOx and CO, a credit that only counts within a five-year contemporaneous window and is spent once made enforceable. No journal piece mentions air permits, netting or emission credits (grepped).

## The claim (revised after fact-check, 29 Oct 2026)

**Proposed (one sentence):** At Homer City the closed coal plant's air record did more than its wires: the coal boilers' 2021 to 2022 emissions let a gas plant of up to 4,678 megawatts, more than twice the old station, net NOx out of both federal PSD review and Pennsylvania's nonattainment review, so it bears neither the lowest achievable emission rate nor 1.15 to 1 NOx offsets that a greenfield plant in the Ozone Transport Region would, a credit that only counts if construction starts within five years of the cut.

Narrowed from the first draft: no primary source ranks air above wires in general or measures how scarce such sites are, so the "scarcest land" line is gone. Reconciled openly with constellation-restarts-the-reactor (its scarce thing was the borrowed grid connection); at Homer City the power reaches AWS through FirstEnergy's grid (AWS narrative), and the 2023 deactivation work reportedly removed the 345/230 kV generator leads (PJM TEAC, from a search summary, not opened).

**Alternatives considered:**
1. "Homer City arrives turbine by turbine: under half of its seven 7HA.02 units run by end-2028." Dropped: no primary unit schedule; repeats Abilene and GE Vernova.
2. "Homer City's ten Mitsubishi FT8 aeroderivatives are the bridge before the 7HA units." Dropped: the permit lists them but nothing public says they run first; overlaps A9.

## Proposed src/data/claims.ts entry

```ts
  {
    id: 'homer-city-inherits-the-air',
    claim: 'At Homer City the closed coal plant\'s air record did more than its wires: the coal boilers\' 2021 to 2022 emissions let a gas plant more than twice the old station\'s size net NOx out of both federal and Pennsylvania nonattainment review, sparing it the strictest controls and the 1.15 to 1 NOx offsets a greenfield plant in the Ozone Transport Region would bear, a credit that counts only if construction starts within five years of the cut.',
    breaksIf: 'Before Homer City\'s first power, targeted for early 2028, the Environmental Hearing Board sets aside or remands plan approval 32-00457A over its netting, or DEP requires Homer City to obtain NOx emission reduction credits; or a greenfield gas plant of a gigawatt or more in the Ozone Transport Region secures its NOx offsets and plan approval on a comparable timeline (Homer City: application 4 April 2025, approval 18 November 2025).',
    watch: ['EHB docket 2025-135-L (Clean Air Council, PennFuture and Sierra Club; objection E on PSD and NSR applicability) and 2025-136-L (McIntosh v. DEP)', 'Any DEP modification of plan approval 32-00457A, and the Title V modification making the coal reductions enforceable', 'Homer City first power, targeted early 2028', 'Plan approvals and NOx ERC purchases for large greenfield gas plants in Pennsylvania and the wider Ozone Transport Region'],
  },
```

## Fact-check fixes applied (29 Oct 2026)

- EHB opinion of 11 Sep 2026 in 2025-135-L read in full (ehb.pa.gov slip opinions; scanned PDF, read as page images): it is an Opinion and Order on Petition to Intervene, granting pro se intervention by James Harris limited to the issues in the notice of appeal. Not a merits ruling. It records written discovery complete, depositions under way under a joint case management order, and a Harris supersedeas petition pending. It describes the appeal as challenging emission limits and "the Department's determination regarding emissions reduction credits for criteria pollutants". https://ehb.pa.gov/_files/ugd/f1e5f9_9ccd0a9c8e034bab8987d8e2fa002115.pdf
- Two appeals: 2025-135-L (groups) and 2025-136-L (McIntosh v. DEP, youth); consolidation refused 23 Mar 2026 (https://ehb.pa.gov/_files/ugd/ad7b29_521b8bb94a4e45ebb73e4ad17514f4a9.pdf). The piece says "two appeals".
- Notice of appeal dated 17 Dec 2025: no objection names netting. Objection E attacks PSD and NSR applicability for failing to consider the whole project including the data centre campus (could reach netting indirectly); objection H attacks ERCs under 127.206(c) and 127.208(3), (4) (the VOC credits). The piece says the groups' appeal "does not object to the netting directly". I did not read the youth notice of appeal; the EHB March order describes it as different in kind (Environmental Rights Amendment).
- NOx netted out of both PSD and NNSR: DEP comment response p.2 ("below the PSD and NNSR significance threshold of 40 tpy, so PSD and NNSR review was not triggered for Nitrogen Oxides"). So no NOx LAER and no NOx offsets.
- State rules: five-year window, 25 Pa. Code 127.203a(a)(1)(ii)(B) (contemporaneous: 5 years before construction commences to completion); federal 40 CFR 52.21(b)(3)(ii). Offset ratio 1.15:1 for NOx in the Transport Region, 25 Pa. Code 127.210(a).
- Title V: DEP's technical memo says the reductions "are being made federally enforceable through a modification to the facility's Title V Operating Permit". Final issuance of that modification is UNCONFIRMED (proposed at 55 Pa. Bull. 7611, 1 Nov 2025). The piece no longer says it was written in.
- Knighthead: piece now says it "invests in it and leads its financing" (Homer City FAQ: equity positions for nearly eight years, leads financing). Ownership share not confirmed.
- "Half a century" dropped (opening year not verified).

## Map layer (src/data/stack.ts)

`onsite` (Power on site), beside constellation-restarts-the-reactor: generation built on a campus for its data centres. Note the power reaches AWS through FirstEnergy's grid (AWS narrative), so `grid` is the second choice.

## Glossary (src/pages/glossary.astro)

Under "Getting power to the building":
- **Netting**: counting a recent emissions cut at the same site against a new plant's increase, so the project can avoid the full federal review for that pollutant.
- **Emission reduction credit**: a certified, permanent cut in pollution elsewhere that a new plant buys and surrenders to offset its own emissions.
- **Greenfield**: a site with no previous industrial use, and so no existing connections or permits to reuse.
NOx and Aeroderivative already exist. Combined cycle gas plant is proposed in the Hyperion sidecar; add it if that piece has not.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '4,678 MW', what: 'Maximum capacity Pennsylvania permitted for the gas plant on the former Homer City coal site, more than twice the old station\'s about 2,000 MW.', piece: 'homer-city-inherits-the-air', asOf: '18 November 2025' },
```

## LinkedIn post (§9)

```
At Homer City, the closed coal plant's old smoke did more for the new gas plant than its wires.

The coal boilers' recent emissions let a gas plant more than twice the size clear NOx from both the federal and Pennsylvania reviews, so it buys no NOx offsets and faces no strictest-control test. That credit only counts within five years of the cut.

I look at how Homer City's permit works, what the regulator recorded, and what would prove me wrong.

https://thephysicallayer.fyi/journal/homer-city-inherits-the-air/

#AIInfrastructure #DataCentres #Energy
```

## Figures in the body and where each is verified

| Figure | Primary source |
|---|---|
| Coal plant not producing power since 2023 | DEP comment response, 18 Nov 2025, p. 1 |
| Up to 4,678 MWe, more than twice the old ~2,000 MWe | DEP comment response, 18 Nov 2025; DEP technical review memo |
| 39 data centres | AWS project narrative to Indiana County, dated 27 Aug 2026 (press reports say 36 from the site plan; the narrative itself says 39) |
| Seven GE Vernova 7HA.02 combined cycle, ten Mitsubishi FT8 aeroderivatives | DEP technical review memo and plan approval 32-00457A, 18 Nov 2025 |
| 2021 to 2022 baseline | DEP technical review memo |
| NOx +1,142.8 tpy, creditable decrease 2,031.8 tpy (net -889.0) | DEP comment response, 18 Nov 2025, p. 2 |
| Five-year contemporaneous window | 25 Pa. Code 127.203a(a)(1)(ii)(B); 40 CFR 52.21(b)(3)(ii) (law.cornell.edu; eCFR blocked) |
| NOx cleared both PSD and NNSR; LAER otherwise | DEP comment response p.2 and LAER definition p.2 to 3 |
| Title V modification (no longer in the piece) | DEP technical review memo says "being made"; final issuance unconfirmed |
| NOx offsets in the Ozone Transport Region at 1.15:1 | 25 Pa. Code 127.210(a) |
| 369 tpy VOC ERCs before operation | Plan approval 32-00457A condition; DEP comment response |
| November 2025 approval | Plan approval issued 18 Nov 2025 |
| First gas turbine set on its foundation | Homer City Generation release, 20 Oct 2026 (Business Wire, read via OffshoreSource syndication) |
| First power targeted early 2028 | Homer City Redevelopment release, 26 Mar 2026 (Business Wire 403; read via 01net.it syndication) |
| Two appeals pending at the EHB; groups' appeal pleads no direct netting objection | Notice of appeal dated 17 Dec 2025 (cleanair.org); EHB orders of 23 Mar and 11 Sep 2026 (pending, discovery under way) |

Derived, not stated in the piece: without netting, 1,142.8 tpy of NOx at 1.15:1 would need about 1,314 tpy of NOx credits. Left out as my arithmetic.

## Video figures dropped or flagged

From "GE Vernova Explained: The Power Bottleneck Behind the AI Boom" by Leo Cui (TRANSCRIPT.md), lead only:
- "About four and a half gigawatts": flagged. Developer said up to 4.5 GW (Apr 2025), then approximately 4.4 GW (FAQ; 26 Mar 2026 release); AWS narrative says 4.5 GW; DEP permits up to 4,678 MWe. The piece uses the DEP figure.
- "Seven GE Vernova gas turbines": verified (7HA.02, DEP). The video omits the ten FT8 aeroderivatives, which the piece adds.
- "Homer City was once the state's largest coal-fired power plant": not verified, not used.
- No video structure, wording or analogy used.

## Verified but not used (for a research note)

- EQT agreement in principle, 15 Jul 2025: up to 665,000 MMBtu a day, from Texas Eastern and Eastern Gas Transmission and Storage (EQT/Homer City release). Agreement in principle only; no definitive agreement found.
- CO netting: +1,104.8 tpy, decrease -4,096.5, net -2,991.7. SO2 net -4,248.8 tpy.
- PSD still applies to PM, PM10, PM2.5, H2SO4 and GHG (BACT); CO2 limit 800 lb/MWh for combined cycle, 1,425 lb/MWh for FT8.
- Plan approval lapses if construction is not commenced within 18 months of issue or lapses for 18 months.
- VOC ERCs proposed at 55 Pa. Bull. 7611 (1 Nov 2025); contested in Earthjustice/Clean Air Council comments, 1 Dec 2025.
- AWS narrative: power acquired from FirstEnergy "supported by" the plant; AWS pays for new electrical infrastructure; construction Dec 2026 to 2036 in six phases; cooling water from existing withdrawal rights, holding the historic withdrawal rate.
- 2023 deactivation work included removing the 345 kV and 230 kV generator leads at Homer City (PJM TEAC, per search summary, not opened); so the "old plug" was partly dismantled. Not used.
- Kiewit on site since October 2025; HRSGs arriving from September 2026; workforce above 2,000 (20 Oct 2026 release).

## Sources (URL, date)

- DEP technical review memo, 18 Nov 2025: https://files.dep.state.pa.us/RegionalResources/NWRO/NWROPortalFiles/Homer-City/Air/Final-AQ-Plan-Approval/Tech%20Review%20Memo%20Signed%2020251118.pdf
- DEP plan approval 32-00457A, 18 Nov 2025: https://files.dep.state.pa.us/RegionalResources/NWRO/NWROPortalFiles/Homer-City/Air/Final-AQ-Plan-Approval/FINAL%20PLAN%20APPROVAL%2032-00457A.pdf
- DEP comment response document, 18 Nov 2025: https://files.dep.state.pa.us/RegionalResources/NWRO/NWROPortalFiles/Homer-City/Air/Final-AQ-Plan-Approval/Final%20Comment%20Response%20Document%2020251118.pdf
- 40 CFR 52.21: https://www.law.cornell.edu/cfr/text/40/52.21
- 25 Pa. Code 127.210: https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/025/chapter127/s127.210.html
- GE Vernova / Homer City / Kiewit release, 2 Apr 2025: https://gevernova.com/news/press-releases/homer-city-redevelopment-kiewit-announce-country-largest-natural-gas-powered-data-center-support-ai-hpc-demand
- Homer City Redevelopment FAQ (read 29 Oct 2026): https://www.homercityredevelopment.com/faq
- Homer City release, 26 Mar 2026 (1,000 workers, first power early 2028): https://www.businesswire.com/news/home/20260326477595/en/ (read via https://www.01net.it/homer-city-redevelopment-reaches-1000-workers-on-construction-site/)
- Homer City Generation release, 20 Oct 2026 (Kiewit one year, first turbine set): https://offshoresource.com/business-wire/homer-city-generation-highlights-kiewits-one-year-anniversary-of-being-active-on-site-as-engineering-procurement-and-construction-partner/
- EQT agreement in principle, 15 Jul 2025: https://www.businesswire.com/news/home/20250715006970/en/
- AWS project narrative, 27 Aug 2026: https://media-cdn.socastsrm.com/wordpress/wp-content/blogs.dir/2140/files/2026/09/pit100-project-narrative-082726.pdf
- EHB Opinion and Order on Petition to Intervene, 2025-135-L, 11 Sep 2026: https://ehb.pa.gov/_files/ugd/f1e5f9_9ccd0a9c8e034bab8987d8e2fa002115.pdf
- EHB Opinion and Order on Motion to Consolidate, 23 Mar 2026: https://ehb.pa.gov/_files/ugd/ad7b29_521b8bb94a4e45ebb73e4ad17514f4a9.pdf
- 25 Pa. Code 127.203a: https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/025/chapter127/s127.203a.html
- Clean Air Council notice of appeal, dated 17 Dec 2025: https://cleanair.org/wp-content/uploads/Notice-of-Appeal__Plan-Approval-No.-32-00457A.pdf
- Earthjustice et al. VOC ERC comments, 1 Dec 2025: https://earthjustice.org/wp-content/uploads/2026/08/2025-12-01-homer-city-ercs-cac-et-al-comments-w-attachments.pdf
- Press, status only: Lehigh Daily (Sept 2026) https://lehighdaily.com/homer-citys-coal-site-now-has-1800-workers-as-courts-weigh-the-data-center-plants-permit/ ; WESA, 21 Jul 2026 https://www.wesanews.org/environment-energy/2026-07-21/pennsylvania-environmental-homer-city-data-center
- Lead sheet only: video "GE Vernova Explained: The Power Bottleneck Behind the AI Boom", https://www.youtube.com/watch?v=TiHQJVK9Kk4, research-build/source-watch-later/ge-vernova-power-bottleneck/TRANSCRIPT.md
