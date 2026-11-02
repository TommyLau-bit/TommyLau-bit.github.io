"""Charts for the SK hynix initiation. House style: navy / light blue, red reference lines, grey price line."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from data import *

plt.rcParams["font.family"] = "Arial"
plt.rcParams["axes.unicode_minus"] = False
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


def k(x):
    return f"{x / 1000:,.0f}k"


# ---- 1. Quarterly revenue and operating margin ----
labs = QL + ["Q4 26E*"]
rev = Q_REV + [Q4_REV]
om = [o / r * 100 for o, r in zip(Q_OP, Q_REV)] + [Q4_OPM * 100]
x = list(range(len(labs)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY] * len(QL) + [LIGHT_BLUE], width=0.62, zorder=3, label="Revenue, KRW tn")
for i in (3, 7, 8, 9, 10, 11):
    ax1.annotate(f"{rev[i]:.0f}", (i, rev[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.0, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 180); ax1.set_ylabel("KRW trillion", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(x); ax1.set_xticklabels(labs, fontsize=5.8, rotation=0)
ax2 = ax1.twinx()
ax2.plot(x, om, color=RED, marker="o", markersize=2.6, linewidth=1.3, zorder=4, label="Operating margin, % (RHS)")
for i in (0, 4, 10):
    ax2.annotate(f"{om[i]:.0f}%", (i, om[i]), xytext=(-3, 4), textcoords="offset points", ha="right", va="bottom", fontsize=6.0, color=RED, fontweight="bold")
ax2.set_ylim(0, 100); ax2.set_yticks([0, 40, 80])
ax2.tick_params(axis="y", labelsize=7.0, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=2)
save("chart_quarters")

# ---- 2. How much is HBM: my estimate against total revenue ----
tot = [REV10[-1], REV26, R27]
rest = [t - h for t, h in zip(tot, HBM_REV)]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
xs = range(3)
ax.bar(xs, HBM_REV, color=RED, width=0.55, zorder=3, label="HBM (my estimate)")
ax.bar(xs, rest, bottom=HBM_REV, color=NAVY, width=0.55, zorder=3, label="Conventional DRAM, NAND and other")
for i in xs:
    ax.annotate(f"HBM {HBM_REV[i] / tot[i] * 100:.0f}%", (i, tot[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6, color=RED, fontweight="bold")
    ax.annotate(f"{tot[i]:.0f}", (i, tot[i] / 2 + HBM_REV[i] / 2), ha="center", va="center", fontsize=6.4, color="white", fontweight="bold")
ax.set_ylim(0, 640); ax.set_ylabel("KRW trillion", fontsize=8)
ax.set_xticks(list(xs)); ax.set_xticklabels(["2025", "2026E*", "2027E*"], fontsize=7)
ax.legend(loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_hbm")

# ---- 3. The cycle: revenue 2016 to 2027E and net margin ----
yrs = [y[2:] for y in YRS10] + ["26E*", "27E*"]
rv = REV10 + [REV26, R27]
nm = [n / r * 100 for n, r in zip(NI10, REV10)] + [NI26 / REV26 * 100, NI27 / R27 * 100]
x = list(range(len(yrs)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rv, color=[NAVY] * len(YRS10) + [LIGHT_BLUE] * 2, width=0.62, zorder=3, label="Revenue, KRW tn")
for i in (2, 9, 10, 11):
    ax1.annotate(f"{rv[i]:.0f}", (i, rv[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.0, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 700); ax1.set_ylabel("KRW trillion", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(x); ax1.set_xticklabels(yrs, fontsize=6.6)
ax2 = ax1.twinx()
ax2.plot(x, nm, color=RED, marker="o", markersize=2.8, linewidth=1.4, zorder=4, label="Net margin, % (RHS)")
ax2.axhline(CYC_NM * 100, color=GRAY, linestyle=":", linewidth=1.0, label=f"2016-25 net margin {CYC_NM * 100:.1f}%")
for i in (2, 7, 10):
    ax2.annotate(f"{nm[i]:.0f}%", (i, nm[i]), xytext=(-4, 4 if nm[i] > 0 else -3), textcoords="offset points", ha="right", va="bottom" if nm[i] > 0 else "top", fontsize=6.0, color=RED, fontweight="bold")
ax2.set_ylim(-60, 100); ax2.set_yticks([-40, 0, 40, 80])
ax2.tick_params(axis="y", labelsize=7.0, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=3)
save("chart_cycle")

# ---- 4. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in VGRID); ghi = max(max(r) for r in VGRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nmargin {SENS_NM[0]*100:.0f}-{SENS_NM[2]*100:.0f}%, {SENS_X[0]}-{SENS_X[2]}x", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    ("Base: cash + excess\n+ 12x normal EPS", "point", base),
    ("Base without the\nnet cash", "point", base - NC_PS),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v / 1000, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(k(v), (v / 1000, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, (hi - lo) / 1000, left=lo / 1000, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        if abs(lo - PRICE) < 250000:
            ax.annotate(k(lo), (lo / 1000, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
        else:
            ax.annotate(k(lo), (lo / 1000, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(k(hi), (hi / 1000, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE / 1000, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE / 1000 + 30, len(rows) - 0.42, f"Price KRW {PRICE:,.0f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (KRW thousand)", fontsize=8)
ax.set_xlim(0, 4100); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 5. Earnings per share: reported, mine, normal, and what the price needs ----
labs5 = ["2025", "2026E*", "2027E*", "2028E*", "Normal,\nmy base*", "Price needs,\ncash kept*", "Needs, cash\nspent*"]
vals5 = [EPS25, EPS26, EPS27, EPS28, N_BASE, NEED_N, NEED_N_NOCASH]
cols5 = [NAVY, LIGHT_BLUE, LIGHT_BLUE, LIGHT_BLUE, GRAY, RED, RED]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(range(7), [v / 1000 for v in vals5], color=cols5, width=0.6, zorder=3)
for i, v in enumerate(vals5):
    ax.annotate(f"{v / 1000:,.0f}", (i, v / 1000), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
ax.set_ylim(0, 520); ax.set_ylabel("EPS (KRW thousand)", fontsize=8)
ax.set_xticks(range(7)); ax.set_xticklabels(labs5, fontsize=5.4)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_eps")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), [p / 1000 for p in PX], color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE / 1000, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE / 1000 + 50, f"My base value KRW {BASE_VALUE / 1000:,.0f}k", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"KRW {PX[-1] / 1000:,.0f}k\n2 Nov 2026", (len(PX) - 1, PX[-1] / 1000), xytext=(len(PX) - 17, 1500), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 3000); ax.set_ylabel("Close (KRW thousand)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
