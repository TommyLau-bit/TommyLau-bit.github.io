import book from '../data/book.json';
import { fmtMoney } from './calls';
import { fmtDate } from '../utils';

// Where a note's company stands in the book today: held, waiting to enter, or
// not bought (and why). One line, for the research table and the note page.
export function bookStatus(slug: string): { label: string; kind: 'held' | 'watch' | 'avoid' | 'none'; detail?: string } {
  const day = (iso: string) => fmtDate(new Date(`${iso}T12:00:00+08:00`));
  const p = book.positions.find((x: any) => x.slug === slug) as any;
  if (p) return { kind: 'held', label: `${p.direction === 'SHORT' ? 'Short' : 'Long'} since ${day(p.entryDate)}` };
  const w = book.watch.find((x: any) => x.slug === slug) as any;
  if (w) return { kind: 'watch', label: 'Waiting to enter', detail: w.signal != null ? `signal above ${fmtMoney(w.currency, w.signal)}` : w.status };
  const a = book.avoid.find((x: any) => x.slug === slug) as any;
  if (a) return { kind: 'avoid', label: 'Not buying', detail: a.read };
  return { kind: 'none', label: 'Not in the book' };
}
