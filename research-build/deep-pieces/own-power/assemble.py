"""Build src/content/journal/building-your-own-power-depth.md from the source, the figures and the claims.
At launch the output replaces building-your-own-power.md (same URL); its claims already have that home."""
import re, os, sys, datetime
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '../../..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else 'building-your-own-power-depth'
src = open(os.path.join(D, 'own-power.src.md')).read()
svg = lambda n: open(os.path.join(D, 'illos', n + '.svg')).read()
FIGS = {
 'turbine': ('illo', 'A gas turbine is a jet engine on the ground; a combined cycle adds a steam loop to use its waste heat', 'A heavy gas turbine and a combined cycle plant, simplified, not to scale', 'GE Vernova 7HA.03 and Siemens Energy HL-class figures; Mitsubishi Heavy for the 1,600°C turbine inlet. My drawing; real plants often put two turbines on one boiler and steam turbine.'),
 'blade': ('illo', 'The gas is hotter than the blade alloy\'s melting point, so the blade lives on its crystal, its cooling and its coat', 'A first-stage turbine blade, simplified', 'Mitsubishi Heavy (1,600°C); US Department of Energy; the melting point is for CMSX-4, a common single-crystal alloy, from published metallurgy studies, not a maker. My drawing.'),
 'boom-chart': ('chart', 'America built about 238 GW of gas plant in six years, then the orders fell away', 'Gigawatts of gas-fired capacity by the year it entered service, plants still running or since retired', 'EIA generator inventory (Form EIA-860M), September 2026; nameplate capacity, my sums. Plants retired before the inventory\'s coverage are missing, so early years are slight undercounts. Siemens (16 November 2017) and GE (7 December 2017).'),
 'queue-chart': ('chart', 'GE Vernova\'s turbine queue grew by almost half in nine months', 'Gas turbine gigawatts under contract, firm orders and paid reservations, at each quarter end', 'GE Vernova results releases to 28 October 2026. Years of output are my arithmetic at its present 20 GW a year. The dashed line is GE Vernova\'s own expectation for the end of 2026.'),
 'makers-chart': ('chart', 'All three big makers are booked for years', 'Gas turbine gigawatts under contract, firm and reserved, at each maker\'s latest report', 'GE Vernova (28 October 2026); Siemens Energy analyst presentation (5 August 2026); Mitsubishi Heavy (6 November 2026), which publishes no reservation figure. Dates and definitions differ.'),
 'cost-chart': ('chart', 'New gas plants now cost two to three times the government\'s planning figure', 'Capital cost, US dollars per kilowatt; builders\' figures are my arithmetic', 'EIA capital cost study for AEO2025 (January 2024, 2023 dollars); Duke Energy Form 10-Q to 30 September 2026; ProPetro (28 October 2026); Williams (13 July 2026). Bases differ: some include financing, and Williams\' may include pipe.'),
 'aero-chart': ('chart', 'Even the fast lane takes orders faster than it can ship them', 'GE Vernova aeroderivative gas turbines, units ordered and shipped', 'GE Vernova 2025 Form 10-K and Form 10-Q to 30 September 2026. The backlog is my arithmetic.'),
 'island': ('illo', 'On the grid, other plants cover a trip or a swing; an island must carry its own spares and buffer', 'Two ways to power a campus; the island is schematic, not Socrates\' actual layout', 'PJM Planning Committee (6 October 2026); Williams Forms 10-K and 10-Q; Wärtsilä\'s engines-versus-aeroderivatives comparison. That islands need more machine than load is my hypothesis, not a finding.'),
 'gas-chart': ('chart', 'A gigawatt of fast machines burns about 46 per cent more gas than a combined cycle', 'Gas burned by one gigawatt running flat out for a day, billion cubic feet', 'My arithmetic from EIA\'s average tested heat rates for 2025 (Electric Power Annual, Table 8.2) and 1,036 Btu per cubic foot. Real running on hot days and part load is worse.'),
 'routes': ('chart', 'Own power is quick for a few hundred megawatts; gigawatts and new turbines take years', 'Dated routes to on-site gas power and its fuel, from the first decision to the first power or gas', 'Hollow dot: approval, permit, financing, signing, open season or sale. Solid dot: the date the owner gives; a thick line is a range. Williams; Pennsylvania DEP and Homer City; Entergy; Wärtsilä; Transco; Kinder Morgan; GE Vernova. A turbine shipped in 2032 needs about 18 months on site.'),
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
get = entry('building-your-own-power')
d = datetime.datetime.fromisoformat(get('date'))
out = out.replace('CLAIM_DATE', f'{d.day} {d:%B %Y}').replace('CLAIM_TEXT', get('claim')).replace('BREAKS_TEXT', get('breaksIf'))
EARLIER = [
 ('the-way-out-has-its-own-queue', 'The best argument against my own thesis, and why I still think it is wrong', '22 September 2026',
  'Holding on the machines. Siemens Energy\'s own investor slides (5 August 2026) now confirm 95 GW under contract, and GE Vernova\'s aeroderivative backlog, 124 units at 30 September 2026, shows the quicker turbines queuing too. Transformers and switchgear are tested in The equipment queue. The second limb, own generation against comparable grid connections, is untested: EIA\'s generator survey covers only plants connected to the grid, so off-grid plants such as Socrates cannot be set against a grid date from it.'),
 ('the-product-is-time', 'Bloom Energy is not selling electricity. It is selling time.', '24 September 2026',
  'Bloom\'s product margin was 37.9 per cent in the third quarter of 2026 against 35.0 per cent a year earlier, by my calculation, but it sat near 35 per cent for the two years before, so its buyers paid mainly in volume, not price. Oracle intends, rather than has committed, to procure up to 2.8 GW, 1.2 GW of it contracted. The claim stands; its margin test is weak.'),
 ('ge-vernova-sells-the-wait', 'GE Vernova\'s customers are paying years in advance for a place in its queue', '9 October 2026',
  'Holding. At 30 September 2026, 122 GW was 6.1 years of 20 GW output, above four years of the 2030 step. Power deposits reached US$33.2 billion; they are reported for the whole Power segment, which also covers nuclear and hydro, though the filings tie the rise to gas orders and reservations. No new heavy turbine factory has been announced, and 2026 orders are priced about 50 per cent above 2025\'s per kilowatt.'),
]
parts = ['Three earlier claims on this queue, word for word:']
for cid, title, date, note in EARLIER:
    g = entry(cid)
    parts.append(f'**{title}** ({date})\n\nClaim: "{g("claim")}"\n\nBreaks if: "{g("breaksIf")}"\n\nWhere later evidence bears on it: {note}')
out = out.replace('EARLIER_CLAIMS', '\n\n'.join(parts))
open(os.path.join(ROOT, 'src/content/journal', OUT + '.md'), 'w').write(out)
print('ok', OUT, len(re.sub(r'<[^>]+>', ' ', out).split()))
