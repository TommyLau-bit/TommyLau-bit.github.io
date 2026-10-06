"""Charts for the TSMC initiation. House style: navy / light blue, red reference lines, grey price line."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from data import *

plt.rcParams["font.family"] = "Arial"
NAVY = "#1F3864"; LIGHT_BLUE = "#8FAADC"; RED = "#C00000"; GRAY = "#7F7F7F"; GRID = "#E3E3E3"
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


# ---- 1. Annual revenue + operating margin, 2024A to 2028E ----
years = ["2024A", "2025A", "2026E*", "2027E*", "2028E*"]
rev = [REV_USD["2024A"], REV_USD["2025A"], REV26, R27, R28]
om = [OM["2024A"] * 100, OM["2025A"] * 100, OM26 * 100, OM27 * 100, OM28 * 100]
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
bars = ax1.bar(years, rev, color=[NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE, LIGHT_BLUE], width=0.52, zorder=3,
               label="Revenue, US$bn")
ax1.set_ylabel("Revenue (US$bn)", fontsize=8); ax1.set_ylim(0, 430)
ax1.yaxis.set_major_locator(mticker.MultipleLocator(50))
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
for b, v in zip(bars, rev):
    ax1.annotate(f"{v:.0f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 3), textcoords="offset points",
                 ha="center", va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax2 = ax1.twinx()
ax2.plot(years, om, color=RED, marker="o", markersize=4, linewidth=1.8, zorder=4, label="Operating margin (RHS)")
ax2.set_ylim(-45, 66); ax2.set_ylabel("Operating margin (%, RHS)", fontsize=8)
ax2.tick_params(axis="y", labelsize=7.4, length=0); ax2.set_yticks([0, 20, 40, 60])
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
for x, m in zip(years, om):
    ax2.annotate(f"{m:.1f}%", (x, m), xytext=(0, 5), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.6, color=RED, fontweight="bold")
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=7.2, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
grid_lo = min(SENS_EPS) * min(SENS_PE); grid_hi = max(SENS_EPS) * max(SENS_PE)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    ("Sensitivity grid\n16 to 24x, EPS 20.00 to 26.00", "range", (grid_lo, grid_hi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: 20x 2028E EPS\nof US${EPS28:.2f}", "point", base),
    ("Consensus target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
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
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 6, len(rows) - 0.42, f"Price US${PRICE:.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per ADR (US$)", fontsize=8)
ax.set_xlim(0, 760); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Quarterly gross margin ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(Q, Q_GM, color=[LIGHT_BLUE] * 8 + [NAVY] * 2, width=0.6, zorder=3)
ax.axhline(56, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(-0.4, 70.5, "Dashed: TSMC's through-the-cycle floor, 56%", fontsize=6.8, color=RED, ha="left", va="bottom")
for b, v in zip(bars, Q_GM):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, 3), ha="center", va="bottom", fontsize=6.4,
                color="white", fontweight="bold")
ax.set_ylim(0, 76); ax.set_ylabel("Gross margin (%)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_qgm")

# ---- 4. HPC share ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(Q, Q_HPC, color=[LIGHT_BLUE] * 8 + [NAVY] * 2, width=0.6, zorder=3)
for b, v in zip(bars, Q_HPC):
    ax.annotate(f"{v}", (b.get_x() + b.get_width() / 2, v), xytext=(0, -3), textcoords="offset points",
                ha="center", va="top", fontsize=6.6, color="white", fontweight="bold")
ax.set_ylim(0, 75); ax.set_ylabel("HPC share of revenue (%)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_hpc")

# ---- 5. Monthly revenue ----
pace = sum(G3_REV) / 2 * G3_FX / 3
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
cols = [LIGHT_BLUE] * 18 + [NAVY] * 2
ax.bar(range(len(M_REV)), M_REV, color=cols, width=0.65, zorder=3)
ax.axhline(pace, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(-0.4, pace + 8, f"Q3 2026 guide midpoint, monthly pace NT${pace:.0f}bn", fontsize=6.8, color=RED,
        ha="left", va="bottom")
for i in (18, 19):
    ax.annotate(f"{M_REV[i]:.0f}", (i, M_REV[i]), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.6, color=NAVY, fontweight="bold")
ax.set_xticks(range(len(M_REV))); ax.set_xticklabels(M_LABELS, rotation=90, fontsize=6.4)
ax.set_ylim(0, 600); ax.set_ylabel("Revenue (NT$bn)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_monthly")

# ---- 6. ADR price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 8, f"My base value US${BASE_VALUE:.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:.2f}", (len(PX) - 1, PX[-1]), xytext=(-4, 4), textcoords="offset points", ha="right",
            va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 560); ax.set_ylabel("ADR close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
