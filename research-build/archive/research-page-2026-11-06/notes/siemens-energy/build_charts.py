"""Charts for the Siemens Energy initiation. House style: navy / light blue, red reference lines, grey price line."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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


# ---- 1. Grid Technologies revenue and margin, FY22 to FY27E ----
years = GT_YEARS + ["FY26E*", "FY27E*"]
rev = GT_REV_HIST + [REV26["GT"] / 1000, REV27["GT"] / 1000]
mar = [m * 100 for m in GT_M_HIST] + [M26["GT"] * 100, M27["GT"] * 100]
x = list(range(len(years)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY] * 4 + [LIGHT_BLUE, PALE], edgecolor=[NAVY] * 6, linewidth=0.6, width=0.6, zorder=3,
        label="Revenue, €bn")
for i, r in enumerate(rev):
    ax1.annotate(f"{r:.1f}", (i, r), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6,
                 color=NAVY, fontweight="bold")
ax1.set_ylim(0, 30); ax1.set_ylabel("Revenue (€bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(x); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(x, mar, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Margin before special items, % (RHS)")
for i, m in enumerate(mar):
    ax2.annotate(f"{m:.1f}%", (i, m), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=6.2,
                 color=RED, fontweight="bold")
ax2.axhspan(18, 20, color=RED, alpha=0.07, zorder=1)
ax2.set_ylim(-25, 28); ax2.set_yticks([0, 10, 20]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.6, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in SENS); ghi = max(max(r) for r in SENS)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nGrid {SENS_GT_X[0]} to {SENS_GT_X[2]}x, Gas {SENS_GS_X[0]} to {SENS_GS_X[2]}x", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: sum of the parts,\nGrid {MULT['GT']}x, Gas Services {MULT['GS']}x", "point", base),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"€{v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"€{lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"€{hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 2, len(rows) - 0.42, f"Price €{PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.6)
ax.set_xlabel("Value per share (€)", fontsize=8)
ax.set_xlim(0, 260); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. The pile: Grid orders against revenue by quarter ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
xs = list(range(len(GT_Q_LABELS)))
w = 0.38
ax.bar([i - w / 2 for i in xs], [o / 1000 for o in GT_Q_ORD], width=w, color=NAVY, zorder=3, label="Orders")
ax.bar([i + w / 2 for i in xs], [r / 1000 for r in GT_Q_REV], width=w, color=LIGHT_BLUE, zorder=3, label="Revenue")
for i, (o, r) in enumerate(zip(GT_Q_ORD, GT_Q_REV)):
    ax.annotate(f"{o / r:.2f}x", (i, o / 1000), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.2, color=RED, fontweight="bold")
ax.set_xticks(xs); ax.set_xticklabels([l.replace(" ", "\n") for l in GT_Q_LABELS], fontsize=6.6)
ax.set_ylim(0, 9); ax.set_ylabel("€bn", fontsize=8)
ax.legend(loc="upper left", fontsize=6.6, frameon=False, ncol=2, bbox_to_anchor=(-0.02, 1.13))
ax.text(6.4, 8.6, "Red: orders / revenue in the quarter", fontsize=6.2, color=RED, ha="right", va="top")
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_queue")

# ---- 4. Sum of the parts, EUR per share ----
parts = [("Grid Technologies", SOTP["GT"]), ("Gas Services", SOTP["GS"]), ("Transformation\nof Industry", SOTP["TI"]),
         ("Siemens Gamesa,\nless cash burn", SOTP["SG"]), ("Corporate costs", SOTP["Corp"]),
         ("Net cash, investments\nless minorities", BRIDGE)]
ps = [(n, v / SHARES * 1000) for n, v in parts]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
left = 0
for i, (n, v) in enumerate(ps):
    col = NAVY if i == 0 else (RED if v < 0 else LIGHT_BLUE)
    ax.barh(len(ps) - 1 - i, v, left=left if v >= 0 else left + v, height=0.6, color=col, zorder=3)
    ax.annotate(f"€{v:,.0f}" if v >= 0 else f"less €{-v:,.0f}", (left + max(v, 0), len(ps) - 1 - i), xytext=(4, 0),
                textcoords="offset points", ha="left", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
    left += v
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(PRICE - 2, -0.75, f"Price €{PRICE:,.0f}", fontsize=6.6, color=RED, ha="right", va="center")
ax.axvline(BASE_VALUE, color=NAVY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(BASE_VALUE + 2, -0.75, f"Base €{BASE_VALUE:,.0f}", fontsize=6.6, color=NAVY, ha="left", va="center")
ax.set_yticks(range(len(ps))); ax.set_yticklabels([n for n, _ in ps][::-1], fontsize=6.4)
ax.set_xlim(0, 215); ax.set_ylim(-1.2, len(ps) - 0.4); ax.set_xlabel("Cumulative value per share (€)", fontsize=8)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_sotp")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 3, f"My base value €{BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"€{PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 6, 60), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 200); ax.set_ylabel("Close (€)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
