"""Build src/content/journal/the-equipment-queue-depth.md from the source, the figures and the claims.
At launch the output replaces the-equipment-queue.md (same URL); its claims already have that home."""
import re, os, sys, datetime
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'the-equipment-queue-depth'
src = open(os.path.join(D, 'equipment.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'chain': ('illo', 'Between the grid and the chip sit five or six machines, each from its own factory, each with its own queue', 'The electrical chain into an AI campus, simplified, not to scale', 'Voltages are typical American ones. The Nvidia technical blog (20 May 2025) for 13.8 kilovolts at the hall; makers\' own statements for the waits; the US Department of Energy (July 2024) for the transformer. My drawing.'),
 'transformer': ('illo', 'A transformer is steel, copper and oil with no moving parts, and every part has its own supplier', 'A large power transformer cut open, simplified, not to scale', 'US Department of Energy (June 2012 and July 2024) for the parts, cost shares and weights; Hitachi Energy\'s component delivery page (29 October 2026) for the bushings and tap changers. My drawing.'),
 'years-chart': ('chart', 'The wait is getting longer, and the new factories are still to come', 'Signed orders not yet delivered, in years of each business\'s sales', 'Years of work is backlog divided by the same business\'s sales over the previous four quarters, my arithmetic from each company\'s filings to 30 September 2026; Siemens Energy\'s latest is 30 June 2026. Siemens Energy\'s figure includes long HVDC links, so compare the direction, not the levels. Plant dates are each maker\'s own: Eaton\'s Jonesville and Bellevue plants in 2027, Siemens Energy\'s Nuremberg expansion by 2028, Hitachi Energy\'s Gallman plant in 2029.'),
 'factories-chart': ('chart', 'Most of the new floor space lands from 2027 on', 'Dated plants for transformers, switchgear, bushings and core steel, from announcement to the production date given', 'Hollow dot: announced or ground broken. Solid dot: the production date each maker gives; a thick line is a year given without a month. Charlotte was announced for early 2026; its 2027 date is a board member\'s, relayed by Reuters (26 June 2025). Hitachi Energy\'s South Boston plant and Siemens Energy\'s Greater Richland plant have no published dates and are left off.'),
 'siemens-chart': ('chart', 'Siemens Energy\'s own forecast: the shortage narrows, but never closes', 'Demand for large and medium power transformers above the capacity of all makers, Europe and North America', 'Siemens Energy, capital market day, 20 November 2025. Only the two percentages are its labels; demand and capacity are in GVA, a thousand MVA. By my reading of its bars, capacity nearly doubles from fiscal 2023 to fiscal 2030.'),
 'imports-chart': ('chart', 'America\'s imports of large transformers more than tripled in three years, and China supplies little', 'US imports of liquid-filled transformers above 10 MVA, by value', 'UN Comtrade, US imports of HS 850423, which carries the US customs figures, read 7 November 2026. Shares are of the 2025 total; my arithmetic.'),
 'tariff-chart': ('chart', 'Until 2028 the finished transformer is taxed less than the steel it is made from', 'US Section 232 tariff on the full value of the goods, since 6 April 2026', 'Proclamation 11021 and its annexes, as reissued by Proclamation 11032 (1 June 2026). For large transformers the 15% includes the normal customs duty. Large transformers are HS 8504.23; distribution transformers 8504.21 and 8504.22.'),
 'prices-chart': ('chart', 'Prices jumped in 2022, slowed, and are rising faster again', 'US producer price indexes, transformer and switchgear makers, 2020 average = 100', 'Bureau of Labor Statistics series PCU335311335311 and PCU335313335313, read 7 November 2026; September 2026 is preliminary. Indexing is my arithmetic.'),
 'waits-chart': ('chart', 'Inside the fence, this year\'s orders ship in one to three years', 'When orders signed now are due, in each maker\'s own words, from today', 'Eaton Form 10-Q (30 September 2026); Schneider Electric (16 October 2026); Generac (28 October 2026); ABB and Caterpillar calls (20 and 29 October 2026, third-party summaries); US Department of Energy (July 2024). A thick line is a range or a year given without a month.'),
 'rack-chart': ('chart', 'An AI rack draws fifteen times the power of an average one, and Nvidia plans over a hundred times', 'Power drawn by one rack, kilowatts', 'Uptime Institute global data centre survey, 2025; Schneider Electric and Nvidia reference design (December 2024); Nvidia technical blog (20 May 2025).'),
 'parts-chart': ('chart', 'A high-voltage bushing from Sweden now waits longer than a whole transformer did in 2010', 'Delivery times quoted for transformer parts, weeks', 'Hitachi Energy, delivery times for transformer components, Ludvika updated 29 October 2026 and Hefei 4 August 2026. The 2012 figure is the US Department of Energy\'s. Lower-voltage bushings and tap changers show the strain is not everywhere.'),
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
get = entry('the-equipment-queue')
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
EARLIER = [
 ('schneider-sells-the-finished-system', 'Schneider Electric sells AI data centres the finished system, not the parts', '7 October 2026',
  'Not broken, but close. In the third quarter of 2026 Products grew 17% against 22% for Systems, and Schneider says Products growth was "majority volume-driven": more loose parts, not just higher prices. The nine-month Systems share is about 34% from rounded shares (33.9% to 34.9%), on the line. The share test checks the outcome, not the cause: buyers may want prefabrication for speed as much as for scarce electricians.'),
 ('hitachi-energy-plans-the-queue', 'Hitachi Energy is spending more than $9 billion on factories, and still plans a three-year queue', '22 October 2026',
  'Holding. The ratio rose to about 3.1 at 30 September 2026 (Hitachi, 28 October 2026). Hitachi Energy\'s US programme is now around $1.5bn; its own releases give no date for the South Boston plant.'),
 ('eaton-order-book-outruns-it', 'Eaton is shipping more electrical gear than ever, and its order book is growing faster still', '26 October 2026',
  'Holding, but flat. At 30 September 2026 the ratio was 1.050, against 1.049 in June (Form 10-Q, 3 November 2026). It has stopped rising but has not fallen; some of the earlier rise may be price. Twelve-month organic orders were up 39%. The margin, 29.8% in the third quarter, was still below the 30.3% of a year earlier.'),
 ('siemens-energy-measures-the-shortage', 'Siemens Energy has measured the transformer shortage, and its own chart runs to 2030', '28 October 2026',
  'No new annual figures by 7 November 2026; fiscal 2026 results are due in November. Grid Technologies\' book-to-bill was 1.48 in the quarter to June 2026 and 1.88 over nine months, and its backlog rose to €51bn. Siemens Energy announced its Charlotte plant for early 2026; a Reuters report of 26 June 2025 relayed a board member giving early 2027, and its release of 3 February 2026 gives no date.'),
]
parts = ['Four earlier claims on this queue, word for word:']
for cid, title, date, note in EARLIER:
    g = entry(cid)
    parts.append(f'**{title}** ({date})\n\nClaim: "{g("claim")}"\n\nBreaks if: "{g("breaksIf")}"\n\nWhere later evidence bears on it: {note}')
out = out.replace('EARLIER_CLAIMS', '\n\n'.join(parts))
open(os.path.join(ROOT, 'src/content/journal', OUT + '.md'), 'w').write(out)
print('ok', OUT, len(re.sub(r'<[^>]+>', ' ', out).split()))
