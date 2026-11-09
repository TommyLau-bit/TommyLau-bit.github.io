"""Build src/content/journal/heat-and-water-depth.md from the source, the figures and the claims.
At launch the output replaces heat-and-water.md (same URL); every old anchor is kept, and the claim's home is unchanged."""
import re, os, sys, datetime
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'heat-and-water-depth'
src = open(os.path.join(D, 'heat.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'heat-chart': ('chart', 'One AI rack would need the air of eight of the best floor tiles', 'Heat per rack, kilowatts, with the air needed to cool it in best-in-class floor tiles of 1,900 cubic feet a minute', 'Uptime Institute survey 2025, as reported by The Register; ASHRAE white paper (2021) for the dense air rack and the tile; Nvidia DGX GB200 User Guide; Vertiv\'s GB300 NVL72 datasheet, a design envelope, not an Nvidia figure. Tiles are my arithmetic at about 120 cubic feet a minute per kW.'),
 'chain': ('illo', 'Only the last step can spend water', 'One watt of heat, from an AI chip to the outside air, simplified', 'Nvidia (16 March and 21 June 2026) for the temperatures and the coolant; Google (30 April 2025) on its own CDU. My drawing.'),
 'roof': ('illo', 'The tower saves power with water; the dry cooler saves water with power', 'Three machines that reject a data centre\'s heat, simplified', 'US Department of Energy cooling tower guidance; Lawrence Berkeley National Laboratory (December 2024) for the tower\'s water; Vertiv Liebert AFC datasheet for the chiller at 35°C. The tower\'s 1 to 2 litres spans Nvidia\'s figure and the laboratory\'s median. My drawing.'),
 'ladder': ('illo', 'At 41 degrees, a dry cooler needs no help for most hours of the year in many climates', 'Coolant temperatures, and the outside air at which a dry cooler alone does the job', 'Nvidia (16 March and 21 June 2026) for the coolant temperatures. The 18°C chilled water and the 5 to 8 degree gap across the dry cooler are typical practice, my assumptions. My drawing.'),
 'lbnl-chart': ('chart', 'In a liquid hall, going dry costs almost nothing in yearly power', 'Simulated yearly medians: PUE, and water evaporated on site per kWh of computing', 'Lawrence Berkeley National Laboratory, December 2024, Figure 4.4: medians as I read them from its chart, rounded. Yearly averages from typical weather; the laboratory publishes no worst-hour figure.'),
 'whole-chart': ('chart', 'Counted whole, a dry liquid hall uses about half the water of an air hall with a tower', 'Water consumed per kWh of computing, litres: at the power station for the electricity bought, plus on the roof', 'My arithmetic from Lawrence Berkeley National Laboratory, December 2024: roof water and PUE from its Figure 4.4 medians; power station water is PUE times its national average of 4.52 litres per kWh bought, which includes hydroelectric reservoirs and ignores power contracts.'),
 'sites-chart': ('chart', 'Where Google judged the water scarce, it used almost none', 'Water consumed in 2025 at four Google campuses, millions of gallons', 'Google 2026 Environmental Report, per-site table; risk judgements from its 2025 report, pages 40 to 41. Waltham Cross and Canelones have no row of their own yet.'),
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
get = entry('heat-and-water')
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
assert 'CLAIM_' not in out and 'BREAKS_TEXT' not in out
open(os.path.join(ROOT, 'src/content/journal', OUT + '.md'), 'w').write(out)
print('ok', OUT, len(re.sub(r'<[^>]+>', ' ', out).split()))
