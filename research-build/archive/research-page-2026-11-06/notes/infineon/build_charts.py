"""Charts for the Infineon initiation. House style: navy / light blue, red reference lines, grey price line."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from data import *

plt.rcParams["font.family"] = "Arial"
plt.rcParams["axes.unicode_minus"] = False
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


# ---- 1. AI data centre power revenue and its share of group revenue ----
labs = ["FY25A", "FY26E", "FY27\nold guide", "FY27E\nmine"]
vals = [AI_FY25 / 1000, AI26 / 1000, AI_FY27_OLD / 1000, B["ai"] / 1000]
share = [AI_FY25 / FY["FY25"][0] * 100, AI_SHARE26 * 100, None, AI_SHARE27 * 100]
x = list(range(len(labs)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, vals, color=[NAVY, LIGHT_BLUE, PALE, LIGHT_BLUE], edgecolor=[NAVY, NAVY, NAVY, NAVY], linewidth=0.6, width=0.58, zorder=3,
        label="AI power revenue, EUR bn")
for i, v in enumerate(vals):
    ax1.annotate(f"{v:.2f}" if i != 2 else "2.5+", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom",
                 fontsize=6.8, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 4.6); ax1.set_ylabel("EUR bn", fontsize=8)
ax1.set_xticks(x); ax1.set_xticklabels(labs, fontsize=6.8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax2 = ax1.twinx()
xs = [i for i, s in enumerate(share) if s is not None]; ys = [s for s in share if s is not None]
ax2.plot(xs, ys, color=RED, marker="o", markersize=3.5, linewidth=1.4, zorder=4, label="Share of group revenue, % (RHS)")
for i, s in zip(xs, ys):
    ax2.annotate(f"{s:.0f}%", (i, s), xytext=(7, -2), textcoords="offset points", ha="left", va="top", fontsize=6.4, color=RED,
                 fontweight="bold")
ax2.set_ylim(0, 40); ax2.set_yticks([0, 10, 20]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=2)
save("chart_ai")

# ---- 2. Segment Result Margin by quarter: PSS against Automotive ----
ql = [l.replace(" ", "\n") for l in Q_LABELS] + ["Q4 FY26\nmine"]
pss = [s / r * 100 for s, r in zip(Q_SR["PSS"], Q_REV["PSS"])] + [Q4_PSS_SR / Q4_PSS_REV * 100]
atv = [s / r * 100 for s, r in zip(Q_SR["ATV"], Q_REV["ATV"])] + [Q4["ATV"][1] * 100]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
w = 0.38
xi = list(range(len(ql)))
ax.bar([i - w / 2 for i in xi], pss, width=w, color=[NAVY] * 5 + [LIGHT_BLUE], zorder=3, label="Power & Sensor Systems")
ax.bar([i + w / 2 for i in xi], atv, width=w, color=[GRAY] * 5 + ["#BFBFBF"], zorder=3, label="Automotive")
for i, (a, b) in enumerate(zip(pss, atv)):
    ax.annotate(f"{a:.1f}", (i - w / 2, a), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=5.9,
                color=NAVY, fontweight="bold")
    ax.annotate(f"{b:.1f}", (i + w / 2, b), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=5.9,
                color=GRAY, fontweight="bold")
ax.set_ylim(0, 36); ax.set_ylabel("Segment Result Margin (%)", fontsize=7.6)
ax.set_xticks(xi); ax.set_xticklabels(ql, fontsize=6.4)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, ncol=2, bbox_to_anchor=(-0.02, 1.13))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_margin")

# ---- 3. Valuation cross-check ----
bear, base, bull = (s["value"] for s in SC)
glo = min(min(r) for r in SENS); ghi = max(max(r) for r in SENS)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_PE[0]} to {SENS_PE[2]}x, AI 2.6 to 4.0bn", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_PE}x FY27E\nEPS of EUR{B['eps']:.2f}", "point", base),
    (f"Consensus FY27 EPS\nat {BASE_PE}x", "point", CONS_VALUE),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"EUR{v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=6.8,
                    color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"EUR{lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=6.8,
                    color=NAVY, fontweight="bold")
        ax.annotate(f"EUR{hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=6.8,
                    color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=GRAY, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 1, len(rows) - 0.42, f"Price EUR{PRICE:.2f}", fontsize=6.8, color=GRAY, ha="left", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.3)
ax.set_xlabel("Value per share (EUR)", fontsize=8)
ax.set_xlim(15, 105); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 4. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 2, f"My base value EUR{BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"EUR{PX[-1]:.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 9, 30), textcoords="data", ha="center",
            va="center", fontsize=6.8, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(20, 95); ax.set_ylabel("Close (EUR)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
