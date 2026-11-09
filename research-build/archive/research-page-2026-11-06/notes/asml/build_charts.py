"""Charts for the ASML initiation. House style: navy / light blue, red reference lines, grey price line."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from data import *

plt.rcParams["font.family"] = "Arial"
NAVY = "#1F3864"; LIGHT_BLUE = "#8FAADC"; PALE = "#C9D6EF"; RED = "#C00000"; GRAY = "#7F7F7F"; GRID = "#E3E3E3"
D = BUILD_DIR
SIZE = (4.7, 2.15)


def style(ax):
    ax.tick_params(axis="both", labelsize=7.4, length=0)
    ax.set_axisbelow(True)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#B0B0B0")


def save(name):
    plt.tight_layout(); plt.savefig(f"{D}/{name}.png", bbox_inches="tight"); plt.close()


# ---- 1. EUV units: sold, then low NA capacity ----
labs = [y for y, _ in EUV_UNITS_SOLD] + ["H1 26", "2026", "2027", "2028"]
vals = [u for _, u in EUV_UNITS_SOLD] + [EUV_UNITS_H126, CAP["c26"], CAP["c27"], CAP["c28"]]
cols = [NAVY] * 6 + [PALE, LIGHT_BLUE, LIGHT_BLUE, "white"]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(range(len(labs)), vals, color=cols, edgecolor=NAVY, linewidth=0.6, width=0.62, zorder=3)
bars[-1].set_hatch("////"); bars[-1].set_edgecolor(LIGHT_BLUE)
for b, v in zip(bars, vals):
    ax.annotate(f"{v}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.4, color=NAVY, fontweight="bold")
ax.plot([9], [LNA_U[2]], marker="D", color=RED, markersize=4, zorder=5, linestyle="none")
ax.annotate(f"My base\n2028: {LNA_U[2]}", (9, LNA_U[2]), xytext=(9, 60), textcoords="data", ha="center", va="center", fontsize=5.8, color=RED,
            bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none"))
ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, fontsize=6.8)
ax.set_ylim(0, 128); ax.set_ylabel("EUV systems", fontsize=8)
ax.legend(handles=[Patch(color=NAVY, label="Recognised in sales (incl. High NA)"), Patch(facecolor=PALE, edgecolor=NAVY, linewidth=0.5, label="H1 2026"),
                   Patch(color=LIGHT_BLUE, label="Low NA capacity / plan"), Patch(facecolor="white", edgecolor=LIGHT_BLUE, hatch="////", label="Investigating")],
          loc="upper left", fontsize=5.9, frameon=False, bbox_to_anchor=(-0.02, 1.24), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_units")

# ---- 2. Revenue by segment, 2023 to 2028E, against the 2030 range ----
years = ["2023", "2024", "2025", "2026E*", "2027E*", "2028E*"]
euv = [e / 1000 for e in EUV_H] + [y["euv"] / 1000 for y in M]
non = [n / 1000 for n in NONEUV_H] + [y["noneuv"] / 1000 for y in M]
ibm = [i / 1000 for i in IBM_H] + [y["ibm"] / 1000 for y in M]
x = range(len(years))
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(x, euv, color=NAVY, width=0.6, zorder=3, label="EUV systems (low and High NA)")
ax.bar(x, non, bottom=euv, color=LIGHT_BLUE, width=0.6, zorder=3, label="DUV and metrology systems")
ax.bar(x, ibm, bottom=[a + b for a, b in zip(euv, non)], color=PALE, edgecolor=NAVY, linewidth=0.4, width=0.6, zorder=3, label="Installed Base Management")
for i in x:
    t = euv[i] + non[i] + ibm[i]
    ax.annotate(f"{t:.1f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
for v, lab in [(44, "2030 low scenario EUR 44bn"), (60, "2030 high scenario EUR 60bn")]:
    ax.axhline(v, color=RED, linestyle="--", linewidth=1.0, zorder=4)
    ax.text(-0.42, v + 0.8, lab, fontsize=5.9, color=RED, ha="left", va="bottom")
ax.set_ylim(0, 74); ax.set_ylabel("Total net sales (EUR bn)", fontsize=8)
ax.set_xticks(list(x)); ax.set_xticklabels(years, fontsize=7)
ax.legend(loc="upper left", fontsize=5.9, frameon=False, bbox_to_anchor=(-0.02, 1.24), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_mix")

# ---- 3. Quarterly: systems and Installed Base Management, with gross margin ----
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
xs = range(len(QL))
sysv = [(s / 1000 if s else (Q_REV[-1] - Q_IBM[-1]) / 1000) for s in Q_SYS]
ib = [i / 1000 for i in Q_IBM]
ax1.bar(xs, sysv, color=[NAVY] * 5 + [LIGHT_BLUE], width=0.6, zorder=3, label="Net system sales")
ax1.bar(xs, ib, bottom=sysv, color=[PALE] * 5 + ["white"], edgecolor=NAVY, linewidth=0.5, width=0.6, zorder=3, label="Installed Base Management")
for i in xs:
    ax1.annotate(f"{ib[i]:.2f}", (i, sysv[i] + ib[i] / 2), ha="center", va="center", fontsize=6.0, color=NAVY, fontweight="bold")
    ax1.annotate(f"{sysv[i] + ib[i]:.1f}", (i, sysv[i] + ib[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=NAVY)
ax1.set_ylim(0, 15.5); ax1.set_ylabel("EUR bn", fontsize=8)
ax1.set_xticks(list(xs)); ax1.set_xticklabels(QL, fontsize=6.6)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax2 = ax1.twinx()
ax2.plot(list(xs), [g * 100 for g in Q_GM], color=RED, marker="o", markersize=3.2, linewidth=1.4, zorder=5, label="Gross margin % (RHS)")
for i, g in enumerate(Q_GM):
    ax2.annotate(f"{g * 100:.1f}" if i < 5 else "55-57", (i, g * 100), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=5.8, color=RED)
ax2.set_ylim(30, 60); ax2.tick_params(axis="y", labelsize=7.2, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=5.9, frameon=False, bbox_to_anchor=(-0.02, 1.22), ncol=3)
save("chart_quarters")

# ---- 4. China share of total net sales ----
labs = ["2023", "2024", "2025", "2026 guide"]
vals = [c * 100 for c in CHINA_SH] + [G26["china"] * 100]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(range(4), vals, color=[NAVY, NAVY, NAVY, LIGHT_BLUE], width=0.55, zorder=3)
for b, v, c in zip(bars, vals, CHINA_H + [None]):
    t = f"{v:.1f}%" + (f"\nEUR {c / 1000:.1f}bn" if c else "\nabout")
    ax.annotate(t, (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=NAVY, fontweight="bold")
ax.set_xticks(range(4)); ax.set_xticklabels(labs, fontsize=7)
ax.set_ylim(0, 47); ax.set_ylabel("China, % of total net sales", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_china")

# ---- 5. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in VGRID); ghi = max(max(r) for r in VGRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_U[0]}-{SENS_U[2]} units, {SENS_X[0]}-{SENS_X[2]}x", "range", (glo, ghi)),
    ("DCF, 95% cash\nconversion", "point", DCF_VALUE),
    ("DCF, 115% cash\nconversion (2025)", "point", DCF_VALUE_HIST),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base\n{MULT}x 2028E", "point", base),
    ("Average analyst target\n(ADR, in EUR)", "point", CONS_TP_USD / EURUSD),
]
fig, ax = plt.subplots(figsize=(4.7, 2.6), dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"EUR {v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"EUR {lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
        ax.annotate(f"EUR {hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE - 20, len(rows) - 0.42, f"Price EUR {PRICE:,.2f}", fontsize=6.6, color=RED, ha="right", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=5.8)
ax.set_xlabel("Value per share (EUR)", fontsize=8)
ax.set_xlim(500, 2600); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 25, f"My base value EUR {BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"EUR {PX[-1]:,.2f}\n6 Oct 2026", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 5.5, 850), textcoords="data", ha="right",
            va="center", fontsize=6.6, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 4))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(400, 1950); ax.set_ylabel("Close (EUR)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
