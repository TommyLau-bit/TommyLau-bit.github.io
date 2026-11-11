// One real photograph near the top of each journal piece (Tommy, 11 Nov 2026: trial, Chapter 4 first).
// The photo shows the actual place the piece is about, never a generic picture. Every photo is
// public domain or openly licensed on Wikimedia Commons and is credited under it. Files are in
// public/journal-photos/, 900 px wide. A piece with no open photo of its real site has no entry.
// Charts, the map, the descent and the illustrations are drawings and stay as they are.

export type Photo = { src: string; alt: string; caption: string; credit: string; licence: string; page: string; w: number; h: number; pos?: string };

export const JOURNAL_PHOTOS: Record<string, Photo> = {
  'the-queue-not-the-chip': {
    src: '/journal-photos/the-queue-not-the-chip.jpg',
    alt: 'A long road causeway crossing a strait from a city on the near shore to tower blocks on the far shore, with an I love Johor sign in the corner.',
    caption: 'The Johor-Singapore Causeway from the Johor side in August 2024, with Singapore across the strait',
    credit: 'ZKang123', licence: 'CC BY-SA 4.0',
    page: 'https://commons.wikimedia.org/wiki/File:Johor-Singapore_Causeway_20240816_163357.jpg',
    w: 900, h: 675, pos: '50% 75%',
  },
  'america-rations-the-plug': {
    src: '/journal-photos/america-rations-the-plug.jpg',
    alt: 'An aerial view of large, flat-roofed data centre buildings and a substation spread among roads and fields.',
    caption: "Data centres near Ashburn, Loudoun County, Virginia, in Dominion Energy's area, in November 2025",
    credit: 'Theodore Christopher', licence: 'CC0',
    page: 'https://commons.wikimedia.org/wiki/File:Data_centers_in_Ashburn.jpg',
    w: 900, h: 573, pos: '50% 100%',
  },
  'building-your-own-power': {
    src: '/journal-photos/building-your-own-power.jpg',
    alt: 'An aerial view of a large power station among autumn hills, with three cooling towers, three tall chimneys and a switchyard.',
    caption: 'Homer City, Pennsylvania, in October 2024: the closed coal plant whose site is being rebuilt as up to 4,678 MW of gas plant',
    credit: 'Designism', licence: 'CC0',
    page: 'https://commons.wikimedia.org/wiki/File:KBTP_to_KAOO_trip_20241027_12.jpg',
    w: 900, h: 639,
  },
  'nuclear-for-ai': {
    src: '/journal-photos/nuclear-for-ai.jpg',
    alt: 'Four cooling towers beside a river, steam rising from the two nearest, with the reactor buildings between them.',
    caption: 'Crane, formerly Three Mile Island, in March 2019, months before Unit 1 shut; the steaming towers are Unit 1, the idle ones Unit 2',
    credit: 'Constellation Energy', licence: 'CC BY-SA 4.0',
    page: 'https://commons.wikimedia.org/wiki/File:Exelon_Three_Mile_Island_Nuclear_Generating_Station_(cropped).jpg',
    w: 900, h: 600, pos: '50% 55%',
  },
  'microreactors': {
    src: '/journal-photos/microreactors.jpg',
    alt: 'Rows of tall white gas centrifuges standing in a long, dark hall.',
    caption: "Gas centrifuges at the government's enrichment plant at Piketon, Ohio, in 1984; Centrus runs America's one HALEU line at Piketon today",
    credit: 'US Department of Energy', licence: 'Public domain',
    page: 'https://commons.wikimedia.org/wiki/File:Gas_centrifuge_cascade.jpg',
    w: 900, h: 720, pos: '50% 45%',
  },
};
