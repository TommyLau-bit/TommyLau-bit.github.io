import sys
from weasyprint import HTML

def render_pdf(html_path, out_path):
    HTML(filename=html_path).write_pdf(out_path)
    print(f"Rendered {out_path}")

if __name__ == "__main__":
    render_pdf(sys.argv[1], sys.argv[2])
