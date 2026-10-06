// ── The calls scorecard ──────────────────────────────────────────────────────
//
// The pitch itself (src/content/calls/<slug>.md) is fixed on the day it
// publishes and is never rewritten. This file is the only thing that moves:
// once a month, with Tommy's approval, each open call gets one dated mark.
// Nothing is ever deleted, right or wrong. A resolved call keeps every mark
// and gains a short dated post-mortem. See CALLS-SPEC.md.

export type Mark = {
  date: string;        // YYYY-MM-DD, the close the price is
  price: number;
  falsifier: string;   // one sentence: has anything in "wrong if" happened?
};

export type Resolution = {
  date: string;        // YYYY-MM-DD
  outcome: 'Right' | 'Wrong' | 'Mixed';
  postmortem: string;  // two or three sentences: what happened and what I learned
};

export type Score = {
  id: string;          // the pitch slug
  marks: Mark[];       // oldest first; the first monthly refresh adds the first one
  resolved?: Resolution;
};

export const SCORECARD_REFRESHED: string | null = null;   // YYYY-MM-DD of the last monthly refresh

export const SCORES: Score[] = [];

export const scoreOf = (id: string) => SCORES.find((s) => s.id === id);
