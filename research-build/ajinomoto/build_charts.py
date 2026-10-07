"""Charts for the Ajinomoto initiation. House style: navy / light blue, red reference lines, grey price line."""

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


# ---- 1. The film's share: of sales, of profit, of value ----
rows = [
    ("Sales, FY2025", FM_SALES_SHARE[1]),
    ("Sales, FY2026 guide", FM_SALES_SHARE[2]),
    ("Business profit, FY2025*", FM_BP_SHARE_SEG[1]),
    ("Business profit, FY2026 guide*", FM_BP_SHARE_SEG[2]),
    ("Enterprise value, my base", FM_SHARE_EV_BASE),
    ("Enterprise value, at the price", FM_SHARE_EV_MKT),
]
fig, ax = plt.subplots(figsize=(4.7, 2.3), dpi=220)
for i, (lab, v) in enumerate(rows[::-1]):
    ax.barh(i, v * 100, color=NAVY, height=0.58, zorder=3)
    ax.barh(i, 100 - v * 100, left=v * 100, color=PALE, height=0.58, zorder=3)
    ax.annotate(f"{v * 100:.0f}%", (v * 100, i), xytext=(3, 0), textcoords="offset points", ha="left", va="center",
                fontsize=6.6, color=NAVY, fontweight="bold")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows[::-1]], fontsize=6.4)
ax.set_xlim(0, 100); ax.set_xlabel("Per cent of the whole", fontsize=7.5)
ax.legend(handles=[Patch(color=NAVY, label="Functional Materials (ABF film and others)"), Patch(color=PALE, label="Everything else")],
          loc="upper left", fontsize=5.9, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=2)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_share")

# ---- 2. Functional Materials by year: sales and margin ----
labs = FM_YEARS + ["FY2026 guide", "FY2026E*", "FY2027E*"]
sales = FM_SALES_H + [SALES["fm"][2], Y26["fm_sales"], Y27["fm_sales"]]
marg = FM_MARGIN_H + [BPROF["fm"][2] / SALES["fm"][2], Y26["fm_margin"], Y27["fm_margin"]]
cols = [NAVY] * 5 + [LIGHT_BLUE, "white", "white"]
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
bars = ax1.bar(range(len(labs)), sales, color=cols, edgecolor=NAVY, linewidth=0.6, width=0.62, zorder=3)
for b in bars[6:]:
    b.set_hatch("////"); b.set_edgecolor(LIGHT_BLUE)
for b, v in zip(bars, sales):
    ax1.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                 va="bottom", fontsize=6.1, color=NAVY, fontweight="bold")
ax1.set_xticks(range(len(labs))); ax1.set_xticklabels([l.replace("FY20", "FY").replace(" guide", "\nguide") for l in labs], fontsize=6.2)
ax1.set_ylim(0, 215); ax1.set_ylabel("Sales (JPY bn)", fontsize=7.5)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax2 = ax1.twinx()
ax2.plot(range(len(labs)), [m * 100 for m in marg], color=RED, marker="o", markersize=3, linewidth=1.3, zorder=5, label="Business profit margin %")
for i, m in enumerate(marg):
    ax2.annotate(f"{m * 100:.0f}", (i, m * 100), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=5.7, color=RED)
ax2.set_ylim(-75, 68); ax2.set_yticks([]); ax2.tick_params(axis="y", labelsize=7, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
ax1.legend(handles=[Patch(color=NAVY, label="Reported"), Patch(color=LIGHT_BLUE, label="Ajinomoto guide (6 Aug)"),
                    Patch(facecolor="white", edgecolor=LIGHT_BLUE, hatch="////", label="My estimate"),
                    plt.Line2D([0], [0], color=RED, marker="o", markersize=3, label="Margin %")],
           loc="upper left", fontsize=5.8, frameon=False, bbox_to_anchor=(-0.02, 1.24), ncol=4)
save("chart_fm")

# ---- 3. Functional Materials by quarter ----
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
x = range(len(FMQ_L))
ax1.bar([i - 0.18 for i in x], FMQ_SALES, width=0.36, color=NAVY, zorder=3, label="Sales")
ax1.bar([i + 0.18 for i in x], FMQ_BP, width=0.36, color=LIGHT_BLUE, zorder=3, label="Business profit")
for i in x:
    ax1.annotate(f"{FMQ_SALES[i]:.1f}", (i - 0.18, FMQ_SALES[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.0, color=NAVY, fontweight="bold")
    ax1.annotate(f"{FMQ_BP[i]:.1f}", (i + 0.18, FMQ_BP[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.0, color=NAVY)
ax1.set_xticks(list(x)); ax1.set_xticklabels(FMQ_L, fontsize=6.8)
ax1.set_ylim(0, 44); ax1.set_ylabel("JPY bn", fontsize=7.5)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax2 = ax1.twinx()
ax2.plot(list(x), [m * 100 for m in FMQ_MARGIN], color=RED, marker="o", markersize=3, linewidth=1.3, zorder=5, label="Margin %")
for i, m in enumerate(FMQ_MARGIN):
    ax2.annotate(f"{m * 100:.1f}", (i, m * 100), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=5.8, color=RED)
ax2.set_ylim(-70, 66); ax2.set_yticks([]); ax2.tick_params(axis="y", labelsize=7, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=5.9, frameon=False, bbox_to_anchor=(-0.02, 1.2), ncol=3)
save("chart_quarters")

# ---- 4. Sum of the parts per share: my base against the price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
food = FOOD_FLOOR_PS
film_base = BASE["fm_ps"]
film_mkt = PRICE - food
xs = [0, 1]
ax.bar(xs, [food, food], color=PALE, edgecolor=NAVY, linewidth=0.5, width=0.5, zorder=3, label="Everything else, less net debt and minorities")
ax.bar(xs, [film_base, film_mkt], bottom=[food, food], color=[NAVY, LIGHT_BLUE], width=0.5, zorder=3)
ax.annotate(f"JPY {food:,.0f}", (0, food / 2), ha="center", va="center", fontsize=6.4, color=NAVY, fontweight="bold")
ax.annotate(f"JPY {food:,.0f}", (1, food / 2), ha="center", va="center", fontsize=6.4, color=NAVY, fontweight="bold")
ax.annotate(f"Film JPY {film_base:,.0f}\n{MULT_FM:.0f}x", (0, food + film_base / 2), ha="center", va="center", fontsize=6.2, color="white", fontweight="bold")
ax.annotate(f"Film JPY {film_mkt:,.0f}\n{FM_IMPLIED_X:.0f}x", (1, food + film_mkt / 2), ha="center", va="center", fontsize=6.2, color=NAVY, fontweight="bold")
ax.annotate(f"JPY {BASE_VALUE:,.0f}", (0, BASE_VALUE), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6, color=NAVY, fontweight="bold")
ax.annotate(f"JPY {PRICE:,.0f}", (1, PRICE), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6, color=RED, fontweight="bold")
ax.set_xticks(xs); ax.set_xticklabels(["My base value", f"The price, {PRICE_DATE[:-5]}"], fontsize=7)
ax.set_xlim(-0.7, 1.7); ax.set_ylim(0, 6400); ax.set_ylabel("JPY per share", fontsize=7.5)
ax.legend(loc="upper left", fontsize=5.9, frameon=False, bbox_to_anchor=(-0.02, 1.16))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_sotp")

# ---- 5. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in VGRID); ghi = max(max(r) for r in VGRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    ("Sensitivity grid\nfilm sales x film multiple", "range", (glo, ghi)),
    (f"Peer medians\n{FOOD_MED:.0f}x and {ELEC_MED:.1f}x", "point", MED_VALUE),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base\n{MULT_FOOD:.0f}x and {MULT_FM:.0f}x FY2027E", "point", base),
    ("Average analyst target", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=(4.7, 2.5), dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"JPY {v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"JPY {lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
        ax.annotate(f"JPY {hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 60, len(rows) - 0.45, f"Price JPY {PRICE:,.0f}", fontsize=6.6, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=5.8)
ax.set_xlabel("Value per share (JPY)", fontsize=8)
ax.set_xlim(1500, 7600); ax.set_ylim(-0.6, len(rows) - 0.05)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 80, f"My base value JPY {BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"JPY {PX[-1]:,.0f}\n7 Oct 2026", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 6, 3000), textcoords="data", ha="right",
            va="center", fontsize=6.6, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(2000, 6600); ax.set_ylabel("Close (JPY, split-adjusted)", fontsize=7.5)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
