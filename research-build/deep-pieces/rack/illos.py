"""Three illustrations: one megawatt from the grid to the chip; the three places AC can become 800 V DC; why DC is hard to switch off."""
import os, math
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
def save(name, W, H, body, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

def arrow(a, x0, x1, y, cls='i-line'):
    a(f'<path class="{cls}" d="M{x0} {y} H{x1}"/><path class="{cls}" d="M{x1-7} {y-5} l7 5 l-7 5" style="fill:none"/>')

# ---------- 1. The chain: one megawatt from the grid to the chip ----------
W = 940; o = []; a = o.append
gy = 200
a(f'<text class="i-head" x="10" y="20">One megawatt, traced from the grid to the chip</text>')
a(f'<line class="i-ground" x1="10" y1="{gy}" x2="{W-10}" y2="{gy}"/>')
C = [80, 270, 470, 670, 860]
for i in range(4):
    arrow(a, C[i] + 66, C[i+1] - 66, 130)
# 1 grid: a pylon
x = C[0]
a(f'<path class="i-line" d="M{x-26} {gy} L{x-8} 52 L{x+8} 52 L{x+26} {gy} M{x-18} 150 H{x+18} M{x-13} 110 H{x+13} M{x-34} 72 H{x+34} M{x-28} 96 H{x+28}" style="fill:none"/>')
for dx in (-34, 34, -28, 28):
    yy = 72 if abs(dx) == 34 else 96
    a(f'<line class="i-thin" x1="{x+dx}" y1="{yy}" x2="{x+dx}" y2="{yy+8}"/>')
# 2 power room: shaded, transformer and UPS
x = C[1]
a(f'<rect class="i-choke" x="{x-80}" y="40" width="160" height="{gy-40}" rx="6"/>')
a(f'<rect class="i-fill" x="{x-66}" y="108" width="62" height="{gy-108}" rx="4"/>')
for k in range(3):
    a(f'<rect class="i-fill" x="{x-60+k*20}" y="84" width="9" height="24" rx="3"/>')
a(f'<line class="i-thin" x1="{x-58}" y1="128" x2="{x-12}" y2="128"/><line class="i-thin" x1="{x-58}" y1="146" x2="{x-12}" y2="146"/>')
a(f'<rect class="i-fill" x="{x+8}" y="96" width="56" height="{gy-96}" rx="3"/>')
for k in range(4):
    a(f'<rect class="i-cool-f" x="{x+16}" y="{106+k*22}" width="40" height="14" rx="2"/>')
a(f'<text class="i-k" x="{x-35}" y="78" text-anchor="middle">transformer</text><text class="i-k" x="{x+36}" y="90" text-anchor="middle">UPS</text>')
a(f'<text class="i-hot-t" x="{x}" y="58" text-anchor="middle">changes last</text>')
# 3 rack: power shelves at top, busbar up the back, trays
x = C[2]
a(f'<rect class="i-fill" x="{x-40}" y="46" width="80" height="{gy-46}" rx="3"/>')
for k in range(3):
    a(f'<rect class="i-metal" x="{x-34}" y="{52+k*12}" width="56" height="9" rx="1"/>')
for k in range(8):
    a(f'<rect class="i-fill" x="{x-34}" y="{92+k*13}" width="56" height="9" rx="1"/>')
a(f'<rect class="i-hot-f" x="{x+26}" y="52" width="8" height="{gy-58}" rx="1"/>')
a(f'<text class="i-n" x="{x-50}" y="62" text-anchor="end">power</text><text class="i-n" x="{x-50}" y="76" text-anchor="end">shelves</text>')
a(f'<text class="i-n" x="{x+48}" y="120">busbar</text>')
# 4 tray: a board with converter and GPU packages
x = C[3]
a(f'<rect class="i-fill" x="{x-62}" y="104" width="124" height="60" rx="3"/>')
a(f'<rect class="i-metal" x="{x-54}" y="116" width="26" height="36" rx="2"/><text class="i-k" x="{x-41}" y="178" text-anchor="middle">IBC</text>')
for k in range(2):
    a(f'<rect class="i-fill" x="{x-14+k*36}" y="114" width="30" height="40" rx="2"/>')
a(f'<line class="i-thin" x1="{x-28}" y1="134" x2="{x-14}" y2="134"/>')
# 5 chip: GPU with ring of regulators
x = C[4]
a(f'<rect class="i-fill" x="{x-40}" y="84" width="80" height="80" rx="4"/><rect class="i-metal" x="{x-22}" y="102" width="44" height="44" rx="2"/>')
for k in range(6):
    a(f'<rect class="i-cool-f" x="{x-36+k*13}" y="88" width="9" height="8" rx="1"/><rect class="i-cool-f" x="{x-36+k*13}" y="152" width="9" height="8" rx="1"/>')
a(f'<text class="i-k" x="{x}" y="178" text-anchor="middle">regulators</text>')
L = [('1. Grid', '35 kV AC', 'about 16 A per phase', ''),
     ('2. Power room', '415 V AC', 'about 1,390 A per phase', 'booked years ahead'),
     ('3. Rack', '54 V DC busbar', 'about 18,500 A', 'at 800 V: 1,250 A'),
     ('4. Tray', 'steps to 12 V', 'about 83,000 A', ''),
     ('5. Chip', 'below 1 V', 'about 1.25 million A', 'at 0.8 V, my estimate')]
for x, (t, v, i, n) in zip(C, L):
    a(f'<text class="i-t" x="{x}" y="{gy+24}" text-anchor="middle">{t}</text><text class="i-n" x="{x}" y="{gy+42}" text-anchor="middle">{v}</text>')
    a(f'<text class="i-hot-t" x="{x}" y="{gy+60}" text-anchor="middle">{i}</text>')
    if n:
        a(f'<text class="{"i-cool-t" if "800" in n else "i-n"}" x="{x}" y="{gy+78}" text-anchor="middle">{n}</text>')
save('chain', W, gy + 90, ''.join(o), 'One megawatt traced from the grid to the chip, in five steps. One, the grid: 35 kilovolts AC, about 16 amps per phase. Two, the power room, with its transformer and UPS: 415 volts AC, about 1,390 amps per phase; it is shaded, because it is booked years ahead and changes last. Three, the rack, with power shelves at the top and a copper busbar up the back: 54 volts DC, about 18,500 amps; at 800 volts it would be 1,250 amps. Four, the compute tray, where an intermediate bus converter steps down to 12 volts, about 83,000 amps. Five, the chip, ringed by voltage regulators, below 1 volt; at an assumed 0.8 volts, about 1.25 million amps.')

# ---------- 2. Three places AC can become 800 V DC ----------
W = 940; o = []; a = o.append
a(f'<text class="i-head" x="10" y="20">Where AC becomes 800 V DC, in three options</text>')
# legend
a(f'<line class="i-line" x1="560" y1="16" x2="590" y2="16"/><text class="i-n" x="596" y="20">AC</text>')
a(f'<line class="i-cool" x1="640" y1="16" x2="670" y2="16"/><text class="i-n" x="676" y="20">800 V DC</text>')
a(f'<circle class="i-hot-f" cx="770" cy="16" r="6"/><text class="i-n" x="782" y="20">AC becomes DC here</text>')
rows = [('A. Power rack', 'beside one or two racks, about 660 kW', 'in production from Q3 2026'),
        ('B. Row power centre', 'end of the row, up to 2 MW', 'as soon as Q3 2027'),
        ('C. DC power block', 'at the building edge, about 4.8 MW', 'rectifier: no date; next SST toward 2029')]
def box(x, y, w, h, lab, cls='i-fill'):
    a(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="3"/>')
    if lab:
        a(f'<text class="i-n" x="{x+w/2}" y="{y+h+16}" text-anchor="middle">{lab}</text>')
def rack(x, y):
    a(f'<rect class="i-fill" x="{x}" y="{y}" width="34" height="64" rx="2"/>')
    for k in range(5):
        a(f'<line class="i-thin" x1="{x+5}" y1="{y+9+k*11}" x2="{x+29}" y2="{y+9+k*11}"/>')
for r, (t, sub, when) in enumerate(rows):
    y = 54 + r * 150
    a(f'<text class="i-t" x="10" y="{y+12}">{t}</text><text class="i-n" x="10" y="{y+30}">{sub}</text><text class="{"i-hot-t" if r == 2 else "i-k"}" x="10" y="{y+48}">{when}</text>')
    gy = y + 96
    # grid pylon
    px = 300
    a(f'<path class="i-line" d="M{px-12} {gy} L{px-4} {y+20} L{px+4} {y+20} L{px+12} {gy} M{px-16} {y+34} H{px+16}" style="fill:none"/>')
    a(f'<text class="i-n" x="{px}" y="{gy+16}" text-anchor="middle">grid</text>')
    if r < 2:
        box(350, y + 36, 90, 60, 'AC power room')
        a(f'<line class="i-line" x1="{px+12}" y1="{y+60}" x2="350" y2="{y+60}"/>')
        a(f'<line class="i-line" x1="440" y1="{y+66}" x2="{540 if r == 0 else 520}" y2="{y+66}"/>')
        a(f'<text class="i-n" x="490" y="{y+58}" text-anchor="middle">415 V AC</text>')
    if r == 0:
        box(540, y + 32, 40, 64, 'power rack', 'i-metal')
        a(f'<circle class="i-hot-f" cx="560" cy="{y+26}" r="6"/>')
        a(f'<line class="i-cool" x1="580" y1="{y+66}" x2="610" y2="{y+66}"/>')
        rack(610, y + 32)
        a(f'<text class="i-n" x="627" y="{y+128}" text-anchor="middle">compute rack</text>')
        a(f'<text class="i-n" x="660" y="{y+50}">800 V stays between two cabinets;</text><text class="i-n" x="660" y="{y+66}">a shelf inside turns it back to 54 V.</text>')
        a(f'<text class="i-n" x="660" y="{y+82}">Certified as IT equipment.</text>')
    elif r == 1:
        box(520, y + 26, 46, 70, 'row power centre', 'i-metal')
        a(f'<circle class="i-hot-f" cx="543" cy="{y+20}" r="6"/>')
        a(f'<path class="i-cool" d="M566 {y+34} H880" style="fill:none"/>')
        for k in range(5):
            xx = 600 + k * 56
            a(f'<line class="i-cool" x1="{xx+17}" y1="{y+34}" x2="{xx+17}" y2="{y+46}"/>')
            a(f'<rect class="i-fill" x="{xx}" y="{y+46}" width="34" height="50" rx="2"/>')
        a(f'<text class="i-n" x="740" y="{y+26}" text-anchor="middle">overhead 800 V busway</text>')
        a(f'<text class="i-n" x="740" y="{y+128}" text-anchor="middle">a whole row of racks; the AC room is unchanged</text>')
    else:
        box(350, y + 36, 90, 60, '', 'i-faint')
        a(f'<text class="i-n" x="395" y="{y+70}" text-anchor="middle">AC room</text><text class="i-hot-t" x="395" y="{y+112}" text-anchor="middle">removed</text>')
        a(f'<path class="i-line" d="M{px+12} {y+60} C {px+30} {y+60}, {px+30} {y+20}, 360 {y+18} H470" style="fill:none"/>')
        box(470, y + 4, 70, 36, '', 'i-metal')
        a(f'<text class="i-n" x="505" y="{y+27}" text-anchor="middle">block</text>')
        a(f'<circle class="i-hot-f" cx="505" cy="{y-4}" r="6"/>')
        a(f'<text class="i-n" x="470" y="{y+64}">rectifier or SST,</text><text class="i-n" x="470" y="{y+78}">medium voltage in</text>')
        a(f'<path class="i-cool" d="M540 {y+22} H600 V{y+34} H880" style="fill:none"/>')
        for k in range(5):
            xx = 600 + k * 56
            a(f'<line class="i-cool" x1="{xx+17}" y1="{y+34}" x2="{xx+17}" y2="{y+46}"/>')
            a(f'<rect class="i-fill" x="{xx}" y="{y+46}" width="34" height="50" rx="2"/>')
        a(f'<text class="i-n" x="740" y="{y+114}" text-anchor="middle">800 V across the hall: what my test counts</text>')
    if r < 2:
        a(f'<line class="i-faint" x1="10" y1="{y+136}" x2="{W-10}" y2="{y+136}"/>')
save('options', W, 54 + 3 * 150 - 10, ''.join(o), 'Three rows, one for each of Nvidia\'s options for where the grid\'s alternating current becomes 800 volts DC. A, the power rack, about 660 kilowatts, in production from the third quarter of 2026: the grid feeds the existing AC power room, which sends 415 volts AC to a power rack beside the compute rack; the power rack makes 800 volts DC, which stays between the two cabinets, and a shelf inside the compute rack turns it back into 54 volts; it is certified as IT equipment. B, the row power centre, up to 2 megawatts, as soon as the third quarter of 2027: the same AC room feeds one cabinet at the end of the row, which makes 800 volts DC for an overhead busway serving a whole row of racks; the AC room is unchanged. C, the DC power block, about 4.8 megawatts, at the building edge: the grid\'s medium voltage goes straight into a rectifier or solid-state transformer, the AC room is removed, and 800 volts DC runs across the hall. Nvidia gives no date for the rectifier version and puts the next generation solid-state transformer toward 2029. Only C is what my test counts.')

# ---------- 3. The off switch ----------
W = 940; o = []; a = o.append
a(f'<text class="i-head" x="10" y="20">Why DC is harder to switch off, and how fast each breaker clears</text>')
# left: AC sine and DC line over 40 ms
px0, px1 = 70, 470
T = 40.0
X = lambda t: px0 + t / T * (px1 - px0)
for (cy, lab) in ((100, 'AC'), (220, 'DC')):
    a(f'<line class="i-faint" x1="{px0}" y1="{cy}" x2="{px1}" y2="{cy}"/><text class="i-t" x="{px0-14}" y="{cy+5}" text-anchor="end">{lab}</text>')
pts = ' '.join(f'{X(t):.1f},{100 - 42*math.sin(2*math.pi*t/20):.1f}' for t in [i*0.25 for i in range(161)])
a(f'<polyline class="i-line" points="{pts}" style="fill:none"/>')
for k in range(5):
    t = k * 10
    a(f'<circle class="i-cool-f" cx="{X(t):.1f}" cy="100" r="4.5"/>')
a(f'<text class="i-cool-t" x="{X(10):.1f}" y="166" text-anchor="middle">current passes zero every 10 ms at 50 Hz:</text>')
a(f'<text class="i-cool-t" x="{X(10):.1f}" y="182" text-anchor="middle">the breaker\'s arc goes out here</text>')
a(f'<line class="i-line" x1="{px0}" y1="196" x2="{px1}" y2="196"/>')
a(f'<text class="i-hot-t" x="{X(20):.1f}" y="246" text-anchor="middle">steady current, never zero: an arc keeps burning</text>')
for t in (0, 10, 20, 30, 40):
    a(f'<text class="i-n" x="{X(t):.1f}" y="270" text-anchor="middle">{t} ms</text>')
# right: clearing times on a log scale, 1 microsecond to 100 ms
rx0, rx1 = 640, 900
LX = lambda ms: rx0 + (math.log10(ms) + 3) / 5 * (rx1 - rx0)
a(f'<line class="i-faint" x1="530" y1="34" x2="530" y2="280"/>')
a(f'<text class="i-t" x="560" y="52">Time to clear a fault</text><text class="i-n" x="560" y="70">log scale, my rough placing of each</text>')
B = [('solid-state', 'a few microseconds', 0.005, 'i-cool-f'), ('fuse', 'several ms', 5, 'i-fill'), ('moulded case', 'up to about 20 ms', 20, 'i-metal')]
for i, (lab, tx, ms, cls) in enumerate(B):
    y = 92 + i * 52
    a(f'<text class="i-n" x="{rx0-8}" y="{y+15}" text-anchor="end">{lab}</text>')
    a(f'<rect class="{cls}" x="{rx0}" y="{y}" width="{LX(ms)-rx0:.1f}" height="22" rx="2"/>')
    a(f'<text class="i-n" x="{rx0}" y="{y+38}">{tx}</text>')
for ms, lab in ((0.001, '1 µs'), (0.1, '0.1 ms'), (10, '10 ms'), (100, '100 ms')):
    a(f'<line class="i-thin" x1="{LX(ms):.1f}" y1="246" x2="{LX(ms):.1f}" y2="252"/><text class="i-n" x="{LX(ms):.1f}" y="270" text-anchor="middle">{lab}</text>')
a(f'<line class="i-thin" x1="{rx0}" y1="249" x2="{rx1}" y2="249"/>')
save('offswitch', W, 284, ''.join(o), 'Left: alternating current swings above and below zero, passing zero every 10 milliseconds at 50 hertz, and a mechanical breaker\'s arc goes out at those moments. Direct current holds steady and never passes zero, so an arc keeps burning. Right: the time each kind of breaker takes to clear a fault, on a log scale, placed roughly: a solid-state breaker, a few microseconds; a fuse, several milliseconds; a moulded case breaker, up to about 20 milliseconds.')
print('ok')
