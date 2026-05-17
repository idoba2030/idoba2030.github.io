#!/usr/bin/env python3
"""
Generate a PDF version of the CV from _pages/cv.md.
Requires: weasyprint  (pip install weasyprint)
Output:   files/cv.pdf
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent
CV_MD = REPO / "_pages" / "cv.md"
OUTPUT = REPO / "files" / "cv.pdf"

HTML_WRAPPER = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>CV – Ido Ben-Artzi</title>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
  <style>
    @page {{ size: A4; margin: 18mm 20mm 18mm 20mm; }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: 'Crimson Pro', 'Palatino Linotype', Palatino, 'Book Antiqua', Georgia, serif;
      font-size: 11pt;
      line-height: 1.45;
      color: #1a1a1a;
      background: #fff;
      margin: 0;
      padding: 0;
    }}
    {styles}
    /* PDF-specific overrides */
    .cv-embed {{ max-width: 100%; padding: 0; margin: 0; font-size: 11pt; }}
    a.pub-link {{ color: inherit; text-decoration: none; border-bottom: 1px solid #888; }}
    a {{ color: inherit; }}
  </style>
</head>
<body>
{body}
</body>
</html>"""


def extract_styles(md_text):
    m = re.search(r"<style>(.*?)</style>", md_text, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_body(md_text):
    m = re.search(r'(<div class="cv-embed">.*?</div>\s*)$', md_text, re.DOTALL)
    if m:
        return m.group(1).strip()
    # fallback: everything after the front matter style block
    m = re.search(r"</style>\s*\n(.*)", md_text, re.DOTALL)
    return m.group(1).strip() if m else ""


def main():
    try:
        from weasyprint import HTML, CSS
    except ImportError:
        print("weasyprint is not installed. Run:  pip install weasyprint")
        sys.exit(1)

    md_text = CV_MD.read_text(encoding="utf-8")
    styles = extract_styles(md_text)
    body = extract_body(md_text)

    html = HTML_WRAPPER.format(styles=styles, body=body)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(REPO)).write_pdf(str(OUTPUT))
    print(f"PDF written to {OUTPUT}")


if __name__ == "__main__":
    main()
