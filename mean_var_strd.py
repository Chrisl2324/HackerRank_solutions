import numpy as np


n, m = map(int, input().split())
matrix = []
for i in range(n):
    elements = list(map(int, input().split()))
    matrix.append(np.array(elements))
    
matrix = np.array(matrix)
mean = np.mean(matrix, 1)
var = np.var(matrix, 0)
std = np.std(matrix)

print(mean)
print(var)
print(f'{std:.11f}')
    