# make_thumbnails.py
from pathlib import Path
import fitz  # pymupdf

CERT_DIR = Path("static/certs")
CERT_DIR.mkdir(parents=True, exist_ok=True)

# choose zoom: 2.0 -> 144 DPI-ish, 3.0 -> ~216 DPI (bigger images)
ZOOM = 2.5

for pdf_path in sorted(CERT_DIR.glob("*.pdf")):
    png_path = pdf_path.with_suffix(".png")
    if png_path.exists():
        print(f"Skipping (exists): {png_path.name}")
        continue

    print(f"Rendering: {pdf_path.name} -> {png_path.name}")
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)  # first page
    mat = fitz.Matrix(ZOOM, ZOOM)
    pix = page.get_pixmap(matrix=mat, alpha=False)  # alpha=False -> no transparency
    pix.save(str(png_path))
    doc.close()
    print(f"Saved thumbnail: {png_path}")
