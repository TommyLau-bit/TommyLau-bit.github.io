"""Charts: two new bar charts, plus three charts lifted unchanged from the live pieces."""
import os, re
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
def hbars(rows, maxv, W=560, x0=210, bh=22, gap=20, ticks=()):
    o = []; y = 30; xw = W - x0 - 70
    sx = lambda v: x0 + v / maxv * xw
    o.append('<g class="c-grid">' + ''.join(f'<line x1="{sx(t):.1f}" y1="18" x2="{sx(t):.1f}" y2="{30+len(rows)*(bh+gap)-gap+4}"/>' for t in ticks) + '</g>')
    o.append('<g class="c-axis">' + ''.join(f'<text x="{sx(t):.1f}" y="12" text-anchor="middle">{t:g}</text>' for t in ticks) + '</g>')
    for lab, sub, v, cls, vtxt in rows:
        o.append(f'<text class="c-box-t" x="0" y="{y+9}">{lab}</text><text class="c-note" x="0" y="{y+24}">{sub}</text>')
        o.append(f'<rect class="{cls}" x="{x0}" y="{y}" width="{max(2, sx(v)-x0):.1f}" height="{bh}" rx="2"/>')
        o.append(f'<text class="c-lab c-s1t" x="{sx(v)+6:.1f}" y="{y+16}">{vtxt}</text>')
        y += bh + gap
    o.append(f'<line class="c-base" x1="{x0}" y1="18" x2="{x0}" y2="{y-gap+4}"/>')
    return ''.join(o), y
def save(name, body, H, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 560 {H}" role="img" aria-label="{aria}">{body}</svg>')
b, H = hbars([
  ('Pilot call', 'awarded July 2023', 80, 'c-bar', 'about 80 MW'),
  ('Second call', 'awarded August 2026', 200, 'c-bar', '200 MW'),
  ('Average draw, 2024', '6.5 TWh, about 10% of use', 740, 'c-bar c-mute', 'about 740 MW'),
  ('Whole fleet, IT capacity', 'maximum, 2026, incl. the 200', 1600, 'c-bar c-alt', 'more than 1.6 GW'),
], 1700, ticks=(0, 500, 1000, 1500))
save('sg-chart', b, H, 'Megawatts. Singapore allocated about 80 MW in its pilot call, awarded July 2023, and 200 MW in its second call, awarded August 2026. Its data centres drew about 740 MW on average in 2024, from 6.5 terawatt-hours, about 10 per cent of national electricity use. Its whole fleet has more than 1.6 GW of maximum IT load capacity, including the 200 MW just awarded.')
b, H = hbars([
  ('Data centres, drawn', 'August 2026, Malaysia', 1.37, 'c-bar', '1.37'),
  ('Data centre peak, 2030', 'planning projection', 8.39, 'c-bar c-mute', '8.39'),
  ('Data centres, booked', 'all supply agreements, Aug 2026', 8.77, 'c-bar c-mute', '8.77'),
  ('117 approved centres', 'if all built, minister (oral)', 23.25, 'c-bar', 'about 23 to 23.5'),
  ('Peninsula, record peak', 'all users, 6 Aug 2026', 22.014, 'c-bar c-alt', '22.0'),
  ('Peninsula, installed', 'all power stations, June 2026', 29.2, 'c-bar c-alt', '29.2'),
], 32, ticks=(0, 10, 20, 30))
save('sums-chart', b, H, 'Gigawatts, Peninsular Malaysia. Data centres drew 1.37 GW in August 2026. Planners project a data centre peak of 8.39 GW by 2030. Data centres have booked 8.77 GW under signed supply agreements. If all 117 approved data centres are built, the investment minister said they would need about 23 to 23.5 GW. The peninsula\'s record peak demand, for all users, was 22.0 GW on 6 August 2026, and its installed generating capacity is 29.2 GW.')
def lift(piece, pat, name):
    t = open(os.path.join(ROOT, 'src/content/journal', piece + '.md')).read()
    i = t.index(pat); s = t.index('<svg', i); e = t.index('</svg>', s) + 6
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(t[s:e])
lift('the-queue-not-the-chip', "Malaysia's halls draw more each quarter", 'fill-chart')
lift('the-queue-not-the-chip', 'Counted against what they contracted', 'ratio-chart')
lift('hong-kong-has-the-plug', 'Data centres are a small load', 'hk-chart')
print('charts ok')
