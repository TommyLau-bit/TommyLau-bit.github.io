"""Charts for the data-centres-in-space depth piece. Coordinates computed; every value is in the evidence fold."""
import os
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
W = 560
def save(name, body, H, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# 1 flux: watts per square metre a two-sided panel sheds, by temperature
sig, eps = 5.670e-8, 0.92
F = lambda c: 2 * eps * sig * (c + 273.15) ** 4
x0, x1, y0, y1 = 56, W - 20, 30, 250          # plot box
X = lambda c: x0 + c / 110 * (x1 - x0)
Y = lambda w: y1 - w / 2200 * (y1 - y0)
o = []
o.append('<g class="c-grid">' + ''.join(f'<line x1="{x0}" y1="{Y(w):.1f}" x2="{x1}" y2="{Y(w):.1f}"/>' for w in (0, 500, 1000, 1500, 2000)) + '</g>')
o.append('<g class="c-axis">' + ''.join(f'<text x="{x0-8}" y="{Y(w)+4:.1f}" text-anchor="end">{w:,}</text>' for w in (0, 500, 1000, 1500, 2000))
         + ''.join(f'<text x="{X(c):.1f}" y="{y1+20}" text-anchor="middle">{c}°C</text>' for c in (0, 20, 40, 60, 80, 100)) + '</g>')
# Nvidia coolant band 45 to 55
o.append(f'<rect class="c-zone" x="{X(45):.1f}" y="{y0}" width="{X(55)-X(45):.1f}" height="{y1-y0}"/>')
o.append(f'<text class="c-note" x="{X(50):.1f}" y="{y0-8}" text-anchor="middle">Nvidia coolant, 45 to 55°C</text>')
pts = ' '.join(f'{X(c):.1f},{Y(F(c)):.1f}' for c in range(0, 111, 2))
o.append(f'<polyline class="c-line c-s1" points="{pts}"/>')
for c, lab, dx, anc in ((20, "Starcloud's panel, 20°C: 771", 8, 'start'), (47, "SpaceX's page: about 1,090", 8, 'start'), (67, "Musk's 1,400 needs about 67°C", -8, 'end')):
    w = F(c)
    o.append(f'<circle class="c-dot c-s2" cx="{X(c):.1f}" cy="{Y(w):.1f}" r="5"/>')
    o.append(f'<text class="c-lab c-s2t" x="{X(c)+dx:.1f}" y="{Y(w)+(22 if anc=="start" else -10):.1f}" text-anchor="{anc}">{lab}</text>')
o.append(f'<line class="c-base" x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}"/>')
save('flux-chart', ''.join(o), y1 + 30, 'Line chart of the heat a two-sided panel radiates to deep space, in watts per square metre, against its temperature from 0 to 110 degrees Celsius, at emissivity 0.92. The curve rises with the fourth power of absolute temperature: about 581 watts at 0 degrees, 771 at 20, about 1,090 near 47, 1,400 at 67 and about 2,020 at 100. A shaded band marks Nvidia\'s coolant temperatures of 45 to 55 degrees. Points mark Starcloud\'s panel at 20 degrees, SpaceX\'s published design at about 1,090 watts, and Musk\'s 1,400 watts, which needs about 67 degrees.')

def hbars(rows, maxv, x0=210, bh=22, gap=20, ticks=(), right=70, fmt=lambda t: f'{t:,g}', y=44):
    """rows: (label, sub, lo, hi, cls, text); lo == hi for a single value."""
    o = []; xw = W - x0 - right; ys = y
    sx = lambda v: x0 + v / maxv * xw
    for lab, sub, lo, hi, cls, txt in rows:
        o.append(f'<text class="c-box-t" x="0" y="{y+9}">{lab}</text><text class="c-note" x="0" y="{y+24}">{sub}</text>')
        if lo == hi:
            o.append(f'<rect class="{cls}" x="{x0}" y="{y}" width="{max(2, sx(hi)-x0):.1f}" height="{bh}" rx="2"/>')
        else:
            o.append(f'<rect class="{cls}" x="{sx(lo):.1f}" y="{y}" width="{sx(hi)-sx(lo):.1f}" height="{bh}" rx="2"/>')
        o.append(f'<text class="c-lab c-s1t" x="{sx(hi)+6:.1f}" y="{y+16}">{txt}</text>')
        y += bh + gap
    top, bot = ys - 12, y - gap + 4
    o.insert(0, '<g class="c-grid">' + ''.join(f'<line x1="{sx(t):.1f}" y1="{top}" x2="{sx(t):.1f}" y2="{bot}"/>' for t in ticks) + '</g>'
             + '<g class="c-axis">' + ''.join(f'<text x="{sx(t):.1f}" y="{top-6}" text-anchor="middle">{fmt(t)}</text>' for t in ticks) + '</g>')
    o.append(f'<line class="c-base" x1="{x0}" y1="{top}" x2="{x0}" y2="{bot}"/>')
    return ''.join(o), sx, top, bot

# 2 radiators, kg per square metre
b, sx, top, bot = hbars([
  ('Space station, as flown', 'NASA unit masses', 14.2, 14.2, 'c-bar c-mute', '14.2 kg/m²'),
  ('Space station, NASA Glenn', 'listed figure', 9, 9, 'c-bar c-mute', '~9'),
  ('Pumped-loop designs', 'NASA paper, 2008', 6, 10, 'c-bar c-alt', '6 to 10'),
  ('Heat-pipe radiator', 'tested on the ground, 2011', 3, 3, 'c-bar', '~3'),
], 16, x0=190, ticks=(0, 4, 8, 12, 16), right=96, fmt=lambda t: f'{t:g} kg')
save('radiator-chart', b, bot + 8, 'Bar chart of space radiator mass per square metre of panel. The International Space Station\'s radiators as flown, from NASA\'s unit masses, about 14.2 kilograms. The same radiators as NASA Glenn lists them, about 9. Pumped-loop designs in a 2008 NASA paper, 6 to 10. A heat-pipe radiator tested on the ground in 2011, about 3.')

# 3 the budget: kg per kW against SpaceX's 10 kg
b, sx, top, bot = hbars([
  ('Solar array', 'Redwire\'s range', 8, 14, 'c-bar', '8 to 14'),
  ('Radiator', 'at 1,400 W/m²', 2.1, 10.1, 'c-bar', '2 to 10'),
  ('Chips and rack', 'ground GB200, a ceiling', 11, 11, 'c-bar c-mute', 'about 11'),
  ('Eclipse batteries', 'cells only', 1.2, 2.2, 'c-bar c-alt', '1 to 2'),
], 16, x0=170, ticks=(0, 4, 8, 12, 16), right=80, fmt=lambda t: f'{t:g} kg')
lx = sx(10)
b += f'<line class="c-today" x1="{lx:.1f}" y1="{top}" x2="{lx:.1f}" y2="{bot}"/><text class="c-note" x="{lx-6:.1f}" y="{bot+18}" text-anchor="end">SpaceX\'s whole budget: 10 kg per kW</text>'
save('budget-chart', b, bot + 26, 'Range bar chart of kilograms launched per kilowatt for each part of an orbital data centre, against SpaceX\'s target of 10 kilograms for the whole craft, shown as a dashed line. Solar array, from Redwire\'s product range, 8 to 14. Radiator, at 1,400 watts per square metre, 2 to 10. Chips and rack, from a ground GB200 rack, about 11, a ceiling since a space payload sheds steel. Eclipse batteries, cells only, 1 to 2. Each part alone sits near the whole budget.')

# 4 kW per tonne
b, sx, top, bot = hbars([
  ('SpaceX target', 'prospectus', 100, 100, 'c-bar c-alt', '100'),
  ('SpaceX page', '"vehicle efficiency"', 75, 75, 'c-bar c-mute', '75'),
  ('AI1 peak, FCC mass', '250 kW / 3 t', 83, 83, 'c-bar', '83'),
  ('AI1 average, FCC mass', '175 kW / 3 t', 58, 58, 'c-bar', '58'),
  ('Per Starship launch', '5 MW / 100 t', 50, 50, 'c-bar', '50'),
  ('Starlink V2 mini', 'whole craft, Google', 49, 49, 'c-bar c-mute', '49'),
  ('Starcloud-1', 'at most, one H100', 12, 12, 'c-bar c-mute', '12'),
], 120, x0=170, ticks=(0, 25, 50, 75, 100), right=50, gap=16)
save('kwpt-chart', b, bot + 8, 'Bar chart of kilowatts of computing per tonne launched. SpaceX\'s prospectus target, 100. SpaceX\'s page, vehicle efficiency 75. AI1 at its 250 kilowatt peak over the 3,000 kilograms filed with the FCC, about 83. AI1 at its 175 kilowatt average, about 58. Five megawatts per Starship launch of 100 tonnes, 50. Google\'s estimate for a Starlink V2 mini, whole craft, about 49. Starcloud-1, at most about 12.')

# 5 launched power price, dollars per kW per year
b, sx, top, bot = hbars([
  ('Orbit, $3,600/kg', 'Starlink-class, today', 14700, 14700, 'c-bar', '$14,700'),
  ('Orbit, $200/kg', 'the same craft', 810, 810, 'c-bar c-alt', '$810'),
  ('Ground power bill', 'US AI hall, Google\'s range', 570, 3000, 'c-bar c-mute', '$570 to $3,000'),
], 18000, x0=170, ticks=(0, 5000, 10000, 15000), right=50, fmt=lambda t: f'${t/1000:g}k')
save('price-chart', b, bot + 8, 'Bar chart of Google\'s launched power price in dollars per kilowatt per year over a five-year life. A Starlink-class satellite at a launch price of 3,600 dollars a kilogram, 14,700 dollars. The same craft at 200 dollars a kilogram, 810. The power bill of an American AI hall on the ground, 570 to 3,000.')
print('ok')
