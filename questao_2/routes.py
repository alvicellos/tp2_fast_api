from fastapi import FastAPI
from fastapi import APIRouter
from models import load_model, translate_text, TranslationResponse

router = APIRouter()
app = FastAPI()

@router.post("/translate", response_model=TranslationResponse)
async def traduzir(text_eng: str):
    pipe = load_model()
    traducao = translate_text(pipe, text_eng)
    return {"texto_traduzido": traducao}