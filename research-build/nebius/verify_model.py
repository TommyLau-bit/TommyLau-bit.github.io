"""Check the LibreOffice-recalculated model against the Python mirror in nebius_data.py.

Usage: python3 verify_model.py <recalculated.xlsx>
"""
import sys
import openpyxl
import nebius_data as D

wb = openpyxl.load_workbook(sys.argv[1], data_only=True)
errs = []
for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and c.value.startswith("#"):
                errs.append(f"{ws.title}!{c.coordinate}={c.value}")
            if c.value is None:
                continue

dep, ue = D.unit_econ()
b = D.share_bridge()
m = D.multiples()
scen, wv, wc = D.scenarios()
sens = D.sensitivity()

checks = [
    ("UnitEcon", "B9", dep),
    *[("UnitEcon", f"C{13+i}", ue[i][2]) for i in range(3)],
    *[("UnitEcon", f"D{13+i}", ue[i][3]) for i in range(3)],
    *[("UnitEcon", f"E{13+i}", ue[i][4]) for i in range(3)],
    ("CapStructure", "C25", b["total"]),
    ("CapStructure", "C32", b["debt_stays"]),
    ("CapStructure", "C33", b["equity"]),
    ("CapStructure", "C36", b["ev"]),
    ("Valuation", "B10", m["ev_ebitda_r"]),
    ("Valuation", "B11", m["ev_ebitda"]),
    ("Valuation", "B12", m["ev_rev"]),
    *[("Scenarios", f"J{5+i}", scen[i][9]) for i in range(3)],
    *[("Scenarios", f"K{5+i}", scen[i][10]) for i in range(3)],
    ("Scenarios", "J8", wv),
    ("Scenarios", "K8", wc),
    *[("Sensitivity", f"{'BCD'[j]}{7+i}", sens[i][j]) for i in range(3) for j in range(3)],
    ("ARR_Recon", "B13", 7000 / 12), ("ARR_Recon", "C13", 750.0), ("ARR_Recon", "B20", 1250 / 170),
    ("ARR_Recon", "B7", 16.0), ("ARR_Recon", "C7", 20.0),
]
bad = 0
for sh, cell, exp in checks:
    got = wb[sh][cell].value
    ok = isinstance(got, (int, float)) and abs(got - exp) < 1e-6 * max(1, abs(exp))
    if not ok:
        bad += 1
    print(f"{'OK ' if ok else 'BAD'} {sh}!{cell}: model={got} python={exp}")

print("\nKey outputs:")
for sh, cell, lbl in [("CapStructure", "C25", "If-converted shares, m"), ("CapStructure", "C33", "Equity value, US$m"),
                      ("CapStructure", "C36", "EV, US$m"), ("Valuation", "B10", "EV/2027 EBITDA (pitch basis)"),
                      ("Valuation", "B12", "EV/2027 revenue"), ("Scenarios", "J5", "Bear"), ("Scenarios", "J6", "Base"),
                      ("Scenarios", "J7", "Bull"), ("Scenarios", "J8", "Weighted"), ("Scenarios", "K8", "Weighted change"),
                      ("Quarterly", "B15", "H2 ARR multiple to guide low"), ("Quarterly", "B18", "H2 capex low"),
                      ("Quarterly", "B19", "H2 capex high"), ("UnitEcon", "B24", "5 GW build, US$bn"),
                      ("CapStructure", "C42", "Cash sum before fees")]:
    print(f"  {lbl}: {wb[sh][cell].value}")
print("\nFormula errors:", errs or "none")
print("Mismatches:", bad)
sys.exit(1 if (bad or errs) else 0)
