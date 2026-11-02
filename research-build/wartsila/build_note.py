# -*- coding: utf-8 -*-
"""Wärtsilä Oyj Abp (Nasdaq Helsinki: WRT1V) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/wartsila.md.
"""
import datetime
from decimal import Decimal, ROUND_HALF_UP
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Wärtsilä Oyj Abp (Nasdaq Helsinki: WRT1V)"
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


def r(x, d=0):
    return Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)


def eur(x, d=2):
    return f"€{r(x, d):,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pct(x, d=1):
    return f"{r(x * 100, d)}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = eur(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {eur(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
EVT = [(d, w, b / a - 1) for d, w, a, b in EVENTS]

A('<h1 class="doctitle">Wärtsilä Oyj Abp</h1>')
A('<p class="docsubtitle"><b>Nasdaq Helsinki: WRT1V | Engine power plants, marine engines and their service | Helsinki</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{eur(PRICE)} (Helsinki close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{eur(PRICE)}, Nasdaq Helsinki close {PRICE_DATE}; record close {eur(HI_CLOSE)} and intraday high {eur(HI_INTRA)}, both 23 Apr 2026; lowest close in 52 weeks {eur(LO_CLOSE_52)} (18 Nov 2025)"),
    ("Market value", f"About €{MCAP:.1f}bn on {SHARES:,.1f}m shares outstanding at 30 Sep 2026"),
    ("Balance sheet, 30 Sep 2026", f"Net cash of continuing operations €{NET_CASH / 1000:.2f}bn; advances received €{ADVANCES / 1000:.2f}bn"),
    ("Energy, Jan to Sep 2026", f"Orders {EN_BTB_9M:.2f} times net sales; {EN_MW_9M26:,} MW ordered, up {MW_GROWTH_9M * 100:.0f}%; order book €{BOOK_SEP26['EN'] / 1000:.1f}bn, up {EN_BOOK_GROWTH * 100:.0f}%"),
    ("Data centres", f"About 1.9 GW of named orders in nine months, {DC_SHARE_9M26 * 100:.0f}% of Energy's MW (my sum of the orders Wärtsilä named)"),
    ("New mid-term targets (27 Oct 2026)", "Energy: high-teens organic growth, 18% operating margin. Marine: mid-single-digit, 14%. Group: low double digit, 16%"),
    ("Consensus (stockanalysis.com)", f"2027 EPS €{CONS_EPS27:.2f}; average target {eur(CONS_TP)} ({CONS_N} analysts)"),
    ("Next events", "Capital Markets Day 3 November 2026; FY2026 results 5 February 2027 (both confirmed by Wärtsilä)"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Wärtsilä\'s engines are the quicker way to power a data centre, and their queue is lengthening too. At {eur(PRICE)} the market pays for Energy as if the queue will not last.</p>')
A(para("Wärtsilä makes medium-speed engines. Marine sells them, and their service, to shipowners; Energy builds engine power "
       "plants, mostly gas-fuelled, and services them. My September piece argued that building your own gas power swaps the "
       "grid's queue for the makers' queues, and that the fast lane is queued too. On 27 October Wärtsilä said \"lead times for "
       "our engines continue to increase\"."))
A(para(f"The figures agree. Energy took orders at {EN_BTB_9M:.2f} times its net sales in the nine months to September, and its "
       f"order book rose {EN_BOOK_GROWTH * 100:.0f}% in a year to €{BOOK_SEP26['EN'] / 1000:.1f}bn. Named data centre orders were "
       f"{DC_SHARE_9M26 * 100:.0f}% of the megawatts. Yet the shares have fallen {abs(OFF_HIGH) * 100:.0f}% from their April "
       f"record, and with Marine at 14 times my 2027 profit the price leaves Energy at about {EN_IMPLIED_X:.1f} times."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction, 12-month target {eur(tgt)}.</b> My base sum of the parts is "
       f"{eur(BASE_VALUE)}, {chg(BASE_VALUE)}, inside a range of {eur(bear)} ({chg(bear)}) to {eur(bull)} ({chg(bull)}). The "
       f"target is my probability-weighted value, rounded, {chg(tgt)}. Conviction is low because the base value clears my 15% "
       "bar by little, and the Capital Markets Day on 3 November sets the path to the new targets."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (calendar years; continuing operations; comparable operating result is Wärtsilä's measure)"))
A(datatable(
    ["€m unless stated", "2024A", "2025A", "9M 2026A", "2026E*", "2027E*", "Mid-term target"],
    [
        ["Energy net sales", f"{REV24['EN']:,}", f"{REV25['EN']:,}", f"{REV9M['EN']:,}", f"{REV26['EN']:,.0f}", f"{REV27['EN']:,.0f}", "high-teens growth"],
        ["Energy margin (%)", f"{P24['EN'] / REV24['EN'] * 100:.1f}", f"{P25['EN'] / REV25['EN'] * 100:.1f}", "16.0", f"{M26['EN'] * 100:.1f}", f"{M27['EN'] * 100:.1f}", "18"],
        ["Energy orders / net sales (x)", "", f"{ORD25['EN'] / REV25['EN']:.2f}", f"{EN_BTB_9M:.2f}", "", "", ""],
        ["Energy MW ordered", f"{EN_MW_24:,}", f"{EN_MW_25:,}", f"{EN_MW_9M26:,}", "", "", ""],
        ["Marine net sales", f"{REV24['MA']:,}", f"{REV25['MA']:,}", f"{REV9M['MA']:,}", f"{REV26['MA']:,.0f}", f"{REV27['MA']:,.0f}", "mid-single-digit"],
        ["Marine margin (%)", f"{P24['MA'] / REV24['MA'] * 100:.1f}", f"{P25['MA'] / REV25['MA'] * 100:.1f}", f"{P9M['MA'] / REV9M['MA'] * 100:.1f}", f"{M26['MA'] * 100:.1f}", f"{M27['MA'] * 100:.1f}", "14"],
        ["Group net sales", "", f"{GROUP_REV25:,}", f"{GROUP_REV9M:,}", f"{GROUP_REV26:,.0f}", f"{GROUP_REV27:,.0f}", "low double digit"],
        ["Group comparable operating result", "", f"{GROUP_P25:,}", f"{GROUP_P9M:,}", f"{GROUP_P26:,.0f}", f"{GROUP_P27:,.0f}", "margin 16%"],
        [f"EV / comparable operating result at {eur(PRICE)} (x)", "", "", "", f"{EV_P26:.1f}", f"{EV_P27:.1f}", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E and 2027E are my own estimates, not Wärtsilä's. Group figures include Portfolio Business until its last units were "
          "sold on 1 June 2026, and exclude Energy Storage, a discontinued operation. 2024 segment figures from the 2025 Financial "
          "Statements Bulletin (4 February 2026); 2025 and 9M 2026 from the Interim Report of 27 October 2026. Targets announced "
          "27 October 2026; growth is organic. EV is market value less net cash of continuing operations and minorities at book."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: Energy's orders run far ahead of its sales, and data centres are a large share of them"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_energy.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_dc.png"></div></div>')
A(caption("Left: Energy orders and net sales by quarter, €bn, with orders over net sales in red and the order book (RHS). Right: Energy "
          "MW ordered; the dark part is data centre orders Wärtsilä named in its reports (789 MW across 2025, not split by quarter; "
          "429 MW in Q1, 1.2 GW in Q2 and 282 MW in Q3 2026). Shares are my arithmetic. Sources: Wärtsilä interim reports and the "
          "2025 Financial Statements Bulletin."))
A('</div>')

A(section("The thesis: the lighter rig, and its own diary"))
A(para("The piece used a picture. Your street's water main is too small, so you sink your own well, and the big drilling firm is "
       "booked for years. A smaller firm with a lighter rig can come sooner, but its diary is filling too. Gas turbines are the "
       "big rig. Wärtsilä's engines are the lighter one: on the data centre orders it has named, fifteen to twenty-four "
       "engines of about 18 to 19 MW each, built in modules."))
A(para(f"The diary is filling. Energy ordered {EN_MW_9M26:,} MW in the nine months to September, up {MW_GROWTH_9M * 100:.0f}% "
       f"on a year earlier and more than in all of 2025. Its equipment orders were €{EN_EQ_ORD9M:,}m against €{EN_EQ_REV9M}m of "
       f"equipment sales, {EN_EQ_BTB_9M:.1f} times. Only €{BOOK_2026DEL['EN']}m of the €{BOOK_SEP26['EN']:,}m order book is due "
       "this year. Wärtsilä said \"equipment delivery times continued to increase, impacting the timing of revenue recognition\"."))
A(para("<b>How much is data centres?</b> Wärtsilä names its large orders. In 2025 it secured its \"first two projects in the US\", "
       f"{DC_MW_25} MW, {DC_SHARE_25 * 100:.0f}% of the year's megawatts. In 2026 it named 429 MW in the first quarter, \"1.2 GW of "
       "firm data centre-related orders across two projects\" in the second and 282 MW in the third: "
       f"about 1.9 GW on my sum, {DC_SHARE_9M26 * 100:.0f}% of the nine months. It is likely a floor, since smaller orders may not be named. "
       f"The Americas took €{EN_EQ_AMERICAS9M:,}m of the €{EN_EQ_ORD9M:,}m of equipment orders."))
A(para("The other half matters as much. Balancing plants, which back up wind and solar, kept ordering: more than 0.5 GW in the "
       "second quarter and a 300 MW plant in the third, the largest engine power plant Australia has ordered. So Energy's growth is roughly half data centres and half "
       "the older balancing business, on the orders Wärtsilä named."))
A(para("<b>Is engine capacity the limit?</b> On Wärtsilä's words, yes for now. It is expanding output at its Vaasa factory by 35% "
       "by the first quarter of 2028, and to about 2.2 times the 2025 level by the first quarter of 2029. Until then, more orders "
       "lengthen the queue rather than lift sales. In October it named a new source of an old risk: \"price pressure, including from the "
       "ongoing expansion in gas engine and turbine manufacturing capacity\". The queue is real, and so is the competition to "
       "shorten it."))
A(para("The piece's claim holds at Wärtsilä. Its 27 October quote and the 282 MW order of fifteen engines match the report, and "
       "nothing I found shows the piece was wrong. The claim itself is tested on GE Vernova; Wärtsilä is the fast lane's evidence."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {eur(PRICE)} Wärtsilä is worth about €{MCAP:.1f}bn on {SHARES:,.1f}m shares. Less €{NET_CASH / 1000:.2f}bn of net "
       f"cash in continuing operations, the enterprise value is about €{EV:.1f}bn: {EV_P26:.1f} times my 2026 estimate of the "
       f"comparable operating result and {EV_P27:.1f} times my 2027 estimate. The shares trade at {PE_C27:.1f} times the "
       f"€{CONS_EPS27:.2f} consensus EPS for 2027 on stockanalysis.com. Engine and power peers trade at about 19 to 26 times "
       "trailing EV to EBIT."))
A(para(f"<strong class='lead'>What the price implies.</strong> Give Marine 14 times my 2027 estimate, and the price leaves "
       f"Energy at {EN_IMPLIED_X:.1f} times, below every engine peer, for a business now targeting high-teens growth with an order book "
       f"{EN_BOOK_X25:.1f} times last year's sales. Put the other way, with Energy at 18 times the price leaves Marine at "
       f"{MA_IMPLIED_X:.1f} times. The market is not paying for both."))
A(para("The shares have fallen on each of the last four results days, even as orders hit records. Wärtsilä does not say why, and I "
       "do not guess. What the reports show is a gap: group orders up 26% in nine months, reported net sales up 2%, because the "
       "engines are queued. Earnings arrive later than orders. I differ on three points."))
A(para("<strong class='lead'>The queue turns into sales, only later.</strong> Energy's 2026 deliveries are €692m of a €5.6bn book. "
       f"The rest, about €{EN_BOOK_LATER / 1000:.1f}bn, is 2027 and later, at an equipment gross margin Wärtsilä said in July "
       "had risen more than 500 basis points since the start of 2025. My 22% growth for Energy in 2027 needs a fraction of it."))
A(para("<strong class='lead'>Marine is not at a peak that must break.</strong> Marine made 55% of the 2025 comparable result, so the "
       "marine cycle still matters. But 64% of its 2025 sales were service, its order book is up 18%, and newbuild contracts "
       "in the market more than doubled in nine months, on the Clarksons figures Wärtsilä cites. My base gives it 5% growth and no margin gain."))
A(para(f"<strong class='lead'>I do not need consensus.</strong> My 2027 EPS is about €{EPS27:.2f}, below the €{CONS_EPS27:.2f} "
       "consensus. My Energy margin of 17.5% is below the new 18% target. On those numbers the base value is still "
       f"{(BASE_VALUE / PRICE - 1) * 100:.0f}% above the price."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [[d, w, f"{'up' if m >= 0 else 'down'} {abs(m) * 100:.1f}%"] for d, w, m in EVT],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: Wärtsilä month-end close, October 2023 to the 30 October 2026 close, against my base value (red). Nasdaq Nordic "
          "price history, retrieved 2 November 2026. Right: moves from the previous close to the close on the day; Wärtsilä "
          "publishes before the market opens."))
A('</div>')

A(section("Valuation, with the working"))
A(para("I value Wärtsilä as two businesses, each at a multiple of my 2027 comparable operating result, the year that will be the "
       "latest full year by October 2027. So I set the multiples against peers' trailing EV to EBIT. I add net cash of "
       f"continuing operations at 30 September, €{NET_CASH / 1000:.2f}bn, deduct minorities at book, value the half of Valo, the "
       f"loss-making battery joint venture, at nil, and divide by {SHARES:,.1f}m shares."))
A(para(f"My 2026 estimates add my fourth quarter to the nine months reported: Energy €{Q4_REV['EN']}m at {pct(Q4_M['EN'])}, "
       f"a little above the €692m of the order book due this year, as in 2025, and Marine €{Q4_REV['MA']}m at {pct(Q4_M['MA'])}. For 2027, Energy grows "
       f"{G27['EN'] * 100:.0f}% at {pct(M27['EN'])} and Marine {G27['MA'] * 100:.0f}% at {pct(M27['MA'])}. All are my estimates, "
       "on today's accounting. IFRS 18 from 2027 moves joint venture results out of the operating result; it changes the label, "
       "not the cash."))
A('<div class="keeptogether">')
A(section("Sum of the parts, base case"))
rowsS = [[n, f"{PROF[k] * 1000:,.0f}", f"{MULT[k]}x", f"{SOTP[k]:.2f}", f"{SOTP[k] / EQUITY * 100:.0f}%", eur(SOTP[k] / SHARES * 1000)]
         for n, k in [("Energy", "EN"), ("Marine", "MA")]]
rowsS.append(["Net cash, less minorities; Valo at nil", "", "", f"{BRIDGE:.2f}", f"{BRIDGE / EQUITY * 100:.0f}%", eur(BRIDGE / SHARES * 1000)])
rowsS.append(["Equity value", "", "", f"{EQUITY:.2f}", "100%", eur(BASE_VALUE)])
A(cols(datatable(["Part", "2027E comparable operating result, €m*", "Multiple", "Value, €bn", "Share", "Per share"], rowsS,
                 num_cols={1, 2, 3, 4, 5}, total_row_idx=len(rowsS) - 1), [36, 18, 10, 12, 10, 14]))
A(caption("*My estimates. Energy at 18x against engine peers' median of 20.7x trailing EV/EBIT (Caterpillar 21.8x, Cummins 18.7x, "
          "Rolls-Royce 20.7x) and Siemens Energy at 26.4x; lower than them because its growth rests on one market cycle in data "
          "centres. Marine at 14x, below Alfa Laval (20.1x), because new marine equipment is cyclical."))
A('</div>')
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "Energy 2027 result", "Energy x", "Marine x", "Value", "Change"],
    [
        ["Bear", "Data centre orders stall; Energy grows 8% at 15.5%; Marine flat at 12%", f"€{PEN[0] * 1000:,.0f}m", f"{SCEN[0][2][2]}x", f"{SCEN[0][1][2]}x", eur(bear), chg(bear)],
        ["Base", "Energy 22% at 17.5%; Marine 5% at 13%", f"€{PEN[1] * 1000:,.0f}m", f"{SCEN[1][2][2]}x", f"{SCEN[1][1][2]}x", eur(base), chg(base)],
        ["Bull", "Energy 30% at 18.5%; Marine 7% at 13.5%", f"€{PEN[2] * 1000:,.0f}m", f"{SCEN[2][2][2]}x", f"{SCEN[2][1][2]}x", eur(bull), chg(bull)],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {eur(WEIGHTED)}", chg(WEIGHTED)],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 41, 13, 9, 9, 10, 9]))
A(caption("Both businesses grow from my 2026 estimates. Net cash and the share count are the same in every case. The bear multiples "
          "sit below every peer; the bull Energy multiple is still below Siemens Energy (26.4x)."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: Marine multiple against the Energy multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Marine \\ Energy"] + [f"{m}x" for m in SENS_EN_X],
    [[f"{a}x"] + [(f"<b>{eur(v)}</b>" if (i == 1 and j == 1) else eur(v)) for j, v in enumerate(row)]
     for i, (a, row) in enumerate(zip(SENS_MA_X, SENS))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for row in SENS for v in row)
n_15 = sum(v >= PRICE * 1.15 for row in SENS for v in row)
A(para(f"With my 2027 results and net cash at base, {n_above} of the nine cells sit above the price and {n_15} sit 15% or more "
       f"above it. Only the corner with both multiples low, 11 times Marine and 13 times Energy, falls below it, at "
       f"{eur(SENS[0][0])}. Under my rule a long needs the base value 15% or more above the price. At "
       f"{(BASE_VALUE / PRICE - 1) * 100:.0f}% above, " + ("my draft view" if CALL["draft"] else "my call") + " is long, by a "
       "narrow margin."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBIT", "What they make"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w, g in PEERS],
    num_cols={2, 3},
), [18, 14, 12, 10, 46]))
A(caption("Forward P/E and trailing EV/EBIT from stockanalysis.com (S&amp;P Global data), retrieved 2 November 2026. Engine maker "
          "median (Caterpillar, Cummins, Rolls-Royce): 20.8x forward P/E, 20.7x EV/EBIT. GE Vernova's trailing 58.9x reflects "
          "earnings still recovering and is not used. Multiples set the ranges only; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["3 November 2026 (confirmed)", "Capital Markets Day, Helsinki; site visit to Vaasa on 4 November", "The path to the new targets; capacity after 2029; data centre pipeline"],
        ["5 February 2027 (confirmed)", "FY2026 results; the new guidance practice, net sales for Marine and Energy, starts in 2027", "Energy sales guidance against my 22% for 2027"],
        ["March 2027 (company)", "2026 figures restated for IFRS 18", "The new base for the operating result"],
        ["27 April 2027 (confirmed)", "Q1 2027 results", "Energy orders against net sales; named data centre MW"],
        ["Q1 2028 (company)", "35% more engine output at Vaasa", "Whether lead times stop lengthening"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Data centre orders stall.</strong> Named data centre orders were 62% of Energy's megawatts in the second quarter "
       "and 25% in the third. Wärtsilä calls the pipeline \"dynamic\" and warns that public opposition "
       "and regulation \"may slow the development of data centres\"."))
A(para("<strong>Rivals add capacity.</strong> Wärtsilä now names price pressure from new gas engine and turbine capacity, "
       "which may cut pricing before its own capacity arrives."))
A(para("<strong>The marine cycle turns.</strong> Marine made 55% of the 2025 comparable result. Newbuild contracting is high, "
       "helped by longer routes around the Strait of Hormuz. A settlement there, or lower freight rates, would cut equipment orders."))
A(para(f"<strong>The cash is partly customers' money.</strong> Advances were €{ADVANCES / 1000:.2f}bn at 30 September, "
       f"more than €{NET_CASH / 1000:.2f}bn of net cash; if orders slow, they unwind."))
A(para("<strong>Currency, tariffs and claims.</strong> Most Energy equipment orders come from the Americas and Wärtsilä reports in euros, "
       "so a weaker dollar cuts reported growth; US tariffs may hit its US energy business. Wärtsilä also notes one \"unusually "
       "sizeable claim\" against it."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into no call:</strong> a price above about {eur(REVISIT_LONG)}, where my base value would sit less than 15% above "
       "it on unchanged estimates, or a Capital Markets Day path that puts Energy's growth well below high-teens. "
       "<strong>Towards a short:</strong> Energy's orders falling below its sales for a year, or an Energy margin that falls as "
       "the order book converts."))
A(para(f"<strong>The view is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para(f"The fast lane is queued too, and Wärtsilä's own figures say so: engine lead times still rising, Energy orders {EN_BTB_9M:.2f} times sales, "
       f"and about {DC_SHARE_9M26 * 100:.0f}% of the megawatts named data centre orders. Nothing I found says the piece was "
       f"wrong. At {eur(PRICE)} the market pays about {EN_IMPLIED_X:.1f} times for Energy if Marine gets 14 times. "
       f"{my_call}: {CALL['direction']}, {conv} conviction, target {eur(tgt)}; base value {eur(BASE_VALUE)}, range {eur(bear)} "
       f"to {eur(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "Basis"],
    [
        ["Energy net sales growth", f"{EN_GROWTH26 * 100:.0f}%", f"{G27['EN'] * 100:.0f}%", "Target high-teens organic; book €5.6bn, €692m due in 2026"],
        ["Energy margin", pct(M26["EN"]), pct(M27["EN"]), "Target 18%; 9M 2026 16.0%, Q3 17.5%"],
        ["Marine growth and margin", f"{(REV26['MA'] / REV25['MA'] - 1) * 100:.0f}%, {pct(M26['MA'])}", f"{G27['MA'] * 100:.0f}%, {pct(M27['MA'])}", "Target mid-single-digit, 14%"],
        ["Net cash, €bn", f"{NET_CASH / 1000:.2f}", "", "Cash €2,469m less debt and leases €548m, 30 Sep 2026"],
        ["Tax rate, 2027", "", f"{TAX27 * 100:.0f}%", "9M 2026: 24.2%"],
    ],
), [26, 15, 15, 44]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Wärtsilä: Interim Report January to September 2026 and Q3 result presentation (27 October 2026), for '
  'segment figures, megawatts, order books, 2026 deliveries, balance sheet, shares, risks and quotes; inside information release '
  'of 27 October 2026 (mid-term targets, guidance practice); Half-year Financial Report (21 July 2026), for the 1.2 GW of data '
  'centre orders, the order book gross margin and the 2.2 times expansion; Interim Report January to March 2026 (28 April 2026), '
  'for the 429 MW order and the 35% expansion; Financial Statements Bulletin 2025 (4 February 2026), for 2024 and 2025 segment '
  'figures and the 789 MW; release of 5 October 2026 (2027 calendar). Share prices from Nasdaq Nordic; consensus (S&amp;P Global '
  'data) and peer multiples from stockanalysis.com; retrieved 2 November 2026. Estimates are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the model independently, not for any bank or broker. '
  'It tests a claim from my journal piece of 22 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/building-your-own-power/">thephysicallayer.fyi/journal/building-your-own-power</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'The forecasts and view are my own. I hold no position in Wärtsilä. Personal research, not investment advice.</p>')
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
