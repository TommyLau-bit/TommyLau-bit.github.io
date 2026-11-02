"""Charts for the CLP Holdings initiation. House style: navy / light blue, red reference lines, grey price line."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from data import *

plt.rcParams["font.family"] = "Arial"
plt.rcParams["axes.unicode_minus"] = False
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


# ---- 1. 2025 operating earnings by segment ----
labs = [s[0] for s in SEG25][::-1]
vals = [s[1] for s in SEG25][::-1]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
cols = [LIGHT_BLUE] * (len(vals) - 1) + [NAVY]
ax.barh(range(len(vals)), vals, color=cols, height=0.6, zorder=3)
tot = sum(vals)
for i, v in enumerate(vals):
    ax.annotate(f"HK${v:,.0f}m  ({v / tot * 100:.0f}%)", (v, i), xytext=(4, 0), textcoords="offset points", ha="left",
                va="center", fontsize=6.8, color=NAVY, fontweight="bold")
ax.set_yticks(range(len(vals))); ax.set_yticklabels(labs, fontsize=7)
ax.set_xlim(0, 13500); ax.set_xlabel("HK$ million", fontsize=7.5)
ax.text(13400, 1.0, f"Group costs and other:\nminus HK${-OTHER25:,.0f}m", fontsize=6.3, color=GRAY, ha="right", va="center")
ax.grid(axis="x", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_segments")

# ---- 2. Implied average SoC net fixed assets, 2023 to 2028E ----
yrs = ["2023", "2024", "2025", "2026E", "2027E", "2028E"]
va = [ANFA["2023"], ANFA["2024"], ANFA["2025"], ANFA_E["2026"], ANFA_E["2027"], ANFA_E["2028"]]
va = [v / 1000 for v in va]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(range(6), va, color=[NAVY] * 3 + [LIGHT_BLUE] * 3, width=0.6, zorder=3)
for b, v in zip(bars, va):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.8, color=NAVY, fontweight="bold")
ax.bar([5], [ANFA_FOR_LONG], bottom=[va[5]], color="none", edgecolor=RED, linestyle="--", linewidth=1.0, width=0.6, zorder=4)
ax.annotate(f"+HK${ANFA_FOR_LONG:.0f}bn needed\nfor a long", (5, va[5] + ANFA_FOR_LONG), xytext=(-30, -6),
            textcoords="offset points", ha="right", va="top", fontsize=6.3, color=RED)
ax.set_xticks(range(6)); ax.set_xticklabels(yrs, fontsize=7)
ax.set_ylim(100, 192); ax.set_ylabel("HK$ billion", fontsize=8)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_rab")

# ---- 3. EPS, operating earnings before fair value movements ----
years = ["2024A", "2025A", "2026E", "2027E", "2028E"]
eps = [EPS_A["2024A"], EPS_A["2025A"], EPS_E["2026"], EPS_E["2027"], EPS_E["2028"]]
hk = [HK_OPE["2024A"] / SHARES, HK_OPE["2025A"] / SHARES, HK_E["2026"] / SHARES, HK_E["2027"] / SHARES, HK_E["2028"] / SHARES]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(range(5), hk, color=[NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE, LIGHT_BLUE], width=0.6, zorder=3, label="Hong Kong energy and related")
ax.bar(range(5), [e - h for e, h in zip(eps, hk)], bottom=hk, color=PALE, width=0.6, zorder=3, label="Rest of the Group, net of costs")
for i, v in enumerate(eps):
    top = max(v, CONS_EPS26 if i == 2 else (CONS_EPS27 if i == 3 else 0))
    ax.annotate(f"{v:.2f}", (i, top), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.8, color=NAVY, fontweight="bold")
ax.plot([1.7, 2.3], [CONS_EPS26, CONS_EPS26], color=RED, linewidth=2, zorder=5)
ax.plot([2.7, 3.3], [CONS_EPS27, CONS_EPS27], color=RED, linewidth=2, zorder=5, label="Consensus (stockanalysis.com)")
ax.set_ylim(0, 6.0); ax.set_ylabel("HK$ per share", fontsize=8)
ax.set_xticks(range(5)); ax.set_xticklabels(years, fontsize=7)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
ax.legend(loc="upper left", fontsize=5.9, frameon=False, ncol=2, bbox_to_anchor=(-0.02, 1.2))
save("chart_eps")

# ---- 4. Valuation cross-check ----
bear, basev, bull = (s["value"] for s in SC)
glo = min(min(r) for r in GRID); ghi = max(max(r) for r in GRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    ("Sensitivity grid\n16 to 20x, +0 to +25bn", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    ("Base: sum of the parts\non 2028E", "point", basev),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"HK${v:,.1f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"HK${lo:,.1f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"HK${hi:,.1f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=GRAY, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE - 1, len(rows) - 0.42, f"Price HK${PRICE:,.2f}", fontsize=7, color=GRAY, ha="right", va="bottom")
ax.axvline(PRICE * 1.15, color=RED, linestyle=":", linewidth=1.1, zorder=4)
ax.text(PRICE * 1.15 + 1, len(rows) - 0.42, f"Long bar HK${PRICE * 1.15:,.1f}", fontsize=7, color=RED, ha="left", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (HK$)", fontsize=8)
ax.set_xlim(45, 115); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 0.8, f"My base value HK${BASE_VALUE:,.2f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"HK${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 6, 62), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(55, 85); ax.set_ylabel("Close (HK$)", fontsize=8)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
