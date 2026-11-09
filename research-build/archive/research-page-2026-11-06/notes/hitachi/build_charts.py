"""Charts for the Hitachi initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Hitachi Energy revenue and margin, FY2024 to FY2027E, with the FY2030 plan ----
years = ["FY24", "FY25", "FY26G", "FY27E*", "FY30 plan"]
rev = HE_REV + [HE_REV27, HE_TGT30["rev"]]
mar = [m * 100 for m in HE_MARGIN] + [HE_M27 * 100, None]
x = list(range(len(years)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rev, color=[NAVY, NAVY, NAVY, LIGHT_BLUE, PALE], edgecolor=[NAVY] * 5, linewidth=0.6, width=0.6, zorder=3,
        label="Revenue, US$bn")
for i, r in enumerate(rev):
    ax1.annotate(f"{r:.2f}" if i == 2 else f"{r:.1f}", (i, r), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6,
                 color=NAVY, fontweight="bold")
ax1.set_ylim(0, 52); ax1.set_ylabel("Revenue (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(x); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(x[:4], mar[:4], color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Adjusted EBITA margin, % (RHS)")
for i, m in enumerate(mar[:4]):
    ax2.annotate(f"{m:.1f}%", (i, m), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=6.2,
                 color=RED, fontweight="bold")
ax2.errorbar([4], [18], yerr=[[2], [2]], fmt="o", color=RED, markersize=3.5, capsize=3, linewidth=1.2)
ax2.annotate("16 to 20%", (4, 20), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=6.2,
             color=RED, fontweight="bold")
ax2.set_ylim(-20, 26); ax2.set_yticks([0, 10, 20]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.6, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
glo = value(min(SENS_HE), min(SENS_MULT)); ghi = value(max(SENS_HE), max(SENS_MULT))
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_MULT[0]} to {SENS_MULT[2]}x Hitachi Energy", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: sum of the parts,\nHitachi Energy at {MULT['HE']}x", "point", base),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"¥{v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"¥{lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"¥{hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 80, len(rows) - 0.42, f"Price ¥{PRICE:,.0f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (¥)", fontsize=8)
ax.set_xlim(0, 9600); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. The queue: Hitachi Energy backlog, with years of revenue where measurable ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(HE_BL_LABELS, HE_BL, color=[NAVY] * 5 + [LIGHT_BLUE], width=0.58, zorder=3)
for b, v in zip(bars, HE_BL):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=7, color=NAVY, fontweight="bold")
for i, r in [(0, RATIO_MAR25), (4, RATIO_MAR26), (5, RATIO_JUN26)]:
    ax.annotate(f"{r:.2f}x", (i, HE_BL[i] / 2), ha="center", va="center", fontsize=6.4, color="white", fontweight="bold")
ax.set_ylim(0, 80); ax.set_ylabel("US$bn", fontsize=8)
ax.text(-0.45, 74, "White: backlog / revenue over the previous four quarters. Claim's floor: 2.5x", fontsize=6.2,
        color=RED, ha="left", va="bottom")
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_queue")

# ---- 4. Sum of the parts, yen per share ----
parts = [("Hitachi Energy", SOTP["HE"]), ("Digital Systems\n& Services", SOTP["DSS"]), ("Connective\nIndustries", SOTP["CI"]),
         ("Mobility", SOTP["Mobility"]), ("Energy rest,\nOthers", SOTP["Eother"] + SOTP["Others"]),
         ("Corporate costs", SOTP["Corporate"]), ("Cash, investments\nless debt etc.", ADJ)]
ps = [(n, v / SHARES * 1000) for n, v in parts]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
left = 0
for i, (n, v) in enumerate(ps):
    col = NAVY if i == 0 else (RED if v < 0 else LIGHT_BLUE)
    ax.barh(len(ps) - 1 - i, v, left=left if v >= 0 else left + v, height=0.6, color=col, zorder=3)
    ax.annotate(f"¥{v:,.0f}" if v >= 0 else f"less ¥{-v:,.0f}", (left + max(v, 0), len(ps) - 1 - i), xytext=(4, 0), textcoords="offset points", ha="left",
                va="center", fontsize=6.6, color=NAVY, fontweight="bold")
    left += v
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(PRICE - 60, -0.75, f"Price ¥{PRICE:,.0f}", fontsize=6.6, color=RED, ha="right", va="center")
ax.axvline(BASE_VALUE, color=NAVY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(BASE_VALUE + 60, -0.75, f"Base ¥{BASE_VALUE:,.0f}", fontsize=6.6, color=NAVY, ha="left", va="center")
ax.set_yticks(range(len(ps))); ax.set_yticklabels([n for n, _ in ps][::-1], fontsize=6.4)
ax.set_xlim(0, 8200); ax.set_ylim(-1.2, len(ps) - 0.4); ax.set_xlabel("Cumulative value per share (¥)", fontsize=8)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_sotp")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 120, f"My base value ¥{BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"¥{PX[-1]:,.0f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 4, 2300), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 7500); ax.set_ylabel("Close (¥)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
