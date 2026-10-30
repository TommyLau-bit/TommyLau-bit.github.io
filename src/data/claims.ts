// ── The claims ───────────────────────────────────────────────────────────────
//
// One entry per Analysis piece, listed on /claims. brand/check-piece.py fails
// an Analysis piece that has no entry here. The claim and the test are fixed
// once published: never reword them to fit what happened. There are no
// statuses or reviews: the page is a plain record of what was claimed, when,
// and what would prove it wrong.

export type Claim = {
  id: string;         // the piece slug
  claim: string;      // one sentence, first person where it is judgement
  breaksIf: string;   // the falsifier, from the piece
  watch: string[];    // the observable evidence, from the piece
  date?: string;      // ISO, the day the claim first went live; fixed, so republishing a merged slug never re-dates it
  home?: string;      // slug of the deep piece that now carries the claim; set only at merge time (see below)
};

export const CLAIMS: Claim[] = [
  {
    id: 'the-queue-not-the-chip',
    date: '2026-07-27',
    claim: 'In Johor and Singapore, a finished grid connection, not chip supply, is the scarce thing holding the AI buildout back.',
    breaksIf: 'Connection waits keep shrinking the way Malaysia\'s Green Lane cut them from 36 months to 12, or transformer and cable lead times normalise faster than utilities commit capital.',
    watch: ['Transformer and high-voltage cable lead times', 'The Green Lane project count beyond 33', 'Malaysia\'s contracted against used data centre load (2,346 MW contracted, about 1,374 MW used, August 2026, Hansard)', 'Who wins Singapore\'s capacity award'],
  },
  {
    id: 'the-part-money-cannot-hurry',
    date: '2026-09-22T18:48:00+08:00',
    home: 'the-queue-not-the-chip',
    claim: 'A grid connection queue is really two queues. Governments can shorten the paperwork one, but the equipment one sets the pace.',
    breaksIf: 'Connection timelines keep compressing across the board, or equipment lead times normalise faster than utility spending is committed. Also if building power on site removes the constraint rather than moving it.',
    watch: ['Transformer and high-voltage cable lead times', 'The Green Lane project count beyond 33', 'Whether the press-reported 72.76 per cent Johor-Singapore zone utilisation is confirmed at source', 'Who wins Singapore\'s capacity award under the 1.25 ceiling'],
  },
  {
    id: 'two-governments-one-confession',
    date: '2026-09-22T19:40:00+08:00',
    home: 'the-queue-not-the-chip',
    claim: 'Malaysia building more grid and Singapore rationing who may connect are opposite answers to the same shortage of connection capacity.',
    breaksIf: 'Malaysia\'s spending turns out to be ordinary renewal weighted towards generation rather than connection, or Singapore\'s efficiency ceiling moves on a fixed schedule rather than with scarcity, or a third constrained market does neither.',
    watch: ['The Green Lane project count beyond 33', 'Who wins the Singapore capacity award', 'Whether Johor\'s 72.76 per cent utilisation figure is restated or explained'],
  },
  {
    id: 'the-power-it-drops',
    date: '2026-09-22T18:53:00+08:00',
    home: 'america-rations-the-plug',
    claim: 'The grid\'s new problem with AI data centres is not the power they draw. It is the gigawatts they can drop in under a second.',
    breaksIf: 'Ride-through turns out to be a cheap settings change rather than a constraint, or Virginia\'s 3.8 gigawatt trip proves to be a local fault rather than how these sites are built.',
    watch: ['Whether PJM\'s ride-through requirements become firm rules', 'Whether grid operators outside North America follow', 'Whether the next comparable disturbance drops less than 3.8 gigawatts'],
  },
  {
    id: 'the-way-out-has-its-own-queue',
    date: '2026-09-22T18:56:00+08:00',
    home: 'building-your-own-power',
    claim: 'Building your own power on site does not escape the queue. Turbines, transformers and switchgear have queues of their own.',
    breaksIf: 'Turbine lead times fall while the backlog is still being worked through, or large sites energise on their own generation faster than comparable sites get a grid connection, or transformers and switchgear stop being the constraint.',
    watch: ['Gas turbine lead times, and whether announced factory expansions land on schedule', 'Behind-the-meter capacity actually energised against grid-connected', 'Transformer and high-voltage cable lead times'],
  },
  {
    id: 'what-the-battery-is-really-for',
    date: '2026-09-22T19:01:00+08:00',
    home: 'america-rations-the-plug',
    claim: 'Large batteries are increasingly bought as connection equipment that lets a site switch on early, not as a way to trade electricity.',
    breaksIf: 'New storage stops clustering where computing load is and spreads out with renewable generation instead, or connection waits shorten enough that opening early stops being worth paying for.',
    watch: ['Where new storage is built relative to new computing load', 'Whether grid operators start requiring this equipment, not just permitting it', 'Whether anyone reports storage bought for connection separately from storage bought for trading'],
  },
  {
    id: 'the-product-is-time',
    date: '2026-09-24T13:43:00+08:00',
    home: 'building-your-own-power',
    claim: 'Bloom Energy\'s customers are paying for an earlier switch-on date, not for cheaper electricity.',
    breaksIf: 'Bloom keeps winning sites where a grid connection is available on schedule, or its deployment times stretch towards turbine and grid timelines, or its gross margin holds while grid waits shorten.',
    watch: ['Bloom\'s time from order to energised power', 'Grid and turbine waits', 'Bloom\'s gross margin against those waits', 'Whether Bloom stays primary supply at sites like Project Jupiter or becomes a bridge'],
  },
  {
    id: 'power-first-chips-last',
    date: '2026-09-25T14:00:00+08:00',
    home: 'contracted-energised-running',
    claim: 'The order builders commit in reveals the constraint, and at Jane Street power now comes first and chips last.',
    breaksIf: 'Chips become the longest wait again while transformer and generator lead times fall back to months, or dropping full generator backup proves a false saving.',
    watch: ['Published lead times for transformers and generators', 'Whether builders keep describing the building as the first decision', 'Whether partial backup spreads, or disappears after the first serious failure'],
  },
  {
    id: 'every-megawatt-got-harder',
    date: '2026-09-25T12:30:00+08:00',
    home: 'powering-the-rack',
    claim: 'What Vertiv sells per megawatt is rising, because AI makes every megawatt harder to power and cool.',
    breaksIf: 'Vertiv\'s growth only ever tracks the megawatts being built, or its margin shrinks while orders stay strong, or the biggest buyers take cooling in-house.',
    watch: ['Adjusted operating margin, quarter by quarter', 'Service revenue against product revenue', 'Whether the 800 VDC line ships on Nvidia\'s timetable', 'Whether Vertiv brings back a backlog figure'],
  },
  {
    id: 'oklo-sells-the-electricity',
    date: '2026-09-29T12:49:48+08:00',
    home: 'nuclear-for-ai',
    claim: 'Oklo is a seller of electricity, not reactors, and the model stands or falls on building its first plant.',
    breaksIf: 'Oklo starts selling reactors outright to raise cash, or Aurora in Idaho slips well past 2028 or produces power uncompetitive with gas, or the letters of intent stay letters.',
    watch: ['The pace of construction in Idaho', 'The first non-binding agreement becoming a binding power purchase agreement', 'A firm HALEU fuel supply contract', 'New capital needed before the first electricity is sold'],
  },
  {
    id: 'marvell-collects-the-toll',
    date: '2026-09-28T13:25:16+08:00',
    home: 'ten-thousand-chips-one-thought',
    claim: 'Marvell is paid every time AI chips talk, through the signal processor in each optical plug, whoever made the chips.',
    breaksIf: 'The translation moves off the plug at scale, through linear pluggable or co-packaged optics, or Marvell\'s interconnect growth stalls while clusters keep growing.',
    watch: ['Whether 1.6T links keep a DSP on board', 'How much of Marvell\'s growth comes from optics rather than custom chips', 'Whether the ten largest customers keep rising as a share of revenue'],
  },
  {
    id: 'nebius-paid-for-what-is-switched-on',
    date: '2026-09-30T13:16:44+08:00',
    home: 'contracted-energised-running',
    claim: 'AI buyers pay for connected power, and Nebius\'s edge is turning contracted power into connected power faster than they can.',
    breaksIf: 'Prepayments fade, or Nebius misses 800 megawatts connected by the end of 2026, or its customers start selling their own spare capacity.',
    watch: ['Connected megawatts against the target', 'The share of new deals with prepayments', 'Whether revenue spreads beyond Microsoft and Meta', 'Whether any hyperscaler starts renting capacity out instead of in'],
  },
  {
    id: 'corning-lays-the-glass',
    date: '2026-10-01T12:01:55+08:00',
    home: 'ten-thousand-chips-one-thought',
    claim: 'Glass fibre is the part of the AI network that outlives every chip generation, and Corning is paid each time a campus grows.',
    breaksIf: 'Fibre stops being scarce as Corning and Chinese producers expand, shown by the segment\'s margin falling while its sales rise.',
    watch: ['Enterprise Networks growth against the rest of Optical Communications', 'Segment profit margin as sales rise', 'The two largest customers\' share of the segment'],
  },
  {
    id: 'broadcom-wins-either-way',
    date: '2026-10-02T12:05:07+08:00',
    home: 'ten-thousand-chips-one-thought',
    claim: 'Broadcom is paid whether the cloud giants stay with Nvidia or leave for their own chips.',
    breaksIf: 'Custom chip customers move work to other designers, as Google has partly done with MediaTek, or Nvidia\'s own networking wins inside its clusters.',
    watch: ['Networking\'s share of Broadcom\'s AI revenue', 'Whether the custom chip customer count rises beyond six', 'What happens to the Google work between Broadcom and MediaTek', 'Whether gross margin keeps falling as custom chips grow'],
  },
  {
    id: 'ti-feeds-the-chip',
    date: '2026-10-02T12:49:47+08:00',
    home: 'powering-the-rack',
    claim: 'The move to 800 volt racks turns Texas Instruments\' small, cheap power chips into a growing data centre business.',
    breaksIf: 'Racks stay at 54 volts for years, or rivals hold the demanding high end, or TI\'s new 300mm lines run part-empty as industrial and car demand weakens.',
    watch: ['Data centre as a share of TI\'s revenue', 'Named operators committing to 800 volt racks', 'Gross margin as the new Sherman capacity comes online'],
  },
  {
    id: 'tsmc-says-it-is-the-bottleneck',
    date: '2026-10-02T12:49:47+08:00',
    home: 'the-chip-supply-chain',
    claim: 'On today\'s horizon, TSMC\'s factories bind before the grid does. Over the longer run, I still expect the grid to be the slower clock.',
    breaksIf: 'For today: TSMC\'s tightness eases while data centres with chips on order still wait for power. For the longer run: TSMC still calls capacity tight in 2028 while grid connection waits shorten.',
    watch: ['Whether TSMC keeps calling packaging capacity tight', 'Whether Arizona\'s second fab reaches volume in the second half of 2027', 'High-performance computing as a share of TSMC\'s revenue', 'How TSMC describes Taiwan\'s electricity supply'],
  },
  {
    id: 'lumentum-makes-the-light',
    date: '2026-10-05T14:01:18+08:00',
    home: 'ten-thousand-chips-one-thought',
    claim: 'The AI network\'s bottleneck has moved to the laser, which only a few indium phosphide factories can make at volume.',
    breaksIf: 'Lumentum\'s gross margin slides towards the low forties as new capacity arrives, or Coherent\'s six-inch wafers take the 200 gigabit EML orders, or silicon photonics routes around the EML.',
    watch: ['Lumentum\'s gross margin as new factories come online', '200 gigabit EMLs as a share of Lumentum\'s laser sales', 'Hyperscaler capital spending'],
  },
  {
    id: 'schneider-sells-the-finished-system',
    date: '2026-10-07T14:17:41+08:00',
    home: 'the-equipment-queue',
    claim: 'Schneider Electric\'s AI data centre growth is arriving as finished systems, built and tested in its factories, rather than as loose parts, because skilled hours on site are now scarcer than equipment, so Systems will keep taking a larger share of its revenue.',
    breaksIf: 'Systems falls below 34 per cent of Schneider\'s group revenue, its 2025 level, for the full year 2026 or 2027 while Schneider describes Data Centre and Networks sales as growing double digit; or Products outgrows Systems on an organic basis for two quarters running while data centres remain Schneider\'s main growth driver.',
    watch: ['Systems as a share of group revenue, each year', 'Systems against Products organic growth, each quarter', 'Whether Schneider keeps naming prefabricated solutions as a data centre growth driver', 'Whether Schneider\'s executives stop describing site labour as a constraint'],
  },
  {
    id: 'ge-vernova-sells-the-wait',
    date: '2026-10-09T11:22:31+08:00',
    home: 'building-your-own-power',
    claim: 'GE Vernova is expanding gas turbine output inside its existing factories, paid for by customers\' deposits, so its queue will stay at four or more years of its planned output through 2030 rather than clear.',
    breaksIf: 'Before 2030, gigawatts under contract fall below four years of the annual output GE Vernova has planned for that year (20 GW now, 24 from 2028, 30 from 2030), or GE Vernova announces a new heavy-duty turbine factory, or Power deposits and price per kilowatt fall while orders stay strong.',
    watch: ['Gigawatts under contract against planned annual output, each quarter', 'Power segment contract liabilities in each filing', 'Whether slot reservations convert into orders or lapse', 'Whether the 24 gigawatt output step lands in 2028'],
  },
  {
    id: 'hitachi-energy-plans-the-queue',
    date: '2026-10-22T12:51:38+08:00',
    home: 'the-equipment-queue',
    claim: 'Hitachi Energy is adding factories only as fast as signed orders justify, and its order backlog will stay at or above about 2.5 times annual revenue, roughly three years of work, through fiscal 2030, which ends on 31 March 2031, so the queue for its transformers and HVDC links will not clear.',
    breaksIf: 'Hitachi Energy\'s order backlog divided by its revenue over the previous four quarters, both in US dollars as Hitachi reports them (about 3.06 at 30 June 2026), falls below 2.5 at two consecutive quarter ends before 31 March 2031, the end of fiscal 2030; or its orders for any full fiscal year up to fiscal 2030 fall below its revenue for that year.',
    watch: ['Hitachi Energy backlog divided by trailing four quarters of revenue, each quarter', 'Hitachi Energy annual orders against annual revenue', 'Whether the South Boston, Virginia (2028) and Mississippi (2029) transformer plants start on time', 'Hitachi Energy\'s published delivery times for its own transformer components, including the 140 weeks quoted for some Ludvika bushings', 'Whether Hitachi announces capacity ahead of signed orders'],
  },
  {
    id: 'eaton-order-book-outruns-it',
    date: '2026-10-26T08:03:14+08:00',
    home: 'the-equipment-queue',
    claim: 'Eaton is shipping more electrical gear than ever, yet its Electrical Americas backlog keeps growing faster than its sales, so the queue for the equipment inside a data centre\'s fence, measured in months of sales on order, will keep lengthening until its new plants arrive in 2027.',
    breaksIf: 'Electrical Americas backlog divided by the segment\'s sales over the previous four quarters (1.05 at June 2026, up from 1.04 in March) falls for two consecutive quarters before mid 2027, when the new plants start; or falls below 0.93, its June 2025 level, before the end of 2027; or the segment\'s twelve-month book-to-bill falls below 1.0 for two quarters running; or Electrical Americas margin is still falling year on year after Eaton reports price and cost back to neutral.',
    watch: ['Electrical Americas backlog divided by trailing four quarters of segment sales, each quarter, and whether it keeps rising', 'Electrical Americas twelve-month book-to-bill', 'Electrical Americas operating margin, year on year', 'Whether the Nebraska switchgear and South Carolina transformer plants start production on time in 2027, and whether Eaton says its extended lead times are shrinking'],
  },
  {
    id: 'siemens-energy-measures-the-shortage',
    date: '2026-10-28T11:50:30+08:00',
    home: 'the-equipment-queue',
    claim: 'By Siemens Energy\'s own estimate, demand for large and medium power transformers in Europe and North America exceeds the combined capacity of all market players in the region in every year through its fiscal 2030, which ends on 30 September 2030, so unfilled orders keep accumulating even as the gap narrows: Grid Technologies\' orders stay above its revenue each fiscal year and its backlog in euros keeps growing.',
    breaksIf: 'Before 30 September 2030: Grid Technologies\' orders fall below its revenue for any full fiscal year; or its order backlog in euros, as Siemens Energy reports it (€51bn at 30 June 2026), falls for two consecutive quarters; or Siemens Energy publishes a revised estimate showing transformer capacity meeting demand in Europe and North America before fiscal 2030.',
    watch: ['Grid Technologies orders against revenue, each fiscal year', 'Grid Technologies backlog in euros, each quarter', 'Whether the Charlotte large power transformer plant ships in 2027 and the Nuremberg expansion opens by 2028', 'Whether Siemens Energy updates its transformer market and capacity chart'],
  },
  {
    id: 'ajinomoto-grows-with-the-package',
    date: '2026-10-07T17:47:04+08:00',
    home: 'the-chip-supply-chain',
    claim: 'Ajinomoto\'s build-up film is used by the area and layer count of each chip package, so as AI packages grow wider and taller its film volume shifts to AI servers faster than chip counts imply, and because a rival film takes a long time to qualify, Ajinomoto keeps that growth at high margins.',
    breaksIf: 'In any of Ajinomoto\'s annual results presentations through fiscal 2029 (the year to March 2030), servers and networks fall below 70 per cent of its ABF volume by application, its fiscal 2025 level (the split is rounded to five points, so a flat 70 per cent passes); or the business profit margin of its Functional Materials business, part of the Healthcare and Others segment, falls below 50 per cent in a year when that business\'s sales still grow. Ajinomoto discloses the margin only as rounded wording ("over 50%"); if it stops doing so, the test rests on the volume split alone.',
    watch: ['Ajinomoto\'s ABF volume by application, each May', 'Functional Materials business sales growth and business profit margin, each year', 'Whether construction at the Kani City, Gifu site starts in 2028 and operation in fiscal 2032', 'Whether Sekisui Chemical or LG Chem announce adoption of their build-up film in AI server substrates'],
  },
  {
    id: 'asml-booked-ahead',
    date: '2026-10-07T17:48:04+08:00',
    home: 'the-chip-supply-chain',
    claim: 'ASML\'s EUV machines are sold out and committed a year or two ahead, and their number grows only as fast as ZEISS optics and ASML\'s cleanrooms allow, about 30 per cent a year, so a chipmaker adding leading-edge AI capacity must commit to scanners a year or two ahead, much as a data centre books a grid connection.',
    breaksIf: 'The booking half fails if ASML says it has EUV capacity beyond what customers have ordered; or ships more than 10 per cent fewer low NA EUV systems than its stated capacity (around 65 for 2026, around 85 for 2027) and itself attributes the shortfall to customer demand or pushed-out orders; or by its fourth quarter 2026 results (January 2027) no longer describes 2027 as close to fully covered with orders; or says its EUV order lead times are shortening. The growth half fails if ASML raises its stated low NA EUV capacity by more than 40 per cent in a single year, or announces new EUV cleanroom space or a second source for its optics. A shortfall caused by ZEISS or other suppliers supports the claim rather than breaking it.',
    watch: ['ASML\'s EUV units each quarter, and low NA (NXE) units in its annual report', 'How ASML describes order coverage for 2027 and 2028', 'Whether ASML confirms the further 30 per cent low NA capacity increase for 2028', 'High NA adoption after Intel qualified it on select 18A layers in July 2026'],
  },
  {
    id: 'micron-three-times-the-wafer',
    date: '2026-10-07T17:49:04+08:00',
    home: 'the-chip-supply-chain',
    claim: 'Micron sells most of each year\'s HBM before that year starts, and because each HBM bit takes about three times the wafer of ordinary DRAM, every year HBM grows faster than conventional DRAM it takes wafers from ordinary memory and keeps that market short too, through calendar 2028.',
    breaksIf: 'The first half fails if, by its fiscal first quarter 2028 results (around December 2027), Micron has not said most of its calendar 2028 HBM supply is agreed; or if Micron reports unsold HBM or cuts HBM output and itself attributes it to customer demand. The second half fails if, before the end of calendar 2028, Micron stops expecting the DRAM industry to be supply-constrained in 2027 or 2028 while still expecting industry HBM bits to grow faster than conventional DRAM; or if Micron states that any current HBM generation needs less than about three times the wafer of DDR5 per bit. A shortage prolonged by late cleanrooms supports the claim rather than breaking it.',
    watch: ['Whether Micron says next year\'s HBM is agreed, each autumn (it usually does between September and December)', 'Micron\'s industry DRAM supply outlook and whether HBM still outgrows conventional DRAM', 'Any new trade ratio Micron gives for HBM4 or HBM4E', 'Whether Micron\'s ID1 fab in Idaho starts wafer output in mid 2027'],
  },
  {
    id: 'constellation-restarts-the-reactor',
    date: '2026-10-30T11:47:00+08:00',
    home: 'nuclear-for-ai',
    claim: 'The fastest nuclear power Constellation can bring to AI this decade comes from reactors that already hold a place on the grid: at Crane the reactor can be ready by 2027, but a fresh grid connection would not have been fully ready until around 2030 or later.',
    breaksIf: 'Crane, with the 760 MW of grid rights transferred from Eddystone, has still not delivered power to the grid at full output by 31 December 2028, which would mean the reactor work and not the connection set the pace; or restarts and uprates that need new grid capacity are connected as quickly as those that reuse an existing one.',
    watch: ['Crane\'s first power to the grid against the 2027 target', 'Whether Crane reaches full deliverability before PJM\'s transmission upgrades finish', 'Palisades and Duane Arnold restart dates, and whether reactor work or the connection sets them', 'Whether the first of the 890 MW Google uprates lands in 2028'],
  },
  {
    id: 'the-plug-not-the-chip',
    date: '2026-10-30T14:20:52+08:00',
    home: 'the-queue-not-the-chip',
    claim: 'In Johor and Singapore the grid connection, not the chip, decides who gets to build: Malaysia\'s data centres, two thirds of whose secured capacity is in Johor, will draw less than 40% of the maximum demand of the data centre projects in Tenaga\'s system at June 2027, and Singapore will add data centre capacity only through calls for applications with efficiency and green energy conditions.',
    breaksIf: 'Tenaga\'s figures for June 2027 show Malaysia\'s data centre load at 40% or more of the maximum demand of the data centre projects in its system, or, before 1 January 2028, Singapore allocates capacity to a new data centre, or new capacity to an existing one, other than through a call for applications carrying efficiency and green energy conditions. Capacity regained by redeveloping or replacing an existing hall within its current allocation, and capacity allocated before 30 October 2026, do not count.',
    watch: ['Tenaga\'s data centre load against maximum demand in system, each quarter (1,256 MW against 5.65 GW, June 2026)', 'Dewan Rakyat figures for signed, operating and drawn data centre load (1.37 GW of 6 GW operating, August 2026), and the Energy Commission study of actual requirements', 'BIS licensing of advanced chips to entities headquartered in Country Group D:5, and DayOne\'s customer concentration', 'Singapore\'s next Data Centre Call for Application (review 18 to 24 months from August 2026) and any capacity allocated outside a call', 'IMDA\'s first efficiency regulations for existing halls under the Digital Infrastructure Act'],
  },
  {
    id: 'america-rations-the-plug',
    date: '2026-10-30T14:20:52+08:00',
    home: 'america-rations-the-plug',
    claim: 'America is rationing the grid connection rather than speeding it up: by the end of 2027, data centres of 50 megawatts or more will be running on an early-connection tier the grid may cut first in at least two of its seven organised grids, and once PJM\'s ride-through deadline for existing sites passes, its data centres will stop dropping to backup power in blocks of 1,500 megawatts or more after normally cleared faults.',
    breaksIf: 'By 31 December 2027, fewer than two of ERCOT, PJM, MISO, SPP, NYISO, ISO New England and CAISO have a load of 50 MW or more, mainly a data centre, actually energised under an early-connection tier the grid may cut first, such as ERCOT\'s Provisional Controllable Load Resource, SPP\'s CHILLS, PJM\'s Interim NITS or CAISO\'s flexible interim service, shown in a filed service agreement or the operator\'s own report; curtailment rights that apply to all large loads during emergency load shed, such as Texas Senate Bill 6, do not count. Or, between 16 January 2028 and 31 December 2028, PJM reports a transfer of 1,500 MW or more of large load to backup generation or off the grid after a normally cleared fault.',
    watch: ['Service agreements for ERCOT PCLR, SPP CHILLS, PJM Interim NITS, CAISO FILI and NYISO and ISO-NE non-firm services', 'RTO and transmission owner filings in EL26-67 to EL26-72 (November 2026) and FERC\'s orders on them', 'ERCOT\'s audit reports (due by 10 December 2026) and the date approvals to energise resume', 'PJM\'s large computational load ride-through filing (November 2026), its limited exceptions, and NERC\'s standards due 31 December 2026', 'PJM event reports of large load transfers after normally cleared faults, from 16 January 2028', 'PJM base auctions against the cap and the reliability requirement, starting with 2029/2030 in December 2026', 'Whether any connection is approved on a computing cut, including DTE\'s 350 MW tied to Google\'s Van Buren site', 'CAISO battery lead at the evening net peak, summer 2027, and PJM\'s four-hour storage rating for 2030/2031'],
  },
  {
    id: 'the-equipment-queue',
    date: '2026-10-30T14:20:52+08:00',
    home: 'the-equipment-queue',
    claim: 'The first wave of new transformer and switchgear plants will not shorten the equipment queue in years of work: at 30 June 2028, Siemens Energy Grid Technologies\' order backlog will still be at least 3.6 times its revenue over the previous four quarters (3.96 at 30 June 2026), and Eaton Electrical Americas\' backlog at least 1.0 times its sales over the previous four quarters (1.05), even though Siemens Energy\'s own chart allows its ratio to fall while the pile grows.',
    breaksIf: 'At 30 June 2028, as each company reports it, Siemens Energy Grid Technologies\' order backlog in euros divided by its revenue over the previous four quarters is below 3.6, or Eaton Electrical Americas\' backlog divided by its sales over the previous four quarters is below 1.0.',
    watch: ['Siemens Energy Grid Technologies backlog over trailing four quarters of revenue, each quarter (3.96 at 30 June 2026; backlog rounded to €1bn)', 'Eaton Electrical Americas backlog over trailing four quarters of sales, each quarter (1.05 at 30 June 2026)', 'Whether Eaton\'s Jonesville and Bellevue plants start in 2027 and Siemens Energy\'s Nuremberg expansion opens by 2028', 'Dates for Siemens Energy\'s Charlotte expansion and Greater Richland switchgear plant (none in its 3 February 2026 release)', 'Whether Siemens Energy updates its transformer demand and capacity chart', 'Hitachi Energy\'s ratio (about 3.1 at 30 September 2026), tested by its own claim'],
  },
  {
    id: 'building-your-own-power',
    date: '2026-10-30T14:20:52+08:00',
    home: 'building-your-own-power',
    claim: 'Building your own gas power swaps the grid\'s queue for the makers\' queues, and the fast lane is queued too: GE Vernova\'s gas turbine gigawatts under contract at 31 December 2027 will be no lower than at 31 December 2026, and at 31 December 2027 its aeroderivative backlog, units ordered less units shipped since 1 January 2025, will still exceed its aeroderivative units shipped in the previous twelve months.',
    breaksIf: 'GE Vernova reports fewer gigawatts of gas turbines under contract, firm orders and slot reservations together, at 31 December 2027 than at 31 December 2026, or at 31 December 2027 its aeroderivative units ordered less units shipped since 1 January 2025 are equal to or fewer than its aeroderivative units shipped in calendar 2027.',
    watch: ['GE Vernova gigawatts under contract each quarter (122 GW at 30 September 2026; at least 130 GW expected at 31 December 2026)', 'GE Vernova aeroderivative units ordered and shipped, each 10-Q and 10-K (cumulative backlog since 1 January 2025: 124 units at 30 September 2026, about 2.3 years of trailing twelve-month shipments)', 'Power segment contract liabilities and current deferred income (US$33.2bn at 30 September 2026)', 'Earliest delivery year of heavy-duty slots sold (2032, October 2026), the 24 GW step in 2028, and any new heavy-duty factory', 'Howmet and Siemens Energy casting capacity dates', 'Permian rig count and Texas LNG exports against Texas power burn (EIA)'],
  },
  {
    id: 'nuclear-for-ai',
    date: '2026-10-30T14:20:52+08:00',
    home: 'nuclear-for-ai',
    claim: 'Nuclear power for AI arrives in the order of what each project already has: restarts and uprates of existing American reactors, which reuse a licensed site, a grid place and ordinary fuel, deliver this decade, while reactors fuelled with HALEU deliver little before 2031, because government stock covers only a few first cores and commercial enrichment at the level they need has stopped in America and not started at the plants contracted to replace it.',
    breaksIf: 'Reactors fuelled with HALEU together send electricity to American grids from 100 MW or more of capacity on or before 31 December 2030; or none of Crane, Palisades or Duane Arnold has delivered power to the grid by 31 December 2029.',
    watch: ['First electricity to a grid from Aurora-INL (target 2028), Kemmerer Unit 1 (complete 2030) and Hermes 2 (operations 2030)', 'First enrichment of uranium at ASP Isotopes\' Pelindaba plant, and the size of the Energy Department\'s HALEU commitments', 'Whether Centrus agrees with the Energy Department to operate the Piketon HALEU cascade privately (maintenance only since 30 June 2026), and progress on the one tonne due by July 2032', 'A definitive Centrus and Oklo HALEU agreement', 'Crane (2027), Palisades (no date since 21 October 2026) and Duane Arnold (first quarter 2029 at the latest) first power to the grid', 'Constellation uprate megawatts in service and the NRC\'s expected uprate list', 'EIA Uranium Marketing Annual Report: Russian and US-origin SWU after the waivers end on 1 January 2028'],
  },
  {
    id: 'powering-the-rack',
    date: '2026-10-30T14:20:52+08:00',
    home: 'powering-the-rack',
    claim: '800 volts reaches the AI rack before it reaches the building: until 2028, 800 VDC enters data halls through power racks and row power centres fed from AC power rooms, and no data hall of 10 MW or more goes into service fed by a facility-level rectifier or solid-state transformer. 800 VDC here includes ±400 VDC, 800 V pole to pole.',
    breaksIf: 'Before 1 January 2028, Nvidia, a data centre operator or its equipment supplier states that a data hall of 10 MW or more is in service with 800 VDC distributed from a facility-level rectifier or solid-state transformer, rather than from power racks or row power centres fed by AC. 800 VDC includes ±400 VDC, 800 V pole to pole.',
    watch: ['Nvidia\'s 800 VDC power rack shipping (due second half of 2026) and row power centre (expected 2027)', 'A date for Nvidia\'s DC power block for direct medium-voltage conversion', 'Foxconn\'s 40 MW Kaohsiung-1 site, built for 800 VDC: how it is fed when it goes into service', 'The solid-state transformer specification past version 0.3 (July 2026)', 'Vertiv\'s next stated per-MW opportunity (US$3.25m to 3.75m, May 2026)', 'Data centre as a share of TI\'s revenue (about 13%, Q3 2026)'],
  },
  {
    id: 'heat-and-water',
    date: '2026-10-30T14:20:52+08:00',
    home: 'heat-and-water',
    claim: 'In AI data centres heat sets the cooling method and water sets where and how the heat leaves the building, not how many halls get built: every Google campus that Google itself names as at high water risk (Mesa, Waltham Cross and Canelones) will consume under 50 million gallons of water in each of 2026 and 2027, and no hyperscaler will report a new evaporatively cooled campus drawing on a water source it rates at high risk.',
    breaksIf: 'Google reports consumption of 50 million gallons or more in 2026 or 2027 at Mesa, Waltham Cross or Canelones; or Google, Microsoft, Amazon or Meta reports opening a data centre cooled by evaporating water from a source it rates at high risk of depletion or scarcity; or a large AI campus with its power already secured is cancelled outright over water rather than redesigned to cool without it.',
    watch: ['Google\'s per-site water table each year (Mesa 9.7 million gallons consumed in 2025; Waltham Cross and Canelones not yet listed)', 'Google\'s share of freshwater withdrawal from high-risk sources (15%, 14%, 13% for 2023 to 2025)', 'New campuses disclosed by Microsoft, Amazon and Meta with their cooling and water source', 'Henderson, Nevada (239.4 million gallons consumed in 2025) and how Google rates its source', 'Permit refusals on water grounds, and whether projects redesign or leave'],
  },
  {
    id: 'the-plug-stays',
    date: '2026-10-30T14:20:52+08:00',
    home: 'ten-thousand-chips-one-thought',
    claim: 'Between the racks of an AI cluster the optical plug stays the default through 2028: switches with co-packaged optics keep their lasers in removable front-panel modules, and Nvidia\'s reference designs for its newest systems keep specifying pluggable switches, as both Vera Rubin designs do today, with the Spectrum-X SN6600-LD and the InfiniBand Quantum-X800 Q3400-RD.',
    breaksIf: 'By the end of 2028, either of Nvidia\'s DGX SuperPOD reference architectures for its newest systems specifies a co-packaged optics switch as the default or only option for the compute fabric, or Nvidia or Broadcom says most of the AI switches it ships carry co-packaged optics, or either ships a co-packaged AI switch as standard whose lasers are fixed to the package rather than in replaceable modules.',
    watch: ['Which switch the next DGX SuperPOD reference architectures specify (for Vera Rubin: pluggable SN6600-LD in the Spectrum-X design, 15 Sep 2026; pluggable Q3400-RD Quantum-X800 in the InfiniBand design), and Feynman\'s "Spectrum-class optical scale-out"', 'SPIL co-packaged optical engine capacity against the 15x mid-2027 target (Nvidia, 21 Oct 2026)', 'Any Nvidia or Broadcom statement of the shipped mix of co-packaged and pluggable switches', 'Laser shortage statements from Lumentum and Broadcom, and Lumentum\'s fiscal 2027 annual report on optical circuit switch buyers other than Google', 'Whether a second cloud giant states optical circuit switches join chips in a production AI cluster, and whether any lab says a named model was trained across Fairwater sites'],
  },
  {
    id: 'the-chip-supply-chain',
    date: '2026-10-30T14:20:52+08:00',
    home: 'the-chip-supply-chain',
    claim: 'In the AI chip supply chain, the parts that only one or a few qualified makers can supply, and that grow only through new cleanrooms, stay sold more than a year ahead. In its results published between 1 December 2027 and 31 March 2028, ASML will describe its 2029 low NA EUV supply as close to fully covered by orders or short of demand, and by its fiscal first quarter 2029 results, around December 2028, Micron will have said most of its calendar 2029 HBM supply is agreed.',
    breaksIf: 'ASML, in its results published between 1 December 2027 and 31 March 2028, says its 2029 low NA EUV capacity exceeds customer orders, or does not describe 2029 as close to fully covered or short of demand; or Micron, by its fiscal first quarter 2029 results (around December 2028), has not said most of its calendar 2029 HBM supply is agreed, or reports unsold HBM and attributes it to customer demand. A shortfall caused by late cleanrooms or suppliers supports the claim rather than breaking it.',
    watch: ['How ASML describes 2028 and 2029 low NA EUV supply against demand, and the size of its 2028 capacity step (Capital Markets Day, 10 June 2027)', 'Whether Micron says most of next year\'s HBM is agreed, each autumn, and whether ID1 starts wafer output in mid 2027', 'How far ahead Seagate says data centre nearline supply is allocated (vast majority through calendar 2028 at 27 October 2026)', 'Whether TSMC publishes any CoWoS capacity or lead time figure', 'Whether Ajinomoto\'s Kani City film plant starts construction in 2028'],
  },
  {
    id: 'contracted-energised-running',
    date: '2026-10-30T14:20:52+08:00',
    home: 'contracted-energised-running',
    claim: 'An AI campus\'s capacity arrives in stages, and energised power is the last one its builder controls: at Abilene, whose tenant ordered its chips with the campus, and at Nebius, which installs its own chips under contracts with delivery dates, computing follows the power within months, so contracted or announced gigawatts overstate it, while in Malaysia, where Johor holds two thirds of secured data centre capacity, halls can be energised and let well before they run.',
    breaksIf: 'Crusoe reports the Abilene campus energised or complete by the end of 2026 but Oracle has not reported all eight buildings delivered to its customer by its results for the quarter ending 28 February 2027, or Nebius reports at least 800 megawatts connected at the end of 2026 but, at 30 June 2027, reports active power below 800 megawatts or, if it reports no active figure, annualised revenue below US$9.6 billion, 800 megawatts at its stated 2026 base of US$12 million a megawatt.',
    watch: ['Oracle\'s Abilene delivery figures in its December 2026 and March 2027 results (Oracle reports delivery, not running, by site)', 'Any Crusoe statement that phase two is energised or complete', 'Nebius connected power at the end of 2026, and active power or annualised revenue at 30 June 2027 (about 170 MW active and US$1.25bn, end 2025; US$3.0bn, June 2026)', 'Tenaga\'s data centre load against booked maximum demand (1,256 MW against 5.65 GW, June 2026)'],
  },
  {
    id: 'hong-kong-has-the-plug',
    claim: 'Hong Kong\'s grid is building to its data centres, not holding them back: CLP will have completed the 18 data centre substations in its 2024 to 2028 Development Plan by 31 December 2028, and Sandy Ridge\'s first phase will be energised by 31 December 2027.',
    breaksIf: 'CLP\'s interim or annual results show fewer than 18 data centre substations completed in its 2024 to 2028 Development Plan by 31 December 2028, or Sandy Ridge\'s first phase is not energised by 31 December 2027.',
    watch: ['Data centre substations completed in CLP\'s interim and annual results, every six months (eight by June 2026, one more targeted in the second half of 2026; 18 planned by 2028)', 'Sandy Ridge\'s first phase against CLP\'s mid-2027, Range\'s 2028 and the government\'s 2029', 'CLP\'s installed capacity and local maximum demand in the annual Ten-year Summary (9,258 MW against 7,455 MW in 2025; a margin below 15% is a warning, not a break)', 'CLP\'s quarterly sales to data centres (+12.8%, 6.6% of sales, nine months 2026)', 'Range Intelligent Computing\'s filings for Hong Kong capacity, customers and chips', 'BIS licensing of H200-class chips to end users located in China, and any change to 15 CFR 742.6 or to Hong Kong\'s treatment'],
    date: '2026-10-30',
  },
];

export const claimOf = (id: string) => CLAIMS.find((c) => c.id === id);

// ── Merged pieces (CLAUDE.md, "Merging keeps the record") ─────────────────────
// When a piece merges into a deep piece, its claim keeps its id (the old slug,
// which research notes point at) and gains `home`: the deep piece's slug. The
// deep piece anchors the old slug (<a id="old-slug"></a>) and quotes the claim
// in its "Claims on record" block. A claim without `home` still lives at its
// own piece. A draft's claim gets `date` when its piece first goes live.

// The slug of the piece that carries the claim today.
export const homeOf = (c: Claim) => c.home ?? c.id;

// Where to link a claim: the anchored section of its deep piece once merged.
export const claimHref = (c: Claim) => (c.home ? `/journal/${c.home}/#${c.id}` : `/journal/${c.id}/`);

// The title of the section a claim's link lands on: the heading (or bold lead)
// right after its <a id> anchor in the deep piece. Undefined for a claim that
// still lives at its own piece, which the piece's title names instead.
export function claimSection(c: Claim, body = ''): string | undefined {
  if (!c.home) return undefined;
  const m = body.match(new RegExp(`<a id="${c.id}"></a>\\s*(?:#{2,4} (.+)|\\*\\*(.+?)\\*\\*)`));
  return (m?.[1] ?? m?.[2])?.trim().replace(/[*_`]/g, '');
}

// Every claim a piece carries: those homed at it, plus its own.
export const claimsHomedAt = (slug: string) => CLAIMS.filter((c) => c.home === slug || c.id === slug);
