# -*- coding: utf-8 -*-
"""Broadcom Inc. (Nasdaq: AVGO) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/broadcom.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Broadcom Inc. (Nasdaq: AVGO)"
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
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = ("My draft view" if CALL["draft"] else "My call")
pb = project(*SCEN[0][1:5]); pu = project(*SCEN[2][1:5])

A('<h1 class="doctitle">Broadcom Inc.</h1>')
A('<p class="docsubtitle"><b>Nasdaq: AVGO | Custom AI accelerators, Ethernet switching and optical parts, and infrastructure software | Palo Alto, California</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:,.2f} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:,.2f}, Nasdaq close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:.2f} (intraday)"),
    ("Market value", f"About US${MCAP:,.0f}bn on {COMMON_OUT * 1000:,.0f}m shares (2 Aug 2026)"),
    ("Net debt, 2 Aug 2026", f"US${NETDEBT:.1f}bn: debt US${DEBT:.1f}bn, cash US${CASH:.1f}bn"),
    ("Non-GAAP P/E, my estimates", f"{PE26:.0f}x FY26E, {PE27:.0f}x FY27E, {PE28:.0f}x FY28E (FY26 ends 1 Nov 2026; FY27 about 31 Oct 2027)"),
    ("Consensus (stockanalysis.com)", f"EPS US${CONS_EPS_26:.2f} FY26, US${CONS_EPS_27:.2f} FY27; average target US${CONS_TP:,.2f}"),
    ("Q4 FY26 guide (2 Sep)", "Revenue US$34.8bn, of which AI US$21.7bn; gross margin about 73%; operating margin about 66%"),
    ("AI outlook (2 Sep)", "About US$58bn in FY26, US$115bn in FY27 and US$230bn in FY28, supply secured for both"),
    ("Customers, Q3 FY26", f"Top five end customers about {TOP5[1] * 100:.0f}% of revenue ({TOP5[0] * 100:.0f}% a year earlier)"),
    ("Next results", f"Q4 FY26, planned for {RESULTS_DATE} (2 Sep 2026 call)"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Broadcom is still paid either way, but the tailor now earns most of the toll. At US${PRICE:,.0f}, the price assumes AI revenue barely grows after fiscal 2027.</p>')
A(para("Broadcom designs the custom AI chips the largest buyers use to rely less on Nvidia, and sells the Ethernet switch chips their "
       "clusters run on, whoever made the chips. On 2 October I argued it is paid whether the cloud giants stay with Nvidia or leave. "
       f"The results support it: AI revenue was US${Q_AI[-1]:.1f}bn in the quarter to 2 August 2026, up {AI_G_Q3 * 100:.0f}%, with custom "
       "chips and AI networking both up more than two and a half times. But custom chips were 73% of it, and networking's share fell from "
       "almost 40% to 27% in a quarter."))
A(para(f"At US${PRICE:,.2f}, on my sum of the parts with chips at {M_SEMI} times and software at {M_SW} times, the price needs fiscal 2028 "
       f"AI revenue of about US${NEED_AI28:.0f}bn: only {NEED_AI_G * 100:.0f}% above the US$115bn Broadcom expects in fiscal 2027, "
       f"against management's US$230bn. I take US${AI28:.0f}bn, a haircut that is my own judgement."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {usd(tgt)}.</b> My base case is worth "
       f"{usd(BASE_VALUE)}, {chg(BASE_VALUE)}. The bear case is {usd(bear)} ({chg(bear)}) and the bull case {usd(bull)} ({chg(bull)}). "
       "Conviction is medium because the two largest buyers from 2027 are AI labs that must borrow, and Broadcom backstops one lab's rack leases."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (non-GAAP unless marked; FY26 ends 1 November 2026, FY27 about 31 October 2027)"))
A(datatable(
    ["US$ billion unless stated", "FY24A", "FY25A", "Q4 FY26 guide", "FY26E*", "FY27E*", "FY28E*"],
    [
        ["Revenue", f"{REV_H[0]:.1f}", f"{REV_H[1]:.1f}", f"{G4['rev']:.1f}", f"{REV26:.1f}", f"{REV27:.1f}", f"{REV28:.1f}"],
        ["Revenue growth (%)", f"{(REV_H[0] / FY23_REV - 1) * 100:.0f}", f"{(REV_H[1] / REV_H[0] - 1) * 100:.0f}", "93", f"{(REV26 / REV_H[1] - 1) * 100:.0f}", f"{(REV27 / REV26 - 1) * 100:.0f}", f"{(REV28 / REV27 - 1) * 100:.0f}"],
        ["AI semiconductors", f"{AI_H[0]:.1f}", f"{AI_H[1]:.1f}", f"{G4['ai']:.1f}", f"{AI26:.1f}", f"{AI27:.1f}", f"{AI28:.1f}"],
        ["Non-AI semiconductors", f"{SEMI_H[0] - AI_H[0]:.1f}", f"{SEMI_H[1] - AI_H[1]:.1f}", f"{G4['nonai_call']:.1f}", f"{NONAI26:.1f}", f"{NONAI27:.1f}", f"{NONAI28:.1f}"],
        ["Infrastructure software", f"{SW_H[0]:.1f}", f"{SW_H[1]:.1f}", f"{G4['sw']:.1f}", f"{SW26:.1f}", f"{SW27:.1f}", f"{SW28:.1f}"],
        ["Gross margin (%)", pc(GMH[0] / REV_H[0]), pc(GMH[1] / REV_H[1]), "about 73", pc(GM26), "", ""],
        ["Operating income", f"{OPH[0]:.1f}", f"{OPH[1]:.1f}", f"{Q4_OP:.1f}", f"{OP26:.1f}", f"{OP27:.1f}", f"{OP28:.1f}"],
        ["Operating margin (%)", pc(OPH[0] / REV_H[0]), pc(OPH[1] / REV_H[1]), "about 66", pc(OM26), pc(OM27), pc(OM28)],
        ["EPS, diluted (US$)", f"{EPS_H[0]:.2f}", f"{EPS_H[1]:.2f}", "", f"{EPS26:.2f}", f"{EPS27:.2f}", f"{EPS28:.2f}"],
        ["Consensus EPS (US$)", "", "", "", f"{CONS_EPS_26:.2f}", f"{CONS_EPS_27:.2f}", "n/v"],
        [f"P/E at US${PRICE:,.2f} (x)", "", f"{PE25:.0f}", "", f"{PE26:.0f}", f"{PE27:.0f}", f"{PE28:.0f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*FY26E is three reported quarters plus my reading of the Q4 guide; FY27E and FY28E are my own estimates, with FY27 AI revenue "
          "at management's US$115bn outlook. Fiscal years end on the Sunday closest to 31 October: FY2026 on 1 November 2026, FY2027 on about "
          "31 October 2027. The Q4 segment guides (AI US$21.7bn, non-AI about US$4.3bn, software about US$8.7bn) sum to US$34.7bn against "
          "the US$34.8bn consolidated guide. Income lines are Broadcom's non-GAAP measures, which "
          f"exclude stock-based pay (US${SBC_Q3:.1f}bn in Q3 FY26) and acquisition amortisation; GAAP EPS for the first three quarters of "
          f"FY26 was US${GAAP_EPS_9M:.2f} against US${NG_NI_9M / NG_SH_9M:.2f} non-GAAP. FY25 AI revenue is the sum of the four quarters. "
          "Consensus from stockanalysis.com (S&P Global data, updated 2 October 2026); n/v: FY28 consensus not verified. History from "
          "Broadcom's results releases."))

A('<div class="keeptogether">')
A(section("Two charts: the AI money, and a value well above the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue by part and non-GAAP diluted EPS, FY24A to FY28E; FY24 and FY25 per Broadcom, the rest my estimates. Right: value "
          "per share from the base case, the probability-weighted cases, the sensitivity grid and the bear to bull range, against the "
          f"US${PRICE:,.2f} price (red) and the stockanalysis.com average analyst target, retrieved 6 October 2026."))
A('</div>')

A(section("The thesis: the tailor who also makes the zip"))
A(para("Go back to the tailor from the October piece. A shirt off the rail fits most people well enough; ten thousand shirts for exactly "
       "the same body are worth having made. Very few workshops can cut cloth at that standard, and one of them also makes the zip sewn "
       "into almost every shirt on the rail. That workshop is Broadcom."))
A(para(f"<strong>Both halves are growing.</strong> In the quarter to 2 August 2026, AI revenue was US${Q_AI[-1]:.1f}bn, "
       f"{AI_SHARE_Q3 * 100:.0f}% of the total. On the 2 September call Hock Tan, the chief executive, said custom accelerator shipments were "
       f"73% of it: about US${XPU_Q3:.1f}bn of custom chips and US${NET_Q3:.1f}bn of networking. Custom chips grew more than three and a "
       "half times in the year and AI networking more than two and a half. Charlie Kawwas, who runs the chip business, said even customers "
       "not using Broadcom's custom chips use Tomahawk 6, its 102.4 terabit switch. That is the half paid by buyers who stay with Nvidia."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_ai.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_mix.png"></div></div>')
A(caption("Left: AI semiconductor revenue by fiscal quarter, US$bn, split into custom accelerators and networking where Broadcom gave the "
          "share on its calls (4 September 2025, 4 March, 3 June and 2 September 2026). Right: revenue by part, with AI's share of the total. "
          "Q3 FY26 is the quarter to 2 August 2026; Q4 FY26 is the guide of 2 September 2026. Source: Broadcom results releases and calls."))
A('</div>')
A(para("<strong>But the tailor now earns most of it.</strong> Networking's share of AI revenue was 35% in the quarter to 3 August 2025, a "
       "third in the quarter to 1 February 2026 and almost 40% in the quarter to 3 May; in the quarter to 2 August it fell to 27%. Tan said "
       "in June that 40% was probably the peak and about 30% the likely level, and in September that networking should grow as fast as custom "
       "chips. Broadcom does not say how much of its networking goes into Nvidia clusters. So the piece's first test has moved against the "
       "stay half, while the claim survives."))
A(para(f"<strong>The supply is physical, and bought.</strong> The 10-Q shows US${PURCH[2]:.1f}bn of unconditional purchase commitments, "
       f"mostly inventory: US${PURCH[0]:.1f}bn in FY27 and US${PURCH[1]:.1f}bn in FY28. Broadcom opens its own substrate plant in Singapore "
       "from FY27, and Kawwas said its indium phosphide laser factories are more than tripling. Remaining performance obligations across "
       f"both segments reached US${RPO:.1f}bn. <strong>The other tests:</strong> the custom customer count is still six, unchanged since "
       "March. Tan said Broadcom is shipping TPU version 8i ahead of MediaTek's 8t, which was started earlier. In April Google signed a "
       "long-term agreement for Broadcom to develop and supply future TPU generations, and a separate supply assurance agreement for "
       "networking and other components through up to 2031."))
A(para(f"<strong>The toll per dollar of sales is thinning.</strong> Non-GAAP gross margin fell from {Q_GM[2]}% a year earlier to "
       f"{Q_GM[-1]}%, and about 73% is guided. Amie Thuener, the finance chief, put it down to custom chips' rising memory content; the chip "
       f"segment's gross margin was about 67%, against 94% for software. Operating margin rose to {Q_OM[-1]}% and is guided at 66%, "
       "because costs grow far more slowly than revenue."))

A('<div class="keeptogether">')
A(section("Where I was wrong in October"))
A(para("My piece's exposure map said: \"Google, Meta, Anthropic and OpenAI design their own AI chips with Broadcom for their own data "
       "centres.\" That is wrong for Anthropic on the chip, and too loose on the data centres. Broadcom's 8-K of 6 April 2026 says Anthropic will \"access through "
       "Broadcom\" next generation \"TPU-based AI compute capacity\"; the TPU is Google's chip. On the December 2025 call Tan described "
       "Anthropic's first orders as TPU Ironwood racks, and in September he said Broadcom delivered Ironwood TPUs in volume \"to both "
       "Anthropic and Google\"."))
A(para(f"The 10-Q for the quarter to 2 August adds that, for a customer it does not name, a financial partner bought racks for more than "
       f"one gigawatt and leases them to that customer, with Broadcom backstopping the lease payments up to about US${BACKSTOP_MAX:.0f}bn; "
       f"Thuener said on the September call that this first US${XPV_TRANCHE:.0f}bn tranche is for Anthropic's one gigawatt deployment. So "
       "the racks are leased, not owned; the filings do not say where they are hosted, so \"their own data centres\" claimed more than I "
       "knew. What showed me the slip was reading the April 8-K against my own exposure map. It matters: Tan "
       "expects Anthropic to be Broadcom's largest custom customer in 2027, so the two largest buyers run one chip family, the one Google "
       "has split with MediaTek. The claim holds, because Broadcom is paid on those TPUs. The piece and the claim stay as published."))
A('</div>')
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_margin.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: non-GAAP operating margin (bars) and gross margin (line) by fiscal quarter, with the Q4 FY26 guide (light blue). Right: "
          "AVGO month-end close, September 2023 to the 5 October 2026 close (Nasdaq.com, retrieved 6 October 2026), against my base value."))
A('</div>')

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:,.2f} Broadcom is worth about US${MCAP:,.0f}bn, with US${NETDEBT:.1f}bn more debt than cash. The shares closed at "
       f"a high of US${HI_CLOSE:.2f} on 2 June 2026 (intraday high US${HI52:.2f} on 3 June) and are {abs(OFF_HIGH) * 100:.0f}% below it, "
       f"up {SINCE_PIECE * 100:.1f}% since my piece. They trade at {PE26:.0f} times my FY26 EPS and {PE27:.0f} times FY27; on consensus, "
       f"{PEC27:.0f} times FY27."))
A(para(f"<strong class='lead'>What the price needs.</strong> By October 2027 the market will price FY28, the year to about October 2028. "
       f"At {M_SEMI} times after-tax operating profit for chips and {M_SW} times for software, less net debt, US${PRICE:,.2f} needs FY28 AI "
       f"revenue of about US${NEED_AI28:.0f}bn, {NEED_AI_G * 100:.0f}% above FY27's US$115bn. Management says it has line of sight to "
       f"US$230bn and that FY28 EPS should exceed US$30; at US$30 the shares would be on {PE28_CALL:.0f} times."))
A(para(f"<strong class='lead'>Where I differ.</strong> Management says supply for both FY27 and FY28 is secured. Tan said timely "
       "deployment is \"always very much in our mind\" when Broadcom sets its outlook, and that customers' land, power and shell are "
       f"already reflected in it. I still take US${AI28:.0f}bn, {(1 - AI28 / AI_FY28_OUT) * 100:.0f}% below management, and the haircut "
       "is my own judgement: most of the growth comes from two labs that must raise money to pay, and in my view doubling deployed "
       "capacity in a year leaves little room for a late building or grid connection. The price assumes far less, and "
       f"US${PURCH[1]:.1f}bn of FY28 supply is already contracted. My worry is credit, not power: Tan expects Anthropic and OpenAI to be the two largest custom buyers by 2028, and "
       "Broadcom built the AI XPV platform with financial partners to fund more than 20 gigawatts for them by the end of 2028. The 8-K "
       "says Anthropic's use of the capacity \"is dependent on Anthropic's continued commercial success\"."))

A(section("Valuation, with the working"))
A(para(f"Two businesses, two multiples, FY28 non-GAAP after-tax operating profit. FY26 is three reported quarters plus the Q4 guide "
       f"(US$34.8bn, 66% operating margin, 16% tax, 4.94bn shares): EPS US${EPS26:.2f}, against US${CONS_EPS_26:.2f} consensus. FY27 takes "
       f"US$115bn of AI, US${NONAI27:.1f}bn of non-AI chips and US${SW27:.1f}bn of software, a {pc(SM27, 0)} chip margin (61.3% in Q3) and "
       f"{pc(SWM, 0)} for software (83.7% in Q3): EPS US${EPS27:.2f}, {abs(EPS27 / CONS_EPS_27 - 1) * 100:.0f}% below the "
       f"US${CONS_EPS_27:.2f} consensus. FY28 takes US${AI28:.0f}bn of AI and a {pc(SM28, 0)} chip margin: EPS US${EPS28:.2f}. Chips are "
       f"worth {usd(P['v_semi'])} a share and software {usd(P['v_sw'])}, less {usd(P['nd'])} of net debt, held flat with the share count "
       f"on the assumption that cash after dividends goes to buybacks: {usd(BASE_VALUE)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "FY28 AI", "Chip margin", "Multiples", "Value", "Change", "Weight"],
    [
        ["Bear", "Lab financing stalls: no AI growth after FY27", f"US${SCEN[0][1]:.0f}bn", pc(SCEN[0][2], 0),
         f"{SCEN[0][3]}x / {SCEN[0][4]}x", usd(bear), chg(bear), "25%"],
        ["Base", "Deployment slips behind management's plan", f"US${SCEN[1][1]:.0f}bn", pc(SCEN[1][2], 0),
         f"{SCEN[1][3]}x / {SCEN[1][4]}x", usd(base), chg(base), "50%"],
        ["Bull", "Management's plan arrives in full", f"US${SCEN[2][1]:.0f}bn", pc(SCEN[2][2], 0),
         f"{SCEN[2][3]}x / {SCEN[2][4]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [10, 34, 10, 10, 11, 9, 9, 7]))
A(caption(f"Multiples are chips / software, on after-tax operating profit. Software (US${SW28:.1f}bn at {pc(SWM, 0)}) and non-AI chips "
          f"(US${NONAI28:.0f}bn) are the same in all three. FY28 EPS: bear US${pb['eps']:.2f}, base US${EPS28:.2f}, bull US${pu['eps']:.2f}. "
          "The bear case is not fanciful: the shares fell 28% between the end of December 2024 and the end of March 2025, and closed at "
          f"US${LO_CLOSE:.2f} on 30 March 2026. The band: long when my base value is at least 15% above the price, short when it is at least "
          "25% below, no call in between."))
A('</div>')
above = sum(v > PRICE for r in VGRID for v in r)
above15 = sum(v > PRICE * 1.15 for r in VGRID for v in r)
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
A('<div class="keeptogether">')
A(section("Sensitivity: FY28 AI revenue against the chip multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["FY28 AI revenue"] + [f"{m}x" for m in SENS_M],
    [[f"US${a:.0f}bn"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (a, r) in enumerate(zip(SENS_AI, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{NUMW[above].capitalize()} of the nine cells sit above today's price, and {NUMW[above15]} by more than 15%. The only cell below "
       f"it needs both FY28 AI revenue of US${SENS_AI[0]:.0f}bn and a chip multiple of {SENS_M[0]} times. Software stays at {M_SW} times. "
       "Every figure is live in the accompanying model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [["Broadcom", "Nasdaq: AVGO", f"{FWD_PE_SA:.1f}x", "Custom AI chips, switch chips, optical parts, infrastructure software"]]
    + [[c, t, f"{p:.1f}x", w] for c, t, p, w in SEMI_PEERS + SW_PEERS + OTHER_PEERS],
    num_cols={2},
), [22, 15, 12, 51]))
A(caption("Forward P/E from stockanalysis.com, retrieved 6 October 2026 during US trading. Chip peer median (AMD to Qualcomm) 20.7 times; "
          "software peer median (ServiceNow to Adobe) 17.4 times; Arista shown for reference. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        [f"{RESULTS_DATE} (planned)", "Q4 FY26 results (quarter to 1 November)", "AI revenue against US$21.7bn; networking's share; Q1 FY27 guide; gross margin against 73%"],
        ["Any time", "Further AI XPV tranches", "Whether Broadcom backstops them, and on what terms"],
        ["Through FY27", "TPU 8i and MediaTek's 8t; Anthropic's 5 gigawatts", "Who ships Google's volume; Anthropic's funding"],
        ["From FY27", "Singapore substrate plant; Tomahawk 7", "Supply against the US$115bn; networking growth against custom"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para(f"<strong>The labs cannot pay.</strong> Anthropic and OpenAI depend on raising capital. Broadcom backstops up to "
       f"US${BACKSTOP_MAX:.0f}bn of one lab's rack leases and may hold up to US${CONV_NOTES:.0f}bn of its convertible notes; if later "
       f"tranches carry similar terms, the exposure grows with the revenue. This is the bear case, a {abs(bear / PRICE - 1) * 100:.0f}% fall. "
       f"<strong>Concentration.</strong> The top five end customers took about {TOP5[1] * 100:.0f}% of revenue in the August quarter, against "
       f"about {TOP5[0] * 100:.0f}% a year earlier; one distributor took {DIST_Q3[1] * 100:.0f}%. <strong>The exit swings both ways.</strong> "
       "Every buyer has its own chip team, and Google started MediaTek's 8t before Broadcom's 8i."))
A(para("<strong>Margin dilution.</strong> If racks with more memory and bought-in parts outgrow operating leverage, operating margin falls "
       "too; my base already takes the chip margin from 61% to 58%. <strong>Nvidia's networking.</strong> If Nvidia's Ethernet and "
       "scale-up links win inside its own clusters, the stay half shrinks further than the 27% share already shows."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Out of the long:</strong> a price above about US${REVISIT_NOCALL:,.0f} with my numbers unchanged, which leaves the base "
       f"less than 15% above it; or evidence that pushes FY28 AI revenue towards US${SENS_AI[0]:.0f}bn and the chip multiple towards "
       f"{SENS_M[0]} times together. <strong>Into more conviction:</strong> a second financing tranche without a Broadcom backstop, or a "
       "further custom customer reaching volume."))
A(para(f"<strong>The call is wrong if</strong> {WRONG_IF[0].lower() + WRONG_IF[1:]}"))
A('</div>')

A(section("Conclusion"))
A(para("My piece of 2 October argued that Broadcom is paid whether the cloud giants stay with Nvidia or leave. The results support it: custom "
       "chips and AI networking both grew more than two and a half times, and Tomahawk 6 sits in clusters with no Broadcom custom chips. But the "
       "custom half now earns almost three quarters of the AI money, and I was wrong that Anthropic designs its own chip with Broadcom; it "
       f"uses Google's TPU. The price assumes FY28 AI revenue of about US${NEED_AI28:.0f}bn, against management's US$230bn and my "
       f"US${AI28:.0f}bn. {my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {usd(tgt)}; base value "
       f"{usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY26E", "FY27E", "FY28E", "Basis"],
    [
        ["AI revenue, US$bn", f"{AI26:.1f}", f"{AI27:.0f}", f"{AI28:.0f}", "FY26: Q4 guide; FY27: management outlook; FY28: mine, 17% below US$230bn"],
        ["Non-AI chips, US$bn", f"{NONAI26:.1f}", f"{NONAI27:.1f}", f"{NONAI28:.1f}", "Q4 guide about US$4.3bn; mine after"],
        ["Software, US$bn", f"{SW26:.1f}", f"{SW27:.1f}", f"{SW28:.1f}", "Q4 guide about US$8.7bn; mine about 6 to 7% growth"],
        ["Chip segment operating margin", "", pc(SM27, 0), pc(SM28, 0), "61.3% in Q3 FY26 (10-Q); diluted by memory-heavy racks"],
        ["Software operating margin", "", pc(SWM, 0), pc(SWM, 0), "83.7% in Q3 FY26; 80.5% over three quarters"],
        ["Interest and other, US$bn", f"{Q4_INT + Q4_OTHER:.2f} (Q4)", f"{INT27:.1f}", f"{INT28:.1f}", "Debt falling; mine"],
        ["Tax rate (non-GAAP)", pc(TAX, 0), pc(TAX, 0), pc(TAX, 0), "Guided 16% for FY26 (global minimum tax)"],
        ["Diluted shares, bn", f"{G4['sh']:.2f} (Q4)", f"{SH:.2f}", f"{SH:.2f}", "Q4 guide; buybacks offset dilution (mine)"],
        ["Multiples, chips / software", "", "", f"{M_SEMI}x / {M_SW}x", "Peer medians 20.7x and 17.4x (stockanalysis.com)"],
    ],
), [26, 10, 9, 9, 46]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Broadcom quarterly results releases furnished on Form 8-K (Exhibit 99.1), 12 December 2024 to 2 September 2026, '
  'with their comparative columns, for revenue, segment and AI revenue, non-GAAP margins, EPS, stock-based pay, balance sheet and the Q4 '
  'FY26 guide. Broadcom Form 10-Q for the quarter to 2 August 2026 (filed 10 September 2026) for shares outstanding, remaining performance '
  'obligations, purchase commitments, the AI XPV platform, the Backstop, the convertible notes, customer concentration and segment '
  'operating income. Broadcom Form 8-K of 6 April 2026 (Google long-term agreement; Anthropic access to TPU-based compute). Broadcom '
  'earnings calls of 4 September 2025, 11 December 2025, 4 March, 3 June and 2 September 2026. Share prices from Nasdaq.com historical '
  'data; consensus EPS, average target and multiples from stockanalysis.com; all retrieved 6 October 2026. Estimates for FY26 to FY28 and '
  'the sum of the parts are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 2 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/broadcom-wins-either-way/">thephysicallayer.fyi/journal/broadcom-wins-either-way</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Broadcom. Personal research, not investment advice.</p>')
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
