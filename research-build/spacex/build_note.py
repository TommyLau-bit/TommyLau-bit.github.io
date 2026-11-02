# -*- coding: utf-8 -*-
"""SpaceX (Nasdaq: SPCX) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/spacex.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "SpaceX (Nasdaq: SPCX)"
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


def bn(x, d=0):
    v = x / 1000
    s = f"{abs(v):,.{d}f}"
    if d == 1 and 0 < abs(v) < 0.05:
        s = f"{abs(v):,.2f}"
    return f"({s})" if v < 0 else s


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = usd(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
grid = [[grid_value(e, m) for m in SENS_MULT] for e in SENS_SI]

A('<h1 class="doctitle">SpaceX</h1>')
A('<p class="docsubtitle"><b>Space Exploration Technologies Corp. | Nasdaq: SPCX | Launch, Starlink, AI computing and models | Starbase, Texas</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{usd(PRICE, 2)} (Nasdaq close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{usd(PRICE, 2)}, close {PRICE_DATE}; IPO at US$135.00 on 12 June 2026; highest close {usd(HI_CLOSE, 2)} ({HI_CLOSE_DATE}); lowest {usd(LO_CLOSE, 2)} ({LO_CLOSE_DATE})"),
    ("Market value", f"About US${MCAP / 1e6:.2f} trillion on {SHARES:,.0f}m Class A and B shares (15 Oct 2026); EV US${EV_MKT / 1e6:.2f} trillion"),
    ("Balance sheet, 30 Sep 2026", f"Cash and securities US${(CASH + SECS) / 1000:.1f}bn; debt and finance leases US${(DEBT_CUR + DEBT_LT) / 1000:.1f}bn"),
    ("Q3 2026", "Revenue US$14.6bn (up 161%); Adjusted EBITDA US$8.8bn; SI US$7.6bn, Starlink US$5.2bn, Space US$1.8bn"),
    ("Guide", "Q1 2027 revenue US$33bn to 37bn; Q4 2026 capex US$35bn to 40bn"),
    ("Consensus (Yahoo, 2 Nov)", f"2027 revenue US${CONS_REV_27 / 1000:.0f}bn (range 72 to 290); EPS US${CONS_EPS_27:.2f}; P/E {PE_27C:.1f}x"),
    ("Control", "Elon Musk about 82% of votes after the IPO; a controlled company"),
    ("Next events", "Starship Flight 15 (about November); 180 day lock-up ends 8 Dec 2026; Q4 results date not announced"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">SpaceX\'s price leaves about US${RESIDUAL / 1000:.0f} billion for businesses it does not yet report. '
  'Orbital compute is the largest of them.</p>')
A(para("My journal piece of 2 November argued that in orbit the power is nearly free and the heat is the bill: by the end of "
       "2028 no compute satellite will be in service at SpaceX's own target of 100 kW per tonne launched, and no launch price "
       "will reach US$200 a kilogram. SpaceX reports no orbital compute business, so this note values the three it does report "
       "and asks how much of the price is left for orbit."))
A(para(f"On my 2027 estimates, Starlink, the AI business and launch are worth about US${TERR_EV / 1e6:.2f} trillion. The "
       f"market's enterprise value is US${EV_MKT / 1e6:.2f} trillion, which leaves about US${RESIDUAL / 1000:.0f}bn, "
       f"{RESIDUAL_SHARE * 100:.0f}% of it, for Starship beyond launch, spectrum, chips and orbit. SpaceX states a \"vehicle "
       f"efficiency\" of {AI1_KW_T:.0f} kW per ton for its first AI satellite: a quarter short of its target if that is compute per metric ton."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction.</b> My base value is {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, inside "
       f"my no-call band, within a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} ({chg(bull)}). I would revisit above about "
       f"US${REVISIT_SHORT:.0f} or below about US${REVISIT_LONG:.0f}."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (US$ billion; Segment Adjusted EBITDA is SpaceX's measure)"))
A(datatable(
    ["", "2024A", "2025A", "9M 2026A", "2026E*", "2027E*", "2027 consensus"],
    [
        ["Space (launch) revenue", bn(REV_24["Space"], 1), bn(REV_25["Space"], 1), bn(REV_9M26["Space"], 1), bn(FY26["Space"][0], 1), bn(R27["Space"], 1), ""],
        ["Connectivity (Starlink) revenue", bn(REV_24["Connectivity"], 1), bn(REV_25["Connectivity"], 1), bn(REV_9M26["Connectivity"], 1), bn(FY26["Connectivity"][0], 1), bn(R27["Connectivity"], 1), ""],
        ["Super Intelligence (SI) revenue", bn(REV_24["SI"], 1), bn(REV_25["SI"], 1), bn(REV_9M26["SI"], 1), bn(FY26["SI"][0], 1), bn(R27["SI"], 1), ""],
        ["Total revenue", bn(REV_TOT_24, 1), bn(REV_TOT_25, 1), "27.1", bn(REV_26E, 1), bn(REV_27E, 1), bn(CONS_REV_27, 1)],
        ["Connectivity Segment Adjusted EBITDA", bn(EBITDA_24["Connectivity"], 1), bn(EBITDA_25["Connectivity"], 1), bn(EBITDA_9M26["Connectivity"], 1), bn(FY26["Connectivity"][1], 1), bn(E27["Connectivity"], 1), ""],
        ["SI Segment Adjusted EBITDA", bn(EBITDA_24["SI"], 1), bn(EBITDA_25["SI"], 1), bn(EBITDA_9M26["SI"], 1), bn(FY26["SI"][1], 1), bn(E27["SI"], 1), ""],
        ["Space Segment Adjusted EBITDA", bn(EBITDA_24["Space"], 1), bn(EBITDA_25["Space"], 1), bn(EBITDA_9M26["Space"], 1), bn(FY26["Space"][1], 1), bn(E27["Space"], 1), ""],
        ["Capital spending", bn(11163, 1), bn(20737, 1), bn(48069, 1), "", "", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E is the first nine months as reported plus my fourth quarter; 2027E is mine, not SpaceX's. 2024 and 2025 from the "
          "final prospectus (424B4, 12 June 2026; 2024 segment revenue derived from the reported 2025 increases); 9M 2026 from the "
          "results release of 20 October 2026. SI was reported as the AI segment until the third quarter. Consensus: Yahoo Finance, "
          "37 analysts, 2 November 2026. Brackets are negative."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: where the revenue is going, and a valuation that sits below the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: revenue by segment; 2026E and 2027E are mine, the red marker the 2027 consensus. Right: value per share from the "
          f"scenarios, the sensitivity grid, the weighted cases, my base and the three businesses alone, against the {usd(PRICE, 2)} "
          "price (red) and the average analyst target."))
A('</div>')

A(section("The thesis: the courier, the phone network, and fins nobody has weighed"))
A(para("Think of a sealed vacuum flask on a sunny windowsill with a laptop inside. The sun charges it for nothing, but the flask "
       "traps the heat, so the laptop needs a black fin to glow the heat away, and every fin goes up by courier, charged by the "
       "kilogram. A buyer of SpaceX buys the courier, a phone network in the sky and a large ground data centre business. "
       "The buyer is also asked to pay for fins nobody has yet weighed in orbit."))
A(para("SpaceX reports three segments. Space is launch: Falcon 9, Falcon Heavy, Dragon and Starship's development. Connectivity "
       "is Starlink. Super Intelligence holds xAI, X and, since 14 August, Cursor, bought for an implied US$60bn. It rents computing "
       f"capacity and sells Grok, advertising and software. In the third quarter SI brought in US$7.6bn, against US$5.2bn for "
       f"Starlink and US$1.8bn for Space, and earned US$5.0bn of Segment Adjusted EBITDA. One SI customer, Customer B, supplied "
       f"{CUST_B_Q3 * 100:.1f}% of all revenue. Orbital compute appears in none of this; the 10-Q of 22 October does not mention it."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_perkg.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_sotp.png"></div></div>')
A(caption("Left: launch services revenue over customer payload mass, US$ per kg, my arithmetic from the 8-K releases of 4 August and "
          "20 October 2026; Q1 figures are the half year less the second quarter. Not a list price. Right: my base sum of the parts per "
          "share, built up part by part; the hatched red bar is what the price pays beyond it."))
A('</div>')
A(para(f"SpaceX's own Starmind page, read on 2 November, describes its AI satellite, AI1: up to {AI1_KW_PEAK:.0f} kW of "
       f"compute at peak and {AI1_KW_AVG:.0f} kW on average, a {AI1_RAD_M2:.0f} m² liquid radiator, a {AI1_SOLAR_KW:.0f} kW solar "
       f"array and a \"vehicle efficiency\" of \"{AI1_KW_T:.0f} kW / ton\", without saying whether that is compute or solar power, "
       f"or which ton. Read as compute per metric ton, it is {AI1_GAP * 100:.0f}% short of the 100 kW target the claim tests. On average compute it implies about {AI1_MASS_T:.1f} tonnes a satellite, on my arithmetic; a radiator of "
       f"that area at the space station's 14 kg per m² would weigh about {AI1_RAD_ISS_T:.1f} tonnes on its own."))
A(para(f"The launch side says the same from SpaceX's books. In the first nine months of 2026 launch customers paid US$2,108m for "
       f"251 tonnes of payload: about {usd(round(KG_9M26_USD, -2))} a kilogram, {KG_X_THRESHOLD:.0f} times the US$200 the claim tests. "
       "Revenue per kilogram is a mix of missions, not a price list, and Starship has flown only SpaceX's own payloads. "
       "Nothing in the record points to US$200 soon."))
A(para("<b>Where I was wrong in November.</b> The piece said that \"a compute satellite flown in 2028, SpaceX's earliest date, "
       "would on that life wear out around 2033\". On the third quarter call of 20 October, Gwynne Shotwell, SpaceX's president, "
       "said, in SpaceX's own transcript, \"we'll begin flying Mobile V2 and Starmind satellites in 2027\", and the Starmind page plans \"thousands of AI "
       "satellites starting as soon as late 2027\". The piece also wrote that \"nobody has yet shown what a kilowatt in orbit "
       "weighs\". For a satellite in service that holds, but SpaceX has stated a design figure, 75 kW per ton, which I missed by "
       "reading only the SEC filings. What showed me the slip was reading SpaceX's call and website for this note. The claim stands: "
       "the test may come a year sooner, and the design figure SpaceX has shown, read as compute per metric ton, sits below "
       "the target the claim names."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {usd(PRICE, 2)} SpaceX trades at {PE_27C:.1f} times the 2027 consensus EPS of US${CONS_EPS_27:.2f}, and its "
       f"enterprise value is {EV_REV27C:.1f} times 2027 consensus revenue of US${CONS_REV_27 / 1000:.0f}bn. The estimates run from "
       "US$72bn to US$290bn of revenue. The guide is steep: US$33bn to 37bn of revenue in the first quarter of 2027 alone, US$100bn "
       "of annualised revenue by the end of 2026, nameplate compute of 2.5 to 3 GW by then, and, in Musk's words, surprise at less "
       "than 13 GW by the end of 2027. Fourth quarter capital spending is guided at US$35bn to 40bn."))
A(para(f"<strong class='lead'>What the price leaves.</strong> I take most of that at face value. The three businesses come to "
       f"about US${TERR_EV / 1e6:.2f} trillion on my 2027 estimates, against an enterprise value of US${EV_MKT / 1e6:.2f} trillion. "
       f"The difference, about US${RESIDUAL / 1000:.0f}bn or {RESIDUAL_SHARE * 100:.0f}%, about US${RESIDUAL_PS:.0f} a share, is what "
       "the price pays for beyond them: Starship beyond its launch revenue, Starlink Mobile, the Terafab chip plant, and orbital "
       "compute, the largest and the one SpaceX puts at the centre of its story."))
A(para(f"<strong class='lead'>The gap in the piece's units.</strong> My SI value is about US${SI_EV_PER_GW / 1000:.0f}bn per GW of "
       f"the 13 GW Musk expects by the end of 2027. At that rate the gap buys about {RESIDUAL_GW:.1f} GW of orbital compute, before "
       f"any discount for time: about {round(RESIDUAL_SATS, -3):,.0f} AI1 satellites, or about {round(RESIDUAL_T_AI1, -3):,.0f} tonnes "
       f"at 75 kW per ton read as compute per metric ton, about {RESIDUAL_X_MASS25:.0f} times all the mass SpaceX launched in 2025."))
A(para(f"<strong class='lead'>Where I differ.</strong> If the claim holds, the satellites flown by the end of 2028 will be "
       "heavier per kilowatt than the target and launch will still cost far more than US$200 a kilogram, so orbit cannot earn "
       f"its share of the gap within any horizon I can value. I credit US$100bn to all unreported options together, which leaves "
       f"about US${GAP_AFTER_OPTIONS / 1000:.0f}bn, roughly US${GAP_AFTER_OPTIONS / SHARES:.0f} a share, for orbit and the other "
       "bets to earn. That argues for caution, not a short: the price sits 17% above my base, not twice it, and the bigger "
       "twelve-month swing is the ground business, whether SI reaches its guide, at what margin, and whether Customer B stays."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Close"],
    [
        ["12 Jun 2026", "IPO at US$135.00; first close", usd(DAY1_CLOSE, 2)],
        ["16 Jun 2026", f"Highest close; intraday high {usd(HI_INTRA, 2)}", usd(HI_CLOSE, 2)],
        ["5 Aug 2026", "Lowest close; Q2 results were filed on 4 August", usd(LO_CLOSE, 2)],
        ["21 Oct 2026", f"Day after Q3 results, {Q3_MOVE * 100:+.1f}%", usd(PX_Q3_DAY, 2)],
        ["30 Oct 2026", f"Latest close, {abs(OFF_HI) * 100:.0f}% below the high", usd(PRICE, 2)],
    ],
), [20, 58, 22]))
A('</div></div>')
A(caption("Left: SpaceX weekly close since the IPO, against the IPO price and my base value (red). Yahoo Finance history pages, read "
          "2 November 2026. Right: closes on dates that matter; results are released after the market closes."))
A('</div>')

A(section("Valuation, with the working"))
A(para("I value SpaceX as a sum of its parts on my 2027 estimates, the year the market will price by October 2027. Starlink and SI "
       "are valued on Segment Adjusted EBITDA; Space on revenue, because Starship spending holds its earnings near zero. I add net "
       f"cash of US${NETCASH / 1000:.1f}bn at 30 September and divide by {SHARES:,.0f}m shares. I do not deduct fourth quarter capital "
       "spending or the US$40bn Apollo GPU lease committed to on 24 October, because both buy capacity my 2027 estimates assume. SI's "
       "margin is 48%, between the second quarter's 45% and the third's 66%; the finance chief expects fourth quarter company gross "
       "margins closer to the second quarter's, citing one-time benefits and customer mix in the third. My 2027 revenue sits 7% below consensus."))
A('<div class="keeptogether">')
A(section("Sum of the parts, base case"))
SH = BASE_EQ
rowsS = [
    ["Connectivity (Starlink)", "2027E EBITDA " + bn(E27["Connectivity"], 1), f"{MULT['Connectivity']:.0f}x", bn(SOTP["Connectivity"]), f"{SOTP['Connectivity'] / SH * 100:.0f}%", usd(SOTP["Connectivity"] / SHARES, 1)],
    ["Super Intelligence", "2027E EBITDA " + bn(E27["SI"], 1), f"{MULT['SI']:.0f}x", bn(SOTP["SI"]), f"{SOTP['SI'] / SH * 100:.0f}%", usd(SOTP["SI"] / SHARES, 1)],
    ["Space (launch)", "2027E revenue " + bn(R27["Space"], 1), f"{MULT['Space']:.0f}x", bn(SOTP["Space"]), f"{SOTP['Space'] / SH * 100:.0f}%", usd(SOTP["Space"] / SHARES, 1)],
    ["Net cash, 30 Sep 2026", "", "", bn(NETCASH), f"{NETCASH / SH * 100:.0f}%", usd(NETCASH / SHARES, 1)],
    ["Options, including orbital compute*", "", "", bn(OPTIONS), f"{OPTIONS / SH * 100:.0f}%", usd(OPTIONS / SHARES, 1)],
    ["Equity value", "", "", f"{BASE_EQ / 1000:,.0f}", "100%", usd(BASE_VALUE, 1)],
]
A(cols(datatable(["Part", "Basis, US$bn", "Multiple", "Value, US$bn", "Share", "Per share"], rowsS,
                 num_cols={1, 2, 3, 4, 5}, total_row_idx=len(rowsS) - 1), [30, 22, 10, 13, 10, 15]))
A(caption("*My estimate of everything not in the three segments today. Multiples are mine, set against trailing peers (table below): "
          "Starlink at 25x against T-Mobile US at 7.9x, because it grew 69% last quarter at a 67% margin; SI at 13x forward, below "
          "CoreWeave at 20.1x and Oracle at 15.3x trailing, because rented computing needs constant new chips; Space at 15x revenue, "
          "below Rocket Lab's 39.7x, because Falcon is mature."))
A('</div>')
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
b, m, x = SCEN[0][1], SCEN[0][2], SCEN[0][3]
u, um, ux = SCEN[2][1], SCEN[2][2], SCEN[2][3]
A(cols(datatable(
    ["Case", "What happens", "SI 2027 EBITDA", "SI multiple", "Options", "Value", "Change", "Weight"],
    [
        ["Bear", f"Rented-compute prices fall; SI US${b['SI'] / 1000:.0f}bn at {m['SI'] * 100:.0f}%; Starlink {x['Connectivity']:.0f}x", f"US${b['SI'] * m['SI'] / 1000:.0f}bn", f"{x['SI']:.0f}x", "none", usd(bear), chg(bear), "25%"],
        ["Base", f"SI US${R27['SI'] / 1000:.0f}bn at {M27['SI'] * 100:.0f}%; Starlink {MULT['Connectivity']:.0f}x", f"US${E27['SI'] / 1000:.1f}bn", f"{MULT['SI']:.0f}x", "US$100bn", usd(base), chg(base), "50%"],
        ["Bull", f"SI US${u['SI'] / 1000:.0f}bn at {um['SI'] * 100:.0f}%; Starlink {ux['Connectivity']:.0f}x; orbit priced", f"US${u['SI'] * um['SI'] / 1000:.0f}bn", f"{ux['SI']:.0f}x", "US$300bn", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 5, 6, 7}, total_row_idx=3,
), [8, 32, 11, 8, 10, 11, 11, 9]))
A(caption("Space and Starlink revenue also move in each case (Assumptions and Scenarios tabs in the model). Net cash is held at 30 "
          "September. The bull case is the one in which the market's extra is earned, orbital compute included."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: SI 2027 EBITDA against its multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["SI EBITDA"] + [f"{mm:.0f}x" for mm in SENS_MULT],
    [[f"US${e / 1000:.1f}bn"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_SI, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_short = sum(v <= PRICE * 0.75 for r in grid for v in r)
A(para(f"With everything else at base, only {n_above} of the nine cells, the bottom right, sits above the price, and {n_short} sit "
       "25% or more below it. None sits 15% above. Under my rule a short needs the base 25% or more below the price and a long "
       f"needs it 15% above. At {abs(BASE_VALUE / PRICE - 1) * 100:.0f}% below, the base is a no call."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "EV, US$bn", "EV/EBITDA", "EV/sales", "What they do"],
    [[c, t, f"{ev:,.0f}", (f"{e + 1e-9:.1f}x" if e else "n/m"), f"{s + 1e-9:.1f}x", w] for c, t, ev, e, s, w, g in PEERS],
    num_cols={2, 3, 4},
), [17, 9, 11, 11, 10, 42]))
A(caption("Trailing multiples from stockanalysis.com, 2 November 2026, at the 30 October close; n/m where EBITDA is negative or "
          "not meaningful (Nebius 172x). SpaceX's own EV/sales is trailing. Multiples only set my ranges; no view on the peers' "
          "shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["About November 2026", "Starship Flight 15, with an attempt to catch both stages", "Reuse is what moves cost per kg"],
        ["8 December 2026", "Last of the 180 day lock-up ends (424B4); Musk's and the extended lock-ups run to mid 2027", "Supply of shares"],
        ["By end 2026", "Apollo GPU lease (about US$40bn) expected to close", "Funding of the 2027 ramp"],
        ["Early 2027 (date not announced)", "Q4 2026 results", "SI revenue and margin; Customer B; the 2027 path"],
        ["2027", "First Starmind (AI1) satellites; Google and Planet's prototypes", "Any weighed kW per tonne in service"],
        ["Open", "Tesla and SpaceX special committees", "Terms, and who pays whom"],
        ["31 December 2028", "My piece's claim is tested", "100 kW per tonne in service; US$200 per kg published"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view, either way"))
A(para("<strong>SI misses the ramp.</strong> Revenue must more than double from the third quarter of 2026 to the first of 2027. "
       "Musk aims to \"rent at effectively the spot-market rate\" rather than sign long-term deals; if rented-compute prices fall as capacity floods in, "
       "revenue and margin fall together. That is most of the bear case."))
A(para("<strong>One customer.</strong> Customer B was 34.5% of third quarter revenue, and one customer held 27.7% of receivables "
       "on 30 September. SpaceX does not name it."))
A(para("<strong>Cash and debt.</strong> Capital spending was US$48.1bn in nine months, with US$35bn to 40bn more guided for the "
       "fourth quarter, US$25bn of bonds issued in June and a binding commitment to a US$40bn GPU lease. A slower ramp leaves that spending earning less."))
A(para("<strong>Control and Tesla.</strong> Musk held about 82% of the votes after the IPO. Both boards have special committees "
       "studying a combination with Tesla; the terms could move value either way, and any deal also needs Musk's approval as controlling shareholder."))
A(para("<strong>Orbit works.</strong> If a satellite flies at 100 kW per tonne by 2028, or launch reaches US$200 a kilogram, the "
       "gap could be earned. That is the bull case's option value, and the claim's falsifier."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Towards a short:</strong> a price above about US${REVISIT_SHORT:.0f}, where my base would sit 25% below it. "
       f"<strong>Towards a long:</strong> a price below about US${REVISIT_LONG:.0f}, where it would sit 15% above, or a weighed AI "
       "satellite in service at 100 kW per tonne, which would break my claim and lift the option value."))
A(para(f"<strong>The view is wrong if</strong> {WRONG_IF[0].lower() + WRONG_IF[1:]}"))
A('</div>')

A(section("Conclusion"))
A(para(f"The November piece argued that in orbit the heat is the bill. SpaceX's own disclosures since say the same: its first AI "
       f"satellite is designed at a stated {AI1_KW_T:.0f} kW per ton against a 100 kW target, and its launch customers paid about "
       f"{usd(round(KG_9M26_USD, -2))} a kilogram this year against a US$200 test. The piece got SpaceX's earliest date wrong: the "
       f"first satellites are now due in 2027. For the shares, orbit is a gap, not the whole price. The three reported businesses "
       f"explain about three quarters of the enterprise value; the rest, about US${RESIDUAL / 1000:.0f}bn, rests on bets that earn "
       f"nothing yet. {my_call}: {CALL['direction']}, {conv} conviction; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "Basis"],
    [
        ["Starlink revenue growth", f"{FY26['Connectivity'][0] / REV_25['Connectivity'] * 100 - 100:.0f}%", f"{R27['Connectivity'] / FY26['Connectivity'][0] * 100 - 100:.0f}%", "Q3 2026 grew 69% year on year; 13.6m consumer subscribers"],
        ["Starlink margin", f"{FY26['Connectivity'][1] / FY26['Connectivity'][0] * 100:.0f}%", f"{M27['Connectivity'] * 100:.0f}%", "Q3 2026: 66.7%"],
        ["SI revenue, US$bn", f"{FY26['SI'][0] / 1000:.1f}", f"{R27['SI'] / 1000:.0f}", "Q1 2027 guide US$33bn to 37bn for the whole company"],
        ["SI margin", f"{FY26['SI'][1] / FY26['SI'][0] * 100:.0f}%", f"{M27['SI'] * 100:.0f}%", "Q2 2026 44.7%, Q3 2026 65.5%"],
        ["Space revenue, US$bn", f"{FY26['Space'][0] / 1000:.1f}", f"{R27['Space'] / 1000:.1f}", "Falcon pipeline; Starship customers later"],
        ["Shares, m", f"{SHARES:,.0f}", "", "Class A and B at 15 October 2026; awards and options excluded"],
    ],
), [30, 14, 14, 42]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">SpaceX final prospectus (Form 424B4), 12 June 2026, for 2023 to 2025 and first quarter 2026 results, '
  'segment data, the lock-up schedule, voting control and the orbital compute disclosure. SpaceX results releases on Form 8-K, '
  'Exhibit 99.1, 4 August and 20 October 2026, for quarterly segment data, capital spending, launch services revenue, customer '
  'payload mass, Starlink subscribers and nameplate compute. SpaceX Form 10-Q for the quarter to 30 September 2026, filed 22 '
  'October 2026, for shares outstanding, backlog, customer concentration and the Tesla special committee. SpaceX Forms 8-K of 23 '
  'and 26 June, 14 August and 26 October 2026. SpaceX third quarter 2026 webcast, 20 October 2026, SpaceX\'s edited transcript '
  'at ir.spacex.com. SpaceX Starmind page (spacex.com), read 2 November 2026. Share prices and consensus from Yahoo Finance '
  'history and analysis pages, read 2 November 2026; average target and peer multiples from stockanalysis.com, 2 November 2026. '
  'Estimates for 2026 and 2027 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 2 November 2026, '
  '<a href="https://thephysicallayer.fyi/journal/data-centres-in-space/">thephysicallayer.fyi/journal/data-centres-in-space</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in SpaceX. Personal research, not investment advice.</p>')
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
