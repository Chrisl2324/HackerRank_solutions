import numpy as np


n, m = map(int, input().split())

matrix = []
for i in range(n):
    elements = list(map(int, input().split()))
    elements = np.array(elements)
    matrix.append(elements)
matrix = np.array(matrix)
trans = np.transpose(matrix)
flat = matrix.flatten()
print(trans)
print(flat)