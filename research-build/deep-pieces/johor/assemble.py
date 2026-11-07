"""Build src/content/journal/johor-singapore-depth.md (draft) from the source, figures and claims.
At launch the output replaces the-queue-not-the-chip.md (same URL) and the claim's home changes to match."""
import re, os, datetime
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
OUT = os.environ.get('OUT', 'johor-singapore-depth')
src = open(os.path.join(D, 'johor.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'chain': ('illo', 'Five steps from application to a working hall, and a government holds the second', 'One campus in Johor or Singapore, November 2026', 'chain', 'Tenaga (9 August 2023; 28 August 2026); EDB and IMDA (21 August 2026); Dewan Rakyat Hansard (28 October 2026); Tenaga Connection Charge Book 2025 for the premium. My framing of the chain.'),
 'map': ('illo', 'Johor\'s data centres sit in two clusters, and their new power has to travel', 'Southern Johor and Singapore, schematic; positions approximate', 'map', 'Tenaga (28 August 2026) for the 500 kV backbone and the Sedenak West substation; operators\' releases and filings for sites; The Edge (14 August 2026) for Tanjung Bin\'s retirement; EDB and JTC (27 October 2025) for Jurong Island; MDDI (8 September 2026). My drawing.'),
 'sg-chart': ('chart', 'Singapore has handed out 280 MW by call since its pause, against a fleet of more than 1.6 GW', 'Singapore data centres, megawatts', 'sg-chart', 'IMDA and EDB (14 July 2023, 21 August 2026); closing speech, Digital Infrastructure Bill (7 October 2026), for 2024 use and for the 1.6 GW as IT capacity that includes the 200 MW. The 740 MW is my arithmetic: 6.5 TWh over 8,784 hours. Capacity and draw are different measures.'),
 'fill-chart': ('chart', 'Malaysia\'s halls draw more each quarter, and still under a quarter of what is connected', 'Data centre load drawn against maximum demand booked by projects in Tenaga\'s system, Malaysia, gigawatts', 'fill-chart', 'Tenaga analyst briefings, June 2025 to June 2026 (latest 28 August 2026). Malaysia-wide; Johor holds two thirds of secured capacity, and no Johor-only draw is published. December 2025 counts capacity in operation, not in system. September 2025 has no published denominator.'),
 'staircase': ('illo', 'A campus books the whole staircase, declares one step a year, and draws less than either', 'An illustrative 100 MW campus, with Tenaga\'s connected load charge', 'staircase', 'Charge lines from Tenaga\'s Connection Charge Book 2025 (pp. 15 to 17). The campus and its numbers are illustrative, not a real site.'),
 'ratio-chart': ('chart', 'Counted against contracted demand, halls use more than half; against what is connected, under a quarter', 'Data centre load drawn as a share of three different bookings, Malaysia', 'ratio-chart', 'Dewan Rakyat Hansard, 28 October 2026 (58.5%, the minister\'s figure) and 13 October 2026 (1.37 GW of 6 GW, my arithmetic); Tenaga briefing, 28 August 2026 (1,256 MW of 5.65 GW). The dashed line is the 40% threshold of my dated test, which reads Tenaga\'s series.'),
 'sums-chart': ('chart', 'If every approved data centre were built, it would need about as much power as the peninsula\'s record peak', "Malaysia's data centres against Peninsular Malaysia's grid, gigawatts", 'sums-chart', 'Dewan Rakyat Hansard (13 and 28 October 2026; the 117-centre figure is the investment minister\'s oral estimate); energy ministry projection as reported by Bernama (19 October 2026); Tenaga briefing and deck (August and October 2026).'),
 'hk-chart': ('chart', 'In Hong Kong, data centres are a small load on a system with a quarter to spare', 'CLP Power, Hong Kong, megawatts', 'hk-chart', 'CLP Power offering circular (1 April 2026) and Ten-year Summary (2025); CLP quarterly statement (12 October 2026). The data centre figure is my arithmetic: 6.6% of 28,131 GWh over 6,552 hours. The margin is for the whole system.'),
}
def fig(k):
    kind, title, sub, f, cap = FIGS[k]
    t, s_ = ('chart-title', 'chart-sub') if kind == 'chart' else ('illo-title', 'illo-sub')
    return f'<figure class="{kind}">\n<p class="{t}">{title}</p>\n<p class="{s_}">{sub}</p>\n{svg(f)}\n<figcaption>{cap}</figcaption>\n</figure>'
out = re.sub(r'<!--FIG:([a-z-]+)-->', lambda m: fig(m.group(1)), src)
ts = open(os.path.join(ROOT, 'src/data/claims.ts')).read()
blk = ts[ts.index("id: 'johor-singapore-rights'"):]; blk = blk[:blk.index('\n  },')]
get = lambda k: re.search(rf"{k}: '((?:[^'\\]|\\.)*)'", blk).group(1).replace("\\'", "'")
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
# earlier claims, word for word from the two live pieces' records
def record(piece, start):
    t = open(os.path.join(ROOT, 'src/content/journal', piece + '.md')).read()
    r = t[t.index('<details class="claims-record">'):]; r = r[:r.index('</details>')]
    return r[r.index(start):].rstrip()
hk = record('hong-kong-has-the-plug', '**Hong Kong has the plug').replace('\n\nThis piece absorbs no earlier piece, so it carries no older claims.', '')
jo = record('the-queue-not-the-chip', '**Johor and Singapore, the plug').replace('Three earlier claims on this market:\n\n', '')
earlier = 'Earlier claims on this market, word for word:\n\n' + jo + '\n\n' + hk
earlier = earlier.replace('the allowance is grid, not generation, but only 13% of it is labelled demand growth, and most of the rest is closer to renewal, with data centre spending in a contingent allowance released on triggers. That weakens the Malaysian half.', 'only 13% of the regulated base allowance for 2025 to 2027 is labelled demand growth, but in the first half of 2026 demand growth took about 42% of actual network spending, with data centre work funded from a contingent allowance released on signed supply agreements. That supports the Malaysian half more than it did.')
assert 'closer to renewal' not in earlier
out = out.replace('EARLIER_CLAIMS', earlier)
open(os.path.join(ROOT, 'src/content/journal', OUT + '.md'), 'w').write(out)
print('ok', OUT, len(re.sub(r'<[^>]+>', ' ', out).split()))
