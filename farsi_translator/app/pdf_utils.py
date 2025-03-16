import fitz  # PyMuPDF
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text("text") + "\n"

    if not text.strip():  # If empty, use OCR
        images = convert_from_path(pdf_path)
        for img in images:
            text += pytesseract.image_to_string(img, lang="fas") + "\n"

    return text
