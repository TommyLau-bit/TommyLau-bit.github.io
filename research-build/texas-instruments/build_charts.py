"""Charts for the Texas Instruments initiation. House style: navy / light blue, red reference lines, grey price line."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from data import *

plt.rcParams["font.family"] = "Arial"
NAVY = "#1F3864"; LIGHT_BLUE = "#8FAADC"; RED = "#C00000"; GRAY = "#7F7F7F"; GRID = "#E3E3E3"
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


# ---- 1. Annual revenue + operating margin, 2019A to 2028E ----
years = YEARS_H + ["2026E*", "2027E*", "2028E*"]
rev = REV_H + [REV26, R27, R28]
om = [o / r * 100 for o, r in zip(OP_H, REV_H)] + [OM26 * 100, OM27 * 100, OM28 * 100]
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
bars = ax1.bar(years, rev, color=[NAVY] * 7 + [LIGHT_BLUE] * 3, width=0.6, zorder=3, label="Revenue, US$bn")
ax1.set_ylabel("Revenue (US$bn)", fontsize=8); ax1.set_ylim(0, 44)
ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(range(len(years))); ax1.set_xticklabels(years, fontsize=6.6)
for b, v in zip(bars, rev):
    ax1.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points",
                 ha="center", va="bottom", fontsize=6.2, color=NAVY, fontweight="bold")
ax2 = ax1.twinx()
ax2.plot(range(len(years)), om, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Operating margin (RHS)")
ax2.set_ylim(-40, 62); ax2.set_ylabel("Operating margin (%, RHS)", fontsize=8)
ax2.tick_params(axis="y", labelsize=7.4, length=0); ax2.set_yticks([0, 20, 40, 60])
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
for x, m in enumerate(om):
    ax2.annotate(f"{m:.0f}", (x, m), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.2, color=RED, fontweight="bold")
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=7.2, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
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
        ax.barh(y, hi - lo, left=lo, height=0.5, color="#C9D6EF", edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 4, len(rows) - 0.42, f"Price US${PRICE:.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 440); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Data centre: my estimate of quarterly revenue and share ----
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
bars = ax1.bar(DCQ_LABELS, [d * 1000 for d in DCQ], color=[LIGHT_BLUE] * 4 + [NAVY] * 2, width=0.55, zorder=3,
               label="Data centre revenue, US$m (my estimate)")
for b, v in zip(bars, DCQ):
    ax1.annotate(f"{v * 1000:.0f}", (b.get_x() + b.get_width() / 2, v * 1000), xytext=(0, 2), textcoords="offset points",
                 ha="center", va="bottom", fontsize=6.6, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 1100); ax1.set_ylabel("US$m", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax2 = ax1.twinx()
ax2.plot(range(6), [s * 100 for s in DCQ_SHARE], color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4,
         label="Share of TI revenue (%, RHS)")
for x, s in enumerate(DCQ_SHARE):
    ax2.annotate(f"{s * 100:.0f}%", (x, s * 100), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.4, color=RED, fontweight="bold")
ax2.set_ylim(-14, 16); ax2.set_yticks([0, 5, 10, 15]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.8, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_dc")

# ---- 4. Quarterly gross margin ----
qgm = [g / r * 100 for g, r in zip(Q_GP, Q_REV)]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(Q, qgm, color=[LIGHT_BLUE] * 8 + [NAVY] * 2, width=0.6, zorder=3)
ax.axhline(GM22 * 100, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(-0.4, GM22 * 100 + 1.2, f"Dashed: 2022 gross margin, {GM22 * 100:.1f}%", fontsize=6.8, color=RED, ha="left", va="bottom")
for b, v in zip(bars, qgm):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, 3), ha="center", va="bottom", fontsize=6.4,
                color="white", fontweight="bold")
ax.set_ylim(0, 78); ax.set_ylabel("Gross margin (%)", fontsize=8)
ax.set_xticks(range(len(Q))); ax.set_xticklabels(Q, fontsize=6.8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_qgm")

# ---- 5. Capex, depreciation and free cash flow ----
yrs = YEARS_H + ["2026E"]
capex = CAPEX_H + [sum(CAPEX_GUIDE_26) / 2]
dep = DEP_H + [sum(DEP_GUIDE_26) / 2]
fcf = [c - x + h for c, x, h in zip(CFO_H, CAPEX_H, CHIPS_H)]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(range(len(yrs)), capex, color=[LIGHT_BLUE] * 2 + [NAVY] * 5 + ["#C9D6EF"], width=0.55, zorder=3, label="Capital spending")
ax.plot(range(len(yrs)), dep, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Depreciation")
ax.plot(range(len(fcf)), fcf, color=GRAY, marker="s", markersize=3.2, linewidth=1.6, zorder=4, label="Free cash flow")
for x, v in enumerate(capex):
    ax.annotate(f"{v:.1f}", (x, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4,
                color=NAVY, fontweight="bold")
ax.set_xticks(range(len(yrs))); ax.set_xticklabels([y if y != "2026E" else "2026 guide" for y in yrs], fontsize=6.8)
ax.set_ylim(0, 8.4); ax.set_ylabel("US$bn", fontsize=8)
ax.legend(loc="upper left", fontsize=6.8, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=3)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_capex")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 6, f"My base value US${BASE_VALUE:.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:.2f}", (len(PX) - 1, PX[-1]), xytext=(-4, 4), textcoords="offset points", ha="right",
            va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 360); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
