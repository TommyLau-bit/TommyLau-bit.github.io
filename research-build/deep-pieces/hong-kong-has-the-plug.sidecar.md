# Sidecar: hong-kong-has-the-plug (new deep piece, "Two tracks for new work", track 1)

Approved by Tommy on 30 Oct 2026 as a new deep piece. Drafted 30 Oct 2026 to BRIEF-DEEP.md and the prototype `the-queue-not-the-chip`. Piece: `research-build/deep-pieces/hong-kong-has-the-plug.md` (draft: true), outside `src/content/journal/` so the loader does not read it. Nothing committed, published or scheduled. Only new files written, plus the condition checks appended to `gap-hong-kong.notes.md` as instructed.

## Condition checks (full record in gap-hong-kong.notes.md, "Condition checks before drafting")

- (a) Tenant: CONFIRMED. Range Intelligent Computing Technology Group Company Limited is the stated foreign name of the Shenzhen-listed 润泽智算科技集团股份有限公司 (300442) itself (interim report, 28 Aug 2026). Its filings: overseas strategy is the "IDC rack business" (tenants bring chips); Hong Kong plus Batam about 600 MW planned, no Hong Kong-only figure; Hong Kong delivery "within 2028"; Hong Kong construction in progress RMB 17.1m at 30 Jun 2026; top three customers 93.7% of 2025 revenue, unnamed; nothing on Hong Kong chips or customers.
- (b) Chips: the scout's "fills with mainland accelerators" is unsupported. The 15 Jan 2026 rule makes H200-class exports from the US to end users located in China (Hong Kong included, per 85 FR 83765) case by case; re-exports, in-country transfers and Chinese-headquartered end users outside China stay presumption of denial; above-threshold parts stay presumption of denial. So for H200-class parts a Chinese tenant faces a softer policy in a Hong Kong hall than in Johor. Nvidia (26 Aug 2026): Hopper data centre shipments to China under 1% of Data Center revenue; outlook assumes no China data centre compute revenue. What fills Hong Kong halls is not shown; the claim does not depend on it.

## Changes from the brief's working version, and why

- Title: "Hong Kong has the plug, and the chip needs a licence" (not "needs two licences"). The second licence, Beijing's NDRC approval, is press-only (FT via secondaries) and stays out of the body.
- Claim: the "CLP data centre sales grow under 20% in FY2027" limb is dropped. Range's own 2028 delivery date explains slow 2027 growth as well as chips do (brief lesson: do not hang the claim on a cause). Sales growth is a watch item; the piece says outright that slow filling would not break the claim.
- New mechanism the site lacks: the US licence follows the hall's address in Hong Kong, and for H200-class parts that makes Hong Kong the more permissive address for a Chinese-headquartered tenant than Johor.

## Fact-check fixes applied (30 Oct 2026, coordinator)

1. "A quarter of its capacity spare" corrected everywhere to "about a quarter more capacity than its highest demand" (9,258 MW against a 7,455 MW peak; about 19% idle at the peak); analogy matched.
2. Reserve margin source: CLP's annual Ten-year Summary, not only offering circulars; published 7,455 MW replaces the implied 7.5 GW.
3. Duty to supply worded as the sources do: "obliged to meet electricity demand at the lowest reasonable cost".
4. Nvidia's "China including Hong Kong" line cut (10-Q narrative unread).
5. Top-layer H200 sentence: comma added and "if the exporter meets the rule's conditions"; investor layer now has the exporter applying, not the tenant.
6. Johor and Singapore licence row: "as BIS enforces it (31 May 2026)".
7. Exposure map trimmed; long sentences split.
New claim on substations and Sandy Ridge's energisation replaces the margin claim; cover drawn.

## Shape and counts

- Slug `hong-kong-has-the-plug`; title 10 words, sentence case, names Hong Kong.
- Top layer: 521 words, 10 figures (checker regex), 0 money figures. Analogy 73 words.
- Investor layer: 2,154 words before the exposure map; map 123 words, three groups plus the against block, exact disclaimer pair plus the prototype's evidence sentence. Whole body 2,969 words.
- `brand/check-piece.py` on the draft path, after the fact-check fixes: 0 failures, one warning (average sentence 24 words, driven by tables and the verbatim claim; the prototype carries the same warning). One US spelling (a verbatim Nvidia quote) was paraphrased to pass.
- No anchors: the piece absorbs no earlier piece, so no old slugs and no redirects.

## New claims.ts entry (existing entries untouched; replaced after the coordinator's fact-check, 30 Oct 2026)

```ts
  {
    id: 'hong-kong-has-the-plug',
    claim: 'Hong Kong\'s grid is building to its data centres, not holding them back: CLP will have completed the 18 data centre substations in its 2024 to 2028 Development Plan by 31 December 2028, and Sandy Ridge\'s first phase will be energised by 31 December 2027.',
    breaksIf: 'CLP\'s interim or annual results show fewer than 18 data centre substations completed in its 2024 to 2028 Development Plan by 31 December 2028, or Sandy Ridge\'s first phase is not energised by 31 December 2027.',
    watch: ['Data centre substations completed in CLP\'s interim and annual results, every six months (eight by June 2026, one more targeted in the second half of 2026; 18 planned by 2028)', 'Sandy Ridge\'s first phase against CLP\'s mid-2027, Range\'s 2028 and the government\'s 2029', 'CLP\'s installed capacity and local maximum demand in the annual Ten-year Summary (9,258 MW against 7,455 MW in 2025; a margin below 15% is a warning, not a break)', 'CLP\'s quarterly sales to data centres (+12.8%, 6.6% of sales, nine months 2026)', 'Range Intelligent Computing\'s filings for Hong Kong capacity, customers and chips', 'BIS licensing of H200-class chips to end users located in China, and any change to 15 CFR 742.6 or to Hong Kong\'s treatment'],
    date: '2026-10-30',
    home: 'hong-kong-has-the-plug',
  },
```

`date` is a placeholder: set it to the real publish time at go-live.

Why it is a real test: CLP finished eight data centre substations in the two and a half years to June 2026, about three a year. With one more targeted by end-2026, about nine remain for 2027 and 2028, roughly four or five a year. The 18 is also an "up to" target, so missing demand would miss it. Sandy Ridge's end-2027 date sits between CLP's mid-2027 and the tenant's "within 2028", so it can fail either way. The old claim (reserve margin at 20% or more, no delay for want of power) was dropped as near-certain or weather-driven. The export licence stays in the body as mechanism, outside the falsifier.

Alternatives considered: (A) "Hong Kong's halls fill with mainland accelerators": not shown, and the rule points the other way for H200-class. (B) Data centre sales growth under 20% in FY2027: Range's 2028 delivery explains slow growth as well. (C) Reserve margin at 20% or more: near-certain, and a hot summer could break it with no bearing on data centres.

## stack.ts

Layer `grid` ("The grid connection"), beside `the-queue-not-the-chip`, which it contrasts with: `pieces: ['the-queue-not-the-chip', 'hong-kong-has-the-plug', 'america-rations-the-plug', 'the-equipment-queue']`. Alternative for Tommy: `operators`, if he reads the piece's point as "what fills the hall". I recommend `grid`, because the claim is about the plug.

## Glossary (src/pages/glossary.astro)

"Getting power to the building":
- Scheme of Control: Hong Kong's agreement between the government and each power company. It obliges the company to meet demand at the lowest reasonable cost and allows it a regulated return. CLP's runs to 31 December 2033.
- Reserve margin (power): installed capacity above the year's highest demand, as a share of that demand. CLP Power's was about 24% in 2025 (9,258 MW against 7,455 MW), so about 19% of capacity was idle at the peak.

"Chips, memory and the wiring between them":
- Presumption of denial: a US licence review policy under which an export application is expected to be refused unless shown otherwise.
- Case-by-case review: a US licence review policy under which each export application is judged on its merits. Since 15 January 2026 it applies to H200-class chips exported from the US to end users located in China, Hong Kong included.
- Petaflops (PFLOPS): a thousand million million calculations a second. Hong Kong's government counts computing power this way without stating the precision, so figures compare only with each other.
- Country Group D:5: the US list of arms-embargoed countries, China among them, used to set export licence policy. Hong Kong is treated as part of China.

Check for duplicates at merge: "Export licence (advanced chips)" may already exist from the Johor piece; if so, extend it with one sentence on Hong Kong rather than adding a new term.

## numbers.ts (physical only)

```ts
  { layer: 'grid', value: '~283 MW', what: 'Average power CLP Power sold to Hong Kong data centres in the first nine months of 2026 (6.6% of 28,131 GWh), on a system of 9,258 MW against a 2025 local peak of 7,455 MW. Derived from CLP figures.', piece: 'hong-kong-has-the-plug', asOf: 'September 2026' },
  { layer: 'grid', value: '8 of 18', what: 'Data centre substations CLP Power had completed by June 2026 in its 2024 to 2028 Development Plan, against 18 planned by 2028 and three in the 2018 to 2023 plan.', piece: 'hong-kong-has-the-plug', asOf: 'June 2026' },
  { layer: 'operators', value: '5,000 PFLOPS', what: 'Hong Kong\'s total computing power as counted by its government; Sandy Ridge promises 180,000 by 2032. Precision not stated.', piece: 'hong-kong-has-the-plug', asOf: 'January 2026' },
```

## LinkedIn post (§9; opens on the sharpest number)

```
Hong Kong's main utility has finished eight substations for data centres since 2024, three times its count from the previous plan, and plans 18 by 2028.

It is obliged to meet demand at the lowest reasonable cost, and had about a quarter more capacity than its 2025 peak. Its one AI megasite drew a single bid, from a group that plans to let racks, not run chips. The hard part is the chip: under US rules Hong Kong is China, so the hall's address decides the licence.

The piece covers CLP's substations and sales to data centres, the Sandy Ridge tender and its tenant, and the US licence rules by chip and route.

https://thephysicallayer.fyi/journal/hong-kong-has-the-plug/

#DataCentres #HongKong #ExportControls
```

## Cover proposal (not drawn)

`/covers/hong-kong-has-the-plug.svg`. A dark harbour at night with a single wall socket on the Kowloon side glowing amber, a thick amber cable running from it into an empty rack outline. Above the rack, a small grey paper tag on a string marked with a stamp outline, unstamped (the licence). Caption in letter-spaced grey: "HONG KONG: THE PLUG IS READY". Background as a plain `<rect width="800" height="600" fill="url(#bg)"/>` after `<defs>` for make-og.py.

DRAWN 30 Oct 2026 at the coordinator's request: `public/covers/hong-kong-has-the-plug.svg`, in the palette and type of `the-queue-not-the-chip.svg`. A lit amber socket (the plug) cabled into a rack of dashed empty slots with one blue chip square, a licence tag hanging above it with an unstamped seal, a harbour line below, caption "HONG KONG: THE PLUG IS BEING BUILT". make-og.py not run.

## Sources, every one with date (all opened by me on 30 Oct 2026 unless marked)

- CLP Ten-year Summary of Scheme of Control statistics, 2025 (installed capacity 9,258 MW; local system maximum demand 7,455 MW, 7,532 MW without demand response): https://www.clpgroup.com/content/dam/clp-group/channels/investor/document/3-1/eSOC10yearsSummaryenglish.pdf.coredownload.pdf
- CLP Power Hong Kong, US$4.5bn MTN offering circular, 1 Apr 2026 (Scheme of Control, 9,258 MW, about 24% reserve margin, 36,989 GWh, 6.4 million people, SoC to 31 Dec 2033): https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0401/2026040100797.pdf
- CLP Holdings quarterly statement Jan to Sep 2026, 12 Oct 2026 (+12.8%, 6.6%, 28,131 GWh, Sandy Ridge phases from mid-2027): https://www1.hkexnews.hk/listedco/listconews/sehk/2026/1012/2026101200581.pdf
- CLP Holdings interim results 2026, 6 Aug 2026 (+11.8%, 7.1%, 17,038 GWh, two substations 260 MVA, eight in plan period, one more in H2): https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0806/2026080600235.pdf
- CLP Holdings quarterly statement Q1 2026, 18 May 2026 (+11.1%, 7,319 GWh): https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0518/2026051800229.pdf
- CLP Holdings annual results 2025, 26 Feb 2026 (+7.5%, 35,760 GWh, three 132 kV substations in 2025, six since 2024, three in 2018 to 2023): https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0226/2026022600152.pdf
- CLP Holdings 2025 results presentation, 26 Feb 2026 (six energised 2024 to 2025, 12 more substations by 2028): https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0226/2026022600162.pdf
- CLP Holdings quarterly statement Jan to Sep 2025, 20 Oct 2025 (+6.7%, 27,456 GWh): https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1020/2025102000455.pdf
- CLP Holdings interim results 2025, 4 Aug 2025 (+6.7%, 16,453 GWh): https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0804/2025080400317.pdf
- HK Electric Investments results, 17 Mar 2026 and 11 Aug 2026 (no mention of data centres): https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0317/2026031700370.pdf ; https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0811/2026081100265.pdf
- ITIB press release, 2 Mar 2026 (award, one tender, HK$581m, 42 months, HK$23.8bn, 250,000 sq m, 180,000 PFLOPS by 2032, ultimate holding company): https://www.info.gov.hk/gia/general/202603/02/P2026030200249.htm
- SITI speech, 16 Jan 2026 (5,000 PFLOPS, Cyberport 3,000): https://www.info.gov.hk/gia/general/202601/16/P2026011600314.htm
- LegCo LCQ11, 22 Apr 2026 (operations in 2029; allocation by the operator): https://www.info.gov.hk/gia/general/202604/22/P2026042200281.htm
- LegCo LCQ11, 1 Apr 2026 (SCAs oblige supply, including I&T demand): https://www.info.gov.hk/gia/general/202604/01/P2026040100263.htm
- 2026 Policy Address, 16 Sep 2026, para 200: https://www.policyaddress.gov.hk/2026/public/pdf/policy/policy-full_en.pdf
- Range Intelligent Computing Technology Group (300442): 2025 annual report, 10 Apr 2026, http://static.cninfo.com.cn/finalpage/2026-04-10/1225090821.PDF ; 2026 interim report, 28 Aug 2026, http://static.cninfo.com.cn/finalpage/2026-08-28/1225521959.PDF ; Q3 2026 report, 23 Oct 2026, http://static.cninfo.com.cn/finalpage/2026-10-23/1225617368.PDF
- BIS, 85 FR 83765, 23 Dec 2020: https://www.govinfo.gov/content/pkg/FR-2020-12-23/html/2020-28101.htm
- BIS, 91 FR 1684, FR Doc 2026-00789, 15 Jan 2026: https://www.govinfo.gov/content/pkg/FR-2026-01-15/html/2026-00789.htm
- 15 CFR 742.6, eCFR (version of 28 Oct 2026 read 30 Oct 2026): https://www.ecfr.gov/current/title-15/part-742/section-742.6
- Nvidia CFO commentary and press release, Q2 FY2027, 26 Aug 2026: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm ; https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm
- SemiAnalysis credit (power-gated and chip-gated): dates 13 Mar 2024 and 30 Dec 2025 inherited from the Johor prototype's sidecar, NOT re-opened by me.

## Figures dropped or flagged

- Dropped (press only): Sandy Ridge about 220 MW (SCMP via Green Earth); CLP CEO's "three to four Sandy Ridges" (China Daily HK); Hong Kong 47 data centres and 581 MW (HKFP/Green Earth); groundbreaking 28 Mar and partial opening 1 Jul 2027 (Xinhua); ByteDance and DeepSeek as Range customers (hk01); Beijing wanting H200s in Hong Kong and ByteDance and Tencent H200 counts (FT via secondaries); 400,000 H200s approved (Reuters via secondaries).
- Not used: CLP's 8% excess capacity adjustment and permitted return rate (verified only in part; the excess capacity term in fact lowers the return on spare generation, so it does not support "paid to build" for generation; the piece says only "a regulated return").
- Derived and labelled as mine: about 283 MW average draw; about 19% of capacity idle at the 2025 peak. The implied 7.5 GW peak is replaced by CLP's published 7,455 MW. The headroom and 36 MW a year lines went with the old claim.
- The 2024 to 2028 Development Plan's about HK$38bn of T&D spending (scout 2.6) not re-checked; not used.

## Could not verify today

- Nvidia's 10-Q narrative (0001045810-26-000075): sec.gov served its undeclared-tool page to curl with the required User-Agent; WebFetch truncated before MD&A and risk factors. Full-text search confirms "H200" appears in it. Not bypassed.
- Any primary MW figure for Sandy Ridge alone.
- Who Range's customers are, in Hong Kong or anywhere.
- What chips any Hong Kong hall runs or will run, and whether any H200 licence names a Hong Kong end user.
- The July 2026 amendments to 15 CFR 742.6 (14, 16, 23 Jul) were not read in full; the H200-class paragraph quoted is unchanged in the current text.

## Edits other files may need (not made)

- `the-queue-not-the-chip` says "The licence follows the tenant's headquarters, not the hall's address." True for Johor; this piece adds that in Hong Kong it follows both. No change needed, but a one-line link from that piece's Johor section to this one would help readers at merge (Tommy's call; it would be an update-track edit).
