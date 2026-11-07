"""Charts for the nuclear depth piece. Coordinates computed; every value is from the evidence fold."""
import os
D = os.path.dirname(os.path.abspath(__file__))
W = 560

def hbars(rows, maxv, x0=210, bh=22, gap=20, ticks=(), right=70):
    """rows: ('H', heading) or (label, sub, value, cls, value_text)."""
    o = []; y = 30; xw = W - x0 - right
    sx = lambda v: x0 + v / maxv * xw
    ys = []
    for r in rows:
        if r[0] == 'H':
            y += 6
            o.append(f'<text class="c-lab c-s2t" x="0" y="{y+10}">{r[1]}</text>'); y += 24; continue
        lab, sub, v, cls, vtxt = r
        o.append(f'<text class="c-box-t" x="0" y="{y+9}">{lab}</text><text class="c-note" x="0" y="{y+24}">{sub}</text>')
        o.append(f'<rect class="{cls}" x="{x0}" y="{y}" width="{max(2, sx(v)-x0):.1f}" height="{bh}" rx="2"/>')
        o.append(f'<text class="c-lab c-s1t" x="{sx(v)+6:.1f}" y="{y+16}">{vtxt}</text>')
        ys.append(y); y += bh + gap
    top, bot = 18, y - gap + 4
    grid = '<g class="c-grid">' + ''.join(f'<line x1="{sx(t):.1f}" y1="{top}" x2="{sx(t):.1f}" y2="{bot}"/>' for t in ticks) + '</g>'
    axis = '<g class="c-axis">' + ''.join(f'<text x="{sx(t):.1f}" y="12" text-anchor="middle">{t:,g}</text>' for t in ticks) + '</g>'
    o.insert(0, grid + axis)
    o.append(f'<line class="c-base" x1="{x0}" y1="{top}" x2="{x0}" y2="{bot}"/>')
    return ''.join(o), y

def save(name, body, H, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# 1 capacity factors
b, H = hbars([
  ('Nuclear', '94 reactors', 91.1, 'c-bar', '91.1%'),
  ('Gas, combined cycle', 'the efficient kind', 58.7, 'c-bar c-mute', '58.7%'),
  ('Coal', '', 48.8, 'c-bar c-mute', '48.8%'),
  ('Wind', '', 33.8, 'c-bar c-alt', '33.8%'),
  ('Solar', 'utility scale', 24.0, 'c-bar c-alt', '24.0%'),
], 100, ticks=(0, 25, 50, 75, 100))
save('cf-chart', b, H, 'Capacity factor in 2025, the share of the year\'s possible output each kind of plant actually produced. Nuclear 91.1 per cent, gas combined cycle 58.7, coal 48.8, wind 33.8, utility-scale solar 24.0.')

# 2 deals
b, H = hbars([
  ('H', 'Binding contracts'),
  ('Existing reactors', '8 deals, incl. their uprates', 9880, 'c-bar', '9,880 MW'),
  ('New reactors', 'Hermes 2, for Google via TVA', 50, 'c-bar c-alt', 'up to 50 MW'),
  ('H', 'Not contracts to buy power'),
  ('TerraPower, for Meta', 'two units funded; rights to six more', 690, 'c-bar c-mute', 'up to 690 MW'),
  ('Oklo, for Meta', 'prepayment framework', 1200, 'c-bar c-mute', 'up to 1,200 MW'),
  ('Kairos, for Google', 'framework, by 2035', 500, 'c-bar c-mute', '500 MW'),
  ('X-energy, for Amazon', 'target, by 2039', 5000, 'c-bar c-mute', 'more than 5,000 MW'),
], 10000, ticks=(0, 2500, 5000, 7500, 10000), right=40)
save('deals-chart', b, H, 'Megawatts in nuclear deals for AI in America. Binding power purchase agreements on existing reactors and their uprates: 9,880 MW across eight deals. Binding contract on a new reactor: up to 50 MW, Hermes 2. Not contracts to buy power: TerraPower for Meta, two units up to 690 MW funded with rights to six more; Oklo for Meta, a prepayment framework for up to 1,200 MW; Kairos for Google, a 500 MW framework by 2035; X-energy for Amazon, a target of more than 5,000 MW by 2039.')

# 3 cost per kW
b, H = hbars([
  ('H', 'Existing reactors'),
  ('Crane restart', 'US$1.6bn for 835 MW', 1900, 'c-bar', 'about 1,900'),
  ('Palisades restart', 'funding available, 800 MW', 2800, 'c-bar', 'about 2,800'),
  ('Duane Arnold restart', 'loan ceiling, 615 MW', 3100, 'c-bar', 'up to 3,100'),
  ('Google\'s uprates', 'US$4.3bn for 890 MW', 4800, 'c-bar', 'about 4,800'),
  ('H', 'A new large reactor'),
  ('Vogtle 3 and 4', 'about US$31bn for 2,234 MW', 14000, 'c-bar c-alt', 'about 14,000'),
], 16000, ticks=(0, 5000, 10000, 15000), right=60)
save('cost-chart', b, H, 'Capital cost in US dollars per kilowatt, my arithmetic. Crane restart about 1,900; Palisades restart about 2,800 on the funding available; Duane Arnold restart up to 3,100 at the loan ceiling; Google\'s uprates at Constellation about 4,800; Vogtle units 3 and 4, a new large reactor, about 14,000.')

# 4 separative work
b, H = hbars([
  ('H', 'Bought by American reactor owners, 2025'),
  ('From Russia', 'ends by the close of 2027', 3.28, 'c-bar', '3.28m SWU, 26%'),
  ('From American plants', '', 2.93, 'c-bar c-mute', '2.93m SWU, 23%'),
  ('H', 'New capacity coming, a year'),
  ('Urenco, Eunice', 'expansion, by spring 2027', 0.70, 'c-bar c-alt', '0.7m'),
  ('Urenco, Eunice', 'new plant, from 2032', 2.1, 'c-bar c-alt', '2.1m'),
  ('Orano, Oak Ridge', 'initial, early 2030s', 4.0, 'c-bar c-alt', '4.0m'),
], 5, ticks=(0, 1, 2, 3, 4, 5), right=110)
save('swu-chart', b, H, 'Millions of separative work units. In 2025 American reactor owners bought 3.28 million from Russia, 26 per cent of 12.71 million, and 2.93 million, 23 per cent, from American plants. New capacity a year: Urenco\'s Eunice expansion 0.7 million by spring 2027; Urenco\'s new plant 2.1 million from 2032; Orano at Oak Ridge 4.0 million initially in the early 2030s. Centrus\'s Piketon expansion starts in 2029 with no capacity figure published.')

# 5 the ladder: what reaches the grid, by date
b, H = hbars([
  ('H', 'Ordinary fuel, existing reactors'),
  ('Crane restart', 'second half of 2027', 835, 'c-bar', '835 MW, 2027'),
  ('Duane Arnold restart', 'first quarter 2029 at the latest', 615, 'c-bar', '615 MW, by early 2029'),
  ('Palisades restart', 'no date since September 2026', 800, 'c-bar', '800 MW, no date'),
  ('AI-funded uprates', 'in steps, 2028 to 2034', 1639, 'c-bar', 'about 1,640 MW'),
  ('H', 'HALEU, new reactors'),
  ('Aurora-ID, Oklo', '2028 to 2029', 75, 'c-bar c-alt', '75 MW'),
  ('Kemmerer 1, TerraPower', '2030', 345, 'c-bar c-alt', '345 MW'),
  ('Hermes 2, Kairos', '2030', 50, 'c-bar c-alt', 'up to 50 MW'),
], 2000, ticks=(0, 500, 1000, 1500, 2000), right=110)
save('ladder', b, H, 'Megawatts and the date each owner gives. Ordinary fuel on existing reactors: Crane restart 835 MW, second half of 2027; Duane Arnold restart 615 MW, first quarter 2029 at the latest; Palisades restart 800 MW, no date; AI-funded uprates about 1,640 MW in steps from 2028 to 2034. HALEU on new reactors: Aurora-ID 75 MW, 2028 to 2029; Kemmerer 1 345 MW, 2030; Hermes 2 up to 50 MW, 2030.')

# 6 Crane's grid timeline
x0, x1, y0 = 200, 540, 2024
X = lambda t: x0 + (t - y0) / (2032 - y0) * (x1 - x0)
o = []
o.append('<g class="c-grid">' + ''.join(f'<line x1="{X(t):.1f}" y1="30" x2="{X(t):.1f}" y2="150"/>' for t in range(2024, 2033, 2)) + '</g>')
o.append('<g class="c-axis">' + ''.join(f'<text x="{X(t):.1f}" y="168" text-anchor="middle">{t}</text>' for t in range(2024, 2033, 2)))
rows = [('The reactor itself', 54), ('Full grid delivery, fresh request', 96), ('With Eddystone\'s 760 MW', 138)]
o.append(''.join(f'<text x="188" y="{y+4}" text-anchor="end">{t}</text>' for t, y in rows) + '</g>')
s = X(2024 + 8.6/12)   # announced 20 September 2024
o.append(f'<line class="c-today" x1="{X(2026+5/12):.1f}" y1="30" x2="{X(2026+5/12):.1f}" y2="150"/><text class="c-today-t" x="{X(2026+5/12):.1f}" y="24" text-anchor="middle">FERC waiver, 1 June 2026</text>')
o.append(f'<g class="c-span"><line x1="{s:.1f}" y1="54" x2="{X(2027.75):.1f}" y2="54"/><line x1="{s:.1f}" y1="96" x2="{X(2031.0):.1f}" y2="96"/></g>')
o.append(f'<g class="c-span"><line x1="{X(2026+5/12):.1f}" y1="138" x2="{X(2030.9):.1f}" y2="138" style="stroke-dasharray:4 4"/></g><g class="c-start"><circle cx="{X(2026+5/12):.1f}" cy="138" r="4"/></g>')
o.append(f'<g class="c-start"><circle cx="{s:.1f}" cy="54" r="4"/><circle cx="{s:.1f}" cy="96" r="4"/></g>')
o.append(f'<g class="c-end"><circle cx="{X(2027.75):.1f}" cy="54" r="4.5"/><circle cx="{X(2031.0):.1f}" cy="96" r="4.5"/></g>')
o.append(f'<g class="c-endt"><text x="{X(2027.75)+9:.1f}" y="58">second half 2027</text><text x="{X(2031.0)-8:.1f}" y="84" text-anchor="end">at risk to the end of 2030</text><text x="{X(2026+5/12)+6:.1f}" y="128">potentially sooner; PJM\'s studies decide</text></g>')
save('crane-chart', ''.join(o), 176, 'Timeline for Crane, from its announcement in September 2024. The reactor itself can run in the second half of 2027. Constellation told FERC that full delivery through a fresh grid request could be at risk until the end of 2030, on its reading of PJM\'s first study. FERC\'s waiver of 1 June 2026 lets 760 MW of rights move from Eddystone, which could potentially bring full delivery sooner, but PJM\'s studies decide.')

# 7 the three restarts: milestones
x0, x1 = 120, 420; t0, t1 = 2019, 2031
X = lambda t: x0 + (t - t0) / (t1 - t0) * (x1 - x0)
o = []
o.append('<g class="c-grid">' + ''.join(f'<line x1="{X(t):.1f}" y1="26" x2="{X(t):.1f}" y2="196"/>' for t in range(2019, 2032, 2)) + '</g>')
o.append('<g class="c-axis">' + ''.join(f'<text x="{X(t):.1f}" y="214" text-anchor="middle">{t}</text>' for t in range(2019, 2032, 2)) + '</g>')
R = [  # name, y, closed, first filing, approval or target, power, power label, deadline, deadline label
  ('Crane', 52, 2019 + 8.6/12, 2024 + 10/12, 2027 + 2/12, 2027.75, 'power, second half 2027', None, None),
  ('Palisades', 112, 2022 + 4.6/12, 2023 + 1/12, 2025 + 6.8/12, None, 'no date', 2027 + 2/12, 'contract deadline, March 2027'),
  ('Duane Arnold', 172, 2020 + 7.3/12, 2025 + 0.8/12, None, 2029.2, 'by Q1 2029', 2030.0, 'grid deadline, end 2029'),
]
for name, y, c, f, ap, pw, pl, dl, dll in R:
    o.append(f'<text class="c-box-t" x="0" y="{y+4}">{name}</text>')
    o.append(f'<line class="c-line c-mute" x1="{X(c):.1f}" y1="{y}" x2="{X(f):.1f}" y2="{y}" style="stroke-dasharray:2 4"/>')
    o.append(f'<circle class="c-dot" cx="{X(c):.1f}" cy="{y}" r="4" style="fill:var(--ink-3)"/><text class="c-note" x="{X(c):.1f}" y="{y-10}" text-anchor="middle">closed</text>')
    end = ap if ap else (pw if pw else f)
    o.append(f'<g class="c-span"><line x1="{X(f):.1f}" y1="{y}" x2="{X(end):.1f}" y2="{y}"/></g><g class="c-start"><circle cx="{X(f):.1f}" cy="{y}" r="4"/></g>')
    o.append(f'<text class="c-note" x="{X(f):.1f}" y="{y+20}" text-anchor="middle">NRC filing</text>')
    if ap:
        o.append(f'<text class="c-note" x="{X(ap):.1f}" y="{y-10}" text-anchor="middle">{"NRC approval" if name == "Palisades" else "NRC target"}</text>')
    if pw:
        o.append(f'<line class="c-span" x1="{X(end):.1f}" y1="{y}" x2="{X(pw):.1f}" y2="{y}" style="stroke-dasharray:4 4"/><g class="c-end"><circle cx="{X(pw):.1f}" cy="{y}" r="4.5"/></g><g class="c-endt"><text x="{X(max(pw, dl or 0))+10:.1f}" y="{y+4}">{pl}</text></g>')
    else:
        o.append(f'<g class="c-endt"><text x="{X(max(end, dl or 0))+10:.1f}" y="{y+4}">{pl}</text></g>')
    if dl:
        o.append(f'<line class="c-today" x1="{X(dl):.1f}" y1="{y-16}" x2="{X(dl):.1f}" y2="{y+16}"/><text class="c-today-t" x="{X(dl):.1f}" y="{y+30}" text-anchor="middle">{dll}</text>')
save('restarts', ''.join(o), 222, 'Milestones of the three restarts. Crane closed in September 2019, filed with the NRC from November 2024, has an NRC target of 4 March 2027 and expects power in the second half of 2027. Palisades closed in May 2022, filed from February 2023, won NRC approval in July 2025, and has no date since its fuel loading stopped; its contracts and grid place run to 1 March 2027. Duane Arnold closed in August 2020, filed from January 2025, expects power by the first quarter of 2029, and must run by 31 December 2029 to keep its grid place.')
print('charts ok')
