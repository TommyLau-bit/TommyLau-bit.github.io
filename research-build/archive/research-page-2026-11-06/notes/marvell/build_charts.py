"""Charts for the Marvell initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Revenue FY24 to FY29E with non-GAAP EPS ----
years = YEARS_H + ["FY27E*", "FY28E*", "FY29E*"]
rev = REV_H + [REV27, REV28_IN, REV29]
eps = EPS_H + [EPS27, EPS28, EPS29]
x = range(len(years))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY] * 3 + [LIGHT_BLUE] * 3, width=0.6, zorder=3, label="Revenue, US$bn")
for i, r in enumerate(rev):
    ax1.annotate(f"{r:.1f}", (i, r), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.4, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 34); ax1.set_ylabel("Revenue (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(list(x)); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(list(x), eps, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Non-GAAP EPS, US$ (RHS)")
for i, e in enumerate(eps):
    ax2.annotate(f"{e:.2f}", (i, e), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.2, color=RED, fontweight="bold")
ax2.set_ylim(-13, 15.5); ax2.set_yticks([0, 4, 8, 12]); twin_clean(ax2)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.8, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
grid_lo = min(SENS_EPS) * min(SENS_PE); grid_hi = max(SENS_EPS) * max(SENS_PE)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_PE[0]} to {SENS_PE[2]}x, EPS {SENS_EPS[0]:.0f} to {SENS_EPS[2]:.1f}", "range", (grid_lo, grid_hi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_PE}x FY29E EPS\nof US${EPS29:.2f}", "point", base),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"US${v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 6, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 620); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Revenue by quarter: data centre and the rest ----
comm = [t - d for t, d in zip(Q_REV, Q_DC)]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(QS, Q_DC, color=NAVY, width=0.6, zorder=3, label="Data centre")
ax.bar(QS, comm, bottom=Q_DC, color=LIGHT_BLUE, width=0.6, zorder=3, label="Communications and other")
for i, (d, t) in enumerate(zip(Q_DC, Q_REV)):
    ax.annotate(f"{d / t * 100:.0f}%", (i, d / 2), ha="center", va="center", fontsize=6.0, color="white", fontweight="bold")
    ax.annotate(f"{t:,.0f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=5.9, color=NAVY, fontweight="bold")
ax.set_ylim(0, 3300); ax.set_ylabel("US$m", fontsize=8)
ax.set_xticks(range(len(QS))); ax.set_xticklabels(QS, fontsize=6.4)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_dc")

# ---- 4. Data centre by business, FY26 to FY28E ----
labs = ["FY26\n(disclosed\nand derived)", "FY27E*", "FY28E*"]
keys = ["FY26", "FY27E", "FY28E"]
rest = [REST[k] for k in keys]; cus = [CUS[k] for k in keys]; swi = [SWI[k] for k in keys]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(labs, rest, color=NAVY, width=0.5, zorder=3, label="Interconnect, storage and other")
ax.bar(labs, swi, bottom=rest, color=GRAY, width=0.5, zorder=3, label="Switching")
ax.bar(labs, cus, bottom=[r + s for r, s in zip(rest, swi)], color=LIGHT_BLUE, width=0.5, zorder=3, label="Custom")
for i, k in enumerate(keys):
    ax.annotate(f"{rest[i]:.1f}", (i, rest[i] / 2), ha="center", va="center", fontsize=6.6, color="white", fontweight="bold")
    ax.annotate(f"{cus[i]:.1f}", (i, rest[i] + swi[i] + cus[i] / 2), ha="center", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
    ax.annotate(f"US${DCV[k]:.1f}bn", (i, DCV[k]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.8, color=NAVY, fontweight="bold")
ax.set_ylim(0, 21.5); ax.set_ylabel("US$bn", fontsize=8)
ax.tick_params(axis="x", labelsize=6.6)
ax.legend(loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.2), ncol=3)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_split")

# ---- 5. Margins by quarter ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(QS, Q_OM, color=NAVY, width=0.6, zorder=3, label="Operating margin, non-GAAP")
for b, v in zip(bars, Q_OM):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v / 2), ha="center", va="center", fontsize=6.0, color="white", fontweight="bold")
ax.plot(range(len(QS)), Q_GM, color=GRAY, marker="s", markersize=2.8, linewidth=1.2, zorder=4, label="Gross margin, non-GAAP")
for i, v in enumerate(Q_GM):
    if i in (0, len(Q_GM) - 1):
        ax.annotate(f"{v:.1f}", (i, v), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=GRAY, fontweight="bold")
ax.axhline(58.0, color=RED, linestyle="--", linewidth=1.1, zorder=4)
ax.text(-0.4, 51.5, "Q3 FY27 gross margin guide, 57.5 to 58.5%", fontsize=6.3, color=RED, ha="left", va="bottom")
ax.set_ylim(0, 72); ax.set_ylabel("Per cent", fontsize=8)
ax.set_xticks(range(len(QS))); ax.set_xticklabels(QS, fontsize=6.4)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_margin")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(CALL["target"], color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, CALL["target"] + 6, f"My target US${CALL['target']:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 1.5, 95), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
i_nv = PX_LABELS.index("Mar 26")
ax.annotate("Nvidia invests,\n31 Mar 2026", (i_nv, PX[i_nv]), xytext=(-62, 30), textcoords="offset points", fontsize=6.4,
            color=NAVY, arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 400); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
