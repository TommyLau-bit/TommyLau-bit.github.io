// Real reading pace for someone reading to understand, not skimming (Tommy, 9 Oct 2026).
// Counts only what a reader reads (Tommy, 6 Nov 2026): the folded claims,
// evidence tables, charts, exposure map and sources line are left out.
export function readingTime(text: string): number {
  const read = text
    .replace(/<details class="(?:claims-record|claims-earlier|evidence)">[\s\S]*?<\/details>/g, ' ')
    .replace(/<figure[\s\S]*?<\/figure>/g, ' ')
    .replace(/<section class="exposure">[\s\S]*?<\/section>/g, ' ')
    .replace(/<p class="sources">[\s\S]*?<\/p>/g, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/^\|.*\|$/gm, ' ');
  const words = read.trim().split(/\s+/).length;
  return Math.max(1, Math.round(words / 130));
}
export function fmtDate(d: Date, locale = 'en-GB'): string {
  return d.toLocaleDateString(locale, { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Singapore' });
}

