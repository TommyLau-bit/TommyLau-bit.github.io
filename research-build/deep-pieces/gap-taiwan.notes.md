# Gap scout: Taiwan (2 Nov 2026)

Question: is Taiwan a distinct market for a new deep piece, where chip fabs and AI data halls compete for one tight grid and the government rations data centre connections to protect chipmaking? Or only a third example of the Johor/Singapore rationing mechanism?

Read first: CLAUDE.md, WRITING-FORMAT.md §D and §E, CONSOLIDATION-PLAN.md, UNCAPPED-RESULTS.md, and in full the-queue-not-the-chip.md, hong-kong-has-the-plug.md, america-rations-the-plug.md, the-chip-supply-chain.md (claim watch list includes "How TSMC describes Taiwan's electricity supply").

## Access log (blocks not bypassed)

- moeaea.gov.tw (Energy Administration, home of the 全國電力資源供需報告 PDF and open-data CSV set_id=365): Cloudflare "Sorry, you have been blocked". Not bypassed.
- moea.gov.tw (MOEA press release of 18 Jun 2026, news_id=123066, "經濟部公布114年度全國電力資源供需報告"): HTTP 403. Not bypassed.
- taipower.com.tw (all pages tried, including the topic page "用電有掌握 台灣電力未來10年準備與布局" /topic/2026_tpslfnty/ and the FAQ "為什麼AI資料中心會對區域電網造成巨大挑戰" /2289/2558/2705/68294/): HTTP 202 with empty body (bot challenge). Not bypassed.
- esg.tsmc.com (TSMC sustainability report): HTTP 403. Not bypassed.
- www.sec.gov via curl rejected the declared User-Agent ("undeclared automated tool"); data.sec.gov submissions JSON worked; the 20-F itself was read through WebFetch.
- ithome.com.tw: 403.
- Readable: law.moj.gov.tw, ey.gov.tw, ly.gov.tw (and its Budget Center API), lis.ly.gov.tw, data.gov.tw, udn, CNA, LTN.

## Primary sources found

### 1. Energy Administration Act (能源管理法), as amended and in force (PRIMARY)
- URL: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0130002 (read 2 Nov 2026). History: https://law.moj.gov.tw/LawClass/LawHistory.aspx?pcode=J0130002
- Amendment promulgated 23 Sep 2026: "中華民國一百十五年九月二十三日總統華總一經字第 11500093321 號令修正公布第 2、6、7、9、10、19-1～22、24、29 條條文；增訂第 6-1 條條文".
- Art. 10 para 4, verbatim: "能源用戶新設或增設用電之契約容量達規定容量者，應於期限內設置一定裝置容量以上之自用發電設備或儲能設備。"
- Art. 10 para 5: contract capacity threshold, deadline, installed capacity, type and method "由中央主管機關定之" (left to MOEA regulations; none found published).
- Art. 24 para 1 item 3: failure to install is fined NT$150,000 to 750,000 after an order to improve, "按次處罰" (per instance).
- Art. 30: "本法自公布日施行" (in force on promulgation, so from 23 Sep 2026).
- Already in the Act (unchanged by this amendment, last amended 2009): Art. 16, large investment projects whose energy use has a "重大影響" on national supply "及區域平衡" must file an energy use statement (能源使用說明書) and get MOEA approval, reviewed on "使用數量、種類、效率及區位" (quantity, type, efficiency and location); Art. 25, MOEA may "命能源供應事業停供能源" to a user that builds or expands without approval. This is an existing statutory siting lever over large loads; whether it has been applied to data centres was not found.
- Correction to the Taipei Times lead (12 Aug 2026): it said "preliminary approval"; the bill in fact passed third reading (press: 21 Aug 2026) and was promulgated 23 Sep 2026. The committee version changed "及" to "或" (own generation OR storage) and limited the duty to NEW or EXPANDED contract capacity (existing users exempt).

### 2. Executive Yuan, 14 May 2026 (PRIMARY)
- Release: https://www.ey.gov.tw/Page/9277F759E41CCD91/99136c96-d69c-4078-b4e5-267b9baaa987 (dated 115-05-14). Cabinet approved the MOEA draft; point three: "增訂能源大用戶應設置自用發電及儲能設備，有助於強化企業能源自給能力". Point (四): duty applies when "用電契約之契約容量達一定容量者" (Art. 10).
- Slides, Energy Administration deputy director-general 陳崇憲, 行政院第4002次院會: https://www.ey.gov.tw/File/FB2D2F3FBB9BD04F?A=C . Page 3: "有助於強化能源用戶之能源自給能力，降低對電網依賴。" No threshold figure, no mention of data centres.

### 3. Legislative Yuan bill record (PRIMARY, status only)
- https://ppg.ly.gov.tw/ppg/bills/201110215640000/details : Economics Committee review on 22 Jul and 5 Aug 2026 (per search result summary; gazette "in production").

### 4. Legislative Yuan Budget Center, Oct 2023 budget review (PRIMARY, reporting the 2023 MOEA forecast)
- https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=46494&pid=233330 , dated 112年10月, authors 涂玉枝, 羅玉姍, in the Energy Administration 2024 budget review, item 二０.
- Quote: "據能源署112年6月公告之「111年度全國電力資源供需報告」揭示，預估112~118年全國用電需求年均成長率2.03%" and "預估該期間之夜間備用容量率將由112年之9.5%逐年上升至118年22.6%".
- So in June 2023 the government planned a 2029 night-time reserve margin of 22.6%. The June 2026 report (below, press) gives 7.1% for 2029. Same year, about 15 points lower, in three report cycles. Also: of 42.99 GW net additions 2023 to 2029, 71.83% intermittent and 44.84% solar; 6 GW of 2026 to 2029 gas listed only as "新增燃氣電源" with no named plant.

### 5. Legislative Yuan Budget Center, Aug 2026 topical study (PRIMARY, table of contents only)
- https://www.ly.gov.tw/Pages/List.aspx?nodeid=56712 ; report 115124, 115年8月, author 江穗美, "我國穩定供電與需求面管理相關計畫執行概況之探討". Found through the Budget Center API (https://www.ly.gov.tw/WebAPI/BudgetCenterResearch.aspx, type 專題研究).
- Problem heading one, verbatim: "備用容量率長期多年未達法定目標，且備用供電容量重要來源之燃氣機組建設多次修正計畫，並延後期程及調增成本". Full text not online; figures from it are press only (see udn, 27 Oct 2026 below).

### 6. TSMC Form 20-F for 2025, filed 16 Apr 2026 (PRIMARY)
- https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- Risk factor heading: "Our operations may be interrupted, and our expansion may be limited, by power or other utility outages or shortages". Body includes: "We have occasionally experienced power outages, dips or surges caused by difficulties encountered by our electricity supplier or other power consumers on the same power grid." and "our future capacity expansions could be curtailed". No consumption figure found in the 20-F read.
- Bears on the-chip-supply-chain claim watch item "How TSMC describes Taiwan's electricity supply": TSMC itself names power as a limit on expansion.

### 7. National Development Council and MOEA written reports, LY Economics Committee, 16 Apr 2026 (PRIMARY, negative finding)
- https://lis.ly.gov.tw/lydbmeetr/uploadn/115/1150416/313.pdf (NDC) and /311.pdf (MOEA). 2025 renewables 22.872 GW installed (solar 15.474, wind 4.517, hydro 2.124), 37.814 billion kWh generated. No mention of data centres, 桃園以北 or 5MW in either.

## Secondary sources (leads, press relaying primary documents not readable here)

### A. The 114年度 national power supply and demand report (MOEA, 18 Jun 2026)
- CNA, 18 Jun 2026: https://www.cna.com.tw/news/afe/202606180283.aspx . 2026 to 2035 demand growth "年均成長率約為2.5%" (previous report 1.7%; 2016 to 2025 average 1.24%). Night-peak load growth 2.7% a year. AIDC: about 1.2 GW of new demand applications filed; MOEA has prepared "2GW至3GW" for AIDC. Semiconductor demand is built from fab, memory and server makers' applications to Taipower, assuming use lags application by about six months. Night-peak reserve 2026 to 2029 about 3,020 to 5,056 MW; 2030 to 2035 6,591 to 11,088 MW. New gas about 26 GW 2026 to 2035. Maanshan restart not in the plan.
- Economic Daily News, 5 Jul 2026: https://udn.com/news/story/7238/9608305 . Night-peak reserve 2028: 3.3 GW, 8%; 2029: 3 GW, 7.1%; 2030: 6.5 GW, 15.2%, after four gas units of 3.51 GW (Dalin new gas 2, Tongxiao new gas 4, Mailiao new gas 1 and 2) due in the second half of 2029.
- udn, 27 Oct 2026 (reporting the LY Budget Center study 115124): https://udn.com/news/story/6656/9838503 . Night reserve 12.8% (2026), 12.5% (2027), 8% (2028), 7.1% (2029); legal target 15% under 備用供電容量管理辦法 Art. 4; 10 of 14 years since 2012 below 15%, five straight years since 2021.
- Taipei Times editorial, 12 Aug 2026 (original lead): https://taipeitimes.com/News/editorials/archives/2026/08/12/2003862328 . Confirms 2.5% vs 1.7%, night reserve "below the 15 percent benchmark from this year through 2029", "falling to 7.1 percent".

### B. The 5 MW restriction north of Taoyuan and its July 2026 easing (all press; Taipower and MOEA pages blocked)
- Origin: Economic Daily News, 15 Jul 2026, https://money.udn.com/money/story/11162/9628824 : "台電在2023年供電會議就做出決議，並且通知業者". Publicly stated by Taipower chairman 曾文生 in Aug 2024 (udn https://udn.com/news/story/7238/9206829 ; Business Next https://www.bnext.com.tw/article/80273/ ).
- 2024 numbers: Executive Yuan spokesman 陳世凱 said north Taiwan used about 93 billion kWh in 2023 and generated about 75 billion (Taipower: 931 vs 750), a gap of about 20 billion kWh (as relayed in press; EY or Taipower primary not found).
- Easing: MOEA minister 龔明鑫 announced on 13 Jul 2026 in Taoyuan; 曾文生 on 15 Jul: because Datan units 7, 8, 9 "已接受調度" and the Hsieh-ho (協和, Keelung) rebuild passed environmental review, Taoyuan and Keelung may propose AI data centre zones near the plants (udn 15 Jul, above; China Times 16 Jul https://www.chinatimes.com/newspapers/20260716000638-260110 ).
- Radius: Economic Daily News, 27 Jul 2026, https://udn.com/news/story/7238/9652344 : MOEA "有條件" eased 5 MW+ AIDC north of Taoyuan, "必須在大潭電廠及協和電廠附近"; Kung told the Economics Committee "約2公里左右". AIDC applications typically "30到50MW". Taipower: whether 2 km applies nationwide is case by case.
- Not verified at primary: the 2023 Taipower decision itself, any written rule, the July 2026 conditions, the 2 km figure.

### C. Threshold of the new Art. 10 duty (press)
- 環境資訊中心, 23 Jul 2026, https://e-info.org.tw/node/243682 : Kung at the 22 Jul committee: "初步規劃將以5MW作為討論基礎，約涵蓋700家業者"; grace period about five years; regulations expected within six months; ratio to start low and rise.
- CNA, 5 Aug 2026, https://www.cna.com.tw/news/aipl/202608050127.aspx : committee passed; aims at "半導體及大型資料中心等產業".
- udn, 21 Aug 2026 third reading: https://udn.com/news/story/6656/9706188 .
- No draft regulation (辦法) or 預告 found as of 2 Nov 2026. The threshold is not in the statute.

### D. Semiconductor and TSMC load (press)
- TechNews/CNA, 27 Jul 2026, https://technews.tw/?p=1593562 : Taipower estimate (chairman 曾文生, Cathay forum) semiconductor use about 52 billion kWh in 2026, 80 billion in 2030, 110 billion in 2035. Other press (udn 9652340) gives shares of 17% (2026), 24% (2030), 30% (2035) of national use.
- TSMC electricity: 25.55 billion kWh in 2024, 9% of a national 283.82 billion (LTN, 28 Sep 2025, https://ec.ltn.com.tw/article/paper/1725922 , from TSMC's sustainability report). 2025: 28.77 billion kWh, 20.1% renewable, Taiwan fabs 11.4% renewable (press on TSMC's 2025 sustainability report, reccessary/LTN; esg.tsmc.com 403, not read). About 10% of national use is press arithmetic.

## Mechanism test (new, or a third example of Johor/Singapore?)

What Taiwan shares with Singapore: the state chooses which halls may plug in, by place and size (5 MW, north of Taoyuan, now within about 2 km of two plants). On that limb alone Taiwan is a third example of rationing the plug, and a piece built on it would repeat the Singapore mechanism with a new name. The working claim as given (5 MW north of Taoyuan limited through 2028) is exactly that limb, and it rests on press only.

What is different, and would be new to the site:
1. The scarce thing is generation at night, not the connection. The night-peak reserve margin is planned below the 15% legal target every year 2026 to 2029, bottoming at 7.1% (press of the June 2026 report), against 22.6% planned for the same year in June 2023 (LY Budget Center, primary). Singapore's limit is land and green power; Johor's is booked connections; Hong Kong has a quarter spare.
2. The competing load is the chip factory, and the forecast is built from fab applications. Taipower: semiconductors 52 to 110 billion kWh by 2035 (press). Data centre applications about 1.2 GW (press). TSMC's own 20-F says its expansion "may be limited" by power shortages (primary). This turns the-chip-supply-chain's long-run limb ("I still expect the grid to be the slower clock") into something testable in the one place the fabs are.
3. Own power is compelled by statute, not escaped into. Art. 10 para 4 (in force 23 Sep 2026, primary) makes every new or expanded large contract build own generation or storage. That is the inverse of Singapore, where the journal shows a turbine buys "not one megawatt of licensed computing", and of America, where on-site power is a voluntary route round the queue. And the siting rule ties new halls to named power stations, the reverse of Johor's grid-built-to-campus model.
4. It answers a standing falsifier: "two-governments-one-confession" breaks if "a third constrained market does neither". Taiwan does neither: it neither builds connections ahead (Malaysia) nor runs a call with efficiency tests (Singapore); it sites halls at the power station and makes them bring their own.

So Taiwan can be a distinct mechanism, but only if the piece is framed on 1 to 3 (night-time adequacy, chip fab as the protected load, compelled own power), not on the 5 MW ban.

## What would make it publishable

- Read the 114年度 全國電力資源供需報告 itself (moeaea.gov.tw blocked here): night-peak reserve table 2026 to 2035, the AIDC load line, the semiconductor load line.
- A Taipower or MOEA written record of the 5 MW rule and the July 2026 conditions (LY gazette for the 22 Jul and 5 Aug 2026 committee sittings once published; the gazette was "in production").
- MOEA's Art. 10 regulation (threshold, ratio, deadline), expected within about six months of promulgation, so around March 2027.
- TSMC's 2025 sustainability report figure read at source.

## Candidate dated claim (reworded from the working claim)

"Taiwan protects chipmaking by making new AI halls bring their own power: before 1 January 2029 MOEA sets the Energy Administration Act Article 10 threshold at 5 MW or below, and the official night-time reserve margin forecast for 2028 stays below 10%." Breaks if the threshold is set above 5 MW or the duty is suspended, or the next supply and demand report lifts 2028 to 10% or more, or Taipower connects a 5 MW+ data centre north of Taoyuan outside the designated plant zones.
