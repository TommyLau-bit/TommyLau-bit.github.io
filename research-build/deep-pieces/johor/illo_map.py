"""Schematic map of southern Johor and Singapore: coast from approximate lat/lon, projected
linearly (no curvature at 1.5 degrees north), data centre clusters, power plants, the new
500 kV backbone and Jurong Island. Not to scale in detail; positions are approximate."""
import os
D = os.path.dirname(os.path.abspath(__file__))
LON0, LON1, LAT0, LAT1 = 102.98, 104.32, 1.18, 2.06
W = 940
K = W / (LON1 - LON0)
H = round((LAT1 - LAT0) * K)
P = lambda lon, lat: (round((lon - LON0) * K, 1), round((LAT1 - lat) * K, 1))
poly = lambda pts: 'M' + ' L'.join(f'{P(*p)[0]} {P(*p)[1]}' for p in pts) + ' Z'

johor = [(102.98, 2.06), (102.98, 1.86), (103.10, 1.72), (103.25, 1.60), (103.39, 1.49), (103.46, 1.37),
         (103.51, 1.27), (103.55, 1.32), (103.59, 1.37), (103.63, 1.40), (103.67, 1.43), (103.72, 1.45),
         (103.77, 1.465), (103.82, 1.472), (103.88, 1.455), (103.95, 1.445), (104.02, 1.45), (104.06, 1.40),
         (104.10, 1.36), (104.18, 1.40), (104.26, 1.55), (104.25, 1.80), (104.20, 2.06)]
sg = [(103.64, 1.32), (103.66, 1.35), (103.70, 1.40), (103.75, 1.435), (103.80, 1.448), (103.84, 1.445),
      (103.88, 1.42), (103.93, 1.40), (103.99, 1.39), (104.03, 1.355), (104.00, 1.32), (103.93, 1.30),
      (103.86, 1.275), (103.80, 1.27), (103.74, 1.285), (103.68, 1.30)]
jurong = [(103.665, 1.268), (103.69, 1.286), (103.725, 1.278), (103.72, 1.252), (103.685, 1.250)]

o = []; a = o.append
a('<defs><marker id="mh" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" style="fill:var(--ink-3)"/></marker></defs>')
a(f'<rect x="0" y="0" width="{W}" height="{H}" style="fill:color-mix(in srgb, var(--cool) 14%, var(--bg))"/>')
a(f'<path d="{poly(johor)}" style="fill:var(--bg);stroke:var(--ink-2);stroke-width:1.2"/>')
a(f'<path class="i-metal" d="{poly(sg)}"/>')
a(f'<path class="i-fuel-soft" d="{poly(jurong)}"/>')

# causeway and second link
for (l1, t1, l2, t2) in [(103.768, 1.462, 103.768, 1.444), (103.635, 1.37, 103.638, 1.335)]:
    x1, y1 = P(l1, t1); x2, y2 = P(l2, t2)
    a(f'<line class="i-line" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" style="stroke-width:3"/>')

# the new 500 kV backbone, arriving from the north, ending at Kulai East
bx, by = P(103.40, 2.06); kx, ky = P(103.635, 1.675)
a(f'<path class="i-hot" d="M{bx} {by} C {bx+40} {by+120}, {kx-60} {ky-90}, {kx} {ky}" style="stroke-dasharray:7 4"/>')
a(f'<rect class="i-hot-f" x="{kx-6}" y="{ky-6}" width="12" height="12"/>')
# existing 500 kV at Yong Peng East, just off the map to the north west
yx, yy = P(103.06, 2.02)
a(f'<path class="i-line" d="M{yx} {yy-20} V{yy+4}"/><rect class="i-fill" x="{yx-5}" y="{yy+4}" width="10" height="10"/>')

def site(lon, lat, r=7, cls='i-cool-f'):
    x, y = P(lon, lat); a(f'<circle class="{cls}" cx="{x}" cy="{y}" r="{r}" opacity=".85"/>'); return x, y
def plant(lon, lat):
    x, y = P(lon, lat); a(f'<rect class="i-fuel" x="{x-7}" y="{y-7}" width="14" height="14" rx="2"/>'); return x, y
def label(x, y, lines, anchor='start', head='i-t'):
    for k, (cls, txt) in enumerate(lines):
        a(f'<text class="{cls}" x="{x}" y="{y + k*16}" text-anchor="{anchor}">{txt}</text>')
def lead(x1, y1, x2, y2):
    a(f'<line class="i-lead" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')

# data centre clusters
sx, sy = site(103.53, 1.70, 11)       # Sedenak
s2x, s2y = site(103.60, 1.655, 7)     # Kulai
ix, iy = site(103.645, 1.448, 10)     # Iskandar Puteri / Nusajaya
kpx, kpy = site(103.715, 1.545, 8)    # Kempas
ux, uy = site(103.82, 1.60, 6)        # Ulu Tiram
# Sedenak West substation marker
swx, swy = P(103.505, 1.735)
a(f'<rect class="i-hot-f" x="{swx-5}" y="{swy-5}" width="10" height="10" transform="rotate(45 {swx} {swy})"/>')
# plants
tbx, tby = plant(103.53, 1.362)      # Tanjung Bin
pgx, pgy = plant(103.905, 1.475)      # Pasir Gudang
# JB city
jx, jy = P(103.76, 1.48); a(f'<circle class="i-line" cx="{jx}" cy="{jy}" r="3" style="fill:var(--ink-2)"/>')

# labels, placed in open land or sea, leaders computed
LX = 22
lead(sx - 11, sy, 226, sy - 66)
label(LX, sy - 92, [('i-t', 'Sedenak and Kulai'), ('i-n', 'YTL, Princeton Digital, Bridge MY06,'), ('i-n', 'K2; Microsoft land at Kulai'), ('i-hot-t', '◆ Sedenak West 500/275/132 kV'), ('i-n', 'substation under way, no date')])
klx2, kly2 = P(103.50, 1.985)
lead(kx + 6, ky - 6, klx2 - 4, kly2 + 30)
label(klx2, kly2, [('i-hot-t', '■ Kulai East: new 500 kV backbone'), ('i-n', 'about 500 km from the east coast,'), ('i-n', 'due by 2030')])
label(yx + 14, yy - 4, [('i-n2', 'Existing 500 kV, Yong Peng East'), ('i-n', 'from 2022')])
# Iskandar Puteri: label in the sea to the south west
ilx, ily = P(103.02, 1.300)
lead(ix - 10, iy + 4, ilx + 230, ily - 14)
label(ilx, ily - 14, [('i-t', 'Iskandar Puteri and Nusajaya'), ('i-n', 'DayOne NTP, AirTrunk JHB1 to JHB4,'), ('i-n', 'Equinix')])
# Tanjung Bin
tlx, tly = P(103.02, 1.215)
lead(tbx - 7, tby + 6, tlx + 205, tly - 12)
label(tlx, tly - 12, [('i-fuel-t', '■ Tanjung Bin coal, 2,100 MW'), ('i-n', 'retires 2031')])
# Kempas and Ulu Tiram: labels to the north east on land
klx, kly = P(103.90, 1.78)
lead(kpx + 8, kpy - 4, klx - 4, kly + 2)
label(klx, kly, [('i-t', 'Kempas'), ('i-n', 'DayOne KTP')])
ulx, uly = P(103.93, 1.66)
lead(ux + 6, uy, ulx - 4, uly - 4)
label(ulx, uly, [('i-t', 'Ulu Tiram'), ('i-n', 'Bridge MY07')])
# Pasir Gudang
plx, ply = P(104.00, 1.535)
lead(pgx + 7, pgy - 4, plx - 4, ply - 4)
label(plx, ply, [('i-fuel-t', '■ Pasir Gudang gas, 1,440 MW')])
# JB
label(jx + 8, jy - 6, [('i-n2', 'Johor Bahru')])
# causeway
cx, cy = P(103.772, 1.452)
# Singapore, inside the island
gx, gy = P(103.80, 1.395)
label(gx, gy, [('i-t', 'Singapore'), ('i-n', 'about 1.6 GW of IT capacity'), ('i-n', 'about 95% of power from gas')], anchor='middle')
# link
lx, ly = P(103.86, 1.432)
# Jurong Island
jlx, jly = P(103.76, 1.226)
lead(P(103.72, 1.262)[0], P(103.72, 1.262)[1], jlx - 4, jly - 4)
label(jlx, jly, [('i-fuel-t', 'Jurong Island: green data centre park,'), ('i-n', 'up to 700 MW; the 2026 call\'s 200 MW')])
# legend and scale bar
lx0, ly0 = W - 236, 26
a(f'<rect x="{lx0-12}" y="{ly0-16}" width="236" height="104" rx="6" style="fill:var(--bg);stroke:var(--rule)"/>')
a(f'<circle class="i-cool-f" cx="{lx0}" cy="{ly0}" r="6" opacity=".85"/><text class="i-n" x="{lx0+14}" y="{ly0+4}">Data centre cluster</text>')
a(f'<rect class="i-fuel" x="{lx0-6}" y="{ly0+16}" width="12" height="12" rx="2"/><text class="i-n" x="{lx0+14}" y="{ly0+26}">Power station</text>')
a(f'<line class="i-hot" x1="{lx0-8}" y1="{ly0+44}" x2="{lx0+8}" y2="{ly0+44}" style="stroke-dasharray:5 3"/><text class="i-n" x="{lx0+14}" y="{ly0+48}">New 500 kV line, by 2030</text>')
km10 = 10 / 111.0 * K
a(f'<line class="i-line" x1="{lx0-6}" y1="{ly0+68}" x2="{lx0-6+km10:.1f}" y2="{ly0+68}"/><text class="i-n" x="{lx0+km10:.1f}" y="{ly0+72}">10 km</text>')

aria = ("Schematic map of southern Johor and Singapore. Data centre clusters sit inland at Sedenak and Kulai "
        "(YTL, Princeton Digital, Bridge, K2, and land bought by Microsoft), where a new 500/275/132 kV substation "
        "is under way at Sedenak West, and near Johor Bahru at Iskandar Puteri and Nusajaya (DayOne, AirTrunk, Equinix), "
        "Kempas (DayOne) and Ulu Tiram (Bridge). A new 500 kV backbone of about 500 km from the east coast ends at Kulai East "
        "by 2030. Tanjung Bin coal station, 2,100 MW, retires in 2031; Pasir Gudang has a 1,440 MW gas plant. "
        "Singapore, across the causeway, has about 1.6 GW of data centre IT capacity and makes about 95% of its power from gas; "
        "its green data centre park on Jurong Island has up to 700 MW, including the 200 MW awarded in 2026.")
svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">' + ''.join(o) + '</svg>'
open(os.path.join(D, 'illos', 'map.svg'), 'w').write(svg)
print('map', W, H)
