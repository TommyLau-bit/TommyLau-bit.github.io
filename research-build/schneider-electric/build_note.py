# -*- coding: utf-8 -*-
"""Schneider Electric SE (Euronext Paris: SU) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/schneider-electric.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Schneider Electric SE (Euronext Paris: SU)"
DLONG = datetime.date.fromisoformat(DATE).strftime("%-d %B %Y")

EXTRA_CSS = """
a { color: #1F3864; text-decoration: none; }
.chartsrow { break-inside: avoid; margin-top: 2px; }
.keeptogether { break-inside: avoid; }
table.datatable.compact td { padding: 2.6px 7px; font-size: 8.5pt; }
table.datatable.compact th { padding: 4px 7px; font-size: 8.5pt; }
p.lede { font-size: 10.4pt; font-weight: 700; color: #1F3864; margin: 0 0 6px 0; line-height: 1.28; }
p.draftnote { font-size: 8.2pt; color: #C00000; font-weight: 700; margin: -6px 0 8px 0; }
"""

P_ = []
A = P_.append


def cols(html, widths):
    cg = "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in widths) + "</colgroup>"
    i = html.index(">") + 1
    return html[:i].replace('class="datatable', 'style="table-layout:fixed" class="compact datatable') + cg + html[i:]


def eur(x, d=0):
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"€{q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


def bn(x, d=1):
    return f"€{x / 1000:,.{d}f}bn"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = eur(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {eur(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = ("My draft view" if CALL["draft"] else "My call")
need_eps_long = PRICE * 1.15 / MULT
need_eps_short = PRICE * 0.75 / MULT
ppa_ps = PPA * (1 - TAX) / SH_PTC28
above = sum(v > PRICE for r in VGRID for v in r)
above15 = sum(v >= PRICE * 1.15 for r in VGRID for v in r)
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

A('<h1 class="doctitle">Schneider Electric SE</h1>')
A('<p class="docsubtitle"><b>Euronext Paris: SU | Electrical distribution, UPS, prefabricated power and cooling, automation and industrial software | Rueil-Malmaison, France</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"€{PRICE:,.2f} (Euronext Paris close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"€{PRICE:,.2f}, close {PRICE_DATE}; €{PRICE_PRE_DEAL:.2f} on 2 Oct, before the PTC deal; past-year range €{LO52:.2f} to {HI52:.2f} (intraday)"),
    ("Market value", f"About €{MCAP:,.1f}bn on {SHARES_OUT:,.1f}m shares"),
    ("Net debt, 30 June 2026", f"€{H['nd_h126'] / 1000:.1f}bn, before Cognite (US$3.1bn) and PTC"),
    ("P/E on consensus", f"{PE_C26:.1f}x 2026, {PE_C27:.1f}x 2027 (stockanalysis.com, 25 Sep); peer median {PEER_MED:.1f}x 2026"),
    ("2026 target (30 Jul)", "Organic revenue +10% to +13%; adjusted EBITA margin about 19.4% to 19.7%"),
    ("2026 to 2030 (CMD)", "Organic revenue +7% to +10% a year; margin +250bps cumulatively"),
    ("PTC (5 Oct)", "US$22.6bn equity, all cash; €5bn to 6bn of new shares and €16bn to 17bn of debt; closing by Q3 2027"),
    ("Next results", f"Q3 2026 revenues on {Q3_DATE}, brought forward from 29 October"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Schneider Electric is still selling AI data centres the finished system. After the PTC sell-off, at €{PRICE:,.2f} the price is close to fair.</p>')
A(para("Schneider makes the switchgear, UPS, prefabricated power rooms and cooling that go inside data centres. On 7 October I argued "
       "its AI growth arrives as finished systems built and tested in a factory, because site hours are scarcer than parts. The "
       f"filings support it: Systems grew {Q_GROW['Systems'][4] * 100:.0f}% organic in Q2 2026 against {Q_GROW['Products'][4] * 100:.0f}% for Products, "
       f"and on my arithmetic supplied {SYS_CONTRIB_SHARE * 100:.0f}% of the quarter's organic growth from a third of the base."))
A(para(f"Then, on 5 October, Schneider agreed to buy PTC, a design software company, for US$22.6bn in cash. In two trading days the "
       f"shares fell {abs(DROP) * 100:.0f}% and about €{MCAP_LOST:.0f}bn of market value went, more than the €21.1bn enterprise value paid. "
       f"On my numbers the deal costs about €{DEAL_COST_PS:.0f} a share: it trims 2028 adjusted EPS by {abs(ACCR_REPORTED) * 100:.0f}% on "
       "Schneider's own definition. But before the deal the shares already sat above my standalone value."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction.</b> My base value, 22 times 2028 adjusted EPS with PTC, "
       f"is {eur(BASE_VALUE)}, {chg(BASE_VALUE)}, inside my no-call band. The bear case is {eur(bear)} ({chg(bear)}) and the bull case "
       f"{eur(bull)} ({chg(bull)}). Without PTC the base would be {eur(BASE_STANDALONE)}, {chg(BASE_STANDALONE)}: no call either way."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (Schneider's adjusted measures; calendar years)"))
A(datatable(
    ["€ million unless stated", "2024A", "2025A", "H1 2026A", "2026E*", "2027E*", "2028E*", "2028E* with PTC"],
    [
        ["Revenue", f"{REV_H[0]:,.0f}", f"{REV_H[1]:,.0f}", f"{H['rev_h126']:,.0f}", f"{REV26:,.0f}", f"{REV27:,.0f}", f"{REV28:,.0f}", f"{PT['rev']:,.0f}"],
        ["Organic growth (%)", f"{ORG_H[0] * 100:.1f}", f"{ORG_H[1] * 100:.1f}", f"{H['org_h126'] * 100:.1f}", f"{ORG26 * 100:.1f}", f"{ORG27 * 100:.1f}", f"{ORG28 * 100:.1f}", ""],
        ["Systems, share of revenue (%)", "31", "34", f"about {SYS_H126 * 100:.0f}", "", "", "", ""],
        ["Gross margin (%)", f"{GM_H[0] * 100:.1f}", f"{GM_H[1] * 100:.1f}", f"{H['gm_h126'] * 100:.1f}", "", "", "", ""],
        ["Adjusted EBITA", f"{EBITA_H[0]:,.0f}", f"{EBITA_H[1]:,.0f}", f"{H['ebita_h126']:,.0f}", f"{EBITA26:,.0f}", f"{EBITA27:,.0f}", f"{EBITA28:,.0f}", f"{EBITA28 + PT['ptc_ebita']:,.0f}"],
        ["Adjusted EBITA margin (%)", pc(EBITA_H[0] / REV_H[0]), pc(EBITA_H[1] / REV_H[1]), pc(H['ebita_h126'] / H['rev_h126']), pc(ST['m'][0]), pc(ST['m'][1]), pc(ST['m'][2]), pc((EBITA28 + PT['ptc_ebita']) / PT['rev'])],
        ["Adjusted EPS (€)", f"{EPS_H[0]:.2f}", f"{EPS_H[1]:.2f}", f"{H['eps_h126']:.2f}", f"{EPS26:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}", f"{EPS28_PTC:.2f}"],
        ["Consensus adjusted EPS (€)", "", "", "", f"{CONS_EPS_26:.2f}", f"{CONS_EPS_27:.2f}", "n/v", ""],
        [f"P/E at €{PRICE:,.2f} (x)", f"{PRICE / EPS_H[0]:.1f}", f"{PRICE / EPS_H[1]:.1f}", "", f"{PE26:.1f}", f"{PE27:.1f}", f"{PE28:.1f}", f"{PE28_PTC:.1f}"],
        ["Net debt, year end", f"{NETDEBT_H[0]:,.0f}", f"{NETDEBT_H[1]:,.0f}", f"{H['nd_h126']:,.0f}", f"{ND_END26:,.0f}", "", "", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6, 7},
))
A(caption("*2026E to 2028E are my own estimates. Adjusted EPS is Schneider's measure, which deducts amortisation of purchase accounting "
          "intangibles; consensus is on the same basis (stockanalysis.com, S&P Global data, updated 25 September 2026, before the deal); "
          "n/v: 2028 consensus not verified. The H1 2026 Systems share is my arithmetic on the rounded Q1 and Q2 shares. Net debt at end 2026E "
          "includes Cognite and AiDASH; Shelly (€1.2bn, closing expected by Q1 2027) is added in 2027. History from Schneider's full year 2024 and 2025 and half year 2026 releases."))

A('<div class="keeptogether">')
A(section("Two charts: the claim's own test, and a value close to the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_share.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: Systems as a share of revenue, from Schneider's releases; H1 2026 is my arithmetic. The claim fails if the full-year share "
          "falls below 34% in 2026 or 2027 while data centres grow double digit. Right: value per share from the scenarios, the sensitivity "
          f"grid, the weighted case and the base with and without PTC, against the €{PRICE:,.2f} price (red) and the average analyst target, "
          "set before the deal."))
A('</div>')

A(section("The thesis: more boxed fridges, fewer loose parts"))
A(para("Nobody builds a fridge in their own kitchen. The compressor, pipes and thermostat are joined and tested in a factory, and the "
       "fridge arrives as one sealed box. When every refrigeration engineer in town is booked, the boxed fridge wins. My piece argued "
       "Schneider is selling AI data centres more boxed fridges: prefabricated power rooms, cooling plants and large UPS, shipped ready to connect."))
A(para(f"<strong>The numbers still say so.</strong> Schneider reports sales in three buckets. Systems has grown fastest in each of the last "
       f"five quarters: {', '.join(f'{s * 100:.0f}' for s in Q_GROW['Systems'])}% organic, against "
       f"{', '.join(f'{p * 100:.0f}' for p in Q_GROW['Products'])}% for Products. In Q2 2026 Schneider named prefabricated solutions, cooling "
       "and three-phase UPS as the data centre drivers, and said Data Center &amp; Networks demand was up triple digit and its sales strong "
       "double digit. Data Center &amp; Networks was 30% of 2025 orders, the largest end market."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_growth.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_annual.png"></div></div>')
A(caption("Left: organic growth by business model, per cent, Q2 2025 to Q2 2026, from Schneider's quarterly releases. Right: revenue and "
          "adjusted EPS, 2024 to 2028E; 2024 and 2025 as reported, the rest my estimates, with PTC added in 2028."))
A('</div>')
A(para(f"<strong>The order book backs it.</strong> Backlog reached €{BACKLOG[1]:.1f}bn at the end of 2025, up 18%, and the part due after "
       "more than a year rose from €4.8bn to €8.0bn; Schneider said Systems in North America led it. <strong>So does the cost.</strong> "
       f"The first half carried a €{abs(H['mix']):.0f}m mix drag on adjusted EBITA, \"mainly due to the relatively faster growth of Systems\". "
       "Mix took 0.7 points off gross margin, which still rose to 42.5% on 2.4 points of productivity. Schneider accepts a thinner gross "
       "margin per euro to sell the work already done."))
A(para(f"<strong>But the claim's own test is close.</strong> My piece set the line at a 34% Systems share for a full year. By my arithmetic "
       f"on rounded shares, the first half of 2026 came in at about {SYS_H126 * 100:.1f}%: 33% in Q1, 35% in Q2. Schneider also expects Products "
       "growth to accelerate in the second half on price rises, which lifts the Products share without any change in what data centres buy. "
       "One nuance on spending: net capex fell €48m in H1 2026, but in 2025 it rose €132m to €1,496m, 3.7% of revenue, roughly in step "
       "with sales. That is still not pouring money into plants. I checked the piece's other figures against the releases; they stand."))

A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_bridge.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: my 2028E adjusted EPS without PTC and with it, € per share; PTC's purchase accounting is my assumption. Right: SU month-end "
          "close, October 2024 to the 6 October 2026 close (Euronext Paris, retrieved 7 October 2026; Euronext gives two years), against my base value."))
A('</div>')

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"<strong class='lead'>The sell-off.</strong> The shares closed at €{PRICE_PRE_DEAL:.2f} on 2 October and €{PRICE:,.2f} on "
       f"6 October, down {abs(DROP) * 100:.1f}%, while Legrand rose {LEGRAND_CHG * 100:.1f}% over the same days. About €{MCAP_LOST:.1f}bn of "
       f"market value went, against €21.1bn paid for PTC's enterprise value. The P/E on 2027 consensus fell from {PE_C27_PRE:.1f} to "
       f"{PE_C27:.1f} times. Schneider plans €5bn to 6bn of new shares, about {ABO / 1000 / MCAP * 100:.0f}% of today's market value, and had not "
       "launched the sale by 6 October."))
A(para(f"<strong class='lead'>What the deal costs on my numbers.</strong> PTC earned about 40% adjusted EBITA margins on €2.4bn of 2025 "
       f"revenue; the price is 21 times 2027E EBITA, which implies about €{PTC_EBITA27:,.0f}m. In 2028, the first full year, I take "
       f"€{PT['ptc_ebita']:,.0f}m including €{SYN28:.0f}m of cost synergies, against €{PT['interest']:,.0f}m of extra interest, "
       f"{NEW_SH:.0f}m new shares at an assumed €{ABO_PX:.0f}, and no buybacks in 2027 and 2028. The €22bn cash consideration exceeds "
       "PTC's €21.1bn enterprise value, so I take it to cover PTC's debt and costs and add nothing on top. Before purchase accounting that is "
       f"{ACCR_PRE_PPA * 100:+.1f}% on EPS, in line with management's \"low single-digit\" accretion. But Schneider's adjusted EPS deducts "
       f"purchase accounting amortisation. With my €{PPA:.0f}m a year for PTC, which is not disclosed, 2028 EPS falls from "
       f"€{EPS28:.2f} to €{EPS28_PTC:.2f}, {ACCR_REPORTED * 100:.1f}%."))
A(para(f"<strong class='lead'>Where I differ.</strong> At 22 times, that is about €{DEAL_COST_PS:.0f} a share, against a €{PRICE_PRE_DEAL - PRICE:.0f} "
       f"fall. So the market priced the deal as worse than my numbers say. But at €{PRICE_PRE_DEAL:.0f} the shares were already above my "
       f"standalone value of {eur(BASE_STANDALONE)}. The price now needs 2028 adjusted EPS of €{NEED_EPS:.2f} at 22 times. My model reaches "
       f"that with organic growth of about {NEED_ORG * 100:.1f}% a year in 2027 and 2028, below the 7% floor of Schneider's 2030 target. I "
       f"take {ORG27 * 100:.0f}% and {ORG28 * 100:.0f}%. That is a real gap, but a small one, and leverage rises: net debt to adjusted EBITA goes "
       f"from {LEV_25:.1f} times at the end of 2025 to about {LEV_CLOSE:.1f} times at closing, on my estimates, after Cognite, "
       "Shelly and PTC."))

A(section("Valuation, with the working"))
A(para(f"I value Schneider on P/E, as its peers are quoted, using 2028E adjusted EPS, the year the market will price in October 2027. "
       f"2026E takes {ORG26 * 100:.0f}% organic growth, the upper half of the guide, a €450m currency drag and a {M26 * 100:.1f}% margin: EPS "
       f"€{EPS26:.2f}, against €{CONS_EPS_26:.2f} consensus. 2027E takes {ORG27 * 100:.0f}% growth and a {ST['m'][1] * 100:.1f}% margin: "
       f"€{EPS27:.2f}, {abs(EPS27 / CONS_EPS_27 - 1) * 100:.0f}% below the €{CONS_EPS_27:.2f} consensus, mainly on margin and financing "
       f"costs. 2028E takes {ORG28 * 100:.0f}% and {ST['m'][2] * 100:.1f}%: €{EPS28:.2f} standalone and €{EPS28_PTC:.2f} with PTC."))
A(para(f"<strong>The multiple.</strong> I use 22 times. On 2026 consensus Schneider trades at {PE_C26:.1f} times, against a {PEER_MED:.1f} times "
       f"median for Eaton, Vertiv, ABB, Siemens and Legrand; my 2026E at that median gives {eur(EPS26 * PEER_MED)}. One year forward, "
       f"Schneider trades at {PE_C27:.1f} times today and traded at {PE_C27_PRE:.1f} before the deal. I sit between, because leverage "
       f"rises by about {(LEV_CLOSE / LEV_25 - 1) * 100:.0f}% and EPS growth slows to about {(EPS28_PTC / EPS27 - 1) * 100:.0f}% in 2028."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "Organic 2027 / 2028", "Margin 2028", "P/E", "EPS 2028E", "Value", "Change", "Weight"],
    [
        ["Bear", "Data centre orders digest; no synergies", f"{SCEN[0][1] * 100:.0f}% / {SCEN[0][2] * 100:.0f}%", pc(SV[0]['m28']), f"{SCEN[0][7]}x", f"€{SV[0]['eps']:.2f}", eur(bear), chg(bear), "25%"],
        ["Base", "Growth inside the CMD range", f"{SCEN[1][1] * 100:.0f}% / {SCEN[1][2] * 100:.0f}%", pc(SV[1]['m28']), f"{SCEN[1][7]}x", f"€{SV[1]['eps']:.2f}", eur(base), chg(base), "50%"],
        ["Bull", "Top of the range; faster synergies", f"{SCEN[2][1] * 100:.0f}% / {SCEN[2][2] * 100:.0f}%", pc(SV[2]['m28']), f"{SCEN[2][7]}x", f"€{SV[2]['eps']:.2f}", eur(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", "", eur(WEIGHTED), chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7, 8}, total_row_idx=3,
), [9, 27, 13, 9, 6, 9, 9, 10, 8]))
A(caption(f"All three include PTC from closing. Without PTC the values would be {eur(SV[0]['value_st'])}, {eur(SV[1]['value_st'])} and "
          f"{eur(SV[2]['value_st'])}. The bear case is not fanciful: the shares closed at €{LO_CLOSE:.2f} on 21 November 2025. The band: long "
          "when my base value is at least 15% above the price, short when it is at least 25% below, no call in between."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 margin against the P/E, with PTC"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["2028 margin"] + [f"{x}x" for x in SENS_X],
    [[pc(m)] + [(f"<b>{eur(v)}</b>" if (i == 1 and j == 1) else eur(v)) for j, v in enumerate(r)]
     for i, (m, r) in enumerate(zip(SENS_M28, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{NUMW[above].capitalize()} of the nine cells sit above the price, but only {NUMW[above15]} clear it by 15% or more, and all of "
       f"those need {SENS_X[2]} times. At {MULT} times even a margin a point above my base gives {eur(VGRID[2][1])}, "
       f"{(VGRID[2][1] / PRICE - 1) * 100:.0f}% above. The three cells below the price all sit at {SENS_X[0]} times; none is 25% below. "
       "Every figure is live in the model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Listing", "P/E 2026 consensus", "What they make"],
    [["Schneider Electric", "Euronext Paris: SU", f"{PE_C26:.1f}x", "Electrical distribution, UPS, prefabricated modules, cooling, automation, software"]]
    + [[c, t, f"{px / e:.1f}x", w + (f" ({n})" if n else "")] for c, t, px, e, cur, w, n in PEERS],
    num_cols={2},
), [20, 18, 13, 49]))
A(caption("Price on 6 October 2026 over 2026 consensus EPS, both from stockanalysis.com (S&P Global data), retrieved 7 October 2026. "
          f"Peer median {PEER_MED:.1f} times. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        [Q3_DATE, "Q3 2026 revenues, brought forward", "Systems against Products growth; data centre commentary; any 2026 target change"],
        ["Not yet set", "Share sale of €5bn to 6bn", "Size and price against my €250 assumption"],
        ["By Q3 2027", "PTC shareholder vote, approvals, closing", "Terms unchanged; debt cost against my 3.5%"],
        ["February 2027 (date not confirmed)", "Full year 2026 results", "Systems share against 34%; 2027 target; PTC accounting"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Data centre digestion.</strong> Data Center &amp; Networks was 30% of 2025 orders and leads the Systems growth. A pause by "
       "hyperscale buyers would hit the fastest-growing bucket first; Europe's data centre sales already fell in Q2 against a strong base. "
       "<strong>The deal.</strong> Schneider pays 21 times 2027E EBITA for a business outside its electrical core, with one-off "
       "implementation costs Schneider puts at €250m and approvals still to come. It also offered €1.2bn in cash for Shelly Group on "
       "24 September, its third software deal since June. A deep discount on the share sale would add dilution."))
A(para("<strong>Costs and currency.</strong> Copper and silver took €330m off H1 adjusted EBITA and tariffs €104m, against €280m of "
       "product price. North America was 40% of Q2 revenue, so a weaker dollar lowers reported euros. <strong>Accounting.</strong> My "
       f"€{PPA:.0f}m of PTC purchase accounting is a guess; if Schneider reports adjusted EPS before it, my 2028E rises by about "
       f"€{ppa_ps:.2f}, worth about €{ppa_ps * MULT:.0f} a share at 22 times."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price at or below about €{REVISIT_LONG:,.0f} with my numbers unchanged, or results that lift "
       f"my 2028E adjusted EPS with PTC to about €{need_eps_long:.2f} or more. <strong>Into a short:</strong> a price at or above about "
       f"€{REVISIT_SHORT:,.0f}, or 2028E EPS at or below about €{need_eps_short:.2f}. <strong>The claim:</strong> a full-year 2026 "
       "Systems share below 34% with data centres still growing double digit would break the piece's claim and the thesis behind this view."))
A(para(f"<strong>The view is wrong if</strong> Schneider's organic revenue growth over the four quarters to September 2027 is below "
       f"{WRONG_ORG[0] * 100:.0f}% or above {WRONG_ORG[1] * 100:.0f}%, the 2027 growth of my bear and bull cases, or its full-year 2026 Systems "
       "share falls below 34% while data centres grow double digit."))
A('</div>')

A(section("Conclusion"))
A(para("My piece argued that Schneider's AI growth arrives as finished systems because site hours are scarcer than parts. The releases "
       f"support it: Systems has outgrown Products for five quarters and supplied most of Q2's growth, though the 34% test is close. The "
       f"PTC deal took {abs(DROP) * 100:.0f}% off the shares; on my numbers it costs about €{DEAL_COST_PS:.0f} a share, but the price was "
       f"rich before it. {my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction. Base value {eur(BASE_VALUE)}, "
       f"{chg(BASE_VALUE)}, range {eur(bear)} to {eur(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Organic revenue growth", pc(ORG26, 0), pc(ORG27, 0), pc(ORG28, 0), "Guide +10% to 13% for 2026; CMD +7% to 10% a year"],
        ["Adjusted EBITA margin", pc(ST['m'][0]), pc(ST['m'][1]), pc(ST['m'][2]), "Guide 19.4% to 19.7%; CMD +250bps to 2030"],
        ["Net financial expense, €m", f"{FIN[0]:.0f}", f"{FIN[1]:.0f}", f"{FIN[2]:.0f} + {PT['interest']:.0f}", "H1 2026 €286m; PTC interest from 2028 (mine)"],
        ["Tax rate", pc(TAX, 0), pc(TAX, 0), pc(TAX, 0), "Guided 23% to 25% for 2026"],
        ["Diluted shares, m", f"{SH[0]:.1f}", f"{SH[1]:.1f}", f"{SH[2]:.1f} / {SH_PTC28:.1f}", "Standalone / with PTC (new shares, no buybacks)"],
        ["PTC EBITA, €m", "", "", f"{PT['ptc_ebita']:,.0f}", "21x price implies €1.0bn for 2027; +10%; €80m synergies"],
        ["PTC purchase accounting, €m", "", "", f"{PPA:.0f}", "Mine; not disclosed"],
        ["P/E on 2028E", "", "", f"{MULT}x", "Between 21.0x and 24.5x on 2027 consensus"],
    ],
), [26, 9, 9, 13, 43]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Schneider Electric financial releases filed with the AMF: Full Year 2024 Results (20 February 2025), Half Year '
  '2025 Results (31 July 2025), Third Quarter 2025 Revenues (30 October 2025), Full Year 2025 Results and presentation (26 February '
  '2026), Q1 2026 Revenues (30 April 2026), Half Year 2026 Results (30 July 2026). Capital Markets Day release, 11 December 2025. '
  '"Schneider Electric to acquire PTC", release and transaction presentation, 5 October 2026 (also PTC Form 8-K, Exhibit 99.1). Share '
  'prices from Euronext Paris historical data; consensus, targets, shares outstanding and peer EPS from stockanalysis.com; all '
  'retrieved 7 October 2026. Estimates for 2026 to 2028, the PTC effect and the valuation are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 7 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/schneider-sells-the-finished-system/">thephysicallayer.fyi/journal/schneider-sells-the-finished-system</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Schneider Electric. Personal research, not investment advice.</p>')
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
