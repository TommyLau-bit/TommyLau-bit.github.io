"""Charts for the Lumentum initiation. House style: navy / light blue, red reference lines, grey price line."""
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


def twin_clean(ax2):
    ax2.tick_params(axis="y", labelsize=7.4, length=0)
    for s in ["top", "left", "right"]:
        ax2.spines[s].set_visible(False)


# ---- 1. Revenue FY24 to FY28E with non-GAAP EPS ----
years = YEARS_H + ["FY27E*", "FY28E*"]
rev = REV_H + [REV27, REV28]
eps = EPS_H + [EPS27, EPS28]
x = range(len(years))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY] * 3 + [LIGHT_BLUE] * 2, width=0.6, zorder=3, label="Revenue, US$bn")
for i, r in enumerate(rev):
    ax1.annotate(f"{r:.1f}", (i, r), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.4, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 12.5); ax1.set_ylabel("Revenue (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(list(x)); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(list(x), eps, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Non-GAAP EPS, US$ (RHS)")
for i, e in enumerate(eps):
    ax2.annotate(f"{e:.2f}", (i, e), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.2, color=RED, fontweight="bold")
ax2.set_ylim(-35, 36); ax2.set_yticks([0, 10, 20, 30]); twin_clean(ax2)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.8, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
grid_lo = min(SENS_EPS) * min(SENS_PE); grid_hi = max(SENS_EPS) * max(SENS_PE)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_PE[0]} to {SENS_PE[2]}x, EPS {SENS_EPS[0]:.0f} to {SENS_EPS[2]:.0f}", "range", (grid_lo, grid_hi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_PE}x FY28E EPS\nof US${EPS28:.2f}", "point", base),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        out = v > PRICE
        ax.annotate(f"US${v:,.0f}", (v, y), xytext=(4 if out else -4, 0), textcoords="offset points", ha="left" if out else "right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 20, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 1800); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Gross margin by quarter, GAAP and non-GAAP, against the claim's test ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(Q, Q_GM_GAAP, color=[LIGHT_BLUE] * 4 + [NAVY] * 4, width=0.6, zorder=3, label="Gross margin, GAAP")
for k, (b, v) in enumerate(zip(bars, Q_GM_GAAP)):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v / 2), xytext=(0, 0), textcoords="offset points",
                ha="center", va="center", fontsize=6.3, color="white" if k >= 4 else NAVY, fontweight="bold")
ax.plot(range(len(Q)), Q_GM, color=GRAY, marker="s", markersize=2.8, linewidth=1.2, zorder=4, label="Gross margin, non-GAAP")
ax.axhline(42, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(-0.4, 42.8, "Low forties: where the claim's test begins", fontsize=6.4, color=RED, ha="left", va="bottom")
ax.set_ylim(0, 62); ax.set_ylabel("Per cent", fontsize=8)
ax.set_xticks(range(len(Q))); ax.set_xticklabels(Q, fontsize=6.6)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_margin")

# ---- 4. Revenue by quarter: components and systems ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(Q, Q_COMP, color=NAVY, width=0.6, zorder=3, label="Components (lasers and chips)")
ax.bar(Q, Q_SYS, bottom=Q_COMP, color=LIGHT_BLUE, width=0.6, zorder=3, label="Systems (transceivers, switches)")
for i, v in enumerate(Q_REV):
    ax.annotate(f"{v:,.0f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.0, color=NAVY, fontweight="bold")
ax.set_ylim(0, 1250); ax.set_ylabel("US$m", fontsize=8)
ax.set_xticks(range(len(Q))); ax.set_xticklabels(Q, fontsize=6.6)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_quarterly")

# ---- 5. What the price needs: FY2028 revenue ----
labs = ["FY26\nactual", "FY27E*", "FY28E*\nbase", "FY28\nconsensus EPS", "FY28\nprice needs"]
vals = [REV_H[2], REV27, REV28, CONS28_REV, NEED_REV28]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(labs, vals, color=[NAVY, LIGHT_BLUE, LIGHT_BLUE, GRAY, RED], width=0.55, zorder=3)
for b, v in zip(bars, vals):
    ax.annotate(f"US${v:.1f}bn", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points",
                ha="center", va="bottom", fontsize=6.8, color=NAVY, fontweight="bold")
ax.set_ylim(0, 12); ax.set_ylabel("Revenue (US$bn)", fontsize=8)
ax.tick_params(axis="x", labelsize=6.6)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_need")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 25, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}", (len(PX) - 1, PX[-1]), xytext=(2, 6), textcoords="offset points", ha="right",
            va="bottom", fontsize=7, color=NAVY, fontweight="bold")
i_nv = PX_LABELS.index("Mar 26")
ax.annotate("Nvidia deal,\n2 Mar 2026", (i_nv, PX[i_nv]), xytext=(12, -38), textcoords="offset points", fontsize=6.4,
            color=NAVY, arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 1250); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
