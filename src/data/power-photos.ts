// Photos for the Power roster cards (Tommy, 11 Nov 2026: real photos, not drawings).
// Every photo is public domain or openly licensed on Wikimedia Commons and is credited
// on its card. No company press photos except those a company released under an open
// licence itself (Bloom Energy, Constellation). Files are in public/power/, 900 px wide.
// The microreactor has no photo: none has run yet, so its card stays locked.

export type Photo = { src: string; alt: string; caption: string; credit: string; licence: string; page: string; pos?: string };

export const PHOTOS: Record<string, Photo> = {
  grid: { src: '/power/grid.jpg', alt: 'A large high-voltage transformer in a substation, with insulators and lines above it.',
    caption: 'A 750 kV substation transformer', credit: 'Novoklimov', licence: 'CC0',
    page: 'https://commons.wikimedia.org/wiki/File:High-voltage_transformer_750_kV_%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%BE%D1%80_750_%D0%BA%D0%92.jpg' },
  'heavy-sc': { src: '/power/heavy-sc.jpg', alt: 'A worker in a hard hat beside the bladed rotor of a large gas turbine being assembled.',
    caption: 'Assembling the rotor of a Siemens SGT5-4000F', credit: 'Siemens Pressebild', licence: 'CC BY-SA 3.0',
    page: 'https://commons.wikimedia.org/wiki/File:Gasturbine_Montage01.jpg', pos: '50% 40%' },
  ccgt: { src: '/power/ccgt.jpg', alt: 'The boiler structures and stack of a combined-cycle gas plant against a blue sky.',
    caption: 'Magnolia Power Plant, Burbank, California', credit: 'Alexis Doine', licence: 'CC0',
    page: 'https://commons.wikimedia.org/wiki/File:Magnolia_Power_Plant_(April_2026).jpg', pos: '50% 45%' },
  aero: { src: '/power/aero.jpg', alt: 'A GE LM6000 aeroderivative gas turbine in its enclosure, with pipes and wiring around it.',
    caption: 'A GE LM6000 at work in Iraq', credit: 'Pro-Per Energy Services', licence: 'CC BY-SA 4.0',
    page: 'https://commons.wikimedia.org/wiki/File:Gas_Turbine_4.jpg' },
  recip: { src: '/power/recip.jpg', alt: 'A large green 20-cylinder V gas engine in a power plant hall.',
    caption: 'A 5 MW, 20-cylinder Jenbacher gas engine', credit: 'Benedikt Schneider', licence: 'CC BY-SA 3.0',
    page: 'https://commons.wikimedia.org/wiki/File:Gasmotor.JPG' },
  fuelcell: { src: '/power/fuelcell.jpg', alt: 'A row of Bloom Energy fuel cell servers, grey cabinets lit from below.',
    caption: 'Bloom Energy Servers', credit: 'Bloom Energy', licence: 'CC BY 2.0',
    page: 'https://commons.wikimedia.org/wiki/File:Bloom_Energy_Servers.jpg' },
  fleet: { src: '/power/fleet.jpg', alt: 'A gas turbine generating unit mounted on road trailers, with its crew standing beside it.',
    caption: 'A Siemens SGT-A45 turbine on trailers, Bayat', credit: 'Mahbubehp', licence: 'CC BY-SA 4.0',
    page: 'https://commons.wikimedia.org/wiki/File:Bayat_Power_Plant.jpg' },
  solar: { src: '/power/solar.jpg', alt: 'Rows of solar panels stretching across a valley under a cloudy sky.',
    caption: 'Topaz Solar Farm, California', credit: 'Sarah Swenty, US Fish and Wildlife Service', licence: 'Public domain',
    page: 'https://commons.wikimedia.org/wiki/File:Solar_Panels_at_Topaz_Solar_2_(8159035028).jpg', pos: '50% 70%' },
  battery: { src: '/power/battery.jpg', alt: 'White battery storage containers on a gravel pad in the countryside.',
    caption: 'A 5 MW battery in containers, Switzerland', credit: 'Kecko', licence: 'CC BY 2.0',
    page: 'https://commons.wikimedia.org/wiki/File:Tesvolt_battery_energy_storage_system_Rheineck.jpg' },
  restart: { src: '/power/restart.jpg', alt: 'Cooling towers at Three Mile Island, now Crane, beside a river.',
    caption: 'Crane, formerly Three Mile Island', credit: 'Constellation Energy', licence: 'CC BY-SA 4.0',
    page: 'https://commons.wikimedia.org/wiki/File:Exelon_Three_Mile_Island_Nuclear_Generating_Station_(cropped).jpg' },
  uprate: { src: '/power/uprate.jpg', alt: 'A black and white photograph of the Palisades nuclear plant, its round containment beside the turbine building.',
    caption: 'Palisades, Michigan, an older DOE photograph', credit: 'US Department of Energy', licence: 'Public domain',
    page: 'https://commons.wikimedia.org/wiki/File:HD.6B.283_(11842918066).jpg' },
  newreactor: { src: '/power/newreactor.jpg', alt: 'An aerial view of the Vogtle nuclear plant, with the construction site of two new reactors beside the old ones.',
    caption: 'Vogtle 3 and 4 under construction, the last new US reactors', credit: 'Charles C Watson Jr', licence: 'CC BY-SA 3.0',
    page: 'https://commons.wikimedia.org/wiki/File:Construction_at_Vogtle_Nuclear_Plant.jpg' },
};
