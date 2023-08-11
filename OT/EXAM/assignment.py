from tabulate import tabulate   # tabulate data into tables
import numpy as np     



def substract_min(A):

    min_values = np.min(A,axis=1,keepdims=True)
    A = A - min_values

    min_values = np.min(A,axis=0,keepdims=True)
    A = A - min_values
    print("reduced matrix : ")
    print(A)
    print(" ")
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
    print("assigned matrix : ")                   
    print(A)
    print(" ")

def check_row(ind):

    global A
    r = []
    m = len(A)
    for i in range(m):
        if A[i,ind] == 0 :
            r.append(i)
    return r

def check_col(ind):
    global A

    c = []
    n = len(A[0])
    for i in range(n):
        if A[ind,i] == -1 :
            c.append(i)
    return c

def marking(A):

    row = []
    col = []
    m,n = A.shape
    con_or_not = True
    for i in range(m):
        if 0 not in A[i]:
            row.append(i)
    
    
    while con_or_not == True :

        lrow = len(row)
        lcol = len(col)
        con_or_not = False

        for i in row:
            c   = check_col(i)
            col = col + c
        col = list(set(col))
        if(len(col) != lcol):
            con_or_not = True

        for j in col:
            r   = check_row(j)
            row = row + r
        row = list(set(row))
        if(len(row) != lrow):
            con_or_not = True

    # print(row,col)
    return row,col

def update(A,row,col):   
    m,n = A.shape
    min_v = 999

    for i in range(m):
        for j in range(n):
            if (i in row) and (j not in col) and (A[i][j]<min_v):
                min_v = A[i][j]
    
    for i in range(m):
        for j in range(n):
            if (i in row) and (j not in col) :
                A[i][j] = A[i][j] - min_v

            elif (i not in row) and (j in col) :
                A[i][j] = A[i][j] + min_v
    print("updated matrix :")
    print(A)
    print(" ")

def hungarian_assignment():

    global A
    A = np.array([[18,26,17,11],[13,28,14,26],[38,19,18,15],[19,26,24,10]],dtype=float)
    m,n = A.shape
    v = 0
    A = substract_min(A)
    while(v<n):
        assign(A)
        row,col = marking(A)
        v = len(col) + m - len(row)
        if(v<n):
            for i in range(m):
                for j in range(n):
                    if A[i][j] == -1 :
                        A[i][j] = 0
            update(A,row,col)
        else: 
            break

hungarian_assignment()





