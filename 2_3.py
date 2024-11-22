from fastapi import FastAPI
from pydantic import BaseModel
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import torch

# Inicialização do FastAPI
app = FastAPI()

# Modelo de entrada
class TextInput(BaseModel):
    text: str

# Verifica se uma GPU está disponível
device = 0 if torch.cuda.is_available() else -1

# Configuração do LangChain com HuggingFace
hf_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de", device=device)
llm = HuggingFacePipeline(pipeline=hf_pipeline)

prompt_template = PromptTemplate(
    input_variables=["text"],
    template="Translate the following text to German: {text}"
)
translation_chain = LLMChain(llm=llm, prompt=prompt_template)

@app.post("/translate_huggingface/")
async def translate_text(input: TextInput):
    translation = translation_chain.run(input.text)
    return {"input": input.text, "translation": translation}