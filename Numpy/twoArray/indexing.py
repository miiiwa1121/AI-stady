import numpy as np

a = np.array([6,4,78,8,5,4,6,5,9,6,5,44])
a = a.reshape(3,4)

print(a)
print(a[0,0])
print(a[-1,-1])
print(a[0,:])
print(a[:,0])
print(a[:2,1:])
print(a[[0,1],[2,3]])
print(a[[[0,1]],[[2,3]]])

