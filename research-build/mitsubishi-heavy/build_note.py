# -*- coding: utf-8 -*-
"""Mitsubishi Heavy Industries (TSE: 7011) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/mitsubishi-heavy.md.
"""
import datetime
from decimal import Decimal, ROUND_HALF_UP
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Mitsubishi Heavy Industries (TSE: 7011)"
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


def yen(x, d=0):
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"¥{q:,.{d}f}"


def bn(x, d=0):
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"{q:,.{d}f}"


def neg(s, v):
    return f"({s.replace('-', '')})" if v < 0 else s


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = yen(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {yen(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
dirw = CALL["direction"].lower() if CALL["direction"] == "NO CALL" else CALL["direction"]
G = GROUP

A('<h1 class="doctitle">Mitsubishi Heavy Industries</h1>')
A('<p class="docsubtitle"><b>TSE: 7011 | Gas turbines, nuclear, defence and space, aero engines, plants | Tokyo</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{yen(PRICE)} (TSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{yen(PRICE)}, TSE close {PRICE_DATE}, the lowest close since July 2025; record close {yen(HI_CLOSE)} (2 Mar 2026)"),
    ("Market value", f"About ¥{MCAP / 1000:.1f} trillion on {SHARES:,.0f}m shares outstanding, net of treasury shares (30 Jun 2026)"),
    ("Balance sheet, 30 Jun 2026", f"Cash ¥{CASH:,.0f}bn, interest-bearing debt ¥{DEBT:,.0f}bn; contract liabilities ¥{CL_JUN26:,.0f}bn, up ¥{ADV_BUILD:,.0f}bn since Mar 2025"),
    ("FY2026 forecast (4 Aug 2026)", f"Orders ¥{G['FY2026G'][0]:,.0f}bn; revenue ¥{G['FY2026G'][1]:,.0f}bn; business profit ¥{G['FY2026G'][2]:,.0f}bn (10.0%); EPS ¥{EPS26G:.2f}"),
    ("Gas turbines (GTCC)", f"FY2025 orders ¥{GT_ORD[3]:,.0f}bn, revenue ¥{GT_REV[3]:,.0f}bn; order book over ¥5tn; 80 large units on order (35 GW)"),
    ("Defense &amp; Space", f"FY2026 forecast orders ¥{DS_ORD['FY2026G']:,.0f}bn, revenue ¥{DS_REV['FY2026G']:,.0f}bn; Aircraft, Defense &amp; Space backlog ¥{BACKLOG_SEG['ADS']:,.0f}bn"),
    ("Consensus (stockanalysis.com)", f"FY2026 EPS ¥{CONS_EPS_26:.2f}; average target {yen(CONS_TP)} ({CONS_N} analysts)"),
    ("Next event", "1H FY2026 results, 6 November 2026, 13:30 JST (scheduled by MHI)"),
]))
A('</div><div class="maincol">')
A("<p class=\"lede\">Mitsubishi Heavy's turbines are booked to 2030, and its buyers have paid ahead. At ¥3,363 the shares sit "
  "close to what both businesses are worth.</p>")
A(para("Mitsubishi Heavy Industries (MHI) is one of three makers of the largest gas turbines. My piece of 22 September argued that "
       "a data centre which builds its own power swaps the grid's queue for the turbine makers'. MHI's figures confirm it: about "
       "five years of gas turbine revenue on order, new talks for delivery around 2030 to 2031, prices not falling, buyers paying ahead."))
A(para(f"But MHI also builds missiles, warships, military aircraft and rockets. On my estimates, gas turbine combined cycle (GTCC) is "
       f"{GT_SHARE_SOTP * 100:.0f}% of my value and Aircraft, Defense and Space {ADS_SHARE_SOTP * 100:.0f}%. At {yen(PRICE)}, after a "
       f"{abs(OFF_HIGH) * 100:.0f}% fall from the March record, the price pays about {GT_IMPLIED_MULT:.0f} times my fiscal 2027 GTCC "
       f"profit with the rest at my base multiples, or about {ADS_IMPLIED_MULT:.0f} times for defence with GTCC at {MULT['GT']} times."))
A(para(f"<b>{my_call}: {dirw}, {conv} conviction.</b> My base sum of the parts is worth {yen(BASE_VALUE)}, {chg(BASE_VALUE)}, "
       f"inside a range of {yen(bear)} ({chg(bear)}) to {yen(bull)} ({chg(bull)}). Most of MHI's net cash is customers' prepayments; "
       f"counting it all as surplus would give {yen(BASE_FULLCASH)}. I would revisit below about ¥3,200."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (fiscal years to March; business profit is MHI's operating measure)"))
A(datatable(
    ["¥bn", "FY2024A", "FY2025A", "FY2026 forecast", "FY2027E*"],
    [
        ["Order intake", bn(G["FY2024"][0]), bn(G["FY2025"][0]), bn(G["FY2026G"][0]), ""],
        ["Revenue", bn(G["FY2024"][1]), bn(G["FY2025"][1]), bn(G["FY2026G"][1]), ""],
        ["GTCC revenue", bn(GT_REV[2]), bn(GT_REV[3]), bn(GT_REV[4]), bn(GT_REV27)],
        ["Defense &amp; Space revenue", bn(DS_REV["FY2024"]), bn(DS_REV["FY2025"]), bn(DS_REV["FY2026G"]), ""],
        ["Business profit", bn(G["FY2024"][2]), bn(G["FY2025"][2]), bn(G["FY2026G"][2]), bn(BP27)],
        ["Business profit margin (%)", f"{G['FY2024'][2] / G['FY2024'][1] * 100:.1f}", f"{G['FY2025'][2] / G['FY2025'][1] * 100:.1f}", "10.0", ""],
        ["Net income", bn(G["FY2024"][3]), bn(G["FY2025"][3]), bn(G["FY2026G"][3]), bn(NI27)],
        ["EPS, ¥", "", f"{EPS25:.2f}", f"{EPS26G:.2f}", f"{EPS27:.2f}"],
        [f"P/E at {yen(PRICE)} (x)", "", f"{PRICE / EPS25:.1f}", f"{PE_G26:.1f}", f"{PE_27:.1f}"],
    ],
    num_cols={1, 2, 3, 4},
))
A(caption("*FY2027E is my own estimate, not MHI's; FY2027E net income keeps the ratio of net income to business profit in MHI's FY2026 "
          "forecast. FY2024 and FY2025 exclude Mitsubishi Logisnext, deconsolidated on 1 May 2026. Sources: FY2025 results (12 May 2026), "
          "Q1 FY2026 results with the revised FY2026 forecast (4 August 2026)."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: the gas turbine queue in yen, and a valuation that sits a little above the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: GTCC order intake against revenue, FY2022 to the FY2026 forecast (MHI, FY2025 presentation p6; FY2026 as revised 4 August "
          f"2026). Right: value per share from the base case, the base with all net cash counted, the weighted cases, the sensitivity grid "
          f"and the bear to bull range, against the {yen(PRICE)} price (red) and the average analyst target."))
A('</div>')

A(section("The thesis: a drilling firm booked for years, inside a defence contractor"))
A(para("Think of the well from the piece. The council's water main is years away, so everyone on the street decides to sink a well, "
       "and the big drilling firm is booked for years. A buyer of that firm gets two things. Its revenue for the next few years is "
       "close to certain, because the diary is full. And each new booking is priced higher, because the diary is full."))
A(para(f"MHI's GTCC business is that drilling firm. GTCC pairs a gas turbine with a steam turbine that runs on its waste heat. In "
       f"fiscal 2025, the year to March 2026, GTCC took ¥{GT_ORD[3]:,.0f}bn of orders against ¥{GT_REV[3]:,.0f}bn of revenue, "
       f"{GT_BTB25:.1f} times. Its order book passed ¥5 trillion in March, about {GT_BL_YEARS:.0f} years of that revenue. In the June "
       f"quarter orders were ¥{GT_Q1_ORD[1]:,.0f}bn against ¥{GT_Q1_REV[1]:,.0f}bn of revenue, {GT_BTB_Q1:.1f} times. In units, MHI had "
       f"48 large turbines (above 100 MW) on order in March 2025 and {UNIT_BL[-1]}, about 35 GW, in June 2026. It booked 35 in fiscal "
       "2025 and ten in the June quarter, four for the United States."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_queue.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_sotp.png"></div></div>')
A(caption("Left: large frame gas turbines on order at period end, units; white figures are gigawatts where MHI states them. Sources: "
          "results presentations, 7 November 2025 to 4 August 2026. Right: my sum of the parts per share, built up part by part, "
          "against the price (red) and the base value (dotted)."))
A('</div>')
A(para("The claim is about the length of the queue, and the finance chief, Hiroshi Nishio, gave it. According to MHI's summary of the "
       "briefing dated 6 August, projects now under discussion \"will generally be delivered around 2030 to 2031\", and orders booked "
       "in the June quarter are due mostly between 2028 and 2030. \"Order pricing has not declined\", he said, and the margin on new "
       "orders keeps improving. Buyers pay to stand in line: MHI doubled its fiscal 2026 free cash flow forecast to ¥600bn mainly "
       "because \"advances received in GTCC have increased more than expected\". Contract liabilities rose from ¥1,435bn in March "
       "2025 to ¥2,483bn in June 2026. In May Nishio said customers pay in advance \"to secure production slots\"."))
A(para("MHI is not building its way out of the queue either. The chief executive, Eisaku Ito, said on 27 May that MHI aims to ship "
       "30% or more units in fiscal 2028 than current capacity allows, and then about 50% more again, around twice the fiscal 2024 "
       "level. He gave no year for the second step, and the first comes mostly from more than 1,000 changes on the factory floor. In "
       "August Nishio said MHI books orders \"while carefully monitoring progress on the capacity expansion\"."))
A(para("<b>The claim holds at a second maker.</b> Lead times are not falling and new output is not clearing the backlog. I checked "
       "the piece's MHI sentences against MHI's Q&amp;A summaries and presentations, and they stand. MHI adds one caution: Ito said "
       "world orders for gas turbines used in power reached 96 GW in 2025, but MHI expects about 70 GW a year on average over the next "
       "five years, about 10 GW above its earlier view of 50 to 60 GW. Ito still expects MHI's own unit orders to grow. GE Vernova said in "
       "July it sees heavy-duty supply and demand very balanced for six years, so the makers do not disagree; but MHI says aloud that "
       "2025 may have been the peak for world orders."))
A(para(f"The money shows up in margin. Energy Systems, which holds GTCC, earned 13.0% in fiscal 2025, forecasts {ES_M26 * 100:.1f}% "
       f"for fiscal 2026 and made {ES_M_Q1 * 100:.1f}% in the June quarter, including about ¥25bn of one-off items. MHI does not "
       "report GTCC's profit. An analyst put it near 20% in August, and Nishio said it should keep rising as higher-margin orders "
       "reach revenue. I assume 20% for fiscal 2026."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {yen(PRICE)} MHI is worth about ¥{MCAP / 1000:.1f} trillion. The shares trade at {PE_G26:.1f} times MHI's fiscal 2026 EPS "
       f"forecast of ¥{EPS26G:.2f} and {PE_C26:.1f} times the ¥{CONS_EPS_26:.2f} consensus (stockanalysis.com, 2 November). The average "
       f"target of {CONS_N} analysts is {yen(CONS_TP)}."))
A(para(f"<strong class='lead'>Gas turbines first, defence second.</strong> On MHI's fiscal 2026 forecast GTCC is {GT_SHARE_REV26 * 100:.0f}% "
       f"of revenue and Defense and Space {DS_SHARE_REV26 * 100:.0f}%. On profit the order changes: at a 20% margin GTCC makes "
       f"¥{GT_BP26:.0f}bn, {GT_SHARE_BP26 * 100:.0f}% of the ¥540bn group forecast, against ¥170bn, {ADS_SHARE_BP26 * 100:.0f}%, for "
       f"Aircraft, Defense and Space. In my sum of the parts GTCC is {GT_SHARE_SOTP * 100:.0f}% of equity value and Aircraft, Defense "
       f"and Space {ADS_SHARE_SOTP * 100:.0f}%. Defence is large and steady: orders of about ¥1.9tn in fiscal 2024, ¥1.7tn in fiscal "
       "2025 and ¥1.5tn expected this year, and revenue rising from ¥828bn to a forecast ¥1,250bn. Aircraft, Defense and Space as a whole "
       "had ¥3.9tn on order in June."))
A(para(f"<strong class='lead'>What the price implies.</strong> With everything but GTCC at my base multiples, the price leaves about "
       f"¥{GT_IMPLIED_EV / 1000:.1f} trillion for GTCC, {GT_IMPLIED_MULT:.1f} times my fiscal 2027 estimate of its profit. With GTCC at "
       f"{MULT['GT']} times, it leaves Aircraft, Defense and Space at {ADS_IMPLIED_MULT:.1f} times, against a European defence median "
       "of 19.8 times trailing EV to EBIT. The market is not paying full peer multiples for both at once. That sounds like a long, and "
       "the analysts' targets say so. I differ on three points."))
A(para(f"<strong class='lead'>The cash is mostly the customers'.</strong> Net cash is ¥{NETCASH:,.0f}bn, but contract liabilities rose "
       f"¥{ADV_BUILD:,.0f}bn in fifteen months, and that money will be spent building the turbines it paid for. Nishio said in August "
       "it \"does not mean that it can immediately be treated as surplus funds\". My profit estimates already count the margin on those "
       f"orders, so I deduct the cost still to come on the rise, {ADV_COST_SHARE * 100:.0f}% of it, ¥{ADV_DEDUCT:,.0f}bn. Counting "
       f"all net cash as surplus would give {yen(BASE_FULLCASH)}, {chg(BASE_FULLCASH)}. This one choice decides whether the base clears "
       "my 15% bar for a long."))
A(para("<strong class='lead'>The queue caps the volume.</strong> Revenue is recognised as work progresses, and the factory sets the pace; "
       f"the 30% step lands in fiscal 2028. I take GTCC revenue up {GT_G27 * 100:.0f}% in fiscal 2027 at a {GT_M27 * 100:.0f}% margin."))
A(para("<strong class='lead'>MHI is choosing price over share.</strong> Ito said in May that in fiscal 2025 the makers that used the most "
       "capacity won the most share, and that MHI hopes to win back the top share as demand normalises. Its 16 GW of orders that year "
       "were roughly a sixth of the 96 GW ordered in calendar 2025, on my rough comparison of different years."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["7 Nov 2025", "1H FY2025 results", f"down {abs(H1_MOVE) * 100:.1f}%"],
        ["2 Mar 2026", f"Record close {yen(HI_CLOSE)}; intraday high {yen(HI_INTRA)}", ""],
        ["12 May 2026", "FY2025 results; FY2026 forecast of ¥540bn business profit", f"down {abs(FY_MOVE) * 100:.1f}%"],
        ["27 May 2026", "2024 medium-term plan progress briefing", f"down {abs(MTBP_MOVE) * 100:.1f}%"],
        ["4 Aug 2026", "Q1 results; GTCC and defence order forecasts raised", f"up {Q1_MOVE * 100:.1f}%"],
        ["2 Nov 2026", f"Close {yen(PRICE)}, down {abs(YTD) * 100:.0f}% in 2026", ""],
    ],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: MHI month-end close, November 2023 to the 2 November 2026 close, adjusted for the April 2024 split, against my base value "
          "(red). stockanalysis.com, retrieved 2 November 2026. Right: moves from the previous close to the close on each release day, "
          "as MHI releases during trading hours. I found no single company event behind the fall since March."))
A('</div>')

A(section("Valuation, with the working"))
A(para(f"I value MHI as a sum of its parts: each business at a multiple of my fiscal 2027 business profit, the year to March 2028, "
       "which the market will price as the year ahead by October 2027. I split Energy Systems into GTCC and the rest (nuclear, steam "
       "power, aero engines, compressors). I add cash and investments at book; deduct debt, minority interests, the pension liability "
       f"and the cost still to come on the prepayments; and divide by {SHARES:,.0f}m shares. GTCC grows {GT_G27 * 100:.0f}% at "
       f"{GT_M27 * 100:.0f}%; the rest of Energy Systems {ER_G27 * 100:.0f}% at {ER_M27 * 100:.1f}%; Aircraft, Defense and Space "
       f"{ADS_G27 * 100:.0f}% at {ADS_M27 * 100:.0f}%. All are my estimates."))
A('<div class="keeptogether">')
A(section("Sum of the parts, base case"))
names = [("GTCC (my split of Energy Systems)", "GT"), ("Aircraft, Defense &amp; Space", "ADS"), ("Energy Systems, rest", "ER"),
         ("Plants &amp; Infrastructure Systems", "PI"), ("Industrial Solutions", "IS"), ("Corporate costs", "Corp")]
rowsS = [[n, neg(bn(E27[k]), E27[k]), f"{MULT[k]}x", neg(bn(SOTP[k]), SOTP[k]), neg(f"{SOTP[k] / EQUITY * 100:.0f}%", SOTP[k]),
          neg(yen(SOTP[k] / SHARES * 1000), SOTP[k])] for n, k in names]
rowsS.append(["Net cash, investments, less minorities, pensions, prepayment cost", "", "", bn(ADJ), f"{ADJ / EQUITY * 100:.0f}%", yen(ADJ / SHARES * 1000)])
rowsS.append(["Equity value", "", "", bn(EQUITY), "100%", yen(BASE_VALUE)])
A(cols(datatable(["Part", "FY2027E profit, ¥bn*", "Multiple", "Value, ¥bn", "Share", "Per share"], rowsS,
                 num_cols={1, 2, 3, 4, 5}, total_row_idx=len(rowsS) - 1), [38, 14, 10, 13, 10, 15]))
A(caption("*My estimates; brackets are negative. Multiples are EV to FY2027E business profit, set against trailing EV/EBIT (peer table): "
          "GTCC 20x, between the 18x I used for Siemens Energy's Gas Services and Siemens Energy's 26.4x; defence 18x, below the "
          "European median of 19.8x; Kawasaki Heavy 16.5x and IHI 14.2x for the other parts. Bridge: net cash ¥1,164bn, equity-method "
          f"and other investments ¥{EQUITY_METHOD + OTHER_FA:,.0f}bn at book, less minorities ¥{NCI:.0f}bn, pensions ¥{PENSION:.0f}bn "
          f"and ¥{ADV_DEDUCT:,.0f}bn of cost on the prepayment build-up."))
A('</div>')
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "GTCC FY2027 profit", "GTCC multiple", "Others", "Value", "Change", "Weight"],
    [
        ["Bear", "World orders fall towards MHI's earlier 50 to 60 GW view; GTCC grows 8% at 19%", f"¥{GTE[0]:.0f}bn", f"{SCEN[0][3]}x", "3 turns lower", yen(bear), chg(bear), "25%"],
        ["Base", f"GTCC grows {GT_G27 * 100:.0f}% at {GT_M27 * 100:.0f}%", f"¥{GTE[1]:.0f}bn", f"{SCEN[1][3]}x", "as above", yen(base), chg(base), "50%"],
        ["Bull", "Capacity step lands early; GTCC grows 25% at 24%", f"¥{GTE[2]:.0f}bn", f"{SCEN[2][3]}x", "2 turns higher", yen(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {yen(round(WEIGHTED, -1))}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 5, 6, 7}, total_row_idx=3,
), [9, 33, 11, 9, 11, 10, 9, 8]))
A(caption("GTCC starts from MHI's FY2026 revenue forecast of ¥1,100bn. The rest of MHI keeps my FY2027E profit; only its multiples move. "
          "The bear GTCC multiple is below where the market already values it; the bull multiple is still below Siemens Energy's 26.4x "
          "trailing EV/EBIT."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: GTCC FY2027 business profit against its multiple"))
A('<div class="chartsrow"><div class="col left">')
grid = [[value(e, m) for m in SENS_MULT] for e in SENS_GT]
A(datatable(
    ["GTCC profit"] + [f"{m}x" for m in SENS_MULT],
    [[f"¥{e:.0f}bn"] + [(f"<b>{yen(v)}</b>" if (i == 1 and j == 1) else yen(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_GT, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
A(para(f"With the rest of MHI at my base, {n_above} of the nine cells sit above the price, but only {n_15} sit 15% or more above it, "
       "and all three need a multiple of 20x or more with GTCC profit at or above my base. A long needs GTCC at about "
       f"{GT_MULT_FOR_LONG:.1f}x with everything else unchanged. Under my rule a long needs the base value 15% or more above the price "
       f"and a short needs it 25% or more below. At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, {my_call.lower()} is no call."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBIT", "What they make"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w, g in PEERS],
    num_cols={2, 3},
), [18, 13, 11, 10, 48]))
A(caption("Forward P/E and trailing EV/EBIT from stockanalysis.com, retrieved 2 November 2026. European defence median (Rheinmetall, BAE "
          "Systems, Thales, Leonardo): 21.7x forward P/E, 19.8x EV/EBIT. GE Vernova's 58.9x reflects earnings still recovering and is not "
          "used to set a multiple. Multiples are used only to set the ranges; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["6 November 2026, 13:30 JST (scheduled)", "1H FY2026 results", "Large frame unit orders against 35 in FY2025; Energy Systems margin against 15.5%; contract liabilities"],
        ["Early February 2027 (not announced)", "Q3 FY2026 results", "GTCC order pace; the FY2026 forecast"],
        ["Around May 2027 (not announced)", "FY2026 results and the 2027 medium-term plan", "A date for doubling gas turbine output; capital allocation of the prepayment cash"],
        ["Through FY2026", "New defence production capacity", "Defense &amp; Space revenue moving towards ¥1.5tn a year of orders"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Orders past the peak.</strong> MHI expects world orders to fall from 96 GW in 2025 to about 70 GW a year over the next "
       "five years; until May it expected 50 to 60 GW. If orders fall faster than capacity rises, the queue shortens and the multiple falls. That is most of the bear case."))
A(para("<strong>Execution and one-offs.</strong> Fiscal 2025 carried about ¥30bn of losses on steam power projects, ¥20bn of it in "
       "South Africa, and a ¥30bn goodwill impairment. The June quarter was lifted by about ¥25bn of one-off items. Large fixed-price "
       "plants can swing a 15% margin quickly."))
A(para("<strong>Capacity.</strong> The doubling has no date. If the 2027 plan pushes it beyond 2030, the queue stays long but GTCC "
       "revenue grows more slowly than my base."))
A(para("<strong>Defence.</strong> Defence orders depend on Japan's budget. A change in plans, or delays to new defence production capacity, would "
       "slow the step up in revenue. Overseas work, such as the Australian frigate programme booked in fiscal 2025, carries terms MHI is "
       "less used to, as Ito said in May."))
A(para("<strong>The yen.</strong> MHI assumes ¥150 to the US dollar for fiscal 2026 and expects about US$3.2bn of dollar amounts to "
       "affect business profit; its revenue rate averaged ¥157.2 in the June quarter. A stronger yen cuts the yen value of the queue "
       "without changing the queue."))
A(para("<strong>The cash.</strong> If MHI treats the prepayments as surplus and returns them, my bridge is too cautious. Nishio said "
       "the 2027 plan will set out its approach to capital allocation."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price below about ¥{round(REVISIT_LONG, -2):,.0f}, where my base value would sit 15% above it on "
       "unchanged estimates, or a 2027 plan that dates the doubling of gas turbine output against fiscal 2024 to fiscal 2030 or earlier. "
       f"<strong>Towards a short:</strong> a price above about ¥{round(REVISIT_SHORT, -1):,.0f}, where my base value would sit 25% below it."))
A(para(f"<strong>The view is wrong if</strong> {WRONG_IF[0].lower() + WRONG_IF[1:]}"))
A('</div>')

A(section("Conclusion"))
A(para("The September piece argued that building your own power swaps the grid's queue for the turbine makers'. MHI's figures confirm "
       "it at a second maker: about five years of GTCC revenue on order, new talks for 2030 to 2031, prices not falling, and buyers "
       "paying ahead. I found nothing in MHI's disclosures that shows the piece wrong. But the queue that makes GTCC's revenue visible "
       f"also paces it, and much of MHI's cash belongs to the buyers in it. {my_call}: {dirw}, {conv} conviction; base value "
       f"{yen(BASE_VALUE)}, range {yen(bear)} to {yen(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY2026", "FY2027E", "Basis"],
    [
        ["GTCC revenue growth", f"{(GT_REV[4] / GT_REV[3] - 1) * 100:.0f}% (forecast)", f"{GT_G27 * 100:.0f}%", "Order book over ¥5tn; 30% capacity step by FY2028"],
        ["GTCC business profit margin", f"{GT_M26 * 100:.0f}% (mine)", f"{GT_M27 * 100:.0f}%", "Not disclosed; Energy Systems 15.5% forecast, 18.9% in Q1"],
        ["Energy Systems rest", f"{EREST_BP26 / EREST_REV26 * 100:.1f}% (derived)", f"{ER_G27 * 100:.0f}% at {ER_M27 * 100:.1f}%", "Nuclear revenue forecast ¥400bn"],
        ["Aircraft, Defense &amp; Space", "11.3% (forecast)", f"{ADS_G27 * 100:.0f}% at {ADS_M27 * 100:.0f}%", "Revenue rising towards about ¥1.5tn of yearly defence orders"],
        ["Plants, Industrial, corporate", "¥90bn, ¥30bn, (¥90bn)", f"¥{PI_BP27:.0f}bn, ¥{IS_BP27:.0f}bn, (¥{-CORP27:.0f}bn)", "Modest growth; corporate flat"],
        ["Prepayment cost deducted", "", f"¥{ADV_DEDUCT:,.0f}bn", f"{ADV_COST_SHARE * 100:.0f}% of the ¥{ADV_BUILD:,.0f}bn rise in contract liabilities since March 2025"],
        ["Shares, m", f"{SHARES:,.1f}", "", "Issued less treasury, 30 June 2026"],
    ],
), [26, 18, 18, 38]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Mitsubishi Heavy Industries, Q1 FY2026 Financial Results presentation and Consolidated Financial Results, 4 '
  'August 2026, for segment orders, revenue and business profit, GTCC, nuclear and defence figures, the revised FY2026 forecast, the '
  'balance sheet, shares, order backlog, large frame gas turbine units and currency assumptions. MHI, Q&amp;A Summary of the Q1 FY2026 '
  'Financial Results Briefing, dated 6 August 2026, for the remarks quoted from the finance chief. MHI, FY2025 Financial Results '
  'presentation, Consolidated Financial Results and Q&amp;A Summary, 12 May 2026, for FY2025 results, GTCC and Defense &amp; Space '
  'history, the gas turbine order book and remarks on share and advance payments. MHI, 2024 Medium-Term Business Plan Progress '
  'presentation and Q&amp;A Summary, 27 May 2026, for the capacity plan and demand outlook. MHI presentations and Q&amp;A summaries of 7 '
  'November 2025 and 4 February 2026 for unit history and earlier demand views. MHI investor relations page for the 6 November 2026 '
  'results date. GE Vernova second quarter 2026 earnings call, 22 July 2026. Share prices, consensus EPS and average target (S&amp;P '
  'Global data) and peer multiples from stockanalysis.com, retrieved 2 November 2026. Estimates for FY2027 and the GTCC profit split '
  'are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 22 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/building-your-own-power/">thephysicallayer.fyi/journal/building-your-own-power</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Mitsubishi Heavy Industries. Personal research, not investment advice.</p>')
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
