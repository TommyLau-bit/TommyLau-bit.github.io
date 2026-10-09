// ── The map of the stack ─────────────────────────────────────────────────────
//
// The physical layers of an AI data centre, from the grid connection inward.
// Every published piece belongs to exactly one layer: brand/check-piece.py
// fails a piece that is not listed here. Companies on the map are not curated:
// they are read from the exposure boxes of the pieces in each layer.

export type Layer = {
  id: string;
  name: string;
  kind: 'energy' | 'compute';
  what: string;       // one plain sentence: what physically happens here
  constraint: string; // one plain sentence: what binds
  pieces: string[];   // piece slugs, best entry point first
};

export const STACK: Layer[] = [
  {
    id: 'grid',
    name: 'The grid connection',
    kind: 'energy',
    what: 'High-voltage power arrives from the public grid through a substation built for the site.',
    constraint: 'The wait for a connection, and the transformers and switchgear behind it, now runs to years.',
    pieces: ['the-queue-not-the-chip', 'the-part-money-cannot-hurry', 'hitachi-energy-plans-the-queue', 'siemens-energy-measures-the-shortage', 'two-governments-one-confession', 'the-power-it-drops', 'pjm-sends-the-bill'],
  },
  {
    id: 'onsite',
    name: 'Power on site',
    kind: 'energy',
    what: 'Turbines, fuel cells, batteries and, one day, small reactors make or store power beside the building.',
    constraint: 'Skipping the grid queue means joining the queue for the equipment instead.',
    pieces: ['the-way-out-has-its-own-queue', 'ge-vernova-sells-the-wait', 'the-product-is-time', 'what-the-battery-is-really-for', 'fluence-short-of-american-made', 'constellation-restarts-the-reactor', 'oklo-sells-the-electricity'],
  },
  {
    id: 'distribution',
    name: 'Power inside the building',
    kind: 'energy',
    what: 'Power is stepped down, backed up and carried to each rack, then down to below one volt at the chip.',
    constraint: 'At a megawatt per rack, the copper needed at today\'s low voltage stops fitting.',
    pieces: ['the-rack-runs-out-of-copper', 'every-megawatt-got-harder', 'schneider-sells-the-finished-system', 'eaton-order-book-outruns-it', 'ti-feeds-the-chip'],
  },
  {
    id: 'cooling',
    name: 'Cooling',
    kind: 'energy',
    what: 'Almost every watt that goes into a chip comes back out as heat, and liquid now carries most of it away.',
    constraint: 'Air stops working somewhere between 30 and 50 kilowatts per rack.',
    pieces: ['cooling-is-half-the-job', 'room-to-spare', 'water-is-a-siting-problem'],
  },
  {
    id: 'network',
    name: 'The network between chips',
    kind: 'compute',
    what: 'Thousands of chips swap partial results constantly, over copper inside the rack and light everywhere else.',
    constraint: 'A slow link leaves the most expensive silicon in the building waiting.',
    pieces: ['ten-thousand-chips-one-thought', 'marvell-collects-the-toll', 'broadcom-wins-either-way', 'corning-lays-the-glass', 'lumentum-makes-the-light'],
  },
  {
    id: 'memory',
    name: 'Memory',
    kind: 'compute',
    what: 'Stacked memory sits beside each processor, feeding it the model\'s numbers.',
    constraint: 'For most of the time a model is answering, the chip is waiting on memory, not maths.',
    pieces: ['the-countertop-is-the-bottleneck', 'micron-three-times-the-wafer', 'seagate-sells-the-terabyte'],
  },
  {
    id: 'chips',
    name: 'Chips and the factories that make them',
    kind: 'compute',
    what: 'The processors that do the work, and the few factories able to make and package them.',
    constraint: 'A new chip factory takes two to three years to build and one to two more to fill.',
    pieces: ['the-two-seconds-after-you-hit-send', 'tsmc-says-it-is-the-bottleneck', 'nobody-makes-a-b200-alone', 'asml-booked-ahead', 'ajinomoto-grows-with-the-package'],
  },
  {
    id: 'operators',
    name: 'Who runs the capacity',
    kind: 'compute',
    what: 'The companies that turn power, buildings and chips into computing that someone else can use.',
    constraint: 'Buyers pay for megawatts switched on, not megawatts signed.',
    pieces: ['nebius-paid-for-what-is-switched-on', 'power-first-chips-last'],
  },
];

export const layerOf = (id: string) => STACK.find((l) => l.pieces.includes(id));
