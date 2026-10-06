# -*- coding: utf-8 -*-
"""Nebius (Nasdaq: NBIS) initiation note, 6 Oct 2026, in the house research-note style.

Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build_note.py
Source of truth for every figure: src/content/calls/nebius.md (the published pitch).
"""
import os
import sys

TEMPLATE = "/Users/tommylau/Desktop/jobs/research coverage/_note_template"
sys.path.insert(0, TEMPLATE)
from common import page_shell, section, para, datatable, caption, statbox  # noqa: E402
from weasyprint import HTML  # noqa: E402
import nebius_data as D  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(HERE, "charts")
PUB = os.path.abspath(os.path.join(HERE, "..", "..", "public", "research"))
PDF = os.path.join(PUB, "2026-10-06_Nebius_Initiation.pdf")
HTML_OUT = os.path.join(HERE, "nebius_note.html")

FOOTER_TITLE = "Nebius (Nasdaq: NBIS)"
DATE = "6 October 2026"

b = D.share_bridge()
scen, wv, wc = D.scenarios()
sens = D.sensitivity()
dep, ue = D.unit_econ()


def img(name):
    return f'<img class="chart" src="file://{os.path.join(CH, name)}">'


def charts_row(left, right):
    return f'<div class="chartsrow keeptogether"><div class="col left">{img(left)}</div><div class="col">{img(right)}</div></div>'


EXTRA_CSS = """
<style>
table.ratingbanner td.rating { width: 24%; }
table.datatable.compact td, table.datatable.compact th { font-size: 8.2pt; padding: 3px 5px; }
table.datatable.compact th { padding: 4px 5px; }
td.flag { color: #595959; }
.callbox { border-left: 2.5pt solid #1F3864; padding: 2px 0 2px 8px; margin: 4px 0 8px 0; }
h3.sub { font-size: 9.6pt; font-weight: 700; color: #1F3864; margin: 7px 0 3px 0; break-after: avoid; }
p.body a, p.aboutnote a, p.sourceline a { color: #2E5395; text-decoration: none; }
</style>
"""

P = []
A = P.append

# ---------------- page 1 ----------------
A('<h1 class="doctitle">Nebius Group N.V.</h1>')
A('<p class="docsubtitle">Nasdaq: NBIS | AI computing centres built and rented out to Microsoft, Meta and AI labs | Netherlands</p>')
A('<p class="docmeta">Tommy Lau | 6 October 2026 | Initiation | Independent research</p>')
A("""<table class="ratingbanner"><tr>
<td class="rating">INITIATE AT<br/>NO CALL</td>
<td class="field"><b>Target price:</b> none</td>
<td class="field"><b>Last price:</b> US$232.57</td>
<td class="field"><b>Re-look:</b> below ~US$185</td>
</tr></table>""")

A('<div class="clearfix">')
A('<div class="sidebar">')
A(statbox([
    ("Call", "No call, no position at this price. Medium conviction"),
    ("Reference price", "US$232.57, Nasdaq close 5 Oct 2026"),
    ("Horizon", "12 months, to October 2027"),
    ("Month-end closes, Nov 2024 to Sep 2026", "US$21.11 (Mar 25) to US$276.17 (Jun 26)"),
    ("Basic shares, 30 Jun 2026", "271.9m (238.4m Class A, 33.5m Class B)"),
    ("Shares, if-converted (my count)", f"~{b['total']:.1f}m"),
    ("Equity value, if-converted", "~US$86bn"),
    ("Pro forma cash / debt staying as debt", "~US$14.5bn / ~US$6.5bn"),
    ("Enterprise value", "~US$78bn"),
    ("EV / 2027 EBITDA, consensus revenue at 50%", "~12.7x"),
    ("EV / 2027 consensus revenue", "6.3x"),
    ("Remaining performance obligations", "US$37.49bn, 30 Jun 2026"),
    ("Top three customers, Q2 2026 revenue", "59% (24%, 21%, 14%)"),
    ("Short interest, 15 Sep 2026", "46.78m shares, ~19.8% of float"),
], "Stock data"))
A('</div>')
A('<div class="maincol">')
A(para("Nebius builds AI computing centres and rents them out to companies such as Microsoft and Meta. It earns money only "
       "once the power is on and the chips are running, and its new contracts pay roughly twice what the existing fleet "
       "earns per megawatt. Both engines are real. At US$232.57 the shares already assume Nebius switches on most of its "
       "contracted power quickly, at the new, higher prices."))
A(para("<strong class='lead'>We initiate at NO CALL, with medium conviction.</strong> There is no target price. My base case "
       "for October 2027 is worth about US$229, 1% below the price; the probability-weighted value is about US$242, 4% "
       "above it; the bear case is US$78, a 66% fall. That is a stock where the market already agrees with the thesis."))
A('<div class="callbox">')
A(para("<strong class='lead'>What turns this into a call.</strong> A price below about US$185, where the base case offers about a "
       "quarter of upside. Or fourth quarter 2026 results, early in 2027, showing at least 800 MW connected, year-end "
       "annualised revenue inside the US$7 to 9bn guide and new deals still at US$20m per MW or more."))
A('</div>')
A(caption("Share counts, cash, notes and warrants from Nebius's interim statements to 30 June 2026 and its August 2026 "
          "releases. If-converted count, equity value, pro forma cash and EV are my own; see CapStructure in the model. "
          "Prices, consensus and short interest from Yahoo Finance, retrieved 6 Oct 2026."))
A('</div></div>')

A('<div class="fullwidth">')
A(section("Key financials", first=True))
rev = D.REVENUE
cap = D.CAPEX
A(datatable(
    ["US$m unless stated", "Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "2026 g / c", "2027 c"],
    [
        ["Revenue"] + [f"{v:,.1f}" for v in rev] + ["3,340 c", "12,300 c"],
        ["Annualised run-rate (ARR), US$bn"] + [f"{v:.2f}" for v in D.ARR] + ["7.0 to 9.0 g", "n.a."],
        ["Capital spending", "544.0", "510.6", "955.5", "~2,100", "~2,500", "~5,700", "20,000 to 25,000 g", "n.a."],
        ["Capital spending per US$1 of revenue (x)"] + [f"{c / r:.1f}" for c, r in zip(cap, rev)] + ["n.a.", "n.a."],
        ["AI cloud adj. EBITDA margin (%)", "n.d.", "n.d.", "19.0", "24.0", "45.0", "49.7", "n.a.", "50.0 e"],
        ["EBITDA at a 50% margin on consensus", "", "", "", "", "", "", "", "~6,200 e"],
        ["Connected power, end of period (MW)", "", "", "", "", "", "", "800 to 1,000 g", ""],
    ],
    num_cols={1, 2, 3, 4, 5, 6, 7, 8}, wide_first=True,
).replace('class="datatable wide-first"', 'class="datatable wide-first compact"'))
A(caption("g = Nebius guidance, Q2 2026 shareholder letter, 12 Aug 2026. c = Yahoo Finance consensus, 6 Oct 2026. e = my "
          "assumption, applied to consensus revenue; it is not a forecast of my own. ~ = approximate, as reported. Before "
          "2026, ARR covers the core AI infrastructure business. Q1 2025 capital spending is the first half less the second "
          "quarter. n.d. = not disclosed on a comparable basis. Source: Nebius shareholder letters and Form 6-K results."))
A('</div>')

# ---------------- page 2 ----------------
A('<div class="fullwidth">')
A(section("To hit even the bottom of its guide, Nebius must more than double its run-rate in six months"))
A(charts_row("nbis_arr.png", "nbis_build.png"))
A(caption("Left: ARR at quarter end against the US$7 to 9bn year-end 2026 guide. Right: quarterly revenue against capital "
          "spending; in Q2 2026 Nebius spent about ten dollars building for every dollar it earned. Source: Nebius "
          "shareholder letters, Q2 2025 to Q2 2026; Q4 2025 to Q2 2026 capital spending approximate, as reported."))

A(section("The thesis: paid for power that is switched on"))
A(para("Nebius closed at US$232.57 on 5 October 2026, more than ten times its price when trading resumed in October 2024. In that time it went "
       "from a leftover of Yandex with one data centre in Finland to a supplier of AI capacity to Microsoft and Meta. In my "
       "30 September journal piece I argued that Nebius is paid for megawatts that are switched on, not megawatts it has "
       "signed. This note asks a narrower question. If that is how Nebius gets paid, what is a share worth, and does the "
       "price already know?"))
A(para("Think of an industrial kitchen. Nebius has booked the gas supply for five kitchens and expects to light about one this "
       "year. Its customers pay only for meals from lit ovens. Lighting the ovens is not the moment the money starts, though. "
       "After the power is connected, Nebius still has to build the network, assemble the clusters, install its software and "
       "bring the customer on. Its chief infrastructure officer described that sequence on the August results call, and said "
       "the stretch after connection takes several months."))
A(para("That changes what the number I watch actually measures. Nebius defines connected power as power wired into fully built "
       "and equipped data centres. Active power is what is feeding running chips and earning money. Connected comes first, "
       "and active follows months later. So the business has two engines. Speed decides how many megawatts bill. Price per "
       "megawatt is roughly doubling as new contracts replace the old fleet. Both have to keep working for the shares to rise "
       "from here."))

A(section("The reconciliation: US$20 to 25m per MW, yet only US$7 to 9bn of run-rate"))
A(para("A gap sat open in my notes from September. Nebius says its large second quarter deals carry annual contract value of "
       "US$20 to 25m per megawatt. Multiply that by 800 MW and you get US$16 to 20bn a year. Yet Nebius guides to annualised "
       "revenue of only US$7 to 9bn at the end of 2026. Three things in Nebius's own words close the gap."))
A(datatable(
    ["Step", "Low", "High", "Working"],
    [
        ["Connected power, end 2026 (bottom of guide)", "800 MW", "800 MW", "Guide is 800 MW to 1 GW"],
        ["New-deal contract value per MW", "US$20m", "US$25m", "Q2 2026 large deals"],
        ["Naive revenue if every connected MW billed at new prices", "US$16bn", "US$20bn", "800 x US$20 to 25m"],
        ["Year-end 2026 ARR guide", "US$7bn", "US$9bn", "ARR is December revenue x 12"],
        ["Fleet base contract value per MW", "US$12m", "US$12m", "Most new deals earn mainly in 2027"],
        ["MW billing in December implied by the guide", "~583 MW", "750 MW", "US$7 to 9bn / US$12m"],
        ["Connected but not yet billing", "~217 MW", "50 MW", "The lag from connected to active"],
        ["Cross-check, end 2025: ARR per active MW", "US$7.4m", "", "US$1.25bn / ~170 MW active"],
    ],
    num_cols={1, 2},
))
A(caption("Source: Nebius Q2 2026 shareholder letter, 12 Aug 2026, for the run-rate guide and contract value per MW; Q1 2026 "
          "letter, 13 May 2026, for the connected power guide and the definitions of connected and active power. Working is mine; see ARR_Recon in the model."))
A(para("First, annualised revenue is December's revenue multiplied by twelve, so it captures only what is billing that month. "
       "Second, the US$20 to 25m applies to the new deals, against an approximate base of US$12m for the 2026 fleet. Third, "
       "Nebius says most of those new deals were signed against capacity arriving in late 2026 and will mainly earn in 2027. "
       "At US$12m per megawatt, US$7 to 9bn of run-rate means about 580 to 750 MW billing in December. That sits below 800 MW "
       "connected, which is exactly what a lag of several months looks like. At the end of 2025, US$1.25bn of run-rate sat on "
       "about 170 MW active, roughly US$7.4m each, from older and cheaper contracts; the 2026 base of about US$12m reflects "
       "newer contracts replacing them."))

A(section("Where I was wrong in September"))
A(para("My 30 September journal piece defined connected power as power wired up and feeding running chips, and said customers "
       "pay for it. That was wrong. What I described is Nebius's active power. Connected power is the building, finished and "
       "equipped; active power is the chips running and billing, and it trails connection by several months. "
       "What changed my view was the gap above: "
       "Nebius's contract value per megawatt and its run-rate guide do not fit together unless much of its connected power is "
       "not yet billing, and its own definitions confirm that."))
A(para("The edge the claim describes is still speed, but the right test is active power, not connected. Nebius does not report "
       "active megawatts each quarter, so I read them through run-rate divided by the fleet price per megawatt. Hitting 800 MW "
       "connected by the end of 2026 is necessary. It is not yet revenue. The piece and the claim stay exactly as published, "
       "so the record shows the mistake."))

A(section("Variant perception: what the market prices in, and where I differ"))
A(para("On my count, Nebius's equity is worth about US$86bn at US$232.57, if every convertible note that is currently worth "
       "converting turns into shares. That count uses about 370m shares, including options, restricted stock and Nvidia's "
       "pre-funded warrants. After the August note issue I estimate cash of about US$14.5bn before third quarter spending, "
       "against about US$6.5bn of notes and loans that would stay as debt. That gives an enterprise value of about US$78bn."))
A(para("Against that, consensus expects revenue of US$3.34bn in 2026 and US$12.3bn in 2027. At a 50% margin, 2027 EBITDA would "
       "be about US$6.15bn. The enterprise value is about 12.7 times that, and 6.3 times 2027 revenue. CoreWeave, the closest "
       "listed rival, trades at about 3.6 times its 2027 revenue on the same source, and Oracle at about 4.3 times its next "
       "year's revenue. So the market already gives Nebius a premium, and it rests on one belief: that Nebius turns "
       "contracted power into earning power faster and at better prices than anyone else."))
A(para("That is my September claim. The difference is that I think the price now pays for it in advance. Consensus revenue "
       "of US$12.3bn for 2027 already assumes the year-end run-rate roughly doubles again through 2027. It assumes Meta's "
       "second contract comes online on time in early 2027, and that new deals keep pricing at US$20m a megawatt or more."))
A(para("<strong class='lead'>Where I differ is on what could break.</strong> The bull story treats five gigawatts as a pipeline. "
       "I treat it as a promise to spend. At my estimate of about US$30m of capital per megawatt, five gigawatts is roughly "
       "US$150bn of building, against an if-converted equity value of US$86bn. Customers prepay part of it, but the rest needs debt and new "
       "shares. And if Meta builds a business selling its own spare capacity, as Bloomberg reported on 1 July, the price per "
       "megawatt is the first thing to give."))
A('</div>')

# ---------------- unit economics ----------------
A('<div class="fullwidth">')
A(section("Unit economics: new contracts pay twice the old, and that is the whole case"))
A(charts_row("nbis_acv.png", "nbis_margin.png"))
A(caption("Left: annual contract value per MW, approximate, revenue recognition basis excluding prepayments; the Q2 bar is the "
          "midpoint of US$20 to 25m and the Q3 figure a floor. Source: Nebius Q2 2026 letter, 'ACV per MW is stepping up'. "
          "Right: AI cloud adjusted EBITDA margin. Source: Nebius shareholder letters, Q3 2025 to Q2 2026."))
A(para("These are my estimates, built on Nebius's figures. I take the cost of a megawatt at about US$30m, from capital spending "
       "of US$20 to 25bn in 2026 against roughly 600 to 800 MW of new connected power, some of which is spending for 2027. I "
       "assume 80% of that is chips and network, worn out over five years, and the rest is building, worn out over twenty. "
       "That is US$5.1m of wear a year. Margin before those costs is 50%, close to the 49.7% the AI cloud business reported."))
A(datatable(
    ["Contract value per MW", "EBITDA per MW", "Profit per MW after wear", "Pre-tax return on US$30m"],
    [[lbl, f"US${e:.1f}m", f"US${p:.1f}m", f"{r * 100:.0f}%"] for lbl, acv, e, p, r in ue],
    num_cols={1, 2, 3},
))
A(caption("My estimates. Wear: US$24m of chips and network over 5 years plus US$6m of building over 20 years. See UnitEcon in the model."))
A(para("This table is the whole case in three lines. At the old price, a megawatt barely earns back its cost before the chips "
       "age out. At the new price, it earns a good return, and prepayments that fund half the building raise the return on "
       "Nebius's own money further. The shares are a bet that the new price lasts through the whole build."))
A('</div>')

# ---------------- valuation ----------------
A('<div class="fullwidth">')
A(section("Valuation: three cases, twelve months out"))
A(para("By October 2027 the market will be pricing 2028. I value 2028 EBITDA at a multiple, then subtract the net debt I expect "
       "by the end of 2027, after another year of heavy building. I assume some new shares are sold along the way. The base "
       "multiple of 11 times sits between CoreWeave and where Nebius trades today."))
A(datatable(
    ["Case", "What happens", "2028 revenue", "Margin", "Multiple", "Net debt", "Shares", "Value", "Change"],
    [[n, w, f"US${rv:.0f}bn", f"{m * 100:.0f}%", f"{x:.0f}x", f"US${nd:.0f}bn", f"{sh:.0f}m", f"US${v:.0f}",
      (f"-{abs(c) * 100:.0f}%" if c < 0 else f"+{c * 100:.0f}%")]
     for n, w, rv, m, x, nd, sh, wt, e, v, c in scen]
    + [["Weighted", "25% bear, 50% base, 25% bull", "", "", "", "", "", f"US${wv:.0f}", f"+{wc * 100:.0f}%"]],
    num_cols={2, 3, 4, 5, 6, 7, 8}, total_row_idx=3,
).replace('class="datatable"', 'class="datatable compact"', 1))
A(caption("Value = (2028 revenue x margin x multiple, less end-2027 net debt) / shares. Change against US$232.57. All my "
          "estimates; see Scenarios in the model."))

A('<div class="clearfix keeptogether">')
A('<div style="float:left; width:47%;">')
A('<h3 class="sub">Sensitivity: value per share, US$</h3>')
A(datatable(
    ["2028 EBITDA", "9x", "11x", "13x"],
    [[f"US${e}bn"] + [f"US${v:.0f}" for v in row] for e, row in zip(D.SENS_EBITDA, sens)],
    num_cols={1, 2, 3},
))
A(caption("Net debt US$15bn and 388m shares throughout. The range is wide and centred close to today's price."))
A('</div>')
A('<div style="float:right; width:50%;">')
A('<h3 class="sub">EV build at US$232.57</h3>')
A(datatable(
    ["Item", "US$bn"],
    [
        ["If-converted shares, ~369.6m x US$232.57", "~86.0"],
        ["Less: pro forma cash before Q3 spending", "(14.5)"],
        ["Plus: notes and loans staying as debt", "6.5"],
        ["Enterprise value", "~78.0"],
        ["EV / 2027 EBITDA (~US$6.15bn)", "12.7x"],
        ["EV / 2027 revenue (US$12.3bn)", "6.3x"],
    ],
    num_cols={1}, total_row_idx=3,
))
A('</div></div>')

A(charts_row("nbis_valuation.png", "nbis_price.png"))
A(caption("Left: valuation cross-check against the price (grey) and the US$185 re-look level (red); my estimates. Right: month-end "
          "closes, Nov 2024 to Sep 2026, and the 5 Oct 2026 close. The shares fell 17% on 1 July 2026, the day Bloomberg "
          "reported that Meta plans to sell its own spare computing capacity. Source: Yahoo Finance, retrieved 6 Oct 2026."))
A('</div>')

# ---------------- capital structure ----------------
A('<div class="fullwidth">')
A(section("Capital structure: six notes count as shares, two stay as debt"))
conv_rows = []
for name, p, c, cp, mat, itm, sh in b["conv_rows"]:
    conv_rows.append([mat, f"{p:,.2f}", (f"{c * 100:.3f}".rstrip("0").rstrip(".") + "%"), f"{cp:.2f}", "Yes" if itm else "No", f"{sh:.1f}",
                      "Shares" if itm else "Debt"])
conv_rows.append(["Secured facility, SOFR + 2.50%, to Oct 2030", "~775", "", "", "", "", "Debt"])
A(datatable(
    ["Instrument (maturity)", "Principal, US$m", "Coupon", "Conversion price, US$", "In the money", "Shares if converted, m", "Treated as"],
    conv_rows, num_cols={1, 2, 3, 5},
).replace('class="datatable"', 'class="datatable compact"', 1))
A(caption("Jun 2029 and Jun 2031 notes are what remains after US$800m was exchanged for ~15.8m shares around 24 Aug 2026. The "
          "Feb 2030 and Feb 2034 notes were issued in August 2026. Source: Nebius interim statements to 30 Jun 2026 and releases "
          "of 10 Jul, 19 Aug and 24 Aug 2026."))
A('<div class="clearfix">')
A('<div style="float:left; width:50%;">')
A(datatable(
    ["If-converted share bridge", "Shares, m"],
    [
        ["Basic shares, 30 Jun 2026", "271.9"],
        ["Nvidia pre-funded warrants", "21.1"],
        ["Issued ~24 Aug for 2029/2031 notes", "~15.8"],
        ["Options, treasury method", f"{b['tsm_opts']:.1f}"],
        ["Restricted stock units", "6.2"],
        ["Six in-the-money convertible notes", f"{b['itm_sh']:.1f}"],
        ["If-converted shares", f"~{b['total']:.1f}"],
    ],
    num_cols={1}, total_row_idx=6,
).replace('class="datatable"', 'class="datatable compact"', 1))
A('</div>')
A('<div style="float:right; width:47%;">')
A(para("The funding picture matters as much as the count. Nebius raised about US$5.75bn of convertible notes in August, sold "
       "12.7m shares at an average of US$223.60 through its at-the-market programme in May and June for about US$2.81bn net, "
       "and took US$2bn from Nvidia in March. Deferred revenue, where customer prepayments sit, was about US$6.0bn at 30 June "
       "(US$979.4m current, US$4,995.8m non-current), against remaining performance obligations of US$37.49bn. Second half "
       "capital spending implied by the guide is US$12 to 17bn."))
A('</div></div>')
A('</div>')

# ---------------- peers ----------------
A('<div class="fullwidth">')
A(section("Peer landscape"))
A(datatable(
    ["Company", "Ticker", "Revenue multiple", "Basis", "What they do"],
    [
        ["Nebius", "Nasdaq: NBIS", "6.3x", "EV / 2027 revenue, my EV", "Builds and runs AI computing centres, rents the capacity"],
        ["CoreWeave", "Nasdaq: CRWV", "3.6x", "EV / 2027 revenue", "AI cloud, the closest listed rival"],
        ["Oracle", "NYSE: ORCL", "4.3x", "Next financial year revenue", "Software and cloud, building AI capacity"],
        ["IREN", "Nasdaq: IREN", "2.4x", "Next financial year revenue", "Powered data centre sites, AI cloud"],
    ],
    num_cols={2},
))
A(caption("Multiples from Yahoo Finance, retrieved 6 Oct 2026, except Nebius, which is on my enterprise value. Bases and "
          "financial years differ, so the table frames the premium rather than setting a value."))
A('</div>')

# ---------------- catalysts ----------------
A('<div class="fullwidth">')
A(section("Catalysts: the evidence is dated"))
A(datatable(
    ["When", "Event", "What I watch"],
    [
        ["~10 to 11 Nov 2026, not confirmed by Nebius", "Q3 2026 results",
         "Connected MW against the pace needed for 800 MW; prepayments in new deals; run-rate progress from US$3.0bn"],
        ["Early 2027", "Q4 2026 results",
         "At least 800 MW connected; year-end run-rate inside US$7 to 9bn; new deals at US$20m per MW or more"],
        ["Early 2027", "Capacity for Meta's second agreement (announced 16 Mar 2026) due",
         "On time, as consensus 2027 revenue assumes"],
        ["Any time", "Meta selling its own spare capacity (Bloomberg, 1 Jul 2026)",
         "Pricing of new deals per MW"],
        ["Any time", "Further share or note issues", "Price and size against second half capital spending of US$12 to 17bn"],
    ],
))
A('</div>')

# ---------------- risks ----------------
A('<div class="fullwidth">')
A(section("Risks"))
A(para("<strong class='lead'>Connection slips.</strong> Nebius guides to 800 MW to 1 GW connected by the end of 2026. Missing the "
       "bottom of that range would mean its edge is not speed, which breaks both the claim and the call."))
A(para("<strong class='lead'>The price per megawatt falls.</strong> The return table shows how much rests on new deals pricing "
       "at US$20m or more. Meta selling spare capacity, or hyperscalers catching up on their own building, would push that "
       "down. The rise of 17 to 21% in on-demand GPU prices reported from 1 October points the other way for now, though I "
       "have not confirmed it on a Nebius page."))
A(para("<strong class='lead'>Funding.</strong> Second half capital spending implied by the guide is US$12 to 17bn. More new "
       "shares are likely, and at a lower price they would cost holders more."))
A(para("<strong class='lead'>Customer concentration.</strong> Three unnamed customers made up 59% of second quarter revenue, at "
       "24, 21 and 14%. A pause by one of them changes the year."))
A(para("<strong class='lead'>Ageing chips.</strong> A switched-on hall of older chips earns less each year. Nebius must keep "
       "replacing them, which is why I depreciate chips over five years rather than longer."))

A(section("What would change our mind"))
A(datatable(
    ["Direction", "Trigger"],
    [
        ["To LONG", "Either is enough. A price below about US$185, where the base case offers about a quarter of upside. Or "
                    "Q4 2026 results, early 2027, showing at least 800 MW connected, year-end run-rate inside US$7 to 9bn and "
                    "new deals still at US$20m per MW or more. That would move weight from the base case to the bull case."],
        ["To SHORT", "Connection behind the pace in the Q3 results, expected around 10 or 11 November though Nebius has not "
                     "confirmed the date, together with falling prepayments. About a fifth of the free float was already "
                     "sold short in mid September, so a short would join a crowded trade."],
        ["The call is wrong if", "Connected power at the end of 2026 comes in below the 800 MW bottom of Nebius's own range, or "
                                 "year-end run-rate lands below US$7bn, or prepayments appear in fewer than half of new deals."],
    ],
))

A(section("Conclusion"))
A(para("The September claim holds up. Nebius earns money only from capacity that is running, its new contracts pay roughly "
       "twice the old ones, and customers prepay to hold their place. The gap between US$20 to 25m per megawatt and a US$7 to "
       "9bn run-rate is explained by the lag between connecting power and billing for it. But the market has read the same "
       "letter. At about 12.7 times 2027 EBITDA, the price assumes fast connection and lasting new-deal pricing. My call is "
       "no call at US$232.57, held with medium conviction. I would go long below about US$185, or at today's price once the "
       "fourth quarter results show the power switching on as promised."))
A('</div>')

# ---------------- sources and about ----------------
A('<div class="fullwidth">')
A(section("Sources"))
for s in [
    "Nebius quarterly shareholder letters and results on Form 6-K, Q2 2025 to Q2 2026: revenue, annualised run-rate, margins, "
    "capital spending, power and customer concentration.",
    "Nebius Q2 2026 shareholder letter, 12 August 2026: run-rate guide, contract value per megawatt and prepayments. Nebius Q1 "
    "2026 shareholder letter, 13 May 2026: definitions of connected and active power, and the 800 MW to 1 GW connected guide. "
    "Nebius Q2 2026 earnings call, 12 August 2026: capital spending guide, connected guide as reaffirmed, deployment sequence.",
    "Nebius interim financial statements to 30 June 2026: shares, cash, restricted cash, deferred revenue, remaining "
    "performance obligations, notes, options, restricted stock units and warrants. Nebius releases of 19 and 24 August 2026 "
    "on the convertible notes, and of 10 July 2026 on the secured loan.",
    "Nebius Form 6-K on the Microsoft agreement, 8 September 2025, and announcement of the second Meta agreement, 16 March 2026. "
    "Bloomberg News on Meta's cloud plans, 1 July 2026.",
    "Consensus revenue, peer multiples, short interest and share prices: Yahoo Finance, retrieved 6 October 2026. On-demand GPU "
    "price changes as reported by Spheron and Coin Republic, September 2026.",
    "Unit economics, pro forma cash, net debt, share count, 2028 scenarios and the sensitivity grid are my own estimates.",
]:
    A(f'<p class="sourceline">{s}</p>')

A(section("About this note"))
A('<p class="aboutnote">I wrote this note and built the accompanying model, 2026-10-06_Nebius_Model.xlsx, independently. The '
  'model carries live formulas off blue input cells across its tabs, including the run-rate reconciliation, unit economics, '
  'the if-converted share bridge, scenarios and sensitivity, and every output was recalculated and checked against an '
  'independent rebuild before publication. The note sets out at initiation depth the call published on 6 October 2026 at '
  '<a href="https://thephysicallayer.fyi/research/">thephysicallayer.fyi/research</a>; the figures, the call and the '
  're-look levels are unchanged from that pitch. It builds on my journal piece of 30 September 2026, '
  '<a href="https://thephysicallayer.fyi/journal/nebius-paid-for-what-is-switched-on/">thephysicallayer.fyi/journal/'
  'nebius-paid-for-what-is-switched-on</a>, which stays as published. Figures from Nebius filings are labelled as such; '
  'everything else, including the estimates, scenarios and the call, is my own view. I hold no position in Nebius. Personal research, not '
  'investment advice.</p>')
A('<p class="signoff">Tommy Lau | The Physical Layer | thephysicallayer.fyi</p>')
A('</div>')

html = page_shell("\n".join(P), FOOTER_TITLE, DATE).replace("</head>", EXTRA_CSS + "</head>")
open(HTML_OUT, "w").write(html)
os.makedirs(PUB, exist_ok=True)
HTML(filename=HTML_OUT).write_pdf(PDF)
print("Rendered", PDF)
