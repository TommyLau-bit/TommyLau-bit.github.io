"""Charts for the Schneider Electric initiation. House style: navy / light blue, red reference lines, grey price line."""

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


# ---- 1. Organic growth by business model, by quarter ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
w = 0.26
for k, (name, col) in enumerate([("Systems", NAVY), ("Products", GRAY), ("Software & Services", LIGHT_BLUE)]):
    vals = [g * 100 for g in Q_GROW[name]]
    xs = [i + (k - 1) * w for i in range(len(QL))]
    ax.bar(xs, vals, width=w, color=col, zorder=3, label=name)
    for x_, v in zip(xs, vals):
        ax.annotate(f"{v:.0f}", (x_, v), xytext=(0, 1.5), textcoords="offset points", ha="center", va="bottom", fontsize=5.8,
                    color=col if col != LIGHT_BLUE else NAVY, fontweight="bold")
ax.set_xticks(range(len(QL))); ax.set_xticklabels(QL, fontsize=7)
ax.set_ylim(0, 33); ax.set_ylabel("Organic growth (%)", fontsize=8)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=3)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_growth")

# ---- 2. Systems share of revenue, with the claim's 34% line ----
labs = ["FY24", "Q2 25", "Q3 25", "FY25", "Q1 26", "Q2 26", "H1 26*"]
vals = [31, 33, 34, 34, 33, 35, SYS_H126 * 100]
cols = [NAVY if l.startswith("FY") else (LIGHT_BLUE if "*" in l else PALE) for l in labs]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(range(len(labs)), vals, color=cols, edgecolor=NAVY, linewidth=0.5, width=0.6, zorder=3)
for b, v in zip(bars, vals):
    ax.annotate(f"{v:.0f}%" if abs(v - round(v)) < 1e-9 else f"{v:.1f}%", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2),
                textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
ax.axhline(34, color=RED, linestyle="--", linewidth=1.1, zorder=4)
ax.text(-0.35, 34.25, "Claim fails below 34%\nfor a full year", fontsize=6.0, color=RED, ha="left", va="bottom")
ax.set_ylim(28, 37.5); ax.set_ylabel("Systems, % of revenue", fontsize=8)
ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, fontsize=7)
ax.legend(handles=[Patch(color=NAVY, label="Full year"), Patch(facecolor=PALE, edgecolor=NAVY, linewidth=0.5, label="Quarter"),
                   Patch(color=LIGHT_BLUE, label="Half year, my arithmetic")],
          loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=3)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_share")

# ---- 3. Revenue and adjusted EPS, 2024 to 2028E ----
years = ["2024", "2025", "2026E*", "2027E*", "2028E*"]
rev = [r / 1000 for r in REV_H + [REV26, REV27, REV28]]
eps = EPS_H + [EPS26, EPS27, EPS28]
x = range(len(years))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE, LIGHT_BLUE], width=0.6, zorder=3, label="Revenue, standalone")
ax1.bar([4], [PT["rev"] / 1000 - REV28 / 1000], bottom=[REV28 / 1000], color=PALE, edgecolor=NAVY, linewidth=0.5, width=0.6, zorder=3,
        label="PTC")
for i in x:
    t = rev[i] + (PT["rev"] / 1000 - REV28 / 1000 if i == 4 else 0)
    ax1.annotate(f"{t:.1f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 75); ax1.set_ylabel("Revenue (EUR bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(list(x)); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(list(x), eps, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Adj. EPS, standalone (RHS)")
ax2.plot([4], [EPS28_PTC], color=RED, marker="D", markersize=3.8, linestyle="none", markerfacecolor="white", zorder=5, label="Adj. EPS with PTC")
for i, e in enumerate(eps):
    ax2.annotate(f"{e:.2f}", (i, e), xytext=(-4, 4), textcoords="offset points", ha="right", va="bottom", fontsize=6.2, color=RED, fontweight="bold")
ax2.annotate(f"{EPS28_PTC:.2f}", (4, EPS28_PTC), xytext=(6, -14), textcoords="offset points", ha="left", va="center", fontsize=6.2, color=RED)
ax2.set_ylim(-8, 15.5); ax2.set_yticks([0, 5, 10, 15])
ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.0, frameon=False, bbox_to_anchor=(-0.02, 1.22), ncol=2)
save("chart_annual")

# ---- 4. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in VGRID); ghi = max(max(r) for r in VGRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nmargin {SENS_M28[0]*100:.1f}-{SENS_M28[2]*100:.1f}%, {SENS_X[0]}-{SENS_X[2]}x", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    ("Base without PTC\n22x 2028E", "point", BASE_STANDALONE),
    ("Base with PTC\n22x 2028E", "point", base),
    ("Average analyst target\n(25 Sep, before the deal)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
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
ax.text(PRICE - 4, len(rows) - 0.42, f"Price EUR {PRICE:,.2f}", fontsize=6.6, color=RED, ha="right", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.3)
ax.set_xlabel("Value per share (EUR)", fontsize=8)
ax.set_xlim(100, 420); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 5. 2028E EPS bridge: standalone to with PTC ----
own_ppa = 0
steps = [
    ("Standalone\n2028E", EPS28, "total"),
    ("PTC EBITA\nafter tax", PT["ptc_ebita"] * (1 - TAX) / SH[2], "delta"),
    ("Interest\nafter tax", -PT["interest"] * (1 - TAX) / SH[2], "delta"),
    ("PTC purchase\naccounting", -PPA * (1 - TAX) / SH[2], "delta"),
    ("New shares,\nno buybacks", None, "delta"),
    ("With PTC\n2028E", EPS28_PTC, "total"),
]
pre_dil = EPS28 + sum(s[1] for s in steps[1:4])
steps[4] = ("New shares,\nno buybacks", EPS28_PTC - pre_dil, "delta")
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
run = 0
for i, (lab, v, kind) in enumerate(steps):
    if kind == "total":
        ax.bar(i, v, color=NAVY, width=0.6, zorder=3); run = v; top = v
        ax.annotate(f"{v:.2f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
    else:
        bottom = run if v >= 0 else run + v
        ax.bar(i, abs(v), bottom=bottom, color=LIGHT_BLUE if v >= 0 else RED, width=0.6, zorder=3)
        ax.annotate(f"{v:+.2f}", (i, max(run, run + v)), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4,
                    color=NAVY if v >= 0 else RED, fontweight="bold")
        run += v
ax.set_ylim(9, 15.5); ax.set_ylabel("Adj. EPS, EUR", fontsize=8)
ax.set_xticks(range(len(steps))); ax.set_xticklabels([s[0] for s in steps], fontsize=6.2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_bridge")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 3, f"My base value EUR {BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"EUR {PX[-1]:,.2f}\n6 Oct 2026, after PTC", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 3.5, 214), textcoords="data", ha="right",
            va="center", fontsize=6.6, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 4))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(180, 320); ax.set_ylabel("Close (EUR)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
