"""The booking staircase for an illustrative 100 MW campus: booked (final maximum demand),
declared (the step for each year), drawn (what flows), and the connected load charge lines
from Tenaga's Connection Charge Book 2025 (85% of the declared step in years 1 to 4,
75% of final maximum demand in years 5 and 6). Numbers are illustrative, not a real site."""
import os
D = os.path.dirname(os.path.abspath(__file__))
W, H = 940, 430
x0, x1, y0, y1 = 70, 620, 370, 60          # plot box: years 0..6, MW 0..110
X = lambda yr: x0 + (x1 - x0) * yr / 6
Y = lambda mw: y0 - (y0 - y1) * mw / 110
declared = [20, 40, 60, 80, 100, 100]
line = [0.85 * d for d in declared[:4]] + [75, 75]
drawn = [(0, 0), (0.5, 6), (1, 11), (1.5, 17), (2, 23), (2.5, 30), (3, 37), (3.5, 44), (4, 50), (4.5, 56), (5, 61), (5.5, 66), (6, 70)]
o = []; a = o.append
# axes
a(f'<line class="i-line" x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}"/><line class="i-line" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1-10}"/>')
for mw in (0, 25, 50, 75, 100):
    a(f'<text class="i-n" x="{x0-10}" y="{Y(mw)+4}" text-anchor="end">{mw}</text><line class="i-faint" x1="{x0}" y1="{Y(mw)}" x2="{x1}" y2="{Y(mw)}"/>')
a(f'<text class="i-k" x="{x0-10}" y="{y1-22}" text-anchor="end">MW</text>')
for yr in range(6):
    a(f'<text class="i-n" x="{(X(yr)+X(yr+1))/2}" y="{y0+20}" text-anchor="middle">Year {yr+1}</text>')
# shortfall: shade between drawn and the charge line where drawn is below it (sampled per half year)
pts_top, pts_bot = [], []
for i in range(12):
    t0, t1 = i / 2, (i + 1) / 2
    yr = int(t0)
    lvl = line[yr]
    d0 = drawn[i][1]; d1 = drawn[i + 1][1]
    a(f'<path d="M{X(t0):.1f} {Y(lvl):.1f} L{X(t1):.1f} {Y(lvl):.1f} L{X(t1):.1f} {Y(min(d1,lvl)):.1f} L{X(t0):.1f} {Y(min(d0,lvl)):.1f} Z" style="fill:color-mix(in srgb, var(--hot) 14%, transparent)"/>')
# booked line
a(f'<line class="i-line" x1="{x0}" y1="{Y(100)}" x2="{x1}" y2="{Y(100)}" style="stroke-dasharray:8 4"/>')
# declared staircase
d = f'M{X(0)} {Y(declared[0])}'
for yr in range(6):
    d += f' H{X(yr+1)}' + (f' V{Y(declared[yr+1])}' if yr < 5 else '')
a(f'<path d="{d}" style="fill:none;stroke:var(--fuel);stroke-width:2.4"/>')
# charge line
d = f'M{X(0)} {Y(line[0])}'
for yr in range(6):
    d += f' H{X(yr+1)}' + (f' V{Y(line[yr+1])}' if yr < 5 else '')
a(f'<path class="i-hot" d="{d}" style="stroke-width:1.4;stroke-dasharray:3 3"/>')
# drawn
a('<path class="i-cool" style="stroke-width:2.6" d="M' + ' L'.join(f'{X(t):.1f} {Y(v):.1f}' for t, v in drawn) + '"/>')
# right-hand labels
RX = 650
def lab(y, lines):
    for k, (cls, txt) in enumerate(lines): a(f'<text class="{cls}" x="{RX}" y="{y+k*16}">{txt}</text>')
lab(Y(100) - 6, [('i-t', 'Booked: 100 MW'), ('i-n', 'final maximum demand in the'), ('i-n', 'supply agreement, the whole staircase')])
a(f'<line class="i-lead" x1="{x1+4}" y1="{Y(100)}" x2="{RX-6}" y2="{Y(100)-10}"/>')
lab(Y(80) + 22, [('i-fuel-t', 'Declared: the step for each year'), ('i-n', 'what the campus expects to stand on')])
a(f'<line class="i-lead" x1="{X(4.6)}" y1="{Y(100)+4}" x2="{RX-6}" y2="{Y(80)+18}"/>')
lab(Y(58) + 16, [('i-hot-t', 'Charge line'), ('i-n', '85% of the step, years 1 to 4;'), ('i-n', '75% of final demand, years 5 and 6')])
a(f'<line class="i-lead" x1="{X(5.5)}" y1="{Y(75)}" x2="{RX-6}" y2="{Y(58)+12}"/>')
lab(Y(30) + 10, [('i-cool-t', 'Drawn: what actually flows'), ('i-n', 'Shaded gap below the charge line'), ('i-n', 'is billed at RM8.50 per kW a month')])
a(f'<line class="i-lead" x1="{X(5.8)}" y1="{Y(68)}" x2="{RX-6}" y2="{Y(30)+6}"/>')
a(f'<text class="i-k" x="{x0}" y="{y0+48}">An illustrative 100 MW campus, six years after connection</text>')
aria = ("Illustrative staircase for a 100 megawatt campus over six years. The booked maximum demand is a flat dashed line at 100 MW. "
        "The declared demand steps up each year: 20, 40, 60, 80, then 100 MW. Tenaga's connected load charge line sits at 85 per cent "
        "of each declared step in years one to four and at 75 per cent of the final 100 MW in years five and six. The drawn power "
        "rises from zero to about 70 MW; where it is below the charge line, the shortfall is billed at RM8.50 per kilowatt a month.")
svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">' + ''.join(o) + '</svg>'
open(os.path.join(D, 'illos', 'staircase.svg'), 'w').write(svg)
print('stairs ok')
