import numpy as np


n, m = map(int, input().split())
array1 = []
array2 = []
for i in range(n):
    elements = list(map(int, input().split()))
    elements = np.array(elements)
    array1.append(elements)
for i in range(n):
    elements = list(map(int, input().split()))
    elements = np.array(elements)
    array2.append(elements)
    
array1 = np.array(array1)
array2 = np.array(array2)

tasks = [array1 + array2, array1 - array2, array1 * array2, np.floor_divide(array1, array2), array1%array2, array1**array2]
for task in tasks:
    print(task)
    


