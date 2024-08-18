"""Diferencia de las diagonales de una matríz

Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 9 + 5 + 3 = 17. Their absolute difference is |15 - 17| = 2.

Function description

Diagonal Difference takes the following parameter:

int arr[n][m]: an array of integers Return

int: the absolute diagonal difference
"""
import random

matrix = []
def generateMatrix(n):
  if n < 2:
    print('Se debe generar una matriz de dimension minimo de 2x2 o más')

  for i in range(n):
    fila = []
    for j in range(n):
      valor_aleatorio = random.randint(1, 10)
      fila.append(valor_aleatorio)
    matrix.append(fila)

  return matrix

def diagonalDifference(arr):
  ls = 0
  rs = 0
  for i in range(len(arr)):
    if i == i:
      ls += arr[i][i]
    
  for j in range(3):
    #print(f'[{j}][{-j-1}] ')
    #print(matrix[j][-j-1])
    rs += arr[j][-j-1]
  print('diogonal ls', ls)
  print('diogonal rs', rs)
  sumTotal = abs(ls-rs)
  return sumTotal


# generar la misma matrix de forma más corta
# matriz_aleatoria = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
# for fila in matriz_aleatoria:

if __name__ == '__main__':

    n = int(input('De que tamaño quieres que sea tu matrix '))
    matrixGenerated = generateMatrix(n)
    for fila in matrixGenerated:
        print(fila)

    res = diagonalDifference(matrixGenerated)
    print('La diferencia de las diagonales es', res)
