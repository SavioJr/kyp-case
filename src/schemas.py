"""
schemas.py
Contrato de dados do projeto (Pydantic).

- Define o "shape" esperado do JSON de entrada
- Garante validação cedo (campos obrigatórios / tipos)
- Deixa o pipeline mais robusto e fácil de avaliar (erros claros)
"""

from pydantic import BaseModel, Field
from typing import Literal


class Company(BaseModel):
    name: str
    cnpj: str
    sector: str
    region: str


class Financials(BaseModel):
    # Período de referência (ex: últimos 12 meses)
    period_months: int = Field(ge=1, le=12)

    # Demonstração simplificada (valores anuais ou últimos 12 meses)
    revenue: float = Field(ge=0)
    cogs: float = Field(ge=0)
    operating_expenses: float = Field(ge=0)

    # Balanço simplificado
    assets_current: float = Field(ge=0)
    assets_total: float = Field(ge=0)
    liabilities_current: float = Field(ge=0)
    liabilities_total: float = Field(ge=0)

    # Patrimônio líquido
    equity: float


class Receivable(BaseModel):
    # Neste MVP, focamos apenas em duplicata escritural
    type: Literal["duplicata_escritural"]
    amount: float = Field(ge=0)
    due_days: int = Field(ge=0, le=365)


class Behavioral(BaseModel):
    # Sinal comportamental simples
    payment_history: Literal["regular", "irregular", "unknown"] = "unknown"
    delinquency_events_last_12m: int = Field(ge=0, le=100)


class InputPayload(BaseModel):
    company: Company
    financials: Financials
    receivable: Receivable
    behavioral: Behavioral