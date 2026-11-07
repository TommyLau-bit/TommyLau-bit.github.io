"""Build src/content/journal/data-centres-in-space-depth.md from the source, the figures and the claims.
At launch the output replaces data-centres-in-space.md (same URL); the anchors data-centres-in-space and heat-pump-trade are kept."""
import re, os, sys, datetime
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'data-centres-in-space-depth'
src = open(os.path.join(D, 'space.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'craft': ('illo', 'The array is five times the radiator, and both are launched', 'SpaceX\'s AI1 computing satellite, as published, drawn to scale', 'SpaceX Starmind page, read 7 November 2026, for the wingspan, array, radiator and power; SpaceX letter to the FCC, 29 May 2026, for the mass, which may belong to an earlier, smaller design. The wing and radiator shapes are my assumptions; their areas are SpaceX\'s. My drawing.'),
 'flux-chart': ('chart', 'A radiator sheds more heat the hotter it runs, by the fourth power', 'Heat radiated to deep space by a two-sided panel, watts per square metre, by temperature', 'Stefan-Boltzmann law at emissivity 0.92, both faces, ignoring sunlight and the Earth\'s glow, my arithmetic. Coolant band: Nvidia, 16 March and 21 June 2026. Points: Starcloud white paper (September 2024); SpaceX Starmind page; interview SpaceX filed with the SEC, 9 June 2026.'),
 'radiator-chart': ('chart', 'Flown radiators are heavy; light ones have been tested only on the ground', 'Space radiator mass, kilograms per square metre of panel', 'NASA space station cooling overview, unit masses and areas, my arithmetic; NASA Glenn, 23 January 2025; Juhasz, NASA/TM-2008-215420.'),
 'budget-chart': ('chart', 'Each part alone uses most of SpaceX\'s 10 kilogram budget', 'Kilograms launched per kilowatt, by part, at today\'s published weights', 'My arithmetic from Redwire\'s product table, the radiator figures above at 1,400 W/m², a press figure for a GB200 rack (The Register, 21 March 2024) and NASA\'s battery cell range. SpaceX prospectus, 12 June 2026, for the target.'),
 'kwpt-chart': ('chart', 'No published figure reaches SpaceX\'s target of 100 kW per tonne', 'Kilowatts of computing per tonne launched', 'SpaceX prospectus, Starmind page, FCC letter and filed interview; Google\'s Suncatcher paper, Table 1; Nvidia blog for Starcloud-1\'s 60 kg. Ratios are my arithmetic; Starcloud-1 assumes its chip at full power.'),
 'price-chart': ('chart', 'At today\'s fare orbit costs several times the ground; at $200 it falls inside its range', 'Launched power price, dollars per kilowatt per year over a five-year life, launch only', 'Google\'s Suncatcher paper. Launch cost only: chips, arrays and the satellite itself are left out on both sides.'),
}
def fig(k):
    kind, title, sub, cap = FIGS[k]
    t, s_ = ('chart-title', 'chart-sub') if kind == 'chart' else ('illo-title', 'illo-sub')
    return f'<figure class="{kind}">\n<p class="{t}">{title}</p>\n<p class="{s_}">{sub}</p>\n{svg(k)}\n<figcaption>{cap}</figcaption>\n</figure>'
out = re.sub(r'<!--FIG:([a-z-]+)-->', lambda m: fig(m.group(1)), src)
assert '<!--FIG' not in out
ts = open(os.path.join(ROOT, 'src/data/claims.ts')).read()
def entry(cid):
    blk = ts[ts.index(f"id: '{cid}'"):]; blk = blk[:blk.index('\n  },')]
    return lambda k: re.search(rf"{k}: '((?:[^'\\]|\\.)*)'", blk).group(1).replace("\\'", "'")
get = entry('data-centres-in-space')
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
assert 'CLAIM_' not in out and 'BREAKS_TEXT' not in out
open(os.path.join(ROOT, 'src/content/journal', OUT + '.md'), 'w').write(out)
print('ok', OUT, len(re.sub(r'<[^>]+>', ' ', out).split()))
