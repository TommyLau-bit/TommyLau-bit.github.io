"""Charts for the heat-and-water depth piece. Coordinates computed; every value is in the evidence fold."""
import os
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
W = 560

def hbars(rows, maxv, x0=210, bh=22, gap=20, ticks=(), right=70, fmt=lambda t: f'{t:,g}', y=30):
    """rows: ('H', heading) or (label, sub, value, cls, value_text)."""
    o = []; xw = W - x0 - right; y0 = y
    sx = lambda v: x0 + v / maxv * xw
    for r in rows:
        if r[0] == 'H':
            y += 6
            o.append(f'<text class="c-lab c-s2t" x="0" y="{y+10}">{r[1]}</text>'); y += 24; continue
        lab, sub, v, cls, vtxt = r
        o.append(f'<text class="c-box-t" x="0" y="{y+9}">{lab}</text><text class="c-note" x="0" y="{y+24}">{sub}</text>')
        o.append(f'<rect class="{cls}" x="{x0}" y="{y}" width="{max(2, sx(v)-x0):.1f}" height="{bh}" rx="2"/>')
        o.append(f'<text class="c-lab c-s1t" x="{sx(v)+6:.1f}" y="{y+16}">{vtxt}</text>')
        y += bh + gap
    top, bot = y0 - 12, y - gap + 4
    grid = '<g class="c-grid">' + ''.join(f'<line x1="{sx(t):.1f}" y1="{top}" x2="{sx(t):.1f}" y2="{bot}"/>' for t in ticks) + '</g>'
    axis = '<g class="c-axis">' + ''.join(f'<text x="{sx(t):.1f}" y="{top-6}" text-anchor="middle">{fmt(t)}</text>' for t in ticks) + '</g>'
    o.insert(0, grid + axis)
    o.append(f'<line class="c-base" x1="{x0}" y1="{top}" x2="{x0}" y2="{bot}"/>')
    return ''.join(o), y, sx, top, bot

def save(name, body, H, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# 1 rack heat, with the air each would need
b, H, sx, top, bot = hbars([
  ('Typical rack, 2025', 'survey average', 7.5, 'c-bar c-mute', '7.5 kW: half a tile'),
  ('Dense air rack', 'ASHRAE, 2021', 45, 'c-bar c-mute', '40 to 50 kW: 2.6 tiles'),
  ('GB200 NVL72', 'Nvidia user guide', 120, 'c-bar', '120 kW: about 8 tiles'),
  ('GB300 NVL72', 'Vertiv\'s design', 142, 'c-bar', '142 kW: about 9 tiles'),
], 160, x0=150, ticks=(0, 40, 80, 120, 160), right=150, y=44, fmt=lambda t: f'{t:g} kW')
save('heat-chart', b, H + 4, 'Bar chart of heat per rack in kilowatts, with the air needed to cool it counted in best-in-class floor tiles of 1,900 cubic feet per minute. A typical rack in 2025, about 7.5 kilowatts, needs about half a tile. A dense air rack of 40 to 50 kilowatts, ASHRAE\'s 2021 example, needs up to 5,000 cubic feet per minute, about 2.6 tiles. Nvidia\'s GB200 NVL72, about 120 kilowatts, would need about 8 tiles. Vertiv\'s GB300 NVL72 design, up to 142 kilowatts, about 9 tiles.')

# 2 LBNL: PUE and site water side by side
rows = [
  ('H', 'Air-cooled hall, midsize'),
  ('With a cooling tower', 1.52, 2.9, False),
  ('Air-cooled chiller', 1.83, 0.05, False),
  ('Dry cooler, chiller backup', 1.6, 0.05, False),
  ('H', 'Liquid-cooled hall, large'),
  ('With a cooling tower', 1.13, 2.0, True),
  ('Dry cooler, adiabatic assist', 1.10, 0.13, True),
  ('Dry cooler', 1.10, 0.0, True),
]
o = []; y = 52; x0 = 172; pw = 160; gx = x0 + pw + 34; ww = W - gx - 36
P = lambda v: x0 + (v - 1.0) / 1.0 * pw          # PUE 1.0 to 2.0
Wt = lambda v: gx + v / 3.0 * ww                  # water 0 to 3 L
o.append(f'<text class="c-lab c-s2t" x="{x0}" y="20">PUE, yearly</text>')
o.append(f'<text class="c-lab c-s2t" x="{gx}" y="20">Water on site, litres per kWh</text>')
y0 = y
for r in rows:
    if r[0] == 'H':
        o.append(f'<text class="c-box-t" x="0" y="{y+12}">{r[1]}</text>'); y += 26; continue
    lab, pue, wat, liq = r
    cls = 'c-bar' if liq else 'c-bar c-mute'
    o.append(f'<text class="c-note" x="0" y="{y+13}">{lab}</text>')
    o.append(f'<rect class="{cls}" x="{x0}" y="{y}" width="{P(pue)-x0:.1f}" height="18" rx="2"/><text class="c-lab c-s1t" x="{P(pue)+5:.1f}" y="{y+13}">{pue:.2f}</text>')
    wt = 'none' if wat == 0 else ('near 0' if wat < 0.1 else f'{wat:.1f}')
    o.append(f'<rect class="{cls}" x="{gx}" y="{y}" width="{max(1.5, Wt(wat)-gx):.1f}" height="18" rx="2"/><text class="c-lab c-s1t" x="{Wt(wat)+5:.1f}" y="{y+13}">{wt}</text>')
    y += 30
g = '<g class="c-grid">' + ''.join(f'<line x1="{P(t):.1f}" y1="{y0-10}" x2="{P(t):.1f}" y2="{y-8}"/>' for t in (1.0, 1.5, 2.0)) + ''.join(f'<line x1="{Wt(t):.1f}" y1="{y0-10}" x2="{Wt(t):.1f}" y2="{y-8}"/>' for t in (0, 1, 2, 3)) + '</g>'
ax = '<g class="c-axis">' + ''.join(f'<text x="{P(t):.1f}" y="{y+8}" text-anchor="middle">{t:g}</text>' for t in (1.0, 1.5, 2.0)) + ''.join(f'<text x="{Wt(t):.1f}" y="{y+8}" text-anchor="middle">{t:g}</text>' for t in (0, 1, 2, 3)) + '</g>'
save('lbnl-chart', g + ax + ''.join(o), y + 18, 'Paired bar charts of simulated yearly medians from Lawrence Berkeley National Laboratory. Midsize air-cooled hall: with a cooling tower, PUE about 1.52 and about 2.9 litres of water evaporated per kilowatt-hour; with an air-cooled chiller, about 1.83 and near zero water; with a dry cooler backed by an air-cooled chiller, about 1.6 and near zero. Large liquid-cooled hall: with a cooling tower, about 1.13 and 2.0 litres; dry cooler with adiabatic assist, about 1.10 and 0.13 litres; dry cooler alone, about 1.10 and no water.')

# 3 whole water: power station plus roof
rows = [
  ('Air hall, tower', 'midsize', 1.52, 2.9),
  ('Air hall, air-cooled chiller', 'midsize', 1.83, 0.0),
  ('Liquid hall, tower', 'large', 1.13, 2.0),
  ('Liquid hall, dry cooler', 'large', 1.10, 0.0),
]
o = []; y = 64; x0 = 190; xw = W - x0 - 60; S = lambda v: v / 10.0 * xw
for lab, sub, pue, site in rows:
    st = pue * 4.52; tot = st + site
    o.append(f'<text class="c-box-t" x="0" y="{y+9}">{lab}</text><text class="c-note" x="0" y="{y+24}">{sub}, PUE {pue:.2f}</text>')
    o.append(f'<rect class="c-bar c-mute" x="{x0}" y="{y}" width="{S(st):.1f}" height="22" rx="2"/>')
    if site:
        o.append(f'<rect class="c-bar c-alt" x="{x0+S(st):.1f}" y="{y}" width="{S(site):.1f}" height="22" rx="2"/>')
    o.append(f'<text class="c-lab c-s1t" x="{x0+S(tot)+6:.1f}" y="{y+16}">{tot:.1f}</text>')
    y += 42
top, bot = 52, y - 16
g = '<g class="c-grid">' + ''.join(f'<line x1="{x0+S(t):.1f}" y1="{top}" x2="{x0+S(t):.1f}" y2="{bot}"/>' for t in (0, 2, 4, 6, 8, 10)) + '</g>'
ax = '<g class="c-axis">' + ''.join(f'<text x="{x0+S(t):.1f}" y="{top-6}" text-anchor="middle">{t} L</text>' for t in (0, 2, 4, 6, 8, 10)) + '</g>'
leg = f'<rect class="c-bar c-mute" x="0" y="8" width="12" height="12" rx="2"/><text class="c-note" x="18" y="18">at the power station</text><rect class="c-bar c-alt" x="160" y="8" width="12" height="12" rx="2"/><text class="c-note" x="178" y="18">on the roof</text>'
save('whole-chart', leg + g + ax + ''.join(o) + f'<line class="c-base" x1="{x0}" y1="{top}" x2="{x0}" y2="{bot}"/>', y, 'Stacked bar chart of water consumed per kilowatt-hour of computing, in litres, at the power station plus on the roof, my arithmetic from the laboratory\'s medians and its national average of 4.52 litres per kilowatt-hour bought. Midsize air hall with a tower: about 6.9 at the power station plus 2.9 on the roof, about 9.8 in all. Air hall with an air-cooled chiller: about 8.3, all at the power station. Large liquid hall with a tower: about 5.1 plus 2.0, about 7.1. Large liquid hall with a dry cooler: about 5.0, all at the power station.')

# 4 Google's sites, 2025 consumption, against the claim's 50 million gallon line
b, H, sx, top, bot = hbars([
  ('The Dalles, Oregon', 'water judged not high risk', 469.0, 'c-bar c-mute', '469.0'),
  ('Henderson, Nevada', 'desert; rating not published', 239.4, 'c-bar c-mute', '239.4'),
  ('Quilicura, Santiago', 'water-cooled', 143.0, 'c-bar c-mute', '143.0'),
  ('Mesa, Arizona', 'Google named it high risk', 9.7, 'c-bar c-alt', '9.7'),
], 500, x0=170, ticks=(0, 100, 200, 300, 400, 500), right=56, y=44)
lx = sx(50)
b += f'<line class="c-today" x1="{lx:.1f}" y1="{top}" x2="{lx:.1f}" y2="{bot}"/>'
b += f'<text class="c-note" x="{lx+6:.1f}" y="{bot+16}">the claim\'s line: 50 million gallons a year</text>'
save('sites-chart', b, bot + 24, 'Bar chart of water consumed in 2025 at four Google campuses, in millions of gallons. The Dalles, Oregon, where Google judged the water not at high risk, 469.0. Henderson, Nevada, a desert site whose source rating Google does not publish, 239.4. Quilicura, Santiago, Chile, water-cooled, 143.0. Mesa, Arizona, which Google named as high water risk, 9.7. A dashed line marks the claim\'s limit of 50 million gallons a year.')
print('ok')
