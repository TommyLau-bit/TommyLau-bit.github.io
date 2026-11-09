"""Charts for the powering-the-rack depth piece. Coordinates computed; every value is in the evidence fold."""
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

# 1 rack power: the typical rack against the AI racks, and Nvidia's 2025 line for 54 volts
b, H, sx, top, bot = hbars([
  ('Typical rack, 2025', 'survey average', 7.5, 'c-bar c-mute', '7.5 kW'),
  ('GB200 NVL72', 'in volume from 2025', 120, 'c-bar', 'about 120 kW'),
  ('Nvidia rack power, Gen 1', 'ceiling', 145, 'c-bar', '145 kW'),
  ('Gen 2, Vera Rubin', 'ceiling, not a draw', 330, 'c-bar', '330 kW'),
  ('Gen 3, still 54 V inside', 'liquid-cooled shelves', 570, 'c-bar', '570 kW'),
  ('Kyber as shown, 2025', 'keynote, as reported', 600, 'c-bar c-mute', 'about 600 kW'),
  ('Nvidia\'s 800 V target', '"starting in 2027"', 1000, 'c-bar c-alt', '1 MW'),
], 1000, x0=170, ticks=(0, 250, 500, 750, 1000), right=88, y=44)
lx = sx(200)
b += f'<line class="c-today" x1="{lx:.1f}" y1="{top}" x2="{lx:.1f}" y2="{bot}"/>'
b += f'<text class="c-note" x="{lx+6:.1f}" y="{bot+16}">Nvidia, 2025: 54 V racks start to hit limits above 200 kW</text>'
save('rack-chart', b, bot + 24, 'Bar chart of power per rack in kilowatts. The typical rack in 2025 averaged about 7.5. Nvidia\'s GB200 NVL72, in volume from 2025, draws about 120. Nvidia\'s rack power generations: Gen 1 up to 145; Gen 2, with Vera Rubin, a ceiling of 330; Gen 3, still on 54 volts inside the rack with liquid-cooled shelves, up to 570. Kyber as shown in March 2025, about 600, as reported. Nvidia\'s 800 volt target, 1 megawatt racks starting in 2027. A dashed line at 200 kilowatts marks where Nvidia said in 2025 that 54 volt racks start to hit physical limits; Gen 3 now plans to run past it.')

# 2 power per square millimetre of conductor, Nvidia's table
b, H, sx, top, bot = hbars([
  ('415 V AC', 'today\'s row, the baseline', 0.6, 'c-bar c-mute', '0.6 kW per mm²'),
  ('480 V AC', 'the American row', 0.8, 'c-bar c-mute', '16% more'),
  ('800 V DC', 'Nvidia\'s choice', 1.7, 'c-bar', '157% more'),
  ('1,500 V DC', 'held back by codes and arc flash', 3.1, 'c-bar c-alt', '382% more'),
], 3.2, x0=170, ticks=(0, 1, 2, 3), right=110, y=44, fmt=lambda t: f'{t:g} kW')
save('copper-chart', b, H + 4, 'Bar chart of power carried per square millimetre of conductor, on Nvidia\'s 48 amp wire basis. 415 volts AC, the baseline, about 0.6 kilowatts per square millimetre. 480 volts AC, about 0.8, 16 per cent more. 800 volts DC, Nvidia\'s choice, about 1.7, 157 per cent more. 1,500 volts DC, about 3.1, 382 per cent more, but held back by electrical codes and the danger of arc flash.')

# 3 the dates: when each maker said it, and the date it gave
def timeline(R, t0, t1, today, years, x0=196, x1=520, rh=40, top=34):
    X = lambda t: x0 + (t - t0) / (t1 - t0) * (x1 - x0)
    o = ['<g class="c-grid">' + ''.join(f'<line x1="{X(t):.1f}" y1="{top-10}" x2="{X(t):.1f}" y2="{top + rh*len(R) - 16}"/>' for t in years) + '</g>']
    o.append('<g class="c-axis">' + ''.join(f'<text x="{X(t):.1f}" y="{top + rh*len(R)}" text-anchor="middle">{t}</text>' for t in years) + '</g>')
    tx = X(today)
    o.append(f'<line class="c-today" x1="{tx:.1f}" y1="{top-10}" x2="{tx:.1f}" y2="{top + rh*len(R) - 16}"/><text class="c-today-t" x="{tx:.1f}" y="{top-16}" text-anchor="middle">today</text>')
    for i, (lab, sub, s, e, e2, et) in enumerate(R):
        y = top + i * rh + 6
        o.append(f'<text class="c-box-t" x="0" y="{y+2}">{lab}</text><text class="c-note" x="0" y="{y+17}">{sub}</text>')
        o.append(f'<g class="c-span"><line x1="{X(s):.1f}" y1="{y}" x2="{X(e):.1f}" y2="{y}"/></g>')
        if e2:
            o.append(f'<g class="c-span"><line x1="{X(e):.1f}" y1="{y}" x2="{X(e2):.1f}" y2="{y}" style="stroke-width:7;opacity:.45"/></g>')
        o.append(f'<g class="c-start"><circle cx="{X(s):.1f}" cy="{y}" r="4"/></g><g class="c-end"><circle cx="{X(e):.1f}" cy="{y}" r="4.5"/></g>')
        endx = X(e2 or e)
        if endx + 8 + len(et) * 6.2 > W:
            o.append(f'<g class="c-endt"><text x="{X(s)-8:.1f}" y="{y+4}" text-anchor="end">{et}</text></g>')
        else:
            o.append(f'<g class="c-endt"><text x="{endx+8:.1f}" y="{y+4}">{et}</text></g>')
    return ''.join(o), top + rh * len(R) + 14, X

R = [
  ('Nvidia power rack', 'beside the rack', 2026 + 7.3/12, 2026 + 7.5/12, 2026.75, 'Q3 2026'),
  ('Vertiv sidecar', 'said H2 2026 in 2025', 2025 + 4.6/12, 2027.0, 2027.25, 'early 2027'),
  ('Nvidia row power centre', 'end of the row', 2026 + 7.3/12, 2027.5, 2027.75, 'Q3 2027 at soonest'),
  ('ABB SST', 'building edge', 2026 + 9.6/12, 2027.5, 2028.0, 'H2 2027'),
  ('Eaton 800 V DC projects', 'shipments', 2026 + 4.1/12, 2027.75, 2028.0, 'late 2027'),
  ('Vertiv data hall level', 'deployment', 2026 + 6.9/12, 2028.0, 2029.0, '2028'),
  ('NEC 2029 edition', 'the US code', 2026 + 2.9/12, 2028.5, 2028.75, 'Q3 2028'),
  ('Nvidia next-gen SST', 'building edge', 2026 + 7.3/12, 2029.0, None, '"toward 2029"'),
]
b, H, X = timeline(R, 2025, 2030, 2026 + 10.2/12, range(2025, 2031))
b = f'<rect class="c-zone" x="{X(2026 + 10.2/12):.1f}" y="24" width="{X(2028)-X(2026 + 10.2/12):.1f}" height="{34 + 40*len(R) - 16 - 24}"/>' + b
b += f'<text class="c-note" x="{X(2028)-4:.1f}" y="{H+6}" text-anchor="end">shaded: what is left of my test, to 1 January 2028</text>'
save('dates-chart', b, H + 14, 'Timeline of dated 800 volt statements, from when each was said (hollow dot) to the date given (solid dot). Nvidia\'s power rack, said in mid-2026, due in the third quarter of 2026. Vertiv\'s sidecar, promised in 2025 for the second half of 2026, now early 2027. Nvidia\'s row power centre, as soon as the third quarter of 2027. ABB\'s solid-state transformer, said October 2026, second half of 2027. Eaton\'s 800 volt DC project shipments, said May 2026, late 2027. Vertiv\'s data hall level, deployment in 2028. The US electrical code\'s 2029 edition, completed in the third quarter of 2028. Nvidia\'s next generation solid-state transformer, "toward 2029". A shaded band marks what remains of my test, to 1 January 2028.')

# 4 where the money is today: chip-side data centre revenue, third quarter 2026
b, H, sx, top, bot = hbars([
  ('Texas Instruments', 'data centre, about 13% of sales', 790, 'c-bar', 'about $790m'),
  ('Monolithic Power', 'Enterprise Data segment', 506.7, 'c-bar', '$506.7m'),
  ('onsemi', 'AI data centre', 180, 'c-bar', 'about $180m'),
  ('Navitas, GaN', 'all of its revenue', 14.0, 'c-bar c-alt', '$14.0m'),
], 900, x0=170, ticks=(0, 300, 600, 900), right=96, y=44, fmt=lambda t: f'${t:,g}m')
save('money-chart', b, H + 4, 'Bar chart of revenue in the third quarter of 2026, in US dollars, each firm\'s own measure. Texas Instruments data centre, about 790 million, my arithmetic from about 13 per cent of sales. Monolithic Power Systems Enterprise Data segment, 506.7 million. onsemi AI data centre, about 180 million. Navitas, a gallium nitride maker, 14.0 million for all of its revenue.')
print('ok')
