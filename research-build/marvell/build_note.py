# -*- coding: utf-8 -*-
"""Marvell Technology (Nasdaq: MRVL) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/marvell.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Marvell Technology (Nasdaq: MRVL)"
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
pb = project(SCEN[0][1], SCEN[0][2]); pu = project(SCEN[2][1], SCEN[2][2])
my_call = ("My draft view" if CALL["draft"] else "My call")
FY27_GM = (1.4238 + 1.6140 + Q3_REV * H2_GM + Q4_REV * H2_GM) / REV27

A('<h1 class="doctitle">Marvell Technology, Inc.</h1>')
A('<p class="docsubtitle"><b>Nasdaq: MRVL | Optical DSPs, interconnect, switching and custom silicon for AI data centres | Santa Clara, California</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"US${PRICE:,.2f} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"US${PRICE:,.2f}, Nasdaq close {PRICE_DATE}; 52-week range US${LO52:.2f} to {HI52:.2f} (intraday)"),
    ("Market value", f"About US${MCAP:.0f}bn on {COMMON_OUT * 1000:.1f}m common shares; US${MCAP_FD:.0f}bn with Nvidia's preferred as converted"),
    ("Net debt, 1 Aug 2026", f"US${NETDEBT:.2f}bn: debt US${DEBT:.2f}bn, cash US${CASH:.2f}bn"),
    ("Non-GAAP P/E, my estimates", f"{PE27:.0f}x FY27E, {PE28:.0f}x FY28E, {PE29:.0f}x FY29E (years to about January)"),
    ("Consensus (stockanalysis.com)", f"EPS US${CONS_EPS_27:.2f} FY27, US${CONS_EPS_28:.2f} FY28; average target US${CONS_TP:,.2f}"),
    ("Q3 FY27 guide (27 Aug)", "Revenue US$3.15bn +/- 5%; non-GAAP gross margin 57.5 to 58.5%; EPS US$1.05 to 1.15"),
    ("Investor Day (6 Oct)", f"Revenue about US$20bn in FY28 (was US$18bn); custom US$12bn+ in FY29; US$70bn to 90bn in FY31"),
    ("FY31 target model", "Gross margin 56 to 59%; operating margin 44 to 46%; tax 15%; FCF above 36%; EPS above US$30"),
    ("Customers, FY26", f"Ten largest took {TOP10[1] * 100:.0f}% of revenue ({TOP10[0] * 100:.0f}% in FY25)"),
    ("Next event", "Q3 FY27 results expected early December 2026; date not yet announced"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Marvell\'s optical toll is still the biggest line in its own plan. At US${PRICE:,.0f}, the price needs little growth after fiscal 2028.</p>')
A(para("Marvell makes the optical DSPs that turn AI network traffic into light and back, plus the switch chips and custom chips around "
       "them. On 28 September I argued that Marvell is paid every time AI chips talk, whoever made the chips. The results support it: "
       f"data centre revenue rose {DC_G_Q2 * 100:.0f}% in the quarter to 1 August 2026, to {DC_SHARE_Q2 * 100:.0f}% of the total, and "
       "Marvell guides interconnect, its largest data centre business, to grow more than 70% this fiscal year."))
A(para(f"At its Investor Day on 6 October Marvell raised its fiscal 2028 outlook to about US$20bn, from US$18bn, and set a fiscal 2031 "
       f"target of US$70bn to 90bn. At the midpoint interconnect is about US${FY31_SPLIT['interconnect']:.1f}bn of it, the largest line, "
       f"ahead of custom chips at about US${FY31_SPLIT['custom']:.0f}bn. At US${PRICE:,.2f} and {BASE_PE} times, the price needs fiscal "
       f"2029 revenue of about US${NEED_REV29:.1f}bn, only {NEED_G29 * 100:.0f}% above the new fiscal 2028 outlook."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {usd(tgt)}.</b> My base case takes "
       f"US${REV29:.0f}bn for fiscal 2029, below the path management set out, and is worth {usd(BASE_VALUE)}, {chg(BASE_VALUE)}. The bear "
       f"case is {usd(bear)} ({chg(bear)}) and the bull case {usd(bull)} ({chg(bull)})."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (non-GAAP unless marked; fiscal years to about 31 January)"))
A(datatable(
    ["US$ billion unless stated", "FY24A", "FY25A", "FY26A", "Q3 FY27 guide", "FY27E*", "FY28E*", "FY29E*"],
    [
        ["Revenue", f"{REV_H[0]:.2f}", f"{REV_H[1]:.2f}", f"{REV_H[2]:.2f}", "2.99 to 3.31", f"{REV27:.2f}", f"{REV28_IN:.2f}", f"{REV29:.2f}"],
        ["Revenue growth (%)", "", f"{(REV_H[1] / REV_H[0] - 1) * 100:.0f}", f"{(REV_H[2] / REV_H[1] - 1) * 100:.0f}", "", f"{(REV27 / REV_H[2] - 1) * 100:.0f}", f"{G28 * 100:.0f}", f"{B[1] * 100:.0f}"],
        ["Data centre revenue", f"{DC_H[0]:.2f}", f"{DC_H[1]:.2f}", f"{DC_H[2]:.2f}", "", f"{DC27:.2f}", f"{DC28:.2f}", ""],
        ["Gross margin (%)", pc(GM_H[0]), pc(GM_H[1]), pc(GM_H[2]), "57.5 to 58.5", pc(FY27_GM), pc(GM28), ""],
        ["Operating income", f"{REV_H[0] * OM_H[0]:.2f}", f"{REV_H[1] * OM_H[1]:.2f}", f"{REV_H[2] * OM_H[2]:.2f}", "", f"{OPINC27:.2f}", f"{OPINC28:.2f}", f"{P['o29']:.2f}"],
        ["Operating margin (%)", pc(OM_H[0]), pc(OM_H[1]), pc(OM_H[2]), "", pc(OM27), pc(OM28), pc(B[2])],
        ["EPS, diluted (US$)", f"{EPS_H[0]:.2f}", f"{EPS_H[1]:.2f}", f"{EPS_H[2]:.2f}", "1.05 to 1.15", f"{EPS27:.2f}", f"{EPS28:.2f}", f"{EPS29:.2f}"],
        ["Consensus EPS (US$)", "", "", "", "", f"{CONS_EPS_27:.2f}", f"{CONS_EPS_28:.2f}", ""],
        [f"P/E at US${PRICE:,.2f} (x)", "", "", f"{PE26:.0f}", "", f"{PE27:.0f}", f"{PE28:.0f}", f"{PE29:.0f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6, 7},
))
A(caption("*FY27E to FY29E are my own estimates; FY28E revenue is management's US$20bn outlook of 6 October 2026. FY2027 is the "
          "year to about 30 January 2027. Income lines are Marvell's non-GAAP measures, which exclude stock-based pay "
          f"(US${SBC_Q2 * 1000:.0f}m in Q2 FY27, {SBC_PCT_Q2 * 100:.1f}% of revenue) and acquisition amortisation; GAAP EPS in the first "
          f"half of FY27 was US${GAAP_EPS_H1:.2f} against US${NG_EPS_H1:.2f} non-GAAP. Operating income to FY26 is revenue times the reported "
          "margin. Consensus from stockanalysis.com: FY27 updated 7 October 2026; FY28 from S&P Global data of 2 October, before the Investor "
          "Day. History from Marvell's results releases."))

A('<div class="keeptogether">')
A(section("Two charts: earnings that compound, and a value above the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue and non-GAAP diluted EPS, FY24A to FY29E; FY24A to FY26A per Marvell, the rest my estimates. Right: value per "
          "share from the base case, the probability-weighted cases, the sensitivity grid and the bear to bull range, against the "
          f"US${PRICE:,.2f} price (red) and the stockanalysis.com average analyst target, updated 7 October 2026."))
A('</div>')

A(section("The thesis: the translators at each end of the torch"))
A(para("Go back to the torches from the September piece. Shout to someone three streets away and the words smear into noise. Flashes "
       "of light carry, but someone at each end must turn words into flashes and back again, without a mistake. Those two translators "
       "do not care who is talking. More talkers, talking faster, need more of them."))
A(para("<strong>Marvell is one of those translators.</strong> It bought the job in April 2021, when it completed its purchase of Inphi. "
       "Its optical DSPs sit inside the transceivers at each end of a fibre, cleaning up a signal that carries two bits per pulse. Around "
       "them it sells the amplifiers and drivers beside the laser, the modules that link data centres, and the Ethernet switch chips the "
       f"plugs slot into. Data centre revenue was US${Q_DC[-1] / 1000:.2f}bn in the quarter to 1 August 2026, {DC_SHARE_Q2 * 100:.0f}% "
       f"of the total and up {DC_G_Q2 * 100:.0f}% on a year earlier. In May Marvell guided interconnect, the largest part of the data "
       "centre business, to grow more than 70% in fiscal 2027; in March it had guided custom chips to grow more than 20%, from "
       f"US${CUSTOM_26:.1f}bn in fiscal 2026."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_dc.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_split.png"></div></div>')
A(caption("Left: revenue by fiscal quarter, data centre (with its share) and communications and other, US$m; Q2 FY27 is the quarter to "
          "1 August 2026. Source: Marvell results releases, 3 December 2024 to 27 August 2026. Right: data centre revenue by business. "
          f"FY26 custom (US${CUSTOM_26:.1f}bn) and switching (above US$0.3bn) as disclosed on the 5 March 2026 call, the remainder derived; "
          "FY27E and FY28E are my split around management's outlook. Marvell does not report interconnect in dollars."))
A('</div>')
A(para(f"<strong>The test the piece set.</strong> It said to watch how much growth comes from optics rather than custom chips. On my "
       f"split, the remainder outside custom and switching, mostly interconnect, grows {REST_G27 * 100:.0f}% in fiscal 2027 and supplies "
       f"about {REST_SHARE_G27 * 100:.0f}% of the data centre growth; custom supplies about {CUS_SHARE_G27 * 100:.0f}%. In fiscal 2028 "
       f"data centre revenue rises to about US${DC28:.0f}bn, Marvell's Investor Day figure, and on my split the remainder still supplies "
       f"about {REST_SHARE_G28 * 100:.0f}% of the growth, custom about {CUS_SHARE_G28 * 100:.0f}%. Custom's turn comes in fiscal 2029: "
       f"Marvell now targets more than US${CUSTOM29_ID:.0f}bn of custom revenue that year, more than three times fiscal 2028."))

A(section("Where I was wrong in September"))
A(para("My piece said: \"On the same call, Marvell said it would make about $1 billion of capacity prepayments to suppliers in fiscal "
       "2027, to secure supply of 1.6T optical DSPs and switch chips.\" The call was the one of 27 August, and Dan Durn, the finance "
       "chief, did repeat the US$1bn plan on it. But neither he nor anyone else on that call or the May call, when the plan was first "
       "given, tied the money to optical DSPs or switch chips. Durn said the prepayments back the design wins Marvell has secured and "
       "will be set against future material purchases."))
A(para("The 10-Q for the quarter to 1 August describes \"capacity reservation arrangements with certain foundries and partners\", and "
       "the 10-K's commitments note names foundries and test and assembly partners. The balance sheet line, prepayments on supply "
       f"capacity reservation agreements, rose from US${PREPAY_JAN * 1000:.1f}m to US${PREPAY_AUG * 1000:.1f}m in six months. So the "
       "prepayments show a company buying capacity ahead of demand across the whole business, in a year when custom chips ramp hard in "
       "the second half. They are not evidence for the optical half in particular. What showed me the slip was reading the 10-Q's note "
       "against my own sentence. The claim does not rest on the prepayments, and the revenue mix still supports it. The piece and the "
       "claim stay as published."))

A(section("The plug is staying, for now"))
A(para("My piece said I was wrong if the translation moved off the plug, into linear or co-packaged optics. On the August call Matt "
       "Murphy, the chief executive, said pluggable modules remain the main form factor for scale-out networks and that he did not "
       "expect that to change; 800G demand remains strong and 1.6T is ramping rapidly. The twist is scale-up, the links inside one large "
       "AI system, where Marvell expects optics to move close to the chip. It bought Celestial AI for US$3.5bn in February to make "
       "co-packaged parts and forecasts a US$500m annualised run rate from them in the fourth quarter of fiscal 2028. At the Investor Day "
       "it put interconnect revenue growth at about 65% a year from fiscal 2026 to 2031, behind only custom at about 80%. Where the "
       "translation does leave the plug, Marvell is so far one of the companies taking it."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_margin.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: non-GAAP operating margin (bars) and gross margin (line) by fiscal quarter, against the Q3 FY27 gross margin guide; "
          "gross margin slips as custom grows, operating margin rises on cost control. Right: MRVL month-end close, September 2023 to the "
          f"{PRICE_DATE} close (Nasdaq.com to 5 October, stockanalysis.com after), against my target."))
A('</div>')

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At US${PRICE:,.2f} Marvell is worth about US${MCAP:.0f}bn on common shares and US${MCAP_FD:.0f}bn with Nvidia's preferred "
       f"as converted, with US${NETDEBT:.1f}bn more debt than cash. The shares closed at US${LO_CLOSE:.2f} on 4 February 2026, "
       f"peaked at a close of US${HI_CLOSE:.2f} on 4 June (intraday high US${HI52:.2f} on 18 June), and fell to US${LO_JUL:.2f} on 30 "
       f"July. They rose {ID_MOVE * 100:.1f}% on the day of the Investor Day, to US${PX_6OCT:.2f}, and have risen {RISE_DEC25 * 100:.0f}% "
       f"since the end of 2025 and {SINCE_PIECE * 100:.1f}% since my piece. They trade at {PE26:.0f} times FY26 non-GAAP EPS of "
       f"US${EPS_H[2]:.2f}, and {PE28:.0f} times my FY28 estimate."))
A(para(f"<strong class='lead'>What the price needs.</strong> By October 2027 the market will price fiscal 2029. At {BASE_PE} times, "
       f"the median of six peers, US${PRICE:,.2f} needs FY29 earnings of US${NEED_EPS29:.2f} a share. At my {pc(B[2], 0)} operating "
       f"margin that needs revenue of about US${NEED_REV29:.1f}bn: management's US$20bn for FY28, already up 67%, plus another "
       f"{NEED_G29 * 100:.0f}%. Marvell's custom target alone adds about US${FY29_PATH_ADD:.0f}bn in FY29 on my FY28 custom estimate, "
       "so the price allows for most of it to slip."))
A(para("<strong class='lead'>Where I differ.</strong> I do not take management's path. Getting from US$20bn to the US$80bn midpoint "
       "in three years means growing about 59% a year, and I take 40% for FY29. Even so, the price needs less than I assume. "
       "The growth beyond FY28 leans towards custom, and the Google deal points that way: its warrant for "
       f"{WARRANT_SH * 1000:.1f}m shares at US${WARRANT_PX:.2f} vests one tranche for each US$500m of custom revenue, across "
       f"{WARRANT_TRANCHES} tranches, so it covers up to US${WARRANT_REV:.0f}bn through fiscal 2033. Custom work is lumpier and the "
       f"buyers are stronger. Non-GAAP gross margin has slipped from {Q_GM[0]}% in the quarter to May 2024 to {Q_GM[-1]}%, and Marvell "
       f"guides 57.5 to 58.5% this quarter because of the custom ramp; the FY31 model allows {LT_GM[0] * 100:.0f} to {LT_GM[1] * 100:.0f}%, "
       "\"influenced by product mix\". So I pay no more than the peer median multiple for it, and get the upside from earnings, not "
       f"from a rerating. The toll stays the largest line: interconnect is {FY31_INT_SHARE * 100:.0f}% of the FY31 midpoint."))

A(section("Valuation, with the working"))
A(para(f"I value Marvell on non-GAAP EPS, the basis on which it guides, twelve months out, so on FY29. FY27 takes the reported first "
       f"half, the third quarter at the guide's midpoints (US${Q3_REV:.2f}bn, {pc(H2_GM, 0)} gross margin, US${Q3_OPEX * 1000:.0f}m of "
       f"costs; EPS US${Q3_EPS:.2f}) and a fourth quarter of US${Q4_REV:.2f}bn, what \"roughly $12 billion\" leaves, at "
       f"{Q4_OPINC / Q4_REV * 100:.1f}% operating margin. FY28 takes management's US$20bn, {pc(GM28, 0)} gross margin, costs growing "
       f"at about half the rate of revenue, as the Investor Day model repeats, and the guided {pc(TAX28, 0)} tax: {pc(OM28)} operating "
       f"margin and US${EPS28:.2f} a share, against a pre-Investor Day consensus of US${CONS_EPS_28:.2f}. FY29 grows {B[1] * 100:.0f}% "
       f"at {pc(B[2], 0)} operating margin, on the way to the 44 to 46% target, with the long-term {pc(TAX29, 0)} tax rate and "
       f"{SH29 * 1000:.0f}m shares. {BASE_PE} x US${EPS29:.2f} = {usd(BASE_VALUE)}; my target is {usd(tgt)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "FY29 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", f"AI spending pauses: no growth in FY29, operating margin {pc(SCEN[0][2], 0)}", usd(pb["eps29"], 2),
         f"{SCEN[0][3]}x", usd(bear), chg(bear), "25%"],
        ["Base", f"Growth {B[1] * 100:.0f}%, operating margin {pc(B[2], 0)}", usd(EPS29, 2), f"{BASE_PE}x",
         usd(base), chg(base), "50%"],
        ["Bull", f"Management's path: growth {SCEN[2][1] * 100:.0f}%, operating margin {pc(SCEN[2][2], 0)}",
         usd(pu["eps29"], 2), f"{SCEN[2][3]}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [10, 40, 11, 9, 11, 11, 8]))
A(caption(f"All cases start from management's FY28 outlook of US${REV28_IN:.0f}bn. The bear case is not fanciful: the shares closed at "
          "US$58.37 at the end of April 2025, and revenue fell in fiscal 2024. The band: I go long when my base value is 15% or more "
          f"above the price; at {usd(BASE_VALUE)} it is {(BASE_VALUE / PRICE - 1) * 100:.0f}% above."))
A('</div>')
grid = [[e * m for m in SENS_PE] for e in SENS_EPS]
above = sum(v > PRICE for r in grid for v in r)
above15 = sum(v > PRICE * 1.15 for r in grid for v in r)
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
A('<div class="keeptogether">')
A(section("Sensitivity: FY29 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["FY29 EPS"] + [f"{m}x" for m in SENS_PE],
    [[usd(e, 2)] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(r)]
     for i, (e, r) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{NUMW[above].capitalize()} of the nine cells sit above today's price, and {NUMW[above15]} by more than 15%. Each of the "
       f"{NUMW[9 - above]} at or below it needs a multiple of {SENS_PE[0]} times, or FY29 earnings of US${SENS_EPS[0]:.2f} at "
       f"{SENS_PE[1]} times. Every "
       "figure is live in the accompanying model, so a change to growth, margin, tax, shares or the multiple moves the value."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [[c, t, (f"{p:.1f}x" if p else "n/m"), w] for c, t, p, w in PEERS],
    num_cols={2},
), [20, 15, 12, 53]))
A(caption("Forward P/E from stockanalysis.com, retrieved 6 October 2026 during US trading; Marvell's at the 7 October close. The peer "
          "median, excluding Marvell, is 33.4 times. Multiples only; no view on the peers' shares."))
A('</div>')

A(section("Shares and dilution"))
A(para(f"Marvell had {COMMON_OUT * 1000:.1f}m common shares on 21 August 2026 and guides to 921m diluted this quarter. On top sit "
       f"Nvidia's US$2.0bn of preferred stock, bought on 31 March, which converts into {PREF_ASCONV * 1000:.1f}m shares at "
       f"US${PREF_CONV:.2f} and is worth about US${NVDA_STAKE:.1f}bn at the price; the Google warrant, which would add about "
       f"{WARRANT_NET * 1000:.0f}m net shares at the price if fully vested; and up to {CELESTIAL_MAX_SH * 1000:.1f}m shares and about "
       "US$233m in cash still due to Celestial AI's sellers on revenue milestones through fiscal 2029. Stock-based pay was "
       f"US${SBC_Q2 * 1000:.0f}m in the August quarter, {SBC_Q2 / SBC_Q2_PY:.1f} times a year earlier. Buybacks, US$400m in the first "
       f"half, offset some of it. I use {SH28 * 1000:.0f}m diluted shares for FY28 and {SH29 * 1000:.0f}m for FY29."))

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Early Dec 2026 (date not yet announced)", "Q3 FY27 results (quarter to October)", "Revenue against US$3.15bn +/- 5%; data centre up more than 20% sequentially; gross margin"],
        ["Early Mar 2027", "Q4 FY27 results and FY27 10-K", "FY28 guide against US$20bn; ten largest customers' share; custom against interconnect"],
        ["Through FY28", "Custom ramp towards the FY29 target", "Whether custom revenue tracks to more than three times FY28 in FY29"],
        ["Through 2027", "1.6T ramp; first scale-up optics revenue", "Whether 1.6T links keep a DSP on board; co-packaged run rate towards US$500m"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The cycle turns.</strong> If the largest cloud companies slow spending, volume falls whatever Marvell's share of each "
       f"link; the bear case is a {abs(bear / PRICE - 1) * 100:.0f}% fall. <strong>Custom is lumpy.</strong> Programmes are won and lost "
       "by generation, the buyers run their own chip teams, and gross margin already slips as custom grows. <strong>Targets are not "
       "results.</strong> The fiscal 2031 range is a plan set in a presentation, not guidance, and Marvell had not filed it with the SEC "
       "by 8 October. <strong>The translation "
       "moves.</strong> If 1.6T or 3.2T links drop the DSP for linear optics, or co-packaged optics spread from scale-up into scale-out, "
       "the toll moves to whoever makes the switch chip; Marvell makes switch chips and now co-packaged parts, so it would compete on "
       "different ground rather than lose outright."))
A(para(f"<strong>Few, large buyers.</strong> The ten largest customers took {TOP10[1] * 100:.0f}% of FY26 revenue, up from "
       f"{TOP10[0] * 100:.0f}%; one distributor took {DIST_A_Q2[1] * 100:.0f}% of revenue in the August quarter, against "
       f"{DIST_A_Q2[0] * 100:.0f}% a year earlier. <strong>Quality of earnings.</strong> Non-GAAP figures exclude stock-based pay of "
       f"{SBC_PCT_Q2 * 100:.1f}% of revenue, which has more than doubled in a year."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Out of the long, into no call:</strong> a price above about US${round(REVISIT_LONG, -1):,.0f} on unchanged estimates, "
       f"which would leave my base case less than 15% above it, or evidence that FY29 earnings will fall below about "
       f"US${EPS_FOR_LONG:.2f}, the level the long needs at today's price, such as Marvell cutting the FY29 custom target back towards "
       "US$10bn. <strong>Into more conviction:</strong> the Investor Day targets repeated in an SEC filing or a results release, and "
       "data centre revenue in the quarter to October rising more than 20% on the quarter before, as guided."))
A(para(f"<strong>The call is wrong if</strong> {WRONG_IF[0].lower() + WRONG_IF[1:]}"))
A('</div>')

A(section("Conclusion"))
A(para("My piece of 28 September argued that Marvell is paid every time AI chips talk, through the signal processor in each optical "
       "plug. The year of results behind it supports that claim: interconnect is the largest part of the data centre business, guided "
       "to grow more than 70% this year, and Marvell expects pluggable optics to stay the norm in scale-out networks. I was wrong about "
       "one thing: Marvell never said its US$1bn of prepayments was for optical DSPs. The Investor Day raised fiscal 2028 to about "
       "US$20bn and kept interconnect the largest line in the fiscal 2031 plan. The price needs only about "
       f"US${NEED_REV29:.1f}bn of FY29 revenue; I take US${REV29:.0f}bn, below management's path, at the peer median multiple. "
       f"{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {usd(tgt)}; range {usd(bear)} to {usd(bull)}. "
       "Medium, because the plan is a presentation, not yet results."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY27E", "FY28E", "FY29E", "Basis"],
    [
        ["Revenue, US$bn", f"{REV27:.2f}", f"{REV28_IN:.2f}", f"{REV29:.2f}", f"Q3 guide midpoint; Q4 {Q4_REV:.2f} from the US$12bn outlook; FY28 Investor Day outlook; FY29 mine"],
        ["Gross margin (non-GAAP)", pc(FY27_GM), pc(GM28), "", "H2 FY27 guide 57.5 to 58.5%; same range in FY28 (CFO)"],
        ["Operating expenses, US$bn", f"{OPEX27:.2f}", f"{OPEX28:.2f}", "", "FY27 guide US$2.55bn; FY28 grows at half the rate of revenue"],
        ["Operating margin (non-GAAP)", pc(OM27), pc(OM28), pc(B[2]), "Prior model 38 to 40%; FY31 target model 44 to 46%"],
        ["Interest and other, US$bn", f"{4 * OTHER_Q:.3f}", f"{OTHER28:.3f}", f"{OTHER29:.3f}", "Q3 guide about US$36m expense a quarter"],
        ["Tax rate (non-GAAP)", pc(TAX27, 0), pc(TAX28, 0), pc(TAX29, 0), "11% in FY27; about 13% guided for FY28; 15% in the FY31 model"],
        ["Diluted shares, m", "", f"{SH28 * 1000:.0f}", f"{SH29 * 1000:.0f}", "Q3 guide 921m; awards, warrant and Celestial shares net of buybacks"],
        ["Target multiple", "", "", f"{BASE_PE}x", "Median of six peers: ALAB 69.9x, LITE 51.5x, COHR 36.0x, CRDO 30.8x, AVGO 20.9x, NVDA 19.8x"],
    ],
), [24, 9, 9, 9, 49]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Marvell quarterly results releases furnished on Form 8-K (Exhibit 99.1), 3 December 2024 to 27 August 2026, '
  'with their comparative columns, for revenue, data centre revenue, non-GAAP margins, EPS, stock-based pay, balance sheet and the Q3 '
  'FY27 guide. Marvell Form 10-Q for the quarter to 1 August 2026 (filed 28 August 2026) for shares outstanding, Celestial AI and its '
  'contingent consideration, prepayments on supply capacity reservation agreements, capacity reservation arrangements and customer '
  'shares. Marvell Forms 10-K for FY26 (filed 11 March 2026) and FY25 (filed 12 March 2025) for ten-largest-customer shares and purchase '
  'commitments. Marvell Forms 8-K of 31 March 2026 (Nvidia preferred stock) and 19 August 2026 (Google warrant). Marvell earnings calls '
  'of 5 March, 27 May and 27 August 2026. Marvell Investor Day presentation, 6 October 2026, investor.marvell.com, for the FY28 and '
  'FY31 revenue targets, data centre and custom targets, the FY31 split and the FY31 target model; transcript of the remarks from '
  'stockanalysis.com. Share prices from Nasdaq.com historical data to 5 October and stockanalysis.com for 6 and 7 October; consensus '
  'EPS, average target and multiples from stockanalysis.com, retrieved 6 to 8 October 2026. Estimates for FY27 to FY29 and the data '
  'centre split are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 28 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/marvell-collects-the-toll/">thephysicallayer.fyi/journal/marvell-collects-the-toll</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Marvell. Personal research, not investment advice.</p>')
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
