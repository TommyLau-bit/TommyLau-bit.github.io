"""Build src/content/journal/nuclear-for-ai-depth.md from the source, the figures and the claims.
At launch the output replaces nuclear-for-ai.md (same URL) and the claim's home changes to match."""
import re, os, sys, datetime
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'nuclear-for-ai-depth'
src = open(os.path.join(D, 'nuclear.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'cf-chart': ('chart', 'A nuclear plant produces about nine tenths of what it could; wind and solar a third or less', 'Capacity factor, United States, 2025: output as a share of running flat out all year', 'cf-chart', 'EIA Electric Power Monthly, Tables 6.07.A and 6.07.B (23 October 2026). Gas and coal plants are often turned down by choice; wind and solar run when the weather allows.'),
 'clocks': ('illo', 'A restart or uprate starts with most of the clocks already run; a HALEU reactor starts with none', 'The four things every nuclear project needs, by kind of project', 'clocks', 'My framing. "Part done" means the thing exists but needs repair, rehiring or a licence change; the fuel for ordinary reactors still has its own Russian deadline, set out later in the piece.'),
 'crane-chart': ('chart', 'Crane\'s reactor is due in 2027; full delivery through a fresh grid request might not have been', 'Crane restart, from its announcement in September 2024', 'crane-chart', 'Constellation (20 September 2024, 6 August 2026); FERC order 195 FERC ¶ 61,162 (1 June 2026), which records Constellation\'s reading of PJM\'s first study and says the transfer could "potentially" bring full delivery sooner.'),
 'restarts': ('chart', 'Palisades won its approvals first and still has no date; Crane, a year behind, is due first', 'The three American restarts: closure, NRC filings and dates given, to 7 November 2026', 'restarts', 'NRC plant pages and orders; Constellation (6 August 2026); NextEra; FERC orders ER25-1083 and ER25-2989; Holtec\'s withdrawn registration statement (8 September 2026). Palisades\' contracts may be ended if it is not in service by March 2027.'),
 'uprate': ('illo', 'The bigger the uprate, the further down the line the plant has to change', 'Where each of the NRC\'s three kinds of uprate touches a plant; simplified, not to scale', 'uprate', 'NRC, Types of Power Uprates (reviewed 15 September 2026). My drawing of a generic pressurised water reactor; boiling water reactors make steam in the reactor itself, but the uprate types are the same.'),
 'cost-chart': ('chart', 'A restart or uprate costs a fraction of a new large reactor for each kilowatt', 'Capital cost, US dollars per kilowatt of capacity; my arithmetic from company and press figures', 'cost-chart', 'Constellation (FERC filing; 6 October 2026); Holtec\'s withdrawn registration statement (8 September 2026); Department of Energy (8 September 2026); Vogtle\'s total as reported by AP. Palisades and Duane Arnold are funding raised or loan ceilings, not reported costs.'),
 'meter': ('illo', 'On the PJM and MISO grids, every binding nuclear deal for AI runs through the grid', 'Behind the meter against in front of the meter', 'meter', 'FERC (1 November 2024, ER24-2172; 18 December 2025, EL25-49); Talen quarterly report for June 2026. My drawing.'),
 'deals-chart': ('chart', 'The firm contracts are on reactors that exist; the new ones have frameworks and targets', 'Megawatts in nuclear deals for AI in America, to 7 November 2026', 'deals-chart', 'Company releases and filings, listed in the figures behind the charts. Bars show megawatts as each company states them; the binding total is my sum. Google\'s 2,700 MW supply deal on existing Constellation plants is excluded.'),
 'advanced': ('illo', 'The advanced reactors have permits, ground and buyers; the fuel column is the one still open', 'Four HALEU reactors linked to AI buyers, against five gates, at 7 November 2026', 'advanced', 'NRC; TerraPower (4 March 2026); Oklo quarterly report (6 November 2026); Kairos, TVA and Google (18 August 2025); X-energy (30 October 2026); ASP Isotopes (15 October 2026). Every design here burns HALEU.'),
 'swu-chart': ('chart', 'Russia sold a quarter of America\'s enrichment in 2025; most replacements arrive in the 2030s', 'Separative work units (SWU), millions a year', 'swu-chart', 'EIA 2025 Uranium Marketing Annual Report, Table 16; Urenco (29 June, 8 October 2026); Federal Register (12 August 2026) and Orano for Oak Ridge. Centrus starts new capacity at Piketon in 2029 and publishes no SWU figure, so it is not shown.'),
 'ladder': ('chart', 'Restarts on ordinary fuel arrive first; uprates follow in steps to 2034; HALEU reactors offer little by 2030', 'Capacity in megawatts, with the date each owner gives; American projects only', 'ladder', 'Owner and developer releases and filings to 6 November 2026. Uprate megawatts are my sum of five AI-funded deals. Darlington, 300 MW on ordinary fuel in Canada, is left out because the claim tests American grids.'),
}
def fig(k):
    kind, title, sub, f, cap = FIGS[k]
    t, s_ = ('chart-title', 'chart-sub') if kind == 'chart' else ('illo-title', 'illo-sub')
    return f'<figure class="{kind}">\n<p class="{t}">{title}</p>\n<p class="{s_}">{sub}</p>\n{svg(f)}\n<figcaption>{cap}</figcaption>\n</figure>'
out = re.sub(r'<!--FIG:([a-z-]+)-->', lambda m: fig(m.group(1)), src)
ts = open(os.path.join(ROOT, 'src/data/claims.ts')).read()
def entry(cid):
    blk = ts[ts.index(f"id: '{cid}'"):]; blk = blk[:blk.index('\n  },')]
    return lambda k: re.search(rf"{k}: '((?:[^'\\]|\\.)*)'", blk).group(1).replace("\\'", "'")
get = entry('nuclear-order-of-holdings')
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
EARLIER = [
 ('nuclear-for-ai', 'Nuclear for AI: restarts first, new reactors later', '30 October 2026',
  'This piece\'s claim replaces it, and keeps its 100 MW test on HALEU reactors by the end of 2030 unchanged. Its cause clause, that commercial enrichment at the level these reactors need "has stopped in America", no longer holds as written: Centrus said on 4 November 2026 that its cascade now enriches HALEU for commercial buyers, with no start date or volume given. The plants contracted to replace it have not started; ASP Isotopes had not enriched uranium-235 by 15 October 2026.'),
 ('constellation-restarts-the-reactor', 'Constellation can bring a closed reactor back by 2027. The grid connection was the hard part.', '30 October 2026',
  'The test is open, and Crane still targets the second half of 2027. Palisades cuts against the premise that the grid connection sets the pace: it held its place and is the slowest of the three, held back by reactor work. The end-2030 date for a fresh connection is Constellation\'s reading of PJM\'s first study, which FERC recorded; FERC said the Eddystone transfer could "potentially" bring full delivery sooner and that PJM\'s studies decide. The test\'s "full output" is not the same as PJM\'s "full deliverability".'),
 ('oklo-sells-the-electricity', 'Oklo will not sell you a reactor. It wants to sell you nuclear electricity for decades.', '29 September 2026',
  'The first half holds: Oklo still sells power, not reactors. Its first powerhouse target is now 2028 to 2029 (quarterly report, 6 November 2026). On fuel, a letter has become a contract: a conditional HALEU supply agreement with Centrus on 30 September 2026, and Meta\'s first funding paid to Centrus on 2 November. On power, no customer megawatt is under a binding power purchase agreement, and Oklo calls Meta\'s arrangement a prepayment framework, so the limb "the letters of intent stay letters" still points towards a break.'),
]
parts = ['Earlier claims on these reactors, word for word:']
for cid, title, date, note in EARLIER:
    g = entry(cid)
    parts.append(f'**{title}** ({date})\n\nClaim: "{g("claim")}"\n\nBreaks if: "{g("breaksIf")}"\n\nWhere later evidence bears on it: {note}')
out = out.replace('EARLIER_CLAIMS', '\n\n'.join(parts))
open(os.path.join(ROOT, 'src/content/journal', OUT + '.md'), 'w').write(out)
print('ok', OUT, len(re.sub(r'<[^>]+>', ' ', out).split()))
