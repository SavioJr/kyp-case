"""
report.py
Geração do relatório final (Markdown).

📌 O*NET Task 4:
"Prepare reports that include the degree of risk involved..."

"""

from typing import Dict, Any
from datetime import datetime

# Formatação percentual
def _pct(x: float) -> str:
    return f"{x * 100:.1f}%"

# Formatação monetária brasileira
def _money(x: float) -> str:
    return f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def make_markdown_report(payload: Dict[str, Any], ratios: Dict[str, float], llm_text: str) -> str:
    company = payload["company"]
    fin = payload["financials"]
    rec = payload["receivable"]
    beh = payload["behavioral"]

    md = []
    md.append("# Relatório Preliminar de Risco — Duplicata Escritural")
    md.append(f"*Gerado em:* {datetime.utcnow().isoformat()}Z")
    md.append("")
    md.append("## 1) Identificação")
    md.append(f"- **Empresa:** {company['name']}")
    md.append(f"- **CNPJ:** {company['cnpj']}")
    md.append(f"- **Setor / Região:** {company['sector']} / {company['region']}")
    md.append("")
    md.append("## 2) Recebível (Duplicata)")
    md.append(f"- **Tipo:** {rec['type']}")
    md.append(f"- **Valor:** {_money(rec['amount'])}")
    md.append(f"- **Prazo:** {rec['due_days']} dias")
    md.append("")
    md.append("## 3) Sinais Comportamentais")
    md.append(f"- **Histórico de pagamento:** {beh.get('payment_history', 'unknown')}")
    md.append(f"- **Eventos de inadimplência {fin['period_months']}m):** {beh.get('delinquency_events_last_12m', 0)}")
    md.append("")
    md.append("## 4) Resumo Financeiro (input)")
    md.append(f"- **Receita (12m):** {_money(fin['revenue'])}")
    md.append(f"- **Custos (COGS):** {_money(fin['cogs'])}")
    md.append(f"- **Despesas operacionais (Opex):** {_money(fin['operating_expenses'])}")
    md.append(f"- **Ativo circulante:** {_money(fin['assets_current'])}")
    md.append(f"- **Passivo circulante:** {_money(fin['liabilities_current'])}")
    md.append(f"- **Ativo total:** {_money(fin['assets_total'])}")
    md.append(f"- **Passivo total:** {_money(fin['liabilities_total'])}")
    md.append(f"- **Patrimônio líquido:** {_money(fin['equity'])}")
    md.append("")
    md.append("## 5) Indicadores Financeiros (calculados)")
    md.append("| Indicador | Valor | Interpretação rápida |")
    md.append("|---|---:|---|")
    md.append(f"| Margem Bruta | {_pct(ratios['gross_margin'])} | quanto sobra após custos diretos |")
    md.append(f"| Margem EBIT | {_pct(ratios['ebit_margin'])} | eficiência operacional (antes de juros/impostos) |")
    md.append(f"| Liquidez Corrente | {ratios['current_ratio']:.2f} | >1 tende a indicar folga de curto prazo |")
    md.append(f"| Dívida / Ativos | {ratios['debt_to_assets']:.2f} | parcela dos ativos financiada por dívida |")
    md.append(f"| Dívida / Patrimônio | {ratios['debt_to_equity']:.2f} | alavancagem (cuidado se muito alto) |")
    md.append(f"| Opex / Receita | {_pct(ratios['opex_ratio'])} | peso das despesas operacionais |")
    md.append("")
    md.append("## 6) Interpretação por IA Generativa")
    md.append("> **Nota:** A IA fornece um **risco preliminar** e recomendações. A decisão final é humana.")
    md.append("")
    md.append(llm_text.strip())
    md.append("")
    return "\n".join(md)