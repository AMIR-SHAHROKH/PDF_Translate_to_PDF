from fastapi import FastAPI, UploadFile, File
from app.pdf_utils import extract_text_from_pdf
from app.translate import translate_text
from app.models import TranslationRequest
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Farsi to English PDF Translator API is running"}

@app.post("/translate-text/")
async def translate_text_api(request: TranslationRequest):
    translated_text = translate_text(request.text, request.src_lang, request.tgt_lang)
    return {"translated_text": translated_text}

@app.post("/translate-pdf/")
async def translate_pdf(file: UploadFile = File(...), src_lang: str = "fa", tgt_lang: str = "en"):
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)
    translated_text = translate_text(extracted_text, src_lang, tgt_lang)

    return {"translated_text": translated_text}
