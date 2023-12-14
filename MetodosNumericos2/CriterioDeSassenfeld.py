 # --- Critério de convergência do método de Gauss-Seidel --- #
 

import math
import numpy as np

# Coeficientes do sistema em uma matriz
A = np.array([[3, 1, -0.4, -0.9],
              [0.1, 4.9, -0.2, -0.6],
              [-0.1, -0.4, 2, 0.3],
              [1, 1.6, 0.4, 5.5]])

def criterioSassenfeld(A):
  coef = []
  for i in range(len(A)):
    somaCoef = 0
    for j in range(len(A)):
      if(i != j and i == 0) or i < j:
        somaCoef += A[i][j]
      elif i != j and i != 0:
        somaCoef+= A[i][j] * coef[j]
    somaCoef /= A[i][j]
    coef.append(somaCoef)

  print(coef)
  print()
  maiorCoef = max(coef)
  if maiorCoef < 1:
    print("O método ira convergir paara esse sistema !")
  else:
    print("Convergência não garantida para esse sistema !!")

criterioSassenfeld(A)