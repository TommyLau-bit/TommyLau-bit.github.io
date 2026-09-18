# The Physical Layer — journal site

Astro static site. Markdown in, website out.

## Publish a piece (the only thing you need to know)
1. Create `src/content/journal/your-slug.md`
2. Top of file:
   ```
   ---
   title: "Your title"
   date: 2026-09-18
   summary: "The one-line plain-English version. Shown at the top of the piece and on the index."
   category: "Explainer"        # small label on the card: Explainer · Note · Analysis · whatever you like
   cover: "/covers/my-image.jpg" # optional. Drop an image in public/covers/. Leave it out and a styled cover renders.
   tags: ["power", "data-centres"]
   draft: false
   ---
   ```
3. Write in Markdown below it. Set `draft: true` to hide a piece while it's unfinished.
4. `git add -A && git commit -m "New piece" && git push` — GitHub builds and publishes it automatically (about 60 seconds).

## Live site
`https://thephysicallayer.fyi` (GitHub Pages, custom domain via `public/CNAME`), built by `.github/workflows/deploy.yml` on every push to `main`.
To use a custom domain later: buy it, add a `CNAME` file in `public/` containing the domain, point the DNS at GitHub Pages, and set `url` in `src/config.ts`.

## Change the name, tagline, author or links
`src/config.ts`. One file. Set `url` to the real domain before deploying.

## Run locally
`npm install` once, then `npm run dev` → http://localhost:4321

## Structure
- `src/content/journal/` — the writing
- `src/pages/` — index, about, article route, RSS
- `src/layouts/Base.astro` — header, footer, meta
- `src/styles/global.css` — all styling, light and dark
