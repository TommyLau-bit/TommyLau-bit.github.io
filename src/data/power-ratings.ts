// ── Power roster: how a grade is worked out ─────────────────────────────────
// Graded A to E on a radar chart, like a fighting-game stat sheet (Tommy, 11 Nov 2026:
// letters replaced scores out of 99, which had no benchmark a reader could feel).
// Every grade is read from ONE sourced number on the card (src/data/power.ts) through
// fixed bands, shown on the page. No grade is typed in by hand. A number that could not
// be sourced is null and grades "?"; a machine that needs no fuel grades "∞" on Stamina.
// A range uses its midpoint. One shape per card, no benchmark outline and no sixth
// axis (Tommy, 11 Nov 2026: keep it simple).

export type Num = number | [number, number] | null;
export type Stat = {
  value: Num;          // the number the grade reads (null = no sourced figure)
  display: string;     // as written in the sources fold, with its unit
  basis?: string;      // what exactly it measures
  source?: string;     // publisher and document
  url?: string;
  date?: string;
  short?: string;      // the figure as shown under the chart, when the worked-out wording would mislead
  claim?: string;      // set when the number is a company's own claim, not a measured project: flagged on the card
};

export const mid = (v: Num): number | null => (v === null ? null : Array.isArray(v) ? (v[0] + v[1]) / 2 : v);

export type Grade = 'A' | 'B' | 'C' | 'D' | 'E' | '?' | '∞';
export const GRADES = ['A', 'B', 'C', 'D', 'E'] as const;
export const GRADE_WORD: Record<string, string> = { A: 'excellent', B: 'strong', C: 'middling', D: 'weak', E: 'very weak' };

export type RatingKey = 'speed' | 'size' | 'cost' | 'reliability' | 'stamina';
export type Rating = {
  key: RatingKey;
  name: string;
  input: 'monthsToPower' | 'sizeMW' | 'costPerKW' | 'elcc' | 'fuelDays';
  inputName: string;
  hint: string;               // one plain line for the key above the cards
  better: 'lower' | 'higher';
  cuts: [number, number, number, number];   // A/B, B/C, C/D, D/E boundaries
  unit: (n: number) => string;              // how a boundary reads in the bands table
};

const months = (n: number) => `${n} months`;
const mw = (n: number) => `${n.toLocaleString('en-GB')} MW`;
const usd = (n: number) => `US$${n.toLocaleString('en-GB')}/kW`;
const pct = (n: number) => `${n}%`;
const days = (n: number) => (n >= 365 ? `${n / 365} year` : n === 1 ? '1 day' : `${n} days`);

// Reliability reads PJM's class rating where one exists; where PJM has none (the grid, fuel
// cells) the card says what stands in for it.
export const RATINGS: Rating[] = [
  { key: 'speed', name: 'Speed', input: 'monthsToPower', inputName: 'months from order to first power',
    hint: 'how fast it can be up and running', better: 'lower', cuts: [6, 18, 36, 60], unit: months },
  { key: 'size', name: 'Size', input: 'sizeMW', inputName: 'MW from one unit (one machine, farm or reactor)',
    hint: 'how much power one unit gives', better: 'higher', cuts: [500, 200, 50, 10], unit: mw },
  { key: 'cost', name: 'Cost', input: 'costPerKW', inputName: 'US$ per kW to build',
    hint: 'how cheap it is to build', better: 'lower', cuts: [1000, 1600, 3000, 6000], unit: usd },
  { key: 'reliability', name: 'Reliability', input: 'elcc', inputName: 'share of each MW PJM counts as firm at peak (ELCC class rating, 2029/30)',
    hint: 'how much you can count on it when demand peaks', better: 'higher', cuts: [90, 70, 50, 30], unit: pct },
  { key: 'stamina', name: 'Stamina', input: 'fuelDays', inputName: 'how long it keeps running on the fuel already on site if deliveries stop (not how hard the fuel is to buy)',
    hint: 'how long it runs without new fuel', better: 'higher', cuts: [365, 30, 7, 1], unit: days },
];

export const gradeOf = (r: Rating, s: Stat | undefined): Grade => {
  const x = s ? mid(s.value) : null;
  if (x === null) return '?';
  if (!Number.isFinite(x)) return '∞';
  const i = r.cuts.findIndex((c) => (r.better === 'lower' ? x <= c : x >= c));
  return GRADES[i === -1 ? 4 : i];
};

// The bands in words, for the table in the fold.
export const bandText = (r: Rating): string[] => {
  const [a, b, c, d] = r.cuts.map(r.unit);
  return r.better === 'lower'
    ? [`${a} or less`, `up to ${b}`, `up to ${c}`, `up to ${d}`, `over ${d}`]
    : [`${a} or more`, `${b} or more`, `${c} or more`, `${d} or more`, `under ${d}`];
};

// The real figure beside each grade on the card, worked out from the same number.
const n0 = (n: number) => Math.round(n).toLocaleString('en-GB');
const span = (v: Num, f: (n: number) => string, unit: string) =>
  Array.isArray(v) ? `${f(v[0])} to ${f(v[1])}${unit}` : `${f(v as number)}${unit}`;
const dur = (d: number) => (d < 1 ? `${n0(d * 24)} hours` : d < 60 ? `${n0(d)} days` : d < 1000 ? `${n0(d / 30.44)} months` : `${n0(d / 365.25)} years`);

export const figure = (r: Rating, s: Stat | undefined): string => {
  if (!s || s.value === null) return 'no sourced figure';
  if (s.short) return s.short;
  const v = s.value;
  const target = /target/i.test(s.display) ? ' (target)' : '';
  switch (r.key) {
    case 'speed': return span(v, n0, ' months') + target;
    case 'size': return span(v, (n) => (n < 100 ? String(n) : n0(n)), ' MW');
    case 'cost': return Array.isArray(v) ? `US$${n0(v[0])} to ${n0(v[1])}/kW` : `US$${n0(v)}/kW`;
    case 'reliability': return `${span(v, n0, '%')} firm`;
    case 'stamina': {
      const x = mid(v)!;
      if (!Number.isFinite(x)) return 'needs no fuel';
      if (x === 0) return '0 days: fuel by pipe';
      if (Array.isArray(v)) { const [a, b] = v.map(dur); const u = a.split(' ')[1]; return b.endsWith(u) ? `${a.split(' ')[0]} to ${b}` : `${a} to ${b}`; }
      return dur(x);
    }
  }
};
