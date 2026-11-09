"""Charts for the Kinder Morgan initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Adjusted EBITDA, 2023A to 2029E: underlying and backlog ----
years = ["2023A", "2024A", "2025A", "2026E*", "2027E*", "2028E*", "2029E*"]
under = [v / 1000 for v in EBITDA_H] + [EBITDA26 / 1000] + [(ebitda(y) - {2027: BL27, 2028: BL28, 2029: BL29}[y]) / 1000 for y in (2027, 2028, 2029)]
blk = [0, 0, 0, 0, BL27 / 1000, BL28 / 1000, BL29 / 1000]
x = list(range(len(years)))
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(x, under, color=[NAVY] * 3 + [LIGHT_BLUE] * 4, width=0.6, zorder=3, label="Existing business")
ax.bar(x, blk, bottom=under, color=RED, width=0.6, zorder=3, label="New projects from the backlog (mine)")
for i in x:
    t = under[i] + blk[i]
    ax.annotate(f"{t:.2f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6,
                color=NAVY, fontweight="bold")
ax.axhline(BUDGET26_EBITDA / 1000, color=GRAY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(-0.45, BUDGET26_EBITDA / 1000 + 0.12, "2026 budget US$8.6bn", fontsize=6.2, color=GRAY, ha="left", va="bottom")
ax.set_ylim(6, 11.2); ax.set_ylabel("Adjusted EBITDA (US$bn)", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(years, fontsize=7)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = (x_["value"] for x_ in SC)
grid = [value(e, m) for e in SENS_E for m in SENS_M]
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_M[0]:.1f} to {SENS_M[2]:.1f}x 2028E", "range", (min(grid), max(grid))),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_MULT:.1f}x 2028E EBITDA\nof US${E28 / 1000:.2f}bn", "point", base),
    ("2027 dividend at\ntoday's 3.5% yield", "point", DIV_CHECK),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"US${v:,.2f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:,.2f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:,.2f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=GRAY, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 0.3, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=GRAY, ha="left", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
    ax.text(CALL["target"] + 0.3, len(rows) - 0.9, f"Target US${CALL['target']:,.0f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.6)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(18, 50); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Project backlog by quarter ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar([l.replace(" ", "\n") for l in BL_LABELS], BACKLOG, color=[NAVY] * 11 + [RED], width=0.6, zorder=3)
for b, v in zip(bars, BACKLOG):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.6, color=NAVY, fontweight="bold")
ax.set_ylim(0, 17); ax.set_ylabel("US$bn", fontsize=8)
ax.text(-0.45, 15.6, "Sep 26: Permian Link and Southeast Connector added", fontsize=6.2, color=RED, ha="left", va="bottom")
ax.tick_params(axis="x", labelsize=6.2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_backlog")

# ---- 4. When the named projects land: KMI-share capital by first in-service year ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
yl = [str(y) for y in LAND_YEARS]
other = [LAND[y] / 1000 for y in LAND_YEARS]
other[-1] = (LAND[2030] - AI_PIPES) / 1000
ax.bar(yl, other, color=NAVY, width=0.58, zorder=3, label="Other named projects")
ax.bar(yl, [0, 0, 0, 0, AI_PIPES / 1000], bottom=other, color=RED, width=0.58, zorder=3,
       label="Permian Link and Southeast Connector")
for i, y in enumerate(LAND_YEARS):
    v = LAND[y] / 1000
    ax.annotate(f"{v:.1f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=7,
                color=NAVY, fontweight="bold")
ax.set_ylim(0, 6.6); ax.set_ylabel("KMI-share capital (US$bn)", fontsize=8)
ax.legend(loc="upper left", fontsize=6.4, frameon=False)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_land")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 0.5, f"My base value US${BASE_VALUE:,.2f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 5, 22), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(12, 40); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
