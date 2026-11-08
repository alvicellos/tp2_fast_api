from fastapi import FastAPI
from fastapi import APIRouter
from models import retornar

router = APIRouter()
app = FastAPI()

@router.post("/generate/text/")
async def serve_language_model_controller(prompt: dict):
    output = retornar(prompt['message'])
    return {"resposta": output}