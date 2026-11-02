# -*- coding: utf-8 -*-
"""Entergy Corporation (NYSE: ETR) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/entergy.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Entergy Corporation (NYSE: ETR)"
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
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"US${q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


bear, base, bull = (x["value"] for x in SC)
tgt = CALL["target"]
tp_txt = usd(tgt, 2) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {usd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
view_txt = (f"{CALL['direction'].lower()}, with {conv} conviction" if CALL["direction"] == "NO CALL"
            else f"{CALL['direction'].lower()}, target {usd(tgt)}, {conv} conviction")
meta_bn = (META1_TOTAL + META2_TOTAL) / 1000

A('<h1 class="doctitle">Entergy Corporation</h1>')
A('<p class="docsubtitle"><b>NYSE: ETR | Regulated electric utilities in Louisiana, Arkansas, Mississippi and Texas | New Orleans, Louisiana</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{usd(PRICE, 2)} (NYSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{usd(PRICE, 2)}, NYSE close {PRICE_DATE}; record close {usd(HI_CLOSE, 2)} on 30 Apr 2026, intraday high {usd(HI_INTRA, 2)} on 1 May 2026"),
    ("Market value", f"US${MCAP:.1f}bn on {SHARES_OUT:.1f}m shares (30 Jun 2026 plus the 2 Sep forward settlement)"),
    ("Net debt, 30 Sep 2026", f"US${NET_DEBT / 1000:.1f}bn; enterprise value about US${EV:.1f}bn; FFO to adjusted debt 16.8%"),
    ("2026 guide", "Adjusted EPS US$4.35 to 4.45, narrowed 2 Nov 2026; 2030 outlook US$7.05 to 7.35 (9 Jun 2026, affirmed 2 Nov)"),
    ("P/E", f"{PE_G26:.1f}x 2026 guide midpoint; {PE_C27:.1f}x 2027 consensus (US${CONS_EPS27:.2f}); {PE_E28:.1f}x 2028 outlook midpoint"),
    ("Dividend", f"US${DIV_Q:.2f} a quarter, declared 2 Nov 2026, up 6%; yield {DIV_YIELD * 100:.1f}%"),
    ("Consensus (stockanalysis.com)", f"Average target {usd(CONS_TP, 2)} ({CONS_N} analysts); forward P/E {FWD_PE_SA:.1f}x"),
    ("Next events", "LPSC vote on the second Meta agreement, December 2026 meeting, after a settlement with staff; Q4 results February 2027 (date not set)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Entergy bought its place in the turbine queue early, and Meta pays for the plants. At US$110 the shares already price the plan.</p>')
A(para("Entergy Louisiana builds the gas plants for Meta's Hyperion campus. My piece on building your own power argued that a campus building its own gas power "
       "swaps the grid's queue for the turbine makers'. Entergy's filings show that queue from the buyer's side: an exclusive "
       "agreement guarantees it one manufacturing slot a quarter, and it raised its minimum order from 15 to 27 sets in a year."))
A(para(f"The growth is real and well protected: Meta pays minimum bills, funds part of the build and owes an exit fee. But at "
       f"{PE_C27:.1f} times the 2027 consensus, and {FWD_PE_SA:.1f} times forward against {PEER_MED:.1f} times for large peers, the price "
       "pays for Entergy's outlook to 2030. The second Meta agreement, now settled with the regulator's staff and due for a vote in "
       "December, is already inside it."))
A(para(f"<b>{my_call}: {view_txt}.</b> Twenty-one and a half times the 2028 outlook midpoint of US${E28:.2f} gives {usd(BASE_VALUE)}, "
       f"{chg(BASE_VALUE)}, inside a range of {usd(bear)} ({chg(bear)}) to {usd(bull)} ({chg(bull)}). That is short of my 15% bar for a long."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (calendar years; adjusted EPS as Entergy defines it)"))
A(datatable(
    ["US$ per share unless stated", "2024A", "2025A", "2026G", "2027O", "2028O", "2030O"],
    [
        ["Entergy guide / outlook range", "", "", "4.35 to 4.45", "4.90 to 5.20", "5.55 to 5.85", "7.05 to 7.35"],
        ["Adjusted EPS (2026 on: my estimate, the midpoint)", f"{ADJ_EPS['2024A']:.2f}", f"{ADJ_EPS['2025A']:.2f}", f"{E26:.2f}", f"{E27:.2f}", f"{E28:.2f}", f"{MID['2030']:.2f}"],
        ["Growth (%)", "", f"{(ADJ_EPS['2025A'] / ADJ_EPS['2024A'] - 1) * 100:.1f}", f"{(E26 / ADJ_EPS['2025A'] - 1) * 100:.1f}",
         f"{(E27 / E26 - 1) * 100:.1f}", f"{(E28 / E27 - 1) * 100:.1f}", ""],
        ["Consensus EPS (stockanalysis.com)", "", "", f"{CONS_EPS26:.2f}", f"{CONS_EPS27:.2f}", "", ""],
        ["Projected rate base, US$bn (Entergy)", "", f"{RATE_BASE['2025E']}", f"{RATE_BASE['2026E']}", f"{RATE_BASE['2027E']}", f"{RATE_BASE['2028E']}", f"{RATE_BASE['2030E']}"],
        ["Capital plan that year, US$bn (10-Q)", "", "", f"{CAPEX['2026'] / 1000:.1f}", f"{CAPEX['2027'] / 1000:.1f}", f"{CAPEX['2028'] / 1000:.1f}", f"{CAPEX['2030'] / 1000:.1f}"],
        [f"P/E at {usd(PRICE, 2)} (x)", "", "", f"{PE_G26:.1f}", f"{PE_G27:.1f}", f"{PE_E28:.1f}", f"{PRICE / MID['2030']:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("G = Entergy's guide, narrowed on 2 November 2026; O = its outlooks from the Investor Day of 9 June 2026, affirmed on 2 November 2026. My estimates sit at the "
          "midpoints. 2024A and 2025A as reported (Q4 2025 release, 12 February 2026). Rate base is Entergy's internal estimate including "
          "construction work in progress. Consensus retrieved 2 November 2026."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: earnings on the company's own outlook, and a value close to the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_eps.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: adjusted EPS, 2024A and 2025A as reported, then the midpoints of Entergy's guide and outlooks with their ranges, against the "
          "2027 consensus (red). Right: value per share from the base case, the weighted cases, the sensitivity grid and the bear to bull "
          "range, against the price (grey) and the 15% bar for a long (red)."))
A('</div>')

A(section("The thesis: the utility that stood in the queue first"))
A(para("Think of the well from the piece. Your street needs water, and one big new neighbour needs a lot of it. The water company "
       "offers to dig a deep well for him. It books the drilling firm years ahead, makes the neighbour pay a minimum fee whether he "
       "draws water or not, and charges him if he walks away. The regulator lets the company earn a fixed return on every pipe it lays."))
A(para(f"That is Entergy. It earns an allowed return on its rate base, the value of the plants and wires it owns; in Louisiana the "
       f"allowed return on equity is 9.3 to 10.1%, on an equity ratio of about 51%. It plans to spend about US${CAPEX_TOTAL / 1000:.1f}bn "
       f"from 2026 to 2030 and projects rate base rising from US$46bn in 2025 to US$97bn in 2030, about {RB_CAGR * 100:.0f}% a year. "
       "Weather-adjusted industrial sales rose 9.6% in the first nine months of 2026, led by data centres and primary metals."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_ratebase.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: Entergy's projected rate base, Investor Day of 9 June 2026, and its capital plan by year, Form 10-Q for the quarter to "
          "30 June 2026. Right: Entergy month-end close, split-adjusted, January 2024 to the 30 October 2026 close, against my base value "
          "(red). Yahoo Finance, read 2 November 2026."))
A('</div>')
A(para("<b>Hyperion is the clearest case.</b> In October 2024 Entergy Louisiana asked the Louisiana Public Service Commission to approve "
       "three combined cycle gas plants, 2,262 MW, for a Meta data centre in Richland Parish. The commission approved a settlement in "
       "August 2025. Franklin Farms Units 1 and 2, about US$2.4bn together, are due in 2028 and Waterford 5 in 2029; a 500 kV line adds "
       "about US$0.5bn. In March 2026 Entergy Louisiana signed a second agreement with Evest LLC, another Meta subsidiary, and filed for "
       "seven more plants, 5,278 MW at about US$12.9bn, in service in 2030 and 2031, plus a US$1.4bn line. In April the commission set "
       "the case for its December 2026 meeting, and on 2 November Entergy said it had reached a settlement with the commission's staff, whose "
       "terms I could not yet read in a filing. These are the facts my piece used, and Entergy's filings match each of them."))
A(para(f"<b>The claim holds, and Entergy shows it from the buyer's side.</b> It signed an exclusive agreement with an unnamed major vendor to "
       "make power island equipment and combustion turbines for gas turbine sets larger than 400 MW. It guarantees one manufacturing "
       f"slot a quarter for up to five years. Entergy raised its minimum order of power island sets from 15 to 21 in the third quarter of 2025 and to "
       f"{PIE_MIN} in the second quarter of 2026, and had taken {PIE_DONE} by the end of June. A heavy turbine slot sold today ships in 2032; "
       "Hyperion's first plants arrive in 2028 and 2029, before Meta's lease begins in 2029, because Entergy ordered early. What a data "
       "centre buys from Entergy is a date."))
A(para(f"<b>The customer pays for the risk.</b> The second agreement makes Meta's subsidiary pay Entergy's incremental costs through "
       "contributions to construction, other advance payments and minimum monthly bills. If it leaves early, restructures or defaults, it "
       "owes Entergy's unrecovered costs, and a Meta Platforms guaranty backs it. The investor day listed 15 to 20 year terms for all its "
       f"large data centre contracts. Customer advances rose from US${CUST_ADV_DEC25 / 1000:.1f}bn at the end of 2025 to "
       f"US${CUST_ADV_JUN26 / 1000:.1f}bn at the end of June 2026, and the return on construction they fund added US$0.21 a share to "
       "the rise in EPS over the first nine months, against the same months of 2025."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {usd(PRICE, 2)} Entergy is worth US${MCAP:.1f}bn, with net debt of US${NET_DEBT / 1000:.1f}bn at the end of September. It trades "
       f"at {PE_G26:.1f} times the 2026 guide midpoint and {PE_C27:.1f} times the 2027 consensus of US${CONS_EPS27:.2f}. On "
       f"stockanalysis.com's forward measure it is {FWD_PE_SA:.1f} times, against a median of {PEER_MED:.1f} times for NextEra, Southern, "
       f"American Electric Power, Duke and Xcel: about {FWD_PE_SA - PEER_MED:.1f} turns more, like for like. The premium has a reason: Entergy's outlook takes adjusted EPS from US$3.91 in 2025 to "
       f"US$7.05 to 7.35 in 2030, about {EPS_CAGR * 100:.0f}% a year, and the consensus agrees with it. Third quarter results on 2 November, "
       "after this price, were strong: US$1.98 against US$1.53, about US$0.24 of it weather. Entergy narrowed the 2026 guide to US$4.35 "
       "to 4.45 and affirmed every outlook, which leaves the 2028 figure I value unchanged."))
A('<div class="keeptogether">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["30 Apr 2026", f"Record close {usd(HI_CLOSE, 2)}, the day after Q1 results", "Peak"],
        ["6 May 2026", "Day after a US$2.175bn share sale with forwards", f"down {abs(OFFER_MOVE) * 100:.1f}%"],
        ["29 Jul 2026", "Q2 results; guide and outlooks affirmed", f"down {abs(Q2_MOVE) * 100:.1f}%"],
        ["September 2026", "No company results", "down 6.6%"],
        ["October 2026", "Month to the 30 October close", f"up {OCT_MOVE * 100:.1f}%"],
        ["2 Nov 2026", "Q3 results, settlement with staff, dividend up 6%", "After this price"],
    ],
), [18, 64, 18]))
A(caption("Moves from the previous close to the close on the day; months are month-end to month-end. Yahoo Finance."))
A('</div>')
A(para("<strong class='lead'>Where I agree with the market.</strong> The growth is real and better protected than most utility growth. A "
       "customer that pays a minimum bill, funds part of the build and owes an exit fee is better than a new housing estate. Entergy "
       "reported 2025 in the top half of its range and affirmed the whole outlook on 2 November."))
A(para(f"<strong class='lead'>Where I differ: the December vote is not upside.</strong> The 10-Q says the updated 2026 to 2030 capital "
       "plan reflects incremental investment primarily for the resources in the March 2026 application. The settlement with staff makes "
       "an outright rejection less likely, but approval only keeps the plan whole; "
       f"rejection, or conditions that move cost back onto Entergy, cuts it. On my arithmetic the two Meta agreements are about "
       f"US${meta_bn:.1f}bn of plants and lines, about {META_SHARE * 100:.0f}% of the five-year plan by gross cost, taking Waterford 5 "
       "at the cost of one Franklin Farms unit, as Entergy's testimony suggests. That is a rough guide, not a bound: some spending falls "
       "after 2030 and customers fund part directly, while the second application also holds batteries and other lines the 10-Q does "
       "not cost. If all US$14.3bn of the second agreement's plants and main line entered rate base at the Louisiana allowed "
       f"return, they would earn about US${META2_NI:.0f}m a year, about US${META2_EPS:.2f} a share, from 2030, against the 2030 outlook of US$7.20."))
A(para("<strong class='lead'>The other customers are the real constraint.</strong> In June the commission's staff argued that the need "
       "for the Cottonwood plant Entergy wants to buy is driven mainly by data centre loads, whose owners should bear the cost. In January "
       "intervenors asked for an inquiry into the financing Meta arranged for Hyperion. In the second case they won, in part, a subpoena of Meta's "
       "data, which Meta moved to quash in July. Entergy says its contracts will save other customers about US$7bn over their lives. "
       f"Funding costs too: about US$7bn of new equity by 2030, US$4.1bn of it done by June, which is why EPS grows about {EPS_CAGR * 100:.0f}% "
       f"a year while rate base grows about {RB_CAGR * 100:.0f}%. <b>The price already pays {PE_E28:.1f} times the 2028 outlook midpoint.</b>"))

A(section("Valuation, with the working"))
A(para("I value Entergy on adjusted EPS, as it reports them, twelve months out: by October 2027 the market will price 2028 as the year "
       "ahead. For a regulated utility whose earnings follow rate base under formula rate plans, the price to earnings ratio is the method "
       "the market uses. My estimates sit at the midpoints of Entergy's own ranges, because it has delivered on them."))
A(para(f"<strong class='lead'>The multiple.</strong> I use {BASE_PE} times 2028 earnings: today's {PE_C27:.1f} times the 2027 consensus, "
       f"held a year forward. It assumes the premium over the {PEER_MED:.1f} times peer median, about {FWD_PE_SA - PEER_MED:.1f} turns like for "
       f"like, neither widens nor narrows while Entergy grows faster. {BASE_PE} x US${E28:.2f} = {usd(BASE_VALUE, 2)}, {(BASE_VALUE / PRICE - 1) * 100:.1f}% above the price."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "Multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "The commission rejects or heavily conditions the second Meta agreement; the growth premium goes", f"US${SC[0]['e28']:.2f}", f"{SC[0]['mult']:.0f}x", usd(bear), chg(bear), "25%"],
        ["Base", "The 2028 outlook midpoint holds; today's multiple held a year forward", f"US${SC[1]['e28']:.2f}", f"{SC[1]['mult']}x", usd(base), chg(base), "50%"],
        ["Bull", "Approval, more of the 7 to 12 GW data centre pipeline signs, the outlook rises", f"US${SC[2]['e28']:.2f}", f"{SC[2]['mult']:.0f}x", usd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {usd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 45, 11, 9, 10, 9, 7]))
A(caption("Bear earnings sit below the bottom of the 2028 outlook (US$5.55) and bull earnings above its top (US$5.85). The bear multiple of "
          "18x is near the low end of the large-utility peers. The 7 to 12 GW of data centre prospects beyond the base plan is from Entergy's "
          "Investor Day of 9 June 2026."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: 2028 EPS against the multiple"))
A('<div class="chartsrow"><div class="col left">')
grid = [[e * mm for mm in SENS_PE] for e in SENS_EPS]
A(datatable(
    ["2028 EPS"] + [f"{mm:g}x" for mm in SENS_PE],
    [[f"US${e:.2f}"] + [(f"<b>{usd(v)}</b>" if (i == 1 and j == 1) else usd(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_EPS, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
n_s = sum(v <= PRICE * 0.75 for r in grid for v in r)
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
A(para(f"{W[n_above]} of the nine cells sit above the price, but only {W[n_15].lower()} sit 15% or more above it, and all four need "
       f"24 times, or US$5.95 of earnings at {BASE_PE} times or more. {W[n_s]} sits 25% or more below. A long needs the base 15% or more "
       f"above the price, a short 25% or more below. At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, {my_call.lower()} is no call, with "
       f"{conv} conviction. Four dividends would lift the base case to about {((BASE_VALUE + 4 * DIV_Q) / PRICE - 1) * 100:.1f}%."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBITDA", "What they run"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w, g in PEERS],
    num_cols={2, 3},
), [20, 13, 11, 10, 46]))
A(caption(f"Forward P/E and EV/EBITDA from stockanalysis.com, updated 2 November 2026. Peer median forward P/E excluding Entergy: "
          f"{PEER_MED:.1f}x. Multiples are used only to set the range; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["November 2026 (not dated)", "Q3 Form 10-Q", "Terms of the Evest settlement with staff: cost sharing, credit support, any change to the plants"],
        ["December 2026 meeting", "LPSC vote on the second Meta agreement; Waterford 6 and Westlake", "Approval as filed, conditions that shift cost, or delay"],
        ["February 2027 (date not announced)", "Q4 2026 results and 2027 guide", "2028 outlook midpoint against US$5.90; equity still to raise"],
        ["2028", "Franklin Farms Units 1 and 2 in service", "On time and on budget; the first test of the queue place"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The December vote.</strong> The commission decides without a formal recommendation from the administrative law judge; "
       f"the release names a settlement with staff only. A rejection, delay or cost-shifting conditions cut a plan the price already assumes: the bear case, an "
       f"{abs(bear / PRICE - 1) * 100:.0f}% fall."))
A(para("<strong>Other customers and politics.</strong> Staff and intervenors pressed on who pays for data centre plants in three proceedings "
       "this year. If bills rise faster than Entergy has promised, the next approval gets harder."))
A(para("<strong>Construction.</strong> Entergy has its slots but must still build seven large plants on time; the second agreement carries "
       "penalties, up to termination, if it fails its performance obligations."))
A(para("<strong>Storms and funding.</strong> One bad Gulf Coast hurricane season can cost billions, though Entergy holds storm escrows and has "
       "used securitisation. It needed about US$2.9bn more equity by 2030 at the end of June; FFO to adjusted debt was 16.8% in the year to September."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price below about {usd(LONG_BELOW, 2)}, or a 2028 outlook raised to a midpoint of US$5.90 or more "
       f"after approval, which at {BASE_PE} times gives about {usd(5.90 * BASE_PE)}, 15% above the price. <strong>Into a short:</strong> a "
       f"price above about {usd(SHORT_ABOVE)}, or a rejection of the second agreement with the shares still near today's multiple."))
A(para(f"<strong>{my_call} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para("The piece argued that building your own gas power swaps the grid's queue for the turbine makers'. Entergy's filings "
       "show it from the buyer's side: one slot a quarter, a minimum order raised from 15 sets to 27 in a year, and plants for Meta that "
       "arrive in 2028 and 2029 because they were ordered early. The shares already pay "
       f"for it: {PE_C27:.1f} times next year's consensus, and the second Meta agreement is already inside the outlook. {my_call}: "
       f"{view_txt}; base value {usd(BASE_VALUE)}, range {usd(bear)} to {usd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Adjusted EPS, US$", f"{E26:.2f}", f"{E27:.2f}", f"{E28:.2f}", "Midpoints of Entergy's guide and outlooks; P/E of 21.5x on 2028E"],
        ["Waterford 5 cost", "", "", "US$1.19bn", "Half of the two Franklin Farms units, from the 10-K's 'similar to the cost of each'"],
    ],
), [22, 11, 11, 12, 44]))
A(caption(f"All my estimates unless marked as Entergy's. Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Entergy earnings releases (Form 8-K, Exhibit 99.1) of 12 February, 29 April, 29 July and 2 November 2026, '
  'for adjusted earnings, guidance, sales, the return on construction work in progress, cash, debt, credit metrics, the Evest settlement '
  'with staff and the dividend. Entergy Form 10-Q for the quarter to 30 June 2026 for the capital plan, the second Meta agreement and its '
  'schedule, contract protections, the subpoena and Cottonwood disputes, the equity plan, the power island agreement, customer advances '
  'and shares. Entergy 2025 Form 10-K for the first Meta application, its costs, dates and termination payments, and the January 2026 '
  'motion. Entergy 2026 Investor Day presentation, 9 June 2026, for the outlooks, rate base, equity plan, contract terms, pipeline and '
  'Louisiana allowed return. Entergy Forms 8-K of 23 June and 2 September 2026. Meta 2025 Form 10-K for the lease; GE Vernova call of '
  '28 October 2026 for the 2032 slot. Prices from Yahoo Finance; consensus, targets and peer multiples from stockanalysis.com (S&amp;P '
  'Global data); retrieved 2 November 2026. Estimates for 2026 to 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece, '
  '<a href="https://thephysicallayer.fyi/journal/building-your-own-power/">thephysicallayer.fyi/journal/building-your-own-power</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Entergy. Personal research, not investment advice.</p>')
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
