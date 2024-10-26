import numpy as np

a = np.array([6,4,78,8,5,4,6,5,9,6,5,44,3,7])
idx = (a%3 == 0)

print(a[0])
print(a[-1])
print(a[[0,1,2]])
print(a[0:7])
print(a[0:7:2])
print(a[2:])
print(a[:5])
print(a[::2])
print(a[idx])

