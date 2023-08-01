import numpy as np


elements = list(map(int, input().split()))
matrix = np.array(elements)
matrix.shape = (3, 3)
print(matrix)