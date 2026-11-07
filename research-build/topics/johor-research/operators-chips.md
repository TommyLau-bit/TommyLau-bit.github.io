# Johor: what fills the halls, how much is running, and the chip rules

Research slice for the depth rebuild of the Johor and Singapore piece. Compiled 7 November 2026. Primary sources are the source of record; press and consultants appear only where no primary figure exists, and are labelled. "My arithmetic" or "inference" marks anything not stated by a source.

## Plain definitions (for the piece)

- **Hyperscaler**: one of the handful of very large cloud and internet companies (Microsoft, Google, Amazon, Oracle, ByteDance, Alibaba) that rent or build whole data centres at a time.
- **Colocation**: a landlord model. The operator builds the hall, the power and the cooling; the tenant brings and owns its servers.
- **Critical IT load / IT power capacity**: the power a hall can deliver to the servers themselves, excluding cooling and losses. DayOne defines it as "the maximum amount of electrical power that is available and allocated specifically for the operation of IT equipment within a facility" (F-1, 5 Oct 2026). Operators quote this; the utility meters total draw, which is higher by the PUE factor (about 1.2 to 1.4 in Johor).
- **Energised**: the power infrastructure and grid connection are finished and live. DayOne: "capacity for which the required power infrastructure and interconnections have been completed and are available for customer use."
- **In service / ready for service (RFS)**: energised and also fully fitted out with mechanical, electrical and cooling plant, so a tenant can move servers in. DayOne: RFS and "fully fitted out and equipped in terms of mechanical, electrical, and plumbing infrastructure systems."
- **Bookings / contracted**: capacity a customer has signed for. **Billings**: the part already paying. **Backlog**: signed but not yet paying.
- **Utilisation rate (DayOne's)**: billings divided by capacity in service. It measures how much finished capacity is being paid for, not how much power is drawn.
- **Take-or-pay**: the tenant pays for the capacity reserved whether or not it uses it. In Johor the energy itself is then passed through at actual consumption.
- **Running**: chips actually drawing power. No operator publishes this; the only measure is the utility's draw.

## 1. Operator table: Johor

IT MW unless stated. "n.p." = not published. Where an operator publishes only a campus build-out size, that goes in "announced".

| Operator | Site(s) | Announced / planned | Contracted | Under construction | In service / operational | As at | Source (primary unless marked) |
|---|---|---|---|---|---|---|---|
| DayOne (ex GDS International) | Nusajaya Tech Park (NTP), Kempas Tech Park (KTP) | Johor bookings about 1.4 GW (NTP 28.8% + KTP 32.5% of 2,281 MW group bookings = about 1,398 MW, my arithmetic) | about 1,398 MW booked (as left) | 616 MW (press summary of F-1; group figure 1,328 MW confirmed) | 789 MW (NTP 47.8% + KTP 34.3% of 962 MW group = about 790 MW) | 20 Sep 2026 | Form F-1, 5 Oct 2026: https://www.sec.gov/Archives/edgar/data/2118192/000119312526414188/d223752df1.htm |
| DayOne, group (for context) | ten markets | 4.6 GW "Resources" | 2,281 MW bookings; 953 MW billings | 1,328 MW | 962 MW; utilisation 99.1% | 20 Sep 2026 (30 Jun 2026: 675 MW in service, 666 MW billing, 98.7%) | F-1, as above |
| YTL Power (YTL Data Center Holdings; Nvidia partner; YTL AI Cloud) | YTL Green Data Center Park, Kulai; new Sedenak Tech Park West campus (Aug 2026) | Kulai raised to up to 1,200 MW from 600 MW; group up to 2,400 MW across Johor and Cyberjaya | 298 MW | n.p. by company | n.p. by company. Brokers: 150 MW delivered at 3QFY26 (MBSB via The Star, 29 Jun 2026); 188 MW operational (Kenanga) | Annual Report 2026 (FY to 30 Jun 2026) | YTL Power Annual Report 2026, MD&A Data Center segment: https://www.ytlpowerinternational.com/wp-content/uploads/ytles/sites/2/files/annual-report/YTLPowerInt_Berhad_Annual_Report_2026.pdf |
| AirTrunk (Blackstone) | JHB1, JHB2 (Iskandar Puteri / Johor Bahru); JHB3, JHB4 announced | JHB1+JHB2 "more than 420MW"; JHB3+JHB4 "more than 280MW"; Malaysia "more than 700MW across four campuses" | JHB1+JHB2 "almost 100% contracted" | JHB2 in development (US$2.325b green financing, 29 Jul 2026) | n.p. (JHB1 operating since 2024 per press; no MW energised published) | 30 Apr 2026 | https://airtrunk.com/airtrunk-doubles-down-in-malaysia-with-two-new-hyperscale-campuses-in-johor-bahru/ ; https://airtrunk.com/airtrunk-secures-us2-325b-green-financing-to-support-sustainable-digital-infrastructure-growth-in-malaysia/ |
| Bridge Data Centres (Bain Capital) | MY06 Sedenak (Kidex), MY07 (Ulu Tiram) | MY06 508 MW, 15 buildings, 275 kV; MY07 374 MW, 8 buildings, 275 kV | n.p. | n.p. | n.p. (press: MY06 opened 2022; MY07 phase 1 2025) | website, 2026 | https://www.bridgedatacentres.com/locations/malaysia/ ; anchor tenant ByteDance per DCD and Epoch AI (not primary) |
| Princeton Digital Group (PDG) | JH1, Sedenak Tech Park; JH2, Senai (press) | JH1 "a 200 MW campus" | n.p. | expansion funded by ~US$1.3b green financing | 52 MW phase 1 delivered July 2024 (MIDA); later phases n.p. | 4 Nov 2026 | https://princetondg.com/press-releases/pdg-secures-usd-1-3-billion-for-jh1-campus-in-johor/ ; https://www.mida.gov.my/mida-news/princeton-digital-delivers-phase-one-of-one-of-southeast-asias-largest-dcs-in-johor/ |
| STT GDC | STT Johor, Nusa Cemerlang, Iskandar Puteri | up to 166 MW | n.p. | phase 1 (STT Johor 1, 16 MW per Feb 2025 groundbreaking) | 0 | 13 Aug 2026 | https://www.sttgdc.com/newsroom/stt-gdc-deepens-malaysia-commitment-up-to-usd-1.37-billion-green-financing-stt-johor-campus ; https://www.sttelemediagdc.com/newsroom/stt-gdc-breaks-ground-high-performance-computing-data-centre-campus-johor-signs-mou-talent-development |
| EdgeConneX | Johor | up to 160 MW | n.p. | n.p. | 36 MW (company page; status undated) | page undated, read 7 Nov 2026 | https://edgeconnex.com/locations/asia-pacific/kl-malaysia |
| K2 Strategic | Sedenak Tech Park | n.p. | n.p. | n.p. | n.p. (Tenaga supply agreement 2023) | | No primary MW found |
| Equinix | JH1 Nusajaya; JH2 | JH2 phase 1 7.2 MW (press) | n.p. | JH2 topped out (press) | JH1 open since 2024; MW n.p. (database says 12 MW, unverified) | | https://www.mida.gov.my/mida-news/equinix-continues-expansion-plan-unveils-new-data-centre/ |
| Microsoft | Kulai (Eco Business Park / QUANTUM Edge land, 123.14 acres bought from Eco World) | n.p. | own use | n.p. | n.p. Microsoft's live Malaysia West region (28 May 2025) is in Greater Kuala Lumpur, not Johor | | https://news.microsoft.com/source/asia/features/microsoft-announces-its-first-cloud-region-in-malaysia-empowering-more-malaysian-organizations-to-accelerate-ai-innovation/ |
| Google | none in Johor | Elmina (Selangor) campus; new campuses in Selangor and Negeri Sembilan (press, 4 Nov 2026) | | | | | Not Johor. Lead: https://www.malaymail.com/news/malaysia/2026/11/04/google-commits-additional-us15b-to-malaysia-data-centre-expansion-over-two-years-projects-37000-jobs-as-anwar-hails-investment/241985 |
| ByteDance (tenant, not operator) | in DayOne, Bridge and others | Johor Menteri Besar: ByteDance investment exceeds RM29.5 billion (Jan 2026, Bernama via Malay Mail) | DayOne's NTP anchor grew "from an initial anchor commitment of 64MW to 838MW" across Johor, Bangkok and Helsinki | | | 20 Sep 2026 | F-1; press lead: https://www.malaymail.com/news/malaysia/2026/01/05/johor-looks-to-lock-in-bytedances-long-term-commitment-after-china-talks-says-onn-hafiz/204326 |

**Market totals for context (consultant, not primary):** Cushman & Wakefield's Asia Pacific Data Centre H1 2026 update puts Johor at 1,110 MW of operational IT capacity, 602 MW under construction and 2,486 MW planning (via EdgeProp and Real Estate Asia: https://edgeprop.my/content/1917257/johor-leads-apac-data-centre-boom-malaysia-tops-construction-%E2%80%94-cw ). I did not find the C&W PDF.

## 2. Fact table: the chip rules

| Date | Measure | What it does | Who it bites in Johor | Source |
|---|---|---|---|---|
| 17 Nov 2023 | US end-user control, EAR §744.23(a)(3) (October 2023 rule) | Licence needed to export advanced computing items (ECCN 3A090.a/.b, 4A090.a/.b) to entities headquartered in Country Group D:5 or Macau, or whose ultimate parent is, wherever located | Chinese-owned tenants receiving chips in Johor | Stated in the BIS guidance of 31 May 2026 (below) |
| 15 Jan 2025 | AI Diffusion Rule, 90 FR 4544; compliance 15 May 2025 | Worldwide tiered licensing; moved the ".a" headquarters requirement into §742.6 | Would have capped Malaysia as a tier-two country | https://www.federalregister.gov/documents/2025/01/15/2025-00636/framework-for-artificial-intelligence-diffusion |
| 13 May 2025 | BIS rescission announcement | Rule not enforced; "BIS plans to publish a regulation formalizing the rescission and will issue a replacement rule in the future"; also announced "additional export licensing requirements for exports of SI chips to Malaysia and Thailand, due to known instances of diversion" | Announced only | https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens |
| to 7 Nov 2026 | Federal Register | No BIS rule formalising the rescission, no replacement rule and no Malaysia or Thailand chip licence rule found in the Federal Register (search of BIS documents since 1 May 2025 mentioning Malaysia, AI or advanced computing) | Non-Chinese buyers in Malaysia still import without a US licence | federalregister.gov API search, 7 Nov 2026 |
| 14 Jul 2025 | Malaysia MITI Strategic Trade Permit | "effective immediately, all exports, tranships and transits of high-performance AI chips of US origin are subject to a Strategic Trade Permit", under the s.12 catch-all of the Strategic Trade Act 2010 with 30 days' notice; an interim step "while Malaysia undertakes further review" on listing them in the Strategic Items List | Chips leaving or passing through Malaysia; not chips imported and run in Johor | https://www.miti.gov.my/miti/resources/Media%20Release/[FINAL]%5FMITI%5FPress%5FStmt%5FMalaysia%5FRegulates%5FTrade%5Fof%5FUS%5FAI%5FChips%5F2025-07-14.pdf |
| 26 Oct 2025 | US and Malaysia Agreement on Reciprocal Trade, Art. 5.2.1 | Malaysia to "align with all unilateral export controls in force by the United States" and "ensure that its companies do not backfill or undermine these controls"; Art. 5.2.3 to explore inbound investment screening | Policy direction; no data centre clause in the body | https://www.whitehouse.gov/briefings-statements/2025/10/agreement-between-the-United-States-of-America-and-Malaysia-on-Reciprocal-Trade/ |
| 30 Sep 2025 / 10 Nov 2025 | Affiliates rule (50% rule), 90 FR 47201, then one-year suspension, 90 FR 50857 | Extends Entity List restrictions to firms 50% or more owned by listed parties; stayed "until November 9, 2026, absent a future extension" | Watch: suspension lapses two days after this note | https://www.federalregister.gov/documents/2025/11/12/2025-19846/one-year-suspension-of-expansion-of-end-user-controls-for-affiliates-of-certain-listed-entities |
| 12 Jan 2026 | Remote Access Security Act (H.R. 2683) passed House 369 to 22 | Would let export controls cover remote (cloud) access to controlled chips; referred to Senate Banking 13 Jan 2026; no further action found | The gap it would close is the Johor one: renting chips to a Chinese firm is not an export | https://www.govinfo.gov/content/pkg/CREC-2026-01-12/html/CREC-2026-01-12-pt1-PgH621-5.htm ; DayOne F-1 risk factors |
| 15 Jan 2026 | BIS rule, 91 FR 1684 | Licence review for Nvidia H200 and lesser chips to China and Macau moved from presumption of denial to case by case, with certifications | Loosens the China route; may reduce the pull to run Chinese workloads abroad | https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities |
| 31 May 2026 | BIS guidance | Confirms the 2023 headquarters requirement is still enforced under §742.6(a)(6)(iii)(A) "to all destinations outside the United States"; the diffusion non-enforcement "applies only to the extent such items are not for entities headquartered in" D:5 or Macau; "Bona fide operators of data centers ... are not required to cease the ongoing use ... until further notice" | Chinese-owned tenants in Johor need licences for new chips; existing installed chips may keep running | https://www.bis.gov/media/documents/bis-guidance-may-31-2026.pdf |
| 10 Jul 2026 | BIS rule, 91 FR 43034 | UAE moved to A:5; license-free advanced computing for approved UAE entities | Contrast: Malaysia got no such status | https://www.federalregister.gov/documents/2026/07/14/2026-14132/enhanced-favorable-treatment-for-the-united-arab-emirates-under-the-export-administration |

**Enforcement record (primary where available):**

| Date | Case | Malaysia link | Source |
|---|---|---|---|
| 19 Mar 2026 | SDNY charges against Super Micro co-founder Yih-Shyan Liaw and two others over about US$2.5 billion of servers with Nvidia GPUs diverted to China | Routed through an unnamed Southeast Asian company (press) | https://www.justice.gov/usao-sdny/pr/three-charged-conspiring-unlawfully-divert-us-artificial-intelligence-technology-china (page did not render for me; details via Bloomberg and The Register) |
| 1 Oct 2026 | Greg Lui (Earthmade Computer) arrested, indictment returned 29 Sep: more than US$300 million of GPU servers to China, 2023 to 2024 | Shipped to "Malaysia and Singapore, where no such license is required"; "more than $176 million from two Malaysia-based shipment companies"; one shipment of 27 servers to Kuala Lumpur | https://www.justice.gov/opa/pr/california-man-arrested-smuggling-more-300-million-export-controlled-computer-servers-china |
| June and 15 Oct 2026 | Royal Malaysian Customs seized 72 and then 30 servers with AI chips (about RM50 million) in the airport free trade zone, "falsely declared as electric components" | Malaysia as a transit hub; origin and destination undisclosed | Press: https://fortune.com/2026/10/28/malaysia-intercepted-ai-chips-shipment-export-controls-china/ (customs statement not found) |
| 2026 (press) | Megaspeed (Singapore): New York Times reports its Malaysian unit bought about US$2 billion of Nvidia chips; Commerce reportedly looking; Singapore police investigating | Data centres in Malaysia and Indonesia | Press only; no primary filing found |

## 3. Short sections

### What fills the halls

DayOne is the biggest single fact in Johor. Its F-1 of 5 October 2026 shows about 789 MW of IT capacity in service in Johor at 20 September 2026, 82% of its group, and 61% of its bookings. One customer, "a global technology company with a leading short-form video platform", paid 69.4% of 2025 revenue and 69.2% in the first half of 2026; the second paid 12.3% and 15.1%. The anchor of NTP grew from 64 MW to 838 MW of bookings across Johor, Bangkok and Helsinki. The filing never says ByteDance; SemiAnalysis and the press do. Malaysia gave DayOne 87.0% of first-half 2026 revenue.

YTL Power reports 298 MW contracted at Kulai, "principally let to third parties under medium to long term leases", and doubled the park's plan to 1,200 MW. Its own reports do not publish MW energised; brokers say 150 to 188 MW. Kenanga says only about 7.5 MW carries the Nvidia-partnered AI cloud, so the "Nvidia data centre" headline is a small slice of a mostly colocation park (broker figure, not primary). The Data Center segment earned RM867.1 million revenue and RM347.4 million pre-tax profit in FY2026, against RM124.1 million and RM32.1 million (Annual Report 2026).

AirTrunk says JHB1 and JHB2, more than 420 MW, are "almost 100% contracted", and has announced more than 280 MW more. Bridge lists 508 MW at MY06 and 374 MW at MY07 but publishes nothing on what is live. No hyperscaler owner (Microsoft, Google, Oracle) has disclosed live Johor capacity; Microsoft's and Google's live Malaysian regions are around Kuala Lumpur.

### How much is really running: the cross-check the live pieces lack

Inference, labelled. DayOne alone had about 789 MW of IT capacity in service in Johor in September 2026, and 99.1% of its in-service capacity was billing. Cushman & Wakefield counts 1,110 MW of operational IT capacity in Johor in June 2026. Yet Tenaga measured the whole of Malaysia's data centres drawing 1,256 MW in June 2026, and the minister gave 1,374 MW for August. Draw at the meter includes cooling, so at a PUE of about 1.3 Johor's operational IT capacity alone would draw about 1.4 GW flat out, above the national draw, before Kuala Lumpur and Cyberjaya are counted. The measures differ (IT rating against metered facility power, different dates and scopes), but the direction is clear: halls that are finished, let and billing draw well below their rating. Billing is not running.

### Contract terms

DayOne: a "significant majority" of contracts run 10 to 15 years, typically with five-year renewals; delivery is "underpinned predominantly by long-term take-or-pay contracts with our hyperscale customers"; "Power is generally charged based on customers' actual power consumption on a pass-through basis." YTL: "medium to long term leases", no years given. AirTrunk, Bridge, PDG, STT GDC: no terms published.

### What the chip rules mean for who can use Johor

1. A Chinese-owned tenant (ByteDance) needs a US licence for any new advanced chips exported to it, in Johor or anywhere, and has since November 2023, not since May 2026. The 31 May 2026 guidance clarified, it did not create. Chips already running may keep running "until further notice".
2. A non-Chinese tenant (Microsoft, Oracle, a Malaysian cloud) imports advanced chips into Malaysia with no US licence: the diffusion rule is not enforced and the announced Malaysia and Thailand requirement has not appeared in the Federal Register.
3. The open door is renting. A Chinese firm that rents computing from a non-Chinese owner in Johor receives no export; the Remote Access Security Act would change that but sits in Senate committee. DayOne's F-1 flags this as a risk.
4. Malaysia's permit polices chips leaving Malaysia, not chips working there. MITI's line since 2025 is that commercial data centre decisions are free if they follow Malaysian law, while the 2025 trade agreement commits Malaysia to "align with all unilateral export controls in force by the United States".
So for Johor's largest operator, the chip gate falls on the speed at which its main tenant can add new chips; it does not shut halls already full.

## 4. What the live pieces have wrong or out of date

Checked: src/content/journal/the-queue-not-the-chip.md (Q) and src/content/journal/contracted-energised-running.md (C), numbers in this slice only. Tenaga and Hansard series are another slice and were not rechecked here.

1. **Q and C: the 31 May 2026 BIS guidance is presented as the start of the licence requirement.** Q: "On 31 May 2026 ... confirmed that advanced computing items need a licence"; C: "under US Commerce Department guidance of 31 May 2026 chips for any tenant headquartered in China or Macau need an American export licence." The requirement dates from 17 November 2023; the guidance says so. Fix: "a licence rule in force since November 2023, which the US Commerce Department confirmed on 31 May 2026".
2. **Q and C: "headquartered in China" is too narrow and "tenant" too broad.** The rule covers Country Group D:5 (China plus other arms-embargoed countries) and Macau, by headquarters or ultimate parent. It attaches to exports to that entity, so chips owned by a non-Chinese landlord or cloud and rented to a Chinese firm need no licence today. C's comparison table ("Do the chips need a US licence? Yes, for any tenant headquartered in China or Macau") overstates it.
3. **Q and C omit the carve-out**: bona fide data centre operators need not stop ongoing use of installed chips "until further notice". This matters to "Part of Johor's idle power waits on Washington": the rule slows new chips, it does not idle installed ones.
4. **Q omits the trade agreement**: Malaysia's 26 October 2025 commitment to align with all US unilateral export controls (Art. 5.2.1). Relevant to "Malaysia's own permit ... not chips running in Johor", which is correct as far as it goes.
5. **Q and C omit that the announced Malaysia and Thailand licence requirement (13 May 2025) was never published as a rule**, and that no replacement for the diffusion rule exists to 7 November 2026. A reader may assume Malaysia is under a US licence regime; it is not, except for Chinese-headquartered buyers.
6. **Q: "DayOne, one of Johor's largest operators"** understates: on its F-1 it has about 789 MW in service in Johor, more than any other operator discloses (AirTrunk's whole two-campus total is 420 MW). Not wrong, but the piece can now say "the largest that discloses".
7. **Q and C: the energised-and-earning point lacks its strongest evidence.** DayOne's 99.1% utilisation (billing over in service) on 962 MW, 789 MW of it in Johor, set against Malaysia-wide draw of 1,256 to 1,374 MW, makes "energised, let and earning while drawing little" concrete. Use with the measurement caveats above.
8. **Q exposure map omits Bridge Data Centres** (MY06 508 MW, MY07 374 MW build-out; ByteDance its reported anchor) and K2, EdgeConneX and Equinix's peers. Bridge is a material omission for "campuses resting on one tenant's licence".
9. **C: "DayOne's largest customer, a global technology company with a leading short-form video platform, provided 69.2% of its revenue in the first half of 2026."** Correct. Could add 69.4% for 2025 and the 64 MW to 838 MW anchor growth.
10. **C: "DayOne ... counts energised and in-service capacity as separate stages"**: correct; the F-1 defines both. Note DayOne publishes in-service, bookings and billings, not an energised MW figure.
11. **Q mentions the January 2026 H200 rule nowhere.** Since 15 January 2026 H200-class chips can be licensed case by case into China itself, which weakens the reason to run Chinese training abroad. It belongs in "What would prove me wrong" or the chips section.
12. **Not checked here, flag for the grid slice:** C line 233 "Johor ... holds 5.6 of Malaysia's 8.35 GW" and line 340 "29 of Malaysia's 61 data centre projects"; Q's "two thirds of secured capacity" (5.6/8.35 = 67%, consistent).

## 5. Open questions

1. No operator publishes energised MW for Johor except DayOne (in service) and EdgeConneX (36 MW, undated). YTL's delivered MW is broker-sourced; ask YTL IR or read its FY2026 analyst briefing slides, which were not on its site.
2. Which DayOne Johor capacity is under construction? The 616 MW figure comes from a press summary of the F-1 (colocationscout.com); I did not find it in the F-1 text, which may hold it in a table image. Check the F-1 "Our Data Center Portfolio" table.
3. How much of ByteDance's Johor capacity runs on chips it owns (licence needed for new ones) versus chips owned by others and rented (no licence)? Not disclosed anywhere.
4. Will BIS extend the affiliates-rule suspension past 9 November 2026? Check the Federal Register next week.
5. Has Malaysia added US-origin AI chips to its Strategic Items List, or amended the Strategic Trade Act in 2026? Not found; a law-firm note says amendments were proposed.
6. Customs statements for the June and 15 October 2026 seizures: primary text not found.
7. Megaspeed: press only. The New York Times story and any Commerce action need a primary document before use.
8. Microsoft's Kulai site: land bought, no status published. Oracle's US$6.5 billion Malaysian region: site not disclosed.
9. Is DayOne's IPO proceeding? 36Kr reported possible postponement; no F-1/A filed as of 7 Nov 2026 (EDGAR list: DRS 10 Aug, DRS/A 10 Sep, F-1 5 Oct).

## Sources read directly (primary)

- DayOne Data Centers, Form F-1, filed 5 Oct 2026 (figures as at 30 Jun and 20 Sep 2026): https://www.sec.gov/Archives/edgar/data/2118192/000119312526414188/d223752df1.htm
- YTL Power International, Annual Report 2026 and 4QFY2026 quarterly report: https://www.ytlpowerinternational.com/investor-relations/quarterly-annual-reports/
- AirTrunk releases, 30 Apr 2026 and 29 Jul 2026 (URLs above)
- Bridge Data Centres Malaysia page (read 7 Nov 2026)
- PDG release, 4 Nov 2026; STT GDC release, 13 Aug 2026; EdgeConneX Malaysia page
- BIS press release, 13 May 2025; BIS guidance, 31 May 2026; Federal Register 91 FR 1684, 90 FR 50857, 91 FR 43034
- MITI press statement, 14 Jul 2025
- US and Malaysia Agreement on Reciprocal Trade, 26 Oct 2025, Art. 5
- DOJ release, 1 Oct 2026 (Lui)
