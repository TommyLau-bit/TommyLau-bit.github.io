"""Charts for the SpaceX initiation. House style: navy / light blue, red reference lines, grey price line."""
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


# ---- 1. Revenue by segment, 2024 to 2027E, US$bn ----
years = ["2024", "2025", "2026E*", "2027E*"]
data = {k: [REV_24[k] / 1000, REV_25[k] / 1000, FY26[k][0] / 1000, R27[k] / 1000] for k in SEGS}
cols = {"Space": GRAY, "Connectivity": LIGHT_BLUE, "SI": NAVY}
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bottom = [0] * 4
for k in ["Space", "Connectivity", "SI"]:
    ax.bar(years, data[k], bottom=bottom, color=cols[k], width=0.58, zorder=3, label=SEG_NAMES[k])
    bottom = [b + v for b, v in zip(bottom, data[k])]
for i, t in enumerate(bottom):
    ax.annotate(f"{t:.1f}", (i, t), xytext=(0, 2), textcoords="offset points", ha="center", va="bottom", fontsize=7,
                color=NAVY, fontweight="bold")
ax.scatter([3.4], [CONS_REV_27 / 1000], color=RED, marker="D", s=14, zorder=5, label="2027 consensus (Yahoo)")
ax.set_ylim(0, 215); ax.set_ylabel("Revenue (US$bn)", fontsize=8)
ax.legend(loc="upper left", fontsize=6.4, frameon=False, ncol=2)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_annual")

# ---- 2. Valuation cross-check ----
bear, base, bull = VALS
glo = grid_value(min(SENS_SI), min(SENS_MULT)); ghi = grid_value(max(SENS_SI), max(SENS_MULT))
rows = [
    ("Scenarios\nbear to bull", "range", (bear, bull)),
    (f"Sensitivity grid\nSI at {SENS_MULT[0]:.0f} to {SENS_MULT[2]:.0f}x EBITDA", "range", (glo, ghi)),
    ("Probability-weighted\n25 / 50 / 25", "point", WEIGHTED),
    ("Base: sum of the parts\nplus US$100bn of options", "point", base),
    ("Three businesses only\n(no options)", "point", TERR_VALUE),
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
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.3, zorder=4)
ax.text(PRICE + 3, len(rows) - 0.42, f"Price US${PRICE:,.2f}", fontsize=7, color=RED, ha="left", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=6.6)
ax.set_xlabel("Value per share (US$)", fontsize=8)
ax.set_xlim(0, 300); ax.set_ylim(-0.6, len(rows) - 0.1)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_valuation")

# ---- 3. Launch services revenue per kg of customer payload ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
bars = ax.bar(KG_LABELS, KG_PRICE_USD, color=[LIGHT_BLUE] * 3 + [NAVY] * 3, width=0.58, zorder=3)
for b, v in zip(bars, KG_PRICE_USD):
    ax.annotate(f"{v:,.0f}", (b.get_x() + b.get_width() / 2, v), xytext=(0, 2), textcoords="offset points", ha="center",
                va="bottom", fontsize=7, color=NAVY, fontweight="bold")
ax.axhline(THRESHOLD_KG, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(5.4, THRESHOLD_KG + 250, "Claim's test: US$200/kg", fontsize=6.6, color=RED, ha="right", va="bottom", zorder=6,
        bbox=dict(facecolor="white", edgecolor="none", pad=1))
ax.axhline(GOOGLE_KG, color=GRAY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(-0.4, GOOGLE_KG + 250, "Google's Falcon 9 estimate: US$3,600/kg", fontsize=6.4, color=GRAY, ha="left", va="bottom", zorder=6,
        bbox=dict(facecolor="white", edgecolor="none", pad=1))
ax.set_ylim(0, 11500); ax.set_ylabel("US$ per kg", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_perkg")

# ---- 4. What the price pays for, US$ per share ----
parts = [("Starlink\n(Connectivity)", SOTP["Connectivity"]), ("SI: compute,\nGrok, X, Cursor", SOTP["SI"]),
         ("Space (launch)", SOTP["Space"]), ("Net cash", NETCASH), ("Options I credit\n(incl. orbital)", OPTIONS),
         ("Left for the\nmarket's extra", MCAP - BASE_EQ)]
ps = [(n, v / SHARES) for n, v in parts]
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
left = 0
for i, (n, v) in enumerate(ps):
    col = RED if i == len(ps) - 1 else (PALE if i == 4 else (NAVY if i in (0, 1) else LIGHT_BLUE))
    ax.barh(len(ps) - 1 - i, v, left=left, height=0.6, color=col, zorder=3,
            hatch="///" if i == len(ps) - 1 else None, edgecolor="white" if i == len(ps) - 1 else None)
    ax.annotate(f"US${v:,.1f}", (left + v, len(ps) - 1 - i), xytext=(4, 0), textcoords="offset points", ha="left",
                va="center", fontsize=6.6, color=NAVY, fontweight="bold", zorder=6,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.5))
    left += v
ax.axvline(PRICE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(PRICE + 2, -0.8, f"Price US${PRICE:,.2f}", fontsize=6.6, color=RED, ha="left", va="center")
ax.axvline(BASE_VALUE, color=NAVY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(BASE_VALUE - 2, -0.8, f"Base US${BASE_VALUE:,.0f}", fontsize=6.6, color=NAVY, ha="right", va="center")
ax.set_yticks(range(len(ps))); ax.set_yticklabels([n for n, _ in ps][::-1], fontsize=6.3)
ax.set_xlim(0, 165); ax.set_ylim(-1.2, len(ps) - 0.1); ax.set_xlabel("Cumulative value per share (US$)", fontsize=8)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_sotp")

# ---- 5. Share price, weekly close since the IPO ----
fig, ax = plt.subplots(figsize=SIZE, dpi=220)
ax.plot(range(len(PX)), PX, color=GRAY, linewidth=1.8, zorder=3)
ax.axhline(BASE_VALUE, color=RED, linestyle="--", linewidth=1.2, zorder=4)
ax.text(len(PX) - 1, BASE_VALUE - 5, f"My base value US${BASE_VALUE:,.0f}", fontsize=6.8, color=RED, ha="right", va="top")
ax.axhline(IPO_PRICE, color=NAVY, linestyle=":", linewidth=1.0, zorder=4)
ax.text(0, IPO_PRICE + 3, "IPO price US$135", fontsize=6.6, color=NAVY, ha="left", va="bottom")
ax.annotate(f"US${PX[-1]:,.2f}\n{PRICE_DATE}", (len(PX) - 1, PX[-1]), xytext=(len(PX) - 5, 195), textcoords="data",
            ha="center", va="center", fontsize=6.8, color=NAVY, fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.7))
ticks = list(range(0, len(PX), 4))
ax.set_xticks(ticks); ax.set_xticklabels([PX_LABELS[i] for i in ticks], fontsize=7)
ax.set_ylim(60, 220); ax.set_ylabel("Weekly close (US$)", fontsize=8)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0); style(ax)
save("chart_price")
print("charts written")
