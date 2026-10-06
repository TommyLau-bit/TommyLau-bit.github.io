# -*- coding: utf-8 -*-
"""Oklo (NYSE: OKLO) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/oklo.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Oklo (NYSE: OKLO)"
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


def usd(x, d=2):
    return f"US${x:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = usd(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
call_word = "no call" if CALL["direction"] == "NO CALL" else CALL["direction"]
flat = [v for r in GRID for v in r]
FALL = {k: 1 - v[1] / v[0] for k, v in PEER_FALL.items()}

A('<h1 class="doctitle">Oklo Inc.</h1>')
A('<p class="docsubtitle"><b>NYSE: OKLO | Aurora sodium-cooled fast reactors it intends to own, selling the power | Santa Clara, California</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:.2f} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:.2f}, NYSE close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:.2f}"),
    ("Market value", f"About US${MCAP / 1000:.1f}bn on at least {SH_SEP:.1f}m shares (10 Sep 2026)"),
    ("Cash and securities", f"US${CASH_JUN / 1000:.2f}bn at 30 Jun 2026; my estimate US${NETCASH_NOW / 1000:.2f}bn at 30 Sep; no debt to speak of"),
    ("Enterprise value", f"About US${EV / 1000:.1f}bn; market value {MCAP / NETCASH_NOW:.1f}x cash"),
    ("Fully diluted shares", f"{FD:.1f}m with {OPTIONS:.1f}m options and {RSUS:.1f}m share units"),
    ("2026 guide (7 Aug)", "Operating cash use US$120 to 150m; capital spending US$400 to 500m"),
    ("Consensus", f"{CONS_N} analysts, average target US${CONS_TP:.2f} (stockanalysis.com); 2026 loss per share US${-CONS_EPS_26:.2f}; {SHORT_PCT:.0f}% of shares sold short"),
    ("Binding PPAs", "None on my reading of the filings. Switch 12 GW master agreement; Meta 1.2 GW prepayment agreement"),
    ("Next results", "Q3 2026: date not yet announced; last year 11 Nov"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Oklo sells electricity it has not yet made. At US${PRICE:.0f}, the shares price a bigger fleet than all the customers it has announced.</p>')
A(para("Oklo designs Aurora, a 75 MW sodium-cooled fast reactor, and plans to own each plant and sell its power for decades. "
       "On 29 September I argued that the model stands or falls on building the first plant. The model has held, Groves went "
       "critical in August and Aurora-INL is targeted for 2028. But no customer has signed a binding power purchase agreement, "
       "and Oklo has not disclosed what a plant costs."))
A(para(f"Shareholders pay for the build: US${RAISED_H1_26 / 1000:.2f}bn net in the first half and about US${ATM_Q3_GROSS:.0f}m "
       f"more by 10 September, at prices that fell from US${ATM_H1[0][3]:.0f} to about US${ATM_Q3_AVG:.0f}. On my base plant "
       f"economics the price needs about {NEED_GW:.0f} GW running by 2040, against {PIPE_GW:.1f} GW of announced customers."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {usd(tgt, 0)}.</b> The target is my "
       f"probability-weighted value, {usd(WEIGHTED)}. My base case is worth {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, but it rests on a "
       f"plant cost and a power price Oklo does not disclose. The bear case is {usd(bear)} ({chg(bear)}) and the bull case "
       f"{usd(bull)} ({chg(bull)}), which is why conviction is low."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials"))
A(datatable(
    ["US$ million unless stated", "2024A", "2025A", "H1 2026A", "2026 guide", "2026E*", "2027E*"],
    [
        ["Revenue", "0", "0", f"{H1['rev']:.1f}", "", f"{CONS_REV_26:.1f} (cons.)", ""],
        ["Operating loss", f"{-OPLOSS_H[0]:.1f}", f"{-OPLOSS_H[1]:.1f}", f"{-H1['oploss']:.1f}", "", "", ""],
        ["Net loss", f"{-NETLOSS_H[0]:.1f}", f"{-NETLOSS_H[1]:.1f}", f"{-H1['netloss']:.1f}", "", "", ""],
        ["Operating cash use", f"{-OCF_H[0]:.1f}", f"{-OCF_H[1]:.1f}", f"{-H1['ocf']:.1f}", "120 to 150", f"{OCF26}", f"{OCF27}"],
        ["Capital spending", f"{CAPEX_H[0]:.1f}", f"{CAPEX_H[1]:.1f}", f"{H1['capex']:.1f}", "400 to 500", f"{CAPEX26}", f"{CAPEX27}"],
        ["Net proceeds from share sales", "0", f"{RAISED_25:,.1f}", f"{RAISED_H1_26:,.1f}", "", f"{RAISED_H1_26 + ATM_Q3_NET:,.0f}", ""],
        ["Cash and securities, end", f"{CASHSEC_H[0]:,.1f}", f"{CASHSEC_H[1]:,.1f}", f"{CASH_JUN:,.1f}", "", f"{CASH_END26:,.0f}", f"{CASH_END26 - OCF27 - CAPEX27:,.0f}"],
        ["Shares outstanding, end (m)", f"{SH_H[0]:.1f}", f"{SH_H[1]:.1f}", f"{SH_JUN:.1f}", "", f"{SH_SEP:.1f}+", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E and 2027E spending and cash are my own estimates; 2026E revenue is the stockanalysis.com consensus. 2026E "
          f"cash adds the US${ATM_Q3_NET:.0f}m net raised from July to 10 September and excludes any sales under the US$1bn "
          "programme opened on 11 September. The guide was raised on 7 August from US$80 to 100m and US$350 to 450m. History "
          "from Oklo's 10-K and 10-Qs."))

A('<div class="keeptogether">')
A(section("Two charts: a cash pile built from shares, and a value below the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_cash.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: cash and marketable securities at quarter end and shares outstanding; Sep 26 is my estimate. Right: value per "
          "share from my base case, the weighted cases, the sensitivity grid and the bear to bull range, against the "
          f"US${PRICE:.2f} price (red) and the stockanalysis.com average target, retrieved 6 October 2026."))
A('</div>')

A(section("The thesis: the coffee supplier before its first machine"))
A(para("Go back to the coffee supplier from the September piece. It installs the machine, keeps owning it and charges for "
       "every cup. Now picture it before it has installed one. It has letters from offices that like the idea, no agreed price "
       "per cup, no firm cost for its own machine, and it pays its bills by selling slices of the company."))
A(para("<strong>That is Oklo today.</strong> Its 10-Q says the primary business model is to sell the energy, not the design. "
       "The 10-Q also says Oklo intends to offer customers \"flexibility in business model\" as the technology matures, and "
       "to raise capital at the corporate and asset levels. Neither is a reactor sale, so the first half of the claim stands. "
       "Oklo broke ground on Aurora-INL on 22 September 2025 under the Department of Energy, which approved its safety design "
       "agreement early in 2026 and its preliminary documented safety analysis on 11 June: two of five steps. Oklo then spoke of "
       "late 2027 or early 2028; it now targets 2028. Groves, its isotope test reactor in Texas, went critical on 5 August 2026."))
A(para("<strong>What is missing is the money per plant.</strong> Oklo has not disclosed what Aurora-INL costs; in August the "
       "finance chief said the total was still being narrowed with Kiewit, the lead constructor. Nor has it disclosed a power "
       "price. The only customer cash on its 30 June balance sheet is a US$25m payment from 2024 for a right of first refusal. "
       "On my reading, no megawatt is under a binding PPA. The 10-K says many of Oklo's master power agreements and letters of "
       "intent are non-binding, and that it is negotiating binding PPAs; the 10-Q calls the 12 GW Switch agreement one of the "
       "largest corporate PPAs in history, but no filing calls it binding. Meta's prepayment agreement of 5 January 2026, for "
       "1.2 GW in Ohio from as early as 2030 to 2034, is a mechanism to prepay for power; no amount is disclosed and it is not "
       "a PPA. Fuel beyond the first core rests on a Centrus letter of "
       "intent from 2029 and talks on surplus government plutonium."))

A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_spend.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_pipeline.png"></div></div>')
A(caption("Left: operating cash use plus capital spending by quarter, against the 2026 guide midpoint per quarter (Oklo 10-Qs "
          "and 10-K; quarters derived from year-to-date figures). Right: announced customer capacity by status (Oklo filings; "
          "Meta announcement of 9 January 2026), against my base fleet and the fleet the price needs at my base costs, by 2040."))
A('</div>')

A(section("Where I was wrong in September"))
A(para(f"In the piece I wrote that cash and marketable securities \"stood at $3.0 billion at 30 June, about $1.9 billion more "
       f"than at the start of the year, raised mainly by issuing new shares.\" The US$3.0bn was right; the rise was not. The "
       f"balance sheet shows US${CASH_DEC25:,.1f}m at 31 December 2025 and US${CASH_JUN:,.1f}m at 30 June 2026, a rise of about "
       f"US${CASH_RISE_H1 / 1000:.1f}bn. The US$1.9bn is what Oklo raised: US$1,880m gross and US${RAISED_H1_26:,.0f}m net. "
       f"The gap of about US${H1_OUT:.0f}m went out as US$65.5m of operating cash, US$126.9m of capital spending, US$25.7m on "
       "two acquisitions, US$16.5m of other investments and US$16.9m moved into restricted cash. Those add to about US$251.5m; "
       "most of the remaining US$7m is unrealised losses and accretion on the securities."))
A(para("What showed me the slip was rebuilding the cash bridge from the balance sheet and the cash flow statement, which I had "
       "not done for the piece. The view did not change: the gap between money raised and money kept is what Oklo spent running "
       "the business and building, US$126.9m of it on plant. The piece and the claim stay as published."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:.2f} Oklo is worth about US${MCAP / 1000:.1f}bn, {MCAP / NETCASH_NOW:.1f} times my estimate of its cash. "
       f"Part of the {FALL['OKLO'] * 100:.0f}% fall from the highest close is the group: NuScale fell {FALL['SMR'] * 100:.0f}% and "
       f"NANO Nuclear {FALL['NNE'] * 100:.0f}% over the same year. Part is Oklo's funding. It sold shares at an average of "
       f"US${ATM_H1[0][3]:.2f} in the first quarter, US${ATM_H1[1][3]:.2f} in the second and about US${ATM_Q3_AVG:.0f} from July to "
       f"10 September. On 11 September it opened another US$1bn programme, and the shares fell from US${PX_ATM[0]:.2f} to "
       f"US${PX_ATM[1]:.2f}. Shares outstanding are up {SH_RISE_2Y * 100:.0f}% since June 2024."))
A(para(f"<strong class='lead'>What the price needs.</strong> On my base economics each Aurora earns about "
       f"US${margin_mw(B[1]) * 1000:.0f}k a megawatt in its first year and is worth about US${npv_mw(B[1], B[2]):.2f}m a megawatt "
       f"more than it costs. To justify US${PRICE:.2f}, Oklo needs about {NEED_RATE / 1000:.1f} GW of new units a year from 2033 to "
       f"2040, about {NEED_GW:.0f} GW running by 2040, against {gw_2040(B[4]):.1f} GW in my base case and {PIPE_GW:.1f} GW of "
       f"announced customers, none under a PPA. At my base fleet the price instead needs plants at about US${NEED_CAPEX:,.0f} a "
       f"kilowatt, against my US${B[2]:,}."))
A(para(f"<strong class='lead'>Where I differ.</strong> Not on the claim, but on what is already in the price. The market prices "
       "Oklo as if a margin per plant were known. The one recent Western small-reactor costing I can check is Ontario's: "
       f"C${DARLINGTON[0]}bn for four 300 MW BWRX-300 units at Darlington, about C${round(DARL_KW, -2):,.0f} a kilowatt, and C${round(DARL1_KW, -2):,.0f} "
       "for the first with shared costs. Oklo's design is simpler and smaller; my base already assumes well under half of that. "
       f"Analysts are more positive: {CONS_N} have an average target of US${CONS_TP:.2f}."))

A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_plant.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: the cost per kW at which a 75 MW Aurora just earns back its cost, by first-year power price (my model: 90% "
          "capacity factor, US$35/MWh to run, 2% escalation, 40 years at 8%). Right: OKLO month-end close from listing in May "
          "2024 to the 5 October 2026 close (Yahoo Finance, retrieved 6 October 2026), with the average prices of the 2026 "
          "share sales (10-Q; 8-K of 11 September 2026) and my base value."))
A('</div>')

A(section("Valuation, with the working"))
A(para("Oklo has no earnings, so I value it plant by plant, twelve months out. <b>One plant:</b> 75 MW at 90% of capacity, "
       f"US${B[1]}/MWh, US${OPEX_MWH}/MWh to run including fuel and decommissioning, both rising 2% a year for 40 years, "
       f"discounted at 8%: about US${margin_mw(B[1]) * pvf():.2f}m a megawatt, less US${B[2]:,}/kW. Break-even is about "
       f"US${BREAKEVEN_CAPEX:,.0f}/kW. <b>The fleet:</b> Aurora-INL in mid-2028 with US${INL_REM}m still to spend after September "
       "2027; Meta's 1.2 GW from 2030 to 2034; then 300 MW a year to 2040. Each plant is discounted at 10% back to October "
       f"2027 and multiplied by a {B[3] * 100:.0f}% chance that Aurora-INL reaches commercial operation on that timetable. "
       f"<b>The company:</b> plus my cash at September 2027, US${CASH_SEP27 / 1000:.2f}bn, less US${PV_CORP / 1000:.2f}bn of "
       f"corporate, fuel, recycling and isotope spending in present value, over {FD:.1f}m diluted shares. No tax or tax credits."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "Price, cost", "P(first plant)", "Value", "Change", "Weight"],
    [
        ["Bear", "Aurora-INL slips past 2029 and the numbers do not close; no fleet; spending winds down", "US$95, US$10,000/kW", "n/a",
         usd(bear), chg(bear), "25%"],
        ["Base", "Aurora-INL in 2028; Meta's 1.2 GW by 2034; then 300 MW a year; 3.7 GW by 2040", "US$110, US$7,500/kW",
         f"{SCEN[1][3] * 100:.0f}%", usd(base), chg(base), "50%"],
        ["Bull", f"Cheap plants; Switch and others contract 900 MW a year from 2033; {gw_2040(SCEN[2][4]):.1f} GW by 2040",
         "US$125, US$6,000/kW", f"{SCEN[2][3] * 100:.0f}%", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", usd(WEIGHTED), chg(WEIGHTED), ""],
    ],
    num_cols={4, 5, 6}, total_row_idx=3,
), [9, 40, 15, 9, 10, 10, 7]))
A(caption(f"The bear case is close to cash: Oklo would still hold about US${CASH_VALUE:.2f} a share in September 2027, which "
          f"limits how far value falls in my three cases, though grid cells where new units do not pay go lower. The bull "
          f"case needs 7.2 GW beyond Meta contracted, 60% of the Switch agreement."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: cost per kW against power price"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Cost per kW"] + [f"US${p}/MWh" for p in SENS_PRICE],
    [[f"US${c:,}"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (c, r) in enumerate(zip(SENS_CAPEX, GRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"None of the nine cells reaches the price; the highest, cheap plants and dear power together, gives {usd(max(flat))}. "
       "Where new units do not pay, only Aurora-INL is built, so two cells share the same low value. What closes the gap to "
       "the price is scale, not margin. Every figure is live in the accompanying model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape: enterprise value per announced gigawatt"))
A(cols(datatable(
    ["Company", "Ticker", "EV, US$bn", "Announced GW", "EV per GW, US$bn", "What they make"],
    [[p[0], p[1], f"{ev / 1000:.2f}", (f"{p[5]:.1f}" if p[5] else "n/m"), (f"{e:.2f}" if e else "n/m"), p[6]]
     for p, ev, e in zip(PEERS, PEER_EV, PEER_EV_GW)],
    num_cols={2, 3, 4},
), [14, 13, 10, 11, 11, 41]))
A(caption("Closes of 5 October 2026 (Yahoo Finance); peer shares and net cash from stockanalysis.com, retrieved 6 October 2026; "
          "Oklo on my share count and cash. Announced GW is customer capacity under agreements, none under a binding PPA. On "
          "this measure Oklo is the cheapest of the group. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Early to mid Nov 2026 (not yet announced)", "Q3 2026 results", "Spending against the guide; sales under the September programme; any Aurora-INL cost"],
        ["Late 2026 to 2027", "Remaining DOE steps for Aurora-INL", "Three of five steps left; any change to the 2028 target"],
        ["Any time", "First binding PPA", "Megawatts, price per MWh and term: replaces my two largest assumptions"],
        ["Any time", "Centrus definitive agreement; plutonium allocation", "Firm fuel beyond the first core; fuel fabrication start-up in 2027"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The first plant slips or costs more.</strong> The claim's own test: Aurora-INL has already moved to 2028, and "
       "Oklo raised its 2026 spending guide in August citing first-of-a-kind costs. <strong>Dilution below value.</strong> My "
       "base fleet needs about US$27bn of plant spending by 2040; if shareholders fund their part at prices below what the plants "
       "are worth, existing holders lose even if the plants work. <strong>The contracts stay paper.</strong> Twenty-two months "
       "after the Switch agreement, on my reading, no megawatt is under a binding PPA."))
A(para("<strong>The risks to the short, and why conviction is low.</strong> The two decisive inputs are undisclosed, so my base case is an assumption stack. "
       f"A binding PPA at a good price, a plutonium allocation or a low disclosed cost could each move the shares sharply, and "
       f"{SHORT_PCT:.0f}% of them are already sold short. Oklo is also the cheapest of the group per announced gigawatt."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Towards higher conviction:</strong> a disclosed Aurora-INL cost implying more than about US$10,000/kW, or "
       f"another share sale below my weighted value. <strong>Out of the short:</strong> a binding PPA of 500 MW or more, a "
       f"disclosed cost at or below about US$6,000/kW with an NRC licence application accepted for a commercial site, or a close "
       f"above US$60. Below about US${REVISIT_LONG:.0f}, my base value, the short has done its work and I would close it."))
A(para("<strong>The short is wrong if,</strong> by October 2027, Oklo signs a binding power purchase agreement for 500 MW or "
       "more; or discloses an Aurora-INL cost at or below US$6,000/kW and the NRC accepts a licence application for a "
       "commercial site; or the shares close above US$60, on the path to my bull case."))
A('</div>')

A(section("Conclusion"))
A(para("The September piece argued that Oklo sells electricity, not reactors, and that the model stands or falls on building "
       "its first plant. Both halves hold: Oklo has kept to its model, broken ground in Idaho and taken Groves critical. But no "
       "customer has signed a binding contract, no plant cost has been disclosed, and shareholders are paying for the build. I "
       f"was wrong about one figure: cash rose about US$1.6bn in the first half, not US$1.9bn. At US${PRICE:.2f} the price needs "
       f"about {NEED_GW:.0f} GW running by 2040 at my base costs. {my_call}: {call_word}, {CALL['conviction'].lower()} "
       f"conviction, twelve-month target {usd(tgt, 0)}, my probability-weighted value; base value {usd(BASE_VALUE)}, range "
       f"{usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: valuation assumptions"))
A(cols(datatable(
    ["Assumption", "Bear", "Base", "Bull", "Basis"],
    [
        ["Power price, US$/MWh, first year", "95", "110", "125", "Mine; Oklo has disclosed no price"],
        ["Plant cost, US$/kW", "10,000", "7,500", "6,000", f"Mine; Darlington about C${round(DARL_KW, -2):,.0f}/kW"],
        ["P(Aurora-INL runs on time)", "0%", "60%", "80%", "Mine; Oklo targets 2028"],
        ["Further units, MW a year 2033 to 2040", "0", "300", "900", "Mine; Switch 12 GW, not binding on my reading"],
        ["Capacity factor; running cost", "", "90%; US$35/MWh", "", "Mine"],
        ["Discount: plant; to Oct 2027", "", "8%; 10%", "", "Mine"],
        ["Corporate spending from Oct 2027, US$m a year", "150 x 3", "250 x 4, 150 x 5", "same", "Mine; 2026 guide US$520 to 650m in all"],
    ],
), [30, 10, 15, 10, 35]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Oklo Form 10-Q for the quarter to 30 June 2026 (filed 7 August 2026) for the financial statements, share '
  'sales, acquisitions, the right of first refusal payment, customer agreements, the Meta prepayment agreement, the Centrus letter '
  'of intent, DOE and NRC status and Groves. Form 10-Q/A for Q1 2026 (17 June 2026; certification only). Form 10-K for 2025 '
  '(17 March 2026) for non-binding agreements and 2025 figures. Form 8-K and prospectus supplement of 11 September 2026 for the '
  'end of the May 2026 programme, the new US$1bn programme, options and share units. SEC XBRL company facts for quarterly '
  'history. Second quarter 2026 business update and call (7 August 2026). Oklo and Meta announcement (9 January 2026); Oklo '
  'groundbreaking (22 September 2025); Q3 2025 date notice (29 October 2025). OPG Darlington approval (8 May 2025). '
  'stockanalysis.com and Yahoo Finance, retrieved 6 October 2026. Estimates are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 29 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/oklo-sells-the-electricity/">thephysicallayer.fyi/journal/oklo-sells-the-electricity</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Oklo. Personal research, not investment advice.</p>')
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
