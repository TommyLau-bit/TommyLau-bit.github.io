// ── Power roster: how a rating is worked out ────────────────────────────────
// Five ratings (Permitting ease and OVR cut: Tommy, 11 Nov 2026). Every rating is a formula of one sourced number on the card (src/data/power.ts).
// No rating is typed in by hand. A number that could not be sourced is null, and
// its rating is then n/a. Each rating is clamped to 25..99; a range uses its midpoint.

export type Num = number | [number, number] | null;
export type Stat = {
  value: Num;          // the number the rating reads (null = n/a)
  display: string;     // as shown on the card, with its unit
  basis?: string;      // what exactly it measures
  source?: string;     // publisher and document
  url?: string;
  date?: string;
  claim?: string;      // set when the number is a company's own claim, not a measured project: flagged on the card
};

export const mid = (v: Num): number | null => (v === null ? null : Array.isArray(v) ? (v[0] + v[1]) / 2 : v);
const clamp = (x: number) => Math.max(25, Math.min(99, Math.round(x)));

export type RatingKey = 'speed' | 'size' | 'cost' | 'reliability' | 'fuel';
export type Rating = {
  key: RatingKey;
  name: string;
  short: string;
  input: 'monthsToPower' | 'sizeMW' | 'costPerKW' | 'elcc' | 'fuelDays';
  inputName: string;
  formula: string;     // shown on the page
  anchors: string;     // worked examples, shown on the page
  f: (x: number) => number;
};

export const RATINGS: Rating[] = [
  { key: 'speed', name: 'Speed', short: 'SPD', input: 'monthsToPower', inputName: 'months from order to first power',
    formula: '99 − 15 × log₂(months ÷ 6)', anchors: '6 months = 99, 12 = 84, 24 = 69, 48 = 54, 96 = 39',
    f: (m) => 99 - 15 * Math.log2(m / 6) },
  { key: 'size', name: 'Size', short: 'SIZE', input: 'sizeMW', inputName: 'MW from one unit (one machine, farm or reactor)',
    formula: '40 + 59 × log₁₀(MW) ÷ 3', anchors: '1 MW = 40, 10 MW = 60, 100 MW = 79, 1,000 MW = 99',
    f: (mw) => 40 + (59 * Math.log10(mw)) / 3 },
  { key: 'cost', name: 'Cost', short: 'CST', input: 'costPerKW', inputName: 'US$ per kW to build',
    formula: '99 − 59 × log₁₀(US$/kW ÷ 500) ÷ log₁₀(20)', anchors: '$500/kW = 99, $2,000 = 72, $10,000 = 40',
    f: (c) => 99 - (59 * Math.log10(c / 500)) / Math.log10(20) },
  { key: 'reliability', name: 'Round the clock', short: 'RTC', input: 'elcc', inputName: "share of each MW PJM counts as firm (ELCC class rating, 2029/30)",
    formula: 'ELCC in per cent', anchors: 'nuclear 96% = 96, gas combined cycle 75% = 75, tracking solar 7% = 25 (the floor)',
    f: (cf) => cf },
  { key: 'fuel', name: 'Without refuelling', short: 'REFUEL', input: 'fuelDays', inputName: 'days it keeps running on the fuel already on site, if deliveries stop (how hard the fuel is to buy is not measured here)',
    formula: '25 + 74 × log₁₀(days + 1) ÷ log₁₀(1,826)', anchors: '0 days (gas on a pipe) = 25, 30 = 59, 540 = 87, 1,825 (5 years) = 99; no fuel to buy = 99',
    f: (d) => 25 + (74 * Math.log10(d + 1)) / Math.log10(1826) },
];

// A stat whose value is Infinity means "no fuel to buy" (sunlight): it rates 99.
export const rateOne = (r: Rating, s: Stat | undefined): number | null => {
  const x = s ? mid(s.value) : null;
  if (x === null) return null;
  if (!Number.isFinite(x)) return 99;
  return clamp(r.f(x));
};
