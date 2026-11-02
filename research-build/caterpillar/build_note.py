# -*- coding: utf-8 -*-
"""Caterpillar Inc. (NYSE: CAT) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/caterpillar.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Caterpillar Inc. (NYSE: CAT)"
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
    return f"US${x:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def m(x):
    return f"{x:,.0f}"


def pct(x, d=1):
    return f"{x * 100:.{d}f}"


bear, base, bull = (x["value"] for x in SC)
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({UP_BASE * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
s24 = {k: SEG[k]["2024A"] for k in SEG}; s25 = {k: SEG[k]["2025A"] for k in SEG}
pg_g26 = Y26["app"]["PG"] / APP["PG"]["2025A"] - 1

A('<h1 class="doctitle">Caterpillar Inc.</h1>')
A('<p class="docsubtitle"><b>NYSE: CAT | Construction and mining machines, engines, gas turbines (Solar Turbines) and locomotives | Irving, Texas</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{usd(PRICE, 2)} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{usd(PRICE, 2)}, NYSE close {PRICE_DATE}; record close {usd(HI_CLOSE, 2)} and intraday high {usd(HI_INTRA, 2)} on 30 Jun 2026"),
    ("Market value", f"US${MCAP:.1f}bn on {SHARES_OUT}m shares (10-Q cover, 30 Jun 2026); MP&amp;E net debt US${NET_DEBT_MPE / 1000:.1f}bn at 30 Sep 2026"),
    ("2026 outlook (29 Oct 2026)", "Sales up mid-to-high teens; adjusted operating margin near the bottom of the target range, excluding tariff refunds"),
    ("P/E", f"{PE_C26:.1f}x 2026 consensus; {PE_C27:.1f}x 2027 consensus (US${CONS_EPS27:.2f}); {PE_E28:.1f}x my 2028E"),
    ("Backlog", f"US$78.1bn at 30 Sep 2026, up 96% in a year; {BL_YEARS_SEP26:.2f} years of trailing sales"),
    ("Power Generation", f"Sales US$3.42bn in Q3 2026, up 30%; my 2026E US${Y26['app']['PG'] / 1000:.1f}bn, {PG_X_2024_26:.2f}x 2024"),
    ("Consensus (stockanalysis.com)", f"Average target {usd(CONS_TP)} ({CONS_N} analysts); forward P/E {FWD_PE_SA:.1f}x"),
    ("Next event", "Q4 2026 results, 2 February 2027 (Caterpillar's call schedule)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Caterpillar sells the quick machines that let a data centre make its own power, and they are booked into 2029. '
  'At US$623 the price pays a fair multiple for that business and a cyclical one for the rest.</p>')
A(para("My September piece argued that a campus building its own gas power swaps the grid's queue for the makers' queues, and that even "
       "the fast lane of engines and smaller turbines is queued. Caterpillar is the largest maker in that fast lane. Its backlog reached "
       f"US$78.1bn in September, and its chief executive says it is taking turbine orders into 2030."))
A(para(f"The claim holds. The question for the shares is how much of Caterpillar's value the boom now carries. On my estimates Power "
       f"Generation is {pct(Y26['pg_share'], 0)}% of 2026 segment profit and {pct(Y28['pg_share'], 0)}% of 2028. The shares have fallen "
       f"{abs(OFF_HIGH) * 100:.0f}% from their June record. At that record the price paid about {IMPLIED_PG_PE_PEAK:.0f} times my 2028 power "
       f"earnings, if the rest earns {REST_PE:.0f} times; today it pays about {IMPLIED_PG_PE:.0f} times."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction.</b> My sum of the parts gives {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, "
       f"inside a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} ({chg(bull)}). The base sits inside my no call band."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (calendar years; adjusted EPS as Caterpillar defines it)"))
pe = lambda d: d["pe_p"] / d["pe_s"]
A(datatable(
    ["US$ million unless stated", "2024A", "2025A", "2026E*", "2027E*", "2028E*"],
    [
        ["Power Generation sales", m(APP["PG"]["2024A"]), m(APP["PG"]["2025A"]), m(Y26["app"]["PG"]), m(Y27["app"]["PG"]), m(Y28["app"]["PG"])],
        ["Power &amp; Energy sales (incl. inter-segment)", m(s24["PE"][0]), m(s25["PE"][0]), m(Y26["pe_s"]), m(Y27["pe_s"]), m(Y28["pe_s"])],
        ["Power &amp; Energy margin (%)", pct(s24["PE"][1] / s24["PE"][0]), pct(s25["PE"][1] / s25["PE"][0]), pct(pe(Y26)), pct(pe(Y27)), pct(pe(Y28))],
        ["Construction Industries sales", m(s24["CI"][0]), m(s25["CI"][0]), m(Y26["ci_s"]), m(Y27["ci_s"]), m(Y28["ci_s"])],
        ["Construction Industries margin (%)", pct(s24["CI"][1] / s24["CI"][0]), pct(s25["CI"][1] / s25["CI"][0]), pct(Y26["ci_p"] / Y26["ci_s"]), pct(Y27["ci_p"] / Y27["ci_s"]), pct(Y28["ci_p"] / Y28["ci_s"])],
        ["Resource Industries sales", m(s24["RI"][0]), m(s25["RI"][0]), m(Y26["ri_s"]), m(Y27["ri_s"]), m(Y28["ri_s"])],
        ["Resource Industries margin (%)", pct(s24["RI"][1] / s24["RI"][0]), pct(s25["RI"][1] / s25["RI"][0]), pct(Y26["ri_p"] / Y26["ri_s"]), pct(Y27["ri_p"] / Y27["ri_s"]), pct(Y28["ri_p"] / Y28["ri_s"])],
        ["Power Generation share of segment profit (%)&dagger;", "", "", pct(Y26["pg_share"]), pct(Y27["pg_share"]), pct(Y28["pg_share"])],
        ["Adjusted EPS (US$)", f"{ADJ_EPS['2024A']:.2f}", f"{ADJ_EPS['2025A']:.2f}", f"{E26:.2f}", f"{E27:.2f}", f"{E28:.2f}"],
        ["Consensus EPS (US$)", "", "", f"{CONS_EPS26:.2f}", f"{CONS_EPS27:.2f}", ""],
        [f"P/E at {usd(PRICE, 2)} (x)", "", "", f"{PE_E26:.1f}", f"{PE_E27:.1f}", f"{PE_E28:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*2026E is Caterpillar's first nine months plus my fourth quarter; 2027E and 2028E are my estimates. 2024A and 2025A as recast for "
          "the move of Rail into Resource Industries (Form 8-K, 26 March 2026). &dagger;My estimate: Caterpillar does not report Power Generation "
          "profit, so I give it the Power &amp; Energy margin and its share of that segment's external sales. Consensus from stockanalysis.com, "
          "updated 30 October 2026."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: the fast lane's sales, and a value close to the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: Power Generation external sales, US$bn, and their share of Power &amp; Energy external sales; 2024A and 2025A per Caterpillar, "
          "2026E to 2028E mine. Dotted: the 2030 target of more than twice 2024 (Caterpillar, Q4 2025 slides). Right: value per share from the "
          "base case, the weighted cases, the sensitivity grid and the bear to bull range, against the price (grey)."))
A('</div>')

A(section("The thesis: the quick rig is booked too, and it is a quarter of the firm"))
A(para("The piece explained it with a street whose water main is too small. Every house decides to sink its own well. The big drilling "
       "firm is booked for years, so people turn to a smaller firm with a lighter rig. That diary fills too. Caterpillar is the lighter "
       "rig, but it is also the firm that sells the street its diggers, its lorries and its quarry machines. The rig is now booked years "
       "ahead; the diggers sell with the building cycle."))
A(para("The rig first. Caterpillar's Power &amp; Energy segment sells gas turbines up to 38 MW through Solar Turbines, large reciprocating "
       "engines and generator sets, to data centres, oil and gas fields and industry. Power Generation sales rose from US$7.76bn in 2024 to "
       f"US$10.28bn in 2025, and to US$9.34bn in the first nine months of 2026 alone. In the third quarter they were US$3.42bn, up 30%, "
       "and the release puts the rise down mainly to turbines, turbine services and large reciprocating engines, primarily for "
       "data centres. Retail sales of Power Generation equipment rose 75%."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_queue.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_split.png"></div></div>')
A(caption("Left: firm order backlog at period end, US$bn, split by whether Caterpillar expects to fill it within twelve months. Sources: "
          "Form 10-K 2024 and 2025, Form 10-Qs to June 2026; September 2026 from the Q3 slides, with the split from the CFO's 58% on the "
          "call (third-party transcript), so it is shaded paler. Right: the price at the June record and today, and my base value, split "
          f"into the rest of Caterpillar at {REST_PE:.0f} times my 2028E and what is left for Power Generation, with the multiple of my "
          "2028E Power Generation earnings that implies."))
A('</div>')
A(para(f"<b>The queue is real and getting longer.</b> Caterpillar's firm backlog was US$30.0bn at the end of 2024 and US$78.1bn at the end of "
       f"September 2026, about {BL_YEARS_SEP26:.1f} year of its sales over the previous four quarters against {BL_YEARS_DEC24:.2f} at the end "
       "of 2024. Every 10-K and 10-Q since, to June 2026, has put the largest increase in Power &amp; Energy, or before the 2026 recast its "
       "predecessor, Energy &amp; Transportation. The part not expected to ship within twelve months rose from "
       "US$8.0bn to US$29.2bn in June 2026. Customers pay ahead as well: customer advances rose from US$3.3bn to US$5.3bn in the nine months "
       "to September."))
A(para("At a Wells Fargo event on 10 September, in a transcript Caterpillar posted, the chief executive said the company was \"starting to "
       "take orders in 2029 and even our first order into 2030 on turbines\", and was \"pretty full for 2027 on large engines and turbines\". "
       "On the third quarter call, per a third-party transcript, he repeated that some large engine orders run \"as far out as 2029\" and "
       "turbine orders into 2030. Framework agreements with large customers also hold factory slots before they become firm orders, and in "
       "September he said Caterpillar has \"a line of sight past the backlog\"."))
A(para("<b>The piece's Caterpillar sentence is right.</b> Third quarter Power Generation sales were US$3,421m against US$2,634m, up 30%, and the "
       "release gives the reason the piece quotes. Caterpillar backs the claim's second half: the fast lane is queued into 2029 and 2030. "
       "On the same call, per the transcript, he said smaller generator sets have much shorter lead times, so the fast lane has a faster lane inside it."))
A(para("<b>The rig is a part of the firm, not all of it.</b> In 2025 Power &amp; Energy earned US$6.26bn of Caterpillar's US$14.05bn segment profit, "
       f"45%. Power Generation was 43% of that segment's external sales. On my estimates it earns {pct(Y26['pg_share'], 0)}% of 2026 segment "
       f"profit, rising to {pct(Y28['pg_share'], 0)}% in 2028. Not all of it is data centres, and Caterpillar does not split it out. Some of "
       "the data centre boom also lands elsewhere: in gas compression for the pipes that feed new plants, and in the machines that build "
       "the campuses. Most of the rest is diggers and mining trucks, which follow building and commodity cycles."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {usd(PRICE, 2)} Caterpillar is worth US${MCAP:.1f}bn. Its machinery business held net debt of only US${NET_DEBT_MPE / 1000:.1f}bn "
       "at the end of September; the finance arm's debt is backed by its loans. The shares trade at "
       f"{PE_C26:.1f} times the 2026 consensus of US${CONS_EPS26:.2f} and {PE_C27:.1f} times 2027's US${CONS_EPS27:.2f}. At the June record "
       f"they paid {PE_PEAK_C27:.1f} times that 2027 figure. Caterpillar's forward P/E averaged {HIST_FWD_PE_AVG_2124:.1f} times from 2021 to 2024 "
       f"and reached {HIST_FWD_PE['2025']:.1f} times in 2025 (stockanalysis.com). The average target of {CONS_N} analysts is {usd(CONS_TP)}."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["30 Apr 2026", "Q1 results; sales up 22%; record backlog", f"up {Q1_MOVE * 100:.1f}%"],
        ["30 Jun 2026", f"Record close {usd(HI_CLOSE, 2)}", "Peak"],
        ["1 to 31 Jul", "No results", f"down {abs(JUL_FALL) * 100:.1f}%"],
        ["4 Aug 2026", "Q2 results; first US$20bn quarter", f"up {Q2_MOVE * 100:.1f}%"],
        ["29 Oct 2026", "Q3 results; Q4 guide of moderate growth", f"down {abs(Q3_MOVE) * 100:.1f}%"],
        ["6 to 30 Oct", "Whole October fall", f"down {abs(OCT_FALL) * 100:.1f}%"],
    ],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: Caterpillar month-end close, January 2024 to the 30 October 2026 close, against my base value (red). stockanalysis.com, "
          "retrieved 2 November 2026. Right: moves from the previous close to the close on the results day (results come before the open)."))
A('</div>')
A(para("I split the price in two. If the rest of Caterpillar earns its old cyclical multiple, what is left over is what the market pays for "
       "Power Generation."))
A(para(f"<strong class='lead'>The rest is worth about {usd(REST_VAL)} a share.</strong> On my estimates it earns US${REST_EPS:.2f} a share in "
       f"2028. At {REST_PE:.0f} times, near Caterpillar's own 2021 to 2024 average and the 15.2 times median of five machinery and truck peers, "
       f"that is {usd(REST_VAL)}."))
A(para(f"<strong class='lead'>So the price pays about {IMPLIED_PG_PE:.0f} times for the power business.</strong> That leaves "
       f"{usd(PRICE - REST_VAL)} for US${PG_EPS:.2f} of 2028 Power Generation earnings. At the June record it left {usd(HI_CLOSE - REST_VAL)}, "
       f"about {IMPLIED_PG_PE_PEAK:.0f} times; power was then {PG_SHARE_PEAK * 100:.0f}% of the price, against {PG_SHARE_PRICE * 100:.0f}% today. "
       "The three power peers I use, GE Vernova, Siemens Energy and Wartsila, trade at 20 to 37 times forward earnings, median 21.8."))
A(para("<strong class='lead'>Where I differ from the market, and from consensus.</strong> The market has stopped paying an AI premium on "
       "Caterpillar, and I think it was right to. But I also sit below consensus: my 2027 EPS of "
       f"US${E27:.2f} is {abs(E27 / CONS_EPS27 - 1) * 100:.0f}% under the US${CONS_EPS27:.2f} consensus. I assume Construction Industries barely "
       "grows after a 21% year that included a dealer stock build, and that Caterpillar only begins to lift its margin off the bottom of its "
       "range, as its chief executive put it on the call (third-party transcript). The power queue is visible; the diggers' cycle is not. That leaves the price close "
       "to fair, not cheap."))

A(section("Valuation, with the working"))
A(para("I value Caterpillar on adjusted EPS twelve months out, so 2028 is the year the market will price in October 2027. I build segment "
       "sales and margins and bridge to EPS. Power &amp; Energy is built by application: Power Generation grows "
       f"{G['PG27'] * 100:.0f}% in 2027 and {G['PG28'] * 100:.0f}% in 2028 as capacity arrives, reaching {PG_X_2024_28:.1f} times 2024, ahead of "
       f"the 2030 target of more than twice. The segment margin goes from {pct(pe(Y26))}% to {pct(pe(Y28))}%. Corporate costs and "
       f"eliminations take US${-G['BR27'] / 1000:.1f}bn and US${-G['BR28'] / 1000:.1f}bn, tax is 23% and buybacks cut diluted shares to {G['SH28']:.0f}m. "
       f"My 2026E of US${E26:.2f} sits close to the US${CONS_EPS26:.2f} consensus."))
A(para(f"<strong class='lead'>Sum of the parts.</strong> I give Power Generation {PG_PE:.0f} times its 2028 earnings, above the 21.8 times power "
       "peer median because its growth runs further and its orders reach 2030, and below GE Vernova. The rest gets "
       f"{REST_PE:.0f} times. {PG_PE:.0f} x US${PG_EPS:.2f} + {REST_PE:.0f} x US${REST_EPS:.2f} = {usd(BASE_VALUE, 2)}, or {BLENDED_PE:.1f} times "
       f"my 2028 EPS. Power Generation is {PG_SHARE_BASE * 100:.0f}% of that value."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiples", "Value", "Change", "Weight"],
    [
        ["Bear", "Data centre orders pause and diggers turn: PG growth 10% then 3%, CI down 6% then 4%, margins slip", f"US${SC[0]['e28']:.2f}", f"{SC[0]['mpg']:.0f}x / {SC[0]['mrest']:.0f}x", usd(bear), chg(bear), "25%"],
        ["Base", f"PG growth {G['PG27'] * 100:.0f}% then {G['PG28'] * 100:.0f}%; CI flat; margins edge up", f"US${SC[1]['e28']:.2f}", f"{SC[1]['mpg']:.0f}x / {SC[1]['mrest']:.0f}x", usd(base), chg(base), "50%"],
        ["Bull", "Capacity arrives early: PG growth 28% then 22%, P&amp;E margin 27%; CI and mining grow", f"US${SC[2]['e28']:.2f}", f"{SC[2]['mpg']:.0f}x / {SC[2]['mrest']:.0f}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 41, 11, 11, 10, 10, 8]))
A(caption("Multiples are Power Generation / the rest, on 2028E. All cases start from my 2026E and use the same bridge. The bear case is close "
          "to two fifths below the price: the risk is weighted to the downside because the cycle and the multiple fall together."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: the two multiples on my 2028 EPS"))
A('<div class="chartsrow"><div class="col left">')
grid = [[PG_EPS * a + REST_EPS * b for b in SENS_REST] for a in SENS_PG]
A(datatable(
    ["Power x \\ rest x"] + [f"{b:.0f}x" for b in SENS_REST],
    [[f"{a:.0f}x"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (a, row) in enumerate(zip(SENS_PG, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
n_25 = sum(v <= PRICE * 0.75 for r in grid for v in r)
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
A(para(f"{W[n_above]} of the nine cells sit above the price, {W[n_15].lower()} of them 15% or more above it, and {W[n_25].lower()} 25% "
       "or more below it. The rest's multiple moves the value more than the power multiple: each turn on the rest is worth "
       f"{usd(REST_EPS)}, each turn on power {usd(PG_EPS)}. A long needs the base 15% or more above the price, a short 25% or more below. "
       f"At {UP_BASE * 100:+.0f}%, {my_call.lower()} is no call."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBIT", "What they make"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w, g in PEERS],
    num_cols={2, 3},
), [16, 15, 11, 10, 48]))
A(caption("Forward P/E and trailing EV/EBIT from stockanalysis.com (S&amp;P Global data), retrieved 2 November 2026. Power peers (GE Vernova, "
          "Siemens Energy, Wartsila) median 21.8x; machinery and truck peers (Cummins, Paccar, Komatsu, Volvo, Deere) median 15.2x. Deere's "
          "multiple is high because its earnings are near a cyclical low. Multiples are used only to set the range; no view on the peers' "
          "shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Early November 2026", "Q3 2026 Form 10-Q", "Backlog not due within twelve months; any Power &amp; Energy backlog detail"],
        ["2 February 2027", "Q4 2026 results and 2027 outlook", "Power Generation for 2026 against my US$13.4bn; backlog; how far off the bottom of the margin range 2027 starts"],
        ["2027 (dates not set)", "Capacity steps for large engines and turbines", "Units shipped against the three-times target; any sign of discounting"],
        ["Late April 2027", "Q1 2027 results", "Construction Industries volume after the 2026 dealer stock build"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view, either way"))
A(para("<strong>Data centre orders pause.</strong> Power Generation is about a quarter of my 2028 earnings, and the backlog is concentrated in "
       "large customers on framework agreements. In September the chief executive said conversion to firm orders will be lumpy. A pause would show first in the "
       "backlog, which has risen in every quarter since the end of 2024."))
A(para("<strong>Too much capacity, everywhere.</strong> Caterpillar is lifting large engine capacity to about three times its 2024 level by 2030, "
       "up from two times at its 2025 Investor Day, and is adding turbine capacity. Rivals are adding too. The chief executive said "
       "at some point the industry \"probably needs to be in free supply\". Prices would then soften."))
A(para("<strong>The diggers turn.</strong> Construction Industries grew about 21% in 2026 on my estimate, helped by dealers adding stock, and "
       "on the call (third-party transcript) Caterpillar said it expects fourth quarter volume to be down modestly. Mining depends on copper and gold prices. The rest of "
       "Caterpillar, mostly construction and mining, carries about three quarters of my 2028 earnings at a cyclical multiple."))
A(para("<strong>Tariffs and one-offs.</strong> On the call (third-party transcript) Caterpillar said it expects tariff costs of about US$2.2bn in 2026, "
       "and 2026 profit includes US$520m of refunds of tariffs the Supreme Court ruled unauthorised (Form 10-Q, June 2026). Both move the margin by more than half a point."))
A(para("<strong>Upside risk.</strong> If capacity arrives early, Power Generation keeps growing above 20% and the diggers hold up, "
       f"my bull case gives {usd(bull)}, {chg(bull)}."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into long:</strong> a price below about {usd(LONG_BELOW)}, where my base value would sit 15% above it, or fourth quarter "
       "results showing Power Generation up 25% or more for a second year with the backlog still rising. <strong>Into short:</strong> a "
       f"price above about {usd(SHORT_ABOVE)} on unchanged estimates, or a fall in the backlog with construction volumes falling."))
A(para(f"<strong>{my_call} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para("The September piece argued that building your own power swaps the grid's queue for the makers' queues, and that the fast lane is "
       "queued too. Caterpillar confirms it: a US$78.1bn backlog, orders into 2029 for large engines and into 2030 for turbines, and "
       f"customers paying ahead. Power Generation is about {pct(Y26['pg_share'], 0)}% of 2026 segment profit on my estimates, rising to "
       f"{pct(Y28['pg_share'], 0)}%, and the rest is a cyclical machinery business. At {usd(PRICE, 2)} the market pays about "
       f"{IMPLIED_PG_PE:.0f} times for the power business, down from about {IMPLIED_PG_PE_PEAK:.0f} in June. {my_call}: {CALL['direction']}, "
       f"{conv} conviction; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Power Generation growth", f"{pg_g26 * 100:.0f}%", f"{G['PG27'] * 100:.0f}%", f"{G['PG28'] * 100:.0f}%", "Q4 2026E up 25%; capacity sets the pace"],
        ["Oil and Gas / Industrial growth", f"{(Y26['app']['OG'] / APP['OG']['2025A'] - 1) * 100:.0f}% / {(Y26['app']['IN'] / APP['IN']['2025A'] - 1) * 100:.0f}%",
         f"{G['OG27'] * 100:.0f}% / {G['IN27'] * 100:.0f}%", f"{G['OG28'] * 100:.0f}% / {G['IN28'] * 100:.0f}%", "Gas compression demand"],
        ["Power &amp; Energy margin", f"{pct(pe(Y26))}%", f"{pct(pe(Y27))}%", f"{pct(pe(Y28))}%", "Q3 2026: 24.4%; Q4 guided similar"],
        ["Construction Industries growth / margin", f"{(Y26['ci_s'] / s25['CI'][0] - 1) * 100:.0f}% / {pct(Y26['ci_p'] / Y26['ci_s'])}%",
         f"{G['CI27'] * 100:.0f}% / {G['CIM27'] * 100:.1f}%", f"{G['CI28'] * 100:.0f}% / {G['CIM28'] * 100:.1f}%", "After a dealer stock build"],
        ["Resource Industries growth / margin", f"{(Y26['ri_s'] / s25['RI'][0] - 1) * 100:.0f}% / {pct(Y26['ri_p'] / Y26['ri_s'])}%",
         f"{G['RI27'] * 100:.0f}% / {G['RIM27'] * 100:.1f}%", f"{G['RI28'] * 100:.0f}% / {G['RIM28'] * 100:.1f}%", "Mining orders up; tariff costs ease"],
        ["Corporate and eliminations, US$m", f"{Y26['bridge']:,.0f}", f"{G['BR27']:,.0f}", f"{G['BR28']:,.0f}", "2026 includes US$520m tariff refunds"],
        ["Tax rate / diluted shares, m", "23% (Q4)", f"23% / {G['SH27']:.0f}", f"23% / {G['SH28']:.0f}", "Guided rate; buybacks"],
    ],
), [30, 15, 13, 13, 29]))
A(caption(f"All my estimates. Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Caterpillar third quarter 2026 earnings release (Form 8-K, Exhibit 99.1, 29 October 2026) for segment sales and profit, '
  'Power &amp; Energy sales by application, the adjusted EPS reconciliation, the balance sheet and customer advances. Caterpillar Q3 2026 analyst '
  'slides (29 October 2026) for the US$78.1bn backlog, the 2026 outlook, the margin target range, retail statistics and the results calendar. '
  'Q1 and Q2 2026 earnings releases (30 April and 4 August 2026). Form 8-K of 26 March 2026 recasting 2024 and 2025 segments. Q4 2025 earnings '
  'release and analyst slides (29 January 2026) for 2024 and 2025 adjusted results and the 2030 targets. Form 10-K for 2024 and 2025 and Form '
  '10-Qs from March 2025 to June 2026 for backlog. Caterpillar virtual HQ visit with Wells Fargo, 10 September 2026, transcript posted by '
  'Caterpillar. Q3 2026 earnings call, 29 October 2026, from a third-party transcript (The Singju Post). Share prices, consensus, targets and '
  'peer multiples from stockanalysis.com (S&amp;P Global data), retrieved 2 November 2026. Estimates for the fourth quarter of 2026, 2027 and '
  '2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 22 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/building-your-own-power/">thephysicallayer.fyi/journal/building-your-own-power</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Caterpillar. Personal research, not investment advice.</p>')
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
