# Execução dos aplicativos — TP2 FastAPI

O repositório contém dois aplicativos independentes: geração de texto com GPT-2 (`questao_1`) e tradução do inglês para o francês com Helsinki-NLP (`questao_2`). Cada pasta contém `main.py`, `models.py`, `routes.py` e `requisicao.py`.

## Clonando o repositório

Para baixar o projeto localmente, abra o terminal na pasta onde deseja armazená-lo e execute:

```powershell
git clone https://github.com/alvicellos/tp2_fast_api.git
cd tp2_fast_api
```

Após acessar a pasta do projeto, siga as instruções de instalação abaixo.

## 1. Instalação

Na raiz do repositório, crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando do Windows, a ativação é feita com `.venv\Scripts\activate.bat`; no Linux/macOS, com `source .venv/bin/activate`.

Instale as dependências a partir do arquivo `requirements.txt` na raiz:

```powershell
python -m pip install -r requirements.txt
```

Na primeira execução, os modelos e tokenizers poderão ser baixados do Hugging Face; é necessária conexão com a internet para esse download.

## 2. Questão 1 — Geração de texto (GPT-2)

No terminal com o ambiente ativado, acesse a pasta e inicie a API:

```powershell
cd questao_1
python -m uvicorn main:app --reload
```

Acesse a documentação interativa (Swagger UI) em: http://127.0.0.1:8000/docs

---
### Alternativa para testar a execução sem abrir o Swagger:

Mantenha o servidor aberto. Em **outro terminal**, a partir da pasta `questao_1`, execute o teste (usando o Python do ambiente virtual):

```powershell
python requisicao.py "Once upon a time"
```

O script envia uma requisição POST para `http://127.0.0.1:8000/generate/text` com o texto no campo JSON `message` e exibe a resposta no terminal.

## 3. Questão 2 — Tradução (Helsinki-NLP)

Encerre o servidor anterior com `Ctrl+C`. A partir da raiz do repositório, acesse a pasta da segunda questão e inicie a API:

```powershell
cd questao_2
python -m uvicorn main:app --reload
```

Acesse a documentação interativa (Swagger UI): http://127.0.0.1:8000/docs

---
### Alternativa para testar a execução sem abrir o Swagger:

Em **outro terminal**, a partir da pasta `questao_2`, execute:

```powershell
python requisicao.py "Good morning, how are you?"
```

O script envia uma requisição POST para `http://127.0.0.1:8000/translate`, passando o texto em inglês pelo parâmetro `text_eng`, e exibe a tradução no terminal.

### Observação relacionada à questão 3:

O arquivo `questao_2/exemplo.py` demonstra traduções literais de expressões idiomáticas pelo modelo. Basta executá-lo com:

```powershell
python exemplo.py
```

## 4. Observações

- Execute cada servidor a partir da pasta de sua respectiva questão, para que os imports locais sejam encontrados.
- Os dois scripts `requisicao.py` usam a porta **8000**; execute apenas um dos servidores por vez nessa porta.
- Se aparecer erro de conexão, verifique se o servidor está em execução antes de chamar `requisicao.py`.
- No Windows, caso não consiga ativar o ambiente, utilize o executável `..\.venv\Scripts\python.exe` dentro de cada pasta `questao_1` ou `questao_2` no lugar de `python`