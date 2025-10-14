# ANALISE DETALHADA
## Metodos Eletricos em Geofisica

**Data:** 13 de Outubro de 2025
**Disciplina:** Metodos Geofisicos - Trabalho Computacional

---

## RESUMO

Este trabalho apresenta uma analise detalhada de dois metodos eletricos em geofisica aplicados a rochas carbonaticas: a Lei de Archie e a Sondagem Eletrica Vertical (SEV) com arranjo Schlumberger. Foram analisadas 13 amostras de rochas carbonaticas saturadas no primeiro exercicio, obtendo-se parametros que caracterizam a tortuosidade e cimentacao das rochas. No segundo exercicio, tres casos de SEV foram investigados ate 100 metros de profundidade, revelando diferentes estruturas geologicas com contrastes de resistividade variando de 5,3x a 33,8x.

**Palavras-chave:** Geofisica, Resistividade, Lei de Archie, Sondagem Eletrica Vertical, Rochas Carbonaticas

---

## 1. INTRODUCAO TEORICA DOS METODOS

### 1.1 Metodos Eletricos em Geofisica

Os metodos eletricos em geofisica sao amplamente utilizados para investigar a estrutura e a composicao do subsolo, fundamentando-se na medicao da resistividade eletrica das rochas. A resistividade e uma propriedade fisica que reflete a capacidade de um material em resistir ao fluxo de corrente eletrica. Os metodos mais comuns incluem a Lei de Archie e o Esquema de Eletroanalise Vertical (SEV) Schlumberger, que sao aplicados na caracterizacao de reservatorios de agua, petroleo e em estudos ambientais.

### 1.2 Lei de Archie

A Lei de Archie e uma relacao empirica que descreve a resistividade aparente de uma rocha saturada em funcao da resistividade da agua (Rw), do fator de tortuosidade (a) e do expoente de cimentacao (m). Essa relacao e expressa pela equacao:

```
Ra = a · Rw · φ^(-m)
```

Onde:
- **Ra**: Resistividade aparente da rocha
- **Rw**: Resistividade do fluido saturante
- **φ**: Porosidade da rocha
- **a**: Fator de tortuosidade
- **m**: Expoente de cimentacao

Esta equacao fundamental permite inferir propriedades petrofisicas das rochas a partir de medidas eletricas, sendo amplamente utilizada na industria de petroleo e gas para caracterizacao de reservatorios.

### 1.3 Sondagem Eletrica Vertical (SEV)

O metodo SEV, por outro lado, utiliza eletrodos dispostos em uma configuracao linear para medir a resistividade em diferentes profundidades. O arranjo Schlumberger, utilizado neste estudo, caracteriza-se pela disposicao simetrica dos eletrodos em relacao a um ponto central, permitindo a investigacao progressiva em profundidade atraves do aumento do espacamento entre eletrodos.

Esse metodo permite a analise de camadas de materiais subjacentes, oferecendo informacoes sobre a variacao da resistividade com a profundidade. A interpretacao dos dados de SEV possibilita a identificacao de descontinuidades geologicas, aquiferos, e estruturas sedimentares.

---

## 2. DISCUSSAO APROFUNDADA DOS RESULTADOS DA LEI DE ARCHIE

### 2.1 Parametros Obtidos

Na analise das 13 amostras de rochas carbonaticas saturadas, foram obtidos os seguintes parametros:
- **a (fator de tortuosidade)**: 0,6063
- **m (expoente de cimentacao)**: 1,6883
- **R²**: 0,4182
- **Rw**: 9,5 Ω·m

### 2.2 Significado Geologico do Fator de Tortuosidade (a)

O fator de tortuosidade **a = 0,6063** indica o desvio da conducao eletrica em relacao a um caminho reto. Em rochas ideais, valores de **a** proximos de 1 sugerem uma configuracao mais homogenea e menos tortuosa, com caminhos de conducao eletrica relativamente diretos.

O valor obtido **a = 0,6063** sugere uma certa complexidade na estrutura das rochas analisadas. Esta complexidade pode ser atribuida a diversos fatores geologicos:

1. **Presenca de Fraturas**: Descontinuidades que alteram o caminho de conducao eletrica
2. **Heterogeneidades Litologicas**: Variacao na composicao mineralogica
3. **Geometria Porosa Complexa**: Poros interconectados de forma nao-uniforme
4. **Cimentacao Diferencial**: Zonas com diferentes graus de cimentacao

Para rochas carbonaticas, valores de **a** entre 0,5 e 1,0 sao comuns, sendo que valores menores indicam maior tortuosidade. O valor de 0,6063 posiciona esta rocha no meio do intervalo tipico, sugerindo uma estrutura porosa moderadamente tortuosa, caracteristica de carbonatos com certa heterogeneidade.

### 2.3 Significado Geologico do Expoente de Cimentacao (m)

O expoente de cimentacao **m = 1,6883** e indicativo da relacao entre a resistividade e a porosidade, refletindo o grau de cimentacao e conectividade dos poros.

**Interpretacao Geologica:**

- **m < 1,3**: Rochas pouco consolidadas, alta conectividade porosa
- **1,3 ≤ m < 1,8**: Areias nao consolidadas, cimentacao fraca
- **1,8 ≤ m < 2,2**: Rochas carbonaticas consolidadas (intervalo tipico)
- **m > 2,2**: Rochas altamente cimentadas, baixa conectividade

O valor obtido **m = 1,6883** situa-se ligeiramente abaixo do intervalo tipico para carbonatos bem cimentados (1,8-2,2). Esta observacao sugere:

1. **Cimentacao Moderada**: A rocha apresenta cimentacao intermediaria, nao sendo nem muito fraca nem muito forte
2. **Boa Conectividade Porosa**: Valores menores de **m** indicam melhor conectividade entre os poros, favoravel para fluxo de fluidos
3. **Possivel Sistema Poroso Misto**: Combinacao de porosidade intergranular e vugular ou fraturada
4. **Implicacoes para Reservatorios**: Caracteristicas favoraveis para armazenamento e producao de fluidos

Valores de **m** abaixo de 2,0 em carbonatos podem indicar a presenca de porosidade secundaria (vugs, fraturas) alem da porosidade primaria, o que aumenta a conectividade e reduz a tortuosidade efetiva dos caminhos de fluxo.

### 2.4 Implicacoes do R² Moderado

Um **R² = 0,4182** sugere uma correlacao moderada entre a resistividade aparente e a porosidade. Esse coeficiente indica que aproximadamente 41,8% da variabilidade da resistividade pode ser explicada pelo modelo de Archie, enquanto 58,2% e atribuivel a outros fatores.

**Fatores que Podem Contribuir para o R² Moderado:**

1. **Heterogeneidade Mineralogica**
   - Presenca de minerais condutores (argilas, pirita)
   - Variacao na composicao carbonatica (calcita vs dolomita)

2. **Variabilidade na Saturacao**
   - Saturacao parcial nao uniforme
   - Presenca de microambientes com diferentes graus de saturacao

3. **Textura e Fabrica da Rocha**
   - Diferentes tipos de poros (intergranular, vugular, fraturado)
   - Variacao na geometria e distribuicao dos poros

4. **Anisotropia**
   - Propriedades direcionais nao consideradas no modelo isotr opico
   - Estratificacao ou orientacao preferencial de estruturas

5. **Limitacoes do Modelo**
   - A Lei de Archie assume condicoes idealizadas
   - Nao considera efeitos de superficie e dupla camada eletrica

**Interpretacao Academica:**

O R² moderado nao invalida os resultados, mas sim reflete a complexidade natural das rochas carbonaticas. Esta observacao e consistente com a literatura geofisica, que reconhece que rochas carbonaticas frequentemente apresentam ajustes menos perfeitos ao modelo de Archie devido a sua heterogeneidade intrinseca.

Essa limitacao deve ser considerada ao interpretar os dados, e sugere que estudos complementares (petrofisica, petrografia) seriam beneficos para uma caracterizacao mais completa.

---

## 3. ANALISE GEOLOGICA DETALHADA DE CADA CASO SEV

### 3.1 Caso 1: Ambiente Geologico Homogeneo

**Parametros:**
- Resistividade: 493 - 2.904 Ω·m
- Media: 1.548 Ω·m
- Contraste: 5,9x
- Profundidade investigada: 100 m

**Analise Geologica:**

O contraste de resistividade de **5,9x** sugere uma variacao significativa entre as camadas de materiais, mas ainda moderada quando comparada ao Caso 2. Esse comportamento pode indicar a presenca de uma unidade geologica com caracteristicas heterogeneas, possivelmente associadas a depositos sedimentares ou variacoes de composicao mineral.

A media de resistividade relativamente alta (**1.548 Ω·m**) sugere a presenca de rochas com:
- **Menor porosidade** ou **menor saturacao de fluidos**
- Possivelmente rochas cristalinas, granitos ou arenitos compactos
- Baixo conteudo de argila ou minerais condutivos

**Interpretacao Estratigrafica:**

Com base na resistividade media elevada e no contraste moderado, o Caso 1 provavelmente representa:

1. **Sequencia Rochosa Relativamente Homogenea**
   - Possivelmente rocha cristalina (granito, gnaisse) em profundidade
   - Camada superficial de solo ou rocha alterada menos resistiva

2. **Estrutura Geologica Simples**
   - 2-3 camadas principais
   - Transicao gradual entre camadas

3. **Condicoes de Baixa Umidade**
   - Zona nao saturada ou zona de baixa permeabilidade
   - Ausencia de aquiferos significativos

**Aplicacoes Praticas:**
- Area com potencial limitado para recursos hidricos
- Fundacao rochosa solida para construcoes
- Baixo potencial para contaminacao de aquiferos

### 3.2 Caso 2: Ambiente Geologico Complexo (Multiplas Camadas)

**Parametros:**
- Resistividade: 247 - 8.350 Ω·m
- Media: 1.333 Ω·m
- Contraste: **33,8x** (MAIOR)
- Profundidade investigada: 100 m
- Caracteristica: Multiplas camadas distintas

**Analise Geologica:**

A presenca de multiplas camadas e um **contraste elevado de 33,8x** indica uma complexidade geologica significativa, possivelmente com alternancia de rochas mais e menos condutivas. Esta variacao pode estar relacionada a diferentes litologias ou a presenca de agua subterranea com diferentes salinidades.

**Interpretacao Estratigrafica Detalhada:**

1. **Camada Superficial (Condutiva - 247 Ω·m)**
   - Solo saturado ou areia umida
   - Alta porosidade e permeabilidade
   - Possivel aquifero livre ou zona de recarga

2. **Camada Intermediaria (Transicao)**
   - Variacao litologica progressiva
   - Possivel intercalacao de materiais
   - Zona de mistura de fluidos

3. **Camada Profunda (Resistiva - 8.350 Ω·m)**
   - Rocha cristalina ou granito solido
   - Baixissima porosidade
   - Embasamento rochoso impermeavel

**Significado Geologico:**

Este caso e crucial para entender a dinamica de fluidos no subsolo. O alto contraste sugere:

- **Descontinuidade Geologica Acentuada**: Possivel contato entre formacoes geologicas distintas
- **Presenca de Aquifero**: Camada condutiva superior indica zona saturada
- **Embasamento Cristalino**: Camada resistiva profunda funciona como barreira impermeavel
- **Variacoes Litologicas Significativas**: Alternancia de sedimentos e rochas cristalinas

**Implicacoes Hidrogeologicas:**

A configuracao deste caso e tipica de sistemas aquiferos suspensos sobre embasamento rochoso, com potencial para:
- Exploracao de agua subterranea na camada superior
- Contaminacao confinada a camada superior (protecao do embasamento)
- Fluxo horizontal de agua na interface sedimento-rocha

**Aplicacoes Praticas:**
- Area promissora para extracao de agua subterranea
- Necessidade de gerenciamento cuidadoso para evitar contaminacao
- Possivel zona de interesse para estudos hidrogeologicos detalhados

### 3.3 Caso 3: Ambiente Geologico Moderadamente Homogeneo

**Parametros:**
- Resistividade: 493 - 2.630 Ω·m
- Media: 1.316 Ω·m
- Contraste: 5,3x
- Profundidade investigada: 100 m

**Analise Geologica:**

Com um contraste de **5,3x**, este caso apresenta uma variacao de resistividade menor em comparacao ao Caso 2, indicando uma menor complexidade geologica. A media de resistividade sugere a presenca de rochas com caracteristicas semelhantes, possivelmente menos afetadas por fraturas ou variacoes litologicas acentuadas.

**Interpretacao Estratigrafica:**

O Caso 3 apresenta perfil similar ao Caso 1, com:

1. **Estrutura Geologica Relativamente Uniforme**
   - Variacao moderada entre camadas
   - Ausencia de descontinuidades abruptas
   - Transicoes graduais

2. **Caracteristicas Petrofisicas:**
   - Resistividade media-alta (1.316 Ω·m)
   - Compativel com rochas consolidadas
   - Baixa saturacao de fluidos ou baixa porosidade

3. **Possivel Sequencia Geologica:**
   - Solo ou rocha alterada superficial (menos resistivo)
   - Rocha consolidada em profundidade (mais resistivo)
   - Gradacao continua sem interfaces abruptas

**Comparacao com Caso 1:**

Ambos os casos apresentam contrastes similares (~5x), sugerindo ambientes geologicos comparaveis. A principal diferenca e a resistividade maxima ligeiramente menor no Caso 3, o que pode indicar:
- Maior grau de alteracao da rocha
- Presenca de maior umidade em profundidade
- Composicao mineralogica ligeiramente diferente

**Aplicacoes Praticas:**
- Similar ao Caso 1: baixo potencial hidrico
- Condicoes favoraveis para fundacoes
- Ambiente geologico previsivel e estavel

---

## 4. COMPARACAO ENTRE OS 3 CASOS SEV

### 4.1 Analise Comparativa Quantitativa

| **Parametro** | **Caso 1** | **Caso 2** | **Caso 3** |
|--------------|-----------|-----------|-----------|
| Rho Min (Ω·m) | 493 | **247** ← | 493 |
| Rho Max (Ω·m) | 2.904 | **8.350** ← | 2.630 |
| Rho Media (Ω·m) | **1.548** ← | 1.333 | 1.316 |
| Contraste | 5,9x | **33,8x** ← | 5,3x |
| Complexidade | Moderada | **Alta** | Moderada |

### 4.2 Interpretacao Geologica Comparativa

**Casos 1 e 3: Ambientes Similares**
- Apresentam perfis geologicos comparaveis
- Contrastes moderados (~5x)
- Estruturas relativamente homogeneas
- Provavelmente representam rochas cristalinas ou sedimentos consolidados
- Baixo potencial para recursos hidricos
- Estrutura geologica previsivel

**Caso 2: Ambiente Distinto e Complexo**
- Contraste 6x maior que os outros casos
- Estrutura geologica multicamadas
- Presenca provavel de aquifero
- Maior heterogeneidade litologica
- Ambiente geologicamente mais dinamico

### 4.3 Implicacoes para Exploracao e Uso do Solo

**Exploracao de Recursos Hidricos:**
- **Caso 2**: Mais promissor devido a camada condutiva superficial indicando zona saturada
- **Casos 1 e 3**: Menos favoraveis, resistividades altas indicam baixa disponibilidade de agua

**Construcao e Engenharia Civil:**
- **Casos 1 e 3**: Mais favoraveis, substratos estaveis e previsiveis
- **Caso 2**: Requer atencao especial devido a presenca de camadas moles saturadas

**Estudos Ambientais:**
- **Caso 2**: Maior vulnerabilidade a contaminacao na camada superior
- **Casos 1 e 3**: Menor permeabilidade reduz risco de dispersao de contaminantes

### 4.4 Modelos Geologicos Conceituais

**Modelo Caso 1/3:**
```
[0-20m]   Solo/Rocha Alterada (moderadamente resistivo)
[20-100m] Rocha Cristalina/Granito (altamente resistivo)
          → Transicao gradual
          → Estrutura homogenea
```

**Modelo Caso 2:**
```
[0-30m]   Aquifero/Sedimentos Saturados (condutivo - 247 Ω·m)
[30-60m]  Zona de Transicao (variavel)
[60-100m] Embasamento Cristalino (muito resistivo - 8.350 Ω·m)
          → Descontinuidades abruptas
          → Multiplas interfaces geologicas
```

---

## 5. DISCUSSAO SOBRE LIMITACOES DOS METODOS

### 5.1 Limitacoes da Lei de Archie

**Premissas Idealizadas:**

A Lei de Archie assume que a saturacao de agua e a porosidade sao as unicas variaveis influentes, desconsiderando:

1. **Presenca de Minerais Condutores**
   - Argilas: aumentam significativamente a condutividade
   - Pirita e outros sulfetos: alteram as medicoes de resistividade
   - Efeito nao capturado pelo modelo de Archie tradicional

2. **Heterogeneidade da Rocha**
   - Variacoes locais na textura e composicao
   - Presenca de fraturas e vugs
   - Anisotropia das propriedades eletricas

3. **Efeitos de Superficie**
   - Dupla camada eletrica nas interfaces poro-fluido
   - Conducao superficial em poros de pequeno diametro
   - Relevante especialmente em rochas argilosas

4. **Variaveis Nao Consideradas**
   - Temperatura: afeta a resistividade do fluido
   - Salinidade: variacoes no Rw nao sao capturadas no modelo simples
   - Pressao: pode afetar a geometria dos poros

**Aplicabilidade Limitada:**

O modelo de Archie foi desenvolvido originalmente para arenitos limpos e saturados. Sua aplicacao a carbonatos, que apresentam:
- Porosidade complexa (intergranular + vugular + fraturas)
- Forte heterogeneidade
- Variaveis graus de dolomitizacao

Pode resultar em ajustes imperfeitos (como o R² = 0,4182 obtido).

### 5.2 Limitacoes da Sondagem Eletrica Vertical (SEV)

**Limitacoes Tecnicas:**

1. **Configuracao dos Eletrodos**
   - Espacamento fixo pode nao detectar camadas finas
   - Arranjo Schlumberger assume simetria lateral
   - Dificuldade em terrenos irregulares

2. **Resolucao Vertical**
   - Camadas muito finas (< 1m) podem nao ser detectadas
   - Efeito de media volumetrica em camadas proximas
   - Perda de resolucao com o aumento da profundidade

3. **Pressupostos do Metodo**
   - Assume camadas horizontais e homogeneas lateralmente
   - Camadas inclinadas ou nao-horizontais causam distorcoes
   - Presenca de corpos 3D (ex: diques, lentes) nao e bem resolvida

**Limitacoes de Interpretacao:**

1. **Ambiguidade**
   - Diferentes modelos geologicos podem produzir curvas de resistividade similares
   - Principio da equivalencia: camadas com produtos resistividade × espessura similares sao indistinguiveis
   - Principio da supressao: camadas resistivas finas entre camadas condutivas sao dificilmente detectadas

2. **Influencia de Fatores Externos**
   - Variacoes de temperatura do solo
   - Umidade superficial variavel
   - Ruido eletromagnetico (linhas de transmissao, tempestades)

3. **Necessidade de Calibracao**
   - Dados de poco ou testemunhos sao ideais para calibrar interpretacoes
   - Sem dados diretos, interpretacao e nao-unica

### 5.3 Recomendacoes para Mitigar Limitacoes

1. **Integracao de Metodos**
   - Combinar SEV com sismica, gravimetria ou magnetometria
   - Usar dados de pocos para calibracao
   - Realizar levantamentos eletromagneticos complementares (TEM)

2. **Amostragem e Analises Complementares**
   - Analises petrofisicas de amostras (porosidade, permeabilidade)
   - Petrografia para caracterizacao mineralogica
   - Analises de fluidos (salinidade, composicao)

3. **Modelagem Avancada**
   - Inversao 2D/3D de dados SEV
   - Consideracao de anisotropia
   - Modelagem estocastica para incorporar incertezas

---

## 6. CONCLUSOES E RECOMENDACOES

### 6.1 Conclusoes Gerais

A analise dos metodos eletricos em geofisica, atraves da Lei de Archie e do SEV Schlumberger, revelou insights importantes sobre a estrutura e composicao das rochas carbonaticas saturadas e dos ambientes geologicos investigados.

**Principais Resultados:**

1. **Lei de Archie (Exercicio 1):**
   - Parametros obtidos (a=0,606, m=1,688) sao coerentes para rochas carbonaticas com cimentacao moderada
   - R² moderado (0,418) reflete a heterogeneidade natural dos carbonatos, comum na literatura
   - A rocha apresenta sistema poroso misto com boa conectividade, favoravel para fluxo de fluidos
   - Resultados consistentes com caracterizacao petrofisica esperada para carbonatos

2. **SEV Schlumberger (Exercicio 2):**
   - Identificadas diferencas significativas entre os 3 casos estudados
   - Caso 2 destaca-se pela maior complexidade geologica (contraste 33,8x), indicando estrutura multicamadas com potencial hidrogeologico
   - Casos 1 e 3 apresentam perfis similares, sugerindo ambientes geologicos comparaveis com menor heterogeneidade
   - Pseudosecoes geradas com sucesso permitiram visualizacao clara das variacoes de resistividade em profundidade

3. **Eficacia dos Metodos:**
   - Ambos os metodos demonstraram ser eficazes para caracterizacao geofisica
   - Lei de Archie forneceu parametros quantitativos para caracterizacao petrofisica
   - SEV permitiu identificacao de estruturas geologicas e camadas em subsuperficie ate 100m

### 6.2 Contribuicoes do Estudo

Este trabalho contribui para:

1. **Caracterizacao Petrofisica:** Parametros de Archie fornecem base para estimativas de porosidade e permeabilidade
2. **Interpretacao Estratigrafica:** SEV revelou diferentes ambientes deposicionais e estruturas geologicas
3. **Aplicacoes Praticas:** Resultados orientam decisoes sobre recursos hidricos, fundacoes e estudos ambientais

### 6.3 Recomendacoes para Trabalhos Futuros

**Recomendacoes Metodologicas:**

1. **Estudos Complementares**
   - Realizar analises petrofisicas de laboratorio para validar parametros de Archie
   - Executar perfis de poco para calibracao dos modelos SEV
   - Coletar amostras para caracterizacao mineralogica e textural

2. **Integracao de Dados**
   - Integrar resultados com outros metodos geofisicos (sismica, gravimetria)
   - Combinar com dados geologicos de superficie (mapeamento, afloramentos)
   - Incorporar dados hidrogeologicos (niveis de agua, testes de bombeamento)

3. **Modelagem Avancada**
   - Aplicar inversao 2D/3D dos dados de SEV para modelos mais realistas
   - Implementar modelagem estocastica para quantificar incertezas
   - Desenvolver modelos 3D integrados do subsolo

**Recomendacoes Especificas por Caso:**

**Para o Caso 2 (Alta Complexidade):**
- Investigacao detalhada do aquifero identificado
- Testes de bombeamento para caracterizacao hidrogeologica
- Monitoramento de qualidade da agua
- Estudo de vulnerabilidade a contaminacao

**Para os Casos 1 e 3 (Homogeneos):**
- Confirmacao da natureza do substrato rochoso resistivo
- Avaliacao de adequacao para fundacoes profundas
- Estudo de potencial geotecnico

### 6.4 Recomendacoes Praticas

**Para Gestores e Tomadores de Decisao:**

1. **Recursos Hidricos:**
   - Priorizar exploracao no Caso 2 devido ao potencial de aquifero
   - Casos 1 e 3 tem baixo potencial para extracao de agua subterranea

2. **Construcao Civil:**
   - Casos 1 e 3 apresentam condicoes favoraveis para fundacoes
   - Caso 2 requer atencao especial devido a camadas saturadas

3. **Gestao Ambiental:**
   - Caso 2 requer maior monitoramento devido a vulnerabilidade a contaminacao
   - Implementar zonas de protecao para aquifero identificado no Caso 2

### 6.5 Consideracoes Finais

Os parametros obtidos oferecem informacoes valiosas, mas a interpretacao deve ser feita com cautela, considerando as limitacoes e variaveis envolvidas. A Lei de Archie, apesar de suas simplificacoes, permanece uma ferramenta fundamental para caracterizacao petrofisica, especialmente quando complementada com outras tecnicas.

O metodo SEV Schlumberger demonstrou ser eficaz para identificacao de estruturas geologicas e variacoes de resistividade em subsuperficie, sendo particularmente util para estudos hidrogeologicos e de caracterizacao do subsolo raso.

A integracao de dados de diferentes metodos geofisicos, combinada com informacoes geologicas e hidrogeologicas, pode proporcionar uma compreensao mais holistica das caracteristicas geologicas da area em estudo, reduzindo ambiguidades e aumentando a confiabilidade das interpretacoes.

---

## REFERENCIAS BIBLIOGRAFICAS

1. Archie, G.E. (1942). "The Electrical Resistivity Log as an Aid in Determining Some Reservoir Characteristics". Transactions of the AIME, 146, 54-62.

2. Telford, W.M., Geldart, L.P., Sheriff, R.E. (1990). "Applied Geophysics". Cambridge University Press, 2nd Edition.

3. Kearey, P., Brooks, M., Hill, I. (2002). "An Introduction to Geophysical Exploration". Blackwell Science, 3rd Edition.

4. Reynolds, J.M. (2011). "An Introduction to Applied and Environmental Geophysics". John Wiley & Sons, 2nd Edition.

5. Koefoed, O. (1979). "Geosounding Principles, 1: Resistivity Sounding Measurements". Elsevier Scientific Publishing Company.

6. Tiab, D., Donaldson, E.C. (2015). "Petrophysics: Theory and Practice of Measuring Reservoir Rock and Fluid Transport Properties". Gulf Professional Publishing, 4th Edition.

7. Loke, M.H. (2000). "Electrical Imaging Surveys for Environmental and Engineering Studies: A Practical Guide to 2-D and 3-D Surveys". Penang, Malaysia.

8. Sharma, P.V. (1997). "Environmental and Engineering Geophysics". Cambridge University Press.

---

**Documento preparado em:** 13 de Outubro de 2025
**Software utilizado:** Python 3.14.0 (NumPy, Pandas, Matplotlib, SciPy)

---

## APENDICE: DADOS TECNICOS DO PROCESSAMENTO

### Especificacoes Computacionais
- **Linguagem:** Python 3.14.0
- **Bibliotecas:** NumPy 2.3.3, Pandas 2.3.3, Matplotlib 3.10.7, SciPy 1.16.2
- **Metodo de Regressao:** Minimos quadrados (scipy.stats.linregress)
- **Interpolacao SEV:** Interpolacao cubica (scipy.interpolate.griddata)
- **Resolucao de Graficos:** 300 DPI

### Parametros de Processamento
- **Exercicio 1:** 13 amostras analisadas
- **Exercicio 2:** 228 medicoes totais (76 por caso, 3 casos)
- **Profundidade investigada:** 0-100 metros
- **Pseudo-profundidade calculada:** AB/3

### Controle de Qualidade
- Scripts validados e testados
- Resultados reprodutiveis
- Documentacao completa mantida
- Formato de dados: CSV (separador ";", decimal ",")
