"""
llm.py
Camada de IA Generativa (provider-agnostic, aqui usando Groq).

📌 O*NET Task 1:
"Analyze credit data and financial statements to determine the degree of risk involved in extending 
credit or lending money."

Aqui a IA NÃO decide sozinha.
Ela:
- interpreta os números (ratios + dados)
- produz um risco preliminar + justificativa
- gera perguntas/pontos de atenção para revisão humana
"""

from typing import Dict, Any
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")  # default seguro


def build_prompt(context: Dict[str, Any]) -> str:
    """
    Prompt com formato rígido para:
    - facilitar leitura humana
    - facilitar parsing depois (se quiser evoluir)
    - manter consistência entre casos
    """
    return f"""
Você é um assistente de análise de risco de crédito. Você apoia analistas humanos.

Responda OBRIGATORIAMENTE no formato abaixo (sem texto extra):

risk_level: baixo|medio|alto
resumo_executivo: <1 frase>
justificativa:
- ...
- ...
pontos_de_atencao:
- ...
- ...
perguntas_para_verificar:
- ...
- ...

Regras:
- Não invente dados que não estejam no input.
- Se faltar informação, diga explicitamente o que falta (em bullets).
- Faça referência ao prazo e valor do recebível (duplicata) quando relevante.
- Seja objetivo e consistente.

DADOS (JSON):
{context}
""".strip()


def call_llm(context: Dict[str, Any]) -> str:
    if not GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY não configurada no .env")

    client = Groq(api_key=GROQ_API_KEY)
    prompt = build_prompt(context)

    resp = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": "Responda em português do Brasil, tom profissional e direto."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=600,
    )

    return resp.choices[0].message.content.strip()