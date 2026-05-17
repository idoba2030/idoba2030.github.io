#!/usr/bin/env python3
"""
Generate a PDF version of the CV from _pages/cv.md using headless Edge/Chrome.
No extra Python packages required — uses the browser already on the machine.
Output: files/cv.pdf
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).parent.parent
CV_MD = REPO / "_pages" / "cv.md"
OUTPUT = REPO / "files" / "cv.pdf"

BROWSER_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

HTML_TEMPLATE = """<!doctype html>
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
      margin: 0; padding: 0;
    }}
    {styles}
    .cv-embed {{ max-width: 100%; padding: 0; margin: 0; font-size: 11pt; }}
    a.pub-link {{ color: inherit; text-decoration: none; border-bottom: 1px solid #888; }}
    a {{ color: inherit; }}
  </style>
</head>
<body>
{body}
</body>
</html>"""


def find_browser():
    for path in BROWSER_CANDIDATES:
        if Path(path).exists():
            return path
    # fallback: check PATH
    for name in ("msedge", "google-chrome", "chromium"):
        found = shutil.which(name)
        if found:
            return found
    return None


def extract_styles(md_text):
    m = re.search(r"<style>(.*?)</style>", md_text, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_body(md_text):
    m = re.search(r'(<div class="cv-embed">.*)', md_text, re.DOTALL)
    return m.group(1).strip() if m else ""


def main():
    browser = find_browser()
    if not browser:
        print("No Edge or Chrome browser found. Install one and try again.")
        sys.exit(1)

    md_text = CV_MD.read_text(encoding="utf-8")
    styles = extract_styles(md_text)
    body = extract_body(md_text)
    html = HTML_TEMPLATE.format(styles=styles, body=body)

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False,
                                     mode="w", encoding="utf-8") as f:
        f.write(html)
        tmp_html = f.name

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run([
            browser,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={OUTPUT}",
            "--print-to-pdf-no-header",
            f"file:///{tmp_html.replace(chr(92), '/')}",
        ], check=True, capture_output=True)
        print(f"PDF written to {OUTPUT}")
    finally:
        Path(tmp_html).unlink(missing_ok=True)


if __name__ == "__main__":
    main()
