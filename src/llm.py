"""
llm.py
Camada de IA Generativa (provider-agnostic, aqui usando Groq).

📌 O*NET Task 1:
"Analyze credit data and financial statements to determine the degree of risk involved in extending 
credit or lending money."

Aqui a IA:
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
    return f"""
Você é um analista de crédito sênior auxiliando uma equipe humana.
Seu objetivo é produzir uma ANÁLISE PRELIMINAR de risco, clara e estruturada.

⚠️ IMPORTANTE:
- Não invente dados.
- Use APENAS as informações fornecidas.
- Se algo estiver faltando, indique explicitamente.
- Seja direto, profissional e organizado.
- NÃO faça decisão final, apenas triagem.

Responda OBRIGATORIAMENTE no formato abaixo:

RISCO: <BAIXO | MÉDIO | ALTO>

RESUMO EXECUTIVO:
<2–3 frases objetivas resumindo o perfil de risco>

FUNDAMENTOS DO RISCO:
- <ligar indicadores financeiros a risco>
- <ligar liquidez ao prazo do recebível>
- <ligar endividamento à sustentabilidade>

PONTOS DE ATENÇÃO:
- <itens que NÃO impedem a operação, mas exigem cuidado>

PERGUNTAS PARA VALIDAÇÃO HUMANA:
- <questões que um analista deveria verificar antes da decisão>

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
        temperature=0.2, # respostas mais focadas e consistentes
        max_tokens=600, # controle de custo
    )

    return resp.choices[0].message.content.strip()