# --- Critério de convergência do método Gauss-Jacobi --- #



import math
import numpy as np

# Coeficientes do sistema em uma matriz
A = np.array([[3, 1, -0.4, -0.9],
              [0.1, 4.9, -0.2, -0.6],
              [-0.1, -0.4, 2, 0.3],
              [1, 1.6, 0.4, 5.5]])

def criterioJacobi(A):
  coef = []
  for i in range(len(A)):
    somaCoef = 0
    for j in range(len(A)):
      if i != j:
        somaCoef += math.fabs(A[i][j])
    somaCoef /= math.fabs(A[i][i])
    coef.append(somaCoef)
  print('Coeficientes:')
  print(coef)
  maiorCoef = max(coef)

  if maiorCoef < 1:
      print("O método vai convergir para esse sistema !!")
  else:
      print("Convergência não garantida para esse sistema !!")

criterioJacobi(A)