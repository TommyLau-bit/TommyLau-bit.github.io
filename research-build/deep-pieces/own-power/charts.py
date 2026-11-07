"""Charts for the own-power depth piece. Coordinates computed; every value is from the evidence fold."""
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

# 1 the boom and the bust: US gas capacity by year entered service (EIA-860M, September 2026; my sums)
GW = {1995: 7.2, 1996: 5.0, 1997: 4.3, 1998: 2.2, 1999: 9.4, 2000: 30.2, 2001: 43.4, 2002: 68.6, 2003: 53.8, 2004: 25.0,
      2005: 17.1, 2006: 10.2, 2007: 7.9, 2008: 8.8, 2009: 10.8, 2010: 7.5, 2011: 10.9, 2012: 11.5, 2013: 8.1, 2014: 9.4,
      2015: 7.1, 2016: 9.4, 2017: 10.8, 2018: 21.7, 2019: 8.8, 2020: 7.1, 2021: 7.4, 2022: 7.1, 2023: 9.9, 2024: 2.4,
      2025: 5.3, 2026: 3.7}
x0, x1, top, base = 34, 548, 30, 230
yrs = sorted(GW); n = len(yrs); step = (x1 - x0) / n; bw = step * 0.72
Y = lambda v: base - v / 70 * (base - top)
o = ['<g class="c-grid">' + ''.join(f'<line x1="{x0}" y1="{Y(t):.1f}" x2="{x1}" y2="{Y(t):.1f}"/>' for t in (20, 40, 60)) + '</g>']
o.append('<g class="c-axis">' + ''.join(f'<text x="{x0-6}" y="{Y(t)+4:.1f}" text-anchor="end">{t}</text>' for t in (0, 20, 40, 60))
         + ''.join(f'<text x="{x0 + (yrs.index(t)+0.5)*step:.1f}" y="{base+18}" text-anchor="middle">{t}</text>' for t in (1995, 2002, 2010, 2017, 2026)) + '</g>')
for i, t in enumerate(yrs):
    cls = 'c-bar' if 2000 <= t <= 2005 else ('c-bar c-alt' if t == 2026 else 'c-bar c-mute')
    o.append(f'<rect class="{cls}" x="{x0 + i*step + (step-bw)/2:.1f}" y="{Y(GW[t]):.1f}" width="{bw:.1f}" height="{base-Y(GW[t]):.1f}" rx="1"/>')
o.append(f'<line class="c-base" x1="{x0}" y1="{base}" x2="{x1}" y2="{base}"/>')
px = x0 + (yrs.index(2002)+0.5)*step
o.append(f'<text class="c-lab c-s1t" x="{px+14:.1f}" y="{Y(68.6)+10:.1f}">68.6 GW in 2002</text>')
o.append(f'<text class="c-note" x="{px+14:.1f}" y="{Y(68.6)+28:.1f}">about 238 GW in 2000 to 2005</text>')
sx = x0 + (yrs.index(2017)+0.5)*step
o.append(f'<line class="c-today" x1="{sx:.1f}" y1="{Y(40):.1f}" x2="{sx:.1f}" y2="{base}"/><text class="c-today-t" x="{sx:.1f}" y="{Y(40)-6:.1f}" text-anchor="middle">2017: makers cut jobs</text>')
o.append(f'<text class="c-note" x="{x1}" y="{Y(30):.1f}" text-anchor="end">2026, to September: 3.7</text>')
save('boom-chart', ''.join(o), 252, 'Gigawatts of American gas-fired generating capacity by the year it entered service, from EIA\'s generator inventory of September 2026, plants still running or since retired. The figure rose from 2.2 GW in 1998 to 68.6 GW in 2002, about 238 GW across 2000 to 2005, then fell back to between about 7 and 11 GW in most years, with 21.7 GW in 2018. Siemens and GE cut jobs in their power businesses in 2017. 2024: 2.4 GW; 2025: 5.3 GW; 2026 to September: 3.7 GW.')

# 2 GE Vernova's queue: firm orders and reservations, stacked, with years of output
Q = [('Dec 2025', 40, 43), ('Mar 2026', 44, 56), ('Jun 2026', 53, 63), ('Sep 2026', 64, 58)]
x0, x1, top, base = 40, 470, 30, 230
Y = lambda v: base - v / 140 * (base - top)
step = (x1 - x0) / 5; bw = step * 0.56
o = ['<g class="c-grid">' + ''.join(f'<line x1="{x0}" y1="{Y(t):.1f}" x2="{x1+40}" y2="{Y(t):.1f}"/>' for t in (40, 80, 120)) + '</g>']
o.append('<g class="c-axis">' + ''.join(f'<text x="{x0-6}" y="{Y(t)+4:.1f}" text-anchor="end">{t}</text>' for t in (0, 40, 80, 120)) + '</g>')
for i, (lab, f, s) in enumerate(Q):
    cx = x0 + (i+0.5)*step; bx = cx - bw/2
    o.append(f'<rect class="c-bar" x="{bx:.1f}" y="{Y(f):.1f}" width="{bw:.1f}" height="{base-Y(f):.1f}"/>')
    o.append(f'<rect class="c-bar c-alt" x="{bx:.1f}" y="{Y(f+s):.1f}" width="{bw:.1f}" height="{Y(f)-Y(f+s):.1f}"/>')
    o.append(f'<text class="c-lab c-s1t" x="{cx:.1f}" y="{Y(f+s)-8:.1f}" text-anchor="middle">{f+s} GW</text>')
    o.append(f'<text class="c-note" x="{cx:.1f}" y="{base+18}" text-anchor="middle">{lab}</text>')
    o.append(f'<text class="c-note" x="{cx:.1f}" y="{base+34}" text-anchor="middle">{(f+s)/20:.1f} years</text>')
cx = x0 + 4.5*step
o.append(f'<line class="c-today" x1="{cx-bw/2:.1f}" y1="{Y(130):.1f}" x2="{cx+bw/2:.1f}" y2="{Y(130):.1f}"/><text class="c-note" x="{cx:.1f}" y="{Y(130)-8:.1f}" text-anchor="middle">130+ expected</text>')
o.append(f'<text class="c-note" x="{cx:.1f}" y="{base+18}" text-anchor="middle">Dec 2026</text>')
o.append(f'<line class="c-base" x1="{x0}" y1="{base}" x2="{x1+40}" y2="{base}"/>')
ly = base + 56
o.append(f'<rect class="c-bar" x="{x0}" y="{ly-10}" width="12" height="12"/><text class="c-note" x="{x0+18}" y="{ly}">firm orders</text>')
o.append(f'<rect class="c-bar c-alt" x="{x0+110}" y="{ly-10}" width="12" height="12"/><text class="c-note" x="{x0+128}" y="{ly}">paid slot reservations</text>')
o.append(f'<text class="c-note" x="{x0+300}" y="{ly}">years: at 20 GW a year</text>')
save('queue-chart', ''.join(o), ly + 10, 'Gas turbine gigawatts under contract at GE Vernova at each quarter end, firm orders plus paid slot reservations. December 2025: 40 plus 43, 83 GW, 4.2 years of output at 20 GW a year. March 2026: 44 plus 56, 100 GW, 5.0 years. June 2026: 53 plus 63, 116 GW, 5.8 years. September 2026: 64 plus 58, 122 GW, 6.1 years. GE Vernova expects at least 130 GW at the end of 2026.')

# 3 three makers
b, H = hbars([
  ('GE Vernova', 'at 30 September 2026', 122, 'c-bar', '122 GW: 64 firm, 58 reserved'),
  ('Siemens Energy', 'at 30 June 2026', 95, 'c-bar', '95 GW: 69 firm, 26 reserved'),
  ('Mitsubishi Heavy', 'large units, 30 September 2026', 37, 'c-bar c-mute', '37 GW firm, 83 units'),
], 200, x0=150, ticks=(0, 50, 100, 150, 200), right=10)
save('makers-chart', b, H, 'Gas turbine gigawatts under contract at the three big makers. GE Vernova at 30 September 2026: 122 GW, 64 firm and 58 in paid reservations. Siemens Energy at 30 June 2026: 95 GW, 69 firm and 26 in reservations. Mitsubishi Heavy, large frame units at 30 September 2026: 37 GW of backlog in 83 units; it publishes no reservation figure.')

# 4 cost per kilowatt
b, H = hbars([
  ('H', 'The government\'s planning figure, 2023 dollars'),
  ('Combined cycle, EIA', 'two H-class turbines, 1,227 MW', 868, 'c-bar c-mute', '868'),
  ('Aeroderivatives, EIA', 'four units, 211 MW', 1606, 'c-bar c-mute', '1,606'),
  ('H', 'What builders now file or say'),
  ('Duke, Person County 2', '1,360 MW, with financing', 1618, 'c-bar', 'about 1,620'),
  ('Duke, Cayuga', '1,476 MW, before financing', 2236, 'c-bar', 'about 2,240'),
  ('Duke, Anderson County', '1,365 MW, with financing', 2344, 'c-bar', 'about 2,340'),
  ('Engines, ProPetro', 'with balance of plant', 1450, 'c-bar c-alt', '1,400 to 1,500'),
  ('Williams\' five plants', 'all their capital, 2,588 MW', 3470, 'c-bar c-alt', 'about 3,500'),
], 4000, ticks=(0, 1000, 2000, 3000, 4000), right=90)
save('cost-chart', b, H, 'Capital cost in US dollars per kilowatt. EIA\'s planning figures in 2023 dollars: a two-turbine H-class combined cycle plant 868; four aeroderivatives 1,606. What builders now file or say, my arithmetic: Duke Energy\'s Person County unit 2 about 1,620 with financing; Cayuga about 2,240 before financing; Anderson County about 2,340 with financing; ProPetro\'s gas engines 1,400 to 1,500 with balance of plant; Williams\' five on-site plants about 3,500, all their expected capital.')

# 5 aeroderivatives: ordered against shipped
b, H = hbars([
  ('H', '2025'),
  ('Ordered', '', 63, 'c-bar', '63'),
  ('Shipped', '', 27, 'c-bar c-mute', '27'),
  ('H', 'January to September 2026'),
  ('Ordered', '', 127, 'c-bar', '127'),
  ('Shipped', '', 39, 'c-bar c-mute', '39'),
  ('H', 'Ordered less shipped since 1 January 2025'),
  ('Backlog', 'units waiting', 124, 'c-bar c-alt', '124 units'),
], 140, x0=150, ticks=(0, 35, 70, 105, 140), right=70)
save('aero-chart', b, H, 'GE Vernova aeroderivative gas turbines, in units. In 2025, 63 ordered and 27 shipped. In January to September 2026, 127 ordered and 39 shipped. Ordered less shipped since 1 January 2025: 124 units.')

# 6 gas per gigawatt
b, H = hbars([
  ('Combined cycle', 'heat rate 7,535 Btu/kWh', 0.175, 'c-bar', '0.175 Bcf/d'),
  ('Gas engines', 'heat rate 8,853', 0.205, 'c-bar c-alt', '0.205 Bcf/d'),
  ('Simple-cycle turbines', 'heat rate 10,975', 0.254, 'c-bar c-alt', '0.254 Bcf/d'),
], 0.3, x0=170, ticks=(0, 0.1, 0.2, 0.3), right=90, fmt=lambda t: f'{t:.1f}')
save('gas-chart', b, H, 'Billion cubic feet of gas a day burned by one gigawatt of generation running flat out, my arithmetic from EIA\'s average tested heat rates for 2025. Combined cycle 0.175, at 7,535 Btu per kWh. Gas engines 0.205, at 8,853. Simple-cycle gas turbines, including aeroderivatives, 0.254, at 10,975.')

# 7 the routes, from decision to first power or gas
x0, x1, t0, t1 = 196, 520, 2023, 2035
X = lambda t: x0 + (t - t0) / (t1 - t0) * (x1 - x0)
R = [  # label, sub, start, end, end2 (range end or None), dashed tail to, end text
  ('Socrates, Williams', '556 MW, off the grid', 2025 + 8.6/12, 2026.85, None, None, 'late 2026'),
  ('Williams\' next four', '2,032 MW', 2026 + 6.4/12, 2027.75, 2028.75, None, '2027 to 2028'),
  ('Homer City', 'up to 4,678 MW', 2025 + 10.6/12, 2028.2, None, None, 'early 2028'),
  ('Hyperion, Entergy', '2,262 MW', 2025 + 7.5/12, 2028.5, 2029.5, None, '2028 to 2029'),
  ('Wärtsilä engines', '282 MW order', 2026.6, 2029.5, None, None, '2029'),
  ('Hyperion, second deal', '5,278 MW, vote pending', 2026.2, 2030.5, 2031.5, None, '2030 to 2031'),
  ('Transco pipe, SSE', '1.6 Bcf/d, 55 miles', 2023 + 6/12, 2027.7, None, None, 'Q3 2027'),
  ('Permian Link pipe', '2.8 Bcf/d, 434 miles', 2026 + 9.7/12, 2030.7, None, None, 'Q3 2030'),
  ('A heavy turbine slot', 'sold now', 2026 + 9.9/12, 2032.5, None, 2034.0, 'ships 2032'),
]
rh = 40; top = 34; Hh = top + rh * len(R) + 30
o = ['<g class="c-grid">' + ''.join(f'<line x1="{X(t):.1f}" y1="{top-10}" x2="{X(t):.1f}" y2="{top + rh*len(R) - 16}"/>' for t in range(2023, 2036, 2)) + '</g>']
o.append('<g class="c-axis">' + ''.join(f'<text x="{X(t):.1f}" y="{top + rh*len(R)}" text-anchor="middle">{t}</text>' for t in range(2023, 2036, 2)) + '</g>')
tx = X(2026 + 10.2/12)
o.append(f'<line class="c-today" x1="{tx:.1f}" y1="{top-10}" x2="{tx:.1f}" y2="{top + rh*len(R) - 16}"/><text class="c-today-t" x="{tx:.1f}" y="{top-16}" text-anchor="middle">today</text>')
for i, (lab, sub, s, e, e2, tail, et) in enumerate(R):
    y = top + i * rh + 6
    o.append(f'<text class="c-box-t" x="0" y="{y+2}">{lab}</text><text class="c-note" x="0" y="{y+17}">{sub}</text>')
    o.append(f'<g class="c-span"><line x1="{X(s):.1f}" y1="{y}" x2="{X(e):.1f}" y2="{y}"/></g>')
    if e2:
        o.append(f'<g class="c-span"><line x1="{X(e):.1f}" y1="{y}" x2="{X(e2):.1f}" y2="{y}" style="stroke-width:7;opacity:.45"/></g>')
    if tail:
        o.append(f'<g class="c-span"><line x1="{X(e):.1f}" y1="{y}" x2="{X(tail):.1f}" y2="{y}" style="stroke-dasharray:4 4"/></g>')
    o.append(f'<g class="c-start"><circle cx="{X(s):.1f}" cy="{y}" r="4"/></g><g class="c-end"><circle cx="{X(e):.1f}" cy="{y}" r="4.5"/></g>')
    endx = X(tail or e2 or e)
    if endx + 8 + len(et) * 6.6 > W:
        o.append(f'<g class="c-endt"><text x="{X(s)-8:.1f}" y="{y+4}" text-anchor="end">{et}</text></g>')
    else:
        o.append(f'<g class="c-endt"><text x="{endx+8:.1f}" y="{y+4}">{et}</text></g>')
save('routes', ''.join(o), Hh, 'Dated routes to on-site gas power and its fuel, from the first decision to the first power or gas the owner gives. Socrates, 556 MW off the grid for a Meta affiliate: approved September 2025, power late 2026. Williams\' next four plants, 2,032 MW: financed July 2026, power from the second half of 2027 to the second half of 2028. Homer City, up to 4,678 MW: air permit November 2025, first power targeted early 2028. Entergy\'s plants for Hyperion, 2,262 MW: approved August 2025, power 2028 to 2029. Wärtsilä\'s 282 MW engine order: booked in the third quarter of 2026, fully running in 2029. Entergy\'s second Hyperion deal, 5,278 MW: signed March 2026, vote pending, power 2030 to 2031. Transco\'s Southeast Supply Enhancement pipe: open season mid-2023, gas as early as the third quarter of 2027. Kinder Morgan\'s Permian Link: sanctioned October 2026, gas from the third quarter of 2030. A heavy turbine slot sold now: ships in 2032 and needs about 18 months on site, so power around 2034.')
print('charts ok')
