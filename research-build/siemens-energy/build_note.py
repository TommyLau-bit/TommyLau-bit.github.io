# -*- coding: utf-8 -*-
"""Siemens Energy AG (Xetra: ENR) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/siemens-energy.md.
"""
import datetime
from decimal import Decimal, ROUND_HALF_UP
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Siemens Energy AG (Xetra: ENR)"
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


def eur(x, d=0):
    return f"€{r(x, d):,.{d}f}"


def bn(x, d=1):
    return f"{r(x, d):,.{d}f}"


def neg(s, v):
    return f"({s.replace('-', '')})" if v < 0 else s


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
dirw = CALL["direction"].lower() if CALL["direction"] != "NO CALL" else "no call"
P26B = {k: v / 1000 for k, v in P26.items()}
EVT = [(d, w, b / a - 1) for d, w, a, b in EVENTS]

A('<h1 class="doctitle">Siemens Energy AG</h1>')
A('<p class="docsubtitle"><b>Xetra: ENR | Grid equipment, gas turbines and service, wind turbines, industrial compressors | Frankfurt</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{eur(PRICE, 2)} (Xetra close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{eur(PRICE, 2)}, Xetra close {PRICE_DATE}; record close {eur(HI_CLOSE, 2)} and intraday high {eur(HI_INTRA, 2)}, both 24 Apr 2026; lowest close of 2026 {eur(LO_CLOSE_26, 2)} (23 Oct)"),
    ("Market value", f"About €{MCAP:.1f}bn on {SHARES:,.1f}m shares outstanding (derived: issued shares less treasury shares, after buybacks to 27 Oct)"),
    ("Balance sheet, 30 Jun 2026", f"Adjusted net cash €{ADJ_NET_CASH:.1f}bn; customer advances and other contract liabilities €{CONTRACT_LIAB:.1f}bn"),
    ("FY2026 outlook (confirmed 30 Sep 2026)", "Comparable revenue growth 14 to 16%; margin before special items 10 to 12%, towards the upper end; net income about €4bn"),
    ("Grid Technologies", f"Backlog €{GT_BL[-1]}bn at 30 Jun 2026; orders {GT_9M_BTB:.2f} times revenue in the nine months; Q3 margin {pct(GT_Q3_M)}"),
    ("Grid in my value", f"{GT_SHARE_EQ * 100:.0f}% of my sum of the parts; Gas Services {GS_SHARE_EQ * 100:.0f}%"),
    ("Consensus (stockanalysis.com)", f"FY2027 EPS €{CONS_EPS27:.2f}; average target {eur(CONS_TP, 2)} ({CONS_N} analysts)"),
    ("Next event", "Q4 and FY2026 results, FY2027 outlook and FY2030 targets, 11 November 2026 (confirmed by Siemens Energy)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Siemens Energy\'s grid order book keeps growing faster than its factories can empty it. At €128.58, the market pays little for that.</p>')
A(para("Siemens Energy makes power transformers, switchgear and HVDC links in Grid Technologies, gas turbines and their service in Gas "
       "Services, compressors in Transformation of Industry, and wind turbines in Siemens Gamesa. My piece of 28 October argued that "
       "by its own estimate the transformer shortage in Europe and North America narrows to 2030 but never closes, so Grid's pile "
       "of waiting orders keeps growing."))
A(para(f"The claim holds. Grid took orders at {GT_9M_BTB:.2f} times its revenue in the nine months to June, and its backlog rose to "
       f"€{GT_BL[-1]}bn. The shares have fallen {abs(OFF_HIGH) * 100:.0f}% from their April record on doubts about AI spending. "
       f"On my numbers the price values Grid at about {GT_IMPLIED_X:.0f} times my fiscal 2027 estimate of its profit before special "
       f"items, if the rest of the group is valued at my base multiples."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction, 12-month target {eur(tgt)}.</b> My base sum of the parts is worth "
       f"{eur(BASE_VALUE)}, {chg(BASE_VALUE)}, inside a range of {eur(bear)} ({chg(bear)}) to {eur(bull)} ({chg(bull)}). The target "
       f"is my probability-weighted value, rounded, {chg(tgt)}. Siemens "
       "Gamesa is valued at close to nothing after the cash it still has to burn."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (fiscal years to September; profit before special items is Siemens Energy's measure)"))
A(datatable(
    ["€bn unless stated", "FY2024A", "FY2025A", "9M FY2026A", "FY2026E*", "FY2027E*", "FY2028 target"],
    [
        ["Grid revenue", f"{GT_REV_HIST[2]:.1f}", f"{REV25['GT'] / 1000:.1f}", f"{REV9M['GT'] / 1000:.1f}", f"{REV26['GT'] / 1000:.1f}", f"{REV27['GT'] / 1000:.1f}", "high-teens CAGR"],
        ["Grid margin before SI (%)", f"{GT_M_HIST[2] * 100:.1f}", f"{M25['GT'] * 100:.1f}", f"{P9M['GT'] / REV9M['GT'] * 100:.1f}", f"{M26['GT'] * 100:.1f}", f"{M27['GT'] * 100:.1f}", "18 to 20"],
        ["Grid orders / revenue (x)", f"{GT_BTB_FY24:.2f}", f"{GT_BTB_FY25:.2f}", f"{GT_9M_BTB:.2f}", "", "", ""],
        ["Gas Services revenue", "", f"{REV25['GS'] / 1000:.1f}", f"{REV9M['GS'] / 1000:.1f}", f"{REV26['GS'] / 1000:.1f}", f"{REV27['GS'] / 1000:.1f}", "mid-teens CAGR"],
        ["Gas Services margin before SI (%)", "", f"{M25['GS'] * 100:.1f}", f"{P9M['GS'] / REV9M['GS'] * 100:.1f}", f"{M26['GS'] * 100:.1f}", f"{M27['GS'] * 100:.1f}", "18 to 20"],
        ["Siemens Gamesa margin before SI (%)", "", neg(f"{M25['SG'] * 100:.1f}", M25['SG']), neg(f"{P9M['SG'] / REV9M['SG'] * 100:.1f}", -1), neg(f"{M26['SG'] * 100:.1f}", M26['SG']), f"{M27['SG'] * 100:.1f}", "3 to 5"],
        ["Group revenue", "", f"{GROUP_REV25 / 1000:.1f}", f"{GROUP_REV9M / 1000:.1f}", f"{GROUP_REV26 / 1000:.1f}", f"{GROUP_REV27 / 1000:.1f}", "low-teens CAGR"],
        ["Group profit before SI", "", bn(GROUP_PBSI25 / 1000, 2), bn(GROUP_PBSI9M / 1000, 2), bn(GROUP_PBSI26 / 1000, 2), bn(GROUP_PBSI27 / 1000, 2), "margin 14 to 16%"],
        ["EV / group profit before SI at €128.58 (x)", "", "", "", f"{EV_PBSI26:.1f}", f"{EV_PBSI27:.1f}", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*FY2026E and FY2027E are my own estimates, not Siemens Energy's; FY2026 results are due on 11 November 2026. Actuals from the "
          "shareholder letters of 13 November 2024 and 14 November 2025 and the Q3 FY2026 release of 5 August 2026. FY2028 targets from "
          "the Capital Market Day of 20 November 2025 (revenue growth is a compound rate from FY2025, comparable basis). EV is market value "
          "less adjusted net cash and equity-method investments at book, plus minorities at 15 times their earnings."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: Grid's earnings path, and a valuation that sits above the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: Grid Technologies revenue and margin before special items; FY26E and FY27E are mine; the shaded band is the FY2028 target "
          "of 18 to 20%. Right: value per share from the base case, the weighted cases, the sensitivity grid and the bear to bull range, "
          f"against the {eur(PRICE, 2)} price (red) and the average analyst target."))
A('</div>')

A(section("The thesis: a bath that keeps filling, inside a group with four taps"))
A(para("Picture the bath from the piece. The tap runs harder than the plughole can drain, so the water rises. The industry is widening "
       "the plughole, nearly doubling it on Siemens Energy's chart, but demand keeps turning the tap up. By 2030 the tap runs only a little "
       "faster than the drain, so the water rises more slowly. It still never falls."))
A(para("For an investor the water level is visibility. Each litre in the bath is revenue already sold, and new orders arrive at today's "
       "prices while the old, cheaper ones drain out. That is why Grid's margin has risen every year, from 3.6% in fiscal 2022 to "
       f"15.8% in fiscal 2025 and {pct(GT_Q3_M)} in the June quarter. Siemens Energy credits the \"improved margin profile of the "
       "processed order backlog\"."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_queue.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_sotp.png"></div></div>')
A(caption("Left: Grid Technologies orders and revenue by quarter, €bn; red figures are orders over revenue. Sources: earnings releases "
          "of 11 February, 12 May and 5 August 2026 (with prior-year quarters) and the Q4 FY2025 shareholder letter. Right: my sum of the "
          "parts per share, built up part by part, against the price (red) and the base value (dotted)."))
A('</div>')
A(para(f"<b>The claim holds on every test it set.</b> Grid's orders were {GT_BTB_FY24:.2f} times its revenue in fiscal 2024, "
       f"{GT_BTB_FY25:.2f} times in fiscal 2025 and {GT_9M_BTB:.2f} times in the nine months to June 2026. Its backlog rose from "
       f"€33bn in September 2024 to €42bn a year later, then €45bn, €49bn and €{GT_BL[-1]}bn in the three quarters since. Even if Grid "
       f"booked nothing in the September quarter, its fiscal 2026 orders of €{GT_9M_ORD / 1000:.1f}bn to June already exceed my "
       f"estimate of the full year's revenue, €{REV26['GT'] / 1000:.1f}bn. In the transcript it published of its pre-close call on 30 September, Siemens Energy "
       "said Grid booked no HVDC project in that quarter, so orders stayed \"similar to previous quarters\". Nothing I found shows "
       "the piece was wrong."))
A(para("The piece's caveat still stands. Grid's backlog is global and includes long HVDC projects, while the chart covers transformers "
       "in Europe and North America. The pre-close call supports the link: order momentum is \"led by the product business, "
       "particularly large power transformers\", with Europe and North America the strongest regions."))
A(para("The investment case needs one more step. Grid is about half of what I think Siemens Energy is worth. Gas Services, which "
       "makes and services gas turbines, is about two fifths. Siemens Gamesa, the wind business, made its first quarterly profit since 2022 only in the June quarter. "
       "So the question is what the price says about each part."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {eur(PRICE, 2)} Siemens Energy is worth about €{MCAP:.1f}bn on {SHARES:,.1f}m shares, my count after the buybacks. "
       f"Adjusted net cash, less the buybacks paid since June, plus equity-method investments at book, less minorities at 15 times "
       f"their earnings, add about €{BRIDGE:.1f}bn. The enterprise value is about €{EV_ADJ:.1f}bn: {EV_PBSI26:.1f} times my fiscal "
       f"2026 estimate of profit before special items and {EV_PBSI27:.1f} times my fiscal 2027 estimate. The shares trade at "
       f"{PE_C27:.1f} times the €{CONS_EPS27:.2f} fiscal 2027 consensus EPS on stockanalysis.com."))
A(para(f"<strong class='lead'>What the price implies.</strong> With Gas Services at 18 times, Transformation of Industry at 14 times, "
       f"Siemens Gamesa at close to nothing and corporate costs capitalised, the price leaves about €{GT_IMPLIED_EV:.0f}bn for Grid. "
       f"That is {GT_IMPLIED_X:.1f} times my fiscal 2027 estimate of its profit before special items. Grid equipment peers trade at a "
       f"median of 20.8 times trailing EV to EBIT. Put the other way, with Grid at 22 times the price leaves Gas Services at "
       f"{GS_IMPLIED_X:.1f} times. The market is not paying for both engines at once."))
A(para("The shares fell 31% from the April record, and 8.6% on 22 October alone, when a Barclays sector study questioned the pricing "
       "power of AI equipment makers and doubts about AI spending hit the sector. Barclays has rated the shares underweight with a "
       f"€130 target since July. The average target of {CONS_N} analysts is {eur(CONS_TP, 2)}, "
       "but most predate the fall. I differ on three points."))
A(para("<strong class='lead'>Grid's pile is not an AI bet.</strong> At its 30 September pre-close call, Siemens Energy said data centres are \"additive\" for Grid but "
       "\"not its foundation\": regulated grid investment, the replacement of 30 to 40 year old assets and interconnection are. Its own "
       "chart counts a transformer shortage in Europe and North America through 2030. A slowdown in AI spending would slow the pile's "
       "growth; on the chart, it would not drain it."))
A(para(f"<strong class='lead'>I do not need consensus to be right.</strong> My fiscal 2027 estimates give EPS of about €{EPS27:.2f}, "
       f"below the €{CONS_EPS27:.2f} consensus. They assume Grid grows 18% at a 20% margin, the top of its fiscal 2028 range a year "
       "early, and Gas Services 17% at 18%. On those numbers the base value is still 27% above the price."))
A(para("<strong class='lead'>The wind business is priced as a drag, and I price it the same.</strong> Siemens Gamesa burned €1.7bn "
       "of free cash flow before tax in the nine months to June. I value its fiscal 2027 profit at 10 times and deduct €1.5bn of cash "
       f"still to burn, which leaves about €{SOTP['SG']:.1f}bn. The base case does not need the turnaround."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [[d, w, "unchanged" if abs(m) < 0.0005 else f"{'up' if m >= 0 else 'down'} {abs(m) * 100:.1f}%"] for d, w, m in EVT],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: Siemens Energy month-end close, October 2023 to the 27 October 2026 close, against my base value (red). Yahoo Finance, "
          "retrieved 28 October 2026. Right: moves from the previous close to the close on the day; Siemens Energy releases results "
          "before the market opens. The 22 October move as reported by German financial press."))
A('</div>')

A(section("Valuation, with the working"))
A(para("I value Siemens Energy as a sum of its parts. Each business is valued at a multiple of my fiscal 2027 profit before special "
       "items, the year to September 2027, which will be the latest full year by October 2027. So I set the multiples against peers' "
       "trailing EV to EBIT. Siemens Gamesa is valued separately as a drag. I add adjusted net cash at 30 June less buybacks since and "
       f"equity-method investments at book, deduct minorities at 15 times their earnings, and divide by {SHARES:,.1f}m shares."))
A(para(f"My fiscal 2026 estimates add my September quarter to the nine months reported, inside segment revenue guidance on a comparable basis: Grid €{REV26['GT'] / 1000:.1f}bn "
       f"of revenue at {pct(M26['GT'])}, Gas Services €{REV26['GS'] / 1000:.1f}bn at {pct(M26['GS'])}, Siemens Gamesa at break-even. "
       f"My Gas Services margin ({pct(M26['GS'])}) and group margin ({pct(GROUP_PBSI26 / GROUP_REV26)}) sit just above the top of the "
       "guided ranges, as the nine months' 16.6% and 12.6% already do. "
       f"For fiscal 2027, Grid grows 18% at 20%, Gas Services 17% at 18%, Transformation of Industry 6% at 13% and Siemens Gamesa 4% at "
       "2%. Corporate costs stay at €0.3bn. All are my estimates."))
A('<div class="keeptogether">')
A(section("Sum of the parts, base case"))
names = [("Grid Technologies", "GT"), ("Gas Services", "GS"), ("Transformation of Industry", "TI")]
rowsS = [[n, bn(PROF[k], 2), f"{MULT[k]}x", bn(SOTP[k]), f"{SOTP[k] / EQUITY * 100:.0f}%", eur(SOTP[k] / SHARES * 1000)] for n, k in names]
rowsS.append(["Siemens Gamesa: profit at 10x, less €1.5bn cash burn", bn(PROF["SG"], 2), f"{MULT['SG']}x", bn(SOTP["SG"]),
              f"{SOTP['SG'] / EQUITY * 100:.0f}%", eur(SOTP["SG"] / SHARES * 1000)])
rowsS.append(["Corporate costs", "(0.30)", f"{MULT['Corp']}x", neg(bn(SOTP["Corp"]), -1), neg(f"{SOTP['Corp'] / EQUITY * 100:.0f}%", -1),
              neg(eur(SOTP["Corp"] / SHARES * 1000), -1)])
rowsS.append(["Net cash, investments, less minorities", "", "", bn(BRIDGE), f"{BRIDGE / EQUITY * 100:.0f}%", eur(BRIDGE / SHARES * 1000)])
rowsS.append(["Equity value", "", "", bn(EQUITY), "100%", eur(BASE_VALUE)])
A(cols(datatable(["Part", "FY2027E profit before SI, €bn*", "Multiple", "Value, €bn", "Share", "Per share"], rowsS,
                 num_cols={1, 2, 3, 4, 5}, total_row_idx=len(rowsS) - 1), [38, 15, 10, 12, 10, 15]))
A(caption("*My estimates; brackets are negative. Grid at 22x against a grid equipment median of 20.8x trailing EV/EBIT (22.4x without "
          "Hitachi), for faster growth and a higher margin. Gas Services at 18x, below Mitsubishi Heavy (21.5x) and Baker Hughes (20.9x), "
          "because its new-unit pricing is at a cycle high. Transformation of Industry at 14x. Siemens Gamesa at 10x against Vestas at "
          "15.5x, less €1.5bn of cash I expect it to burn before it turns cash positive. Corporate costs capitalised at 15x."))
A('</div>')
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "Grid FY2027", "Grid x", "Gas x", "Gamesa", "Value", "Change"],
    [
        ["Bear", "Grid grows 12% at 18.5%; Gas 10% at 16%; Gamesa breaks even but burns €3bn", f"€{PGT[0]:.2f}bn", f"{SCEN[0][1][2]}x", f"{SCEN[0][2][2]}x", "minus €3.0bn", eur(bear), chg(bear)],
        ["Base", "Grid 18% at 20%; Gas 17% at 18%; Gamesa 2% margin", f"€{PGT[1]:.2f}bn", f"{SCEN[1][1][2]}x", f"{SCEN[1][2][2]}x", f"€{SOTP['SG']:.1f}bn", eur(base), chg(base)],
        ["Bull", "Grid 22% at 21%; Gas 20% at 19%; Gamesa 4% margin", f"€{PGT[2]:.2f}bn", f"{SCEN[2][1][2]}x", f"{SCEN[2][2][2]}x", "€4.2bn", eur(bull), chg(bull)],
        ["Weighted", "25 / 50 / 25", "", "", "", "", f"about {eur(WEIGHTED)}", chg(round(WEIGHTED))],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [9, 37, 11, 7, 7, 11, 9, 9]))
A(caption("Grid and Gas Services grow from my FY2026 estimates. Transformation of Industry keeps my FY2027E profit at 10x, 14x and 16x. "
          "Corporate costs, the bridge and the share count are the same in every case. The bear multiples sit below every grid and "
          "gas peer on trailing EV/EBIT; the bull Grid multiple is still below Eaton (31.1x)."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: Gas Services multiple against the Grid multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Gas \\ Grid"] + [f"{m}x" for m in SENS_GT_X],
    [[f"{a}x"] + [(f"<b>{eur(v)}</b>" if (i == 1 and j == 1) else eur(v)) for j, v in enumerate(row)]
     for i, (a, row) in enumerate(zip(SENS_GS_X, SENS))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for row in SENS for v in row)
n_15 = sum(v >= PRICE * 1.15 for row in SENS for v in row)
A(para(f"With my fiscal 2027 profits and everything else at base, {n_above} of the nine cells sit above the price and {n_15} sit 15% "
       f"or more above it. Only the corner with both multiples low, 13 times Gas and 16 times Grid, falls below it, at "
       f"{eur(SENS[0][0])}. Under my rule a long needs the base value 15% or more above the price. At "
       f"{(BASE_VALUE / PRICE - 1) * 100:.0f}% above, " + ("my draft view" if CALL["draft"] else "my call") + " is long."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBIT", "What they make"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w, g in PEERS],
    num_cols={2, 3},
), [18, 14, 11, 10, 47]))
A(caption("Forward P/E and trailing EV/EBIT from stockanalysis.com (S&amp;P Global data), retrieved 28 October 2026. Grid equipment median "
          "(ABB, Schneider Electric, Eaton, Prysmian, Hitachi): 22.2x forward P/E, 20.8x EV/EBIT. GE Vernova's trailing 84x reflects "
          "earnings still recovering and is not used. Multiples are used only to set the ranges; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["11 November 2026 (confirmed)", "Q4 and FY2026 results; FY2027 outlook, FY2030 targets, capital allocation to FY2030", "Grid orders against revenue for the year; the FY2027 Grid outlook against 18% growth and 20%; Gas backlog margin"],
        ["Early FY2027 (company guidance)", "Next HVDC order for Grid", "Whether the backlog keeps rising after a quarter without HVDC"],
        ["Through 31 March 2027", "Third buyback tranche of up to €2bn", "Share count"],
        ["11 February 2027 (confirmed)", "Q1 FY2027 results", "Grid backlog in euros; Siemens Gamesa cash flow"],
        ["2027", "Charlotte large power transformer plant ships", "Whether the US plant runs on time"],
        ["Around mid-2027", "Decision on separating Transformation of Industry", "Price and the minority stake kept"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The gas cycle turns.</strong> Gas Services is about two fifths of my value and its new-unit pricing is at a cycle high. "
       "Siemens Energy expects lower gas orders in the September quarter and says to judge them over a full year. If data centre "
       "projects stall, slot reservations may not convert. It says none have been delayed or cancelled so far."))
A(para("<strong>Grid's price rises stop.</strong> At the same call Siemens Energy said European grid pricing has \"stabilized at a high level\" and that "
       "further margin gains will come from execution and utilisation. My 20% Grid margin for fiscal 2027 needs that execution."))
A(para("<strong>Siemens Gamesa.</strong> Offshore orders for fiscal 2026 came in below plan and moved into fiscal 2027. It still booked "
       "€189m of negative special items in the nine months to June. My bear case has it burn €3bn more."))
A(para(f"<strong>The cash is partly customers' money.</strong> Contract liabilities, mostly customer advances, were €{CONTRACT_LIAB:.1f}bn at "
       "30 June. If orders slow, advances unwind and the €7.7bn of adjusted net cash would shrink."))
A(para("<strong>Currency and policy.</strong> Siemens Energy reports in euros and much of its order growth is in the US, so a weaker "
       "dollar cuts reported growth. A US executive order on bulk-power equipment is not yet detailed. Siemens AG held 5.54% of "
       "the voting rights after a sale, according to its notice of 2 April 2026 published via Deutsche Boerse."))
A(para("<strong>Capacity timing.</strong> The Charlotte plant slipped by a year to 2027 and Nuremberg's expansion runs to 2028. A slip "
       "delays revenue, though it also keeps the pile growing."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into no call:</strong> a price above about €{REVISIT_LONG:.1f}, where my base value would sit less than 15% above it, or a "
       "fiscal 2027 Grid outlook on 11 November below high-teens growth or below an 18% margin. <strong>Towards a short:</strong> Grid's orders "
       "falling below its revenue, or a turn in gas orders large enough to cut my fiscal 2027 Gas Services profit by a third."))
A(para(f"<strong>The view is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para(f"The October piece argued that Siemens Energy's own chart shows the transformer shortage narrowing but never closing, so Grid's "
       f"pile keeps growing. Its figures say so: orders at {GT_9M_BTB:.2f} times revenue in the nine months, a backlog of €{GT_BL[-1]}bn "
       "rising every quarter, and fiscal 2026 orders that already exceed the year's revenue. Nothing I found says the piece was wrong. "
       f"The market has de-rated the shares on doubts about AI spending, and at {eur(PRICE, 2)} it pays about {GT_IMPLIED_X:.0f} times "
       f"for Grid if Gas Services gets a below-peer multiple. {my_call}: {CALL['direction']}, {conv} conviction, target {eur(tgt)}; base "
       f"value {eur(BASE_VALUE)}, range {eur(bear)} to {eur(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY2026E", "FY2027E", "Basis"],
    [
        ["Grid revenue growth (nominal)", f"{GT_GROWTH26 * 100:.0f}%", f"{G27['GT'] * 100:.0f}%", "FY2026 guide 25 to 27% comparable; FY2028 target high-teens"],
        ["Grid margin before SI", pct(M26["GT"]), pct(M27["GT"]), "FY2026 guide 18 to 20%; Q3 19.9%"],
        ["Gas Services growth and margin", f"{(REV26['GS'] / REV25['GS'] - 1) * 100:.0f}%, {pct(M26['GS'])}", f"{G27['GS'] * 100:.0f}%, {pct(M27['GS'])}", "FY2028 target mid-teens growth, 18 to 20%"],
        ["Transformation of Industry", f"{(REV26['TI'] / REV25['TI'] - 1) * 100:.0f}%, {pct(M26['TI'])}", f"{G27['TI'] * 100:.0f}%, {pct(M27['TI'])}", "FY2028 target 12 to 14%"],
        ["Siemens Gamesa", "about flat, break-even", f"{G27['SG'] * 100:.0f}%, {pct(M27['SG'])}", "FY2028 target 3 to 5%; €1.5bn cash burn to come"],
        ["Bridge, €bn", f"{BRIDGE:.2f}", "", "Adjusted net cash 30 June less €1.26bn buybacks since; investments at book; minorities 15x"],
        ["Shares, m", f"{SHARES:,.1f}", "", "Issued 861.1m less treasury shares, derived from buyback reports"],
    ],
), [28, 15, 15, 42]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Siemens Energy, Earnings Release Q3 FY2026, 5 August 2026, for segment orders, revenue and profit before special '
  'items, the balance sheet, adjusted net cash and the FY2026 outlook. Earnings Releases Q1 FY2026 (11 February 2026) and Q2 FY2026 '
  '(12 May 2026) for quarterly Grid figures. Shareholder Letters Q4 FY2025 (14 November 2025) and Q4 FY2024 (13 November 2024) for '
  'full-year segment results, Grid backlog and the FY2028 targets. Capital Market Day presentations, 20 November 2025 (CEO, Grid '
  'Technologies, Gas Services, Siemens Gamesa, Transformation of Industry), for targets and Grid history. Half-year Financial Report '
  '2026, 12 May 2026, Note 4, for treasury shares. Siemens Energy share buyback page, read 28 October 2026. Q4 FY2026 Pre-Close Call '
  'transcript, 30 September 2026, and the investor relations financial calendar, for the 11 November 2026 results date and the remarks '
  'quoted. Siemens AG voting rights notice of 2 April 2026. Share prices from Yahoo Finance (ENR.DE); consensus EPS and average target '
  '(S&amp;P Global data) and peer multiples from stockanalysis.com; all retrieved 28 October 2026. The 22 October move as reported by '
  'boersennews.de. Estimates for FY2026 and FY2027 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 28 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/siemens-energy-measures-the-shortage/">thephysicallayer.fyi/journal/siemens-energy-measures-the-shortage</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Siemens Energy. Personal research, not investment advice.</p>')
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
