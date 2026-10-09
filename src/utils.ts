// Real reading pace for someone reading to understand, not skimming (Tommy, 9 Oct 2026).
export function readingTime(text: string): number {
  const words = text.trim().split(/\s+/).length;
  return Math.max(1, Math.round(words / 130));
}
export function fmtDate(d: Date, locale = 'en-GB'): string {
  return d.toLocaleDateString(locale, { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Singapore' });
}

