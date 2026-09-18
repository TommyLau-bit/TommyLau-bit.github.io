import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { SITE } from '../config';
export async function GET(context) {
  const posts = (await getCollection('journal', ({ data }) => !data.draft))
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
  return rss({
    title: SITE.name, description: SITE.description, site: context.site,
    items: posts.map((p) => ({ title: p.data.title, pubDate: p.data.date, description: p.data.summary, link: `/journal/${p.id}/` })),
  });
}
