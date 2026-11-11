// One real photograph near the top of each journal piece (Tommy, 11 Nov 2026: trial, Chapter 4 first).
// The photo shows the actual place the piece is about, never a generic picture. Every photo is
// public domain or openly licensed on Wikimedia Commons and is credited under it. Files are in
// public/journal-photos/, 900 px wide. A piece with no open photo of its real site has no entry.
// Charts, the map, the descent and the illustrations are drawings and stay as they are.

export type Photo = { src: string; alt: string; caption: string; credit: string; licence: string; page: string; w: number; h: number };

export const JOURNAL_PHOTOS: Record<string, Photo> = {
  'building-your-own-power': {
    src: '/journal-photos/building-your-own-power.jpg',
    alt: 'An aerial view of a large power station among autumn hills, with three cooling towers, three tall chimneys and a switchyard.',
    caption: 'Homer City, Pennsylvania, in October 2024: the closed coal plant whose site is being rebuilt as up to 4,678 MW of gas plant',
    credit: 'Designism', licence: 'CC0',
    page: 'https://commons.wikimedia.org/wiki/File:KBTP_to_KAOO_trip_20241027_12.jpg',
    w: 900, h: 639,
  },
};
