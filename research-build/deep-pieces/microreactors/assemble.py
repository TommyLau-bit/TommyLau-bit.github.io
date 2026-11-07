"""Build src/content/journal/microreactors.md from the source, the figures and the claim."""
import re, os
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
src = open(os.path.join(D, 'microreactors.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'size': ('chart', 'One large AI campus needs about fifty of the biggest microreactors', 'Electricity output per unit, megawatts electric (MWe); each square is 20 MWe', 'size-chart', 'Georgia Power (Vogtle), GE Vernova, INL (August 2024), BWXT. 1 GW is the scale large AI campuses now plan; definitions of "microreactor" differ (see the figures behind the charts).'),
 'core': ('illo', 'Inside a microreactor: a reflector and turning drums stand in for size', 'A generic gas-cooled design, simplified and not to scale', 'core', 'My drawing of a generic design. Real designs differ: eVinci moves heat with heat pipes, others with helium gas; Pele, BANR and Kaleidos are gas-cooled.'),
 'triso': ('illo', 'Every speck of uranium carries its own containment', 'A TRISO fuel element from block to particle; layer sizes from US AGR-programme particles', 'triso', 'Sizes from Demkowicz, Liu and Hunn (2019) and INL test reports: kernel about 0.4 mm, buffer 0.1 mm, inner carbon 0.04 mm, silicon carbide 0.035 mm, outer carbon 0.04 mm; compact about 12.3 by 25 mm. Block size is the classic prismatic design. Drawing is mine.'),
 'chain': ('illo', 'From mine to microreactor, three steps in a row have almost nobody on them', 'The HALEU and TRISO fuel chain in America, November 2026', 'chain', 'DOE (7 November 2023), Public Law 118-62, Centrus quarterly report (4 November 2026), GAO-26-107385 (20 August 2026), NRC (Federal Register, 15 April 2026), BWXT (2 November 2026), Standard Nuclear (quarterly report to 30 June 2026). The 0.7 t TRISO figure is my sum of nameplate capacity.'),
 'haleu-chart': ('chart', 'Everything America holds or has contracted covers about half the HALEU needed by 2030', 'Tonnes of HALEU (uranium enriched to just under 20%)', 'haleu-chart', 'DOE to GAO (GAO-26-107385, 20 August 2026); Centrus quarterly report (30 June 2026); DOE Record of Decision (14 January 2025) and HALEU FAQ. Government stock includes HALEU Centrus has made for the DOE.'),
 'price-chart': ('chart', 'A first microreactor costs far more than grid power, and about what remote sites pay for diesel', 'US cents per kilowatt-hour; bars from a range show low to high', 'price-chart', 'INL/RPT-24-80433 (August 2024) for microreactors, a 7 MWe reference plant; EIA 2025 averages (preliminary); INL/EXT-21-63214 (June 2021), citing NEI, for remote diesel. Estimates, not quotes from vendors.'),
}
def fig(k):
    kind, title, sub, f, cap = FIGS[k]
    t, s_ = ('chart-title', 'chart-sub') if kind == 'chart' else ('illo-title', 'illo-sub')
    return f'<figure class="{kind}">\n<p class="{t}">{title}</p>\n<p class="{s_}">{sub}</p>\n{svg(f)}\n<figcaption>{cap}</figcaption>\n</figure>'
out = re.sub(r'<!--FIG:([a-z-]+)-->', lambda m: fig(m.group(1)), src)
ts = open(os.path.join(ROOT, 'src/data/claims.ts')).read()
blk = ts[ts.index("id: 'microreactors'"):]; blk = blk[:blk.index('\n  },')]
get = lambda k: re.search(rf"{k}: '((?:[^'\\]|\\.)*)'", blk).group(1).replace("\\'", "'")
import datetime
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
open(os.path.join(ROOT, 'src/content/journal/microreactors.md'), 'w').write(out)
print('ok', len(out.split()))
