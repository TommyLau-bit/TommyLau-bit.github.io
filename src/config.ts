// ── ONE PLACE TO CHANGE THE NAME, TAGLINE AND LINKS ──────────────────────────
export const SITE = {
  name: 'The Physical Layer',
  tagline: 'AI and energy infrastructure, explained plainly.',
  description:
    'A journal on the physical constraints behind the AI buildout: power, grid connection, data centres, cooling and the supply chains that gate them. Written to be understood by anyone.',
  author: 'Tommy Lau',
  email: 'tommyllk2003@gmail.com',
  linkedin: 'https://www.linkedin.com/in/tommy-lau-170364253',
  linkedinPage: 'https://www.linkedin.com/company/143897682/',
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
export const PATH_REVIEWED = 'October 2026';

export const READING_PATH = [
  {
    stage: 'Getting a connection',
    note: 'Why the plug, not the chip, decides who gets to build, and what builders do when the grid cannot wait.',
    ids: ['the-queue-not-the-chip', 'building-your-own-power'],
  },
  {
    stage: 'Getting the power in and the heat out',
    note: 'From the power room down to the rack, then every watt back out as heat, by liquid, air or water.',
    ids: ['powering-the-rack', 'heat-and-water'],
  },
  {
    stage: 'Keeping the chips fed',
    note: 'The wiring between chips, and the few factories that make the chips and their memory.',
    ids: ['ten-thousand-chips-one-thought', 'the-chip-supply-chain'],
  },
];

export const READING_ORDER = READING_PATH.flatMap((s) => s.ids).slice(0, PATH_MAX);

export const OG_VERSION = 'v9';
