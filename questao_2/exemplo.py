import requests    
    
texto_ingles = '''One day, Jack woke up feeling under the weather, but he decided to bite the bullet and go to work anyway. On his way, he ran into an old friend who told him about a mysterious treasure hidden in the mountains. At first, Jack thought his friend was pulling his leg, but curiosity got the better of him. They decided to give it a shot, knowing that finding the treasure would be like looking for a needle in a haystack. To their surprise, they struck gold and realized that sometimes taking a chance can be a blessing in disguise'''

def exemplo():
    resposta = requests.post(
    "http://127.0.0.1:8000/translate",
    params={"text_eng": texto_ingles}
    )

    print(f"Texto original em inglês:\n{texto_ingles}")
    print(f"Texto traduzino pela aplicação:\n{resposta.json()['translated_text']}")
    
if __name__ == "__main__":
    exemplo()