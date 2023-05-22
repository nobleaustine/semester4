# importing required libraries
import numpy as np  # for performing matrix operations
import pandas as pd # for labeling the data and introducing a data frame
import re           # regular expressions for manipulating strings

# required functionalities
# funtions to convert inequalities to equalities by adding slack and substracing slack variables
def convertingToEquality(constraintsP,variablesP):  
    
    sVariableCount = 0  # count of slack or surplus variables
    equation = 0        # varible to store altered equation

    # adding slack or surplus variables and changing to equality
    # by iterating through constraintsP and checking for >/</>=/<= on each constraint
    # and modifing the constrints through constraint addition also using sVariableCount to count and update
    for i,constraint in enumerate(constraintsP):
            
            if(constraint.find(">")!=-1 or constraint.find(">=")!=-1):
                sVariableCount +=1;
                equation = constraint.find(">")
                constraint = constraint[0:equation-1] + ' + ' + f'-1s{sVariableCount}' + " = " + constraint[equation+1:len(constraint)]
                constraintsP[i]=constraint

            elif(constraint.find("<")!=-1 or constraint.find("<=")!=-1):
                sVariableCount +=1;
                equation = constraint.find("<")
                constraint = constraint[0:equation-1] + ' + ' + f'1s{sVariableCount}' + " = " + constraint[equation+1:len(constraint)]
                constraintsP[i]=constraint

    # getting set of all variables
    for constraint in constraintsP:
        for i, letter in enumerate(constraint):
            if(letter=="x"):
                variablesP.add(constraint[i:i+2])
            elif(letter=="s"):
                variablesP.add(constraint[i:i+2])

    # sorting variables in the order x1, x2, ...., s1, s2, ....
    tempVariables = list(sorted(variablesP))
    variablesModified= []
    for i in range(len(tempVariables)-sVariableCount):
        variablesModified.append(tempVariables[i+sVariableCount])

    for i in range(sVariableCount):
        variablesModified.append(tempVariables[i])
    
    # returning sorted list of variables
    return sVariableCount,variablesModified

# completing constraints by adding 0 as coefficient to the variables which are not present
def completeConstraints(constraintsP,variablesP):

    pos = 0 # position of "=" to add remaining variables
   
    for variable in variablesP:
        for i,constraint in enumerate(constraintsP):
                
                if(constraint.find(variable) ==-1):

                    pos = constraint.find(" = ")
                    constraint = constraint[0:pos] + ' + ' + f'0{variable}' + constraint[int(pos):int(len(constraint))]
                    constraintsP[i]=constraint
    
# completing the z relation by adding 0 as coefficient to the variables which are not present 
def completeZ(zValue,variablesP):

    # adding variables with zero as coefficients
    for variable in variablesP:
        if(zValue.find(variable) ==-1):
            zValue= zValue + ' + ' + f'0{variable}'
    return zValue

# extracting coefficients in the constraints                 
def extractCoefficients(tableP,constraintsP,variablesP):
    
    parts=[] # to store the parts of constraint split by "+"
    for i in range(len(variablesP)):

        coefficients=[]

        for constraint in constraintsP:

            parts = constraint.split('+')
            for element in parts:

                if(element.find(variablesP[i]) !=-1):

                    if(element.find('-') !=-1):
                        result=re.findall(r"\d+", element)
                        coefficients.append(int('-'+result[0]))
                    else:
                        result=re.findall(r"\d+", element)
                        coefficients.append(int(result[0]))

        tableP.append(coefficients )

# extracting coefficients of variables in z relation
def extractZ(zValue,tableP,variablesP):

    for i in range(len(variablesP)):
        parts = zValue.split('+')
        for element in parts:
            if(element.find(variablesP[i]) !=-1):
                result=re.findall(r"\d+", element)
                tableP.append(int(result[0]))

# extracting RHS of constraints 
def extractXb(tableP,constraintsP):

    for i in range(len(constraintsP)):
        result=re.findall(r"\d+", constraintsP[i])
        tableP.append(int(result[len(result)-1]))

# implementation of simplex method 
def simplexMethod(tableP,variablesP,CJ,S):

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
    
    for i in range(len(variablesP)-s+1):
        rowHead.append(variablesP[i+s-1])
        variable.append(variablesP[i+s-1])

    df = pd.DataFrame(tableP, index = rowHead,columns =columnHead)

    while(min(list(zj_cj))<0):
        
        zj_cj =[]
        zj = []
        count = count+1
        print("Iteration No : ",count)
        print(" ")
        print(df)
        print(" ")

        for i in range(tableP.shape[1]-2):
            value = np.multiply(tableP[:,0],tableP[:,i+2])
            zj.append(np.sum(value))
        
        zj_cj = np.subtract(zj,CJ)
        column = list(zj_cj).index(min(list(zj_cj)))
        column = column + 2

        xb_xj = np.divide(tableP[:,1],tableP[:,column])

        row = list(xb_xj).index(min(list(xb_xj)))


        variable[row] = variablesP[column -2]
        df = df.rename(index={df.index[row]: variablesP[column -2]})
        
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
         
        tableP[row,0]=cj[column-2]
        tableP[row,1:] = np.divide(tableP[row,1:],tableP[row,column])
        
        for i in range(tableP.shape[0]):
            if(i!=row):
                tableP[i,1:] = tableP[i,1:] - (tableP[i,column]/tableP[row,column])*tableP[row,1:] 

        for i,v in enumerate(variable): 
          df.loc[v] = tableP[i]

    print(" ")
    print("Final Table : ")  
    
    print(df)
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
    
#default values for testing : uncomment from 212-220 and  comment from 227-247 and
constraints=["2x1 + 1x2 < 50","2x1 + 5x2 < 100","2x1 + 3x2 < 90"]
z="4x1 + 10x2"

variables=set()
table = [] # table to take values of constraints
v =[]    # list of variables v as set defaultVariables can not be modified 
cj = []  # cj : coefficients of z
xb = []  # xb : RHS of constraints
s = 0    # s : no. of slack/surplus variables

print(" ")
print("------ Solving LPP using Simplex Method ------")
print(" ")

# requesting inputs
# getting the z relation to be optimized
# z = input(("Maximize/Minimize : "))
# print(" ")

# # getting the number of constraints
# constraintsCount = int(input("Enter the number of constraints : "))
# constraints = []
# print(" ")

# # getting constraints as user inputs
# print("Enter constraints of the form : w1x1 + w2x2 + ..... + wnxn ~ w0 where, ~ = >/</=/>=/<=")
# print(" ")
# for i in range (1,constraintsCount+1):
#     if(i==1):
#         constraint = str(input("Enter the 1st constraint : "))
#     elif(i==2):
#         constraint = str(input("Enter the 2nd constraint : "))
#     elif(i==3):
#         constraint = str(input("Enter the 3rd constraint : "))
#     else:
#         constraint = str(input(f"Enter the {constraintsCount}th constraint : "))
#     constraints.append(constraint)       
# print(" ")

# calling functions to test with default values uncomment for testing
s,v=convertingToEquality(constraints,variables)

completeConstraints(constraints,variables)
z=completeZ(z,variables)

extractCoefficients(table,constraints,v)
extractZ(z,cj,v)
extractXb(xb,constraints)

print("Modified LPP : Maximize/Minimize : ",z)
print(" ")
print("subject to :")
for constraint in constraints:
    print(constraint)
print(" ")

temp1 = np.array(table)
temp2= temp1.transpose()

initialCB=[]
for i in range(s):
    initialCB.append(float(0))

temp3 = np.concatenate((np.array(xb)[:, np.newaxis],temp2), axis=1)
Table = np.concatenate((np.array(initialCB)[:, np.newaxis], temp3), axis=1)


simplexMethod(Table,v,cj,s)








                



