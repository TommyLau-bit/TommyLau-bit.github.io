# -*- coding: utf-8 -*-
"""Constellation Energy Corporation (Nasdaq: CEG) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/constellation.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Constellation Energy Corporation (Nasdaq: CEG)"
DLONG = datetime.date.fromisoformat(DATE).strftime("%-d %B %Y")

EXTRA_CSS = """
a { color: #1F3864; text-decoration: none; }
.chartsrow { break-inside: avoid; margin-top: 2px; }
.keeptogether { break-inside: avoid; }
table.datatable.compact td { padding: 2.6px 7px; font-size: 8.5pt; }
table.datatable.compact th { padding: 4px 7px; font-size: 8.5pt; }
p.lede { font-size: 10.4pt; font-weight: 700; color: #1F3864; margin: 0 0 6px 0; line-height: 1.28; }
.fullwidth > p.body { clear: both; }
p.draftnote { font-size: 8.2pt; color: #C00000; font-weight: 700; margin: -6px 0 8px 0; }
"""

P_ = []
A = P_.append


def cols(html, widths):
    cg = "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in widths) + "</colgroup>"
    i = html.index(">") + 1
    return html[:i].replace('class="datatable', 'style="table-layout:fixed" class="compact datatable') + cg + html[i:]


def usd(x, d=0):
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"US${q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


bear, base, bull = (x["value"] for x in SC)
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
g_mid = (GUIDE26["lo"] + GUIDE26["hi"]) / 2
view_txt = (f"{CALL['direction'].lower()}, with {conv} conviction" if CALL["direction"] == "NO CALL"
            else f"{CALL['direction'].lower()}, target {usd(tgt)}, {conv} conviction")

A('<h1 class="doctitle">Constellation Energy Corporation</h1>')
A('<p class="docsubtitle"><b>Nasdaq: CEG | Nuclear, gas and geothermal power generation; retail electricity supply | Baltimore, Maryland</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{usd(PRICE, 2)} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{usd(PRICE, 2)}, Nasdaq close {PRICE_DATE}; record close {usd(HI_CLOSE, 2)} and intraday high {usd(HI_INTRA, 2)} on 15 Oct 2025"),
    ("Market value", f"US${MCAP:.1f}bn on {SHARES_OUT}m shares (31 Jul 2026)"),
    ("Net debt, 30 Jun 2026", f"US${NET_DEBT / 1000:.1f}bn before about US${SALE_PROCEEDS / 1000:.1f}bn of pending sale proceeds; enterprise value about US${EV:.0f}bn"),
    ("2026 guide (6 Aug 2026)", f"Adjusted operating EPS US$11.50 to 12.50, raised from US$11.00 to 12.00"),
    ("P/E", f"{PE_G26:.1f}x 2026 guide midpoint; {PE_C27:.1f}x 2027 consensus (US${CONS_EPS27:.2f}); {PE_E28:.1f}x my 2028E"),
    ("Crane", f"{CRANE_MW} MW restart for Microsoft, target H2 2027; {CIR_MW} MW of grid rights moved from Eddystone (FERC, 1 Jun 2026)"),
    ("Consensus (stockanalysis.com)", f"Average target {usd(CONS_TP)} ({CONS_N} analysts); forward P/E {FWD_PE_SA:.1f}x"),
    ("Next event", "Q3 2026 results, listed for 9 November 2026 on the investor events page; not confirmed by a release I could read"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Constellation\'s scarcest asset is its place on the grid. At US$265, the shares already price in most of its own plan.</p>')
A(para("Constellation runs America's largest nuclear fleet and is restarting the 835 MW Crane reactor, the former Three Mile Island "
       "Unit 1, for Microsoft. My piece of 30 October argued that the fastest nuclear power for AI comes from reactors that already "
       "hold a place on the grid. Its FERC filing agrees: a fresh connection would not have been fully deliverable before the end of 2030."))
A(para(f"The claim holds, and it explains the premium the market pays. Crane adds only about {CRANE_TWH / NUC_TWH_26 * 100:.1f}% to nuclear "
       "output; the money is in pricing the rest of a fleet that already holds its grid places. But the 2027 consensus of "
       f"US${CONS_EPS27:.2f} already sits {CONS_GAP27 * 100:.0f}% above what Constellation's own March framework implies."))
A(para(f"<b>{my_call}: {view_txt}.</b> Twenty times my 2028 EPS of US${E28:.2f} gives {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, inside "
       f"a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} ({chg(bull)}). That is short of my 15% bar for a long."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (calendar years; adjusted operating EPS as Constellation defines it)"))
A(datatable(
    ["US$ per share unless stated", "2024A", "2025A", "2026E*", "2027E*", "2028E*"],
    [
        ["Base EPS, Constellation's framework (midpoint)", "", "", f"{BASE['2026']:.2f}", f"{BASE['2027']:.2f}", f"{BASE28:.2f}&dagger;"],
        ["Enhanced share of the total (%)", "", "", f"{(EPS26 - BASE['2026']) / EPS26 * 100:.1f}", f"{ENH27 * 100:.1f}", f"{ENH28 * 100:.1f}"],
        ["Adjusted operating EPS", f"{ADJ_EPS['2024A']:.2f}", f"{ADJ_EPS['2025A']:.2f}", f"{EPS26:.2f}", f"{E27:.2f}", f"{E28:.2f}"],
        ["Growth (%)", "", f"{(ADJ_EPS['2025A'] / ADJ_EPS['2024A'] - 1) * 100:.1f}", f"{(EPS26 / ADJ_EPS['2025A'] - 1) * 100:.1f}",
         f"{(E27 / EPS26 - 1) * 100:.1f}", f"{(E28 / E27 - 1) * 100:.1f}"],
        ["Guide midpoint / consensus EPS", "", "", f"{g_mid:.2f}", f"{CONS_EPS27:.2f}", ""],
        [f"P/E at {usd(PRICE, 2)} (x)", "", "", f"{PE_G26:.1f}", f"{PE_E27:.1f}", f"{PE_E28:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*2026E is Constellation's first half (US$5.29) plus my US$3.90 for Q3 and US$2.91 for Q4. 2027E and 2028E are my estimates on "
          "Constellation's framework of 31 March 2026: base EPS at its midpoints (US$6.70, US$7.65, US$11.65 for 2026, 2027, 2029) and "
          "enhanced earnings at the midpoint of its 35 to 40% range for 2027 and 35% for 2028. &dagger;My interpolation between 2027 and 2029. "
          "2026 P/E on the guide midpoint. Consensus from stockanalysis.com, checked 28 October 2026."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: earnings on the company's own framework, and a value close to the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: adjusted operating EPS, 2024A and 2025A as reported; 2026E to 2028E split into Constellation's base earnings and my enhanced "
          "share, against the 2027 consensus (red). Right: value per share from the base case, the weighted cases, the sensitivity grid and "
          "the bear to bull range, against the price (grey) and the 15% bar for a long (red)."))
A('</div>')

A(section("The thesis: the reactor was the easy part"))
A(para("Think of the empty house from the piece. The boiler can be fixed in weeks, but the electricity account was closed and the meter "
       "taken away, and the power company will take years to reconnect it. The quick way in is to move the connection from another "
       "house you own and meant to close."))
A(para("Crane is that house. Constellation shut it in 2019 and announced the restart in September 2024, with Microsoft buying its output "
       "for 20 years. It estimated about US$1.6bn of capital spending; a federal loan guarantee of up to US$1.0bn was issued in November "
       "2025, and the NRC approved Crane's fuel licence amendment this summer. Its FERC waiver request of 31 March 2026 says the plant can "
       "physically generate in the second half of 2027, with the regulator's approvals expected early that year."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_crane.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_qeps.png"></div></div>')
A(caption("Left: Crane's dates. Sources: Constellation release of 20 September 2024; FERC waiver request and affidavit, docket ER26-2028-000, "
          "31 March 2026; the claim in my piece of 30 October. Right: adjusted operating EPS by quarter; Q3 2025 derived from the full year. "
          "Sources: Constellation quarterly earnings releases, Form 8-K Exhibit 99.1."))
A('</div>')
A(para("<b>The connection was the hard part.</b> The 10-Q says PJM's first study tied Crane to transmission upgrades with in-service dates "
       "as late as December 2030: hundreds of miles of new 765 kV and 500 kV lines, as far away as West Virginia, the waiver request "
       "adds. On that study the soonest Crane could be fully deliverable was 31 December 2030. So Constellation borrowed a connection. "
       "Eddystone Units 3 and 4, roughly 50-year-old oil and gas units of 380 MW each, were due to retire on 31 May 2025 and now run only "
       "under federal emergency orders, as energy-only resources. FERC agreed on 1 June 2026 that their 760 MW of capacity "
       "interconnection rights can move to Crane, which it said could let Crane be fully operational before 31 December 2030."))
A(para("<b>Nothing in Constellation's filings shows the piece was wrong.</b> Its 2027 date, its 2030 date, the 760 MW and the emergency "
       "orders all match the 10-Q and the waiver request. The claim's own test, power at full output by the end of 2028, is still open."))
A(para(f"<b>Crane is the proof, not the profit.</b> At a {CRANE_CF * 100:.0f}% capacity factor, my assumption, 835 MW makes about "
       f"{CRANE_TWH:.1f} TWh a year, {CRANE_TWH / NUC_TWH_26 * 100:.1f}% of the {NUC_TWH_26} TWh Constellation expects its nuclear fleet "
       f"to make in 2026. Each US$10/MWh of margin on Crane's output is worth about US${EPS_PER_10:.2f} a share a year after tax, on my "
       f"arithmetic. The profit is in the rest of the fleet: Constellation says {AVAIL_TWH} million MWh a year of its nuclear output still "
       "earns only the federal tax credit floor and is free to sell under long contracts. Every one of those MWh already has a grid place."))
A(para(f"That is what Google bought on 6 October: 890 MW of uprates at 11 existing units on a 20-year contract, and a separate 15-year "
       "supply deal for 2,700 MW, price not disclosed. The costs show why existing sites win. US$1.6bn for Crane is about "
       "US$1,900 per kW. Constellation puts the cost of replacing the Calpine gas plants at about US$65bn, more than "
       "twice the US$26.6bn enterprise value it paid. More than US$4.3bn for 890 MW of uprates is about US$4,800 per kW, "
       "and Google still signed for 20 years."))
A(para("Constellation is also bigger than when the story began. It closed the Calpine purchase on 7 January 2026 for about US$21.8bn in "
       "shares and cash, adding about 23 GW of gas, geothermal and battery plants after the sales regulators required. The last of those, "
       "4.4 GW in PJM for US$5.0bn and Brazos Valley in Texas for US$860m, are due to close by the end of 2026."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {usd(PRICE, 2)} Constellation is worth US${MCAP:.1f}bn. Net debt was US${NET_DEBT / 1000:.1f}bn at the end of June, before "
       f"about US${SALE_PROCEEDS / 1000:.1f}bn of sale proceeds, so the enterprise value is about US${EV:.0f}bn. The shares trade at "
       f"{PE_G26:.1f} times the US${g_mid:.2f} midpoint of the raised 2026 guide and {PE_C27:.1f} times the 2027 consensus of "
       f"US${CONS_EPS27:.2f}. The forward P/E is {FWD_PE_SA:.1f} times, against 14.4 times for Vistra, 12.0 for Talen and 9.6 for NRG "
       f"(stockanalysis.com): a premium of seven to twelve turns for a fleet that is mostly nuclear and mostly contracted or floored."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["15 Oct 2025", f"Record close {usd(HI_CLOSE, 2)}", "Peak"],
        ["January 2026", "Calls to cap PJM capacity prices; Calpine closes", "down 20.5%"],
        ["11 May 2026", "Q1 results; guide affirmed", f"down {abs(Q1_MOVE) * 100:.1f}%"],
        ["6 Aug 2026", "Q2 results; guide raised; FERC waiver", f"down {abs(Q2_MOVE) * 100:.1f}%"],
        ["6 Oct 2026", "Google: 890 MW uprates, 2,700 MW supply", f"up {GOOG_MOVE * 100:.1f}%"],
        ["13 to 23 Oct", "No company results", f"down {abs(OCT_FALL) * 100:.1f}%"],
    ],
), [21, 58, 21]))
A('</div></div>')
A(caption("Left: Constellation month-end close, January 2024 to the 29 October 2026 close, against my base value (red). Yahoo Finance, read "
          "30 October 2026. Right: moves from the previous close to the close on the day; January is the month-end change."))
A('</div>')
A(para("I read the fall since the record as the market pricing PJM politics. On 16 January 2026, according to press reports, the White "
       "House and the PJM governors called for an emergency auction and a longer cap on capacity prices, and the shares fell 20.5% that "
       f"month. PJM's 2028 to 2029 auction then cleared at the US$325 per MW-day cap; every Constellation plant in PJM cleared, "
       f"{CAP_MW_ALL:,} MW in all, about US${CAP_REV / 1000:.1f}bn a year of capacity revenue on my arithmetic."))
A(para("<strong class='lead'>Where I agree with the market.</strong> The piece's mechanism is real and it justifies the premium. A grid place "
       "is scarce, Constellation owns more of them than anyone, and buyers like Google pay for them. That is not news to the market, and "
       "at 20 times next year's earnings it is not cheap."))
A(para("<strong class='lead'>Where I differ: the consensus runs ahead of the company's own plan.</strong> On 31 March Constellation split "
       "its earnings into base (contracts, the tax credit floor, average margins) and enhanced (higher prices and trading). It guided base "
       "EPS of about US$6.70 in 2026, US$7.65 in 2027 and US$11.65 in 2029, and put enhanced at 35 to 40% of the 2027 total. At the "
       f"midpoints that gives about US${E27:.2f} for 2027. The consensus of US${CONS_EPS27:.2f} is {CONS_GAP27 * 100:.1f}% higher."))
A(para(f"Part of the gap is fair: the guide was raised by US$0.50 in August, Google signed in October, and enhanced earnings are about "
       f"{(EPS26 - BASE['2026']) / EPS26 * 100:.0f}% of my 2026 estimate, above the company's own 40%. Part of it is a bet that 2026's "
       f"prices and new contracts last. <b>The price pays {PE_E28:.1f} times my 2028 estimate</b>, which already sits close to what the "
       "company's own framework delivers."))

A(section("Valuation, with the working"))
A(para("I value Constellation on adjusted operating EPS, as it reports them, excluding mark-to-market swings, decommissioning trust "
       "results and Calpine merger costs, twelve months out: by October 2027 the market will price 2028 as the year ahead. I use the "
       f"company's own framework rather than build every plant. For 2028 I take the geometric path from US$7.65 to US$11.65, about "
       f"US${BASE28:.2f} of base EPS, and a 35% enhanced share, which gives US${E28:.2f}. The base figures are Constellation's; the paths "
       "and shares are my choices."))
A(para(f"<strong class='lead'>The multiple.</strong> I use {BASE_PE:.0f} times 2028 earnings: about one turn below the forward P/E today, "
       "because the growth after 2028 is base earnings the company has already guided, and well above the 12.0 times median of the three "
       "power peers, because most of Constellation's earnings are nuclear, contracted or floored by the tax credit. "
       f"{BASE_PE:.0f} x US${E28:.2f} = {usd(BASE_VALUE, 2)}, {(BASE_VALUE / PRICE - 1) * 100:.1f}% above the price."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "PJM caps prices for longer, power prices fall, Crane slips; base US$8.60, enhanced 30%", f"US${SC[0]['e28']:.2f}", f"{SC[0]['mult']}x", usd(bear), chg(bear), "25%"],
        ["Base", "Constellation's framework at the midpoints", f"US${SC[1]['e28']:.2f}", f"{SC[1]['mult']:.0f}x", usd(base), chg(base), "50%"],
        ["Bull", "Google's 2,700 MW priced at the low end of the company's range, enhanced 40%; base US$9.94", f"US${SC[2]['e28']:.2f}", f"{SC[2]['mult']}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 43, 11, 9, 10, 10, 8]))
A(caption("2028 EPS = base EPS / (1 - enhanced share). The bear multiple of 15x is near Vistra's today. The bull base adds about US$0.50 for "
          "the Google supply deal on the company's own 2029 sensitivity of US$0.40 a share per GW at a US$20/MWh premium; with no start date "
          "or price disclosed, taking half a year in 2028 is my own assumption."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
grid = [[e * mm for mm in SENS_PE] for e in SENS_EPS]
A(datatable(
    ["2028 EPS"] + [f"{mm}x" for mm in SENS_PE],
    [[f"US${e:.2f}"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
n_s = sum(v <= PRICE * 0.75 for r in grid for v in r)
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
A(para(f"{W[n_above]} of the nine cells sit above the price, but only {W[n_15].lower()} sit 15% or more above it, and all three need "
       f"either 23 times or US$16.50 of earnings. {W[n_s]} sits 25% or more below. A long needs the base 15% or more above the price, a "
       f"short 25% or more below. At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, {my_call.lower()} is no call, with {conv} conviction."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBITDA", "What they run"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w, g in PEERS],
    num_cols={2, 3},
), [17, 13, 11, 10, 49]))
A(caption("Forward P/E and EV/EBITDA from stockanalysis.com, updated 29 October 2026. Peer median forward P/E excluding Constellation: 12.0x. "
          "Talen had a trailing net loss, so its EV/EBITDA is not meaningful. Multiples are used only to set the range; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["9 November 2026 (listed, not confirmed)", "Q3 2026 results", f"Adjusted EPS against US${Q3_CONS:.2f} consensus (MarketBeat) and US$3.04 a year earlier; Crane milestones"],
        ["By end of 2026", "PJM asset and Brazos Valley sales close", f"About US${SALE_PROCEEDS / 1000:.1f}bn before tax and adjustments; debt reduction against buybacks"],
        ["Early 2027 (date not announced)", "Q4 2026 results and 2027 guide", "Guide midpoint against US$13.00; enhanced share against 35 to 40%"],
        ["Early 2027", "NRC approvals and PJM agreement for Crane", "Whether the reactor or the connection sets the date"],
        ["H2 2027", "Crane able to generate", "First power to the grid; output against 835 MW"],
        ["2028", "First Google uprate", "On time; pricing of the 2,700 MW supply deal if disclosed"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>PJM politics.</strong> PJM is Constellation's largest market: 15,700 MW of its nuclear plants cleared the latest auction. "
       "The governors' statement and the cap show that the price a scarce grid place earns can be set by politics. That is the bear case, a 30% fall."))
A(para("<strong>Crane slips.</strong> NRC approvals and PJM's agreement are expected early in 2027. A delay hurts the claim more than the earnings."))
A(para("<strong>The fleet runs less.</strong> The nuclear capacity factor was 93.0% in Q2, against 94.8% a year earlier, on more refuelling "
       "outage days, and the plants are old."))
A(para(f"<strong>Gas and integration.</strong> Calpine made Constellation a large gas generator, much of it in Texas. Net debt rose from "
       f"US$5.4bn at the end of 2025 to US${NET_DEBT / 1000:.1f}bn at the end of June; Constellation bought back about US$2.2bn of shares "
       "from January to July."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price below about {usd(LONG_BELOW)}, or a 2027 guide midpoint of US$13.00 or more. Scaled up in "
       "proportion, my 2028 estimate becomes about US$15.40 and the base value about US$310, 17% above the price; on my framework path "
       "alone it would be only about US$299, so the trigger assumes the higher guide carries into 2028. A priced long contract for a large part of the available "
       f"nuclear output would do the same. <strong>Into a short:</strong> a price above about {usd(SHORT_ABOVE)}, or PJM extending the cap "
       "on capacity prices for several more years."))
A(para(f"<strong>{my_call} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para("The October piece argued that the fastest nuclear power for AI comes from reactors that already hold a place on the grid. "
       "Constellation's filings agree: a fresh connection for Crane was not fully deliverable before the end of 2030, and borrowing "
       "760 MW of Eddystone's rights keeps 2027 alive. Nothing I found says the piece was wrong. For the shares, Crane is the proof, not "
       f"the profit, and the market already pays for the rest of the fleet: {PE_C27:.1f} times a 2027 consensus that sits "
       f"{CONS_GAP27 * 100:.0f}% above the company's own framework. {my_call}: {view_txt}; base value {usd(BASE_VALUE)}, range "
       f"{usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Base EPS, US$", f"{BASE['2026']:.2f}", f"{BASE['2027']:.2f}", f"{BASE28:.2f}", "Constellation midpoints; 2028 my geometric path to US$11.65 in 2029"],
        ["Enhanced share", f"{(EPS26 - BASE['2026']) / EPS26 * 100:.1f}%", f"{ENH27 * 100:.1f}%", f"{ENH28 * 100:.1f}%", "Company: ~40% (2026), 35 to 40% (2027), 30 to 35% (2029)"],
    ],
), [24, 13, 11, 11, 41]))
A(caption(f"All my estimates unless marked as Constellation's. Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Constellation second quarter 2026 earnings release (Form 8-K, Exhibit 99.1) and Form 10-Q, 6 August 2026, for '
  'adjusted earnings, guidance, the balance sheet, nuclear output, the Crane interconnection note, the Calpine purchase and divestitures, '
  'and share repurchases. Constellation first quarter 2026 release, 11 May 2026, and fourth quarter 2025 release, 24 February 2026. '
  'Constellation 2026 Business and Earnings Outlook (Form 8-K, Exhibit 99.1), 31 March 2026, for base and enhanced earnings, the 2029 '
  'framework, its sensitivities and the Calpine replacement cost. Constellation Form 8-K of 14 July 2026 on the PJM 2028 to 2029 capacity '
  'auction and Form 8-K/A of 20 April 2026 on the Calpine closing. Constellation\'s request for '
  'limited waiver at FERC, docket ER26-2028-000, 31 March 2026, with its supporting affidavit, and the FERC order of 1 June 2026 as quoted by '
  'Utility Dive and the American Nuclear Society. Constellation and Google announcement of 6 October 2026. Constellation third quarter 2024 '
  'results, 4 November 2024, for the US$1.6bn estimate. Share prices from Yahoo Finance; consensus, targets and peer multiples from '
  'stockanalysis.com (S&amp;P Global data); third quarter consensus from MarketBeat; all retrieved 30 October 2026. Estimates for the '
  'second half of 2026, 2027 and 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 30 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/constellation-restarts-the-reactor/">thephysicallayer.fyi/journal/constellation-restarts-the-reactor</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Constellation. Personal research, not investment advice.</p>')
A('<p class="signoff">Tommy Lau | The Physical Layer | thephysicallayer.fyi</p>')
A('</div>')

html = page_shell("\n".join(P_), FOOT, DLONG).replace("</style>", EXTRA_CSS + "</style>")
hp = f"{D}/{SLUG}_note.html"
open(hp, "w", encoding="utf-8").write(html)
render_pdf(hp, PDF)

import pypdfium2 as pdfium
doc = pdfium.PdfDocument(PDF)
print("pages", len(doc))
doc[0].render(scale=2).to_pil().save(PNG)
print("thumb", PNG)
