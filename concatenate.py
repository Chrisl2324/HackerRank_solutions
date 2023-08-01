import numpy as np


n, m, p = list(map(int, input().split()))
matrix1 = []
matrix2 = []
for i in range(n):
    elements = list(map(int, input().split()))
    elements = np.array(elements)
    matrix1.append(elements)
for j in range(m):
    elements = list(map(int, input().split()))
    elements = np.array(elements)
    matrix2.append(elements)

matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

print(np.concatenate((matrix1, matrix2)))
