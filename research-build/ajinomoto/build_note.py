# -*- coding: utf-8 -*-
"""Ajinomoto Co., Inc. (Tokyo: 2802) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/ajinomoto.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Ajinomoto Co., Inc. (Tokyo Stock Exchange Prime: 2802)"
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


def yen(x, d=0):
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"¥{q:,.{d}f}"


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


def b1(x):
    return f"{x:,.1f}"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = yen(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {yen(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = ("My draft view" if CALL["draft"] else "My call")
above = sum(v > PRICE for r in VGRID for v in r)
above15 = sum(v >= PRICE * 1.15 for r in VGRID for v in r)
below25 = sum(v <= PRICE * 0.75 for r in VGRID for v in r)
NUMW = {0: "none", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
lean = " leaning short," if CALL["direction"] == "NO CALL" else ""

A('<h1 class="doctitle">Ajinomoto Co., Inc.</h1>')
A('<p class="docsubtitle"><b>Tokyo Stock Exchange Prime: 2802 | Seasonings, frozen foods, amino acids, CDMO, and ABF build-up film for chip packages | Tokyo, Japan | Fiscal year ends 31 March</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"¥{PRICE:,.0f} (Tokyo close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"¥{PRICE:,.0f}, close {PRICE_DATE}; past-year closes ¥{LO_CLOSE:,.0f} to ¥{HI_CLOSE:,.0f}"),
    ("Market value", f"About ¥{MCAP:,.0f}bn on {SHARES:,.1f}m shares; EV ¥{EV_MKT:,.0f}bn"),
    ("Net debt", f"¥{NET_DEBT:,.1f}bn at 30 June 2026, excluding leases"),
    ("Multiples", f"P/E {PE_CONS26:.1f}x FY2026 consensus; EV {EV_BP26_GUIDE:.1f}x guided business profit"),
    ("FY2026 guide (6 Aug)", "Sales ¥1,732.0bn; business profit ¥202.0bn; EPS ¥129.84; film ¥120.6bn sales, ¥65.5bn profit"),
    ("The film's share, FY2025", f"{pc(FM_SALES_SHARE[1])} of sales; {pc(FM_BP_SHARE_SEG[1])} of business profit before shared costs"),
    ("Next results", "Q2 FY2026, 9 November 2026 (third-party calendar; not yet on Ajinomoto's)"),
]))
A('</div><div class="maincol">')
A(f'<p class="lede">Ajinomoto is a food company with a chip film inside. At ¥{PRICE:,.0f}, most of the price is for the film.</p>')
A(para("Ajinomoto sells seasonings, frozen foods and amino acids. It also makes ABF, the insulating film inside the base of almost "
       "every high-performance processor. On 7 October I argued that the film grows with the area of each AI package, and stays with "
       "Ajinomoto at high margins. The results support it: film sales rose 54% and profit 77% in April to June 2026."))
A(para(f"By sales this is a food company: the film was {pc(FM_SALES_SHARE[1])} of fiscal 2025 sales. By profit it is a quarter to a "
       f"third. By value at ¥{PRICE:,.0f} it is mostly film: everything else is worth about {yen(FOOD_FLOOR_PS)} a share on my numbers, "
       f"so the price pays {FM_IMPLIED_X:.0f} times my fiscal 2027 estimate of the film's profit."))
A(para(f"<b>{my_call}: {CALL['direction']},{lean} {CALL['conviction'].lower()} conviction.</b> My sum of the parts, {MULT_FOOD:.0f} times "
       f"for everything else and {MULT_FM:.0f} times for the film on fiscal 2027, gives {yen(BASE_VALUE)}, {chg(BASE_VALUE)}, inside my "
       f"no-call band. The bear case is {yen(bear)} ({chg(bear)}) and the bull {yen(bull)} ({chg(bull)}); on peer medians alone the "
       f"value is {yen(MED_VALUE)} ({chg(MED_VALUE)})."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (IFRS; fiscal years to 31 March)"))
A(datatable(
    ["¥ billion unless stated", "FY2024A", "FY2025A", "Q1 FY26A", "FY2026 guide", "FY2026E*", "FY2027E*"],
    [
        ["Sales", "1,530.6", "1,583.7", "412.1", "1,732.0", b1(Y26['sales']), b1(Y27['sales'])],
        ["Functional Materials sales", "76.5", "100.7", "33.1", "120.6", b1(Y26['fm_sales']), b1(Y27['fm_sales'])],
        ["Functional Materials business profit", "40.2", "54.6", "19.1", "65.5", b1(Y26['fm_bp']), b1(Y27['fm_bp'])],
        ["Film margin", pc(40.2 / 76.5), pc(54.6 / 100.7), pc(19.1 / 33.1), pc(65.5 / 120.6), pc(Y26['fm_margin']), pc(Y27['fm_margin'])],
        ["Food business profit (S&F + Frozen)", "147.1", "151.4", "43.1", "158.0", b1(Y26['food_bp']), b1(Y27['food_bp'])],
        ["Group business profit", "159.3", "181.1", "60.1", "202.0", b1(Y26['bp']), b1(Y27['bp'])],
        ["Film share of profit before shared costs", pc(FM_BP_SHARE_SEG[0]), pc(FM_BP_SHARE_SEG[1]), pc(FM_BP_SHARE_SEG[4]), pc(FM_BP_SHARE_SEG[2]), "", ""],
        ["EPS (¥)", "69.77", "138.36", "38.11", "129.84", f"{Y26['eps']:.2f}", f"{Y27['eps']:.2f}"],
        ["Consensus EPS (¥)", "", "", "", "", f"{CONS_EPS26:.2f}", "n/v"],
        [f"P/E at ¥{PRICE:,.0f} (x)", f"{PRICE / EPS_H[0]:.1f}", f"{PRICE / EPS_H[1]:.1f}", "", f"{PE_GUIDE26:.1f}", f"{PE26:.1f}", f"{PE27:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*My own estimates. FY2026 is the year to March 2027. Consensus: stockanalysis.com (S&P Global), updated 7 August 2026; n/v: "
          "FY2027 consensus not verified. FY2025 EPS includes a ¥41.2bn gain on the sale of fixed assets. History from Ajinomoto's tanshin "
          "and Consolidated Results data sheets; FY2024 business profit restated without shared costs."))

A('<div class="keeptogether">')
A(section("Two charts: small in sales, large in value"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_share.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_sotp.png"></div></div>')
A(caption("Left: Functional Materials as a share of sales, of business profit (*before shared costs) and of enterprise value, at my base "
          f"and at the price. Right: value per share. Everything except the film, less net debt and minorities, is worth about "
          f"{yen(FOOD_FLOOR_PS)}; the rest of the price pays {FM_IMPLIED_X:.1f} times my FY2027 film profit after costs, against my {MULT_FM:.0f} times."))
A('</div>')

A(section("The thesis: the pasta maker inside a grocer"))
A(para("Go back to the lasagne in the piece. Ajinomoto makes the pasta sheets that hold every layer of an AI chip's base apart, and the "
       "dish keeps getting wider and taller. But the shop that makes the sheets is mostly a grocer. Most of what it sells is soup "
       "stock, mayonnaise and frozen dumplings."))
A(para(f"<strong>By sales, a food company.</strong> Seasonings and Foods and Frozen Foods were {pc(FOOD_SALES_SHARE[1])} of fiscal 2025 "
       f"sales of ¥1,583.7bn. Functional Materials, the film business inside Healthcare and Others, sold ¥100.7bn, {pc(FM_SALES_SHARE[1])}. "
       f"<strong>By profit, a quarter to a third.</strong> It earned ¥54.6bn at a 54.2% margin: {pc(FM_BP_SHARE_SEG[1])} of the businesses' "
       f"profit before ¥42.5bn of shared costs, against {pc(FOOD_BP_SHARE_SEG[1])} for food. With a sales-based share of those costs it "
       f"earned ¥{FM_BP_ALLOC_25:.1f}bn, {pc(FM_BP_SHARE_ALLOC_25)} of group business profit. Ajinomoto "
       "Fine-Techno, which makes the film, earned ¥53.0bn of operating profit on ¥98.4bn of sales."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_fm.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_quarters.png"></div></div>')
A(caption("Left: Functional Materials sales and business profit margin by fiscal year, the 6 August guide and my estimates (profit bases "
          "differ slightly before FY2024). Right: by quarter, Q1 FY2025 to Q1 FY2026. Source: Ajinomoto Consolidated Results data sheets."))
A('</div>')
A(para("<strong>The claim is holding.</strong> In April to June 2026 film sales rose 54% and profit 77%, a 57.7% margin. Ajinomoto said "
       "ABF sales \"continue to be strong\" for AI, server and network boards and its \"product mix is also improving\", and raised its "
       "guide by ¥9.0bn of sales and ¥5.0bn of profit, all in this business. Servers and networks stayed at 70% of film volume in fiscal "
       "2025, the piece's floor, as read from the chart on slide 25 of the 7 May 2026 presentation (rounded to five points). "
       "<strong>It is not a straight line:</strong> in fiscal 2023 film sales fell 13% and profit 25%, to a 45% margin, as substrate "
       "makers cut stock."))
A(para("<strong>Where I was wrong in October.</strong> My piece said: \"Ajinomoto discloses that margin only as rounded wording, "
       "'over 50%'.\" The claim's test says the same. That was wrong. The Consolidated Results data sheets print Functional Materials "
       "sales and business profit in yen every quarter (¥100.7bn and ¥54.6bn for FY2025; ¥33.1bn and ¥19.1bn for Q1 FY2026), so the "
       "margin can be computed exactly: 54.2% and 57.7%. What showed me the slip was building this model from those sheets. It "
       "strengthens the test: the margin half no longer depends on wording Ajinomoto might stop printing. The piece and claim stay as "
       "published; I found nothing else wrong."))
A(para("<strong>Price is the open question.</strong> On 31 March 2026 Palliser Capital, an activist among the top 25 shareholders, asked "
       "for a film price rise of more than 30% and for Functional Materials to become a reportable segment. In May DigiTimes reported that Taiwanese substrate makers had "
       "notice of a 30% rise from the third quarter of 2026. Ajinomoto's own documents do not mention it, so I treat it as not verified."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"<strong class='lead'>The price.</strong> At ¥{PRICE:,.0f} on {SHARES:,.1f}m shares, my arithmetic after buybacks to 30 September, "
       f"the market value is ¥{MCAP:,.0f}bn and the enterprise value ¥{EV_MKT:,.0f}bn, {EV_BP26_GUIDE:.1f} times guided business profit. "
       f"The obvious objection to valuing it as one company is that the parts are so different. So I split it. I spread shared costs and "
       f"about ¥18bn a year of other operating expense by sales, so the film carries {pc(Y27['fm_share'])} of them: Fine-Techno's own "
       "accounts already carry most of its overheads."))
A(para(f"<strong class='lead'>What the price implies.</strong> Everything except the film earns ¥{Y27['nonfm_net']:.1f}bn after costs in "
       f"fiscal 2027 on my numbers. At {MULT_FOOD:.0f} times, less net debt and minorities, it is worth {yen(FOOD_FLOOR_PS)} a share, "
       f"{pc(FOOD_FLOOR_SHARE, 0)} of the price. The other ¥{FM_IMPLIED_EV:,.0f}bn of enterprise value prices the film at "
       f"{FM_IMPLIED_X:.1f} times my ¥{Y27['fm_net']:.1f}bn of film profit after costs, {pc(FM_SHARE_EV_MKT, 0)} of the enterprise value. "
       f"So a call on these shares is, by sales, a call on a food company, but the price is mostly about the film. Every 10% on the "
       f"film's implied value moves the shares about {yen(FM_10PCT_MKT_PS)}, {pc(FM_10PCT_MKT_PS / PRICE)}."))
A(para(f"<strong class='lead'>Where I differ.</strong> At {MULT_FM:.0f} times the price needs about ¥{FM_IMPLIED_NET_AT_BASE_X:.0f}bn of film "
       f"profit after costs, about ¥{NEED_FM_BP:.0f}bn of Functional Materials business profit, more than twice fiscal 2025's ¥54.6bn. "
       f"My base is ¥{Y27['fm_bp']:.1f}bn on sales of ¥{Y27['fm_sales']:.0f}bn. The price's number needs the reported 30% rise to hold "
       "in full, and volume to keep growing from plants that add capacity slowly until Kani City opens in fiscal 2032. That is my bull "
       "case, not my base."))

A(section("Valuation, with the working"))
A(para(f"<strong>FY2026E</strong>: Ajinomoto's guide except the film, where I take ¥{Y26['fm_sales']:.0f}bn at {pc(Y26['fm_margin'], 0)} "
       "(guide ¥120.6bn at 54.3%; it implies only 10% growth for the last three quarters after 54% in the first). Business profit "
       f"¥{Y26['bp']:.1f}bn, EPS ¥{Y26['eps']:.1f}, {abs(Y26['eps'] / CONS_EPS26 - 1) * 100:.1f}% below consensus. <strong>FY2027E</strong>: "
       f"film sales +{(Y27['fm_sales'] / Y26['fm_sales'] - 1) * 100:.0f}% to ¥{Y27['fm_sales']:.0f}bn at {pc(Y27['fm_margin'], 0)}, "
       f"food profit +{FOOD_G27 * 100:.0f}%, Bio-Pharma ¥{BIO_BP[1]:.0f}bn: business profit ¥{Y27['bp']:.1f}bn, EPS ¥{Y27['eps']:.1f}."))
A(para(f"<strong>The multiples.</strong> {MULT_FOOD:.0f} times for everything except the film, between Nestle ({PEER_EVEBIT['Nestle']:.1f}x) "
       f"and Kikkoman ({PEER_EVEBIT['Kikkoman']:.1f}x), the closest peer. Ajinomoto's own year-end P/E from FY2016 to FY2021 ran "
       f"{PE_HIST_RANGE[0]:.1f} to {PE_HIST_RANGE[1]:.1f} times, the top inflated by impairments in FY2018 and FY2019; as P/E figures they "
       f"support an EV multiple only roughly. {MULT_FM:.0f} times for the film, a premium to the {ELEC_MED:.1f} times median of "
       f"electronic materials peers, which rests on three names and so equals Resonac, for a margin above 50% and a share Ajinomoto puts above 95%."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "Film sales FY27", "Film margin", "Multiples", "Film share of EV", "Value", "Change", "Weight"],
    [
        ["Bear", "A pause like FY2023; food flat", f"¥{SCEN[0][1]:.0f}bn", pc(SCEN[0][2], 0), f"{SCEN[0][5]:.0f}x, {SCEN[0][6]:.0f}x", pc(SV[0]['v']['ev_fm'] / SV[0]['v']['ev'], 0), yen(bear), chg(bear), "25%"],
        ["Base", "Volume and mix, some price", f"¥{SCEN[1][1]:.0f}bn", pc(SCEN[1][2], 0), f"{SCEN[1][5]:.0f}x, {SCEN[1][6]:.0f}x", pc(SV[1]['v']['ev_fm'] / SV[1]['v']['ev'], 0), yen(base), chg(base), "50%"],
        ["Bull", "The 30% price rise holds", f"¥{SCEN[2][1]:.0f}bn", pc(SCEN[2][2], 0), f"{SCEN[2][5]:.0f}x, {SCEN[2][6]:.0f}x", pc(SV[2]['v']['ev_fm'] / SV[2]['v']['ev'], 0), yen(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", "", yen(WEIGHTED), chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7, 8}, total_row_idx=3,
), [9, 25, 10, 8, 10, 10, 9, 10, 9]))
A(caption(f"Multiples are EV over business profit after costs: everything except the film, then the film. On the peer medians, "
          f"{FOOD_MED:.1f}x and {ELEC_MED:.1f}x, the value is {yen(MED_VALUE)} ({chg(MED_VALUE)}), past the short line. The band: long when "
          "my base value is at least 15% above the price, short when it is at least 25% below, no call in between."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: FY2027E film sales (56% margin) against the film multiple"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Film sales FY2027E"] + [f"{x:.0f}x" for x in SENS_X],
    [[f"¥{s:.0f}bn"] + [(f"<b>{yen(v)}</b>" if (i == 1 and j == 1) else yen(v)) for j, v in enumerate(r)]
     for i, (s, r) in enumerate(zip(SENS_S, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{NUMW[above].capitalize()} of the nine cells sits above the price, and {NUMW[above15]} by 15% or more; it needs both "
       f"¥{SENS_S[2]:.0f}bn of film sales and {SENS_X[2]:.0f} times. {NUMW[below25].capitalize()} cells sit 25% or more below, all at "
       f"{SENS_X[0]:.0f} times. One turn of the film multiple is worth {yen(FM_TURN_PS)} a share, one turn on everything else "
       f"{yen(FOOD_TURN_PS)}. Every figure is live in the model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
peer_rows = []
for p in PEERS + REF_PEERS:
    pe = PEER_PE[p[0]]
    peer_rows.append([p[0], p[1], {"food": "Food", "elec": "Electronic materials", "ref": "Reference"}[p[2]], p[7],
                      f"{PEER_EVEBIT[p[0]]:.1f}x", f"{pe:.1f}x" if pe else "n/m", p[8]])
peer_rows.append(["Ajinomoto", "Tokyo: 2802", "Subject", "Mar 2027", f"{EV_OP_CONS:.1f}x", f"{PE_CONS26:.1f}x", "Seasonings, frozen foods, amino acids, CDMO, ABF film"])
A(cols(datatable(["Company", "Listing", "Group", "Year end", "EV / op. income", "P/E", "What they make"], peer_rows, num_cols={4, 5}),
       [15, 12, 13, 9, 10, 7, 34]))
A(caption("stockanalysis.com (S&P Global consensus) for the fiscal year ending December 2026 or March 2027, retrieved 7 October 2026; "
          f"year ends differ by up to three months. Medians: food {FOOD_MED:.1f}x, electronic materials {ELEC_MED:.1f}x; Sekisui Chemical, a "
          "rival film maker inside a broad group, is shown for reference only. JSR was delisted in June 2024. Entegris P/E on adjusted "
          "EPS (US$3.93; 61.1x on reported); Kraft Heinz consensus is on reported figures. Multiples only; no view on the peers' shares."))
A('</div>')

A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_valuation.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: value per share from the scenarios, the sensitivity grid, the peer medians, the weighted case and my base, against the "
          f"price (red) and the average analyst target of ¥{CONS_TP:,.0f}. Right: month-end close, split-adjusted, October 2023 to "
          "7 October 2026 (stockanalysis.com, retrieved 7 October 2026), against my base value."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["9 November 2026 (third-party; not yet on Ajinomoto's calendar)", "Q2 FY2026 results", "Film growth after Q1's 54%; any sign of the price rise in the margin"],
        ["26 November 2026 (planned)", "Board vote on merging Fine-Techno", "Effective 1 April 2027; the subsidiary's own accounts stop"],
        ["30 November 2026", "End of the ¥80bn buyback", "Whether a new programme follows"],
        ["May 2027", "FY2026 results and FY2027 guide", "Film volume by application; film margin; the FY2027 film guide"],
        ["Any time", "Rival films; Palliser", "Sekisui or LG Chem qualified in AI substrates; a reportable film segment"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para(f"<strong>Against the lean, on the upside.</strong> If the 30% rise holds and volume keeps growing, fiscal 2027 film profit could "
       f"pass my bull case; the average analyst target is ¥{CONS_TP:,.0f}. A reportable film segment, as Palliser asks, could make the film easier "
       "to value on its own. <strong>The film's own cycle.</strong> Fiscal 2023 showed it can fall a quarter in a year; a pause in AI "
       "servers hits it first, and the multiple with it. <strong>A rival qualified.</strong> A large price rise makes a second source, "
       "Sekisui Chemical or LG Chem, more worth the long qualification. <strong>Food.</strong> Frozen Foods earned ¥8.4bn in fiscal 2025, "
       "down from ¥13.0bn, and raw material and Middle East costs weigh on food. The shares fell 16% on 7 November 2025 when the first "
       "half came in flat."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price at or below about {yen(REVISIT_LONG)} with my numbers unchanged, or results that lift my "
       f"FY2027 film business profit to about ¥{FM_BP_LONG:.0f}bn or more. <strong>Into a short:</strong> a price at or above about "
       f"{yen(REVISIT_SHORT)}, or FY2027 film profit at or below about ¥{FM_BP_SHORT:.0f}bn."))
A(para("<strong>The view is wrong if</strong>, by October 2027, Ajinomoto reports FY2026 Functional Materials business profit below "
       "fiscal 2025's ¥54.6bn, a fall like fiscal 2023's, which points to my bear case; or its May 2027 forecast puts FY2027 Functional "
       "Materials business profit at ¥105bn or more, which points to my bull case."))
A('</div>')

A(section("Conclusion"))
A(para("My piece argued that Ajinomoto's film grows with the package and stays with Ajinomoto at high margins. The results support it: "
       "54% growth in the latest quarter at a 57.7% margin, and a guide raised on the film alone. By sales Ajinomoto is a food company; "
       f"by value at ¥{PRICE:,.0f} it is mostly a film company, priced at about {FM_IMPLIED_X:.0f} times my FY2027 film profit. "
       f"{my_call}: {CALL['direction']},{lean} {CALL['conviction'].lower()} conviction. Base value {yen(BASE_VALUE)}, {chg(BASE_VALUE)}, "
       f"range {yen(bear)} to {yen(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY2026E", "FY2027E", "Basis"],
    [
        ["Functional Materials sales, ¥bn", f"{FM_SALES[0]:.0f}", f"{FM_SALES[1]:.0f}", "Guide 120.6; Q1 33.1 (+54%)"],
        ["Functional Materials margin", pc(FM_MARGIN[0], 0), pc(FM_MARGIN[1], 0), "FY2025 54.2%; Q1 FY2026 57.7%"],
        ["Food business profit, ¥bn", f"{Y26['food_bp']:.1f}", f"{Y27['food_bp']:.1f}", "Guide for FY2026; +4% in FY2027"],
        ["Bio-Pharma business profit, ¥bn", f"{BIO_BP[0]:.0f}", f"{BIO_BP[1]:.0f}", "Guide 17.0 for FY2026"],
        ["Shared costs and other expense, ¥bn", f"{SHARED[0] + OTHER_OPEX[0]:.1f}", f"{SHARED[1] + OTHER_OPEX[1]:.1f}", "Guide: shared -46.2; OP less BP -17.8; spread by sales"],
        ["Tax rate; minorities' profit, ¥bn", f"26%; {NCI_PROFIT[0]:.1f}", f"26%; {NCI_PROFIT[1]:.1f}", "Guide 25.9% and 10.0"],
        ["Net debt; minorities (book), ¥bn", f"{NET_DEBT:.1f}; {NCI:.1f}", "held flat", "30 June 2026; dividends and buybacks absorb free cash flow"],
    ],
), [30, 13, 13, 44]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Ajinomoto Consolidated Financial Results (tanshin) for FY2025, 7 May 2026, and Q1 FY2026, 6 August 2026. '
  'Ajinomoto Consolidated Results data sheets of 11 May 2023, 9 May 2024, 8 May 2025, 6 November 2025, 5 February 2026, 7 May 2026 and '
  '6 August 2026. FY2026 Revised Forecast by Segment and Notice of Revision to Full-Year Forecast, 6 August 2026. Results presentation '
  'with script, 7 May 2026; Q1 FY2026 presentation, 6 August 2026; ASV Report 2026. Buyback notices of 2 July and 2 October 2026. '
  'Palliser Capital plan, 31 March 2026, as reported; DigiTimes, 13 May 2026. Share prices, consensus, the average target and peer '
  'figures from stockanalysis.com (S&P Global), retrieved 7 October 2026. Estimates for FY2026 and FY2027, the cost allocation and the '
  'valuation are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 7 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/ajinomoto-grows-with-the-package/">thephysicallayer.fyi/journal/ajinomoto-grows-with-the-package</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Ajinomoto. Personal research, not investment advice.</p>')
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
