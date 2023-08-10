import numpy as np
from sympy import *

table = np.array([[0,2,4,6,8,10],[0,4,56,204,496,980]])
for_table = []
def calc_fore_table(table):
    m,n = table.shape
    for_table = np.zeros((n,n+1),dtype=float)
    for i in range(n):
        for_table[i][0] = table[0][i]
        for_table[i][1] = table[1][i]
    for i in range(2,n):
        for j in range(0,abs(n-i)+1):
            for_table[j][i] = for_table[j+1][i-1] - for_table[j][i-1]
    
    print(for_table)

def get_u(xn):
    n = len(table[0])
    n = n-1
    for i in range(n,-1,-1):
        if(table[0][i] < xn):
            x0 = table[i]
    u = (xn - x0 )/(table[0][1]-table[0][0]) 

    return u  

# def calculate(u):
#     sum = 0
#     m,n = for_table.shape
#     for i in range(n):



calc_fore_table(table)
get_u(1)

