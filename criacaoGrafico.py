 # --- algoritimo para criar o gráfico de uma função  ( cos(x) - x^3 )--- #
 # --- Lucas Souza - Equipe 1 --- #

import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def f(x):
    return np.cos(x) - x**3

# criando um intervalo de valores para x
x = np.linspace(-2, 2, 100)
y = f(x)

# criando o gráfico
plt.figure(figsize = (10, 10))
plt.plot(x, y, label = 'f(x) = cos(x) - x^3')
plt.axhline(0, color='red', linestyle='-', linewidth=0.7) # linha horizontal em y = 0
plt.axvline(0, color='red', linestyle='-', linewidth=0.7) # linha vertical x = 0
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafico de f(x)')
plt.legend() # legenda do eixo
plt.grid(True)
plt.show()