# Trabalho Computacional - Métodos Elétricos em Geofísica

Trabalho da disciplina de Métodos Geofísicos - 2025

## Sobre o Projeto

Este trabalho apresenta a aplicação computacional de métodos elétricos em geofísica, focando em dois exercícios principais:

1. **Exercício 1 - Lei de Archie**: Análise de parâmetros petrofísicos de rochas carbonáticas saturadas
2. **Exercício 2 - Sondagem Elétrica Vertical (SEV)**: Investigação de subsuperfície usando arranjo Schlumberger

## Estrutura dos Arquivos

```
.
├── Exercicio1_Archie/           Resultados da Lei de Archie
├── Exercicio2_SEV/              Resultados das sondagens elétricas
├── Scripts/                     Códigos Python utilizados
└── Documentacao/                Relatórios e análises detalhadas
```

## Resultados Principais

### Exercício 1 - Lei de Archie

Foram analisadas 13 amostras de rochas carbonáticas. Os parâmetros estimados foram:

- Fator de tortuosidade (a): 0,6063
- Expoente de cimentação (m): 1,6883
- Coeficiente de correlação (R²): 0,4182

### Exercício 2 - SEV Schlumberger

Três casos foram investigados até 100 metros de profundidade:

| Caso | Resistividade Média (Ω·m) | Contraste |
|------|---------------------------|-----------|
| 1    | 1.548                     | 5,9x      |
| 2    | 1.333                     | 33,8x     |
| 3    | 1.316                     | 5,3x      |

O Caso 2 apresentou maior complexidade geológica, indicando presença de múltiplas camadas.

## Documentação

- **ANALISE_DETALHADA.md**: Discussão aprofundada dos métodos e resultados
- **Documentacao/RELATORIO_COMPLETO.md**: Relatório técnico detalhado
- **Documentacao/REVISAO_TECNICA.md**: Revisão crítica dos resultados

## Como Executar os Scripts

### Requisitos

- Python 3.14 ou superior
- Bibliotecas: NumPy, Pandas, Matplotlib, SciPy

### Instalação das Dependências

```bash
pip install numpy pandas matplotlib scipy
```

### Execução

```bash
python Scripts/exercicio1_archie.py
python Scripts/exercicio2_SEV.py
```

## Formato dos Dados

Os arquivos CSV utilizam:
- Separador: ponto e vírgula (;)
- Decimal: vírgula (,)

## Metodologia

**Exercício 1**: Regressão linear em escala logarítmica para estimativa dos parâmetros da equação de Archie.

**Exercício 2**: Interpolação cúbica dos dados de resistividade para geração de pseudoseções e análise de camadas.

## Referências

- Archie, G.E. (1942). The Electrical Resistivity Log as an Aid in Determining Some Reservoir Characteristics
- Telford, W.M. et al. (1990). Applied Geophysics
- Reynolds, J.M. (2011). An Introduction to Applied and Environmental Geophysics

---

Data de conclusão: Outubro de 2025
