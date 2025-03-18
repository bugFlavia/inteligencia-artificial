import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

preco_distribuicao_nova_andradina = [4.89, 5.08, 5.27, 5.19, 5.12, 5.06, 5.02, 5.17, 5.22, 5.24]
preco_revenda_nova_andradina = [5.87, 6.08, 6.21, 6.22, 6.19, 6.17, 6.10, 6.03, 6.09, 6.10]

# Criar o DataFrame
df = pd.DataFrame({
    'Preço Distribuição (R$)': preco_distribuicao_nova_andradina,
    'Preço Revenda (R$)': preco_revenda_nova_andradina
})

# Calcular a regressão linear
slope, intercept, r_value, p_value, std_err = linregress(preco_distribuicao_nova_andradina, preco_revenda_nova_andradina)

# Gerar os valores da linha de tendência
x = np.array(preco_distribuicao_nova_andradina)
y_tendencia = slope * x + intercept

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(preco_distribuicao_nova_andradina, preco_revenda_nova_andradina, color='blue', label='Dados Observados')
plt.plot(x, y_tendencia, color='red', label='Linha de Tendência')

# Adicionar a equação da linha de tendência ao gráfico
plt.text(min(x) + 0.1, max(preco_revenda_nova_andradina) - 0.1, f'y = {slope:.4f}x + {intercept:.4f}', fontsize=12, color='red')

# Personalizar o gráfico
plt.title('Regressão Linear entre Preço Distribuição e Preço Revenda')
plt.xlabel('Preço Distribuição (R$)')
plt.ylabel('Preço Revenda (R$)')
plt.legend()
plt.grid(True)
plt.show()

# Calcular a correlação
correlacao = df.corr()

# Exibir os resultados
print(f'Correlação entre Preço Distribuição e Preço Revenda: \n{correlacao}\n')
print(f'Coeficiente angular (slope): {slope}')
print(f'Intercepto (intercept): {intercept}')
print(f'Coeficiente de determinação (R²): {r_value**2}')
