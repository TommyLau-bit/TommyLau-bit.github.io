"""Charts for the Williams initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Power Innovation: installed MW in service at the end of each half year ----
periods = ["1H 26", "2H 26", "1H 27", "2H 27", "1H 28", "2H 28"]
# MW in service at period end (Williams' windows; Aquila half in 2H27, half in 1H28: my split)
inserv = {
    "Socrates": [0, 556, 556, 556, 556, 556],
    "Apollo": [0, 0, 0, 490, 490, 490],
    "Aquila": [0, 0, 0, 260, 520, 520],
    "Socrates the Younger": [0, 0, 0, 0, 0, 340],
    "Neo": [0, 0, 0, 0, 0, 682],
}
cols = [NAVY, "#2F5597", LIGHT_BLUE, PALE, "#D9D9D9"]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bottom = [0] * len(periods)
for (nm, vals), c in zip(inserv.items(), cols):
    ax.bar(periods, vals, bottom=bottom, color=c, width=0.6, zorder=3, label=nm, edgecolor="white", linewidth=0.4)
    bottom = [b + v for b, v in zip(bottom, vals)]
for i, t in enumerate(bottom):
    if t:
        ax.annotate(f"{t:,}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.8,
                    color=NAVY, fontweight="bold")
ax.set_ylim(0, 3300); ax.set_ylabel("Installed MW", fontsize=8)
ax.legend(fontsize=5.9, frameon=False, loc="upper left", ncol=2)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_power")

# ---- 2. Adjusted EBITDA by source, 2024A to 2028E ----
yrs = ["2024A", "2025A", "2026G*", "2027E", "2028E"]
core = [EBITDA["2024A"], EBITDA["2025A"], CORE26, CORE27, CORE28]
mom = [0, 0, MOM26, MOM27, MOM28]
pi = [0, 0, PI26, PI27, PI28]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
x = range(len(yrs))
ax.bar(x, [c / 1000 for c in core], color=NAVY, width=0.6, zorder=3, label="Pipes, gathering, other")
ax.bar(x, [m / 1000 for m in mom], bottom=[c / 1000 for c in core], color=LIGHT_BLUE, width=0.6, zorder=3, label="Momentum")
ax.bar(x, [p / 1000 for p in pi], bottom=[(c + m) / 1000 for c, m in zip(core, mom)], color=RED, width=0.6, zorder=3,
       label="Power Innovation")
tot = [c + m + p for c, m, p in zip(core, mom, pi)]
for i, t in enumerate(tot):
    ax.annotate(f"{t / 1000:.1f}", (i, t / 1000), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.8, color=NAVY, fontweight="bold")
ax.set_xticks(list(x)); ax.set_xticklabels(yrs, fontsize=7)
ax.set_ylim(0, 13.5); ax.set_ylabel("US$bn", fontsize=8)
ax.legend(fontsize=6.2, frameon=False, loc="upper left", ncol=3)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_ebitda")

# ---- 3. Valuation cross-check ----
bear, base, bull = (s_["value"] for s_ in SC)
glo = min(min(r) for r in GRID); ghi = max(max(r) for r in GRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    ("Sensitivity grid\n12 to 15x pipes, 6 to 10x power", "range", (glo, ghi)),
    ("Dividend model\n7% growth, 8% cost of equity", "point", DDM_VALUE),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    ("Base: sum of the parts\n13.5x pipes, 8x power", "point", base),
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
ax.text(PRICE + 1, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=GRAY, ha="left", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.4)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(35, 115); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 4. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 1.5, f"My base value US${BASE_VALUE:,.2f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 5, 50), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(25, 90); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID_C, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
