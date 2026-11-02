# -*- coding: utf-8 -*-
"""Infineon Technologies AG (Xetra: IFX) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/infineon.md.
"""
import datetime, statistics
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Infineon Technologies AG (Xetra: IFX)"
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


def eur(x, d=0):
    return f"€{x:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def m(x):
    return f"{x:,.0f}"


def pc(x, d=1):
    return f"{x * 100:.{d}f}"


bear, base, bull = SC
tgt = CALL["target"]
tp_txt = eur(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {eur(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
peer_med = statistics.median(p[2] for p in PEERS[1:])
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
n_above = sum(v > PRICE for r in SENS for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in SENS for v in r)

A('<h1 class="doctitle">Infineon Technologies AG</h1>')
A('<p class="docsubtitle"><b>Xetra: IFX | Power semiconductors (silicon, silicon carbide, gallium nitride), car and industrial chips | Neubiberg, Germany</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{eur(PRICE, 2)} (Xetra close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{eur(PRICE, 2)}, Xetra close {PRICE_DATE}; record close {eur(HI_CLOSE, 2)} on 2 and 3 Jun 2026, intraday high {eur(HI_INTRA, 2)} on 22 Jun"),
    ("Market value", f"€{MCAP:.1f}bn on {SHARES:,.0f}m shares"),
    ("Net debt", f"€{NET_DEBT_JUN26:,}m at 30 Jun 2026; about €{NET_DEBT_SEP26 / 1000:.1f}bn at 30 Sep (my estimate); EV about €{EV:.0f}bn"),
    ("FY26 guide (5 Aug 2026)", "Revenue around €16.3bn; Segment Result Margin around 20%; Q4 €4.7bn at about 23%"),
    ("AI data centre power", f"Over €0.7bn FY25; more than €1.6bn FY26; €2.5bn plus FY27, which Infineon expects to raise materially on 10 Nov"),
    ("P/E", f"{PE_C26:.1f}x FY26 and {PE_C27:.1f}x FY27 consensus; {PE_M27:.1f}x my FY27E"),
    ("Consensus (stockanalysis.com)", f"Average target {eur(CONS_TP, 2)} ({CONS_N} analysts); forward P/E {FWD_PE_SA:.1f}x"),
    ("Next event", "Q4 FY26 results and FY27 outlook, 10 November 2026 (Infineon investor page)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Infineon\'s AI power business is now big enough to move it. At €50.56, the shares price in most of what I expect.</p>')
A(para("Infineon makes the power chips that step grid electricity down to the trickle an AI processor runs on, and it is the "
       f"largest maker of chips for cars. AI power is about {pc(AI_SHARE26, 0)}% of its sales but about {pc(AI_SHARE_GROWTH26, 0)}% of "
       "this year's revenue growth, and its Power &amp; Sensor Systems margin has overtaken Automotive's."))
A(para(f"The shares have fallen {abs(OFF_HIGH) * 100:.0f}% from their June record with no warning from Infineon. At my multiple the price "
       f"implies about €{IMPLIED_AI / 1000:.1f}bn of AI revenue in fiscal 2027, below the €2.5bn plus already guided. But cars are "
       f"{pc(ATV_SHARE26, 0)}% of sales, and I sit below consensus on the rest of the group."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction.</b> Twenty-one times my fiscal 2027 EPS of €{B['eps']:.2f} gives "
       f"{eur(BASE_VALUE)}, {chg(BASE_VALUE)}, inside a range of {eur(bear['value'])} ({chg(bear['value'])}) to {eur(bull['value'])} "
       f"({chg(bull['value'])}). The 10 November AI guide is the test."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (fiscal years to 30 September; adjusted EPS as Infineon defines it)"))
A(datatable(
    ["€ million unless stated", "FY24A", "FY25A", "FY26E*", "FY27E*"],
    [
        ["Revenue", m(FY["FY24"][0]), m(FY["FY25"][0]), m(GROUP_REV26), m(B["rev"])],
        ["Growth (%)", "", pc(FY["FY25"][0] / FY["FY24"][0] - 1), pc(GROUP_REV26 / FY["FY25"][0] - 1), pc(B["rev"] / GROUP_REV26 - 1)],
        ["Automotive revenue", "7,716", m(SEG_FY25["ATV"]), m(REV26["ATV"]), m(B["atv"])],
        ["AI data centre power revenue", "", "700+", m(AI26), m(B["ai"])],
        ["AI share of revenue (%)", "", pc(AI_FY25 / FY["FY25"][0]), pc(AI_SHARE26), pc(AI_SHARE27)],
        ["Segment Result", m(FY["FY24"][1]), m(FY["FY25"][1]), m(GROUP_SR26), m(B["sr"])],
        ["Segment Result Margin (%)", pc(FY["FY24"][1] / FY["FY24"][0]), pc(FY["FY25"][1] / FY["FY25"][0]), pc(GROUP_SR26 / GROUP_REV26), pc(B["margin"])],
        ["Adjusted EPS, diluted (€)", f"{FY['FY24'][2]:.2f}", f"{FY['FY25'][2]:.2f}", f"{EPS26:.2f}", f"{B['eps']:.2f}"],
        ["Consensus EPS (€)", "", "", f"{CONS_EPS26:.2f}", f"{CONS_EPS27:.2f}"],
        [f"P/E at {eur(PRICE, 2)} (x)", "", "", f"{PE_M26:.1f}", f"{PE_M27:.1f}"],
    ],
    num_cols={1, 2, 3, 4},
))
A(caption("*FY26E is Q1 to Q3 as reported plus Infineon's Q4 guide, split by segment by me; FY27E is my base case. FY24A and FY25A from the "
          "Annual Report 2025; Automotive FY24 and FY25 before a small restatement. AI figures are Infineon's to FY25 (over €700m); the FY26 guide "
          "is more than €1.6bn. Consensus from stockanalysis.com (S&amp;P Global), updated 21 October 2026."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: AI power is a tenth of sales, and the higher-margin tenth"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_ai.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_margin.png"></div></div>')
A(caption("Left: AI data centre power revenue, €bn, and its share of group revenue; FY25 per the Annual Report 2025, FY27 guide per the "
          "Q3 FY26 call, FY26E and FY27E mine. Right: Segment Result Margin by quarter, Power &amp; Sensor Systems against Automotive; Q3 FY25 to "
          "Q3 FY26 from Infineon's August 2026 company presentation (restated), Q4 FY26 my split of the 23% group guide."))
A('</div>')

A(section("The thesis: valves for every step from the grid to the chip"))
A(para("Think of the electricity in an AI data centre as water coming down from a reservoir to a tap. At every step the pressure has "
       "to come down, from the grid's tens of thousands of volts to below one volt at the processor. Each step needs a valve, and in "
       "electricity the valve is a power chip that switches on and off very fast."))
A(para("Infineon makes valves for every step. It sells all three materials: silicon, silicon carbide for the high voltage steps near "
       "the grid, and gallium nitride for the dense middle steps. It says it is in almost every AI platform from every relevant maker, "
       "and puts the semiconductor content of an AI rack at US$100 to 250 per kilowatt, about US$175 on average (6 May 2026)."))
A(para("My piece argued that 800 volts reaches the AI rack before it reaches the building. Until 2028 it enters data halls through power "
       "racks and row power centres fed from today's AC power rooms; no hall of 10 MW or more is fed by a facility-level rectifier or "
       "solid-state transformer before then. Infineon's filings since support that claim and add nothing against it."))
A(para("For Infineon the claim does two things. <b>It says where next year's money comes from.</b> Nvidia's 800 volt power rack is only "
       "due to ship from the second half of 2026, and its Kyber racks in 2027, so most of what Infineon sells in fiscal 2027 still goes "
       "into today's racks. Infineon does not split AI revenue by voltage. <b>It also limits one source of upside.</b> Infineon says "
       "solid-state transformers will push content per kilowatt up, and is developing a 2 to 5 MW block on its silicon carbide with "
       "SolarEdge (5 November 2025). If my claim is right, that content does not reach large halls before 2028. What protects Infineon in "
       "the change of voltage is its own expectation (May 2025) that power chips take a similar or higher share of an 800 volt design."))
A(para(f"<strong class='lead'>Is AI power big enough to matter?</strong> Infineon sold over €700m of AI data centre power in fiscal 2025, "
       f"out of €14.66bn of revenue, and guides to more than €1.6bn in fiscal 2026. On my €1.65bn, AI is {pc(AI_SHARE26)}% of sales; with "
       f"the €0.5bn a year of classic data centre power, all data centre power is {pc(DC_SHARE26)}%. But AI supplies about "
       f"{pc(AI_SHARE_GROWTH26, 0)}% of the revenue Infineon adds this year. Power &amp; Sensor Systems, where most AI power sits, grew 34% "
       "on a year earlier in the June quarter, at a 24.9% margin against 18.4% in Automotive."))
A(para(f"Automotive is still {pc(ATV_SHARE26, 0)}% of fiscal 2026 sales on my estimates. S&amp;P Global cut its 2026 light vehicle production "
       "forecast in April, and Infineon is cutting back silicon power parts for electric drivetrains. So the answer is yes, with a "
       f"qualification: each €1bn of AI revenue adds about €{EPS_PER_AI_BN:.2f} to my fiscal 2027 EPS, one point of Automotive margin "
       f"about €{EPS_PER_ATV_PT:.2f}. Cars set the floor; AI sets the slope."))
A(para(f"<strong class='lead'>A check on size.</strong> At US$175 per kilowatt, €1.65bn of AI revenue equals the whole power chip content "
       f"of about {GW_FY26:.0f} GW of AI racks (my arithmetic). Infineon does not sell all of that content, so it serves even more "
       "capacity. It already holds a large share; growth from here depends more on the build than on share gains."))
A(para("<strong class='lead'>Supply, not demand, sets the pace.</strong> Infineon is in allocation. Customers have signed, or are "
       "negotiating, multi-year capacity reservation agreements worth a high single-digit billion euros in total, with some prepayment. "
       "It opened its Smart Power Fab in Dresden this summer and pulled €500m of AI investment into fiscal 2026. The backlog rose from "
       "about €21bn in December 2025 to about €25bn in March and close to €30bn in June. The piece's statements about Infineon match the "
       "company's own releases."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {eur(PRICE, 2)} Infineon is worth €{MCAP:.1f}bn. Net debt was €{NET_DEBT_JUN26:,}m in June; less the fourth-quarter "
       f"free cash flow implied by the guide, I estimate €{NET_DEBT_SEP26 / 1000:.1f}bn in September, for an enterprise value of about "
       f"€{EV:.1f}bn. The shares trade at {PE_C26:.1f} times the fiscal 2026 consensus of €{CONS_EPS26:.2f} and {PE_C27:.1f} times the "
       f"fiscal 2027 consensus of €{CONS_EPS27:.2f}. The median of eight chip peers is {peer_med:.1f} times; Texas Instruments, Analog "
       f"Devices and Monolithic Power trade at 26 to 28 times. At the June peak the shares traded at {PE_PEAK_C27:.1f} times today's "
       "fiscal 2027 consensus."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [[d, w.replace("EUR", "€"), chg_ if True else ""] for d, w, chg_ in
     [(d, w, f"{'up' if b >= a else 'down'} {abs(b / a - 1) * 100:.1f}%") for d, w, a, b in EVENTS]] +
    [["2 to 3 Jun 2026", f"Record close {eur(HI_CLOSE, 2)}", "Peak"],
     ["Jul and Oct 2026", "Chip sector sell-offs; no warning from Infineon", f"down {abs(OFF_HIGH) * 100:.0f}% from peak"]],
), [21, 56, 23]))
A('</div></div>')
A(caption(f"Left: Infineon month-end close, October 2023 to the {PRICE_DATE} close, against my base value (red). Yahoo Finance, read 2 "
          "November 2026. Right: moves from the previous close to the close on results days (releases come before Xetra opens)."))
A('</div>')
A(para("So the market now pays for Infineon roughly what it pays for a car and industrial chip maker, with nothing extra for AI. The "
       "shares fell on each of the last three results days, even as Infineon raised its guidance or its AI targets each time."))
A(para(f"<strong class='lead'>First, the price assumes less AI than Infineon has guided.</strong> Holding my other assumptions, at "
       f"{BASE_PE} times the price implies about €{IMPLIED_AI / 1000:.1f}bn of AI revenue in fiscal 2027. Infineon's indication is "
       f"€2.5bn plus, and it said in August that the November update would be material. My base case is €{B['ai'] / 1000:.1f}bn."))
A(para(f"<strong class='lead'>Second, I am below consensus on the rest.</strong> My fiscal 2027 EPS is €{B['eps']:.2f}, "
       f"{abs(B['eps'] / CONS_EPS27 - 1) * 100:.0f}% below the €{CONS_EPS27:.2f} consensus. On my bridge that consensus needs a group margin "
       f"of about 25% in the first full year of a recovery. I assume {pc(B['margin'])}%, up from {pc(GROUP_SR26 / GROUP_REV26)}% in fiscal "
       "2026 and in line with the 23% guided for the September quarter."))
A(para("<strong class='lead'>Third, watch the definition on 10 November.</strong> Infineon said its updated fiscal 2027 figure will "
       "\"also include our power solutions for all different forms of datacenter configurations\", with CPU power named as a driver. Part of a higher headline may be classic data "
       "centre power it already sells, about €0.5bn a year. I compare like with like. The two differences pull against each other, which "
       "is why my base value lands close to the price."))

A(section("Valuation, with the working"))
A(para("I value Infineon on adjusted EPS for fiscal 2027, the year to September 2027, which is the year ahead for most of my twelve "
       f"months. I build three blocks, Automotive, AI power and everything else, and bridge Segment Result to EPS with €{FIN['FY27']}m of "
       f"net financial cost and a {pc(TAX)}% tax rate. The same bridge gives €{EPS26:.2f} for fiscal 2026, equal to consensus, and "
       f"€{EPS25_CHECK:.2f} for fiscal 2025 against €1.39 reported. Fiscal 2026 is Q1 to Q3 as reported plus the €4.7bn, 23% Q4 guide."))
A(para(f"<strong class='lead'>Fiscal 2027, base.</strong> Automotive grows {pc(SCEN[1][1], 0)}% at a {pc(SCEN[1][2])}% margin. AI power "
       f"reaches €{B['ai'] / 1000:.1f}bn at a {pc(AI_M, 0)}% margin, my assumption, since Infineon does not disclose it. Everything else "
       f"grows {pc(SCEN[1][5], 0)}%, with a full year of the ams OSRAM sensors, at {pc(SCEN[1][6], 0)}%. Revenue is €{B['rev'] / 1000:.1f}bn "
       f"against a €20.0bn consensus; Segment Result €{B['sr'] / 1000:.2f}bn; EPS €{B['eps']:.2f}, {pc(AI_SHARE_SR27, 0)}% of it from AI."))
A(para(f"<strong class='lead'>The multiple.</strong> I use {BASE_PE} times: about two turns above the {peer_med:.1f} times peer median, "
       f"for EPS growing about {pc(B['eps'] / EPS26 - 1, 0)}% next year with the fastest part tied to AI, and five to seven turns below "
       f"the analog and power specialists, because nearly half of sales go to carmakers. {BASE_PE} x €{B['eps']:.2f} = "
       f"{eur(BASE_VALUE, 2)}, {chg(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "FY27 EPS", "P/E", "Value", "Change", "Weight"],
    [
        ["Bear", f"AI €2.6bn at 33%; cars up 2% at 18.5%; rest up 5% at 15%; margin {pc(bear['margin'])}%", f"€{bear['eps']:.2f}", f"{bear['pe']}x", eur(bear["value"]), chg(bear["value"]), "25%"],
        ["Base", f"AI €3.3bn at 38%; cars up 7% at 21.5%; rest up 15% at 20%; margin {pc(base['margin'])}%", f"€{base['eps']:.2f}", f"{base['pe']}x", eur(base["value"]), chg(base["value"]), "50%"],
        ["Bull", f"AI €4.2bn at 40%; cars up 10% at 22.5%; rest up 20% at 22%; margin {pc(bull['margin'])}%", f"€{bull['eps']:.2f}", f"{bull['pe']}x", eur(bull["value"]), chg(bull["value"]), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {eur(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 45, 10, 7, 10, 11, 8]))
A(caption("All cases start from my FY26E and use the same bridge. The bear case is close to a 40% fall: AI below Infineon's own floor, "
          "cars up only 2% and a car-maker multiple."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: FY27 AI revenue against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["FY27 AI revenue"] + [f"{p}x" for p in SENS_PE],
    [[f"€{a / 1000:.1f}bn"] + [(f"<b>{eur(v)}</b>" if (i == 1 and j == 1) else eur(v)) for j, v in enumerate(row)]
     for i, (a, row) in enumerate(zip(SENS_AI, SENS))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{W[n_above]} of the nine cells sit above the price, and {W[n_15].lower()} sit 15% or more above it. Each €1bn of AI revenue is worth "
       f"about €{VAL_PER_AI_BN:.2f} a share at {BASE_PE} times. A long needs the base 15% or more above the price, a short 25% or more below. "
       f"At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, {my_call.lower()} is no call. Consensus EPS at my multiple gives {eur(CONS_VALUE)}, "
       f"{chg(CONS_VALUE)}: the gap between no call and long is my margin assumption."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Valuation cross-check and peers"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_valuation.png"></div><div class="col">')
A(cols(datatable(
    ["Company", "Fwd P/E", "EV/EBIT"],
    [[c, f"{p:.1f}x", f"{e:.1f}x"] for c, t, p, e, w in PEERS],
    num_cols={1, 2},
), [50, 25, 25]))
A('</div></div>')
A(caption(f"Left: value per share from each method against the price (grey). Right: forward P/E and trailing EV/EBIT from stockanalysis.com "
          f"(S&amp;P Global data), read 2 November 2026; peer median forward P/E excluding Infineon {peer_med:.1f}x. Multiples set the range "
          "only; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["10 November 2026 (announced)", "Q4 FY26 results; FY27 outlook in the new three-division setup", "FY27 AI guide, like for like against €3.3bn; Q4 margin against about 23%; restated history"],
        ["Second half of 2026", "Nvidia's 800 volt power rack ships", "Whether Infineon names 800 volt revenue; content per kW against US$175"],
        ["Early February 2027 (date not announced)", "Q1 FY27 results", "Allocation easing or not; Dresden ramp; Automotive orders"],
        ["During 2027", "Capacity reservation agreements", "How many are signed, their size and prepayments"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The AI build slows.</strong> Capacity reservation agreements cover part of future demand, but they are not orders and "
       f"their terms are not public. The bear case is a {abs(bear['value'] / PRICE - 1) * 100:.0f}% fall."))
A(para("<strong>Capacity sets the pace.</strong> Infineon is in allocation and ramping Dresden while converting other lines. A slow ramp "
       "pushes revenue into later quarters, and about €2.7bn of investment in fiscal 2026 raises depreciation until the lines fill."))
A(para(f"<strong>Cars and factories.</strong> Automotive is {pc(ATV_SHARE26, 0)}% of sales. A weaker car market, or a slow industrial "
       f"recovery, would hold the rest of the group below my margins. Each point of Automotive margin is worth about "
       f"€{EPS_PER_ATV_PT * BASE_PE:.0f} a share at {BASE_PE} times."))
A(para("<strong>Rivals and the change of voltage.</strong> Monolithic Power, Texas Instruments, Analog Devices and Renesas compete at the "
       "processor; onsemi, STMicroelectronics and Navitas in silicon carbide and gallium nitride. At 800 volts Infineon expects its share "
       "of content to hold; that is its expectation, not a contract."))
A(para("<strong>Currency and debt.</strong> The guide assumes US$1.15 per euro. Net debt was €5.2bn in June, which Infineon puts at a "
       "net leverage of 1.4 times."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a call:</strong> {REVISIT_IF}"))
A(para(f"<strong>{my_call} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para("My piece claimed that 800 volts reaches the AI rack before it reaches the building. Infineon's statements fit it, and the claim "
       "tells me what not to pay for: solid-state transformer content belongs after 2028, and fiscal 2027 still rides on today's racks. "
       f"AI power is now big enough to move Infineon: about {pc(AI_SHARE_GROWTH26, 0)}% of this year's growth and, on my numbers, "
       f"{pc(AI_SHARE_SR27, 0)}% of next year's profit. After a {abs(OFF_HIGH) * 100:.0f}% fall the price assumes less AI than Infineon "
       f"has guided, but nearly half of sales are cars and my base value of {eur(BASE_VALUE)} is only "
       f"{(BASE_VALUE / PRICE - 1) * 100:.0f}% above {eur(PRICE, 2)}. {my_call}: {CALL['direction']}, {conv} conviction, until the "
       "10 November guide shows how far the AI number really moves."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY26E", "FY27E", "Basis"],
    [
        ["Q4 FY26 revenue by segment, €m", f"ATV {Q4['ATV'][0]:,}; GIP {Q4['GIP'][0]}; PSS {Q4_PSS_REV:,}; CSS {Q4['CSS'][0]}", "", "Infineon's group guide of €4.7bn and its direction by segment"],
        ["Q4 FY26 margin by segment", f"ATV {pc(Q4['ATV'][1])}%; GIP {pc(Q4['GIP'][1], 0)}%; PSS {pc(Q4_PSS_SR / Q4_PSS_REV)}%; CSS {pc(Q4['CSS'][1], 0)}%", "", "PSS is the plug to the 23% group guide"],
        ["AI power revenue, €m", f"{AI26:,}", f"{B['ai']:,.0f}", "Guide more than 1,600; FY27 indication 2,500 plus"],
        ["AI power margin", f"{pc(AI_M, 0)}%", f"{pc(AI_M, 0)}%", "Not disclosed; my assumption"],
        ["Automotive growth / margin", f"{pc(SR26['ATV'] / REV26['ATV'])}% margin", f"{pc(SCEN[1][1], 0)}% / {pc(SCEN[1][2])}%", "Replenishment, flat car market"],
        ["Everything else growth / margin", f"{pc(REST_SR26 / REST26)}% margin", f"{pc(SCEN[1][5], 0)}% / {pc(SCEN[1][6], 0)}%", "Upcycle, ams OSRAM sensors, lower idle costs"],
        ["Net financial cost, €m / tax rate", f"{FIN['FY26']} / {pc(TAX)}%", f"{FIN['FY27']} / {pc(TAX)}%", "Q1 to Q3 effective tax rates 24%, 23%, 21%"],
        ["Shares, m", f"{SHARES:,.0f}", f"{SHARES:,.0f}", "Annual Report 2025, after the November 2025 buyback"],
    ],
), [26, 30, 14, 30]))
A(caption(f"All my estimates. Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Infineon Annual Report 2025 (fiscal year to 30 September 2025), for revenue, Segment Result, adjusted EPS, '
  'shares, net cash and the AI data centre passage. Infineon analyst call statements of 4 February, 6 May and 5 August 2026 (CEO and CFO '
  'prepared remarks), and the Q3 FY26 results release of 5 August 2026, for segment results, AI revenue targets, content per kilowatt, '
  'backlog, capacity reservation agreements, guidance, free cash flow and net debt. Infineon company presentation, August 2026, for '
  'segment figures by quarter, restated. Infineon investor page, read 2 November 2026, for the results date. Infineon release on 800 '
  'volt power with Nvidia, 20 May 2025 (Business Wire); Infineon and SolarEdge release, 5 November 2025. Nvidia Technical Blog, '
  '20 May 2025 and 11 August 2026, for the dates of 1 MW Kyber racks and the 800 volt power rack. Share prices from Yahoo Finance '
  'history, checked against stockanalysis.com; consensus, targets and peer multiples from '
  'stockanalysis.com (S&amp;P Global data); all read 2 November 2026. Q4 FY26 segment figures and FY27 estimates are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece on 800 volt power for AI racks, '
  '<a href="https://thephysicallayer.fyi/journal/powering-the-rack/">thephysicallayer.fyi/journal/powering-the-rack</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Infineon. Personal research, not investment advice.</p>')
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
