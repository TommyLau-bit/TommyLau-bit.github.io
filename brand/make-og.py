#!/usr/bin/env python3
"""Social cards: the piece's cover exactly as on the site, no title, scrim or logo.
LinkedIn wants 1200x630 and covers are 800x600, so each card is framed around the
cover's own drawing and the cover's background is stretched to fill the frame.
Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py"""
import cairosvg, io, glob, re, os
from PIL import Image, ImageChops
W, H = 1200, 630
MARGIN, MIN_H = 50, 420
BG = re.compile(r'<rect width="800" height="600" fill="(url\(#\w+\))"\s*/>')
VER = re.search(r"OG_VERSION = '([^']+)'", open('src/config.ts').read()).group(1)

def render(svg, w, h):
    return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=w, output_height=h))).convert('RGB')

def content_box(svg):
    """Bounding box of everything drawn on top of the background, in SVG units."""
    m = BG.search(svg)
    full = render(svg, 800, 600)
    bg = render(svg[:m.end()] + '</svg>', 800, 600)
    mask = ImageChops.difference(full, bg).convert('L').point(lambda v: 255 if v > 12 else 0)
    return mask.getbbox() or (0, 0, 800, 600)

def frame(box):
    """A 1200:630 viewBox around the drawing, with a margin and a minimum height."""
    x0, y0, x1, y1 = box
    h = max(y1 - y0 + 2 * MARGIN, MIN_H)
    w = h * W / H
    if w < x1 - x0 + 2 * MARGIN:
        w = x1 - x0 + 2 * MARGIN
        h = w * H / W
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return cx - w / 2, cy - h / 2, w, h

os.makedirs('public/og', exist_ok=True)
for md in sorted(glob.glob('src/content/journal/*.md')):
    pid = os.path.basename(md)[:-3]
    cover = re.search(r'^cover:\s*"?(.+?)"?\s*$', open(md).read(), re.M)
    path = 'public' + cover.group(1) if cover else ''
    if not os.path.exists(path):
        print(f'{pid}: no cover, skipped'); continue
    svg = open(path).read()
    if not BG.search(svg):
        print(f'{pid}: cover has no 800x600 background rect, skipped'); continue
    vx, vy, vw, vh = frame(content_box(svg))
    svg = BG.sub(lambda m: f'<rect x="{vx:.1f}" y="{vy:.1f}" width="{vw:.1f}" height="{vh:.1f}" fill="{m.group(1)}"/>', svg, count=1)
    svg = re.sub(r'viewBox="[^"]*"', f'viewBox="{vx:.1f} {vy:.1f} {vw:.1f} {vh:.1f}"', svg, count=1)
    render(svg, W, H).save(f'public/og/{pid}-{VER}.png', optimize=True)
    print(f'{pid}-{VER}.png')
