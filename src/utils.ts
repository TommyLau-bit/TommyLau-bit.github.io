export function readingTime(text: string): number {
  const words = text.trim().split(/\s+/).length;
  return Math.max(1, Math.round(words / 220));
}
export function fmtDate(d: Date, locale = 'en-GB'): string {
  return d.toLocaleDateString(locale, { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Singapore' });
}

// Topic labels for tags. Anything not listed is shown with hyphens as spaces.
const TOPIC_LABEL: Record<string, string> = {
  'data-centres': 'Data centres', '800VDC': '800 VDC', HBM: 'HBM', 'the-stack': 'The whole stack',
  'custom-chips': 'Custom chips', 'fuel-cells': 'Fuel cells', 'supply-chain': 'Supply chain',
};
export function topicLabel(tag: string): string {
  if (TOPIC_LABEL[tag]) return TOPIC_LABEL[tag];
  const t = tag.replace(/-/g, ' ');
  return t.charAt(0).toUpperCase() + t.slice(1);
}
export const topicSlug = (tag: string) => tag.toLowerCase();
