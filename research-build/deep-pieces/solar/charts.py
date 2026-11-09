"""Charts for the solar and batteries piece. Every value is a sourced figure (see the evidence fold).
Writes illos/<name>.svg. Classes only, no inline colours (dark mode)."""
import os
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, 'illos')
os.makedirs(OUT, exist_ok=True)
def save(name, s): open(os.path.join(OUT, name + '.svg'), 'w').write(s)
f = lambda v: f'{v:.1f}'

# 1 · monthly capacity factor, 2025: solar against nuclear (EIA EPM Table 6.07.B, 23 Oct 2026)
months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
solar = [16.2, 18.7, 23.6, 27.5, 29.3, 31.9, 31.9, 29.7, 26.7, 22.4, 16.9, 13.1]
nuke = [98.3, 93.6, 85.4, 81.8, 84.9, 93.4, 96.7, 96.6, 92.4, 81.0, 90.2, 99.2]
W, H, L, R, T, B = 560, 270, 52, 470, 20, 232
x = lambda i: L + i * (R - L) / 11
y = lambda v: B - v / 100 * (B - T)
s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Monthly capacity factor in 2025. Solar: ' + ', '.join(f'{m} {v}' for m, v in zip(months, solar)) + ' per cent. Nuclear: ' + ', '.join(f'{m} {v}' for m, v in zip(months, nuke)) + ' per cent.">']
s.append('<g class="c-grid">' + ''.join(f'<line x1="{L}" y1="{f(y(v))}" x2="{R}" y2="{f(y(v))}"/>' for v in (25, 50, 75, 100)) + '</g>')
s.append('<g class="c-axis">' + ''.join(f'<text x="{L-8}" y="{f(y(v)+4)}" text-anchor="end">{v}%</text>' for v in (0, 25, 50, 75, 100)) + ''.join(f'<text x="{f(x(i))}" y="{B+20}" text-anchor="middle">{m}</text>' for i, m in enumerate(months)) + '</g>')
s.append(f'<line class="c-base" x1="{L}" y1="{B}" x2="{R}" y2="{B}"/>')
for vals, cls in ((nuke, 'c-s1'), (solar, 'c-s2')):
    s.append(f'<polyline class="c-line {cls}" points="' + ' '.join(f'{f(x(i))},{f(y(v))}' for i, v in enumerate(vals)) + '"/>')
    s.append(f'<circle class="c-dot {cls}" cx="{f(x(11))}" cy="{f(y(vals[11]))}" r="3.5"/>')
s.append(f'<text class="c-lab c-s1t" x="{R+8}" y="{f(y(99.2)+4)}">Nuclear</text><text class="c-lab c-s1t" x="{R+8}" y="{f(y(99.2)+20)}">99.2% in Dec</text>')
s.append(f'<text class="c-lab c-s2t" x="{R+8}" y="{f(y(13.1)-8)}">Solar</text><text class="c-lab c-s2t" x="{R+8}" y="{f(y(13.1)+8)}">13.1% in Dec</text>')
s.append('</svg>'); save('cf-month', ''.join(s))

# 2 · PJM ELCC class ratings for the 2029/2030 BRA (posted 7 Aug 2026)
rows = [('Nuclear', 96, 'c-alt'), ('Gas, combined cycle', 75, 'c-alt'), ('Battery, 4 hours', 57, ''), ('Onshore wind', 37, 'c-mute'), ('Solar, tracking', 7, ''), ('Solar, fixed', 6, '')]
W, L, R, T, rh = 560, 170, 500, 26, 34
H = T + rh * len(rows) + 14
xv = lambda v: L + v / 100 * (R - L)
s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Share of each megawatt PJM counts as firm capacity for the 2029/2030 auction: ' + '; '.join(f'{n} {v} per cent' for n, v, _ in rows) + '.">']
s.append('<g class="c-grid">' + ''.join(f'<line x1="{f(xv(v))}" y1="{T-6}" x2="{f(xv(v))}" y2="{H-10}"/>' for v in (25, 50, 75, 100)) + '</g>')
s.append('<g class="c-axis">' + ''.join(f'<text x="{f(xv(v))}" y="{T-12}" text-anchor="middle">{v}%</text>' for v in (0, 25, 50, 75, 100)) + '</g>')
for i, (n, v, cls) in enumerate(rows):
    yy = T + i * rh
    s.append(f'<text class="c-note" x="{L-10}" y="{yy+17}" text-anchor="end">{n}</text>')
    s.append(f'<rect class="{("c-bar " + cls).strip()}" x="{L}" y="{yy+4}" width="{f(xv(v)-L)}" height="20"/>')
    s.append(f'<text class="c-note" x="{f(xv(v)+6)}" y="{yy+18}">{v}%</text>')
s.append(f'<line class="c-base" x1="{L}" y1="{T-6}" x2="{L}" y2="{H-10}"/>')
s.append('</svg>'); save('elcc-bars', ''.join(s))

# 3 · the climax: ratings over delivery years. Final BRA ratings 2025/26 to 2029/30;
# PJM's preliminary, non-binding ratings for 2030/31 onwards (4 Sep 2026). Solar's
# preliminary values are given only as a 7 to 10% band, so solar is drawn to 2029/30 only.
years = ['25/26', '26/27', '27/28', '28/29', '29/30', '30/31', '31/32', '32/33', '33/34', '34/35', '35/36']
stor = [59, 50, 58, 59, 57, 42, 34, 30, 26, 24, 23]
trk = [14, 11, 8, 10, 7, 8, 8, 7, 7, 8, 8]
nuc = [95, 95, 95, 96, 96]
W, H, L, R, T, B = 560, 290, 46, 470, 22, 246
xi = lambda i: L + i * (R - L) / (len(years) - 1)
y = lambda v: B - v / 100 * (B - T)
s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Share of a megawatt PJM counts as firm, by delivery year. Four-hour battery, final ratings: ' + ', '.join(f'{a} {b}' for a, b in zip(years[:5], stor[:5])) + '; preliminary: ' + ', '.join(f'{a} {b}' for a, b in zip(years[5:], stor[5:])) + ', and 19 by 2042/43. Tracking solar, final then preliminary: ' + ', '.join(f'{a} {b}' for a, b in zip(years, trk)) + '. Nuclear, final: ' + ', '.join(f'{a} {b}' for a, b in zip(years, nuc)) + ' per cent.">']
s.append(f'<rect class="c-zone" x="{f(xi(4.5))}" y="{T}" width="{f(xi(10)-xi(4.5))}" height="{B-T}"/>')
s.append(f'<text class="c-zone-t" x="{f(xi(7.5))}" y="{f(y(70))}" text-anchor="middle">PJM\'s preliminary ratings</text>')
s.append('<g class="c-grid">' + ''.join(f'<line x1="{L}" y1="{f(y(v))}" x2="{R}" y2="{f(y(v))}"/>' for v in (25, 50, 75, 100)) + '</g>')
s.append('<g class="c-axis">' + ''.join(f'<text x="{L-8}" y="{f(y(v)+4)}" text-anchor="end">{v}%</text>' for v in (0, 25, 50, 75, 100)) + ''.join(f'<text x="{f(xi(i))}" y="{B+18}" text-anchor="middle">{a}</text>' for i, a in enumerate(years) if i % 2 == 0) + '</g>')
s.append(f'<line class="c-base" x1="{L}" y1="{B}" x2="{R}" y2="{B}"/>')
for vals, cls in ((nuc, 'c-s1'), (stor, 'c-s3'), (trk, 'c-s2')):
    s.append(f'<polyline class="c-line {cls}" points="' + ' '.join(f'{f(xi(i))},{f(y(v))}' for i, v in enumerate(vals)) + '"/>')
    s.append(f'<circle class="c-dot {cls}" cx="{f(xi(len(vals)-1))}" cy="{f(y(vals[-1]))}" r="3.5"/>')
s.append(f'<text class="c-lab c-s1t" x="{f(xi(4)+8)}" y="{f(y(96)+4)}">Nuclear 96%</text>')
s.append(f'<text class="c-lab c-s3t" x="{R+8}" y="{f(y(23)-6)}">4-hour</text><text class="c-lab c-s3t" x="{R+8}" y="{f(y(23)+10)}">battery 23%</text>')
s.append(f'<text class="c-lab c-s2t" x="{R+8}" y="{f(y(8)-2)}">Tracking</text><text class="c-lab c-s2t" x="{R+8}" y="{f(y(8)+14)}">solar 8%</text>')
s.append('</svg>'); save('elcc-years', ''.join(s))

# 4 · a winter weekday, schematic: the data centre's flat load against the solar day and a 4-hour battery.
# Load 83 to 86% of peak is read off the CEC's chart (12 Aug 2026, slide 10, winter weekday). The solar
# and battery shapes are a drawing, not data.
W, H, L, R, T, B = 560, 260, 46, 520, 30, 214
xh = lambda h: L + h / 24 * (R - L)
y = lambda v: B - v / 175 * (B - T)
import math
sun = [(h, max(0.0, math.sin(math.pi * (h - 7.5) / 9)) * 140 if 7.5 <= h <= 16.5 else 0.0) for h in [i / 4 for i in range(97)]]
s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Schematic of a winter weekday. A data centre draws 83 to 86 per cent of its peak every hour. Solar produces only between about 7:30 and 16:30. Solar is drawn larger than the load, and its midday surplus charges a four-hour battery, which covers 16:30 to 20:30. From about 20:30 to 7:30, eleven hours, neither covers the load.">']
s.append(f'<rect class="c-zone" x="{f(xh(20.5))}" y="{T}" width="{f(xh(24)-xh(20.5))}" height="{B-T}"/><rect class="c-zone" x="{f(xh(0))}" y="{T}" width="{f(xh(7.5)-xh(0))}" height="{B-T}"/>')
s.append(f'<text class="c-zone-t" x="{f(xh(3.75))}" y="{B-10}" text-anchor="middle">Night gap</text><text class="c-zone-t" x="{f(xh(22.25))}" y="{B-10}" text-anchor="middle">Night</text>')
s.append('<path class="c-bar" d="M' + ' L'.join(f'{f(xh(h))},{f(y(v))}' for h, v in sun) + f' L{f(xh(24))},{B} L{f(xh(0))},{B} Z" opacity=".55"/>')
surplus = [(h, v) for h, v in sun if v > 84.5]
s.append('<path class="c-bar c-alt" d="M' + ' L'.join(f'{f(xh(h))},{f(y(v))}' for h, v in surplus) + f' L{f(xh(surplus[-1][0]))},{f(y(84.5))} L{f(xh(surplus[0][0]))},{f(y(84.5))} Z" opacity=".6"/>')
s.append(f'<text class="c-lab c-s3t" x="{f(xh(12))}" y="{f(y(146))}" text-anchor="middle">Midday surplus charges the battery</text>')
s.append(f'<rect class="c-bar c-alt" x="{f(xh(16.5))}" y="{f(y(84.5))}" width="{f(xh(20.5)-xh(16.5))}" height="{f(B-y(84.5))}" opacity=".6"/>')
s.append(f'<line class="c-line c-s1" x1="{L}" y1="{f(y(84.5))}" x2="{R}" y2="{f(y(84.5))}"/>')
s.append('<g class="c-axis">' + ''.join(f'<text x="{f(xh(h))}" y="{B+18}" text-anchor="middle">{h:02d}:00</text>' for h in (0, 6, 12, 18, 24)) + '</g>')
s.append(f'<line class="c-base" x1="{L}" y1="{B}" x2="{R}" y2="{B}"/>')
s.append(f'<text class="c-lab c-s1t" x="{f(xh(3.75))}" y="{f(y(84.5)+18)}" text-anchor="middle">Data centre load</text><text class="c-lab c-s1t" x="{f(xh(3.75))}" y="{f(y(84.5)+34)}" text-anchor="middle">83 to 86% of peak</text>')
s.append(f'<text class="c-lab c-s2t" x="{f(xh(12))}" y="{f(y(40))}" text-anchor="middle">Solar</text>')
s.append(f'<text class="c-lab c-s3t" x="{f(xh(18.5))}" y="{f(y(45))}" text-anchor="middle">4-hour</text><text class="c-lab c-s3t" x="{f(xh(18.5))}" y="{f(y(45)+16)}" text-anchor="middle">battery</text>')
s.append('</svg>'); save('winter-day', ''.join(s))
print('ok', sorted(os.listdir(OUT)))
