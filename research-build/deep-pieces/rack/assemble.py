"""Build src/content/journal/powering-the-rack-depth.md from the source, the figures and the claims.
At launch the output replaces powering-the-rack.md (same URL); every old anchor is kept."""
import re, os, sys, datetime
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'powering-the-rack-depth'
src = open(os.path.join(D, 'rack.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'rack-chart': ('chart', 'One AI rack now draws about what sixteen ordinary racks draw, and the roadmap keeps climbing', 'Power per rack, kilowatts, against the line where Nvidia said in 2025 that 54 volt racks start to fail', 'Uptime Institute survey 2025, as reported by The Register; Nvidia DGX GB200 User Guide; Nvidia\'s 2026 white paper for Gen 1 to Gen 3 (ceilings, not measured draws); Kyber as shown at Nvidia\'s March 2025 keynote, as reported; Nvidia Technical Blog (20 May 2025) for the 1 MW target and the 200 kW line.'),
 'chain': ('illo', 'The current climbs at every step down, and the power room changes last', 'One megawatt from the grid to the chip, with the current it needs at each step, simplified', 'Voltages from Nvidia\'s Technical Blog (13 October 2025) and its DGX GB200 User Guide. Currents are my arithmetic at one megawatt, ignoring losses; three-phase AC per phase; the 0.8 V at the chip is my assumption. My drawing.'),
 'copper-chart': ('chart', 'At 800 volts the same copper carries about two and a half times the power', 'Power a conductor carries per square millimetre, by voltage, on Nvidia\'s comparison', 'Nvidia\'s first 800 VDC white paper (October 2025), conductor table on a 48 amp wire basis; the 415 V AC figure is rounded, so the others are shown as Nvidia states them, in per cent.'),
 'options': ('illo', 'Two options keep the old power room; only the third removes it', 'Where the grid\'s alternating current becomes 800 volts DC, in Nvidia\'s three options, simplified', 'Nvidia\'s 2026 white paper for the options, sizes and dates. Nvidia calls them "flexible deployment options", not steps in order. My drawing.'),
 'dates-chart': ('chart', 'Every maker dates the building step to late 2027 or later', 'Dated 800 volt statements: hollow dot when it was said, solid dot the date given', 'Nvidia\'s 2026 white paper and blog (11 August 2026); Vertiv releases (2025), investor deck (20 May 2026) and call (29 July 2026); ABB release (20 October 2026); Eaton call (5 May 2026); the OCP LVDC white paper (30 March 2026) for the US code. A year or half year given is drawn across its span.'),
 'offswitch': ('illo', 'AC puts out its own arc a hundred times a second; DC never does', 'Current over 40 milliseconds, and the time each kind of breaker takes to clear a fault, simplified', 'Nvidia\'s 2026 white paper for the arc and the moulded case breaker\'s 20 ms; Infineon (September 2026) for a few microseconds; Nvidia\'s white paper, citing Siemens, for fuses and mechanical breakers in several milliseconds. My drawing; the placing on the log scale is rough.'),
 'money-chart': ('chart', 'Today the money at the chip is in silicon, not in GaN at 800 volts', 'Revenue in the third quarter of 2026, US dollars, each firm\'s own measure', 'Texas Instruments call and Form 8-K (21 October 2026), my arithmetic from management\'s rounded share; Monolithic Power Systems Form 8-K (29 October 2026); onsemi call (2 November 2026), as summarised; Navitas release (3 November 2026). The measures differ, so the bars show scale only.'),
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
get = entry('powering-the-rack')
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
EARLIER = [
 ('every-megawatt-got-harder', 'Vertiv is paid per megawatt, and AI has made every megawatt harder to build', '25 September 2026',
  'Weaker on two limbs. Services no longer support it: organically, services and spares grew 18.1% in the third quarter of 2026 against 63.6% for products, and fell from 19.0% to 16.7% of sales. The margin has not shrunk, 25.2% and up 2.9 points, but Vertiv\'s finance chief credits volume, operating leverage and productivity, not richer content. Its 800 volt line moved from the second half of 2026 to early 2027, and it no longer reports orders. The claim now rests on Vertiv\'s own per-megawatt estimate, up about 10 to 15%, part of it acquired scope, against Schneider Electric\'s view that the most complex AI sites will not reach the top of its range. The in-house limb was partly met from the start: Google has liquid-cooled its own chips since 2018.'),
 ('ti-feeds-the-chip', 'The most expensive chip in an AI rack runs on Texas Instruments\' cheapest ones', '2 October 2026',
  'The growing data centre business is here, about 13% of revenue in the third quarter of 2026, up about 95%. But it grew before 800 volt racks ship in volume, "800 volt" does not appear in TI\'s October call, and TI names density and voltage together, so the cause the claim names is not yet shown. Nvidia\'s 2026 roadmap keeps 54 volts inside the rack to 570 kW, so the first limb cannot be tested before 2027. Industrial grew more than 40% and the new Sherman fab is producing, so the part-empty limb is not near.'),
]
parts = ['Two earlier claims on the rack\'s power, word for word:']
for cid, title, date, note in EARLIER:
    g = entry(cid)
    parts.append(f'**{title}** ({date})\n\nClaim: "{g("claim")}"\n\nBreaks if: "{g("breaksIf")}"\n\nWhere later evidence bears on it: {note}')
out = out.replace('EARLIER_CLAIMS', '\n\n'.join(parts))
open(os.path.join(ROOT, 'src/content/journal', OUT + '.md'), 'w').write(out)
print('ok', OUT, len(re.sub(r'<[^>]+>', ' ', out).split()))
