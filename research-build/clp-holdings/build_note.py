# -*- coding: utf-8 -*-
"""CLP Holdings Limited (HKEX: 0002) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/clp-holdings.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "CLP Holdings Limited (HKEX: 0002)"
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


def hkd(x, d=2):
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(repr(abs(x))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"{'minus ' if x < 0 else ''}HK${q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    if abs(x) < 0.005:
        return "flat"
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def m(x):
    return f"{x:,.0f}"


bear, base, bull = (x["value"] for x in SC)
tgt = CALL["target"]
tp_txt = hkd(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.1f}%" if tgt else f"Base value {hkd(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
view_txt = (f"{CALL['direction'].lower()}, with {conv} conviction" if CALL["direction"] == "NO CALL"
            else f"{CALL['direction'].lower()}, target {hkd(tgt)}, {conv} conviction")
W = ["None", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

A('<h1 class="doctitle">CLP Holdings Limited</h1>')
A('<p class="docsubtitle"><b>HKEX: 0002 | Regulated electricity in Kowloon and the New Territories; Mainland nuclear and renewables; EnergyAustralia; Apraava Energy | Hong Kong</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{hkd(PRICE)} (HKEX close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{hkd(PRICE)}, HKEX close {PRICE_DATE}; highest close of the past year {hkd(HI_CLOSE)} on 21 Aug 2026; up {YTD * 100:.1f}% in 2026"),
    ("Market value", f"HK${MCAP:.1f}bn on {SHARES:,.0f}m shares"),
    ("Net debt, 30 Jun 2026", f"HK${NET_DEBT / 1000:.1f}bn, plus HK${PERPS / 1000:.1f}bn of perpetual securities"),
    ("Dividend", f"HK${DPS25:.2f} for 2025, a {YIELD25 * 100:.2f}% yield; three interims of HK$0.63 declared for 2026"),
    ("P/E", f"{PE_TTM:.1f}x trailing operating earnings; {PE_E27:.1f}x my 2027E; {PE_C27:.1f}x 2027 consensus (HK${CONS_EPS27:.2f})"),
    ("Hong Kong", f"{HK_SHARE25 * 100:.0f}% of 2025 segment operating earnings; permitted return 8% of average net fixed assets, SoC to 2033"),
    ("Data centres", f"6.6% of CLP Power sales, up 12.8% (nine months 2026); {DC_SUBS_DONE} of {DC_SUBS_PLAN} planned substations built"),
    ("Next event", "2026 annual results, usually late February; date not yet announced"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Hong Kong\'s grid is building for its data centres. CLP is paid on the substations, not the kilowatt-hours, and at HK$77.75 the shares already pay for the plan.</p>')
A(para("CLP Power, the regulated core of CLP Holdings, must supply all the electricity Kowloon and the New Territories ask for. "
       "My piece of 2 November argued that Hong Kong's grid builds to its data centres rather than holding them back: CLP had "
       "finished eight data centre substations by June 2026, against 18 planned by 2028, and gives Sandy Ridge the earliest date of anyone."))
A(para(f"For the shares the question is narrower. The Scheme of Control pays 8% a year on the average net fixed assets of the "
       f"Hong Kong business, so data centres matter only as far as they add assets. On my arithmetic each HK$1bn of extra "
       f"assets adds about HK${PER_BN_EPS:.3f} a share a year. A long would need about HK${ANFA_FOR_LONG:.0f}bn more by 2028, "
       f"{ANFA_FOR_LONG / (PLAN_CAPEX / 1000) * 100:.0f}% of the whole five-year plan."))
A(para(f"<b>{my_call}: {view_txt}.</b> A sum of the parts on my 2028 estimates gives {hkd(BASE_VALUE)}, {chg(BASE_VALUE)}, "
       f"inside a range of {hkd(bear)} ({chg(bear)}) to {hkd(bull)} ({chg(bull)}). The yield of {YIELD25 * 100:.1f}% is the return; the AI story is not."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (operating earnings before fair value movements, HK$ million unless stated)"))
A(datatable(
    ["HK$ million", "2024A", "2025A", "2026E*", "2027E*", "2028E*"],
    [
        ["Implied average SoC net fixed assets (HK$bn)", f"{ANFA['2024'] / 1000:.1f}", f"{ANFA['2025'] / 1000:.1f}",
         f"{ANFA_E['2026'] / 1000:.1f}", f"{ANFA_E['2027'] / 1000:.1f}", f"{ANFA_E['2028'] / 1000:.1f}"],
        ["Hong Kong energy and related", m(HK_OPE["2024A"]), m(HK_OPE["2025A"]), m(HK_E["2026"]), m(HK_E["2027"]), m(HK_E["2028"])],
        ["Mainland, Australia, India, Taiwan Region and SE Asia", m(1851 + 591 + 329 + 260), m(1598 + 85 + 221 + 179),
         m(OVS_E["2026"]), m(OVS_E["2027"]), m(OVS_E["2028"])],
        ["Other Hong Kong, unallocated finance and Group costs", m(-58 + 45 - 964), m(OTHER25), m(CORP_E["2026"]), m(CORP_E["2027"]), m(CORP_E["2028"])],
        ["Operating earnings before fair value movements", m(OPE["2024A"]), m(OPE["2025A"]), m(OPE_E["2026"]), m(OPE_E["2027"]), m(OPE_E["2028"])],
        ["Per share (HK$)", f"{EPS_A['2024A']:.2f}", f"{EPS_A['2025A']:.2f}", f"{EPS_E['2026']:.2f}", f"{EPS_E['2027']:.2f}", f"{EPS_E['2028']:.2f}"],
        ["Consensus EPS (HK$, stockanalysis.com)", "", "", f"{CONS_EPS26:.2f}", f"{CONS_EPS27:.2f}", ""],
        [f"P/E at {hkd(PRICE)} (x)", f"{PRICE / EPS_A['2024A']:.1f}", f"{PRICE / EPS_A['2025A']:.1f}", f"{PE_E26:.1f}", f"{PE_E27:.1f}", f"{PE_E28:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5},
))
A(caption("*My estimates. Net fixed assets are derived from the SoC permitted return (8%) in CLP Power's statements; 2026E to 2028E add the "
          "rest of the HK$52.9bn Development Plan evenly and take off depreciation growing 3% a year. Hong Kong earnings = average net fixed "
          f"assets x {R_NET_E * 100:.2f}% net return x {SHARE_NR * 100:.1f}% CLP share + HK${HK_OTHER:.0f}m of other Hong Kong earnings. "
          "Consensus from stockanalysis.com (S&amp;P Global), read 2 November 2026 and last updated 17 September 2026; its 2025 figure matches operating earnings after fair value "
          "movements, so the basis may differ slightly from mine."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: what CLP earns from, and the asset base that drives it"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_segments.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_rab.png"></div></div>')
A(caption("Left: 2025 operating earnings before fair value movements by segment; Hong Kong includes the SoC business, CLPe and related assets. "
          "Source: CLP 2025 annual results, 26 February 2026. Right: average SoC net fixed assets implied by the permitted return, 2023 to 2025, and "
          "my path to 2028; the red box is the extra regulated assets a long would need at an 18x Hong Kong multiple."))
A('</div>')

A(section("The thesis: the landlord is paid on the wiring, not the rent"))
A(para("Think of the landlord from the piece, who must by law wire every flat that gets let. In Hong Kong he is not paid by the "
       "kilowatt-hour his tenants use. He is paid a fixed return on the wiring he has installed. A new tenant with a power-hungry "
       "kitchen helps him only if he has to put in a bigger fuse box to serve it."))
A(para(f"That is the Scheme of Control. CLP Power and Castle Peak Power, 70% owned, must meet demand at the lowest reasonable cost. "
       f"In return the tariff is set to earn a permitted return of 8% a year on their average net fixed assets. In 2025 that was "
       f"HK${PERMITTED['2025']:,.0f}m, which implies average net fixed assets of about HK${ANFA['2025'] / 1000:.1f}bn. The net return "
       f"deducts interest on borrowed capital of up to 7% (HK$1,488m) and a charge on the Tariff Stabilisation Fund (HK$85m), and adds "
       f"performance incentives (HK$526m, about 0.36 points). 65% of the energy efficiency incentives go to the Community Energy Saving "
       f"Fund (HK$242m). That left HK${NET_AFTER_CESF['2025']:,.0f}m, or {R_NET25 * 100:.2f}% of the assets, and CLP's share was "
       f"HK${CLP_SHARE_NR['2025']:,.0f}m."))
A(para("Sales sit outside that formula. If tariff revenue beats the permitted return, the excess goes into a Tariff Stabilisation Fund "
       "that belongs to customers; if it falls short, the fund makes it up, though only up to its balance. So the 12.8% rise in sales to data centres in the first nine "
       "months of 2026 does not lift CLP's profit by itself. It spreads fixed costs over more units and helps hold tariffs down."))
A(para(f"<b>The substations are what count.</b> The 2024 to 2028 Development Plan, approved in November 2023, projects about "
       f"HK$52.9bn of capital spending, 72% of it on transmission and distribution. CLP finished six data centre substations in 2024 and "
       f"2025 and two more of 260 MVA in the first half of 2026, against three in the previous plan, and targets one more this year. "
       f"Each sits in the asset base and earns the return for its working life. Hong Kong earnings rose 7.3% in 2025 and 5.7% in the first "
       f"half of 2026, on higher net fixed assets and lower interest costs."))
A(para(f"CLP does not disclose what the data centre substations cost. As an illustration only, if data centres held the same share of "
       f"the asset base as of sales, 6.6%, they would account for about HK${DC_ANFA_ILLUS:.1f}bn of it and about "
       f"HK${DC_EPS_ILLUS:.2f} of earnings a share, {DC_EPS_ILLUS / EPS_E['2028'] * 100:.0f}% of my 2028 estimate. The data centre is a "
       "real part of the growth, but a small part of the whole."))
A(para("<b>The claim holds on CLP's filings.</b> The eight substations, the 260 MVA, the three in the previous plan, "
       "the mid-2027 target for Sandy Ridge and the 6.6% share of sales all match CLP's announcements. The 18 traces to CLP's 2023 "
       "results, which aimed to supply \"up to 18 large-scale data centres by 2028\", against four in the previous period; CLP's 2025 "
       "results count three, and the piece uses the later count. The claim's tests, 18 substations by the end of 2028 and Sandy Ridge "
       "energised by the end of 2027, are still open."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {hkd(PRICE)} CLP is worth HK${MCAP:.1f}bn. Net debt was HK${NET_DEBT / 1000:.1f}bn at the end of June. The shares trade "
       f"at {PE_TTM:.1f} times operating earnings for the year to June, {PE_E27:.1f} times my 2027 estimate and {PE_C27:.1f} times the "
       f"2027 consensus of HK${CONS_EPS27:.2f}, and yield {YIELD25 * 100:.1f}% on the 2025 dividend. They have risen {YTD * 100:.0f}% this "
       f"year and sit {abs(OFF_HIGH) * 100:.1f}% below the year's highest close."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_eps.png"></div></div>')
A(caption("Left: CLP month-end close, January 2024 to the 2 November 2026 close, against my base value (red). Yahoo Finance history, read "
          "2 November 2026. Right: operating earnings before fair value movements per share, split into Hong Kong and the rest; 2026E to 2028E "
          "mine; red bars are the stockanalysis.com consensus."))
A('</div>')
A(para(f"<strong class='lead'>What the price implies.</strong> If I value the overseas businesses at 10 times earnings and the Group costs at "
       f"16 times, the price pays about {IMPLIED_HK_MULT:.1f} times my 2028 Hong Kong earnings. HK Electric Investments, the island's "
       "regulated utility with a HK$22.0bn plan, trades at 16.3 times forward earnings. The market already pays CLP a premium to its "
       "island neighbour."))
A(para(f"<strong class='lead'>Where I differ: the AI demand is already inside an approved plan.</strong> The data centre buildout is "
       f"real, and my piece rests on it. But it is being built within a HK$52.9bn plan agreed three years ago, so my asset base grows only "
       f"about {ANFA_CAGR * 100:.1f}% a year to 2028. Each HK$1bn of assets above that path is worth about HK${PER_BN_VALUE:.2f} a share at "
       f"18 times. To lift my base value 15% would take about HK${ANFA_FOR_LONG:.0f}bn more by 2028. A story about AI does not change "
       "that arithmetic; only an approved change to the plan does."))
A(para(f"<strong class='lead'>Where the market may be ahead.</strong> The 2027 consensus of HK${CONS_EPS27:.2f} sits "
       f"{CONS_GAP27 * 100:.0f}% above my HK${EPS_E['2027']:.2f}. Some of that may be basis, since the consensus appears to include fair "
       "value movements, and some is a better view of the businesses outside Hong Kong than mine. EnergyAustralia lost about 125,000 "
       "retail accounts in the year to September and its generation margins fell with wholesale prices."))
A(para("<strong class='lead'>Where the real upside sits.</strong> The Scheme allows a development plan review whenever a major system "
       "expansion is proposed. Sandy Ridge, San Tin and the Northern Metropolis could bring one before 2028. The next five-year plan, from "
       "2029, is where data centre demand could move the asset base most, and it lands after my twelve-month horizon."))

A(section("Valuation, with the working"))
A(para(f"I value CLP as a sum of its parts on 2028 earnings, because by late 2027 the market will price 2028 as the year ahead. "
       f"Hong Kong at {M_HK:.0f} times is about two turns above HK Electric Investments, whose results do not mention data centres, for a "
       f"business adding data centre and Northern Metropolis load. The "
       f"overseas businesses at {M_OVS:.0f} times have no clean listed peer: their earnings fell {abs(OVS_DROP25) * 100:.0f}% in 2025, "
       f"EnergyAustralia is losing retail accounts and Mainland nuclear tariffs are falling. At {M_OVS_ALT:.0f} times the base would be "
       f"{hkd(BASE_ALT)}, {(BASE_ALT / PRICE - 1) * 100:.0f}% above the price, still no call. Group costs and other items, minus HK${-CORP_E['2028']:,.0f}m, are capitalised at {M_CORP:.0f} "
       f"times, close to the Group multiple. All three multiples are mine."))
A(cols(datatable(
    ["Part", "2028E earnings, HK$m", "Multiple", "Value, HK$m", "Per share"],
    [
        ["Hong Kong energy and related", m(HK_E["2028"]), f"{M_HK:.0f}x", m(HK_E["2028"] * M_HK), hkd(HK_E["2028"] * M_HK / SHARES)],
        ["Mainland, Australia, India, Taiwan Region and SE Asia", m(OVS_E["2028"]), f"{M_OVS:.0f}x", m(OVS_E["2028"] * M_OVS), hkd(OVS_E["2028"] * M_OVS / SHARES)],
        ["Group costs and other", m(CORP_E["2028"]), f"{M_CORP:.0f}x", m(CORP_E["2028"] * M_CORP), hkd(CORP_E["2028"] * M_CORP / SHARES)],
        ["Base value", m(OPE_E["2028"]), f"{BASE_VALUE / EPS_E['2028']:.1f}x", m(BASE_VALUE * SHARES), hkd(BASE_VALUE)],
    ],
    num_cols={1, 2, 3, 4}, total_row_idx=3,
), [38, 17, 11, 17, 17]))
A(caption(f"Per share on {SHARES:,.0f}m shares. Net debt sits inside the earnings, after interest, so it is not deducted again. The base "
          f"value is {(BASE_VALUE / PRICE - 1) * 100:.1f}% above the price; with about HK$3.2 of dividends over the year the total return "
          "would be about 5 to 6%."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2028 EPS", "HK multiple", "Value", "Change", "Weight"],
    [
        ["Bear", "Rates rise and the net return falls to 6.95%; overseas earnings HK$1.9bn; multiples 15x, 8x and 13x",
         f"HK${SC[0]['eps']:.2f}", f"{SC[0]['mhk']:.0f}x", hkd(bear), chg(bear), "25%"],
        ["Base", "The approved plan, net return 7.25%, overseas HK$2.4bn", f"HK${SC[1]['eps']:.2f}", f"{SC[1]['mhk']:.0f}x", hkd(base), chg(base), "50%"],
        ["Bull", "HK$5bn of assets added to the plan for the Northern Metropolis, net return 7.35%, overseas HK$2.6bn; multiples 20x, 11x and 18x",
         f"HK${SC[2]['eps']:.2f}", f"{SC[2]['mhk']:.0f}x", hkd(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", f"about {hkd(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6}, total_row_idx=3,
), [9, 45, 10, 10, 10, 8, 8]))
A(caption("All three cases are mine. The net return is after interest on borrowed capital, so higher rates lower it; 2025 was 7.11%."))
A('</div>')

A('<div class="keeptogether">')
A(section("Sensitivity: extra regulated assets against the Hong Kong multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Extra 2028 assets"] + [f"{mm:.0f}x" for mm in SENS_MULT],
    [[f"+HK${a:.0f}bn"] + [(f"<b>{hkd(v)}</b>" if (i == 0 and j == 1) else hkd(v)) for j, v in enumerate(row)]
     for i, (a, row) in enumerate(zip(SENS_ANFA, GRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in GRID for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in GRID for v in r)
n_s = sum(v <= PRICE * 0.75 for r in GRID for v in r)
A(para(f"{W[n_above]} of the nine cells sit above the price, but only {W[n_15].lower()} sit 15% or more above it, and each needs "
       f"both extra assets and a multiple of 18 times or more. {W[n_s]} sits 25% or more below. A long needs the base 15% or more above "
       f"the price, a short 25% or more below. At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, {my_call.lower()} is no call, with {conv} conviction."))
A('</div></div>')
A(caption("Overseas earnings at 10x and Group costs at 16x in every cell. Extra assets earn the 7.25% net return at CLP's 90.6% share."))
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "HKEX", "Forward P/E", "Trailing P/E", "Yield", "What they run"],
    [[c, t, f"{p:.1f}x", f"{tp:.1f}x", f"{y * 100:.2f}%", w] for c, t, p, tp, y, w, g in PEERS],
    num_cols={2, 3, 4},
), [19, 7, 10, 10, 8, 46]))
A(caption("stockanalysis.com, 2 November 2026. Power Assets' first half 2026 profit of HK$14.7bn included a gain of about HK$11.3bn on "
          f"the sale of UK Power Networks, completed in May 2026, so its P/E is distorted; CK Infrastructure's multiples carry the same sale, and "
          f"on the 2027 consensus of HK$3.29 it trades at about {CKI_PE27:.0f}x. Excluding those two, the peer median forward P/E is 18.8x. Multiples set the "
          "range only; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["Late February 2027 (not announced)", "2026 annual results", "Hong Kong earnings against HK$9.8bn; substations completed (nine targeted); SoC capex"],
        ["May 2027 (not announced)", "First quarter statement", "Data centre sales growth and share of sales"],
        ["Mid-2027", "Sandy Ridge first phase", "CLP's target for operations in phases; the claim's test is energised by 31 Dec 2027"],
        ["August 2027 (not announced)", "2027 interim results", "Substation count against the 18; any revision to the Development Plan"],
        ["2028", "Next interim review of the Scheme; next Development Plan", "Permitted return and capital spending from 2029"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Interest rates.</strong> The net return deducts interest on borrowed capital of up to 7%. Lower rates helped in 2025 "
       "and 2026; a rise would take some of that back. That is most of the bear case."))
A(para("<strong>Tariff politics.</strong> Fuel costs pass through, but the bill does not look that way to customers. The Average Net "
       "Tariff in October was 4.8% above January's. The Scheme runs to 2033, and the return after that is not fixed."))
A(para("<strong>Outside Hong Kong.</strong> Yangjiang sells more power at market prices on lower tariffs, EnergyAustralia's retail "
       "business is losing accounts, and Yallourn is due to close in 2028."))
A(para("<strong>Data centres stall.</strong> The plan's \"up to 18\" is CLP's own figure. If demand slows, substations slip and the "
       "asset base grows more slowly, though the rest of the plan still runs."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price below about {hkd(LONG_BELOW)}, or Government approval of additions to the plan worth "
       f"about HK${ANFA_FOR_LONG:.0f}bn of regulated assets by 2028. <strong>Into a short:</strong> a price above about "
       f"{hkd(SHORT_ABOVE)}, or a cut to the permitted return."))
A(para(f"<strong>{my_call} is wrong if:</strong> {WRONG_IF}"))
A('</div>')

A(section("Conclusion"))
A(para("My November piece argued that Hong Kong's grid builds to its data centres, and CLP's filings agree: eight substations by June, "
       "18 planned by 2028 and the earliest date for Sandy Ridge. For the shares, the Scheme of "
       "Control turns that buildout into earnings only through the asset base, and the asset base is set by a plan approved in 2023. "
       f"At {IMPLIED_HK_MULT:.1f} times my 2028 Hong Kong earnings the price already pays for it. {my_call}: {view_txt}; base value "
       f"{hkd(BASE_VALUE)}, range {hkd(bear)} to {hkd(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["SoC capital spending, HK$bn", f"{CAPEX_E / 1000:.1f}", f"{CAPEX_E / 1000:.1f}", f"{CAPEX_E / 1000:.1f}", "Rest of the HK$52.9bn plan after SoC capex of HK$10.8bn (2024) and HK$10.6bn (2025), spread evenly"],
        ["SoC depreciation, HK$bn", f"{DEP_E['2026'] / 1000:.1f}", f"{DEP_E['2027'] / 1000:.1f}", f"{DEP_E['2028'] / 1000:.1f}", "2025 HK$5.8bn, growing 3% a year"],
        ["Net return after interest and CESF", f"{R_NET_E * 100:.2f}%", f"{R_NET_E * 100:.2f}%", f"{R_NET_E * 100:.2f}%", "2025: 7.11%; lower interest in 2026"],
        ["Overseas earnings, HK$m", m(OVS_E["2026"]), m(OVS_E["2027"]), m(OVS_E["2028"]), "2025: HK$2,083m; H1 2026: HK$1,298m"],
        ["Group costs and other, HK$m", m(CORP_E["2026"]), m(CORP_E["2027"]), m(CORP_E["2028"]), "2025: minus HK$942m"],
    ],
), [27, 10, 10, 10, 43]))
A(caption(f"All my estimates. Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">CLP Holdings annual results announcement for 2025 and results presentation, 26 February 2026, for segment '
  'earnings, dividends, capital additions, data centre sales and substations, and the HK$52.9bn Development Plan. CLP Holdings interim '
  'results 2026, 6 August 2026, and quarterly statement for January to September 2026, 12 October 2026. CLP Power Hong Kong offering '
  'circular for its US$4.5bn medium term note programme, 1 April 2026, for the Scheme of Control terms, SoC capital expenditure and '
  'the SoC statements for 2023 to 2025. Scheme of Control Agreement with CLP Power and Castle Peak Power, clause 5(2), on the Tariff '
  'Stabilisation Fund. CLP Holdings 2023 annual results, 26 February 2024, for "up to 18 large-scale data centres". LegCo Panel on Environmental '
  'Affairs paper on CLP\'s 2024 to 2028 Development Plan, 28 November 2023, and the Government release of the same date. Share prices '
  'from Yahoo Finance and stockanalysis.com; consensus (last updated 17 September 2026) and peer multiples from stockanalysis.com (S&amp;P Global data); Power Assets interim results 2026 for the UK Power Networks gain; all read '
  '2 November 2026. Estimates for 2026 to 2028 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 2 November 2026, '
  '<a href="https://thephysicallayer.fyi/journal/hong-kong-has-the-plug/">thephysicallayer.fyi/journal/hong-kong-has-the-plug</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in CLP Holdings. Personal research, not investment advice.</p>')
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
