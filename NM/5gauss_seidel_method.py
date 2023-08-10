import numpy as np

# [[45,2,3,58],[-3,22,2,47],[5,1,20,67]]

def gauss_seidel(A,it):
    m,n = A.shape
    n = n-1

    ans = np.zeros(m,dtype=float)
    count = 0
    while(count<it):
        for i in range(m):
            sum = 0
            for j in range(n):
                if(i != j):
                    sum = sum + ans[j]*A[i][j]
            ans[i] = round((A[i][n] - sum)/A[i][i],6)
        count +=1
    print("answer : ",ans)
            

A   =[]
row = []
r = int(input("number of variables : "))
c = int(input("number of equations : "))
it = int(input("number of iterations : "))
print("coefficients of equation :")
for i in range(r):
    row = [float(x) for x in input(f'   equation{i+1} : ').split()]
    A.append(row)

A = np.array(A,dtype=float)
A = np.array([[45,2,3,58],[-3,22,2,47],[5,1,20,67]],dtype=float)

print("matrix :")
print(A)

gauss_seidel(A,10)
