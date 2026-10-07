# Eaton draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/eaton-order-book-outruns-it.md` (draft: true)
Cover: `public/covers/eaton-order-book-outruns-it.svg`
Drafted 7 October 2026. Claim needs Tommy's approval before publish.

## Proposed claim

Eaton is shipping more electrical gear than ever, yet its Electrical Americas backlog keeps growing faster than its sales, so the queue for the equipment inside a data centre's fence, measured in months of sales on order, will keep lengthening until its new plants arrive in 2027.

### Alternatives considered

1. Eaton's grid-to-chip portfolio (Fibrebond, Resilient solid-state transformers, Boyd liquid cooling, $3.4m content per MW by management's account) makes it the supplier that captures the 800 VDC shift. Rejected: content per megawatt is the Vertiv piece's argument, 800 VDC is the-rack-runs-out-of-copper, and the content figure is an analyst-prompted management estimate, not a filing.
2. Eaton's year-long, fixed-price order book turns any rise in metal costs into a margin squeeze until prices catch up (EA margin 29.5% to 27.5%, 470 bps from commodity inflation). Rejected as the lead: it is a financial consequence, not the physical mechanism. Kept as one section and as a falsifier test.

Chosen because it is new to the site (the electrical room inside the fence, not the transformer or the turbine, as a lengthening queue), it is tested directly on Eaton's own segment backlog and sales, and its falsifier is a ratio with a named denominator that stays valid as Eaton grows.

## claims.ts entry

```ts
  {
    id: 'eaton-order-book-outruns-it',
    claim: 'Eaton is shipping more electrical gear than ever, yet its Electrical Americas backlog keeps growing faster than its sales, so the queue for the equipment inside a data centre\'s fence, measured in months of sales on order, will keep lengthening until its new plants arrive in 2027.',
    breaksIf: 'Electrical Americas backlog divided by the segment\'s sales over the previous four quarters (1.05 at June 2026, up from 1.04 in March) falls for two consecutive quarters before mid 2027, when the new plants start; or falls below 0.93, its June 2025 level, before the end of 2027; or the segment\'s twelve-month book-to-bill falls below 1.0 for two quarters running; or Electrical Americas margin is still falling year on year after Eaton reports price and cost back to neutral.',
    watch: ['Electrical Americas backlog divided by trailing four quarters of segment sales, each quarter, and whether it keeps rising', 'Electrical Americas twelve-month book-to-bill', 'Electrical Americas operating margin, year on year', 'Whether the Nebraska switchgear and South Carolina transformer plants start production on time in 2027, and whether Eaton says its extended lead times are shrinking'],
  },
```

## stack.ts

Layer `distribution` ("Power inside the building"). Suggested position after `every-megawatt-got-harder`:
`pieces: ['the-rack-runs-out-of-copper', 'every-megawatt-got-harder', 'eaton-order-book-outruns-it', 'ti-feeds-the-chip']`

## Glossary

Heading "Inside the building":
- `Prefabricated power module`: An electrical room built and wired in a factory, with its switchgear and backup power inside, then shipped to site and connected. It trades scarce site electricians for factory time.
- `Inside the fence`: Equipment on the data centre site itself, between the grid connection and the racks, as opposed to the substation and grid on the utility's side.

Heading "Getting power to the building" (finance-as-evidence terms sit there):
- `Deferred revenue`: Payments and billings a company has received ahead of delivering the product. Unlike pure customer deposits, it also includes amounts billed in advance. Used on this site only as evidence of how buyers hold their place in a queue.
- `Basis point`: A hundredth of a percentage point. A margin falling 200 basis points has fallen two percentage points.

Existing entries already cover switchgear, UPS, busway, backlog, book-to-bill, CDU, cold plate, lead time.

## numbers.ts (physical figure, time-based)

```ts
  { layer: 'distribution', value: '~13 months', what: 'Orders Eaton\'s North American electrical business has signed but not yet shipped, measured against its sales over the previous four quarters. Up from about 11 months a year earlier, despite a factory ramp. A proxy for the queue, not a lead time.', piece: 'eaton-order-book-outruns-it', asOf: '30 June 2026' },
```

Note: this is a dollar ratio turned into time, my arithmetic. If Tommy prefers numbers.ts to hold only purely physical figures, skip it.

## LinkedIn post (§9)

```
Eaton shipped 18% more electrical gear in the year to June, and its order book grew 33%.

Eaton makes the switchgear, backup power and wiring that sit between the grid and the racks in a data centre. It is spending more than $1 billion on two dozen capacity projects, yet the orders waiting in its North American business have grown from about eleven months of sales to about thirteen. The big new plants that could close the gap arrive in 2027.

The piece covers what Eaton makes, how its queue is measured in months, and what that queue does to its margin.

https://thephysicallayer.fyi/journal/eaton-order-book-outruns-it/

#DataCentres #Electrification #EnergyInfrastructure
```

## Fact-check changes (7 October 2026)

The backlog-to-sales ratio is presented as the measure of the queue (months of sales on order), explicitly a proxy, not a lead time: it also rises if customers book earlier for later delivery, and Ruiz said most of the US data centre pipeline delivers in 2028 and beyond. Title changed to "Eaton is shipping more electrical gear than ever, and its order book is growing faster still"; slug kept. Falsifier now fires if the ratio falls two quarters running before mid 2027. Margin test is year on year, noting the 190 bps sequential recovery in Q2. Jonesville customers include data centres. "Revenue per day" as Ruiz said it. Segment sales described as equipment and services.

## Arithmetic (my own, from Eaton filings, $m)

Electrical Americas quarterly sales: Q3 2024 2,963; Q4 2024 2,906 (11,436 FY24 less 8,530 9M24); Q1 2025 3,010; Q2 2025 3,350; Q3 2025 3,410; Q4 2025 3,506 (13,276 FY25 less 9,770 9M25); Q1 2026 3,600; Q2 2026 3,951.
EA backlog: Dec 2024 10,141; Jun 2025 11,377; Sep 2025 12,009; Dec 2025 13,246; Mar 2026 14,459; Jun 2026 15,175.
Backlog / trailing four quarter sales: Dec 2024 0.89; Jun 2025 0.93 (11,377 / 12,229); Sep 2025 0.95; Dec 2025 1.00; Mar 2026 1.04; Jun 2026 1.05 (15,175 / 14,467). Trailing sales growth Jun 2025 to Jun 2026: 18.3%.
Caveats: Fibrebond (acquired 1 April 2025) is in both June figures but only one quarter of the June 2025 trailing sales; the rise slowed in Q2 2026 (1.04 to 1.05); price increases reach backlog before sales, and Eaton does not split backlog into price and volume.
Deferred revenue $1,159m vs total firm backlog ~$24.1bn at 30 June 2026 (group-wide, includes Aerospace).

## Sources (every figure)

- Eaton 2Q 2026 earnings release (8-K Ex. 99), 31 July 2026: https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000027/etn06302026exhibit99.htm
  - EA sales $3,951m, +18% organic; operating margin 27.5%, up 190 bps sequentially; EA 12-month orders +41% organic; backlog +33%; Boyd closed and contributing; FY2025 revenue $27.4bn; founded 1911; Dublin.
- Eaton Form 10-Q, quarter ended 30 June 2026, filed 31 July 2026: https://www.sec.gov/Archives/edgar/data/1551182/000155118226000030/etn-20260630.htm
  - EA backlog $15,175m vs $11,377m; organic orders +41%; book-to-bill 1.3 (1.1 a year earlier); margin 29.5% to 27.5%, "470 basis point decline from higher commodity inflation, partially offset by a 260 basis point increase from higher sales"; deferred revenue $1,159m; total backlog ~$24.1bn, ~71% due within twelve months; capex ~$1.15bn expected in 2026; Fibrebond (1 April 2025, $1.43bn, "pre-integrated modular power enclosures"); Boyd Thermal (12 March 2026, $9.55bn); Resilient Power (6 August 2025, solid-state transformer technology).
- Eaton Form 10-Q, quarter ended 31 March 2026, filed 5 May 2026: https://www.sec.gov/Archives/edgar/data/1551182/000155118226000013/etn-20260331.htm
  - EA sales $3,600m; backlog $14,459m; margin 30.0% to 25.6% (480 bps commodity inflation, 100 bps growth-initiative costs, +210 bps sales).
- Eaton Form 10-Q, quarter ended 30 September 2025, filed 4 November 2025: https://www.sec.gov/Archives/edgar/data/1551182/000155118225000036/etn-20250930.htm
  - EA Q3 2025 sales $3,410m, 9M $9,770m; backlog $12,009m.
- Eaton Form 10-Q, quarter ended 30 September 2024, filed 31 October 2024: https://www.sec.gov/Archives/edgar/data/1551182/000155118224000041/etn-20240930.htm
  - EA Q3 2024 sales $2,963m, 9M $8,530m.
- Eaton Form 10-K for 2025, filed 26 February 2026: https://www.sec.gov/Archives/edgar/data/1551182/000155118226000007/etn-20251231.htm
  - EA sales FY2025 $13,276m, FY2024 $11,436m; EA backlog $13,246m (Dec 2025), $10,141m (Dec 2024); capex $919m in 2025.
- Eaton 2Q 2026 earnings call, 31 July 2026. Transcript used: Motley Fool via The Globe and Mail: https://www.theglobeandmail.com/investing/markets/stocks/ETN/pressreleases/3731391/eaton-etn-q2-2026-earnings-call-transcript/
  - Ruiz: "Scaling capacity to turn demand into revenue remains the clear priority in the business"; more than $1bn and two dozen projects across EA; "roughly 25% growth in revenue per day since the start of 2025"; disruption "happened in Q4 and Q1"; 307 GW US data centre backlog, "15 years of backlog at 2025 build rates"; "one of the bottlenecks in the industry, which is to have availability of electricians, plumbers"; Fibrebond packages "our UPSs, our switchgear"; "we know the product lines where our lead times are extended". Foster: data centres "up about 65%" in EA; "the majority of the margin decline was driven by temporary negative price/cost"; return to "roughly neutral impact in the second half"; Q3 "on regular time versus overtime", "more experienced operators".
- Eaton South Carolina transformer plant, announced 12 February 2025 (Business Wire): https://www.businesswire.com/news/home/20250212663224/en/ ; detail confirmed via Manufacturing Dive, 18 February 2025: https://www.manufacturingdive.com/news/eaton-transformer-production-shortage-investment/740135 ($340m, Jonesville, three-phase transformers, production and hiring 2027).
- Eaton Nebraska switchgear plant, announced 8 April 2026 (Business Wire): https://www.businesswire.com/news/home/20260408952863/en/ ; detail confirmed via EW, https://www.ewweb.com/news/bulletin-board/article/55369576/eaton-to-invest-more-than-30-million-in-nebraska-factory-to-produce-switchgear ($30m+, Bellevue, 370,000 sq ft, AIS and GIS, production first half 2027).
- Eaton Arkansas enclosure plant, announced 2 September 2026 (Business Wire): https://secure.businesswire.com/news/home/20260902691655/en/ ; detail confirmed via Talk Business, https://talkbusiness.net/2026/09/eaton-to-locate-242-million-facility-in-north-little-rock-adding-1200-jobs/ ($242m, North Little Rock, double US capacity for Fibrebond enclosures).

## Could not verify / left out

- The call transcript is a third-party (Motley Fool, partly LLM-produced) transcript; Eaton's site would not load to check its own. Quotes should be checked against the webcast replay before publish. The transcript renders the CEO as "Paulo Sternadt"; the press release names him Paulo Ruiz, which the piece uses.
- The three plant announcements are Eaton's own Business Wire releases, but Business Wire blocked direct fetching; figures were confirmed through trade press quoting them. The Arkansas start date (one outlet said fully operational by 2028) was not confirmed, so the piece gives none.
- Data centre share of Eaton's sales is not in the filings, so it is left out. The "orders up 85%" and "$3.4m content per megawatt" figures circulate in coverage but are not in the filings; left out.
- Eaton does not name the commodity behind the 470 bps; the piece does not say copper.
- The backlog-to-sales ratio is my arithmetic, labelled as such through the test wording; Eaton does not publish it.
