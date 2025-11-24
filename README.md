1. Instale e inicie o Ollama
# Baixe e instale conforme instruções em:
https://ollama.com/download


Depois:
```bash
ollama serve
```

Baixe um modelo (exemplo):
```bash
ollama pull llama3
```

2. Configure o ambiente Python

Crie o venv:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale dependências:
```bash
pip install -r requirements.txt
```
3. Configure o arquivo .env

Crie um .env na raiz com:
```bash
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL_NAME=llama3
```
4. Rode a API
```bash
uvicorn app.main:app --reload
```