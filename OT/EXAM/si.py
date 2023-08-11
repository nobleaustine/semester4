import numpy as np
import pandas as pd

tableP = np.array([[0,50,2,1,1,0,0],[0,100,2,5,0,1,0],[0,90,2,3,0,0,1]])
variablesP = ["x1","x2","s1","s2","s3"]
CJ = [4,10,0,0,0]
S = 3
def simplexMethod(tableP,variablesP,CJ,s):

    # intializing variables
    columnHead = ["CB","XB"]
    rowHead = []
    variable = []
    zj_cj =[-1]
    column = 0
    row = 0
    count = 0
    zValue=0
    solution = {}

    for var in variablesP:
        columnHead.append(var)
    rowHead = ["s1","s2","s3"]
    
    # for i in range(len(variablesP)-s+1):
    #     rowHead.append(variablesP[i+s-1])
    variable = ["s1","s2","s3"]

    df = pd.DataFrame(tableP, index = rowHead,columns =columnHead)

    while(min(list(zj_cj))<0):
        
        zj_cj =[]
        zj = []
        count = count+1
        print("Iteration No : ",count)
        print(" ")
        # print(tabulate(df,tablefmt="grid",stralign="right", numalign="right"))
        print(" ")

        for i in range(tableP.shape[1]-2):
            value = np.multiply(tableP[:,0],tableP[:,i+2])
            zj.append(np.sum(value))
        
        zj_cj = np.subtract(zj,CJ)
        column = list(zj_cj).index(min(list(zj_cj)))
        column = column + 2

        # for i in range()
        xb_xj = np.divide(tableP[:,1],tableP[:,column])

        row = list(xb_xj).index(min(list(xb_xj)))


        variable[row] = variablesP[column -2]
        df = df.rename(index={df.index[row]: variablesP[column -1]})
        
        print("zj : ",zj)
        print(" ")
        print("zj-cj : ",zj_cj)
        print(" ")
        print("xb/xj : ",xb_xj)
        print(" ")

        print("row    : ",row)
        print("column : ",column)
        print("key    : ",tableP[row,column])
        print(" ")
        print("---------------------------------------------------------------------------------------------- ")
        print(" ")
         
        tableP[row,0]=CJ[column-2]
        tableP[row,1:] = np.divide(tableP[row,1:],tableP[row,column])
        
        for i in range(tableP.shape[0]):
            if(i!=row):
                tableP[i,1:] = tableP[i,1:] - (tableP[i,column]/tableP[row,column])*tableP[row,1:] 

        for i,v in enumerate(variable): 
          df.loc[v] = tableP[i]

    print(" ")
    print("Final Table : ")  
    
    print(df)
    # print(tabulate(df,tablefmt="grid",stralign="right", numalign="right"))
    print(" ")
    
    # printing solution
    print("Solution : ")
    print(" ")
    for i,var in enumerate(variable):
        print(var," = ",round(tableP[i,1],4))
        solution[var] = round(tableP[i,1],4)
    for var in variablesP:
        if(var in variable ):
            chomma = 0
        else:
            print(var," = 0")
            solution[var] = 0
    
    for i,var in enumerate(variable):
        zValue = zValue + solution[var]*CJ[i]

    print(" ")
    print("Optimum Value of Z : ",zValue)  
    print(" ") 
    print("---------------------------------------------------------------------------------------------- ")
   
simplexMethod(tableP,variablesP,CJ,S)