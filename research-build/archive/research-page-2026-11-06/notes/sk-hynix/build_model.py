"""SK hynix initiation model, 2 Nov 2026. Live formulas throughout.

House style follows the Vertiv and Micron models: navy header rows, blue font for hardcoded inputs, yellow fill on my own
assumptions, green font for cross-sheet links, black for formulas. KRW trillion unless stated; shares in millions; per-share
figures in KRW. Calendar years.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from data import *
import data as _d

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

K0 = '"KRW "#,##0'; TN1 = '#,##0.0'; TN2 = '#,##0.00'; TN3 = '#,##0.000'
PCT1 = '0.0%'; PCT0 = '0%'; MULT1 = '0.0"x"'; MULT0 = '0"x"'
SUB = f"Tommy Lau | SK hynix Inc. (KRX: 000660) | {DATE_LONG} | KRW trillion unless stated; per share in KRW; shares in millions | Personal research, not investment advice."

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


sheet("Cover", "SK HYNIX INC. (KRX: 000660)  INITIATION MODEL", [38, 26, 90])

# ===================================================================== ASSUMPTIONS
ws = sheet("Assumptions", "ASSUMPTIONS AND INPUTS", [62, 16, 10, 92])
ws["A3"] = ("Blue = hardcoded input. Yellow fill = my own assumption (change these to move the value). Green = link to another tab. "
            "Black = formula. KRW trillion unless stated; per share in KRW; shares in millions.")
ws["A3"].font = F_NOTE
head(ws, 5, ["Input", "Value", "Unit", "Source / note"])
A = {}
MINE = {"q4rev", "q4opm", "tax", "r27", "opm27", "g28", "opm28", "daq4", "da27", "capexq4", "capex27", "wcq4", "wc27", "staff",
        "tam25", "tam26", "tam27", "sh25", "sh26", "sh27", "fx25", "fx26", "hbmopm", "bits", "nyears", "pf", "nm", "mult", "rate",
        "w1", "w2", "w3"}
rows = [
    ("MARKET (retrieved 2 November 2026)", None, None, None, None),
    ("price", "Share price (KRX: 000660)", PRICE, "KRW", "KRX regular-session close, 2 November 2026, via Yahoo Finance, checked against stockanalysis.com."),
    ("hiclose", "Highest close of the past year (22 June 2026)", HI_CLOSE[0], "KRW", "Yahoo Finance. Intraday high KRW 2,987,000 on 25 June 2026."),
    ("pxdec25", "Close, 30 December 2025", PRICE_DEC25, "KRW", "Yahoo Finance."),
    ("fx", "KRW per US$", FX, "KRW", "Hana Bank notice rate, 18:21 KST 2 November 2026, via Naver Finance."),
    ("ads", "SKHY ADS close, 30 October 2026", ADS_OCT30, "US$", "Nasdaq.com. One ADS = one tenth of a common share (prospectus)."),
    ("px30", "KRX close, 30 October 2026", PX_OCT30, "KRW", "Yahoo Finance and stockanalysis.com."),
    ("fx30", "KRW per US$, previous notice (used for 30 October)", FX_PREV, "KRW", "2 November rate less the reported change of 5.20."),
    ("sh", "Shares entitled to the Q3 2026 dividend", SH, "m", "Form 6-K, 28 Oct 2026: total KRW 14,103,466,480,000 at KRW 20,000 a share. Held flat in my forecasts."),
    ("cons26", "2026 consensus EPS", CONS_EPS_26, "KRW", "stockanalysis.com (S&P Global), 37 analysts; range 268,436 to 426,371."),
    ("cons27", "2027 consensus EPS", CONS_EPS_27, "KRW", "stockanalysis.com (shown as 527.16K)."),
    ("consrev26", "2026 consensus revenue", CONS_REV_26, "KRW tn", "stockanalysis.com."),
    ("consrev27", "2027 consensus revenue", CONS_REV_27, "KRW tn", "stockanalysis.com."),
    ("constp", "Average analyst target", CONS_TP, "KRW", "stockanalysis.com, 41 analysts; range 1,575,000 to 4,700,000."),
    ("REPORTED (releases, Form 6-K, prospectus)", None, None, None, None),
    ("rev24", "2024 revenue", REV10[-2], "KRW tn", "Prospectus."),
    ("rev25", "2025 revenue", REV10[-1], "KRW tn", "Prospectus; release of 28 Jan 2026."),
    ("op24", "2024 operating profit", OP24, "KRW tn", "Release / stockanalysis.com."),
    ("op25", "2025 operating profit", OP25, "KRW tn", "Release of 28 Jan 2026."),
    ("ni24", "2024 net profit attributable", NI10[-2], "KRW tn", "stockanalysis.com."),
    ("ni25", "2025 net profit attributable", NI10[-1], "KRW tn", "stockanalysis.com (total profit 42.948 in the prospectus)."),
    ("eps24", "2024 EPS", 28418.66, "KRW", "stockanalysis.com."),
    ("eps25", "2025 EPS", EPS25, "KRW", "stockanalysis.com."),
    ("dram25", "2025 DRAM revenue", DRAM["2025"], "KRW tn", "Prospectus."),
    ("ytdrev", "Revenue, Q1 to Q3 2026", YTD26_REV, "KRW tn", "Form 6-K, 28 Oct 2026."),
    ("ytdop", "Operating profit, Q1 to Q3 2026", YTD26_OP, "KRW tn", "Form 6-K."),
    ("ytdni", "Profit attributable to controlling interests, Q1 to Q3 2026", YTD26_NI_CTRL, "KRW tn", "Form 6-K. Includes Kioxia gains and Q3 valuation and FX losses."),
    ("netcash", "Net cash, 30 Sep 2026", NET_CASH, "KRW tn", "Q3 release: cash 114.5, borrowings 15.8."),
    ("buyoct", "Share purchases executed in October 2026", BUY_OCT, "KRW tn", "Form 6-K, 26 Oct 2026: 5,943,272 shares bought 1 to 21 October (my sum of the daily table)."),
    ("MY ASSUMPTIONS", None, None, None, None),
    ("q4rev", "Q4 2026 revenue", Q4_REV, "KRW tn", "MINE. Consensus implies about 127 (363.55 less 236.51). DRAM bits guided up mid 20s %."),
    ("q4opm", "Q4 2026 operating margin", Q4_OPM, "%", "MINE. Q3 80%."),
    ("tax", "Tax rate on operating profit", TAX, "%", "MINE. Q1 2026 21.8% (prospectus); Q3 2026 about 21.6%."),
    ("r27", "2027 revenue", R27, "KRW tn", "MINE. Consensus 576.17."),
    ("opm27", "2027 operating margin", OPM27, "%", "MINE."),
    ("g28", "2028 revenue change", G28, "%", "MINE."),
    ("opm28", "2028 operating margin", OPM28, "%", "MINE."),
    ("daq4", "Q4 2026 depreciation and amortisation", DA_Q4, "KRW tn", "MINE. Q3 2026 4.3 (call)."),
    ("da27", "2027 depreciation and amortisation", DA27, "KRW tn", "MINE. 2025 13.5 (prospectus)."),
    ("capexq4", "Q4 2026 capital spending", CAPEX_Q4, "KRW tn", "MINE."),
    ("capex27", "2027 capital spending", CAPEX27, "KRW tn", "MINE. 2027 to 'increase significantly compared to 2026' (call); 2025 27.5."),
    ("wcq4", "Q4 2026 working capital build", WC_Q4, "KRW tn", "MINE."),
    ("wc27", "2027 working capital build", WC27, "KRW tn", "MINE."),
    ("staff", "Share purchases for staff compensation (a cost)", STAFF_BUY, "KRW tn", "MINE treatment; about 10 of the 20 resolved on 28 Oct 2026 (Form 6-K)."),
    ("tam25", "Industry HBM revenue 2025", HBM_TAM[0], "US$bn", "MINE, after Micron (about 35, 17 Dec 2025); Gartner 33 (prospectus)."),
    ("tam26", "Industry HBM revenue 2026", HBM_TAM[1], "US$bn", "MINE. 40% a year, as in my Micron note."),
    ("tam27", "Industry HBM revenue 2027", HBM_TAM[2], "US$bn", "MINE. Gartner 86 (prospectus) would give 57.7tn, 10.7% of my revenue."),
    ("sh25", "SK hynix HBM share 2025", HBM_SHARE[0], "%", "MINE. IDC 56.4% in Q1 2026 (prospectus)."),
    ("sh26", "SK hynix HBM share 2026", HBM_SHARE[1], "%", "MINE."),
    ("sh27", "SK hynix HBM share 2027", HBM_SHARE[2], "%", "MINE."),
    ("fx25", "Average KRW per US$, 2025", HBM_FX[0], "KRW", "MINE, approximate."),
    ("fx26", "Average KRW per US$, 2026", HBM_FX[1], "KRW", "MINE, approximate (1,523.5 on 31 Mar, 1,538.05 on 2 Jul, 1,341 now)."),
    ("hbmopm", "HBM operating margin 2026", HBM_OPM26, "%", "MINE. Below the company's: HBM priced a year ahead (Micron: 2027 prices narrow the gap)."),
    ("bits", "Bit growth a year to a mid-cycle year", BITS, "x", "MINE, as in my Micron note."),
    ("nyears", "Years to the mid-cycle year", N_YEARS, "yrs", "MINE."),
    ("pf", "Mid-cycle revenue per bit against the base period", PF, "%", "MINE, as in my Micron note."),
    ("nm", "Mid-cycle net margin", NM, "%", "MINE. 2016 to 2025: 23.5% in all; 2018 peak 38.4% (Normal tab)."),
    ("mult", "P/E on normal earnings", _d.MULT, "x", "MINE."),
    ("rate", "Discount rate on above-normal earnings", RATE, "%", "MINE."),
    ("w1", "Share of 2027 excess still to come at Oct 2027 (Q4)", W_UP[0], "%", "MINE: one quarter, undiscounted."),
    ("w2", "Share of 2028 excess earned in 2028", W_UP[1], "%", "MINE."),
    ("w3", "Share of 2028 excess earned again in 2029", W_UP[2], "%", "MINE: half."),
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
    c.number_format = PCT1 if unit == "%" else ("0.00" if unit == "x" else ('#,##0.00' if unit in ("US$", "KRW") and val < 100000 else ('#,##0' if unit == "KRW" else TN3)))
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=src).alignment = WRAP
    A[key] = f"Assumptions!$B${r}"
    r += 1

# ===================================================================== QUARTERLY
ws = sheet("Quarterly", "QUARTERLY HISTORY, Q1 2024 TO Q3 2026, AND MY Q4 2026", [40] + [10] * 12)
head(ws, 4, ["KRW trillion"] + QL + ["Q4 26E"])
C = [get_column_letter(2 + j) for j in range(12)]
ws.cell(row=5, column=1, value="Revenue").font = F_B
ws.cell(row=6, column=1, value="Operating profit").font = F_B
ws.cell(row=7, column=1, value="Operating margin")
ws.cell(row=8, column=1, value="Net profit (reported, total)")
ws.cell(row=9, column=1, value="Revenue growth on a year earlier")
for j in range(11):
    put(ws, 5, 2 + j, Q_REV[j], TN2); put(ws, 6, 2 + j, Q_OP[j], TN2)
    put(ws, 7, 2 + j, f"={C[j]}6/{C[j]}5", PCT0)
    if Q_NI[j] is not None: put(ws, 8, 2 + j, Q_NI[j], TN2)
    if j >= 4: put(ws, 9, 2 + j, f"={C[j]}5/{C[j - 4]}5-1", PCT0)
put(ws, 5, 13, "=" + A["q4rev"], TN2); put(ws, 6, 13, f"=M5*{A['q4opm']}", TN2); put(ws, 7, 13, "=M6/M5", PCT0)
put(ws, 9, 13, "=M5/I5-1", PCT0)
ws["A11"] = "Checks"; ws["A11"].font = Font(bold=True, color=NAVY)
for rr, lab, f, fmt in [(12, "Revenue Q1 to Q3 2026, sum", "=SUM(J5:L5)", TN3), (13, "2024 revenue, sum", "=SUM(B5:E5)", TN3),
                        (14, "2025 revenue, sum", "=SUM(F5:I5)", TN3), (15, "Four quarters to June 2026 (normal base)", "=SUM(H5:K5)", TN2),
                        (16, "Q3 2026 revenue growth on a year earlier", "=L9", PCT1)]:
    ws.cell(row=rr, column=1, value=lab); c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
note(ws, 18, ["Source: SK hynix preliminary results releases, 23 January 2025 to 28 October 2026; Form 6-K, 28 October 2026. 2024 quarters per the releases, summing to the prospectus total.",
              "Q3 2026 non-operating: KRW 32.6tn of expenses, including an 11.6tn foreign exchange loss and 22.9tn of investment valuation losses (call). Q2 2026 net profit includes Kioxia gains."])

# ===================================================================== HBM
ws = sheet("HBM", "HOW MUCH OF SK HYNIX IS HBM (MY ESTIMATES; SK HYNIX DOES NOT DISCLOSE HBM REVENUE)", [48, 14, 14, 14])
head(ws, 4, ["", "2025", "2026E", "2027E"])
hb = [
    (5, "Industry HBM revenue, US$bn", ["=" + A["tam25"], "=" + A["tam26"], "=" + A["tam27"]], TN1),
    (6, "SK hynix share", ["=" + A["sh25"], "=" + A["sh26"], "=" + A["sh27"]], PCT0),
    (7, "Average KRW per US$", ["=" + A["fx25"], "=" + A["fx26"], "=" + A["fx"]], '#,##0'),
    (8, "SK hynix HBM revenue, KRW tn", ["=B5*B6*B7/1000", "=C5*C6*C7/1000", "=D5*D6*D7/1000"], TN1),
    (9, "Total revenue, KRW tn", ["=" + A["rev25"], "=Financials!D5", "=Financials!E5"], TN1),
    (10, "HBM share of revenue", ["=B8/B9", "=C8/C9", "=D8/D9"], PCT1),
    (11, "HBM share of DRAM revenue (2025)", [f"=B8/{A['dram25']}", None, None], PCT1),
    (12, "HBM operating profit at my HBM margin (2026)", [None, f"=C8*{A['hbmopm']}", None], TN1),
    (13, "HBM share of operating profit (2026)", [None, "=C12/Financials!D8", None], PCT1),
]
for rr, lab, vals, fmt in hb:
    ws.cell(row=rr, column=1, value=lab).font = F_B if rr in (8, 10) else Font()
    for j, v in enumerate(vals):
        put(ws, rr, 2 + j, v, fmt)
note(ws, 15, ["Cross-checks from primary sources: HBM was more than 40% of DRAM revenue in Q4 2024 and HBM revenue more than doubled in 2025 (SK hynix releases);",
              "the largest customer was 23.9% of 2025 revenue, the two largest 14.8% and 12.4% of Q1 2026; China rose from 19.7% to 24.3% of revenue (prospectus)."])

# ===================================================================== FINANCIALS
ws = sheet("Financials", "FINANCIAL SUMMARY AND FORECASTS (KRW trillion unless stated)", [60, 13, 13, 13, 13, 13])
head(ws, 4, ["", "2024A", "2025A", "2026E*", "2027E*", "2028E*"])
# columns: B 2024, C 2025, D 2026, E 2027, F 2028
fin = [
    (5, "Revenue", ["=" + A["rev24"], "=" + A["rev25"], f"={A['ytdrev']}+{A['q4rev']}", "=" + A["r27"], f"=E5*(1+{A['g28']})"], TN1, True),
    (6, "Revenue growth", [None, "=C5/B5-1", "=D5/C5-1", "=E5/D5-1", "=F5/E5-1"], PCT1, False),
    (7, "Revenue against consensus", [None, None, f"=D5/{A['consrev26']}-1", f"=E5/{A['consrev27']}-1", None], PCT1, False),
    (8, "Operating profit", ["=" + A["op24"], "=" + A["op25"], f"={A['ytdop']}+{A['q4rev']}*{A['q4opm']}", f"=E5*{A['opm27']}", f"=F5*{A['opm28']}"], TN1, True),
    (9, "Operating margin", ["=B8/B5", "=C8/C5", "=D8/D5", "=E8/E5", "=F8/F5"], PCT1, False),
    (10, "Net profit (2026: nine months reported plus my Q4 on operations; later: operations only)",
     ["=" + A["ni24"], "=" + A["ni25"], f"={A['ytdni']}+{A['q4rev']}*{A['q4opm']}*(1-{A['tax']})", f"=E8*(1-{A['tax']})", f"=F8*(1-{A['tax']})"], TN1, True),
    (11, "Net margin", ["=B10/B5", "=C10/C5", "=D10/D5", "=E10/E5", "=F10/F5"], PCT1, False),
    (12, "EPS, KRW", ["=" + A["eps24"], "=" + A["eps25"], f"=D10/{A['sh']}*1000000", f"=E10/{A['sh']}*1000000", f"=F10/{A['sh']}*1000000"], '#,##0', True),
    (13, "Consensus EPS, KRW", [None, None, "=" + A["cons26"], "=" + A["cons27"], None], '#,##0', False),
    (14, "Mine against consensus", [None, None, "=D12/D13-1", "=E12/E13-1", None], PCT1, False),
    (15, "P/E at the reference price", [f"={A['price']}/B12", f"={A['price']}/C12", f"={A['price']}/D12", f"={A['price']}/E12", f"={A['price']}/F12"], MULT1, False),
    (16, "P/E on consensus", [None, None, f"={A['price']}/D13", f"={A['price']}/E13", None], MULT1, False),
    (18, "Free cash flow (Q4 2026 in the 2026 column; full year 2027)", [None, None,
     f"={A['q4rev']}*{A['q4opm']}*(1-{A['tax']})+{A['daq4']}-{A['capexq4']}-{A['wcq4']}", f"=E10+{A['da27']}-{A['capex27']}-{A['wc27']}", None], TN1, False),
    (19, "Net cash at 30 Sep 2027, before dividends and cancellations", [None, None, None,
     f"={A['netcash']}-{A['buyoct']}-{A['staff']}+D18+0.75*E18", None], TN1, True),
    (20, "  per share, KRW", [None, None, None, f"=E19/{A['sh']}*1000000", None], '#,##0', True),
    (21, "Net cash now after October purchases, per share, KRW", [None, None, f"=({A['netcash']}-{A['buyoct']})/{A['sh']}*1000000", None, None], '#,##0', False),
]
for rr, label, vals, fmt, bold in fin:
    ws.cell(row=rr, column=1, value=label).font = F_B if bold else Font()
    for j, v in enumerate(vals):
        put(ws, rr, 2 + j, v, fmt)
note(ws, 23, ["*2026E: reported Q1 to Q3 (Form 6-K) plus my Q4. 2027E and 2028E are my estimates on operations only, excluding finance items.",
              "EPS for 2026 to 2028 is on the 705.2m shares entitled to the Q3 dividend; reported 2024 and 2025 EPS are on the shares of those years.",
              "Consensus from stockanalysis.com (S&P Global), retrieved 2 November 2026."])

# ===================================================================== NORMAL
ws = sheet("Normal", "THE CYCLE AND NORMAL (MID-CYCLE) EARNINGS", [44, 13, 13, 13])
head(ws, 4, ["Year", "Revenue, KRW tn", "Net profit", "Net margin"])
for i, (y, rv, ni) in enumerate(zip(YRS10, REV10, NI10)):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=y)
    put(ws, rr, 2, rv, TN3); put(ws, rr, 3, ni, TN3); put(ws, rr, 4, f"=C{rr}/B{rr}", PCT1)
ws["A16"] = "2016 to 2025, all ten years"; ws["A16"].font = F_B
ws["B16"] = "=SUM(B5:B14)"; ws["C16"] = "=SUM(C5:C14)"; ws["D16"] = "=C16/B16"
for c, f in (("B16", TN2), ("C16", TN2), ("D16", PCT1)): ws[c].number_format = f
ws["A17"] = "2018, the last cycle's peak"; ws["D17"] = "=D7"; ws["D17"].number_format = PCT1
head(ws, 19, ["Normal year (base)", "Value", "", ""])
nrows = [
    (20, "Revenue, four quarters to June 2026", "=Quarterly!B15", TN2),
    (21, "Bit growth factor", f"={A['bits']}^{A['nyears']}", "0.0000"),
    (22, "Revenue per bit against the base period", "=" + A["pf"], PCT0),
    (23, "Normal revenue, KRW tn", "=B20*B21*B22", TN1),
    (24, "Normal net margin", "=" + A["nm"], PCT0),
    (25, "Normal net profit, KRW tn", "=B23*B24", TN2),
    (26, "Normal EPS, KRW", f"=B25/{A['sh']}*1000000", '#,##0'),
]
for rr, lab, f, fmt in nrows:
    ws.cell(row=rr, column=1, value=lab); c = ws.cell(row=rr, column=2, value=f); c.number_format = fmt
ws["A26"].font = F_B; ws["B26"].fill = FILL_KEY
note(ws, 28, ["Revenue and net profit: SK hynix annual results releases for 2016 to 2020; stockanalysis.com (S&P Global) for 2021 to 2025 (attributable).",
              "The normal year is mine and uses the method of my Micron note: the four quarters nearest Micron's fiscal 2026, bits up 20% a year for four years, 55% of the price per bit."])

# ===================================================================== SCENARIOS
ws = sheet("Scenarios", "THREE CASES, TWELVE MONTHS OUT (VALUE AT OCTOBER 2027, KRW PER SHARE)", [10] + [11] * 18)
head(ws, 4, ["Case", "Rev. per bit", "Normal margin", "Normal P/E", "2027 rev.", "2027 OPM", "2028 change", "2028 OPM", "w Q4 27",
             "w 2028", "w 2029", "Normal EPS", "2027 EPS", "2028 EPS", "Net cash / sh", "Excess / sh", "Normal value / sh", "Value", "vs price"])
for i, s in enumerate(SCEN):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=s[0]).font = F_B
    keys = ["pf", "nm", "mult", "r27", "opm27", "g28", "opm28", "w1", "w2", "w3"]
    vals = [s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8][0], s[8][1], s[8][2]]
    fmts = [PCT0, PCT0, MULT0, TN1, PCT0, PCT0, PCT0, PCT0, PCT0, PCT0]
    for col, (kk, v, fmt) in enumerate(zip(keys, vals, fmts), 2):
        if s[0] == "Base":
            c = ws.cell(row=rr, column=col, value="=" + A[kk]); c.font = F_LINK
        else:
            c = ws.cell(row=rr, column=col, value=v); c.font = F_INB; c.fill = FILL_ASSUME
        c.number_format = fmt
    sh = A["sh"]; t = A["tax"]
    ws.cell(row=rr, column=12, value=f"=Normal!$B$20*Normal!$B$21*B{rr}*C{rr}/{sh}*1000000").number_format = '#,##0'
    ws.cell(row=rr, column=13, value=f"=E{rr}*F{rr}*(1-{t})/{sh}*1000000").number_format = '#,##0'
    ws.cell(row=rr, column=14, value=f"=E{rr}*(1+G{rr})*H{rr}*(1-{t})/{sh}*1000000").number_format = '#,##0'
    ws.cell(row=rr, column=15, value=f"=({A['netcash']}-{A['buyoct']}-{A['staff']}+Financials!$D$18+0.75*(E{rr}*F{rr}*(1-{t})+{A['da27']}-{A['capex27']}-{A['wc27']}))/{sh}*1000000").number_format = '#,##0'
    ws.cell(row=rr, column=16, value=f"=I{rr}*(M{rr}-L{rr})+J{rr}*(N{rr}-L{rr})/(1+{A['rate']})+K{rr}*(N{rr}-L{rr})/(1+{A['rate']})^2").number_format = '#,##0'
    ws.cell(row=rr, column=17, value=f"=L{rr}*D{rr}").number_format = '#,##0'
    ws.cell(row=rr, column=18, value=f"=O{rr}+P{rr}+Q{rr}").number_format = '#,##0'
    ws.cell(row=rr, column=19, value=f"=R{rr}/{A['price']}-1").number_format = PCT1
ws["A10"] = "Probability"; ws["A10"].font = F_B
for j, s in enumerate(SCEN):
    ws.cell(row=9, column=2 + j, value=s[0]).font = F_B
    c = ws.cell(row=10, column=2 + j, value=s[9]); c.font = F_INB; c.fill = FILL_ASSUME; c.number_format = PCT0
ws["E10"] = "=SUM(B10:D10)"; ws["E10"].number_format = PCT0; ws["F10"] = "must be 100%"; ws["F10"].font = F_NOTE
ws["A12"] = "Probability-weighted value, KRW"; ws["A12"].font = F_B
ws["R12"] = "=B10*R5+C10*R6+D10*R7"; ws["R12"].number_format = '#,##0'; ws["R12"].font = F_B; ws["R12"].fill = FILL_KEY
ws["S12"] = f"=R12/{A['price']}-1"; ws["S12"].number_format = PCT1
note(ws, 14, ["Value at October 2027 = net cash at 30 Sep 2027 per share + above-normal earnings still to come, discounted + normal EPS x normal P/E.",
              "Excess = w Q4 27 x (2027 EPS - normal) + w 2028 x (2028 EPS - normal) / 1.1 + w 2029 x (2028 EPS - normal) / 1.1^2.",
              "Net cash moves with each case's 2027 profit (three quarters of 2027 free cash flow by 30 Sep 2027). Normal cases are those of my Micron note.",
              "Bear: prices turn in 2027; 2028 revenue falls 35%; normal margin 19%. Bull: 2027 above consensus; shortage lasts to 2029; normal margin 40%."])

# ===================================================================== VALUATION
ws = sheet("Valuation", "VALUATION: NET CASH + ABOVE-NORMAL EARNINGS + NORMAL EARNINGS, AT OCTOBER 2027", [74, 18, 70])
head(ws, 4, ["Line", "Value", "Working / note"])
val = [
    ("nc", "Net cash per share at 30 Sep 2027, KRW", "=Scenarios!O6", '#,##0', "Before dividends and cancellations, which reach holders."),
    ("exc", "Above-normal earnings, discounted, per share, KRW", "=Scenarios!P6", '#,##0', "Base case."),
    ("term", "Normal EPS x normal P/E, KRW", "=Scenarios!Q6", '#,##0', "Base case."),
    ("base", "Base-case value per share, KRW", "=B5+B6+B7", '#,##0', ""),
    ("px", "Reference price, KRW", "=" + A["price"], '#,##0', "KRX close, 2 November 2026."),
    ("upb", "Base value against the price", "=B8/B9-1", PCT1, ""),
    ("wtd", "Probability-weighted value, KRW", "=Scenarios!R12", '#,##0', ""),
    ("rule", "Rule on value alone (long at 15% above, short at 25% below)", '=IF(B10>=0.15,"LONG",IF(B10<=-0.25,"SHORT","NO CALL"))', None, "Mechanical only."),
    ("call", "DRAFT VIEW" if CALL["draft"] else "CALL", CALL["direction"], None, "Draft for Tommy Lau's decision." if CALL["draft"] else "Tommy Lau's call."),
    ("tgt", "Target, KRW", CALL["target"] if CALL["target"] else "None (no call)", '#,##0', "Base value rounded down."),
    ("mcap", "Market value, KRW tn", f"={A['price']}*{A['sh']}/1000000", TN1, "On 705.2m shares."),
    ("mcapusd", "Market value, US$bn", f"=B15/{A['fx']}*1000", TN1, ""),
    ("ev", "Enterprise value, KRW tn (net of 30 Sep net cash)", f"=B15-{A['netcash']}", TN1, ""),
    ("k", "Weight on normal EPS inside the excess (base)", f"={A['w1']}+{A['w2']}/(1+{A['rate']})+{A['w3']}/(1+{A['rate']})^2", "0.0000", ""),
    ("c", "Excess before normal EPS (base), KRW", f"={A['w1']}*Scenarios!M6+({A['w2']}/(1+{A['rate']})+{A['w3']}/(1+{A['rate']})^2)*Scenarios!N6", '#,##0', ""),
    ("need", "Normal EPS the price needs, cash kept, KRW", f"=(B9-B5-B19)/({A['mult']}-B18)", '#,##0', "What the market prices in."),
    ("needm", "That as a net margin on my normal revenue", f"=B20*{A['sh']}/1000000/Normal!B23", PCT1, "2016 to 2025: 23.5%."),
    ("need0", "Normal EPS the price needs if the cash is spent and earns nothing, KRW", f"=(B9-B19)/({A['mult']}-B18)", '#,##0', ""),
    ("need0m", "That as a net margin on my normal revenue", f"=B22*{A['sh']}/1000000/Normal!B23", PCT1, "Against my base 30%."),
    ("nocash", "Base value without the net cash, KRW", "=B8-B5", '#,##0', ""),
    ("nocashup", "  against the price", "=B24/B9-1", PCT1, ""),
    ("half", "Base value with half the net cash, KRW", "=B8-0.5*B5", '#,##0', ""),
    ("halfup", "  against the price", "=B26/B9-1", PCT1, ""),
    ("revisit", "Price above which the base is less than 15% above (back to no call)", "=B8/1.15", '#,##0', ""),
    ("pe26", "P/E on my 2026E", "=Financials!D15", MULT1, ""),
    ("pec27", "P/E on 2027 consensus", "=Financials!E16", MULT1, ""),
    ("pe27", "P/E on my 2027E", "=Financials!E15", MULT1, ""),
    ("pen", "P/E on my normal EPS", f"={A['price']}/Normal!B26", MULT1, ""),
    ("offhi", "Against the highest close (22 Jun 2026)", f"={A['price']}/{A['hiclose']}-1", PCT1, ""),
    ("adsprem", "ADS premium to Seoul, 30 October 2026", f"={A['ads']}*10/({A['px30']}/{A['fx30']})-1", PCT1, "ADS x 10 against the KRX close in dollars."),
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
assert V["base"] == "Valuation!$B$8" and V["k"] == "Valuation!$B$18" and V["c"] == "Valuation!$B$19" and V["need0"] == "Valuation!$B$22" and V["half"] == "Valuation!$B$26"

# ===================================================================== SENSITIVITY
ws = sheet("Sensitivity", "VALUE PER SHARE: NORMAL NET MARGIN AGAINST THE MULTIPLE ON NORMAL EARNINGS (KRW)", [30, 16, 16, 16])
head(ws, 4, ["Normal net margin \\ normal P/E", "", "", ""])
for j, (m, link) in enumerate(zip(SENS_X, [False, True, False])):
    c = ws.cell(row=4, column=2 + j, value=("=" + A["mult"]) if link else m)
    c.number_format = MULT0; c.font = Font(bold=True, color="FFFFFF"); c.fill = FILL_HDR; c.alignment = RIGHT
for i, (m, link) in enumerate(zip(SENS_NM, [False, True, False])):
    rr = 5 + i
    c = ws.cell(row=rr, column=1, value=("=" + A["nm"]) if link else m)
    c.number_format = PCT0; c.font = F_LINK if link else F_IN
    for j in range(3):
        col = get_column_letter(2 + j)
        n = f"(Normal!$B$23*$A{rr}/{A['sh']}*1000000)"
        ws.cell(row=rr, column=2 + j, value=f"=Valuation!$B$5+Valuation!$B$19-Valuation!$B$18*{n}+{n}*{col}$4").number_format = '#,##0'
ws["C6"].fill = FILL_KEY
ws["A9"] = "Cells above the reference price"; ws["A9"].font = F_B
ws["B9"] = f'=COUNTIF(B5:D7,">"&{A["price"]})'; ws["C9"] = "of 9"
ws["A10"] = "Lowest cell against the price"; ws["A10"].font = F_B
ws["B10"] = f"=MIN(B5:D7)/{A['price']}-1"; ws["B10"].number_format = PCT1
note(ws, 12, ["Middle row links to my base normal margin and the middle column to the base multiple. Net cash, 2027 and 2028 as in the base."])

# ===================================================================== PEERS
ws = sheet("Peers", "PEER MULTIPLES ON CONSENSUS FOR THE YEAR ENDING IN 2027 (stockanalysis.com, 2 NOVEMBER 2026)", [24, 16, 14, 8, 14, 16, 12, 40])
head(ws, 4, ["Company", "Listing", "Price", "Currency", "Consensus EPS", "Year", "P/E", "What they make"])
ws["A5"] = "SK hynix"; ws["A5"].font = F_B; ws["B5"] = "KRX: 000660"
c = ws.cell(row=5, column=3, value="=" + A["price"]); c.font = F_LINK; c.number_format = '#,##0'
ws["D5"] = "KRW"
c = ws.cell(row=5, column=5, value="=" + A["cons27"]); c.font = F_LINK; c.number_format = '#,##0'
ws["F5"] = "CY2027"; ws["G5"] = "=C5/E5"; ws["G5"].number_format = MULT1; ws["H5"] = "DRAM, HBM, NAND"
for i, (co, tk, px, cur, eps, yr, what, nt) in enumerate(PEERS):
    rr = 6 + i
    ws.cell(row=rr, column=1, value=co); ws.cell(row=rr, column=2, value=tk)
    put(ws, rr, 3, px, TN2); ws.cell(row=rr, column=4, value=cur); put(ws, rr, 5, eps, TN2)
    ws.cell(row=rr, column=6, value=yr); ws.cell(row=rr, column=7, value=f"=C{rr}/E{rr}").number_format = MULT1
    ws.cell(row=rr, column=8, value=what)
note(ws, 9, ["Prices: SK hynix and Samsung Electronics KRX closes of 2 November 2026; Micron Nasdaq close of 30 October 2026. Consensus from stockanalysis.com (S&P Global).",
             "Micron's fiscal year ends in August, so the multiples are not on one basis. Multiples only; no view on the peers' shares."])

# ===================================================================== SOURCES
ws = sheet("Sources", "SOURCES", [6, 130])
head(ws, 4, ["No.", "Source and what it supports"])
srcs = [
    "SK hynix preliminary results releases (newsroom): 23 January 2025 (FY24, as reprinted; HBM over 40% of DRAM revenue in Q4 2024), 28 January 2026 (FY25; HBM revenue more than doubled), 23 April 2026, 29 July 2026, 28 October 2026 (Q3 2026; net cash 98.7tn; 14 LTAs; shareholder returns).",
    "SK hynix Form 6-K, 28 October 2026: preliminary results of operations (revenue, operating profit, pre-tax and net profit, attributable profit, year to date).",
    "SK hynix Forms 6-K, 26 October 2026 (report on acquisition of treasury shares, daily table; amended cancellation decision, 23,693,272 shares on 5 November 2026) and 28 October 2026 (cash dividend of KRW 20,000, total KRW 14,103,466,480,000; FY26 return plan; KRW 20tn new buyback).",
    "SK hynix Q3 2026 earnings call, 28 October 2026 (stockanalysis.com and The Motley Fool transcripts): bits and prices, Q4 guide, custom HBM, HBM4E, LTAs, capex, non-operating items, D&A.",
    "SK hynix prospectus, Form 424B4, 10 July 2026 (SEC EDGAR, CIK 2120882): income statements 2023 to 2025 and Q1 2026; revenue by product; customer and regional concentration; capex; shares; ADS terms; Yongin plan; custom HBM definition; IDC market shares and Gartner forecasts as quoted.",
    "SK hynix annual results releases for 2016 to 2020; stockanalysis.com (S&P Global) annual figures for 2021 to 2025.",
    "Yahoo Finance and stockanalysis.com: KRX regular-session closes; Naver Finance: Hana Bank KRW/USD notice rate; retrieved 2 November 2026. Nasdaq.com: SKHY and MU closes.",
    "stockanalysis.com, retrieved 2 November 2026: consensus EPS and revenue, average target, Samsung Electronics and Micron consensus.",
    "Micron earnings call, 17 December 2025 (HBM market about US$35bn in 2025 to about US$100bn in 2028); prepared remarks, 30 September 2026. Nvidia NVHBM blog, 26 August 2026.",
    "The Physical Layer, 'Memory, not maths, sets the pace of AI, so the biggest buyer now designs it', 31 October 2026: https://thephysicallayer.fyi/journal/memory-not-maths/",
    "Estimates from Q4 2026, HBM revenue, normal earnings and the valuation are the author's own. Personal research, not investment advice. I hold no position in SK hynix.",
]
for i, s in enumerate(srcs):
    ws.cell(row=5 + i, column=1, value=i + 1)
    ws.cell(row=5 + i, column=2, value=s).alignment = WRAP

# ===================================================================== COVER
ws = wb["Cover"]
head(ws, 4, ["Item", "Value", "Note"])
cover = [
    ("Draft view" if CALL["draft"] else "Call", "=" + V["call"], None, "Draft for Tommy Lau's decision; not yet a call." if CALL["draft"] else "Tommy Lau's call."),
    ("Target, KRW", "=" + V["tgt"], '#,##0', "Base value rounded down."),
    ("Conviction", CALL["conviction"], None, "Judgement, not formula."),
    ("Reference price, KRW", "=" + A["price"], '#,##0', "KRX close, 2 November 2026."),
    ("Base value, KRW", "=" + V["base"], '#,##0', "Net cash + above-normal earnings + 12x normal EPS, at October 2027."),
    ("Base value against the price", "=" + V["upb"], PCT1, ""),
    ("Probability-weighted value, KRW", "=" + V["wtd"], '#,##0', "25 / 50 / 25 bear / base / bull."),
    ("Normal EPS the price needs, cash kept / spent, KRW", '=TEXT(Valuation!B20,"#,##0")&" / "&TEXT(Valuation!B22,"#,##0")', None, "Against my base normal EPS on the Normal tab."),
    ("HBM share of 2026 revenue (my estimate)", "=HBM!C10", PCT1, "HBM tab."),
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
for i, (t, dsc) in enumerate([
    ("Assumptions", "Every input, with its source. Change the yellow cells to move the value."),
    ("Quarterly", "Q1 2024 to Q3 2026 reported and my Q4 2026."),
    ("HBM", "My estimate of HBM revenue and its share of revenue and operating profit."),
    ("Financials", "2024A to 2028E: revenue, margins, EPS, consensus, P/E, cash at September 2027."),
    ("Normal", "Ten years of the cycle and my normal (mid-cycle) year."),
    ("Scenarios", "Bear / base / bull value at October 2027 and the probability-weighted value."),
    ("Valuation", "Base value, what the price needs with and without the cash, multiples."),
    ("Sensitivity", "Normal net margin against the multiple on normal earnings."),
    ("Peers", "Memory peers on consensus for the year ending in 2027."),
    ("Sources", "Every source used."),
]):
    ws.cell(row=18 + i, column=1, value=t); ws.cell(row=18 + i, column=2, value=dsc)
ws["A30"] = "Colour key: blue = hardcoded input; yellow fill = my own assumption; green = link to another tab; black = formula."
ws["A30"].font = F_NOTE
ws["A31"] = f"Companion note: {DATE}_{COMPANY}_Initiation.pdf. Personal research, not investment advice."; ws["A31"].font = F_NOTE

order = ["Cover", "Assumptions", "Quarterly", "HBM", "Financials", "Normal", "Scenarios", "Valuation", "Sensitivity", "Peers", "Sources"]
wb._sheets = [wb[n] for n in order]
for w in wb.worksheets:
    w.freeze_panes = "A5"
wb.active = 0
wb.save(XLSX)
print("model written", XLSX)
