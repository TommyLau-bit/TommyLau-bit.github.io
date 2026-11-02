"""Charts for the Coherent initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Revenue by segment, quarterly, with the Q1 FY27 guide midpoint ----
labels = QS + ["Sep 26\nguide"]
dc = [v / 1000 for v in Q_DC] + [None]
ind = [v / 1000 for v in Q_IND] + [None]
x = list(range(len(labels)))
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(x[:-1], dc[:-1], color=NAVY, width=0.62, zorder=3, label="Datacenter & Communications")
ax.bar(x[:-1], ind[:-1], bottom=dc[:-1], color=LIGHT_BLUE, width=0.62, zorder=3, label="Industrial")
gm = sum(G_REV) / 2 / 1000
ax.bar(x[-1], gm, color="white", edgecolor=NAVY, hatch="///", linewidth=0.8, width=0.62, zorder=3, label="Guide midpoint")
for i in range(len(QS)):
    ax.annotate(f"{Q_REV[i] / 1000:.2f}", (i, Q_REV[i] / 1000), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
    ax.annotate(f"{Q_DC[i] / Q_REV[i] * 100:.0f}%", (i, Q_DC[i] / 2000), ha="center", va="center", fontsize=6.0,
                color="white", fontweight="bold")
ax.annotate(f"{gm:.2f}", (x[-1], gm), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4,
            color=NAVY, fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=6.4)
ax.set_ylim(0, 2.9); ax.set_ylabel("US$bn", fontsize=8)
ax.legend(loc="upper left", fontsize=6.2, frameon=False, ncol=3, bbox_to_anchor=(-0.02, 1.15))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_segments")

# ---- 2. Non-GAAP gross and operating margin by quarter ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
xs = list(range(len(QS)))
ax.plot(xs, Q_NGGM, color=NAVY, marker="o", markersize=3.4, linewidth=1.6, zorder=4, label="Non-GAAP gross margin")
ax.plot(xs, Q_NGOPM, color=LIGHT_BLUE, marker="o", markersize=3.4, linewidth=1.6, zorder=4, label="Non-GAAP operating margin")
for i in xs:
    ax.annotate(f"{Q_NGGM[i]:.1f}", (i, Q_NGGM[i]), xytext=(0, -10), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.2, color=NAVY, fontweight="bold")
    ax.annotate(f"{Q_NGOPM[i]:.1f}", (i, Q_NGOPM[i]), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                fontsize=6.2, color=NAVY)
ax.axhline(42, color=RED, linestyle="--", linewidth=1.0, zorder=3)
ax.text(-0.3, 42.6, "Coherent's target: gross margin above 42%", fontsize=6.3, color=RED, ha="left", va="bottom")
ax.set_xticks(xs); ax.set_xticklabels(QS, fontsize=6.6)
ax.set_ylim(10, 47); ax.set_ylabel("Per cent", fontsize=8)
ax.legend(loc="center right", fontsize=6.2, frameon=False, bbox_to_anchor=(1.0, 0.42))
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_margin")

# ---- 3. Cash: operating cash flow against capital spending ----
yrs = ["FY24", "FY25", "FY26"]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
w = 0.36
xx = list(range(3))
b1 = ax.bar([i - w / 2 for i in xx], [OCF[y] / 1000 for y in yrs], width=w, color=NAVY, zorder=3, label="Operating cash flow")
b2 = ax.bar([i + w / 2 for i in xx], [CAPEX[y] / 1000 for y in yrs], width=w, color=RED, zorder=3, label="Capital spending")
for bars in (b1, b2):
    for b in bars:
        v = b.get_height()
        ax.annotate(f"{v:.2f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                    va="bottom", fontsize=6.6, color=NAVY, fontweight="bold")
ax.set_xticks(xx); ax.set_xticklabels(["FY24 (to Jun 24)", "FY25", "FY26"], fontsize=7)
ax.set_ylim(0, 1.45); ax.set_ylabel("US$bn", fontsize=8)
ax.text(0.55, 1.30, f"Inventory, 30 Jun: US${INVENTORY['FY25'] / 1000:.2f}bn (FY25)\nto US${INVENTORY['FY26'] / 1000:.2f}bn (FY26)",
        fontsize=6.4, color=GRAY, ha="left", va="center")
ax.legend(loc="upper left", fontsize=6.4, frameon=False)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_cash")

# ---- 4. Valuation cross-check ----
bear, base, bull = (x_["value"] for x_ in SC)
glo = min(SENS_EPS) * min(SENS_PE); ghi = max(SENS_EPS) * max(SENS_PE)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_PE[0]} to {SENS_PE[2]}x FY28E EPS", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_PE:.0f}x FY28E\nEPS of US${E28:.2f}", "point", base),
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
ax.text(PRICE - 5, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=GRAY, ha="right", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
    ax.text(CALL["target"] + 5, len(rows) - 0.42, f"Draft target US${CALL['target']:,.0f}" if CALL["draft"] else f"Target US${CALL['target']:,.0f}",
            fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(20, 520); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 8, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.axhline(NV_PRICE, color=NAVY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(0, NV_PRICE - 10, f"Nvidia paid US${NV_PRICE:.2f} a share, 2 Mar 2026", fontsize=6.4, color=NAVY, ha="left", va="top")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 5, 110), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 450); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
