# -*- coding: utf-8 -*-
"""Fluence Energy (Nasdaq: FLNC) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/fluence.md.
"""
import datetime
from decimal import Decimal, ROUND_HALF_UP
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Fluence Energy (Nasdaq: FLNC)"
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


def usd(x, d=2):
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"US${q:,.{d}f}"


def m(x):
    return f"{x:,.0f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def mv(a, b):
    x = b / a - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.1f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = usd(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
direction = CALL["direction"].lower() if CALL["direction"] == "NO CALL" else CALL["direction"]

A('<h1 class="doctitle">Fluence Energy, Inc.</h1>')
A('<p class="docsubtitle"><b>Nasdaq: FLNC | Grid battery storage systems, services and software | Arlington, Virginia</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:,.2f} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:.2f}, Nasdaq close {PRICE_DATE}; highest close US${HI_CLOSE:.2f} (3 Feb 2026); intraday high US${HI_INTRA:.2f} (30 Jan 2026); 52-week low close US${LO_CLOSE:.2f} (22 Sep 2026)"),
    ("Market value", f"About US${MCAP / 1000:.2f}bn on {SHARES:.1f}m shares (Class A {SH_A:.1f}m plus Class B-1 {SH_B1:.1f}m, 31 Jul 2026)"),
    ("Net debt", f"US${NETDEBT_JUN:.0f}m at 30 Jun 2026 (US${CONVERT:.0f}m convertible less US${CASH_JUN:.0f}m cash); about US${NETDEBT:.0f}m at 30 Sep 2026 on my estimate"),
    ("Enterprise value", f"About US${EV / 1000:.2f}bn; {EV_S26:.2f}x the FY26 revenue guide, {EV_S28:.2f}x my FY28 revenue"),
    ("FY26 guide (16 Sep 2026)", "Revenue about US$2.4bn (was US$3.2 to 3.6bn); adjusted EBITDA loss about US$200m"),
    ("Backlog, 30 Jun 2026", "US$6.4bn, a record; 48 to 53% expected as revenue in the next 12 months"),
    ("Consensus (stockanalysis.com)", f"FY27 revenue US${CONS_REV_27 / 1000:.2f}bn; average target {usd(CONS_TP)} ({CONS_N} analysts), median {usd(CONS_TP_MED)}"),
    ("Next event", "FY26 results, first US production figures and the FY27 plan; date not announced (last year 24 November)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Fluence has the orders. Until its Houston line proves it can make American-made systems, US$7.43 is a fair price for not knowing.</p>')
A(para("Fluence designs the large battery systems that utilities and, now, data centres buy. My piece of 12 October argued that its "
       "American deliveries are limited not by demand but by how fast it can make systems that count as American-made, which tax "
       "rules reward, and that a new Houston line making them fell badly behind this summer."))
A(para(f"The filings support the claim. Backlog reached a record US$6.4bn at the end of June and orders nearly tripled, yet the "
       f"revenue guide for the year to September 2026 was cut twice in six weeks, to about US$2.4bn, {GUIDE_CUT * 100:.0f}% below "
       f"the November midpoint, and the September release names Houston as the primary reason. At US${PRICE:.2f} the shares trade at "
       f"{EV_S28:.2f} times my FY28 revenue: a partial, late recovery."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction.</b> My base case is worth {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, "
       f"inside a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} ({chg(bull)}). I would revisit below about "
       f"{usd(REVISIT_LONG)}, or when Fluence's first published US production figures show Houston near 11 units a day."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (fiscal years to 30 September)"))
A(datatable(
    ["US$ million unless stated", "FY24A", "FY25A", "FY26 guide", "FY27E*", "FY28E*"],
    [
        ["Revenue", m(REV_H[0]), m(REV_H[1]), "about 2,400", m(REV27), m(REV28)],
        ["Revenue growth (%)", "", f"{(REV_H[1] / REV_H[0] - 1) * 100:.0f}", f"{(REV26 / REV_H[1] - 1) * 100:.0f}", f"{G27 * 100:.0f}", f"{G28 * 100:.0f}"],
        ["Adjusted gross margin (%)", f"{AGP_H[0] / REV_H[0] * 100:.1f}", f"{AGP_H[1] / REV_H[1] * 100:.1f}", "", f"{AGM27 * 100:.1f}", f"{AGM28 * 100:.1f}"],
        ["Net operating costs&dagger;", m(OPX_H[0]), m(OPX_H[1]), "", m(OPX27), m(OPX28)],
        ["Adjusted EBITDA", m(EBITDA_H[0]), m(EBITDA_H[1]), "about -200", m(EBITDA27), m(EBITDA28)],
        ["Adjusted EBITDA margin (%)", f"{EBITDA_H[0] / REV_H[0] * 100:.1f}", f"{EBITDA_H[1] / REV_H[1] * 100:.1f}", f"{G26['ebitda'] / REV26 * 100:.1f}", f"{EBITDA27 / REV27 * 100:.1f}", f"{EBITDA28 / REV28 * 100:.1f}"],
        ["Free cash flow", m(FCF_H[0]), m(FCF_H[1]), f"{FCF_9M:,.0f} (9 months)", "", ""],
        [f"EV / revenue at US${PRICE:.2f} (x)", "", "", f"{EV_S26:.2f}", f"{EV / REV27:.2f}", f"{EV_S28:.2f}"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*FY27E and FY28E are my own estimates, not Fluence's. Adjusted measures are Fluence's non-GAAP measures. FY24A and FY25A from the FY25 results release of 24 November 2025; "
          "FY26 is the guide of 16 September 2026; free cash flow for the nine months to June 2026 from the 5 August release. "
          "&dagger;Derived: adjusted gross profit less adjusted EBITDA. EV uses my net debt estimate for 30 September 2026."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: a margin that has to come back, and a valuation that sits around the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and adjusted EBITDA margin, FY24A to FY28E. FY26G is the guide of 16 September 2026; FY27E and FY28E are my "
          "estimates. Right: value per share from the base case, the probability-weighted cases, the sensitivity grid and the bear to "
          f"bull range, against the US${PRICE:.2f} price (red) and the average analyst target."))
A('</div>')

A(section("The thesis: a shop full of orders, waiting on one workshop"))
A(para("Think of the boiler shop from the piece. Its customers get a large discount from the council only if the boiler was built in "
       "this country. Its warehouse is full of cheap imported boilers, and the one local workshop is welding by hand while its robot is "
       "fixed. The shop has more orders than ever. What it can deliver this winter is set by that one workshop."))
A(para("Fluence is that shop, at the scale of power stations. It does not make battery cells: it designs the system, has contract "
       "factories assemble it and writes the software that runs it. Its backlog was a record US$6.4bn at the end of June, and it "
       "expects 48 to 53% of that to become revenue in the next twelve months."))
A(para(f"<b>Demand is not the problem.</b> June quarter orders were more than US$1.44bn, nearly triple a year earlier. In the nine "
       f"months to June it contracted {GW_ORD_9M} GW of storage against {GW_ORD_9M_PY} GW a year before, and its pipeline grew "
       f"{(PIPE_GWH / PIPE_GWH_PY - 1) * 100:.0f}% to {PIPE_GWH} GWh. By July it had about US$850m of data centre business, including "
       "a first large order behind the meter and about US$550m of hyperscaler awards that were not yet purchase orders."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_quarters.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_backlog.png"></div></div>')
A(caption("Left: revenue by quarter and adjusted gross margin as first reported. Right: backlog at quarter end, US$bn, against the "
          "FY26 revenue guide. Sources: Fluence quarterly results releases, 10 February 2025 to 5 August 2026."))
A('</div>')
A(para("<b>Delivery is the problem.</b> The FY26 revenue guide went from US$3.2 to 3.6bn in November 2025 to US$2.9 to 3.1bn on 5 "
       "August and about US$2.4bn on 16 September, with an adjusted EBITDA loss of about US$200m. The September release says demand "
       "\"has remained strong\", the international supply chain \"has continued to work well\", and delays at the Houston contract "
       "manufacturing facility are \"the primary reason\". On the August call the chief executive described Houston as a fully "
       "automated enclosure plant sized for 15 GWh a year, running on generators while it waited for its grid connection. Trade "
       "press reports of the September call say it averaged under one unit a day in August against a plan of eleven, reached three "
       "in early September, and that more than 80% of the cut came from US production; I could not verify these against the replay."))
A(para(f"The money shows where the strain sits. June quarter gross margin was {Q_GM[-1] * 100:.1f}%, against {Q_GM[2] * 100:.1f}% a "
       "year earlier. The quarterly report names liquidated damages, the late delivery penalties agreed in contracts, first for the June "
       "quarter, ahead of cost overruns on newer products and higher battery prices; for the nine months it also names cost increases "
       "on certain projects produced in the US. Customers in the Americas "
       f"made up {AMERICAS_SHARE * 100:.0f}% of revenue in the nine months to June."))
A(para("<strong>Where I was wrong in October.</strong> The piece said: \"Its factories overseas, the company said, kept working "
       "well.\" That is what Fluence said on 16 September. But it followed the line that Fluence \"cut its revenue forecast twice in "
       "six weeks\", and the first cut, on 5 August, blamed two things: \"production issues at a new international contract "
       "manufacturing facility\" and construction delays at the new US one. On the August call management said a new China "
       "facility's first output had needed rework and was then at full production. What showed me the slip was the August release "
       "itself. It does not change the view: the second, larger cut was mainly American, and the claim stands."))
A(para("Fluence says it will publish US production figures, actual and forecast, and a fiscal 2027 business plan with its fiscal "
       "2026 results. Those numbers are the test of the claim and of the shares."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:.2f} Fluence is worth about US${MCAP / 1000:.2f}bn on {SHARES:.1f}m shares, counting the Class B-1 shares AES "
       f"can redeem for Class A one for one. Net debt was US${NETDEBT_JUN:.0f}m at the end of June. The September quarter is not yet "
       f"reported: free cash flow was minus US${abs(FCF_9M):,.0f}m in the nine months, and the S&amp;P Global full-year forecast "
       f"implies about minus US${abs(FCF_CONS_Q4):,.0f}m in the last quarter. I assume US${Q4_BURN:.0f}m of cash use, so net debt of "
       f"about US${NETDEBT:.0f}m and an enterprise value of about US${EV / 1000:.2f}bn, my estimates."))
A(para(f"That is {EV_S26:.2f} times this year's revenue guide and {EV_S27C:.2f} times the S&amp;P Global consensus of "
       f"US${CONS_REV_27 / 1000:.2f}bn for FY27. The average target of {CONS_N} analysts is {usd(CONS_TP)}, but the median is "
       f"{usd(CONS_TP_MED)} and the range runs from {usd(CONS_TP_LO)} to {usd(CONS_TP_HI)}; fourteen rate it a hold, and about "
       f"{SHORT_PCT:.0f}% of the shares are sold short. The market expects a recovery, but not a full or a quick one. I differ on three points."))
A(para(f"<strong class='lead'>Next year is not as safe as consensus.</strong> On the August call Fluence said US${BACKLOG_FY27 / 1000:.1f}bn "
       "of backlog was scheduled for FY27, before the September cut pushed more work into that year. Consensus needs the Houston fix "
       "early and new orders delivered within the year, and the September release lists plans to right-size revenue growth. I take "
       f"US${REV27 / 1000:.1f}bn, a little below consensus."))
A(para(f"<strong class='lead'>The margin comes back, but slowly.</strong> Penalties and launch costs should fade once deliveries run on "
       f"time, and FY25 adjusted gross margin was {AGP_H[1] / REV_H[1] * 100:.1f}%. I assume {AGM27 * 100:.1f}% in FY27 and "
       f"{AGM28 * 100:.0f}% in FY28. Even then Fluence earns little: adjusted EBITDA of about US${EBITDA27:.0f}m in FY27 and "
       f"US${EBITDA28:.0f}m, a {EBITDA28 / REV28 * 100:.1f}% margin, in FY28."))
A(para(f"<strong class='lead'>The balance sheet is the bear case, not the orders.</strong> Total liquidity was US${LIQ_JUN:.0f}m at "
       "the end of June. The revolving credit facility carries a US$150m minimum liquidity test through 31 December 2026 and a "
       "leverage ratio test from 1 January 2027, while adjusted EBITDA is negative. A further slip at Houston would test both, and the "
       "May 2026 shelf registration lets Fluence issue new shares if it must."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [[d, w, mv(a, b)] for d, w, a, b in MOVES] + [["9 Oct 2026", f"Close of US${PRICE:.2f}, {abs(OFF_HIGH) * 100:.0f}% below the highest close", ""]],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: Fluence month-end close, September 2023 to the 9 October 2026 close, against my base value (red). Nasdaq.com historical "
          "data, retrieved 12 October 2026. Right: moves in the session after each release (all filed after the close), close to close."))
A('</div>')

A(section("Valuation, with the working"))
A(para("I value Fluence on enterprise value to revenue in FY28, the year to September 2028, which is what the market will price by "
       f"October 2027. Its EBITDA is too thin to carry the value alone: one point of gross margin moves my FY28 EBITDA by about "
       f"{REV28 * 0.01 / EBITDA28 * 100:.0f}%. I cross-check every case against EBITDA. Net operating costs, adjusted gross profit "
       f"less adjusted EBITDA, were US${OPX_H[0]:.0f}m in FY24 and US${OPX_H[1]:.0f}m in FY25; I take US${OPX27:.0f}m and US${OPX28:.0f}m."))
A(para(f"<b>The multiple: {BASE_MULT:.2f} times FY28 revenue.</b> At my {EBITDA28 / REV28 * 100:.1f}% margin that is about "
       f"{BASE_EVEB:.0f} times EBITDA, below the median of {PEER_MED_EB:.1f} times trailing EBITDA for Sungrow, Nextracker, Shoals and Array "
       f"Technologies. Fluence earns thinner margins than any of them, so I do not use their revenue multiples (median {usd(PEER_MED_S)[3:]} times). "
       f"{BASE_MULT:.2f} x US${REV28:,.0f}m less net debt of US${NETDEBT:.0f}m, over {SHARES:.1f}m shares, gives {usd(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "FY28 revenue", "FY28 EBITDA", "EV/sales", "Value", "Change", "Weight"],
    [
        ["Bear", "Houston stays slow into 2027, the plan is cut again; growth 10% a year, adjusted gross margin 12%", f"US${RV28[0]:,.0f}m", f"US${EB28[0]:.0f}m", f"{SCEN[0][4]:.2f}x", usd(bear), chg(bear), "25%"],
        ["Base", "Houston reaches its rate during 2027; growth 25% then 20%, margin back to 13%", f"US${RV28[1]:,.0f}m", f"US${EB28[1]:.0f}m", f"{SCEN[1][4]:.2f}x", usd(base), chg(base), "50%"],
        ["Bull", "Houston fixed early in 2027, data centre awards become orders; growth 35% then 30%, margin 14.5%", f"US${RV28[2]:,.0f}m", f"US${EB28[2]:.0f}m", f"{SCEN[2][4]:.2f}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [9, 35, 11, 10, 8, 10, 9, 8]))
A(caption(f"All cases start from the FY26 guide of about US$2.4bn, use my FY28 net operating costs of US${OPX28:.0f}m for EBITDA, and "
          f"take off the same net debt over the same shares. The bull multiple is about {EVEB[2]:.0f} times FY28 EBITDA. The bear "
          "multiple prices a company with almost no earnings and a cash question; its EBITDA multiple is not meaningful."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: FY28 revenue against the revenue multiple"))
A('<div class="chartsrow"><div class="col left">')
grid = [[value(e, mm) for mm in SENS_MULT] for e in SENS_REV]
A(datatable(
    ["FY28 revenue"] + [f"{mm:.2f}x" for mm in SENS_MULT],
    [[f"US${e:,.0f}m"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_REV, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
A(para(f"{n_above} of the nine cells sit above the price, but only {n_15} sit 15% or more above it, and each of those needs revenue "
       "above my base, a multiple above it, or both. Under my rule, a long needs the base value 15% or more above the price and a "
       f"short needs it 25% or more below. At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, " + ("my draft view is no call." if CALL["draft"] else "I make no call.")))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "EV/sales", "EV/EBITDA", "What they make"],
    [[c, t, f"{s:.2f}x", (f"{e:.1f}x" if e else "n.m."), w] for c, t, s, e, w in PEERS],
    num_cols={2, 3},
), [19, 15, 10, 11, 45]))
A(caption("Trailing EV/sales and EV/EBITDA from stockanalysis.com, retrieved 12 October 2026; n.m. where EBITDA is negative. Median of the "
          f"four peers with positive EBITDA (excluding Eos Energy): {usd(PEER_MED_S)[3:]}x EV/sales and {PEER_MED_EB:.1f}x EV/EBITDA. Multiples are used only to set the range for Fluence; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Late November 2026 (date not announced)", "FY26 results, first quarterly US production figures and the FY27 plan", "Houston units a day against 11; FY27 revenue against US$2.6 to 3.5bn; September quarter cash use"],
        [LEAD_PLAINTIFF, f"Lead plaintiff deadline in {CASE.split(',')[0]}", "Any change to disclosure or reserves"],
        ["31 Dec 2026 / 1 Jan 2027", "Minimum liquidity test ends; leverage ratio test begins", "Waiver, new facility or new equity"],
        ["End of March 2027", "The claim's test date", "Houston at about 11 units a day or a 15 GWh a year pace; FY27 plan not cut again"],
        ["Each quarter", "Results and Form 10-Q", "Liquidated damages and gross margin; whether the US$550m hyperscaler awards become orders"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Houston.</strong> Everything turns on it. In August Fluence expected full production in the three months to December "
       "2026; trade press reports of the September call put it at three units a day against eleven, after a switch to manual welding. "
       "A new chief operating officer, Bernerd Da Santos, formerly of AES, started on 15 September to run supply chain and manufacturing."))
A(para("<strong>Cash and covenants.</strong> A weak first quarter of FY27 could force a waiver, a smaller facility or new shares. "
       "Fluence says its aim is to fund the backlog without external capital."))
A(para("<strong>Penalties.</strong> Liquidated damages reduce revenue as projects slip. Trade press puts this year's in the tens of "
       "millions of dollars, with figures that differ between reports. Each month Houston runs late adds to them."))
A(para("<strong>Data centre awards.</strong> The US$550m of hyperscaler awards were not purchase orders in August. Data centre buyers "
       "want speed, and delays could send them to Tesla Energy or Sungrow, which also build complete systems."))
A(para("<strong>Policy.</strong> The domestic content bonus and the prohibited foreign entity rules make US-made systems scarce. Fluence "
       "believes its US suppliers comply under Treasury guidance of 12 February 2026. A change would cut both ways."))
A(para(f"<strong>Holders and lawsuits.</strong> Siemens and AES each hold about 41.4m shares, and selling holders can still sell "
       f"{SELLABLE:.1f}m shares under the May 2026 shelf. A securities class action, {CASE}, was filed on {CASE_FILED} for buyers "
       f"between 24 November 2025 and 16 September 2026; the lead plaintiff deadline is {LEAD_PLAINTIFF}."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price below about {usd(REVISIT_LONG)}, where my base value would sit 15% above it on unchanged "
       "estimates, or Fluence's first US production figures showing Houston at or near 11 units a day with an FY27 plan of at least "
       f"US$3.0bn. <strong>Towards a short:</strong> a price above about {usd(REVISIT_SHORT)}, where my base value would sit 25% below it."))
A(para(f"<strong>The view is wrong if</strong> {WRONG_IF[0].lower() + WRONG_IF[1:]}"))
A('</div>')

A(section("Conclusion"))
A(para("The October piece argued that Fluence's American deliveries are limited by how fast it can make systems that count as "
       "American-made, not by demand. Its filings say so: a record US$6.4bn backlog, orders nearly tripled, and a September release "
       "that blames Houston and says demand stays strong. One correction: the first cut, in August, also named a new overseas factory, "
       "since fixed. The claim stands. But a claim about a bottleneck does not say how long it lasts, and at "
       f"US${PRICE:.2f} the shares price a recovery that is partial and late. {my_call}: {CALL['direction']}, {conv} conviction; base "
       f"value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY26", "FY27E", "FY28E", "Basis"],
    [
        ["Revenue growth", f"{(REV26 / REV_H[1] - 1) * 100:.0f}% (guide)", f"{G27 * 100:.0f}%", f"{G28 * 100:.0f}%", "Below FY27 consensus; record backlog supports FY28"],
        ["Adjusted gross margin", "", f"{AGM27 * 100:.1f}%", f"{AGM28 * 100:.0f}%", "Back to about the FY24 and FY25 level by FY28"],
        ["Net operating costs, US$m", "", f"{OPX27:.0f}", f"{OPX28:.0f}", "US$270m in FY24, US$290m in FY25"],
        ["Net debt, US$m", f"{NETDEBT:.0f} (Sep, est.)", "", "", f"June net debt plus my US${Q4_BURN:.0f}m September quarter cash use; held flat"],
        ["Shares, m", f"{SHARES:.1f}", "", "", "Class A plus Class B-1, 31 July 2026; convertible out of the money"],
        ["Multiple, EV / FY28 revenue", "", "", f"{BASE_MULT:.2f}x", f"About {BASE_EVEB:.0f}x FY28 EBITDA; peer median {PEER_MED_EB:.1f}x"],
    ],
), [25, 16, 9, 9, 41]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Fluence quarterly results releases on Form 8-K, Exhibit 99.1, of 10 February 2025, 7 May 2025, 11 August 2025, '
  '24 November 2025, 4 February 2026, 6 May 2026 and 5 August 2026, for revenue, gross and adjusted gross margin, adjusted EBITDA, free '
  'cash flow, orders, backlog, liquidity and guidance. Fluence Form 8-K of 16 September 2026, Exhibits 99.1 and 99.2, for the revised '
  'guide, the Houston statement and the chief operating officer. Fluence Form 10-Q for the quarter to 30 June 2026, filed 5 August 2026, '
  'for the balance sheet, shares, convertible notes, backlog conversion, operating metrics, revenue by region, liquidated damages, the '
  'credit agreement and the shelf registration. Fluence Form 8-K of 15 May 2026 on the AES redemption. Fluence third quarter fiscal 2026 '
  'earnings call, 6 August 2026, transcript published by The Motley Fool, for Houston, FY27 backlog and data centre comments. Latitude '
  'Media, 21 September 2026, mgrid.org, 18 September 2026, and the Quartr summary of the 16 September call, for Houston unit rates, the US '
  'share of the cut and penalties, not verified against the replay. ' + CASE + ', filed ' + CASE_FILED + ', and law firm announcements from 30 September 2026 (Kaplan Fox; Kessler Topaz on Business Wire, 1 October 2026) for the class action. Share '
  'prices from Nasdaq.com historical data; consensus, targets, short interest and peer multiples from stockanalysis.com (S&amp;P Global '
  'data); all retrieved 12 October 2026. Estimates for FY27 and FY28 and the September 2026 '
  'quarter cash use are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 12 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/fluence-short-of-american-made/">thephysicallayer.fyi/journal/fluence-short-of-american-made</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Fluence. Personal research, not investment advice.</p>')
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
