# Sidecar: johor-waits-on-the-treatment-plant

Draft of 29 Oct 2026, Watch Later batch, revised after fact-check the same day. Publishes 23 Nov 2026, after water-is-a-siting-problem (13 Nov), so the link to it stays. Piece: `src/content/journal/johor-waits-on-the-treatment-plant.md` (draft: true). Cover: `public/covers/johor-waits-on-the-treatment-plant.svg`. Checker 0 failures, 0 warnings; build clean; body just under 600 words, 15 figures.

## The claim

**Proposed:** Johor's water limit for data centres is how fast Ranhill SAJ and the federal agencies can build treatment plants, not raw water, so Johor's reserve margin as stated by SPAN or the federal water ministry stays under SPAN's 15% minimum at the end of 2027 and the state keeps rationing data centre water.

**Honest risk (fact-check, 29 Oct):** the same 24 Jun 2026 Dewan Rakyat answer lists federal JBA projects adding 1,337 MLD, phased to 2027, which RTM and Bernama describe as dams, off-river storage, barrages and raw-water conveyance (The Star calls it treated water; I follow RTM/Bernama), plus four PAAB-financed treatment plants (The Star: RM1.17bn, 388 MLD; 388 not in RTM/Bernama, and no completion dates given). With Johor's two state plants (210 MLD), six treatment plants are under way. If they all run by end-2027 the margin clears 15% and the claim fails. The piece now says so plainly. The claim is still worth making: Johor's margin averaged about 10% in 2018 to 2022 (JP Morgan, press), was 11.5% in 2022 (SPAN Fact Book via MIDA) and about 10% in March 2025 (state), so the bet is that plant delivery keeps lagging the raw-water works and demand, which is exactly the mechanism. Overlap between the PAAB four and the two state plants is unknown.

How the outline changed after research:
- The video's "about 11%" margin is old. The latest official figure is about 14.4%, given by the Deputy Prime Minister in the Dewan Rakyat on 24 June 2026 (SPAN's 2022 Fact Book had 11.5%; the state said "about 10%" in March 2025). So the test is now close to the line, and it is a genuine risk: the two plants under construction (Semanggar package 50 MLD, due 2026; Layang 2 Phase 2 160 MLD, due 2027) could lift the margin above 15% if demand grows slowly. That is what makes it falsifiable. If Tommy wants a safer test, raise the bar to 20% (alternative B below).
- Data centres are a small slice of Johor's water today (broker estimates about 18 MLD actual against 45 MLD requested, press only, not used in the piece). The piece therefore does not say data centres are draining Johor. It says the buffer is thin because plants lag, and the state rations data centre water to protect it.

Consistency with `water-is-a-siting-problem` (publishing 13 Nov): this piece says the plant queue decides how Johor's campuses are cooled and which districts can host them, not whether they come, and links to that piece. The link only works once that piece is live; publish this one after 13 Nov or drop the link.

**Alternatives considered:**
- A. "Johor sells raw water to Singapore and buys treated water back, so its constraint is processing, not supply." Vivid but an Explainer, no dated test. Used as the cold open instead.
- B. Same mechanism, test set at 20%: "Johor's reserve margin is still under 20% at end-2027." Safer, but further from SPAN's own line, which is the natural benchmark. Chose 15% because it is the regulator's threshold.

## claims.ts entry

```ts
  {
    id: 'johor-waits-on-the-treatment-plant',
    claim: 'Johor\'s water limit for data centres is how fast its treatment plants can be built, not raw water, so the state keeps rationing data centre water while its reserve margin stays under SPAN\'s 15% minimum.',
    breaksIf: 'SPAN or the federal water ministry states Johor\'s reserve margin at 15% or more for the end of 2027, or Johor drops its air-cooling rule for data centres before then because treated water has caught up, or Johor\'s next major water cuts are officially attributed to drought or raw water shortage.',
    watch: ['Johor\'s reserve margin as reported by SPAN, the state or the federal government (about 14.4% in June 2026)', 'Johor\'s two state plants (210 MLD, due 2026 and 2027) and four PAAB-financed plants in service', 'Federal raw-water works (1,337 MLD, phased to 2027) against treatment capacity actually added', 'Johor\'s data centre approval rules and recycled water volumes (about 12 MLD in June 2026)'],
  },
```

## stack.ts layer

`cooling` (beside `water-is-a-siting-problem`). The mechanism is the clean-water supply behind cooling towers and the push to air and recycled-water cooling. No new layer proposed; if Tommy later wants a "Water supply" layer, it would sit between `grid` and `onsite`, but one piece does not justify it.

## Glossary (heading "Inside the building")

- Water treatment plant: Works that settle, filter and disinfect river or reservoir water so it can be piped to taps and cooling towers. Building one takes years.
- Reserve margin (water): Spare treatment capacity above what customers draw on an average day. Malaysia's regulator SPAN recommends at least 15%.
- Megalitre: A million litres. Malaysian water capacity is quoted in megalitres a day (MLD).
- Reclaimed water: Sewage treated to a high standard and reused, for example in data centre cooling, instead of drinking water.

## numbers.ts (physical)

```ts
  { layer: 'cooling', value: '~14.4%', what: 'Johor\'s treated-water reserve margin, the spare plant capacity above average demand, against SPAN\'s recommended 15% minimum.', piece: 'johor-waits-on-the-treatment-plant', asOf: 'June 2026' },
```

## LinkedIn post (§9)

Johor sells raw water to Singapore and buys clean water back.

That tells you its water problem is not the river. It is treatment plants, which take years to build, and Johor's spare capacity sits just under the regulator's 15% minimum. So the state now approves new data centres only if they cool with air, and steers them to recycled water.

The piece covers how clean water gets made, what Johor's own figures show, and what would prove me wrong.

https://thephysicallayer.fyi/journal/johor-waits-on-the-treatment-plant/

#DataCentres #Johor #Water

## Figures in the body and their sources

| Figure | Source | Status |
|---|---|---|
| Singapore may draw up to 250 mgd from the Johor River (stated as "roughly 1,100 megalitres") | MFA Singapore, Water Agreements page | Primary for 250 mgd. The litre conversion is my assumption of imperial gallons (250 x 4.546 = 1,137 ML); no primary source states imperial, hence "roughly". |
| "In 2017 Singapore said it regularly supplied Johor" about 16 mgd treated ("roughly 70 megalitres") | MFA, Minister for Foreign Affairs' written reply to Parliament, 9 Jan 2017 (not on the Water Agreements page) | Primary, dated 2017, so the piece puts it in the past tense. Same imperial-gallon assumption (16 x 4.546 = 72.7 ML). |
| SPAN recommends a minimum 15% reserve margin | Bernama Garasi, 20 Mar 2026, citing SPAN (SPAN presentation at mgtc.gov.my could not be opened) | Press citing regulator |
| Demand 2,700 MLD by 2030; design capacity 2,352 MLD (48 plants); 2025 average production 2,037 MLD (not used) | Johor state assembly answer by exco Mohamad Fazli Mohamad Salleh, 19 Nov 2025, via Bernama, The Star, FMT | Press report of an official assembly answer |
| Reserve margin about 14.4% ("Malaysia's water minister") | Fadillah Yusof, Dewan Rakyat, 24 Jun 2026, via The Star and NST | Press report of a parliamentary answer. Definition caution: the 19 Nov 2025 state figures imply 15.5% (design capacity over average production) or 13.4% (over capacity), and a TNB news clip uses 14.4% for Peninsular Malaysia as a whole. The falsifier therefore names the measure: Johor's margin as stated by SPAN or the federal water ministry. |
| Two state plants being built, 210 MLD total by 2027 | State assembly, 19 Nov 2025 (FMT: 50 + 160); Johor MB, 7 Mar 2026 ("two water treatment plants with a combined capacity of 210 MLD"); RHB gives 60 + 150. Totals agree, so the piece gives the total only | Press report of official statements |
| Federal projects due by 2027 add 1,337 MLD, mostly dams, barrages and raw-water pipes; four PAAB-financed plants under way | Fadillah Yusof (Deputy PM and Minister of Energy Transition and Water Transformation), Dewan Rakyat, 24 Jun 2026, via RTM, Bernama and The Star | Press report of a parliamentary answer. The Star calls the 1,337 treated water; RTM and Bernama list raw-water works. |
| Johor stopped approving the lowest grades (Tier 1 and 2) in 2025; in March 2026 the MB "reiterated" that Tier 3 and 4 are approved only with air cooling, none with high water demand | Malay Mail and Bernama, 10 Mar 2026; The Star, 23 Jul 2026 (Tier 1 and 2 halt "late last year") | Press report; rule predates March; no gazetted rule found |
| About 12 MLD reclaimed water to data centre cooling in Johor | Fadillah Yusof, Dewan Rakyat, 24 Jun 2026, via NST | Press report of a parliamentary answer |

No company financial figures are used. **Every Johor figure is press-only.** SPAN's and Parliament's sites failed TLS for the fact-checker, and I found no Ranhill SAJ filing giving the margin. Tommy should open the Dewan Rakyat Hansard for 24 Jun 2026 himself (14.4%, 1,337 MLD, PAAB plants, 12 MLD) and, if possible, SPAN's latest Fact Book before publish.

Source URLs (accessed 29 Oct 2026):
- https://www.mfa.gov.sg/about-mfa/key-issues/water-agreements/ (250 mgd)
- https://www.mfa.gov.sg/newsroom/press-statements-transcripts-and-photos/mfa-press-release-minister-for-foreign-affairs-dr-vivian-balakrishnans-written-reply-to-parliamentar-09-jan-2017/ (9 Jan 2017, 16 mgd)
- https://berita.rtm.gov.my/nasional/senarai-berita-nasional/senarai-artikel/rm1-6-bilion-perkukuh-bekalan-air-johor-tambah-kapasiti-1337-juta-liter-sehari/ (24 Jun 2026, 1,337 MLD raw-water works)
- https://www.bernama.com/lite/news.php?id=2572269 (24 Jun 2026)
- https://garasi.bernama.com/stories/water-bankruptcy-is-coming-are-we-prepared (20 Mar 2026)
- https://www.bernama.com/en/news.php?id=2492657 (19 Nov 2025)
- https://www.freemalaysiatoday.com/category/nation/2025/11/19/johor-spending-rm184mil-on-2-new-water-treatment-plants (19 Nov 2025)
- https://www.thestar.com.my/metro/metro-news/2025/12/01/more-treated-water-needed (1 Dec 2025)
- https://www.thestar.com.my/news/nation/2026/06/24/johor-has-enough-water-reserves-to-meet-current-demand-says-fadillah (24 Jun 2026)
- https://www.nst.com.my/news/regional/2026/06/1471404/data-centre-boom-drives-johor-water-security-upgrade (Jun 2026)
- https://www.thestar.com.my/news/nation/2026/03/07/johor-to-implement-38-projects-worth-rm153bil-to-boost-water-security (7 Mar 2026)
- https://www.malaymail.com/news/malaysia/2026/03/10/johor-mb-onn-hafiz-no-approval-for-data-centres-with-high-water-demand-welfare-comes-first/212089 (10 Mar 2026)
- https://bernama.com/en/news.php?id=2532596 (10 Mar 2026)
- https://www.thestar.com.my/news/nation/2026/07/23/johor-data-centre-turn-to-recycled-water (23 Jul 2026, background)
- https://www.mida.gov.my/mida-news/investments-in-water-need-to-keep-pace-with-influx-of-data-centres/ (2024, SPAN 2022 Fact Book 11.5%, background)
- https://www.thestar.com.my/news/nation/2026/02/08/johor-reviews-groundwater-potential-for-data-centres (8 Feb 2026, background)
- https://www.thestar.com.my/news/nation/2025/11/02/water-supply-restored-to-over-244000-accounts-after-sg-johor-contamination (2 Nov 2025, background)
- https://theedgemalaysia.com/node/787702 (BIMB note on 18 vs 45 MLD; date on page unclear; not used)
- Lead: CNA Insider, "Who Will Be Prioritised?": The Dilemma Of Malaysia's AI Push, https://www.youtube.com/watch?v=H39gck73WCQ

## Video figures dropped or flagged

- 20 million litres a day used by Johor data centres: not verified at a primary source. A BIMB broker note (press) gives about 18 MLD actual against 45 MLD requested. Dropped.
- US$1.1bn plan adding 41%: this is the RM5bn March 2025 plan (three reservoirs, federally funded; three plants, state-funded via Ranhill SAJ) adding 890 MLD, 2,171 to 3,061 MLD, per press. The 41% checks out against press; the US$ figure is the video's conversion. Dropped (money figure, and superseded by the 38-project RM15.3bn plan of March 2026).
- 1,000 MLD needed by 2030: attributed to Ranhill SAJ only via a BIMB note (press). The state assembly figure is demand of 2,700 MLD by 2030 against 2,352 MLD design capacity. Used the state figure; dropped 1,000.
- 2,000 MLD reclaimed water nationally: not found anywhere. Press reports IWK produces about 7,371 MLD of treated effluent nationally (1,067 MLD in Johor). Dropped.
- "Semangar": spelling in official reports is Semanggar (Bernama, FMT); The Star sometimes writes Semangar. Plant not named in the piece.
- November 2025 cut "affecting about 800,000 people": the Sungai Johor pollution of 31 Oct 2025 (sand-mining pond breach, Kota Tinggi) cut supply to 455,499 accounts, about 1.8 million residents per press. The 800,000 figure does not match. Dropped; also it was raw water pollution, not plant capacity.
- 2026 groundwater review: confirmed (exco Fazli, Feb 2026, via Bernama/The Star); no outcome published. Not used.
- 65 Johor projects as of June 2026 (20 operating, 8 building, 37 in approval): not found in any official source. Dropped. The "timing, not sufficiency" interview quote is unattributed in the transcript; not used.
- "About 11% reserve margin": superseded by the official 14.4% (June 2026). Flagged above.
- BAKAJ is named in the piece as the state regulator; no BAKAJ figures used.

## Primary-source re-check, 29 Oct 2026 (verdict: HOLD)

Parliament's and SPAN's sites opened this time. Found:

- SPAN Water and Sewerage Fact Book 2025, p.45 to 46 (https://www.span.gov.my/document/upload/sPF1aUUdC4IYfngEe3JdJdQbqDjRTX7Y.pdf): Johor reserve margin 14.3% (2021), 11.5% (2022), 16.8% (2023), 15.7% (2024), 14.3% (2025). Johor design capacity 2,375 MLD in 2024 and 2025 (2,336 in 2023); system input volume 2,034 MLD in 2025. Peninsular Malaysia and Labuan margin 14.4% in 2025. Margin = (design capacity less SIV) / design capacity (2,375 and 2,034 give 14.4%). Primary.
- Dewan Rakyat Hansard, 24 Jun 2026, question 1 (https://www.parlimen.gov.my/files/hindex/pdf/DR-24062026.pdf, pp.1 to 3) and the ministry's written answer (https://www.petra.gov.my/uploads/content-downloads/file_20260630123353.pdf): raw water intake 2,052 MLD per SPAN; four PAAB-financed treatment plants; 12 MLD reclaimed water (IWK and JSW) for data centre cooling. In the supplementary: JBA projects RM1,628.52m for 1,337 MLD, to 2027; PAAB four projects about 388 MLD, RM1,169m loan, at various stages, some expected to go to tender in 2028; "reserved margin 14.4 peratus" for Johor. Primary. The 14.4% matches SPAN's Peninsular figure, not SPAN's Johor 14.3%; use SPAN's.
- Ministry written answer, 12 Nov 2019 (https://www.nres.gov.my/Parlimen/MQT/MQT-DATO%27%20SRI%20DR.%20SANTHARA%20(12%20November%202019).pdf): SPAN's reserve margin target is 10% to 15%. Primary. No primary source found for "SPAN recommends at least 15%"; that wording is press (Bernama Garasi) and an RHB note.
- Still press-only: 2,352 MLD and 2,700 MLD by 2030 (state assembly, 19 Nov 2025; no DUN Hansard online); the two state plants, 210 MLD (no Ranhill filing or Bursa announcement found); the Tier 1 and 2 halt and air-cooling rule (no gazetted guideline found).

Why HOLD:
1. The benchmark is not primary as worded. SPAN's own target is a 10% to 15% band, so Johor at 14.3% sits inside SPAN's target, not under its minimum.
2. SPAN's series shows Johor above 15% in 2023 and 2024. The margin moves in steps when plants open and erodes between them; "stays under 15%" is not structural.
3. On SPAN's numbers the test leans against the claim. If Semanggar (50 MLD, 2026) and Layang 2 Phase 2 (160 MLD, 2027) open on time, capacity is about 2,585 MLD; with SIV growing at its 2021 to 2025 pace (about 35 to 60 MLD a year) to roughly 2,150 MLD, the margin is about 17% at end-2027. The claim then holds only if a plant slips. (The PAAB tenders in 2028 support "plants lag", but do not save the 2027 test.)

Possible reframe for Tommy: a sawtooth claim built on SPAN's series (margin jumps when a plant opens, then demand eats it back within two years), tested on whether Johor's 2027 or 2028 Fact Book margin is back under 15% after Layang 2 Phase 2 opens. That would rest on SPAN primary data, but it is a new claim and needs his sign-off.
