"""
ratios.py
Cálculos determinísticos de indicadores financeiros.

📌 O*NET Task 3:
"Generate financial ratios, using computer programs, to evaluate customers' financial status."

"""

from typing import Dict
from .schemas import Financials

EPS = 1e-9 # Evitar divisão por zero


def _safe_div(a: float, b: float) -> float:
    """Divisão segura para evitar ZeroDivisionError."""
    return float(a) / float(b if abs(b) > EPS else EPS)


def compute_ratios(fin: Financials) -> Dict[str, float]:
    """
    Retorna um dicionário com ratios simples, suficientes para uma análise preliminar.

    Observação:
    - Não é um modelo contábil completo.
    - É um conjunto mínimo para demonstrar automação e interpretação por IA.
    """
    gross_profit = fin.revenue - fin.cogs # Lucro bruto (receita após custos diretos)
    ebit = gross_profit - fin.operating_expenses # Lucro bruto - despesas operacionais

    ratios = {
        # Margens
        "gross_margin": _safe_div(gross_profit, fin.revenue), # margem após custos diretos
        "ebit_margin": _safe_div(ebit, fin.revenue), # margem operacional

        # Liquidez
        "current_ratio": _safe_div(fin.assets_current, fin.liabilities_current), # capacidade de pagar dívidas de curto prazo

        # Endividamento / alavancagem
        "debt_to_assets": _safe_div(fin.liabilities_total, fin.assets_total), # parcela dos ativos financiada por dívida
        "debt_to_equity": _safe_div(fin.liabilities_total, fin.equity), # alavancagem em relação ao patrimônio

        # Estrutura de custos
        "opex_ratio": _safe_div(fin.operating_expenses, fin.revenue), # peso das despesas operacionais na receita
    }
    return ratios