import numpy as np  # for performing matrix operations

X = [[1,1,1],[1,0,1],[0,1,1],[0,0,1]]
Y =[1,-1,-1,-1]

def posetrion (x,y):
    m = 0
    w = np.array([0,0,0])
    i = 0
    while(i<x.len()):
        while(np.multiply(w,x[i])*y[i]<=0):
            w = w +y[i]*x[i]
            m = m + 1
        i = i + 1