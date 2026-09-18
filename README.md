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

## Every piece needs these two blocks

**1. The analogy.** Right before the first `##` heading. This is the whole point of the journal: the same idea in a familiar frame, for a reader with no finance background.

```html
<details class="analogy">
<summary>Explain it like I don't work in finance</summary>
<p>Everyday comparison, two or three sentences.</p>
<p>Why the comparison holds.</p>
</details>
```

**2. The exposure map.** Just before the closing `---` and the sources note. Turns a viewpoint into something checkable by naming who actually operates in the layer.

```html
<section class="exposure">
<h3>Who is exposed if the claim is right</h3>
<p class="note">This maps who operates in each layer. It is not a recommendation, and naming a company is not a view on its shares.</p>
<dl>
<dt>Category</dt>
<dd>What they do: <span class="names">Company, Company</span>.</dd>
</dl>
<dl class="against">
<dt>On the other side</dt>
<dd>Who loses if this is right.</dd>
</dl>
</section>
```

**Rules for the exposure map.** Name companies and what they make. Never market share, backlogs, financials or ratings. Never a view on shares. Where the AI layer map says there is no view (memory equities), say so in the box.

## "Where to start" is not a table of contents

`/start` is an on-ramp for someone who has never read the site. It is **not** an
index, and **you never touch it when you publish**.

Write whatever you want, drop the `.md` in, push. The piece appears on the home
page in date order and gets its own URL. It does not need a home in the path and
nothing breaks if it never gets one. An energy piece, a one-off note, anything
outside the main arc: all fine, none of it belongs on `/start` by default.

The list is capped at `PATH_MAX` in `src/config.ts`. Anything past the cap is
ignored, so it cannot creep into an index you owe something to.

Revisit it when you feel like it, twice a year at most. Ask one question: if
someone landed here today, which pieces get them oriented fastest? **Swap one
out rather than adding another**, then update `PATH_REVIEWED`, which is the
"Chosen ..." date shown on the page.

## Social cards
`public/og/<slug>.png` is generated per piece from its cover diagram. After adding a piece, run the generator in `brand/make-og.py`, then re-run LinkedIn's Post Inspector on the URL before sharing it.

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
