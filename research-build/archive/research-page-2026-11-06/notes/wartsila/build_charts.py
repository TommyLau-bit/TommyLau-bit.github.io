"""Charts for the Wärtsilä initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Energy orders against net sales by quarter, with the order book ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
xs = list(range(len(EN_Q_LABELS)))
w = 0.38
ax.bar([i - w / 2 for i in xs], [o / 1000 for o in EN_Q_ORD], width=w, color=NAVY, zorder=3, label="Orders")
ax.bar([i + w / 2 for i in xs], [r / 1000 for r in EN_Q_REV], width=w, color=LIGHT_BLUE, zorder=3, label="Net sales")
for i, (o, r) in enumerate(zip(EN_Q_ORD, EN_Q_REV)):
    ax.annotate(f"{o / r:.2f}x", (i - w / 2, o / 1000), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.0, color=RED, fontweight="bold")
ax.set_xticks(xs); ax.set_xticklabels([l.replace(" ", "\n") for l in EN_Q_LABELS], fontsize=6.6)
ax.set_ylim(0, 2.2); ax.set_ylabel("€bn", fontsize=8)
ax2 = ax.twinx()
ax2.plot(xs, [b / 1000 for b in EN_Q_BOOK], color=GRAY, marker="o", markersize=3, linewidth=1.4, zorder=4, label="Order book (RHS)")
ax2.annotate(f"€{EN_Q_BOOK[-1] / 1000:.1f}bn", (xs[-1], EN_Q_BOOK[-1] / 1000), xytext=(-4, 4), textcoords="offset points",
             ha="right", va="bottom", fontsize=6.4, color=GRAY, fontweight="bold")
ax2.set_ylim(0, 6.6); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, ncol=3, bbox_to_anchor=(-0.02, 1.15))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_energy")

# ---- 2. Energy MW ordered: named data centre orders against the rest ----
labels = ["FY 2025", "Q1 26", "Q2 26", "Q3 26"]
tot = [EN_MW_25] + EN_Q_MW[4:]
dc = [DC_MW_25] + list(DC_MW_Q.values())
rest = [t - d for t, d in zip(tot, dc)]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
xs = list(range(len(labels)))
ax.bar(xs, dc, width=0.55, color=NAVY, zorder=3, label="Named data centre orders")
ax.bar(xs, rest, bottom=dc, width=0.55, color=PALE, edgecolor=NAVY, linewidth=0.5, zorder=3, label="Other (balancing, baseload)")
for i, (t, d) in enumerate(zip(tot, dc)):
    ax.annotate(f"{t:,} MW", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6,
                color=NAVY, fontweight="bold")
    ax.annotate(f"{d / t * 100:.0f}%", (i, d / 2), ha="center", va="center", fontsize=6.6, color="white", fontweight="bold")
ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=7)
ax.set_ylim(0, 2900); ax.set_ylabel("MW ordered", fontsize=8)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, ncol=2, bbox_to_anchor=(-0.02, 1.15))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_dc")

# ---- 3. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in SENS); ghi = max(max(r) for r in SENS)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nEnergy {SENS_EN_X[0]} to {SENS_EN_X[2]}x, Marine {SENS_MA_X[0]} to {SENS_MA_X[2]}x", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: sum of the parts,\nEnergy {MULT['EN']}x, Marine {MULT['MA']}x", "point", base),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"€{v:,.2f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"€{lo:,.2f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"€{hi:,.2f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 0.3, len(rows) - 0.42, f"Price €{PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.6)
ax.set_xlabel("Value per share (€)", fontsize=8)
ax.set_xlim(0, 46); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 4. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 0.6, f"My base value €{BASE_VALUE:,.2f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"€{PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 6, 12), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 45); ax.set_ylabel("Close (€)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
