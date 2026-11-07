"""Inside a transportable microreactor: core seen from above (fuel blocks, reflector,
control drums) and the module on a trailer with its helium loop. Generic gas-cooled design."""
import math
W, H = 930, 470
o = []; a = o.append
a('<defs><marker id="ah" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" style="fill:var(--ink-2)"/></marker>'
  '<marker id="ahot" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" style="fill:var(--hot)"/></marker>'
  '<marker id="acool" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" style="fill:var(--cool)"/></marker></defs>')
a('<text class="i-k" x="20" y="28">1 · The core, seen from above</text><text class="i-n" x="20" y="44">simplified, not to scale</text>')
cx, cy = 200, 250
# reflector ring
a(f'<circle class="i-metal" cx="{cx}" cy="{cy}" r="170"/>')
a(f'<circle class="i-fill" cx="{cx}" cy="{cy}" r="108" style="fill:var(--bg)"/>')
# hex fuel blocks: 19 small hexes
s = 22
def hexpts(x, y, r):
    return ' '.join(f'{x+r*math.cos(math.radians(60*i)):.1f},{y+r*math.sin(math.radians(60*i)):.1f}' for i in range(6))
cells = []
for q in range(-2, 3):
    for r_ in range(-2, 3):
        if abs(q + r_) > 2: continue
        x = cx + s * 1.5 * q * 1.02
        y = cy + s * math.sqrt(3) * (r_ + q / 2) * 1.02
        cells.append((x, y, q == 0 and r_ == 0))
for x, y, centre in cells:
    if centre:
        a(f'<polygon class="i-metal" points="{hexpts(x,y,s-1.5)}"/><circle style="fill:var(--ink-2)" cx="{x:.1f}" cy="{y:.1f}" r="6"/>')
    else:
        a(f'<polygon class="i-fuel-soft" points="{hexpts(x,y,s-1.5)}"/>')
        for k in range(6):
            ang = math.radians(60*k+30); a(f'<circle class="i-fuel" cx="{x+10*math.cos(ang):.1f}" cy="{y+10*math.sin(ang):.1f}" r="2.3"/>')
        a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" style="fill:var(--bg);stroke:var(--cool);stroke-width:1.2"/>')
# control drums in reflector
for k in range(12):
    ang = math.radians(k * 30 + 15)
    dx, dy = cx + 140*math.cos(ang), cy + 140*math.sin(ang)
    a(f'<circle class="i-fill" cx="{dx:.1f}" cy="{dy:.1f}" r="21"/>')
    # absorber arc on the outward side (reactor running); one drum turned inward
    face = ang if k != 4 else ang + math.pi
    a0, a1 = face - math.radians(70), face + math.radians(70)
    x0, y0 = dx + 18*math.cos(a0), dy + 18*math.sin(a0); x1, y1 = dx + 18*math.cos(a1), dy + 18*math.sin(a1)
    a(f'<path d="M{x0:.1f} {y0:.1f} A18 18 0 0 1 {x1:.1f} {y1:.1f}" style="fill:none;stroke:var(--ink);stroke-width:5;stroke-linecap:butt"/>')
# neutron paths: one escapes, one reflected
a(f'<path d="M{cx+30} {cy-40} L{cx+95} {cy-110} L{cx+150} {cy-200}" class="i-dash" marker-end="url(#ah)" style="stroke:var(--ink-2)"/>')
a(f'<path d="M{cx-40} {cy+30} L{cx-125} {cy+85} L{cx-70} {cy+60}" class="i-dash" marker-end="url(#ah)" style="stroke:var(--ink-2)"/>')
# labels
L = [
 (cx+150, cy-205, 365, 78, 'A neutron that escapes is lost', 'a small core leaks far more'),
 (cx-128, cy+86, 20, 445, 'The reflector bounces neutrons back', 'graphite or beryllium around the core'),
]
a(f'<text class="i-t" x="372" y="74">A neutron that escapes is wasted</text><text class="i-n" x="372" y="89">a small core leaks far more</text>')
a(f'<line class="i-lead" x1="{cx+152}" y1="{cy-196}" x2="368" y2="80"/>')
a(f'<text class="i-t" x="20" y="452">The reflector bounces neutrons back</text><text class="i-n" x="296" y="452">graphite or beryllium</text>')
a(f'<line class="i-lead" x1="{cx-128}" y1="{cy+92}" x2="90" y2="438"/>')
dk = math.radians(4*30+15); kx, ky = cx+140*math.cos(dk), cy+140*math.sin(dk)
a(f'<line class="i-lead" x1="{kx-14:.1f}" y1="{ky+16:.1f}" x2="372" y2="420"/>' if False else '')
a(f'<text class="i-t" x="372" y="150">Control drums turn instead of rods</text><text class="i-n" x="372" y="165">black face out: reactor runs</text><text class="i-n" x="372" y="179">black face in: soaks up neutrons, stops</text>')
d0 = math.radians(-15); a(f'<line class="i-lead" x1="{cx+140*math.cos(d0)+20:.1f}" y1="{cy+140*math.sin(d0):.1f}" x2="368" y2="156"/>')
a(f'<text class="i-t" x="372" y="230">Fuel blocks hold the TRISO</text><text class="i-n" x="372" y="245">holes for fuel, channels for helium</text>')
a(f'<line class="i-lead" x1="{cx+66}" y1="{cy-10}" x2="368" y2="236"/>')
a(f'<text class="i-t" x="372" y="292">Shutdown rod in the centre</text><text class="i-n" x="372" y="307">a backup that drops in if needed</text>')
a(f'<line class="i-lead" x1="{cx+7}" y1="{cy+2}" x2="368" y2="298"/>')
# 2. module on a trailer
a('<text class="i-k" x="640" y="28">2 · The plant on a trailer</text><text class="i-n" x="640" y="44">shipping-container sized modules</text>')
ty = 330
a(f'<rect class="i-fill" x="618" y="{ty}" width="300" height="14" rx="2"/>')
for wx in (650, 678, 860, 888): a(f'<circle class="i-fill" cx="{wx}" cy="{ty+24}" r="11"/><circle cx="{wx}" cy="{ty+24}" r="3" style="fill:var(--ink-3)"/>')
a(f'<line class="i-faint" x1="600" y1="{ty+35}" x2="930" y2="{ty+35}"/>')
# reactor module
a(f'<rect class="i-metal" x="628" y="{ty-170}" width="120" height="170" rx="4"/>')
a(f'<rect class="i-fill" x="650" y="{ty-140}" width="76" height="118" rx="30"/>')
a(f'<rect class="i-fuel-soft" x="664" y="{ty-112}" width="48" height="62" rx="3"/>')
a(f'<text class="i-n2" x="688" y="{ty+56}" text-anchor="middle">Reactor</text><text class="i-n" x="688" y="{ty+70}" text-anchor="middle">core and shield</text>')
# power module
a(f'<rect class="i-fill" x="768" y="{ty-130}" width="140" height="130" rx="4"/>')
a(f'<path class="i-line" d="M790 {ty-90} L820 {ty-100} V{ty-50} L790 {ty-60} Z"/>')
a(f'<circle class="i-fill" cx="866" cy="{ty-75}" r="22"/><text class="i-n2" x="866" y="{ty-71}" text-anchor="middle">G</text>')
a(f'<line class="i-line" x1="820" y1="{ty-75}" x2="844" y2="{ty-75}"/>')
a(f'<text class="i-n2" x="838" y="{ty+56}" text-anchor="middle">Turbine and generator</text><text class="i-n" x="838" y="{ty+70}" text-anchor="middle">heat into electricity</text>')
# helium loop
a(f'<path class="i-hot" d="M712 {ty-112} V{ty-150} H780 V{ty-98} H790" marker-end="url(#ahot)"/>')
a(f'<path class="i-cool" d="M790 {ty-62} H770 V{ty-10} H700 V{ty-50}" marker-end="url(#acool)"/>')
a(f'<text class="i-hot-t" x="752" y="{ty-156}">hot helium</text><text class="i-cool-t" x="704" y="{ty+0-2}" style="font-size:11px"></text>')
a(f'<text class="i-cool-t" x="772" y="{ty+12}" style="font-size:11px">cooled, back to the core</text>' if False else '')
a(f'<line class="i-hot" x1="908" y1="{ty-75}" x2="926" y2="{ty-75}"/><text class="i-hot-t" x="900" y="{ty-30}" text-anchor="end">electricity out</text><text class="i-n" x="900" y="{ty-16}" text-anchor="end">1 to 20 MWe</text>')
a(f'<text class="i-n" x="640" y="{ty+100}">Built and fuelled in a factory, trucked in,</text><text class="i-n" x="640" y="{ty+114}">run for years, then trucked back out.</text>')
svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Inside a transportable gas-cooled microreactor. Left: the core seen from above. Hexagonal graphite fuel blocks hold TRISO fuel and helium channels, with a shutdown rod in the centre. A ring of reflector surrounds them, bouncing escaping neutrons back. Twelve control drums sit in the reflector, each with an absorbing face: turned out, the reactor runs; turned in, they soak up neutrons and stop it. Right: the plant as modules on a trailer. Hot helium carries heat from the reactor module to a turbine and generator, and returns cooled. Output 1 to 20 megawatts of electricity.">' + ''.join(x for x in o if x) + '</svg>'
open('illos/core.svg', 'w').write(svg)
