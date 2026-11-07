"""Five steps from application to a working hall, with the government's step shaded."""
import os
D = os.path.dirname(os.path.abspath(__file__))
W, H = 940, 400
X = [20 + i * 184 for i in range(5)]
base = 210
o = []; a = o.append
a('<defs><marker id="pc" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" style="fill:var(--ink-3)"/></marker></defs>')
a(f'<rect class="i-ground" x="0" y="{base}" width="{W}" height="14"/><line class="i-line" x1="0" y1="{base}" x2="{W}" y2="{base}"/>')
c = 1
a(f'<rect class="i-choke" x="{X[c]-10}" y="40" width="176" height="{H-48}" rx="6"/>')
a(f'<text class="i-hot-t" x="{X[c]}" y="58" style="font-size:10.5px;letter-spacing:.08em">THE CHOKE POINT</text>')
for i in range(4):
    a(f'<line class="i-lead" x1="{X[i]+150}" y1="{base-60}" x2="{X[i+1]-8}" y2="{base-60}" marker-end="url(#pc)"/>')
# 1 apply: a form on a clipboard
x = X[0]
a(f'<rect class="i-fill" x="{x+40}" y="{base-110}" width="70" height="92" rx="3"/><rect class="i-metal" x="{x+62}" y="{base-116}" width="26" height="10" rx="2"/>')
for k in range(5): a(f'<line class="i-thin" x1="{x+50}" y1="{base-92+k*14}" x2="{x+[98,92,100,86,96][k]}" y2="{base-92+k*14}"/>')
# 2 allocate: a government building with a gate
x = X[1]
a(f'<path class="i-fill" d="M{x+30} {base-96} L{x+80} {base-124} L{x+130} {base-96} Z"/><rect class="i-fill" x="{x+34}" y="{base-96}" width="92" height="8"/>')
for k in range(5): a(f'<rect class="i-fill" x="{x+40+k*18}" y="{base-88}" width="8" height="70"/>')
a(f'<rect class="i-fill" x="{x+28}" y="{base-18}" width="104" height="18"/>')
# 3 book: a contract with a seal
x = X[2]
a(f'<rect class="i-fill" x="{x+44}" y="{base-118}" width="68" height="98" rx="2" transform="rotate(-4 {x+78} {base-70})"/>')
for k in range(4): a(f'<line class="i-thin" x1="{x+54}" y1="{base-98+k*14}" x2="{x+100}" y2="{base-100+k*14}"/>')
a(f'<circle class="i-fuel" cx="{x+96}" cy="{base-36}" r="10" opacity=".8"/>')
# 4 plant: pylon, transformer, cable
x = X[3]
a(f'<path class="i-line" d="M{x+30} {base} L{x+44} {base-120} L{x+58} {base} M{x+34} {base-40} H{x+54} M{x+38} {base-80} H{x+50} M{x+26} {base-104} H{x+62}"/>')
a(f'<rect class="i-metal" x="{x+78}" y="{base-58}" width="54" height="58" rx="3"/>')
for k in range(4): a(f'<line class="i-thin" x1="{x+84+k*12}" y1="{base-52}" x2="{x+84+k*12}" y2="{base-6}"/>')
a(f'<path class="i-thin" d="M{x+62} {base-104} Q {x+90} {base-90} {x+104} {base-58}"/>')
# 5 fill: racks with chips
x = X[4]
for k in range(3):
    a(f'<rect class="i-metal" x="{x+30+k*34}" y="{base-110}" width="28" height="110" rx="2"/>')
    for r in range(6): a(f'<rect class="i-cool-f" x="{x+34+k*34}" y="{base-102+r*16}" width="20" height="6" rx="1" opacity="{.85 if (k < 2 or r < 2) else .15}"/>')
ST = [
 ('Apply', ['The operator asks', 'the utility for', 'supply'], ['Weeks to months']),
 ('Allocate', ['The government says', 'who may plug in'], ['Singapore: only by a call', 'Malaysia: only from the', 'grid\'s spare margin', '(since 28 Oct 2026)']),
 ('Book', ['A supply contract for', 'the finished size,', 'years before it fills'], ['Malaysia: 8.35 GW', 'booked, June 2026']),
 ('Build the plant', ['Substation,', 'transformers, cable'], ['Malaysia: 12 months', 'on the Green Lane;', 'faster delivery', 'now priced']),
 ('Fill', ['Tenants rack their', 'chips, at their', 'own pace'], ['Malaysia draws', 'about 22% of what', 'is connected']),
]
for i, (name, what, note) in enumerate(ST):
    x = X[i]
    a(f'<text class="i-k" x="{x}" y="{base+34}">Step {i+1}</text><text class="i-t" x="{x}" y="{base+52}">{name}</text>')
    for k, t in enumerate(what): a(f'<text class="i-n" x="{x}" y="{base+70+k*15}">{t}</text>')
    yy = base + 70 + len(what) * 15 + 8
    for k, t in enumerate(note): a(f'<text class="{"i-hot-t" if i == c else "i-n2"}" x="{x}" y="{yy+k*15}" style="font-size:12px">{t}</text>')
aria = ("Five steps from application to a working hall. One, apply: the operator asks the utility for supply, weeks to months. "
        "Two, allocate: the government says who may plug in; in Singapore only through a call, in Malaysia only from the grid's spare margin "
        "since 28 October 2026. This is the choke point. Three, book: a supply contract for the finished size, years before it fills; "
        "Malaysia had 8.35 GW booked in June 2026. Four, build the plant: substation, transformers and cable, 12 months on Malaysia's Green Lane, with faster delivery now priced. "
        "Five, fill: tenants rack their chips at their own pace; Malaysia's data centres draw about 22 per cent of what is connected.")
open(os.path.join(D, 'illos', 'chain.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">' + ''.join(o) + '</svg>')
print('chain ok')
