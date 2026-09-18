// ── ONE PLACE TO CHANGE THE NAME, TAGLINE AND LINKS ──────────────────────────
export const SITE = {
  name: 'The Physical Layer',
  tagline: 'AI and energy infrastructure, explained plainly.',
  description:
    'A journal on the physical constraints behind the AI buildout: power, grid connection, data centres, cooling and the supply chains that gate them. Written to be understood by anyone.',
  author: 'Tommy Lau',
  email: 'tommyllk2003@gmail.com',
  linkedin: 'https://www.linkedin.com/in/tommy-lau-170364253',
  url: 'https://thephysicallayer.fyi',
  locale: 'en-GB',
};

// ── The on-ramp for a new reader. NOT an index of the site. ──────────────────
//
// THE RULE: you do not touch this when you publish. Write whatever you want,
// push it, and it appears on the home page in date order. This list exists only
// to answer "where does a stranger start", and it is capped so it cannot creep
// into a table of contents that you owe something to.
//
// Revisit it when you feel like it, twice a year at most, by asking one
// question: if someone landed here today, which pieces get them oriented
// fastest? Swap one out rather than adding a seventh. Then update REVIEWED.
//
// Anything beyond PATH_MAX is ignored by /start.
export const PATH_MAX = 6;
export const PATH_REVIEWED = 'September 2026';

export const READING_PATH = [
  {
    stage: 'What the building is actually doing',
    note: 'One piece. Read it and the rest of the site makes sense.',
    ids: ['the-two-seconds-after-you-hit-send'],
  },
  {
    stage: 'Getting the power in',
    note: 'From the grid connection down to the busbar inside the cabinet.',
    ids: ['the-queue-not-the-chip', 'the-rack-runs-out-of-copper'],
  },
  {
    stage: 'Getting the heat back out',
    note: 'Every watt that goes in comes out as heat. Somebody has to carry it away.',
    ids: ['cooling-is-half-the-job'],
  },
  {
    stage: 'Keeping the chips fed',
    note: 'The wiring between chips and the memory beside them decide whether the silicon earns its keep.',
    ids: ['ten-thousand-chips-one-thought', 'the-countertop-is-the-bottleneck'],
  },
];

export const READING_ORDER = READING_PATH.flatMap((s) => s.ids).slice(0, PATH_MAX);

export const OG_VERSION = 'v3';
