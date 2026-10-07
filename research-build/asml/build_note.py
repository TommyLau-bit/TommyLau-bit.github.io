# -*- coding: utf-8 -*-
"""ASML Holding N.V. (Euronext Amsterdam: ASML) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/asml.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "ASML Holding N.V. (Euronext Amsterdam: ASML)"
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


def m0(x):
    return f"{x:,.0f}"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = eur(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {eur(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = ("My draft view" if CALL["draft"] else "My call")
need_eps_long = PRICE * 1.15 / MULT
need_eps_short = PRICE * 0.75 / MULT
above = sum(v > PRICE for r in VGRID for v in r)
above15 = sum(v >= PRICE * 1.15 for r in VGRID for v in r)
below25 = sum(v <= PRICE * 0.75 for r in VGRID for v in r)
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

A('<h1 class="doctitle">ASML Holding N.V.</h1>')
A('<p class="docsubtitle"><b>Euronext Amsterdam: ASML | Nasdaq: ASML | Lithography systems (EUV and DUV), metrology, installed base service and upgrades | Veldhoven, the Netherlands</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"€{PRICE:,.2f} (Euronext Amsterdam close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"€{PRICE:,.2f}, close {PRICE_DATE}; Nasdaq ADR US${ADR_PRICE:,.2f}; past-year closes €{LO_CLOSE:,.2f} to €{HI_CLOSE:,.2f}"),
    ("Market value", f"About €{MCAP:,.1f}bn on {SHARES_OUT:,.1f}m shares; EV €{EV:,.1f}bn"),
    ("Cash less long-term debt", f"€{NET_CASH / 1000:.1f}bn, 28 June 2026"),
    ("P/E on consensus", f"{PE_C26:.1f}x 2026, {PE_C27:.1f}x 2027 (Zacks, converted); peers {PEER_MED:.1f}x on FY ending 2027"),
    ("2026 guide (15 Jul)", "Total net sales €43bn to €45bn; gross margin 54% to 56%; about 65 low NA EUV shipped"),
    ("Capacity", "Low NA EUV 65 (2026), about 85 planned (2027), 110 under study (2028)"),
    ("2030 (Investor Day 2024)", "Revenue €44bn to €60bn; gross margin 56% to 60%; update at CMD on 10 June 2027"),
    ("Next results", f"Q3 2026 on {Q3_DATE} (ASML financial calendar)"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">ASML\'s machines are booked to 2027, so its earnings are unusually visible. At €{PRICE:,.2f}, the price already pays for them.</p>')
A(para("ASML is the only maker of EUV lithography machines, which print the finest layers of AI chips. On 7 October I argued they "
       "are sold out and booked a year or two ahead, and grow only about 30% a year. The July results support it: about 65 low NA "
       "machines ship in 2026, equal to capacity, and the planned 85 for 2027 are close to fully covered with orders."))
A(para(f"That makes the next two years unusually visible: my 2027 EPS of €{EPS27:.2f} is within {abs(EPS27 / CONS_EPS_27 - 1) * 100:.0f}% "
       f"of consensus. The question is the multiple. At {MULT} times 2028 earnings, the price needs about {NEED_UNITS:.0f} low NA machines "
       f"in 2028, between the 85 planned for 2027 and the 110 ASML is investigating. I take {LNA_U[2]}."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction.</b> My base value, {MULT} times 2028E EPS of "
       f"€{EPS28:.2f}, is {eur(BASE_VALUE)}, {chg(BASE_VALUE)}, inside my no-call band. The bear case is {eur(bear)} ({chg(bear)}) and the "
       f"bull case {eur(bull)} ({chg(bull)}). On earnings the shares look roughly fairly priced; a DCF falls below the price only on "
       f"below-history cash conversion ({eur(DCF_VALUE)} at 95%, {eur(DCF_VALUE_HIST)} at 2025's 115%)."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (US GAAP; calendar years)"))
A(datatable(
    ["€ million unless stated", "2024A", "2025A", "H1 2026A", "2026E*", "2027E*", "2028E*"],
    [
        ["Low NA EUV units", f"{NXE_U[1]}", f"{NXE_U[2]}", "", f"{LNA_U[0]}", f"{LNA_U[1]}", f"{LNA_U[2]}"],
        ["EUV system sales", m0(EUV_H[1]), m0(EUV_H[2]), "", m0(Y26['euv']), m0(Y27['euv']), m0(Y28['euv'])],
        ["DUV and metrology systems", m0(NONEUV_H[1]), m0(NONEUV_H[2]), "", m0(Y26['noneuv']), m0(Y27['noneuv']), m0(Y28['noneuv'])],
        ["Installed Base Management", m0(IBM_H[1]), m0(IBM_H[2]), m0(H1['ibm']), m0(Y26['ibm']), m0(Y27['ibm']), m0(Y28['ibm'])],
        ["Total net sales", m0(REV_H[1]), m0(REV_H[2]), m0(H1['rev']), m0(Y26['rev']), m0(Y27['rev']), m0(Y28['rev'])],
        ["Gross margin (%)", pc(GP_H[1] / REV_H[1]), pc(GP_H[2] / REV_H[2]), pc(H1['gp'] / H1['rev']), pc(Y26['gm']), pc(Y27['gm']), pc(Y28['gm'])],
        ["Income from operations", m0(EBIT_H[1]), m0(EBIT_H[2]), m0(H1['ebit']), m0(Y26['ebit']), m0(Y27['ebit']), m0(Y28['ebit'])],
        ["Diluted EPS (€)", f"{EPS_DIL_H[1]:.2f}", f"{EPS_DIL_H[2]:.2f}", "14.73", f"{EPS26:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}"],
        ["Consensus EPS (€)", "", "", "", f"{CONS_EPS_26:.2f}", f"{CONS_EPS_27:.2f}", "n/v"],
        [f"P/E at €{PRICE:,.2f} (x)", f"{PRICE / EPS_DIL_H[1]:.1f}", f"{PRICE / EPS_DIL_H[2]:.1f}", "", f"{PE26:.1f}", f"{PE27:.1f}", f"{PE28:.1f}"],
        ["China, share of total net sales", pc(CHINA_SH[1]), pc(CHINA_SH[2]), "", "about 20%", "", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E to 2028E are my own estimates. Units for 2024 and 2025 are low NA systems recognised in sales; 2026 and 2027 are "
          "shipments equal to capacity. Consensus is Zacks EPS for the ADR in US$, converted at the ECB rate of 6 October 2026 "
          f"(stockanalysis.com has €{CONS_EPS_26_SA:.2f} for 2026); n/v: 2028 consensus not verified. History from the 2025 20-F and the Q2 2026 6-K."))

A('<div class="keeptogether">')
A(section("Two charts: the count behind the claim, and a value close to the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_units.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: EUV systems recognised in sales 2020 to 2025 (including High NA), then ASML's low NA capacity: 65 in 2026, about 85 "
          f"planned for 2027, 110 under study for 2028; my base is {LNA_U[2]}. Right: value per share from the scenarios, the sensitivity "
          f"grid, the DCF at 95% and 115% cash conversion and the weighted case, against the €{PRICE:,.2f} price (red) and the average analyst target converted to euros."))
A('</div>')

A(section("The thesis: one workshop, its ovens promised a year ahead"))
A(para("One workshop in the whole country makes the special oven every bakery needs. Next year's ovens are already promised, and it "
       "can add only a few each year, as fast as its glassmaker can make oven doors. For an owner of the workshop, demand is not the "
       "unknown for two years. The unknowns are how many ovens, at what price, and what it earns servicing ovens already sold."))
A(para("<strong>The count is set.</strong> ASML expects to ship about 65 low NA EUV machines in 2026, equal to capacity. It plans "
       "about 85 for 2027 and is \"close to being fully covered with orders\". For 2028 it holds \"a significant number\" of orders and "
       "is investigating 110, which the finance chief called pre-empting demand, as transcribed. Each step comes from the existing footprint. "
       "ASML is not claiming a shortage: Christophe Fouquet said \"the capacity is there to meet the demand but the demand is still "
       "fluctuating\", the main counterpoint to booked. "
       f"<strong>The price per machine is rising:</strong> low NA sales per system rose from €{NXE_ASP_H[1]:.0f}m in 2024 to "
       f"€{NXE_ASP_H[2]:.0f}m in 2025, my arithmetic, as the NXE:3800E took over; four High NA machines averaged €{EXE_ASP_25:.0f}m."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_mix.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_quarters.png"></div></div>')
A(caption("Left: total net sales by segment, 2023 to 2028E, against the 2030 range from the November 2024 Investor Day; 2026E to 2028E "
          "are my estimates. Right: net system sales and Installed Base Management by quarter, with gross margin; Q3 2026 is the guide "
          "(midpoint for sales)."))
A('</div>')
A(para(f"<strong>The installed base pays twice.</strong> Installed Base Management grew 26.2% in 2025 to €8.2bn and "
       f"{IBM_G_H126 * 100:.1f}% in the first half of 2026. In Q2 it beat guidance by almost €300m, \"driven primarily by additional "
       "upgrade business\", and its \"very high margin components\" lifted gross margin to 54.0%. As my piece noted, NXE:3800E field "
       "upgrades moved \"a substantial portion of EUV system revenue\" into this line. An upgrade adds wafers per hour to a machine "
       "already installed, the one way round the queue. In 2025 systems earned a "
       f"{SYS_GM_H[2] * 100:.1f}% gross margin and the installed base {IBM_GM_H[2] * 100:.1f}%, my arithmetic from the cost lines."))
A(para("<strong>The supplier behind it.</strong> ASML bought €4.4bn from Carl Zeiss SMT in 2025, against €3.3bn in 2023, and owns "
       "24.9% of the ZEISS holding company. <strong>Not everything is EUV.</strong> DUV and metrology brought €12.9bn in 2025 and are "
       "guided up about 25% this year. China took 36.1% of total net sales in 2024 and 29.1% in 2025; ASML expects around 20% in 2026. "
       "<strong>Customers are few:</strong> four each took over 10% of 2025 sales, together 61.2%. ASML does not name them; Taiwan and "
       "South Korea each took about a quarter. I checked the piece's figures against the 20-F, the releases and ASML's transcript; they stand."))

A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_china.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: China as a share of total net sales, from the 2025 20-F, and ASML's 2026 expectation. Right: ASML month-end close on "
          "Euronext Amsterdam, October 2024 to the 6 October 2026 close (retrieved 7 October 2026; Euronext gives two years), against my base value."))
A('</div>')

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"<strong class='lead'>The price.</strong> ASML trades at {PE_C26:.1f} times 2026 and {PE_C27:.1f} times 2027 consensus, and "
       f"at {EV_EBIT27:.1f} times my 2027 income from operations on enterprise value. On the ADR it trades at {PE_ADR27:.1f} times "
       f"consensus for 2027, below the {PEER_MED:.1f} times median of Applied Materials, Lam Research, KLA and Tokyo Electron for "
       "their fiscal years ending in 2027. Those end two to nine months earlier, so on calendar 2027 their multiples would be lower and the "
       "gap narrower. The obvious objection is that the only EUV maker "
       "deserves a premium. My answer: its growth is booked, and it is capped at steps of about 30% a year. The market prices a known path."))
A(para(f"<strong class='lead'>What the price needs.</strong> In October 2027 the market will price 2028. At {MULT} times, "
       f"€{PRICE:,.2f} needs 2028 EPS of €{NEED_EPS:.2f}: about {NEED_UNITS:.0f} low NA machines with my other base assumptions. I take "
       f"{LNA_U[2]}. On the next two years I barely differ: my 2027 EPS is {abs(EPS27 / CONS_EPS_27 - 1) * 100:.1f}% below consensus."))
A(para(f"<strong class='lead'>Where I differ.</strong> After 2028. On my numbers ASML reaches €{Y28['rev'] / 1000:.1f}bn of revenue "
       "in 2028, the top of the €44bn to €60bn range it gave for 2030, two years early. A DCF at an 8.5% cost of equity gives "
       f"{eur(DCF_VALUE)} with free cash flow at {FCF_CONV * 100:.0f}% of net income, and {eur(DCF_VALUE_HIST)} at the "
       f"{FCF_CONV_HIST * 100:.0f}% of 2025. At {FCF_CONV_HIST * 100:.0f}%, the price needs net income to grow about "
       f"{DCF_NEED_G_HIST * 100:.0f}% a year from 2029 to 2032 ({DCF_NEED_G * 100:.0f}% at {FCF_CONV * 100:.0f}%). The "
       "Capital Markets Day on 10 June 2027 is where ASML will say whether the next leg is there."))

A(section("Valuation, with the working"))
A(para(f"I value ASML on {MULT} times 2028E EPS and build revenue by segment. <strong>2026E</strong>: EUV +{EUV_G26 * 100:.0f}% "
       f"(guide over 45%), non-EUV +{NONEUV_G26 * 100:.0f}%, installed base +{IBM_G26 * 100:.0f}%: €{Y26['rev'] / 1000:.1f}bn, the middle "
       f"of the guide, a {GM[0] * 100:.1f}% gross margin and EPS of €{EPS26:.2f}. <strong>2027E</strong>: 85 low NA at €{Y27['asp']:.0f}m, "
       f"{HNA_U[1]} High NA at €{HNA_ASP:.0f}m, non-EUV +{NONEUV_G[0] * 100:.0f}%, installed base +{IBM_G[0] * 100:.0f}%: "
       f"€{Y27['rev'] / 1000:.1f}bn, {GM[1] * 100:.1f}%, EPS €{EPS27:.2f}. <strong>2028E</strong>: {LNA_U[2]} low NA at "
       f"€{Y28['asp']:.0f}m, {HNA_U[2]} High NA: €{Y28['rev'] / 1000:.1f}bn, {GM[2] * 100:.1f}%, EPS €{EPS28:.2f}."))
A(para(f"<strong>The multiple.</strong> At the end of 2024 the shares traded at {FWD_PE_DEC24:.1f} times the EPS ASML then earned in "
       f"2025; today {PE27:.1f} times my 2027. One year on, my EPS growth slows from {(EPS27 / EPS26 - 1) * 100:.0f}% to "
       f"{(EPS28 / EPS27 - 1) * 100:.0f}%, so I take {MULT} times. On the base value, EV is {EV_EBIT28_BASE:.1f} times 2028E income "
       "from operations."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens in 2028", "Low NA units", "Gross margin", "P/E", "EPS 2028E", "Value", "Change", "Weight"],
    [
        ["Bear", "Memory and China digest; no step; DUV -10%", f"{SCEN[0][1]}", pc(SCEN[0][6]), f"{SCEN[0][7]}x", f"€{SV[0]['eps']:.2f}", eur(bear), chg(bear), "25%"],
        ["Base", "One more step, short of the 110 under study", f"{SCEN[1][1]}", pc(SCEN[1][6]), f"{SCEN[1][7]}x", f"€{SV[1]['eps']:.2f}", eur(base), chg(base), "50%"],
        ["Bull", "110 machines, richer mix, High NA ramps", f"{SCEN[2][1]}", pc(SCEN[2][6]), f"{SCEN[2][7]}x", f"€{SV[2]['eps']:.2f}", eur(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", "", eur(WEIGHTED), chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7, 8}, total_row_idx=3,
), [9, 30, 9, 9, 6, 10, 9, 10, 8]))
A(caption("2026 and 2027 are the same in all three cases, because 2027 output is close to fully covered with orders. The band: long "
          "when my base value is at least 15% above the price, short when it is at least 25% below, no call in between."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 low NA units against the P/E"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["2028 low NA units"] + [f"{x}x" for x in SENS_X],
    [[f"{u}"] + [(f"<b>{eur(v)}</b>" if (i == 1 and j == 1) else eur(v)) for j, v in enumerate(r)]
     for i, (u, r) in enumerate(zip(SENS_U, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{NUMW[above].capitalize()} of the nine cells sit above the price, but only {NUMW[above15]} clear it by 15% or more, both at "
       f"{SENS_X[2]} times with {SENS_U[1]} or {SENS_U[2]} machines. {NUMW[below25].capitalize()} sits 25% below. The multiple moves the "
       "value more than the count, as a booked order book should. The DCF, at 8.5% and 3% terminal growth, gives "
       f"{eur(DCF_VALUE)} at my {FCF_CONV * 100:.0f}% cash conversion, below 2024's 120% and 2025's 115%, and {eur(DCF_VALUE_HIST)} at "
       f"115%. It sits below the price mainly because my conversion is below history. Every figure is live in the model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Listing", "Year end", "P/E FY ending 2027", "What they make"],
    [["ASML (ADR)", "Nasdaq: ASML", "Dec 2027", f"{PE_ADR27:.1f}x", "Lithography systems, metrology, installed base service and upgrades"]]
    + [[c, t, ye, f"{px / e:.1f}x", w] for c, t, px, e, cur, ye, srcn, w in PEERS],
    num_cols={3},
), [20, 16, 11, 14, 39]))
A(caption("Closes of 6 October 2026 over consensus EPS for the fiscal year ending in 2027: Zacks for the US listings, stockanalysis.com "
          f"(S&P Global) for Tokyo Electron; retrieved 7 October 2026. Peer median {PEER_MED:.1f} times. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        [Q3_DATE, "Q3 2026 results", "2027 and 2028 order coverage; China; Q4 implied by the €43bn to €45bn guide"],
        ["Late January 2027 (not confirmed)", "Q4 and full year 2026 results", "Whether 2027 is still close to fully covered; 2028 capacity"],
        [CMD_DATE, "Capital Markets Day", "New long-term targets to replace the 2030 range"],
        ["Any time", "Export controls (MATCH Act, US enquiries)", "DUV to China; service on installed tools"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>China and export controls.</strong> China falls to around 20% of sales this year. The 20-F says export control changes "
       "\"may have a material impact\" on volume, mix and timing. The MATCH Act, introduced in Congress on 2 April 2026, would ban DUV "
       "immersion sales to China and require licences to service tools in covered Chinese fabs, which reaches Installed Base Management "
       "too; TrendForce reported on 17 April that a revised version dropped some curbs but kept both. In June Bloomberg reported US concerns "
       "that an EUV system may have reached China; ASML told Reuters it has \"never shipped an EUV machine to China\". No evidence has been "
       "made public. <strong>Few customers, one cycle.</strong> Four "
       "customers took 61.2% of 2025 sales, and memory system sales are guided up over 75% this year. If DRAM prices turn, the 2028 step "
       "goes first."))
A(para("<strong>Fewer machines per layer.</strong> High NA saves fab space by \"requiring fewer systems overall\", and faster low NA "
       "machines and upgrades do the same. <strong>ZEISS.</strong> A shortfall caused by ZEISS would support my piece's claim but cut "
       "earnings that year. <strong>Upside.</strong> The Capital Markets Day could set targets well above a 2030 range my base already "
       "reaches in 2028, and Intel now uses High NA on some layers of its 18A process."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price at or below about €{REVISIT_LONG:,.0f} with my numbers unchanged, or results that lift "
       f"my 2028E EPS to about €{need_eps_long:.2f} or more. <strong>Into a short:</strong> a price at or above about "
       f"€{REVISIT_SHORT:,.0f}, or 2028E EPS at or below about €{need_eps_short:.2f}."))
A(para("<strong>The view is wrong if</strong>, by October 2027, ASML says 2027 low NA shipments will fall more than 10% short of about "
       "85 because customers pushed out or cancelled orders, which points to my bear case; or it confirms 2028 low NA capacity of 110 or "
       "more and says 2028 is close to fully covered, which points to my bull case."))
A('</div>')

A(section("Conclusion"))
A(para("My piece argued that ASML's EUV machines are sold out, booked a year or two ahead, and grow about 30% a year. The July results "
       f"support both halves, which makes the next two years unusually visible. The shares already pay for it: at €{PRICE:,.2f} the price "
       f"needs about {NEED_UNITS:.0f} low NA machines in 2028 at {MULT} times. {my_call}: {CALL['direction']}, {CALL['conviction'].lower()} "
       f"conviction. Base value {eur(BASE_VALUE)}, {chg(BASE_VALUE)}, range {eur(bear)} to {eur(bull)}; the DCF sits lower only on "
       "below-history cash conversion."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Low NA EUV units", f"{LNA_U[0]}", f"{LNA_U[1]}", f"{LNA_U[2]}", "Capacity 65; plan about 85; 110 under study"],
        ["Low NA sales per system, €m", f"{Y26['asp']:.0f}", f"{Y27['asp']:.0f}", f"{Y28['asp']:.0f}", "2025: €237m; 2027 mix \"more positive\""],
        ["High NA units at €300m", f"{HNA_U[0]}", f"{HNA_U[1]}", f"{HNA_U[2]}", "Mine; 2025: four at €289m each"],
        ["Non-EUV growth", pc(NONEUV_G26, 0), pc(NONEUV_G[0], 0), pc(NONEUV_G[1], 0), "Guide about 25% for 2026"],
        ["Installed base growth", pc(IBM_G26, 0), pc(IBM_G[0], 0), pc(IBM_G[1], 0), "Guide over 30% for 2026"],
        ["Gross margin", pc(GM[0]), pc(GM[1]), pc(GM[2]), "Guide 54% to 56%; 2030 range 56% to 60%"],
        ["R&D and SG&A, €m", f"{RD[0] + SGA[0]:,.0f}", f"{RD[1] + SGA[1]:,.0f}", f"{RD[2] + SGA[2]:,.0f}", "Q3 guide R&D €1.2bn, SG&A €0.4bn"],
        ["Tax rate; diluted shares, m", f"17%; {SH[0]:.1f}", f"17%; {SH[1]:.1f}", f"17%; {SH[2]:.1f}", "Guided about 17%; €12bn buyback to 2028"],
    ],
), [27, 10, 10, 10, 43]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">ASML Annual Report 2025 on Form 20-F, filed 25 February 2026. ASML Q4 2025 results, Form 6-K, 28 January 2026. '
  'ASML Q2 2026 results, Form 6-K, 15 July 2026: release, presentation and US GAAP statements. ASML transcript of its Q2 2026 investor '
  'call, 15 July 2026; the Q&A as transcribed by Webull. Share prices from Euronext Amsterdam historical data; ADR and peer closes, '
  'shares outstanding and Tokyo Electron consensus from stockanalysis.com; Zacks consensus; ECB reference rates; all retrieved 7 October '
  '2026. Bloomberg report of 18 June 2026 as carried by NL Times; ASML statement to Reuters, 19 June 2026; TrendForce, 17 April 2026. Estimates for 2026 to 2028, the scenarios, the DCF and the valuation '
  'are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 7 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/asml-booked-ahead/">thephysicallayer.fyi/journal/asml-booked-ahead</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in ASML. Personal research, not investment advice.</p>')
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
