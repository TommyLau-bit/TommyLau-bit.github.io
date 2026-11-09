"""Charts for the Caterpillar initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Power Generation sales, 2024A to 2028E, and share of Power & Energy external sales ----
years = ["2024A", "2025A", "2026E*", "2027E*", "2028E*"]
pg = [APP["PG"]["2024A"] / 1000, APP["PG"]["2025A"] / 1000, Y26["app"]["PG"] / 1000, Y27["app"]["PG"] / 1000, Y28["app"]["PG"] / 1000]
ext = [sum(APP[k]["2024A"] for k in APP), sum(APP[k]["2025A"] for k in APP), Y26["ext"], Y27["ext"], Y28["ext"]]
share = [p * 1000 / e * 100 for p, e in zip(pg, ext)]
x = list(range(len(years)))
fig, ax1 = plt.subplots(figsize=SIZE, dpi=220)
ax1.bar(x, pg, color=[NAVY, NAVY, LIGHT_BLUE, LIGHT_BLUE, LIGHT_BLUE], width=0.6, zorder=3, label="Power Generation sales, US$bn")
for i, s in enumerate(pg):
    ax1.annotate(f"{s:.1f}", (i, s), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=6.6,
                 color=NAVY, fontweight="bold")
ax1.axhline(APP["PG"]["2024A"] * 2 / 1000, color=GRAY, linestyle=":", linewidth=1.0, zorder=4)
ax1.text(-0.45, APP["PG"]["2024A"] * 2 / 1000 + 0.3, "2030 target: more than 2x 2024", fontsize=6.0, color=GRAY, ha="left", va="bottom")
ax1.set_ylim(0, 29); ax1.set_ylabel("US$bn", fontsize=8)
ax1.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax1)
ax1.set_xticks(x); ax1.set_xticklabels(years, fontsize=7)
ax2 = ax1.twinx()
ax2.plot(x, share, color=RED, marker="o", markersize=3.5, linewidth=1.6, zorder=4, label="Share of P&E external sales, % (RHS)")
for i, m in enumerate(share):
    ax2.annotate(f"{m:.0f}%", (i, m), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom", fontsize=6.2,
                 color=RED, fontweight="bold")
ax2.set_ylim(-170, 75); ax2.set_yticks([]); ax2.tick_params(axis="y", labelsize=7.4, length=0)
for s in ["top", "left", "right"]:
    ax2.spines[s].set_visible(False)
h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.4, frameon=False, bbox_to_anchor=(-0.02, 1.16), ncol=2)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = (x_["value"] for x_ in SC)
glo = PG_EPS * SENS_PG[0] + REST_EPS * SENS_REST[0]; ghi = PG_EPS * SENS_PG[2] + REST_EPS * SENS_REST[2]
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    ("Sensitivity grid\nmultiples of 2028E", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    (f"Base: {PG_PE:.0f}x power, {REST_PE:.0f}x\nthe rest, 2028E", "point", base),
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
ax.text(PRICE - 8, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=GRAY, ha="right", va="bottom")
if CALL["target"]:
    ax.axvline(CALL["target"], color=RED, linestyle="--", linewidth=1.3, zorder=4)
    ax.text(CALL["target"] + 8, len(rows) - 0.42, f"Target US${CALL['target']:,.0f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.8)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(240, 1000); ax.set_ylim(-0.6, len(rows) + 0.2)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. The queue: firm backlog, with the part not expected within twelve months ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
late = [v if v is not None else BL_LATE_SEP26 for v in BL_LATE]
near = [b - l for b, l in zip(BL, late)]
xs = range(len(BL))
ax.bar(xs, near, color=NAVY, width=0.58, zorder=3, label="Due within twelve months")
ax.bar(xs, late, bottom=near, color=[LIGHT_BLUE] * 7 + [PALE], width=0.58, zorder=3, label="Due later")
for i, (b, l) in enumerate(zip(BL, late)):
    ax.annotate(f"{b:.1f}", (i, b), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=7,
                color=NAVY, fontweight="bold")
ax.set_xticks(list(xs)); ax.set_xticklabels(BL_LABELS, fontsize=7)
ax.set_ylim(0, 92); ax.set_ylabel("US$bn", fontsize=8)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_queue")

# ---- 4. What the price pays for: value per share split at three prices ----
labels = ["30 Jun 2026\nrecord close", f"{PRICE_DATE}\nclose", "My base value"]
rest = [REST_VAL, REST_VAL, REST_VAL]
pgv = [HI_CLOSE - REST_VAL, PRICE - REST_VAL, PG_VAL]
mults = [IMPLIED_PG_PE_PEAK, IMPLIED_PG_PE, PG_PE]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.bar(range(3), rest, color=NAVY, width=0.55, zorder=3, label=f"The rest at {REST_PE:.0f}x my 2028E")
ax.bar(range(3), pgv, bottom=rest, color=[RED, LIGHT_BLUE, LIGHT_BLUE], width=0.55, zorder=3, label="Left for Power Generation")
for i in range(3):
    tot = rest[i] + pgv[i]
    ax.annotate(f"US${tot:,.0f}", (i, tot), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=7,
                color=NAVY, fontweight="bold")
    ax.annotate(f"{mults[i]:.0f}x", (i, rest[i] + pgv[i] / 2), ha="center", va="center", fontsize=7, color="white", fontweight="bold")
    ax.annotate(f"US${rest[i]:,.0f}", (i, rest[i] / 2), ha="center", va="center", fontsize=6.6, color="white", fontweight="bold")
ax.set_xticks(range(3)); ax.set_xticklabels(labels, fontsize=6.8)
ax.set_ylim(0, 1250); ax.set_ylabel("US$ per share", fontsize=8)
ax.legend(loc="upper right", fontsize=6.4, frameon=False)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_split")

# ---- 5. Share price ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(0, BASE_VALUE + 12, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 4, 380), textcoords="data", ha="right",
            va="center", fontsize=7, color=NAVY, fontweight="bold", arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 6))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(200, 1150); ax.set_ylabel("Close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
