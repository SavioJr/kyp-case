"""
ratios.py
Cálculos determinísticos de indicadores financeiros.

📌 O*NET Task 3:
"Generate financial ratios, using computer programs, to evaluate customers' financial status."

Por que isso importa:
- É a parte 100% auditável e reprodutível do pipeline.
- Remove trabalho manual repetitivo do analista (carpintaria intelectual).
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
    gross_profit = fin.revenue - fin.cogs
    ebit = gross_profit - fin.operating_expenses

    ratios = {
        # Margens
        "gross_margin": _safe_div(gross_profit, fin.revenue),
        "ebit_margin": _safe_div(ebit, fin.revenue),

        # Liquidez
        "current_ratio": _safe_div(fin.assets_current, fin.liabilities_current),

        # Endividamento / alavancagem
        "debt_to_assets": _safe_div(fin.liabilities_total, fin.assets_total),
        "debt_to_equity": _safe_div(fin.liabilities_total, fin.equity),

        # Estrutura de custos
        "opex_ratio": _safe_div(fin.operating_expenses, fin.revenue),
    }
    return ratios