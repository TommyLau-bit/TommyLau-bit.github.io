# Crusoe draft: sidecar for Tommy and the publish step

Piece: `src/content/journal/crusoe-borrows-the-jet-engine.md` (draft: true)
Cover: `public/covers/crusoe-borrows-the-jet-engine.svg`
Drafted 29 October 2026 from the uncapped re-scout, Tier A item A9 (batch 3). Claim wording needs Tommy's approval before publish.

## Quality bar verdict: PASS

1. New mechanism: the site has said aeroderivatives are "quicker to ship" (ge-vernova-sells-the-wait, one clause) and that on-site power has its own queue (the-way-out-has-its-own-queue). Neither says WHY the small machine is faster. This piece does: its engine is made by a different company (GE Aerospace, the aircraft engine maker) on a different line from the heavy-duty slots in Greenville, so the two queues are separate, and the fast one is now filling. Howmet (castings, heavy-duty step to 30 GW) and Homer City (air permit netting) are different mechanisms; Homer City's FT8 units appear only in the exposure map here.
2. Primary sources: every figure is from GE Vernova or GE Aerospace SEC filings, GE Vernova's own call transcript PDF, or GE Vernova's own release and case study. No press-only figure in the body.
3. Beyond the headline: the 24 month shipping gap and six versus 18 month commissioning (CEO, 22 July 2026), aeroderivative orders at about three times shipments in 2026 (127 against 39, nine months), and GE Aerospace's sales of engines and parts to GE Vernova in nine months of 2026 already above all of 2025. None of that is in the Crusoe headline.

## Proposed claim

Crusoe's aeroderivative turbines arrive years before heavy-duty machines because their engines come from GE Aerospace's aircraft engine lines, not from GE Vernova's heavy-duty slots in Greenville; that fast lane is now forming its own queue, so GE Vernova's aeroderivative orders will keep running ahead of its aeroderivative shipments through 2027.

### Alternatives considered

1. "Aeroderivatives are the only gas route under two years" (the outline). Rejected: not provable from primary sources (reciprocating engines and fuel cells are also fast, and Bloom is already covered), and GE Vernova itself frames the gap as 24 months of shipping plus a shorter commissioning, not a two year cut-off.
2. "Crusoe's 29 units were running by the end of 2025." Rejected: only GE Vernova's case study says they were "expected to be in full operation" in Q4 2025. No Crusoe or GE Vernova statement confirming operation was found, and the Abilene draft says Crusoe's Abilene turbines are backup to a grid connection. The piece reports the expectation as GE Vernova's.

Chosen because it names the physical reason for the speed (a separate engine supply chain) and gives a test GE Vernova reports every quarter (aeroderivative orders and sales in units).

## claims.ts entry

```ts
  {
    id: 'crusoe-borrows-the-jet-engine',
    claim: 'Crusoe\'s aeroderivative turbines arrive years before heavy-duty machines because their engines come from GE Aerospace\'s aircraft engine lines, not GE Vernova\'s heavy-duty slots, and that fast lane is now forming its own queue, so GE Vernova\'s aeroderivative orders will keep running ahead of its aeroderivative shipments through 2027.',
    breaksIf: 'GE Vernova says aeroderivative deliveries have slid into the same years as its heavy-duty slots, or over any four consecutive quarters before the end of 2027 GE Vernova ships more aeroderivative units than it orders.',
    watch: ['GE Vernova aeroderivative orders and sales in units, each 10-Q', 'GE Vernova statements on the gap between aeroderivative and heavy-duty shipment dates', 'GE Aerospace sales of engines and parts to GE Vernova, each 10-Q', 'Crusoe confirmation that its 29 LM2500XPRESS units are running'],
  },
```

## stack.ts

Layer `onsite` ("Power on site"). Suggested position: after `ge-vernova-sells-the-wait` (and after `howmet-casts-the-queue` if that publishes first). No new layer.

## Glossary

`Aeroderivative` already exists ("A smaller gas turbine adapted from a jet engine..."). No new terms needed. Optional, heading "Getting power to the building": `Commissioning`: the testing and tuning after a machine is installed, before it is allowed to run for real.

## numbers.ts (physical figures only)

```ts
  { layer: 'onsite', value: '24 months', what: 'How far ahead an aeroderivative can ship compared with a heavy-duty gas turbine, then about six months to commission against about 18 for the heavy-duty unit (GE Vernova CEO).', piece: 'crusoe-borrows-the-jet-engine', asOf: '22 July 2026' },
```

## LinkedIn post (§9)

Crusoe got its gas turbines years before a big power station machine because the engines come from an aircraft engine maker.

GE Vernova's small aeroderivative turbines are built around engines from GE Aerospace, not on the heavy-duty lines booked to 2030 and beyond. Its chief executive says they can ship 24 months sooner and commission in about six months. But that fast lane now has its own queue: 127 ordered against 39 shipped in the first nine months of this year.

I cover how the fast lane works, what GE Vernova and GE Aerospace report, and what would prove me wrong.

https://thephysicallayer.fyi/journal/crusoe-borrows-the-jet-engine/

#GasTurbines #AIInfrastructure #DataCentres

## Figures in the body, with sources

- Ten units ordered December 2024, nineteen more in June 2025 ("six months later"), 29 in all, nearly 1 GW: GE Vernova release, 22 July 2025 (financial editors' note: 19 units booked in Q2 2025). Primary.
- First ten for the campus outside Abilene: GE Vernova article "Going big to support data center growth" (Crusoe ordered 10 LM2500XPRESS "to be installed at the data center" outside Abilene). Primary (company). Sites of the other 19 not named anywhere.
- "Expected in full operation by the end of 2025": GE Vernova Crusoe case study ("expected to be in full operation" Q4 2025). Primary, but an expectation; NOT confirmed as achieved. Re-check before publish.
- Heavy-duty ordered today ships 2030 or later: GE Vernova 2Q 2026 call, 22 July 2026, Strazik ("largely sold out of '30 and more than half of '31"; heavy-duty "shipped in '30, '31"). Primary.
- About 95 per cent factory assembled; about 35 MW per unit; generator, gas compressor, emissions control: GE Vernova release, 22 July 2025. Primary.
- Heavy-duty shipped from Greenville: same 22 July 2026 call ("after it's actually shipped from Greenville"). South Carolina is general knowledge of GE Vernova's gas turbine plant.
- GE Aerospace spun GE Vernova off on 2 April 2024: GE Vernova 2025 10-K. Primary.
- GE Aerospace reports aeroderivative engines alongside military ones: GE Aerospace 10-Q for Q3 2026, filed 20 Oct 2026 ("our Aeroderivative business, previously reported in CES, has moved to our DPT segment"; Defense & Systems engine units "Includes Defense and Aeroderivative units"). Primary. GE Aerospace 2025 10-K: CES "manufactures ... jet engines for commercial airframes, as well as business aviation and aeroderivative applications"; LM2500 listed among defence platforms. GE Vernova Form 10 (2024): aeroderivatives "leverage GE Aerospace airplane engine technology".
- Engines and parts sourced from GE Aerospace and Aero Alliance (50-50 JV with Baker Hughes, "fulfillment of aeroderivative engines, spare parts, repairs, and maintenance services"): GE Vernova 2025 10-K, Note 11; Q3 2026 10-Q. Primary.
- 24 months shipping gap, about six months commissioning against another 18 on site, "the bridge": GE Vernova 2Q 2026 call transcript, 22 July 2026, Strazik in Q&A (verified against GE Vernova's own PDF). Primary.
- 127 aeroderivative orders and 39 shipped (units), nine months to 30 Sep 2026: GE Vernova 10-Q, Q3 2026, filed 28 Oct 2026 (Power, orders and sales in units). Primary. Context not in body: Q3 alone 57 against 13; full 2025 63 against 27 (2025 10-K).
- $407 million of engines and parts sold to GE Vernova in nine months 2026, above $350 million for all of 2025: GE Aerospace Q3 2026 10-Q and 2025 10-K ("direct and indirect sales ... to GE Vernova, primarily related to engine sales and parts"). Primary. Note: this includes all engine and parts sales to GE Vernova, mostly but not provably only aeroderivative.

Company financial figures in body: 127, 39, $407m (three, at the cap). One money figure only.

## Every source, with URL and date

- GE Vernova and Crusoe release, 22 July 2025: https://www.gevernova.com/news/press-releases/ge-vernova-crusoe-announce-major-29-unit-aeroderivative-gas-turbine-deliver-ai-data-centers (Crusoe copy: https://crusoe.ai/newsroom/ge-vernova-and-crusoe-announce-major-29-unit-gas-turbine-deal/)
- GE Vernova Crusoe case study (undated page, accessed 29 Oct 2026): https://www.gevernova.com/gas-power/resources/case-studies/crusoe-ai-data-centers-lm2500xpress
- GE Vernova article on Crusoe's first ten units (undated, 2025): https://www.gevernova.com/news/articles/going-big-support-data-center-growth-rising-renewables-crusoe-ordering-flexible-gas
- GE Vernova LM2500 product page (accessed 29 Oct 2026): https://www.gevernova.com/gas-power/products/gas-turbines/lm2500
- GE Vernova 2025 Form 10-K, filed 29 Jan 2026: https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/gev-20251231.htm
- GE Vernova Form 10-Q, Q2 2026, filed 22 Jul 2026: https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev-20260630.htm
- GE Vernova Form 10-Q, Q3 2026, filed 28 Oct 2026: https://www.sec.gov/Archives/edgar/data/1996810/000199681026000163/gev-20260930.htm
- GE Vernova 3Q 2026 release, 28 Oct 2026: https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm
- GE Vernova 2Q 2026 call transcript, 22 Jul 2026: https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf
- GE Vernova Form 10 information statement (amended), 5 Mar 2024: https://www.sec.gov/Archives/edgar/data/1996810/000119312524059354/d542465dex991.htm
- GE Aerospace 2025 Form 10-K, filed 29 Jan 2026: https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm
- GE Aerospace Form 10-Q, Q3 2026, filed 20 Oct 2026: https://www.sec.gov/Archives/edgar/data/40545/000004054526000064/ge-20260930.htm
- Exposure map only: ProEnergy release, 16 Apr 2026 (13 PE6000 aeroderivative sets, 50 MW each, for Crusoe): https://www.proenergyservices.com/2026/04/proenergy-to-deliver-major-generating-equipment-to-power-crusoe-ai-factories/ ; Mitsubishi FT8 units from Pennsylvania DEP plan approval 32-00457A (see homer-city-inherits-the-air sidecar).
- Checked, not used: TCEQ notice 182126 (Crusoe Energy Systems, Longhorn Data Center Buildings 9 and 10, 615 FM 2404 Abilene, filed 7 Nov 2025; does not name turbine models): https://www.tceq.texas.gov/downloads/permitting/air/bilingual/pending-permit-notices/182126-nori-spanish.pdf . A search summary pointed to TCEQ 182267 (five 34.1 MW GE LM2500 at "Abilene Data Center Campus Master Association"), but the notice now returns 404, so no state permit naming Crusoe's LM2500XPRESS units was read. Not used.
- Lead only: YouTube, "GE Vernova Explained: The Power Bottleneck Behind the AI Boom", transcript in research-build/source-watch-later/ge-vernova-power-bottleneck/TRANSCRIPT.md

## Video figures dropped or flagged

- "Crusoe ordered 29 of them, about one gigawatt in total": CONFIRMED (GE Vernova release, 22 Jul 2025). Kept.
- Aeroderivatives "designed for fast start backup and temporary bridge power ... tens of megawatts": consistent with GE Vernova (35 MW, five minute start, "the bridge"). Reworded, not quoted.
- Outline's "ship in months while heavy frames wait years" and "only gas route under two years": NOT verified as stated. Replaced with GE Vernova's own 24 month shipping gap and six versus 18 month commissioning.
- Outline's "tied to aviation engine parts": supported by GE Aerospace and GE Vernova filings (engine sales to GE Vernova, Aero Alliance). The piece does not claim aeroderivative engines share specific production lines or castings with airline engines, which no filing states.
- Outline's "state air permits naming the units": none could be read (see above). Dropped.
- Video's other figures (heavy-duty above 600 MW per plant, Doosan for xAI, life extension work): not used.

## Refresh before publish

- Look for any Crusoe or GE Vernova statement that the 29 units are running; if none, keep "expected".
- Re-read the Q3 2026 call transcript when GE Vernova posts it (gev_webcast_transcript_10282026.pdf returned 404 on 29 Oct) for any update on aeroderivative lead times.

## Checks

- `python3 brand/check-piece.py src/content/journal/crusoe-borrows-the-jet-engine.md`: 0 failures, 0 warnings.
- Body about 504 words (excluding exposure map and sources).
