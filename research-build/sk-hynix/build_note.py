# -*- coding: utf-8 -*-
"""SK hynix Inc. (KRX: 000660) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/sk-hynix.md.
"""
import datetime
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "SK hynix Inc. (KRX: 000660)"
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


def krw(x, r=1000):
    from decimal import Decimal, ROUND_HALF_UP
    q = int(Decimal(repr(x / r)).quantize(Decimal(1), rounding=ROUND_HALF_UP)) * r
    return f"KRW {q:,.0f}"


def num(x, r=1000):
    return krw(x, r)[4:]


def chg(v):
    x = v / PRICE - 1
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
half_cash = BASE_VALUE - 0.5 * NC_PS

A('<h1 class="doctitle">SK hynix Inc.</h1>')
A('<p class="docsubtitle"><b>KRX: 000660 (ADS: Nasdaq SKHY) | DRAM including HBM, and NAND flash | Icheon, Korea</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"KRW {PRICE:,.0f} (KRX close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"KRW {PRICE:,.0f}, KRX close {PRICE_DATE}; 52-week range KRW {LO52[0]:,.0f} to {HI52[0]:,.0f} (intraday, regular session)"),
    ("Market value", f"About KRW {MCAP:,.0f}tn on {SH:.1f}m shares; US${MCAP / FX * 1000:,.0f}bn at KRW {FX:,.0f} per US$ (2 Nov)"),
    ("Net cash, 30 Sep 2026", f"KRW {NET_CASH:.1f}tn; KRW {NET_CASH - BUY_OCT:.1f}tn after October share purchases, KRW {NC_NOW_PS:,.0f} a share"),
    ("P/E", f"{PE26:.1f}x my 2026; {PEC27:.1f}x 2027 consensus; {PE27:.1f}x my 2027"),
    ("Consensus (stockanalysis.com)", f"EPS KRW {CONS_EPS_26:,.0f} 2026, KRW {CONS_EPS_27:,.0f} 2027; average target KRW {CONS_TP:,.0f}"),
    ("Q3 2026 (28 Oct)", "Revenue KRW 104.6tn; operating margin 80%; Q4 DRAM bits guided up mid 20s %"),
    ("HBM", "Not disclosed; my estimate about 11% of 2026 revenue, against about 30% in 2025"),
    ("Next results", "Q4 2026, expected late January 2027 (not yet confirmed by SK hynix)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">SK Hynix is sold as an HBM company. Nine tenths of its revenue is ordinary memory, and the price already assumes the worst.</p>')
A(para("SK Hynix leads the world in HBM, the memory stacked beside AI chips. On 31 October I argued that from HBM4E the biggest buyer "
       "designs the bottom of that memory stack. But HBM is now a small slice of SK Hynix's money: on my estimates about "
       f"{pc(HBM_REV26_SHARE, 0)} of 2026 revenue, against about {pc(HBM_REV[0] / REV10[-1], 0)} in 2025, because ordinary memory prices have soared while HBM was priced a year ahead."))
A(para(f"At KRW {PRICE:,.0f} the shares trade at {PEC27:.1f} times 2027 consensus earnings. On my method the price needs normal "
       f"earnings worth a {pc(NEED_NM)} net margin once the cash is counted, about half SK Hynix's ten-year {pc(CYC_NM)}. Only if the cash "
       f"is spent and earns nothing does the price look fair: then it needs {pc(NEED_NM_NOCASH)}, close to my base of {pc(NM, 0)}."))
A(para(f"<b>{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {tp_txt}.</b> My base value is "
       f"{krw(BASE_VALUE)}, {chg(BASE_VALUE)}. The bear case is {krw(bear)} ({chg(bear)}) and the bull case {krw(bull)} ({chg(bull)}). "
       "The margin of safety is the cash, so the call rests on SK Hynix returning it."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials (KRW trillion unless stated; calendar years)"))
A(datatable(
    ["KRW trillion unless stated", "2024A", "2025A", "2026E*", "2027E*", "2028E*", "Normal year*"],
    [
        ["Revenue", f"{REV10[-2]:.1f}", f"{REV10[-1]:.1f}", f"{REV26:.1f}", f"{R27:.1f}", f"{REV28:.1f}", f"{normal_rev():.1f}"],
        ["Revenue growth (%)", f"{(REV10[-2] / REV10[-3] - 1) * 100:.0f}", f"{(REV10[-1] / REV10[-2] - 1) * 100:.0f}", f"{(REV26 / REV10[-1] - 1) * 100:.0f}", f"{(R27 / REV26 - 1) * 100:.0f}", f"{G28 * 100:.0f}", ""],
        ["  HBM (my estimate)", "", f"{HBM_REV[0]:.1f}", f"{HBM_REV[1]:.1f}", f"{HBM_REV[2]:.1f}", "", ""],
        ["  HBM share of revenue (%)", "", f"{HBM_REV[0] / REV10[-1] * 100:.0f}", f"{HBM_REV26_SHARE * 100:.0f}", f"{HBM_REV27_SHARE * 100:.0f}", "", ""],
        ["Operating profit", f"{OP24:.1f}", f"{OP25:.1f}", f"{OP26:.1f}", f"{R27 * OPM27:.1f}", f"{REV28 * OPM28:.1f}", ""],
        ["Operating margin (%)", pc(OP24 / REV10[-2]), pc(OP25 / REV10[-1]), pc(OP26 / REV26), pc(OPM27), pc(OPM28), ""],
        ["Net margin (%)", pc(NI10[-2] / REV10[-2]), pc(NI10[-1] / REV10[-1]), pc(NI26 / REV26), pc(NI27 / R27), pc(BASE_Y["ni28"] / REV28), pc(NM)],
        ["EPS (KRW)", "28,419", f"{EPS25:,.0f}", f"{EPS26:,.0f}", f"{EPS27:,.0f}", f"{EPS28:,.0f}", f"{N_BASE:,.0f}"],
        ["Consensus EPS (KRW)", "", "", f"{CONS_EPS_26:,.0f}", f"{CONS_EPS_27:,.0f}", "", ""],
        [f"P/E at KRW {PRICE:,.0f} (x)", f"{PRICE / 28418.66:.0f}", f"{PE25:.1f}", f"{PE26:.1f}", f"{PE27:.1f}", f"{PE28:.1f}", f"{PE_NORMAL:.1f}"],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*2026E is reported profit for the first nine months (including finance items such as Kioxia gains) plus my fourth quarter; "
          "2027E, 2028E and the normal year are my own estimates on operations only, taxed at 22%. EPS for my years is on the "
          f"{SH:.1f}m shares entitled to the third quarter dividend. HBM revenue is not disclosed; the HBM lines are mine. History from SK hynix's "
          "prospectus of 10 July 2026 and results releases; consensus from stockanalysis.com (S&P Global), retrieved 2 November 2026."))

A('<div class="keeptogether">')
A(section("Two charts: a boom in ordinary memory, and HBM a shrinking share of it"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_quarters.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_hbm.png"></div></div>')
A(caption("Left: revenue by quarter and operating margin, from SK hynix's results releases; Q4 2026 is my estimate. Right: my estimate of HBM "
          "revenue against the rest. Industry HBM of about US$35bn in 2025 growing about 40% a year (Micron, 17 December 2025, as in my "
          "Micron note), SK Hynix's share 58, 55 and 50% (IDC: 56.4% in Q1 2026, quoted in the prospectus), at my average exchange rates."))
A('</div>')

A(section("The thesis: the supplier now earns most of its money on flour"))
A(para("Go back to the kitchen from the October piece. The chef is the AI chip and the hatch is the memory feeding it. SK Hynix stocks "
       "the pantry, and it built the best hatch in the business. This year the pantry's ordinary goods, the flour and the oil, have become "
       "the scarce part. Their price has soared, while the hatch was sold a year ahead at last year's price."))
A(para(f"<strong>The pantry is full.</strong> Third quarter revenue was KRW {Q_REV[-1]:.1f}tn, up 328% on a year earlier, and operating "
       f"profit KRW {Q_OP[-1]:.1f}tn, an 80% margin against 47%. DRAM bits rose about 10% on the quarter and DRAM prices by a high twenties "
       "percentage; NAND prices rose by a mid twenties percentage. SK Hynix guides fourth quarter DRAM bits up by a mid twenties percentage. "
       "First quarter DRAM revenue was 2.9 times a year earlier, and Gartner, quoted in the prospectus, forecast conventional DRAM prices "
       "to roughly triple year on year by the second quarter."))
A(para("<strong>HBM is now a small slice.</strong> SK Hynix's last HBM figure I could find is for the fourth quarter of 2024, when HBM was "
       "more than 40% of DRAM revenue; HBM revenue more than doubled in 2025. On my estimate HBM was about "
       f"KRW {HBM_REV[0]:.1f}tn in 2025, {pc(HBM_REV[0] / REV10[-1], 0)} of revenue, and is about KRW {HBM_REV[1]:.0f}tn of my "
       f"KRW {REV26:.1f}tn in 2026, {pc(HBM_REV26_SHARE, 0)}. Two primary figures point the same way: the largest customer took "
       "23.9% of 2025 revenue, while in the first quarter of 2026 the two largest took 14.8% and 12.4%; sales booked in China rose from "
       "19.7% to 24.3% of revenue. Micron says its 2027 HBM prices narrow \"the gross margin gap with conventional DRAM\", so HBM earns "
       f"the lower margin today. At my {pc(HBM_OPM26, 0)} HBM margin it is about {pc(HBM_OP26_SHARE, 0)} of 2026 operating profit."))
A(para("<strong>Custom HBM decides how durable that slice is.</strong> On 28 October SK Hynix's head of HBM sales said \"we are seeing "
       "growing importance of custom HBM\", and SK Hynix runs joint projects with major customers. The piece did not cite the July "
       "prospectus, which defines custom HBM as integrating \"certain functions of GPUs and ASICs into the HBM base die\" and lists custom "
       "base die integration in its HBM4E work. None of it gives a date for volume, so the piece's claim stays open. A base die drawn by the "
       "buyer ties each stack to one chip, which protects the leader's tenth; but Nvidia says NVHBM will be \"available from multiple "
       "memory providers\", so pricing power moves to the buyer, as the piece argued."))
A(para("<strong>Moat or capex trap.</strong> Custom is a moat for the tenth. For the other nine tenths the risk is the old one: too many "
       "fabs. The prospectus says SK Hynix is \"targeting to double our wafer production capacity within the next five years\" and expects "
       "to invest about KRW 600tn at Yongin, the fourth fab's first cleanroom due by 2033. 2027 capital spending will \"increase "
       f"significantly\". Against that, long-term agreements with {LTA_N} customers cover more than half of 2027 and 2028 capacity, "
       "generally for five years, priced within agreed ranges with safeguards such as deposits."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At KRW {PRICE:,.0f} SK Hynix is worth about KRW {MCAP:,.0f}tn on {SH:.1f}m shares (730.5m issued less 25.3m in treasury, "
       f"matching the third quarter dividend of KRW 14.10tn at KRW 20,000 a share). It trades at {PEC27:.1f} times 2027 consensus, against {PEER_PE[0][1]:.1f} times for Samsung "
       f"Electronics and {PEER_PE[1][1]:.1f} times for Micron's fiscal 2027, and is {abs(OFF_HIGH) * 100:.0f}% below its June high. "
       "As in my Micron note, peak memory earnings are not a stream to capitalise: SK Hynix lost KRW 9.1tn in 2023, a year after record "
       f"revenue, and earned {pc(CYC_NM)} net over 2016 to 2025, with {pc(PEAK18_NM)} at the 2018 peak."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_eps.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_price.png"></div></div>')
A(caption("Left: EPS, reported for 2025, my estimates for 2026 to 2028, my base normal year, and the normal year the price needs with the "
          "cash kept and with it spent. Right: month-end KRX close, September 2023 to the 2 November 2026 close (Yahoo Finance, checked against "
          "stockanalysis.com, retrieved 2 November 2026), against my base value."))
A('</div>')
A(para(f"<strong class='lead'>What the price needs.</strong> I value the cycle with the method and normal cases of my Micron note: net "
       f"cash at September 2027, plus earnings above normal still to come, plus {MULT} times normal earnings. I expect net cash of about "
       f"KRW {NC_SEP27:.0f}tn by then, {krw(NC_PS)} a share, before dividends and cancellations. On that, the price needs normal EPS of "
       f"only about {krw(NEED_N, 100)}: a {pc(NEED_NM)} net margin on my normal revenue, about half the ten-year margin."))
A(para(f"<strong class='lead'>Where I differ.</strong> The market does not believe the cash reaches holders. If it is spent and earns "
       f"nothing, the price needs normal EPS of about {krw(NEED_N_NOCASH, 100)}, a {pc(NEED_NM_NOCASH)} margin, close to my base. So "
       "the price is roughly my base with the cash thrown away. I think that is too harsh: SK Hynix plans about KRW 100tn of "
       "shareholder returns for 2026, at least KRW 30tn in dividends and KRW 60tn in cancelled shares, says it intends to return at "
       f"least half its free cash flow, and cancels 23.7m shares on 5 November. With only half the cash, my base is about {krw(half_cash, 10000)}, "
       f"{chg(half_cash)}. One sign of the gap: on 30 October the ADSs closed at US${ADS_OCT30} for a tenth of a share, about "
       f"{pc(ADS_PREMIUM, 0)} above Seoul at the day's rate; the prospectus warns withdrawn shares may not be deposited again."))

A(section("Valuation, with the working"))
A(para(f"I value operations, because reported profit swings with finance items: KRW {Q3_INV_LOSS}tn of investment valuation losses "
       f"and KRW {Q3_FX_LOSS}tn of foreign exchange losses in the third quarter alone. 2026 adds a fourth quarter of KRW {Q4_REV:.0f}tn at "
       f"an 80% margin (consensus implies about 127). 2027 revenue is KRW {R27:.0f}tn, {abs(R27 / CONS_REV_27 - 1) * 100:.1f}% below "
       f"consensus, at a {pc(OPM27, 0)} margin and {pc(TAX, 0)} tax: EPS {krw(EPS27, 100)}, {abs(EPS27 / CONS_EPS_27 - 1) * 100:.1f}% below "
       f"consensus. 2028 revenue falls {abs(G28) * 100:.0f}% at {pc(OPM28, 0)} as M15X and Yongin add supply. Free cash flow is about "
       f"KRW {FCF_Q4:.0f}tn in the fourth quarter and KRW {FCF27:.0f}tn in 2027 after KRW {CAPEX27:.0f}tn of capital spending; I deduct the "
       f"October purchases and KRW {STAFF_BUY:.0f}tn of new purchases set aside for staff pay. Net cash adds {krw(sm['nc'], 100)} a "
       f"share; a quarter of 2027's excess, all of 2028's and half again in 2029, at 10%, add {krw(sm['exc'], 100)}; {MULT} times normal "
       f"EPS of {krw(N_BASE, 100)} adds {krw(sm['term'], 100)}. Total {krw(BASE_VALUE)}. Normal revenue takes the four quarters to June "
       f"2026, nearest Micron's fiscal 2026, grows bits 20% a year for four years at 55% of the price per bit: KRW {normal_rev():.1f}tn."))
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "2027 EPS, KRW", "Normal EPS, KRW", "Normal P/E", "Value, KRW", "Change", "Weight"],
    [
        ["Bear", "Prices turn in 2027; 2028 revenue falls 35%; normal margin 19%", num(sb["eps27"], 100), num(sb["n"], 100),
         f"{SCEN[0][3]}x", num(bear), chg(bear), "25%"],
        ["Base", "Tight through 2028, half the excess in 2029; normal margin 30%", num(sm["eps27"], 100), num(sm["n"], 100),
         f"{SCEN[1][3]}x", num(base), chg(base), "50%"],
        ["Bull", "2027 above consensus; shortage lasts to 2029; normal margin 40%", num(su["eps27"], 100), num(su["n"], 100),
         f"{SCEN[2][3]}x", num(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {num(WEIGHTED)}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 4, 5, 6, 7}, total_row_idx=3,
), [8, 34, 12, 12, 7, 12, 8, 7]))
A(caption(f"2027 revenue: bear KRW {SCEN[0][4]:.0f}tn at {pc(SCEN[0][5], 0)}; base {R27:.0f} at {pc(OPM27, 0)}; bull {SCEN[2][4]:.0f} at "
          f"{pc(SCEN[2][5], 0)}. Normal revenue: bear KRW {sb['nrev']:.0f}tn, base {sm['nrev']:.0f}, bull {su['nrev']:.0f}. The normal cases "
          "are those of my Micron note. Unlike there, the bear also cuts 2027, because SK Hynix's year runs to December and its agreements set "
          "price ranges, not fixed prices. The band: long when my base value is at least 15% above the price, short when at least 25% below."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: normal net margin against the multiple on normal earnings"))
A('<div class="chartsrow"><div class="col left">')
A(datatable(
    ["Normal net margin (value, KRW)"] + [f"{m}x" for m in SENS_X],
    [[pc(m, 0)] + [(f"<b>{num(v)}</b>" if (i == 1 and j == 1) else num(v)) for j, v in enumerate(r)]
     for i, (m, r) in enumerate(zip(SENS_NM, VGRID))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
A(para(f"{'All nine' if above == 9 else str(above)} cells sit above the price; the lowest, {krw(VGRID[0][0])}, is "
       f"{(VGRID[0][0] / PRICE - 1) * 100:.0f}% above. The grid holds the cash fixed. Take the cash away and the base falls to about "
       f"{krw(BASE_VALUE - NC_PS)}, {chg(BASE_VALUE - NC_PS)}, which is why the cash is the call. Every figure is live in the model."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape and valuation cross-check"))
A('<div class="chartsrow"><div class="col left">')
A(cols(datatable(
    ["Company", "P/E on consensus", "Year"],
    [["SK Hynix", f"{PEC27:.1f}x", "CY2027"]] + [[c, f"{px / e:.1f}x", y] for c, t, px, cur, e, y, w, nt in PEERS],
    num_cols={1},
), [44, 28, 28]))
A(caption("Price over consensus EPS for the year ending in 2027, stockanalysis.com (S&P Global), retrieved 2 November 2026. Prices: Seoul "
          "closes of 2 November, Micron's Nasdaq close of 30 October. Micron's year ends in August. Multiples only; no view on the peers' shares."))
A('</div><div class="col">')
A(f'<img class="chart" src="file://{D}/chart_valuation.png">')
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["5 November 2026", "Cancellation of 23.7m shares (KRW 40.0tn)", "Share count; the next quarterly buyback resolution"],
        ["Late January 2027 (expected)", "Q4 2026 results and the annual dividend", "DRAM price and bits; the rest of the Kioxia special dividend; 2027 capex"],
        ["Early 2027", "First Yongin cleanroom opens", "Pace of tool-in against the 'increase significantly' capex guide"],
        ["March 2027", "Nvidia GTC", "Any NVHBM date or partner list naming SK Hynix"],
        ["Through 2027", "HBM4E qualification", "First SK Hynix statement of custom HBM in volume"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>The cycle turns early.</strong> About nine tenths of revenue rides on ordinary DRAM and NAND prices that have soared in a "
       "year, and Micron says server makers already use a \"modestly lower rate of content growth\". If prices fall in 2027 my bear case "
       f"applies, {chg(bear)}. <strong>The capex trap.</strong> Doubling wafer capacity in five years, with Samsung, Micron and Chinese makers "
       "seeing the same price signal, can consume the cash I count; then the price is about fair."))
A(para("<strong>Custom HBM moves the edge to the buyer.</strong> My numbers already let SK Hynix's HBM share fall to half by 2027 as "
       "Samsung's HBM4 ramps; that costs the most durable tenth, not the bulk. <strong>The won.</strong> It moved from KRW 1,538 to the "
       "dollar on 2 July to KRW 1,341 now, which cuts dollar sales in won. <strong>Leakage.</strong> About KRW 10tn of the new KRW 20tn "
       "buyback goes to staff pay, on top of profit sharing of 10% of operating profit."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Back to no call:</strong> a price above about {krw(REVISIT_HI)}, where my base would sit less than 15% above it, with my "
       "numbers unchanged. <strong>Towards the bull case:</strong> SK Hynix confirming custom HBM in volume and agreements covering more "
       "than half of 2029 capacity."))
A(para("<strong>The view is wrong if</strong>, by October 2027, SK Hynix reports a quarter in which total revenue and DRAM average selling "
       "price both fall on the quarter before, which points to my bear case; or it returns less than half of its free cash flow to "
       "shareholders for 2026 or 2027, which turns the cash I count into the capital spending the price already assumes."))
A('</div>')

A(section("Conclusion"))
A(para("My piece of 31 October argued that from HBM4E the biggest buyer designs the bottom of the memory stack. SK Hynix's own words "
       "since support the direction, and the claim stays open until a maker reports volume. The shares are a different question. HBM is "
       f"about a tenth of revenue; the rest is an ordinary memory boom. At {PEC27:.1f} times consensus the price assumes the boom ends badly "
       f"and its cash is spent for nothing. Base value {krw(BASE_VALUE)}, {chg(BASE_VALUE)}, range {krw(bear)} to {krw(bull)}. "
       f"{my_call}: {CALL['direction']}, {CALL['conviction'].lower()} conviction, target {tp_txt}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "2026E", "2027E", "2028E", "Basis"],
    [
        ["Revenue, KRW tn", f"{REV26:.1f}", f"{R27:.1f}", f"{REV28:.1f}", "Nine months reported plus Q4 of 128; 2027 6% below consensus; 2028 down 10%"],
        ["Operating margin", pc(OP26 / REV26), pc(OPM27), pc(OPM28), "Q3 2026 80%"],
        ["Tax rate", "", pc(TAX, 0), pc(TAX, 0), "Q1 2026 21.8%; Q3 2026 about 21.6%"],
        ["Capex, KRW tn", "Q4 14", f"{CAPEX27:.0f}", "", "'Increase significantly' in 2027; 2025 27.5"],
        ["Shares, m", f"{SH:.1f}", f"{SH:.1f}", f"{SH:.1f}", "Held; cancellations treated as cash returned"],
        ["Normal margin, multiple, rate", "", "", f"{pc(NM, 0)}, {MULT}x, 10%", "As in my Micron note; 2016 to 2025 23.5%"],
    ],
), [24, 9, 9, 12, 46]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">SK hynix preliminary results releases of 23 January 2025 (as reprinted), 28 January 2026, 23 April 2026, '
  '29 July 2026 and 28 October 2026. Forms 6-K of 26 and 28 October 2026 (results, treasury shares, cancellation, dividend, shareholder '
  'return plan, new buyback). Third quarter 2026 earnings call, 28 October 2026. Prospectus (Form 424B4), 10 July 2026, for 2023 to 2025 '
  'and Q1 2026 financials, revenue by product, customers, regions, share count, ADS terms, the Yongin plan and custom HBM, with IDC and '
  'Gartner figures as quoted there. Annual results releases for 2016 to 2020; stockanalysis.com (S&P Global) for 2021 to 2025, consensus '
  'and peers, retrieved 2 November 2026. Micron call of 17 December 2025 and prepared remarks of 30 September 2026; Nvidia NVHBM blog, '
  '26 August 2026. KRX closes via Yahoo Finance and stockanalysis.com, the Hana Bank KRW/USD notice rate via Naver Finance and ADS closes from Nasdaq.com, retrieved '
  '2 November 2026. Estimates from the fourth quarter of 2026, HBM revenue, normal earnings and the valuation are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 31 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/memory-not-maths/">thephysicallayer.fyi/journal/memory-not-maths</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in SK hynix. Personal research, not investment advice.</p>')
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
