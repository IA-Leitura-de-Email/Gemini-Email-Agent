import google.generativeai as genai
import os

# Configure sua chave
genai.configure(api_key="AIzaSyDgZrpBbnrliKTeZ07u9scIgCL1QMWBKG0")

print("Listando modelos disponíveis:")
print("-" * 50)

# O loop percorre todos os modelos que o SDK reconhece
for m in genai.list_models():
    # Filtra apenas os que suportam geração de conteúdo
    if 'generateContent' in m.supported_generation_methods:
        print(f"Nome do Modelo: {m.name}")
        print(f"Versão: {m.version}")
        print(f"Descrição: {m.description}")
        print("-" * 50)