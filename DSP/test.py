import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

d = np.linalg.norm(a,2,keepdims=False)
r = np.linalg.norm(a)
print(d)
U,Z,V = np.linalg.svd(a)

print("A U = ")
print(U)
print("A Z = ")
print(Z)
print("A V = ")
print(V)

b = np.fft.fft2(a,norm='ortho')

u,z,v = np.linalg.svd(b)
print("B U = ")
print(u)
print("B Z = ")
print(z)
print("B V = ")
print(v)