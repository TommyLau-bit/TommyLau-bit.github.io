# -*- coding: utf-8 -*-
"""Coherent Corp. (NYSE: COHR) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/coherent.md.
"""
import datetime, statistics
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Coherent Corp. (NYSE: COHR)"
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


bear, base, bull = (x["value"] for x in SC)
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
tgt_word = "draft target" if CALL["draft"] else "target"
peer_med = statistics.median(p[2] for p in PEERS if p[4] == "peer")
grid = [[e * mm for mm in SENS_PE] for e in SENS_EPS]
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
mar_move = PX_MAR2 / PX_MAR2_PRE - 1
aug_move = PX_AUG13 / PX_AUG12 - 1

A('<h1 class="doctitle">Coherent Corp.</h1>')
A('<p class="docsubtitle"><b>NYSE: COHR | Datacentre transceivers and indium phosphide lasers; industrial lasers and materials | Saxonburg, Pennsylvania</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{usd(PRICE, 2)} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made. '
      'Q1 FY27 results are due on 4 November 2026, after this draft.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{usd(PRICE, 2)}, NYSE close {PRICE_DATE}; record close {usd(HI_CLOSE, 2)} on {HI_CLOSE_DATE}, intraday high {usd(HI_INTRA, 2)} on {HI_INTRA_DATE}"),
    ("Market value", f"US${MCAP:.1f}bn on {SHARES_OUT:.1f}m shares (10 Aug 2026)"),
    ("Net debt, 30 Jun 2026", f"US${NET_DEBT / 1000:.2f}bn; enterprise value about US${EV:.1f}bn"),
    ("FY26 (to 30 Jun 2026)", f"Revenue US${REV['FY26'] / 1000:.2f}bn, up 22.5%; non-GAAP EPS US$5.61; Datacenter &amp; Communications {DC_SHARE26 * 100:.0f}% of revenue"),
    ("Q1 FY27 guide (12 Aug 2026)", "Revenue US$2.2 to 2.4bn; non-GAAP gross margin 39.5 to 41.5%; EPS US$1.85 to 2.05"),
    ("P/E", f"{PE_C27:.1f}x FY27 and {PE_C28:.1f}x FY28 consensus; {PE_E28:.1f}x my FY28E"),
    ("Consensus (stockanalysis.com)", f"Average target {usd(CONS_TP)} ({CONS_N} analysts, low {usd(CONS_TP_LO)})"),
    ("Next event", "Q1 FY27 results, Wednesday 4 November 2026, after the NYSE close (announced 14 Oct)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Coherent is paid every time the plug is bought again. At US$210, the shares pay for this year\'s step and none after it.</p>')
A(para("Coherent builds the optical plugs that link the racks of an AI cluster, and grows the indium phosphide lasers inside them. "
       "My piece of 4 September argued that the plug survives co-packaged optics and is bought again at every speed step, from "
       "800 gigabits to 1.6 terabits. Coherent is the company most paid by that claim, and most hurt if it fails."))
A(para(f"The claim holds so far. Coherent's data centre business grew {DC_GROWTH26 * 100:.0f}% in fiscal 2026, 1.6T is ramping and 800G "
       f"still grows. Yet the shares have fallen {abs(OFF_HIGH) * 100:.0f}% from their June record, to {PE_C28:.1f} times consensus "
       "fiscal 2028 earnings, as fear of co-packaging and of a laser glut has spread across optics."))
A(para(f"<b>{my_call}: {CALL['direction']}, {tgt_word} {usd(tgt)}, {conv} conviction.</b> Twenty-two times my fiscal 2028 EPS of "
       f"US${E28:.2f} gives {usd(BASE_VALUE)}, {chg(BASE_VALUE)}, inside a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} "
       f"({chg(bull)}). Conviction is low: results land in two days, the business has fallen before, and it burns cash to grow."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (fiscal years to 30 June; non-GAAP EPS as Coherent defines it)"))
A(datatable(
    ["US$ million unless stated", "FY24A", "FY25A", "FY26A", "FY27E*", "FY28E*"],
    [
        ["Revenue", m(REV["FY24"]), m(REV["FY25"]), m(REV["FY26"]), m(F27["rev"]), m(B["rev"])],
        ["Growth (%)", "", f"{(REV['FY25'] / REV['FY24'] - 1) * 100:.0f}", f"{(REV['FY26'] / REV['FY25'] - 1) * 100:.0f}",
         f"{(F27['rev'] / REV['FY26'] - 1) * 100:.0f}", f"{G28 * 100:.0f}"],
        ["Datacenter &amp; Communications", "", m(DC["FY25"]), m(DC["FY26"]), "", ""],
        ["Non-GAAP gross margin (%)", "", f"{NG_GM['FY25'] * 100:.1f}", f"{NG_GM['FY26'] * 100:.1f}", f"{F27['gm'] * 100:.1f}", f"{GM28 * 100:.1f}"],
        ["Non-GAAP operating margin (%)", "", f"{NG_OPM['FY25'] * 100:.1f}", f"{NG_OPM['FY26'] * 100:.1f}", f"{F27['opm'] * 100:.1f}", f"{B['opm'] * 100:.1f}"],
        ["Non-GAAP EPS (US$)", f"{NG_EPS['FY24']:.2f}", f"{NG_EPS['FY25']:.2f}", f"{NG_EPS['FY26']:.2f}", f"{E27:.2f}", f"{E28:.2f}"],
        ["Consensus EPS (US$)", "", "", "", f"{CONS_EPS27:.2f}", f"{CONS_EPS28:.2f}"],
        [f"P/E at {usd(PRICE, 2)} (x)", "", "", f"{PE_26:.1f}", f"{PE_E27:.1f}", f"{PE_E28:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*My estimates. FY24A to FY26A from Coherent's results releases; FY24 and FY25 non-GAAP as recast, FY24 EPS derived from the "
          "FY25 release. Consensus from stockanalysis.com (S&amp;P Global), updated 30 October 2026. Industrial revenue fell 10% in FY26 "
          "after the sale of the aerospace and defence business in September 2025 and a Munich unit in January 2026."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: the plug is now four fifths of the business, and the margin is rising"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_segments.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_margin.png"></div></div>')
A(caption("Left: revenue by segment, US$bn, with Datacenter &amp; Communications as a share of revenue; the last bar is the Q1 FY27 guide "
          "midpoint. Right: non-GAAP gross and operating margin, per cent; the 42% gross margin target is from the 12 August 2026 call. "
          "Sources: Coherent results releases, 6 November 2024 to 12 August 2026; FY25 non-GAAP as recast."))
A('</div>')

A(section("The thesis: the bulb is bought again, and Coherent makes both bulb and filament"))
A(para("Go back to the house from the piece. The wires in the walls, the glass fibre, are laid once. The bulbs, the optical plugs, are "
       "replaced whenever the owner wants more light. Coherent sells the whole bulb, and it also grows the filament, the indium "
       "phosphide laser, in its own fabs. Each brighter generation of chips sends the owner back to the shop."))
A(para(f"The numbers show the shop busy. Datacenter &amp; Communications revenue rose from US${DC['FY25'] / 1000:.2f}bn to "
       f"US${DC['FY26'] / 1000:.2f}bn in fiscal 2026, {DC_GROWTH26 * 100:.0f}%, and the 10-K says the growth was driven primarily by "
       "transceivers. The segment was 64% of revenue in the September 2024 quarter and 79% in the June 2026 quarter. Its segment profit rose 47%, to "
       "US$1,330m, a 25.2% margin."))
A(para("<b>Paid at every speed step.</b> On the 12 August call, by third-party transcripts, management said growth would come from "
       "both 800G and 1.6T, and the 1.6T ramp had pulled in. Its results deck lists 1.6T, 3.2T and 6.4T transceivers among existing "
       "growth engines, and the 10-K shows research on 400 gigabit per lane parts for 3.2T and 6.4T. Each step needs new plugs and "
       "faster lasers, so Coherent is paid again each time."))
A(para("<b>The constraint is the laser, and Coherent is adding it.</b> Management said on the call that laser output, not assembly, "
       "caps data centre revenue, and that it made about 80% more indium phosphide lasers in the June quarter than a year earlier. "
       "The deck says internal output is on track to double by the end of 2026 and more than double again by 2027. Its six-inch lines "
       "in Texas and Sweden make EMLs, continuous lasers and photodiodes at higher yields than three-inch lines; the finance chief "
       "put a six-inch wafer at about four times the output for half the cost."))
A(para("<b>Nvidia is committed.</b> On 2 March 2026 it bought 7,788,161 new shares at US$256.80, US$2bn, alongside a "
       "multi-billion-dollar purchase commitment and capacity rights (Form 8-K). The same filing gives Nvidia access to five more "
       "Coherent product families related to co-packaged optics. On the call Coherent said fiscal 2027 is effectively booked, with orders into "
       "calendar 2028."))
A('<div class="keeptogether">')
A(section("The co-packaging question: what Coherent loses, and what it keeps"))
A(para("Co-packaging is a bigger question for Coherent than for Lumentum. Lumentum mainly sells the laser, which both designs need. "
       "Coherent's largest product is the whole plug, and a co-packaged switch has no plug between racks. So Coherent loses the "
       "module where co-packaging wins, and keeps the laser that feeds it, in a removable module."))
A(para("It has hedged both ways. The deck dates first co-packaged revenue to the second half of 2026, and the call to the December "
       "quarter, with scale-up use from the second half of 2027. Coherent sizes the extra market from co-packaged and near-packaged "
       "optics at over US$15bn. The piece's evidence still says the plug stays: Nvidia's Vera Rubin blueprints of 15 September picked "
       "pluggable switches for both fabrics. I cannot split Coherent's revenue between plug and laser from its filings; it does not "
       "report one."))
A('</div>')
A(para("<b>The claim holds.</b> Coherent's results support it on every point I can test: plugs growing at two speeds at once, the "
       "laser the limit, and co-packaging still arriving as an addition, not a replacement. Coherent also makes optical circuit "
       "switches, which its 10-K lists in the same segment, and it said on the call that their revenue grew in the June quarter."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {usd(PRICE, 2)} Coherent is worth US${MCAP:.1f}bn, with net debt of US${NET_DEBT / 1000:.2f}bn. The shares trade at "
       f"{PE_26:.1f} times fiscal 2026 earnings, {PE_C27:.1f} times the fiscal 2027 consensus of US${CONS_EPS27:.2f} and {PE_C28:.1f} times "
       f"the fiscal 2028 consensus of US${CONS_EPS28:.2f}. Six optics and networking peers have a median forward P/E of {peer_med:.1f} "
       f"times; Lumentum, the laser maker, trades at 38.5 times. Coherent's forward P/E was {FWD_PE_PEAK:.1f} times at the end of June."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["2 Mar 2026", "Nvidia invests US$2bn at US$256.80", f"up {mar_move * 100:.1f}%"],
        ["2 Jun 2026", f"Record close {usd(HI_CLOSE, 2)}", "Peak"],
        ["13 Aug 2026", "Day after Q4 results and a guide above US$2.2bn", f"down {abs(aug_move) * 100:.1f}%"],
        ["22 Oct 2026", "Day after Nvidia dated SPIL's co-packaged engine capacity", f"down {abs(OCT22_MOVE) * 100:.1f}%"],
        ["30 Oct 2026", "No Coherent news found", f"down {abs(OCT30_MOVE) * 100:.1f}%"],
    ],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: Coherent month-end close, January 2024 to the 30 October 2026 close, against my base value (red) and Nvidia's purchase "
          "price (dotted). Nasdaq.com, retrieved 2 November 2026. Right: daily closes against the previous close. I found no "
          "company statement for 22 or 30 October; the 22 October fall came the day after Nvidia's release, which proves timing, not cause."))
A('</div>')
A(para(f"<strong class='lead'>What the price assumes.</strong> At my base multiple of 22 times, {usd(PRICE, 2)} needs fiscal 2028 "
       f"earnings of US${EPS_IMPLIED:.2f}, the same as my fiscal 2027 estimate of US${E27:.2f}. The price pays for the 1.6T step "
       "Coherent has already booked and assumes earnings stop growing after it, in the year Coherent's laser output more than doubles "
       f"again. The shares are {abs(VS_NV) * 100:.0f}% below what Nvidia paid eight months ago."))
A(para("<strong class='lead'>Where I differ.</strong> I read the fall as the market pricing two fears at once: that co-packaging retires "
       "the plug, and that new laser capacity ends the shortage. The first fear runs ahead of the evidence: the newest blueprints still "
       "pick the plug, and the claim runs to the end of 2028. The second is real, and my base case allows for it. I grow fiscal 2028 "
       f"revenue {G28 * 100:.0f}% against the 38% consensus implies, and my fiscal 2028 EPS sits "
       f"{abs(E28 / CONS_EPS28 - 1) * 100:.0f}% below consensus. Even so the base value is {UP_BASE * 100:.0f}% above the price."))

A(section("Valuation, with the working"))
A(para("I value Coherent on non-GAAP EPS, the basis it guides on, twelve months out: by October 2027 the market will price fiscal 2028, "
       "the year to June 2028. For fiscal 2027 I build each quarter. Revenue of US$2.32bn in the first quarter, within the guide, rises to "
       "US$2.90bn in the fourth, just short of the US$3bn quarter Coherent targets. Gross margin rises from 40.5% to 42.0% and operating "
       f"costs from US$410m to US$480m a quarter. With US$120m of interest and other costs, a 19% tax rate and 204m shares, that gives "
       f"US${E27:.2f}, against the US${CONS_EPS27:.2f} consensus. My first quarter is US${F27['q1eps']:.2f}, against a US$1.85 to 2.05 guide."))
A(para(f"For fiscal 2028 I grow revenue {G28 * 100:.0f}% to US${B['rev'] / 1000:.1f}bn, with a 42.0% gross margin and operating costs "
       f"of 16.5% of revenue, an operating margin of {B['opm'] * 100:.1f}%. On 207m shares that gives US${E28:.2f}. All are my estimates."))
A(para(f"<strong class='lead'>The multiple.</strong> I use {BASE_PE:.0f} times. Coherent's own forward P/E averaged {HIST_FWD_PE_AVG:.1f} "
       f"times at the ends of fiscal 2023 to 2025, and six peers sit at a {peer_med:.1f} times median. I take a discount to both: "
       "Coherent's margin is below the laser makers', and the plug is the part co-packaging would replace. "
       f"{BASE_PE:.0f} x US${E28:.2f} = {usd(BASE_VALUE, 2)}, rounded down to a {tgt_word} of {usd(tgt)}."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "FY28 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "Industry laser capacity meets an inventory pause, as in FY24: flat revenue, gross margin 37.5%, costs 18%", f"US${SC[0]['e28']:.2f}", f"{SC[0]['mult']}x", usd(bear), chg(bear), "25%"],
        ["Base", "Growth 25%, gross margin 42%, costs 16.5% of revenue", f"US${SC[1]['e28']:.2f}", f"{SC[1]['mult']:.0f}x", usd(base), chg(base), "50%"],
        ["Bull", "The plug stays and 3.2T ramps on time: growth 40%, gross margin 43.5%, costs 16%", f"US${SC[2]['e28']:.2f}", f"{SC[2]['mult']}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 41, 11, 9, 11, 11, 8]))
A(caption("All cases start from my FY27E revenue of US$10.42bn and use the same interest, tax and share count. Revenue fell 9% in FY24, "
          "when customers worked through stock; the bear case repeats a pause of that kind and halves the price."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: FY28 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["FY28 EPS"] + [f"{mm}x" for mm in SENS_PE],
    [[f"US${e:.2f}"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{W[n_above]} of the nine cells sit above the price and {W[n_15].lower()} sit 15% or more above it. The two below it both "
       "need EPS of US$9.50 at 22 times or less, which is no growth on fiscal 2027. A long needs the base 15% or more above the "
       f"price, a short 25% or more below. At {UP_BASE * 100:.0f}% above, {my_call.lower()} is long."))
A('</div></div>')
A(f'<img class="chart" src="file://{D}/chart_valuation.png" style="width:62%">')
A(caption(f"Value per share from the base case, the weighted cases, the grid and the bear to bull range, against the {tgt_word} (red) and the price (grey)."))
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "What they make"],
    [[c, t, f"{p:.1f}x", w] for c, t, p, w, g in PEERS],
    num_cols={2},
), [22, 16, 12, 50]))
A(caption(f"Forward P/E from stockanalysis.com at the 30 October 2026 close. Peer median excluding Coherent: {peer_med:.1f}x. Innolight "
          "and Eoptolink, the largest transceiver makers, list in China and are left out. Multiples are used only to set the range; no "
          "view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Cash: Coherent is betting its balance sheet on the plug"))
A('<div class="chartsrow"><div class="col left">')
A(f'<img class="chart" src="file://{D}/chart_cash.png">')
A('</div><div class="col">')
A(para(f"Fiscal 2026 operating cash flow was US${OCF['FY26']:.0f}m against US${CAPEX['FY26']:,.0f}m of capital spending, so free "
       f"cash flow was minus US${abs(FCF26):,.0f}m. Inventory rose 80% to US${INVENTORY['FY26'] / 1000:.2f}bn. The 10-K lists purchase "
       f"commitments of US${PURCH_27}bn in fiscal 2027 and US${PURCH_LATER}bn after. Nvidia's US$2bn funded the gap. If demand pauses, "
       "this is where it shows first."))
A('</div></div>')
A(caption("Operating cash flow and capital spending, US$bn, fiscal years to June. Sources: Form 10-K for fiscal 2026 and the 12 August 2026 release."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["4 November 2026 (announced)", "Q1 FY27 results, after the NYSE close", "Revenue against US$2.2 to 2.4bn; gross margin above 39.5%; the Q2 guide; 1.6T and laser output"],
        ["December 2026 quarter", "First co-packaged optics revenue, per Coherent", "Whether it is lasers and engines, and whether plug revenue still grows"],
        ["First half of calendar 2027", "Third six-inch InP site, Zurich (call)", "Laser output more than doubling again by end 2027"],
        ["Undated", "Nvidia's Feynman reference architecture", "Plug or co-packaged switch for the compute fabric: the claim's test"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Co-packaging arrives early.</strong> If a blueprint before the end of 2028 makes a co-packaged switch the default, Coherent "
       "loses the plug between racks and keeps only the laser and engine. My piece's claim breaks with it."))
A(para("<strong>The shortage ends at once.</strong> Coherent, Lumentum and Broadcom are all adding indium phosphide capacity, and Nvidia funded "
       "two of them on one day. If supply lands together, prices fall; the bear case halves the shares."))
A(para("<strong>Few buyers, and Chinese rivals.</strong> Two customers each took more than 10% of fiscal 2026 revenue (10-K). Innolight and "
       "Eoptolink compete for the same transceiver orders. A BIS inquiry into past sales to Huawei, opened in January 2025, is unresolved."))
A(para("<strong>Cash and dilution.</strong> Free cash flow was negative by US$1.0bn in fiscal 2026. Special share awards granted in August "
       "vest only at prices from US$454.43, so they cost little unless the shares more than double."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into no call:</strong> a price above about {usd(LONG_BELOW)}, where the base value is less than 15% above it, or a gross "
       "margin that stalls below 40% while revenue grows. Q1 results may move both."))
A(para(f"<strong>{'My draft view' if CALL['draft'] else 'My call'} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para("My September piece argued that the plug between racks survives co-packaging and is bought again at every speed step. Coherent "
       f"builds that plug and grows its laser, and its results agree: data centre revenue up {DC_GROWTH26 * 100:.0f}%, 1.6T pulled in, "
       f"laser output doubling. At {usd(PRICE, 2)} the price pays 22 times my fiscal 2027 earnings and nothing for the next step. "
       f"{my_call}: {CALL['direction']}, {tgt_word} {usd(tgt)}, {conv} conviction; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "Q1 FY27E", "Q2", "Q3", "Q4", "FY28E"],
    [
        ["Revenue, US$m", m(F27_REV[0]), m(F27_REV[1]), m(F27_REV[2]), m(F27_REV[3]), m(B["rev"])],
        ["Non-GAAP gross margin", *[f"{g * 100:.1f}%" for g in F27_GM], f"{GM28 * 100:.1f}%"],
        ["Non-GAAP operating costs", *[f"US${o:.0f}m" for o in F27_OPEX], f"{OPEX28 * 100:.1f}% of revenue"],
        ["Interest and other, tax, shares", "US$120m a year", "19%", "204m", "", "US$120m, 19%, 207m"],
    ],
), [28, 14, 12, 12, 12, 22]))
A(caption(f"All my estimates. Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Coherent fourth quarter fiscal 2026 results release and investor presentation (Form 8-K, Exhibits 99.1 and 99.2, '
  '12 August 2026), for results, segment revenue, the balance sheet, cash flow, guidance, laser output, six-inch lines and the product '
  'roadmap. Coherent Form 10-K for the year to 30 June 2026, filed 14 August 2026, for shares, segment profit, customers, purchase '
  'commitments, the Nvidia share issue and the BIS inquiry. Coherent quarterly results releases from 6 November 2024 to 6 May 2026. '
  'Coherent Form 8-K of 2 March 2026 on Nvidia\'s investment and of 31 August 2026 on special share awards. Coherent\'s 14 October 2026 '
  'announcement of its 4 November results date. Q4 fiscal 2026 call (12 August 2026), from the third-party transcript published by '
  'stockanalysis.com. Nvidia DGX SuperPOD reference architectures (15 September 2026) and release of 21 October 2026, '
  'as cited in the journal piece. Share prices from Nasdaq.com, checked against Yahoo Finance; consensus, targets and peer multiples from stockanalysis.com (S&amp;P '
  'Global data); all retrieved 2 November 2026. Estimates for fiscal 2027 and 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 4 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/ten-thousand-chips-one-thought/">thephysicallayer.fyi/journal/ten-thousand-chips-one-thought</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Coherent. Personal research, not investment advice.</p>')
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
