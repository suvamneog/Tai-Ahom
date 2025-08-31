import os, json
from pdf2image import convert_from_path
import pdfplumber
from PyPDF2 import PdfReader


PDF_FILE = "2.Morey.pdf"  
OUTPUT_DIR_RAW = "data/raw"
OUTPUT_DIR_TEXT = "docs/references"
OUTPUT_METADATA = "docs/metadata.json"

os.makedirs(OUTPUT_DIR_RAW, exist_ok=True)
os.makedirs(OUTPUT_DIR_TEXT, exist_ok=True)
os.makedirs("docs", exist_ok=True)

# === 1. Extract Metadata ===
def extract_metadata(pdf_path):
    reader = PdfReader(pdf_path)
    meta = reader.metadata
    if meta:
        clean_meta = {k: str(v) for k, v in meta.items()}
    else:
        clean_meta = {}
    with open(OUTPUT_METADATA, "w", encoding="utf-8") as f:
        json.dump(clean_meta, f, indent=4, ensure_ascii=False)
    print(f"[+] Metadata saved → {OUTPUT_METADATA}")

# === 2. Extract Text ===
def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                out_path = os.path.join(OUTPUT_DIR_TEXT, f"page_{i+1}.txt")
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"[+] Text extracted → {out_path}")

# === 3. Extract Images (scanned pages) ===
def extract_images(pdf_path, dpi=300):
    pages = convert_from_path(pdf_path, dpi=dpi)
    for i, page in enumerate(pages):
        out_path = os.path.join(OUTPUT_DIR_RAW, f"page_{i+1}.png")
        page.save(out_path, "PNG")
        print(f"[+] Image saved → {out_path}")


if __name__ == "__main__":
    print(f"Processing: {PDF_FILE}")
    extract_metadata(PDF_FILE)
    extract_text(PDF_FILE)
    extract_images(PDF_FILE)
    print("\n✅ Extraction complete!")