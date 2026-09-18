import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
const journal = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/journal' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    summary: z.string(),                       // plain-English one-liner
    category: z.string().default('Explainer'), // small label under the card, e.g. Explainer · Note · Analysis
    cover: z.string().optional(),              // /covers/name.svg or .jpg — optional, a styled fallback renders without it
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});
export const collections = { journal };
