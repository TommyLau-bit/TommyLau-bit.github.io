"""Three illustrations: the combined cycle plant, the hot blade, and the island campus."""
import os
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
def save(name, W, H, body, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# ---------- 1. The gas turbine and the combined cycle ----------
W, H = 940, 500
o = []; a = o.append
cy = 230                       # shaft line
# brackets over the two halves
a(f'<path class="i-thin" d="M20 34 V24 H600 V34"/><text class="i-k" x="310" y="16" text-anchor="middle">Simple cycle: the gas turbine alone</text>')
a(f'<path class="i-thin" d="M612 34 V24 H930 V34"/><text class="i-k" x="771" y="16" text-anchor="middle">Combined cycle adds a steam loop</text>')
# generator 1
a(f'<rect class="i-metal" x="24" y="{cy-40}" width="88" height="80" rx="8"/><text class="i-t" x="68" y="{cy+64}" text-anchor="middle">Generator</text>')
a(f'<line class="i-line" x1="112" y1="{cy}" x2="140" y2="{cy}" style="stroke-width:4"/>')
# compressor: tall at intake, narrowing
a(f'<path class="i-fill" d="M140 {cy-78} L320 {cy-36} L320 {cy+36} L140 {cy+78} Z"/>')
for k in range(8):
    x = 156 + k * 21; h = 74 - k * 5
    a(f'<line class="i-thin" x1="{x}" y1="{cy-h+4}" x2="{x}" y2="{cy+h-4}"/>')
a(f'<path class="i-cool" d="M118 {cy-110} C150 {cy-110} 160 {cy-90} 170 {cy-70}"/><path class="i-cool" d="M164 {cy-80} l8 12 l4 -14"/>')
a(f'<text class="i-cool-t" x="110" y="{cy-118}">air in</text>')
a(f'<text class="i-t" x="230" y="{cy+110}" text-anchor="middle">Compressor</text><text class="i-n" x="230" y="{cy+128}" text-anchor="middle">squeezes air about 24 times</text>')
# combustor
a(f'<rect class="i-fill" x="320" y="{cy-40}" width="66" height="80" rx="6"/>')
a(f'<path class="i-hot-f" d="M353 {cy+22} C335 {cy+4} 348 {cy-10} 353 {cy-26} C360 {cy-10} 372 {cy+2} 353 {cy+22} Z" opacity=".85"/>')
a(f'<path class="i-fuel" d="M353 {cy-120} V{cy-44}" style="stroke:var(--fuel);stroke-width:3;fill:none"/><text class="i-fuel-t" x="353" y="{cy-128}" text-anchor="middle">gas in</text>')
a(f'<line class="i-lead" x1="353" y1="{cy+44}" x2="353" y2="{cy+150}"/><text class="i-t" x="353" y="{cy+168}" text-anchor="middle">Combustor</text><text class="i-hot-t" x="353" y="{cy+186}" text-anchor="middle">gas burns at about 1,600°C</text>')
# turbine: widening
a(f'<path class="i-fill" d="M386 {cy-40} L500 {cy-70} L500 {cy+70} L386 {cy+40} Z"/>')
for k in range(5):
    x = 398 + k * 22; h = 42 + k * 7
    a(f'<line class="i-hot" x1="{x}" y1="{cy-h+4}" x2="{x}" y2="{cy+h-4}" style="stroke-width:1.4"/>')
a(f'<text class="i-t" x="443" y="{cy+110}" text-anchor="middle">Turbine</text><text class="i-n" x="443" y="{cy+128}" text-anchor="middle">hot gas spins it; it turns</text><text class="i-n" x="443" y="{cy+144}" text-anchor="middle">the compressor and generator</text>')
# shaft through
a(f'<line class="i-line" x1="140" y1="{cy}" x2="500" y2="{cy}" style="stroke-dasharray:6 4"/>')
# exhaust duct
a(f'<path class="i-fill" d="M500 {cy-70} L600 {cy-70} L600 {cy+70} L500 {cy+70}"/>')
a(f'<path class="i-hot" d="M512 {cy} H588"/><path class="i-hot" d="M580 {cy-7} l9 7 l-9 7"/>')
a(f'<text class="i-hot-t" x="550" y="{cy+92}" text-anchor="middle">exhaust</text><text class="i-hot-t" x="550" y="{cy+108}" text-anchor="middle">about 670°C</text>')
# simple-cycle stack (dashed alternative)
a(f'<path class="i-dash" d="M560 {cy-70} V{cy-130} H590 V{cy-70}" style="fill:none"/>')
a(f'<text class="i-n" x="575" y="{cy-156}" text-anchor="middle">simple cycle:</text><text class="i-n" x="575" y="{cy-140}" text-anchor="middle">heat goes up</text>')
# HRSG
a(f'<rect class="i-fill" x="612" y="{cy-70}" width="140" height="140" rx="4"/>')
for k in range(5):
    x = 632 + k * 24
    a(f'<path class="i-cool" d="M{x} {cy+56} V{cy-56}" style="stroke-width:1.4"/>')
a(f'<path class="i-line" d="M720 {cy-70} V{cy-130} H748 V{cy-70}" style="fill:none"/><text class="i-n" x="734" y="{cy-140}" text-anchor="middle">cooled exhaust</text>')
a(f'<text class="i-t" x="682" y="{cy+110}" text-anchor="middle">Heat recovery boiler</text><text class="i-n" x="682" y="{cy+128}" text-anchor="middle">exhaust boils water to steam</text>')
# steam to steam turbine
a(f'<path class="i-cool" d="M752 {cy-40} H790"/><path class="i-cool" d="M783 {cy-47} l9 7 l-9 7"/>')
a(f'<path class="i-fill" d="M794 {cy-28} L846 {cy-50} L846 {cy+50} L794 {cy+28} Z"/>')
a(f'<rect class="i-metal" x="858" y="{cy-34}" width="66" height="68" rx="8"/><line class="i-line" x1="846" y1="{cy}" x2="858" y2="{cy}" style="stroke-width:4"/>')
a(f'<text class="i-t" x="860" y="{cy+110}" text-anchor="middle">Steam turbine</text><text class="i-n" x="860" y="{cy+128}" text-anchor="middle">and a second generator</text>')
a(f'<path class="i-cool" d="M820 {cy+52} V{cy+76} H700 V{cy+70}" style="stroke-dasharray:3 3"/><text class="i-n" x="760" y="{cy+92}" text-anchor="middle">water back</text>')
# outcome strip
yb = 458
a(f'<line class="i-faint" x1="20" y1="{yb-26}" x2="{W-20}" y2="{yb-26}"/>')
a(f'<text class="i-t" x="24" y="{yb}">About 43 per cent</text><text class="i-n" x="24" y="{yb+18}">of the gas\'s energy becomes electricity: one GE 7HA.03, 430 MW</text>')
a(f'<text class="i-t" x="612" y="{yb}">About 64 per cent</text><text class="i-n" x="612" y="{yb+18}">same turbine plus steam: about 640 MW</text>')
save('turbine', W, yb + 30, ''.join(o), 'A heavy gas turbine and a combined cycle plant, simplified. On the left, a generator on the same shaft as the gas turbine. The compressor squeezes air about 24 times. In the combustor gas burns at about 1,600 degrees Celsius. The hot gas spins the turbine, which turns both the compressor and the generator. The exhaust leaves at about 670 degrees. In simple cycle it goes up a stack, and about 43 per cent of the gas\'s energy becomes electricity, as in one GE 7HA.03 of 430 MW. In combined cycle the exhaust boils water in a heat recovery boiler, and the steam drives a steam turbine and a second generator, lifting efficiency to about 64 per cent, about 640 MW from the same turbine.')

# ---------- 2. The hot blade ----------
W, H = 940, 470
o = []; a = o.append
# left: a blade, root at the bottom
bx, by = 120, 60
a(f'<path class="i-metal" d="M{bx-40} 400 h150 v-26 h-14 v-14 h14 v-14 h-14 v-14 h14 v-12 h-150 v12 h14 v14 h-14 v14 h14 v14 h-14 Z"/>')   # fir-tree root
a(f'<rect class="i-metal" x="{bx-56}" y="300" width="182" height="20" rx="3"/>')                              # platform
a(f'<path class="i-fill" d="M{bx-30} 300 C{bx-50} 220 {bx-36} 120 {bx-6} 70 C{bx+30} 60 {bx+80} 70 {bx+96} 84 C{bx+70} 150 {bx+70} 230 {bx+90} 300 Z" style="stroke-width:1.6"/>')
# serpentine cooling passages
a(f'<path class="i-cool" d="M{bx} 296 C{bx-6} 220 {bx-2} 140 {bx+10} 96 M{bx+26} 96 C{bx+22} 160 {bx+22} 230 {bx+30} 296 M{bx+46} 296 C{bx+42} 230 {bx+42} 160 {bx+50} 100 M{bx+66} 100 C{bx+60} 170 {bx+62} 236 {bx+70} 296" style="stroke-dasharray:5 3"/>')
for k in range(9):
    yy = 108 + k * 22; xx = bx - 14 - (6 if k in (0, 8) else 0) + (k % 3)
    a(f'<circle class="i-cool-f" cx="{xx}" cy="{yy}" r="2.6"/>')
a(f'<path class="i-cool" d="M{bx+20} 450 V412"/><path class="i-cool" d="M{bx+13} 420 l7 -10 l7 10"/><text class="i-cool-t" x="{bx+30}" y="452">cooling air from the compressor</text>')
a(f'<path class="i-hot" d="M{bx-110} 150 H{bx-52}"/><path class="i-hot" d="M{bx-60} 143 l9 7 l-9 7"/><path class="i-hot" d="M{bx-110} 210 H{bx-56}"/><path class="i-hot" d="M{bx-64} 203 l9 7 l-9 7"/><text class="i-hot-t" x="{bx-110}" y="136">hot gas</text>')
a(f'<text class="i-t" x="{bx+20}" y="40" text-anchor="middle">A first-stage blade</text><text class="i-n" x="{bx+20}" y="56" text-anchor="middle">about a hand\'s length</text>')
# callouts
cx0 = 300
notes = [
  (100, 'One metal crystal', 'grown whole, so there are no grain boundaries', 'to creep and crack at heat'),
  (190, 'Cooling passages', 'cast in around ceramic cores; air leaves by rows', 'of tiny holes and lays a cool film on the skin'),
  (280, 'Ceramic coat', 'a thin thermal barrier over a metal bond coat', ''),
]
for y, t, n1, n2 in notes:
    a(f'<line class="i-lead" x1="{bx+92 if y==100 else bx+70}" y1="{y}" x2="{cx0-8}" y2="{y}"/>')
    a(f'<text class="i-t" x="{cx0}" y="{y-4}">{t}</text><text class="i-n" x="{cx0}" y="{y+13}">{n1}</text>' + (f'<text class="i-n" x="{cx0}" y="{y+29}">{n2}</text>' if n2 else ''))
# right: temperature ladder
lx, ly0, ly1 = 690, 80, 400
T = lambda c: ly1 - (c - 0) / 1700 * (ly1 - ly0)
a(f'<line class="i-line" x1="{lx}" y1="{T(0)}" x2="{lx}" y2="{T(1700)}"/>')
for c in (0, 500, 1000, 1500):
    a(f'<line class="i-thin" x1="{lx-5}" y1="{T(c):.1f}" x2="{lx+5}" y2="{T(c):.1f}"/><text class="i-n" x="{lx-10}" y="{T(c)+4:.1f}" text-anchor="end">{c:,}°C</text>')
a(f'<rect class="i-choke" x="{lx+12}" y="{T(1600)-12:.1f}" width="220" height="24" rx="4"/>')
a(f'<circle class="i-hot-f" cx="{lx}" cy="{T(1600):.1f}" r="6"/><text class="i-hot-t" x="{lx+20}" y="{T(1600)+4:.1f}">gas entering the turbine: 1,600°C</text>')
a(f'<circle class="i-fuel" cx="{lx}" cy="{T(1340):.1f}" r="5"/><text class="i-fuel-t" x="{lx+20}" y="{T(1340)+4:.1f}">a common blade alloy</text><text class="i-fuel-t" x="{lx+20}" y="{T(1340)+19:.1f}">starts to melt: about 1,340°C</text>')
a(f'<path class="i-cool" d="M{lx+30} {T(1240):.1f} V{T(900):.1f}"/><path class="i-cool" d="M{lx+23} {T(900)-10:.1f} l7 10 l7 -10"/><text class="i-cool-t" x="{lx+44}" y="{T(1080):.1f}">coat and cooling hold</text><text class="i-cool-t" x="{lx+44}" y="{T(1080)+15:.1f}">the metal well below it</text>')
a(f'<text class="i-t" x="{lx}" y="44" text-anchor="middle">The flame is hotter than the metal can stand</text>')
save('blade', W, H, ''.join(o), 'A first-stage turbine blade, about a hand\'s length, with its fir-tree root. It is cast as one metal crystal, so there are no grain boundaries to creep and crack at heat. Cooling passages are cast in around ceramic cores; cooling air from the compressor runs through them and leaves by rows of tiny holes, laying a cool film on the surface. A thin ceramic thermal barrier coat sits on a metal bond coat. A temperature scale shows the gas entering the turbine at 1,600 degrees Celsius, above the point at which a common blade alloy starts to melt, about 1,340 degrees; the coat and the cooling hold the metal well below it.')

# ---------- 3. The island campus ----------
W, H = 940, 470
o = []; a = o.append
a(f'<line class="i-faint" x1="470" y1="20" x2="470" y2="{H-20}"/>')
# left: on the grid
a(f'<text class="i-k" x="40" y="40">On the grid</text>')
def plant(x, y, s=1.0):
    a(f'<rect class="i-fill" x="{x}" y="{y}" width="{34*s:.0f}" height="{24*s:.0f}" rx="2"/><rect class="i-fill" x="{x+22*s:.0f}" y="{y-18*s:.0f}" width="{8*s:.0f}" height="{18*s:.0f}"/>')
def pylon(x, y):
    a(f'<path class="i-line" d="M{x-10} {y+40} L{x} {y} L{x+10} {y+40} M{x-7} {y+26} H{x+7} M{x-14} {y+8} H{x+14}"/>')
for i, (px, py) in enumerate([(40, 90), (100, 70), (160, 96), (60, 150), (130, 140), (200, 160), (90, 210), (170, 220)]):
    plant(px, py, 0.9)
for px in (260, 320):
    pylon(px, 150)
a(f'<path class="i-thin" d="M230 120 C250 140 255 150 260 158 M230 230 C250 210 255 200 260 190 M270 158 H310 M330 158 H360"/>')
a(f'<rect class="i-fill" x="360" y="130" width="84" height="64" rx="4"/><text class="i-t" x="402" y="216" text-anchor="middle">Data centre</text>')
a(f'<text class="i-n" x="40" y="300">Thousands of plants share the load.</text><text class="i-n" x="40" y="318">When one trips or the load jumps,</text><text class="i-n" x="40" y="336">the rest cover it, and spares are shared.</text>')
a(f'<text class="i-n" x="40" y="372">PJM, 22 July 2026: after one fault, about</text><text class="i-hot-t" x="40" y="390">3,900 MW of data-centre load switched</text><text class="i-hot-t" x="40" y="406">to backup at once; the grid absorbed it.</text>')
# right: the island
a(f'<text class="i-k" x="500" y="40">An island campus</text>')
a(f'<rect class="i-fill" x="770" y="120" width="130" height="80" rx="4"/><text class="i-t" x="835" y="222" text-anchor="middle">Data centre</text><text class="i-n" x="835" y="238" text-anchor="middle">400 MW committed</text>')
gx, gy, gw, gh, gap = 500, 92, 46, 30, 8
labels = []
for r in range(2):
    for c in range(4):
        k = r * 4 + c
        x = gx + c * (gw + gap); y = gy + r * (gh + 30)
        if k < 6:
            a(f'<rect class="i-metal" x="{x}" y="{y}" width="{gw}" height="{gh}" rx="3"/>')
        elif k == 6:
            a(f'<rect class="i-choke" x="{x}" y="{y}" width="{gw}" height="{gh}" rx="3"/><text class="i-hot-t" x="{x+gw/2}" y="{y+gh+15}" text-anchor="middle">spare</text>')
        else:
            a(f'<rect class="i-fill" x="{x}" y="{y}" width="{gw}" height="{gh}" rx="3" style="stroke-dasharray:4 3"/><text class="i-n" x="{x+gw/2}" y="{y+gh+15}" text-anchor="middle">hot day</text>')
a(f'<path class="i-line" d="M{gx+4*(gw+gap)-4} 140 H770"/>')
a(f'<rect class="i-cool-f" x="672" y="200" width="80" height="34" rx="4" opacity=".85"/><text class="i-t" x="712" y="252" text-anchor="middle">Battery</text><text class="i-n" x="712" y="268" text-anchor="middle">soaks up swings</text>')
a(f'<path class="i-cool" d="M752 190 H790 V200"/>')
a(f'<text class="i-t" x="500" y="232">556 MW built</text><text class="i-n" x="500" y="250">Socrates, Williams: 1.39 MW</text><text class="i-n" x="500" y="266">for each MW committed</text>')
a(f'<line class="i-faint" x1="500" y1="296" x2="{W-30}" y2="296"/>')
for i, (t, n) in enumerate([
    ('A spare for every outage', 'one unit down for repair or a trip must not cut the load'),
    ('Margin for heat', 'an aeroderivative loses about a quarter of its output at 45°C'),
    ('A buffer for swings', 'a campus\'s load can drop off or return by hundreds of MW at once'),
]):
    y = 324 + i * 44
    a(f'<text class="i-t" x="500" y="{y}">{t}</text><text class="i-n" x="500" y="{y+17}">{n}</text>')
save('island', W, H, ''.join(o), 'Two ways to power a data centre. On the grid, thousands of plants share the load, and when one trips or the load jumps the rest cover it; on 22 July 2026, after one fault, about 3,900 MW of data-centre load in PJM switched to backup at once and the grid absorbed it. An island campus must carry its own cover: eight generating units for a data centre with 400 MW committed, six carrying the load, one spare and one margin for hot days, plus a battery to soak up swings. Williams\' Socrates has 556 MW built for 400 MW committed, 1.39 MW for each MW. The three reasons: a spare for every outage; margin for heat, since an aeroderivative loses about a quarter of its output at 45 degrees; and a buffer for swings, since a campus\'s load can drop off or return by hundreds of megawatts at once.')
print('illos ok')
