# 🧠 Automação da Carpintaria Intelectual na Análise de Duplicatas Escriturais

Este repositório apresenta um **MVP (Minimum Viable Product)** que automatiza tarefas repetitivas do trabalho de um **analista de crédito**, no contexto de **duplicatas escriturais**.  
A solução demonstra como **workflows automatizados e IA generativa** podem apoiar decisões humanas, reduzindo esforço manual, padronizando análises e aumentando a escala operacional.

---

## 📌 O que é uma Duplicata Escritural

Uma **duplicata** é um título de crédito que representa um **direito de recebimento futuro**, originado de uma venda a prazo. Ela formaliza a obrigação de pagamento do comprador e pode ser utilizada para controle financeiro, cobrança ou antecipação de crédito.

Com a evolução regulatória e tecnológica, surge a **duplicata escritural**, que substitui o documento físico por um **registro eletrônico padronizado**, mantido em sistemas autorizados. Esse modelo elimina papel, reduz fraudes e aumenta a rastreabilidade das operações.

Na prática, a duplicata escritural:
- formaliza o recebível de forma digital;
- facilita o controle de pagamentos e inadimplência;
- aumenta a segurança jurídica das operações;
- permite maior escala na negociação de recebíveis.

Esse modelo é amplamente discutido no contexto de **controle de pagamentos e gestão de recebíveis**, conforme descrito pela Serasa Experian:  
https://www.serasaexperian.com.br/conteudos/controle-de-pagamentos-de-clientes/

---

## 🔍 O Problema

A digitalização das duplicatas transforma o recebível em um **ativo financeiro estruturado**, mas também gera um novo desafio operacional: **o aumento massivo no volume de títulos a serem analisados**.

Cada duplicata exige que um analista:
- valide dados,
- calcule indicadores financeiros,
- interprete risco de crédito,
- produza documentação padronizada.

Hoje, grande parte desse trabalho ainda é feita **manualmente**, mesmo sendo altamente repetitiva e estruturável.  
Esse conjunto de tarefas cognitivas operacionais é o que este projeto chama de **“carpintaria intelectual”**.

Com o crescimento do mercado de duplicatas escriturais, manter esse processo manual:
- cria gargalos,
- aumenta risco de erro,
- limita escala.

---

## 🎯 Objetivo da Solução

O objetivo deste projeto é **automatizar a carpintaria intelectual** — as etapas iniciais, repetitivas e estruturáveis do trabalho do analista de crédito — mantendo o **julgamento humano** apenas onde ele realmente agrega valor.

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

| O*NET Task | Descrição resumida | Implementação no projeto |
|-----------|--------------------|--------------------------|
| Task 3 | Generate financial ratios to evaluate customers' financial status | `ratios.py` |
| Task 1 | Analyze credit data to determine degree of risk | `llm.py` |
| Task 4 | Prepare reports that include the degree of risk involved | `report.py` |

Essas tarefas formam um pipeline lógico:
**dados → interpretação → comunicação**, refletindo o fluxo real de trabalho do analista.

---

## 🧩 Arquitetura da Solução (MVP)

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
+ src/
  + init.py
  + main.py        # Orquestra o workflow completo
  + schemas.py     # Contratos de dados (validação do input)
  + ratios.py      # Cálculo determinístico de indicadores financeiros
  + llm.py         # Interpretação preliminar de risco com IA generativa
  + report.py      # Geração do relatório em Markdown
  + utils.py       # Funções utilitárias de I/O
+ data/
  + sample_input.json
  + low_risk.json
  + medium_risk.json
  + high_risk.json
+ outputs/         # Relatórios gerados (não versionado)
+ .env.example     # Exemplo de variáveis de ambiente
+ requirements.txt
+ README.md

---
## ▶️ Como Executar o Projeto

### Pré-requisitos
- Python 3.11+

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

# 🤖 IA Generativa - API

Neste MVP, a **Groq API** foi utilizada como provider de IA generativa. No entanto, a arquitetura do projeto **não é acoplada a um provider específico**.

- A camada de IA está isolada em `llm.py`
- Qualquer provider compatível (ex: OpenAI, Azure OpenAI, Anthropic, etc.) pode ser integrado
- A troca de provider exige apenas ajustes de configuração e chamada de API

O objetivo do projeto é demonstrar o **workflow de automação**, e não avaliar ou comparar modelos específicos.

# 🧪 Dados Utilizados

Os dados utilizados neste projeto são **mockados / sintéticos**, criados exclusivamente para demonstrar o funcionamento do workflow.

- Nenhum dado real de empresa ou operação financeira é utilizado
- Os cenários (`low_risk`, `medium_risk`, `high_risk`) representam **casos hipotéticos**
- Os valores não devem ser interpretados como análises reais de crédito

O foco do MVP é validar a **ideia, arquitetura e automação das tarefas**, e não produzir avaliações de risco reais em ambiente produtivo.

---

## 🏁 Conclusão

A duplicata escritural transforma um direito de recebimento em um ativo financeiro digital, escalável e rastreável. Para que esse modelo funcione de forma segura em grande escala, é fundamental automatizar as tarefas repetitivas que antecedem a decisão humana.

Este projeto demonstra como automação e IA generativa podem cumprir esse papel de forma pragmática, responsável e alinhada à rotina real de um analista de crédito.
