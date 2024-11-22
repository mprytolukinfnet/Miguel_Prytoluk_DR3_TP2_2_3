# TP2 Exercício 2_3: Tradução para Alemão com LangChain e HuggingFace
Este aplicativo usa o modelo `Helsinki-NLP/opus-mt-en-de` integrado com LangChain para traduzir textos do inglês para o alemão.

**Passos para Configuração**:

1. Certifique-se de que o ambiente Python está configurado.
2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```
3. Instalar Pytorch: https://pytorch.org/get-started/locally/

**Como Executar**: Inicie o servidor FastAPI com o comando:
```bash
uvicorn 2_3:app --reload
```

**Uso da API**: Traduza um texto:

```bash
curl -X POST "http://127.0.0.1:8000/translate_huggingface/" \
-H "Content-Type: application/json" \
-d '{"text": "Good morning!"}'
```