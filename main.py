import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Dados para Nova Andradina
preco_distribuicao_nova_andradina = [4.89, 5.08, 5.27, 5.19, 5.12, 5.06, 5.02, 5.17, 5.22, 5.24]
preco_revenda_nova_andradina = [5.87, 6.08, 6.21, 6.22, 6.19, 6.17, 6.10, 6.03, 6.09, 6.10]

# Calcular a regressão linear para Nova Andradina
slope_na, intercept_na, r_value_na, _, _ = linregress(preco_distribuicao_nova_andradina, preco_revenda_nova_andradina)
correlacao_na = np.corrcoef(preco_distribuicao_nova_andradina, preco_revenda_nova_andradina)

# Exibir resultados no console para Nova Andradina
print("Resultados para Nova Andradina:")
print(f"Correlação:\n{correlacao_na}")
print(f"Coeficiente angular (slope): {slope_na}")
print(f"Intercepto (intercept): {intercept_na}")
print(f"Coeficiente de determinação (R²): {r_value_na**2}\n")

# Dados para Ponta Porã
preco_distribuicao_ponta_pora = [4.92, 5.09, 5.29, 5.21, 5.10, 5.05, 5.03, 5.22, 5.28, 5.29]
preco_revenda_ponta_pora = [5.66, 5.89, 6.08, 6.05, 5.92, 5.84, 5.80, 5.90, 5.99, 6.00]

# Calcular a regressão linear para Ponta Porã
slope_pp, intercept_pp, r_value_pp, _, _ = linregress(preco_distribuicao_ponta_pora, preco_revenda_ponta_pora)
correlacao_pp = np.corrcoef(preco_distribuicao_ponta_pora, preco_revenda_ponta_pora)

# Exibir resultados no console para Ponta Porã
print("Resultados para Ponta Porã:")
print(f"Correlação:\n{correlacao_pp}")
print(f"Coeficiente angular (slope): {slope_pp}")
print(f"Intercepto (intercept): {intercept_pp}")
print(f"Coeficiente de determinação (R²): {r_value_pp**2}\n")

# Gráfico para Nova Andradina
x_na = np.array(preco_distribuicao_nova_andradina)
y_tendencia_na = slope_na * x_na + intercept_na

plt.figure(figsize=(10, 6))
plt.scatter(preco_distribuicao_nova_andradina, preco_revenda_nova_andradina, color='blue', label='Dados Observados')
plt.plot(x_na, y_tendencia_na, color='red', label='Linha de Tendência')
plt.text(min(x_na) + 0.1, max(preco_revenda_nova_andradina) - 0.1, f'y = {slope_na:.4f}x + {intercept_na:.4f}', fontsize=12, color='red')
plt.title('Regressão Linear entre Preço Distribuição e Preço Revenda Nova Andradina')
plt.xlabel('Preço Distribuição (R$)')
plt.ylabel('Preço Revenda (R$)')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico para Ponta Porã
x_pp = np.array(preco_distribuicao_ponta_pora)
y_tendencia_pp = slope_pp * x_pp + intercept_pp

plt.figure(figsize=(10, 6))
plt.scatter(preco_distribuicao_ponta_pora, preco_revenda_ponta_pora, color='green', label='Dados Observados')
plt.plot(x_pp, y_tendencia_pp, color='orange', label='Linha de Tendência')
plt.text(min(x_pp) + 0.1, max(preco_revenda_ponta_pora) - 0.1, f'y = {slope_pp:.4f}x + {intercept_pp:.4f}', fontsize=12, color='orange')
plt.title('Regressão Linear entre Preço Distribuição e Preço Revenda Ponta Porã')
plt.xlabel('Preço Distribuição (R$)')
plt.ylabel('Preço Revenda (R$)')
plt.legend()
plt.grid(True)
plt.show()
