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

def gauss_elimination(A):
    m,n = A.shape
    n = n - 1
    for i in range(n-1):
        for j in range(i+1,m):
            k = A[j][i]/A[i][i]
            A[j] = A[j] - k*A[i]

def back_propogation(A):
    m,n = A.shape
    n = n-1
    ans = np.zeros(m,dtype=float)
    for i in range(m-1,-1,-1):
        sum = 0
        for j in range(i+1,n,1):
            sum = sum + ans[j]*A[i][j]
        ans[i] = (A[i][n] -sum)/A[i][i]
    return ans

print("matrix :")
print(A)
gauss_elimination(A)
ans =  back_propogation(A)

print("answer : ")
print(ans)
