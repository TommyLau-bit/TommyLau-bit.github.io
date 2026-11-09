"""Schneider Electric initiation model, 7 Oct 2026. Live formulas throughout.

House style follows the Vertiv and Broadcom models: navy header rows, blue font for hardcoded inputs, yellow fill on
my own assumptions, green font for cross-sheet links, black for formulas. EUR million unless stated; per-share in EUR.
Adjusted figures are Schneider's own definitions (adjusted EPS deducts purchase accounting amortisation).
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from data import *

NAVY = "1F3864"; MUTED = "595959"
F_TTL = Font(bold=True, color=NAVY, size=12)
F_SUB = Font(color=MUTED, size=9)
F_HDR = Font(bold=True, color="FFFFFF", size=10)
F_IN = Font(color="0000FF")
F_INB = Font(color="0000FF", bold=True)
F_LINK = Font(color="008000")
F_B = Font(bold=True)
F_NOTE = Font(color=MUTED, size=9, italic=True)
FILL_HDR = PatternFill("solid", fgColor=NAVY)
FILL_ASSUME = PatternFill("solid", fgColor="FFFF00")
FILL_KEY = PatternFill("solid", fgColor="D9E2F3")
WRAP = Alignment(wrap_text=True, vertical="top")
RIGHT = Alignment(horizontal="right")

EUR2 = '"EUR "#,##0.00'; EUR0 = '"EUR "#,##0'; M0 = '#,##0'; M1 = '#,##0.0'; N2 = '#,##0.00'
PCT1 = '0.0%'; PCT0 = '0%'; XMULT = '0.0"x"'; MULT0 = '0"x"'
SUB = f"Tommy Lau | Schneider Electric SE (Euronext Paris: SU) | {DATE_LONG} | EUR million unless stated | Personal research, not investment advice."

wb = openpyxl.Workbook()


def sheet(name, title, widths):
    ws = wb.active if wb.active.title == "Sheet" else wb.create_sheet(name)
    ws.title = name
    ws["A1"] = title; ws["A1"].font = F_TTL
    ws["A2"] = SUB; ws["A2"].font = F_SUB
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.sheet_view.showGridLines = False
    return ws


def head(ws, row, cells, start=1):
    for i, c in enumerate(cells, start):
        x = ws.cell(row=row, column=i, value=c)
        x.font = F_HDR; x.fill = FILL_HDR
        x.alignment = Alignment(horizontal="left" if i == start else "right", vertical="center", wrap_text=True)


def note(ws, row, texts):
    for i, t in enumerate(texts):
        ws.cell(row=row + i, column=1, value=t).font = F_NOTE


def is_formula(v):
    return isinstance(v, str) and v.startswith("=")


def put(ws, r, c, v, fmt=None, bold=False):
    x = ws.cell(row=r, column=c, value=v if v is not None else "")
    if fmt: x.number_format = fmt
    x.alignment = RIGHT
    if v is not None and not is_formula(v) and not isinstance(v, str):
        x.font = Font(color="0000FF", bold=bold)
    elif isinstance(v, str) and v.startswith("=Assumptions"):
        x.font = Font(color="008000", bold=bold)
    elif bold:
        x.font = F_B
    return x


sheet("Cover", "SCHNEIDER ELECTRIC SE (EURONEXT PARIS: SU)  INITIATION MODEL", [40, 26, 90])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [64, 14, 10, 96])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to "
            "another tab. Black = formula. EUR million unless stated; per-share figures in EUR; shares in millions.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"org26", "m26", "amort26", "amort27", "amort28", "fin26", "fin27", "fin28", "tax", "minor26", "minor27", "minor28",
        "sh26", "sh27", "sh28", "org27", "org28", "dm27", "dm28", "mult", "ptcg", "syn28", "rate", "abopx", "bbsaved", "ppa",
        "bb26", "fcfh2", "fcf27", "div27"}
rows = [
    ("MARKET (retrieved 7 October 2026)", None, None, None, None),
    ("price", "Share price (Euronext Paris: SU)", PRICE, "EUR", "Euronext Paris close, 6 October 2026."),
    ("prepx", "Close on 2 October 2026, before the PTC announcement", PRICE_PRE_DEAL, "EUR", "Euronext Paris."),
    ("hiclose", "Highest close of the past year (12 August 2026)", HI_CLOSE, "EUR", "Euronext Paris; intraday high EUR 312.30 on 13 August."),
    ("pxdec25", "Close, 31 December 2025", PRICE_DEC25, "EUR", "Euronext Paris."),
    ("lr0", "Legrand close, 2 October 2026", LEGRAND[0], "EUR", "Euronext Paris; control for the sector move."),
    ("lr1", "Legrand close, 6 October 2026", LEGRAND[1], "EUR", "Euronext Paris."),
    ("shout", "Shares outstanding", SHARES_OUT, "m", "stockanalysis.com, 7 October 2026."),
    ("cons26", "2026 consensus adjusted EPS", CONS_EPS_26, "EUR", "stockanalysis.com (S&P Global), updated 25 September 2026, before the deal."),
    ("cons27", "2027 consensus adjusted EPS", CONS_EPS_27, "EUR", "Same."),
    ("constp", "Average analyst target, 21 analysts", CONS_TP, "EUR", "Same; range EUR 262 to 370."),
    ("REPORTED AND GUIDED (Schneider releases)", None, None, None, None),
    ("rev25", "Revenue, 2025", REV_H[1], "EUR m", "Full Year 2025 Results, 26 February 2026."),
    ("ebita25", "Adjusted EBITA, 2025", EBITA_H[1], "EUR m", "Same."),
    ("nd25", "Net debt, 31 December 2025", NETDEBT_H[1], "EUR m", "Same."),
    ("ndh126", "Net debt, 30 June 2026", H["nd_h126"], "EUR m", "Half Year 2026 Results, 30 July 2026."),
    ("fx26", "Currency effect on 2026 revenue", G26["fx"], "EUR m", "H1 2026 release: EUR -400m to -500m at current rates; midpoint."),
    ("orglo", "2026 organic revenue growth guide, low", G26["org_lo"], "%", "H1 2026 release: +10% to +13%."),
    ("orghi", "2026 organic revenue growth guide, high", G26["org_hi"], "%", "Same."),
    ("mlo", "2026 adjusted EBITA margin implied, low", G26["m_lo"], "%", "Same: around 19.4% to 19.7%."),
    ("mhi", "2026 adjusted EBITA margin implied, high", G26["m_hi"], "%", "Same."),
    ("ptcev", "PTC enterprise value", PTC["ev_eur"] * 1000, "EUR m", "Release of 5 October 2026: US$23.7bn (EUR 21.1bn at 1.1255)."),
    ("ptceq", "PTC equity value", PTC["eq_eur"] * 1000, "EUR m", "Same: US$22.6bn (EUR 20.1bn)."),
    ("ptcm27", "EV / 2027E adjusted EBITA paid for PTC", PTC["mult27"], "x", "Same: 21x before synergies, 13x with full run-rate synergies."),
    ("ptcrev25", "PTC revenue, CY2025", PTC["rev25"], "EUR m", "Same: EUR 2.4bn, about 40% adjusted EBITA margin."),
    ("ptccash", "Total cash consideration", PTC["cash"], "EUR m", "Same: about EUR 22bn, bridge from Morgan Stanley and Societe Generale."),
    ("newdebt", "New debt to fund PTC", NEW_DEBT, "EUR m", "Same: EUR 16bn to 17bn across several currencies; midpoint."),
    ("abo", "Equity raise (accelerated bookbuild)", ABO, "EUR m", "Same: about EUR 5bn to 6bn; midpoint. Not launched by 6 October 2026 (AMF filings)."),
    ("cognite", "Cognite, all-cash, agreed 30 June 2026", COGNITE, "EUR m", "H1 2026 release: US$3.1bn at 1.1255."),
    ("aidash", "AiDASH, c.90% of a US$350m enterprise value", AIDASH, "EUR m", "H1 2026 release, at 1.1255."),
    ("shelly", "Shelly Group, all-cash offer", SHELLY, "EUR m", "Release of 24 September 2026 (AMF FCECO083243): EUR 1.2bn, EUR 70 a share; closing expected by Q1 2027."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("org26", "Organic revenue growth, 2026", ORG26, "%", "MINE. Upper half of the +10% to +13% guide; H1 was +14.0%."),
    ("m26", "Adjusted EBITA margin, 2026", M26, "%", "MINE. Inside the guided 19.4% to 19.7%."),
    ("org27", "Organic revenue growth, 2027", ORG27, "%", "MINE. CMD target +7% to +10% a year to 2030; backlog +18% at end 2025."),
    ("org28", "Organic revenue growth, 2028", ORG28, "%", "MINE."),
    ("dm27", "Adjusted EBITA margin step, 2027", DM27, "%", "MINE. CMD: +250bps cumulatively 2026 to 2030."),
    ("dm28", "Adjusted EBITA margin step, 2028", DM28, "%", "MINE."),
    ("amort26", "Purchase accounting amortisation, 2026", AMORT[0], "EUR m", "MINE. H1 2026: EUR 206m."),
    ("amort27", "Purchase accounting amortisation, 2027", AMORT[1], "EUR m", "MINE."),
    ("amort28", "Purchase accounting amortisation, 2028 (before PTC)", AMORT[2], "EUR m", "MINE."),
    ("fin26", "Net financial expense, 2026", FIN[0], "EUR m", "MINE. H1 2026: EUR 286m."),
    ("fin27", "Net financial expense, 2027 (before PTC)", FIN[1], "EUR m", "MINE. Includes Cognite's financing."),
    ("fin28", "Net financial expense, 2028 (before PTC)", FIN[2], "EUR m", "MINE."),
    ("tax", "Tax rate on adjusted profit", TAX, "%", "Guided 23% to 25% for 2026; MINE for 2027 and 2028."),
    ("minor26", "Associates and minorities, 2026", MINOR[0], "EUR m", "MINE. H1 2026: EUR 40m."),
    ("minor27", "Associates and minorities, 2027", MINOR[1], "EUR m", "MINE."),
    ("minor28", "Associates and minorities, 2028", MINOR[2], "EUR m", "MINE."),
    ("sh26", "Diluted shares, 2026", SH[0], "m", "MINE. H1 2026 implied 562.8m."),
    ("sh27", "Diluted shares, 2027, standalone", SH[1], "m", "MINE. Buybacks of about EUR 0.6bn a year."),
    ("sh28", "Diluted shares, 2028, standalone", SH[2], "m", "MINE."),
    ("mult", "P/E on 2028E adjusted EPS, base", MULT, "x", "MINE. Today: 21.0x 2027 consensus (24.5x before the deal); peers 25.9x on 2026."),
    ("ptcg", "PTC growth, 2027 to 2028", PTC_G28, "%", "Release: revenue and ARR about 10% a year to 2029 (broker consensus)."),
    ("syn28", "Cost synergies in 2028", SYN28, "EUR m", "MINE. About a third of the EUR 250m expected by year 3."),
    ("rate", "Cost of new debt", RATE, "%", "MINE. Blended across currencies."),
    ("abopx", "Placement price of new shares", ABO_PX, "EUR", "MINE. About 4% below the 6 October close."),
    ("bb26", "Shares still to be bought back in 2026", 0.6, "m", "MINE. Rest of the EUR 600m programme."),
    ("bbsaved", "Buybacks paused in 2027 and 2028", BUYBACK_SAVED, "EUR m", "MINE. Release: pause in 2027 and 2028."),
    ("ppa", "Annual amortisation of PTC purchase accounting", PPA, "EUR m", "MINE. Not disclosed; deducted in Schneider's adjusted EPS."),
    ("fcfh2", "Free cash flow, H2 2026", 3400.0, "EUR m", "MINE. H1 2026: EUR 1,631m; FY2025: EUR 4,635m."),
    ("fcf27", "Free cash flow, January to September 2027", 3300.0, "EUR m", "MINE."),
    ("div27", "Dividend paid May 2027", 2600.0, "EUR m", "MINE. FY2025 dividend paid in 2026: EUR 2,411m."),
]
r = 6
for key, label, val, unit, src in rows:
    if label is None:
        ws.cell(row=r, column=1, value=key).font = Font(bold=True, color=NAVY); r += 1; continue
    ws.cell(row=r, column=1, value=label)
    c = ws.cell(row=r, column=2, value=val)
    mine = key in MINE
    c.font = F_INB if mine else F_IN
    if mine: c.fill = FILL_ASSUME
    c.number_format = PCT1 if unit == "%" else (MULT0 if unit == "x" else (N2 if unit == "EUR" else M1))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1

# ===================================================================== QUARTERLY
ws = sheet("Quarterly", "REVENUE BY BUSINESS MODEL, Q2 2025 TO Q2 2026", [56] + [11] * 5)
head(ws, 4, ["EUR million unless stated"] + QL)
C = [get_column_letter(2 + j) for j in range(5)]
qrows = [(5, "Revenue", Q_REV, M0), (6, "Organic growth, group", Q_ORG, PCT1)]
rr = 7
for name in ["Products", "Systems", "Software & Services"]:
    qrows.append((rr, f"{name}, share of the quarter", Q_SHARE[name], PCT0)); rr += 1
    qrows.append((rr, f"{name}, organic growth", Q_GROW[name], PCT0)); rr += 1
for row, lab, vals, fmt in qrows:
    ws.cell(row=row, column=1, value=lab)
    for j, v in enumerate(vals):
        put(ws, row, 2 + j, v, fmt)
ws["A14"] = "Checks"; ws["A14"].font = Font(bold=True, color=NAVY)
chk = [
    (15, "Systems contribution to Q2 2026 organic growth, EUR m (Q2 2025 base x share x growth)", "=B5*B9*F10", M0),
    (16, "Products contribution, EUR m", "=B5*B7*F8", M0),
    (17, "Software & Services contribution, EUR m", "=B5*B11*F12", M0),
    (18, "Systems share of Q2 2026 organic growth", "=B15/SUM(B15:B17)", PCT1),
    (19, "Systems share of H1 2026 revenue (Q1 and Q2 rounded shares)", "=(E5*E9+F5*F9)/(E5+F5)", '0.00%'),
    (20, "Systems share, FY2024 (FY2024 release)", SYS_SHARE_FY["2024"], PCT0),
    (21, "Systems share, FY2025 (FY2025 release)", SYS_SHARE_FY["2025"], PCT0),
]
for rr, lab, f, fmt in chk:
    ws.cell(row=rr, column=1, value=lab); put(ws, rr, 2, f, fmt)
note(ws, 23, ["Source: Schneider Electric releases: H1 2025 (31 July 2025), Q3 2025 revenues (30 October 2025), FY2025 (26 February 2026), Q1 2026 (30 April 2026), H1 2026 (30 July 2026).",
              "Q4 2025 shares by business model are not disclosed; the FY2025 release gives full-year shares (Products 47%, Systems 34%, Software & Services 19%).",
              "Shares are rounded to whole per cent in the releases, so the contributions and the H1 share are my approximate arithmetic."])

# ===================================================================== FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (EUR million unless stated, Schneider's adjusted measures)", [52, 12, 12, 12, 12, 12, 14])
head(ws, 4, ["", "2024A", "2025A", "2026E*", "2027E*", "2028E*", "2028E* with PTC"])
fin = [
    (5, "Revenue", [REV_H[0], REV_H[1], f"=C5*(1+{A['org26']})+{A['fx26']}", f"=D5*(1+{A['org27']})", f"=E5*(1+{A['org28']})", "=F5+PTC!B8"], M0, True),
    (6, "Organic growth", [ORG_H[0], ORG_H[1], "=" + A["org26"], "=" + A["org27"], "=" + A["org28"], None], PCT1, False),
    (7, "Adjusted EBITA margin", ["=B8/B5", "=C8/C5", "=" + A["m26"], f"=D7+{A['dm27']}", f"=E7+{A['dm28']}", "=G8/G5"], PCT1, False),
    (8, "Adjusted EBITA", [EBITA_H[0], EBITA_H[1], "=D5*D7", "=E5*E7", "=F5*F7", "=F8+PTC!B10"], M0, True),
    (9, "Purchase accounting amortisation", [-AMORT_H[0], -AMORT_H[1], "=-" + A["amort26"], "=-" + A["amort27"], "=-" + A["amort28"], f"=F9-{A['ppa']}"], M0, False),
    (10, "Net financial expense", [-FIN_H[0], -FIN_H[1], "=-" + A["fin26"], "=-" + A["fin27"], "=-" + A["fin28"], "=F10-PTC!B13"], M0, False),
    (11, "Tax on adjusted profit", [-ADJ_TAX_H[0], -ADJ_TAX_H[1], f"=-(D8+D9+D10)*{A['tax']}", f"=-(E8+E9+E10)*{A['tax']}", f"=-(F8+F9+F10)*{A['tax']}", f"=-(G8+G9+G10)*{A['tax']}"], M0, False),
    (12, "Associates and minorities", [-MINOR_H[0], -MINOR_H[1], "=-" + A["minor26"], "=-" + A["minor27"], "=-" + A["minor28"], "=F12"], M0, False),
    (13, "Adjusted net income", ["=SUM(B8:B12)", "=SUM(C8:C12)", "=SUM(D8:D12)", "=SUM(E8:E12)", "=SUM(F8:F12)", "=SUM(G8:G12)"], M0, True),
    (14, "Diluted shares, m", ["=B13/B15", "=C13/C15", "=" + A["sh26"], "=" + A["sh27"], "=" + A["sh28"], "=PTC!B16"], M1, False),
    (15, "Adjusted EPS, EUR", [EPS_H[0], EPS_H[1], "=D13/D14", "=E13/E14", "=F13/F14", "=G13/G14"], N2, True),
    (16, "EPS growth", [None, "=C15/B15-1", "=D15/C15-1", "=E15/D15-1", "=F15/E15-1", "=G15/E15-1"], PCT1, False),
    (17, "P/E at reference price", ["=" + A["price"] + "/B15", "=" + A["price"] + "/C15", "=" + A["price"] + "/D15", "=" + A["price"] + "/E15", "=" + A["price"] + "/F15", "=" + A["price"] + "/G15"], XMULT, False),
    (18, "Consensus adjusted EPS, EUR", [None, None, "=" + A["cons26"], "=" + A["cons27"], None, None], N2, False),
    (19, "Mine against consensus", [None, None, "=D15/D18-1", "=E15/E18-1", None, None], PCT1, False),
    (20, "P/E on consensus", [None, None, "=" + A["price"] + "/D18", "=" + A["price"] + "/E18", None, None], XMULT, False),
]
for rr, label, vals, fmt, bold in fin:
    ws.cell(row=rr, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        put(ws, rr, 2 + j, v, fmt)
note(ws, 22, [
    "*2026E to 2028E are my estimates. 2024 and 2025 as reported (FY2024 and FY2025 results); history reconciles to reported adjusted net income of EUR 4,664m and 4,829m.",
    "Schneider's adjusted net income deducts purchase accounting amortisation, so PTC's purchase accounting reduces it. Management's accretion guide is before that charge.",
    "Cognite and AiDASH revenue is not modelled (not disclosed); their financing cost is in net financial expense. Consensus from stockanalysis.com, updated 25 September 2026.",
    f"Note check: 2026E EPS {EPS26:.2f}; 2027E {EPS27:.2f}; 2028E standalone {EPS28:.2f}, with PTC {EPS28_PTC:.2f}.",
])

# ===================================================================== PTC
ws = sheet("PTC", "THE PTC DEAL: FINANCING, 2028 EARNINGS EFFECT AND LEVERAGE", [72, 16, 70])
head(ws, 4, ["Line", "Value", "Working / note"])
ptc = [
    ("ebita27", "PTC 2027E adjusted EBITA implied by the price, EUR m", f"={A['ptcev']}/{A['ptcm27']}", M0, "EUR 21.1bn / 21x."),
    ("ptcnd", "PTC net debt (enterprise value less equity value), EUR m", f"={A['ptcev']}-{A['ptceq']}", M0, "Not added again: the EUR 22bn cash consideration exceeds the EUR 21.1bn EV, so it covers PTC's debt and costs."),
    ("ptcrev27", "PTC revenue, 2027E, EUR m", f"={A['ptcrev25']}*(1+{A['ptcg']})^2", M0, "CY2025 EUR 2.4bn grown about 10% a year."),
    ("ptcrev28", "PTC revenue, 2028E, EUR m", f"=B7*(1+{A['ptcg']})", M0, "Full year of consolidation after closing in Q3 2027."),
    ("ptcebita28", "PTC 2028E adjusted EBITA before synergies, EUR m", f"=B5*(1+{A['ptcg']})", M0, ""),
    ("ptcebita28s", "PTC 2028E adjusted EBITA with synergies, EUR m", f"=B9+{A['syn28']}", M0, "Cost synergies about a third of EUR 250m in year 1."),
    ("newsh", "New shares from the equity raise, m", f"={A['abo']}/{A['abopx']}", M1, "EUR 5.5bn at my EUR 250 placement price."),
    ("dil", "Dilution, new shares against shares outstanding", f"=B11/{A['shout']}", PCT1, ""),
    ("interest", "Extra interest, 2028, EUR m", f"=({A['newdebt']}-{A['bbsaved']})*{A['rate']}", M0, "New debt, less cash kept by pausing buybacks."),
    ("addpre", "PTC contribution after interest and tax, before purchase accounting, EUR m", f"=(B10-B13)*(1-{A['tax']})", M0, ""),
    ("ppaat", "PTC purchase accounting after tax, EUR m", f"={A['ppa']}*(1-{A['tax']})", M0, "My assumption; not disclosed."),
    ("sh28", "Diluted shares in 2028 with PTC, m", f"={A['sh26']}-{A['bb26']}+B11", M1, "No buybacks in 2027 and 2028."),
    ("accr", "2028E adjusted EPS with PTC against standalone (Schneider's definition)", "=Financials!G15/Financials!F15-1", PCT1, "After purchase accounting."),
    ("eps_pre", "2028E EPS with PTC before purchase accounting, EUR", f"=(Financials!G13+B15+{A['amort28']}*(1-{A['tax']}))/B16", N2, ""),
    ("st_pre", "2028E standalone EPS before purchase accounting, EUR", f"=(Financials!F13+{A['amort28']}*(1-{A['tax']}))/Financials!F14", N2, ""),
    ("accr_pre", "Accretion before purchase accounting (management's measure)", "=B18/B19-1", PCT1, "Management: low single digit in year 1."),
    ("ndend26", "Net debt, end 2026E, EUR m", f"={A['ndh126']}+{A['cognite']}+{A['aidash']}-{A['fcfh2']}", M0, "Cognite and AiDASH assumed paid by year end."),
    ("ndpre", "Net debt before closing, Q3 2027E, EUR m", f"=B21+{A['shelly']}-{A['fcf27']}+{A['div27']}", M0, "Includes Shelly, expected to close by Q1 2027."),
    ("ndclose", "Net debt at closing, EUR m", f"=B22+{A['ptccash']}-{A['abo']}", M0, "Cash consideration (which covers PTC's net debt) less the equity raise."),
    ("lev25", "Net debt / adjusted EBITA, end 2025", f"={A['nd25']}/{A['ebita25']}", XMULT, "My leverage measure."),
    ("levclose", "Net debt / adjusted EBITA at closing (2027E incl. PTC)", "=B23/(Financials!E8+B5)", XMULT, ""),
]
P_ = {}
for i, (key, label, f, fmt, nt) in enumerate(ptc):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=label); put(ws, rr, 2, f, fmt); ws.cell(row=rr, column=3, value=nt).alignment = WRAP
    P_[key] = f"PTC!$B${rr}"
assert P_["ptcrev28"] == "PTC!$B$8" and P_["ptcebita28s"] == "PTC!$B$10" and P_["interest"] == "PTC!$B$13" and P_["sh28"] == "PTC!$B$16"
note(ws, 28, ["Source: 'Schneider Electric to acquire PTC', 5 October 2026, and the transaction presentation. All forecasts here are mine."])

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (P/E ON 2028E ADJUSTED EPS, WITH PTC)", [22] + [12] * 18)
hd = ["Case", "Org. 2027", "Org. 2028", "Margin step 27", "Margin step 28", "PTC synergies 28", "P/E", "Revenue 2027", "Margin 2027",
      "Revenue 2028", "Margin 2028", "EBITA 2028", "Net income 28, standalone", "EPS 28, standalone", "Net income 28, with PTC",
      "EPS 28, with PTC", "Value, EUR", "vs price", "Value without PTC"]
head(ws, 4, hd)
SROWS = SCEN + [("Price-implied", NEED_ORG, NEED_ORG, DM27, DM28, SYN28, PPA, MULT, None)]
for i, s in enumerate(SROWS):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    if s[0] == "Base":
        for col, key, fmt in [(2, "org27", PCT1), (3, "org28", PCT1), (4, "dm27", PCT1), (5, "dm28", PCT1), (6, "syn28", M0), (7, "mult", MULT0)]:
            c = ws.cell(row=rr, column=col, value="=" + A[key]); c.font = F_LINK; c.number_format = fmt
    else:
        for col, v, fmt in [(2, s[1], '0.00%'), (3, s[2], '0.00%'), (4, s[3], PCT1), (5, s[4], PCT1), (6, s[5], M0), (7, s[7], MULT0)]:
            c = ws.cell(row=rr, column=col, value=v); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = fmt
    f = {
        8: f"=Financials!$D$5*(1+B{rr})", 9: f"={A['m26']}+D{rr}", 10: f"=H{rr}*(1+C{rr})", 11: f"=I{rr}+E{rr}", 12: f"=J{rr}*K{rr}",
        13: f"=(L{rr}-{A['amort28']}-{A['fin28']})*(1-{A['tax']})-{A['minor28']}", 14: f"=M{rr}/{A['sh28']}",
        15: f"=M{rr}+(PTC!$B$9+F{rr}-PTC!$B$13)*(1-{A['tax']})-{A['ppa']}*(1-{A['tax']})", 16: f"=O{rr}/PTC!$B$16",
        17: f"=P{rr}*G{rr}", 18: f"=Q{rr}/{A['price']}-1", 19: f"=N{rr}*G{rr}",
    }
    fm = {8: M0, 9: PCT1, 10: M0, 11: PCT1, 12: M0, 13: M0, 14: N2, 15: M0, 16: N2, 17: EUR2, 18: PCT1, 19: EUR2}
    for col, ff in f.items():
        ws.cell(row=rr, column=col, value=ff).number_format = fm[col]
ws["A11"] = "Probability"; ws["A11"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=10, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=11, column=2 + j, value=s[8]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E11"] = "=SUM(B11:D11)"; ws["E11"].number_format = PCT0; ws["F11"] = "must be 100%"; ws["F11"].font = F_NOTE
ws["A13"] = "Probability-weighted value, EUR"; ws["A13"].font = F_B
ws["Q13"] = "=B11*Q5+C11*Q6+D11*Q7"; ws["Q13"].number_format = EUR2; ws["Q13"].font = F_B; ws["Q13"].fill = FILL_KEY
ws["R13"] = f"=Q13/{A['price']}-1"; ws["R13"].number_format = PCT1
note(ws, 15, ["Value = 2028E adjusted EPS with PTC (Schneider's definition, after purchase accounting) x P/E. The last column shows the same case without PTC.",
              "Bear: data centre orders digest, organic growth 4% and 3%, margin flat at 19.6%, no PTC synergies, 18x. Bull: growth 11% and 10%, margin +80bps a year, 25x.",
              "Price-implied: the organic growth in 2027 and 2028, at base margins and multiple, that gives today's price (row 8 value equals the price)."])

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION: P/E ON 2028E, TWELVE MONTHS OUT", [72, 16, 70])
head(ws, 4, ["Line", "Value", "Working / note"])
val = [
    ("base", "Base value with PTC, EUR", "=Scenarios!Q6", EUR2, "22x 2028E adjusted EPS with PTC."),
    ("st", "Base value without PTC, EUR", "=Scenarios!S6", EUR2, "22x 2028E standalone EPS."),
    ("dealcost", "Cost of the deal per share at the base multiple, EUR", "=B6-B5", EUR2, ""),
    ("px", "Reference price, EUR", "=" + A["price"], EUR2, "Euronext Paris close, 6 October 2026."),
    ("upb", "Base value against the price", "=B5/B8-1", PCT1, ""),
    ("upst", "Value without PTC against the price", "=B6/B8-1", PCT1, ""),
    ("wtd", "Probability-weighted value, EUR", "=Scenarios!Q13", EUR2, ""),
    ("rule", "Rule on value alone (long at 15% above, short at 25% below)", '=IF(B9>=0.15,"LONG",IF(B9<=-0.25,"SHORT","NO CALL"))', None, "Mechanical, on the base value."),
    ("call", "DRAFT VIEW" if CALL["draft"] else "CALL", CALL["direction"], None, "Draft for Tommy Lau's decision." if CALL["draft"] else "Tommy Lau's call."),
    ("tgt", "Target, EUR", CALL["target"] if CALL["target"] else "none", EUR2, "No target for no call."),
    ("rlong", "Price at or below which the base is 15% above (points long)", "=B5/1.15", EUR2, ""),
    ("rshort", "Price at or above which the base is 25% below (points short)", "=B5/0.75", EUR2, ""),
    ("mcap", "Market value, EUR bn", f"={A['price']}*{A['shout']}/1000", M1, ""),
    ("mcappre", "Market value at the 2 October close, EUR bn", f"={A['prepx']}*{A['shout']}/1000", M1, ""),
    ("lost", "Market value lost, 2 to 6 October, EUR bn", "=B18-B17", M1, "Against EUR 21.1bn paid for PTC's enterprise value."),
    ("drop", "Share price change, 2 to 6 October", f"={A['price']}/{A['prepx']}-1", PCT1, ""),
    ("lrchg", "Legrand share price change, 2 to 6 October", f"={A['lr1']}/{A['lr0']}-1", PCT1, "Control."),
    ("pec26", "P/E on 2026 consensus", "=Financials!D20", XMULT, ""),
    ("pec27", "P/E on 2027 consensus", "=Financials!E20", XMULT, ""),
    ("pec27pre", "P/E on 2027 consensus at the 2 October close", f"={A['prepx']}/{A['cons27']}", XMULT, ""),
    ("pe28", "P/E on my 2028E with PTC", "=Financials!G17", XMULT, ""),
    ("needeps", "2028E EPS the price needs at the base multiple, EUR", f"={A['price']}/{A['mult']}", N2, ""),
    ("needorg", "Organic growth a year in 2027 and 2028 that gives it", "=Scenarios!B8", PCT1, "Scenarios row 8; CMD target 7% to 10%."),
    ("peermed", "Peer median P/E on 2026 consensus", "=Peers!E11", XMULT, ""),
    ("peerval", "My 2026E EPS at the peer median, EUR", "=Financials!D15*B28", EUR2, "Cross-check."),
    ("offhi", "Against the highest close (12 August 2026)", f"={A['price']}/{A['hiclose']}-1", PCT1, ""),
    ("sincedec", "Change since 31 December 2025", f"={A['price']}/{A['pxdec25']}-1", PCT1, ""),
]
V = {}
for i, (key, label, f, fmt, nt) in enumerate(val):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=label)
    c = ws.cell(row=rr, column=2, value=f)
    if fmt: c.number_format = fmt
    if not is_formula(f): c.font = F_IN
    if key in ("base", "call"):
        ws.cell(row=rr, column=1).font = F_B; c.font = F_B; c.fill = FILL_KEY
    if key == "call": c.font = F_INB
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
    V[key] = f"Valuation!$B${rr}"
assert V["base"] == "Valuation!$B$5" and V["px"] == "Valuation!$B$8" and V["upb"] == "Valuation!$B$9" and V["mcap"] == "Valuation!$B$17" and V["peermed"] == "Valuation!$B$28"

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE WITH PTC: 2028 ADJUSTED EBITA MARGIN AGAINST THE P/E (EUR)", [34, 14, 14, 14])
head(ws, 4, ["2028 margin (standalone) \\ P/E", "", "", ""])
for j, (x, link) in enumerate(zip(SENS_X, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["mult"]) if link else x)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, d in enumerate([-0.01, 0, 0.01]):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=f"=Financials!$F$7{d:+.2f}" if d else "=Financials!$F$7")
    c.number_format = PCT1; c.font = F_LINK
    for j in range(3):
        col = get_column_letter(2 + j)
        ws.cell(row=rr, column=2 + j, value=(
            f"=(((Financials!$F$5*$A{rr}-{A['amort28']}-{A['fin28']})*(1-{A['tax']})-{A['minor28']})"
            f"+PTC!$B$14-PTC!$B$15)/PTC!$B$16*{col}$4")).number_format = EUR0
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Cells 15% or more above the price"; ws["A10"].font = F_B
ws["B10"] = f'=COUNTIF(B5:D7,">="&{A["price"]}*1.15)'; ws["C10"] = "of 9"
ws["A11"] = "Cells 25% or more below the price"; ws["A11"].font = F_B
ws["B11"] = f'=COUNTIF(B5:D7,"<="&{A["price"]}*0.75)'; ws["C11"] = "of 9"
note(ws, 13, ["Middle row is my base 2028 standalone margin; revenue and the PTC contribution as in the base case."])

# ===================================================================== PEERS
ws = sheet("Peers", "PEER MULTIPLES: P/E ON 2026 CONSENSUS EPS (stockanalysis.com, closes of 6 OCTOBER 2026)", [22, 20, 12, 12, 12, 70])
head(ws, 4, ["Company", "Listing", "Price", "2026 EPS", "P/E 2026", "What they make"])
ws.cell(row=5, column=1, value="Schneider Electric").font = F_B; ws.cell(row=5, column=2, value="Euronext Paris: SU")
put(ws, 5, 3, "=" + A["price"], N2); put(ws, 5, 4, "=" + A["cons26"], N2); put(ws, 5, 5, "=C5/D5", XMULT)
ws.cell(row=5, column=6, value="Electrical distribution, UPS, prefabricated modules, cooling, automation, software")
for i, (co, tk, px, eps, cur, what, nt) in enumerate(PEERS):
    rr = 6 + i
    ws.cell(row=rr, column=1, value=co); ws.cell(row=rr, column=2, value=tk)
    put(ws, rr, 3, px, N2); put(ws, rr, 4, eps, N2); put(ws, rr, 5, f"=C{rr}/D{rr}", XMULT)
    ws.cell(row=rr, column=6, value=f"{what} ({cur}{'; ' + nt if nt else ''})").alignment = WRAP
ws["A11"] = "Median, five peers"; ws["A11"].font = F_B; ws["E11"] = "=MEDIAN(E6:E10)"; ws["E11"].number_format = XMULT
note(ws, 13, ["2026 consensus EPS from stockanalysis.com forecast pages (S&P Global data), updated 25 September to 6 October 2026; prices are 6 October 2026 closes in local currency.",
              "Siemens' fiscal year ends 30 September. Multiples only, to set the base multiple; no view on the peers' shares is expressed."])

# ===================================================================== SOURCES
ws = sheet("Sources", "SOURCES", [6, 130])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "Schneider Electric Full Year 2024 Results, 20 February 2025 (AMF FCECO077559): revenue, adjusted EBITA, adjusted EPS, business model shares (Systems 31%).",
    "Schneider Electric Half Year 2025 Results, 31 July 2025 (AMF FCECO079331): Q2 2025 revenue and business model growth; net capex H1 2025.",
    "Schneider Electric Third Quarter 2025 Revenues, 30 October 2025 (AMF FCECO080070): Q3 2025 revenue and business model shares and growth.",
    "Schneider Electric Full Year 2025 Results, release and presentation, 26 February 2026: revenue, adjusted EBITA, adjusted net income bridge, net debt, capex, backlog, Data Center & Networks 30% of orders, 2026 target and 2026 to 2030 targets.",
    "Schneider Electric announcement of a takeover offer for Shelly Group, 24 September 2026 (AMF FCECO083243): EUR 1.2bn, all cash.",
    "Schneider Electric Q1 2026 Revenues, 30 April 2026; Half Year 2026 Results, 30 July 2026 (AMF FCECO082813): quarterly revenue and business model, mix effect of EUR -148m, gross margin bridge, net debt, buyback, Cognite and AiDASH, upgraded 2026 target, results date.",
    "Schneider Electric Capital Markets Day, 11 December 2025: release (targets, buyback, disposals) and LSEG transcript.",
    "Schneider Electric to acquire PTC, release of 5 October 2026 (AMF FCECO083330; PTC Form 8-K Ex. 99.1) and transaction presentation: price, values, multiples, synergies, financing, accretion guide, ratings, buyback pause, closing, Q3 revenues brought forward to 16 October 2026.",
    "Euronext Paris historical prices (live.euronext.com), retrieved 7 October 2026: Schneider Electric and Legrand closes. (Yahoo Finance chart API refused requests on 7 October 2026.)",
    "stockanalysis.com, retrieved 7 October 2026: Schneider consensus EPS and average target (updated 25 September 2026), shares outstanding; peers' 2026 consensus EPS and prices.",
    "The Physical Layer, 'Schneider Electric sells AI data centres the finished system, not the parts', 7 October 2026: https://thephysicallayer.fyi/journal/schneider-sells-the-finished-system/",
    "Estimates for 2026 to 2028, the PTC effect and the valuation are the author's own. Personal research, not investment advice. I hold no position in Schneider Electric.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# ===================================================================== COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Draft view" if CALL["draft"] else "Call", "=" + V["call"], None, "Draft for Tommy Lau's decision; not yet a call." if CALL["draft"] else "Tommy Lau's call."),
    ("Target, EUR", "=" + V["tgt"], EUR2, "None for no call."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Reference price, EUR", "=" + A["price"], EUR2, "Euronext Paris close, 6 October 2026."),
    ("Base value with PTC, EUR", "=" + V["base"], EUR2, "22x 2028E adjusted EPS with PTC."),
    ("Base value against the price", "=" + V["upb"], PCT1, ""),
    ("Base value without PTC, EUR", "=" + V["st"], EUR2, ""),
    ("Probability-weighted value, EUR", "=" + V["wtd"], EUR2, "25 / 50 / 25 bear / base / bull."),
    ("2026E / 2027E / 2028E EPS (with PTC), EUR", '=TEXT(Financials!D15,"0.00")&" / "&TEXT(Financials!E15,"0.00")&" / "&TEXT(Financials!G15,"0.00")', None, "Own estimates, Schneider's adjusted definition."),
    ("Horizon", "12 months, to October 2027", None, ""),
]
for i, (lab, v, fmt, nt) in enumerate(cover):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=lab).font = F_B
    c = ws.cell(row=rr, column=2, value=v)
    if fmt: c.number_format = fmt
    c.alignment = RIGHT
    c.font = F_LINK if is_formula(v) else F_IN
    ws.cell(row=rr, column=3, value=nt).alignment = WRAP
ws["A17"] = "Tabs"; ws["A17"].font = Font(bold=True, color=NAVY)
for i, (t, d) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Quarterly", "Revenue by business model, Q2 2025 to Q2 2026, and the claim's tests."),
    ("Financials", "2024A to 2028E, standalone and with PTC: revenue, adjusted EBITA, adjusted net income, EPS, P/E, consensus."),
    ("PTC", "Financing, 2028 earnings effect, accretion on both definitions, net debt and leverage at closing."),
    ("Scenarios", "Bear / base / bull and the price-implied case; probability-weighted value."),
    ("Valuation", "Base value, the band, market value lost, multiples."),
    ("Sensitivity", "2028 margin against the P/E."),
    ("Peers", "P/E on 2026 consensus for five peers."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t); ws.cell(row=18 + i, column=2, value=d)
ws["A29"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A29"].font = F_NOTE
ws["A30"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."; ws["A30"].font = F_NOTE

order = ["Cover", "Assumptions", "Quarterly", "Financials", "PTC", "Scenarios", "Valuation", "Sensitivity", "Peers", "Sources"]
wb._sheets = [wb[n] for n in order]
for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
