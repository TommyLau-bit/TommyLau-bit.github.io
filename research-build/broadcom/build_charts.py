"""Charts for the Broadcom initiation. House style: navy / light blue, red reference lines, grey price line."""

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


def twin_clean(ax2):
    ax2.tick_params(axis="y", labelsize=7.4, length=0)
    for s in ["top", "left", "right"]:
        ax2.spines[s].set_visible(False)


# ---- 1. Revenue by part, FY24 to FY28E, with non-GAAP EPS ----
years = ["FY24", "FY25", "FY26E*", "FY27E*", "FY28E*"]
ai = AI_H + [AI26, AI27, AI28]
nonai = [SEMI_H[0] - AI_H[0], SEMI_H[1] - AI_H[1], NONAI26, NONAI27, NONAI28]
sw = SW_H + [SW26, SW27, SW28]
eps = EPS_H + [EPS26, EPS27, EPS28]
x = range(len(years))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, ai, color=NAVY, width=0.6, zorder=3, label="AI semis")
ax1.bar(x, nonai, bottom=ai, color=GRAY, width=0.6, zorder=3, label="Non-AI semis")
ax1.bar(x, sw, bottom=[a + n for a, n in zip(ai, nonai)], color=LIGHT_BLUE, width=0.6, zorder=3, label="Software")
for i in x:
    t = ai[i] + nonai[i] + sw[i]
    ax1.annotate(f"{t:.0f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 330); ax1.set_ylabel("Revenue (US$bn)", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(list(x)); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(list(x), eps, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="EPS, US$ (RHS)")
for i, e in enumerate(eps):
    ax2.annotate(f"{e:.2f}", (i, e), xytext=(-4, 4), textcoords="offset points", ha="right", va="bottom", fontsize=6.2, color=RED, fontweight="bold")
ax2.set_ylim(-28, 34); ax2.set_yticks([0, 10, 20, 30]); twin_clean(ax2)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=4)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in VGRID); ghi = max(max(r) for r in VGRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nAI US${SENS_AI[0]:.0f}-{SENS_AI[2]:.0f}bn, {SENS_M[0]}-{SENS_M[2]}x", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: sum of the parts\non FY28E", "point", base),
    ("Average analyst target\n(stockanalysis.com)", "point", CONS_TP),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(f"US${v:,.0f}", (v, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, hi - lo, left=lo, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(f"US${lo:,.0f}", (lo, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(f"US${hi:,.0f}", (hi, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE - 8, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=RED, ha="right", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 780); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. AI revenue by quarter, with the networking share where disclosed ----
labs = QS + ["Q4 26\nguide"]
aiq = Q_AI + [G4["ai"]]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for i, (l, a) in enumerate(zip(labs, aiq)):
    sh = NET_SHARE.get(l)
    if sh is None:
        ax.bar(i, a, color=LIGHT_BLUE if i == len(aiq) - 1 else PALE, edgecolor=NAVY, linewidth=0.5, width=0.6, zorder=3)
    else:
        ax.bar(i, a * (1 - sh), color=NAVY, width=0.6, zorder=3)
        ax.bar(i, a * sh, bottom=a * (1 - sh), color=GRAY, width=0.6, zorder=3)
        ax.annotate(f"{sh * 100:.0f}%", (i, a * (1 - sh) + a * sh / 2), ha="center", va="center", fontsize=5.8, color="white", fontweight="bold")
    ax.annotate(f"{a:.1f}", (i, a), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=NAVY, fontweight="bold")
from matplotlib.patches import Patch
hs = [Patch(color=NAVY, label="Custom accelerators (XPUs)"), Patch(color=GRAY, label="AI networking (share shown)"),
      Patch(facecolor=PALE, edgecolor=NAVY, linewidth=0.5, label="Split not disclosed")]
ax.set_ylim(0, 25); ax.set_ylabel("US$bn", fontsize=8)
ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, fontsize=6.2)
ax.legend(handles=hs, loc="upper left", fontsize=6.0, frameon=False, bbox_to_anchor=(-0.02, 1.2), ncol=3)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_ai")

# ---- 4. Revenue by part, by quarter ----
nonaiq = [s - a for s, a in zip(Q_SEMI, Q_AI)] + [G4["nonai_call"]]
swq = Q_SW + [G4["sw"]]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(range(len(labs)), aiq, color=NAVY, width=0.6, zorder=3, label="AI semis")
ax.bar(range(len(labs)), nonaiq, bottom=aiq, color=GRAY, width=0.6, zorder=3, label="Non-AI semis")
ax.bar(range(len(labs)), swq, bottom=[a + n for a, n in zip(aiq, nonaiq)], color=LIGHT_BLUE, width=0.6, zorder=3, label="Infrastructure software")
for i in range(len(labs)):
    t = (Q_REV + [G4["rev"]])[i]
    ax.annotate(f"{aiq[i] / t * 100:.0f}%", (i, aiq[i] / 2), ha="center", va="center", fontsize=5.8, color="white", fontweight="bold")
    ax.annotate(f"{t:.1f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.0, color=NAVY, fontweight="bold")
ax.set_ylim(0, 40); ax.set_ylabel("US$bn", fontsize=8)
ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, fontsize=6.2)
ax.legend(loc="upper left", fontsize=6.2, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=3)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_mix")

# ---- 5. Margins by quarter, with the Q4 guide ----
gm = Q_GM + [G4["gm"] * 100]; om = Q_OM + [G4["om"] * 100]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
cols = [NAVY] * len(Q_OM) + [LIGHT_BLUE]
bars = ax.bar(range(len(labs)), om, color=cols, width=0.6, zorder=3, label="Operating margin, non-GAAP")
for b, v in zip(bars, om):
    ax.annotate(f"{v:.1f}", (b.get_x() + b.get_width() / 2, v / 2), ha="center", va="center", fontsize=6.0, color="white", fontweight="bold")
ax.plot(range(len(labs)), gm, color=GRAY, marker="s", markersize=2.8, linewidth=1.2, zorder=4, label="Gross margin, non-GAAP")
for i, v in enumerate(gm):
    if i in (0, len(Q_GM) - 1, len(gm) - 1):
        ax.annotate(f"{v:.1f}", (i, v), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=GRAY, fontweight="bold")
ax.set_ylim(0, 95); ax.set_ylabel("Per cent", fontsize=8)
ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs, fontsize=6.2)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.18), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_margin")

# ---- 6. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 8, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n5 Oct 2026", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 2, 150), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(0, 560); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
