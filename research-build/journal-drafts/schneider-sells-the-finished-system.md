# Schneider Electric draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/schneider-sells-the-finished-system.md` (draft: true)
Cover: `public/covers/schneider-sells-the-finished-system.svg`
Drafted 7 October 2026. Claim needs Tommy's approval before publish.

## Proposed claim

Schneider Electric's AI data centre growth is arriving as finished systems, built and tested in its factories, rather than as loose parts, because skilled hours on the building site are now scarcer than the equipment, so Systems will keep taking a larger share of its revenue.

### Alternatives considered

1. The PTC deal (about $22.6bn equity, agreed 5 October 2026) shows Schneider thinks the constraint is design and engineering data, not factory output. Rejected as the lead: PTC mainly serves discrete manufacturing (cars, aircraft, machines), which is outside the site's scope; it does not close until Q3 2027; and nothing in Schneider's disclosures could test it for years. Kept as supporting evidence in one section, with the deal value stated as fact only.
2. Motivair makes Schneider a liquid cooling contender against Vertiv. Rejected: Schneider stopped reporting Motivair separately once it became organic in Q2 2026, so it cannot be tested on disclosures, and cooling is already covered by cooling-is-half-the-job, room-to-spare and every-megawatt-got-harder.

Chosen because it is new to the site (the constraint is site labour and commissioning, and the evidence is the shift in what Schneider sells, not a queue), it rests on a disclosure only Schneider publishes (revenue by business model: Products, Systems, Software and Services), and it can be proved wrong by one reported ratio with a named denominator. It does not use backlog, backlog-to-revenue or demand-versus-capacity, which the GE Vernova, Eaton, Hitachi Energy and Siemens Energy drafts use.

## claims.ts entry

```ts
  {
    id: 'schneider-sells-the-finished-system',
    claim: 'Schneider Electric\'s AI data centre growth is arriving as finished systems, built and tested in its factories, rather than as loose parts, because skilled hours on site are now scarcer than equipment, so Systems will keep taking a larger share of its revenue.',
    breaksIf: 'Systems falls below 34 per cent of Schneider\'s group revenue, its 2025 level, for the full year 2026 or 2027 while Schneider describes Data Centre and Networks sales as growing double digit; or Products outgrows Systems on an organic basis for two quarters running while data centres remain Schneider\'s main growth driver.',
    watch: ['Systems as a share of group revenue, each year', 'Systems against Products organic growth, each quarter', 'Whether Schneider keeps naming prefabricated solutions as a data centre growth driver', 'Whether Schneider\'s executives stop describing site labour as a constraint'],
  },
```

Note on the test: the full-year share is used because quarterly shares vary (Q1 2026 was 33%). The share test checks the outcome; the labour mechanism is checked by the watch item on executives citing site labour. Schneider gives no data centre sales figure, only qualitative descriptions of Data Center & Networks, which also includes Distributed IT.

## stack.ts

Layer `distribution` ("Power inside the building"). Suggested position after `every-megawatt-got-harder` (and after `eaton-order-book-outruns-it` if that publishes first):
`pieces: ['the-rack-runs-out-of-copper', 'every-megawatt-got-harder', 'schneider-sells-the-finished-system', 'ti-feeds-the-chip']`

## Glossary

Heading "Inside the building":
- `Prefabricated module`: A power or cooling room built, wired and tested in a factory, then shipped to the data centre site in one piece and connected. It trades scarce site labour for factory time. (The Eaton sidecar proposes "Prefabricated power module"; add one entry, not both.)
- `Commissioning`: Testing equipment under power on site before it is allowed to carry the real load. Every panel, UPS and cooling loop in a data centre has to pass it.
- `Three-phase UPS`: A large uninterruptible power supply on three-phase power, the kind that carries a whole data hall through a grid dip, as opposed to a small unit under a desk.
- `Digital twin`: A working computer simulation of a building or system, used to design and test it before it exists and to run it afterwards.

Heading "Getting power to the building" (finance-as-evidence terms sit there):
- `Supply capacity agreement`: A multi-year deal in which a data centre operator commits to buy a supplier's equipment in phases, so both sides can plan output. Used on this site only as evidence of how buyers secure equipment.
- `Revenue mix`: How a company's sales split between kinds of offer, such as catalogue products against engineered systems. A shifting mix shows what customers are actually buying.

Existing entries already cover UPS, CDU, switchgear, gross margin, organic growth, hyperscaler, colocation.

## numbers.ts

No new physical figure is essential. Optional, if Tommy accepts a labour figure as structural (it is capacity of a kind, not anything about shares):

```ts
  { layer: 'distribution', value: '821,000', what: 'Electrician jobs in the United States in 2025, the pool every data centre, home, factory and grid project draws on to install and commission equipment. Projected to grow 9 per cent by 2035.', piece: 'schneider-sells-the-finished-system', asOf: '2025' },
```

## LinkedIn post (§9)

```
Schneider Electric's fastest-growing business is not the breakers and switches it is best known for.

Its Systems business, which includes power rooms and cooling plants built and tested in a factory, grew 28% in the second quarter against 13% for its catalogue products. Schneider says data centres led that growth. I think the reason is on the building site: an AI hall cannot switch on until every panel is installed and tested, and the people who do that work are scarce.

The piece covers how Schneider splits what it sells, the shift in its own numbers, and why it is spending on design tools as well as factories.

https://thephysicallayer.fyi/journal/schneider-sells-the-finished-system/

#DataCentres #Electrification #EnergyInfrastructure
```

## Arithmetic (my own, from Schneider releases, € million)

Q2 2026 revenue 11,459, up 16.5% organic, so the Q2 2025 base is about 10,008 (11,459 / 1.145 reported).
Q2 2025 shares (H1 2025 release): Products 48%, Systems 33%, Software and Services 19%.
Approximate organic growth contribution in Q2 2026: Systems 3,303 x 28% = about 925; Products 4,804 x 13% = about 624; Software and Services 1,902 x 6% = about 114. Total about 1,663, against 16.5% x 10,008 = about 1,651. Systems therefore supplied about 56% of organic growth from 33% of the base. Approximate, because the shares are rounded and the base uses reported rather than organic growth.
Systems share of revenue: FY2024 31%, Q2 2025 33%, Q3 2025 34% of Q3, FY2025 34%, Q1 2026 33% of Q1, Q2 2026 35% of Q2.
Systems against Products organic growth: Q2 2025 17 v 2; Q3 2025 19 v 3; Q4 2025 19 v 4; Q1 2026 16 v 9; Q2 2026 28 v 13. Software and Services in the same quarters: 11, 8, 10, 9, 6, so Systems was the fastest of the three every quarter.

## Sources (every figure)

- Schneider Electric Half Year 2026 Results, 30 July 2026 (AMF filing): https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2026/07/FCECO082813_20260730.pdf (also https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
  - Q2 revenue €11,459m, +16.5% organic; H1 €21,226m, +14.0% organic; Products 47% of Q2, +13%; Systems 35% of Q2, +28%, "the Data Center end -market continues to lead the growth, with prefabricated solutions, cooling technologies and 3 -phase UPS all seeing significant growth"; Software and Services 18%, +6%; mix -€148m "mainly due to the relatively faster growth of Systems revenues compared to Products and Software"; gross margin "Mix also adversely impacted the Gross margin, given the relative strength of Systems growth"; net capex €669m, €48m lower than H1 2025; gross pricing on products; Motivair organic from Q2 2026.
- Schneider Electric Full Year 2025 Results, 26 February 2026: https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf
  - Revenue €40,152m; Products 47%, Systems 34%, Software and Services 19% of FY25 revenue; Q4 Systems +19%, Products +4%, Software and Services +10%.
- Schneider Electric Full Year 2025 Results presentation, 26 February 2026: https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf
  - Data Center & Networks 30% end-market exposure, footnoted "% of FY 2025 Orders"; Buildings 29%, Industry 27%, Infrastructure 14%; ETAP and NVIDIA Omniverse "AI Factory digital twin".
- Schneider Electric Full Year 2024 Results, 20 February 2025 (via MarketScreener reproduction of the release): https://ae.marketscreener.com/quote/stock/SCHNEIDER-ELECTRIC-SE-4699/news/Schneider-Electric-Full-Year-2024-Results-Press-Release-49107937/
  - Products 50%, Systems 31%, Software and Services 19% of FY2024 revenue.
- Schneider Electric Half Year 2025 Results, 31 July 2025 (AMF filing): https://echanges.dila.gouv.fr/OPENDATA/AMF/ECO/2025/07/FCECO079331_20250731.pdf
  - Products 48% of Q2, +2%; Systems 33% of Q2, +17%; Software and Services 19%, +11%; net capex H1 2025 €717m.
- Schneider Electric Third Quarter 2025 Revenues, 30 October 2025: https://webdisclosure.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2025-jK0pNmvoQyw (figures via search extract of the release; fact-checker should confirm on the PDF)
  - Products 48% of Q3, +3%; Systems 34% of Q3, +19%; Software and Services 18%, +8%.
- Schneider Electric Q1 2026 Revenues, 30 April 2026: https://www.se.com/ww/en/assets/pdf/release-q1-revenues-2026
  - Products 48% of Q1, +9%; Systems 33%, +16%; Software and Services 19%, +9%.
- Schneider Electric Capital Markets Day transcript (LSEG StreetEvents), 11 December 2025: https://www.se.com/ww/en/assets/pdf/capital-markets-day-transcript
  - Frédéric Godemel, EVP Energy Management: "Take the example of data center, where today there is tension on the number of people to commission product and install them."
  - Aamir Paul, CEO North America: "specifically in the US market is we have a labor shortage" and "lots of conversations about land and power as being barriers in terms of scale-up, but actually labor is one".
  - David Howson, President EMEA, Vantage Data Centers: "designed to be deployed in a pre-configured, pre-commissioned to avoid the labor challenges that we've got".
  - Noelle Walsh, President of Cloud Operations and Innovation, Microsoft: "new ways to deliver capacity at a faster speed to market. Such as through innovations like skidding and modularization."
- Schneider Electric half year 2026 results call, 30 July 2026. Transcript used: Investing.com: https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-lifts-2026-outlook-after-strong-h1-93CH-4822615
  - Olivier Blum: the "Foxconn agreement for North America will help us to improve, increase our capacity to deliver prefab for the data center industry."
- Schneider Electric and Switch announcement, 19 November 2025: https://www.se.com/us/en/about-us/newsroom/news/press-releases/Schneider-Electric-and-Switch-Expand-Partnership-with-1-9-Billion-Supply-Capacity-Agreement-to-Power-AI-Factories-691d16cc3a880bee320a9cc6 (read via the identical copy at https://www.switch.com/schneider-electric-and-switch-expand-partnership-with-1-9-billion-supply-capacity-agreement-to-power-ai-factories/)
  - "two-phase supply capacity agreement" of $1.9bn; "prefabricated power modules and the first North American deployment of chillers"; "standardized, pretested layouts".
- Schneider Electric completion of the Motivair majority stake, 28 February 2025: https://www.optionfinance.fr/info-financiere-en-continu/d/2025-02-28-schneider-electric-finalise-sa-prise-de-participation-majoritaire-dans-motivair.html
  - 75% stake, Buffalo, New York; remaining 25% in 2028.
- Schneider Electric US investment announcement, 26 March 2025 (read via trade press): https://www.manufacturingdive.com/news/schneider-electric-700-million-investment-us-data-center-demand-ai/743630/
  - About $700m through 2027 across several US states. Piece no longer says eight sites.
- Schneider Electric and PTC announcement, 5 October 2026 (PTC Form 8-K Ex. 99.1): https://www.sec.gov/Archives/edgar/data/0000857005/000119312526413124/d174191dex991.htm
  - $205 per share in cash, PTC equity valued at about $22.6bn (€20.1bn); "bridging the physical and digital worlds across the lifecycle, from design and build to operate and maintain"; PTC "products and machines system of design"; closing expected by Q3 2027. Industries (automotive, aerospace) per Engineering.com: https://www.engineering.com/schneider-electric-to-acquire-ptc-in-22-6b-deal/
- US Bureau of Labor Statistics, Occupational Outlook Handbook, Electricians: https://www.bls.gov/ooh/construction-and-extraction/electricians.htm
  - 821,000 jobs in 2025; employment projected to grow 9% from 2025 to 2035.

## Fact-check fixes (7 October 2026)

Walsh now "at the same event" (recorded message). Gross margin sentence adds Schneider's "mitigated at the adjusted EBITA level". Falsifier reworded to Schneider's qualitative Data Centre and Networks description; full-year shares explained; outcome versus mechanism tests separated. Drives now "low voltage drives" under Products (medium voltage drives sit in Systems). PTC described as an all-cash deal worth about $22.6bn, no equity value wording. US plants: about $700m across several states, dated 26 March 2025. Sources line adds Q3 2025 revenues, the Foxconn announcement of 15 June 2026 and the US investment release; Foxconn remark attributed to the call via a third-party transcript. Added one sentence that prefabrication moves part of the wait into the factory, consistent with the Eaton draft.

## Could not verify / left out

- Aamir Paul's own figures at the Capital Markets Day (about 600,000 US electricians against 900,000 needed; 10,000 retiring and 7,000 joining a year) conflict with the BLS count of 821,000 jobs, so the piece uses BLS and quotes Paul only qualitatively.
- Schneider does not disclose data centre revenue as a share of sales; the 30% figure is share of 2025 orders, and the piece says so.
- Schneider does not split Systems between data centres and industrial automation, or report Motivair or prefabricated revenue separately. The piece flags the industrial automation caveat in the falsifier section.
- Q3 2025 business-model figures came from a search extract of the release, not the PDF itself; confirm before publish.
- The Foxconn quote comes from a third-party transcript (Investing.com); check against the webcast. The Foxconn partnership was announced 15 June 2026 per trade press; Schneider's own release was not read.
- The $700m US investment figure is from trade press reporting Schneider's March 2025 release; Schneider's page was not read directly.
- The deal value for PTC is stated as fact only; the premium and the share price were deliberately left out.
- Several se.com PDFs block direct download; they were read through the fetch tool's saved copies.
