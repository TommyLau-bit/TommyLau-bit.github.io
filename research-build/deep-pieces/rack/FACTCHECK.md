# Fact-check: powering-the-rack-depth (7 Nov 2026)

Draft checked: src/content/journal/powering-the-rack-depth.md. Read in full against Nvidia WP1 (Oct 2025) and WP2 (2026) PDFs (text extracted and searched word for word), the Nvidia blogs of 20 May 2025 and 13 Oct 2025, the Google Cloud blog (30 Apr 2025), the Vertiv Q3 2026 8-K exhibit, the TI Q3 2026 8-K, the Infineon Q3 FY26 analyst-call statement (PDF), the Eaton Q3 2026 and Q1 2026 call transcripts, and catalogue and press checks listed below. `brand/check-piece.py` passes (0 failures, 0 warnings).

---

## ERRORS

**E1. "Two years apart" is wrong.**
Draft (line 113): "Its May 2025 post gave 85% more power and 45% less copper, a different basis; both are Nvidia's, two years apart."
Wrong: the posts are 20 May 2025 and the October 2025 white paper and blog, five months apart.
Replace: "Its May 2025 post gave 85% more power and 45% less copper, on a different basis; both are Nvidia's, five months apart."
Source: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/ (20 May 2025); WP1 Table 1 (Oct 2025).

**E2. Infineon quote is not word for word.**
Draft (line 244): 'Lead times were rising, "an early-upcycle pattern".'
Source says: "Lead times are rising ... a typical early-upcycle pattern as supply starts to tighten."
Replace: 'Lead times were rising, which it called "a typical early-upcycle pattern".'
Source: Infineon Q3 FY26 analyst-call intro statement, 5 Aug 2026, p.8, https://www.infineon.com/row/public/documents/corporate/investors/presentations/2026/2026-08-05-q3-fy26-intro-statement-analyst-call-v01-00-en.pdf

**E3. Sherman is not TI's first 300 mm fab.**
Draft (line 297): "Its first 300 millimetre fab at Sherman, Texas, began production on 17 December 2025."
Wrong: TI already ran 300 mm wafers at RFAB (Richardson) and LFAB (Lehi). SM1 is its first fab at Sherman.
Replace: "Its first fab at Sherman, Texas, a 300 millimetre plant called SM1, began production on 17 December 2025."

**E4. "Every maker dates the building step to late 2027 or later" is contradicted by two facts the piece itself reports.**
Draft (line 177): "Every maker that dates its building-scale product dates it to the end of 2027 or later." Chart title (line 169): "Every maker dates the building step to late 2027 or later".
Wrong: (a) on 3 Nov 2026 Eaton's CEO said "we have 10 pilots running parallel and multiple 15 kV projects that we are going to ship this year", which are medium voltage SSTs shipping in 2026; (b) Envision says its SST-fed 800 V system is already live. The chart also includes the Nvidia power rack (Q3 2026) and Vertiv sidecar (early 2027), which are not building steps, so its title does not describe its own rows.
Replace line 177: "Most makers date volume building-scale products to late 2027 or later. Eaton is the exception in timing: it says it will ship several 15 kV solid-state transformer projects this year, though 800 volt DC project shipments start in late 2027."
Replace line 175 sentence: "Eaton said on 3 November 2026 that its 15 kV, 2 MW unit had passed all its UL tests in October, with ten pilots running and "multiple 15 kV projects that we are going to ship this year"."
Replace chart title: "Most dated 800 volt products reach the building in late 2027 or later". Add Eaton SST "ship this year" as a row, or say in the caption that Eaton's 2026 pilot shipments are not drawn.
Source: Eaton Q3 2026 call, 3 Nov 2026, https://stockanalysis.com/stocks/etn/transcripts/721435-q3-2026/

**E5. UIG cannot be part of a May 2026 per-megawatt rise.**
Draft (lines 277 to 279): "...part of the rise is scope Vertiv has bought. It agreed in September 2026 to buy Utility Innovation Group..."
Wrong in sequence: the US$3.25m to 3.75m estimate is from 19 to 20 May 2026; UIG was agreed on 1 Sep 2026, after it. Only PurgeRite (closed 4 Dec 2025) predates it. And no Vertiv source I found attributes the per-MW rise to acquisitions; the deck attributes its TAM rise to "organic and inorganic actions".
Replace: "That is an estimate of opportunity, not reported revenue, and part of the rise may reflect scope Vertiv has bought, such as PurgeRite, which flushes and fills liquid cooling loops, closed in December 2025 for about US$1.0 billion upfront. Since the estimate, Vertiv has also agreed to buy Utility Innovation Group, which designs microgrids and on-site power, for about US$1.45 billion plus up to US$1.15 billion more; it closed in late October 2026." Apply the same fix to the every-megawatt-got-harder note ("part of it acquired scope" becomes "possibly part acquired scope").

**E6. "AC stays the default for the building" overstates WP2.**
Draft (line 16): 'Alternating current, the kind the grid delivers, stays "the default" for the building.' Line 142: "AC remains the default in its 2026 reference design for AI factories." Summary: "Nvidia's own plan keeps the building on alternating current by default".
WP2 says the AC option "remains the default and broadly adopted solution for today's AI Factory deployments" and that "the NVIDIA DSX reference design will be updated to incorporate 800 VDC architectures with multiple deployment options". The quoted "not intended to replace" sentence continues "but rather to complement and coexist alongside them as an additional deployment option".
Replace line 16 second sentence: 'Alternating current, the kind the grid delivers, "remains the default" for today's AI factories, and 800 volts comes as "an additional deployment option".'
Replace line 142 sentence: "Either way, AC remains the default for today's deployments in its DSX reference design, which Nvidia says will be updated to add 800 volt options."
Summary: "But Nvidia's own plan keeps AC as today's default, and the new voltage arrives first..."
Source: WP2 pp.2 to 8, https://dam-cdn.nvd.orangelogic.com/AssetLink/7rj0u54stc41tk6s57dbs2p0qdte5874.pdf

**E7. TI's 13% evidence line misattributes the source.**
Evidence fold (line 394): "about 13% of revenue, from analyst wording and summaries". The money-chart caption says "management's rounded share".
The CEO said it: "I think it was about 13% of revenue in Q3 or so." Fix the fold: "about 13% of revenue (CEO Haviv Ilan: 'about 13% of revenue in Q3 or so')". The body is then correct.
Source: TI Q3 2026 call, 21 Oct 2026 (transcript via Webull, https://www.webull.com/news/15789174635930624).

---

## ARITHMETIC

All checked; all correct within rounding except where noted.

- 1 MW at 54 V = 18,519 A; at 800 V = 1,250 A; at 12 V = 83,333 A; at 0.8 V = 1.25 million A. Three-phase per phase: 35 kV 16.5 A, 415 V 1,391 A. Correct.
- Copper bar 100 x 10 mm: 16.8 micro-ohm/m ("about 17 millionths", fine). 18,500 A: 5.75 kW/m (18,519 A: 5.76 kW/m), "about 5.8 kW", fine. Voltage drop 0.31 V, "a third of a volt": add "per metre" so it reads correctly. 1,250 A: 26.3 W/m. Correct. 14.8 squared = 219. Correct.
- 64 U x 44.45 mm = 2.84 m. Correct. (Note Nvidia MGX racks are 48 U, not 42; the point stands either way.)
- "Several hundred household circuits": 18,500 A / 32 A = 578; / 10 A = 1,850. Suggest "several hundred to nearly two thousand household circuits' worth".
- TI: 13% x US$6,055m = US$787m ("near US$790 million", correct); x4 = US$3.15bn. "About US$3.1 billion" is acceptable; "about US$3.1 to 3.2 billion" is exact. With 13% rounded (12.5 to 13.5%), the quarter is US$757m to 817m.
- TI gross margin 3,887 / 6,055 = 64.2%. Correct.
- Vertiv services and spares: 508.2 / 2,675.8 = 19.0%; 719.0 / 4,312.8 = 16.7%. Correct and confirmed in the 8-K sales-by-offering table. (The income-statement "services" line gives 17.2% to 15.7%; same direction.)
- "About sixteen typical racks": 120 / 7.5 = 16. Correct.
- Copper chart: bars are drawn as 0.6 kW/mm² x (1 + Nvidia's %): 0.70, 1.54, 2.89. But Nvidia's own Table 1 gives absolute values 0.8, 1.7 and 3.1 kW/mm²; its 0.6 is rounded down (the % column implies about 0.65 to 0.69). So the bars understate Nvidia's absolute values by about 10 to 13%. Fix: draw Nvidia's absolute values (0.6, 0.8, 1.7, 3.1) and keep the % labels, or drop the kW axis and draw on % alone. Title "about two and a half times" is fine (2.57x).
- Chart pixel positions for chart 1, timeline and money chart all match their stated values (checked).

---

## OVERSTATEMENTS AND FAIRNESS

**F1 (most serious). WP2 calls Option C near-term; the piece implies the building step is a 2029 story.** WP2 p.22: "Option C will continue to evolve and innovate beyond current deployment-ready 800 VDC solutions. While Options A, B, and C focus on near-term deployment readiness." "Toward 2029" applies to the next generation 34.5 kV SST, not to the transformer rectifier version of Option C. The piece says Nvidia "gives no date for the version built from conventional parts" (true) but never says Nvidia groups Option C with the near-term options. Add after line 140: "Nvidia does not date this version, but it groups all three options under 'near-term deployment readiness'; the 2029 date is for the next generation SST fed at 34.5 kV." This strengthens the TRU risk the piece already concedes and makes it fair.

**F2. The claim's first half is already strained by Envision.** The claim says "until 2028, 800 VDC enters data halls through power racks and row power centres fed from AC power rooms". Envision's live SST-fed bus is 800 V entering a hall another way; only the 10 MW falsifier protects the claim. Line 191 should say so plainly: "Strictly, Envision already shows 800 volts entering a hall without a power rack; what keeps the claim standing is size: the test needs 10 MW, and Envision gives none."

**F3. Eaton's 2026 SST shipments are omitted** (see E4). Also mention in "The readings come soon" (line 317): "Eaton says several 15 kV SST projects ship this year."

**F4. Vertiv "has moved its own date" omits Vertiv's later statement.** A Vertiv blog of 17 Jul 2026 (Martin Olsen) still speaks of PowerDirect 5000 commercialisation from the second half of 2026, with "deployments beginning in 2027". The May deck says "Commercial launch expected in early 2027". Replace line 271 first sentence with: "Vertiv, a maker of data centre power and cooling gear, has given later dates than it first did." Then after the deck sentence add: "A July blog still spoke of commercialisation from the second half of 2026, with deployments beginning in 2027." Same nuance in the every-megawatt note ("moved from the second half of 2026 to early 2027" becomes "slipped from a 2026 release to a commercial launch expected in early 2027, per its May deck").
Source: https://www.vertiv.com/en-us/insights/articles/blog-posts/from-rack-to-data-hall-the-practical-path-to-800-vdc/

**F5. "They disagree on direction" (line 281) overstates Schneider.** Schneider's CFO said the most complex AI sites would not "trend to the top of that range" over five years. That is about position in a range, not a fall. Replace: "The two estimates have different scopes and cannot be compared, and Schneider's does not suggest the most complex sites keep climbing." Also "because designs optimise cost" is not in the quote I could find; either cite the page or drop it.

**F6. TI claim note leans the wrong way on the first limb.** Note says "Nvidia's 2026 roadmap keeps 54 volts inside the rack to 570 kW, so the first limb cannot be tested before 2027." The limb is "Racks stay at 54 volts for years". Nvidia keeping 54 V inside the rack through Gen 3 is evidence toward that limb, not neutral. Replace: "Nvidia's 2026 roadmap keeps 54 volts inside the rack up to 570 kW, with 800 volts arriving next to the rack, so the first limb leans against the claim; it is settled only when Nvidia dates its fourth generation."

**F7. "The building waits on transformers that are still a first draft" (summary).** The SST spec is a first draft; transformer rectifier units are mature, as the piece itself says. Replace: "The building waits on a solid-state transformer whose specification is still a first draft, on breakers and codes still being written, and on rooms booked years ahead".

**F8. Inference not labelled.**
- Line 248: "That is AI power broadly, mostly silicon power stages and controllers, not 800 volt parts." Infineon did not break this out. Prefix "On my reading,".
- Line 297: "Industrial sales grew more than 40%, so the new lines are not running part-empty." Utilisation is not disclosed. Replace: "Industrial sales grew more than 40%, so on my reading the new lines are unlikely to be running part-empty."
- Line 61: "That is the 200 kilograms in Nvidia's sum." Replace: "That, on my reading, is what Nvidia's 200 kilograms measures."
- Line 14: "its power supplies would fill more rack space than the computers". Nvidia said shelves would take up to 64 U, "leaving no space for compute". Replace: "and its power supplies would leave no room in the rack for the computers."
- Line 45: "A third ... reaches 570 kW". WP2: "can support up to 570kW". Replace "reaches" with "can support up to".

**F9. Small press-vs-primary points.**
- Line 47: "A press report in July said it had slipped to 2028" – the report was SemiAnalysis's; Bloomberg rendered Nvidia's reply as "road map is intact". Replace: "A SemiAnalysis report in July, carried by the press, said it had slipped to 2028; Nvidia replied that its roadmap was intact." (drops a quote whose wording differs by outlet).
- Line 269: Lite-On "showcased" a power rack at GTC with no rating or date; "launched" fits Flex and Delta. Replace: "Delta and Flex each launched an 800 volt power rack at Nvidia's March 2026 conference, and Lite-On showed one."
- Line 32: Uptime's 2026 survey (released 28 Jul 2026) exists; one report gives an average of 7.8 kW excluding facilities built above 30 kW. Optional: keep 2025 and say so, or update to the newer primary release if its text gives the figure.
- Line 299 and money chart: onsemi's 175% and about US$180 million are in onsemi's own release (2 Nov 2026), so cite the release, not "as summarised".

**F10. Evidence fold, codes.** OCP LVDC white paper has a version 1.1.0 dated 2 Sep 2026. Check the NEC lines still read the same and cite the latest version.

---

## UNVERIFIABLE (could not confirm word for word; suggested softer wording)

- Envision exact phrase "directly from 10 kV medium voltage to an 800V DC bus" (PR Newswire blocked; pv magazine renders it "take power from 10 kV medium voltage to an 800 V DC bus"). "Now powering live computing workloads", August 2026 and 3 GW confirmed (pv magazine, 2 Nov 2026). If the PR Newswire page cannot be reopened, paraphrase: "converting 10 kV medium voltage straight to an 800 volt DC bus".
- OCP LVDC paper quotes ("will be completed in the third quarter of 2028", "must lean on interim guidance"): the OCP PDF was blocked to me; the research file cites p.145. Keep, but reconfirm on v1.1.0.
- SST spec rev 0.3.0 details (22 Jun 2026, "first draft", SKUs, "detailed design TBD"): not reopened. Note claims.ts watch item says "version 0.3 (July 2026)"; the PDF is dated 2 Jul. Not a conflict, but say "effective 22 June 2026, published in July".
- Schneider CMD quotes (Godemel "Up to 2027, we don't see at large new technology like"; Maxson range): transcript not reopened; the clipped quote ending on "like" is awkward; consider 'Schneider said it did not see the SST "at large" before 2027.'
- Vertiv CFO margin quote and executive chairman "not planning to share orders data going forward": call transcript not reopened. The 8-K text credits "operational leverage on higher sales and by manufacturing productivity"; if the call quote cannot be reconfirmed, use the release wording.
- Vertiv deck page 31 "~$3.25M - $3.75M per MW", up 10 to 15%: not reopened.
- Navitas first shipments of US-made parts on 3 Nov 2026, buffer capacity at TSMC "through 2029 and beyond": not found. Soften to "Navitas says it has begun shipping parts made at GlobalFoundries" only if the release says so; otherwise drop.
- Monolithic Power "has begun sampling GaN parts for 800 volt data centre designs": not found in what I read. Soften: "and says it is developing GaN parts for 800 volt designs" or cite the line.
- Power Integrations 1,250 and 1,700 V GaN "October 2025": dates not confirmed; 1,700 V GaN may predate October 2025. Soften: "Power Integrations now offers 1,250 and 1,700 volt GaN".
- Infineon and SolarEdge "2 to 5 MW SST block": the SST announced Nov 2025 is 13.8 to 34.5 kV in, 800 to 1,500 V out; the MW range not confirmed. Soften to "a megawatt-scale SST".
- TrendForce and Dell'Oro quotes, Delta chairman (Taipei Times), Villach €319m, Innoscience 183%, Renesas ¥235bn: press or not reopened; all are marked as such or plausibly primary. Low risk.
- Kaohsiung-1 and five cloud providers "designing for": confirmed via DCD's reading of Nvidia's 13 Oct 2025 post, not the Nvidia page itself.

Confirmed word for word or by figure: all WP1 and WP2 quotes in the piece (not intended to replace; near-term generations; 145/330/570; Q3 2026; Q3 2027; toward 2029; not sequential; retrofit deployment; remain highly practical; approximately 15kV-class; zero-crossings; converter-limited; primary branch; approximately 20 ms; preferred long-term; supply chain readiness; important enabler; system-level studies; UL 62368-1; certified now; 660 kW; 6x18.3 kW; four earthing schemes; 125 A and 1,250 A SSCBs; 2x, 4x or 8x; 20%; highest value real estate; transitional; optimal solution; faster and proven path; 17.5 MW five 3.5 MW 5,000 A; potential long-term target; three-pole; two-pole; 750 V VDE-SPEC 90037; 100 ms capacitors); Nvidia 20 May 2025 (200 kW; 64 U; 200 kg; 200,000 kg; 1 MW starting 2027; 85% and 45%); Nvidia 13 Oct 2025 (less than 90%; 157%; three wires; in phases; 64:1; 26%); Google 30 Apr 2025 (all three quotes); Eaton (65%, 101%, UL tests, 10 pilots, US$375m, US$600m; May "shipments starting in late 2027"); ABB SST H2 2027; Vertiv 8-K (55.0%, 63.6%, 18.1%, 25.2%, +2.9 pts, 19.0% to 16.7%); TI 8-K (US$6,055m, US$3,887m, capex US$463m vs US$1,197m) and call (95%, 13%, both quotes, no "800"); Infineon (allocation quote, high single-digit billion, €1.6bn, more than double, €500m, November upgrade, Siemens 1.2 kV SiC); Infineon September 2026 "natural current zero" quote; IEC 60947-10 ed. 1.0 May 2026; Mt Diablo 1.0.0 effective 8 Oct 2026, authors Microsoft, Meta, Google; Navitas 8-K TSMC July 2027 and 12-24 months; MPS US$506.7m, +164.6%; onsemi 175%, about US$180m, Ferric; Navitas US$14.0m; Uptime 7.5 kW (The Register, 3 Aug 2025); Kyber "roadmap intact".

---

## FORMAT AND STYLE

- Checker clean. No em or en dashes. No "center" or -ize spellings outside quotes ("specialized" is inside a WP1 quote).
- Unquoted American "toward": the options illustration aria-label ("puts the next generation solid-state transformer toward 2029") and the timeline aria-label ("Nvidia's next generation solid-state transformer, toward 2029"). Put the phrase in quotation marks or use "towards" outside quotes.
- Voltage inconsistency at the rack: line 78 says the GB200 shelves "make about 50 volts", elsewhere 54 V and the illustration says 54 V. Add: "about 50 volts (Nvidia's later racks run at 54)" or align.
- Line 59: add "per metre" after "a third of a volt".
- Borderline investor wording: "is paid twice in the meantime" and "three kinds of business gain first" are about businesses, not shares, and the exposure-map note covers it. Acceptable; no share prices, valuations or targets anywhere.
- Every term is explained at first use (checked: rack, kW, GPU, NVLink, volts/amps, MW, resistance, AC, transformer, medium voltage, UPS, busway, whips, power shelves, DC, busbar, IBC, regulators, U, GW, ±400 V, SST, TRU, arc, arc flash, MCCB, SSCB, AHJ, bandgap, SiC, GaN). "Hot-swap controllers" (line 293) is not explained; add "which let a board be plugged in live".
- `date:` is a placeholder (7 Nov 18:00) with `draft: true`; reset at the real publish time.
- No mention of AI help.

---

**Verdict:** Not ready to publish: fix E1 to E7 and F1 to F2 (the building-step dates and Nvidia's own "near-term" framing of Option C), then it is a sound, well-sourced piece whose arithmetic holds.
