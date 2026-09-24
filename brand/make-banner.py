#!/usr/bin/env python3
"""Brand banner: pylons receding to a data centre on the horizon, with the slogan.
Writes the LinkedIn company cover (brand/linkedin-banner.png, 4200x700) and the
site's default share image (public/og.png, 1200x630) from the same scene.
Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-banner.py"""
import cairosvg

SLOGAN = 'The AI buildout has a physical layer.'
TAGLINE = 'AI AND ENERGY INFRASTRUCTURE, EXPLAINED PLAINLY'
A, BLUE = '#f59e0b', '#60a5fa'
FONT = 'font-family="Helvetica Neue,Helvetica,Arial,sans-serif"'


def pylon(x, base, h, op):
    sw = max(0.9, h / 48)
    top, waist = base - h, base - 0.55 * h
    wb, ww = 0.34 * h, 0.10 * h
    arm1, arm2 = base - 0.66 * h, base - 0.84 * h
    path = lambda pts: 'M' + ' L'.join(f'{a:.1f} {b:.1f}' for a, b in pts)
    left = [(x - wb / 2, base), (x - ww / 2, waist), (x - ww * 0.6, top + 0.08 * h), (x, top)]
    right = [(x + wb / 2, base), (x + ww / 2, waist), (x + ww * 0.6, top + 0.08 * h), (x, top)]
    s = f'<g stroke="{A}" stroke-width="{sw:.2f}" fill="none" stroke-linejoin="round" opacity="{op:.2f}">'
    s += f'<path d="{path(left)}"/><path d="{path(right)}"/>'
    for i in range(3):
        t0, t1 = i / 3, (i + 1) / 3
        ya, yb = base - (base - waist) * t0, base - (base - waist) * t1
        wa, wz = wb / 2 - (wb / 2 - ww / 2) * t0, wb / 2 - (wb / 2 - ww / 2) * t1
        s += f'<path d="M{x-wa:.1f} {ya:.1f} L{x+wz:.1f} {yb:.1f} M{x+wa:.1f} {ya:.1f} L{x-wz:.1f} {yb:.1f}"/>'
    s += f'<path d="M{x-0.30*h:.1f} {arm1:.1f} H{x+0.30*h:.1f} M{x-0.22*h:.1f} {arm2:.1f} H{x+0.22*h:.1f}"/></g>'
    tips = [(x - 0.30 * h, arm1), (x + 0.30 * h, arm1), (x - 0.22 * h, arm2), (x + 0.22 * h, arm2)]
    return s, tips


def scene(w, h, hz, k, xs, hs, dc_x, text):
    """w x h canvas, horizon at hz, k scales the data centre, xs/hs place the pylons."""
    horizon = hz / h
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">'
    s += ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
          f'<stop offset="0" stop-color="#0c0b0a"/><stop offset="{horizon*0.79:.3f}" stop-color="#17120c"/>'
          f'<stop offset="{horizon:.3f}" stop-color="#3a240a"/><stop offset="{horizon+0.001:.3f}" stop-color="#0b0a09"/>'
          '<stop offset="1" stop-color="#070706"/></linearGradient>'
          f'<radialGradient id="glow" cx="{(dc_x+30*k)/w:.3f}" cy="{horizon:.3f}" r="0.55">'
          '<stop offset="0" stop-color="#f59e0b" stop-opacity=".30"/><stop offset=".5" stop-color="#b45309" stop-opacity=".08"/>'
          '<stop offset="1" stop-color="#b45309" stop-opacity="0"/></radialGradient></defs>')
    s += f'<rect width="{w}" height="{h}" fill="url(#sky)"/><rect width="{w}" height="{h}" fill="url(#glow)"/>'
    s += (f'<rect x="{dc_x}" y="{hz-15*k}" width="{66*k}" height="{15*k}" fill="#1a1612" stroke="#2c251c" stroke-width="{k}"/>'
          f'<rect x="{dc_x+16*k}" y="{hz-22*k}" width="{30*k}" height="{7*k}" fill="#1a1612" stroke="#2c251c" stroke-width="{k}"/>')
    s += f'<g fill="{BLUE}">' + ''.join(
        f'<rect x="{dc_x+(5+i*8)*k:.1f}" y="{hz-9*k:.1f}" width="{4*k}" height="{2.5*k}"/>' for i in range(8)) + '</g>'
    ops = [0.9, 0.8, 0.68, 0.56, 0.46]
    towers = [pylon(x, hz, ht, o) for x, ht, o in zip(xs, hs, ops)]
    for i in range(len(towers) - 1):
        for j in range(4):
            (ax, ay), (bx, by) = towers[i][1][j], towers[i + 1][1][j]
            sag = 10 * k + hs[i] * 0.12
            s += (f'<path d="M{ax:.1f} {ay:.1f} Q {(ax+bx)/2:.1f} {max(ay,by)+sag:.1f} {bx:.1f} {by:.1f}" '
                  f'stroke="{A}" stroke-width="{k}" fill="none" opacity="{0.45*ops[i]:.2f}"/>')
    ex, ey = dc_x + 16 * k, hz - 21 * k
    for j in range(4):
        bx, by = towers[-1][1][j]
        s += (f'<path d="M{bx:.1f} {by:.1f} Q {(bx+ex)/2:.1f} {by+5*k:.1f} {ex:.1f} {ey:.1f}" '
              f'stroke="{A}" stroke-width="{0.8*k}" fill="none" opacity=".25"/>')
    s += ''.join(t[0] for t in towers)
    s += f'<path d="M0 {hz} H{w}" stroke="{A}" stroke-opacity=".25" stroke-width="{k}"/>'
    return s + text + '</svg>'


def words(x, y, size, sub_size, gap):
    return (f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="700" fill="#f0efea" letter-spacing="-0.3">{SLOGAN}</text>'
            f'<text x="{x+1}" y="{y+gap}" {FONT} font-size="{sub_size}" fill="#a39a8c" letter-spacing="{sub_size*0.2:.1f}">{TAGLINE}</text>')


# LinkedIn company cover: 6:1, drawn at 1128 x 188 and exported at 4200 x 700
li = scene(1128, 188, 148, 1, [640, 790, 895, 968, 1018], [100, 72, 52, 37, 27], 1046, words(40, 70, 28, 12, 26))
cairosvg.svg2png(bytestring=li.encode(), write_to='brand/linkedin-banner.png', output_width=4200, output_height=700)
open('brand/linkedin-banner.svg', 'w').write(li)

# Site default share image: 1200 x 630, slogan stacked on two lines
og_words = (f'<text x="72" y="150" {FONT} font-size="64" font-weight="700" fill="#f0efea" letter-spacing="-0.5">The AI buildout has</text>'
            f'<text x="72" y="226" {FONT} font-size="64" font-weight="700" fill="#f0efea" letter-spacing="-0.5">a physical layer.</text>'
            f'<text x="74" y="276" {FONT} font-size="20" fill="#a39a8c" letter-spacing="4">{TAGLINE}</text>'
            f'<text x="74" y="580" {FONT} font-size="24" font-weight="700" fill="{A}" letter-spacing="1">thephysicallayer.fyi</text>')
og = scene(1200, 630, 500, 1.6, [640, 820, 940, 1015, 1060], [210, 150, 108, 78, 56], 1082, og_words)
cairosvg.svg2png(bytestring=og.encode(), write_to='public/og.png', output_width=1200, output_height=630)
print('brand/linkedin-banner.png, public/og.png')
