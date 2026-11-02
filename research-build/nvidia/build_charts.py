"""Charts for the Nvidia initiation. House style: navy / light blue, red reference lines, grey price line."""

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


# ---- 1. Revenue by quarter: Data Center and the rest, with the Q3 FY27 guide ----
labs = QS + ["Q3 27\nguide"]
dc = Q_DC + [None]
rest = [r - d for r, d in zip(Q_REV, Q_DC)] + [None]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for i in range(len(labs)):
    if dc[i] is None:
        ax.bar(i, G3["rev"], color=LIGHT_BLUE, width=0.6, zorder=3)
        ax.annotate(f"{G3['rev']:.0f}", (i, G3["rev"]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=NAVY, fontweight="bold")
    else:
        ax.bar(i, dc[i], color=NAVY, width=0.6, zorder=3)
        ax.bar(i, rest[i], bottom=dc[i], color=GRAY, width=0.6, zorder=3)
        ax.annotate(f"{dc[i]:.0f}", (i, dc[i] + rest[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=NAVY, fontweight="bold")
hs = [Patch(color=NAVY, label="Data Center (labelled)"), Patch(color=GRAY, label="Everything else"), Patch(color=LIGHT_BLUE, label="Q3 FY27 revenue guide")]
ax.set_ylim(0, 125); ax.set_ylabel("US$bn", fontsize=8)
ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, fontsize=6.2)
ax.legend(handles=hs, loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=3)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_dc")

# ---- 2. Data Center revenue translated into gigawatts of IT load a year ----
pb = project(*SCEN[1][1:8])
rows = [("FY26\nactual", DC_H[1], USD_GW["FY26"], NAVY), ("FY27E\nmine", DC27, USD_GW["FY27"], NAVY),
        ("FY28E\nmine", pb["dc28"], USD_GW["FY28"], LIGHT_BLUE), ("FY28\nconsensus", DC28_CONS, USD_GW["FY28"], GRAY),
        ("FY29E\nmine", pb["dc29"], USD_GW["FY29"], LIGHT_BLUE)]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for i, (lab, d, usd, col) in enumerate(rows):
    mid = d / usd
    lo, hi = GW_RANGE(d, usd)
    ax.bar(i, mid, color=col, width=0.58, zorder=3)
    ax.plot([i, i], [lo, hi], color=RED, linewidth=1.1, zorder=4)
    ax.plot([i - 0.08, i + 0.08], [lo, lo], color=RED, linewidth=1.1, zorder=4)
    ax.plot([i - 0.08, i + 0.08], [hi, hi], color=RED, linewidth=1.1, zorder=4)
    ax.annotate(f"{mid:.1f}", (i, mid / 2), ha="center", va="center", fontsize=6.6, color="white", fontweight="bold")
    ax.annotate(f"US\\${usd:.0f}bn/GW", (i, hi), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=5.8, color=GRAY)
ax.set_ylim(0, 24); ax.set_ylabel("GW of IT load a year", fontsize=8)
ax.set_xticks(range(len(rows))); ax.set_xticklabels([r[0] for r in rows], fontsize=6.6)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_gw")

# ---- 3. Commitments: supply bought ahead, and power guaranteed ----
labs3 = ["Q4 FY26", "Q1 FY27", "Q2 FY27", "Q2 FY27\nguarantees"]
vals3 = [95.2, 119.0, 279.0, GUAR_TOTAL]
cols3 = [NAVY, NAVY, NAVY, RED]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for i, (v, c) in enumerate(zip(vals3, cols3)):
    ax.bar(i, v, color=c, width=0.55, zorder=3)
    ax.annotate(f"{v:.1f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.8, color=c, fontweight="bold")
hs = [Patch(color=NAVY, label="Supply and capacity commitments"), Patch(color=RED, label="Land, power and shell guarantees (cap)")]
ax.set_ylim(0, 330); ax.set_ylabel("US$bn", fontsize=8)
ax.set_xticks(range(len(labs3))); ax.set_xticklabels(labs3, fontsize=6.8)
ax.legend(handles=hs, loc="upper left", fontsize=6.3, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_commit")

# ---- 4. Revenue and EPS by fiscal year ----
years = ["FY25", "FY26", "FY27E*", "FY28E*", "FY29E*"]
dcs = DC_H + [DC27, pb["dc28"], pb["dc29"]]
oth = [REV_H[0] - DC_H[0], REV_H[1] - DC_H[1], EDGE27, EDGE28, EDGE29]
eps = GAAP_EPS_H + [EPS27, pb["eps28"], pb["eps29"]]
x = range(len(years))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, dcs, color=NAVY, width=0.6, zorder=3, label="Data Center")
ax1.bar(x, oth, bottom=dcs, color=GRAY, width=0.6, zorder=3, label="Edge and other")
for i in x:
    t = dcs[i] + oth[i]
    ax1.annotate(f"{t:.0f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
ax1.scatter([3], [CONS_REV_28], marker="_", s=260, color=RED, zorder=5, linewidths=1.6, label="FY28 consensus revenue")
ax1.set_ylim(0, 1000); ax1.set_ylabel("Revenue (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(list(x)); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(list(x), eps, color=LIGHT_BLUE, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="EPS, US\\$ (RHS)")
for i, e in enumerate(eps):
    ax2.annotate(f"{e:.2f}", (i, e), xytext=(-4, 4), textcoords="offset points", ha="right", va="bottom", fontsize=6.2, color=NAVY, fontweight="bold")
ax2.set_ylim(-24, 19); ax2.set_yticks([0, 5, 10, 15, 20])
ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.2), ncol=4)
save("chart_annual")

# ---- 5. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in VGRID); ghi = max(max(r) for r in VGRID)
rows5 = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nGW +{SENS_GW[0]*100:.0f}-{SENS_GW[2]*100:.0f}%, {SENS_M[0]}-{SENS_M[2]}x", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {M_BASE}x FY29E EPS", "point", base),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows5):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"US${v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 6, len(rows5) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows5))); ax.set_yticklabels([r[0] for r in rows5], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 470); ax.set_ylim(-0.6, len(rows5) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 5, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n30 Oct 2026", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 3, 110), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 300); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
