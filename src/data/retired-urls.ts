// Old URLs that must keep resolving after their pages were removed. Each one redirects to the homepage.
// Research notes (33, off the site since 6 Nov 2026; source in research-build/archive/research-page-2026-11-06/):
// served at /research/<slug>/ and the older /calls/<slug>/.
export const NOTE_SLUGS = [
  'ajinomoto', 'asml', 'bloom-energy', 'broadcom', 'caterpillar', 'clp-holdings', 'coherent',
  'constellation', 'corning', 'eaton', 'entergy', 'ge-vernova', 'hitachi', 'infineon',
  'kinder-morgan', 'lumentum', 'marvell', 'micron', 'mitsubishi-heavy', 'nebius', 'nvidia', 'oklo',
  'samsung-electronics', 'schneider-electric', 'seagate', 'siemens-energy', 'sk-hynix', 'spacex',
  'texas-instruments', 'tsmc', 'vertiv', 'wartsila', 'williams',
];

// Company pages (removed 6 Nov 2026), frozen at the 128 slugs that were live: /companies/<slug>/.
export const COMPANY_SLUGS = [
  'aalo', 'abb', 'airtrunk', 'ajinomoto', 'alphabet', 'amazon', 'american-electric-power',
  'antares', 'arista', 'asml', 'asp-isotopes', 'bloom-energy', 'bridge-data-centres', 'broadcom',
  'bwxt', 'bytedance', 'caterpillar', 'centrus-energy', 'ciena', 'cisco', 'cleveland-cliffs',
  'clp-power', 'coherent', 'consolidated-precision-products', 'constellation', 'coreweave',
  'corning', 'crusoe', 'cummins', 'dayone', 'digital-realty', 'dominion-energy', 'doncasters',
  'duke-energy', 'eaton', 'emerald-ai', 'energy-transfer', 'entergy', 'eoptolink', 'eqt',
  'equinix', 'ercot', 'fabrinet', 'ferc', 'first-solar', 'fujikura', 'ge-vernova',
  'ge-vernova-hitachi', 'generac', 'general-atomics', 'general-matter', 'google',
  'hd-hyundai-electric', 'hitachi-energy', 'holtec', 'homer-city-generation', 'howmet-aerospace',
  'hubbell', 'hyosung-heavy-industries', 'ibiden', 'innolight', 'intel', 'intersect',
  'kairos-power', 'keppel-data-centres', 'kinder-morgan', 'legrand', 'ls-electric', 'lumentum',
  'marvell', 'maschinenfabrik-reinhausen', 'meta', 'micron', 'microsoft', 'mitsubishi-heavy',
  'nebius', 'nerc', 'nexans', 'nextera-energy', 'nippon-steel', 'nkt', 'nvent', 'nvidia', 'oklo',
  'oncor', 'oracle', 'orano', 'pjm', 'powell-industries', 'precision-castparts',
  'princeton-digital-group', 'propetro', 'prysmian', 'radiant', 'range-intelligent-computing',
  'rolls-royce', 'samsung', 'schneider-electric', 'seagate', 'siemens', 'siemens-energy',
  'sk-hynix', 'solaris-energy-infrastructure', 'sp-group', 'spil', 'standard-nuclear', 'stt-gdc',
  'talen-energy', 'tenaga-nasional', 'terrapower', 'tesla', 'tesla-energy', 'toshiba', 'trench',
  'trumpf', 'unimicron', 'urenco', 'us-air-force', 'us-army', 'vertiv', 'vistra', 'wartsila',
  'western-digital', 'westinghouse', 'williams', 'x-energy', 'ytl-power', 'zeiss',
];
