# -*- coding: utf-8 -*-
"""Nvidia (Nasdaq: NVDA) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/nvidia.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Nvidia Corporation (Nasdaq: NVDA)"
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
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"US${q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


bear, base, bull = VALS
pb, pbe, pbu = project(*SCEN[1][1:8]), project(*SCEN[0][1:8]), project(*SCEN[2][1:8])
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
gw27lo, gw27hi = DC27 / USD_PER_GW[1], DC27 / USD_PER_GW[0]

A('<h1 class="doctitle">Nvidia Corporation</h1>')
A('<p class="docsubtitle"><b>Nasdaq: NVDA | AI accelerators, rack-scale systems, NVLink, InfiniBand and Ethernet networking | Santa Clara, California</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:,.2f} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:,.2f}, Nasdaq close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:.2f} (intraday)"),
    ("Market value", f"About US${MCAP / 1000:,.2f} trillion on {SHARES_OUT:.1f}bn shares (21 Aug 2026)"),
    ("Net cash, 26 Jul 2026", f"US${NETCASH:.1f}bn: cash and debt securities US${CASH:.1f}bn, debt US${DEBT:.1f}bn"),
    ("P/E, my estimates", f"{PE27:.0f}x FY27E, {PE28:.0f}x FY28E, {PE29:.0f}x FY29E (FY27 ends about 31 Jan 2027)"),
    ("Consensus (stockanalysis.com)", f"EPS US${CONS_EPS_27:.2f} FY27, US${CONS_EPS_28:.2f} FY28; average target US${CONS_TP:,.2f}"),
    ("Q3 FY27 guide (26 Aug)", "Revenue US$108.0bn, plus or minus 2%; gross margin 74.0%; no Data Center compute revenue from China assumed"),
    ("Guarantees", f"Up to US${GUAR_TOTAL:.1f}bn for customers' land, power and shell, US$105bn of it for 4.25 GW in Ohio"),
    ("Supply commitments", "US$279bn at 26 Jul 2026, up from US$119bn a quarter earlier, mainly memory"),
    ("Next results", f"Q3 FY27, {RESULTS_DATE} (Nvidia release, 28 Oct 2026)"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Nvidia already sells about twelve gigawatts of AI a year. Consensus needs half as much again next year; the price assumes the power stops growing after that.</p>')
A(para("Nvidia designs the chips, racks and networks inside AI data centres. My journal pieces argue that power, not chips, sets the pace "
       "of AI. Nvidia's own filings now agree: it lists energy among the things that move its demand, and since August it has guaranteed "
       f"up to US${GUAR_TOTAL:.1f}bn of its customers' land, power and buildings. On its own yardstick, about US${USD_PER_GW_MID:.0f}bn of revenue "
       f"for each gigawatt of computers, its revenue this year equips about {GW27:.0f} gigawatts."))
A(para(f"The FY28 consensus needs about {CONS_GW_G * 100:.0f}% more gigawatts than that, which the grid and equipment queues on this site "
       f"make hard. I assume 20% and then 15%, so my FY28 EPS of US${pb['eps28']:.2f} is {abs(EPS28_VS_CONS) * 100:.0f}% below consensus. "
       f"Yet at {M_BASE} times, the price needs FY29 EPS of only US${NEED_EPS29:.2f}: it pays for one more year of growth and little after."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {usd(tgt)}.</b> My base case is worth "
       f"{usd(BASE_VALUE)}, {chg(BASE_VALUE)}. The bear case is {usd(bear)} ({chg(bear)}) and the bull case {usd(bull)} ({chg(bull)}). "
       "Conviction is low because the growth in powered gigawatts is my judgement, and no one publishes it."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (non-GAAP from FY27; FY27 ends about 31 January 2027)"))
A(datatable(
    ["US$ billion unless stated", "FY25A", "FY26A", "FY27E*", "FY28E*", "FY29E*"],
    [
        ["Data Center revenue", f"{DC_H[0]:.1f}", f"{DC_H[1]:.1f}", f"{DC27:.1f}", f"{pb['dc28']:.1f}", f"{pb['dc29']:.1f}"],
        ["Edge Computing and other", f"{REV_H[0] - DC_H[0]:.1f}", f"{REV_H[1] - DC_H[1]:.1f}", f"{EDGE27:.1f}", f"{EDGE28:.1f}", f"{EDGE29:.1f}"],
        ["Revenue", f"{REV_H[0]:.1f}", f"{REV_H[1]:.1f}", f"{REV27:.1f}", f"{pb['rev28']:.1f}", f"{pb['rev29']:.1f}"],
        ["Revenue growth (%)", f"{(REV_H[0] / FY24_REV - 1) * 100:.0f}", f"{(REV_H[1] / REV_H[0] - 1) * 100:.0f}", f"{(REV27 / REV_H[1] - 1) * 100:.0f}", f"{(pb['rev28'] / REV27 - 1) * 100:.0f}", f"{(pb['rev29'] / pb['rev28'] - 1) * 100:.0f}"],
        ["GW of IT load equipped (my yardstick)", "", f"{GW_FY26:.1f}", f"{GW27:.1f}", f"{pb['gw28']:.1f}", f"{pb['gw29']:.1f}"],
        ["Non-GAAP operating margin (%)", "", "", pc(OM27), pc(OM28), pc(OM29)],
        ["EPS, US$ (GAAP to FY26)", f"{GAAP_EPS_H[0]:.2f}", f"{GAAP_EPS_H[1]:.2f}", f"{EPS27:.2f}", f"{pb['eps28']:.2f}", f"{pb['eps29']:.2f}"],
        ["Consensus EPS (US$)", "", "", f"{CONS_EPS_27:.2f}", f"{CONS_EPS_28:.2f}", "n/v"],
        [f"P/E at US${PRICE:,.2f} (x)", "", f"{PRICE / GAAP_EPS_H[1]:.1f}", f"{PE27:.1f}", f"{PE28:.1f}", f"{PE29:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*FY27E is two reported quarters, the Q3 guide (US$108.0bn at 74.0% gross margin and US$9.0bn of costs) and my US$122bn Q4; "
          "FY28E and FY29E are my estimates. From Q1 FY27 Nvidia's non-GAAP measures include stock-based pay; FY25 and FY26 non-GAAP EPS on "
          f"the old basis were US${NG_EPS_OLD_H[0]:.2f} and US${NG_EPS_OLD_H[1]:.2f}, so history is shown on GAAP. Gigawatts are my translation "
          "at Nvidia's own PORTS yardstick (see the thesis). Consensus from stockanalysis.com (S&P Global data, updated 26 October 2026); "
          "FY28 is the page's 'next year' figure; n/v: FY29 consensus not verified. History from Nvidia's CFO commentaries."))

A('<div class="keeptogether">')
A(section("Two charts: the business, and the gigawatts it needs"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_dc.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_gw.png"></div></div>')
A(caption("Left: revenue by fiscal quarter, Data Center (labelled) and everything else, with the Q3 FY27 guide for total revenue (CFO "
          "commentaries). Right: Data Center revenue divided by Nvidia revenue per gigawatt of IT load, my arithmetic; the red bars span "
          f"Nvidia's US${PORTS_REV[0]:.0f}bn to US${PORTS_REV[1]:.0f}bn for {PORTS_GW} GW at PORTS, set to FY29 and deflated by my assumed "
          "rises for earlier years. FY28 consensus is revenue less my Edge estimate. A yardstick, not a count."))
A('</div>')

A(section("The thesis: the furniture maker waits for the house"))
A(para("Go back to the housing estate in my piece on how AI capacity arrives. Houses are sold off plan, built, connected to the mains, "
       "handed over and lived in. Nvidia sells the furniture. For three years every house came with a removal van booked, so the furniture "
       "maker sold as fast as it could make sofas. Now the houses are the slow part, and the four claims this note rests on point to the "
       "same place: Nvidia has bought its inputs years ahead and sets its suppliers' designs, but it cannot buy a switched-on hall."))
A(para("<strong>The chips now wait on the plug.</strong> Nvidia's 10-K for the year to 25 January 2026 lists whether customers can find "
       "enough data centre capacity \"or energy\" among the things that move its demand. Its CFO commentary of 26 August says securing land, "
       "power and shell \"has become the next critical phase in the AI infrastructure buildout\". On 17 August it guaranteed leases for "
       f"about {PORTS_GW} GW of IT load at SB Energy's PORTS campus in Ohio, which OpenAI will rent and fill only with Nvidia systems. The "
       "guarantees are capped at US$105bn and take effect as halls become ready for service, expected from 2028. With US$3.5bn of smaller "
       f"guarantees for AI clouds, Nvidia stands behind up to US${GUAR_TOTAL:.1f}bn. That is the stage my piece called the last one a "
       "builder controls, energised power, and the chip maker now pays to hurry it."))
A(para("<strong>Nvidia's revenue, in gigawatts.</strong> Nvidia gave the yardstick: each generation at PORTS \"could represent "
       "approximately 1.5 million NVIDIA GPUs, or approximately $150 billion to $200 billion in NVIDIA revenue\". Over 4.25 GW that is "
       f"US${USD_PER_GW[0]:.0f}bn to US${USD_PER_GW[1]:.0f}bn per gigawatt of computers, {NV_TO_VERTIV[0]:.0f} to {NV_TO_VERTIV[1]:.0f} times "
       "the US$3.25m to US$3.75m a megawatt Vertiv puts on its power and cooling gear. The halls are ready from 2028, so I set the "
       f"US${USD_PER_GW_MID:.0f}bn midpoint to FY29 and deflate it by my own assumed rises: US${USD_GW_28:.0f}bn in FY28 and "
       f"US${USD_GW_27:.0f}bn in FY27. On my FY27 Data Center revenue of US${DC27:.0f}bn that is about {GW27:.1f} GW of IT load in a "
       f"year; on the undeflated PORTS range, {gw27lo:.0f} to {gw27hi:.0f} GW."))
A(para("Set that against what the site has measured. Texas has been asked for 474 GW of connections and had cleared 6.6 GW to the last "
       "step by 20 August. GE Vernova ships about 20 GW of gas turbines a year in all, with heavy turbines largely sold out "
       "to 2030. Nebius expects 5 GW contracted at the end of 2026 against at most 1 GW connected. The grid makers hold one to four years "
       f"of orders. The FY28 consensus of US${CONS_REV_28:.0f}bn, less my US${EDGE28:.0f}bn for edge devices, needs about "
       f"US${DC28_CONS:.0f}bn of Data Center revenue: with revenue per gigawatt up 15%, about {CONS_GW_G * 100:.0f}% more gigawatts, "
       f"roughly {GW28_CONS:.1f} against {GW27:.1f}. I assume 20% and then 15%. That is faster than the makers add factories, because "
       "energised halls stand partly idle (Malaysia's data centres drew 1.26 of the 5.65 GW booked in June) and buyers add power of their "
       "own. It is my judgement, not a published figure, and the call turns on it."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_commit.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_annual.png"></div></div>')
A(caption("Left: supply and capacity commitments at each quarter end, and the cap on land, power and shell guarantees at 26 July 2026 "
          "(CFO commentaries; Form 8-K of 17 August 2026). Right: revenue by fiscal year, Data Center and the rest, with EPS (GAAP to FY26, "
          "non-GAAP after) and the FY28 consensus revenue (red); FY27 to FY29 are my estimates."))
A('</div>')
A(para("<strong>The other three claims: Nvidia holds the rest of the chain.</strong> On memory, its commitments rose from US$119bn to "
       "US$279bn in one quarter, \"primarily related to the procurement of memory\", with US$87bn due in FY28. Its NVHBM design (26 August) "
       "puts Nvidia's controller in the base of each memory stack, \"available from multiple memory providers\": Nvidia draws the part and "
       "chooses the maker. On the rack, Nvidia sets the 800 volt design and dates its power rack to the second half of 2026 and its row "
       "power centre to 2027, the building step undated, so new racks can go into halls whose power rooms already exist. On the network, "
       "its Vera Rubin blueprints still specify pluggable switches; networking was US$14.8bn of US$75.2bn of Data Center revenue in the "
       "quarter to April, the last quarter with the split."))
A(para("I checked each Nvidia fact the four pieces rely on against Nvidia's filings and releases, and none needs correcting. The pieces "
       "and claims stay exactly as published."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:,.2f} Nvidia is worth about US${MCAP / 1000:.2f} trillion, with US${NETCASH:.1f}bn more cash and debt securities "
       f"than debt. The shares closed at a high of US${HI_CLOSE:.2f} on 6 October (intraday US${HI52:.2f}) and are "
       f"{abs(OFF_HIGH) * 100:.1f}% below it. They trade at {PE27:.0f} times my FY27 EPS of US${EPS27:.2f}, which matches the "
       f"US${CONS_EPS_27:.2f} consensus, and at {PEC28:.1f} times the FY28 consensus. Twelve to thirteen times next year's consensus is low "
       "for a company still doubling its main business: the market does not believe the consensus will last."))
A(para(f"<strong class='lead'>Against consensus.</strong> Consensus needs the gigawatts equipped with Nvidia systems to rise about half in "
       f"a year. My FY28 revenue is US${pb['rev28']:.0f}bn, {abs(REV28_VS_CONS) * 100:.0f}% below consensus, and EPS US${pb['eps28']:.2f}, "
       f"{abs(EPS28_VS_CONS) * 100:.0f}% below. <strong class='lead'>Against the price.</strong> By October 2027 the market will price FY29, "
       f"the year to January 2029. At {M_BASE} times, US${PRICE:,.2f} needs FY29 EPS of US${NEED_EPS29:.2f}. If gigawatts and revenue per "
       f"gigawatt both stopped rising after FY28, my model gives US${eps29_flat(0.0):.2f}. The price assumes growth roughly stops after "
       "next year; the physical layer says it slows. Equipment makers are adding plants, Nvidia is paying to bring 4.25 GW forward, and "
       "each generation earns more per gigawatt."))
A(para(f"<strong class='lead'>The obvious objection</strong> is that chips already ship ahead of the power to run them. Receivables "
       f"reached US${AR_Q2:.1f}bn in July, {DSO_Q2} days of sales against {DSO_Q1}, on \"extended payment terms on large, multi-quarter "
       "agreements\"; the 10-Q says such terms run from 90 days up to a year for large data centre builds. If systems are reaching halls not "
       "yet energised, a pause follows. That is the bear case, and why the first test of the call is a quarter of falling Data Center revenue."))

A(section("Valuation, with the working"))
A(para("I value Nvidia on EPS: it holds more cash than debt and its profit converts largely to cash. Revenue in my model is gigawatts "
       "equipped times revenue per gigawatt, plus edge devices. Base: gigawatts up 20% in FY28 and 15% in FY29, revenue per gigawatt up "
       f"15% and 10%, non-GAAP operating margin {pc(OM28, 0)} and {pc(OM29, 0)} as memory costs rise (the Q3 guide already steps gross "
       f"margin down a point to 74%), tax {pc(TAX)} and {SH29}bn shares. That gives FY29 EPS of US${pb['eps29']:.2f}. I use {M_BASE} times, "
       f"about today's {FWD_PE_SA:.1f} times forward multiple, rounded down: {usd(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "GW FY28, FY29", "US$/GW", "FY29 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "Chips outrun the power; growth stalls", "+5%, flat", "+10%, +5%", f"US${pbe['eps29']:.2f}", f"{SCEN[0][7]}x", usd(bear), chg(bear), "25%"],
        ["Base", "Power paces growth", "+20%, +15%", "+15%, +10%", f"US${pb['eps29']:.2f}", f"{SCEN[1][7]}x", usd(base), chg(base), "50%"],
        ["Bull", "Consensus pace arrives", "+50%, +30%", "+15%, +10%", f"US${pbu['eps29']:.2f}", f"{SCEN[2][7]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7, 8}, total_row_idx=3,
), [9, 27, 11, 10, 9, 8, 9, 9, 8]))
A(caption(f"Operating margins: bear 60% and 59%, base 63% and 62%, bull 64%. The bull case gives FY28 EPS of US${pbu['eps28']:.2f}, close "
          f"to the US${CONS_EPS_28:.2f} consensus. Gigawatts: bear {pbe['gw29']:.1f}, base {pb['gw29']:.1f}, bull {pbu['gw29']:.1f} GW in "
          "FY29. The bear case is not fanciful: the shares closed at US$149.43 on 6 January 2025 and at US$94.31 on 4 April 2025, 37% lower, and Nvidia's "
          "guarantees reach 4.7 times its net cash. The band: long when my base value is at least 15% above the price, short when at least "
          "25% below, no call in between."))
A('</div>')
above = sum(v > PRICE for r in VGRID for v in r)
above15 = sum(v > PRICE * 1.15 for r in VGRID for v in r)
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
A('<div class="keeptogether">')
A(section("Sensitivity: FY28 gigawatt growth against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["FY28 GW growth"] + [f"{m}x" for m in SENS_M],
    [[f"+{g * 100:.0f}%"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (g, r) in enumerate(zip(SENS_GW, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{NUMW[above].capitalize()} of the nine cells sit above today's price, and {NUMW[above15]} by more than 15%. The two below it both "
       f"need the multiple to fall to {SENS_M[0]} times, with growth of 20% or less; at {SENS_M[0]} times even 35% growth only matches the "
       "price. FY29 growth is held at 15% and every other input at the base. Every figure is live in the accompanying model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_valuation.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: value per share from the base case, the weighted cases, the sensitivity grid and the bear to bull range, against the "
          f"US${PRICE:,.2f} price (red) and the stockanalysis.com average analyst target. Right: NVDA month-end close, January 2024 to the "
          "30 October 2026 close (Nasdaq.com, retrieved 2 November 2026), against my base value."))
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [["Nvidia", "Nasdaq: NVDA", f"{FWD_PE_SA:.1f}x", "GPUs, rack-scale systems, NVLink, InfiniBand and Ethernet networking"]]
    + [[c, t, f"{p:.1f}x", w] for c, t, p, w in PEERS],
    num_cols={2},
), [20, 15, 12, 53]))
A(caption("Forward P/E from stockanalysis.com at the 30 October 2026 close, retrieved 2 November 2026. Five-peer median 19.1 times; "
          "Micron's multiple reflects peak memory earnings. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        [RESULTS_DATE, "Q3 FY27 results (quarter to 25 October)", "Data Center against the US$108.0bn total guide; gross margin against 74%; receivables and payment terms"],
        ["Around late February 2027 (expected)", "Q4 FY27 results and 10-K", "Supply commitments; guarantees; any new land, power and shell deals"],
        ["March 2027", "GTC", "A date for the DC power block and NVHBM; Kyber; Feynman's network"],
        ["From 2028", "First PORTS halls ready for service", "Whether 4.25 GW arrives on time, and the guarantees take effect"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Chips outrun the power.</strong> If buyers hold systems they cannot switch on, orders pause until halls catch up; longer "
       f"terms and higher receivables fit, though they prove nothing yet. This is the bear case, a {abs(bear / PRICE - 1) * 100:.0f}% fall. "
       f"<strong>The guarantees.</strong> Up to US${GUAR_TOTAL:.1f}bn, {GUAR_TOTAL / NETCASH:.1f} times net cash; for Ohio, OpenAI has agreed "
       f"to reimburse Nvidia for any payment, so the exposure is to OpenAI's ability to pay. Nvidia also has US${AI_CLOUD_COMMIT:.0f}bn of AI "
       f"cloud agreements and US${LEASE_3P:.0f}bn of leases it expects to pass to others. <strong>Concentration and custom chips.</strong> "
       f"One direct customer took {TOP_CUST_Q2 * 100:.0f}% of revenue in the July quarter, and every large buyer designs chips of its own."))
A(para("<strong>Memory and margin.</strong> US$279bn of commitments, mostly memory, lock in costs as prices rise; a gross margin below 70% "
       "would mean Nvidia cannot pass them on. <strong>China.</strong> Nvidia's guides assume no Data Center compute revenue from China; "
       "any licence is upside I do not count."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Out of the long:</strong> a price above about US${BASE_VALUE / 1.15:,.0f} with my numbers unchanged, which leaves the "
       "base less than 15% above it; or evidence that powered gigawatts for Nvidia grow 10% or less while the multiple falls towards "
       f"{SENS_M[0]} times. <strong>Into more conviction:</strong> a grid operator or equipment maker showing the queues shortening, or the "
       "first PORTS halls ready early, would move the base towards the bull case."))
A(para(f"<strong>The call is wrong if</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para("The pieces this note rests on argue that power, not chips, sets the pace of AI. Nvidia's filings now agree: it lists energy among "
       "its demand risks and guarantees its customers' land, power and buildings. On its own PORTS yardstick its revenue already equips "
       f"about {GW27:.0f} gigawatts a year, and consensus needs half as much again next year. I do not believe that pace, and my FY28 EPS "
       f"is {abs(EPS28_VS_CONS) * 100:.0f}% below consensus. But the price goes further and assumes growth ends after next year. "
       f"{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {usd(tgt)}; base value {usd(BASE_VALUE)}, range "
       f"{usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY27E", "FY28E", "FY29E", "Basis"],
    [
        ["Revenue, US$bn", f"{REV27:.1f}", f"{pb['rev28']:.1f}", f"{pb['rev29']:.1f}", "FY27: two quarters, the Q3 guide and my Q4 of US$122bn"],
        ["Growth in GW equipped", "", pc(G_GW[0], 0), pc(G_GW[1], 0), "Mine: the pace of the queues, plus idle energised halls and on-site power"],
        ["Rise in revenue per GW", "", pc(G_USD[0], 0), pc(G_USD[1], 0), "Mine: Vera Rubin began production shipments in Q3 FY27 (10-Q)"],
        ["Revenue per GW, US$bn", f"{USD_GW_27:.1f}", f"{USD_GW_28:.1f}", f"{USD_GW_29:.1f}", "PORTS midpoint set to FY29; earlier years deflated (mine)"],
        ["Edge Computing, US$bn", f"{EDGE27:.1f}", f"{EDGE28:.0f}", f"{EDGE29:.0f}", "Q1 and Q2 reported; mine after"],
        ["Non-GAAP operating margin", pc(OM27), pc(OM28, 0), pc(OM29, 0), "Q2 66.5%; Q3 guide implies 65.7%; memory costs (mine)"],
        ["Tax rate (non-GAAP)", pc(TAX), pc(TAX), pc(TAX), "Guide 16% to 18% for FY27"],
        ["Diluted shares, bn", f"{SH27_Q3Q4} (H2)", f"{SH28}", f"{SH29}", "Buybacks net of dilution (mine)"],
        ["Multiple on FY29 EPS", "", "", f"{M_BASE}x", f"Forward P/E {FWD_PE_SA:.1f}x, rounded down"],
    ],
), [26, 10, 9, 9, 46]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Nvidia CFO commentaries for Q3 FY25 to Q2 FY27, with comparative columns, for revenue, Data Center and '
  'sub-market revenue, non-GAAP margins and EPS, commitments, guarantees, balance sheet and the Q3 FY27 outlook. Nvidia Form 10-K for '
  'the year to 25 January 2026 (filed 25 February 2026): memory suppliers and demand risk factors. Form 10-Q for the quarter to 26 July '
  '2026 (filed 26 August 2026): balance sheet, shares outstanding, payment terms, customer concentration, Vera Rubin production shipments '
  'and the SB Energy guarantees. Form 8-K of 17 August 2026 (PORTS campus). Nvidia release of 28 October 2026 (results date). Nvidia '
  'blogs of 11 August 2026 (800 VDC) and 26 August 2026 (NVHBM) and the DGX SuperPOD Vera Rubin reference architectures (15 September '
  '2026), as cited in the journal pieces, which also give the ERCOT, GE Vernova, Nebius, Tenaga and equipment backlog figures. Share '
  'prices from Nasdaq.com historical data; consensus, average target and multiples from stockanalysis.com; all retrieved 2 November 2026. '
  'Gigawatt translations and estimates for FY27 to FY29 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests claims from my journal pieces, chiefly '
  '<a href="https://thephysicallayer.fyi/journal/contracted-energised-running/">thephysicallayer.fyi/journal/contracted-energised-running</a>, '
  'with <a href="https://thephysicallayer.fyi/journal/memory-not-maths/">memory-not-maths</a>, '
  '<a href="https://thephysicallayer.fyi/journal/powering-the-rack/">powering-the-rack</a> and '
  '<a href="https://thephysicallayer.fyi/journal/ten-thousand-chips-one-thought/">ten-thousand-chips-one-thought</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Nvidia. Personal research, not investment advice.</p>')
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
