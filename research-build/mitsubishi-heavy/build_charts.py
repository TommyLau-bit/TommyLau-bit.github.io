"""Charts for the Mitsubishi Heavy Industries initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. GTCC orders against revenue, FY2022 to FY2026 forecast ----
x = list(range(len(GT_YEARS)))
w = 0.38
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar([i - w / 2 for i in x], GT_ORD, width=w, color=[NAVY] * 4 + [LIGHT_BLUE], zorder=3, label="Order intake, ¥bn")
ax.bar([i + w / 2 for i in x], GT_REV, width=w, color=[GRAY] * 4 + ["#BFBFBF"], zorder=3, label="Revenue, ¥bn")
for i in x:
    ax.annotate(f"{GT_ORD[i]:,.0f}", (i - w / 2, GT_ORD[i]), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.3, color=NAVY, fontweight="bold")
    ax.annotate(f"{GT_REV[i]:,.0f}", (i + w / 2, GT_REV[i]), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.3, color="#404040")
ax.set_xticks(x); ax.set_xticklabels(GT_YEARS, fontsize=7)
ax.set_ylim(0, 3200); ax.set_ylabel("¥bn", fontsize=8)
ax.legend(loc="upper left", fontsize=6.6, frameon=False, ncol=2, bbox_to_anchor=(-0.02, 1.14))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
glo = value(min(SENS_GT), min(SENS_MULT)); ghi = value(max(SENS_GT), max(SENS_MULT))
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_MULT[0]} to {SENS_MULT[2]}x GTCC", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    ("Base, counting all\nnet cash as surplus", "point", BASE_FULLCASH),
    (f"Base: sum of the parts,\nGTCC at {MULT['GT']}x", "point", base),
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
ax.text(PRICE + 50, len(rows) - 0.42, f"Price ¥{PRICE:,.0f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.6)
ax.set_xlabel("Value per share (¥)", fontsize=8)
ax.set_xlim(0, 6400); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. The queue: large frame gas turbines on order, units ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(UNIT_LABELS, UNIT_BL, color=[NAVY] * 7 + [LIGHT_BLUE], width=0.58, zorder=3)
for b, v in zip(bars, UNIT_BL):
    ax.annotate(f"{v}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=7, color=NAVY, fontweight="bold")
for lab, gw in UNIT_BL_GW.items():
    i = UNIT_LABELS.index(lab)
    ax.annotate(f"{gw} GW", (i, UNIT_BL[i] / 2), ha="center", va="center", fontsize=6.2, color="white", fontweight="bold")
ax.set_ylim(0, 100); ax.set_ylabel("Units", fontsize=8)
ax.tick_params(axis="x", labelsize=6.8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_queue")

# ---- 4. Sum of the parts, yen per share ----
parts = [("GTCC (gas turbine\ncombined cycle)", SOTP["GT"]), ("Aircraft, Defense\n& Space", SOTP["ADS"]),
         ("Energy rest (nuclear,\nsteam, aero engines)", SOTP["ER"]), ("Plants & Infra,\nIndustrial Solutions", SOTP["PI"] + SOTP["IS"]),
         ("Corporate costs", SOTP["Corp"]), ("Cash, investments less\ndebt, advances etc.", ADJ)]
ps = [(n, v / SHARES * 1000) for n, v in parts]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
left = 0
for i, (n, v) in enumerate(ps):
    col = NAVY if i < 2 else (RED if v < 0 else LIGHT_BLUE)
    ax.barh(len(ps) - 1 - i, v, left=left if v >= 0 else left + v, height=0.6, color=col, zorder=3)
    ax.annotate(f"¥{v:,.0f}" if v >= 0 else f"less ¥{-v:,.0f}", (left + max(v, 0), len(ps) - 1 - i), xytext=(4, 0),
                textcoords="offset points", ha="left", va="center", fontsize=6.6, color=NAVY, fontweight="bold")
    left += v
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(PRICE - 40, -0.75, f"Price ¥{PRICE:,.0f}", fontsize=6.6, color=RED, ha="right", va="center")
ax.axvline(BASE_VALUE, color=NAVY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(BASE_VALUE + 40, -0.75, f"Base ¥{BASE_VALUE:,.0f}", fontsize=6.6, color=NAVY, ha="left", va="center")
ax.set_yticks(range(len(ps))); ax.set_yticklabels([n for n, _ in ps][::-1], fontsize=6.2)
ax.set_xlim(0, 5200); ax.set_ylim(-1.2, len(ps) - 0.4); ax.set_xlabel("Cumulative value per share (¥)", fontsize=8)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_sotp")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 90, f"My base value ¥{BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"¥{PX[-1]:,.0f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 6, 1500), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 6000); ax.set_ylabel("Close (¥)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
