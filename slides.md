---
marp: true
theme: default
paginate: true
footer: "KYP Case — Automação da Análise de Duplicatas Escriturais"
style: |
  section {
    background-color: #0e0e0e;
    color: #f5f5f5;
  }
  h1, h2, h3 {
    color: #ffffff;
  }
  footer {
    color: #aaaaaa;
  }
  /* ===== TABLE FIX ===== */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85em;
  }

  th {
    background-color: #1f2933;
    color: #ffffff;
    padding: 12px;
    border: 1px solid #4b5563;
    text-align: left;
  }

  td {
    background-color: #111827;
    color: #e5e7eb;
    padding: 12px;
    border: 1px solid #374151;
  }

  tr:nth-child(even) td {
    background-color: #0b1220;
  }
---

# 🧠 KYP Case  
## Automação da Análise de Duplicatas Escriturais

**Domingos Sávio**  
MVP — Credit Analysis Automation  
GitHub: https://github.com/SavioJr/kyp-case

---

## 📌 O que é uma Duplicata Escritural

- Título de crédito que representa um **direito de recebimento futuro**
- Evolução da duplicata física para um **registro eletrônico padronizado**
- Mais segurança jurídica, rastreabilidade e eficiência

📈 **Impacto direto:** aumento significativo no volume de operações

---

## 🔍 O Problema

- Digitalização → **escala**
- Cada duplicata exige:
  - validação de dados
  - cálculo de indicadores
  - análise de risco
  - geração de relatório

⚠️ Processos manuais **não escalam**  
➡️ Gargalos, atrasos e maior risco operacional

---

## 🎯 Objetivo do Projeto

**Automatizar a “carpintaria intelectual”**  
(etapas repetitivas e estruturáveis do analista)

- Acelerar a análise preliminar
- Padronizar avaliações
- Reduzir esforço manual
- Preservar decisão final humana

👉 **MVP focado em triagem inicial**

---

## 📌 Alinhamento com O*NET (Credit Analyst)

Baseado no O*NET — *Credit Analyst (13-2041.00)*

| O*NET Task | Importância | Descrição | Implementação |
|-----------|------------|-----------|---------------|
| Task 3 | 89 | Generate financial ratios to evaluate customers' financial status | `ratios.py` |
| Task 1 | 98 | Analyze credit data to determine degree of risk | `llm.py` |
| Task 4 | 89 | Prepare reports that include the degree of risk involved | `report.py` |

🧩 Pipeline lógico: **dados → interpretação → comunicação**

---

## ⚙️ Arquitetura da Solução

```
JSON (mockado)
   ↓
Validação + Ratios
   ↓
Interpretação com LLM
   ↓
Relatório Padronizado (.md)
```

- Cálculos determinísticos
- IA como **assistente**
- Outputs auditáveis

---

## 📥 Input Data — Financials

Recorte padrão de:
- **DRE simplificada**
- **Balanço patrimonial simplificado**

### Variáveis usadas (exemplos):
- `revenue` → receita do período    
- `operating_expenses` → despesas operacionais  

- `assets_current` → ativo circulante  
- `equity` → patrimônio líquido  

➡️ Adequado para risco de duplicata (prazo curto)

---

## 📊 Indicadores Calculados - Python

Os ratios calculados capturam:
- **geração de lucro**
- **liquidez** (ativo vs passivo circulante)
- **endividamento** (dívida vs patrimônio)

### Exemplos práticos:
- `current_ratio = assets_current / liabilities_current`  
  → capacidade de pagar obrigações no mesmo prazo do recebível

- `gross_margin = (revenue - cogs) / revenue`  
  → quanto sobra após custos diretos

---

## 🤖 IA Generativa (LLM)

- Interpretação preliminar
- Justificativas e pontos de atenção
- Perguntas para o analista

⚠️ IA **não decide**
- Apoio cognitivo
- Decisão final humana

---

## 📝 Relatório Final

- Gerado automaticamente
- Formato Markdown
- Estrutura fixa e auditável

---