"""Charts for the equipment queue depth piece. Coordinates computed; every value is from the evidence fold.
years-chart and siemens-chart are carried over from the live piece (extracted, label updated)."""
import os
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
W = 560

def hbars(rows, maxv, x0=210, bh=22, gap=20, ticks=(), right=70, fmt=lambda t: f'{t:,g}'):
    """rows: ('H', heading) or (label, sub, value, cls, value_text)."""
    o = []; y = 30; xw = W - x0 - right
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
    top, bot = 18, y - gap + 4
    grid = '<g class="c-grid">' + ''.join(f'<line x1="{sx(t):.1f}" y1="{top}" x2="{sx(t):.1f}" y2="{bot}"/>' for t in ticks) + '</g>'
    axis = '<g class="c-axis">' + ''.join(f'<text x="{sx(t):.1f}" y="12" text-anchor="middle">{fmt(t)}</text>' for t in ticks) + '</g>'
    o.insert(0, grid + axis)
    o.append(f'<line class="c-base" x1="{x0}" y1="{top}" x2="{x0}" y2="{bot}"/>')
    return ''.join(o), y

def save(name, body, H, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

def timeline(R, t0, t1, today, years, x0=196, x1=520, rh=40, top=34, ranges=False):
    """R rows: (label, sub, start, end, end2, end_text). start None = no start dot (line from today)."""
    X = lambda t: x0 + (t - t0) / (t1 - t0) * (x1 - x0)
    o = ['<g class="c-grid">' + ''.join(f'<line x1="{X(t):.1f}" y1="{top-10}" x2="{X(t):.1f}" y2="{top + rh*len(R) - 16}"/>' for t in years) + '</g>']
    o.append('<g class="c-axis">' + ''.join(f'<text x="{X(t):.1f}" y="{top + rh*len(R)}" text-anchor="middle">{t}</text>' for t in years) + '</g>')
    tx = X(today)
    o.append(f'<line class="c-today" x1="{tx:.1f}" y1="{top-10}" x2="{tx:.1f}" y2="{top + rh*len(R) - 16}"/><text class="c-today-t" x="{tx:.1f}" y="{top-16}" text-anchor="middle">today</text>')
    for i, (lab, sub, s, e, e2, et) in enumerate(R):
        y = top + i * rh + 6
        o.append(f'<text class="c-box-t" x="0" y="{y+2}">{lab}</text><text class="c-note" x="0" y="{y+17}">{sub}</text>')
        s0 = today if s is None else s
        o.append(f'<g class="c-span"><line x1="{X(s0):.1f}" y1="{y}" x2="{X(e):.1f}" y2="{y}"/></g>')
        if e2:
            o.append(f'<g class="c-span"><line x1="{X(e):.1f}" y1="{y}" x2="{X(e2):.1f}" y2="{y}" style="stroke-width:7;opacity:.45"/></g>')
        if s is not None:
            o.append(f'<g class="c-start"><circle cx="{X(s):.1f}" cy="{y}" r="4"/></g>')
        o.append(f'<g class="c-end"><circle cx="{X(e):.1f}" cy="{y}" r="4.5"/></g>')
        endx = X(e2 or e)
        if endx + 8 + len(et) * 6.4 > W:
            o.append(f'<g class="c-endt"><text x="{X(s0)-8:.1f}" y="{y+4}" text-anchor="end">{et}</text></g>')
        else:
            o.append(f'<g class="c-endt"><text x="{endx+8:.1f}" y="{y+4}">{et}</text></g>')
    return ''.join(o), top + rh * len(R) + 14

# 1 the factories: announcement to production (each maker's own dates; Charlotte's later date is a press report)
F = [
  ('Siemens Energy, Charlotte', 'large transformers, $150m', 2024 + 1.5/12, 2027.1, None, 'early 2027, press'),
  ('Virginia Transformer, Rincon', 'expansion, $40m', 2025 + 10.5/12, 2027 + 2.5/12, None, 'March 2027'),
  ('HD Hyundai, Montgomery', 'second plant, about $200m', 2026 + 2.2/12, 2027 + 3.5/12, None, 'April 2027'),
  ('Eaton, Bellevue', 'switchgear, over $30m', 2026 + 3.3/12, 2027.0, 2027.5, 'first half 2027'),
  ('Hitachi Energy, Alamo', 'bushings, $106m', 2025 + 7.6/12, 2027.5, None, 'mid-2027'),
  ('Eaton, Jonesville', 'transformers, $340m', 2025 + 1.4/12, 2027.0, 2028.0, '2027'),
  ('Cleveland-Cliffs, Butler', 'core steel, $200m', 2026 + 9.2/12, 2028.15, None, 'early 2028'),
  ('Siemens Energy, Nuremberg', 'transformers, €220m', 2025 + 8.2/12, 2028.0, None, 'by 2028'),
  ('Hyosung, Memphis', 'transformers, $157m', 2025 + 10.5/12, 2028.0, 2029.0, '2028'),
  ('Hitachi Energy, Gallman', 'transformers, $528m', 2026 + 8.5/12, 2029.0, 2030.0, '2029'),
  ('Prolec GE, Goldsboro', 'transformers, $140m', 2025 + 4.5/12, 2030.0, None, 'doubled by 2030'),
]
b, H = timeline(F, 2024, 2031, 2026 + 10.2/12, range(2024, 2032))
save('factories-chart', b, H, 'Timeline of dated new plants for transformers, switchgear, bushings and core steel, from announcement to the production date each maker gives. Siemens Energy Charlotte, announced February 2024 for early 2026, early 2027 by a press report. Virginia Transformer Rincon, announced November 2025, March 2027. HD Hyundai Montgomery, ground broken March 2026, April 2027. Eaton Bellevue, April 2026, first half of 2027. Hitachi Energy Alamo bushings, August 2025, mid-2027. Eaton Jonesville, February 2025, 2027. Cleveland-Cliffs Butler Works steel, October 2026, early 2028. Siemens Energy Nuremberg, September 2025, by 2028. Hyosung Memphis, November 2025, 2028. Hitachi Energy Gallman, September 2026, 2029. Prolec GE Goldsboro, May 2025, capacity doubled by 2030.')

# 2 imports of large liquid transformers, HS 850423 (UN Comtrade, US imports)
b, H = hbars([
  ('H', 'Each year'),
  ('2022', '', 1258, 'c-bar c-mute', '$1.26bn'),
  ('2023', '', 1927, 'c-bar c-mute', '$1.93bn'),
  ('2024', '', 2978, 'c-bar c-mute', '$2.98bn'),
  ('2025', '5,021 units', 4145, 'c-bar', '$4.15bn'),
  ('H', '2025, by origin'),
  ('Mexico', '31% in 2022', 803, 'c-bar', '$803m, 19%'),
  ('Korea', '7% in 2022', 748, 'c-bar', '$748m, 18%'),
  ('Brazil', '', 531, 'c-bar', '$531m, 13%'),
  ('Austria', '', 431, 'c-bar', '$431m, 10%'),
  ('China', '4.7% in Jan to Aug 2026', 90, 'c-bar c-alt', '$90m, 2.2%'),
], 4500, x0=170, bh=18, gap=18, ticks=(0, 1500, 3000, 4500), right=96, fmt=lambda t: f'${t/1000:g}bn' if t else '0')
save('imports-chart', b, H, 'US imports of liquid-filled transformers above 10 MVA, from UN trade data. 2022: 1.26 billion dollars. 2023: 1.93 billion. 2024: 2.98 billion. 2025: 4.15 billion, 5,021 units. In 2025 by origin: Mexico 803 million, 19 per cent, down from 31 per cent in 2022; Korea 748 million, 18 per cent, up from 7 per cent; Brazil 531 million, 13 per cent; Austria 431 million, 10 per cent; China 90 million, 2.2 per cent, and 4.7 per cent in January to August 2026.')

# 3 tariffs (Section 232, Proclamation 11021 annexes, in force 6 April 2026)
b, H = hbars([
  ('H', 'The finished unit'),
  ('Large transformer', 'over 10 MVA, to end 2027', 15, 'c-bar c-mute', '15%'),
  ('Large transformer', 'from 1 January 2028', 25, 'c-bar c-mute', '25%'),
  ('Distribution transformer', 'up to 10 MVA', 25, 'c-bar c-mute', '25%'),
  ('H', 'Its inputs'),
  ('Cores and laminations', '15% if for large units', 25, 'c-bar', '25%'),
  ('Core steel strip', 'GOES and other alloy steel', 50, 'c-bar', '50%'),
  ('Copper wire', 'winding wire, stranded wire', 50, 'c-bar', '50%'),
], 60, x0=190, ticks=(0, 25, 50), right=60, fmt=lambda t: f'{t}%')
save('tariff-chart', b, H, 'US Section 232 tariffs on the full value of the goods, since 6 April 2026. Large power transformers over 10 MVA: 15 per cent until the end of 2027, then 25 per cent from 1 January 2028. Distribution transformers up to 10 MVA: 25 per cent. Cores and laminations: 25 per cent, or 15 per cent since 8 June 2026 when imported to make large transformers. Grain-oriented electrical steel strip and other flat-rolled alloy steel: 50 per cent. Copper wire: 50 per cent.')

# 4 prices: BLS PPI indexed to 2020 average = 100
P = [('2020', 2020.5), ('Dec 2022', 2022.95), ('Dec 2023', 2023.95), ('Dec 2024', 2024.95), ('Dec 2025', 2025.95), ('Sep 2026', 2026.7)]
TR = [255.3, 410.3, 425.9, 432.6, 455.9, 475.1]
SW = [219.1, 291.2, 310.4, 329.6, 369.2, 412.2]
x0, x1, top, base = 44, 400, 24, 224
X = lambda t: x0 + (t - 2020) / (2027 - 2020) * (x1 - x0)
Y = lambda v: base - (v - 80) / (200 - 80) * (base - top)
o = ['<g class="c-grid">' + ''.join(f'<line x1="{x0}" y1="{Y(t):.1f}" x2="{x1}" y2="{Y(t):.1f}"/>' for t in (100, 140, 180)) + '</g>']
o.append('<g class="c-axis">' + ''.join(f'<text x="{x0-6}" y="{Y(t)+4:.1f}" text-anchor="end">{t}</text>' for t in (100, 140, 180))
         + ''.join(f'<text x="{X(t):.1f}" y="{base+18}" text-anchor="middle">{t}</text>' for t in range(2020, 2027, 2)) + '</g>')
for ser, cls, lab, dy in ((TR, 's1', 'Transformers, +86%', 16), (SW, 's2', 'Switchgear, +88%', -8)):
    pts = [(X(t), Y(v / ser[0] * 100)) for (_, t), v in zip(P, ser)]
    o.append(f'<polyline class="c-line c-{cls}" points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '"/>')
    o.append(''.join(f'<circle class="c-dot c-{cls}" cx="{x:.1f}" cy="{y:.1f}" r="3"/>' for x, y in pts))
    o.append(f'<text class="c-lab c-{cls}t" x="{pts[-1][0]+8:.1f}" y="{pts[-1][1]+dy:.1f}">{lab}</text>')
o.append(f'<line class="c-base" x1="{x0}" y1="{base}" x2="{x1}" y2="{base}"/>')
o.append(f'<text class="c-note" x="{X(2021.2):.1f}" y="{Y(186):.1f}">2020 average = 100</text>')
save('prices-chart', ''.join(o), base + 30, 'US producer price indexes for transformer makers and switchgear makers, indexed to their 2020 averages. Transformers: 100 in 2020, about 161 in December 2022, 167 in December 2023, 169 in December 2024, 179 in December 2025 and 186 in September 2026, up 86 per cent. Switchgear: 100, about 133, 142, 150, 169 and 188, up 88 per cent.')

# 5 inside the fence: when 2026's orders ship, in the makers' own words (from today)
WAITS = [
  ('Eaton, whole company', '72% of backlog', None, 2027.7, None, 'within a year'),
  ('Schneider Electric', 'backlog visibility', None, 2027.0, 2029.0, 'into 2027 and 2028'),
  ('Generac, Amazon deal', 'first deliveries', None, 2027.0, 2029.0, '2027 and 2028'),
  ('ABB, data centre gear', 'lead time 12 to 24 months', None, 2027.85, 2028.85, '12 to 24 months'),
  ('Caterpillar, engines', 'large engines, call', None, 2029.0, 2030.0, 'into 2029'),
  ('Caterpillar, turbines', 'call', None, 2030.0, 2031.0, 'into 2030'),
  ('Large power transformer', 'DOE, July 2024', None, 2029.85, 2031.85, '3 to 5 years'),
]
b, H = timeline(WAITS, 2026, 2033, 2026 + 10.2/12, range(2026, 2034))
save('waits-chart', b, H, 'When orders signed now are due to ship, in each maker\'s own words, measured from today. Eaton, whole company: 72 per cent of its backlog within twelve months. Schneider Electric: backlog gives visibility into 2027 and 2028. Generac: Amazon\'s initial deliveries in 2027 and 2028. ABB: data centre lead times of 12 to 24 months, said on a call. Caterpillar: large engine orders accepted into 2029 and turbine orders into 2030, said on a call. A large power transformer: 36 months commonly quoted and up to 60, US Department of Energy, July 2024.')

# 6 rack power
b, H = hbars([
  ('Typical rack', 'Uptime survey, 2025', 9, 'c-bar c-mute', 'almost 9 kW'),
  ('Nvidia GB200 rack', 'reference design, 2024', 132, 'c-bar', 'up to 132 kW'),
  ('Nvidia\'s plan', 'racks from 2027', 1000, 'c-bar c-alt', '1,000 kW'),
], 1000, x0=170, ticks=(0, 250, 500, 750, 1000), right=84, fmt=lambda t: f'{t:,}')
save('rack-chart', b, H, 'Power drawn by one rack, in kilowatts. The typical rack in the Uptime Institute\'s 2025 survey: almost 9. An Nvidia GB200 rack in the Schneider and Nvidia reference design of 2024: up to 132. Nvidia\'s plan for racks from 2027: 1,000 kilowatts, a megawatt.')

# 7 parts: delivery times in weeks (Hitachi Energy's component page)
b, H = hbars([
  ('H', 'From Sweden, Oct 2026'),
  ('Bushings, 245 to 550 kV', 'GSBK and ARF', 135, 'c-bar', '135 weeks'),
  ('Bushings, GOH', '', 46, 'c-bar c-mute', '46'),
  ('Bushings, GOB+ and GSA', '', 40, 'c-bar c-mute', '40'),
  ('Tap changers', 'on-load', 22, 'c-bar c-mute', '10 to 22'),
  ('H', 'From China, Aug 2026'),
  ('Bushings, ARF 550 kV', '', 16, 'c-bar c-alt', '16'),
  ('Bushings, ARF 245, 420', '', 14, 'c-bar c-alt', '14'),
  ('H', 'In 2012'),
  ('High-voltage bushings', 'up to five months, DOE', 22, 'c-bar c-mute', 'about 22'),
], 156, x0=190, bh=18, gap=18, ticks=(0, 52, 104, 156), right=80, fmt=lambda t: f'{t//52} yr' if t else '0')
save('parts-chart', b, H, 'Delivery times for transformer parts, in weeks, from Hitachi Energy\'s component page. From Ludvika, Sweden, updated 29 October 2026: high-voltage bushings of 245 to 550 kilovolts, 135 weeks; GOH bushings 46; GOB plus and GSA bushings 40; on-load tap changers 10 to 22. From Hefei, China, updated 4 August 2026: ARF 550 bushings 16 weeks; ARF 245 and 420, 14. In 2012 the US Department of Energy heard that high-voltage bushings took up to five months, about 22 weeks.')
print('charts ok')
