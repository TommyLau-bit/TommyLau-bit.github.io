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
  { layer: 'grid', value: '1.26 GW of 5.65 GW', what: 'Data centre load Tenaga Nasional supplied across Malaysia in June 2026, against the maximum demand booked by the data centre projects in its system. Johor holds two thirds of Malaysia\'s secured data centre capacity.', piece: 'the-queue-not-the-chip', asOf: 'June 2026' },
  { layer: 'grid', value: '~6 GW', what: 'Low-carbon electricity Singapore aims to import by 2035, all by subsea cable. Every one of the 13 projects approved so far is still conditional.', piece: 'the-queue-not-the-chip', asOf: 'August 2026' },
  { layer: 'grid', value: '3 MW', what: 'Critical IT load from which a Singapore data centre needs an IMDA licence stating the capacity it may run, existing halls included. About 70 are in scope.', piece: 'the-queue-not-the-chip', asOf: 'October 2026' },
  { layer: 'grid', value: '1.25', what: 'The power usage effectiveness Singapore requires to win new data centre capacity. Megawatts go to whoever wastes the fewest of them.', piece: 'the-queue-not-the-chip', asOf: '2026' },
  { layer: 'grid', value: '474 GW', what: 'Requests to connect to ERCOT\'s Texas grid, more than five times the state\'s record peak, about 90 per cent from data centres.', piece: 'america-rations-the-plug', asOf: '3 August 2026' },
  { layer: 'grid', value: '6,831 MW', what: 'How far PJM\'s capacity auction for 2028/2029 fell short of its own reliability requirement. New power stations and upgrades cleared only 525 MW.', piece: 'america-rations-the-plug', asOf: '14 July 2026' },
  { layer: 'grid', value: '50 MW', what: 'The size from which PJM proposes a data centre must ride through faults rather than drop to backup power, existing sites included by 2028.', piece: 'america-rations-the-plug', asOf: '6 October 2026' },
  { layer: 'grid', value: '3.8 GW', what: 'Data centre load in Dominion Energy\'s zone that switched to backup generation after a normally cleared fault on 22 July 2026, the largest load transfer in PJM\'s history.', piece: 'america-rations-the-plug', asOf: '22 July 2026', note: 'Earlier worded as demand that vanished in under a second; PJM times the transfer to the minute, in two stages.' },
  { layer: 'grid', value: '~40% → ~10%', what: 'How far demand for large and medium power transformers in Europe and North America runs ahead of the combined capacity of all makers in the region, by Siemens Energy\'s estimate: about 40 per cent in fiscal 2025 and still about 10 per cent in fiscal 2030.', piece: 'the-equipment-queue', asOf: '20 November 2025' },
  { layer: 'grid', value: '2 to 3 years', what: 'From announcement to planned first output at new transformer plants: Siemens Energy Charlotte (February 2024 for early 2026), Eaton Jonesville (February 2025 for 2027), Hitachi Energy Gallman (September 2026 for 2029).', piece: 'the-equipment-queue', asOf: '15 September 2026' },

  // power on site
  { layer: 'onsite', value: '~6 years', what: 'Gas turbine capacity GE Vernova has under contract, 122 gigawatts, against its output of 20 gigawatts a year. It is now selling places for delivery in 2032.', piece: 'building-your-own-power', asOf: '30 September 2026', note: 'Was 116 GW at 30 June 2026.' },
  { layer: 'onsite', value: '127 vs 39', what: 'Aeroderivative gas turbines GE Vernova took orders for, against those it shipped, in the first nine months of 2026. The fast route to on-site power has its own queue.', piece: 'building-your-own-power', asOf: '30 September 2026' },
  { layer: 'onsite', value: '4,678 MW', what: 'Maximum capacity Pennsylvania permitted for the gas plant on the former Homer City coal site, cleared of NOx review by netting against the old boilers\' cuts.', piece: 'building-your-own-power', asOf: '18 November 2025' },
  { layer: 'onsite', value: '302 → 242', what: 'Rigs drilling in the Permian Basin in early 2025 and early 2026. Gas output rose by about a twelfth over the same year, because the gas comes up oil wells.', piece: 'building-your-own-power', asOf: 'Q1 2026' },
  { layer: 'onsite', value: '53%', what: 'Share of planned 2026 American utility-scale battery additions sited in Texas, 12.9 of 24 gigawatts. Storage is following the computing load.', piece: 'america-rations-the-plug', asOf: 'February 2026', note: 'Counts planned grid-scale battery additions, which also trade; no one publishes the share sited at data centres.' },
  { layer: 'onsite', value: '835 MW', what: 'Output of the Crane reactor at Three Mile Island that Constellation is restarting for Microsoft, enough for a large AI campus running around the clock.', piece: 'nuclear-for-ai', asOf: 'target 2027' },
  { layer: 'onsite', value: '75 MW', what: 'The design output of Oklo\'s first Aurora reactor in Idaho, small enough to sit beside a data centre campus.', piece: 'nuclear-for-ai', asOf: '2026' },
  { layer: 'onsite', value: '900 kg', what: 'HALEU delivered by Centrus\'s sixteen-centrifuge demonstration cascade in Ohio, the only American enrichment line that has made it. Its contracted production finished in mid-June 2026; the next contracted tonne is due by July 2032.', piece: 'nuclear-for-ai', asOf: 'August 2026' },
  { layer: 'onsite', value: '760 MW', what: 'Grid rights FERC let Constellation move to the Crane restart from two Eddystone units it had planned to retire, so Crane need not wait for new lines; a fresh connection was not fully deliverable before the end of 2030.', piece: 'nuclear-for-ai', asOf: '1 June 2026' },
  { layer: 'onsite', value: '26%', what: 'Share of the enrichment bought by US reactor owners in 2025 that came from Russia; every waiver under the ban ends by 1 January 2028.', piece: 'nuclear-for-ai', asOf: 'EIA, August 2026' },

  // power inside the building
  { layer: 'distribution', value: '1 MW', what: 'The draw Nvidia\'s next rack generation, Kyber, is designed for in a single cabinet.', piece: 'powering-the-rack', asOf: 'due 2027' },
  { layer: 'distribution', value: '200 kg', what: 'Copper busbar a one megawatt rack would need at today\'s 54 volts, by Nvidia\'s own figure. The reason the industry is moving to 800 volts.', piece: 'powering-the-rack', asOf: '2026' },
  { layer: 'distribution', value: '18,500 A', what: 'Current needed to deliver one megawatt at 54 volts. At 800 volts it is about 1,250 amps, which is why the rack is moving to 800 VDC.', piece: 'powering-the-rack', asOf: 'physics' },
  { layer: 'distribution', value: '2 MW', what: 'Power per row of racks from Nvidia\'s 800 VDC row power centre, expected in 2027. Its power rack comes first, in the second half of 2026.', piece: 'powering-the-rack', asOf: 'August 2026' },
  { layer: 'distribution', value: '~140 kW', what: 'Peak draw of one current Nvidia rack of 72 GPUs, in the footprint of a fridge.', piece: 'heat-and-water', asOf: '2026' },

  // cooling
  { layer: 'cooling', value: '85–90%', what: 'Share of each AI server\'s heat that leaves through liquid cold plates in a current Jane Street data hall.', piece: 'heat-and-water', asOf: '2026' },
  { layer: 'cooling', value: '~12×', what: 'Water consumed at the power stations supplying American data centres, nearly 800 billion litres, against 66 billion litres consumed on site. Most of a data centre\'s water follows its electricity.', piece: 'heat-and-water', asOf: '2023' },
  { layer: 'cooling', value: '~2 L to ~0', what: 'Water evaporated per kilowatt-hour in a large liquid-cooled hall using a cooling tower, against a dry cooler, in LBNL\'s simulations. PUE stays about 1.1 either way.', piece: 'heat-and-water', asOf: '2024' },
  { layer: 'cooling', value: '9.7 vs 469', what: 'Million gallons of water consumed in 2025 at Google\'s air-cooled Mesa campus, where it judged the source high risk, against its water-cooled campus at The Dalles, Oregon.', piece: 'heat-and-water', asOf: '2025' },

  // the network
  { layer: 'network', value: '102.4 Tb/s', what: 'Data moved through one Broadcom Tomahawk 6 switch chip, enough for two tiers of switches to join more than 100,000 AI chips, by Broadcom\'s own figure.', piece: 'ten-thousand-chips-one-thought', asOf: 'June 2025' },
  { layer: 'network', value: '800G → 1.6T', what: 'Data per second through one optical plug, now doubling. Every step needs faster lasers and replaces the plugs, while the fibre stays.', piece: 'ten-thousand-chips-one-thought', asOf: '2026' },
  { layer: 'network', value: '<3%', what: 'Share of a Google TPU v4 pod\'s power taken by its whole optical switching layer, mirror switches, plugs and fibre included, for 4,096 chips. Google\'s figure for cost is under 5%.', piece: 'ten-thousand-chips-one-thought', asOf: '2023' },
  { layer: 'network', value: '~5 microseconds per km', what: 'How long light takes to cover each kilometre of glass fibre. Across the roughly 1,000 km between Microsoft\'s Fairwater sites that is at least 5 ms one way.', piece: 'ten-thousand-chips-one-thought', asOf: '2026' },
  { layer: 'network', value: '15×', what: 'Rise in co-packaged optical engine capacity SPIL targets by mid-2027, with another doubling by the end of 2028, according to Nvidia. A target, not built capacity.', piece: 'ten-thousand-chips-one-thought', asOf: 'October 2026' },

  // memory
  { layer: 'memory', value: '~3×', what: 'The wafer HBM3E uses for each bit stored, against ordinary DDR5 memory, by Micron\'s estimate, restated in December 2025, when it said the ratio only increases with future generations. Every HBM bit is about three ordinary bits not made.', piece: 'the-chip-supply-chain', asOf: 'December 2025' },
  { layer: 'memory', value: '+26% on flat units', what: 'How much more hard drive storage Seagate shipped in a year on a similar number of drives. Supply grows by packing each drive, not by making more.', piece: 'the-chip-supply-chain', asOf: 'December quarter 2025' },

  // chips and factories
  { layer: 'chips', value: '2–3 + 1–2 yrs', what: 'TSMC\'s time to build a new chip factory, then to bring it to full output. The slowest clock on the chip side.', piece: 'the-chip-supply-chain', asOf: 'January 2026' },
  { layer: 'chips', value: '~65 → ~85', what: 'ASML\'s capacity for standard (low NA) EUV machines in 2026, all expected to ship, and its plan for 2027, already close to fully ordered by July 2026. Every leading-edge chip factory needs them.', piece: 'the-chip-supply-chain', asOf: 'July 2026' },
  { layer: 'chips', value: '70 → 120 mm', what: 'Ajinomoto\'s estimate of how the base of an advanced chip package grows: about 70 millimetres square with nine wiring layers up to 2023, about 100 with eleven in 2026, about 120 with thirteen from 2031. Each layer needs its own sheet of insulating film.', piece: 'the-chip-supply-chain', asOf: 'May 2026' },
  { layer: 'chips', value: '2029 and 2030', what: 'Years for which some of ASML\'s customers already want to order EUV machines, as ASML said its planned supply for 2027 and 2028 will not fully meet demand. ASML is the only maker.', piece: 'the-chip-supply-chain', asOf: 'October 2026' },
  { layer: 'chips', value: 'through 2028', what: 'How far ahead Seagate has allocated the vast majority of its data centre nearline drive supply, with some cloud agreements to 2030. It grows supply by more terabytes per drive, not more drives.', piece: 'the-chip-supply-chain', asOf: 'October 2026' },
  { layer: 'chips', value: '2.25×', what: 'Area of a 300 millimetre wafer against a 200 millimetre one, so each pass through the factory yields more than twice the chips.', piece: 'powering-the-rack', asOf: '2026' },

  // who runs the capacity
  { layer: 'operators', value: '5 GW vs ~1 GW', what: 'Power Nebius expects to have contracted by the end of 2026, against the 0.8 to 1 gigawatt it expects to have connected.', piece: 'contracted-energised-running', asOf: 'end of 2026, company target' },
  { layer: 'operators', value: '6 of 8', what: 'Buildings at the Abilene, Texas AI campus Oracle said it had delivered to its customer, 618 MW and about three quarters of capacity, more than two years after work began in June 2024. From Oracle\'s results call, as transcribed.', piece: 'contracted-energised-running', asOf: '10 September 2026' },
  { layer: 'operators', value: '~170 MW', what: 'Active power at Nebius at the end of 2025, power drawn by running computers, against more than 2 GW contracted by February 2026.', piece: 'contracted-energised-running', asOf: 'end of 2025' },
];
