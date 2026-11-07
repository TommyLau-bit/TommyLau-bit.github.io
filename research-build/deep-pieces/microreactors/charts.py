def hbars(rows, maxv, unit, W=560, x0=200, bh=22, gap=20, ticks=()):
    o = []; y = 30; xw = W - x0 - 60
    sx = lambda v: x0 + v / maxv * xw
    o.append('<g class="c-grid">' + ''.join(f'<line x1="{sx(t):.1f}" y1="18" x2="{sx(t):.1f}" y2="{30+len(rows)*(bh+gap)-gap+4}"/>' for t in ticks) + '</g>')
    o.append('<g class="c-axis">' + ''.join(f'<text x="{sx(t):.1f}" y="12" text-anchor="middle">{t:g}</text>' for t in ticks) + '</g>')
    for lab, sub, lo, hi, cls, vtxt in rows:
        o.append(f'<text class="c-box-t" x="0" y="{y+9}">{lab}</text><text class="c-note" x="0" y="{y+24}">{sub}</text>')
        o.append(f'<rect class="{cls}" x="{sx(lo):.1f}" y="{y}" width="{max(2, sx(hi)-sx(lo)):.1f}" height="{bh}" rx="2"/>')
        o.append(f'<text class="c-lab c-s1t" x="{sx(hi)+6:.1f}" y="{y+16}">{vtxt}</text>')
        y += bh + gap
    o.append(f'<line class="c-base" x1="{x0}" y1="18" x2="{x0}" y2="{y-gap+4}"/>')
    return o, y
o, H = hbars([
  ('Government stock', 'released by 2028 (DOE to GAO)', 0, 21.2, 'c-bar c-alt', '21.2'),
  ('New production contracted', 'Centrus task order, by July 2032', 0, 1, 'c-bar c-alt', '1'),
  ('Needed by 2030', 'DOE, "more than 40 tonnes"', 0, 40, 'c-bar', '40+'),
  ('Needed each year by 2035', 'DOE estimate', 0, 50, 'c-bar c-mute', '~50 a year'),
], 55, 't', ticks=(0, 10, 20, 30, 40, 50))
open('illos/haleu-chart.svg','w').write(f'<svg viewBox="0 0 560 {H}" role="img" aria-label="Tonnes of HALEU. Government stock released by 2028: about 21.2 tonnes. New production under contract: 1 tonne by July 2032. Needed by 2030 according to the Energy Department: more than 40 tonnes. Needed each year by 2035: about 50 tonnes.">' + ''.join(o) + '</svg>')
o, H = hbars([
  ('Grid, industrial', 'US average, 2025 (EIA)', 0, 8.62, 'c-bar c-mute', '8.6'),
  ('Grid, commercial', 'US average, 2025 (EIA)', 0, 13.41, 'c-bar c-mute', '13.4'),
  ('Microreactor, mass-produced', 'INL estimate', 11.9, 15, 'c-bar', '12 to 15'),
  ('Microreactor, first of a kind', 'INL estimate', 0, 32.5, 'c-bar', '32.5'),
  ('Remote site on diesel', 'INL, citing NEI', 15, 60, 'c-bar c-alt', '15 to 60'),
], 66, 'c', ticks=(0, 10, 20, 30, 40, 50, 60))
open('illos/price-chart.svg','w').write(f'<svg viewBox="0 0 560 {H}" role="img" aria-label="US cents per kilowatt-hour. Grid power, industrial average 2025: 8.6. Grid power, commercial average 2025: 13.4. Mass-produced microreactor, INL estimate: 12 to 15. First-of-a-kind microreactor, INL estimate: 32.5. Remote site on diesel generators, INL citing NEI: 15 to 60.">' + ''.join(o) + '</svg>')
