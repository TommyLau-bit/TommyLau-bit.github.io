"""Charts for the Vertiv initiation. House style: navy / light blue, red TP line, grey price line."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from data import *

plt.rcParams["font.family"] = "Arial"
NAVY = "#1F3864"; LIGHT_BLUE = "#8FAADC"; RED = "#C00000"; GRAY = "#7F7F7F"; GRID = "#E3E3E3"
D = BUILD_DIR


def style(ax):
    ax.tick_params(axis="both", labelsize=7.6, length=0)
    ax.set_axisbelow(True)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#B0B0B0")


# ---- 1. Annual sales + adjusted operating margin ----
years = ["2024A", "2025A", "2026 guide", "2027E*", "2028E*"]
sales = [SALES["2024A"], SALES["2025A"], G_SALES_MID, S27, S28]
marg = [MARGIN["2024A"] * 100, MARGIN["2025A"] * 100, G_M_MID * 100, M27 * 100, M28 * 100]
fig, ax1 = plt.subplots(figsize=(4.7, 2.15), dpi=220)
cols = [NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE, LIGHT_BLUE]
bars = ax1.bar(years, sales, color=cols, width=0.52, zorder=3, label="Net sales, US$bn")
ax1.set_ylabel("Net sales (US$bn)", fontsize=8)
ax1.set_ylim(0, 38)
ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
style(ax1)
for b, v in zip(bars, sales):
    ax1.annotate(f"{v:.2f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 3), textcoords="offset points",
                 ha="center", va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax2 = ax1.twinx()
ax2.plot(years, marg, color=RED, marker="o", markersize=4, linewidth=1.8, zorder=4, label="Adj. operating margin (RHS)")
ax2.set_ylim(0, 30)
ax2.set_ylabel("Adj. op. margin (%, RHS)", fontsize=8)
ax2.tick_params(axis="y", labelsize=7.6, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
for x, m in zip(years, marg):
    ax2.annotate(f"{m:.1f}%", (x, m), xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.6, color=RED, fontweight="bold")
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=7.2, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
plt.tight_layout(); plt.savefig(f"{D}/chart_annual.png", bbox_inches="tight"); plt.close()

# ---- 2. Valuation cross-check ----
bear = SCEN[0][4] * project(*SCEN[0][1:4])[3]
bull = SCEN[2][4] * project(*SCEN[2][1:4])[3]
base = BASE_PE * E28
wtd = sum(p * mult * project(g1, g2, m)[3] for _, g1, g2, m, mult, p in SCEN)
rows = [  # label, kind, values
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    ("Sensitivity grid\n24 to 32x, EPS 9.50 to 11.50", "range", (9.50 * 24, 11.50 * 32)),
    ("Probability-weighted\n25 / 50 / 25", "point", wtd),
    ("Base: 28x 2028E EPS\nof US$10.65", "point", base),
]
fig, ax = plt.subplots(figsize=(4.7, 2.15), dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"US${v:.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color="#C9D6EF", edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=GRAY, linestyle="--", linewidth=1.3, zorder=4)
ax.axvline(TARGET, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE - 3, len(rows) - 0.42, f"Price US${PRICE:.2f}", fontsize=7, color=GRAY, ha="right", va="bottom")
ax.text(TARGET + 3, len(rows) - 0.42, f"TP US${TARGET:.0f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=7)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 460); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
style(ax)
plt.tight_layout(); plt.savefig(f"{D}/chart_valuation.png", bbox_inches="tight"); plt.close()

# ---- 3. Quarterly adjusted operating margin ----
fig, ax = plt.subplots(figsize=(4.7, 2.05), dpi=220)
cols = [LIGHT_BLUE] * 6 + [NAVY] * 4
bars = ax.bar(Q, Q_MARGIN, color=cols, width=0.6, zorder=3)
ax.axhline(G_M_MID * 100, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(-0.4, G_M_MID * 100 + 0.6, "2026 guide midpoint 23.8%", fontsize=6.8, color=RED, ha="left", va="bottom")
for b, v in zip(bars, Q_MARGIN):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, -3), textcoords="offset points",
                ha="center", va="top", fontsize=6.6, color="white", fontweight="bold")
ax.set_ylim(0, 29); ax.set_ylabel("Adj. operating margin (%)", fontsize=8)
ax.yaxis.set_major_locator(mticker.MultipleLocator(5))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
style(ax); ax.tick_params(axis="x", labelsize=6.8)
plt.tight_layout(); plt.savefig(f"{D}/chart_qmargin.png", bbox_inches="tight"); plt.close()

# ---- 4. Organic growth, products vs service ----
import numpy as np
x = np.arange(len(Q)); w = 0.38
fig, ax = plt.subplots(figsize=(4.7, 2.05), dpi=220)
ax.bar(x - w / 2, Q_PROD, w, color=NAVY, zorder=3, label="Products")
ax.bar(x + w / 2, Q_SERV, w, color=LIGHT_BLUE, zorder=3, label="Service and spares")
ax.set_xticks(x); ax.set_xticklabels(Q)
ax.set_ylim(0, 45); ax.set_ylabel("Organic growth y/y (%)", fontsize=8)
ax.yaxis.set_major_locator(mticker.MultipleLocator(10))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
style(ax); ax.tick_params(axis="x", labelsize=6.8)
ax.legend(loc="upper left", fontsize=7.2, frameon=False, ncol=2, bbox_to_anchor=(-0.02, 1.15))
plt.tight_layout(); plt.savefig(f"{D}/chart_mix.png", bbox_inches="tight"); plt.close()

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=(4.7, 2.05), dpi=220)
ax.plot(range(len(PX)), PX, color=NAVY, linewidth=1.8, zorder=3)
ax.axhline(TARGET, color=RED, linestyle="--", linewidth=1.2, zorder=2)
ax.text(0, TARGET + 6, f"TP US${TARGET:.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:.2f}", (len(PX) - 1, PX[-1]), xytext=(-2, -12), textcoords="offset points",
            ha="right", va="top", fontsize=6.8, color=NAVY, fontweight="bold")
ax.annotate(f"Intraday peak US${PEAK:.2f}\n14 May 2026", (28, 315.71), xytext=(-60, 30), textcoords="offset points",
            ha="right", va="center", fontsize=6.6, color=GRAY,
            arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.7))
ticks = [0, 6, 12, 18, 24, len(PX) - 1]
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks])
ax.set_ylim(0, 400); ax.set_ylabel("Month-end close (US$)", fontsize=8)
ax.yaxis.set_major_locator(mticker.MultipleLocator(100))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
style(ax); ax.tick_params(axis="x", labelsize=6.8)
plt.tight_layout(); plt.savefig(f"{D}/chart_price.png", bbox_inches="tight"); plt.close()
print("charts done; base", round(base, 2), "wtd", round(wtd, 2), "bear", round(bear, 2), "bull", round(bull, 2))
