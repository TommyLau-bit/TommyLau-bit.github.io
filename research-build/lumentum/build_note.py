# -*- coding: utf-8 -*-
"""Lumentum (Nasdaq: LITE) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/lumentum.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Lumentum (Nasdaq: LITE)"
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
    return f"US${x:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
pb = project(SCEN[0][1], SCEN[0][2]); pu = project(SCEN[2][1], SCEN[2][2])
call_word = CALL["direction"].lower() if CALL["direction"] == "NO CALL" else CALL["direction"]
my_call = ("My draft view" if CALL["draft"] else "My call")

A('<h1 class="doctitle">Lumentum Holdings Inc.</h1>')
A('<p class="docsubtitle"><b>Nasdaq: LITE | Indium phosphide lasers, optical transceivers and circuit switches for AI data centres | San Jose, California</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:,.2f} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:,.2f}, Nasdaq close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:,.2f}"),
    ("Market value", f"About US${MCAP:.0f}bn on {COMMON_OUT * 1000:.1f}m common shares; US${MCAP_FD:.0f}bn with Nvidia's {PREF * 1000:.1f}m preferred"),
    ("Net cash, 27 Jun 2026", f"US${NETCASH:.2f}bn: cash and investments US${CASH:.2f}bn, convertible notes US${NOTES_PRINC:.2f}bn, loans US${JAPAN_LOANS:.2f}bn"),
    ("Non-GAAP P/E, my estimates", f"{PE27:.0f}x FY27E, {PE28:.0f}x FY28E (years to June)"),
    ("Consensus", f"EPS US${CONS_EPS_27:.2f} FY27 (stockanalysis.com), US${CONS_EPS_28:.2f} FY28 (Nasdaq.com, Zacks); average target US${CONS_TP:,.0f}"),
    ("Q1 FY27 guide (11 Aug)", "Revenue US$1.225 to 1.275bn; non-GAAP operating margin 39.5 to 40.5%; EPS US$4.05 to 4.35; 102.0m shares"),
    ("Customers, FY26", f"Two took {CUST_A * 100:.1f}% and {CUST_B * 100:.1f}% of revenue"),
    ("Fabs", "Two indium phosphide wafer fabs in Japan, expanding; Greensboro, North Carolina, bought March 2026, first revenue early 2028"),
    ("Next results", "Q1 FY27 (to September 2026): 5 November 2026, after the US close"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Lumentum is shipping behind demand for its lasers and is charging for it. At US${PRICE:,.0f} the shares already pay for the shortage to outlast the new factories.</p>')
A(para("Lumentum makes the indium phosphide lasers that turn AI network traffic into light. On 5 October I argued that the "
       "network's bottleneck has moved to the laser. The year of results behind that piece supports the claim: revenue rose "
       f"{REV_Q4_GROWTH * 100:.0f}% in the June 2026 quarter, GAAP gross margin rose from {Q_GM_GAAP[3]}% to {Q_GM_GAAP[-1]}%, "
       "partly on higher prices, and the company is still shipping behind demand."))
A(para(f"But the shortage has a timetable. Lumentum is expanding its two Japanese fabs and converting a new one in Greensboro for "
       f"first revenue in early 2028. Nvidia put US$2bn into Coherent, its closest rival, on the day it invested in Lumentum. At "
       f"US${PRICE:,.2f} the price needs fiscal 2028 revenue of about US${NEED_REV28:.1f}bn at today's margins, "
       "three times fiscal 2026, in the year that capacity lands."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, leaning short.</b> My base case is worth "
       f"{usd(BASE_VALUE)}, {chg(BASE_VALUE)}. The bear case is {usd(bear)} ({chg(bear)}) and the bull case {usd(bull)} "
       f"({chg(bull)}). I would revisit below about US${round(REVISIT_LONG, -1):,.0f} or above about US${round(REVISIT_SHORT, -1):,.0f}."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (non-GAAP unless marked; fiscal years to late June)"))
A(datatable(
    ["US$ billion unless stated", "FY24A", "FY25A", "FY26A", "Q1 FY27 guide", "FY27E*", "FY28E*"],
    [
        ["Revenue", f"{REV_H[0]:.2f}", f"{REV_H[1]:.2f}", f"{REV_H[2]:.2f}", "1.225 to 1.275", f"{REV27:.2f}", f"{REV28:.2f}"],
        ["Revenue growth (%)", f"{(REV_H[0] / FY23_REV - 1) * 100:.0f}", f"{(REV_H[1] / REV_H[0] - 1) * 100:.0f}", f"{(REV_H[2] / REV_H[1] - 1) * 100:.0f}", "", f"{(REV27 / REV_H[2] - 1) * 100:.0f}", f"{B[1] * 100:.0f}"],
        ["Gross margin, GAAP (%)", pc(GM_GAAP_H[0]), pc(GM_GAAP_H[1]), pc(GM_GAAP_H[2]), "", "", ""],
        ["Gross margin (%)", pc(GM_H[0]), pc(GM_H[1]), pc(GM_H[2]), "", "", ""],
        ["Operating income", f"{OPINC_H[0]:.2f}", f"{OPINC_H[1]:.2f}", f"{OPINC_H[2]:.2f}", "", f"{OPINC27:.2f}", f"{P['o28']:.2f}"],
        ["Operating margin (%)", pc(OM_H[0]), pc(OM_H[1]), pc(OM_H[2]), "39.5 to 40.5", pc(OM27), pc(B[2])],
        ["EPS, diluted (US$)", f"{EPS_H[0]:.2f}", f"{EPS_H[1]:.2f}", f"{EPS_H[2]:.2f}", "4.05 to 4.35", f"{EPS27:.2f}", f"{EPS28:.2f}"],
        ["Consensus EPS (US$)", "", "", "", f"{CONS_Q1:.2f}", f"{CONS_EPS_27:.2f}", f"{CONS_EPS_28:.2f}"],
        [f"P/E at US${PRICE:,.2f} (x)", "", "", f"{PRICE / EPS_H[2]:.0f}", "", f"{PE27:.0f}", f"{PE28:.0f}"],
        ["Diluted shares (m)", "", f"{SH_H[1] * 1000:.1f}", f"{SH_H[2] * 1000:.1f}", "102.0", f"{SH27 * 1000:.1f}", f"{SH28 * 1000:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*FY27E and FY28E are my own estimates. FY2026 is the year to 27 June 2026; FY2027 runs to June 2027. Income lines are "
          f"Lumentum's non-GAAP measures, which exclude stock-based pay (US${SBC_26 * 1000:.0f}m in FY26) and one-off items, including a "
          f"US${LOSS_EXTING:.2f}bn non-cash loss on swapping notes for shares in Q4 FY26 (GAAP EPS that quarter: US${GAAP_EPS_Q4:.2f}). "
          "FY24 non-GAAP figures as recast in the Q4 FY25 release. Consensus: Q1 and FY28 from Nasdaq.com (Zacks), whose Q1 figure sits "
          "below the company's own guide; FY27 from stockanalysis.com (Zacks: US$19.78). History from Lumentum's results releases."))

A('<div class="keeptogether">')
A(section("Two charts: earnings that compound, and a value just below the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and non-GAAP diluted EPS, FY24A to FY28E; FY24A to FY26A per Lumentum, the rest my estimates. Right: value "
          "per share from the base case, the probability-weighted cases, the sensitivity grid and the bear to bull range, against the "
          f"US${PRICE:,.2f} price (red) and the stockanalysis.com average analyst target, retrieved 6 October 2026."))
A('</div>')

A(section("The thesis: a queue at the glassblower's"))
A(para("Go back to the glassblowers from the October piece. Every new AI chip wants a faster torch, and only a few workshops can "
       "blow the special glass for its bulb. When the queue runs round the block, a workshop raises its prices and runs its kilns "
       "flat out."))
A(para(f"<strong>Lumentum is one of those workshops.</strong> Its lasers, mainly EMLs, are grown on indium phosphide in two wafer "
       f"fabs in Japan. In the June 2026 quarter components, mainly lasers, grew {COMP_Q4_GROWTH * 100:.0f}% on a year earlier and "
       f"systems, mainly transceivers and optical circuit switches, {SYS_Q4_GROWTH * 100:.0f}%. Lumentum set records for 100 and 200 "
       "gigabit EML shipments, and 200 gigabit parts passed a quarter of EML revenue. GAAP gross margin has risen in each of the past "
       f"eight quarters, from {Q_GM_GAAP[0]}% to {Q_GM_GAAP[-1]}%. The finance chief put the gain down to fuller factories, a richer "
       "mix and higher prices on some products. On the August call Michael Hurlston, the chief executive, said Lumentum was still "
       "shipping behind demand for EMLs, expected to be significantly behind at the end of the year, and had repriced some orders."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_margin.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_quarterly.png"></div></div>')
A(caption("Left: gross margin by fiscal quarter, GAAP (bars) and non-GAAP (line), against the low forties where the claim's test "
          "begins. Right: revenue by fiscal quarter, components and systems. Q4 FY26 is the quarter to 27 June 2026. Source: Lumentum "
          "results releases, 7 November 2024 to 11 August 2026."))
A('</div>')

A(section("Where I was wrong in October"))
A(para("My piece was headlined \"Nvidia paid Lumentum $2 billion for lasers, because silicon cannot make light\", and its summary said "
       "Nvidia \"paid $2 billion to make sure Lumentum builds more of them\". Parts of the body framed it the same way, as \"the "
       "bottleneck Nvidia paid to clear\" and as Nvidia paying Lumentum \"to keep a kiln running for it\". The headline was wrong about "
       f"what the money bought, and those passages repeated it. Lumentum's Form 8-K of 2 March 2026, Item 3.02, shows that the US$2bn bought {PREF * 1e9:,.0f} shares of Series A "
       f"convertible preferred stock at US${PREF_PX:.2f} each, which convert into common shares one for one."))
A(para(f"So the US$2bn is a shareholding, not a payment for lasers. At the 5 October close it was worth about US${NVDA_STAKE:.1f}bn, "
       f"{NVDA_GAIN * 100:.0f}% more than Nvidia paid. The place in the queue comes from a separate, non-exclusive purchase "
       "commitment and rights to future capacity, which the joint release calls multibillion but whose size Lumentum has not "
       "disclosed. Other parts of the body did describe an investment and a separate commitment, and Nvidia's own release says the money supports "
       "research, future capacity and operations at a new fab. What showed me the slip was reading the 8-K against my own headline. "
       "Nvidia's cost of securing lasers so far is a profitable investment, not a premium price. The claim, that the laser is the "
       "bottleneck, survives. The piece and the claim stay as published."))

A(section("The shortage has a timetable"))
A(para("If the margin is scarcity, the question is when supply catches up. Lumentum is expanding both Japanese fabs and qualifying "
       f"EML and CW process flows on new tools. It bought a fab in Greensboro, North Carolina, on 17 March 2026 for US${GREENSBORO_USD * 1000:.0f}m "
       "and is converting it from gallium arsenide to indium phosphide; Hurlston expects first revenue in early 2028 and full output by "
       "the end of 2028. Coherent makes indium phosphide lasers on six-inch wafers, which it says yield four times as many devices as "
       "three-inch ones. And on 2 March Nvidia put US$2bn into Coherent too, with its own purchase commitment and capacity rights."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_need.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption(f"Left: fiscal 2026 revenue, my fiscal 2027 and 2028 estimates, and the fiscal 2028 revenue that the Zacks consensus EPS "
          f"and the price at {BASE_PE}x each need at my {pc(B[2])} operating margin (my derivation). Right: LITE month-end close, "
          "September 2023 to the 5 October 2026 close (Nasdaq.com, retrieved 6 October 2026), against my base value."))
A('</div>')
A(para("A buyer that funds two rival suppliers on the same day is building a second source. That is how shortages end. None of this "
       "says demand is weak: lasers for 200 gigabit lanes, optical circuit switches and co-packaged optics are all still growing. It "
       "says the extra margin that scarcity pays is most at risk in fiscal 2028, the year the price leans on."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:,.2f} Lumentum is worth about US${MCAP:.0f}bn on common shares, US${MCAP_FD:.0f}bn with the preferred, "
       f"with US${NETCASH:.1f}bn more cash than debt. The shares closed at US${LO_CLOSE:.2f} on 10 October 2025 and have risen "
       f"{RISE_DEC25 * 100:.0f}% since the end of 2025. They trade at {PRICE / EPS_H[2]:.0f} times FY26 non-GAAP EPS of US${EPS_H[2]:.2f} and "
       f"{PE_RUNRATE:.0f} times this quarter's guided earnings multiplied by four; on consensus, {PEC27:.0f} times FY27 and "
       f"{PEC28:.0f} times FY28."))
A(para(f"<strong class='lead'>What the price needs.</strong> By October 2027 the market will price fiscal 2028. At {BASE_PE} times, "
       f"US${PRICE:,.2f} needs FY28 earnings of US${NEED_EPS28:.2f} a share. At my {pc(B[2])} operating margin that needs revenue "
       f"of about US${NEED_REV28:.1f}bn, {NEED_X26:.1f} times FY26 and {NEED_G28 * 100:.0f}% above my FY27 estimate. The Zacks "
       f"consensus of US${CONS_EPS_28:.2f} needs about US${CONS28_REV:.1f}bn on the same margin."))
A(para("<strong class='lead'>Where I differ.</strong> Not on demand, which is real, but on how long the shortage pays. The price "
       f"assumes volume grows by half again in FY28 and margin holds, in the year the new capacity arrives. My base case has revenue "
       f"growing {B[1] * 100:.0f}% with the margin flat at today's level, which is still a strong year."))

A(section("Valuation, with the working"))
A(para(f"I value Lumentum on non-GAAP earnings per share, the basis on which it guides, twelve months out, so on FY28. FY27 is built "
       f"by quarter: revenue of US${Q27_REV[0]:.2f}bn in the first, within the guide, then US${Q27_REV[1]:.2f}, {Q27_REV[2]:.2f} and "
       f"{Q27_REV[3]:.2f}bn, with operating margin rising from {pc(Q27_OM[0])} to {pc(Q27_OM[3])}. I add about US${OTHER_Q * 1000:.0f}m "
       f"a quarter of interest income and tax at the company's {pc(TAX, 1)}. My first quarter EPS is US${Q27_EPS[0]:.2f}, inside the "
       f"US$4.05 to 4.35 guide. I use {BASE_PE} times, the median forward multiple of five optical peers. "
       f"{BASE_PE} x US${EPS28:.2f} = {usd(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "FY28 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", f"New capacity meets an inventory pause: growth {SCEN[0][1] * 100:.0f}%, operating margin {pc(SCEN[0][2], 0)}", usd(pb["eps28"], 2),
         f"{SCEN[0][3]}x", usd(bear), chg(bear), "25%"],
        ["Base", f"Growth {B[1] * 100:.0f}%, operating margin flat at {pc(B[2])}", usd(EPS28, 2), f"{BASE_PE}x",
         usd(base), chg(base), "50%"],
        ["Bull", f"Shortage lasts through 2028: growth {SCEN[2][1] * 100:.0f}%, operating margin {pc(SCEN[2][2], 0)}",
         usd(pu["eps28"], 2), f"{SCEN[2][3]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [10, 40, 11, 9, 11, 11, 8]))
A(caption(f"All cases start from my FY27E revenue of US${REV27:.2f}bn. The bear case is not fanciful: revenue fell "
          f"{abs(FY24_DROP) * 100:.0f}% in FY24 when customers worked through stock, and non-GAAP operating margin fell below zero. "
          f"The bull case needs FY28 revenue of US${pu['r28']:.1f}bn."))
A('</div>')
grid = [[e * m for m in SENS_PE] for e in SENS_EPS]
above = sum(v > PRICE for r in grid for v in r)
A('<div class="keeptogether">')
A(section("Sensitivity: FY28 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["FY28 EPS"] + [f"{m}x" for m in SENS_PE],
    [[usd(e, 2)] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (e, r) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
A(para(f"Only {NUMW[above]} of the nine cells sit above today's price. Each needs either {SENS_PE[2]} times my base earnings or FY28 "
       f"earnings of US${SENS_EPS[2]:.0f}, above the consensus, at {BASE_PE} times or more. Every figure is live in the accompanying "
       "model, so a change to growth, margin, tax, shares or the multiple moves the value."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [[c, t, (f"{p:.1f}x" if p else "n/m"), w] for c, t, p, w in PEERS],
    num_cols={2},
), [22, 15, 12, 51]))
A(caption("Forward P/E from stockanalysis.com, retrieved 6 October 2026 during US trading. The peer median, excluding Lumentum, is "
          "35.5 times (Coherent). Multiples only; no view on the peers' shares."))
A('</div>')

A(section("Shares, counted properly"))
A(para(f"Lumentum guides to {SH_GUIDE * 1000:.1f}m diluted shares this quarter. My count at US${PRICE:,.2f} reaches about "
       f"{FD_NOW * 1000:.1f}m: {COMMON_OUT * 1000:.1f}m common, {PREF * 1000:.1f}m preferred, about {AWARDS * 1000:.1f}m from staff "
       f"awards and about {(sum(NOTE_SH) - CAPCALL_SH) * 1000:.1f}m from four series of convertible notes, net of the capped call on the "
       f"2032 notes. The notes' US${NOTES_PRINC:.2f}bn of principal is paid in cash; only the value above each conversion price is paid "
       f"in shares. The 2032 notes convert at US${NOTES[0][2]:.2f} and the capped call stops offsetting them at US${CAP_PRICE:.2f}. "
       f"Holders had asked to convert US${EARLY_CONV * 1000:.0f}m of principal by 14 August, so cash will fall by at least that. In fiscal "
       f"2026 Lumentum swapped notes for about 10.7m shares in exchanges of 7 April and 29 May, which cut debt by about US$1.1bn."))

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["5 Nov 2026, after the close", "Q1 FY27 results (quarter to Sep 2026)", "Revenue against US$1.225 to 1.275bn; GAAP gross margin against 47.4%; Q2 guide"],
        ["Early Feb 2027 (not yet announced)", "Q2 FY27 results", "Whether EML supply has caught up; GAAP gross margin above or below 50%"],
        ["Through 2027", "Japanese fab expansions; Coherent's six-inch output", "Pricing on new long-term agreements; 200 gigabit EML share"],
        ["Aug 2027", "Q4 FY27 results and FY27 10-K", "Customer concentration; capital spending; first FY28 guide"],
        ["Early 2028", "Greensboro first revenue", "On time; whether added supply moves GAAP gross margin towards the low forties"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The shortage lasts longer.</strong> The bull case, and the main risk to a no call that leans short. Lumentum keeps "
       "beating its guide, and demand for 200 gigabit lasers, circuit switches and lasers for co-packaged optics is still rising. "
       "<strong>The shortage ends faster.</strong> The bear case and the claim's falsifier: new fabs, larger wafers and silicon "
       "photonics, which needs simpler lasers, add supply at once."))
A(para(f"<strong>Few, large buyers.</strong> Two customers took {CUST_A * 100:.1f}% and {CUST_B * 100:.1f}% of FY26 revenue, and most "
       "buy on purchase orders without volume commitments, as they showed in FY24. <strong>Capital.</strong> Capital spending was "
       f"US${CAPEX_26 * 1000:.0f}m in FY26 against US${OCF_26 * 1000:.0f}m of operating cash flow. <strong>Quality of earnings.</strong> "
       f"Non-GAAP figures exclude US${SBC_26 * 1000:.0f}m of stock-based pay, and note conversions add shares as the price rises."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"I make no call while my base value sits between 15% above the price and 25% below it; the band is wider on the "
       "short side because a short's losses are open-ended when a stock keeps rising."))
A(para(f"<strong>Into a short:</strong> a price above about US${round(REVISIT_SHORT, -1):,.0f}, which would put my base case 25% below it, or "
       "GAAP gross margin below 44% in any quarter while revenue still grows. <strong>Into a long:</strong> a price below about "
       f"US${round(REVISIT_LONG, -1):,.0f}, or revenue above US$1.6bn in the December 2026 quarter with GAAP gross margin above 50%, which would "
       "show the shortage tightening as capacity grows."))
A(para("<strong>The call is wrong if</strong> FY27 revenue reaches US$6.8bn or more with GAAP gross margin of 50% or more in its "
       "fourth quarter, or the shares close above US$1,450 or below US$750 by October 2027."))
A('</div>')

A(section("Conclusion"))
A(para("My piece of 5 October argued that the AI network's bottleneck has moved to the laser. The year of results behind it supports that claim: "
       "revenue more than doubled, margin rose 14 points and Lumentum still cannot ship enough. I was wrong about one thing: Nvidia's "
       f"US$2bn bought shares, now worth about US${NVDA_STAKE:.1f}bn, not lasers. At US${PRICE:,.2f} the price needs FY28 revenue of "
       f"about US${NEED_REV28:.1f}bn at today's margins, in the year the new capacity arrives. {my_call}: {CALL['direction']}, "
       f"{CALL['conviction'].lower()} conviction, leaning short; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}. "
       f"Revisit below about US${round(REVISIT_LONG, -1):,.0f} or above about US${round(REVISIT_SHORT, -1):,.0f}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY27E", "FY28E", "Basis"],
    [
        ["Revenue, US$bn", f"{REV27:.2f}", f"{REV28:.2f}", f"FY27 by quarter: {', '.join(f'{x:.2f}' for x in Q27_REV)}; Q1 guide 1.225 to 1.275"],
        ["Revenue growth", f"{(REV27 / REV_H[2] - 1) * 100:.0f}%", f"{B[1] * 100:.0f}%", "Supply-limited; Greensboro adds from early 2028"],
        ["Operating margin (non-GAAP)", pc(OM27), pc(B[2]), "Q1 guide 39.5 to 40.5%; Q4 FY26 36.6%"],
        ["Other income, US$bn", f"{OTHER_Q * 4:.3f}", f"{OTHER_Y:.3f}", "Q4 FY26: 0.022 a quarter; cash falls with conversions"],
        ["Tax rate (non-GAAP)", pc(TAX), pc(TAX), "Company's long-term non-GAAP rate"],
        ["Diluted shares, m", f"{SH27 * 1000:.1f}", f"{SH28 * 1000:.1f}", "Q1 FY27 guide, then 1% a year more"],
        ["Target multiple", "", f"{BASE_PE}x", "Median of five peers: AAOI 55.3x, Ciena 40.8x, Coherent 35.5x, Fabrinet 26.4x, Broadcom 20.9x"],
    ],
), [26, 10, 10, 54]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Lumentum quarterly results releases furnished on Form 8-K (Exhibit 99.1), Q4 FY24 (14 August 2024) to Q4 FY26 '
  '(11 August 2026), with their comparative periods, for revenue, components and systems, GAAP and non-GAAP margins, EPS, diluted '
  'shares and guidance. Lumentum Form 10-K for the year to 27 June 2026 (filed 17 August 2026) for shares outstanding, convertible '
  'notes and capped call, early conversions, customer concentration, capital spending, cash flow, Greensboro and Sagamihara. Lumentum '
  'Form 8-K of 2 March 2026 (Items 3.02 and 7.01) and its joint release with Nvidia. Coherent Form 8-K, Exhibit 99.1, 2 March 2026. '
  'Coherent release of 25 March 2024 on six-inch indium phosphide wafers. Lumentum Q4 FY26 earnings presentation and call, 11 August '
  '2026. Lumentum investor relations event listing (Q1 FY27 call, 5 November 2026). Share prices from Nasdaq.com historical data; '
  'consensus EPS from stockanalysis.com and Nasdaq.com (Zacks); multiples and average target from stockanalysis.com; all retrieved '
  '6 October 2026. Estimates for FY27 and FY28 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 5 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/lumentum-makes-the-light/">thephysicallayer.fyi/journal/lumentum-makes-the-light</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Lumentum. Personal research, not investment advice.</p>')
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
