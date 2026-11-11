// One real photograph near the top of each journal piece (Tommy, 11 Nov 2026: trial, Chapter 4 first).
// The photo shows the machine or the work the piece is about, not scenery (Tommy, 12 Nov 2026: America and own
// power swapped to a grid control room and a gas turbine; Johor keeps the Causeway, as no open photo of Johor's
// grid or data centres exists); a real
// photo of the machine the piece is about (Tommy, 11 Nov 2026: transformer for the equipment queue, solar farm for solar). Every photo is
// public domain or openly licensed on Wikimedia Commons and is credited under it. Files are in
// public/journal-photos/, 900 px wide.
// Charts, the map, the descent and the illustrations are drawings and stay as they are.

// Licence deeds for the attribution-required licences (TASL: title, author, source, licence, plus a note
// that the file was resized). CC0 and public domain need no link.
export const LICENCE_URL: Record<string, string> = {
  'CC BY 2.0': 'https://creativecommons.org/licenses/by/2.0/',
  'CC BY 3.0': 'https://creativecommons.org/licenses/by/3.0/',
  'CC BY-SA 3.0': 'https://creativecommons.org/licenses/by-sa/3.0/',
  'CC BY-SA 4.0': 'https://creativecommons.org/licenses/by-sa/4.0/',
};

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
    alt: 'A grid dispatcher on the phone at a desk of screens, beneath a wall display of a load curve and a map of Texas.',
    caption: "A dispatcher in the control room of ERCOT, Texas's grid operator, in 2012",
    credit: 'Dpysh w', licence: 'CC BY 3.0',
    page: 'https://commons.wikimedia.org/wiki/File:ERCOTOperator_2.jpg',
    w: 900, h: 599, pos: '50% 60%',
  },
  'building-your-own-power': {
    src: '/journal-photos/building-your-own-power.jpg',
    alt: 'The core of a GE gas turbine on a maintenance stand at a gas plant, with a crane, an air intake and exhaust stacks behind it.',
    caption: 'The core of a GE LMS100 gas turbine on a maintenance stand at a gas plant, in 2017',
    credit: 'Hotdiggity46290', licence: 'CC BY-SA 4.0',
    page: 'https://commons.wikimedia.org/wiki/File:GE_LMS100.jpg',
    w: 900, h: 675, pos: '50% 65%',
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
  'the-equipment-queue': {
    src: '/journal-photos/the-equipment-queue.jpg',
    alt: 'A large high-voltage transformer in a substation, with insulators and lines above it.',
    caption: 'A large high-voltage transformer in a substation, the machine at the front of the equipment queue',
    credit: 'Novoklimov', licence: 'CC0',
    page: 'https://commons.wikimedia.org/wiki/File:High-voltage_transformer_750_kV_%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%BE%D1%80_750_%D0%BA%D0%92.jpg',
    w: 900, h: 675,
  },
  'solar-and-batteries': {
    src: '/journal-photos/solar-and-batteries.jpg',
    alt: 'Rows of solar panels stretching across a valley under a cloudy sky.',
    caption: 'Topaz Solar Farm in California, a utility-scale solar park of the kind the piece is about',
    credit: 'Sarah Swenty, US Fish and Wildlife Service', licence: 'Public domain',
    page: 'https://commons.wikimedia.org/wiki/File:Solar_Panels_at_Topaz_Solar_2_(8159035028).jpg',
    w: 900, h: 597, pos: '50% 70%',
  },
};
