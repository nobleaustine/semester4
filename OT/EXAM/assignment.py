from tabulate import tabulate   # tabulate data into tables
import numpy as np     

A = np.array([[18,26,17,11],[13,28,14,26],[38,19,18,15],[19,26,24,10]],dtype=float)

def substract_min(A):

    min_values = np.min(A,axis=1,keepdims=True)
    A = A - min_values

    min_values = np.min(A,axis=0,keepdims=True)
    A = A - min_values
    
    print(A)
    return A

def assign(A):
    m,n = A.shape
    # ans = np.zeros(m,n,dtype=float)
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0 :
                for k in range(j+1,n):
                    if A[i][k] == 0 :
                        A[i][k] = -1
                for l in range(i+1,m):
                    if A[l][j] == 0 :
                        A[l][j] = -1
    print(A)

def marking(A):
    row = []
    col = []
    m,n = A.shape
    for i in range(m):
        if 0 not in A[i]:
            row.append(i)
    print(row)
        # for j in range(n):
        #     if A[i][j] == 0 :
        #         for k in range(j+1,n):
        #             if A[i][k] == 0 :
        #                 A[i][k] = -1
        #         for l in range(i+1,m):
        #             if A[l][j] == 0 :
        #                 A[l][j] = -1

A = substract_min(A)
assign(A)
marking(A)


