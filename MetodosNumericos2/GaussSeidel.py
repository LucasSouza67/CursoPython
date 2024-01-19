# --- Método de Gauss-Seidel --- #


import math
import numpy as np
import matplotlib.pyplot as plt

# Coeficientes do sistema em uma matriz
A = np.array([[3, 1, -0.4, -0.9],
              [0.1, 4.9, -0.2, -0.6],
              [-0.1, -0.4, 2, 0.3],
              [1, 1.6, 0.4, 5.5]])

b = np.array([0.9, -6.7, 5, -1])
vetSolu = np.zeros(len(b))

def gausSeidel(A, b, vetSolu, erro, iteracoes = 100):
  iteracao = 0
  grafico = []
  erro_atual = 0

  for k in range(iteracoes):
    for i in range(len(A)):
      x = b[i]
      for j in range(len(A)):
        if i != j:
          x -= A[i][j] * vetSolu[j]
      x /= A[i][i]
      vetSolu[i] = x
    iteracao +=1

    # Adiciona vetor de erro ao gráfico
    grafico.append(np.linalg.norm(np.dot(A, vetSolu) - b))

    erro_atual = np.linalg.norm(np.dot(A, vetSolu) - b)
    if erro_atual < erro:
      print('Convergência alcançada com {} iterações\n'.format(iteracao))
      break
    if iteracao >= iteracoes:
      print("Método não convergiu no número de iterações espereado")
      break

  plt.plot(range(1, iteracao + 1), grafico, linestyle='-', color='r')
  plt.xlabel('Número de Iterações')
  plt.ylabel('Erro')
  plt.title('Convergência das Iterações')
  plt.grid(True)
  plt.show()

  return vetSolu

erro = 0.001
solucao = gausSeidel(A, b, vetSolu, erro, iteracoes = 100)

print('\nSolução encontarda com o erro de {}: '.format(erro))
print(solucao)
print('\nA solução exata é: \n', np.linalg.inv(A)@b)