import numpy as np  # for performing matrix operations
# import matplotlib.pyplot as plt

# x1 = np.array([0, 0, 1, 1])
# y1 = np.array([0, 1, 1, 0])

# plt.title("AND gate with perceptron")
# plt.xlabel("x coordinate")
# plt.ylabel("y coordinate")

# plt.plot(x1, y1)

# plt.grid(color = 'green', linestyle = '--')

# plt.show()
X = [[0,0,1],[0,1,1],[1,1,1],[1,0,1]]
X = np.array(X)
Y =[-1,-1,1,-1]
Y = np.array(Y)

def perceptron(X,Y):
    m = 1
    w = np.array([0,0,0])
    it = 0
    while(m>0):
        it = it + 1
        m = 0
        print("Iteration : ",it)
        print(" ")
        for i,x in enumerate(X) :

            print(f'y{i}wTx{i} = ',np.dot(w,x)*Y[i])
            
            if np.dot(w,x)*Y[i] <= 0 :
                w = w +Y[i]*x
                m = m + 1
            print("w = ",w)
            print(" ")
        print("-----------------------")
perceptron(X,Y)