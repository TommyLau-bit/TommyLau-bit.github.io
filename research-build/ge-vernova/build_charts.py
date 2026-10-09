"""Charts for the GE Vernova initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Revenue and adjusted EBITDA margin, 2024A to 2028E ----
years = YEARS_H + ["2026G", "2027E*", "2028E*"]
rev = REV_H + [REV26, REV27, REV28]
mar = [e / r * 100 for e, r in zip(EBITDA_H, REV_H)] + [M26 * 100, M27 * 100, M28 * 100]
x = range(len(years))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY, NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE], width=0.6, zorder=3, label="Revenue, US$bn")
for i, r in enumerate(rev):
    ax1.annotate(f"{r:.1f}", (i, r), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6,
                 color=NAVY, fontweight="bold")
ax1.set_ylim(0, 85); ax1.set_ylabel("Revenue (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(list(x)); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(list(x), mar, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Adjusted EBITDA margin, % (RHS)")
for i, m in enumerate(mar):
    ax2.annotate(f"{m:.1f}%", (i, m), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=6.2,
                 color=RED, fontweight="bold")
ax2.set_ylim(-22, 26); ax2.set_yticks([0, 10, 20]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.6, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
glo = value(min(SENS_EBITDA), min(SENS_MULT)); ghi = value(max(SENS_EBITDA), max(SENS_MULT))
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_MULT[0]} to {SENS_MULT[2]}x 2028E EBITDA", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_MULT}x 2028E EBITDA\nof US${EBITDA28:.1f}bn", "point", base),
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
ax.text(PRICE + 15, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 1850); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. The queue: GW under contract, firm backlog and slot reservations ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(Q, GW_BACKLOG, color=NAVY, width=0.6, zorder=3, label="Firm orders in backlog")
ax.bar(Q, GW_SRA, bottom=GW_BACKLOG, color=LIGHT_BLUE, width=0.6, zorder=3, label="Slot reservation agreements")
for i, (b, t) in enumerate(zip(GW_BACKLOG, GW_TOTAL)):
    ax.annotate(f"{t}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.8,
                color=NAVY, fontweight="bold")
    ax.annotate(f"{GW_YEARS[i]:.1f}y", (i, b / 2), ha="center", va="center", fontsize=6.0, color="white", fontweight="bold")
ax.axhline(NEED_GW["2026"], color=RED, linestyle="--", linewidth=1.1, zorder=4)
ax.text(-0.45, NEED_GW["2026"] + 2, "Claim's floor: 4 years of 20 GW = 80 GW", fontsize=6.3, color=RED, ha="left", va="bottom")
ax.set_ylim(0, 140); ax.set_ylabel("Gigawatts", fontsize=8)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_queue")

# ---- 4. Deposits: Power contract liabilities ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(CL_LABELS, CL_POWER, color=[NAVY] * 4 + [LIGHT_BLUE], width=0.55, zorder=3)
for b, v in zip(bars, CL_POWER):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax.axhline(POWER_REV_25, color=RED, linestyle="--", linewidth=1.1, zorder=4)
ax.text(-0.4, POWER_REV_25 + 0.6, f"Power revenue, full year 2025: US${POWER_REV_25:.1f}bn", fontsize=6.3, color=RED, ha="left", va="bottom")
ax.set_ylim(0, 32); ax.set_ylabel("US$bn", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_deposits")

# ---- 5. Power: revenue and segment EBITDA margin by quarter ----
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(Q, Q_POWER_REV, color=NAVY, width=0.6, zorder=3, label="Power revenue, US$bn")
for i, v in enumerate(Q_POWER_REV):
    ax1.annotate(f"{v:.1f}", (i, v / 2), ha="center", va="center", fontsize=6.4, color="white", fontweight="bold")
ax1.set_ylim(0, 9); ax1.set_ylabel("US$bn", fontsize=8); style(ax1)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
ax2 = ax1.twinx()
ax2.plot(range(len(Q)), Q_POWER_M, color=RED, marker="o", markersize=3.3, linewidth=1.5, zorder=4, label="Segment EBITDA margin, % (RHS)")
for i, m in enumerate(Q_POWER_M):
    ax2.annotate(f"{m:.1f}", (i, m), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=RED, fontweight="bold")
ax2.axhline(OUT28["power_m"] * 100, color=GRAY, linestyle=":", linewidth=1.0)
ax2.text(5.4, OUT28["power_m"] * 100 + 0.4, "2028 target 22%", fontsize=6.2, color=GRAY, ha="right", va="bottom")
ax2.set_ylim(-10, 29); ax2.set_yticks([0, 10, 20]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
save("chart_power")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 25, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 3, 420), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 1350); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
