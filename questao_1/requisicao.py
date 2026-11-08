import requests
import sys

def completar(inicio):
    continuacao = requests.post(
        "http://127.0.0.1:8000/generate/text",
        json={"message": inicio}
    )
    return continuacao

if __name__ == "__main__":
    inicio = sys.argv[1]
    print(completar(inicio).json())