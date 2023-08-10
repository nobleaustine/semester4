# required libraries
import numpy as np

# [[2,1,-1,8],[-3,-1,2,-11],[-2,1,2,-3]]

A   =[]
row = []
r = int(input("number of variables : "))
c = int(input("number of equations : "))
print("coefficients of equation :")
for i in range(r):
    row = [float(x) for x in input(f'   equation{i+1} : ').split()]
    A.append(row)

A = np.array(A,dtype=float)

def gauss_jordan(A):
    m,n = A.shape
    n = n - 1
    for i in range(n-1):
        for j in range(i+1,m):
            k = A[j][i]/A[i][i]
            A[j] = A[j] - k*A[i]
    

    for i in range(n-1,0,-1):
        for j in range(i-1,-1,-1):
            k = A[j][i]/A[i][i]
            A[j] = A[j] - k*A[i]
    

    for i in range(n):
        k = 1/A[i][i]
        A[i] = k*A[i]
    
    ans = A[:,n]
    return ans

print("matrix :")
print(A)
ans = gauss_jordan(A)
print("answer : ")
print(ans)
