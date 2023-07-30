import numpy as np

np.set_printoptions(legacy='1.13')

a = list(map(float, input().split()))
a = np.array(a)

floor = np.floor(a)
ceiling = np.ceil(a)
rint = np.rint(a)

print(floor)
print(ceiling)
print(rint)
