import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
const journal = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/journal' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    summary: z.string(),                       // plain-English one-liner
    category: z.string().default('Explainer'),
    shortLabel: z.string().optional(),   // 1-3 words, shown huge on the social card so it reads at thumbnail size // small label under the card, e.g. Explainer · Note · Analysis
    cover: z.string().optional(),              // /covers/name.svg or .jpg — optional, a styled fallback renders without it
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    updated: z.coerce.date().optional(),       // when a figure in the piece was overtaken and corrected
    updateNote: z.string().optional(),         // one sentence: what changed. Shown under the title.
  }),
});

// ── Research: one initiation note per file, summarised at /research/<slug>/.
// The full note is a PDF with its Excel model, both in public/research/. The
// Markdown body is the note's text of record; the web page shows only the
// call box, the key points and the downloads. See CALLS-SPEC.md.
// The call is fixed on the day it publishes and never edited after.
// Monthly marks against it live in src/data/calls.ts, not here.
const chart = z.object({
  id: z.string(),
  title: z.string(),
  kind: z.enum(['bar', 'line']),
  unit: z.string().default(''),                 // shown after values, e.g. '%', 'bn'
  prefix: z.string().default(''),               // shown before values, e.g. 'US$'
  decimals: z.number().default(0),
  labels: z.array(z.string()),                  // x axis, oldest first
  series: z.array(z.object({ name: z.string(), values: z.array(z.number().nullable()) })).min(1).max(2),
  refs: z.array(z.object({ value: z.number(), label: z.string() })).default([]),
  note: z.string().optional(),                  // one sentence under the chart: what to see
  source: z.string(),                           // filing or data source, with dates
});
const calls = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/calls' }),
  schema: z.object({
    title: z.string(),                          // the pitch headline, sentence case
    summary: z.string(),                        // two or three plain sentences
    company: z.string(),
    ticker: z.string(),
    exchange: z.string(),
    claims: z.array(z.string()).min(1),         // the claim ids (journal slugs) it rests on
    // Where the pitch finds the claim's piece was wrong, in one sentence. Shown
    // under the claim on /claims; the claim itself is never reworded.
    correction: z.string().optional(),
    keyPoints: z.array(z.string()).min(3).max(5),  // the thesis in three to five sentences
    files: z.object({
      pdf: z.string(),                          // /research/<date>_<Company>_Initiation.pdf
      xlsx: z.string(),                         // /research/<date>_<Company>_Model.xlsx
      thumb: z.string().optional(),             // page one as a PNG, for the library card
      pages: z.number().optional(),
    }),
    date: z.coerce.date().optional(),           // the real publication time; required once published
    draft: z.boolean().default(true),
    // Tommy's call. Left null until he decides it; a pitch cannot publish without it.
    call: z.object({
      // NO CALL is a decided verdict: the research is published, no position is
      // taken, and the box names the price or evidence that would make it a call.
      direction: z.enum(['LONG', 'SHORT', 'NO CALL']).nullable(),
      price: z.number(),                        // price at publication
      priceDate: z.coerce.date(),               // the close that price is
      currency: z.string().default('US$'),
      target: z.number().nullable(),
      horizon: z.string(),                      // e.g. '12 months, to October 2027'
      conviction: z.enum(['High', 'Medium', 'Low']).nullable(),
      wrongIf: z.string(),                      // what proves the call wrong
      revisitIf: z.string().optional(),         // NO CALL only: what would turn it into a call
      position: z.string().default(''),          // a holdings statement, only as Tommy gives it
    }),
    // Claude's draft view for Tommy to accept, change or reject. Never rendered in production.
    draftView: z.object({
      direction: z.enum(['LONG', 'SHORT', 'NO CALL']),
      target: z.number().nullable(),
      conviction: z.enum(['High', 'Medium', 'Low']),
      reasoning: z.string(),
    }).optional(),
    charts: z.array(chart).default([]),
  }),
});
export const collections = { journal, calls };
