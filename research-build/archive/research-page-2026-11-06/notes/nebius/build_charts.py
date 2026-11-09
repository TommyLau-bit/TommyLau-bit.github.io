"""Charts for the Nebius initiation, house style (navy / light blue, red re-look line, grey price line)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import nebius_data as D

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "charts")
os.makedirs(OUT, exist_ok=True)

plt.rcParams["font.family"] = ["Arial", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1F3864"
LIGHT_BLUE = "#8FAADC"
PALE = "#C9D6EF"
RED = "#C00000"
GRAY = "#7F7F7F"
GRID = "#E3E3E3"
SIZE = (4.7, 2.15)


def style(ax, grid_axis="y"):
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#B0B0B0")
    ax.tick_params(axis="both", labelsize=7.6, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis=grid_axis, color=GRID, linewidth=0.7, zorder=0)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", dpi=220)
    plt.close(fig)


# 1. ARR vs year-end guide
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
labels = D.Q_LABELS + ["YE 26 guide"]
bars = ax.bar(D.Q_LABELS, D.ARR, color=NAVY, width=0.55, zorder=3, label="ARR at quarter end")
lo, hi = D.ARR_GUIDE
ax.bar(["YE 26 guide"], [hi - lo], bottom=[lo], color=PALE, edgecolor=NAVY, linewidth=0.9, width=0.55, zorder=3,
       label="Year-end 2026 guide, US$7 to 9bn")
for b, v in zip(bars, D.ARR):
    ax.annotate(f"{v:.2f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 3), textcoords="offset points",
                ha="center", va="bottom", fontsize=7.1, color=NAVY, fontweight="bold")
ax.annotate("7 to 9", (6, hi), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom",
            fontsize=7.1, color=NAVY, fontweight="bold")
ax.axhline(lo, color=RED, linestyle="--", linewidth=1.1, zorder=4)
ax.text(0, lo + 0.25, "Guide low end US$7bn", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_ylabel("US$ bn", fontsize=8)
ax.set_ylim(0, 10.5)
style(ax)
ax.legend(loc="upper left", fontsize=7, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2, handletextpad=0.5)
save(fig, "nbis_arr.png")

# 2. Revenue vs capex
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
x = range(len(D.Q_LABELS))
w = 0.38
b1 = ax.bar([i - w / 2 for i in x], D.REVENUE, width=w, color=NAVY, zorder=3, label="Revenue")
b2 = ax.bar([i + w / 2 for i in x], D.CAPEX, width=w, color=LIGHT_BLUE, zorder=3, label="Capital spending")
for b, v in zip(b1, D.REVENUE):
    ax.annotate(f"{v:,.0f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points",
                ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
for b, v in zip(b2, D.CAPEX):
    ax.annotate(f"{v:,.0f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points",
                ha="center", va="bottom", fontsize=6.4, color="#2E5395")
ax.set_xticks(list(x))
ax.set_xticklabels(D.Q_LABELS)
ax.set_ylabel("US$ m", fontsize=8)
ax.set_ylim(0, 6600)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"{v:,.0f}"))
style(ax)
ax.legend(loc="upper left", fontsize=7, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2, handletextpad=0.5)
save(fig, "nbis_build.png")

# 3. ACV per MW step-up
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
cols = [LIGHT_BLUE, NAVY, NAVY]
bars = ax.barh(range(3), D.ACV, color=cols, height=0.52, zorder=3)
txt = ["~US$12m", "US$20 to 25m (mid 22.5)", "Above US$40m (floor)"]
for b, v, t in zip(bars, D.ACV, txt):
    ax.annotate(t, (v, b.get_y() + b.get_height() / 2), xytext=(4, 0), textcoords="offset points",
                ha="left", va="center", fontsize=7.1, color=NAVY, fontweight="bold")
ax.set_yticks(range(3))
ax.set_yticklabels(["2026 fleet\nbase", "Q2 2026\nlarge deals", "Q3 2026\nshort-term deals"], fontsize=7.4)
ax.invert_yaxis()
ax.set_xlim(0, 62)
ax.set_xlabel("Annual contract value per MW, US$ m, approximate", fontsize=7.8)
style(ax, "x")
save(fig, "nbis_acv.png")

# 4. AI cloud margin
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ml = ["Q3 25", "Q4 25", "Q1 26", "Q2 26"]
mv = [19, 24, 45, 49.7]
bars = ax.bar(ml, mv, color=NAVY, width=0.5, zorder=3)
for b, v in zip(bars, mv):
    ax.annotate(f"{v:g}%", (b.get_x() + b.get_width() / 2, v), xytext=(0, 3), textcoords="offset points",
                ha="center", va="bottom", fontsize=7.1, color=NAVY, fontweight="bold")
ax.axhline(50, color=GRAY, linestyle="--", linewidth=1.1, zorder=4)
ax.text(-0.3, 51, "50% margin used in unit economics", fontsize=7, color=GRAY, ha="left", va="bottom")
ax.set_ylim(0, 62)
ax.set_ylabel("AI cloud adj. EBITDA margin, %", fontsize=7.6)
style(ax)
save(fig, "nbis_margin.png")

# 5. Valuation cross-check (football field)
scen, wv, _ = D.scenarios()
sens = D.sensitivity()
fig, ax = plt.subplots(figsize=(4.7, 2.3), dpi=220)
rows = [
    ("Sensitivity grid\n(EBITDA 7.5 to 11.5bn,\n9x to 13x)", min(min(r) for r in sens), max(max(r) for r in sens), "range"),
    ("Bear to bull\nscenarios", scen[0][9], scen[2][9], "range"),
    ("Probability-weighted\n(25 / 50 / 25)", None, wv, "point"),
    ("Base case\n(21bn, 45%, 11x)", None, scen[1][9], "point"),
]
for y, (lbl, lo, hi, kind) in enumerate(rows):
    if kind == "range":
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        ax.barh(y, hi, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"US${hi:.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(D.PRICE, color=GRAY, linestyle="--", linewidth=1.3, zorder=4)
ax.axvline(D.RELOOK, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(D.PRICE + 4, len(rows) - 0.45, "Price US$232.57", fontsize=7, color=GRAY, ha="left", va="bottom")
ax.text(D.RELOOK - 4, len(rows) - 0.45, "Re-look ~US$185", fontsize=7, color=RED, ha="right", va="bottom")
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows], fontsize=7)
ax.set_xlim(0, 500)
ax.set_ylim(-0.6, len(rows) - 0.1)
ax.set_xlabel("Value per share, October 2027, US$", fontsize=7.8)
style(ax, "x")
save(fig, "nbis_valuation.png")

# 6. Share price
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
xs = list(range(len(D.PRICE_SERIES)))
ax.plot(xs, D.PRICE_SERIES, color=NAVY, linewidth=1.8, zorder=4, marker="o", markersize=2.4)
ax.axhline(D.RELOOK, color=RED, linestyle="--", linewidth=1.1, zorder=3)
ax.text(0.2, D.RELOOK + 5, "Re-look ~US$185", fontsize=7, color=RED, ha="left", va="bottom")
ax.annotate("US$232.57", (xs[-1], D.PRICE_SERIES[-1]), xytext=(-4, 8), textcoords="offset points",
            ha="right", va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax.text(17.2, 262, "Jun 26 close\nUS$276.17", fontsize=6.6, color=GRAY, ha="right", va="center")
ticks = [0, 4, 8, 12, 16, 20, 23]
ax.set_xticks(ticks)
ax.set_xticklabels([D.PRICE_LABELS[i] for i in ticks])
ax.set_ylabel("US$, month-end close", fontsize=7.8)
ax.set_ylim(0, 310)
style(ax)
save(fig, "nbis_price.png")

print("Charts saved to", OUT)
