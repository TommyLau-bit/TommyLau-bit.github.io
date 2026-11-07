"""Build src/content/journal/america-rations-the-plug-depth.md from the source, the figures and the claims.
At launch the output replaces america-rations-the-plug.md (same URL). The three claims homed at
contracted-energised-running move their home here, and that piece's URL redirects to its anchors here."""
import re, os, sys, datetime
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'america-rations-the-plug-depth'
src = open(os.path.join(D, 'plug.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'path': ('illo', 'Four of the five steps are paperwork; the third is steel and copper', 'From application to running, for a large data centre in an American grid, simplified', 'FERC\'s PJM show cause order (18 June 2026) for the study target and who handles load requests; the equipment queue for the build. My drawing.'),
 'texas-chart': ('chart', 'Texas has been asked for 474 gigawatts, and has cleared 6.6', 'Large loads asking to connect to ERCOT, at each gate, gigawatts', 'Office of the Texas Governor (3 August 2026); ERCOT\'s Senate briefing (29 July 2026, preliminary) and its presentation to the Texas regulator (20 August 2026); Oncor Form 8-K exhibit (5 November 2026). ERCOT\'s figures are from different dates in the same summer.'),
 'duke-chart': ('chart', 'If new load accepts a few cuts a year, existing grids can take far more of it', 'New load America\'s 22 largest grids could add without new capacity, gigawatts, by the share of its yearly energy it gives up', 'Duke University Nicholas Institute, Rethinking Load Growth (11 February 2025), as summarised by the institute and the trade press; I could not open the report itself. Hours are the model\'s, not a contract\'s.'),
 'ratings-chart': ('chart', 'PJM counts a megawatt that can be cut for more than a megawatt of battery', 'Share of each megawatt PJM counts towards its capacity needs', 'PJM preliminary effective load carrying capability ratings, delivery years 2028/29 to 2042/43. The 2030/31 ratings are not yet binding.'),
 'ridethrough': ('illo', 'Each site counts the dips and leaves on the third; PJM\'s rule says stay', 'A fault the grid clears normally, as one data centre sees it, and PJM\'s proposed ride-through rule, simplified, not to scale in time', 'NERC incident review (January 2025) for the counting rule and the 2024 event; PJM\'s Members Committee deck (28 October 2026) for the rule. My drawing.'),
 'events-chart': ('chart', 'July\'s drop was the largest in PJM\'s history, and the third in two years', 'Data centre load that moved to backup after a fault the grid cleared normally, megawatts', 'NERC incident review (January 2025); PJM\'s Planning Committee deck (6 October 2026), which gives the February 2025 event as about 1,800 MW and July 2026 as about 3,900 MW; earlier PJM material gave about 1,500 and 3,800. PJM release on the 2028/29 auction (14 July 2026).'),
 'auction-chart': ('chart', 'PJM\'s auction has sat at its cap three times running, and the cap rises in December', 'Price paid to power stations to stand ready, dollars per megawatt of capacity per day, by delivery year', 'PJM auction reports and releases to 14 July 2026, and its 2029/30 planning parameters (31 August 2026). The uncapped 2028/29 price is as reported by the American Public Power Association from PJM\'s figures. The cap differs slightly each year.'),
 'bill-chart': ('chart', 'Capacity tripled, but energy is still most of the cost', 'PJM total wholesale cost of power, dollars per megawatt-hour, first half of each year', 'PJM market monitor, report to the Members Committee (27 July 2026). The split into parts is my arithmetic from its shares and growth rates; the small remainder is other charges.'),
 'dominion-chart': ('chart', 'Dominion has about 54 gigawatts of data centres under contract, and bills 4.8', 'Dominion Energy\'s data centre contracts in Virginia by stage, July 2026, and its data centre billing peak, August 2026, gigawatts', 'Dominion Energy to PJM\'s Load Analysis Subcommittee (29 September 2026). Dominion counts engineering letters as non-firm.'),
 'operators-chart': ('chart', 'At the operators too, signed power runs far ahead of power at work', 'Contracted, connected and active power, gigawatts', 'CoreWeave earnings release (11 August 2026); Nebius shareholder letters (12 February and 12 August 2026). Nebius has never reported connected and active power for the same date; its third-quarter letter is due on 12 November 2026.'),
 'abilene-chart': ('chart', 'Abilene arrived building by building, and the chips arrived with the power', 'Construction start to running, and handover of capacity to Oracle\'s customer', 'Crusoe releases (21 May 2025, 30 September 2025, 27 March 2026); Oracle\'s results calls of 10 June and 10 September 2026, as transcribed by The Motley Fool, since I found no primary copy. Crusoe gives no energisation date for phase two. Oracle reports handover, not chips at work, by site.'),
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
get = entry('america-rations-the-plug')
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
EARLIER = [
 ('contracted-energised-running', 'Contracted, energised, running', '30 October 2026',
  'Open. Oracle put Abilene\'s last two buildings in its quarter to 30 November 2026; its December results are the reading, and nothing confirms delivery by 7 November. Nebius reports its connected power on 12 November. The Malaysian limb is followed in the piece on Johor and Singapore.'),
 ('the-power-it-drops', 'The grid\'s new problem is not the power AI uses, it is the power it drops', '22 September 2026',
  'The fault "cleared properly" and this was PJM\'s third such transfer in about two years, which supports the second limb; PJM later put the July event at about 3,900 MW. The first limb is open: nobody has published what compliance costs. PJM times the event to the minute, and its second wave came a minute after the first, so "under a second" is my reading, not PJM\'s figure.'),
 ('what-the-battery-is-really-for', 'The battery has quietly stopped being an energy product', '22 September 2026',
  'California\'s 17.3 GW fleet is a time-shifter, earning about four times as much from shifting energy as from balancing. My count of the 2026 summer narrows the claim to, at most, the newest buyers beside data centres. Texas\'s planned 12.9 GW counts grid batteries, which also trade, and no one publishes the share at data centre sites. PJM rates a four-hour battery below demand response, and falling.'),
 ('nebius-paid-for-what-is-switched-on', 'Nebius has lined up five gigawatts of power. It expects about one switched on this year.', '30 September 2026',
  'Against the first limb: on Nebius\'s own definitions buyers pay for active power, chips installed and running, which comes after connection. The 800 MW limb is unresolved until Nebius reports the end of 2026. Its letter of 12 August put prepayments in about 70% of second quarter deals, and nothing since shows them fading. I have found no primary evidence of a Nebius customer selling its spare capacity.'),
 ('power-first-chips-last', 'Jane Street now commits to the power first and picks the chips last', '25 September 2026',
  'Nothing I have found cuts against it. It rests on one firm\'s own account, and I have no published outage record to test the generator saving either way. Jane Street\'s US$6 billion commitment to CoreWeave in April gives no megawatts or dates: a builder short of finished power also rents it.'),
]
parts = ['Five earlier claims on the plug, the battery and the stages, word for word:']
for cid, title, date, note in EARLIER:
    g = entry(cid)
    parts.append(f'**{title}** ({date})\n\nClaim: "{g("claim")}"\n\nBreaks if: "{g("breaksIf")}"\n\nWhere later evidence bears on it: {note}')
out = out.replace('EARLIER_CLAIMS', '\n\n'.join(parts))
open(os.path.join(ROOT, 'src/content/journal', OUT + '.md'), 'w').write(out)
print('ok', OUT, len(re.sub(r'<[^>]+>', ' ', out).split()))
