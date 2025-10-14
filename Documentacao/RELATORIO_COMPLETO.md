# TRABALHO COMPUTACIONAL - METODOS ELETRICOS
## Geofísica Aplicada

---

## IDENTIFICACAO DO TRABALHO

**Disciplina:** Métodos Elétricos em Geofísica
**Data de Execução:** 13 de Outubro de 2025
**Formato de Entrega:** Pasta organizada com resultados completos

---

## CONTEUDO DA PASTA DE ENTREGA

Esta pasta contém todos os arquivos resultantes do trabalho computacional divididos em 4 subpastas:

```
ENTREGA_TRABALHO/
├── Exercicio1_Archie/          (3 arquivos)
├── Exercicio2_SEV/             (8 arquivos)
├── Scripts/                    (2 arquivos)
├── Documentacao/               (3 arquivos)
└── LEIA-ME.md                  (este arquivo)
```

**TOTAL:** 16 arquivos + 1 guia (este arquivo)

---

## DESCRICAO DOS EXERCICIOS

### **EXERCICIO 1 - EQUACAO DE ARCHIE**

**Objetivo:**
Estimar os parâmetros da equação de Archie (fator de tortuosidade `a` e expoente de cimentação `m`) a partir de dados de porosidade e resistividade de rochas carbonáticas saturadas.

**Equação Utilizada:**
```
Rt/Rw = a × φ^(-m)
```

**Metodologia:**
1. Carregamento de 13 amostras de rochas carbonáticas
2. Cálculo da razão Rt/Rw
3. Linearização logarítmica da equação
4. Regressão linear para estimativa dos parâmetros
5. Plotagem de gráficos (linear e log-log)
6. Interpretação geológica dos resultados

**Resultados Principais:**
- **Fator de tortuosidade (a):** 0,6063
- **Expoente de cimentação (m):** 1,6883
- **Coeficiente R²:** 0,4182
- **Interpretação:** Carbonato com cimentação moderada e estrutura porosa heterogênea

**Arquivos na pasta `Exercicio1_Archie/`:**
- `exercicio1_archie_grafico.png` - Gráficos de ajuste (linear e log-log)
- `exercicio1_archie_resultados.csv` - Dados completos com predições e resíduos
- `exercicio1_archie_parametros.txt` - Parâmetros estimados e equação ajustada

---

### **EXERCICIO 2 - SONDAGEM ELETRICA VERTICAL (SEV)**

**Objetivo:**
Analisar dados de Sondagem Elétrica Vertical com arranjo Schlumberger para identificar camadas geológicas e interpretar materiais com base nos contrastes de resistividade.

**Metodologia:**
1. Análise de 3 casos independentes
2. Cada caso possui 3 linhas de sondagem (SE-01, SE-02, SE-03)
3. Leitura de 76 medições por caso (228 medições totais)
4. Cálculo de pseudo-profundidade: AB/3
5. Interpolação cúbica para geração de pseudoseções
6. Plotagem de curvas de resistividade (escala log-log)
7. Análise estatística e interpretação geológica

**Resultados por Caso:**

| **CASO** | **Resistividade Mínima** | **Resistividade Máxima** | **Resistividade Média** | **Contraste** | **Interpretação Principal** |
|----------|--------------------------|--------------------------|-------------------------|---------------|-----------------------------|
| **Caso 1** | 493,41 Ω·m | 2.904,07 Ω·m | 1.547,64 Ω·m | 5,9x | Rocha cristalina/granito - Material homogêneo |
| **Caso 2** | 246,71 Ω·m | 8.350,22 Ω·m | 1.333,26 Ω·m | **33,8x** | Múltiplas camadas distintas - Alta heterogeneidade |
| **Caso 3** | 493,41 Ω·m | 2.629,65 Ω·m | 1.316,23 Ω·m | 5,3x | Similar ao Caso 1 - Material homogêneo |

**Observações Importantes:**
- O **Caso 2** apresenta o maior contraste de resistividade, indicando estrutura geológica complexa
- Possível sequência no Caso 2: camada superficial condutiva → camada profunda resistiva
- Casos 1 e 3 apresentam perfis similares com menor variabilidade

**Arquivos na pasta `Exercicio2_SEV/`:**
- `exercicio2_SEV_caso1_analise.png` - Pseudoseção + curvas + histograma (Caso 1)
- `exercicio2_SEV_caso2_analise.png` - Pseudoseção + curvas + histograma (Caso 2)
- `exercicio2_SEV_caso3_analise.png` - Pseudoseção + curvas + histograma (Caso 3)
- `exercicio2_SEV_caso1_dados.csv` - Dados detalhados das 3 linhas (Caso 1)
- `exercicio2_SEV_caso2_dados.csv` - Dados detalhados das 3 linhas (Caso 2)
- `exercicio2_SEV_caso3_dados.csv` - Dados detalhados das 3 linhas (Caso 3)
- `exercicio2_SEV_comparacao_casos.csv` - Tabela comparativa dos 3 casos
- `exercicio2_SEV_comparacao_geral.png` - Gráfico comparativo das curvas dos 3 casos

---

## SCRIPTS PYTHON DESENVOLVIDOS

**Pasta: `Scripts/`**

### 1. **exercicio1_archie.py**
Script completo para análise da Equação de Archie:
- Carregamento e validação de dados
- Regressão linear em escala logarítmica
- Geração de gráficos em alta resolução (300 DPI)
- Interpretação automatizada dos parâmetros
- Exportação de resultados em CSV

### 2. **exercicio2_SEV.py**
Script completo para análise de SEV:
- Leitura de dados Schlumberger (.dat)
- Cálculo de pseudo-profundidade
- Interpolação cúbica para pseudoseções
- Geração de múltiplos gráficos (pseudoseção, curvas, histogramas)
- Análise comparativa dos 3 casos
- Interpretação geológica automatizada

**Requisitos dos Scripts:**
- Python 3.14 ou superior
- Bibliotecas: NumPy, Pandas, Matplotlib, SciPy

---

## DOCUMENTACAO COMPLETA

**Pasta: `Documentacao/`**

### 1. **RELATORIO_FINAL_Metodos_Eletricos.md**
Relatório técnico completo contendo:
- Introdução e objetivos
- Metodologia detalhada de cada exercício
- Resultados numéricos e gráficos
- Interpretações geológicas fundamentadas
- Tabelas comparativas
- Conclusões e observações finais
- Lista completa de arquivos gerados

### 2. **FEEDBACK_ChatGPT.md**
Avaliação técnica do trabalho por IA especializada:
- Análise da coerência dos resultados do Archie
- Avaliação da interpretação geológica do SEV
- Pontos fortes identificados
- Sugestões de melhorias futuras
- Validação da metodologia aplicada

### 3. **projeto_log.txt**
Log detalhado de todas as atividades realizadas:
- Cronologia de execução
- Configurações utilizadas
- Decisões metodológicas
- Problemas encontrados e soluções
- Estatísticas do projeto

---

## ESPECIFICACOES TECNICAS

### **Software e Bibliotecas:**
- **Python:** 3.14.0
- **NumPy:** 2.3.3
- **Pandas:** 2.3.3
- **Matplotlib:** 3.10.7
- **SciPy:** 1.16.2

### **Formato dos Arquivos:**
- **Gráficos:** PNG, 300 DPI, alta qualidade
- **Dados:** CSV com separador ";" e decimal ","
- **Documentação:** Markdown (.md) e texto (.txt)

### **Qualidade e Validação:**
- Todos os scripts foram testados e executados com sucesso
- Gráficos gerados em resolução adequada para impressão
- Dados exportados em formato compatível com Excel
- Interpretações baseadas em literatura geofísica estabelecida

---

## COMO UTILIZAR ESTE MATERIAL

### **Para Visualização Rápida:**
1. Abra os arquivos PNG para ver os gráficos
2. Consulte o `RELATORIO_FINAL_Metodos_Eletricos.md` para análise completa

### **Para Análise Detalhada:**
1. Abra os arquivos CSV no Excel ou LibreOffice
2. Verifique os parâmetros em `exercicio1_archie_parametros.txt`
3. Leia as interpretações no relatório final

### **Para Reproduzir os Resultados:**
1. Instale Python 3.14+ e as bibliotecas listadas
2. Execute os scripts na pasta `Scripts/`
3. Os resultados serão regenerados

### **Para Compreensão Completa:**
1. Leia o `RELATORIO_FINAL_Metodos_Eletricos.md`
2. Analise os gráficos gerados
3. Consulte o feedback técnico
4. Revise o log do projeto

---

## PRINCIPAIS CONCLUSOES

### **Exercício 1 - Equação de Archie:**
✓ Os parâmetros obtidos (a=0,606, m=1,688) são coerentes para rochas carbonáticas
✓ O R² moderado (0,418) reflete a heterogeneidade natural dos carbonatos
✓ A rocha apresenta sistema poroso misto com cimentação moderada
✓ Metodologia de regressão aplicada corretamente

### **Exercício 2 - SEV:**
✓ Identificadas diferenças significativas entre os 3 casos
✓ Caso 2 apresenta estrutura geológica mais complexa (contraste 33,8x)
✓ Pseudoseções geradas com sucesso para visualização das camadas
✓ Interpretações geológicas fundamentadas em faixas de resistividade conhecidas
✓ Técnica de SEV eficaz para caracterização de subsuperfície

---

## TABELA RESUMO DOS RESULTADOS

| **Item** | **Exercício 1** | **Exercício 2** |
|----------|----------------|-----------------|
| **Método** | Equação de Archie | SEV Schlumberger |
| **Amostras** | 13 medições | 228 medições (3 casos) |
| **Parâmetro Principal 1** | a = 0,6063 | Caso 1: 1.548 Ω·m |
| **Parâmetro Principal 2** | m = 1,6883 | Caso 2: 1.333 Ω·m |
| **Parâmetro Principal 3** | R² = 0,4182 | Caso 3: 1.316 Ω·m |
| **Gráficos Gerados** | 1 figura (2 plots) | 4 figuras |
| **Arquivos CSV** | 1 | 4 |
| **Interpretação** | Carbonato misto | Múltiplas camadas |

---

## FAIXAS DE RESISTIVIDADE - REFERENCIA

| **Material** | **Resistividade (Ω·m)** | **Observado em** |
|--------------|-------------------------|------------------|
| Argila saturada | 1 - 20 | - |
| Areia/silte úmido | 20 - 200 | - |
| Areia seca | 200 - 2000 | SEV (transição) |
| Arenito | 100 - 1000 | SEV (intermediário) |
| Calcário | 50 - 1000 | - |
| Granito | 1000 - 10000 | SEV (casos 1 e 3) |
| Rocha cristalina | 1000 - 100000 | SEV (caso 2 - camada profunda) |

---

## VALIDACAO E FEEDBACK

O trabalho foi submetido a análise por IA especializada (ChatGPT) e recebeu as seguintes avaliações:

**✓ Metodologia:** Correta e bem aplicada
**✓ Resultados:** Coerentes com teoria geofísica
**✓ Interpretação:** Fundamentada e consistente
**✓ Qualidade Técnica:** Adequada para nível acadêmico
**✓ Documentação:** Completa e organizada

**Sugestões de Melhoria Futura:**
- Implementar validação cruzada no modelo de Archie
- Integrar com dados sísmicos quando disponíveis
- Desenvolver modelos 2D/3D das pseudoseções
- Comparar com dados geológicos de campo

---

## AUTOR E INFORMACOES

**Processamento:** Python 3.14.0
**Data de Execução:** 13/10/2025
**Total de Arquivos Gerados:** 15 arquivos + documentação
**Tempo de Processamento:** < 5 minutos (ambos os exercícios)
**Status:** ✓ Trabalho completo e validado

---

## COMO CITAR ESTE TRABALHO

```
Trabalho Computacional - Métodos Elétricos em Geofísica
Exercício 1: Equação de Archie para Rochas Carbonáticas
Exercício 2: Sondagem Elétrica Vertical - Arranjo Schlumberger
Data: 13 de Outubro de 2025
Software: Python 3.14.0 (NumPy, Pandas, Matplotlib, SciPy)
```

---

## CONTATO E SUPORTE

Para dúvidas sobre:
- **Metodologia:** Consulte o RELATORIO_FINAL_Metodos_Eletricos.md
- **Código:** Revise os comentários nos scripts Python
- **Interpretação:** Veja a seção de interpretação no relatório
- **Dados:** Abra os arquivos CSV com separador ";"

---

## CHECKLIST DE ENTREGA

- [X] Exercício 1 completo (3 arquivos)
- [X] Exercício 2 completo (8 arquivos)
- [X] Scripts Python documentados (2 arquivos)
- [X] Relatório final detalhado
- [X] Feedback técnico incluído
- [X] Log do projeto atualizado
- [X] Arquivo LEIA-ME explicativo
- [X] Pasta organizada e estruturada

**STATUS FINAL: TRABALHO COMPLETO E PRONTO PARA ENTREGA**

---

*Última atualização: 13/10/2025*
