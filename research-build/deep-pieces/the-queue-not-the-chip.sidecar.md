# Sidecar: the-queue-not-the-chip (deep piece 1 of 11, prototype)

Cluster 1, "Johor and Singapore: the plug, not the chip". Drafted 30 Oct 2026 as the format prototype for §D. Piece: `research-build/deep-pieces/the-queue-not-the-chip.md` (draft: true). Kept outside `src/content/journal/` on purpose so the loader does not read it. Nothing committed, published or scheduled. No existing file edited.

## Shape and counts

- Title: "Johor and Singapore: the plug, not the chip, decides who gets to build" (12 words, sentence case, names both subjects).
- Top layer (cold open, analogy, How it works, The number that matters): about 508 words, 12 figures, 0 company financial figures. Analogy about 70 words. Average sentence about 14 words.
- Investor layer: about 2,480 words before the exposure map (inside the 1,200 to 2,500 band), about 2,810 with the map (about 130 words) and sources. Whole body about 3,320 words by token count.
- Revised 30 Oct 2026 after the coordinator's fact-check (11 points); see "Fact-check fixes applied" below.
- `brand/check-piece.py`, run on a scratch copy: 0 punctuation, spelling or valuation failures. It still FAILS on length (3,260) and figures (209) and warns on sections, map and sources length, because the checker still enforces the retired §3 and §4b rules. **check-piece.py needs §D rules (count the top layer only for the 550 word and 15 figure caps) before any deep piece can publish.**
- The layout needs CSS for `hr.layer` and `p.layer-label`; neither exists in `src/` yet.

## Frontmatter notes

- `date: 2026-07-27` is kept as a placeholder only. **At go-live it becomes the real publish time** (`YYYY-MM-DDTHH:MM:SS+08:00`). The three live claims keep their original dates (27 July and 22 September 2026), which is why claims.ts needs a `date` field (below): today the claims page takes each claim's date from its piece, so republishing this slug would silently re-date the July claim.
- Slug stays `the-queue-not-the-chip` (most-linked URL; also in `READING_PATH` in `src/config.ts`, which needs no change).
- `cover: "/covers/queue.svg"` (existing) until a new cover is drawn; proposal below.
- Tags: grid, power, johor, singapore (all existing).

## Thesis and how it treats the old claims

Thesis: in both places the plug, not the chip, decides who gets to build. Singapore rations it; Johor books it years before tenants fill it, so booked megawatts overstate computing at work.

SemiAnalysis credit: power-gated (US), chip-gated (China), "the grid is sold out" and about a terawatt of requests are attributed to SemiAnalysis by name. "The grid is sold out" first appeared in its report of 13 Mar 2024 and is repeated in the 30 Dec 2025 piece; the cold open says "as the firm has put it since 2024" and the sources line cites both dates. (Title of the 13 Mar 2024 report not re-checked by me; the date is the fact-checker's.) Tommy's contribution is stated modestly: SemiAnalysis itself calls Inner Mongolia "China's Johor", so the piece says only that it places Johor and Singapore on their own regulators' figures. Only free text used. ByteDance attributed to SemiAnalysis's free article of 30 Jun 2025.

"Where later evidence cuts against it" notes, in the Claims on record block:
- the-queue-not-the-chip: now framed on the Malaysia-wide ratio (Johor two thirds of secured capacity); wrong for campuses already connected, holds for Singapore and campuses waiting to connect; notes Tenaga's 2023 release says 36 to 48 months.
- the-part-money-cannot-hurry: "Where I was wrong". Tenaga's 9 Aug 2023 release cut the whole implementation period, plant included, so the equipment clock is not shown to bind on Malaysia's own connections. The old bold line "the floor is made of steel and copper" is replaced by "Malaysia has shown the queue can be shortened. It has not yet had to show the factories can keep up."
- two-governments-one-confession: the falsifier's first limb is addressed openly. Tenaga's deck p.6 splits base capex RM26.55bn as energy transition 12.10 (46%), security of supply 10.96 (41%), demand growth 3.49 (13%, "data centres and industries"); data centre connection sits mainly in the RM16.27bn contingent allowance, "activated upon trigger events". The piece says this weakens the Malaysian half. Also "Singapore cannot make more" was too strong (five gas plants by 2031).

## Needed edit to another file (not made; for Tommy or the merge step)

`src/content/journal/abilene-switched-on-in-stages.md` (scheduled draft) contradicts this thesis in two places: it says chips go in "in months", and "I have argued that Johor is short of [connections, not chips](/journal/the-queue-not-the-chip/)." Proposed: replace the second with "I have argued that Johor connects its campuses faster than tenants fill them" (linking the same URL, which this piece keeps), and soften "in months" to say chips arrive on the tenant's schedule, which for some tenants includes a US export licence. Not edited, per instruction.

## Proposed claims.ts change (existing entries untouched)

Two additions to the type, which the consolidation plan already anticipates (check-piece.py, check-call.py and claims.astro need small code changes to read them):

```ts
export type Claim = {
  id: string;
  claim: string;
  breaksIf: string;
  watch: string[];
  piece?: string;  // the deep piece the claim now lives in; defaults to id
  date?: string;   // the date the claim was first published; defaults to the piece date
};
```

At merge, the three live entries gain only `piece: 'the-queue-not-the-chip'` (for the two absorbed slugs) and `date` (2026-07-27 for the-queue-not-the-chip, 2026-09-22T18:48:00+08:00 for the-part-money-cannot-hurry, 2026-09-22T19:40:00+08:00 for two-governments-one-confession). `claim`, `breaksIf` and `watch` are not touched. This is metadata, not rewording, but it is a change to existing entries, so Tommy should approve it explicitly.

New entry:

```ts
  {
    id: 'the-plug-not-the-chip',
    piece: 'the-queue-not-the-chip',
    claim: 'In Johor and Singapore the grid connection, not the chip, decides who gets to build: Malaysia\'s data centres, two thirds of whose secured capacity is in Johor, will draw less than 40% of the maximum demand of the data centre projects in Tenaga\'s system at June 2027, and Singapore will add data centre capacity only through calls for applications with efficiency and green energy conditions.',
    breaksIf: 'Tenaga\'s figures for June 2027 show Malaysia\'s data centre load at 40% or more of the maximum demand of the data centre projects in its system, or, before 1 January 2028, Singapore allocates capacity to a new data centre, or new capacity to an existing one, other than through a call for applications carrying efficiency and green energy conditions. Capacity regained by redeveloping or replacing an existing hall within its current allocation, and capacity allocated before 30 October 2026, do not count.',
    watch: ['Tenaga\'s data centre load against maximum demand in system, each quarter (1,256 MW against 5.65 GW, June 2026)', 'Dewan Rakyat figures for signed, operating and drawn data centre load (1.37 GW of 6 GW operating, August 2026), and the Energy Commission study of actual requirements', 'BIS licensing of advanced chips to entities headquartered in Country Group D:5, and DayOne\'s customer concentration', 'Singapore\'s next Data Centre Call for Application (review 18 to 24 months from August 2026) and any capacity allocated outside a call', 'IMDA\'s first efficiency regulations for existing halls under the Digital Infrastructure Act'],
  },
```

The causal "so" is gone: under 40% fits ramp and overbooking as well as chips, and the falsifier section says so. Why 40% is a real test: on Tenaga's series the share drawn went from about 17% (June 2025) to 22% (June 2026). If load doubles again to about 2.5 GW while most of the 2.21 GW under construction enters the system, the ratio is about a third. Faster filling or slower connecting breaches 40%. The Singapore limb is a genuine risk too: MDDI says there is no fixed ceiling, and a direct allocation (for example on Jurong Island) before the next call would break it.

Alternatives considered: (A) a Johor-only fill test: not observable, Tenaga publishes no Johor-only draw. (B) "Johor is chip-gated for Chinese tenants": not observable, no licence or tenant split is published. (C) the held drafts' water and tariff claims: both failed their primary re-checks.

## Redirect map

Live and scheduled-draft URLs (the five that need redirects):

| Old URL | Redirect to |
|---|---|
| /journal/two-governments-one-confession/ | /journal/the-queue-not-the-chip/#two-governments-one-confession |
| /journal/the-part-money-cannot-hurry/ | /journal/the-queue-not-the-chip/#the-part-money-cannot-hurry |
| /journal/singapore-cannot-wait-for-the-cable/ | /journal/the-queue-not-the-chip/#singapore-cannot-wait-for-the-cable |
| /journal/singapore-licenses-the-old-halls/ | /journal/the-queue-not-the-chip/#singapore-licenses-the-old-halls |
| /journal/johor-plugs-in-before-it-fills/ | /journal/the-queue-not-the-chip/#johor-plugs-in-before-it-fills |

The held drafts (johor-waits-on-the-treatment-plant, malaysia-keeps-the-wires-shared) were never live, so they need no redirect, but their anchors exist in the piece in case a redirect is wanted anyway. `#the-queue-not-the-chip` is anchored on the Malaysia queue section for completeness. Inbound links already on the site (abilene, fairwater, hitachi-energy-plans-the-queue, room-to-spare, the-way-out-has-its-own-queue, the-rack-runs-out-of-copper, tsmc-says-it-is-the-bottleneck) and in `brand/linkedin-posts.md` resolve through these redirects. At merge, the five draft and two held files leave `src/content/journal/` and go, with the three live originals, verbatim into `research-build/archive/pieces/`.

Sections and anchors, in order: The mechanism in depth; Malaysia's queue (#the-queue-not-the-chip, #the-part-money-cannot-hurry); Johor: plugged in faster than it fills (#johor-plugs-in-before-it-fills); Malaysia's bill (#malaysia-keeps-the-wires-shared); Johor's water (#johor-waits-on-the-treatment-plant); Singapore rations what Malaysia builds (#two-governments-one-confession); Singapore's green power (#singapore-cannot-wait-for-the-cable); Singapore's old halls (#singapore-licenses-the-old-halls); Claims on record; What would prove me wrong; Research notes.

## stack.ts

Layer `grid` ("The grid connection"). At merge, the grid list becomes:
`pieces: ['the-queue-not-the-chip', 'hitachi-energy-plans-the-queue', 'siemens-energy-measures-the-shortage', 'the-power-it-drops', 'pjm-sends-the-bill']`
(removing the-part-money-cannot-hurry and two-governments-one-confession; the other entries move when their own clusters merge). The johor-plugs sidecar had proposed `operators`; the deep piece's lead mechanism is the connection, so `grid` is right, and the operators layer gets the fill point through cluster 11.

## Glossary (src/pages/glossary.astro)

"Getting power to the building":
- Maximum demand: The most power a customer may draw at once, booked in its supply agreement with the utility. A data centre books it for its finished size and fills it over years.
- Energy supply agreement: In Malaysia, the contract between Tenaga Nasional and a large new customer that fixes the maximum demand the grid will provide.
- Green Lane Pathway: Tenaga Nasional's fast-track connection route for data centres, launched in August 2023, which cut supply delivery from 36 to 48 months to about 12.
- Connected load charge: In Malaysia, a penalty on a large new customer drawing less than 85% of the demand it declared, phase by phase, in its first four years, charged per kilowatt of shortfall.
- Ultra high voltage tariff: Malaysia's tariff class, from 1 July 2025, for data centres connected above 50 kilovolts. Its energy charge is higher than ordinary high voltage users pay; its capacity and network charges are the same.
- Subsea power cable: An armoured high voltage cable laid on the seabed to carry power between countries. Made to order in a few specialist factories.
- Converter station: The plant at each end of a direct current link that turns alternating current into direct current and back. Built to order.
- Electricity Importer Licence: In Singapore, the full licence from the Energy Market Authority that lets an import project build and operate. It comes after a conditional approval or licence.
- Data Centre Call for Application: Singapore's competitive process, run by EDB and IMDA, for handing out new data centre capacity under efficiency and green power conditions.
- Critical IT load: The most power a data centre is designed to deliver to its servers. Singapore licenses halls of 3 MW and up and states it on each licence.

"Chips, memory and the wiring between them":
- Export licence (advanced chips): US permission needed to ship advanced AI chips to any company headquartered in China, or whose parent is, wherever its subsidiary sits.

"Inside the building":
- Reserve margin (water): Spare water treatment capacity above average intake. Malaysia's regulator SPAN targets 10 to 15%.
- Megalitre: A million litres. Malaysian water capacity is quoted in megalitres a day.

Already present, no change: PUE, HVDC, Interconnection queue, Substation, Transformer (the grid kind), Grain-oriented electrical steel, Switchgear, Announced versus energised megawatts.

## numbers.ts (physical only)

New:
```ts
  { layer: 'grid', value: '1.26 GW of 5.65 GW', what: 'Data centre load Tenaga Nasional supplied across Malaysia in June 2026, against the maximum demand booked by the data centre projects in its system. Johor holds two thirds of Malaysia\'s secured data centre capacity.', piece: 'the-queue-not-the-chip', asOf: 'June 2026' },
  { layer: 'grid', value: '~6 GW', what: 'Low-carbon electricity Singapore aims to import by 2035, all by subsea cable. Every one of the 13 projects approved so far is still conditional.', piece: 'the-queue-not-the-chip', asOf: 'August 2026' },
  { layer: 'grid', value: '3 MW', what: 'Critical IT load from which a Singapore data centre needs an IMDA licence stating the capacity it may run, existing halls included. About 70 are in scope.', piece: 'the-queue-not-the-chip', asOf: 'October 2026' },
```
Existing entries needing Tommy's decision at merge (not edited now):
- The "36 to 12 months" entry and `1.25` point at two-governments-one-confession; repoint `piece` to the-queue-not-the-chip (the redirect would also work). The Green Lane figure is "36 to 48 months" in Tenaga's own 2023 release; a `note` would record that.
- `3.8 GW` (Johor, 2025) points at the-queue-not-the-chip and is a Wood Mackenzie figure, not primary. The deep piece no longer uses it. Suggest replacing it with the Tenaga entry above, with a `note`.

## LinkedIn post (§9)

```
Malaysia's data centres draw less than a quarter of the power they have booked from the grid.

Johor holds two thirds of Malaysia's secured data centre capacity, and across the causeway Singapore allocates new capacity in rationed batches, 200 megawatts provisionally in August. In both, the connection decides who gets to build. In Johor, the halls then fill only as fast as tenants bring chips, some of which need an American licence.

The piece covers the three clocks every campus passes, what Tenaga and Singapore's regulators publish, and the claims I have on record.

https://thephysicallayer.fyi/journal/the-queue-not-the-chip/

#DataCentres #Grid #SoutheastAsia
```
Note: this URL already has a live post (July). LinkedIn caches the card by URL, so a new cover means bumping `OG_VERSION` and running Post Inspector (§8 step 6).

## Cover proposal (not drawn)

`/covers/the-queue-not-the-chip.svg` (new file at merge; queue.svg stays for the archive). One idea: the causeway seen from above, a single amber line crossing a dark strait. On the Singapore side, a small fuse box with three amber sockets, two of them capped (rationed). On the Johor side, a row of six plugs all lit amber at the socket, with only one or two blue chip squares behind them (connected, not filled). Caption in letter-spaced grey: "JOHOR AND SINGAPORE: THE PLUG, NOT THE CHIP". Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

## Sources, every one with date

Re-opened by me on 30 Oct 2026:
- Tenaga Nasional, Analyst Briefing 2QFY2026, 28 Aug 2026, pp.3 to 4 (load series 603, 710, 850, 1,054, 1,256 MW Jun 2025 to Jun 2026; 42 projects 5.65 GW in system; 2.21 GW under construction; 0.49 GW signed; 61 projects 8.35 GW; Johor 29 of 61, 5.6 of 8.3 GW, 67%): https://www.tnb.com.my/assets/quarterly_results/Analyst_Briefing_-_2QFY2026.pdf
- Tenaga Nasional press release, 9 Aug 2023 (Green Lane launched 8 Aug 2023; 132/275 kV; "three times faster"; 36 to 48 months to 12): https://www.tnb.com.my/assets/press_releases/2023080944_ENG.pdf
- Tenaga-hosted press clip, 29 May 2026 (33 projects by March 2026, quoting a TNB social media post): https://www.tnb.com.my/assets/newsclip/29052026a3.pdf . NOT USED: press only, no TNB primary found (searched tnb.com.my 30 Oct 2026).

From the cluster sidecars (primary, verified there, not re-opened today):
- Tenaga analyst briefings 2QFY2025, 4QFY2025, 1QFY2026 (denominators 3.5 GW, about 4.5 GW, about 4.5 GW): https://www.tnb.com.my/assets/quarterly_results/
- Tenaga Investor Deck, Oct 2026, p.6, re-opened 30 Oct 2026 (base capex RM26.55bn: energy transition 12.10, security of supply 10.96, demand growth 3.49 "e.g. data centres and industries"; contingent RM16.27bn, pre-approved by the Energy Commission, "Activated upon trigger events", examples include "new demand from data centres with signed ESAs"; same 7.3% return): https://www.tnb.com.my/assets/conference_materials/TNB_Investor_Deck_Oct_2026.pdf
- Tenaga Connection Charge Book 2025, section 3 and Table 7: https://www.tnb.com.my/assets/files/TNB_Connection_Charges_Book_2025_ENG.pdf
- Tenaga connected load charge terms: https://www.tnb.com.my/commercial-industrial/charges-penalties
- Energy Commission tariff schedule, 1 Jul 2025 to 31 Dec 2027: https://myenergystats.st.gov.my/documents/d/guest/jadual-tarif-tnb-terkini
- Dewan Negara Hansard, 8 Dec 2025 (UHV class for data centres): https://www.parlimen.gov.my/files/hindex/pdf/DN-08122025.pdf
- Dewan Rakyat Hansard, 13 Oct 2026, pp.31 to 33 (62 data centres, 8.771 GW signed; 45 operating, 6 GW; 1.37 GW used; overbooking; Energy Commission study): https://www.parlimen.gov.my/files/hindex/pdf/DR-13102026.pdf
- Dewan Rakyat Hansard, 15 Oct 2026, pp.5 to 6 (user-pays study; fifth period 2028 to 2032): https://www.parlimen.gov.my/files/hindex/pdf/DR-15102026.pdf
- Dewan Rakyat Hansard, 24 Jun 2026, pp.1 to 3, and ministry written answer (PAAB four plants about 388 MLD, some to tender 2028; 12 MLD reclaimed water): https://www.parlimen.gov.my/files/hindex/pdf/DR-24062026.pdf ; https://www.petra.gov.my/uploads/content-downloads/file_20260630123353.pdf
- SPAN Water and Sewerage Fact Book 2025, pp.45 to 46: https://www.span.gov.my/document/upload/sPF1aUUdC4IYfngEe3JdJdQbqDjRTX7Y.pdf
- Ministry written answer, 12 Nov 2019 (SPAN target 10 to 15%): https://www.nres.gov.my/Parlimen/MQT/MQT-DATO%27%20SRI%20DR.%20SANTHARA%20(12%20November%202019).pdf
- DayOne Form F-1, 5 Oct 2026: https://www.sec.gov/Archives/edgar/data/2118192/000119312526414188/d223752df1.htm
- BIS guidance, 31 May 2026: https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf
- MITI press statement, 14 Jul 2025: https://www.miti.gov.my/miti/resources/Media%20Release/[FINAL]%5FMITI%5FPress%5FStmt%5FMalaysia%5FRegulates%5FTrade%5Fof%5FUS%5FAI%5FChips%5F2025-07-14.pdf
- EDB and IMDA, DC-CFA2 launch, 1 Dec 2025: https://www.edb.gov.sg/content/dam/edb-en/about-edb/media-releases/news/launch-of-second-data-centre-call-for-application/Launch%20of%20second%20data%20centre-call%20for%20application.pdf
- EDB and IMDA, DC-CFA2 award, 21 Aug 2026: https://www.edb.gov.sg/content/dam/edb-en/about-edb/media-releases/news/four-data-centre-proposals-selected-as-part-of-second-data-centre/Fact%20Sheet%20-Four%20data%20centre%20proposals%20selected%20as%20part%20of%20second%20data%20centre.pdf
- EMA, 5 Sep 2024: https://ema.gov.sg/news-events/news/media-releases/2024/singapore-indonesia-make-substantive-progress-on-electricity-imports
- EMA, 30 May 2025: https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2025/20250530-Media-Release-Singapore-Grants-Conditional-Licence-to-Singa-Renewables.pdf.coredownload.pdf
- EMA, 7 Aug 2026: https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2026/20260807-Media-Release-Conditional-Approval-for-900MW-of-Electricity-Trade-Between-Peninsular%20Malaysia-SG.pdf.coredownload.pdf
- EMA, 26 Oct 2026 (Sembcorp 1.3 GW): https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2026/20262610-EMA-Media-Release-EMA-Grants-Conditional-Approval-to-Sembcorp-Utilities.pdf.coredownload.pdf
- EMA, 26 Oct 2026 (five-year plan: 95% gas, 8.6 GW peak, 9.9 to 13 GW by 2031, five gas plants, about 26% from about 12 GW, landing sites, 1 GW link, second link up to 2 GW): https://www.ema.gov.sg/content/dam/corporate/news/media-releases/2026/20262610-EMA-Media-Release-Five-Year-Energy-Infra-Plan-to-Meet-Unprecedented-Future-Demand.pdf.coredownload.pdf
- Digital Infrastructure Bill, Bill No. 20 of 2026: https://www.parliament.gov.sg/api/media/27325093-8be6-4ca2-bc3e-5e7a5f70b2f1/Digital-Infrastructure-Bill-20-2026.pdf
- MDDI, 8 Sep 2026 (more than 1.6 GW; 3 and 10 MW): https://www.mddi.gov.sg/newsroom/new-digital-infrastructure-bill-to-strengthen-the-foundations-for-singapore-s-digital-economy/
- MDDI, Second Reading speeches, 6 and 7 Oct 2026: https://www.mddi.gov.sg/newsroom/opening-speech-by-sms-tan-kiat-how-for-the-second-reading-of-the-digital-infrastructure-bill/ ; https://www.mddi.gov.sg/newsroom/closing-speech-by-sms-tan-kiat-how-for-the-second-reading-of-the-digital-infrastructure-bill/
- MDDI reply to PQ, 3 Mar 2026 ("within the envelope of our resource constraints"): https://www.mddi.gov.sg/newsroom/mddi-s-response-to-pq-on-limits-on-singapore-s-total-data-centre-capacity/
- Hitachi Investor Day, 10 Jun 2026, and results to June 2026; Siemens Energy Capital Market Day, 20 Nov 2025: as sourced in the live pieces hitachi-energy-plans-the-queue and siemens-energy-measures-the-shortage.
- SemiAnalysis, free text only: https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power (30 Dec 2025); https://newsletter.semianalysis.com/p/the-chinese-ai-infrastructure-boom (25 Sep 2026); https://newsletter.semianalysis.com/p/how-oracle-is-winning-the-ai-compute-market (30 Jun 2025)

## Figures dropped or flagged

- 3,885 MVA vs 1,272 MW and 72.76%: NOT used anywhere in the piece, per instruction (press only; internally inconsistent; covers all JS-SEZ load). The "Watch" lists of the three live claims still contain "72.76 per cent"; the piece quotes only claim and breaksIf, so it does not appear. Tommy is deciding separately.
- 3.8 GW Johor maximum demand and "one and a half times the state's use": Wood Mackenzie, not primary. Dropped from the body; numbers.ts entry flagged above.
- "Generation is sufficient, access to the wires decides" (Wood Mackenzie, in two live pieces): not primary, dropped.
- Singapore's 2019 to 2022 moratorium ("froze approvals for about three years" in two-governments): press only (DCD, ITPro). Dropped.
- DC-CFA pilot PUE 1.3 (2022): press only, dropped.
- Johor's air-cooling rule for Tier 3 and 4 data centres and the Tier 1 and 2 halt: press only (Malay Mail, Bernama, The Star), dropped.
- Johor water: 2,352 MLD design capacity, 2,700 MLD demand by 2030, the two state plants at 210 MLD: press only, dropped. SPAN's 2,375 MLD used instead. The 1,337 MLD federal projects are in the Hansard but whether they are raw or treated water is disputed in press; the piece no longer uses the figure.
- 14.4% Johor margin (Hansard 24 Jun 2026): matches SPAN's Peninsular figure, not SPAN's Johor 14.3%; SPAN's used.
- "SPAN recommends at least 15%": press wording; SPAN's primary target is a 10 to 15% band. Band used.
- A raised connected load charge for data centres: press only; Tenaga's book shows one rate for all. Not used.
- 33 Green Lane projects by March 2026: DROPPED. Press only (Bernama via Borneo Post and a Tenaga-hosted clip, quoting a TNB social post); no TNB primary found. The claims.ts watch item "The Green Lane project count beyond 33" is not quoted in the piece.
- SPAN figures 2,375 MLD design capacity and 2,034 MLD: DROPPED. 2,034 is SPAN's system input volume (which SPAN calls demand; raw intake is 2,052), and the pair gives 14.4%, not SPAN's stated 14.3%. The piece keeps only SPAN's stated margins and its 10 to 15% band.
- Federal 1,337 MLD and PAAB 388 MLD: dropped in the trim (water section cut to three sentences plus table).
- Exposure map trimmed to about 130 words: Schneider Electric, Eaton, Sembcorp and Ranhill SAJ no longer appear in this piece's map; their company pages lose this link at merge.
- Parliament's 7 Oct vote on the Digital Infrastructure Bill: press only; the piece says only that the closing speech refers to "the approved Act".
- Princeton Digital Group's Sedenak campus connected in 12 months: press only, not used.
- Battery makers named in the live queue piece's exposure map (one of them on the never-name list) are left out of the deep piece's map; their company pages lose that link at merge.

## Could not verify today

- I re-opened Tenaga's 2QFY2026 briefing, its 2023 Green Lane release and its October 2026 investor deck p.6. The "in system" labels for June 2025 (24 projects, 3.5 GW) and March 2026 are the fact-checker's reading of 2QFY2025 p.4 and 1QFY2026; I did not re-open those two. The 2QFY2025, 4QFY2025 and 1QFY2026 denominators, the investor-deck capex split, the tariff and connection-charge terms, the Hansard pages, SPAN, DayOne, BIS, MITI, EMA, EDB/IMDA and MDDI figures rest on the cluster sidecars' verification (29 to 30 Oct 2026).
- Hitachi Energy and Siemens Energy figures are as cited in their live pieces, not re-opened.
- The September 2025 load point (710 MW) has no denominator in my notes, so it is left out of the table.

## Fact-check fixes applied (30 Oct 2026)

1. Fill table: June 2025, March 2026, June 2026 labelled "in system" (June 2025: 24 projects); only December 2025 is "in operation", flagged as not strictly comparable.
2. Green Lane: concession added to the-part-money-cannot-hurry ("Where I was wrong"); the "steel and copper" line replaced; table and top layer now say the whole implementation period was cut; 33 projects dropped.
3. DayOne: "pay for capacity, while power is charged on customers' actual consumption as a pass-through"; hall "earning its capacity fees".
4. Water: 2,375 and 2,034 dropped; SPAN's stated margins and band kept.
5. RM16.27bn described as contingent, "activated upon trigger events", not spent; base split checked and used in the two-governments section and note; the duplicated RP4 sentence removed.
6. DC-CFA2: "provisionally allocated" in both layers.
7. "The grid is sold out": dated to March 2024, repeated December 2025; "What I add" made modest, with SemiAnalysis's "China's Johor" acknowledged.
8. Sources line: MDDI PQ reply (3 March 2026), the ministry answer (12 November 2019) and EMA 5 September 2024 added; the 29 May 2026 clip dropped with the figure it carried.
9. New claim: Malaysia-wide ratio, no causal "so", redevelopment uplifts and pre-30 October 2026 allocations excluded; queue note reworded to the national ratio.
10. Trims: duplicated RP4 capex, CLC paragraph, "power-gated by geography" paragraph cut; water three sentences plus table; cable section about 100 words; analogy about 70 words; map about 130 words with the exact disclaimer pair.
11. Abilene edit listed above, not made.
