# The Physical Layer: journal site

Astro static site, live at https://thephysicallayer.fyi. Built and deployed by `.github/workflows/deploy.yml` on every push to `main` (about 60 seconds).

## Where things are

| Path | What it is |
|---|---|
| `CLAUDE.md` | The rule book. Hard rules, what the site around each piece needs, publish commands. |
| `WRITING-FORMAT.md` | The full spec for a piece: deep piece format (§D), sourcing (§E), style, cover, checklist, LinkedIn post. |
| `CALLS-SPEC.md` | The spec for research notes and calls (`/research`). |
| `research-build/HANDOVER.md` | Start here each session: what is scheduled, open flags, what was done each day. |
| `src/content/journal/` | The deep pieces (the live writing). |
| `src/content/calls/` | Research notes, text of record. |
| `src/data/` | `stack.ts` (the map), `claims.ts`, `numbers.ts`, `calls.ts` (track record). |
| `src/pages/`, `src/components/`, `src/layouts/`, `src/styles/` | The site itself. |
| `public/covers/`, `public/og/` | Cover art and social cards, one per live piece. `public/research/` holds note PDFs and models. |
| `brand/` | Checkers (`check-piece.py`, `check-call.py`), card and banner makers, `add-redirects.py`, `linkedin-posts.md` (every post and its slot). |
| `research-build/deep-pieces/` | Working area: agent briefs, each piece's sidecar (verified sources), gap notes, `updates/` (approved update copies waiting for their publish date). |
| `research-build/<company>/` | Build scripts and sources for each research note. `BRIEF-note*.md` are the note briefs; `CHANGELOG.md` logs post-publication corrections to notes. |
| `research-build/archive/` | History, never edited: the original short pieces (`pieces/`), their old drafts and sidecars, pre-merge deep drafts, video transcripts, retired briefs and template, old images. |

## Before every publish

```bash
python3 brand/check-piece.py src/content/journal/<slug>.md
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py
npm run build
```

## Run locally

`npm install` once, then `npm run dev` → http://localhost:4321. Name, tagline and links live in `src/config.ts`.
