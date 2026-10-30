"""Charts for the Constellation initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Annual adjusted EPS, 2024A to 2028E, base and enhanced stacked for 2026E to 2028E ----
years = ["2024A", "2025A", "2026E*", "2027E*", "2028E*"]
base = [None, None, BASE["2026"], BASE["2027"], BASE28]
tot = [ADJ_EPS["2024A"], ADJ_EPS["2025A"], EPS26, E27, E28]
x = list(range(len(years)))
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(x[:2], tot[:2], color=NAVY, width=0.6, zorder=3, label="Reported")
ax.bar(x[2:], base[2:], color=NAVY, width=0.6, zorder=3, alpha=0.55, label="Base (Constellation's framework)")
ax.bar(x[2:], [t - b for t, b in zip(tot[2:], base[2:])], bottom=base[2:], color=LIGHT_BLUE, width=0.6, zorder=3,
       label="Enhanced (my share)")
for i, v in enumerate(tot):
    ax.annotate(f"{v:.2f}", (i, v), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.8,
                color=NAVY, fontweight="bold")
ax.plot([3.33, 3.6], [CONS_EPS27, CONS_EPS27], color=RED, linewidth=2, zorder=5, label=f"2027 consensus US${CONS_EPS27:.2f}")
ax.set_ylim(0, 18.5); ax.set_ylabel("US$ per share", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(years, fontsize=7)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
ax.legend(loc="upper left", fontsize=6.0, frameon=False, ncol=2, bbox_to_anchor=(-0.02, 1.2))
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, basev, bull = (s["value"] for s in SC)
glo = min(SENS_EPS) * min(SENS_PE); ghi = max(SENS_EPS) * max(SENS_PE)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\n{SENS_PE[0]} to {SENS_PE[2]}x 2028E EPS", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {BASE_PE:.0f}x 2028E\nEPS of US${E28:.2f}", "point", basev),
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
ax.text(PRICE - 4, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=GRAY, ha="right", va="bottom")
ax.axvline(PRICE * 1.15, color=RED, linestyle=":", linewidth=1.1, zorder=4)
ax.text(PRICE * 1.15 + 4, len(rows) - 0.42, f"Long bar US${PRICE * 1.15:,.0f}", fontsize=7, color=RED, ha="left", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(120, 450); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Quarterly adjusted EPS ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
cols = [NAVY] * 4 + [RED, RED]
bars = ax.bar(Q_LABELS, Q_EPS, color=cols, width=0.6, zorder=3)
for b, v in zip(bars, Q_EPS):
    ax.annotate(f"{v:.2f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax.set_ylim(0, 4.0); ax.set_ylabel("US$ per share", fontsize=8)
ax.text(-0.45, 3.65, "Red: 2026 quarters, with Calpine from 7 January", fontsize=6.4, color=RED, ha="left", va="bottom")
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_qeps")

# ---- 4. Crane: the reactor date against the grid date ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
items = [
    ("Restart announced\n(Sep 2024, target 2028)", 2024.72, 2028.0, LIGHT_BLUE),
    ("Reactor able to generate\n(H2 2027, waiver request)", 2024.72, 2027.5, NAVY),
    ("Full deliverability on a fresh\nconnection (31 Dec 2030)", 2024.72, 2031.0, RED),
    ("Claim's test: full output\nby 31 Dec 2028", 2024.72, 2029.0, GRAY),
]
for y, (lab, a, b, c) in enumerate(items):
    ax.barh(y, b - a, left=a, height=0.5, color=c, zorder=3)
ax.axvline(2026.42, color=GRAY, linestyle=":", linewidth=1.0)
ax.text(2026.47, -0.62, "FERC waiver, 1 Jun 2026", fontsize=6.2, color=GRAY, ha="left", va="center")
ax.set_yticks(range(len(items))); ax.set_yticklabels([i[0] for i in items], fontsize=6.4)
ax.set_xlim(2024.5, 2031.3); ax.set_xticks([2025, 2026, 2027, 2028, 2029, 2030, 2031])
ax.set_xticklabels(["2025", "2026", "2027", "2028", "2029", "2030", "2031"], fontsize=7)
ax.set_ylim(3.5, -0.85)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_crane")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 6, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 5, 150), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(80, 420); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
