"""
main.py
Pipeline principal do projeto (workflow + CLI).

Fluxo:
1) Ler JSON de entrada
2) Validar contrato de dados (schema)
3) Calcular indicadores financeiros (O*NET Task 3)
4) Interpretar risco com IA Generativa (O*NET Task 1)
5) Gerar relatório estruturado (O*NET Task 4)
"""

import argparse
from datetime import datetime
from anyio import Path

from .schemas import InputPayload          # contrato de dados
from .ratios import compute_ratios         # Task 3
from .llm import call_llm                  # Task 1
from .report import make_markdown_report   # Task 4
from .utils import read_json, write_json, write_text


def run(input_path: str, out_dir: str) -> None:
    # 1) Ler input
    raw = read_json(input_path)

    # 2) Validar schema (falha cedo se algo estiver errado)
    payload = InputPayload.model_validate(raw)

    # 3) O*NET Task 3: gerar indicadores financeiros
    ratios = compute_ratios(payload.financials)

    # Contexto usado pela IA e salvo para auditoria/debug
    context = {
        "company": payload.company.model_dump(),
        "financials": payload.financials.model_dump(),
        "receivable": payload.receivable.model_dump(),
        "behavioral": payload.behavioral.model_dump(),
        "ratios": ratios,
    }

    # 4) O*NET Task 1: interpretação preliminar via IA Generativa
    llm_text = call_llm(context)

    # 5) O*NET Task 4: gerar relatório Markdown
    report_md = make_markdown_report(raw, ratios, llm_text)

    # 6) Persistir outputs (input + timestamp)
    input_name = Path(input_path).stem
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    write_json(f"{out_dir}/{input_name}__{ts}_context.json", context)
    write_text(f"{out_dir}/{input_name}__{ts}_report.md", report_md)

    print(f"✅ Gerado: {out_dir}/{input_name}__{ts}_report.md")
    print(f"✅ Contexto: {out_dir}/{input_name}__{ts}_context.json")


def main():
    parser = argparse.ArgumentParser(
        description="Automação de tarefas de analista de crédito usando GenAI"
    )
    parser.add_argument(
        "--input",
        default="data/sample_input.json",
        help="Caminho para o JSON de entrada"
    )
    parser.add_argument(
        "--out",
        default="outputs",
        help="Diretório de saída"
    )

    args = parser.parse_args()
    run(args.input, args.out)


if __name__ == "__main__":
    main()