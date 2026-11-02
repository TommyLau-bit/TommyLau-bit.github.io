# -*- coding: utf-8 -*-
"""Samsung Electronics Co., Ltd. (KRX: 005930) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/samsung-electronics.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Samsung Electronics Co., Ltd. (KRX: 005930)"
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


def krw(x, r=100):
    from decimal import Decimal, ROUND_HALF_UP
    q = int(Decimal(repr(x / r)).quantize(Decimal(1), rounding=ROUND_HALF_UP)) * r
    return f"KRW {q:,.0f}"


def num(x, r=100):
    return krw(x, r)[4:]


def chg(v, p=PRICE):
    x = v / p - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


def pc(x, d=1):
    return f"{x * 100:.{d}f}%"


bear, base, bull = VALS
sb, sm, su = SV
tgt = CALL["target"]
tp_txt = krw(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {krw(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = ("My draft view" if CALL["draft"] else "My call")
above = sum(v > PRICE for r in VGRID for v in r)
ps = lambda v: v / SH * 1e6
ds_share_9m = sum(Q_DS_OP[4:]) / sum(Q_OP[4:])

A('<h1 class="doctitle">Samsung Electronics Co., Ltd.</h1>')
A('<p class="docsubtitle"><b>KRX: 005930 (preferred 005935) | Memory, foundry, phones, TVs, displays, Harman | Suwon, Korea</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"KRW {PRICE:,.0f} (common, KRX close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"Common KRW {PRICE:,.0f}, preferred KRW {PRICE_P:,.0f} ({pc(PREF_GAP)} below), KRX closes {PRICE_DATE}; common 52-week range KRW {LO52[0]:,.0f} to {HI52[0]:,.0f} (intraday)"),
    ("Market value", f"About KRW {MCAP:,.0f}tn on {SH_C:,.0f}m common and {SH_P:,.0f}m preferred shares; US${MCAP / FX * 1000:,.0f}bn at KRW {FX:,.2f} per US$"),
    ("Net cash, 30 Sep 2026", f"KRW {NET_CASH:.1f}tn; about KRW {NC_NOW:.0f}tn after the declared Q3 dividend and October buybacks"),
    ("P/E (common)", f"{PE26:.1f}x my 2026; {PEC27:.1f}x 2027 consensus; {PE27:.1f}x my 2027"),
    ("Consensus (stockanalysis.com)", f"EPS KRW {CONS_EPS_26:,.0f} 2026, about KRW {CONS_EPS_27:,.0f} 2027; average target KRW {CONS_TP:,.0f}"),
    ("Q3 2026 (29 Oct)", "Revenue KRW 195.3tn; operating profit KRW 107.4tn, of which chips KRW 106.5tn; memory sales KRW 140.7tn"),
    ("HBM", f"Not disclosed; my estimate about {pc(HBM_REV[1] / MEM26, 0)} of 2026 memory sales. 2027 supply sold out (call)"),
    ("Next results", "Q4 2026, expected late January 2027 with preliminary figures in early January (not yet confirmed)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Samsung Electronics is a memory company with a phone maker attached, and its price assumes the memory cash never leaves the group.</p>')
A(para(f"Samsung makes memory, phones, TVs, displays and chips for others, but its chip division earned {pc(ds_share_9m, 0)} of operating "
       "profit in the first nine months of 2026, almost all of it from memory. HBM, the memory stacked beside AI chips, is about "
       f"{pc(HBM_REV[1] / MEM26, 0)} of 2026 memory sales on my estimates. Samsung's real AI difference is the base die: it is the only "
       "HBM maker that builds that logic chip in its own foundry."))
A(para(f"At KRW {PRICE:,.0f} the common shares trade at {PEC27:.1f} times 2027 consensus. On my sum of the parts the market value needs "
       f"normal memory earnings worth only a {pc(NEED_0[1])} net margin before any discount, and {pc(NEED_D[1])} after my {pc(DISC, 0)} "
       f"conglomerate discount, against my base of {pc(NM, 0)}. If the cash also stays in the group and earns nothing, it needs {pc(NEED_D0[1])}."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {tp_txt}.</b> My base value is "
       f"{krw(BASE_VALUE)}, {chg(BASE_VALUE)}. The bear case is {krw(bear)} ({chg(bear)}) and the bull case {krw(bull)} ({chg(bull)}). "
       f"The preferred shares carry the same dividend at a {pc(PREF_GAP)} discount."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (KRW trillion unless stated; calendar years)"))
A(datatable(
    ["KRW trillion unless stated", "2024A", "2025A", "2026E*", "2027E*", "2028E*", "Normal*"],
    [
        ["Revenue", f"{REV[-2]:.1f}", f"{REV[-1]:.1f}", f"{REV26:.1f}", f"{REV27:.1f}", f"{REV28:.1f}", ""],
        ["  Memory sales", f"{MEM_REV_H['2024']:.1f}", f"{MEM_REV_H['2025']:.1f}", f"{MEM26:.1f}", f"{MEM27:.1f}", f"{BASE_Y['m28']:.1f}", f"{normal_mem():.1f}"],
        ["  HBM (my estimate)", "", f"{HBM_REV[0]:.1f}", f"{HBM_REV[1]:.1f}", f"{HBM_REV[2]:.1f}", "", ""],
        ["Operating profit", f"{OP[-2]:.1f}", f"{OP[-1]:.1f}", f"{OP26:.1f}", f"{OP27:.1f}", f"{OP28:.1f}", ""],
        ["  of which chips (DS)", f"{DS_OP[-2]:.1f}", f"{DS_OP[-1]:.1f}", f"{DS_OP26:.1f}", f"{MEM27 * MEM_OPM27 + OTH27['nonmem'][1]:.1f}", f"{BASE_Y['m28'] * MEM_OPM28 + OTH28['nonmem'][1]:.1f}", ""],
        ["Operating margin (%)", pc(OP[-2] / REV[-2]), pc(OP[-1] / REV[-1]), pc(OP26 / REV26), pc(OP27 / REV27), pc(OP28 / REV28), ""],
        ["Memory net margin (%)", "", "", "", pc(BASE_Y['mni27'] / MEM27), pc(BASE_Y['mni28'] / BASE_Y['m28']), pc(NM)],
        ["EPS (KRW)", f"{EPS_H[-2]:,}", f"{EPS_H[-1]:,}", f"{EPS26:,.0f}", f"{EPS27:,.0f}", f"{EPS28:,.0f}", ""],
        ["Consensus EPS (KRW)", "", "", f"{CONS_EPS_26:,.0f}", f"{CONS_EPS_27:,.0f}", "", ""],
        [f"P/E at KRW {PRICE:,.0f} (x)", f"{PRICE / EPS_H[-2]:.1f}", f"{PE25:.1f}", f"{PE26:.1f}", f"{PE27:.1f}", f"{PE28:.1f}", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E is reported profit for the first nine months plus my fourth quarter; 2027E, 2028E and the normal year are my own "
          f"estimates on operations only, taxed at {pc(TAX, 0)}. EPS for my periods is on {SH:,.0f}m economic shares (common and preferred, "
          "which earn near-identical EPS). HBM revenue is not disclosed; the HBM line is mine. History from Samsung's earnings call decks; "
          "consensus from stockanalysis.com (S&P Global), retrieved 2 November 2026."))

A('<div class="keeptogether">')
A(section("Two charts: the chips are the company, and the phones pay for the memory"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_profit.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_squeeze.png"></div></div>')
A(caption("Left: operating profit by quarter, Device Solutions against the rest of the group, from Samsung's earnings call decks; Q4 2026 "
          "is my estimate. Right: MX and Networks operating profit against memory sales; the phone division lost money in the second and "
          "third quarters of 2026, which Samsung put down to component and cost pressures."))
A('</div>')

A(section("The thesis: paid twice for the shortage, charged once"))
A(para("Go back to the kitchen from the October piece. The chef is the AI chip and the hatch is the memory feeding it. Samsung stocks "
       "the pantry, builds hatches, and also runs a restaurant chain that buys its own flour. This year flour became the scarce part: the "
       "pantry earns a fortune, the restaurants pay more for every loaf, and the hatch, sold a year ahead, is a small line in the books."))
A(para(f"<strong>The pantry is the company.</strong> Third quarter revenue was KRW {Q_REV[-1]:.1f}tn, up 127% on a year earlier, and operating "
       f"profit KRW {Q_OP[-1]:.1f}tn, a 55% margin. Memory sales were KRW {Q_MEM[-1]:.1f}tn, and the chip division earned KRW {Q_DS_OP[-1]:.1f}tn. "
       "DRAM bits rose by a low to mid single digit percentage on the quarter and DRAM prices by about 20%; NAND prices rose by a high "
       "teens percentage. Samsung guides fourth quarter DRAM bits up by a mid to high teens percentage."))
A(para("<strong>The restaurants pay for the flour.</strong> MX and Networks lost KRW 0.6tn in the third quarter on KRW 37.7tn of sales, "
       "its second loss in a row, and Samsung expects high raw material prices to persist into 2027. Against a year earlier the consumer "
       "businesses lost about KRW 4tn of quarterly profit while the chip division gained about KRW 100tn. The hedge is small."))
A(para(f"<strong>HBM is a small slice.</strong> Samsung said in February that HBM sales would more than triple in 2026; HBM4 sales rose more "
       "than threefold on the quarter in the third quarter, to 60% of HBM sales, and its 2027 HBM supply is already sold out, at prices "
       "agreed with customers. It began volume HBM4 sales for Nvidia's Vera Rubin in the first quarter. On my estimate HBM was about "
       f"KRW {HBM_REV[0]:.1f}tn in 2025 and KRW {HBM_REV[1]:.0f}tn in 2026, {pc(HBM_REV[1] / MEM26, 0)} of memory sales."))
A(para(f"<strong>My notes do not fully agree.</strong> IDC, as quoted in SK Hynix's US prospectus, put HBM shares in 2025 at "
       "63.2% for SK Hynix, 19.3% for Samsung and 17.4% for Micron, and in the first quarter of 2026 at 56.4%, 20.5% and 23.1%. "
       f"From IDC's 2025 share, Samsung's tripling implies about {pc(HBM_SHARE_26, 0)} of a US$49bn market in 2026, the path in my Micron "
       "note. My SK Hynix note gives SK Hynix 55% of that 2026 market and my Micron note implies about a fifth for Micron, which sum to "
       "more than the whole. Samsung also says its third quarter 2026 HBM share matched its DRAM share. Either the 2026 market is larger "
       "than US$49bn, or SK Hynix's share falls faster than my SK Hynix note assumes. No maker discloses HBM revenue; on any of these, HBM "
       "is a small part of Samsung's money."))
A(para("<strong>The base die is Samsung's real difference.</strong> Samsung builds its HBM4 base die on a 4 nanometre process in its own "
       "foundry, which credited improving results to base die demand in the second quarter and base die sales growth in the third. SK Hynix said in April 2024 it would "
       "use TSMC's logic process for HBM4's base die. Micron makes its HBM4 base die in house, but said on 23 September 2025 that it is partnering "
       "with TSMC to make its HBM4E base die. From HBM4E, Samsung is the only one of the three that keeps the whole stack under one roof."))
A(para("<strong>Where I was wrong in October.</strong> My piece listed among the facts it did not use that \"Micron's HBM4E base die partner "
       "is likewise press only\". That was wrong. In Micron's prepared remarks for its call of 23 September 2025, Sanjay Mehrotra said: "
       "\"We are partnering with TSMC for manufacturing the HBM4E base logic die\", for standard and custom products alike. It "
       "strengthens the piece's point that the base die moves to logic foundries, and sharpens Samsung's difference."))
A(para("<strong>Custom HBM cuts both ways.</strong> While the maker designs the base die, one roof is an edge. When the buyer designs it, as "
       "Nvidia's NVHBM does, the buyer has a say in where it is made, and Nvidia's chips are made at TSMC; that is my reading, not anything "
       "Samsung or Nvidia has said. Samsung said in February that \"custom HBM samples will start reaching customers in 2027\", and plans "
       "HBM4E mass production in the first half of 2027. So Samsung is unlikely to report custom HBM in volume by the end of 2027, and the "
       "piece's claim now rests mainly on SK Hynix and Micron."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At KRW {PRICE:,.0f} for the common and KRW {PRICE_P:,.0f} for the preferred, Samsung is worth about KRW {MCAP:,.0f}tn. I count "
       f"about {SH_C:,.0f}m common shares ({SH_C_ISSUED:,.1f}m issued at 30 June, from the half-year report, less {TREAS_C:.1f}m in "
       f"treasury, from the buyback report of 12 October) and {SH_P:,.0f}m preferred, none in treasury. The common trades at {PEC27:.1f} times 2027 consensus, against "
       f"{PEER_PE[0][1]:.1f} times for SK Hynix and {PEER_PE[1][1]:.1f} times for Micron's fiscal 2027, and is {abs(OFF_HIGH) * 100:.0f}% "
       f"below its June high. As in my other memory notes, peak earnings are not a stream to capitalise: the chip division lost KRW 14.9tn "
       f"in 2023 and earned a {pc(DS_CYC_M)} operating margin over 2017 to 2025."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_cycle.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: Device Solutions sales and operating margin, 2017 to 2025 from Samsung's fourth quarter decks (restated for chips only), "
          "2026 and 2027 my estimates. Right: month-end closes of the common and preferred shares, September 2023 to 2 November 2026 "
          "(KRX closes via Naver Finance to August 2026 and stockanalysis.com since), against my base value."))
A('</div>')
A(para(f"<strong class='lead'>What the price needs.</strong> Memory is valued with the method and normal cases of my Micron and SK Hynix "
       f"notes: net cash at September 2027, plus memory earnings above normal still to come, plus {MULT} times normal memory earnings. The "
       f"other businesses are added at modest multiples, and I take {pc(DISC, 0)} off the whole. I expect net cash of about KRW {NC_SEP27:.0f}tn "
       f"by September 2027, {krw(NC_PS)} a share, before distributions. With no discount the market value needs normal memory earnings of "
       f"only KRW {NEED_0[0]:.0f}tn after tax, a {pc(NEED_0[1])} net margin on my normal memory sales. With my discount it needs "
       f"{pc(NEED_D[1])}; with the discount and the cash spent for nothing, {pc(NEED_D0[1])}, close to my base."))
A(para("<strong class='lead'>Where I differ.</strong> The discount is earned, but the market charges it twice. Samsung's 2026 plan returns "
       "a third to two fifths of my 2026 free cash flow, where SK Hynix has committed to at least half, and the Lee family controls Samsung "
       "through Samsung C&amp;T and Samsung Life Insurance with a small direct stake. That justifies a discount, which I take. But Samsung "
       f"now plans KRW {RETURN_26[0]:.0f} to {RETURN_26[1]:.0f}tn of 2026 returns, KRW 55 to 75tn still to come, including \"a substantial "
       "share repurchase and cancellation program\", set at a board meeting in late January 2027."))
A(para(f"<strong class='lead'>The preferred shares.</strong> Each preferred share received the same KRW {DPS_Q3:,} third quarter dividend "
       f"and earned near the same EPS (KRW 11,492 against 11,462), but trades {pc(PREF_GAP)} below the common, against "
       f"{pc(PREF_GAP_HIST[1][1])} at the end of 2024. Samsung says it will consider \"adjusting the proportion of preferred shares\" in its "
       f"buybacks. My value per share applies to both classes; the preferred lacks only the vote, and sits {chg(VALUE_P, PRICE_P)} from it."))

A(section("Valuation, with the working"))
A(para(f"I value operations, because reported profit swings with finance items: a KRW {abs(Q3_FIN)}tn finance loss in the third quarter, "
       f"and about KRW {Q3_FX_OP:.0f}tn of operating profit lost to the stronger won. 2026 adds a fourth quarter of KRW {Q4['mem']:.0f}tn of "
       f"memory sales at a {pc(Q4['ds_opm'], 0)} chip margin: revenue KRW {REV26:.1f}tn (consensus {CONS_REV_26}), EPS {krw(EPS26)}, "
       f"{abs(EPS26 / CONS_EPS_26 - 1) * 100:.1f}% below consensus. 2027 memory sales are KRW {MEM27:.0f}tn at {pc(MEM_OPM27, 0)}: revenue "
       f"KRW {REV27:.0f}tn, {abs(REV27 / CONS_REV_27 - 1) * 100:.1f}% below consensus, EPS {krw(EPS27)}, {abs(EPS27 / CONS_EPS_27 - 1) * 100:.1f}% "
       f"below. 2028 memory sales fall {abs(G28) * 100:.0f}% at {pc(MEM_OPM28, 0)}. Free cash flow is about KRW {FCF_Q4:.0f}tn in the fourth "
       f"quarter and KRW {FCF27:.0f}tn in 2027 after KRW {CAPEX27:.0f}tn of capital spending (2026 plan KRW {CAPEX_26}tn, {CAPEX_DS_26}tn for chips). "
       f"Normal memory sales take the four quarters to June 2026, KRW {BASE_MEM:.1f}tn, grow bits 20% a year for four years at 55% of the "
       f"price per bit: KRW {normal_mem():.1f}tn, at {pc(NM, 0)} net, KRW {N_BASE:.1f}tn."))

A('<div class="keeptogether">')
A(section("Sum of the parts at October 2027"))
A('<div class="chartsrow"><div class="col left">')
A(cols(datatable(
    ["Part", "Basis (my estimates)", "KRW tn", "Per share"],
    [
        ["Net cash, Sep 2027", "Sep 2026 less Q3 dividend and Oct buybacks, plus FCF", f"{BASE['nc']:.0f}", num(ps(BASE['nc']))],
        ["Memory above normal", "1/4 of 2027 excess, 2028, half of 2028 again; 10%", f"{BASE['exc']:.0f}", num(ps(BASE['exc']))],
        ["Memory, normal", f"{MULT}x KRW {N_BASE:.1f}tn", f"{BASE['term']:.0f}", num(ps(BASE['term']))],
        ["Phones (MX, Networks)", "10x after-tax on KRW 12tn", f"{OTH_VAL[1]:.0f}", num(ps(OTH_VAL[1]))],
        ["Display, TVs and appliances, Harman", "8x, 8x, 12x after tax", f"{sum(OTH_VAL[2:]):.0f}", num(ps(sum(OTH_VAL[2:])))],
        ["Foundry and System LSI", f"{FOUNDRY_X}x 2026 sales", f"{OTH_VAL[0]:.0f}", num(ps(OTH_VAL[0]))],
        ["Investments", f"KRW {INVEST}tn book at {pc(1 - INV_HAIRCUT, 0)}", f"{INV_VAL:.0f}", num(ps(INV_VAL))],
        ["Gross", "", f"{BASE['gross']:,.0f}", num(BASE['gross_ps'])],
        [f"Less {pc(DISC, 0)} discount", "Conglomerate and governance", f"{-BASE['gross'] * DISC:,.0f}", num(-BASE['gross_ps'] * DISC)],
        ["Base value", f"{SH:,.0f}m economic shares", f"{BASE['net']:,.0f}", num(BASE_VALUE)],
    ],
    num_cols={2, 3}, total_row_idx=9,
), [27, 43, 13, 17]))
A('</div><div class="col">')
A(f'<img class="chart" src="file://{D}/chart_parts.png">')
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2027 EPS, KRW", "Normal memory, KRW tn", "Normal P/E", "Value, KRW", "Change", "Weight"],
    [
        ["Bear", "Prices turn in 2027; 2028 memory sales fall 35%; normal margin 19%", num(sb["eps27"]), f"{sb['n']:.1f}",
         f"{SCEN[0][3]}x", num(bear), chg(bear), "25%"],
        ["Base", "Tight through 2028, half the excess in 2029; normal margin 30%", num(sm["eps27"]), f"{sm['n']:.1f}",
         f"{SCEN[1][3]}x", num(base), chg(base), "50%"],
        ["Bull", "2027 near consensus; shortage lasts to 2029; normal margin 40%", num(su["eps27"]), f"{su['n']:.1f}",
         f"{SCEN[2][3]}x", num(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {num(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [8, 34, 11, 12, 8, 12, 8, 7]))
A(caption(f"2027 memory sales: bear KRW {SCEN[0][4]:.0f}tn at {pc(SCEN[0][5], 0)}; base {MEM27:.0f} at {pc(MEM_OPM27, 0)}; bull "
          f"{SCEN[2][4]:.0f} at {pc(SCEN[2][5], 0)}. Normal memory sales: bear KRW {sb['nrev']:.0f}tn, base {sm['nrev']:.0f}, bull "
          f"{su['nrev']:.0f}. The normal cases are those of my Micron and SK Hynix notes; the other businesses and the {pc(DISC, 0)} discount "
          "are the same in all three. The band: long when my base value is at least 15% above the price, short when at least 25% below."))
A('</div>')

A('<div class="keeptogether">')
A(section("Sensitivity: normal memory net margin against the multiple on normal earnings"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Normal net margin (value, KRW)"] + [f"{m}x" for m in SENS_X],
    [[pc(m, 0)] + [(f"<b>{num(v)}</b>" if (i == 1 and j == 1) else num(v)) for j, v in enumerate(r)]
     for i, (m, r) in enumerate(zip(SENS_NM, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{'All nine' if above == 9 else str(above)} cells sit above the price, but the lowest, {krw(VGRID[0][0])}, only by "
       f"{(VGRID[0][0] / PRICE - 1) * 100:.1f}%. The grid holds the discount at {pc(DISC, 0)}. The discount matters as much: at 10% the "
       f"base is {krw(DISC_ROW[1])}, at none {krw(DISC_ROW[0])}, and at 30% {krw(DISC_ROW[3])}. Take the cash away and the base falls to "
       f"{krw(NOCASH)}, {chg(NOCASH)}. Every figure is live in the model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape and valuation cross-check"))
A('<div class="chartsrow"><div class="col left">')
A(cols(datatable(
    ["Company", "P/E on consensus", "Year"],
    [["Samsung Electronics (common)", f"{PEC27:.1f}x", "CY2027"]] + [[c, f"{px / e:.1f}x", y] for c, t, px, e, y, d in PEERS],
    num_cols={1},
), [48, 26, 26]))
A(caption("Price over consensus EPS for the year ending in 2027, stockanalysis.com (S&P Global), retrieved 2 November 2026. Prices: "
          "Seoul closes of 2 November, Micron's Nasdaq close of 30 October. Micron's year ends in August. Samsung is the only one of the "
          "three with phones, TVs, displays and a foundry inside. Multiples only; no view on the peers' shares."))
A('</div><div class="col">')
A(f'<img class="chart" src="file://{D}/chart_valuation.png">')
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["27 November 2026", "Q3 dividend paid (KRW 4,601 a share)", "Treasury share purchases and cancellations into the year end"],
        ["Early January 2027 (expected)", "Q4 2026 preliminary results", "Memory profit against my KRW 131tn chip operating profit"],
        ["Late January 2027", "Q4 results; board sets the 2026 return", "Amount against KRW 90 to 110tn; preferred share of buybacks"],
        ["First half 2027", "HBM4E mass production", "Any custom HBM customer or date; base die foundry"],
        ["2027", "Taylor fab and 2nm ramp", "Foundry sales, and whether base dies stay in house"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The cycle turns early.</strong> The chip division, almost all of it memory, earns nearly all the profit, and its prices have soared in a year. SK Hynix aims to "
       f"double its wafer capacity in five years and Micron's new fabs start in 2027. If prices fall in 2027 my bear case applies, {chg(bear)}. "
       "<strong>The cash stays in the group.</strong> Samsung had planned or completed about KRW 35tn of 2026 returns by October, against "
       "nine months of free cash flow near KRW 186tn. If the January plan disappoints, my base falls below the price."))
A(para("<strong>Custom HBM goes to the buyer's foundry.</strong> If NVHBM's base die is made at TSMC, Samsung's one roof matters less and "
       "its foundry loses the base die sales that lifted it this year. <strong>The won.</strong> A stronger won cost about KRW 10tn of third "
       "quarter operating profit against the second. <strong>Phones.</strong> A longer squeeze would cut the KRW 91tn I give MX, a small "
       "part of the value."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Back to no call:</strong> a price above about {krw(REVISIT_HI, 500)}, where my base would sit less than 15% above it, with "
       "my numbers unchanged. <strong>Towards the bull case:</strong> a January return plan at the top of the range, weighted towards "
       "cancelled shares."))
A(para("<strong>The view is wrong if</strong>, by October 2027, Samsung reports a quarter in which memory sales and DRAM prices both fall "
       "on the quarter before, which points to my bear case; or the 2026 shareholder return it finalises in late January 2027 comes in below "
       "KRW 90tn, the bottom of its own range, which says the cash I count stays inside the group."))
A('</div>')

A(section("Conclusion"))
A(para("My piece of 31 October argued that from HBM4E the biggest buyer designs the bottom of the memory stack. Samsung is the maker best "
       "placed to build such a stack under one roof, and the one least likely to ship it in volume by the end of 2027. The shares are a "
       f"different question: HBM is about {pc(HBM_REV[1] / MEM26, 0)} of memory sales, and the rest is an ordinary memory boom inside a conglomerate. At "
       f"{PEC27:.1f} times consensus the price assumes the boom ends badly and the cash stays in the group. Base value {krw(BASE_VALUE)}, "
       f"{chg(BASE_VALUE)}, range {krw(bear)} to {krw(bull)}. {my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, "
       f"target {tp_txt}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Memory sales, KRW tn", f"{MEM26:.1f}", f"{MEM27:.0f}", f"{BASE_Y['m28']:.0f}", "Nine months reported plus Q4 of 170; 2028 down 10%"],
        ["Chip or memory operating margin", f"Q4 {pc(Q4['ds_opm'], 0)}", pc(MEM_OPM27, 0), pc(MEM_OPM28, 0), "Q3 2026 chip division 72%"],
        ["Other businesses' operating profit", f"Q4 {Q4['op'] - Q4['ds'] * Q4['ds_opm']:.1f}", f"{sum(v[1] for k, v in OTH27.items() if k != 'nonmem'):.1f}", f"{sum(v[1] for k, v in OTH28.items() if k != 'nonmem'):.1f}", "Phones squeezed in 2027; 2025 18.7"],
        ["Tax rate", "", pc(TAX, 0), pc(TAX, 0), "Q3 2026 23.8%; Q2 24.2%"],
        ["Capex, KRW tn", f"{CAPEX_26}", f"{CAPEX27:.0f}", "", "2026 plan; industry capex to rise significantly in 2027"],
        ["Normal margin, multiple, rate, discount", "", "", f"{pc(NM, 0)}, {MULT}x, 10%, {pc(DISC, 0)}", "As in my Micron and SK Hynix notes; discount mine"],
    ],
), [26, 9, 9, 15, 41]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Samsung Electronics earnings call decks for 1Q, 2Q and 3Q 2026 and for 4Q 2018, 2019, 2021, 2022, 2024 and 2025 '
  '(Samsung IR). Samsung 3Q 2026 earnings call, 29 October 2026 (transcript via Investing.com). Samsung filings to the London Stock '
  'Exchange of 31 March, 12 October and 29 October 2026 (share cancellation, buyback and treasury shares, third quarter dividend, 2026 '
  'capital spending plan); Samsung 2026 half-year business report, filed 31 August 2026 (shares issued). SK hynix prospectus '
  '(Form 424B4), 10 July 2026 (IDC HBM market shares). Samsung newsroom, 12 February 2026 (HBM4, base die, custom HBM, '
  'HBM sales). Micron prepared remarks of 23 September 2025; SK Hynix release of 19 April 2024; Nvidia NVHBM blog, 26 August 2026. stockanalysis.com '
  '(S&P Global) for 2021 to 2025 annual figures, consensus and peers, retrieved 2 November 2026. KRX closes via Naver Finance and '
  'stockanalysis.com and the Hana Bank KRW/USD notice rate via Naver, retrieved 2 November 2026. Estimates from the fourth quarter of 2026, '
  'HBM revenue, normal earnings, the other businesses, the discount and the valuation are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 31 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/memory-not-maths/">thephysicallayer.fyi/journal/memory-not-maths</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Samsung Electronics. Personal research, not investment advice.</p>')
A('<p class="signoff">Tommy Lau | The Physical Layer | thephysicallayer.fyi</p>')
A('</div>')

html = page_shell("\n".join(x for x in P_ if x), FOOT, DLONG).replace("</style>", EXTRA_CSS + "</style>")
hp = f"{D}/{SLUG}_note.html"
open(hp, "w", encoding="utf-8").write(html)
render_pdf(hp, PDF)

import pypdfium2 as pdfium
doc = pdfium.PdfDocument(PDF)
print("pages", len(doc))
doc[0].render(scale=2).to_pil().save(PNG)
print("thumb", PNG)
