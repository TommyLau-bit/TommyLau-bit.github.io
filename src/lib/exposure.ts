// Reads the exposure box of every piece and builds the company index from it.
// Nothing here is curated: a company appears because a piece names it in a
// <span class="names">, and what the site says about it is that piece's own
// "what they make" sentence.

type Post = { id: string; body?: string; data: { title: string; date: Date } };

export type Mention = { post: Post; group: string; text: string; subject: boolean };
export type Company = { name: string; slug: string; mentions: Mention[] };

// Spellings that differ between pieces but mean the same company.
const ALIAS: Record<string, string> = { LITEON: 'LiteOn', NVIDIA: 'Nvidia', InnoLight: 'Innolight' };

export const slugify = (s: string) =>
  s.toLowerCase().normalize('NFKD').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

const strip = (s: string) => s.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();

export function splitNames(span: string): string[] {
  return strip(span)
    .split(/,\s*|\s+and\s+/)
    .map((n) => n.trim())
    .filter(Boolean)
    .map((n) => ALIAS[n] ?? n);
}

export function exposureOf(post: Post) {
  const box = post.body?.match(/<section class="exposure">([\s\S]*?)<\/section>/)?.[1] ?? '';
  const main = box.split('<dl class="against">')[0];
  const rows: { group: string; text: string; names: string[] }[] = [];
  for (const m of main.matchAll(/<dt>([\s\S]*?)<\/dt>\s*<dd>([\s\S]*?)<\/dd>/g)) {
    const names = [...m[2].matchAll(/<span class="names">([\s\S]*?)<\/span>/g)].flatMap((s) => splitNames(s[1]));
    rows.push({ group: strip(m[1]), text: strip(m[2]), names: [...new Set(names)] });
  }
  return rows;
}

export function companyIndex(posts: Post[]): Company[] {
  const map = new Map<string, Company>();
  for (const post of posts) {
    for (const row of exposureOf(post)) {
      for (const name of row.names) {
        const slug = slugify(name);
        if (!slug) continue;
        const c = map.get(slug) ?? { name, slug, mentions: [] };
        if (!c.mentions.some((m) => m.post.id === post.id && m.group === row.group)) {
          c.mentions.push({ post, group: row.group, text: row.text, subject: /^the subject$/i.test(row.group) });
        }
        map.set(slug, c);
      }
    }
  }
  for (const c of map.values()) c.mentions.sort((a, b) => b.post.data.date.valueOf() - a.post.data.date.valueOf());
  return [...map.values()].sort((a, b) => a.name.localeCompare(b.name, 'en', { sensitivity: 'base' }));
}

// The companies most often named across a set of pieces, for the map.
export function topCompanies(posts: Post[], limit = 10): Company[] {
  return companyIndex(posts)
    .sort((a, b) => new Set(b.mentions.map((m) => m.post.id)).size - new Set(a.mentions.map((m) => m.post.id)).size || a.name.localeCompare(b.name))
    .slice(0, limit);
}

export const pieceCount = (c: Company) => new Set(c.mentions.map((m) => m.post.id)).size;
