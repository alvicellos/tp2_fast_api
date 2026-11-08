import requests
import sys

def traduzir(texto):
    resposta = requests.post(
        "http://127.0.0.1:8000/translate",
        params={"text_eng": texto}
    )
    return resposta.json()["translated_text"]

if __name__ == "__main__" and sys.argv[1] != None :
    texto = sys.argv[1]
    print(traduzir(texto))
    
    