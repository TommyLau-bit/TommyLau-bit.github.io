// ── The map of the stack ─────────────────────────────────────────────────────
//
// The physical layers the journal covers, in the order of the story: the grid
// connection, its equipment, power made beside the site, then reactors (Tommy,
// 9 Nov 2026: one sector, power for AI data centres; no rack, cooling, chip or orbit layers).
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
    name: 'Power beside the site',
    kind: 'energy',
    what: 'Gas turbines, engines and fuel cells make power beside the building; solar farms and batteries are the fastest to build.',
    constraint: 'Gas joins the turbine makers\' queue, and solar and batteries cannot carry a winter night.',
    pieces: ['building-your-own-power', 'solar-and-batteries'],
  },
  {
    id: 'nuclear',
    name: 'Nuclear power',
    kind: 'energy',
    what: 'Existing reactors, restarted or upgraded, sell power to AI campuses first; new and micro reactors follow.',
    constraint: 'Most new reactors need a richer fuel, HALEU, that America makes on one demonstration line.',
    pieces: ['nuclear-for-ai', 'microreactors'],
  },
];

export const layerOf = (id: string) => STACK.findLast((l) => l.pieces.includes(id));

// ── The story ───────────────────────────────────────────────────────────────
// One question, seven chapters (Tommy, 9 Nov 2026): where does the next gigawatt
// for AI come from, and why is every answer a queue? Each chapter hands off to the
// next with a reason already in the pieces; `next` is that handoff, shown under the
// chapter on the homepage and at the end of the piece.
export type Chapter = { slug: string; name: string; next: string };
export const CHAPTERS: Chapter[] = [
  { slug: 'the-queue-not-the-chip', name: 'Johor and Singapore', next: 'Malaysia is not alone. In America, the grid now decides who waits, who is cut first and who pays.' },
  { slug: 'america-rations-the-plug', name: 'America rations the plug', next: 'The grid cannot simply build its way out, because its machines come from a few factories.' },
  { slug: 'the-equipment-queue', name: 'The equipment queue', next: 'So builders skip the grid and make their own power, and meet the turbine makers\' queue instead.' },
  { slug: 'building-your-own-power', name: 'Building your own power', next: 'GE Vernova is now selling heavy gas turbine places for 2032. Why not build solar and batteries, the fastest power there is?' },
  { slug: 'solar-and-batteries', name: 'Solar and batteries', next: 'They are fast, but the grid counts them as a fraction of a firm megawatt, so buyers turn to power that runs all year: reactors.' },
  { slug: 'nuclear-for-ai', name: 'Nuclear for AI', next: 'Old reactors go first. The new ones are small, and their fuel is the gate.' },
  { slug: 'microreactors', name: 'Microreactors', next: 'The reactor is the easy part. Every route to the next gigawatt for AI runs through a queue.' },
];
export const chapterOf = (id: string) => { const i = CHAPTERS.findIndex((c) => c.slug === id); return i < 0 ? undefined : { ...CHAPTERS[i], n: i + 1, prev: CHAPTERS[i - 1], following: CHAPTERS[i + 1] }; };
