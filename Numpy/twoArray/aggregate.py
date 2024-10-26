import numpy as np

a = np.array([[2, 4, 9], [375, 4, 743], [23, 62, 45743], [16, 43, 6]])
b = np.array([2, 1, 0])

print(np.max(a))
print(np.sum(a))
print(np.mean(a))
print(np.std(a))

print(np.max(a,axis=0))
print(np.sum(a,axis=0))
print(np.mean(a,axis=0))
print(np.std(a,axis=0))

print(np.max(a,axis=0,keepdims = True))
print(np.sum(a,axis=0,keepdims = True))
print(np.mean(a,axis=0,keepdims = True))
print(np.std(a,axis=0,keepdims = True))
