# -*- coding: utf-8 -*-
"""
Exercicio 2 - Sondagem Eletrica Vertical (SEV)
Analise de resistividade aparente com arranjo Schlumberger
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend nao-interativo
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import pandas as pd
import os

# Configuracoes
plt.rcParams['font.size'] = 11

def read_schlumberger(file_path, line_id, spacing_between_lines=50):
    """
    Le dados de SEV Schlumberger e constroi coordenadas para pseudosecao.

    file_path : caminho do arquivo (.dat)
    line_id : numero da linha SE-x
    spacing_between_lines : deslocamento entre linhas no eixo X (m)
    """
    data = np.loadtxt(file_path)
    AB2 = data[:, 0]   # coluna 1 -> AB/2
    MN2 = data[:, 1]   # coluna 2 -> MN/2
    rho_a = data[:, 2] # coluna 3 -> resistividade aparente

    # Centro do arranjo (posicao lateral)
    x_center = np.ones_like(AB2) * line_id * spacing_between_lines

    # Pseudo-profundidade empirica (aprox. AB/3)
    z = AB2 / 3

    return x_center, z, rho_a, AB2, MN2

def processar_caso(caso_nome, pasta_base):
    """
    Processa um caso completo de SEV (3 linhas de sondagem)
    """
    print("\n" + "="*70)
    print(f"PROCESSANDO {caso_nome.upper()}")
    print("="*70)

    # Caminhos dos arquivos
    files = [
        (f"{pasta_base}/{caso_nome}/SE-01.dat", 1),
        (f"{pasta_base}/{caso_nome}/SE-02.dat", 2),
        (f"{pasta_base}/{caso_nome}/SE-03.dat", 3)
    ]

    # Agrupa dados de todas as linhas
    X, Z, RHO = [], [], []
    todos_dados = []

    for file_path, idx in files:
        x, z, rho, ab2, mn2 = read_schlumberger(file_path, idx)
        X.extend(x)
        Z.extend(z)
        RHO.extend(rho)

        # Armazenar dados para analise
        for i in range(len(ab2)):
            todos_dados.append({
                'Linha': f'SE-{idx:02d}',
                'AB/2 (m)': ab2[i],
                'MN/2 (m)': mn2[i],
                'Rho_aparente (ohm.m)': rho[i],
                'Posicao_X (m)': x[i],
                'Pseudo-profundidade (m)': z[i]
            })

    X, Z, RHO = np.array(X), np.array(Z), np.array(RHO)

    # Estatisticas
    print(f"\nTotal de medicoes: {len(RHO)}")
    print(f"Resistividade aparente - Min: {RHO.min():.2f} ohm.m")
    print(f"Resistividade aparente - Max: {RHO.max():.2f} ohm.m")
    print(f"Resistividade aparente - Media: {RHO.mean():.2f} ohm.m")
    print(f"Profundidade maxima investigada: {Z.max():.2f} m")

    # Salvar dados em CSV
    df_dados = pd.DataFrame(todos_dados)
    arquivo_csv = f'C:\\projetos\\Exercicio Computacional\\exercicio2_SEV_{caso_nome}_dados.csv'
    df_dados.to_csv(arquivo_csv, sep=';', decimal=',', index=False)
    print(f"\nDados salvos: exercicio2_SEV_{caso_nome}_dados.csv")

    # Interpolacao para o grid
    xi = np.linspace(min(X), max(X), 300)
    zi = np.linspace(min(Z), max(Z), 300)
    Xi, Zi = np.meshgrid(xi, zi)
    Ri = griddata((X, Z), RHO, (Xi, Zi), method='cubic')

    # Criar figura com pseudosecao e curvas de resistividade
    fig = plt.figure(figsize=(16, 10))

    # Pseudosecao
    ax1 = plt.subplot(2, 2, (1, 3))
    levels = np.linspace(RHO.min(), RHO.max(), 20)
    contour = ax1.contourf(Xi, Zi, Ri, levels=levels, cmap='jet', extend='both')
    scatter = ax1.scatter(X, Z, c=RHO, edgecolor='k', cmap='jet', s=40,
                         vmin=RHO.min(), vmax=RHO.max())
    cbar = plt.colorbar(contour, ax=ax1, label='Resistividade Aparente (ohm.m)')
    ax1.invert_yaxis()
    ax1.set_xlabel('Posicao da Linha (m)', fontsize=12)
    ax1.set_ylabel('Pseudo-profundidade (m)', fontsize=12)
    ax1.set_title(f'Pseudosecao de Resistividade Aparente - {caso_nome.upper()}\\nArranjo Schlumberger',
                  fontsize=14, fontweight='bold')
    ax1.grid(alpha=0.3)

    # Curvas de resistividade por linha (escala log-log)
    ax2 = plt.subplot(2, 2, 2)
    for file_path, idx in files:
        x, z, rho, ab2, mn2 = read_schlumberger(file_path, idx)
        ax2.loglog(ab2, rho, 'o-', label=f'Linha SE-{idx:02d}', markersize=6, linewidth=2)
    ax2.set_xlabel('AB/2 (m)', fontsize=11)
    ax2.set_ylabel('Resistividade Aparente (ohm.m)', fontsize=11)
    ax2.set_title('Curvas de Resistividade (Log-Log)', fontsize=12, fontweight='bold')
    ax2.grid(True, which='both', alpha=0.3)
    ax2.legend()

    # Histograma de resistividade
    ax3 = plt.subplot(2, 2, 4)
    ax3.hist(RHO, bins=15, color='steelblue', edgecolor='black', alpha=0.7)
    ax3.axvline(RHO.mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {RHO.mean():.1f}')
    ax3.set_xlabel('Resistividade Aparente (ohm.m)', fontsize=11)
    ax3.set_ylabel('Frequencia', fontsize=11)
    ax3.set_title('Distribuicao de Resistividade', fontsize=12, fontweight='bold')
    ax3.legend()
    ax3.grid(alpha=0.3)

    plt.tight_layout()
    arquivo_png = f'C:\\projetos\\Exercicio Computacional\\exercicio2_SEV_{caso_nome}_analise.png'
    plt.savefig(arquivo_png, dpi=300, bbox_inches='tight')
    print(f"Grafico salvo: exercicio2_SEV_{caso_nome}_analise.png")
    plt.close()

    return RHO, Z, X

def interpretar_resistividade(caso_nome, rho_min, rho_max, rho_media):
    """
    Interpreta os valores de resistividade e identifica possiveis materiais
    """
    print("\n" + "-"*70)
    print(f"INTERPRETACAO GEOLOGICA - {caso_nome.upper()}")
    print("-"*70)

    # Faixas de resistividade tipicas (ohm.m)
    interpretacoes = []

    if rho_min < 10:
        interpretacoes.append("- Resistividade muito baixa (< 10 ohm.m): possivel presenca de ARGILA, SOLO SATURADO ou AGUA SALOBRA")

    if rho_min < 50 and rho_max > 10:
        interpretacoes.append("- Resistividade baixa (10-50 ohm.m): provavel ARGILA UMIDA, SILTE ou SOLO COM ALTA SATURACAO")

    if rho_media >= 50 and rho_media < 200:
        interpretacoes.append("- Resistividade moderada (50-200 ohm.m): compativel com AREIA UMIDA, ARENITO ou CALCARIO FRATURADO")

    if rho_media >= 200 and rho_media < 1000:
        interpretacoes.append("- Resistividade alta (200-1000 ohm.m): compativel com AREIA SECA, ARENITO COMPACTO ou ROCHA SEDIMENTAR")

    if rho_max >= 1000:
        interpretacoes.append("- Resistividade muito alta (> 1000 ohm.m): possivel ROCHA CRISTALINA, GRANITO ou AREIA MUITO SECA")

    print("\nFaixas de resistividade detectadas:")
    for interp in interpretacoes:
        print(interp)

    # Analise de camadas
    print("\nANALISE DE CAMADAS:")
    razao = rho_max / rho_min
    if razao > 10:
        print(f"- Alto contraste de resistividade (razao: {razao:.1f}x)")
        print("- Indica presenca de MULTIPLAS CAMADAS com propriedades distintas")
        print("- Possivel sequencia: camada superficial condutiva -> camada profunda resistiva")
    elif razao > 3:
        print(f"- Contraste moderado de resistividade (razao: {razao:.1f}x)")
        print("- Provavel presenca de 2-3 camadas distintas")
    else:
        print(f"- Baixo contraste de resistividade (razao: {razao:.1f}x)")
        print("- Material relativamente homogeneo")

    print("-"*70)

# Script principal
def main():
    pasta_base = r'C:\projetos\Exercicio Computacional\dataset_SEV'
    casos = ['caso1', 'caso2', 'caso3']

    print("="*70)
    print("EXERCICIO 2 - SONDAGEM ELETRICA VERTICAL (SEV)")
    print("Arranjo Schlumberger")
    print("="*70)

    resultados_comparacao = []

    for caso in casos:
        RHO, Z, X = processar_caso(caso, pasta_base)
        interpretar_resistividade(caso, RHO.min(), RHO.max(), RHO.mean())

        resultados_comparacao.append({
            'Caso': caso,
            'Rho_min (ohm.m)': RHO.min(),
            'Rho_max (ohm.m)': RHO.max(),
            'Rho_media (ohm.m)': RHO.mean(),
            'Prof_max (m)': Z.max(),
            'Num_medicoes': len(RHO)
        })

    # Comparacao entre casos
    print("\n" + "="*70)
    print("COMPARACAO ENTRE OS 3 CASOS")
    print("="*70)

    df_comp = pd.DataFrame(resultados_comparacao)
    print("\n", df_comp.to_string(index=False))

    # Salvar comparacao
    df_comp.to_csv(r'C:\projetos\Exercicio Computacional\exercicio2_SEV_comparacao_casos.csv',
                   sep=';', decimal=',', index=False)
    print("\nComparacao salva: exercicio2_SEV_comparacao_casos.csv")

    # Grafico comparativo
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for idx, caso in enumerate(casos):
        pasta_base = r'C:\projetos\Exercicio Computacional\dataset_SEV'
        files = [
            (f"{pasta_base}/{caso}/SE-01.dat", 1),
            (f"{pasta_base}/{caso}/SE-02.dat", 2),
            (f"{pasta_base}/{caso}/SE-03.dat", 3)
        ]

        for file_path, line_id in files:
            x, z, rho, ab2, mn2 = read_schlumberger(file_path, line_id)
            axes[idx].loglog(ab2, rho, 'o-', label=f'SE-{line_id:02d}', markersize=5, linewidth=1.5)

        axes[idx].set_xlabel('AB/2 (m)', fontsize=11)
        axes[idx].set_ylabel('Resistividade Aparente (ohm.m)', fontsize=11)
        axes[idx].set_title(f'{caso.upper()}', fontsize=12, fontweight='bold')
        axes[idx].grid(True, which='both', alpha=0.3)
        axes[idx].legend(fontsize=9)

    plt.suptitle('Comparacao das Curvas de Resistividade - 3 Casos', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(r'C:\projetos\Exercicio Computacional\exercicio2_SEV_comparacao_geral.png',
                dpi=300, bbox_inches='tight')
    print("Grafico comparativo salvo: exercicio2_SEV_comparacao_geral.png")
    plt.close()

    print("\n" + "="*70)
    print("EXERCICIO 2 CONCLUIDO COM SUCESSO!")
    print("="*70)

if __name__ == '__main__':
    main()
