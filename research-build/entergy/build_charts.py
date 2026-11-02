"""Charts for the Entergy initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Adjusted EPS: reported, then Entergy's guide and outlooks (midpoint bar, range whisker) ----
years = ["2024A", "2025A", "2026G", "2027O", "2028O", "2029O", "2030O"]
vals = [ADJ_EPS["2024A"], ADJ_EPS["2025A"]] + [MID[y] for y in ["2026", "2027", "2028", "2029", "2030"]]
x = list(range(len(years)))
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(x[:2], vals[:2], color=NAVY, width=0.6, zorder=3, label="Reported")
ax.bar(x[2:], vals[2:], color=LIGHT_BLUE, width=0.6, zorder=3, label="Entergy guide / outlook, midpoint")
for i, y in enumerate(["2026", "2027", "2028", "2029", "2030"]):
    lo, hi = GUIDE[y]
    ax.plot([i + 2, i + 2], [lo, hi], color=NAVY, linewidth=1.1, zorder=4)
for i, v in enumerate(vals):
    ax.annotate(f"{v:.2f}", (i, v), xytext=(0, 5), textcoords="offset points", ha="center", va="bottom", fontsize=6.6,
                color=NAVY, fontweight="bold")
ax.plot([2.7, 3.3], [CONS_EPS27, CONS_EPS27], color=RED, linewidth=2, zorder=5, label=f"2027 consensus US${CONS_EPS27:.2f}")
ax.set_ylim(0, 8.8); ax.set_ylabel("US$ per share", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(years, fontsize=7)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
ax.legend(loc="upper left", fontsize=6.0, frameon=False, ncol=1)
save("chart_eps")

# ---- 2. Valuation cross-check ----
bear, basev, bull = (s["value"] for s in SC)
glo = min(SENS_EPS) * min(SENS_PE); ghi = max(SENS_EPS) * max(SENS_PE)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_PE[0]:.0f} to {SENS_PE[2]:.0f}x 2028E EPS", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_PE}x 2028E\nEPS of US${E28:.2f}", "point", basev),
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
ax.text(PRICE - 1.5, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=GRAY, ha="right", va="bottom")
ax.axvline(PRICE * 1.15, color=RED, linestyle=":", linewidth=1.1, zorder=4)
ax.text(PRICE * 1.15 + 1.5, len(rows) - 0.42, f"Long bar US${PRICE * 1.15:,.0f}", fontsize=7, color=RED, ha="left", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(75, 165); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Rate base, Entergy's projection, with the annual capital plan ----
yrs = list(RATE_BASE.keys())
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(yrs, list(RATE_BASE.values()), color=NAVY, width=0.6, zorder=3, label="Projected rate base, US$bn (Entergy)")
for b, v in zip(bars, RATE_BASE.values()):
    ax.annotate(f"{v}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax.plot(yrs[1:], [CAPEX[y[:4]] / 1000 for y in yrs[1:]], color=RED, marker="o", markersize=3.5, linewidth=1.4, zorder=5,
        label="Capital plan that year, US$bn (10-Q)")
for y in yrs[1:]:
    v = CAPEX[y[:4]] / 1000
    ax.annotate(f"{v:.1f}", (y, v), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color="white", fontweight="bold")
ax.set_ylim(0, 112); ax.set_ylabel("US$ billion", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
ax.legend(loc="upper left", fontsize=6.0, frameon=False)
save("chart_ratebase")

# ---- 4. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 2, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 6, 70), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(40, 135); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
