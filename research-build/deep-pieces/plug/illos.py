"""Two illustrations: the path from application to running, and what a data centre does in a voltage dip."""
import os
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(D, 'illos'), exist_ok=True)
def save(name, W, H, body, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# ---------- 1. The path: five steps, one of which no rule can hurry ----------
W = 940; o = []; a = o.append
gy = 190
a(f'<line class="i-ground" x1="10" y1="{gy}" x2="{W-10}" y2="{gy}"/>')
C = [92, 280, 470, 660, 850]
def arrow(x0, x1, y=130):
    a(f'<path class="i-line" d="M{x0} {y} H{x1}"/><path class="i-line" d="M{x1-7} {y-5} l7 5 l-7 5" style="fill:none"/>')
for i in range(4):
    arrow(C[i] + 62, C[i+1] - 62)
# 1 apply: a form with a megawatt figure, and a deposit
x = C[0]
a(f'<rect class="i-fill" x="{x-34}" y="70" width="56" height="74" rx="3"/>')
for k in range(4):
    a(f'<line class="i-thin" x1="{x-26}" y1="{86+k*12}" x2="{x+(8 if k%2 else 14)}" y2="{86+k*12}"/>')
a(f'<text class="i-k" x="{x-6}" y="138" text-anchor="middle">300 MW</text>')
for k in range(4):
    a(f'<ellipse class="i-metal" cx="{x+40}" cy="{gy-8-k*8}" rx="16" ry="5"/>')
# 2 study: a network of nodes, and a lens
x = C[1]
N = [(x-44, 90), (x-10, 70), (x+30, 96), (x-30, 140), (x+16, 150), (x+46, 130)]
for (p, q) in [(0, 1), (1, 2), (0, 3), (3, 4), (4, 5), (2, 5), (1, 4)]:
    a(f'<line class="i-thin" x1="{N[p][0]}" y1="{N[p][1]}" x2="{N[q][0]}" y2="{N[q][1]}"/>')
for nx, ny in N:
    a(f'<circle class="i-fill" cx="{nx}" cy="{ny}" r="5"/>')
a(f'<circle class="i-line" cx="{x+18}" cy="118" r="20" style="fill:none"/><line class="i-line" x1="{x+32}" y1="132" x2="{x+50}" y2="152"/>')
# 3 upgrades: the choke, a pylon and a transformer
x = C[2]
a(f'<rect class="i-choke" x="{x-74}" y="40" width="148" height="{gy-40}" rx="6"/>')
a(f'<path class="i-line" d="M{x-50} {gy} L{x-34} 58 L{x-18} {gy} M{x-44} 150 H{x-24} M{x-40} 110 H{x-28} M{x-58} 76 H{x-10}" style="fill:none"/>')
a(f'<rect class="i-fill" x="{x}" y="112" width="56" height="{gy-112}" rx="4"/>')
for k in range(3):
    a(f'<rect class="i-fill" x="{x+6+k*18}" y="88" width="8" height="24" rx="3"/>')
a(f'<line class="i-thin" x1="{x+8}" y1="130" x2="{x+48}" y2="130"/><line class="i-thin" x1="{x+8}" y1="146" x2="{x+48}" y2="146"/>')
# 4 switch on: a fork to firm or cut first
x = C[3]
a(f'<path class="i-line" d="M{x-50} 130 H{x-10} L{x+20} 92 H{x+52} M{x-10} 130 L{x+20} 168 H{x+52}" style="fill:none"/>')
a(f'<circle class="i-fill" cx="{x-10}" cy="130" r="5"/>')
a(f'<text class="i-n" x="{x+14}" y="84">firm</text><text class="i-hot-t" x="{x+14}" y="160">cut first</text>')
# 5 run: hall, UPS battery, generator
x = C[4]
a(f'<rect class="i-fill" x="{x-56}" y="84" width="74" height="{gy-84}" rx="3"/>')
for k in range(3):
    a(f'<rect class="i-metal" x="{x-48+k*22}" y="100" width="14" height="{gy-112}" rx="1"/>')
a(f'<rect class="i-cool-f" x="{x+26}" y="132" width="26" height="{gy-132}" rx="2"/><text class="i-k" x="{x+39}" y="126" text-anchor="middle">UPS</text>')
a(f'<rect class="i-metal" x="{x+56}" y="150" width="30" height="{gy-150}" rx="2"/><line class="i-thin" x1="{x+62}" y1="150" x2="{x+62}" y2="140"/><text class="i-k" x="{x+71}" y="136" text-anchor="middle">gen</text>')
# labels under each step
L = [('1. Apply', 'site, megawatts, deposit', 'to the local utility', 'weeks'),
     ('2. Study', 'what the wires can carry', 'utility and grid operator', 'FERC wants 60 to 90 days'),
     ('3. Build the upgrades', 'lines, substations, transformers', 'factories and the utility', 'years: no rule hurries it'),
     ('4. Switch on', 'firm, or on a tier cut first', 'utility and grid operator', 'firm waits for step 3'),
     ('5. Run', 'hold on in a dip, pay the bill', 'the site', 'every year after')]
for x, (t, n1, n2, tm) in zip(C, L):
    a(f'<text class="i-t" x="{x}" y="{gy+24}" text-anchor="middle">{t}</text><text class="i-n" x="{x}" y="{gy+41}" text-anchor="middle">{n1}</text><text class="i-n" x="{x}" y="{gy+57}" text-anchor="middle">{n2}</text>')
    a(f'<text class="{"i-hot-t" if t.startswith("3") else "i-k"}" x="{x}" y="{gy+77}" text-anchor="middle">{tm}</text>')
a(f'<text class="i-head" x="10" y="22">Who decides each step, and how long it takes</text>')
save('path', W, gy + 92, ''.join(o), 'The five steps from application to running for a large data centre in America. One, apply: the developer files its site, megawatts and a deposit with the local utility, in weeks. Two, study: the utility and grid operator check what the wires can carry; FERC wants studies done in 60 to 90 days. Three, build the upgrades: new lines, substations and transformers, made by factories and built by the utility, which takes years and is the step no rule can hurry; it is shaded. Four, switch on: firm service waits for step three, or the site switches on now on a tier the grid may cut first. Five, run: the site must hold on through voltage dips, with its UPS batteries and generators, and pays its share of the bill every year.')

# ---------- 2. The dip: what the grid sees, what the site does, and PJM's new rule ----------
W = 940; o = []; a = o.append
# left panel: voltage at the site over about a minute and a half, not to scale in time
px0, px1, vy0, vy1 = 70, 548, 40, 190          # voltage plot box (1.2 pu at top, 0 at bottom)
V = lambda pu: vy1 - pu / 1.2 * (vy1 - vy0)
a(f'<text class="i-head" x="10" y="18">What the site sees on the line, and what it does</text>')
for pu, lab in ((1.0, 'normal'), (0.5, 'half')):
    a(f'<line class="i-faint" x1="{px0}" y1="{V(pu):.1f}" x2="{px1}" y2="{V(pu):.1f}"/><text class="i-k" x="{px0-8}" y="{V(pu)+4:.1f}" text-anchor="end">{lab}</text>')
a(f'<line class="i-ground" x1="{px0}" y1="{vy1}" x2="{px1}" y2="{vy1}"/>')
dips = [130, 250, 370]
d = [f'M{px0} {V(1.0):.1f}']
for k, x in enumerate(dips):
    d.append(f'H{x} L{x+4} {V(0.3):.1f} H{x+12} L{x+16} {V(1.0):.1f}')
d.append(f'H{dips[-1]+40} C{dips[-1]+52} {V(1.0):.1f} {dips[-1]+56} {V(1.09):.1f} {dips[-1]+70} {V(1.09):.1f} H{dips[-1]+96} C{dips[-1]+110} {V(1.09):.1f} {dips[-1]+120} {V(1.0):.1f} {dips[-1]+140} {V(1.0):.1f} H{px1}')
a(f'<path class="i-line" d="{" ".join(d)}" style="fill:none"/>')
for k, x in enumerate(dips):
    a(f'<text class="i-n" x="{x+8}" y="{V(0.3)+16:.1f}" text-anchor="middle">{"fault" if k == 0 else "retry"}</text>')
a(f'<text class="i-k" x="{dips[0]+8}" y="{vy0-6}" text-anchor="middle">cleared in about 0.05 s</text>')
a(f'<text class="i-hot-t" x="{dips[-1]+80}" y="{V(1.09)-8:.1f}" text-anchor="middle">voltage overshoots</text>')
# lower lane: the site's draw from the grid, and the UPS's count
ly = 250
a(f'<text class="i-k" x="{px0-8}" y="{ly-14}" text-anchor="end">draw</text>')
a(f'<path class="i-cool" d="M{px0} {ly-20} H{dips[-1]+12} L{dips[-1]+16} {ly+10} H{px1}" style="fill:none"/>')
for k, x in enumerate(dips):
    a(f'<circle class="{"i-hot-f" if k == 2 else "i-fill"}" cx="{x+8}" cy="{ly+34}" r="11"/><text class="i-t" x="{x+8}" y="{ly+39}" text-anchor="middle">{k+1}</text>')
a(f'<text class="i-n" x="{px0}" y="{ly+66}">The UPS counts the dips. A common setting: three within a minute,</text>')
a(f'<text class="i-n" x="{px0}" y="{ly+82}">and the site moves to its generators until staff switch it back.</text>')
a(f'<text class="i-hot-t" x="{dips[-1]+26}" y="{ly+39}">the site leaves the grid</text>')
# right panel: PJM's proposed envelope, how long a site must stay on at each voltage
rx0 = 640; rw = 280
a(f'<text class="i-head" x="{rx0-20}" y="18">PJM\'s proposed rule: stay on for at least</text>')
B = [('above 1.2', 'may trip', 0), ('1.1 to 1.2', '1 s', 0.42), ('0.9 to 1.1', 'always', 1.0), ('0.8 to 0.9', '2 s', 0.55), ('0.5 to 0.8', '0.5 s', 0.3), ('below 0.5', '0.25 s', 0.18)]
for i, (band, t, w) in enumerate(B):
    y = 40 + i * 40
    a(f'<text class="i-k" x="{rx0-10}" y="{y+17}" text-anchor="end">{band}</text>')
    if w:
        a(f'<rect class="{"i-cool-f" if t == "always" else "i-fill"}" x="{rx0}" y="{y}" width="{rw*w*0.78:.0f}" height="24" rx="2"/>')
    a(f'<text class="i-n" x="{rx0 + rw*w*0.78 + 8:.0f}" y="{y+17}">{t}</text>')
a(f'<text class="i-n" x="{rx0-20}" y="{40+6*40+12}">Voltage as a share of normal. Then back to 90%</text>')
a(f'<text class="i-n" x="{rx0-20}" y="{40+6*40+28}">of its earlier draw within 2 seconds.</text>')
a(f'<line class="i-faint" x1="600" y1="30" x2="600" y2="340"/>')
save('ridethrough', W, 350, ''.join(o), 'Left: what a data centre sees in a fault the grid clears normally. Voltage on the line falls to about a third of normal for about a twentieth of a second, the fault is cleared, and the line is retried twice, each retry another dip. The UPS counts the dips; a common setting is three within a minute, after which the site moves to its generators and stays there until staff switch it back. Its draw from the grid falls to nothing, and with that load gone the voltage overshoots. Right: PJM\'s proposed rule, how long a site must stay connected at each voltage: above 1.2 times normal it may trip; 1.1 to 1.2, one second; 0.9 to 1.1, always; 0.8 to 0.9, two seconds; 0.5 to 0.8, half a second; below half, a quarter of a second. It must then return to 90 per cent of its earlier draw within two seconds.')
print('ok')
