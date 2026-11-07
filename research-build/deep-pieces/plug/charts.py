"""Charts for the America rations the plug depth piece. Coordinates computed; every value is in the evidence fold.
abilene-chart.svg is carried over from the live contracted-energised-running piece (extracted unchanged)."""
import os
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
W = 560

def hbars(rows, maxv, x0=210, bh=22, gap=20, ticks=(), right=70, fmt=lambda t: f'{t:,g}', y=30):
    """rows: ('H', heading) or (label, sub, value, cls, value_text). value may be (lo, hi) for a range."""
    o = []; xw = W - x0 - right; y0 = y
    sx = lambda v: x0 + v / maxv * xw
    for r in rows:
        if r[0] == 'H':
            y += 6
            o.append(f'<text class="c-lab c-s2t" x="0" y="{y+10}">{r[1]}</text>'); y += 24; continue
        lab, sub, v, cls, vtxt = r
        o.append(f'<text class="c-box-t" x="0" y="{y+9}">{lab}</text><text class="c-note" x="0" y="{y+24}">{sub}</text>')
        if isinstance(v, tuple):
            lo, hi = v
            o.append(f'<rect class="{cls}" x="{x0}" y="{y}" width="{max(2, sx(lo)-x0):.1f}" height="{bh}" rx="2"/>')
            o.append(f'<rect class="c-bar c-mute" x="{sx(lo):.1f}" y="{y}" width="{sx(hi)-sx(lo):.1f}" height="{bh}" rx="2"/>')
            v = hi
        else:
            o.append(f'<rect class="{cls}" x="{x0}" y="{y}" width="{max(2, sx(v)-x0):.1f}" height="{bh}" rx="2"/>')
        o.append(f'<text class="c-lab c-s1t" x="{sx(v)+6:.1f}" y="{y+16}">{vtxt}</text>')
        y += bh + gap
    top, bot = y0 - 12, y - gap + 4
    grid = '<g class="c-grid">' + ''.join(f'<line x1="{sx(t):.1f}" y1="{top}" x2="{sx(t):.1f}" y2="{bot}"/>' for t in ticks) + '</g>'
    axis = '<g class="c-axis">' + ''.join(f'<text x="{sx(t):.1f}" y="{top-6}" text-anchor="middle">{fmt(t)}</text>' for t in ticks) + '</g>'
    o.insert(0, grid + axis)
    o.append(f'<line class="c-base" x1="{x0}" y1="{top}" x2="{x0}" y2="{bot}"/>')
    return ''.join(o), y

def save(name, body, H, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# 1 Texas: the length of the list against what reached the last gate
b, H = hbars([
  ('H', 'All of ERCOT, summer 2026'),
  ('Requests to connect', 'large loads, June 2026', 474, 'c-bar c-mute', '474 GW'),
  ('Eligible for the first batch', 'preliminary, 29 July', 205, 'c-bar c-mute', '205 GW'),
  ('Cleared all but the last gate', '17 loads, 20 August', 6.6, 'c-bar', '6.6 GW, then paused'),
  ('H', 'Oncor alone, the largest wires company'),
  ('Data centre requests', '30 September 2026', 293, 'c-bar c-mute', '293 GW'),
  ('Classified, on condition', 'base and studied load', 45, 'c-bar', '45 GW, 10 already on'),
], 500, x0=200, ticks=(0, 100, 200, 300, 400, 500), right=100, y=40)
save('texas-chart', b, H + 4, 'Bar chart in gigawatts. All of ERCOT in summer 2026: 474 of requests to connect large loads as of June; about 205 eligible for the first batch study, preliminary, 29 July; 17 loads totalling 6.6 that had cleared every step but approval to energise on 20 August, after which ERCOT paused that approval for data centres of 75 megawatts or more. Oncor alone, at 30 September 2026: 293 of data centre requests; about 45 classified on condition of ERCOT\'s audit, 24 as base load, including 10 already energised, and 21 as studied load.')

# 2 the three load transfers, with the test line and the new plant PJM's last auction added
o = []
x0, x1, base, top = 70, 540, 240, 40
maxv = 4000
Y = lambda v: base - v / maxv * (base - top)
o.append('<g class="c-grid">' + ''.join(f'<line x1="{x0}" y1="{Y(t):.1f}" x2="{x1}" y2="{Y(t):.1f}"/>' for t in (1000, 2000, 3000, 4000)) + '</g>')
o.append('<g class="c-axis">' + ''.join(f'<text x="{x0-8}" y="{Y(t)+4:.1f}" text-anchor="end">{t:,}</text>' for t in (0, 1000, 2000, 3000, 4000)) + '</g>')
bars = [(140, '10 Jul 2024', 'six dips in 82 s', [(1500, 'c-bar')], 'about 1,500 MW'),
        (260, '17 Feb 2025', 'four dips', [(1800, 'c-bar')], 'about 1,800 MW'),
        (380, '22 Jul 2026', 'two waves', [(2900, 'c-bar'), (1000, 'c-bar c-alt')], 'about 3,900 MW'),
        (490, 'New plant', '2028/29 auction', [(525, 'c-bar c-mute')], '525 MW')]
for cx, lab, sub, segs, vt in bars:
    acc = 0
    for v, cls in segs:
        o.append(f'<rect class="{cls}" x="{cx-34}" y="{Y(acc+v):.1f}" width="68" height="{Y(acc)-Y(acc+v):.1f}" rx="2"/>'); acc += v
    o.append(f'<text class="c-lab c-s2t" x="{cx}" y="{Y(acc)-8:.1f}" text-anchor="middle">{vt}</text>')
    o.append(f'<text class="c-box-t" x="{cx}" y="{base+20}" text-anchor="middle">{lab}</text><text class="c-note" x="{cx}" y="{base+35}" text-anchor="middle">{sub}</text>')
o.append(f'<text class="c-note" x="{380+40}" y="{Y(2900)+18:.1f}">2,900</text><text class="c-note" x="{380+40}" y="{Y(3900)+18:.1f}">+1,000 a minute later</text>')
o.append(f'<line class="c-today" x1="{x0}" y1="{Y(1500):.1f}" x2="{x1}" y2="{Y(1500):.1f}"/>')
o.append(f'<line class="c-base" x1="{x0}" y1="{base}" x2="{x1}" y2="{base}"/>')
o.append(f'<text class="c-note" x="{x0}" y="{base+58}">Dashed line: 1,500 MW, the size my test says must not recur in 2028</text>')
save('events-chart', ''.join(o), base + 66, 'Bar chart of data centre load in PJM that switched to backup power after a fault the grid cleared normally, in megawatts. 10 July 2024: about 1,500, after six dips in 82 seconds. 17 February 2025: about 1,800, after four dips. 22 July 2026: about 3,900, in two waves, about 2,900 and then about 1,000 a minute later. For scale, the new plant and upgrades cleared in PJM\'s 2028/29 capacity auction: 525. A dashed line at 1,500 megawatts marks the size my test says must not recur in 2028.')

# 3 PJM's capacity auction, with the December cap and the uncapped price
o = []
x0, x1, base, top = 60, 540, 270, 40
maxv = 600
Y = lambda v: base - v / maxv * (base - top)
o.append('<g class="c-grid">' + ''.join(f'<line x1="{x0}" y1="{Y(t):.1f}" x2="{x1}" y2="{Y(t):.1f}"/>' for t in (100, 200, 300, 400, 500, 600)) + '</g>')
o.append('<g class="c-axis">' + ''.join(f'<text x="{x0-8}" y="{Y(t)+4:.1f}" text-anchor="end">${t}</text>' for t in (0, 200, 400, 600)) + '</g>')
A = [('2024/25', 28.92, 'c-bar c-mute', '$28.92', ''), ('2025/26', 269.92, 'c-bar c-mute', '$269.92', ''),
     ('2026/27', 329.17, 'c-bar', '$329.17', 'cap'), ('2027/28', 333.44, 'c-bar', '$333.44', 'cap'),
     ('2028/29', 325.00, 'c-bar', '$325', 'cap'), ('2029/30', 337.83, None, 'cap $337.83', 'December')]
for i, (yr, v, cls, vt, note) in enumerate(A):
    cx = 100 + i * 84
    if cls:
        o.append(f'<rect class="{cls}" x="{cx-26}" y="{Y(v):.1f}" width="52" height="{base-Y(v):.1f}" rx="2"/>')
    else:
        o.append(f'<rect class="c-zone" x="{cx-26}" y="{Y(v):.1f}" width="52" height="{base-Y(v):.1f}" rx="2"/><line class="c-today" x1="{cx-30}" y1="{Y(v):.1f}" x2="{cx+30}" y2="{Y(v):.1f}"/>')
    o.append(f'<text class="c-lab c-s2t" x="{cx}" y="{Y(v)-8:.1f}" text-anchor="middle">{vt}</text>')
    o.append(f'<text class="c-box-t" x="{cx}" y="{base+18}" text-anchor="middle">{yr}</text>')
    if note: o.append(f'<text class="c-note" x="{cx}" y="{base+33}" text-anchor="middle">{note}</text>')
cx = 100 + 4 * 84
o.append(f'<rect class="c-bar c-mute" x="{cx-26}" y="{Y(554.72):.1f}" width="52" height="{Y(325)-Y(554.72):.1f}" rx="2" style="opacity:.35"/>')
o.append(f'<text class="c-note" x="{cx-34}" y="{Y(554.72)+4:.1f}" text-anchor="end">$554.72 without the cap, reported</text>')
o.append(f'<line class="c-base" x1="{x0}" y1="{base}" x2="{x1}" y2="{base}"/>')
save('auction-chart', ''.join(o), base + 44, 'Bar chart of PJM capacity auction prices in dollars per megawatt-day, by delivery year: 28.92 for 2024/25; 269.92 for 2025/26; then the cap three times running, 329.17 for 2026/27, 333.44 for 2027/28 and 325 for 2028/29. Without the cap the 2028/29 auction would have cleared at about 554.72, as reported from PJM. The auction for 2029/30, held in December 2026, has a cap of 337.83.')

# 4 PJM's wholesale cost per MWh, first half 2025 against first half 2026, by part
tot26, tot25 = 114.50, 76.16
sh = {'Energy': 0.635, 'Capacity': 0.171, 'Transmission': 0.174}
v26 = {k: tot26 * s for k, s in sh.items()}; v26['Other'] = tot26 - sum(v26.values())
gr = {'Energy': 1.477, 'Capacity': 3.071, 'Transmission': 1.056}
v25 = {k: v26[k] / g for k, g in gr.items()}; v25['Other'] = tot25 - sum(v25.values())
o = []; x0, x1 = 120, 500; maxv = 120
X = lambda v: x0 + v / maxv * (x1 - x0)
cls = {'Energy': 'c-bar c-mute', 'Capacity': 'c-bar', 'Transmission': 'c-bar c-alt', 'Other': 'c-bar c-mute'}
o.append('<g class="c-grid">' + ''.join(f'<line x1="{X(t):.1f}" y1="30" x2="{X(t):.1f}" y2="150"/>' for t in (0, 30, 60, 90, 120)) + '</g>')
o.append('<g class="c-axis">' + ''.join(f'<text x="{X(t):.1f}" y="22" text-anchor="middle">${t}</text>' for t in (0, 30, 60, 90, 120)) + '</g>')
for row, (lab, vv, tot) in enumerate([('First half 2025', v25, tot25), ('First half 2026', v26, tot26)]):
    y = 44 + row * 60; acc = 0
    o.append(f'<text class="c-box-t" x="0" y="{y+16}">{lab}</text>')
    for k in ('Energy', 'Capacity', 'Transmission', 'Other'):
        o.append(f'<rect class="{cls[k]}" x="{X(acc):.1f}" y="{y}" width="{X(acc+vv[k])-X(acc):.1f}" height="26"{' style="opacity:.5"' if k=="Other" else ""}/>')
        if k in ('Energy', 'Capacity', 'Transmission'):
            o.append(f'<text class="c-note" x="{(X(acc)+X(acc+vv[k]))/2:.1f}" y="{y+42}" text-anchor="middle">${vv[k]:.0f}</text>')
        acc += vv[k]
    o.append(f'<text class="c-lab c-s1t" x="{X(tot)+6:.1f}" y="{y+18}">${tot:.2f}</text>')
lx = x0
for k, t in (('Energy', 'energy'), ('Capacity', 'capacity'), ('Transmission', 'transmission')):
    o.append(f'<rect class="{cls[k]}" x="{lx}" y="178" width="12" height="12"/><text class="c-note" x="{lx+18}" y="188">{t}</text>'); lx += 110
o.append(f'<line class="c-base" x1="{x0}" y1="30" x2="{x0}" y2="150"/>')
save('bill-chart', ''.join(o), 200, f'Stacked bar chart of PJM\'s total wholesale cost of power, in dollars per megawatt-hour. First half of 2025: 76.16, of which energy about {v25["Energy"]:.0f}, capacity about {v25["Capacity"]:.0f} and transmission about {v25["Transmission"]:.0f}. First half of 2026: 114.50, of which energy about {v26["Energy"]:.0f}, capacity about {v26["Capacity"]:.0f} and transmission about {v26["Transmission"]:.0f}. Split by my arithmetic from the market monitor\'s shares and growth rates.')
print('bill parts 2025', {k: round(v, 2) for k, v in v25.items()}, '2026', {k: round(v, 2) for k, v in v26.items()})

# 5 Dominion: contracted against billed
b, H = hbars([
  ('Engineering letters', 'study the substation', 32.5, 'c-bar c-mute', '32.5 GW'),
  ('Construction letters', 'start building it', 9.4, 'c-bar c-mute', '9.4 GW'),
  ('Service agreements', 'both sides committed', 12.0, 'c-bar c-alt', '12.0 GW'),
  ('Billed at peak', 'August 2026', 4.8, 'c-bar', '4.8 GW'),
], 35, x0=200, ticks=(0, 10, 20, 30), right=70, y=40)
save('dominion-chart', b, H + 4, 'Bar chart of Dominion Energy\'s data centre contracts in Virginia, in gigawatts, as of July 2026: 32.5 under engineering letters of authorisation, 9.4 under construction letters and 12.0 under electric service agreements, about 54 in all. Data centre billing peak load in August 2026: 4.8.')

# 6 the operators: contracted against active
b, H = hbars([
  ('H', 'CoreWeave, 30 June 2026'),
  ('Contracted', 'signed power', 3.7, 'c-bar c-mute', '3.7 GW'),
  ('Active', 'chips drawing power', 1.5, 'c-bar', '1.5 GW'),
  ('H', 'Nebius'),
  ('Contracted', 'end 2026 target', 5.0, 'c-bar c-mute', '5 GW'),
  ('Connected', 'end 2026 guide', (0.8, 1.0), 'c-bar c-alt', '0.8 to 1 GW'),
  ('Active', 'end 2025, latest', 0.17, 'c-bar', 'about 0.17 GW'),
], 5.5, x0=200, ticks=(0, 1, 2, 3, 4, 5), right=90, y=40)
save('operators-chart', b, H + 4, 'Bar chart in gigawatts. CoreWeave at 30 June 2026: 3.7 contracted, 1.5 active. Nebius: 5 contracted, its target for the end of 2026; 0.8 to 1 connected, its guide for the end of 2026; about 0.17 active at the end of 2025, its latest active figure.')

# 7 Duke: how much new load fits if it accepts cuts
b, H = hbars([
  ('Cut 0.25% of its energy', 'about 85 hours a year', 76, 'c-bar', '76 GW'),
  ('Cut 0.5%', 'about 177 hours a year', 98, 'c-bar', '98 GW'),
  ('Cut 1%', 'about 366 hours a year', 126, 'c-bar', '126 GW'),
], 140, x0=200, ticks=(0, 40, 80, 120), right=60, y=40)
save('duke-chart', b, H + 4, 'Bar chart of new load the 22 largest US grids could add without new capacity if that load accepts cuts, from Duke University\'s Nicholas Institute, February 2025. 76 gigawatts if it gives up 0.25 per cent of its yearly energy, about 85 hours of cuts a year; 98 gigawatts at 0.5 per cent, about 177 hours; 126 gigawatts at 1 per cent, about 366 hours.')

# 8 PJM's capacity rating: demand response against a four-hour battery
b, H = hbars([
  ('H', 'Demand response'),
  ('2028/29', 'binding', 91, 'c-bar', '91%'),
  ('2029/30', 'binding', 90, 'c-bar', '90%'),
  ('2030/31', 'preliminary', 84, 'c-bar', '84%'),
  ('H', 'Four-hour battery'),
  ('2028/29', 'binding', 59, 'c-bar c-alt', '59%'),
  ('2029/30', 'binding', 57, 'c-bar c-alt', '57%'),
  ('2030/31', 'preliminary', 42, 'c-bar c-alt', '42%'),
], 100, x0=160, bh=18, gap=14, ticks=(0, 25, 50, 75, 100), right=60, fmt=lambda t: f'{t}%', y=40)
save('ratings-chart', b, H + 4, 'Bar chart of how much of each megawatt PJM counts in its capacity market. Demand response: 91 per cent for 2028/29, 90 per cent for 2029/30 and 84 per cent for 2030/31, preliminary. A four-hour battery: 59, 57 and 42 per cent for the same years.')
print('ok')
