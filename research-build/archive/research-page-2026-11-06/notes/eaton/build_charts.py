"""Charts for the Eaton initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Electrical Americas sales and margin, 2024A to 2028E ----
years = ["2024A", "2025A", "2026E*", "2027E*", "2028E*"]
sales = [11436 / 1000, SEG25["EA"][0] / 1000, S26["EA"][0] / 1000, B["s27"]["EA"] / 1000, B["s28"]["EA"] / 1000]
mar = [3455 / 11436 * 100, SEG25["EA"][1] / SEG25["EA"][0] * 100, EA_M26 * 100, EA_M27 * 100, EA_M28 * 100]
x = list(range(len(years)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, sales, color=[NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE, LIGHT_BLUE], width=0.6, zorder=3, label="Sales, US$bn")
for i, s in enumerate(sales):
    ax1.annotate(f"{s:.1f}", (i, s), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6,
                 color=NAVY, fontweight="bold")
ax1.set_ylim(0, 34); ax1.set_ylabel("Sales (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(x); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(x, mar, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Operating margin, % (RHS)")
for i, m in enumerate(mar):
    ax2.annotate(f"{m:.1f}%", (i, m), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=6.2,
                 color=RED, fontweight="bold")
ax2.set_ylim(-35, 45); ax2.set_yticks([0, 10, 20, 30]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.6, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = (x_["value"] for x_ in SC)
glo = min(SENS_EPS) * min(SENS_PE); ghi = max(SENS_EPS) * max(SENS_PE)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_PE[0]} to {SENS_PE[2]}x 2028E EPS", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_PE:.0f}x 2028E\nEPS of US${E28:.2f}", "point", base),
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
ax.axvline(PRICE, color=GRAY, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE - 6, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=GRAY, ha="right", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
    ax.text(CALL["target"] + 6, len(rows) - 0.42, f"Draft target US${CALL['target']:,.0f}" if CALL["draft"] else f"Target US${CALL['target']:,.0f}",
            fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(150, 640); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. The queue: Electrical Americas backlog, with months of sales ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bl = [b / 1000 for b in EA_BL]
bars = ax.bar(BL_LABELS, bl, color=[NAVY] * 6 + [LIGHT_BLUE], width=0.58, zorder=3)
for b, v, m in zip(bars, bl, EA_MONTHS):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=7, color=NAVY, fontweight="bold")
    ax.annotate(f"{m:.1f}", (b.get_x() + b.get_width() / 2, v / 2), ha="center", va="center", fontsize=6.6,
                color="white", fontweight="bold")
ax.set_ylim(0, 20); ax.set_ylabel("US$bn", fontsize=8)
ax.text(-0.45, 18.4, "White: months of sales on order (backlog / previous four quarters' sales x 12)", fontsize=6.2,
        color=RED, ha="left", va="bottom")
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_queue")

# ---- 4. Electrical Americas operating margin by quarter ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
cols = [NAVY] * 8 + [RED, RED]
bars = ax.bar(Q, EA_M, color=cols, width=0.6, zorder=3)
for b, v in zip(bars, EA_M):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.6, color=NAVY, fontweight="bold")
ax.axhline(EA_M27 * 100, color=GRAY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(-0.4, EA_M27 * 100 + 1.3, f"My 2027E: {EA_M27 * 100:.1f}%", fontsize=6.4, color=GRAY, ha="left", va="bottom")
ax.set_ylim(20, 36); ax.set_ylabel("Operating margin (%)", fontsize=8)
ax.tick_params(axis="x", labelsize=6.6)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_qmargin")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 6, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 4, 230), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(180, 500); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
