# RELATORIO FINAL
## Trabalho Computacional - Metodos Eletricos

---

## EXERCICIO 1 - EQUACAO DE ARCHIE

### Objetivo
Estimar os coeficientes da equacao de Archie (fator de tortuosidade **a** e expoente de cimentacao **m**) a partir de dados de porosidade e resistividade de rochas carbonaticas saturadas.

### Equacao Utilizada
```
Rt/Rw = a * φ^(-m)
```

Onde:
- **Rt**: Resistividade da rocha saturada (ohm.m)
- **Rw**: Resistividade do fluido saturante = 9,5 ohm.m
- **φ**: Porosidade da rocha
- **a**: Fator de tortuosidade
- **m**: Expoente de cimentacao

### Metodologia
1. Carregamento dos dados de porosidade (Phi) e resistividade (Rt)
2. Calculo da razao Rt/Rw
3. Linearizacao da equacao: log(Rt/Rw) = log(a) - m*log(φ)
4. Regressao linear nos dados logaritmicos
5. Extracao dos coeficientes a e m

### Resultados Obtidos

#### Parametros Estimados
- **Fator de tortuosidade (a)**: 0,6063
- **Expoente de cimentacao (m)**: 1,6883
- **Coeficiente de correlacao (R²)**: 0,4182
- **Erro padrao**: 0,6005

#### Equacao Ajustada
```
Rt/Rw = 0,6063 * φ^(-1,6883)
```

### Interpretacao dos Resultados

#### 1. Fator de Tortuosidade (a = 0,6063)
- Valor moderado, tipico de rochas carbonaticas
- Indica poros com alguma conectividade, mas ainda tortuosos
- Caminhos para fluxo de corrente eletrica nao sao totalmente diretos

#### 2. Expoente de Cimentacao (m = 1,6883)
- Valor tipico para areias nao consolidadas
- Indica cimentacao fraca a moderada
- Valor ligeiramente abaixo do esperado para carbonatos bem cimentados (m ~2,0)

#### 3. Tipo de Rocha Provavel
- **CARBONATO COM CARACTERISTICAS MISTAS**
- Possivelmente carbonato com cimentacao moderada
- Pode apresentar heterogeneidades na estrutura porosa

#### 4. Qualidade do Ajuste (R² = 0,4182)
- Ajuste moderado
- Sugere heterogeneidades na rocha ou variabilidade na porosidade
- Pode indicar presenca de diferentes tipos de poros (intergranular, vugular, fraturas)

### Graficos Gerados
- **Grafico 1**: Rt/Rw vs Porosidade (escala linear)
- **Grafico 2**: Rt/Rw vs Porosidade (escala log-log)

Arquivo: `exercicio1_archie_grafico.png`

### Arquivos Gerados
1. `exercicio1_archie_grafico.png` - Graficos de ajuste
2. `exercicio1_archie_resultados.csv` - Dados completos com predicoes
3. `exercicio1_archie_parametros.txt` - Parametros estimados

---

## EXERCICIO 2 - SONDAGEM ELETRICA VERTICAL (SEV)

### Objetivo
Analisar dados de Sondagem Eletrica Vertical (SEV) com arranjo Schlumberger para identificar camadas geologicas e interpretar materiais com base nos contrastes de resistividade.

### Metodologia
1. Leitura dos dados de 3 casos (caso1, caso2, caso3)
2. Cada caso contem 3 linhas de sondagem (SE-01, SE-02, SE-03)
3. Calculo da pseudo-profundidade (AB/3)
4. Interpolacao dos dados para criar pseudosecoes de resistividade
5. Analise de curvas de resistividade aparente vs AB/2
6. Interpretacao geologica baseada em faixas de resistividade

### Estrutura dos Dados
- **Coluna 1**: AB/2 - Espacamento dos eletrodos de corrente (m)
- **Coluna 2**: MN/2 - Espacamento dos eletrodos de potencial (m)
- **Coluna 3**: ρa - Resistividade aparente (ohm.m)

### Resultados por Caso

#### CASO 1
| Parametro | Valor |
|-----------|-------|
| Resistividade minima | 493,41 ohm.m |
| Resistividade maxima | 2.904,07 ohm.m |
| Resistividade media | 1.547,64 ohm.m |
| Profundidade maxima investigada | 100,0 m |
| Numero de medicoes | 76 |
| Razao de contraste | 5,9x |

**Interpretacao Geologica - CASO 1:**
- Resistividade muito alta (> 1000 ohm.m)
- Compativel com: **ROCHA CRISTALINA, GRANITO ou AREIA MUITO SECA**
- Contraste moderado de resistividade (5,9x)
- Provavel presenca de **2-3 camadas distintas**
- Material relativamente homogeneo em profundidade

#### CASO 2
| Parametro | Valor |
|-----------|-------|
| Resistividade minima | 246,71 ohm.m |
| Resistividade maxima | 8.350,22 ohm.m |
| Resistividade media | 1.333,26 ohm.m |
| Profundidade maxima investigada | 100,0 m |
| Numero de medicoes | 76 |
| Razao de contraste | 33,8x |

**Interpretacao Geologica - CASO 2:**
- Ampla variacao de resistividade (246 a 8.350 ohm.m)
- **Alto contraste de resistividade (33,8x)**
- Indica presenca de **MULTIPLAS CAMADAS com propriedades muito distintas**
- Possivel sequencia: **camada superficial condutiva → camada profunda resistiva**
- Camada superficial: compativel com AREIA UMIDA ou ARENITO (200-500 ohm.m)
- Camada profunda: compativel com ROCHA CRISTALINA ou GRANITO (> 1000 ohm.m)
- **Caso mais heterogeneo dos tres**

#### CASO 3
| Parametro | Valor |
|-----------|-------|
| Resistividade minima | 493,41 ohm.m |
| Resistividade maxima | 2.629,65 ohm.m |
| Resistividade media | 1.316,23 ohm.m |
| Profundidade maxima investigada | 100,0 m |
| Numero de medicoes | 76 |
| Razao de contraste | 5,3x |

**Interpretacao Geologica - CASO 3:**
- Resistividade muito alta (> 1000 ohm.m)
- Compativel com: **ROCHA CRISTALINA, GRANITO ou AREIA MUITO SECA**
- Contraste moderado de resistividade (5,3x)
- Provavel presenca de **2-3 camadas distintas**
- Perfil similar ao CASO 1

### Comparacao entre os 3 Casos

| Caso | Rho_min (ohm.m) | Rho_max (ohm.m) | Rho_media (ohm.m) | Contraste |
|------|-----------------|-----------------|-------------------|-----------|
| caso1 | 493,41 | 2.904,07 | 1.547,64 | 5,9x |
| caso2 | 246,71 | 8.350,22 | 1.333,26 | **33,8x** |
| caso3 | 493,41 | 2.629,65 | 1.316,23 | 5,3x |

**Observacoes:**
- **CASO 2** apresenta o maior contraste de resistividade (33,8x)
- **CASO 2** e o unico com resistividade minima < 300 ohm.m
- **CASO 1** apresenta a maior resistividade media (1.547,64 ohm.m)
- **CASO 1 e CASO 3** apresentam perfis similares
- **CASO 2** indica estrutura geologica mais complexa com multiplas camadas

### Analise das Pseudosecoes

#### Caracteristicas Observadas:
1. **Variacao Lateral**: Pequenas variacoes entre as 3 linhas de sondagem em cada caso
2. **Variacao Vertical**: Aumento da resistividade com a profundidade (geral)
3. **Anomalias**: CASO 2 apresenta anomalias de alta resistividade mais pronunciadas

### Faixas de Resistividade Tipicas (Referencia)
| Material | Resistividade (ohm.m) |
|----------|----------------------|
| Argila saturada | 1 - 20 |
| Areia/silte umido | 20 - 200 |
| Areia seca | 200 - 2000 |
| Arenito | 100 - 1000 |
| Calcario | 50 - 1000 |
| Granito | 1000 - 10000 |
| Rocha cristalina | 1000 - 100000 |

### Graficos Gerados

#### Por Caso:
- `exercicio2_SEV_caso1_analise.png`
- `exercicio2_SEV_caso2_analise.png`
- `exercicio2_SEV_caso3_analise.png`

Cada grafico contem:
1. Pseudosecao de resistividade aparente
2. Curvas de resistividade (log-log) por linha
3. Histograma de distribuicao de resistividade

#### Comparacao Geral:
- `exercicio2_SEV_comparacao_geral.png` - Comparacao das curvas dos 3 casos

### Arquivos Gerados
1. **Dados detalhados** (CSV):
   - `exercicio2_SEV_caso1_dados.csv`
   - `exercicio2_SEV_caso2_dados.csv`
   - `exercicio2_SEV_caso3_dados.csv`

2. **Graficos de analise** (PNG):
   - `exercicio2_SEV_caso1_analise.png`
   - `exercicio2_SEV_caso2_analise.png`
   - `exercicio2_SEV_caso3_analise.png`

3. **Comparacao** (CSV e PNG):
   - `exercicio2_SEV_comparacao_casos.csv`
   - `exercicio2_SEV_comparacao_geral.png`

---

## CONCLUSOES GERAIS

### Exercicio 1 - Equacao de Archie
1. Os coeficientes estimados (a=0,606, m=1,688) indicam rocha carbonatica com cimentacao moderada
2. O R² moderado (0,418) sugere heterogeneidade na estrutura porosa
3. A rocha provavelmente apresenta sistema poroso misto (intergranular + vugular ou fraturas)

### Exercicio 2 - SEV
1. **CASO 1 e CASO 3**: Perfis similares, materiais resistivos (possivelmente rocha cristalina ou areia seca)
2. **CASO 2**: Perfil mais complexo com multiplas camadas, variando de material moderadamente condutivo em superficie a muito resistivo em profundidade
3. Todos os casos investigaram ate 100 m de profundidade
4. A tecnica de SEV foi eficaz para identificar contrastes de resistividade e inferir camadas geologicas

### Metodologia Aplicada
- **Processamento**: Python 3.14 com bibliotecas NumPy, Pandas, Matplotlib e SciPy
- **Visualizacao**: Graficos em alta resolucao (300 DPI)
- **Formato de dados**: CSV com separador ";" e decimal ","
- **Interpretacao**: Baseada em faixas de resistividade de materiais geologicos conhecidos

---

## ARQUIVOS DO PROJETO

### Scripts Python
- `C:\projetos\CC2\servic\exercicio1_archie.py`
- `C:\projetos\CC2\servic\exercicio2_SEV.py`

### Resultados Exercicio 1
- Grafico: `exercicio1_archie_grafico.png`
- Dados: `exercicio1_archie_resultados.csv`
- Parametros: `exercicio1_archie_parametros.txt`

### Resultados Exercicio 2
- Graficos individuais: `exercicio2_SEV_caso[1-3]_analise.png`
- Dados individuais: `exercicio2_SEV_caso[1-3]_dados.csv`
- Comparacao: `exercicio2_SEV_comparacao_casos.csv`
- Grafico comparativo: `exercicio2_SEV_comparacao_geral.png`

### Relatorio
- `RELATORIO_FINAL_Metodos_Eletricos.md` (este arquivo)

---

**Data de execucao**: 2025-10-13
**Software utilizado**: Python 3.14.0
**Bibliotecas**: NumPy 2.3.3, Pandas 2.3.3, Matplotlib 3.10.7, SciPy 1.16.2
