"""Four illustrations: the four clocks, the uprate steam loop, the meter, and the advanced reactors' gates."""
import os
D = os.path.dirname(os.path.abspath(__file__))
def save(name, W, H, body, aria):
    open(os.path.join(D, 'illos', name + '.svg'), 'w').write(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{body}</svg>')

# ---------- 1. The four clocks ----------
W, H = 940, 560
o = []; a = o.append
CX = [300, 460, 620, 780]       # column centres
cw = 150
heads = ['Grid place', 'Reactor', 'Licence', 'Fuel']
# column icons, drawn at y 40..100
def pylon(x, y):
    a(f'<path class="i-line" d="M{x-16} {y+60} L{x} {y} L{x+16} {y+60} M{x-11} {y+40} H{x+11} M{x-7} {y+22} H{x+7} M{x-22} {y+12} H{x+22}"/>')
    a(f'<path class="i-thin" d="M{x-22} {y+12} q -14 10 -30 14 M{x+22} {y+12} q 14 10 30 14"/>')
def reactor(x, y):
    a(f'<path class="i-metal" d="M{x-26} {y+60} V{y+24} A26 26 0 0 1 {x+26} {y+24} V{y+60} Z"/>')
    a(f'<rect class="i-fuel-soft" x="{x-9}" y="{y+30}" width="18" height="24" rx="2"/>')
def licence(x, y):
    a(f'<rect class="i-fill" x="{x-22}" y="{y+2}" width="44" height="58" rx="2"/>')
    for k in range(4): a(f'<line class="i-thin" x1="{x-14}" y1="{y+14+k*9}" x2="{x+[14,10,14,6][k]}" y2="{y+14+k*9}"/>')
    a(f'<circle class="i-hot-f" cx="{x+12}" cy="{y+50}" r="6" opacity=".8"/>')
def fuel(x, y):
    for k in range(3):
        a(f'<rect class="i-fuel" x="{x-20+k*14}" y="{y+8}" width="10" height="52" rx="2" opacity=".9"/>')
    a(f'<rect class="i-metal" x="{x-24}" y="{y+2}" width="40" height="6" rx="1"/>')
for x, f in zip(CX, [pylon, reactor, licence, fuel]): f(x, 34)
for x, h in zip(CX, heads): a(f'<text class="i-t" x="{x}" y="122" text-anchor="middle">{h}</text>')
LANES = [
 ('Restart', 'Crane, Palisades, Duane Arnold',
  [('part', 'kept, or borrowed and studied'), ('part', 'repair and rehire'), ('part', 'restore the old one'), ('held', 'ordinary fuel')]),
 ('Uprate', 'a running reactor, more heat',
  [('held', 'already connected'), ('part', 'meters to turbines'), ('part', 'an amendment'), ('held', 'ordinary fuel')]),
 ('New build,', 'ordinary fuel: BWRX-300, AP1000',
  [('zero', 'a new request'), ('zero', 'build from bare ground'), ('zero', 'permit, then licence'), ('held', 'ordinary fuel')]),
 ('New build,', 'HALEU: Natrium, Aurora, Hermes',
  [('zero', 'a new request'), ('zero', 'build from bare ground'), ('zero', 'permit, then licence'), ('choke', 'one demo line')]),
]
y = 150
for name, sub, cells in LANES:
    a(f'<line class="i-faint" x1="20" y1="{y-8}" x2="{W-20}" y2="{y-8}"/>')
    a(f'<text class="i-t" x="24" y="{y+26}">{name}</text><text class="i-n" x="24" y="{y+44}">{sub}</text>')
    for x, (st, note) in zip(CX, cells):
        cy = y + 30
        if st == 'held':
            a(f'<circle class="i-cool-f" cx="{x}" cy="{cy}" r="15" opacity=".9"/><path d="M{x-7} {cy} l5 5 l9 -10" style="fill:none;stroke:var(--bg);stroke-width:2.6"/>')
        elif st == 'part':
            a(f'<circle class="i-line" cx="{x}" cy="{cy}" r="15" style="fill:none"/><path class="i-cool-f" d="M{x} {cy-15} A15 15 0 0 1 {x} {cy+15} Z" opacity=".9"/>')
        elif st == 'zero':
            a(f'<circle class="i-line" cx="{x}" cy="{cy}" r="15" style="fill:none"/>')
        else:
            a(f'<rect class="i-choke" x="{x-cw/2+6}" y="{y-2}" width="{cw-12}" height="72" rx="6"/>')
            a(f'<circle class="i-hot" cx="{x}" cy="{cy}" r="15" style="fill:none;stroke-width:2.4"/><path class="i-hot" d="M{x-8} {cy-8} L{x+8} {cy+8} M{x+8} {cy-8} L{x-8} {cy+8}" style="stroke-width:2.4"/>')
        a(f'<text class="{"i-hot-t" if st == "choke" else "i-n"}" x="{x}" y="{cy+34}" text-anchor="middle">{note}</text>')
    y += 92
# legend
ly = y + 6
a(f'<line class="i-faint" x1="20" y1="{ly-14}" x2="{W-20}" y2="{ly-14}"/>')
items = [('held', 'Already held'), ('part', 'Part done: repair or paperwork'), ('zero', 'Starts from zero'), ('choke', 'The binding gate')]
lx = 24
for st, t in items:
    if st == 'held': a(f'<circle class="i-cool-f" cx="{lx+8}" cy="{ly+4}" r="8"/>')
    elif st == 'part': a(f'<circle class="i-line" cx="{lx+8}" cy="{ly+4}" r="8" style="fill:none"/><path class="i-cool-f" d="M{lx+8} {ly-4} A8 8 0 0 1 {lx+8} {ly+12} Z"/>')
    elif st == 'zero': a(f'<circle class="i-line" cx="{lx+8}" cy="{ly+4}" r="8" style="fill:none"/>')
    else: a(f'<circle class="i-hot" cx="{lx+8}" cy="{ly+4}" r="8" style="fill:none;stroke-width:2"/>')
    a(f'<text class="i-n" x="{lx+22}" y="{ly+8}">{t}</text>'); lx += 22 + len(t) * 7.4 + 34
H = ly + 22
save('clocks', W, H, ''.join(o), 'A grid of four kinds of nuclear project against the four things each needs: a grid place, a reactor, a licence and fuel. A restart, such as Crane, Palisades or Duane Arnold, has a grid place kept, or borrowed subject to the grid operator\'s studies, and ordinary fuel; its reactor needs repair and rehiring and its old licence must be restored. An uprate already holds its grid connection and ordinary fuel; it needs equipment from meters to turbines and a licence amendment. A new build on ordinary fuel, such as the BWRX-300 or AP1000, starts the grid place, the reactor and the licence from zero but has ordinary fuel. A new build on HALEU, such as Natrium, Aurora or Hermes, starts all three from zero and its fuel comes from one demonstration line: the binding gate.')

# ---------- 2. The uprate steam loop ----------
W, H = 940, 470
o = []; a = o.append
gy = 300   # ground line
a(f'<rect class="i-ground" x="0" y="{gy}" width="{W}" height="12"/><line class="i-line" x1="0" y1="{gy}" x2="{W}" y2="{gy}"/>')
# containment with reactor and steam generator
a(f'<path class="i-metal" d="M40 {gy} V150 A90 90 0 0 1 220 150 V{gy} Z" style="opacity:.55"/>')
a(f'<rect class="i-fill" x="66" y="190" width="54" height="100" rx="20"/><rect class="i-fuel-soft" x="78" y="214" width="30" height="56" rx="3"/>')
a(f'<text class="i-n" x="93" y="182" text-anchor="middle">core</text>')
a(f'<rect class="i-fill" x="146" y="140" width="46" height="140" rx="20"/><text class="i-n" x="169" y="118" text-anchor="middle">steam</text><text class="i-n" x="169" y="132" text-anchor="middle">generator</text>')
a(f'<path class="i-hot" d="M120 220 H146 M120 250 H146" style="stroke-width:2.4"/>')
# steam line to turbine
a(f'<path class="i-hot" d="M192 160 H250 V170 H300" style="stroke-width:3"/>')
# turbine (EPU zone)
tx = 300
a(f'<path class="i-metal" d="M{tx} 150 L{tx+150} 130 V230 L{tx} 210 Z"/>')
for k in range(6): a(f'<line class="i-thin" x1="{tx+18+k*22}" y1="{152-k*3}" x2="{tx+18+k*22}" y2="{208+k*3}"/>')
a(f'<text class="i-t" x="{tx+62}" y="254" text-anchor="middle">Turbine</text>')
# shaft and generator
a(f'<line class="i-line" x1="{tx+150}" y1="180" x2="{tx+190}" y2="180" style="stroke-width:4"/>')
gx = tx + 190
a(f'<rect class="i-metal" x="{gx}" y="140" width="90" height="80" rx="12"/><circle class="i-line" cx="{gx+45}" cy="180" r="22" style="fill:none"/>')
a(f'<text class="i-t" x="{gx+45}" y="262" text-anchor="middle">Generator</text>')
# transformer and pylon
trx = gx + 140
a(f'<line class="i-line" x1="{gx+90}" y1="160" x2="{trx}" y2="160"/>')
a(f'<rect class="i-metal" x="{trx}" y="190" width="70" height="{gy-190}" rx="3"/>')
for k in range(4): a(f'<line class="i-thin" x1="{trx+10+k*16}" y1="196" x2="{trx+10+k*16}" y2="{gy-6}"/>')
a(f'<path class="i-line" d="M{trx+35} 190 V160"/>')
a(f'<text class="i-t" x="{trx+35}" y="{gy+34}" text-anchor="middle">Transformer</text>')
px = trx + 130
a(f'<path class="i-line" d="M{px-24} {gy} L{px} 120 L{px+24} {gy} M{px-18} {gy-60} H{px+18} M{px-12} 200 H{px+12} M{px-30} 140 H{px+30}"/>')
a(f'<path class="i-thin" d="M{trx+70} 200 Q {px-50} 170 {px-30} 140"/>')
a(f'<text class="i-t" x="{px}" y="{gy+34}" text-anchor="middle">To the grid</text>')
# condenser and feedwater return with meter (MUR)
a(f'<path class="i-cool" d="M{tx+138} 228 V280 H230 V250 H192" style="stroke-width:2.6"/>')
a(f'<text class="i-n" x="262" y="294">condensed water returns</text>')
mx = 248
a(f'<circle class="i-cool-f" cx="{mx}" cy="280" r="11"/><path d="M{mx-6} 280 L{mx+5} 275" style="stroke:var(--bg);stroke-width:2"/>')
# control setpoints (stretch): a small panel by the containment
a(f'<rect class="i-fuel" x="236" y="60" width="64" height="40" rx="4" style="opacity:.9"/>')
for k in range(3): a(f'<circle cx="{252+k*16}" cy="80" r="4" style="fill:var(--bg)"/>')
a(f'<path class="i-lead" d="M236 80 Q 200 80 170 120"/>')
# EPU shading over turbine, generator, transformer
a(f'<rect class="i-choke" x="{tx-12}" y="112" width="{trx+82-(tx-12)}" height="{gy-104}" rx="8"/>')
# labels for types
def tag(x, y, cls, head, lines):
    a(f'<text class="{cls}" x="{x}" y="{y}">{head}</text>')
    for k, t in enumerate(lines): a(f'<text class="i-n" x="{x}" y="{y+16+k*15}">{t}</text>')
tag(40, 360, 'i-cool-t', '● Under 2%: measurement uncertainty recapture', ['Better meters on the returning water, so the plant knows', 'its true power and runs closer to its limit'])
tag(40, 420, 'i-fuel-t', '■ Up to 7%: stretch', ['Instrument settings moved within the', 'margins the plant was designed with'])
tag(500, 360, 'i-hot-t', '▢ Up to 20%: extended', ['New turbines, generators, pumps or transformers,', 'fitted while the reactor is shut to refuel. The same', 'heavy equipment the rest of the grid is queueing for'])
a(f'<path class="i-lead" d="M{mx} 291 V340"/>')
a(f'<text class="i-n" x="236" y="50">controls</text>')
save('uprate', W, H, ''.join(o), 'A simplified nuclear plant: the core heats water, which boils water in a steam generator; steam drives a turbine, which turns a generator; a transformer steps the power up for the grid; condensed water returns to the steam generator. A measurement uncertainty recapture uprate, under 2 per cent, fits better meters on the returning water. A stretch uprate, up to 7 per cent, moves instrument settings within the design margins. An extended uprate, up to 20 per cent, replaces the turbine, generator, pumps or transformer, during refuelling shutdowns, and needs the same heavy equipment the rest of the grid queues for.')

# ---------- 3. Behind or in front of the meter ----------
W, H = 940, 430
o = []; a = o.append
def plant(x, y):
    a(f'<path class="i-metal" d="M{x} {y} V{y-60} A34 34 0 0 1 {x+68} {y-60} V{y} Z"/>')
    a(f'<path class="i-fill" d="M{x+90} {y} C {x+98} {y-50}, {x+96} {y-80}, {x+92} {y-96} H{x+142} C {x+138} {y-80}, {x+136} {y-50}, {x+144} {y} Z"/>')
def dc(x, y):
    a(f'<rect class="i-fill" x="{x}" y="{y-56}" width="110" height="56" rx="3"/>')
    for k in range(5): a(f'<rect class="i-cool-f" x="{x+12+k*19}" y="{y-44}" width="11" height="34" rx="1" opacity=".75"/>')
def pyl(x, y):
    a(f'<path class="i-line" d="M{x-16} {y} L{x} {y-90} L{x+16} {y} M{x-12} {y-30} H{x+12} M{x-8} {y-60} H{x+8} M{x-22} {y-76} H{x+22}"/>')
def meter(x, y):
    a(f'<rect class="i-hot-f" x="{x-11}" y="{y-11}" width="22" height="22" rx="4"/><text x="{x}" y="{y+4}" text-anchor="middle" style="fill:var(--bg);font-size:11px;font-weight:700">M</text>')
half = W / 2
for p, title, sub in [(0, 'Behind the meter: co-located', 'The campus takes power before it reaches the grid'), (half, 'In front of the meter: through the grid', 'The plant sells into the grid; the campus buys from it')]:
    a(f'<text class="i-t" x="{p+24}" y="34">{title}</text><text class="i-n" x="{p+24}" y="52">{sub}</text>')
    a(f'<rect class="i-ground" x="{p+10}" y="270" width="{half-30}" height="10"/><line class="i-line" x1="{p+10}" y1="270" x2="{p+half-20}" y2="270"/>')
# left: plant -> DC directly; grid via meter
plant(30, 270); dc(230, 270)
a(f'<path class="i-hot" d="M176 190 H285 V214" style="stroke-width:2.8"/>')
pyl(400, 270); meter(400, 150)
a(f'<path class="i-thin" d="M285 190 H330 V150 H389" style="stroke-dasharray:4 3"/><text class="i-n" x="330" y="140" text-anchor="middle">top-up and backup</text>')
a(f'<text class="i-n" x="24" y="306">Example: Talen\'s Susquehanna plant and an Amazon</text><text class="i-n" x="24" y="322">campus beside it, until April 2026. FERC rejected a larger</text><text class="i-n" x="24" y="338">co-located load in November 2024; since December 2025</text><text class="i-n" x="24" y="354">co-located load in PJM must take a transmission service.</text>')
# right: plant -> meter -> grid -> meter -> DC; PPA paper
plant(half + 20, 270); pyl(half + 230, 270); dc(half + 330, 270)
meter(half + 180, 190); meter(half + 300, 190)
a(f'<path class="i-hot" d="M{half+166} 190 H{half+169} M{half+191} 190 H{half+289} M{half+311} 190 H{half+385} V214" style="stroke-width:2.8"/>')
a(f'<rect class="i-fill" x="{half+150}" y="74" width="160" height="44" rx="3"/><text class="i-t" x="{half+230}" y="94" text-anchor="middle">Power purchase</text><text class="i-n" x="{half+230}" y="110" text-anchor="middle">agreement, 20 years</text>')
a(f'<path class="i-lead" d="M{half+150} 96 Q {half+90} 96 {half+70} 140"/><path class="i-lead" d="M{half+310} 96 Q {half+380} 96 {half+385} 150"/>')
a(f'<text class="i-n" x="{half+24}" y="306">Every binding deal in PJM and MISO: Crane,</text><text class="i-n" x="{half+24}" y="322">Susquehanna since April 2026, Clinton, Duane Arnold,</text><text class="i-n" x="{half+24}" y="338">Calvert Cliffs, Vistra\'s plants and Google\'s uprates.</text><text class="i-n" x="{half+24}" y="354">The match between plant and campus is on paper.</text>')
a(f'<line class="i-faint" x1="{half}" y1="20" x2="{half}" y2="360"/>')
a(f'<text class="i-k" x="24" y="398">M = a meter, where power enters or leaves the grid and grid charges apply</text>')
save('meter', W, 410, ''.join(o), 'Two ways to supply a data centre from a nuclear plant. Behind the meter, or co-located, the campus sits beside the plant and takes power before it reaches the grid, using the grid only for top-up and backup; Talen\'s Susquehanna plant supplied an Amazon campus this way until April 2026, after FERC rejected a larger co-located load in November 2024, and since December 2025 co-located load in PJM must take a transmission service. In front of the meter, the plant sells all its output into the grid and the campus buys from the grid, with a 20-year power purchase agreement matching the two on paper. Every binding nuclear deal for AI on the PJM and MISO grids now works this way; the exception is Comanche Peak in Texas.')

# ---------- 4. The advanced reactors' gates ----------
W = 940
o = []; a = o.append
cols = ['Permit or approval', 'Ground broken', 'A buyer', 'Fuel source', 'Fuel enriched']
CX = [320, 445, 570, 695, 830]
for x, c in zip(CX, cols):
    for k, w in enumerate(c.split(' ', 1) if len(c) > 12 else [c]):
        a(f'<text class="i-t" x="{x}" y="{30+k*16}" text-anchor="middle">{w}</text>')
ROWS = [
 ('Kemmerer 1', 'TerraPower, 345 MW, 2030', ['done', 'done', 'part', 'part', 'no'],
  ['4 Mar 2026', 'under way', 'grid; Meta later', 'DOE, then ASP', 'ASP: not yet']),
 ('Aurora-ID', 'Oklo, 75 MW, 2028 to 2029', ['part', 'done', 'part', 'done', 'done'],
  ['2 of 5 DOE steps', 'Sep 2025', 'letters only', '5 t government', 'old reactor fuel']),
 ('Hermes 2', 'Kairos, up to 50 MW, 2030', ['done', 'part', 'done', 'no', 'no'],
  ['Nov 2024', 'site clearing', 'TVA, for Google', 'not named', '']),
 ('Long Mott', 'X-energy, 4 x 80 MW, early 2030s', ['part', 'no', 'part', 'done', 'part'],
  ['review done Oct 2026', '', 'Dow, then Amazon', 'Centrus contract', 'plant from 2029']),
]
y = 70
for name, sub, st, notes in ROWS:
    a(f'<line class="i-faint" x1="20" y1="{y-6}" x2="{W-20}" y2="{y-6}"/>')
    a(f'<text class="i-t" x="24" y="{y+22}">{name}</text><text class="i-n" x="24" y="{y+40}">{sub}</text>')
    for x, s, n in zip(CX, st, notes):
        cy = y + 22
        if s == 'done': a(f'<circle class="i-cool-f" cx="{x}" cy="{cy}" r="12" opacity=".9"/><path d="M{x-6} {cy} l4 4 l8 -9" style="fill:none;stroke:var(--bg);stroke-width:2.4"/>')
        elif s == 'part': a(f'<circle class="i-line" cx="{x}" cy="{cy}" r="12" style="fill:none"/><path class="i-cool-f" d="M{x} {cy-12} A12 12 0 0 1 {x} {cy+12} Z"/>')
        else: a(f'<circle class="i-hot" cx="{x}" cy="{cy}" r="12" style="fill:none;stroke-width:2"/>')
        if n: a(f'<text class="i-n" x="{x}" y="{cy+28}" text-anchor="middle">{n}</text>')
    y += 78
a(f'<rect class="i-choke" x="{CX[3]-62}" y="56" width="{CX[4]-CX[3]+124}" height="{y-56}" rx="8"/>')
a(f'<text class="i-hot-t" x="{(CX[3]+CX[4])/2}" y="{y+18}" text-anchor="middle">THE FUEL GATE</text>')
lx, ly = 24, y + 18
for s, t in [('done', 'Done'), ('part', 'Partly, or conditional'), ('no', 'Not yet')]:
    if s == 'done': a(f'<circle class="i-cool-f" cx="{lx+7}" cy="{ly-4}" r="7"/>')
    elif s == 'part': a(f'<circle class="i-line" cx="{lx+7}" cy="{ly-4}" r="7" style="fill:none"/><path class="i-cool-f" d="M{lx+7} {ly-11} A7 7 0 0 1 {lx+7} {ly+3} Z"/>')
    else: a(f'<circle class="i-hot" cx="{lx+7}" cy="{ly-4}" r="7" style="fill:none;stroke-width:2"/>')
    a(f'<text class="i-n" x="{lx+20}" y="{ly}">{t}</text>'); lx += 20 + len(t) * 7.4 + 30
save('advanced', W, y + 34, ''.join(o), 'Four advanced reactors tied to AI, all fuelled with HALEU, against five gates. Kemmerer 1, TerraPower, 345 MW, 2030: construction permit 4 March 2026, construction under way, selling to the grid with Meta funding later units of the design, a first core from a conditional government allocation and later fuel from ASP Isotopes, which had not enriched uranium by October 2026. Aurora-ID, Oklo, 75 MW, 2028 to 2029: two of five Energy Department steps, ground broken September 2025, letters of intent only, five tonnes of government HALEU recovered from old reactor fuel. Hermes 2, Kairos, up to 50 MW, 2030: permit November 2024, site clearing, TVA buying for Google, fuel source not named. Long Mott, X-energy, four 80 MW units, early 2030s: NRC safety review finished October 2026, not yet built, Dow as buyer with Amazon behind a later project, a Centrus fuel contract for a plant starting from 2029.')
print('illos ok')
