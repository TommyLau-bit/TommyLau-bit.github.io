# -*- coding: utf-8 -*-
"""Hitachi, Ltd. (TSE: 6501) initiation note. House style per _note_template/common.py.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
The banner and call wording come from CALL in data.py; text of record is src/content/calls/hitachi.md.
"""
import datetime
from decimal import Decimal, ROUND_HALF_UP
from common import page_shell, section, para, datatable, rating_banner, statbox, caption
from render import render_pdf
from data import *

D = BUILD_DIR
FOOT = "Hitachi, Ltd. (TSE: 6501)"
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


def yen(x, d=0):
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"¥{q:,.{d}f}"


def bn(x, d=0):
    q = Decimal(repr(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"{q:,.{d}f}"


def neg(s, v):
    return f"({s.replace('-', '')})" if v < 0 else s


def chg(v):
    x = v / PRICE - 1
    return f"{'up' if x >= 0 else 'down'} {abs(x) * 100:.0f}%"


bear, base, bull = VALS
tgt = CALL["target"]
tp_txt = yen(tgt) if tgt else "None (no call)"
up_txt = f"{(tgt / PRICE - 1) * 100:+.0f}%" if tgt else f"Base value {yen(BASE_VALUE)} ({(BASE_VALUE / PRICE - 1) * 100:+.0f}%)"
banner = CALL["banner"].replace(": ", ":<br/>") if CALL["draft"] else CALL["banner"]
my_call = "My draft view" if CALL["draft"] else "My call"
conv = CALL["conviction"].lower()
SH = SOTP_EV + ADJ

A('<h1 class="doctitle">Hitachi, Ltd.</h1>')
A('<p class="docsubtitle"><b>TSE: 6501 | Grid equipment (Hitachi Energy), IT services, rail and industrial products | Tokyo</b></p>')
A(f'<p class="docmeta">Tommy Lau | {DLONG} | Initiation of coverage | Independent research</p>')
A(rating_banner(banner, tp_txt, f"{yen(PRICE)} (TSE close, {PRICE_DATE})", up_txt))
if CALL["draft"]:
    A('<p class="draftnote">DRAFT for review. The view below is a draft; the final call is Tommy Lau\'s and is not yet made.</p>')

A('<div class="clearfix"><div class="sidebar">')
A(statbox([
    ("Last price", f"{yen(PRICE)}, TSE close {PRICE_DATE}, a record close; intraday high {yen(HI_INTRA)} (10 Feb 2026); lowest close of 2026 {yen(LO_CLOSE_26)} (31 Mar)"),
    ("Market value", f"About ¥{MCAP / 1000:.1f} trillion on {SHARES:,.0f}m shares outstanding, net of treasury stock (30 Jun 2026)"),
    ("Balance sheet, 30 Jun 2026", f"Cash ¥{CASH:,.0f}bn, interest-bearing debt ¥{DEBT:,.0f}bn; investments ¥{EQUITY_METHOD + SECURITIES:,.0f}bn at book"),
    ("FY2026 forecast (29 Jul 2026)", f"Revenue ¥{GROUP_REV26:,.0f}bn; adjusted EBITA ¥{GROUP_EBITA26:,.0f}bn (13.0%); EPS ¥{EPS26:.2f}"),
    ("Hitachi Energy, FY2026 forecast", f"Revenue US${HE_REV[2]}bn, adjusted EBITA US${HE_EBITA[2]:.2f}bn (14.8%); backlog US$63.6bn at 30 Jun 2026"),
    ("Hitachi Energy in Hitachi", f"{HE_SHARE_REV26 * 100:.0f}% of FY2026 revenue, {HE_SHARE_EBITA26 * 100:.0f}% of adjusted EBITA, {HE_SHARE_SOTP_EQ * 100:.0f}% of my sum of the parts"),
    ("Consensus (stockanalysis.com)", f"FY2026 EPS ¥{CONS_EPS_26:.2f}; average target {yen(CONS_TP)} ({CONS_N} analysts)"),
    ("Next event", "Q2 FY2026 results, 28 October 2026 (confirmed by Hitachi)"),
]))
A('</div><div class="maincol">')
A('<p class="lede">Hitachi Energy\'s queue will outlast its new factories. At ¥5,840, Hitachi already prices in most of what that is worth.</p>')
A(para("Hitachi Energy, Hitachi's grid business, makes power transformers, HVDC links and high voltage switchgear. My piece of "
       "22 October argued that it builds factories only as fast as signed orders justify, so its queue of about three years of "
       "sales will not clear through fiscal 2030. Hitachi Energy is not listed on its own, so this note is on its parent."))
A(para(f"The claim holds. At the end of June the backlog was US$63.6bn, {RATIO_JUN26:.2f} times revenue over the previous four "
       f"quarters, and Hitachi plans to keep the ratio at 2.5 to 3 times. But the queue that makes the revenue visible also caps "
       f"it, and Hitachi Energy is {HE_SHARE_SOTP_EQ * 100:.0f}% of my value of Hitachi. At {yen(PRICE)} the market values it at "
       f"about {HE_IMPLIED_MULT:.0f} times my fiscal 2027 estimate of its adjusted EBITA, with the rest at my base multiples, and Hitachi as a whole at "
       f"{PE_G26:.0f} times its own earnings forecast."))
A(para(f"<b>{my_call}: {CALL['direction']}, {conv} conviction.</b> My base sum of the parts is worth {yen(BASE_VALUE)}, "
       f"{chg(BASE_VALUE)}, inside a range of {yen(bear)} ({chg(bear)}) to {yen(bull)} ({chg(bull)}). I would revisit below "
       "about ¥5,600, or if Hitachi lifts its fiscal 2027 target for Hitachi Energy above US$28bn at a 16% margin."))
A('</div></div>')

A('<div class="fullwidth">')
A('<div>')
A(section("Key financials (fiscal years to March; adjusted EBITA is Hitachi's measure)"))
A(datatable(
    ["", "FY2024A", "FY2025A", "FY2026 forecast", "FY2027E*", "FY2027 target", "FY2030 plan"],
    [
        ["Hitachi Energy revenue, US$bn", f"{HE_REV[0]:.1f}", f"{HE_REV[1]:.1f}", f"{HE_REV[2]:.2f}", f"{HE_REV27:.1f}", "about 26", "36"],
        ["Growth (%)", "", f"{HE_GROWTH_25 * 100:.0f}", f"{HE_GROWTH_26 * 100:.0f}", f"{HE_G27 * 100:.0f}", "", ""],
        ["Adjusted EBITA margin (%)", f"{HE_MARGIN[0] * 100:.1f}", f"{HE_MARGIN[1] * 100:.1f}", f"{HE_MARGIN[2] * 100:.1f}", f"{HE_M27 * 100:.1f}", "15+", "16 to 20"],
        ["Adjusted EBITA, US$bn", f"{HE_EBITA[0]:.2f}", f"{HE_EBITA[1]:.2f}", f"{HE_EBITA[2]:.2f}", f"{HE_EBITA27_USD:.2f}", "", ""],
        ["Adjusted EBITA, ¥bn at ¥160", "", "", f"{HE_EBITA26_YEN:.0f}", f"{HE_EBITA27:.0f}", "", ""],
        ["Group revenue, ¥bn", "", f"{GROUP_REV25:,.0f}", f"{GROUP_REV26:,.0f}", "", "", ""],
        ["Group adjusted EBITA, ¥bn", "", f"{GROUP_EBITA25:,.0f}", f"{GROUP_EBITA26:,.0f}", f"{GROUP_EBITA27:,.0f}", "", ""],
        ["EV / group adjusted EBITA at ¥5,840 (x)", "", "", f"{EV_EBITA26:.1f}", f"{EV_EBITA27:.1f}", "", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6},
))
A(caption("*FY2027E is my own estimate, not Hitachi's. Hitachi Energy figures in US dollars as Hitachi reports them: FY2024 from the results "
          "of 28 April 2025, FY2025 from 27 April 2026, the FY2026 forecast as raised on 29 July 2026; targets from the Investor Day of 10 June "
          "2026. Group FY2025 is restated for the April 2026 segment changes. EV is market value less net cash and investments at book, plus "
          "minority interests and pensions."))
A('</div>')

A('<div class="keeptogether">')
A(section("Two charts: Hitachi Energy's earnings path, and a valuation that sits a little above the price"))
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_annual.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_valuation.png"></div></div>')
A(caption("Left: Hitachi Energy revenue and adjusted EBITA margin. FY26G is Hitachi's forecast; FY27E is mine; FY30 is Hitachi's plan, with "
          "its 16 to 20% margin range, at Hitachi's 2026 budget rate. Right: value per share from the base case, the weighted cases, the sensitivity grid and the bear to "
          f"bull range, against the {yen(PRICE)} price (red) and the average analyst target."))
A('</div>')

A(section("The thesis: a joiner booked three years ahead, inside a much larger firm"))
A(para("Think of the joiner from the piece. Her diary is full for three years, so she takes on apprentices and rents a bigger workshop, "
       "but only once new bookings are written down. Each year she builds more wardrobes than the last, and each year the diary still "
       "runs three years ahead. The diary tells a buyer two things. Her revenue next year is close to certain, and it is also capped. "
       "What a buyer gains over time is the price on each new booking, and the efficiency of a bigger, busier workshop."))
A(para(f"Hitachi Energy is that joiner at the scale of national grids. At the end of June 2026 it had US$63.6bn of orders signed but "
       f"not yet delivered, against US${HE_TTM_JUN26:.1f}bn of revenue over the previous four quarters: {RATIO_JUN26:.2f} times. The "
       f"ratio was {RATIO_MAR25:.2f} in March 2025 and {RATIO_MAR26:.2f} in March 2026. Orders were {BTB25:.2f} times revenue in fiscal "
       f"2025, the year to March 2026. In the June quarter, orders in Power Grids, the business unit that holds Hitachi Energy, were "
       f"{Q1_PG_BTB:.2f} times its revenue, lifted by several large HVDC awards in Europe."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_queue.png"></div>'
  f'<div class="col"><img class="chart" src="file://{D}/chart_sotp.png"></div></div>')
A(caption("Left: Hitachi Energy order backlog at quarter end, US$bn; white figures are backlog over revenue for the previous four quarters, "
          "shown where Hitachi's disclosures allow (derived). Sources: results presentations, 28 April 2025 to 29 July 2026. Right: my sum of "
          "the parts per share, built up part by part, against the price (red) and the base value (dotted)."))
A('</div>')
A(para("The plan matches the claim. At its investor day on 10 June, Hitachi showed Hitachi Energy's backlog rising from about US$60bn in "
       "fiscal 2025 to about US$100bn in fiscal 2030, while revenue rises from US$20bn to US$36bn. The slide says the ratio of backlog "
       "to revenue is expected to remain stable at 2.5 to 3 times. The investment programme, more than US$9bn across more than 40 "
       "factories, goes only to \"bankable business cases\". Asked whether investment would grow on the way to 2030, Andreas Schierenbeck, "
       "who runs the business, said Hitachi invests only with a bankable business case and is \"not building over-capacity\", "
       "according to Hitachi's translated summary of the Q&amp;A. Hitachi states the plan figures at its 2026 budget exchange rate."))
A(para("<b>The claim holds on both of its tests.</b> The ratio is 3.06, above the 2.5 floor, and orders have run well ahead of revenue "
       "every year. Nothing in Hitachi's disclosures shows the piece was wrong."))
A(para("The claim has a consequence. If factories follow orders, revenue grows at the pace new capacity allows: Hitachi's own plan "
       "implies about 12% a year from fiscal 2025 to 2030 (at Hitachi's 2026 budget rate). The rest of the value comes from margin, and here the record is good. The "
       "adjusted EBITA margin rose from 11.1% in fiscal 2024 to 13.4% in fiscal 2025; Hitachi forecasts 14.8% for fiscal 2026, more than "
       "15% for fiscal 2027 and 16 to 20% by fiscal 2030. It has also raised its forecasts as each year goes on: in April 2025 it "
       "expected fiscal 2025 revenue of US$18.0bn at 11.9%, and delivered US$19.8bn at 13.4%. In July 2026 it raised fiscal 2026 from "
       "US$23.2bn at 14.3% to US$23.65bn at 14.8%."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para(f"At {yen(PRICE)} Hitachi is worth about ¥{MCAP / 1000:.1f} trillion on {SHARES:,.0f}m shares. Net cash, equity-method and other "
       f"long-term investments at book, less minority interests and the pension liability, add about ¥{ADJ:,.0f}bn, so the enterprise "
       f"value is about ¥{EV_ADJ:,.0f}bn: {EV_EBITA26:.1f} times the raised fiscal 2026 forecast of ¥1,520bn of adjusted EBITA and "
       f"{EV_EBITA27:.1f} times my fiscal 2027 estimate. The shares trade at {PE_G26:.1f} times Hitachi's EPS forecast of ¥{EPS26:.2f} "
       f"and {PE_C26:.1f} times the ¥{CONS_EPS_26:.2f} consensus. Stockanalysis.com puts the forward P/E at {FWD_PE_SA:.1f} times, "
       "against 23.0 for Siemens Energy, 23.9 for ABB, 20.6 for Schneider Electric and 18.3 for Mitsubishi Electric."))
A(para(f"<strong class='lead'>How much of Hitachi is Hitachi Energy.</strong> At Hitachi's assumed ¥160 to the dollar, Hitachi "
       f"Energy's fiscal 2026 forecast is ¥{HE_REV26_YEN:,.0f}bn of revenue, {HE_SHARE_REV26 * 100:.0f}% of the group, and "
       f"¥{HE_EBITA26_YEN:,.0f}bn of adjusted EBITA, {HE_SHARE_EBITA26 * 100:.0f}% of the group's ¥1,520bn. In my sum of the parts it "
       f"is {HE_SHARE_SOTP_EQ * 100:.0f}% of the equity value; the IT business is next at {SOTP['DSS'] / SH * 100:.0f}%."))
A(para(f"<strong class='lead'>What the price implies.</strong> With the rest of Hitachi at my base multiples, which sit below its peers, the price leaves about "
       f"¥{HE_IMPLIED_EV / 1000:.1f} trillion for Hitachi Energy: {HE_IMPLIED_MULT:.1f} times my fiscal 2027 estimate, or about "
       f"US${HE_IMPLIED_USD:.0f}bn. Grid peers trade at a median 24.5 times trailing EV to EBIT, so the market applies a discount inside "
       f"the group, but not a large one. The average target of {CONS_N} analysts is {yen(CONS_TP)}, "
       f"{(CONS_TP / PRICE - 1) * 100:.0f}% above the price. I differ on three points."))
A(para("<strong class='lead'>The queue caps the volume, so the upside is margin.</strong> Hitachi Energy cannot surprise much on revenue "
       "if it builds only against signed orders. My base case takes 12% growth in fiscal 2027 at a 15.5% margin, close to Hitachi's own "
       "target of about US$26bn at more than 15%. The pattern of rising forecasts says the margin may come in higher; that is the bull case."))
A(para(f"<strong class='lead'>Hitachi Energy alone cannot move the whole enough.</strong> Even {MULT['HE']} times its fiscal "
       f"2027 adjusted EBITA, a forward multiple below the 24.5 times trailing peer median, lifts my value of Hitachi to only {yen(BASE_VALUE)}, {chg(BASE_VALUE)}. For 15% upside "
       f"Hitachi Energy needs about {HE_MULT_FOR_LONG:.0f} times with everything else unchanged. The rest of Hitachi grows at 5 to 10%, and "
       "its IT business told investors in June that overseas customers are moving development in house and pressing on price."))
A(para("<strong class='lead'>The yen sits between the queue and the shares.</strong> Hitachi Energy earns in dollars and euros and "
       "Hitachi reports in yen. Group revenue rose 20% in the June quarter, but 12% without currency. I hold the yen at Hitachi's ¥160 to "
       "the dollar; a stronger yen would cut the yen value of every dollar in the queue without changing the queue at all."))
A('<div class="keeptogether">')
A(f'<div class="chartsrow"><div class="col left"><img class="chart" src="file://{D}/chart_price.png"></div><div class="col">')
A(cols(datatable(
    ["Date", "What happened", "Move"],
    [
        ["27 Apr 2026", "FY2025 results; FY2026 forecast of ¥1,420bn adjusted EBITA", f"down {abs(FY_MOVE) * 100:.1f}%"],
        ["10 Jun 2026", "Investor Day; Hitachi Energy plan to FY2030", f"down {abs(ID_MOVE) * 100:.1f}%"],
        ["29 Jul 2026", "Q1 results; FY2026 forecast raised to ¥1,520bn", f"up {Q1_MOVE * 100:.1f}%"],
        ["21 Oct 2026", f"Record close of {yen(PRICE)}, up {RISE_DEC25 * 100:.0f}% in 2026", ""],
    ],
), [20, 60, 20]))
A('</div></div>')
A(caption("Left: Hitachi month-end close, April 2024 to the 21 October 2026 close, split-adjusted, against my base value (red). Yahoo "
          "Finance, retrieved 22 October 2026. Right: moves from the close on the day of each release to the next day's close, as Hitachi "
          "releases results after the market closes."))
A('</div>')

A(section("Valuation, with the working"))
A(para("I value Hitachi as a sum of its parts: each business at a multiple of my fiscal 2027 adjusted EBITA, the year to March 2028, which "
       "the market will price as current by October 2027. I add cash and investments at book, deduct debt, minority interests and the "
       f"pension liability, and divide by {SHARES:,.0f}m shares, with no further buybacks. Hitachi Energy grows 12% in dollars at a 15.5% "
       "margin, converted at ¥160. Digital Systems and Services grows 6%, Connective Industries 5% and Mobility 10% from Hitachi's fiscal "
       "2026 forecasts; corporate costs rise to ¥100bn. All are my estimates."))
A('<div class="keeptogether">')
A(section("Sum of the parts, base case"))
names = [("Hitachi Energy", "HE"), ("Energy, rest (mainly nuclear)", "Eother"), ("Digital Systems & Services", "DSS"),
         ("Connective Industries", "CI"), ("Mobility", "Mobility"), ("Others", "Others"), ("Corporate costs", "Corporate")]
rowsS = [[n, neg(bn(E27[k]), E27[k]), f"{MULT[k]}x", neg(bn(SOTP[k]), SOTP[k]), neg(f"{SOTP[k] / SH * 100:.0f}%", SOTP[k]),
          neg(yen(SOTP[k] / SHARES * 1000), SOTP[k])] for n, k in names]
rowsS.append(["Cash, investments, less debt, minorities, pensions", "", "", bn(ADJ), f"{ADJ / SH * 100:.0f}%", yen(ADJ / SHARES * 1000)])
rowsS.append(["Equity value", "", "", bn(SH), "100%", yen(BASE_VALUE)])
A(cols(datatable(["Part", "FY2027E EBITA, ¥bn*", "Multiple", "Value, ¥bn", "Share", "Per share"], rowsS,
                 num_cols={1, 2, 3, 4, 5}, total_row_idx=len(rowsS) - 1), [38, 14, 10, 13, 10, 15]))
A(caption("*My estimates; brackets are negative. Multiples are EV to FY2027E adjusted EBITA, set against peers' trailing EV/EBIT (table below): grid median 24.5x, "
          "less a year of growth, for Hitachi Energy; Fujitsu 17.4x and NEC 19.1x for IT; Mitsubishi Electric 19.1x for Connective "
          "Industries, which carries a weak China elevator business; Alstom 10.3x for Mobility. Corporate costs are capitalised at 15x."))
A('</div>')
A('<div class="keeptogether">')
A(section("Scenarios: three cases, twelve months out"))
A(cols(datatable(
    ["Case", "What happens", "HE FY2027 EBITA", "HE multiple", "Others", "Value", "Change", "Weight"],
    [
        ["Bear", "Orders slow; growth 8%, margin flat at 14.8%; grid names de-rate", f"¥{HEE[0]:.0f}bn", f"{SCEN[0][3]}x", "2 turns lower", yen(bear), chg(bear), "25%"],
        ["Base", "Growth 12%, margin 15.5%", f"¥{HEE[1]:.0f}bn", f"{SCEN[1][3]}x", "as above", yen(base), chg(base), "50%"],
        ["Bull", "Growth 15%, margin 16.5%; the plan keeps rising", f"¥{HEE[2]:.0f}bn", f"{SCEN[2][3]}x", "2 turns higher", yen(bull), chg(bull), "25%"],
        ["Weighted", "25 / 50 / 25", "", "", "", f"about {yen(round(WEIGHTED, -1))}", chg(WEIGHTED), ""],
    ],
    num_cols={2, 3, 5, 6, 7}, total_row_idx=3,
), [9, 33, 11, 9, 11, 10, 9, 8]))
A(caption("Hitachi Energy (HE) starts from Hitachi's FY2026 forecast of US$23.65bn at ¥160. The rest of Hitachi keeps my FY2027E EBITA; only its "
          "multiples move. The bear multiple for Hitachi Energy is below where the market already values it; the bull multiple is still "
          "below Siemens Energy (27.9x) and Eaton (31.8x) on trailing EBIT."))
A('</div>')
A('<div class="keeptogether">')
A(section("Sensitivity: Hitachi Energy FY2027 adjusted EBITA against its multiple"))
A('<div class="chartsrow"><div class="col left">')
grid = [[value(e, m) for m in SENS_MULT] for e in SENS_HE]
A(datatable(
    ["HE EBITA"] + [f"{m}x" for m in SENS_MULT],
    [[f"¥{e:.0f}bn"] + [(f"<b>{yen(v)}</b>" if (i == 1 and j == 1) else yen(v)) for j, v in enumerate(row)]
     for i, (e, row) in enumerate(zip(SENS_HE, grid))],
    num_cols={1, 2, 3},
))
A('</div><div class="col">')
n_above = sum(v > PRICE for r in grid for v in r)
n_15 = sum(v >= PRICE * 1.15 for r in grid for v in r)
A(para(f"With the rest of Hitachi at my base, {n_above} of the nine cells sit above the price, but only {n_15} sit 15% or more above it, "
       "and both need 24 times. Under my rule, a long needs the base value 15% or more above the price and a short needs it 25% or more "
       f"below. At {(BASE_VALUE / PRICE - 1) * 100:.0f}% above, my call is no call."))
A('</div></div>')
A('</div>')

A('<div class="keeptogether">')
A(section("Peer landscape"))
A(cols(datatable(
    ["Company", "Ticker", "Forward P/E", "EV/EBIT", "What they make"],
    [[c, t, f"{p:.1f}x", f"{e:.1f}x", w] for c, t, p, e, w, g in PEERS],
    num_cols={2, 3},
), [18, 13, 11, 10, 48]))
A(caption("Forward P/E and trailing EV/EBIT from stockanalysis.com, retrieved 22 October 2026. Grid equipment median (Siemens Energy, ABB, "
          "Schneider Electric, Eaton, Prysmian): 23.0x forward P/E, 24.5x EV/EBIT. GE Vernova is left out: its trailing EV/EBIT of 87x "
          "reflects earnings still recovering. Multiples are used only to set the ranges; no view on the peers' shares is expressed."))
A('</div>')

A('<div class="keeptogether">')
A(section("Catalysts"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["28 October 2026 (confirmed)", "Q2 FY2026 results; webcast 17:00 to 18:00 JST", "Hitachi Energy backlog against 2.5 to 3 times revenue; margin against 14.8%; any change to the FY2026 forecast"],
        ["Early 2027 (date not announced)", "Q3 FY2026 results", "Orders against revenue as the large HVDC awards are booked"],
        ["Late April 2027 (date not announced)", "FY2026 results and the FY2027 forecast", "Whether the FY2027 Hitachi Energy figure moves above the US$26bn target"],
        ["Through FY2026", "¥550bn of buybacks (¥147.9bn done in Q1); home appliance deconsolidation", "Share count; Connective Industries mix"],
        ["2028 and 2029", "South Boston and Mississippi transformer plants", "On time, and only against signed orders"],
    ],
))
A('</div>')

A(section("Risks: what would hurt the view"))
A(para("<strong>Orders slow as factories open.</strong> The claim breaks if the backlog falls below 2.5 times revenue at two quarter ends "
       "in a row, or a year's orders fall below revenue. HVDC awards are lumpy, and the June quarter's 2.16 will not repeat every quarter. "
       "A falling ratio would cut the multiple and the margin path. That is most of the bear case."))
A(para("<strong>Execution on large projects.</strong> Schierenbeck said HVDC links normally take three to four years to execute, and they "
       "are priced years ahead. A cost overrun on one large European link would show up quickly in a 15% margin."))
A(para(f"<strong>The yen.</strong> Hitachi says each yen of weakness against the dollar adds ¥11.0bn of revenue and ¥1.2bn of adjusted "
       f"EBITA over the last three quarters of fiscal 2026. On my fiscal 2027 Hitachi Energy estimate alone the effect is about "
       f"¥{HE_EBITA27_USD:.1f}bn of adjusted EBITA per yen."))
A(para("<strong>The rest of the group.</strong> Digital Systems and Services faces price pressure overseas. Connective Industries depends "
       "partly on semiconductor equipment and Chinese building demand, and the home appliance business is due to be deconsolidated within "
       "fiscal 2026."))
A(para("<strong>The Middle East.</strong> Hitachi says the situation cost it about ¥16.0bn of revenue and ¥7.0bn of adjusted EBITA in the "
       "June quarter, and its forecast allows for ¥10.0bn more of each for the rest of the year."))
A(para("<strong>Capacity timing.</strong> Hitachi expects South Boston, Virginia to operate by 2028 and Mississippi to start production in "
       "2029. A slip delays revenue the plan needs, though it would also keep the queue long."))

A('<div class="keeptogether">')
A(section("What would change my mind"))
A(para(f"<strong>Into a long:</strong> a price below about ¥{round(REVISIT_LONG, -2):,.0f}, where my base value would sit 15% above it on "
       "unchanged estimates, or Hitachi raising its fiscal 2027 target for Hitachi Energy above US$28bn of revenue at a 16% margin. "
       f"<strong>Towards a short:</strong> a price above about ¥{round(REVISIT_SHORT, -1):,.0f}, where my base value would sit 25% below it."))
A(para(f"<strong>The view is wrong if</strong> {WRONG_IF[0].lower() + WRONG_IF[1:]}"))
A('</div>')

A(section("Conclusion"))
A(para("The October piece argued that Hitachi Energy is building just fast enough to keep its queue, not to clear it. Hitachi's figures "
       f"say so: US$63.6bn of backlog, {RATIO_JUN26:.2f} times a year of revenue, a plan to hold the ratio at 2.5 to 3 times through 2030, "
       "and orders well ahead of revenue. Nothing I found says the piece was wrong. One simplification: the piece said Hitachi Energy "
       "\"is spending more than $9 billion\", but about US$3bn of it was spent from 2020 to 2023; this does not affect the claim. But "
       f"the queue that makes Hitachi Energy's revenue so visible also caps it, and Hitachi Energy is under half of Hitachi. {my_call}: "
       f"{CALL['direction']}, {conv} conviction; base value {yen(BASE_VALUE)}, range {yen(bear)} to {yen(bull)}."))

A('<div class="keeptogether">')
A(section("Appendix: forecast assumptions"))
A(cols(datatable(
    ["Assumption", "FY2026", "FY2027E", "Basis"],
    [
        ["Hitachi Energy revenue growth (US$)", f"{HE_GROWTH_26 * 100:.0f}% (forecast)", f"{HE_G27 * 100:.0f}%", "Plan pace to FY2030; FY2027 target about US$26bn"],
        ["Hitachi Energy adjusted EBITA margin", "14.8% (forecast)", f"{HE_M27 * 100:.1f}%", "Target 15%+; FY2030 range 16 to 20%"],
        ["Yen per US$", "160 (Hitachi)", f"{FX27:.0f}", "Held at Hitachi's own assumption"],
        ["Other parts, adjusted EBITA growth", "Hitachi forecast", "DSS 6%, CI 5%, Mobility 10%", "Below Hitachi Energy; DSS revenue grows 6% in FY2026 on Hitachi's basis excluding FX and one-offs"],
        ["Bridge, ¥bn", f"{ADJ:,.0f}", "", "30 June 2026, at book, held flat"],
        ["Shares, m", f"{SHARES:,.1f}", "", "Issued less treasury, 30 June 2026; no further buybacks"],
    ],
), [28, 18, 18, 36]))
A(caption(f"Full workings, with live formulas, in the accompanying model, {DATE}_{COMPANY}_Model.xlsx."))
A('</div>')

A(section("Sources"))
A('<p class="sourceline">Hitachi, Outline of Consolidated Financial Results for the First Quarter Ended June 30, 2026, Consolidated '
  'Financial Results and Supplemental Material, 29 July 2026, for segment results, the raised fiscal 2026 forecast, Hitachi Energy in US '
  'dollars, orders, backlog, the balance sheet, shares, FX assumptions and buybacks. Hitachi, Outline of Consolidated Financial Results '
  'for Fiscal 2025, 27 April 2026, for fiscal 2025 results, the April forecast and Hitachi Energy orders and backlog. Hitachi results '
  'presentations of 28 April 2025, 31 July 2025 (page 11, June 2025 backlog), 30 October 2025 and 29 January 2026 for earlier backlog and forecasts. Hitachi Investor '
  'Day 2026, Energy Business Strategy and Q&amp;A summary, 10 June 2026, for the backlog ratio, the investment programme, the fiscal 2027 '
  'and 2030 targets and the remarks quoted from Hitachi\'s translated Q&amp;A summary. Hitachi investor relations library for the 28 October 2026 results date. Share prices from '
  'Yahoo Finance (6501.T); consensus EPS and average target (S&amp;P Global data, targets updated 17 September 2026) and peer '
  'multiples from stockanalysis.com; all retrieved 22 October 2026. Estimates '
  'for fiscal 2027 are the author\'s own.</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model independently. It is not a product of any bank or broker. '
  'It tests a claim from my journal piece of 22 October 2026, '
  '<a href="https://thephysicallayer.fyi/journal/hitachi-energy-plans-the-queue/">thephysicallayer.fyi/journal/hitachi-energy-plans-the-queue</a>; '
  'all notes and their track record are at <a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>. '
  'Figures from company filings are labelled as such; derived figures are marked; the forecasts and view are my own estimates and my '
  'own view. I hold no position in Hitachi. Personal research, not investment advice.</p>')
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
