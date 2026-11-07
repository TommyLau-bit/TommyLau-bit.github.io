"""Unit chart: each square is 20 MWe, the top of the microreactor range."""
rows = [  # label, sub, MWe, class
 ('A large reactor', 'one Vogtle unit, Georgia', 1114, 'c-bar c-mute'),
 ('A 1 GW AI campus', 'what large AI sites now plan', 1000, 'c-bar c-alt'),
 ('A small modular reactor', 'GE Vernova BWRX-300', 300, 'c-bar c-mute'),
 ('The largest microreactor', 'top of the 1 to 20 MWe range', 20, 'c-bar'),
 ('Project Pele', 'the Pentagon’s prototype, 1.5 MWe', 1.5, 'c-bar'),
]
W = 560; sq = 11; gap = 2; per = 21; x0 = 186
o = []; y = 16
for lab, sub, mw, cls in rows:
    n = mw / 20
    full = int(n); frac = n - full
    rws = max(1, -(-int(n + 0.999) // per))
    o.append(f'<text class="c-box-t" x="0" y="{y+10}">{lab}</text><text class="c-note" x="0" y="{y+25}">{sub}</text>')
    for k in range(full):
        r, c = divmod(k, per)
        o.append(f'<rect class="{cls}" x="{x0+c*(sq+gap)}" y="{y+r*(sq+gap)}" width="{sq}" height="{sq}" rx="1.5"/>')
    if frac > 0.01:
        r, c = divmod(full, per)
        o.append(f'<rect class="{cls}" x="{x0+c*(sq+gap)}" y="{y+r*(sq+gap)}" width="{max(1.2, sq*frac):.1f}" height="{sq}" rx="0.5"/>')
        if full == 0: o.append(f'<rect x="{x0}" y="{y}" width="{sq}" height="{sq}" rx="1.5" style="fill:none;stroke:var(--ink-3);stroke-dasharray:2 2"/>')
    mwtxt = f'{mw:,.0f} MWe' if mw >= 2 else f'{mw} MWe'
    lastx = x0 + (min(per, max(1, int(n + 0.999))) ) * (sq + gap) + 6
    o.append(f'<text class="c-lab c-s1t" x="{W-2}" y="{y+10}" text-anchor="end">{mwtxt}</text>')
    y += max(rws * (sq + gap), 26) + 18
H = y
svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Each square is 20 megawatts of electricity, the top of the microreactor range. One Vogtle unit, 1,114 MWe, is about 56 squares. A 1 gigawatt AI campus is 50 squares. A BWRX-300 small modular reactor is 15. The largest microreactor is one square. Project Pele, 1.5 MWe, is less than a tenth of one square.">' + ''.join(o) + '</svg>'
open('illos/size-chart.svg','w').write(svg)
