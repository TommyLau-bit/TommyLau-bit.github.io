"""Two illustrations: the chain from grid to rack, and a large transformer cut open."""
import os
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
def save(name, W, H, body, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# ---------- 1. The chain from grid to rack ----------
W = 940
o = []; a = o.append
gy = 250                      # ground line
a(f'<line class="i-ground" x1="10" y1="{gy}" x2="{W-10}" y2="{gy}"/>')
# voltage band labels across the top
bands = [(10, 250, 'Transmission: 115 to 345 kV'), (262, 548, 'Medium voltage: 13.8 or 34.5 kV'), (560, 930, 'Low voltage: 480 V and below')]
for x0, x1, t in bands:
    a(f'<path class="i-thin" d="M{x0} 34 V24 H{x1} V34"/><text class="i-k" x="{(x0+x1)/2}" y="16" text-anchor="middle">{t}</text>')
# 1 pylon
px = 40
a(f'<path class="i-line" d="M{px} {gy} L{px+18} 70 L{px+36} {gy} M{px+6} 200 H{px+30} M{px+11} 150 H{px+25} M{px-6} 92 H{px+42} M{px+3} 120 H{px+33}" style="fill:none"/>')
a(f'<path class="i-thin" d="M{px+42} 96 C{px+70} 112 {px+86} 112 {px+104} 104"/>')
# 2 substation: breaker + big transformer (the choke)
bx = 110
a(f'<rect class="i-choke" x="{bx-8}" y="78" width="148" height="{gy-78}" rx="6"/>')
a(f'<rect class="i-metal" x="{bx}" y="140" width="34" height="{gy-140}" rx="3"/>')               # breaker
a(f'<line class="i-thin" x1="{bx+17}" y1="104" x2="{bx+17}" y2="140"/>')
a(f'<rect class="i-fill" x="{bx+46}" y="130" width="80" height="{gy-130}" rx="4"/>')            # transformer tank
for k in range(3):
    a(f'<rect class="i-fill" x="{bx+54+k*24}" y="100" width="10" height="30" rx="3"/>')          # bushings
for k in range(5):
    a(f'<line class="i-thin" x1="{bx+130+k*0}" y1="{150+k*16}" x2="{bx+130}" y2="{150+k*16}"/>')
a(f'<text class="i-t" x="{bx+66}" y="{gy+22}" text-anchor="middle">1. Substation</text><text class="i-n" x="{bx+66}" y="{gy+38}" text-anchor="middle">breakers and a large</text><text class="i-n" x="{bx+66}" y="{gy+54}" text-anchor="middle">power transformer</text>')
a(f'<text class="i-hot-t" x="{bx+66}" y="{gy+74}" text-anchor="middle">the longest wait: years</text>')
# arrow helper
def arrow(x0, x1, y=200):
    a(f'<path class="i-line" d="M{x0} {y} H{x1}"/><path class="i-line" d="M{x1-7} {y-5} l7 5 l-7 5" style="fill:none"/>')
arrow(254, 276)
# 3 MV switchgear: row of cabinets
sx = 282
for k in range(4):
    a(f'<rect class="i-metal" x="{sx+k*30}" y="130" width="28" height="{gy-130}" rx="2"/><circle class="i-fill" cx="{sx+k*30+14}" cy="160" r="5"/><line class="i-thin" x1="{sx+k*30+6}" y1="190" x2="{sx+k*30+22}" y2="190"/>')
a(f'<text class="i-t" x="{sx+59}" y="{gy+22}" text-anchor="middle">2. Medium-voltage</text><text class="i-t" x="{sx+59}" y="{gy+38}" text-anchor="middle">switchgear</text><text class="i-n" x="{sx+59}" y="{gy+54}" text-anchor="middle">the campus fuse board</text>')
arrow(406, 428)
# 4 unit transformer
ux = 434
a(f'<rect class="i-fill" x="{ux}" y="160" width="70" height="{gy-160}" rx="4"/>')
for k in range(4):
    a(f'<line class="i-thin" x1="{ux+10}" y1="{172+k*14}" x2="{ux+60}" y2="{172+k*14}"/>')
a(f'<text class="i-t" x="{ux+35}" y="{gy+22}" text-anchor="middle">3. Unit</text><text class="i-t" x="{ux+35}" y="{gy+38}" text-anchor="middle">transformers</text><text class="i-n" x="{ux+35}" y="{gy+54}" text-anchor="middle">down to 480 volts</text>')
arrow(510, 560)
# 5 LV switchgear
lx = 566
for k in range(3):
    a(f'<rect class="i-metal" x="{lx+k*24}" y="150" width="22" height="{gy-150}" rx="2"/><line class="i-thin" x1="{lx+k*24+5}" y1="{170}" x2="{lx+k*24+17}" y2="170"/><line class="i-thin" x1="{lx+k*24+5}" y1="{186}" x2="{lx+k*24+17}" y2="186"/>')
a(f'<text class="i-t" x="{lx+35}" y="{gy+22}" text-anchor="middle">4. Low-voltage</text><text class="i-t" x="{lx+35}" y="{gy+38}" text-anchor="middle">switchgear</text>')
arrow(644, 666)
# 6 UPS + batteries
ux2 = 672
a(f'<rect class="i-metal" x="{ux2}" y="150" width="40" height="{gy-150}" rx="3"/>')
for k in range(4):
    a(f'<rect class="i-cool-f" x="{ux2+50}" y="{160+k*22}" width="26" height="16" rx="2"/>')
a(f'<text class="i-t" x="{ux2+38}" y="{gy+22}" text-anchor="middle">5. UPS and</text><text class="i-t" x="{ux2+38}" y="{gy+38}" text-anchor="middle">batteries</text><text class="i-n" x="{ux2+38}" y="{gy+54}" text-anchor="middle">bridge the seconds</text>')
# generator feeding the UPS from below-left
gx = 676
a(f'<rect class="i-choke" x="{gx-6}" y="{gy+70}" width="114" height="58" rx="6"/>')
a(f'<rect class="i-metal" x="{gx}" y="{gy+78}" width="70" height="42" rx="4"/><circle class="i-fill" cx="{gx+86}" cy="{gy+99}" r="12"/>')
a(f'<text class="i-t" x="{gx-16}" y="{gy+92}" text-anchor="end">6. Backup generators</text><text class="i-n" x="{gx-16}" y="{gy+108}" text-anchor="end">diesel or gas, run for days</text><text class="i-hot-t" x="{gx-16}" y="{gy+124}" text-anchor="end">some orders into 2029</text>')
arrow(756, 790)
# 7 racks
rx = 796
for k in range(3):
    a(f'<rect class="i-fill" x="{rx+k*42}" y="110" width="36" height="{gy-110}" rx="3"/>')
    for j in range(6):
        a(f'<line class="i-thin" x1="{rx+k*42+6}" y1="{124+j*20}" x2="{rx+k*42+30}" y2="{124+j*20}"/>')
a(f'<text class="i-t" x="{rx+60}" y="{gy+22}" text-anchor="middle">7. Busway and racks</text><text class="i-n" x="{rx+60}" y="{gy+38}" text-anchor="middle">a few dozen volts</text><text class="i-n" x="{rx+60}" y="{gy+54}" text-anchor="middle">at the chips</text>')
# key
a(f'<rect class="i-choke" x="20" y="{gy+92}" width="26" height="16" rx="3"/><text class="i-n" x="54" y="{gy+105}">shaded: the longest queues</text>')
save('chain', W, gy + 140, ''.join(o), 'The electrical chain from the grid to an AI rack, simplified. Power arrives on transmission lines at 115,000 to 345,000 volts. One: a substation with circuit breakers and a large power transformer steps it down to medium voltage, 13,800 or 34,500 volts; this has the longest wait, measured in years. Two: medium-voltage switchgear, the campus fuse board, routes it to each hall. Three: unit transformers step it down to 480 volts. Four: low-voltage switchgear divides it. Five: a UPS with batteries bridges the seconds after a fault. Six: backup generators, diesel or gas, start and can run for days; some orders are booked into 2029. Seven: busways carry power into the racks, where it reaches the chips at a few dozen volts.')

# ---------- 2. A large power transformer, cut open ----------
W, H = 960, 470
o = []; a = o.append
tx, ty, tw, th = 190, 150, 380, 240        # tank
gy = ty + th
a(f'<line class="i-ground" x1="40" y1="{gy+12}" x2="680" y2="{gy+12}"/>')
a(f'<rect class="i-line" x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="6" style="fill:none;stroke-width:2"/>')
a(f'<rect class="i-cool-f" x="{tx+4}" y="{ty+4}" width="{tw-8}" height="{th-8}" rx="4" opacity=".35"/>')   # oil
# core: three-limb steel, E shape with a top yoke
cx0, cy0, cw, ch = tx + 40, ty + 30, 300, 180
a(f'<path class="i-metal" d="M{cx0} {cy0} H{cx0+cw} V{cy0+ch} H{cx0} Z M{cx0+30} {cy0+30} H{cx0+120} V{cy0+ch-30} H{cx0+30} Z M{cx0+180} {cy0+30} H{cx0+cw-30} V{cy0+ch-30} H{cx0+180} Z" style="fill-rule:evenodd"/>')
for k in range(9):    # laminations hint on the top yoke
    a(f'<line class="i-thin" x1="{cx0+8+k*34}" y1="{cy0+4}" x2="{cx0+8+k*34}" y2="{cy0+26}" opacity=".5"/>')
# windings on the three limbs (copper)
for lx in (cx0 + 0, cx0 + 120, cx0 + cw - 30):
    a(f'<rect class="i-hot-f" x="{lx-14}" y="{cy0+38}" width="58" height="{ch-76}" rx="6" opacity=".8"/>')
    for j in range(7):
        a(f'<line class="i-thin" x1="{lx-14}" y1="{cy0+46+j*14}" x2="{lx+44}" y2="{cy0+46+j*14}" opacity=".6"/>')
# bushings on the lid
for k, bx in enumerate((tx + 80, tx + 190, tx + 300)):
    hgt = 110 if k < 3 else 80
    a(f'<rect class="i-fill" x="{bx-9}" y="{ty-hgt}" width="18" height="{hgt}" rx="3"/>')
    for j in range(6):
        a(f'<ellipse class="i-fill" cx="{bx}" cy="{ty-hgt+12+j*15}" rx="16" ry="4"/>')
    a(f'<circle class="i-metal" cx="{bx}" cy="{ty-hgt-4}" r="5"/>')
# conservator tank on top right
a(f'<rect class="i-metal" x="{tx+tw-46}" y="{ty-46}" width="96" height="26" rx="13"/><line class="i-thin" x1="{tx+tw-20}" y1="{ty-20}" x2="{tx+tw-20}" y2="{ty}"/>')
# tap changer box on the left wall
a(f'<rect class="i-metal" x="{tx-46}" y="{ty+60}" width="46" height="90" rx="4"/>')
for j in range(4):
    a(f'<circle class="i-fill" cx="{tx-23}" cy="{ty+76+j*20}" r="4"/>')
# radiators on the right wall
for k in range(5):
    a(f'<rect class="i-fill" x="{tx+tw+8+k*14}" y="{ty+30}" width="8" height="{th-60}" rx="2"/>')
a(f'<line class="i-thin" x1="{tx+tw}" y1="{ty+40}" x2="{tx+tw+76}" y2="{ty+40}"/><line class="i-thin" x1="{tx+tw}" y1="{ty+th-40}" x2="{tx+tw+76}" y2="{ty+th-40}"/>')
# callouts on the right
cxl = 690
notes = [
  (ty - 100, tx + 300 + 16, 'Bushings', 'carry each line through the lid;', 'some now wait 135 weeks from Sweden', True),
  (ty + 46, cx0 + cw - 2, 'Core', 'grain-oriented steel, stacked by hand;', 'about a quarter of the cost; one US mill', True),
  (ty + 126, cx0 + cw - 2 - 14, 'Windings', 'copper coils wrapped in paper;', 'about a quarter of the cost', False),
  (ty + 196, tx + tw - 10, 'Tank and oil', 'oil insulates and carries heat', 'out to the radiators and fans', False),
]
for y, x_from, t, n1, n2, hot in notes:
    a(f'<line class="i-lead" x1="{x_from}" y1="{y}" x2="{cxl-8}" y2="{y}"/>')
    a(f'<text class="i-t" x="{cxl}" y="{y-4}">{t}</text><text class="i-n" x="{cxl}" y="{y+13}">{n1}</text><text class="{"i-hot-t" if hot else "i-n"}" x="{cxl}" y="{y+29}">{n2}</text>')
# tap changer callout on the left
a(f'<text class="i-t" x="{tx-50}" y="{ty+176}" text-anchor="end">Tap changer</text><text class="i-n" x="{tx-50}" y="{ty+192}" text-anchor="end">adjusts the ratio</text><text class="i-n" x="{tx-50}" y="{ty+208}" text-anchor="end">10 to 22 weeks</text>')
a(f'<line class="i-lead" x1="{tx-23}" y1="{ty+150}" x2="{tx-23}" y2="{ty+162}"/>')
# bottom strip
yb = gy + 46
a(f'<text class="i-t" x="40" y="{yb}">A large unit weighs about 100 to 400 tons</text><text class="i-n" x="40" y="{yb+18}">most railcars carry about 100; it travels drained, without its bushings, and is rebuilt on site</text>')
save('transformer', W, yb + 30, ''.join(o), 'A large power transformer cut open, simplified, not to scale. A steel tank full of insulating oil holds a core of grain-oriented electrical steel, stacked by hand, with three limbs. Copper windings wrapped in paper sit on each limb. The core steel and the copper each make up about a quarter of the cost, and America has one mill that makes the steel. Tall insulated bushings carry each line through the lid; some now take 135 weeks from Hitachi Energy\'s Swedish plant. A tap changer on the side adjusts the ratio of turns, quoted at 10 to 22 weeks. Radiators on the other side shed the oil\'s heat. A large unit weighs about 100 to 400 tons, while most railcars carry about 100, so it travels drained and stripped and is rebuilt on site.')
print('illos ok')
