# -*- coding: utf-8 -*-
"""
Exercicio 1 - Equacao de Archie
Analise de porosidade e resistividade de rochas carbonaticas
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Backend nao-interativo
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Configuracoes
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# Carregar dados
dados = pd.read_csv(r'C:\projetos\Exercicio Computacional\dataset_archie\dados_porosidade_resistividade.csv')
print("Dados carregados:")
print(dados.head())
print(f"\nTotal de amostras: {len(dados)}")

# Extrair variaveis
phi = dados['Phi'].values          # Porosidade
Rt = dados['Rt'].values            # Resistividade da rocha saturada (ohm.m)
Rw = dados['Rw'].values[0]         # Resistividade do fluido (constante)

print(f"\nResistividade do fluido (Rw): {Rw} ohm.m")

# Calcular Rt/Rw
Rt_Rw = Rt / Rw

# Equacao de Archie: Rt/Rw = a * phi^(-m)
# Linearizando: log(Rt/Rw) = log(a) - m*log(phi)

log_phi = np.log(phi)
log_Rt_Rw = np.log(Rt_Rw)

# Regressao linear nos dados logaritmicos
slope, intercept, r_value, p_value, std_err = stats.linregress(log_phi, log_Rt_Rw)

# Coeficientes da equacao de Archie
m = -slope              # Expoente de cimentacao
a = np.exp(intercept)   # Fator de tortuosidade

print("\n" + "="*60)
print("RESULTADOS DA REGRESSAO - EQUACAO DE ARCHIE")
print("="*60)
print(f"Fator de tortuosidade (a): {a:.4f}")
print(f"Expoente de cimentacao (m): {m:.4f}")
print(f"Coeficiente de correlacao (R^2): {r_value**2:.4f}")
print(f"Erro padrao: {std_err:.4f}")
print("="*60)

# Funcao de Archie para plotagem
def archie(phi_val, a_val, m_val):
    return a_val * phi_val**(-m_val)

# Gerar curva ajustada
phi_fit = np.linspace(phi.min(), phi.max(), 100)
Rt_Rw_fit = archie(phi_fit, a, m)

# Criar grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Grafico 1: Escala linear
ax1.scatter(phi, Rt_Rw, color='blue', s=50, alpha=0.6, edgecolors='black', label='Dados medidos')
ax1.plot(phi_fit, Rt_Rw_fit, 'r-', linewidth=2, label=f'Ajuste: a={a:.3f}, m={m:.3f}')
ax1.set_xlabel('Porosidade (phi)', fontsize=12)
ax1.set_ylabel('Rt/Rw', fontsize=12)
ax1.set_title('Equacao de Archie - Escala Linear', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()

# Grafico 2: Escala log-log
ax2.scatter(phi, Rt_Rw, color='blue', s=50, alpha=0.6, edgecolors='black', label='Dados medidos')
ax2.plot(phi_fit, Rt_Rw_fit, 'r-', linewidth=2, label=f'Ajuste: a={a:.3f}, m={m:.3f}')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel('Porosidade (phi)', fontsize=12)
ax2.set_ylabel('Rt/Rw', fontsize=12)
ax2.set_title('Equacao de Archie - Escala Log-Log', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3, which='both')
ax2.legend()

plt.tight_layout()
plt.savefig(r'C:\projetos\Exercicio Computacional\exercicio1_archie_grafico.png', dpi=300, bbox_inches='tight')
print("\nGrafico salvo: exercicio1_archie_grafico.png")
plt.close()

# Interpretacao dos resultados
print("\n" + "="*60)
print("INTERPRETACAO DOS RESULTADOS")
print("="*60)

print(f"\n1. FATOR DE TORTUOSIDADE (a = {a:.4f}):")
if a < 0.6:
    print("   - Valor baixo: indica alta tortuosidade dos poros")
    print("   - Caminhos tortuosos dificultam o fluxo de corrente eletrica")
elif 0.6 <= a < 1.0:
    print("   - Valor moderado: tortuosidade tipica de rochas carbonaticas")
    print("   - Poros com alguma conectividade, mas ainda tortuosos")
elif 1.0 <= a < 1.5:
    print("   - Valor alto: baixa tortuosidade")
    print("   - Poros bem conectados, caminhos mais diretos")
else:
    print("   - Valor muito alto: pode indicar fraturas ou poros muito conectados")

print(f"\n2. EXPOENTE DE CIMENTACAO (m = {m:.4f}):")
if m < 1.3:
    print("   - Valor baixo: pouca consolidacao")
    print("   - Possivel presencia de fraturas ou poros mal consolidados")
elif 1.3 <= m < 1.8:
    print("   - Valor tipico para areias nao consolidadas")
    print("   - Cimentacao fraca a moderada")
elif 1.8 <= m < 2.0:
    print("   - Valor comum para rochas carbonaticas bem cimentadas")
    print("   - Boa consolidacao da rocha")
elif 2.0 <= m < 2.5:
    print("   - Valor alto: forte cimentacao")
    print("   - Rochas carbonaticas compactas e bem cimentadas")
else:
    print("   - Valor muito alto: cimentacao extrema ou matriz muito densa")

print("\n3. TIPO DE ROCHA PROVAVEL:")
if 1.8 <= m <= 2.2 and 0.6 <= a <= 1.0:
    print("   - CARBONATO CIMENTADO (calcario ou dolomito)")
    print("   - Caracteristicas: boa cimentacao, porosidade intergranular")
elif m > 2.0 and a < 0.8:
    print("   - CARBONATO COMPACTO")
    print("   - Caracteristicas: alta cimentacao, poros tortuosos")
elif m < 1.8 and a > 1.0:
    print("   - CARBONATO FRATURADO OU VUGULAR")
    print("   - Caracteristicas: presenca de fraturas ou vugs aumentando conectividade")
else:
    print("   - CARBONATO COM CARACTERISTICAS MISTAS")
    print("   - Analise adicional recomendada")

print(f"\n4. QUALIDADE DO AJUSTE (R^2 = {r_value**2:.4f}):")
if r_value**2 > 0.9:
    print("   - Excelente ajuste: o modelo de Archie representa bem os dados")
elif r_value**2 > 0.7:
    print("   - Bom ajuste: modelo adequado com alguma variabilidade")
else:
    print("   - Ajuste moderado: pode haver heterogeneidades na rocha")

print("="*60)

# Salvar resultados em CSV
resultados = pd.DataFrame({
    'Porosidade': phi,
    'Rt (ohm.m)': Rt,
    'Rt/Rw': Rt_Rw,
    'Rt/Rw_predito': archie(phi, a, m),
    'Residuo': Rt_Rw - archie(phi, a, m)
})

resultados.to_csv(r'C:\projetos\Exercicio Computacional\exercicio1_archie_resultados.csv',
                  sep=';', decimal=',', index=False)
print("\nResultados salvos: exercicio1_archie_resultados.csv")

# Salvar parametros
with open(r'C:\projetos\Exercicio Computacional\exercicio1_archie_parametros.txt', 'w', encoding='utf-8') as f:
    f.write("PARAMETROS DA EQUACAO DE ARCHIE\n")
    f.write("="*50 + "\n\n")
    f.write(f"Fator de tortuosidade (a): {a:.4f}\n")
    f.write(f"Expoente de cimentacao (m): {m:.4f}\n")
    f.write(f"Coeficiente de correlacao (R^2): {r_value**2:.4f}\n")
    f.write(f"Erro padrao: {std_err:.4f}\n")
    f.write(f"\nEquacao ajustada: Rt/Rw = {a:.4f} * phi^(-{m:.4f})\n")

print("Parametros salvos: exercicio1_archie_parametros.txt")
print("\nExercicio 1 concluido com sucesso!")
