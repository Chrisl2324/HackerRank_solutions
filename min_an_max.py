import numpy as np


n, m = map(int, input().split())

array = []
for i in range(n):
    values = list(map(int, input().split()))
    array.append(values)
    
array = np.array(array)

minimum_rows = np.min(array, axis=1)
maximum = np.max(minimum_rows)
print(maximum)