"""Build the solar and batteries piece from solar.src.md, the charts and the claim (sidecar until launch).
Output: src/content/journal/solar-and-batteries.md, draft: true, kept out of git until launch
(.git/info/exclude). At launch: add CLAIM to src/data/claims.ts, set draft: false and the real date."""
import re, os
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
src = open(os.path.join(D, 'solar.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'cf-month': ('chart', 'A solar farm makes about a quarter of what it could, and an eighth in December', 'Capacity factor by month, United States, 2025: output as a share of running flat out', 'cf-month', 'EIA Electric Power Monthly, Table 6.07.B (23 October 2026). Nuclear\'s spring and autumn dips are refuelling outages.'),
 'winter-day': ('chart', 'A four-hour battery reaches the evening; nothing on the site reaches the night', 'A winter weekday at a solar-powered data centre, schematic', 'winter-day', 'The flat load is the California Energy Commission\'s metered winter weekday profile, 83 to 86 per cent of peak (12 August 2026), my reading of its chart. The solar and battery shapes are my drawing, not data: solar is drawn larger than the load, so its midday surplus can charge the battery.'),
 'elcc-bars': ('chart', 'PJM counts a megawatt of solar as 7 per cent of a firm one', 'Share of each megawatt PJM counts as firm capacity, auction for June 2029 to May 2030', 'elcc-bars', 'PJM, ELCC class ratings for the 2029/2030 Base Residual Auction (7 August 2026). Batteries and solar in amber, firm plants in blue.'),
 'elcc-years': ('chart', 'PJM expects each new battery to count for less', 'Share of a megawatt PJM counts as firm, by delivery year', 'elcc-years', 'PJM class ratings for each auction, 2025/26 to 2029/30; preliminary, non-binding ratings from 2030/31 (4 September 2026), which take the four-hour battery to 19 per cent by 2042/43 and hold tracking solar at 7 to 8 per cent.'),
}
CLAIM = {
 'date': '9 November 2026',
 'claim': 'Solar and batteries are the fastest power America builds, but PJM\'s riskiest hours are winter nights, when an AI data centre still draws nearly its full load, and PJM expects each new four-hour battery to count for less: in its class ratings, four-hour storage will be below 50 per cent of a firm megawatt for the 2030/2031 Base Residual Auction and at or below 40 per cent for 2031/2032, lower than in any auction so far, with tracking solar at 10 per cent or less in both.',
 'breaksIf': 'PJM rates four-hour storage at 50 per cent or more in its ELCC class ratings for the 2030/2031 delivery year or above 40 per cent for 2031/2032, or rates tracking solar above 10 per cent in either year.',
}
def fig(k):
    kind, title, sub, f, cap = FIGS[k]
    t, s_ = ('chart-title', 'chart-sub') if kind == 'chart' else ('illo-title', 'illo-sub')
    return f'<figure class="{kind}">\n<p class="{t}">{title}</p>\n<p class="{s_}">{sub}</p>\n{svg(f)}\n<figcaption>{cap}</figcaption>\n</figure>'
out = re.sub(r'<!--FIG:([a-z-]+)-->', lambda m: fig(m.group(1)), src)
out = out.replace('CLAIM_DATE', CLAIM['date']).replace('CLAIM_TEXT', CLAIM['claim']).replace('BREAKS_TEXT', CLAIM['breaksIf'])
assert '<!--FIG' not in out and 'CLAIM_' not in out
open(os.path.join(ROOT, 'src/content/journal/solar-and-batteries.md'), 'w').write(out)
print('ok')
