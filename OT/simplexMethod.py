# importing required libraries
import numpy as np
import pandas as pd
import re

# # requesting inputs
# count = int(input("Enter the number of constraints : "))
# constrains = []
# variables = set()
# z = ""

# # getting constraints as user inputs
# for i in range (1,count+1):

#     if(i==1):
#         constrain = str(input("Enter the 1st constrain :"))
#     elif(i==2):
#         constrain = str(input("Enter the 2nd constrain :"))
#     elif(i==3):
#         constrain = str(input("Enter the 3rd constrain :"))
#     else:
#         constrain = str(input(f"Enter the {count}th constrain :"))
        
#     constrains.append(constrain)

# # getting the z equation to be optimized
# z = input(("Enter the z function :"))

#default values 
dconstrains=["2x1 + 1x2 < 50","2x1 + 5x2 < 100","2x1 + 3x2 < 90"]
dvariables=set()
z="4x1 + 10x2"
table = []
v =[]
cj = []
xb = []
s=0

print("actual constraints")
print(dconstrains)
print(" ")

print("actual z")
print(z)
print(" ")

# funtions to convert inequalities to equalities
def convertingToEquality(constrainsList,variableList):  

    SvariableCount = 0
    equ = 0
    # adding slack or surplus variables and changing to equality
    for i,string in enumerate(constrainsList):
            if(string.find(">")!=-1):
                SvariableCount +=1;
                equ = string.find(">")
                string = string[0:equ-1] + ' + ' + f'-1s{SvariableCount}' + " = " + string[equ+1:len(string)]
                constrainsList[i]=string
            elif(string.find("<")!=-1):
                SvariableCount +=1;
                equ = string.find("<")
                string = string[0:equ-1] + ' + ' + f'1s{SvariableCount}' + " = " + string[equ+1:len(string)]
                constrainsList[i]=string

    # getting list of all variables
    for j,string in enumerate(constrainsList):
        for i, letter in enumerate(string):
            if(letter=="x"):
                variableList.add(string[i:i+2])
            elif(letter=="s"):
                variableList.add(string[i:i+2])

    # sorting variables
    vList = list(sorted(variableList))
    variableList = []
    for i in range(len(vList)-SvariableCount):
        variableList.append(vList[i+SvariableCount])

    for i in range(SvariableCount):
        variableList.append(vList[i])
    
    # printing all variables
    return SvariableCount,variableList

# adding 0 as coefficient to the variables
def completeEquation(constrainsList,variableList):
    equ = 0
    # adding variables with zero as coefficients
    for variable in variableList:
        for j,string in enumerate(constrainsList):
                if(string.find(variable) ==-1):
                    equ = string.find(" = ")
                    string = string[0:equ] + ' + ' + f'0{variable}' + string[int(equ):int(len(string))]
                    constrainsList[j]=string
    
# completing z function
def completeZ(zValue,variableList):

    # adding variables with zero as coefficients
    for variable in variableList:
        if(zValue.find(variable) ==-1):
            zValue= zValue + ' + ' + f'0{variable}'
    return zValue

# extracting coefficients                   
def extract(tableList,constrainsList,variableList):
    
    coefficients=[]
    parts=[]
    for i in range(len(variableList)):
        coefficients=[]
        for string in constrainsList:
            parts = string.split('+')
            for element in parts:
                if(element.find(variableList[i]) !=-1):
                    if(element.find('-') !=-1):
                        result=re.findall(r"\d+", element)
                        coefficients.append(int('-'+result[0]))
                    else:
                        result=re.findall(r"\d+", element)
                        coefficients.append(int(result[0]))

        tableList.append(coefficients )

# extracting z function
def extractZ(zValue,tableList,variableList):
    for i in range(len(variableList)):
        parts = zValue.split('+')
        for element in parts:
            if(element.find(variableList[i]) !=-1):
                result=re.findall(r"\d+", element)
                tableList.append(int(result[0]))

def extractXb(tableList,constrainsList):
    for i in range(len(constrainsList)):
        result=re.findall(r"\d+", constrainsList[i])
        tableList.append(int(result[len(result)-1]))


# convertingToEquality(constrains,variables)
# completeEquation(constrains,variables)
# completeZ(z,variables)

#testing with default values
s,v=convertingToEquality(dconstrains,dvariables)
completeEquation(dconstrains,dvariables)
z=completeZ(z,dvariables)
extract(table,dconstrains,v)
extractZ(z,cj,v)
extractXb(xb,dconstrains)

print("final z")
print(z)
print(" ")

print("final constraints")
print(dconstrains)
print(" ")

print("cj")
print(cj)
print(" ")

print("table")
print(table)
print(" ")

print("variables")
print(v)
print(" ")

print("final xb")
print(xb)
print(" ")

temp1 = np.array(table)
temp2= temp1.transpose()

l=[]
for i in range(s):
    l.append(float(0))

workingTable = np.concatenate((np.array(xb)[:, np.newaxis],temp2), axis=1)
Table = np.concatenate((np.array(l)[:, np.newaxis], workingTable), axis=1)


print("Final Table : ")
print(Table)
print(" ")


def simplexMethod(T,V,C):

    # intializing variables
    columnHead = ["CB","XB","x1","x2","s1","s2","s3"]
    rowHead = ["s1","s2","s3"]
    variable = ["s1","s2","s3"]
    zj_cj =[-1]
    column = 0
    row = 0
    df = pd.DataFrame(T, index = rowHead,columns =columnHead)

    while(min(list(zj_cj))<0):
        zj_cj =[]
        zj = []

        print("calculating zj")
        for i in range(T.shape[1]-2):
            print(T[:,0],T[:,i+2])
            print(" ")
            value = np.multiply(T[:,0],T[:,i+2])
            zj.append(np.sum(value))
        
        print("zj : ",end="")
        print(zj)
        print(" ")

        zj_cj = np.subtract(zj,C)
        column = list(zj_cj).index(min(list(zj_cj)))
        column = column + 2

        xb_xj = np.divide(T[:,1],T[:,column])

        row = list(xb_xj).index(min(list(xb_xj)))


        variable[row] = V[column -2]
        df = df.rename(index={df.index[row]: V[column -2]})

        print("zj_cj : ",zj_cj)
        print(" ")
        print("xb_xj",xb_xj)
        print(" ")

        print("row  : ",row)
        print("column : ",column)
        print("key : ",Table[row,column])
        print(" ")
        
        print("Making key value 1")
        T[row,0]=cj[column-2]
        T[row,1:] = np.divide(T[row,1:],T[row,column])
        print(T)
        print(" ")

        print("Making column values to 0 ")
        for i in range(T.shape[0]):
            if(i!=row):
                T[i,1:] = T[i,1:] - (T[i,column]/T[row,column])*T[row,1:] 

        for i,v in enumerate(variable): 
          df.loc[v] = T[i]    
        print(df)
        print(" ")

def printResult(T,V,C):
    R =[]
    for i in range(len(C)):
        for value in T[:,1]:
            if(value==i):
                R.append(value)
    


simplexMethod(Table,v,cj)








                



