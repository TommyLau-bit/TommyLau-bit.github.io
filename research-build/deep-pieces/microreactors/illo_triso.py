"""TRISO zoom: graphite block -> fuel compact -> one particle -> its layers.
Numbers: AGR-2 style UCO particle (kernel ~425 um, buffer ~100, IPyC ~40, SiC ~35, OPyC ~40),
compact ~12.3 mm x 25 mm, prismatic block ~36 cm across flats. Confirm against triso.md."""
import math, random
random.seed(4)
W, H = 930, 440
o = []
a = o.append
# panel frames (faint)
a('<text class="i-k" x="20" y="28">1 · The graphite block</text><text class="i-n" x="20" y="44">about 36 cm across</text>')
a('<text class="i-k" x="318" y="28">2 · One fuel compact</text><text class="i-n" x="318" y="44">graphite, about 12 mm wide</text>')
a('<text class="i-k" x="490" y="28">3 · One TRISO particle</text><text class="i-n" x="490" y="44">just under 1 mm, a poppy seed</text>')
# 1. hexagonal block with holes
cx, cy, R = 135, 230, 112
pts = ' '.join(f'{cx+R*math.cos(math.radians(60*i+30)):.1f},{cy+R*math.sin(math.radians(60*i+30)):.1f}' for i in range(6))
a(f'<polygon class="i-metal" points="{pts}"/>')
# triangular lattice of holes: fuel (amber) and coolant (cool), 2 fuel per coolant
pitch = 16.5
holes = []
for j in range(-8, 9):
    for i in range(-8, 9):
        x = cx + pitch * (i + 0.5 * (j % 2)); y = cy + pitch * 0.866 * j
        # inside hex (use inscribed check)
        dx, dy = abs(x - cx), abs(y - cy)
        if dy > R * 0.866 - 9 or dx > R * 0.866 - 9 or dx * 0.5 + dy * 0.866 > R * 0.866 - 9 + 0.0 and False:
            continue
        if max(dx * 0.866 + dy * 0.5, dy) > R * 0.866 - 10: continue
        if math.hypot(x-cx, y-cy) < 12: continue  # handling hole
        holes.append((x, y, (i + 2*j) % 3 == 0))
for x, y, cool in holes:
    if cool: a(f'<circle class="i-fill" cx="{x:.1f}" cy="{y:.1f}" r="4.3" style="stroke:var(--cool)"/>')
    else: a(f'<circle class="i-fuel-soft" cx="{x:.1f}" cy="{y:.1f}" r="5"/>')
a(f'<circle class="i-fill" cx="{cx}" cy="{cy}" r="7"/>')
# pick one fuel hole to zoom
fx, fy = [(x, y) for x, y, c in holes if not c and x > cx + 30 and abs(y - cy) < 20][0]
a(f'<circle fill="none" stroke="var(--ink)" stroke-width="1.6" cx="{fx:.1f}" cy="{fy:.1f}" r="8.5"/>')
a('<circle class="i-fuel-soft" cx="34" cy="382" r="5"/><text class="i-n" x="46" y="386">fuel hole, stacked with compacts</text>')
a('<circle class="i-fill" cx="34" cy="402" r="4.3" style="stroke:var(--cool)"/><text class="i-n" x="46" y="406">coolant channel (helium)</text>')
# 2. compact cylinder
x0, y0, w, h = 335, 110, 120, 250
a(f'<line class="i-lead" x1="{fx+8:.1f}" y1="{fy-6:.1f}" x2="{x0}" y2="{y0+8}"/><line class="i-lead" x1="{fx+8:.1f}" y1="{fy+6:.1f}" x2="{x0}" y2="{y0+h-8}"/>')
a(f'<path class="i-fill" d="M{x0} {y0+12} V{y0+h-12} A{w/2} 12 0 0 0 {x0+w} {y0+h-12} V{y0+12}"/>')
a(f'<ellipse class="i-metal" cx="{x0+w/2}" cy="{y0+12}" rx="{w/2}" ry="12"/>')
specks = []
while len(specks) < 230:
    x = random.uniform(x0+6, x0+w-6); y = random.uniform(y0+28, y0+h-14)
    if all(math.hypot(x-p, y-q) > 6.2 for p, q in specks): specks.append((x, y))
for x, y in specks: a(f'<circle class="i-fuel" cx="{x:.1f}" cy="{y:.1f}" r="2.1" opacity="0.85"/>')
for k in range(14):
    x = random.uniform(x0+14, x0+w-14); y = y0 + 12 + random.uniform(-6, 6)
    a(f'<circle class="i-fuel" cx="{x:.1f}" cy="{y:.1f}" r="1.8" opacity="0.6"/>')
zx, zy = specks[60]
a(f'<circle fill="none" stroke="var(--ink)" stroke-width="1.4" cx="{zx:.1f}" cy="{zy:.1f}" r="5"/>')
a(f'<text class="i-n" x="{x0}" y="{y0+h+24}">thousands of particles</text><text class="i-n" x="{x0}" y="{y0+h+39}">held in graphite</text>')
# 3. particle cross-section, labels with leaders on the right
pcx, pcy, PR = 590, 238, 122
um = PR / 427.5
dark = 'fill:color-mix(in srgb, var(--ink) 34%, var(--bg));stroke:var(--ink-2);stroke-width:1'
layers = [  # outer radius um, style, label, job
    (427.5, dark, 'Outer carbon', 'protects the shell, bonds it to the graphite'),
    (387.5, 'fill:color-mix(in srgb, var(--cool) 38%, var(--bg));stroke:var(--ink-2);stroke-width:1', 'Silicon carbide', 'the pressure shell that holds fission products in'),
    (352.5, dark, 'Inner carbon', 'seals the kernel: the first wall'),
    (312.5, 'fill:url(#porous);stroke:var(--ink-3);stroke-width:1', 'Porous carbon buffer', 'empty space for gas, catches flying fragments'),
    (212.5, 'fill:var(--fuel);stroke:var(--ink-2);stroke-width:1.2', 'Uranium kernel', 'HALEU, about 0.4 mm across'),
]
a('<defs><pattern id="porous" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" style="fill:color-mix(in srgb, var(--ink) 7%, var(--bg))"/><circle cx="2" cy="2" r="0.9" style="fill:var(--ink-3)" opacity="0.5"/><circle cx="5" cy="5" r="0.6" style="fill:var(--ink-3)" opacity="0.4"/></pattern></defs>')
a(f'<line class="i-lead" x1="{zx+5:.1f}" y1="{zy-3:.1f}" x2="{pcx-PR*0.5:.1f}" y2="{pcy-PR*0.87:.1f}"/><line class="i-lead" x1="{zx+5:.1f}" y1="{zy+3:.1f}" x2="{pcx-PR*0.5:.1f}" y2="{pcy+PR*0.87:.1f}"/>')
for r, st, *_ in layers:
    a(f'<circle style="{st}" cx="{pcx}" cy="{pcy}" r="{r*um:.1f}"/>')
lx = 742
for k, (r, st, lab, job) in enumerate(layers):
    inner = layers[k+1][0] if k+1 < len(layers) else 0
    mid = (r + inner) / 2 * um if k < 4 else 0.45 * r * um
    ang = math.radians(-52 + k * 22)
    px, py = pcx + mid*math.cos(ang), pcy + mid*math.sin(ang)
    ty = 128 + k * 50
    a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.2" style="fill:var(--ink)"/>')
    a(f'<polyline class="i-lead" points="{px:.1f},{py:.1f} {lx-14},{ty-4} {lx-4},{ty-4}"/>')
    a(f'<text class="i-t" x="{lx}" y="{ty}">{lab}</text>')
    words = job.split(); l1 = []; 
    while words and len(' '.join(l1 + [words[0]])) <= 24: l1.append(words.pop(0))
    a(f'<text class="i-n" x="{lx}" y="{ty+15}">{" ".join(l1)}</text>')
    if words: a(f'<text class="i-n" x="{lx}" y="{ty+29}">{" ".join(words)}</text>')
svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="A TRISO fuel element in three zooms. One: a hexagonal graphite block about 36 centimetres across, drilled with fuel holes and helium coolant channels. Two: one fuel compact from a fuel hole, a graphite pellet about 12 millimetres wide holding thousands of tiny particles. Three: one particle, just under one millimetre, cut open to show a uranium kernel of about 0.4 millimetres inside four layers: a porous carbon buffer that gives gas room, an inner carbon layer, a silicon carbide shell that holds the fission products in, and an outer carbon layer.">' + ''.join(x for x in o if x) + '</svg>'
open('illos/triso.svg', 'w').write(svg)
print(len(svg))
