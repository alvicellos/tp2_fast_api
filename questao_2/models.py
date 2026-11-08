import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from pydantic import BaseModel

class TranslationResponse(BaseModel):
    texto_traduzido: str    

def load_model():
    
    modelo = "Helsinki-NLP/opus-mt-en-fr"
    
    tokenizer = AutoTokenizer.from_pretrained(
        modelo,
        clean_up_tokenization_spaces=True
    )
    
    device = 0 if torch.cuda.is_available() else -1

    pipe = pipeline(
        "translation",
        model=modelo,
        tokenizer=tokenizer,
        device=device,
    )
    return pipe


def translate_text(pipe, param_user_prompt, max_new_tokens=100):
    
    predictions = pipe(
        param_user_prompt,
        max_new_tokens=max_new_tokens
    )
    return predictions[0]["translation_text"]