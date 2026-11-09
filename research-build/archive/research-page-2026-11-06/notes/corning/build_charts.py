"""Charts for the Corning initiation. House style: navy / light blue, red reference lines, grey price line."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
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


# ---- 1. Core sales split, optical and the rest, 2023A to 2028E, with core EPS ----
years = YEARS_H + ["2026E*", "2027E*", "2028E*"]
opt = OPT_H + [OPT26, P["opt27"], P["opt28"]]
rest = [s - o for s, o in zip(SALES_H, OPT_H)] + [REST26, P["rest27"], P["rest28"]]
eps = EPS_H + [EPS26, EPS27, EPS28]
x = range(len(years))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, opt, color=[NAVY] * 3 + [LIGHT_BLUE] * 3, width=0.6, zorder=3, label="Optical, US$bn")
ax1.bar(x, rest, bottom=opt, color=[PALE] * 6, width=0.6, zorder=3, label="Rest of Corning")
for i, (o, r) in enumerate(zip(opt, rest)):
    ax1.annotate(f"{o:.1f}", (i, o / 2), ha="center", va="center", fontsize=6.2, color="white", fontweight="bold")
    ax1.annotate(f"{o + r:.1f}", (i, o + r), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.2, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 44); ax1.set_ylabel("Core sales (US$bn)", fontsize=8)
ax1.yaxis.set_major_locator(mticker.MultipleLocator(10))
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(list(x)); ax1.set_xticklabels(years, fontsize=6.8)
ax2 = ax1.twinx()
ax2.plot(list(x), eps, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Core EPS, US$ (RHS)")
for i, e in enumerate(eps):
    ax2.annotate(f"{e:.2f}", (i, e), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.2, color=RED, fontweight="bold")
ax2.set_ylim(-6, 7.5); ax2.set_yticks([0, 2, 4, 6]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.8, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=3)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
grid_lo = min(SENS_EPS) * min(SENS_PE); grid_hi = max(SENS_EPS) * max(SENS_PE)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_PE[0]} to {SENS_PE[2]}x, EPS {SENS_EPS[0]:.2f} to {SENS_EPS[2]:.2f}", "range", (grid_lo, grid_hi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_PE}x 2028E EPS\nof US${EPS28:.2f}", "point", base),
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
ax.text(PRICE + 3, len(rows) - 0.42, f"Price US${PRICE:.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 260); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Optical sales by quarter with y/y growth ----
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
bars = ax1.bar(Q, Q_OPT, color=[LIGHT_BLUE] * 8 + [NAVY] * 2, width=0.6, zorder=3, label="Optical sales, US$m")
for b, v in zip(bars, Q_OPT):
    ax1.annotate(f"{v:,}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points",
                 ha="center", va="bottom", fontsize=5.9, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 3300); ax1.set_ylabel("US$m", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(range(len(Q))); ax1.set_xticklabels(Q, fontsize=6.6)
ax2 = ax1.twinx()
yy = [(i, v * 100) for i, v in enumerate(OPT_YY) if v is not None]
ax2.plot([i for i, _ in yy], [v for _, v in yy], color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4,
         label="Growth on a year earlier (%, RHS)")
for i, v in yy:
    ax2.annotate(f"{v:.0f}%", (i, v), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.2, color=RED, fontweight="bold")
ax2.set_ylim(-60, 60); ax2.set_yticks([0, 20, 40]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.8, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_optical")

# ---- 4. Optical segment net margin by quarter (the claim's falsifier) ----
nm = [v * 100 for v in OPT_NM]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(Q, nm, color=[LIGHT_BLUE] * 8 + [NAVY] * 2, width=0.6, zorder=3)
for b, v in zip(bars, nm):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points",
                ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
ax.axhline(B[4] * 100, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(-0.4, B[4] * 100 + 0.6, f"Dashed: my 2028 base case, {B[4] * 100:.0f}%", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.set_ylim(0, 30); ax.set_ylabel("Segment net margin (%)", fontsize=8)
ax.set_xticks(range(len(Q))); ax.set_xticklabels(Q, fontsize=6.6)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_margin")

# ---- 5. Capital spending, free cash flow and dividends ----
labs = YEARS_H + ["H1 2026"]
capex = CAPEX_H + [H1_26_CAPEX]
dep = [max(f, 0) for f in DEP_FLOW_H] + [H1_26_DEP_INFLOW]
fcf_ex = [f - d for f, d in zip(FCF_H + [H1_26_FCF], dep)]
div = DIV_H + [H1_26_DIV]
xs = range(len(labs)); w = 0.27
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar([i - w for i in xs], capex, width=w, color=NAVY, zorder=3, label="Capital spending")
ax.bar(list(xs), fcf_ex, width=w, color=LIGHT_BLUE, zorder=3, label="Adjusted free cash flow")
ax.bar(list(xs), dep, bottom=fcf_ex, width=w, color=PALE, hatch="////", edgecolor=NAVY, linewidth=0.4, zorder=3,
       label="of which net deposits and incentives")
ax.bar([i + w for i in xs], div, width=w, color=GRAY, zorder=3, label="Dividends")
for i in xs:
    for xx, v in [(i - w, capex[i]), (i, fcf_ex[i] + dep[i]), (i + w, div[i])]:
        ax.annotate(f"{v:.2f}", (xx, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                    fontsize=5.8, color=NAVY, fontweight="bold")
ax.set_xticks(list(xs)); ax.set_xticklabels(labs, fontsize=7)
ax.set_ylim(0, 2.6); ax.set_ylabel("US$bn", fontsize=8)
ax.legend(loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.2), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_cash")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 5, f"My base value US${BASE_VALUE:.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:.2f}", (len(PX) - 1, PX[-1]), xytext=(2, -14), textcoords="offset points", ha="right",
            va="top", fontsize=7, color=NAVY, fontweight="bold")
ax.annotate(f"US${PX[31]:.2f}", (31, PX[31]), xytext=(-4, 0), textcoords="offset points", ha="right",
            va="center", fontsize=6.6, color=NAVY)
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 290); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
