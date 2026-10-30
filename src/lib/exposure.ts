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

export const pieceCount = (c: Company) => new Set(c.mentions.map((m) => m.post.id)).size;

// ── Which companies get a page (Tommy, 30 Oct 2026) ──────────────────────────
// The index names every company in an exposure map, but a page of its own is
// kept only for a company the site actually writes about. A company keeps its
// page if any one of these holds:
//   1. it has a research note (src/content/calls/*.md `company:`);
//   2. a heading in the investor layer of a piece that maps it names it;
//   3. the running prose of a piece that maps it names it BODY_MENTIONS times
//      or more, outside the exposure map (tables, boxes and headings excluded).
// Every other company URL redirects to /companies/ (src/pages/companies/[slug].astro).
export const BODY_MENTIONS = 2;

const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

function partsOf(post: Post) {
  const body = (post.body ?? '').replace(/<section class="exposure">[\s\S]*?<\/section>/g, '');
  const investor = body.split('<hr class="layer">')[1] ?? '';
  const headings = investor.split('\n').filter((l) => /^#{2,4}\s/.test(l)).join('\n');
  const prose = body
    .replace(/<(section|details|figure|aside|table|dl|div)\b[\s\S]*?<\/\1>/g, '')
    .split('\n')
    .filter((l) => !/^\s*[|<#]/.test(l))
    .join('\n');
  return { headings, prose };
}

// Times `name` appears as a whole word, not counting where it is part of a
// longer company name (Siemens inside Siemens Energy).
function mentions(name: string, text: string, longer: string[]): number {
  for (const l of longer) text = text.split(l).join(' ');
  return (text.match(new RegExp(`(?<![A-Za-z0-9])${esc(name)}(?![A-Za-z0-9])`, 'g')) ?? []).length;
}

export function companyPages(posts: Post[], noteCompanies: string[]): Company[] {
  const all = companyIndex(posts);
  const names = all.map((c) => c.name);
  const slugs = new Set(all.map((c) => c.slug));
  // A note on "Hitachi" covers "Hitachi Energy" when no company is named plain "Hitachi".
  const noted = (c: Company) => noteCompanies.some((n) =>
    slugify(n) === c.slug || (!slugs.has(slugify(n)) && c.name.startsWith(`${n} `)));
  const parts = new Map(posts.map((p) => [p.id, partsOf(p)]));
  return all.filter((c) => {
    if (noted(c)) return true;
    const longer = names.filter((n) => n !== c.name && n.includes(c.name)).sort((a, b) => b.length - a.length);
    return [...new Set(c.mentions.map((m) => m.post.id))].some((id) => {
      const pt = parts.get(id)!;
      return mentions(c.name, pt.headings, longer) > 0 || mentions(c.name, pt.prose, longer) >= BODY_MENTIONS;
    });
  });
}
