// ── The map of the stack ─────────────────────────────────────────────────────
//
// The physical layers of an AI data centre, from the grid connection inward to the
// rack, plus orbit. Only layers the journal covers (Tommy, 8 Nov 2026: no chip,
// memory or network layers; semiconductors are not this site's field).
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
    constraint: 'The wait for a connection now runs to years, and the grid decides who is served first.',
    pieces: ['the-queue-not-the-chip', 'america-rations-the-plug'],
  },
  {
    id: 'equipment',
    name: 'Transformers and switchgear',
    kind: 'energy',
    what: 'Transformers step the voltage down at the grid and switchgear routes and protects it inside the fence; a handful of makers build them.',
    constraint: 'The makers add factories only as fast as signed orders justify, so the wait is kept, not cleared.',
    pieces: ['the-equipment-queue'],
  },
  {
    id: 'onsite',
    name: 'Power on site',
    kind: 'energy',
    what: 'Gas turbines, engines, fuel cells and batteries make or store power beside the building.',
    constraint: 'Skipping the grid queue means joining the turbine makers\' queue instead.',
    pieces: ['building-your-own-power'],
  },
  {
    id: 'nuclear',
    name: 'Nuclear power',
    kind: 'energy',
    what: 'Existing reactors, restarted or upgraded, sell power to AI campuses first; new and micro reactors follow.',
    constraint: 'Most new reactors need a richer fuel, HALEU, that America makes on one demonstration line.',
    pieces: ['nuclear-for-ai', 'microreactors'],
  },
  {
    id: 'distribution',
    name: 'Power inside the building',
    kind: 'energy',
    what: 'Power is stepped down, backed up and carried to each rack, then down to below one volt at the chip.',
    constraint: 'At a megawatt per rack, the copper needed at today\'s low voltage stops fitting.',
    pieces: ['powering-the-rack'],
  },
  {
    id: 'cooling',
    name: 'Cooling',
    kind: 'energy',
    what: 'Almost every watt that goes into a chip comes back out as heat, and liquid now carries most of it away.',
    constraint: 'A typical rack drew about 7.5 kilowatts in 2025; Nvidia\'s GB200 rack draws about 120, too much heat for air to carry.',
    pieces: ['heat-and-water'],
  },
  {
    id: 'orbit',
    name: 'Data centres in orbit',
    kind: 'energy',
    what: 'Satellites in near-constant sunlight run AI chips on solar power and shed the heat by radiating it into cold space.',
    constraint: 'Every kilogram of radiator and solar panel must be launched, so the weight of each kilowatt decides the cost.',
    pieces: ['data-centres-in-space'],
  },
];

export const layerOf = (id: string) => STACK.findLast((l) => l.pieces.includes(id));
