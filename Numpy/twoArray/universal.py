import numpy as np

a = np.array([[2,4,9],[1,2,3],[6,6,6]])
b = np.array([2,1,0])
c = np.array([2,1,0,5,7,9])
c = c.reshape(3,2)

print(c)
print(c.shape)
print(a)
print(a.shape)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(np.dot(a,b))#内積
print(a==a)
print(a==b)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))

