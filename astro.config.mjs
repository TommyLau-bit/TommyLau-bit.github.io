import { defineConfig } from 'astro/config';
import { existsSync } from 'node:fs';
import sitemap from '@astrojs/sitemap';
import { SITE } from './src/config.ts';

// ── Redirects for merged pieces (CLAUDE.md, "Merging keeps the record") ──────
// Every old URL of a piece merged into a deep piece points at its anchored
// section there. With static output Astro writes /journal/<old>/index.html as
// a meta-refresh page, #fragment included. Add a piece's entries at merge time
// with `python3 brand/add-redirects.py <sidecar>`, and delete the old .md from
// src/content/journal/ in the same change: a redirect and a live page cannot
// share a path. Keys have no trailing slash; the old URL with one still lands.
const REDIRECTS = {
  // the-queue-not-the-chip
  '/journal/johor-plugs-in-before-it-fills': '/journal/the-queue-not-the-chip/#johor-plugs-in-before-it-fills',
  '/journal/johor-waits-on-the-treatment-plant': '/journal/the-queue-not-the-chip/#johor-waits-on-the-treatment-plant',
  '/journal/malaysia-keeps-the-wires-shared': '/journal/the-queue-not-the-chip/#malaysia-keeps-the-wires-shared',
  '/journal/singapore-cannot-wait-for-the-cable': '/journal/the-queue-not-the-chip/#singapore-cannot-wait-for-the-cable',
  '/journal/singapore-licenses-the-old-halls': '/journal/the-queue-not-the-chip/#singapore-licenses-the-old-halls',
  '/journal/the-part-money-cannot-hurry': '/journal/the-queue-not-the-chip/#the-part-money-cannot-hurry',
  '/journal/two-governments-one-confession': '/journal/the-queue-not-the-chip/#two-governments-one-confession',
  // america-rations-the-plug
  '/journal/california-still-shifts-the-sun': '/journal/america-rations-the-plug/#california-still-shifts-the-sun',
  '/journal/ercot-rations-the-plug': '/journal/america-rations-the-plug/#ercot-rations-the-plug',
  '/journal/ferc-asks-for-a-softer-plug': '/journal/america-rations-the-plug/#ferc-asks-for-a-softer-plug',
  '/journal/google-lets-the-grid-slow-its-chips': '/journal/america-rations-the-plug/#google-lets-the-grid-slow-its-chips',
  '/journal/pjm-sends-the-bill': '/journal/america-rations-the-plug/#pjm-sends-the-bill',
  '/journal/the-power-it-drops': '/journal/america-rations-the-plug/#the-power-it-drops',
  '/journal/virginia-bills-the-empty-site': '/journal/america-rations-the-plug/#virginia-bills-the-empty-site',
  '/journal/what-the-battery-is-really-for': '/journal/america-rations-the-plug/#what-the-battery-is-really-for',
  // the-equipment-queue
  '/journal/eaton-order-book-outruns-it': '/journal/the-equipment-queue/#eaton-order-book-outruns-it',
  '/journal/hitachi-energy-plans-the-queue': '/journal/the-equipment-queue/#hitachi-energy-plans-the-queue',
  '/journal/schneider-sells-the-finished-system': '/journal/the-equipment-queue/#schneider-sells-the-finished-system',
  '/journal/siemens-energy-measures-the-shortage': '/journal/the-equipment-queue/#siemens-energy-measures-the-shortage',
  // building-your-own-power
  '/journal/crusoe-borrows-the-jet-engine': '/journal/building-your-own-power/#crusoe-borrows-the-jet-engine',
  '/journal/ge-vernova-sells-the-wait': '/journal/building-your-own-power/#ge-vernova-sells-the-wait',
  '/journal/golden-pass-joins-the-gas-queue': '/journal/building-your-own-power/#golden-pass-joins-the-gas-queue',
  '/journal/homer-city-inherits-the-air': '/journal/building-your-own-power/#homer-city-inherits-the-air',
  '/journal/howmet-casts-the-queue': '/journal/building-your-own-power/#howmet-casts-the-queue',
  '/journal/hyperion-the-plant-outlasts-the-lease': '/journal/building-your-own-power/#hyperion-the-plant-outlasts-the-lease',
  '/journal/permian-gas-follows-the-oil-rig': '/journal/building-your-own-power/#permian-gas-follows-the-oil-rig',
  '/journal/the-product-is-time': '/journal/building-your-own-power/#the-product-is-time',
  '/journal/the-way-out-has-its-own-queue': '/journal/building-your-own-power/#the-way-out-has-its-own-queue',
  // nuclear-for-ai
  '/journal/constellation-restarts-the-reactor': '/journal/nuclear-for-ai/#constellation-restarts-the-reactor',
  '/journal/constellation-squeezes-the-reactors': '/journal/nuclear-for-ai/#constellation-squeezes-the-reactors',
  '/journal/darlington-builds-on-the-old-plug': '/journal/nuclear-for-ai/#darlington-builds-on-the-old-plug',
  '/journal/eunice-cannot-fill-the-gap': '/journal/nuclear-for-ai/#eunice-cannot-fill-the-gap',
  '/journal/kairos-signs-before-it-switches-on': '/journal/nuclear-for-ai/#kairos-signs-before-it-switches-on',
  '/journal/oklo-sells-the-electricity': '/journal/nuclear-for-ai/#oklo-sells-the-electricity',
  '/journal/palisades-waits-on-the-reactor': '/journal/nuclear-for-ai/#palisades-waits-on-the-reactor',
  '/journal/terrapower-waits-on-the-fuel': '/journal/nuclear-for-ai/#terrapower-waits-on-the-fuel',
  // powering-the-rack
  '/journal/every-megawatt-got-harder': '/journal/powering-the-rack/#every-megawatt-got-harder',
  '/journal/the-rack-runs-out-of-copper': '/journal/powering-the-rack/#the-rack-runs-out-of-copper',
  '/journal/ti-feeds-the-chip': '/journal/powering-the-rack/#ti-feeds-the-chip',
  // heat-and-water
  '/journal/cooling-is-half-the-job': '/journal/heat-and-water/#cooling-is-half-the-job',
  '/journal/room-to-spare': '/journal/heat-and-water/#room-to-spare',
  '/journal/water-is-a-siting-problem': '/journal/heat-and-water/#water-is-a-siting-problem',
  // ten-thousand-chips-one-thought
  '/journal/broadcom-wins-either-way': '/journal/ten-thousand-chips-one-thought/#broadcom-wins-either-way',
  '/journal/corning-lays-the-glass': '/journal/ten-thousand-chips-one-thought/#corning-lays-the-glass',
  '/journal/fairwater-spans-two-states': '/journal/ten-thousand-chips-one-thought/#fairwater-spans-two-states',
  '/journal/google-steers-the-light': '/journal/ten-thousand-chips-one-thought/#google-steers-the-light',
  '/journal/lumentum-makes-the-light': '/journal/ten-thousand-chips-one-thought/#lumentum-makes-the-light',
  '/journal/marvell-collects-the-toll': '/journal/ten-thousand-chips-one-thought/#marvell-collects-the-toll',
  '/journal/the-optics-you-cannot-unplug': '/journal/ten-thousand-chips-one-thought/#the-optics-you-cannot-unplug',
  // the-chip-supply-chain
  '/journal/ajinomoto-grows-with-the-package': '/journal/the-chip-supply-chain/#ajinomoto-grows-with-the-package',
  '/journal/asml-booked-ahead': '/journal/the-chip-supply-chain/#asml-booked-ahead',
  '/journal/micron-three-times-the-wafer': '/journal/the-chip-supply-chain/#micron-three-times-the-wafer',
  '/journal/nobody-makes-a-b200-alone': '/journal/the-chip-supply-chain/#nobody-makes-a-b200-alone',
  '/journal/seagate-sells-the-terabyte': '/journal/the-chip-supply-chain/#seagate-sells-the-terabyte',
  '/journal/the-countertop-is-the-bottleneck': '/journal/the-chip-supply-chain/#the-countertop-is-the-bottleneck',
  '/journal/the-two-seconds-after-you-hit-send': '/journal/the-chip-supply-chain/#the-two-seconds-after-you-hit-send',
  '/journal/tsmc-says-it-is-the-bottleneck': '/journal/the-chip-supply-chain/#tsmc-says-it-is-the-bottleneck',
  // contracted-energised-running
  '/journal/abilene-switched-on-in-stages': '/journal/contracted-energised-running/#abilene-switched-on-in-stages',
  '/journal/nebius-paid-for-what-is-switched-on': '/journal/contracted-energised-running/#nebius-paid-for-what-is-switched-on',
  '/journal/power-first-chips-last': '/journal/contracted-energised-running/#power-first-chips-last',
};

// A redirect must never shadow a live piece: fail the build if the old .md is still there.
for (const from of Object.keys(REDIRECTS)) {
  const m = from.match(/^\/journal\/([a-z0-9-]+)\/?$/);
  if (m && existsSync(new URL(`./src/content/journal/${m[1]}.md`, import.meta.url)))
    throw new Error(`Redirect ${from} would shadow src/content/journal/${m[1]}.md: delete the old piece (its original is archived in research-build/archive-pieces/) or drop the redirect.`);
}

export default defineConfig({
  site: SITE.url,
  redirects: REDIRECTS,
  integrations: [sitemap({ filter: (page) => !page.includes('/topics/') })],
  markdown: { shikiConfig: { theme: 'github-light' } },
});
