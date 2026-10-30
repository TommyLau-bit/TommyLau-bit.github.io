#!/usr/bin/env python3
"""Print the astro.config.mjs redirect entries for a deep piece's merged slugs.

  python3 brand/add-redirects.py research-build/deep-pieces/<deep>.sidecar.md

Reads the sidecar's redirect map, in either form:

  old-slug -> /journal/<deep>/#old-slug
  | /journal/old-slug/ | /journal/<deep>/#old-slug |      (markdown table row)

and prints one line per entry to paste into REDIRECTS in astro.config.mjs.
Nothing is written; the paste is a deliberate step at merge time.

A redirect cannot coexist with a live page at the same path. At merge time,
in the same change as the paste, delete src/content/journal/<old-slug>.md
(its original text is kept verbatim in research-build/archive/pieces/, never
in src/), and take the old slug off src/data/stack.ts. astro.config.mjs fails
the build if a redirect still has its old .md; this script warns first.
Exit code 1 if the map is empty or a target lacks its #old-slug fragment.
"""
import sys, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = r'[a-z0-9-]+'
ARROW = re.compile(rf'^\s*[-*]?\s*`?(?:/journal/)?({SLUG})/?`?\s*->\s*`?(/journal/{SLUG}/#{SLUG})`?\s*$')
ROW = re.compile(rf'^\|\s*`?/journal/({SLUG})/?`?\s*\|\s*`?(/journal/{SLUG}/#{SLUG})`?\s*\|')


def entries(text):
    out = []
    for line in text.splitlines():
        m = ARROW.match(line) or ROW.match(line)
        if m and (m.group(1), m.group(2)) not in out:
            out.append((m.group(1), m.group(2)))
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    found = entries(open(sys.argv[1]).read())
    if not found:
        print('no redirect lines found (old-slug -> /journal/<deep>/#old-slug)')
        sys.exit(1)
    bad = 0
    for old, to in found:
        frag = to.split('#', 1)[1]
        if frag != old:
            print(f'  FAIL  {old}: target fragment #{frag} is not the old slug')
            bad += 1
        if to.split('/')[2] == old:
            print(f'  FAIL  {old}: redirects to itself; the deep piece keeps this slug, so it needs no redirect')
            bad += 1
        if os.path.exists(os.path.join(ROOT, 'src/content/journal', old + '.md')):
            print(f'  warn  src/content/journal/{old}.md still exists: delete it in the same change, or the build fails')
    print('\n// paste into REDIRECTS in astro.config.mjs')
    for old, to in found:
        print(f"  '/journal/{old}': '{to}',")
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
