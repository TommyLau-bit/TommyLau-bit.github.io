"""Three illustrations: one watt of heat from the chip to the sky; the three roof machines; why warm coolant frees the roof."""
import os
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
def save(name, W, H, body, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# ---------- 1. The chain: one watt from the chip to the outside air ----------
W = 940; o = []; a = o.append
C = [90, 285, 475, 665, 855]
HY, CY = 96, 150          # hot pipe, cool pipe
# sealed zone and water zone
a(f'<rect class="i-faint" x="16" y="34" width="{C[3]+70-16}" height="160" rx="8"/>')
a(f'<text class="i-cool-t" x="{(16+C[3]+70)/2:.0f}" y="50" text-anchor="middle">sealed loops: no water lost</text>')
a(f'<rect class="i-choke" x="{C[4]-80}" y="34" width="160" height="160" rx="8"/>')
a(f'<text class="i-hot-t" x="{C[4]}" y="50" text-anchor="middle">can spend water</text>')
# pipes between stations
for i in range(4):
    x0, x1 = C[i] + 52, C[i+1] - 52
    a(f'<path class="i-hot" d="M{x0} {HY} H{x1}"/><path class="i-hot" d="M{x1-7} {HY-5} l7 5 l-7 5"/>')
    a(f'<path class="i-cool" d="M{x1} {CY} H{x0}"/><path class="i-cool" d="M{x0+7} {CY-5} l-7 5 l7 5"/>')
# 1 chip with cold plate
x = C[0]
a(f'<rect class="i-fill" x="{x-46}" y="140" width="92" height="28" rx="3"/>')
a(f'<rect class="i-metal" x="{x-26}" y="122" width="52" height="18" rx="2"/>')
a(f'<rect class="i-fill" x="{x-34}" y="88" width="68" height="34" rx="3"/>')
for k in range(5):
    a(f'<line class="i-thin" x1="{x-26+k*13}" y1="94" x2="{x-26+k*13}" y2="116"/>')
a(f'<text class="i-k" x="{x}" y="82" text-anchor="middle">cold plate</text>')
# 2 rack
x = C[1]
a(f'<rect class="i-fill" x="{x-34}" y="66" width="68" height="112" rx="3"/>')
for k in range(7):
    a(f'<rect class="i-fill" x="{x-28}" y="{72+k*14}" width="44" height="9" rx="1"/>')
a(f'<line class="i-hot" x1="{x+24}" y1="70" x2="{x+24}" y2="174"/><line class="i-cool" x1="{x+29}" y1="70" x2="{x+29}" y2="174"/>')
# 3 CDU: pump and plate exchanger
x = C[2]
a(f'<rect class="i-fill" x="{x-40}" y="78" width="80" height="96" rx="4"/>')
a(f'<circle class="i-metal" cx="{x-16}" cy="146" r="13"/><path class="i-line" d="M{x-22} 146 l6 -6 l6 6 l-6 6 z"/>')
a(f'<path class="i-line" d="M{x+8} 90 l8 8 l-8 8 l8 8 l-8 8 l8 8 l-8 8 l8 8" style="fill:none"/>')
a(f'<path class="i-line" d="M{x+22} 90 l8 8 l-8 8 l8 8 l-8 8 l8 8 l-8 8 l8 8" style="fill:none"/>')
# 4 facility water: risers through a floor
x = C[3]
a(f'<line class="i-line" x1="{x-50}" y1="124" x2="{x+50}" y2="124"/>')
a(f'<line class="i-hot" x1="{x-8}" y1="{HY}" x2="{x-8}" y2="176"/><line class="i-cool" x1="{x+8}" y1="{CY}" x2="{x+8}" y2="70"/>')
a(f'<text class="i-n" x="{x+16}" y="78">to the roof</text>')
# 5 roof: dry cooler with fans
x = C[4]
a(f'<rect class="i-fill" x="{x-56}" y="112" width="112" height="44" rx="3"/>')
for k in range(3):
    a(f'<circle class="i-fill" cx="{x-36+k*36}" cy="100" r="13"/><line class="i-thin" x1="{x-46+k*36}" y1="100" x2="{x-26+k*36}" y2="100"/>')
for k in range(6):
    a(f'<line class="i-thin" x1="{x-48+k*19}" y1="118" x2="{x-48+k*19}" y2="150"/>')
for k in range(3):
    a(f'<path class="i-dash" d="M{x-30+k*30} 84 q6 -10 0 -20"/>')
a(f'<text class="i-n" x="{x}" y="176" text-anchor="middle">tower or dry cooler</text>')
# temperatures on the pipes
a(f'<text class="i-hot-t" x="{(C[0]+C[1])/2:.0f}" y="{HY-10}" text-anchor="middle">about 55°C</text>')
a(f'<text class="i-cool-t" x="{(C[0]+C[1])/2:.0f}" y="{CY+20}" text-anchor="middle">45°C in</text>')
a(f'<text class="i-cool-t" x="{(C[2]+C[3])/2:.0f}" y="{CY+20}" text-anchor="middle">about 41°C</text>')
L = [('1. Chip', 'coolant runs through a', 'copper plate on the chip'),
     ('2. Rack loop', 'water and glycol,', 'sealed inside the rack'),
     ('3. CDU', 'pumps and a heat exchanger;', 'the liquids never mix'),
     ('4. Facility water', 'the building\'s loop', 'carries heat upward'),
     ('5. The roof', 'heat leaves to the air;', 'water is spent only here')]
for (t, l1, l2), x in zip(L, C):
    a(f'<text class="i-t" x="{x}" y="216" text-anchor="middle">{t}</text><text class="i-n" x="{x}" y="234" text-anchor="middle">{l1}</text><text class="i-n" x="{x}" y="250" text-anchor="middle">{l2}</text>')
save('chain', W, 262, ''.join(o), 'Drawing of one watt of heat travelling from an AI chip to the outside air in five steps. One: a copper cold plate on the chip, with coolant running through it. Two: the rack loop of water and glycol, entering at 45 degrees and leaving the chip at about 55. Three: the coolant distribution unit, pumps and a heat exchanger, where the rack loop hands its heat to the building water without the two mixing. Four: the facility water, arriving at the unit at about 41 degrees and carrying heat up to the roof. Five: the roof, a cooling tower or a dry cooler, where the heat leaves to the air. The first four steps are sealed loops that lose no water; only the fifth can spend water.')

# ---------- 2. The three roof machines ----------
W = 940; o = []; a = o.append
C = [160, 470, 780]; base = 170
a(f'<text class="i-head" x="10" y="20">Three ways to put the heat into the sky</text>')
a(f'<rect class="i-ground" x="10" y="{base}" width="{W-20}" height="6"/>')
# tower: a box with fill, fan on top, vapour
x = C[0]
a(f'<path class="i-fill" d="M{x-60} {base} L{x-46} 70 H{x+46} L{x+60} {base} Z"/>')
for k in range(4):
    a(f'<line class="i-thin" x1="{x-44+k*4}" y1="{110+k*14}" x2="{x+44-k*4}" y2="{110+k*14}"/>')
a(f'<circle class="i-fill" cx="{x}" cy="62" r="16"/><line class="i-thin" x1="{x-12}" y1="62" x2="{x+12}" y2="62"/>')
for k in range(3):
    a(f'<path class="i-dash" d="M{x-22+k*22} 42 q8 -10 0 -22"/>')
a(f'<text class="i-cool-t" x="{x+70}" y="40">vapour</text>')
# dry cooler: V coil with fans
x = C[1]
a(f'<path class="i-fill" d="M{x-90} 80 L{x-20} {base} H{x+20} L{x+90} 80 Z"/>')
for k in range(5):
    a(f'<line class="i-thin" x1="{x-80+k*10}" y1="{92+k*16}" x2="{x+80-k*10}" y2="{92+k*16}"/>')
for k in range(3):
    a(f'<circle class="i-fill" cx="{x-50+k*50}" cy="66" r="16"/><line class="i-thin" x1="{x-62+k*50}" y1="66" x2="{x-38+k*50}" y2="66"/>')
# chiller: box, compressor, fans
x = C[2]
a(f'<rect class="i-fill" x="{x-90}" y="86" width="180" height="{base-86}" rx="4"/>')
a(f'<circle class="i-metal" cx="{x-48}" cy="132" r="22"/><text class="i-k" x="{x-48}" y="136" text-anchor="middle">comp</text>')
for k in range(2):
    a(f'<circle class="i-fill" cx="{x+12+k*46}" cy="72" r="16"/><line class="i-thin" x1="{x+k*46}" y1="72" x2="{x+24+k*46}" y2="72"/>')
a(f'<path class="i-hot" d="M{x+4} 132 H{x+76}"/><path class="i-cool" d="M{x+4} 150 H{x+76}"/>')
T = [('Cooling tower', 'evaporates about 1 to 2 L per kWh', 'cools water below the air,', 'towards the wet bulb', 'little power'),
     ('Dry cooler', 'uses no water', 'cools water only to a few', 'degrees above the air', 'fan power, more when hot'),
     ('Chiller', 'air-cooled: no water', 'makes water colder than the', 'air with a compressor', 'about 0.25 kW per kW at 35°C')]
for (t, wl, c1, c2, pw), x in zip(T, C):
    a(f'<text class="i-t" x="{x}" y="204" text-anchor="middle">{t}</text>')
    a(f'<text class="i-cool-t" x="{x}" y="224" text-anchor="middle">{wl}</text>')
    a(f'<text class="i-n" x="{x}" y="244" text-anchor="middle">{c1}</text><text class="i-n" x="{x}" y="260" text-anchor="middle">{c2}</text>')
    a(f'<text class="i-hot-t" x="{x}" y="282" text-anchor="middle">{pw}</text>')
save('roof', W, 294, ''.join(o), 'Drawing of three machines that put a data centre\'s heat into the outside air. A cooling tower sprays water over packing and evaporates about 1 to 2 litres per kilowatt-hour of heat; it can cool water below the air temperature, towards the wet-bulb temperature, for little power. A dry cooler is a radiator with fans; it uses no water but can only cool water to a few degrees above the air, and its fans use more power when it is hot. A chiller uses a compressor to make water colder than the air; an air-cooled chiller uses no water, and at 35 degree air it costs about a quarter of a kilowatt for each kilowatt of heat removed.')

# ---------- 3. The ladder: why warm coolant frees the roof ----------
W = 940; o = []; a = o.append
T0, T1, yb, yt = 0, 60, 300, 50
Y = lambda t: yb - (t - T0) / (T1 - T0) * (yb - yt)
a(f'<text class="i-head" x="10" y="20">Each degree of coolant adds hours when fans alone can do the job</text>')
sx = 150
a(f'<line class="i-line" x1="{sx}" y1="{Y(0)}" x2="{sx}" y2="{Y(60)}"/>')
for t in range(0, 61, 10):
    a(f'<line class="i-thin" x1="{sx-6}" y1="{Y(t):.0f}" x2="{sx}" y2="{Y(t):.0f}"/><text class="i-n" x="{sx-10}" y="{Y(t)+4:.0f}" text-anchor="end">{t}°C</text>')
# coolant marks, right of the scale
M = [(55, 'out of the chip, about 55°C', 'i-hot-t'), (45, 'into the rack, 45°C', 'i-hot-t'), (41, 'building water, about 41°C', 'i-hot-t'), (18, 'old air hall\'s chilled water, about 18°C', 'i-cool-t')]
for t, lab, cls in M:
    a(f'<line class="i-thin" x1="{sx}" y1="{Y(t):.0f}" x2="{sx+18}" y2="{Y(t):.0f}"/><circle class="{"i-hot-f" if "hot" in cls else "i-cool-f"}" cx="{sx}" cy="{Y(t):.0f}" r="4"/><text class="{cls}" x="{sx+24}" y="{Y(t)+4:.0f}">{lab}</text>')
# two columns: when outside air is cool enough for a dry cooler alone
for x, lo, hi, t1, t2 in [(560, 10, 13, 'Old air hall', 'fans alone below about 10 to 13°C'), (800, 33, 36, 'Hall at 41°C water', 'fans alone below about 33 to 36°C')]:
    a(f'<rect class="i-cool-f" x="{x-36}" y="{Y(lo):.0f}" width="72" height="{Y(0)-Y(lo):.0f}" rx="2" style="opacity:.35"/>')
    a(f'<rect class="i-cool-f" x="{x-36}" y="{Y(hi):.0f}" width="72" height="{Y(lo)-Y(hi):.0f}" rx="2" style="opacity:.18"/>')
    a(f'<line class="i-dash" x1="{sx}" y1="{Y(hi):.0f}" x2="{x+36}" y2="{Y(hi):.0f}"/>')
    a(f'<text class="i-t" x="{x}" y="{Y(hi)-30:.0f}" text-anchor="middle">{t1}</text><text class="i-n" x="{x}" y="{Y(hi)-12:.0f}" text-anchor="middle">{t2}</text>')
a(f'<text class="i-n" x="680" y="{Y(0)+20:.0f}" text-anchor="middle">shaded: outside air temperatures at which a dry cooler needs no chiller</text>')
save('ladder', W, Y(0) + 30, ''.join(o), 'Drawing of a temperature scale from 0 to 60 degrees. Coolant temperatures are marked: about 55 degrees out of the chip, 45 into the rack, about 41 for the building water, and about 18 for an old air-cooled hall\'s chilled water. Two shaded columns show the outside air temperatures at which a dry cooler alone can do the job, assuming a gap of 5 to 8 degrees: for the old air hall, below about 10 to 13 degrees; for a hall with 41 degree water, below about 33 to 36 degrees, which in many climates is nearly every hour of the year, though not in the hottest deserts.')
print('ok')
