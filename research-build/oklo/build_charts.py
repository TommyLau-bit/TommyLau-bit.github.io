"""Charts for the Oklo initiation. House style: navy / light blue, red reference lines, grey price line."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from data import *

plt.rcParams["font.family"] = "Arial"
NAVY = "#1F3864"; LIGHT_BLUE = "#8FAADC"; PALE = "#C9D6EF"; RED = "#C00000"; GRAY = "#7F7F7F"; GRID_C = "#E3E3E3"
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


# ---- 1. Cash and marketable securities by quarter, with shares outstanding ----
labs = Q + ["Sep 26*"]
cash = [v / 1000 for v in Q_CASHSEC] + [NETCASH_NOW / 1000]
shares = Q_SHARES + [SH_SEP]
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(range(len(labs)), cash, color=[NAVY] * len(Q) + [LIGHT_BLUE], width=0.6, zorder=3, label="Cash and securities, US$bn")
for i, v in enumerate(cash):
    ax1.annotate(f"{v:.1f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.2, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 4.6); ax1.set_ylabel("US$bn", fontsize=8)
ax1.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(range(len(labs))); ax1.set_xticklabels(labs, fontsize=6.4)
ax2 = ax1.twinx()
ax2.plot(range(len(labs)), shares, color=RED, marker="o", markersize=3.2, linewidth=1.5, zorder=4, label="Shares outstanding, m (RHS)")
ax2.set_ylim(0, 240); ax2.set_yticks([0, 100, 200]); twin_clean(ax2)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
save("chart_cash")

# ---- 2. Spending by quarter: capex and operating cash use ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ocf = [-v for v in Q_OCF]
ax.bar(range(len(Q)), ocf, color=LIGHT_BLUE, width=0.6, zorder=3, label="Operating cash use")
ax.bar(range(len(Q)), Q_CAPEX, bottom=ocf, color=NAVY, width=0.6, zorder=3, label="Capital spending")
for i, (a, b) in enumerate(zip(ocf, Q_CAPEX)):
    ax.annotate(f"{a + b:.0f}", (i, a + b), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.3, color=NAVY, fontweight="bold")
q_guide = (sum(GUIDE_26["ocf"]) + sum(GUIDE_26["capex"])) / 2 / 4
ax.axhline(q_guide, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(-0.4, q_guide + 4, f"2026 guide midpoint, per quarter: US${q_guide:.0f}m", fontsize=6.6, color=RED, ha="left", va="bottom")
ax.set_ylim(0, 185); ax.set_ylabel("US$m", fontsize=8)
ax.set_xticks(range(len(Q))); ax.set_xticklabels(Q, fontsize=6.6)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_spend")

# ---- 3. Announced capacity against what the price needs ----
labs = ["Binding\nPPAs", "Meta\n(prepay)", "Switch\n(master)", "My base\nby 2040", "Price needs\nby 2040"]
gw = [0, PIPE[1][1], PIPE[2][1], gw_2040(B[4]), NEED_GW]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(labs, gw, color=[NAVY, LIGHT_BLUE, LIGHT_BLUE, NAVY, RED], width=0.55, zorder=3)
for b, v in zip(bars, gw):
    ax.annotate(f"{v:.1f} GW", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points",
                ha="center", va="bottom", fontsize=6.8, color=NAVY, fontweight="bold")
ax.set_ylim(0, 20); ax.set_ylabel("GW", fontsize=8)
ax.tick_params(axis="x", labelsize=6.6)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_pipeline")

# ---- 4. Plant economics: break-even cost per kW at each power price ----
prices = [80, 95, 110, 125, 140]
be = [margin_mw(p) * pvf() * 1000 for p in prices]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar([f"US${p}" for p in prices], be, color=[LIGHT_BLUE, LIGHT_BLUE, NAVY, LIGHT_BLUE, LIGHT_BLUE], width=0.55, zorder=3)
for b, v in zip(bars, be):
    ax.annotate(f"{v:,.0f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points",
                ha="center", va="bottom", fontsize=6.8, color=NAVY, fontweight="bold")
ax.axhline(B[2], color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(4.4, B[2] + 250, f"My base cost, US${B[2]:,}/kW", fontsize=6.6, color=RED, ha="right", va="bottom", bbox=dict(facecolor="white", edgecolor="none", pad=0.5), zorder=6)
ax.axhline(SCEN[0][2], color=GRAY, linestyle=":", linewidth=1.2, zorder=4)
ax.text(-0.4, SCEN[0][2] + 250, f"Bear cost, US${SCEN[0][2]:,}/kW", fontsize=6.6, color=GRAY, ha="left", va="bottom")
ax.set_ylim(0, 14500); ax.set_ylabel("US$ per kW", fontsize=8)
ax.set_xlabel("Power price, US$/MWh, first year", fontsize=7.4)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_plant")

# ---- 5. Valuation cross-check ----
bear, base, bull = VALS
flat = [v for r in GRID for v in r]
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nprice x cost per kW", "range", (min(flat), max(flat))),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    ("Base: risked fleet\nplus cash", "point", base),
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
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 1.5, len(rows) - 0.42, f"Price US${PRICE:.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.tick_params(axis="y", pad=22)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 95); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 6. Share price, with the average prices of the 2026 share sales ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(9, BASE_VALUE - 9.5, f"My base value US${BASE_VALUE:.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
atm_pts = [(21, ATM_H1[0][3], "Q1 26 sales\nUS$97"), (24, ATM_H1[1][3], "Q2 26\nUS$64"), (27.5, ATM_Q3_AVG, "Jul to Sep\nUS$44")]
for x, y, t in atm_pts:
    ax.plot(x, y, marker="D", color=NAVY, markersize=4, zorder=5)
    ax.annotate(t, (x, y), xytext=(4, 4), textcoords="offset points", fontsize=5.9, color=NAVY)
ax.annotate(f"US${PX[-1]:.2f}", (len(PX) - 1, PX[-1]), xytext=(0, -12), textcoords="offset points", ha="right",
            va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax.annotate(f"US${PX[17]:.2f}", (17, PX[17]), xytext=(-4, 2), textcoords="offset points", ha="right",
            va="bottom", fontsize=6.6, color=NAVY)
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 150); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
