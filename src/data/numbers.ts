// ── The numbers that matter ──────────────────────────────────────────────────
//
// Physical and structural figures only: power, distance, time, capacity.
// Never a share price, a valuation or a forecast of anyone's revenue.
// Each figure is as the linked piece cites it, on that piece's date or the
// date given in `asOf`. When a figure is overtaken, update it here and say so
// in `note`, rather than editing history out of the piece.

export type Num = {
  layer: string;   // a STACK layer id
  value: string;   // the figure, as it should read large
  what: string;    // one plain sentence: what it measures and why it matters
  piece: string;   // the slug of the piece that explains it
  asOf: string;    // when the figure was true
  note?: string;
};

export const NUMBERS: Num[] = [
  // the grid connection
  { layer: 'grid', value: '36 → 12 months', what: 'How far Malaysia\'s Green Lane Pathway cut the wait for a new grid connection. The paperwork queue can be shortened by policy.', piece: 'two-governments-one-confession', asOf: 'March 2026' },
  { layer: 'grid', value: '3.8 GW', what: 'Data centre maximum demand in Johor after more than doubling in a year, about one and a half times the state\'s own electricity use.', piece: 'the-queue-not-the-chip', asOf: '2025' },
  { layer: 'grid', value: '3.8 GW', what: 'Demand that vanished from the grid in under a second when data centres in northern Virginia tripped offline together. The largest such event in PJM\'s history.', piece: 'the-power-it-drops', asOf: '22 July 2026' },
  { layer: 'grid', value: '1.25', what: 'The power usage effectiveness Singapore requires to win new data centre capacity. Megawatts go to whoever wastes the fewest of them.', piece: 'two-governments-one-confession', asOf: '2026' },
  { layer: 'grid', value: '~40% → ~10%', what: 'How far demand for large and medium power transformers in Europe and North America runs ahead of the combined capacity of all makers in the region, by Siemens Energy\'s estimate: about 40 per cent in fiscal 2025 and still about 10 per cent in fiscal 2030.', piece: 'siemens-energy-measures-the-shortage', asOf: '20 November 2025' },

  // power on site
  { layer: 'onsite', value: '116 GW', what: 'Gas turbine capacity GE Vernova has under contract. A buyer who skips the grid queue joins this one.', piece: 'the-way-out-has-its-own-queue', asOf: '1 September 2026' },
  { layer: 'onsite', value: '54–60%', what: 'Share of the energy in gas a solid oxide fuel cell turns into electricity, against roughly 35 to 40 per cent for a simple gas turbine.', piece: 'the-product-is-time', asOf: '2026' },
  { layer: 'onsite', value: '53%', what: 'Share of planned 2026 American utility-scale battery additions sited in Texas, 12.9 of 24 gigawatts. Storage is following the computing load.', piece: 'what-the-battery-is-really-for', asOf: 'February 2026' },
  { layer: 'onsite', value: '75 MW', what: 'The design output of Oklo\'s first Aurora reactor in Idaho, small enough to sit beside a data centre campus.', piece: 'oklo-sells-the-electricity', asOf: '2026' },
  { layer: 'onsite', value: '~6 years', what: 'Gas turbine capacity GE Vernova has under contract, 116 gigawatts, against its output of 20 gigawatts a year. The queue for building your own power, measured in factory time.', piece: 'ge-vernova-sells-the-wait', asOf: '30 June 2026' },
  { layer: 'onsite', value: '15 GWh', what: 'Planned yearly capacity of the Houston plant that assembles Fluence\'s American-made battery systems. American-made, not batteries, is the scarce kind.', piece: 'fluence-short-of-american-made', asOf: 'August 2026' },

  // power inside the building
  { layer: 'distribution', value: '5–10 kW', what: 'What a traditional server rack drew for two decades. Everything in the building was sized for this.', piece: 'cooling-is-half-the-job', asOf: '2026' },
  { layer: 'distribution', value: '~140 kW', what: 'Peak draw of one current Nvidia rack of 72 GPUs, in the footprint of a fridge.', piece: 'room-to-spare', asOf: '2026' },
  { layer: 'distribution', value: '1 MW', what: 'The draw Nvidia\'s next rack generation, Kyber, is designed for in a single cabinet.', piece: 'the-rack-runs-out-of-copper', asOf: 'due 2027' },
  { layer: 'distribution', value: '200 kg', what: 'Copper busbar a one megawatt rack would need at today\'s 54 volts, by Nvidia\'s own figure. The reason the industry is moving to 800 volts.', piece: 'the-rack-runs-out-of-copper', asOf: '2026' },

  // cooling
  { layer: 'cooling', value: '30–50 kW', what: 'The rack density at which air can no longer carry heat away fast enough.', piece: 'cooling-is-half-the-job', asOf: '2026' },
  { layer: 'cooling', value: '85–90%', what: 'Share of each AI server\'s heat that leaves through liquid cold plates in a current Jane Street data hall.', piece: 'room-to-spare', asOf: '2026' },

  // the network
  { layer: 'network', value: '~2 m', what: 'How far a copper signal travels at today\'s speeds before fading into noise. Beyond a rack, everything becomes light.', piece: 'corning-lays-the-glass', asOf: '2026' },
  { layer: 'network', value: '16×', what: 'Fibre a 72-GPU AI rack needs compared with a traditional cloud switch rack, according to Corning.', piece: 'corning-lays-the-glass', asOf: '2026' },
  { layer: 'network', value: '102.4 Tb/s', what: 'Data moved through one Broadcom Tomahawk 6 switch chip, enough for two tiers of switches to join about 128,000 AI chips.', piece: 'broadcom-wins-either-way', asOf: 'June 2025' },
  { layer: 'network', value: '800G → 1.6T', what: 'Data per second through one optical plug, now doubling. Every step needs faster lasers and replaces the plugs, while the fibre stays.', piece: 'lumentum-makes-the-light', asOf: '2026' },

  // memory
  { layer: 'memory', value: '~3×', what: 'The wafer HBM3E uses for each bit stored, against ordinary DDR5 memory, by Micron\'s estimate, restated in December 2025, when it said the ratio only increases with future generations. Every HBM bit is about three ordinary bits not made.', piece: 'micron-three-times-the-wafer', asOf: 'December 2025' },

  // chips and factories
  { layer: 'chips', value: '2–3 + 1–2 yrs', what: 'TSMC\'s time to build a new chip factory, then to bring it to full output. The slowest clock on the chip side.', piece: 'tsmc-says-it-is-the-bottleneck', asOf: 'January 2026' },
  { layer: 'chips', value: '2.25×', what: 'Area of a 300 millimetre wafer against a 200 millimetre one, so each pass through the factory yields more than twice the chips.', piece: 'ti-feeds-the-chip', asOf: '2026' },
  { layer: 'chips', value: '~65 → ~85', what: 'ASML\'s capacity for standard (low NA) EUV machines in 2026, all expected to ship, and its plan for 2027, already close to fully ordered by July 2026. Every leading-edge chip factory needs them.', piece: 'asml-booked-ahead', asOf: 'July 2026' },
  { layer: 'chips', value: '70 → 120 mm', what: 'Ajinomoto\'s estimate of how the base of an advanced chip package grows: about 70 millimetres square with nine wiring layers up to 2023, about 100 with eleven in 2026, about 120 with thirteen from 2031. Each layer needs its own sheet of insulating film.', piece: 'ajinomoto-grows-with-the-package', asOf: 'May 2026' },

  // who runs the capacity
  { layer: 'operators', value: '5 GW vs ~1 GW', what: 'Power Nebius expects to have contracted by the end of 2026, against the 0.8 to 1 gigawatt it expects to have connected.', piece: 'nebius-paid-for-what-is-switched-on', asOf: 'end of 2026, company target' },
];
