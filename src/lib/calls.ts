import { getCollection, type CollectionEntry } from 'astro:content';
import { scoreOf } from '../data/calls';

export type Pitch = CollectionEntry<'calls'>;

// Published pitches only, except under `astro dev`, where drafts show with a
// banner so Tommy can read them before deciding the call. A pitch marked
// draft: false without Tommy's call fails the build rather than going live
// undecided.
export async function getPitches(): Promise<Pitch[]> {
  const all = await getCollection('calls');
  for (const p of all) {
    if (p.data.draft) continue;
    const c = p.data.call;
    const missing = [
      !p.data.date && 'date',
      !c.direction && 'call.direction',
      c.direction !== 'NO CALL' && c.target == null && 'call.target',
      c.direction === 'NO CALL' && !c.revisitIf && 'call.revisitIf',
      !c.conviction && 'call.conviction',
    ].filter(Boolean);
    if (missing.length) throw new Error(`Pitch ${p.id} is not a draft but has no ${missing.join(', ')}. Only Tommy's decided call can publish.`);
  }
  return all
    .filter((p) => import.meta.env.DEV || !p.data.draft)
    .sort((a, b) => (b.data.date?.valueOf() ?? Infinity) - (a.data.date?.valueOf() ?? Infinity));
}

export const pitchesFor = (pitches: Pitch[], claimId: string) =>
  pitches.filter((p) => p.data.claims.includes(claimId));

// Return on the call since publication, signed so that a correct call is positive.
export function callReturn(p: Pitch, price: number): number | null {
  const c = p.data.call;
  if (c.direction === 'NO CALL') return null;
  const r = price / c.price - 1;
  return c.direction === 'SHORT' ? -r : r;
}

export function latest(p: Pitch) {
  const s = scoreOf(p.id);
  const mark = s?.marks.at(-1);
  const move = mark ? mark.price / p.data.call.price - 1 : null;
  return { score: s, mark, ret: mark ? callReturn(p, mark.price) : null, move };
}

export const fmtMoney = (cur: string, n: number) =>
  `${cur}${n.toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
export const fmtPct = (r: number) => `${r >= 0 ? '+' : ''}${(r * 100).toFixed(1)}%`;
