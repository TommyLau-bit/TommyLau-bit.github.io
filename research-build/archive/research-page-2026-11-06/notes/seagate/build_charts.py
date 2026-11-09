"""Charts for the Seagate initiation. House style: navy / light blue, red reference lines, grey price line."""

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


# ---- 1. The cycle: GAAP revenue FY16 to FY26, my FY27E and FY28E (bars) and gross margin (line) ----
yrs = [y[2:] for y in YRS] + ["27E*", "28E*"]
rev = REV_H + [REV27, REV28]
x = list(range(len(yrs)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY] * len(YRS) + [LIGHT_BLUE] * 2, width=0.62, zorder=3, label="Revenue, US$bn")
for i in (10, 11, 12):
    ax1.annotate(f"{rev[i]:.1f}", (i, rev[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.0, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 36); ax1.set_ylabel("Revenue (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(x); ax1.set_xticklabels(yrs, fontsize=6.6); ax1.set_xlabel("Fiscal year", fontsize=7)
ax2 = ax1.twinx()
nm = [n / r * 100 for n, r in zip(NI_H, REV_H)] + [NI27 / REV27 * 100, NI28 / REV28 * 100]
ax2.plot(x, nm, color=RED, marker="o", markersize=2.8, linewidth=1.4, zorder=4, label="Net margin, % (RHS)")
ax2.axhline(CYC_NM * 100, color=GRAY, linestyle=":", linewidth=1.0, label=f"FY16-25 net margin {CYC_NM * 100:.1f}%")
for i in (3, 7, 10, 12):
    ax2.annotate(f"{nm[i]:.0f}%", (i, nm[i]), xytext=(-4, 4) if nm[i] > 0 else (5, -3), textcoords="offset points", ha="right" if nm[i] > 0 else "left",
                 va="bottom" if nm[i] > 0 else "top", fontsize=6.0, color=RED, fontweight="bold")
ax2.set_ylim(-30, 60); ax2.set_yticks([-20, 0, 20, 40])
ax2.tick_params(axis="y", labelsize=7.0, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=3)
save("chart_cycle")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in VGRID); ghi = max(max(r) for r in VGRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nmargin {SENS_NM[0]*100:.0f}-{SENS_NM[2]*100:.0f}%, {SENS_X[0]}-{SENS_X[2]}x", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: cash + excess\n+ {MULT}x normal EPS", "point", base),
    ("Highest close\n22 June 2026", "point", HI_CLOSE),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        if v < PRICE:
            ax.annotate(f"US${v:,.0f}", (v, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=7, color=NAVY, fontweight="bold")
        else:
            ax.annotate(f"US${v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 12, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 1250); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Price per nearline terabyte (bars) and nearline exabytes (line) ----
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
xs = list(range(len(QS)))
ax1.bar(xs, Q_PTB, color=[NAVY] * 8 + [RED], width=0.6, zorder=3, label="Data Center revenue per nearline TB, US$")
for i, v in enumerate(Q_PTB):
    ax1.annotate(f"{v:.1f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 24); ax1.set_ylabel("US$ per TB", fontsize=8)
ax1.set_xticks(xs); ax1.set_xticklabels(QS, fontsize=6.6)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax2 = ax1.twinx()
ax2.plot(xs, Q_NL, color=LIGHT_BLUE, marker="o", markersize=3, linewidth=1.6, zorder=4, label="Nearline exabytes shipped (RHS)")
ax2.set_ylim(0, 300); ax2.tick_params(axis="y", labelsize=7.0, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
save("chart_ptb")

# ---- 4. Quarterly revenue: Data Center and Edge IoT, with the Q2 FY27 guide; gross margin in white ----
labs = QS + ["Dec 26\nguide"]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(xs, Q_DC, color=NAVY, width=0.6, zorder=3, label="Data Center")
ax.bar(xs, Q_EDGE, bottom=Q_DC, color=LIGHT_BLUE, width=0.6, zorder=3, label="Edge IoT")
ax.bar(len(QS), G2["rev"], color=PALE, edgecolor=NAVY, linewidth=0.5, width=0.6, zorder=3, label="Guide, total")
for i, t in enumerate(Q_REV + [G2["rev"]]):
    ax.annotate(f"{t:.2f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=5.8, color=NAVY, fontweight="bold")
for i in range(len(QS)):
    ax.annotate(f"{Q_GM[i] * 100:.0f}%", (i, Q_DC[i] / 2), ha="center", va="center", fontsize=5.6, color="white", fontweight="bold")
ax.set_ylim(0, 5.8); ax.set_ylabel("US$bn", fontsize=8)
ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, fontsize=6.2)
ax.legend(loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=3)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_quarters")

# ---- 5. Earnings per share: reported, mine, and what the price needs from a normal year ----
labs5 = ["FY25", "FY26", "FY27E*", "FY28E*", "Normal,\nmy base*", "Normal the\nprice needs*"]
vals5 = [FY25["eps"], FY26["eps"], EPS27, EPS28, N_BASE, NEED_N]
cols5 = [NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE, GRAY, RED]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(range(6), vals5, color=cols5, width=0.6, zorder=3)
for i, v in enumerate(vals5):
    ax.annotate(f"US${v:,.2f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
ax.set_ylim(0, 64); ax.set_ylabel("Non-GAAP EPS (US$)", fontsize=8)
ax.set_xticks(range(6)); ax.set_xticklabels(labs5, fontsize=6.4)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_eps")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 20, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n30 Oct 2026", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 3, 230), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 1150); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
