from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    src_lang: str
    tgt_lang: str
