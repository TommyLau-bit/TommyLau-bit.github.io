"""The fuel chain from mine to microreactor: seven drawn stages, who does each in the US,
and where it pinches. Labels in LAB are filled from the research files."""
import json, math
LAB = json.load(open('chain_labels.json'))
W, H = 940, 420
o = []; a = o.append
a('<defs><marker id="ch" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" style="fill:var(--ink-3)"/></marker></defs>')
X = [20 + i * 132 for i in range(7)]
base = 250
a(f'<rect class="i-ground" x="0" y="{base}" width="{W}" height="18"/><line class="i-line" x1="0" y1="{base}" x2="{W}" y2="{base}"/>')
# choke zone: one band over the consecutive choke steps
c0, c1 = min(LAB['choke']), max(LAB['choke'])
a(f'<rect class="i-choke" x="{X[c0]-8}" y="84" width="{X[c1]-X[c0]+128}" height="{base+150-84}" rx="6"/>')
a(f'<text class="i-hot-t" x="{X[c0]}" y="100" style="font-size:10.5px;letter-spacing:.08em">THE CHOKE POINTS</text>')
for i in range(6):
    a(f'<line class="i-lead" x1="{X[i]+114}" y1="{base-40}" x2="{X[i+1]-4}" y2="{base-40}" marker-end="url(#ch)"/>')
# 1 mine: open pit terraces + truck
x = X[0]
a(f'<path class="i-fill" d="M{x} {base} L{x+18} {base-14} H{x+96} L{x+112} {base} Z"/><path class="i-thin" d="M{x+24} {base-6} H{x+90} M{x+34} {base-11} H{x+82}"/>')
a(f'<path class="i-line" d="M{x+30} {base-40} h28 v-14 h-12 l-6 -8 h-10 z"/><circle class="i-fill" cx="{x+36}" cy="{base-38}" r="4"/><circle class="i-fill" cx="{x+52}" cy="{base-38}" r="4"/>')
a(f'<circle class="i-fuel" cx="{x+76}" cy="{base-26}" r="4" opacity=".5"/><circle class="i-fuel" cx="{x+84}" cy="{base-30}" r="3" opacity=".5"/>')
# 2 convert: chemical plant towers
x = X[1]
for k, (w, h) in enumerate([(18, 90), (14, 70), (22, 55)]):
    a(f'<rect class="i-fill" x="{x+12+k*30}" y="{base-h}" width="{w}" height="{h}"/>')
a(f'<path class="i-thin" d="M{x+20} {base-90} v-10 M{x+46} {base-70} q 6 -8 0 -16 q -6 -8 0 -16" opacity=".6"/><rect class="i-fill" x="{x+8}" y="{base-26}" width="96" height="26"/>')
# 3 enrich: rows of centrifuges
x = X[2]
a(f'<rect class="i-metal" x="{x+2}" y="{base-120}" width="108" height="120" rx="2"/>')
for r in range(2):
    for c in range(8):
        cx_, top = x + 12 + c * 12.5, base - 112 + r * 56
        a(f'<rect class="i-fill" x="{cx_}" y="{top}" width="7" height="46" rx="3.5"/>')

# 4 deconvert: furnace + powder
x = X[3]
a(f'<rect class="i-fill" x="{x+14}" y="{base-80}" width="50" height="80" rx="3"/><path class="i-hot" d="M{x+28} {base-30} q 4 -10 0 -18 M{x+42} {base-30} q 4 -10 0 -18"/>')
a(f'<path class="i-fill" d="M{x+74} {base} l14 -24 h12 l14 24 z"/><circle class="i-fuel" cx="{x+94}" cy="{base-8}" r="6" opacity=".7"/>')
# 5 TRISO: fluidised bed coater (tall vessel) with particles
x = X[4]
a(f'<path class="i-fill" d="M{x+40} {base} V{base-110} q 16 -18 32 0 V{base} Z"/>')
for k in range(14):
    a(f'<circle class="i-fuel" cx="{x+46+(k*7)%20:.0f}" cy="{base-30-(k*13)%70:.0f}" r="2.4"/>')
a(f'<path class="i-cool" d="M{x+30} {base-8} H{x+40}"/><path class="i-thin" d="M{x+56} {base-128} v-12"/>')
# 6 ship: truck with cask
x = X[5]
a(f'<rect class="i-fill" x="{x+6}" y="{base-34}" width="100" height="12" rx="2"/><rect class="i-metal" x="{x+18}" y="{base-70}" width="64" height="36" rx="14"/>')
a(f'<path class="i-line" d="M{x+6} {base-34} v-22 h-0"/>')
for wx in (x+20, x+40, x+86): a(f'<circle class="i-fill" cx="{wx}" cy="{base-14}" r="8"/>')
# 7 reactor: small module
x = X[6]
a(f'<rect class="i-metal" x="{x+20}" y="{base-96}" width="70" height="96" rx="3"/><rect class="i-fuel-soft" x="{x+38}" y="{base-70}" width="34" height="42" rx="3"/>')
# stage labels
for i, st in enumerate(LAB['stages']):
    x = X[i]
    a(f'<text class="i-k" x="{x}" y="{base+20}">Step {i+1}</text>')
    a(f'<text class="i-t" x="{x}" y="{base+36}">{st["name"]}</text>')
    for k, line in enumerate(st['what']): a(f'<text class="i-n" x="{x}" y="{base+52+k*14}">{line}</text>')
    yy = base + 52 + len(st['what'])*14 + 10
    for k, line in enumerate(st['who']): a(f'<text class="{"i-hot-t" if i in LAB["choke"] else "i-n2"}" x="{x}" y="{yy+k*14}" style="font-size:11.5px">{line}</text>')
# Russia crossed out over enrichment and government stock bypass
x = X[2]
a(f'<text class="i-n" x="{X[1]}" y="44">{LAB["russia"][0]}</text><text class="i-n" x="{X[1]}" y="58">{LAB["russia"][1]}</text><path class="i-lead" d="M{X[2]+56} 62 V{base-124}"/>')
a(f'<path class="i-dash" d="M{X[1]+60} 118 C {X[1]+60} 96, {X[3]+40} 96, {X[3]+40} 128" style="stroke:var(--fuel)"/>' if False else '')
gx = X[3]
a(f'<path class="i-dash" d="M{gx+56} 64 V{base-88}" style="stroke:var(--fuel)" marker-end="url(#ch)"/>')
a(f'<text class="i-fuel-t" x="{gx+56}" y="44" text-anchor="middle">{LAB["govt"][0]}</text><text class="i-n" x="{gx+56}" y="58" text-anchor="middle">{LAB["govt"][1]}</text>')
svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{LAB["aria"]}">' + ''.join(x for x in o if x) + '</svg>'
open('illos/chain.svg', 'w').write(svg)
