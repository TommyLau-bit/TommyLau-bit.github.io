// ── The claims ledger ────────────────────────────────────────────────────────
//
// One entry per Analysis piece. brand/check-piece.py fails an Analysis piece
// that has no entry here. The claim and the tests are fixed once published:
// never reword them to fit what happened. Only `reviews` grows.
//
// Add a review when the evidence named in `watch` moves, usually after the
// company's results or the regulator's next publication. A review is dated,
// carries a status and says in a sentence or two what changed. The latest
// review sets the status shown. No review yet means Open.

export type Status = 'open' | 'holding' | 'pressure' | 'broken';

export const STATUS_LABEL: Record<Status, string> = {
  open: 'Open',
  holding: 'Holding',
  pressure: 'Under pressure',
  broken: 'Broken',
};

export const STATUS_MEANING: Record<Status, string> = {
  open: 'Made, not yet tested against new evidence.',
  holding: 'The evidence since publication points the way I said.',
  pressure: 'Some evidence is running against it. Not yet decided.',
  broken: 'The test I named has been met. I was wrong, and the review says how.',
};

export type Review = { date: string; status: Exclude<Status, 'open'>; note: string };

export type Claim = {
  id: string;         // the piece slug
  claim: string;      // one sentence, first person where it is judgement
  breaksIf: string;   // the falsifier, from the piece
  watch: string[];    // the observable evidence, from the piece
  reviews: Review[];  // oldest first
};

export const CLAIMS: Claim[] = [
  {
    id: 'the-queue-not-the-chip',
    claim: 'In Johor and Singapore, a finished grid connection, not chip supply, is the scarce thing holding the AI buildout back.',
    breaksIf: 'Connection waits keep shrinking the way Malaysia\'s Green Lane cut them from 36 months to 12, or transformer and cable lead times normalise faster than utilities commit capital.',
    watch: ['Transformer and high-voltage cable lead times', 'The Green Lane project count beyond 33', 'Johor-Singapore zone utilisation past 72.76 per cent', 'Who wins Singapore\'s capacity award'],
    reviews: [],
  },
  {
    id: 'the-part-money-cannot-hurry',
    claim: 'A grid connection queue is really two queues. Governments can shorten the paperwork one, but the equipment one sets the pace.',
    breaksIf: 'Connection timelines keep compressing across the board, or equipment lead times normalise faster than utility spending is committed. Also if building power on site removes the constraint rather than moving it.',
    watch: ['Transformer and high-voltage cable lead times', 'The Green Lane project count beyond 33', 'Johor-Singapore zone utilisation past 72.76 per cent', 'Who wins Singapore\'s capacity award under the 1.25 ceiling'],
    reviews: [],
  },
  {
    id: 'two-governments-one-confession',
    claim: 'Malaysia building more grid and Singapore rationing who may connect are opposite answers to the same shortage of connection capacity.',
    breaksIf: 'Malaysia\'s spending turns out to be ordinary renewal weighted towards generation rather than connection, or Singapore\'s efficiency ceiling moves on a fixed schedule rather than with scarcity, or a third constrained market does neither.',
    watch: ['The Green Lane project count beyond 33', 'Who wins the Singapore capacity award', 'Whether Johor\'s 72.76 per cent utilisation figure is restated or explained'],
    reviews: [],
  },
  {
    id: 'the-power-it-drops',
    claim: 'The grid\'s new problem with AI data centres is not the power they draw. It is the gigawatts they can drop in under a second.',
    breaksIf: 'Ride-through turns out to be a cheap settings change rather than a constraint, or Virginia\'s 3.8 gigawatt trip proves to be a local fault rather than how these sites are built.',
    watch: ['Whether PJM\'s ride-through requirements become firm rules', 'Whether grid operators outside North America follow', 'Whether the next comparable disturbance drops less than 3.8 gigawatts'],
    reviews: [],
  },
  {
    id: 'the-way-out-has-its-own-queue',
    claim: 'Building your own power on site does not escape the queue. Turbines, transformers and switchgear have queues of their own.',
    breaksIf: 'Turbine lead times fall while the backlog is still being worked through, or large sites energise on their own generation faster than comparable sites get a grid connection, or transformers and switchgear stop being the constraint.',
    watch: ['Gas turbine lead times, and whether announced factory expansions land on schedule', 'Behind-the-meter capacity actually energised against grid-connected', 'Transformer and high-voltage cable lead times'],
    reviews: [],
  },
  {
    id: 'what-the-battery-is-really-for',
    claim: 'Large batteries are increasingly bought as connection equipment that lets a site switch on early, not as a way to trade electricity.',
    breaksIf: 'New storage stops clustering where computing load is and spreads out with renewable generation instead, or connection waits shorten enough that opening early stops being worth paying for.',
    watch: ['Where new storage is built relative to new computing load', 'Whether grid operators start requiring this equipment, not just permitting it', 'Whether anyone reports storage bought for connection separately from storage bought for trading'],
    reviews: [],
  },
  {
    id: 'the-product-is-time',
    claim: 'Bloom Energy\'s customers are paying for an earlier switch-on date, not for cheaper electricity.',
    breaksIf: 'Bloom keeps winning sites where a grid connection is available on schedule, or its deployment times stretch towards turbine and grid timelines, or its gross margin holds while grid waits shorten.',
    watch: ['Bloom\'s time from order to energised power', 'Grid and turbine waits', 'Bloom\'s gross margin against those waits', 'Whether Bloom stays primary supply at sites like Project Jupiter or becomes a bridge'],
    reviews: [],
  },
  {
    id: 'power-first-chips-last',
    claim: 'The order builders commit in reveals the constraint, and at Jane Street power now comes first and chips last.',
    breaksIf: 'Chips become the longest wait again while transformer and generator lead times fall back to months, or dropping full generator backup proves a false saving.',
    watch: ['Published lead times for transformers and generators', 'Whether builders keep describing the building as the first decision', 'Whether partial backup spreads, or disappears after the first serious failure'],
    reviews: [],
  },
  {
    id: 'every-megawatt-got-harder',
    claim: 'What Vertiv sells per megawatt is rising, because AI makes every megawatt harder to power and cool.',
    breaksIf: 'Vertiv\'s growth only ever tracks the megawatts being built, or its margin shrinks while orders stay strong, or the biggest buyers take cooling in-house.',
    watch: ['Adjusted operating margin, quarter by quarter', 'Service revenue against product revenue', 'Whether the 800 VDC line ships on Nvidia\'s timetable', 'Whether Vertiv brings back a backlog figure'],
    reviews: [],
  },
  {
    id: 'oklo-sells-the-electricity',
    claim: 'Oklo is a seller of electricity, not reactors, and the model stands or falls on building its first plant.',
    breaksIf: 'Oklo starts selling reactors outright to raise cash, or Aurora in Idaho slips well past 2028 or produces power uncompetitive with gas, or the letters of intent stay letters.',
    watch: ['The pace of construction in Idaho', 'The first non-binding agreement becoming a binding power purchase agreement', 'A firm HALEU fuel supply contract', 'New capital needed before the first electricity is sold'],
    reviews: [],
  },
  {
    id: 'marvell-collects-the-toll',
    claim: 'Marvell is paid every time AI chips talk, through the signal processor in each optical plug, whoever made the chips.',
    breaksIf: 'The translation moves off the plug at scale, through linear pluggable or co-packaged optics, or Marvell\'s interconnect growth stalls while clusters keep growing.',
    watch: ['Whether 1.6T links keep a DSP on board', 'How much of Marvell\'s growth comes from optics rather than custom chips', 'Whether the ten largest customers keep rising as a share of revenue'],
    reviews: [],
  },
  {
    id: 'nebius-paid-for-what-is-switched-on',
    claim: 'AI buyers pay for connected power, and Nebius\'s edge is turning contracted power into connected power faster than they can.',
    breaksIf: 'Prepayments fade, or Nebius misses 800 megawatts connected by the end of 2026, or its customers start selling their own spare capacity.',
    watch: ['Connected megawatts against the target', 'The share of new deals with prepayments', 'Whether revenue spreads beyond Microsoft and Meta', 'Whether any hyperscaler starts renting capacity out instead of in'],
    reviews: [],
  },
  {
    id: 'corning-lays-the-glass',
    claim: 'Glass fibre is the part of the AI network that outlives every chip generation, and Corning is paid each time a campus grows.',
    breaksIf: 'Fibre stops being scarce as Corning and Chinese producers expand, shown by the segment\'s margin falling while its sales rise.',
    watch: ['Enterprise Networks growth against the rest of Optical Communications', 'Segment profit margin as sales rise', 'The two largest customers\' share of the segment'],
    reviews: [],
  },
  {
    id: 'broadcom-wins-either-way',
    claim: 'Broadcom is paid whether the cloud giants stay with Nvidia or leave for their own chips.',
    breaksIf: 'Custom chip customers move work to other designers, as Google has partly done with MediaTek, or Nvidia\'s own networking wins inside its clusters.',
    watch: ['Networking\'s share of Broadcom\'s AI revenue', 'Whether the custom chip customer count rises beyond six', 'What happens to the Google work between Broadcom and MediaTek', 'Whether gross margin keeps falling as custom chips grow'],
    reviews: [],
  },
  {
    id: 'ti-feeds-the-chip',
    claim: 'The move to 800 volt racks turns Texas Instruments\' small, cheap power chips into a growing data centre business.',
    breaksIf: 'Racks stay at 54 volts for years, or rivals hold the demanding high end, or TI\'s new 300mm lines run part-empty as industrial and car demand weakens.',
    watch: ['Data centre as a share of TI\'s revenue', 'Named operators committing to 800 volt racks', 'Gross margin as the new Sherman capacity comes online'],
    reviews: [],
  },
  {
    id: 'tsmc-says-it-is-the-bottleneck',
    claim: 'On today\'s horizon, TSMC\'s factories bind before the grid does. Over the longer run, I still expect the grid to be the slower clock.',
    breaksIf: 'For today: TSMC\'s tightness eases while data centres with chips on order still wait for power. For the longer run: TSMC still calls capacity tight in 2028 while grid connection waits shorten.',
    watch: ['Whether TSMC keeps calling packaging capacity tight', 'Whether Arizona\'s second fab reaches volume in the second half of 2027', 'High-performance computing as a share of TSMC\'s revenue', 'How TSMC describes Taiwan\'s electricity supply'],
    reviews: [],
  },
  {
    id: 'lumentum-makes-the-light',
    claim: 'The AI network\'s bottleneck has moved to the laser, which only a few indium phosphide factories can make at volume.',
    breaksIf: 'Lumentum\'s gross margin slides towards the low forties as new capacity arrives, or Coherent\'s six-inch wafers take the 200 gigabit EML orders, or silicon photonics routes around the EML.',
    watch: ['Lumentum\'s gross margin as new factories come online', '200 gigabit EMLs as a share of Lumentum\'s laser sales', 'Hyperscaler capital spending'],
    reviews: [],
  },
];

export const claimOf = (id: string) => CLAIMS.find((c) => c.id === id);
export const statusOf = (c: Claim): Status => c.reviews.at(-1)?.status ?? 'open';
