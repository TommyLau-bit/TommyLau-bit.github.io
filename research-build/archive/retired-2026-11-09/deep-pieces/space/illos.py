"""One illustration: SpaceX's AI1 satellite as published, array and radiator to scale, with a tennis court for size."""
import os
D = os.path.dirname(os.path.abspath(__file__))
def save(name, W, H, body, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

W = 940; s = 10                     # 10 px per metre
o = []; a = o.append
cx = W / 2; bus = 5 * s
wing_l, wing_w = 35 * s, 12 * s     # 2 x 35 m x 12 m = 840 m2
y0 = 34
for side in (-1, 1):
    x = cx - bus / 2 - wing_l if side < 0 else cx + bus / 2
    a(f'<rect class="i-cool-f" x="{x:.0f}" y="{y0}" width="{wing_l}" height="{wing_w}" rx="2"/>')
    for k in range(1, 7):
        a(f'<line class="i-thin" x1="{x + k * wing_l / 7:.0f}" y1="{y0}" x2="{x + k * wing_l / 7:.0f}" y2="{y0 + wing_w}"/>')
    a(f'<line class="i-thin" x1="{x:.0f}" y1="{y0 + wing_w / 2}" x2="{x + wing_l:.0f}" y2="{y0 + wing_w / 2}"/>')
a(f'<rect class="i-metal" x="{cx - bus / 2}" y="{y0 + wing_w / 2 - bus / 2}" width="{bus}" height="{bus}" rx="2"/>')
a(f'<text class="i-cool-t" x="{cx - bus / 2 - wing_l / 2:.0f}" y="{y0 + wing_w + 20}" text-anchor="middle">solar array, about 840 m²</text>')
a(f'<text class="i-cool-t" x="{cx + bus / 2 + wing_l / 2:.0f}" y="{y0 + wing_w + 20}" text-anchor="middle">210 kW at 250 W/m²</text>')
# span marker
ys = y0 - 14
a(f'<line class="i-line" x1="{cx - bus / 2 - wing_l}" y1="{ys}" x2="{cx + bus / 2 + wing_l}" y2="{ys}"/>')
for x in (cx - bus / 2 - wing_l, cx + bus / 2 + wing_l):
    a(f'<line class="i-line" x1="{x}" y1="{ys - 5}" x2="{x}" y2="{ys + 5}"/>')
a(f'<text class="i-n" x="{cx}" y="{ys - 6}" text-anchor="middle">wingspan 75 m</text>')
# radiator below the bus: 16 m x 10 m = 160 m2
ry = y0 + wing_w + 62; rw, rh = 16 * s, 10 * s
a(f'<line class="i-dash" x1="{cx}" y1="{y0 + wing_w / 2 + bus / 2}" x2="{cx}" y2="{ry}"/>')
a(f'<rect class="i-hot-f" x="{cx - rw / 2}" y="{ry}" width="{rw}" height="{rh}" rx="2"/>')
for k in range(1, 8):
    a(f'<line class="i-thin" x1="{cx - rw / 2 + 8}" y1="{ry + k * rh / 8:.0f}" x2="{cx + rw / 2 - 8}" y2="{ry + k * rh / 8:.0f}"/>')
a(f'<text class="i-hot-t" x="{cx + rw / 2 + 12}" y="{ry + 30}">radiator, 160 m²</text>')
a(f'<text class="i-n" x="{cx + rw / 2 + 12}" y="{ry + 48}">sheds 175 kW at 47 to 54°C,</text>')
a(f'<text class="i-n" x="{cx + rw / 2 + 12}" y="{ry + 64}">glowing from both faces</text>')
a(f'<text class="i-n" x="{cx - bus / 2 - 8}" y="{ry - 10}" text-anchor="end">chips: 175 kW average, 250 peak</text>')
# tennis court for scale: 23.77 x 10.97 m
tx, ty = 40, ry; tw, th = 23.77 * s, 10.97 * s
a(f'<rect class="i-faint" x="{tx}" y="{ty}" width="{tw:.0f}" height="{th:.0f}"/>')
a(f'<line class="i-thin" x1="{tx + tw / 2:.0f}" y1="{ty}" x2="{tx + tw / 2:.0f}" y2="{ty + th:.0f}"/>')
a(f'<text class="i-n" x="{tx + tw / 2:.0f}" y="{ty + th + 18:.0f}" text-anchor="middle">a tennis court, for scale</text>')
# mass note
a(f'<text class="i-t" x="{cx}" y="{ry + rh + 56}" text-anchor="middle">Mass filed with the FCC: 3,000 kg. At 175 kW, about 58 kW per tonne; the target is 100.</text>')
save('craft', W, ry + rh + 70, ''.join(o), 'Scale drawing of SpaceX\'s AI1 computing satellite as published on its Starmind page. Two solar wings span 75 metres and cover about 840 square metres, delivering 210 kilowatts at 250 watts per square metre. A small bus at the centre carries chips drawing 175 kilowatts on average and 250 at peak. A radiator of 160 square metres, about a fifth of the array\'s area, sheds that heat at about 47 to 54 degrees, counting the Earth\'s glow, from both faces. A tennis court is drawn beside it for scale. The mass filed with the FCC is 3,000 kilograms, about 58 kilowatts per tonne against a target of 100.')
print('ok')
