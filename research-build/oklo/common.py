"""Shared design system matching the Marco Polo Marine initiation note style."""

NAVY = "#1F3864"
NAVY_LIGHT = "#2E5395"
BORDER_GRAY = "#BFBFBF"
TEXT = "#1A1A1A"
MUTED = "#595959"

BASE_CSS = f"""
* {{ box-sizing: border-box; }}
body {{
    font-family: 'Liberation Sans', Arial, Helvetica, sans-serif;
    font-size: 9.3pt;
    line-height: 1.32;
    color: {TEXT};
    margin: 0;
    padding: 0;
}}
h1.doctitle {{
    font-size: 19pt;
    font-weight: 700;
    color: {NAVY};
    text-transform: uppercase;
    margin: 0 0 3px 0;
    letter-spacing: 0.2px;
}}
p.docsubtitle {{
    font-size: 9.3pt;
    color: {TEXT};
    margin: 0 0 10px 0;
}}
p.docmeta {{
    font-size: 9.3pt;
    color: {TEXT};
    margin: 0 0 10px 0;
}}
table.ratingbanner {{
    width: 100%;
    border-collapse: collapse;
    border: 0.75pt solid {NAVY};
    margin-bottom: 12px;
    table-layout: fixed;
}}
table.ratingbanner td {{
    border: 0.75pt solid {NAVY};
    padding: 6px 10px;
    font-size: 9.6pt;
    vertical-align: middle;
}}
table.ratingbanner td.rating {{
    background: {NAVY};
    color: #FFFFFF;
    font-weight: 700;
    text-align: center;
    width: 22%;
    font-size: 10pt;
}}
table.ratingbanner td.field b {{
    font-weight: 700;
}}
h2.section {{
    font-size: 11.3pt;
    font-weight: 700;
    color: {NAVY};
    margin: 9px 0 4px 0;
    break-after: avoid;
}}
h2.section.first {{ margin-top: 2px; }}
p.body {{
    text-align: left;
    margin: 0 0 6px 0;
}}
.clearfix::after {{ content: ""; display: table; clear: both; }}
.sidebar {{
    float: right;
    width: 40%;
    margin-left: 14px;
}}
.maincol {{
    float: left;
    width: 53%;
}}
.fullwidth {{
    width: 100%;
    clear: both;
}}
table.statbox {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 10px;
}}
table.statbox th {{
    background: {NAVY};
    color: #FFFFFF;
    font-size: 9pt;
    font-weight: 700;
    text-align: left;
    padding: 4px 7px;
}}
table.statbox td {{
    font-size: 8.6pt;
    line-height: 1.22;
}}
table.statbox td.lbl {{
    font-size: 7.4pt;
    color: {MUTED};
    text-transform: uppercase;
    letter-spacing: 0.2px;
    padding: 3px 7px 0 7px;
}}
table.statbox td.val {{
    text-align: left;
    font-weight: 600;
    padding: 0 7px 4px 7px;
    border-bottom: 0.5pt solid {BORDER_GRAY};
}}
p.caption {{
    font-size: 7.6pt;
    color: {MUTED};
    font-style: italic;
    margin: 2px 0 6px 0;
}}
table.datatable {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 4px;
}}
table.datatable th {{
    background: {NAVY};
    color: #FFFFFF;
    font-size: 8.8pt;
    font-weight: 700;
    text-align: left;
    padding: 5px 8px;
}}
table.datatable th.num {{ text-align: right; }}
table.datatable td {{
    font-size: 8.8pt;
    padding: 3.5px 8px;
    border-bottom: 0.5pt solid {BORDER_GRAY};
    vertical-align: top;
}}
table.datatable tr {{ break-inside: avoid; }}
table.keyfacts tr {{ break-inside: avoid; }}
table.datatable td.num {{ text-align: right; }}
table.datatable tr.total td {{
    font-weight: 700;
    border-top: 0.75pt solid {NAVY};
}}
table.datatable td.rowlabel {{ font-weight: 600; }}
table.wide-first th:first-child, table.wide-first td:first-child {{
    width: 34%;
}}
.keeptogether {{ break-inside: avoid; }}
.chartsrow {{ width: 100%; }}
.chartsrow::after {{ content: ""; display: table; clear: both; }}
.chartsrow .col {{
    width: 49%;
    float: left;
}}
.chartsrow .col.left {{ margin-right: 2%; }}
img.chart {{
    width: 100%;
    display: block;
}}
strong.lead {{ font-weight: 700; }}
table.keyfacts {{
    width: 100%;
    border-collapse: collapse;
    border: 0.75pt solid {NAVY};
    margin: 4px 0 14px 0;
}}
table.keyfacts td {{
    border: 0.5pt solid {BORDER_GRAY};
    padding: 5px 9px;
    font-size: 8.9pt;
    vertical-align: top;
}}
table.keyfacts td.label {{
    background: {NAVY};
    color: #FFFFFF;
    font-weight: 700;
    width: 18%;
    white-space: nowrap;
}}
p.sourceline {{
    font-size: 8.3pt;
    margin: 0 0 5px 0;
    color: {TEXT};
}}
p.aboutnote {{
    font-size: 8.6pt;
    color: {MUTED};
    text-align: left;
    margin: 0 0 6px 0;
}}
p.signoff {{
    font-size: 8.6pt;
    margin: 4px 0 0 0;
}}
"""


def page_css(title, date):
    """Per-document @page rule with the running footer baked in (WeasyPrint margin boxes)."""
    return f"""
@page {{
    size: Letter;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-left {{
        content: "Tommy Lau | {title} | {date}\\A Personal research, not investment advice.";
        white-space: pre-line;
        font-family: 'Liberation Sans', Arial, sans-serif;
        font-size: 7.6pt;
        line-height: 1.5;
        color: {TEXT};
        border-top: 0.75pt solid {NAVY};
        padding-top: 2.5mm;
        width: 100%;
    }}
    @bottom-right {{
        content: "Page " counter(page);
        font-family: 'Liberation Sans', Arial, sans-serif;
        font-size: 7.6pt;
        color: {TEXT};
        border-top: 0.75pt solid {NAVY};
        padding-top: 2.5mm;
        white-space: nowrap;
    }}
}}
"""


def page_shell(body_html, title, date):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>{page_css(title, date)}{BASE_CSS}</style>
</head>
<body>
{body_html}
</body></html>"""


def datatable(headers, rows, num_cols=None, total_row_idx=None, wide_first=False):
    """headers: list[str]; rows: list[list[str]]; num_cols: set of column indices that are right-aligned numeric."""
    num_cols = num_cols or set()
    cls = "datatable wide-first" if wide_first else "datatable"
    out = [f'<table class="{cls}">', "<tr>"]
    for i, h in enumerate(headers):
        c = ' class="num"' if i in num_cols else ""
        out.append(f"<th{c}>{h}</th>")
    out.append("</tr>")
    for ridx, row in enumerate(rows):
        trcls = ' class="total"' if total_row_idx is not None and ridx == total_row_idx else ""
        out.append(f"<tr{trcls}>")
        for i, cell in enumerate(row):
            if i == 0:
                c = ' class="rowlabel num"' if i in num_cols else ' class="rowlabel"'
            else:
                c = ' class="num"' if i in num_cols else ""
            out.append(f"<td{c}>{cell}</td>")
        out.append("</tr>")
    out.append("</table>")
    return "\n".join(out)


def keyfacts_table(rows):
    out = ['<table class="keyfacts">']
    for label, value in rows:
        out.append(f'<tr><td class="label">{label}</td><td>{value}</td></tr>')
    out.append('</table>')
    return "\n".join(out)


def rating_banner(rating, tp, last, upside):
    return f"""<table class="ratingbanner">
<tr>
<td class="rating">{rating}</td>
<td class="field"><b>Target price:</b> {tp}</td>
<td class="field"><b>Last price:</b> {last}</td>
<td class="field"><b>Upside:</b> {upside}</td>
</tr>
</table>"""


def statbox(rows, title="Stock data"):
    out = [f'<table class="statbox"><tr><th>{title}</th></tr>']
    for label, val in rows:
        out.append(f'<tr><td class="lbl">{label}</td></tr>')
        out.append(f'<tr><td class="val">{val}</td></tr>')
    out.append("</table>")
    return "\n".join(out)


def section(title, first=False):
    cls = "section first" if first else "section"
    return f'<h2 class="{cls}">{title}</h2>'


def para(text):
    return f'<p class="body">{text}</p>'


def caption(text):
    return f'<p class="caption">{text}</p>'
