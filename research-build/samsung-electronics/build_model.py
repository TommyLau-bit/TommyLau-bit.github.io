"""Samsung Electronics initiation model, 2 Nov 2026. Live formulas throughout.

House style follows the Vertiv, Micron and SK Hynix models: navy header rows, blue font for hardcoded inputs, yellow fill on my
own assumptions, black for formulas. KRW trillion unless stated; shares in millions; per-share figures in KRW. Calendar years.
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
F_B = Font(bold=True)
F_NOTE = Font(color=MUTED, size=9, italic=True)
FILL_HDR = PatternFill("solid", fgColor=NAVY)
FILL_ASSUME = PatternFill("solid", fgColor="FFFF00")
FILL_KEY = PatternFill("solid", fgColor="D9E2F3")
WRAP = Alignment(wrap_text=True, vertical="top")

K0 = '"KRW "#,##0'; TN1 = '#,##0.0'; TN2 = '#,##0.00'; PCT1 = '0.0%'; PCT0 = '0%'; X1 = '0.0"x"'; N0 = '#,##0'
SUB = (f"Tommy Lau | Samsung Electronics Co., Ltd. (KRX: 005930) | {DATE_LONG} | KRW trillion unless stated; per share in KRW; "
       "shares in millions | Blue = input; yellow = my assumption | Personal research, not investment advice.")

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


def head(ws, row, cells):
    for i, c in enumerate(cells, 1):
        x = ws.cell(row=row, column=i, value=c); x.font = F_HDR; x.fill = FILL_HDR


def put(ws, ref, v, fmt=None, inp=False, mine=False, bold=False):
    c = ws[ref]; c.value = v
    if fmt: c.number_format = fmt
    if inp: c.font = F_IN
    if mine: c.fill = FILL_ASSUME; c.font = F_IN
    if bold: c.font = Font(bold=True, color="0000FF" if (inp or mine) else "000000")
    return c


# =================== Inputs ===================
I = sheet("Inputs", "Inputs: market data, balance sheet, shares and my assumptions", [46, 16, 70])
head(I, 4, ["Input", "Value", "Source / note"])
NAMES = {}
rows = [
    ("price", "Common share price, KRW", PRICE, K0, False, "KRX close 2 Nov 2026 (stockanalysis.com)"),
    ("price_p", "Preferred share price, KRW", PRICE_P, K0, False, "KRX close 2 Nov 2026 (stockanalysis.com)"),
    ("fx", "KRW per US$", FX, TN2, False, "Hana Bank notice rate, 2 Nov 2026"),
    ("div_total", "Q3 2026 dividend total, KRW tn", DIV_TOTAL, '0.000', False, "RNS, 29 Oct 2026"),
    ("pref_iss", "Preferred shares issued, m", SH_P, TN2, False, "2026 half-year business report, at 30 Jun 2026; none in treasury (RNS, 12 Oct 2026)"),
    ("com_iss", "Common shares issued, m", SH_C_ISSUED, TN2, False, "2026 half-year business report, at 30 Jun 2026"),
    ("dps", "Q3 2026 dividend per share, KRW", DPS_Q3, N0, False, "Same for common and preferred"),
    ("treas", "Common treasury shares after 6 Oct buyback, m", TREAS_C, TN2, False, "RNS, 12 Oct 2026"),
    ("net_cash", "Net cash, 30 Sep 2026", NET_CASH, TN1, False, "3Q 2026 deck"),
    ("buy_oct", "October buybacks, KRW tn", BUY_OCT, TN1, True, "MINE: KRW 15tn programme less 12.5 paid in 3Q"),
    ("invest", "Investments, 30 Sep 2026", INVEST, TN1, False, "3Q 2026 deck"),
    ("ni_9m", "Profit attributable, Q1 to Q3 2026", sum(Q_NI_ATTR_26), TN1, False, "Decks: 47.1 + 71.3 + 75.2"),
    ("eps_9m", "EPS, Q1 to Q3 2026 (common), KRW", sum(Q_EPS_26), N0, False, "Decks: 7,123 + 10,849 + 11,462"),
    ("rev_9m", "Revenue, Q1 to Q3 2026", sum(Q_REV[4:]), TN1, False, "Decks"),
    ("op_9m", "Operating profit, Q1 to Q3 2026", sum(Q_OP[4:]), TN1, False, "Decks"),
    ("mem_9m", "Memory sales, Q1 to Q3 2026", sum(Q_MEM[4:]), TN1, False, "Decks"),
    ("dsop_9m", "Device Solutions operating profit, Q1 to Q3 2026", sum(Q_DS_OP[4:]), TN1, False, "Decks"),
    ("mem_base", "Memory sales, four quarters to June 2026", BASE_MEM, TN1, False, "Decks: 26.7 + 37.1 + 74.8 + 120.8"),
    ("capex26", "2026 capex plan", CAPEX_26, TN1, False, "RNS, 29 Oct 2026"),
    ("capex9m", "Capex, Q1 to Q3 2026", CAPEX_9M, TN1, False, "3Q 2026 release"),
    ("cons26", "Consensus EPS 2026, KRW", CONS_EPS_26, N0, False, "stockanalysis.com, 2 Nov 2026"),
    ("cons27", "Consensus EPS 2027, KRW", CONS_EPS_27, N0, False, "stockanalysis.com, 2 Nov 2026 (shown as 75.63K)"),
    ("consrev26", "Consensus revenue 2026", CONS_REV_26, TN1, False, "stockanalysis.com"),
    ("consrev27", "Consensus revenue 2027", CONS_REV_27, TN1, False, "stockanalysis.com"),
    ("tax", "Tax rate", TAX, PCT0, True, "MINE: Q3 2026 23.8%, Q2 24.2%"),
    ("q4_mem", "Q4 2026 memory sales", Q4["mem"], TN1, True, "MINE"),
    ("q4_nonmem", "Q4 2026 foundry and LSI sales (net)", Q4["nonmem"], TN1, True, "MINE"),
    ("q4_dsopm", "Q4 2026 chip operating margin", Q4["ds_opm"], PCT0, True, "MINE: Q3 72%"),
    ("q4_dx", "Q4 2026 DX sales", Q4["dx"], TN1, True, "MINE: MX to decline on the quarter"),
    ("q4_dxop", "Q4 2026 DX operating profit", Q4["dx_op"], TN1, True, "MINE"),
    ("q4_sdc", "Q4 2026 SDC sales", Q4["sdc"], TN1, True, "MINE"),
    ("q4_sdcop", "Q4 2026 SDC operating profit", Q4["sdc_op"], TN1, True, "MINE"),
    ("q4_har", "Q4 2026 Harman sales", Q4["har"], TN1, True, "MINE"),
    ("q4_harop", "Q4 2026 Harman operating profit", Q4["har_op"], TN1, True, "MINE"),
    ("q4_elim", "Q4 2026 intersegment eliminations", Q4["elim"], TN1, True, "MINE: Q2 and Q3 about -16"),
    ("mem27", "2027 memory sales", MEM27, TN1, True, "MINE"),
    ("mopm27", "2027 memory operating margin", MEM_OPM27, PCT0, True, "MINE"),
    ("g28", "2028 memory sales change", G28, PCT0, True, "MINE"),
    ("mopm28", "2028 memory operating margin", MEM_OPM28, PCT0, True, "MINE"),
    ("oth_rev27", "2027 other sales, net of eliminations", sum(v[0] for v in OTH27.values()), TN1, True, "MINE: foundry 32, DX 196, SDC 33, Harman 18, elim -72"),
    ("oth_op27", "2027 other operating profit", sum(v[1] for v in OTH27.values()), TN1, True, "MINE: foundry 1, DX 2, SDC 3.5, Harman 1.7"),
    ("oth_rev28", "2028 other sales, net of eliminations", sum(v[0] for v in OTH28.values()), TN1, True, "MINE: foundry 36, DX 200, SDC 34, Harman 19, elim -70"),
    ("oth_op28", "2028 other operating profit", sum(v[1] for v in OTH28.values()), TN1, True, "MINE: foundry 2, DX 6, SDC 4, Harman 1.8"),
    ("da_q4", "Q4 2026 depreciation", DA_Q4, TN1, True, "MINE"),
    ("da27", "2027 depreciation", DA27, TN1, True, "MINE"),
    ("capex27", "2027 capex", CAPEX27, TN1, True, "MINE"),
    ("wc_q4", "Q4 2026 working capital build", WC_Q4, TN1, True, "MINE"),
    ("wc27", "2027 working capital build", WC27, TN1, True, "MINE"),
    ("bits", "Bit growth a year to the normal year", BITS - 1, PCT0, True, "As in my Micron and SK Hynix notes"),
    ("years", "Years of bit growth", N_YEARS, N0, True, "As in my Micron and SK Hynix notes"),
    ("pf", "Revenue per bit in the normal year, share of base", PF, PCT0, True, "As in my Micron and SK Hynix notes"),
    ("nm", "Normal memory net margin", NM, PCT0, True, "As in my Micron and SK Hynix notes"),
    ("mult", "Multiple on normal memory earnings", MULT, '0"x"', True, "As in my Micron and SK Hynix notes"),
    ("rate", "Discount rate", RATE, PCT0, True, "As in my Micron and SK Hynix notes"),
    ("w0", "Weight: Q4 2027 share of 2027 excess", W_UP[0], TN2, True, "As in my SK Hynix note"),
    ("w1", "Weight: 2028 excess", W_UP[1], TN2, True, ""),
    ("w2", "Weight: half of 2028 excess again in 2029", W_UP[2], TN2, True, ""),
    ("fdy_rev", "Foundry and System LSI sales, 2026", FOUNDRY_REV26, TN1, True, "DS less memory: 6.9 + 6.7 + 6.4 + my Q4 7.5"),
    ("fdy_x", "Foundry and LSI, multiple of sales", FOUNDRY_X, X1, True, "MINE"),
    ("mx_op", "Phones (MX/NW) normal operating profit", OTHERS[1][1], TN1, True, "2023 to 2025 average 12.2"),
    ("mx_x", "Phones multiple on after-tax profit", OTHERS[1][2], '0"x"', True, "MINE"),
    ("vd_op", "VD/DA normal operating profit", OTHERS[2][1], TN1, True, "2023 to 2025 average 0.9"),
    ("vd_x", "VD/DA multiple", OTHERS[2][2], '0"x"', True, "MINE"),
    ("sdc_op", "Samsung Display normal operating profit", OTHERS[3][1], TN1, True, "2023 to 2025 average 4.5"),
    ("sdc_x", "Display multiple", OTHERS[3][2], '0"x"', True, "MINE"),
    ("har_op", "Harman normal operating profit", OTHERS[4][1], TN1, True, "2025 1.5"),
    ("har_x", "Harman multiple", OTHERS[4][2], '0"x"', True, "MINE"),
    ("inv_cut", "Haircut on investments", INV_HAIRCUT, PCT0, True, "MINE"),
    ("disc", "Conglomerate and governance discount", DISC, PCT0, True, "MINE"),
]
for i, (key, lab, v, fmt, mine, note) in enumerate(rows, 5):
    I.cell(row=i, column=1, value=lab)
    put(I, f"B{i}", v, fmt, inp=not mine, mine=mine)
    I.cell(row=i, column=3, value=note).font = F_NOTE
    NAMES[key] = f"Inputs!$B${i}"
N = NAMES
# derived shares
r = len(rows) + 6
I.cell(row=r, column=1, value="Shares (derived)").font = F_B
labels = [("sh_p", "Preferred shares, m", f"={N['pref_iss']}"),
          ("sh_c_iss", "Common issued, m", f"={N['com_iss']}"),
          ("sh_c", "Common outstanding, m", None),
          ("sh", "Economic shares, m", None),
          ("mcap", "Market value, both classes, KRW tn", None),
          ("mcap_usd", "Market value, US$bn", None),
          ("pref_gap", "Preferred discount to common", None)]
for j, (key, lab, f) in enumerate(labels):
    rr = r + 1 + j
    NAMES[key] = f"Inputs!$B${rr}"
    I.cell(row=rr, column=1, value=lab)
for j, (key, lab, f) in enumerate(labels):
    rr = r + 1 + j
    fm = {"sh_p": f, "sh_c_iss": f, "sh_c": f"={N['sh_c_iss']}-{N['treas']}", "sh": f"={N['sh_c']}+{N['sh_p']}",
          "mcap": f"=({N['price']}*{N['sh_c']}+{N['price_p']}*{N['sh_p']})/1E6", "mcap_usd": f"={N['mcap']}/{N['fx']}*1000",
          "pref_gap": f"=1-{N['price_p']}/{N['price']}"}[key]
    put(I, f"B{rr}", fm, PCT1 if key == "pref_gap" else TN1)

# =================== Quarterly history ===================
Q = sheet("Quarterly", "Quarterly segment history (Samsung earnings call decks)", [34] + [10] * 7)
head(Q, 4, ["KRW tn"] + QL)
qrows = [("Revenue", Q_REV), ("Operating profit", Q_OP), ("Device Solutions sales", Q_DS_REV), ("Device Solutions OP", Q_DS_OP),
         ("Memory sales", Q_MEM), ("MX/NW sales", Q_MX_REV), ("MX/NW operating profit", Q_MX_OP), ("DX operating profit", Q_DX_OP)]
for i, (lab, vals) in enumerate(qrows, 5):
    Q.cell(row=i, column=1, value=lab)
    for j, v in enumerate(vals, 2):
        put(Q, f"{get_column_letter(j)}{i}", v, TN1, inp=True)
Q.cell(row=13, column=1, value="Chips share of operating profit")
Q.cell(row=14, column=1, value="Operating margin")
for j in range(2, 9):
    L = get_column_letter(j)
    put(Q, f"{L}13", f"={L}8/{L}6", PCT0)
    put(Q, f"{L}14", f"={L}6/{L}5", PCT1)
Q["A16"] = "Chips share of operating profit, Q1 to Q3 2026"; put(Q, "B16", "=SUM(F8:H8)/SUM(F6:H6)", PCT1)

# =================== Financials ===================
F = sheet("Financials", "Financials: history and my forecasts", [40, 12, 12, 12, 12, 12, 40])
head(F, 4, ["KRW tn unless stated", "2025A", "2026E", "2027E", "2028E", "", "Note"])
t = N["tax"]
q4ds = f"({N['q4_mem']}+{N['q4_nonmem']})"
F["A5"] = "Memory sales"; put(F, "B5", MEM_REV_H["2025"], TN1, inp=True); put(F, "C5", f"={N['mem_9m']}+{N['q4_mem']}", TN1)
put(F, "D5", f"={N['mem27']}", TN1); put(F, "E5", f"=D5*(1+{N['g28']})", TN1)
F["A6"] = "Revenue"; put(F, "B6", REV[-1], TN1, inp=True)
put(F, "C6", f"={N['rev_9m']}+{q4ds}+{N['q4_dx']}+{N['q4_sdc']}+{N['q4_har']}+{N['q4_elim']}", TN1)
put(F, "D6", f"=D5+{N['oth_rev27']}", TN1); put(F, "E6", f"=E5+{N['oth_rev28']}", TN1)
F["A7"] = "Revenue vs consensus"; put(F, "C7", f"=C6/{N['consrev26']}-1", PCT1); put(F, "D7", f"=D6/{N['consrev27']}-1", PCT1)
F["A8"] = "Memory operating profit (2026: chip division)"; put(F, "C8", f"={N['dsop_9m']}+{q4ds}*{N['q4_dsopm']}", TN1)
put(F, "D8", f"=D5*{N['mopm27']}", TN1); put(F, "E8", f"=E5*{N['mopm28']}", TN1)
F["A9"] = "Q4 2026 operating profit"; put(F, "C9", f"={q4ds}*{N['q4_dsopm']}+{N['q4_dxop']}+{N['q4_sdcop']}+{N['q4_harop']}", TN1)
F["A10"] = "Operating profit"; put(F, "B10", OP[-1], TN1, inp=True); put(F, "C10", f"={N['op_9m']}+C9", TN1)
put(F, "D10", f"=D8+{N['oth_op27']}", TN1); put(F, "E10", f"=E8+{N['oth_op28']}", TN1)
F["A11"] = "Operating margin"
for L in "BCDE":
    put(F, f"{L}11", f"={L}10/{L}6", PCT1)
F["A12"] = "Net profit attributable (2026: 9M reported + Q4 mine)"; put(F, "B12", NI[-1], TN1, inp=True)
put(F, "C12", f"={N['ni_9m']}+C9*(1-{t})", TN1); put(F, "D12", f"=D10*(1-{t})", TN1); put(F, "E12", f"=E10*(1-{t})", TN1)
F["A13"] = "EPS, KRW"; put(F, "B13", EPS_H[-1], N0, inp=True)
put(F, "C13", f"={N['eps_9m']}+C9*(1-{t})/{N['sh']}*1E6", N0); put(F, "D13", f"=D12/{N['sh']}*1E6", N0); put(F, "E13", f"=E12/{N['sh']}*1E6", N0)
F["A14"] = "Consensus EPS, KRW"; put(F, "C14", f"={N['cons26']}", N0); put(F, "D14", f"={N['cons27']}", N0)
F["A15"] = "Mine vs consensus"; put(F, "C15", "=C13/C14-1", PCT1); put(F, "D15", "=D13/D14-1", PCT1)
F["A16"] = "P/E at the common price"
for L in "BCDE":
    put(F, f"{L}16", f"={N['price']}/{L}13", X1)
F["A17"] = "P/E on consensus"; put(F, "C17", f"={N['price']}/C14", X1); put(F, "D17", f"={N['price']}/D14", X1)
F["A18"] = "Memory after-tax profit"; put(F, "D18", f"=D8*(1-{t})", TN1); put(F, "E18", f"=E8*(1-{t})", TN1)
F["A19"] = "Memory net margin"; put(F, "D19", "=D18/D5", PCT1); put(F, "E19", "=E18/E5", PCT1)
F["A21"] = "Free cash flow (Q4 2026; 2027)"
put(F, "C21", f"=C9*(1-{t})+{N['da_q4']}-({N['capex26']}-{N['capex9m']})-{N['wc_q4']}", TN1)
put(F, "D21", f"=D12+{N['da27']}-{N['capex27']}-{N['wc27']}", TN1)
F["A22"] = "Net cash now (after Q3 dividend and Oct buybacks)"; put(F, "C22", f"={N['net_cash']}-{N['div_total']}-{N['buy_oct']}", TN1)
F["A23"] = "Net cash, 30 Sep 2027, before distributions"; put(F, "D23", "=C22+C21+0.75*D21", TN1)
F["A24"] = "Net cash per share, Sep 2027, KRW"; put(F, "D24", f"=D23/{N['sh']}*1E6", N0)
F["A26"] = "Chips share of 2026 operating profit"; put(F, "C26", "=C8/C10", PCT1)
F["G5"] = "2025: deck; 2026: nine months reported + my Q4"
for c in ("G5",):
    F[c].font = F_NOTE

# =================== HBM (my estimates) ===================
H = sheet("HBM", "HBM: how much of the memory business (my estimates; Samsung does not disclose HBM revenue)", [46, 12, 12, 12, 60])
head(H, 4, ["", "2025", "2026E", "2027E", "Basis"])
H["A5"] = "Industry HBM, US$bn"
for L, v in zip("BCD", HBM_TAM):
    put(H, f"{L}5", v, TN1, mine=True)
H["E5"] = "Micron's path (about 35 in 2025, about 40% a year), as in my Micron and SK Hynix notes"
H["A6"] = "Samsung share of 2025 HBM (IDC)"; put(H, "B6", IDC_SAM_25, PCT1, inp=True)
H["E6"] = "IDC as quoted in SK hynix's prospectus, 10 Jul 2026: SK hynix 63.2%, Samsung 19.3%, Micron 17.4% (2025)"
H["A7"] = "IDC, 1Q 2026: SK hynix, Samsung, Micron"; H["B7"] = "56.4%, 20.5%, 23.1%"
H["A8"] = "Samsung growth in 2026 (Samsung: more than triple)"; put(H, "C8", 3.2, X1, mine=True)
H["A9"] = "Samsung 2027 share (share in line with DRAM share)"; put(H, "D9", 0.35, PCT0, mine=True)
H["A10"] = "Samsung HBM, US$bn"; put(H, "B10", "=B5*B6", TN1); put(H, "C10", "=B10*C8", TN1); put(H, "D10", "=D5*D9", TN1)
H["A11"] = "Average KRW per US$"
for L, v in zip("BC", HBM_FX[:2]):
    put(H, f"{L}11", v, N0, mine=True)
put(H, "D11", f"={N['fx']}", TN2)
H["A12"] = "Samsung HBM, KRW tn"
for L in "BCD":
    put(H, f"{L}12", f"={L}10*{L}11/1000", TN1)
H["A13"] = "Memory sales"; put(H, "B13", "=Financials!B5", TN1); put(H, "C13", "=Financials!C5", TN1); put(H, "D13", "=Financials!D5", TN1)
H["A14"] = "HBM share of memory sales"
for L in "BCD":
    put(H, f"{L}14", f"={L}12/{L}13", PCT1)
H["A15"] = "Implied Samsung share of 2026 industry"; put(H, "C15", "=C10/C5", PCT0)
H["E15"] = "With SK Hynix at 55% in my SK Hynix note and Micron about a fifth, the 2026 shares sum to more than 100%; disclosed in the note."

# =================== Valuation (base) ===================
V = sheet("Valuation", "Valuation: sum of the parts at October 2027 (base case)", [52, 16, 16, 50])
head(V, 4, ["", "KRW tn", "KRW per share", "Basis"])
nm_rev = f"{N['mem_base']}*(1+{N['bits']})^{N['years']}*{N['pf']}"
V["A5"] = "Normal memory sales"; put(V, "B5", f"={nm_rev}", TN1)
V["A6"] = "Normal memory after-tax profit"; put(V, "B6", f"=B5*{N['nm']}", TN1)
V["A7"] = "Net cash, Sep 2027"; put(V, "B7", "=Financials!D23", TN1)
V["A8"] = "Memory above normal"
put(V, "B8", f"={N['w0']}*(Financials!D18-B6)+{N['w1']}*(Financials!E18-B6)/(1+{N['rate']})+{N['w2']}*(Financials!E18-B6)/(1+{N['rate']})^2", TN1)
V["A9"] = "Memory, multiple of normal"; put(V, "B9", f"=B6*{N['mult']}", TN1)
V["A10"] = "Foundry and System LSI"; put(V, "B10", f"={N['fdy_rev']}*{N['fdy_x']}", TN1)
V["A11"] = "Phones (MX/NW)"; put(V, "B11", f"={N['mx_op']}*(1-{t})*{N['mx_x']}", TN1)
V["A12"] = "VD/DA"; put(V, "B12", f"={N['vd_op']}*(1-{t})*{N['vd_x']}", TN1)
V["A13"] = "Samsung Display"; put(V, "B13", f"={N['sdc_op']}*(1-{t})*{N['sdc_x']}", TN1)
V["A14"] = "Harman"; put(V, "B14", f"={N['har_op']}*(1-{t})*{N['har_x']}", TN1)
V["A15"] = "Investments"; put(V, "B15", f"={N['invest']}*(1-{N['inv_cut']})", TN1)
V["A16"] = "Gross"; put(V, "B16", "=SUM(B7:B15)", TN1)
V["A17"] = "Less discount"; put(V, "B17", f"=-B16*{N['disc']}", TN1)
V["A18"] = "Base value"; put(V, "B18", "=B16+B17", TN1)
for rr in range(7, 19):
    put(V, f"C{rr}", f"=B{rr}/{N['sh']}*1E6", N0)
V["A18"].font = F_B; V["C18"].fill = FILL_KEY
V["A19"] = "Base value vs common price"; put(V, "C19", f"=C18/{N['price']}-1", PCT1)
V["A20"] = "Base value vs preferred price"; put(V, "C20", f"=C18/{N['price_p']}-1", PCT1)
V["A21"] = "Band (long >= 15% above, short >= 25% below)"; put(V, "C21", '=IF(C19>=0.15,"LONG",IF(C19<=-0.25,"SHORT","NO CALL"))')
V["A22"] = "Draft view"; put(V, "C22", CALL["direction"], inp=True)
V["A23"] = "Target, KRW"; put(V, "C23", CALL["target"], N0, inp=True)
V["A24"] = "Price above which back to no call"; put(V, "C24", "=C18/1.15", N0)
V["A25"] = "Base without the net cash"; put(V, "C25", f"=(B16-B7)*(1-{N['disc']})/{N['sh']}*1E6", N0)
V["A26"] = "Base without the net cash vs price"; put(V, "C26", f"=C25/{N['price']}-1", PCT1)
V["A28"] = "What the market value needs (normal memory after-tax profit)"
k = f"({N['w0']}+{N['w1']}/(1+{N['rate']})+{N['w2']}/(1+{N['rate']})^2)"
c = f"({N['w0']}*Financials!D18+({N['w1']}/(1+{N['rate']})+{N['w2']}/(1+{N['rate']})^2)*Financials!E18)"
rest = "SUM(B10:B15)"
V["A29"] = "No discount, cash kept"; put(V, "B29", f"=({N['mcap']}-B7-{rest}-{c})/({N['mult']}-{k})", TN1); put(V, "C29", "=B29/B5", PCT1)
V["A30"] = "My discount, cash kept"; put(V, "B30", f"=({N['mcap']}/(1-{N['disc']})-B7-{rest}-{c})/({N['mult']}-{k})", TN1); put(V, "C30", "=B30/B5", PCT1)
V["A31"] = "My discount, cash spent"; put(V, "B31", f"=({N['mcap']}/(1-{N['disc']})-{rest}-{c})/({N['mult']}-{k})", TN1); put(V, "C31", "=B31/B5", PCT1)
V["D29"] = "Column C: as a net margin on normal memory sales"; V["D29"].font = F_NOTE
V["A33"] = "Discount sensitivity (value per share)"
for j, d in enumerate([0, 0.1, 0.2, 0.3]):
    V.cell(row=34 + j, column=1, value=f"Discount {int(d * 100)}%")
    put(V, f"C{34 + j}", f"=B16*(1-{d})/{N['sh']}*1E6", N0)

# =================== Scenarios ===================
S = sheet("Scenarios", "Scenarios: three cases, twelve months out", [44, 14, 14, 14])
head(S, 4, ["", "Bear", "Base", "Bull"])
srow = [("Revenue per bit, share of base", 1, PCT0), ("Normal memory net margin", 2, PCT0), ("Multiple on normal", 3, '0"x"'),
        ("2027 memory sales", 4, TN1), ("2027 memory operating margin", 5, PCT0), ("2028 memory sales change", 6, PCT0),
        ("2028 memory operating margin", 7, PCT0)]
for i, (lab, idx, fmt) in enumerate(srow, 5):
    S.cell(row=i, column=1, value=lab)
    for j, s in enumerate(SCEN):
        L = "BCD"[j]
        if j == 1:
            src = {1: 'pf', 2: 'nm', 3: 'mult', 4: 'mem27', 5: 'mopm27', 6: 'g28', 7: 'mopm28'}[idx]
            put(S, f"{L}{i}", f"={N[src]}", fmt)
        else:
            put(S, f"{L}{i}", s[idx], fmt, mine=True)
S["A12"] = "Weights: Q4 2027, 2028, 2029"
for j, s in enumerate(SCEN):
    L = "BCD"[j]
    for m, w in enumerate(s[8]):
        put(S, f"{L}{13 + m}", f"={N['w' + str(m)]}" if j == 1 else w, TN2, mine=(j != 1))
S["A13"] = "  Q4 2027 share of 2027 excess"; S["A14"] = "  2028 excess"; S["A15"] = "  2029 (share of 2028 excess)"
S["A16"] = "Probability"
for j, s in enumerate(SCEN):
    put(S, f"{'BCD'[j]}16", s[9], PCT0, mine=True)
calc = ["Memory after-tax 2027", "Memory after-tax 2028", "Net profit 2027", "EPS 2027, KRW", "Free cash flow 2027", "Net cash Sep 2027",
        "Normal memory sales", "Normal memory after-tax profit", "Memory above normal", "Memory, multiple of normal", "Gross",
        "Value per share, KRW", "Change vs price"]
for i, lab in enumerate(calc, 18):
    S.cell(row=i, column=1, value=lab)
for j in range(3):
    L = "BCD"[j]
    put(S, f"{L}18", f"={L}8*{L}9*(1-{t})", TN1)
    put(S, f"{L}19", f"={L}8*(1+{L}10)*{L}11*(1-{t})", TN1)
    put(S, f"{L}20", f"=({L}8*{L}9+{N['oth_op27']})*(1-{t})", TN1)
    put(S, f"{L}21", f"={L}20/{N['sh']}*1E6", N0)
    put(S, f"{L}22", f"={L}20+{N['da27']}-{N['capex27']}-{N['wc27']}", TN1)
    put(S, f"{L}23", f"=Financials!C22+Financials!C21+0.75*{L}22", TN1)
    put(S, f"{L}24", f"={N['mem_base']}*(1+{N['bits']})^{N['years']}*{L}5", TN1)
    put(S, f"{L}25", f"={L}24*{L}6", TN1)
    put(S, f"{L}26", f"={L}13*({L}18-{L}25)+{L}14*({L}19-{L}25)/(1+{N['rate']})+{L}15*({L}19-{L}25)/(1+{N['rate']})^2", TN1)
    put(S, f"{L}27", f"={L}25*{L}7", TN1)
    put(S, f"{L}28", f"={L}23+{L}26+{L}27+SUM(Valuation!$B$10:$B$15)", TN1)
    put(S, f"{L}29", f"={L}28*(1-{N['disc']})/{N['sh']}*1E6", N0)
    put(S, f"{L}30", f"={L}29/{N['price']}-1", PCT1)
S["A32"] = "Probability-weighted value, KRW"; put(S, "B32", "=SUMPRODUCT(B29:D29,B16:D16)", N0)
S["A33"] = "Weighted vs price"; put(S, "B33", f"=B32/{N['price']}-1", PCT1)

# =================== Sensitivity ===================
G = sheet("Sensitivity", "Sensitivity: normal memory net margin (rows) against the multiple on normal earnings (columns); discount fixed", [30, 14, 14, 14])
head(G, 4, ["Normal net margin", f"{SENS_X[0]}x", f"{SENS_X[1]}x", f"{SENS_X[2]}x"])
for j, x in enumerate(SENS_X):
    put(G, f"{'BCD'[j]}3", x, '0"x"', inp=True)
for i, m in enumerate(SENS_NM):
    rr = 5 + i
    put(G, f"A{rr}", m, PCT0, inp=True)
    for j in range(3):
        L = "BCD"[j]
        n = f"(Valuation!$B$5*$A{rr})"
        exc = (f"({N['w0']}*(Financials!$D$18-{n})+{N['w1']}*(Financials!$E$18-{n})/(1+{N['rate']})"
               f"+{N['w2']}*(Financials!$E$18-{n})/(1+{N['rate']})^2)")
        put(G, f"{L}{rr}", f"=(Valuation!$B$7+{exc}+{n}*{L}$3+SUM(Valuation!$B$10:$B$15))*(1-{N['disc']})/{N['sh']}*1E6", N0)
G["A9"] = "Cells above the price"; put(G, "B9", f'=COUNTIF(B5:D7,">"&{N["price"]})', N0)
G["A10"] = "Lowest cell vs price"; put(G, "B10", f"=MIN(B5:D7)/{N['price']}-1", PCT1)

# =================== Peers ===================
Pe = sheet("Peers", "Peers: price over consensus EPS for the year ending in 2027 (stockanalysis.com, 2 Nov 2026)", [26, 16, 14, 14, 18, 12])
head(Pe, 4, ["Company", "Listing", "Price", "Consensus EPS", "Year", "P/E"])
Pe["A5"] = "Samsung Electronics"; Pe["B5"] = "KRX: 005930"; put(Pe, "C5", f"={N['price']}", N0); put(Pe, "D5", f"={N['cons27']}", N0); Pe["E5"] = "CY2027"
for i, (c_, l_, px, e, y, d) in enumerate(PEERS, 6):
    Pe[f"A{i}"] = c_; Pe[f"B{i}"] = l_; put(Pe, f"C{i}", px, TN2, inp=True); put(Pe, f"D{i}", e, TN2, inp=True); Pe[f"E{i}"] = y
for i in (5, 6, 7):
    put(Pe, f"F{i}", f"=C{i}/D{i}", X1)
Pe["A9"] = "Multiples only; no view on the peers' shares. Micron's price is the Nasdaq close of 30 October 2026."; Pe["A9"].font = F_NOTE

# =================== History ===================
Hs = sheet("History", "History: chip division (DS) sales and operating profit, 2017 to 2025 (Samsung fourth quarter decks)", [20, 14, 14, 14])
head(Hs, 4, ["Year", "DS sales", "DS operating profit", "Margin"])
for i, (y, rv, op) in enumerate(zip(DS_YRS, DS_REV, DS_OP), 5):
    Hs[f"A{i}"] = y; put(Hs, f"B{i}", rv, TN2, inp=True); put(Hs, f"C{i}", op, TN2, inp=True); put(Hs, f"D{i}", f"=C{i}/B{i}", PCT1)
e = 5 + len(DS_YRS)
Hs[f"A{e}"] = "2017 to 2025"; put(Hs, f"B{e}", f"=SUM(B5:B{e - 1})", TN1); put(Hs, f"C{e}", f"=SUM(C5:C{e - 1})", TN1); put(Hs, f"D{e}", f"=C{e}/B{e}", PCT1)

wb.save(XLSX)
print("model written", XLSX)
