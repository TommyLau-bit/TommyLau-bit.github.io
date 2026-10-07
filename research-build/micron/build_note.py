# -*- coding: utf-8 -*-
"""Micron Technology, Inc. (Nasdaq: MU) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/micron.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Micron Technology, Inc. (Nasdaq: MU)"
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


def usd(x, d=0):
    from decimal import Decimal, ROUND_HALF_UP   # half-up, as the model's cells display
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"US${q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


bear, base, bull = VALS
sb, sm, su = SV
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = ("My draft view" if CALL["draft"] else "My call")
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
above = sum(v > PRICE for r in VGRID for v in r)
below25 = sum(v <= PRICE * 0.75 for r in VGRID for v in r)

A('<h1 class="doctitle">Micron Technology, Inc.</h1>')
A('<p class="docsubtitle"><b>Nasdaq: MU | DRAM including HBM, and NAND flash | Boise, Idaho</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:,.2f} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:,.2f}, Nasdaq close {PRICE_DATE}; 52-week range US${LO52:,.2f} to {HI52:,.2f} (intraday)"),
    ("Market value", f"About US${MCAP:,.0f}bn on {SHARES_OUT:.2f}bn shares"),
    ("Net cash, 3 Sep 2026", f"US${NET_CASH:.1f}bn; US${NET_CASH_ADJ:.1f}bn after US${DEPOSITS:.1f}bn of customer deposits; per share on 1.15bn diluted shares"),
    ("Non-GAAP P/E", f"{PE26:.1f}x FY26; {PEC27:.1f}x FY27 and {PEC28:.1f}x FY28 consensus; {PE27:.1f}x and {PE28:.1f}x my estimates"),
    ("Consensus (stockanalysis.com)", f"EPS US${CONS_EPS_27:.2f} FY27, US${CONS_EPS_28:.2f} FY28; average target US${CONS_TP:,.2f}"),
    ("Q1 FY27 guide (30 Sep)", "Revenue US$61.5bn; gross margin about 86.25%; EPS US$38.15"),
    ("Fiscal year", "Ends on the Thursday nearest 31 August: FY26 to 3 Sep 2026; FY27 to about 2 Sep 2027"),
    ("Next results", f"Q1 FY27, expected {RESULTS_DATE} (third-party calendars; not yet confirmed by Micron)"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Micron\'s wafers are still short, but at US${PRICE:,.0f} the price needs the next normal year to earn like the last peak.</p>')
A(para("Micron makes DRAM, including the HBM stacked beside AI chips, and NAND flash. On 7 October I argued that HBM, sold a year "
       "ahead and three times as hungry for wafers, keeps ordinary memory short too. The results support it: fiscal 2026 revenue was "
       f"US${FY26['rev']:.1f}bn, {FY26['rev'] / FY25['rev']:.1f} times the year before, and Micron says its 2027 HBM prices narrow "
       "the gross margin gap with conventional DRAM."))
A(para(f"At US${PRICE:,.2f} the shares trade at {PEC27:.1f} times consensus fiscal 2027 earnings. That looks cheap, but memory is "
       f"cyclical. On my method the price needs normal earnings of about {usd(NEED_N, 2)} a share after the shortage: a "
       f"{pc(NEED_NM)} net margin on my normal revenue, near the {pc(PEAK18_NM)} of the 2018 peak. I take {pc(NM, 0)}."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction.</b> My base case is worth "
       f"{usd(BASE_VALUE)}, {chg(BASE_VALUE)}, inside my band. The bear case is {usd(bear)} ({chg(bear)}) and the bull case "
       f"{usd(bull)} ({chg(bull)}). The view leans short, but take-or-pay floors make the next trough hard to call."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (non-GAAP unless marked; FY26 ended 3 September 2026, FY27 ends about 2 September 2027)"))
A(datatable(
    ["US$ billion unless stated", "FY25A", "FY26A", "Q1 FY27 guide", "FY27E*", "FY28E*", "Normal year*"],
    [
        ["Revenue", f"{FY25['rev']:.1f}", f"{FY26['rev']:.1f}", f"{G1['rev']:.1f}", f"{REV27:.1f}", f"{REV28:.1f}", f"{normal_rev():.1f}"],
        ["Revenue growth (%)", "49", f"{(FY26['rev'] / FY25['rev'] - 1) * 100:.0f}", "", f"{(REV27 / FY26['rev'] - 1) * 100:.0f}", f"{G28 * 100:.0f}", ""],
        ["  HBM (my estimate)", "", f"about {HBM26:.0f}", "", f"{SPLIT27['hbm']:.0f}", f"{SPLIT28['hbm']:.0f}", ""],
        ["  Conventional DRAM", "", f"about {CONV26:.0f}", "", f"{CONV27:.0f}", f"{CONV28:.0f}", ""],
        ["  NAND", "", f"{FY26['nand']:.1f}", "", f"{SPLIT27['nand']:.0f}", f"{SPLIT28['nand']:.0f}", ""],
        ["Gross margin (%)", pc(FY25["gm"]), pc(FY26["gm"]), "86.25", pc(GM27), pc(GM28), ""],
        ["Operating income", "", f"{FY26['op']:.1f}", "", f"{OP27:.1f}", f"{REV28 * GM28 - OPEX28:.1f}", ""],
        ["Net margin (%)", pc(FY25["ni"] / FY25["rev"]), pc(FY26["ni"] / FY26["rev"]), "", pc(NI27 / REV27), pc(EPS28 * SH / REV28), pc(NM)],
        ["EPS, diluted (US$)", f"{FY25['eps']:.2f}", f"{FY26['eps']:.2f}", f"{G1['eps']:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}", f"{N_BASE:.2f}"],
        ["Consensus EPS (US$)", "", "", "", f"{CONS_EPS_27:.2f}", f"{CONS_EPS_28:.2f}", ""],
        [f"P/E at US${PRICE:,.2f} (x)", f"{PRICE / FY25['eps']:.0f}", f"{PE26:.1f}", "", f"{PE27:.1f}", f"{PE28:.1f}", f"{PE_NORMAL:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*FY27E is the Q1 guide plus my Q2 to Q4; FY28E and the normal year are my own estimates. Micron reports DRAM including HBM "
          "and stopped giving HBM revenue, so the HBM and conventional DRAM split is mine. FY26 operating income is the sum of the quarters. Consensus from "
          "stockanalysis.com (S&P Global data, updated 6 October 2026). History from Micron's release and prepared remarks of 30 September 2026."))

A('<div class="keeptogether">')
A(section("Two charts: a cycle at its highest, and a value below the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_cycle.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and net margin by fiscal year; GAAP to FY26 (10-K data via SEC EDGAR and stockanalysis.com), my non-GAAP "
          "estimates for FY27 and FY28. Right: value per share from the base case, the probability-weighted cases, the sensitivity grid "
          f"and the bear to bull range, against the US${PRICE:,.2f} price (red) and the stockanalysis.com average analyst target."))
A('</div>')

A(section("The thesis: the bread is earning more than the cakes"))
A(para("Go back to the baker from the October piece. She has one oven and bakes bread and wedding cakes. A cake takes three trays of "
       "oven time for the weight of one tray of bread, and couples book a year ahead at a fixed price. So as cake orders grow, the bread "
       "queue lengthens, and right now the bread is where the money is, because it sells at today's price."))
A(para(f"<strong>The oven is full.</strong> In the quarter to 3 September revenue was US${Q_REV[-1]:.1f}bn: DRAM US${Q_DRAM[-1]:.1f}bn "
       f"and NAND US${Q_NAND[-1]:.1f}bn. DRAM bits rose by a mid single digit percentage on the quarter and prices by a high teens "
       f"percentage. Gross margin was {pc(Q_GM[-1])}, against {pc(Q_GM[0])} a year earlier. Micron guides US$61.5bn for the quarter "
       "to November and expects revenue to rise in every quarter of fiscal 2027."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_quarters.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_bu.png"></div></div>')
A(caption("Left: revenue by fiscal quarter, DRAM (including HBM) and NAND, with non-GAAP gross margin in white, and the Q1 FY27 guide. "
          "Q4 FY25 DRAM and NAND are derived from the growth Micron gave on 30 September 2026. Right: gross margin by business unit in "
          "fiscal 2026. Source: Micron prepared remarks and earnings calls, 17 December 2025 to 30 September 2026."))
A('</div>')
A(para("<strong>The cakes are booked, and the piece holds.</strong> On 30 September Micron said it had agreements for \"the vast "
       "majority\" of its calendar 2027 HBM bits, at significant price increases. In December 2025 it said the three to one trade "
       "ratio with DDR5 \"only increases with future generations\". And it expects industry HBM bits to outgrow conventional DRAM "
       "through calendar 2028, with DRAM supply constrained in 2027 and 2028. I checked the piece's figures against the remarks, "
       "calls and release; they stand."))
A(para("<strong>The bread earns more.</strong> Micron says its 2027 HBM prices narrow \"the gross margin gap with conventional "
       "DRAM\", as the piece read. The unit margins are consistent with it: the cloud unit, which carries HBM, held an 83% gross margin "
       "in the last quarter, flat because of \"higher HBM mix\", while the core data centre and mobile units rose to 90%. The units are "
       "customer groups, not products, and the cloud unit sells conventional DRAM too. HBM was nearly US$2bn of revenue in the quarter to August 2025; on my "
       f"estimate it was about US${HBM26:.0f}bn of fiscal 2026's US${FY26['dram']:.1f}bn of DRAM. The squeeze pays mostly through "
       "ordinary memory, as the piece argued."))
A(para(f"<strong>The baker now takes deposits.</strong> Micron has signed {SCA_N} multi-year take-or-pay agreements, which it estimates "
       f"cover more than 35% of revenue through 2030, with US${SCA_COMMIT:.0f}bn of customer commitments, mostly cash deposits. Three "
       "quarters of that revenue has a defined pricing framework, a majority of it with floor and ceiling prices, so floors cover "
       "roughly 13 to 26% of revenue. The CFO said that even at floor prices margins sit \"meaningfully above any prior cycle peak "
       "margins\", which Micron's June remarks tie to gross margin. More than 75% of 2027 output is committed. New cleanrooms take years: ID1 starts output in mid calendar 2027, ID2 in late "
       "2028 and New York in 2030."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:,.2f} Micron is worth about US${MCAP:,.0f}bn. The shares trade at {PE26:.1f} times fiscal 2026 EPS of "
       f"US${FY26['eps']:.2f}, {PEC27:.1f} times fiscal 2027 consensus and {PEC28:.1f} times fiscal 2028. They closed at a high of "
       f"US${HI_CLOSE:,.2f} on 25 June 2026 and are {abs(OFF_HIGH) * 100:.0f}% below it."))
A(para(f"<strong class='lead'>The low multiple is not the point.</strong> Peak memory earnings are not a stream to capitalise. Micron's "
       f"highest close of fiscal 2022 was US${FY22_HI[0]:.2f}, {FY22_PE_HI:.1f} times that year's GAAP EPS of US$7.75; eight months "
       f"later the shares had halved to US${FY23_LO[0]:.2f}, and fiscal 2023 brought a loss of US$5.34 a share. On the 30 September "
       "call an analyst said memory shares look depressed because people think next year may be the peak. Mehrotra answered that 2027 "
       "and 2028 will be tighter than 2026."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_eps.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: non-GAAP EPS, reported for FY25 and FY26, my estimates for FY27 and FY28, my base normal year, and the normal year "
          "the price needs on my method. Right: MU month-end close, September 2023 to the 6 October 2026 close (Nasdaq.com, retrieved "
          "7 October 2026), against my base value."))
A('</div>')
A(para(f"<strong class='lead'>What the price needs.</strong> I value the cycle, not the year: net cash at October 2027, plus the "
       f"earnings above normal still to come, plus {MULT} times normal earnings. On my base fiscal 2028, US${PRICE:,.2f} needs normal "
       f"EPS of about {usd(NEED_N, 2)}, {NEED_VS_26 * 100:.0f}% of fiscal 2026 and a third of my fiscal 2028. On my normal revenue of "
       f"US${normal_rev():.0f}bn, that is a {pc(NEED_NM)} net margin. Micron earned {pc(PEAK18_NM)} in fiscal 2018, the last peak, "
       f"and {pc(CYC_NM)} over fiscal 2016 to 2025 in all."))
A(para(f"<strong class='lead'>Where I differ.</strong> I take a {pc(NM, 0)} normal margin: far above history, because the take-or-pay "
       "floors, HBM and the deposits are real changes, but well below the old peak. My normal revenue lets bits grow 20% a year for "
       f"four years and revenue per bit settle at {PF * 100:.0f}% of fiscal 2026's average. The market assumes Micron keeps close to "
       "peak economics through the next downturn. It may, which is why I do not go short. The floors deserve their due: a gross margin "
       "above the old peaks implies a net margin of roughly 45% or more on the floored slice. If that is a fifth to a quarter of revenue, "
       "my 30% needs the rest to earn about 25 to 26%, a little above its ten-year 18.8%; the price needs the rest near 45% too."))

A(section("Valuation, with the working"))
A(para(f"Fiscal 2027 is the Q1 guide, then revenue up about 6, 5 and 4% a quarter, gross margin rising to 88% and operating costs "
       f"up the guided US$2.5bn to US${OPEX27:.1f}bn, with 15.5% tax on 1.15bn shares: EPS {usd(EPS27, 2)}, "
       f"{abs(EPS27 / CONS_EPS_27 - 1) * 100:.1f}% below consensus. Fiscal 2028 grows {G28 * 100:.0f}% at an {pc(GM28, 0)} gross "
       f"margin: EPS {usd(EPS28, 2)}, {abs(EPS28 / CONS_EPS_28 - 1) * 100:.1f}% below consensus. Free cash flow of about "
       f"US${FCF27:.0f}bn after US${CAPEX27:.0f}bn of capital spending takes net cash after deposits to about {usd(NC_PS)} a share (on 1.15bn diluted shares) by "
       f"October 2027. The fiscal 2028 excess, and half of it again in 2029, discounted at 10%, adds {usd(sm['exc'])}; "
       f"{MULT} times normal EPS of {usd(N_BASE, 2)} adds {usd(sm['term'])}. Total: {usd(BASE_VALUE)}. Measuring the excess on "
       "earnings is generous, because construction spending will run far ahead of depreciation."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "FY28 EPS", "Normal EPS", "Normal P/E", "Value", "Change", "Weight"],
    [
        ["Bear", "Prices turn in 2027 as new cleanrooms ramp; normal year at the ten-year margin", usd(sb["eps28"], 2), usd(sb["n"], 2),
         f"{SCEN[0][3]}x", usd(bear), chg(bear), "25%"],
        ["Base", "Tight through FY28, half the excess in FY29; normal year above history", usd(sm["eps28"], 2), usd(sm["n"], 2),
         f"{SCEN[1][3]}x", usd(base), chg(base), "50%"],
        ["Bull", "Shortage outlasts 2028, as Micron's \"no line of sight\" to balance allows; floors hold margins near 40%", usd(su["eps28"], 2), usd(su["n"], 2),
         f"{SCEN[2][3]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [9, 37, 10, 10, 8, 9, 10, 7]))
A(caption(f"Normal revenue: bear US${sb['nrev']:.0f}bn at a {pc(SCEN[0][2], 0)} margin; base US${sm['nrev']:.0f}bn at "
          f"{pc(SCEN[1][2], 0)}; bull US${su['nrev']:.0f}bn at {pc(SCEN[2][2], 0)}. Fiscal 2027 and the cash at October 2027 are the "
          "same in all three on purpose: Q1 is guided and more than 75% of 2027 output is committed, so the bear's price turn shows from FY28. The bear case is not fanciful: in the last cycle the shares halved within nine months of their high. "
          "The band: long when my base value is at least 15% above the price, short when it is at least 25% below, no call in between."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: normal net margin against the multiple on normal earnings"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Normal net margin"] + [f"{m}x" for m in SENS_X],
    [[pc(m, 0)] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (m, r) in enumerate(zip(SENS_NM, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{NUMW[above].capitalize()} of the nine cells sits above the price, and only just: it needs both a {pc(SENS_NM[2], 0)} normal "
       f"margin and {SENS_X[2]} times. {NUMW[below25].capitalize()} cells sit 25% or more below the price, all with a margin of "
       f"{pc(SENS_NM[0], 0)} or a multiple of {SENS_X[0]} times. Normal revenue, fiscal 2028 and the cash are as in the base. Every "
       "figure is live in the accompanying model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Listing", "P/E on consensus", "Year", "What they make"],
    [["Micron", "Nasdaq: MU", f"{PEC27:.1f}x", "FY to Aug 2027", "DRAM, HBM, NAND"]]
    + [[c, t, f"{px / e:.1f}x", y, w] for c, t, px, cur, e, y, w, nt in PEERS]
    + [[KIOXIA[0], KIOXIA[1], f"{KIOXIA[2] / KIOXIA[3]:.1f}x", KIOXIA[4], KIOXIA[5]]],
    num_cols={2},
), [22, 16, 14, 16, 32]))
A(caption(f"Price over consensus EPS for the year ending in 2027, from stockanalysis.com (S&P Global), retrieved 7 October 2026; Kioxia "
          f"is market value over consensus net income. Median of the four peers {PEER_MED:.1f} times. Prices are Nasdaq closes of 6 "
          "October and Seoul and Tokyo closes of 7 October 2026. Fiscal year-ends differ by up to eight months, so the multiples are not on one basis. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        [RETURN_DATE, "Capital return steps up (CHIPS Act anniversary)", "Size of the buyback against free cash flow"],
        [f"{RESULTS_DATE} (expected)", "Q1 FY27 results (quarter to about 3 December)", "Revenue against US$61.5bn; Q2 guide; DRAM price per bit"],
        ["Mid calendar 2027", "ID1 and Tongluo start output; Singapore HBM packaging", "Whether supply growth stays near the low 20s %"],
        ["September to December 2027", "Calendar 2028 HBM agreements", "Whether most of 2028 is agreed, and at what price"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>On the upside, the floors.</strong> Take-or-pay agreements are new to memory. If Micron reaches its goal of about half of "
       "revenue under these agreements, with more of it floored, and keeps signing to 2031, the next trough could look nothing like 2023; that is my bull "
       f"case, {chg(bull)}. <strong>On the downside, supply.</strong> Micron's guidance implies more than US$50bn of capital spending in fiscal 2027, mostly on "
       "construction, and ID1, Tongluo, Singapore and SK Hynix's Yongin all start in 2027. Every maker has the same price signal and "
       "the cash to answer it."))
A(para("<strong>Customers adjusting.</strong> Micron says servers now carry a \"modestly lower rate of content growth\", and an analyst "
       "asked about one large customer using less HBM. If HBM wafers returned to ordinary DRAM, the squeeze would ease. <strong>Ceilings "
       "as well as floors.</strong> The largest agreements generally cap existing products at calendar second quarter 2026 market prices."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price at or below about {usd(REVISIT_LONG)} with my numbers unchanged. "
       f"<strong>Into a short:</strong> a price at or above about {usd(REVISIT_SHORT)}. On my model, normal earnings of about "
       f"{usd(REVISIT_N_LONG)} a share or more would point long and about {usd(REVISIT_N_SHORT)} or less short, but those are my "
       "estimates, not something Micron reports."))
A(para("<strong>The view is wrong if</strong>, by October 2027, Micron reports a quarter in which DRAM prices and total revenue both fall "
       "on the quarter before, which points to my bear case; or it says strategic customer agreements with a defined pricing framework "
       "cover at least half of its revenue through 2030 while it still expects the industry to be supply constrained in calendar 2028, which lifts normal earnings towards my bull case."))
A('</div>')

A(section("Conclusion"))
A(para("My piece of 7 October argued that HBM takes wafers from ordinary memory and keeps that market short too. Micron's results "
       "support it: the 2027 HBM is sold, the trade ratio stands, and 2027 HBM prices narrow the margin gap with conventional DRAM. The "
       f"shares are a different question. At about {PEC27:.0f} times consensus they look cheap, but the price needs a normal year near "
       f"the 2018 peak margin. Base value {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}. {my_call}: "
       f"{CALL['direction']}, leaning short, {CALL['conviction'].lower()} conviction."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY27E", "FY28E", "Normal", "Basis"],
    [
        ["Revenue, US$bn", f"{REV27:.1f}", f"{REV28:.1f}", f"{normal_rev():.1f}", "Q1 guide, then about 6, 5, 4% a quarter; FY28 +10%; normal: bits x1.2 a year for 4 years, 55% of FY26 price"],
        ["Gross margin", pc(GM27), pc(GM28), "", "Q1 guided 86.25%, 'the floor' for FY27"],
        ["Operating expenses, US$bn", f"{OPEX27:.1f}", f"{OPEX28:.1f}", "", "FY26 about 6.8 plus the guided 2.5"],
        ["Net margin", pc(NI27 / REV27), pc(EPS28 * SH / REV28), pc(NM, 0), "Normal: FY16-25 18.8%; FY18 peak 46.5%"],
        ["Tax rate", pc(TAX), pc(TAX), "", "Guided around 15.5%"],
        ["Diluted shares, bn", f"{SH:.2f}", f"{SH:.2f}", f"{SH:.2f}", "Q1 guide held; buybacks treated as cash kept"],
        ["Capex, US$bn", f"{CAPEX27:.0f}", "", "", "First half about 25 guided, second half higher"],
        ["Multiple, discount rate", "", "", f"{MULT}x, 10%", "Mine"],
    ],
), [24, 9, 9, 10, 48]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Micron fourth quarter and fiscal 2026 results release, Exhibit 99.1 to Form 8-K, 30 September 2026, for revenue, '
  'margins, net income, EPS, business unit revenue, cash flow, cash, debt, shares and the Q1 FY27 guide. Micron prepared remarks of 24 June '
  'and 30 September 2026, for DRAM and NAND revenue, bits and prices, business unit margins, HBM agreements, strategic customer agreements, '
  'deposits, the market outlook, fab timing and the fiscal 2027 outlook. Micron earnings calls of 23 September 2025, 17 December 2025, '
  '18 March 2026 and 30 September 2026. Micron 10-K data via SEC EDGAR for fiscal 2016 to 2021. Share prices from Nasdaq.com historical '
  'data, retrieved 7 October 2026; consensus, average target, shares outstanding and peer figures from stockanalysis.com, retrieved '
  '7 October 2026. Estimates for fiscal 2027 and 2028, the HBM split, normal earnings and the valuation are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 7 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/micron-three-times-the-wafer/">thephysicallayer.fyi/journal/micron-three-times-the-wafer</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Micron. Personal research, not investment advice.</p>')
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
