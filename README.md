# 🧠 Automação da Carpintaria Intelectual na Análise de Duplicatas Escriturais

Este repositório apresenta um **MVP (Minimum Viable Product)** que automatiza tarefas repetitivas do trabalho de um **analista de crédito**, no contexto de **duplicatas escriturais**. 

---

## 🎥 Demonstração em Vídeo (5 minutos)

Clique na imagem abaixo para assistir a uma rápida explicação sobre o projeto:

[![KYP Case Demo](https://img.youtube.com/vi/_1iDfU89DrU/maxresdefault.jpg)](https://youtu.be/_1iDfU89DrU)

---

## 📌 O que é uma Duplicata Escritural

Uma **duplicata** é um título de crédito que representa um **direito de recebimento futuro** em uma venda à prazo, formalizando a obrigação de pagamento do comprador por um produto ou serviço.

Com a evolução regulatória e tecnológica, surge a **duplicata escritural**, que substitui o documento físico por um **registro eletrônico padronizado** intermediado por uma instiuição financeira ou uma registradora. Esse modelo elimina papel, diminuindo burocracia e aumentando a rastrabilidade e transparência das operações.

Na prática, a duplicata escritural:
- formaliza o recebível de forma digital, com registro obrigatório;
- facilita o controle de pagamentos e inadimplência;
- aumenta a segurança jurídica das operações;
- permite maior escala na negociação de recebíveis.

Referência: https://www.serasaexperian.com.br/conteudos/controle-de-pagamentos-de-clientes/

---

## 🔍 O Problema

A digitalização das duplicatas gera um novo desafio operacional: **o aumento massivo no volume de títulos a serem analisados**.

Cada duplicata exige que um analista:
- valide dados,
- calcule indicadores financeiros,
- interprete risco de crédito,
- produza documentação padronizada.

Como grande parte desse trabalho é repetitivo/estruturável e considerando o crescimento do mercado de duplicatas escriturais, executar esses processos de forma manual:
- cria gargalos,
- aumenta risco de erro,
- limita escala.

---

## 🎯 Objetivo da Solução

O objetivo deste projeto é **automatizar a "carpintaria" intelectual** — as etapas iniciais, repetitivas e estruturáveis do trabalho do analista de crédito — mantendo o **julgamento humano** apenas onde ele realmente agrega valor.

A solução:
- acelera a análise preliminar;
- padroniza avaliações;
- gera relatórios consistentes;
- preserva a decisão final para o analista.

---

## 📌 Alinhamento com Atividades do Analista de Crédito (O*NET)

O projeto foi desenhado com base nas atividades descritas no **O*NET** para o cargo de **Credit Analyst (13-2041.00)**:  
https://www.onetonline.org/link/details/13-2041.00

Foram selecionadas tarefas altamente estruturáveis e ideais para automação:

| O*NET Task | Importância | Descrição | Implementação no projeto |
|-----------|------------|-----------|--------------------------|
| Task 3 | 89 | Generate financial ratios to evaluate customers' financial status | `ratios.py` |
| Task 1 | 98 | Analyze credit data to determine degree of risk | `llm.py` |
| Task 4 | 89 | Prepare reports that include the degree of risk involved | `report.py` |

Essas tarefas formam um pipeline lógico:
**dados → interpretação → comunicação**, refletindo o fluxo real de trabalho do analista.

---

## 🧩 Arquitetura da Solução

### Entrada
- Arquivo JSON mockado contendo:
  - dados da empresa,
  - informações financeiras básicas,
  - dados da duplicata,
  - sinais comportamentais.

### Etapas do Workflow
1. **Validação de dados**
   - verificação de campos obrigatórios;
   - padronização de formatos.

2. **Cálculo automático de indicadores financeiros**
   - margens,
   - liquidez,
   - endividamento,
   - alavancagem.

3. **Interpretação preliminar de risco com IA generativa**
   - classificação de risco (baixo / médio / alto);
   - justificativa textual baseada nos indicadores.

4. **Geração automática de relatório**
   - sumário executivo;
   - grau de risco;
   - pontos de atenção;
   - observações para revisão humana.

### Saída
- Relatório estruturado (`.md`);
- contexto e indicadores auditáveis (`.json`).

---

## 📁 Estrutura do Projeto

```text
src/
├── __init__.py        # Torna o diretório src um pacote Python
├── main.py            # Orquestra o workflow completo
├── schemas.py         # Contratos de dados (validação do input)
├── ratios.py          # Cálculo determinístico de indicadores financeiros
├── llm.py             # Interpretação preliminar de risco com IA generativa
├── report.py          # Geração do relatório final em Markdown
└── utils.py           # Funções utilitárias de I/O

data/
├── sample_input.json   # Exemplo de entrada válida
├── invalid_input.json  # Exemplo de entrada inválida (validação Pydantic)
├── low_risk.json       # Cenário mockado: baixo risco
├── medium_risk.json    # Cenário mockado: médio risco
└── high_risk.json      # Cenário mockado: alto risco

outputs/               # Relatórios gerados (não versionado)

.env.example           # Exemplo de variáveis de ambiente
requirements.txt       # Dependências do projeto
README.md
```

---
## ▶️ Como Executar o Projeto

### Pré-requisitos
- Python 3.11+

### 0. Clonar o Repositório
```bash
git clone https://github.com/SavioJr/kyp-case.git
cd kyp-case
```

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente
```bash
cp .env.example .env
# edite o arquivo .env e insira sua chave de API
```

### 3. Executar Pipeline
```bash
python -m src.main --input data/sample_input.json --out outputs
```

- Edite o input para apontar para seu arquivo `.json`
- Os relatórios são gerados no diretório `outputs/` em formato Markdown (`.md`)

---

## 🚀 Ganho de Eficiência

A automação permite:
- reduzir o tempo de análise inicial de horas para minutos;
- padronizar avaliações preliminares;
- reduzir erros operacionais;
- escalar a operação sem crescimento proporcional de equipe.

O analista passa a focar em exceções e decisões de maior impacto.

---

## ⚠️ Limitações e Próximos Passos

O sistema **não substitui o julgamento humano**.

- Não há integração com bases externas neste MVP.
- Próximos passos possíveis:
  - human-in-the-loop;
  - feedback contínuo dos analistas;
  - integração com registradoras e fontes externas.

## 🤖 IA Generativa - API

Neste MVP, a **Groq API** foi utilizada como provider de IA generativa. No entanto, a arquitetura do projeto **não é acoplada a um provider específico**.

- A camada de IA está isolada em `llm.py`
- Qualquer provider compatível (ex: OpenAI, Azure OpenAI, Anthropic, etc.) pode ser integrado
- A troca de provider exige apenas ajustes de configuração e chamada de API

O objetivo do projeto é demonstrar o **workflow de automação**, e não avaliar ou comparar modelos específicos.

## 🧪 Dados Utilizados

Os dados utilizados neste projeto são **mockados / sintéticos**, criados exclusivamente para demonstrar o funcionamento do workflow.

- Nenhum dado real de empresa ou operação financeira é utilizado
- Os cenários (`low_risk`, `medium_risk`, `high_risk`) representam **casos hipotéticos**
- Os valores não devem ser interpretados como análises reais de crédito

O foco do MVP é validar a **ideia, arquitetura e automação das tarefas**, e não produzir avaliações de risco reais em ambiente produtivo.

---

## 🏁 Conclusão

A duplicata escritural transforma um direito de recebimento em um ativo financeiro digital, escalável e rastreável. Para que esse modelo funcione de forma segura em grande escala, é fundamental automatizar as tarefas repetitivas que antecedem a decisão humana.

Este projeto demonstra como automação e IA generativa podem cumprir esse papel de forma pragmática, responsável e alinhada à rotina real de um analista de crédito.
