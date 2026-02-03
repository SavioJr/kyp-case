# Automação da Carpintaria Intelectual na Análise de Duplicatas Escriturais

## Contexto

Uma duplicata é um título de crédito que representa um **direito de recebimento futuro** originado de uma venda a prazo. Tradicionalmente, esse processo envolvia documentos físicos e validações manuais, o que limitava escala e aumentava risco operacional.

Com a introdução da **duplicata escritural**, esse direito passa a existir de forma **digital, padronizada e rastreável**, tornando-se um ativo financeiro estruturado e negociável. Esse avanço aumenta significativamente a eficiência do mercado, mas também gera um novo desafio: **um crescimento acelerado no volume de operações** que precisam ser analisadas.

Nesse novo cenário, processos manuais não escalam.

---

## O Problema

Cada duplicata escritural gera um conjunto de dados que precisa ser:
- validado,
- analisado,
- interpretado,
- documentado.

Hoje, grande parte desse trabalho é feita manualmente por analistas de crédito, por meio de tarefas repetitivas como:
- cálculo de indicadores financeiros,
- análise preliminar de risco,
- preparação de relatórios padronizados.

Esse conjunto de tarefas repetitivas e estruturáveis é o que o case chama de **“carpintaria intelectual”**.  
Com o aumento expressivo no volume de duplicatas, manter esse modelo manual cria gargalos operacionais, atrasos e maior probabilidade de erro.

---

## Objetivo da Solução

O objetivo deste projeto é **automatizar a carpintaria intelectual**, ou seja, as etapas iniciais, repetitivas e estruturáveis do trabalho do analista, preservando o julgamento humano apenas para os casos que realmente exigem decisão.

---

## Escopo

Foram selecionadas três tarefas típicas do trabalho de um analista de crédito, ideais para automação:

1. **Geração de indicadores financeiros**
2. **Análise preliminar de risco de crédito**
3. **Preparação de relatórios de risco**

Essas tarefas formam um pipeline lógico:
**dados → interpretação → comunicação**.

---

## Arquitetura da Solução (MVP)

A solução é implementada como um workflow automatizado.

### Entrada
- JSON mockado representando dados financeiros básicos de uma empresa relacionada a uma duplicata.

### Etapas do Workflow

1. **Validação e normalização de dados**
   - Verificação de campos obrigatórios
   - Padronização de formatos
   - Registro de inconsistências

2. **Cálculo automático de indicadores financeiros (Python)**
   - Margem
   - Liquidez
   - Endividamento
   - Alavancagem

3. **Interpretação preliminar de risco com IA generativa**
   - Classificação de risco (baixo / médio / alto)
   - Explicação textual baseada nos indicadores

4. **Geração automática de relatório**
   - Sumário executivo
   - Grau de risco
   - Principais pontos de atenção
   - Observações para revisão humana

### Saída
- Relatório estruturado
- Classificação preliminar de risco
- Dados auditáveis para análise posterior

---

## Ganho de Eficiência

A automação permite:
- reduzir o tempo de análise inicial de horas para minutos;
- padronizar avaliações;
- reduzir erros operacionais;
- escalar a operação sem aumento proporcional de equipe.

O analista passa a atuar apenas em exceções e decisões finais.

---

## Limitações e Próximos Passos

- A solução não substitui o julgamento humano.
- Próximos passos incluem:
  - human-in-the-loop;
  - aprendizado com feedback dos analistas;
  - integração com registradoras e bases externas.

---

## Conclusão

A duplicata escritural transforma um direito de recebimento em um ativo financeiro digital. Para que esse novo modelo escale com segurança, é fundamental automatizar as tarefas repetitivas que antecedem a decisão humana. Este MVP demonstra como workflows e IA generativa podem cumprir esse papel de forma pragmática e responsável.