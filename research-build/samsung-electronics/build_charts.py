"""Charts for the Samsung Electronics initiation. House style: navy / light blue, red reference lines, grey price line."""

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


def k(x):
    return f"{x / 1000:,.0f}k"


# ---- 1. Operating profit by quarter: chips against the rest ----
labs = QL + ["Q4 26E*"]
ds = Q_DS_OP + [Q4["ds"] * Q4["ds_opm"]]
rest = [t - d for t, d in zip(Q_OP, Q_DS_OP)] + [Q4["op"] - Q4["ds"] * Q4["ds_opm"]]
x = list(range(len(labs)))
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(x, ds, color=[NAVY] * len(QL) + [LIGHT_BLUE], width=0.62, zorder=3, label="Device Solutions (chips)")
ax.bar(x, rest, bottom=[max(d, 0) for d in ds], color=GRAY, width=0.62, zorder=3, label="Phones, TVs, display, Harman")
for i in range(len(x)):
    tot = ds[i] + rest[i]
    share = ds[i] / tot * 100
    ax.annotate(f"{tot:.0f}\n({share:.0f}% chips)" if i in (0, 3, 6) else f"{tot:.0f}", (i, tot), xytext=(0, 2), textcoords="offset points",
                ha="center", va="bottom", fontsize=5.8, color=NAVY, fontweight="bold")
ax.set_ylim(0, 165); ax.set_ylabel("KRW trillion", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=6.4)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_profit")

# ---- 2. The squeeze: MX/NW operating profit against memory sales ----
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
x = list(range(len(QL)))
ax1.bar(x, Q_MX_OP, color=[RED if v < 0 else NAVY for v in Q_MX_OP], width=0.6, zorder=3, label="MX and Networks operating profit")
for i, v in enumerate(Q_MX_OP):
    ax1.annotate(f"{v:.1f}", (i, v), xytext=(0, 2 if v >= 0 else -2), textcoords="offset points", ha="center",
                 va="bottom" if v >= 0 else "top", fontsize=6.2, color=NAVY, fontweight="bold")
ax1.axhline(0, color="#B0B0B0", linewidth=0.8)
ax1.set_ylim(-2, 6); ax1.set_ylabel("KRW trillion", fontsize=8)
ax1.set_xticks(x); ax1.set_xticklabels(QL, fontsize=6.8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax2 = ax1.twinx()
ax2.plot(x, Q_MEM, color=GRAY, marker="o", markersize=2.6, linewidth=1.3, zorder=4, label="Memory sales (RHS)")
ax2.set_ylim(0, 160); ax2.tick_params(axis="y", labelsize=7.0, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.3, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=2)
save("chart_squeeze")

# ---- 3. The chip cycle: DS sales and operating margin, 2017 to 2027E ----
yrs = [y[2:] for y in DS_YRS] + ["26E*", "27E*"]
ds27 = MEM27 + OTH27["nonmem"][0]
dsop27 = MEM27 * MEM_OPM27 + OTH27["nonmem"][1]
ds26 = sum(Q_DS_REV[4:]) + Q4["ds"]
rv = DS_REV + [ds26, ds27]
om = [o / r * 100 for o, r in zip(DS_OP, DS_REV)] + [DS_OP26 / ds26 * 100, dsop27 / ds27 * 100]
x = list(range(len(yrs)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, rv, color=[NAVY] * len(DS_YRS) + [LIGHT_BLUE] * 2, width=0.62, zorder=3, label="Device Solutions sales, KRW tn")
for i in (1, 8, 9, 10):
    ax1.annotate(f"{rv[i]:.0f}", (i, rv[i]), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.0, color=NAVY, fontweight="bold")
ax1.set_ylim(0, 1000); ax1.set_ylabel("KRW trillion", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(x); ax1.set_xticklabels(yrs, fontsize=6.6)
ax2 = ax1.twinx()
ax2.plot(x, om, color=RED, marker="o", markersize=2.8, linewidth=1.4, zorder=4, label="Operating margin, % (RHS)")
ax2.axhline(DS_CYC_M * 100, color=GRAY, linestyle=":", linewidth=1.0, label=f"2017-25 margin {DS_CYC_M * 100:.1f}%")
for i in (1, 6, 10):
    ax2.annotate(f"{om[i]:.0f}%", (i, om[i]), xytext=(-6, 4 if om[i] > 0 else -3), textcoords="offset points", ha="right",
                 va="bottom" if om[i] > 0 else "top", fontsize=6.0, color=RED, fontweight="bold")
ax2.set_ylim(-40, 100); ax2.set_yticks([-20, 0, 40, 80])
ax2.tick_params(axis="y", labelsize=7.0, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.0, frameon=False, bbox_to_anchor=(-0.02, 1.17), ncol=3)
save("chart_cycle")

# ---- 4. Sum of the parts per share (waterfall) ----
ps = lambda v: v / SH * 1e6 / 1000
parts = [("Net cash", ps(BASE["nc"])), ("Memory\nexcess", ps(BASE["exc"])), ("Memory\n12x normal", ps(BASE["term"])),
         ("Other\nbusinesses", ps(sum(OTH_VAL[1:]))), ("Foundry,\nLSI", ps(OTH_VAL[0])), ("Invest-\nments", ps(INV_VAL)),
         ("20%\ndiscount", -ps(BASE["gross"] * DISC))]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
cum = 0
for i, (lab, v) in enumerate(parts):
    bottom = cum if v >= 0 else cum + v
    ax.bar(i, abs(v), bottom=bottom, color=NAVY if v >= 0 else RED, width=0.6, zorder=3)
    ax.annotate(f"{v:+.0f}", (i, cum + max(v, 0)), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.2, color=NAVY, fontweight="bold")
    cum += v
ax.bar(len(parts), cum, color=LIGHT_BLUE, width=0.6, zorder=3)
ax.annotate(f"{cum:.0f}", (len(parts), cum), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6, color=NAVY, fontweight="bold")
ax.axhline(PRICE / 1000, color=RED, linestyle="--", linewidth=1.1, zorder=4)
ax.text(-0.4, PRICE / 1000 + 8, f"Price {PRICE / 1000:.0f}k", fontsize=6.6, color=RED, ha="left", va="bottom")
ax.set_xticks(range(len(parts) + 1)); ax.set_xticklabels([p[0] for p in parts] + ["Base\nvalue"], fontsize=5.8)
ax.set_ylim(0, 400); ax.set_ylabel("KRW thousand per share", fontsize=7.5)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_parts")

# ---- 5. Valuation cross-check ----
bear, base, bull = VALS
glo = min(min(r) for r in VGRID); ghi = max(max(r) for r in VGRID)
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nmargin {SENS_NM[0]*100:.0f}-{SENS_NM[2]*100:.0f}%, {SENS_X[0]}-{SENS_X[2]}x", "range", (glo, ghi)),
    ("Discount\n30% to none", "range", (DISC_ROW[3], DISC_ROW[0])),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    ("Base, 20%\ndiscount", "point", base),
    ("Base without\nthe net cash", "point", NOCASH),
]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
for y, (lab, kind, v) in enumerate(rows):
    if kind == "point":
        ax.barh(y, v / 1000, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.annotate(k(v), (v / 1000, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
    else:
        lo, hi = v
        ax.barh(y, (hi - lo) / 1000, left=lo / 1000, height=0.5, color=PALE, edgecolor=NAVY, linewidth=0.9, zorder=3)
        ax.annotate(k(lo), (lo / 1000, y), xytext=(-4, 0), textcoords="offset points", ha="right", va="center", fontsize=7, color=NAVY, fontweight="bold")
        ax.annotate(k(hi), (hi / 1000, y), xytext=(4, 0), textcoords="offset points", ha="left", va="center", fontsize=7, color=NAVY, fontweight="bold")
ax.axvline(PRICE / 1000, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE / 1000 + 6, len(rows) - 0.42, f"Price KRW {PRICE:,.0f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.4)
ax.set_xlabel("Value per share (KRW thousand)", fontsize=8)
ax.set_xlim(0, 520); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 6. Share prices, common and preferred ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), [p / 1000 for p in PX], color=GRAY, linewidth=1.8, zorder=3, label="Common (005930)")
ax.plot(range(len(PX_P)), [p / 1000 for p in PX_P], color=LIGHT_BLUE, linewidth=1.5, zorder=3, label="Preferred (005935)")
ax.axhline(BASE_VALUE / 1000, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE / 1000 + 6, f"My base value KRW {BASE_VALUE / 1000:,.0f}k a share", fontsize=6.6, color=RED, ha="left", va="bottom")
ax.text(len(PX) - 1, 25, f"2 Nov 2026: KRW {PX[-1] / 1000:,.0f}k and {PX_P[-1] / 1000:,.0f}k, a {PREF_GAP * 100:.1f}% gap", ha="right", va="bottom", fontsize=6.4, color=NAVY, fontweight="bold")
ticks = list(range(0, len(PX), 3))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=6.6)
ax.set_ylim(0, 400); ax.set_ylabel("Close (KRW thousand)", fontsize=8)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.15), ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
