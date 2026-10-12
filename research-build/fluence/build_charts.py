"""Charts for the Fluence initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Revenue and adjusted EBITDA margin, FY24A to FY28E ----
years = YEARS_H + ["FY26G", "FY27E*", "FY28E*"]
rev = [r / 1000 for r in REV_H + [REV26, REV27, REV28]]
mar = [e / r * 100 for e, r in zip(EBITDA_H + [G26["ebitda"], EBITDA27, EBITDA28], REV_H + [REV26, REV27, REV28])]
x = range(len(years))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY, NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE], width=0.6, zorder=3, label="Revenue, US$bn")
for i, r in enumerate(rev):
    ax1.annotate(f"{r:.1f}", (i, r / 2), ha="center", va="center", fontsize=6.6, color="white", fontweight="bold")
ax1.set_ylim(0, 6.2); ax1.set_ylabel("Revenue (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(list(x)); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(list(x), mar, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Adjusted EBITDA margin, % (RHS)")
for i, m in enumerate(mar):
    ax2.annotate(f"{m:.1f}%", (i, m), xytext=(0, -9 if m < 0 else 4), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.2, color=RED, fontweight="bold")
ax2.axhline(0, color=GRAY, linewidth=0.6, linestyle=":")
ax2.set_ylim(-40, 10); ax2.set_yticks([-8, 0, 8]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.6, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
glo = value(min(SENS_REV), min(SENS_MULT)); ghi = value(max(SENS_REV), max(SENS_MULT))
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_MULT[0]:.2f} to {SENS_MULT[2]:.2f}x FY28E sales", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_MULT:.2f}x FY28E sales\nof US${REV28 / 1000:.1f}bn", "point", base),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"US${v:,.2f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:,.2f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:,.2f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 0.2, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 19); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Quarterly revenue and adjusted gross margin ----
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(QL, Q_REV, color=[NAVY] * 4 + [LIGHT_BLUE] * 3, width=0.6, zorder=3, label="Revenue, US$m")
for i, v in enumerate(Q_REV):
    ax1.annotate(f"{v:,.0f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.3,
                 color=NAVY, fontweight="bold")
ax1.set_ylim(0, 1500); ax1.set_ylabel("US$m", fontsize=8); style(ax1)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
ax2 = ax1.twinx()
ax2.plot(range(len(QL)), Q_AGM, color=RED, marker="o", markersize=3.3, linewidth=1.5, zorder=4, label="Adjusted gross margin, % (RHS)")
for i, m in enumerate(Q_AGM):
    ax2.annotate(f"{m:.1f}", (i, m), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=RED, fontweight="bold")
ax2.set_ylim(-25, 22); ax2.set_yticks([0, 5, 10, 15]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
save("chart_quarters")

# ---- 4. Backlog at quarter end ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(QL, BACKLOG, color=[NAVY] * 6 + [LIGHT_BLUE], width=0.55, zorder=3)
for b, v in zip(bars, BACKLOG):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax.axhline(G26["rev"] / 1000, color=RED, linestyle="--", linewidth=1.1, zorder=4)
ax.text(3, G26["rev"] / 1000 + 0.12, "FY26 revenue guide, 16 Sep 2026: about US$2.4bn", fontsize=6.3, color=RED, ha="center", va="bottom",
        zorder=5, bbox=dict(facecolor="white", edgecolor="none", pad=1.2))
ax.set_ylim(0, 7.5); ax.set_ylabel("US$bn", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_backlog")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 0.5, f"My base value US${BASE_VALUE:,.2f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 6, 2.6), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 35); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
