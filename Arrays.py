import numpy as np


elements = list(map(int, input().split()))
elements.reverse()
array = np.array(elements, float)
print(array)
